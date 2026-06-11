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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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
# China Restaurants: Monthly Tracker: May update: Trends turn softer but divergence across brands; FMD high base effect kicking in

May SSSG performance was sequentially softer from Apr, with moderate demand during the Labor Day holiday and softness in consumption sentiment/weather headwinds. By brand, Haidilao's table turn turned to slightly negative growth yoy (vs. yoy stable growth during Labor Day), implying low-mid 80% recovery compared to the 2019 level (slightly higher than Apr yet remains below the 1Q level); Tai Er recorded SSSG of low DD%, slightly lower than Apr with weather headwinds during Labor Day (SSSG up MSD%-HSD%), but post holiday SSSG has picked up. For freshly made drinks (FMD), high base impact has started to kick in, and brands have generally seen SSSG pressure in May on a yoy basis. We continue to see performance divergence across brands, e.g. Nayuki per store sales decline further expanded to 24% yoy (vs. -11% in Apr), while leading brands were more resilient with support from category expansion/new products. On the bright side, multiple brands commented that delivery mix declined sequentially and/or on a yoy basis. On pricing, our tracker suggests more pricing activities were introduced in coffee from freshly made tea brands (e.g. Guming launched weekly Rmb9.9 coupon, Mixue launched a buy-one-get-one free coupon for stores that introduced coffee machines), to educate customers and drive dine-in sales; Luckin also launched a daily Rmb9.9 offering for select SKUs across categories. All said, promotion magnitude/scale remains disciplined in our view. For restaurant brands we track, Jiumaojiu and Haidilao both saw stable pricing trends.

In this note, we provide updates on a variety of high-frequency indicators, including air traffic run rate, and commodity inflation. We also include competition environment updates, key company news and key reports published over the past month for covered China Restaurants names and peers.

## Brand performance

1. Haidilao (6862.HK; Neutral): Haidilao's average table turn turned to slightly negative in May, vs. a MSD% increase in Apr from a low base. Management believes the calendar shift of the Dragon Boat festival (1 day in May in 2025) was a headwind for May performance. Based on our calculation, this implies a \~3.8x table turn, or 3.5x\~3.6x post Labor Day holiday which is a similar table turn level compared to Apr. This implies a low-mid 80% recovery level compared to 2019, slightly better than \~80% for Apr but remains lower than 1Q. Haidilao opened 4 company stores and 1 franchise store, and closed 4 company stores in May.

## Michelle Cheng

+852-2978-6631

michelle.cheng@gs.com

GS (Asia) L.L.C.

## Xinyu Ruan

+852-2978-7347 | xinyu.ruan@gs.com

GS (Asia) L.L.C.

## Molly Dai

+852-3966-4000 | molly.dai@gs.com

GS (Asia) L.L.C.

## Carol Chen

+852-2978-7999 | carol.chen@gs.com

GS (Asia) L.L.C.

## Keira Liu

+852-2978-0473 | keira.liu@gs.com

GS (Asia) L.L.C.

GS read: Table turn performance remained relatively soft, and post-holiday growth slightly decelerated (vs. stable table turn in Labor Day), but we believe market expectation has also come down considering softness in overall consumption/weather headwinds. YTD average table turn increase of LSD% is slightly tracking behind GSe which assumes 4% per store sales growth yoy.

2. Jiumaojiu (9922.HK, Buy): Tai Er recorded LDD% SSSG in ML China, which slightly declined from Apr yet remained above the 1Q level (10.9% SSSG in ML China). This implies a post holiday acceleration compared to MSD%-HSD% SSSG during the Labor Day holiday when rainy weather in South China was a headwind. New model stores continued to drive growth, while old models continued to see positive SSSG, also recording LSD%-MSD% SSSG in May. For Jiumaojiu and Song, pressure lingered and SSSG trends remained similar to 1Q (-20%/-11% for Song/Jiumaojiu respectively).

GS read: Tai Er continues to see solid SSSG performance despite the fluid consumption in May, and the post-holiday improvement shows momentum of its new model/fresh product strategy. That said, Song/Jiumaojiu brands are still seeing pressure despite their base being sequentially easier compared to 1Q. Compared to GSe, Tai Er/Jiumaojiu are largely on track, while Song is tracking behind our 1H26 expectation.

