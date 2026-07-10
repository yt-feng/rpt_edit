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
# Potential Debit Network Sale Could Unlock Value; Another Leadership Change Adds to Uncertainty

What happened: WSJ reported that US banks are exploring an acquisition of FISV's debit networks (STAR and Accel) to circumvent debit interchange limits imposed by the Durbin Amendment. The article, citing “people familiar with the matter”, reports that banks including JPM, BAC, WFC, and PNC have engaged with FISV over a potential deal, but that at least “several of the banks” have indicated that they are unlikely to pursue an acquisition. Fiserv and other parties mentioned did not provide a comment to the WSJ and we have no knowledge of any potential transaction. JPM (JPM), BofA (BAC), Wells Fargo (WFC) & PNC Financial Services (PNC) are covered by Manan Gosalia; Capital One Financial (COF) is covered by Jeffrey Adelson.

Separately, Dhivya Suryadevara's resignation likely to be viewed as incrementally negative as investors assess execution risk in Financial Solutions, leadership continuity, and durability of strategic reset. Fiserv disclosed today that Dhivya Suryadevara, President of Fiserv, resigned effective July 7, with Andrew Gelb, EVP and COO, Financial Solutions, and Srini Krish, Head of Technology and Operations, Financial Solutions, appointed as interim leaders of the company's Financial Solutions business. We expect the announcement to add to investor uncertainty around the trajectory of Financial Solutions, particularly given Suryadevara's relatively recent appointment, her visible role at Investor Day, and her involvement in shaping the turnaround strategy for a business facing bank client churn, technology-conversion challenges, and service-quality concerns. The departure also follows closely on the resignation of CEO Mike Lyons and the appointment of Takis Georgakopoulos as CEO, further reinforcing questions around leadership continuity.

Logic of potential FISV deal for banks: Per the report, the rationale would be similar to COF's acquisition of Discover, which allows COF to charge higher interchange rates on debit transactions, which COF initially indicated would yield just over \$1B a year in operational synergies.

Implications for MA/V: We ultimately think MA and V's network scale, speed, security, merchant routing optimization, dispute infrastructure, fraud tools, issuer processing, and acceptance breadth would be costly and complex to replicate. We expect the required investment is perhaps one of the reasons that a similar acquisition hasn't been pursued before (though we acknowledge valuations are more attractive now than historically). Notably, JPM's ChaseNet is proprietary closed-loop merchant processing network, launched in 2013, that was designed to

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">James E Faucette</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>James.Faucette@morganstanley.com</td><td>+1 212 296-5771</td></tr><tr><td colspan="2">Meryl R Thomas, CFA</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Meryl.Thomas@morganstanley.com</td><td>+1 212 761-0774</td></tr><tr><td colspan="2">Michael N Infante</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Michael.Infante@morganstanley.com</td><td>+1 212 761-4631</td></tr><tr><td colspan="2">Shefali Tamaskar</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Shefali.Tamaskar@morganstanley.com</td><td>+1 212 761-4948</td></tr></table>

## Fiserv Inc. (FISV.O, FISV US)

<table><tr><td colspan="2">Payments and Processing | United States of America</td></tr><tr><td>Stock Rating</td><td>Equal-weight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$65.00</td></tr><tr><td>Shr price, close (Jul 6, 2026)</td><td>$51.78</td></tr><tr><td>Mkt cap, curr (mm)</td><td>$26,770</td></tr><tr><td>52-Week Range</td><td>$175.92-47.04</td></tr></table>

simplify the traditional payment ecosystem by having Chase act as the merchant acquirer, card network, and issuing bank for transactions made with Chase credit and debit cards. However, it still relies on Visa's processing network (VisaNet) to route transactions. If a bank does choose to pursue the own-network strategy to increase debit interchange economics, we estimate the loss of one large debit issuer would likely represent \~0.5-1% headwind to MA or V's revenue (similar magnitude as COF rolling off debit volumes from MA), depending on which bank and timing. Historically, we feel FISV management have been dismissive of the viability of adapting STAR/Accel to being credit networks, and we note there wouldn't be incremental interchange uplift from owning a credit network as those rates aren't regulated.

Exhibit 1: Debit transactions covered by the Durbin Amendment are capped at 21c + .05%  
Average Debit Card Interchange Fee, by Transaction Status and Network Type  
![](images/db1eb7db2bd78bf3f0cc047ac038b9e1914bafe2df29727a130d5fdb06f076d3.jpg)  
Source: Federal Reserve

