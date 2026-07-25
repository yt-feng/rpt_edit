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

<table><tr><td>Rmb m</td><td>1H25</td><td>2H25</td><td>1H26E</td><td>2H26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenues</td><td>1,567</td><td>2,192</td><td>2,107</td><td>4,287</td><td>1,552</td><td>2,384</td><td>3,758</td><td>6,394</td><td>10,735</td><td>18,996</td><td>24,856</td><td>28,444</td></tr><tr><td>COGS</td><td>543</td><td>790</td><td>825</td><td>1,529</td><td>457</td><td>542</td><td>1,333</td><td>2,354</td><td>3,681</td><td>7,138</td><td>9,631</td><td>11,053</td></tr><tr><td>Gross profits</td><td>1,024</td><td>1,402</td><td>1,282</td><td>2,758</td><td>1,094</td><td>1,841</td><td>2,426</td><td>4,040</td><td>7,053</td><td>11,858</td><td>15,225</td><td>17,391</td></tr><tr><td>Selling</td><td>272</td><td>360</td><td>286</td><td>378</td><td>327</td><td>410</td><td>632</td><td>664</td><td>431</td><td>367</td><td>385</td><td>420</td></tr><tr><td>G&amp;A</td><td>307</td><td>419</td><td>323</td><td>440</td><td>443</td><td>638</td><td>726</td><td>762</td><td>534</td><td>534</td><td>587</td><td>640</td></tr><tr><td>R&amp;D</td><td>2,300</td><td>2,854</td><td>2,760</td><td>3,424</td><td>2,366</td><td>3,156</td><td>5,154</td><td>6,184</td><td>6,679</td><td>6,793</td><td>7,200</td><td>7,917</td></tr><tr><td>Opex</td><td>2,879</td><td>3,632</td><td>3,368</td><td>4,242</td><td>3,137</td><td>4,204</td><td>6,512</td><td>7,610</td><td>7,644</td><td>7,693</td><td>8,172</td><td>8,976</td></tr><tr><td>OP income (EBIT)</td><td>(1,855)</td><td>(2,231)</td><td>(2,086)</td><td>(1,484)</td><td>(2,043)</td><td>(2,362)</td><td>(4,086)</td><td>(3,570)</td><td>(591)</td><td>4,165</td><td>7,053</td><td>8,415</td></tr><tr><td>Pretax income</td><td>(5,229)</td><td>(5,237)</td><td>3,599</td><td>(1,900)</td><td>(6,744)</td><td>2,351</td><td>(10,466)</td><td>1,699</td><td>(73)</td><td>4,786</td><td>7,532</td><td>8,950</td></tr><tr><td>Tax</td><td>(4)</td><td>7</td><td>4</td><td>(2)</td><td>(5)</td><td>5</td><td>3</td><td>2</td><td>(0)</td><td>5</td><td>8</td><td>9</td></tr><tr><td>Minority</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(0)</td><td>(1)</td><td>(1)</td><td>(1)</td><td>(1)</td><td>(1)</td></tr><tr><td>Net income to owners</td><td>(5,225)</td><td>(5,244)</td><td>3,596</td><td>(1,897)</td><td>(6,739)</td><td>2,347</td><td>(10,469)</td><td>1,698</td><td>(72)</td><td>4,781</td><td>7,525</td><td>8,941</td></tr><tr><td>Net income</td><td>(5,225)</td><td>(5,245)</td><td>3,595</td><td>(1,898)</td><td>(6,739)</td><td>2,347</td><td>(10,469)</td><td>1,698</td><td>(73)</td><td>4,781</td><td>7,524</td><td>8,941</td></tr><tr><td>EBIT</td><td>(1,855)</td><td>(2,231)</td><td>(2,086)</td><td>(1,484)</td><td>(2,043)</td><td>(2,362)</td><td>(4,086)</td><td>(3,570)</td><td>(591)</td><td>4,165</td><td>7,053</td><td>8,415</td></tr><tr><td>EBITDA</td><td>(1,609)</td><td>(1,984)</td><td>(1,842)</td><td>(1,241)</td><td>(1,738)</td><td>(1,982)</td><td>(3,593)</td><td>(3,083)</td><td>(70)</td><td>4,684</td><td>7,162</td><td>8,735</td></tr><tr><td colspan="13">Margins/ Ratios</td></tr><tr><td>GM</td><td>65.4%</td><td>64.0%</td><td>60.9%</td><td>64.3%</td><td>70.5%</td><td>77.3%</td><td>64.5%</td><td>63.2%</td><td>65.7%</td><td>62.4%</td><td>61.3%</td><td>61.1%</td></tr><tr><td>OP margin (EBIT margin)</td><td>-118.4%</td><td>-101.8%</td><td>-99.0%</td><td>-34.6%</td><td>-131.6%</td><td>-99.1%</td><td>-108.7%</td><td>-55.8%</td><td>-5.5%</td><td>21.9%</td><td>28.4%</td><td>29.6%</td></tr><tr><td>EBITDA margin</td><td>-102.7%</td><td>-90.5%</td><td>-87.4%</td><td>-28.9%</td><td>-112.0%</td><td>-83.2%</td><td>-95.6%</td><td>-48.2%</td><td>-0.7%</td><td>24.7%</td><td>28.8%</td><td>30.7%</td></tr><tr><td>Net margin (Attributed to owners)</td><td>-333.5%</td><td>-239.3%</td><td>170.6%</td><td>-44.3%</td><td>-434.3%</td><td>98.4%</td><td>-278.6%</td><td>26.6%</td><td>-0.7%</td><td>25.2%</td><td>30.3%</td><td>31.4%</td></tr><tr><td colspan="13">Ratios</td></tr><tr><td>Net margin</td><td>-333.5%</td><td>-239.3%</td><td>170.6%</td><td>-44.3%</td><td>-434.3%</td><td>98.4%</td><td>-278.6%</td><td>26.6%</td><td>-0.7%</td><td>25.2%</td><td>30.3%</td><td>31.4%</td></tr><tr><td>Selling ratio</td><td>17.4%</td><td>16.4%</td><td>13.6%</td><td>8.8%</td><td>21.1%</td><td>17.2%</td><td>16.8%</td><td>10.4%</td><td>4.0%</td><td>1.9%</td><td>1.5%</td><td>1.5%</td></tr><tr><td>G&amp;A ratio</td><td>19.6%</td><td>19.1%</td><td>15.3%</td><td>10.3%</td><td>28.6%</td><td>26.8%</td><td>19.3%</td><td>11.9%</td><td>5.0%</td><td>2.8%</td><td>2.4%</td><td>2.2%</td></tr><tr><td>R&amp;D ratio</td><td>146.8%</td><td>130.2%</td><td>131.0%</td><td>79.9%</td><td>152.5%</td><td>132.4%</td><td>137.1%</td><td>96.7%</td><td>62.2%</td><td>35.8%</td><td>29.0%</td><td>27.8%</td></tr><tr><td>Opex ratio</td><td>183.8%</td><td>165.7%</td><td>159.8%</td><td>99.0%</td><td>202.2%</td><td>176.4%</td><td>173.3%</td><td>119.0%</td><td>71.2%</td><td>40.5%</td><td>32.9%</td><td>31.6%</td></tr><tr><td>Tax rate</td><td>0.1%</td><td>-0.1%</td><td>0.1%</td><td>0.1%</td><td>0.1%</td><td>0.2%</td><td>0.0%</td><td>0.1%</td><td>0.1%</td><td>0.1%</td><td>0.1%</td><td>0.1%</td></tr><tr><td colspan="13">YoY</td></tr><tr><td>Revenues</td><td>68%</td><td>51%</td><td>34%</td><td>96%</td><td>71%</td><td>54%</td><td>58%</td><td>70%</td><td>68%</td><td>77%</td><td>31%</td><td>14%</td></tr><tr><td>Gross profits</td><td>39%</td><td>27%</td><td>25%</td><td>97%</td><td>74%</td><td>68%</td><td>32%</td><td>67%</td><td>75%</td><td>68%</td><td>28%</td><td>14%</td></tr></table>

