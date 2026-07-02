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
- 已识别机构名：`Citi`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Taiwan PCB & Laminates

## ABF/BT Sector: GM/pricing Upcycle Underway; Buy with Higher TPs

## CITI'S TAKE

Both ABF and BT substrate demand are rising on AI applications. With rising AI GPU/ASIC/CPU demand, we expect the ABF supply tightness to continue throughout 2027 with continued price hikes. For BT, we also see improving S/D status, given peers' less willingness in BT production. T glass is likely to still be a constraint throughout 2027, if new capacity ramps slower than expected. We expect substrate makers to enjoy GM expansion cycle evidenced by recent monthly earnings release. We raise TPs of NYPCB (new TP NT\$1,550), Kinsus (new TP NT\$1,100) and Unimicron (new TP NT\$1,500) and reiterate our Buy ratings. In the short term, we prefer NYPCB and Kinsus on more aggressive pricing strategies. We open 30-day upside CWs for NYPCB and Kinsus on potential sales/GM upbeat on price hikes.

ABF substrate: tight supply evidenced by improving China UTR — Besides rapid recovery in UTR of non-China capacity, we observe UTR in China ABF capacity is improving with peers like Zhen Ding announcing further capacity expansion. To note that, China ABF capacity is the least favorable option to US customers given geopolitical risk. However, it seems US customers are adopting it given lack of choices. Meanwhile, domestic AI demand for China is also improving, competing for capacity as well. Unless there is any sign of loosening demand in China capacity, we are confident on the growth prospects of the ABF industry. We currently forecast 15-20% QoQ ABF price hike in 3Q26 considering higher willingness to pay in high season and followed by 10-15% QoQ in 4Q26 considering lower seasonality.

BT substrate: improving S/D with peers gradually cutting capacity — Our industry checks suggest some peers are showing less willingness to take BT orders or are planning to convert BT production lines into ABF lines given better profitability and visibility. This coupled with its guidance, Unimicron now targets to cut at least 15% of its total BT capacity by end-2026, likely mostly for WBCSP-related products in Taiwan plants. We think Unimicron won’t fully exit BT market in the mid-term given some of its major ABF customers like Apple and few key Chinese customers still have BT demand. Thus, we think its capacity in Suzhou’s BT plant might be kept operational. As per our calculation (see figure 2), Unimicron’s BT sales roughly account for 11% of BT sales from global major peers. We project Unimicron to cut 40-50% of its BT capacity in the mid-term, thereby gradually transferring BT orders to other Taiwanese peers.

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td rowspan="2">ESPR (%)</td><td rowspan="2">Div Yld (%)</td><td rowspan="2">ETR (%)</td><td rowspan="2">Last Rpt Yr</td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td colspan="2">EPS</td><td colspan="2">EPS</td></tr><tr><td>Kinsus Interconnect Technology</td><td>3189.TW</td><td>NT$</td><td>891.00</td><td>469,482</td><td>30 Jun 13:30</td><td>1</td><td>nc</td><td>Upside^</td><td>400.00</td><td>1,100.00</td><td>23.5</td><td>0.2</td><td>23.6</td><td>Dec-25</td><td>9.56</td><td>11.42</td><td>16.20</td><td>38.61</td></tr><tr><td>Nan Ya PCB</td><td>8046.TW</td><td>NT$</td><td>1,185.00</td><td>765,706</td><td>30 Jun 13:30</td><td>1</td><td>nc</td><td>Upside^</td><td>1,100.00</td><td>1,550.00</td><td>30.8</td><td>0.2</td><td>31.0</td><td>Dec-25</td><td>14.07</td><td>16.41</td><td>36.82</td><td>51.89</td></tr><tr><td>Unimicron Technology</td><td>3037.TW</td><td>NT$</td><td>1,070.00</td><td>1,700,094</td><td>30 Jun 13:30</td><td>1</td><td>nc</td><td>Upside^</td><td>1,080.00</td><td>1,500.00</td><td>40.2</td><td>0.2</td><td>40.4</td><td>Dec-25</td><td>17.71</td><td>21.12</td><td>35.94</td><td>50.49</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High Risk</td><td colspan="13">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change</td></tr><tr><td colspan="6">Source: Citi</td><td colspan="13">^Catalyst Watch</td></tr></table>

Jack Chen AC

