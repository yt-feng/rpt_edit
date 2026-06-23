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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
GLOBAL WEEKLY KICKSTART

# Global equities extend gains as Middle East de-escalation continues

Global equities rose 1.2% last week, led by a rebound in Japan and APxJ, up 4.6% and 4.1% (Exhibit 1). AI-driven momentum continued to support Technology, up 4.3%, while Energy lagged, down 6.3% (Exhibit 3). Brent fell around 8% as the US and Iran headed into a prolonged period of talks. Cyclicals outperformed Defensives (Exhibit 30) as risk appetite strengthened (Exhibit 11). At the same time, monthly inflows from global investors remain strong, driven by passive funds and reaching an all-time high (Exhibit 44).

## Macro data this week

US: PCE inflation report, several speaking engagements with Fed officials, including events with Governor Waller and Presidents Williams, Goolsbee, and Kashkari.

Europe: Euro area, Germany, France, UK flash PMIs; Euro area consumer confidence.

Japan: “Summary of Opinions” from the June BOJ MPM, June Tokyo new core CPI.

AEJ: Korea 20-day exports, Taiwan IP, CPI in Malaysia and Singapore, and Thailand central bank meeting.

Pricing is as of the close of Friday, June 19.

## The Post Modern Cycle – Navigating the Capex Boom

The Post Modern cycle is reshaping equity returns. It marks a shift away from disinflation, deregulation, falling rates and globalisation toward higher macro volatility, higher real rates, greater state intervention and regionalisation. Returns are likely to rely less on valuation expansion and more on EPS growth.

A capex supercycle is taking hold. The AI revolution is creating a new engine of private investment, while energy security and geopolitics are driving a synchronised rise in public spending. Supply chains are also being rebuilt for resilience, lifting capital intensity and structurally raising cost bases.

■ Markets are broadening opportunity sets. Higher private capex and rising government borrowing are pushing up the cost of capital, supporting faster technology growth and stronger real asset values. The result is greater cross-sectional dispersion and more scope for alpha generation.

See more: Global Strategy Paper: The Post Modern Cycle – Navigating the Capex Boom

## Guillaume Jaisson

+44(20)7552-3000 | guillaume.jaisson@gs.com GS International

Peter Oppenheimer
+44(20)7552-5782 |
peter.oppenheimer@gs.com
GS International

## Sharon Bell

+44(20)7552-1341
sharon.bell@gs.com
GS International

John Kwon
+65-6654-6337 |
jongmin.kwon@gs.com
GS (Singapore) Pte

Giovanni Ferrannini
+44(20)7051-2589 |
giovanni.ferrannini@gs.com
GS International

Elena Porfidia
+44(20)7051-5240 |
elena.porfidia@gs.com
GS International

## The week at a glance — Global markets and indices

Exhibit 1: Global market performance
MSCI Indices, 1-week price return (USD, %)  
![](images/9713d194499151a65158cbd8b955a6958cd80252c1f1aff3a9fabe196c0f3c60.jpg)  
Source: Datastream, Bloomberg, GS Global Investment Research

Exhibit 2: World equity indices USD, indexed price performance  
![](images/7233b25f3876fdc291024d289425e6f2c66edc4b623ae97b85a760016654422d.jpg)  
Source: Datastream, STOXX, GS Global Investment Research

Exhibit 3: MSCI AC World sector performance  
MSCI Indices, 1-week price return (USD, %)  
![](images/9abe5850359bb60619aebd58a933d9de699da93df58b7c2ae991d53f9ef8f54d.jpg)  
Source: Datastream, Bloomberg, GS Global Investment Research  
Exhibit 4: Cross-asset performance
MSCI Indices, 1-week price return (USD, %)

![](images/777405a50174ee690e8ad1da340f632ad6c6b3485145c03e06b8b0ff39fbc2d5.jpg)  
Source: Datastream, Bloomberg, GS Global Investment Research

## Forecasts

Exhibit 5: GDP growth, % yoy: GS vs. consensus

