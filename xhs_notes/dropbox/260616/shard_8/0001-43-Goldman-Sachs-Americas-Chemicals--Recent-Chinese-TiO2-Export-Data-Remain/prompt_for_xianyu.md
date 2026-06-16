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
# Americas Chemicals: Recent Chinese TiO2 Export Data Remains Elevated; Updating KRO Estimates

Chinese April TiO2 net export data released indicates sustained high export volumes to markets where Western producers (CC, TROX, KRO) compete. Year-to-date through April TiO2 net exports are up 88kt (a 14% increase). We have long viewed China's net export number, the key metric by which to judge the health of Western TiO2 producers markets. The higher exports were surprising to us given the sulfur issues but that extra volume will likely lead to weaker than expected price increases in 2H. The Indian anti-dumping duty (ADD) remains suspended, with no definitive timeline for a judicial decision regarding its potential reinstatement; however since China lacks bonded warehouses in India, any reinstatement would likely have an immediate market impact. In April, Chinese exports to India increased by 14kt to 32kt, contributing to a year-to-date increase of 32kt, or 28%. Similarly, April exports to the EU increased by 4kt to 20kt, with year-to-date volumes up 19kt, a 32% increase. It seems the impact of elevated sulfur on Chinese production has not done enough to curtail exports into the international market, indicating that the Chinese product is more resilient than expected. Regarding demand, paint volumes (the dominant end market for TiO2) looks weaker than we expected to start the year. With meaningfully higher Chinese exports and paint volumes weaker than expected, we believe the TiO2 market will soften by the end of the summer and that could lead to pricing move up less than expected.

Duffy Fischer

+1(212)902-0099

duffy.fischer@gs.com

GS & Co. LLC

Ramsey Abdulrahim

+1(212)902-0091

ramsey.abdulrahim@gs.com

GS & Co. LLC

Mike Harris

+1(212)902-3667 | mike.harris@gs.com

GS & Co. LLC

Jordan Lee

+1(212)357-6986 | jordan.lee@gs.com

GS & Co. LLC