+886-2-8726-9091

jack1.chen@citi.com

Laura (Chia Yi) Chen

+886-2-8726-9090

laura.cy.chen@citi.com

Nicholas Lai

+886-2-8726-9093

nicholas.lai@citi.com

Earnings Estimates

<table><tr><td colspan="4"></td><td colspan="4">Last Reported Year</td><td></td><td colspan="4">Current Fiscal Year</td><td></td><td colspan="4">Next Fiscal Year</td><td></td></tr><tr><td>Company Name</td><td>Ticker</td><td>Last Rpt Year</td><td>Currency</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY0</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY1</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY2</td></tr><tr><td rowspan="2">Kinsus Interconnect Technology</td><td rowspan="2">3189.TW</td><td>Dec-25</td><td></td><td>0.61</td><td>0.74</td><td>0.75</td><td>1.41</td><td>3.51</td><td>1.17</td><td>2.50</td><td>3.45</td><td>4.08</td><td>11.42</td><td>6.97</td><td>8.74</td><td>10.37</td><td>12.53</td><td>38.61</td></tr><tr><td></td><td>NT$</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Old</td><td></td><td>Dec-25</td><td>NT$</td><td>0.61</td><td>0.74</td><td>0.75</td><td>1.41</td><td>3.51</td><td>1.69</td><td>1.74</td><td>2.80</td><td>3.24</td><td>9.56</td><td>3.22</td><td>3.59</td><td>4.77</td><td>4.62</td><td>16.20</td></tr><tr><td>Nan Ya PCB</td><td>8046.TW</td><td>Dec-25</td><td>NT$</td><td>0.32</td><td>-0.29</td><td>1.12</td><td>1.86</td><td>3.01</td><td>2.03</td><td>3.38</td><td>5.08</td><td>5.92</td><td>16.41</td><td>8.73</td><td>12.22</td><td>14.65</td><td>16.29</td><td>51.89</td></tr><tr><td>Old</td><td></td><td>Dec-25</td><td>NT$</td><td>0.32</td><td>-0.29</td><td>1.12</td><td>1.86</td><td>3.01</td><td>2.03</td><td>2.87</td><td>4.07</td><td>5.11</td><td>14.07</td><td>6.52</td><td>8.41</td><td>10.48</td><td>11.41</td><td>36.82</td></tr><tr><td>Unimicron Technology</td><td>3037.TW</td><td>Dec-25</td><td>NT$</td><td>0.60</td><td>0.02</td><td>1.44</td><td>2.32</td><td>4.38</td><td>3.28</td><td>6.29</td><td>5.03</td><td>6.52</td><td>21.12</td><td>8.08</td><td>9.78</td><td>14.04</td><td>18.58</td><td>50.49</td></tr><tr><td>Old</td><td></td><td>Dec-25</td><td>NT$</td><td>0.60</td><td>0.02</td><td>1.44</td><td>2.32</td><td>4.38</td><td>3.20</td><td>4.07</td><td>4.11</td><td>6.34</td><td>17.71</td><td>6.88</td><td>7.79</td><td>9.90</td><td>11.38</td><td>35.94</td></tr><tr><td colspan="19">Source: Citi</td></tr></table>

T glass: likely continued constraint throughout 2027 — With rising AI GPU/ASIC/CPU demand, we think T glass constraint will likely continue into 2027, given the qualification progress for new vendors seems to be slower than expected. Among all the new vendors, Taiwan Glass Industry takes the lead in thick glass, but its product quality still falls short of Nittobo's. End-customers/fabless currently are still trying to find new vendors or other kinds of new solutions, which is why EMC's ABF CCL, MGC's RS Resin solution, Nanya Plastics' T glass or other new unlisted vendors' T glass are considered yet without proven. In our view, Nittobo's capacity expansion plan remains the key to the supply, yet whether to initiate another price hike is up to Nittobo's willingness, which is addressed in our JP analyst Yuta Nishiyama's report. In our view, whether industrywide T glass supply is able to fulfill all the AI chips demand is less concerning as we think substrate makers would just hike the prices to achieve growth despite the unit shipments being constrained. We expect fabless in the queue eventually needs to pay premium for the shortage, unless there is any delay in their AI chip development.

