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
# JPM

## China Property

## Why the recent share price weakness?

Over the past 4 trading days, China Property has underperformed the HSI by $9\%$ . While high-frequency data (after adjustments as last week's data was disrupted by public holidays) maintains a similar trend vs. the past few months, we believe the share price weakness has mostly been driven by (1) negative read-through from weakening consumption data; (2) the sector's higher-beta nature amid the broader market sell-off; (3) a lack of near-term catalysts especially when high-frequency data is, while intact, not turning significantly better; (4) some investors may have focused on the weaker M/M secondary sales volume; however, in our view, this not an accurate way to gauge the market well-being due to seasonality (March & April typically see stronger sales), and thus Y/Y would be more reasonable. Even for leading SOEs like CRL & COLI, while their share prices had been relatively resilient throughout May & the first half of June (Figure 7), they both abruptly corrected $11\%$ (HSI: $-2\%$ ) over the past 2 trading days. We believe this was due to profit-taking amid broader market weakness as both stocks remain outperformers year-to-date. In fact, even after the correction, year-to-date, CRL $(+15\%) / \text{COLI} (+7\%)$ are still outperforming the HSI $(-7\%)$ (Figure 6). However, as data in tier-1 cities continues to show stabilization, on dips we'd selectively buy SOE developers with (1) outperforming sales growth; (2) strong exposure to tier-1 cities (COLI, CRL & Jinmao), but we remain cautious on most non-SOE developers (e.g. Vanke, Sunac) who may not benefit from the K-shaped stabilization.

## A quick look at the latest high-frequency data

\- Iceberg Index real-time secondary data (冰山指数实时二手成交): As of 21 June, 9-city (excluding Shanghai as data is not yet available as of the time of writing) real-time weekly secondary sales marginally rose $1\%$ Y/Y (down from $+12\%$ Y/Y). However, the drop is mainly due to the Dragonboat Festival. If we compare last week's data to the week last year with the Dragonboat Festival, the Y/Y growth would be $+15\%$ Y/Y, which is similar to the range $(10 - 20\%$ Y/Y) in previous weeks.

\- Iceberg Index tier-1 city secondary listings (冰山指数二手挂牌量): Likely under-appreciated by the market, the volume of secondary listings in tier-1 cities has been consistently coming down (dropped $2.5\%$ from the peak in March), and this is a key factor that will support continual secondary home price stabilization.

\- Sales registrations (official data with lag of a few weeks): The 60-city primary weekly sales registrations (一手网签) fell $23\%$ Y/Y, mostly due to the inclusion of the 3-day Dragon Boat Festival (during public holidays, sales registrations are significantly lower than usual). Compared to the same 3-day Dragon Boat Festival period in 2025, sales registrations were up $60\%$ Y/Y (but the sample size is too small, so we do not think this alone is representative). Similarly, the 12-city secondary sales registrations (二手网签) fell $13\%$ Y/Y (for a similar reason), reversing the positive Y/Y growth for the past 9 weeks. We expect both the primary & secondary sales registrations to see solid W/W

Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC (852) 2800-8513 karl.chan@JPM.com

Jocelyn Gao (852) 2800-8529 jocelyn.gao@JPM.com

(852) 2800-8599

venus.choi@JPM.com

JPM Securities (Asia Pacific) Limited/JPM Broking (Hong Kong) Limited

improvement due to the quarter-end-loaded nature of sales registrations, but we believe Y/Y growth is a more accurate way to assess market trend.

\- Home price stabilization in tier-1 cities has continued into May: According to the NBS home price index, tier-1 cities continued to register positive M/M growth (+0.2% in primary; +0.3% in secondary) in May (the $3^{rd}$ consecutive month). For the Centraline tier-1 secondary home price index, although the M/M growth slowed from +0.6% in April to +0.3% in May, this was the $4^{th}$ consecutive month of positive M/M growth. For more discussion, please see our earlier report with commentary on the latest NBS data.

## Iceberg Index – real time data

Figure 1: Iceberg Index - 10-city real time secondary daily sales since April 2026 (冰山指数实时二手成交)  
![](images/0a0bab2195a638ad5bb6df97b95af5881e1579e1572e1c739c95740dec8500e9.jpg)  
Source: Iceberg Index, JPM  
Note: The data for the last week is excluded as Shanghai data is not yet available. Please check our "Property Data Monitor" report for subsequent updates.

Figure 2: Iceberg Index - tier-1 cities' secondary listing volume (冰山指数二手挂牌量)  
No. of secondary listings ('000 units) - Tier 1 cities  
![](images/5271c35f7b5ec1219c86ddc7f2352935ed3b4d67c2ec86c9bd563f3efa0762e6.jpg)  
Source: Iceberg Index, JPM

## Official sales registrations (lag of a few weeks)

Figure 3: 60-city weekly primary sales registrations (一手网签) – compared with 2019-25  
![](images/240ae6a1af05cfcc1d2f77be2617707ab57419d000a9449e024284b75945fcb3.jpg)  
Source: CREIS  
Note: The steeper Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holidays).

Figure 4: 60-city weekly primary sales registrations (一手网签)  
![](images/7682170656aa19cf460030520e7dcf98f4521db303291f7bd81657a2080032cd.jpg)  
Source: CREIS  
Note: The Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holidays).