<table><tr><td colspan="6">Real GDP Growth</td></tr><tr><td rowspan="2">Percent Change yoy</td><td>2025</td><td colspan="2">2026</td><td colspan="2">2027</td></tr><tr><td>GS</td><td>GS</td><td>Cons*</td><td>GS</td><td>Cons*</td></tr><tr><td>USA</td><td>2.1</td><td>2.1</td><td>2.1</td><td>2.1</td><td>2.0</td></tr><tr><td>Japan</td><td>1.1</td><td>0.5</td><td>0.6</td><td>1.0</td><td>0.8</td></tr><tr><td>Euro area</td><td>1.5</td><td>0.3</td><td>0.6</td><td>0.9</td><td>1.2</td></tr><tr><td>Germany</td><td>0.3</td><td>0.7</td><td>0.6</td><td>1.0</td><td>1.1</td></tr><tr><td>France</td><td>0.9</td><td>0.4</td><td>0.6</td><td>0.6</td><td>0.9</td></tr><tr><td>Italy</td><td>0.7</td><td>0.6</td><td>0.6</td><td>0.5</td><td>0.7</td></tr><tr><td>Spain</td><td>2.8</td><td>2.1</td><td>2.2</td><td>1.5</td><td>1.8</td></tr><tr><td>UK</td><td>1.4</td><td>1.2</td><td>1.0</td><td>1.3</td><td>1.1</td></tr><tr><td>China</td><td>5.0</td><td>4.7</td><td>4.6</td><td>4.7</td><td>4.5</td></tr><tr><td>Developed Markets</td><td>1.8</td><td>1.4</td><td>1.9</td><td>1.7</td><td>1.5</td></tr><tr><td>Emerging Markets</td><td>4.2</td><td>3.7</td><td>4.0</td><td>4.1</td><td>3.9</td></tr><tr><td>World</td><td>2.8</td><td>2.4</td><td>2.8</td><td>2.7</td><td>2.5</td></tr></table>

\* Bloomberg country and GS aggregate consensus  
Source: Bloomberg, GS Global Investment Research

Exhibit 6: GS Macro 3-, 6- and 12-month forecasts

<table><tr><td rowspan="2"></td><td rowspan="2">Current</td><td colspan="3">Forecast</td><td rowspan="2">Up/Downside to 12m TP (%)</td></tr><tr><td>3m</td><td>6m</td><td>12m</td></tr><tr><td colspan="6">Equities</td></tr><tr><td>S&amp;P 500</td><td>7501</td><td>7600</td><td>8000</td><td>8300</td><td>10.7</td></tr><tr><td>STOXX Europe 600</td><td>636</td><td>640</td><td>645</td><td>660</td><td>3.8</td></tr><tr><td>MSCI Asia-Pacific Ex-Japan</td><td>918</td><td>980</td><td>1030</td><td>1080</td><td>17.7</td></tr><tr><td>Topix</td><td>4045</td><td>4100</td><td>4200</td><td>4400</td><td>8.8</td></tr><tr><td colspan="6">10Y Rate (%)</td></tr><tr><td>US</td><td>4.5</td><td>4.5</td><td>4.4</td><td>4.3</td><td>-14 bp</td></tr><tr><td>Euro Area (Germany)</td><td>3.0</td><td>2.9</td><td>3.0</td><td>3.0</td><td>2 bp</td></tr><tr><td>Japan</td><td>2.6</td><td>2.5</td><td>2.5</td><td>2.4</td><td>-22 bp</td></tr><tr><td colspan="6">Currencies</td></tr><tr><td>€/$</td><td>1.15</td><td>1.14</td><td>1.18</td><td>1.20</td><td>4.7</td></tr><tr><td>£/$</td><td>1.32</td><td>1.33</td><td>1.34</td><td>1.33</td><td>0.9</td></tr><tr><td>$/¥</td><td>161</td><td>160</td><td>158</td><td>155</td><td>-3.9</td></tr><tr><td colspan="6">Commodities</td></tr><tr><td>Brent Crude Oil ($/bbl)</td><td>80.6</td><td>83</td><td>80</td><td>75</td><td>-6.9</td></tr><tr><td>NYMEX Nat. Gas ($/mmBtu)</td><td>3.2</td><td>3.50</td><td>3.50</td><td>3.50</td><td>8.3</td></tr><tr><td>Gold ($/troy oz)</td><td>4151</td><td>4690</td><td>4900</td><td>5115</td><td>23.2</td></tr><tr><td>LME Copper ($/mt)</td><td>13527</td><td>13620</td><td>13735</td><td>13800</td><td>2.0</td></tr></table>

Source: Bloomberg, Datastream, STOXX, GS Global Investment Research