NYPCB: aggressive ABF/BT pricing strategies — NYPCB is the key beneficiary to Broadcom's Tomahawk products for ABF. Besides switch ICs, the company would also supply some ASIC projects with minority share. For BT, the company sees strong demand from memory. NYPCB is reluctant to enter into long-term agreements with customers with high exposure to spot market. Based on the last cycle experience, we expect the company to be aggressive in both ABF and BT pricing strategies in the coming quarters. We expect price hikes and improving UTR to drive its GM profile in the coming quarters. Our 2027E profit forecast increases by \~40% to NT\$33.5bn given more aggressive pricing strategies.

Kinsus: Vera CPU key suppliers + improving BT S/D — The company is bullish on its market share in Vera CPU, which echoes our view of market share >50%. The upside to its market share in Vera CPU would hinge on its capacity expansion pace. For its BT demand, we expect Kinsus to benefit from outflowing orders from Unimicron, driving its UTR quarter after quarter. We expect Kinsus' both ABF and BT UTR to reach full levels by end 2026. To note that, we think BT GM would likely surpass 20% levels in this cycle vs historical levels of 5-15% range. Kinsus currently has 35-40% BT sales exposure. We forecast more than double our 2027E profit estimate to NT\$20.8bn given improvement in both ABF and BT GM.

Unimicron: more T glass supply + HDI upside — To note that, in the long term, we remain bullish on Unimicron. We understand investors' short-term preference to ABF names with higher spot-price exposure and earnings growth. However, we think Unimicron still sees meaningful earnings upside from 1) GM benefits from long-term agreements, 2) HDI GM improvement when mass production kicks off and 3) more sufficient T glass supply, which would give Unimicron more bargaining power with customers vs other ABF peers. To note that, we think current 2Q26 GM uptick is likely driven by rising ABF demand rather than by HDI UTR improvement. Our 2027E profit forecast increases by 37% to NT\$77.6bn given GM expansion on more AI GPU/ASIC demand and price hikes.

GM expansion/price hikes underway; NYPCB/Kinsus preferred in the S-T — We see improving monthly profitability (see figure 1) of three Taiwanese substrate makers, which we believe is driven by enhanced product mix, rising UTR and price hikes. Given material changes to our 2027E profit estimates driven by margin expansion, we raise TPs of Unimicron/NYPCB/Kinsus to NT\$1,500 (30x 2027E EPS)/ NT\$1,550 (30x 2027E EPS)/ NT\$1,100 (28x 2027E EPS). We believe the GM/pricing upcycle would justify the high PE multiple of \~30x for all the three companies. Reiterate our Buy ratings on three names. In the short term, we prefer

NYPCB/Kinsus given aggressive pricings and improving BT sentiment. In the long term, we still like Unimicron given its leadership position.

