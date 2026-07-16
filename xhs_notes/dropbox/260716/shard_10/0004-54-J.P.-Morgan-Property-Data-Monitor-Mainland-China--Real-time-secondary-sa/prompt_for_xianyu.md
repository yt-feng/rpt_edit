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

Mainland China: Real-time secondary sales moderated; HK: Link REIT starts buyback

## Mainland China

\- Iceberg 10-city real-time secondary weekly sales (冰山指数实时二手成交) rose $2\%$ Y/Y (last week: $+11\%$ ). Tier-1 cities' weekly sales grew $4\%$ Y/Y (prior: $+8\%$ Y/Y) (Table 1), with Shanghai outperforming $(+8\%$ Y/Y). Real-time sales generally lead the trend of official sales registrations by a few weeks.

\- Iceberg 10-city secondary listings (冰山指数二手挂牌量) mildly rose $0.1\%$ W/W. Tier-1 cities' listings dropped $0.2\%$ W/W, driven by $-1.4\%$ W/W in Shenzhen and $-0.1\%$ W/W in Shanghai (Table 2). The volume of secondary listings in tier-1 cities has been consistently coming down (down $3.8\%$ from the peak in March), and this is a key factor that supports price stabilization.

\- 60-city primary sales registrations (一手网签) rose 10% Y/Y (last week: +20% Y/Y) (more).

\- 12-city secondary sales registrations (二手网签) rose $10\%$ Y/Y (Figure 7) (last week: $+12\%$ ). YTD, 12-city secondary sales have risen $5\%$ Y/Y (Shanghai: $+15\%$ ).

\- The Centraline tier-1 cities' secondary asking price index dropped from 16.6 to 16.3 (Figure 3).

\- The Centaline secondary manager confidence index dropped from 55 to 52 (Figure 4).

\- Southbound holdings rose 0.33% W/W (Table 7): China Jinmao +1.4%; CR Land +0.7%.

\- Share price moves (Figure 16): The sector rose 1% last week, underperforming the HSI (+3%). The outperformers were COLI and Sunac Services (both +4%). The underperformers were Shimao (-19%) and Sunac (-10%).

• JPM top picks: COLI, CR Land, Jinmao & CR Mixc.

## Hong Kong SAR

\- Link REIT starts unit buyback: Link REIT bought back 1.6 and 0.6mn units on 9 and 10 July respectively, totalling HK\$83mn, equivalent to 5.6% of the HK\$1.5bn proceeds from the disposal of Swing By @ Thompson Plaza. Assuming Link REIT deploys the full proceeds towards buybacks, based on the last close, this would reduce the unit count by 1.6%, potentially more than offsetting the dilution impact of the scrip dividend (we estimate 0.6% dilution if 9% of DPU is paid through scrip, referencing the average scrip dividend election % in the last two semi-annual results).

\- The home price index fell 0.8% W/W (Figure 12), the steepest decline year-to-date. Home prices have risen 11% YTD, already reaching our full-year target of 10-15%. We expect slower price growth of <5% in 2H26. For more discussion, please see our report HK Residential Property: Home prices already hit our full-year target; momentum may slow in 2H.

\- SHKP released the price lists of Garden Regency (in Kam Tin). The first price list (120 units) is priced at HK\$14.0K, 21% above nearby secondary

## Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC
(852) 2800-8513
karl.chan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Venus Choi
(852) 2800-8599
venus.choi@JPM.com
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

## Shirley Yau

(852) 2800-0566
shirley.yau@JPM.com
JPM Securities (Asia Pacific) Limited

See page 20 for analyst certification and important disclosures, including non-US analyst disclosures.

projects. The second price list (60 units) is priced at HK\$13.2K psf, 6% lower than the first price list (due to differences in floor levels and views), or 14% above secondary. The project will be launched for sale on 18 July (Sat). The first two price lists are currently 21x over-subscribed (as of 13 July), and we expect a decent >90% sell-through rate, especially due to the low lump sum (HK\$4-5 million) which is likely to be attractive to first-home buyers.

