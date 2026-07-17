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
# China Economic Comment Another positive surprise in export to yield strong 1H26

## Another positive surprise in export growth

Export growth accelerated further to 27.0% y/y in June, exceeding both the previous month's 19.4% y/y and the consensus expectation of 19.0%. Our preliminary estimates suggest exports expanded by around 6.0% m/m in June after adjusting for seasonality and moving holiday effects, marking the fastest sequential gain in more than a year. Thus, exports expanded by around 8.0% q/q in 2Q26, slightly stronger than the pace recorded in 1Q26. Exports grew by 17.6% y/y in 1H26, substantially outperforming the 5.8% growth recorded in 2025. While price effects likely contributed meaningfully to the strength, volume estimates remain challenging given the growing dominance of technology products in driving growth.

## Shipments to the US contracted; the EU and BRI Economies offered the "delta"

Export volumes to the US continued to decline. However, a low base of comparison from last year amid reciprocal tariffs continued to generate double-digit y/y export growth to the US. Shipments to North Asia expanded further in June. Although the pace softened from an elevated base, the expansion trend remained intact, with North Asia continuing to be the largest contributor to overall export growth. In contrast, exports to ASEAN moderated, possibly reflecting easing supply-chain disruptions as improved energy availability reduced demand for related intermediate inputs. Meanwhile, exports to other major destinations, particularly the EU and BRI economies, recorded strong sequential rebounds following weakness in previous months.

## Non-Tech sectors provided the incremental push

Growth in the IT export basket moderated from an exceptional 76.0% y/y in May to a still historically elevated 72.4% y/y. Exports of integrated circuits surged 122% y/y, a pace rarely seen in recent history. Slower growth in mobile-phone and PC exports slightly weighed on overall performance. Nevertheless, on a sequential basis, shipment volumes of technology products continued to expand. Following a pause in 1Q26, automobile export volumes increased sequentially in every month of 2Q26, with another jump in June. This may reflect stronger demand for China's new-energy vehicles amid heightened uncertainty surrounding global energy prices. Consumer-goods exports grew by 4% y/y, marking an improvement after a prolonged period of contraction. Exports of furniture and home appliances accelerated significantly, possibly reflecting increased demand related to heatwaves experienced across several markets.

## IT goods imports surged further, crude oil import volume dropped to recent low

Import growth accelerated further to 36.0% y/y in June, up from 27.4% y/y in the previous month and well above the consensus expectation of 26.0%. Consequently, China's monthly trade surplus widened to over USD 125 billion. IT-related imports remained the primary driver of import growth. Imports of IT components accelerated to 68% y/y, led by strong growth in integrated circuit imports. Imports of automatic data-processing equipment (ADPs) surged 157% y/y, an unprecedented pace which points to a rapid increase in demand for AI data-center-related products. Growth in the value of commodity imports moderated during the month. Our estimates indicate that crude oil import volumes fell further to one of the lowest levels in recent history. In contrast, natural-gas import volumes improved. Given the improvements in shipping conditions through the Strait of Hormuz, the decline in crude oil imports likely reflects limited urgency to rebuild inventories, while other economies may have taken advantage of the ceasefire period to replenish their stockpiles. Meanwhile, import volumes of iron ore and copper ore showed signs of stabilization after several months of contraction.

## Economics

China

William Deng

Economist

william-w.deng@ubs.com

+852-2971 6765

Yu Song

Economist

S1460526010002

yu-za.song@ubs.com

+86-10-5832 8508

Grace Wang

Economist

S1460524050003

grace-zc.wang@ubs.com

+86-105-832 8335

Jennifer Zhong

Economist

S1460516050002

jennifer-a.zhong@ubs.com

+86-105-832 8324

## Strong external performance boosts confidence; the July Politburo Meeting remains a potential window for policy adjustments

June's robust export performance extended the streak of positive export surprises observed throughout 2026. Despite already being the largest exporter in the region, China achieved $17.6\%$ y/y export growth in 1H26, outperforming many of its EM Asia peers and, indeed, most economies globally.

Importantly, the drivers of export growth are increasingly shifting toward AI-related and other technology products, suggesting that China is becoming more deeply integrated into the more dynamic segments of the global supply chain. The continued expansion in automobile exports also indicates that China's new-energy vehicles are gaining market share amid ongoing uncertainty surrounding global energy supply conditions.

The strong headline growth, China's outperformance relative to peers, and the increasingly technology-intensive nature of its exports is likely to be viewed as supportive of the country's manufacturing competitiveness and production capabilities. That said, given the softness observed in domestic activity indicators during April and May, the upcoming Politburo meeting in late July remains an important potential window for policy adjustments aimed at supporting overall economic growth.

