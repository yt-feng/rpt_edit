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
# VPEC (2455.TW): New equipment reflects strong orders; 3Q26 to ride on better InP substrate supply and capacity expansion; Buy

VPEC announced equipment procurement of NT\$653m (US\$20m) from Aixtron (MOCVD supplier), reflecting strong orders on hand and demand sustainability beyond 2027E, considering the lead time of MOCVD is now around 12 months. The continued investment in MOCVD reaffirms our positive view on VPEC, which is positioned to benefit from the AI server rack ramp up, optical networking specification upgrades across transmitters / CW lasers (toward 1.6T optical modules) and receivers (toward 200G PD), product expansion toward EML base epiwafers, further customer penetration for CW lasers, improving InP substrate supply, and opportunities in CPO (with customers placing R&D orders on InP epiwafers for 300mW CW lasers). Maintain Buy with TP at NT\$505 (implied 52.3x 2027E PE vs. 49% NI YoY in 2027-28E).

Exhibit 1: VPEC revenues by products and GM trend  
![](images/5761fe6ffb5113276953bc9b00cca3478ce23abed0f98b93a18f72ee81125564.jpg)  
Source: Company data, GS Global Investment Research

3-month revenue preview: VPEC delivered flat revenues QoQ in 1Q26 and 2Q26; however, we expect +23% QoQ in 3Q26 thanks to capacity expansion and better InP substrate supply, on the back of more customers carrying substrate, InP substrate suppliers' capacity expansion, and consecutive export permission received from the Chinese government. We expect VPEC to better capture strong AI data center demand in 3Q26, driving its Optoelectronics revenue contribution up to 41% (vs. 27% in 2Q26), leading to further GM expansion.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Yifan Hu
+852-2978-0996 | yifan.hu@gs.com
GS (Asia) L.L.C.

Exhibit 2: VPEC monthly revenue preview

<table><tr><td></td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>Jul-26 (E)</td><td>Aug-26 (E)</td><td>Sep-26 (E)</td><td>1Q26</td><td>2Q26</td><td>3Q26E</td></tr><tr><td>Rev (NT$m)</td><td>319</td><td>321</td><td>326</td><td>342</td><td>377</td><td>467</td><td>959</td><td>965</td><td>1,186</td></tr><tr><td>YoY</td><td>38%</td><td>47%</td><td>24%</td><td>18%</td><td>37%</td><td>35%</td><td>21%</td><td>35%</td><td>30%</td></tr><tr><td>MoM/QoQ</td><td>2%</td><td>1%</td><td>2%</td><td>5%</td><td>10%</td><td>24%</td><td>0%</td><td>1%</td><td>23%</td></tr><tr><td>GS (NT$m)</td><td>334</td><td>325</td><td>353</td><td></td><td></td><td></td><td>968</td><td>996</td><td></td></tr><tr><td>Actual vs. GS</td><td>-5%</td><td>-1%</td><td>-8%</td><td></td><td></td><td></td><td>-1%</td><td>-3%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

2Q26 net income in line: VPEC gross profits increased +2% QoQ in 2Q26, largely in line with our and Bloomberg consensus. The company's optoelectronics (mainly InP epiwafer for optical networking) carrying higher GM compared to microelectronics (mainly GaAs epiwafer for smartphone PA), while it continues to deliver blended GM expansion despite a less favorable product mix in 2Q26 vs. 4Q25, reflecting InP epiwafer ASP increase under strong demand. With better InP substrate supply going forward, we expect GM expansion to continue, along with product mix upgrade toward optoelectronics. Opex ratio remained high in 2Q26 at 15.4% (vs. 14.5% in 1Q26), given modest revenues QoQ and continuous R&D investments, leading OP income to decline 1% QoQ, or 11% / 10% below our / Bloomberg consensus. With strong revenues QoQ in 3Q26, we expect opex ratio to improve to 13%. With lower than expected tax rate, net income increased +9% QoQ in 2Q26, in line with our / Bloomberg consensus.

Exhibit 3: VPEC 2Q26 results snapshot

