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
# First Read

# China Aluminum Sector

# Takeaways on China, Indonesia, and Middle East

# China: updates on overproduction

We hosted an Aladdiny expert meeting. Expert estimates China's aluminium output to reach 45.5mt in 2026 (+2% vs. 44.5mt in 2025). Amid recent concerns on overproduction, expert attributes this primarily to: 1) Legacy non-compliant capacity continues to operate. Projects initiated 3-5 years ago without final approval were built and commissioned during the application phase and remain active, with volumes estimated at 0.6-0.7mtpa (e.g. Guangxi 0.1mt exposed). 2) Capacity swaps are not fully synchronized. New capacity is often ramped up before legacy assets are shut, temporarily pushing output above approved levels. 3) Higher-amperage operations exist but remain limited. Producers are cautious about maximizing short-term output, as this increases next-year performance pressure and shortens pot life. 4) Incremental pot upgrades have modestly increased per-unit productivity. Expert notes effective operating capacity already exceeds 45.5mt, including unapproved legacy volumes. Local governments have limited incentive to enforce cuts given strong fiscal contributions. At the central level, expert indicates policy focus may gradually shift toward formalizing legacy capacity through carbon compliance onwards. Once resolved, authorized capacity might rise to \~46mt, broadly aligned with the current ceiling.

# Indonesia: capacity ramp faces rising practical constraints

Expert expects Indonesia to add 2.2mt/2.0mt of aluminium capacity in 2026/27 (1.1mt/1.8mt output, Figure 1). While smelters are attempting to ramp up ahead of schedule amid strong margins, execution risks remain high: 1) Tax incentives are a key constraint. Many smelters have yet to secure tax-exempt status, covering import duties (13.5%), export taxes and corporate income tax. Without these exemptions, margins are compressed, discouraging sales. Juwan and Adaro have accumulated \~0.1mt of unsold inventory in 2025, and Adaro may not obtain approval through 2027, potentially adding \~0.3mt of inventory in 2026. 2) Power and equipment constraints. Power plant construction requires >2 years, while delivery of Chinese generating equipment can take \~4 years due to lengthy order backlogs. Pots also face 6–12 month delivery time. Tsingshan plans to divert power from nickel to aluminium based on current margin differentials, supporting near-term supply. However, from 2027, power availability becomes less certain as new capacity ramps and relative nickel/aluminium profitability may change. In alumina, Indonesia plans to add 1mt/5.2mt of capacity in 2026/27 (2.1mt/2.0mt output). The key constraint is bauxite mining approvals (RKAB): 1) Shift to annual approvals has slowed progress; as of end-May, only \~1/3 of quotas had been approved, limiting feedstock supply. 2) Regulatory tightening adds further friction, including higher land fees, stricter environmental standards, production controls and downstream linkage requirements. 3) HPM-linked pricing also supported bauxite FOB prices to \~USD42/t (from USD32/t in Jan), pushing alumina production costs up to Rmb2,200–2,400/t (from Rmb2,000–2,200/t).

# Middle East: persistent supply disruptions

In the Middle East, the expert expects aluminium output to decline by \~2.2mt in 2026, with 3.5–3.8mt of capacity affected. Disruptions are driven by both feedstock shortages and facility damage: 1) Raw material shortages have curtailed capacity at Alba (>1.1mt), Jebel Ali (\~0.2mt) and Iran (>0.3mt), with restart timelines of 3–6 months. 2) More severe damage to smelting and power infrastructure at Al Taweelah (>1.6mt) and Qatalum (\~0.2mt) implies longer recovery timelines of >12 months. Logistics remain constrained. Limited alumina inflows via the Red Sea and Gulf ports support only partial operations in Bahrain and Qatar, while aluminium exports are restricted, with only limited aluminum ingot shipments from Saudi Arabia. Expert estimates regional inventories have built to \~1.1-1.2mt since disruptions began.

# Equities

China

Aluminum

Beili Wang

Analyst

beili.wang@ubs.com

+852-2971 7812

Sharon Ding

Analyst

sharon.ding@ubs.com

+852-2971 6284

Elvis Liu

Associate Analyst

elvis.liu@ubs.com

+852-3712 3052

Figure 1: Capacity and output estimate for Indonesia aluminium smelter progress   
Capacity: Indonesia aluminium smelter progress estimate (unit: 10kt) 

