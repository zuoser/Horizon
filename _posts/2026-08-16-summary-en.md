---
layout: default
title: "Horizon Summary: 2026-08-16 (EN)"
date: 2026-08-16
lang: en
---

> From 101 items, 5 important content pieces were selected

---

**Technology News**
1. [Anthropic publishes Claude system prompts](#item-tech-news-1) ⭐️ 8.0/10
2. [Qwen 3.8 27B shines but defaults to extreme overthinking](#item-tech-news-2) ⭐️ 7.0/10
3. [PJM&\#x27;s $12B Modeling Mistake Wastes Ratepayer Money](#item-tech-news-3) ⭐️ 7.0/10
4. [SSOG-Attention: Subquadratic Attention via Separable Gaussians](#item-tech-news-4) ⭐️ 7.0/10
5. [ECA Paper&\#x27;s Core Hypothesis Questioned by k=1 Ablation](#item-tech-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Anthropic publishes Claude system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic published the system prompts used by its Claude models, marking a rare public release of the actual instructions that shape model behavior and enabling researchers to track how those prompts evolve. The release notes document current and past prompts, including details such as Claude being instructed to verify whether an image is actually present before assuming one exists, and to prioritize user well-being over task completion during crisis conversations. Community members immediately began analyzing the changes, with Simon Willison creating a git commit history to make prompt diffs easier to inspect, such as the changes between Opus 4.8 and Opus 5. The publication gives AI researchers and engineers a concrete reference for auditing Claude behavior and comparing model versions, and it sets a transparency precedent for other AI labs.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**「Background」** Anthropic publishes the system prompts used by Claude models in its release notes, providing the current date and behavioral guidelines to guide each conversation. These prompts are updated with model releases, and community members such as Simon Willison have created git repositories to track changes over time. The published prompts offer a rare window into the instructions that shape Claude&\#x27;s responses.

**「Impact」** For AI researchers and engineers, the release provides a direct, versioned source for analyzing how Claude&\#x27;s instructions evolve and for auditing behavior changes across model versions like Opus 4.8 and Opus 5.

**「Community discussion」** Commenters focused on prompt details and transparency: Simon Willison created a git history to highlight changes between Opus versions and noted new references to Claude Fable 5 and Mythos 5, while others debated whether system-prompt instructions like having Claude check for missing images reveal limits of model intelligence, and one unrelated commenter raised concerns about AI-critical stories disappearing from the forum.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs</a></li>
<li><a href="https://tactiq.io/learn/claude-system-prompt">Claude System Prompt Explained: What&#x27;s Inside and Why It Matters</a></li>
<li><a href="https://simonwillison.net/2025/May/25/claude-4-system-prompt/">Highlights from the Claude 4 system prompt</a></li>

</ul>
</details>

**Tags**: `#Claude`, `#system prompts`, `#Anthropic`, `#AI transparency`, `#model behavior`

---

<a id="item-tech-news-2"></a>
### [Qwen 3.8 27B shines but defaults to extreme overthinking](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 7.0/10

Simon Willison reviewed Qwen 3.8 27B, an Apache-2.0-licensed 27B-parameter vision-capable LLM from Alibaba&\#x27;s Qwen lab, released Friday. Running locally on an M5 Max MacBook Pro and an NVIDIA DGX Spark via LM Studio and llama-server, he found that the model defaults to an xhigh reasoning\_effort, causing spectacular overthinking: a pelican SVG took 21 minutes with 22,276 reasoning tokens, while turning reasoning off produced a similar result in about two minutes. Even a simple &quot;draw an svg of a circle&quot; prompt triggered elaborate, animated output after several minutes. Qwen&\#x27;s self-reported benchmarks show improvements over Qwen 3.6 27B and the closed-weight Qwen 3.7-Plus, but Willison strongly recommends running this model on low or no reasoning levels at first, noting that independent benchmarks are still awaited.

rss · Simon Willison · Aug 16, 22:00

**「Background」** Qwen 3.8 27B is a 27B-parameter open-weight model released under the Apache 2.0 license, making it practical to run on a reasonably specced laptop. Its predecessor Qwen 3.6 27B was already impressive, and Qwen&\#x27;s self-reported benchmarks claim gains over both that model and the larger closed-weight Qwen 3.7-Plus. The model supports a reasoning\_effort parameter with xhigh as the default, intended for complex tasks but causing excessive token usage on simple requests.

**「Impact」** Users running Qwen 3.8 27B locally should set reasoning\_effort to low or disable reasoning to avoid multi-minute waits and context exhaustion; the default xhigh setting can consume the full 8,192-token context on trivial prompts. The 17GB Q4\_K\_M quantized build works well on Mac and DGX Spark hardware, but the model&\#x27;s impressive outputs are not worth the default thinking overhead.

**Tags**: `#Qwen`, `#LLM`, `#open source`, `#benchmarks`, `#AI`

---

<a id="item-tech-news-3"></a>
### [PJM&\#x27;s $12B Modeling Mistake Wastes Ratepayer Money](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 7.0/10

An analysis by Robert Boswall argues that PJM Interconnection&\#x27;s flawed modeling caused a $12 billion waste of US ratepayer money and still poses risks to grid planning. The piece examines how bad model design in PJM&\#x27;s capacity market exposed vulnerabilities in computational approaches to infrastructure. It warns that PJM may be repeating the same mistake, putting ratepayers at further risk. The analysis frames this as a technical systems problem rather than a software breakthrough.

rss · SemiAnalysis · Aug 16, 22:27

**「Background」** PJM Interconnection operates the largest wholesale electricity market in the U.S., using a capacity market to ensure enough generation is available to meet future demand. In that market, modeling mistakes can lead it to procure significantly more capacity than its reserve target requires, and ratepayers ultimately pay the higher capacity prices that result from that surplus.

**「Impact」** For US electricity ratepayers under PJM, the modeling error has already led to $12 billion in waste and creates ongoing risk of further losses if PJM repeats the flawed approach.

<details><summary>References</summary>
<ul>
<li><a href="https://cpowerenergy.com/why-doesnt-texas-have-a-capacity-market/">Why doesn&#x27;t Texas have a Capacity Market ? - CPower Energy</a></li>

</ul>
</details>

**Tags**: `#modeling`, `#energy`, `#infrastructure`, `#systems analysis`, `#PJM`

---

<a id="item-tech-news-4"></a>
### [SSOG-Attention: Subquadratic Attention via Separable Gaussians](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 7.0/10

The author introduced SSOG-Attention, a sub-quadratic alternative to scaled dot-product attention \(SDPA\) that learns a few separable Gaussian atoms per head and steers them geometrically based on the query token, reducing complexity from O\(N²·d\) to O\(N·√N·d\). Experiments on CIFAR-100 show SSOG clearly beats SDPA, while on ImageNet-1k it delivers equivalent performance with much faster convergence, along with better speed and memory efficiency at increasing scale. The approach is released as a blog post and GitHub repository, with the author noting that AI was used for some code and writing but that they stand behind the results.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 10:06

**「Background」** Scaled dot-product attention \(SDPA\) computes pairwise similarity scores between all query and key tokens, leading to quadratic O\(N²·d\) complexity in sequence length. SSOG \(Sum Of Separable Gaussians\) approximates this by modeling attention with a sum of factorized Gaussian atoms, which can be evaluated more efficiently because separable Gaussians decompose into lower-dimensional operations.

**「Impact」** If the reported results hold up under independent verification, SSOG-Attention offers a practical way to train transformers on longer sequences with comparable accuracy to SDPA while cutting computation and memory costs.

**Tags**: `#attention mechanisms`, `#efficient transformers`, `#sub-quadratic complexity`, `#machine learning`, `#separable Gaussians`

---

<a id="item-tech-news-5"></a>
### [ECA Paper&\#x27;s Core Hypothesis Questioned by k=1 Ablation](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

A Reddit critique argues that the 2019 Efficient Channel Attention \(ECA\) paper, with roughly 12,000 citations, is conceptually flawed because it applies a 1D convolution over channel means, treating the channel dimension as if it had a spatial or temporal topology when channels are more like unordered tabular features. The author tests ECA and related gates on chess endgame tablebases, a complete and unbiased dataset, and finds that ECA with kernel size k=3 reaches 96.68% test accuracy versus 96.17% for Squeeze-and-Excitation \(SE\), but ECA with k=1, which has no cross-channel interaction, still achieves 96.61% and beats SE. A masked \[1,0,1\] ECA variant performs comparably at 96.63%, while a per-channel scalar gate reaches 96.65%, and identity gating lags at 96.04%. The author notes that neither the official ECA repository nor common reimplementations like timm report a pure k=1 ablation, which would have contradicted the paper&\#x27;s central claim that cross-channel interaction is key. They suggest that synthetic complete datasets, like chess tablebases, can help separate implicit regularization effects from core architectural efficiency, and call for testing degenerate kernel sizes to disprove hypotheses. In the experiments, ECA k=1 outperforms SE and nearly matches ECA k=3, undermining the paper&\#x27;s explanation despite its empirical success.

reddit · r/MachineLearning · /u/arkuto · Aug 16, 10:13

**「Background」** Squeeze-and-Excitation \(SE\) networks improve CNNs by computing per-channel weights from global average-pooled features, typically using a dimensionality-reducing bottleneck. Efficient Channel Attention \(ECA\) was proposed as a successor that avoids dimensionality reduction by applying a 1D convolution directly to the channel means, claiming that local cross-channel interactions are essential. The critic&\#x27;s central point is that convolutions rely on an underlying topology such as space or time, so sliding a kernel over unordered channel indices is conceptually unjustified, even if it works in practice because neural networks can adapt.

**「Impact」** For researchers and practitioners using or extending ECA, the k=1 result suggests the mechanism behind ECA&\#x27;s improvement may be misattributed, and that simpler per-channel scaling or even a mask with no middle-channel interaction can match the full ECA, so future attention designs should include degenerate ablations and be validated on complete datasets to avoid overfitting artifacts.

**Tags**: `#Efficient Channel Attention`, `#Deep Learning`, `#Computer Vision`, `#Attention Mechanisms`, `#Model Architecture`

---