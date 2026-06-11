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
## Japan Equity Style Investing

Stay with AI Momentum, Hedge a Hawkish BOJ Hike with Value-Momentum

- Japanese equities strengthened in May as risk-on sentiment accelerated on the back of easing geopolitical risk and a further intensification of the global AI semiconductor boom. In line with record highs across major global equity markets, the Nikkei 225 rose sharply into early June, approaching the 68,000 level. While the rally was significantly supported by semiconductor-related names with large index weights, style performance also confirmed a broader pro-risk bias, with Beta, Momentum, and Size, particularly Large Cap, outperforming.  
- Global optimism toward AI semiconductors continued to support Japanese equities on a smoothed basis, despite intermittent pullbacks driven by short-term overextension. In Japan, not only core semiconductor and semiconductor production equipment names, but also AI infrastructure-related stocks posted notable gains. The earnings contribution from the global surge in semiconductor demand remains a key driver. As a result, even when mini-crashes in Momentum occur, fundamental investors have tended to buy the dips before selling pressure from speculative accounts becomes prolonged. This has helped limit downside pressure.

\- At the same time, while AI-related names continue to benefit from medium-term Momentum support, concerns are increasing over the excessive polarization that has developed in the market. With investors pricing in an additional BOJ rate hike in June, some have begun to question the persistent underperformance of Value stocks. Within Value, there are also a number of names that carry a reasonable degree of Momentum. As such, in a short-term rotation away from AI Momentum names, Value with Momentum characteristics could become an attractive destination for flows.

\- Our proprietary Japan QMI improved month-over-month in May and remained in Expansion territory by definition. Although higher commodity prices stemming from the Strait of Hormuz closure have affected parts of the domestic non-manufacturing sector, manufacturing has shown greater-than-expected resilience, led by AI-related demand. The global capex cycle also remains on an upswing, contributing to the improvement in Japan QMI. That said, the recent pace of improvement partly reflects one-off tailwinds such as special demand in memory, and statistically, maintaining the current pace of acceleration appears challenging. Looking into the summer, our base case remains that investors should keep potential cyclical deceleration in mind and remain alert to overheating in the Beta effect.

\- From June onward, we expect the AI semiconductor-led market structure to remain broadly intact, while periodic reversals are likely. However, investors should also prepare for two risks: insufficient pricing of a potentially more hawkish-than-expected BOJ rate hike, and a partial correction of the extreme polarization between winning and losing sectors. In that context, we would pay closer attention to the overlap between Value and Momentum, where laggards may become a recipient of hedging-related flows.

## Global Quantitative and Derivatives Strategy

Masanari Takada AC

(81-3) 6736-8636

masanari.takada@JPM.com

JPM Securities Japan Co., Ltd.

Tony SK Lee

(852) 2800-8857

tony.sk.lee@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Robert Smith, PhD

(61-2) 9003-8808

robert.z.smith@JPM.com

JPM Securities Australia Limited

Khuram Chaudhry

(44-20) 7134-6297

khuram.chaudhry@JPM.com

JPM Securities plc

Dubravko Lakos-Bujas

(1-212) 622-3601

dubravko.lakos-bujas@JPM.com

JPM Securities LLC

Figure 1: Japan Equity Style Assessments for June  
Changes from the prior quarter (Q1 2026) are highlighted in red (there may be none)

<table><tr><td colspan="2">Styles</td><td>Value</td><td>Growth</td><td>Quality</td><td>Low Vol</td><td>High Beta</td><td>Size (L-Smid)</td><td>Momentum</td></tr><tr><td colspan="2">Overall Japan Views</td><td>OW</td><td>UW</td><td>OW on Mid caps</td><td>UW</td><td>N</td><td>OW on Mid caps</td><td>Selective OW</td></tr><tr><td>Cycle (QMI)</td><td>Exp -&gt;Slowing</td><td>EV/EBITDA</td><td>Earning Mom</td><td>Buy</td><td>UW</td><td>N</td><td>OW</td><td>Sticky</td></tr><tr><td>Position</td><td>Mild heavy</td><td>Mild-Heavy</td><td>Less Heavy</td><td>Less Heavy</td><td>Light</td><td>Heavy</td><td>Concentrated</td><td>Heavy</td></tr><tr><td>Themes</td><td>Themes affecting JPN</td><td>Inflation/ROIC&gt;WACC/BOJ Hike</td><td>Quality-competitions/AI</td><td>Takaichi&#x27;s Industrial Policy/AI</td><td>Defensive</td><td>Offensives</td><td>Concentration/Passive flows</td><td>Concentration on AI-related names</td></tr></table>

