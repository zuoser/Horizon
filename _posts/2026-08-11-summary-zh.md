---
layout: default
title: "Horizon Summary: 2026-08-11 (ZH)"
date: 2026-08-11
lang: zh
---

> 从 123 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [Nvidia 与六家华尔街机构筹资逾 5000 亿美元建设 AI 基础设施](#item-tech-news-1) ⭐️ 9.0/10
2. [英国的匿名战争蔓延至美国](#item-tech-news-2) ⭐️ 8.0/10
3. [Meta 开源 Muse Glimmer 30B 本地代理模型](#item-tech-news-3) ⭐️ 8.0/10
4. [手工编写 Transformer 权重实现 100%精确乘法](#item-tech-news-4) ⭐️ 8.0/10
5. [Needle2：14MB 端侧 Agentic LLM，主打工具调用与结构化提取](#item-tech-news-5) ⭐️ 7.0/10
6. [扎克伯格抨击封闭 AI 对手 Meta 回归开放模型](#item-tech-news-6) ⭐️ 7.0/10
7. [Rust SIMD 在 GPU 上的应用引发稳定版与可移植性讨论](#item-tech-news-7) ⭐️ 7.0/10
8. [Anthropic 研究展示 Claude 在黎曼 zeta 函数上的数学推理进展](#item-tech-news-8) ⭐️ 7.0/10
9. [超长中断触发 SMM 代码执行](#item-tech-news-9) ⭐️ 7.0/10
10. [Fru：Rust 编写的高性能随机森林库](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [英伟达联手六家资管公司，拟为 AI 基础设施融资 5000 亿美元](#item-finance-news-1) ⭐️ 8.0/10
2. [美股午盘重大异动：并购、增发与评级调整](#item-finance-news-2) ⭐️ 7.0/10
3. [盘前异动：英特尔、Verisk、伯克希尔等](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Nvidia 与六家华尔街机构筹资逾 5000 亿美元建设 AI 基础设施](https://www.theguardian.com/business/live/2026/aug/11/oil-prices-rise-gold-hits-two-month-high-trump-makes-new-deal-demands-iran-live-updates) ⭐️ 9.0/10

英伟达（Nvidia）宣布与 Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs 和 KKR 六家华尔街金融机构合作，筹集超过 5000 亿美元（约 3700 亿英镑）资金用于人工智能基础设施。这是投资者首次将 AI 硬件和基础设施（即“算力”）作为独立资产类别进行承销。英伟达 CEO 黄仁勋表示，公司可选择为其中最多 1250 亿美元（约 25%）的交易提供支持。资金将用于新建数据中心以及 AI 芯片工厂等项目。此次融资凸显出 AI 算力已被视为可投资的关键基础设施资产。

rss · The Guardian International · 8月11日 06:49

**「背景」** 英伟达是 AI 领域最主要的 GPU（图形处理器）供应商，谷歌、Meta、微软、OpenAI 等公司都依赖其芯片训练和运行 AI 模型。过去三年，这些科技公司已在 AI 项目和基础设施上合计支出超过 1 万亿美元，需求推动了英伟达市值增长约五倍。此次与华尔街机构的合作旨在为后续大规模基础设施建设提供长期资本。

**「影响」** 这一安排可能加速数据中心和 AI 芯片工厂的建设，使英伟达及其合作伙伴乃至下游 AI 公司更容易获得大规模算力，同时为华尔街机构开辟新的资产类别。

**标签**: `#AI`, `#Nvidia`, `#Infrastructure`, `#Finance`, `#Hardware`

---

<a id="item-tech-news-2"></a>
### [英国的匿名战争蔓延至美国](https://www.effort.news/uk-lobby) ⭐️ 8.0/10

一篇评论分析指出，英国“儿童安全”游说力量正影响美国数字身份立法，试图在保护儿童的名义下让成年人无法继续匿名使用互联网。作者认为，这类主张可能催生针对美国用户的强制性数字身份或年龄验证要求，从而改变当前网络匿名访问的现状。对隐私捍卫者、开源项目开发者及更广泛的互联网用户而言，这一趋势具有显著风险。文章自身并未提供详细立法文本，分析立场明显，实际法律走向和可执行性仍存在不确定性。

hackernews · slowin · 8月10日 23:45 · [社区讨论](https://news.ycombinator.com/item?id=49251411)

**「背景」** 英国《适龄设计准则》（Age Appropriate Design Code，AADC）要求在线服务对未成年用户进行年龄核验并加强隐私保护，英国非政府组织 5Rights 正向美国各州推广这一模式。加利福尼亚州的 AB 2273（《加州适龄设计准则法案》）便直接借鉴了英国 AADC，要求对 16 至 17 岁用户取得家长同意、通过第三方数字身份验证年龄等。批评者认为，这类以儿童安全为名的数字身份法可能迫使所有成年用户放弃匿名上网，从而威胁网络自由。

**「影响」** 若相关方向落地，成年用户的匿名网络访问可能受限，开源开发者也可能因被牵连的年龄验证或身份法律而面临刑事风险；不过这些后果主要来自评论者的担忧，尚未有正式立法确认。

**「社区讨论」** 多数评论者批评“儿童安全”话术被用作推动数字身份和反匿名政策的工具，质疑政策制定者容易受此类叙事影响。也有观点提醒，完全否定家长对儿童保护的合理关切，反而会削弱反对者的公信力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Social_media_age_verification_laws_in_the_United_States">Social media age verification laws in the United States - Wikipedia</a></li>
<li><a href="https://www.effort.news/uk-lobby">The UK ’s War on Anonymity Has Come to America — Effort</a></li>
<li><a href="https://spectrum.ieee.org/californias-proposed-law-could-change-the-internet">AB 2273 could be a sea change for online privacy - IEEE Spectrum</a></li>

</ul>
</details>

**标签**: `#privacy`, `#anonymity`, `#digital identity`, `#legislation`, `#child safety`

---

<a id="item-tech-news-3"></a>
### [Meta 开源 Muse Glimmer 30B 本地代理模型](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) ⭐️ 8.0/10

Meta 发布了 Muse Glimmer，一个 30B 参数的开放权重模型，专为常驻（always-on）本地代理工作流优化。Meta 同时宣布将开放其最新基础模型 Muse Spark 1.2 的权重，扩大自托管选项。社区反馈显示，该模型可在 32GB 内存的 Mac mini 上通过 Ollama 本地运行，但速度偏慢；Unsloth 已上传量化版本。这一发布被视为“稠密 30B 模型回归”趋势的一部分，并可能与即将发布的 Qwen3.8 27B 形成竞争。

hackernews · riordan · 8月10日 10:10 · [社区讨论](https://news.ycombinator.com/item?id=49241679)

**「背景」** Muse Glimmer 是 Meta Superintelligence Labs 于 2026 年 8 月 10 日发布的 300 亿参数开放权重智能体模型，采用 Apache 2.0 许可，专为在单块消费级 GPU 上运行常驻本地智能体工作流而优化。它是从 Meta 在 4 月推出的闭源前沿模型 Muse Spark 蒸馏而来的多模态模型，并且 Meta 还宣布将在未来几周内发布最新基础模型 Muse Spark 1.2 的开放权重版本，进一步扩展自托管选择。

**「影响」** 对自托管用户而言，Muse Glimmer 提供了可实际在本地硬件运行的 30B 代理模型，社区实测显示在 32GB Mac mini 上可用但响应较慢，量化版本可降低部署门槛；Muse Spark 1.2 的开放权重则进一步丰富了美国开源权重模型的选择。

**「社区讨论」** 评论者普遍对这一发布持积极态度，但也存在分歧：有人期待与本周将发布的 Qwen3.8 27B 对比，认为稠密 30B 模型重新流行；另一些人则强调 Muse Spark 1.2 开放权重更具战略意义，并预测本地小模型将取代大型数据中心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model">Introducing Muse Glimmer: An Open Agentic Model That Runs on Your ...</a></li>
<li><a href="https://www.marktechpost.com/2026/08/10/meta-ai-releases-muse-glimmer/">Meta AI Releases Muse Glimmer: A 30B Open-Weights Agentic Model That ...</a></li>
<li><a href="https://rits.shanghai.nyu.edu/ai/meta-releases-muse-glimmer-a-30b-agent-model-for-a-single-gpu/">Meta Releases Muse Glimmer, a 30B Agent Model for a Single GPU</a></li>
<li><a href="https://gadgetsnow.indiatimes.com/laptops-pc/meta-opens-muse-glimmer-a-30b-agent-model-for-laptops/articleshow/133100438.cms">Meta Opens Muse Glimmer, A 30B Agent Model For Laptops</a></li>

</ul>
</details>

**标签**: `#meta`, `#llm`, `#local-ai`, `#agentic`, `#open-source`

---

<a id="item-tech-news-4"></a>
### [手工编写 Transformer 权重实现 100%精确乘法](https://www.reddit.com/r/MachineLearning/comments/1vkrnb5/transformers_are_famously_bad_at_arithmetic_so_i/) ⭐️ 8.0/10

开发者/u/notforrob 用自己写的编译器 Torchwright，将竖式乘法算法编译成 Phi-3 Hugging Face 检查点的权重，完全不训练即让普通 Transformer 精确乘法。三位数计算器覆盖全部 3,000,000 个受支持表达式，准确率 100%；已发布支持到 12 位乘 12 位的检查点。他还对比六款前沿模型（关闭推理），数字变长后准确率骤降，七位数时五款模型 500 题全错，而他的版本保持 100%。共实现四种版本：竖式、硬件风格、草稿本和暴力记忆，它们在层数、宽度、生成 token 和参数使用上差异很大。这项工作展示用权重直接编程可以实现训练模型难以达到的精确算术。

reddit · r/MachineLearning · /u/notforrob · 8月10日 17:37

**「背景」** Transformer 通常通过大量训练学习统计规律，但做精确算术（如多位乘法）时容易出错。这个项目改变思路：不训练，而是把算法手动编译成网络权重，用 Torchwright 把计算图写入 Phi-3 检查点，让原有架构在推理时执行准确计算。

**「影响」** 对关注可解释性和权重级可编程性的 ML 从业者而言，这个项目证明无需训练即可在标准 Transformer 中实现精确算术，也为在推理时嵌入确定性算法提供了一条可行路径。

**标签**: `#transformers`, `#arithmetic`, `#weight compilation`, `#interpretability`, `#machine learning`

---

<a id="item-tech-news-5"></a>
### [Needle2：14MB 端侧 Agentic LLM，主打工具调用与结构化提取](https://cactuscompute.com/needle) ⭐️ 7.0/10

Needle2 是一个 14MB 的 agentic 大语言模型，面向手机、可穿戴设备、智能家居和机器人；整个模型是单一 14MB 二进制，完整会话仅需 28MB RAM，拥有 45M 参数并以 2bit 压缩。它在 Raspberry Pi 5 上可达 500 tokens/s 解码速度，在 Meta Quest 3S 和 Apple Vision Pro 等 VR 设备上为 400–1500 tokens/s，在三星 A 系列等 200 美元以下手机上为 300–700 tokens/s，并声称在工具调用和移动设备使用基准上与 LFM2.5 230M、Apple Foundation Model 互有胜负，体积却小 5 到 70 倍。模型基于作者提出的 Simple Attention Networks，每次 token 处理约需 70 MFLOP；Needle 2 新增结构化提取能力，可通过传入 schema 代替工具返回结构化输出，并支持在 Mac/PC 上数分钟到数小时内完成微调。作者强调它面向无 NPU、低功耗和低成本设备，并内置 Cactus Hybrid 置信度评分，低于阈值时可升级到云端或更大模型。

hackernews · HenryNdubuaku · 8月10日 17:22 · [社区讨论](https://news.ycombinator.com/item?id=49246804)

**「背景」** Needle（现为 Needle 2）是 Cactus Compute 推出的超小型智能体大语言模型，单文件 14MB，约 4500 万参数，采用论文提出的 Simple Attention Networks 架构，并以 Cactus Quants 的 CQ2-bit 压缩后运行在自研引擎中。与常规 Transformer（如同样尺寸需 87–164 MFLOPs/词元）相比，它每词元只需约 70 MFLOPs，目标设备是手机、手表、智能家居、树莓派和机器人等低功耗边缘设备。其主要用途不是自由文本生成，而是把自然语言映射到带类型参数的函数调用，例如工具调用与结构化提取。

**「影响」** 对边缘 AI 开发者，Needle 2 让工具调用与结构化提取能在树莓派、VR 头显和低端安卓手机等设备上以数百 tokens/s 本地运行，无需 NPU 或高端 GPU。不过，开发者需要依赖置信度阈值和云端升级机制，避免把简单意图误判（如“调暖”被识别为制冷）直接当作最终动作。

**「社区讨论」** 社区中有人看好“微型 LLM”作为分层模型体系的最底层，rcarmo 已在项目中把 Needle 用作 router，arthuqa 也想将 270M 模型压到 1–2bit 并称赞微调流程方便。但多位用户指出演示中模型语义理解有限：dbeardsl 的“调暖一点”被识别成 65°F 制冷，Tiberium 的简单查询被识别为默认锁前门且置信度为 0。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cactuscompute.com/needle">Needle 2 - The 14 MB Agentic LLM for Tiny Devices | Cactus</a></li>
<li><a href="https://github.com/cactus-compute/needle">GitHub - cactus-compute/needle: 14MB foundation model for tiny devices; phones, wearables, smart home, and robots. · GitHub</a></li>
<li><a href="https://medium.com/@creativeaininja/needle-is-a-14mb-tool-calling-model-the-agent-architecture-underneath-it-is-the-real-news-cd9595ba3f99">Needle Is a 14MB Tool-Calling Model. The Agent Architecture Underneath It Is the Real News. | by Kristopher Dunham | Medium</a></li>

</ul>
</details>

**标签**: `#edge-ai`, `#tiny-llm`, `#agentic-models`, `#on-device`, `#tool-calling`

---

<a id="item-tech-news-6"></a>
### [扎克伯格抨击封闭 AI 对手 Meta 回归开放模型](https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878) ⭐️ 7.0/10

Meta 首席执行官 Mark Zuckerberg 公开抨击封闭式 AI 竞争对手，并宣布 Meta 将回归开放权重模型路线。他在 Meta 官网上发表文章，主张 AI 未来应属于所有人，认为以安全为由集中 AI 权力存在根本性问题。这一立场凸显了 Meta 与 OpenAI、Anthropic 等闭源 AI 公司之间的路线分歧，也让开源与闭源 AI 的争论更加激烈。

hackernews · root-parent · 8月10日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=49243880)

**「背景」** Meta 在 2023 年发布 Llama 系列模型，被视为开源 AI 竞赛的开端；2024 年发布的 Llama 3.1 405B 被称作首个开源的前沿 AI 模型，在多项基准测试中击败了 GPT-4o 等闭源模型。扎克伯格一直主张更开放的 AI 发展路线，并批评苹果等公司的封闭生态系统。Meta 首席 AI 科学家 Yann LeCun 早在 Llama 推出前就在 Meta 内部围绕开源工作建立了 AI 研究体系。

**「影响」** 对开发者与开源社区而言，Meta 重新拥抱开放权重模型可能降低对封闭商用 API 的依赖，并被视为开源与商用 AI 采用的一个潜在转折点。不过，结合此前报道中 Meta 向付费 AI 模型倾斜的策略，其开放姿态的商业动机仍存在不确定性，实际影响取决于后续版本许可、开放程度与支持承诺。

**「社区讨论」** 社区评论对此反应不一：有用户认为这是毫无疑问的好事，开源 AI 越多越好；也有用户怀疑 Meta 动机，指出其一周前才发布封闭模型且无人购买后才转为开源。另有人质疑“打不过就改规则”，认为这是 Meta 在竞争压力下的策略调整。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=Vy3OkbtUa5k">Mark Zuckerberg on Llama 3.1, Open Source , AI Agents... - YouTube</a></li>
<li><a href="https://fortune.com/2024/11/19/zuckerberg-meta-ai-openai-llama/">How Mark Zuckerberg went all-in to make Meta a major AI ... | Fortune</a></li>
<li><a href="https://theoutpost.ai/news-story/meta-launches-open-source-ai-model-llama-3-1-challenging-industry-giants-1262/">theoutpost. ai /news-story/ meta -launches- open - source - ai -model- llama ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2025-12-10/inside-meta-s-pivot-from-open-source-to-money-making-ai-model">Inside Meta’s Pivot From Open Source to Money-Making AI Model - Bloomberg</a></li>
<li><a href="https://www.ico-optics.org/meta-releases-powerful-new-open-source-ai-model/">Meta Releases Powerful New Open Source AI Model – ICO Optics</a></li>

</ul>
</details>

**标签**: `#Meta`, `#open-source AI`, `#Llama`, `#AI industry`, `#open vs closed AI`

---

<a id="item-tech-news-7"></a>
### [Rust SIMD 在 GPU 上的应用引发稳定版与可移植性讨论](https://www.vectorware.com/blog/simd-on-gpu/) ⭐️ 7.0/10

一篇博客文章讨论了将 Rust 的可移植 SIMD 应用于 GPU，引发社区关于稳定版可用性和性能可移植性的讨论。评论指出 Rust 标准库的 portable SIMD 目前仅在 nightly 上可用，例如 FFT crate 作者因此改用 fearless\_simd crate 以在 stable 上获得可移植 SIMD。还有评论质疑现有示例的可移植性，因为固定 SIMD 宽度导致无法做到性能可移植。也有人希望出现一个成熟度堪比 C++ Google Highway 的开源 Rust SIMD 库。讨论中还包括对 Rust GPU 复杂算法（如基数排序）竞争力表现的疑问。

hackernews · sagacity · 8月10日 18:12 · [社区讨论](https://news.ycombinator.com/item?id=49247477)

**「背景」** Rust 的可移植 SIMD（portable SIMD，即 std::simd）提供一种通用向量类型，可根据目标 CPU 的向量指令自动映射；不过它目前只在 nightly Rust 中可用。VectorWare 团队认为 GPU 本质上也是另一种“向量硬件”，因此尝试把 portable SIMD 的目标扩展到 GPU，使同一套抽象能覆盖 CPU 与 GPU 向量指令。与此同时，社区中的 fearless\_simd crate 提供了一套在 stable Rust 上可用的可移植 SIMD 方案，通过编译多个版本并在运行时根据指令集分派来选择最优实现。

**「影响」** 对 Rust 开发者而言，stable 版上使用可移植 SIMD 仍缺乏标准方案，需依赖 fearless\_simd 等第三方 crate，且现有方案的性能可移植性受限于固定 SIMD 宽度。

**「社区讨论」** 评论者普遍认为标准 portable SIMD 的 nightly 限制是主要痛点，并转向 fearless\_simd；同时有人质疑固定 SIMD 宽度损害性能可移植性，也有人呼吁类似 Google Highway 的成熟 Rust 库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vectorware.com/blog/simd-on-gpu/">Vectorware</a></li>
<li><a href="https://www.vectorware.com/blog/threads-on-gpu/">Rust threads on the GPU</a></li>
<li><a href="https://crates.io/crates/fearless_simd">fearless_simd - crates.io: Rust Package Registry</a></li>
<li><a href="https://raphlinus.github.io/rust/simd/2018/10/19/fearless-simd.html">Towards fearless SIMD | Raph Levien’s blog</a></li>

</ul>
</details>

**标签**: `#Rust`, `#SIMD`, `#GPU`, `#portable-simd`, `#systems programming`

---

<a id="item-tech-news-8"></a>
### [Anthropic 研究展示 Claude 在黎曼 zeta 函数上的数学推理进展](https://www.anthropic.com/research/riemann-zeta) ⭐️ 7.0/10

Anthropic 发布研究，展示其大语言模型 Claude 在数学推理方面的进展，研究对象为黎曼 zeta 函数。研究中，Claude 的交互者 Jarred 主要发送“继续”或“相信你自己”等鼓励信息，而非提供技术指导，Claude 仍能取得有意义的进展，显示模型在复杂数学问题上的自主推理能力有所提升。这一工作被视为 AI 推理能力发展的一个具体案例，但具体方法与结论的细节尚未在本次内容中完整披露。

hackernews · tosh · 8月10日 17:41 · [社区讨论](https://news.ycombinator.com/item?id=49247070)

**「背景」** 黎曼猜想是数学中最著名的未解问题之一，它与黎曼ζ函数非平凡零点的分布有关。Anthropic 在一项研究中让一个未发布的 Claude 模型（由工程师 Jarred Sumner 在 Claude Code 中凭借提示驱动）尝试解决该问题，模型结合了近期的人类论文，将黎曼ζ函数零点的一个已证明下界从 41.6% 提升至 67.2%。这展示了大型语言模型在数学推理方面可能具备的潜力。

**「影响」** 这项研究为理解 Claude 在数学推理上的能力提供了新的实证案例，可能促使 AI 研究社区进一步探索鼓励性交互等提示方式对大型语言模型推理表现的实际影响。

**「社区讨论」** 评论者以幽默方式回应此事，有人感叹当代 AI 交互方式的荒诞，有人建议使用自动“鼓励”插件防止模型在难题前放弃，还有人分享了 Claude 在未见于文献的数学问题上获得结果的个人经验，并惊讶于这一进展未能在 HN 首页获得更多关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/riemann-zeta">Learning more about Claude &#x27;s mathematical capabilities \ Anthropic</a></li>
<li><a href="https://digg.com/tech/rep4a9q0">Claude Raises Riemann Zeta Bound from 41.6 to 67.2 Percent · Digg</a></li>
<li><a href="https://www.datacamp.com/tutorial/claude-and-the-riemann-hypothesis">Claude Tried the Riemann Hypothesis. Here&#x27;s What... | DataCamp</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#mathematics`, `#machine learning`

---

<a id="item-tech-news-9"></a>
### [超长中断触发 SMM 代码执行](https://github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii) ⭐️ 7.0/10

安全研究员 xoreaxeaxeax 在 GitHub 仓库 smiiiiiiiiiiiiiiii 中演示了一种利用超长指令进入系统管理模式（SMM）执行代码的技术。该攻击需要 root 权限，不属于可直接远程利用的普遍威胁，但展示了攻击者获得 root 后能进一步深入硬件控制。SMM 是 x86 中比操作系统更底层的固件执行环境，代码在 SMI（系统管理中断）触发后运行。方法依赖平台在 SMI 处理期间设置的超时机制：固件设计者预期了这种攻击，但把超时值的选择交给平台实现者，且要求超时长于系统中可能的最长 I/O 操作。

hackernews · WhiteDawn · 8月10日 16:03 · [社区讨论](https://news.ycombinator.com/item?id=49245491)

**「背景」** 系统管理模式（SMM）是 x86 处理器中一种用于固件（如 BIOS/UEFI）的最高特权执行模式，通常由系统管理中断（SMI）触发，操作系统和普通软件无法直接访问其内存区域。该研究展示的攻击思路是构造一个极长的中断/指令，使处理器在执行过程中进入 SMM，从而在底层硬件层面执行任意代码；但由于攻击者需要 root 权限，这更多是安全研究中的概念验证，而非面向大众的普遍威胁。

**「影响」** 影响集中在固件和平台实现者：他们必须按注释要求选择足够长的 SMI 超时值，使其长于系统中可能的最长 I/O 操作，否则持有 root 权限的攻击者可能借超长指令在 SMM 中执行代码；对普通用户，由于需要 root，直接危害有限。

**「社区讨论」** 评论者大多认为这更像“重新拿回硬件控制权”而不是漏洞，因为需要 root；有人引用固件源码指出厂商已预期此类攻击但把超时参数交给平台实现者。也有人注意到 README 用超长代码块来强调“超长指令”的幽默表达，并讨论攻击是否要求超长指令正好与 SMM 操作产生交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eucloudservers.com/security-encryption/exploiting-system-management-mode-with-a-very-long-interrupt/">Exploiting System Management Mode With A Very Long Interrupt</a></li>

</ul>
</details>

**标签**: `#system management mode`, `#hardware security`, `#low-level programming`, `#exploit`, `#x86`

---

<a id="item-tech-news-10"></a>
### [Fru：Rust 编写的高性能随机森林库](https://www.reddit.com/r/MachineLearning/comments/1vkrvks/fru_fast_random_forest_implementation_p/) ⭐️ 7.0/10

Fru 是一个用 Rust 开发的高性能随机森林实现，提供 Python 和 R 绑定，相关论文已发表在 Software X 期刊。在 Python 中，它的运行速度比 scikit-learn 快数倍，某些场景可达数百倍；在 R 中通常比 ranger 快几十个百分点，部分用例可达数倍。实现包含新颖的排列重要性计算方法，能进一步优化性能。其分层设计便于绑定，并通过 Arrow PyCapsule 与 pandas、polars、pyarrow 等库无缝协作。

reddit · r/MachineLearning · /u/kpiwonski · 8月10日 17:45

**「背景」** 随机森林是一种基于决策树集成的机器学习算法，常用于分类和回归。scikit-learn 是 Python 的主流实现，ranger 是 R 中常用的高效实现。Fru 通过 Rust 底层优化和高性能计算策略，在这些环境中提供了更快的训练速度，并借助 Arrow PyCapsule 实现跨库数据交换。

**「影响」** 使用 Python 或 R 进行随机森林训练的开发者，可以在保持模型功能的同时显著缩短训练时间，尤其在大规模数据集和需要多次试验的场景中收益明显。

**标签**: `#random forest`, `#Rust`, `#machine learning`, `#performance`, `#open source`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [英伟达联手六家资管公司，拟为 AI 基础设施融资 5000 亿美元](https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html) ⭐️ 8.0/10

英伟达周一宣布，已与阿波罗、黑石、贝莱德、Brookfield、高盛和 KKR 六家资产管理公司签署谅解备忘录，拟筹集超过 5000 亿美元第三方资金，用于帮助客户建设数据中心和购买英伟达硬件。英伟达 CEO 黄仁勋在 CNBC 采访中称，芯片已成为“可投资资产”。

rss · CNBC Finance · 8月10日 22:09

**「背景」** 此前图形处理器（GPU）通常被视为快速折旧的硬件，而英伟达此次试图把 AI 算力变成可抵押、可产生收入的长期基础设施，类似于商业地产或收费公路。

**「影响」** 这一计划若落地，超大规模云厂商、前沿 AI 实验室和企业可借助外部资本建设算力，无需自行承担全部资金压力；但怀疑者认为芯片价值可能随新一代产品推出而缩水。

**标签**: `#Nvidia`, `#AI infrastructure`, `#financing`, `#asset management`, `#compute`

---

<a id="item-finance-news-2"></a>
### [美股午盘重大异动：并购、增发与评级调整](https://www.cnbc.com/2026/08/10/stocks-making-the-biggest-moves-midday-ntap-intc-aapl-docs-vrsk.html) ⭐️ 7.0/10

美股午盘多只个股因并购、法院裁决和券商评级调整大幅波动：MarineMax 同意以每股 53 美元现金（约 15 亿美元）出售给 Blackstone 旗下 Safe Harbor Marinas，股价上涨 46%；Varex Imaging 被 Teledyne 以每股 18.90 美元现金收购，股价上涨 48%。Intel 宣布发行 150 亿美元普通股后下跌近 3%，Verisk 因法院裁定须推进 23.5 亿美元收购 AccuLynx 而下跌逾 5%。

rss · CNBC Finance · 8月10日 19:19

**「背景」** 该报道汇总午盘时段主要异动，其中 Verisk 此前在 12 月因 FTC 审查未于截止日前完成而终止对 AccuLynx 的收购，法院裁决要求其继续推进；Intel 则通过发行新股筹集资金。

**标签**: `#mergers and acquisitions`, `#stock movers`, `#analyst actions`, `#equity offering`, `#tech stocks`

---

<a id="item-finance-news-3"></a>
### [盘前异动：英特尔、Verisk、伯克希尔等](https://www.cnbc.com/2026/08/10/stocks-making-the-biggest-moves-premarket-aapl-hpe-rklb-and-more.html) ⭐️ 7.0/10

英特尔宣布将发行 150 亿美元普通股，用于一般公司用途；Verisk Analytics 因特拉华州法官裁定其必须完成 23.5 亿美元收购 AccuLynx，股价盘前跌逾 6.5%。伯克希尔·哈撒韦公布第二季度运营利润同比增长 16%，而 GameStop 据彭博社报道正考虑放弃对 eBay 的 560 亿美元收购。

rss · CNBC Finance · 8月10日 13:52

**「背景」** Verisk 此前因美国联邦贸易委员会对该交易的审查未在截止日期前完成，于去年 12 月终止了与 AccuLynx 的收购协议。

**标签**: `#Intel`, `#Berkshire Hathaway`, `#Verisk Analytics`, `#GameStop`, `#M&amp;A`

---