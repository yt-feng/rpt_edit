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
Global Energy Storage

# Global Energy Storage: Have lithium prices peaked?

![](images/1825fdc29836d003bb5d9b407b8d19bc1a59e2abae5c41b4233a58bb595b744e.jpg)

Brian Ho, CFA

+852 2123 2615

brian.ho@bernsteinsg.com

![](images/d5bc6a2c7181a9dc8bc6503e2a13baf6226d2cc31771317097a2e0f711a025e9.jpg)

Neil Beveridge, Ph.D.

+852 2123 2648

neil.beveridge@bernsteinsg.com

![](images/3a5f6e6b2981a7e401c82786de22a5a6eff88d302c0ccdf12c2ca374bc69988c.jpg)

Kelvin Yuan, Ph.D., CFA

+852 2123 2612

kelvin.yuan@bernsteinsg.com

Lithium carbonate prices have tripled from 2025 lows, reaching \~\$30k/t in May before easing to \$20–25k/t on supply restarts, which we view as a short-term buffer. We continue to view the market as being in a mid-cycle recovery rather than approaching a peak. Inventories are tight at \~20 days, capex has yet to recover, and supply growth is starting to moderate. On the demand side, robust battery demand led by ESS continues to absorb higher prices. Taken together, we see further upside risks, with prices likely peaking closer to 2027.

Lithium demand has grown \~32% year to date, outpacing supply growth of \~24% and driving a meaningful market tightening. The key driver has been ESS, with demand up \~100% YTD, offsetting more moderate EV growth of \~9%. On the lithium supply side, growth has been led by China (+30%), Chile (+25%), and Argentina (+106%), while Australia (+6%) and Zimbabwe (+16%) have lagged, contributing to a tighter-than-expected balance.

We estimate \~200kt LCE of curtailed supply is gradually returning to the market although this only provides a short term buffer. While this may help partially close the supply gap in 2026, it is unlikely to keep pace with demand growth as capacity additions slow beyond 2026, leaving the market increasingly tight into 2027.

Inventories have tightened significantly, with lithium inventory days falling to \~20 days year to date. Historically, lithium prices tend to rise more sharply once inventory falls below \~20 days, with spikes often occurring closer to \~15 days or lower. Current levels suggest the market has moved from balanced toward tightening, with inventory now firmly within a range that has historically supported stronger pricing momentum.

Current higher lithium prices have not led to any meaningful demand slowdown. We expect ESS markets can absorb lithium carbonate prices in the \~\$30k/t range based on underlying project economics. Importantly, sustained higher prices are required to incentivize new supply, particularly given long development timelines and the lag in capex following the recent downturn across the sector.

We have revised up our lithium price assumptions to reflect tighter lithium market. We now estimate lithium carbonate prices of \~\$25k/t in 2026 (from \$21k/t previously) and \~\$32.5k/t in 2027 (from \$25k/t), while maintaining our long-term price assumption of \$16k/t. This reflects both tighter near-term market conditions and required to sustain long-term supply growth.

