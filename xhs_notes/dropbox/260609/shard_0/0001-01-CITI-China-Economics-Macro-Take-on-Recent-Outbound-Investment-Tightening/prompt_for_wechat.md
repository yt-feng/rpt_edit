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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Citi`。标题格式建议：`# Citi：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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
08 Jun 2026 00:21:55 ET | 11 pages

# China Economics

Macro Take on Recent Outbound Investment Tightening

## CITI'S TAKE

The government/ministries have launched a series of actions tightening China's outbound investments. We do not view them primarily about curbing capital outflows but see the main policy focus on closing regulatory loopholes and strengthening domestic policy effectiveness. For ODI, national security is viewed as a rising policy concern, while for portfolio flows, what happened is an enforcement action rather than a new regulation. We expect the macro impact to be limited, as we believe the backdrop of RMB appreciation and Middle East flows into Hong Kong could alleviate the negative impact. Implementation details, second-order taxation concerns, and further opening via official channels are three things to watch. We don't see the crackdown on illicit outflows undermining RMB internationalization, as the latter runs via official and legal channels.

Xiangrong Yu $^{AC}$

+852-2501-2754

xiangrong.yu@citi.com

Xinyu Ji AC

+852-2501-2792

xinyu.ji@citi.com

What happened? — The government/ministries have launched a series of actions to tighten China's outbound investments lately. [1] State Council released new outbound investment regulations expanding coverage to individuals and consolidating national security, data, and technology controls into a single unified framework (Gov, Jun 1 $^{st}$ ). [2] CSRC and other ministries issued action plans to rectify illegal cross-border securities, futures and fund operations (CSRC, May 22 $^{nd}$ ). CSRC singled out its investigations on three brokers and imposed penalties to confiscate gains from onshore brokerage activities since 2023 (CSRC, May 22 $^{nd}$ ). [3] HK SFC (SFC, May 22 $^{nd}$ ) and HKMA (HKMA, May 22 $^{nd}$ ) issued guidance on account openings and management for mainland investors. Increased scrutiny has rippled into Hong Kong property, insurance (SCMP, Jun 1 $^{st}$ ), and private banking (Bloomberg, Jun 5 $^{th}$ ).

Why, why now, and how much impact? — The policy focus, in our view, is on closing regulatory loopholes and strengthening domestic policy effectiveness. Unlike in previous episodes, there is little RMB depreciation pressure now, and unexplained capital outflows, as we calculated, appear manageable.

■ ODI: National security considerations are growing, particularly amid the AI race. Tighter scrutiny over technology and data, and the extension of controls to individuals, are unsurprising, in our view.  
■ Portfolio flows: The crackdown is not new regulation but an enforcement action. The three named brokers were flagged by CSRC as early as 2016 (CSRC, Jul 26 $^{th}$ , 2016), with a prior tightening round in 2022 (CSRC, Dec 30 $^{th}$ , 2022). The timing may also dampen the market impact from the move: the RMB is in an appreciation cycle, and Middle East funds could be flowing into Hong Kong post the conflict (The Standard, Jun 1 $^{st}$ ).

Macro impact looks limited. ODI is structurally set to rise as Chinese firms expand abroad. On portfolio flows, the named brokers could hold \~HK\$250bn in mainland customer assets (Bloomberg, May 28 $^{th}$ and Jun 2 $^{nd}$ ). The impact could be measured even if the rectification expands to other channels, such as Hong Kong property.

What to watch ahead? — [1] Implementation details are key to watch. The three brokers are likely the first targets of tightened scrutiny, and further expansion to other brokers or regions would not surprise us. A broadening of scope to insurance, WMPs, private equity, and property remains a possibility. [2] Taxation is an induced second-order question, in our view, particularly with funds rerouting back to the mainland. Personal income tax growth rose to 11.5% YoY in 2025 and accelerated to 12.2% YoY this Jan-April, partially as the government steps up tax collection on overseas gains (Xinhua, Jan 16 $^{th}$ ). [3] Expansion of official outbound investment channels could follow, though likely gradually. An increase in QDII quota (US176bn now), a broader WMP connect rollout beyond the Greater Bay Area and pilot program of insurance connect are all possible options. Closing the back door won’t prevent opening the front door wider, in our view.

