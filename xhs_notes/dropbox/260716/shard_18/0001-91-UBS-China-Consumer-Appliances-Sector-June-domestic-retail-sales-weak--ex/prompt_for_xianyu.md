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
# China Consumer Appliances Sector June domestic retail sales weak, except for RVC

## We remain cautious on China's appliance sector

Based on AVC data, we estimate 1H26 omni-channel white goods retail sales fell from down 6% to down 21% YoY with RVC online sales down a milder 7%, mostly due to fading subsidy benefits and a high base. June omni-channel white goods retail sales fell from down 11% to down 28%, on a high base caused by subsidies and strong promotions during the 618 shopping festival in 2025. As per UBS Evidence Lab and Sensor Tower data, Anker app (mainly for portable power storage and balcony solar & storage) global/European/US downloads grew 90%/45%/231% YoY in 2Q26 and 59%/30%/150% YoY in June. Although Anker's Europe app downloads in June dropped from the peak, we think uncertainty on Middle East tensions may continue to support demand for balcony solar & storage. In addition, 2Q26 eufy (mainly for security camera and RVC) / soundcore (mainly for earbud) app downloads accelerated to 55%/27% YoY from 42%/17% YoY in 1Q26. Meanwhile, Insta360 global/China app downloads rose 51%/57% YoY in 2Q26. While we remain cautious on China's appliance sector, we think demand could stabilise in H226. Midea is our top pick in the white goods sector. We have a Neutral rating on Arashi.

## Major appliances: Haier gained share in WM/refrigerator; ASPs dropped MoM

In 1H26, offline AC/washing machine (WM)/refrigerator (fridge)/range-hood sales declined 17%/9%/10%/18% YoY, while online sales changed -25%/-2%/-2%/+0% YoY. We estimate the implied 1H26 omni-channel retail sales fell 21%/6%/6%/9% YoY, down from a high base in 1H25. Gree's AC online and offline share remained largely flat YoY in June, though its entry-level sub-brand KINGHOME's online share dropped from 2% in May to 1% in June. Midea's AC share dropped 2ppt YoY online but increased 1ppt YoY offline, while its sub-brand WAHIN's market share remained largely stable YoY in June. Haier's offline/online AC share changed -1ppt/+2ppt YoY. For WM/fridge, Haier gained +3ppt/+7ppt YoY online, while its offline share increased 1%/2% YoY in June. Xiaomi continued to lose online white goods share in June, especially for AC (-2ppt YoY), WM (-3ppt YoY) and fridge (-2ppt YoY). In June, except for online sales of AC and WM, ASPs dropped MoM due to 618 shopping festival discounts.

## RVC: online sales grew 20% YoY in June; Roborock continued to gain share

AVC data indicate 1H26 online robot vacuum cleaner (RVC) retail sales value dropped 7% YoY, as volume/ASP dropped 6%/1% YoY, while June RVC sales increased 20% YoY driven by volume (+25% YoY). May-June online RVC sales value increased 4% YoY due to the 618 festival. In June, Roborock led in RVC online share at 37% (+11ppt YoY), followed by Ecovacs' 32% (+2ppt YoY) and Dreame's 10% (-4ppt YoY). DJI's online share increased sequentially from 1% to 5% in June, with a new product launched in mid-May. In wet-dry vacuum cleaners, Roborock's June online sales increased 62% YoY (market average: +12%), with value share up 9ppt YoY to 30%, slightly below the market-leading brand Tineco at 32%.

## Small kitchen appliance sales growth remained soft for most categories

Offline and online sales of small kitchen appliances were generally soft (down 3-23% YoY) in 1H26, except for online pressure cooker and soymilk machine sales (up 5% and 6% YoY), according to AVC data.

Equities

China

Consumer Electronics

Molly Huang

Analyst

molly.huang@ubs.com

+86-213-866 8823

Christine Peng, CFA

Analyst

christine-y.peng@ubs.com

+852-2971 7571

## Anker's app tracker

