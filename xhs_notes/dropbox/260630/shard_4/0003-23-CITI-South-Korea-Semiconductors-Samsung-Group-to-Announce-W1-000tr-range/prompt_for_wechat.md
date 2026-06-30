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
# South Korea Semiconductors

# Samsung Group to Announce W1,000tr-range Investment Across Advanced Industries in Korea

## CITI'S TAKE

Domestic Media (Maekyung, Donga, 26 June) reported that Samsung group will announce a massive and long-term investment worth \~W1,000tr centered on semiconductors and AI on 29 June. As a part of the Blue House's initiative to foster the semiconductor industry in the Honam region, we project the massive investment led by the government should boost the sustained growth of the Korean semiconductor supply chain. We are constructive on Korean SPE names, backed by the promising AI demand outlook and accelerated green-field capacity expansion plans.

Samsung Group to Invest \~W1,000tr Over the Next Decade Mainly on Semiconductor & AI – According to domestic media (Maekyung, Donga, 26 June), Samsung Group is expected to announce \~W1,000tr investment for the semiconductor and advanced industries over the next decade at a national briefing at the Blue House on 29 June. The source noted that the investment will include approx. \~W300tr for 4\~5 fabs in Gwangju and South Jeolla Province, over W56tr for a packaging R&D and production cluster in the Chungcheong region, \~W360tr for 6 fabs at the Yongin cluster, and over W350tr for AI data centers in Asan. Samsung is also reported to be accelerating its Yongin fabs' completion from 2048E to 2034E-2035E.

Accelerated Semiconductor Investment Under the Blue House's Mega Project Initiative – The Blue House will announce “Three Mega Projects for Korea’s Great Leap Forward” plan centered on establishing a semiconductor cluster in the Honam region, with more than half the total investment flowing into Gwangju and South Jeolla. After the mega project announcement by the Blue House, SK will also announce a southwestern investment event in Gwangju on 30 June and Samsung also will host an investment event on 2nd July in Asan, South Chungcheong province, focused on the Chungcheong region. Samsung is currently reviewing back-end fab upgrades at its Cheonan and Onyang campuses. Samsung Group’s chairman JY Lee is expected to detail the AI data center plans in Asan and a next-generation battery base in Ulsan.

Implication: Maintain a Constructive View on Korean SPE names – Pulling together recent news and reports regarding the \~W1,000tr investment by Samsung, we expect Samsung to invest W360tr for the Yongin semiconductor cluster, W300tr for Honam-region semiconductor fabs in Gwangju and South Jeolla, and >W350tr for AI data centers and >W56tr packaging facilities in Chungcheong region. While Samsung is expected to review additional investment across advanced industries such as battery, display, and substrates, we believe Samsung will allocate the bulk of the total investment plan into semiconductor and AI projects. We expect Korean front-end SPEs including Wonik IPS, TES, and Eugene Technology as well as Korean back-end SPEs such as TechWing will likely benefit.

Peter Lee $^{AC}$

+82-2-3705-0720

peter.sc.lee@citi.com

Jayden Oh

+82-2-3705-0747

jayden.oh@citi.com

## EugeneTechnology

(084370.KQ; W172600.0; 1; 26 Jun 26; 15:45)

## Valuation

We value Eugene Tech shares at W193,000, derived by assigning a 6.2x 27E P/B, which is the average of its global peers' 12m fwd PB multiple. We assign this multiple based on our projection of an advanced DRAM capex upcycle in 2026E & 2027E and commodity memory supply shortage.

## Risks

Key downside risks that could prevent the Eugene Tech stock from reaching our target price include: [1] Weaker-than-expected new equipment sales: If Eugene Tech's new product, Large Batch Type Thermal ALD, results in weaker-than-expected orders from key clients, we believe it could pose both earnings and sentiment risks to the company; [2] Fiercer competition: Stiffer competition from the global equipment players to protect market share could potentially delay the company's market share gains from global players; and [3] An unexpected memory market downcycle.

Key upside risks that could prevent the Eugene Tech stock from reaching our target price include: [1] stronger-than-expected new equipment sales: If Eugene Tech's new products result in stronger-than-expected orders from key clients, we believe it could lead to both earnings and sentiment upside to the company; and [2] continued memory market upcycle beyond 2027E.

## Samsung Electronics

(005930.KS; W339500.0; 1; 26 Jun 26; 15:45)

## Valuation

Our 12-month target price for Samsung of W460,000 is derived using a sum-of-the-parts (SOTP) methodology, based on 2026E EBITDA. In calculating total operating value, we reference global peers in assigning fair-value EV/EBITDA multiples for the five main divisions (7.8x for Memory, 4.1x for Foundry, 0.5x for Display Panel, 4.8x for Mobile and 2.0x for Consumer Electronics), in line with trading multiples of relevant peer companies.

