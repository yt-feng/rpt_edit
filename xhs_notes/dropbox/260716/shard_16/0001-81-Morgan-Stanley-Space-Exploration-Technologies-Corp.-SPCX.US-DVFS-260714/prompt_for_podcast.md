你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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

Overweight (O). The stock's total return is expected to exceed the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Equal-weight (E). The stock's total return is expected to be in line with the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Not-Rated (NR). Currently the analyst does not have adequate conviction about the stock's total return relative to the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Underweight (U). The stock's total return is expected to be below the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Unless otherwise specified, the time frame for price targets included in MS is 12 to 18 months.

## Analyst Industry Views

Attractive (A): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be attractive vs. the relevant broad market benchmark, as indicated below.

In-Line (I): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be in line with the relevant broad market benchmark, as indicated below. Cautious (C): The analyst views the performance of his or her industry coverage universe over the next 12-18 months with caution vs. the relevant broad market benchmark, as indicated below. Benchmarks for each region are as follows: North America - S&P 500; Latin America - relevant MSCI country index or MSCI Latin America Index; Europe - MSCI Europe; Japan - TOPIX; Asia - relevant MSCI country index or MSCI sub-regional index or MSCI AC Asia Pacific ex Japan Index.

Stock Price, Price Target and Rating History (See Rating Definitions)  
Space Exploration Technologies Corp. (SPCX.O) - As of 07/13/26 GMT in USD  
![](images/fa41658d8b06f6536ce2642ca2d28a0dbbc234ee7603d23365c01c97e4f023cd.jpg)  
Stock Rating History: 7/7/26 : 0/A  
Price

[中间内容因长度限制已省略]

f its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

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