Source: JPM

Figure 2: Key Summary of Japan Style for May

<table><tr><td>Factor</td><td>May</td><td>Apr</td><td>Mar</td><td>Sharpe Last 12 Months</td></tr><tr><td>Momentum</td><td>6.4%</td><td>14.1%</td><td>-12.9%</td><td>0.44</td></tr><tr><td>Size (L-S)</td><td>6.3%</td><td>13.3%</td><td>-4.0%</td><td>0.68</td></tr><tr><td>Beta (High)</td><td>6.2%</td><td>25.9%</td><td>-8.6%</td><td>0.74</td></tr><tr><td>Earnings Growth</td><td>3.7%</td><td>13.7%</td><td>-5.9%</td><td>0.32</td></tr><tr><td>Price to Book</td><td>0.8%</td><td>-10.5%</td><td>4.5%</td><td>0.17</td></tr><tr><td>Earnings Yield</td><td>-2.3%</td><td>-18.7%</td><td>0.6%</td><td>0.00</td></tr><tr><td>Div Yield</td><td>-5.9%</td><td>-14.1%</td><td>9.9%</td><td>-0.03</td></tr><tr><td>ROE</td><td>-8.9%</td><td>5.5%</td><td>4.2%</td><td>-0.21</td></tr><tr><td>JPM Quality</td><td>-10.3%</td><td>5.0%</td><td>5.7%</td><td>-0.27</td></tr><tr><td>Q-Score</td><td>-10.5%</td><td>10.2%</td><td>-6.7%</td><td>0.37</td></tr><tr><td>Low Vol</td><td>-11.1%</td><td>-23.6%</td><td>9.9%</td><td>-0.50</td></tr></table>

Source: JPM

Figure 3: Key Chart - Value Performance Isn't Priced for a BoJ Rate Hike  
![](images/dae69060b72b8225dc9f9472fb9d632e4e2b0ca15eaea79ec9cca4c6587789ab.jpg)

<details>
<summary>line chart</summary>

| Year | Value (12m/m, LHS) | JPM BoJ Speech score (RHS) |
|------|---------------------|-----------------------------|
| 2016 | ~0%                 | ~0%                         |
| 2017 | ~25%                | ~-30%                       |
| 2018 | ~-10%               | ~-40%                       |
| 2019 | ~-5%                | ~-30%                       |
| 2020 | ~-30%               | ~-45%                       |
| 2021 | ~-40%               | ~-35%                       |
| 2022 | ~45%                | ~-10%                       |
| 2023 | ~50%                | ~-5%                        |
| 2024 | ~35%                | ~-10%                       |
| 2025 | ~-15%               | ~-30%                       |
| 2026 | ~-5%                | ~-10%                       |
</details>

Source: JPM

Figure 4: Value stocks with moderate momentum (upside) effect as of 8 June  
1. Universe: MSXJP constituents. 2. Mechanically selected based on each name's factor loadings (as of last month-end). 3. We first select stocks in the top $50\%$ by Momentum factor loading (positive values only). From that subset, we choose the 30 names with the highest Value factor loading.

