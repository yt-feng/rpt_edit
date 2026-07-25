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
# Horizon Robotics (9660.HK): HSD V2.0 launched with new models and enhanced experiences; 1H26 rev to up 25-35% YoY; Buy

Horizon Robotics announced 1H26 guidance with (1) revenues to grow at 25% - 35% YoY, or midpoint at Rmb20bn (-9% HoH, 30% YoY), outperformed China automotive market growth (EV shipment declined by 14% YoY), driven by the deployment of full-scenario NOA and comprehensive offerings across BPU and AI models, (2) adjusted net income at Rmb1.4bn loss to Rmb1.7bn loss (vs. 1H25 at Rmb1.3bn loss), and (3) net income at Rmb3.5bn to Rmb4.0bn gain. The differences between adjusted net income and net income is mainly the fair value change of the convertible loan issued to CARIAD in relation to Horizon Robotics' stock price fluctuations. In late Jun 2026, Horizon Robotics launched HSD (Horizon SuperDrive) V2.0 with 18 new features based on the World Model, also recently announced partnership with VW on the migration to L3/ L4, driving growth in 2H26 and 2027. Maintain Buy.

HSD V2.0 launched: The company released the new version of HSD (Horizon SuperDrive, V2.0) with Journey 6P platform in late Jun, which is based on the upgraded World Model and End-to-end model to enhance the vehicle responding speed, driving environment mgmt., parking experiences etc. The HSD V2.0 is available for Chery iCAR V27 with high adoption rate, and management notes the HSD solution benefits car models priced at Rmb100k\~200k to adopt urban NOA on vehicles.

Earnings revision: We factor in Horizon Robotics 1H26 guidance, and revise up 2026 NI to Rmb1.7bn (vs. previously at Rmb4.5bn net loss) mainly on higher than expected non-OP, due to fair value change of the convertible bond. We revise down revenues by 8%/ 2%/ 2% in 2026-28E on lower auto licenses revenues, and keep 2029-30E estimates largely unchanged.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Ting Song
+852-2978-6466 | ting.song@gs.com
GS (Asia) L.L.C.

Exhibit 1: Earnings revision