Capital controls undermine RMB internationalization? — Curbs on illicit cross-border flows need not undermine the "golden window" for RMB

internationalization, in our view. Flows associated with RMB internationalization run through official channels, including QFII, Bond Connect, CIBM Direct, Stock Connect, and others, and are unaffected. Hong Kong's role as a connector is not likely to be materially undermined, supported by RMB appreciation and continued Middle East fund inflows. If anything, enforcement of capital control strengthens our view that RMB internationalization still has a long way to go as the PBoC tries to find the right balance in the classical trilemma.

Figure 1. Unexplained capital outflows from the BoP – a likely upper bound for capital flight appears manageable  
![](images/c281a684256ea939051bd090df05632baae776908ce3b6c8931e799a00d5efe0.jpg)

<details>
<summary>bar chart</summary>

| Category                  | Value (US$ bn) |
| ------------------------- | -------------- |
| Current Account Surplus   | 730            |
| Decrease in Reserves      | 760            |
| Net Outflows              | 780            |
| Net FDI                   | 740            |
| Net Portfolio Flow        | 700            |
| Banking Related Flows and Others | 279          |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SAFE, Citi

Figure 3. There is little RMB depreciation pressure now with FX settlement...  
![](images/749c9f970e9e89f270a5a7a4f9bae1b6fe62621d76cac2a4f177a3cfee561d3b.jpg)

<details>
<summary>line chart</summary>

| Year | Net FX Settlement (US$ bn) | USDCNY, Reversed (RHS) |
|------|-----------------------------|--------------------------|
| 11   | ~400                        | ~6.2                     |
| 12   | ~500                        | ~6.3                     |
| 13   | ~300                        | ~6.4                     |
| 14   | ~350                        | ~6.5                     |
| 15   | ~300                        | ~6.4                     |
| 16   | ~-500                       | ~6.3                     |
| 17   | ~-200                       | ~6.2                     |
| 18   | ~0                          | ~6.4                     |
| 19   | ~-100                       | ~6.3                     |
| 20   | ~-50                        | ~6.2                     |
| 21   | ~100                        | ~6.3                     |
| 22   | ~200                        | ~6.4                     |
| 23   | ~-100                       | ~6.3                     |
| 24   | ~-200                       | ~6.2                     |
| 25   | ~-100                       | ~6.1                     |
| 26   | ~400                        | ~6.4                     |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SAFE, Wind, Citi

Figure 5. The macro impact from this round of outbound investment tightening looks limited  
![](images/695a340221d0a3dd0d53ddd4ada24894968f932dd6a9d44dbec4872284316262.jpg)

<details>
<summary>bar chart</summary>

Potential Inflows from Mainland China to Hong Kong
| Category | Potential Inflows (HKD bn) |
| :--- | :--- |
| Client Assets under Crackdown, Stock, Brokers | 250 |
| HK Asset/Wealth Mgmt, Net Inflows, Mainland-Related Firms, 2024 | 255 |
| Insurance, Mainland Visitor Premium Payment, 2024 | 60 |
| Property, Non-HKID Purchase, 2025 | 30 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: HKIA, HK SFC, news reports, Citi Property Research, Citi

Figure 2. The capital outflow pressure could be smaller compared with the episode in 2015  
![](images/aac80d552b9317f07ad4e0baf578a0ac10ddb576b5d2bdd0039ea98933c8d3b8.jpg)

<details>
<summary>line chart</summary>

| Year | Residual Change in FX Reserves (US$ bn) |
| ---- | -------------------------------------- |
| 06   | -50                                    |
| 07   | 0                                      |
| 08   | 50                                     |
| 09   | 150                                    |
| 10   | -100                                   |
| 11   | -150                                   |
| 12   | 350                                    |
| 13   | 200                                    |
| 14   | 0                                      |
| 15   | 600                                    |
| 16   | 650                                    |
| 17   | 550                                    |
| 18   | 150                                    |
| 19   | 250                                    |
| 20   | 100                                    |
| 21   | 550                                    |
| 22   | 250                                    |
| 23   | -50                                    |
| 24   | 50                                     |
| 25   | 350                                    |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SAFE, Citi

