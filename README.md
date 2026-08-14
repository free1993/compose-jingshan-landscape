# compose-jingshan-landscape

**作者 / Author：junhaogege_**

[English](README.en.md) · [对比示例](#对比示例) · [安装](#安装) · [兼容性](#兼容性) · [豆包与通用-ai](#豆包与通用-ai) · [发布包](#发布包)

一个以郎静山集锦摄影与中国画意摄影为主要方向的摄影修图 Agent Skill。它把手机拍摄的风景、人在景中与日常小景，重构为具有云山层次、诗性留白和“无画处”意识的作品，同时支持摄影改单图、同画面实景叠层、无照片块影像蒸馏及原图/成图对比。

> 致敬中国摄影之父郎静山。本项目是个人学习与当代视觉实验，不代表郎静山先生、其家属或相关机构的官方授权或合作。发布方案与创作探索参考了 [Zeejay0 的 Gathered Scenes Zine Skill](https://github.com/Zeejay0/gathered-scenes-zine-skill)。

## 对比示例

![AI 演示原图与郎静山取向 5:3 成图的无裁切对比](docs/images/jingshan-before-after-example.webp)

左侧为项目自有的 AI 演示原图，右侧为按本 Skill 规则生成的横幅 `5:3` 成图；对比板由确定性脚本排版，两侧均未被生成模型二次改写或裁切。演示图只用于说明工作流，不代表历史作品或郎静山先生原作。

## 搜索名称

在 GitHub 或支持 GitHub 搜索的 AI 中输入完整名称：

```text
compose-jingshan-landscape
```

GitHub 仓库：[junhaogege6/compose-jingshan-landscape](https://github.com/junhaogege6/compose-jingshan-landscape)

公开 GitHub 仓库可以通过名称搜索，但不会因此自动进入 Codex、ChatGPT 或其他产品的官方 Skill/Plugin Directory；目录发布属于独立流程。

## 能做什么

| 模式 | 作用 |
| --- | --- |
| `jingshan-single` | 改单图，输出保留照片事实的独立画意摄影作品 |
| `jingshan-layered` | 在同一张成图中保留真实照片核，与纸本、留白和画意重构形成可见叠层 |
| `jingshan-distilled` | 原图只作语义和构图参考，完全重构不含照片碎片的画意摄影作品 |
| `before-after` | 生成精确、可复现的原图/成图对比板 |
| `叠图对比` | 同时输出叠层艺术成图与确定性对比板 |
| `poetic-small-scene` | 处理花枝、器物、窗影、街角等手机摄影小景 |

Skill 默认保留主体身份、关键动作和照片事实，不以“水墨滤镜”覆盖原图，而是通过取舍、层次、雾气、纸白与书画式空间关系完成重构。未指定比例时，竖向主体默认 `3:5`，横向游观山水默认 `5:3`；也支持用户明确指定常用比例或保持原图比例。

## 安装

### 让 Codex 按仓库安装

直接提出：

```text
安装 GitHub 仓库 junhaogege6/compose-jingshan-landscape 里的 compose-jingshan-landscape Skill
```

### 手动安装到 Codex

macOS / Linux：

```bash
git clone https://github.com/junhaogege6/compose-jingshan-landscape.git
mkdir -p ~/.codex/skills
cp -R compose-jingshan-landscape/compose-jingshan-landscape ~/.codex/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/junhaogege6/compose-jingshan-landscape.git
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse ".\compose-jingshan-landscape\compose-jingshan-landscape" "$HOME\.codex\skills\compose-jingshan-landscape"
```

安装后重新打开任务；若 Skill 没有立即出现，请重启宿主应用。

### ZIP 导入

从 [Releases](https://github.com/junhaogege6/compose-jingshan-landscape/releases) 下载：

```text
compose-jingshan-landscape-v1.1.0.zip
```

ZIP 内只有一个顶层 Skill 文件夹，`SKILL.md` 位于该文件夹根目录，可用于支持 Agent Skills ZIP 导入的产品。

## 兼容性

| 产品或环境 | 使用方式 | 兼容级别 |
| --- | --- | --- |
| Codex | 安装仓库中的 Skill 文件夹 | 原生 Agent Skill |
| ChatGPT Skills | 在账号支持 Skills 时上传发布 ZIP | 原生开放格式；可用性受套餐与工作区设置影响 |
| TRAE | 导入包含 `SKILL.md` 的 Skill 文件夹 | 原生 Agent Skills 格式 |
| 火山引擎 AgentKit | 上传发布 ZIP 到 Skills 中心 | ZIP 导入 |
| Claude、Claude Code及其他 Agent Skills 宿主 | 按宿主文档导入 Skill 文件夹或 ZIP | 格式兼容；图像能力取决于宿主 |
| 豆包普通客户端及其他通用 AI | 使用 [`PORTABLE_PROMPT.md`](PORTABLE_PROMPT.md) | 提示词兼容，不是原生安装 |

OpenAI Skills 遵循开放 Agent Skills 标准，但每个宿主提供的图像编辑、文件系统和脚本能力不同，因此同一 Skill 的成图一致性仍取决于所用模型和工具。

参考规范：[OpenAI Skills](https://help.openai.com/en/articles/20001066) · [火山引擎 AgentKit Skill 代码包](https://www.volcengine.com/docs/86681/2205064)

## 豆包与通用 AI

普通豆包客户端目前按“提示词兼容”使用：

1. 打开 [`PORTABLE_PROMPT.md`](PORTABLE_PROMPT.md)。
2. 将其中“可复制提示词”粘贴到新对话或自定义助手的设定中。
3. 上传照片，并提出“郎静山改单图”“实景叠图”“影像蒸馏”或“原图成图对比”等要求。
4. 如果宿主没有图片编辑能力，让它输出完整修图提示词与构图方案，再交给具备图片能力的模型执行。

这种方式保留主要创作判断，但不等同于安装 Agent Skill；不能运行 Python 的环境也无法自动生成确定性对比板。

## 使用示例

```text
$compose-jingshan-landscape 用郎静山取向处理这张手机照片，保留花瓶和枝条，强化无画处。
```

```text
$compose-jingshan-landscape 做同画面叠图：真实照片核清晰可辨，外围转为纸本云山与诗性留白。
```

```text
$compose-jingshan-landscape 把这张照片完全蒸馏成郎静山取向作品：原图只作语义参考，不保留照片块。
```

```text
$compose-jingshan-landscape 把这张横向山水处理成 5:3，保留完整岸线和侧向游观路径。
```

```text
$compose-jingshan-landscape 输出郎静山改单图，并生成原图/成图对比板。
```

## 颜色与输入

- 支持 1 张主图，并可选最多 3 张辅助图。
- 原图颜色没有硬性限制；Skill 会根据主体、光线与意境进行受控减色，而不是统一套用单一色调。
- 未指定比例时自动在竖幅 `3:5` 与横幅 `5:3` 间路由；支持 `4:5`、`2:3`、`3:2`、`16:9`、`1:1`、`9:16` 和原图比例。
- 艺术成图依赖宿主具备图像编辑或生成能力。
- `scripts/build_comparison.py` 用于确定性对比排版，需要 Pillow；它不参与艺术生成。

## 仓库结构

```text
compose-jingshan-landscape/
├── README.md
├── README.en.md
├── PORTABLE_PROMPT.md
├── LICENSE
├── docs/images/                 # GitHub 对比演示
└── compose-jingshan-landscape/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/build_comparison.py
```

## 发布包

标准发布包只包含可安装 Skill，不包含 README、演示图、设计文档或仓库元数据。发布版本：[v1.1.0](https://github.com/junhaogege6/compose-jingshan-landscape/releases/tag/v1.1.0)。

## 隐私

仓库除 Skill 指令、参考规范与排版脚本外，只公开项目自有的 AI 演示原图、演示成图及确定性对比板；不包含作者或使用者的私人原始照片、私人测试图及生成记录。发布 ZIP 不包含任何演示图片。运行时请根据自己的隐私需求选择可接受的图像处理服务。

## 许可

[MIT License](LICENSE)
