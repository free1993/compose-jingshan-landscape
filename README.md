# compose-jingshan-landscape

**作者 / Author：junhaogege_**

一个面向 Codex 的摄影修图 Skill。它以郎静山的集锦摄影与中国画意摄影为主要视觉方向，把手机拍摄的风景、人在景中与日常小景，重构为具有云山层次、诗性留白和“无画处”意识的作品。

> 致敬中国摄影之父郎静山。本项目是个人学习与当代视觉实验，不代表郎静山先生、其家属或相关机构的官方授权或合作。（方案灵感参考Zeejay0大佬，https://github.com/Zeejay0/gathered-scenes-zine-skill）

## 能做什么

- `jingshan-single`：改单图，输出独立的 3:5 郎静山取向画意摄影作品。
- `jingshan-layered`：在同一张成图中保留真实照片核，并与纸本、留白和画意重构形成可见叠层。
- `before-after`：生成精确、可复现的原图/成图对比板，不把对比排版混入艺术成图。
- `叠图对比`：组合输出叠层艺术成图与确定性对比板。
- `poetic-small-scene`：处理花枝、器物、窗影、街角等手机摄影小景。

Skill 默认保留主体身份、关键动作与照片事实，不以“水墨滤镜”覆盖原图，而是通过取舍、层次、雾气、纸白与书画式空间关系完成重构。

## 安装

在 Codex 中直接提出：

```text
安装 GitHub 仓库 free1993/compose-jingshan-landscape 里的 compose-jingshan-landscape Skill
```

也可以将仓库中的 `compose-jingshan-landscape` 文件夹复制到：

```text
~/.codex/skills/compose-jingshan-landscape
```

重启或重新打开 Codex 任务后即可触发。

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

## 输入与依赖

- 支持 1 张主图，并可选最多 3 张辅助图。
- 原图颜色没有硬性限制；Skill 会根据主体、光线与意境进行受控减色，而不是统一套用单一色调。
- 艺术成图依赖具备图像编辑/生成能力的运行环境。
- `scripts/build_comparison.py` 用于确定性对比排版，需要 Pillow；它不参与艺术生成。

## 隐私

仓库只包含 Skill 指令、参考规范和排版脚本，不包含作者或使用者的原始照片、测试成图及生成记录。运行时请根据自己的隐私需求选择可接受的图像处理服务。

## 许可

[MIT License](LICENSE)
