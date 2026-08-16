---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> 从 101 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [Anthropic 公开 Claude 系统提示词](#item-tech-news-1) ⭐️ 8.0/10
2. [Qwen 3.8 27B 评测：性能出色但默认过度思考](#item-tech-news-2) ⭐️ 7.0/10
3. [PJM 建模错误浪费 120 亿美元，并可能重蹈覆辙](#item-tech-news-3) ⭐️ 7.0/10
4. [SSOG-Attention：可分离高斯和作为亚二次方注意力替代方案](#item-tech-news-4) ⭐️ 7.0/10
5. [重新审视 ECA 论文：跨通道交互假设可能并不成立](#item-tech-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Anthropic 公开 Claude 系统提示词](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 在官方发布说明中公开了其 Claude 模型实际使用的系统提示词，使外界能够详细查看并追踪不同版本间的提示词演变。这一透明度举措为 AI 研究者和工程师提供了直接分析模型行为塑造指令的素材，例如模型会自行检查图像是否真的上传，而不是仅凭提示词中的描述判断。公开内容还包含 Anthropic 关于在用户处于危机时优先处理其福祉等行为目标的明确表述。系统提示词的发布成为理解 Claude 行为变化的重要参考。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**「背景」** Anthropic 在其官方文档中发布了 Claude 模型（包括网站和移动应用）使用的系统提示词，这些提示词位于每次对话的开头，用于提供当前日期等最新信息并引导模型行为。系统提示词是塑造 Claude 行为的分层系统的一部分，Anthropic 会随每次模型发布更新这些提示词的发布说明，使外界能够追踪其演变。

**「影响」** 对 AI 研究者和工程师而言，公开的系统提示词提供了可审计的技术材料，可直接用于分析 Claude 行为变化并评估模型迭代的影响。

**「社区讨论」** Simon Willison 在 GitHub 上把提示词重建为 git 提交历史，并指出 Opus 4.8 与 Opus 5 的差异中最有意思的新增内容是涉及 Claude Fable 5 和 Claude Mythos 5 的说明。另有评论质疑通过系统提示词强制模型检查图像是否上传与 Anthropic 对‘智能’的宣称之间存在矛盾，也有人提醒系统提示词只是塑造 Claude 行为的分层体系的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#Claude`, `#system prompts`, `#Anthropic`, `#AI transparency`, `#model behavior`

---

<a id="item-tech-news-2"></a>
### [Qwen 3.8 27B 评测：性能出色但默认过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 7.0/10

西蒙·威利森评测了阿里 Qwen 实验室发布的 Apache-2.0 协议、27B 参数视觉语言模型 Qwen 3.8 27B。该模型自称在基准测试中同时超越了 Qwen 3.6 27B 和闭源的 Qwen 3.7-Plus，但他强调其默认的 xhigh 推理档位会导致严重过度思考。在 128GB M5 Max MacBook Pro 和 NVIDIA DGX Spark 上，模型默认 xhigh 时生成一张鹈鹕骑自行车的 SVG 用了 21 分钟，消耗 22,276 个推理 token 和 3,223 个输出 token；关闭推理后同样任务只需 137 秒、3,715 个 token。他强烈建议用户一开始使用 low 或关闭推理档位，并指出该模型在图像边界框任务上表现很好。

rss · Simon Willison · 8月16日 22:00

**「背景」** Qwen 3.8 27B 是继 Qwen 3.6 27B 之后的新一代本地可运行视觉语言模型，27B 参数规模适合在配置较好的笔记本电脑上使用。模型默认启用 xhigh reasoning\_effort，文档称其面向复杂任务，但这在消费级硬件上会导致极慢的生成速度和过长推理链条。

**「影响」** 对希望在本地运行 Qwen 3.8 27B 的用户，默认 xhigh 设置会造成不切实际的等待时间，因此应手动选择 low 或关闭推理档位以获取可用的速度；该模型在视觉边界框等任务上仍表现良好。

**标签**: `#Qwen`, `#LLM`, `#open source`, `#benchmarks`, `#AI`

---

<a id="item-tech-news-3"></a>
### [PJM 建模错误浪费 120 亿美元，并可能重蹈覆辙](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 7.0/10

据分析，美国电网运营机构 PJM 在容量市场建模中的错误，导致美国费率人浪费了约 120 亿美元；这些错误并非来自 AI 模型，而是电网规划和市场设计中使用的仿真模型存在缺陷。这一事件暴露了系统分析和基础设施规划中的结构性风险，可能影响电网可靠性和市场设计的公信力。更重要的是，PJM 目前的做法显示它可能再次复制同样的建模错误，从而让费率人继续面临额外的财务和可靠性风险。分析还指出了模型设计、验证和监管审查环节的不足，使这类高成本失误得以重演。

rss · SemiAnalysis · 8月16日 22:27

**「背景」** PJM 是美国最大的电网运营商之一，负责为美国东部多个州协调电力批发市场。其容量市场旨在确保未来几年有足够的发电资源，价格通常由拍卖决定，但需要通过建模仿真预测未来电力需求和发电资源可用性。近年来，PJM 在容量拍卖中使用建模方法，过度采购了约 21%高于目标的备用容量，导致成本上升，由消费者（即费率支付者）承担，这构成了建模错误造成巨额浪费的背景。

**「影响」** 该失误直接影响 PJM 覆盖区域的费率人，他们已承担约 120 亿美元的浪费，而 PJM 若重蹈覆辙，将进一步推高成本并增加电网运行风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.monitoringanalytics.com/reports/PJM_State_of_the_Market/2024/2024-som-pjm-sec12.pdf">2024 State of the Market Report for PJM</a></li>
<li><a href="https://cpowerenergy.com/why-doesnt-texas-have-a-capacity-market/">Why doesn&#x27;t Texas have a Capacity Market ? - CPower Energy</a></li>

</ul>
</details>

**标签**: `#modeling`, `#energy`, `#infrastructure`, `#systems analysis`, `#PJM`

---

<a id="item-tech-news-4"></a>
### [SSOG-Attention：可分离高斯和作为亚二次方注意力替代方案](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 7.0/10

SSOG-Attention 提出一种基于可分离高斯和（Sum of Separable Gaussians）的注意力机制，作为标准缩放点积注意力（SDPA）的亚二次复杂度替代方案。作者称该方法将复杂度从 O\(N²·d\) 降至 O\(N·√N·d\)，并通过在 CIFAR-100 和 ImageNet（IN1k）上的实验显示，在小型数据集上明显优于 SDPA，在更大数据集上性能相当且收敛更快。帖子还表示，随着规模增大，该方法在速度和内存效率上更具优势。相关博客文章和代码仓库已公开。

reddit · r/MachineLearning · /u/4rtemi5 · 8月16日 10:06

**「背景」** 标准缩放点积注意力（SDPA）需要计算所有查询与键的相似度，因此计算和内存复杂度为 O\(N²·d\)，其中 N 为序列长度，d 为特征维度。这使得长序列 Transformer 的训练和推理成本随序列长度平方增长。SSOG 通过为每个注意力头学习少量高斯原子，并基于查询令牌对它们进行几何调整，利用可分离结构实现更低复杂度。

**「影响」** 对于从事高效 Transformer 架构的研究人员和工程师，SSOG-Attention 提供了一种在长序列场景下可能降低计算与内存开销的新选择，但其性能优势目前仅为作者自报，尚未经过独立验证。

**标签**: `#attention mechanisms`, `#efficient transformers`, `#sub-quadratic complexity`, `#machine learning`, `#separable Gaussians`

---

<a id="item-tech-news-5"></a>
### [重新审视 ECA 论文：跨通道交互假设可能并不成立](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

对 2019 年 Efficient Channel Attention（ECA）论文的批判性分析认为，其用 1D 卷积直接处理通道均值、避免 SE 式降维的设计虽然在 ImageNet 等任务上效果更好，但在概念上难以成立，因为通道维度不像空间或时间那样具有可滑动卷积所需的拓扑与平移不变性。作者用六子国际象棋残局库做了门控机制对照实验，结果与 ECA 原始报告一致：k=3 的 ECA（测试损失 0.0822，准确率 96.68%）明显优于 SE（0.0954，96.17%）和 Identity（0.0981，96.04%）。但关键的 k=1 消融（无跨通道交互，仅每通道缩放）也取得 0.0826 的测试损失和 96.61%的准确率，几乎追平 k=3 并胜过 SE，削弱了“跨通道交互是关键”这一核心假设。CenterMasked ECA（\[1,0,1\]掩码）得分约 0.0821/96.63%，说明跨通道信号在某些条件下仍可能有帮助。作者还指出，官方仓库与复现项目没有对纯 k=1 做独立基准，因此建议新架构应同时在包含完整标签分布的综合数据集上检验，以区分核心机制作用与隐式正则化效果。

reddit · r/MachineLearning · /u/arkuto · 8月16日 10:13

**「背景」** SE（Squeeze-and-Excitation）先对每个通道做全局平均池化，再用小型 MLP 降维并生成通道权重；ECA 则用核大小为 k 的 1D 卷积在通道均值序列上直接生成权重，论文声称局部跨通道交互是关键，且避免降维带来收益。但是卷积假设数据存在局部相关的有序结构；通道列表（如 cost、weight、material）更像无序的表格数据，对其做 1D 卷积缺乏先验合理性，这正是作者批评“被诅咒的卷积”的背景。

**「影响」** 对采用 ECA 的模型设计者而言，这一结果显示 ECA 相对 SE 的收益可能并非源于跨通道交互机制本身，而可能来自每通道缩放或隐式正则化；因此在将 ECA 机制归因于跨通道交互前，应补充 k=1 等消融验证。若进一步得到验证，该结果也会支持作者关于网络架构可能过度工程化的担忧，但当前证据仅来自单一棋盘数据集的非正式实验。

**标签**: `#Efficient Channel Attention`, `#Deep Learning`, `#Computer Vision`, `#Attention Mechanisms`, `#Model Architecture`

---