<table><tr><td>NT$m</td><td>2Q25</td><td>1Q26</td><td>2Q26</td><td>QoQ</td><td>YoY</td><td>GS</td><td>Act / GS</td><td>Cons.</td><td>Act / Cons.</td></tr><tr><td>Revenues</td><td>714</td><td>959</td><td>965</td><td>1%</td><td>35%</td><td>996</td><td>-3%</td><td>987</td><td>-2%</td></tr><tr><td>GP</td><td>246</td><td>365</td><td>373</td><td>2%</td><td>52%</td><td>386</td><td>-3%</td><td>394</td><td>-5%</td></tr><tr><td>OP</td><td>122</td><td>227</td><td>224</td><td>-1%</td><td>83%</td><td>252</td><td>-11%</td><td>248</td><td>-10%</td></tr><tr><td>Net income</td><td>36</td><td>195</td><td>214</td><td>9%</td><td>488%</td><td>212</td><td>1%</td><td>215</td><td>-1%</td></tr><tr><td colspan="6">Margins</td><td colspan="4"></td></tr><tr><td>GM</td><td>34.4%</td><td>38.1%</td><td>38.6%</td><td></td><td></td><td>38.7%</td><td></td><td>39.9%</td><td></td></tr><tr><td>OPM</td><td>17.1%</td><td>23.6%</td><td>23.2%</td><td></td><td></td><td>25.2%</td><td></td><td>25.1%</td><td></td></tr><tr><td>NM</td><td>5.1%</td><td>20.3%</td><td>22.1%</td><td></td><td></td><td>21.2%</td><td></td><td>21.8%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research, Bloomberg

Earnings revision: We raise net income by 2% / 3% in 2027 / 28E mainly on better optoelectronics, considering better InP substrate supply and the company's capacity expansion to better capture strong demand. We factor in 2Q26 results and keep our 2026E net income largely unchanged.

Exhibit 4: Earnings revision

<table><tr><td rowspan="2">NT$m</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td></tr><tr><td>Revenues</td><td>4,702</td><td>4,688</td><td>0%</td><td>6,473</td><td>6,532</td><td>1%</td><td>8,655</td><td>8,714</td><td>1%</td></tr><tr><td>GP</td><td>1,952</td><td>1,945</td><td>0%</td><td>2,918</td><td>2,965</td><td>2%</td><td>4,022</td><td>4,132</td><td>3%</td></tr><tr><td>OP</td><td>1,378</td><td>1,346</td><td>-2%</td><td>2,160</td><td>2,201</td><td>2%</td><td>3,056</td><td>3,133</td><td>3%</td></tr><tr><td>Net income</td><td>1,149</td><td>1,148</td><td>0%</td><td>1,779</td><td>1,811</td><td>2%</td><td>2,488</td><td>2,556</td><td>3%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>GM</td><td>41.5%</td><td>41.5%</td><td></td><td>45.1%</td><td>45.4%</td><td></td><td>46.5%</td><td>47.4%</td><td></td></tr><tr><td>OPM</td><td>29.3%</td><td>28.7%</td><td></td><td>33.4%</td><td>33.7%</td><td></td><td>35.3%</td><td>36.0%</td><td></td></tr><tr><td>NM</td><td>24.4%</td><td>24.5%</td><td></td><td>27.5%</td><td>27.7%</td><td></td><td>28.7%</td><td>29.3%</td><td></td></tr><tr><td>Opex ratio</td><td>12.2%</td><td>12.8%</td><td></td><td>11.7%</td><td>11.7%</td><td></td><td>11.2%</td><td>11.5%</td><td></td></tr></table>

Source: GS Global Investment Research

Compared to Bloomberg consensus, our net income is 13% / 7% higher in 2026 / 27E, mainly on higher revenues and GM, reflecting our positive view on its InP epiwafers for optical networking across transmitters / CW lasers and receivers, which we believe will continue to drive its product mix upgrade, GM expansion, and expanding the end

market exposure from consumer electronics to AI data centers.

Exhibit 5: GS vs. Bloomberg consensus

<table><tr><td rowspan="2">NT$m</td><td colspan="3">2026E</td><td colspan="3">2027E</td></tr><tr><td>GS</td><td>Cons.</td><td>Diff %</td><td>GS</td><td>Cons.</td><td>Diff %</td></tr><tr><td>Revenues</td><td>4,688</td><td>4,401</td><td>7%</td><td>6,532</td><td>6,185</td><td>6%</td></tr><tr><td>GP</td><td>1,945</td><td>1,811</td><td>7%</td><td>2,965</td><td>2,730</td><td>9%</td></tr><tr><td>OP</td><td>1,346</td><td>1,214</td><td>11%</td><td>2,201</td><td>2,064</td><td>7%</td></tr><tr><td>Net income</td><td>1,148</td><td>1,018</td><td>13%</td><td>1,811</td><td>1,692</td><td>7%</td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GM</td><td>41.5%</td><td>40.4%</td><td></td><td>45.4%</td><td>43.3%</td><td></td></tr><tr><td>OPM</td><td>28.7%</td><td>27.6%</td><td></td><td>33.7%</td><td>33.4%</td><td></td></tr><tr><td>NM</td><td>24.5%</td><td>23.1%</td><td></td><td>27.7%</td><td>27.4%</td><td></td></tr></table>

Source: GS Global Investment Research, Bloomberg

Exhibit 6: VPEC P&L