<table><tr><td>Code</td><td>Name</td><td>Sector(TSE33)</td><td>mkt cap (bn¥)</td><td>Price (¥)</td><td>3m Ret% (Absl)</td><td>12m Ret% (Absl)</td><td>3m Ret% (vs. TPX)</td><td>12m Ret% (vs. TPX)</td><td>Beta</td><td>P/E (12m fwd)</td><td>P/B (LTM)</td><td>ROE (LTM)</td><td>DivYld% (LTM)</td></tr><tr><td>9503</td><td>KANSAI ELEC PWR</td><td>Electric Power &amp; Gas</td><td>2,576</td><td>2,311</td><td>-10%</td><td>38%</td><td>-14%</td><td>1%</td><td>0.9</td><td>8.7</td><td>0.7</td><td>11.7</td><td>3.5</td></tr><tr><td>7259</td><td>AISIN CORP</td><td>Transportation Equipment</td><td>1,714</td><td>2,361</td><td>-3%</td><td>29%</td><td>-7%</td><td>-8%</td><td>1.1</td><td>9.8</td><td>0.8</td><td>8.2</td><td>3.2</td></tr><tr><td>5019</td><td>IDEMITSU KOSAN C</td><td>Oil &amp; Coal Products</td><td>1,650</td><td>1,349</td><td>-6%</td><td>51%</td><td>-10%</td><td>14%</td><td>0.8</td><td>10.3</td><td>0.9</td><td>9.4</td><td>2.7</td></tr><tr><td>8473</td><td>SBI HOLDINGS INC</td><td>Securities &amp; Commodity Futures</td><td>1,871</td><td>2,831</td><td>-6%</td><td>20%</td><td>-10%</td><td>-17%</td><td>1.3</td><td>8.7</td><td>1.0</td><td>28.0</td><td>3.4</td></tr><tr><td>7181</td><td>JAPAN POST INSUR</td><td>Insurance</td><td>1,623</td><td>1,455</td><td>-8%</td><td>33%</td><td>-12%</td><td>-5%</td><td>1.0</td><td>9.5</td><td>0.4</td><td>4.6</td><td>3.4</td></tr><tr><td>9502</td><td>CHUBU ELEC POWER</td><td>Electric Power &amp; Gas</td><td>2,028</td><td>2,675</td><td>6%</td><td>52%</td><td>1%</td><td>15%</td><td>0.6</td><td>11.2</td><td>0.6</td><td>7.7</td><td>2.6</td></tr><tr><td>9104</td><td>MITSUI OSK LINES</td><td>Marine Transportation</td><td>2,094</td><td>5,767</td><td>-8%</td><td>19%</td><td>-12%</td><td>-18%</td><td>0.8</td><td>10.7</td><td>0.7</td><td>7.7</td><td>3.6</td></tr><tr><td>8725</td><td>MS&amp;AD INSURANCE</td><td>Insurance</td><td>6,570</td><td>4,402</td><td>8%</td><td>35%</td><td>3%</td><td>-2%</td><td>1.2</td><td>9.2</td><td>1.3</td><td>18.0</td><td>3.2</td></tr><tr><td>8630</td><td>SOMPO HOLDINGS I</td><td>Insurance</td><td>5,598</td><td>5,992</td><td>1%</td><td>33%</td><td>-3%</td><td>-4%</td><td>1.2</td><td>10.0</td><td>1.0</td><td>13.7</td><td>3.3</td></tr><tr><td>5020</td><td>ENEOS HOLDINGS I</td><td>Oil &amp; Coal Products</td><td>3,383</td><td>1,250</td><td>-9%</td><td>70%</td><td>-13%</td><td>32%</td><td>1.1</td><td>9.9</td><td>1.0</td><td>8.0</td><td>2.7</td></tr><tr><td>8593</td><td>MITSUBISHI HC CA</td><td>Other Financing Business</td><td>1,905</td><td>1,299</td><td>-11%</td><td>24%</td><td>-15%</td><td>-14%</td><td>0.8</td><td>10.6</td><td>0.9</td><td>8.6</td><td>3.9</td></tr><tr><td>1605</td><td>INPEX CORP</td><td>Mining</td><td>4,585</td><td>3,641</td><td>-13%</td><td>69%</td><td>-17%</td><td>31%</td><td>0.8</td><td>9.0</td><td>0.9</td><td>7.9</td><td>3.0</td></tr><tr><td>9531</td><td>TOKYO GAS CO LTD</td><td>Electric Power &amp; Gas</td><td>2,114</td><td>6,311</td><td>-18%</td><td>30%</td><td>-22%</td><td>-7%</td><td>0.5</td><td>16.2</td><td>1.2</td><td>13.2</td><td>1.9</td></tr><tr><td>3003</td><td>HULIC CO LTD</td><td>Real Estate</td><td>1,288</td><td>1,677</td><td>-14%</td><td>13%</td><td>-19%</td><td>-24%</td><td>0.6</td><td>10.0</td><td>1.4</td><td>13.3</td><td>4.0</td></tr><tr><td>8750</td><td>DAIICHI LIFE GRO</td><td>Insurance</td><td>6,040</td><td>1,668</td><td>13%</td><td>52%</td><td>9%</td><td>15%</td><td>1.2</td><td>12.5</td><td>1.4</td><td>11.3</td><td>4.3</td></tr><tr><td>8601</td><td>DAIWA SECS GRP</td><td>Securities &amp; Commodity Futures</td><td>2,410</td><td>1,536</td><td>2%</td><td>51%</td><td>-2%</td><td>14%</td><td>1.2</td><td>12.4</td><td>1.2</td><td>10.3</td><td>4.2</td></tr><tr><td>8604</td><td>NOM HOLDINGS</td><td>Securities &amp; Commodity Futures</td><td>4,199</td><td>1,360</td><td>10%</td><td>48%</td><td>6%</td><td>11%</td><td>1.4</td><td>10.5</td><td>1.1</td><td>10.1</td><td>3.8</td></tr><tr><td>9107</td><td>KAWASAKI KISEN</td><td>Marine Transportation</td><td>1,728</td><td>2,703</td><td>0%</td><td>31%</td><td>-4%</td><td>-6%</td><td>1.0</td><td>15.4</td><td>0.9</td><td>7.7</td><td>4.4</td></tr><tr><td>6178</td><td>JAPAN POST HOLDI</td><td>Services</td><td>5,976</td><td>2,128</td><td>14%</td><td>58%</td><td>10%</td><td>21%</td><td>1.1</td><td>13.4</td><td>0.6</td><td>4.0</td><td>2.8</td></tr><tr><td>2503</td><td>KIRIN HOLDINGS C</td><td>Foods</td><td>2,155</td><td>2,642</td><td>0%</td><td>29%</td><td>-4%</td><td>-9%</td><td>0.4</td><td>12.2</td><td>1.6</td><td>12.4</td><td>2.9</td></tr><tr><td>9532</td><td>OSAKA GAS CO LTD</td><td>Electric Power &amp; Gas</td><td>2,195</td><td>5,516</td><td>-13%</td><td>48%</td><td>-17%</td><td>11%</td><td>0.6</td><td>14.4</td><td>1.2</td><td>8.7</td><td>2.4</td></tr><tr><td>5201</td><td>AGC INC</td><td>Glass &amp; Ceramics Products</td><td>1,569</td><td>7,214</td><td>20%</td><td>67%</td><td>16%</td><td>30%</td><td>0.9</td><td>17.0</td><td>1.0</td><td>6.0</td><td>2.9</td></tr><tr><td>3407</td><td>ASAHI KASEI CORP</td><td>Chemicals</td><td>2,385</td><td>1,746</td><td>2%</td><td>79%</td><td>-2%</td><td>42%</td><td>0.9</td><td>14.0</td><td>1.1</td><td>8.0</td><td>2.5</td></tr><tr><td>8309</td><td>SUMITOMO MITSUI</td><td>Banks</td><td>4,043</td><td>5,786</td><td>13%</td><td>51%</td><td>9%</td><td>14%</td><td>1.1</td><td>11.1</td><td>1.1</td><td>9.5</td><td>0.8</td></tr><tr><td>6326</td><td>KUBOTA CORP</td><td>Machinery</td><td>3,135</td><td>2,754</td><td>0%</td><td>71%</td><td>-5%</td><td>34%</td><td>1.0</td><td>13.5</td><td>1.2</td><td>8.6</td><td>1.9</td></tr><tr><td>4503</td><td>ASTELLAS PHARMA</td><td>Pharmaceutical</td><td>3,889</td><td>2,149</td><td>-13%</td><td>56%</td><td>-17%</td><td>19%</td><td>0.6</td><td>10.8</td><td>2.1</td><td>17.4</td><td>3.7</td></tr><tr><td>7912</td><td>DAI NIPPON PRINT</td><td>Other Products</td><td>1,155</td><td>2,628</td><td>-15%</td><td>22%</td><td>-19%</td><td>-15%</td><td>0.8</td><td>11.5</td><td>1.0</td><td>8.9</td><td>1.6</td></tr><tr><td>4188</td><td>MITSUBISHI CHEMI</td><td>Chemicals</td><td>1,490</td><td>1,034</td><td>7%</td><td>35%</td><td>2%</td><td>-2%</td><td>1.0</td><td>13.4</td><td>0.8</td><td>0.7</td><td>3.1</td></tr><tr><td>4507</td><td>SHIONOGI &amp; CO</td><td>Pharmaceutical</td><td>2,531</td><td>2,845</td><td>-18%</td><td>14%</td><td>-22%</td><td>-23%</td><td>0.6</td><td>10.5</td><td>1.4</td><td>13.5</td><td>2.7</td></tr><tr><td>1802</td><td>OBAYASHI CORP</td><td>Construction</td><td>2,125</td><td>3,071</td><td>-23%</td><td>37%</td><td>-28%</td><td>0%</td><td>0.9</td><td>13.1</td><td>1.7</td><td>14.4</td><td>3.1</td></tr></table>

