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
Unless otherwise noted, all metrics are based on MS ModelWare framework  
\*\* = Based on consensus methodology  
e = MS estimates

VNET Group Inc | Asia Pacific

# 2Q26 preview and our thoughts on recent performance

## Key Takeaways

We forecast revenue growth of 10.6% YoY and adjusted EBITDA growth of 23% YoY/1.1% QoQ.

The slower QoQ pace largely reflects more back-end-loaded chip supply.

We also expect some new orders into the results after some hyperscaler tenders during the quarter.

We're also watching for more details on the synergy with CATL after the transaction's approval. We hope to get more visibility into future development.

Our thoughts on recent performance: The share price has remained weak even though fundamentals remain solid, in our view, and Shandong Hi Speed has recently approved the transaction with CATL in a special resolution.

We think macro factors such as the US yield environment have been dominant, capping valuation. As shown in Exhibit 2 below, VNET's EV/EBITDA has a high correlation with the inverse 10-year TIPS yield, given its high leverage.

We see this more as a sentiment drag. VNET's debt is mostly financed onshore and should not be affected by the offshore rate environment.

Exhibit 1: VNET - 2Q26 preview

<table><tr><td>Years Ending December 31Rmb mn</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>% YoY</td><td>% QoQ</td></tr><tr><td>Net revenues</td><td>2,246</td><td>2,434</td><td>2,582</td><td>2,687</td><td>2,691</td><td>2,691</td><td>10.6%</td><td>0.0%</td></tr><tr><td>Cost of revenues</td><td>1,681</td><td>1,886</td><td>2,043</td><td>2,147</td><td>2,075</td><td>2,015</td><td>6.8%</td><td>-2.9%</td></tr><tr><td>Sales and marketing expenses</td><td>64</td><td>70</td><td>71</td><td>74</td><td>54</td><td>-</td><td></td><td></td></tr><tr><td>G&amp;A (including bad debt provision)</td><td>210</td><td>236</td><td>203</td><td>250</td><td>241</td><td>-</td><td></td><td></td></tr><tr><td>R&amp;D costs</td><td>44</td><td>68</td><td>71</td><td>79</td><td>74</td><td>-</td><td></td><td></td></tr><tr><td>Total operating expenses</td><td>318</td><td>374</td><td>346</td><td>402</td><td>369</td><td>374</td><td>0.0%</td><td>1.2%</td></tr><tr><td>Other operating income</td><td>1</td><td>(1)</td><td>13</td><td>15</td><td>0</td><td>(0)</td><td></td><td></td></tr><tr><td>Adjusted EBITDA</td><td>682</td><td>732</td><td>758</td><td>805</td><td>892</td><td>902</td><td>23.1%</td><td>1.1%</td></tr><tr><td>% margin</td><td>30.4%</td><td>30.1%</td><td>29.4%</td><td>30.0%</td><td>33.1%</td><td>33.5%</td><td></td><td></td></tr><tr><td>Profit before tax</td><td>(168)</td><td>112</td><td>(254)</td><td>734</td><td>41</td><td>160</td><td></td><td></td></tr><tr><td>Net profit</td><td>94</td><td>(82)</td><td>17</td><td>(415)</td><td>(529)</td><td>551</td><td></td><td></td></tr></table>

Source: Company data, MS estimates.

Exhibit 2: VNET – EV/EBITDA vs. US 10-year TIPS (inverse) – key valuation drag  
![](images/c27cc84ddbd81632b3fc5de80c8505f432c54bd98ab4217f186a3651ff996615.jpg)  
Source: FactSet, MS.  
Greater China Telecoms | China

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Tom Tang</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Tom.Tang@morganstanley.com</td><td>+852 3963-1860</td></tr><tr><td colspan="2">Yang Liu</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Yang.Liu@morganstanley.com</td><td>+852 2239-1911</td></tr><tr><td colspan="2">Gary Yu</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Gary.Yu@morganstanley.com</td><td>+852 2848-6918</td></tr></table>

Asia Summer School 2026

![](images/f611b371d08d0bb1d4f2ee48c710be8708ac0b6facd2ad6e9a40e39bd5c90ff2.jpg)

