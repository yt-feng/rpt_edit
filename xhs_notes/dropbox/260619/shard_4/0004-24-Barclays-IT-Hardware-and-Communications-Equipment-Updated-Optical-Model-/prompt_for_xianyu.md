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

CH: BARC Bank PLC and/or its group companies makes, or will make, a market in the securities (as defined under paragraph 16.2 (k) of the HK SFC Code of Co

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
