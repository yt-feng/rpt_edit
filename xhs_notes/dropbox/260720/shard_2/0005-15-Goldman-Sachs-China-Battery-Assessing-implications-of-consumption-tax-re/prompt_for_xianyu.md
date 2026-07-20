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
# China Battery: Assessing implications of consumption tax resumption. CATL screens as most resilient — Buy A/H

What happened? On July 17, 2026, China's Ministry of Finance, China Customs, and State Taxation Administration jointly issued the “Notice on Adjusting the Consumption Tax Policy for Certain Battery Products”. Under the revised policy, China will phase out its decade-long consumption tax exemption for mature battery products. From Sep 1, 2026, primary lithium batteries and lithium-ion batteries will be subject to a 2% consumption tax, rising to the standard 4% rate from Sep 1, 2027. To support technological innovation, next-generation battery technologies will remain temporarily exempt from Sep 1, 2026, through Dec 31, 2028, including sodium-ion batteries, solid-state batteries, fuel cells, and advanced PV technologies.

Nick Zheng, CFA
+852-2978-1405 | nick.zheng@gs.com
GS (Asia) L.L.C.

Selina Yan
+852-2978-0178 | shuling.yan@gs.com
GS (Asia) L.L.C.

GS View: We view the policy change as manageable for sector leaders but more challenging for domestic-centric, lower-profitability battery makers, reinforcing our view of continued market-share consolidation. CATL screens as the most resilient name in our coverage, while most Tier-2/3 players face greater earnings sensitivity. Downstream, the impact appears limited for passenger vehicles and eHDTs under full pass-through, but BESS projects look more exposed given tighter return thresholds. Near term, anticipation of the consumption tax resumption could pull forward demand ahead of the implementation dates. We will monitor management commentary on the potential impact during the upcoming 2Q26 earnings season.

## Assessing the potential impact on battery makers

While final pass-through arrangements will likely vary by negotiation outcome across players and customers, we assess the potential impact under two simplified scenarios: no pass-through and 50% pass-through. As the consumption tax applies to domestic sales, companies with more domestic-skewed exposure and lower unit profitability are most sensitive to the policy. A 4% tax rate would imply an estimated unit tax of Rmb11–24/kWh for our covered companies, compared with their 2025 unit net profit of Rmb8–109/kWh.

CATL screens as the most resilient, with downside of just 1–6% versus our current GSe in 2026–2028E under 50% tax pass-through, and 2–13% with no pass-through. This is mainly supported by its high overseas exposure of over 30% and strong unit net profit of Rmb109/kWh in 2025, which exceeds the combined level of other covered players;

Most Tier-2 and Tier-3 players appear more vulnerable: We estimate earnings downside of 8–41% for CALB and REPT in 2026–2028E under 50% tax

pass-through, widening to 15–82% with no pass-through. Gotion faces potential risk of turning loss-making, given its lower domestic unit profitability relative to peers. By contrast, EVE and Zenergy appear less affected, supported by their relatively higher unit profitability.

We view this policy shift as a compelling opportunity for leading players to further consolidate market share. As the newly introduced consumption tax squeezes margins for smaller, less cost-efficient, and more domestic-centric manufacturers, many may find it increasingly difficult to either absorb the tax or pass it through to customers.

## Assessing the potential impact on the downstream

We also assess the potential downstream impact under a full pass-through scenario.

\- Passenger vehicles: We estimate a 1–2% end-customer price impact if the 4% battery consumption tax is fully passed through, with economy models likely more affected than premium models.

Electric heavy-duty trucks (eHDTs): The impact on driver economics should be limited. Under current fuel prices, a short-haul eHDT can generate roughly Rmb8k more profit per month than an ICE HDT. As such, even if the 4% tax is fully passed through, amounting to around Rmb8k per unit, drivers could recover the incremental cost within just one month of operation.

Battery energy storage system (BESS) projects: This segment appears most sensitive to the tax adjustment. Based on our estimates, if the 4% tax is fully passed through, the IRR of a 400MWh project would decline by 0.3ppt, potentially pushing projects currently near the hurdle rate into below required return threshold.

