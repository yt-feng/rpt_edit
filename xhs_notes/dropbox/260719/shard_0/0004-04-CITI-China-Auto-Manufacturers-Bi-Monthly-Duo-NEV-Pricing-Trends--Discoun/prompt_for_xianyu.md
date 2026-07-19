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
# China Auto Manufacturers

## Bi-Monthly Duo NEV Pricing Trends (Discount & MSRP): Mid-Jul-26

## CITI'S TAKE

In this bi-monthly pricing trend report, we monitor the NEV-PV pricing of major OEMs based on data from Top 30 cities collected by Thinkercar. Discount is calculated as the difference between 4S shop retail price and the MSRP. In the first half of Jul-26, China NEV-PV sector weighted average retail discount was +0.1ppt MoM to 5.9% (versus end-Jun). NEV-PV sector weighted average MSRP was +0.1% MoM to Rmb183,863.

## NEV brands

— Tesla: retail discount stands at 0.6% (+0.0ppt MoM); MSRP at Rmb293,628 (flat MoM)

— Nio: retail discount stands at 1.6% (+0.1ppt MoM); MSRP at Rmb353,562 (flat MoM)

— Xpeng: retail discount stands at 3.6% (+0.1ppt MoM); MSRP at Rmb196,720 (flat MoM)

— Li Auto: retail discount stands at 4.1% (-0.6ppt MoM); MSRP at Rmb315,595 (+0.7% MoM)

— AITO: retail discount 2.7% (+1.1ppt MoM); MSRP Rmb372,634 (flat MoM)

— Leapmotor: retail discount stands at 4.3% (+0.0ppt MoM); MSRP at Rmb123,966 (+1.0% MoM)

## Traditional local brands (for NEV models only)

— BYD: retail discount stands at 6.9% (+0.2ppt MoM); MSRP at Rmb133,685 (-0.3% MoM)

— Geely: retail discount stands at 10.5% (+0.4ppt MoM); MSRP at Rmb117,312 (+0.1% MoM)

— Great Wall: retail discount stands at 5.3% (+0.0ppt MoM); MSRP at Rmb265,827 (flat MoM)

## Traditional luxury brands

— Beijing Mercedes: NEV+ICE weighted-average retail price at Rmb297,069 (-1.2% MoM/-8.4% YoY)

— Brilliance BMW: NEV+ICE weighted-average retail price at Rmb289,639 (-1.3% MoM/-7.1% YoY)

— Audi Group: NEV+ICE weighted-average retail price at Rmb238,369 (-0.6% MoM/-8.9% YoY)

## See Figure 6-11 for CPCA discount summary

## Jeff Chung $^{AC}$

+852-2501-2787

jeff.m.chung@citi.com

## Kyle Wu

+852-2501-8483

kyle.wu@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations.