<table><tr><td rowspan="2">Rmb$m</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td><td colspan="3">2029E</td><td colspan="3">2030E</td></tr><tr><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td></tr><tr><td>Revenues</td><td>6,945</td><td>6,394</td><td>-8%</td><td>10,909</td><td>10,735</td><td>-2%</td><td>19,390</td><td>18,996</td><td>-2%</td><td>24,826</td><td>24,856</td><td>0%</td><td>28,387</td><td>28,444</td><td>0%</td></tr><tr><td>GP</td><td>4,524</td><td>4,040</td><td>-11%</td><td>7,144</td><td>7,053</td><td>-1%</td><td>12,063</td><td>11,858</td><td>-2%</td><td>15,210</td><td>15,225</td><td>0%</td><td>17,362</td><td>17,391</td><td>0%</td></tr><tr><td>OP</td><td>(3,087)</td><td>(3,570)</td><td>na</td><td>(500)</td><td>(591)</td><td>na</td><td>4,370</td><td>4,165</td><td>-5%</td><td>7,037</td><td>7,053</td><td>0%</td><td>8,386</td><td>8,415</td><td>0%</td></tr><tr><td>Net income</td><td>(4,512)</td><td>1,698</td><td>na</td><td>(80)</td><td>(72)</td><td>na</td><td>4,825</td><td>4,781</td><td>-1%</td><td>7,533</td><td>7,525</td><td>0%</td><td>8,960</td><td>8,941</td><td>0%</td></tr><tr><td>Adj. net income</td><td>(1,733)</td><td>(2,223)</td><td>na</td><td>(15)</td><td>(6)</td><td>na</td><td>5,056</td><td>5,012</td><td>-1%</td><td>7,836</td><td>7,827</td><td>0%</td><td>9,383</td><td>9,364</td><td>0%</td></tr><tr><td>EPS (Rmb, Diluted)</td><td>(0.35)</td><td>0.13</td><td>na</td><td>(0.01)</td><td>(0.01)</td><td>na</td><td>0.37</td><td>0.37</td><td>-1%</td><td>0.58</td><td>0.58</td><td>0%</td><td>0.69</td><td>0.69</td><td>0%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>GM</td><td>65.1%</td><td>63.2%</td><td>-2ppts</td><td>65.5%</td><td>65.7%</td><td>0ppts</td><td>62.2%</td><td>62.4%</td><td>0ppts</td><td>61.3%</td><td>61.3%</td><td>0ppts</td><td>61.2%</td><td>61.1%</td><td>0ppts</td></tr><tr><td>OPM</td><td>-44.4%</td><td>-55.8%</td><td>na</td><td>-4.6%</td><td>-5.5%</td><td>-1ppts</td><td>22.5%</td><td>21.9%</td><td>-1ppts</td><td>28.3%</td><td>28.4%</td><td>0ppts</td><td>29.5%</td><td>29.6%</td><td>0ppts</td></tr><tr><td>NM</td><td>-65.0%</td><td>26.6%</td><td>na</td><td>-0.7%</td><td>-0.7%</td><td>0ppts</td><td>24.9%</td><td>25.2%</td><td>0ppts</td><td>30.3%</td><td>30.3%</td><td>0ppts</td><td>31.6%</td><td>31.4%</td><td>0ppts</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We keep our 12m TP at HK\$13.14 (unchanged). Our valuation is based on 2030E EV/ EBITDA (unchanged), then discounting back to 2027E. Our target 2030E discounted EV/ EBITDA multiple at 22.0x (vs. previously at 23.1x) is derived from the correlation of EBITDA growth and trading EV/EBITDA multiples of peers, which captures the growth elements in fundamentals, based on the company's 2031E EBITDA growth. We then discount it back to 2027E using an unchanged COE of 11.5% (equity risk premium of 6.5%, risk free rate of 3.0%, and a beta of 1.3, unchanged). The implied 2027/ 28E EV/ Sales is at 12.9x/ 7.3x (vs. previously at 13.3x/ 7.5x). Maintain Buy.

Exhibit 2: Horizon Robotics discounted EV/ EBITDA

