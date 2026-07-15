你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# Switching Trends

# 1Q26 Switching Trends: AI switching drives strength; Campus steadily improving

Industry Overview

## DC leading overall switch growth; Strong Campus growth

The switching market is showing no signs of slowdown. The overall market grew 36.1% YoY, with data center (DC) switching up 50% YoY, broken out by AI back-end switching up 121% YoY and front-end switching growing 26% YoY. Growth continues to be driven by Tier-1 and Tier-2 Cloud providers driving elevated investments in both AI and non-AI infrastructure, with Capex across the top five hyperscalers expected to grow 85% YoY in 2026, above 2025's 72% growth. In 1Q, the top 4 hyperscalers accounted for 41% of the DC switching market and grew 90.4% YoY. Just to put this in perspective, the very same segment grew only 1.6% in 1Q24. Campus switching also shows strong momentum, up 15.1% YoY, an important distinction for Cisco who holds 53.5% share of this segment.

## Both back-end and front-end switching leading DC growth

Data Center switching is the largest segment, accounting for 66% of the total switching market. This segment was up 50% in 1Q, driven by 90% growth from hyperscalers, 51% growth in Tier-2 and NeoClouds, and 16% growth in the Enterprise segment. We divide the market into two main segments: AI back-end accounts for \~38% of the DC switching market, where AI DC buildouts drove 121% YoY growth, as well as Front-end switching, that also grew nicely, accelerating to 25.6% YoY growth from 11.8% last year. At the aggregate level, Arista leads the DC switching market, growing share from 19.6% to 21.1% QoQ, followed by Cisco that grew share from 16.6% to 17.8% sequentially and Celestica who also grew share from 13.2% to 14.7% in the same period.

## Back-end growth driven by Data Center buildouts

AI back-end DC switching was up 121% YoY, accounting for 38% of total DC demand versus 26% a year ago. We recognize that the growth is cyclical, but the data does not show any evidence of growth slowdown. The most interesting trend was Cisco's share gain, increasing from zero last year to 7.9% in 1Q26, mostly attributed to its growing position with hyperscalers. Cisco's share at Hyperscaler back-end switching grew from nil in 1Q25 to 13.2% in 1Q26, matching now Arista's 13.2% and NVidia's 13%, which we attribute mostly to Cisco's penetration to Meta's 800G leaf switch layer. Celestica remains the largest player in back-end switching, holding 26.3% share, followed by Nvidia's 24.5% and Arista's 12.1%. Lastly, we highlight Arista's growing share in the Neocloud and Tier-2 Cloud market, with its share growing from 2% in 1Q24 to 11.1% in 1Q25 and now at 19.1% in 1Q26.

## Front-end remains steady, supported by Cloud/Enterprise

Back-end investments also drive front-end demand, with this segment accelerating to 26% YoY growth in 1Q26 from 11.8% in 1Q25. We highlight three key trends: First, Hyperscalers (32% of total) continue to invest in Front-end switching networks, up 51% YoY vs. 25.2% growth in 1Q25. Enterprise growth (42% of total) is also solid at 13.4%, although somewhat down from last year's growth. Second, Cisco and Arista lead the Front-end market, at 23.8% and 26.5%, fluctuating around the same levels in the last few quarters. Lastly, Arista's implied guidance for Front-end switching calls for no growth in 2026, while in reality, this segment grew 19.1% YoY in 1Q26, suggesting upside to its implied growth guidance. Analysis of Campus Switching on Page 3.

## 14 July 2026

Equity
United States
Telecom Equipment

Tal Liani
Research Analyst
BofAS
+1 646 855 5107
tal.liani@bofa.com

Tomer Zilberman
Research Analyst
BofAS
+1 646 855 3203
tomer.zilberman@bofa.com

Research Analyst

BofAS

+1 646 855-1540

kevin.niederpruem@bofa.com

Research Analyst

BofAS

+1 646 855 1971

eden.vacnich@bofa.com

## Contents

Switching Market Overview 4
Total Switching Market Trends 4
Campus Switching Market Trends 5
Data Center Switching Market Trends 5
Front-End Data Center Switching Market Trends 8
AI Back-End Data Center Switching Market Trends 12

## Campus growth improving on refresh opportunity

Campus switching accounts for 34% of total switching and was up 15.1% YoY in 1Q26. We believe the underlying growth is about 10-11%, with the reported 15% growth somewhat bolstered by reconciliation done by market research company Dell'Oro. Regardless, we highlight a few key trends: a) the market is consistently growing at 9%+ vs. historical levels of 1-2%, driven by product introduction and refreshes. b) Market shares fluctuate from quarter to quarter, but remain relatively stable. Cisco leads the market with 53% share, HPE at 12% and Arista at 3%. c) Lastly, Cisco's share should increase in the next few quarters, driven by the end-of-service (EOS) of its Catalyst 4000 series in 2026 and the Catalyst 6000 series reaching EOS at year-end 2027.

