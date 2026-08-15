#!/usr/bin/env python3
"""Add an exact vertical Chinese inscription without regenerating the image."""

from __future__ import annotations

import argparse
import io
import os
from pathlib import Path
import tempfile

from PIL import Image, ImageCms, ImageDraw, ImageFont, ImageOps


class InscriptionError(ValueError):
    """Raised when inscription inputs or rendering options are invalid."""


FONT_CANDIDATES = (
    Path("C:/Windows/Fonts/STXINGKA.TTF"),
    Path("C:/Windows/Fonts/STKAITI.TTF"),
    Path("C:/Windows/Fonts/simkai.ttf"),
    Path("/System/Library/Fonts/Supplemental/Kaiti.ttc"),
    Path("/System/Library/Fonts/Kaiti.ttc"),
    Path("/Library/Fonts/Kaiti.ttc"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add an exact, seal-free vertical Chinese inscription to an image."
    )
    parser.add_argument("--input", required=True, type=Path, help="Finished image path")
    parser.add_argument("--out", required=True, type=Path, help="New output image path")
    parser.add_argument("--text", required=True, help="Exact Chinese inscription")
    parser.add_argument("--font", type=Path, help="Optional licensed xingkai/kaiti font")
    parser.add_argument(
        "--placement",
        choices=("upper-left", "upper-right", "lower-left", "lower-right"),
        default="upper-right",
    )
    parser.add_argument(
        "--size-ratio",
        type=float,
        default=0.032,
        help="Font size as a fraction of the image short edge (default: 0.032)",
    )
    parser.add_argument(
        "--margin-ratio",
        type=float,
        default=0.09,
        help="Outer margin as a fraction of the image short edge (default: 0.09)",
    )
    parser.add_argument(
        "--spacing-ratio",
        type=float,
        default=0.22,
        help="Inter-character spacing relative to font size (default: 0.22)",
    )
    parser.add_argument(
        "--ink",
        default="#3B3935",
        help="Ink color as #RGB or #RRGGBB (default: #3B3935)",
    )
    parser.add_argument(
        "--opacity",
        type=int,
        default=215,
        help="Ink opacity from 1 to 255 (default: 215)",
    )
    return parser.parse_args()


def parse_color(value: str) -> tuple[int, int, int]:
    text = value.strip().lstrip("#")
    if len(text) == 3:
        text = "".join(character * 2 for character in text)
    if len(text) != 6:
        raise InscriptionError("--ink must be #RGB or #RRGGBB")
    try:
        return tuple(int(text[index : index + 2], 16) for index in (0, 2, 4))
    except ValueError as exc:
        raise InscriptionError("--ink contains a non-hexadecimal value") from exc


def validate_text(value: str) -> str:
    text = "".join(value.split())
    if not text:
        raise InscriptionError("--text cannot be empty")
    if len(text) > 12:
        raise InscriptionError("--text supports at most 12 characters in one column")
    cjk_ranges = (
        (0x3400, 0x4DBF),
        (0x4E00, 0x9FFF),
        (0xF900, 0xFAFF),
        (0x20000, 0x2FA1F),
    )
    if any(
        not any(start <= ord(character) <= end for start, end in cjk_ranges)
        for character in text
    ):
        raise InscriptionError("--text must contain Chinese characters only")
    return text


def resolve_font(explicit: Path | None, size: int) -> tuple[ImageFont.FreeTypeFont, Path]:
    candidates = (explicit,) if explicit else FONT_CANDIDATES
    for candidate in candidates:
        if candidate and candidate.is_file():
            try:
                return ImageFont.truetype(str(candidate), size=size), candidate
            except OSError:
                continue
    if explicit:
        raise InscriptionError(f"cannot load font: {explicit}")
    raise InscriptionError(
        "no compatible local xingkai/kaiti font found; pass --font with a licensed font"
    )


def convert_to_srgb(image: Image.Image, icc_profile: bytes | None) -> Image.Image:
    if icc_profile:
        try:
            source_profile = ImageCms.ImageCmsProfile(io.BytesIO(icc_profile))
            srgb_profile = ImageCms.createProfile("sRGB")
            return ImageCms.profileToProfile(
                image, source_profile, srgb_profile, outputMode="RGBA"
            )
        except (ImageCms.PyCMSError, OSError, ValueError):
            pass
    return image.convert("RGBA")


def load_image(path: Path) -> Image.Image:
    if not path.is_file():
        raise InscriptionError(f"image does not exist: {path}")
    try:
        with Image.open(path) as source:
            icc_profile = source.info.get("icc_profile")
            oriented = ImageOps.exif_transpose(source)
            oriented.load()
            return convert_to_srgb(oriented, icc_profile)
    except (OSError, ValueError) as exc:
        raise InscriptionError(f"cannot read image: {path}") from exc


def measure_column(
    text: str,
    font: ImageFont.FreeTypeFont,
    spacing: int,
) -> tuple[int, int, list[tuple[int, int, int, int]]]:
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    boxes = [probe.textbbox((0, 0), character, font=font) for character in text]
    widths = [right - left for left, _, right, _ in boxes]
    heights = [bottom - top for _, top, _, bottom in boxes]
    width = max(widths)
    height = sum(heights) + spacing * (len(text) - 1)
    return width, height, boxes


def resolve_position(
    image_size: tuple[int, int],
    column_size: tuple[int, int],
    margin: int,
    placement: str,
) -> tuple[int, int]:
    image_width, image_height = image_size
    column_width, column_height = column_size
    left = margin if placement.endswith("left") else image_width - margin - column_width
    top = margin if placement.startswith("upper") else image_height - margin - column_height
    if left < 0 or top < 0:
        raise InscriptionError("inscription does not fit; reduce --size-ratio or text length")
    return left, top


def render_inscription(
    image: Image.Image,
    text: str,
    font: ImageFont.FreeTypeFont,
    placement: str,
    margin: int,
    spacing: int,
    ink: tuple[int, int, int],
    opacity: int,
) -> Image.Image:
    column_width, column_height, boxes = measure_column(text, font, spacing)
    origin_x, origin_y = resolve_position(
        image.size, (column_width, column_height), margin, placement
    )
    layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    cursor_y = origin_y
    for character, box in zip(text, boxes):
        left, top, right, bottom = box
        glyph_width = right - left
        glyph_height = bottom - top
        x = origin_x + (column_width - glyph_width) // 2 - left
        y = cursor_y - top
        draw.text((x, y), character, font=font, fill=(*ink, opacity))
        cursor_y += glyph_height + spacing
    return Image.alpha_composite(image, layer)


def save_non_destructive(image: Image.Image, output: Path) -> None:
    if output.exists():
        raise InscriptionError(f"refusing to overwrite existing output: {output}")
    suffix = output.suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".webp"}:
        raise InscriptionError("--out extension must be .png, .jpg, .jpeg, or .webp")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            prefix=f".{output.stem}-",
            suffix=suffix,
            dir=output.parent,
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
        save_image = image if suffix == ".png" else image.convert("RGB")
        options: dict[str, object] = {}
        if suffix in {".jpg", ".jpeg"}:
            options.update(quality=95, subsampling=0, optimize=True)
        elif suffix == ".webp":
            options.update(quality=95, method=6)
        save_image.save(temporary_path, **options)
        os.replace(temporary_path, output)
    finally:
        if temporary_path and temporary_path.exists():
            temporary_path.unlink()


