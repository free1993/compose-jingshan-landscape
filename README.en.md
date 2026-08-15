# lang-jingshan-photo-skill

**Author: junhaogege_**

[中文](README.md) · [Comparison](#comparison-example) · [Archive](#work-archive) · [Install](#installation) · [GitHub transition](#github-transition) · [Compatibility](#compatibility) · [Portable prompt](#doubao-and-general-ai-tools) · [Commercial licensing](#commercial-licensing) · [Release](#release-package)

An Agent Skill for photo editing and image generation inspired by Lang Jingshan's composite photography and Chinese pictorialist landscape tradition. It transforms mobile landscapes, figures in landscape, and quiet everyday scenes through source-faithful editing, visible real-scene layering, no-photo semantic distillation, atmospheric depth, and the Chinese idea of the meaningful unpainted area.

> A tribute to Lang Jingshan, widely recognized as a pioneering figure in Chinese photography. This independent learning and contemporary visual experiment is not officially affiliated with or endorsed by Lang Jingshan, his family, or related institutions. The distribution approach and creative exploration were informed in part by [Zeejay0's Gathered Scenes Zine Skill](https://github.com/Zeejay0/gathered-scenes-zine-skill).

## Comparison example

![Uncropped comparison of an AI demonstration source and a warm silver-gelatin 5:3 Lang Jingshan-inspired result](docs/images/jingshan-before-after-example.webp)

The left panel is a project-owned AI demonstration source. The right panel is the generated `5:3` warm silver-gelatin result, using ivory highlights, warm-gray middle tones, and charcoal shadows rather than heavy sepia or yellow paper. The deterministic comparison script assembles both panels without generative rewriting or cropping. This workflow example is not a historical photograph or an artwork by Lang Jingshan.

## Work archive

The repository now follows a project-repo style that is closer to Zeejay0's update pattern: the README is the main entry point, the installable Skill lives under `skills/`, and public cases plus observation notes live under `examples/`.

- Public case index: [examples/README.md](examples/README.md)
- Installable Skill entry: [skills/lang-jingshan-photo-skill/SKILL.md](skills/lang-jingshan-photo-skill/SKILL.md)

## Search name

Use the formal Skill name first in GitHub or an AI tool that can search GitHub:

```text
lang-jingshan-photo-skill
```

Repository: [junhaogege6/compose-jingshan-landscape](https://github.com/junhaogege6/compose-jingshan-landscape)

The public repository URL still uses the older path `compose-jingshan-landscape`. The installable Skill name and invocation name now use `lang-jingshan-photo-skill` so the published links stay intact while search and installation language match the final identity.

If search is inconsistent during the transition, try the older repository keyword `compose-jingshan-landscape` as a fallback.

A public GitHub repository is searchable by name, but it is not automatically listed in the official Codex, ChatGPT, or third-party Skill/Plugin Directory. Directory publication is a separate process.

## Creative paths

You do already have explicit creative paths; they were simply spread across the mode system rather than presented as one table. For this repository, the most accurate framing is not "two paths" but three creation paths inside one Skill:

| Dimension | Standalone Jingshan edit | Same-canvas layered result | Image distillation |
| --- | --- | --- | --- |
| Best for | keeping the original subject, space, and photographic facts | keeping both a truthful photo anchor and a pictorial translated field | extracting the source theme, emotion, and spatial gesture into a fully rebuilt work |
| Role of the source photo | becomes the photographic skeleton of the final work | remains a real anchor inside the same final canvas | serves only as semantic and emotional evidence, not as visible source material |
| Transformation method | rebuild through depth logic, blank space, restrained warm silver-gelatin tonality, and spatial editing | make the real photo anchor hand off into paper, mist, and pictorial mountain space | extract tension, visual metaphor, and spatial gesture from the source, then recreate |
| Result | a standalone pictorial photograph with a clear photographic footing | a layered artwork where the real photo anchor and pictorial field coexist | a complete Lang Jingshan-oriented work with no retained photo fragment |
| Typical request language | "rework this photo", "Lang Jingshan edit", "preserve the vase and branches" | "layered", "photo anchor", "same-canvas composite" | "distill", "semantic reference only", "retain no photo fragment" |
| Invocation | `$lang-jingshan-photo-skill` | `$lang-jingshan-photo-skill` | `$lang-jingshan-photo-skill` |

`before-after` is not a separate creation path. It is a delivery mode added after one of the three paths above has produced the artwork.

## Creative modes

| Mode | Result |
| --- | --- |
| `jingshan-single` | A standalone pictorial photograph that preserves source facts |
| `jingshan-layered` | One artwork combining a truthful photo anchor with an interpreted paper-and-mist field |
| `jingshan-distilled` | A complete pictorial reconstruction that uses the photo only as semantic evidence and retains no photo fragment |
| `before-after` | An exact deterministic source/result comparison board |
| Layered comparison | A layered artwork plus the deterministic comparison board |
| `poetic-small-scene` | Branches, vessels, window shadows, street corners, and other quiet mobile-photo scenes |

The Skill preserves subject identity, meaningful action, and photographic facts by default. It does not prove a Chinese aesthetic by applying an ink-wash filter; it rebuilds the image through selection, depth, mist, paper white, and Chinese landscape spatial logic. Without an explicit ratio, portrait subjects route to `3:5` and expansive landscapes route to `5:3`.

## Installation

### Ask Codex to install from GitHub

```text
Install the lang-jingshan-photo-skill Skill from the GitHub repository junhaogege6/compose-jingshan-landscape.
```

### Manual Codex installation

macOS / Linux:

```bash
git clone https://github.com/junhaogege6/compose-jingshan-landscape.git
mkdir -p ~/.codex/skills
cp -R compose-jingshan-landscape/skills/lang-jingshan-photo-skill ~/.codex/skills/
```

Windows PowerShell:

```powershell
git clone https://github.com/junhaogege6/compose-jingshan-landscape.git
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse ".\compose-jingshan-landscape\skills\lang-jingshan-photo-skill" "$HOME\.codex\skills\lang-jingshan-photo-skill"
```

Open a new task after installation. Restart the host application if the Skill does not appear immediately.

### ZIP import

Download the latest ZIP from [Releases](https://github.com/junhaogege6/compose-jingshan-landscape/releases). The archive contains exactly one top-level Skill folder with `SKILL.md` at its root.

## GitHub transition

Two naming layers currently coexist:

- Formal Skill name, invocation name, and local install name: `lang-jingshan-photo-skill`
- Current public GitHub repository path: `junhaogege6/compose-jingshan-landscape`

The structure is also split in two layers:

- Project-repo entry: `README.md`, `examples/`, `docs/`, and `assets/`
- Installable Skill: `skills/lang-jingshan-photo-skill/`

This keeps the Skill-side installation language clean while preserving the existing public repository and release links. When you are ready to rename the GitHub remote itself, use this checklist:

[GitHub rename checklist](docs/github-rename-checklist.md)

## Compatibility

| Product or environment | Method | Compatibility level |
| --- | --- | --- |
| Codex | Install `skills/lang-jingshan-photo-skill` from this repository | Native Agent Skill |
| ChatGPT Skills | Upload the release ZIP when Skills are available for the account | Native open format; availability depends on plan and workspace settings |
| TRAE | Import the folder containing `SKILL.md` | Native Agent Skills format |
| Volcengine AgentKit | Upload the release ZIP to Skills Center | ZIP import |
| Claude, Claude Code, and other Agent Skills hosts | Import the folder or ZIP according to host documentation | Format-compatible; image capability depends on the host |
| Consumer Doubao and general AI chat tools | Use [`PORTABLE_PROMPT.md`](PORTABLE_PROMPT.md) | Prompt compatibility, not native installation |

OpenAI Skills follow the open Agent Skills standard, but image editing, filesystem access, and script execution differ across hosts. Output consistency therefore depends on the selected model and tools.

References: [OpenAI Skills](https://help.openai.com/en/articles/20001066) · [Volcengine AgentKit Skill package requirements](https://www.volcengine.com/docs/86681/2205064)

## How others can use it

The three most practical usage paths are:

### 1. Install it directly in an Agent Skills host

- open this repository
- locate `skills/lang-jingshan-photo-skill/`
- import that folder, or a ZIP containing only that folder
- after installation, describe the source photo and desired output directly

Best for: Codex, ChatGPT Skills, TRAE, AgentKit, and other hosts that support `SKILL.md`.

### 2. Copy it into a Codex-style local skills directory

- `git clone` this repository
- copy `skills/lang-jingshan-photo-skill/` into the local skills directory
- start a new task and either describe the request naturally or call `$lang-jingshan-photo-skill`

Best for: users who want the full rule set and deterministic comparison script.

### 3. Use it as a portable prompt in Doubao, WorkBuddy, or general LLM chat tools

- open [`PORTABLE_PROMPT.md`](PORTABLE_PROMPT.md)
- copy the portable prompt block
- paste it into a new chat, system prompt, or custom assistant setup
- upload the photo and give a direct request

Best for: hosts that cannot install Skills natively but can follow a long prompt or custom-assistant instruction.

## Recommended usage pattern

People get better results when they provide information in this order:

1. upload the primary photo
2. specify the output type: standalone edit, layered result, distillation, or before/after
3. list the must-keep elements
4. list the removable clutter
5. add ratio or mood, such as `3:5`, `5:3`, quiet, airy, warm silver-gelatin, or larger blank space

When in doubt, write more about what must stay and what should go. That is more useful than saying only "make it Lang Jingshan style."

## Doubao and general AI tools

Use the project through prompt compatibility when the host cannot install Agent Skills:

1. Open [`PORTABLE_PROMPT.md`](PORTABLE_PROMPT.md).
2. Paste its portable prompt into a new conversation or custom-assistant instruction field.
3. Upload a photograph and request a Jingshan single artwork, real-scene layered artwork, no-photo distillation, or before/after output.
4. If the host lacks image editing, ask it for an executable image prompt and composition plan, then run that prompt in an image-capable model.

This preserves the main creative decisions but is not the same as native Skill installation. A host without Python execution cannot automatically build the deterministic comparison board.

## Example requests

```text
$lang-jingshan-photo-skill Rework this mobile photograph in a Lang Jingshan-inspired direction. Preserve the vase and branches and strengthen the meaningful unpainted space.
```

```text
$lang-jingshan-photo-skill Create one layered artwork with a clearly recognizable source-photo anchor dissolving into paper, mist, and pictorial mountain space.
```

```text
$lang-jingshan-photo-skill Fully distill this photograph into a Jingshan-inspired artwork. Use it only as semantic evidence and retain no photographic fragment.
```

```text
$lang-jingshan-photo-skill Rework this horizontal landscape at 5:3 while preserving the full shoreline and lateral roaming path.
```

```text
$lang-jingshan-photo-skill Produce the standalone artwork and an exact source/result comparison board.
```

## Prompt templates

These examples are easier for other people to reuse because they are concrete and execution-oriented.

### 1. Small mobile still life

```text
Rework this mobile photo in a Lang Jingshan-inspired direction. Preserve the vase, branches, and wall shadow. Remove the drink cup and can. Let the empty wall become the main unpainted area, and keep the result photographic before it becomes pictorial. Output 3:5.
```

### 2. Identity-safe figure in landscape

```text
Process this travel portrait in landscape. The face, age impression, pose, clothes, and identity must remain accurate. Preserve the true relationship between the person and the hillside, while rebuilding the environment into layered mist, mountain depth, and warm silver-gelatin tonality. Output 3:5.
```

### 3. Horizontal landscape

```text
Transform this horizontal landscape photo into a Lang Jingshan-inspired result. Preserve the full shoreline, distant mountains, and lateral roaming path. Compress small foliage detail, strengthen atmospheric depth and blank space, and output 5:3.
```

### 4. Same-canvas layered result

```text
Create a same-canvas layered artwork. The real photo anchor must remain clearly recognizable so the original subject and space can still be identified. Let the surrounding field dissolve into paper, mist, and pictorial mountain space. Do not turn it into a generic torn-paper poster or add decorative labels.
```

### 5. Full distillation

```text
Use this photo only as semantic evidence and fully distill it into a Lang Jingshan-inspired pictorial photograph. Keep no source photo fragment, no photographic window, and no realistic crop piece. Retain only its spatial gesture, mood, and subject relationships.
```

### 6. Before/after delivery

```text
First produce one complete Lang Jingshan-inspired standalone result, then generate a separate source/result comparison board. The source image must remain unchanged and must not be repainted by the model. Keep the final artwork in a restrained warm silver-gelatin direction.
```

### 7. Multi-image support

```text
The primary image provides the person and terrain. Supporting images provide distant mountains, cloud layers, and pine forms. Rebuild the scene in a Lang Jingshan-inspired direction while preserving the person's identity and the primary landform. Avoid a heavy scrapbook or obvious collage feel.
```

### 8. For Doubao or general chat models

```text
Do not explain theory first. Execute directly: preserve the subject, remove clutter, expand blank space, compress tiny texture, and keep the result photographic before it becomes pictorial. If you do not have real image-editing ability, output a complete executable generation or editing prompt instead.
```

## Input and color

- Accept one primary photograph and up to three optional supporting photographs.
- There is no mandatory source color palette. The Skill performs controlled color reduction according to subject, light, and mood instead of applying one fixed grade.
- The default `silver-gelatin` mode uses restrained warm-gray print tonality, not neutral digital grayscale, heavy sepia, or a yellow rice-paper filter.
- Without an explicit ratio, the Skill routes between portrait `3:5` and landscape `5:3`; explicit `4:5`, `2:3`, `3:2`, `16:9`, `1:1`, `9:16`, and original-ratio output are supported.
- Artistic output requires an image-editing or image-generation capability.
- `scripts/build_comparison.py` requires Pillow and creates deterministic comparison layouts; it does not generate the artwork.

## Repository

```text
compose-jingshan-landscape/
├── README.md
├── README.en.md
├── PORTABLE_PROMPT.md
├── LICENSE
├── assets/
│   └── brand/
├── examples/
│   └── README.md
├── docs/
│   └── images/
└── skills/
    └── lang-jingshan-photo-skill/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        └── scripts/build_comparison.py
```

## Release package

The main update path now follows the repository's default branch, closer to a "project repo plus skills subdirectory" model; ZIP remains an optional distribution format. The standard release archive contains only the installable Skill. It excludes repository documentation, demonstration images, design notes, and Git metadata. The current public release page remains under the older repository path: [Releases](https://github.com/junhaogege6/compose-jingshan-landscape/releases).

## Commercial licensing

This project now uses a personal non-commercial license instead of an MIT-style free commercial license.

- Allowed: free personal learning, research, experimentation, and hobby use
- Not allowed without permission: paid generation, commissioned work, classes, consulting, SaaS/API use, client work, internal company use, commercial training, or any other direct or indirect commercial use
- For commercial licensing: contact the author first and obtain clear written permission

The default business contact path is the GitHub account [junhaogege6](https://github.com/junhaogege6), unless another contact method is explicitly listed in this repository.

## Privacy

In addition to instructions, references, and the comparison-layout script, the repository publishes only project-owned AI demonstration source/result media. It contains no private user photographs, private tests, paths, or generation history. The release ZIP contains no demonstration images. Choose an image-processing provider that matches your privacy requirements.

## License

[Personal Non-Commercial License](LICENSE)
