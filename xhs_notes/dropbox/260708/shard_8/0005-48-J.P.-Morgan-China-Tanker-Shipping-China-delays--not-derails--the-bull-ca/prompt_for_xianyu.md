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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## China Tanker Shipping

China delays, not derails, the bull case

We reiterate our Overweight rating on Cosco Shipping Energy (CSET) H/A and continue to recommend buying on dips. CSET H/A shares corrected 14%/13% this week, underperforming the HSI (+3%) and CSI 300 (-1%), as VLCC freight continued to normalize following the reopening of the Strait of Hormuz. While rates have pulled back from recent peaks, they remain well above historical averages and total tanker traffic has recovered to only 44% of pre-conflict levels (10-day moving average), suggesting physical market normalization remains incomplete. We believe the recent freight correction reflects a temporary mismatch between recovering Gulf exports and Chinese crude demand rather than a deterioration in tanker fundamentals. The JPM Commodities research team highlights this as the key near-term debate, but its base case still expects Chinese crude imports to recover through 2H26. We therefore remain constructive on the medium-term tanker outlook while monitoring the pace of China's demand recovery.

\- Freight rates continue to normalize but remain historically elevated: VLCC rates softened further this week, with TD3C (Hormuz–China) declining 32% WoW to US\$285k/day and TD2 (Hormuz–Singapore) falling 42% WoW to US\$315k/day. Atlantic Basin routes also moderated, with TD15 (West Africa–China) easing 27% WoW to US\$129k/day and TD22 (US Gulf–China) by 22% to US\$118k/day. Despite the correction, all major VLCC routes remain 1.7-7x above pre-conflict and medium-term historical averages (since 2024), indicating freight markets remain fundamentally healthy.

\- Hormuz reopening remains gradual: Total tanker transits through the Strait of Hormuz have recovered to 44% of pre-conflict levels (in terms of barrel capacity) based on the 10-day moving average, with crude tanker transits reaching 48% and product tanker transits 26%. While vessel movements continue to improve, traffic remains well below historical levels, suggesting Gulf export logistics are still normalizing and additional shipping capacity has yet to fully return.

\- China has become the key freight debate: JPM's Commodities research team argues that China absorbed much of the conflict's supply disruption by reducing crude imports and drawing inventories. As Hormuz reopens and Gulf exports recover, returning barrels are temporarily outpacing Chinese demand, creating a near-term surplus that may explain why both crude prices and tanker freight have softened more quickly than expected. However, the team still expects Chinese imports to gradually recover through 2H26 as lower Middle East official selling prices, improving refinery margins, and strategic petroleum reserve replenishment support incremental buying.

\- Our view remains constructive: We believe the current freight weakness reflects a timing mismatch rather than a structural deterioration in tanker fundamentals. The key catalyst from here should be a recovery in Chinese crude imports, which is likely to coincide with a further normalization of Gulf exports. As inventories are rebuilt and seaborne crude trade gradually recovers, we expect freight to remain structurally above historical averages despite near-term volatility.

See page 6 for analyst certification and important disclosures, including non-US analyst disclosures.

Infrastructure, Industrials & Transport

Beatrice Lam AC

(852) 2800-8738

beatrice.lam@JPM.com

Karen Li, CFA

(852) 2800-8589

karen.yy.li@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

\- Key risks: A more prolonged slowdown in Chinese crude imports or weaker-than-expected refinery runs could delay the recovery in VLCC freight despite improving Gulf exports. Conversely, faster strategic petroleum reserve purchases, stronger Chinese refinery demand, or a quicker rebound in crude imports would support both freight rates and tanker equities.

Figure 1: VLCC spot earnings: BDTI TD15-TCE: 260,000t West Africa – China, \$/day  
![](images/5e8be69195dc1752ee77c10dcfcb1a19602f67b354308ac1edbd342aea3b2f72.jpg)  
Source: Clarksons Research

Figure 2: VLCC spot earnings: BDTI TD22-TCE: 270,000mt, USG – China, \$/day  
![](images/3732f6ba6bdd00a835c355bd42b27a1381f77825819e24a1b322253a010ba2a5.jpg)  
Source: Clarksons Research

Figure 3: VLCC spot earnings, BDTI TD2-TCE: 270,000mt, Middle East Gulf to Singapore, \$/day  
![](images/ed9b3b1e6de4ec4157368b05eef7b150cba3c5a20314f627afc589f4544a4b09.jpg)  
Source: Clarksons Research