Potential value to FISV if it announced a sale of its debit networks: FISV does not break out revenue or earnings contribution from its STAR and Accel debit networks, but we estimate that the networks generate \~\$500M in EBITDA. Digital Payments in total makes up \$3.9B or 19% of total revenue, and we believe debit network revenue is about \~\$1B or 10%, with volumes growing low-double digits in 1Q26 following price cuts in '25, and an estimated \~50% EBITDA margin. We estimate current payments valuations likely values the business at around \~\$3-\$4B based on an assumed multiple range of 6-8x, and a potential acquirer that could generate larger synergies from debit interchange uplift might be willing to pay above a 20% premium. Proceeds could support deleveraging or additional buybacks (Street looks for \$7B in buybacks in '27-29, or 25% of market cap).

Exhibit 2: FISV's Digital Payments business makes up 19% of total  
Fiserv 2026E Revenue Mix %  
![](images/9c09512ddfcf28c9b79e81f1ede46bfe01199d0d808bcaf611fa3e26d288d89a.jpg)  
Source: MS Estimates

CHYM/XYZ could see greater implications long-term if FISV announced the sale of its debit networks: We think any such potential deal, if announced, could create more competitive intensity in the low-end consumer segment of the market, as large banks could more economically serve that segment through the same exempted debit interchange revenue stream that CHYM and XYZ's Cash App generate. If large banks can recapture higher debit interchange economics through owned-network structures, they could redeploy those economics into debit rewards, free checking, early-paycheck access, overdraft relief, ATM access, or lower-fee consumer-banking products. That would directly pressure the value proposition that has helped CHYM and Cash App serve debit-heavy, lower-income, and paycheck-to-paycheck consumers at lower fees. For reference, we estimate debit-interchange related revenue is 40% of Chime's total, and 15% of XYZ's total.

Exhibit 3: We estimate higher debit interchange rates support 40% of CHYM's revenue, and drive the pricing advantage for other features

CHYM 2026E Revenue Mix %  
![](images/e1a2dca6730183a14fa2b7da4340a5dbdb7eee9c877e74a2798c905795328f10.jpg)  
Source: MS Estimates

## Valuation Methodology and Risks

## Chime Financial Inc (CHYM.O)

Our 5x EV/Txn Profit multiple on our '27 forecasts is at a modest premium to peers on a growth-adjusted basis, given Chime's 1) higher quality customer relationships, 2) consistent execution + product development, and 3) less cyclical overall revenue exposure, with limited credit revenues and 70% nondiscretionary purchase volume. Our 5x multiple is a \~3x premium to slower-growing Block (Cash App) and a 3x discount to slightly faster-growing AFRM.

## Risks to Upside

■ Faster rollout of unsecured credit card with well managed losses

■ Improved capture of young or higher-income customers within forecast period

■ Strong execution on Chime Enterprise that accelerates user acquisition

■ Better than expected profitability ramp

## Risks to Downside

■ Worsening macro/employment conditions

■ Increased regulatory risk related to Durbin Debit amendment.

■ High loss rates on newer credit products

## Fiserv Inc. (FISV.O)

Our PT is derived by applying a 7x P/E multiple on our 2027 Adj. EPS. This is at a slight discount to payments peers on a growth adjusted basis given modest execution risk.

## Risks to Upside

■ Client wins

■ Fls increase outsourced tech spend

■ Clover significantly outpaces peers

■ Faster deleveraging, resulting in new accretive M&A

## Risks to Downside

■ Competitive losses or decreased outsourced tech spend

■ Security breach leading to client loss/investments

■ Consolidation of FIs

■ Competition drives up investments, pressuring margins

■ Pricing sensitivity returns to merchant acquiring

## MasterCard Inc (MA.N)

Based on a 30x target P/E multiple on our base-case 2027 EPS estimate. This target multiple is generally in-line with where MA has historically traded and at a \~8x premium to where the stock currently trades.

## Risks to Upside

■ Uptick in consumer spending trends

■ New client wins in the US/Europe

## Risks to Downside

■ Impact from regulatory action in Europe and elsewhere

■ Material slowdown in consumer spending

■ Potential for market share loss in Europe as V becomes more aggressive

## Visa Inc. (V.N)

Based on 27x target P/E multiple on our base-case CY27 EPS estimate. This target multiple is slightly below V's 5-year average multiple and at a \~6x premium to where V currently trades.

## Risks to Upside

■ Faster than expected recovery of cross-border tourism

■ Ability to continue to meet/beat expectations

■ Faster-than-expected adoption/scaling of B2B solutions, driving multiple expansion

## Risks to Downside

■ Material slowdown in consumer spend; Slow recovery in cross-border growth

■ Portfolio losses in the US

■ Regulatory changes in key markets promoting domestic schemes

