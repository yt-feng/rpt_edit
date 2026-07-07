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
Unless otherwise noted, all metrics are based on MS ModelWare framework
§ = Consensus data is provided by Refinitiv Estimates
\*\* = Based on consensus methodology
e = MS estimates

July 5, 2026 02:23 PM GMT

Tianshan Aluminum | Asia Pacific

# Preliminary 1H26 earnings better than expected excluding tax impact

Tianshan expects its 1H26 net profit to double to Rmb4.2bn: Excluding one-offs, recurring earnings grew 109% YoY to Rmb 4.1bn, helped by 1) higher aluminum prices, supported by tight supply overseas amid the conflict in the Middle East, and 2) better cost control. 1H26 earnings will reflect increases in the tax rate in Xinjiang, up to 15% to 25%, affecting \~Rmb700mn profit in 2Q26; excluding this, net profit in 2Q26 could reach Rmb2.6bn, better than our expectation.

Earnings should remain solid in 2H26: Aluminum prices corrected recently amid talk of potential rate hikes from the US and easing supply overseas. Increasing supply from capacity restarts in Middle East and gradual volume release from new capacities in Indonesia could continue to pressure aluminum prices. However, the aluminum industry remains in deficit this year, which we think should limit price downside in 2026. This, together with higher volume in the Xinjiang production base, implies solid earnings for Tianshan in 2H26.

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Hannah Yang, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Hannah.Yang1@morganstanley.com</td><td>+852 2239-7079</td></tr><tr><td colspan="2">Rachel L Zhang</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Rachel.Zhang@morganstanley.com</td><td>+852 2239-1520</td></tr><tr><td colspan="2">Chris Jiang</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Chris.Jiang@morganstanley.com</td><td>+852 3963-1593</td></tr><tr><td colspan="2">Cynthia Tang</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Cynthia.Tang@morganstanley.com</td><td>+852 3963-4360</td></tr></table>

![](images/7c570fc066d99a232151ef391710898a9eddabeb4d0b7776ad5a6a4cc2762417.jpg)

## Tianshan Aluminum (002532.SZ, 002532 CS)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>Rmb23.00</td></tr><tr><td>Up/downside to price target (%)</td><td>102</td></tr><tr><td>Shr price, close (Jul 3, 2026)</td><td>Rmb11.37</td></tr><tr><td>52-Week Range</td><td>Rmb21.88-8.32</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>4,629</td></tr><tr><td>Mkt cap, curr (mn)</td><td>Rmb52,628.7</td></tr><tr><td>EV, curr (mn)</td><td>Rmb54,930.1</td></tr><tr><td>Avg daily trading value (mn)</td><td>Rmb926</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (Rmb)**</td><td>1.0</td><td>2.1</td><td>2.3</td><td>2.3</td></tr><tr><td>EPS (Rmb)§</td><td>1.1</td><td>2.0</td><td>2.3</td><td>2.3</td></tr><tr><td>Revenue, net (Rmb mn)</td><td>29,502.2</td><td>38,312.8</td><td>39,958.4</td><td>40,324.5</td></tr><tr><td>EBITDA (Rmb mn)</td><td>7,736.9</td><td>13,638.0</td><td>14,310.7</td><td>14,609.6</td></tr><tr><td>ModelWare net inc (Rmb mn)</td><td>4,817.8</td><td>9,829.6</td><td>10,427.0</td><td>10,693.6</td></tr><tr><td>P/E</td><td>15.4</td><td>5.3</td><td>5.0</td><td>4.9</td></tr><tr><td>P/BV</td><td>2.5</td><td>1.5</td><td>1.3</td><td>1.2</td></tr><tr><td>RNOA (%)</td><td>15.4</td><td>27.5</td><td>28.9</td><td>30.5</td></tr><tr><td>ROE (%)</td><td>18.0</td><td>33.2</td><td>30.4</td><td>27.3</td></tr><tr><td>EV/EBITDA</td><td>10.0</td><td>3.7</td><td>3.1</td><td>2.6</td></tr><tr><td>Div yld (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>FCF yld ratio (%)*</td><td>8.8</td><td>19.7</td><td>22.8</td><td>23.7</td></tr><tr><td>Leverage (EOP) (%)</td><td>7.8</td><td>(6.7)</td><td>(21.0)</td><td>(32.7)</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Valuation Methodology and Risks