<table><tr><td>Group</td><td>Project</td><td>Venue</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E+</td><td>Remarks</td></tr><tr><td>Tsingshan / Huafeng</td><td>Huaqing (Morowali)</td><td>Sulawesi</td><td>50</td><td>50</td><td>50</td><td>50</td><td>50</td><td>Planned 1.0mt; second 0.5mt deferred (no land/power)</td></tr><tr><td>Tsingshan / Xinfa</td><td>Taijing/HF (Morowali)</td><td>Sulawesi</td><td></td><td>60</td><td>60</td><td>60</td><td>60</td><td>Started May26; ~0.6mt by end-26</td></tr><tr><td>Tsingshan / Xinfa</td><td>Taiyun (Morowali)</td><td>Sulawesi</td><td></td><td></td><td>60</td><td>60</td><td>60</td><td>Power constraints; full ramp by late-2026/early-2027 if smooth</td></tr><tr><td>Tsingshan / Xinfa</td><td>Juwan (Weda Bay)</td><td>Maluku</td><td>20</td><td>27</td><td>27</td><td>27</td><td>27</td><td>Full ramp delayed from Dec-25 to mid-Feb 2026</td></tr><tr><td>Tsingshan / Xinfa</td><td>Xianfeng (Weda Bay)</td><td>Maluku</td><td></td><td>33</td><td>33</td><td>33</td><td>33</td><td>Starts early Jun-26; full ramp by end-Oct 2026</td></tr><tr><td>Tsingshan</td><td>Weda Bay Industrial Park</td><td>Maluku</td><td></td><td>40</td><td>80</td><td>80</td><td>80</td><td>Phase 1: 0.4mt (early 2027); Phase 2: 0.4mt (2028)</td></tr><tr><td>Nanshan A/H</td><td>Bintan Nanshan</td><td>Riau Islands</td><td></td><td>13</td><td>50</td><td>50</td><td>100</td><td>A: 0.125mt (end-26), 0.125mt (27); H: 0.25mt (27–28), 0.5mt (post-28)</td></tr><tr><td>Inalum</td><td>Inalum</td><td>North Sumatra</td><td>28</td><td>28</td><td>28</td><td>28</td><td>90</td><td>Remaining 0.6mt post-2029; likely delayed to 2032</td></tr><tr><td>Adaro / Lygend</td><td>PT KAI</td><td>North Kalimantan</td><td></td><td>43</td><td>50</td><td>50</td><td>150</td><td>0.425mt in 26; ~0.3mt sales potentially delayed (no tax-exempt status)</td></tr><tr><td>Harita / Weiqiao</td><td>PT DIB</td><td>North Kalimantan</td><td></td><td></td><td>50</td><td>100</td><td>100</td><td>Two phases: 0.5mt (2H27), 0.5mt (28)</td></tr><tr><td>Bosai</td><td>PT Bosai</td><td>East Java</td><td></td><td></td><td>30</td><td>60</td><td>60</td><td>Two phases: 0.3mt (4Q27), 0.3mt (2028)</td></tr><tr><td>East Hope</td><td>PT WAI</td><td>West Kalimantan</td><td></td><td></td><td></td><td></td><td>240</td><td>No land/power; 28–29 unlikely start, excluded from the total number</td></tr><tr><td>Total</td><td></td><td></td><td>98</td><td>313</td><td>518</td><td>598</td><td>810</td><td></td></tr></table>

New capacity

Production: Indonesia aluminium smelter progress estimate (unit: 10kt) 