## Block, Inc (XYZ.N)

Our price target applies an 18x multiple to CY27 SBC-burdened adjusted EPS, which is in-line to peers' on a growth-adjusted basis.

## Risks to Upside

■ Faster ramp in Cash app credit products could accelerate revenue/user growth

■ Faster-than-expected move up-market, without deterioration in take rate, could drive upside from core payment

■ Meaningful profitability outperformance

## Risks to Downside

■ Expansion internationally/up-market pressure margins, and slow vol. ramp limits growth.

■ Competition drives pricing pressure across merchant segments

■ Regulatory intervention

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: James E Faucette; Michael N Infante; Shefali Tamaskar; Meryl R Thomas, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Affirm Holdings Inc, Automatic Data Processing Inc, Block, Inc, Broadridge Financial Solutions Inc., Circle Internet Group Inc., Corpay Inc, Evertec Inc, Fidelity National Information Services, Fiserv Inc., Flywire Corp, Galaxy Digital Inc., Global Payments Inc, Jack Henry & Associates, Inc., MasterCard Inc, nCino, Inc., NerdWallet Inc., Paychex Inc, PayPal Holdings, Inc., Q2 Holdings Inc, Shift4 Payments Inc., Upstart Holdings, Inc., Verra Mobility Corp, Visa Inc., Western Union Co, WEX Inc.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Affirm Holdings Inc, Automatic Data Processing Inc, Block, Inc, Broadridge Financial Solutions Inc., Galaxy Digital Inc., Global Payments Inc, Klarna Group Plc, MasterCard Inc, PayPal Holdings, Inc..

Within the last 12 months, MS has received compensation for investment banking services from Affirm Holdings Inc, Automatic Data Processing Inc, Block, Inc, Broadridge Financial Solutions Inc., Evertec Inc, Galaxy Digital Inc., Global Payments Inc, Klarna Group Plc, MasterCard Inc, PayPal Holdings, Inc., SS&C Technologies Holdings, Inc..

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Affirm Holdings Inc, Automatic Data Processing Inc, Block, Inc, Broadridge Financial Solutions Inc., Chime Financial Inc, Circle Internet Group Inc., Corpay Inc, Evertec Inc, Fidelity National Information Services, Fiserv Inc., Flywire Corp, Galaxy Digital Inc., Global Payments Inc, Global-e Online Ltd., Jack Henry & Associates, Inc., Klarna Group Plc, Marqeta, Inc., MasterCard Inc, nCino, Inc., NerdWallet Inc., Paychex Inc, PayPal Holdings, Inc., Q2 Holdings Inc, SS&C Technologies Holdings, Inc., Upstart Holdings, Inc., Visa Inc., Western Union Co, WEX Inc.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Affirm Holdings Inc, Automatic Data Processing Inc, Block, Inc, Broadridge Financial Solutions Inc., Chime Financial Inc, Corpay Inc, Fidelity National Information Services, Fiserv Inc., Global Payments Inc, Global-e Online Ltd., Klarna Group Plc, MasterCard Inc, Paychex Inc, PayPal Holdings, Inc., Shift4 Payments Inc., SS&C Technologies Holdings, Inc., Verra Mobility Corp, Visa Inc., Western Union Co, WEX Inc.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Affirm Holdings Inc, Automatic Data Processing Inc, Block, Inc, Broadridge Financial Solutions Inc., Chime Financial Inc, Circle Internet Group Inc., Corpay Inc, Evertec Inc, Fidelity National Information Services, Fiserv Inc., Flywire Corp, Galaxy Digital Inc., Global Payments Inc, Global-e Online Ltd., Jack Henry & Associates, Inc., Klarna Group Plc, Marqeta, Inc., MasterCard Inc, nCino, Inc., NerdWallet Inc., Paychex Inc, PayPal Holdings, Inc., Q2 Holdings Inc, SS&C Technologies Holdings, Inc., Upstart Holdings, Inc., Visa Inc., Western Union Co, WEX Inc.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Affirm Holdings Inc, Automatic Data Processing Inc, Block, Inc, Broadridge Financial Solutions Inc., Chime Financial Inc, Corpay Inc, Fidelity National Information Services, Fiserv Inc., Global Payments Inc, Global-e Online Ltd., Klarna Group Plc, MasterCard Inc, Paychex Inc, PayPal Holdings, Inc., Q2 Holdings Inc, Shift4 Payments Inc., SS&C Technologies Holdings, Inc., Upstart Holdings, Inc., Verra Mobility Corp, Visa Inc., Western Union Co, WEX Inc.

