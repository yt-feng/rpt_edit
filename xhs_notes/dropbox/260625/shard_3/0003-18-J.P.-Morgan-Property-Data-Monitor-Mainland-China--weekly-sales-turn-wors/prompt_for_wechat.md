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
# Property Data Monitor

Mainland China: weekly sales turn worse due to holidays; HK: home prices up another 0.6% W/W

## Mainland China

\- Iceberg 10-city real-time secondary weekly sales (冰山指数实时二手成交) dropped $0.05\%$ Y/Y (down from $+13\%$ Y/Y). Tier-1 cities' weekly sales dropped $3\%$ Y/Y (down from $+14\%$ ) (Table 1). The decline is mostly due to the Dragon Boat Festival. If we compare last week's data vs. the week with the same festival last year, 10-city & tier-1 sales would be up $15\% / 10\%$ Y/Y. Real-time sales generally lead the trend of official sales registrations by a few weeks.

\- Iceberg 10-city secondary listings (冰山指数二手挂牌量) fell further, down $0.2\%$ W/W. Tier-1 cities' listings dropped $0.5\%$ W/W, while Shanghai's dropped another $1.1\%$ W/W (prior: $-0.6\%$ ) (Table 2). The volume of secondary listings in tier-1 cities has been consistently coming down (down $2.6\%$ from the peak in March), and this is a key factor that will support continual secondary home price stabilization.

\- 60-city primary sales registrations (一手网签) fell $23\%$ Y/Y (more), mostly due to the inclusion of the 3-day Dragon Boat Festival (during public holidays, sales registrations are significantly lower than usual). Compared to the same 3-day Dragon Boat Festival period in 2025, sales registrations were up $60\%$ Y/Y (but the sample size is too small, hence we do not think this alone is representative).

\- 12-city secondary sales registrations (二手网签) fell $13\%$ Y/Y (Figure 7), reversing the positive Y/Y growth for the past 9 weeks (due to public holidays). Shanghai $(+12\%)$ is the only city with Y/Y growth among tier-1 cities. YTD, 12-city secondary sales have risen $5\%$ Y/Y (Shanghai: $+13\%$ ).

\- The Centraline tier-1 cities' secondary asking price index dropped mildly from 17.8 to 17.3 (Figure 3).

\- The Centaline manager confidence index dropped from 53 to 51 (Figure 4).

\- Southbound holdings rose 0.32% W/W (Table 7): Sunac +2.4%; CRL +0.9%

\- Share price moves (Figure 17): The sector dropped 13% last week, underperforming the HSI (-5%). The outperformer was Sunac (-5%). The underperformers were A-Living (-20%) and Longfor (-17%). For further discussion, please see our report China Property: Why the recent share price weakness?

• JPM top picks: COLI, CR Land, Jinmao and CR Mixc.

## Hong Kong SAR

\- The home price index rose 0.6% W/W (Figure 12). Home prices have risen 10.4% YTD, already reaching our full-year target of 10-15%. Looking ahead to 2H26, we expect slower price growth of <5%. For more discussion, please see our report HK Residential Property: Home prices already hit our full-year target; momentum may slow in 2H.

• Secondary transactions in the top 35 estates totaled 43 units, down 16%

## Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC
(852) 2800-8513
karl.chan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

(852) 2800-8599
venus.choi@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Jocelyn Gao
(852) 2800-8529
jocelyn.gao@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## APAC Credit Research

Alvin Au AC
(852) 2800-8533
alvin.au@JPM.com
JPM Securities (Asia Pacific) Limited

Soo Chong Lim
(852) 2800-7387
soochong.lim@JPM.com
JPM Securities (Asia Pacific) Limited

Shirley Yau
(852) 2800-0566
shirley.yau@JPM.com
JPM Securities (Asia Pacific) Limited

See page 20 for analyst certification and important disclosures, including non-US analyst disclosures.

W/W & down 47% Y/Y (Figure 11), the lowest since CNY. This is partially due to adverse weather.

\- The Centa Salesman Index (CSI) (Figure 14) moderated from 69.6 last week to 68.2. A reading of $>50 =$ sentiment is positive and property prices are likely to rise.

\- The Centaline Valuation Index (CVI) rose from 82.7 last week to 86.2 this week.

\- Southbound holdings fell 0.07% W/W (Table 7): Hang Lung Prop -0.6%; Swire Prop +0.04%.