## VNET Group Inc (VNET.O, VNET US)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td>Price target</td><td>US$16.00</td></tr><tr><td>Up/downside to price target (%)</td><td>105</td></tr><tr><td>Shr price, close (Jul 22, 2026)</td><td>US$7.82</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>271</td></tr><tr><td>Mkt cap, curr (mn)</td><td>US$2,119</td></tr><tr><td>EV, curr (mn)</td><td>US$4,578</td></tr><tr><td>Avg daily trading value (mn)</td><td>US$57.00</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (Rmb)**</td><td>(1.52)</td><td>0.98</td><td>2.25</td><td>4.10</td></tr><tr><td>Prior EPS (Rmb)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Revenue, net (Rmb mn)</td><td>9,949</td><td>11,936</td><td>14,492</td><td>17,297</td></tr><tr><td>EBITDA (Rmb mn)</td><td>2,906</td><td>3,640</td><td>4,714</td><td>5,906</td></tr><tr><td>ModelWare net inc (Rmb mn)</td><td>(418)</td><td>264</td><td>610</td><td>1,111</td></tr><tr><td>P/E</td><td>NM</td><td>54.3</td><td>23.5</td><td>12.9</td></tr><tr><td>P/BV</td><td>2.6</td><td>1.7</td><td>1.3</td><td>1.0</td></tr><tr><td>EV/EBITDA</td><td>11.2</td><td>10.5</td><td>9.6</td><td>8.3</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

AlphaSignals Earnings Preview

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">VNET Group Inc VNET.O</td></tr><tr><td>EBITDA growth</td><td>– In-line</td><td>– Largely unchanged</td></tr></table>

\- We forecast EBITDA growth of $23\%$ YoY/1.1% QoQ. The QoQ pace reflects more back-end-loaded capacity addition.

• We also see potential new orders being announced with the coming results.

\*Likely impact to consensus EPS is for the next 12 months

Source: Company data, MS

## Valuation Methodology and Risks

## VNET Group Inc (VNET.O)

Base case, 10-year discounted cash flow (DCF) model. Our assumption of weighted average cost of capital (WACC) is 8.7%, with a 4.0% cost of debt, 14.0% cost of equity and 50% debt weighting. We assume a terminal growth rate (TGR) of 3%.

## Risks to Upside

■ Adding new wholesale contracts

■ Faster move-in than expected

■ Further interest rate cuts in China or the US

■ Progress in asset monetization via REITs at accretive valuations

## Risks to Downside

■ Hyperscalers reducing their cloud capex, especially AI-related investment

■ Delay of capacity delivery

■ Weak sales execution

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Yang Liu; Tom Tang; Gary Yu.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: China Communication Service Co Ltd, GDS Holdings Ltd, VNET Group Inc.

Within the last 12 months, MS has received compensation for investment banking services from GDS Holdings Ltd, HKT Trust and HKT Ltd., PCCW Ltd.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from China Telecom, China Tower Corp Ltd, Far Eastone, GDS Holdings Ltd, HKBN Ltd, PCCW Ltd, SUNeVision Holdings Limited, Taiwan Mobile, VNET Group Inc.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from China Unicom, China United Network Communications, Chunghwa Telecom, VNET Group Inc.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: China Telecom, China Tower Corp Ltd, Far Eastone, GDS Holdings Ltd, HKBN Ltd, HKT Trust and HKT Ltd., PCCW Ltd, SUNeVision Holdings Limited, Taiwan Mobile, VNET Group Inc.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: China Unicom, China United Network Communications, Chunghwa Telecom, VNET Group Inc.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of June 30, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment Services Clients (MISC)</td></tr><tr><td>Stock Rating Category</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of Rating Category</td><td>Count</td><td>% of Total Other MISC</td></tr><tr><td>Overweight/Buy</td><td>1544</td><td>42%</td><td>453</td><td>49%</td><td>29%</td><td>757</td><td>44%</td></tr><tr><td>Equal-weight/Hold</td><td>1577</td><td>43%</td><td>390</td><td>42%</td><td>25%</td><td>769</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>1</td><td>0%</td><td>33%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>544</td><td>15%</td><td>89</td><td>10%</td><td>16%</td><td>204</td><td>12%</td></tr><tr><td>Total</td><td>3,668</td><td></td><td>933</td><td></td><td></td><td>1731</td><td></td></tr></table>

