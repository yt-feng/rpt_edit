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
# Global LNG Supply & Shipping Tracker

Qatar's winter supply clock starts to tick

Extel - 2026

CLICK TO VOTE

Global Fixed Income Research Survey

Voting Open July 6 - July 24

Please vote for JPM (5 stars)

![](images/2e7416a81073a1f28ae94b33e5cbc80f3eb3b13584bfe0e58de5d1995acb6312.jpg)

Global Commodities Research

Otar Dgebuadze, CFA
(44-20) 3493-8246
otar.dgebuadze@JPM.com
JPM Securities plc

Following the recent re-escalation of the Middle East conflict, LNG transit through the Strait of Hormuz has virtually halted. Based on Bloomberg ship-tracking data, the last observed transit occurred on 12 July, when a Qatari vessel exited the Strait (Figure 1). Since then, we have noted only one delivery to Kuwait. Qatar loadings, however, appear to be continuing, albeit at a reduced pace. We estimate that Qatar loadings are currently averaging around 22% on a 7-day moving-average basis, compared to 30% earlier in July. However, most of these loaded cargoes are effectively functioning as floating storage, given that Hormuz is once again effectively closed and intra-Gulf deliveries remain limited (Figure 2).

Aradhaya Makkar
aradhaya.makkar@jpmchase.com
JPM India Private Limited

The key question now is how quickly the current escalation can be resolved, and whether Qatar may be forced to shut down production again. There are many moving parts in these estimates. At the onset of the conflict, we estimated that Qatar had roughly five days of storage capacity when operating at full liquefaction capacity. Mathematically, this could extend to 20-25 days if Qatar is running at about 20% utilization, with floating storage providing an additional cushion. With no confirmed transits via Hormuz over the past week, we still count 23 LNG vessels in the Gulf (Table 1). However, how many of these vessels are already loaded, and how many are available for Qatar Energy to load additional cargoes, remains unclear. Furthermore, onshore operational complexities, including the processing and storage requirements for rich versus lean LNG, impose further limitations.

At current price levels of around €60/MWh this morning, we believe the market is beginning to price in a risk premium around Qatar winter volumes. This would mark a sharp sea-change compared to the prevailing market view prior to the escalation, which appeared to assume that Qatar would be fully back on line by winter and that Europe could source additional spot LNG cargoes as needed, rather than relying on storage as in the past. That expectation had helped keep a lid on TTF prices. However, the longer the current circumstances persist, the more that assumption will be tested, and prices could move sharply higher.

We think Qatar can reach “tank-full” within the next 2-3 weeks, potentially forcing production to shut down again or drop materially. There is, however, a significant margin of error around this timing, given the uncertainties and complexities over onshore/offshore storage availability, as described above. From the point of any shutdown, a full restart could take another 2-3 months, by which time we would already be in the Northern Hemisphere winter.

See page 15 for analyst certification and important disclosures.

Figure 1: LNG vessels traffic in Strait of Hormuz n of vessels, 7 day moving sum  
![](images/9f2dd02b3561790909b31351daefb3d513426ee5ea18583951b4afc3b5a01665.jpg)  
Latest forecasts from Global LNG Analyzer: Again on Qatari restarts, 21 April 2026  
Source: JPM Commodities Research

Figure 2: Actual ramp up speed of Qatar LNG liquefaction capacity  
![](images/ebc3daf826ccf38a42b0916dfeda118b29aa931c877e6422cbbe1d85554ec530.jpg)  
Actual loadings and Hormuz exits are 7-day moving averages. Hormuz exits are based on observed number of crossings and average Qatari cargo size, includes all exits (i.e. ballast and UAE loaded cargoes). Source: Bloomberg Finance L.P., Wood Mackenzie, JPM Commodities Research

## US LNG remains Asia bound

