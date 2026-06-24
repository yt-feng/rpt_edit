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
# JPM

## China Property

## Why the recent share price weakness?

Over the past 4 trading days, China Property has underperformed the HSI by $9\%$ . While high-frequency data (after adjustments as last week's data was disrupted by public holidays) maintains a similar trend vs. the past few months, we believe the share price weakness has mostly been driven by (1) negative read-through from weakening consumption data; (2) the sector's higher-beta nature amid the broader market sell-off; (3) a lack of near-term catalysts especially when high-frequency data is, while intact, not turning significantly better; (4) some investors may have focused on the weaker M/M secondary sales volume; however, in our view, this not an accurate way to gauge the market well-being due to seasonality (March & April typically see stronger sales), and thus Y/Y would be more reasonable. Even for leading SOEs like CRL & COLI, while their share prices had been relatively resilient throughout May & the first half of June (Figure 7), they both abruptly corrected $11\%$ (HSI: $-2\%$ ) over the past 2 trading days. We believe this was due to profit-taking amid broader market weakness as both stocks remain outperformers year-to-date. In fact, even after the correction, year-to-date, CRL $(+15\%) / \text{COLI} (+7\%)$ are still outperforming the HSI $(-7\%)$ (Figure 6). However, as data in tier-1 cities continues to show stabilization, on dips we'd selectively buy SOE developers with (1) outperforming sales growth; (2) strong exposure to tier-1 cities (COLI, CRL & Jinmao), but we remain cautious on most non-SOE developers (e.g. Vanke, Sunac) who may not benefit from the K-shaped stabilization.

## A quick look at the latest high-frequency data

\- Iceberg Index real-time secondary data (冰山指数实时二手成交): As of 21 June, 9-city (excluding Shanghai as data is not yet available as of the time of writing) real-time weekly secondary sales marginally rose $1\%$ Y/Y (down from $+12\%$ Y/Y). However, the drop is mainly due to the Dragonboat Festival. If we compare last week's data to the week last year with the Dragonboat Festival, the Y/Y growth would be $+15\%$ Y/Y, which is similar to the range $(10 - 20\%$ Y/Y) in previous weeks.

\- Iceberg Index tier-1 city secondary listings (冰山指数二手挂牌量): Likely under-appreciated by the market, the volume of secondary listings in tier-1 cities has been consistently coming down (dropped $2.5\%$ from the peak in March), and this is a key factor that will support continual secondary home price stabilization.

\- Sales registrations (official data with lag of a few weeks): The 60-city primary weekly sales registrations (一手网签) fell $23\%$ Y/Y, mostly due to the inclusion of the 3-day Dragon Boat Festival (during public holidays, sales registrations are significantly lower than usual). Compared to the same 3-day Dragon Boat Festival period in 2025, sales registrations were up $60\%$ Y/Y (but the sample size is too small, so we do not think this alone is representative). Similarly, the 12-city secondary sales registrations (二手网签) fell $13\%$ Y/Y (for a similar reason), reversing the positive Y/Y growth for the past 9 weeks. We expect both the primary & secondary sales registrations to see solid W/W

Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC (852) 2800-8513 karl.chan@JPM.com

Jocelyn Gao (852) 2800-8529 jocelyn.gao@JPM.com

(852) 2800-8599

venus.choi@JPM.com

JPM Securities (Asia Pacific) Limited/JPM Broking (Hong Kong) Limited

improvement due to the quarter-end-loaded nature of sales registrations, but we believe Y/Y growth is a more accurate way to assess market trend.

\- Home price stabilization in tier-1 cities has continued into May: According to the NBS home price index, tier-1 cities continued to register positive M/M growth (+0.2% in primary; +0.3% in secondary) in May (the $3^{rd}$ consecutive month). For the Centraline tier-1 secondary home price index, although the M/M growth slowed from +0.6% in April to +0.3% in May, this was the $4^{th}$ consecutive month of positive M/M growth. For more discussion, please see our earlier report with commentary on the latest NBS data.

## Iceberg Index – real time data

Figure 1: Iceberg Index - 10-city real time secondary daily sales since April 2026 (冰山指数实时二手成交)  
![](images/0a0bab2195a638ad5bb6df97b95af5881e1579e1572e1c739c95740dec8500e9.jpg)  
Source: Iceberg Index, JPM  
Note: The data for the last week is excluded as Shanghai data is not yet available. Please check our "Property Data Monitor" report for subsequent updates.

Figure 2: Iceberg Index - tier-1 cities' secondary listing volume (冰山指数二手挂牌量)  
No. of secondary listings ('000 units) - Tier 1 cities  
![](images/5271c35f7b5ec1219c86ddc7f2352935ed3b4d67c2ec86c9bd563f3efa0762e6.jpg)  
Source: Iceberg Index, JPM

## Official sales registrations (lag of a few weeks)

Figure 3: 60-city weekly primary sales registrations (一手网签) – compared with 2019-25  
![](images/240ae6a1af05cfcc1d2f77be2617707ab57419d000a9449e024284b75945fcb3.jpg)  
Source: CREIS  
Note: The steeper Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holidays).

Figure 4: 60-city weekly primary sales registrations (一手网签)  
![](images/7682170656aa19cf460030520e7dcf98f4521db303291f7bd81657a2080032cd.jpg)  
Source: CREIS  
Note: The Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holidays).

