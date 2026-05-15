你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `建议价格：` 一行，给一个资料类商品常见价格区间，例如 `8-20 元`，不要承诺成交价。
3. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
4. `搜索关键词：` 一行，给 8-15 个关键词，用空格分隔。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要写“原版/内部/独家/无水印/全网最低”等容易违规或夸张的词。
- 不要承诺投资收益。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# Global Strategy

# Client views - Oil vs Fed vs ECB vs Carry vs Political risk

Client views after meetings with hedge funds, real money and bank treasury clients in the first half of May. Slides are here: "Iran conflict meets hawkish US."

Appetite for large, directional positions remains limited, though risk-taking has improved since April. Several clients believed that geopolitical risks remain unresolved with energy price tensions unlikely to ease soon. Many pointed to the drop in global oil inventory, and some also thought that upcoming disruptions in supply chains are underestimated. Nevertheless, the realized range on oil prices is less elevated than feared and allows for some risk-taking. Some investors are expecting higher US rates and oil prices to weigh on Q2 risk sentiment so are looking to cut EM/equity exposure after the US tech rally and strong performance in some EM. H2 expected to be a good window to trade central bank pricing as there will be more clarity on how central bankers think on the nature of the ongoing supply shock.

US – Short front-end and duration have worked, with recent US CPI data validating hawkish positioning. A group of clients think that US rates will go higher from here, but there was less conviction on the shape of the curve. Several clients are waiting to see how Chair Warsh will navigate the FOMC and likely higher inflation prints. The concerns are not universal and several real money and treasury clients see value in going long US 10y at 4.50%. At UBS, we have had a baseline of US 10y at 4.50% in Q2 with US 10y reaching 4.75% in case of an extended energy disruption. In meetings ahead of this week's US CPI release, some clients feared that US CPI could be lower than consensus after a relatively high print became baseline. But the April CPI print was relatively hot and in line with further elevated prints ahead. Several clients said that lower new tenants rents will not be enough to push against broader inflationary pressures.

ECB – Central expectation remains a total of 50–75 bps of hikes in 2026, but sentiment has turned more dovish. Investors increasingly question whether more than one hike will be delivered, given subdued wage pressures and emerging growth concerns visible in May PMI data. Clients like structures positioning for backloaded ECB cuts. We have short EUR June '27 vs June '28, but some clients prefer to position for rate cuts further along the curve. Clients also asked us to stress-test the pricing of a ECB hike June. This was before Austrian central bank governor Kocher said that we “cannot call hike June baseline”. As we write, this 20 bps was priced for the June ECB meeting. On our end, we have been receiving July ECB since 19 bps of hikes was priced going into the last ECB meeting (16 bps was priced for the July ECB today).

Relative value in European Government bonds (EGBs). Some clients argued that Italy is more vulnerable than France, and made a case to go short 10y Italy vs France with 10y Italian yields \~11 bps above 10y France. 10y Italy vs France traded around zero in the final quarter of 2025 and rose to 22 bps in March. We think that Italy may eventually underperform France but we do not see the case for near-term underperformance as a moderate search for carry in EGBs has resumed. We have been neutral on Italy, France and Spain against Germany but would not lean against further tightening in spreads. The European Commission is reviewing the escape clause for fiscal rules but we do not see a repeat of the fiscal support granted in the pandemic with ECB president Lagarde echoing comments of other euro area central bankers that the price signal in particular should not be eliminated by the fiscal measures that should be temporary and targeted.

# Global Strategy

Global

Reinout De Bock

Strategist

reinout.de-bock@UBS.com

+44-20-7567 0152

Mustafa Oguz Caylan

Strategist

mustafa.caylan@UBS.com

+44-20-7901 5203

Bhanu Baweja

Strategist

bhanu.baweja@UBS.com

+44-20-7568 6833

