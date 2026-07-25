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
# Semiconductor Capital Equipment | North America Thoughts on Intel Capex

There's upside to our \$25bn assumption for 2027 WFE. We see TEL, Lasertec and KLA as core beneficiaries.

## Key Takeaways

\- Our \$202bn (+31% y/y) 2027 WFE forecast reflects \$25bn of Intel capex.

22.4mn units of Xeon6/7 would require \$24-28bn of WFE.

Inevitability to Intel Capex revisions. Intel revised up their 2026 capex outlook to \$20bn+ and spoke of 2027 capex to be “significantly above 2026 levels”. As highlighted in Semiconductor Capital Equipment: 2Q'26 WFE update, memory mismatch unresolved (18 May 2026), our view was that were Intel to take part in this CPU upcycle, we think there is an inevitability to capex hikes. We estimated that if the company wants to produce 5mn incremental Xeon 6s, the company will have to spend \$5.3bn in WFE. Assuming Intel wants to take two-thirds of the incremental CPU units, we think the company will have to expand logic wafer capacity by a minimum of \$23.8bn. Assuming 2 compute tiles for Xeon 7, we estimate Intel will have to spend \$27.9bn in WFE. We saw capex tracking possibly even higher as our capex argument is purely based on Intel looking to increase capex to meet rising CPU demand, i.e. Intel IDM. Foundry customers acquisition will necessitate spending beyond the \$23.8-27.9bn of WFE to meet rising CPU demand. Our latest WFE forecast reflects \$25bn of Intel capex in 2027, but there's upside.

Biggest beneficiaries outside of the US. We see the biggest beneficiaries to an Intel capex hike outside of the US, as Tokyo Electron has seen Intel as a 10%+ customer from F3/14-24, reaching as high as 20.4% in F3/20. Similarly, Lasertec has seen Intel as a 10% customer from F6/20-25, reaching as high as 31.6% in F6/22. Within the US we see KLA as an outsized beneficiary. Intel has not been a 10% customer for KLA since F6/15, but we think Intel is leaning on KLA as a key partner to improve yield in order to improve margin and become a viable foundry. We see possibility of KLA 6.4x their Intel revenue from 2025 to 2027 on the back of PC intensity and share gain. In our view, this update from Intel validates our positive view on KLA's long-term story, but as we highlighted in our preview, we would be slightly more cautious than positive into the print. Tokyo Electron and Lasertec are covered by Suzune Tamura.

MS & CO. LLC

Shane Brett
Equity Analyst
Shane.Brett@morganstanley.com +1 212 761-1022

Suzune Tamura, CFA
Equity Analyst
Suzune.Tamura@morganstanleymufg.com +81 3 6836-8891

Joseph Moore
Equity Analyst
Joseph.Moore@morganstanley.com +1 212 761-7516

Research Associate
Ella.Tulchinsky@morganstanley.com +1 212 761-2222

## SEMICONDUCTOR CAPITAL EQUIPMENT

North America
Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Wafers per CPU

Exhibit 1: We estimate 5mn incremental server CPUs would require \$5.3bn+ of WFE

<table><tr><td>WFE per CPU Needs ($mn)</td><td>Intel Xeon 6</td><td>Intel Xeon 7</td></tr><tr><td>Total</td><td>5,326</td><td>6,233</td></tr><tr><td>Logic</td><td>5,251</td><td>6,158</td></tr><tr><td>2nm</td><td>0</td><td>4,535</td></tr><tr><td>3nm</td><td>4,502</td><td>0</td></tr><tr><td>7nm</td><td>749</td><td>1,623</td></tr><tr><td>EMIB</td><td>75</td><td>75</td></tr></table>

Exhibit 2: Two-thirds of the incremental units through 2030 (22.4mn units) would require \$23.8bn+ of WFE

<table><tr><td>WFE per CPU Needs ($mn)</td><td>Intel Xeon 6</td><td>Intel Xeon 7</td></tr><tr><td>Total</td><td>23,854</td><td>27,913</td></tr><tr><td>Logic</td><td>23,517</td><td>27,577</td></tr><tr><td>2nm</td><td>0</td><td>20,311</td></tr><tr><td>3nm</td><td>20,164</td><td>0</td></tr><tr><td>7nm</td><td>3,354</td><td>7,266</td></tr><tr><td>EMIB</td><td>336</td><td>336</td></tr></table>

<table><tr><td colspan="3">Wafers per CPU Needs</td></tr><tr><td>Total</td><td>23,487</td><td>24,214</td></tr><tr><td>Logic</td><td>22,485</td><td>23,213</td></tr><tr><td>2nm</td><td>0</td><td>14,199</td></tr><tr><td>3nm</td><td>18,325</td><td>0</td></tr><tr><td>7nm</td><td>4,160</td><td>9,014</td></tr><tr><td>EMIB</td><td>1,001</td><td>1,001</td></tr></table>

Source: MS estimates. 2nm = Intel 18A, 3nm = Intel 3.

<table><tr><td colspan="3">Wafers per CPU Needs</td></tr><tr><td>Total</td><td>105,182</td><td>108,441</td></tr><tr><td>Logic</td><td>100,698</td><td>103,957</td></tr><tr><td>2nm</td><td>0</td><td>63,588</td></tr><tr><td>3nm</td><td>82,066</td><td>0</td></tr><tr><td>7nm</td><td>18,632</td><td>40,368</td></tr><tr><td>EMIB</td><td>4,484</td><td>4,484</td></tr></table>

