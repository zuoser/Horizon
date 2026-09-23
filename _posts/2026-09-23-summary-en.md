---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
lang: en
---

> From 168 items, 10 important content pieces were selected

---

**Technology News**
1. [OpenAI announces GPT-6 Sol and Luna, drawing heavy Hacker News debate](#item-tech-news-1) ⭐️ 9.0/10
2. [WordPress Patches Unauthenticated Path Traversal With Conditional RCE Risk](#item-tech-news-2) ⭐️ 9.0/10
3. [Claude Opus 5.5 Release Highlights Price Cuts and Output Improvements](#item-tech-news-3) ⭐️ 8.0/10
4. [Pentagon Says AI Overreliance Contributed to Iran School Missile Strike](#item-tech-news-4) ⭐️ 8.0/10
5. [Claude Opus 5.5 and GPT-6 Sol/Luna launch with steep price cuts](#item-tech-news-5) ⭐️ 8.0/10
6. [Complex KDA Extends Kimi Delta Attention Expressivity](#item-tech-news-6) ⭐️ 8.0/10
7. [Visual FoxPro revived with Rust/wasm runtime and vfp9 compatibility](#item-tech-news-7) ⭐️ 7.0/10
8. [Claude Opus 5.5 Max Benchmarks Spark Cost and Reliability Debate](#item-tech-news-8) ⭐️ 7.0/10
9. [QontoFAQ: New Information Retrieval Benchmark for Product FAQs](#item-tech-news-9) ⭐️ 7.0/10

**Technology Blog**
1. [Persona 4 Revival Interview: Modernizing a Classic Without Erasing Its Era](#item-tech-blog-1) ⭐️ 5.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenAI announces GPT-6 Sol and Luna, drawing heavy Hacker News debate](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI has published an announcement for GPT-6 Sol and Luna, a new pair of models whose Hacker News thread reached 1,152 points and 597 comments. The material available for this summary contains no official technical benchmarks, model specifications, or formal pricing documentation, so the release&\#x27;s concrete capabilities remain unverified here. Commenters treated pricing as the headline change, with one noting that GPT-6 Luna costs half as much as GPT-5.6 Luna. Others compared agent-workflow usage limits across competing subscription tiers, including Claude Code 20x versus Codex Pro 20x, and discussed model &quot;personality,&quot; with one long-time agent user saying GPT-5.6 Sol had been a personal sweet spot and worrying that a technically better successor might feel less natural to work with.

hackernews · OfficialTurkey · Sep 22, 18:00 · [Discussion](https://news.ycombinator.com/item?id=49805509)

**「Background」** GPT-6 Sol and Luna are OpenAI&\#x27;s new mainstream frontier models, positioned around different balances of capability and cost. OpenAI released them on September 22, 2026, 19 days after GPT-6 Astra. For developers, one integration detail from the Sol model page affects older code: Chat Completions supports function calling only when reasoning\_effort is set to none.

**「Impact」** Developers running high-volume coding and agent workloads can expect API costs to fall by 50% or more, while ChatGPT Plus users in Work and Codex see wider five-hour usage ranges on Sol and Luna than on the GPT-5.6 models. OpenAI’s published benchmarks are selective, so the price-performance gain may vary by workload.

**「Community Discussion」** Discussion centered on practical economics rather than demonstrated capability: per-token pricing, plan resets, and opaque usage-window math were treated as deciding factors, with one user calling Codex the clear winner on metering because ChatGPT usage is essentially unmetered on the 20x plan. Views on model quality were more personal than consensus-driven, as users debated whether a newer model could reproduce the working &quot;feel&quot; of an earlier one and praised ChatGPT Plus as effectively limitless for general chat, search, light coding, and document review since 5.6.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://www.zdnet.com/innovation/openai-gpt-6-sol-luna-release/">OpenAI &#x27;s GPT - 6 Sol doubles its accuracy rate - for half the... - ZDNET</a></li>
<li><a href="https://www.digitalapplied.com/blog/gpt-6-sol-luna-launch-pricing-benchmarks-2026">GPT - 6 Sol and Luna : API Prices, Benchmarks and Trade-offs</a></li>
<li><a href="https://coursiv.io/blog/gpt-6-sol-luna">GPT-6 Sol and Luna: What&#x27;s New, Pricing, Benchmarks, and Who Should Use Them</a></li>
<li><a href="https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more">OpenAI releases GPT-6 Sol and Luna models, slashing API costs 50% or more | VentureBeat</a></li>
<li><a href="https://runtimewire.com/article/openai-gpt-6-sol-luna-launch">OpenAI launches GPT-6 Sol and Luna with sharply lower API prices</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-6`, `#AI models`, `#LLM release`, `#Hacker News`

---

<a id="item-tech-news-2"></a>
### [WordPress Patches Unauthenticated Path Traversal With Conditional RCE Risk](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) ⭐️ 9.0/10

WordPress has fixed a critical unauthenticated path traversal vulnerability in WordPress core that is reported to lead to conditional remote code execution, according to the project&\#x27;s security advisory GHSA-7hp8-65ch-5whp. The fix is included in WordPress 7.1.2 and, as a courtesy to users on older branches, has been backported to all branches back to 4.7. The advisory is listed under the wordpress-develop repository, and community discussion points to a patch commit and to locate\_template\(\) documentation that warns directory traversal can occur when a user-provided template name is passed without validation. The remote code execution is described as conditional, meaning exploitation depends on prerequisites that the supplied material does not fully specify; concrete technical details of the vulnerable code path are not available in the item text.

hackernews · vntok · Sep 22, 16:33 · [Discussion](https://news.ycombinator.com/item?id=49803959)

**「Background」** WordPress is a very widely deployed open-source content management system whose page-template resolution relies on functions such as locate\_template\(\), which does not by itself prevent directory traversal when a user-supplied template name is passed in. That flaw class allows an attacker to reach files outside the intended theme and /wp-includes locations, and because the resolved file can be a local PHP file, the impact can escalate from local file inclusion to conditional remote code execution rather than guaranteed execution. WordPress 7.1.2, released 22 September 2026, contains the fix, which was backported as a courtesy to all branches still eligible for security fixes—currently down to 4.7—although only the most recent version is actively supported.

**「Impact」** WordPress site operators running affected versions—including the official php Docker image and default cPanel configurations using PHP prior to 8.5—face an unauthenticated path traversal that can lead to conditional remote code execution, so upgrading to 7.1.2 or applying the corresponding backported fix is the necessary mitigation.

**「Community Discussion」** Commenters largely treated the flaw as another reminder of WordPress&\#x27;s broad attack surface and the operational risk that many sites remain on older branches; one commenter estimated that about one-third of installs are not on the recent 7 branch. Others highlighted mitigation experience, including moving a site to static Hugo templates, while a patch-focused comment linked the specific commit and a nine-year-old locate\_template\(\) documentation note that explicitly warned about directory traversal when user-provided template names are not validated.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp">Unauthenticated path traversal in page-template resolution leading to conditional RCE · Advisory · WordPress/wordpress-develop · GitHub</a></li>
<li><a href="https://wordpress.org/news/2026/09/wordpress-7-1-2-release/">WordPress 7.1.2 Release – WordPress News</a></li>
<li><a href="https://patchstack.com/articles/wordpress-7-1-2-security-release-unauthenticated-lfi-to-rce/">WordPress 7.1.2 Security Release: Unauthenticated LFI to RCE - Patchstack</a></li>
<li><a href="https://wordpress.org/documentation/wordpress-version/version-7-1-2/">Version 7 . 1 . 2 – Documentation – WordPress .org</a></li>
<li><a href="https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp">Unauthenticated path traversal in page-template resolution leading to...</a></li>

</ul>
</details>

**Tags**: `#WordPress`, `#security vulnerability`, `#path traversal`, `#remote code execution`, `#open source`

---

<a id="item-tech-news-3"></a>
### [Claude Opus 5.5 Release Highlights Price Cuts and Output Improvements](https://www.anthropic.com/claude-opus-5-5) ⭐️ 8.0/10

Anthropic released Claude Opus 5.5, drawing 1,181 points and 803 comments on Hacker News, with commenters focusing on reported price reductions and improved model output. According to one commenter&\#x27;s price table, Opus 5.5 costs per million tokens $0.20 for cache reads \(down from $0.50\), $4 for input tokens \(down from $5\), $20 for output tokens \(down from $25\), and $5 for cache writes \(down from $6.25\). A commenter also quoted the release stating that Opus 5.5 &quot;communicates more naturally than prior models,&quot; puts important information up front, and is a better work partner over long sessions. The supplied excerpt lacks full technical details such as benchmark scores or architecture changes, and no source content was available for independent verification. Community reaction ranged from praise for output improvements to criticism that the release invokes frontier pacing while shipping major capability and price changes.

hackernews · km144 · Sep 22, 16:29 · [Discussion](https://news.ycombinator.com/item?id=49803892)

**「Background」** Claude Opus is Anthropic&\#x27;s top-tier frontier model line, and the prior Opus 5 generation established the capability and price baseline against which this release is being measured. Opus 5.5 is described as the first model in Anthropic&\#x27;s new Claude 5.5 family, and it arrives shortly after the company publicly called for &quot;pacing the frontier,&quot; a juxtaposition commenters in this thread flagged. The release lowers list pricing to $4 per million input tokens and $20 per million output tokens — 20% below Opus 5 — and Anthropic reports that it outperforms recent Claude models on nearly every measure in a roughly 2,000-scenario automated behavioral audit.

**「Impact」** Developers and organizations running Opus-class workloads through the API will pay less per task, with Opus 5.5 list prices of $4 per million input tokens, $20 per million output tokens and $0.20 per million cache reads, down from Opus 5&\#x27;s $5, $25 and $0.50. The lower pricing does not appear to come with a capability regression: Anthropic is reported to reach parity with GPT-6 Astra on evaluations such as Terminal-Bench 4.0 and AutomationBench-AA while extending its lead in agentic knowledge work.

**「Community Discussion」** Commenters broadly welcomed the price cuts, and one reported a significant improvement when rerunning a 3D pelican animation prompt with Claude 5.5 versus Claude 5. Others were skeptical: one noted that the release&\#x27;s first line recalls Anthropic&\#x27;s call to pace the frontier while the rest demonstrates the opposite, and another said they preferred DeepSeek v4.1 set to high.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://www.unite.ai/anthropic-releases-claude-opus-5-5-with-lower-pricing-and-new-safeguards/">Anthropic Releases Claude Opus 5.5 With Lower Pricing and New ...</a></li>
<li><a href="https://venturebeat.com/technology/anthropic-releases-claude-opus-5-5-beating-fable-5-1-on-key-agentic-benchmarks-at-60-cheaper-api-price">Anthropic releases Claude Opus 5.5, beating Fable 5.1 on key ...</a></li>
<li><a href="https://artificialanalysis.ai/articles/claude-opus-5-5">Claude Opus 5 . 5 takes the top spot on the Artificial... | Artificial Analysis</a></li>
<li><a href="https://www.ibtimes.co.uk/anthropic-claude-opus-5-5-price-cut-safety-1821320">Anthropic Calls Claude Opus 5 . 5 &#x27;Strongest-Performing Model We&#x27;ve...</a></li>
<li><a href="https://claude.com/blog/what-a-task-costs-on-opus-5-5">What a task costs on Opus 5 . 5 | Claude by Anthropic</a></li>

</ul>
</details>

**Tags**: `#Claude`, `#Anthropic`, `#LLM`, `#AI models`, `#pricing`

---

<a id="item-tech-news-4"></a>
### [Pentagon Says AI Overreliance Contributed to Iran School Missile Strike](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 8.0/10

A Pentagon report says overreliance on AI contributed to a missile strike on a school in Iran. Quoted passages from the report in the discussion say the U.S. &\#x27;failed in its obligation to do everything feasible to verify&\#x27; that the school was a military objective and that the failure &\#x27;went beyond mere negligence,&\#x27; adding that the U.S. directed strikes at the school building while aware of a substantial risk of striking a civilian object and acting recklessly. Commenters also cite the Minab site, which was cataloged as an Islamic Revolutionary Guard Corps facility due to outdated data, fed into Maven with other candidates, and recommended as a day-one target, compressing target-list work that once took hours into minutes. The episode has renewed scrutiny of military AI validation, automation bias, and accountability for civilian casualties.

hackernews · devonnull · Sep 22, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49806430)

**「Background」** The strike at issue hit a girls&\#x27; school in Minab, Iran, and Pentagon investigators reportedly traced it to a cascade of preventable failures that included overreliance on an AI tool built by Palantir, along with staff cuts and rushed targeting procedures; some personnel knew within hours that the school had been hit. That tool sits inside the U.S. military&\#x27;s machine-learning targeting workflow, where algorithms surface imagery-derived candidates and compress target-list work that once took hours into minutes. The report&\#x27;s central technical concern is automation bias — operators&\#x27; tendency to defer to algorithmic recommendations — a recognized risk in military AI because human review can become perfunctory when recommendations arrive fast and appear authoritative.

**「Impact」** The Pentagon finding is likely to intensify scrutiny of the Maven targeting pipeline and of how military AI recommendations are validated and overseen, since the strike exposed how outdated, human-curated data flowed into an AI-generated day-one target list. Attribution remains contested, however: former military officials have said humans rather than AI were to blame for the school strike, and reporting accounts differ on the death toll.

**「Community discussion」** Commenters disagreed about whether AI was the main culprit, with one arguing the report&\#x27;s language points to recklessness and verification failures rather than the system, and another defending the campaign&\#x27;s overall target accuracy and noting the school was wrapped by an L-shaped military complex. Concerns about accountability and process dominated, including a question about who will face consequences, criticism that compressing target-list work from hours to minutes optimizes the wrong metric, and a cited separate incident in which AI incorrectly flagged a Chinese boat as carrying nuclear weapons materiel.

<details><summary>References</summary>
<ul>
<li><a href="https://gizmodo.com/pentagon-investigators-say-overreliance-on-palantir-ai-tech-contributed-to-u-s-strike-that-killed-123-iranian-children-2000814477">Pentagon Investigators Say Overreliance on Palantir AI Tech...</a></li>
<li><a href="https://www.rt.com/news/646000-overreliance-on-ai-contributed-to/">US overreliance on AI contributed to deadly Iran school strike ...</a></li>
<li><a href="https://www.yahoo.com/news/us/articles/pentagon-review-links-ai-targeting-172754307.html">Pentagon Review Links AI Targeting System to Strike That Killed 120 Iranian Children</a></li>
<li><a href="https://www.militarytimes.com/news/your-military/2026/03/24/deadly-iran-school-strike-casts-shadow-over-pentagons-ai-targeting-push/">Deadly Iran school strike casts shadow over Pentagon’s AI targeting push</a></li>
<li><a href="https://www.reddit.com/r/worldnews/comments/1wko4v6/pentagon_investigators_have_discovered_that/">r/worldnews on Reddit: Pentagon investigators have discovered that flawed intelligence and an overreliance on AI contributed to a missile strike that killed 123 Iranian school children</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#military AI`, `#autonomous weapons`, `#AI policy`, `#automation bias`

---

<a id="item-tech-news-5"></a>
### [Claude Opus 5.5 and GPT-6 Sol/Luna launch with steep price cuts](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 8.0/10

Simon Willison reports that Anthropic released Claude Opus 5.5 and, roughly an hour later, OpenAI released GPT-6 Sol and GPT-6 Luna, following the prior day&\#x27;s Grok 4.7 and MiMo v2.6 Flash/Pro launches; the post is a set of early first impressions rather than a deep evaluation. OpenAI halved its prices: GPT-6 Luna costs $0.10/M input, $0.01/M cached input and $0.50/M output versus GPT-5.6 Luna&\#x27;s $0.20/$0.02/$1.20, and GPT-6 Sol costs $2/$0.20/$10 versus GPT-5.6 Sol&\#x27;s $4/$0.40/$20 — with the comparison against GPT-5.6&\#x27;s promotional pricing, since GPT-5.6 has a scheduled 25% price increase in November. Claude Opus 5.5 cut prices 20% to $4/M input and $20/M output from the $5/$25 shared by Opus 4.5 through 5, with cache-read pricing down 60%, which matters for long agentic conversations where over 90% of input tokens are billed at cached rates; Anthropic says Sonnet 5.5 and Haiku 5.5 are coming soon. At $0.10/$0.50, GPT-6 Luna is one of OpenAI&\#x27;s cheapest releases, beaten only by GPT-4.1 Nano \($0.10/$0.40, April 2025\) and GPT-5 Nano \($0.05/$0.40, August 2025\), while the price war currently affects tiers below the $10/M input and $50/M output level still occupied by GPT-6 Astra and Claude Fable 5.1. In Willison&\#x27;s pelican SVG test, Claude Opus 5.5 at &quot;max&quot; thinking failed to return a response twice, exhausting its 128,000 maximum output token limit while still reasoning, each attempt costing about $2.56 and nearly 20 minutes, which left him suspecting &quot;max&quot; is effectively useless and noting Opus 5.5 has also been positioned as better at communication style and at Blender.

rss · Simon Willison · Sep 22, 23:46

**「Background」** Frontier labs now ship flagship models on overlapping, fast cadences: Anthropic released Claude Opus 5.5 on 22 September 2026, about two months after Opus 5 \(24 July 2026\), and OpenAI followed roughly an hour later with GPT-6 Sol and Luna, cutting API prices by half versus the GPT-5.6 versions. API pricing in this tier is quoted per million tokens split into input, cached input, and output, and vendors position models in families by cost and capability — Anthropic&\#x27;s Opus and Fable at the high end with Sonnet and Haiku below, and OpenAI&\#x27;s Sol, Terra, Astra, and Luna across the range. Cached input pricing matters disproportionately for long agentic conversations, where most input tokens are billed at the cached rate, so reductions there can outweigh headline drops.

**「Impact」** Developers building on Luna-class models get frontier-adjacent capability at half the previous cost — GPT-6 Luna at $0.10/$0.50 per million tokens versus GPT-5.6 Luna&\#x27;s $0.20/$1.20 — while Claude users running long agentic sessions gain a 60% reduction in cache-read pricing. Early testing also suggests Anthropic&\#x27;s new &quot;max&quot; thinking level can over-reason past the 128,000-token output limit and return no response at all, at roughly $2.56 per failed attempt.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://codersera.com/blog/claude-opus-5-5-complete-guide-2026/">Claude Opus 5.5: Specs, Pricing &amp; Benchmarks (2026)</a></li>
<li><a href="https://thenewstack.io/openai-gpt-6-sol-luna-release/">OpenAI releases GPT-6 Sol and Luna — and cuts token prices in half - The New Stack</a></li>
<li><a href="https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more">OpenAI releases GPT-6 Sol and Luna models, slashing API costs 50% or more | VentureBeat</a></li>
<li><a href="https://thenextweb.com/news/openai-gpt-6-sol-luna-api-price-cut">OpenAI cuts GPT-6 prices in half with Sol and Luna</a></li>

</ul>
</details>

**Tags**: `#AI models`, `#Claude Opus`, `#GPT-6`, `#LLM pricing`, `#model releases`

---

<a id="item-tech-news-6"></a>
### [Complex KDA Extends Kimi Delta Attention Expressivity](https://www.reddit.com/r/MachineLearning/comments/1wn5uv9/understanding_and_enhancing_kimi_delta_attention_r/) ⭐️ 8.0/10

A Reddit r/MachineLearning post by /u/Yossarian\_1234 summarizes the paper Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention, which analyzes expressivity differences between Gated DeltaNet \(GDN\) and Kimi Delta Attention \(KDA\). The work shows that KDA&\#x27;s full diagonal gate can act as a reflection enabling 2D rotations in a single step, but only when the gate range is extended to \[-1,1\] and the delta-rule learning rate is extended to \[0,2\], a variant called Complex KDA \(CKDA\). The theory claims CKDA can express any orthogonal diagonal-plus-rank-one matrix and track the S3, S4, and A5 groups, but not S5. Experiments report that CKDA can learn S3 and S4, shows promising audio-continuation results, and trains stably while remaining competitive with standard KDA on language modeling. The post presents these results as promising rather than conclusively groundbreaking, based on a Reddit TLDR summary of the paper.

reddit · r/MachineLearning · /u/Yossarian\_1234 · Sep 22, 10:34

**「Background」** Linear attention aims for O\(T\) efficiency by compressing context into a fixed-size recurrent state rather than a growing KV cache, but it has historically lagged full attention on recall and copying tasks. Gated DeltaNet combines the delta rule — an error-correcting state update — with gating, and Kimi Delta Attention \(KDA\), introduced in the Kimi Linear architecture in October 2025, extends it with finer-grained channel-wise diagonal gating so limited finite-state memory is used more effectively. Prior analysis showed KDA can realize 2D rotations by combining a single delta-rule transformation with a second reflection supplied by its channel-wise gate, which is the foundation the Complex KDA work builds on.

**「Impact」** For researchers and developers building on Kimi Delta Attention, extending gate values to \[-1,1\] and the delta-rule coefficient β to \[0,2\] enables Complex KDA to realize 2D rotations in a single delta-rule transition, lifting its expressivity to orthogonal diagonal-plus-rank-one matrices and S3, S4, and A5 group tracking \(though not S5\) while remaining trainable and competitive with standard KDA on language modeling. Those gains are currently demonstrated on group-tracking, audio-continuation, and language-modeling experiments rather than conclusively established at larger scale.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://github.com/hwilner/kimi-delta-attention">GitHub - hwilner/kimi-delta-attention: Educational ...</a></li>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention ... Kimi Linear: An Expressive, Efficient Attention Architecture Linear Attention: Kimi Delta Attention | Jianyu Huang kimi-delta-attention/docs/ARCHITECTURE.md at main · hwilner ... Linear Attention, From Scratch to Kimi 3 (Kimi Delta Attention) Kimi Delta Attention: Delta‐Rule Linear Mechanism</a></li>
<li><a href="https://arxiv.org/abs/2609.24797">[2609.24797] Complex KDA: Understanding and Enhancing the ...</a></li>
<li><a href="https://aiweekly.co/alerts/complex-kda-lifts-kimi-delta-attentions-expressivity-ceiling">Complex KDA lifts Kimi Delta Attention&#x27;s expressivity ceiling</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#attention mechanisms`, `#linear attention`, `#expressivity theory`, `#sequence modeling`

---

<a id="item-tech-news-7"></a>
### [Visual FoxPro revived with Rust/wasm runtime and vfp9 compatibility](https://foxscript.org/) ⭐️ 7.0/10

A project at foxscript.org has revived Visual FoxPro with a new runtime written in Rust and compiled to WebAssembly, checked for compatibility against the real vfp9.exe. Although Microsoft stopped Visual FoxPro at version 9 in 2007, the project targets organizations that still rely on 32-bit FoxPro business applications and want to keep them running. It removes the 2 GB table limit, continues to load old 32-bit .fll add-ins, and adds lambdas, JSON support, and an HTTP server. The project is MIT-licensed, but its reports are not done and its builds are unsigned. The source says customer demand motivated the effort.

hackernews · boredjohnny · Sep 22, 21:00 · [Discussion](https://news.ycombinator.com/item?id=49808023)

**「Background」** Visual FoxPro was Microsoft&\#x27;s COM-based database management and application development system; its final version 9.0 shipped in December 2004 and received the SP2 patch in October 2007, after which Microsoft discontinued the product without producing a .NET successor. Long after end-of-life, many organizations still run mission-critical accounting, inventory management, production tracking, and internal reporting applications on Visual FoxPro. This legacy persistence is the context for a project that reimplements the FoxPro language on a new Rust/WebAssembly runtime while aiming for compatibility with the real vfp9.exe.

**「Impact」** Organizations maintaining Visual FoxPro systems could get a path to extend legacy applications on a modern Rust/wasm runtime, though the project&\#x27;s incomplete reports and unsigned builds limit immediate production use.

**「Community discussion」** Commenters raised a major security concern: Database Container files require read/write access for all users and store executable FoxPro stored procedures as plain text, allowing an attacker with technical knowledge to modify triggers and potentially run Win32 calls through the FoxPro runtime. Others shared mixed experiences with FoxPro deployments, including file-locking and record-contention problems on network drives, a migration to .NET client/server architecture, and nostalgia for how quickly CRUD business applications could be built and sold.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Visual_FoxPro">Visual FoxPro - Wikipedia</a></li>
<li><a href="https://intersoftassociates.com/articles/legacy-systems/foxpro-and-end-of-life-migrations/">FoxPro Replacement and End of Life Migrations | Intersoft ...</a></li>
<li><a href="https://4devnet.com/legacy-foxpro-systems-on-modern-windows-what-companies-must-know/">Visual FoxPro on Windows 11: Risks, Compatibility &amp; Migration</a></li>

</ul>
</details>

**Tags**: `#Visual FoxPro`, `#legacy software`, `#language runtime`, `#WebAssembly`, `#Rust`

---

<a id="item-tech-news-8"></a>
### [Claude Opus 5.5 Max Benchmarks Spark Cost and Reliability Debate](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 7.0/10

The Hacker News discussion centers on Artificial Analysis&\#x27;s benchmark page for Claude Opus 5.5 under its &\#x27;max&\#x27; reasoning setting, with separate pages also available for &\#x27;xhigh&\#x27; and &\#x27;medium&\#x27; \(the default\). Commenters highlight that max effort reportedly costs about half as much per task as Opus 5 when comparing high effort to high effort, while one user reported failing twice to generate an SVG of a pelican on a bicycle because the model exhausted its 128,000-token budget while still reasoning. The thread also raises concerns about evaluation stability and whether benchmark results are re-run after launch, including an anecdotal internal evaluation where Sol&\#x27;s performance regressed to match Luna&\#x27;s. Some participants argue that frontier models are only slightly better than open-weight alternatives while costing around 100x as much, questioning the business case for the most expensive models.

hackernews · theanonymousone · Sep 22, 16:51 · [Discussion](https://news.ycombinator.com/item?id=49804316)

**「Background」** Artificial Analysis is a third-party site that publishes comparative model metrics — including quality/intelligence indices, price per million tokens, output speed, time to first token, and context window — so readers can weigh capability against cost rather than rely on a single benchmark score. Anthropic&\#x27;s Claude Opus 5.5 is positioned as its flagship model for demanding reasoning, coding, and long-horizon agentic work, and it uses adaptive reasoning with selectable effort levels, where medium is the default and higher settings such as max spend more reasoning tokens. Because results, latency, and price differ by effort setting, benchmark pages are published separately per setting, which is why the item points to distinct max, xhigh, and medium pages.

**「Impact」** For developers choosing the max reasoning setting, the discussion frames the trade-off concretely: roughly half the cost per task versus Opus 5 at equivalent high effort, according to one commenter, weighed against reported runs where the 128,000-token budget was exhausted before a task finished. Anthropic&\#x27;s own launch material claims about 40% lower cost per task, so whether that advantage survives independent re-runs of these benchmarks is the practical question for teams budgeting reasoning-token spend.

**「Community Discussion」** There is no consensus on the significance of the reported cost and performance figures: some commenters found the halving of per-task cost versus Opus 5 notable, while others focused on practical failures like the 128,000-token budget exhaustion or argued the price gap with open-weight models is unjustified. Several users also expressed concern that launch-time benchmark results may not be re-run or may regress, citing one anecdotal internal evaluation as a counterexample to stable model performance.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/claude-opus-5-5">Claude Opus 5 . 5 ( max with fallback) - Intelligence... | Artificial Analysis</a></li>
<li><a href="https://kingy.ai/blog/claude-opus-5-5-specs-benchmarks-pricing-comparison/">Claude Opus 5 . 5 : Specs, Benchmarks , Pricing and How It... - Kingy AI</a></li>
<li><a href="https://kilo.ai/models/anthropic-claude-opus-5-5">Anthropic: Claude Opus 5 . 5 Coding Benchmark | Kilo Code</a></li>
<li><a href="https://mashable.com/tech/claude-opus-launch-promises-better-performance-cheaper-price">Anthropic launches Claude Opus 5.5: Benchmarks, pricing, safety | Mashable</a></li>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5.5 \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#LLM benchmarks`, `#AI model pricing`, `#reasoning models`, `#Claude Opus`

---

<a id="item-tech-news-9"></a>
### [QontoFAQ: New Information Retrieval Benchmark for Product FAQs](https://www.reddit.com/r/MachineLearning/comments/1wn9xqk/qontofaq_a_better_information_retrieval_benchmark/) ⭐️ 7.0/10

A Reddit post by /u/espadrine introduces QontoFAQ, a new information retrieval benchmark and metric for evaluating embedding models on product FAQ retrieval. The author says existing retrieval benchmarks can feel &quot;benchmaxxed&quot; by models, so the goal was to tie evaluation closely to finding the article that answers a product question correctly. The post links to a Medium article describing the approach and to the associated GitHub repository, qonto/qonto-faq-benchmark. The post claims the new metric is more proportional to document relevance and that a benchmarking dataset was built to measure embedding models. However, the supplied post only summarizes the work and provides links, so methodology, results, and independent validation are not available for assessing the benchmark&\#x27;s significance.

reddit · r/MachineLearning · /u/espadrine · Sep 22, 13:45

**「Background」** Information retrieval \(IR\) benchmarks are standard datasets and scoring procedures used to compare systems — increasingly embedding models — on how well they surface the document that actually answers a query. A recurring concern among practitioners is that widely used benchmarks can become &quot;benchmaxxed,&quot; with models tuned to score well on the test set rather than to solve real retrieval tasks. QontoFAQ responds to that concern by pairing a new metric intended to be more proportional to document relevance with a dataset aimed at product FAQ retrieval, released alongside the linked article as the public GitHub repository qonto/qonto-faq-benchmark.

**「Impact」** ML and information-retrieval practitioners now have a publicly released benchmark, dataset, and relevance metric from Qonto for evaluating embedding models specifically on product FAQ retrieval, published alongside open-source code. Because the announcement provides no methodology, results, or independent validation, the benchmark&\#x27;s actual usefulness relative to existing retrieval benchmarks remains unverified.

<details><summary>References</summary>
<ul>
<li><a href="https://trendshift.io/repositories/253658">qonto / qonto -faq- benchmark — GitHub trending stats... | Trendshift</a></li>

</ul>
</details>

**Tags**: `#Information Retrieval`, `#Benchmarking`, `#Embedding Models`, `#Evaluation Metrics`, `#Datasets`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Persona 4 Revival Interview: Modernizing a Classic Without Erasing Its Era](https://www.gcores.com/articles/220050) ⭐️ 5.0/10

rss · 机核GCORES游戏资讯 · Sep 22, 14:27

**「Background」** At TGS, the author played Persona 4 Revival&\#x27;s prologue demo—April 18–20 in Inaba, including COOP scenes and Yukiko&\#x27;s Castle—and interviewed producer Wada and director Yajima. The question was what “Revival” should mean beyond better graphics.

**「Solution」** The most visible change is full 3D: fixed-camera backgrounds become freely explorable spaces, so the team rebuilt areas players never saw, from the shopping district to the riverbank and Junes, while preserving Inaba&\#x27;s faded mood. Combat keeps weakness hits, knockdowns, and All-Out Attacks, but adds ailment spreading: attacking a status-affected enemy knocks it back and passes the ailment to others. Because ailments raise critical-hit odds, the developers say this links normal attacks, ailments, crits, and All-Out Attacks without extra resource cost. Fusion remains two-person and special fusion, but forecasts were reworked, Persona 5 Royal-style traits were added, and new Personas are promised. Prime Time uses a gauge for free consecutive actions and handoffs; Yajima says balance was rebuilt with these systems from the start, so bosses should not become trivial, though skilled use still gives clear advantages. Wada says Prime Time lets players use learned skills freely instead of hoarding SP. Dialogue modernization is limited to text and lines—not script or main story—and Yosuke stays himself. Some scenes were remade in real-time or by MAPPA animation, chosen by story importance. The team also kept flip phones and CRT-era details as Heisei retro.

**「Takeaway」** The author concludes that “Revival” means not simply modern presentation but reconnecting old systems into new combat axes while preserving the period texture that made Persona 4 distinctive.

**Tags**: `#Persona 4 Revival`, `#game remake design`, `#battle system design`, `#3D reconstruction`, `#developer interview`

---