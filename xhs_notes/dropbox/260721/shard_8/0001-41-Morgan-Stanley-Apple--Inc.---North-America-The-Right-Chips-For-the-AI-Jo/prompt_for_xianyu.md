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
Apple, Inc. | North America

# The Right Chips For the AI Job?

Apple's AI server silicon is potentially facing performance challenges that could (1) dampen Siri AI performance and/or (2) force greater (costlier) adoption of NVDA chips in GCP. Our checks indicate no change to M-series builds, with AAPL's first ASIC coming in C1H27, followed by a 2nd gen in '28.

## Key Takeaways

Last week The Information reported performance of Apple's M2 Ultra AI server chip was "struggling" and that Apple is on the lookout for chip acquisitions.

\- Apple will be reliant on these M series AI server chips to process more complex Siri AI workloads not run on-device.

Apple's Baltra ASIC is "on plan" for small volumes in C1H27, with a 2nd gen AI server ASIC to follow in 2028 that could potentially match merchant silicon.

Why does this matter? A lack of power/performant chips in Private Cloud Compute could either (1) degrade Siri AI performance or (2) force more workloads to GCP.

Signposts to track Apple's AI server silicon? SolC bookings at TSMC, CoWoS bookings at TSMC, 2nd-Gen ASIC tape-out progress, and Apple's capex trajectory.

What's new, and what are the potential implications? Last week, The Information reported that Apple is "on the lookout for acquisitions of chip companies to boost its efforts to build server chips for running AI", noting that the performance of Apple's M2 Ultra powered AI servers is "struggling". We have no knowledge of any pending transactions, and Apple has not commented in response to the report. The Information also reported that a future version of Apple's AI server chip, code-named "Baltra" has been delayed, citing people familiar with the project. While Apple's internal AI efforts are still very early days – with Siri AI expected to launch this Fall – and more skewed to on-device inferencing than peers, the risk of not developing a chip capable of powering inference workloads in Apple's Private Cloud Compute (PCC) has two potentially major ramifications – (1) Apple could be forced to use underperforming chips in PCC for a period of time, which could seriously degrade the performance/latency of more complex Siri AI queries, and/or (2) Apple would be forced to run more Siri AI workloads in Google Cloud, a likely costly endeavour.

## A history of Apple's silicon efforts, and why AI chips are a new beast for Apple.

Apple's silicon expertise has been concentrated in the power-efficient chips used in iPhone, Mac, and iPad – which started with the A4 in 2010, debuting on the original iPad and iPhone 4. These System on a Chip (SoC) solutions – the A series (powering the iPhone, base iPad, etc.), M series (powering the Mac, iPad Pro/Air), S Series (Apple Watch), etc. – are unmatched in delivering performance and efficiency (silicon/hardware/software vertical integration helps as well). In fact, Apple's silicon

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Erik W Woodring</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Erik.Woodring@morganstanley.com</td><td>+1 212 296-8083</td></tr><tr><td colspan="2">Dylan Liu</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Dylan.Liu@morganstanley.com</td><td>+1 212 761-4519</td></tr><tr><td colspan="2">Maya C Neuman</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Maya.Neuman@morganstanley.com</td><td>+1 212 761-1946</td></tr><tr><td colspan="2">Rauf Ural</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Rauf.Ural@morganstanley.com</td><td>+1 212 761-5958</td></tr></table>

## Apple, Inc. (AAPL.O, AAPL US)

## IT Hardware | United States of America

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Cautious</td></tr><tr><td>Price target</td><td>$360.00</td></tr><tr><td>Shr price, close (Jul 17, 2026)</td><td>$333.74</td></tr><tr><td>Mkt cap, curr (mm)</td><td>$4,912,741</td></tr><tr><td>52-Week Range</td><td>$334.99-201.50</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

team is so talented that it had TSMC (covered by Charlie Chan) customize an advanced packaging line for the A series chip. However, Apple doesn't have a long history in designing power-hungry but also extremely performant chips, which are required to run AI inferencing workloads in PCC. This is why, for example, the most performant Siri AI workloads are expected to run on NVDA chips on Google's Cloud (NVDA is covered by Joe Moore; Alphabet is covered by Brian Nowak).

## What we know about Apple's M2 Ultra and "Baltra" from our supply chain

