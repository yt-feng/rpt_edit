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
# Property Data Monitor

Mainland China: weekly sales turn worse due to holidays; HK: home prices up another 0.6% W/W

## Mainland China

\- Iceberg 10-city real-time secondary weekly sales (冰山指数实时二手成交) dropped $0.05\%$ Y/Y (down from $+13\%$ Y/Y). Tier-1 cities' weekly sales dropped $3\%$ Y/Y (down from $+14\%$ ) (Table 1). The decline is mostly due to the Dragon Boat Festival. If we compare last week's data vs. the week with the same festival last year, 10-city & tier-1 sales would be up $15\% / 10\%$ Y/Y. Real-time sales generally lead the trend of official sales registrations by a few weeks.

\- Iceberg 10-city secondary listings (冰山指数二手挂牌量) fell further, down $0.2\%$ W/W. Tier-1 cities' listings dropped $0.5\%$ W/W, while Shanghai's dropped another $1.1\%$ W/W (prior: $-0.6\%$ ) (Table 2). The volume of secondary listings in tier-1 cities has been consistently coming down (down $2.6\%$ from the peak in March), and this is a key factor that will support continual secondary home price stabilization.

\- 60-city primary sales registrations (一手网签) fell $23\%$ Y/Y (more), mostly due to the inclusion of the 3-day Dragon Boat Festival (during public holidays, sales registrations are significantly lower than usual). Compared to the same 3-day Dragon Boat Festival period in 2025, sales registrations were up $60\%$ Y/Y (but the sample size is too small, hence we do not think this alone is representative).

\- 12-city secondary sales registrations (二手网签) fell $13\%$ Y/Y (Figure 7), reversing the positive Y/Y growth for the past 9 weeks (due to public holidays). Shanghai $(+12\%)$ is the only city with Y/Y growth among tier-1 cities. YTD, 12-city secondary sales have risen $5\%$ Y/Y (Shanghai: $+13\%$ ).

\- The Centraline tier-1 cities' secondary asking price index dropped mildly from 17.8 to 17.3 (Figure 3).

\- The Centaline manager confidence index dropped from 53 to 51 (Figure 4).

\- Southbound holdings rose 0.32% W/W (Table 7): Sunac +2.4%; CRL +0.9%

\- Share price moves (Figure 17): The sector dropped 13% last week, underperforming the HSI (-5%). The outperformer was Sunac (-5%). The underperformers were A-Living (-20%) and Longfor (-17%). For further discussion, please see our report China Property: Why the recent share price weakness?

• JPM top picks: COLI, CR Land, Jinmao and CR Mixc.

## Hong Kong SAR

\- The home price index rose 0.6% W/W (Figure 12). Home prices have risen 10.4% YTD, already reaching our full-year target of 10-15%. Looking ahead to 2H26, we expect slower price growth of <5%. For more discussion, please see our report HK Residential Property: Home prices already hit our full-year target; momentum may slow in 2H.

• Secondary transactions in the top 35 estates totaled 43 units, down 16%

## Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC
(852) 2800-8513
karl.chan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

(852) 2800-8599
venus.choi@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Jocelyn Gao
(852) 2800-8529
jocelyn.gao@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## APAC Credit Research

Alvin Au AC
(852) 2800-8533
alvin.au@JPM.com
JPM Securities (Asia Pacific) Limited

Soo Chong Lim
(852) 2800-7387
soochong.lim@JPM.com
JPM Securities (Asia Pacific) Limited

Shirley Yau
(852) 2800-0566
shirley.yau@JPM.com
JPM Securities (Asia Pacific) Limited

See page 20 for analyst certification and important disclosures, including non-US analyst disclosures.

W/W & down 47% Y/Y (Figure 11), the lowest since CNY. This is partially due to adverse weather.

\- The Centa Salesman Index (CSI) (Figure 14) moderated from 69.6 last week to 68.2. A reading of $>50 =$ sentiment is positive and property prices are likely to rise.

\- The Centaline Valuation Index (CVI) rose from 82.7 last week to 86.2 this week.

\- Southbound holdings fell 0.07% W/W (Table 7): Hang Lung Prop -0.6%; Swire Prop +0.04%.

\- Share price moves (Figure 18): The sector dropped $4.4\%$ last week, marginally outperforming the HSI $(-4.7\%)$ . The outperformer was HKL $(-1\%)$ , followed by Hysan and JM (both $-2\%$ ), while Champion REIT and NWD (both $-8\%$ ) underperformed.

JPM top picks: Developers – CKA, Sino; landlords – Swire Prop & HKL; conglomerates – JM & CKH.

