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
- 已识别机构名：`Bernstein`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Global Hotels & Leisure

# Global Lodging: World Cup boost covers softness elsewhere

![](images/a0a1573b8e3ce04d97480022be17d29900820ca20e3a3748795dc811b86fe87f.jpg)

Richard J. Clarke, FCA

+44 20 7676 6850

richard.clarke@bernsteinsg.com

![](images/be629e67990e56a63c9cc6b60740f9a3586380881f632e66673014e048b94dde.jpg)

Niall Mitchelson

+44 20 7676 7144

niall.mitchelson@bernsteinsg.com

![](images/17678cc89d48dc77b8d9a96bcde93cef257b45d156e9ac82be91452dff174274.jpg)

Lasith Siriwardana

+44 20 7550 2191

lasith.siriwardana@bernsteinsg.com

![](images/4d247a3e1cf4e98c55f8888a37a8946c95f2869660723ae812e5e077a9818f4f.jpg)

Sabrina Blanc

+33 1 42 13 47 32

sabrina.blanc@bernsteinsg.com

The headline grabbing numbers at Q2 look set to be in US RevPAR. US RevPAR rose 4% across April–May, accelerating to 7% in the first week of June. That week included just eight World Cup matches versus 28 and 36 in the following two weeks. Even without further acceleration, the World Cup boost should push hotel groups to the top end of guidance - or better; Hyatt should lead. US strength more than offsets well-flagged Middle East weakness and slower growth in Europe and China. OTA traffic has softened into Q2, particularly at Booking and Expedia. However, Booking consensus has fallen to 3.5% room night growth (vs. 2–4% guidance); unless cancellations remain elevated, this looks beatable, with \~6.5% achievable. Airbnb looks cleaner, with stronger web and download trends driven more by APAC/LatAm than the World Cup; we expect \~10% night growth, a 1.6% beat to consensus. Expedia looks a bigger concern, and looks to need a big B2B quarter to avoid a miss to consensus.

OTA demand. App traffic growth has slowed across all three major platforms. Web trends are mixed: deterioration at BKNG and EXPE, but resilience at ABNB, driving LDD y/y growth. Agoda remains strong (\~30% app engagement growth), while Booking and Priceline lag. At EXPE, Expedia and Hotels.com face y/y declines, while Vrbo performs well. Overall, Airbnb should deliver the cleanest quarter (\~10% growth), while Booking (\~6.5%) can still beat a low guide and conservative consensus.

AI showing early signs of an inflection? Referral data shows that traffic being directed to the OTAs by AI has returned to growth this quarter, having slowly been in decline since Q3 last year. Despite this inflection, AI referrals still contribute $< 0.5\%$ of total traffic. We still await the launch of Google's AI-mode hotel feature which is expected to leverage Google's suite of AI protocols (Universal Commerce, Model Context, Agentic Payments) to facilitate booking without visiting a brand website or OTA.

Hotel demand: Q2 marks the start of the World Cup effect, which looks positive against muted expectations given strong June run rates ( $\sim$ 4%) and easy comps. North American strength should push RevPAR to or above the top end of guidance despite international softness. The K-shape persists, with luxury outperforming: Hyatt (4.3%), Marriott (3.2%), Hilton (2.9%), IHG (2.6%), the latter weighed down by a slower quarter in China.

