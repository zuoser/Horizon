---
layout: default
title: "Horizon Summary: 2026-08-15 (ZH)"
date: 2026-08-15
lang: zh
---

> 从 101 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Codex 自动研究实现 232 倍内核加速](#item-tech-news-1) ⭐️ 8.0/10
2. [AI 并非更会思考，而是靠更大工作记忆和持久力](#item-tech-news-2) ⭐️ 7.0/10
3. [BDH-CQ：用循环潜在推理进行上下文学习](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Codex 自动研究实现 232 倍内核加速](https://sankalp.bearblog.dev/autoresearch/) ⭐️ 8.0/10

开发者分享了一个使用 Codex 进行自动研究的工作流——通过基准测试、剖析、验证、研究、改进的循环来优化内核，并声称实现了 232 倍性能提升。这一流程依赖语言模型在 GPU 内核和 SIMD 优化子领域丰富的训练数据，能够自动产出大幅调优的代码。不过，社区讨论指出，这类 AI 生成优化容易过拟合于特定基准输入，单纯追求基准分数可能牺牲泛化能力。整体来看，结果令人印象深刻，但鲁棒性和专家监督仍是落地时需要重点关注的问题。

hackernews · tosh · 8月15日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49309549)

**「背景」** 这项优化来自 GPU 编程竞赛中的 qr\_v2 问题，要求实现批量的紧凑 Householder QR 分解内核。作者让 Codex 以“基准测试—性能剖析—验证—研究—改进”的自动研究循环反复迭代，最终在 183 名参赛者中排名第 12，并把基线内核从约 419 毫秒降到约 1.8 毫秒，实现 232 倍加速。社区讨论强调，这类方法依赖验证器确保正确性，而且容易在竞争样例上过拟合，专家监督仍然关键。

**「影响」** 对于尝试以 AI 自动调优优化内核或 GPU 程序的开发者，最直接的启示是必须把验证器、专家审查和输入多样性测试纳入流程；来自相关竞赛的社区证据显示，多数 AI 优化方案会在非竞赛形状输入上完全失效。

**「社区讨论」** 评论者一方面对非 AI 生成的长文和新鲜工作流表示认可，另一方面普遍担忧过拟合：Almondsetat 在视频压缩编解码器上给 agent 接入编译器剖析器和流验证器来约束改动；augment\_me 指出某竞赛 10 个顶尖方案中 8 个在 OOD 输入上失效，只有熟悉 GPU 编程的专家在合理范围内调整的方案未受影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sankalp.bearblog.dev/autoresearch/">Auto-research with codex: How I achieved a 232x Faster Kernel over baseline with Codex in GPU Mode&#x27;s qr_v2 problem – sankalp&#x27;s blog</a></li>
<li><a href="https://news.ycombinator.com/item?id=49309549">Auto-research with codex: How I achieved a 232x Faster Kernel | Hacker News</a></li>
<li><a href="https://ecosistemastartup.com/auto-research-con-codex-logra-optimizacion-232x-en-kernels-gpu-para-founders/">Auto-research con Codex logra optimización 232x en kernels GPU para founders – El Ecosistema Startup</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#kernel optimization`, `#GPU programming`, `#code generation`, `#performance engineering`

---

<a id="item-tech-news-2"></a>
### [AI 并非更会思考，而是靠更大工作记忆和持久力](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians) ⭐️ 7.0/10

一篇由戴维德·皮费尔（Davide Piffer）撰写的文章及 Hacker News 讨论认为，AI 在数学上的出色表现并非源于真正的“超越人类思考”，而是因为其拥有远大于人类的工作记忆，并能不知疲倦地搜索和尝试。评论者进一步指出，人类数学家往往只发表正面结果，而 AI 可以利用和复用负面轨迹；所谓的高智力表现，也可能只是“比周围人记得更多”以及更有精力。该观点挑战了近来关于 AI 已能“超越数学家思考”的说法，强调其优势来自记忆容量与持续性而非推理突破。

hackernews · rzk · 8月15日 18:13 · [社区讨论](https://news.ycombinator.com/item?id=49312845)

**「背景」** 这篇文章和相关的讨论源于一篇题为“AI 并非在数学上超越人类思维，而是在记忆上超越人类”的随笔。其核心背景是：近年来，人工智能，尤其是大语言模型（LLM），在数学和推理任务上表现日益强劲，引发了数学家群体的关注和警告；例如，有报道提到数学家正在探讨 AI 可能取代他们的可能性，也有人持乐观态度，认为 AI 将帮助而非取代数学家。该随笔提出的关键观点是，AI 所谓的数学能力并非来自真正超越人类的推理，而是来自其远大于人脑的工作记忆和不疲倦的搜索能力；社区讨论中进一步补充了“过目不忘”、“输出负结果”以及“暴力搜索”等角度。

**「影响」** 这一论点提醒研究者和公众，在评估 AI 数学能力时，应将更大的工作记忆、不知疲倦的搜索和可复用的负面结果视为关键变量，而非单纯归因于推理能力的突破。

**「社区讨论」** 评论区普遍认同这一框架：有开发者以自己的软件生涯为例，指出所谓“高绩效”常来自回忆既有知识或比旁人更有精力；另有人提到人类数学家很少发表负面结果，而 AI 可发布并复用这类轨迹，并引用了 TheoremDB 等项目；还有评论强调 AI“不知疲倦”，能持续暴力搜索而不像人类一样气馁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians">AI Isn’t Outthinking Mathematicians. It’s Out-Remembering Them.</a></li>
<li><a href="https://news.ycombinator.com/item?id=48382052">Mathematicians issue warning as AI rapidly gains ground | Hacker News</a></li>
<li><a href="https://www.understandingai.org/p/mathematicians-are-grappling-with">Mathematicians are grappling with the possibility that AI might eclipse them</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#working memory`, `#mathematics`, `#LLMs`, `#cognitive science`

---

<a id="item-tech-news-3"></a>
### [BDH-CQ：用循环潜在推理进行上下文学习](https://www.reddit.com/r/MachineLearning/comments/1vov5r5/bdhcq_incontext_learning_with_recurrent_latent/) ⭐️ 7.0/10

BDH-CQ 是一个 150M 参数规模的推理系统，它将上下文学习的演示写入循环记忆，并在高维潜在工作空间中通过迭代计算求解查询，且不把中间推理状态解码为语言。该系统在 ARC-AGI-1 上达到 29.5% pass@2，单任务计算成本约为 0.00070 美元，称其突破了此前报告的成本–精度帕累托前沿。训练中不使用任务标识符或评估任务演示对，推理时也不更新参数。该结果来自 Reddit 帖子，尚未经过同行评审，因此头条数据仍需独立验证。

reddit · r/MachineLearning · /u/moschles · 8月15日 06:18

**「背景」** ARC-AGI-1 是一个旨在测试模型抽象推理与泛化能力的基准，常被用来衡量模型能否解决未见过的任务。传统的大语言模型主要依靠提示词中的示例进行上下文学习，并将中间推理步骤显式地写成自然语言。BDH-CQ（arXiv:2608.09888）提出了一种不同的思路：将示例输入到循环记忆中，让模型在高维潜在空间中迭代计算来求解查询，而不把中间推理状态解码为语言。该模型参数规模仅为 1.5 亿，在 ARC-AGI-1 上报告了 29.5% 的 pass@2 成绩，并且计算成本据称约为每个任务 0.00070 美元。

**「影响」** 对从事上下文学习与推理成本优化的研究者而言，该结果提供了一个 150M 参数模型在 ARC-AGI-1 上达到 29.5% pass@2 且单任务成本约 0.00070 美元的基准点。但由于该结果来自未经同行评审的 Reddit 帖子，仍需独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2608.09888">Paper page - BDH-CQ: In-Context Learning with Recurrent Latent Reasoning</a></li>
<li><a href="https://arxiv.org/abs/2608.09888">[2608.09888] BDH-CQ: In-Context Learning with Recurrent Latent Reasoning</a></li>

</ul>
</details>

**标签**: `#in-context learning`, `#recurrent neural networks`, `#latent reasoning`, `#ARC-AGI`, `#cost efficiency`

---