\- Share price moves (Figure 18): The sector dropped $4.4\%$ last week, marginally outperforming the HSI $(-4.7\%)$ . The outperformer was HKL $(-1\%)$ , followed by Hysan and JM (both $-2\%$ ), while Champion REIT and NWD (both $-8\%$ ) underperformed.

JPM top picks: Developers – CKA, Sino; landlords – Swire Prop & HKL; conglomerates – JM & CKH.

## Credit View (by Alvin Au)

\- The JACI China HY Property index rose 0.3% (vs China HY: +0.16%) last week, resuming the uptrend after a brief correction the previous week. This brings YTD returns to +6.4%.

\- Seazen: Debtwire reported that Seazen is planning a Rmb2bn tap of private REIT as soon as in June. This is on top of a Rmb616mn private REIT issued in Nov 2025 backed by its Shanghai Qingpu Wuyue Plaza, and the developer will add two more shopping malls in Tianjin and Nantong as underlying assets for this tap. We think the scale of the tap is material, as it more than covers the Rmb1.7bn of onshore maturities for the rest of 2026. Management mentioned earlier that it is planning to launch a public REIT as an additional funding channel later in 2026 as well.

\- Continued K-shape for China's housing market as reflected in May 2026 NBS data: Top-tier cities remain solid as all four tier-1 cities report positive m/m increase in secondary home price (for the third month in a row). However, the broader industry remains weak with the 70-city m/m decline marginally widening from -0.23% in April to -0.26% in May (see details in equity report). As market fragmentation continues, we continue to prefer credits with IP transformation stories, solid debt servicing ability and decent valuations.

JPM top picks: LNGFOR '29s (84 offer, 9.9% ytm) and SHUION '29s (101.5 offer, 9.1% ytm).

## Table Of Contents

Mainland China.... 1
Hong Kong SAR.... 1
Credit View (by Alvin Au).... 2
1. Mainland China – real-time secondary sales & listings .... 4
2. Mainland China – leading indicators from Centraline.... 5
3. Mainland China – Weekly primary sales registrations .... 6
4. Mainland China – Weekly secondary sales registrations. .... 7
5. Hong Kong – Residential market update .... 8
6. Hong Kong – Tourist arrivals and resident departures .... 12
7. Share price update .... 13
8. Credit recommendations .... 17
9. Equity valuation summary .... 18

## 1. Mainland China – real-time secondary sales & listings

Table 1: Iceberg 10-city real time secondary weekly sales 冰山指数实时二手每周成交 (十大城市)

<table><tr><td rowspan="2">Week ending</td><td colspan="6">No. of units</td><td colspan="6">Y/Y</td><td colspan="6">4-week rolling Y/Y</td></tr><tr><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>Top-10</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>Top-10</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>Top-10</td></tr><tr><td>24-May-26</td><td>3,795</td><td>6,014</td><td>2,460</td><td>1,396</td><td>13,665</td><td>31,096</td><td>11%</td><td>14%</td><td>17%</td><td>15%</td><td>14%</td><td>13%</td><td>16%</td><td>16%</td><td>26%</td><td>24%</td><td>18%</td><td>17%</td></tr><tr><td>31-May-26</td><td>3,799</td><td>5,488</td><td>2,694</td><td>1,391</td><td>13,372</td><td>30,110</td><td>19%</td><td>11%</td><td>35%</td><td>29%</td><td>19%</td><td>22%</td><td>16%</td><td>18%</td><td>26%</td><td>25%</td><td>20%</td><td>19%</td></tr><tr><td>7-Jun-26</td><td>3,817</td><td>5,597</td><td>2,462</td><td>1,257</td><td>13,133</td><td>29,310</td><td>22%</td><td>16%</td><td>17%</td><td>36%</td><td>19%</td><td>16%</td><td>15%</td><td>13%</td><td>23%</td><td>25%</td><td>16%</td><td>16%</td></tr><tr><td>14-Jun-26</td><td>3,980</td><td>5,580</td><td>2,416</td><td>1,126</td><td>13,102</td><td>29,372</td><td>16%</td><td>18%</td><td>8%</td><td>0%</td><td>14%</td><td>13%</td><td>17%</td><td>15%</td><td>19%</td><td>19%</td><td>16%</td><td>16%</td></tr><tr><td>21-Jun-26</td><td>3,288</td><td>4,528</td><td>1,881</td><td>1,011</td><td>10,708</td><td>25,055</td><td>1%</td><td>-5%</td><td>-4%</td><td>-6%</td><td>-3%</td><td>0%</td><td>14%</td><td>20%</td><td>14%</td><td>14%</td><td>12%</td><td>13%</td></tr></table>

