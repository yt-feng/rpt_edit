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
# Company Horizon Robotics

Rating Buy

Asia China

Reuters 9660.HK

Bloomberg 9660 HK

Consumer
Autos & Auto Technology

# May autonomous-driving SoC up $35 \%$ YoY; front camera chip down $11 \%$ YoY

## Estimated high-level autonomous-driving systems (Level 2+/Level 3)

penetration reaches 47.3% in May 2026

According to statistics from NE Times, China's overall autonomous-driving system-on-chip (SoC) volume increased 10% YoY and 26% MoM to \~760k units in May 2026. Dividing the overall SoC volume by China's May retail sales volume of 1.47 million units yields a penetration rate of 51.8% (up 14.0 ppts YoY and 6.8 ppts MoM). We treat this as a proxy to forecast the high-level autonomous-driving systems (Level 2+/Level 3 with navigation on autopilot [NOA]) penetration rate. In the months of January to April, this proxy rate is on average 4.5 ppts higher than the actual high-level autonomous-driving systems penetration rate. Assuming the same gap is unchanged in May, the implied Level 2+/Level 3 penetration rate in May would be 47.3% (up 19.1 ppts YoY and 6.8 ppts MoM).

## Horizon Robotics' autonomous-driving SoC volume up 35% YoY in May

The top eight players accounted for \~98% of market share in the month, with the breakdown as follows: Nvidia's deliveries declined 19% YoY to 313,125 units (41.2% market share), Huawei's volume increased 73% YoY to 122,557 units (16.1% market share), Tesla's deliveries increased 22% YoY to 95,446 units (12.6% market share), and Horizon Robotics' volume grew 35% YoY to 91,640 units (12.1% market share). Qualcomm's deliveries increased 261% YoY to 59,338 units (7.8% market share), NIO's volume increased 57% YoY to 24,356 units (3.2% market share), Texas Instruments' deliveries declined 53% YoY to 18,014 units (2.4% market share), and XPeng delivered 16,937 units (2.2% market share).

We note that Horizon Robotics' autonomous-driving SoC volume increased 35% YoY and 12% MoM to 91,640 units in May, ranking fourth among the autonomous-driving SoC makers in China (after Nvidia, Huawei and Tesla). Horizon Robotics' 5M 2026 delivery volume was 324,344 units (up 28% YoY), translating into a 11.4% market share (up 1.9 ppt YoY).

## Horizon Robotics' ADAS front camera chip volume down 11% YoY in May

According to statistics from NE Times, China's overall advanced driver assistance system (ADAS) front camera chip volume decreased 31% YoY to \~501k units in May 2026, with the top five players accounting for \~97% of market share in the month. Breaking this down, Mobileye's deliveries declined 36% YoY to 204,907 units (40.9% market share), followed by Renesas' volume declining 44% YoY to 151,143 units (30.2% market share). Meanwhile, Horizon Robotics' deliveries declined 11% YoY to 63,821 units (12.7% market share), Axera's volume

## DB AG/Hong Kong

Date 6 July 2026

Rating Buy
Price target (HKD) 9.40
Price at 3 Jul 26 4.68
52-week range 10.81 – 3.61

Valuation & Risks

Bin Wang

Research Analyst

+852-220-35496

## Wei Huang

Research Associate

+852-2203-7057

increased $178\%$ YoY to 38,260 units (7.6% market share), and AMD's deliveries fell $13\%$ YoY to 30,062 units (6.0% market share).

We note that Horizon Robotics' ADAS front camera chip volume decreased 11% YoY to 63,821 units in May, ranking it third among the ADAS front camera chipmakers in China (after Mobileye and Renesas). Horizon Robotics' 5M 2026 delivery volume was 312,410 units (down 35% YoY), accounting for 11.4% market share (down 1.6 ppt YoY).

## Introduces HSD 2.0 with advanced dual-engine autonomous driving architecture

Horizon Robotics has unveiled its second-generation "Horizon Superdrive (HSD V2.0)" full-scenario autonomous driving system, marking a significant architectural shift from a single-stage, end-to-end modular design to a sophisticated "world model + reinforcement learning" dual-engine framework. This innovative architecture is engineered to deliver a comprehensive leap in driving capabilities. The "HSD V2.0" leverages a "world model" that, through training on real-world expert driver data, gains a spatiotemporal understanding to simulate complex long-tail scenarios. Critically, this world model can dynamically predict future traffic states, enabling the system to perform defensive driving and navigation maneuvers that closely mimic those of a professional human driver. Furthermore, HSD V2.0 optimizes the computing efficiency of Horizon Robotics' "Journey 6P" chip through persistent toolchain improvements.

Complementing its world model, Horizon Superdrive (HSD) V2.0 incorporates a reinforcement learning model that ensures continuous self-iteration and evolution, fostering ongoing capability improvement across critical domains including general driving, parking, safety, and the handling of unpredictable long-tail scenarios. This dual-engine approach establishes a sustainable and self-evolving technical evolutionary path for intelligent driving systems, promising continuous improvements in autonomous functionality over time. A key advancement lies in the application of the Occupancy Network (OCC) to active safety features such as Automatic Emergency Braking (AEB), Automatic Emergency Steering (AES), and Anti-maloperation for Accelerator Pedal (AMAP). This means the vehicle's active safety system has been upgraded from traditional "whitelist" object recognition to an "occupancy network," significantly enhancing its ability to detect and respond to unforeseen and irregular obstacles, thereby improving overall vehicle safety.

