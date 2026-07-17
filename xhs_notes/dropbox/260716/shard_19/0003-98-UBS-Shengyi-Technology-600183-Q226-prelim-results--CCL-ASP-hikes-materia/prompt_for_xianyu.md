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
EPS (UBS, diluted) (Rmb)

First Read

# Shengyi Technology Q226 prelim results: CCL ASP hikes materialized, PCB margin concerns alleviated

## Q: How did the results compare vs expectations?

A: : Shengyi Technology (SYT) announced H126 preliminary results: net profit to parent is expected to be Rmb3.1-3.3bn (up 117%-131% YoY) and Rmb2.7-2.9bn (up 97-112% YoY) after non-recurring items. Q226 net profit to parent is expected to fall in the range of Rmb1.9-2.1bn (up 125-148% YoY/+68-85% QoQ), 37-51% above UBS-S estimate of Rmb1.4bn and 32-45% above Reuters consensus. We believe the impressive earnings beat is from 1) robust CCL sales growth and better profitability driven by both higher AI mix and strong ASP lift on conventional CCL; 2) accelerating sales growth and margin improvement from PCB business under Shengyi Electronics (SYE).

## Q: What were the most noteworthy areas in the results?

A: SYE (fully consolidated by SYT) guides its H126 revenue to grow by 49-58% YoY to Rmb5.6-5.9bn, supported by strong AI server and switch orders and contribution from new capacity. Net profit to parent is expected to be in the range of Rmb1.08 -1.14bn (up 104-114% YoY). This implies SYE's Q226 revenue at Rmb3.2-3.5bn (+54%/40% YoY/QoQ at midpoint), keeping >50% YoY growth since Q125 and resuming QoQ growth after 2 quarters' decline; net profit is expected to be Rmb637- 692mn, +93-110% YoY and +43-56% QoQ. The implied Q226 net profit margin would reach 19.7% at midpoint, +1.1ppt vs 18.6% in Q126.

## Q: Has the company's outlook/guidance changed?

A: No guidance was provided in the preliminary results. Based on our industry study, since H225 tier-1 CCL makers such as Kingboard Laminates and SYT have been raising CCL ASP several rounds to offset raw material price inflation (ie copper and glass fibre). We've been flagging expectation of a CCL upcycle multiple times in our previous reports (here, here and here). We expect SYT's CCL business to continue operating at full UTR in H226 based on current order visibility. On PCB business, many investors have feared such CCL ASP hikes would squeeze margins of PCB players. While we do acknowledge such pressure on conventional PCB makers, we believe AI CCL prices have been largely stable and AI PCB players can better mitigate by lifting AI product mix. We view the accelerating QoQ NP growth of Shennan and WUS in Q226 prelim results and SYE's improved Q226 NPM as the supporting evidence.

## Q: How would we expect investors to react?

A: We expect investors to react positively to the prelim earnings beat. SYT is due to announce full Q226 results on Aug 14th.

Our rating and price target are Under Review pending further analysis.

## Equities

China
Diversified Technology Services

12-month rating (UR) Buy \*

12m price target (UR) Rmb97.00

Price (13 Jul 2026) Rmb134.45

