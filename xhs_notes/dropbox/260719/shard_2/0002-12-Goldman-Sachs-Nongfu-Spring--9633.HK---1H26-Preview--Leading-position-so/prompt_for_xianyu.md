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
# Nongfu Spring (9633.HK): 1H26 Preview: Leading position solidified across categories with strong sugar-free tea; water recovery/new

We look for Rmb29.3bn in sales and Rmb8.9bn in reported net income in 1H26E, up 14%/17% yoy, mainly driven by Tea/Juice and mild NPM expansion to 30.4% (1H25: 29.7%). We expect 1H26 sales to mainly be driven by ongoing strong momentum tea (up 22% yoy on GSE, mainly driven by c.35%+ growth in Oriental Leaf) and Juice (up 18%)/functional drinks (up 12% yoy), while packaged water (up 6% yoy) was under more impact from unfavorable weathers/industry slowdown. That said, we believe the company has solidified its market position across all categories in 2026 YTD, while cost lock-in/inventory benefits, favorable product mix and operating leveraging contributed to drive steady margin expansion.

Tea- strong momentum from sugar-free tea: We expect c.35% yoy growth for Oriental Leaf, vs. 3% growth for Tea Pie in 1H26. The sugar-free tea, Oriental Leaf, continued to lead in growth with promotional campaigns and new flavor launches ie. New Season Longjing Tea. CT Brand data showed that sugar-free tea category recorded 16.1% yoy sales growth in 2Q26 for the offline channels they tracked (limited sample base) and significantly outperformed other categories' declines. We expect Oriental Leaf to continue the market share gain in 1H26.

Water- still lapping a low base but growth under the weather: Bottled water industry had encountered pressure especially in 2Q26 from unfavorable weather and likely consumer shift to other healthy drinks (incl. sugar-free drinks). CT Brand data showed that packaged water sales sector declined by $9\%$ in 2Q26 yoy for the offline channels they tracked. We expect Nongfu's water to grow $6\%$ yoy in 1H26 (vs. GSE of a SD% decline for CR Beverage's bottled water in 1H26) with still some gap vs. 1H23 level, while we noted a slower run-rate for Nongfu's water since April (see our monthly tracker).

■ Juice: We expect continued strong growth from 100% Juice and NFC Juice benefiting from increasing health awareness among consumers, together with the resilient flagship C100 SKU to drive an 18% sales growth for Juice in 1H26.

Functional drinks: we estimate roughly Rmb350mn sales in 1H26 from the successful launch of new electrolyte water since March, which helps to drive a $12\%$ sales growth in Functional drinks segment.

Going into 2H26, we expect the company to still aim for DD% sales growth with relentless efforts on category expansion/channel penetration amid weak macro, while margin level will still be dependent on the volatility of cost trend and

Leaf Liu  
+852-3966-4169 | leaf.liu@gs.com  
GS (Asia) L.L.C.

## Christina Liu

+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