Figure 1: Export upswing has carried on with another sequential jump in monthly shipment revenue  
![](images/70340f02ce9996e51f70ecef3b509bf8de6adbe06112144bbfb833180e6fd297.jpg)  
Source: CEIC, UBS estimates

Figure 2: Export momentum (\%3m/3m, sa) picked up over June, leading to a strong 2Q  
![](images/94ee79c2153d7fc1e352f4695a968162f3dab9247edd26cea113a8904b069773.jpg)  
Source: CEIC, UBS estimates

Figure 3: Shipments to the US contracted, the rather low base yield strong y/y growth  
![](images/4b4c85dcad49d00a41abedd87560e1fd8c1f7ae50333aa69f4f8fd87917ce192.jpg)  
Source: CEIC, UBS estimates

Figure 4: Shipments to the EU and the BRI economies improved sequentially...  
![](images/6ccc85be464bb63322b0917d9248d9f4bba8950f52ef0d3e276a48d849fd4596.jpg)  
Source: CEIC, UBS estimates

Figure 5: ...while shipments to North Asia remained strong  
![](images/6dd35f207dc9d0c54bc083705155ff14c6aa475c66eeb4a67fffa18fcbb129ee.jpg)  
Source: CEIC, UBS estimates

Figure 6: Improvements in Non-Tech exports offered the incremental push  
![](images/599185e9d0a13e928ce8c61bd41292453cd4b02cd074a20f6ff50c89ef535b1a.jpg)  
Source: CEIC, UBS estimates

Figure 7: Tech and autos still dominate recent export growth  
![](images/3066ae0f1d03b48b56ef10043b654f75de477d40a7ba70a94e1aa98fb299b51d.jpg)  
Source: CEIC, UBS estimates

Figure 8: IT component import growth jumped further  
![](images/58fb9c33ef287daa23745a9fc7e345bca0864c03d886b81a90b8d061231bc398.jpg)  
Source: CEIC, UBS estimates

Figure 9: Natural gas import volumes improved, however, those of crude oil continued dropping sharply - the lowest of recent history  
![](images/f202e2bf34e91a2e0bb1c7105f4271bc0cf9b5df5b1c1761d234607285444b1c.jpg)  
Source: CEIC, UBS estimates

Figure 10: The weakening trend of iron and copper imports stabilized  
![](images/ed13a0a0e425db84f2b5a027baa271a4c23814f4f47ef65be05d47e3f547b9e6.jpg)  
Source: CEIC, UBS estimates

Figure 11: China's export growth by key product

