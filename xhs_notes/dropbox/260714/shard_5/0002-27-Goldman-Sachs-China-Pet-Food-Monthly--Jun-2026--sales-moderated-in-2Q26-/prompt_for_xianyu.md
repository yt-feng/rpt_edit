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
# China Pet Food Monthly: Jun 2026: sales moderated in 2Q26 with more divergent landscape; China Pet Food led

In this monthly pet food tracker, we monitor: 1) domestic demand for pet food; 2) ASP trajectory and competitive dynamics within product/channel mix shifts; and 3) overseas demand and our monthly cost tracker.

## Overview:

1) GMV performance on Tmall/Taobao/Douyin: In Jun, pet food online GMV accelerated to $17\%$ yoy from $8\%$ yoy decline in May, driven by strong Douyin growth at $40\%$ yoy. In May and Jun combined, which we believe should represent the full picture of 618 shopping festival, Tmall/Taobao/Douyin GMV total grew $12\%$ yoy, mainly driven by $35\%$ yoy increase on Douyin while partially offset by $1\%$ yoy decline on Tmall/Taobao. Total 2Q26 GMV was stable at $14\%$ yoy vs. $14\%$ in 1Q26, with $34\%$ yoy on Douyin and $3\%$ yoy on Tmall/Taobao.

Valerie Zhou  
+852-2978-0820 | valerie.zhou@gs.com  
GS (Asia) L.L.C.

3) On product discounts and Douyin ROI, we saw higher livestreaming sales mix (Exhibit 19) with a shift towards E-shelf/Merchants in 2Q26 (Exhibit 18). We saw Royal Canin and Myfoodie leading fan attraction on a yoy basis in Jun (Exhibit 15).

4) Overseas demand and cost tracker: US total dog and cat food imports via China recovered at 4%/50% yoy in May vs +3%/-30% in Apr, echoing recovery in orders reading from Petpal mgmt. On costs, Jun raw material costs trended lower vs May, with 1-3% MoM decline in Cost index for our covered names. That said, we still see 31%/5% higher PET/chicken prices vs 2025 average. And we note RMB appreciation is likely to lead to FX losses among pet OEMs as well.

2) Performance by brands: In May+Jun combined, local brands continue to show divergent performance where non-listed leading companies are more aggressive (avg. 30% yoy GMV growth online), while global brands continued to show slow growth at 2% yoy in May+Jun; Specifically, China pet food grew 29% yoy with Wanpy being the best-performing local brand at 41% yoy while Zeal/Toptrees at 19%/21%. Gambol declined 4% yoy, with Myfoodie/Fregate at -10%/-6% yoy, albeit Balance Nutrition came in at 95% growth. For Petpal, Meatyway declined 4% yoy in May+Jun-26, with Tmall/Taobao at 1% yoy decline and Douyin declining 13% yoy; However we believe ongoing consolidation trend with top 10 brands in Douyin remains outpaced at 70% yoy in 2Q26 vs top 300's c.40% yoy.

5) Thoughts on recent social media events: While we acknowledge ongoing social media discussions regarding food safety and potential health issues from cat food consumption, we await more proof & evidence regarding the issue. That said, we

Christina Liu  
+852-2978-6983 | christina.liu@gs.com  
GS (Asia) L.L.C.

Leaf Liu  
+852-3966-4169 | leaf.liu@gs.com  
GS (Asia) L.L.C.

## Table of Contents

Domestic online tracker 3
Overseas import demand 11
GS proprietary cost index 12
Disclosure Appendix 15 believe the discussions could lead to better awareness on the pet food quality and stricter government regulation which potentially helps drive industry consolidation.

Within our Pet Foods coverage, we are Neutral on China Pet Foods/Gambol. While we acknowledge China Pet Foods' rising domestic momentum and strong global supply chain which we expect to drive wallet share gains, we expect pressures on profitability in the domestic market with heightened competition and in the overseas market with tariff sharing, FX losses and raw material headwinds. While Gambol maintains a leading position in China, we are Neutral rated on the stock on valuation and fierce competition in the premium-priced cat food segment. We maintain a Sell rating on Petpal, given pressures on domestic and overseas profitability and weaker bargaining power.