Exhibit 1: Chinese Net Exports  
![](images/770ec5b4674d0ea0994aa9583cf1abe0732037f3b81a2ba147cbc6c32c06bb8e.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 2014 | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  |
| 2015 | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  |
| 2016 | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  |
| 2017 | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  |
| 2018 | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  |
| 2019 | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  | 50  |
| 2020 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| 2021 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| 2022 | 125 | 125 | 125 | 125 | 125 | 125 | 125 | 125 | 125 | 125 | 125 | 125 |
| 2023 | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 2024 | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 2025 | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 2026 | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| Total (in '1' or similar)<lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><nl>

</details>

Source: China Government Export Data

Exhibit 2: Chinese Net TiO2 Exports  
MoM, in kt  
![](images/344851418bc48a19fb1915793bdf0b7405245e672389a435b406fee5926dec2a.jpg)

<details>
<summary>bar chart</summary>

| Month | 2024 | 2025 | 2026 |
|---|---|---|---|
| January | 153 | 153 | 178 |
| February | 127 | 153 | 149 |
| March | 183 | 176 | 196 |
| April | 151 | 141 | 187 |
| May | 141 | 129 | - |
| June | 169 | 128 | - |
| July | 151 | 128 | - |
| August | 155 | 136 | - |
| September | 139 | 150 | - |
| October | 149 | 140 | - |
| November | 143 | 148 | - |
| December | 152 | 166 | - |
Jan-Apr 26/25: +88kt/14% y/y
</details>

Source: China Government Export Data

Exhibit 3: China TiO2 Exports to the EU

<table><tr><td>EU</td><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td><td>Jul</td><td>Aug</td><td>Sep</td><td>Oct</td><td>Nov</td><td>Dec</td><td>YTD</td></tr><tr><td>2023</td><td>21</td><td>25</td><td>21</td><td>20</td><td>31</td><td>24</td><td>23</td><td>17</td><td>19</td><td>14</td><td>16</td><td>24</td><td>256</td></tr><tr><td>2024</td><td>32</td><td>29</td><td>32</td><td>34</td><td>24</td><td>17</td><td>7</td><td>18</td><td>11</td><td>17</td><td>10</td><td>12</td><td>243</td></tr><tr><td>2025</td><td>12</td><td>14</td><td>17</td><td>16</td><td>15</td><td>16</td><td>11</td><td>11</td><td>11</td><td>15</td><td>14</td><td>16</td><td>169</td></tr><tr><td>2026</td><td>16</td><td>19</td><td>24</td><td>20</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>79</td></tr></table>

Source: China Government Export Data

Exhibit 4: China TiO2 Exports to India

<table><tr><td>India</td><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td><td>Jul</td><td>Aug</td><td>Sep</td><td>Oct</td><td>Nov</td><td>Dec</td><td>YTD</td></tr><tr><td>2023</td><td>20</td><td>28</td><td>24</td><td>19</td><td>19</td><td>15</td><td>19</td><td>21</td><td>20</td><td>17</td><td>21</td><td>25</td><td>248</td></tr><tr><td>2024</td><td>22</td><td>17</td><td>26</td><td>22</td><td>23</td><td>35</td><td>27</td><td>30</td><td>23</td><td>23</td><td>30</td><td>29</td><td>308</td></tr><tr><td>2025</td><td>30</td><td>33</td><td>34</td><td>18</td><td>10</td><td>13</td><td>17</td><td>15</td><td>23</td><td>17</td><td>18</td><td>29</td><td>257</td></tr><tr><td>2026</td><td>49</td><td>29</td><td>39</td><td>32</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>149</td></tr></table>

Source: China Government Export Data

We update our estimates to reflect the positive impact KRO is seeing from the lower operating rates they ran in late 2025. Their Q4 loss underlines the high fixed cost absorption that ran through the P&L. In 1H26, they are seeing the benefit of making that operating decision last year. KRO is also seeing a benefit from the structural cost actions they took plus some price and some improvement in ore costs. We think that later into the year, KRO production rates could catch up with sales volumes which they have been under since 2Q25. Separately, we introduce 2028 forecasts.

Exhibit 5: GS EBITDA Revisions

<table><tr><td colspan="4">EBITDA Estimates (adj)</td></tr><tr><td>Period</td><td>New</td><td>Old</td><td>% Change</td></tr><tr><td>2Q26</td><td>36</td><td>19</td><td>86%</td></tr><tr><td>3Q26</td><td>44</td><td>30</td><td>50%</td></tr><tr><td>FY2026</td><td>136</td><td>82</td><td>66%</td></tr><tr><td>FY2027</td><td>154</td><td>157</td><td>-2%</td></tr><tr><td>FY2028</td><td>167</td><td>-</td><td>-</td></tr></table>

Source: GS Global Investment Research

Exhibit 6: Existing Home Sales Remain Subdued  
in thousands  
![](images/cf1d19afbfac39f87c6e90569195608ad171ee20362c75a7d42860b1e69e7493.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | United States Housing starts (level, SAAR) | United States Existing home sales (% chg yoy) |
|------|---------------------------------------------|-----------------------------------------------|
| 2014 | 1,000                                       | -                                             |
| 2015 | 1,100                                       | 10%                                           |
| 2016 | 1,200                                       | 5%                                            |
| 2017 | 1,150                                       | 0%                                            |
| 2018 | 1,250                                       | -5%                                           |
| 2019 | 1,300                                       | 0%                                            |
| 2020 | 1,400                                       | 5%                                            |
| 2021 | 1,600                                       | 10%                                           |
| 2022 | 1,550                                       | -15%                                          |
| 2023 | 1,450                                       | -20%                                          |
| 2024 | 1,350                                       | 0%                                            |
| 2025 | 1,350                                       | 5%                                            |
| 2026 | 1,300                                       | 5%                                            |
| 2027 | 1,350                                       | 5%                                            |
</details>

Source: GS Global Investment Research

Exhibit 7: US New home sales (level, SAAR)  
in thousands  
![](images/a2bf486feb1bd018e631a598f63295d335402ccd7c6f6045057099e814e9b779.jpg)

<details>
<summary>bar chart</summary>

| Year | Value |
|---|---|
| 2014 | 440 |
| 2015 | 500 |
| 2016 | 560 |
| 2017 | 615 |
| 2018 | 615 |
| 2019 | 685 |
| 2020 | 830 |
| 2021 | 770 |
| 2022 | 635 |
| 2023 | 665 |
| 2024 | 685 |
| 2025 | 670 |
| 2026 | 670 |
| 2027 | 645 |
</details>

Source: GS Global Investment Research

## Valuation and Key Risks:

We are Sell rated on KRO with a 12-month price target of \$7 (from \$5 prior), which is based on a 9.0x EV/EBITDA on our 2027 estimates (from 14x 2026 EBITDA prior). The change in our target multiple is due to roll forward of the multiple year.

We see four upside risks as it relates to our rating on KRO: 1) Demand could strengthen into the TiO2 industry's supply side reduction moves driving supply-demand to tighten meaningfully leading to unexpected price increases. 2) The cost of upstream titanium ore could weaken meaningfully, helping Kronos and negatively impacting more integrated peers. Kronos is much more exposed to titanium ore purchased from large miners/refiners. 3) The ownership structure could change which may bring more attention, more float and new investors into the stock. With only \~20% float, KRO may not appear on the screens of large funds.

## Disclosure Appendix

## Reg AC

We, Duffy Fischer, Ramsey Abdulrahim, Mike Harris and Jordan Lee, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Duffy Fischer GS & Co. LLC, Ramsey Abdulrahim GS & Co. LLC, Mike Harris GS & Co. LLC, Jordan Lee GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Kronos Worldwide Inc. is/are relative to the other companies in its/their coverage universe: Air Products & Chemicals Inc., Axalta Coating Systems Ltd., CF Industries Holdings, Chemours, Corteva Inc., Dow Inc., Eastman Chemical Co., Element Solutions Inc., FMC Corp., Huntsman Corp., Kronos Worldwide Inc., Linde PLC, LyondellBasell, Mosaic Co., Nutrien Ltd., Olin Corp., PPG Industries Inc., Sherwin-Williams Co., Tronox Holdings, Westlake Corp.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS had a non-securities services client relationship during the past 12 months with: Kronos Worldwide Inc. (\$7.04)

GS makes a market in the securities or derivatives thereof: Kronos Worldwide Inc. (\$7.04)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, C

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