Exhibit 7: GS top-down vs. consensus bottom-up estimates of 2026 EPS growth  
![](images/1fce4051fc1bd868fb542bbdb5b5a137c0c6013a1672f7a3bb597394865166ab.jpg)  
Source: I/B/E/S, Toyo Keizai, STOXX, MSCI, GS Global Investment Research

Exhibit 8: GS top-down vs. consensus bottom-up estimates of 2027 EPS growth  
![](images/317cee3cb709a20815bef65ad845c5bec15bced0a69bb09c71d0b94573c7c21d.jpg)  
Source: I/B/E/S, Toyo Keizai, STOXX, MSCI, GS Global Investment Research

## Risk and Sentiment indicators

Exhibit 9: GS Bull/Bear Market Indicator (GSBLBR)  
![](images/2f7943921edb536e99988a0043d036e723671b8232f4bfd1bf07075f0e400565.jpg)  
Exhibit 10: Details of components of the GS Bull/Bear Market Indicator
GS Bull/Bear Market Indicator = Average percentile

<table><tr><td></td><td>Level</td><td>Percentile</td></tr><tr><td>Shiller PE</td><td>40.5</td><td>98%</td></tr><tr><td>Unemployment</td><td>4.3</td><td>77%</td></tr><tr><td>0-6 quarter yield curve</td><td>0.3</td><td>73%</td></tr><tr><td>Private sector Financial Balance</td><td>3.9</td><td>56%</td></tr><tr><td>ISM</td><td>54.0</td><td>55%</td></tr><tr><td>Core Inflation</td><td>2.9</td><td>53%</td></tr><tr><td>GS Bull/Bear Market Indicator</td><td></td><td>68%</td></tr></table>

Note: 100 $^{th}$ percentile means these variables are at their highest level, except for Private sector Financial Balance, yield curve and unemployment where 100% means they are at their lowest.  
Source: Shiller, Haver Analytics, Datastream, GS Global Investment Research  
Source: Haver Analytics, Datastream, Robert Shiller, GS Global Investment Research

## Exhibit 11: Risk Appetite Indicator (GSRAII)

The RAI is based on 27 pair-trades across asset classes measured on z-scores rel. to last 2 years' performance, see July 2016 GOAL for details

![](images/10529e92e7c99ddcc18f1637770aabb1974c58d3940adae865d5faab30881eb3.jpg)  
Source: GS Global Investment Research

Exhibit 12: Percentile of sentiment indicators
Data since 2007  
![](images/f10cd2ea994ccce533e7fb1a5155ee4908b63b799fc8fe686356e5b59e066b76.jpg)  
Source: EPFR, Datastream, Haver Analytics, GS Global Investment Research

## Performance - Local indices

Exhibit 13: Global equity market performance (local indices)

