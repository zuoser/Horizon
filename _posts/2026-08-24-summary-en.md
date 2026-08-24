---
layout: default
title: "Horizon Summary: 2026-08-24 (EN)"
date: 2026-08-24
lang: en
---

> From 155 items, 11 important content pieces were selected

---

**Technology News**
1. [MS Paint and Photos Add Invisible GUID Watermarks to AI-Edited Images](#item-tech-news-1) ⭐️ 8.0/10
2. [San Francisco recreated as a playable web-based 3D map](#item-tech-news-2) ⭐️ 8.0/10
3. [seL4 security proofs complete on AArch64, with caveats](#item-tech-news-3) ⭐️ 8.0/10
4. [AI Coding Reliance Threatens Deep Software Engineering Expertise](#item-tech-news-4) ⭐️ 7.0/10
5. [Nearly 3M Teslas Recalled in China Over Hidden Door Handles](#item-tech-news-5) ⭐️ 7.0/10
6. [Executable SQLite Databases via the SELF Format](#item-tech-news-6) ⭐️ 7.0/10
7. [Does CUDA&\#x27;s Moat Survive Agentic Inference? SemiAnalysis Weighs In](#item-tech-news-7) ⭐️ 7.0/10
8. [Unbounded Labs Releases Bart, a Vintage LLM Trained on Pre-1931 English](#item-tech-news-8) ⭐️ 7.0/10
9. [AI Generates 3D Objects as Programmable Spatial Software](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [Bitcoin extends rally after biggest three-day gain since 2023](#item-finance-news-1) ⭐️ 8.0/10
2. [Alibaba shares plunge after $10.2 billion share placement for AI](#item-finance-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [MS Paint and Photos Add Invisible GUID Watermarks to AI-Edited Images](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

A reverse-engineering analysis of Microsoft Paint and Microsoft Photos found that both apps silently embed an invisible GUID watermark into images edited using AI features, even when the AI model runs locally. The apps also add a visible watermark that users can disable, but the invisible identifier cannot be turned off and is inserted without user notice. The practice raises privacy and anonymity concerns because a unique identifier could potentially be used to trace an image back to a Microsoft account, and local processing does not guarantee that the complete operation stays local. The finding is based on analysis of the apps&\#x27; behavior rather than official Microsoft documentation.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**「Background」** Microsoft Paint and Photos now include AI-powered editing features that can run models locally on the device, but a reverse-engineering analysis found that even locally generated images receive an invisible GUID watermark. According to the analysis, Microsoft still receives and moderates the prompt in the cloud, then issues the unique GUID that Paint embeds into the locally generated image, allowing output to be traced back to the user&\#x27;s Microsoft account. This hidden identifier sits alongside a visible watermark that can be turned off, but the invisible GUID cannot be disabled.

**「Impact」** Users who AI-edit images in Paint or Photos may unknowingly produce files carrying a unique identifier that, if shared, could be traced to their Microsoft account, undermining anonymity and inviting regulatory scrutiny under data-protection rules. The exact scope, including whether features like AI-enhanced background removal are affected, remains unclear.

**「Community Discussion」** Commenters broadly agree the hidden identifier is a privacy problem, with one arguing the AI framing is a red herring and that a subpoena to Microsoft could link an image to a user&\#x27;s account; another cites Microsoft&\#x27;s recent incorrect Copilot watermark on Azure DevOps commits as evidence of sloppy implementation. A separate commenter laments that Paint no longer remains a simple pixel editor.

<details><summary>References</summary>
<ul>
<li><a href="https://zeli.app/story/49421158">Microsoft Paint and Photos Embed Server-Issued GUIDs as... | Zeli</a></li>
<li><a href="https://news.ycombinator.com/item?id=49421158">MS Paint and Photos inivisibly watermark even locally generated ...</a></li>

</ul>
</details>

**Tags**: `#watermarking`, `#privacy`, `#AI-generated content`, `#Windows`, `#reverse engineering`

---

<a id="item-tech-news-2"></a>
### [San Francisco recreated as a playable web-based 3D map](https://sf.thijs.gg/) ⭐️ 8.0/10

A web-based interactive 3D recreation of San Francisco built from GIS data is now playable at sf.thijs.gg, letting users explore the city in a browser and collect coins while driving a vehicle. The project demonstrates how published geographic data can be turned into a lightweight, accessible game environment, and it has generated substantial community interest and discussion. It currently includes the city&\#x27;s layout and terrain from GIS sources, though commenters note there is no deeper game loop beyond driving and coin collection. The site appeared as the subject of a Hacker News submission and drew reactions from former San Francisco residents and developers working on similar city-scale projects.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**「Background」** This item is a web-based interactive 3D recreation of San Francisco generated from real-world geographic information system \(GIS\) data—typically building footprints, elevation, and map layers—compiled into a playable city. San Francisco publishes such geospatial data through its Enterprise GIS Program, which provides open mapping data and services, lowering the barrier for developers to build city-scale simulations. The project follows earlier video games set in a modeled San Francisco, but uses actual city data rather than hand-authored geometry.

**「Impact」** For people familiar with San Francisco, the simulation offers an emotionally resonant way to revisit familiar locations, as one long-time resident described being moved to tears while exploring their old neighborhood. For developers, it showcases a low-barrier pipeline for converting real-world GIS data into playable 3D city experiences and may inspire similar community-built maps for other cities.

**「Community Discussion」** Commenters shared related projects, such as a Philadelphia-based city game built on GIS data, and discussed the dream of a full pipeline that could turn elevation, building, map, and street-view data into assets for engines like GTA. Several users requested enhancements like higher-resolution textures from Street View, street names, landmarks, address teleporting, and a live MMO mode, while others simply expressed delight at walking through the disc golf course and favorite neighborhood spots.

<details><summary>References</summary>
<ul>
<li><a href="https://sfgov.maps.arcgis.com/home/index.html">City and County of San Francisco - ArcGIS</a></li>

</ul>
</details>

**Tags**: `#GIS`, `#3D rendering`, `#game development`, `#San Francisco`, `#web-based game`

---

<a id="item-tech-news-3"></a>
### [seL4 security proofs complete on AArch64, with caveats](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

The seL4 microkernel&\#x27;s formal security proofs are now complete for AArch64, marking an important milestone for verified computing on ARM. The completion was announced on August 21, 2026 via Proofcraft Systems, extending the formally verified microkernel to a new architecture. However, the proofs cover only a unicore, non-MCS \(mixed-criticality systems\) configuration, and unresolved side-channel timing concerns remain. This means the verified guarantee does not yet extend to multicore systems, mixed-criticality scheduling, or timing-based attacks.

hackernews · snvzz · Aug 24, 11:32 · [Discussion](https://news.ycombinator.com/item?id=49418255)

**「Background」** seL4 is a microkernel whose implementation has been formally verified for functional correctness, and whose verification effort has been extended over the years to security properties such as integrity, availability, and confidentiality, as well as binary correctness. The newly completed proof for AArch64 closes the formal security-enforcement argument for that architecture, demonstrating that the seL4 implementation enforces isolation for applications running on top of it. However, the verified configuration is non-MCS and single-core, and the proof does not cover microarchitectural side-channel timing, so its guarantees are limited to that specific setup.

**「Impact」** Developers building secure ARM-based systems now have a formally verified microkernel foundation for single-core, non-mixed-criticality use cases, but real-world deployments with multicore or mixed-criticality requirements will still need additional verification.

**「Community Discussion」** Commenters quickly noted the caveats, with one warning that a side-channel timing attack could completely invalidate the result and another pointing out the fine print about non-MCS and unicore. Discussion also covered known seL4 users such as GenodeOS, LionsOS, and a Chinese car maker, while another commenter expressed skepticism about seL4&\#x27;s security claims without a native seL4/Linux approach.

<details><summary>References</summary>
<ul>
<li><a href="https://news.linxi.com.au/news/sel4-microkernel-achieves-full-formal-security-verification-on-aarch64">seL4 Microkernel Formal Security Proofs Completed on AArch64 ...</a></li>
<li><a href="https://sel4.systems/Verification/proofs.html">seL4 Proofs | seL4</a></li>
<li><a href="https://deepwiki.com/seL4/website/5.2-formal-verification">Formal Verification | seL4/website | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#seL4`, `#AArch64`, `#microkernel`, `#security`

---

<a id="item-tech-news-4"></a>
### [AI Coding Reliance Threatens Deep Software Engineering Expertise](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 7.0/10

The article by Lars Faye argues that excessive reliance on AI coding tools will collapse deep coding expertise, warning that productivity gains come at the cost of long-term skill formation. The piece has sparked a widespread debate, including a 415-comment Hacker News discussion, about the future of software engineering abilities and engineering culture. Key concerns include engineers producing code faster than humans can understand or review, and the potential erosion of foundational expertise as AI tools increasingly handle the mechanics of programming.

hackernews · larsfaye · Aug 24, 15:52 · [Discussion](https://news.ycombinator.com/item?id=49421554)

**「Background」** The article argues that reliance on AI coding assistants such as Claude Code and Antigravity—which can write, debug, and even perform system design from training-data patterns—removes the productive friction that historically helped developers build deep expertise. The piece describes a &\#x27;pipeline collapse&\#x27; where the knowledge and skills needed for software engineering may stop being formed if LLMs handle the work.

**「Impact」** As AI-assisted coding becomes mandated in some enterprises, codebases may grow faster than human review capacity, increasing maintainability risks and placing a disproportionate review burden on engineers who choose not to rely on AI for coding.

**「Community discussion」** Commenters are divided: some report enterprise mandates that treat manual coding as wrong, leading to unsustainable review loads and skill erosion, while others emphasize that guided, integrated AI coding can boost productivity without sacrificing quality or enjoyment. One educator agrees with the article, and several argue that strong engineers still seek out productive friction, but the overall consensus is that the issue deserves serious attention.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49421554">Coding expertise is going to collapse from AI reliance | Hacker News</a></li>
<li><a href="https://larsfaye.com/articles/ai-coding-will-prevent-expertise">AI Coding will Prevent Expertise | Lars Faye</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#software engineering`, `#skill formation`, `#expertise`, `#developer productivity`

---

<a id="item-tech-news-5"></a>
### [Nearly 3M Teslas Recalled in China Over Hidden Door Handles](https://www.bbc.co.uk/news/articles/c4g6ggdg030o?at_medium=RSS&amp;at_campaign=rss) ⭐️ 7.0/10

China&\#x27;s largest car recall is affecting more than 4 million vehicles, including 2.98 million Chinese-made Teslas, because hidden door handles are difficult to locate and open in emergencies. Tesla&\#x27;s recall covers Model 3, Y, S, and X vehicles, and the fix includes placing warning labels on interior doors and issuing a software update that automatically lowers windows after a collision. The wider recall also affects Chinese carmakers XPeng, Xiaomi, and Geely. The move follows safety scrutiny after two fatal Xiaomi EV crashes and a Chinese regulation that will ban hidden door handles starting in 2027. It remains unclear whether similar recalls will be issued in other countries.

rss · BBC World · Aug 24, 05:01

**「Background」** Hidden door handles that sit flush with the vehicle body became a popular electric vehicle design trend after Tesla&\#x27;s Model S sedan in 2014. While sleek, these handles can be difficult to operate in emergencies, especially if a crash causes the vehicle&\#x27;s low-voltage system to fail. Chinese authorities have announced a ban on the design from 1 January 2027, and US safety regulators have also investigated Tesla&\#x27;s door handles after reports of children being trapped.

**「Impact」** Owners of the affected Teslas and other EVs in China will receive warning labels and a software update to lower windows after crashes, but experts describe this as a &\#x27;band-aid&\#x27; rather than a lasting solution, and there is no confirmation of similar action outside China.

**Tags**: `#Tesla`, `#Electric Vehicles`, `#Automotive Safety`, `#Recall`, `#China`

---

<a id="item-tech-news-6"></a>
### [Executable SQLite Databases via the SELF Format](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria has described a Linux technique that makes SQLite database files directly executable by embedding ELF executable components in SQLite tables. The trick sets the 4-byte application ID in SQLite&\#x27;s header at byte offset 68 to the ASCII string SELF \(Structured Executable &amp; Linkable Format\), then organizes ELF pieces into several database tables using a published schema. A companion interpreter, self-exec, extracts and runs the embedded code, and Linux&\#x27;s binfmt\_misc mechanism can be configured so the kernel automatically dispatches any executable carrying that marker. Farid uses NixOS in the example, and a registration command for non-NixOS systems maps the pattern to /usr/local/bin/self-exec. This creates a hybrid file format that is both a valid SQLite database and a working executable, with interesting implications for systems programming.

rss · Simon Willison · Aug 24, 11:38

**「Background」** SQLite database files begin with a fixed header structure that includes a 4-byte application ID, typically used to identify the file&\#x27;s format. ELF is the standard binary format for executables on Linux, and binfmt\_misc is a kernel feature that allows non-standard executable formats to be dispatched to user-space interpreters based on a byte-pattern match.

**Tags**: `#SQLite`, `#ELF`, `#Linux`, `#binfmt\_misc`, `#systems programming`

---

<a id="item-tech-news-7"></a>
### [Does CUDA&\#x27;s Moat Survive Agentic Inference? SemiAnalysis Weighs In](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat) ⭐️ 7.0/10

SemiAnalysis published an analysis by Cam Quilici examining whether CUDA&\#x27;s competitive moat holds up for agentic inferencing. The piece cites newly released resources including an open-sourced $3 million USD dataset with 1 million-plus context length, multiturn interactions, and subagents, as well as a claimed 95%+ KVCache hit rate. It also compares NVIDIA GB300 NVL72 and B200 hardware against AMD MI355 for agentic inference workloads. The central question is whether CUDA remains defensible as AI workloads shift toward long-context, multi-agent inference rather than conventional training or single-turn serving.

rss · SemiAnalysis · Aug 24, 00:19

**「Background」** CUDA is NVIDIA&\#x27;s proprietary software stack that lets developers use its GPUs for general computation, and its ecosystem of frameworks and optimizations has long been considered a competitive moat protecting NVIDIA&\#x27;s hardware. The rise of agentic inference—workloads with very long contexts, multiturn interactions, and sub-agents—tests whether that software advantage holds on competitor hardware such as AMD&\#x27;s MI355X. According to SemiAnalysis coverage, AMD&\#x27;s implementation of distributed communication primitives such as DCP/PCP is not yet optimized, and in the vLLM support matrix every AMD backend is currently unsupported. Meanwhile, AI coding agents themselves are emerging as a threat to the moat, because they can generate the low-level, CUDA-compatible code that previously required human engineers.

**「Impact」** Infrastructure decision-makers can use the head-to-head GB300 NVL72, B200, and MI355 comparisons to assess whether NVIDIA&\#x27;s CUDA ecosystem still justifies lock-in for agentic inference deployments.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic Inferencing?</a></li>
<li><a href="https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing">Can AMD break the CUDA Moat? AMD Advancing AI 2026</a></li>
<li><a href="https://thenextweb.com/news/nvidia-cuda-moat-ai-coding-agents-inference">Nvidia’s CUDA moat faces its first real threat: AI itself</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#Agentic Inference`, `#KVCache`, `#GPU Hardware`, `#AI Infrastructure`

---

<a id="item-tech-news-8"></a>
### [Unbounded Labs Releases Bart, a Vintage LLM Trained on Pre-1931 English](https://www.reddit.com/r/MachineLearning/comments/1vx94er/bart_a_vintage_llm_r/) ⭐️ 7.0/10

Unbounded Labs released Bart \(Bartholomew\), a 2.82B-parameter LLM trained from scratch on 20.1B tokens of English text written before 1931, with an interactive demo, a detailed blog article, and a Hugging Face model. The project tests whether LLMs can independently rediscover historical scientific conclusions, as proposed by Demis Hassabis, and includes the creation of Vintage CORE, a suite of 20 benchmarks built specifically for vintage LLMs, along with a 416k-question SFT dataset grounded in pre-1930s text. The final model was trained in five days on a single H100 at 60% MFU, with total costs of about $807, and all datasets, methodology, training code, evals, and training runs were open sourced. The team also reported cleaning Harvard&\#x27;s Institutional Books from 242B to 23B tokens and running 100 autonomous experiments that produced 26 improvements, with the base model outperforming GPT-1900 on Vintage CORE at a smaller token budget.

reddit · r/MachineLearning · /u/soggydoggy8 · Aug 24, 17:20

**「Background」** Demis Hassabis has proposed that AI systems could rediscover scientific ideas or conclusions that past scientists reached, since nature is not random and efficient representations can be recovered. Bart is a large language model trained from scratch on 20.1B tokens of English written before 1931, specifically to test whether such a model can arrive at insights similar to those of historical scientists. Because no suitable benchmarks existed for evaluating models on vintage text, the researchers also built a new benchmark suite and a cleaned corpus from Harvard&\#x27;s Institutional Books.

**「Impact」** By open-sourcing a complete training pipeline, model, benchmarks, and datasets for under $1,000, Unbounded Labs gives the research community reproducible, low-cost resources for studying how training data and domain constraints affect LLM capabilities and for evaluating whether models can rediscover historical scientific ideas.

<details><summary>References</summary>
<ul>
<li><a href="https://lexfridman.com/demis-hassabis-2-transcript/">Transcript for Demis Hassabis: Future of AI, Simulating Reality, Physics and Video Games | Lex Fridman Podcast #475 - Lex Fridman</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#retrieval`, `#research`, `#dataset`, `#machine-learning`

---

<a id="item-tech-news-9"></a>
### [AI Generates 3D Objects as Programmable Spatial Software](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

A co-author of a new machine-learning paper describes using LLMs as spatial software generators that produce 3D objects as programmable programs rather than monolithic mesh blobs. The resulting objects are composed of logical parts, are animation-ready and programmable from creation, and can adapt detail for weak compute environments such as mobiles versus powerful game engines. They can include full hierarchical structure and hinge/socket articulation at authoring time. The author acknowledges the approach lags traditional AI 3D generators on complex organic shapes, but sees code as eventually dominating all 3D generation. Visual demonstrations and a GitHub repository are available at nova3d.xyz.

reddit · r/MachineLearning · /u/mhb\_11 · Aug 24, 19:10

**「Background」** Traditional AI 3D generators typically output monolithic mesh geometry—static polygon &quot;blobs&quot; that are difficult to edit, animate, or adapt across environments. The Nova3D approach instead uses large language models to generate 3D assets as executable spatial programs, so objects are composed of named logical parts \(e.g., Door, Gearbox, Steering Wheel\) that downstream systems can inspect, measure, modify, and animate.

**「Impact」** For 3D developers and designers, the shift toward LLM-generated spatial software promises inherently programmable, animation-ready objects that can adapt detail to device performance, but the approach currently lags behind traditional AI generators on complex organic shapes, so immediate disruption is most likely in industrial design, game development, simulation, and AR/VR/XR workflows. External industry analyses already highlight AI-assisted 3D modeling&\#x27;s broad impact across industrial design, prototyping, video games, and cinema, supporting the author&\#x27;s expectation that these sectors will see the strongest effects.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.22738v1">Nova3D: Code-Native Generation of Programmable 3D Assets Generating structured, editable, constraint-consistent 3D assets as executable programs</a></li>
<li><a href="https://x.com/nova3d_ai">Nova3D (@nova3d_ai) / Posts / X</a></li>
<li><a href="https://arxiv.org/html/2607.22738">Nova3D: Code-Native Generation of Programmable 3D AssetsGenerating structured, editable, constraint-consistent 3D assets as executable programs</a></li>
<li><a href="https://www.giuseppegalliano.eu/risorse-e-guide/artificial-intelligence-and-3d-modeling/">Artificial Intelligence and 3D Modeling - AI-powered 3D content generation.</a></li>
<li><a href="https://resources.imagine.io/blog/the-future-of-industrial-design-how-ai-3d-visualization-are-changing-the-game">The Future of Industrial Design: How AI &amp; 3D Visualization Are Changing the Game</a></li>

</ul>
</details>

**Tags**: `#3D generation`, `#large language models`, `#spatial programming`, `#programmable objects`, `#animation`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Bitcoin extends rally after biggest three-day gain since 2023](https://www.cnbc.com/2026/08/24/crypto-extends-gains-after-biggest-3-day-rally-since-2023.html) ⭐️ 8.0/10

Bitcoin extended its rally Monday, trading just under $80,000, after a more than 20% gain over three days—its largest such rally since 2023—supported by a macro shift, $1.92 billion in weekly spot bitcoin ETF inflows, and more than $4 billion in liquidated bearish crypto positions.

rss · CNBC Finance · Aug 24, 20:02

**「Background」** Bitcoin had been stuck in a prolonged slump since October, before a macro shift last week: the Treasury said it would double purchases of longer-dated government bonds, briefly pushing yields lower and reviving demand for risk assets like bitcoin. The move triggered a short squeeze, with more than $4 billion in bearish crypto positions liquidated as prices rose.

**「Impact」** The rally also lifted crypto-treasury stocks, with Strive up 8%, Strategy up 2%, and ETH treasury names Bitmine and Sharplink gaining 5% and 4%, respectively.

**Tags**: `#bitcoin`, `#cryptocurrency`, `#ETF inflows`, `#short squeeze`, `#Treasury bonds`

---

<a id="item-finance-news-2"></a>
### [Alibaba shares plunge after $10.2 billion share placement for AI](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html) ⭐️ 8.0/10

Alibaba priced an HK$80 billion \($10.20 billion\) placement of 710 million new shares at HK$112.70 apiece to non-U.S. investors to fund AI infrastructure, and its Hong Kong shares fell as much as 10% on Monday.

rss · CNBC Finance · Aug 24, 08:21

**「Background」** The deal follows Alibaba&\#x27;s June-quarter report showing profit down 75% while capital expenditure jumped 75% to 67.7 billion yuan; the company has previously pledged at least 380 billion yuan in cloud and AI infrastructure over three years.

**「Impact」** The issuance of 710 million new shares will dilute existing shareholders&\#x27; stakes.

**Tags**: `#Alibaba`, `#share placement`, `#AI investment`, `#capital expenditure`, `#Hong Kong market`

---