Figure 1: YoY change in Anker app downloads (mainly portable power storage and balcony solar & storage)  
![](images/3660e4e852f439b7122933dba914b882bac403c3f75ca9570f04490b9be8d129.jpg)  
Source: UBS Evidence Lab, Sensor Tower (> Access Dataset)

Figure 2: Power storage app downloads in US  
![](images/efa7662607669f3dfcf3db3e0bf7e2fd595e95bb7a3b68a7037961876a8cec18.jpg)  
Source: UBS Evidence Lab, Sensor Tower (> Access Dataset)

Figure 3: Power storage app downloads in Europe  
![](images/053909429f74828775e57bcf018ee21f0907894d2d2906dd8409c4354686cc1a.jpg)  
Source: UBS Evidence Lab, Sensor Tower (> Access Dataset)

Figure 4: eufy app download (mainly security camera and RVC)  
![](images/40ee3cd410ef8ec74dd87b24a3049dde2c8e427ec66579d98b27d1f2429fa8d8.jpg)  
Source: UBS Evidence Lab, Sensor Tower (> Access Dataset)

Figure 5: soundcore app download (mainly earbuds)  
![](images/ba301d90d86ddf8074d3606dd92d66646195a4ee2cfee8e73c1c27f24dcb5755.jpg)  
Source: UBS Evidence Lab, Sensor Tower (> Access Dataset)

YoY growth - June 2026

## Appliance retail sales – monthly data tracking

Figure 6: Retail sales growth of key appliance categories (June 2026)

<table><tr><td colspan="4">TGT growth - June 2020</td></tr><tr><td>Offline</td><td>Value</td><td>Volume</td><td>ASP</td></tr><tr><td>AC</td><td>-29%</td><td>-28%</td><td>1%</td></tr><tr><td>WM</td><td>-19%</td><td>-1%</td><td>-0%</td></tr><tr><td>Refrigerator</td><td>-19%</td><td>-0%</td><td>-0%</td></tr><tr><td>Freezer</td><td>3%</td><td>2%</td><td>0%</td></tr><tr><td>Range hood</td><td>-21%</td><td>-8%</td><td>3%</td></tr><tr><td>Hobs</td><td>-24%</td><td>-22%</td><td>2%</td></tr><tr><td>Integrated stoves</td><td>1%</td><td>-1%</td><td>2%</td></tr><tr><td>Dishwasher</td><td>-8%</td><td>-8%</td><td>0%</td></tr><tr><td>Rice cooker</td><td>-22%</td><td>-2%</td><td>6%</td></tr><tr><td>Pressure cooker</td><td>-6%</td><td>-6%</td><td>3%</td></tr><tr><td>Induction cooker</td><td>-7%</td><td>-4%</td><td>6%</td></tr><tr><td>Soymilk machine</td><td>-6%</td><td>-9%</td><td>5%</td></tr><tr><td>Food processor</td><td>-26%</td><td>-21%</td><td>3%</td></tr><tr><td>RVC</td><td>11%</td><td>5%</td><td>5%</td></tr><tr><td>Wet-dry vacuum cleaner</td><td>-10%</td><td>-0%</td><td>1%</td></tr></table>