<table><tr><td>NT$ mn</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td colspan="8">Income statement</td><td colspan="8"></td></tr><tr><td>Revenue</td><td>2,604</td><td>2,694</td><td>3,241</td><td>3,380</td><td>4,688</td><td>6,532</td><td>8,714</td><td>794</td><td>714</td><td>913</td><td>960</td><td>959</td><td>965</td><td>1,186</td><td>1,577</td></tr><tr><td>Gross profit</td><td>1,089</td><td>1,109</td><td>1,279</td><td>1,220</td><td>1,945</td><td>2,965</td><td>4,132</td><td>317</td><td>246</td><td>300</td><td>358</td><td>365</td><td>373</td><td>486</td><td>721</td></tr><tr><td>OP income</td><td>580</td><td>542</td><td>721</td><td>669</td><td>1,346</td><td>2,201</td><td>3,133</td><td>179</td><td>122</td><td>159</td><td>209</td><td>227</td><td>224</td><td>333</td><td>563</td></tr><tr><td>Net income</td><td>545</td><td>450</td><td>671</td><td>548</td><td>1,148</td><td>1,811</td><td>2,556</td><td>157</td><td>36</td><td>160</td><td>194</td><td>195</td><td>214</td><td>276</td><td>463</td></tr><tr><td>EPS (NT$)</td><td>2.93</td><td>2.43</td><td>3.62</td><td>2.95</td><td>6.12</td><td>9.65</td><td>13.63</td><td>0.85</td><td>0.20</td><td>0.86</td><td>1.04</td><td>1.04</td><td>1.14</td><td>1.47</td><td>2.47</td></tr><tr><td colspan="8">Ratios</td><td colspan="8"></td></tr><tr><td>Opex ratio</td><td>19.6%</td><td>21.0%</td><td>17.2%</td><td>16.3%</td><td>12.8%</td><td>11.7%</td><td>11.5%</td><td>17.3%</td><td>17.3%</td><td>15.4%</td><td>15.5%</td><td>14.5%</td><td>15.4%</td><td>13.0%</td><td>10.0%</td></tr><tr><td>Tax rate</td><td>18.4%</td><td>16.9%</td><td>17.9%</td><td>17.9%</td><td>18.2%</td><td>19.9%</td><td>19.9%</td><td>20.0%</td><td>-48.8%</td><td>19.9%</td><td>21.2%</td><td>19.9%</td><td>9.8%</td><td>19.9%</td><td>19.9%</td></tr><tr><td colspan="8">Margins</td><td colspan="8"></td></tr><tr><td>Gross margin</td><td>41.8%</td><td>41.2%</td><td>39.5%</td><td>36.1%</td><td>41.5%</td><td>45.4%</td><td>47.4%</td><td>39.9%</td><td>34.4%</td><td>32.9%</td><td>37.3%</td><td>38.1%</td><td>38.6%</td><td>41.0%</td><td>45.7%</td></tr><tr><td>Operating margin</td><td>22.3%</td><td>20.1%</td><td>22.3%</td><td>19.8%</td><td>28.7%</td><td>33.7%</td><td>36.0%</td><td>22.6%</td><td>17.1%</td><td>17.4%</td><td>21.8%</td><td>23.6%</td><td>23.2%</td><td>28.0%</td><td>35.7%</td></tr><tr><td>Net margin</td><td>20.9%</td><td>16.7%</td><td>20.7%</td><td>16.2%</td><td>24.5%</td><td>27.7%</td><td>29.3%</td><td>19.8%</td><td>5.1%</td><td>17.6%</td><td>20.2%</td><td>20.3%</td><td>22.1%</td><td>23.3%</td><td>29.3%</td></tr><tr><td colspan="8">YoY</td><td colspan="8"></td></tr><tr><td>Revenue</td><td>-28%</td><td>3%</td><td>20%</td><td>4%</td><td>39%</td><td>39%</td><td>33%</td><td>-5%</td><td>-18%</td><td>13%</td><td>33%</td><td>21%</td><td>35%</td><td>30%</td><td>64%</td></tr><tr><td>Gross profit</td><td>-28%</td><td>2%</td><td>15%</td><td>-5%</td><td>59%</td><td>52%</td><td>39%</td><td>-7%</td><td>-29%</td><td>-9%</td><td>37%</td><td>15%</td><td>52%</td><td>62%</td><td>102%</td></tr><tr><td>OP income</td><td>-45%</td><td>-7%</td><td>33%</td><td>-7%</td><td>101%</td><td>63%</td><td>42%</td><td>-10%</td><td>-41%</td><td>-18%</td><td>71%</td><td>27%</td><td>83%</td><td>109%</td><td>169%</td></tr><tr><td>Net income</td><td>-36%</td><td>-17%</td><td>49%</td><td>-18%</td><td>109%</td><td>58%</td><td>41%</td><td>-18%</td><td>-82%</td><td>11%</td><td>46%</td><td>24%</td><td>488%</td><td>72%</td><td>139%</td></tr><tr><td colspan="8">QoQ</td><td colspan="8"></td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>10%</td><td>-10%</td><td>28%</td><td>5%</td><td>0%</td><td>1%</td><td>23%</td><td>33%</td></tr><tr><td>Gross profit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>22%</td><td>-22%</td><td>22%</td><td>19%</td><td>2%</td><td>2%</td><td>30%</td><td>48%</td></tr><tr><td>OP income</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>47%</td><td>-32%</td><td>30%</td><td>31%</td><td>8%</td><td>-1%</td><td>49%</td><td>69%</td></tr><tr><td>Net income</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>18%</td><td>-77%</td><td>342%</td><td>21%</td><td>1%</td><td>9%</td><td>29%</td><td>67%</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We continue to derive target price from 2029E discounted P/E back to 2027E via 10.5% COE (no change), and derive target PE multiple from peers' trading P/E vs. forward year fundamentals (NI YoY and OPM). Based on our updated 2029-30E NI YoY of 20% (vs. 13% previously) and 2029-30E OPM of 37% (vs. 35% previously), and peers' PEG&M of 0.3x (vs. 0.4x previously), we derive target PE multiple at 18.2x (vs. 19.6x previously), reflecting the sector de-rating under the AI server rack model transition and concerns on AI spending sustainability. Our new target price is at NT\$505 (vs. NT\$504 previously). Our new TP implied 2027E PE is at 52x, within the company's trading range (vs. peak at 74x, and +1stv. at 46x). Maintain Buy.