## Tianshan Aluminum (002532.SZ)

Base case, derived from residual income valuation model. We discount our earnings forecasts through 2037 and then normalize earnings. Key assumptions include a cost of equity of 8.6% (risk-free rate of 1.8%, risk premium of 7%, beta of 0.97), a long-term ROE of 15% and a steady-state growth rate of 4%.

## Risks to Upside

■ Better-than-expected demand

■ Decreasing raw material and energy prices

■ More plants in maintenance than expected

## Risks to Downside

■ Slowdown in global aluminum demand

■ Rising raw material and energy prices

■ Industry overcapacity

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Chris Jiang; Hannah Yang, CFA; Rachel L Zhang.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Aluminum Corp. of China Ltd., Anhui Honglu Steel Construction, Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Flat Glass Group Co Ltd, Ganfeng Lithium Co. Ltd., GEM Co Ltd, Jiangxi Copper, JL Mag Rare-Earth Co. Ltd, Shandong Gold Mining Co. Ltd, Shenzhen Kedali Industry Co Ltd, Sinomine Resource Group Co Ltd, Tianqi Lithium Industries Inc., Zijin Mining Group.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of CNGR Advanced Material Co., Ltd., MMG Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for investment banking services from Ganfeng Lithium Co. Ltd., MMG Ltd, Zijin Mining Group.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Baoshan Iron & Steel, China Jushi, China Steel Corp., CMOC Group Ltd, Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Mining Group.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Baoshan Iron & Steel, China Jushi, China Steel Corp., CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Gold International, Zijin Mining Group.

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