Source: Iceberg Index  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 1: Iceberg 10-city real time secondary daily sales 冰山指数实时二手每日成交 (十大城市)  
![](images/4cc37c7fdafb79b314a5c3deae11c02976f5733b8ee8601ac220aca5d11afcac.jpg)  
Source: Iceberg Index  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Table 2: Iceberg 10-city secondary listing volume 冰山指数二手挂牌量 (十大城市)

<table><tr><td rowspan="2">Week ending</td><td colspan="6">No. of secondary listings (&#x27;000 units)</td><td colspan="6">W/W</td></tr><tr><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier-1</td><td>Top-10</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier-1</td><td>Top-10</td></tr><tr><td>25-May-26</td><td>120</td><td>85</td><td>137</td><td>89</td><td>431</td><td>1,559</td><td>-0.6%</td><td>-0.5%</td><td>-0.2%</td><td>0.2%</td><td>-0.3%</td><td>0.0%</td></tr><tr><td>1-Jun-26</td><td>120</td><td>84</td><td>137</td><td>89</td><td>430</td><td>1,556</td><td>-0.2%</td><td>-0.6%</td><td>-0.1%</td><td>-0.1%</td><td>-0.2%</td><td>-0.2%</td></tr><tr><td>8-Jun-26</td><td>119</td><td>84</td><td>137</td><td>89</td><td>429</td><td>1,555</td><td>-0.2%</td><td>-0.4%</td><td>-0.2%</td><td>0.1%</td><td>-0.2%</td><td>-0.1%</td></tr><tr><td>15-Jun-26</td><td>120</td><td>84</td><td>137</td><td>89</td><td>429</td><td>1,559</td><td>0.3%</td><td>-0.6%</td><td>0.0%</td><td>0.3%</td><td>0.0%</td><td>0.2%</td></tr><tr><td>22-Jun-26</td><td>119</td><td>83</td><td>137</td><td>88</td><td>427</td><td>1,556</td><td>-0.4%</td><td>-1.1%</td><td>-0.1%</td><td>-0.8%</td><td>-0.5%</td><td>-0.2%</td></tr></table>

Source: Iceberg Index

Figure 2: Iceberg tier-1 cities secondary listing volume 冰山指数二手挂牌量 (一线城市)  
![](images/8fc9e902063edb0d36195c2f744d5ab28e6566e14a5d86f94abb7cb3677ccf9c.jpg)  
Source: Iceberg Index

## 2. Mainland China – leading indicators from Centraline

Figure 3: Centraline secondary asking price index vs. NBS secondary home price index M/M in tier-1 cities

![](images/ea98acb5442960e7a8ade382ed3867ccb4e339ea8ea3b9b79d20089b41603454.jpg)  
Source: Centraline, Wind, NBS.  
Note: The asking price index represents the percentage of projects with home price increases. For example, an index of 20 means that 20% of projects raise prices (while 80% do not).  
Figure 4: Centraline secondary manager confidence index in tier-1 cities vs. three-month rolling secondary sales

![](images/e5e3b7e8e40ee9da8834478dc6e83053cca0aed7c70dfdf5fc569c19b26d31c2.jpg)  
Source: Centraline, Wind. Note: The index surveys managers across the country for their judgment on the market outlook.

# 3. Mainland China – Weekly primary sales registrations

Figure 5: 60-city weekly primary sales registrations (一手网签) – compared with 2019-24  
![](images/95d0ab1478fb3f8db01a19b1326c6f4957650dbfdebc49777325cecf2626880d.jpg)  
Source: CREIS.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 6: 60-city weekly primary sales registrations (一手网签)  
![](images/495684aef95b1ce19fbcdace00e3704b53cece7fbf20849e5ea0b86eebb35efc.jpg)  
Source: CREIS.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Table 3: 60-city weekly primary sales registrations (一手网签) by tier

<table><tr><td rowspan="2">Week ending</td><td colspan="6">60-City</td><td colspan="6">Tier-1</td><td colspan="6">Tier-2</td><td colspan="6">Tier-3/4</td></tr><tr><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td></td><td></td><td></td><td></td></tr><tr><td>19-Apr-26</td><td>21,159</td><td>6%↑</td><td>15%↑</td><td>-1%↑</td><td>-69%↑</td><td>3,726</td><td>5%↑</td><td>13%↑</td><td>9%↑</td><td>-35%↓</td><td>12,813</td><td>18%↑</td><td>15%↑</td><td>3%↑</td><td>-70%↑</td><td>4,620</td><td>-16%↑</td><td>16%↑</td><td>-18%↑</td><td>-77%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>26-Apr-26</td><td>23,318</td><td>-7%↓</td><td>10%↓</td><td>1%↑</td><td>-60%↑</td><td>4,297</td><td>6%↑</td><td>15%↑</td><td>11%↑</td><td>-23%↑</td><td>13,879</td><td>-6%↓</td><td>8%↓</td><td>4%↑</td><td>-60%↑</td><td>5,142</td><td>-16%↓</td><td>11%↓</td><td>-10%↑</td><td>-73%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>3-May-26</td><td>21,384</td><td>-4%↑</td><td>-8%↓</td><td>-4%↓</td><td>-65%↓</td><td>4,223</td><td>12%↑</td><td>-2%↓</td><td>6%↓</td><td>-14%↑</td><td>12,503</td><td>3%↑</td><td>-10%↓</td><td>2%↓</td><td>-66%↓</td><td>4,658</td><td>-25%↓</td><td>-9%↓</td><td>-22%↓</td><td>-75%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>10-May-26</td><td>20,449</td><td>-2%↑</td><td>-4%↑</td><td>-2%↑</td><td>-67%↓</td><td>3,523</td><td>2%↓</td><td>-17%↓</td><td>6%↓</td><td>-29%↓</td><td>12,116</td><td>3%↑</td><td>-3%↑</td><td>3%↑</td><td>-68%↓</td><td>4,810</td><td>-15%↑</td><td>3%↑</td><td>-18%↑</td><td>-76%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>17-May-26</td><td>24,282</td><td>3%↑</td><td>19%↑</td><td>-2%↓</td><td>-62%↑</td><td>4,874</td><td>22%↑</td><td>38%↑</td><td>11%↑</td><td>-17%↑</td><td>13,822</td><td>4%↑</td><td>14%↑</td><td>1%↓</td><td>-64%↑</td><td>5,586</td><td>-10%↑</td><td>16%↑</td><td>-17%↑</td><td>-72%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>24-May-26</td><td>24,411</td><td>-10%↓</td><td>1%↓</td><td>-3%↓</td><td>-65%↓</td><td>5,032</td><td>11%↓</td><td>3%↓</td><td>12%↑</td><td>-18%↓</td><td>13,964</td><td>-11%↓</td><td>1%↓</td><td>-1%↓</td><td>-68%↓</td><td>5,415</td><td>-22%↓</td><td>-3%↓</td><td>-18%↓</td><td>-73%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>31-May-26</td><td>31,094</td><td>14%↑</td><td>27%↑</td><td>1%↑</td><td>-53%↑</td><td>5,784</td><td>28%↑</td><td>15%↑</td><td>16%↑</td><td>9%↑</td><td>17,992</td><td>15%↑</td><td>29%↑</td><td>3%↑</td><td>-55%↑</td><td>7,318</td><td>2%↑</td><td>35%↑</td><td>-11%↑</td><td>-65%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>7-Jun-26</td><td>21,851</td><td>17%↑</td><td>-30%↓</td><td>5%↑</td><td>-66%↓</td><td>3,572</td><td>1%↓</td><td>-38%↓</td><td>16%↓</td><td>-29%↓</td><td>13,011</td><td>31%↑</td><td>-28%↓</td><td>8%↑</td><td>-67%↓</td><td>5,268</td><td>0%↓</td><td>-28%↓</td><td>-8%↑</td><td>-74%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>14-Jun-26</td><td>19,881</td><td>-7%↓</td><td>-9%↑</td><td>3%↓</td><td>-69%↓</td><td>3,188</td><td>-2%↓</td><td>-11%↑</td><td>11%↓</td><td>-40%↓</td><td>12,051</td><td>-2%↓</td><td>-7%↑</td><td>6%↓</td><td>-69%↓</td><td>4,642</td><td>-19%↓</td><td>-12%↑</td><td>-10%↓</td><td>-76%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>21-Jun-26</td><td>20,899</td><td>-23%↓</td><td>5%↑</td><td>-1%↓</td><td>-73%↓</td><td>3,447</td><td>-11%↓</td><td>8%↑</td><td>5%↓</td><td>-56%↓</td><td>13,511</td><td>-15%↓</td><td>12%↑</td><td>5%↓</td><td>-71%↓</td><td>3,941</td><td>-46%↓</td><td>-15%↓</td><td>-17%↓</td><td>-83%↓</td><td></td><td></td><td></td><td></td></tr></table>

Source: CREIS.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

## 4. Mainland China – Weekly secondary sales registrations

Figure 7: 12-city daily secondary sales registrations (二手网签)  
![](images/90533d0fea4223e7cc20bfda78727e14303567cf638afc71fcfb1e0d8222103f.jpg)  
Source: Wind.  
Note: The decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 8: 12-city secondary sales registrations (二手网签) 7-day moving average  
Secondary sales 7-day moving average - 12-city  
![](images/c59f6193b7be64a24c850b878391878d758dfe8bcd180bd0247c5b682bb3a8f6.jpg)  
Source: Wind.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

## 5. Hong Kong – Residential market update

Table 4: Hong Kong primary residential projects – Latest sell-through rates and upcoming launches

<table><tr><td colspan="2">Project</td><td>Location</td><td>Developer</td><td>Launch Date</td><td>ASP (HK$ psf)</td><td>Total no. of units</td><td>Units launched</td><td>Units sold</td><td>Sell- through</td><td>vs. previous phase</td><td>vs. secondary prices</td></tr><tr><td colspan="12">Major primary new launches since May 2026</td></tr><tr><td rowspan="4">Lime SPARK</td><td rowspan="4">形瑁</td><td rowspan="4">Tsuen Wan</td><td rowspan="4">SHKP</td><td>9-May-26</td><td>16 - 18K</td><td>462</td><td>154</td><td>154</td><td>100%</td><td>-</td><td>14%</td></tr><tr><td>16-May-26</td><td>17 - 19K</td><td></td><td>121</td><td>121</td><td>100%</td><td>4%</td><td>19%</td></tr><tr><td>23-May-26</td><td>18 - 20K</td><td></td><td>87</td><td>87</td><td>100%</td><td>3%</td><td>22%</td></tr><tr><td>30-May-26</td><td>18 - 20K</td><td></td><td>52</td><td>52</td><td>100%</td><td>3%</td><td>26%</td></tr><tr><td rowspan="5">Highwood Ph2</td><td rowspan="5">壹沐2期</td><td rowspan="5">To Kwa Wan</td><td rowspan="5">Henderson</td><td>9-May-26</td><td>19 - 24K</td><td>415</td><td>150</td><td>150</td><td>100%</td><td>14%</td><td>14%</td></tr><tr><td>13-May-26</td><td>19 - 24K</td><td></td><td>50</td><td>50</td><td>100%</td><td>4%</td><td>22%</td></tr><tr><td>17-May-26</td><td>20 - 26K</td><td></td><td>50</td><td>42</td><td>84%</td><td>2%</td><td>25%</td></tr><tr><td>23-May-26</td><td>20 - 27K</td><td></td><td>35</td><td>29</td><td>83%</td><td>1%</td><td>26%</td></tr><tr><td>31-May-26</td><td>22 - 27K</td><td></td><td>23</td><td>5</td><td>22%</td><td>13%</td><td>35%</td></tr><tr><td rowspan="2">PORTO</td><td rowspan="2"></td><td rowspan="2">Ap Lei Chau</td><td rowspan="2">Wang On</td><td>9-May-26</td><td>20 - 25K</td><td>174</td><td>86</td><td>55</td><td>64%</td><td>-</td><td>31%</td></tr><tr><td>24-May-26</td><td>24 - 31K</td><td></td><td>6</td><td>1</td><td>17%</td><td>5%</td><td>61%</td></tr><tr><td rowspan="3">One Victoria Cove Ph3</td><td rowspan="3">首岸3期</td><td rowspan="3">Hung Hom</td><td rowspan="3">Henderson/Hysan/ Empire/URA</td><td>10-May-26</td><td>21 - 23K</td><td>288</td><td>130</td><td>130</td><td>100%</td><td>16%</td><td>20%</td></tr><tr><td>14-May-26</td><td>20 - 24K</td><td></td><td>70</td><td>61</td><td>87%</td><td>4%</td><td>25%</td></tr><tr><td>19-May-26</td><td>22 - 24K</td><td></td><td>58</td><td>49</td><td>84%</td><td>2%</td><td>28%</td></t

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and

should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
