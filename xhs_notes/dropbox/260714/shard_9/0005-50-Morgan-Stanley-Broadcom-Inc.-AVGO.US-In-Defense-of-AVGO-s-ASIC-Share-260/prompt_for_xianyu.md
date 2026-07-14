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
July 14, 2026 12:30 AM GMT

Broadcom Inc. | North America

# In Defense of AVGO's ASIC Share

MediaTek participation in TPU is real, but we view displacement fears as premature. AVGO should retain majority share, sustain strong AI growth, and remain a core compute winner, close behind NVDA.

## Key Takeaways

We expect AVGO to retain \~80% TPU share over time, contrary to what some supply chain checks are indicating.

■ HBM supply, packaging execution, and scale make rapid Broadcom displacement unlikely.

AVGO remains a core AI winner and close #2 to NVDA, supported by ASIC leadership, networking, and new customer ramps; reiterate OW.

We have been somewhat surprised by AVGO's underperformance YTD, particularly given the continued strength of the company's AI growth trajectory. We think there are a few reasons for the weakness, including investor preference for growthier "bottleneck" stories across the AI semiconductor ecosystem, but the most persistent overhang remains the debate around MediaTek versus Broadcom share on Google TPU. Our view is that MediaTek participation is real, but not disruptive: AVGO should remain the majority TPU supplier over time, with \~80% share, and we see the bearish calls for 50% share or eventual displacement as premature.

Exhibit 1: AVGO and NVDA performance have lagged other AI Semis  
![](images/177830057b65a7bc44f3321b879b700d6328d26983d6097f0f24488cdab70d09.jpg)  
Source: Factset, MS

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Joseph Moore</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joseph.Moore@morganstanley.com</td><td>+1 212 761-7516</td></tr><tr><td colspan="2">Ella Tulchinsky</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ella.Tulchinsky@morganstanley.com</td><td>+1 212 761-2222</td></tr><tr><td colspan="2">Mason Wayne</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Mason.Wayne@morganstanley.com</td><td>+1 212 761-6012</td></tr><tr><td colspan="2">Shane Brett</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Shane.Brett@morganstanley.com</td><td>+1 212 761-1022</td></tr><tr><td colspan="2">Nicole Kozhukhov</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Nicole.Kozhukhov@morganstanley.com</td><td>+1 212 761-1636</td></tr></table>

## Broadcom Inc. (AVGO.O, AVGO US)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$502.00</td></tr><tr><td>Shr price, close (Jul 13, 2026)</td><td>$384.05</td></tr><tr><td>Mkt cap, curr (mm)</td><td>$1,872,628</td></tr><tr><td>52-Week Range</td><td>$495.00-269.58</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>10/25</td><td>10/26e</td><td>10/27e</td><td>10/28e</td></tr><tr><td>ModelWare EPS ($)</td><td>5.39</td><td>9.98</td><td>16.63</td><td>21.48</td></tr><tr><td>P/E</td><td>68.6</td><td>38.5</td><td>23.1</td><td>17.9</td></tr><tr><td>EPS ($)**</td><td>6.82</td><td>11.59</td><td>18.28</td><td>23.19</td></tr><tr><td>EPS ($)§</td><td>6.67</td><td>11.55</td><td>19.22</td><td>25.47</td></tr><tr><td>Div yld (%)</td><td>0.7</td><td>0.7</td><td>0.7</td><td>0.8</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
§ = Consensus data is provided by Refinitiv Estimates
e = MS estimates

<table><tr><td>Quarter</td><td>2025</td><td>2026e Prior</td><td>2026e Current</td><td>2027e Prior</td><td>2027e Current</td></tr><tr><td>Q1</td><td>1.60</td><td>-</td><td>2.05a</td><td>-</td><td>4.14</td></tr><tr><td>Q2</td><td>1.58</td><td>-</td><td>2.44a</td><td>-</td><td>4.28</td></tr><tr><td>Q3</td><td>1.69</td><td>-</td><td>3.24</td><td>-</td><td>4.72</td></tr><tr><td>Q4</td><td>1.95</td><td>-</td><td>3.85</td><td>-</td><td>5.14</td></tr></table>

e = MS estimates, a = Actual Company reported data

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

This debate is somewhat reminiscent of last year's MRVL / Alchip debate, not because the share outcomes are identical, but because the market again appears to be extrapolating new supplier participation into a much more extreme displacement thesis. Marvell did lose meaningful Trainium share, but the view that it would be fully replaced proved too draconian. Similarly, while MediaTek clearly has a role in the TPU ecosystem, we think calls for Broadcom's share to fall to $50\%$ or below, or eventually be fully displaced, are premature.

We agree MediaTek has a role, but disagree with converting that into a disruptive Broadcom share-loss thesis. To be clear, we do not dismiss MediaTek's opportunity. Google is cost conscious, wants supplier optionality, and is developing multiple TPU iterations. The Taiwan supply chain view also raises real points: MediaTek appears to have a credible 3nm TPU opportunity, Google has an incentive to reduce reliance on Broadcom, and advanced packaging constraints create a reason to explore alternatives. Where we disagree is the conversion of those facts into a disruptive share-loss thesis for Broadcom.