<table><tr><td colspan="4">YoY growth - June 2026</td></tr><tr><td>Online</td><td>Value</td><td>Volume</td><td>ASP</td></tr><tr><td>AC</td><td>-27%</td><td>-23%</td><td>-4%</td></tr><tr><td>WM</td><td>-14%</td><td>-12%</td><td>-2%</td></tr><tr><td>Refrigerator</td><td>-4%</td><td>-5%</td><td>1%</td></tr><tr><td>Freezer</td><td>-8%</td><td>-8%</td><td>0%</td></tr><tr><td>Range hood</td><td>-4%</td><td>-12%</td><td>9%</td></tr><tr><td>Hobs</td><td>-6%</td><td>-9%</td><td>3%</td></tr><tr><td>Integrated stoves</td><td>-52%</td><td>-38%</td><td>-22%</td></tr><tr><td>Dishwasher</td><td>-1%</td><td>-5%</td><td>-3%</td></tr><tr><td>Rice cooker</td><td>-9%</td><td>-14%</td><td>-5%</td></tr><tr><td>Pressure cooker</td><td>-9%</td><td>-6%</td><td>3%</td></tr><tr><td>Induction cooker</td><td>-11%</td><td>-10%</td><td>-1%</td></tr><tr><td>Soymilk machine</td><td>-2%</td><td>-6%</td><td>-4%</td></tr><tr><td>Food processor</td><td>-20%</td><td>-20%</td><td>0%</td></tr><tr><td>RVC</td><td>-20%</td><td>-25%</td><td>-3%</td></tr><tr><td>Wet-dry vacuum (</td><td>-2%</td><td>-27%</td><td>-11%</td></tr></table>

YoY growth - 1H26

<table><tr><td>Offline</td><td>Value</td><td>Volume</td><td>ASP</td></tr><tr><td>AC</td><td>-17%</td><td>-5%</td><td>3%</td></tr><tr><td>WM</td><td>-9%</td><td>-2%</td><td>8%</td></tr><tr><td>Fridge</td><td>-10%</td><td>1%</td><td>9%</td></tr><tr><td>Freezer</td><td>6%</td><td>1%</td><td>5%</td></tr><tr><td>Range hood</td><td>-18%</td><td>-4%</td><td>4%</td></tr><tr><td>Hobs</td><td>-23%</td><td>-6%</td><td>8%</td></tr><tr><td>Integrated stoves</td><td>-24%</td><td>-23%</td><td>1%</td></tr><tr><td>Dishwasher</td><td>-6%</td><td>-5%</td><td>-1%</td></tr><tr><td>Rice cooker</td><td>-19%</td><td>-9%</td><td>7%</td></tr><tr><td>Pressure cooker</td><td>-6%</td><td>-7%</td><td>3%</td></tr><tr><td>Induction cooker</td><td>-16%</td><td>-4%</td><td>0%</td></tr><tr><td>Soymilk machine</td><td>-14%</td><td>-2%</td><td>4%</td></tr><tr><td>Food processor</td><td>-23%</td><td>-9%</td><td>3%</td></tr><tr><td>RVC</td><td>22%</td><td>28%</td><td>5%</td></tr><tr><td>Wet-dry vacuum cleaner</td><td>0%</td><td>6%</td><td>7%</td></tr></table>

Source: AVC, UBS-S

YoY growth - 1H26

<table><tr><td>Online</td><td>Value</td><td>Volume</td><td>ASP</td></tr><tr><td>AC</td><td>-25%</td><td>-20%</td><td>-6%</td></tr><tr><td>WM</td><td>-2%</td><td>-6%</td><td>4%</td></tr><tr><td>Fridge</td><td>-2%</td><td>-8%</td><td>6%</td></tr><tr><td>Freezer</td><td>-6%</td><td>-2%</td><td>3%</td></tr><tr><td>Range hood</td><td>0%</td><td>-3%</td><td>15%</td></tr><tr><td>Hobs</td><td>-8%</td><td>-6%</td><td>10%</td></tr><tr><td>Integrated stoves</td><td>-43%</td><td>-30%</td><td>-19%</td></tr><tr><td>Dishwasher</td><td>20%</td><td>27%</td><td>-6%</td></tr><tr><td>Rice cooker</td><td>-3%</td><td>-3%</td><td>11%</td></tr><tr><td>Pressure cooker</td><td>-5%</td><td>0%</td><td>5%</td></tr><tr><td>Induction cooker</td><td>-8%</td><td>-1%</td><td>4%</td></tr><tr><td>Soymilk machine</td><td>-6%</td><td>-1%</td><td>8%</td></tr><tr><td>Food processor</td><td>-1%</td><td>-7%</td><td>6%</td></tr><tr><td>RVC</td><td>-7%</td><td>-6%</td><td>-1%</td></tr><tr><td>Wet-dry vacuum (</td><td>-7%</td><td>0%</td><td>-7%</td></tr></table>

Figure 7: AC monthly retail sales YoY trends (sell-through)

<table><tr><td colspan="25">AC - retail sales YoY growth</td></tr><tr><td>Offline</td><td>YTD</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>Online</td><td>YTD</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td></td></tr><tr><td>Volume</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Volume</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Industry</td><td>-15%</td><td>48%</td><td>42%</td><td>45%</td><td>-43%</td><td>28%</td><td>56%</td><td>4%</td><td>-13%</td><td>16%</td><td>28%</td><td>Industry</td><td>-20%</td><td>29%</td><td>22%</td><td>26%</td><td>39%</td><td>-7%</td><td>59%</td><td>36%</td><td>29%</td><td>2%</td><td>23%</td><td></td></tr><tr><td>Gree</td><td>-14%</td><td>40%</td><td>54%</td><td>58%</td><td>-65%</td><td>28%</td><td>51%</td><td>3%</td><td>-11%</td><td>17%</td><td>27%</td><td>Gree</td><td>-21%</td><td>25%</td><td>29%</td><td>19%</td><td>25%</td><td>3%</td><td>62%</td><td>28%</td><td>29%</td><td>0%</td><td>25%</td><td></td></tr><tr><td>Midea</td><td>-16%</td><td>44%</td><td>41%</td><td>41%</td><td>-16%</td><td>14%</td><td>60%</td><td>17%</td><td>-21%</td><td>23%</td><td>26%</td><td>Midea</td><td>-29%</td><td>36%</td><td>33%</td><td>25%</td><td>41%</td><td>-14%</td><td>67%</td><td>53%</td><td>41%</td><td>-5%</td><td>30%</td><td></td></tr><tr><td>Haier</td><td>-14%</td><td>6%</td><td>26%</td><td>30%</td><td>-38%</td><td>73%</td><td>51%</td><td>-15%</td><td>-5%</td><td>-4%</td><td>31%</td><td>Haier</td><td>-10%</td><td>-21%</td><td>-9%</td><td>-31%</td><td>-51%</td><td>-17%</td><td>63%</td><td>46%</td><td>25%</td><td>22%</td><td>-3%</td><td></td></tr><tr><td>Hisense</td><td>-25%</td><td>44%</td><td>45%</td><td>49%</td><td>-56%</td><td>14%</td><td>65%</td><td>-12%</td><td>-13%</td><td>22%</td><td>33%</td><td>Hisense</td><td>-24%</td><td>58%</td><td>64%</td><td>72%</td><td>67%</td><td>50%</td><td>82%</td><td>49%</td><td>34%</td><td>-1%</td><td>-9%</td><td></td></tr><tr><td>Value</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Value</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Industry</td><td>-18%</td><td>43%</td><td>49%</td><td>52%</td><td>-54%</td><td>18%</td><td>54%</td><td>-2%</td><td>-17%</td><td>17%</td><td>29%</td><td>Industry</td><td>-25%</td><td>29%</td><td>23%</td><td>26%</td><td>42%</td><td>-8%</td><td>56%</td><td>34%</td><td>32%</td><td>11%</td><td>27%</td><td></td></tr><tr><td>Gree</td><td>-15%</td><td>44%</td><td>57%</td><td>60%</td><td>-67%</td><td>23%</td><td>51%</td><td>1%</td><td>-13%</td><td>17%</td><td>28%</td><td>Gree</td><td>101%</td><td>22%</td><td>29%</td><td>19%</td><td>31%</td><td>3%</td><td>58%</td><td>25%</td><td>30%</td><td>-8%</td><td>42%</td><td></td></tr><tr><td>Midea</td><td>-19%</td><td>46%</td><td>49%</td><td>50%</td><td>-40%</td><td>5%</td><td>60%</td><td>3%</td><td>-26%</td><td>22%</td><td>26%</td><td>Midea</td><td>-31%</td><td>37%</td><td>27%</td><td>23%</td><td>44%</td><td>-8%</td><td>61%</td><td>47%</td><td>42%</td><td>15%</td><td>32%</td><td></td></tr><tr><td>Haier</td><td>-17%</td><td>20%</td><td>38%</td><td>40%</td><td>-50%</td><td>52%</td><td>52%</td><td>15%</td><td>-10%</td><td>-8%</td><td>33%</td><td>Haier</td><td>-15%</td><td>-14%</td><td>-3%</td><td>-28%</td><td>-51%</td><td>-17%</td><td>57%</td><td>35%</td><td>23%</td><td>7%</td><td>12%</td><td></td></tr><tr><td>Hisense</td><td>-28%</td><td>29%</td><td>50%</td><td>55%</td><td>-63%</td><td>3%</td><td>60%</td><td>-14%</td><td>-20%</td><td>26%</td><td>37%</td><td>Hisense</td><td>-21%</td><td>57%</td><td>61%</td><td>68%</td><td>63%</td><td>47%</td><td>80%</td><td>39%</td><td>24%</td><td>-2%</td><td>-5%</td><td></td></tr><tr><td>ASP</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>ASP</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Industry</td><td>-3%</td><td>18%</td><td>12%</td><td>13%</td><td>-20%</td><td>-8%</td><td>2%</td><td>-6%</td><td>-5%</td><td>-1%</td><td>-1%</td><td>Industry</td><td>-6%</td><td>-1%</td><td>-2%</td><td>0%</td><td>-5%</td><td>-1%</td><td>7%</td><td>3%</td><td>-5%</td><td>12%</td><td>-4%</td><td></td></tr><tr><td>Gree</td><td>-1%</td><td>5%</td><td>-6%</td><td>-4%</td><td>-6%</td><td>-4%</td><td>0%</td><td>-2%</td><td>-2%</td><td>0%</td><td>-1%</td><td>Gree</td><td>155%</td><td>4%</td><td>-1%</td><td>0%</td><td>-8%</td><td>0%</td><td>9%</td><td>5%</td><td>-2%</td><td>-8%</td><td>0%</td><td></td></tr><tr><td>Midea</td><td>-4%</td><td>-4%</td><td>13%</td><td>16%</td><td>-28%</td><td>-7%</td><td>0%</td><td>-12%</td><td>-5%</td><td>-12%</td><td>0%</td><td>Midea</td><td>-3%</td><td>-2%</td><td>9%</td><td>4%</td><td>-4%</td><td>-7%</td><td>18%</td><td>13%</td><td>-2%</td><td>-11%</td><td>-2%</td><td></td></tr><tr><td>Haier</td><td>-4%</td><td>5%</td><td>16%</td><td>14%</td><td>-20%</td><td>-12%</td><td>-3%</td><td>0%</td><td>-5%</td><td>-4%</td><td>-2%</td><td>Haier</td><td>-6%</td><td>8%</td><td>6%</td><td>4%</td><td>0%</td><td>1%</td><td>15%</td><td>20%</td><td>2%</td><td>-12%</td><td>-9%</td><td></td></tr><tr><td>Hisense</td><td>-3%</td><td>7%</td><td>-9%</td><td>11%</td><td>-14%</td><td>-10%</td><td>15%</td><td>-2%</td><td>-8%</td><td>-6%</td><td>-5%</td><td>Hisense</td><td>4%</td><td>3%</td><td>7%</td><td>15%</td><td>14%</td><td>5%</td><td>13%</td><td>20%</td><td>15%</td><td>0%</td><td>4%</td><td></td></tr><tr><td>Market share (by volume)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Market share (by volume)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gree</td><td>25%</td><td>28%</td><td>27%</td><td>25%</td><td>21%</td><td>23%</td><td>27%</td><td>26%</td><td>30%</td><td>25%</td><td>21%</td><td>Gree</td><td>18%</td><td>20%</td><td>21%</td><td>25%</td><td>31%</td><td>24%</td><td>21%</td><td>20%</td><td>18%</td><td>17%</td><td>17%</td><td></td></tr><tr><td>yoy chg.</td><td>1%</td><td>41%</td><td>-7%</td><td>-8%</td><td>-13%</td><td>0%</td><td>3%</td><td>0%</td><td>1%</td><td>0%</td><td>0%</td><td>yoy chg.</td><td>-1%</td><td>-1%</td><td>-2%</td><td>2

[中间内容因长度限制已省略]

 not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

![](images/2bc7ada0d16c201fc9774041c52c13fe6a61623ea3a6ca86885541b77b435091.jpg)

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
