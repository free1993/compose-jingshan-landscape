# Photo Role and Aspect Routing Design

## Goal

Evolve `compose-jingshan-landscape` without splitting it into separate installable Skills. The Skill will support three clearly separated ways to use a source photograph, route portrait and landscape subjects to suitable canvases, and retain its Lang Jingshan-inspired photographic identity.

The design independently adapts two useful method-level distinctions observed in Zeejay0's Gathered Scenes Zine project:

- a source photograph can remain visibly present as a truthful photographic anchor;
- a source photograph can instead act only as semantic evidence for a fully reconstructed artwork.

No prompt language, protected configuration text, or distinctive parameter wording will be copied. The reference project uses a personal non-commercial license, while this project is MIT-licensed.

## Approved Architecture

Keep one public Skill and one installation name:

```text
compose-jingshan-landscape
```

Add a third processing mode inside that Skill. Do not create a second repository, second `SKILL.md`, or competing trigger description.

### Processing Modes

| Mode | Source-photo role | Final-image requirement |
| --- | --- | --- |
| `jingshan-single` | Photographic subject and factual anchor | A standalone pictorial photograph that preserves identity, action, geometry, and believable photographic material |
| `jingshan-layered` | Visible photographic anchor inside an interpreted field | One artwork where a recognizable real-scene core meets mist, paper white, composite landscape space, and restrained material transitions |
| `jingshan-distilled` | Semantic and compositional evidence only | A newly reconstructed pictorial artwork with no embedded photo fragment, photo window, literal crop, or retained photographic region |

`jingshan-single` remains the default. `jingshan-layered` and `jingshan-distilled` require explicit user intent or strong unambiguous wording. Automatic routing must never choose distillation when the user asks to preserve a person, exact object, documentary event, or location faithfully.

The existing presentation modes remain independent:

- `artwork-only` returns the selected artwork mode;
- `before-after` returns the artwork and a deterministic source/result comparison board;
- a layered comparison combines `jingshan-layered` with `before-after`.

The comparison board is the only output that always contains the exact supplied source pixels. A generative layered artwork must be described as containing a recognizable photographic anchor, not as guaranteeing byte-identical source pixels unless the host provides deterministic image compositing or masking.

## Alternatives Considered

### Separate Skills

Create one Skill for photographic collage and another for distillation. This improves conceptual separation but creates overlapping triggers, duplicates shared Lang Jingshan rules, complicates installation, and weakens exact-name discovery. Reject this approach.

### Fold Distillation Into `jingshan-single`

Treat distillation as a strength parameter inside the default single-image mode. This reduces the number of modes but makes the critical no-photo boundary ambiguous and increases accidental loss of identity. Reject this approach.

### One Skill With Three Modes

Keep a single shared visual grammar and expose three source-photo roles. This preserves the existing repository and user mental model while making the no-photo rule testable. This is the approved approach.

## Aspect-Ratio Router

`3:5` is an aspect ratio, not an encoded image format. The Skill must no longer describe every artwork as vertical `3:5`.

Apply this priority order:

1. Honor an explicit user ratio or orientation.
2. Use portrait `3:5` for portrait sources, vertical subjects, figures, branches, vessels, architecture with upward movement, and ambiguous or square scenes.
3. Use landscape `5:3` when the source is horizontal or the subject depends on lateral movement, water, ridges, roads, layered distance, or Chinese landscape-style roaming observation.
4. Preserve the original ratio only when the user requests it or when changing it would destroy essential framing.

Supported explicit ratios are:

- `3:5` portrait, the default mobile-friendly house format;
- `5:3` landscape, the horizontal counterpart and default for expansive scenery;
- `4:5` and `2:3` for conventional portrait publishing or photographic framing;
- `3:2` and `16:9` for broad landscapes;
- `1:1` for deliberately compact, seal-like, or centered small scenes;
- `9:16` for an explicitly requested phone wallpaper or story format;
- `original` for composition-preserving output.

Do not choose a non-house ratio randomly. When the user does not specify a ratio, route only between `3:5` and `5:3`, with `original` used solely to protect essential framing.

All generated modes use the selected artwork ratio. The deterministic comparison script must contain both source and result without cropping, regardless of their differing ratios.

## Visual Translation Rules

The reference project's collage and distillation concepts must be translated into this Skill's existing visual language rather than imported as a zine aesthetic.

### Shared Lang Jingshan Grammar

All three modes retain:

- composite-photography reasoning and a credible photographic base;
- high, deep, and level-distance organization where the subject supports it;
- mist, air, paper white, and the meaningful unpainted area as spatial structure;
- silver-gelatin, source-tint, or muted-original color modes;
- source identity, semantic minimums, and restrained invention;
- the historical-homage note to Lang Jingshan in documentation;
- the `junhaogege_` author line in Skill source and repository documentation, never in the generated image or default response.

### Real-Scene Layering

`jingshan-layered` absorbs the useful photo-anchor principle but replaces default torn-paper zine treatment with:

