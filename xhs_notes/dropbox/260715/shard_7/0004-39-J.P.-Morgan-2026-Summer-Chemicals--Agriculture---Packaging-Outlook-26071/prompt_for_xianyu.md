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
# 2026 Summer Chemicals, Agriculture & Packaging Outlook

Specialty, Commodity, and Agricultural Chemicals & Packaging

Jeffrey J. Zekauskas AC
1-(212)-622-6644
jeffrey.zekauskas@JPM.com
Bloomberg Finance L.P.
JPM Securities LLC

Silke Kueck
1-(212)-622-6503
Silke.x.kueck@JPM.com
JPM Securities LLC

Katie Zhang
1-(212)-622-3262
Katie.zhang@JPM.com
JPM Securities LLC

Lydia Huang
1-(212)-622-0086
Lydia.huang@JPM.com
JPM Securities LLC

## Table of Contents

Pages 3-13: Equity Performances & Valuation

Pages 14-17: Macroeconomic trends

Pages 18-50: Commodity Pricing, Margin, Supply/Demand, Expansions, Exports

Pages 51-57: Housing & Construction Data

Pages 58-70: Global Automotive Sales, Production, Mileage, Collision & Vehicle Repair

Pages 71-74: Beverage Can Supply/Demand, Market Share

Pages 75-91: Agricultural Commodities / Grains

Pages 92-113: Fertilizers

## Stock Performance, 2026 YTD