Our base case is that Broadcom maintains roughly 80% TPU share over time. We do not agree with the supply-chain framework that implies a rapid move toward Broadcom share loss. This view is consistent with MediaTek's publicly stated long-term strategy of reaching 15-20% share. Said differently, we think MediaTek participation is real, but we believe the market is overstating the amount and pace of Broadcom share loss within TPU. The key debate, in our view, is not whether MediaTek participates, but whether that participation disrupts Broadcom's broader AI ASIC growth trajectory. We do not believe it will, given risk around MediaTek's execution, AVGO's supply advantage, and the overall difficulty of replacing a scaled platform. In addition, AVGO has multiple new ASIC customers ramping in 2H27, which should help support its growth.

Exhibit 2: MS estimate of AVGO XPU GW deployed by customer  
![](images/0055fe4745bcc5dee498285f0e75f3c7578346313df0a504ce7c1801df690005.jpg)  
Source: MS Estimate

One of the primary motivations behind MediaTek adoption appears to be cost reduction, including the ability to procure certain commodity components separately rather than paying Broadcom pass-through revenue. However, we believe some of the hoped-for savings could be challenging to realize, particularly around

HBM. Buying HBM off the shelf is no longer necessarily cost advantaged given how constrained the market has become and how much open-market pricing has moved higher. By contrast, Broadcom has already secured supply under previously agreed contracts, which could make it difficult for a competing solution to achieve the intended cost advantage.

We also think investors should be careful underwriting aggressive MediaTek growth and high 2nm TPU expectations before the packaging path is more clearly de-risked. Our Taiwan semis team still expects MediaTek to secure some CoWoS capacity for 2nm TPU minimum production, with EMIB framed more as a potential 2029 volume and cost unlock “if executed well.” Our latest checks suggest EMIB remains uncertain for the level of complexity Google requires, with substrate capacity a potential bottleneck and CoWoS still viewed as the more reliable fallback. We are not arguing EMIB cannot work, but we think assuming a large 2nm TPU ramp before that path is proven requires too much faith, particularly given the execution risk and the availability of CoWoS as a fallback.

Ultimately, we believe investors are underestimating how difficult it is to replace Broadcom in a scaled TPU platform. This is not simply a question of whether MediaTek can tape out a chip or generate initial revenue. The relevant question is whether the chip can perform reliably at scale, secure constrained memory supply, qualify at the system level, and deploy across large TPU pods without disrupting Google's AI infrastructure roadmap. That is a much higher bar.

We do not expect the MediaTek ramp to disrupt Broadcom's overall ASIC growth trajectory. In fact, we believe multiple new programs ramping in 2H27 should help AVGO remain one of the fastest growers in our coverage. Our current expectation is for AVGO to generate roughly \$120bn of AI revenue in FY27. Within that, we assume TPU, including both Google internal deployment and external opportunities, accounts for roughly 75% of 10GW of AI deployment. Assuming a cost per GW of roughly \$10-12bn, this translates to approximately \$80bn of TPU-related revenue next year.

Exhibit 3: MS estimate for AVGO AI revenue and XPU GW  
![](images/f6a0def5608c63eb0996550a1568611589e911805102aea3efadd4a445e71feb.jpg)  
Source: MS Estimate

Looking into FY28 is still early, but we think it is feasible that AVGO supports at least 15GW of AI deployment. In that scenario, we would expect TPU to decline as a percentage of AI revenue to roughly 60%, not because TPU weakens, but because newer ASIC customers begin to ramp more meaningfully. We would also highlight that Hock sounded incrementally bullish on FY28 during the last earnings call. We think the bias is to the upside, but we are remaining conservative because each new ASIC program has its own execution risk and optionality. That said, there are a lot of credible shots on goal.

MediaTek certainly has a role in this ecosystem, but we push back on the idea that its involvement is structurally disruptive to Broadcom. While MediaTek may take some share, we think that share gain is likely to be modest and additive to a broader TPU market rather than disruptive to Broadcom's growth. Until there is clear evidence that MediaTek can execute at scale, secure the necessary supply chain, and match Broadcom's performance and reliability, we view the bearish share-loss narrative as premature.

How do we reconcile with our Mediatek view? Our Mediatek team lead by Charlie Chan believes that Mediatek can take majority share of TPU over the next couple of years. That is based primarily on a view of supply chain planning, while we take the view that key milestones in chip development are still to be determined; our view is that replacing high functioning TPUs at scale is quite challenging. We also note that our split of the market seems closer to both companies' long-term share view (with AVGO suggesting to us that they can maintain 80%+ of its SAM while Mediatek's longer term goal is 20% share of ASIC). We also note that unit share can be misleading, given the substantially lower prices for the Mediatek part - even our Mediatek unit numbers are closer to 20% revenue share next year. That said, our teams share many of the same inputs and we will continue to test our hypothesis over time.