## Switching Market Overview

We present the total market data first, followed by the Campus and Data Center segments. All figures are global, unless otherwise noted.
Total Switching Market Trends

## By Vendor

Exhibit 1: The total switching market declined about 6% sequentially, in line with historical seasonality
Total Switching Market Revenue, Broken Out by Vendor

<table><tr><td>Calendar Year ($mn)</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td></td><td>$8,784.2</td><td>$10,194.4</td><td>$10,924.9</td><td>$11,725.2</td><td>$11,076.2</td><td>$13,453.0</td><td>$14,483.0</td><td>$15,961.5</td><td>$15,073.1</td><td></td><td></td><td></td><td>$31,588.0</td><td>$36,533.8</td><td>$43,663.1</td><td>$41,628.7</td><td>$54,973.7</td></tr><tr><td>QoQ Chg (%)</td><td>-13.6%</td><td>16.1%</td><td>7.2%</td><td>7.3%</td><td>-5.5%</td><td>21.5%</td><td>7.7%</td><td>10.2%</td><td>-5.6%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>YoY Chg (%)</td><td>-12.6%</td><td>-13.9%</td><td>-5.9%</td><td>15.3%</td><td>26.1%</td><td>32.0%</td><td>32.6%</td><td>36.1%</td><td>36.1%</td><td></td><td></td><td></td><td>9.4%</td><td>15.7%</td><td>19.5%</td><td>-4.7%</td><td>32.1%</td></tr><tr><td>Market Share (%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cisco</td><td>39.5%</td><td>34.7%</td><td>36.9%</td><td>33.7%</td><td>32.7%</td><td>29.5%</td><td>30.2%</td><td>28.1%</td><td>29.8%</td><td></td><td></td><td></td><td>44.1%</td><td>43.3%</td><td>44.1%</td><td>36.0%</td><td>29.9%</td></tr><tr><td>Arista</td><td>15.0%</td><td>13.8%</td><td>13.8%</td><td>13.6%</td><td>15.2%</td><td>13.8%</td><td>13.0%</td><td>12.9%</td><td>15.1%</td><td></td><td></td><td></td><td>7.5%</td><td>10.1%</td><td>11.4%</td><td>14.0%</td><td>13.6%</td></tr><tr><td>Huawei</td><td>8.0%</td><td>13.5%</td><td>10.5%</td><td>13.1%</td><td>6.7%</td><td>10.9%</td><td>10.1%</td><td>12.6%</td><td>6.7%</td><td></td><td></td><td></td><td>11.6%</td><td>11.3%</td><td>10.4%</td><td>11.4%</td><td>10.4%</td></tr><tr><td>White Box - Celestica</td><td>3.6%</td><td>4.9%</td><td>5.5%</td><td>5.3%</td><td>8.1%</td><td>7.8%</td><td>8.8%</td><td>8.1%</td><td>9.7%</td><td></td><td></td><td></td><td>0.0%</td><td>0.0%</td><td>2.8%</td><td>4.9%</td><td>8.2%</td></tr><tr><td>HPE</td><td>5.7%</td><td>5.7%</td><td>4.4%</td><td>4.6%</td><td>4.5%</td><td>4.7%</td><td>6.7%</td><td>6.3%</td><td>5.9%</td><td></td><td></td><td></td><td>5.1%</td><td>4.6%</td><td>6.5%</td><td>5.1%</td><td>5.7%</td></tr><tr><td>Nvidia</td><td>1.5%</td><td>2.6%</td><td>2.4%</td><td>2.4%</td><td>5.1%</td><td>4.8%</td><td>5.0%</td><td>5.5%</td><td>6.3%</td><td></td><td></td><td></td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>2.3%</td><td>5.1%</td></tr><tr><td>White Box - Others</td><td>6.0%</td><td>5.5%</td><td>6.2%</td><td>6.3%</td><td>4.7%</td><td>4.1%</td><td>4.6%</td><td>4.7%</td><td>5.4%</td><td></td><td></td><td></td><td>7.6%</td><td>7.8%</td><td>4.2%</td><td>6.0%</td><td>4.6%</td></tr><tr><td>White Box - Accton</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>3.1%</td><td>3.3%</td><td>3.9%</td><td>4.0%</td><td>4.6%</td><td></td><td></td><td></td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>3.7%</td></tr><tr><td>Extreme</td><td>1.0%</td><td>1.1%</td><td>1.2%</td><td>1.1%</td><td>1.2%</td><td>1.1%</td><td>1.0%</td><td>1.0%</td><td>1.0%</td><td></td><td></td><td></td><td>1.8%</td><td>1.6%</td><td>1.6%</td><td>1.1%</td><td>1.1%</td></tr><tr><td>Fortinet</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.8%</td><td>0.7%</td><td>0.8%</td><td>0.8%</td><td>0.9%</td><td></td><td></td><td></td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.8%</td></tr><tr><td>Vistance Networks (formerly CommScope)</td><td>0.4%</td><td>0.3%</td><td>0.4%</td><td>0.3%</td><td>0.4%</td><td>0.3%</td><td>0.4%</td><td>0.4%</td><td>0.3%</td><td></td><td></td><td></td><td>0.6%</td><td>0.4%</td><td>0.6%</td><td>0.3%</td><td>0.4%</td></tr><tr><td>Juniper</td><td>2.6%</td><td>2.5%</td><td>3.2%</td><td>2.9%</td><td>2.4%</td><td>3.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td></td><td></td><td></td><td>2.9%</td><td>3.2%</td><td>2.9%</td><td>2.8%</td><td>1.2%</td></tr><tr><td>Other Vendors</td><td>16.8%</td><td>15.5%</td><td>15.6%</td><td>16.8%</td><td>15.1%</td><td>15.8%</td><td>15.4%</td><td>15.5%</td><td>14.2%</td><td></td><td></td><td></td><td>18.8%</td><td>17.8%</td><td>15.6%</td><td>16.1%</td><td>15.5%</td></tr></table>

Source: Dell'Oro  
BofA GLOBAL RESEARCH

## Campus Switching versus Data Center Switching

Exhibit 2: Increased Cloud and AI investments drove the data center segment up to account for 66% of overall switching, up from about 45% historically
Total Switching Market Revenue, Broken Out by Switch Type

<table><tr><td>Calendar Year ($mn)</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td></td><td>$8,784.2</td><td>$10,194.4</td><td>$10,924.9</td><td>$11,725.2</td><td>$11,076.2</td><td>$13,453.0</td><td>$14,483.0</td><td>$15,961.5</td><td>$15,073.1</td><td></td><td></td><td></td><td>$31,588.0</td><td>$36,533.8</td><td>$43,663.1</td><td>$41,628.7</td><td>$54,973.7</td></tr><tr><td>QoQ Chg (%)</td><td>-13.6%</td><td>16.1%</td><td>7.2%</td><td>7.3%</td><td>-5.5%</td><td>21.5%</td><td>7.7%</td><td>10.2%</td><td>-5.6%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>YoY Chg (%)</td><td>-12.6%</td><td>-13.9%</td><td>-5.9%</td><td>15.3%</td><td>26.1%</td><td>32.0%</td><td>32.6%</td><td>36.1%</td><td>36.1%</td><td></td><td></td><td></td><td>9.4%</td><td>15.7%</td><td>19.5%</td><td>-4.7%</td><td>32.1%</td></tr><tr><td>Switch Share (%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Campus</td><td>47.1%</td><td>46.7%</td><td>47.0%</td><td>48.3%</td><td>40.0%</td><td>40.4%</td><td>38.5%</td><td>38.9%</td><td>33.8%</td><td></td><td></td><td></td><td>53.7%</td><td>53.1%</td><td>56.0%</td><td>47.3%</td><td>39.4%</td></tr><tr><td>Data Center</td><td>52.9%</td><td>53.3%</td><td>53.0%</td><td>51.7%</td><td>60.0%</td><td>59.6%</td><td>61.5%</td><td>61.1%</td><td>66.2%</td><td></td><td></td><td></td><td>46.3%</td><td>46.9%</td><td>44.0%</td><td>52.7%</td><td>60.6%</td></tr></table>

Source: Dell'Oro  
BofA GLOBAL RESEARCH

![](images/30ea237d4d27eb608f2746dfe71d6aba43b347c6fb44dc3d17a70716b9a219ee.jpg)

## Campus Switching Market Trends

Exhibit 3: Campus switching declined 18% sequentially, a reflection of historical seasonal patterns of Enterprise spending Campus Switching Market Revenue, Broken Out by Vendor

<table><tr><td>Calendar Year ($mn)</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td></td><td>$4,140.0</td><td>$4,759.1</td><td>$5,139.7</td><td>$5,666.8</td><td>$4,425.0</td><td>$5,441.7</td><td>$5,573.8</td><td>$6,210.3</td><td>$5,091.3</td><td></td><td></td><td></td><td>$16,970.4</td><td>$19,388.2</td><td>$24,442.7</td><td>$19,705.6</td><td>$21,650.8</td></tr><tr><td>% of Total</td><td>47.1%</td><td>46.7%</td><td>47.0%</td><td>48.3%</td><td>40.0%</td><td>40.4%</td><td>38.5%</td><td>38.9%</td><td>33.8%</td><td></td><td></td><td></td><td>53.7%</td><td>53.1%</td><td>56.0%</td><td>47.3%</td><td>39.4%</td></tr><tr><td>QoQ Chg (%)</td><td>-23.9%</td><td>15.0%</td><td>8.0%</td><td>10.3%</td><td>-21.9%</td><td>23.0%</td><td>2.4%</td><td>11.4%</td><td>-18.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>YoY Chg (%)</td><td>-23.1%</td><td>-30.3%</td><td>-24.4%</td><td>4.2%</td><td>6.9%</td><td>14.3%</td><td>8.4%</td><td>9.6%</td><td>15.1%</td><td></td><td></td><td></td><td>9.3%</td><td>14.2%</td><td>26.1%</td><td>-19.4%</td><td>9.9%</td></tr><tr><td>Market Share (%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cisco</td><td>54.7%</td><td>51.2%</td><td>54.2%</td><td>49.0%</td><td>53.7%</td><td>49.9%</td><td>51.3%</td><td>46.2%</td><td>53.5%</td><td></td><td></td><td></td><td>52.8%</td><td>54.4%</td><td>55.8%</td><td>52.1%</td><td>50.0%</td></tr><tr><td>Huawei</td><td>9.2%</td><td>15.4%</td><td>13.3%</td><td>17.7%</td><td>7.9%</td><td>12.7%</td><td>12.1%</td><td>17.6%</td><td>8.2%</td><td></td><td></td><td></td><td>12.3%</td><td>12.8%</td><td>11.2%</td><td>14.2%</td><td>13.0%</td></tr><tr><td>HPE</td><td>10.3%</td><td>10.2%</td><td>8.0%</td><td>7.9%</td><td>9.4%</td><td>9.7%</td><td>12.0%</td><td>10.4%</td><td>12.1%</td><td></td><td></td><td></td><td>8.5%</td><td>7.9%</td><td>10.3%</td><td>9.0%</td><td>10.4%</td></tr><tr><td>Arista</td><td>3.0%</td><td>2.6%</td><td>2.5%</td><td>2.2%</td><td>3.2%</td><td>3.0%</td><td>2.6%</td><td>2.4%</td><td>3.3%</td><td></td><td></td><td></td><td>0.9%</td><td>1.2%</td><td>1.5%</td><td>2.5%</td><td>2.8%</td></tr><tr><td>Extreme</td><td>1.8%</td><td>2.1%</td><td>2.2%</td><td>2.0%</td><td>2.7%</td><td>2.4%</td><td>2.4%</td><td>2.2%</td><td>2.7%</td><td></td><td></td><td></td><td>2.7%</td><td>2.4%</td><td>2.5%</td><td>2.0%</td><td>2.4%</td></tr><tr><td>Fortinet</td><td></td><td></td><td></td><td></td><td>2.1%</td><td>1.8%</td><td>2.0%</td><td>2.2%</td><td>2.6%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2.0%</td></tr><tr><td>Juniper</td><td>2.5%</td><td>2.5%</td><td>2.9%</td><td>2.8%</td><td>2.9%</td><td>2.8%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td></td><td></td><td></td><td>2.5%</td><td>2.6%</td><td>2.9%</td><td>2.7%</td><td>1.3%</td></tr><tr><td>Vistance Networks (formerly CommScope)</td><td>0.8%</td><td>0.7%</td><td>0.8%</td><td>0.6%</td><td>0.9%</td><td>0.7%</td><td>1.1%</td><td>1.1%</td><td>0.9%</td><td></td><td></td><td></td><td>1.1%</td><td>0.7%</td><td>1.0%</td><td>0.7%</td><td>1.0%</td></tr><tr><td>Other Vendors</td><td>17.6%</td><td>15.3%</td><td>16.1%</td><td>17.8%</td><td>17.2%</td><td>17.0%</td><td>16.5%</td><td>17.9%</td><td>16.7%</td><td></td><td></td><td></td><td>19.2%</td><td>18.1%</td><td>14.8%</td><td>16.7%</td><td>17.1%</td></tr></table>

Source: Dell'Oro  
BofA GLOBAL RESEARCH

## Data Center Switching Market Trends

## By Vendor

Exhibit 4: The data center switching market grew 2% QoQ, a cool down from the last few q

[中间内容因长度限制已省略]

ect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

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
