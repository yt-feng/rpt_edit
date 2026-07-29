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
# US IT Services

All Eyes on Outlook

## CITI'S TAKE

Valuations across the IT Services space have materially come in following instances of slipped bookings, more delayed decision making, and continued pricing pressure due to GenAI, but we believe that 2Q organic revenue growth should be in-line with guidance for the digital engineering focused players EPAM and GLOB. Thematically, discretionary spend has yet to unlock and AI has yet to drive any noticeable acceleration (mostly pressure), with 2H26 outlooks now in focus and investors wondering how much needs to be cut on the annual guidance. As for the FY26 Y/Y organic CC revenue growth guidance ranges, we estimate EPAM to slightly cut to 2-4% (vs 2.5-5% prior) and for GLOB to slightly cut to -0.7-1.2% (vs 0.3-2.2% prior). We remain Neutral on EPAM (reports 8/6), trimming our PT to \$100, and Neutral/HR on GLOB (estimated to report 8/13), trimming our PT to \$37, both due to falling peer multiples.

Short Duration Discretionary Demand Must Overcome Unfavorable Near Term Operating Environment. Thematically, EPAM and GLOB are both major digital engineering focused IT services providers that in our view should be approaching their respective troughs in near term revenue growth rates. Guidance from both companies suggest a 2H acceleration over 1H performance, but we think that more evidence of stability will need to surface before valuation multiples can expand to more normalized levels.

Bryan Keane $^{AC}$ +1415-658-4236
bryan.keane@citi.com

William Tang
+1-212-816-8743
william1.tang@citi.com

Adam Butler, CFA

+1-212-816-5181

adam.butler@citi.com

Payments, Processors & IT Services

<table><tr><td rowspan="2" colspan="14"></td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td><td></td></tr><tr><td colspan="2">EPS</td><td colspan="2">EPS</td><td></td></tr><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td rowspan="2">ESPR (%)</td><td rowspan="2">Div Yld (%)</td><td rowspan="2">ETR (%)</td><td rowspan="2">Last Rpt Yr</td><td rowspan="2">Old</td><td rowspan="2">New</td><td rowspan="2">Old</td><td rowspan="2">New</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td></tr><tr><td>EPAM Systems, Inc.</td><td>EPAM</td><td>US$</td><td>89.85</td><td>4,694</td><td>24 Jul 16:00</td><td>2</td><td>nc</td><td>-</td><td>112.00</td><td>100.00</td><td>11.3</td><td>0.0</td><td>11.3</td><td>Dec-25</td><td>13.05</td><td>nc</td><td>14.50</td><td>nc</td></tr><tr><td>Globant SA</td><td>GLOB</td><td>US$</td><td>31.30</td><td>1,352</td><td>24 Jul 16:00</td><td>2H</td><td>nc</td><td>-</td><td>42.00</td><td>37.00</td><td>18.2</td><td>0.0</td><td>18.2</td><td>Dec-25</td><td>6.21</td><td>nc</td><td>6.63</td><td>nc</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High Risk</td><td colspan="13">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change</td></tr><tr><td colspan="6">Source: Citi</td><td colspan="13">^Catalyst Watch</td></tr></table>

Earnings Estimates

<table><tr><td colspan="4"></td><td colspan="5">Last Reported Year</td><td colspan="5">Current Fiscal Year</td><td colspan="5">Next Fiscal Year</td></tr><tr><td>Company Name</td><td>Ticker</td><td>Last Rpt Year</td><td>Currency</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY0</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY1</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY2</td></tr><tr><td>EPAM Systems, Inc.</td><td>EPAM</td><td>Dec-25</td><td>US$</td><td>2.41</td><td>2.77</td><td>3.08</td><td>3.26</td><td>11.50</td><td>2.86</td><td>3.15</td><td>3.45</td><td>3.59</td><td>13.05</td><td>3.20</td><td>3.44</td><td>3.92</td><td>3.95</td><td>14.50</td></tr><tr><td>Globant SA</td><td>GLOB</td><td>Dec-25</td><td>US$</td><td>1.50</td><td>1.53</td><td>1.53</td><td>1.54</td><td>6.13</td><td>1.50</td><td>1.51</td><td>1.58</td><td>1.62</td><td>6.21</td><td>1.51</td><td>1.62</td><td>1.72</td><td>1.78</td><td>6.63</td></tr><tr><td colspan="19">Source: Citi</td></tr></table>

