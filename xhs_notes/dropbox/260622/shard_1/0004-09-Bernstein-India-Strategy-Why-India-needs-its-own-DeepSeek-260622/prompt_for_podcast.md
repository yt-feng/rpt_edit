你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
India Strategy

# India Strategy: Why India needs its own DeepSeek

![](images/79a87c4711e79e20d410b3d0cd6bdf9934a5e40d1fcd7664f2e3d428525d638a.jpg)  
Venugopal Garre

+65 6326 7643

venugopal.garre@bernsteinsg.com

![](images/b2d4140e693072e7596790dd4906c4df1d013f7fd064d3396383023f05cd6169.jpg)

Nikhil Arela

+91 226 842 1482

nikhil.arela@bernsteinsg.com

India can't build its AI future on borrowed models. While renting compute to power foreign LLMs may look like progress, it leaves the country dependent. The recent US restrictions on access to the latest AI model for non-citizens drive home the risk that India could find itself locked out some day, with its applications trailing those in the US and China. We had raised this topic even earlier but were muffled with noises of “LLM does not matter”. But the recent development compels us to have a relook.

AI is the next ‘fighter jet’: Technology access has been rationed and controlled in the past, and a trend emerging in last few years is shattering the “Global” image of AI. It started with critical minerals & semiconductors equipment, moved to GPUs and now exhibits itself in the form of restricted frontier models. The recent ban on Anthropic’s latest models for non-US citizens confirms that it’s no longer an anomaly. As AI moves from a mere commodity to a tool of strategic importance, one thing is clear: foundational models will no longer be SaaS products, they would rather be critical resources, becoming the “fighter jets” of an era where bleeding-edge models will be guardrailed. This will only aggravate further, with deep implications for India currently trying to convince itself that applications built on foreign LLMs and earning rent on datacentres is a sound AI strategy. To be clear, we are not dismissing this approach. There is value in participating in the ecosystem through infrastructure build-out and application layers. But at the very least, India needs to be aware about the risks embedded in effectively outsourcing the core AI models.

Why doesn't India have its own large-scale LLM? It may be counterintuitive that despite being the source of vast data, which is virtually the fuel to train global models, India itself hasn't harnessed this advantage to build competitive GenAI systems at global scale. This absence of an India “DeepSeek moment” is structural rather than a thought out strategy. India's tech ecosystem has long been services-led, with sparse consumer-facing platforms in areas like search, social media or messaging—domains that typically generate the rich, organized datasets critical for training advanced AI. The lack of such data ecosystems has never necessitated the development of talent pipelines and academic depth to build foundational models. The IT services model, where low cost labor effectively fine-tunes software built by global giants, further adds to the baggage of sticking to application layer. Heads of many leading Institutions have argued that India does not need its LLMs, but can focus on AI applications. These views are more reflective of the path India has taken to stand where it is today, rather than a deliberate strategic choice.

Can India afford its AI stack at the mercy of someone else? Let's picture this: India's core intelligence layer, from enterprise software to defence and space could be powered by foreign LLMs. Enter a geopolitical disruption, and that access could be curtailed overnight, bringing critical applications to a halt. A more likely outcome is subtler but equally concerning: India operates one or two generations behind. Applications built on older models struggle to compete with global offerings. An Indian IT giant with talent at its disposal could lose out to a young US SaaS firm bootstrapped by amateur coders having access to cutting-edge models. There is, however, a path that looks more resilient —building domain-specific LLMs on proprietary data and layering AI solutions on top. The real vulnerability lies with large-scale, horizontal GenAI applications built on external models....continued on page 2

## DETAILS

...continued from page 1. Framing India's AI Policy Choices: The solution set is not easy for policymakers. Ideas such as ringfencing AI for domestic firms (which we have given in the past) may lack practicality in a globally integrated technology landscape. That said, two strategic levers stand out. One approach is to restrict or pace access to global AI models, while channeling significant capital and talent into building India-native LLM capabilities. The other is to mandate or incentivize localization—requiring foreign firms to build and operate India-based AI stacks that are insulated from geopolitical controls. Both options are imperfect, but they frame the core policy trade-off between access and autonomy.