Table 1: 12-city primary sales registrations (一手网签) (comparing first 3 days of Dragon Boat Festival only)

<table><tr><td colspan="3">Primary - First 3 days of Dragon Boat Festival</td></tr><tr><td>Year</td><td>No. of units sold</td><td>2026 vs.</td></tr><tr><td>2020</td><td>17,067</td><td>-67%</td></tr><tr><td>2021</td><td>8,490</td><td>-34%</td></tr><tr><td>2022</td><td>5,319</td><td>6%</td></tr><tr><td>2023</td><td>5,535</td><td>2%</td></tr><tr><td>2024</td><td>3,919</td><td>44%</td></tr><tr><td>2025</td><td>3,519</td><td>60%</td></tr><tr><td>2026</td><td>5,628</td><td></td></tr></table>

Source: CREIS  
Note: As the sample size is small, the Y/Y growth may not necessarily be representative.

Figure 5: 8-city secondary sales registrations (二手网签)  
![](images/83c284fa3f7c4432ef2bb90aca1b18048b256e72f3c24521751bc398cadf7af8.jpg)  
Source: CREIS  
Note: The Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holidays).

## Home price trend

Table 2: Monthly home price index in tier-1 cities

<table><tr><td></td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td colspan="14">Primary (NBS)</td></tr><tr><td>Beijing</td><td>-0.4%</td><td>-0.3%</td><td>0.0%</td><td>-0.4%</td><td>0.2%</td><td>-0.1%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.0%</td><td>-0.2%</td><td>-0.2%</td></tr><tr><td>Shanghai</td><td>0.7%</td><td>0.4%</td><td>0.3%</td><td>0.4%</td><td>0.3%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td><td>0.0%</td><td>0.2%</td><td>0.3%</td><td>0.4%</td><td>0.2%</td></tr><tr><td>Guangzhou</td><td>-0.8%</td><td>-0.5%</td><td>-0.3%</td><td>-0.2%</td><td>-0.6%</td><td>-0.8%</td><td>-0.5%</td><td>-0.6%</td><td>-0.6%</td><td>0.0%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td></tr><tr><td>Shenzhen</td><td>-0.4%</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>-1.0%</td><td>-0.7%</td><td>-0.9%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.1%</td><td>0.4%</td></tr><tr><td>Tier-1 Primary (NBS)</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.3%</td><td>-0.3%</td><td>-0.5%</td><td>-0.3%</td><td>-0.3%</td><td>0.0%</td><td>0.2%</td><td>0.1%</td><td>0.2%</td></tr><tr><td colspan="14">Secondary (NBS)</td></tr><tr><td>Beijing</td><td>-0.8%</td><td>-1.0%</td><td>-1.1%</td><td>-1.2%</td><td>-0.9%</td><td>-1.1%</td><td>-1.3%</td><td>-1.3%</td><td>-0.2%</td><td>0.3%</td><td>0.6%</td><td>0.4%</td><td>0.1%</td></tr><tr><td>Shanghai</td><td>-0.7%</td><td>-0.7%</td><td>-0.9%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.6%</td><td>-0.4%</td><td>0.2%</td><td>0.4%</td><td>0.7%</td><td>0.6%</td></tr><tr><td>Guangzhou</td><td>-0.8%</td><td>-0.7%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.9%</td><td>-1.2%</td><td>-1.0%</td><td>-0.7%</td><td>-0.5%</td><td>0.2%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>Shenzhen</td><td>-0.5%</td><td>-0.5%</td><td>-0.9%</td><td>-0.8%</td><td>-1.0%</td><td>-0.9%</td><td>-1.0%</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>0.4%</td><td>0.3%</td><td>0.6%</td></tr><tr><td>Tier-1 Secondary (NBS)</td><td>-0.7%</td><td>-0.7%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.9%</td><td>-1.1%</td><td>-0.9%</td><td>-0.5%</td><td>-0.1%</td><td>0.4%</td><td>0.4%</td><td>0.3%</td></tr><tr><td colspan="14">Secondary (Centaline)</td></tr><tr><td>Beijing</td><td>-0.9%</td><td>-1.6%</td><td>-1.5%</td><td>-1.8%</td><td>-2.1%</td><td>-1.9%</td><td>-1.9%</td><td>-1.9%</td><td>-0.5%</td><td>1.2%</td><td>1.5%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>Shanghai</td><td>-1.4%</td><td>-1.4%</td><td>-1.7%</td><td>-1.7%</td><td>-1.5%</td><td>-2.2%</td><td>-2.0%</td><td>-2.8%</td><td>-0.5%</td><td>0.9%</td><td>1.0%</td><td>1.6%</td><td>0.9%</td></tr><tr><td>Guangzhou</td><td>-1.0%</td><td>-1.4%</td><td>-1.2%</td><td>-1.8%</td><td>-1.4%</td><td>-2.0%</td><td>-1.9%</td><td>-1.3%</td><td>-0.8%</td><td>-1.5%</td><td>0.8%</td><td>-0.3%</td><td>-0.2%</td></tr><tr><td>Shenzhen</td><td>-1.1%</td><td>-0.5%</td><td>-1.1%</td><td>-1.0%</td><td>-1.5%</td><td>-0.5%</td><td>-1.0%</td><td>-1.6%</td><td>-1.3%</td><td>0.9%</td><td>0.1%</td><td>1.0%</td><td>0.1%</td></tr><tr><td>Tier-1 Secondary (Centaline)</td><td>-1.1%</td><td>-1.2%</td><td>-1.4%</td><td>-1.6%</td><td>-1.6%</td><td>-1.6%</td><td>-1.7%</td><td>-1.9%</td><td>-0.8%</td><td>0.4%</td><td>0.9%</td><td>0.6%</td><td>0.3%</td></tr></table>

