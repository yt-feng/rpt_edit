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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`BARC`。标题格式建议：`# BARC：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份BARC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
IT Hardware and Communications Equipment

# Updated Optical Model

We update our detailed Optical model that include splits for Long Haul/Submarine/Metro/Pluggable (ZR/ZR+) and Telco/Cloud breakouts. We continue to model DD growth on average over CY26E-27E, given sustained cloud strength and telco momentum.

In this report, we update our expanded Optical model, moving up our 2027 estimates based on strength across end markets and products. For this market, we are looking at the total Optical Networks market, with splits for Long Haul, Submarine, and Metro, as well as Pluggable (ZR/ZR+) breakouts. Additionally, we include a breakout of customer verticals (Telco, Cloud, Enterprise) and the estimated market share CIEN has in each.

Overall growth has been choppy the last few years (prior to 2025), given telco digestion (macro) and cloud lumpiness, though beginning 2025 and now moving into CY26-27 we expect growth to sustain at DD levels. We are encouraged by the strength we see across end markets and products. We now expect DD growth this year, and an acceleration on this growth into 2027, given current dynamics around AI.

Driving our estimates is the expanding cloud applications (i.e. scale across, hyper-rail, DCOM, etc) and cloud demand acceleration, as well as growing MOFN opportunities (\~10-15% of CIEN's telco business) and BEAD funding moving through the market. Our CY26 estimates move to 10% from 8%, and our CY27 estimates move to 12% from 13% (given nuances between FY and CY, as well as the higher base of CY26). We could see upward bias to our estimates with cloud demand acceleration continuing.

In alignment with our estimates, CIEN raised its FY26 guidance and gave high level commentary around FY27 - management expects "meaningful uptick" in revenue in FY27 due partially to hyper-rail and expects to see continued operating leverage into FY27+ (hyper-rail is better margin product). Despite the impressive book-to-bill and backlog posted the prior Q, the most recent Q book-to-bill was over 1 (\~1.3x) and management still expects backlog to grow through the year. We would highlight that we view these backlog dynamics fundamentally different that some of the backlog dynamics in our space post pandemic/supply chain crisis - management mentioned, given their relationships with the hyperscalers, they can see that the products are being deployed (not sitting in warehouses).

## Our conclusions are as follows:

\- AI-related spend has already propelled the Optical market over the past few years (CY19 and CY22 notable standouts as telco spend and hyperscalers built out networks). We continue to

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

IT Hardware and Communications

Equipment

NEUTRAL

IT Hardware and Communications

Equipment

Tim Long

+1 212 526 4043

tim.long@BARC.com

BCI, US

Alyssa Shreves

+1 212 526 7570

alyssa.shreves@BARC.com

BCI, US

Mary Lenox

+1 212 526 6277

mary.lenox@BARC.com

BCI, US

Clarisse Yu

+1 212 526 7025

clarisse.yu@BARC.com

BCI, US

expect DD growth in the cloud vertical in CY26-CY27, as AI-related cloud build-outs broaden and continue to accelerate.

FIGURE 1. Optical Market Expected to Enjoy DD Growth Trends, Driven by Telco Recovery and AI  
![](images/84b01a75fdc09635ead0564e6419cac581a6b3da015f2fbe6f687acec62d2d22.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | LH WDM ($) | Submarine ($) | Metro WDM ($) | Y/Y growth (%) |
| :--- | :--- | :--- | :--- | :--- |
| 2018 | 5,918 | 538 | 7,091 | |
| 2019 | 6,592 | 571 | 7,455 | 8 |
| 2020 | 6,664 | 774 | 7,510 | 0 |
| 2021 | 6,592 | 945 | 7,263 | -3 |
| 2022 | 7,798 | 849 | 7,307 | 7 |
| 2023 | 7,709 | 848 | 7,445 | -7 |
| 2024 | 7,118 | 704 | 6,195 | -12 |
| 2025E | 8,656 | 555 | 5,913 | 9 |
| 2026E | 8,025 | 475 | 6,403 | 10 |
| 2027E | 9,582 | 608 | 8,158 | 12 |
</details>

Source: 650 Group, Bloomberg, company documents, BARC estimates

- We currently do not forecast meaningful coherent Optical inside the data center in CY26 (potentially could see 2H26), and believe that to be more of a CY27+ opportunity.  
- We continue to expect the total Optical market to have a LSD CAGR from CY22-27, taking into account the down years of CY23-24.  
- Within this, we expect Metro to drive the lion's share of growth (down MSD in CY25 though +DD on average in CY26-27), as pluggables accelerate. We expect LH to grow this year and next (+HSD on average), as longer distance scale across (utilizes more LH network approaches vs synchronous scale across applications), MOFN-related demand, and telco general re-architecture of LH networks takes shape. We expect LH to remain roughly half of the total Optical market through CY27.  
• We expect growth in Metro to largely be driven by the rise of ZR/ZR+ Pluggables (+72% and +33% market growth during CY26-27, respectively). We believe the Metro market ex Pluggables is down HSD on average over the same time period.  
- We expect Pluggables to remain a small piece of the overall Optical market (on average high teens % of the total market through CY26-27), given their limited use cases and pricing dynamics (as well as continued growth in other equipment types).

FIGURE 2. Pluggables Remain a Small, Though Rapidly Growing, Part of the Metro Market  
![](images/2eb1089cf2f17a5dda9c882ecd995be373b387a047cc4e6714730f49b9458cd7.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | Metro WDM ex ZR/ZR+Pluggables ($) | Pluggable (ZR/ZR+) ($) | % Pluggables (ZR/ZR+) within Metro WDM (%) |
| :--- | :--- | :--- | :--- |
| 2021 | 6,859 | 404 | 6 |
| 2022 | 6,783 | 525 | 7 |
| 2023 | 6,893 | 553 | 7 |
| 2024 | 5,445 | 750 | 14 |
| 2025 | 4,599 | 1,314 | 22 |
| 2026E | 3,958 | 2,444 | 38 |
| 2027E | 4,004 | 4,153 | 51 |
</details>

Source: 650 Group, Bloomberg, company documents, BARC estimates

- We expect Sub to see +DD recovery in CY27 (on easy comps), after multiple down years through CY26. Sub is MSD-HSD% of the total market.  
- Despite the expected cloud growth opportunity, we expect telco to remain the lion's share of the industry (>50%) through CY25-27. However, we acknowledge >50% is materially lower than mid-70% representation just a few years prior.

FIGURE 3. Despite Cloud Growth, Telco Still Majority of the Market  
![](images/0942378ed02ab89628b703cbd3e00539438d14330974d3b82e8cc3c28495ba7f.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Telco ($) | Cloud ($) | Enterprise ($) |
| :--- | :--- | :--- | :--- |
| 2020 | 11,634 | 2,793 | 1,313 |
| 2021 | 11,177 | 2,872 | 1,209 |
| 2022 | 11,888 | 3,216 | 1,156 |
| 2023 | 11,902 | 3,241 | 1,112 |
| 2024 | 10,394 | 2,765 | 1,123 |
| 2025 | 10,000 | 3,579 | 1,977 |
| 2026E | 10,535 | 4,955 | 1,673 |
| 2027E | 10,810 | 6,127 | 2,223 |
</details>

Source: 650 Group, Bloomberg, company documents, BARC estimates

Within our AI-bucketed stock exposure, Optical continues to have among the highest implied AI multiples, such as CIEN and GLW. For further details on implied AI multiples in our coverage: Implied AI Multiples - Rising Tides Lift Some, 6/01/26

FIGURE 4. Summary of Implied AI P/E as of 5/29/2026

<table><tr><td>Company</td><td>Rating</td><td>p/e on CY27</td><td>core p/E</td><td>implied AI p/e</td></tr><tr><td>SMCI</td><td>EW</td><td>11x</td><td>11x</td><td>7x</td></tr><tr><td>FN</td><td>OW</td><td>36x</td><td>14x</td><td>40x</td></tr><tr><td>CLS</td><td>OW</td><td>26x</td><td>12x</td><td>31x</td></tr><tr><td>ANET</td><td>OW</td><td>37x</td><td>32x</td><td>40x</td></tr><tr><td>CIEN</td><td>OW</td><td>64x</td><td>18x</td><td>115x</td></tr><tr><td>JBL</td><td>OW</td><td>23x</td><td>12x</td><td>37x</td></tr><tr><td>FLEX</td><td>OW</td><td>26x</td><td>12x</td><td>40x</td></tr><tr><td>DELL</td><td>OW</td><td>19x</td><td>10x</td><td>58x</td></tr><tr><td>KEYS</td><td>OW</td><td>27x</td><td>22x</td><td>63x</td></tr><tr><td>HPE</td><td>OW</td><td>15x</td><td>11x</td><td>55x</td></tr><tr><td>GLW</td><td>EW</td><td>47x</td><td>19x</td><td>141x</td></tr><tr><td>CSCO</td><td>EW</td><td>25x</td><td>18x</td><td>72x</td></tr><tr><td>Average</td><td></td><td>30x</td><td>16x</td><td>58x</td></tr></table>

Source: Company Documents, Bloomberg, BARC estimates. Industry View: Neutral. Stock rating: OW=Overweight; EW=Equal Weight; UW=Underweight. For full disclosures on each covered company, including details of our company-specific valuation methodology and risks, please refer to http://publicresearch.barcap.com

## From a vendor standpoint:

\- CIEN (OW-rated) is the only company under our coverage in Optical that has been, and that we continue to expect to be, a share gainer – moving from 16% of the market in CY18 to \~32% in CY27E. We expect CIEN to be a beneficiary of telco customers' recovery, MOFN-related activity, and hyperscalers' AI build-outs, given its existing relationships with each customer set. CIEN also now competes in the ZR/ZR+ market, which we believe is largely incremental revenue for the company (with little cannibalization to existing Metro business).

FIGURE 5. CIEN Cloud Market Share Climbing  
![](images/2e72226bcc53d7e005966b1ccea2e39db23125c0afea86fa82a088fe4072509b.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | Cloud Worldwide Revenue ex CIEN ($M) | CIEN Cloud Revenue ($M) | CIEN Cloud Market Share (%) |
| :--- | :--- | :--- | :--- |
| 2021 | 2,070 | 802 | 28 |
| 2022 | 2,396 | 820 | 26 |
| 2023 | 1,987 | 1,254 | 39 |
| 2024 | 1,557 | 1,207 | 44 |
| 2025 | 1,496 | 2,083 | 58 |
| 2026E | 1,649 | 3,305 | 67 |
| 2027E | 1,357 | 4,770 | 78 |
</details>

Source: 650 Group, Bloomberg, company documents, BARC estimates

\- Within the ZR/ZR+ market, we expect CIEN to maintain its market share in the mid-teens from CY24-27, given its tech advantage (first win in the market for 800G ZR+) offset by the multiple players in the market. CIEN remains on track to more than double its pluggable revenue from 2025. We expect IADC revenue to be low DD % of total revenue this FY (we forecast \~10%), implying growth of almost 300% y/y (inclusive of pluggables, DCOM, scale-across).

FIGURE 6. CIEN Market Share Within the ZR/ZR+ Pluggable Market Mid-Teens %  
![](images/d90e6fec96b9dbbfa2d23c24b65331afceca668357a27e1fd6d8e7463288d0dd.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | Pluggable Revenue (ZR/ZR+) ex CIEN ($M) | CIEN Pluggable Revenue ($M) | CIEN % Market Share (%) |
| :--- | :--- | :--- | :--- |
| 2021 | 391 | 13 | 3 |
| 2022 | 512 | 13 | 2 |
| 2023 | 538 | 95 | 3 |
| 2024 | 650 | 181 | 13 |
| 2025 | 1,110 | 203 | 15 |
| 2026E | 2,044 | 401 | 16 |
| 2027E | 3,668 | 485 | 12 |
</details>

Source: 650 Group, Bloomberg, company documents, BARC estimates

- CSCO (EW-rated): The company had their first scale-across design win with P200 from two different hypers last Q, with an additional third hyper win announced in early Q4, leading to confidence on the uptake and momentum within this business. The other 50% of AI orders in the Q came from Optics, with five new design wins with different hypers in Q3. Management is confident in the Acacia momentum and expects 200%+ y/y growth in FY26, and we model much higher. CSCO is not a meaningful player in the LH or Sub markets. While CSCO isn’t a major player in optical systems, the company's Acacia business is very strong on components and sub systems.  
- Unlike other verticals under our coverage, white box does not dominate the market share of the Optical market. From CY18 to CY27, we forecast white box to stay around LSD-MSD % of the total market. We believe this is due largely to the technical complexity required of Optical systems and low overall percentage of spending.

## Analyst(s) Certification(s):

I, Tim Long, hereby certify (1) that the views expressed in this research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC"). All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

Where any companies are the subject of this research report, for current important disclosures regarding those companies please refer to https://publicresearch.BARC.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

The analysts responsible for preparing this research report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by investment banking activities, the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst.

Research analysts employed outside the US by affiliates of BARC Capital Inc. are not registered/qualified as research analysts with FINRA. Such non-US research analysts may not be associated persons of BARC Capital Inc., which is a FINRA member, and therefore may not be subject to FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst's account.

Analysts regularly conduct site visits to view the material operations of covered companies, but BARC policy prohibits them from accepting payment or reimbursement by any covered company of their travel expenses for such visits.

BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

## Materially Mentioned Stocks (Ticker, Date, Price)

Ciena Corporation (CIEN, 15-Jun-2026, USD 463.41), Overweight/Neutral, CD/CE/J

Cisco Systems, Inc. (CSCO, 15-Jun-2026, USD 120.17), Equal Weight/Neutral, CD/CE/D/J/K/L/M

Unless otherwise indicated, prices are sourced from Bloomberg and reflect the closing price in the relevant trading market, which may not be the last available closing price at the time of publication.

## Disclosure Legend:

A: BARC Bank PLC and/or an affiliate has been lead manager or co-lead manager of a publicly disclosed offer of securities of the issuer in the previous 12 months.

B: An employee or non-executive director of BARC PLC is a director of this issuer.

CD: BARC Bank PLC and/or an affiliate is a market-maker in debt securities issued by this issuer.

CE: BARC Bank PLC and/or an affiliate is a market-maker in equity securities issued by this issuer.

CH: BARC Bank PLC and/or its group companies makes, or will make, a market in the securities (as defined under paragraph 16.2 (k) of the HK SFC Code of Conduct) in respect of this issuer.

D: BARC Bank PLC and/or an affiliate has received compensation for investment banking services from this issuer in the past 12 months.

E: BARC Bank PLC and/or an affiliate expects to receive or intends to seek compensation for investment banking services from this issuer within the next 3 months.

FA: BARC Bank PLC and/or an affiliate beneficially owns 1% or more of a class of equity securities of this issuer, as calculated in accordance with US regulations.

FB: BARC Bank PLC and/or an affiliate beneficially owns a long position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FC: BARC Bank PLC and/or an affiliate beneficially owns a short position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FD: BARC Bank PLC and/or an affiliate beneficially owns 1% or more of a class of equity securities of this issuer, as calculated in accordance with South Korean regulations.

FE: BARC Bank PLC and/or its group companies has financial interests in relation to this issuer and such interests aggregate to an amount equal to or more than 1% of this issuer's market capitalization, as calculated in accordance with HK regulations.

GD: One of the Research Analysts on the fundamental credit coverage team (and/or a member of his or her household) has a long position in the common equity securities of this issuer.

GE: One of the Research Analysts on the fundamental equity coverage team (and/or a member of his or her household) has a long position in the common equity securities of this issuer.

H: This issuer beneficially owns more than 5% of any class of common equity securities of BARC PLC.

I: BARC Bank PLC and/or an affiliate is party to an agreement with this issuer for the provision of financial services to BARC Bank PLC and/or an affiliate.

J: BARC Bank PLC and/or an affiliate is a liquidity provider and/or trades regularly in the securities of this issuer and/or in any related derivatives.

K: BARC Bank PLC and/or an affiliate has received non-investment banking related compensation (including compensation for brokerage services, if applicable) from this issuer within the past 12 months.

L: This issuer is, or during the past 12 months has been, an investment banking client of BARC Bank PLC and/or an affiliate.

M: This issuer is, or during the past 12 months has been, a non-investment banking client (securities related services) of BARC Bank PLC and/or an affiliate.

N: This issuer is, 

[中间内容因长度限制已省略]

 scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