Development remains resilient in the face of conflict in the Middle East. The hotel pipeline continues a steady recovery from last year's Liberation day contraction, showing no signs of being impacted by the conflict in the Middle East. The global pipeline is now \~48,000 rooms (1.9%) larger than pre-Liberation day levels, with all regions contributing to this recovery. Construction has been even stronger, with \~54,500 (6.1%) more rooms in construction in May than at the end of 2025. MEA has been resilient given the conflict in the region, with the pipeline 3.5% larger than it was in February and in construction rooms continuing to increase. With the conflict in Iran now in its fourth month, the inflationary pressure of building material prices and fuel are yet to have a meaningful impact on global development.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">18 Jun 2026</td><td>TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td></td><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td rowspan="2">Cur</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td></tr><tr><td>BKNG (Booking)</td><td>M</td><td>USD</td><td>171.78</td><td>188.00</td><td>(44.4)%</td><td>USD</td><td>9.12</td><td>10.53</td><td>12.29</td><td>18.8</td><td>16.3</td><td>14.0</td></tr><tr><td>ABNB (Airbnb )</td><td>O</td><td>USD</td><td>142.41</td><td>168.00</td><td>(17.9)%</td><td>USD</td><td>4.03</td><td>5.44</td><td>6.65</td><td>35.3</td><td>26.2</td><td>21.4</td></tr><tr><td>EXPE (Expedia)</td><td>M</td><td>USD</td><td>240.90</td><td>253.00</td><td>22.6%</td><td>USD</td><td>15.86</td><td>20.92</td><td>25.20</td><td>15.2</td><td>11.5</td><td>9.6</td></tr><tr><td>TRIP (TripAdvisor)</td><td>O</td><td>USD</td><td>12.97</td><td>20.00</td><td>(26.3)%</td><td>USD</td><td>1.27</td><td>1.30</td><td>1.88</td><td>10.2</td><td>10.0</td><td>6.9</td></tr><tr><td>HLT (Hilton)</td><td>M</td><td>USD</td><td>348.84</td><td>320.00</td><td>15.2%</td><td>USD</td><td>8.11</td><td>8.96</td><td>10.28</td><td>43.0</td><td>38.9</td><td>33.9</td></tr><tr><td>MAR (Marriott)</td><td>O</td><td>USD</td><td>396.20</td><td>402.00</td><td>28.2%</td><td>USD</td><td>10.02</td><td>11.53</td><td>13.30</td><td>39.5</td><td>34.4</td><td>29.8</td></tr><tr><td>IHG.LN (IHG)</td><td>M</td><td>USD</td><td>171.20</td><td>154.00</td><td>37.0%</td><td>USD</td><td>5.01</td><td>5.69</td><td>6.48</td><td>34.2</td><td>30.1</td><td>26.4</td></tr><tr><td>H (Hyatt)</td><td>O</td><td>USD</td><td>202.09</td><td>202.00</td><td>26.8%</td><td>USD</td><td>2.25</td><td>4.03</td><td>5.17</td><td>89.7</td><td>50.1</td><td>39.1</td></tr><tr><td>AC.FP (Accor)</td><td>O</td><td>EUR</td><td>48.86</td><td>55.70</td><td>(1.0)%</td><td>EUR</td><td>1.86</td><td>2.25</td><td>2.73</td><td>26.3</td><td>21.8</td><td>17.9</td></tr><tr><td>SPX</td><td></td><td></td><td>7,500.58</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,578.06</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

In lodging, we rate Marriott, Accor and Hyatt Outperform, and IHG and Hilton Market-Perform. In online travel, we rate Airbnb and Tripadvisor Outperform, and Booking and Expedia Market-Perform.

## Recent research on OTAs:

Tripadvisor: TheFork sale agreed with American Express for \$700m (49% of market cap)

Booking: How it won online travel & can it win AI travel?

Airbnb: Bernstein SDC best ideas slides & key take aways from investor meetings

OTAs in the Quarter (1Q26): Winning the Phony War

OTAs: Updates from Airbnb's Summer Release, Google I/O, and Expedia EXPLORE 26

OTAs: Google didn't kill the OTAs, so why might AI?

## Recent research on Hotels:

Quick Take: Marriott - WSJ letter suggests owners want more Credit Card Cash

Hyatt: Thesis recap & key highlights from the 2026 investor day

Lodging in the Quarter (1Q26): K-Popped? Not yet - Hyatt back to top pick on H2 inflection

Global Hotels: Key takeaways from our expert franchisee calls

Global Hotels and Cruise: Artificial Intelligence.... Sooner or Later - do bots take vacations?

EXHIBIT 1: Under April - May performance and assuming early June performance will continue through the month, we expect Marriott to beat their Q2 RevPAR guidance, and Hilton to come right at the top end of their 2-3% range

