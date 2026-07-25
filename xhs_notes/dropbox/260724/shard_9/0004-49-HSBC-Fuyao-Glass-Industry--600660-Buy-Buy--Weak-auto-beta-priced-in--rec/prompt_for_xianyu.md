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
# Fuyao Glass Industry (3606 HK/600660 CH)

Buy/Buy: Weak auto beta priced in; recovery ahead

\- Weak auto beta is largely priced in after YTD correction

◆ Fundamentals should improve in 2H26, with valuation remaining compelling

\- Maintain Buy/Buy for A/H shares, with target prices cut to RMB83.30/HKD87.40, from RMB92.20/HKD91.20

The correction largely prices in the weak auto beta. The company's A/H shares have corrected $15\% / 17\%$ YTD (vs. CSI300 $-2\%$ and HSCI $-7\%$ ), primarily reflecting the weak beta of China's auto sector (6M26 domestic wholesales $-6\%$ YoY; Wind Auto Index $-26\%$ YTD). As the domestic auto market enters its seasonally stronger second half, we expect both auto demand and sector sentiment to improve.

Fundamentals should improve from hereon. Despite operating within a weak auto backdrop, the company continues to demonstrate defensive earnings characteristics through: 1) ongoing domestic ASP expansion (supported by higher glazing content from vehicle intelligence upgrades and a richer product mix); 2) further overseas market share gains amid overseas competitor contraction. Meanwhile, cost concerns from soda ash, shipping costs, and energy prices triggered by elevated oil prices in 1H26, should gradually stabilize going into 2H26. Furthermore, utilisation at the new Fuzhou and Anhui facilities should improve and the US Phase II value-added glass plants should ramp up, and likely support sequential gross margin improvement. Although 2Q26 earnings may still face FX-related pressure, we believe the main fundamental uncertainties have passed. A/H shares trade at 12x/11x 2027E P/E vs 22% 2027e earnings growth, and in our view the current valuation looks attractive.

Estimate revisions: We cut our earnings estimates by 16% for 2026 and 13% for 2027, mainly on lower revenue estimates due to the weak domestic auto sales, partly offset by Fuyao's ASP expansion and overseas market share gains. We introduce our 2028 forecasts in this report. Our 2026 estimates are behind Bloomberg consensus considering FX loss impact this year. Our 2027-28 earnings estimates are above Bloomberg by 3% on average, as we are more positive on its margin sustainability and its overseas expansion potential.

Maintain Buy ratings with lower target prices: We continue to use DCF to value Fuyao and cut our target prices, mainly due to lower earnings estimates and revised WACC assumptions (see page 4). Our new target prices of RMB83.30 (previously RMB92.20) for the A-shares and HKD87.40 (previously HKD91.20) for the H-shares imply c52% and c58% upside, respectively, and we maintain our Buy ratings on the A/H shares. See pages 6 for catalysts and downside risks.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

## Equities

Auto Components

China

![](images/eb24ceb4298b3c3b668d0421a74cb40f60774e8f02254d54cb1232c8c94f7667.jpg)

H: MAINTAIN BUY

TARGET PRICE (HKD) PREVIOUS TARGET (HKD)

87.40 91.20

SHARE PRICE (HKD) UPSIDE/DOWNSIDE

55.45 +57.6%

![](images/657055f3c89a123df2931f6c1eb3347f48ab91038670e768dba834e440e27623.jpg)

A: MAINTAIN BUY

TARGET PRICE (CNY) PREVIOUS TARGET (CNY)

83.30 92.20

SHARE PRICE (CNY) UPSIDE/DOWNSIDE

54.94 +51.6%

MARKET DATA

<table><tr><td>BBG / RIC</td><td>3606 HK / 3606.HK</td></tr><tr><td>Market cap (HKDm / USDm)</td><td>161,157 / 20,553</td></tr><tr><td>Free float (H / A)</td><td>100% / 66%</td></tr><tr><td>3m ADTV (USDm) (H / A)</td><td>22 / 117</td></tr></table>

FINANCIALS AND RATIOS (CNY)

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>HSBC EPS</td><td>3.57</td><td>3.67</td><td>4.48</td><td>5.28</td></tr><tr><td>HSBC EPS (prev)</td><td>3.69</td><td>4.38</td><td>5.12</td><td>na</td></tr><tr><td>Change (%)</td><td>-3.2</td><td>-16.2</td><td>-12.5</td><td>na</td></tr><tr><td>Consensus EPS</td><td>3.66</td><td>3.95</td><td>4.63</td><td>5.26</td></tr></table>

Source: LSEG IBES, HSBC estimates

## Yuqian Ding\*

Head of China Technology & Autos Research
The Hongkong and Shanghai Banking Corporation Limited
yuqian.ding@hsbc.com.hk
+852 2288 5108

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