What would make us wrong? We would become more concerned if MediaTek's silicon proves materially more performant than expected, if Google / MediaTek can secure competitive HBM supply, if EMIB becomes reliable enough to support a scaled 2nm ramp, and if customer deployments move from risk silicon to production faster than historical AI accelerator ramps. Until then, we view MediaTek as a second-source diversification story rather than evidence that Broadcom's TPU position is structurally impaired.

Thoughts on the stock: AVGO remains one of our preferred AI compute names and a close #2 behind NVIDIA, which remains our Top Pick. We view Broadcom as one of the best growth stories in semis, supported by its leadership in custom ASICs, strong networking franchise, increasing AI revenue diversification, and a management team we trust to execute through product transitions. While the MediaTek / TPU debate is a real overhang, we think the market is overstating the risk to Broadcom's growth trajectory and view AVGO as a core AI winner

MS is acting as advisor to Broadcom Inc. ("Broadcom"), in connection with its establishment of the AI XPV Platform with Apollo and Blackstone Credit & Insurance Business as initial anchor investors, as announced on June 9, 2026. Broadcom has agreed to pay fees to MS for its financial services.

Please refer to the notes at the end of the report.

## Risk Reward – Broadcom Inc. (AVGO.O)

Overweight on growth in AI, recovery in core semis, and potential VMW upside.

## PRICE TARGET \$502.00

We value AVGO at 28X CY2027e ModelWare EPS of \$17.92. This is roughly 26x non-GAAP EPS of \$19.59, which is broadly in-line or below their AI peer group.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/4a77bb41ae08c50774ed0a86382210f89e97ee0523b3a5d5140b9cc92e2aab7d.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/0eca4303a185a04b88b2790c470d7b279cd4baef0aa589fe506a22f61a7c8c31.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 13 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## OVERWEIGHT THESIS

■ AVGO has the second largest AI exposure (in absolute dollars) in our coverage and is poised to grow as hyperscale capex increases. We see the company maintaining their premium multiple as networking and ASIC businesses continue to grow.

We expect non-AI semis to have a cyclical rebound late next year after a period of high excess inventory in the networking and storage markets.

■ We expect VMware to successfully integrate into the portfolio and focus operations, cut costs, and drive stable cash flows.

![](images/f184923c999951f7036b38ede96ef9e9d6600f69f20ada9c09d8f17463378999.jpg)

## Risk Reward Themes

New Data Era: Positive
Pricing Power: Positive

View descriptions of Risk Rewards Themes here

## BULL CASE

## \$637.00

## 31X 2027e ModelWare Bull EPS of \$20.55

Revenue growth surprises to the upside and AI revenues grow from ramp of new xPU customers, continued networking strength, and VMware synergies. The stock's valuation multiple expands as investors gain confidence in its AI and M&A strategy.

## BASE CASE

## \$502.00

## 28X 2027e ModelWare Base EPS of \$17.92

Posts strong revenue growth in CY26 CY27 driven by strong AI revenues from xPU and Networking, and software growth.

## BEAR CASE

## \$308.00

## 20X 2027e ModelWare Bear EPS of \$15.40

Revenue growth disappoints and synergies underwhelm. New customer engagements fail to reach production The stock's valuation multiple falls to 31X

## Risk Reward – Broadcom Inc. (AVGO.O)

## KEY EARNINGS INPUTS

<table><tr><td>Drivers</td><td>Oct 2025</td><td>Oct 2026e</td><td>Oct 2027e</td><td>Oct 2028e</td></tr><tr><td>GAAP Revenue ($, mm)</td><td>63,887</td><td>105,746</td><td>167,484</td><td>214,313</td></tr><tr><td>MW Gross Margin (%)</td><td>77.3</td><td>74.0</td><td>70.3</td><td>69.8</td></tr><tr><td>MW EPS ($)</td><td>5.39</td><td>9.98</td><td>16.63</td><td>21.48</td></tr><tr><td>Inventory ($, mm)</td><td>2,270</td><td>7,864</td><td>10,715</td><td>12,477</td></tr><tr><td>DOI</td><td>57.2</td><td>104.3</td><td>78.6</td><td>70.3</td></tr></table>

## INVESTMENT DRIVERS

\- Dominant position in the data center with merchant silicon and ASICs

\- Increasing adoption of carrier aggregation, antenna filtering in RF and 5G adopt

[中间内容因长度限制已省略]

lusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/13/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$534.39</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$18.81</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$50.86</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$72.00</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$66.06</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$386.01</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$362.05</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$384.05</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$204.62</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$63.94</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$103.12</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$38.88</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$217.53</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$84.23</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$937.00</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$12.87</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$203.53</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$278.39</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>++</td><td>$90.37</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$84.35</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>E (06/24/2026)</td><td>$183.98</td></tr><tr><td>Quantinuum (QNT.O)</td><td>E (06/29/2026)</td><td>$64.09</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,673.97</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$132.15</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$218.75</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$58.24</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$298.57</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$33.65</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$298.99</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$377.92</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$433.82</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
