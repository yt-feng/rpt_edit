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
# Autos & Shared Mobility | Japan

# Feedback from US Investor

# Visits

While most have a guarded view on the autos industry given the situation in the Middle East and concerns about the rise of Chinese OEMs, some have switched to a more bullish stance amid hopes for a resolution of issues relating to the Middle East.

Our visits to investors in the US: We had the opportunity to hold meetings with institutional investors in the US over Jun 8-11 (in New York and San Francisco), and report back on the main topics that came up and views we heard from investors, and the impressions we took away.

Autos industry as a whole: Our impression was that most investors have taken a cautious stance on the industry with the Middle East situation ongoing. Some – albeit not many – have already adopted a more bullish stance, with a view to the situation resolving (particularly on stocks where share prices have fallen as the situation has deteriorated).

The main topics of interest among investors centered on 1) effects of supply chain constraints and rising raw materials prices resulting from the Middle East situation and 2) concerns about falling market shares among Japan OEMs due to the rise of Chinese OEMs. In addition, we also fielded many questions about our interpretation as the US-Mexico-Canada Agreement comes up for review in Jul 2026.

Individual stocks: Toyota: We found interest in topics including scope for upside vs. F3/27 OP guidance, earnings contributions from HEV models, and changes under the new president from Apr 2026. We had the impression that the conservative nature of F3/27 OP guidance is not well understood. Honda: Many questions concerned seeking business opportunities relating to energy storage systems (ESSs). With 4-wheeler business subdued, we also noted considerable interest in growth potential for 2-wheelers, and risk of profit margins worsening with rising exposure to EVs. Nissan: While many investors spoke positively about progress in cutting fixed costs, we had the impression that many remain concerned about prospects of ending losses in autos and securing positive free cash flow. SUBARU: Besides the revised approach to shareholder return announced with the most recent earnings release, another topic of high interest was the longer-term earnings outlook, including measures to reduce prime costs and fill out the product lineup indicated in the Management Policy 2025. Mazda: Expectations of growth in sales via the full model change in the new CX-5 SUV appear to have subsided since the situation in the Middle East worsened. (continued on second page)

MS MUFG SECURITIES CO., LTD.+

## Hiroto Segawa

Equity Analyst

Hiroto.Segawa@morganstanleymufg.com

+81 3 6836-8403

## Shinji Kakiuchi

Equity Analyst

Shinji.Kakiuchi@morganstanleymufg.com

+81 3 6836-5416

## Hayato Takashima

Research Associate

Hayato.Takashima@morganstanleymufg.com

+81 3 6836-5414

## Japan Summer School 2026

![](images/d2c0374bee5044f74bb04f0b480d1eb14506f0800b5293c884db3fc220f594df.jpg)

## AUTOS & SHARED MOBILITY

Japan

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Suzuki: We were asked a lot of questions about recent trends in auto sales in India, price hikes announced in May, and the outlook for gasoline prices. Many investors also expressed concerns about effects of the Middle East situation on the Indian economy as a whole, and we found no noticeable increase in interest in Suzuki while the situation remains unresolved. Mitsubishi Motors: Here, many investors voiced concerns about a stiffer competitive climate in ASEAN markets due to events in the Middle East. We were also asked about further development of collaboration with others such as Honda and Nissan beyond the content of the longer-term vision unveiled in May 2026. Isuzu: Pushback on our UW rating was limited, and many commented on slow recovery in N. America and Thailand. Yamaha Motor: Our impression was that interest has increased among long-term investors. Besides a considerable focus on outdoor land vehicle (OLV) business restructuring expected to be unveiled with results for Apr-Jun, some investors spoke positively about longer-term growth potential in outboard motors and stability of 2-wheeler earnings.

## Valuation Methodology and Risks

## Isuzu Motors (7202.T)

F3/27e BPS x 0.85. We apply a P/B multiple based on the correlation with ROE. Deriving the applied multiple at an approximately 10% discount to the three-year average trading range, taking into account the high sales exposure to the Middle East.

## Risks to Upside

■ Market share increase in overseas LCV market  
■ Growth potential mainly in overseas CV market  
■ Further improvement of shareholder returns

## Risks to Downside

■ Slowing overseas CV sales volumes  
■ In the US, the impact of tariffs is a concern.  
■ FX impact

## Disclosure Section

The information and opinions in MS were prepared by MS MUFG Securities Co., Ltd. and its affiliates (collectively, "MS").

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Hiroto Segawa.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Isuzu Motors, Mazda Motor, Mitsubishi Motors, Nissan Motor, SUBARU, Suzuki Motor.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Honda Motor, Isuzu Motors, Nissan Motor, Toyota Motor.