## No country for bears

The $24^{\text{th}}$ edition of the EM Sentiment Survey Click to view

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

View HSBC Global Investment Research at: https://www.research.hsbc.com

## Financials & valuation

Financial statements

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Profit &amp; loss summary (CNYm)</td></tr><tr><td>Revenue</td><td>45,787</td><td>49,492</td><td>56,459</td><td>65,559</td></tr><tr><td>EBITDA</td><td>13,152</td><td>14,695</td><td>17,196</td><td>19,555</td></tr><tr><td>Depreciation &amp; amortisation</td><td>-3,077</td><td>-3,490</td><td>-3,780</td><td>-3,998</td></tr><tr><td>Operating profit/EBIT</td><td>10,075</td><td>11,205</td><td>13,416</td><td>15,557</td></tr><tr><td>Net interest</td><td>831</td><td>-11</td><td>304</td><td>669</td></tr><tr><td>PBT</td><td>11,162</td><td>11,473</td><td>13,999</td><td>16,504</td></tr><tr><td>HSBC PBT</td><td>11,162</td><td>11,473</td><td>13,999</td><td>16,504</td></tr><tr><td>Taxation</td><td>-1,845</td><td>-1,896</td><td>-2,314</td><td>-2,728</td></tr><tr><td>Net profit</td><td>9,321</td><td>9,581</td><td>11,689</td><td>13,781</td></tr><tr><td>HSBC net profit</td><td>9,321</td><td>9,581</td><td>11,689</td><td>13,781</td></tr><tr><td colspan="5">Cash flow summary (CNYm)</td></tr><tr><td>Cash flow from operations</td><td>12,055</td><td>11,708</td><td>13,161</td><td>14,398</td></tr><tr><td>Capex</td><td>-6,164</td><td>-6,731</td><td>-4,517</td><td>-4,261</td></tr><tr><td>Cash flow from investment</td><td>-6,099</td><td>-6,731</td><td>-4,517</td><td>-4,261</td></tr><tr><td>Dividends</td><td>-5,480</td><td>-5,639</td><td>-6,879</td><td>-8,110</td></tr><tr><td>Change in net debt</td><td>-1,012</td><td>503</td><td>-3,006</td><td>-3,257</td></tr><tr><td>FCF equity</td><td>5,931</td><td>4,977</td><td>8,644</td><td>10,136</td></tr><tr><td colspan="5">Balance sheet summary (CNYm)</td></tr><tr><td>Intangible fixed assets</td><td>1,953</td><td>3,127</td><td>3,443</td><td>3,492</td></tr><tr><td>Tangible fixed assets</td><td>27,004</td><td>29,072</td><td>29,492</td><td>29,705</td></tr><tr><td>Current assets</td><td>39,345</td><td>40,161</td><td>45,936</td><td>53,323</td></tr><tr><td>Cash &amp; others</td><td>19,274</td><td>18,771</td><td>21,776</td><td>25,033</td></tr><tr><td>Total assets</td><td>70,062</td><td>74,169</td><td>80,773</td><td>88,536</td></tr><tr><td>Operating liabilities</td><td>21,231</td><td>21,400</td><td>23,199</td><td>25,295</td></tr><tr><td>Gross debt</td><td>11,279</td><td>11,279</td><td>11,279</td><td>11,279</td></tr><tr><td>Net debt</td><td>-7,995</td><td>-7,492</td><td>-10,497</td><td>-13,755</td></tr><tr><td>Shareholders&#x27; funds</td><td>37,556</td><td>41,499</td><td>46,309</td><td>51,979</td></tr><tr><td>Invested capital</td><td>27,798</td><td>32,188</td><td>33,896</td><td>36,192</td></tr></table>

Ratio, growth and per share analysis

Valuation data: 3606 HK

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>EV/sales</td><td>2.9</td><td>2.7</td><td>2.3</td><td>1.9</td></tr><tr><td>EV/EBITDA</td><td>10.0</td><td>9.0</td><td>7.5</td><td>6.4</td></tr><tr><td>EV/IC</td><td>4.7</td><td>4.1</td><td>3.8</td><td>3.5</td></tr><tr><td>PE*</td><td>13.4</td><td>13.0</td><td>10.7</td><td>9.1</td></tr><tr><td>PB</td><td>3.3</td><td>3.0</td><td>2.7</td><td>2.4</td></tr><tr><td>FCF yield (%)</td><td>4.3</td><td>3.6</td><td>6.2</td><td>7.3</td></tr><tr><td>Dividend yield (%)</td><td>4.4</td><td>4.5</td><td>5.5</td><td>6.5</td></tr></table>

\* Based on HSBC EPS (diluted)