Figure 1: Monthly ADCU chip and ADAS front camera chip volume summary

<table><tr><td>(unit)</td><td>May-26</td><td>YoY</td><td>MoM</td><td>5M 2026</td><td>YoY</td></tr><tr><td>DCU-Chip Provider</td><td>760,012</td><td>10%</td><td>26%</td><td>2,833,872</td><td>7%</td></tr><tr><td>Nvidia</td><td>313,125</td><td>-19%</td><td>4%</td><td>1,292,375</td><td>-11%</td></tr><tr><td>Tesla</td><td>95,446</td><td>22%</td><td>82%</td><td>373,540</td><td>-8%</td></tr><tr><td>Huawei</td><td>122,557</td><td>73%</td><td>112%</td><td>341,218</td><td>36%</td></tr><tr><td>Horizon Robotics</td><td>91,640</td><td>35%</td><td>12%</td><td>324,344</td><td>28%</td></tr><tr><td>Texas Instruments</td><td>18,014</td><td>-53%</td><td>19%</td><td>90,131</td><td>-36%</td></tr><tr><td>Qualcomm</td><td>59,338</td><td>261%</td><td>35%</td><td>176,228</td><td>157%</td></tr><tr><td>Xpeng</td><td>16,937</td><td></td><td>3%</td><td>66,222</td><td></td></tr><tr><td>NIO</td><td>24,356</td><td>57%</td><td>9%</td><td>107,632</td><td>594%</td></tr></table>

DCU-Chip Provider Market share

<table><tr><td>Nvidia</td><td>41.2%</td><td>-14.6%</td><td>-8.6%</td><td>45.6%</td><td>-8.8%</td></tr><tr><td>Tesla</td><td>12.6%</td><td>1.3%</td><td>3.9%</td><td>13.2%</td><td>-2.1%</td></tr><tr><td>Huawei</td><td>16.1%</td><td>5.8%</td><td>6.5%</td><td>12.0%</td><td>2.6%</td></tr><tr><td>Horizon Robotics</td><td>12.1%</td><td>2.3%</td><td>-1.5%</td><td>11.4%</td><td>1.9%</td></tr><tr><td>Texas Instruments</td><td>2.4%</td><td>-3.2%</td><td>-0.1%</td><td>3.2%</td><td>-2.1%</td></tr><tr><td>Qualcomm</td><td>7.8%</td><td>5.4%</td><td>0.5%</td><td>6.2%</td><td>3.6%</td></tr><tr><td>Xpeng</td><td>2.2%</td><td>2.2%</td><td>-0.5%</td><td>2.3%</td><td>2.3%</td></tr><tr><td>NIO</td><td>3.2%</td><td>0.9%</td><td>-0.5%</td><td>3.8%</td><td>3.2%</td></tr></table>

<table><tr><td>ADAS Front Camera Chip</td><td>500,995</td><td>-31%</td><td>6%</td><td>2,736,318</td><td>-25%</td></tr><tr><td>Mobileye</td><td>204,907</td><td>-36%</td><td>1%</td><td>1,278,484</td><td>-19%</td></tr><tr><td>Renesas</td><td>151,143</td><td>-44%</td><td>13%</td><td>793,590</td><td>-38%</td></tr><tr><td>Horizon Robotics</td><td>63,821</td><td>-11%</td><td>9%</td><td>312,410</td><td>-35%</td></tr><tr><td>AMD</td><td>30,062</td><td>-13%</td><td>-2%</td><td>161,499</td><td>-3%</td></tr><tr><td>Axera</td><td>38,260</td><td>178%</td><td>-1%</td><td>137,477</td><td>181%</td></tr></table>

ADAS Front Camera Chip market share

<table><tr><td>Mobileye</td><td>40.9%</td><td>-3.3%</td><td>-2.0%</td><td>46.7%</td><td>3.9%</td></tr><tr><td>Renesas</td><td>30.2%</td><td>-6.6%</td><td>1.9%</td><td>29.0%</td><td>-6.0%</td></tr><tr><td>Horizon Robotics</td><td>12.7%</td><td>2.8%</td><td>0.3%</td><td>11.4%</td><td>-1.6%</td></tr><tr><td>AMD</td><td>6.0%</td><td>1.3%</td><td>-0.5%</td><td>5.9%</td><td>1.4%</td></tr><tr><td>Axera</td><td>7.6%</td><td>5.7%</td><td>-0.6%</td><td>5.0%</td><td>3.7%</td></tr><tr><td colspan="6">Source: NE Times</td></tr></table>

## Appendix 1

## Important Disclosures

<table><tr><td>Company</td><td>Ticker</td><td>Recent price</td><td>Disclosure</td></tr><tr><td>Horizon Robotics</td><td>9660.HK</td><td>4.68 (HKD) 3 Jul 26</td><td>NA</td></tr></table>

Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources.