attractive. We update our earnings estimates and valuation to reflect higher lithium price assumptions in 2026 and 2027. Following the higher price assumption, we revise up our DCF-based valuation for Tianqi Lithium to RMB80/sh (from RMB73) for Tianqi (A-share) and HKD65/sh (from HKD61) for Tianqi (H-share), using a 9% WACC and terminal growth rate of 2% (both unchanged). This assumes a long term lithium carbonate price of \$16k/t. The stock currently trades at \~17x 1-year forward P/E, well below its historical average of \~50x, suggesting scope for further re-rating as the cycle strengthens.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">22 Jun 2026</td><td colspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td></td><td>ClosingPrice</td><td>PriceTarget</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td><td></td></tr><tr><td>300750.CH (CATL)</td><td>O</td><td>CNY</td><td>408.98</td><td>800.00</td><td>25.0%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>25.3</td><td>18.6</td><td>14.2</td><td></td></tr><tr><td>3750.HK (CATL)</td><td>M</td><td>HKD</td><td>741.50</td><td>770.00</td><td>102.4%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>39.7</td><td>29.2</td><td>22.3</td><td></td></tr><tr><td>247540.KS (EcoPro BM)</td><td>U</td><td>KRW</td><td>169,400</td><td>140,000</td><td>15.7%</td><td>KRW</td><td>403.00</td><td>854.00</td><td>1,963.00</td><td>420.3</td><td>198.4</td><td>86.3</td><td></td></tr><tr><td>051910.KS (LG Chem)</td><td>M</td><td>KRW</td><td>336,500</td><td>298,000</td><td>6.4%</td><td colspan="2">KRW(13,258.70)</td><td>2,042.47</td><td>31,118</td><td>(25.4)</td><td>164.8</td><td>10.8</td><td></td></tr><tr><td>373220.KS (LGES)</td><td>M</td><td>KRW</td><td>404,500</td><td>347,000</td><td>(19.7)%</td><td colspan="2">KRW (5,308.10)</td><td>1,811.04</td><td>9,452.97</td><td>(76.2)</td><td>223.4</td><td>42.8</td><td></td></tr><tr><td>003670.KS (Posco Future M)</td><td>U</td><td>KRW</td><td>199,600</td><td>190,000</td><td>1.5%</td><td colspan="2">KRW (2,740.96)</td><td>376.72</td><td>898.20</td><td>(72.8)</td><td>529.8</td><td>222.2</td><td></td></tr><tr><td>006400.KS (SDI)</td><td>M</td><td>KRW</td><td>564,000</td><td>520,000</td><td>157.6%</td><td colspan="2">KRW (9,933.80)</td><td>2,099.51</td><td>18,376</td><td>(56.8)</td><td>268.6</td><td>30.7</td><td></td></tr><tr><td>002466.CH (Tianqi Lithium)</td><td>O</td><td>CNY</td><td>64.97</td><td>80.00</td><td>74.5%</td><td>CNY</td><td>0.28</td><td>3.90</td><td>7.75</td><td>230.2</td><td>16.6</td><td>8.4</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>73.00</td><td></td><td></td><td></td><td>3.29</td><td>6.18</td><td></td><td></td><td></td><td></td></tr><tr><td>9696.HK (Tianqi Lithium)</td><td>O</td><td>HKD</td><td>44.64</td><td>65.00</td><td>29.1%</td><td>CNY</td><td>0.28</td><td>3.90</td><td>7.75</td><td>136.6</td><td>9.9</td><td>5.0</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>61.00</td><td></td><td></td><td></td><td>3.29</td><td>6.18</td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,048.07</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

003670.KS base year is 2024;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Lithium carbonate prices have more than doubled to above \~\$20k/t from 2025 lows, yet we view the market as mid-cycle with further upside as supply response continues to lag tightening fundamentals. Lithium demand has grown \~32% YTD, led by ESS (+100%), outpacing supply growth of \~24% and driving a meaningful market tightening. Inventory days have fallen to \~20 days, a level historically associated with stronger price momentum. While \~200kt of curtailed supply may return in 2026, this is only a temporary buffer, with 2027 expected to tighten further. Demand remains resilient, with ESS and EV markets able to absorb prices in the \~\$30k/t range. We raise our price forecasts to \$25k/t in 2026 and \$32.5k/t in 2027, with Tianqi offering attractive upside.

## VALUATION COMPS TABLE

EXHIBIT 1: Lithium companies valuation comparison table