Valuation data: 600660 CH

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>EV/sales</td><td>2.9</td><td>2.7</td><td>2.3</td><td>1.9</td></tr><tr><td>EV/EBITDA</td><td>10.0</td><td>9.0</td><td>7.5</td><td>6.4</td></tr><tr><td>EV/IC</td><td>4.7</td><td>4.1</td><td>3.8</td><td>3.5</td></tr><tr><td>PE*</td><td>15.4</td><td>15.0</td><td>12.3</td><td>10.4</td></tr><tr><td>PB</td><td>3.8</td><td>3.5</td><td>3.1</td><td>2.8</td></tr><tr><td>FCF yield (%)</td><td>4.3</td><td>3.6</td><td>6.2</td><td>7.3</td></tr><tr><td>Dividend yield (%)</td><td>3.8</td><td>3.9</td><td>4.8</td><td>5.7</td></tr></table>

\* Based on HSBC EPS (diluted)

<table><tr><td>Environmental Indicators</td><td>12/2025a</td><td>Governance Indicators</td><td>12/2025a</td></tr><tr><td>GHG emission intensity*</td><td>413.3</td><td>No. of board members</td><td>11</td></tr><tr><td>Energy intensity*</td><td>1,034.7</td><td>Average board tenure (years)</td><td>10.7</td></tr><tr><td>CO2 reduction policy</td><td>Yes</td><td>Female board members (%)</td><td>36.4</td></tr><tr><td>Social Indicators</td><td>12/2025a</td><td>Board members independence (%)</td><td>36.4</td></tr><tr><td>Employee costs as % of revenues</td><td>[n/a]</td><td></td><td></td></tr><tr><td>Employee turnover (%)</td><td>[n/a]</td><td></td><td></td></tr><tr><td>Diversity policy</td><td>Yes</td><td></td><td></td></tr></table>

Source: Company data, HSBC  
\* GHG intensity and energy intensity are measured in kg and kWh respectively against revenue in USD '000s

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Y-o-y % change</td></tr><tr><td>Revenue</td><td>16.7</td><td>8.1</td><td>14.1</td><td>16.1</td></tr><tr><td>EBITDA</td><td>20.5</td><td>11.7</td><td>17.0</td><td>13.7</td></tr><tr><td>Operating profit</td><td>23.0</td><td>11.2</td><td>19.7</td><td>16.0</td></tr><tr><td>PBT</td><td>24.1</td><td>2.8</td><td>22.0</td><td>17.9</td></tr><tr><td>HSBC EPS</td><td>24.1</td><td>2.8</td><td>22.0</td><td>17.9</td></tr><tr><td colspan="5">Ratios (%)</td></tr><tr><td>Revenue/IC (x)</td><td>1.7</td><td>1.7</td><td>1.7</td><td>1.9</td></tr><tr><td>ROIC</td><td>32.0</td><td>32.6</td><td>35.9</td><td>39.5</td></tr><tr><td>ROE</td><td>25.5</td><td>24.2</td><td>26.6</td><td>28.0</td></tr><tr><td>ROA</td><td>14.0</td><td>14.3</td><td>15.7</td><td>16.6</td></tr><tr><td>EBITDA margin</td><td>28.7</td><td>29.7</td><td>30.5</td><td>29.8</td></tr><tr><td>Operating profit margin</td><td>22.0</td><td>22.6</td><td>23.8</td><td>23.7</td></tr><tr><td>EBITDA/net interest (x)</td><td></td><td>1356.6</td><td></td><td></td></tr><tr><td>Net debt/equity</td><td>-21.3</td><td>-18.1</td><td>-22.7</td><td>-26.5</td></tr><tr><td>Net debt/EBITDA (x)</td><td>-0.6</td><td>-0.5</td><td>-0.6</td><td>-0.7</td></tr><tr><td>CF from operations/net debt</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="5">Per share data (CNY)</td></tr><tr><td>EPS reported (diluted)</td><td>3.57</td><td>3.67</td><td>4.48</td><td>5.28</td></tr><tr><td>HSBC EPS (diluted)</td><td>3.57</td><td>3.67</td><td>4.48</td><td>5.28</td></tr><tr><td>DPS</td><td>2.10</td><td>2.16</td><td>2.64</td><td>3.11</td></tr><tr><td>Book value</td><td>14.39</td><td>15.90</td><td>17.74</td><td>19.92</td></tr></table>

Price relative: 3606 HK  
![](images/c4963e9812d23945dcc324a05941f42311391f6e1d41ee74559324dccf580ef7.jpg)  
Source: HSBC

Price relative: 600660 CH  
![](images/8ab365e11929190419926fe60b9f38e02b58edc63c8d2adeac9e4f13240c4c5d.jpg)  
Source: HSBC  
Note: Priced at close of 20 Jul 2026