<table><tr><td colspan="7">Figure 1. Unaudited monthly results of Unimicron, NYPCB and Kinsus</td></tr><tr><td colspan="7">Unimicron</td></tr><tr><td>(NT$mn)</td><td>1Q26</td><td>Jan</td><td>Implied Feb</td><td>March</td><td>April</td><td>May</td></tr><tr><td>Sales</td><td>37,446</td><td>12,767</td><td>11,600</td><td>13,079</td><td>13,933</td><td>na</td></tr><tr><td>Pre-tax earnings</td><td>6,299</td><td>2,382</td><td>2,290</td><td>1,627</td><td>3,460</td><td>na</td></tr><tr><td>Pre-tax margin %</td><td>16.8%</td><td>18.7%</td><td>19.7%</td><td>12.4%</td><td>24.8%</td><td>na</td></tr><tr><td>EPS (NT$)</td><td>3.28</td><td>1.23</td><td>1.31</td><td>0.74</td><td>1.85</td><td>na</td></tr><tr><td>Gains on financial assets (liabilities) at fair value</td><td>2,507</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>% of total sales</td><td>6.7%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">Share price performance of Unimicron&#x27;s financial assets (%)</td></tr><tr><td>Unimicron</td><td>92%</td><td>72%</td><td>27%</td><td>-8%</td><td>99%</td><td>19%</td></tr><tr><td>UMC</td><td>18%</td><td>27%</td><td>5%</td><td>-14%</td><td>37%</td><td>87%</td></tr><tr><td>TWSE Index</td><td>11%</td><td>11%</td><td>10%</td><td>-10%</td><td>23%</td><td>15%</td></tr><tr><td colspan="7">Share price diff. of Unimicron&#x27;s financial assets (NT$/share, except Index)</td></tr><tr><td>Unimicron</td><td>225</td><td>159</td><td>103</td><td>(37)</td><td>439</td><td>172</td></tr><tr><td>UMC</td><td>7</td><td>13</td><td>3</td><td>(9)</td><td>21</td><td>67</td></tr><tr><td>TWSE Index</td><td>2,759</td><td>3,100</td><td>3,351</td><td>(3,692)</td><td>7,204</td><td>5,806</td></tr><tr><td colspan="7">NYPCB</td></tr><tr><td>(NT$mn)</td><td>1Q26</td><td>Jan</td><td>Feb</td><td>Implied March</td><td>April</td><td>May</td></tr><tr><td>Sales</td><td>11,177</td><td>3,720</td><td>3,166</td><td>4,291</td><td>4,451</td><td>4,440</td></tr><tr><td>Pre-tax earnings</td><td>1,598</td><td>450</td><td>369</td><td>779</td><td>746</td><td>977</td></tr><tr><td>Pre-tax margin %</td><td>14.3%</td><td>12.1%</td><td>11.7%</td><td>18.2%</td><td>16.8%</td><td>22.0%</td></tr><tr><td>EPS (NT$)</td><td>2.03</td><td>0.56</td><td>0.46</td><td>1.01</td><td>0.92</td><td>1.21</td></tr><tr><td colspan="7">Kinsus</td></tr><tr><td>(NT$mn)</td><td>1Q26</td><td>Implied Jan</td><td>Feb</td><td>March</td><td>April</td><td>May</td></tr><tr><td>Sales</td><td>11,105</td><td>3,962</td><td>3,204</td><td>3,939</td><td>na</td><td>4,200</td></tr><tr><td>Pre-tax earnings</td><td>964</td><td>99</td><td>421</td><td>444</td><td>na</td><td>563</td></tr><tr><td>Pre-tax margin %</td><td>8.7%</td><td>2.5%</td><td>13.1%</td><td>11.3%</td><td>na</td><td>13.4%</td></tr><tr><td>EPS (NT$)</td><td>1.17</td><td>-0.09</td><td>0.68</td><td>0.58</td><td>na</td><td>0.91</td></tr></table>

Figure 2. BT estimated sales of major global peers in 2025

<table><tr><td></td><td>Market Share (%)</td><td>Sales (US$mn)</td></tr><tr><td colspan="3">Taiwan peers</td></tr><tr><td>Unimicron</td><td>11%</td><td>551</td></tr><tr><td>Kinsus</td><td>10%</td><td>460</td></tr><tr><td>Nanya PCB</td><td>8%</td><td>376</td></tr><tr><td>Zhen Ding</td><td>5%</td><td>260</td></tr><tr><td colspan="3">Chinese peers</td></tr><tr><td>Shennan Circuits</td><td>12%</td><td>577</td></tr><tr><td>Shenzhen Fastprint</td><td>4%</td><td>186</td></tr><tr><td colspan="3">Korea peers</td></tr><tr><td>Simmtech</td><td>16%</td><td>748</td></tr><tr><td>SEMCO</td><td>14%</td><td>657</td></tr><tr><td>Daeduck</td><td>10%</td><td>479</td></tr><tr><td>LG Innotek</td><td>7%</td><td>322</td></tr><tr><td>Other small peers</td><td>4%</td><td>205</td></tr><tr><td>Total</td><td>100%</td><td>4,820</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi Estimates, Bloomberg

Figure 3. NYCPB – Earnings Revision