<table><tr><td colspan="2">Trading data and key metrics</td></tr><tr><td>52-wk range</td><td>Rmb187.20-32.91</td></tr><tr><td>Market cap.</td><td>Rmb327b/US$48.1b</td></tr><tr><td>Shares o/s</td><td>2,429m (ORDA)</td></tr><tr><td>Free float</td><td>46%</td></tr><tr><td>Avg. daily volume (&#x27;000)</td><td>74,000</td></tr><tr><td>Avg. daily value (m)</td><td>Rmb9,363</td></tr><tr><td>Common s/h equity (12/26E)</td><td>Rmb19.6b</td></tr><tr><td>P/BV (12/26E)</td><td>16.6x</td></tr><tr><td>Net debt to EBITDA (12/26E)</td><td>0.3x</td></tr></table>

<table><tr><td></td><td>UBS</td><td>Cons.</td></tr><tr><td>12/26E</td><td>2.38</td><td>2.35</td></tr><tr><td>12/27E</td><td>3.17</td><td>3.48</td></tr><tr><td>12/28E</td><td>4.10</td><td>4.92</td></tr></table>

Jimmy Yu
Analyst
S1460517080002
jimmy.yu@ubs.com
+86-21-3866 8880

<table><tr><td>Highlights (Rmbm)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>Revenues</td><td>16,586</td><td>20,388</td><td>28,431</td><td>41,184</td><td>53,730</td><td>65,875</td><td>69,294</td><td>72,646</td></tr><tr><td>EBIT (UBS)</td><td>1,291</td><td>1,998</td><td>4,300</td><td>7,307</td><td>9,458</td><td>12,018</td><td>12,442</td><td>13,174</td></tr><tr><td>Net earnings (UBS)</td><td>1,164</td><td>1,739</td><td>3,334</td><td>5,761</td><td>7,669</td><td>9,911</td><td>10,269</td><td>10,937</td></tr><tr><td>EPS (UBS, diluted) (Rmb)</td><td>0.50</td><td>0.74</td><td>1.39</td><td>2.38</td><td>3.17</td><td>4.10</td><td>4.25</td><td>4.53</td></tr><tr><td>DPS (net) (Rmb)</td><td>0.45</td><td>0.60</td><td>1.20</td><td>1.78</td><td>2.37</td><td>3.26</td><td>3.38</td><td>3.60</td></tr><tr><td>Net (debt) / cash</td><td>(1,063)</td><td>(1,536)</td><td>(1,902)</td><td>(2,864)</td><td>(3,757)</td><td>(4,137)</td><td>(2,907)</td><td>(1,415)</td></tr><tr><td>Profitability/valuation</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>EBIT (UBS) margin %</td><td>7.8</td><td>9.8</td><td>15.1</td><td>17.7</td><td>17.6</td><td>18.2</td><td>18.0</td><td>18.1</td></tr><tr><td>ROIC (EBIT) %</td><td>7.9</td><td>11.9</td><td>23.0</td><td>33.2</td><td>36.2</td><td>39.4</td><td>37.3</td><td>38.2</td></tr><tr><td>EV/EBITDA (UBS core) x</td><td>19.6</td><td>16.8</td><td>19.3</td><td>39.7</td><td>31.1</td><td>24.6</td><td>23.3</td><td>22.2</td></tr><tr><td>P/E (UBS, diluted) x</td><td>32.8</td><td>25.9</td><td>28.9</td><td>56.4</td><td>42.4</td><td>32.8</td><td>31.6</td><td>29.7</td></tr><tr><td>Equity FCF (UBS) yield %</td><td>4.4</td><td>1.2</td><td>3.0</td><td>0.8</td><td>1.0</td><td>1.6</td><td>2.8</td><td>3.0</td></tr><tr><td>Dividend yield (net) %</td><td>2.7</td><td>3.1</td><td>3.0</td><td>1.3</td><td>1.8</td><td>2.4</td><td>2.5</td><td>2.7</td></tr></table>

Source: Company accounts, LSEG Eikon, UBS estimates. Metrics marked as (UBS) have had analyst adjustments applied. Valuations: based on an average share price that year, (E): based on a share price of Rmb 134.45 on 13-Jul-2026

Figure 1: SYT 1H26/2Q26 preliminary results

<table><tr><td>H126 Prelim (Rmb mn)</td><td>Low</td><td>Mid</td><td>High</td></tr><tr><td>NP to parent</td><td>3,099</td><td>3,199</td><td>3,298</td></tr><tr><td>vs. UBS</td><td>20%</td><td>24%</td><td>28%</td></tr><tr><td>vs. Reuters</td><td>18%</td><td>22%</td><td>25%</td></tr><tr><td>YoY</td><td>117%</td><td>124%</td><td>131%</td></tr><tr><td>NP excl. non-recurring</td><td>2,719</td><td>2,819</td><td>2,918</td></tr><tr><td>YoY</td><td>97%</td><td>105%</td><td>112%</td></tr><tr><td colspan="4">Q226 Prelim (Rmb mn)</td></tr><tr><td>NP to parent</td><td>1,941</td><td>2,040</td><td>2,140</td></tr><tr><td>vs. UBS</td><td>37%</td><td>44%</td><td>51%</td></tr><tr><td>vs. Reuters</td><td>32%</td><td>38%</td><td>45%</td></tr><tr><td>YoY</td><td>125%</td><td>136%</td><td>148%</td></tr><tr><td>QoQ</td><td>68%</td><td>76%</td><td>85%</td></tr><tr><td>NP excl. non-recurring</td><td>1,636</td><td>1,736</td><td>1,835</td></tr><tr><td>YoY</td><td>100%</td><td>112%</td><td>124%</td></tr><tr><td>QoQ</td><td>51%</td><td>60%</td><td>69%</td></tr></table>

Source: Company data, UBS-S estimates, LSEG

Figure 2: SYE 1H26/2Q26 preliminary results

<table><tr><td>H126 Prelim (Rmb mn)</td><td>Low</td><td>Mid</td><td>High</td></tr><tr><td>Revenue</td><td>5,622</td><td>5,779</td><td>5,937</td></tr><tr><td>YoY</td><td>49%</td><td>53%</td><td>58%</td></tr><tr><td>NP to parent</td><td>1,082</td><td>1,109</td><td>1,137</td></tr><tr><td>YoY</td><td>104%</td><td>109%</td><td>114%</td></tr><tr><td>NP excl. non-recurring</td><td>1,082</td><td>1,109</td><td>1,137</td></tr><tr><td>YoY</td><td></td><td></td><td></td></tr><tr><td colspan="4">Q226 Prelim (Rmb mn)</td></tr><tr><td>Revenue</td><td>3,211</td><td>3,369</td><td>3,526</td></tr><tr><td>YoY</td><td>47%</td><td>54%</td><td>61%</td></tr><tr><td>QoQ</td><td>33%</td><td>40%</td><td>46%</td></tr><tr><td>NP to parent</td><td>637</td><td>665</td><td>692</td></tr><tr><td>YoY</td><td>93%</td><td>101%</td><td>110%</td></tr><tr><td>QoQ</td><td>43%</td><td>49%</td><td>56%</td></tr><tr><td>NPM</td><td>19.8%</td><td>19.7%</td><td>19.6%</td></tr></table>

Source: Company data

Special thanks to Edward Liu and David Chow for their contribution on this note.

## Forecast returns

<table><tr><td>Forecast price appreciation</td><td>-27.9%</td></tr><tr><td>Forecast dividend yield</td><td>1.3%</td></tr><tr><td>Forecast stock return</td><td>-26.5%</td></tr><tr><td>Market return assumption</td><td>6.8%</td></tr><tr><td>Forecast excess return</td><td>-33.3%</td></tr></table>

## Company Description

Shengyi Technology, founded in 1985, is the world's leading electronic circuit base maker. Its main product, Copper Clad Laminate (CCL) is the most crucial material used in printed circuit board (PCB) manufacturing. The company is headquartered in Dongguan, Guangdong and has subsidiaries and holding companies in Xinyang, Suzhou, Hong Kong, Taiwan, Changshu, Nantong and Jiujiang. In 2020, the company spun off its PCB subsidiary, Shengyi Electronics, for an independent listing on the A-share STAR board.

## Valuation Method and Risk Statement

Our valuation of Shengyi Technology is based on a PE methodology.

Downside risks: 1) severe raw material price inflation; 2) slower exit of low-end CCL capacity and intensifying competition; and 3) weakening end demand from home appliance, telecommunication, automotive, or data communication

