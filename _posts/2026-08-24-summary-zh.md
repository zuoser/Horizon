---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> 从 155 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [微软画图和照片应用给本地 AI 图像添加隐形水印](#item-tech-news-1) ⭐️ 8.0/10
2. [旧金山全城 GIS 数据变成可玩的网页 3D 游戏](#item-tech-news-2) ⭐️ 8.0/10
3. [seL4 形式化安全证明完成 AArch64 支持，仍有限制](#item-tech-news-3) ⭐️ 8.0/10
4. [AI 依赖或将导致编程专业知识崩溃](#item-tech-news-4) ⭐️ 7.0/10
5. [中国召回近三百万辆特斯拉：隐藏式门把手安全隐患](#item-tech-news-5) ⭐️ 7.0/10
6. [你的可执行文件可以是一个 SQLite 数据库](#item-tech-news-6) ⭐️ 7.0/10
7. [CUDA 护城河在智能体推理中是否成立](#item-tech-news-7) ⭐️ 7.0/10
8. [Bart：一个基于 1931 年前英语训练的复古大语言模型](#item-tech-news-8) ⭐️ 7.0/10
9. [用 AI 作为空间软件生成器：创建本质上可编程的三维对象](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [比特币创 2023 年来最大三日涨幅，价格逼近 8 万美元](#item-finance-news-1) ⭐️ 8.0/10
2. [阿里巴巴配股融资 102 亿美元，股价在香港一度跌 10%](#item-finance-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [微软画图和照片应用给本地 AI 图像添加隐形水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

逆向工程分析显示，微软的 MS Paint 和 Photos 应用会为经过 AI 功能编辑的图像静默添加不可见的 GUID 水印，即使这些操作完全在本地完成。这个隐形水印无法被用户关闭，而可见水印则可以手动禁用。分析指出，这一机制意味着“本地生成”并不等于整个操作不包含外部标识，可能将图像与用户的微软账号关联，从而引发隐私和匿名性方面的担忧。目前尚不清楚该水印是否适用于所有 AI 操作，例如 AI 增强的背景删除或移除。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**「背景」** 微软画图和照片应用最近加入了基于本地模型的 AI 图像编辑功能，但逆向工程分析发现，即使用户选择在本地生成输出，应用仍会把提示词发送给微软服务器进行审核，并由服务器颁发一个唯一 GUID。随后，这个 GUID 会作为不可见水印嵌入到本地生成的图像中，而可见水印虽然可以关闭，不可见水印却无法禁用且不会通知用户。这种做法意味着“本地生成”并不等于完整操作都在本地完成，用户可能在不知情的情况下被标记。

**「影响」** 使用 Paint 或 Photos 中 AI 编辑功能的用户，其输出的图像可能携带一个与微软账号关联的隐藏唯一标识，从而削弱互联网匿名性，并在极端情况下可能被用于通过传票向微软索取用户个人信息。

**「社区讨论」** 评论者普遍认为，问题的核心不在于 AI，而在于应用悄悄为每张图片加入唯一标识，这被视为隐私侵犯和针对网络匿名的又一工具；也有评论指出微软此前曾在 Azure DevOps 中错误地给所有提交添加 Copilot“水印”，反映出其实现方式可能不够严谨。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeli.app/story/49421158">Microsoft Paint and Photos Embed Server-Issued GUIDs as... | Zeli</a></li>
<li><a href="https://news.ycombinator.com/item?id=49421158">MS Paint and Photos inivisibly watermark even locally generated ...</a></li>

</ul>
</details>

**标签**: `#watermarking`, `#privacy`, `#AI-generated content`, `#Windows`, `#reverse engineering`

---

<a id="item-tech-news-2"></a>
### [旧金山全城 GIS 数据变成可玩的网页 3D 游戏](https://sf.thijs.gg/) ⭐️ 8.0/10

一个名为 sf.thijs.gg 的网页项目把旧金山的 GIS 数据转换成了可交互的 3D 城市，并做成了可驾驶车辆、收集硬币的游玩形式。该作品在 Hacker News 上引发大量讨论，许多用户表示在虚拟城市中探索带来了强烈的情感共鸣，也有开发者分享了类似用本地 GIS 数据做游戏的经验。它说明借助现有开源数据和低门槛工具，个人开发者也能快速搭建真实城市的可玩数字孪生，尽管目前更接近技术演示而非完整游戏。

hackernews · centrosphere · 8月24日 17:05 · [社区讨论](https://news.ycombinator.com/item?id=49422784)

**「背景」** 该项目利用 GIS（地理信息系统）数据在网页中重建了旧金山全市的 3D 场景。旧金山市政厅通过 SFGIS 计划向公众提供建筑、高程等地理空间数据，这类开放数据正是该网页游戏能够还原街区与建筑的基础。玩家可以在其中驾驶车辆收集金币，社区讨论也关注如何将类似的 GIS 数据流水线用于 GTA 等游戏引擎或制作更高分辨率的本地版本。

**「影响」** 这个演示为开发者提供了一个具体的范例：用公开 GIS、高程和建筑数据就能在网页端生成一座完整可玩的城市，社区评论也显示出对加入街道名、地标、街景纹理和更高分辨率版本等扩展功能的明确需求。

**「社区讨论」** 评论整体非常积极，有评论者表示在游戏中重访旧金山街区让自己感动；也有用户展示了类似项目（费城的 cityrider），并讨论了把 GIS、街景影像和地图数据流水线化为 GTA 式游戏地图的设想。部分人希望增加街道名称、地址跳转、多人在线和本地高清版本，但目前没有明显争议或反对意见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sfgov.maps.arcgis.com/home/index.html">City and County of San Francisco - ArcGIS</a></li>

</ul>
</details>

**标签**: `#GIS`, `#3D rendering`, `#game development`, `#San Francisco`, `#web-based game`

---

<a id="item-tech-news-3"></a>
### [seL4 形式化安全证明完成 AArch64 支持，仍有限制](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

2026 年 8 月 21 日，seL4 微内核在 AArch64 架构上的形式化安全证明宣告完成，这是 ARM 上可验证计算的一个重要里程碑。不过该证明目前仅覆盖单核（unicore）配置，不包含混合关键性系统（non-MCS），也未解决旁道时序问题。对安全关键型 ARM 平台而言，这套证明为更可靠的内核安全保证提供了基础，但距离覆盖完整 AArch64 场景仍有明显距离。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**「背景」** seL4 是一个以形式化验证著称的微内核，其验证工作包括功能正确性、二进制正确性以及安全属性的数学证明。此前 seL4 已在多种架构上完成核心证明；本次针对 AArch64 的新保密性证明，补全了该架构上安全强制（完整性、可用性、保密性）的正式验证。这项工作还得到了英国国家网络安全中心（NCSC）的持续支持。

**「影响」** 对使用 ARM 的安全关键系统开发者（如汽车、国防和嵌入式领域）而言，可在受支持的单核非 MCS 配置中利用该证明来支撑其安全论证；但在单核之外或对时序侧信道敏感的场景中，需自行评估残余风险。

**「社区讨论」** 社区评论一方面提醒要“阅读细则”，指出当前结果限定在 unicore 和 non-MCS；另一方面质疑侧信道时序攻击可能使该证明失去实际意义。讨论还涉及 seL4 的部署现状，包括 GenodeOS、LionsOS 和某中国车企的整车 hypervisor 使用案例，并认为嵌入式与军工市场或有持续投入，但若要宣称提升系统安全，仍需原生 seL4/Linux 方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.linxi.com.au/news/sel4-microkernel-achieves-full-formal-security-verification-on-aarch64">seL4 Microkernel Formal Security Proofs Completed on AArch64 ...</a></li>
<li><a href="https://sel4.systems/Verification/proofs.html">seL4 Proofs | seL4</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#seL4`, `#AArch64`, `#microkernel`, `#security`

---

<a id="item-tech-news-4"></a>
### [AI 依赖或将导致编程专业知识崩溃](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 7.0/10

Lars Faye 的文章认为，过度依赖 AI 编程工具将导致深度编程专业知识的崩溃。这一观点在 Hacker News 上引发广泛讨论，共获得 415 条评论。评论者反映，在企业层面，管理层常常要求“手动写代码就是犯错”，导致代码产出激增，但人类理解和审查代码的能力被远远甩开。也有人提倡在编辑器内集成 LLM 的引导式编码，认为它比纯 agentic/vibe coding 更高效且质量更高。还有人担心这种趋势不可持续，并迫使不依赖 AI 的开发者不得不审查大量劣质 AI 生成代码。

hackernews · larsfaye · 8月24日 15:52 · [社区讨论](https://news.ycombinator.com/item?id=49421554)

**「背景」** 随着 Claude Code、Antigravity 等 AI 编码工具和代理工作流越来越普及，开发者可以借助大语言模型生成、调试代码甚至完成系统设计。然而，这类工具的便利性带来一个关键问题：长期技能形成需要持续的“摩擦”和刻意练习，而过度依赖 AI 可能让开发者跳过这些必经阶段。Lars Faye 的文章《AI Coding will Prevent Expertise》正是基于这一视角，认为如果 LLM 能替代大量基础编程实践，深度编码专业能力可能会逐渐崩溃；这篇文章在 Hacker News 上引发了广泛讨论。

**「影响」** 对开发者而言，最直接的后果是代码审查负担加剧，长期编程技能培养受到侵蚀；但对不同开发者影响不一，认同引导式编码者认为可以兼顾效率与学习。

**「社区讨论」** 评论者普遍认同过度依赖 AI 会侵蚀编程技能，但存在分歧：一部分人认为在编辑器中集成 LLM 的引导式编码既能保持高效又能保证质量，另一部分人则担心这会导致少数不依赖 AI 的开发者被迫审查大量低质量 AI 代码，长期来看不可持续。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49421554">Coding expertise is going to collapse from AI reliance | Hacker News</a></li>
<li><a href="https://larsfaye.com/articles/ai-coding-will-prevent-expertise">AI Coding will Prevent Expertise | Lars Faye</a></li>
<li><a href="https://forum.devtalk.com/t/ai-coding-will-prevent-expertise-lars-faye/248226">AI Coding will Prevent Expertise | Lars Faye - AI In The News - Devtalk</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#software engineering`, `#skill formation`, `#expertise`, `#developer productivity`

---

<a id="item-tech-news-5"></a>
### [中国召回近三百万辆特斯拉：隐藏式门把手安全隐患](https://www.bbc.co.uk/news/articles/c4g6ggdg030o?at_medium=RSS&amp;at_campaign=rss) ⭐️ 7.0/10

中国启动迄今最大规模汽车召回，涉及逾 400 万辆汽车，其中近 298 万辆为中国产特斯拉。召回原因是隐藏式门把手在紧急情况下难以找到和打开；特斯拉称部分 Model 3、Y、S 和 X 车型门把手颜色与内饰相近，严重碰撞导致低压系统失效时可能阻碍逃生和救援。补救措施包括粘贴警告标签和软件更新，使车辆碰撞后自动降下车窗。此前中国曾发生两起涉小米电动汽车的致命事故，怀疑电源故障导致车门无法打开。此外，中国已宣布自 2027 年 1 月 1 日起禁止隐藏式门把手，要求车门内外均配备机械释放装置。

rss · BBC World · 8月24日 05:01

**「背景」** 隐藏式门把手自 2014 年特斯拉 Model S 以来成为电动汽车的流行设计，中国品牌迅速模仿这种流线外观。但其在碰撞或断电时难以操作的安全隐患引发监管关注；美国国家公路交通安全管理局也已展开相关调查，并提议制定新的安全标准。

**「影响」** 此次召回直接影响到中国数百万特斯拉、小鹏、小米和吉利车主，他们需要留意警告标签和软件更新以降低紧急情况下无法开门风险。目前尚不清楚相关车企是否会对全球其他市场实施类似召回。

**标签**: `#Tesla`, `#Electric Vehicles`, `#Automotive Safety`, `#Recall`, `#China`

---

<a id="item-tech-news-6"></a>
### [你的可执行文件可以是一个 SQLite 数据库](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria 提出了一种 Linux 模式，让 SQLite 数据库文件可以被内核直接当作可执行文件运行。他将 SQLite 文件格式中第 68 字节处的 4 字节应用 ID 设为 SELF，即 Structured Executable &amp; Linkable Format，并把 ELF 可执行文件的各个组成部分拆入多个 SQLite 表（schema 见仓库）。配套的 self-exec 解释器（C 语言）负责提取并执行这些片段；Linux 可用 binfmt\_misc 注册文件模式，让内核在遇到 SELF 前缀的可执行文件时调用该解释器。作者在 NixOS 上演示，Simon Willison 也给出了非 NixOS 的注册命令示例。这个把 SQLite 与 ELF 结合的设计为系统程序员展示了一种新颖的“数据库即可执行文件”思路。

rss · Simon Willison · 8月24日 11:38

**「背景」** SQLite 数据库文件的头部包含一个 4 字节的应用 ID，位于文件偏移 68 字节处，通常用于标识数据库属于哪个应用。ELF 是 Linux 上常见的可执行文件格式，内核默认通过文件开头的 ELF 魔数来识别可执行文件。binfmt\_misc 是 Linux 内核的一种机制，允许管理员注册额外的二进制格式，让内核根据文件特定偏移处的字节模式来调用对应的解释器。

**「影响」** 该技巧让 Linux 用户和开发者可以用一个 SQLite 文件同时承载数据与程序逻辑，并在启用 binfmt\_misc 的系统上直接作为可执行文件调用；不过当前实现依赖自定义 schema 和 self-exec 解释器，更偏向概念验证和系统编程实验，而非现成的通用部署格式。

**标签**: `#SQLite`, `#ELF`, `#Linux`, `#binfmt\_misc`, `#systems programming`

---

<a id="item-tech-news-7"></a>
### [CUDA 护城河在智能体推理中是否成立](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat) ⭐️ 7.0/10

半导体行业研究机构 SemiAnalysis 发表文章《AgentX - InferenceXv3：CUDA 在智能体推理中的护城河是否成立？》，由 Cam Quilici 撰写，评估 CUDA 在智能体推理场景下的竞争优势。文中给出多项具体指标：开源了价值 300 万美元的数据集、支持超过 100 万 token 的上下文长度、多轮与子智能体工作负载下 KVCache 命中率超过 95%，并将 GB300 NVL72、MI355、B200 等硬件纳入对比。文章将 CUDA 生态与 AMD 等竞争对手在智能体推理新需求中的表现并列考察，核心在于判断 CUDA 是否仍能维持其生态壁垒。

rss · SemiAnalysis · 8月24日 00:19

**「背景」** CUDA 是英伟达的软件生态，包含库、调试工具以及 DCP/PCP 等分布式通信协议，长期以来构成英伟达在 AI 计算上的护城河。在智能体推理场景中，vLLM 支持矩阵里 AMD 后端几乎全部不受支持，且 AMD 对 DCP/PCP 的实现尚未优化，这使得 AMD 硬件在兼容性上仍明显落后。历史上英伟达拥有比 AMD 多一个数量级以上的内部 GPU 集群用于开发，而 AI 编码智能体正被视为可能削弱这种生态壁垒的新威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic Inferencing?</a></li>
<li><a href="https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing">Can AMD break the CUDA Moat? AMD Advancing AI 2026</a></li>
<li><a href="https://thenextweb.com/news/nvidia-cuda-moat-ai-coding-agents-inference">Nvidia’s CUDA moat faces its first real threat: AI itself</a></li>

</ul>
</details>

**标签**: `#CUDA`, `#Agentic Inference`, `#KVCache`, `#GPU Hardware`, `#AI Infrastructure`

---

<a id="item-tech-news-8"></a>
### [Bart：一个基于 1931 年前英语训练的复古大语言模型](https://www.reddit.com/r/MachineLearning/comments/1vx94er/bart_a_vintage_llm_r/) ⭐️ 7.0/10

Unbounded Labs 发布了 Bart（巴塞洛缪），一个从零开始训练的 2.82B 参数大语言模型，使用 20.1B 个 1931 年前的英语 token 训练而成，并提供了交互式演示、详细研究博客和 Hugging Face 模型下载。该项目旨在探索 Demis Hassabis 提出的问题：LLM 能否重新发现过去伟大科学家的结论。研究团队公开了语料库清洗流程（将哈佛机构藏书从 242B token 清理至 23B token）、自建的 Vintage CORE 基准套件（20 个针对复古 LLM 的基准）、416k 个基于 1930 年前文本的 SFT 问答对，以及训练代码和评估结果。最终模型在一张 H100 上训练了 5 天，维持 60% 的 MFU，总花费约 807 美元；团队称其在 Vintage CORE 上是同规模最佳复古基础模型，优于 GPT-1900，且使用的 token 预算更少。团队正在寻求计算资源资助、资金和导师支持，以进行更大规模的训练。

reddit · r/MachineLearning · /u/soggydoggy8 · 8月24日 17:20

**「背景」** Demis Hassabis 曾提出，人工智能系统或许能重新发现科学史上伟大科学家得出的结论，这一设想是本项目的重要动机。Bart 是一款完全从零训练的“复古”大语言模型，仅使用 1931 年前的英语文本，目的是检验语言模型能否在特定历史语料下独立产生类似过去的科学洞见。该模型由 Unbounded Labs 自筹资金开发，训练数据来自哈佛大学馆藏书籍的清洗版本，并配套构建了面向复古语言模型的基准测试集 Vintage CORE。

**「影响」** 对于研究复古或历史文本 LLM 的研究者，Bart 提供了首个大规模开源语料库、基准套件和训练方法，可能降低该方向的研究门槛；同时，它以极低预算（约 807 美元）完成从头训练和微调，为资源有限的小型实验室提供了一个可复现的高效率训练范例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amacad.org/publication/daedalus/ai-ultimate-tool-science-conversation-demis-hassabis">AI as the Ultimate Tool for Science: A Conversation with Demis Hassabis | American Academy of Arts and Sciences</a></li>
<li><a href="https://www.dwarkesh.com/p/demis-hassabis">Demis Hassabis — Scaling, superhuman AIs, AlphaZero atop LLMs, AlphaFold</a></li>

</ul>
</details>

**标签**: `#LLM`, `#retrieval`, `#research`, `#dataset`, `#machine-learning`

---

<a id="item-tech-news-9"></a>
### [用 AI 作为空间软件生成器：创建本质上可编程的三维对象](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

该论文的合著者介绍了一种利用大型语言模型（LLM）通过空间编程生成三维对象的研究方法。其核心主张是，作为软件存在的三维对象比传统 AI 生成器产生的单体网格块更有用，因为这类对象从创建之初就具备动画就绪、适应性细节（可根据弱计算环境如手机或强计算环境如游戏引擎自动调整呈现）以及层级结构和铰链/插座式关节连接能力。作者在 nova3d.xyz 上提供了可视化演示并附带了 GitHub 仓库。论文承认，该方法在创建复杂有机形状方面仍落后于传统 AI 三维生成器，但作者认为随着 LLM 空间编码能力的提升，代码最终将“吞噬”所有三维生成，受冲击最大的行业将是工业设计、游戏开发、仿真以及 AR/VR/XR。

reddit · r/MachineLearning · /u/mhb\_11 · 8月24日 19:10

**「背景」** 传统 AI 3D 生成器通常直接输出不可编辑的网格模型；而 Nova3D 采用“代码原生”方式，让大语言模型生成可执行程序形式的 3D 资产，物体带有命名部件、约束关系和层级结构，因此可被下游系统检查、修改和动画化。论文中的消融实验显示，这些能力来自 Nova3D 系统本身，而非 LLM 写代码的通用能力。

**「影响」** 对于工业设计、游戏开发、仿真和 AR/VR/XR 领域的开发者与设计师，这项研究意味着 AI 生成的 3D 对象可以天生具备可编程、可动画、含层级结构及铰接/插座运动学的能力，并能根据设备算力自动改变呈现细节，但其在复杂有机形状上的表现仍落后于传统网格生成器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.22738v1">Nova3D: Code-Native Generation of Programmable 3D Assets Generating structured, editable, constraint-consistent 3D assets as executable programs</a></li>
<li><a href="https://x.com/nova3d_ai">Nova3D (@nova3d_ai) / Posts / X</a></li>
<li><a href="https://www.giuseppegalliano.eu/risorse-e-guide/artificial-intelligence-and-3d-modeling/">Artificial Intelligence and 3D Modeling - AI-powered 3D content generation.</a></li>
<li><a href="https://resources.imagine.io/blog/the-future-of-industrial-design-how-ai-3d-visualization-are-changing-the-game">The Future of Industrial Design: How AI &amp; 3D Visualization Are Changing the Game</a></li>

</ul>
</details>

**标签**: `#3D generation`, `#large language models`, `#spatial programming`, `#programmable objects`, `#animation`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [比特币创 2023 年来最大三日涨幅，价格逼近 8 万美元](https://www.cnbc.com/2026/08/24/crypto-extends-gains-after-biggest-3-day-rally-since-2023.html) ⭐️ 8.0/10

比特币延续涨势，周一上涨逾 1%至接近 80,000 美元，为 5 月以来最高；过去三日涨幅超过 20%，是 2023 年以来最大三日涨幅。上周现货比特币 ETF 净流入 19.2 亿美元，为 10 月以来最大单周流入，同时超过 40 亿美元看空加密货币的仓位被平仓。

rss · CNBC Finance · 8月24日 20:02

**「背景」** 此前比特币自去年 10 月以来一直处于长期低迷，上周美国财政部表示将加倍购买较长期国债后，收益率短线走低，带动比特币等风险资产跳涨；机构需求同步回归，现货比特币 ETF 上周流入 19.2 亿美元，超过 40 亿美元的看空仓位被清算。

**标签**: `#bitcoin`, `#cryptocurrency`, `#ETF inflows`, `#short squeeze`, `#Treasury bonds`

---

<a id="item-finance-news-2"></a>
### [阿里巴巴配股融资 102 亿美元，股价在香港一度跌 10%](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html) ⭐️ 8.0/10

阿里巴巴在香港股价周一盘中一度跌 10%，此前公司以每股 112.70 港元向非美国投资者配售 7.1 亿股新股，筹资约 800 亿港元（102 亿美元），用于投资 AI 基础设施。配售价较上周五收市价 123 港元折让约 8.4%，股份最后报 112.7 港元，跌 8.4%。

rss · CNBC Finance · 8月24日 08:21

**「背景」** 本次配售预计周三完成，紧接公司公布 6 月季度净利润下跌 75%，资本开支则增加 75%至 677 亿元人民币。公司此前宣布未来三年在云计算和 AI 基础设施投入至少 3800 亿元人民币，以推动 AI 成为增长引擎。

**「影响」** 现有股东将面临股权稀释，而 AI 资本开支高企可能继续压制阿里巴巴近期利润。

**标签**: `#Alibaba`, `#share placement`, `#AI investment`, `#capital expenditure`, `#Hong Kong market`

---