EPAM: Unexpected Exogenous Headwinds Continue to Mute ‘26 Growth. EPAM entered YE25 anticipating that organic growth could accelerate in 2026 vs in 2025, but encountered material unexpected headwinds that continue to impact the business. For example, on the 4Q25 earnings call, EPAM announced that NEORIS’s largest client (headquartered in Mexico) decided to pull back on IT services spend at least in part due to challenges created by the impact of US tariffs. By the 1Q26 earnings call (ie across April and early May), EPAM began seeing increased delays in client decision making due to turmoil in the Middle East, and so consequently reduced the annual growth guide. We believe that while EPAM remains a valuable and differentiated services provider, the company needs to either demonstrate it can take share faster (and therefore overcome the various macro headwinds) or provide evidence that go-forward demand realization can improve (eg via accelerating TCV bookings growth or improving existing customer sentiment in decision making).

\- We note that given 1Q26 organic CC growth of $3.7\%$ Y/Y, and 2Q's guide of $2.7\%$ at the midpoint, 2H26 revenues need to rise $4.4\%$ to hit the midpoint of the FY26 guide, suggesting 2H acceleration. We believe that constructive commentary from the company at 2Q earnings should help support a near term floor for valuation, but anticipate that investors will wait until 3Q earnings before leaning either way with more conviction.

GLOB: Large Accounts Resilient Above the Rest. While GLOB's Data & AI digital studio continues to see strong revenue growth (25%+ in 1Q26) relative to the consolidated business, the company's critical Engineering studio is growing only MSD. Looking at revenue growth by client sizing in 1Q26, the top 50 powered revenue growth of 5.2%, the top 10 powered growth of 4%, and the top 2 to 5 cohort powered growth of 8.2%. We infer then that many of GLOB's smaller and arguably newer clients are likely demonstrating continued reservation regarding an unlocking of discretionary spend. For the time being then, we believe that GLOB may find the operating environment to be particularly difficult as it relates to making progress towards the company's longer term “100 squared” objective.

\- Having grown revenues $-2.7\%$ Y/Y organic CC in 1Q26, and guiding for 2Q and annual performance of $-1.2\%$ and $1.2\%$ respectively, at the midpoint, we calculate that 2H revenue growth is implied to accelerate to $4.3\%$ . We believe part of the sharp sequential increase in growth rate stems from easier Y/Y comps (4Q25 growth was $-6.5\%$ ), but new large deals that have already been signed should begin to bill as well. Finally, GLOB's AI Pods initiative should modestly add to consolidated growth too as TCV scales there.