<table><tr><td rowspan="2">Name</td><td rowspan="2">Market Value ($b) 7/10/2026</td><td rowspan="2">Rating</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026 YTD</td></tr><tr><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td><td>Incr/(Decr)</td></tr><tr><td>Compass Minerals</td><td>1.25</td><td>N</td><td>7.1%</td><td>8.5%</td><td>(13.3%)</td><td>4.1%</td><td>(7.8%)</td><td>(42.3%)</td><td>46.2%</td><td>1.2%</td><td>(17.2%)</td><td>(19.7%)</td><td>(38.2%)</td><td>(55.6%)</td><td>74.6%</td><td>51.9%</td></tr><tr><td>CF Industries Holdings</td><td>17.96</td><td>N</td><td>14.7%</td><td>16.9%</td><td>(25.1%)</td><td>(22.9%)</td><td>35.1%</td><td>2.3%</td><td>9.7%</td><td>(18.9%)</td><td>82.8%</td><td>20.4%</td><td>(6.7%)</td><td>7.3%</td><td>(9.4%)</td><td>51.2%</td></tr><tr><td>Chemours</td><td>2.68</td><td>N</td><td>NA</td><td>NA</td><td>NA</td><td>312.1%</td><td>126.6%</td><td>(43.6%)</td><td>(35.9%)</td><td>37.0%</td><td>35.4%</td><td>(8.8%)</td><td>3.0%</td><td>(46.4%)</td><td>(30.2%)</td><td>51.1%</td></tr><tr><td>Tronox</td><td>0.98</td><td>N</td><td>26.4%</td><td>3.5%</td><td>(83.6%)</td><td>163.7%</td><td>98.9%</td><td>(62.1%)</td><td>46.8%</td><td>28.0%</td><td>64.4%</td><td>(42.9%)</td><td>3.3%</td><td>(28.9%)</td><td>(58.6%)</td><td>47.2%</td></tr><tr><td>Bayer AG</td><td>49.61</td><td>OW</td><td>41.8%</td><td>10.8%</td><td>2.5%</td><td>(14.4%)</td><td>4.9%</td><td>(40.8%)</td><td>20.2%</td><td>(33.9%)</td><td>(2.4%)</td><td>4.5%</td><td>(30.4%)</td><td>(42.6%)</td><td>91.6%</td><td>36.4%</td></tr><tr><td>Valvoline</td><td>4.93</td><td>N</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>16.6%</td><td>(22.8%)</td><td>10.6%</td><td>8.1%</td><td>61.1%</td><td>(12.4%)</td><td>15.1%</td><td>(3.7%)</td><td>(19.7%)</td><td>33.0%</td></tr><tr><td>Cabot Corp.</td><td>4.51</td><td>UW</td><td>29.2%</td><td>(14.7%)</td><td>(6.8%)</td><td>23.6%</td><td>21.9%</td><td>(30.3%)</td><td>10.7%</td><td>(5.6%)</td><td>25.2%</td><td>18.9%</td><td>24.9%</td><td>9.4%</td><td>(27.4%)</td><td>31.7%</td></tr><tr><td>LyondellBasell</td><td>18.19</td><td>N</td><td>40.6%</td><td>(1.1%)</td><td>9.5%</td><td>(1.3%)</td><td>28.6%</td><td>(24.6%)</td><td>13.6%</td><td>(3.0%)</td><td>0.6%</td><td>(10.0%)</td><td>14.5%</td><td>(21.9%)</td><td>(41.7%)</td><td>30.1%</td></tr><tr><td>Corteva</td><td>57.52</td><td>N</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>31.0%</td><td>22.1%</td><td>24.3%</td><td>(18.5%)</td><td>18.9%</td><td>17.7%</td><td>27.8%</td></tr><tr><td>Linde</td><td>245.08</td><td>OW</td><td>18.8%</td><td>(0.4%)</td><td>(21.0%)</td><td>14.4%</td><td>32.0%</td><td>0.9%</td><td>36.4%</td><td>23.8%</td><td>31.5%</td><td>(5.8%)</td><td>25.9%</td><td>1.9%</td><td>1.8%</td><td>24.3%</td></tr><tr><td>Dow</td><td>20.92</td><td>OW</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>1.4%</td><td>2.2%</td><td>(11.2%)</td><td>8.8%</td><td>(26.8%)</td><td>(41.7%)</td><td>24.2%</td></tr><tr><td>Methanex</td><td>3.76</td><td>N</td><td>85.9%</td><td>(22.6%)</td><td>(28.0%)</td><td>32.7%</td><td>38.2%</td><td>(20.5%)</td><td>(19.5%)</td><td>19.3%</td><td>(14.2%)</td><td>(4.3%)</td><td>25.1%</td><td>5.4%</td><td>(20.5%)</td><td>22.5%</td></tr><tr><td>Air Products &amp; Chemicals</td><td>66.70</td><td>OW</td><td>33.0%</td><td>29.0%</td><td>(9.8%)</td><td>19.6%</td><td>14.1%</td><td>(2.5%)</td><td>46.8%</td><td>16.3%</td><td>11.4%</td><td>1.3%</td><td>(11.2%)</td><td>5.9%</td><td>(14.8%)</td><td>21.3%</td></tr><tr><td>Ball Corp</td><td>16.42</td><td>OW</td><td>16.9%</td><td>34.2%</td><td>5.5%</td><td>2.4%</td><td>0.8%</td><td>18.4%</td><td>43.8%</td><td>44.1%</td><td>2.4%</td><td>(45.9%)</td><td>12.5%</td><td>(4.2%)</td><td>(3.9%)</td><td>16.5%</td></tr><tr><td>Intl. Flavors &amp; Fragrances</td><td>19.79</td><td>OW</td><td>29.2%</td><td>17.9%</td><td>18.0%</td><td>(1.5%)</td><td>29.5%</td><td>(12.0%)</td><td>(3.9%)</td><td>(15.6%)</td><td>38.4%</td><td>(30.4%)</td><td>(22.8%)</td><td>4.4%</td><td>(20.3%)</td><td>15.0%</td></tr><tr><td>PPG Industries</td><td>26.03</td><td>OW</td><td>40.1%</td><td>21.9%</td><td>(14.5%)</td><td>(4.1%)</td><td>23.3%</td><td>(12.5%)</td><td>30.6%</td><td>8.0%</td><td>19.6%</td><td>(27.1%)</td><td>18.9%</td><td>(20.1%)</td><td>(14.2%)</td><td>14.0%</td></tr><tr><td>Ashland</td><td>3.06</td><td>OW</td><td>20.7%</td><td>23.4%</td><td>(14.2%)</td><td>6.4%</td><td>33.2%</td><td>(0.3%)</td><td>7.8%</td><td>3.5%</td><td>35.9%</td><td>(0.1%)</td><td>(21.6%)</td><td>(15.2%)</td><td>(17.9%)</td><td>13.8%</td></tr><tr><td>Scotts Miracle-Gro</td><td>3.81</td><td>N</td><td>41.2%</td><td>0.2%</td><td>3.5%</td><td>48.1%</td><td>12.0%</td><td>(42.6%)</td><td>72.8%</td><td>93.1%</td><td>(19.2%)</td><td>(69.8%)</td><td>31.2%</td><td>4.1%</td><td>(12.0%)</td><td>12.2%</td></tr><tr><td>DuPont</td><td>18.40</td><td>OW</td><td>37.3%</td><td>2.7%</td><td>12.9%</td><td>11.1%</td><td>24.5%</td><td>(24.9%)</td><td>(15.6%)</td><td>10.8%</td><td>13.6%</td><td>(15.0%)</td><td>12.1%</td><td>(0.9%)</td><td>26.1%</td><td>11.7%</td></tr><tr><td>Silgan</td><td>4.75</td><td>OW</td><td>15.6%</td><td>11.6%</td><td>0.2%</td><td>(4.7%)</td><td>14.8%</td><td>(19.6%)</td><td>31.6%</td><td>19.3%</td><td>15.8%</td><td>21.0%</td><td>(12.7%)</td><td>15.0%</td><td>(22.4%)</td><td>11.4%</td></tr><tr><td>Huntsman Corp.</td><td>1.94</td><td>N</td><td>54.7%</td><td>(7.4%)</td><td>(50.1%)</td><td>67.8%</td><td>74.5%</td><td>(42.1%)</td><td>25.2%</td><td>4.1%</td><td>38.7%</td><td>(21.2%)</td><td>(8.6%)</td><td>(28.3%)</td><td>(44.5%)</td><td>11.3%</td></tr><tr><td>Celanese</td><td>5.15</td><td>OW</td><td>24.2%</td><td>8.4%</td><td>12.3%</td><td>16.9%</td><td>36.0%</td><td>(16.0%)</td><td>36.8%</td><td>5.5%</td><td>29.3%</td><td>(39.2%)</td><td>52.0%</td><td>(55.5%)</td><td>(38.9%)</td><td>11.0%</td></tr><tr><td>Crown</td><td>12.46</td><td>OW</td><td>21.1%</td><td>14.2%</td><td>(0.4%)</td><td>3.7%</td><td>7.0%</td><td>(26.1%)</td><td>74.5%</td><td>38.1%</td><td>10.4%</td><td>(25.7%)</td><td>12.0%</td><td>(10.2%)</td><td>24.5%</td><td>8.3%</td></tr><tr><td>Orion</td><td>0.32</td><td>UW</td><td>NA</td><td>NA</td><td>(25.8%)</td><td>49.6%</td><td>35.8%</td><td>(1.3%)</td><td>(23.7%)</td><td>(11.2%)</td><td>7.1%</td><td>(3.0%)</td><td>55.7%</td><td>(43.1%)</td><td>(66.6%)</td><td>7.8%</td></tr><tr><td>Nutrien</td><td>31.36</td><td>OW</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>1.9%</td><td>0.5%</td><td>56.1%</td><td>(2.9%)</td><td>(22.9%)</td><td>(20.6%)</td><td>37.9%</td><td>6.0%</td></tr><tr><td>Eastman Chemical</td><td>7.73</td><td>OW</td><td>21.0%</td><td>(4.2%)</td><td>(11.5%)</td><td>10.9%</td><td>23.2%</td><td>(22.0%)</td><td>8.4%</td><td>26.5%</td><td>20.6%</td><td>(32.6%)</td><td>10.3%</td><td>1.7%</td><td>(30.1%)</td><td>5.9%</td></tr><tr><td>Ecolab</td><td>77.20</td><td>OW</td><td>45.0%</td><td>0.2%</td><td>9.4%</td><td>2.5%</td><td>14.5%</td><td>9.8%</td><td>31.0%</td><td>12.1%</td><td>8.4%</td><td>(38.0%)</td><td>36.3%</td><td>18.1%</td><td>12.0%</td><td>4.5%</td></tr><tr><td>Amcor</td><td>19.96</td><td>OW</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>(0.8%)</td><td>8.6%</td><td>2.0%</td><td>(0.8%)</td><td>(19.1%)</td><td>(2.4%)</td><td>(11.4%)</td><td>3.5%</td></tr><tr><td>Sherwin-Williams</td><td>82.37</td><td>OW</td><td>19.3%</td><td>43.3%</td><td>(1.3%)</td><td>3.5%</td><td>52.6%</td><td>(4.0%)</td><td>48.3%</td><td>25.9%</td><td>43.8%</td><td>(32.6%)</td><td>31.4%</td><td>9.0%</td><td>(4.7%)</td><td>3.1%</td></tr><tr><td>Westlake</td><td>9.67</td><td>N</td><td>53.9%</td><td>0.1%</td><td>(11.1%)</td><td>3.1%</td><td>90.3%</td><td>(37.9%)</td><td>6.0%</td><td>16.3%</td><td>19.0%</td><td>5.6%</td><td>36.5%</td><td>(18.1%)</td><td>(35.5%)</td><td>2.1%</td></tr><tr><td>RPM International</td><td>13.41</td><td>OW</td><td>41.4%</td><td>22.2%</td><td>(13.1%)</td><td>22.2%</td><td>(2.6%)</td><td>12.1%</td><td>30.6%</td><td>18.3%</td><td>11.3%</td><td>(3.5%)</td><td>14.6%</td><td>10.2%</td><td>(15.5%)</td><td>1.1%</td></tr><tr><td>Axalta</td><td>6.96</td><td>NR</td><td>NA</td><td>NA</td><td>2.4%</td><td>2.1%</td><td>19.0%</td><td>(27.6%)</td><td>29.8%</td><td>(6.1%)</td><td>16.0%</td><td>(23.1%)</td><td>33.4%</td><td>0.7%</td><td>(5.6%)</td><td>0.6%</td></tr><tr><td>Olin</td><td>2.36</td><td>N</td><td>33.6%</td><td>(21.1%)</td><td>(24.2%)</td><td>48.4%</td><td>38.9%</td><td>(43.5%)</td><td>(14.2%)</td><td>42.4%</td><td>134.2%</td><td>(8.0%)</td><td>1.9%</td><td>(37.3%)</td><td>(38.4%)</td><td>(0.7%)</td></tr><tr><td>H.B. Fuller</td><td>3.01</td><td>OW</td><td>49.5%</td><td>(14.4%)</td><td>(18.1%)</td><td>32.5%</td><td>11.5%</td><td>(20.8%)</td><td>20.9%</td><td>0.6%</td><td>56.1%</td><td>(11.6%)</td><td>13.7%</td><td>(17.1%)</td><td>(11.9%)</td><td>(6.0%)</td></tr><tr><td>Mosaic Company</td><td>6.84</td><td>UW</td><td>(16.5%)</td><td>(3.4%)</td><td>(39.6%)</td><td>6.3%</td><td>(12.5%)</td><td>13.8%</td><td>(25.9%)</td><td>6.3%</td><td>70.8%</td><td>11.7%</td><td>(18.6%)</td><td>(31.2%)</td><td>(2.0%)</td><td>(10.7%)</td></tr><tr><td>Albemarle Corp.</td><td>14.87</td><td>N</td><td>2.0%</td><td>(5.1%)</td><td>(6.9%)</td><td>53.7%</td><td>48.6%</td><td>(39.7%)</td><td>(5.2%)</td><td>102.0%</td><td>58.5%</td><td>(7.2%)</td><td>(33.4%)</td><td>(40.4%)</td><td>64.3%</td><td>(10.9%)</td></tr><tr><td>Avery Dennison</td><td>12.29</td><td>OW</td><td>43.7%</td><td>3.4%</td><td>20.8%</td><td>12.1%</td><td>63.6%</td><td>(21.8%)</td><td>45.6%</td><td>18.6%</td><td>39.6%</td><td>(16.4%)</td><td>11.7%</td><td>(7.4%)</td><td>(2.8%)</td><td>(11.6%)</td></tr><tr><td>FMC</td><td>1.36</td><td>N</td><td>26.6%</td><td>(22.8%)</td><td>(30.3%)</td><td>48.9%</td><td>66.0%</td><td>(23.5%)</td><td>52.5%</td><td>14.2%</td><td>(3.3%)</td><td>13.3%</td><td>(49.5%)</td><td>(22.9%)</td><td>(71.5%)</td><td>(21.3%)</td></tr><tr><td colspan="17"></td></tr><tr><td>S&amp;P 500</td><td></td><td></td><td>29.6%</td><td>11.4%</td><td>(0.7%)</td><td>9.5%</td><td>19.4%</td><td>(6.2%)</td><td>28.9%</td><td>16.3%</td><td>26.9%</td><td>(19.4%)</td><td>24.2%</td><td>23.3%</td><td>16.4%</td><td>10.7%</td></tr></table>