<table><tr><td></td><td>28-Feb-26</td><td>15-Mar-26</td><td>31-Mar-26</td><td>15-Apr-26</td><td>30-Apr-26</td><td>15-May-26</td><td>31-May-26</td><td>15-Jun-26</td><td>30-Jun-26</td><td>15-Jul-26</td></tr><tr><td colspan="11">Weighted average retail discount</td></tr><tr><td>Tesla</td><td>0.8%</td><td>0.7%</td><td>0.7%</td><td>0.3%</td><td>0.3%</td><td>0.9%</td><td>0.9%</td><td>0.6%</td><td>0.6%</td><td>0.6%</td></tr><tr><td>Nio</td><td>1.9%</td><td>3.3%</td><td>3.3%</td><td>2.8%</td><td>2.8%</td><td>2.5%</td><td>2.5%</td><td>2.1%</td><td>1.5%</td><td>1.6%</td></tr><tr><td>Xpeng</td><td>6.4%</td><td>6.8%</td><td>6.7%</td><td>3.9%</td><td>4.4%</td><td>4.4%</td><td>3.6%</td><td>3.6%</td><td>3.6%</td><td>3.6%</td></tr><tr><td>Li Auto</td><td>5.3%</td><td>6.6%</td><td>6.6%</td><td>6.4%</td><td>6.4%</td><td>6.5%</td><td>6.1%</td><td>4.6%</td><td>4.6%</td><td>4.1%</td></tr><tr><td>AITO</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.6%</td><td>1.6%</td><td>2.7%</td></tr><tr><td>Leapmotor</td><td>9.2%</td><td>9.2%</td><td>9.2%</td><td>7.9%</td><td>7.9%</td><td>6.0%</td><td>6.3%</td><td>5.9%</td><td>4.3%</td><td>4.3%</td></tr><tr><td>BYD</td><td>7.5%</td><td>8.3%</td><td>8.6%</td><td>8.2%</td><td>7.8%</td><td>6.8%</td><td>6.9%</td><td>6.6%</td><td>6.7%</td><td>6.9%</td></tr><tr><td>Geely</td><td>10.2%</td><td>11.3%</td><td>11.7%</td><td>12.4%</td><td>12.6%</td><td>12.3%</td><td>12.5%</td><td>9.9%</td><td>10.1%</td><td>10.5%</td></tr><tr><td>Great Wall</td><td>4.4%</td><td>4.4%</td><td>4.5%</td><td>7.3%</td><td>7.2%</td><td>5.8%</td><td>5.9%</td><td>5.3%</td><td>5.3%</td><td>5.3%</td></tr><tr><td>Beijing Mercedes</td><td>31.2%</td><td>31.1%</td><td>31.2%</td><td>35.3%</td><td>35.7%</td><td>28.0%</td><td>28.1%</td><td>33.5%</td><td>33.5%</td><td>33.5%</td></tr><tr><td>Brilliance BMW</td><td>38.3%</td><td>37.5%</td><td>37.6%</td><td>33.2%</td><td>33.5%</td><td>33.1%</td><td>33.2%</td><td>32.5%</td><td>32.8%</td><td>33.4%</td></tr><tr><td>Audi Group</td><td>19.2%</td><td>14.9%</td><td>14.9%</td><td>19.4%</td><td>16.5%</td><td>13.4%</td><td>13.5%</td><td>12.2%</td><td>15.8%</td><td>15.9%</td></tr><tr><td>NEV-PV sector weighted average discount</td><td>6.3%</td><td>7.4%</td><td>7.6%</td><td>7.8%</td><td>7.7%</td><td>6.7%</td><td>6.8%</td><td>5.9%</td><td>5.7%</td><td>5.9%</td></tr><tr><td colspan="11">Weighted average retail discount MoM change</td></tr><tr><td>Tesla</td><td>0.5ppt</td><td>-0.1ppt</td><td>-0.1ppt</td><td>-0.4ppt</td><td>-0.4ppt</td><td>0.6ppt</td><td>0.6ppt</td><td>-0.3ppt</td><td>-0.3ppt</td><td>0.0ppt</td></tr><tr><td>Nio</td><td>0.4ppt</td><td>1.4ppt</td><td>1.4ppt</td><td>-0.5ppt</td><td>-0.5ppt</td><td>-0.3ppt</td><td>-0.3ppt</td><td>-0.4ppt</td><td>-1.0ppt</td><td>0.1ppt</td></tr><tr><td>Xpeng</td><td>3.1ppt</td><td>0.3ppt</td><td>0.3ppt</td><td>-2.8ppt</td><td>-2.4ppt</td><td>0.0ppt</td><td>-0.8ppt</td><td>0.0ppt</td><td>0.0ppt</td><td>0.1ppt</td></tr><tr><td>Li Auto</td><td>-0.1ppt</td><td>1.3ppt</td><td>1.3ppt</td><td>-0.1ppt</td><td>-0.1ppt</td><td>0.1ppt</td><td>-0.3ppt</td><td>-1.5ppt</td><td>-1.5ppt</td><td>-0.6ppt</td></tr><tr><td>AITO</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.1ppt</td></tr><tr><td>Leapmotor</td><td>1.8ppt</td><td>0.0ppt</td><td>0.0ppt</td><td>-1.4ppt</td><td>-1.3ppt</td><td>-2.0ppt</td><td>-1.7ppt</td><td>-0.3ppt</td><td>-2.0ppt</td><td>0.0ppt</td></tr><tr><td>BYD</td><td>0.9ppt</td><td>0.8ppt</td><td>1.1ppt</td><td>-0.4ppt</td><td>-0.9ppt</td><td>-1.0ppt</td><td>-0.9ppt</td><td>-0.3ppt</td><td>-0.1ppt</td><td>0.2ppt</td></tr><tr><td>Geely</td><td>0.5ppt</td><td>1.1ppt</td><td>1.5ppt</td><td>0.7ppt</td><td>0.9ppt</td><td>-0.3ppt</td><td>-0.1ppt</td><td>-2.6ppt</td><td>-2.4ppt</td><td>0.4ppt</td></tr><tr><td>Great Wall</td><td>0.3ppt</td><td>0.0ppt</td><td>0.1ppt</td><td>2.8ppt</td><td>2.7ppt</td><td>-1.4ppt</td><td>-1.3ppt</td><td>-0.6ppt</td><td>-0.5ppt</td><td>0.0ppt</td></tr><tr><td>Beijing Mercedes</td><td>1.7ppt</td><td>-0.1ppt</td><td>0.0ppt</td><td>4.1ppt</td><td>4.5ppt</td><td>-7.7ppt</td><td>-7.6ppt</td><td>5.4ppt</td><td>5.4ppt</td><td>0.0ppt</td></tr><tr><td>Brilliance BMW</td><td>-1.0ppt</td><td>-0.8ppt</td><td>-0.7ppt</td><td>-4.4ppt</td><td>-4.1ppt</td><td>-0.3ppt</td><td>-0.3ppt</td><td>-0.7ppt</td><td>-0.4ppt</td><td>0.5ppt</td></tr><tr><td>Audi Group</td><td>3.5ppt</td><td>-4.3ppt</td><td>-4.2ppt</td><td>4.5ppt</td><td>1.6ppt</td><td>-3.1ppt</td><td>-3.0ppt</td><td>-1.3ppt</td><td>2.3ppt</td><td>0.1ppt</td></tr><tr><td>Changes in sector weighted average discount</td><td>0.3ppt</td><td>1.1ppt</td><td>1.3ppt</td><td>0.2ppt</td><td>0.1ppt</td><td>-0.9ppt</td><td>-0.9ppt</td><td>-0.8ppt</td><td>-1.0ppt</td><td>0.1ppt</td></tr></table>

