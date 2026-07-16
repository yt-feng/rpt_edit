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
<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td>Eva Hou</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Eva.Hou@morganstanley.com</td><td>+852 2848-6964</td></tr><tr><td>Tom Li</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Tom.Li1@morganstanley.com</td><td>+852 2239-1059</td></tr></table>

# China Yangtze Power Co. | Asia Pacific

# SG NDR Key Takeaways

CYPC remains positioned as a high-quality defensive utility with strong cash-flow generation, declining financing costs, and increasing strategic value within a more renewable-intensive electricity system.

## Key Takeaways

CYPC's high proportion of long-term contracted electricity sales limits short-term price volatility.

Hydropower's flexibility (30GW daily peak-shaving capacity) and environmental value should become increasingly important as China's power system evolves.

■ CYPC will maintain the >70% dividend payout ratio.

Capex during the 15th FYP will be concentrated on pumped-storage projects, expansion of existing hydropower assets, and selective strategic investments.

■ After funding dividends and capex, CYPC intends to use excess cash to reduce debt and optimize its liability structure.

Hydro tariff in the LT = Energy value + capacity value + green value: Market-based electricity accounted \~36% of the company's total electricity sales in 2025. Within the market-based segment, \~98% of electricity is sold through medium- and long-term contracts. As a result, only a small proportion is directly exposed to spot-market price volatility. Management emphasized that electricity market reform should not automatically be interpreted as negative for hydropower pricing: 1) Hydropower units can start and stop rapidly, typically within approximately 10 minutes; 2) Reservoir-based hydropower offers strong peak-shaving and system-balancing capabilities; 3) Hydropower has green and environmental value through green certificates, although this value is not yet fully tradable or monetized.

Dividend policy and B/S management: CYPC will maintain at least 70% dividend payout ratio. After funding dividends and capital expenditure, the company intends to use excess cash to reduce debt and optimize its liability structure. The company's average financing cost is currently below 3%, while newly issued medium- and long-term bonds carry interest rates below 2%. This creates further potential to reduce financing costs through refinancing and liability management.

El Niño: Current forecasts suggest that a strong El Niño event may emerge in the autumn. Historically, the year following a strong El Niño event has sometimes experienced higher precipitation and stronger river inflows. Management cited the 1997–1998 period as an example, when a strong El Niño event in 1997 was followed by severe flooding in the Yangtze River basin in 1998. However, management did not indicate that this relationship is certain. Actual generation and inflow conditions will continue to depend on observed rainfall, weather patterns, and reservoir conditions.

## Asia Summer School 2026

![](images/588794be80aa91f6451a1b833893754294dcf54ebe1759abf551375b79305cb5.jpg)

## China Yangtze Power Co. (600900.SS, 600900 CG)

China Utilities | China

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>Rmb34.79</td></tr><tr><td>Up/downside to price target (%)</td><td>22</td></tr><tr><td>Shr price, close (Jul 14, 2026)</td><td>Rmb28.55</td></tr><tr><td>52-Week Range</td><td>Rmb30.79-25.38</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>24,468</td></tr><tr><td>Mkt cap, curr (mn)</td><td>Rmb698,568</td></tr><tr><td>EV, curr (mn)</td><td>Rmb1,002,586</td></tr><tr><td>Avg daily trading value (mn)</td><td>Rmb2,775</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/24</td><td>12/25e</td><td>12/26e</td><td>12/27e</td></tr><tr><td>EPS (Rmb)**</td><td>1.33</td><td>1.52</td><td>1.61</td><td>1.66</td></tr><tr><td>EPS (Rmb)§</td><td>1.38</td><td>1.41</td><td>1.50</td><td>1.54</td></tr><tr><td>Revenue, net (Rmb mn)</td><td>84,492</td><td>90,458</td><td>92,841</td><td>94,402</td></tr><tr><td>EBITDA (Rmb mn)</td><td>64,175</td><td>69,499</td><td>71,351</td><td>72,563</td></tr><tr><td>ModelWare net inc (Rmb mn)</td><td>32,496</td><td>37,140</td><td>39,445</td><td>40,530</td></tr><tr><td>P/E</td><td>22.2</td><td>17.9</td><td>17.7</td><td>17.2</td></tr><tr><td>P/BV</td><td>3.4</td><td>3.0</td><td>2.9</td><td>2.8</td></tr><tr><td>RNOA (%)</td><td>6.4</td><td>7.1</td><td>7.4</td><td>7.6</td></tr><tr><td>ROE (%)</td><td>16.1</td><td>17.7</td><td>17.6</td><td>17.0</td></tr><tr><td>EV/EBITDA</td><td>16.0</td><td>13.6</td><td>13.4</td><td>12.9</td></tr><tr><td>Div yld (%)</td><td>2.8</td><td>3.9</td><td>4.0</td><td>4.1</td></tr><tr><td>FCF yld ratio (%)</td><td>6.2</td><td>8.9</td><td>8.1</td><td>8.2</td></tr><tr><td>Leverage (EOP) (%)</td><td>139.0</td><td>118.7</td><td>102.8</td><td>88.7</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
§ = Consensus data is provided by Refinitiv Estimates
e = MS estimates

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

