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
# Space Exploration Technologies Corp. | North America

## DVFS

There's vertical integration. There's extreme vertical integration. And then there's SpaceX. We struggle to think of any other company that exhibits similar levels of Dimensionality, Verticality, Flexibility and Speed.

Exhibit 1: DVFS: Dimensionality, Verticality, Flexibility, Speed

![](images/6b0c9338dc033dbb9d451bc513a44c97ed9d3b42ba49d70726f74654e966a920.jpg)  
Source: MS

Please see here for our SpaceX Initiation: SpaceX: AI's Final Frontier; Initiate at Overweight, PT \$300 (7 Jul 2026)

Dimensionality. Breadth. Polymathic ability that spans a wide range of capability. Cohesion and surface area create ecosystem value. Example: Lowering cost of mass to orbit (\$/kg) unlocks opportunity in space based AI infrastructure. Or AI sats using Starlink sats as a comms relay back to earth.

Verticality. Depth. In-house expertise from upstream supply chain down to after sales/service. Example: Identifying the top impediment for time to power in terrestrial AI is the natural gas (CCGT) turbine. Identifying supply of vanes and blades as the key impediment. SpaceX to make their own vanes and blades.

Flexibility. Ability to learn and pivot from, especially from mistakes. Example: Gigawatt scale compute clusters can be sold in a neocloud model to 3rd party AI

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Adam Jonas, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Adam.Jonas@morganstanley.com</td><td>+1 212 761-1726</td></tr><tr><td colspan="2">William Tackett, CFA</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>William.Tackett@morganstanley.com</td><td>+1 212 761-6028</td></tr></table>

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$300.00</td></tr><tr><td>Shr price, close (Jul 13, 2026)</td><td>$139.14</td></tr><tr><td>52-Week Range</td><td>$225.64-139.14</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS ($)**</td><td>(1.69)</td><td>0.28</td><td>2.18</td><td>6.29</td></tr><tr><td>Prior EPS ($)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>P/E</td><td>NM</td><td>491.4</td><td>63.8</td><td>22.1</td></tr><tr><td>EPS ($)§</td><td>-</td><td>(0.59)</td><td>0.64</td><td>3.21</td></tr><tr><td>Div yld (%)</td><td>-</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
§ = Consensus data is provided by Refinitiv Estimates
e = MS estimates

<table><tr><td colspan="6">QUARTERLY EPS ($)</td></tr><tr><td>Quarter</td><td>2025</td><td>2026e Prior</td><td>2026e Current</td><td>2027e Prior</td><td>2027e Current</td></tr><tr><td>Q1</td><td>(0.18)</td><td>-</td><td>(0.84)a</td><td>-</td><td>0.54</td></tr><tr><td>Q2</td><td>(0.34)</td><td>-</td><td>(0.35)</td><td>-</td><td>0.55</td></tr><tr><td>Q3</td><td>(0.36)</td><td>-</td><td>0.27</td><td>-</td><td>0.54</td></tr><tr><td>Q4</td><td>(0.80)</td><td>-</td><td>0.45</td><td>-</td><td>0.56</td></tr></table>

e = MS estimates, a = Actual Company reported data

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

Constant Focus on Manufacturability & Scalability

labs with ability to shift to internal model training or end-to-end enterprise AI as Cursor scales.

Speed. Moving an order of magnitude faster than competitors (when needed). Example: Experience with local power/electric utility authorities at Tesla + in-house contractor capability enable SpaceX able to bring to market hundred-megawatt scale in 90 days - nearly 8x faster than industry benchmarks. We should mention that 'Speed' in our DVFS framework doesn't always mean fastest. Think of 'Speed' as the ability to toggle strategy and execution to the correct velocity at the right time. In some situations that may mean faster. In other situations that may mean slower. Matching velocity with mission dynamically is the key.

## A note on vertical integration.

• 80% of Starship is made in-house

\- SpaceX manufactures Starlink satellites and user terminals, builds much of its ground infrastructure, produces battery systems, and is expanding into in-house production of certain Starship propellants

\- SpaceX's Bastrop, TX facility is the largest printed circuit board (PCB) manufacturing facility in the US

\- SpaceX is expected to break ground on a foundry to make vanes and blades for nat gas turbines

\- SpaceX is building an 11-million-square-foot “Gigasat” factory in Bastrop, Texas, to vertically integrate and mass-produce AI satellites, including solar cells, electronics, communications hardware and complete spacecraft targeting production equivalent to 1 GW of orbital AI compute annually by late 2027.

\- SpaceX and Tesla are planning Terafab, an integrated semiconductor-manufacturing project expected to include chip fabrication, lithography, memory, packaging, and testing to produce 1TW of chips/year

When SpaceX builds a datacenter, they don't use general contractors - they do it all in-house - 8x faster construction time for a 100 MW-scale cluster than peers (90 days vs. 2 years). Building big projects fast is actually a product for this company.

Exhibit 2: SpaceX Vertical Integration: Starship & The Algorithm

Vertical Integration & First-Principles Thinking  
![](images/6494b9c93e1e4ba25d3e39cbc234500fd45ea5c4c41e10c3e23ab9b20f914bd8.jpg)  
Source: SpaceX, Company Data, MS

Exhibit 3: SpaceX Vertical Integration: Starlink Vertical Integration & First-Principles Thinking Constant Focus on Manufacturability & Scalability  
![](images/e99e39f7c0d9adf08eccfb9ab27e694d21d95e4c2b8af798653a773016466661.jpg)

![](images/01bde6d90840882094ff3a282759add06e83cda40df98394e999da529b84d5be.jpg)  
Source: SpaceX, Company Data, Government of Texas, MS