\- Secondary transactions in the top 35 estates totaled 39 units, +11% W/W or -53% Y/Y (Figure 11).

\- The Centa-Salesman Index (CSI) (Figure 14) moderated from 64.5 last week to 63.3. A reading of $>50 =$ sentiment is positive and property prices are likely to rise.

\- The Centaline Valuation Index (CVI) (Figure 13) marginally rose from 81.6 last week to 81.8.

\- Southbound holdings marginally rose 0.3% W/W (Table 7): Swire Prop +0.18%; Henderson +0.17%.

\- Share price moves (Figure 17): The sector rose 1% last week, underperforming the HSI (+3%). The outperformers were CK Hutchison (+6%), Wharf REIC and Swire Pacific (both +5%). The underperformer was Kerry Prop (-3%).

JPM top picks: landlords - Link REIT & Swire Prop; developers - CKA & Sino; conglomerates - CKH & JM

## Credit View (by Alvin Au)

\- The JACI China HY Property index rose 0.36% last week (vs China HY: +0.1%), bringing YTD returns to 5.86%.

\- Vanke: Vanke released a profit warning last week, and expects a core net loss of Rmb11-14bn in 1H26. This implies net losses have widened from Rmb5.3bn in 1Q26 to Rmb7.2bn in 2Q (based on the mid-point of the quoted 1H26 range), due to (1) a decline in DP bookings and lower gross margins, and (2) additional impairment provisions, etc (see equity report for details). We note that Vanke has been extending onshore maturities with a $40\%$ upfront payment, and its debt maturity wall will become lighter in 2H26 after July (Rmb2bn due), with only Rmb3.4bn due in Dec 2026 (extended from Dec 2025 maturity).

\- GLP: GLP China signed a strategic cooperation agreement with the Ulanqab government to develop a phased, multi-GW hyperscale/AI-ready data center campus in Inner Mongolia (\~1.33m sqm). This marks the company's second partnership with a local government – it partnered with the Zhejiang government for a Rmb2.5bn investment in August 2025. We see this as credit-positive and another signal that GLP is not in distress, and we maintain OW on GLPSP '28s (86.5 offer, 18.7% ytw) and GLPCHI '29s (87.2 offer, 13.4% ytw).

JPM top picks: LNGFOR '29s (84.2 offer, 9.9% ytm) and SHUION '29s (101.3 offer, 9.1% ytm).

## Table Of Contents

Mainland China.... 1
Hong Kong SAR.... 1
Credit View (by Alvin Au).... 2
1. Mainland China – real-time secondary sales & listings .... 4
2. Mainland China – leading indicators from Centraline.... 6
3. Mainland China – Weekly primary sales registrations .... 7
4. Mainland China – Weekly secondary sales registrations. .... 8
5. Hong Kong – Residential market update .... 9
6. Hong Kong – Tourist arrivals and resident departures .... 12
7. Share price update .... 13
8. Credit recommendations .... 17
9. Equity valuation summary .... 18

## 1. Mainland China – real-time secondary sales & listings

Table 1: Iceberg 10-city real time secondary weekly sales 冰山指数实时二手每周成交 (十大城市)