More details

15th FYP to focus on existing hydropower expansion, pumped storage and strategic investments: 1) It plans to expand Gezhouba and Xiangjiaba by a combined 2.2GW over the next five years. The expansion is intended to address bottlenecks in the coordinated operation of the six-reservoir system, improve dispatch efficiency, and reduce water spillage. 2) Incremental investment will primarily target pumped-storage hydropower. It has approved five projects with a combined capacity of 6.8GW, which are expected to commence operations around 2030. These projects are expected to generate positive free cash flow approximately six to seven years after commissioning. 3) It will also undertake a limited number of renewable energy projects, mainly focused on integrated hydro-wind-solar development. 4) Equity investments will focus on assets in the middle and lower reaches of the Jinsha River. Such investments must offer clear strategic or operational synergies with the company's existing portfolio. The company intends to hold these investments for the long term rather than engage in secondary-market trading.

## EPS accretion and strategic importance remain the key investment criterion:

Management indicated that the company's current ROE is approximately 15%, while returns on new projects are expected to be lower than those of its existing hydropower portfolio. However, management emphasized that investment decisions are not based solely on project-level ROE. Continued investment is considered essential to maintaining the company's strategic importance within China's power system and preserving its bargaining power in future electricity pricing negotiations. Accordingly, management places greater emphasis on whether new projects are accretive to EPS over the long term, rather than simply maximizing ROE.

## Valuation Methodology and Risks

## China Yangtze Power Co. (600900.SS)

Our price target is derived from a discounted cash flow (DCF) methodology, as we believe the company can generate stable profit and cash flows from its hydropower stations. We use a WACC of 6.7% and assume no terminal growth. Our WACC reflects a corporate cost of equity of 8.8%, an after-tax cost of debt of 3% and a target debt-to-capital ratio of 36.2%.

## Risks to Upside

1) Better-than-expected hydropower resources; 2) better-than-expected dividend payout ratio; 3) better-than-expected hydropower utilization hours; 4) higher-than-expected renewable energy capacity expansion.

## Risks to Downside

1) Weaker-than-expected hydropower resources; 2) lower-than-expected dividend payout ratio; 3) lower-than-expected renewable energy capacity expansion.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Eva Hou; Tom Li.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Anhui Yingliu Electromechanical Co Ltd, China Longyuan Power Group, Dajin Heavy Industry, Goldwind, Huaming Power Equipment, JA Solar Technology Co Ltd, LONGi Green Energy Technology Co Ltd, Sieyuan Electric Co.Ltd., Sungrow Power Supply Co. Ltd.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Anhui Yingliu Electromechanical Co Ltd, China Gas Holdings, China Resources Gas, China Resources Power, Sungrow Power Supply Co. Ltd, Tongwei Co. Ltd..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from China Gas Holdings, China Longyuan Power Group, Huaneng Power International Inc..

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Anhui Yingliu Electromechanical Co Ltd, China Gas Holdings, China Resources Gas, China Resources Power, Sungrow Power Supply Co. Ltd, Tongwei Co. Ltd..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: China Gas Holdings, China Longyuan Power Group, Huaneng Power International Inc..

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Rati

[中间内容因长度限制已省略]

