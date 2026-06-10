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
# Base Metals Supply & Demand Tracker

Chinese exports are the relief valve for ex-China aluminium tightness

## Copper:

- China's apparent and end-use copper consumption diverge markedly. Our consumption-weighted end-use indicator for Chinese copper demand declined by 4% yoy (now +1.2% yoy YTD through 4M26) amid continued weakness in renewables installations and white goods production (Figure 22). The slowdown comes despite continued strong grid demand, EV production and product exports which work to offset weakness in other sectors. At the same time, Chinese apparent consumption was remarkable in April (+9% yoy), with inventory draws boosting overall figures reflecting the level of inventory destock across the supply chain over the 4Q25/1Q26 buyers strike in China. More recently, drawing momentum in Chinese inventory has leveled off in recent weeks as copper prices have ranged between \$13,500-14,000/mt (Figure 23).  
- US tariff review forthcoming. Later this month, by June 30, 2026, the US Commerce Secretary is to provide the President with an update on whether additional Section 232 copper tariff modifications are necessary. Our view remains that it is more likely than not that the Trump administration will enact an escalating tariff as was laid out in last July's original executive order (i.e. starting at $15\%$ in 2027, increasing to $30\%$ a year later) to 1) ensure that all the copper that has already been imported into the US stays onshore and 2) keep this excess US inventory as a critical reserve, rather than enact policy which incentivizes it to quickly destock in the coming years. A continued strong import pull into the US in the coming quarters would continue to strain ex-US cathode supply, particularly over periods where China's import arb is also open.

## Aluminium:

- Chinese aluminium semis and finished product exports are the relief valve for ex-China tightness. As LME inventories continue to draw lower to 330 kmt, Chinese visible inventory levels are still sitting near multi-year highs at \~1.4 mmt. With the semis export arb from China to rest of Asia open and at attractive levels (Figure 72), we continue to expect strong exports out of China to accelerate weekly withdrawals from onshore aluminium inventory in China (Figure 53 & Figure 55). So far, in the last 6 weeks only around 90 kmt has been drawn from SHFE and regional warehouses in China as production levels have risen and imports of aluminum have remained firm, with drawing activity only picking up since mid-May.  
- Producers in China are reaping the rewards of higher aluminium prices. Refined production in China in April grew by 3.4% yoy, running at an annualized level of 45 mmt, contributing to YTD growth of \~4% yoy according to CRU (Figure 70). Chinese producers are currently highly incentivized to keep churning out production towards the limiting cap amid elevated aluminium prices. We continue to monitor for disruptions of bauxite exports from Guinea, as this could become a serious bottleneck for Chinese producers

## Global Commodities Research

## Gregory C. Shearer

(44-20) 7134-8161

gregory.c.shearer@JPM.com

JPM Securities plc

## Ali A. Ibrahim

(44-20) 3493-6438

ali.ibrahim@JPM.com

JPM Securities plc

## Ananyashree Gupta

(91-22) 6157 3627

ananyashree.gupta@jpmchase.com

JPM India Private Limited

Contents

<table><tr><td>Base Metals Supply &amp; Demand Tracker</td><td>1</td></tr><tr><td>Global demand indicators</td><td>3</td></tr><tr><td>China demand indicators</td><td>5</td></tr><tr><td>Copper</td><td>9</td></tr><tr><td>Aluminium</td><td>16</td></tr><tr><td>Zinc</td><td>21</td></tr><tr><td>Nickel</td><td>25</td></tr><tr><td>JPM metals price forecasts</td><td>28</td></tr></table>

as $75\%$ of the country's bauxite imports come from Guinea alone. While bauxite imports from Guinea were up by $13\%$ yoy in April, a sharp change here could eventually threaten Chinese output and potentially also influence Chinese policy around exports as domestic supply security becomes more critical.

## Zinc:

