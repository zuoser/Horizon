---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22
lang: en
---

> From 165 items, 11 important content pieces were selected

---

**Technology News**
1. [Cloudflare Python Workers reach general availability](#item-tech-news-1) ⭐️ 8.0/10
2. [Xiaomi releases MiMo v2.6 open-weight Flash and Pro models](#item-tech-news-2) ⭐️ 7.0/10
3. [I Don&\#x27;t Want to Read What You Didn&\#x27;t Write](#item-tech-news-3) ⭐️ 7.0/10
4. [Bryan Cantrill on What Sun Microsystems Got Wrong](#item-tech-news-4) ⭐️ 7.0/10
5. [xAI&\#x27;s Grok 4.7 Point Release Draws Mixed Early Reactions](#item-tech-news-5) ⭐️ 7.0/10
6. [FAA halts East Coast flights after fiber cut and backup failure](#item-tech-news-6) ⭐️ 7.0/10
7. [US and China discuss AI incident notification mechanism](#item-tech-news-7) ⭐️ 7.0/10
8. [TypeSafe AI&\#x27;s Jev returns typed probabilistic decisions, not text](#item-tech-news-8) ⭐️ 7.0/10
9. [SemiAnalysis: Mapping Mixture-of-Experts Models onto Inference Hardware](#item-tech-news-9) ⭐️ 7.0/10

**Technology Blog**
1. [TGS2026 Interview: Dynasty Warriors 2 Remaster’s Classic-Modern Balance](#item-tech-blog-1) ⭐️ 5.0/10

**Financial News**
1. [Tariffs, fuel costs and rising rates squeeze US companies, CNBC reports](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Cloudflare Python Workers reach general availability](https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/) ⭐️ 8.0/10

After a two-year preview, Cloudflare&\#x27;s Python Workers are now generally available, with the company describing Python as &quot;a first-class, fully supported language on the Cloudflare Developer Platform.&quot; Python code runs compiled to WebAssembly via Pyodide inside Cloudflare&\#x27;s V8-based workerd runtime, and the release announcement is credited to Gyeongjae Choi, Dominik Picheta, and Hood Chatham, two of whom are Pyodide core maintainers. Documented limitations include that both multiprocessing and threading are non-functional in the WebAssembly VM. The pywrangler development tool \(packaged confusingly as workers-py on PyPI\) provides a local simulation of the stack, executing code with Pyodide in WebAssembly in V8 inside a 123MB workerd binary, which one installation placed at node\_modules/@cloudflare/workerd-darwin-arm64/bin/workerd.

rss · Simon Willison · Sep 21, 22:25

**「Background」** Cloudflare Workers is a serverless platform that executes code inside workerd, Cloudflare&\#x27;s open-source runtime built on the V8 JavaScript engine. Python support was introduced roughly two years before general availability as an open beta that embedded Pyodide, a port of CPython compiled to WebAssembly, directly into workerd rather than reimplementing the language for the platform. That WebAssembly-based design is what lets many existing Python packages run in the Workers sandbox, but it also constrains features that depend on native threads or separate processes.

**「Impact」** Python developers can now deploy Python web frameworks and AI orchestration libraries directly on Cloudflare Workers and integrate with D1, R2, and Workers AI without writing JavaScript glue code. Because threading and multiprocessing remain non-functional in the WebAssembly VM, however, workloads that depend on those modules are still not viable on this runtime.

**「Community discussion」** An urllib3 maintainer noted that urllib3 merged large contributions adding Pyodide/Emscripten support years ago and later JSPI support, which made this work possible for Requests, and said the funding went to the external contributor rather than to urllib3&\#x27;s maintainers. Wasmer&\#x27;s Syrus Akbary welcomed Cloudflare&\#x27;s progress since the original launch, particularly PEP 783 standardizing PyEmscripten, while saying some architectural concerns from his earlier feedback remain; other commenters compared the move to Google App Engine&\#x27;s 2008 Python 2.5 launch or joked about misreading the headline.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/python-workers?ref=dmytrolitvinov.com/">Bringing Python to Workers using Pyodide and WebAssembly</a></li>
<li><a href="https://blog.cloudflare.com/python-workers-ga/">Python Workers are now generally available | Cloudflare Blog</a></li>
<li><a href="https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/">Cloudflare Python Workers are now generally available</a></li>

</ul>
</details>

**Tags**: `#Cloudflare Workers`, `#Python`, `#WebAssembly`, `#Serverless`, `#Pyodide`

---

<a id="item-tech-news-2"></a>
### [Xiaomi releases MiMo v2.6 open-weight Flash and Pro models](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 7.0/10

Xiaomi released MiMo v2.6, an open-weight model family with Flash and Pro variants. The Flash model has 309B total and 15B activated parameters, while Pro has 1.02T total and 42B activated parameters; weights are publicly posted on Hugging Face. Xiaomi paired the release with transparent training documentation, a detailed technical report, and a public real-time RL training dashboard. The Hacker News submission drew 519 points and 269 comments. The release matters as a substantive open-weight LLM drop from Xiaomi with concrete architecture details and unusually open training disclosures.

hackernews · volf\_ · Sep 21, 20:12 · [Discussion](https://news.ycombinator.com/item?id=49792730)

**「Background」** MiMo is Xiaomi&\#x27;s family of large language models, and version 2.6 is released as two open-weight variants built on a mixture-of-experts \(MoE\) architecture, in which only a fraction of a model&\#x27;s total parameters are activated for each token. Flash is reported at roughly 309 billion total and 15 billion activated parameters, while Pro is around 1.02 trillion total and 42 billion activated, with the larger model optimized for agentic coding and long-horizon tool-use workflows. The release package pairs weights on Hugging Face with a technical report, deployment instructions, and detailed reinforcement-learning disclosures, including a Pro RL post-training run that was streamed live at a reported compute cost of about $2.62 million.

**「Impact」** Developers choosing an open-weight model for agent work gain a directly competitive option: Xiaomi states that MiMo-V2.6-Pro matches Claude Opus 5 and GPT-5.6 Sol on most agent benchmarks, while MiMo-V2.6-Flash reportedly outperforms the earlier MiMo-V2.5-Pro. Those parity claims come from the vendor and have not been independently verified here.

**「Community Discussion」** Commenters broadly praised the transparency, with one calling the real-time RL training dashboard an incredible learning and teaching tool, while another said affordability makes Chinese models more exciting than American models. Others focused on concrete release details like the Flash and Pro parameter counts and Hugging Face weight links, shared SVG pelican tests, and noted a recurring &quot;01 - UPPERCASE TEXT&quot; frontend design motif in generated examples.

<details><summary>References</summary>
<ul>
<li><a href="https://alphasignal.ai/news/xiaomi-s-mimo-v2-6-pro-tops-open-weight-rankings-with-a-1t-parameter-model">Xiaomi&#x27;s MiMo-V2.6-Pro Tops Open-Weight Rankings With a 1T-Parameter Model | AlphaSignal</a></li>
<li><a href="https://rajeshparikh.substack.com/p/xiaomis-live-mimo-v26-rl-run">Xiaomi’s Live MiMo-V2.6 RL Run - by Rajesh Parikh</a></li>
<li><a href="https://runtimewire.com/article/xiaomi-open-sources-mimo-v2-6-rl-cost-3-47m">Xiaomi open-sources MiMo-V2.6 and the RL machinery behind it</a></li>
<li><a href="https://officechai.com/ai/xiaomi-mimo-v-2-6-pro-benchmarks/">Xiaomi MiMo V2.6 Pro Becomes Top Open Model On Artificial Analysis Intelligence Index</a></li>
<li><a href="https://mimo.mi.com/docs/en-US/news/latest/v2-6">Xiaomi MiMo-V2.6 Series: 3 New Models Officially Released</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open weights`, `#model release`, `#mixture-of-experts`, `#AI training transparency`

---

<a id="item-tech-news-3"></a>
### [I Don&\#x27;t Want to Read What You Didn&\#x27;t Write](https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/) ⭐️ 7.0/10

A blog post titled &quot;I Don&\#x27;t Want to Read What You Didn&\#x27;t Write&quot; argues against reading text not written by its purported author, and it sparked a Hacker News discussion with 220 points and 86 comments about LLM writing quality, authenticity, and communication in software engineering. The post critiques the use of AI to produce technical writing and documentation instead of having the author write it directly. Commenters debated whether LLM writing quality has declined rather than plateaued and whether LLMs can meaningfully transfer information the author did not supply. A practical theme was that AI-generated pull-request descriptions can add review friction when they bury small changes under extensive rationale.

hackernews · mooreds · Sep 21, 22:30 · [Discussion](https://news.ycombinator.com/item?id=49794330)

**「Background」** The item centers on a blog post by Colin Breck titled “I Don’t Want to Read What You Didn’t Write,” which argues against reading text that an author did not write themselves. The post responds to a broader shift in which people who rarely produced original writing are suddenly generating extensive design proposals, business plans, documentation, presentations, tickets, pull requests, and meeting summaries with LLMs. The accompanying Hacker News discussion examines how that shift affects authenticity, information transfer, and communication norms in software engineering.

**「Impact」** For software engineers and reviewers, the practical consequence is that generated documentation and PR descriptions can shift from helpful context to review overhead, making explicit team norms about LLM-assisted writing more important.

**「Community Discussion」** Commenters broadly agreed that LLM-generated writing often fails to carry the author&\#x27;s intended meaning, but they disagreed on the cause: one argued that model writing quality has dropped sharply and that good writing is expensive, while another framed the issue as a fundamental limit of asking an LLM to fill in semantic information the author omitted. A recurring practical example was PR review friction, with one reviewer objecting to pages of generated description and justification for a 20-line change and another noting that the article&\#x27;s own opening sentence illustrated the problem it criticizes.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/">I Don’t Want to Read What You Didn’t Write</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#AI-generated content`, `#writing`, `#software engineering culture`, `#developer communication`

---

<a id="item-tech-news-4"></a>
### [Bryan Cantrill on What Sun Microsystems Got Wrong](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 7.0/10

Bryan Cantrill, the DTrace co-creator and former Sun engineer, has published a retrospective titled &quot;What Sun got wrong&quot; on his blog at bcantrill.dtrace.org, examining the strategic and technical missteps that contributed to Sun Microsystems&\#x27; decline. The post drew substantial attention on Hacker News, where it accumulated 494 points and 283 comments from readers sharing first-hand experience with Sun hardware, software, and sales. Because no article text was supplied, the specific arguments and claims in the piece cannot be summarized or verified here; the item&\#x27;s value rests on Cantrill&\#x27;s insider authority and the accompanying discussion. Commenters&\#x27; recollections focus on Sun&\#x27;s enterprise procurement friction in the late 1990s and 2000s, decisions such as briefly cancelling Solaris on x86 in 2002 and failing to reach a deal with Google that same year, and the company&\#x27;s stock collapse after the dot-com bubble.

hackernews · chmaynard · Sep 21, 14:03 · [Discussion](https://news.ycombinator.com/item?id=49787436)

**「Background」** Sun Microsystems was the vendor behind the SPARC processor architecture and the Solaris operating system, a central force in enterprise computing from the 1980s through the dot-com boom before its fortunes turned in the 2000s. Bryan Cantrill is a former Sun engineer and co-creator of the DTrace tracing framework, and the essay&\#x27;s argument rests on that first-hand experience inside the company; coverage of the piece notes that he joined a startup after leaving Sun \(tool-1-1\). The environment the essay examines is illustrated by an often-cited 2005 episode in which a fast-growing OpenSolaris-based startup wanted to buy Sun hardware but could not get Sun to respond, while Dell&\#x27;s sales representative closed the deal within weeks \(tool-1-2\).

**「Community Discussion」** Commenters largely agree that Sun&\#x27;s weaknesses lay in business execution rather than engineering: one reader contends that Sun &quot;was never interested in running a business&quot; and cared more about building top-tier technology, while another describes being forced into live sales meetings and endless quote revisions, noting that rails and power cords for a DEC Alpha server could cost more than a fully delivered Dell machine. Specific grievances cited include the 2002 cancellation of Solaris on x86, the failed Google deal, and the stock&\#x27;s fall from roughly $70 to $7, alongside fonder memories of Sun thin clients and workstations used at university.

<details><summary>References</summary>
<ul>
<li><a href="https://ecosistemastartup.com/bryan-cantrill-oxide-revela-lo-que-sun-hizo-mal/">Bryan Cantrill (Oxide) revela lo que Sun hizo mal – El Ecosistema Startup</a></li>
<li><a href="https://daily.dev/posts/what-sun-got-wrong-zlxeetcyz">What Sun got wrong | daily.dev</a></li>

</ul>
</details>

**Tags**: `#Sun Microsystems`, `#software industry history`, `#business strategy`, `#Solaris`, `#open source`

---

<a id="item-tech-news-5"></a>
### [xAI&\#x27;s Grok 4.7 Point Release Draws Mixed Early Reactions](https://x.ai/news/grok-4-7) ⭐️ 7.0/10

xAI has released Grok 4.7 as a point-release update to its frontier large language model, drawing substantial Hacker News attention and mixed early reactions. The release item itself provides no detailed technical content, so many specifications come from Hacker News commenters: they said Grok 4.7 has 40% more weights than Grok 4.6 while keeping the same $2 input and $6 output token pricing, and that the launch came almost two weeks later than originally expected. Early user impressions characterized Grok 4.7 as slower and more expensive, with some suspecting that extra token use was needed to improve benchmark results, though whether it clears users&\#x27; practical intelligence thresholds for coding and agentic workflows was disputed. Some commenters welcomed xAI&\#x27;s increasing release cadence and predicted a larger step up with Grok 5 later this year.

hackernews · meetpateltech · Sep 21, 15:50 · [Discussion](https://news.ycombinator.com/item?id=49788838)

**「Background」** Grok is the flagship large language model family from xAI, and the 4.7 label denotes a point release that refines the preceding 4.6 model rather than a generational architectural break. In the current frontier landscape, xAI is competing directly with Anthropic&\#x27;s Claude and OpenAI&\#x27;s GPT lines, so each point release tends to be judged on benchmark positioning and price-performance rather than on a new capability class. Grok 4.7 retains the same $2 per million input tokens and $6 per million output tokens pricing as its predecessor, and reporting describes it as built on a larger base model trained with longer reinforcement learning and improved self-verification.

**「Impact」** For developers and teams weighing Grok 4.7 against rival frontier models, the expanded model keeps the same $2-per-million input and $6-per-million output pricing, so per-task cost rather than sticker price is likely to decide adoption, especially with early users reporting slower responses and heavier token use. xAI&\#x27;s own GDPval chart reports 1,695 for Grok 4.7 at xhigh reasoning for professional work, but given only mixed early impressions, it remains unconfirmed whether that translates into better agentic coding outcomes.

**「Community Discussion」** Hacker News commenters were divided: some saw incremental or token-burning benchmark gains, slower and more expensive behavior, and questioned xAI&\#x27;s margins after the reported two-week delay, while others welcomed the faster release cadence and looked forward to Grok 5. One commenter also described inconsistent reasoning-level token usage and planned to retry directly through the xAI API instead of OpenRouter.

<details><summary>References</summary>
<ul>
<li><a href="https://kingy.ai/blog/grok-4-7-release-features-pricing-access/">Grok 4.7 Is Out: New Features, Pricing and How to Try It</a></li>
<li><a href="https://the-decoder.com/xai-launches-grok-4-7-at-bargain-prices-but-benchmarks-reveal-a-wide-gap-to-claude-and-gpt-6/">xAI launches Grok 4.7 at bargain prices, but benchmarks reveal a wide gap to Claude and GPT-6</a></li>
<li><a href="https://www.androidheadlines.com/2026/09/grok-4-7-ai-launch-coding-upgrades-pricing.html">Grok 4.7 Brings Big Coding Upgrades to Challenge Claude AI at Unchanged Pricing</a></li>
<li><a href="https://kingy.ai/blog/grok-4-7-benchmarks-specs-frontier-comparison/">Grok 4.7 Benchmarks vs GPT, Claude &amp; Gemini</a></li>

</ul>
</details>

**Tags**: `#Grok`, `#large language models`, `#model release`, `#xAI`, `#benchmarking`

---

<a id="item-tech-news-6"></a>
### [FAA halts East Coast flights after fiber cut and backup failure](https://www.reuters.com/world/us/faa-halts-some-us-east-coast-flights-due-communication-issues-2026-09-21/) ⭐️ 7.0/10

Reuters reported that the FAA halted flights at busy East Coast airports after a fiber line cut disrupted communications. When the system attempted to switch to a backup fiber link, that link was also broken, leaving no working path. The halt affected a safety-critical aviation system, making the outage a notable example of how single points of failure and failover gaps can disrupt operations. The incident has prompted discussion about whether critical infrastructure operators provide enough diverse paths and continuously monitor backup links before an emergency.

hackernews · allanbreyes · Sep 21, 18:41 · [Discussion](https://news.ycombinator.com/item?id=49791509)

**「Background」** The FAA&\#x27;s air traffic control network relies on dedicated telecommunications circuits rather than the public internet, so traffic cannot simply reroute around a severed cable the way ordinary internet traffic would. The affected airports serve New York, Philadelphia, and Boston, and the FAA said the initial fiber cut occurred at a construction site in New Jersey, with a backup fiber line also broken and repairs estimated to take up to 13 hours. Separately, the FAA has been preparing to field a new AI-based traffic-flow management capability — an effort reported at roughly $875 million — with an initial &quot;bounded introduction&quot; limited to air traffic at 24,000 feet \(7,300 m\) and above.

**「Impact」** The FAA ground stop caused flight delays at five East Coast airports—Newark Liberty, Teterboro, Philadelphia International, LaGuardia, and John F. Kennedy International—after a construction crew cut a fiber cable and the backup for Philadelphia&\#x27;s radio communications system also failed, affecting one of the country&\#x27;s most congested airspaces.

**「Community Discussion」** Commenters largely criticized the lack of redundancy and monitoring, noting that two fiber paths are insufficient for critical workloads and that the backup fiber was discovered to be broken only when failover was attempted; one asked how long it had been down. Others questioned whether ATC networks are separate or air-gapped with fewer alternative routes, and one commenter pointed to a newly deploying FAA ATC system.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cp24.com/news/world/2026/09/21/us-halts-flights-at-busy-east-coast-airports-says-fiber-line-cut-at-construction-site/">U.S. halts East Coast airports flights due to cut fiber line</a></li>
<li><a href="https://www.aljazeera.com/economy/2026/9/21/faa-halts-flights-to-major-us-east-coast-airports-amid-outage">FAA halts flights to major US East Coast airports amid... | Al Jazeera</a></li>
<li><a href="https://www.ntd.com/faa-halts-east-coast-flights-after-backup-fiber-line-cut_1174093.html">FAA Halts East Coast Flights After Backup Fiber Line Cut | NTD</a></li>
<li><a href="https://www.airwaysmag.com/new-post/faa-smart-first-deployment-washington">FAA Prepares to Field SMART in Washington in First Operational Deployment</a></li>
<li><a href="https://arstechnica.com/ai/2026/09/faa-tees-up-875m-ai-tool-to-help-manage-air-traffic-congestion/">FAA tees up $875M AI tool to help manage air traffic congestion - Ars Technica</a></li>
<li><a href="https://www.aljazeera.com/economy/2026/9/21/faa-halts-flights-to-major-us-east-coast-airports-amid-outage">FAA halts flights to major US East Coast airports amid... | Al Jazeera</a></li>
<li><a href="https://sg.news.yahoo.com/fiber-cut-construction-crew-leads-184300766.html">Fiber cut by construction crew leads to ground stop and delays at...</a></li>
<li><a href="https://www.nytimes.com/2026/09/21/us/east-coast-flights-ground-stop-communication-failure.html">Technical Problems Ground Flights at Major East Coast Airports</a></li>

</ul>
</details>

**Tags**: `#network reliability`, `#infrastructure outage`, `#aviation systems`, `#fiber optics`, `#systems engineering`

---

<a id="item-tech-news-7"></a>
### [US and China discuss AI incident notification mechanism](https://www.bbc.co.uk/news/articles/c8vgyzn2d31yo?at_medium=RSS&amp;at_campaign=rss) ⭐️ 7.0/10

Top US and Chinese officials discussed creating a new &quot;notification mechanism&quot; for AI incidents that could affect national security, Treasury Secretary Scott Bessent told reporters on Sunday. Bessent described the talks with Chinese Vice Premier He Lifeng in New York as successful and said they came ahead of a planned summit between President Donald Trump and Xi Jinping in Washington later this week. Bessent argued that moving from opacity to more transparency between the world&\#x27;s number one and number two AI powers is important, while Chinese state news agency Xinhua said the two sides had candid, in-depth and constructive exchanges on key economic and trade issues and noted they discussed AI. The meeting also covered plans to operationalise a process to identify potential tariff cuts on goods called the Board of Trade, as a tariffs truce between the two largest economies is due to expire on 10 November. The report described early talks rather than a concrete agreement, and the BBC said it contacted the Chinese embassy in the US for comment.

rss · BBC World · Sep 21, 05:50

**「Background」** A notification mechanism for AI incidents would involve the US and China sharing information about serious AI-related threats that could affect national security, an idea Washington proposed during the New York talks. The discussions are part of a broader US-China race for AI and technology leadership, and the two leaders have addressed AI cooperation before: at a May meeting in Beijing, collaboration on AI was among the issues discussed alongside a trade agreement in which China would buy Boeing jets and US agricultural goods in exchange for lower tariffs. The upcoming Washington summit, described as the first Trump-Xi summit on US soil since 2017, will follow the Bessent-He talks, and the AI notification proposal is one item the leaders may consider.

**「Impact」** For AI developers and companies operating across both markets, a bilateral incident-notification mechanism would create a formal channel for the two leading AI powers to alert each other to AI incidents with national-security implications, a shift from the current opacity that officials described as the motivation for the talks. The discussions remain preliminary, with no agreement announced and no public detail on the scope, timing, or categories of incidents that would be reportable.

<details><summary>References</summary>
<ul>
<li><a href="https://edition.cnn.com/2026/09/20/business/us-china-trade-talks-ai-intl-hnk">Bessent proposes AI safety notifications in talks with China ahead...</a></li>
<li><a href="https://the-decoder.com/us-and-china-agree-on-ai-dialogue-with-security-mechanism-ahead-of-trump-xi-summit/">US and China agree on AI dialogue with security mechanism ahead of...</a></li>
<li><a href="https://www.aljazeera.com/economy/2026/9/20/us-china-open-high-level-talks-ahead-of-trump-xi-summit">US proposes AI safety notification mechanism in talks with China</a></li>
<li><a href="https://nourished.news/story/j0ew7uzsoblvflrq">AI diplomacy on edge as US , China push for dialogue</a></li>
<li><a href="https://en.walaw.press/articles/us_proposes_ai_incident_notification_mechanism_with_china/GPFRLRXPXGQM">US proposes AI incident notification mechanism with China</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI governance`, `#US-China relations`, `#technology policy`, `#national security`

---

<a id="item-tech-news-8"></a>
### [TypeSafe AI&\#x27;s Jev returns typed probabilistic decisions, not text](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 7.0/10

TypeSafe AI unveiled Jev last week as the first example of what it calls &quot;System One models,&quot; a category Simon Willison—echoing Maggie Appleton—argues is better named &quot;decision models.&quot; Jev accepts text states in the form of a string, an array of strings, or a set of name-value pairs, but returns floating-point numbers instead of text: a confidence value between 0 and 1 for &quot;Noul&quot; \(Bernoulli\) yes/no questions, a probability distribution across supplied options for choice questions, and a numeric score within a described range for score questions. It is positioned as fast and cheap, charging only for input at $0.042 per million tokens—below OpenAI&\#x27;s GPT-5 Nano at $0.05 per million—with questions against a single state evaluated in parallel, making it suited to classification, labeling, prioritization, and reranking tasks such as rescoring BM25 search candidates. Willison cautions that Jev represents a further regression toward black-box machine learning, returning only a number with no justification or explanation, which makes bias a central concern and structured evals more important than for ordinary LLM projects; an informal test scoring Bay Area cities on whether they were a &quot;Good city?&quot; rated Cupertino top and East Palo Alto bottom. Within days of release, the community produced experimental projects including jevchat, jev-leftpad, and jev-2048, along with open-weight recreations such as Jared Palmer&\#x27;s Kev, built on Qwen 3.5 at 0.8B, 4B, and 9B, and a JevBench benchmark comparing &quot;Jev-class decision models,&quot; though no independent benchmark results for Jev itself were reported.

rss · Simon Willison · Sep 21, 23:09

**「Background」** TypeSafe AI launched Jev on September 15, 2026, presenting it as the first of a new &quot;System One model&quot; category. The name contrasts with conventional &quot;System Two&quot; LLMs, which reason out loud token by token and return text, whereas Jev takes a state object plus predefined questions and returns typed answers with probabilities — reportedly in roughly 70–500 ms. Writers such as Maggie Appleton prefer the term &quot;decision models&quot; for this class, since the output is a decision rather than prose.

**「Impact」** For developers building classification, labeling, prioritization, or search-reranking pipelines, Jev&\#x27;s typed probabilistic outputs — yes/no confidence scores, choice distributions, and numeric scores — combined with $0.042 per million input tokens and free output let teams run hundreds or thousands of scoring experiments for cents while evaluating many questions in parallel. The practical limit is that Jev returns only floating-point numbers with no justification, so teams must supply their own evals and calibration checks before trusting it in consequential decisions; independent comparison tooling such as the JevBench benchmark for &quot;Jev-class decision models&quot; is emerging, but the source provides no independent accuracy or bias results for Jev itself.

<details><summary>References</summary>
<ul>
<li><a href="https://jev-agent.com/">What is Jev ? TypeSafe AI &#x27;s System One decision model explained</a></li>
<li><a href="https://jevai.net/">Jev AI — Decisions at machine speed</a></li>
<li><a href="https://aijev.org/">Jev : System One Decision Model Explained | AIJev</a></li>
<li><a href="https://benchmarkheaven.com/jev-models">Jev -class decision models — JevBench v1.2 | Benchmark Heaven</a></li>
<li><a href="https://jevmodel.org/benchmarks/">Jev Benchmarks : Accuracy, Calibration, Latency, Fallback</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#AI models`, `#decision models`, `#model interfaces`, `#TypeSafe AI`

---

<a id="item-tech-news-9"></a>
### [SemiAnalysis: Mapping Mixture-of-Experts Models onto Inference Hardware](https://newsletter.semianalysis.com/p/computation-and-data-movement-for) ⭐️ 7.0/10

SemiAnalysis published an article titled &quot;Computation and Data Movement for Inference,&quot; authored by Tanj Bennett, that addresses how Mixture-of-Experts \(MoE\) models are mapped onto inference hardware. According to the available description, the piece covers MoE model structure, the data movement involved during inference, and approaches to efficient serving. The topic matters because MoE inference is both compute-intensive and memory-bandwidth-intensive, making the placement of experts and the cost of moving activations and weights central concerns for AI infrastructure and model-serving teams. The item as supplied contains only a title and a one-line description, with no body text, benchmarks, specific technical claims, version numbers, hardware targets, or performance figures, so the depth, findings, and any concrete recommendations of the article cannot be verified from the available material.

rss · SemiAnalysis · Sep 21, 18:14

**「Background」** Mixture-of-Experts \(MoE\) models are now widely used in frontier models and, according to SemiAnalysis, have changed both the structure of serving and the economics of useful inference—doing more than simply increasing parameter count. Prior work such as DeepSpeed-MoE has focused on advancing MoE inference and training for next-generation AI scale. The SemiAnalysis article examines how MoE models are mapped onto inference hardware, covering model structure, data movement, and efficient serving.

**「Impact」** Developers and platform teams serving Mixture-of-Experts models are the direct audience: the article&\#x27;s stated focus on structure, data movement, and efficient serving targets the memory-bandwidth limits and on-demand expert-weight streaming that dominate MoE inference cost when all experts cannot fit in fast GPU memory. Because only a title and one-line description were supplied, the concrete guidance and any performance claims the article makes cannot be verified from the available material.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/computation-and-data-movement-for">Computation and Data Movement for Inference</a></li>
<li><a href="https://www.alphaxiv.org/abs/2201.5596">DeepSpeed-MoE: Advancing Mixture - of - Experts Inference ... | alphaXiv</a></li>
<li><a href="https://arxiv.org/pdf/2201.05596">DeepSpeed-MoE: Advancing Mixture - of - Experts Inference</a></li>
<li><a href="https://www.kriraai.com/blog/mixture-of-experts-inference-latency">Mixture of Experts Inference Latency Using PEARL</a></li>

</ul>
</details>

**Tags**: `#mixture-of-experts`, `#inference`, `#hardware`, `#model-serving`, `#AI-systems`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [TGS2026 Interview: Dynasty Warriors 2 Remaster’s Classic-Modern Balance](https://www.gcores.com/articles/220015) ⭐️ 5.0/10

rss · 机核GCORES游戏资讯 · Sep 21, 13:35

**「Background」** At TGS 2026, the author played Dynasty Warriors 2 with Xtreme Legends Remaster and interviewed its producer. The challenge is modernizing controls, visuals, enemy counts, and combat while preserving the original, not remaking it.

**「Solution」** The producer insists it is a Remaster, not a Remake: a &quot;Classic&quot; mode restores many original behaviors, though he recommends keeping modern camera and all-direction guard because more on-screen enemies and aggressive soldiers would make rear attacks too punishing. To keep higher enemy counts from multiplying difficulty, the team adjusted soldier attack frequency and aggression, while officers telegraph powerful attacks as in Origins. Dying enemies can recover health or gain attack power and counter, so combat is less continuously mow-down; the producer says earlier entries already expected players to grow stronger before becoming overpowered. Weapon synthesis is optional, and balance was built as if it did not exist; unique-weapon conditions are shown in-game, but their difficulty stays faithful. Modern hardware raises on-screen soldiers beyond PS2&\#x27;s roughly 50 and extends draw distance beyond the original&\#x27;s roughly 50-100 meters. Local split-screen was retained after player feedback, online co-op remains undecided, and the new &quot;Nameless&quot; character uses a one-handed sword based on Origins. Character backgrounds were not heavily rewritten; only situational introductions were added, and the producer says he would rather make new Musou games than continue remasters.

**「Takeaway」** The remaster&\#x27;s thesis is to preserve the original&\#x27;s growth and difficulty identity while using optional modernization and careful rebalancing to keep it playable, rather than sanding it into a remake.

**Tags**: `#game-remaster`, `#game-design`, `#musou`, `#interview`, `#difficulty-balance`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Tariffs, fuel costs and rising rates squeeze US companies, CNBC reports](https://www.cnbc.com/2026/09/20/tariffs-fuel-prices-and-interest-rates-squeeze-us-companies.html) ⭐️ 7.0/10

CNBC reports that tariffs imposed under President Donald Trump&\#x27;s trade policies, surging fuel prices tied to the Iran war and rising interest rates are squeezing U.S. companies across manufacturing, logistics and retail, forcing executives to cut flights, hoard inventory or halt operations. At Iowa saw maker Original Saw Co., a small motor bracket more than doubled in price this summer, to $87 from $42, owner Allen Eden said, while auto parts maker Lucerne International stopped U.S. manufacturing and canceled a planned $50 million aluminum forging plant in Michigan.

rss · CNBC Finance · Sep 21, 15:04

**「Background」** The squeeze follows three converging shocks: tariffs imposed under President Donald Trump&\#x27;s trade policies, fuel costs driven up by the Iran war that began in late February 2026 \(oil rose from about $70 a barrel before the war to an average of $103 in March\), and the Federal Reserve&\#x27;s first interest-rate increase in three years, announced by new Chair Kevin Warsh to fight elevated inflation. Because fuel and raw materials feed directly into manufacturing and trucking, and rates raise the cost of financing inventory and equipment, capital-intensive sectors feel the pressure first.

**「Impact」** Smaller companies typically depend on shorter-term borrowing, so Federal Reserve rate hikes pass more directly into their costs, while capital-intensive manufacturers, trucking fleets and commercial real estate are most exposed to the combined rise in rates and fuel prices, according to JPMorgan Chase global strategy head Dubravko Lakos-Bujas.

<details><summary>References</summary>
<ul>
<li><a href="https://www.britannica.com/event/2026-Iran-war">2026 Iran war | Oil , Explained, United States, Israel, Strait... | Britannica</a></li>
<li><a href="https://www.pbs.org/video/rate-hike-1789591971/">PBS News Hour | Economist: Rate hike a reassuring sign Fed is...</a></li>

</ul>
</details>

**Tags**: `#tariffs`, `#interest rates`, `#inflation`, `#manufacturing`, `#supply chains`

---