你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

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

UBS Global Research is provided to our clients through UBS Neo, and in certain instances, UBS.com and any other system or distribution method specifically identified in one or more communications distributed through UBS Neo or UBS.com (each a system) as an approved means for distributing UBS Global Research. It may also be made available through third party vendors and distributed by UBS and/or third parties via e-mail or alternative electronic means.

All UBS Global Research is available on UBS Neo. Please contact your UBS sales representative if you wish to discuss your access to UBS Neo. Where UBS Global Research refers to "UBS Evidence Lab Inside" or has made use of data provided by UBS Evidence Lab and you would like to access that data please contact your UBS sales representative. UBS Evidence Lab data is available on UBS Neo. The level and types of services provided by UBS Global Research and UBS Evidence Lab to a client may vary depending upon various factors such as a client's individual preferences as to the frequency and manner of receiving communications, a client's risk profile and investment focus and perspective (e.g., market wide, sector specific, long-term, short-term, etc.), the size and scope of the overall client relationship with UBS Global Research and UBS Evidence Lab and legal and regulatory constraints. UBS HOLT and UBS Pharma Values are offerings of UBS Global Research. HOLT Lens is a corporate performance platform offering that provides an objective accounting-led framework for comparing and valuing companies and is available to clients of UBS Global Research; for further details and pricing please contact your UBS Sales representative. In particular, HOLT has a variety of warranted prices based on the scenario chosen; please mail UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research, if you are interested in the warranted price on a particular company, again subject to commercial considerations. UBS Pharma Values is an analytical tool that involves the creation of a number of individual product net present value calculations, based on published forecasts of sales for pharmaceuticals, and is available to clients of UBS Global Research; for further details and pricing please contact your UBS Sales representative. For all other specific disclaimers, please see https://www.UBS.com/disclosures.

When you receive UBS Global Research through a system, your access and/or use of such UBS Global Research is subject to this UBS Global Research Disclaimer and to the UBS Neo Platform Use Agreement (the "Neo Terms") together with any other relevant terms of use governing the applicable System.

When you receive UBS Global Research via a third party vendor, e-mail or other electronic means, you agree that use shall be subject to this UBS Global Research Disclaimer, the Neo Terms and where applicable the UBS Investment Bank terms of business (https://www.UBS.com/global/en/investment-bank/regulatory.html) and to UBS's

[中间内容因长度限制已省略]

y recommendations or opinions in such this publication or material are not made or provided to you, and (ii) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material and (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr. Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: ol-UBS-sec-compliance@UBS.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.UBS.com/global/en/about\_UBS/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.UBS.com/UBSsi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a sUBSidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian Citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian Citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/6978e3db8c630d56ee2e19ff44a2f26a7124b32e76aaa5df613ef4ff29e63e63.jpg)

# UBS
"""