For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s). In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Bin Wang.

Historical recommendations and target price: Horizon Robotics (9660.HK)

![](images/3e0d92ece6f3d84645d3274f7efb926a54ba58d2d9e99941fb45b68a0ca042e9.jpg)

<table><tr><td>1.</td><td>30 Dec 24</td><td>Price target: 5 (HKD), close price 3.73 (HKD), Recommendation: Buy, Analyst: Bin Wang</td></tr><tr><td>2.</td><td>24 Mar 25</td><td>Price target: 9 (HKD), close price 7.39 (HKD), Recommendation: Buy, Analyst: Bin Wang</td></tr><tr><td>3.</td><td>27 Aug 25</td><td>Price target: 8.8 (HKD), close price 7.94 (HKD), Recommendation: Buy, Analyst: Bin Wang</td></tr><tr><td>4.</td><td>29 Sep 25</td><td>Price target: 10.5 (HKD), close price 9.59 (HKD), Recommendation: Buy, Analyst: Bin Wang</td></tr><tr><td>5.</td><td>19 Mar 26</td><td>Price target: 9.4 (HKD), close price 7.25 (HKD), Recommendation: Buy, Analyst: Bin Wang</td></tr></table>

Company rating dispersion and banking relationships

<table><tr><td>DBSI Companies under Coverage</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Covered</td><td>57%</td><td>43%</td><td>0%</td></tr><tr><td>w/ Banking relationship</td><td>43%</td><td>35%</td><td>0%</td></tr><tr><td>w/ MiFID services</td><td>63%</td><td>50%</td><td>67%</td></tr></table>

<table><tr><td>Global Companies under Coverage</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Covered</td><td>57%</td><td>41%</td><td>2%</td></tr><tr><td>w/ Banking relationship</td><td>47%</td><td>34%</td><td>31%</td></tr><tr><td>w/ MiFID services</td><td>75%</td><td>68%</td><td>94%</td></tr></table>

## Company Rating and Dispersion Key

The above table provides a snapshot of DB's company research rating distribution across our covered companies. We also present the percentage of companies where DB has provided Investment Banking Services in the past 12 months and/or MIFID Investment and Ancillary services, in the past 12 months. Please see the key and definition of our rating below.

Note - percentages are rounded so may not total 100%.

Covered: The overall rating distribution across all companies under coverage with a rating.

w/Banking relation: Percentage of companies under coverage with a rating within each of the "buy", "hold" and "sell" categories for which DB has provided Investment Banking Services within the previous 12 months.

w/MiFID services: Percentage of companies under coverage with a rating within each of the "buy", "hold" and "sell" categories for which DB has provided MIFID Investment and Ancillary services within the previous 12 months.

Buy/Hold/Sell Percentages: These percentages reflect the proportion of companies within each category that have been assigned the corresponding rating, based on our 12-month view of Total Shareholder Return (TSR).

## Rating definitions:

Buy: Based on a current 12-month view of TSR, we recommend that investors buy the stock.

Sell: Based on a current 12-month view of TSR, we recommend that investors sell the stock.

Hold: We take a neutral view on the stock 12-months out and, based on this time horizon, do not recommend either a Buy or Sell.

TSR: Total Shareholder Return. Percentage change in share price from current price to projected target price plus projected dividend yield.

Newly issued research recommendations and target prices supersede previously published research.

## Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. DB and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of DB AG and its affiliates, which includes investment banking, trading and principal trading revenues.

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of DB and are subject to change without notice. DB provides liquidity for buyers and sellers of securities issued by the companies it covers. DB analysts sometimes have shorter-term trade ideas that may be inconsistent with DB's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website (https://research.db.com/Research/), and can be found on the general coverage list and also on the covered company's page. A Catalyst Call represents a high-conviction belief by an analyst that a stock will outperform or underperform the market and/or a specified sector over a time frame of no less than two weeks and no more than three months. In addition to Catalyst Calls, analysts may occasionally discuss with our clients, and with

[中间内容因长度限制已省略]

ed, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau  
Group Chief Economist and Global Head of Research

<table><tr><td>Pam Finelli
COO and Head of Fixed Income Research</td><td>Steve Pollard
Global Head of Company Research and Sales</td><td>Jim Reid
Global Head of Macro and Thematic Research</td><td>Tim Rokossa
Head of European Company Research</td></tr><tr><td>Matthew Barnard
Head of Americas
Company Research</td><td>Debbie Jones
Global Head of Sustainability and Data Innovation, Research</td><td>Robin Winkler
Head of German Macro Research</td><td>Sameer Goel
Global Head of EM &amp; APAC Research</td></tr><tr><td>Francis Yared
Global Head of Rates Research</td><td>George Saravelos
Global Head of FX Research</td><td>Peter Hooper
Vice-Chair of Research</td><td>Nilendra de-Mel
Head of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Japan</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td>Tel: (852) 2203 8888</td><td>Tel: (81) 3 6730 1000</td></tr></table>

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South TowerSingapore 048583Tel: (65) 6423 8001</td></tr></table>
"""