## INDIA'S TECH DEPENDENCE

For years, India's relationship with technology has followed a familiar script. Build locally where possible, but rely on global giants where it matters. The internet era was perhaps the clearest example. While China built walls and created large scale platforms that have provided it cash flows, talent pools and data to build AI models, India stayed open, and global platforms quietly became the rails on which its digital economy runs.

But here's the catch. What started as a story of internet dependence is, in reality, much bigger. Step back and look at the full stack. From hardware and core IT components to operating systems and enterprise software, India sits downstream across almost every layer. Exhibit 1 and Exhibit 2 make this stark. This is not just about apps or platforms; it is about systemic dependence. And overwhelmingly, that dependence points in one direction: the US. There have been attempts by Indian companies to break through in pockets, to build credible vertical platforms, but most have struggled to scale, out-competed by global incumbents with deeper moats, better products, and capital at scale.

Which brings us to today, and to AI. If history is any guide, the path forward seems obvious. Why fight it? Why not allow the same playbook to repeat, with global companies building, owning, and monetizing India's AI layer while domestic players participate on the margins? And yet, something feels different this time. AI is not just another application layer. It is emerging as the underlying rail for everything from enterprise workflows to consumer interactions. Importantly, it is still early. Unlike past technology cycles where India entered late, this is a moment where the contours are still being shaped. That is what is triggering the current debate around a sovereign AI stack. Not because India has suddenly discovered technological self-reliance, but because the cost of missing this wave could be far higher. Waiting 20–30 years, as India effectively did in earlier tech cycles, could entrench dependence in ways that are far harder to reverse, locking in value capture outside the country for decades.

But here lies the dilemma. Recognizing the importance of sovereignty is one thing; executing on it is another. The policy levers are limited, the competitive gap is large, and the alternatives outlined in our framework are far from straightforward. India may not dominate the core AI stack, but the choices it makes now will determine where value pools emerge, who captures them, and whether the next decade of AI-led growth deepens dependence or begins to rebalance it. The debate on LLMs, therefore, is not just a technology discussion. It is an early signal of how India intends to position itself in the AI economy. And this time, the decision cannot be deferred.

We believe India's real opportunity lies in owning and leveraging its rich, domain-specific datasets, especially across sectors like Industrials and healthcare. These datasets can become the foundation for building defensible, smaller, specialized LLMs by Indian technology companies, on top of which a wide range of applications can be developed. Importantly, these applications need not be confined to the digital world. They can extend into the physical economy as well, powering use cases such as training industrial robots, including next-generation humanoid systems where perhaps the Industrial context specific data set is more critical than the use of the latest Gen AI model and where older gen AI models may also work. The opportunity is, therefore, not just in software, but in shaping how AI integrates with real-world assets and workflows.

The core idea is simple but powerful: retain and control access to high-quality, hard-to-replicate vertical data. By limiting unrestricted access to such datasets for global platforms, India can create pockets of defensibility where domestic players can build meaningful capabilities. Over time, these can evolve into scalable solutions within India, and eventually be exported as global offerings. Realistically, this path may not produce trillion-dollar tech giants in the near term. But that is not the only metric of success. Even a shift toward building credible, globally relevant platforms anchored in proprietary data would expand India's share of value creation beyond IT services, and gradually reposition it within the global tech ecosystem. More importantly, it sets the foundation for the future. As talent and capital begin to recognize the viability of an India-led tech stack, it could trigger a virtuous cycle—one where the next generation of entrepreneurs builds not just for India, but from India.

EXHIBIT 1: India's tech dependence