Hotels: 26Q2 RevPAR growth estimate (Apr-May run rate + June assumption) vs guidance  
![](images/0e30eb9454e552753da606decdc491382f510242ebd06b9c25304c8477ecab6a.jpg)  
Source: CoStar, Bernstein analysis & estimates

EXHIBIT 2: Airbnb is set to lead room night growth given the current traffic data  
26Q2 BernE Room Night Growth  
![](images/6cc5a84f28ac3abee94f84cb0018452b7dcc32a6f2d2f645ae18d5a33123cec4.jpg)

EXHIBIT 3: Based on current traffic data, we expect Airbnb and Booking to outperform consensus on room nights, while Expedia is likely to underperform

<table><tr><td>2Q26</td><td>ABNB</td><td>BKNG</td><td>EXPE</td></tr><tr><td></td><td colspan="2">(Room) Nights Booked</td><td></td></tr><tr><td>BernE</td><td>148.0</td><td>329.7</td><td>109.3</td></tr><tr><td>Consensus</td><td>145.7</td><td>320.0</td><td>110.9</td></tr><tr><td>vs</td><td>1.6%</td><td>3.0%</td><td>-1.5%</td></tr></table>

Source: Bloomberg, Bernstein analysis & estimates  
We have included no effect yet from elevated cancellations or a positive effect from RNPL at Airbnb  
Source: SensorTower, SimilarWeb, Company reports, Bernstein analysis & estimates

## DETAILS

## ONLINE TRAVEL AGENTS

EXHIBIT 4: Based on current traffic data, we expect Airbnb and Booking to outperform consensus on room nights, while Expedia is likely to underperform

<table><tr><td>2Q26</td><td>ABNB</td><td>BKNG</td><td>EXPE</td></tr><tr><td></td><td colspan="2">(Room) Nights Booked</td><td></td></tr><tr><td>BernE</td><td>148.0</td><td>329.7</td><td>109.3</td></tr><tr><td>Consensus</td><td>145.7</td><td>320.0</td><td>110.9</td></tr><tr><td>vs</td><td>1.6%</td><td>3.0%</td><td>-1.5%</td></tr></table>

Source: Bloomberg, Bernstein analysis & estimates

EXHIBIT 5: Airbnb is set to lead room night growth given the current traffic data  
26Q2 BernE Room Night Growth  
![](images/bb77279e93440820700145b6352cebe9d6cc7a0abd8c3afaa11098dffa02728a.jpg)  
We have included no effect yet from elevated cancellations or a positive effect from RNPL at Airbnb  
Source: SensorTower, SimilarWeb, Company reports, Bernstein analysis & estimates  
EXHIBIT 6: Only BKNG is preferred to the SPX by the sell side  
OTAs: Sell side ratings

![](images/57ba2828968f6cb8adf34e6b48277c6a95ac41700bca16d356288c6b1ef1ee04.jpg)  
Ratings as at 19 June 2026  
Source: Bloomberg, Bernstein analysis

■ Since start of Iran War ■ Since Q1 results ■ YTD

Hotels: 26Q2 RevPAR growth estimate (Apr-May run rate + June assumption) vs guidance  
![](images/37b700cc92fea7cb4a15abbdb3f56cb5b3246e15bb8a5c88921c82e0c0042705.jpg)  
EXHIBIT 8: Only Airbnb recorded a gain in share price following the Q1 results

YTD Stock Price Returns  
![](images/eda2e994ef55df5fad8cf901da2b39d410a4f3c51c0e7cbb391b83fea76b6dc1.jpg)  
Share prices as of 19 June 2026
Source: CapIQ, Bernstein analysis & estimates

## AIRBNB

EXHIBIT 9: Airbnb's web traffic continues to accelerate whilst app engagement growth has eased slightly; app downloads has accelerated significantly to \~30% y/y growth