Data include common stock and ADRs currently assigned ratings. Investment Banking Clients are companies from whom MS received investment banking compensation in the last 12 months. Due to rounding off of decimals, the percentages provided in the "% of total" column may not add up to exactly 100 percent.

## Analyst Stock Ratings

Overweight (O). The stock's total return is expected to exceed the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Equal-weight (E). The stock's total return is expected to be in line with the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Not-Rated (NR). Currently the analyst does not have adequate conviction about the stock's total return relative to the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Underweight (U). The stock's total return is expected to be below the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Unless otherwise specified, the time frame for price targets included in MS is 12 to 18 months.

## Analyst Industry Views

Attractive (A): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be attractive vs. the relevant broad market benchmark, as indicated below.

In-Line (I): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be in line with the relevant broad market benchmark, as indicated below. Cautious (C): The analyst views the performance of his or her industry coverage universe over the next 12-18 months with caution vs. the relevant

[中间内容因长度限制已省略]

icated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of China Tower Corp Ltd, GDS Holdings Ltd, HKT Trust and HKT Ltd. listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Greater China Telecoms

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/23/2026)</td></tr><tr><td colspan="3">Gary Yu</td></tr><tr><td>China Mobile Limited (0941.HK)</td><td>E (01/27/2026)</td><td>HK$81.40</td></tr><tr><td>China Mobile Limited (600941.SS)</td><td>E (07/06/2023)</td><td>Rmb94.43</td></tr><tr><td>China Telecom (601728.SS)</td><td>E (07/06/2023)</td><td>Rmb6.04</td></tr><tr><td>China Telecom (0728.HK)</td><td>E (01/27/2026)</td><td>HK$4.64</td></tr><tr><td>China Tower Corp Ltd (0788.HK)</td><td>O (01/21/2025)</td><td>HK$9.83</td></tr><tr><td>China Unicom (0762.HK)</td><td>E (01/27/2026)</td><td>HK$6.63</td></tr><tr><td>China United Network Communications (600050.SS)</td><td>U (10/30/2016)</td><td>Rmb4.42</td></tr><tr><td colspan="3">Tom Tang</td></tr><tr><td>Beijing Sinnet Technology (300383.SZ)</td><td>U (05/16/2022)</td><td>Rmb13.17</td></tr><tr><td>China Communication Service Co Ltd (0552.HK)</td><td>E (11/12/2024)</td><td>HK$4.20</td></tr><tr><td>Chunghwa Telecom (2412.TW)</td><td>E (04/29/2025)</td><td>NT$138.00</td></tr><tr><td>Far Eastone (4904.TW)</td><td>O (10/16/2024)</td><td>NT$102.50</td></tr><tr><td>Guangdong Aofei Data Technology Co Ltd (300738.SZ)</td><td>E (10/23/2023)</td><td>Rmb22.63</td></tr><tr><td>HKBN Ltd (1310.HK)</td><td>E (10/20/2025)</td><td>HK$5.89</td></tr><tr><td>HKT Trust and HKT Ltd. (6823.HK)</td><td>O (12/11/2020)</td><td>HK$12.77</td></tr><tr><td>PCCW Ltd (0008.HK)</td><td>E (09/07/2023)</td><td>HK$5.85</td></tr><tr><td>SUNeVision Holdings Limited (1686.HK)</td><td>O (08/03/2020)</td><td>HK$4.83</td></tr><tr><td>Taiwan Mobile (3045.TW)</td><td>E (01/27/2026)</td><td>NT$112.00</td></tr><tr><td>VNET Group Inc (VNET.O)</td><td>O (10/04/2017)</td><td>US$7.82</td></tr><tr><td colspan="3">Yang Liu</td></tr><tr><td>GDS Holdings Ltd (GDS.O)</td><td>++</td><td>US$32.70</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
