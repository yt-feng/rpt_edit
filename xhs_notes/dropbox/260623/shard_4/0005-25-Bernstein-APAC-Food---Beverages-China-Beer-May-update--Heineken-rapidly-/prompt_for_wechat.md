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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
APAC Food & Beverages

# China Beer May update: Heineken rapidly accelerating while Bud still languishes

![](images/a155a8007989766b4016ecc8d8f9cf6a20786cbdc53a98d07a8d7cfb03f50d9e.jpg)  
Euan McLeish  
+81 3 5962 9611  
euan.mcleish@bernsteinsg.com

![](images/837643d63510e7942c73ecce021563ed278bfa2173a97ca789bc92812e052f1b.jpg)

Hao Wang, CFA

+852 2123 2627

hao.wang@bernsteinsg.com

![](images/57f4c1274d6a8d09ee19c742e0cd19360dcf2b3012f908e9add47fb2e756a13d.jpg)

Mufei Gao

+81 3 6777 6995

mufei.gao@bernsteinsg.com

China beer total sell-out value was +2% in May 2026, reflecting a small step up from April's 1% growth. Restaurant channel value growth continued in line with April at +3%, while off-trade value growth improved to +1% from -1% in April. Yanjing (not covered) was again the strongest performer in May with value +17% YoY (slowing down somewhat from April's +19%), followed by Chongqing (not covered) at +9% and CRBeer +3%, while Tsingtao value was -2%, and Bud China again underperforming the industry with a -3% decline.

Our regressions now indicate that CRBeer's topline growth will accelerate to c. 2% in Q2, Bud China's decline will narrow to c. -2%, and Tsingtao's will widen to c. -3% based on the Q2 to date monthly sales. We have observed a 96% correlation between Bud's reported growth over the last 15 months, compared to 84% for Yanjing, 81% for Tsingtao and Chongqing at 73%. CRBeer's correlation is low given they only report semi-annually.

Total off-trade beer sales improved MoM in all five key provinces, led by Zhejiang and Jiangsu which improved to +11%/+5%, from -7%/-11%, and Guangdong's off-trade growth continued to accelerate to +14% YoY vs +10% in April. All segments, other than MS+, bounced back to growth in the off-trade. In the restaurant channel, Guangdong again outperformed at +20% but we still haven't seen this filter through to Bud China. Shandong led the decline at -20%, dragging Tsingtao down. Premium segment value was up 8%, while Super Premium and M/S&Econ both declined in May.

CRBeer's April value growth came in at +3% in May, ahead of April's +2% but below Q1's +4% average yoy. CRBeer outperformed the Premium segment (+11% vs overall segment +5%) in May, driven by Heineken at +37%, with 11% value growth in both channels and both accelerating vs April. Overall, CRB grew value in both channels in May and the most pronounced growth was recorded in Guangdong and Fujian provinces where both channels registered double-digit growths in both channels (Exhibit 21).

Bud China's value was $-3\%$ again in May, similar to April and up from $-8\%$ in Q1 and $-11\%$ in Q4. Both channels showed modest trajectory improvement, but the lack of material uptick in the off-trade (- $10\%$ in May vs $-12\%$ in March & April) suggests that Bud's route to market expansion strategy is yet to deliver the goods. Bud improved in both channels in Zhejiang and also in Premium (Exhibit 19), but performance in the Guangdong restaurant channel slowed down and was materially behind overall channel performance.