<table><tr><td>Company</td><td>Ticker</td><td>Market cap (USD bn)</td><td>12 month return</td><td>2025 P/E</td><td>2025 P/S</td><td>2025 EV/EBITDA</td><td>2024 Revenue (USD bn)</td><td>Lithium % of Rev.</td><td>24-25 Rev Growth</td><td>2024 OPM</td></tr><tr><td>Tianqi Lithium</td><td>9696 HK Equity</td><td>14.9</td><td>77%</td><td>153.5</td><td>10.3</td><td>23.2</td><td>1.8</td><td>100%</td><td>-9%</td><td>39%</td></tr><tr><td>Ganfeng Lithium</td><td>1772 HK Equity</td><td>20.0</td><td>183%</td><td>199.5</td><td>8.1</td><td>59.0</td><td>2.6</td><td>74%</td><td>18%</td><td>0%</td></tr><tr><td>Yahua Industrial Group</td><td>002497 CH Equity</td><td>3.8</td><td>106%</td><td>44.7</td><td>2.9</td><td>22.7</td><td>1.1</td><td>79%</td><td>16%</td><td>5%</td></tr><tr><td>Yongxing Special Materials</td><td>002756 CH Equity</td><td>4.9</td><td>105%</td><td>40.3</td><td>4.3</td><td>33.2</td><td>1.1</td><td>55%</td><td>0%</td><td>16%</td></tr><tr><td>Jiangxi Special Electric Motor</td><td>002176 CH Equity</td><td>2.8</td><td>61%</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>0.3</td><td>81%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Chengxin Lithium Group Co Ltd</td><td>002240 CH Equity</td><td>6.2</td><td>283%</td><td>-75.2</td><td>11.2</td><td>n.a</td><td>0.6</td><td>99%</td><td>2%</td><td>-11%</td></tr><tr><td>Zangge Mining Co Ltd</td><td>000408 CH Equity</td><td>17.7</td><td>94%</td><td>34.1</td><td>35.7</td><td>n.a</td><td>0.5</td><td>38%</td><td>0%</td><td>88%</td></tr><tr><td>Qinghai Salt Lake Industry Co</td><td>000792 CH Equity</td><td>23.3</td><td>89%</td><td>21.8</td><td>8.2</td><td>16.5</td><td>2.1</td><td>30%</td><td>0%</td><td>39%</td></tr><tr><td>Rongjie Co.</td><td>002192 CH Equity</td><td>3.3</td><td>213%</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>0.1</td><td>84%</td><td>0%</td><td>n.a.</td></tr><tr><td>Jinzhou Yongshan Lithium Co Lt</td><td>603399 CH Equity</td><td>1.5</td><td>150%</td><td>n.a</td><td>n.a</td><td>n.a</td><td>0.8</td><td>35%</td><td>n.a</td><td>n.a</td></tr><tr><td>Average (China)</td><td></td><td></td><td>143%</td><td>44.2</td><td>11.7</td><td>32.9</td><td></td><td></td><td></td><td>23%</td></tr><tr><td>Albemarle</td><td>ALB US Equity</td><td>18.9</td><td>183%</td><td>-195.7</td><td>4.4</td><td>21.0</td><td>5.4</td><td>74%</td><td>-6%</td><td>-11%</td></tr><tr><td>SQM</td><td>SQM US Equity</td><td>21.9</td><td>148%</td><td>34.1</td><td>5.7</td><td>16.8</td><td>4.5</td><td>69%</td><td>0%</td><td>27%</td></tr><tr><td>Sigma Lithium Corp</td><td>SGML US Equity</td><td>1.5</td><td>187%</td><td>-80.4</td><td>13.1</td><td>-129.6</td><td>0.2</td><td>100%</td><td>-24%</td><td>0%</td></tr><tr><td>Average (Americas)</td><td></td><td></td><td>173%</td><td>-80.7</td><td>7.7</td><td>-30.6</td><td></td><td></td><td></td><td>5%</td></tr><tr><td>Mineral Resources Ltd</td><td>MIN AU Equity</td><td>9.8</td><td>222%</td><td>-60.4</td><td>3.4</td><td>18.1</td><td>3.5</td><td>40%</td><td>-16%</td><td>9%</td></tr><tr><td>PLS Group Ltd</td><td>PLS AU Equity</td><td>14.0</td><td>350%</td><td>-280.5</td><td>27.9</td><td>257.4</td><td>0.8</td><td>100%</td><td>-40%</td><td>36%</td></tr><tr><td>IGO Ltd</td><td>IGO AU Equity</td><td>4.6</td><td>104%</td><td>-51.0</td><td>13.1</td><td>383.1</td><td>0.6</td><td>81%</td><td>-40%</td><td>19%</td></tr><tr><td>Liontown Ltd</td><td>LTR AU Equity</td><td>4.6</td><td>190%</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>0.0</td><td>100%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Average (Australia)</td><td></td><td></td><td>216%</td><td>-130.6</td><td>14.8</td><td>219.5</td><td></td><td></td><td></td><td>22%</td></tr></table>