CGN Mining Co Ltd (1164.HK)</td><td>O (01/18/2023)</td><td>HK$2.59</td></tr><tr><td>Chengxin Lithium Group Co. Ltd. (002240.SZ)</td><td>E (12/16/2025)</td><td>Rmb42.10</td></tr><tr><td>GEM Co Ltd (002340.SZ)</td><td>U (04/20/2026)</td><td>Rmb6.69</td></tr><tr><td>Shenzhen Kedali Industry Co Ltd (002850.SZ)</td><td>O (08/21/2023)</td><td>Rmb226.16</td></tr><tr><td>Sinomine Resource Group Co Ltd (002738.SZ)</td><td>O (12/16/2025)</td><td>Rmb64.26</td></tr><tr><td>Yongxing Special Materials Technology (002756.SZ)</td><td>E (11/25/2022)</td><td>Rmb60.27</td></tr><tr><td>Zhejiang Huayou Cobalt Co Ltd (603799.SS)</td><td>O (10/08/2025)</td><td>Rmb46.76</td></tr><tr><td colspan="3">Hannah Yang, CFA</td></tr><tr><td>China Hongqiao Group (1378.HK)</td><td>O (09/15/2023)</td><td>HK$20.88</td></tr><tr><td>Chuangxin Industries Holdings Ltd. (2788.HK)</td><td>O (03/19/2026)</td><td>HK$15.48</td></tr><tr><td>Flat Glass Group Co Ltd (6865.HK)</td><td>O (07/30/2020)</td><td>HK$6.51</td></tr><tr><td>Flat Glass Group Co Ltd (601865.SS)</td><td>O (07/30/2020)</td><td>Rmb10.19</td></tr><tr><td>MMG Ltd (1208.HK)</td><td>O (12/16/2024)</td><td>HK$7.29</td></tr><tr><td>Shandong Pharmaceutical Glass Co. Ltd. (600529.SS)</td><td>U (04/20/2026)</td><td>Rmb18.66</td></tr><tr><td>Shenhuo Coal and Power (000933.SZ)</td><td>O (09/02/2025)</td><td>Rmb22.06</td></tr><tr><td>Tianshan Aluminum (002532.SZ)</td><td>O (03/19/2026)</td><td>Rmb11.37</td></tr><tr><td>Xinyi Glass Holding Limited (0868.HK)</td><td>U (05/14/2024)</td><td>HK$8.66</td></tr><tr><td>Zhongfu Shenying Carbon Fiber Co Ltd (688295.SS)</td><td>O (08/25/2023)</td><td>Rmb54.45</td></tr><tr><td colspan="3">Rachel L Zhang</td></tr><tr><td>Aluminum Corp. of China Ltd. (601600.SS)</td><td>O (11/30/2020)</td><td>Rmb8.33</td></tr><tr><td>Aluminum Corp. of China Ltd. (2600.HK)</td><td>O (11/30/2020)</td><td>HK$7.70</td></tr><tr><td>Baoshan Iron &amp; Steel (600019.SS)</td><td>O (01/16/2016)</td><td>Rmb5.59</td></tr><tr><td>Beijing New Building Materials (000786.SZ)</td><td>O (04/09/2024)</td><td>Rmb18.10</td></tr><tr><td>Beijing Oriental Yuhong Waterproof Techn (002271.SZ)</td><td>E (09/25/2024)</td><td>Rmb12.30</td></tr><tr><td>China Jushi (600176.SS)</td><td>O (12/22/2020)</td><td>Rmb70.90</td></tr><tr><td>China Lesso Group Holdings Ltd (2128.HK)</td><td>U (10/08/2025)</td><td>HK$3.76</td></tr><tr><td>China Steel Corp. (2002.TW)</td><td>U (12/16/2025)</td><td>NT$18.95</td></tr><tr><td>CMOC Group Ltd (3993.HK)</td><td>O (09/24/2019)</td><td>HK$16.20</td></tr><tr><td>CMOC Group Ltd (603993.SS)</td><td>O (06/21/2024)</td><td>Rmb18.52</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (300919.SZ)</td><td>E (01/12/2026)</td><td>Rmb41.95</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (2579.HK)</td><td>O (01/12/2026)</td><td>HK$25.48</td></tr><tr><td>FangDa Carbon New Material Co. Ltd. (600516.SS)</td><td>U (12/16/2024)</td><td>Rmb5.79</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (002460.SZ)</td><td>O (04/20/2026)</td><td>Rmb62.97</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (1772.HK)</td><td>O (12/16/2025)</td><td>HK$49.70</td></tr><tr><td>Henan Liliang Diamond Co. Ltd (301071.SZ)</td><td>U (04/20/2026)</td><td>Rmb84.11</td></tr><tr><td>Jiangsu Dingsheng New Materials (603876.SS)</td><td>U (04/20/2026)</td><td>Rmb24.06</td></tr><tr><td>Jiangxi Copper (0358.HK)</td><td>O (10/08/2025)</td><td>HK$31.72</td></tr><tr><td>Jiangxi Copper (600362.SS)</td><td>O (10/08/2025)</td><td>Rmb43.28</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (6680.HK)</td><td>O (04/23/2025)</td><td>HK$19.30</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (300748.SZ)</td><td>O (04/23/2025)</td><td>Rmb34.25</td></tr><tr><td>Nine Dragons Paper (2689.HK)</td><td>E (01/04/2023)</td><td>HK$7.25</td></tr><tr><td>Shandong Gold Mining Co. Ltd (600547.SS)</td><td>O (04/23/2025)</td><td>Rmb26.08</td></tr><tr><td>Shandong Gold Mining Co. Ltd (1787.HK)</td><td>O (12/12/2024)</td><td>HK$19.68</td></tr><tr><td>Shandong Nanshan Aluminium Co. (600219.SS)</td><td>O (11/30/2020)</td><td>Rmb4.17</td></tr><tr><td>Tianqi Lithium Industries Inc. (9696.HK)</td><td>O (12/16/2025)</td><td>HK$40.30</td></tr><tr><td>Tianqi Lithium Industries Inc. (002466.SZ)</td><td>O (04/20/2026)</td><td>Rmb58.66</td></tr><tr><td>Weixing New Building Materials (002372.SZ)</td><td>U (10/08/2025)</td><td>Rmb8.55</td></tr><tr><td>Zhaojin Mining Industry (1818.HK)</td><td>O (06/21/2024)</td><td>HK$19.17</td></tr><tr><td>Zijin Gold International (2259.HK)</td><td>O (11/06/2025)</td><td>HK$107.50</td></tr><tr><td>Zijin Mining Group (2899.HK)</td><td>O (11/06/2025)</td><td>HK$30.72</td></tr><tr><td>Zijin Mining Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb27.82</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