## Credit View (by Alvin Au)

\- The JACI China HY Property index rose 0.3% (vs China HY: +0.16%) last week, resuming the uptrend after a brief correction the previous week. This brings YTD returns to +6.4%.

\- Seazen: Debtwire reported that Seazen is planning a Rmb2bn tap of private REIT as soon as in June. This is on top of a Rmb616mn private REIT issued in Nov 2025 backed by its Shanghai Qingpu Wuyue Plaza, and the developer will add two more shopping malls in Tianjin and Nantong as underlying assets for this tap. We think the scale of the tap is material, as it more than covers the Rmb1.7bn of onshore maturities for the rest of 2026. Management mentioned earlier that it is planning to launch a public REIT as an additional funding channel later in 2026 as well.

\- Continued K-shape for China's housing market as reflected in May 2026 NBS data: Top-tier cities remain solid as all four tier-1 cities report positive m/m increase in secondary home price (for the third month in a row). However, the broader industry remains weak with the 70-city m/m decline marginally widening from -0.23% in April to -0.26% in May (see details in equity report). As market fragmentation continues, we continue to prefer credits with IP transformation stories, solid debt servicing ability and decent valuations.

JPM top picks: LNGFOR '29s (84 offer, 9.9% ytm) and SHUION '29s (101.5 offer, 9.1% ytm).

## Table Of Contents

Mainland China.... 1
Hong Kong SAR.... 1
Credit View (by Alvin Au).... 2
1. Mainland China – real-time secondary sales & listings .... 4
2. Mainland China – leading indicators from Centraline.... 5
3. Mainland China – Weekly primary sales registrations .... 6
4. Mainland China – Weekly secondary sales registrations. .... 7
5. Hong Kong – Residential market update .... 8
6. Hong Kong – Tourist arrivals and resident departures .... 12
7. Share price update .... 13
8. Credit recommendations .... 17
9. Equity valuation summary .... 18

## 1. Mainland China – real-time secondary sales & listings

Table 1: Iceberg 10-city real time secondary weekly sales 冰山指数实时二手每周成交 (十大城市)

<table><tr><td rowspan="2">Week ending</td><td colspan="6">No. of units</td><td colspan="6">Y/Y</td><td colspan="6">4-week rolling Y/Y</td></tr><tr><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>Top-10</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>Top-10</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>Top-10</td></tr><tr><td>24-May-26</td><td>3,795</td><td>6,014</td><td>2,460</td><td>1,396</td><td>13,665</td><td>31,096</td><td>11%</td><td>14%</td><td>17%</td><td>15%</td><td>14%</td><td>13%</td><td>16%</td><td>16%</td><td>26%</td><td>24%</td><td>18%</td><td>17%</td></tr><tr><td>31-May-26</td><td>3,799</td><td>5,488</td><td>2,694</td><td>1,391</td><td>13,372</td><td>30,110</td><td>19%</td><td>11%</td><td>35%</td><td>29%</td><td>19%</td><td>22%</td><td>16%</td><td>18%</td><td>26%</td><td>25%</td><td>20%</td><td>19%</td></tr><tr><td>7-Jun-26</td><td>3,817</td><td>5,597</td><td>2,462</td><td>1,257</td><td>13,133</td><td>29,310</td><td>22%</td><td>16%</td><td>17%</td><td>36%</td><td>19%</td><td>16%</td><td>15%</td><td>13%</td><td>23%</td><td>25%</td><td>16%</td><td>16%</td></tr><tr><td>14-Jun-26</td><td>3,980</td><td>5,580</td><td>2,416</td><td>1,126</td><td>13,102</td><td>29,372</td><td>16%</td><td>18%</td><td>8%</td><td>0%</td><td>14%</td><td>13%</td><td>17%</td><td>15%</td><td>19%</td><td>19%</td><td>16%</td><td>16%</td></tr><tr><td>21-Jun-26</td><td>3,288</td><td>4,528</td><td>1,881</td><td>1,011</td><td>10,708</td><td>25,055</td><td>1%</td><td>-5%</td><td>-4%</td><td>-6%</td><td>-3%</td><td>0%</td><td>14%</td><td>20%</td><td>14%</td><td>14%</td><td>12%</td><td>13%</td></tr></table>

Source: Iceberg Index  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 1: Iceberg 10-city real time secondary daily sales 冰山指数实时二手每日成交 (十大城市)  
![](images/4cc37c7fdafb79b314a5c3deae11c02976f5733b8ee8601ac220aca5d11afcac.jpg)  
Source: Iceberg Index  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Table 2: Iceberg 10-city secondary listing volume 冰山指数二手挂牌量 (十大城市)