NOTE: Companies at or above the shaded line represent companies that outperformed the S&P 500. \*Bayer is co-covered with Richard Vosser. DuPont is covered by Chigusa Katoku. Source: Bloomberg Finance L.P. & JPM Estimates.

## Quarter-to-Date Performance

<table><tr><td>Ticker</td><td>6/30/26</td><td>7/10/26</td><td>% Change</td></tr><tr><td>CF</td><td>108.26</td><td>116.92</td><td>8.0%</td></tr><tr><td>LYB</td><td>52.65</td><td>56.35</td><td>7.0%</td></tr><tr><td>DOW</td><td>27.36</td><td>29.03</td><td>6.1%</td></tr><tr><td>MEOH</td><td>46.15</td><td>48.66</td><td>5.4%</td></tr><tr><td>HUN</td><td>10.62</td><td>11.13</td><td>4.8%</td></tr><tr><td>BAYN GR</td><td>€ 48.21</td><td>€ 50.50</td><td>4.8%</td></tr><tr><td>OLN</td><td>19.82</td><td>20.68</td><td>4.3%</td></tr><tr><td>NTR</td><td>62.95</td><td>65.43</td><td>3.9%</td></tr><tr><td>WLK</td><td>73.00</td><td>75.49</td><td>3.4%</td></tr><tr><td>APD</td><td>293.18</td><td>299.53</td><td>2.2%</td></tr><tr><td>LIN</td><td>518.94</td><td>529.79</td><td>2.1%</td></tr><tr><td>CE</td><td>46.00</td><td>46.92</td><td>2.0%</td></tr><tr><td>MOS</td><td>21.19</td><td>21.51</td><td>1.5%</td></tr><tr><td>ASH</td><td>65.89</td><td>66.75</td><td>1.3%</td></tr><tr><td>CTVA</td><td>84.69</td><td>85.68</td><td>1.2%</td></tr><tr><td>EMN</td><td>66.98</td><td>67.57</td><td>0.9%</td></tr><tr><td>CCK</td><td>111.82</td><td>111.47</td><td>(0.3%)</td></tr><tr><td>AMCR</td><td>43.35</td><td>43.18</td><td>(0.4%)</td></tr><tr><td>DD</td><td>135.64</td><td>134.68</td><td>(0.7%)</td></tr><tr><td>AVY</td><td>162.35</td><td>160.71</td><td>(1.0%)</td></tr><tr><td>BALL</td><td>62.40</td><td>61.69</td><td>(1.1%)</td></tr><tr><td>ECL</td><td>278.61</td><td>274.31</td><td>(1.5%)</td></tr><tr><td>IFF</td><td>79.22</td><td>77.53</td><td>(2.1%)</td></tr><tr><td>VVV</td><td>39.54</td><td>38.64</td><td>(2.3%)</td></tr><tr><td>TROX</td><td>6.30</td><td>6.14</td><td>(2.5%)</td></tr><tr><td>SHW</td><td>344.32</td><td>333.99</td><td>(3.0%)</td></tr><tr><td>SLGN</td><td>46.39</td><td>44.98</td><td>(3.0%)</td></tr><tr><td>PPG</td><td>121.29</td><td>116.76</td><td>(3.7%)</td></tr><tr><td>CBT</td><td>90.82</td><td>87.32</td><td>(3.9%)</td></tr><tr><td>SMG</td><td>68.11</td><td>65.48</td><td>(3.9%)</td></tr><tr><td>FUL</td><td>58.29</td><td>55.91</td><td>(4.1%)</td></tr><tr><td>CMP</td><td>31.13</td><td>29.84</td><td>(4.1%)</td></tr><tr><td>AXTA</td><td>34.22</td><td>32.51</td><td>(5.0%)</td></tr><tr><td>FMC</td><td>11.50</td><td>10.91</td><td>(5.1%)</td></tr><tr><td>RPM</td><td>111.15</td><td>105.10</td><td>(5.4%)</td></tr><tr><td>ALB</td><td>135.03</td><td>126.05</td><td>(6.7%)</td></tr><tr><td>CC</td><td>20.52</td><td>17.81</td><td>(13.2%)</td></tr><tr><td>OEC</td><td>6.63</td><td>5.69</td><td>(14.2%)</td></tr><tr><td>RIY</td><td>4093.86</td><td>4125</td><td>0.8%</td></tr><tr><td>RDG</td><td>2362.63</td><td>2299</td><td>(2.7%)</td></tr><tr><td>XLB</td><td>50.83</td><td>50.89</td><td>0.1%</td></tr><tr><td>SPX</td><td>7499.36</td><td>7575</td><td>1.0%</td></tr></table>