Figure 4: VLCC spot earnings: BDTI TD3C-TCE: 270,000t Middle East Gulf to China, \$/day  
![](images/eff7575b067e01c423850067c1014e076954c1a2819567c40bd55c307231f7b7.jpg)  
Source: Clarksons Research

Figure 5: Hormuz oil (crude+product) tanker transits continue gradual recovery  
![](images/68f1604599b8005cf45eafe3b3c5623064fa518e72744fac965d650fd86ae50a.jpg)  
Source: Clarksons Research

## Other relevant reports:

\- COSCO Shipping Energy Transport (1138.HK/600026.SH): Tight effective balance supports 2026 earnings; risks shift into 2027; buy CSET-H on dips (19 Dec 2025)

\- China Tanker Shipping: Venezuelan flow displacement and Hormuz risk reprice tanker freight — reaffirming a strong 2026 outlook (17 Jan 2026)

\- China Tanker Shipping: VLCC rate swings and equity volatility amid Iran headlines – what is priced in? (2 Feb 2026)

\- China Tanker Shipping: What to make of the YTD tanker TCE and equity frenzy? And will India and China revert to old habits? (24 Feb 2026)

\- China Tanker Shipping: Iran conflict: \~50% of seaborne oil exposed – immediate tanker tightening, duration decides outcome (2 Mar 2026)

\- COSCO Shipping Energy Transport (1138.HK/600026.SH): Takeaways from fireside chat (27 February): Sinokor, sanctions and Iran (3 Mar 2026)

\- COSCO Shipping Energy Transport (1138.HK/600026.SH): Black swans compound: Iran, compliant tightening and market consolidation reset VLCC earnings power; lift CSET-H/A PTs and upgrade CSET-A to OW (3 Mar 2026)

\- China Tanker Shipping: Hormuz disruption monitor — Week 1.0: Freight explodes as oil flows pause (10 Mar 2026)

\- China Tanker Shipping: Expert call takeaways: Hormuz disruption – tighter fleet, longer voyages, slower normalization (11 Mar 2026)

\- China Tanker Shipping: Hormuz disruption monitor – Week 2.0: freight moderates from extreme highs but structural tightness remains (16 Mar 2026)

\- China Tanker Shipping: Hormuz disruption monitor – Week 2.7: demand is absorbing the cost shock, supporting sustained strength in tanker earnings (20 Mar 2026)

\- China Tanker Shipping: Hormuz disruption monitor – week 3.0: The market is underestimating how structural this oil trade disruption has become (23 Mar 2026)

\- COSCO Shipping Energy Transport (1138.HK/600026.SH): 4Q25 earnings miss on impairments; core in-line as Hormuz-driven earnings upside remains intact (27 Mar 2026)

\- COSCO Shipping Energy Transport (1138.HK/600026.SH): Post-4Q25-results briefing takeaways — safety removes supply, rates broaden beyond VLCCs (27 Mar 2026)

\- China Tanker Shipping: Hormuz disruption monitor – week 4.0: Consolidation strengthening, supply constrained – Buy Cosco Shipping Energy Transport on earnings capture (30 Mar 2026)

\- China Tanker Shipping: Hormuz disruption monitor – week 5.0: Fewer VLCCs are heading to Saudi — zero CSET participation signals preemptive withdrawal, not de-escalation (6 Apr 2026)

\- China Tanker Shipping: Ceasefire is a reprieve, not a resolution — tanker shipping upside persists across scenarios, magnitude vs base case varies (8 Apr 2026)

\- China Tanker Shipping: Hormuz disruption monitor – week 6: Too eventful for Easter — from ceasefire to blockade in one week (13 Apr 2026)

\- China Tanker Shipping: Hormuz disruption monitor – week 7: not crowded, still tight — tanker markets under selective participation (19 Apr 2026)

\- China Tanker Shipping: Hormuz disruption monitor – week 8: Hormuz closure persists — lag phase masks underlying tightening (27 Apr 2026)

\- China Tanker Shipping: UAE abandons quotas — tankers to gain incremental barrels, post-Hormuz reopening (29 Apr 2026)

\- China Tanker Shipping: Hormuz disruption monitor – week 9: panic fades, rates ease — optionality builds (4 May 2026)