<table><tr><td rowspan="2">Market</td><td colspan="4">Price return (Local CCY, %)</td></tr><tr><td>Index</td><td>1-week (Local)</td><td>Ytd</td><td>1Yr</td></tr><tr><td>South Korea</td><td>KOSPI</td><td>11.4</td><td>114.8</td><td>204.0</td></tr><tr><td>Turkey</td><td>XU100</td><td>5.7</td><td>30.8</td><td>61.9</td></tr><tr><td>Taiwan</td><td>TWSE</td><td>5.2</td><td>60.4</td><td>111.2</td></tr><tr><td>Austria</td><td>ATX</td><td>4.3</td><td>22.6</td><td>51.5</td></tr><tr><td>Japan</td><td>TPX</td><td>4.2</td><td>18.7</td><td>44.9</td></tr><tr><td>Philippines</td><td>PCOMP</td><td>3.8</td><td>1.4</td><td>(3.5)</td></tr><tr><td>Egypt</td><td>EGX30</td><td>3.5</td><td>25.8</td><td>74.0</td></tr><tr><td>China (A)</td><td>SHSZ300</td><td>3.4</td><td>6.7</td><td>28.6</td></tr><tr><td>Singapore</td><td>FSSTI</td><td>3.3</td><td>11.8</td><td>33.3</td></tr><tr><td>Spain</td><td>IBEX</td><td>3.1</td><td>11.8</td><td>40.8</td></tr><tr><td>Indonesia</td><td>JCI</td><td>2.8</td><td>(28.6)</td><td>(11.4)</td></tr><tr><td>Italy</td><td>FTSEMIB</td><td>2.6</td><td>17.6</td><td>35.7</td></tr><tr><td>Greece</td><td>ASE</td><td>2.2</td><td>16.8</td><td>39.1</td></tr><tr><td>Sweden</td><td>OMX</td><td>2.1</td><td>10.3</td><td>29.9</td></tr><tr><td>EuroStoxx 50</td><td>SX5E</td><td>1.7</td><td>8.7</td><td>21.1</td></tr><tr><td>Malaysia</td><td>FBMKLCI</td><td>1.7</td><td>1.9</td><td>14.0</td></tr><tr><td>India</td><td>NIFTY EM</td><td>1.7</td><td>(8.1)</td><td>(3.1)</td></tr><tr><td>Germany</td><td>DAX DM</td><td>1.4</td><td>2.0</td><td>8.4</td></tr><tr><td>Hungary</td><td>HUX</td><td>1.4</td><td>24.0</td><td>41.2</td></tr><tr><td>US</td><td>SPX</td><td>0.9</td><td>9.6</td><td>25.4</td></tr><tr><td>France</td><td>CAC</td><td>0.8</td><td>3.3</td><td>11.5</td></tr><tr><td>New Zealand</td><td>NZX 50</td><td>0.8</td><td>(1.7)</td><td>4.2</td></tr><tr><td>Denmark</td><td>KFX</td><td>0.6</td><td>(4.3)</td><td>(16.9)</td></tr><tr><td>Switzerland</td><td>SMI</td><td>0.5</td><td>3.8</td><td>16.0</td></tr><tr><td>Stoxx 600</td><td>SXXP</td><td>0.4</td><td>7.3</td><td>18.6</td></tr><tr><td>Australia</td><td>AS51</td><td>0.3</td><td>1.3</td><td>3.6</td></tr><tr><td>Portugal</td><td>BVLX</td><td>0.2</td><td>13.5</td><td>26.2</td></tr><tr><td>Poland</td><td>WiG</td><td>0.1</td><td>18.4</td><td>38.9</td></tr><tr><td>Czech</td><td>PX</td><td>0.1</td><td>(4.5)</td><td>20.3</td></tr><tr><td>South Africa</td><td>JALSH</td><td>-0.1</td><td>(2.8)</td><td>18.6</td></tr><tr><td>Netherlands</td><td>AEX</td><td>-0.3</td><td>13.3</td><td>18.6</td></tr><tr><td>Canada</td><td>SPTSX60</td><td>-0.3</td><td>9.9</td><td>29.6</td></tr><tr><td>Mexico</td><td>MEXBOL</td><td>-0.4</td><td>5.3</td><td>20.8</td></tr><tr><td>UK</td><td>UKX</td><td>-1.0</td><td>4.3</td><td>17.9</td></tr><tr><td>Thailand</td><td>SET</td><td>-1.3</td><td>24.8</td><td>47.1</td></tr><tr><td>Belgium</td><td>BEL20</td><td>-1.6</td><td>11.2</td><td>28.0</td></tr><tr><td>Brazil</td><td>IBOV</td><td>-1.6</td><td>4.5</td><td>21.4</td></tr><tr><td>Norway</td><td>OSEAX</td><td>-2.9</td><td>17.1</td><td>19.6</td></tr><tr><td>HK</td><td>HSI</td><td>-3.2</td><td>(6.7)</td><td>3.0</td></tr><tr><td>China (H)</td><td>HSCEI</td><td>-4.8</td><td>(10.5)</td><td>(5.2)</td></tr></table>