<table><tr><td rowspan="2">Week ending</td><td colspan="6">No. of secondary listings (&#x27;000 units)</td><td colspan="6">W/W</td></tr><tr><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier-1</td><td>Top-10</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier-1</td><td>Top-10</td></tr><tr><td>25-May-26</td><td>120</td><td>85</td><td>137</td><td>89</td><td>431</td><td>1,559</td><td>-0.6%</td><td>-0.5%</td><td>-0.2%</td><td>0.2%</td><td>-0.3%</td><td>0.0%</td></tr><tr><td>1-Jun-26</td><td>120</td><td>84</td><td>137</td><td>89</td><td>430</td><td>1,556</td><td>-0.2%</td><td>-0.6%</td><td>-0.1%</td><td>-0.1%</td><td>-0.2%</td><td>-0.2%</td></tr><tr><td>8-Jun-26</td><td>119</td><td>84</td><td>137</td><td>89</td><td>429</td><td>1,555</td><td>-0.2%</td><td>-0.4%</td><td>-0.2%</td><td>0.1%</td><td>-0.2%</td><td>-0.1%</td></tr><tr><td>15-Jun-26</td><td>120</td><td>84</td><td>137</td><td>89</td><td>429</td><td>1,559</td><td>0.3%</td><td>-0.6%</td><td>0.0%</td><td>0.3%</td><td>0.0%</td><td>0.2%</td></tr><tr><td>22-Jun-26</td><td>119</td><td>83</td><td>137</td><td>88</td><td>427</td><td>1,556</td><td>-0.4%</td><td>-1.1%</td><td>-0.1%</td><td>-0.8%</td><td>-0.5%</td><td>-0.2%</td></tr></table>

Source: Iceberg Index

Figure 2: Iceberg tier-1 cities secondary listing volume 冰山指数二手挂牌量 (一线城市)  
![](images/8fc9e902063edb0d36195c2f744d5ab28e6566e14a5d86f94abb7cb3677ccf9c.jpg)  
Source: Iceberg Index

## 2. Mainland China – leading indicators from Centraline

Figure 3: Centraline secondary asking price index vs. NBS secondary home price index M/M in tier-1 cities

![](images/ea98acb5442960e7a8ade382ed3867ccb4e339ea8ea3b9b79d20089b41603454.jpg)  
Source: Centraline, Wind, NBS.  
Note: The asking price index represents the percentage of projects with home price increases. For example, an index of 20 means that 20% of projects raise prices (while 80% do not).  
Figure 4: Centraline secondary manager confidence index in tier-1 cities vs. three-month rolling secondary sales

![](images/e5e3b7e8e40ee9da8834478dc6e83053cca0aed7c70dfdf5fc569c19b26d31c2.jpg)  
Source: Centraline, Wind. Note: The index surveys managers across the country for their judgment on the market outlook.

# 3. Mainland China – Weekly primary sales registrations

Figure 5: 60-city weekly primary sales registrations (一手网签) – compared with 2019-24  
![](images/95d0ab1478fb3f8db01a19b1326c6f4957650dbfdebc49777325cecf2626880d.jpg)  
Source: CREIS.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 6: 60-city weekly primary sales registrations (一手网签)  
![](images/495684aef95b1ce19fbcdace00e3704b53cece7fbf20849e5ea0b86eebb35efc.jpg)  
Source: CREIS.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Table 3: 60-city weekly primary sales registrations (一手网签) by tier

<table><tr><td rowspan="2">Week ending</td><td colspan="6">60-City</td><td colspan="6">Tier-1</td><td colspan="6">Tier-2</td><td colspan="6">Tier-3/4</td></tr><tr><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td></td><td></td><td></td><td></td></tr><tr><td>19-Apr-26</td><td>21,159</td><td>6%↑</td><td>15%↑</td><td>-1%↑</td><td>-69%↑</td><td>3,726</td><td>5%↑</td><td>13%↑</td><td>9%↑</td><td>-35%↓</td><td>12,813</td><td>18%↑</td><td>15%↑</td><td>3%↑</td><td>-70%↑</td><td>4,620</td><td>-16%↑</td><td>16%↑</td><td>-18%↑</td><td>-77%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>26-Apr-26</td><td>23,318</td><td>-7%↓</td><td>10%↓</td><td>1%↑</td><td>-60%↑</td><td>4,297</td><td>6%↑</td><td>15%↑</td><td>11%↑</td><td>-23%↑</td><td>13,879</td><td>-6%↓</td><td>8%↓</td><td>4%↑</td><td>-60%↑</td><td>5,142</td><td>-16%↓</td><td>11%↓</td><td>-10%↑</td><td>-73%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>3-May-26</td><td>21,384</td><td>-4%↑</td><td>-8%↓</td><td>-4%↓</td><td>-65%↓</td><td>4,223</td><td>12%↑</td><td>-2%↓</td><td>6%↓</td><td>-14%↑</td><td>12,503</td><td>3%↑</td><td>-10%↓</td><td>2%↓</td><td>-66%↓</td><td>4,658</td><td>-25%↓</td><td>-9%↓</td><td>-22%↓</td><td>-75%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>10-May-26</td><td>20,449</td><td>-2%↑</td><td>-4%↑</td><td>-2%↑</td><td>-67%↓</td><td>3,523</td><td>2%↓</td><td>-17%↓</td><td>6%↓</td><td>-29%↓</td><td>12,116</td><td>3%↑</td><td>-3%↑</td><td>3%↑</td><td>-68%↓</td><td>4,810</td><td>-15%↑</td><td>3%↑</td><td>-18%↑</td><td>-76%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>17-May-26</td><td>24,282</td><td>3%↑</td><td>19%↑</td><td>-2%↓</td><td>-62%↑</td><td>4,874</td><td>22%↑</td><td>38%↑</td><td>11%↑</td><td>-17%↑</td><td>13,822</td><td>4%↑</td><td>14%↑</td><td>1%↓</td><td>-64%↑</td><td>5,586</td><td>-10%↑</td><td>16%↑</td><td>-17%↑</td><td>-72%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>24-May-26</td><td>24,411</td><td>-10%↓</td><td>1%↓</td><td>-3%↓</td><td>-65%↓</td><td>5,032</td><td>11%↓</td><td>3%↓</td><td>12%↑</td><td>-18%↓</td><td>13,964</td><td>-11%↓</td><td>1%↓</td><td>-1%↓</td><td>-68%↓</td><td>5,415</td><td>-22%↓</td><td>-3%↓</td><td>-18%↓</td><td>-73%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>31-May-26</td><td>31,094</td><td>14%↑</td><td>27%↑</td><td>1%↑</td><td>-53%↑</td><td>5,784</td><td>28%↑</td><td>15%↑</td><td>16%↑</td><td>9%↑</td><td>17,992</td><td>15%↑</td><td>29%↑</td><td>3%↑</td><td>-55%↑</td><td>7,318</td><td>2%↑</td><td>35%↑</td><td>-11%↑</td><td>-65%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>7-Jun-26</td><td>21,851</td><td>17%↑</td><td>-30%↓</td><td>5%↑</td><td>-66%↓</td><td>3,572</td><td>1%↓</td><td>-38%↓</td><td>16%↓</td><td>-29%↓</td><td>13,011</td><td>31%↑</td><td>-28%↓</td><td>8%↑</td><td>-67%↓</td><td>5,268</td><td>0%↓</td><td>-28%↓</td><td>-8%↑</td><td>-74%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>14-Jun-26</td><td>19,881</td><td>-7%↓</td><td>-9%↑</td><td>3%↓</td><td>-69%↓</td><td>3,188</td><td>-2%↓</td><td>-11%↑</td><td>11%↓</td><td>-40%↓</td><td>12,051</td><td>-2%↓</td><td>-7%↑</td><td>6%↓</td><td>-69%↓</td><td>4,642</td><td>-19%↓</td><td>-12%↑</td><td>-10%↓</td><td>-76%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>21-Jun-26</td><td>20,899</td><td>-23%↓</td><td>5%↑</td><td>-1%↓</td><td>-73%↓</td><td>3,447</td><td>-11%↓</td><td>8%↑</td><td>5%↓</td><td>-56%↓</td><td>13,511</td><td>-15%↓</td><td>12%↑</td><td>5%↓</td><td>-71%↓</td><td>3,941</td><td>-46%↓</td><td>-15%↓</td><td>-17%↓</td><td>-83%↓</td><td></td><td></td><td></td><td></td></tr></table>

Source: CREIS.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

## 4. Mainland China – Weekly secondary sales registrations

Figure 7: 12-city daily secondary sales registrations (二手网签)  
![](images/90533d0fea4223e7cc20bfda78727e14303567cf638afc71fcfb1e0d8222103f.jpg)  
Source: Wind.  
Note: The decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 8: 12-city secondary sales registrations (二手网签) 7-day moving average  
Secondar

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and

should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