Source: FactSet, JPM

## Market cycle (top down)

Japan QMI remained in Expansion territory in May. Against the backdrop of the global AI boom, real activity appears to have improved more than expected in sectors such as semiconductor production equipment and AI infrastructure. The negative impact of Middle East-related tensions, which we have been monitoring since March, has not yet appeared clearly in QMI.

Figure 5: Japan QMI since 2010  
![](images/8ee46e1b7ea6bd7569a88905c472dffac19f4d4ad09045410f88615ba6ff6e7d.jpg)

<details>
<summary>line chart</summary>

| Year | JPM Japan QMI (LHS) | Japan PMI Composite (Mfg+Non-mfg) |
|------|---------------------|-----------------------------------|
| 2010 | -4.0                | 1.0                               |
| 2012 | -1.0                | 2.0                               |
| 2014 | 3.0                 | 3.0                               |
| 2016 | -3.0                | 1.0                               |
| 2018 | 2.0                 | 2.0                               |
| 2020 | -8.0                | -1.0                              |
| 2022 | 4.0                 | 3.0                               |
| 2024 | 3.0                 | 2.0                               |
| 2026 | 5.0                 | 4.0                               |
</details>

Source: Bloomberg Finance L.P., MSCI Barra, JPM

Figure 6: Japan QMI State Positions for the Past 1 Year  
![](images/5e7cc2510bb9337f22a97847323857f3b9c74d4f5a7cb4af935a603cca4a9007.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["May-25"] --> B["Jun-25"]
  B --> C["Jul-25"]
  C --> D["Aug-25"]
  D --> E["Sep-25"]
  E --> F["Oct-25"]
  F --> G["Nov-25"]
  G --> H["Dec-25"]
  H --> I["Feb-26"]
  I --> J["Mar-26"]
  J --> K["May-26"]
    style A fill:#f9f,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
    style E fill:#f9f,stroke:#333
    style F fill:#f9f,stroke:#333
    style G fill:#f9f,stroke:#333
 

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 09 Jun 2026 08:35 AM JST

Disseminated 09 Jun 2026 08:35 AM JST
"""