checks. Earlier this year, we published that our checks indicated TSMC's SolC (System on Integrated Circuit) output for Apple in 2027 would match AMD's output, indicating strong volumes for what we believed would be Apple's AI server chip. Our checks would still indicate Apple has not cancelled any packaging capacity at TSMC, but SolC technology is also used in Apple's M5 Max and M5 Ultra, its highest performance M-series chips debuted in March '26, which could indicate these volumes are for chips supporting a number of devices – Mac, workstations, AI servers, etc. Furthermore, we learned that the 'Baltra' ASIC (likely produced in partnership with Broadcom – covered by Joe Moore – who Apple just announced a \$30B partnership with) was always targeting C1H27 volume production, which will be quite small at first as it is Apple's first high-power chip, and therefore definitionally more experimental. Apple's 2nd Gen AI ASIC is likely to enter volume production in 2028, and we have heard the power envelope will potentially be close to merchant AI GPUs (e.g. NVIDIA's GPUs).

The signposts we are tracking to stay on top of this debate: (1) SolC capacity bookings at TSMC – this remains a key indicator of Apple’s M-series trajectory as well as broader AI ASIC demand; (2) CoWoS capacity bookings at TSMC – while Apple has yet to emerge as a major CoWoS user, moving toward a power envelope closer to NVIDIA’s AI GPUs would likely necessitate HBM adoption, and in turn, CoWoS packaging; (3) Second-generation AI ASIC tape-out progress – as noted, we expect Apple’s second-generation AI ASIC to reach volume production as early as 2028, implying a potential tape-out sometime in 2027; and (4) Apple’s capex trajectory – although capex has already been trending higher, a successful volume ramp of a second-generation AI ASIC would likely drive further acceleration. It’s also worth keeping in mind that Apple may refer to these technologies differently within the foundry ecosystem (i.e. not literally “CoWoS” or “SolC”). That said, our checks suggest that the underlying toolsets and process technologies are broadly comparable, so we use these industry-standard terms for clarity and ease of discussion.

<table><tr><td colspan="2">Risk Reward Themes</td></tr><tr><td>Disruption:</td><td>Positive</td></tr><tr><td>New Data Era:</td><td>Positive</td></tr><tr><td>Pricing Power:</td><td>Positive</td></tr><tr><td colspan="2">View descriptions of Risk Rewards Themes here</td></tr></table>

## Risk Reward – Apple, Inc. (AAPL.O)

More Near-Term Cost Uncertainties Before a Catalyst-Laden 2H

## PRICE TARGET \$360.00

Our \$360 PT is based on 9.1x EV/Sales FY27 multiple, which is derived from a regression of tech and consumer platform peers. Our price target implies \~35x P/E on \$10.30 FY27 EPS.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/739721abdefbad7347b35dd3fb9fcb513c25ade9e00c2140a634844d1f81b6c9.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/a06dba7065ae49a9b7330e33c69dcfc23bb514c4fdeebbf3815490f051c1f9a4.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target  
Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 17 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## OVERWEIGHT THESIS

With the most elongated iPhone replacement cycles, new AI features rolling out around the world, and a renewed focus on device form factor changes, we believe Apple can accelerate iPhone growth starting in FY26, with replacement cycles peaking as aged installed base starts to upgrade. When combined with consistent, double digit services growth and moderate operating leverage, we believe Apple can earn \$8.89 in FY26 and \$10.30 by FY27. Memory cost dynamic could create uncertainties in the near term. Longer-term, investments in AI, payments, cloud, health, and home, and long runway to grow spend per user from \$1/day today are key arguments for sustained long-term growth and value creation.

![](images/273681d00fc6fee6b2b915a993637305f7f28756e3e32e74e88ee6ca3df422b4.jpg)  
Source: Refinitiv, MS

## Risk Reward Themes

## BULL CASE

\$453.00

11x EV/Sales FY27; \~41x Bull FY27 P/E of \$11.02

iPhone replacement cycles accelerate in FY26/FY27 with Robotics as an long-term upside. Consumer demand returns, and stronger than expected iPhone 17 upgrade intentions + mix shift to higher end iPhones drives mid-teens Y/Y iPhone revenue growth, while rising component costs are mitigated given Apple's bargaining power against consumers and the supply chain. Our bull case valuation implies a 41.1x P/E multiple on FY27 Bull EPS, which embeds \$22 per share of upside from its Robotics efforts.

## BASE CASE

\$360.00

9.1x EV/Sales FY27 or \~35x FY27 EPS of \$10.30

Services and margins remain resilient, while investors start to expect stronger iPhone cycles ahead. Revenue grows 15% Y/Y in FY27, driven by 10%+ Services growth and mid-teens % Products growth. GM may contract Y/Y in FY27 driven by higher Product revenue mix and memory costs, while Apple leverages the supply chain and repricing to mitigate the cost impact. The iPhone replacement cycle is peaking and creates pent up demand for upgrades in FY27.

## BEAR CASE

\$194.00

