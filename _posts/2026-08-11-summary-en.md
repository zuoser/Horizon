---
layout: default
title: "Horizon Summary: 2026-08-11 (EN)"
date: 2026-08-11
lang: en
---

> From 124 items, 11 important content pieces were selected

---

**Technology News**
1. [Zuckerberg criticizes closed AI rivals as Meta embraces open models](#item-tech-news-1) ⭐️ 8.0/10
2. [Rust SIMD on the GPU](#item-tech-news-2) ⭐️ 8.0/10
3. [Muse Glimmer: Meta&\#x27;s 30B Open Model for Local Agent Workflows](#item-tech-news-3) ⭐️ 8.0/10
4. [Exploiting SMM with an Extremely Long Interrupt Instruction](#item-tech-news-4) ⭐️ 8.0/10
5. [Hand-Compiled Transformer Weights Achieve Perfect Multiplication](#item-tech-news-5) ⭐️ 8.0/10
6. [antirez releases h3.c native MiniMax-H3 inference for Apple Silicon](#item-tech-news-6) ⭐️ 7.0/10
7. [Style-Prompting LLMs Is Lossy and Risks Hallucinations](#item-tech-news-7) ⭐️ 7.0/10
8. [Nvidia and Wall Street giants raise $500bn for AI infrastructure](#item-tech-news-8) ⭐️ 7.0/10
9. [Fru: Fast Rust Random Forest with Python/R Bindings](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [Nvidia and six asset managers target $500 billion for AI infrastructure financing](#item-finance-news-1) ⭐️ 9.0/10
2. [Premarket Movers: Intel $15B Stock Offering, GameStop&\#x27;s Possible eBay Bid Withdrawal, Verisk Acquisition Ruling](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Zuckerberg criticizes closed AI rivals as Meta embraces open models](https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878) ⭐️ 8.0/10

Mark Zuckerberg has publicly attacked &\#x27;closed&\#x27; AI rivals and reaffirmed Meta&\#x27;s commitment to open models, according to a Financial Times article and a companion post on Meta&\#x27;s website. The piece reports that Meta is returning to open models as a strategic priority, with Zuckerberg arguing that open-source AI is crucial for competition and safety. The move centers on Meta&\#x27;s Llama family of open-weight models, a key asset in the open-source AI landscape. The story has sparked broad community discussion on Hacker News, with 463 points and 430 comments at the time of reporting.

hackernews · root-parent · Aug 10, 14:06 · [Discussion](https://news.ycombinator.com/item?id=49243880)

**「Background」** Meta&\#x27;s open-source Llama models, beginning with Llama in 2023, are widely credited with helping start the open-source AI race, though Meta later experimented with closed, proprietary AI offerings. In a new statement, Mark Zuckerberg attacked OpenAI and Anthropic for their closed approaches and argued that powerful AI should be freely available, marking Meta&\#x27;s return to open models after that proprietary detour.

**「Community Discussion」** Several commenters welcome the open-model stance as a net good, crediting Meta for kicking off the open-source AI race with Llama. Others are skeptical, suggesting the move is a competitive reversal or a reaction to a closed launch that lacked buyers.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/zuckerberg-criticizes-closed-ai-meta-open-models/">Mark Zuckerberg criticizes closed AI rivals as Meta returns to open models</a></li>
<li><a href="https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878?syn-25a6b1a6=1">Mark Zuckerberg attacks ‘closed’ AI rivals as Meta returns to open models</a></li>

</ul>
</details>

**Tags**: `#open source`, `#artificial intelligence`, `#Meta`, `#AI industry`, `#Llama`

---

<a id="item-tech-news-2"></a>
### [Rust SIMD on the GPU](https://www.vectorware.com/blog/simd-on-gpu/) ⭐️ 8.0/10

Rust&\#x27;s portable SIMD language features are being explored for GPU programming, an approach that seeks to bring performant, portable data-parallel computing to Rust systems programmers. The article, published on Vectorware, highlights how CPU-style SIMD abstractions can be applied to GPU compute workloads as an alternative to vendor-specific GPU frameworks. Community discussion notes that the standard library&\#x27;s portable SIMD module remains available only on nightly Rust, which limits stable-compatible adoption; one project, an FFT crate, switched to the fearless\_simd crate to achieve portable SIMD on stable. The approach is described as timely and useful for the systems/GPU space, though not groundbreaking, and it still faces questions about performance portability and library maturity.

hackernews · sagacity · Aug 10, 18:12 · [Discussion](https://news.ycombinator.com/item?id=49247477)

**「Background」** SIMD \(Single Instruction, Multiple Data\) is a technique that lets a processor perform the same operation on multiple data points in a single instruction, traditionally used on CPUs to speed up tasks like image processing and numerical computing. Rust&\#x27;s portable SIMD library \(core::simd\) provides a hardware-independent abstraction for writing SIMD code, but it is generally only available on nightly Rust builds. VectorWare&\#x27;s reported milestone is that the same Rust portable SIMD code can now be compiled to run on both CPUs and GPUs without rewriting or using intrinsics, with GPU warps executing the SIMD operations unchanged.

**「Impact」** Developers applying Rust&\#x27;s portable SIMD abstractions to GPU code must currently use nightly Rust for std::simd, a constraint that has already led some projects to adopt the fearless\_simd crate for stable compatibility.

**「Community Discussion」** Commenters pointed out that std::simd is nightly-only, with fearless\_simd serving as a stable workaround; they also questioned whether fixed-width portable SIMD is truly performance-portable and expressed interest in an open-source Rust SIMD library with the maturity of Google Highway, plus asked for examples of complex GPU algorithms achieving competitive performance in Rust.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vectorware.com/blog/simd-on-gpu/">Rust SIMD on the GPU - VectorWare</a></li>
<li><a href="https://elsolitario.org/en/2026/08/10/vectorware-portable-simd-gpu-rust/">SIMD on GPU: Rust&#x27;s core::simd Runs on Warps Unchanged</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#SIMD`, `#GPU computing`, `#portable SIMD`, `#systems programming`

---

<a id="item-tech-news-3"></a>
### [Muse Glimmer: Meta&\#x27;s 30B Open Model for Local Agent Workflows](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) ⭐️ 8.0/10

Meta introduced Muse Glimmer, a 30B-parameter open-weight model optimized for always-on local agent workflows. The release addresses the growing need for efficient on-device AI and is notable for being designed specifically for agentic, always-on use rather than serving as a general-purpose chat model. It has generated significant community discussion about its competitiveness, likely timing with other releases in the dense 30B class, and Meta&\#x27;s strategic positioning in open-weights AI. The model is available as open weights, and users have begun running it locally with tools like Ollama.

hackernews · riordan · Aug 10, 10:10 · [Discussion](https://news.ycombinator.com/item?id=49241679)

**「Background」** Meta Superintelligence Labs has released Muse Glimmer, a 30-billion-parameter dense multimodal model designed for always-on local agent workflows, with open weights under the Apache 2.0 license. It features a 120K+ token context window and is optimized to run on a range of local hardware, including NVIDIA platforms, for long-running agentic AI work.

**「Impact」** Developers and self-hosting enthusiasts can now experiment with a 30B open model tailored for local agent workflows, with early user reports showing it runs on a 32GB Mac Mini via Ollama, though slowly.

**「Community Discussion」** Commenters are watching comparisons with upcoming dense 30B models like Qwen3.8 27B, and several see Meta&\#x27;s plan to also release Muse Spark 1.2 weights as a strategically important move that could strengthen its position among US open-weights models. An early user reports that Muse Glimmer works locally on a 32GB Mac Mini via Ollama but is slow, while others spotlight readily available quantized versions.

<details><summary>References</summary>
<ul>
<li><a href="https://korshunov.ai/en/article/17490-meta-releases-open-weight-muse-glimmer-30b-agentic-vision-model/">Meta releases open-weight Muse Glimmer 30 B agentic vision model</a></li>
<li><a href="https://developer.nvidia.com/blog/run-local-agentic-ai-workflows-with-metas-muse-glimmer-on-nvidia/">Run Local Agentic AI Workflows with Meta ’s Muse Glimmer on NVIDIA</a></li>
<li><a href="https://www.phoronix.com/news/Meta-Muse-Glimmer">Meta Publishes Muse Glimmer As 30 B Open Agentic Model - Phoronix</a></li>

</ul>
</details>

**Tags**: `#meta`, `#open-weights`, `#local-ai`, `#agent-workflows`, `#llm`

---

<a id="item-tech-news-4"></a>
### [Exploiting SMM with an Extremely Long Interrupt Instruction](https://github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii) ⭐️ 8.0/10

A GitHub repository titled &\#x27;smiiiiiiiiiiiiiiii&\#x27; by xoreaxeaxeax demonstrates a proof-of-concept exploit of System Management Mode \(SMM\) by using an extremely long interrupt instruction. The technique requires root privileges, so it is not a remote vulnerability, but it reveals how SMM&\#x27;s design assumption that the CPU stops between instructions can be violated. It is significant for firmware security research and offers insight into low-level CPU behavior, including instruction latency boundaries. The repository also references a related &\#x27;Assembly Hall of Shame&\#x27; project that analyzes the slowest possible single instructions.

hackernews · WhiteDawn · Aug 10, 16:03 · [Discussion](https://news.ycombinator.com/item?id=49245491)

**「Background」** System Management Mode \(SMM, sometimes called ring −2\) is a special x86 CPU operating mode that suspends all normal execution, including the operating system, and runs an alternate software system that usually resides in the computer&\#x27;s firmware. The GitHub repository smiiiiiiiiiiiiiiii demonstrates that this supposedly secure, ultra-privileged execution environment can be disrupted by an obscenely long-running machine instruction, showing that SMM&\#x27;s assumptions about instruction boundaries can be violated. This builds on the author&\#x27;s related work on instruction latency, such as the Assembly Hall of Shame, which focuses on the extreme lower bound of single-instruction performance.

**「Impact」** For firmware and low-level security researchers, this repository provides a concrete SMM attack primitive that could be used after an attacker already has root, limiting practical impact to post-compromise scenarios while highlighting a gap in SMM&\#x27;s isolation model. For most users, there is no direct threat because the attack requires elevated privileges.

**「Community Discussion」** Commenters largely agree the technique is more a curiosity than a practical vulnerability because it requires root, with one calling it &\#x27;taking back control of your hardware&\#x27; and noting SMM&\#x27;s user-hostile nature. Others point to the related assembly instruction latency repository and discuss SMM&\#x27;s timeout assumptions and whether the long instruction can actually interact with SMM while it is executing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/System_Management_Mode">System Management Mode - Wikipedia</a></li>
<li><a href="https://github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii">GitHub - xoreaxeaxeax/smiiiiiiiiiiiiiiii: A very very very very very very very long interrupt · GitHub</a></li>

</ul>
</details>

**Tags**: `#security`, `#system-management-mode`, `#firmware`, `#exploit`, `#low-level`

---

<a id="item-tech-news-5"></a>
### [Hand-Compiled Transformer Weights Achieve Perfect Multiplication](https://www.reddit.com/r/MachineLearning/comments/1vkrnb5/transformers_are_famously_bad_at_arithmetic_so_i/) ⭐️ 8.0/10

A developer hand-compiled the grade-school multiplication algorithm into the weights of a stock Phi-3 transformer using a custom compiler called Torchwright, with no training. The resulting three-digit calculator correctly solves all 3,000,000 supported expressions, and published checkpoints support multiplication up to 12 digits by 12 digits with 100% accuracy. In contrast, six frontier models tested without reasoning scored 0/500 on seven-digit multiplication, highlighting their steep accuracy drop on longer numbers. Four versions were built—grade-school, hardware-style, scratchpad, and brute-force memorization—which compute the same function but differ in layer usage, width, generated tokens, and parameters. The checkpoints and code are publicly available on Hugging Face and GitHub.

reddit · r/MachineLearning · /u/notforrob · Aug 10, 17:37

**「Background」** Transformers are normally trained by gradient descent to perform tasks, and they are known to struggle with exact arithmetic because their learned weights only approximate functions. Torchwright takes the opposite approach: it is a compiler that directly constructs the weights of a standard decoder-only transformer from a Python computation graph, with no training. The author used Torchwright to compile a grade-school multiplication algorithm into a Phi-3 checkpoint, so the model&\#x27;s weights embody the algorithm rather than a statistical approximation.

**「Impact」** This demonstration provides a concrete, reproducible baseline showing that an off-the-shelf transformer architecture can perform exact arithmetic when weights are directly compiled, offering a useful tool for mechanistic interpretability and compiler-based model construction. It does not change practical inference for general arithmetic, since the model can only multiply and required hand-engineering rather than learning.

<details><summary>References</summary>
<ul>
<li><a href="https://ood.dev/posts/torchwright-intro/">Introducing torchwright — Out of Distribution</a></li>
<li><a href="https://pypi.org/project/torchwright/">torchwright · PyPI</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#arithmetic`, `#mechanistic interpretability`, `#compilers`, `#machine learning`

---

<a id="item-tech-news-6"></a>
### [antirez releases h3.c native MiniMax-H3 inference for Apple Silicon](https://github.com/antirez/h3.c) ⭐️ 7.0/10

antirez released h3.c, a native MiniMax-H3 inference implementation for Apple Silicon, aiming to enable local video generation on Macs. Early community usage shows it working in practice: one user runs MiniMax H3 on a 64GB MacBook Pro through ComfyUI with GGUF quantizations, choosing Q5\_K\_M or the 34GB Q8\_0, which fits when resolution is modest. Speed is the key bottleneck, with a ~9-second 480x864 clip at 20 steps taking over an hour to generate. Antirez also noted that MiniMax said during an AMA that H3 could support indexed attention, which would be a large speedup, and another user asked whether the implementation still requires 128GB of memory.

hackernews · swyx · Aug 11, 01:22 · [Discussion](https://news.ycombinator.com/item?id=49252179)

**「Background」** MiniMax-H3 is a video-generation model, and antirez—the creator of Redis—has been building h3.c as a native inference engine for running it on Apple Silicon. The project is implemented in plain C with Metal, avoiding Python and PyTorch, and is being developed as vertical slices covering model metadata, Metal compute parity, prompt encoding, prompt-to-video/audio, and conditioning. Running it still requires the MiniMax-H3 checkpoint, FFmpeg, and substantial unified memory, with the developer’s optimization focused on M3 Max and M5 Max.

**「Impact」** Apple Silicon users can now run MiniMax-H3 natively with Metal acceleration, including video/audio conditioning support, without relying on cloud APIs; however, local generation remains resource-intensive, with one user reporting over an hour to generate a 9-second 480x864 clip at 20 steps on an M5 Pro 64GB Mac.

**「Community Discussion」** Reports are positive on practical usability through ComfyUI with GGUF quantizations, though speed remains a concern. Users also debate memory requirements \(some asking whether 128GB is still necessary\) and note the potential for indexed attention to yield major speedups, while another commenter contrasts CUDA-based systems like the DGX Spark for diffusion workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://upstract.com/x/3438bb50f95f2e72">Antirez / h 3 . c : MiniMax H 3 inference engine for Mac computers</a></li>
<li><a href="https://githubawesome.com/h3-c-minimax-h3-video-generation-on-apple-silicon-in-pure-c-and-metal/">h 3 . c : MiniMax H 3 video generation on Apple Silicon in pure C and...</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-08-11-h3-metal-native-minimax-h3-inference-implementation-optimized-for-apple-silicon-m3-and-m5-max-chips">H3-Metal: Native MiniMax-H3 Inference for Apple Silicon</a></li>
<li><a href="https://github.com/antirez/h3.c">GitHub - antirez/h3.c: MiniMax H3 inference engine for Mac ...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#inference`, `#apple-silicon`, `#minimax-h3`, `#machine-learning`

---

<a id="item-tech-news-7"></a>
### [Style-Prompting LLMs Is Lossy and Risks Hallucinations](https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb) ⭐️ 7.0/10

An opinion piece by kuberwastaken argues that &quot;humanising&quot; LLM outputs—forcing generated text into natural, friendly, or stylistically constrained prose—is counterproductive. The author contends that these style instructions are lossy: they are folded into the same generation pass as the actual work, so the model may discard useful information to satisfy the stylistic constraint. The piece further warns that imposing such constraints can increase hallucination risk, because the model may invent filler or blithering to match the desired style. For engineers building LLM-based agents and prompts, the argument suggests that minimal style prompting may be more reliable than elaborate humanisation instructions.

hackernews · kuberwastaken · Aug 10, 13:35 · [Discussion](https://news.ycombinator.com/item?id=49243474)

**「Background」** The blog post criticizes a growing trend in LLM prompting: instructing models to adopt particular writing styles, such as &\#x27;I have ADHD&\#x27; or Simplified Technical English \(ASD-STE100\), to make outputs more concise and readable. The author argues that such stylistic instructions are not post-processing filters but become part of the generation process itself, making the transformation &\#x27;lossy&\#x27; \(like lossy compression\) and potentially triggering hallucinations or inserted filler. This debate reflects wider concerns among developers and users about how to balance readability, fidelity, and reliability in LLM outputs.

**「Impact」** The piece gives prompt engineers a concrete reason to avoid over-prescriptive style directives: because style constraints become part of the generation task itself, they can reduce factual completeness and add hallucinated content rather than improving readability.

**「Community discussion」** Commenters largely agree, with one sharing a prompt for impersonal, objective, engineering-style responses and another noting that style instructions are applied during generation, not after it. Animats reinforces the lossy-style point and suggests that forced style may insert hallucinated blithering, while firefoxd observes that power users have lost their ability to tune search-style inputs in the AI-overview era.

<details><summary>References</summary>
<ul>
<li><a href="https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb">Humanising LLM Outputs is Dumb — Kuber Mehta - kuber.studio</a></li>
<li><a href="https://www.explainx.ai/blog/humanising-llm-outputs-lossy-compression-agents-august-2026">Humanising LLM Output Is Lossy — Render at the Boundary ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#prompt engineering`, `#AI`, `#software engineering`, `#natural language processing`

---

<a id="item-tech-news-8"></a>
### [Nvidia and Wall Street giants raise $500bn for AI infrastructure](https://www.bbc.co.uk/news/articles/c78gr0jv0mdo?at_medium=RSS&amp;at_campaign=rss) ⭐️ 7.0/10

Nvidia has partnered with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, and KKR to raise $500bn \(£370bn\) for AI infrastructure, marking the first time investors treat AI hardware and infrastructure—often called &\#x27;compute&\#x27;—as an asset class. The capital will fund Nvidia&\#x27;s own projects and partner-built data centers and chip factories. Nvidia CEO Jensen Huang said &\#x27;In AI, compute is revenue,&\#x27; while KKR co-CEOs noted &\#x27;delivery, not ambition, is the hard part.&\#x27; The announcement follows over $1tn in collective AI spending by major technology companies in three years and a fivefold rise in Nvidia&\#x27;s market value.

rss · BBC World · Aug 10, 22:31

**「Background」** Nvidia&\#x27;s graphics processing units \(GPUs\) power AI services for nearly every major technology and AI company, including Google, Meta, Amazon, Microsoft, OpenAI, and Anthropic. As demand for AI compute has surged, companies have heavily invested in data centers and chips; Nvidia is now expanding beyond chipmaking to help finance the infrastructure that supports AI deployment.

**「Impact」** The financing gives Nvidia and its partners a new pool of capital to accelerate data-center and chip-factory construction, which could ease persistent AI compute shortages for companies building and running AI products.

**Tags**: `#AI infrastructure`, `#Nvidia`, `#investment`, `#data centers`, `#compute`

---

<a id="item-tech-news-9"></a>
### [Fru: Fast Rust Random Forest with Python/R Bindings](https://www.reddit.com/r/MachineLearning/comments/1vkrvks/fru_fast_random_forest_implementation_p/) ⭐️ 7.0/10

The newly published Software X paper introduces Fru, a Rust-based random forest library with Python and R bindings that aims to offer faster training and inference than mainstream implementations. Its authors report that Fru outperforms scikit-learn&\#x27;s random forest by several factors, with speedups up to hundreds of times in some scenarios, while typically running a few dozen percent faster than the R ranger package and sometimes several times faster. The implementation includes a novel permutation importance routine that adds another performance boost, and uses Arrow PyCapsule in Python to integrate with pandas, polars, pyarrow, and similar tools. Because the benchmarks come from the authors and depend heavily on the use case, independent validation is still needed to confirm the magnitude of the gains.

reddit · r/MachineLearning · /u/kpiwonski · Aug 10, 17:45

**「Background」** Random forest, introduced by Leo Breiman, is an ensemble method that fits many decision trees on bootstrap resamples while constraining split optimization to random feature subsets. Popular implementations include scikit-learn for Python and ranger for R. Fru, described in a Software X paper and available on CRAN, is a Rust-based implementation with Python and R bindings that also introduces a novel permutation importance method.

**「Impact」** Practitioners using CPU-bound random forest workflows in Python or R could benefit from substantially lower training times, particularly in cases where Fru&\#x27;s reported multi-factor speedups apply, though actual gains will depend on dataset size, feature dimensionality, and the exact algorithm configurations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2352711026004097">fru: Fast random forest implementation - ScienceDirect</a></li>
<li><a href="https://cran.r-project.org/web/packages/fru/fru.pdf">fru: A Blazing Fast Implementation of Random Forest</a></li>
<li><a href="https://cran.r-project.org/package=fru">CRAN: Package fru</a></li>

</ul>
</details>

**Tags**: `#random forest`, `#Rust`, `#machine learning`, `#performance`, `#library`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Nvidia and six asset managers target $500 billion for AI infrastructure financing](https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html) ⭐️ 9.0/10

Nvidia and six asset managers—Apollo, Blackstone, BlackRock, Brookfield, Goldman Sachs and KKR—said Monday they signed memorandums of understanding to build financing platforms that aim to mobilize more than $500 billion in third-party capital for data centers and Nvidia hardware. CEO Jensen Huang described the chips as an &quot;investable asset class&quot; that is revenue-generating, long-lived and transferable.

rss · CNBC Finance · Aug 10, 22:09

**「Background」** The plan challenges the long-held view that GPUs rapidly depreciate, treating AI compute like infrastructure that can be borrowed against, similar to real estate or toll roads. It comes after a July global market selloff prompted questions about whether Big Tech&\#x27;s heavy AI spending will pay off.

**Tags**: `#Nvidia`, `#AI infrastructure`, `#asset financing`, `#capital markets`, `#data centers`

---

<a id="item-finance-news-2"></a>
### [Premarket Movers: Intel $15B Stock Offering, GameStop&\#x27;s Possible eBay Bid Withdrawal, Verisk Acquisition Ruling](https://www.cnbc.com/2026/08/10/stocks-making-the-biggest-moves-premarket-aapl-hpe-rklb-and-more.html) ⭐️ 7.0/10

Several major stocks moved in premarket trading Monday: Intel fell 3% after announcing a $15 billion common stock offering, GameStop rose more than 1.5% on a Bloomberg report it may withdraw its $56 billion bid for eBay, and Verisk Analytics slid more than 6.5% after a Delaware judge ordered it to complete its $2.35 billion acquisition of AccuLynx.

rss · CNBC Finance · Aug 10, 13:52

**「Background」** GameStop&\#x27;s unsolicited bid for eBay was rejected by eBay in May, and Verisk had terminated the AccuLynx deal in December because an FTC review was not completed by the deadline.

**Tags**: `#M&amp;A`, `#Stock offerings`, `#Corporate earnings`, `#Analyst ratings`, `#Legal rulings`

---