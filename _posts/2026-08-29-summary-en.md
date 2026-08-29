---
layout: default
title: "Horizon Summary: 2026-08-29 (EN)"
date: 2026-08-29
lang: en
---

> From 144 items, 14 important content pieces were selected

---

**Technology News**
1. [Z.ai releases open-weight GLM-5.3 with strong reasoning](#item-tech-news-1) ⭐️ 9.0/10
2. [Htmx 4.0.0 Released with Alpine Compatibility and Hypermedia Features](#item-tech-news-2) ⭐️ 8.0/10
3. [OpenAI Cuts Off Cursor After SpaceX Acquisition](#item-tech-news-3) ⭐️ 8.0/10
4. [AI turns bug rumors into exploits, overwhelming maintainers](#item-tech-news-4) ⭐️ 8.0/10
5. [Tiny Latent Flow Transformer Generates 128x128 Faces on RP2350](#item-tech-news-5) ⭐️ 8.0/10
6. [US sanctions label hosting collective Autistici/Inventati as terrorist](#item-tech-news-6) ⭐️ 7.0/10
7. [OpenAI Python SDK Migrates to HTTPX2](#item-tech-news-7) ⭐️ 7.0/10
8. [Berlin Mayor Says City Will Not Cave to Hackers&\#x27; Ransom](#item-tech-news-8) ⭐️ 7.0/10
9. [US datacentre backlash grows as states weigh bans](#item-tech-news-9) ⭐️ 7.0/10

**Technology Blog**
1. [Exterminauts Preview: Co-op PVE, Mod Builds, and Blue-Collar Bosses](#item-tech-blog-1) ⭐️ 4.0/10

**Financial News**
1. [Corn and wheat futures hit three-year highs on supply concerns](#item-finance-news-1) ⭐️ 8.0/10
2. [U.S. appeals court rules sports prediction contracts are sports bets, not CFTC-regulated swaps](#item-finance-news-2) ⭐️ 8.0/10
3. [Rate-Hike Odds for September Rise After Warsh Speech](#item-finance-news-3) ⭐️ 8.0/10
4. [Premarket movers: PayPal drops on scrapped buyout, Affirm and Gap gain on earnings](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Z.ai releases open-weight GLM-5.3 with strong reasoning](https://huggingface.co/zai-org/GLM-5.3) ⭐️ 9.0/10

Z.ai has released GLM-5.3 as an open-weight model, generating significant interest among practitioners. Early user reports describe it as a sweet spot beyond DeepSeek Flash models, with strong reasoning and intuition on hard problems, and compare it favorably to Opus 4.8. It is said to be slightly behind Kimi in ability but much easier to run, with expectations of noticeably better third-party pricing and speed. Users highlight an improved tokens-vs-accuracy ratio compared to earlier Chinese models like Qwen3.8 and GLM 5.2, reducing excessive thinking in complex data analysis tasks. The release follows Z.ai&\#x27;s announcement via Twitter and a blog post, though specific technical details remain limited.

hackernews · jeudesprits · Aug 28, 15:20 · [Discussion](https://news.ycombinator.com/item?id=49479878)

**「Background」** GLM-5.3 is the latest open-weight large language model from Z.ai, the lab behind the GLM series. It is built on the same base model as GLM-5.2, with improvements coming from post-training rather than architectural changes. Z.ai reports that GLM-5.3 is its most capable open-weights model for coding, achieving a 50% gain over GLM-5.2 on its in-house Code Bench and posting open-source state-of-the-art results on Terminal Bench 3.0 and Agents&\#x27; Last Exam. The model weights are available on Hugging Face under zai-org/GLM-5.3.

**「Impact」** Early user reports point to GLM-5.3 as a stronger cost-performance choice for open-weight deployments: it is easier to run than Kimi and produces fewer output tokens than earlier Chinese models on complex data-analysis workloads, which should lower inference costs for developers and third-party providers. Those seeking the highest-end local performance may need large unified memory systems, as one user noted while anticipating a 512 GB Mac M5 Ultra.

**「Community discussion」** Commenters are largely impressed with GLM-5.3&\#x27;s reasoning ability and intuition, with one noting it handles hard problems that DeepSeek Flash lacks intuition for, while another says it feels like Opus 4.8. They also note it is less restrictive on sensitive topics than US models, and although it is slightly behind Kimi in ability, its operational advantages and token efficiency make it attractive. No major disagreement emerges, though one user cautions that it is still nowhere near a Fable-class model.

<details><summary>References</summary>
<ul>
<li><a href="https://kie.ai/blog/what-is-glm-5-3">What Is GLM - 5 . 3 ? Z . ai &#x27;s Next Open - Weight Model</a></li>
<li><a href="https://glm-ai.chat/models/glm-5-3/">GLM - 5 . 3 : Specs , API, Pricing and Benchmarks</a></li>
<li><a href="https://neomanex.com/models/glm-5-3">GLM - 5 . 3 | AI Model Review | Neomanex</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open-weights`, `#AI`, `#GLM-5.3`, `#model-release`

---

<a id="item-tech-news-2"></a>
### [Htmx 4.0.0 Released with Alpine Compatibility and Hypermedia Features](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) ⭐️ 8.0/10

Htmx 4.0.0 was released on August 28, 2026, as a major version of the hypermedia-focused JavaScript library. The announcement highlights new features including \`hx-alpine-compat\`, which smooths over compatibility issues between htmx and Alpine.js. The release is significant because htmx remains widely adopted among developers who prefer server-side rendering and simplicity in web UIs. Community response includes enthusiasm from existing users and some contrasting experiences from frontend developers accustomed to API-plus-SPA stacks.

hackernews · rmsaksida · Aug 28, 13:28 · [Discussion](https://news.ycombinator.com/item?id=49478178)

**「Background」** htmx is a small JavaScript library for building interactive web interfaces by issuing AJAX requests directly from HTML attributes, which encourages server-side rendering and hypermedia-driven development. The 4.0 release is a major overhaul that rebuilds htmx&\#x27;s internals around the Fetch API, based on lessons from the fixi.js experiment and five years of supporting the library. According to the official announcement, htmx 2.x codebases can be migrated to 4.x using the provided upgrade guide. During its development, htmx 4.0 was only available as an alpha, with the stable release targeted for early-to-mid 2026 and the latest npm tag remaining on 2.x until early 2027.

**「Impact」** Developers using htmx alongside Alpine.js now have a dedicated compatibility attribute, \`hx-alpine-compat\`, to address integration issues in the 4.0 release.

**「Community Discussion」** Commenters largely welcomed 4.0, with one praising the joy of Go + htmx + SQLite and another identifying as HTMX CEO noting they are excited to try the new version. A .NET/Angular developer offered a contrarian view that htmx requires mixing presentation concerns with backend logic, while another commenter preferred the smaller alpine-ajax library after testing htmx 4.

<details><summary>References</summary>
<ul>
<li><a href="https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released">htmx 4 . 0 . 0 has been released ! ~ htmx</a></li>
<li><a href="https://medium.com/django-journal/htmx-4-0-alpha-in-django-fetch-api-superpowers-for-real-time-uis-early-benchmarks-vs-htmx-2-x-2b68407a22cc">HTMX 4 . 0 Alpha in Django: Fetch API Superpowers for... | Medium</a></li>
<li><a href="https://web.archive.org/web/20251103222343/https://htmx.org/essays/the-fetchening/">htmx ~ The fetch() ening</a></li>

</ul>
</details>

**Tags**: `#htmx`, `#web-development`, `#hypermedia`, `#javascript`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [OpenAI Cuts Off Cursor After SpaceX Acquisition](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 8.0/10

OpenAI is cutting off Cursor&\#x27;s access to its models following SpaceX&\#x27;s acquisition of the AI coding tool, a strategic move in the intensifying competition among frontier AI labs. The decision means Cursor users will no longer be able to use OpenAI models inside Cursor, which has relied on reselling third-party APIs. Commentators note that Cursor&\#x27;s business model as an API reseller was already under pressure, and that Anthropic previously banned xAI for similar terms-of-service violations. The move could push some developers toward Anthropic or xAI&\#x27;s Grok model, but the full impact on Cursor&\#x27;s user base remains unclear.

hackernews · meetpateltech · Aug 29, 01:47 · [Discussion](https://news.ycombinator.com/item?id=49486172)

**「Background」** Cursor is an AI-powered coding tool developed by Anysphere, which SpaceX acquired for $60 billion after Microsoft explored and passed on an acquisition, while OpenAI reportedly approached Cursor twice but Cursor chose independence. The acquisition supplies additional compute capacity to Cursor while giving SpaceX an established coding product to integrate with Grok. OpenAI announced it intends to wind down its contract providing OpenAI models to Cursor, with a proposed shutoff date of November 12, 2026.

**「Impact」** Cursor users who relied on OpenAI models will lose that access, and some commentators say they will shift to Anthropic or rely on Grok through Cursor.

**「Community Discussion」** Commenters largely see the move as expected, citing Cursor&\#x27;s API-reselling business model and its acquisition by a Musk-affiliated company, with references to Anthropic&\#x27;s earlier ban on xAI. There is practical speculation about whether Anthropic will also ban Cursor, and users are weighing alternatives like switching to Anthropic or staying with Grok within Cursor.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/aamir-shah-728295148_elonmusk-spacex-cursor-activity-7472656157015298048-g84O">SpaceX Acquires Anysphere&#x27;s Cursor for $60B | Aamir... | LinkedIn</a></li>
<li><a href="https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/">Our decision on Cursor following its acquisition by SpaceX | OpenAI</a></li>
<li><a href="https://politicalos.io/story/spacex-cursor-acquisition">SpaceX Acquisition of Cursor — PoliticalOS | PoliticalOS</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Cursor`, `#AI models`, `#SpaceX`, `#model access`

---

<a id="item-tech-news-4"></a>
### [AI turns bug rumors into exploits, overwhelming maintainers](https://anil.recoil.org/notes/rumour-is-the-exploit) ⭐️ 8.0/10

The piece argues that AI and LLMs are dramatically lowering the barrier between a mere bug rumor and a working exploit, reshaping vulnerability response. Open source maintainers are feeling the brunt: rclone&\#x27;s maintainer reports roughly 20 security disclosures in the project&\#x27;s first 10 years but over 40 in the last month alone, with about 75% containing something worth investigating. The surge is consuming maintainer time even with AI-assisted triage, while commenters note that LLM-driven tooling has also democratized mass exploitation of low-value targets. The trend highlights a widening gap between exploit discovery speed and the practical capacity to patch, test, and deploy fixes.

hackernews · avsm · Aug 28, 15:58 · [Discussion](https://news.ycombinator.com/item?id=49480466)

**「Background」** Traditionally, crafting an exploit required deep expertise and often relied on details visible in patches, commit messages, or other technical clues. The author argues that AI and LLMs now enable even a vague bug rumor or an overheard remark to be quickly turned into working exploit code, dramatically shortening the time from disclosure to exploitation and weakening traditional security embargoes. This is reflected in real-world reports from maintainers such as rclone, which received roughly 20 security disclosures in its first decade but over 40 in the past month alone.

**「Impact」** Open source maintainers and security teams face a 40-fold increase in security disclosures and a heavy triage burden, even with AI assistance, while users face heightened risk because most organizations cannot update software within the short window between a bug rumor and a working exploit.

**「Community discussion」** Commenters agree the scale is new even if the technique is old, with one noting that exploiting patch diffs and commit messages predates LLMs but is now democratized to mass low-value attacks. Others emphasize deployment and supply-chain risks, arguing that automatic updates are dangerous and most CI pipelines take longer than 10 minutes, while one commenter adds that AI can detect silent bug fixes in routine commits.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49480466">Just the rumour of a bug is enough to find an exploit these days | Hacker News</a></li>
<li><a href="https://anil.recoil.org/notes/rumour-is-the-exploit">Just a rumour of a bug is enough to find a security exploit ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI`, `#open source`, `#vulnerabilities`, `#software engineering`

---

<a id="item-tech-news-5"></a>
### [Tiny Latent Flow Transformer Generates 128x128 Faces on RP2350](https://www.reddit.com/r/MachineLearning/comments/1w10tax/i_implemented_a_very_tiny_image_generation_model/) ⭐️ 8.0/10

A developer implemented a 2.4–4 million parameter latent flow transformer image generation model on an RP2350 microcontroller, generating 128x128 face images in about 20 seconds. The model is quantized to int8, uses 12 layers with AdaLN-Zero conditioning, and supports classifier-free guidance \(CFG\), which significantly improved image quality. The inference engine streams weights from flash via DMA while computing the previous layer, and uses ReLU² activation to increase sparsity so it can skip calculations. This demonstrates that sophisticated generative models can run on low-power embedded devices with careful optimization.

reddit · r/MachineLearning · /u/cpldcpu · Aug 28, 19:48

**「Background」** The RP2350 is Raspberry Pi&\#x27;s microcontroller that succeeds the RP2040, adding dual Arm Cortex-M33 cores, optional RISC-V cores, and 520 KB of on-chip SRAM while supporting higher clock speeds and double the flash memory of the previous design. Because microcontrollers have far less memory and compute power than typical ML hardware, running a neural network on them requires aggressive compression techniques such as int8 quantization, DMA-based weight streaming, and skipping sparse activation computations.

**「Impact」** The approach provides a concrete path for on-device generative image models in RP2350-class microcontrollers, showing that sub-5M parameter transformers with int8 quantization and sparse activation can deliver practical results in embedded systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RP2350">RP2350 - Wikipedia</a></li>
<li><a href="https://www.sparkfun.com/rp2350">RP2350 - The latest microcontroller from Raspberry Pi - SparkFun Electronics</a></li>

</ul>
</details>

**Tags**: `#embedded-ml`, `#image-generation`, `#efficient-inference`, `#microcontroller`, `#quantization`

---

<a id="item-tech-news-6"></a>
### [US sanctions label hosting collective Autistici/Inventati as terrorist](https://www.inventati.org/) ⭐️ 7.0/10

The U.S. government has designated the Italian hosting collective Autistici/Inventati \(A/I\) as a &\#x27;global terrorist&\#x27; under sanctions, targeting the group that runs the privacy-focused noblogs.org platform. The move is unprecedented, commenters say, because it sanctions infrastructure providers rather than individuals or violent groups. A/I has long hosted activist and anarchist projects, including work connected to the Genoa G8 protests, and the designation follows claims of PKK links that commenters say are hard to verify. Because A/I provides infrastructure used by open-source and decentralized communities, the sanctions raise concerns for any project that could be targeted for merely hosting controversial groups.

hackernews · exiguus · Aug 28, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49477854)

**「Background」** Autistici/Inventati \(A/I Collective\) is a 25-year-old Italian hosting collective and privacy advocacy group that runs the noblogs.org blogging platform and provides roughly 16,000 mailboxes and 1,500 websites. On August 26, 2026, the U.S. State Department and Treasury designated the collective as a Specially Designated Global Terrorist \(SDGT\) under Executive Order 13224, claiming it builds digital infrastructure for far-left militants; a wind-down period is authorized only through September 25, 2026. The designation is notable because it targets an infrastructure provider rather than individuals and bypasses Italian courts and the EU&\#x27;s intermediary-liability process.

**「Impact」** The immediate practical effect is that noblogs.org is partly dysfunctional and autistici.org is down, leaving users of the collective&\#x27;s privacy-focused blogging and email services without reliable access.

**「Community Discussion」** Commenters largely worry that designating an infrastructure provider as a terrorist is unprecedented and could set a dangerous precedent for networks like I2P, Monero, Veilid, Tox, and Signal. Others question the evidence, saying third-party links between A/I and the PKK are hard to find, while some are confused about what the collective actually does.

<details><summary>References</summary>
<ul>
<li><a href="https://www.state.gov/releases/office-of-the-spokesperson/2026/08/designation-of-autistici-inventati-as-a-specially-designated-global-terrorist/">Designation of Autistici/Inventati as a Specially Designated ...</a></li>
<li><a href="https://cryptobriefing.com/us-sanctions-autistici-inventati-terrorism/">United States sanctions Autistici/Inventati for supporting ...</a></li>
<li><a href="https://peopleofinternet.com/articles/washington-s-terrorism-sanctions-on-an-italian-hosting.html">Washington&#x27;s Terrorism Sanctions on an Italian Hosting ...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#open source`, `#internet infrastructure`, `#sanctions`, `#decentralization`

---

<a id="item-tech-news-7"></a>
### [OpenAI Python SDK Migrates to HTTPX2](https://github.com/openai/openai-python/blob/main/httpx2.md) ⭐️ 7.0/10

OpenAI&\#x27;s Python SDK is migrating to HTTPX2, a stable fork of the httpx HTTP client, according to a migration document in the repository. Because httpx is heading toward a 1.0 release with breaking changes, HTTPX2 promises to preserve the existing API and give SDKs a more stable dependency target. Anthropic&\#x27;s Python SDK made the same switch weeks after OpenAI, according to a Hacker News comment. The change carries trade-offs that commenters are still debating, including how it compares with alternatives such as niquests.

hackernews · tosh · Aug 28, 11:51 · [Discussion](https://news.ycombinator.com/item?id=49477212)

**「Background」** The OpenAI Python SDK is adopting HTTPX2, a fork of the widely used httpx HTTP client, for both its synchronous and asynchronous clients; HTTPX2 now installs automatically with the \`openai\` package, replacing the previous \`httpx\` dependency. The fork exists because the original httpx project is heading toward a 1.0 release that will introduce breaking changes, while HTTPX2 promises to preserve the existing API. According to OpenAI&\#x27;s migration issue, swapping to HTTPX2 is straightforward for common usage because it is API-compatible and a drop-in replacement, and the change prevents the SDK from depending on an unmaintained transport layer.

**「Impact」** Developers using OpenAI&\#x27;s or Anthropic&\#x27;s Python SDKs may see HTTPX2 appear as a transitive dependency and should verify that their own httpx-based code remains compatible, especially if they rely on internal or version-specific httpx behavior.

**「Community Discussion」** Commenters pointed out that Anthropic adopted the same fork and generally understood the stability motivation, while others questioned whether niquests was considered, what concrete upsides exist, and why the change deserved front-page attention. One user also reported a network error when trying to reach OpenAI support.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/openai-python/blob/main/httpx2.md">openai-python/httpx2.md at main - GitHub</a></li>
<li><a href="https://developers.openai.com/api/reference/python">OpenAI Python API library | OpenAI API Reference</a></li>
<li><a href="https://github.com/openai/openai-python/issues/3375">Consider migrating from httpx to httpx2 #3375 - GitHub</a></li>

</ul>
</details>

**Tags**: `#openai`, `#httpx`, `#python`, `#sdks`, `#dependency-management`

---

<a id="item-tech-news-8"></a>
### [Berlin Mayor Says City Will Not Cave to Hackers&\#x27; Ransom](https://www.bbc.co.uk/news/articles/cm2q7gv3l5qo?at_medium=RSS&amp;at_campaign=rss) ⭐️ 7.0/10

Berlin&\#x27;s mayor, Kai Wegner, said the city is being blackmailed by hackers who compromised city systems and stole data, but officials will not pay the ransom demand. The hackers reportedly demand 30 bitcoin \(around €2 million, £1.7 million\), and the Rhysida group, linked to previous attacks including on the British Museum, is said to be responsible. An initial data leak occurred between 7 and 12 August, after which two department networks were shut down on 14 August, halting housing benefit and payment applications for several days. Investigators found further leaks in the transport and environment department, and the mayor&\#x27;s office warned that personal or other non-public data may be affected. Rhysida has threatened to auction the 5.79 terabytes of stolen data within seven days, with a starting price of 30 bitcoin.

rss · BBC World · Aug 28, 21:29

**「Background」** Rhysida is a ransomware group first observed in May 2023 that operates as a ransomware-as-a-service \(RaaS\), using phishing and tools like Cobalt Strike to breach networks, encrypt data, and threaten to publish stolen files unless a ransom is paid. The group previously disrupted the British Museum&\#x27;s systems in 2023, publishing around 500,000 files after the institution refused to pay. Berlin&\#x27;s city administration has been targeted in a similar extortion scheme, with the attackers claiming to have stolen 5.79 TB of data and demanding 30 bitcoin.

**「Impact」** Berlin residents faced disrupted housing benefit and payment services for days, and now risk exposure of personal data if the stolen information is published or auctioned. If Rhysida follows its pattern from the British Museum attack, the data could be dumped on the dark web, affecting thousands of individuals whose contracts, personnel files, and contact details may be included.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rhysida_%28hacker_group%29">Rhysida (hacker group) - Wikipedia</a></li>
<li><a href="https://www.sentinelone.com/anthology/rhysida/">Rhysida Ransomware: In-Depth Analysis, Detection, Mitigation Analyzing Rhysida Ransomware Intrusion - Fortinet Ransom-DB | Live Threat Command Center 202308041500_Rhysida Ransomware Sector Alert_TLPCLEAR - HHS.gov Rhysida Ransomware: The Silent Serpent - Threat Actors rhysida - Ransomware Group | Ransomwhere.org</a></li>
<li><a href="https://www.fortinet.com/content/dam/fortinet/assets/threat-reports/rhysida-ransomware-intrusion.pdf">Analyzing Rhysida Ransomware Intrusion - Fortinet</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#ransomware`, `#data breach`, `#Berlin`, `#hacking`

---

<a id="item-tech-news-9"></a>
### [US datacentre backlash grows as states weigh bans](https://www.theguardian.com/environment/2026/aug/19/is-the-environmental-impact-of-datacentres-finally-cutting-through) ⭐️ 7.0/10

Anti-datacentre sentiment is rising across the US political spectrum as the public learns about effects on energy bills. More than a dozen states have considered moratoria, and New York in July 2026 became the first US state to enact a temporary ban on datacentres. Senator Bernie Sanders and Representative Alexandria Ocasio-Cortez have proposed a national moratorium, while Texas Governor Greg Abbott called for a ban on datacentre development in rural parts of his state. The pushback reflects growing concern about the environmental and energy-cost impacts of AI and cloud infrastructure.

rss · The Guardian International · Aug 28, 16:20

**「Background」** Datacentres are energy-intensive facilities that support cloud computing and AI workloads, making them a growing source of electricity demand and environmental concern. The political and regulatory response now ranges from state-level moratoria to federal proposals, driven by public worries about higher energy bills and local environmental damage.

**「Impact」** Operators and developers face new regulatory uncertainty as state moratoria and national proposals threaten approval timelines for AI and cloud infrastructure across the US.

**Tags**: `#datacentres`, `#regulation`, `#environmental impact`, `#AI infrastructure`, `#energy`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Exterminauts Preview: Co-op PVE, Mod Builds, and Blue-Collar Bosses](https://www.gcores.com/articles/218963) ⭐️ 4.0/10

rss · 机核GCORES游戏资讯 · Aug 28, 14:30

**「Background」** At a ChinaJoy hands-on session, the author previewed Exterminauts, a three-player co-op PVE action shooter from Behaviour Interactive set for PC/PS5/Xbox in 2027. Players take on &quot;Exterminauts&quot;—blue-collar astronaut exterminators on planet Tian—clearing alien creatures and completing tasks for a mega-corporation, a premise that invites comparisons with Helldivers 2.

**「Solution」** Each mission begins with the captain choosing the target, planet, difficulty, and enemy type, then the squad selects weapons and weapon mods. Mods are powerful enough that the session started without them, but once equipped, the author&\#x27;s crit-and-effect build melted tanky enemies while a teammate&\#x27;s healing mod kept them alive—revealing build synergy as the core fun. Friendly fire is common, and a resurrection gun literally shoots dead teammates back in, creating an explosion on impact. Supplies are paid from the company budget and deducted from the mission&\#x27;s wages, so resource efficiency matters. Big firepower comes from overloading tool-like weapons—such as a cryo tool that freezes everything, including friends—or by spending power to skip puzzle interactions. The blue-collar aesthetic is detailed, yet during the short session the author never felt the oppressive &quot;working for a bad boss&quot; atmosphere. The release plan is aggressive: seasons every three months, Battle Passes every six weeks, and a price below similar products.

**「Takeaway」** The author argues that games like Helldivers 2 succeed not just through fun combat but through fully selling players on their world and cause, something Exterminauts must prove with a new IP. Worth following for fans of three-player co-op PVE shooters, though its blue-collar soul needs more time in the full version to shine.

**Tags**: `#game-preview`, `#co-op-pve`, `#game-design`, `#exterminauts`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Corn and wheat futures hit three-year highs on supply concerns](https://www.cnbc.com/2026/08/28/corn-and-wheat-prices-jump-to-highest-prices-in-more-than-three-years.html) ⭐️ 8.0/10

Corn and wheat futures jumped on Aug. 28, 2026, to their highest levels in more than three years, with wheat settling 3.1% higher at 784 cents per bushel and corn settling 0.6% higher at 536.5 cents per bushel. Wheat posted its biggest weekly gain since March 2022, rising 12.1%.

rss · CNBC Finance · Aug 28, 20:00

**「Background」** Corn rallied after the U.S. Department of Agriculture cut its U.S. yield forecast and crop tour observations showed heat damage, while wheat was driven by disruptions to Black Sea exports after escalating Russia-Ukraine tensions.

**「Impact」** Higher grain prices can raise costs for food producers, livestock feed users, and consumers, since wheat and corn are staple inputs for food and animal feed.

**Tags**: `#wheat prices`, `#corn prices`, `#supply disruption`, `#USDA crop report`, `#Russia-Ukraine conflict`

---

<a id="item-finance-news-2"></a>
### [U.S. appeals court rules sports prediction contracts are sports bets, not CFTC-regulated swaps](https://www.cnbc.com/2026/08/28/appeals-court-rules-against-prediction-markets-tees-up-scotus-fight.html) ⭐️ 8.0/10

A federal appeals court ruled that sports-related event contracts offered by Kalshi, Crypto.com, and Robinhood are sports bets, not CFTC-regulated swaps, rejecting the platforms&\#x27; requests to stop Nevada&\#x27;s enforcement. The 9th Circuit decision conflicts with an April 3rd Circuit ruling that only the CFTC can regulate such contracts, making Supreme Court review likely.

rss · CNBC Finance · Aug 29, 02:23

**「Background」** The Commodity Futures Trading Commission \(CFTC\), which oversees swaps—a type of derivative—had argued it has exclusive jurisdiction over all event contracts and has sued nine states to defend that position. Nevada and other states contended these offerings were unlicensed sports betting.

**「Impact」** The ruling lets Nevada and other states in the 9th Circuit&\#x27;s territory continue enforcing gambling rules against the platforms; Robinhood said it plans to appeal.

**Tags**: `#prediction markets`, `#CFTC`, `#regulation`, `#litigation`, `#derivatives`

---

<a id="item-finance-news-3"></a>
### [Rate-Hike Odds for September Rise After Warsh Speech](https://www.cnbc.com/2026/08/28/-september-fed-decision-now-a-coin-flip-as-rate-hike-odds-increase.html) ⭐️ 8.0/10

Traders now view the Federal Reserve&\#x27;s September rate decision as a near coin flip after Chairman Kevin Warsh&\#x27;s hawkish Jackson Hole speech. Implied odds of a quarter-percentage-point hike at the Sept. 16 meeting are 48% on Kalshi, 56% on CME FedWatch, and 49% on Polymarket. Before the speech, traders put nearly 70% odds on the Fed holding rates steady.

rss · CNBC Finance · Aug 28, 15:22

**「Background」** Odds had fallen over the past month after July data showed job losses and cooler inflation, but Warsh said the summer readings did not convince him that underlying price pressures were moving to the Fed&\#x27;s 2% target.

**Tags**: `#Federal Reserve`, `#Interest Rates`, `#Monetary Policy`, `#Jackson Hole`, `#Market Expectations`

---

<a id="item-finance-news-4"></a>
### [Premarket movers: PayPal drops on scrapped buyout, Affirm and Gap gain on earnings](https://www.cnbc.com/2026/08/28/stocks-making-the-biggest-moves-premarket-pypl-afrm-gap-mrvl.html) ⭐️ 7.0/10

Shares moved sharply premarket after corporate news: PayPal fell nearly 16% when Advent and Stripe dropped a potential buyout; Affirm, Gap, and Elastic jumped after earnings beats or stronger guidance; Marvell, Rubrik, and Autodesk fell on weaker guidance or margins.

rss · CNBC Finance · Aug 28, 11:43

**「Background」** The moves mostly follow quarterly reports and forecasts compared with LSEG or StreetAccount consensus: Affirm&\#x27;s fiscal fourth-quarter revenue was $1.17 billion versus a $1.11 billion estimate, Gap&\#x27;s adjusted second-quarter earnings were 52 cents versus 48 cents expected, Elastic guided above forecasts, Marvell&\#x27;s current-quarter profit forecast was $1.10 per share plus or minus 5 cents versus $1.07 expected, Rubrik&\#x27;s gross margin missed while it beat on profit and revenue, and Autodesk&\#x27;s third-quarter profit forecast was below estimates.

**Tags**: `#Earnings`, `#Mergers and Acquisitions`, `#Stock Movers`, `#PayPal`, `#Guidance`

---