---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> 从 144 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [GLM-5.3 开放权重模型发布](#item-tech-news-1) ⭐️ 9.0/10
2. [Htmx 4.0 发布：新特性与社区讨论](#item-tech-news-2) ⭐️ 8.0/10
3. [OpenAI 在 SpaceX 收购 Cursor 后决定切断其模型访问](#item-tech-news-3) ⭐️ 8.0/10
4. [谣言即漏洞：AI 让安全披露浪潮加剧](#item-tech-news-4) ⭐️ 8.0/10
5. [在 RP2350 微控制器上运行极简潜流 Transformer 图像生成模型](#item-tech-news-5) ⭐️ 8.0/10
6. [美国制裁 A/I 集体引发基础设施安全担忧](#item-tech-news-6) ⭐️ 7.0/10
7. [OpenAI Python SDK 迁移至 HTTPX2](#item-tech-news-7) ⭐️ 7.0/10
8. [柏林遭黑客勒索，市长拒绝屈服](#item-tech-news-8) ⭐️ 7.0/10
9. [美国数据中心环保争议升温：多州暂停新建项目](#item-tech-news-9) ⭐️ 7.0/10

**科技博客**
1. [《异克斯小队》试玩：三人联机 PVE 的蓝领打工体验](#item-tech-blog-1) ⭐️ 4.0/10

**财经新闻**
1. [玉米和小麦价格创三年多新高](#item-finance-news-1) ⭐️ 8.0/10
2. [美上诉法院裁定体育赛事合约非联邦监管掉期，预测市场纠纷或上诉至最高法院](#item-finance-news-2) ⭐️ 8.0/10
3. [Warsh 讲话后 9 月美联储加息概率升至约 56%](#item-finance-news-3) ⭐️ 8.0/10
4. [美股盘前：PayPal 大跌，Affirm 等财报超预期上涨](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [GLM-5.3 开放权重模型发布](https://huggingface.co/zai-org/GLM-5.3) ⭐️ 9.0/10

Z.ai 在 Hugging Face 上发布了开放权重模型 GLM-5.3，并在 z.ai/blog 上提供了技术说明。社区早期反馈显示，该模型在复杂推理任务上表现出色，能够处理高难度问题，且比 DeepSeek Flash 等同类模型更高效。有用户认为其能力略逊于 Kimi，但大幅降低了本地或第三方部署的硬件门槛，预计推理成本和速度更具吸引力。GLM-5.3 作为开放权重模型，使开发者能够在不依赖闭源 API 的情况下获得接近顶尖闭源模型的体验，有用户称其体验感觉像 Opus 4.8。

hackernews · jeudesprits · 8月28日 15:20 · [社区讨论](https://news.ycombinator.com/item?id=49479878)

**「背景」** GLM-5.3 是 Z.ai 最新发布的开放权重模型，它在 GLM-5.2 的基础上通过后训练优化而来，官方称其在代码与智能体基准上取得了显著提升。开放权重意味着模型参数和权重可以公开下载与部署，这使开发者能够在自有硬件或第三方服务上运行模型，而不必仅依赖厂商的托管 API。在社区讨论中，它常被拿来与 DeepSeek、Kimi 等模型比较，并被认为在推理能力和运行成本之间取得了较好的平衡。

**「影响」** 对于需要在本地或第三方平台部署高性能模型的开发者，GLM-5.3 提供了比同等能力模型更低的运行门槛和成本预期，可能加速相关应用生态向开源权重迁移。

**「社区讨论」** 社区普遍对 GLM-5.3 持正面评价，认为其推理能力接近领先闭源模型，并在运行效率和成本上有优势；也有用户强调其仍需要高端硬件（如双路 DGX Sparks 或 Mac M5 Ultra 512GB 统一内存）才能发挥最佳性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kie.ai/blog/what-is-glm-5-3">What Is GLM - 5 . 3 ? Z . ai &#x27;s Next Open - Weight Model</a></li>
<li><a href="https://glm-ai.chat/models/glm-5-3/">GLM - 5 . 3 : Specs , API, Pricing and Benchmarks</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-weights`, `#AI`, `#GLM-5.3`, `#model-release`

---

<a id="item-tech-news-2"></a>
### [Htmx 4.0 发布：新特性与社区讨论](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) ⭐️ 8.0/10

Htmx 4.0.0 于 2026 年 8 月 28 日发布，为这一广受关注的开源超媒体库带来重大版本更新。新版本包含 \`hx-alpine-compat\` 等用于平滑衔接 Alpine.js 的兼容改进，继续强化服务端渲染驱动的交互方式。不过，有开发者在尝试后指出，Htmx 在特定场景下并非体积最优，例如他们转向了更小的 alpine-ajax 库。社区整体肯定了 htmx 的简洁性，但也有人提出，在以 .NET API 后端加 Angular 前端的架构中，使用 htmx 意味着将界面生成移回后端，可能增加复杂度。

hackernews · rmsaksida · 8月28日 13:28 · [社区讨论](https://news.ycombinator.com/item?id=49478178)

**「背景」** htmx 是一个以超媒体为中心的 JavaScript 库，允许开发者通过 HTML 属性直接使用 AJAX、CSS 过渡、WebSocket 和服务器发送事件，从而减少对复杂前端 JavaScript 框架的依赖。htmx 4.0.0 是该库的主要版本更新，官方将其内部重构为基于 fetch\(\) API，并提供了从 htmx 2.x 迁移到 4.x 的升级指南。根据早期的开发说明，4.0 的稳定版计划在 2026 年初至年中发布，而 2.x 会继续作为 npm 最新标签保留到 2027 年初。

**「影响」** 对于偏好服务端渲染或轻量前端栈的开发者，Htmx 4.0 提供了一条保持简单与快速响应的交互实现路径；而对于依赖 API 后端与 SPA 前端的团队，它可能要求重新混合表现层与业务逻辑，带来架构上的额外权衡。

**「社区讨论」** 评论中的共识是 htmx 带来了简洁和愉悦的开发体验，特别是搭配 Go 与 SQLite 等简单技术栈；但存在明显分歧：有开发者认为它在 API 后端加前端框架的设定下反而更复杂，也有开发者表示 alpine-ajax 比 htmx 更小且功能足够，甚至得到了官方项目的认可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released">htmx 4 . 0 . 0 has been released ! ~ htmx</a></li>
<li><a href="https://medium.com/django-journal/htmx-4-0-alpha-in-django-fetch-api-superpowers-for-real-time-uis-early-benchmarks-vs-htmx-2-x-2b68407a22cc">HTMX 4 . 0 Alpha in Django: Fetch API Superpowers for... | Medium</a></li>
<li><a href="https://web.archive.org/web/20251103222343/https://htmx.org/essays/the-fetchening/">htmx ~ The fetch() ening</a></li>

</ul>
</details>

**标签**: `#htmx`, `#web-development`, `#hypermedia`, `#javascript`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [OpenAI 在 SpaceX 收购 Cursor 后决定切断其模型访问](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 8.0/10

OpenAI 宣布，在 SpaceX 收购 Cursor 之后，将停止向 Cursor 提供 OpenAI 模型的访问权限。这一决定直接影响了 Cursor 用户通过该工具使用 OpenAI 模型的能力，也反映出前沿 AI 实验室之间围绕模型供应和竞争格局的紧张态势。作为一款广泛使用的 AI 编程工具，Cursor 此前依赖转售多家模型提供商的 API 来提供服务。目前尚不清楚该限制的具体生效时间，以及是否会影响 Cursor 现有订阅用户。此举可能促使部分用户转向 Anthropic 等替代模型或工具。

hackernews · meetpateltech · 8月29日 01:47 · [社区讨论](https://news.ycombinator.com/item?id=49486172)

**「背景」** OpenAI 已通知 SpaceX，计划终止向 Cursor 提供 OpenAI 模型的合约，拟议的关闭日期为 2026 年 11 月 12 日。此前 SpaceX 以约 600 亿美元收购了 Anysphere 的 Cursor，而 Cursor 本来就在使用大量 xAI 芯片，并有资深工程师转投 xAI，这使 Cursor 成为与 xAI/Grok 深度绑定的编码工具。与此同时，Anthropic 今年早些时候也因类似的条款违规问题禁止了 xAI 使用其模型，因此 OpenAI 此举被视为在模型访问竞争中对收购后 Cursor 的回应。

**「影响」** Cursor 用户将无法继续在 Cursor 中直接使用 OpenAI 模型，依赖这一集成的开发者需要寻找替代的模型供应商或编码工具。

**「社区讨论」** 评论普遍认为 Cursor 转售其他 API 的商业模式本就难以为继，并指出 Anthropic 此前曾因类似的服务条款违规封禁 xAI，因而猜测其是否会同样封禁 Cursor。也有用户表示，自己作为 Cursor 和 Claude 订阅者，会因此更倾向回到 Anthropic，或继续只使用 Grok 和 Composer 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/aamir-shah-728295148_elonmusk-spacex-cursor-activity-7472656157015298048-g84O">SpaceX Acquires Anysphere&#x27;s Cursor for $60B | Aamir... | LinkedIn</a></li>
<li><a href="https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/">Our decision on Cursor following its acquisition by SpaceX | OpenAI</a></li>
<li><a href="https://politicalos.io/story/spacex-cursor-acquisition">SpaceX Acquisition of Cursor — PoliticalOS | PoliticalOS</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Cursor`, `#AI models`, `#SpaceX`, `#model access`

---

<a id="item-tech-news-4"></a>
### [谣言即漏洞：AI 让安全披露浪潮加剧](https://anil.recoil.org/notes/rumour-is-the-exploit) ⭐️ 8.0/10

这篇文章指出，在 AI 与 LLM 的推动下，仅仅出现漏洞传闻就可能迅速被转化为可用的攻击程序，漏洞披露的速度和规模正在显著提升。这种变化降低了制作漏洞利用代码的门槛，使安全团队和开源维护者必须在更短时间内响应大量报告。作者认为，漏洞响应的负担已从“发现漏洞”转移到“筛选和修复由传闻催生的利用尝试”。文章强调，维护者正面临披露量激增的冲击，自动化分诊和修复协作变得日益必要。

hackernews · avsm · 8月28日 15:58 · [社区讨论](https://news.ycombinator.com/item?id=49480466)

**「背景」** 这篇文章讨论的是安全响应中的一个新现象：过去安全社区依赖漏洞保密（embargo）来争取修复时间，但现在大型语言模型（LLM）和 AI 工具能根据简短的漏洞传闻、补丁或提交信息，快速生成可利用的漏洞代码（PoC）。这导致安全披露的规模和速度急剧上升，也让传统的保密流程难以维持。例如，开源项目 rclone 的维护者反映，过去 10 年仅收到约 20 份安全披露，而最近一个月就超过 40 份，其中约 75% 需要实际查看，凸显了维护者面临的巨大压力。

**「影响」** 最直接的影响是开源维护者和安全团队收到的安全披露数量激增，即使其中不少是低质量或半成品利用，也需要大量时间去核验和修复；没有自动化分诊和优先级排序的项目很可能被淹没。

**「社区讨论」** HN 评论中，rclone 维护者 nickcw 报告称项目前 10 年约收到 20 份安全披露，而最近一个月超过 40 份，约 75% 都包含需要处理的问题。多名评论者指出真正瓶颈在于组织缺乏修复意愿和部署速度太慢，也有人认为利用补丁和提交消息拼凑 PoC 并非 LLM 时代的新现象，但 LLM 让这类攻击大规模民主化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49480466">Just the rumour of a bug is enough to find an exploit these days | Hacker News</a></li>
<li><a href="https://anil.recoil.org/notes/rumour-is-the-exploit">Just a rumour of a bug is enough to find a security exploit ...</a></li>

</ul>
</details>

**标签**: `#security`, `#AI`, `#open source`, `#vulnerabilities`, `#software engineering`

---

<a id="item-tech-news-5"></a>
### [在 RP2350 微控制器上运行极简潜流 Transformer 图像生成模型](https://www.reddit.com/r/MachineLearning/comments/1w10tax/i_implemented_a_very_tiny_image_generation_model/) ⭐️ 8.0/10

一位开发者成功在 RP2350 微控制器上实现了一个极小的潜流 Transformer 图像生成模型，该模型约有 240 万至 400 万参数，经 int8 量化后可完全在微控制器上运行，生成 128×128 人脸图像最长约需 20 秒，生成结果可通过显示器显示或经 USB 传输。模型包含 12 层，使用 AdaLN-Zero 进行条件化，并支持 CFG（分类器自由引导），作者表示 CFG 显著提升了图像质量。推理引擎通过 DMA 从闪存流式加载权重，同时计算上一层，并使用 ReLU²激活函数增加稀疏性以便跳过无效计算。作者称经过大量消融实验才达到这一效果，并对仅用如此少的参数取得的结果感到惊讶。

reddit · r/MachineLearning · /u/cpldcpu · 8月28日 19:48

**「背景」** RP2350 是树莓派推出的微控制器，常见于 Raspberry Pi Pico 2 等开发板，搭载双核 Arm Cortex-M33（也可选 RISC-V 核心），最高运行频率约 150MHz，并内置 520KB SRAM。它比前代 RP2040 具有更高的主频、双倍 SRAM 和更多闪存，支持 C、C++、Rust、MicroPython 等多种编程语言。在这样资源受限的微控制器上运行图像生成模型，需要借助量化、稀疏激活跳过和流式权重加载等优化手段，这正是帖子中实现的核心背景。

**「影响」** 该实现表明，借助量化、权重流式加载和稀疏激活等优化，生成式图像模型可以在低功耗微控制器上离线运行，为嵌入式 ML 和低成本边缘 AI 应用提供了具体可行的参考方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RP2350">RP2350 - Wikipedia</a></li>
<li><a href="https://smd-chip.com/en/IC_specification_rp2350-microcontroller-datasheet_1.html">RP2350 Datasheet - 150MHz Dual-Core Arm Cortex-M33 / RISC-V MCU with 520KB SRAM, 1.8-3.3V I/O, QFN-60/80 - English Technical Documentation</a></li>

</ul>
</details>

**标签**: `#embedded-ml`, `#image-generation`, `#efficient-inference`, `#microcontroller`, `#quantization`

---

<a id="item-tech-news-6"></a>
### [美国制裁 A/I 集体引发基础设施安全担忧](https://www.inventati.org/) ⭐️ 7.0/10

美国政府对意大利托管集体 Autistici/Inventati（A/I Collective）实施制裁，并将其运营 noblogs.org 等隐私服务的组织列入“全球恐怖分子”名单。此前 Hacker News 上已有两个相关讨论帖（分别有 131 条和 219 条评论）。此举被视为史无前例地针对基础设施提供者，引发对 I2P、Monero、Veilid、Tox、Signal 等去中心化网络和隐私工具用户及开发者是否会被波及的担忧。社区评论还提到，A/I 参与者曾参与意大利 Indymedia 和 2001 年热那亚 G8 抗议活动的媒体中心建设，但也有一些用户质疑该组织是否真与 PKK 有直接关联。

hackernews · exiguus · 8月28日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49477854)

**「背景」** Autistici/Inventati（A/I Collective）是一个成立于意大利、已运营约 25 年的隐私倡导与托管组织，为约 16,000 个邮箱和 1,500 个网站提供基础设施服务，其中包括知名博客平台 noblogs.org。2026 年 8 月 26 日，美国国务院与财政部依据第 13224 号行政令将其列为“特别指定全球恐怖分子”（SDGT），称其构建并运营“暴力反法西斯组织及其他极左激进分子”的数字基础设施。制裁允许在 2026 年 9 月 25 日前进行有限的逐步缩减活动，且此决定绕过了意大利法院和欧盟《数字服务法》的中介责任程序。

**「影响」** 根据用户报告，制裁已导致 noblogs.org 部分功能异常、autistici.org 下线，直接中断了依赖这些服务的隐私通信与博客托管。更深远的影响在于，该案为将基础设施提供者视为恐怖分子开创先例，可能对 I2P、Monero、Signal 等项目的开发者与用户形成寒蝉效应。

**「社区讨论」** 评论中，有用户强调把基础设施提供者列为“恐怖分子”是前所未有的危险信号，并援引该集体在热那亚 G8 抗议中的历史以说明其背景；另一些用户则指出难以找到该组织直接支持 PKK 的证据，并认为其网站和宣言不够清晰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.state.gov/releases/office-of-the-spokesperson/2026/08/designation-of-autistici-inventati-as-a-specially-designated-global-terrorist/">Designation of Autistici/Inventati as a Specially Designated ...</a></li>
<li><a href="https://cryptobriefing.com/us-sanctions-autistici-inventati-terrorism/">United States sanctions Autistici/Inventati for supporting ...</a></li>
<li><a href="https://peopleofinternet.com/articles/washington-s-terrorism-sanctions-on-an-italian-hosting.html">Washington&#x27;s Terrorism Sanctions on an Italian Hosting ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#open source`, `#internet infrastructure`, `#sanctions`, `#decentralization`

---

<a id="item-tech-news-7"></a>
### [OpenAI Python SDK 迁移至 HTTPX2](https://github.com/openai/openai-python/blob/main/httpx2.md) ⭐️ 7.0/10

OpenAI 的 Python SDK 正在迁移至 HTTPX2，这是一个承诺不会破坏现有 API 的 httpx 稳定分支。Anthropic 在几周前也做了同样的变更。此举的背景是 httpx 正朝着 1.0 版本迈进，而该版本将包含大量破坏性变更，因此 HTTPX2 作为更稳定的依赖项成为更合适的选择。这一变化会影响大量使用 OpenAI 和 Anthropic Python SDK 的开发者，并引发关于 AI 工具生态中依赖选择稳定性的讨论。

hackernews · tosh · 8月28日 11:51 · [社区讨论](https://news.ycombinator.com/item?id=49477212)

**「背景」** httpx 是 Python 常用的 HTTP 客户端库，OpenAI Python SDK 原先依赖它来支持同步与异步请求。HTTPX2 是 httpx 的一个版本/分支，OpenAI 文档称其与 httpx API 兼容、可直接替换常用 HTTP 客户端用法，因此 SDK 现在默认安装 HTTPX2 而不再依赖 httpx 包。此外，Anthropic 的 Python SDK 也在短时间内做了类似迁移，这一变化主要影响与 SDK HTTP 层交互的应用程序。

**「社区讨论」** 开发者们普遍理解这一变更是为了避免 httpx 1.0 的破坏性变更，但有人质疑是否评估过 niquests 等其他替代方案，也有人询问相比缺点，这一变更到底有哪些实际好处。另有评论者批评 OpenAI 出现的网络错误，还有人质疑此事为何登上首页。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/openai-python/blob/main/httpx2.md">openai-python/httpx2.md at main - GitHub</a></li>
<li><a href="https://developers.openai.com/api/reference/python">OpenAI Python API library | OpenAI API Reference</a></li>
<li><a href="https://github.com/openai/openai-python/issues/3375">Consider migrating from httpx to httpx2 #3375 - GitHub</a></li>

</ul>
</details>

**标签**: `#openai`, `#httpx`, `#python`, `#sdks`, `#dependency-management`

---

<a id="item-tech-news-8"></a>
### [柏林遭黑客勒索，市长拒绝屈服](https://www.bbc.co.uk/news/articles/cm2q7gv3l5qo?at_medium=RSS&amp;at_campaign=rss) ⭐️ 7.0/10

柏林市长凯·韦格纳证实，黑客在本月早些时候入侵城市系统并窃取数据后，正对柏林进行勒索。黑客要求支付 30 比特币（约合 200 万欧元或 170 万英镑），但韦格纳表示柏林不会屈服。攻击导致部分在线系统被迫关闭，调查人员正在查明被窃数据的内容。据路透社报道，名为 Rhysida 的黑客组织声称对此负责，并计划在七天后开始拍卖所窃取的 5.79 TB 数据。柏林官员表示，初步数据泄露发生在 8 月 7 日至 12 日之间，随后 8 月 14 日两个部门的网络被关闭，导致住房福利和支付申请数日无法办理，且不能排除个人数据被泄露的可能。

rss · BBC World · 8月28日 21:29

**「背景」** Rhysida 是一个自 2023 年 5 月出现的勒索软件即服务（RaaS）组织，通过钓鱼邮件和 Cobalt Strike 等工具入侵目标网络，加密数据并威胁公开泄露以索取赎金。该类攻击常采用“双重勒索”模式：受害者不仅要恢复系统，还要防止敏感数据被公开。Rhysida 曾攻击英国博物馆并在拒绝支付后公开约 50 万份文件，此次声称对柏林市政府网络攻击负责，宣称窃取 5.79TB 数据并计划在七天后拍卖，起拍价 30 比特币。柏林作为德国首都和城市州，本次攻击导致部分在线系统关闭，官方正在调查数据泄露范围。

**「影响」** 柏林市民的住房福利和支付申请曾中断数日，且个人数据可能已被泄露；由于市政府拒绝支付赎金，Rhysida 组织可能会在未来公开或拍卖被窃数据，进一步扩大隐私泄露风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rhysida_%28hacker_group%29">Rhysida (hacker group) - Wikipedia</a></li>
<li><a href="https://www.sentinelone.com/anthology/rhysida/">Rhysida Ransomware: In-Depth Analysis, Detection, Mitigation Analyzing Rhysida Ransomware Intrusion - Fortinet Ransom-DB | Live Threat Command Center 202308041500_Rhysida Ransomware Sector Alert_TLPCLEAR - HHS.gov Rhysida Ransomware: The Silent Serpent - Threat Actors rhysida - Ransomware Group | Ransomwhere.org</a></li>
<li><a href="https://www.fortinet.com/content/dam/fortinet/assets/threat-reports/rhysida-ransomware-intrusion.pdf">Analyzing Rhysida Ransomware Intrusion - Fortinet</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#ransomware`, `#data breach`, `#Berlin`, `#hacking`

---

<a id="item-tech-news-9"></a>
### [美国数据中心环保争议升温：多州暂停新建项目](https://www.theguardian.com/environment/2026/aug/19/is-the-environmental-impact-of-datacentres-finally-cutting-through) ⭐️ 7.0/10

美国国内对数据中心的反对情绪正跨越政治光谱蔓延。超过十二个州已考虑暂停新建数据中心，纽约州在 7 月成为首个实施临时禁令的州；参议员伯尼·桑德斯和众议员亚历山德里娅·奥卡西奥-科尔特斯提议全国性暂停，得克萨斯州州长格雷格·阿博特也呼吁在乡村地区禁止开发。公众开始关注这些设施对电费和环境的潜在影响。此事标志着 AI 和云计算基础设施可能面临更严格的监管约束。

rss · The Guardian International · 8月28日 16:20

**「背景」** 数据中心是支撑云计算和 AI 训练的高耗能设施，通常需要大量电力和水冷资源。此前其环境影响多被忽视，但随着扩张加速，地方社区开始担忧电网负荷、电价上涨和碳排放。

**「影响」** 这一政治反弹可能迫使科技公司在选址和能源采购上更加谨慎，并推动更透明的环境影响评估。若更多州或联邦层面落实限制，AI 基础设施的扩张速度或将放缓。

**标签**: `#datacentres`, `#regulation`, `#environmental impact`, `#AI infrastructure`, `#energy`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [《异克斯小队》试玩：三人联机 PVE 的蓝领打工体验](https://www.gcores.com/articles/218963) ⭐️ 4.0/10

rss · 机核GCORES游戏资讯 · 8月28日 14:30

**「背景」** 作者在 ChinaJoy 参加了三人联机 PVE 动作射击游戏《异克斯小队》的闭门试玩。游戏由 Behaviour Interactive 开发、腾讯与 Level Infinite 发行，玩家扮演“Exterminauts”，为一家巨型企业前往异星消灭生物、开采能源，玩法流程很容易让人联想到《绝地潜兵 2》。作者想看看这款新 IP 如何在该赛道中立足。

**「方案」** 试玩中，队长先选择任务目标，再配置主武器、特殊武器、道具和武器模组。作者起初被禁止使用模组，朴素体验类似《星际战甲》；装上模组后，他构筑了一套以暴击触发特效为核心的爆发配置，队友则选择了治疗生存路线，两人形成“输出+治疗”的极化配合，让他意识到模组构筑与队友配合才是核心乐趣。游戏同时设计了友军伤害和“复活枪”爆炸机制，以及从任务工资中扣除补给费用的公司预算系统，迫使玩家权衡资源消耗；玩家还能用电池超载“工具”式武器获得大范围杀伤，或超载谜题跳过流程。作者欣赏这些围绕蓝领劳保用品的美术细节和加班式临时任务，但也坦承两小时试玩没真正感受到黑心企业的叙事氛围和蓝领气质，这类体验是否成立要等正式版再判断。发行方计划以三月一赛季、六周一 Battle Pass 的节奏更新，售价不高于同类产品。

**「启示」** 作者认为《异克斯小队》的差异化在于“蓝领英雄”主题、强构筑配合和密集的长线运营，但成败取决于能否像《绝地潜兵 2》那样让玩家真正沉浸于为“公司卖命”的氛围，而不只是玩法相似。要想做到这点，团队应去倾听真实打工人的思考方式与困境。

**标签**: `#game-preview`, `#co-op-pve`, `#game-design`, `#exterminauts`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [玉米和小麦价格创三年多新高](https://www.cnbc.com/2026/08/28/corn-and-wheat-prices-jump-to-highest-prices-in-more-than-three-years.html) ⭐️ 8.0/10

玉米和小麦期货价格分别收于每蒲式耳 536.5 美分和 784 美分，均创三年多新高；小麦本周上涨 12.1%，为 2022 年 3 月以来最大周涨幅，玉米 8 月上涨 15.6%，有望创 2021 年 4 月以来最佳月度表现。

rss · CNBC Finance · 8月28日 20:00

**「背景」** 玉米上涨主要源于美国供应前景恶化：农业部下调单产预期至 180.7 蒲式耳/英亩，田间考察显示炎热天气损害作物；小麦上涨则因黑海地区俄罗斯与乌克兰出口中断，俄乌合计占全球小麦出口逾四分之一。

**「影响」** 若供应紧张持续，依赖进口谷物的国家和食品企业可能面临成本上升，进而推高全球食品通胀。

**标签**: `#wheat prices`, `#corn prices`, `#supply disruption`, `#USDA crop report`, `#Russia-Ukraine conflict`

---

<a id="item-finance-news-2"></a>
### [美上诉法院裁定体育赛事合约非联邦监管掉期，预测市场纠纷或上诉至最高法院](https://www.cnbc.com/2026/08/28/appeals-court-rules-against-prediction-markets-tees-up-scotus-fight.html) ⭐️ 8.0/10

美国第九巡回上诉法院裁定，Kalshi、Crypto.com 和 Robinhood 等平台提供的体育赛事相关“事件合约”不属于受美国商品期货交易委员会（CFTC）监管的掉期，而属于体育博彩，使州监管机构可以继续叫停这些产品。该裁决与第三巡回法院今年 4 月的裁决相冲突，形成“巡回法院分歧”，很可能促使美国最高法院受理此案。

rss · CNBC Finance · 8月29日 02:23

**「背景」** CFTC 和这些平台主张，所有事件合约无论标的是什么都是掉期，应由 CFTC 独家监管；44 个州则认为体育赛事合约只是体育博彩。该判决驳回平台的禁制令请求，而 CFTC 已就九州的监管权问题提起诉讼，坚持自身拥有排他管辖权。

**「影响」** 对 Kalshi、Crypto.com 和 Robinhood 而言，这在第九巡回法院辖区内意味着其体育赛事合约可能继续被州监管机构叫停；裁决公布后，DraftKings 和 Flutter 等传统体育博彩公司股价上涨，市场认为其竞争压力有所缓解。

**标签**: `#prediction markets`, `#CFTC`, `#regulation`, `#litigation`, `#derivatives`

---

<a id="item-finance-news-3"></a>
### [Warsh 讲话后 9 月美联储加息概率升至约 56%](https://www.cnbc.com/2026/08/28/-september-fed-decision-now-a-coin-flip-as-rate-hike-odds-increase.html) ⭐️ 8.0/10

美联储主席 Kevin Warsh 在杰克逊霍尔发表承诺对抗通胀的讲话后，市场对 9 月 16 日加息 25 个基点的概率大幅上升：CME FedWatch 显示约 56%，Kalshi 和 Polymarket 分别为 48%和 49%。讲话前，市场认为 9 月按兵不动的概率接近 70%。

rss · CNBC Finance · 8月28日 15:22

**「背景」** 7 月美联储会议后，投资者原本相当确信 9 月会加息，因三位 FOMC 委员反对维持利率不变；但 7 月就业报告弱于预期、通胀虽有回落仍高于 2%目标，过去一个月加息预期曾降温。Warsh 在讲话中说夏季通胀读数好于预期，但“不能告诉我潜在趋势已有意义改善”。

**标签**: `#Federal Reserve`, `#Interest Rates`, `#Monetary Policy`, `#Jackson Hole`, `#Market Expectations`

---

<a id="item-finance-news-4"></a>
### [美股盘前：PayPal 大跌，Affirm 等财报超预期上涨](https://www.cnbc.com/2026/08/28/stocks-making-the-biggest-moves-premarket-pypl-afrm-gap-mrvl.html) ⭐️ 7.0/10

美股盘前多只个股大幅波动。PayPal 跌近 16%，因彭博社援引知情人士称 Advent 和 Stripe 放弃收购；Affirm、Gap、Elastic 分别上涨 13%、近 15%和超 17%，受益于财报或指引超预期（Gap 还宣布 Old Navy 换帅）；Marvell、Autodesk、Rubrik 分别下跌约 8%、近 4%和超 5%，因指引或毛利率低于预期。

rss · CNBC Finance · 8月28日 11:43

**「背景」** PayPal 此前被报道可能成为大型杠杆收购对象；其他个股的盘前波动主要由最新季度财报或业绩指引引发。

**标签**: `#Earnings`, `#Mergers and Acquisitions`, `#Stock Movers`, `#PayPal`, `#Guidance`

---