UK – Demand is emerging at higher yields, but opinions diverge. Some interest in longs has started to emerge at higher gilt yields, but long positions taken ahead of local elections or on Friday after elections have performed poorly. BoE MPC member Mann warned about the implications for the UK change in the investor base for gilts away from domestic pension funds to highly price-sensitive foreign funds. This dynamic is now also a concern with investors. On our end, we opened 5s10s steepeners at 45bps (target: 65bps and stop: 30bps) at the start of this week. We went long June BoE (opened at 19 bps of hikes) before the last BOE meeting.

Extras - We did not pick up material concerns on US or EUR funding markets (despite issuance likely picking up in May/June). Investors are eager for more clarity on German budgets for 2027-28 and coalition dynamics are closely followed given deteriorating approval ratings.

# Recent Notes

UK curve: Higher and steeper for longer (12 May)

2026 Outlook – Iran conflict meets hawkish US (11 May)

AI releases did not lower rates or reduce fiscal risks in '25-26 (8 May)

Not long 10y UK at 4.94% - Rate uncertainty, politics and oil (7 May)

Receive 1y1y SEK versus USD (5 May)

AI - No clear path to lower rates (5 May)

Receiving July ECB at 19 bps, still short June '27 vs June '28 Euribor (30 Apr)

US Refunding - Revising expected '26 coupon supply slightly lower (29 Apr)

Receive BoE June Meeting at 19 bps (29 Apr)

Warsh vs Bernanke Fed - More volatile rates ahead? (28 Apr)

UK Remit Revisions and Supply Chart Pack (23 Apr)

IMF Takeaways - Trading "one transitory shock after another" (20 April)

UK 10y higher for longer: 4.75% at end '26 (from 4.05%) (20 April)

End '26 Forecast: 10y US at 4.25% (4%) - bund at 2.75% (3%) (16 April)

Figure 1: Open UBS rates trades 

<table><tr><td>Market</td><td>Position</td><td>Entry Date</td><td>Entry Level</td><td>Current Level</td><td>Target</td><td>Stop</td><td>Gain (bps)</td></tr><tr><td>USD</td><td>Long 2s7s10s SOFR butterfly</td><td>27-Mar-26</td><td>-8</td><td>-4</td><td>-40</td><td>10</td><td>-4</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EUR</td><td>Receive July ECB</td><td>30-Apr-26</td><td>19</td><td>17</td><td>0</td><td>28</td><td>3</td></tr><tr><td>EUR</td><td>Long 10y EU vs Germany</td><td>27-Mar-26</td><td>35</td><td>33</td><td>20</td><td>45</td><td>2</td></tr><tr><td>EUR</td><td>Long 10y bunds (%)</td><td>26-Mar-26</td><td>3.00</td><td>3.10</td><td>2.75</td><td>3.25</td><td>-10</td></tr><tr><td>EUR</td><td>Pay June &#x27;27 Euribor vs receive June &#x27;28 Euribo</td><td>21-Mar-26</td><td>-3</td><td>-14</td><td>-30</td><td>-10</td><td>11</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GBP</td><td>Long nominal 5s10s steepener</td><td>12-May-26</td><td>45</td><td>46</td><td>65</td><td>30</td><td>1</td></tr><tr><td>GBP</td><td>Receive BoE June Meeting</td><td>29-Apr-26</td><td>19</td><td>11</td><td>0</td><td>30</td><td>8</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CHF</td><td>Receive SARON Sep-27 (%)</td><td>11-Mar-26</td><td>0.22</td><td>0.35</td><td>0.00</td><td>0.40</td><td>-13</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AUD</td><td>Pay 1y swap (%)</td><td>23-Mar-26</td><td>4.76</td><td>4.73</td><td>5.00</td><td>4.70</td><td>-3</td></tr><tr><td>AUD</td><td>Pay AUD 10y EFP</td><td>16-Mar-26</td><td>5</td><td>6</td><td>15</td><td>1</td><td>1</td></tr><tr><td>AUD</td><td>Receive 5y2y (%)</td><td>14-Jan-26</td><td>4.83</td><td>5.08</td><td>4.40</td><td>5.10</td><td>-25</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>NZD</td><td>Pay May-26 RBNZ vs Receiving 1y1y (%)</td><td>21-Apr-26</td><td>1.49</td><td>1.68</td><td>1.40</td><td>1.60</td><td>-19</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JPY</td><td>Long 6m fwd 2s10s steepener</td><td>09-Feb-26</td><td>64</td><td>85</td><td>100</td><td>55</td><td>21</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SEK VS USD</td><td>Receive 1y1y SEK vs USD (%)</td><td>05-May-26</td><td>-1.31</td><td>-1.56</td><td>-1.65</td><td>-1.20</td><td>25</td></tr></table>