<table><tr><td rowspan="2">Market</td><td colspan="4">Relative Price return (vs MSCI AC World, USD, %)</td></tr><tr><td>Index</td><td>1-week (USD)</td><td>Ytd</td><td>1Yr</td></tr><tr><td>South Korea</td><td>KOSPI</td><td>9.6</td><td>91.6</td><td>147.6</td></tr><tr><td>Egypt</td><td>EGX30</td><td>6.6</td><td>9.2</td><td>49.3</td></tr><tr><td>Taiwan</td><td>TWSE</td><td>4.2</td><td>48.8</td><td>71.1</td></tr><tr><td>Turkey</td><td>XU100</td><td>4.1</td><td>10.1</td><td>10.8</td></tr><tr><td>Philippines</td><td>PCOMP</td><td>3.5</td><td>(12.9)</td><td>(35.9)</td></tr><tr><td>Japan</td><td>TPX</td><td>2.4</td><td>4.4</td><td>3.9</td></tr><tr><td>China (A)</td><td>SHSZ300</td><td>2.2</td><td>(0.7)</td><td>9.6</td></tr><tr><td>Austria</td><td>ATX</td><td>2.1</td><td>8.7</td><td>24.4</td></tr><tr><td>Indonesia</td><td>JCI</td><td>2.1</td><td>(44.0)</td><td>(45.4)</td></tr><tr><td>Singapore</td><td>FSSTI</td><td>1.4</td><td>0.3</td><td>5.9</td></tr><tr><td>India</td><td>NIFTY</td><td>1.3</td><td>(23.4)</td><td>(38.0)</td></tr><tr><td>Spain</td><td>IBEX</td><td>0.9</td><td>(1.8)</td><td>13.7</td></tr><tr><td>Italy</td><td>FTSEMIB</td><td>0.5</td><td>3.9</td><td>8.6</td></tr><tr><td>Greece</td><td>ASE</td><td>0.1</td><td>3.1</td><td>12.1</td></tr><tr><td>US</td><td>SPX</td><td>-0.3</td><td>(1.4)</td><td>(1.7)</td></tr><tr><td>EuroStoxx 50</td><td>SX5E</td><td>-0.4</td><td>(4.8)</td><td>(6.0)</td></tr><tr><td>Hungary</td><td>HUX</td><td>-0.6</td><td>21.2</td><td>34.9</td></tr><tr><td>Germany</td><td>DAX</td><td>-0.7</td><td>(11.3)</td><td>(18.7)</td></tr><tr><td>Sweden</td><td>OMX</td><td>-0.9</td><td>(4.8)</td><td>3.8</td></tr><tr><td>France</td><td>CAC</td><td>-1.3</td><td>(10.1)</td><td>(15.6)</td></tr><tr><td>Malaysia</td><td>FBMKLCI</td><td>-1.4</td><td>(10.8)</td><td>(9.5)</td></tr><tr><td>Denmark</td><td>KFX</td><td>-1.5</td><td>(17.5)</td><td>(44.2)</td></tr><tr><td>Australia</td><td>AS51</td><td>-1.5</td><td>(4.4)</td><td>(14.6)</td></tr><tr><td>Stoxx 600</td><td>SXXP</td><td>-1.8</td><td>(6.1)</td><td>(8.5)</td></tr><tr><td>Portugal</td><td>BVLX</td><td>-2.0</td><td>(0.2)</td><td>(0.9)</td></tr><tr><td>New Zealand</td><td>NZX 50</td><td>-2.1</td><td>(12.8)</td><td>(26.9)</td></tr><tr><td>Switzerland</td><td>SMI</td><td>-2.2</td><td>(9.1)</td><td>(9.4)</td></tr><tr><td>Czech</td><td>PX</td><td>-2.2</td><td>(17.8)</td><td>(3.7)</td></tr><tr><td>South Africa</td><td>JALSH</td><td>-2.3</td><td>(13.1)</td><td>3.7</td></tr><tr><td>Mexico</td><td>MEXBOL</td><td>-2.3</td><td>(1.7)</td><td>6.0</td></tr><tr><td>Poland</td><td>WiG</td><td>-2.4</td><td>3.8</td><td>12.5</td></tr><tr><td>Netherlands</td><td>AEX</td><td>-2.4</td><td>(0.3)</td><td>(8.5)</td></tr><tr><td>Thailand</td><td>SET</td><td>-3.0</td><td>8.8</td><td>19.7</td></tr><tr><td>Canada</td><td>SPTSX60</td><td>-3.0</td><td>(4.7)</td><td>(1.5)</td></tr><tr><td>UK</td><td>UKX</td><td>-3.6</td><td>(8.3)</td><td>(10.9)</td></tr><tr><td>Belgium</td><td>BEL20</td><td>-3.7</td><td>(2.4)</td><td>0.9</td></tr><tr><td>Brazil</td><td>IBOV</td><td>-4.0</td><td>0.5</td><td>2.7</td></tr><tr><td>HK</td><td>HSI</td><td>-4.4</td><td>(18.3)</td><td>(24.0)</td></tr><tr><td>Norway</td><td>OSEAX</td><td>-6.0</td><td>11.1</td><td>(2.7)</td></tr><tr><td>China (H)</td><td>HSCEI</td><td>-6.0</td><td>(22.1)</td><td>(32.1)</td></tr></table>

Source: MSCI, STOXX, Local Index Compilers, FactSet, GS Global Investment Research