- Chinese concentrate imports cooled in April though refined output stayed strong. China's zinc concentrate imports fell by nearly $10\%$ yoy in April, as a lack of concentrate availability is beginning to emerge with spot TCs in China flipping to negative territory since the end of March. Smelter production, on the other hand, remained robust increasing by $5\%$ yoy in April, as smelters work through concentrate inventory following strong imports in 1Q26. Even tighter concentrate markets could eventually weigh on Chinese output, which remains a risk for a tighter than expected refined balance this year.  
- Subdued demand continues to show via elevated and stagnant visible inventory. Total SHFE + social warehouse inventories in China have stabilized near 264 kmt as galvaniser operating rates remain subdued and construction activity remains lifeless in China (Figure 76). Galvaniser demand continues to remain below the 5-yr average, while apparent demand is down by 12% yoy as of April (Figure 78& Figure 86).

## Nickel:

\- Visible inventory builds stagnate. While inventory on SHFE continues to rise, LME stocks modestly declined from a peak in February, leading to net inventory growth of 70 kmt YTD to a total inventory level of \~470 kmt. Meanwhile, Indonesia's policy framework is set to weigh on producer margins amid higher ore benchmarks, potentially weighing on refined output somewhat this year, though the market remains focused on any upcoming additions to Indonesia's ore quota into the summer.

## China demand indicators:

- China's grid investment remains solid as renewables remain under pressure. Following a sharp jump at the start of the year, April grid spend rose by $9\%$ yoy, resulting in $>30\%$ growth yoy on a ytd basis (Figure 5). However, renewable installations continue to stumble, coming off the rapid pace of installations in 1H2025. Solar installations in April decelerated to $\sim 9.5\mathrm{GW}$ in April, decreasing by $79\%$ yoy, while wind installations declined by $7\%$ yoy to 5.4GW (Figure 7 & Figure 8).  
- NEV production in China rebounded in April. Total EV and PHEV production through April in China rose by 4% yoy while EV sales increased by 2.5% yoy in April. US EV sales continued to struggle while other regions such as Europe saw healthy EV sales. Overall, global passenger vehicle sales decreased by 10% yoy in April, with China and US taking the biggest hit (Figure 1).  
- White goods demand stumbled in April. Our estimate for total aggregate white goods copper demand in China decreased by 3% yoy in April, driven by a 9% decline in AC production.

## Global demand indicators

Table 1: Global metals monthly price change heatmap  
Percent change, MoM & YoY

