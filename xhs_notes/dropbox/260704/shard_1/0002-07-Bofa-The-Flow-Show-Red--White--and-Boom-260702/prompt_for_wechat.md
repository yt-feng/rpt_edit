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
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如中国/行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/降息/通胀/机器人/比特币等。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`BofA`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
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
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 5-8 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 第一条 `KC评论` 之后，插入一段 1-2 句的中段 CTA：说明单篇报告只是一个切片，每天的国际信源汇编会把当天国际投行、咨询公司、国际机构报告整理成中文摘要、KC评论和图表合集，适合喂给 AI 追问，也适合人工快速扫市场变化。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化。星球会把单篇报告放回当天国际投行、咨询公司、国际机构主线里，整理成中文摘要、KC评论和图表合集，便于喂给AI，也便于人工快速扫市场dynamics。汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；每日汇编会把单篇报告放回当天主线，整理成中文摘要、KC评论和图表合集，便于喂给 AI，也便于人工快速扫市场 dynamics；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
- CTA 不要只在结尾出现；中段 CTA 要讲清楚“每日汇编 + 图表合集 + AI/人工浏览使用场景”，让读者在读到一半时已经理解知识星球的价值。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份BofA研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# The Flow Show

# Red, White, and Boom

Scores on the Doors: commods 33.3%, oil 19.2%, intl stocks 12.0%, SPX 9.3%, US\$ 2.6%, cash 1.9%, HY 1.8%, IG 0.2%, govt bonds -1.2%, gold -4.7%, bitcoin -30.1% YTD.

Tale of the Tape: Q2 AI/US boom leaders... SOX 88%, KOSPI 64%, biotech 24%, small cap 21%, banks 17%; Q2 war/inflation laggards... Saudi -4%, China -10%, gold -14%, bitcoin -14%, energy -15%, defense -16%, oil -31%; USTs vs. gold breaking 2020s down-trend (Chart 3 – peak inflationary de-globalization), boomy secular breakout for EM & small cap, AI arms race hyperscalers (MAGS) sideways for third straight quarter... all big stuff.

The Price is Right: since independence in 1776... US beats UK on population growth (2.0% vs. 0.8% – Table 1), nominal GDP growth (6.0% vs. 5.8% – Chart 5), real GDP growth (3.6% vs. 2.1%), and US has better inflation record (2.5% vs. 3.9% for UK); but UK has enjoyed lower cost of government debt... UK 10-year bond yield average 5.6% past 250 years vs. 5.8% in US (Chart 6); note US govt debt has grown 5.8% p.a. since 1780), and annual total return from US Treasuries since independence is 5.1%.

The Biggest Picture: red, white, and boom... past 250 years, US stocks (USA Top 100 index) have annualized 3.6% price return (Chart 2), 8.7% total return; even stronger past 150 years (S&P 500 = 4.9% price return & 9.3% total return); but in their first 50 years, US stocks annualized a 2% loss (flat in first 100 years) driven by panics of 1819 & 1837, limited growth drivers until railroads, and highly concentrated indices (First Bank of the United States = >80% of market cap of Philadelphia Stock Exchange in 1792).

Chart 2: Red, White & Boom – US stock prices since independence USA Top 100 index since 1972 (price return, log scale)  
![](images/84a7f33668e405d6ca74fe721973afd67efd82fb642b8459b2e0c5ed8c9cb812.jpg)  
Source: BofA Global Investment Strategy, GFD Finaeon  
BofA GLOBAL RESEARCH

More on page 2...

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 11 to 13.
12990253

## 02 July 2026

Investment Strategy
Global

## BofA Data Analytics

![](images/deaadd2e1d82c7a9459f79a370fb8fd4396136fbbda95d08e1d81bed79a5d74d.jpg)

Michael Hartnett
Investment Strategist
BofAS
+1 646 855 1508
michael.hartnett@bofa.com

Anya Shelekhin
Investment Strategist
BofAS
+1 646 855 3753
anya.shelekhin@bofa.com

Myung-Jee Jung
Investment Strategist
BofAS
+1 646 855 0389
myung-jee.jung@bofa.com

