你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Shandong Sinocera - A

## There is no alternative – Buy the upside optionality; Strong momentum of MLCC chain; AI-grade capacity to ramp up

Sinocera is the only A-share listed domestic MLCC ceramic powder supplier. Its share price has rallied 102% since 27 May, vs SZCOMP Index up 1%, due to continued competitor price hikes across electronic materials and rising expectations for potential good news of MLCC price hike penetration through upstream players (manufacturers and distributors) to the downstream (materials suppliers). However, we note that the majority of investors remain skeptical and uninvested in Sinocera, preferring more obvious pure plays of MLCC component and PCB chain companies, which on average have seen their share prices rise +315% YTD (vs Sinocera +261%/SZCOMP Index +13%). High-end MLCC powder capacity ramp-up and potential PCB new orders in 2027 might be the multi-driver catalysts. We raise our 2027/28E EPS by 21%/29% to reflect recent MLCC price hikes and higher AI-grade product mix (JPMe high-end MLCC now >35% of segmental revenue by 2027, vs negligible in 1H26), and our price target to a Street high of Rmb136 (based on 93x P/E, Rmb1.46 2028E EPS).

\- Good progress on AI-grade MLCC powder capacity expansion. Sinocera currently operates 10,000 tons of standard MLCC powder capacity and is actively expanding high-end capacity dedicated to AI servers and automotive-grade applications, targeting 5,000 tons – of which 2,000 tons were commissioned by YE25 and the remaining 3,000 tons are expected by YE26. The company is one of the few domestic players mastering hydrothermal barium titanate core technology and capable of mass-producing high-end powders with particle sizes of 50-100 nm, successfully breaking the long-standing dominance of global suppliers in the high-end segment. In 2025, the company produced approximately 7,000 tons of MLCC powder, in line with market expectations. Looking ahead, Sinocera is advancing stable, large-scale supply of high-end MLCC powders to major customers including Samsung, Fenghua, and Yageo.

\- Price upside may be greater than market expectations. In Mar-May 2026, downstream MLCC manufacturers Murata and Samsung Electromechanics raised high-end MLCC prices by 10-35%, and upstream dielectric powder prices followed with 10-15% increases. Price tiers are clearly differentiated: standard consumer-grade powder at Rmb60k-70k/ton with a gross margin of c.33%, automotive-grade powder at Rmb80k-90k/ton, and AI server high-capacitance powder above Rmb100k/ton with a GM of 45-50%. The price hikes were driven by three factors: AI server demand (single rack MLCC usage is 15× that of traditional servers), automotive electronics growth, and potential supply constraints on global competitors due to China's tightened heavy rare earth export controls. Sinocera's 4Q25 contract liabilities surged to Rmb56mn, up 216% q/q, and 1Q26 remained at a high of Rmb40mn, partially confirming strong orders.

## Overweight

300285.SZ, 300285 CH
Price (01 Jul 26): Rmb98.82

▲ Price Target (Dec-27): Rmb136.00
Prior (Jun-27): Rmb60.40

## China

Asia Oils
Lei Mu AC
(86-21) 6106 6319
lei.mu@JPM.com
SAC Registration Number: S1730521050002
JPM Securities (China) Company Limited

## Key Changes (FYE Dec)

<table><tr><td></td><td>Prev</td><td>Cur</td><td> $\Delta$ </td></tr><tr><td>Adj. EPS - 27E (Rmb)</td><td>0.99</td><td>1.20</td><td>21.5%</td></tr></table>

Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>91</td><td>84</td><td>82</td><td>93</td><td>92</td></tr><tr><td>Growth</td><td>17</td><td>53</td><td>34</td><td>45</td><td>29</td></tr><tr><td>Momentum</td><td>14</td><td>43</td><td>63</td><td>71</td><td>34</td></tr><tr><td>Quality</td><td>9</td><td>56</td><td>41</td><td>34</td><td>29</td></tr><tr><td>Low Vol</td><td>76</td><td>57</td><td>57</td><td>40</td><td>62</td></tr></table>