<table><tr><td></td><td>Global Metals Price Heatmap</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>2023</td><td>2024</td><td>2025</td><td>2026 YTD</td></tr><tr><td rowspan="16">Metals Prices</td><td>LME Copper</td><td>4.1%</td><td>3.9%</td><td>-2.6%</td><td>3.0%</td><td>3.7%</td><td>6.0%</td><td>2.8%</td><td>11.0%</td><td>5.9%</td><td>1.4%</td><td>-9.3%</td><td>5.3%</td><td>5.0%</td><td>2.2%</td><td>2.4%</td><td>41.7%</td><td>10.5%</td></tr><tr><td>LME Aluminium</td><td>1.9%</td><td>6.3%</td><td>-1.3%</td><td>2.0%</td><td>2.5%</td><td>7.6%</td><td>-0.6%</td><td>4.4%</td><td>5.0%</td><td>-0.1%</td><td>3.8%</td><td>0.2%</td><td>5.5%</td><td>0.3%</td><td>7.0%</td><td>17.4%</td><td>21.7%</td></tr><tr><td>LME Zinc</td><td>1.1%</td><td>5.0%</td><td>0.3%</td><td>2.1%</td><td>5.0%</td><td>3.2%</td><td>0.0%</td><td>2.0%</td><td>9.1%</td><td>-2.5%</td><td>-8.3%</td><td>4.2%</td><td>5.3%</td><td>-10.6%</td><td>12.1%</td><td>4.7%</td><td>14.5%</td></tr><tr><td>LME Nickel</td><td>-1.2%</td><td>-0.1%</td><td>-1.8%</td><td>3.2%</td><td>-1.2%</td><td>-0.1%</td><td>-2.6%</td><td>12.3%</td><td>7.9%</td><td>-0.6%</td><td>-5.0%</td><td>13.8%</td><td>-2.1%</td><td>-44.7%</td><td>-7.7%</td><td>8.6%</td><td>11.3%</td></tr><tr><td>LME Lead</td><td>0.0%</td><td>4.4%</td><td>-3.6%</td><td>1.0%</td><td>-0.1%</td><td>1.4%</td><td>-1.8%</td><td>1.5%</td><td>-0.1%</td><td>-2.3%</td><td>-3.5%</td><td>2.8%</td><td>3.1%</td><td>-9.8%</td><td>-5.6%</td><td>3.0%</td><td>-0.1%</td></tr><tr><td>LME Tin</td><td>-3.0%</td><td>10.9%</td><td>-3.0%</td><td>7.1%</td><td>1.1%</td><td>1.9%</td><td>8.5%</td><td>3.6%</td><td>28.1%</td><td>11.1%</td><td>-23.4%</td><td>5.3%</td><td>12.6%</td><td>2.4%</td><td>14.4%</td><td>39.4%</td><td>33.4%</td></tr><tr><td>LME Cobalt spot</td><td>0.0%</td><td>-1.1%</td><td>0.0%</td><td>0.0%</td><td>5.1%</td><td>39.3%</td><td>0.0%</td><td>9.9%</td><td>5.5%</td><td>0.1%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>-44.3%</td><td>-15.4%</td><td>117.8%</td><td>5.6%</td></tr><tr><td>LME Lithium Hydroxide</td><td>-6.9%</td><td>-3.2%</td><td>-2.1%</td><td>5.4%</td><td>11.9%</td><td>1.0%</td><td>5.8%</td><td>10.1%</td><td>62.0%</td><td>-4.3%</td><td>12.5%</td><td>3.5%</td><td>7.8%</td><td>-80.4%</td><td>-42.9%</td><td>18.5%</td><td>83.4%</td></tr><tr><td>COMEX Copper</td><td>2.6%</td><td>7.5%</td><td>-13.4%</td><td>3.8%</td><td>7.5%</td><td>4.8%</td><td>1.9%</td><td>9.6%</td><td>4.3%</td><td>1.4%</td><td>-9.7%</td><td>5.6%</td><td>7.8%</td><td>2.1%</td><td>3.5%</td><td>41.1%</td><td>12.8%</td></tr><tr><td>SHFE Copper</td><td>0.5%</td><td>2.4%</td><td>-1.9%</td><td>1.0%</td><td>5.1%</td><td>4.8%</td><td>0.0%</td><td>13.1%</td><td>8.3%</td><td>-4.2%</td><td>-7.8%</td><td>5.8%</td><td>3.6%</td><td>4.4%</td><td>6.8%</td><td>33.7%</td><td>6.8%</td></tr><tr><td>SHFE Aluminium</td><td>0.6%</td><td>2.8%</td><td>-0.5%</td><td>0.6%</td><td>0.0%</td><td>2.5%</td><td>1.1%</td><td>5.6%</td><td>10.6%</td><td>-6.0%</td><td>0.1%</td><td>-1.3%</td><td>-0.5%</td><td>4.5%</td><td>1.0%</td><td>14.7%</td><td>6.8%</td></tr><tr><td>SHFE Zinc</td><td>-0.7%</td><td>-0.5%</td><td>-0.6%</td><td>-1.3%</td><td>-1.0%</td><td>2.0%</td><td>0.2%</td><td>4.1%</td><td>12.2%</td><td>-6.0%</td><td>-6.3%</td><td>0.4%</td><td>5.1%</td><td>-9.5%</td><td>19.0%</td><td>-9.4%</td><td>6.3%</td></tr><tr><td>Spot Gold</td><td>0.0%</td><td>0.4%</td><td>-0.4%</td><td>4.8%</td><td>11.9%</td><td>3.7%</td><td>5.9%</td><td>1.9%</td><td>13.3%</td><td>7.9%</td><td>-15.2%</td><td>-1.1%</td><td>-1.7%</td><td>13.1%</td><td>27.2%</td><td>64.6%</td><td>3.3%</td></tr><tr><td>Spot Silver</td><td>1.1%</td><td>9.5%</td><td>1.7%</td><td>8.2%</td><td>17.4%</td><td>4.4%</td><td>16.0%</td><td>26.8%</td><td>18.9%</td><td>10.1%</td><td>-24.1%</td><td>-1.9%</td><td>2.1%</td><td>-0.7%</td><td>21.5%</td><td>148.0%</td><td>1.1%</td></tr><tr><td>Spot Platinum</td><td>9.1%</td><td>28.5%</td><td>-5.0%</td><td>6.1%</td><td>14.9%</td><td>-0.1%</td><td>6.1%</td><td>23.3%</td><td>6.5%</td><td>7.9%</td><td>-18.5%</td><td>1.7%</td><td>-3.4%</td><td>-7.7%</td><td>-8.5%</td><td>127.0%</td><td>-8.7%</td></tr><tr><td>Spot Palladium</td><td>3.2%</td><td>13.6%</td><td>8.3%</td><td>-7.9%</td><td>14.3%</td><td>14.1%</td><td>1.1%</td><td>11.4%</td><td>5.7%</td><td>4.4%</td><td>-19.4%</td><td>3.6%</td><td>-11.2%</td><td>-38.6%</td><td>-17.1%</td><td>77.5%</td><td>-19.6%</td></tr></table>