Jessica Guo
Investment Strategist
BofAS
+1 646 855 0033
jessica.guo@bofa.com

## Chart 1: BofA Bull & Bear Indicator Up to 9.5 from 9.1

![](images/0bc5182417d88537ae561c6bf34a47a92bd0fd9e066ad1ba70991d899445b4ee.jpg)  
Source: BofA Global Investment Strategy. The indicator identified above as the BofA Bull & Bear Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.  
BofA GLOBAL RESEARCH

Weekly Flows: \$55.0bn to cash, \$29.1bn to bonds, \$2.0bn from crypto, \$3.0bn from gold, \$13.9bn from stocks.

## Flows to Know:

• Crypto: \$2.0bn outflow, biggest since Nov'25,

• Gold: \$3.0bn outflow, 7 $^{th}$ week of outflows, longest streak since Mar'24,

• IG bonds: \$17.2bn inflow, 13 $^{th}$ week of inflows,

• HY bonds: \$3.4bn inflow, biggest since May'25,

• US equities: \$17.2bn outflow, biggest since Mar'26,

• Japan equities: \$1.9bn inflow, biggest in 7 weeks,

• Financials: \$2.2bn inflow, biggest since Jan'26,

• Telcos: \$2.4bn inflow, biggest since Aug'25,

• Tech: \$14.3bn inflow, on track for record \$152bn inflow YTD,

• Energy: \$3.2bn outflow, biggest since Jul'24,

• Materials: \$6.8bn outflow, biggest since Mar'26.

BofA Private Clients: \$4.5tn AUM... 65.4% stocks, 17.6% bonds, 9.8% cash; biggest outflow to equities in four weeks; private clients extending duration in USTs... fifth week of outflow from T-bills, inflows to T-notes; private client equity ETF share count up 5.4% YTD, 0.6% MTD, 0.1% past week; in ETFs past four weeks, private clients buying materials, healthcare, munis, and selling Japan, staples, financials.

BofA Bull & Bear Indicator $^{1}$ : rises to 9.5 from 9.1 driven by more bullish hedge fund positioning (reducing S&P 500 futures shorts and reducing VIX futures longs), bond inflow to HY bonds, equity inflows to tech and healthcare; BofA Bull and Bear Indicator "sell signal" triggered May 20 $^{th}$ ; since 2002 there have been 17 "sell signals", average loss for global stocks over 2-3 months is 2-3%, hit ratio of \~60%, max drawdowns of 15-20% (see BofA Bull & Bear Indicator revamp report).