Tianqi Lithium is covered by Bernstein. All other companies are not covered by Bernstein. Market data as of June 18, 2026
Source: Bloomberg (consensus estimates), Bernstein analysis

## DETAILS

## SUMMARY

We expect the lithium market to remain a highly cyclical industry with supply responding elastically to price changes. Since our last lithium supply and demand update from last December (Global Energy Storage: 2026 Lithium Outlook. How high can prices go?), lithium carbonate prices have more than doubled and market sentiment has turned far more constructive. We still view the industry as mid-cycle rather than late-cycle. The key change has been stronger-than-expected battery demand, led by energy storage, which has tightened the market much faster than we previously expected. While lithium equities have already rebounded sharply, historical cycles suggest the move in the underlying commodity can still have room to run once inventories tighten and supply response lags. Lithium stocks often recover 6 to 12 months ahead of spot prices. In our view, the current rebound is consistent with the middle part of the cycle rather than the end, with the setup still supportive through 2027.

EXHIBIT 2: Historical cycles suggest that entering lithium stocks at the bottom can be attractive over a 2-year horizon

3-yr average sector performance from lithium price trough  
![](images/7d7e534ead098a9d8dc7853199c3e09702ec70260a69cb11790b81e4c4fea056.jpg)  
Companies include Albermarle, SQM, Tianqi Lithium, Ganfeng Lithium, Pilbara Minerals, Livent, and Allkem Source: Bloomberg, Bernstein analysis

Lithium carbonate prices fell from a peak of \$80k/t in November 2022 to a trough of around \$8k/t in mid-2025, but have since recovered to around \$20-25k/t. Unlike six months ago, prices are now well above marginal cash costs and high enough to encourage some curtailed supply to restart. Even so, the industry is still coming off two years of weak returns and capex cuts, meaning supply response should remain slower than the increase in demand over the next 12 to 18 months.

Lithium Carbonate Prices vs Marginal Costs

China's lithium inventory days vs price  
EXHIBIT 3: Lithium prices have rebounded to around \$20-25k/t from the 2025 trough, but we still see further upside as the market tightens  
![](images/e1222baae1cc38d4ee4786ead51900cbf6257cbaca258c132e21f37e7bae9cd4.jpg)  
Source: Company data, Bloomberg, Bernstein estimates and analysis

Year to date, lithium demand has increased by around 32% while supply has grown by around 24%, implying demand has outpaced supply and the market has tightened materially. The key driver has been energy storage, with ESS demand up around 100% year to date compared with EV demand growth of around 9%. As a result, lithium inventory days have fallen to below 20 days, the lowest level since 2022, which has been a key driver of the sharp rise in lithium prices this year. Lithium prices remain highly correlated to inventory days. While the relationship is not perfect, prices have historically moved sharply higher when inventory falls below 20 days. With inventory now back in that range, the market appears to have shifted from a balanced market to a tightening market, which is more supportive for pricing than at the start of the year.

EXHIBIT 4: Inventory days have fallen below 20 days, a level that has historically been supportive of stronger lithium prices  
![](images/036142bc9d1ff4af89d3739c48601c1ebba6b4ab9cf1e4050675ee3026ac5462.jpg)  
Source: SMM, SNE, Bernstein estimates and analysis