<table><tr><td>Area</td><td>Main companies India depends on</td><td>Country of origin</td><td>Indian providers / initiatives</td></tr><tr><td colspan="4">Core compute: CPUs, GPUs, chipsets</td></tr><tr><td>PC/server CPUs</td><td>Intel, AMD</td><td>Intel: US; AMD: US</td><td>CDAC&#x27;s ARM designs for niche HPC; no mass CPU yet</td></tr><tr><td>Mobile SoCs</td><td>Qualcomm, MediaTek, Apple (A-series), Samsung Exynos</td><td>US; Taiwan; US; South Korea</td><td>Jio/Reliance design efforts (limited), none at scale</td></tr><tr><td>AI NPUs / accelerators</td><td>NVIDIA, AMD, Google TPU (cloud), Intel Gaudi</td><td>US; US; US; US</td><td>None in production; early RISC-V and fabless efforts</td></tr><tr><td>GPUs (datacenter/client)</td><td>NVIDIA, AMD</td><td>US; US</td><td>None meaningful; India is a GPU consumer onlyinstagram</td></tr><tr><td>Memory (DRAM, NAND)</td><td>Samsung, SK Hynix, Micron</td><td>South Korea; South Korea; US</td><td>No large domestic DRAM/NAND makers</td></tr><tr><td>Storage controllers, SSDs</td><td>Samsung, Western Digital, Seagate, Kioxia</td><td>KR; US; US; Japan</td><td>Only assembly/integration by Indian system integrators</td></tr><tr><td colspan="4">Operating systems (PC, mobile, server)</td></tr><tr><td>Desktop / laptop OS</td><td>Microsoft Windows (dominant), Apple macOS, desktop Linux</td><td>US; US; global OSS</td><td>Maya OS (Govt Linux-based for defence)facebook</td></tr><tr><td>Mobile OS</td><td>Google Android (incl. OEM skins), Apple iOS</td><td>US; US</td><td>BharatOS / homegrown Android forks (small share)</td></tr><tr><td>Server OS</td><td>Linux distros (Red Hat, Ubuntu, etc.), Windows Server</td><td>US/UK; US; others</td><td>Local Linux customizations in govt/PSUs</td></tr><tr><td colspan="4">Desktop productivity, content creation, key software</td></tr><tr><td>Office suites</td><td>Microsoft 365/Office</td><td>US</td><td>Zoho Workplace (Zoho, India); LibreOffice (OSS)</td></tr><tr><td>PDF tools</td><td>Adobe Acrobat</td><td>US</td><td>Small Indian PDF tools; none at Adobe&#x27;s scale</td></tr><tr><td>Creative suite (photo, video, design)</td><td>Adobe Creative Cloud, Corel, Autodesk</td><td>US; Canada; US</td><td>Inkscape, GIMP (OSS); few Indian pro-grade suites</td></tr><tr><td>IDEs &amp; dev tools</td><td>Microsoft (VS, VS Code), JetBrains, open-source tools</td><td>US; Czech/Netherlands</td><td>Indian plugin/tool vendors; core IDEs foreign</td></tr><tr><td>Browsers</td><td>Google Chrome, Apple Safari, Microsoft Edge, Firefox</td><td>US; US; US; US</td><td>Indian Chromium forks possible; no large consumer brand</td></tr><tr><td colspan="4">Enterprise applications: ERP, accounting, CRM</td></tr><tr><td>Large-enterprise ERP</td><td>SAP, Oracle, Microsoft Dynamics, Infor, Sage</td><td>Germany; US; US; US; UK</td><td>Ramco Systems, Tally Solutions, Focus Softnet, Bsquare Pothera ERP</td></tr><tr><td>SME accounting / ERP</td><td>Tally (very dominant), Zoho Books, QuickBook</td><td>India; India; US</td><td>Tally Solutions (India), Zoho (India)</td></tr><tr><td>CRM / SaaS business apps</td><td>Salesforce, Microsoft, HubSpot, SAP, Oracle</td><td>US; US; US; Germany; US</td><td>Zoho CRM (India), Freshworks (Freshdesk, etc.), LeadSquared</td></tr><tr><td>HR / payroll</td><td>SAP SuccessFactors, Oracle HCM, Workday</td><td>Germany; US; US</td><td>Darwinbox, Keka, GreytHR (India)</td></tr><tr><td colspan="4">PCs, laptops, and other client hardware</td></tr><tr><td>Laptops / PCs</td><td>HP, Dell, Lenovo, Acer, Asus, Apple</td><td>US; US; China; Taiwan; Taiwan; US</td><td>HCL (legacy PCs), Reliance, Lava, Dixon assembling for brands</td></tr><tr><td>PC components</td><td>Motherboards, GPUs, RAM, SSDs from global brands (ASUS, Gigabyte, MSI, etc.)</td><td>Taiwan; Taiwan; Taiwan</td><td>No major Indian component brands; mostly import-dependent</td></tr><tr><td>Monitors</td><td>Samsung, LG, Dell, HP</td><td>KR; KR; US; US</td><td>A few Indian labels (e.g. Intex, Zebronics) using imported panels</td></tr></table>