Table 1: 12-city primary sales registrations (一手网签) (comparing first 3 days of Dragon Boat Festival only)

<table><tr><td colspan="3">Primary - First 3 days of Dragon Boat Festival</td></tr><tr><td>Year</td><td>No. of units sold</td><td>2026 vs.</td></tr><tr><td>2020</td><td>17,067</td><td>-67%</td></tr><tr><td>2021</td><td>8,490</td><td>-34%</td></tr><tr><td>2022</td><td>5,319</td><td>6%</td></tr><tr><td>2023</td><td>5,535</td><td>2%</td></tr><tr><td>2024</td><td>3,919</td><td>44%</td></tr><tr><td>2025</td><td>3,519</td><td>60%</td></tr><tr><td>2026</td><td>5,628</td><td></td></tr></table>

Source: CREIS  
Note: As the sample size is small, the Y/Y growth may not necessarily be representative.

Figure 5: 8-city secondary sales registrations (二手网签)  
![](images/83c284fa3f7c4432ef2bb90aca1b18048b256e72f3c24521751bc398cadf7af8.jpg)  
Source: CREIS  
Note: The Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holidays).

## Home price trend

Table 2: Monthly home price index in tier-1 cities

<table><tr><td></td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td colspan="14">Primary (NBS)</td></tr><tr><td>Beijing</td><td>-0.4%</td><td>-0.3%</td><td>0.0%</td><td>-0.4%</td><td>0.2%</td><td>-0.1%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.0%</td><td>-0.2%</td><td>-0.2%</td></tr><tr><td>Shanghai</td><td>0.7%</td><td>0.4%</td><td>0.3%</td><td>0.4%</td><td>0.3%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td><td>0.0%</td><td>0.2%</td><td>0.3%</td><td>0.4%</td><td>0.2%</td></tr><tr><td>Guangzhou</td><td>-0.8%</td><td>-0.5%</td><td>-0.3%</td><td>-0.2%</td><td>-0.6%</td><td>-0.8%</td><td>-0.5%</td><td>-0.6%</td><td>-0.6%</td><td>0.0%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td></tr><tr><td>Shenzhen</td><td>-0.4%</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>-1.0%</td><td>-0.7%</td><td>-0.9%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.1%</td><td>0.4%</td></tr><tr><td>Tier-1 Primary (NBS)</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.3%</td><td>-0.3%</td><td>-0.5%</td><td>-0.3%</td><td>-0.3%</td><td>0.0%</td><td>0.2%</td><td>0.1%</td><td>0.2%</td></tr><tr><td colspan="14">Secondary (NBS)</td></tr><tr><td>Beijing</td><td>-0.8%</td><td>-1.0%</td><td>-1.1%</td><td>-1.2%</td><td>-0.9%</td><td>-1.1%</td><td>-1.3%</td><td>-1.3%</td><td>-0.2%</td><td>0.3%</td><td>0.6%</td><td>0.4%</td><td>0.1%</td></tr><tr><td>Shanghai</td><td>-0.7%</td><td>-0.7%</td><td>-0.9%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.6%</td><td>-0.4%</td><td>0.2%</td><td>0.4%</td><td>0.7%</td><td>0.6%</td></tr><tr><td>Guangzhou</td><td>-0.8%</td><td>-0.7%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.9%</td><td>-1.2%</td><td>-1.0%</td><td>-0.7%</td><td>-0.5%</td><td>0.2%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>Shenzhen</td><td>-0.5%</td><td>-0.5%</td><td>-0.9%</td><td>-0.8%</td><td>-1.0%</td><td>-0.9%</td><td>-1.0%</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>0.4%</td><td>0.3%</td><td>0.6%</td></tr><tr><td>Tier-1 Secondary (NBS)</td><td>-0.7%</td><td>-0.7%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.9%</td><td>-1.1%</td><td>-0.9%</td><td>-0.5%</td><td>-0.1%</td><td>0.4%</td><td>0.4%</td><td>0.3%</td></tr><tr><td colspan="14">Secondary (Centaline)</td></tr><tr><td>Beijing</td><td>-0.9%</td><td>-1.6%</td><td>-1.5%</td><td>-1.8%</td><td>-2.1%</td><td>-1.9%</td><td>-1.9%</td><td>-1.9%</td><td>-0.5%</td><td>1.2%</td><td>1.5%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>Shanghai</td><td>-1.4%</td><td>-1.4%</td><td>-1.7%</td><td>-1.7%</td><td>-1.5%</td><td>-2.2%</td><td>-2.0%</td><td>-2.8%</td><td>-0.5%</td><td>0.9%</td><td>1.0%</td><td>1.6%</td><td>0.9%</td></tr><tr><td>Guangzhou</td><td>-1.0%</td><td>-1.4%</td><td>-1.2%</td><td>-1.8%</td><td>-1.4%</td><td>-2.0%</td><td>-1.9%</td><td>-1.3%</td><td>-0.8%</td><td>-1.5%</td><td>0.8%</td><td>-0.3%</td><td>-0.2%</td></tr><tr><td>Shenzhen</td><td>-1.1%</td><td>-0.5%</td><td>-1.1%</td><td>-1.0%</td><td>-1.5%</td><td>-0.5%</td><td>-1.0%</td><td>-1.6%</td><td>-1.3%</td><td>0.9%</td><td>0.1%</td><td>1.0%</td><td>0.1%</td></tr><tr><td>Tier-1 Secondary (Centaline)</td><td>-1.1%</td><td>-1.2%</td><td>-1.4%</td><td>-1.6%</td><td>-1.6%</td><td>-1.6%</td><td>-1.7%</td><td>-1.9%</td><td>-0.8%</td><td>0.4%</td><td>0.9%</td><td>0.6%</td><td>0.3%</td></tr></table>