\- China Tanker Shipping: Hormuz disruption monitor - week 10: The next move depends on whether oil demand holds up (11 May 2026)

\- China Tanker Shipping: Hormuz disruption monitor - week 11: CSET recovers as shadow fleet risks build (19 May 2026)

\- China Tanker Shipping: Global China Summit Takeaways: CMES sees post-Hormuz-reopening VLCC TCE at US\$130-150k/day (21 May 2026)

\- China Tanker Shipping: Hormuz reopening back on the table; time to revisit CSET (15 June 2026)

Companies Discussed in This Report (all prices in this report as of market close on 03 July 2026, unless otherwise indicated) COSCO Shipping Energy Transport - A(600026.SS/Rmb17.37/OW), COSCO Shipping Energy Transport - H(1138.HK/HK \$14.55/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to COSCO Shipping Energy Transport - A, COSCO Shipping Energy Transport - H or related entities.

\- Market Maker/ Liquidity Provider (Hong Kong): JPM Securities (Asia Pacific) Limited and/or JPM Broking (Hong Kong) Limited and/or an affiliate is a market maker and/or liquidity provider in the securities of COSCO Shipping Energy Transport - A, COSCO Shipping Energy Transport - H or related entities and/or warrants or options thereon, which are listed or traded on The Stock Exchange of Hong Kong Limited.

\- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of COSCO Shipping Energy Transport - A, COSCO Shipping Energy Transport - H or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: COSCO Shipping Energy Transport - A, COSCO Shipping Energy Transport - H or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: COSCO Shipping Energy Transport - A, COSCO Shipping Energy Transport - H or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from COSCO Shipping Energy Transport - A, COSCO Shipping Energy Transport - H or related entities.

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from COSCO Shipping Energy Transport - A, COSCO Shipping Energy Transport - H or related entities.

\- Debt Position: JPM may hold a position in the debt securities of COSCO Shipping Energy Transport - A, COSCO Shipping Energy Transport - H or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

COSCO Shipping Energy Transport - A (600026.SS, 600026 CH) Price  
![](images/799ba158168b4a5e0662f4031d8e99bfa0eedd08b281356a9cb87034f6958ed9.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>23-Apr-24</td><td>N</td><td>16.51</td><td>18</td></tr><tr><td>26-Jul-24</td><td>N</td><td>14.76</td><td>16</td></tr><tr><td>31-Oct-24</td><td>N</td><td>13.19</td><td>13</td></tr><tr><td>23-Sep-25</td><td>N</td><td>12.23</td><td>13</td></tr><tr><td>31-Oct-25</td><td>N</td><td>13.53</td><td>14</td></tr><tr><td>19-Dec-25</td><td>N</td><td>11.85</td><td>13</td></tr><tr><td>03-Mar-26</td><td>OW</td><td>22.64</td><td>28</td></tr><tr><td>27-Mar-26</td><td>OW</td><td>23.90</td><td>30</td></tr><tr><td>28-Apr-26</td><td>OW</td><td>21.50</td><td>32</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Apr 23, 2024. All share prices are as of market close on the previous business day. Break in coverage Jan 17, 2025 - Sep 22, 2025.

COSCO Shipping Energy Transport - H (1138.HK, 1138 HK) Price Chart  
![](images/18356661d09179eee6b0b4335adbc43128dd583ff76f13a341b4ced118f9fdf2.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target (HK$)</td></tr><tr><td>23-Apr-24</td><td>OW</td><td>8.70</td><td>12</td></tr><tr><td>31-Oct-24</td><td>OW</td><td>7.57</td><td>10</td></tr><tr><td>23-Sep-25</td><td>OW</td><td>9.20</td><td>12</td></tr><tr><td>31-Oct-25</td><td>OW</td><td>11.22</td><td>13</td></tr><tr><td>19-Dec-25</td><td>OW</td><td>9.92</td><td>12</td></tr><tr><td>03-Mar-26</td><td>OW</td><td>20.50</td><td>24</td></tr><tr><td>27-Mar-26</td><td>OW</td><td>19.42</td><td>26</td></tr><tr><td>28-Apr-26</td><td>OW</td><td>17.73</td><td>27</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends.  
Break in coverage Jan 17, 2025 - Sep 22, 2025.

The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period. JPM ratings or designations: OW = Overweight, N= Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the sto

[中间内容因长度限制已省略]

ever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is

Completed 03 Jul 2026 09:23 PM HKT
"""