Source: Company data, GS Global Investment Research

## Price Target Risks and Methodology - Horizon Robotics

Valuation: We derive our 12-month target price of HK\$13.14 based on a 2030E discounted EV/EBITDA multiple of 22.0x (using our estimate of the company's 2030E EBITDA), which is based on the correlation of EBITDA growth and trading EV/EBITDA of its peers. We then discount it back to 2027E using a COE of 11.5% (equity risk premium of 6.5%, risk free rate of 3.0%, and a beta of 1.3; similar to what we apply for our coverage).

Key downside risks: (1) fiercer-than-expected competition or auto supply chain pricing pressure amid slow demand, (2) slower-than-expected product mix upgrade toward AD, (3) slower-than-expected expansion in the customer base, and (4) supply chain risks amid geopolitical tensions.

<table><tr><td>9660.HK</td><td>12m Price Target: HK$13.14</td><td colspan="2">Price: HK$4.75</td><td colspan="2">Upside: 176.6%</td></tr><tr><td colspan="6"></td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="9">Market cap: HK$59.9bn / $7.6bn Enterprise value: HK$40.3bn / $5.1bn 3m ADTV: HK$1.0bn / $133.8mn China Greater China Technology M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: Yes</td><td>Revenue (Rmb mn) New</td><td>3,758.3</td><td>6,394.0</td><td>10,734.7</td><td>18,995.6</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>3,758.3</td><td>6,944.6</td><td>10,909.2</td><td>19,389.6</td></tr><tr><td>EBITDA (Rmb mn)</td><td>(3,593.4)</td><td>(3,083.3)</td><td>(70.3)</td><td>4,684.1</td></tr><tr><td>EPS (Rmb) New</td><td>(0.83)</td><td>0.13</td><td>(0.01)</td><td>0.37</td></tr><tr><td>EPS (Rmb) Old</td><td>(0.83)</td><td>(0.35)</td><td>(0.01)</td><td>0.37</td></tr><tr><td>P/E (X)</td><td>NM</td><td>31.2</td><td>NM</td><td>11.1</td></tr><tr><td>P/B (X)</td><td>6.8</td><td>3.7</td><td>3.7</td><td>2.8</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

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