Source: NBS, Centraline

Sector share price performance

Figure 6: China property – year-to-date share price performance by stock

![](images/01aae231d85b523f2bd65f456046924e5b0e8e1c88f3bf766b617c1115227035.jpg)  
Source: Bloomberg Finance L.P. as of 22 June 2026, JPM

Figure 7: MSCI China Real Estate Index vs. HSI, year-to-date  
![](images/4a81120f9d91c6d31b7fd6922d79f4d86e730a416bc8dd74899f9c9abd29333a.jpg)  
Source: Bloomberg Finance L.P. as of 22 June 2026, JPM  
Note: normalized to 100 as of 5 January 2026

## Valuation Summary

Table 3: China property – valuation summary

<table><tr><td rowspan="2">Company</td><td rowspan="2">Stock Code</td><td rowspan="2">JPM Rating</td><td rowspan="2">Last Close (HK$)</td><td rowspan="2">Market Cap US$M</td><td rowspan="2">ADV US$M</td><td colspan="2">P/E</td><td colspan="2">Dvd Yield</td><td colspan="2">P/B</td><td colspan="4">Share price return</td></tr><tr><td>1FY (x)</td><td>2FY (x)</td><td>1FY (%)</td><td>2FY (%)</td><td>1FY (x)</td><td>2FY (x)</td><td>5D</td><td>YTD</td><td>1Y</td><td>vs. AT high</td></tr><tr><td colspan="16">Mainland China Developers</td></tr><tr><td>China Resources Land</td><td>1109.HK</td><td>OW</td><td>31.18</td><td>28,362</td><td>110.2</td><td>9.0</td><td>8.9</td><td>4.1%</td><td>4.2%</td><td>0.6</td><td>0.6</td><td>-14%</td><td>18%</td><td>22%</td><td>-25%</td></tr><tr><td>China Overseas Land</td><td>0688.HK</td><td>OW</td><td>13.13</td><td>18,331</td><td>64.6</td><td>10.4</td><td>9.4</td><td>3.5%</td><td>3.9%</td><td>0.3</td><td>0.3</td><td>-16%</td><td>7%</td><td>2%</td><td>-60%</td></tr><tr><td>China Jinmao</td><td>0817.HK</td><td>OW</td><td>1.35</td><td>2,327</td><td>10.8</td><td>21.1</td><td>16.8</td><td>2.6%</td><td>2.7%</td><td>0.4</td><td>0.4</td><td>-16%</td><td>12%</td><td>25%</td><td>-79%</td></tr><tr><td>C&amp;D International</td><td>1908.HK</td><td>NC</td><td>12.96</td><td>3,703</td><td>14.6</td><td>6.9</td><td>6.3</td><td>7.7%</td><td>8.6%</td><td>0.7</td><td>0.7</td><td>-16%</td><td>-12%</td><td>-15%</td><td>-53%</td></tr><tr><td>Greentown China</td><td>3900.HK</td><td>NC</td><td>6.97</td><td>2,258</td><td>13.1</td><td>32.7</td><td>16.4</td><td>2.2%</td><td>4.8%</td><td>0.4</td><td>0.4</td><td>-17%</td><td>-18%</td><td>-23%</td><td>-65%</td></tr><tr><td>Yuexiu Property</td><td>123.HK</td><td>NC</td><td>3.71</td><td>1,905</td><td>6.1</td><td>33.7</td><td>17.6</td><td>2.6%</td><td>4.5%</td><td>0.2</td><td>0.2</td><td>-17%</td><td>-6%</td><td>-8%</td><td>-81%</td></tr><tr><td>Poly Property</td><td>119.HK</td><td>NC</td><td>1.66</td><td>809</td><td>5.0</td><td>22.7</td><td>10.5</td><td>1.7%</td><td>5.7%</td><td>0.2</td><td>0.2</td><td>-13%</td><td>-16%</td><td>20%</td><td>-87%</td></tr><tr><td colspan="5">SOEs</td><td>76.9</td><td>11.7</td><td>9.8</td><td>3.9%</td><td>4.4%</td><td>0.5</td><td>0.5</td><td>-15%</td><td>10%</td><td>10%</td><td>-44%</td></tr><tr><td>Longfor</td><td>0960.HK</td><td>OW</td><td>6.60</td><td>5,975</td><td>21.6</td><td>-</td><td>-</td><td>0.0%</td><td>1.1%</td><td>0.2</td><td>0.2</td><td>-25%</td><td>-22%</td><td>-27%</td><td>-88%</td></tr><tr><td>Seazen Group</td><td>1030.HK</td><td>N</td><td>1.45</td><td>1,344</td><td>6.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.2</td><td>0.2</td><td>-13%</td><td>-29%</td><td>-37%</td><td>-87%</td></tr><tr><td colspan="5">POEs</td><td>18.7</td><td>-</td><td>-</td><td>0.0%</td><td>0.9%</td><td>0.2</td><td>0.2</td><td>-22%</td><td>-24%</td><td>-29%</td><td>-88%</td></tr><tr><td>China Vanke - H</td><td>2202.HK</td><td>UW</td><td>2.47</td><td>5,158</td><td>8.7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.3</td><td>0.3</td><td>-6%</td><td>-25%</td><td>-47%</td><td>-94%</td></tr><tr><td>Country Garden</td><td>2007.HK</td><td>UW</td><td>0.19</td><td>1,146</td><td>12.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-8%</td><td>-53%</td><td>-50%</td><td>-99%</td></tr><tr><td>Sunac China</td><td>1918.HK</td><td>UW</td><td>0.72</td><td>1,567</td><td>21.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.4</td><td>0.8</td><td>-14%</td><td>-45%</td><td>-50%</td><td>-99%</td></tr><tr><td>Shimao</td><td>0813.HK</td><td>UW</td><td>0.08</td><td>99</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-8%</td><td>-59%</td><td>-89%</td><td>-100%</td></tr><tr><td>Agile</td><td>3383.HK</td><td>NC</td><td>0.16</td><td>106</td><td>0.1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-17%</td><td>-39%</td><td>-57%</td><td>-99%</td></tr><tr><td>Logan</td><td>3380.HK</td><td>NC</td><td>1.44</td><td>1,044</td><td>3.1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-6%</td><td>-20%</td><td>78%</td><td>-91%</td></tr><tr><td>CIFI</td><td>884.HK</td><td>NC</td><td>0.05</td><td>104</td><td>0.7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-12%</td><td>-72%</td><td>-81%</td><td>-99%</td></tr><tr><td>R&amp;F</td><td>2777.HK</td><td>NC</td><td>0.24</td><td>114</td><td>0.3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-13%</td><td>-53%</td><td>-75%</td><td>-99%</td></tr><tr><td colspan="5">Distressed</td><td>10.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.2</td><td>0.3</td><td>-8%</td><td>-32%</td><td>-35%</td><td>-95%</td></tr><tr><td colspan="6">Mainland China Developers (Overall HK Listed)</td><td>9.1</td><td>7.6</td><td>3.1%</td><td>3.5%</td><td>0.4</td><td>0.4</td><td>-15%</td><td>1%</td><td>1%</td><td>-55%</td></tr><tr><td colspan="16"></td></tr><tr><td colspan="16">Mainland China Property Management</td></tr><tr><td>China Resources Mixc</td><td>1209.HK</td><td>OW</td><td>38.48</td><td>11,204</td><td>21.6</td><td>17.3</td><td>15.6</td><td>5.8%</td><td>6.4%</td><td>4.9</td><td>4.8</td><td>-10%</td><td>-8%</td><td>7%</td><td>-30%</td></tr><tr><td>China Overseas PH</td><td>2669.HK</td><td>UW</td><td>3.44</td><td>1,441</td><td>4.9</td><td>7.3</td><td>7.5</td><td>6.2%</td><td>6.2%</td><td>1.5</td><td>1.3</td><td>-13%</td><td>-24%</td><td>-33%</td><td>-69%</td></tr><tr><td>Poly Property Services</td><td>6049.HK</td><td>OW</td><td>27.22</td><td>1,921</td><td>4.0</td><td>8.0</td><td>7.6</td><td>6.2%</td><td>6.6%</td><td>1.1</td><td>1.1</td><td>-11%</td><td>-10%</td><td>-10%</td><td>-71%</td></tr><tr><td>Greentown Service</td><td>2869.HK</td><td>OW</td><td>4.18</td><td>1,670</td><td>2.2</td><td>10.7</td><td>10.0</td><td>6.7%</td><td>7.2%</td><td>1.3</td><td>1.3</td><td>-13%</td><td>-11%</td><td>-1%</td><td>-70%</td></tr><tr><td colspan="5">Backed by SOE developers</td><td>16.0</td><td>14.6</td><td>13.4</td><td>6.0%</td><td>6.5%</td><td>3.8</td><td>3.7</td><td>-11%</td><td>-10%</td><td>1%</td><td>-43%</td></tr><tr><td>Country Garden Services</td><td>6098.HK</td><td>N</td><td>5.25</td><td>2,182</td><td>5.5</td><td>6.0</td><td>5.9</td><td>10.1%</td><td>10.2%</td><td>0.4</td><td>0.4</td><td>-5%</td><td>-4%</td><td>-10%</td><td>-94%</td></tr><tr><td>A-Living</td><td>3319.HK</td><td>UW</td><td>1.84</td><td>333</td><td>0.8</td><td>3.0</td><td>3.4</td><td>3.6%</td><td>3.2%</td><td>0.2</td><td>0.2</td><td>-14%</td><td>-17%</td><td>-32%</td><td>-96%</td></tr><tr><td>Sunac Services</td><td>1516.HK</td><td>UW</td><td>0.78</td><td>301</td><td>1.4</td><td>4.4</td><td>5.2</td><td>6.8%</td><td>4.2%</td><td>0.4</td><td>0.4</td><td>-10%</td><td>-44%</td><td>-53%</td><td>-97%</td></tr><tr><td colspan="5">Backed by POE developers</td><td>4.5</td><td>5.4</td><td>5.5</td><td>9.0%</td><td>8.7%</td><td>0.4</td><td>0.4</td><td>-7%</td><td>-10%</td><td>-17%</td><td>-94%</td></tr><tr><td colspan="5">Property Management (Overall)</td><td>14.3</td><td>13.3</td><td>12.2</td><td>6.4%</td><td>6.8%</td><td>3.3</td><td>3.2</td><td>-10%</td><td>-10%</td><td>-2%</td><td>-50%</td></tr></table>

Source: Company data, Bloomberg Finance L.P. as of Jun 22, 2026, JPM estimates.  
Note: Companies marked with "NC" are not covered by JPM; all such estimates are based on Bloomberg consensus estimates.

Companies Discussed in This Report (all prices in this report as of market close on 22 June 2026, unless otherwise indicated)

China Jinmao (0817)(0817.HK/HK\$1.35/OW), China Overseas Land & Investment (0688)(0688.HK/HK\$13.13/OW), China Resources Land (1109)(1109.HK/HK\$31.18/OW), China Vanke - H(2202.HK/HK\$2.47/UW), SUNAC China(1918.HK/HK\$0.72/UW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are p

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