## Risks

Downside risks that could prevent the shares from reaching our target price include: 1) Longer-than-expected approval delay in HBM shipment to its key customers; 2) PC sales weaken more than our forecast and NAND demand fails to meet our expectations; 3) aggressive investment by competitors in memory semiconductor/foundry could have a negative impact on prices; 4) competition in the handset market intensifies, reducing SEC's handset margins; 5) any major appreciation of the won would impact SEC's earnings.

## TechWing

(089030.KQ; W51800.0; 1H; 26 Jun 26; 15:45)

## Valuation

Our W80k TP for Techwing is derived by applying 23.5x PE multiple, the upper bound of Techwing's historically traded multiple, to the average of 2026E and 2027E earnings, when we expect earnings momentum from its HBM-specialized handler to be fully reflected. We think applying upper bound multiple is justifiable given increased likelihood of successful launch of HBM prober in 2026E, which would support Techwing's robust top line growth and margin improvement throughout 2026E-2027E.

## Risks

Our quant risk rating assigns a High Risk rating to Techwing to reflect potential near-term earnings and stock price volatility following the strong rally of late. As Techwing's current stock price partially reflects anticipation of the launch of HBM tester, we believe the stock could fluctuate depending on the progress of HBM tester launch.

Key downside risks that could impede the shares from reaching our target include: [1] delay in the qualification approval of Cube Prober, which would delay Cube Prober revenue to 2025E from 4Q23E, [2] emergence of a new competitor in the HBM handler market given robust market growth outlook, which could limit Techwing's revenue upside in the HBM handler market, and [3] delay in memory market recovery, which could dent recovery in Techwing's memory handler, COK, and parts revenue.

## TES

(095610.KQ; W183300.0; 1; 26 Jun 26; 15:45)

## Valuation

Our W160k target price for TES is based on 6.6x 2026E BPS, obtained by applying the average of PE-CVD peer multiple given the unprecedented memory shortage, robust order outlook on customers' aggressive memory fab expansion, and growing exposure to advanced DRAM process.

## Risks

Key downside risks that could impede the shares from reaching our target price include: (1) Delays in new equipment development: BSD and low-k equipment, the new equipment TES is developing, fails to pass the key client's qualification test. We believe this could pose both earnings and sentiment downside risks for the company. (2) Fiercer competition from global players to protect market share: Keener competition from the global equipment players to protect market share could potentially delay the company's efforts in gaining market share. (3) An unexpected memory market downcycle throughout 2026E could potentially delay the company's capex and pressure near-term earnings and investor sentiment. Key upside risks include: 1) successful diversification into foundry equipment from current memory-centered equipment portfolio, and 2) a quicker memory market recovery, which would result in memory makers' upward capex revision.

## Wonik IPS

(240810.KQ; W163800.0; 1; 26 Jun 26; 15:45)

## Valuation

Our target price of W185,000 is based on 7.9x 2026E BVPS, which is the peer average of 12m-forward PB to factor in multi-year memory WFE upcycle and potential upside from advanced nodes including 1cnm DRAM and US foundry investment by its strategic customer.

## Risks

Key downside risks that could prevent the shares from reaching our target price include: (1) Delays in new equipment development: If equipment Wonik IPS is developing, such as carbon/halogen-free precursor and equipment used in high/metal gate deposition process, meet with additional requests from the clients or fail to pass clients' qualification tests, we believe it could pose both earnings and sentiment downside risks to the company. (2) Fiercer competition from global players to protect market share: Keener competition from the global equipment players to protect market share could potentially delay the company's efforts in gaining market share. (3) Prolonged memory market downcycle: An extended memory market downcycle throughout 2022E could potentially delay the company's capex and pressure near-term earnings and investor sentiment.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

![](images/8a359c872e75fc24568d417d47626a43b75079dd0e52b8a6f8dc229ee1ddde20.jpg)

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>25-Aug-23 08:37:25</td><td>1</td><td>*40,000.00</td><td>30,800.00</td></tr><tr><td>2</td><td>26-Sep-23 10:43:43</td><td>1</td><td>*39,000.00</td><td>32,400.00</td></tr><tr><td>3</td><td>26-Mar-24 10:32:16</td><td>1</td><td>*45,000.00</td><td>36,150.00</td></tr><tr><td>4</td><td>11-Nov-24 16:49:03</td><td>1</td><td>*40,000.00</td><td>24,200.00</td></tr></table>

\*Indicates Change  
Rating/target price changes above reflect Eastern Time

## EugeneTechnology (084370.KQ)

Ratings and Target Price History
Fundamental Research

Analyst: Peter Lee