<table><tr><td>Rmb m</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td></tr><tr><td>Key assumptions</td><td colspan="2">Local leading supplier</td><td colspan="5">Market share gain with AD expansion</td><td colspan="3">License fees</td></tr><tr><td>ADAS &amp; AD China market share in value</td><td>2%</td><td>3%</td><td>4%</td><td>9%</td><td>16%</td><td>22%</td><td>37%</td><td rowspan="3" colspan="3"></td></tr><tr><td>AD chips (80+ TOPS) revenues exposure</td><td>3%</td><td>11%</td><td>10%</td><td>37%</td><td>44%</td><td>47%</td><td>59%</td></tr><tr><td>ADAS &amp; AD chipset revenues contribution</td><td>25%</td><td>29%</td><td>25%</td><td>41%</td><td>56%</td><td>60%</td><td>71%</td></tr><tr><td>Revenues</td><td>906</td><td>1,552</td><td>2,384</td><td>3,758</td><td>6,394</td><td>10,735</td><td>18,996</td><td>24,856</td><td>28,444</td><td>32,142</td></tr><tr><td>Rev YoY growth</td><td>94%</td><td>71%</td><td>54%</td><td>58%</td><td>70%</td><td>68%</td><td>77%</td><td>31%</td><td>14%</td><td>13%</td></tr><tr><td>GM</td><td>69.3%</td><td>70.5%</td><td>77.3%</td><td>64.5%</td><td>63.2%</td><td>65.7%</td><td>62.4%</td><td>61.3%</td><td>61.1%</td><td>61.1%</td></tr><tr><td>Opex</td><td>2,552</td><td>3,137</td><td>4,204</td><td>6,512</td><td>7,610</td><td>7,644</td><td>7,693</td><td>8,172</td><td>8,976</td><td>9,500</td></tr><tr><td>Opex ratio</td><td>282%</td><td>202%</td><td>176%</td><td>173%</td><td>119%</td><td>71%</td><td>40%</td><td>33%</td><td>32%</td><td>30%</td></tr><tr><td>EBIT</td><td>(1,925)</td><td>(2,043)</td><td>(2,362)</td><td>(4,086)</td><td>(3,570)</td><td>(591)</td><td>4,165</td><td>7,053</td><td>8,415</td><td>10,151</td></tr><tr><td>Adjusted OP</td><td></td><td>(1,687)</td><td>(1,495)</td><td>(2,372)</td><td>(1,667)</td><td>399</td><td>5,319</td><td>8,279</td><td>9,761</td><td>10,451</td></tr><tr><td>OP margin</td><td>-212.5%</td><td>-131.6%</td><td>-99.1%</td><td>-108.7%</td><td>-55.8%</td><td>-5.5%</td><td>21.9%</td><td>28.4%</td><td>29.6%</td><td>31.6%</td></tr><tr><td>EBITDA</td><td>(1,676)</td><td>(1,738)</td><td>(1,982)</td><td>(3,593)</td><td>(3,083)</td><td>(70)</td><td>4,684</td><td>7,162</td><td>8,735</td><td>10,401</td></tr><tr><td>EBITDA margin</td><td>-185.0%</td><td>-112.0%</td><td>-83.2%</td><td>-95.6%</td><td>-48.2%</td><td>-0.7%</td><td>24.7%</td><td>28.8%</td><td>30.7%</td><td>32.4%</td></tr><tr><td>Non-OP</td><td>(6,800)</td><td>(4,702)</td><td>4,713</td><td>(6,380)</td><td>5,269</td><td>518</td><td>621</td><td>479</td><td>535</td><td>555</td></tr><tr><td>Pre tax income</td><td>(8,725)</td><td>(6,744)</td><td>2,351</td><td>(10,466)</td><td>1,699</td><td>(73)</td><td>4,786</td><td>7,532</td><td>8,950</td><td>10,706</td></tr><tr><td>Tax</td><td>(4)</td><td>(5)</td><td>5</td><td>3</td><td>2</td><td>(0)</td><td>5</td><td>8</td><td>9</td><td>9</td></tr><tr><td>Net income (Attributed to owners)</td><td>(8,719)</td><td>(6,739)</td><td>2,347</td><td>(10,469)</td><td>1,698</td><td>(72)</td><td>4,781</td><td>7,525</td><td>8,941</td><td>10,697</td></tr><tr><td>Adjusted NI</td><td></td><td>(1,635)</td><td>(1,681)</td><td>(2,812)</td><td>(2,223)</td><td>(6)</td><td>5,012</td><td>7,827</td><td>9,364</td><td>11,047</td></tr><tr><td>NI YoY</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>57%</td><td>19%</td><td>20%</td></tr><tr><td>EPS (Rmb)</td><td></td><td>(2.50)</td><td>0.17</td><td>(0.83)</td><td>0.13</td><td>(0.01)</td><td>0.37</td><td>0.58</td><td>0.69</td><td>0.83</td></tr><tr><td>Target EV/ EBITDA</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>22.0</td><td></td></tr><tr><td>Target multiple x 2030 EBITDA (Rmb m)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>192,257</td><td></td></tr><tr><td>Enterprise value (2027E, Rmb m)</td><td></td><td></td><td></td><td></td><td></td><td>138,881</td><td></td><td></td><td></td><td></td></tr><tr><td>Cash and equivalents (2027E, Rmb m)</td><td></td><td></td><td></td><td></td><td></td><td>17,378</td><td></td><td></td><td></td><td></td></tr><tr><td>Debt (2027E, Rmb m)</td><td></td><td></td><td></td><td></td><td></td><td>508</td><td></td><td></td><td></td><td></td></tr><tr><td>Fwd equity valuation (Rmb m, 2027E)</td><td></td><td></td><td></td><td></td><td></td><td>155,751</td><td></td><td></td><td></td><td></td></tr><tr><td>Fwd equity valuation (US$ m, 2027E)</td><td></td><td></td><td></td><td></td><td></td><td>21,336</td><td></td><td></td><td></td><td></td></tr><tr><td>Target price (HKD$, 2027E)</td><td></td><td></td><td></td><td></td><td></td><td>13.14</td><td></td><td></td><td></td><td></td></tr><tr><td>Implied P/E</td><td></td><td></td><td></td><td></td><td></td><td></td><td>38.7</td><td>24.6</td><td>20.7</td><td>17.3</td></tr><tr><td>Implied EV/Sales</td><td></td><td></td><td></td><td></td><td>21.7</td><td>12.9</td><td>7.3</td><td>5.6</td><td>4.9</td><td>4.3</td></tr></table>