Figure 4. ... and exporters' conversion ratio both rising  
![](images/3272751dae6ab46ea97a91c2b5defd847f1fc6140df43a833fa52c75957fbaab.jpg)

<details>
<summary>line chart</summary>

| Year | FX Receipts Conversion Ratio | USDCNY (Reversed) |
|------|-------------------------------|--------------------|
| 12   | 64%                           | 6.0                |
| 13   | ~61%                          | ~6.2               |
| 14   | ~62%                          | ~6.4               |
| 15   | ~59%                          | ~6.3               |
| 16   | ~57%                          | ~6.1               |
| 17   | ~55%                          | ~5.9               |
| 18   | ~57%                          | ~6.2               |
| 19   | ~58%                          | ~6.0               |
| 20   | ~57%                          | ~5.8               |
| 21   | ~56%                          | ~6.0               |
| 22   | ~55%                          | ~6.2               |
| 23   | ~54%                          | ~6.0               |
| 24   | ~53%                          | ~5.8               |
| 25   | ~54%                          | ~6.0               |
| 26   | ~56%                          | ~6.8               |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SAFE, Wind, Citi

Figure 6. China's ODI could be on a structural upward trend as Chinese corporates search for growth engines  
![](images/00deec57f443824fe687e1cd8e3a37c4a84ef4ab009b747b2073c24fb867bc54.jpg)

<details>
<summary>line chart</summary>

| Year | Non-Financial Sectors | All |
|------|------------------------|-----|
| 11   | ~65                    | -   |
| 12   | ~70                    | -   |
| 13   | ~80                    | -   |
| 14   | ~90                    | -   |
| 15   | ~100                   | -   |
| 16   | ~110                   | -   |
| 17   | ~170                   | -   |
| 18   | ~110                   | -   |
| 19   | ~120                   | ~160 |
| 20   | ~110                   | ~120 |
| 21   | ~115                   | ~130 |
| 22   | ~120                   | ~140 |
| 23   | ~125                   | ~150 |
| 24   | ~130                   | ~155 |
| 25   | ~140                   | ~160 |
| 26   | ~145                   | ~175 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: MoFCOM, Wind, Citi

Figure 7. Taxation concerns could follow the tightening on portfolio flows  
![](images/59cfedb72d0d25012e4eaf826c6999809ebe4a8fc552c4b631a06b01e8ee32b8.jpg)

<details>
<summary>line chart</summary>

| Year | Personal Income Tax Revenue | Nominal GDP (RHS) |
|------|-----------------------------|-------------------|
| 14   | ~15%                        | ~10%              |
| 15   | ~10%                        | ~5%               |
| 16   | ~20%                        | ~0%               |
| 17   | ~15%                        | ~5%               |
| 18   | ~20%                        | ~10%              |
| 19   | ~15%                        | ~5%               |
| 20   | ~-25%                       | ~-10%             |
| 21   | ~10%                        | ~-5%              |
| 22   | ~30%                        | ~13%              |
| 23   | ~5%                         | ~5%               |
| 24   | ~0%                         | ~0%               |
| 25   | ~5%                         | ~5%               |
| 26   | ~10%                        | ~5%               |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: MoF, NBS, Wind, Citi

Figure 8. The expansion of official channels is one thing to watch, with Stock Connect showing need to diversify  
![](images/fd27fea8ce12dc51a53fdfa87329c5bbcb762c9c9d6d80424ad31ccce416ae9a.jpg)

<details>
<summary>line chart</summary>

| Year | Stock Connect, Southbound (HKD trn) |
| ---- | ---------------------------------- |
| 15   | ~0.1                               |
| 16   | ~0.05                              |
| 17   | ~0.15                              |
| 18   | ~0.25                              |
| 19   | ~-0.05                             |
| 20   | ~0.3                               |
| 21   | ~0.7                               |
| 22   | ~-0.05                             |
| 23   | ~0.2                               |
| 24   | ~0.3                               |
| 25   | ~0.9                               |
| 26   | ~0.4                               |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Wind, Citi

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from China.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from China.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from China in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): China.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: China.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: China.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to China. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr><tr><td>Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for wh

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