<table><tr><td>Export growth by product (%y/y)</td><td>6/2025</td><td>7/2025</td><td>8/2025</td><td>9/2025</td><td>10/2025</td><td>11/2025</td><td>12/2025</td><td>1/2026</td><td>2/2026</td><td>3/2026</td><td>4/2026</td><td>5/2026</td><td>6/2026</td></tr><tr><td>Consumer Goods</td><td>-1.6</td><td>-2.8</td><td>-10.8</td><td>-11.1</td><td>-18.7</td><td>-12.8</td><td>-11.9</td><td>14.0</td><td>14.0</td><td>-30.1</td><td>-4.7</td><td>-2.0</td><td>4.0</td></tr><tr><td>Lamp</td><td>1.3</td><td>-5.3</td><td>-16.9</td><td>-17.0</td><td>-30.6</td><td>-22.0</td><td>-19.3</td><td>16.7</td><td>16.7</td><td>-44.1</td><td>-19.6</td><td>-12.0</td><td>-4.2</td></tr><tr><td>Suitcase</td><td>-7.1</td><td>-9.7</td><td>-15.5</td><td>-11.5</td><td>-25.9</td><td>-19.5</td><td>-13.5</td><td>18.4</td><td>18.4</td><td>-34.5</td><td>-11.3</td><td>-4.9</td><td>1.6</td></tr><tr><td>Footwear</td><td>-4.1</td><td>-7.8</td><td>-16.8</td><td>-13.7</td><td>-20.5</td><td>-17.7</td><td>-16.7</td><td>6.1</td><td>6.1</td><td>-39.5</td><td>-17.0</td><td>-10.3</td><td>-1.4</td></tr><tr><td>Clothing</td><td>1.0</td><td>-0.8</td><td>-9.7</td><td>-8.6</td><td>-15.6</td><td>-10.5</td><td>-10.8</td><td>14.8</td><td>14.8</td><td>-29.4</td><td>-2.3</td><td>-3.9</td><td>2.7</td></tr><tr><td>Toy</td><td>8.3</td><td>-3.3</td><td>-20.6</td><td>-27.9</td><td>-31.1</td><td>-25.9</td><td>-19.3</td><td>1.5</td><td>1.5</td><td>-41.9</td><td>-12.2</td><td>-7.2</td><td>-6.3</td></tr><tr><td>Furniture</td><td>0.2</td><td>3.4</td><td>-2.8</td><td>0.0</td><td>-12.9</td><td>-8.7</td><td>-7.8</td><td>24.7</td><td>24.7</td><td>-33.4</td><td>-3.8</td><td>1.7</td><td>9.0</td></tr><tr><td>Home appliance</td><td>-8.9</td><td>-3.8</td><td>-6.3</td><td>-10.0</td><td>-13.9</td><td>-5.7</td><td>-7.2</td><td>11.4</td><td>11.4</td><td>-15.3</td><td>7.2</td><td>9.5</td><td>15.3</td></tr><tr><td>IT</td><td>6.2</td><td>0.6</td><td>6.2</td><td>9.0</td><td>-1.9</td><td>3.4</td><td>19.8</td><td>30.6</td><td>30.6</td><td>44.8</td><td>56.8</td><td>75.6</td><td>72.4</td></tr><tr><td>Computers</td><td>-2.1</td><td>-9.3</td><td>-3.0</td><td>-1.2</td><td>-9.9</td><td>-6.6</td><td>4.6</td><td>20.6</td><td>20.6</td><td>37.3</td><td>46.8</td><td>65.9</td><td>53.0</td></tr><tr><td>LCD panel</td><td>8.4</td><td>1.7</td><td>13.8</td><td>16.2</td><td>12.9</td><td>16.6</td><td>16.5</td><td>23.3</td><td>23.3</td><td>2.2</td><td>-3.4</td><td>-5.0</td><td>9.4</td></tr><tr><td>Electronic ICs</td><td>25.3</td><td>29.3</td><td>32.9</td><td>31.9</td><td>27.3</td><td>34.2</td><td>47.2</td><td>72.6</td><td>72.6</td><td>85.3</td><td>100.0</td><td>111.1</td><td>122.1</td></tr><tr><td>Mobile phones</td><td>-8.5</td><td>-21.8</td><td>-19.1</td><td>-1.7</td><td>-16.6</td><td>-12.5</td><td>10.0</td><td>-8.3</td><td>-8.3</td><td>2.5</td><td>11.2</td><td>43.5</td><td>27.5</td></tr><tr><td>Auto and Auto Parts</td><td>12.2</td><td>12.0</td><td>11.9</td><td>8.7</td><td>15.4</td><td>29.1</td><td>37.8</td><td>41.9</td><td>41.9</td><td>17.7</td><td>28.3</td><td>25.2</td><td>47.9</td></tr><tr><td>Auto</td><td>23.7</td><td>17.9</td><td>17.4</td><td>10.8</td><td>34.9</td><td>52.3</td><td>72.1</td><td>67.1</td><td>67.1</td><td>44.0</td><td>44.0</td><td>39.0</td><td>69.9</td></tr><tr><td>Auto parts</td><td>-0.1</td><td>4.5</td><td>4.5</td><td>5.4</td><td>-11.2</td><td>1.9</td><td>-1.4</td><td>14.4</td><td>14.4</td><td>-12.4</td><td>6.6</td><td>5.2</td><td>19.1</td></tr><tr><td>EV</td><td>70.9</td><td>48.8</td><td>57.6</td><td>46.9</td><td>54.1</td><td>139.8</td><td>154.9</td><td>76.2</td><td>120.0</td><td>69.0</td><td>57.0</td><td>55.9</td><td>#N/A</td></tr></table>

Source: CEIC, UBS estimates

Figure 12: China's import growth by key product