Chart 3: 2020s bear market in Treasuries vs. Gold inflecting
TLT (20+ year US Treasury ETF) vs gold – price relative  
![](images/9b9ea15a7806a69b6dc5f6cfde77ac1cff010607d80b476f26f36fcee84860b4.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 4: June payrolls weak, but profits why jobs stronger in '26 US payrolls MoM (3mma) vs S&P 500 forward EPS YoY (RHS)  
![](images/9516318b3060d88e9a8854adfc8774ef3c41791c316856c388c585fecd05eb75.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Table 1: 250 years of US demographic, economic & financial history
Evolution of US economic and financial markets

<table><tr><td colspan="2">250 years of US history...</td></tr><tr><td>Population growth</td><td>2.0%</td></tr><tr><td>Nominal GDP growth</td><td>6.0%</td></tr><tr><td>Real GDP growth</td><td>3.6%</td></tr><tr><td>Inflation</td><td>2.5%</td></tr><tr><td>Government debt growth</td><td>5.8%</td></tr><tr><td>10-year UST yield</td><td>5.6%</td></tr><tr><td>10-year UST total return</td><td>5.1%</td></tr><tr><td>US stocks price return (USA Top 100 index since 1792)</td><td>3.6%</td></tr><tr><td>US stocks total return</td><td>8.7%</td></tr><tr><td>US stocks real price return</td><td>1.8%</td></tr><tr><td>US stocks real total return</td><td>6.7%</td></tr><tr><td>US stocks price return (S&amp;P 500 index since 1871)</td><td>4.9%</td></tr><tr><td>US stocks total return</td><td>9.3%</td></tr><tr><td>US stocks real price return</td><td>2.4%</td></tr><tr><td>US stocks real total return</td><td>6.7%</td></tr></table>

\*GDP growth and inflation figures are annual averages since 1789; 10-year UST yield is average since 1786; population growth, government debt growth, US stocks returns are CAGRs from 1780, 1792, and 1871, respectively.

Chart 5: US vs. UK nominal GDP since independence
US nominal GDP vs UK nominal GDP (log scale)  
![](images/b993d04782a989f61a8485d719031a8d7a40c0387098104ef0fcbf1ef2f3b284.jpg)  
Source: BofA Global Investment Strategy, GFD Finaeon \*log scale, rebased to 1789  
BofA GLOBAL RESEARCH

Chart 6: US 10-year Treasury yield since 1786
US 10-year Treasury yield since 1786 (%)  
![](images/dc634e4c3642182e43370014b323dad45f7a8909b8a01a4789ea738be94fc4b8.jpg)  
Source: BofA Global Investment Strategy, GFD Finaeon  
BofA GLOBAL RESEARCH

Chart 7: S&P 500 in real terms since 1871
S&P 500 in real terms since 1871 (log scale)  
![](images/827a985ec3c30272da3b2453152c7ae5165bca208d2adc219ca7bbe22d79c2cb.jpg)  
Source: BofA Global Investment Strategy, GFD Finaeon  
BofA GLOBAL RESEARCH

Chart 8: Tech funds on track for record \$152bn inflow in '26 Flows to tech funds, weekly vs 4wk-ma (\$bn)  
![](images/fa2bef8493f45fcd0feba3034dbb08e67471973ab207805037bf31f86239f705.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 9: Biggest inflow to financials since Jan'26 Flows to financials funds, weekly vs 4wk-ma (\$bn)  
![](images/a1fe71ce775f49842d7fb8e08353813619de5011223cddd7d619a9fa24c01b78.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 10: Biggest outflow from materials since Mar'26 Flows to materials funds, weekly vs 4wk-ma (\$bn)  
![](images/b65ff26157643ea28a61410b942671a363668c8040082d04262908013cde6853.jpg)  
Source: BofA Global Investment Strategy, EPFR

Chart 11: Biggest outflow from energy since Jul'24 Flows to energy funds, weekly vs 4wk-ma (\$bn)  
![](images/63c7ab62937ce6f94c6921a3c90a524edaf34b1d4bbe5d7d06ce31aa53c63014.jpg)  
Source: BofA Global Investment Strategy, EPFR

## Asset Class Flows (Table 2)

Equities: \$13.9bn outflow (\$5.2bn to ETFs, \$18.8bn from mutual funds)

Bonds: inflows past 62 weeks (\$29.1bn)

Precious metals: outflows past 7 weeks (\$3.0bn)

## Fixed Income Flows (Chart 12)

IG Bond inflows past 13 weeks (\$17.2bn)

HY Bond inflows past 3 weeks (\$3.4bn)

EM Debt inflows past 3 weeks (\$0.8bn)

Munis inflows past 11 weeks (\$1.9bn)

Govt/Tsy inflows resume (\$4.7bn)

TIPS inflows past 22 weeks (\$0.3bn)

Bank loan inflows past 4 weeks (\$0.8bn)

## Equity Flows (Table 3)

US: outflows past 2 weeks (\$17.2bn)

Japan: inflows past 4 weeks (\$1.9bn)

Europe: outflows past 12 weeks (\$3.7bn)

EM: outflows past 3 weeks (\$4.0bn)

By style: outflows US small cap (\$3.0bn), US large cap (\$11.0bn), US growth (\$13.3bn), US value (\$15.8bn).

By sector: inflows tech (\$14.4bn), com svs (\$2.4bn), financials (\$2.2bn), hcare (\$1.6bn), utilities (\$0.2bn), consumer (\$48mn); outflows real estate (\$0.2bn), energy (\$3.2bn), materials (\$3.8bn).

Table 2: Cumulative YTD flows by asset class Global flows by asset class, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td><td>YTD %AUM</td></tr><tr><td>Equities</td><td>0.0%</td><td>516,137</td><td>1.8%</td></tr><tr><td>ETFs</td><td>0.0%</td><td>802,094</td><td>4.9%</td></tr><tr><td>LO</td><td>-0.1%</td><td>-285,653</td><td>-2.3%</td></tr><tr><td>Bonds</td><td>0.3%</td><td>480,004</td><td>5.0%</td></tr><tr><td>Commodities</td><td>-0.6%</td><td>7,800</td><td>0.8%</td></tr><tr><td>Money-market</td><td>0.5%</td><td>441,922</td><td>4.0%</td></tr></table>

\*week ended 7/1/2026: Source: EPFR Global  
BofA GLOBAL RESEARCH

Table 3: Big YTD inflows to US stocks
Global equity flows by region, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td></tr><tr><td>Total Equities</td><td>0.0%</td><td>516,137</td></tr><tr><td>long-only funds</td><td>-0.1%</td><td>-285,653</td></tr><tr><td>ETFs</td><td>0.0%</td><td>802,094</td></tr><tr><td>Total EM</td><td>-0.1%</td><td>-135,297</td></tr><tr><td>Brazil</td><td>-0.7%</td><td>4,098</td></tr><tr><td>India</td><td>-0.3%</td><td>-8,829</td></tr><tr><td>China</td><td>-0.9%</td><td>-245,942</td></tr><tr><td>Total DM</td><td>0.0%</td><td>651,434</td></tr><tr><td>US</td><td>-0.1%</td><td>315,462</td></tr><tr><td>Europe</td><td>-0.2%</td><td>-15,052</td></tr><tr><td>Japan</td><td>0.2%</td><td>14,659</td></tr><tr><td>International</td><td>0.1%</td><td>313,720</td></tr></table>

Total Equities = Total EM + Total DM
Source: EPFR Global  
BofA GLOBAL RESEARCH

Chart 12: FICC inflows to HY bonds, cash, and bank loans Weekly FICC flows as a % AUM  
![](images/b8435788d6914ee5307b272f0b7ef8b63cad12a8c95221f9e704bed22219d3e6.jpg)  
Source: BofA Global Investment Strategy, EPFR Global  
BofA GLOBAL RESEARCH

## BofA private client flows & allocations

Chart 13: Private clients bought materials, healthcare, munis
BofA private clients 4-week ETF flows as % of AUM  
![](images/ae0619f81b6749a1e623c2f79b425c76bdf0160744943359791b060c5d02df43.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 14: GWIM equity allocation at 65%
BofA private client equity holdings as % of AUM  
![](images/ca1545e605aa21c12a89c9a74b63e0ccb5ba700e522b0dd6ec56006e7238c4dd.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 15: GWIM debt allocation at 18%
BofA private client debt holdings as % of AUM  
![](images/b59cf1dd685e18b566470dbe82b08b04825886e22476fc3e89b65e731817c405.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 16: GWIM cash allocation at 10%
BofA private client cash holdings as % of AUM  
![](images/d1c25273d39c9e53e85142cb15ff4d0b69701b6f17f692b43fa0da6b0ae5d400.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 17: GWIM equity ETFs 21%, debt ETFs 18% of AUM
BofA private client ETF holdings as % of AUM  
![](images/8a57c0734d64a5dabd0a918991ecaf98365fa4e1938318a1cbdc26f396b50ac1.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 18: \$49bn to T-notes vs \$27bn to T-bills since 2020
BofA private client cumulative inflow to Treasuries since 2020 (\$bn)  
![](images/e49ad533d8f5a7db5b0dc491c4d7abd75ea4e4ed4db24fe489ba5c4eb777a70a.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

## The Asset Class Quilt of Total Returns

Chart 19: Historical asset class performance by year
Ranked cross asset returns by year

<table><tr><td>2000</td><td>2001</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026*</td></tr><tr><td>Commodities 58.2%</td><td>US Treasuries 6.7%</td><td>Commodities 39.5%</td><td>MSCI EM 56.3%</td><td>REITS 32.0%</td><td>MSCI EM 34.5%</td><td>REITS 37.5%</td><td>MSCI EM 39.8%</td><td>US Treasuries 14.0%</td><td>MSCI EM 79.0%</td><td>Gold 29.2%</td><td>US Treasuries 9.8%</td><td>REITS 23.8%</td><td>S&amp;P 500 32.4%</td><td>S&amp;P 500 13.7%</td><td>S&amp;P 500 1.4%</td><td>Commodities 17.5%</td><td>MSCI EM 37.8%</td><td>Cash 1.8%</td><td>S&amp;P 500 31.5%</td><td>Gold 24.8%</td><td>Commodities 46.3%</td><td>Commodities 31.1%</td><td>S&amp;P 500 26.3%</td><td>Gold 26.7%</td><td>Gold 60.7%</td><td>Commodities 33.6%</td></tr><tr><td>US Treasuries 13.4%</td><td>Global IG 4.6%</td><td>Gold 25.6%</td><td>MSCI EAFE 39.2%</td><td>Commodities 28.7%</td><td>Commodities 33.7%</td><td>MSCI EM 32.6%</td><td>Commodities 33.0%</td><td>Gold 4.3%</td><td>Global HY 62.0%</td><td>MSCI EM 19.2%</td><td>Gold 8.9%</td><td>Global HY 19.3%</td><td>MSCI EAFE 23.3%</td><td>REITS 11.7%</td><td>US Treasuries 0.8%</td><td>Global HY 14.8%</td><td>MSCI EAFE 25.9%</td><td>US Treasuries 0.8%</td><td>REITS 27.4%</td><td>MSCI EM 18.8%</td><td>REITS 37.1%</td><td>Cash 1.5%</td><td>MSCI EAFE 18.9%</td><td>S&amp;P 500 25.0%</td><td>MSCI EM 32.0%</td><td>MSCI EM 24.0%</td></tr><tr><td>REITS 8.5%</td><td>Cash 4.4%</td><td>Global IG 14.9%</td><td>REITS 33.5%</td><td>MSCI EM 26.0%</td><td>Gold 17.8%</td><td>MSCI EAFE 26.9%</td><td>Gold 31.9%</td><td>Cash 2.1%</td><td>MSCI EAFE 32.5%</td><td>REITS 15.9%</td><td>Global IG 4.5%</td><td>MSCI EM 18.6%</td><td>Global HY 8.0%</td><td>US Treasuries 6.0%</td><td>Cash 0.1%</td><td>S&amp;P 500 12.0%</td><td>S&amp;P 500 22.0%</td><td>Gold -1.9%</td><td>MSCI EAFE 22.8%</td><td>S&amp;P 500 18.4%</td><td>S&amp;P 500 28.7%</td><td>Gold -0.8%</td><td>Global HY 13.4%</td><td>MSCI EM 8.0%</td><td>MSCI EAFE 29.0%</td><td>REITS 12.2%</td></tr><tr><td>Cash 6.2%</td><td>Global HY 3.1%</td><td>US Treasuries 11.6%</td><td>Commodities 30.1%</td><td>MSCI EAFE 20.7%</td><td>MSCI EAFE 14.0%</td><td>Gold 23.2%</td><td>MSCI EAFE 11.6%</td><td>Global IG -8.3%</td><td>REITS 31.7%</td><td>S&amp;P 500 15.1%</td><td>Global HY 2.6%</td><td>MSCI EAFE 17.9%</td><td>REITS 0.7%</td><td>Global IG 3.2%</td><td>MSCI EAFE -0.8%</td><td>MSCI EM 11.2%</td><td>Gold 12.9%</td><td>Global HY -3.3%</td><td>Commodities 20.1%</td><td>Global IG 10.3%</td><td>MSCI EAFE 11.9%</td><td>US Treasuries -12.9%</td><td>Gold 12.7%</td><td>Global HY 7.5%</td><td>S&amp;P 500 18.5%</td><td>S&amp;P 500 10.0%</td></tr><tr><td>Global IG 3.1%</td><td>Gold -0.7%</td><td>Cash 1.8%</td><td>Global HY 30.7%</td><td>Global HY 12.4%</td><td>REITS 10.7%</td><td>S&amp;P 500 15.8%</td><td>US Treasuries 9.1%</td><td>Global HY -27.9%</td><td>S&amp;P 500 26.5%</td><td>Global HY 13.9%</td><td>S&amp;P 500 2.1%</td><td>S&amp;P 500 16.0%</td><td>Global IG 0.1%</td><td>Gold 0.1%</td><td>REITS -3.4%</td><td>Gold 8.6%</td><td>REITS 11.5%</td><td>Global IG -3.4%</td><td>MSCI EM 18.6%</td><td>MSCI EAFE 8.4%</td><td>Global HY 1.4%</td><td>Global HY -13.2%</td><td>REITS 11.3%</td><td>Commodities 5.5%</td><td>Global HY 9.9%</td><td>MSCI EAFE 9.4%</td></tr><tr><td>Gold -5.4%</td><td>MSCI EM -2.4%</td><td>Global HY -1.1%</td><td>S&amp;P 500 28.7%</td><td>S&amp;P 500 10.9%</td><td>S&amp;P 500 4.9%</td><td>Global HY 13.5%</td><td>Global IG 7.3%</td><td>S&amp;P 500 -37.0%</td><td>Commodities 26.1%</td><td>Commodities 13.3%</td><td>Cash 0.1%</td><td>Global IG 11.1%</td><td>Cash 0.1%</td><td>Cash 0.0%</td><td>Global IG -3.8%</td><td>Global IG 4.3%</td><td>Global HY 10.2%</td><td>REITS -3.9%</td><td>Gold 17.9%</td><td>US Treasuries 8.2%</td><td>Cash 0.0%</td><td>MSCI EAFE -13.9%</td><td>MSCI EM 10.1%</td><td>Cash 5.3%</td><td>Global IG 9.8%</td><td>Cash 1.8%</td></tr><tr><td>Global HY -5.8%</td><td>REITS -7.8%</td><td>REITS -2.4%</td><td>Gold 19.9%</td><td>Global IG 9.4%</td><td>Cash 3.1%</td><td>Global IG 7.2%</td><td>S&amp;P 500 5.5%</td><td>Commodities -42.6%</td><td>Gold 25.0%</td><td>MSCI EAFE 8.2%</td><td>Commodities -2.6%</td><td>Gold 8.3%</td><td>Commodities -2.1%</td><td>Global HY -0.1%</td><td>Global HY -4.2%</td><td>REITS 1.3%</td><td>Global IG 9.3%</td><td>S&amp;P 500 -4.3%</td><td>Global HY 13.7%</td><td>Global HY 8.0%</td><td>MSCI EM -2.3%</td><td>Global IG -16.7%</td><td>Global IG 9.5%</td><td>MSCI EAFE 4.4%</td><td>US Treasuries 6.1%</td><td>Global HY 1.6%</td></tr><tr><td>S&amp;P 500 -9.1%</td><td>S&amp;P 500 -11.9%</td><td>MSCI EM -6.0%</td><td>Global IG 14.5%</td><td>Gold 4.6%</td><td>US Treasuries 2.8%</td><td>Cash 4.9%</td><td>Cash 5.0%</td><td>MSCI EAFE -43.1%</td><td>Global IG 19.2%</td><td>Global IG 6.0%</td><td>REITS -9.4%</td><td>US Treasuries 2.2%</td><td>MSCI EM -2.3%</td><td>MSCI EM -1.8%</td><td>Gold -10.4%</td><td>US Treasuries 1.1%</td><td>Commodities 7.6%</td><td>Commodities -13.1%</td><td>Global IG 11.4%</td><td>Cash 0.5%</td><td>US Treasuries -2.4%</td><td>S&amp;P 500 -18.1%</td><td>Cash 5.1%</t

[中间内容因长度限制已省略]

h information is distributed simultaneously to internal and client websites and other portals by BofA and is not publicly-available material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