3. Gourmet Master (2723.TW; Neutral): ML China sales decline remained significant at -46% yoy (Apr: -48%), with store count sequentially stable at 290-300 which implies a >30% yoy decline and transition to franchised stores. In the US market, sales growth has been sequentially accelerating in Apr-May (sales in local currency up 4%/8% yoy) post the weather headwinds in 1Q26, and the company expects store count to reach 95 (3 expected to be opened in Jun)/>100 by mid/end of 2026.

GS read: The sales decline in Apr-May at high 40%s in ML China iss tracking behind GSe (\~-40% yoy decline). While in the US market, Apr-May sales growth is slightly ahead of GSe (MSD% growth in local currency), and store openings have been on track with GSe.

Exhibit 1: Haidilao/Tai Er May SSSG decelerated; FMD players generally seeing SSSG pressure due to a tough base

<table><tr><td></td><td>Jan 25</td><td>Feb 25</td><td>Mar 25</td><td>Apr 25</td><td>May 25</td><td>Jun 25</td><td>Jul 25</td><td>Aug 25</td><td>Sep 25</td><td>25-Oct</td><td>25-Nov</td><td>25-Dec</td><td>26-Jan</td><td>26-Feb</td><td>26-Mar</td><td>26-Apr</td><td>26-May</td><td>Apr-May</td><td>CNY 2023</td><td>Labor Day 2023</td><td>National Day 2023</td><td>CNY 2024</td><td>Labor Day 2024</td><td>National Day 2024</td><td>CNY 2025</td><td>Labor Day 2025</td><td>National Day 2025</td><td>CNY 2026</td><td>Labor Day 2026</td><td></td></tr><tr><td colspan="30">SSSG</td><td></td></tr><tr><td>Haidiao (avg. tabletum)</td><td>0%</td><td>-8%</td><td>-9%</td><td>-13%</td><td>-6%</td><td>-7%</td><td>0%</td><td>1%</td><td>-2%</td><td>2%</td><td>-1%</td><td>-1%</td><td>-5%</td><td>13%</td><td>1%</td><td>5%</td><td>-1%</td><td>2%</td><td>-10%</td><td>40%</td><td>25%</td><td>40%</td><td>20%</td><td>0%</td><td>-5%</td><td>-10%</td><td>0%</td><td>5%</td><td>0%</td><td></td></tr><tr><td>Tai Er</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>LSD% decl</td><td></td><td>HSD%</td><td>MSD%</td><td>DD%</td><td>LDD%</td><td>DD%</td><td>LDD%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>low teens decline</td><td></td><td>HSD%</td><td></td></tr><tr><td>Nayuki</td><td>-8%</td><td>-13%</td><td>-7%</td><td>3%</td><td>14%</td><td>13%</td><td>22%</td><td>8%</td><td>0%</td><td>-1%</td><td>10%</td><td>0%</td><td></td><td></td><td>-3%</td><td>-11%</td><td></td><td></td><td>-10%</td><td>30%</td><td>-14%</td><td>-20%</td><td>-20%</td><td>-23%</td><td></td><td>20%</td><td></td><td></td><td>-30%</td><td></td></tr><tr><td>Nayuki (average sales per store)</td><td></td><td></td><td></td><td></td><td>20%</td><td>20%</td><td>29%</td><td>15%</td><td>5%</td><td>3%</td><td>13%</td><td>3%</td><td></td><td></td><td>-1%</td><td>-11%</td><td>-24%</td><td>-18%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Guming</td><td>+LSD%</td><td></td><td></td><td>Acceleration</td><td>DD</td><td>DD</td><td colspan="2">&gt;20% (GMV)</td><td>~20% (GMV)</td><td>No slower vs. Sep</td><td></td><td>Slightly slower vs. Oct</td><td>DD%</td><td>SD%</td><td>&gt;20%</td><td>HSD%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>DD%</td><td></td></tr><tr><td>ChaPanda</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>SD%</td><td>DD%</td><td>~25%</td><td>SD%</td><td>DD%</td><td>SD%</td><td>SD%</td><td>Decline</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>DD%</td><td>decline</td><td></td></tr><tr><td>Auntea Jenny</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>close to 20%</td><td></td><td>Slower than 1Q26</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Slower than Apr-26</td><td></td></tr><tr><td colspan="30">SSS vs. 2021</td><td></td></tr><tr><td>Haidiao (avg. tabletum)</td><td>27%</td><td>18%</td><td>23%</td><td>17%</td><td>27%</td><td>52%</td><td>34%</td><td>52%</td><td>17%</td><td>15%</td><td>32%</td><td>26%</td><td>21%</td><td>33%</td><td>24%</td><td>23%</td><td>26%</td><td>24%</td><td>-16%</td><td>5%</td><td>5%</td><td>18%</td><td>26%</td><td>5%</td><td>12%</td><td>14%</td><td>5%</td><td>17%</td><td>14%</td><td></td></tr><tr><td>Nayuki</td><td>-50%</td><td>-54%</td><td>-48%</td><td>-47%</td><td>-41%</td><td>-40%</td><td>-41%</td><td>-28%</td><td>-43%</td><td>-47%</td><td>-38%</td><td>-52%</td><td></td><td></td><td>-49%</td><td>-53%</td><td>-55%</td><td>-54%</td><td>-30%</td><td>-20%</td><td>-31%</td><td>-44%</td><td>-36%</td><td>-47%</td><td></td><td>-23%</td><td></td><td></td><td>-46%</td><td></td></tr><tr><td>Gourmet Master</td><td>-33%</td><td>-27%</td><td>-22%</td><td>-23%</td><td>-28%</td><td>-31%</td><td>-35%</td><td>-34%</td><td>-32%</td><td>-33%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>average</td><td>-18%</td><td>-21%</td><td>-15%</td><td>-18%</td><td>-14%</td><td>-6%</td><td>-14%</td><td>-4%</td><td>-19%</td><td>-22%</td><td>-3%</td><td>-13%</td><td></td><td></td><td>-12%</td><td>-15%</td><td>-15%</td><td>-15%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SSS as % of 2021</td><td>82%</td><td>79%</td><td>85%</td><td>82%</td><td>86%</td><td>94%</td><td>86%</td><td>96%</td><td>81%</td><td>78%</td><td>97%</td><td>87%</td><td></td><td></td><td>88%</td><td>85%</td><td>85%</td><td>85%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="30">SSS vs. 2019</td><td></td></tr><tr><td>Haidiao (avg. tabletum)</td><td>-12%</td><td>-12%</td><td>-14%</td><td>-24%</td><td>-15%</td><td>-19%</td><td>-20%</td><td>-19%</td><td>-29%</td><td>-15%</td><td>-17%</td><td>-17%</td><td>-16%</td><td>0%</td><td>-13%</td><td>-20%</td><td>-16%</td><td>-18%</td><td>-37%</td><td>-24%</td><td>-10%</td><td>-12%</td><td>-8%</td><td>-10%</td><td>-16%</td><td>-18%</td><td>-10%</td><td>-12%</td><td>-18%</td><td></td></tr><tr><td>Gourmet Master</td><td>-34%</td><td>-29%</td><td>-26%</td><td>-29%</td><td>-35%</td><td>-38%</td><td>-42%</td><td>-39%</td><td>-39%</td><td>-39%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>average</td><td>-23%</td><td>-20%</td><td>-20%</td><td>-26%</td><td>-25%</td><td>-29%</td><td>-31%</td><td>-29%</td><td>-34%</td><td>-27%</td><td>-17%</td><td>-17%</td><td>-16%</td><td>0%</td><td>-13%</td><td>-20%</td><td>-16%</td><td>-18%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SSS as % of pre-COVID</td><td>77%</td><td>80%</td><td>80%</td><td>74%</td><td>75%</td><td>71%</td><td>69%</td><td>71%</td><td>66%</td><td>73%</td><td>83%</td><td>83%</td><td>84%</td><td>100%</td><td>87%</td><td>80%</td><td>84%</td><td>82%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data