Meanwhile, the competitiveness of the US spot cargoes remains largely unchanged. Most of the cargoes are still pointing towards Asian destinations, as JKM/TTF netbacks remain largely flat for the next month or two (Figure 3 & Figure 4). A sizeable TTF netback premium only emerges from November, implying higher reliance on LNG imports in winter, as described above. However, this might prove a very risky strategy for Europe with historically low storage levels, rising uncertainties around Qatar supply and the usual winter weather risks not only in Europe, but also in the US and Asia.

Figure 3: JKM/TTF netbacks  
![](images/965922014017924c3ae6800ebd06cf60b776e8370626a2d9aa34487aac71d8e5.jpg)  
Netbacks based on USGC origin cargoes, assuming current West of Suez shipping spot rates and estimated other costs (insurance, port fees, etc.)

Figure 4: Europe share in USGC LNG exports  
![](images/16d644d42ab8e9b32c35b9c770e9c5da4b4badbe7d3a8f8c4f786dca72d6d998.jpg)  
Based on loading dates, in transit volumes based on the current location of the vessels  
Source: Bloomberg Finance L.P., JPM Commodities Research  
Source: Bloomberg Finance L.P., JPM Commodities Research

## Weekly export/import trends

During the week of July 13-19, LNG deliveries increased by a healthy 2.1 Bcm week-over-week (+0.8 Bcm YoY). This was driven by a 1.5 Bcm WoW increase in deliveries to China (+1 Bcm YoY), followed by increases in other Asian importers: JKM (+0.3 Bcm WoW, +0.6 Bcm YoY), India/Taiwan (each +0.2 Bcm WoW, flat YoY). Accordingly, deliveries to Europe decreased over the week by 0.6 Bcm WoW (-1.2 Bcm YoY), and remain well below seasonal norms and levels required to correct the storage path (Figure 5).

Corpus Christi LNG stage 3 capacity includes potential de-bottlenecking (2mtpa across 9 mid-scale trains). CP2 capacity excludes bolt-on 10mtpa, which is expected in 2028 (A)= Actual, (F) = Forecast, \* as of June 2026
Source: Wood Mackenzie, company data, Bloomberg Finance L.P., JPM Commodities Research

With regard to LNG exports, in line with our expectations, the global LNG supply starts to show signs of slowdown. Overall weekly loadings marginally decreased by 0.8 Bcm WoW (-1.2 Bcm YoY), led by the US (-0.2 Bcm WoW) and rest of North America (-0.3 Bcm WoW) (Figure 6).

Figure 5: Change in LNG imports  
![](images/8e26d536bfc1413e67b23f7c182c042f9a94ba9bd259976cf286cf1e70734b52.jpg)  
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 6: Change in LNG exports (loadings)  
![](images/e6e2d4f88e1efda0fb9ac3f920e6b803484f71619416e4bd367b25c2ce96de14.jpg)  
Source: Bloomberg Finance L.P., JPM Commodities Research

## Weekly loadings from recent projects

Loadings from existing projects, which are expected to increase supply year-over-year, remained broadly flat (Figure 7). Arctic LNG 2 loaded one cargo, reaching 44% utilization on a four-week rolling average basis, similar to the May peak level. LNG Canada loadings declined by one cargo week-over-week, leading to utilization declining to an 83% rate. In the US, Golden Pass and Plaquemines loaded one more cargo compared to the week before, while elsewhere loadings remained broadly unchanged (Figure 12-Figure 24).

Figure 7: LNG supply decomposition (2025-27)