Source: Citi, Thinkercar

Figure 1. NEV-PV retail discounts by OEMs

© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 2. Sector weighted average NEV-PV discount vs MSRP  
![](images/28d0866324c9c9619e5c9b78f9ffe7bf90c53d070999f82633455f676567959e.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 3. NEV-PV retail MSRP by OEMs

<table><tr><td></td><td>28-Feb-26</td><td>15-Mar-26</td><td>31-Mar-26</td><td>15-Apr-26</td><td>30-Apr-26</td><td>15-May-26</td><td>31-May-26</td><td>15-Jun-26</td><td>30-Jun-26</td><td>15-Jul-26</td></tr><tr><td colspan="11">Weighted average MSRP</td></tr><tr><td>Tesla</td><td>295,288</td><td>293,475</td><td>293,475</td><td>294,716</td><td>294,716</td><td>289,540</td><td>289,540</td><td>293,628</td><td>293,628</td><td>293,628</td></tr><tr><td>Nio</td><td>345,919</td><td>330,031</td><td>330,031</td><td>317,320</td><td>320,799</td><td>313,047</td><td>313,047</td><td>354,313</td><td>353,577</td><td>353,562</td></tr><tr><td>Xpeng</td><td>191,933</td><td>187,516</td><td>186,612</td><td>178,019</td><td>178,019</td><td>164,596</td><td>178,334</td><td>196,720</td><td>196,720</td><td>196,720</td></tr><tr><td>Li Auto</td><td>282,728</td><td>282,677</td><td>282,677</td><td>282,865</td><td>282,865</td><td>288,739</td><td>291,513</td><td>313,356</td><td>313,356</td><td>315,595</td></tr><tr><td>AITO</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>378,726</td><td>372,634</td><td>372,634</td></tr><tr><td>Leapmotor</td><td>130,589</td><td>129,277</td><td>129,277</td><td>118,784</td><td>123,975</td><td>122,852</td><td>122,852</td><td>123,081</td><td>122,761</td><td>123,966</td></tr><tr><td>BYD</td><td>137,757</td><td>128,236</td><td>128,083</td><td>131,935</td><td>132,570</td><td>131,481</td><td>131,975</td><td>130,806</td><td>134,060</td><td>133,685</td></tr><tr><td>Geely</td><td>125,921</td><td>110,174</td><td>110,240</td><td>106,513</td><td>107,090</td><td>111,118</td><td>112,890</td><td>115,722</td><td>117,163</td><td>117,312</td></tr><tr><td>Great Wall</td><td>267,758</td><td>258,235</td><td>258,235</td><td>231,473</td><td>255,107</td><td>225,924</td><td>267,995</td><td>266,532</td><td>265,827</td><td>265,827</td></tr><tr><td>Beijing Mercedes</td><td>454,328</td><td>422,375</td><td>422,375</td><td>420,636</td><td>418,376</td><td>375,874</td><td>375,874</td><td>390,627</td><td>390,627</td><td>390,627</td></tr><tr><td>Brilliance BMW</td><td>320,878</td><td>321,588</td><td>321,588</td><td>301,729</td><td>301,729</td><td>297,410</td><td>297,410</td><td>297,949</td><td>297,949</td><td>297,949</td></tr><tr><td>Audi Group</td><td>290,536</td><td>286,218</td><td>286,218</td><td>324,674</td><td>317,034</td><td>327,624</td><td>327,624</td><td>336,221</td><td>336,221</td><td>336,221</td></tr><tr><td>NEV-PV sector weighted average MSRP</td><td>205,131</td><td>185,580</td><td>185,490</td><td>171,642</td><td>173,654</td><td>173,515</td><td>176,911</td><td>182,459</td><td>183,755</td><td>183,863</td></tr><tr><td colspan="11">Weighted average MSRP MoM change</td></tr><tr><td>Tesla</td><td>1.8%</td><td>-0.6%</td><td>-0.6%</td><td>0.4%</td><td>0.4%</td><td>-1.8%</td><td>-1.8%</td><td>1.4%</td><td>1.4%</td><td>0.0%</td></tr><tr><td>Nio</td><td>-2.3%</td><td>-4.6%</td><td>-4.6%</td><td>-3.9%</td><td>-2.8%</td><td>-2.4%</td><td>-2.4%</td><td>13.2%</td><td>12.9%</td><td>0.0%</td></tr><tr><td>Xpeng</td><td>-7.9%</td><td>-2.3%</td><td>-2.8%</td><td>-4.6%</td><td>-4.6%</td><td>-7.5%</td><td>0.2%</td><td>10.3%</td><td>10.3%</td><td>0.0%</td></tr><tr><td>Li Auto</td><td>-0.1%</td><td>0.0%</td><td>0.0%</td><td>0.1%</td><td>0.1%</td><td>2.1%</td><td>3.1%</td><td>7.5%</td><td>7.5%</td><td>0.7%</td></tr><tr><td>AITO</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.0%</td></tr><tr><td>Leapmotor</td><td>1.3%</td><td>-1.0%</td><td>-1.0%</td><td>-8.1%</td><td>-4.1%</td><td>-0.9%</td><td>-0.9%</td><td>0.2%</td><td>-0.1%</td><td>1.0%</td></tr><tr><td>BYD</td><td>-3.9%</td><td>-6.9%</td><td>-7.0%</td><td>3.0%</td><td>3.5%</td><td>-0.8%</td><td>-0.4%</td><td>-0.9%</td><td>1.6%</td><td>-0.3%</td></tr><tr><td>Geely</td><td>1.1%</td><td>-12.5%</td><td>-12.5%</td><td>-3.4%</td><td>-2.9%</td><td>3.8%</td><td>5.4%</td><td>2.5%</td><td>3.8%</td><td>0.1%</td></tr><tr><td>Great Wall</td><td>0.9%</td><td>-3.6%</td><td>-3.6%</td><td>-10.4%</td><td>-1.2%</td><td>-11.4%</td><td>5.1%</td><td>-0.5%</td><td>-0.8%</td><td>0.0%</td></tr><tr><td>Beijing Mercedes</td><td>-0.3%</td><td>-7.0%</td><td>-7.0%</td><td>-0.4%</td><td>-0.9%</td><td>-10.2%</td><td>-10.2%</td><td>3.9%</td><td>3.9%</td><td>0.0%</td></tr><tr><td>Brilliance BMW</td><td>-6.7%</td><td>0.2%</td><td>0.2%</td><td>-6.2%</td><td>-6.2%</td><td>-1.4%</td><td>-1.4%</td><td>0.2%</td><td>0.2%</td><td>0.0%</td></tr><tr><td>Audi Group</td><td>-13.6%</td><td>-1.5%</td><td>-1.5%</td><td>13.4%</td><td>10.8%</td><td>3.3%</td><td>3.3%</td><td>2.6%</td><td>2.6%</td><td>0.0%</td></tr><tr><td>Changes in sector weighted average MSRP</td><td>1.9%</td><td>-9.5%</td><td>-9.6%</td><td>-7.5%</td><td>-6.4%</td><td>-0.1%</td><td>1.9%</td><td>3.1%</td><td>3.9%</td><td>0.1%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 4. German luxury ICE discount summary

<table><tr><td></td><td>15-Jul-26</td><td>30-Jun-26</td><td>Jul-26 MoM</td><td>15-Jul-25</td><td>Jul-26 YoY</td><td>30-Jun-25</td><td>Jul-25 MoM</td></tr><tr><td>German Luxury ICE (weighted avg)</td><td>27.0%</td><td>27.2%</td><td>-0.2ppt</td><td>29.0%</td><td>-2.0ppt</td><td>34.0%</td><td>-5.0ppt</td></tr><tr><td colspan="8">By brand</td></tr><tr><td>Brilliance BMW</td><td>22.9%</td><td>23.2%</td><td>-0.3ppt</td><td>28.7%</td><td>-5.8ppt</td><td>34.6%</td><td>-6.0ppt</td></tr><tr><td>Beijing Mercedes</td><td>24.6%</td><td>24.8%</td><td>-0.2ppt</td><td>25.1%</td><td>-0.5ppt</td><td>31.6%</td><td>-6.5ppt</td></tr><tr><td>Audi Group</td><td>33.1%</td><td>33.2%</td><td>-0.1ppt</td><td>32.4%</td><td>0.7ppt</td><td>35.5%</td><td>-3.1ppt</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 5. German luxury ICE discount summary  
![](images/474a4792c28362eeb5dcab0e3e9b689691967e69b301d98a2e60ad4fe9b6cc58.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 6. CPCA: Monthly Number of Car Model Adopted Price Cut  
![](images/5acdb8648207959782e3de3f5b51329e632652371b9622e18d42df96d17fc13e.jpg)

© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 7. CPCA: ICE Discount Trend
ICE Discount Trend

![](images/d7c1e12b5fa8c76d97d5eabe40f5c49589bc1450fb8a252475bef8d3b7596605.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, CPCA

Figure 8. CPCA: NEV Discount Trend  
![](images/f2359d60db28212f1f38c58161c7bf63689c3b4da0607e21e2a36e9abc58a460.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, CPCA

Figure 9. CPCA: Luxury ICE Discount  
![](images/8a8826389876e27eab0b05ad2db1c6950edc06e9691685cfd4a1af108424e5ad.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, CPCA

Figure 10. CPCA: JV ICE Discount  
![](images/7840eebf4c6b6c12794070ff1bfcb03cc4367234fba499a936c532a18dfd7160.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, CPCA

Figure 11. CPCA: Local ICE Discount  
![](images/9d264d3e205f350638257d7a4416e65c80e2c6bbc74b68b93363ab143eab1401.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, CPCA

## Companies Mentioned:

BMW (BMWG.DE; €58.32; 2; 16 Jul 26; 17:30)

BYD (1211.HK; HK\$88.7; 1; 17 Jul 26; 16:10)

BYD (002594.SZ; Rmb93.47; 1; 17 Jul 26; 15:00)

Geely Automobile (0175.HK; HK\$18.48; 1; 17 Jul 26; 16:10)

Great Wall Motor (2333.HK; HK\$8.66; 3; 17 Jul 26; 16:10)

Great Wall Motor (601633.SS; Rmb15.66; 3; 17 Jul 26; 15:00)

Leapmotor (9863.HK; HK\$35.14; 1; 17 Jul 26; 16:10)

Li Auto (LI.O; US\$12.86; 2; 16 Jul 26; 16:00)

Li Auto Inc (2015.HK; HK\$48.94; 2; 17 Jul 26; 16:10)

Mercedes-Benz Group AG (MBGn.DE; €45.86; 2; 16 Jul 26; 17:30)

NIO (NIO.N; US\$4.99; 1; 16 Jul 26; 16:00)

NIO (9866.HK; HK\$37.78; 1; 17 Jul 26; 16:10)

Seres Group (601127.SS; Rmb54.3; 3; 17 Jul 26; 15:00)

Seres Group (9927.HK; HK\$42.08; 3; 17 Jul 26; 16:10)

Volkswagen (VOWG\_p.DE; €73.46; 1; 16 Jul 26; 17:30)

XPeng (XPEV.N; US\$14.04; 1; 16 Jul 26; 16:00)

XPeng (9868.HK; HK\$51.65; 1; 17 Jul 26; 16:10)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing

such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