Exhibit 2: Quarterly SSSG tracker

<table><tr><td colspan="10">SSSG yoy trend</td><td colspan="10">vs. 2019</td></tr><tr><td>SSSG yoy</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td></td></tr><tr><td>KFC China</td><td>-2.0%</td><td>-3.0%</td><td>-2.0%</td><td>-1.0%</td><td>0.0%</td><td>1.0%</td><td>2.0%</td><td>3.0%</td><td>1.0%</td><td>-10%</td><td>-12%</td><td>-12%</td><td>-16%</td><td>-10%</td><td>-11%</td><td>-10%</td><td>-14%</td><td>-9%</td><td></td></tr><tr><td>Pizza Hut China</td><td>-5.0%</td><td>-8.0%</td><td>-6.0%</td><td>-2.0%</td><td>0.0%</td><td>2.0%</td><td>1.0%</td><td>1.0%</td><td>-1.0%</td><td>-8%</td><td>-14%</td><td>-14%</td><td>-16%</td><td>-8%</td><td>-12%</td><td>-13%</td><td>-16%</td><td>-9%</td><td></td></tr><tr><td>YUM China</td><td>-3.0%</td><td>-4.0%</td><td>-3.0%</td><td>-1.0%</td><td>0.0%</td><td>1.0%</td><td>1.0%</td><td>3.0%</td><td>0.0%</td><td>-10%</td><td>-13%</td><td>-12%</td><td>-16%</td><td>-10%</td><td>-12%</td><td>-11%</td><td>-13%</td><td>-10%</td><td></td></tr><tr><td>Starbucks China</td><td>-11.0%</td><td>-14.0%</td><td>-14.0%</td><td>-6.0%</td><td>0.0%</td><td>2.0%</td><td>2.0%</td><td>7.0%</td><td>0.5%</td><td>-33%</td><td>-32%</td><td>-32%</td><td>-34%</td><td>-33%</td><td>-31%</td><td>-30%</td><td>-29%</td><td>-32%</td><td></td></tr><tr><td>Gourmet Master China</td><td>-15.7%</td><td>-16.7%</td><td>-15.2%</td><td>-9.7%</td><td>-9.7%</td><td>-4.0%</td><td>-7.7%</td><td>-10.0%</td><td></td><td>-26%</td><td>-31%</td><td>-35%</td><td>-28%</td><td>-33%</td><td>-34%</td><td>-40%</td><td>-36%</td><td>-33%</td><td></td></tr><tr><td>Xiabuxiabu</td><td>-19.0%</td><td></td><td>-27.6%</td><td></td><td>-15.6%</td><td></td><td></td><td>-3.6%</td><td></td><td></td><td>-55%</td><td></td><td>-54%</td><td></td><td>-62%</td><td></td><td></td><td></td><td></td></tr><tr><td>Coucou</td><td>-43.0%</td><td></td><td>-21.0%</td><td></td><td>-14.0%</td><td></td><td></td><td>-14.4%</td><td></td><td></td><td>-57%</td><td></td><td>-61%</td><td></td><td>-63%</td><td></td><td></td><td></td><td></td></tr><tr><td>Haidilao</td><td>14.5%</td><td></td><td>-4.6%</td><td></td><td>14.5%</td><td></td><td></td><td>-3.0%</td><td>2.0%</td><td></td><td>-16%</td><td></td><td>-22%</td><td></td><td>-4%</td><td></td><td>-24%</td><td></td><td></td></tr><tr><td>Jiu Mao Jiu</td><td>-4.1%</td><td>-12.6%</td><td>-10.3%</td><td>-18.5%</td><td>-18.6%</td><td>-18.5%</td><td>-14.8%</td><td>-16.4%</td><td>-11.3%</td><td>-26%</td><td>-29%</td><td>-26%</td><td>-38%</td><td>-40%</td><td>-43%</td><td>-37%</td><td>-48%</td><td>-47%</td><td></td></tr><tr><td>Tai Er</td><td>-13.9%</td><td>-18.1%</td><td>-18.3%</td><td>-24.6%</td><td>-21.2%</td><td>-13.7%</td><td>-9.3%</td><td>-3.0%</td><td>6.9%</td><td>-24%</td><td>-33%</td><td>-32%</td><td>-41%</td><td>-40%</td><td>-42%</td><td>-38%</td><td>-43%</td><td>-36%</td><td></td></tr><tr><td>Tai Er - China</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>10.9%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Song</td><td>-34.8%</td><td>-36.6%</td><td>-32.5%</td><td>-26.9%</td><td>-24.2%</td><td>-14.3%</td><td>-19.1%</td><td>-19.0%</td><td>-19.9%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Helens</td><td>-29.7%</td><td></td><td>-12.9%</td><td></td><td>-17.9%</td><td></td><td></td><td>-18.9%</td><td></td><td></td><td>-48%</td><td></td><td>-43%</td><td></td><td>-58%</td><td></td><td>-54%</td><td></td><td></td></tr><tr><td>Nayuki</td><td>-28.5%</td><td></td><td>-21.3%</td><td></td><td>-9.3%</td><td>10.0%</td><td>10.0%</td><td>3.0%</td><td>LSD%</td><td></td><td>-47%</td><td></td><td>-44%</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Juewei</td><td>-13.7%</td><td>-11.0%</td><td>-5.5%</td><td>-21.5%</td><td>1.7%</td><td>-10.1%</td><td>0.3%</td><td>18.4%</td><td>-1.2%</td><td>-22%</td><td>-29%</td><td>-27%</td><td>-41%</td><td>-21%</td><td>-36%</td><td>-27%</td><td>-30%</td><td>-22%</td><td></td></tr><tr><td>Guming</td><td></td><td>-1.2%</td><td></td><td></td><td>HSD</td><td>DD</td><td>&gt;20% (GMV)</td><td>DD</td><td>DD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Luckin</td><td>-20.3%</td><td>-20.9%</td><td>-13.1%</td><td>-3.4%</td><td>8.1%</td><td>13.4%</td><td>14.4%</td><td>1.2%</td><td>0.1%</td><td>127%</td><td>116%</td><td>119%</td><td>88%</td><td>145%</td><td>145%</td><td>151%</td><td>90%</td><td>145%</td><td></td></tr><tr><td>Chagee - China</td><td>46.0%</td><td>38.0%</td><td>0.4%</td><td>-19.3%</td><td>-19.1%</td><td>-23.1%</td><td>-27.9%</td><td>-25.5%</td><td>-16.1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tims China - self-operated store</td><td>-11.7%</td><td>-13.8%</td><td>-20.7%</td><td>-12.3%</td><td>-6.5%</td><td>-3.6%</td><td>3.3%</td><td>-1.4%</td><td>-12.4%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tims China - system-wide store</td><td>-13.6%</td><td>-14.6%</td><td>-21.7%</td><td>-13.3%</td><td>-7.8%</td><td>-4.8%</td><td>1.3%</td><td>-2.4%</td><td>-13.2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Domino&#x27;s Pizza China</td><td>3.6%</td><td></td><td>1.6%</td><td></td><td>-1.0%</td><td></td><td></td><td>-1.9%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Saizeriya Shanghai (existing store sales)</td><td>-1.8%</td><td>-6.6%</td><td>-10.5%</td><td>-6.3%</td><td>-14.8%</td><td>-19.7%</td><td>-16.2%</td><td>-11.0%</td><td>-9.1%</td><td>14%</td><td>20%</td><td>11%</td><td>5%</td><td>-3%</td><td>-3%</td><td>-7%</td><td>-6%</td><td>-12%</td><td></td></tr><tr><td>Saizeriya Guangzhou (existing store sales)</td><td>-0.9%</td><td>-7.1%</td><td>-12.1%</td><td>-9.6%</td><td>-15.9%</td><td>-18.2%</td><td>-11.2%</td><td>4.0%</td><td>-1.8%</td><td>38%</td><td>28%</td><td>18%</td><td>7%</td><td>16%</td><td>5%</td><td>5%</td><td>12%</td><td>14%</td><td></td></tr><tr><td>Saizeriya Beijing (existing store sales)</td><td>8.2%</td><td>-2.9%</td><td>-7.2%</td><td>0.4%</td><td>-11.5%</td><td>-18.7%</td><td>-15.4%</td><td>-11.3%</td><td>-14.5%</td><td>29%</td><td>36%</td><td>25%</td><td>25%</td><td>14%</td><td>11%</td><td>6%</td><td>11%</td><td>-3%</td><td></td></tr><tr><td>Saizeriya China average (existing store sales)</td><td>1.8%</td><td>-5.5%</td><td>-9.9%</td><td>-5.2%</td><td>-14.1%</td><td>-18.9%</td><td>-14.3%</td><td>-6.1%</td><td>-8.5%</td><t

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