\- Ceramic substrate broadening opportunities. Through subsidiary Sinocera Saichuang, Sinocera has established leading technical capabilities in substrate metallization via ‘powder + ceramic + metallization’ integration. LED ceramic substrates have achieved stable bulk supply to global tier customers. Communication RF microsystem chip packaging enclosures have become the mainstream packaging solution for low-orbit satellite RF chips, with revenue growing rapidly in 2025 and a Rmb100mn order signed in June 2025 expected to complete by 1H26. For optical module ceramic substrates, Thermoelectric Cooler (TEC) products have achieved small-batch sales with some customers while new customer qualification is ongoing. The PCB ceramic substrate testing with a major customer is ongoing, and the company expects meaningful progress and new orders to kick-in by 2027. The company is also developing laser thermal sinks, microwave capacitors, ferrite magnetic devices, and other new products. Phase II new plant construction has been completed, with capacity gradually ramping up.

\- Raise FY27/28 EPS by 21%/30% and PT to new Street-high of Rmb136. We raise our FY27/28E EPS to reflect improved product mix, margins and volume, as well as upward revisions to consensus expectations for AI-related products in next 2+ years. Our FY27/28 EPS is now 20%/22% above the Street. We now forecast MLCC powder business to account for 25%/28% of total gross profit by FY27/28 (previously 16%/18%). The improved product mix would result in electronic materials segmental gross margin reaching historically high levels of 50% in FY27E/28E, versus the previous peak of 49.9% in FY18. Our revised Dec-27 PT of Rmb136 is based on 93x one-year forward P/E (previously 60x) to reflect the aforementioned positives of AI-related businesses. Our revised PT of Rmb136 implies 88x/72x 2027/28E P/E, versus its industry peers at 99x/82x of 2027/28E P/E, based on market estimates.

Price Performance  
![](images/4b98af60de2599f129d10a92db66c7a1256262ed8198780992c3943c93475ee2.jpg)