Tsingtao's May value was -2% YoY, in line with Q1's -2% but marginally below March's 0% and April's -1%. Its home province Shandong (36% of Tsingtao's national sell-out value) was the biggest drag in the month with provincial value in restaurant channel performing much worse than March and April (Exhibit 25).

Chongqing (not covered) overall value was +9% YoY in May, in line with +9% in the

$1^{st}$ Quarter but slowing down from April's +12%, as the restaurant channel delivered significant sequential improvement in key provinces apart from Guangdong, but off-trade channel deteriorated in the month.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="3">22 Jun 2026</td><td colspan="2">TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td></td><td colspan="2">Closing</td><td>Price</td><td>Rel.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Price</td><td>Target</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>1876.HK (Bud APAC)</td><td>M</td><td>HKD</td><td>6.46</td><td>7.60</td><td>(66.4)%</td><td>USD</td><td>0.04</td><td>0.05</td><td>0.05</td><td>22.2</td><td>17.6</td><td>15.4</td></tr><tr><td>291.HK (CRB)</td><td>O</td><td>HKD</td><td>21.42</td><td>46.00</td><td>(57.8)%</td><td>CNY</td><td>1.80</td><td>1.98</td><td>2.17</td><td>10.3</td><td>9.3</td><td>8.5</td></tr><tr><td>168.HK (Tsingtao)</td><td>O</td><td>HKD</td><td>44.88</td><td>71.00</td><td>(58.4)%</td><td>CNY</td><td>3.36</td><td>3.53</td><td>3.60</td><td>11.5</td><td>11.0</td><td>10.8</td></tr><tr><td>600600.CH (Tsingtao)</td><td>M</td><td>CNY</td><td>53.92</td><td>62.00</td><td>(71.2)%</td><td>CNY</td><td>3.36</td><td>3.53</td><td>3.60</td><td>16.0</td><td>15.3</td><td>15.0</td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,048.07</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate CRBeer Outperform with a Price Target of HK\$46. Model: 291.HK

We rate Tsingtao H-Share Outperform with a Price Target of HK\$71 and Tsingtao's A-share Market-Perform with a Price Target of RMB62. Model: 168.HK

We rate Bud APAC Market-Perform with a Price Target of HK\$7.60. Model: 1876.HK

## DETAILS

EXHIBIT 1: Our regressions now indicate that CRBeer's topline growth will accelerate to c. 2% in Q2, Bud China's decline will narrow to c. -2%, and Tsingtao's to widen to c. -3% based on our regression formulae and the Q2 to date monthly sales.

China Beer Q1 Actual & Q2 Regression-based Revenue YoY % Est.

![](images/03f326730aa3c9ef7636cd45dcc10f826e852e8e28f0940d98f3c52c9489907b.jpg)  
Regression is based on Jan-May for CRBeer and Apr-May for the rest; CRBeer's two bars are 2H25 actual and 1H26 est. based on regression Source: BigOne Lab, company reports, Bernstein analysis and estimates  
Regression R-square of BigOne National Sell-out Value YoY % vs Reported Beer Revenue YoY % (22Q3-26Q1)

EXHIBIT 2: We see a 73-96% correlation between BigOne Lab quarterly brewer value growth and reported revenue growth

![](images/7b58d4a0ce695ed9810a6750409b9dfe1e129c7c6a631e9835145c75ea93a3a6.jpg)  
CRBeer reports semi-annually  
Source: BigOne Lab, company reports, Bernstein analysis

## MONTHLY OVERVIEW

Our BigOne Lab China beer data set leverages the POS sell-out data to track 180k supermarket stores and menu QR code data for 230k restaurant outlets nationally, allowing us to track brewer sell-out value performance by province and price segment on a monthly basis. The data set does not cover the nightlife channel, however.

In May 2026 we saw 3-month rolling overall national beer value growth (i.e Off-Trade + Restaurant channel) +2% in the period ending May 31 (Exhibit 3). Comparing May vs April and March, May standalone value was +1% YoY, slightly better than March's -1% and April's +1%. Monthly value growth performance improved for CRBeer, Bud was at similar rate vs April, and all others saw deterioration in the month. By brewer, Yanjing (not covered) was again the strongest performer in May with value +17% YoY (slowing down somewhat from April's +19%), followed by Chongqing at +9% and CRBeer +3%, while Tsingtao value was -2%, and Bud China again underperforming the industry with a -3% decline in the month.

Going into June, comps are similar versus May (Exhibit 14), before they become much tougher in July for most brewers apart from Bud China and Yanjing.

EXHIBIT 3: In May 2026 we saw a marginal growth in national beer value growth

China Total Beer Value Growth (Rolling 3-month / Monthly YoY %)  
![](images/3ff2dc0a29168f2a2ba4b42d1109006e52b05bacbfe05527bb64f15345f6df60.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 4: In May, Restaurant channel value was again in growth  
China Restaurant Beer Value Growth Monthly YoY %  
![](images/208ced775340ba07d63e28c499e26c801602871e2c82e851c279b3e239702a4b.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 5: Off-trade value was in marginal growth at +1% YoY in the month  
China Off-Trade Beer Value Growth Monthly YoY %  
![](images/352a2af896b3be785c638238499108569cea89a94b13868d9cfb02377055e86d.jpg)  
Source: BigOne Lab, Bernstein analysis  
China Total Beer Value Growth YoY% by Brewer

EXHIBIT 6: In Q1 Bud China / Chongqing / Yanjing performed sequentially better than Q4

![](images/29e83de757cd3b126100d92be5e9bec5d595faf7caab030267c042c34dd3fd7b.jpg)  
EXHIBIT 7: Monthly value growth improved for CRBeer but worsened for Chongqing / Yanjing / Tsingtao in May vs April  
Bernstein does not cover Yanjing or Chongqing Source: BigOne Lab, Bernstein analysis

China Total Beer Value Growth YoY% by Brewer  
![](images/013629f10f780bf23d5da287002c8ece0feca132aca4064878c434cfa8ba98f8.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 8: Yanjing materially outperformed in most segments in the month  
Beer Value YoY % in May 2026 by Segment by Brewer (Both Channel)  
![](images/83c7fef70611ede46b2f961fe13e638ee524a3019421d9986050e482c875b1db.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 9: Yanjing & Chongqing were top in share gains while Bud China's share loss narrowed  
China Total Beer Value Share Gain/Loss (YoY in bps)

![](images/2d7fb9f91539b092dcfe22aa8bfda481d2aa229a7fa53411bb2c248ef96bbf9f.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 10: And similarly in May vs April  
China Total Beer Value Share Gain/Loss (YoY in bps)

![](images/9a7f20bca067a3ec89658eaea884187165beb894b389a05ac460f6d17345ffbd.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 11: At the national level Bud China's share loss was across the board in May while CRB gained the most in Super Premium and M/S&Econ  
May '26 National Segment Share Gain/Loss in bps YoY  
![](images/2801914be3f6d74ea7745c2080c15b5aca868f1244e343e2e6c6597bf66e8a2f.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 12: In the Off-Trade, Bud China was maintaining its share in MS+  
May '26 National Off-Trade Segment Share Gain/Loss in bps YoY

![](images/58c6a588bf7c7495cbaa56999d5029bab09475db454005ad6a767532cf68346a.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 13: And they even gained share in Premium segment of Restaurant channel  
May '26 National Restaurant Segment Share Gain/Loss in bps YoY

![](images/11131cb6e2f74cb5bd92100f842974d7142e0daf19847e983a215c25272ae30b.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 14: In June comps are softer for CRBeer and Bud China but tougher for Chongqing and Yanjing

Forthcoming Comps - China Total Beer Value Growth YoY% by Brewer

![](images/f31b614c63500b2a6c0b09de64e57fe2078e9f8647966ec8464bc9cc6b98c4ea.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 15: By province Jiangsu and Zhejiang were improving MoM in May while Fujian and Shandong decelerated

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">COMBINED CHANNELS</td></tr><tr><td>Mar-2026</td><td>Apr-2026</td><td>May-2026</td><td>Last 3m Avg</td></tr><tr><td rowspan="7">By Province</td><td>Guangdong</td><td>17%</td><td>7%</td><td>16%</td><td>17%</td><td>14%</td></tr><tr><td>Fujian</td><td>5%</td><td>-1%</td><td>1%</td><td>0%</td><td>0%</td></tr><tr><td>Zhejiang</td><td>7%</td><td>-6%</td><td>-2%</td><td>11%</td><td>2%</td></tr><tr><td>Jiangsu</td><td>6%</td><td>-7%</td><td>-6%</td><td>5%</td><td>-2%</td></tr><tr><td>Shandong</td><td>12%</td><td>-6%</td><td>-11%</td><td>-14%</td><td>-11%</td></tr><tr><td>Others</td><td>53%</td><td>-2%</td><td>1%</td><td>0%</td><td>0%</td></tr><tr><td>Total</td><td></td><td>-1%</td><td>1%</td><td>2%</td><td>1%</td></tr><tr><td rowspan="5">By Segment</td><td>Super Premium</td><td>5%</td><td>-19%</td><td>-18%</td><td>-10%</td><td>-15%</td></tr><tr><td>Premium</td><td>42%</td><td>1%</td><td>4%</td><td>5%</td><td>4%</td></tr><tr><td>Mainstream+</td><td>28%</td><td>2%</td><td>3%</td><td>0%</td><td>2%</td></tr><tr><td>M/S &amp; Eco</td><td>26%</td><td>-5%</td><td>-2%</td><td>2%</td><td>-2%</td></tr><tr><td>Total</td><td></td><td>-1%</td><td>1%</td><td>2%</td><td>1%</td></tr></table>

Source: BigOne Lab, Bernstein analysis

EXHIBIT 16: National monthly growth diagnostic by Province and Segment and Channel

<table><tr><td rowspan="3" colspan="2"></td><td colspan="5">RESTAURANT CHANNEL</td><td colspan="5">OFF-TRADE CHANNEL</td></tr><tr><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">Brewer&#x27;s Value Growth YoY %</td><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">Brewer&#x27;s Value Growth YoY %</td></tr><tr><td>Mar-2026</td><td>Apr-2026</td><td>May-2026</td><td>Last 3m Avg</td><td>Mar-2026</td><td>Apr-2026</td><td>May-2026</td><td>Last 3m Avg</td></tr><tr><td rowspan="7">By Province</td><td>Guangdong</td><td>15%</td><td>8%</td><td>22%</td><td>20%</td><td>17%</td><td>19%</td><td>6%</td><td>10%</td><td>14%</td><td>10%</td></tr><tr><td>Fujian</td><td>5%</td><td>8%</td><td>3%</td><td>1%</td><td>4%</td><td>4%</td><td>-8%</td><td>-3%</td><td>0%</td><td>-3%</td></tr><tr><td>Zhejiang</td><td>7%</td><td>-2%</td><td>3%</td><td>12%</td><td>5%</td><td>8%</td><td>-10%</td><td>-7%</td><td>11%</td><td>0%</td></tr><tr><td>Jiangsu</td><td>5%</td><td>-1%</td><td>1%</td><td>4%</td><td>2%</td><td>7%</td><td>-12%</td><td>-11%</td><td>5%</td><td>-5%</td></tr><tr><td>Shandong</td><td>16%</td><td>-10%</td><td>-16%</td><td>-20%</td><td>-16%</td><td>8%</td><td>7%</td><td>0%</td><td>1%</td><td>2%</td></tr><tr><td>Others</td><td>52%</td><td>1%</td><td>4%</td><td>5%</td><td>4%</td><td>54%</td><td>-5%</td><td>-3%</td><td>-5%</td><td>-4%</td></tr><tr><td>Total</td><td></td><td>0%</td><td>3%</td><td>3%</td><td>2%</td><td></td><td>-3%</td><td>-1%</td><td>1%</td><td>-1%</td></tr><tr><td rowspan="5">By Segment</td><td>Super Premium</td><td>6%</td><td>-26%</td><td>-23%</td><td>-16%</td><td>-21%</td><td>3%</td><td>-5%</td><td>-6%</td><td>5%</td><td>-1%</td></tr><tr><td>Premium</td><td>50%</td><td>5%</td><td>9%</td><td>8%</td><td>8%</td><td>33%</td><td>-5%</td><td>-3%</td><td>1%</td><td>-2%</td></tr><tr><td>Mainstream+</td><td>32%</td><td>1%</td><td>4%</td><td>2%</td><td>3%</td><td>23%</td><td>3%</td><td>3%</td><td>-2%</td><td>1%</td></tr><tr><td>M/S &amp; Eco</td><td>12%</td><td>-13%</td><td>-8%</td><td>-4%</td><td>-8%</td><td>41%</td><td>-4%</td><td>-2%</td><td>3%</td><td>0%</td></tr><tr><td>Total</td><td></td><td>0%</td><td>3%</td><td>3%</td><td>2%</td><td></td><td>-3%</td><td>-1%</td><td>1%</td><td>-1%</td></tr></table>

Source: BigOne Lab, Bernstein analysis

## OFF-TRADE / RESTAURANT CHANNEL MOMENTUM BY BREWER

## BUD CHINA

Guangdong and Zhejiang were the largest contributors to Bud China's growth in the Restaurant channel (Exhibit 17). And similarly is Premium segment in the same channel (Exhibit 18), while in the off-trade Mainstream+ delivered marginal decline in the month.

Comparing May vs April, Bud's performance in the off-trade channel improved slightly on a national basis, and particularly in ZJ&JS, and also in the M/S&Econ segment. In the restaurant channel, we saw relatively better performance in ZJ&HeN and the Premium segment (Exhibit 19).

EXHIBIT 17: Bud China Value bridge by PROVINCE

Bud China Value Bridge by PROVINCE (Indexed to May '25 = 100)

![](images/14f6137f2e5a6e16ce470b8cdc7b6e8314a26cfcd5742e3903cabdb524330cac.jpg)  
Source: BigOne Lab, Bernstein analysis  
Restaurant Channel

![](images/3627a0b45866d41bd934f26f98767e482e97a08c288d80571475359239bc12cc.jpg)

EXHIBIT 18: Bud China Value bridge by SEGMENT
Bud China Value Bridge by SEGMENT (Indexed to May '25 = 100)  
![](images/2d206a6cb40a3dff561e477a9c9752fe477874a2abc36fbacd08fec0ec40ccb1.jpg)  
Source: BigOne Lab, Bernstein analysis

![](images/1432801ec9e7dc1588b615d6e81fc43806e50d88adfdb3f9d501e597de9a7917.jpg)

EXHIBIT 19: Bud China monthly growth diagnostic by Province and Segment and Channel

<table><tr><td rowspan="3" colspan="2"></td><td colspan="5">RESTAURANT CHANNEL</td><td colspan="5">OFF-TRADE CHANNEL</td></tr><tr><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">Brewer&#x27;s Value Growth YoY %</td><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">Brewer&#x27;s Value Growth YoY %</td></tr><tr><td>Mar-2026</td><td>Apr-2026</td><td>May-2026</td><td>Last 3m Avg</td><td>Mar-2026</td><td>Apr-2026</td><td>May-2026</td><td>Last 3m Avg</td></tr><tr><td rowspan="7">By Province</td><td>Guangdong</td><td>34%</td><td>-10%</td><td>9%</td><td>5%</td><td>2%</td><td>31%</td><td>-10%</td><td>-7%</td><td>-5%</td><td>-7%</td></tr><tr><td>Fujian</td><td>10%</td><td>-23%</td><td>-17%</td><td>-23%</td><td>-21%</td><td>10%</td><td>-22%</td><td>-20%</td><td>-19%</td><td>-21%</td></tr><tr><td>Zhejiang</td><td>15%</td><td>-9%</td><td>2%</td><td>8%</td><td>1%</td><td>12%</td><td>-6%</td><td>-8%</td><td>3%</td><td>-3%</td></tr><tr><td>Jiangsu</td><td>5%</td><td>-7%</td><td>9%</td><td>7%</td><td>4%</td><td>6%</td><td>-12%</td><td>-17%</td><td>-2%</td><td>-10%</td></tr><tr><td>Henan</td><td>4%</td><td>-33%</td><td>-29%</td><td>-16%</td><td>-25%</td><td>5%</td><td>-26%</td><td>-23%</td><td>-26%</td><td>-25%</td></tr><tr><td>Others</td><td>33%</td><td>-11%</td><td>1%</td><td>6%</td><td>-1%</td><td>35%</td><td>-9%</td><td>-12%</td><td>-15%</td><td>-13%</td></tr><tr><td>Total</td><td></td><td>-12%</td><td>1%</td><td>2%</td><td>-2%</td><td></td><td>-12%</td><td>-12%</td><td>-10%</td><td>-11%</td></tr><tr><td rowspan="5">By Segment</td><td>Super Premium</td><td>4%</td><td>-56%</td><td>-38%</td><td>-33%</td><td>-42%</td><td>3%</td><td>-22%</td><td>-23%</td><td>-12%</td><td>-19%</td></tr><tr><td>Premium</td><td>75%</td><td>-4%</td><td>8%</td><td>10%</td><td>5%</td><td>53%</td><td>-13%</td><td>-17%</td><td>-17%</td><td>-16%</td></tr><tr><td>Mainstream+</td><td>17%</td><td>-27%</td><td>-9%</td><td>-17%</td><td>-17%</td><td>15%</td><td>-7%</td><td>2%</td><td>-2%</td><td>-2%</td></tr><tr><td>M/S &amp; Eco</td><td>4%</td><td>-43%</td><td>-30%</td><td>-17%</td><td>-28%</td><td>30%</td><td>-10%</td><td>-8%</td><td>-2%</td><td>-6%</td></tr><tr><td>Total</td><td></td><td>-12%</td><td>1%</td><td>2%</td><td>-2%</td><td></td><td>-12%</td><td>-12%</td><td>-10%</td><td>-11%</td></tr></table>

Source: BigOne Lab, Bernstein analysis

## CRBEER

Both channels' value growths were in positive range in April for CRBeer, and was most prominent in Guangdong and Fujian for both off-trad

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