def main() -> int:
    args = parse_args()
    try:
        text = validate_text(args.text)
        if not 0.012 <= args.size_ratio <= 0.08:
            raise InscriptionError("--size-ratio must be between 0.012 and 0.08")
        if not 0.02 <= args.margin_ratio <= 0.25:
            raise InscriptionError("--margin-ratio must be between 0.02 and 0.25")
        if not 0 <= args.spacing_ratio <= 1:
            raise InscriptionError("--spacing-ratio must be between 0 and 1")
        if not 1 <= args.opacity <= 255:
            raise InscriptionError("--opacity must be between 1 and 255")
        if args.input.resolve() == args.out.resolve():
            raise InscriptionError("--out cannot replace the input image")

        image = load_image(args.input)
        short_edge = min(image.size)
        font_size = max(12, round(short_edge * args.size_ratio))
        margin = max(8, round(short_edge * args.margin_ratio))
        spacing = max(0, round(font_size * args.spacing_ratio))
        font, font_path = resolve_font(args.font, font_size)
        output = render_inscription(
            image,
            text,
            font,
            args.placement,
            margin,
            spacing,
            parse_color(args.ink),
            args.opacity,
        )
        save_non_destructive(output, args.out)
    except InscriptionError as exc:
        raise SystemExit(f"error: {exc}") from exc

    print(f"output={args.out.resolve()}")
    print(f"font={font_path.resolve()}")
    print(f"text={text}")
    print(f"placement={args.placement}")
    print(f"size={output.width}x{output.height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
