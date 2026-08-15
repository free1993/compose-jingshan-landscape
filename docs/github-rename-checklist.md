# GitHub Rename Checklist

本清单用于把当前公开仓库 `junhaogege6/compose-jingshan-landscape` 过渡到与 Skill 正式名称一致的 GitHub 命名。

## 当前状态

- Skill 正式名：`lang-jingshan-photo-skill`
- 本地安装名：`lang-jingshan-photo-skill`
- 当前公开仓库路径：`junhaogege6/compose-jingshan-landscape`
- 当前公开发布页：`https://github.com/junhaogege6/compose-jingshan-landscape/releases`

## 建议目标

- GitHub 仓库名：`lang-jingshan-photo-skill`
- 仓库描述首词包含：`Lang Jingshan`, `photo`, `skill`
- Release ZIP 名：`lang-jingshan-photo-skill-vX.Y.Z.zip`
- ZIP 顶层文件夹名：`lang-jingshan-photo-skill`

## 正式改名前

- 确认 README、README.en、`skills/lang-jingshan-photo-skill/SKILL.md`、`agents/openai.yaml` 与调用示例全部使用 `lang-jingshan-photo-skill`
- 确认本地已安装副本也使用 `~/.codex/skills/lang-jingshan-photo-skill`
- 确认是否要保留旧仓库名关键词 `compose-jingshan-landscape` 作为过渡搜索词
- 准备一个新版本号，例如 `v1.1.2` 或 `v1.2.0`

## GitHub 上的操作顺序

1. 在 GitHub 仓库设置页将仓库名从 `compose-jingshan-landscape` 改为 `lang-jingshan-photo-skill`
2. 立即检查仓库首页、README 图片、Release 页面是否能正常打开
3. 更新仓库描述，保持“郎静山取向摄影修图 Skill”与英文关键词并存
4. 新建一个改名后的发布版本，重新上传 ZIP 资产
5. 确认 ZIP 内顶层文件夹名与 `SKILL.md` frontmatter 名称一致
6. 检查 README 中所有仓库链接、Release 链接、安装命令和调用示例
7. 用新旧两个关键词分别搜索一次，确认别人还能找到项目

## 改名后要复查的点

- 浏览器访问旧仓库链接时是否能跳转到新链接
- Release 资产下载链接是否仍可用；如不确定，以 README 中的新链接为准
- README 中的安装命令是否仍指向正确的文件夹名
- 任何截图、教程、帖子里的旧命名是否需要补一条说明
- `PORTABLE_PROMPT.md` 是否仍正确引用 `skills/lang-jingshan-photo-skill/SKILL.md`

## 建议的过渡文案

可放在 README 的搜索或安装部分：

> 正式 Skill 名称为 `lang-jingshan-photo-skill`。当前公开仓库路径仍可能暂时保留旧名 `compose-jingshan-landscape`，用于兼容既有链接与发布页。

## 不建议的做法

- 只改 README 标题，不改 `SKILL.md` 的 `name`
- 只改 GitHub 仓库名，不重做 ZIP 顶层文件夹名
- 同时保留两个可安装 Skill 文件夹在 `~/.codex/skills` 下
- 在没有检查 Release 和安装路径之前就对外发布“已完成改名”
