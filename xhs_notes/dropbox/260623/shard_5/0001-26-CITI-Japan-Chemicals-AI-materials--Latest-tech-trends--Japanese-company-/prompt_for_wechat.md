你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`Citi`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Japan Chemicals

## AI materials: Latest tech trends, Japanese company strengths and issues

## CITI'S TAKE

We heard this week about AI-related materials technology trends in interviews with Mitsubishi Gas Chemical's Toru Harada (Executive Officer, Division Director, Electronics materials Division, Specialty Chemicals Business), Tsuyoshi Yamazaki (General Manager, Laminate Material Group, Electronics materials Division, Specialty Chemicals Business), and Kiyonari Hiramatsu (General Manager, Raw-New Materials Sales & Marketing Department, Electronics materials Division, Specialty Chemicals Business); Nitto Boseki's Hiroki Kajikawa (Senior Executive Officer, Deputy Division General Manager of the Corporate Management Division, General Manager Corporate Communication); JX Advanced Materials' Tomoji Mizuguchi (Senior Executive Officer, Deputy General Manager, Technology Group); Asahi Kasei's Toshiyasu Horie (Representative Director, Primary Executive Officer, CFO); and Mitsui Kinzoku's Kenji Kubou (General Manager, Business Planning Department) and Kenji Mori (Assistant General Manager, Marketing Group, New Product & Process Development). We also followed up on AGC's June 2 semiconductor-related business briefing and attended talks on PTFE at JPCA 2026 (June 10-12).

Strength—The emphasis on the strength of AI-related demand at this management level (not only on the IR side) was reassuring. Our meetings also confirmed the technological strength of Japan's materials industry. Such highly competitive Japanese firms can be considered the support base for current AI supply chains.