The improvement in prices should lead to better profitability for lithium producers, but the industry is still recovering from a prolonged downturn. Returns on capital have been compressed for the last two years and balance sheets remain a focus for management teams. This matters because even with a stronger price signal today, the supply side is unlikely to respond immediately given prior capex cuts and the time needed to restart or expand operations.

EXHIBIT 5: Average return on capital for the industry have remained close to zero for the last two years and have only started recovering  
Profitability and Returns  
![](images/1e5dc6f82d2cb7ac00a0a0539932657bb17b1e0cc877e6ba7e18ff0d49a6c385.jpg)  
Source: Bloomberg, Bernstein analysis

Historical correlation indicates the industry generally needs lithium prices in the range of \$15-20k/t to earn around a 10% return on capital. Current prices are now above that range, which should support the restart of curtailed production and improve producer economics. However, a stronger and more durable price signal is still needed to drive a broader newbuild cycle, especially for projects with longer lead times or higher capital intensity.

EXHIBIT 6: Based on historical correlation, the industry needs a lithium price of \$15-20k/t to achieve a 10% return on capital

Industry ROACE vs lithium carbonate price  
![](images/60dadfd1c2bf8b78a69d8f2f967f889f3e4f7c168f946c297eb1e64a8f53a14e.jpg)  
Source: Bloomberg, Bernstein analysis

Capex peaked at the end of 2023 and fell materially through 2024 and 2025 as producers focused on preserving balance sheets. Even though spot prices have recovered, the investment response should lag because managers are unlikely to reverse course immediately after a deep downturn. In our view, that lagged capex response is one of the main reasons the market can remain tight through 2026 and into 2027.

Existing projects under C&M or running at reduced rates

EXHIBIT 7: Capex is expected to have fallen by 50% in 2025 which would take lithium investments to a 3-year low. Higher price signal is required to drive new supply growth

Capex and Reinvestment  
![](images/cd68a8581c9584d530e424dd47f0fac7f178191ac17e2c78d74ec4907c264f31.jpg)  
Source: Bloomberg, Bernstein analysis

Low prices in the last two years led to the curtailment of a meaningful amount of higher-cost supply. We now estimate around 200kt LCE of previously curtailed production could return as prices recover. This should help fill part of the supply gap in 2026, but if demand remains strong it is unlikely to be enough to prevent further tightening in 2027.

EXHIBIT 8: Higher prices are bringing back curtailed supply, but around 200kt LCE of restarts is still not enough to solve 2027 tightness

<table><tr><td>Project</td><td>Status</td><td>Underutilized capacity (kt LCE)</td><td>Cash costs ($/t LCE)</td></tr><tr><td>Finniss (Australia)</td><td>Restarted in May-26</td><td>14</td><td>12,000</td></tr><tr><td>Bald Hill (Australia)</td><td>Restarted in May-26</td><td>19</td><td>9,168</td></tr><tr><td>Ngungaju (Australia)</td><td>Restart in July-26</td><td>24</td><td>8,712</td></tr><tr><td>Mt Cattlin (Australia)</td><td>Care and maintenance</td><td>29</td><td>11,272</td></tr><tr><td>Jianxiawo (China)</td><td>Care and maintenance</td><td>45</td><td>15,000</td></tr><tr><td>Sabi Star, Kamativi, Bikita (Zimbabwe)</td><td>Reduced operating rates</td><td>29</td><td>8,291</td></tr><tr><td>Other lepidolite mines (China)</td><td>Reduced operating rates</td><td>30</td><td>15,000</td></tr><tr><td>Total</td><td></td><td>191</td><td></td></tr></table>

## Source: Company data, Bernstein analysis

Taking a closer look at supply start-ups over the coming quarters, there are still projects ramping up in 2026 as a result of FIDs taken during 2021 to 2023. However, beyond mid-2026 the pace of new capacity additions is still expected to slow materially. That means the near-term supply response should come more from restarts th

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