<table><tr><td rowspan="2">Week ending</td><td colspan="6">No. of units</td><td colspan="6">Y/Y</td><td colspan="6">4-week rolling Y/Y</td></tr><tr><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>10-city</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>10-city</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>10-city</td></tr><tr><td>14-Jun-26</td><td>3,980</td><td>5,580</td><td>2,416</td><td>1,126</td><td>13,102</td><td>29,372</td><td>16%</td><td>18%</td><td>8%</td><td>0%</td><td>14%</td><td>13%</td><td>17%</td><td>15%</td><td>19%</td><td>19%</td><td>16%</td><td>16%</td></tr><tr><td>21-Jun-26</td><td>3,288</td><td>4,528</td><td>1,881</td><td>1,011</td><td>10,708</td><td>25,055</td><td>1%</td><td>-5%</td><td>-4%</td><td>-6%</td><td>-3%</td><td>0%</td><td>14%</td><td>10%</td><td>14%</td><td>14%</td><td>12%</td><td>13%</td></tr><tr><td>28-Jun-26</td><td>3,517</td><td>6,735</td><td>2,025</td><td>1,180</td><td>13,457</td><td>28,706</td><td>3%</td><td>46%</td><td>-1%</td><td>15%</td><td>21%</td><td>18%</td><td>10%</td><td>18%</td><td>5%</td><td>10%</td><td>13%</td><td>12%</td></tr><tr><td>5-Jul-26</td><td>3,433</td><td>4,594</td><td>2,262</td><td>1,170</td><td>11,459</td><td>26,498</td><td>15%</td><td>4%</td><td>4%</td><td>14%</td><td>8%</td><td>11%</td><td>9%</td><td>16%</td><td>2%</td><td>6%</td><td>10%</td><td>11%</td></tr><tr><td>12-Jul-26</td><td>3,125</td><td>5,053</td><td>1,956</td><td>957</td><td>11,091</td><td>25,153</td><td>3%</td><td>8%</td><td>1%</td><td>-6%</td><td>4%</td><td>2%</td><td>5%</td><td>13%</td><td>0%</td><td>4%</td><td>8%</td><td>8%</td></tr></table>

Source: Iceberg Index  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 1: Iceberg 10-city real time secondary daily sales 冰山指数实时二手每日成交 (十大城市)  
![](images/5bd7c04f74f08e25ddb1c89bb8078ee337dfed783329d0e712e3f5c8d791639a.jpg)  
Source: Iceberg Index

Table 2: Iceberg 10-city secondary listing volume 冰山指数二手挂牌量 (十大城市)