![](images/6f2708178b0fef32baae464111637a9898e58f6e0c6ca9e95460740458863c5c.jpg)  
\~200,000 Starlink Kits Produced In-House Per Week
To be \~500k by YE26. Bastrop, TX to be Largest PCB Manufacturing Facility in the US

## Valuation Methodology and Risks

## Space Exploration Technologies Corp. (SPCX.O)

Sum-of-the-Parts by Segment: Space, Connectivity, AI (Divided into X & Grok and Enterprise AI)

■ \$300 Price Target = sum of Space (\$8), Connectivity (\$128), X & Grok (\$12), Enterprise AI (\$152)

2040 ending forecast period

6/30/2027 valuation date

11.1% WACC; 11.9% Cost of Equity

50% Enterprise AI valuation discount for execution risk

TGR of: 4.0% Space, 4.5% connectivity, 3.0% X & Grok, 5.0% Enterprise AI

## Equates to 0.41 EV/EBIT/Growth

## Risks to Upside

■ Faster Starship reuse progress

■ Faster Starlink capacity growth

■ Stronger DTC / enterprise adoption

■ More neocloud wins

■ Cursor ARR acceleration

■ Lower AI infrastructure time to power and cost

## Risks to Downside

■ Slower Starship reuse cadence

■ Slower Starlink subscriber growth

■ Weaker enterprise AI monetization

■ Higher capex / cost per watt of compute

■ Longer time-to-power

■ Greater funding needs / dilution

■ Regulatory delays

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Adam Jonas, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Firefly Aerospace Inc, Iridium Communications Inc, MDA Space Ltd, Rocket Lab USA Inc, Viasat Inc, Virgin Galactic Holdings Inc, Voyager Technologies Inc.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Firefly Aerospace Inc, Space Exploration Technologies Corp., Voyager Technologies Inc.

Within the last 12 months, MS has received compensation for investment banking services from Firefly Aerospace Inc, Space Exploration Technologies Corp., Voyager Technologies Inc.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Firefly Aerospace Inc, Gogo Inc, Iridium Communications Inc, MDA Space Ltd, Planet Labs PBC, Rocket Lab USA Inc, Space Exploration Technologies Corp., Viasat Inc, Voyager Technologies Inc.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Gogo Inc, Iridium Communications Inc, Rocket Lab USA Inc, Space Exploration Technologies Corp., Viasat Inc, Voyager Technologies Inc.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Firefly Aerospace Inc, Gogo Inc, Iridium Communications Inc, MDA Space Ltd, Planet Labs PBC, Rocket Lab USA Inc, Space Exploration Technologies Corp., Viasat Inc, Voyager Technologies Inc. Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Gogo Inc, Iridium Communications Inc, Rocket Lab USA Inc, Space Exploration Technologies Corp., Viasat Inc, Virgin Galactic Holdings Inc, Voyager Technologies Inc.

MS & Co. LLC makes a market in the securities of Iridium Communications Inc, Space Exploration Technologies Corp., Viasat Inc.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

## (as of June 30, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1544</td><td>42%</td><td>453</td><td>49%</td><td>29%</td><td>757</td><td>44%</td></tr><tr><td>Equal-weight/Hold</td><td>1577</td><td>43%</td><td>390</td><td>42%</td><td>25%</td><td>769</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>1</td><td>0%</td><td>33%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>544</td><td>15%</td><td>89</td><td>10%</td><td>16%</td><td>204</td><td>12%</td></tr><tr><td>Total</td><td>3,668</td><td></td><td>933</td><td></td><td></td><td>1731</td><td></td></tr></table>

Data include common stock and ADRs currently assigned ratings. Investment Banking Clients are companies from whom MS received investment banking compensation in the last 12 months. Due to rounding off of decimals, the percentages provided in the "% of total" column may not add up to exactly 100 percent.

## Analyst Stock Ratings

Overweight (O). The stock's total return is expected to exceed the average total re

[中间内容因长度限制已省略]

Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Space Technology

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/13/2026)</td></tr><tr><td>Adam Jonas, CFA</td><td></td><td></td></tr><tr><td>Space Exploration Technologies Corp. (SPCX.O)</td><td>O (07/07/2026)</td><td>$139.14</td></tr><tr><td>Justin M Lang</td><td></td><td></td></tr><tr><td>Gogo Inc (GOGO.O)</td><td>E (08/14/2025)</td><td>$3.54</td></tr><tr><td>Iridium Communications Inc (IRDM.O)</td><td>E (01/16/2026)</td><td>$48.59</td></tr><tr><td>MDA Space Ltd (MDA.TO)</td><td>O (01/16/2026)</td><td>C$44.68</td></tr><tr><td>Viasat Inc (VSAT.O)</td><td>E (12/15/2017)</td><td>$69.54</td></tr><tr><td colspan="3">Kristine T Liwag</td></tr><tr><td>Firefly Aerospace Inc (FLY.O)</td><td>E (09/02/2025)</td><td>$22.27</td></tr><tr><td>Planet Labs PBC (PL.N)</td><td>E (01/22/2023)</td><td>$25.96</td></tr><tr><td>Rocket Lab USA Inc (RKLB.O)</td><td>O (01/16/2026)</td><td>$76.73</td></tr><tr><td>Virgin Galactic Holdings Inc (SPCE.N)</td><td>U (11/22/2023)</td><td>$2.42</td></tr><tr><td>Voyager Technologies Inc (VOYG.N)</td><td>E (07/07/2025)</td><td>$29.66</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