<table><tr><td>Country</td><td>Project</td><td>JPMe start date</td><td>Capacity (Bcm/Year)</td><td>2025 Output (A)</td><td>2026 Output (F)</td><td>2027 Output (F)</td><td>2025 y/y (A)</td><td>2026 y/y (F)</td><td>2027 y/y (F)</td><td>2026 YTD y/y (A)*</td><td>% 2026 (A)*</td></tr><tr><td colspan="12">Projects started in 2025</td></tr><tr><td>US</td><td>Plaquemines LNG Phase 1 + 2</td><td>Jan-25</td><td>38.4</td><td>22.8</td><td>37.7</td><td>37.7</td><td>22.8</td><td>14.8</td><td>-</td><td>11.0</td><td>74%</td></tr><tr><td>Canada</td><td>LNG Canada</td><td>Jul-25</td><td>19.2</td><td>2.7</td><td>15.3</td><td>16.2</td><td>2.7</td><td>12.5</td><td>0.9</td><td>7.5</td><td>60%</td></tr><tr><td>US</td><td>Corpus Christi LNG Stage 3</td><td>Jan-25</td><td>16.4</td><td>2.9</td><td>11.0</td><td>15.6</td><td>2.9</td><td>8.1</td><td>4.6</td><td>4.2</td><td>52%</td></tr><tr><td>Russia</td><td>Arctic LNG 2 - Train 1 + 2</td><td>Jul-25</td><td>18.1</td><td>1.6</td><td>5.9</td><td>6.0</td><td>1.6</td><td>4.3</td><td>0.1</td><td>2.6</td><td>61%</td></tr><tr><td>Mauritania/Senegal</td><td>Tortue Phase 1 FLNG</td><td>Apr-25</td><td>3.3</td><td>1.8</td><td>3.4</td><td>3.4</td><td>1.8</td><td>1.6</td><td>-</td><td>1.4</td><td>90%</td></tr><tr><td colspan="12">Projects starting in 2026</td></tr><tr><td>Australia</td><td>Darwin Restart</td><td>Jan-26</td><td>5.1</td><td>-</td><td>2.3</td><td>3.5</td><td>-</td><td>2.3</td><td>1.3</td><td>0.7</td><td>31%</td></tr><tr><td>Congo</td><td>Nguya FLNG</td><td>Mar-26</td><td>3.3</td><td>-</td><td>1.9</td><td>2.6</td><td>-</td><td>1.9</td><td>0.7</td><td>0.6</td><td>31%</td></tr><tr><td>US</td><td>Golden Pass Export - Train 1</td><td>Apr-26</td><td>8.3</td><td>-</td><td>4.2</td><td>7.8</td><td>-</td><td>4.2</td><td>3.7</td><td>0.3</td><td>7%</td></tr><tr><td>Mexico</td><td>Costa Azul Phase 1</td><td>Sep-26</td><td>4.5</td><td>-</td><td>1.0</td><td>3.6</td><td>-</td><td>1.0</td><td>2.5</td><td>-</td><td>-</td></tr><tr><td>Australia</td><td>Pluto Expansion</td><td>Nov-26</td><td>6.9</td><td>-</td><td>0.7</td><td>5.8</td><td>-</td><td>0.7</td><td>5.1</td><td>-</td><td>-</td></tr><tr><td colspan="12">Projects starting in 2027</td></tr><tr><td>US</td><td>Golden Pass Export - Train 2</td><td>Feb-27</td><td>8.3</td><td>-</td><td>-</td><td>4.6</td><td>-</td><td>-</td><td>4.6</td><td>-</td><td>-</td></tr><tr><td>US</td><td>CP2 LNG Phase 1 + 2</td><td>Sep-27</td><td>39.7</td><td>-</td><td>-</td><td>4.2</td><td>-</td><td>-</td><td>4.2</td><td>-</td><td>-</td></tr><tr><td>US</td><td>Port Arthur LNG - Phase 1 - Train 1</td><td>Dec-27</td><td>8.9</td><td>-</td><td>-</td><td>0.1</td><td>-</td><td>-</td><td>0.1</td><td>-</td><td>-</td></tr><tr><td>Nigeria</td><td>NLNG Seven - Train 1</td><td>Jul-27</td><td>5.3</td><td>-</td><td>-</td><td>1.3</td><td>-</td><td>-</td><td>1.3</td><td>-</td><td>-</td></tr><tr><td>Indonesia</td><td>Genting FLNG</td><td>Jul-27</td><td>1.6</td><td>-</td><td>-</td><td>0.4</td><td>-</td><td>-</td><td>0.4</td><td>-</td><td>-</td></tr><tr><td>Qatar</td><td>Qatar North Field East - Train 1</td><td>Sep-27</td><td>11.0</td><td>-</td><td>-</td><td>1.7</td><td>-</td><td>-</td><td>1.7</td><td>-</td><td>-</td></tr><tr><td>Gabon</td><td>Gabon FLNG</td><td>Sep-27</td><td>1.0</td><td>-</td><td>-</td><td>0.2</td><td>-</td><td>-</td><td>0.2</td><td>-</td><td>-</td></tr><tr><td>Mexico</td><td>Altamira FLNG 1</td><td>Dec-27</td><td>1.9</td><td>-</td><td>-</td><td>0.0</td><td>-</td><td>-</td><td>0.0</td><td>-</td><td>-</td></tr><tr><td></td><td>Total 2025 projects</td><td></td><td></td><td>32.0</td><td>73.3</td><td>78.9</td><td>32.0</td><td>41.3</td><td>5.6</td><td>26.8</td><td>65%</td></tr><tr><td></td><td>Total 2026 projects</td><td></td><td></td><td>-</td><td>10.1</td><td>23.4</td><td>-</td><td>10.1</td><td>13.3</td><td>1.6</td><td>16%</td></tr><tr><td></td><td>Total 2027 projects</td><td></td><td></td><td>-</td><td>-</td><td>12.5</td><td>-</td><td>-</td><td>12.5</td><td>-</td><td>-</td></tr><tr><td></td><td>Total 2025-27 projects</td><td></td><td></td><td>32.0</td><td>83.4</td><td>114.9</td><td>32.0</td><td>51.4</td><td>31.5</td><td>28.3</td><td>55%</td></tr><tr><td>Qatar</td><td>Existing 14 trains</td><td></td><td></td><td>112.6</td><td>61.6</td><td>87.3</td><td>4.7</td><td>-51.0</td><td>25.7</td><td></td><td></td></tr><tr><td>UAE</td><td>Existing 2 trains</td><td></td><td></td><td>6.3</td><td>4.9</td><td>6.7</td><td>-1.2</td><td>-1.4</td><td>1.8</td><td></td><td></td></tr><tr><td></td><td>Rest of the world</td><td></td><td></td><td>448.0</td><td>451.6</td><td>451.6</td><td>2.3</td><td>3.6</td><td>-</td><td></td><td></td></tr><tr><td></td><td>Grand total</td><td></td><td></td><td>598.9</td><td>601.5</td><td>660.5</td><td>37.8</td><td>2.6</td><td>59.0</td><td></td><td></td></tr></table>