- mist dissolution;
- exposed paper white;
- soft silver-gelatin density transitions;
- mountain, branch, water, or architectural contours that continue across the boundary;
- one coherent shared visual skeleton between the photographic anchor and interpreted field.

A hand-torn paper seam may appear only when the user explicitly asks for a modern paper-collage variant. High-chroma structural color is not the default because it conflicts with the quiet tonal hierarchy of the Skill.

### Jingshan Distillation

`jingshan-distilled` must first extract a compact distillation card:

- semantic nucleus;
- factual anchors that must remain recognizable in newly generated form;
- emotional tension;
- dominant spatial gesture;
- one source-derived visual metaphor when justified;
- intentional omissions;
- desired interpretive opening.

The final prompt must identify the source as a semantic reference only and prohibit photo fragments, photorealistic windows, literal crops, tracing, rotoscoping, and source-composition copying. The output remains pictorial photography rather than generic illustration, ink-wash filtering, scrapbook collage, or editorial poster design.

## Color and Material

Input color remains unrestricted. Continue to analyze source color by semantic role, value structure, temperature, and atmosphere.

- `silver-gelatin` remains the default.
- `source-tint` may retain one meaningful low-saturation source color.
- `muted-original` may preserve a restrained version of the source palette when color is essential to identity or season.
- Do not adopt a mandatory high-chroma accent from the reference project.
- Do not add a second accent hue or a detached decorative color block.

Distillation changes the role of the photograph, not the core color system.

## Prompt and Trigger Routing

Natural-language intent takes priority over internal mode names.

Examples that route to `jingshan-single`:

- "Use the Lang Jingshan approach to edit this photograph."
- "Keep the person and scene truthful, but strengthen mist and unpainted space."

Examples that route to `jingshan-layered`:

- "Keep a recognizable real-photo core and let it dissolve into a Jingshan landscape."
- "Create a real-scene layered collage in the existing Chinese pictorial style."

Examples that route to `jingshan-distilled`:

- "Use this photo only as inspiration and fully distill it into a Jingshan artwork."
- "Do not retain any original photo fragment; reconstruct its emotion and spatial gesture."

When intent is ambiguous, preserve photography and choose `jingshan-single`. Never silently remove the source photograph.

## Output Contract

Return the generated artwork plus one short creative rationale by default. Do not reveal the full generation prompt unless the user asks for it.

For `before-after`, return:

1. the selected generated artwork;
2. a deterministic comparison board produced by the existing script;
3. one concise explanation of what was preserved and transformed.

PNG is preferred for paper texture, fine tonal transitions, and small text when the host supports output-format control. JPEG may be supplied for sharing when requested. If the host controls encoding, the Skill must not promise a file type it cannot enforce.

## Documentation and Distribution Changes

Implementation will update:

- Skill frontmatter and routing sections;
- the visual grammar reference;
- layered-composite guidance;
- evaluation cases;
- Chinese and English READMEs;
- the portable prompt;
- the OpenAI agent metadata if its description needs the new trigger terms.

The GitHub repository short description remains plain text because GitHub does not support embedded images in that field. It should mention that before/after examples are available. Both READMEs will place a visible comparison example near the introduction using project-owned demonstration assets under `docs/images/`.

The public example must:

- show an exact demonstration source beside or above the generated result;
- be generated from project-owned or newly created synthetic source material;
- avoid the user's private photographs and third-party example artwork;
- identify synthetic source material transparently when used;
- include useful alt text and a compact file size suitable for GitHub;
- use the deterministic comparison script so neither panel is generatively rewritten or cropped.

The release should be published as a new version rather than replacing `v1.0.0`. The installable archive must retain one top-level Skill folder and the established six-file layout unless a required reference file is added intentionally.

## Validation

Add or revise evaluation cases for:

- portrait source automatically routed to `3:5`;
- horizontal landscape automatically routed to `5:3`;
- explicit `4:5`, `1:1`, `9:16`, and `original` requests honored;
- default ambiguous request routed to `jingshan-single`;
- layered request retaining a recognizable photographic anchor;
- distilled request containing no photo fragment or photorealistic window;
- person-preservation request never routed to distillation automatically;
- color remaining within the selected existing color mode;
- horizontal and vertical before/after boards containing both images without crop;
- author credit remaining in source and repository documentation, never inside generated images.
- README comparison media rendering from the public GitHub URL with both panels legible.

Validate frontmatter, Skill package structure, README links, portable-prompt consistency, comparison-script behavior, installed-copy synchronization, and release archive hash before publication.

## Success Criteria

- Users install and search for only `compose-jingshan-landscape`.
- The Skill clearly distinguishes photographic editing, visible real-scene layering, and no-photo distillation.
- Default output is no longer incorrectly described as always vertical `3:5`.
- Portrait and landscape subjects route predictably to `3:5` and `5:3`.
- Explicit ratios are honored without weakening source identity or meaningful unpainted space.
- The new behavior remains recognizably Lang Jingshan-inspired rather than becoming a copy of a paper-zine aesthetic.
- All borrowed concepts are independently expressed and compatible with this repository's MIT distribution.
