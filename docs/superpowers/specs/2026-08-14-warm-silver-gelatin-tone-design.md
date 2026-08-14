# Warm Silver-Gelatin Tone Design

## Goal

Refine the default `silver-gelatin` mode and public comparison example so they read as restrained warm-gray photographic prints rather than neutral digital grayscale or cream zine paper.

The direction is informed by Lang Jingshan photographs in the National Museum of History collection and the museum record for `Lake and Mountain Scenery`:

- https://artistsday.nmh.gov.tw/art9.html
- https://www.nmh.gov.tw/News_Publish_Content.aspx?n=6998&s=174527

Online reproductions vary with scan, print, paper age, and display. The Skill therefore interprets the common tonal character rather than copying the yellow cast of any single reproduction.

## Tonal Direction

The target is a subtly warm silver-gelatin or restrained selenium-like print:

- luminous ivory highlights rather than digital white;
- low-saturation warm-gray middle tones;
- charcoal shadows and a small amount of deep photographic black;
- clear separation between foreground, middle distance, and pale atmospheric distance;
- no uniform brown wash and no yellow paper filter.

The deterministic comparison board uses `#E4E0D5` as its default pale ivory-gray support color. This exact value applies only to layout pixels, not as a mandatory generation color.

## Image Edit

Edit only the generated `AFTER` artwork used in the public demonstration. Preserve the complete 5:3 composition, shoreline, person, path, reeds, water, mountain geometry, focus, and grain.

Change only the tonal family:

- move cool neutral whites toward soft ivory;
- move middle grays toward a subtle warm stone-gray;
- retain charcoal and deep black without crushing foliage detail;
- keep the cast barely perceptible and photographic;
- avoid sepia, tobacco brown, orange, green, cyan, stains, foxing, vignette, paper fibers, or antique-frame effects.

Rebuild the comparison board from the unchanged demonstration source and the revised result using the deterministic script. Do not ask the image model to redraw the board.

## Skill Rules

Update `silver-gelatin` consistently in the Skill, visual grammar, layered guidance, portable prompt, READMEs, and evaluation cases.

The mode remains monochrome. Warm-gray paper tone is not counted as `source-tint` and must not introduce a colored object or second accent hue.

Add a correction rule: if the result reads as sepia nostalgia, yellow rice paper, or a generic antique photograph, neutralize the yellow/brown cast while preserving the slight warm-gray print base.

## Distribution

Publish the refinement as `v1.1.1`:

- replace the repository comparison media at the existing stable path;
- keep demonstration media outside the installable ZIP;
- retain the six-file Skill package layout;
- synchronize the installed local Skill;
- verify the downloaded release asset hash against the local package.

## Success Criteria

- The `AFTER` image feels subtly warmer than neutral grayscale but does not read as sepia.
- Highlights remain luminous, middle distances remain separated, and deep blacks retain detail.
- The board background supports the image without resembling cream scrapbook paper.
- All documentation uses the same warm silver-gelatin definition.
- The public README image, local installed Skill, repository source, and `v1.1.1` release are synchronized.