Within the last 12 months, MS has received compensation for investment banking services from Honda Motor, Isuzu Motors, Nissan Motor, SUBARU, Toyota Motor.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Honda Motor, Isuzu Motors, Mazda Motor, Mitsubishi Motors, Nissan Motor, SUBARU, Suzuki Motor, Toyota Motor, Yamaha Motor.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Nissan Motor, Toyota Motor.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Honda Motor, Isuzu Motors, Mitsubishi Motors, Nissan Motor, SUBARU, Suzuki Motor, Toyota Motor, Yamaha Motor.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Nissan Motor, SUBARU, Toyota Motor.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td><td>16%</td><td>201</td><td>12%</td></tr><tr><td>Total</td><td>3,667</td><td></td><td>920</td><td></td><td></td><td>1632</td><td></td></tr></table>

Data include common stock and ADRs currently assigned ratings. Investment Banking Clients are companies from whom MS received investment banking compensation in the last 12 months. Due to rounding off of decimals, the percentages provided in the "% of total" column may not add up to exactly 100 percent.

## Analyst Stock Ratings

Overweight (O). The stock's total return is expected to exceed the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Equal-weight (E). The stock's total return is expected to be in line with the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Not-Rated (NR). Currently the analyst does not have adequate conviction about the stock's total return relative to the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Underweight (U). The stock's total return is expected to be below the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Unless otherwise specified, the time frame for price targets included in MS is 12 to 18 months.

## Analyst Industry Views

Attractive (A): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be attractive vs. the relevant broad market benchmark, as indicated below.

In-Line (I): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be in line with the relevant broad market benchmark, as indicated below. Cautious (C): The analyst views the performance of his or her industry coverage universe over the next 12-18 months with caution vs. the relevant broad market benchmark, as indicated below. Benchmarks for each region are as follows: North America - S&P 500; Latin America - relevant MSCI country index or MSCI Latin America Index; Europe - MSCI Europe; Japan - TOPIX; Asia - relevant MSCI country index or MSCI sub-regional index or MSCI AC Asia Pacific ex Japan Index.

## Stock Price, Price Target and Rating History (See Rating Definitions)

Isuzu Motors (7202.T) - As of 06/15/26 GMT in JPY Industry : Autos & Shared Mobility  
![](images/fbd8dbfa675f65c95150996f96a28a7659b5108132197940c5adff0de9ac796d.jpg)

<details>
<summary>line chart</summary>

| Date       | Value |
| ---------- | ----- |
| 06/01 2023 | 1800  |
| 06/01 2024 | 2000  |
| 06/01 2024 | 2200  |
| 06/01 2024 | 2000  |
| 06/01 2025 | 2250  |
| 06/01 2025 | 2300  |
| 06/01 2026 | 1300  |
</details>

Stock Rating History: 6/1/21 : NA/C; 9/26/21 : NA/NR; 10/12/21 : NA/I; 11/30/23 : E/I; 6/2/26 : U/I  
Price Target History: 11/30/23 : 2000; 5/10/24 : 2200; 11/6/24 : 2000; 12/17/25 : 2250; 3/13/26 : 2300; 6/2/26 : 1900  
Source: MS Date Format : MM/DD/YY Price Target No Price Target Assigned (NA)  
Stock Price (Not Covered by Current Analyst) — Stock Price (Covered by Current Analyst)  
Stock and Industry Ratings (abbreviations below) appear as ♦ Stock Rating/Industry View  
Stock Ratings: Overweight (O) Equal-weight (E) Underweight (U) Not-Rated (NR) No Rating Available

[中间内容因长度限制已省略]

vestment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Autos & Shared Mobility

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/15/2026)</td></tr><tr><td colspan="3">Hiroto Segawa</td></tr><tr><td>Honda Motor (7267.T)</td><td>E (03/12/2026)</td><td>¥1,458</td></tr><tr><td>Isuzu Motors (7202.T)</td><td>U (06/02/2026)</td><td>¥2,294</td></tr><tr><td>Mazda Motor (7261.T)</td><td>E (04/25/2023)</td><td>¥1,183</td></tr><tr><td>Mitsubishi Motors (7211.T)</td><td>E (09/26/2024)</td><td>¥337</td></tr><tr><td>Nissan Motor (7201.T)</td><td>E (01/23/2023)</td><td>¥357</td></tr><tr><td>SUBARU (7270.T)</td><td>E (06/02/2026)</td><td>¥2,568</td></tr><tr><td>Suzuki Motor (7269.T)</td><td>O (12/09/2024)</td><td>¥1,933</td></tr><tr><td>Toyota Motor (7203.T)</td><td>E (05/01/2026)</td><td>¥2,903</td></tr><tr><td>Yamaha Motor (7272.T)</td><td>E (04/17/2025)</td><td>¥1,232</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS MUFG
"""