6.3x EV/Sales FY27; 24.6x FY27 Bear EPS of \$7.89

iPhone 17 cycle disappoints as consumer spending weakens more than expected amidst synthetic price increases. Growth slows further across the portfolio as discretionary income is pressured by hard landing, leading to just LSD of Product rev growth and decelerating Services rev growth in FY26. With revenue slightly growing but margin contracting, FY26 EPS will only grow MSD to \~\$7.36. Our bear case valuation implies a 24.6x FY27 P/E, below T5Y avg of 26.0x due to plateauing Services profit mix.

## Risk Reward – Apple, Inc. (AAPL.O)

## KEY EARNINGS INPUTS

<table><tr><td>Drivers</td><td>Sep 2025</td><td>Sep 2026e</td><td>Sep 2027e</td><td>Sep 2028e</td></tr><tr><td>Total Revenue Growth (Y/Y) (%)</td><td>6.4</td><td>16.6</td><td>14.9</td><td>5.8</td></tr><tr><td>iPhone Revenue Growth (Y/Y) (%)</td><td>4.2</td><td>23.6</td><td>19.1</td><td>4.2</td></tr><tr><td>Services Revenue Growth (Y/Y) (%)</td><td>13.5</td><td>14.0</td><td>12.1</td><td>11.3</td></tr><tr><td>Gross Margin (%)</td><td>46.9</td><td>48.0</td><td>47.5</td><td>48.0</td></tr><tr><td>EPS Growth (Y/Y) (%)</td><td>10.6</td><td>19.1</td><td>15.9</td><td>7.5</td></tr></table>

## INVESTMENT DRIVERS

\- Positive iPhone build revisions / clearer signs of accelerating replacement cycles

• Services revenue growth reacceleration

\- Apple Intelligence feature and distribution expansion

\- New product launches in home, health and AI

## GLOBAL REVENUE EXPOSURE

![](images/2de8d4a5fa2486c362ea9af05ae30d4d58b9ea461b8af0fc75921cb8e04729ce.jpg)

APAC, ex Japan, Mainland China and India
0-10%
India
0-10%
Japan
0-10%
Latin America
0-10%
MEA
0-10%
UK
0-10%
Europe ex UK
10-20%
Mainland China
10-20%
30-40% North America

Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS

<table><tr><td>3/5BEST</td><td>24 MonthHorizon</td><td>1/5MOST</td><td>3 MonthHorizon</td></tr></table>

Source: Refinitiv, FactSet, MS; 1 is the highest favored Quintile and 5 is the least favored Quintile

## RISKS TO PT/RATING

RISKS TO UPSIDE

\- iPhone 17 outperforms expectations - Apple Intelligence adoption surprises to the upside

• Apple pulls forward form factor changes

• Services growth re-accelerates despite tougher compares

• Gross margins surprise positively

## RISKS TO DOWNSIDE

\- Weak consumer spending limits iPhone upgrade rates

• Higher memory input costs

\- Limited progress on AI features

\- Geopolitical tensions

\- Increased regulation, particularly with App Store

## OWNERSHIP POSITIONING

<table><tr><td>Inst. Owners, % Active</td><td>47.5%</td><td></td><td></td><td></td></tr><tr><td>HF Sector Long/Short Ratio</td><td>2.1x</td><td></td><td></td><td></td></tr><tr><td>HF Sector Net Exposure</td><td>29.5%</td><td></td><td></td><td></td></tr></table>

Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

## MS ESTIMATES VS. CONSENSUS

Sales / Revenue
( \$, mm )
557,504
Note: There are not sufficient brokers supplying consensus data for this metric

EBITDA
(\$, mm)
192,404
Note: There are not sufficient brokers supplying consensus data for this metric

Net income (\$, mm)
149,643
Note: There are not sufficient brokers supplying consensus data for this metric

EPS
(\$) 10.30
Note: There are not sufficient brokers supplying consensus data for this metric

Source: Refinitiv, MS

## Apple (AAPL) Financial Model

Exhibit 1: Apple Income Statement