<table><tr><td>Import growth by product (%y/y)</td><td>6/2025</td><td>7/2025</td><td>8/2025</td><td>9/2025</td><td>10/2025</td><td>11/2025</td><td>12/2025</td><td>1/2026</td><td>2/2026</td><td>3/2026</td><td>4/2026</td><td>5/2026</td><td>6/2026</td></tr><tr><td>Commodities</td><td>-9.1</td><td>-4.0</td><td>-9.6</td><td>-1.7</td><td>0.8</td><td>-0.8</td><td>6.5</td><td>3.0</td><td>3.0</td><td>8.2</td><td>13.1</td><td>14.3</td><td>12.3</td></tr><tr><td>Iron Ore &amp; Concentrate</td><td>-4.6</td><td>-9.9</td><td>-3.4</td><td>14.6</td><td>15.3</td><td>13.7</td><td>11.9</td><td>10.7</td><td>10.7</td><td>12.5</td><td>5.1</td><td>8.2</td><td>21.3</td></tr><tr><td>Copper Ore &amp; Concentrate</td><td>21.9</td><td>37.8</td><td>19.4</td><td>28.2</td><td>31.4</td><td>41.0</td><td>38.7</td><td>37.2</td><td>37.2</td><td>62.6</td><td>16.7</td><td>35.9</td><td>37.3</td></tr><tr><td>Coal</td><td>-44.6</td><td>-48.3</td><td>-36.1</td><td>-27.7</td><td>-27.8</td><td>-34.4</td><td>-0.8</td><td>-10.4</td><td>-10.4</td><td>4.0</td><td>-5.6</td><td>11.1</td><td>62.1</td></tr><tr><td>Crude Petroleum Oil</td><td>-14.9</td><td>-6.0</td><td>-15.0</td><td>-6.9</td><td>0.0</td><td>-6.8</td><td>4.0</td><td>-5.2</td><td>-5.2</td><td>-3.9</td><td>15.9</td><td>17.0</td><td>-6.9</td></tr><tr><td>Refined Petroleum Product</td><td>-4.9</td><td>5.1</td><td>-27.5</td><td>-16.5</td><td>-17.9</td><td>-3.4</td><td>-3.5</td><td>20.8</td><td>20.8</td><td>31.2</td><td>-16.3</td><td>-27.1</td><td>-29.4</td></tr><tr><td>Steel Product</td><td>-13.0</td><td>-8.3</td><td>-5.7</td><td>-0.2</td><td>-12.7</td><td>-1.5</td><td>-8.7</td><td>-16.4</td><td>-16.4</td><td>1.5</td><td>0.1</td><td>-11.4</td><td>3.5</td></tr><tr><td>Unwrought Copper and Copper Product</td><td>4.1</td><td>11.8</td><td>7.0</td><td>7.7</td><td>-5.5</td><td>-7.1</td><td>-5.5</td><td>12.2</td><td>12.2</td><td>20.4</td><td>39.6</td><td>44.9</td><td>44.9</td></tr><tr><td>Natural Gas</td><td>-6.5</td><td>-9.3</td><td>-9.1</td><td>-20.1</td><td>-22.4</td><td>-6.2</td><td>0.2</td><td>-12.7</td><td>-12.7</td><td>-21.8</td><td>-14.1</td><td>10.5</td><td>17.5</td></tr><tr><td>Soya Bean</td><td>-1.8</td><td>6.3</td><td>-8.8</td><td>1.0</td><td>12.0</td><td>7.8</td><td>3.3</td><td>-3.1</td><td>-3.1</td><td>20.6</td><td>51.8</td><td>-10.0</td><td>15.5</td></tr><tr><td>Machine Tool</td><td>3.9</td><td>5.0</td><td>4.5</td><td>1.7</td><td>-3.4</td><td>-11.7</td><td>4.1</td><td>-3.9</td><td>-3.9</td><td>-0.6</td><td>-11.9</td><td>-16.2</td><td>6.0</td></tr><tr><td>IT Components</td><td>10.1</td><td>11.8</td><td>6.8</td><td>13.3</td><td>9.8</td><td>13.0</td><td>14.6</td><td>37.5</td><td>37.5</td><td>50.0</td><td>50.8</td><td>62.5</td><td>67.6</td></tr><tr><td>Diode, Transistor &amp; Similar Semiconductor</td><td>8.0</td><td>-2.7</td><td>-0.2</td><td>8.1</td><td>6.1</td><td>6.7</td><td>3.6</td><td>17.1</td><td>17.1</td><td>10.7</td><td>9.7</td><td>5.2</td><td>16.4</td></tr><tr><td>Electronic Integrated Circuit</td><td>11.3</td><td>13.4</td><td>8.0</td><td>14.3</td><td>10.6</td><td>14.2</td><td>15.8</td><td>39.8</td><td>39.8</td><td>54.0</td><td>54.9</td><td>67.8</td><td>72.6</td></tr><tr><td>Liquid Crystal Display Panel</td><td>-19.2</td><td>-9.1</td><td>-16.0</td><td>-8.9</td><td>-11.9</td><td>-13.9</td><td>-6.4</td><td>-2.2</td><td>-2.2</td><td>0.3</td><td>-8.1</td><td>-8.9</td><td>-2.5</td></tr><tr><td>ADPs</td><td>10.5</td><td>-11.9</td><td>-9.0</td><td>-12.1</td><td>-26.9</td><td>6.5</td><td>18.2</td><td>68.7</td><td>68.7</td><td>30.0</td><td>91.3</td><td>80.7</td><td>157.4</td></tr></table>

Source: CEIC, UBS estimates

Valuation Method and Risk Statement N/A

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made 

[中间内容因长度限制已省略]

me by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) Unit 2901, Level 29 Altimus, Pandurang Budhkar Road, Worli, Mumbai – 400 018. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email : parameshwaran.s@ubs.com, Name of Grievance Officer Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company / companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch to professional institutional investors and/or persons permitted under applicable regulation. Unless permitted by applicable Taiwan laws and regulations, this material is for reference and information only and should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reprinted, reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.T

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
