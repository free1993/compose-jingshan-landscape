# compose-jingshan-landscape

**作者 / Author：junhaogege_**

[English](README.en.md) · [安装](#安装) · [兼容性](#兼容性) · [豆包与通用-ai](#豆包与通用-ai) · [发布包](#发布包)

一个以郎静山集锦摄影与中国画意摄影为主要方向的摄影修图 Agent Skill。它把手机拍摄的风景、人在景中与日常小景，重构为具有云山层次、诗性留白和“无画处”意识的作品，同时支持同画面照片核叠层及原图/成图对比。

> 致敬中国摄影之父郎静山。本项目是个人学习与当代视觉实验，不代表郎静山先生、其家属或相关机构的官方授权或合作。（方案灵感参考Zeejay0大佬，https://github.com/Zeejay0/gathered-scenes-zine-skill）

## 搜索名称

在 GitHub 或支持 GitHub 搜索的 AI 中输入完整名称：

```text
compose-jingshan-landscape
```

GitHub 仓库：[free1993/compose-jingshan-landscape](https://github.com/free1993/compose-jingshan-landscape)

公开 GitHub 仓库可以通过名称搜索，但不会因此自动进入 Codex、ChatGPT 或其他产品的官方 Skill/Plugin Directory；目录发布属于独立流程。

## 能做什么

| 模式 | 作用 |
| --- | --- |
| `jingshan-single` | 改单图，输出独立的 3:5 郎静山取向画意摄影作品 |
| `jingshan-layered` | 在同一张成图中保留真实照片核，与纸本、留白和画意重构形成可见叠层 |
| `before-after` | 生成精确、可复现的原图/成图对比板 |
| `叠图对比` | 同时输出叠层艺术成图与确定性对比板 |
| `poetic-small-scene` | 处理花枝、器物、窗影、街角等手机摄影小景 |

Skill 默认保留主体身份、关键动作和照片事实，不以“水墨滤镜”覆盖原图，而是通过取舍、层次、雾气、纸白与书画式空间关系完成重构。

## 安装

### 让 Codex 按仓库安装

直接提出：

```text
安装 GitHub 仓库 free1993/compose-jingshan-landscape 里的 compose-jingshan-landscape Skill
```

### 手动安装到 Codex

macOS / Linux：

```bash
git clone https://github.com/free1993/compose-jingshan-landscape.git
mkdir -p ~/.codex/skills
cp -R compose-jingshan-landscape/compose-jingshan-landscape ~/.codex/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/free1993/compose-jingshan-landscape.git
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse ".\compose-jingshan-landscape\compose-jingshan-landscape" "$HOME\.codex\skills\compose-jingshan-landscape"
```

安装后重新打开任务；若 Skill 没有立即出现，请重启宿主应用。

### ZIP 导入

从 [Releases](https://github.com/free1993/compose-jingshan-landscape/releases) 下载：

```text
compose-jingshan-landscape-v1.0.0.zip
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
3. 上传照片，并提出“郎静山改单图”“叠图”或“原图成图对比”等要求。
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
$compose-jingshan-landscape 输出郎静山改单图，并生成原图/成图对比板。
```

## 颜色与输入

- 支持 1 张主图，并可选最多 3 张辅助图。
- 原图颜色没有硬性限制；Skill 会根据主体、光线与意境进行受控减色，而不是统一套用单一色调。
- 艺术成图依赖宿主具备图像编辑或生成能力。
- `scripts/build_comparison.py` 用于确定性对比排版，需要 Pillow；它不参与艺术生成。

## 仓库结构

```text
compose-jingshan-landscape/
├── README.md
├── README.en.md
├── PORTABLE_PROMPT.md
├── LICENSE
└── compose-jingshan-landscape/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/build_comparison.py
```

## 发布包

标准发布包只包含可安装 Skill，不包含 README、设计文档或仓库元数据。发布版本：[v1.0.0](https://github.com/free1993/compose-jingshan-landscape/releases/tag/v1.0.0)。

## 隐私

仓库和发布包只包含 Skill 指令、参考规范与排版脚本，不包含作者或使用者的原始照片、测试成图及生成记录。运行时请根据自己的隐私需求选择可接受的图像处理服务。

## 许可

[MIT License](LICENSE)