<table><tr><td>Group</td><td>Project</td><td>Venue</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E+</td><td>Remarks</td></tr><tr><td>Tsingshan / Huafeng</td><td>Huaqing (Morowali)</td><td>Sulawesi</td><td>50</td><td>50</td><td>50</td><td>50</td><td>50</td><td>Planned 1.0mt; second 0.5mt deferred (no land/power)</td></tr><tr><td>Tsingshan / Xinfa</td><td>Taijing/HF (Morowali)</td><td>Sulawesi</td><td></td><td>35</td><td>60</td><td>60</td><td>60</td><td>Started May26; ~0.6mt by end-26</td></tr><tr><td>Tsingshan / Xinfa</td><td>Taiyun (Morowali)</td><td>Sulawesi</td><td></td><td></td><td>60</td><td>60</td><td>60</td><td>Power constraints; full ramp by late-2026/early-2027 if smooth</td></tr><tr><td>Tsingshan / Xinfa</td><td>Juwan (Weda Bay)</td><td>Maluku</td><td>10</td><td>27</td><td>27</td><td>27</td><td>27</td><td>Full ramp delayed from Dec-25 to mid-Feb 2026</td></tr><tr><td>Tsingshan / Xinfa</td><td>Xianfeng (Weda Bay)</td><td>Maluku</td><td></td><td>15</td><td>30</td><td>33</td><td>33</td><td>Starts early Jun-26; full ramp by end-Oct 2026</td></tr><tr><td>Tsingshan</td><td>Weda Bay Industrial Park</td><td>Maluku</td><td></td><td></td><td>37</td><td>80</td><td>80</td><td>Phase 1: 0.4mt (early 2027); Phase 2: 0.4mt (2028)</td></tr><tr><td>Nanshan A/H</td><td>Bintan Nanshan</td><td>Riau Islands</td><td></td><td>3</td><td>24</td><td>50</td><td>100</td><td>A: 0.125mt (end-26), 0.125mt (27); H: 0.25mt (27–28), 0.5mt (post-28)</td></tr><tr><td>Inalum</td><td>Inalum</td><td>North Sumatra</td><td>28</td><td>28</td><td>28</td><td>28</td><td>90</td><td>Remaining 0.6mt post-2029; likely delayed to 2032</td></tr><tr><td>Adaro / Lygend</td><td>PT KAI</td><td>North Kalimantan</td><td></td><td>37</td><td>50</td><td>50</td><td>150</td><td>0.425mt in 26; ~0.3mt sales potentially delayed (no tax-exempt status)</td></tr><tr><td>Harita / Weiqiao</td><td>PT DIB</td><td>North Kalimantan</td><td></td><td></td><td>12</td><td>75</td><td>100</td><td>Two phases: 0.5mt (2H27), 0.5mt (28)</td></tr><tr><td>Bosai</td><td>PT Bosai</td><td>East Java</td><td></td><td></td><td></td><td>60</td><td>60</td><td>Two phases: 0.3mt (4Q27), 0.3mt (2028)</td></tr><tr><td>East Hope</td><td>PT WAI</td><td>West Kalimantan</td><td></td><td></td><td></td><td></td><td>240</td><td>No land/power; 28–29 unlikely start, excluded from the total number</td></tr><tr><td>Total</td><td></td><td></td><td>88</td><td>194</td><td>377</td><td>573</td><td>810</td><td></td></tr><tr><td>New production</td><td></td><td></td><td>23</td><td>107</td><td>183</td><td>196</td><td>238</td><td></td></tr><tr><td>Potential Inventory</td><td></td><td></td><td>10</td><td>30</td><td></td><td></td><td></td><td></td></tr><tr><td>Potential Sales</td><td></td><td></td><td></td><td>87</td><td></td><td></td><td></td><td></td></tr></table>

Source: Aladdiny, UBS

# Valuation Method and Risk Statement

Aluminium sector - Downside risks include: 1) worsened property construction; 2) less-than-expected solar/wind installation; 3) declining home appliance export order; 4) State Grid and Southern Grid capex missed. Upside risks include: 1) improved property construction, 2) better-than-expected solar/wind installation, 3) State Grid and Southern Grid capex beat, 4) home appliance shipments beat.

# Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 04 June 2026 04:47 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

# Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions 

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>54%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 31 March 2026.   
1: Percentage of companies under coverage globally within the 12-month rating category.   
2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE): Exceptions to the standard +/-6% bands may be granted by the Investment Review Consultation (IRC). Factors considered by the IRC include the stock's volatility and the credit spread of the respective company's debt. As a result, stocks deemed to be very high or low risk may be subject to higher or lower bands as they relate to the rating. When such exceptions apply, they will be identified in the Company Disclosures table in the relevant research piece.

Research analysts contributing to this report who are employed by any non-US affiliate of UBS LLC are not registered/qualified as research analysts with FINRA. Such analysts may not be associated persons of UBS LLC and therefore are not subject to the FINRA restrictions on communications with a subject company, public appearances, and trading securities held by a research analyst account. The name of each affiliate and analyst employed by that affiliate contributing to this report, if any, follows.

UBS AG Hong Kong Branch: Beili Wang, Elvis Liu, Sharon Ding.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies discussed in this report, including information on valuation and risk, please contact UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research.

# The Disclaimer relevant to Global Wealth Management clients follows the Global Research Disclaimer. The Disclaimer relevant to CS Wealth Management follows the Global Wealth Management Disclaimer.

# UBS Global Research Disclaimer

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

Any opinions expressed in this document may change without notice and are only current as of the date of publication. Different areas, groups, and personnel within UBS may produce and distribute separate research products independently of each other. For example, research publications from UBS CIO are produced by UBS Global Wealth Management. UBS Global Research is produced by UBS Investment Bank. Research methodologies and rating systems of each separate research organization may differ, for example, in terms of investment recommendations, investment horizon, model assumptions, and valuation methods. As a consequence, except for certain economic forecasts (for which UBS CIO and UBS Global Research may collaborate), investment recommendations, ratings, price targets, and valuations provided by each of the separate research organizations may be different, or inconsistent. You should refer to each relevant research product for the details as to thei

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/f5433cdaecc112955483d87e232d5bdfcb9c0388357c9bfcf8a2e4773d622f90.jpg)
"""