Exhibit 1: A 4% tax rate would imply an estimated unit tax of Rmb11–24/kWh for our covered companies, compared with their 2025 unit net profit of Rmb8–109/kWh.
Unit consumption tax and after-tax net profit across the battery companies we cover (2025-2028E), Rmb/kWh  
![](images/a231b54fcf228db27eab861914bc317fdf0e33fb9961d87beca1da81a2dba338.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 2: We view the policy change as manageable for sector leaders but more challenging for domestic-centric, lower-profitability battery makers, reinforcing our view of continued market-share consolidation. CATL screens as the most resilient name in our coverage, while most Tier-2/3 players face greater earnings sensitivity. Summary of earning impact to battery companies we covere

<table><tr><td rowspan="2"></td><td rowspan="2">2025</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>No tax/100% tax pass-through</td><td>Tax resumes, with 0% pass-through</td><td>Tax resumes, with 50% pass-through</td><td>No tax/100% tax pass-through</td><td>Tax resumes, with 0% pass-through</td><td>Tax resumes, with 50% pass-through</td><td>No tax/100% tax pass-through</td><td>Tax resumes, with 0% pass-through</td><td>Tax resumes, with 50% pass-through</td></tr><tr><td>Consumption tax (%)</td><td>0%</td><td>0%</td><td>2% since Sep 1st</td><td>2% since Sep 1st</td><td>0%</td><td>2% before Sep 1st and 4% after that</td><td>2% before Sep 1st and 4% after that</td><td>0%</td><td>4%</td><td>4%</td></tr><tr><td>Tax pass-through to end-customers (%)</td><td></td><td></td><td>0%</td><td>50%</td><td></td><td>0%</td><td>50%</td><td></td><td>0%</td><td>50%</td></tr><tr><td>Annualized consumption tax rate (%)</td><td>0%</td><td>0%</td><td>0.7%</td><td>0.3%</td><td>0%</td><td>2.7%</td><td>1.3%</td><td>0%</td><td>4%</td><td>2%</td></tr><tr><td>CATL</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>423.7</td><td>611.7</td><td>611.7</td><td>611.7</td><td>728.3</td><td>728.3</td><td>728.3</td><td>804.1</td><td>804.1</td><td>804.1</td></tr><tr><td>Domestic battery sales</td><td>281.3</td><td>398.6</td><td>398.6</td><td>398.6</td><td>474.5</td><td>474.5</td><td>474.5</td><td>518.3</td><td>518.3</td><td>518.3</td></tr><tr><td>as % of total sales</td><td>66%</td><td>65%</td><td>65%</td><td>65%</td><td>65%</td><td>65%</td><td>65%</td><td>64%</td><td>64%</td><td>64%</td></tr><tr><td>GP</td><td>111.3</td><td>149.2</td><td>146.5</td><td>147.8</td><td>182.9</td><td>170.3</td><td>176.6</td><td>208.0</td><td>187.3</td><td>197.7</td></tr><tr><td>GPM%</td><td>26.3%</td><td>24.4%</td><td>24.0%</td><td>24.2%</td><td>25.1%</td><td>23.4%</td><td>24.2%</td><td>25.9%</td><td>23.3%</td><td>24.6%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-2%</td><td>-1%</td><td></td><td>-7%</td><td>-3%</td><td></td><td>-10%</td><td>-5%</td></tr><tr><td>NP</td><td>72.2</td><td>95.6</td><td>93.3</td><td>94.5</td><td>118.9</td><td>108.1</td><td>113.5</td><td>137.8</td><td>120.2</td><td>129.0</td></tr><tr><td>NPM%</td><td>17.0%</td><td>15.6%</td><td>15.3%</td><td>15.4%</td><td>16.3%</td><td>14.8%</td><td>15.6%</td><td>17.1%</td><td>15.0%</td><td>16.0%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-2%</td><td>-1%</td><td></td><td>-9%</td><td>-5%</td><td></td><td>-13%</td><td>-6%</td></tr><tr><td>Zenergy</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>8.1</td><td>14.9</td><td>14.9</td><td>14.9</td><td>24.9</td><td>24.9</td><td>24.9</td><td>32.9</td><td>32.9</td><td>32.9</td></tr><tr><td>Domestic battery sales</td><td>8.1</td><td>14.9</td><td>14.9</td><td>14.9</td><td>24.9</td><td>24.9</td><td>24.9</td><td>32.9</td><td>32.9</td><td>32.9</td></tr><tr><td>as % of total sales</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr><tr><td>GP</td><td>1.5</td><td>2.3</td><td>2.2</td><td>2.3</td><td>3.9</td><td>3.3</td><td>3.6</td><td>5.4</td><td>4.0</td><td>4.7</td></tr><tr><td>GPM%</td><td>18.4%</td><td>15.6%</td><td>14.9%</td><td>15.2%</td><td>15.8%</td><td>13.1%</td><td>14.5%</td><td>16.3%</td><td>12.3%</td><td>14.3%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-4%</td><td>-2%</td><td></td><td>-17%</td><td>-8%</td><td></td><td>-25%</td><td>-12%</td></tr><tr><td>NP</td><td>0.8</td><td>1.1</td><td>1.0</td><td>1.1</td><td>1.9</td><td>1.3</td><td>1.6</td><td>2.8</td><td>1.6</td><td>2.2</td></tr><tr><td>NPM%</td><td>10.0%</td><td>7.5%</td><td>6.9%</td><td>7.2%</td><td>7.6%</td><td>5.2%</td><td>6.4%</td><td>8.3%</td><td>4.8%</td><td>6.6%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-8%</td><td>-4%</td><td></td><td>-31%</td><td>-16%</td><td></td><td>-42%</td><td>-21%</td></tr><tr><td>EVE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>61.5</td><td>92.2</td><td>92.2</td><td>92.2</td><td>107.1</td><td>107.1</td><td>107.1</td><td>106.2</td><td>106.2</td><td>106.2</td></tr><tr><td>Domestic battery sales</td><td>44.0</td><td>64.8</td><td>64.8</td><td>64.8</td><td>74.3</td><td>74.3</td><td>74.3</td><td>68.8</td><td>68.8</td><td>68.8</td></tr><tr><td>as % of total sales</td><td>72%</td><td>70%</td><td>70%</td><td>70%</td><td>69%</td><td>69%</td><td>69%</td><td>65%</td><td>65%</td><td>65%</td></tr><tr><td>GP</td><td>9.9</td><td>14.4</td><td>13.9</td><td>14.2</td><td>17.4</td><td>15.3</td><td>16.4</td><td>17.8</td><td>15.0</td><td>16.4</td></tr><tr><td>GPM%</td><td>16.2%</td><td>15.6%</td><td>15.1%</td><td>15.4%</td><td>16.2%</td><td>14.3%</td><td>15.3%</td><td>16.8%</td><td>14.1%</td><td>15.4%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-3%</td><td>-2%</td><td></td><td>-12%</td><td>-6%</td><td></td><td>-16%</td><td>-8%</td></tr><tr><td>NP</td><td>4.1</td><td>6.5</td><td>6.1</td><td>6.3</td><td>8.1</td><td>6.3</td><td>7.2</td><td>8.6</td><td>6.1</td><td>7.3</td></tr><tr><td>NPM%</td><td>6.7%</td><td>7.1%</td><td>6.6%</td><td>6.9%</td><td>7.6%</td><td>5.9%</td><td>6.7%</td><td>8.1%</td><td>5.7%</td><td>6.9%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-6%</td><td>-3%</td><td></td><td>-23%</td><td>-11%</td><td></td><td>-29%</td><td>-15%</td></tr><tr><td>CALB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>44.4</td><td>68.6</td><td>68.6</td><td>68.6</td><td>85.7</td><td>85.7</td><td>85.7</td><td>87.4</td><td>87.4</td><td>87.4</td></tr><tr><td>Domestic battery sales</td><td>43.5</td><td>67.2</td><td>67.2</td><td>67.2</td><td>84.0</td><td>84.0</td><td>84.0</td><td>85.7</td><td>85.7</td><td>85.7</td></tr><tr><td>as % of total sales</td><td>98%</td><td>98%</td><td>98%</td><td>98%</td><td>98%</td><td>98%</td><td>98%</td><td>98%</td><td>98%</td><td>98%</td></tr><tr><td>GP</td><td>7.4</td><td>11.2</td><td>10.8</td><td>11.0</td><td>14.4</td><td>12.2</td><td>13.3</td><td>15.0</td><td>11.6</td><td>13.3</td></tr><tr><td>GPM%</td><td>16.7%</td><td>16.4%</td><td>15.8%</td><td>16.1%</td><td>16.8%</td><td>14.2%</td><td>15.5%</td><td>17.1%</td><td>13.2%</td><td>15.2%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-4%</td><td>-2%</td><td></td><td>-16%</td><td>-8%</td><td></td><td>-23%</td><td>-11%</td></tr><tr><td>NP</td><td>1.5</td><td>2.7</td><td>2.2</td><td>2.5</td><td>3.6</td><td>1.6</td><td>2.6</td><td>3.8</td><td>0.7</td><td>2.2</td></tr><tr><td>NPM%</td><td>3.3%</td><td>3.9%</td><td>3.3%</td><td>3.6%</td><td>4.2%</td><td>1.9%</td><td>3.1%</td><td>4.3%</td><td>0.8%</td><td>2.6%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-16%</td><td>-8%</td><td></td><td>-56%</td><td>-28%</td><td></td><td>-82%</td><td>-41%</td></tr><tr><td>Rept</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>24.3</td><td>32.6</td><td>32.6</td><td>32.6</td><td>37.6</td><td>37.6</td><td>37.6</td><td>35.9</td><td>35.9</td><td>35.9</td></tr><tr><td>Domestic battery sales</td><td>22.6</td><td>28.8</td><td>28.8</td><td>28.8</td><td>33.2</td><td>33.2</td><td>33.2</td><td>31.1</td><td>31.1</td><td>31.1</td></tr><tr><td>as % of total sales</td><td>93%</td><td>88%</td><td>88%</td><td>88%</td><td>88%</td><td>88%</td><td>88%</td><td>87%</td><td>87%</td><td>87%</td></tr><tr><td>GP</td><td>2.7</td><td>4.1</td><td>4.0</td><td>4.1</td><td>5.0</td><td>4.1</td><td>4.5</td><td>4.8</td><td>3.6</td><td>4.2</td></tr><tr><td>GPM%</td><td>11.2%</td><td>12.7%</td><td>12.2%</td><td>12.5%</td><td>13.3%</td><td>10.9%</td><td>12.1%</td><td>13.4%</td><td>10.0%</td><td>11.7%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-5%</td><td>-2%</td><td></td><td>-18%</td><td>-9%</td><td></td><td>-26%</td><td>-13%</td></tr><tr><td>NP</td><td>0.6</td><td>1.2</td><td>1.0</td><td>1.1</td><td>1.5</td><td>0.6</td><td>1.1</td><td>1.4</td><td>0.3</td><td>0.8</td></tr><tr><td>NPM%</td><td>2.6%</td><td>3.7%</td><td>3.1%</td><td>3.4%</td><td>3.9%</td><td>1.7%</td><td>2.8%</td><td>3.9%</td><td>0.7%</td><td>2.3%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-15%</td><td>-8%</td><td></td><td>-56%</td><td>-28%</td><td></td><td>-82%</td><td>-41%</td></tr><tr><td>Gotion</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>45.1</td><td>62.0</td><td>62.0</td><td>62.0</td><td>74.2</td><td>74.2</td><td>74.2</td><td>76.2</td><td>76.2</td><td>76.2</td></tr><tr><td>Domestic battery sales</td><td>35.3</td><td>47.6</td><td>47.6</td><td>47.6</td><td>56.2</td><td>56.2</td><td>56.2</td><td>55.3</td><td>55.3</td><td>55.3</td></tr><tr><td>as % of total sales</td><td>78%</td><td>77%</td><td>77%</td><td>77%</td><td>76%</td><td>76%</td><td>76%</td><td>73%</td><td>73%</td><td>73%</td></tr><tr><td>GP</td><td>7.3</td><td>9.3</td><td>8.9</td><td>9.1</td><td>11.4</td><td>9.9</td><td>10.6</td><td>11.2</td><td>9.0</td><td>10.1</td></tr><tr><td>GPM%</td><td>16.2%</td><td>14.9%</td><td>14.4%</td><td>14.7%</td><td>15.3%</td><td>13.3%</td><td>14.3%</td><td>14.7%</td><td>11.7%</td><td>13.2%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-3%</td><td>-2%</td><td></td><td>-13%</td><td>-7%</td><td></td><td>-20%</td><td>-10%</td></tr><tr><td>NP</td><td>2.4</td><td>0.9</td><td>0.6</td><td>0.8</td><td>1.9</td><td>0.5</td><td>1.2</td><td>1.5</td><td>(0.5)</td><td>0.5</td></tr><tr><td>NPM%</td><td>5.3%</td><td>1.5%</td><td>1.0%</td><td>1.2%</td><td>2.6%</td><td>0.7%</td><td>1.6%</td><td>1.9%</td><td>-0.7%</td><td>0.6%</td></tr><tr><td>Diff%</td><td></td><td></td><td>-32%</td><td>-16%</td><td></td><td>-71%</td><td>-36%</td><td></td><td>-135%</td><td>-68%</td></tr><tr><td>Farasis</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>9.1</td><td>9.1</td><td>9.1</td><td>9.1</td><td>9.7</td><td>9.7</td><td>9.7</td><td>10.4</td><td>10.4</td><td>10.4</td></tr><tr><td>Domestic battery sales</td><td>1.6</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.3</td><td>2.3</td><td>2.3</td><td>2.5</td><td>2.5</td><td>2.5</td></tr><tr><td>as % of total sales</td><td>17%</td><td>22%</td><td>22%</td><td>22%</td><td>23%</td><td>23%</td><td>23%</td><td>24%</td><td>24%</td><td>24%</td></tr><tr><td>GP</td><td>0.8</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.1</td><td>1.1</td><td>1.2</td><td>1.1</td><td>1.2</td></tr><tr><td>GPM%</td><td>9.2

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for

equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
