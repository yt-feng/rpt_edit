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
## Lam Research

Beat-and-Raise on NAND Reacceleration and Continued Momentum on Leading-Edge F/L and DRAM; CY26 WFE Raised to \$150B+ with Strong CY27 Setup; LT GMs Move to Mid-50% Range; Reit OW

Lam Research Corporation (LRCX) delivered yet another clean beat-and-raise, with strong results that beat Street expectations and an even more impressive out-quarter guide that surpassed the high end of buyside expectations we had heard heading into the print. The company posted record revenues, gross margins (\~highest in 20 years), operating margins, and EPS, and guided out-quarter revenues to \$8.10B ± \$400M, implying \~20% Q/Q growth off a record base. Strength in the quarter was driven by a sharp acceleration in NAND spending, continued DRAM strength, improving leading-edge foundry/logic demand, and another record quarter in CSBG. Outside of the strength in memory (NAND/DRAM), LRCX highlighted traction at leading-edge foundry/logic customers and noted that it was in active engagement with a “new logic customer in the U.S.,” and we think this creates another potential share-gain opportunity for the company, adding to its ability to outgrow broader WFE over the next few years. Looking ahead, LRCX guided out-quarter revenues to \$8.10B at the midpoint, with gross margins of \~52%, operating margins of \~39.5%, and non-GAAP EPS of \$2.15 — all of which screened higher than Street/buyside expectations heading into the print. LRCX also notably updated its multi-year profitability framework, stating that it is now targeting mid-50% gross margins and mid-40% operating margins over the next several years. To us, this marks a positive structural shift in expectations, as LRCX is now effectively moving from proving that \~50% gross margins are sustainable to establishing an explicit path toward mid-50% gross margins. Much like its capital equipment peers earlier this week, LRCX also raised its CY26 WFE outlook to the low-\$150B range, up from its prior \~\$140B view. The upward revision reflects stronger AI-driven investment across memory, foundry/logic, and advanced packaging, as well as customers finding incremental cleanroom capacity and resolving prior bottlenecks to capacity additions. And while management did not provide a numerical WFE forecast for CY27, it characterized the setup as “extraordinary,” with current customer conversations signaling unprecedented long-term demand visibility into 2027 and beyond. From a bottom-up standpoint, LRCX expects CY27 WFE growth to be led by DRAM, followed by F/L, and then NAND, with management remaining confident in its ability to outperform broader WFE growth due to its technology leadership in deposition and etch, expanding SAM (\~trending towards high-30% of WFE), and strong customer partnerships. On the back of the results, stronger out-quarter guidance, and the improved multi-year profitability framework, we are raising our 2026 estimates and establishing our new Dec-27 price target of \$340 (vs. prior Dec-26 PT of \$315), which assumes LRCX trades at \~30x our 2H27 annualized EPS power of \$11.35, broadly in line with comparable large-cap semiconductor capital equipment peers.

## Overweight

LRCX, LRCX US
Price (29 Jul 26):\$252.35

▲Price Target (Dec-27):\$340.00
Prior (Dec-26):\$315.00

Semiconductors & Semiconductor Capital Equipment / IT Hardware

Harlan Sur AC
(1-415) 315-6700
harlan.sur@JPM.com

Apoorva Kumar
(1-212) 270-0668
apoorva.kumar@JPM.com

Mayur Ramdhani
(1-212) 622-1664
mayur.ramdhani@JPM.com
JPM Securities LLC

Quarterly Forecasts (FYE Jun)
Adj. EPS (\$)

<table><tr><td colspan="4">Adj. EFO (4)</td></tr><tr><td></td><td>2026A</td><td>2027E</td><td>2028E</td></tr><tr><td>Q1</td><td>1.26</td><td>2.15</td><td></td></tr><tr><td>Q2</td><td>1.27</td><td>2.21</td><td></td></tr><tr><td>Q3</td><td>1.47</td><td>2.42</td><td></td></tr><tr><td>Q4</td><td>1.78</td><td>2.62</td><td></td></tr><tr><td>FY</td><td>5.82</td><td>9.40</td><td></td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>86</td><td>84</td><td>65</td><td>61</td><td>57</td></tr><tr><td>Growth</td><td>54</td><td>65</td><td>75</td><td>61</td><td>76</td></tr><tr><td>Momentum</td><td>16</td><td>5</td><td>30</td><td>40</td><td>20</td></tr><tr><td>Quality</td><td>7</td><td>4</td><td>6</td><td>6</td><td>5</td></tr><tr><td>Low Vol</td><td>46</td><td>45</td><td>45</td><td>44</td><td>59</td></tr></table>