## Sector performance across regions - Weekly

Exhibit 14: 1-week sector performance across regions
Light blue: below -1 standard dev. from the AC world market performance. Dark blue: above +1 standard dev. from the AC world market performance.

<table><tr><td rowspan="2">MSCI Index</td><td colspan="18">Weekly Absolute Performance (%) in USD</td></tr><tr><td>US</td><td>Canada</td><td>UK</td><td>Germany</td><td>France</td><td>Swiss</td><td>Spain</td><td>Italy</td><td>Devd Euro</td><td>Japan</td><td>Korea</td><td>Brazil</td><td>India</td><td>China</td><td>Taiwan</td><td>AC APxJ</td><td>EM</td><td>AC World</td></tr><tr><td>Market</td><td>1.0</td><td>-1.8</td><td>-2.5</td><td>0.1</td><td>-0.1</td><td>-0.8</td><td>2.6</td><td>2.0</td><td>-0.4</td><td>4.7</td><td>13.1</td><td>-2.2</td><td>3.0</td><td>-2.9</td><td>5.2</td><td>4.1</td><td>4.1</td><td>1.2</td></tr><tr><td>Energy</td><td>-6.6</td><td>-5.4</td><td>-7.9</td><td>-</td><td>-7.6</td><td>-</td><td>-6.0</td><td>-7.7</td><td>-7.8</td><td>-0.9</td><td>-5.4</td><td>-7.2</td><td>2.1</td><td>-7.1</td><td>-</td><td>-3.5</td><td>-3.8</td><td>-6.3</td></tr><tr><td>Materials</td><td>-0.2</td><td>-1.4</td><td>-5.5</td><td>-0.4</td><td>-4.7</td><td>1.9</td><td>-</td><td>0.5</td><td>-2.8</td><td>4.2</td><td>-4.7</td><td>0.1</td><td>1.9</td><td>-0.5</td><td>16.6</td><td>-0.5</td><td>-0.3</td><td>-0.9</td></tr><tr><td>Industrials</td><td>2.9</td><td>-3.0</td><td>0.1</td><td>3.2</td><td>5.3</td><td>3.5</td><td>2.6</td><td>2.7</td><td>2.7</td><td>3.2</td><td>10.3</td><td>2.3</td><td>5.9</td><td>0.5</td><td>-4.0</td><td>5.0</td><td>5.9</td><td>2.9</td></tr><tr><td>Capital Goods</td><td>4.8</td><td>0.6</td><td>1.8</td><td>3.7</td><td>5.5</td><td>4.4</td><td>2.8</td><td>2.7</td><td>3.7</td><td>4.3</td><td>10.5</td><td>5.9</td><td>6.0</td><td>2.6</td><td>-2.4</td><td>6.8</td><td>7.3</td><td>4.5</td></tr><tr><td>Comm &amp; Profess. Srvcs</td><td>-3.2</td><td>0.7</td><td>-4.4</td><td>-</td><td>1.2</td><td>0.1</td><td>-</td><td>-</td><td>-3.6</td><td>0.1</td><td>-</td><td>-</td><td>-</td><td>0.0</td><td>-</td><td>-0.1</td><td>0.0</td><td>-2.5</td></tr><tr><td>Transportation</td><td>-3.6</td><td>-5.8</td><td>-</td><td>-0.9</td><td>0.3</td><td>-8.4</td><td>2.2</td><td>-</td><td>-2.9</td><td>-4.3</td><td>4.1</td><td>-4.1</td><td>4.9</td><td>-5.0</td><td>-6.3</td><td>-0.7</td><td>0.6</td><td>-3.2</td></tr><tr><td>Consumer Discretionary</td><td>0.8</td><td>-4.0</td><td>-3.5</td><td>-5.8</td><td>-1.6</td><td>1.1</td><td>-0.8</td><td>-2.2</td><td>-2.3</td><td>1.8</td><td>-2.3</td><td>-1.5</td><td>4.2</td><td>-5.1</td><td>4.8</td><td>-2.4</td><td>-2.8</td><td>0.1</td></tr><tr><td>Automobiles &amp; Comp.</td><td>-1.8</td><td>-2.8</td><td>-</td><td>-7.4</td><td>-0.2</td><td>-</td><td>-</td><td>-2.1</td><td>-4.7</td><td>3.2</td><td>-1.7</td><td>-</td><td>2.1

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