— 300285.SZ Price (Rmb) SHCOMP (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>260.5%</td><td>91.5%</td><td>214.9%</td><td>473.9%</td></tr><tr><td>Rel</td><td>256.9%</td><td>90.2%</td><td>210.8%</td><td>454.9%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>1,004</td></tr><tr><td>52-week range (Rmb)</td><td>112.88-16.90</td></tr><tr><td>Market cap ($ mn)</td><td>14,615</td></tr><tr><td>Exchange rate</td><td>6.79</td></tr><tr><td>Free float (%)</td><td>67.6%</td></tr><tr><td>3M ADV (mn)</td><td>86.02</td></tr><tr><td>3M ADV ($ mn)</td><td>761.6</td></tr><tr><td>Volatility (90 Day)</td><td>90</td></tr><tr><td>Index</td><td>SSE</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>16|3|0</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>Rmb in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>4,583</td><td>5,717</td><td>6,800</td><td>7,737</td></tr><tr><td>Adj. EBITDA</td><td>1,202</td><td>1,475</td><td>1,888</td><td>2,193</td></tr><tr><td>Adj. EBIT</td><td>874</td><td>1,173</td><td>1,573</td><td>1,866</td></tr><tr><td>Adj. net income</td><td>610</td><td>847</td><td>1,200</td><td>1,458</td></tr><tr><td>Adj. EPS</td><td>0.61</td><td>0.85</td><td>1.20</td><td>1.46</td></tr><tr><td>BBG EPS</td><td>0.67</td><td>0.82</td><td>1.02</td><td>1.22</td></tr><tr><td>Cashflow from operations</td><td>804</td><td>879</td><td>1,140</td><td>1,467</td></tr><tr><td>FCFF</td><td>405</td><td>466</td><td>718</td><td>1,036</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>13.2%</td><td>24.8%</td><td>18.9%</td><td>13.8%</td></tr><tr><td>EBITDA margin</td><td>26.2%</td><td>25.8%</td><td>27.8%</td><td>28.3%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>6.1%</td><td>22.7%</td><td>28.0%</td><td>16.2%</td></tr><tr><td>EBIT margin</td><td>19.1%</td><td>20.5%</td><td>23.1%</td><td>24.1%</td></tr><tr><td>Net margin</td><td>13.3%</td><td>14.8%</td><td>17.6%</td><td>18.8%</td></tr><tr><td>Adj. EPS growth</td><td>1.3%</td><td>38.8%</td><td>41.6%</td><td>21.5%</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>11.8%</td><td>11.8%</td><td>11.8%</td><td>11.8%</td></tr><tr><td>Interest cover</td><td>235.2</td><td>288.6</td><td>369.4</td><td>429.1</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROCE</td><td>10.5%</td><td>13.0%</td><td>15.8%</td><td>16.7%</td></tr><tr><td>ROE</td><td>8.8%</td><td>11.3%</td><td>14.4%</td><td>15.5%</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>0.4%</td><td>0.5%</td><td>0.7%</td><td>1.1%</td></tr><tr><td>Dividend yield</td><td>0.2%</td><td>0.2%</td><td>0.2%</td><td>0.3%</td></tr><tr><td>EV/Revenue</td><td>23.2</td><td>18.5</td><td>15.5</td><td>13.5</td></tr><tr><td>EV/EBITDA</td><td>88.3</td><td>71.8</td><td>55.9</td><td>47.8</td></tr><tr><td>Adj. P/E</td><td>161.4</td><td>116.3</td><td>82.1</td><td>67.6</td></tr></table>

## Summary Investment Thesis and Valuation

Sinocera is China's leading integrated and platform-style ceramic (functional) manufacturer. Its business includes four key ceramic material segments: electronic (MLCC powder), catalyst (honeycomb), biomedical (dental/denture) and others (ball bearing and ink). Our OW rating is based on: 1) Sinocera being the #1 MLCC powder producer in China, with new capacity expansion completed and efforts ongoing to break into the market for higher-end products; 2) A sustainable honeycomb ceramic demand outlook, with the potential to gain market share from global major suppliers; 3) A positive outlook for dental material demand in China with integrated industrial chain development; and 4) Strong demand upside for new materials and products in the China semiconductor industries. We believe Sinocera will maintain its growth momentum in both earnings and operations over the next three years.

Our Dec-27 price target of Rmb136 is based on a 93x one-year forward P/E, an historically high level. Sinocera's current valuation is at the record high of 113x; the historical forward P/E multiple range is 17x-113x, with an average of 35x.

Performance Drivers  
![](images/50671efdb01a3e1d60ad770dfa67900cb7dfef188712ccdfcf7692dcfb7b078d.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>0.24</td><td>0.29</td></tr><tr><td>Region: China</td><td>-0.15</td><td>-0.05</td></tr><tr><td colspan="3">Macro:</td></tr><tr><td>Generic 1st &#x27;CO&#x27; Future</td><td>0.34</td><td>0.24</td></tr><tr><td>JPM Global Equity Sentiment</td><td>0.57</td><td>0.23</td></tr><tr><td>JPM China A-shares Sentiment</td><td>0.24</td><td>0.18</td></tr><tr><td colspan="3">Quant Styles:</td></tr><tr><td>DivYld</td><td>-0.56</td><td>-0.51</td></tr><tr><td>Value</td><td>-0.56</td><td>-0.46</td></tr><tr><td>Growth</td><td>0.43</td><td>0.36</td></tr></table>

Figure 1: China dental hospitals & clinics  
![](images/7b070c5226fe1a386d72e34aced15365179b326975041861a0d3440dd5372cc8.jpg)  
Source: Sinocera FY25 Annual report, as of 21 April 2026, JPM estimates.

Figure 2: TAM of China dental implant industry (Rmb 100Mn)  
![](images/e9783da7f9d7dcaaff51afdf990b0a512d78ead9f009d4119eb2879618321203.jpg)  
Source: Sinocera FY25 Annual report, as of 21 April 2026, JPM estimates.

Table 1: JPM earnings revisions for Sinocera

<table><tr><td rowspan="2">RMB Mn</td><td colspan="3">JPMe Previous</td><td colspan="3">JPMe Current</td><td colspan="3">Change</td><td colspan="3">Consensus</td><td colspan="3">JPMe vs. Consensus (%)</td></tr><tr><td>26E</td><td>27E</td><td>28E</td><td>26E</td><td>27E</td><td>28E</td><td>26E</td><td>27E</td><td>28E</td><td>26E</td><td>27E</td><td>28E</td><td>26E</td><td>27E</td><td>28E</td></tr><tr><td>Revenue</td><td>5,682</td><td>6,452</td><td>7,203</td><td>5,717</td><td>6,800</td><td>7,737</td><td>1%</td><td>5%</td><td>7%</td><td>5,395</td><td>6,384</td><td>7,594</td><td>6%</td><td>7%</td><td>2%</td></tr><tr><td>COGS</td><td>(3,469)</td><td>(3,948)</td><td>(4,419)</td><td>(3,491)</td><td>(3,988)</td><td>(4,483)</td><td>1%</td><td>1%</td><td>1%</td><td>(3,319)</td><td>(3,892)</td><td>(4,603)</td><td>5%</td><td>2%</td><td>-3%</td></tr><tr><td>Gross Profit</td><td>2,213</td><td>2,504</td><td>2,785</td><td>2,226</td><td>2,812</td><td>3,254</td><td>1%</td><td>12%</td><td>17%</td><td>2,076</td><td>2,492</td><td>2,991</td><td>7%</td><td>13%</td><td>9%</td></tr><tr><td>Operating Profit</td><td>1,167</td><td>1,332</td><td>1,497</td><td>1,173</td><td>1,573</td><td>1,866</td><td>1%</td><td>18%</td><td>25%</td><td>1,030</td><td>1,272</td><td>1,514</td><td>14%</td><td>24%</td><td>23%</td></tr><tr><td>EBITDA</td><td>1,469</td><td>1,647</td><td>1,824</td><td>1,475</td><td>1,888</td><td>2,193</td><td>0%</td><td>15%</td><td>20%</td><td>1,336</td><td>1,586</td><td>1,818</td><td>10%</td><td>19%</td><td>21%</td></tr><tr><td>Pre-Tax Profit</td><td>1,023</td><td>1,188</td><td>1,353</td><td>1,029</td><td>1,429</td><td>1,722</td><td>1%</td><td>20%</td><td>27%</td><td>1,017</td><td>1,262</td><td>1,514</td><td>1%</td><td>13%</td><td>14%</td></tr><tr><td>Net Income*</td><td>842</td><td>987</td><td>1,133</td><td>847</td><td>1,200</td><td>1,458</td><td>1%</td><td>22%</td><td>29%</td><td>811</td><td>1,003</td><td>1,214</td><td>4%</td><td>20%</td><td>20%</td></tr><tr><td>EPS</td><td>0.84</td><td>0.99</td><td>1.14</td><td>0.85</td><td>1.20</td><td>1.46</td><td>1%</td><td>22%</td><td>28%</td><td>0.82</td><td>1.01</td><td>1.22</td><td>4%</td><td>19%</td><td>20%</td></tr><tr><td>DPS</td><td>0.15</td><td>0.18</td><td>0.20</td><td>0.15</td><td>0.22</td><td>0.26</td><td>2%</td><td>20%</td><td>32%</td><td>0.16</td><td>0.19</td><td>0.23</td><td>-1%</td><td>12%</td><td>17%</td></tr><tr><td>Gross margin (%)</td><td>38.9%</td><td>38.8%</td><td>38.7%</td><td>38.9%</td><td>41.4%</td><td>42.1%</td><td>0.0pp</td><td>2.6pp</td><td>3.4pp</td><td>38.5%</td><td>39.0%</td><td>39.4%</td><td>0.5pp</td><td>2.3pp</td><td>2.7pp</td></tr><tr><td>ROE (%)</td><td>11.2%</td><td>12.0%</td><td>12.4%</td><td>11.3%</td><td>14.4%</td><td>15.5%</td><td>0.1pp</td><td>2.4pp</td><td>3.1pp</td><td>10.7%</td><td>11.8%</td><td>12.8%</td><td>0.6pp</td><td>2.6pp</td><td>2.6pp</td></tr><tr><td>ROA (%)</td><td>8.0%</td><td>8.5%</td><td>8.9%</td><td>8.0%</td><td>10.2%</td><td>11.0%</td><td>0.0pp</td><td>1.7pp</td><td>2.1pp</td><td>8.3%</td><td>9.1%</td><td>10.2%</td><td>-0.2pp</td><td>1.0pp</td><td>0.8pp</td></tr></table>

Source: JPM estimates, Bloomberg Finance L.P. Priced on 30 June 2026.

Table 2: P/E Valuation – JPMe estimates vs Consensus for ceramic-linked stocks

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">JPM rating</td><td rowspan="2">Price Currency</td><td rowspan="2">Last price</td><td rowspan="2">Mkt cap ($bn)</td><td colspan="2">P/E (x)</td><td colspan="2">EV/EBITDA (x)</td><td colspan="2">ROE</td><td rowspan="2">EPS CAGR FY26-28E</td><td colspan="2">PEG</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td>Shandong Sinocera</td><td>300285 CH</td><td>OW</td><td>CNY</td><td>103.1</td><td>15.1</td><td>87.7</td><td>72.2</td><td>55.9</td><td>47.8</td><td>14%</td><td>15%</td><td>31%</td><td>2.8</td><td>2.3</td></tr><tr><td>MLCC Units Producer</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Three-Circle Group</td><td>300408 CH</td><td>NC</td><td>CNY</td><td>166.5</td><td>47.0</td><td>86.6</td><td>67.4</td><td>67.3</td><td>52.9</td><td>15%</td><td>17%</td><td>25%</td><td>3.5</td><td>2.7</td></tr><tr><td>Fenghua Advanced Tech</td><td>000636 CH</td><td>NC</td><td>CNY</td><td>72.2</td><td>12.3</td><td>176.2</td><td>133.8</td><td>n/a</td><td>n/a</td><td>4%</td><td>5%</td><td>21%</td><td>8.4</td><td>6.4</td></tr><tr><td>Dental Material/Equipment Producer</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Meiya Optoelectronic</td><td>002690 CH</td><td>NC</td><td>CNY</td><td>14.1</td><td>1.8</td><td>15.1</td><td>13.5</td><td>11.6</td><td>10.4</td><td>27%</td><td>29%</td><td>11%</td><td>1.4</td><td>1.3</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td>91.4</td><td>71.7</td><td>44.9</td><td>37.0</td><td>15%</td><td>17%</td><td>22%</td><td>4.0</td><td>3.2</td></tr><tr><td>Global Peers by Product</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sakai Chemical (MLCC Powder)</td><td>4078 JT</td><td>NC</td><td>JPY</td><td>4660</td><td>0.5</td><td>24.4</td><td>17.8</td><td>n/a</td><td>n/a</td><td>4%</td><td>5%</td><td>24%</td><td>1.0</td><td>0.7</td></tr><tr><td>Murata Manufacturing (MLCC Powder)</td><td>6981 JT</td><td>OW</td><td>JPY</td><td>11505</td><td>139.3</td><td>98.0</td><td>65.0</td><td>48.9</td><td>37.3</td><td>8%</td><td>12%</td><td>56%</td><td>1.7</td><td>1.2</td></tr><tr><td>Corning INC (Honeycomb Ceramic)</td><td>GLW US</td><td>OW</td><td>USD</td><td>256</td><td>219.6</td><td>79.9</td><td>66.4</td><td>42.0</td><td>36.0</td><td>22%</td><td>23%</td><td>28%</td><td>2.8</td><td>2.4</td></tr><tr><td>NGK Insulators (Honeycomb Ceramic)</td><td>5333 JT</td><td>N</td><td>JPY</td><td>7562</td><td>13.3</td><td>36.6</td><td>25.2</td><td>13.8</td><td>12.0</td><td>8%</td><td>10%</td><td>25%</td><td>1.5</td><td>1.0</td></tr><tr><td>Tosoh Corp (Dental Material/Equipment)</td><td>4042 JT</td><td>NC</td><td>JPY</td><td>2923</td><td>5.9</td><td>24.9</td><td>14.4</td><td>7.7</td><td>6.9</td><td>4%</td><td>7%</td><td>36%</td><td>0.7</td><td>0.4</td></tr><tr><td>3M Co (Dental Material/Equipment)</td><td>MMM US</td><td>N</td><td>USD</td><td>162</td><td>84.7</td><td>18.6</td><td>17.1</td><td>12.8</td><td>12.0</td><td>89%</td><td>76%</td><td>8%</td><td>2.4</td><td>2.2</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td>26.7</td><td>18.9</td><td>11.5</td><td>10.3</td><td>34%</td><td>31%</td><td>23%</td><td>1.5</td><td>1.2</td></tr></table>

Source: JPM estimates, Bloomberg Finance L.P. Note: Prices as of 30 Jun 2026. Note: ROE calculation excluded returns and equity of minority interest.

## Investment Thesis, Valuati

[中间内容因长度限制已省略]

ore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