Source: Bloomberg, Haver, UBS. Past performance is not necessarily indicative of future results.

We would like to thank Deepak Joy and Mehak Bhalla, our research support service professionals in our Hyderabad Research BSC, for assisting in preparing this research report.

A record of our current and 12 month historical, Rates trade recommendations is available on UBS Neo or via your UBS sales representative.

# Valuation Method and Risk Statement

Risks of multi-asset investing include but are not limited to market risk, credit risk, interest rate risk, and foreign exchange risk. Correlations of returns among different asset classes may deviate from historical patterns. Geopolitical events and policy shocks pose risks that can reduce asset returns. Valuations may be adversely affected during times of high market volatility, thin liquidity, and economic dislocation. Valuation methods across sectors include DCF, SOTP and multiples analysis.

# Required Disclosures

This document has been prepared by UBS AG London Branch, an affiliate of UBS AG. UBS AG, its sUBSidiaries, branches and affiliates, including former CS AG and its sUBSidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.UBS.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 14 May 2026 09:40 AM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.UBS.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on UBS-quant-answers@UBS.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

# Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

Research analysts contributing to this report who are employed by any non-US affiliate of UBS LLC are not registered/qualified as research analysts with FINRA. Such analysts may not be associated persons of UBS LLC and therefore are not subject to the FINRA restrictions on communications with a subject company, public appearances, and trading securities held by a research analyst account. The name of each affiliate and analyst employed by that affiliate contributing to this report, if any, follows.

UBS AG London Branch: Bhanu Baweja, Mustafa Oguz Caylan, Reinout De Bock.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies discussed in this report, including information on valuation and risk, please contact UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research.

# UBS Global Research Disclaimer

This document has been prepared by UBS AG London Branch, an affiliate of UBS AG. UBS AG, its sUBSidiaries, branches and affiliates, including former CS AG and its sUBSidiaries, branches and affiliates are referred to herein as "UBS".

Any opinions expressed in this document may change without notice and are only current as of the date of publication. Different areas, groups, and personnel within UBS may produce and distribute separate research products independently of each other. For example, research publications from UBS CIO are produced by UBS Global Wealth Management. UBS Global Research is produced by UBS Investment Bank. Research methodologies and rating systems of each separate research organization may differ, for example, in terms of investment recommendations, investment horizon, model assumptions, and valuation methods. As a consequence, except for certain economic forecasts (for which UBS CIO and UBS Global Research may collaborate), investment recommendations, ratings, price targets, and valuations provided by each of the separate research organizations may be different, or inconsistent. You should refer to each relevant research product for the details as to their methodologies and rating system. Not all clients may have access to all products from every organization. Each research product is subject to the policies and procedures of the organization that produces it.

# This document is provided solely to recipients who are expressly authorized by UBS to receive it. If you are not so authorized you must immediately destroy the document.

UBS Global Research is provided to our clients through UBS Neo, and in certain instances, UBS.com and any other system or distribution method specifically identified in one or more communications distributed t

[中间内容因长度限制已省略]

edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr. Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: ol-UBS-sec-compliance@UBS.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.UBS.com/global/en/about\_UBS/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.UBS.com/UBSsi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a sUBSidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian Citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian Citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/6978e3db8c630d56ee2e19ff44a2f26a7124b32e76aaa5df613ef4ff29e63e63.jpg)

# UBS
"""