Monthly Momentum of Pet Food Sector

![](images/e9bce8713d1a92daeb090570c97c7904dcf191a441012d570df58cded64c5ece.jpg)  
Source: GS Global Investment Research

## Domestic online tracker

## Growth profile - Platform growth and Company growth

Exhibit 1: Category growth on Tmall, Taobao

<table><tr><td></td><td>May+Jun-26</td><td>Jun-26</td><td>2Q26</td><td>1Q26</td><td>4Q25</td><td>3Q25</td><td>2Q25</td><td>1Q25</td><td>2025</td></tr><tr><td>Category</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cat treats</td><td>-6.3%</td><td>-3.6%</td><td>-2.7%</td><td>0.3%</td><td>-16.4%</td><td>-15.7%</td><td>-14.2%</td><td>-15.4%</td><td>-15.4%</td></tr><tr><td>Dog treats</td><td>-10.1%</td><td>1.5%</td><td>-7.8%</td><td>-2.6%</td><td>-12.8%</td><td>-10.2%</td><td>-8.9%</td><td>-10.8%</td><td>-10.7%</td></tr><tr><td>Cat staple food</td><td>0.0%</td><td>5.7%</td><td>4.5%</td><td>0.6%</td><td>-9.4%</td><td>-3.0%</td><td>-4.2%</td><td>0.0%</td><td>-4.5%</td></tr><tr><td>Dog staple food</td><td>2.7%</td><td>11.3%</td><td>4.7%</td><td>-1.2%</td><td>-11.2%</td><td>-9.8%</td><td>-8.4%</td><td>-9.3%</td><td>-9.7%</td></tr><tr><td>Total</td><td>-0.9%</td><td>5.4%</td><td>2.8%</td><td>-0.1%</td><td>-11.0%</td><td>-7.3%</td><td>-7.0%</td><td>-5.5%</td><td>-7.9%</td></tr></table>

Source: Moojing Market Intelligence, Data compiled by GS Global Investment Research

## Exhibit 2: Jun contributed around $9\%$ of total annual GMV in 2025 Tmall/Taobao GMV distribution by month over 2020-2025

<table><tr><td colspan="14">GMV contribution</td></tr><tr><td colspan="2"></td><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td><td>Jul</td><td>Aug</td><td>Sep</td><td>Oct</td><td>Nov</td><td>Dec</td></tr><tr><td rowspan="6">Pet food</td><td>2020</td><td>5%</td><td>6%</td><td>11%</td><td>6%</td><td>7%</td><td>10%</td><td>6%</td><td>8%</td><td>8%</td><td>8%</td><td>15%</td><td>9%</td></tr><tr><td>2021</td><td>8%</td><td>5%</td><td>7%</td><td>7%</td><td>7%</td><td>10%</td><td>7%</td><td>8%</td><td>8%</td><td>8%</td><td>16%</td><td>9%</td></tr><tr><td>2022</td><td>8%</td><td>6%</td><td>7%</td><td>7%</td><td>7%</td><td>12%</td><td>6%</td><td>7%</td><td>8%</td><td>8%</td><td>16%</td><td>9%</td></tr><tr><td>2023</td><td>6%</td><td>7%</td><td>8%</td><td>7%</td><td>6%</td><td>13%</td><td>7%</td><td>8%</td><td>8%</td><td>7%</td><td>16%</td><td>7%</td></tr><tr><td>2024</td><td>9%</td><td>6%</td><td>9%</td><td>8%</td><td>11%</td><td>6%</td><td>7%</td><td>7%</td><td>8%</td><td>11%</td><td>10%</td><td>8%</td></tr><tr><td>2025</td><td>9%</td><td>7%</td><td>10%</td><td>8%</td><td>10%</td><td>9%</td><td>6%</td><td>8%</td><td>7%</td><td>11%</td><td>9%</td><td>7%</td></tr></table>

Green shades denote positive divergence from median, with darker shades indicating higher difference from median.

Source: Moojing Market Intelligence, Chanmama, Data compiled by GS Global Investment Research