Issues: pricing strategy — However, our regular conversations with investors suggest stock market frustration with Japanese materials makers for a low-key approach to price negotiations. While our June 17 Macro to Micro report (Japan Multi-Asset - The new pricing era: Pass-throughs fueling Japan's virtuous cycle) notes signs that Japanese firms are becoming more proactive on price pass-through, we acknowledge that materials makers still look conservative in pricing strategy in comparison with foreign counterparts. Given tight supply/demand and involvement in key materials for AI supply chains (as well as the broad social acceptance of price pass-through signaled by the report) we think materials makers could show greater hunger for profit. In this vein we think JX Advanced Materials might take price hikes to a new dimension in upcoming negotiations, having announced up to ten-fold expansion in InP substrate capacity on June 16. We have heard particularly positive responses from foreign investors, who have referred to untypical aggressive capacity expansion and pricing strategy direction for a Japanese company.

Issues: ability to grasp downstream trends —Many business division managers indicated that upstream materials involvement means high sensitivity to primary customer demand trends but makes it difficult to discern demand and technological trends in the segments from secondary to final customers (sometimes the final application breakout is unknown, and the reasons underlying the magnitude of growth in demand are not clearly understood). Improvements to capabilities for gauging downstream trends in supply chains should facilitate early moves on next-generation product development and accurate assessment of underlying demand (avoidance of oversupply risk inherent in order duplication).

Yuta Nishiyama $^{AC}$ +81-3-6776-4643
yuta.nishiyama@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations.

\- Mitsubishi Gas Chemical — The favorable progress in customer evaluations of RS material, a new BT material product, is a positive. We got the impression that there is a very high likelihood the material will be adopted for use in FC-BGA packaging (especially for GPUs). MGC’s materials were never seen as inferior to competing products in terms of key physical characteristics (like low-CTE, low-Dk), but we understand the semiconductor industry was generally reluctant to use alternative materials (due to lack of track record). However, the company explained that, in the last one-to-two years, efforts to find alternative materials have intensified across the supply chain amid CCL supply shortages (stemming originally from tighter low-CTE glass supply/demand), and that BT looks increasingly likely to be chosen as an alternative (given that its physical characteristics are basically superior). MGC intends to use the combination of RS and e-glass to target market share in applications like switches and PMICs, and the combination of RS and low-CTE glass to target share in BGA applications. In low-CTE glass, it appears the company is making progress in securing/using alternative suppliers beyond the main players. The company’s OPE product currently offers low-Dk and low-Df characteristics in line with those of PPE in current target domains, but MGC is developing new products, aiming at characteristics on a par with hydrocarbon and PTFE materials. Shipments of samples have already started.

Nittobo — The supply/demand balance is tightest for T-glass (low-CTE), followed by NER-glass (second-gen low-Dk), then NE-glass (first-gen low-Dk). Nittobo believes it is effectively the only company capable of supplying T-glass. Prospects of further increases in demand mean Nittobo may need to look at further capacity expansion; we understand the company would plan to enter into price negotiations as needed in that scenario. The NER-glass product cycle is proving more prolonged than initially expected, suggesting that the size of the addressable market could increase significantly. Specifically, it was originally thought that M9 and more advanced CCLs would require Q-glass or third-generation low-Dk glass (NEZ-glass), but we understand that recent advances in resin technology are generally seen as implying that the low-Dk requirements for glass cloth may not be as stringent as first thought (i.e., NER-glass may be sufficient). In low-Dk glass, overseas competitors have been making up ground sooner than expected, but management commented that their catching-up was not necessarily unfavorable from an overall market perspective given that the market was expected to expand beyond the size where Nittobo alone could handle all the supply. On the question of whether PTFE could threaten the low-Dk glass market, the company commented that the hurdle to adoption would be high given issues like PTFE's lack of rigidity.

■ JX Advanced Metals — On June 16, the company announced plans to increase InP substrate production capacity by up to 10x through FY3/31. Management commented that, while InP substrate demand growth was initially projected at around 25% annually, recent momentum suggests growth of 30-40% could be expected. As of 2026, data centers are already using optical communication between racks, within data centers, and between centers. From 2028 onward, there could also be a transition from electrical to optical transmission within servers and within racks. This would mean higher demand for optical transceivers and, by extension, for InP substrates. Although JX announced a 10x production capacity increase, we do not think it would be surprising if demand increased by a greater factor. Citing a desire to quickly recoup capex (around ¥145bn cumulatively), the company also noted the importance of pricing strategy (our view is that, based on capex to date and the extent of price hikes JX has implemented in the past, there could be negotiations geared toward price increases of 2-3x). The company also explained that, with future GPU models

expected to have TDPs (thermal design powers) around 3x those of current models and their maximum power consumption expected to be 8x higher or more, the need to secure suitable power supply could lead to explosive growth in demand for tantalum powder for use in tantalum capacitors. The company also demonstrated how its magnetic target materials for HDD production have an edge in HAMR (heat-assisted magnetic recording) applications, with a share higher than the 50-60% share for PMR (perpendicular magnetic recording) applications.

■ AGC — The company provides CCLs (marketed under the Meteorwave brand) for PCB manufacturing (customers are PCB manufacturers). Based on statements on AGC’s website, we understand the resin used in the Meteorwave line is a PPE resin developed in-house. We understand that the cutting-edge ELL series within the Meteorwave line uses a hydrocarbon resin also developed in-house. The company says that use of these resins means that applications previously thought to require Q-glass now can use second-generation low-Dk glass cloth (this ties in with the explanation of the extended NER-glass product cycle in the Nittobo section). We understand evaluation of ELL series products is underway for applications like 1.6T (224Gbps x 8L) switches and routers. AGC is also independently developing low-Dk fluororesin, which it says is being well received by CCL manufacturer customers. We understand that, although this resin is not strictly PTFE, it has a molecular structure close to that of PTFE (per AGC’s website). The material is said to share the low-Df, low-Dk characteristics of PTFE while also allowing lamination with other materials with no need for an adhesive layer (as we describe later, interlayer adhesion is a challenge with PTFE).

Asahi Kasei — Asahi Kasei's PIMEL, used as a redistribution layer (RDL) material, has an extremely high share in cutting edge applications at key customers, with supply struggling to keep up with demand. The company plans to bring forward production increases. Demand for RDL materials is expected to increase as layer counts rise in line with the evolution of CoWoS packaging (CoWoS-S, CoWoS-R, CoWoS-L). In glass cloth production, the company expects to be able to secure yarn for L2 (second-gen low-Dk) cloth from new suppliers and to increase the volume of procurement. Sample shipments of low-CTE glass cloth have already started, with evaluations underway. The plan is to move to a full launch at end-FY3/27 or during FY3/28. Regarding Q-glass, while noting that customers would be motivated to use second-generation low-Dk glass to the extent possible (which squares with Nittobo's and AGC's explanations), management highlighted the edge offered by Asahi Kasei's combination of fiber and chemicals technologies.

■ Mitsui Kinzoku — Beyond its established applications (like smartphone motherboards, memory), the MicroThin series has seen a sharp increase in inquiries for use in PCBs for optical transceivers. As for VSP, the sales weightings of HVLP4 and HVLP 5 are already quite high, with the firm commanding the top share in HVLP4 and an 80% share in HVLP5.

■ PTFE — We attended a talk on PTFE at JPCA 2026 (Total Solution Exhibition for Electronic Equipment) held on June 10-12. PTFE's extremely favorable low-Dk and low-Df characteristics mean it is expected to be used in high-speed, high-volume, low-latency PCBs. However, there are issues with the use of PTFE, including a lack of rigidity, which leads to a tendency to warp (especially in large PCBs), low surface energy, which makes lamination difficult due to increased challenges with interlayer adhesion, and poor CTE characteristics, making heat deformation more likely (high coefficient of thermal expansion). To address

these challenges, we understand efforts are underway to improve rigidity and achieve low-CTE characteristics through measures like impregnating the substrate with fillers that have a low coefficient of thermal expansion.

![](images/931768c7d501e6eac69b439830376b9e2c583059bdf7bf5136fc3942bb5dda5e.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Company data

![](images/bfb36653ed204631462cc8274c6d92184409ca619dab2db570457cf0cf1e4b16.jpg)

Figure 3. JXAM: Product deployment in data centers (particularly AI servers)  
![](images/86f83851f73c821b0e8480cc8f8b8841cb0ecdde785a546ccd5b27c00ee11781.jpg)

<table><tr><td>Product</td><td>Overview</td><td>Market Share</td><td>Competitor</td></tr><tr><td>1 Sputtering Targets for Semiconductors</td><td>Metal materials for semiconductor circuit formation. Approximately 30% of sales are for leading-edge logic, 5% for interposer redistribution layers (RDL), and 5% for TSV formation in HBM.</td><td>approx. 60%</td><td>CN KFMIUS Honeywell</td></tr><tr><td>2 Sputtering Targets for Magnetic Devices</td><td>Metal materials used to form HDD media, with 80–90% of sales for data centers.</td><td>approx. 60%</td><td>JP TanakaPrecious Metals</td></tr><tr><td>3 InP Substrates</td><td>Adoption of InP substrates for optical networks between AI servers (optoelectronic devices) is rapidly expanding due to high transmission speed, low loss, and superior high-frequency performance. About 80% of sales are for data-center applications.</td><td>approx. 40%</td><td>JP Sumitomo ElectricUS AXT</td></tr><tr><td>4 CVD/ALD Precursors</td><td>In highly stacked NAND (300 layers and above), molybdenum (Mo) is attracting attention as a new material for word lines. Sales remain limited as of 2025, but are expected to expand from 2026 onward.</td><td>approx. 30%</td><td>US EntegrisFR Air Liquide</td></tr><tr><td>5 Lithography Materials</td><td>The company supplies reflective materials for EUV light in EUV exposure systems.</td><td>approx. 100%</td><td>NA</td></tr><tr><td>6 Tantalum Powder (CAP Powder)</td><td>Because AI servers tend to generate high heat, adoption of heat-resistant tantalum capacitors as power-delivery components is rapidly increasing, and approx. 40% of sales for CAP powder are for data centers.</td><td>approx. 50%</td><td>US GAM</td></tr><tr><td>7 Titanium Copper Alloy</td><td>While copper alloys had been used for connectors in general-purpose servers, they are rapidly being replaced by Titanium Copper due to heat-resistance and related requirements. Approx. 50% of Titanium Copper sales are for data center.</td><td>approx. 90%</td><td>JP DOWAMetaltech</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: All numbers are Citi estimates.

Source: Citi, Company data

Figure 4. Resins with low dielectric properties and OPE application areas  
![](images/ba08bf6fd246e53353c630118e8f017bf16fa459bde9a0b003445698fa18c24d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: Citi, Company data  
Figure 5. AGC's solutions for semiconductor target applications  
![](images/3d67a77bbd3d02d32589f34ec8f87c585e1ab9db099355f40ccb477a1e70d490.jpg)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

# Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at

https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding

[中间内容因长度限制已省略]

ves, financial situation or needs of any particular investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a

subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.  
Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.
"""