Source: MS estimates. 2nm = Intel 18A, 3nm = Intel 3.

## Valuation Methodology and Risks

## Lasertec (6920.T)

P/E is set in line with front-end equipment peers under our coverage.

## Risks to Upside

■ Strong uptake of the new product

■ Rising demand for EUV mask inspection systems driven by robust investment in leading-edge semiconductors.

■ Higher ASPs and replacement demand driven by the transition to HNA systems.

## Risks to Downside

■ Suspension of advanced semiconductor development by major semiconductor manufacturers and increased competition from new market entrants

■ Weak performance of the new product launch

## Tokyo Electron (8035.T)

Our target P/E uses the average one-year forward weekly multiple (just under 30x) since October 2025, when the current SPE upcycle began, through to the present.

## Risks to Upside

Intel & TeraFab capex materializes sooner than expected

■ Expansion in applications of NAND for AI inference, and resulting acceleration in green-field investments.

\- Earlier-than-expected ramp in mass production adoption of cryo etchers.

## Risks to Downside

■ Export controls to China tighten

■ Coater/developer market shrinks due to adoption of dry resist technology

■ Tech innovation greatly reduces memory usage in AI inference

## Intel Corporation (INTC.O)

\~42x EPS CY2027 EPS of \$1.77, 42x is above the high end of the large cap logic semi peer group, reflecting high leverage potential on numbers that are still depressed, and foundry optionality, despite our longer term skepticism

## Risks to Upside

■ Foundry partnerships de-risk the story and further improve the multiple

■ The company regains lost share in desktop and server following CPU shortages

## Risks to Downside

■ AMD competition increasingly becomes more significant, which could lead to further share losses in processors and pressure on ASPs

■ Minimal success in foundry leads to an inflated cost structure

## KLA Corp (KLAC.O)

38x CY28e EPS of \$7.22, a 15% premium to US SPE peers LAM & AMAT to reflect growth prospects in foundry logic and DRAM.

## Risks to Upside

■ Foundries (TSMC, Intel, Samsung) pull forward their logic roadmaps

■ Design starts in leading edge nodes increase

■ Process control intensity increases in DRAM due to HBM

## Risks to Downside

■ Certain foundries (Intel, Samsung) scale back their aspirations

■ China restrictions

■ Market share loss in mask inspection to Lasertec or in e-beam to AMAT or ASML

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Shane Brett; Nicole Kozhukhov; Joseph Moore; Suzune Tamura, CFA; Ella Tulchinsky; Mason Wayne.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Advanced Energy Industries Inc., Applied Materials Inc., Intel Corporation, KLA Corp, Lam Research Corp, Lasertec, MKS Inc., ONTO Innovation Inc, Teradyne Inc, Tokyo Electron.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Advanced Energy Industries Inc., Camtek, Intel Corporation, MKS Inc., Nova Ltd, ONTO Innovation Inc.

Within the last 12 months, MS has received compensation for investment banking services from Advanced Energy Industries Inc., Applied Materials Inc., Camtek, Intel Corporation, MKS Inc., Nova Ltd, Tokyo Electron.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Advanced Energy Industries Inc., Applied Materials Inc., Camtek, Intel Corporation, KLA Corp, Lam Research Corp, Lasertec, MKS Inc., Nova Ltd, Teradyne Inc, Tokyo Electron.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Applied Materials Inc., Intel Corporation, MKS Inc., Tokyo Electron.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Advanced Energy Industries Inc., Applied Materials Inc., Camtek, Intel Corporation, KLA Corp, Lam Research Corp, Lasertec, MKS Inc., Nova Ltd, ONTO Innovation Inc, Teradyne Inc, Tokyo Electron.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Advanced Energy Industries Inc., Applied Materials Inc., Intel Corporation, MKS Inc., Tokyo Electron.

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

Overweight (O). The stock's total

[中间内容因长度限制已省略]

 section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Semiconductor Capital Equipment

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/23/2026)</td></tr><tr><td colspan="3">Shane Brett</td></tr><tr><td>Advanced Energy Industries Inc. (AEIS.O)</td><td>O (07/22/2026)</td><td>$315.14</td></tr><tr><td>Applied Materials Inc. (AMAT.O)</td><td>E (05/18/2026)</td><td>$562.80</td></tr><tr><td>Camtek (CAMT.O)</td><td>E (12/01/2025)</td><td>$155.19</td></tr><tr><td>KLA Corp (KLAC.O)</td><td>O (01/15/2026)</td><td>$218.73</td></tr><tr><td>Lam Research Corp (LRCX.O)</td><td>O (05/18/2026)</td><td>$319.78</td></tr><tr><td>MKS Inc. (MKSI.O)</td><td>O (08/04/2024)</td><td>$345.30</td></tr><tr><td>Nova Ltd (NVMI.O)</td><td>E (12/01/2025)</td><td>$455.37</td></tr><tr><td>ONTO Innovation Inc (ONTO.N)</td><td>O (06/14/2026)</td><td>$291.27</td></tr><tr><td>Teradyne Inc (TER.O)</td><td>E (07/30/2025)</td><td>$373.75</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