![](images/92a2e58f9d9c0ce88c37c6c1cf8373ec6c2a46a057539147ac66ae9d0b3abf65.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis  
EXHIBIT 10: Web traffic has grown in the LDDs through the quarter so far with a slight deceleration in app engagement; app downloads has surged with June currently tracking for 43% y/y growth

![](images/50bb5696b073accb754eb286ff3b819c8254057061cf2f7836a21280d198a21e.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis

EXHIBIT 11: India saw the largest increase in downloads versus Q2 last year, contributing to 34% of the total increase, following by Pakistan (20%) and Indonesia (6%). This is followed by three South American nations, with MSD % contributions.

Downloads Growth Q2 2026 (#, 000s)  
![](images/6270dff10669f2249539bd11c2bb55cbbf8552487acf2729c00a3fcf8ecf8564.jpg)  
June downloads number adjusted for partial month
Source: SensorTower, Bernstein analysis  
Airbnb - nights booked (millions) quarterly predictor

EXHIBIT 12: Airbnb model vs actual

![](images/6056edf6df5e1bbaeb3c52aef15207a62f97dbcccdad71b6a4b00049d8ea789a.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis  
EXHIBIT 13: Traffic is correlated with nights booked  
Airbnb - Traffic vs nights booked

![](images/f88b6a2f1db8d671653ece167428863c8254959ca0cfe102715c60847ba9923a.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis

## BOOKING

EXHIBIT 14: Both app and web traffic growth have decelerated in the quarter driven by a weak start to June; app downloads is set to grow y/y in the quarter driven by a strong start to June

BKNG - Quarterly traffic growth  
![](images/61331c4a930375ac35af9590948e2305803b2886405f094695bc15b46b2abfec.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis

EXHIBIT 15: A weak start to June is the primary driver of weak app engagement and web traffic growth. Despite this, June has started with high app download activity, lapping a 3% y/y decline in 2025.

![](images/0bdd98bda7853043ea60e51955798b6620e430fec95f7915497f391a3ea3a6a2.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis

EXHIBIT 16: Growth at Agoda continues to exhibit strength but has slowed down from the $40\%+$ growth seen in Q1; the Booking app's engagement has decelerated whilst Priceline continues to struggle

BKNG - App DAU growth by app  
![](images/8a3f24e5371eba44bcbbbca11f5140f49eead3f557f49be8e07bbd772ef9ea95.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis

EXHIBIT 17: Booking's traffic is correlated to room nights  
BKNG - Traffic vs room nights  
![](images/954049d64b64051496d0b80f810e6d48653ff5bcfbbf287a41ae6bf6895166a0.jpg)  
Source: Company reports, SensorTower, SimilarWeb, Bernstein analysis

EXHIBIT 18: BKNG model vs actual  
BKNG - room nights (millions) quarterly predictor  
![](images/f986c38c5d3e44b5ed544eb7d969eeceab2f2caf2d06a59970a856d106296556.jpg)  
Source: Company reports, Bloomberg, SensorTower, SimilarWeb, Bernstein analysis & estimates

Traffic growth change since guidance issued

EXHIBIT 19: Without any change to traffic trends post guiding BKNG usually beat their guidance range by \~2%, any change in traffic post guiding can impact how BKNG does on room night growth relative to guidance  
BKNG room night growth relative to guidance vs change in traffic growth post guidance issued  
![](images/a155e09ee128ced54ee11e70fda082c91a59e7852a487225efa48125a8522b1b.jpg)  
Source: Company reports, SensorTower, SimilarWeb, Bernstein analysis

## EXPEDIA

EXHIBIT 20: App engagement has been very weak through the quarter, set to grow just 2.3%, whilst web has also slowed following five consecutive quarters of acceleration; downloads growth now laps the beginning of declines in 2Q25

EXPE - Quarterly traffic growth  
![](images/1778c63b526eb40e7fdc6bb2237e759a66dd73afc274ddd96bcf48127533f533.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis

EXHIBIT 21: App engagement and web traffic decelerated through the quarter; the y/y fall in downloads abated in June  
![](images/300747dde47ecfb3d0be385ebcb01c9fc71fb0e8d9195550b86611d2e5b80132.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis

EXHIBIT 22: Both Hotels.com and Expedia have experienced a deceleration in app engagement through the quarter with y/y declines so far in June, whilst Vrbo continues to experience steady growth  
EXPE - DAU growth by app  
![](images/5b9c86c5366cd1c44b5c690581ed800dcc9904f83fba041b0d4199ca140187b0.jpg)  
Source: Bernstein analysis, Sensortower, Similarweb

EXHIBIT 23: Expedia B2C room nights are correlated with traffic  
Actual vs. modelled room nights (B2C)  
![](images/88015006133e76a584b1de0fb40cd728f272e5c204ff84ba5618d17ebf537480.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis

EXHIBIT 24: EXPE model vs actual  
EXPE - Room nights (millions) quarterly predictor  
![](images/73922fbda931e975dc2e587b46accde65ee37f9570738e3f1e6e85bd2c349d05.jpg)  
Source: SensorTower, SimilarWeb, Bernstein analysis

## TRIPADVISOR

EXHIBIT 25: App engagement at TheFork continued its y/y declines into Q2, but but web engagement growth has surged, running at 31% y/y growth so far in June

![](images/0f82b678645788f06dd62362c7d95c93910a9b86c4634d0a786c2bedfe5d355a.jpg)  
Source: SimilarWeb, SensorTower, Bernstein analysis

EXHIBIT 26: Tripadvisor continues to struggle with declines in traffic across both web and app channels
Tripadvisor traffic growth (y/y)  
![](images/693d1396ac4a03e5fc7e394646484bd00b35883358d7301d1ab1d78d76f7b748.jpg)  
Source: SimilarWeb, SensorTower, Bernstein analysis

EXHIBIT 27: Viator, which suffered web traffic declines through 2025, has seen declines ease in last six months with y/y traffic up so far in June; app engagement at the Viator was storing in April and May with \~40% y/y growth

Viator traffic growth (y/y)  
![](images/a4bb3b3a38dd21b6dfed38acc134ea205fed69972a3409664f748da90b8f8cdc.jpg)  
Source: SimilarWeb, SensorTower, Bernstein analysis

## AI TRAFFIC

Referral traffic to the OTAs from AI seems to have inflected in April and May, with traffic growing 24% m/m in April and 31% in May, averaged across the four platforms. As a proportion of traffic, generative AI referrals have also inflected upwards, increasing by \~15 bps from March to May. However, these referrals continue to make up a very small proportion of overall traffic (<0.5%).

Automatic app suggestions could be driving this referral traffic. Now if a user tells Claude that it wants to book a hotel, Claude will automatically suggest using a Claude connector (equivalent to a ChatGPT app), bringing up a list of relevant hotel booking connectors (i.e. Booking.com, Trivago)

EXHIBIT 28: Traffic generated by AI sources to major OTAs, particularly Booking, saw a notable increase in April and May  
Absolute Generative AI Traffic  
![](images/1e2302c9d8db042213d0b8bdbb928d01574f683dad011aaf12e1f51e0fefdd2d.jpg)  
Source: SimilarWeb, Bernstein analysis  
EXHIBIT 29: The share of traffic the OTAs derive from Generative AI has surged since March, but still sits at very low levels (<0.5%). This is potentially driven by increased leisure travel research ahead of the key summer travel period.

Generative AI Traffic as % of Total Traffic  
![](images/c2ffad48ec0e077970ff28f6057a6662554656d968152a295393253c11569986.jpg)  
Source: SimilarWeb, Bernstein analysis

EXHIBIT 30: Claude now automatically suggests relevant connectors (apps) to hotel search queries  
![](images/29d4191c14df083e688ec2f5d11ceb163d59b4ac8ecc7f5ffdb5390392da0cdb.jpg)  
Source: AgentDiscoverability.com, Claude, Bernstein analysis  
EXHIBIT 31: We can with a little trial and error, now get ChatGPT to call apps mid-flow rather than right at the top. Here is only calls one app - in this case Booking.com  
Stays based on your search
20 Ju

[中间内容因长度限制已省略]

nce system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
