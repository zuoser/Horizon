---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 168 条内容中筛选出 10 条重要资讯。

---

**科技新闻**
1. [OpenAI 发布 GPT-6 Sol 与 Luna：定价与用量引热议](#item-tech-news-1) ⭐️ 9.0/10
2. [WordPress 修复未授权路径遍历漏洞，可致条件性 RCE](#item-tech-news-2) ⭐️ 9.0/10
3. [Anthropic 发布 Claude Opus 5.5：降价与输出改进](#item-tech-news-3) ⭐️ 8.0/10
4. [五角大楼：过度依赖 AI 促成伊朗学校导弹袭击](#item-tech-news-4) ⭐️ 8.0/10
5. [Claude Opus 5.5 与 GPT-6 Sol/Luna 同日发布并掀起价格战](#item-tech-news-5) ⭐️ 8.0/10
6. [Complex KDA：扩展 Kimi Delta Attention 表达能力](#item-tech-news-6) ⭐️ 8.0/10
7. [FoxPro 复活：Rust/Wasm 新运行时兼容 VFP 9](#item-tech-news-7) ⭐️ 7.0/10
8. [Claude Opus 5.5 Max 档基准与成本讨论](#item-tech-news-8) ⭐️ 7.0/10
9. [QontoFAQ：面向产品 FAQ 检索的嵌入模型基准](#item-tech-news-9) ⭐️ 7.0/10

**科技博客**
1. [《女神异闻录 4 Revival》TGS2026 专访：重制的取舍](#item-tech-blog-1) ⭐️ 5.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 发布 GPT-6 Sol 与 Luna：定价与用量引热议](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI 宣布推出 GPT-6 Sol 和 Luna，相关话题在 Hacker News 上获得 1152 分和 597 条评论，成为高热度讨论。社区关注点集中在定价、代理（agent）工作流适配和使用限制，其中评论者 simonw 称 GPT-6 Luna 价格是 GPT-5.6 Luna 的一半，并提供了多组模型生成鹈鹕图的对比链接。由于官方来源内容缺失，现有材料未包含技术基准、上下文窗口、完整定价表或具体发布日期等可核实细节。因此，目前可以确认的是此次发布在实践层面引发强烈关注，但其技术深度与官方规格仍不明确。

hackernews · OfficialTurkey · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**「背景」** GPT-6 Sol 与 GPT-6 Luna 是 OpenAI 发布并全面开放的两款主流模型，官方称它们以不同的能力与成本组合将前沿智能带入日常工作。第三方报道显示，这两款模型于 2026 年 9 月 22 日发布，距离 GPT-6 Astra 发布仅 19 天。还有集成细节提到，Sol 模型页指出 Chat Completions 仅在 reasoning\_effort 设为 none 时支持函数调用。

**「影响」** 对使用 OpenAI API 及 Codex、ChatGPT Work 的开发者与团队而言，Luna 将高频抽取、摘要和代理类工作负载的每 token 成本压到此前的一半或更低，Sol 以 Sonnet 级定价承接日常编码与代理任务，而 ChatGPT Work/Codex 的每五小时消息额度较 GPT-5.6 有所扩大（Plus 档 Sol 为 15–150 条、Luna 为 350–3,000 条，5.6 对应为 10–100 与 250–2,000），因此多数常规工作流可直接迁移，仅最难的任务仍需保留 Astra。

**「社区讨论」** 评论者从不同角度评价此次发布：simonw 认为 GPT-6 Luna 半价是重大变化；m\_fayer 表示 GPT-5.6 Sol 在沟通方式和工程直觉上与其工作流特别契合，并担心继任模型虽技术上更好却可能不如它自然；jeffnash 则比较 Claude Code 20x 与 Codex Pro 20x，强调使用限制、重置窗口和套餐倍率计算是决定因素，并称 ChatGPT 用量在 20x 方案上基本不受计量；leokennis 从普通用户视角称 ChatGPT Plus 自 5.6 起“基本无限”且应用体验良好。总体共识是价格与用量限制已成为实际选择模型和代理工具的关键因素，分歧主要体现在模型更替对个人工作流习惯的冲击以及不同订阅方案的实际可用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://www.zdnet.com/innovation/openai-gpt-6-sol-luna-release/">OpenAI &#x27;s GPT - 6 Sol doubles its accuracy rate - for half the... - ZDNET</a></li>
<li><a href="https://www.digitalapplied.com/blog/gpt-6-sol-luna-launch-pricing-benchmarks-2026">GPT - 6 Sol and Luna : API Prices, Benchmarks and Trade-offs</a></li>
<li><a href="https://coursiv.io/blog/gpt-6-sol-luna">GPT-6 Sol and Luna: What&#x27;s New, Pricing, Benchmarks, and Who Should Use Them</a></li>
<li><a href="https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more">OpenAI releases GPT-6 Sol and Luna models, slashing API costs 50% or more | VentureBeat</a></li>
<li><a href="https://runtimewire.com/article/openai-gpt-6-sol-luna-launch">OpenAI launches GPT-6 Sol and Luna with sharply lower API prices</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6`, `#AI models`, `#LLM release`, `#Hacker News`

---

<a id="item-tech-news-2"></a>
### [WordPress 修复未授权路径遍历漏洞，可致条件性 RCE](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) ⭐️ 9.0/10

WordPress 核心中被披露存在一个未经身份验证的路径遍历漏洞，据报道可在特定条件下导致远程代码执行（RCE）；该漏洞已在 WordPress 7.1.2 中修复，并向后移植到更早版本分支。社区评论称修复回溯至 4.7，以照顾仍在使用旧分支的用户；一位评论者还提到约三分之一安装未使用较新的 7 分支。评论者指出补丁可从 7.1.1 之后的比较中识别，具体提交为 9c4e85...，并认为受影响函数之一是 locate\_template\(\)，其旧文档早已警告该函数不会阻止目录遍历攻击。因此，若应用把用户提供的模板名传入该函数，必须验证其来自活动主题目录、父主题目录或 /wp-includes/ 等三个适当位置。需要注意的是，RCE 的触发是有条件的，并非所有部署都会自动受此影响。

hackernews · vntok · 9月22日 16:33 · [社区讨论](https://news.ycombinator.com/item?id=49803959)

**「背景」** WordPress 是使用极广的开源内容管理系统，其模板解析机制会根据请求参数决定由主题中的哪个文件来渲染页面；本次漏洞正出在这一“页面模板解析”环节，未认证攻击者可借助路径穿越影响被包含的本地文件（LFI），在满足额外条件时进一步导致远程代码执行（RCE）。官方在 2026 年 9 月 22 日发布的 WordPress 7.1.2 中修复了该问题，并将修复回溯到所有仍可接收安全更新的分支，最早直至 4.7；不过官方强调只有最新版本受到主动支持。

**「影响」** 对使用官方 PHP Docker 镜像、或在 PHP 8.5 之前版本的默认 cPanel 配置下运行 WordPress 的站点而言，漏洞在未打补丁前可被未认证攻击者利用，因此必须升级到 WordPress 7.1.2 或对应旧分支的修复版本才能消除该风险。

**「社区讨论」** 社区反应以担忧和批评为主：有人指出这类漏洞正是可公开访问的 Web 服务器常被扫描的原因，并认为 WordPress 可能是 Web 历史上最易受攻击的软件之一；也有人分享已迁移到 Hugo 等静态站点生成器以彻底摆脱 WordPress 的压力。与此同时，评论者提醒大量安装未使用较新的 7 分支，并引用 locate\_template\(\) 的旧文档说明开发者应自行验证用户提供的模板路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp">Unauthenticated path traversal in page-template resolution leading to conditional RCE · Advisory · WordPress/wordpress-develop · GitHub</a></li>
<li><a href="https://wordpress.org/news/2026/09/wordpress-7-1-2-release/">WordPress 7.1.2 Release – WordPress News</a></li>
<li><a href="https://patchstack.com/articles/wordpress-7-1-2-security-release-unauthenticated-lfi-to-rce/">WordPress 7.1.2 Security Release: Unauthenticated LFI to RCE - Patchstack</a></li>
<li><a href="https://wordpress.org/documentation/wordpress-version/version-7-1-2/">Version 7 . 1 . 2 – Documentation – WordPress .org</a></li>
<li><a href="https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp">Unauthenticated path traversal in page-template resolution leading to...</a></li>

</ul>
</details>

**标签**: `#WordPress`, `#security vulnerability`, `#path traversal`, `#remote code execution`, `#open source`

---

<a id="item-tech-news-3"></a>
### [Anthropic 发布 Claude Opus 5.5：降价与输出改进](https://www.anthropic.com/claude-opus-5-5) ⭐️ 8.0/10

Anthropic 发布了 Claude Opus 5.5，Hacker News 相关讨论获得 1181 分和 803 条评论；但源页面正文未提供，因此无法核实完整技术规格与官方基准。评论者整理的价格表显示，Opus 5.5 相比 Opus 5 明显降价：每百万 token 输入从 5 美元降至 4 美元，输出从 25 美元降至 20 美元，缓存读取从 0.50 美元降至 0.20 美元，缓存写入从 6.25 美元降至 5 美元。有评论者用同一项 3D 动画提示测试后称，Claude 5.5（high）的输出较 Claude 5（high）有显著改进。另据评论引用的官方说明，Opus 5.5 在沟通上更自然、写作更清晰、更强调把重要信息前置，并被认为更适合长时间协作。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**「背景」** Claude Opus 5.5 是 Anthropic 于 2026 年 9 月 22 日发布的模型，也是其新的 Claude 5.5 系列中的首个模型，接替此前的 Claude Opus 5，并已在各平台上线（官方文档列出了模型 ID、上下文窗口、输出上限与可用性等信息）。Anthropic 此前曾公开呼吁为前沿模型的发展“设定节奏”（pacing the frontier），而本次发布仍以大量具体性能数据继续推进能力前沿，这一反差成为社区讨论的焦点。相比 Opus 5，其 API 定价下调约 20%，为每百万输入 token 4 美元、每百万输出 token 20 美元。

**「影响」** 对于以 Opus 5 为主要调用模型的开发者与团队，Opus 5.5 将 API 列表价降至每百万输入 token 4 美元、输出 token 20 美元、缓存读取 0.20 美元，使同等预算可支撑更多或更长时间的任务调用。据第三方评测机构 Artificial Analysis，它在 Terminal-Bench 4.0、AutomationBench-AA 等项目上已与 GPT-6 Astra 持平并登上其榜首，但实际成本仍取决于具体任务的 token 消耗结构。

**「社区讨论」** 讨论中既有对降价和输出质量提升的正面反馈，也有批评：Anthropic 刚呼吁“为前沿技术减速”，却很快发布 Opus 5.5，并在发布说明首行重提该呼吁，而后续具体数字显示其并未放缓。还有评论者表示不会转用，继续选择 DeepSeek v4.1（high）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://www.unite.ai/anthropic-releases-claude-opus-5-5-with-lower-pricing-and-new-safeguards/">Anthropic Releases Claude Opus 5.5 With Lower Pricing and New ...</a></li>
<li><a href="https://venturebeat.com/technology/anthropic-releases-claude-opus-5-5-beating-fable-5-1-on-key-agentic-benchmarks-at-60-cheaper-api-price">Anthropic releases Claude Opus 5.5, beating Fable 5.1 on key ...</a></li>
<li><a href="https://artificialanalysis.ai/articles/claude-opus-5-5">Claude Opus 5 . 5 takes the top spot on the Artificial... | Artificial Analysis</a></li>
<li><a href="https://claude.com/blog/what-a-task-costs-on-opus-5-5">What a task costs on Opus 5 . 5 | Claude by Anthropic</a></li>

</ul>
</details>

**标签**: `#Claude`, `#Anthropic`, `#LLM`, `#AI models`, `#pricing`

---

<a id="item-tech-news-4"></a>
### [五角大楼：过度依赖 AI 促成伊朗学校导弹袭击](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 8.0/10

彭博社报道称，五角大楼一份报告认定，对人工智能的过度依赖促成了美军对伊朗一所学校的导弹袭击，使军事 AI 的目标验证、自动化偏见与监督问责问题受到关注。讨论中引述的报告措辞称，美国“未能尽一切可行努力核实”该学校是军事目标，这种失败“超出单纯疏忽”，美方在明知存在重大平民目标风险的情况下仍下令打击、行为鲁莽。评论还提到，Minab 站点因过时数据被列为伊斯兰革命卫队（IRGC）设施，输入 Maven 系统后成为推荐的首日打击目标，原本耗时数小时的目标清单工作被压缩到几分钟。

hackernews · devonnull · 9月22日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49806430)

**「背景」** Maven（亦称 Project Maven）是美国国防部用于辅助分析影像和目标识别的 AI 系统，Palantir 是其相关工具的主要承包商之一。此次事件中，对 Palantir 所建 AI 工具的过度依赖、人员裁减以及被压缩的目标选定流程共同影响了打击决策；Minab 地点因数据过时被误标为伊朗伊斯兰革命卫队设施，并被系统列为推荐目标。

**「影响」** 在造成逾百名伊朗学童死亡的学校误击事件后，五角大楼的 AI 目标锁定推进计划受到更严格审视，Maven 系统依赖过时人工数据的问题成为问责焦点。前军方官员则强调责任在于人类而非 AI 本身，事故归因仍存分歧。

**「社区讨论」** 评论区对责任归属存在分歧：有观点认为核心问题不是 AI，而是指挥与核实失败，并批评把目标清单工作从数小时压缩到几分钟是“优化错误的指标”；也有人以 2026 年约 13,000 个目标中仅约 3 个误击、且比例优于历史空中战役为由，认为不能简单归咎于自动化，并追问最终谁会承担刑责。另有评论提到美国曾因 AI 错误标记而险些登上一艘被误认为运载核材料的中国船只，凸显对 AI 目标识别可靠性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gizmodo.com/pentagon-investigators-say-overreliance-on-palantir-ai-tech-contributed-to-u-s-strike-that-killed-123-iranian-children-2000814477">Pentagon Investigators Say Overreliance on Palantir AI Tech...</a></li>
<li><a href="https://www.rt.com/news/646000-overreliance-on-ai-contributed-to/">US overreliance on AI contributed to deadly Iran school strike ...</a></li>
<li><a href="https://www.yahoo.com/news/us/articles/pentagon-review-links-ai-targeting-172754307.html">Pentagon Review Links AI Targeting System to Strike That Killed 120 Iranian Children</a></li>
<li><a href="https://www.militarytimes.com/news/your-military/2026/03/24/deadly-iran-school-strike-casts-shadow-over-pentagons-ai-targeting-push/">Deadly Iran school strike casts shadow over Pentagon’s AI targeting push</a></li>
<li><a href="https://www.reddit.com/r/worldnews/comments/1wko4v6/pentagon_investigators_have_discovered_that/">r/worldnews on Reddit: Pentagon investigators have discovered that flawed intelligence and an overreliance on AI contributed to a missile strike that killed 123 Iranian school children</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#military AI`, `#autonomous weapons`, `#AI policy`, `#automation bias`

---

<a id="item-tech-news-5"></a>
### [Claude Opus 5.5 与 GPT-6 Sol/Luna 同日发布并掀起价格战](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 8.0/10

Anthropic 发布 Claude Opus 5.5，约一小时后 OpenAI 发布 GPT-6 Sol 与 GPT-6 Luna，Simon Willison 记录了这一轮明显的降价竞争。GPT-6 Luna 定价为输入 $0.10/百万 token、缓存输入 $0.01、输出 $0.50，恰是 GPT-5.6 Luna（$0.20/$0.02/$1.20）的一半；GPT-6 Sol 为 $2/$0.20/$10，也较 GPT-5.6 Sol 的 $4/$0.40/$20 减半，但 GPT-5.6 计划在 11 月涨价 25%，所以实际对比的是其促销价。Claude Opus 5.5 的输入/输出价格从 $5/$25 降至 $4/$20（降幅 20%），缓存读取价格下降 60%，这对缓存 token 占输入九成以上的长程 agent 会话尤其重要。Willison 还发现 Opus 5.5 在 “max” 思考档做经典的“骑自行车鹈鹕”SVG 测试时两次都因推理耗尽 128,000 输出 token 上限而未能返回结果，每次花费 $2.56、耗时近 20 分钟，他因此怀疑该档位实际上不可用。Anthropic 表示 Sonnet 5.5 和 Haiku 5.5 即将推出，而现有 Haiku 4.5 的 $1/$5 定价已是 GPT-6 Luna 的十倍。

rss · Simon Willison · 9月22日 23:46

**「背景」** Anthropic 与 OpenAI 长期按能力层级为旗舰模型定价，Opus 系列一直是 Claude 家族中能力最强、价格最高的产品线，Opus 4.5 至 Opus 5 各代都维持在每百万 token 输入 5 美元、输出 25 美元。Claude Opus 5.5 于 2026 年 9 月 22 日发布，距 7 月 24 日的 Opus 5 约两个月，是一次降价与能力提升同时发生的更新。OpenAI 的 GPT-6 Sol/Luna 在同一时期把 API 价格相对 GPT-5.6 同级模型削减约一半，OpenAI 称推理与缓存方面的改进使降价成为可能，而其发布时点仅比 Anthropic 的降价版 Opus 晚约 90 分钟，因此这轮调整被外界视为围绕前沿模型 API 定价的竞争。

**「影响」** 对在这批新模型上构建应用的开发者而言，推理成本被直接压低：GPT-6 Luna 的每百万 token 输入/输出价格为 $0.10/$0.50，是 GPT-5.6 Luna 的一半，而 Claude Opus 5.5 不仅输入输出下调 20% 至 $4/$20，缓存读取价格更下降 60%，对缓存命中率高的长时 agent 对话影响尤为明显。不过 Opus 5.5 在“max”思考档两次因耗尽 128,000 输出 token 上限而未能返回结果，单次尝试花费约 $2.56 并耗时近 20 分钟，该档位的成本与可靠性仍需实测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codersera.com/blog/claude-opus-5-5-complete-guide-2026/">Claude Opus 5.5: Specs, Pricing &amp; Benchmarks (2026)</a></li>
<li><a href="https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more">OpenAI releases GPT-6 Sol and Luna models, slashing API costs 50% or more | VentureBeat</a></li>
<li><a href="https://thenextweb.com/news/openai-gpt-6-sol-luna-api-price-cut">OpenAI cuts GPT-6 prices in half with Sol and Luna</a></li>

</ul>
</details>

**标签**: `#AI models`, `#Claude Opus`, `#GPT-6`, `#LLM pricing`, `#model releases`

---

<a id="item-tech-news-6"></a>
### [Complex KDA：扩展 Kimi Delta Attention 表达能力](https://www.reddit.com/r/MachineLearning/comments/1wn5uv9/understanding_and_enhancing_kimi_delta_attention_r/) ⭐️ 8.0/10

一篇 Reddit r/MachineLearning 帖子总结了一篇题为《Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention》的论文，分析并对比了 Gated Deltanet（GDN）与 Kimi Delta Attention（KDA）在表达能力上的差异。帖子指出，KDA 的完整对角门可以充当反射，从而在单步内完成二维旋转，但前提是把门的取值范围扩展到 \[-1,1\]、并把 delta 规则的学习率扩展到 \[0,2\]，这一形式被称为 Complex KDA（CKDA）。理论结果表明，CKDA 能够表达任意“正交对角加秩一”（orthogonal diagonal-plus-rank-one）矩阵，并可跟踪 S3、S4 和 A5 群，但无法跟踪 S5 群。实验方面，帖子称 CKDA 能学会 S3 与 S4，在音频续写任务上取得有希望的结果，并且在语言建模中训练稳定、可与标准 KDA 相竞争。上述内容来自 Reddit 上的 TLDR 摘要，相关结果被描述为有前景而非定论。

reddit · r/MachineLearning · /u/Yossarian\_1234 · 9月22日 10:34

**「背景知识」** 线性注意力以随序列长度线性增长的代价取代全注意力的二次复杂度，但长期以来在召回和“复制”能力上不及全注意力。Kimi Delta Attention（KDA）出自 2025 年 10 月发布的 Kimi Linear 架构，它在 Gated DeltaNet 基础上引入更细粒度的对角门控，使有限的有限状态 RNN 记忆得到更有效的利用。在此之上，Complex KDA 一文指出 KDA 可以把一次 delta-rule 变换与其通道门控提供的第二次反射组合起来实现二维旋转，并进一步把门控范围扩展到 \[-1,1\]、把 delta 规则的学习率扩展到 \[0,2\]。

**「影响」** 对于实现 KDA 类线性注意力层的开发者而言，Complex KDA 表明只需把通道门控范围扩展到 \[-1,1\]、并把 delta 规则系数 β 扩展到 \[0,2\]，就能让单步 delta 更新表达 2D 旋转，从而在不改动架构主体的情况下提升对 S3、S4 等群跟踪任务的可表达性，同时在语言建模上保持与标准 KDA 相当的竞争力。不过这些结论目前主要来自作者自述的实验，仍属&quot;有前景&quot;而尚未被独立复现验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.24797">[2609.24797] Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention</a></li>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention ... Kimi Linear: An Expressive, Efficient Attention Architecture Linear Attention: Kimi Delta Attention | Jianyu Huang kimi-delta-attention/docs/ARCHITECTURE.md at main · hwilner ... Linear Attention, From Scratch to Kimi 3 (Kimi Delta Attention) Kimi Delta Attention: Delta‐Rule Linear Mechanism</a></li>
<li><a href="https://arxiv.org/abs/2609.24797">[2609.24797] Complex KDA: Understanding and Enhancing the ...</a></li>
<li><a href="https://aiweekly.co/alerts/complex-kda-lifts-kimi-delta-attentions-expressivity-ceiling">Complex KDA lifts Kimi Delta Attention&#x27;s expressivity ceiling</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#attention mechanisms`, `#linear attention`, `#expressivity theory`, `#sequence modeling`

---

<a id="item-tech-news-7"></a>
### [FoxPro 复活：Rust/Wasm 新运行时兼容 VFP 9](https://foxscript.org/) ⭐️ 7.0/10

Visual FoxPro 在 2007 年停在版本 9，但仍有大量 32 位业务系统在运行；一个项目试图把它们延续下去。该项目用 Rust 编写、编译到 WebAssembly 的新运行时承载同样的 Visual FoxPro 语言，并对照真实的 vfp9.exe 做兼容性检查，同时让旧的 32 位 .fll 插件继续加载。它还取消了表 2 GB 的限制，并加入 lambdas、JSON 和 HTTP 服务器等扩展。项目采用 MIT 许可证，但目前报告尚未完成，构建也未签名。

hackernews · boredjohnny · 9月22日 21:00 · [社区讨论](https://news.ycombinator.com/item?id=49808023)

**「背景」** Visual FoxPro 是微软的数据库管理系统和开发语言，其 9.0 版于 2004 年 12 月发布，2007 年 10 月发布 SP2 后成为最终版本，微软随后终止了该产品线，并表示不会推出 .NET 版本。由于许多会计、库存、生产跟踪和内部报表等关键业务应用仍在运行 VFP，维护和迁移这些遗留系统成为长期问题。此次“复活”项目将同一语言放到用 Rust 编写并编译为 WebAssembly 的新运行时上，以延续对既有 FoxPro 代码和 vfp9.exe 兼容性的支持。

**「影响」** 对仍在维护 Visual FoxPro 业务系统的组织而言，该项目提供了不重写旧应用而迁移运行时的潜在路径。但构建未签名且报告未完成，现阶段只适合评估和小范围试验。

**「社区讨论」** 评论者一方面回忆 FoxPro/dBase 的易用性和商业价值，另一方面集中担忧其安全与并发缺陷：DBC 需对所有用户可读写，存储过程以明文 memo 保存且可执行 FoxPro 代码甚至 Win32 调用，容易被篡改触发器；也有开发者提到多用户经网络驱动器访问时出现文件锁和记录冲突，最终转向 .NET 客户端/服务器架构。这些经验表明，复活运行时并不能自动解决遗留系统的架构与权限问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Visual_FoxPro">Visual FoxPro - Wikipedia</a></li>
<li><a href="https://intersoftassociates.com/articles/legacy-systems/foxpro-and-end-of-life-migrations/">FoxPro Replacement and End of Life Migrations | Intersoft ...</a></li>
<li><a href="https://4devnet.com/legacy-foxpro-systems-on-modern-windows-what-companies-must-know/">Visual FoxPro on Windows 11: Risks, Compatibility &amp; Migration</a></li>
<li><a href="https://rustwasm.github.io/book/">Introduction - Rust and WebAssembly</a></li>

</ul>
</details>

**标签**: `#Visual FoxPro`, `#legacy software`, `#language runtime`, `#WebAssembly`, `#Rust`

---

<a id="item-tech-news-8"></a>
### [Claude Opus 5.5 Max 档基准与成本讨论](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 7.0/10

Hacker News 上围绕 Artificial Analysis 的 Claude Opus 5.5 「max」推理档基准页面展开讨论，评论者指出 xhigh 档与 medium（默认）档各自有独立页面。simonw 表示他两次尝试用 max 档完成「骑自行车的鹈鹕」SVG 生成都失败，因为模型在仍在推理时就耗尽了 128,000 token 的预算。hglaser 称在同为 high effort 的比较下，该模型每任务成本约为 Opus 5 的一半。breckenedge 质疑这类评测是否会在发布数周后重跑，他对自己内部数据集的一次重跑发现 Sol 的性能已回落到与 Luna 相当。另有评论认为前沿模型相对开放权重模型提升有限但价格高出约 100 倍，并有人对该模型是否应强于 Fable 表示疑问。

hackernews · theanonymousone · 9月22日 16:51 · [社区讨论](https://news.ycombinator.com/item?id=49804316)

**「背景」** Artificial Analysis 是第三方评测站点，会把同一模型的不同推理档位拆成独立页面，汇总质量、价格、吞吐与首 token 延迟等指标；Claude Opus 5.5 在该站就同时存在 max、xhigh 和默认的 medium 三个档位页面。Claude Opus 5.5 是 Anthropic 面向高难度推理、编程和长周期智能体任务的旗舰模型，其定价标注为每百万 token 4 美元，而“自适应推理”档位越高，模型在给出答案前消耗的推理 token 越多，因此单位任务成本与质量会一同变化。正因为这类评测可以用“每个任务成本”和推理 token 预算来横向比较（讨论中提到 max 档的 128,000 token 预算上限），这些数字是否稳定、能否复现才会成为关注点。

**「影响」** 对准备采用 max 推理档的开发者来说，实际后果是成本与可完成性的权衡：厂商基准称 Opus 5.5 每任务成本比 Opus 5 低约 40%、性能更高，但社区实测指出该档位可能在 128,000 token 推理预算内尚未产出结果就已耗尽预算，因此长链条任务需重新评估预算上限与重试策略。相关成本与性能数字目前仍属发布时点的厂商与聚合方数据，其数周后的可复现性尚待验证。

**「社区讨论」** 社区认可 Opus 5.5 max 档在每任务成本上的改善，但分歧集中在评测可靠性：多位评论者担心模型发布初期公布的基准成绩未必能长期保持，质疑基准是否会定期重跑。围绕性价比也存在张力，一方强调成本下降，另一方则认为相对开放权重模型的高价难以被「好 enough」的替代品支撑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/claude-opus-5-5">Claude Opus 5 . 5 ( max with fallback) - Intelligence... | Artificial Analysis</a></li>
<li><a href="https://kingy.ai/blog/claude-opus-5-5-specs-benchmarks-pricing-comparison/">Claude Opus 5 . 5 : Specs, Benchmarks , Pricing and How It... - Kingy AI</a></li>
<li><a href="https://kilo.ai/models/anthropic-claude-opus-5-5">Anthropic: Claude Opus 5 . 5 Coding Benchmark | Kilo Code</a></li>
<li><a href="https://mashable.com/tech/claude-opus-launch-promises-better-performance-cheaper-price">Anthropic launches Claude Opus 5.5: Benchmarks, pricing, safety | Mashable</a></li>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5.5 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#LLM benchmarks`, `#AI model pricing`, `#reasoning models`, `#Claude Opus`

---

<a id="item-tech-news-9"></a>
### [QontoFAQ：面向产品 FAQ 检索的嵌入模型基准](https://www.reddit.com/r/MachineLearning/comments/1wn9xqk/qontofaq_a_better_information_retrieval_benchmark/) ⭐️ 7.0/10

Reddit 用户 /u/espadrine 在 r/MachineLearning 发帖介绍了 QontoFAQ，一个用于评估嵌入模型在产品 FAQ 检索任务上表现的新信息检索基准，并配套提出了一种新指标。作者称现有检索基准有时会被模型“刷榜”，因此希望让评测更贴近“找到能回答产品问题的正确文章”这一实际目标。该工作包含一个与文档相关性更成比例的新指标、一个用于测量嵌入模型的基准数据集，以及一篇 Medium 文章和 GitHub 仓库 qonto/qonto-faq-benchmark。不过，帖子只提供概述和链接，未给出方法细节、实验结果或独立验证，因此其实际效果和意义尚无法充分评估。

reddit · r/MachineLearning · /u/espadrine · 9月22日 13:45

**「背景」** 信息检索基准用于衡量模型从文档库中找出与查询最相关文档的能力，而嵌入模型把查询与文档映射到同一向量空间、按相似度排序，是这类检索的常见技术基础。近年一些检索基准被认为已被模型“刷榜”（benchmaxxed），即排行榜分数的提升未必对应真实场景中的相关性。QontoFAQ 正是在这一背景下提出的：它面向产品 FAQ／产品问题场景，试图用更贴近文档相关性的新指标，并配合自建数据集来评估嵌入模型。

**「影响」** 对从事产品 FAQ 与问答式检索的 ML/IR 从业者来说，QontoFAQ 提供了一套据称与文档相关性更成比例的新指标，以及配套的评测数据集和开源代码，可用于评估嵌入模型。不过由于原帖未给出方法细节与实测结果，其相对现有检索基准的实际增益仍无法判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://trendshift.io/repositories/253658">qonto / qonto -faq- benchmark — GitHub trending stats... | Trendshift</a></li>

</ul>
</details>

**标签**: `#Information Retrieval`, `#Benchmarking`, `#Embedding Models`, `#Evaluation Metrics`, `#Datasets`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [《女神异闻录 4 Revival》TGS2026 专访：重制的取舍](https://www.gcores.com/articles/220050) ⭐️ 5.0/10

rss · 机核GCORES游戏资讯 · 9月22日 14:27

**「背景」** 《女神异闻录 4》以固定机位、立绘对话和稻羽市的地方氛围构成独特记忆，但这类较早期作品的画面与文本放到今天已显过时。作者在 TGS2026 试玩了序章 4 月 18 日至 20 日的自由探索版本，并采访总制作人和田和久与总监矢岛大亮，追问“Revival（复兴）”究竟意味着什么。

**「方案」** 重制的核心是把原本受固定机位限制的场景重建为可自由观察的全 3D 空间，代价是玩家原本看不到的区域也必须补齐：商店街要补全视线外空间又不能失去衰败感，河川敷因视野变远而需要重新梳理整个城市的地理关系，团队还实地取材了日本与稻羽市相似的地点。战斗上，作者称本作保留了“攻击弱点→击倒→总攻击”的核心节奏，并围绕异常状态新增机制——对异常状态敌人普通攻击可将其击飞，把异常状态传染给其他敌人，再借异常状态下更易暴击的特性衔接击倒与总攻击；矢岛表示这是为了不破坏核心循环，同时让使用频率偏低的普通攻击和状态异常成为新轴心，且不额外消耗资源。Persona 合体仍以二身合体与特殊合体为核心，但调整了合体预报效果并加入《女神异闻录 5 皇家版》的 Persona“特性”，还会新增数体 Persona。Prime Time 让玩家积攒量表后无消耗连续行动，和田称其目的是让玩家真正使用已学会的高消耗技能，矢岛则强调团队从一开始就把换手和 Prime Time 纳入战斗设计再重建平衡，因此熟练玩家会获得明显优势，但不会让 Boss 突然变简单。叙事上，和田明确不会改动剧本与主线，现代化只集中在台词文本润色，阳介并非唯一调整对象；过场按剧情重要程度筛选，原作动画尽量保留动画形式，战前演出偏好实时演算以延续模型连贯性，动画部分仍由 MAPPA 负责。视觉上团队坚持不改平成年代设定，把翻盖手机等元素当作“平成复古”保留，兼顾怀旧与新玩家的新鲜感。

**「启示」** 在作者看来，这次重制并非单纯用现代画面和玩法包装经典，而是在现代化与原作气质之间重新找平衡，让构成《女神异闻录 4》独特魅力的部分在今天仍有吸引力。

**标签**: `#Persona 4 Revival`, `#game remake design`, `#battle system design`, `#3D reconstruction`, `#developer interview`

---