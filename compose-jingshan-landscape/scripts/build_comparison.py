#!/usr/bin/env python3
"""Build a deterministic before/after image without generative alteration."""

from __future__ import annotations

import argparse
import io
import os
from pathlib import Path
import tempfile

from PIL import Image, ImageCms, ImageDraw, ImageFont, ImageOps


class ComparisonError(ValueError):
    """Raised when comparison inputs or options are invalid."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compose an exact source image and finished image into a comparison board."
    )
    parser.add_argument("--before", required=True, type=Path, help="Source image path")
    parser.add_argument("--after", required=True, type=Path, help="Finished image path")
    parser.add_argument("--out", required=True, type=Path, help="New output image path")
    parser.add_argument(
        "--layout",
        choices=("auto", "stacked", "side-by-side"),
        default="auto",
        help="Auto stacks portrait results and places landscape results side by side",
    )
    parser.add_argument(
        "--gap",
        default="2%",
        help="Gap in pixels, or a percent of the shared panel dimension (default: 2%%)",
    )
    parser.add_argument(
        "--background",
        default="#E4E0D5",
        help="Board background as #RGB or #RRGGBB (default: #E4E0D5)",
    )
    parser.add_argument(
        "--labels",
        choices=("none", "auto", "custom"),
        default="none",
        help="Optional labels; auto uses BEFORE and AFTER",
    )
    parser.add_argument("--before-label", help="Exact custom source label")
    parser.add_argument("--after-label", help="Exact custom finished label")
    return parser.parse_args()


def parse_color(value: str) -> tuple[int, int, int]:
    text = value.strip().lstrip("#")
    if len(text) == 3:
        text = "".join(character * 2 for character in text)
    if len(text) != 6:
        raise ComparisonError("--background must be #RGB or #RRGGBB")
    try:
        return tuple(int(text[index : index + 2], 16) for index in (0, 2, 4))
    except ValueError as exc:
        raise ComparisonError("--background contains a non-hexadecimal value") from exc


def parse_gap(value: str, basis: int) -> int:
    text = value.strip()
    try:
        if text.endswith("%"):
            percent = float(text[:-1])
            if percent < 0 or percent > 25:
                raise ComparisonError("percentage --gap must be between 0% and 25%")
            return round(basis * percent / 100)
        pixels = int(text)
    except ValueError as exc:
        raise ComparisonError("--gap must be an integer pixel value or percentage") from exc
    if pixels < 0:
        raise ComparisonError("pixel --gap cannot be negative")
    return pixels


def convert_to_srgb(image: Image.Image, icc_profile: bytes | None) -> Image.Image:
    has_alpha = "A" in image.getbands()
    output_mode = "RGBA" if has_alpha else "RGB"
    if icc_profile:
        try:
            source_profile = ImageCms.ImageCmsProfile(io.BytesIO(icc_profile))
            srgb_profile = ImageCms.createProfile("sRGB")
            return ImageCms.profileToProfile(
                image,
                source_profile,
                srgb_profile,
                outputMode=output_mode,
            )
        except (ImageCms.PyCMSError, OSError, ValueError):
            pass
    return image.convert(output_mode)


def load_image(path: Path) -> Image.Image:
    if not path.is_file():
        raise ComparisonError(f"image does not exist: {path}")
    try:
        with Image.open(path) as source:
            icc_profile = source.info.get("icc_profile")
            oriented = ImageOps.exif_transpose(source)
            oriented.load()
            return convert_to_srgb(oriented, icc_profile)
    except (OSError, ValueError) as exc:
        raise ComparisonError(f"cannot read image: {path}") from exc


def flatten(image: Image.Image, background: tuple[int, int, int]) -> Image.Image:
    if image.mode == "RGB":
        return image
    canvas = Image.new("RGBA", image.size, (*background, 255))
    canvas.alpha_composite(image.convert("RGBA"))
    return canvas.convert("RGB")


def resize_to_width(image: Image.Image, width: int) -> Image.Image:
    if image.width == width:
        return image.copy()
    height = max(1, round(image.height * width / image.width))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def resize_to_height(image: Image.Image, height: int) -> Image.Image:
    if image.height == height:
        return image.copy()
    width = max(1, round(image.width * height / image.height))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def find_font(size: int, requires_unicode: bool) -> ImageFont.ImageFont:
    candidates = (
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/simsun.ttc"),
        Path("/System/Library/Fonts/PingFang.ttc"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    )
    for candidate in candidates:
        if candidate.is_file():
            try:
                return ImageFont.truetype(str(candidate), size=size)
            except OSError:
                continue
    if requires_unicode:
        raise ComparisonError("custom non-ASCII labels require an installed Unicode font")
    return ImageFont.load_default()


def add_label_band(
    image: Image.Image,
    label: str | None,
    background: tuple[int, int, int],
) -> Image.Image:
    if not label:
        return image
    font_size = max(14, round(min(image.size) * 0.035))
    font = find_font(font_size, any(ord(character) > 127 for character in label))
    padding = max(10, round(font_size * 0.7))
    probe = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    left, top, right, bottom = probe.textbbox((0, 0), label, font=font)
    band_height = bottom - top + padding * 2
    labeled = Image.new("RGB", (image.width, image.height + band_height), background)
    labeled.paste(image, (0, band_height))
    draw = ImageDraw.Draw(labeled)
    text_width = right - left
    draw.text(
        ((image.width - text_width) // 2 - left, padding - top),
        label,
        fill=(55, 52, 46),
        font=font,
    )
    return labeled


def resolve_labels(args: argparse.Namespace) -> tuple[str | None, str | None]:
    if args.labels == "none":
        return None, None
    if args.labels == "auto":
        return "BEFORE", "AFTER"
    if args.before_label is None or args.after_label is None:
        raise ComparisonError(
            "--labels custom requires --before-label and --after-label"
        )
    return args.before_label, args.after_label


def compose_stacked(
    before: Image.Image,
    after: Image.Image,
    gap_value: str,
    background: tuple[int, int, int],
    before_label: str | None,
    after_label: str | None,
) -> Image.Image:
    shared_width = min(before.width, after.width)
    before_panel = add_label_band(
        resize_to_width(before, shared_width), before_label, background
    )
    after_panel = add_label_band(
        resize_to_width(after, shared_width), after_label, background
    )
    gap = parse_gap(gap_value, shared_width)
    board = Image.new(
        "RGB",
        (shared_width, after_panel.height + gap + before_panel.height),
        background,
    )
    board.paste(after_panel, (0, 0))
    board.paste(before_panel, (0, after_panel.height + gap))
    return board


def compose_side_by_side(
    before: Image.Image,
    after: Image.Image,
    gap_value: str,
    background: tuple[int, int, int],
    before_label: str | None,
    after_label: str | None,
) -> Image.Image:
    shared_height = min(before.height, after.height)
    before_panel = add_label_band(
        resize_to_height(before, shared_height), before_label, background
    )
    after_panel = add_label_band(
        resize_to_height(after, shared_height), after_label, background
    )
    panel_height = max(before_panel.height, after_panel.height)
    gap = parse_gap(gap_value, shared_height)
    board = Image.new(
        "RGB",
        (before_panel.width + gap + after_panel.width, panel_height),
        background,
    )
    board.paste(before_panel, (0, (panel_height - before_panel.height) // 2))
    board.paste(
        after_panel,
        (before_panel.width + gap, (panel_height - after_panel.height) // 2),
    )
    return board


def save_non_destructive(image: Image.Image, output: Path) -> None:
    if output.exists():
        raise ComparisonError(f"refusing to overwrite existing output: {output}")
    if output.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
        raise ComparisonError("--out extension must be .png, .jpg, .jpeg, or .webp")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            prefix=f".{output.stem}-",
            suffix=output.suffix,
            dir=output.parent,
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
        save_options: dict[str, object] = {}
        if output.suffix.lower() in {".jpg", ".jpeg"}:
            save_options.update(quality=95, subsampling=0, optimize=True)
        elif output.suffix.lower() == ".webp":
            save_options.update(quality=95, method=6)
        image.save(temporary_path, **save_options)
        os.replace(temporary_path, output)
    finally:
        if temporary_path and temporary_path.exists():
            temporary_path.unlink()


def main() -> int:
    args = parse_args()
    try:
        if args.before.resolve() == args.after.resolve():
            raise ComparisonError("--before and --after must be different files")
        if args.out.resolve() in {args.before.resolve(), args.after.resolve()}:
            raise ComparisonError("--out cannot replace an input image")

        background = parse_color(args.background)
        before_label, after_label = resolve_labels(args)
        before = flatten(load_image(args.before), background)
        after = flatten(load_image(args.after), background)
        layout = args.layout
        if layout == "auto":
            layout = "stacked" if after.height >= after.width else "side-by-side"

        if layout == "stacked":
            board = compose_stacked(
                before,
                after,
                args.gap,
                background,
                before_label,
                after_label,
            )
        else:
            board = compose_side_by_side(
                before,
                after,
                args.gap,
                background,
                before_label,
                after_label,
            )
        save_non_destructive(board, args.out)
    except ComparisonError as exc:
        raise SystemExit(f"error: {exc}") from exc

    print(f"output={args.out.resolve()}")
    print(f"layout={layout}")
    print(f"size={board.width}x{board.height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