<table><tr><td rowspan="2">($ in millions)</td><td colspan="4">2025A</td><td colspan="4">2026E</td><td colspan="4">2027E</td></tr><tr><td>Dec-24</td><td>Mar-25</td><td>Jun-25</td><td>Sep-25</td><td>Dec-25</td><td>Mar-26</td><td>Jun-26</td><td>Sep-26</td><td>Dec-26</td><td>Mar-27</td><td>Jun-27</td><td>Sep-27</td></tr><tr><td>Revenues</td><td>124,300</td><td>95,359</td><td>94,036</td><td>102,466</td><td>143,756</td><td>111,184</td><td>108,771</td><td>121,635</td><td>150,274</td><td>134,142</td><td>135,287</td><td>137,802</td></tr><tr><td>iPhone</td><td>69,138</td><td>46,841</td><td>44,582</td><td>49,025</td><td>85,269</td><td>56,994</td><td>54,207</td><td>62,581</td><td>85,657</td><td>75,145</td><td>74,791</td><td>72,997</td></tr><tr><td>iPad</td><td>8,088</td><td>6,402</td><td>6,581</td><td>6,952</td><td>8,595</td><td>6,914</td><td>6,848</td><td>7,892</td><td>9,223</td><td>7,106</td><td>7,444</td><td>8,043</td></tr><tr><td>Mac</td><td>8,987</td><td>7,949</td><td>8,046</td><td>8,726</td><td>8,386</td><td>8,399</td><td>8,839</td><td>9,702</td><td>9,529</td><td>9,304</td><td>9,293</td><td>10,500</td></tr><tr><td>Wearables, Home and Accessories</td><td>11,747</td><td>7,522</td><td>7,404</td><td>9,013</td><td>11,493</td><td>7,901</td><td>7,796</td><td>9,106</td><td>12,227</td><td>8,381</td><td>8,454</td><td>9,952</td></tr><tr><td>Services</td><td>26,340</td><td>26,645</td><td>27,423</td><td>28,750</td><td>30,013</td><td>30,976</td><td>31,081</td><td>32,354</td><td>33,639</td><td>34,205</td><td>35,305</td><td>36,309</td></tr><tr><td>Cost of Sales</td><td>66,025</td><td>50,492</t

[中间内容因长度限制已省略]

search relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: IT Hardware

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/17/2026)</td></tr><tr><td colspan="3">Erik W Woodring</td></tr><tr><td>Apple, Inc. (AAPL.O)</td><td>O (05/26/2009)</td><td>$333.74</td></tr><tr><td>CDW Corporation (CDW.O)</td><td>O (06/23/2026)</td><td>$133.24</td></tr><tr><td>Cricut Inc (CRCT.O)</td><td>U (08/12/2021)</td><td>$4.63</td></tr><tr><td>Dell Technologies Inc. (DELL.N)</td><td>E (06/01/2026)</td><td>$396.34</td></tr><tr><td>Everpure, Inc. (P.N)</td><td>E (06/11/2024)</td><td>$69.38</td></tr><tr><td>Garmin Ltd (GRMN.N)</td><td>E (02/18/2026)</td><td>$249.56</td></tr><tr><td>GoPro Inc (GPRO.O)</td><td>U (12/12/2023)</td><td>$0.66</td></tr><tr><td>Hewlett Packard Enterprise (HPE.N)</td><td>E (11/16/2025)</td><td>$45.82</td></tr><tr><td>HP Inc. (HPQ.N)</td><td>U (11/16/2025)</td><td>$24.84</td></tr><tr><td>IBM (IBM.N)</td><td>E (01/18/2023)</td><td>$212.67</td></tr><tr><td>Ingram Micro (INGM.N)</td><td>E (06/11/2025)</td><td>$29.28</td></tr><tr><td>Kornit Digital Ltd. (KRNT.O)</td><td>E (11/06/2025)</td><td>$15.03</td></tr><tr><td>Logitech International SA (LOGI.O)</td><td>U (01/20/2026)</td><td>$102.83</td></tr><tr><td>NetApp Inc (NTAP.O)</td><td>U (01/20/2026)</td><td>$163.88</td></tr><tr><td>Resideo Technologies Inc (REZI.N)</td><td>O (08/11/2025)</td><td>$35.83</td></tr><tr><td>Seagate Technology (STX.O)</td><td>O (03/26/2024)</td><td>$787.66</td></tr><tr><td>SmartRent, Inc. (SMRT.N)</td><td>++</td><td>$0.96</td></tr><tr><td>Sonos Inc. (SONO.O)</td><td>E (11/06/2025)</td><td>$15.11</td></tr><tr><td>TD Synnex Corporation (SNX.N)</td><td>O (06/11/2025)</td><td>$242.62</td></tr><tr><td>Teradata (TDC.N)</td><td>O (04/08/2025)</td><td>$30.52</td></tr><tr><td>Western Digital (WDC.O)</td><td>O (04/16/2025)</td><td>$477.22</td></tr><tr><td colspan="3">Sanjit K Singh</td></tr><tr><td>Nutanix Inc (NTNX.O)</td><td>E (01/12/2026)</td><td>$55.08</td></tr></table>

\* Historical prices are not split adjusted.  
Stock Ratings are subject to change. Please see latest research for each company.

© 2026 MS
"""