MS & Co. LLC makes a market in the securities of Broadridge Financial Solutions Inc., Corpay Inc, Evertec Inc, Flywire Corp, Global-e Online Ltd., Jack Henry & Associates, Inc., Marqeta, Inc., NerdWallet Inc., Q2 Holdings Inc, SS&C Technologies Holdings, Inc., Verra Mobility Corp, WEX Inc.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions b

[中间内容因长度限制已省略]

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The following companies do business in countries which are generally subject to comprehensive sanctions programs administered or enforced by the U.S. Department of the Treasury's Office of Foreign Assets Control ("OFAC") and by other countries and multi-national bodies: MasterCard Inc.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Payments and Processing

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/07/2026)</td></tr><tr><td colspan="3">James E Faucette</td></tr><tr><td>Affirm Holdings Inc (AFRM.O)</td><td>E (06/25/2026)</td><td>$83.62</td></tr><tr><td>Automatic Data Processing Inc (ADP.O)</td><td>E (02/25/2021)</td><td>$245.60</td></tr><tr><td>Block, Inc (XYZ.N)</td><td>O (02/27/2026)</td><td>$77.56</td></tr><tr><td>Broadridge Financial Solutions Inc. (BR.N)</td><td>E (12/14/2022)</td><td>$148.60</td></tr><tr><td>Chime Financial Inc (CHYM.O)</td><td>O (07/07/2025)</td><td>$21.12</td></tr><tr><td>Circle Internet Group Inc. (CRCL.N)</td><td>E (02/02/2026)</td><td>$65.15</td></tr><tr><td>Evertec Inc (EVTC.N)</td><td>E (11/21/2024)</td><td>$28.60</td></tr><tr><td>Fidelity National Information Services (FIS.N)</td><td>E (07/07/2026)</td><td>$42.60</td></tr><tr><td>Fiserv Inc. (FISV.O)</td><td>E (10/30/2025)</td><td>$52.71</td></tr><tr><td>Galaxy Digital Inc. (GLXY.O)</td><td>O (11/06/2025)</td><td>$24.73</td></tr><tr><td>Global-e Online Ltd. (GLBE.O)</td><td>O (03/26/2025)</td><td>$36.92</td></tr><tr><td>Global Payments Inc (GPN.N)</td><td>E (06/22/2026)</td><td>$77.59</td></tr><tr><td>Jack Henry &amp; Associates, Inc. (JKHY.O)</td><td>E (06/15/2022)</td><td>$146.71</td></tr><tr><td>Klarna Group Plc (KLAR.N)</td><td>E (10/06/2025)</td><td>$19.42</td></tr><tr><td>MasterCard Inc (MA.N)</td><td>O (03/28/2016)</td><td>$531.62</td></tr><tr><td>Paychex Inc (PAYX.O)</td><td>E (02/25/2021)</td><td>$108.12</td></tr><tr><td>PayPal Holdings, Inc. (PYPL.O)</td><td>U (12/18/2025)</td><td>$45.65</td></tr><tr><td>Shift4 Payments Inc. (FOUR.N)</td><td>E (08/25/2023)</td><td>$51.16</td></tr><tr><td>SS&amp;C Technologies Holdings, Inc. (SSNC.O)</td><td>E (10/28/2019)</td><td>$66.30</td></tr><tr><td>Upstart Holdings, Inc. (UPST.O)</td><td>E (02/14/2025)</td><td>$33.06</td></tr><tr><td>Verra Mobility Corp (VRRM.O)</td><td>E (05/26/2021)</td><td>$4.22</td></tr><tr><td>Visa Inc. (V.N)</td><td>O (03/28/2016)</td><td>$352.20</td></tr><tr><td>Western Union Co (WU.N)</td><td>U (02/02/2015)</td><td>$7.95</td></tr><tr><td colspan="3">Michael N Infante</td></tr><tr><td>Corpay Inc (CPAY.N)</td><td>O (01/26/2026)</td><td>$357.10</td></tr><tr><td>Flywire Corp (FLYW.O)</td><td>O (03/02/2026)</td><td>$18.55</td></tr><tr><td>Marqeta, Inc. (MQ.O)</td><td>E (02/25/2026)</td><td>$15.93</td></tr><tr><td>nCino, Inc. (NCNO.O)</td><td>O (09/10/2025)</td><td>$18.06</td></tr><tr><td>NerdWallet Inc. (NRDS.O)</td><td>U (03/13/2026)</td><td>$9.50</td></tr><tr><td>Q2 Holdings Inc (QTWO.N)</td><td>E (08/10/2020)</td><td>$53.95</td></tr><tr><td>WEX Inc (WEX.N)</td><td>E (02/25/2021)</td><td>$153.14</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
