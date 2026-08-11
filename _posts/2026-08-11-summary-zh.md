---
layout: default
title: "Horizon Summary: 2026-08-11 (ZH)"
date: 2026-08-11
lang: zh
---

> 从 124 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [Meta 回归开源，扎克伯格抨击封闭 AI](#item-tech-news-1) ⭐️ 8.0/10
2. [Rust 可移植 SIMD 应用于 GPU 编程的探讨](#item-tech-news-2) ⭐️ 8.0/10
3. [Meta 发布面向本地智能体工作流的开源模型 Muse Glimmer](#item-tech-news-3) ⭐️ 8.0/10
4. [利用超长中断指令攻击系统管理模式](#item-tech-news-4) ⭐️ 8.0/10
5. [手工将乘法算法编译进 Transformer 权重，实现 100%精确乘法](#item-tech-news-5) ⭐️ 8.0/10
6. [antirez 发布面向 Apple Silicon 的原生 MiniMax-H3 推理项目 h3.c](#item-tech-news-6) ⭐️ 7.0/10
7. [人性化 LLM 输出并不可取](#item-tech-news-7) ⭐️ 7.0/10
8. [英伟达联手华尔街募资 5000 亿美元发展 AI 基础设施](#item-tech-news-8) ⭐️ 7.0/10
9. [Fru：基于 Rust 的快速随机森林实现，支持 Python 与 R](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [英伟达联手六家资产管理公司，拟撬动 5000 亿美元 AI 基础设施融资](#item-finance-news-1) ⭐️ 9.0/10
2. [英特尔、Verisk 与 GameStop 领衔盘前异动](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Meta 回归开源，扎克伯格抨击封闭 AI](https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878) ⭐️ 8.0/10

据《金融时报》报道，Meta 首席执行官马克·扎克伯格公开抨击封闭式 AI 竞争对手，并重申 Meta 将回归开源模型战略。他在 Meta 官方页面发布题为《未来属于每个人》的文章，强调开源 AI 的价值，并质疑 AI 安全必须依赖权力高度集中的观点。这一表态在 Hacker News 上引发大量讨论，有人视之为开源 AI 的利好，也有人怀疑 Meta 的动机。整体上，Meta 正通过与 OpenAI、Google 等更封闭的对手形成对比，继续推进开源模型路线。

hackernews · root-parent · 8月10日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=49243880)

**「背景」** Meta 曾于 2023 年发布 Llama 模型，被视为开源 AI 竞赛的开端；随后该公司一度转向闭源或专有模型路线。如今，扎克伯格在公开文章中批评 OpenAI 和 Anthropic 等“封闭”AI 对手，并宣布 Meta 重新押注开源模型。这些背景解释了为何此次表态被看作 Meta 战略上的重要回归。

**「影响」** 对依赖开源模型的企业和开发者而言，Meta 继续押注开源路线意味着开放权重模型可能获得持续投入，并在与封闭式 AI 的竞争中获得更多选择。

**「社区讨论」** Hacker News 评论中，不少用户认为无论 Meta 动机如何，开源 AI 整体是好事；也有人批评 Meta 先推封闭 API、遇冷后才开源，或认为这是落后后要求改变规则的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/zuckerberg-criticizes-closed-ai-meta-open-models/">Mark Zuckerberg criticizes closed AI rivals as Meta returns to open models</a></li>
<li><a href="https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878?syn-25a6b1a6=1">Mark Zuckerberg attacks ‘closed’ AI rivals as Meta returns to open models</a></li>

</ul>
</details>

**标签**: `#open source`, `#artificial intelligence`, `#Meta`, `#AI industry`, `#Llama`

---

<a id="item-tech-news-2"></a>
### [Rust 可移植 SIMD 应用于 GPU 编程的探讨](https://www.vectorware.com/blog/simd-on-gpu/) ⭐️ 8.0/10

这篇文章探讨了将 Rust 的可移植 SIMD 抽象用于 GPU 编程的方法，目标是让 SIMD 代码在 CPU 与 GPU 上更易复用。文中指出目前 Rust 标准库的 portable SIMD 仅存在于 nightly，而评论者提到可用 fearless\_simd crate 在 stable 上获得类似能力。讨论还涉及固定 SIMD 宽度带来的性能可移植性问题，以及社区对成熟开源 Rust SIMD 库（类似 Google Highway）的期待。整体上，该方案回应了在 Rust 中编写高性能、可移植 GPU 代码的需求，但库成熟度和工具链支持仍是主要限制。

hackernews · sagacity · 8月10日 18:12 · [社区讨论](https://news.ycombinator.com/item?id=49247477)

**「背景」** Rust 的可移植 SIMD 抽象（core::simd）是一套平台无关的向量运算 API，旨在让同一份 SIMD 代码能在不同 CPU 架构上运行；然而这套 API 目前主要仅在 nightly 工具链上可用，一些项目不得不借助 fearless\_simd 等第三方库在 stable 上获得可移植 SIMD 能力。VectorWare 最近取得的技术进展让 Rust 的 core::simd 代码可以直接在 GPU 上运行，并且以 warp 为单位保持不变，无需使用 intrinsics 或重写代码。这意味着开发者可以在 GPU 编程中继续使用熟悉的 Rust SIMD 抽象，为高性能、可移植的 GPU 计算提供了新的路径。

**「影响」** 对希望用 Rust 编写高性能可移植 GPU/CPU SIMD 代码的开发者，直接的影响是标准 portable SIMD 目前仍需 nightly，生产项目往往需要改用 fearless\_simd 等第三方库，并自行处理性能可移植性问题。

**「社区讨论」** 评论者指出 portable SIMD 仅限 nightly，fearless\_simd 是在 stable 上使用的替代方案；还有人惊讶于 SIMD 可用于 GPU，并质疑固定 SIMD 宽度示例的“可移植性”，同时希望出现像 Google Highway 那样成熟的 Rust 生态库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vectorware.com/blog/simd-on-gpu/">Rust SIMD on the GPU - VectorWare</a></li>
<li><a href="https://elsolitario.org/en/2026/08/10/vectorware-portable-simd-gpu-rust/">SIMD on GPU: Rust&#x27;s core::simd Runs on Warps Unchanged</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-08-11-vectorware-achieves-milestone-in-gpu-computing-with-rust-portable-simd-integration">Rust Portable SIMD on GPU: VectorWare&#x27;s Technical Milestone</a></li>

</ul>
</details>

**标签**: `#Rust`, `#SIMD`, `#GPU computing`, `#portable SIMD`, `#systems programming`

---

<a id="item-tech-news-3"></a>
### [Meta 发布面向本地智能体工作流的开源模型 Muse Glimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) ⭐️ 8.0/10

Meta 推出了 Muse Glimmer，一个约 300 亿（30B）参数的开源模型，专为常驻本地的智能体工作流设计。该模型体现了开放权重模型在本地部署方面的进展，让开发者和用户可以在自己的设备上运行智能体任务，而无需依赖大规模云端推理。社区正在讨论它与即将发布的 Qwen3.8 27B 等模型的对比，以及 Meta 在开放权重美国模型中的战略位置。Meta 还表示将发布 Muse Spark 1.2 基础模型的权重，被视为对自托管爱好者更有意义的消息。

hackernews · riordan · 8月10日 10:10 · [社区讨论](https://news.ycombinator.com/item?id=49241679)

**「背景」** Meta 发布了 Muse Glimmer，这是一个 300 亿参数（30B）的稠密多模态开放权重模型，专为常驻本地的智能体工作流优化。模型权重采用 Apache 2.0 许可证发布，支持 120K 以上的上下文窗口，设计用于本地长时间运行的智能体任务，并针对多种 NVIDIA 平台进行了优化。这类智能体模型与普通聊天模型不同，强调自主感知环境、调用工具并持续执行多步任务。

**「影响」** 社区用户已经能在 Ollama 等工具中本地运行 Muse Glimmer（例如在 32G 内存的旧款 Mac mini 上），并有 Unsloth 提供的量化版本，降低了本地部署门槛；不过实际运行速度较慢，适合离线或低交互场景。

**「社区讨论」** 社区意见分歧不大，主要关注点在于 Muse Glimmer 与即将发布的 Qwen3.8 27B 等模型的对比，以及 Meta 发布 Muse Spark 1.2 权重在战略上的意义。有用户实际在 Ollama 上运行 Muse Glimmer，效果尚可但速度很慢，并认为本地大模型的普及可能改变 AI 基础设施格局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://korshunov.ai/en/article/17490-meta-releases-open-weight-muse-glimmer-30b-agentic-vision-model/">Meta releases open-weight Muse Glimmer 30 B agentic vision model</a></li>
<li><a href="https://developer.nvidia.com/blog/run-local-agentic-ai-workflows-with-metas-muse-glimmer-on-nvidia/">Run Local Agentic AI Workflows with Meta ’s Muse Glimmer on NVIDIA</a></li>
<li><a href="https://www.phoronix.com/news/Meta-Muse-Glimmer">Meta Publishes Muse Glimmer As 30 B Open Agentic Model - Phoronix</a></li>

</ul>
</details>

**标签**: `#meta`, `#open-weights`, `#local-ai`, `#agent-workflows`, `#llm`

---

<a id="item-tech-news-4"></a>
### [利用超长中断指令攻击系统管理模式](https://github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii) ⭐️ 8.0/10

该 GitHub 仓库展示了一种利用极长中断指令触发系统管理模式（SMM）的新颖漏洞利用技术。作者提供了概念验证代码和详尽说明，分析了 CPU 在执行超长指令期间 SMM 超时假设可被滥用的问题。该技术需要 root 权限才能实施，因此并非传统意义上的远程或提权漏洞，但对固件安全研究和理解 CPU 底层行为具有重要价值。仓库还关联了作者的另一项目 asm-hall-of-shame，专门研究单条指令的最差性能。

hackernews · WhiteDawn · 8月10日 16:03 · [社区讨论](https://news.ycombinator.com/item?id=49245491)

**「背景」** 系统管理模式（SMM，有时称为 ring −2）是 x86 CPU 的一种特殊运行模式，它会挂起包括操作系统在内的所有正常执行，转而运行通常驻留在固件中的独立代码。该仓库展示了一种利用超长运行时间机器指令来打断 SMM 的方法，作者称仅凭一条极长的指令就能攻破这种隐藏的特权执行环境。相关讨论指出，该攻击需要 root/内核级权限，因此更像是对硬件的重新控制而非普遍可利用的漏洞；SMM 的这种设计也常引发关于用户无法控制或审查其内存区域的争议。

**「影响」** 该技术的主要影响是为固件安全研究提供新的攻击面，但因其需要 root 权限，对普通用户的实际威胁有限。

**「社区讨论」** Hacker News 评论中，有用户指出固件设计者已预料到此类攻击，但将超时值选择的责任推给了平台实现者；另有用户强调该技术需要 root，称其为“夺回硬件控制权”而非漏洞，并对 SMM 的用户不可控性表达担忧。不少评论也提到 README 用超长代码块示例来强调指令必须“非常长”，增加了趣味性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/System_Management_Mode">System Management Mode - Wikipedia</a></li>
<li><a href="https://github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii">GitHub - xoreaxeaxeax/smiiiiiiiiiiiiiiii: A very very very very very very very long interrupt · GitHub</a></li>
<li><a href="https://news.ycombinator.com/item?id=49245491">Exploiting System Management Mode with a very long interrupt | Hacker News</a></li>

</ul>
</details>

**标签**: `#security`, `#system-management-mode`, `#firmware`, `#exploit`, `#low-level`

---

<a id="item-tech-news-5"></a>
### [手工将乘法算法编译进 Transformer 权重，实现 100%精确乘法](https://www.reddit.com/r/MachineLearning/comments/1vkrnb5/transformers_are_famously_bad_at_arithmetic_so_i/) ⭐️ 8.0/10

作者手写实现了一种将小学乘法算法编译进 Phi-3 Transformer 权重的方法，未经过任何训练。Torchwright 编译器把计算图转为普通 Hugging Face 检查点，三位的计算器在全部 300 万受支持表达式上准确率为 100%；还发布了支持 12 位乘 12 位的检查点。对比测试中，禁用推理的六个前沿模型在数字变长后准确率迅速下降，七位数时五个模型得分 0/500，而作者模型保持 100%。作者构建了四种版本（小学算法、硬件风格、草稿本、暴力记忆），它们计算相同函数但层数、宽度、生成 token 和参数使用不同。相关工作可在 ood.dev 文章、GitHub 仓库和 Hugging Face 检查点中查看。

reddit · r/MachineLearning · /u/notforrob · 8月10日 17:37

**「背景」** Transformer 是一种标准解码器架构，包含因果 softmax 注意力、旋转位置嵌入、RMSNorm 和 KV 缓存；它通常在精确算术任务上表现很差，因为训练学到的是近似模式而非严格算法。torchwright 是一个编译器，它把这种架构当作可编程的固定计算基质：用户在普通 Python 中定义计算图，编译器不经过任何训练，直接将计算图转换为 Transformer 的权重，使标准模型执行该计算图。这项工作的背景来自作者自己开发并开源发布的 torchwright 编译器，其介绍页面、PyPI 项目和 GitHub 仓库都说明了这种无需训练、直接设置权重的编译思路。

**「影响」** 对于可解释性和机制理解研究，这一演示证明普通 Transformer 可通过直接设置权重执行精确多位乘法，为算法编译进权重提供了具体实例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ood.dev/posts/torchwright-intro/">Introducing torchwright — Out of Distribution</a></li>
<li><a href="https://pypi.org/project/torchwright/">torchwright · PyPI</a></li>
<li><a href="https://github.com/physicsrob/torchwright/tree/main">GitHub - physicsrob/torchwright: A compiler that transforms ...</a></li>

</ul>
</details>

**标签**: `#transformers`, `#arithmetic`, `#mechanistic interpretability`, `#compilers`, `#machine learning`

---

<a id="item-tech-news-6"></a>
### [antirez 发布面向 Apple Silicon 的原生 MiniMax-H3 推理项目 h3.c](https://github.com/antirez/h3.c) ⭐️ 7.0/10

antirez 正式发布了 h3.c（H3-metal），这是一个面向 Apple Silicon 的原生 MiniMax-H3 推理实现，为 Mac 用户本地运行该模型提供了新的开源选项。项目托管在 GitHub 的 antirez/h3.c，名称中的 H3-metal 表明它利用 Apple 的 Metal 图形 API 实现高效推理。该发布填补了 MiniMax-H3 在 Apple 硬件上缺乏原生运行工具的实用缺口，但目前尚未公布官方性能基准或详细规格。社区初期的使用反馈显示，模型可以实际运行，但通常需要借助 ComfyUI 的 GGUF 量化节点，并且对统一内存容量和生成速度有明显限制。总体而言，这对在 Apple Silicon 上进行本地 AI 推理的实践者是一个有价值的工具，但仍有待更完整的文档和基准测试。

hackernews · swyx · 8月11日 01:22 · [社区讨论](https://news.ycombinator.com/item?id=49252179)

**「背景」** MiniMax-H3 是 MiniMax 推出的视频生成模型，传统上依赖 Python、PyTorch 和 NVIDIA CUDA 生态。antirez（Redis 作者）用纯 C 和 Metal 为 Apple Silicon 编写了 h3.c 原生推理引擎，不需要 Python 和 PyTorch 即可在 Mac 上运行，但仍需官方 MiniMax-H3 检查点、FFmpeg 和大量统一内存，目前针对 M3 Max 和 M5 Max 进行了优化。

**「影响」** 此项目让 Apple Silicon 开发者能够以原生 Metal 性能在本地运行 MiniMax-H3 推理（针对 M3/M5 Max 优化），并可通过 ComfyUI 配合 GGUF 量化模型实际使用，例如在 64GB M5 Pro 上运行 Q8\_0 34GB 模型；但生成速度仍是明显瓶颈，一段 9 秒 480x864、20 步的片段耗时超过一小时。

**「社区讨论」** 社区反馈显示实际使用门槛较高：有用户询问是否仍需要 128GB 统一内存，并因自己的 96GB 配置感到受限；另一名用户在 M5 Pro 64GB MacBook Pro 上通过 ComfyUI 运行，称效果很好，但需改用 city96 的 ComfyUI-GGUF 自定义节点和 GGUF 量化（如 Q5\_K\_M、Q8\_0），且生成一段约 9 秒、480x864、20 步的片段耗时超过一小时。antirez 本人则提到 MiniMax 在 AMA 中表示 H3 未来可能支持 indexed attention，有望带来大幅速度提升，社区对此表示关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://upstract.com/x/3438bb50f95f2e72">Antirez / h 3 . c : MiniMax H 3 inference engine for Mac computers</a></li>
<li><a href="https://githubawesome.com/h3-c-minimax-h3-video-generation-on-apple-silicon-in-pure-c-and-metal/">h 3 . c : MiniMax H 3 video generation on Apple Silicon in pure C and...</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-08-11-h3-metal-native-minimax-h3-inference-implementation-optimized-for-apple-silicon-m3-and-m5-max-chips">H3-Metal: Native MiniMax-H3 Inference for Apple Silicon</a></li>
<li><a href="https://github.com/antirez/h3.c">GitHub - antirez/h3.c: MiniMax H3 inference engine for Mac ...</a></li>

</ul>
</details>

**标签**: `#open-source`, `#inference`, `#apple-silicon`, `#minimax-h3`, `#machine-learning`

---

<a id="item-tech-news-7"></a>
### [人性化 LLM 输出并不可取](https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb) ⭐️ 7.0/10

这篇由 kuberwastaken 撰写的博客文章反对“人性化”大语言模型（LLM）输出的做法，认为强制模型采用特定文风是有损的：由于风格指令是在生成过程中内化而非事后应用，它可能扭曲模型原本的输出，并增加产生幻觉的风险。文章以“direct model calls as replaceable semantic workers”这类过度修饰的表述为例，说明强行风格化的文本反而会让人难以理解。作者主张，比起追求类人散文，用户应更关注清晰、有用的输出，并对风格约束进行谨慎权衡。

hackernews · kuberwastaken · 8月10日 13:35 · [社区讨论](https://news.ycombinator.com/item?id=49243474)

**「背景」** “人性化 LLM 输出”指的是通过提示词给 AI 模型强加风格约束（如使用简短句子、避免术语、采用 ASD-STE100 简化技术英语等），让输出读起来更像自然人写的。这种趋势在最近的 AI 工具文化中越来越常见（例如“我有 ADHD”之类的技能提示），但作者认为这类约束是在生成过程中施加的，属于有损转换：它可能降低信息保真度，甚至增加模型产生幻觉的风险。评论中一些用户也支持“强行注入风格可能导致更多胡编乱造”的观点。

**「社区讨论」** 评论者普遍赞同文章观点，认为强行施加文风是有损操作，并可能引入新的“胡言乱语”甚至幻觉内容；例如 Xcelerate 和 Animats 都指出，过度风格化会让文本更难解析和验证。也有用户分享了个人提示词，例如要求模型“不拟人、不友好、简洁、不用第一人称、不用表情”，以及注意到搜索行为正从“机器人式关键词”转向自然语言提问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb">Humanising LLM Outputs is Dumb — Kuber Mehta - kuber.studio</a></li>
<li><a href="https://www.explainx.ai/blog/humanising-llm-outputs-lossy-compression-agents-august-2026">Humanising LLM Output Is Lossy — Render at the Boundary ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#prompt engineering`, `#AI`, `#software engineering`, `#natural language processing`

---

<a id="item-tech-news-8"></a>
### [英伟达联手华尔街募资 5000 亿美元发展 AI 基础设施](https://www.bbc.co.uk/news/articles/c78gr0jv0mdo?at_medium=RSS&amp;at_campaign=rss) ⭐️ 7.0/10

英伟达与 Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs 及 KKR 等华尔街大型银行和投资机构达成合作，筹集 5000 亿美元（约 3700 亿英镑）用于人工智能基础设施，包括建设新数据中心和芯片制造工厂。这些投资者首次将 AI 硬件与基础设施（通常称为“算力”）视为独立资产类别；英伟达 CEO 黄仁勋表示“在 AI 领域，算力就是收入”，并称正在帮助创建“AI 工厂”这一新的可投资基础设施类别。资金将投入英伟达自身及其合作伙伴的项目。公告称，过去三年各大科技和 AI 公司已在 AI 项目和基础设施上合计花费超过 1 万亿美元，而英伟达的市值也在三年内上涨五倍。

rss · BBC World · 8月10日 22:31

**「背景」** AI 基础设施或“算力”指的是用于训练和运行 AI 模型所需的 GPU 芯片、数据中心以及供电冷却等配套系统。过去这类设施多由科技公司自建；如今大型投资机构开始将其视为可以独立融资和持有的资产类别，这为英伟达及合作伙伴开辟了大规模长期资金渠道，以便更快扩充算力供给。

**「影响」** 对依赖英伟达 GPU 的科技和 AI 企业而言，这笔融资有望加速数据中心和芯片工厂建设，从而缓解算力短缺、缩短 GPU 交付周期；不过项目具体细节和执行时间尚未公布，实际落地仍存在不确定性。

**标签**: `#AI infrastructure`, `#Nvidia`, `#investment`, `#data centers`, `#compute`

---

<a id="item-tech-news-9"></a>
### [Fru：基于 Rust 的快速随机森林实现，支持 Python 与 R](https://www.reddit.com/r/MachineLearning/comments/1vkrvks/fru_fast_random_forest_implementation_p/) ⭐️ 7.0/10

Fru 是一个新发布的基于 Rust 的随机森林库，由作者团队开发，并已在 Software X 期刊发表；它同时提供 Python 与 R 绑定。作者声称，在 Python 中 Fru 比 scikit-learn 实现快数倍，某些场景可达数百倍；在 R 中通常比 ranger 快几十个百分点，部分用例可达数倍。该实现包含一种新的排列重要性算法，可带来额外性能提升，并采用分层设计，因此容易生成 Python 和 R 绑定；Python 绑定通过 Arrow PyCapsule 与 pandas、polars、pyarrow 等兼容库无缝协作。这些性能数据来自作者自述基准，目前尚缺乏独立验证。

reddit · r/MachineLearning · /u/kpiwonski · 8月10日 17:45

**「背景」** 随机森林是 Leo Breiman 提出的一种集成学习方法，通过在自助重采样样本上构建多棵决策树，并在每次分裂时仅考虑随机特征子集来降低过拟合、提升稳定性。Fru 是一个用 Rust 编写的随机森林实现，提供了 R 和 Python 的绑定，目标是利用现代多核机器实现高效率、可扩展性以及数值稳定性。该实现已被发表论文介绍，并通过 CRAN 发布 R 包，底层可兼容 pandas、polars、pyarrow 等基于 Arrow PyCapsule 的 Python 生态。

**「影响」** 对使用 Python 或 R 进行随机森林建模的用户，Fru 提供可能大幅缩短训练和推理时间的选择，尤其在与 Arrow 生态的数据框库配合时。但其加速幅度依赖于自报基准，实际效果需独立复现后确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2352711026004097">fru: Fast random forest implementation - ScienceDirect</a></li>
<li><a href="https://cran.r-project.org/web/packages/fru/fru.pdf">fru: A Blazing Fast Implementation of Random Forest</a></li>
<li><a href="https://cran.r-project.org/package=fru">CRAN: Package fru</a></li>

</ul>
</details>

**标签**: `#random forest`, `#Rust`, `#machine learning`, `#performance`, `#library`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [英伟达联手六家资产管理公司，拟撬动 5000 亿美元 AI 基础设施融资](https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html) ⭐️ 9.0/10

英伟达周一宣布与 Apollo、Blackstone、BlackRock、Brookfield、Goldman Sachs 和 KKR 签署谅解备忘录，计划调动超过 5000 亿美元第三方资金，为数据中心建设和英伟达硬件采购提供融资，试图把 AI 芯片变成可投资资产类别。

rss · CNBC Finance · 8月10日 22:09

**「背景」** 此前市场曾在 7 月经历震荡，投资者开始质疑大型科技公司在 AI 上的巨额投入能否获得回报，同时评级机构警告相关资本开支正挤压企业现金流。

**「影响」** 若计划落地，英伟达的客户（如超大规模云厂商和前沿 AI 实验室）可在不消耗自身资产负债表的情况下获得建设数据中心和购买芯片的资金，同时也为机构投资者提供新的信贷投资机会。

**标签**: `#Nvidia`, `#AI infrastructure`, `#asset financing`, `#capital markets`, `#data centers`

---

<a id="item-finance-news-2"></a>
### [英特尔、Verisk 与 GameStop 领衔盘前异动](https://www.cnbc.com/2026/08/10/stocks-making-the-biggest-moves-premarket-aapl-hpe-rklb-and-more.html) ⭐️ 7.0/10

盘前报道显示，英特尔宣布增发 150 亿美元普通股后跌 3%，Verisk 因法院裁定须推进 23.5 亿美元收购 AccuLynx 跌逾 6.5%。GameStop 据彭博报道正考虑放弃对 eBay 的 560 亿美元收购，股价涨逾 1.5%。

rss · CNBC Finance · 8月10日 13:52

**「背景」** Verisk 此前于 12 月终止收购 AccuLynx，原因是联邦贸易委员会（FTC）审查未在交易截止日前完成；eBay 在 5 月曾拒绝 GameStop 的收购要约，称其“既不可信也不具吸引力”。

**标签**: `#M&amp;A`, `#Stock offerings`, `#Corporate earnings`, `#Analyst ratings`, `#Legal rulings`

---