MediaTek, Samsung, SK Hynix, Micron and Kioxia are covered by Mark Li; Microsoft, Adobe, SAP, Oracle, Salesforce, HubSpot and Workday are covered by Mark Moerdler; Apple, Western Digital, Seagate, HP and Dell are covered by Mark Newman; Alphabet (owns Android, Chrome) is covered by Mark Shmulik; Sage is covered by Richard Nguyen; Intel, AMD, Qualcomm and Nvidia are covered by Stacy Rasgon

Lenovo, Acer, Asus, Gigabyte, MSI, LG Electronics, Reliance, Ramco Systems, HCL Tech and Freshworks are not covered

Remaining companies are unlisted

Source: Company Data, Bernstein Analysis

EXHIBIT 2: India's tech dependence

<table><tr><td>Area</td><td>Main companies India depends on</td><td>Country of origin</td><td>Indian providers / initiatives</td></tr><tr><td colspan="4">Smartphones, feature phones, and mobile hardware</td></tr><tr><td>Smartphones (brands)</td><td>Samsung, Xiaomi, Vivo, Oppo, Apple, OnePlus, Motorola</td><td>KR; China; China; China; US; China; US</td><td>Lava, Micromax (smaller), JioPhone (Reliance), Karbonn</td></tr><tr><td>ODM / manufacturing</td><td>Chinese/Taiwanese ODMs; Foxconn, Wistron, Pegatron, etc.</td><td>Taiwan; Taiwan; Taiwan</td><td>Dixon, local EMS units under PLI schemes</td></tr><tr><td>Modems / RF chips</td><td>Qualcomm, MediaTek, UNISOC</td><td>US; Taiwan; China</td><td>No domestic RF baseband vendor</td></tr><tr><td>Displays &amp; batteries</td><td>Samsung, LG, BOE, CATL, others</td><td>KR; KR; China; China</td><td>Limited local battery assembly, cells largely imported</td></tr><tr><td colspan="4">Telecom networks and equipment</td></tr><tr><td>Mobile RAN &amp; core</td><td>Ericsson, Nokia, Huawei (historically), ZTE, Cisco</td><td>Sweden; Finland; China; China; US</td><td>Tejas Networks, HFCL, ITI, C-DOT-aligned vendors</td></tr><tr><td>Transmission &amp; fiber</td><td>Nokia, Ericsson, Huawei; global fiber makers</td><td>Finland; Sweden; China</td><td>HFCL, Sterlite Technologies (STL) for fiber and some gear</td></tr><tr><td>Tower infra</td><td>American Tower, global OEMs for gear</td><td>US, others</td><td>Indus Towers (India), Bharti Infratel (now merged)</td></tr><tr><td>Routers/switches (IP)</td><td>Cisco, Juniper, Huawei, Nokia</td><td>US; US; China; Finland</td><td>Some L2/L3 switches by Indian OEMs; not yet at Tier-1 scale</td></tr><tr><td colspan="4">Cloud, hyperscale, and developer platforms</td></tr><tr><td>Public cloud IaaS/PaaS</td><td>AWS, Microsoft Azure, Google Cloud</td><td>US</td><td>Niche Indian DC/cloud providers (CtrlS, ESDS, Krutrim)</td></tr><tr><td>SaaS productivity</td><td>Microsoft 365, Google Workspace, Zoom, Slack</td><td>US</td><td>Zoho suite (India), Flock (India)</td></tr><tr><td>Code hosting</td><td>GitHub, GitLab,</td><td>US</td><td>Few Indian Git alternatives; minor adoption</td></tr><tr><td colspan="4">Social media, messaging, consumer internet</td></tr><tr><td>Social media</td><td>Meta (Facebook, Instagram), X (Twitter), LinkedIn</td><td>US</td><td>ShareChat, Koo, Josh (short video)</td></tr><tr><td>Video streaming</td><td>YouTube, Netflix, Amazon Prime Video, Disney+ Hotstar</td><td>US</td><td>JioCinema, SonyLIV, Zee5</td></tr><tr><td>Messaging apps</td><td>WhatsApp, Telegram, Signal, iMessage</td><td>US; UAE/Cyprus; US; US</td><td>Hike (pivoted), JioChat; limited scale now</td></tr><tr><td>E-commerce</td><td>Amazon, Walmart/Flipkart</td><td>US</td><td>Reliance JioMart, Tata Neu, Snapdeal</td></tr><tr><td>Payments / UPI</td><td>Google Pay, PhonePe (Walmart-backed), Paytm</td><td>US; US; India</td><td>Paytm (India), many Indian UPI apps</td></tr><tr><td colspan="4">Peripherals and other PC/mobile parts</td></tr><tr><td>Keyboards, mice</td><td>Logitech, HP, Dell, local OEM imports</td><td>Switzerland; US; US</td><td>Zebronics, Intex, iBall (brand/OEM, not deep IP)</td></tr><tr><td>Printers, scanners</td><td>HP, Canon, Epson, Brother</td><td>US; Japan; Japan; Japan</td><td>Very limited Indian printer IP; mostly imports</td></tr><tr><td>Power adapters, chargers</td><td>OEMs from China/Taiwan</td><td>China; Taiwan</td><td>Many small Indian brands; core designs imported</td></tr><tr><td>PC cabinets, PSUs</td><td>Cooler Master, Corsair, Antec, OEM imports</td><td>Taiwan; US; US</td><td>Local brands (e.g. Artis); still largely imported components</td></tr></table>

Xiaomi is covered by Eunice Lee; Netflix is covered by Laurent Yoon; American Tower is covered by Madison Rezaei; Samsung is covered by Mark Li; Microsoft (owns Github) and Salesforce (owns Slack) are covered by Mark Moerdler; Apple, HP and Dell are covered by Mark Newman; Amazon, Alphabet and Meta are covered by Mark Shmulik; CATL is covered by Neil Beveridge; Zoom and GitLab are covered by Peter Weed; Paytm is covered by Pranav Gundlapalle; Ericsson and Nokia are covered by Ulrich Rathe; Walmart is covered by Zhihan Ma

Hon hai, Wistron, Pegatron, BOE tech, Lenovo, Reliance, HFCL, Sterlite Tech, Indus Towers, Bharti Airtel, Ola (owns Krutrim), Zee, ZTE, Cisco, Juniper, Logitech, Canon, Epson, Brother Industries, Corsair, Antec and TCS (owns Tejas Networks) are not covered

Rest of the companies are unlisted

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