Table 1: LNG vessels in the Persian Gulf
As of 20 July 2026

<table><tr><td>Vessel Name</td><td>Beneficial Owner</td><td>DWT</td><td>Insurer</td><td>Insurance country</td><td>Comment</td></tr><tr><td>Al Samriya</td><td>Qatar Energy</td><td>154,900</td><td>Gard</td><td>Norway</td><td></td></tr><tr><td>Mekaines</td><td>Qatar Energy</td><td>143,309</td><td>Gard</td><td>Norway</td><td></td></tr><tr><td>Al Dafna</td><td>Qatar Energy</td><td>130,157</td><td>Britannia P&amp;I</td><td>UK</td><td></td></tr><tr><td>Al Sadd</td><td>Qatar Energy</td><td>121,913</td><td>NorthStandard</td><td>UK</td><td></td></tr><tr><td>Umm Al Amad</td><td>Qatar Energy</td><td>121,730</td><td>Japan P&amp;I Club</td><td>Japan</td><td></td></tr><tr><td>Al Gharrafa</td><td>Qatar Energy</td><td>113,861</td><td>Gard</td><td>Norway</td><td></td></tr><tr><td>Mesaimeer</td><td>Qatar Energy</td><td>113,852</td><td>Britannia P&amp;I</td><td>UK</td><td>Last seen July 19</td></tr><tr><td>Al Kharaitiyat</td><td>Qatar Energy</td><td>113,845</td><td>NorthStandard</td><td>UK</td><td></td></tr><tr><td>Al Sahla</td><td>Qatar Energy</td><td>113,715</td><td>UK P&amp;I</td><td>UK</td><td></td></tr><tr><td>Al Gattara</td><td>Qatar Energy</td><td>113,590</td><td>Gard</td><td>Norway</td><td></td></tr><tr><td>Al Shamal</td><td>Qatar Energy</td><td>109,662</td><td>NorthStandard</td><td>UK</td><td></td></tr><tr><td>Al Kharsaah</td><td>Qatar Energy</td><td>109,484</td><td>NorthStandard</td><td>UK</td><td></td></tr><tr><td>Milaha Qatar</td><td>Qatar Energy</td><td>77,803</td><td>NorthStandard</td><td>UK</td><td></td></tr><tr><td>Al Rayyan</td><td>Qatar Energy</td><td>72,430</td><td>Britannia P&amp;I</td><td>UK</td><td></td></tr><tr><td>Mubaraz</td><td>ADNOC</td><td>72,950</td><td>NorthStandard</td><td>UK</td><td>Last seen July 16</td></tr><tr><td>Seapeak Bahrain</td><td>Seapeak</td><td>95,289</td><td>NorthStandard</td><td>UK</td><td>Last seen July 19</td></tr><tr><td>Al Areesh</td><td>Seapeak</td><td>90,617</td><td>Skuld</td><td>Norway</td><td></td></tr><tr><td>Al Marrouna</td><td>Seapeak</td><td>81,936</td><td>Skuld</td><td>Norway</td><td></td></tr><tr><td>Gaslog Shanghai</td><td>China Development Bank</td><td>82,104</td><td>West of England</td><td>UK</td><td></td></tr><tr><td>Gaslog Skagen</td><td>China Development Bank</td><td>81,847</td><td>West of England</td><td>UK</td><td></td></tr><tr><td>Qtaifan</td><td>ICBC</td><td>88,039</td><td>Gard</td><td>Norway</td><td></td></tr><tr><td>Wadi Al Sail</td><td>Other/unknown</td><td>93,124</td><td>Skuld</td><td>Norway</td><td></td></tr><tr><td>Shandong Redwood</td><td>Other/unknown</td><td>79,084</td><td>Gard</td><td>Norway</td><td></td></tr></table>

Source: Bloomberg Finance L.P., JPM Commodities Research

# LNG shipments through major maritime routes

Figure 8: LNG vessels through the Strait of Hormuz  
![](images/0819f031b7bad402475baea648a9b7b79dda30a5d25b4e2b7ee975df2e162dc9.jpg)  
Includes all passages by laden and ballast vessels
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 9: LNG vessels through the Suez Canal n of vessels, 7 day moving sum  
![](images/c8743fc7e34415b22f0732238f9346d27f76228a0809b0b38951eb1e46b98880.jpg)  
Includes all passages by laden and ballast vessels
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 10: LNG vessels through the Panama Canal  
![](images/7fecab8d15dbce9310114445aeb1dc5ecd8f4ddbc33c3445e8d5714b2103f616.jpg)  
Includes all passages by laden and ballast vessels
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 11: LNG vessels through the Cape of Good Hope  
![](images/e1e2a6f78cc4e96bbf60f0144a458e6a82d4b8c3c3585e090ce14a692aafed8e.jpg)  
Includes all passages by laden and ballast vessels
Source: Bloomberg Finance L.P., JPM Commodities Research

## New supply tracker

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 20 Jul 2026 02:36 PM BST

Disseminated 20 Jul 2026 02:36 PM BST
"""