ective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: China Utilities

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/14/2026)</td></tr><tr><td colspan="3">Eva Hou</td></tr><tr><td>CGN Power Co., Ltd (1816.HK)</td><td>E (03/21/2026)</td><td>HK$2.72</td></tr><tr><td>CGN Power Co., Ltd (003816.SZ)</td><td>U (03/29/2021)</td><td>Rmb3.90</td></tr><tr><td>China Longyuan Power Group (0916.HK)</td><td>E (01/20/2026)</td><td>HK$5.27</td></tr><tr><td>China Longyuan Power Group (001289.SZ)</td><td>E (08/06/2024)</td><td>Rmb15.75</td></tr><tr><td>China Resources Power (0836.HK)</td><td>E (03/21/2026)</td><td>HK$17.83</td></tr><tr><td>China Yangtze Power Co. (600900.SS)</td><td>O (11/14/2023)</td><td>Rmb28.55</td></tr><tr><td>Dajin Heavy Industry (002487.SZ)</td><td>O (04/18/2026)</td><td>Rmb43.70</td></tr><tr><td>Goldwind (002202.SZ)</td><td>U (01/20/2026)</td><td>Rmb19.17</td></tr><tr><td>Goldwind (2208.HK)</td><td>E (08/17/2022)</td><td>HK$9.53</td></tr><tr><td>Hangzhou First Applied Material Co. Ltd (603806.SS)</td><td>O (01/18/2023)</td><td>Rmb14.91</td></tr><tr><td>Henan Pinggao Electric (600312.SS)</td><td>O (01/18/2024)</td><td>Rmb17.33</td></tr><tr><td>Huaneng Power International Inc. (0902.HK)</td><td>E (06/30/2022)</td><td>HK$5.66</td></tr><tr><td>Huaneng Power International Inc. (600011.SS)</td><td>U (04/07/2021)</td><td>Rmb6.91</td></tr><tr><td>JA Solar Technology Co Ltd (002459.SZ)</td><td>E (09/02/2025)</td><td>Rmb7.08</td></tr><tr><td>Jiangsu Zhongtian Technology Co. Ltd. (600522.SS)</td><td>O (10/12/2020)</td><td>Rmb42.85</td></tr><tr><td>LONGi Green Energy Technology Co Ltd (601012.SS)</td><td>U (09/02/2025)</td><td>Rmb11.73</td></tr><tr><td>NARI Technology (600406.SS)</td><td>O (11/01/2015)</td><td>Rmb21.99</td></tr><tr><td>Ningbo Orient Wires &amp; Cables Co Ltd (603606.SS)</td><td>O (08/17/2022)</td><td>Rmb40.73</td></tr><tr><td>Riyue Heavy Industry Co., Ltd. (603218.SS)</td><td>O (02/11/2025)</td><td>Rmb9.46</td></tr><tr><td>Shanghai Electric (2727.HK)</td><td>U (03/26/2021)</td><td>HK$3.21</td></tr><tr><td>Shanghai Electric (601727.SS)</td><td>U (03/26/2021)</td><td>Rmb6.59</td></tr><tr><td>Sieyuan Electric Co.Ltd. (002028.SZ)</td><td>O (07/01/2025)</td><td>Rmb162.00</td></tr><tr><td>Sinoma Science &amp; Technology Co. Ltd. (002080.SZ)</td><td>O (09/23/2025)</td><td>Rmb72.35</td></tr><tr><td>Sungrow Power Supply Co. Ltd (300274.SZ)</td><td>O (06/09/2026)</td><td>Rmb108.29</td></tr><tr><td>Tongwei Co. Ltd. (600438.SS)</td><td>E (09/02/2025)</td><td>Rmb10.68</td></tr><tr><td>XJ Electric (000400.SZ)</td><td>E (03/21/2026)</td><td>Rmb19.85</td></tr><tr><td colspan="3">Hannah Yang, CFA</td></tr><tr><td>Xinyi Solar Holdings Ltd (0968.HK)</td><td>O (07/30/2020)</td><td>HK$1.97</td></tr><tr><td colspan="3">Tom Li</td></tr><tr><td>Anhui Yingliu Electromechanical Co Ltd (603308.SS)</td><td>O (04/08/2026)</td><td>Rmb53.56</td></tr><tr><td>China Gas Holdings (0384.HK)</td><td>E (07/10/2026)</td><td>HK$5.51</td></tr><tr><td>China Resources Gas (1193.HK)</td><td>E (07/10/2026)</td><td>HK$15.20</td></tr><tr><td>Huaming Power Equipment (002270.SZ)</td><td>O (04/08/2026)</td><td>Rmb17.90</td></tr><tr><td>Ningbo Sanxing Medical Electric Co. Ltd. (601567.SS)</td><td>O (04/08/2026)</td><td>Rmb13.49</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