Key charts  
Exhibit 1. Resilient GPM and OPM performance during past quarters  
![](images/177cd7876d5ba192e4662c81ce4d6862045dc84dbf3b2d2aa18f708909b94594.jpg)  
Source: Company data, HSBC

Exhibit 2. Fuyao's revenue growth has been defensive against China and Global PC sales volatility, thanks to its ASP expansion and overseas market share gain  
![](images/408ab771cf54a300b53aba225640416eb436df3e049b5faef8f48ddc8fac23a0.jpg)  
Source: Rho Motion, Company data, HSBC

## Estimate changes

## We lower our earnings estimates

We cut our earnings estimates by 16% for 2026 and 13% for 2027, mainly because:

We lower 2026-27e revenue estimates by $12\%$ and $14\%$ due to the weak domestic auto sales, but partly offset by Fuyao's ASP expansion and overseas market share gains.

We raise GPM (incl. D&A) by 0.3ppt and 0.9ppt, on continued improved execution and stabilised soda ash pricing.

We raise operating expense (SG&A and R&D) ratio estimates by 0.6ppt for 2026e and 0.2ppt for 2026e, on new factory ramping-up impact.

We introduce our 2028 forecasts in this report. Our 2026e estimates are behind Bloomberg consensus considering FX loss impact this year. Our 2027-28e earnings estimates are above Bloomberg by 3% on average, as we are more positive on its margin sustainability and its overseas expansion potential.

Exhibit 3. Estimate changes

<table><tr><td rowspan="2">(RMBm)</td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">Change</td></tr><tr><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td></tr><tr><td>Revenue</td><td>49,492</td><td>56,459</td><td>65,559</td><td>55,945</td><td>65,293</td><td>NA</td><td>-12%</td><td>-14%</td><td>NA</td></tr><tr><td>Gross profit (incl. D&amp;A)</td><td>18,629</td><td>21,602</td><td>25,063</td><td>20,891</td><td>24,423</td><td>NA</td><td>-11%</td><td>-12%</td><td>NA</td></tr><tr><td>GPM (incl. D&amp;A)</td><td>37.6%</td><td>38.3%</td><td>38.2%</td><td>37.3%</td><td>37.4%</td><td>NA</td><td>+0.3ppt</td><td>+0.9ppt</td><td>NA</td></tr><tr><td>Operating expense ratio</td><td>15.0%</td><td>14.5%</td><td>14.5%</td><td>14.4%</td><td>14.3%</td><td>NA</td><td>+0.6ppt</td><td>+0.2ppt</td><td>NA</td></tr><tr><td>Net profit</td><td>9,581</td><td>11,689</td><td>13,781</td><td>11,428</td><td>13,362</td><td>NA</td><td>-16%</td><td>-13%</td><td>NA</td></tr><tr><td>EPS (RMB)</td><td>3.67</td><td>4.48</td><td>5.28</td><td>4.38</td><td>5.12</td><td>NA</td><td>-16%</td><td>-13%</td><td>NA</td></tr></table>

Source: HSBC estimates

Exhibit 4. HSBC estimates vs Bloomberg consensus

<table><tr><td rowspan="2">(RMBm)</td><td colspan="3">HSBC estimates</td><td colspan="3">Consensus</td><td colspan="3">Difference</td></tr><tr><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td></tr><tr><td>Revenue</td><td>49,492</td><td>56,459</td><td>65,559</td><td>52,083</td><td>60,021</td><td>67,893</td><td>-5%</td><td>-6%</td><td>-3%</td></tr><tr><td>Net profit</td><td>9,581</td><td>11,689</td><td>13,781</td><td>10,103</td><td>11,589</td><td>12,980</td><td>-5%</td><td>1%</td><td>6%</td></tr></table>

Source: Bloomberg, HSBC estimates

## Valuation and risks

## Maintain Buy ratings with lower target prices

We continue to use a DCF model to value Fuyao and lower our target prices, mainly due to lower earnings estimates and revised WACC assumptions. We now apply a WACC of 7.9% (from 7.0%), based on a risk-free rate of 4.25% (unchanged), a market premium of 4.75% (unchanged), and beta coefficient of 0.9 (from 0.8). Applying an H/A share valuation discount of 90% (unchanged), the latest HSBC end-2026 RMB-HKD FX forecast of 1.17 (previously end-2025 RMB-HKD FX rate of 1.10), and a perpetual growth rate of 2.5% (unchanged; see Exhibit 6), we derive our new target prices of RMB83.30 (previously RMB92.20) for the A shares and HKD87.40 (previously HKD91.20) for the H shares, which imply c52% and c58% upside, respectively. We maintain our Buy ratings for the A/H shares.

Exhibit 5. DCF valuation assumptions – cash f

[中间内容因长度限制已省略]

es Commission and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.
"""
