---
layout: default
title: "Horizon Summary: 2026-08-20 (EN)"
date: 2026-08-20
lang: en
---

> From 155 items, 13 important content pieces were selected

---

**Technology News**
1. [GitHub Details August 17 Outage, Blames Retry Storms](#item-tech-news-1) ⭐️ 8.0/10
2. [AliExpress silent WebAudio fingerprinting breaks Bluetooth multipoint](#item-tech-news-2) ⭐️ 8.0/10
3. [Malicious arrayref crate runs build-time payload; Rust ecosystem responds](#item-tech-news-3) ⭐️ 8.0/10
4. [Bun 1.4 stable after Rust rewrite; Bun.WebView JSON API demo](#item-tech-news-4) ⭐️ 8.0/10
5. [Huzzah: A New Way to Code with AI Using Persistent Pseudocode](#item-tech-news-5) ⭐️ 7.0/10
6. [125M Transformer Autocompletes Piano in Real Time on iPhone](#item-tech-news-6) ⭐️ 7.0/10
7. [Linux 7.2 Release Announced by Igalia with Hardware Updates](#item-tech-news-7) ⭐️ 7.0/10
8. [Spectral Neuron: New ML Primitive for Scalable Interpretable Models](#item-tech-news-8) ⭐️ 7.0/10
9. [Entropic Scree: Information-Theoretic Rank Diagnostic for Complex Tabular Data](#item-tech-news-9) ⭐️ 7.0/10

**Technology Blog**
1. [Black Myth: Zhong Kui&\#x27;s Restrained PV and a Youth Before the Myth](#item-tech-blog-1) ⭐️ 7.0/10
2. [Steam Wallpaper Engine Workshop Hosts Large-Scale Malware Campaign](#item-tech-blog-2) ⭐️ 5.0/10

**Financial News**
1. [Midday Movers: Walmart Drops on Guidance, Deere Rises on Earnings Beat](#item-finance-news-1) ⭐️ 7.0/10
2. [Premarket movers: Walmart drops, crypto stocks rally, Alibaba profit slides](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [GitHub Details August 17 Outage, Blames Retry Storms](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) ⭐️ 8.0/10

GitHub published a postmortem of the August 17 outage that affected parts of GitHub and Copilot, attributing it to cascading failures and a client-side retry loop. Delayed replies to a single internal endpoint triggered a latent retry bug in VS Code that amplified traffic by approximately 10x and delayed recovery for the Copilot Token Service. The postmortem notes that monthly commits have grown from 1.4 billion in April to 2.9 billion, and outlines reliability work ahead. The incident highlights how retry storms can turn a small latency failure into a large-scale outage.

hackernews · 0xedb · Aug 20, 19:22 · [Discussion](https://news.ycombinator.com/item?id=49378957)

**「Background」** On August 17, GitHub experienced a major outage lasting 7 hours and 47 minutes, disrupting github.com, authentication, GitHub Actions, APIs, pull requests, issues, and Copilot for developers worldwide. The incident began with network saturation on load balancers in GitHub&\#x27;s Central US datacenter during a traffic peak, traced to an Istio sidecar pod that hit its concurrency limit and failed to autoscale correctly. This initial failure triggered client-side retry loops that amplified traffic by approximately 10x, delaying recovery for the Copilot Token Service and turning a contained issue into a cascading failure.

**「Impact」** For developers and organizations using GitHub and Copilot, the outage caused delayed recovery during the incident, and the postmortem&\#x27;s central lesson is that client-side retry logic must be carefully bounded to avoid amplifying traffic during recovery.

**「Community Discussion」** Commenters debated whether retries are appropriate for desktop-heavy services like GitHub, with some arguing that hiding errors behind endless retries leaves users staring at spinners. Others focused on the platform&\#x27;s rapid commit growth and the value of its free tier.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/">The August 17 outage, and the work ahead - The GitHub Blog</a></li>
<li><a href="https://www.statuscake.com/blog/what-broke-github-on-august-17-and-how-retries-made-the-incident-worse/">What Broke GitHub on August 17 and How Retries Made the Incident Worse</a></li>

</ul>
</details>

**Tags**: `#github`, `#postmortem`, `#reliability`, `#incident-response`, `#distributed-systems`

---

<a id="item-tech-news-2"></a>
### [AliExpress silent WebAudio fingerprinting breaks Bluetooth multipoint](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) ⭐️ 8.0/10

A blog post describes how AliExpress runs silent WebAudio fingerprinting, a privacy-invasive tracking technique that collects device identifiers from audio processing without playing audible sound. The fingerprinting inadvertently disrupts Bluetooth multipoint, causing side effects such as interference with hearing aids and car audio systems. The report highlights a novel consequence of silent audio fingerprinting: it changes the audio device environment in ways that can break normal Bluetooth multipoint operation. Because the technique operates below the audible threshold, browsers do not show the tab speaker indicator, making it invisible to users. The findings are relevant to web developers and privacy researchers concerned with browser-based tracking, though the evidence is mainly observational and lacks published performance data.

hackernews · emctech · Aug 20, 10:08 · [Discussion](https://news.ycombinator.com/item?id=49372583)

**「Background」** WebAudio is a browser API that lets websites synthesize and process audio; its output characteristics differ subtly between devices, so sites can use it to generate a fingerprint. AliExpress’s anti-abuse script creates hidden WebAudio graphs with zero gain that remain connected to the audio destination, holding the system audio path open. Because multipoint Bluetooth headphones rely on the audio path being free to switch between connected devices, this silent audio activity prevents them from switching away from the computer. Browsers have separately worked to limit AudioContext fingerprinting, such as Firefox’s resistFingerprinting efforts and the option to disable WebAudio entirely.

**「Impact」** Visitors using multipoint Bluetooth headphones can have audio routing disrupted by AliExpress&\#x27;s silent WebAudio fingerprinting scripts \(collina.js and fireyejs.js\), which create zero-gain audio graphs connected to the system destination; blocking these scripts with uBlock Origin restores normal headphone behavior.

**「Community Discussion」** Commenters connected the report to real-world Bluetooth and audio anomalies: one noticed hearing-aid amplification changes while browsing, another traced car-audio mis-triggering to a backgrounded AliExpress iOS app, and a third wished browsers would show a speaker indicator for silent audio. One commenter noted that Firefox has largely mitigated WebAudio fingerprinting, while another questioned whether Apple would remove AliExpress from the App Store under its closed-system security rationale.

<details><summary>References</summary>
<ul>
<li><a href="https://www.elseif.net/stories/aliexpress-runs-silent-webaudio-fingerprinting-that-breaks-bluetooth-m-4d2c69f">AliExpress silent WebAudio fingerprinting keeps Bluetooth ... — elseif</a></li>
<li><a href="https://www.drweb.de/webaudio-fingerprinting-aliexpress-bluetooth/">WebAudio - Fingerprinting : Wie erkennt AliExpress Ihr Gerät?</a></li>
<li><a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1708593">1708593 - Enhance resist fingerprinting: Disable web audio (API) by default when privacy.resistFingerprinting is enabled</a></li>
<li><a href="https://elsolitario.org/en/2026/08/20/aliexpress-webaudio-fingerprinting-bluetooth-en/">WebAudio Fingerprinting: The AliExpress Case - elsolitario.org</a></li>
<li><a href="https://zeli.app/en/story/49372583">AliExpress runs silent WebAudio fingerprinting that breaks ...</a></li>

</ul>
</details>

**Tags**: `#web-privacy`, `#fingerprinting`, `#webaudio`, `#browser-security`, `#tracking`

---

<a id="item-tech-news-3"></a>
### [Malicious arrayref crate runs build-time payload; Rust ecosystem responds](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) ⭐️ 8.0/10

A malicious version of the widely used Rust crate arrayref executes a build-time payload, marking a supply-chain security incident in the Rust ecosystem. The Rust project acknowledged the attack in a blog post dated August 20, 2026, and the issue is tracked in rustsec/advisory-db issue \#3161. The payload runs during the crate&\#x27;s build process, which can compromise developers who compile the affected version into their projects. Community members noted that the bad version disappeared from crates.io without an explicit yank marker or a visible security advisory, adding to concerns about registry incident response. The incident has renewed calls for build-script sandboxing in Cargo and for reducing reliance on large dependency trees.

hackernews · abhisek · Aug 20, 13:23 · [Discussion](https://news.ycombinator.com/item?id=49374269)

**「Background」** Rust crates are distributed through crates.io and commonly include build scripts or procedural macros that execute code on the developer&\#x27;s machine during compilation, which means updating a dependency can run arbitrary code at build time. Arrayref is a widely used crate for safely creating array references. In this incident, security researchers found that a compromised release of arrayref depended on a typosquatted proc-macro1 crate whose build script downloaded and ran a remote binary when compiled, leading the Rust team to delete the malicious releases.

**「Impact」** Developers who built Rust projects with affected arrayref, internment, or append-only-vec versions during the incident should treat their build environments as potentially compromised and scan caches for malicious crate files; the Rust Security Response Team removed the malicious version, unyanked affected legitimate versions, and locked the author&\#x27;s account, with pending RustSec advisories for the involved crates. 

**「Community Discussion」** Commenters criticized the incident response, saying GitHub effectively hid the repository and crates.io removed the bad version without a yank indication or advisory, suggesting the registry was unprepared for such an attack. Others argued for Cargo sandboxing of build scripts and for more robust standard libraries to reduce dependency counts, with one commenter comparing the situation to the JavaScript ecosystem&\#x27;s supply-chain risks.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html">Rust Supply Chain Attack Puts Build-Time Malware in Crates ...</a></li>
<li><a href="https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/">Malicious Rust Crate arrayref Runs a Build-Time Payload</a></li>
<li><a href="https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/">Supply chain attack on arrayref | Rust Blog</a></li>
<li><a href="https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack">Rust Supply-Chain Attack: arrayref, internment, and append-only-vec Poisoned by the proc-macro1 Build-Time Dropper - StepSecurity</a></li>
<li><a href="https://www.linuxcompatible.org/story/rust-supply-chain-attack-malicious-arrayref-crate-pulled-after-2hour-breach">Rust Supply Chain Attack: Malicious arrayref Crate Pulled After 2-Hour Breach</a></li>

</ul>
</details>

**Tags**: `#rust`, `#security`, `#supply-chain`, `#malware`, `#crates.io`

---

<a id="item-tech-news-4"></a>
### [Bun 1.4 stable after Rust rewrite; Bun.WebView JSON API demo](https://simonwillison.net/2026/Aug/20/bun-webview-json-api/) ⭐️ 8.0/10

Bun 1.4 was released today as the first stable version since its Rust rewrite, adding over 2,900 bug fixes and 1,517 tests from the Node.js test suite. The release reduces idle CPU usage by 5x, cuts memory usage by up to 35%, and starts 50% faster on Linux. New features include Bun.Image, Bun.WebView, Bun.markdown, Bun.cron\(\), Bun.Terminal, bun run --parallel, bun test --parallel, bun audit fix, bun dedupe, and bun prune. Bun.WebView provides first-class browser automation via macOS WebKit or local Chromium over the Chrome DevTools Protocol \(CDP\). Simon Willison built a shot-scraper-style JSON API on Bun.WebView, and its prototype server needs a 192MB-256MB container to run full Chrome against complex web pages.

rss · Simon Willison · Aug 20, 15:37

**「Background」** Bun is a JavaScript runtime, bundler, and package manager, while shot-scraper is a CLI tool for taking screenshots and executing JavaScript against web pages. Bun.WebView extends this capability by embedding browser automation directly into the Bun runtime, supporting both macOS WebKit and Chromium via CDP, so developers can build browser-driven services without separate driver installations.

**「Impact」** Developers can now build browser automation and JavaScript-execution APIs using Bun core with less overhead than traditional standalone browser drivers, and the demonstration indicates such a service can operate in a 192-256MB container when using Chromium.

**Tags**: `#bun`, `#webview`, `#json-api`, `#javascript`, `#rust`, `#web-development`

---

<a id="item-tech-news-5"></a>
### [Huzzah: A New Way to Code with AI Using Persistent Pseudocode](https://www.danielvaughn.dev/posts/huzzah/) ⭐️ 7.0/10

Huzzah is a proof-of-concept editor by danielvaughn that lets developers write pseudocode, synchronizes it to real source code on save, and persists the pseudocode as a stored record of intent. The author built it after working with coding agents almost exclusively since January, finding it increasingly tedious to write full sentences for every change and noticing a complexity limit beyond which agents begin confusing themselves. The workflow is to write pseudocode in whatever way makes sense to the user, save, and have the editor generate corresponding source code while keeping the pseudocode alongside it as intent documentation. Installation instructions are available in the GitHub readme, and a video demonstration was shared on X. Huzzah is experimental, and the author notes it may not work for every use case.

hackernews · danielvaughn · Aug 20, 19:05 · [Discussion](https://news.ycombinator.com/item?id=49378768)

**「Background」** Coding agents are AI tools that accept natural-language instructions and generate or modify source code. While they speed up individual changes, developers often must write long prompts for each edit, and larger codebases can overwhelm the agent&\#x27;s understanding. Huzzah explores a different interaction paradigm: instead of continuously prompting in English, the developer writes pseudocode that is compiled into real code, with the pseudocode preserved as a human-readable record of intent.

**「Impact」** For developers experimenting with AI-assisted programming, Huzzah demonstrates a workflow in which pseudocode becomes the primary interface for generating code, with the generated source kept in sync and the pseudocode retained for future changes. Its immediate practical effect is limited to the author&\#x27;s proof-of-concept, but it offers a concrete alternative to full-sentence prompting for anyone who wants to try it.

**「Community discussion」** Commenters generally welcomed the experiment and connected it to a shared challenge: finding the right abstraction level between verbose prompting and direct IDE editing. One commenter disagreed with the premise, arguing that fatigue with agents comes from delegating thinking rather than writing English, while another proposed the more important direction is decomposing existing complex codebases into editable pseudocode.

**Tags**: `#AI coding`, `#pseudocode`, `#developer tools`, `#human-AI interaction`, `#editor`

---

<a id="item-tech-news-6"></a>
### [125M Transformer Autocompletes Piano in Real Time on iPhone](https://simedw.com/2026/08/20/midi-autocomplete/) ⭐️ 7.0/10

The author trained a 125M-parameter transformer to autocomplete piano performances in real time on an iPhone, and released the app as a free download. Like Copilot for code, the model takes a few MIDI notes as a prompt and continues the performance entirely on-device. The author reports the model runs at roughly 108 notes per second on an iPhone 15 and shares training and Core ML details alongside the many failed approaches. The project demonstrates viable on-device music generation and is presented as an early experiment rather than a completed product.

hackernews · simedw · Aug 20, 12:04 · [Discussion](https://news.ycombinator.com/item?id=49373456)

**「Background」** This item relies on the idea of sequence autocomplete, popularized by tools such as GitHub Copilot, applied to MIDI piano input. MIDI represents notes digitally, allowing keyboard performances to be tokenized and predicted by a transformer, while Core ML is Apple&\#x27;s framework for running models locally on iPhone hardware. Training a 125M-parameter model to run in real time on-device requires trade-offs between model size, quantization, and latency.

**「Impact」** Musicians with an iPhone can try a free app that continues their playing locally in real time, and developers get a concrete example of optimizing a 125M-parameter transformer for Core ML on consumer hardware.

**「Community Discussion」** Commenters were largely positive, comparing the concept to classical composition training and modern AI design tools, though one listener found familiar melodies diverging into unexpected directions disconcerting. A user also asked for details about training dataset size, which the post did not mention in the supplied text.

**Tags**: `#machine-learning`, `#music-generation`, `#transformer`, `#core-ml`, `#on-device-ai`

---

<a id="item-tech-news-7"></a>
### [Linux 7.2 Release Announced by Igalia with Hardware Updates](https://www.igalia.com/2026/08/19/Linux-72-Released.html) ⭐️ 7.0/10

Igalia announced the Linux 7.2 kernel release on August 19, 2026, presenting it as a regular milestone in the open-source kernel&\#x27;s development cycle. The release focuses on hardware enablement and driver updates rather than a major architectural shift, with community attention centering on improved HDMI 2.1 support and Raspberry Pi-related changes. Linux 7.2 continues the kernel&\#x27;s incremental release pattern, so most users can expect broad compatibility gains rather than a headline feature. The announcement generated discussion about display connectivity and single-board-computer adoption, though specific technical details in the available excerpt were limited.

hackernews · mariuz · Aug 20, 15:46 · [Discussion](https://news.ycombinator.com/item?id=49376265)

**「Background」** HDMI 2.1&\#x27;s higher bandwidth relies on Fixed Rate Link \(FRL\) signaling, and for years the AMD open-source driver could not implement it because the HDMI Forum restricted open-source use of the specification. Linux kernel 7.2 changes that by adding initial AMDGPU HDMI 2.1 FRL support for modern Radeon GPUs, though it is not enabled by default yet. This release also brings other hardware and power-management improvements, such as a new AMDGPU DC power module, and is part of the ongoing kernel release cycle that distributions like Manjaro are integrating.

**「Impact」** The most concrete consequence is that Raspberry Pi 4 owners have a reason to update their kernel, while desktop users remain uncertain about whether HDMI 2.1 support is now fully enabled on Linux.

**「Community discussion」** Commenters were generally receptive, with one Raspberry Pi 4 owner eager to update, but key questions remained unresolved: whether HDMI 2.1 support had been unblocked for AMD&\#x27;s open-source driver and why a user would choose HDMI over DisplayPort on desktop monitors. Another commenter asked how this release compares with LWN&\#x27;s coverage, suggesting the official announcement may not be the most detailed source.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeky-gadgets.com/linux-7-2-kernel-updates/">Linux 7.2 Release Features and Manjaro 26.1 Updates - Geeky Gadgets</a></li>
<li><a href="https://ubuntuhandbook.org/index.php/2026/08/linux-kernel-7-2-released-with-amdgpu-hdmi-2-1-frl-support/">Linux Kernel 7.2 Released with AMDGPU HDMI 2.1 FRL Support</a></li>

</ul>
</details>

**Tags**: `#linux`, `#kernel`, `#open source`, `#hardware support`, `#release`

---

<a id="item-tech-news-8"></a>
### [Spectral Neuron: New ML Primitive for Scalable Interpretable Models](https://www.reddit.com/r/MachineLearning/comments/1vtfimo/the_spectral_neuron_an_ml_primitive_for_scalable/) ⭐️ 7.0/10

The Spectral Neuron is a newly proposed machine learning primitive defined by models of the form f\(x\) = λ\_k\(A0 + Σᵢ xᵢAᵢ\), designed to combine scalability, interpretability, and controllability. The author, who previously worked on an ad team at Yahoo, presents the approach in a preprint on arXiv \(2608.08003\) and provides open-source code on GitHub. The work develops mathematical properties of the model as matrices grow, details what can be read from learned matrices, guarantees certain shapes by construction, and offers a practical initialization and training recipe. Scaling experiments are reported on both synthetic and real data, with the author noting that while the manuscript was written by them with AI assistance for literature review, the code was heavily AI-written and reviewed by them.

reddit · r/MachineLearning · /u/alexsht1 · Aug 20, 10:20

**「Background」** In machine learning, simple and interpretable models are often favored for their transparency and control, but they can lack the expressive power needed for complex tasks. Spectral methods use eigenvalues and eigenvectors of matrices to analyze or transform data, providing a mathematical framework for studying linear operators. This work introduces a primitive that leverages matrix-valued parameters to achieve a balance between simplicity and expressiveness, building on earlier blog posts and the author&\#x27;s experience in applied ML settings.

**「Impact」** Machine learning researchers and practitioners seeking interpretable yet scalable models can now evaluate the Spectral Neuron through its available code and empirical scaling tests, though its practical benefits remain unverified outside the author&\#x27;s own experiments. This introduces a new primitive that may inspire further work on matrix-based model architectures, but independent validation is still needed.

**Tags**: `#machine learning`, `#spectral methods`, `#interpretability`, `#scalable models`, `#research`

---

<a id="item-tech-news-9"></a>
### [Entropic Scree: Information-Theoretic Rank Diagnostic for Complex Tabular Data](https://www.reddit.com/r/MachineLearning/comments/1vtjotb/mapping_intrinsic_rank_and_informational_gravity/) ⭐️ 7.0/10

A Reddit user introduced Entropic Scree, a non-parametric, model-agnostic information-theoretic diagnostic for estimating intrinsic rank and dependency structure in complex tabular data, with a preprint \(doi:10.5281/zenodo.22028087\) and open-source code on GitHub. The method replaces linear covariance and Euclidean distances with normalized mutual information and information-theoretic Jaccard/Variation-of-Information similarities, aiming to avoid what the author describes as PCA&\#x27;s &\#x27;dimensional inflation&\#x27; and Kernel PCA&\#x27;s structural collapse on entangled or sparse data. In a synthetic stress test with 20 generative roots expanded into 5th-order combinations across 20,000 proxies but only 10,000 samples, the author reports that standard PCA falsely extracted about 5,700 dimensions, Kernel PCA and Spearman rank overestimated rank by 100%, while Entropic Scree recovered exactly 20 intrinsic dimensions and identified 1.45% shared signal versus 98.55% idiosyncratic noise. The framework also introduces &\#x27;Informational Gravity&\#x27; factors \(AIG/FSIG\) to interpret the topology of extracted roots, for example a primary factor equivalent to about 74.5 variables followed by a plateau of roughly 11.5 variable-equivalents each. This is a substantive but not yet peer-reviewed or independently verified contribution.

reddit · r/MachineLearning · /u/Chocolate\_Milk\_Son · Aug 20, 13:34

**「Background」** Intrinsic dimensionality estimation attempts to find the true number of underlying generative variables in a dataset, often using PCA, kernel PCA, or Euclidean nearest-neighbor estimators. PCA relies on linear covariance, so non-linear interactions can appear as additional orthogonal dimensions, while kernel PCA in infinite-dimensional Hilbert spaces can smear sparse noise into elevated tails, and Euclidean methods suffer distance concentration when the number of features exceeds the number of samples. Entropic Scree is proposed as an alternative that measures shared probability mass via Shannon entropy, making it invariant to mixed variable types and capable of bypassing the algebraic N-1 rank ceiling of PCA.

**「Impact」** If validated, the method gives practitioners analyzing sample-starved, highly non-linear tabular datasets a principled way to size autoencoder bottlenecks and separate signal from noise without relying on metric assumptions. Until independent replication or peer review, users should treat the reported exact rank recovery on synthetic data as preliminary evidence rather than a proven guarantee.

**Tags**: `#intrinsic dimensionality`, `#information theory`, `#tabular data`, `#dimensionality reduction`, `#open source`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Black Myth: Zhong Kui&\#x27;s Restrained PV and a Youth Before the Myth](https://www.gcores.com/articles/218610) ⭐️ 7.0/10

rss · 机核GCORES游戏资讯 · Aug 20, 12:00

**「Background」** After Black Myth: Wukong proved that Chinese mythology could be turned into a world-class action game, Game Science returned with a 15-minute PV for Black Myth: Zhong Kui. This time the team deliberately hides its virtuosity, a stance the author calls “cangfeng,” or sheathing the blade, presenting a ragged young Daoist wandering an overcast, rainy world.

**「Solution」** The author reads the PV as technical and narrative restraint. Overcast lighting is the hardest environment to render because materials cannot be hidden by darkness or cleaned by strong light; footage of footstep splashes, submersion, and seamless transitions between water and land creates an almost documentary realism. Combat also shifts from Wukong&\#x27;s single-target showcases to multi-enemy engagements, with explicit feedback for block, parry, dodge, and perfect dodge. Narratively, the game chooses Zhong Kui before he became the red-robed door god. Drawing on historical and folkloric evidence, the author argues that Zhong Kui was a failed examinee, an undignified ghost-catcher, and arguably a “position” rather than a person. He connects the sword and talisman to Taoist ritual—iron swords for slaying, thunder-struck wood for summoning thunder, peach wood for warding—and surveys regional customs from Anhui dances to Taiwan rituals to support the idea that a young Zhong Kui can act as a vessel for local folklore. The open-world hints in the PV are frankly speculative, and the author hopes for a semi-open structure of narrative-dense nodes rather than a sprawling map.

**「Takeaway」** The author&\#x27;s central point is that Zhong Kui is a human-god intersection whose narrow, vertical calling—handling concrete injustices—makes him a natural game protagonist. Unlike Wukong&\#x27;s need to prove capability, this restrained PV suggests the studio is competing only with itself, asking whether it can do even better.

**Tags**: `#game design`, `#rendering`, `#Chinese mythology`, `#Black Myth`, `#cultural analysis`

---

<a id="item-tech-blog-2"></a>
### [Steam Wallpaper Engine Workshop Hosts Large-Scale Malware Campaign](https://www.gcores.com/articles/218568) ⭐️ 5.0/10

rss · 机核GCORES游戏资讯 · Aug 20, 01:45

**「Background」** Kaspersky has warned that attackers are again using Steam&\#x27;s popular Wallpaper Engine software to spread malware. By compromising users&\#x27; Steam clients and stealing account credentials, the attackers make the in-client warnings and support messages unreliable.

**「Solution」** The author reports that hackers embed malicious code in animated wallpapers uploaded to the Steam Workshop; after installation and execution, the code silently activates in the background. Researchers found dozens of malicious wallpapers, some with tens of thousands of downloads, with victims concentrated in China at 89% of malicious download attempts and Russia at 5.5%. The analyzed samples deploy a backdoor called Synaptics.exe and replace the system&\#x27;s AggregatorHost.dll to locate Steam, steal credentials, and hijack login sessions, then use the victim&\#x27;s account to upload more malicious wallpapers and propagate the infection. The malware includes families such as DarkKomet, Lumma, Vidar, and RenEngine, suggesting multiple independent attackers. Once account access is obtained, victims may receive fake red letters and &\#x27;live support&\#x27; messages inside Steam; the author stresses that official support only communicates through website tickets and never requests inventory transfers or payments. Kaspersky advises affected users to review authorized devices in Steam settings, revoke unrecognized permissions, check for unauthorized Web API keys, and run a full antivirus scan after removing unknown wallpapers.

**「Takeaway」** The article&\#x27;s central warning is that credential-stealing malware in this ecosystem turns the trusted Steam client interface into a channel for scams, so users must treat in-client communications and unfamiliar workshop content with caution. The report is a practical alert rather than deep technical analysis, but it emphasizes auditing account access and cleaning local files as critical responses.

**Tags**: `#Steam`, `#Wallpaper Engine`, `#malware`, `#security`, `#Kaspersky`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Midday Movers: Walmart Drops on Guidance, Deere Rises on Earnings Beat](https://www.cnbc.com/2026/08/20/stocks-making-the-biggest-moves-midday-wmt-de-crwd-mrna-more.html) ⭐️ 7.0/10

Quarterly earnings reports and President Donald Trump’s push for crypto-friendly legislation drove sharp midday moves: Walmart fell 9% after sales at stores open at least a year grew 2.6%, below the 3.5% FactSet consensus, while Deere rose nearly 9% after beating fiscal third-quarter profit and revenue estimates and lifting its full-year net income outlook. Moderna plunged 25% a day after jumping 177% on promising skin-cancer vaccine trial data.

rss · CNBC Finance · Aug 20, 20:43

**「Background」** The moves came as investors sorted through a batch of quarterly reports and responded to President Donald Trump’s call for Congress to pass crypto-friendly legislation.

**Tags**: `#earnings`, `#stock movers`, `#retail`, `#crypto`, `#guidance`

---

<a id="item-finance-news-2"></a>
### [Premarket movers: Walmart drops, crypto stocks rally, Alibaba profit slides](https://www.cnbc.com/2026/08/20/stocks-making-the-biggest-moves-premarket-.html) ⭐️ 7.0/10

Walmart fell 6% in premarket trading after its second-quarter U.S. comparable sales rose 2.6%, below the 3.5% analysts expected, and its fiscal third-quarter and full-year earnings guidance missed forecasts. Crypto-related stocks rose after President Donald Trump called for Congress to pass crypto-friendly legislation, with Coinbase up nearly 7% and Strategy up 10%.

rss · CNBC Finance · Aug 20, 12:24

**「Background」** Moderna shed 7% a day after gaining 177% on promising late-stage trial results for its cancer vaccine, and Alibaba reported a 75% drop in June-quarter profit because of higher artificial intelligence spending.

**Tags**: `#Walmart`, `#Alibaba`, `#Crypto stocks`, `#Moderna`, `#Earnings`

---