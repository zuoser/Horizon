---
layout: default
title: "Horizon Summary: 2026-08-22 (EN)"
date: 2026-08-22
lang: en
---

> From 100 items, 6 important content pieces were selected

---

**Technology News**
1. [MCP Roadmap Targets HTTP Normalization and Agent Identity](#item-tech-news-1) ⭐️ 8.0/10
2. [Chinese robot Lightning runs 100m in 9.32 seconds, beating Bolt&\#x27;s record](#item-tech-news-2) ⭐️ 7.0/10
3. [Meta accused in landmark trial of &\#x27;hook, hold, harvest, hide&\#x27; strategy](#item-tech-news-3) ⭐️ 7.0/10
4. [Developer builds 250M-parameter quantized LLM that runs in 60 MB](#item-tech-news-4) ⭐️ 7.0/10
5. [DelveRL: Open-Source Roguelike for Training Game-Playing Agents](#item-tech-news-5) ⭐️ 7.0/10
6. [Evaluation resolution flips which learning rule looks most brain-like at V1](#item-tech-news-6) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [MCP Roadmap Targets HTTP Normalization and Agent Identity](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) ⭐️ 8.0/10

The MCP \(Model Context Protocol\) project has published a roadmap focused on making remote MCP servers behave like standard HTTP workloads and standardizing how agents are authorized. The roadmap directly addresses prominent criticism of the initial protocol design, which some developers called a needlessly bespoke new protocol. Planned work includes giving servers a standardized way to recognize and trust agent identities for cloud workloads, delegated sub-agents, and users who are not present, built on existing standards. This matters for AI tool interoperability because MCP connects increasingly capable models to external systems, and remote server support has been a major limitation. The roadmap frames the target as making a remote MCP server no different from any other HTTP workload, with a cited release milestone of 2026-07-28.

hackernews · pentagrama · Aug 22, 13:31 · [Discussion](https://news.ycombinator.com/item?id=49399591)

**「Background」** The Model Context Protocol \(MCP\) is an open standard introduced by Anthropic in November 2024 to standardize how AI systems like large language models integrate with external tools, data sources, and systems. Anthropic published an updated roadmap for MCP covering the next specification release and beyond, focusing on transport scalability, agent communication, governance maturation, and enterprise readiness. The roadmap aims to address major criticisms of the protocol, including making remote servers behave like standard HTTP workloads and standardizing agent authorization.

**「Impact」** MCP server operators and client maintainers will need to update their implementations to align with HTTP semantics and the new agent authorization model, with the clearest benefit for cloud-hosted agents acting on behalf of users.

**「Community Discussion」** Commenters largely welcome the shift toward standard HTTP workloads, calling the original bespoke protocol one of MCP&\#x27;s more bone-headed initial decisions, but they remain skeptical about how many servers will fully implement the authorization system and whether MCP endpoints are genuinely easier for agents than REST plus a skills file.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://blog.modelcontextprotocol.io/posts/mcp-roadmap/">The New MCP Roadmap | Model Context Protocol Blog</a></li>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/">The 2026 MCP Roadmap | Model Context Protocol Blog</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#AI infrastructure`, `#protocols`, `#authentication`, `#LLM tools`

---

<a id="item-tech-news-2"></a>
### [Chinese robot Lightning runs 100m in 9.32 seconds, beating Bolt&\#x27;s record](https://www.theguardian.com/sport/2026/aug/22/chinese-robot-runs-100m-sprint-quicker-usain-bolt-world-record) ⭐️ 7.0/10

Lightning, a humanoid robot developed by Chinese smartphone maker Honor, ran 100 meters in 9.32 seconds at a test event for the second World Humanoid Robot Games in Beijing, according to China&\#x27;s state broadcaster. That time beats the 9.58-second men&\#x27;s world record set by Usain Bolt 17 years ago and included a peak speed of 14.5 meters per second. The run marks a notable milestone in humanoid robotics, though the report provides no technical details about the robot&\#x27;s design or the conditions of the run.

rss · The Guardian International · Aug 22, 10:25

**「Background」** Usain Bolt&\#x27;s 100m world record of 9.58 seconds was set at the 2009 World Athletics Championships in Berlin. The second World Humanoid Robot Games in Beijing feature humanoid robots competing in physical events, and the 9.32-second sprint by Honor&\#x27;s Lightning robot occurred during a test event before the games. Humanoid robots have been advancing in speed and agility, but this performance highlights a milestone where a bipedal machine beat the fastest human in a sprint.

**「Impact」** The 9.32-second sprint gives robot developers and event organizers a new, concrete benchmark for humanoid robot speed, surpassing the fastest human 100m time and likely raising expectations for future World Humanoid Robot Games demonstrations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nbcnews.com/tech/tech-news/chinese-humanoid-robot-lightning-beats-human-100m-world-record-rcna593869">Move over, Usain Bolt: Humanoid robots smash human records at Beijing games</a></li>
<li><a href="https://www.dw.com/en/chinese-robot-beats-usain-bolts-100m-world-record/a-78468749">Chinese robot beats Usain Bolt&#x27;s 100m world record</a></li>
<li><a href="https://www.abc.net.au/news/2026-08-22/the-robot-that-can-beat-usain-bolt/107067592">Chinese humanoid robot &#x27;Lightning&#x27; beats Usain Bolt&#x27;s 100 metres world record in test run - ABC News</a></li>

</ul>
</details>

**Tags**: `#humanoid robots`, `#robotics`, `#Honor`, `#technology news`, `#sprint`

---

<a id="item-tech-news-3"></a>
### [Meta accused in landmark trial of &\#x27;hook, hold, harvest, hide&\#x27; strategy](https://www.theguardian.com/technology/2026/aug/22/meta-trial-children-privacy) ⭐️ 7.0/10

In a landmark trial that opened on Tuesday, California and 28 other states accused Meta of designing addictive sites and violating laws that protect children&\#x27;s privacy. During opening arguments, a lawyer prosecuting the case argued that Meta&\#x27;s business model can be boiled down to four words: hook, hold, harvest, and hide. The owner of Facebook and Instagram allegedly &quot;hooks&quot; users, &quot;holds&quot; them on its platforms for as long as possible, &quot;harvests&quot; their data, and then &quot;hides&quot; the truth from the public. The case centers on the company&\#x27;s platform design practices and its handling of young users&\#x27; data, and could carry significant implications for social media regulation.

rss · The Guardian International · Aug 22, 08:00

**「Background」** Meta, the parent company of Facebook and Instagram, is facing multiple state-led lawsuits over its treatment of young users. The first federal trial opened in August 2026 with California and 28 other states accusing Meta of using addictive product design and of violating children&\#x27;s privacy laws. Additional cases brought by more states are scheduled for later trials, and Meta has said it disputes the allegations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cpr.org/2026/08/18/meta-facebook-social-media-trial-oakland/">States take Meta to trial in California in the biggest fight yet over ...</a></li>
<li><a href="https://www.cnbc.com/2026/08/17/meta-attorneys-general-california-federal-trial-astronomical-consequences.html">Meta faces state AG trial over child safety claims - CNBC</a></li>

</ul>
</details>

**Tags**: `#social media`, `#privacy`, `#regulation`, `#tech industry`, `#Meta`

---

<a id="item-tech-news-4"></a>
### [Developer builds 250M-parameter quantized LLM that runs in 60 MB](https://www.reddit.com/r/MachineLearning/comments/1vv2nkh/i_developed_my_own_quantized_llm_from_scratch/) ⭐️ 7.0/10

A developer trained a 250M-parameter language model from scratch on 30B tokens of FineWeb, quantized it to under 2 bits, and shipped the full deployment at 60 MB with about 80 MB of RAM usage. Running at roughly 400 tokens per second on a laptop CPU without a GPU, the model keeps the most recent 2,048 tokens in an FP16 KV cache and compresses older context to 1 bit on disk at about 320 bytes per token, supporting retrieval from up to 100M tokens of archive history. The base model, evaluated on held-out educational English web pages, achieves 3.15 nats per token \(perplexity 23.3, 0.99 bits per byte\). Its vocabulary uses fixed 512-bit codes for 131k tokens with no trained embedding parameters, scoring 0.619 Spearman correlation on WordSim-353 versus 0.029 for random codes. The full fine-tuning kit and master weights are available as SHADOW-250M-Instruct on GitHub and NODEMIND/SHADOW-250M on Hugging Face.

reddit · r/MachineLearning · /u/Final-Data-1410 · Aug 22, 04:39

**「Background」** Quantization compresses neural networks by storing weights in fewer bits, trading some accuracy for lower memory and faster inference on ordinary hardware. The post&\#x27;s approach also uses a disk-backed cache that preserves recent context in high precision while compressing older tokens to 1 bit, which lets the model retrieve from extremely long histories without needing to hold them in RAM.

**「Impact」** For developers targeting CPU-only or memory-constrained environments, this demonstrates a working sub-2-bit 60 MB LLM with long-context retrieval, though the author cautions that the model was not trained to reason over retrieved content and can make mistakes on open facts.

**Tags**: `#quantization`, `#long-context`, `#efficient-deployment`, `#language-model`, `#from-scratch-training`

---

<a id="item-tech-news-5"></a>
### [DelveRL: Open-Source Roguelike for Training Game-Playing Agents](https://www.reddit.com/r/MachineLearning/comments/1vvii1j/i_built_an_opensource_roguelike_specifically_for/) ⭐️ 7.0/10

Developer SnyderConsulting released DelveRL, an open-source, human-playable roguelike built specifically for training game-playing agents. The environment includes a structured API, deterministic simulation, procedural levels, partial observability, and strategic challenges such as exploration, resource and risk management, combat, and escaping each floor. It runs entirely locally, with batched renderer-free environments and a recurrent PPO trainer included. The baseline agent reaches a median floor of 18, with extended runs reaching floor 33. The game, training code, checkpoint, bridge documentation, and raw benchmarks are all open source, addressing the common difficulty of integrating existing games with agent harnesses.

reddit · r/MachineLearning · /u/SnyderConsulting · Aug 22, 17:32

**「Background」** Reinforcement-learning projects from organizations like DeepMind and OpenAI often rely on game environments, but many existing games are difficult to integrate with custom agent training harnesses. DelveRL is a turn-based roguelike, a genre defined by procedurally generated dungeons, permadeath, and tactical decision-making, which makes it well suited for testing agent exploration, planning, and resource management under partial observability.

**「Impact」** Machine-learning researchers and game-AI developers can now use DelveRL as a reproducible, locally runnable environment with baseline benchmarks and a ready-to-use PPO trainer, reducing the engineering overhead of creating or adapting game environments for agent research.

**Tags**: `#reinforcement-learning`, `#open-source`, `#game-ai`, `#environments`, `#procedural-generation`

---

<a id="item-tech-news-6"></a>
### [Evaluation resolution flips which learning rule looks most brain-like at V1](https://www.reddit.com/r/MachineLearning/comments/1vvdxwt/the_evaluation_resolution_has_been_shown_to_have/) ⭐️ 7.0/10

An analysis posted on Reddit reports that the resolution at which stimuli are evaluated can reverse conclusions about which learning rule is most brain-like in V1 model-brain comparisons, indicating that the widely repeated claim that untrained CNNs match or surpass backpropagation-trained CNNs at V1 is largely an artifact of evaluation resolution. The authors trained a small CNN at 32px on a CIFAR-10 subset, compared five learning rules \(random init, backprop, feedback alignment, predictive coding, STDP\) against THINGS-fMRI stimuli at six resolutions from 32px to 224px, and found the trained-versus-untrained backprop V1 gap shifted non-monotonically from -0.001±0.007 at 32px to +0.044±0.006 at 224px across n=5 seeds. They ruled out train/eval resolution mismatch, Gabor/pixel low-level structure, uncalibrated batch-norm in untrained baselines, and convergence of pooled features toward global brightness, while noting that a single scalar luminance value reached rho=0.075 against V1, almost matching the untrained network&\#x27;s 0.076. One resolution-independent effect remained: backprop outperformed untrained networks at the LOC \(lateral occipital complex\) across every tested resolution. The preprint is available at arXiv:2608.12408 and code at github.com/nilsleut/evaluation-resolution-rsa; the release also fixes a batch-norm evaluation-mode bug that had affected three earlier preprints.

reddit · r/MachineLearning · /u/ConfusionSpiritual19 · Aug 22, 14:30

**「Background」** Model-brain comparisons use representational similarity analysis \(RSA\) to test which neural network internal representations best predict responses in brain regions such as the early visual cortex \(V1\). A recurring claim has been that untrained CNNs are as good as or better than backpropagation-trained CNNs at explaining V1, but this conclusion depends on the resolution of the stimuli used for evaluation, with small images allowing low-level features to dominate the comparison.

**「Impact」** Researchers performing model-brain comparisons should treat evaluation resolution as a controlled variable and avoid relying on low-resolution V1 comparisons to claim that training or learning rules do not matter, because the observed brain-likeness ranking is resolution-dependent.

**Tags**: `#neuroscience`, `#model-brain comparison`, `#CNNs`, `#learning rules`, `#evaluation methodology`

---