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
First Read

# China PCB Sector

# Our initial read on potential Kyber backplane delay and sector updates

## Kyber orthogonal backplane delay in-line with our expectation

Recent press noted NVDA Kyber rack architecture is facing delays to 2028 due to supply chain challenges on PCB backplane. We view this timeline as in-line with our expectation based on our early industry study from upstream CCL vendors back in May, suggesting potential delays of orthogonal backplane to Feynman in 2028. This was corroborated by Victory Giant mentioned in our H-share Corp Day (link) that there are currently 10+ material/vendor combinations being considered including different layer count designs. We see potential challenges are: 1) M9+Q-glass' processing difficulties, inadequate supply and higher costs vs. other possible solutions (e.g. with low-dk2); we believe this option is on hold for the Kyber backplane despite multiple rounds of trials; 2) PTFE's unexpected emergence as an optimal alternative due to its outstanding performance and improving yield, despite time required for supply chain readiness with further testing and; 3) suboptimal yields on the PCB side as both Q-glass and PTFE materials demand much higher manufacturing capability on a 100+ layer form factor. We think the impact on PCB companies earnings in 2026/27E could be limited as Kyber was originally expected in late 2027 on Rubin Ultra with relatively small volume, and despite a slightly later timeline, we believe it's not cancelled altogether. Also see our Taiwan analyst Diana Chang's latest reads on Kyber, substrate pricing, and T-glass supply here (link).

## Conventional CCL price hikes accelerate, BT substrate pricing resilient

KBL announced another round of 15% conventional FR4 CCL price hike today, shortly after 2 rounds of hikes in June at 15% and 10%, respectively. We are optimistic on conventional CCL names benefiting from aggressive price hikes with margins expanding and we see current pricing above the previous upcycle peak at c.Rmb220/sheet. We expect this upcycle to be sustainable and forecast monthly hike cadence continuing through 2H26 into 1H27 primarily driven by AI crowding out conventional supply with limited near-term capacity addition. On BT substrate, despite news reported Korean memory makers are pushing for substrate price cuts into H226, our checks with China BT substrate makers (Shennan and FastPrint) indicate no such thing and we expect H226 pricing would be favourable with UTR at very high levels.

## mSAP capacity expansions underway for optical transceiver demand

We see PCB makers are adding mSAP capacity on the back of rising 1.6T/3.2T optical module demand. Avary announced on 3 July to raise up to Rmb9.6bn toward its Huai'an plant, adding 655.6k sqm of annual high-end HDI capacity for AI servers and optical modules. FastPrint's placement plan (23 June) would raise up to Rmb3.9bn, with Rmb2bn for a Zhuhai high-end mSAP plant, adding 120k sqm per year for optical module PCB over a two-year build. Victory Giant is investing c.Rmb1bn on mSAP production lines in Plant 4 with further mSAP capacity expansions in Plant 12/13 dedicated for optical modules at its key customer, mentioned in our H-share Corp Day.

## Prefer upstream/CCL; selective on PCB with diversified AI exposure + share gain

We reiterate our near-term preference on upstream CCL players over downstream PCB. Within PCB names we are selective on players with more diversified AI customer exposure (e.g. ASIC) and with share gain potential into NVDA chain. At current valuation for the PCB sector, especially post numerous stock outperformance over the past 6 months driven by Kyber adoption, we believe some investors could turn more conservative towards how much incremental TAM Kyber could bring and thus discount the earning growth after 2027. For now, we still look toward a 2028-launch timeline for the Kyber backplane and expect the PTFE-M9 hybrid as a prime option.

Equities

China

Communications Technology

Jimmy Yu

Analyst

jimmy.yu@ubs.com

+86-21-3866 8880

Edward Liu

Analyst

edward.liu@ubs.com

+852-3712 3981

David Chow

Associate Analyst

david.chow@ubs.com

+852-3712 3512

## Valuation Method and Risk Statement

We value FastPrint Circuit using the sum-of-the-parts method, in which both the core business and the new ABF business valuations are PE-based. Upside risks to our current valuation include: 1) ABF capacity orders faster than expected; and 2) core PCB business recovery faster than expected. Downside risks to our current valuation include: 1) ramp-up of new ABF capacities is slower than expected; and 2) core PCB business recovery does not outperform the China PCB market.

We value Shennan Circuit using the sum-of-the-parts method, in which both the core business and the new ABF business valuations are PE-based: we derive the core business valuation using 22x 2024E PE and apply 30x 2027E PE to the new ABF business. Downside risks: 1) slower-than-expected server demand pick up in China and the rest of the world; 2) stronger-than-expected pricing pressure from clients and intensifying competition; and 3) longer time to breakeven for ABF business.

Our valuation of Avary is based on target PE methodology. Upside risks: 1) faster FPC/SLP adoption in the Android camp; 2) earlier launches of new AR/VR headsets or devices equipped with mini-LED displays; 3) meaningful orders from auto-related business. Downside risks: 1) more severe ASP cuts in existing FPC parts; 2) underwhelming iPhone shipment numbers; 3) lacklustre demand for AR/VR products and limited application of mini-LED on new devices; 4) unfavourable FX changes.

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 06 July 2026 02:00 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>55%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 30 June 2026.  
1: Percentage of companies under coverage globally within the 12-month rating category.