Source: NBS, Centraline

Sector share price performance

Figure 6: China property – year-to-date share price performance by stock

![](images/01aae231d85b523f2bd65f456046924e5b0e8e1c88f3bf766b617c1115227035.jpg)  
Source: Bloomberg Finance L.P. as of 22 June 2026, JPM

Figure 7: MSCI China Real Estate Index vs. HSI, year-to-date  
![](images/4a81120f9d91c6d31b7fd6922d79f4d86e730a416bc8dd74899f9c9abd29333a.jpg)  
Source: Bloomberg Finance L.P. as of 22 June 2026, JPM  
Note: normalized to 100 as of 5 January 2026

## Valuation Summary

Table 3: China property – valuation summary

<table><tr><td rowspan="2">Company</td><td rowspan="2">Stock Code</td><td rowspan="2">JPM Rating</td><td rowspan="2">Last Close (HK$)</td><td rowspan="2">Market Cap US$M</td><td rowspan="2">ADV US$M</td><td colspan="2">P/E</td><td colspan="2">Dvd Yield</td><td colspan="2">P/B</td><td colspan="4">Share price return</td></tr><tr><td>1FY (x)</td><td>2FY (x)</td><td>1FY (%)</td><td>2FY (%)</td><td>1FY (x)</td><td>2FY (x)</td><td>5D</td><td>YTD</td><td>1Y</td><td>vs. AT high</td></tr><tr><td colspan="16">Mainland China Developers</td></tr><tr><td>China Resources Land</td><td>1109.HK</td><td>OW</td><td>31.18</td><td>28,362</td><td>110.2</td><td>9.0</td><td>8.9</td><td>4.1%</td><td>4.2%</td><td>0.6</td><td>0.6</td><td>-14%</td><td>18%</td><td>22%</td><td>-25%</td></tr><tr><td>China Overseas Land</td><td>0688.HK</td><td>OW</td><td>13.13</td><td>18,331</td><td>64.6</td><td>10.4</td><td>9.4</td><td>3.5%</td><td>3.9%</td><td>0.3</td><td>0.3</td><td>-16%</td><td>7%</td><td>2%</td><td>-60%</td></tr><tr><td>China Jinmao</td><td>0817.HK</td><td>OW</td><td>1.35</td><td>2,327</td><td>10.8</td><td>21.1</td><td>16.8</td><td>2.6%</td><td>2.7%</td><td>0.4</td><td>0.4</td><td>-16%</td><td>12%</td><td>25%</td><td>-79%</td></tr><tr><td>C&amp;D International</td><td>1908.HK</td><td>NC</td><td>12.96</td><td>3,703</td><td>14.6</td><td>6.9</td><td>6.3</td><td>7.7%</td><td>8.6%</td><td>0.7</td><td>0.7</td><td>-16%</td><td>-12%</td><td>-15%</td><td>-53%</td></tr><tr><td>Greentown China</td><td>3900.HK</td><td>NC</td><td>6.97</td><td>2,258</td><td>13.1</td><td>32.7</td><td>16.4</td><td>2.2%</td><td>4.8%</td><td>0.4</td><td>0.4</td><td>-17%</td><td>-18%</td><td>-23%</td><td>-65%</td></tr><tr><td>Yuexiu Property</td><td>123.HK</td><td>NC</td><td>3.71</td><td>1,905</td><td>6.1</td><td>33.7</td><td>17.6</td><td>2.6%</td><td>4.5%</td><td>0.2</td><td>0.2</td><td>-17%</td><td>-6%</td><td>-8%</td><td>-81%</td></tr><tr><td>Poly Property</td><td>119.HK</td><td>NC</td><td>1.66</td><td>809</td><td>5.0</td><td>22.7</td><td>10.5</td><td>1.7%</td><td>5.7%</td><td>0.2</td><td>0.2</td><td>-13%</td><td>-16%</td><td>20%</td><td>-87%</td></tr><tr><td colspan="5">SOEs</td><td>76.9</td><td>11.7</td><td>9.8</td><td>3.9%</td><td>4.4%</td><td>0.5</td><td>0.5</td><td>-15%</td><td>10%</td><td>10%</td><td>-44%</td></tr><tr><td>Longfor</td><td>0960.HK</td><td>OW</td><td>6.60</td><td>5,975</td><td>21.6</td><td>-</td><td>-</td><td>0.0%</td><td>1.1%</td><td>0.2</td><td>0.2</td><td>-25%</td><td>-22%</td><td>-27%</td><td>-88%</td></tr><tr><td>Seazen Group</td><td>1030.HK</td><td>N</td><td>1.45</td><td>1,344</td><td>6.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.2</td><td>0.2</td><td>-13%</td><td>-29%</td><td>-37%</td><td>-87%</td></tr><tr><td colspan="5">POEs</td><td>18.7</td><td>-</td><td>-</td><td>0.0%</td><td>0.9%</td><td>0.2</td><td>0.2</td><td>-22%</td><td>-24%</td><td>-29%</td><td>-88%</td></tr><tr><td>China Vanke - H</td><td>2202.HK</td><td>UW</td><td>2.47</td><td>5,158</td><td>8.7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.3</td><td>0.3</td><td>-6%</td><td>-25%</td><td>-47%</td><td>-94%</td></tr><tr><td>Country Garden</td><td>2007.HK</td><td>UW</td><td>0.19</td><td>1,146</td><td>12.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-8%</td><td>-53%</td><td>-50%</td><td>-99%</td></tr><tr><td>Sunac China</td><td>1918.HK</td><td>UW</td><td>0.72</td><td>1,567</td><td>21.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.4</td><td>0.8</td><td>-14%</td><td>-45%</td><td>-50%</td><td>-99%</td></tr><tr><td>Shimao</td><td>0813.HK</td><td>UW</td><td>0.08</td><td>99</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-8%</td><td>-59%</td><td>-89%</td><td>-100%</td></tr><tr><td>Agile</td><td>3383.HK</td><td>NC</td><td>0.16</td><td>106</td><td>0.1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-17%</td><td>-39%</td><td>-57%</td><td>-99%</td></tr><tr><td>Logan</td><td>3380.HK</td><td>NC</td><td>1.44</td><td>1,044</td><td>3.1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-6%</td><td>-20%</td><td>78%</td><td>-91%</td></tr><tr><td>CIFI</td><td>884.HK</td><td>NC</td><td>0.05</td><td>104</td><td>0.7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-12%</td><td>-72%</td><td>-81%</td><td>-99%</td></tr><tr><td>R&amp;F</td><td>2777.HK</td><td>NC</td><td>0.24</td><td>114</td><td>0.3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-13%</td><td>-53%</td><td>-75%</td><td>-99%</td></tr><tr><td colspan="5">Distressed</td><td>10.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.2</td><td>0.3</td><td>-8%</td><td>-32%</td><td>-35%</td><td>-95%</td></tr><tr><td colspan="6">Mainland China Developers (Overall HK Listed)</td><td>9.1</td><td>7.6</td><td>3.1%</td><td>3.5%</td><td>0.4</td><td>0.4</td><td>-15%</td><td>1%</td><td>1%</td><td>-55%</td></tr><tr><td colspan="16"></td></tr><tr><td colspan="16">Mainland China Property Management</td></tr><tr><td>China Resources Mixc</td><td>1209.HK</td><td>OW</td><td>38.48</td><td>11,204</td><td>2

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