Price Performance  
![](images/908f74d9d8bdc34a014e445b49bbd7e0a2b53cb2a582a827ff2cf2d8ddb26282.jpg)

— LRCX Price (\$) — S&P500 (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>47.4%</td><td>-38.6%</td><td>1.4%</td><td>155.0%</td></tr><tr><td>Rel</td><td>40.5%</td><td>-36.9%</td><td>-1.1%</td><td>140.2%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>1,269</td></tr><tr><td>52-week range ($)</td><td>438.50-90.93</td></tr><tr><td>Market cap ($ mn)</td><td>320,311.10</td></tr><tr><td>Exchange rate</td><td>1.00</td></tr><tr><td>Free float (%)</td><td>99.7%</td></tr><tr><td>3M ADV (mn)</td><td>11.39</td></tr><tr><td>3M ADV ($ mn)</td><td>3,781.7</td></tr><tr><td>Volatility (90 Day)</td><td>76</td></tr><tr><td>Index</td><td>S&amp;P 500</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>31|6|0</td></tr></table>

Key Metrics (FYE Jun)

<table><tr><td>$ in millions</td><td>FY26A</td><td>FY27E</td></tr><tr><td>Financial Estimates</td><td></td><td></td></tr><tr><td>Revenue</td><td>23,233</td><td>34,634</td></tr><tr><td>Adj. EBIT</td><td>8,237</td><td>13,984</td></tr><tr><td>Adj. EBITDA</td><td>8,237</td><td>13,984</td></tr><tr><td>Adj. net income</td><td>7,340</td><td>11,796</td></tr><tr><td>Adj. EPS</td><td>5.82</td><td>9.40</td></tr><tr><td>BBG EPS</td><td>5.69</td><td>8.20</td></tr><tr><td>Cashflow from operations</td><td>5,858</td><td>8,604</td></tr><tr><td>FCFF</td><td>4,891</td><td>7,045</td></tr><tr><td>Margins and Growth</td><td></td><td></td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>26.0%</td><td>49.1%</td></tr><tr><td>EBIT margin</td><td>35.5%</td><td>40.4%</td></tr><tr><td>EBIT Growth Y/Y (%)</td><td>38.3%</td><td>69.8%</td></tr><tr><td>EBITDA margin</td><td>35.5%</td><td>40.4%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>39.1%</td><td>69.8%</td></tr><tr><td>Net margin</td><td>31.6%</td><td>34.1%</td></tr><tr><td>Adj. EPS growth</td><td>40.8%</td><td>61.5%</td></tr><tr><td>Ratios</td><td></td><td></td></tr><tr><td>Adj. tax rate</td><td>11.9%</td><td>15.2%</td></tr><tr><td>Interest cover</td><td>-</td><td>-</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td></tr><tr><td>ROE</td><td>66.0%</td><td>71.8%</td></tr><tr><td>Valuation</td><td></td><td></td></tr><tr><td>FCFF yield</td><td>1.5%</td><td>2.2%</td></tr><tr><td>Dividend yield</td><td>0.1%</td><td>0.1%</td></tr><tr><td>EV/Revenue</td><td>13.7</td><td>9.1</td></tr><tr><td>EV/EBITDA</td><td>38.7</td><td>22.6</td></tr><tr><td>Adj. P/E</td><td>43.4</td><td>26.8</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

Capital spending environment driven by technology transitions (5nm/3nm/2nm) Foundry / Logic, sub-20nm DRAM, and 3D NAND.

Market leader in plasma etch, thin-film deposition (metal and dielectric) platforms, photoresist strip systems, and single-wafer wet/plasma-based cleaning products.

Service/installed base business continues to outperform through cycles.

Expansion of its end markets, market share gain across etching, deposition, and cleaning, technological leadership, and scale should enable Lam Research to outgrow the overall market and drive an EPS CAGR of 18-20% over the next two to three years.

## Valuation

Our Dec-27 PT assumes that LRCX trades at $\sim 30x$ its 2H27 annualized earnings power of \$11.35, in-line with comparable large-cap semiconductor capital equipment peers.

Performance Drivers  
![](images/d09e08a0b9f2ab9963e826e386c92af3e437589258f74343c61b1ccf051ad8f9.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI US</td><td>0.52</td><td>0.53</td></tr><tr><td>Sect: Technology</td><td>-0.09</td><td>0.02</td></tr><tr><td>Ind: Semicond &amp; S Equip</td><td>0.37</td><td>0.36</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>Crude Oil</td><td>-0.43</td><td>-0.26</td></tr><tr><td>US 10yr Breakeven</td><td>-0.20</td><td>-0.20</td></tr><tr><td>Economic Surprise</td><td>-0.15</td><td>-0.19</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>Momentum</td><td>0.45</td><td>0.36</td></tr><tr><td>Size</td><td>0.26</td><td>0.23</td></tr><tr><td>LowVol</td><td>-0.13</td><td>-0.20</td></tr></table>

\- Jun-Qtr results came in above Street estimates, driven by a sharp acceleration in NAND spending, continued DRAM strength, and leading-edge F/L demand... LRCX reported strong Jun-Qtr revenues of \$6.72B (+15% Q/Q. +30% Y/Y), above the midpoint of prior guidance/Street estimates at \~\$6.60B and largely in-line with buyside expectations. This marked the fourth consecutive quarter of record revenues, with the mix of system sales becoming increasingly geared towards memory (\~46% of system revenues this quarter vs. \~39% last quarter). The source of this increase primarily came from NAND, which more than doubled Q/Q as customers accelerated conversions to 256+ layer devices for enterprise SSD / AI storage demand. DRAM also remained strong at \~23% of systems revenues (a slight step down from the record \~27% last quarter). The remaining \~54% of system sales were accounted for by Foundry (\~44% this quarter vs. \~54% last quarter) and Logic (\~10% this quarter vs. \~7% last quarter), with management noting that it was seeing traction at leading-edge F/L customers (specifically on 2/3nm nodes + advanced packaging) and that it was actively engaging with a “new logic customer in the U.S.” Outside of its systems business, LRCX also posted strong results in its CSBG business, which delivered a third consecutive record quarter of revenues at \$2.47B (+17% Q/Q, +43% Y/Y), due to record upgrades (NAND), additional growth in Reliant, and sustained strength in spares demand.

\- Sep-Qtr revenue guide was considerably above Street/buyside expectations, implying a material step up in growth and continued operating leverage... At the midpoint, LRCX guided Sep-Qtr revenues to \$8.10B, implying more than 20% Q/Q growth, with gross margins of \~52%, operating margins at \~39.5%, and non-GAAP EPS of \$2.15 — all of which screened higher than Street/Buyside expectations coming into the print. Although opex is expected to rise next quarter, LRCX noted that the rate of spending should grow at a much slower pace than revenue growth, creating continued operating leverage going forward. More importantly, LRCX updated its multi-year profitability framework, with the company now targeting mid-50% gross margins and mid-40% operating margins over the next several years, both of which will be underpinned by the company's scale, new product introductions, value-based pricing, and further operational efficiencies. We view this as a meaningful reset, as LRCX is already operating above the profitability objectives it outlined at its 2025 Investor Day.

\- CY26 WFE raised to the low-\$150B range, with CY27 WFE setup described as “extraordinary”... Much like its peers, LRCX raised its CY26 WFE outlook to the low-\$150B range, up from its prior view of \~\$140B, and clarified that the earlier upside bias has now effectively played out into the new forecast. The upward revision reflects stronger AI-driven investment across memory, foundry/logic, and advanced packaging, as well as customers finding incremental cleanroom capacity and resolving prior bottlenecks to capacity additions. Although management did not provide a numerical WFE forecast for 2027, it characterized the setup as “extraordinary” as current customer conversations signal unprecedented long-term demand visibility. From a bottom-up perspective, management flagged that it expects 2027 WFE growth to be led by DRAM, followed by F/L, then NAND, with the belief that LRCX would continue to outperform broader WFE growth due to its technology leadership (in deposition & etch) and its strong customer partnerships.

\- Raising PT to \$340 on new 2H27 annualized EPS of \$11.35... On the back of tonight's results, we are raising our 2026 estimates to reflect management's stronger out-quarter guidance and commentary and initiating our new Dec-27 PT of \$340. Our new PT assumes that LRCX trades at \~30x (peer multiple) its 2H27 annualized earnings power of \$11.35, in-line with comparable large-cap semicap peers.

Figure 1: LRCX Quarterly Results and Out-Quarter Guidance

<table><tr><td></td><td>F4Q26 Actual</td><td>JPM Estimate</td><td>Diff</td><td>F4Q26 Consensus</td><td>F1Q27 Guidance</td><td>F1Q27 Consensus</td></tr><tr><td>Revenue ($M)</td><td>$6,722.2</td><td>$6,600.0</td><td>$122.2</td><td>$6,682</td><td>$8,100 ± $400m</td><td>$7,130</td></tr><tr><td>Q/Q Change</td><td>15.1%</td><td>13.0%</td><td>2.1%</td><td>14.4%</td><td>-</td><td>6.7%</td></tr><tr><td>Gross Margin (PF)</td><td>52.0%</td><td>50.5%</td><td>1.5%</td><td>50.5%</td><td>52.0% ± 1%</td><td>50.6%</td></tr><tr><td>Op Margin (PF)</td><td>38.4%</td><td>36.5%</td><td>1.9%</td><td>36.8%</td><td>39.5% ± 1%</td><td>37.1%</td></tr><tr><td>Net Income (PF)</td><td>$2,280.0</td><td>$2,073.0</td><td>$207.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pro-forma EPS</td><td>$1.82</td><td>$1.65</td><td>$0.16</td><td>$1.70</td><td>$2.15 ± $0.15</td><td>$1.84</td></tr></table>

Source: Company Reports, JPM Estimates, Bloomberg Finance L.P.

Figure 2: LRCX Quarterly Revenue by Segment (% of Total)

<table><tr><td></td><td>F1Q26</td><td>F2Q26</td><td>F3Q26</td><td>F4Q26</td></tr><tr><td>DRAM</td><td>16%</td><td>23%</td><td>27%</td><td>23%</td></tr><tr><td>NAND</td><td>18%</td><td>11%</td><td>12%</td><td>23%</td></tr><tr><td>Foundry</td><td>60%</td><td>59%</td><td>54%</td><td>44%</td></tr><tr><td>Logic and Other</td><td>6%</td><td>7%</td><td>7%</td><td>10%</td></tr></table>

Note: Logic includes CMOS Image Sensor, other. Systems include upgrades and revenue from Reliant product line  
Source: Company Reports, JPM Estimates, Bloomberg Finance L.P.

## Balance Sheet and Cash Flow

LRCX exited F4Q26 with cash and short/long-term marketable investments of \$5.58B (vs. \$4.75B in the prior quarter) and operating cash flow of \$1.46B (vs. 1.14B in the prior quarter).

## Appendix I: Valuation and Comps

Figure 3: Semiconductor Capital Equipment Comp Table

<table><tr><td rowspan="2">Company</td><td rowspan="2">Co Ticker</td><td rowspan="2">JPM Rating</td><td rowspan="2">Price 7/29/26</td><td rowspan="2">Mkt Cap ($m)</td><td rowspan="2">EV ($m)</td><td colspan="4">Non-GAAP EPS ($)</td><td rowspan="2">2025-28 CAGR</td><td colspan="4">PE Multiple</td><td colspan="4">Sales ($m)</td><td rowspan="2">2025-28 CAGR</td><td colspan="4">PS Multiple</td></tr><tr><td>2025</td><td>2026</td><td>2027</td><td>2028</td><td>2025</td><td>2026</td><td>2027</td><td>2028</td><td>2025</td><td>2026</td><td>2027</td><td>2028</td><td>2025</td><td>2026</td><td>2027</td><td>2028</td></tr><tr><td>Semiconductor Capital Equipment:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Applied Materials</td><td>AMAT</td><td>OW</td><td>$436.45</td><td>346,524</td><td>345,551</td><td>9.42</td><td>13.81</td><td>18.82</td><td>23.88</td><td>36%</td><td>46.3x</td><td>31.6x</t

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 30 Jul 2026 01:52 AM EDT

Disseminated 30 Jul 2026 05:15 AM EDT
"""