Source: Datastream

<table><tr><td colspan="2">COE assumption</td></tr><tr><td>Beta</td><td>1.3</td></tr><tr><td>Risk free</td><td>3.0%</td></tr><tr><td>Market risk premium</td><td>6.5%</td></tr><tr><td>COE</td><td>11.5%</td></tr></table>

Exhibit 3: The target multiple is derived from peers EV/EBITDA and EBITDA growth  
![](images/d972eb6e5e3e2d51a14ea207178a3694859222ec326803e944e33564c0ff1c2b.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: Horizon Robotics 12M forward P/S  
![](images/36762742fe5d4e8f3bb3546c28ed7896a3b684c4f6fd67556a45fafad41c8c71.jpg)  
Source: Eikon Datastream

Exhibit 5: Horizon Robotics P&L Summary

<table><tr><td>Rmb m</td><td>1H25</td><td>2H25</td><td>1H26E</td><td>2H26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenues</td><td>1,567</td><td>2,192</td><td>2,107</td><td>4,287</td><td>1,552</td><td>2,384</td><td>3,758</td><td>6,394</td><td>10,735</td><td>18,996</td><td>24,856</td><td>28,444</td></tr><tr><td>COGS</td><td>543</td><td>790</td><td>825</td><td>1,529</td><td>457</td><td>542</td><td>1,333</td><td>2,354</td><td>3,681</td><td>7,138</td><td>9,631</td><td>11,053</td></tr><tr><td>Gross profits</td><td>1,024</td><td>1,402</td><td>1,282</td><td>2,758</td><td>1,094</td><td>1,841</td><td>2,426</td><td>4,040</td><td>7,053</td><td>11,858</td><td>15,225</td><td>17,391</td></tr><tr><td>Selling</td><td>272</td><td>360</td><td>286</td><td>378</td><td>327</td><td>410</td><td>632</td><td>664</td><td>431</td><td>367</td><td>385</td><td>420</td></tr><tr><td>G&amp;A</td><td>307</td><td>419</td><td>323</td><td>440</td><td>443</td><td>638</td><td>726</td><td>762</td><td>534</td><td>534</td><td>587</td><td>640</td></tr><tr><td>R&amp;D</td><td>2,300</td><td>2,854</td><td>2,760</td><td>3,424</td><td>2,366</td><td>3,156</td><td>5,154</td><td>6,184</td><td>6,679</td><td>6,793</td><td>7,200</td><td>7,917</td></tr><tr><td>Opex</td><td>2,879</td><td>3,632</td><td>3,368</td><td>4,242</td><td>3,137</td><td>4,204</td><td>6,512</td><td>7,610</td><td>7,644</td><td>7,693</td><td>8,172</td><td>8,976</td></tr><tr><td>OP income (EBIT)</td><td>(1,855)</td><td>(2,231)</td><td>(2,086)</td><td>(1,484)</td><td>(2,043)</td><td>(2,362)</td><td>(4,086)</td><td>(3,570)</td><td>(591)</td><td>4,165</td><td>7,053</td><td>8,415</td></tr><tr><td>Pretax income</td><td>(5,229)</td><td>(5,237)</td><td>3,599</td><td>(1,900)</td><td>(6,744)</td><td>2,351</td><td>(10,466)</td><td>1,699</td><td>(73)</td><td>4,786</td><td>7,532</td><td>8,950</td></tr><tr><td>Tax</td><td>(4)</td><td>7</td><td>4</td><td>(2)</td><td>(5)</td><td>5</td><td>3</td><td>2</td><td>(0)</td><td>5</td><td>8</td><td>9</td></tr><tr><td>Minority</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(1)</td><td>(1)</td><td>(1)</td><td>(1)</td><td>(1)</td></tr><tr><td>Net income to owners</td><td>(5,225)</td><td>(5,244)</td><td>3,596</td><td>(1,897)</td><td>(6,739)</td><td>2,347</td><td>(10,469)</td><td>1,698</td><td>(72)</td><td>4,781</td><td>7,525</td><td>8,941</td></tr><tr><td>Net income</td><td>(5,225)</td><td>(5,245)</td><td>3,595</td><td>(1,898)</td><td>(6,739)</td><td>2,347</td><td>(10,469)</td><td>1,698</td><td>(73)</td><td>4,781</td><td>7,524</td><td>8,941</td></tr><tr><td>EBIT</td><td>(1,855)</td><td>(2,231)</td><td>(2,086)</td><td>(1,484)</td><td>(2,043)</td><td>(2,362)</td><td>(4,086)</td><td>(3,570)</td><td>(591)</td><td>4,165</td><td>7,053</td><td>8,415</td></tr><tr><td>EBITDA</td><td>(1,609)</td><td>(1,984)</td><td>(1,842)</td><td>(1,241)</td><td>(1,738)</td><td>(1,982)</td><td>(3,593)</td><td>(3,083)</td><td>(70)</td><td>4,684</td><td>7,162</td><td>8,735</td></tr><tr><td colspan="13">Margins/ Ratios</td></tr><tr><td>GM</td><td>65.4%</td><td>64.0%</td><td>60.9%</td><td>64.3%</td><td>70.5%</td><td>77.3%</td><td>64.5%</td><td>63.2%</td><td>65.7%</td><td>62.4%</td><td>61.3%</td><td>61.1%</td></tr><tr><td>OP margin (EBIT margin)</td><td>-118.4%</td><td>-101.8%</td><td>-99.0%</td><td>-34.6%</td><td>-131.6%</td><td>-99.1%</td><td>-108.7%</td><td>-55.8%</td><td>-5.5%</td><td>21.9%</td><td>28.4%</td><td>29.6%</td></tr><tr><td>EBITDA margin</td><td>-102.7%</td><td>-90.5%</td><td>-87.4%</td><td>-28.9%</td><td>-112.0%</td><td>-83.2%</td><td>-95.6%</td><td>-48.2%</td><td>-0.7%</td><td>24.7%</td><td>28.8%</td><td>30.7%</td></tr><tr><td>Net margin (Attributed to owners)</td><td>-333.5%</td><td>-239.3%</td><td>170.6%</td><td>-44.3%</td><td>-434.3%</td><td>98.4%</td><td>-278.6%</td><td>26.6%</td><td>-0.7%</td><td>25.2%</td><td>30.3%</td><td>31.4%</td></tr><tr><td colspan="13">Ratios</td></tr><tr><td>Net margin</td><td>-333.5%</td><td>-239.3%</td><td>170.6%</td><td>-44.3%</td><td>-434.3%</td><td>98.4%</td><td>-278.6%</td><td>26.6%</td><td>-0.7%</td><td>25.2%</td><td>30.3%</td><td>31.4%</td></tr><tr><td>Selling ratio</td><td>17.4%</td><td>16.4%</td><td>13.6%</td><td>8.8%</td><td>21.1%</td><td>17.2%</td><td>16.8%</td><td>10.4%</td><td>4.0%</td><td>1.9%</td><td>1.5%</td><td>1.5%</td></tr><tr><td>G&amp;A ratio</td><td>19.6%</td><td>19.1%</td><td>15.3%</td><td>10.3%</td><td>28.6%</td><td>26.8%</td><td>19.3%</td><td>11.9%</td><td>5.0%</td><td>2.8%</td><td>2.4%</td><td>2.2%</td></tr><tr><td>R&amp;D ratio</td><td>146.8%</td><td>130.2%</td><td>131.0%</td><td>79.9%</td><td>152.5%</td><td>132.4%</td><td>137.1%</td><td>96.7%</td><td>62.2%</td><td>35.8%</td><td>29.0%</td><td>27.8%</td

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or

finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