## Quarterly Stock Performance

<table><tr><td>Ticker</td><td>3/31/26</td><td>6/30/26</td><td>% Change</td><td>Ticker</td><td>12/31/25</td><td>3/31/26</td><td>% Change</td><td>Ticker</td><td>9/30/25</td><td>12/31/25</td><td>% Change</td><td>Ticker</td><td>6/30/25</td><td>9/30/25</td><td>% Change</td></tr><tr><td>CMP</td><td>23.35</td><td>31.13</td><td>33.3%</td><td>TROX</td><td>4.17</td><td>9.77</td><td>134.3%</td><td>ALB</td><td>81.08</td><td>141.44</td><td>74.4%</td><td>CC</td><td>11.45</td><td>15.84</td><td>38.3%</td></tr><tr><td>AXTA</td><td>27.70</td><td>34.22</td><td>23.5%</td><td>CC</td><td>11.79</td><td>22.03</td><td>86.9%</td><td>BAYN GR</td><td>€ 28.18</td><td>€ 37.01</td><td>31.3%</td><td>ALB</td><td>62.67</td><td>81.08</td><td>29.4%</td></tr><tr><td>BAYN GR</td><td>€ 39.74</td><td>€ 48.21</td><td>21.3%</td><td>LYB</td><td>43.30</td><td>80.56</td><td>86.1%</td><td>DD</td><td>32.58</td><td>40.20</td><td>23.4%</td><td>OLN</td><td>20.09</td><td>24.99</td><td>24.4%</td></tr><tr><td>CBT</td><td>75.31</td><td>90.82</td><td>20.6%</td><td>DOW</td><td>23.38</td><td>41.65</td><td>78.1%</td><td>ASH</td><td>47.91</td><td>58.67</td><td>22.5%</td><td>MEOH</td><td>33.10</td><td>39.76</td><td>20.1%</td></tr><tr><td>SLGN</td><td>38.80</td><td>46.39</td><td>19.6%</td><td>CF</td><td>77.34</td><td>129.84</td><td>67.9%</td><td>AXTA</td><td>28.62</td><td>32.31</td><td>12.9%</td><td>BAYN GR</td><td>€25.55</td>

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
