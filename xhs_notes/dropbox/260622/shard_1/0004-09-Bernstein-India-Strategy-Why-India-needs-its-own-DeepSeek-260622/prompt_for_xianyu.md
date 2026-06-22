你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

<table><tr><td>Area</td><td>Main companies India depends on</td><td>Country of origin</td><td>Indian providers / initiatives</td></tr><tr><td colspan="4">Smartphones, feature phones, and mobile hardware</td></tr><tr><td>Smartphones (brands)</td><td>Samsung, Xiaomi, Vivo, Oppo, Apple, OnePlus, Motorola</td><td>KR; China; China; China; US; China; US</td><td>Lava, Micromax (smaller), JioPhone (Reliance), Karbonn</td></tr><tr><td>ODM / manufacturing</td><td>Chinese/Taiwanese ODMs; Foxconn, Wistron, Pegatron, etc.</td><td>Taiwan; Taiwan; Taiwan</td><td>Dixon, local EMS units under PLI schemes</td></tr><tr><td>Modems / RF chips</td><td>Qualcomm, MediaTek, UNISOC</td><td>US; Taiwan; China</td><td>No domestic RF baseband vendor</td></tr><tr><td>Displays &amp; batteries</td><td>Samsung, LG, BOE, CATL, others</td><td>KR; KR; China; China</td><td>Limited local battery assembly, cells largely imported</td></tr><tr><td colspan="4">Telecom networks and equipment</td></tr><tr><td>Mobile RAN &amp; core</td><td>Ericsson, Nokia, Huawei (historically), ZTE, Cisco</td><td>Sweden; Finland; China; China; US</td><td>Tejas Networks, HFCL, ITI, C-DOT-aligned vendors</td></tr><tr><td>Transmission &amp; fiber</td><td>Nokia, Ericsson, Huawei; global fiber makers</td><td>Finland; Sweden; China</td><td>HFCL, Sterlite Technologies (STL) for fiber and some gear</td></tr><tr><td>Tower infra</td><td>American Tower, global OEMs for gear</td><td>US, others</td><td>Indus Towers (India), Bharti Infratel (now merged)</td></tr><tr><td>Routers/switches (IP)</td><td>Cisco, Juniper, Huawei, Nokia</td><td>US; US; China; Finland</td><td>So

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