Exhibit 7: VPEC peers comparison

<table><tr><td>Ticker</td><td>Company</td><td>Rating</td><td>2027E P/E</td><td>2027-28E NI YoY</td><td>2027-28E OPM</td><td>Ratio</td></tr><tr><td>3081.TWO</td><td>LandMark</td><td>Buy</td><td>42.3</td><td>85%</td><td>48%</td><td>0.3</td></tr><tr><td>688498.SS</td><td>YJ Semi</td><td>Neutral</td><td>149.0</td><td>82%</td><td>51%</td><td>1.1</td></tr><tr><td>5802.JT</td><td>Sumitomo</td><td>Buy</td><td>15.1</td><td>22%</td><td>11%</td><td>0.5</td></tr><tr><td>LITE</td><td>Lumentum</td><td>NC</td><td>30.3</td><td>80%</td><td>41%</td><td>0.2</td></tr><tr><td>COHR</td><td>Coherent</td><td>NC</td><td>24.5</td><td>45%</td><td>24%</td><td>0.4</td></tr><tr><td>6503.JT</td><td>Mitsubishi</td><td>Buy</td><td>19.5</td><td>18%</td><td>11%</td><td>0.7</td></tr><tr><td>300502.SZ</td><td>Eoptolink</td><td>Buy</td><td>17.2</td><td>30%</td><td>47%</td><td>0.2</td></tr><tr><td colspan="2">Avg. (excl. outliers)</td><td></td><td>25.9</td><td>52%</td><td>34%</td><td>0.3</td></tr><tr><td></td><td></td><td></td><td>2029E P/E</td><td>2029-30E NI YoY</td><td>2029-30E OPM</td><td>PEG&amp;M</td></tr><tr><td>2455.TW</td><td>VPEC</td><td>Buy</td><td>18.2</td><td>20%</td><td>37%</td><td>0.3</td></tr></table>

Outliers are in grey. NC companies' estimates are from Bloomberg consensus. Price as of July 30, 2026.  
Source: Company data, GS Global Investment Research, Bloomberg

Exhibit 8: VPEC discounted PE

<table><tr><td>(NT$mn)</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>SiPh Rev contribution</td><td></td><td></td><td>1%</td><td>6%</td><td>23%</td><td>39%</td><td>49%</td><td></td><td></td></tr><tr><td>SiPh GP contribution</td><td></td><td></td><td>1%</td><td>8%</td><td>32%</td><td>49%</td><td>59%</td><td></td><td></td></tr><tr><td>Revenue</td><td>2,604</td><td>2,694</td><td>3,241</td><td>3,380</td><td>4,688</td><td>6,532</td><td>8,714</td><td>10,587</td><td>12,175</td></tr><tr><td>YoY</td><td>-28%</td><td>3%</td><td>20%</td><td>4%</td><td>39%</td><td>39%</td><td>33%</td><td>22%</td><td>15%</td></tr><tr><td>Gross margin</td><td>41.8%</td><td>41.2%</td><td>39.5%</td><td>36.1%</td><td>41.5%</td><td>45.4%</td><td>47.4%</td><td>47.9%</td><td>48.4%</td></tr><tr><td>Operating profit</td><td>580</td><td>542</td><td>721</td><td>669</td><td>1,346</td><td>2,201</td><td>3,133</td><t

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