![](images/cc466a7af7f288a08d727e7d1d88d6e082774b49d2e7efec2bd29c5b497b3ddb.jpg)

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>26-Sep-23 10:43:43</td><td>*3</td><td>*35,000.00</td><td>42,050.00</td></tr><tr><td>2</td><td>26-Mar-24 10:32:16</td><td>*1</td><td>*55,000.00</td><td>39,500.00</td></tr><tr><td>3</td><td>19-Sep-24 18:15:47</td><td>1</td><td>*60,000.00</td><td>36,350.00</td></tr><tr><td>4</td><td>12-May-25 06:52:03</td><td>1</td><td>*50,000.00</td><td>35,950.00</td></tr></table>

\*Indicates Change  
Rating/target price changes above reflect Eastern Time

## TechWing (089030.KQ)

Ratings and Target Price History
Fundamental Research

Analyst: Jayden Oh

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>11-Mar-24 17:00:45</td><td>*1H</td><td>*41,000.00</td><td>23,900.00</td></tr><tr><td>14-Apr-24 18:50:06</td><td>1H</td><td>*49,000.00</td><td>38,600.00</td></tr></table>

\*Indicates Change

![](images/2d3420f4f5cc5bd33c29dde42cfd26a2262ac3e0dd2f651e05ac09efc5b5038c.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5 21-Oct-25 10:29:44</td><td>1H</td><td>*80,000.00</td><td>63,400.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Samsung Electronics (005930.KS)

Ratings and Target Price History
Fundamental Research

Analyst: Peter Lee

![](images/06192bf068e49effd525e4948fce5aee54f9bf3d4949b97450826c196b082c8f.jpg)

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>28-Jun-23 08:19:44</td><td>1 *105,000.00</td><td>72,700.00</td><td></td></tr><tr><td>2</td><td>27-Jul-23 05:53:47</td><td>1 *110,000.00</td><td>71,700.00</td><td></td></tr><tr><td>3</td><td>31-Aug-23 06:54:46</td><td>1 *120,000.00</td><td>66,900.00</td><td></td></tr><tr><td>4</td><td>22-Sep-23 09:53:22</td><td>1 *110,000.00</td><td>68,800.00</td><td></td></tr><tr><td>5</td><td>01-Apr-24 05:23:20</td><td>1 *120,000.00</td><td>82,000.00</td><td></td></tr><tr><td>6</td><td>09-Sep-24 02:31:35</td><td>1 *110,000.00</td><td>67,500.00</td><td></td></tr><tr><td>7</td><td>02-Oct-24 05:16:51</td><td>1 *97,000.00</td><td>61,300.00</td><td></td></tr><tr><td>8</td><td>26-Dec-24 07:42:50</td><td>1 *87,000.00</td><td>53,600.00</td><td></td></tr></table>

\*Indicates Change  
Rating/target price changes above reflect Eastern Time

## TES (095610.KQ)

Ratings and Target Price History
Fundamental Research

![](images/a8f7f06c70c82960bc5763a057ef42727537d6c740002362b9e1df22a2e4c1cf.jpg)  
\*Indicates Change

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>26-Sep-23 10:43:43</td><td>*2</td><td>*23,000.00</td><td>21,700.00</td></tr><tr><td>2</td><td>01-Apr-24 07:15:32</td><td>*1</td><td>*35,000.00</td><td>21,400.00</td></tr><tr><td>3</td><td>19-Sep-24 18:15:47</td><td>1</td><td>*31,500.00</td><td>16,400.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

![](images/492df5843543c68cfc7aaaacce7a0602b04d33130edc65d66455aecf85718b70.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>31-Aug-23 02:54:46</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>66,900.00</td></tr><tr><td>2</td><td>28-Nov-23 21:19:48</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>72,700.00</td></tr><tr><td>3</td><td>01-Apr-24 01:23:20</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>82,000.00</td></tr><tr><td>4</td><td>30-Apr-24 22:52:33</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>77,500.00</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>5</td><td>17-Nov-24 11:09:02</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>53,500.00</td></tr><tr><td>6</td><td>14-Feb-25 12:17:17</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>56,000.00</td></tr><tr><td>7</td><td>16-Jul-25 01:08:04</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>64,700.00</td></tr><tr><td>8</td><td>15-Aug-25 14:07:20</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>71,600.00</td></tr></table>

<table><tr><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>9 23-Nov-25 05:07:18</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>94,800.00</td></tr><tr><td>10 23-Dec-25 20:51:38</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>111,500.00</td></tr><tr><td>11 11-May-26 03:42:55</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>285,500.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of Samsung Electronics.

<table><tr><td colspan="7">Citi Equity Ratings Distribution</td></tr><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Apr 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>8%</td><td>37%</td><td>47%</td><td>16%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