\*LME is 3-month rolling forward, except cobalt which is spot. Lithium hydroxide and SHFE prices are futures contracts. Prices as of $5^{\text{th}}$ June 2026.  
Source: Bloomberg Finance L.P.

Table 2: Global manufacturing PMI by country

<table><tr><td></td><td></td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td rowspan="5">Groups</td><td>JPM Global</td><td>50.1</td><td>50.6</td><td>50.3</td><td>49.8</td><td>49.5</td><td>50.4</td><td>49.7</td><td>50.9</td><td>50.7</td><td>50.7</td><td>50.5</td><td>50.4</td><td>50.9</td><td>51.8</td><td>51.3</td><td>52.6</td></tr><tr><td>Developed Markets</td><td>49.3</td><td>50.0</td><td>49.1</td><td>49.1</td><td>50.0</td><td>50.5</td><td>49.2</td><td>50.9</td><td>50.3</td><td>50.3</td><td>50.5</td><td>50.5</td><td>51.4</td><td>51.8</td><td>52.0</td><td>53.8</td></tr><tr><td>Emerging Markets</td><td>50.8</td><td>51.1</td><td>51.3</td><td>50.5</td><td>49.2</td><td>50.4</td><td>50.1</td><td>50.9</td><td>51.2</td><td>51.2</td><td>50.5</td><td>50.4</td><td>50.6</td><td>52.0</td><td>50.7</td><td>51.6</td></tr><tr><td>European Union</td><td>46.7</td><td>47.8</td><td>48.6</td><td>49.1</td><td>49.2</td><td>49.2</td><td>49.6</td><td>50.4</td><td>49.7</td><td>49.7</td><td>49.5</td><td>48.8</td><td>49.5</td><td>50.5</td><td>51.3</td><td>52.0</td></tr><tr><td>Eurozone</td><td>46.6</td><td>47.6</td><td>48.6</td><td>49.0</td><td>49.4</td><td>49.5</td><td>49.8</td><td>50.7</td><td>49.8</td><td>49.8</td><td>49.6</td><td>48.8</td><td>49.5</td><td>50.8</td><td>51.6</td><td>52.2</td></tr><tr><td rowspan="4">Asia Pacific</td><td>China (Caixin/Markit)</td><td>50.1</td><td>50.8</td><td>51.2</td><td>50.4</td><td>48.3</td><td>50.4</td><td>49.5</td><td>50.5</td><td>51.2</td><td>51.2</td><td>49.9</td><td>50.1</td><td>50.3</td><td>52.1</td><td>50.8</td><td>52.2</td></tr><tr><td>China (Official PMI)</td><td>49.1</td><td>50.2</td><td>50.5</td><td>49.0</td><td>49.5</td><td>49.7</td><td>49.3</td><td>49.4</td><td>49.8</td><td>49.8</td><td>49.2</td><td>50.1</td><td>49.3</td><td>49.0</td><td>50.4</td><td>50.3</td></tr><tr><td>India</td><td>57.7</td><td>56.3</td><td>58.1</td><td>58.2</td><td>57.6</td><td>58.4</td><td>59.1</td><td>59.3</td><td>57.7</td><td>57.7</td><td>56.6</td><td>55.0</td><td>55.4</td><td>56.9</td><td>53.9</td><td>54.7</td></tr><tr><td>Japan</td><td>48.7</td><td>49.0</td><td>48.4</td><td>48.7</td><td>49.4</td><td>50.1</td><td>48.9</td><td>49.7</td><td>48.5</td><td>48.5</td><td>48.7</td><td>50.0</td><td>51.5</td><td>53.0</td><td>51.6</td><td>55.1</td></tr><tr><td rowspan="5">Europe</td><td>France</td><td>45.0</td><td>45.8</td><td>48.5</td><td>48.7</td><td>49.8</td><td>48.1</td><td>48.2</td><td>50.4</td><td>48.2</td><td>48.2</td><td>47.8</td><td>50.7</td><td>51.2</td><td>50.1</td><td>50.0</td><td>52.8</td></tr><tr><td>Germany</td><td>45.0</td><td>46.5</td><td>48.3</td><td>48.4</td><td>48.3</td><td>49.0</td><td>49.1</td><td>49.8</td><td>49.5</td><td>49.5</td><td>48.2</td><td>47.0</td><td>49.1</td><td>50.9</td><td>52.2</td><td>51.4</td></tr><tr><td>Italy</td><td>46.3</td><td>47.4</td><td>46.6</td><td>49.3</td><td>49.2</td><td>48.4</td><td>49.8</td><td>50.4</td><td>49.0</td><td>49.0</td><td>50.6</td><td>47.9</td><td>48.1</td><td>50.6</td><td>51.3</td><td>52.1</td></tr><tr><td>Spain</td><td>50.9</td><td>49.7</td><td>49.5</td><td>48.1</td><td>50.5</td><td>51.4</td><td>51.9</td><td>54.3</td><td>51.5</td><td>51.5</td><td>51.5</td><td>49.6</td><td>49.2</td><td>50.0</td><td>48.7</td><td>51.7</td></tr><tr><td>United Kingdom</td><td>48.3</td><td>46.9</td><td>44.9</td><td>45.4</td><td>46.4</td><td>47.7</td><td>48.0</td><td>47.0</td><td>46.2</td><td>46.2</td><td>50.2</td><td>50.6</td><td>51.8</td><td>51.7</td><td>51.0</td><td>53.7</td></tr><tr><td rowspan="4">Americas</td><td>Canada</td><td>51.6</td><td>47.8</td><td>46.3</td><td>45.3</td><td>46.1</td><td>45.6</td><td>46.1</td><td>48.3</td><td>47.7</td><td>47.7</td><td>48.4</td><td>48.6</td><td>50.4</td><td>51.0</td><td>50.0</td><td>53.3</td></tr><tr><td>Mexico</td><td>49.1</td><td>47.6</td><td>46.5</td><td>44.8</td><td>46.7</td><td>46.3</td><td>49.1</td><td>50.2</td><td>49.6</td><td>49.6</td><td>47.3</td><td>46.1</td><td>46.3</td><td>47.1</td><td>48.9</td><td>47.7</td></tr><tr><td>United States</td><td>51.2</td><td>52.7</td><td>50.2</td><td>50.2</td><td>52.0</td><td>52.9</td><td>49.8</td

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 08 Jun 2026 04:46 PM BST

Disseminated 08 Jun 2026 04:46 PM BST
"""