Revenue per Headcount Rising: Going Offensive with Newfound Capabilities. As the industry increasingly shifts to outcome based delivery and emphasizes AI-native talent to help drive both the demand for automated/autonomous workflows and the rising need for increased internal productivity (from the IT service provider's perspective), we believe that nimble digital engineering organizations like EPAM and GLOB should be best positioned to capitalize on the changing economics and contractual models of the space.

■ EPAM: Focused on Recruiting AI-Native Talent, Driving Stronger Effective Bill Rates. We believe that AI-led productivity and an increased prevalence of fixed price type contracts (rising consistently from 15.1% of revenues in 1Q24 to 21.7% in 1Q26) has supported positive revenue per headcount growth for 4 consecutive quarters at EPAM. Operationally, while industry level like-for-like AI-driven pricing pressure acts as a headwind, engineers who effectively utilize GenAI for fulfillment are able to complete more projects in a given amount of time, thus driving stronger revenue per headcount metrics, in our view. Given that EPAM stands at total headcount of \~63K globally, we think that the modest size (especially relative to several major peers) combined with a strong heritage of engineering excellence should allow the company to adapt quickly in the changing landscape.

GLOB: Sustained Rising Revenue per Headcount Supports Medium Term Growth Acceleration. GLOB has been able to sustain its recent growth in revenue per employee (up 8% Y/Y in 1Q26; \~\$90K) for 4 consecutive quarters, partly because of the company's steady but consistent expansion of its AI Pods initiative, in our view. Additionally, we think that the organization's focus on realizing delivery productivity ahead of levels seen at peers gives the company an edge to grow top line faster, all else equal. The rising mix shift to fixed price type contracts (30% in 1Q26 vs \~25% in 1Q24) should also create opportunity for incremental revenue per headcount growth. We believe that if GLOB can continue to take share in the nascent but growing AI-based TAM, the company stands to accelerate growth to more normalized levels medium term, potentially sooner and more aggressively than larger peers.

New TAM To Help Longer Term: Whether AL-Enabled Consolidation Deals or AI-Native Recurring Revenue Implementations.

EPAM: Extending Engineering Excellence into AI-Based Consolidations. While EPAM has a strong legacy in executing on shorter duration, smaller scale projects, we believe that rising customer demand for vendor consolidation of systems on the AI front present an incremental opportunity that EPAM previously didn't have. Specifically, we think that EPAM stands to win share in a new category of multi-year-large deals whose focus is to consolidate AI-based transformation under one vendor.

\- YTD, EPAM has talked about 10 such initial client engagements that the company hopes to win later this year. While EPAM can hit the midpoint of the annual revenue guidance range without winning any of these deals, winning just 1 or 2 should push the company into the higher half. We believe that winning several more should be enough to allow EPAM to approach the higher end of the guided range.

GLOB: AI Pods Creating New Engagement with Customer Accounts. We believe that GLOB is engaging with customers via new channels in order to better monetize the specific opportunities that demand for GenAI technology is creating. For example, the company is leaning into annual recurring revenue (\~\$33 mln in 1Q26) stemming from its AI Pods model, wherein AI-native service units with task and industry expertise bill based on outcomes as opposed to effort (ie using tokens to track client consumption). The “forward deployed” engineers lead the enablement by integrating the AI Pods capability into customer venues/systems, providing onsite execution and support. In particular, GLOB has already incorporated their new AI Pods business model into 40% of their top 20 revenue-generating accounts, up from 30% in 4Q25, with a longer term goal of 70% penetration in that cohort of accounts.

We think that client specific AI-based integration and use cases should be uniquely proprietary vs more traditional IT services work (even when compared to demand in the realm of digital engineering) such that service models must adapt in order to remain competitive. More specifically, we anticipate that a blend of advanced consulting experience and AI-native execution talent must come together, rather than kept separate, in such cases to fully realize GenAI's latent potential to the customer

Figure 1. GLOB's ARR from the AI Pods Model Is Rising Strongly Sequentially  
![](images/b7b0a12533abde2dd6f2ec92c5738703f10867dc46d781a98cc63d03852fc0c5.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, GLOB Company Disclosures

Gross Margins Structurally Supported by Increased AI Efficiencies. While we believe that pricing compression from new/renewed deals should continue to act as a headwind to margins, we think that continued realization of AI-based efficiencies internally at IT services providers can offset, particularly as an increasingly large AI-native talent base begins to more skillfully utilize the new technology and move the needle.

■ EPAM: GM Inflecting Upwards Both Y/Y and Q/Q. EPAM demonstrated Y/Y expansion in adj. gross margins in 1Q26 (+70 bps), driven by what we think is a combination of increased operating focus on improving profitability across critical geos (eg India, Western Central Asia, and Latam), continued success in realizing internal gains via AI adoption, and a lapping of the recent major Neoris acquisition. Although EPAM typically experiences sequential GM strength across the year, driven largely due to seasonality (eg billing days), we think that 2026 should see a rising momentum in Y/Y strength as well, particularly as the foundation for further GM expansion is set for 2027 and beyond (largely due to pyramid recalibration, supported by enhanced utilization, and further AI associated productivity benefits).

\- While disclosures have been more limited, EPAM's AI-native business is delivering profitability above the company's average, and we think that over time, as demand and realization scales, EPAM's margins should begin to feel tailwinds from the favorable mix shift.

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, FactSet, GLOB Company Disclosures

GLOB: GM Weighed by Unfavorable FX, but AI Pods Initiatives Should Provide Longer Term Tailwinds. GLOB sources much of its technical talent from Latam (66% total), with 18% of total heads coming from Argentina; 22% from Colombia; 26% from other Latam; 17% from India; and 17% from North America, Europe, MENA & APAC. In recent times, the Mexican peso, the Colombian peso, and the Brazilian real in particular are seeing Y/Y strengthening relative to the USD, which hurts GLOB's GM profile all else equal, given that operating costs effectively rise. Note that revenues are expected to feel a 100 bps annual tailwind due to weakening of the USD relative to currencies in international markets in which GLOB performs fulfillment (eg Mexico, Colombia, and Brazil).

Figure 2. Stronger Latam Currencies Imply both Revenue Growth Tailwinds and Gross Margin Pressure for GLOB

<table><tr><td></td><td>2Q26 Y/Y Change (XXX/USD)</td></tr><tr><td>MXN</td><td>-10.9%</td></tr><tr><td>COP</td><td>-14.1%</td></tr><tr><td>BRL</td><td>-10.9%</td></tr></table>

\- From a structural perspective, we would emphasize that gross margins in GLOB's AI Pods initiative are materially higher than that of the consolidated company's (disclosed at 45-60% vs consolidated GM at \~38%), and so we would expect longer term tailwinds from the beneficial mix shift that is taking place (AI Pods annual recurring revenue guided to rise \~290% Y/Y at the midpoint (ie \$60-100 mln in ARR in FY26) vs consolidated revenues guided to rise \~0% organic CC in FY26).

2Q26 Preview. We anticipate a largely in-line quarter for both EPAM and GLOB in 2Q. Although we sense that both companies guided with realistic assessments of the unfavorable macro, we believe that the operating environment did not materially improve in 2Q to effect notable outperformance.

■ EPAM. For EPAM, we model organic CC Y/Y revenue growth of 2.7%, Adj. EBIT margins of 15.4%, and Adj. EPS of \$3.15.

■ GLOB. For GLOB, we model organic CC Y/Y revenue growth of -1.2%, Adj. EBIT margins of 14.4%, and Adj. EPS of \$1.51.

## Guidance Thoughts on FY26:

■ EPAM. We believe that the company will modestly lower the guide for annual organic CC Y/Y revenue growth (2-4% vs 2.5-5% prior), reiterate Adj. EBIT margins (15-16%), and lower the guide for Adj. diluted EPS (\$12.92-\$13.16 vs \$12.98-\$13.28 prior).

■ GLOB. We believe that the company will modestly lower the guide for annual organic CC Y/Y revenue growth (-0.7-1.2% vs 0.3-2.2% prior), reiterate Adj. EBIT margins (14-15%), and lower the guide for Adj. diluted EPS (\$6.04-\$6.44 vs \$6.10-\$6.50 prior)

Figure 3. EPAM: Citi vs Consensus

<table><tr><td rowspan="2"></td><td colspan="5">2Q26</td><td colspan="2">3Q26E</td><td colspan="2">4Q26E</td><td colspan="5">2026E</td></tr><tr><td>Low Outlook</td><td>High Outlook</td><td>Mid Outlook</td><td>Citi Est.</td><td>Cons.</td><td>Citi Est.</td><td>Cons.</td><td>Citi Est.</td><td>Cons.</td><td>Low Outlook</td><td>High Outlook</td><td>Mid Outlook</td><td>Citi Est.</td><td>Cons.</td></tr><tr><td>Revenues</td><td>1,400</td><td>1,415</td><td>1,408</td><td>1,408</td><td>1,407</td><td>1,472</td><td>1,445</td><td>1,485</td><td>1,469</td><td>5,675</td><td>5,812</td><td>5,744</td><td>5,765</td><td>5,722</td></tr><tr><td>Y/Y growth</td><td>3.4%</td><td>4.5%</td><td>4.0%</td><td>4.0%</td><td>4.0%</td><td>5.6%</td><td>3.7%</td><td>5.5%</td><td>4.4%</td><td>4.0%</td><td>6.5%</td><td>5.3%</td><td>5.6%</td><td>4.9%</td></tr><tr><td>FX (headwind)/tailwind</td><td></td><td></td><td></td><td>1.3%</td><td>1.3%</td><td>0.5%</td><td>0.5%</td><td>0.3%</td><td>0.3%</td><td></td><td></td><td></td><td>1.5%</td><td>1.5%</td></tr><tr><td>Inorganic Impact</td><td></td><td></td><td></td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td></td><td></td><td></td><td>0.0%</td><td>0.0%</td></tr><tr><td>Y/Y Organic CC growth</td><td></td><td></td><td>2.7%</td><td>2.7%</td><td>2.7%</td><td>5.1%</td><td>3.2%</td><td>5.2%</td><td>4.1%</td><td>2.5%</td><td>5.0%</td><td>3.8%</td><td>4.1%</td><td>3.4%</td></tr><tr><td>Adj. Gross Profit</td><td></td><td></td><td></td><td>437</td><td>432</td><td>472</td><td>459</td><td>488</td><td>473</td><td></td><td></td><td></td><td>1,808</td><td>1,776</td></tr><tr><td>Adj. GP margin</td><td></td><td></td><td></td><td>31.0%</td><td>30.7%</td><td>32.1%</td><td>31.8%</td><td>32.8%</td><td>32.2%</td><td></td><td></td><td></td><td>31.4%</td><td>31.0%</td></tr><tr><td>Y/Y expansion (bps)</td><td></td><td></td><td></td><td>89 bps</td><td>59 bps</td><td>101 bps</td><td>74 bps</td><td>110 bps</td><td>43 bps</td><td></td><td></td><td>Expansion Y/Y</td><td>91 bps</td><td>58 bps</td></tr><tr><td>Adj. Operating Income</td><td></td><td></td><td>218</td><td>217</td><td>217</td><td>233</td><td>232</td><td>238</td><td>240</td><td></td><td></td><td></td><td>889</td><td>890</td></tr><tr><td>Adj. Operating Margin</td><td>15.0%</td><td>16.0%</td><td>15.5%</td><td>15.4%</td><td>15.4%</td><td>15.8%</td><td>16.1%</td><td>16.0%</td><td>16.4%</td><td

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective

investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
