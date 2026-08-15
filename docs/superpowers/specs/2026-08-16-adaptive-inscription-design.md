# Adaptive Chinese Inscription Design

## Goal

Add optional vertical Chinese inscriptions to all three creative paths without turning the Skill into a calligraphy poster generator or allowing text generation to alter a completed photograph.

## Decision model

Treat inscription as a fourth independent decision axis:

- `inscription-none`: default, no image text.
- `inscription-exact`: use the user's exact Chinese text.
- `inscription-auto`: create a two-to-six-character scene phrase only when the user requests text without supplying it.

Keep `seal-none` permanent. Do not generate seals, signatures, author names, dates, English microtext, or site watermarks.

## Rendering

Use `auto` by default. Complete and lock the no-text artwork first. If the host supports isolated transparent image generation, attempt one AI inscription layer using a restrained small-running-script colophon treatment informed by Lang Jingshan's works without copying his signature or personal handwriting.

Accept the AI layer only when the Chinese text and order are exact, the style remains readable and restrained, no extra content appears, the layer is genuinely transparent, and the underlying image is unchanged. Otherwise discard it and use deterministic xingkai/kaiti rendering.

Support explicit `ai` and `font` rendering choices. `ai` fails cleanly when validation fails. `font` skips generation and uses the deterministic script.

## Deterministic fallback

Bundle `scripts/add_inscription.py`, using Pillow and locally installed fonts. Discover compatible Windows and macOS xingkai/kaiti fonts, or accept an explicit licensed font path. Do not redistribute system fonts. Refuse to overwrite the source image or render with a font that cannot support the requested Chinese text.

## Placement and quality

Use one vertical column in a real blank area, normally two to six characters, charcoal or deep warm-gray ink, and about 1.5% to 3% visual weight. Keep the inscription as second-look information and an eye-path endpoint. Avoid faces, architecture details, mountain silhouettes, dense textures, centered titles, paper labels, borders, shadows, and colored text.

Validate exact text, direction, placement, scale, absence of seals and signatures, and preservation of every non-inscription image region. If neither the AI layer nor deterministic rendering is available, return the no-text artwork plus the proposed inscription and explain the limitation.