Exhibit 3: Gambol/Petpal/China Pet Foods weakened in 2Q26 vs 1Q26 while other local brands accelerated

<table><tr><td rowspan="2">Company brand GMV yoy growth</td><td colspan="3">May+Jun-26</td><td colspan="3">Jun-26</td><td colspan="3">2Q26</td><td colspan="3">1Q26</td><td colspan="3">4Q25</td><td colspan="3">3Q25</td><td colspan="3">2Q25</td><td colspan="3">1Q25</td></tr><tr><td>Tmall/Taobao</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>Douyin</td><td>Total</td></tr><tr><td>Total Pet Food</td><td>-1%</td><td>35%</td><td>12%</td><td>5%</td><td>40%</td><td>17%</td><td>3%</td><td>34%</td><td>14%</td><td>0%</td><td>45%</td><td>14%</td><td>-11%</td><td>53%</td><td>7%</td><td>-7%</td><td>n.a.</td><td>n.a.</td><td>3%</td><td>n.a.</td><td>n.a.</td><td>8%</td><td>n.a.</td><td>n.a.</td></tr><tr><td colspan="25">Local brands</td></tr><tr><td>Gambol</td><td>-9%</td><td>5%</td><td>-4%</td><td>-4%</td><td>3%</td><td>-1%</td><td>-6%</td><td>5%</td><td>-2%</td><td>10%</td><td>3%</td><td>7%</td><td>18%</td><td>16%</td><td>17%</td><td>17%</td><td>48%</td><td>29%</td><td>23%</td><td>73%</td><td>40%</td><td>19%</td><td>95%</td><td>42%</td></tr><tr><td>Myfoodie</td><td>-17%</td><td>2%</td><td>-10%</td><td>-8%</td><td>4%</td><td>-4%</td><td>-12%</td><td>0%</td><td>-7%</td><td>3%</td><td>-10%</td><td>-3%</td><td>10%</td><td>-2%</td><td>5%</td><td>-4%</td><td>16%</td><td>4%</td><td>11%</td><td>44%</td><td>22%</td><td>1%</td><td>60%</td><td>20%</td></tr><tr><td>Balance Nutrition</td><td>274%</td><td>44%</td><td>95%</td><td>283%</td><td>62%</td><td>118%</td><td>255%</td><td>70%</td><td>117%</td><td>132%</td><td>286%</td><td>206%</td><td>134%</td><td>564%</td><td>271%</td><td>125%</td><td>n.a.</td><td>n.a.</td><td>14%</td><td>n.a.</td><td>n.a.</td><td>67%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Fregate</td><td>-8%</td><td>-3%</td><td>-6%</td><td>-12%</td><td>-14%</td><td>-13%</td><td>-11%</td><td>-4%</td><td>-8%</td><td>10%</td><td>-12%</td><td>1%</td><td>22%</td><td>16%</td><td>20%</td><td>94%</td><td>87%</td><td>81%</td><td>65%</td><td>108%</td><td>79%</td><td>90%</td><td>218%</td><td>127%</td></tr><tr><td>China Pet Food</td><td>29%</td><td>29%</td><td>29%</td><td>21%</td><td>21%</td><td>21%</td><td>36%</td><td>27%</td><td>33%</td><td>36%</td><td>86%</td><td>51%</td><td>17%</td><td>99%</td><td>39%</td><td>7%</td><td>77%</td><td>26%</td><td>0%</td><td>81%</td><td>19%</td><td>-7%</td><td>58%</td><td>6%</td></tr><tr><td>Wanpy</td><td>31%</td><td>65%</td><td>41%</td><td>33%</td><td>38%</td><td>34%</td><td>36%</td><td>67%</td><td>46%</td><td>24%</td><td>163%</td><td>53%</td><td>0%</td><td>167%</td><td>33%</td><td>-7%</td><td>148%</td><td>18%</td><td>-6%</td><td>127%</td><td>15%</td><td>-14%</td><td>88%</td><td>-3%</td></tr><tr><td>Zeal</td><td>6%</td><td>37%</td><td>19%</td><td>14%</td><td>46%</td><td>28%</td><td>16%</td><td>34%</td><td>24%</td><td>-13%</td><td>35%</td><td>5%</td><td>-31%</td><td>61%</td><td>-4%</td><td>-28%</td><td>43%</td><td>-2%</td><td>-36%</td><td>52%</td><td>-13%</td><td>-8%</td><td>95%</td><td>14%</td></tr><tr><td>Toptrees</td><td>32%</td><td>0%</td><td>21%</td><td>11%</td><td>-3%</td><td>7%</td><td>41%</td><td>-5%</td><td>23%</td><td>93%</td><td>48%</td><td>75%</td><td>59%</td><td>69%</td><td>62%</td><td>53%</td><td>50%</td><td>52%</td><td>26%</td><td>66%</td><td>39%</td><td>11%</td><td>28%</td><td>17%</td></tr><tr><td colspan="25">Petpal</td></tr><tr><td>Meatway</td><td>-1%</td><td>-13%</td><td>-4%</td><td>69%</td><td>-16%</td><td>45%</td><td>2%</td><td>-6%</td><td>0%</td><td>15%</td><td>5%</td><td>12%</td><td>-6%</td><td>10%</td><td>-4%</td><td>7%</td><td>58%</td><td>22%</td><td>26%</td><td>19%</td><td>24%</td><td>54%</td><td>61%</td><td>56%</td></tr><tr><td>Covered - simple avg</td><td>6%</td><td>7%</td><td>7%</td><td>28%</td><td>3%</td><td>22%</td><td>11%</td><td>9%</td><td>10%</td><td>20%</td><td>31%</td><td>23%</td><td>10%</td><td>42%</td><td>17%</td><td>10%</td><td>61%</td><td>26%</td><td>16%</td><td>57%</td><td>28%</td><td>22%</td><td>72%</td><td>34%</td></tr><tr><td>Nourse</td><td>24%</td><td>190%</td><td>111%</td><td>31%</td><td>164%</td><td>101%</td><td>33%</td><td>227%</td><td>134%</td><td>9%</td><td>300%</td><td>125%</td><td>-23%</td><td>300%</td><td>81%</td><td>-11%</td><td>160%</td><td>49%</td><td>-30%</td><td>116%</td><td>8%</td><td>-5%</td><td>5%</td><td>-2%</td></tr><tr><td>Rosy Fresh</td><td>36%</td><td>18%</td><td>31%</td><td>12%</td><td>40%</td><td>18%</td><td>42%</td><td>24%</td><td>37%</td><td>18%</td><td>38%</td><td>22%</td><td>77%</td><td>39%</td><td>66%</td><td>15%</td><td>55%</td><td>24%</td><td>9%</td><td>116%</td><td>26%</td><td>23%</td><td>167%</td><td>40%</td></tr><tr><td>Yanxuan</td><td>0%</td><td></td><td></td><td>-7%</td><td></td><td></td><td>2%</td><td></td><td></td><td>-11%</td><td></td><td></td><td>-14%</td><td></td><td></td><td>-28%</td><td></td><td></td><td>-22%</td><td></td><td></td><td>-6%</td><td></td><td></td></tr><tr><td>Keres</td><td>-30%</td><td>61%</td><td>-23%</td><td>-22%</td><td>74%</td><td>-14%</td><td>-25%</td><td>46%</td><td>-19%</td><td>-14%</td><td>13%</td><td>-11%</td><td>-29%</td><td>28%</td><td>-25%</td><td>-21%</td><td>-32%</td><td>-23%</td><td>-10%</td><td>-19%</td><td>-11%</td><td>-20%</td><td>1%</td><td>-18%</td></tr><tr><td>Pure &amp; natural</td><td>33%</td><td>92%</td><td>52%</td><td>53%</td><td>106%</td><td>70%</td><td>33%</td><td>84%</td><td>49%</td><td>1%</td><td>47%</td><td>13%</td><td>-19%</td><td>51%</td><td>-3%</td><td>-18%</td><td>95%</td><td>7%</td><td>-27%</td><td>36%</td><td>-15%</td><td>-3%</td><td>27%</td><td>3%</td></tr><tr><td>Honest bite</td><td>-13%</td><td>-29%</td><td>-18%</td><td>-16%</td><td>-23%</td><td>-18%</td><td>-7%</td><td>-30%</td><td>-15%</td><td>0%</td><td>9%</td><td>3%</td><td>8%</td><td>16%</td><td>11%</td><td>32%</td><td>45%</td><td>37%</td><td>24%</td><td>103%</td><td>45%</td><td>76%</td><td>62%</td><td>72%</td></tr><tr><td>Other local - simple avg</td><td>8%</td><td>67%</td><td>30%</td><td>9%</td><td>72%</td><td>31%</td><td>13%</td><td>70%</td><td>37%</td><td>0%</td><td>81%</td><td>30%</td><td>0%</td><td>87%</td><td>26%</td><td>-5%</td><td>65%</td><td>19%</td><td>-9%</td><td>70%</td><td>11%</td><td>11%</td><td>52%</td><td>19%</td></tr><tr><td colspan="25">Global brands</td></tr><tr><td>Royal Canin</td><td>28%</td><td>61%</td><td>31%</td><td>49%</td><td>44%</td><td>48%</td><td>39%</td><td>66%</td><td>42%</td><td>34%</td><td>68%</td><td>37%</td><td>4%</td><td>38%</td><td>7%</td><td>8%</td><td>89%</td><td>12%</td><td>7%</td><td>186%</td><td>14%</td><td>21%</td><td>315%</td><td>28%</td></tr><tr><td>Instinct</td><td>-31%</td><td>-9%</td><td>-30%</td><td>-8%</td><td>21%</td><td>-6%</td><td>-24%</td><td>-14%</td><td>-24%</td><td>-6%</td><td>-97%</td><td>-14%</td><td>-37%</td><td>-92%</td><td>-41%</td><td>-28%</td><td>-24%</td><td>-28%</td><td>9%</td><td>86%</td><td>12%</td><td>-1%</td><td>271%</td><td>6%</td></tr><tr><td>Orijen</td><td>2%</td><td>34%</td><td>8%</td><td>26%</td><td>59%</td><td>30%</td><td>9%</td><td>40%</td><td>14%</td><td>6%</td><td>175%</td><td>17%</td><td>-5%</td><td>61%</td><td>6%</td><td>-7%</td><td>-20%</td><td>-9%</td><td>-5%</td><td>82%</td><td>2%</td><td>21%</td><td>-5%</td><td>19%</td></tr><tr><td>Acana</td><td>1%</td><td>-2%</td><td>1%</td><td>15%</td><td>39%</td><td>17%</td><td>9%</td><td>11%</td><td>9%</td><td>-1%</td><td>152%</td><td>8%</td><td>-11%</td><td>35%</td><td>-4%</td><td>-12%</td><td>-39%</td><td>-16%</td><td>5%</td><td>37%</td><td>8%</td><td>36%</td><td>4%</td><td>33%</td></tr><tr><td>Global brands - simple avg</td><td>0%</td><td>21%</td><td>2%</td><td>20%</td><td>40%</td><td>22%</td><td>8%</td><td>25%</td><td>10%</td><td>8%</td><td>75%</td><td>12%</td><td>-12%</td><td>10%</td><td>-8%</td><td>-10%</td><td>2%</td><td>-10%</td><td>4%</td><td>98%</td><td>9%</td><td>19%</td><td>146%</td><td>22%</td></tr></table>

Applied Pet Marketing data for Douyin Industry GMV in Jun 2026; other Douyin data from Chanmama

Source: Moojing Market Intelligence, Chanmama, Pet Marketing, Data compiled by GS Global Investment Research

Exhibit 4: Douyin channel mix increased in 2Q26 vs 1Q26 for most brands

<table><tr><td rowspan="2">Each channel GMV % of total GMV</td><td colspan="2">May+Jun-26</td><td colspan="2">Jun-26</td><td colspan="2">2Q26</td><td colspan="2">1Q26</td><td colspan="2">4Q25</td><td colspan="2">3Q25</td><td colspan="2">2Q25</td><td colspan="2">1Q25</td><td colspan="2">2025</td><td colspan="2">2024</td></tr><tr><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao<

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