<table><tr><td rowspan="2">(NT$mn)</td><td colspan="3">2Q26E</td><td colspan="3">3Q26E</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td></tr><tr><td>Sales</td><td>13,344</td><td>13,585</td><td>-2%</td><td>16,176</td><td>15,603</td><td>4%</td><td>58,517</td><td>57,230</td><td>2%</td><td>107,214</td><td>92,356</td><td>16%</td><td>164,586</td><td>130,620</td><td>26%</td></tr><tr><td>Sequential growth (%)</td><td>19%</td><td>22%</td><td></td><td>21%</td><td>15%</td><td></td><td>46%</td><td>42%</td><td></td><td>83%</td><td>61%</td><td></td><td>54%</td><td>41%</td><td></td></tr><tr><td>Gross profit</td><td>3,048</td><td>2,651</td><td>15%</td><td>4,486</td><td>3,655</td><td>23%</td><td>14,502</td><td>12,581</td><td>15%</td><td>44,000</td><td>31,624</td><td>39%</td><td>72,477</td><td>48,856</td><td>48%</td></tr><tr><td>Opex</td><td>480</td><td>489</td><td>-2%</td><td>582</td><td>546</td><td>7%</td><td>2,123</td><td>2,045</td><td>4%</td><td>3,645</td><td>3,140</td><td>16%</td><td>5,180</td><td>4,180</td><td>24%</td></tr><tr><td>Operating profit</td><td>2,567</td><td>2,162</td><td>19%</td><td>3,904</td><td>3,108</td><td>26%</td><td>12,379</td><td>10,537</td><td>17%</td><td>40,355</td><td>28,484</td><td>42%</td><td>67,297</td><td>44,676</td><td>51%</td></tr><tr><td>Pre-tax profit</td><td>2,663</td><td>2,258</td><td>18%</td><td>4,002</td><td>3,206</td><td>25%</td><td>12,930</td><td>11,088</td><td>17%</td><td>40,891</td><td>29,012</td><td>41%</td><td>67,907</td><td>45,276</td><td>50%</td></tr><tr><td>Net income</td><td>2,184</td><td>1,852</td><td>18%</td><td>3,282</td><td>2,629</td><td>25%</td><td>10,601</td><td>9,090</td><td>17%</td><td>33,531</td><td>23,790</td><td>41%</td><td>55,684</td><td>37,127</td><td>50%</td></tr><tr><td>EPS (NT$)</td><td>3.38</td><td>2.87</td><td>18%</td><td>5.08</td><td>4.07</td><td>25%</td><td>16.41</td><td>14.07</td><td>17%</td><td>51.89</td><td>36.82</td><td>41%</td><td>86.18</td><td>57.46</td><td>50%</td></tr><tr><td>Gross margin (%)</td><td>22.8%</td><td>19.5%</td><td>+3.3 ppt</td><td>27.7%</td><td>23.4%</td><td>+4.3 ppt</td><td>24.8%</td><td>22.0%</td><td>+2.8 ppt</td><td>41.0%</td><td>34.2%</td><td>+6.8 ppt</td><td>44.0%</td><td>37.4%</td><td>+6.6 ppt</td></tr><tr><td>Opex ratio (%)</td><td>3.6%</td><td>3.6%</td><td>-0.0 ppt</td><td>3.6%</td><td>3.5%</td><td>+0.1 ppt</td><td>3.6%</td><td>3.6%</td><td>+0.1 ppt</td><td>3.4%</td><td>3.4%</td><td>-0.0 ppt</td><td>3.1%</td><td>3.2%</td><td>-0.1 ppt</td></tr><tr><td>Operating margin (%)</td><td>19.2%</td><td>15.9%</td><td>+3.3 ppt</td><td>24.1%</td><td>19.9%</td><td>+4.2 ppt</td><td>21.2%</td><td>18.4%</td><td>+2.7 ppt</td><td>37.6%</td><td>30.8%</td><td>+6.8 ppt</td><td>40.9%</td><td>34.2%</td><td>+6.7 ppt</td></tr><tr><td>Net margin (%)</td><td>16.4%</td><td>13.6%</td><td>+2.7 ppt</td><td>20.3%</td><td>16.9%</td><td>+3.4 ppt</td><td>18.1%</td><td>15.9%</td><td>+2.2 ppt</td><td>31.3%</td><td>25.8%</td><td>+5.5 ppt</td><td>33.8%</td><td>28.4%</td><td>+5.4 ppt</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 4. NYCPB – Forecast Summary

<table><tr><td rowspan="2">NYPCB(NT$ in Mn, year-end Dec)</td><td colspan="4">2026</td><td colspan="4">2027</td><td colspan="11"></td></tr><tr><td>1Q</td><td>2QE</td><td>3QE</td><td>4QE</td><td>1QE</td><td>2QE</td><td>3QE</td><td>4QE</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue</td><td>11,177</td><td>13,344</td><td>16,176</td><t

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