<table><tr><td rowspan="2">Week ending</td><td colspan="6">No. of secondary listings (&#x27;000 units)</td><td colspan="6">W/W</td></tr><tr><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>10-city</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>10-city</td></tr><tr><td>14-Jun-26</td><td>119</td><td>84</td><td>137</td><td>89</td><td>429</td><td>1,559</td><td>-0.1%</td><td>-0.5%</td><td>0.0%</td><td>0.4%</td><td>-0.1%</td><td>0.2%</td></tr><tr><td>21-Jun-26</td><td>119</td><td>83</td><td>137</td><td>89</td><td>428</td><td>1,556</td><td>-0.1%</td><td>-1.1%</td><td>-0.1%</td><td>-0.4%</td><td>-0.3%</td><td>-0.1%</td></tr><tr><td>28-Jun-26</td><td>120</td><td>82</td><td>137</td><td>86</td><td>425</td><td>1,556</td><td>0.2%</td><td>-0.3%</td><td>0.2%</td><td>-2.9%</td><td>-0.6%</td><td>0.0%</td></tr><tr><td>5-Jul-26</td><td>119</td><td>82</td><td>137</td><td>84</td><td>423</td><td>1,553</td><td>-0.3%</td><td>-0.6%</td><td>0.1%</td><td>-2.1%</td><td>-0.6%</td><td>-0.2%</td></tr><tr><td>12-Jul-26</td><td>119</td><td>82</td><td>137</td><td>83</td><td>422</td><td>1,555</td><td>0.2%</td><td>-0.1%</td><td>0.1%</td><td>-1.4%</td><td>-0.2%</td><td>0.1%</td></tr></table>

Source: Iceberg Index

Figure 2: Iceberg tier-1 cities secondary listing volume 冰山指数二手挂牌量 (一线城市)  
No. of secondary listings ('000 units) - Tier 1 cities  
![](images/18dfe811fd998c7c5a0c2f8f3f25a609d459ba96e365f047d752499e2e04e81e.jpg)  
Source: Iceberg Index

# 2. Mainland China – leading indicators from Centraline

Figure 3: Centraline secondary asking price index vs NBS secondary home price index M/M in tier-1 cities  
![](images/d339f74420f0a4253c607a291085e4eeefd1b949525ec628ceb214b293151e87.jpg)  
Source: Centraline, Wind, NBS.  
Note: The asking price index represents the percentage of projects with home price increases. For example, an index of 20 means that 20% of projects raise prices (while 80% do not).  
Figure 4: Centraline secondary manager confidence index in tier-1 cities vs three-month rolling secondary sales

![](images/290849d0812f1e266bcfdea0bb4764ed26e21ed643b7451d0d89c666afe87173.jpg)  
Source: Centraline, Wind. Note: The index surveys managers across the country for their judgment on the market outlook.

# 3. Mainland China – Weekly primary sales registrations

Figure 5: 60-city weekly primary sales registrations (一手网签) – compared with 2019-24  
![](images/d3cfba8edab32fe512684e2947eb02fe118b1fd60d42820c345f0cb3fce3c39c.jpg)  
Source: CREIS.

Figure 6: 60-city weekly primary sales registrations (一手网签)  
![](images/57756dfc8a69e6535d9214a86e5fd86e07199496179d5f80f0375e5ed7dd39af.jpg)  
Source: CREIS.

Table 3: 60-city weekly primary sales registrations (一手网签) by tier

<table><tr><td rowspan="2">Week ending</td><td colspan="5">60-City</td><td colspan="5">Tier-1</td><td colspan="5">Tier-2</td><td colspan="5">Tier-3/4</td></tr><tr><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td></tr><tr><td>10-May-26</td><td>20,374</td><td>-2%↑</td><td>-4%↑</td><td>-2%↑</td><td>-68%↓</td><td>3,512</td><td>1%↓</td><td>-17%↓</td><td>6%↓</td><td>-29%↓</td><td>12,082</td><td>3%↑</td><td>-3%↑</td><td>3%↑</td><td>-68%↓</td><td>4,780</td><td>-15%↑</td><td>3%↑</td><td>-19%↑</td><td>-76%↓</td></tr><tr><td>17-May-26</td><td>24,212</td><td>3%↑</td><td>19%↑</td><td>-3%↓</td><td>-62%↑</td><td>4,877</td><td>22%↑</td><td>39%↑</td><td>11%↑</td><td>-17%↑</td><td>13,750</td><td>3%↑</td><td>14%↑</td><td>0%↓</td><td>-64%↑</td><td>5,585</td><td>-10%↑</td><td>17%↑</td><td>-17%↑</td><td>-72%↑</td></tr><tr><td>24-May-26</td><td>24,322</td><td>-11%↓</td><td>0%↓</td><td>-4%↓</td><td>-65%↓</td><td>5,030</td><td>11%↓</td><td>3%↓</td><td>12%↑</td><td>-18%↓</td><td>13,901</td><td>-11%↓</td><td>1%↓</td><td>-1%↓</td><td>-68%↓</td><td>5,391</td><td>-23%↓</td><td>-3%↓</td><td>-19%↓</td><td>-73%↓</td></tr><tr><td>31-May-26</td><td>31,283</td><td>14%↑</td><td>29%↑</td><td>1%↑</td><td>-52%↓</td><td>5,782</td><td>28%↑</td><td>15%↑</td><td>16%↑</td><td>9%↑</td><td>17,777</td><td>14%↑</td><td>28%↑</td><td>2%↑</td><td>-55%↑</td><td>7,724</td><td>7%↑</td><td>43%↑</td><td>-10%↑</td><td>-63%↑</td></tr><tr><td>7-Jun-26</td><td>21,718</td><td>16%↑</td><td>-31%↓</td><td>5%↑</td><td>-66%↓</td><td>3,666</td><td>3%↓</td><td>-37%↓</td><td>16%↑</td><td>-27%↓</td><td>12,798</td><td>29%↑</td><td>-28%↓</td><td>7%↑</td><td>-67%↓</td><td>5,254</td><td>0%↓</td><td>-32%↓</td><td>-6%↑</td><td>-74%↓</td></tr><tr><td>14-Jun-26</td><td>20,015</td><td>-6%↓</td><td>-8%↑</td><td>3%↓</td><td>-68%↓</td><td>3,570</td><td>10%↑</td><td>-3%↑</td><td>14%↓</td><td>-32%↓</td><td>11,697</td><td>-5%↓</td><td>-9%↑</td><td>5%↓</td><td>-70%↓</td><td>4,748</td><td>-17%↓</td><td>-10%↑</td><td>-8%↓</td><td>-75%↓</td></tr><tr><td>21-Jun-26</td><td>22,425</td><td>-17%↓</td><td>12%↑</td><td>1%↓</td><td>-71%↓</td><td>3,597</td><td>-7%↓</td><td>1%↑</td><td>9%↓</td><td>-54%↓</td><td>14,255</td><td>-10%↓</td><td>22%↑</td><td>5%↑</td><td>-69%↑</td><td>4,573</td><td>-37%↓</td><td>-4%↑</td><td>-12%↓</td><td>-80%↓</td></tr><tr><td>28-Jun-26</td><td>36,809</td><td>-8%↑</td><td>64%↑</td><td>-6%↓</td><td>-48%↑</td><td>5,076</td><td>-10%↓</td><td>41%↑</td><td>-2%↓</td><td>-12%↑</td><td>23,682</td><td>-7%↑</td><td>66%↑</td><td>-2%↓</td><td>-47%↑</td><td>8,051</td><td>-9%↑</td><td>76%↑</td><td>-17%↓</td><td>-59%↑</td></tr><tr><td>5-Jul-26</td><td>31,122</td><td>20%↑</td><td>-15%↓</td><td>-3%↑</td><td>-51%↓</td><td>4,231</td><td>0%↑</td><td>-17%↓</td><td>-3%↓</td><td>-19%↓</td><td>21,723</td><td>38%↑</td><td>-8%↓</td><td>3%↑</td><td>-44%↑</td><td>5,168</td><td>-14%↓</td><td>-36%↓</td><td>-19%↓</td><td>-73%↓</td></tr><tr><td>12-Jul-26</td><td>17,557</td><td>10%↓</td><td>-44%↓</td><td>-1%↑</td><td>-71%↓</td><td>2,967</td><td>23%↑</td><td>-30%↓</td><td>-2%↑</td><td>-36%↓</td><td>10,691</td><td>17%↓</td><td>-51%↓</td><td>6%↑</td><td>-71%↓</td><td>3,899</td><td>-12%↑</td><td>-25%↑</td><td>-18%↑</td><td>-79%↓</td></tr></table>

Source: CREIS.

## 4. Mainland China – Weekly secondary sales registrations

Figure 7: 12-city daily secondary sales registrations (二手网签)  
![](images/b6c69d4f828843c21e1dd9de8bc399678455c462f2207a12b386d272362ed613.jpg)  
Source: Wind.

Figure 8: 12-city secondary sales registrations (二手网签) 7-day moving average  
Secondary sales 7-day moving average - 12-city  
![](images/969db924a1b49fd84c08adb0e657bcdc0a91d02ed3d5b487d470eb3e8b1b765c.jpg)  
Source: Wind.

## 5. Hong Kong – Residential market update

Table 4: Hong Kong primary residential projects – Latest sell-through rates and upcoming launches

<table><tr><td>Project</td><td></td><td>Location</td><td>Developer</td><td>Launch Date</td><td>ASP (HK$ psf)</td><td>Total no. of units</td><td>Units launched</td><td>Units sold</td><td>Sell- through</td><td>vs. previous phase</td><td>vs. second

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