2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE): Exceptions to the standard +/-6% bands may be granted by the Investment Review Consultation (IRC). Factors considered by the IRC include the stock's volatility and the credit spread of the respective company's debt. As a result, stocks deemed to be very high or low risk may be subject to higher or lower bands as they relate to the rating. When such exceptions apply, they will be identified in the Company Disclosures table in the relevant research piece.

Research analysts contributing to this report who are employed by any non-US affiliate of UBS LLC are not registered/qualified as research analysts with FINRA. Such analysts may not be associated persons of UBS LLC and therefore are not subject to the FINRA restrictions on communications with a subject company, public appearances, and trading securities held by a research analyst account. The name of each affiliate and analyst employed by that affiliate contributing to this report, if any, follows.
UBS AG Hong Kong Branch: David Chow, Edward Liu. UBS Co. Limited: Jimmy Yu.

Company Disclosures

<table><tr><td>Company Name</td><td>Reuters</td><td>12-month rating</td><td>Price</td><td>Price date</td></tr><tr><td>Avary Holding Shenzhen</td><td>002938.SZ</td><td>Neutral</td><td>Rmb95.29</td><td>06 Jul 2026</td></tr><tr><td>Shennan Circuits</td><td>002916.SZ</td><td>Buy (UR)</td><td>Rmb440.20</td><td>06 Jul 2026</td></tr><tr><td>Shenzhen FastPrint Circuit</td><td>002436.SZ</td><td>Neutral</td><td>Rmb45.29</td><td>06 Jul 2026</td></tr></table>

Source: UBS Global Research; LSEG Eikon. All prices as of local market close. Ratings in this table are the most current published ratings prior to this report. They may be more recent than the stock pricing date.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies discussed in this report, including information on valuation and risk, please contact UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research.

Shenzhen FastPrint Circuit (Rmb)  
![](images/354f915f5377d27504fa178368fc95e8fe65d6c8e918b786c47a3eaec9a0ff8f.jpg)

<table><tr><td>Date</td><td>Stock Price (Rmb)</td><td>Price Target (Rmb)</td><td>Rating</td></tr><tr><td>2023-04-06</td><td>13.74</td><td>-</td><td>No Rating</td></tr><tr><td>2023-11-21</td><td>16.22</td><td>19.50</td><td>Buy</td></tr><tr><td>2025-08-07</td><td>16.52</td><td>18.00</td><td>Neutral</td></tr><tr><td>2025-10-22</td><td>19.67</td><td>21.00</td><td>Neutral</td></tr><tr><td>2025-10-30</td><td>21.22</td><td>23.00</td><td>Neutral</td></tr><tr><td>2026-03-13</td><td>23.94</td><td>26.00</td><td>Neutral</td></tr></table>

Source: UBS Global Research; LSEG Eikon as of 06-Jul-2026. All prices as of local market close. Ratings as of date shown.

![](images/330f41b9f91209bf8b49dd4ca32b13182140f2fdb75118d08576b37c18593548.jpg)

<table><tr><td>Date</td><td>Stock Price (Rmb)</td><td>Price Target (Rmb)</td><td>Rating</td></tr><tr><td>2023-04-06</td><td>31.99</td><td>30.00</td><td>Neutral</td></tr><tr><td>2023-05-15</td><td>22.94</td><td>23.00</td><td>Neutral</td></tr><tr><td>2024-03-12</td><td>22.15</td><td>24.00</td><td>Neutral</td></tr><tr><td>2024-08-28</td><td>33.61</td><td>35.00</td><td>Neutral</td></tr><tr><td>2025-08-07</td><td>48.52</td><td>51.60</td><td>Neutral</td></tr><tr><td>2025-10-22</td><td>52.05</td><td>52.50</td><td>Neutral</td></tr><tr><td>2026-03-13</td><td>51.13</td><td>55.00</td><td>Neutral</td></tr></table>

Source: UBS Global Research; LSEG Eikon as of 06-Jul-2026. All prices as of local market close. Ratings as of date shown.

Shennan Circuits (Rmb)  
![](images/d199c7e2be0bb4f1c5672185dda1d01199939afae4bd12e2058ddc3467c719a4.jpg)

<table><tr><td>Date</td><td>Stock Price (Rmb)</td><td>Price Target (Rmb)</td><td>Rating</td></tr><tr><td>2023-04-06</td><td>96.80</td><td>123.00</td><td>Buy</td></tr><tr><td>2023-11-21</td><td>75.37</td><td>92.00</td><td>Buy</td></tr><tr><td>2024-03-18</td><td>91.75</td><td>100.00</td><td>Buy</td></tr><tr><td>2024-07-25</td><td>110.24</td><td>-</td><td>No Rating</td></tr><tr><td>2024-08-29</td><td>99.38</td><td>100.00</td><td>Buy</td></tr><tr><td>2024-09-11</td><td>92.08</td><td>-</td><td>No Rating</td></tr><tr><td>2024-09-23</td><td>87.79</td><td>100.00</td><td>Buy</td></tr><tr><td>2024-11-01</td><td>101.56</td><td>-</td><td>No Rating</td></tr><tr><td>2024-11-22</td><td>98.50</td><td>100.00</td><td>Buy</td></tr><tr><td>2025-01-14</td><td>128.00</td><td>-</td><td>No Rating</td></tr><tr><td>2025-05-29</td><td>85.03</td><td>100.00</td><td>Buy</td></tr><tr><td>2025-07-24</td><td>132.41</td><

[中间内容因长度限制已省略]

 is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