investment level offsetting product mix upgrade/operating efficiency. The key swing factors among cost items in 2H26 will not only come from volatile PET cost, but also ingredients (some agriculture goods' prices trending up YTD, ie. Jasmine on unfavorable weather disruptions in Guangxi).

Earnings and TP changes: We now look for Rmb59.4bn/18.0bn sales/reported NP in 2026, up 13%/14% yoy, factoring Rmb7,500 PET/t price in 2H26E (up c.30% yoy in 2H26E). We lower our revenue/NP estimates by c.1\~2%/c.2\~3% in 2026-28E, mainly on lower functional drinks/water forecasts and increase in raw material cost. Our 12m TP is down from HK\$61.6 to HK\$59.9 on updated earnings forecast, with unchanged 30x target 2027E P/E discounted back to mid-2027. Nongfu is currently trading at 23x/20x 2026E/27E P/E vs. historical average level at c.30x, and remain as one of the fastest growing beverage player in our coverage. Reiterate Buy.

The authors would like to thank Lily Qi for her contribution to this report.

## Earnings Estimates Summary

Exhibit 1: Summary Financials

<table><tr><td colspan="16">Nongfu SpringRMB mn</td></tr><tr><td>Key drivers</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>1H23</td><td>2H23</td><td>1H24</td><td>2H24</td><td>1H25</td><td>2H25</td><td>1H26E</td><td>2H26E</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Packaged drinking water products</td><td>18,263</td><td>20,262</td><td>15,952</td><td>18,709</td><td>19,877</td><td>21,152</td><td>22,495</td><td>10,442</td><td>9,820</td><td>8,531</td><td>7,421</td><td>9,443</td><td>9,267</td><td>10,037</td><td>9,840</td></tr><tr><td>Tea beverage products</td><td>6,906</td><td>12,659</td><td>16,745</td><td>21,596</td><td>25,464</td><td>29,377</td><td>33,490</td><td>5,286</td><td>7,372</td><td>8,430</td><td>8,315</td><td>10,089</td><td>11,508</td><td>12,308</td><td>13,156</td></tr><tr><td>Functional beverage products</td><td>3,838</td><td>4,902</td><td>4,932</td><td>5,762</td><td>6,651</td><td>7,426</td><td>8,177</td><td>2,458</td><td>2,444</td><td>2,550</td><td>2,382</td><td>2,898</td><td>2,864</td><td>3,246</td><td>3,405</td></tr><tr><td>Juice beverage products</td><td>2,879</td><td>3,534</td><td>4,085</td><td>5,176</td><td>5,952</td><td>6,815</td><td>7,633</td><td>1,686</td><td>1,848</td><td>2,114</td><td>1,971</td><td>2,564</td><td>2,612</td><td>3,026</td><td>2,927</td></tr><tr><td>Other products</td><td>1,354</td><td>1,311</td><td>1,182</td><td>1,309</td><td>1,427</td><td>1,555</td><td>1,664</td><td>591</td><td>720</td><td>548</td><td>634</td><td>629</td><td>680</td><td>692</td><td>735</td></tr><tr><td>Total</td><td>33,239</td><td>42,667</td><td>42,896</td><td>52,553</td><td>59,370</td><td>66,326</td><td>73,459</td><td>20,462</td><td>22,205</td><td>22,173</td><td>20,723</td><td>25,622</td><td>26,931</td><td>29,309</td><td>30,062</td></tr><tr><td>Revenue mix %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Packaged drinking water products</td><td>55%</td><td>47%</td><td>37%</td><td>36%</td><td>33%</td><td>32%</td><td>31%</td><td>51%</td><td>44%</td><td>38%</td><td>36%</td><td>37%</td><td>34%</td><td>34%</td><td>33%</td></tr><tr><td>Tea beverage products</td><td>21%</td><td>30%</td><td>39%</td><td>41%</td><td>43%</td><td>44%</td><td>46%</td><td>26%</td><td>33%</td><td>38%</td><td>40%</td><td>39%</td><td>43%</td><td>42%</td><td>44%</td></tr><tr><td>Functional beverage products</td><td>12%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>12%</td><td>11%</td><td>12%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td><td>11%</td></tr><tr><td>Juice beverage products</td><td>9%</td><td>8%</td><td>10%</td><td>10%</td><td>10%</td><td>10%</td><td>10%</td><td>8%</td><td>8%</td><td>10%</td><td>10%</td><td>10%</td><td>10%</td><td>10%</td><td>10%</td></tr><tr><td>Other products</td><td>4%</td><td>3%</td><td>3%</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td><td>3%</td><td>3%</td><td>2%</td><td>3%</td><td>2%</td><td>3%</td><td>2%</td><td>2%</td></tr><tr><td>YoY Growth (%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Packaged drinking water products</td><td>7.1%</td><td>10.9%</td><td>-21.3%</td><td>17.3%</td><td>6.2%</td><td>6.4%</td><td>6.3%</td><td>11.7%</td><td>10.2%</td><td>-18.3%</td><td>-24.4%</td><td>10.7%</td><td>24.9%</td><td>6.3%</td><td>6.2%</td></tr><tr><td>Tea beverage products</td><td>50.8%</td><td>83.3%</td><td>32.3%</td><td>29.0%</td><td>17.9%</td><td>15.4%</td><td>14.0%</td><td>59.9%</td><td>104.8%</td><td>59.5%</td><td>12.8%</td><td>19.7%</td><td>38.4%</td><td>22.0%</td><td>14.3%</td></tr><tr><td>Functional beverage products</td><td>3.9%</td><td>27.7%</td><td>0.6%</td><td>16.8%</td><td>15.4%</td><td>11.7%</td><td>10.1%</td><td>21.5%</td><td>34.7%</td><td>3.8%</td><td>-2.6%</td><td>13.6%</td><td>20.3%</td><td>12.0%</td><td>18.9%</td></tr><tr><td>Juice beverage products</td><td>10.1%</td><td>22.7%</td><td>15.6%</td><td>26.7%</td><td>15.0%</td><td>14.5%</td><td>12.0%</td><td>32.2%</td><td>15.2%</td><td>25.4%</td><td>6.7%</td><td>21.3%</td><td>32.5%</td><td>18.0%</td><td>12.1%</td></tr><tr><td>Other products</td><td>-22.6%</td><td>-3.2%</td><td>-9.8%</td><td>10.7%</td><td>9.0%</td><td>9.0%</td><td>7.0%</td><td>-8.4%</td><td>1.6%</td><td>-7.2%</td><td>-12.0%</td><td>14.8%</td><td>7.3%</td><td>10.0%</td><td>8.1%</td></tr><tr><td>Total</td><td>11.9%</td><td>28.4%</td><td>0.5%</td><td>22.5%</td><td>13.0%</td><td>11.7%</td><td>10.8%</td><td>23.3%</td><td>33.4%</td><td>8.4%</td><td>-6.7%</td><td>15.6%</td><td>30.0%</td><td>14.4%</td><td>11.6%</td></tr><tr><td>Operating profit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Packaged drinking water products</td><td>-2.0%</td><td>14.0%</td><td>-32.3%</td><td>40.9%</td><td>3.2%</td><td>2.2%</td><td>3.9%</td><td>4.3%</td><td>26.8%</td><td>-27.8%</td><td>-37.2%</td><td>22.0%</td><td>64.1%</td><td>8.3%</td><td>-1.5%</td></tr><tr><td>Tea beverage products</td><td>50.3%</td><td>104.2%</td><td>34.5%</td><td>37.2%</td><td>18.0%</td><td>17.2%</td><td>16.3%</td><td>56.6%</td><td>157.7%</td><td>63.1%</td><td>15.0%</td><td>31.2%</td><td>42.9%</td><td>23.6%</td><td>13.0%</td></tr><tr><td>Functional beverage products</td><td>-3.8%</td><td>34.8%</td><td>0.7%</td><td>29.5%</td><td>15.6%</td><td>12.4%</td><td>11.7%</td><td>16.1%</td><td>57.9%</td><td>6.5%</td><td>-4.6%</td><td>29.9%</td><td>29.1%</td><td>15.1%</td><td>16.2%</td></tr><tr><td>Juice beverage products</td><td>15.3%</td><td>63.0%</td><td>7.6%</td><td>74.7%</td><td>14.1%</td><td>17.8%</td><td>14.7%</td><td>51.5%</td><td>78.1%</td><td>0.4%</td><td>15.5%</td><td>60.8%</td><td>88.0%</td><td>28.1%</td><td>2.5%</td></tr><tr><td>Other products</td><td>24.2%</td><td>41.3%</td><td>-1.0%</td><td>19.7%</td><td>9.6%</td><td>10.8%</td><td>8.7%</td><td>93.5%</td><td>19.8%</td><td>0.1%</td><td>-1.8%</td><td>44.2%</td><td>3.1%</td><td>11.0%</td><td>8.2%</td></tr><tr><td>Margin</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>OP margin</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Packaged drinking water products</td><td>35.3%</td><td>36.3%</td><td>31.2%</td><td>37.4%</td><td>36.3%</td><td>34.9%</td><td>34.1%</td><td>36.4%</td><td>36.1%</td><td>32.2%</td><td>30.0%</td><td>35.4%</td><td>39.4%</td><td>36.1%</td><td>36.6%</td></tr><tr><td>Tea beverage products</td><td>39.9%</td><td>44.4%</td><td>45.2%</td><td>48.0%</td><td>48.1%</td><td>48.8%</td><td>49.8%</td><td>43.1%</td><td>45.3%</td><td>44.1%</td><td>46.2%</td><td>48.4%</td><td>47.8%</td><td>49.0%</td><td>47.2%</td></tr><tr><td>Functional beverage products</td><td>40.0%</td><td>42.2%</td><td>42.2%</td><td>46.8%</td><td>46.9%</td><td>47.2%</td><td>47.9%</td><td>40.1%</td><td>44.3%</td><td>41.2%</td><td>43.3%</td><td>47.1%</td><td>46.5%</td><td>48.4%</td><td>45.4%</td></tr><tr><td>Juice beverage products</td><td>20.1%</td><td>26.8%</td><td>24.9%</td><td>34.3%</td><td>34.1%</td><td>35.0%</td><td>35.9%</td><td>29.5%</td><td>24.3%</td><td>23.6%</td><td>26.3%</td><td>31.3%</td><td>37.3%</td><td>34.0%</td><td>34.1%</td></tr><tr><td>Other products</td><td>20.7%</td><td>30.2%</td><td>33.2%</td><td>35.9%</td><td>36.1%</td><td>36.7%</td><td>37.3%</td><td>26.8%</td><td>33.0%</td><td>28.9%</td><td>36.8%</td><td>36.4%</td><td>35.4%</td><td>36.7%</td><td>35.5%</td></tr><tr><td>Consolidated P&amp;L</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>1H23</td><td>2H23</td><td>1H24</td><td>2H24</td><td>1H25</td><td>2H25</td><td>1H26E</td><td>2H26E</td></tr><tr><td>Total Sales</td><td>33,239</td><td>42,667</td><td>42,896</td><td>52,553</td><td>59,370</td><td>66,326</td><td>73,459</td><td>20,462</td><td>22,205</td><td>22,173</td><td>20,723</td><td>25,622</td><td>26,931</td><td>29,309</td><td>29,062</td></tr><tr><td>COGS</td><td>-14,144</td><td>-17,260</td><td>-17,980</td><td>-20,745</td><td>-23,342</td><td>-25,944</td><td>-28,293</td><td>-8,152</td><td>-9,108</td><td>-9,141</td><td>-8,840</td><td>-10,166</td><td>-10,579</td><td>-11,254</td><td>-12,087</td></tr><tr><td>Gross Profit</td><td>19,095</td><td>25,407</td><td>24,916</td><td>31,808</td><td>36,029</td><td>40,382</td><td>45,167</td><td>12,310</td><td>13,097</td><td>13,032</td><td>11,883</td><td>15,456</td><td>16,352</td><td>18,054</td><td>17,975</td></tr><tr><td>SG&amp;A</td><td>-9,656</td><td>-11,446</td><td>-11,136</td><td>-12,253</td><td>-13,532</td><td>-14,997</td><td>-16,442</td><td>-5,654</td><td>-5,793</td><td>-5,885</td><td>-5,251</td><td>-6,078</td><td>-6,174</td><td>-7,063</td><td>-6,469</td></tr><tr><td>Selling and distribution expense</td><td>-7,821</td><td>-9,284</td><td>-9,173</td><td>-9,800</td><td>-10,870</td><td>-12,092</td><td>-13,295</td><td>-4,695</td><td>-4,589</td><td>-4,971</td><td>-4,202</td><td>-5,011</td><td>-4,790</td><td>-5,862</td><td>-5,008</td></tr><tr><td>Administrative expenses</td><td>-1,835</td><td>-2,162</td><td>-1,962</td><td>-2,452</td><td>-2,662</td><td>-2,906</td><td>-3,147</td><td>-959</td><td>-1,204</td><td>-913</td><td>-1,049</td><td>-1,068</td><td>-1,384</td><td>-1,202</td><td>-1,460</td></tr><tr><td>Other operating income/(expense)</td><td>1,063</td><td>836</td><td>1,233</td><td>849</td><td>814</td><td>804</td><td>757</td><td>459</td><td>378</td><td>490</td><td>743</td><td>374</td><td>476</td><td>402</td><td>412</td></tr><tr><td>EBIT</td><td>10,503</td><td>14,797</td><td>15,013</td><td>20,405</td><td>23,311</td><td>26,188</td><td>29,482</td><td>7,115</td><td>7,682</td><td>7,638</td><td>7,375</td><td>9,752</td><td>10,653</td><td>11,393</td><td>11,918</td></tr><tr><td>Depreciation</td><td>-2,478</td><td>-2,620</td><td>-2,863</td><td>-3,374</td><td>-3,810</td><td>-4,251</td><td>-4,712</td><td>-1,234</td><td>-1,386</td><td>-1,310</td><td>-1,553</td><td>-1,555</td><td>-1,818</td><td>-1,905</td><td>-1,905</td></tr><tr><td>Amortization</td><td>-9</td><td>-11</td><td>11</td><td>19</td><td>21</td><td>24</td><td>26</td><td>-6</td><td>-5</td><td>-6</td><td>17</td><td>-6</td><td>25</td><td>11</td><td>11</td></tr><tr><td>EBITDA</td><td>12,990</td><td>17,428</td><td>17,865</td><td>23,759</td><td>27,099</td><td>30,416</td><td>34,168</td><td>8,354</td><td>9,074</td><td>8,954</td><td>8,912</td><td>11,313</td><td>12,446</td><td>13,287</td><td>13,812</td></tr><tr><td>Net finance costs</td><td>547</td><td>892</td><td>775</td><td>513</td><td>474</td><td>618</td><td>796</td><td>410</td><td>482</td><td>504</td><td>270</td><td>282</td><td>231</td><td>237</td><td>237</td></tr><tr><td>Other non-op rev/ (exp)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pretax income</td><td>11,050</td><td>15,688</td><td>15,788</td><td>20,918</td><td>23,785</td><td>26,807</td><td>30,278</td><td>7,524</td><td>8,164</td><td>8,142</td><td>7,646</td><td>10,034</td><td>10,884</td><td>11,630</td><td>12,155</td></tr><tr><td>Provisions for taxes</td><td>-2,555</td><td>-3,609</td><td>-3,665</td><td>-5,049</td><td>-5,741</td><td>-6,471</td><td>-7,309</td><td>-1,749</td><td>-1,860</td><td>-1,903</td><td>-1,762</td><td>-2,411</td><td>-2,638</td><td>-2,733</td><td>-3,008</td></tr><tr><td>Minority interest (I/S i

[中间内容因长度限制已省略]

es, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