## Quantitative Research Review

UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. The views for this month can be found below. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research Team on the email above.

## Shengyi Technology

<table><tr><td>Question</td><td>Response</td></tr><tr><td>1. Is the industry structure facing the firm likely to improve or deteriorate over the next six months? Rate on a scale of 1-5 (1 = getting worse, 3 = no change, 5 = getting better, N/A = no view)</td><td>4</td></tr><tr><td>2. Is the regulatory/government environment facing the firm likely to improve or deteriorate over the next six months? Rate on a scale of 1-5 (1 = getting tougher 3 = no change, 5 = getting better, N/A = no view)</td><td>3</td></tr><tr><td>3. Over the last 3-6 months in broad terms have things been improving/no change/getting worse for this stock? Rate on a scale of 1-5 (1 = getting a lot worse, 3 = not much change, 5 = getting a lot better, N/A = no view)</td><td>4</td></tr><tr><td>4. Relative to the current CONSENSUS EPS forecast, is the next company EPS update likely to lead to: (1 = negative surprise vs consensus, 3 = in-line with consensus, 5 = positive surprise vs consensus expectations, N/A = no view)</td><td>3</td></tr><tr><td>5. What&#x27;s driving the difference?</td><td></td></tr><tr><td>6. Relative to YOUR current earnings forecast, is there relatively greater risk at the next earnings result of:(1 = downside skew risk to earnings, 3 = equal upside or downside risk to earnings, 5 = upside skew risk to earnings, N/A = no view)</td><td>3</td></tr><tr><td>7. What&#x27;s driving the difference?</td><td></td></tr><tr><td>8. Is there an upcoming catalyst for the company over the next three months?</td><td></td></tr><tr><td>9. Is there an actual or approximate date for the catalyst?</td><td></td></tr><tr><td>10. Is the catalyst date an actual or approximate date?</td><td></td></tr><tr><td>11. What is the catalyst?</td><td></td></tr></table>

## Required Disclosures

This document has been prepared by UBS Co. Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 14 July 2026 12:15 AM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly o

[中间内容因长度限制已省略]

and/or Market Counterparties only as classified under the DFSA rulebook. It should not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
