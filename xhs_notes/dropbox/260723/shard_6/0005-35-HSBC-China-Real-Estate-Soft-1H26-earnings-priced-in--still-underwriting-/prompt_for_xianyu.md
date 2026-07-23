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
# China Real Estate

Soft 1H26 earnings priced in: still underwriting the 2027 recovery

\- Yuexiu's profit warning proved a non-event; expectations were already reset

\- K-shaped recovery and market consolidation underpin our expectation of a broad earnings recovery from 2027

\- Prefer Buy-rated CRL and C&D, both offering more resilient earnings profile (p.2)

1H26 earnings preview. On 17 July, Yuexiu Property announced a profit alert, expecting 1H26 core net profit to decline by c90–95% y-o-y, citing lower revenue recognition from contracted sales, weaker JV contributions, and continued margin pressure – factors we also expect to see across other developers. Its share price was up 1.6% on 20 July (vs HSI: +2.4%), reflecting these factors have been priced in. We expect developers to record more impairment provisions and lower margins for sold inventories in 1H26 or even the full year, but the sector's earnings recovery theme remains intact (Catch me if you can: the market's already in 2027, 8 April 2026), given narrowing home price decline and reduced destocking pressure.

Capitalising on the K-shaped recovery. Primary sales stayed soft through early summer, partly due to an unusually rainy season across many eastern cities. That said, the K-shaped recovery remains largely undisturbed. On the mass-market side, secondary transactions MTD are up \~7% y-o-y in 10 cities (Figure 3), pointing to improving resale liquidity. Together with better affordability, this could help attract household savings back into housing without a meaningful leverage-up, against tighter cross-border capital controls and limited higher-yielding onshore alternatives. Into 2H, an easier base leaves room for upside surprises. At the premium end, demand remains resilient, with record luxury transactions in Hangzhou in 1H26 and strong recent launches (Figure 4) underscoring appetite for luxury products.

## Market share gains remain concentrated among leaders. In 1H26, Top 10

developers' market share rose \~1ppt y-o-y from 2025, while Top 50's was broadly flat (Figure 5), signalling ongoing consolidation and widening divergence. We believe developers with stronger product capabilities and premium land banks are best positioned to monetise upgrader demand. CRL, COLI and Jinmao continue to gain share alongside meaningful ASP uplift, reflecting a higher mix of premium launches. For retail landlords, despite soft retail sales, the total share of our covered names in national retail sales almost doubled from 2021 to 2025 (Figure 6). Though valuation upside may still be capped by subdued sentiment, earnings visibility supports our positive stance.

Preferred picks. We continue to see greater upside surprise potential for residential developers, favouring CRL and C&D (both Buy-rated) for their leading position in high-end projects and stronger earnings visibility. We expect both companies to have more resilient 1H26 results although they are not immune from the sector headwinds.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Equities REMD

China

## Michelle Kwok\*

Head of Asia Real Estate and HK Equity Research
The Hongkong and Shanghai Banking Corporation Limited
michellekwok@hsbc.com.hk
+852 2996 6918

## Oliver Yu\*

Analyst, Asia Real Estate
The Hongkong and Shanghai Banking Corporation Limited
oliver.y.o.x.yu@hsbc.com.hk
+852 2288 2050

## Stephen Wang\*, CFA

Analyst, Asia Real Estate
The Hongkong and Shanghai Banking Corporation Limited
stephen.wang@hsbc.com.hk
+852 2284 1675

## Brian Yu\*

Associate, Asia Real Estate Research
The Hongkong and Shanghai Banking Corporation Limited
brian.d.yu@hsbc.com.hk
+852 28227281

Charlotte Ye\*  
Associate Guangzhou

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

No country for bears

The $24^{\text{th}}$ edition of the EM Sentiment Survey Click to view

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

View HSBC Global Investment Research at: https://www.research.hsbc.com

## 1H26 results preview

Yuexiu Property's profit alert on 17 July is part of a broader trend: several developers have guided to sharp net profit declines or potential net losses, including China Merchants Shekou (001979 CH, Not Rated) and Huafa Properties (600325 CH, Not Rated). In our view, the market has largely priced in the potentially weak 1H26 and FY26 results, with attention shifting to a more meaningful earnings recovery from 2027 onwards as the drag from falling home prices eases. We expect most developers to face similar pressures:

◆ Development Property (DP) revenue contraction: With contracted sales declining through 2023-25, revenue recognition is likely to fall materially over 2026-28.

\- Margin compression: Continued home price declines and inventory destocking should drive further impairment provisions and lower margins on completed homes sales, weighing on gross margins.

\- Lower JV contribution: Profit shares from jointly developed projects are also likely to weaken amid ongoing sector headwinds.

## Two standouts – CRL and C&D

On stock level, select developers will lead in this earnings recovery cycle - we expect CRL and C&D to have more resilient results.

CRL (Buy): DP challenges partially offset by IP strength. 1H26 gross rental income rose $13\%$ y-o-y (based on monthly announcements), helping to cushion softer DP revenue. High shopping mall margins (FY25: $77\%$ ) should further mitigate DP margin pressure. In addition, a $>RMB2bn$ revaluation gain (vs RMB10bn 1H25 core profit) related to the Chengdu Mixc mall spin-off which we expect to be recognised in 1H26 could alleviate earnings pressure.

C&D (Buy): Supported by a younger landbank. We expect earnings to be stable or decline modestly in 1H26, underpinned by lower impairment risk from a relatively young landbank and less urgency to destock completed homes.

On the other hand, we expect COLI (Buy) and China Jinmao (Hold) to face tougher comparisons given their stronger 1H25 earnings versus 2H25. For Yuexiu Property (Buy), we reckon there are downside risks to our current 2026 forecasts given ongoing margin pressure. We will reassess potential impairment risk after the 1H26 results, as this remains difficult to quantify at this stage. That said, given the low earnings base in 2025 (RMB260m), we still see scope for a meaningful uplift in 2026 earnings.

Figure 1: Key developers' 1H/2H net profit split in 2025  
![](images/a0c6095a13c2e0caf7335c30284bcb438e60f5075bc58e4fcae7af2c36ac8063.jpg)  
Source: Company data, HSBC

Figure 2: Earnings profile of developers

<table><tr><td rowspan="2"></td><td colspan="3">GPM</td><td colspan="3">Core earnings (RMBm)</td><td colspan="3">y-o-y growth</td><td colspan="3">vs consensus</td></tr><tr><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2026</td><td>2027</td><td>2028</td></tr><tr><td>CRL</td><td>23%</td><td>24%</td><td>25%</td><td>23,720</td><td>25,165</td><td>27,085</td><td>6%</td><td>6%</td><td>8%</td><td>-1%</td><td>0%</td><td>1%</td></tr><tr><td>C&amp;D Int&#x27;l</td><td>15%</td><td>15%</td><td>16%</td><td>4,443</td><td>4,767</td><td>5,192</td><td>23%</td><td>7%</td><td>9%</td><td>22%</td><td>19%</td><td>19%</td></tr><tr><td>COLI</td><td>16%</td><td>16%</td><td>17%</td><td>11,892</td><td>12,718</td><td>13,593</td><td>-9%</td><td>7%</td><td>7%</td><td>-6%</td><td>-4%</td><td>-4%</td></tr><tr><td>China Jinmao</td><td>16%</td><td>16%</td><td>16%</td><td>677</td><td>720</td><td>809</td><td>-3%</td><td>6%</td><td>12%</td><td>-53%</td><td>-55%</td><td>-54%</td></tr><tr><td>Greentown</td><td>12%</td><td>12%</td><td>13%</td><td>673</td><td>1,792</td><td>3,108</td><td>n.m.</td><td>166%</td><td>73%</td><td>-9%</td><td>36%</td><td>79%</td></tr><tr><td>Yuexiu</td><td>10%</td><td>11%</td><td>12%</td><td>1,041</td><td>1,637</td><td>2,776</td><td>301%</td><td>57%</td><td>70%</td><td>134%</td><td>124%</td><td>151%</td></tr></table>

Source: Bloomberg, HSBC estimates

Figure 3: Secondary sales continue the momentum in June-July

<table><tr><td>No. of units</td><td>Shanghai</td><td>Beijing</td><td>Shenzhen</td><td>Chengdu</td><td>Hangzhou</td><td>Nanjing</td><td>Foshan</td><td>Suzhou</td><td>Dongguan</td><td>Xiamen</td><td>Average</td></tr><tr><td>June 2026</td><td>25,158</td><td>18,757</td><td>6,357</td><td>20,695</td><td>4,261</td><td>7,542</td><td>7,564</td><td>7,351</td><td>4,261</td><td>4,201</td><td></td></tr><tr><td>June 2025</td><td>20,774</td><td>16,838</td><td>5,494</td><td>19,214</td><td>4,174</td><td>7,459</td><td>6,595</td><td>5,757</td><td>4,174</td><td>3,537</td><td></td></tr><tr><td>June y-o-y</td><td>21%</td><td>11%</td><td>16%</td><td>8%</td><td>2%</td><td>1%</td><td>15%</td><td>28%</td><td>2%</td><td>19%</td><td>14%</td></tr><tr><td>1-19 July 2026</td><td>14,459</td><td>8,576</td><td>3,695</td><td>11,948</td><td>2,250</td><td>3,907</td><td>5,655</td><td>4,079</td><td>2,250</td><td>2,496</td><td></td></tr><tr><td>1-19 July y-o-y</td><td>25%</td><td>4%</td><td>-1%</td><td>-1%</td><td>-7%</td><td>-8%</td><td>24%</td><td>20%</td><td>-7%</td><td>7%</td><td>7%</td></tr></table>

Source: Municipal housing bureaus, Wind, HSBC

Figure 4: June-July luxury projects in key cities with solid sell-through

<table><tr><td>Project</td><td>Project (English)</td><td>Developer</td><td>Latest launch date</td><td>No. of unit offerings</td><td>AV (RMB/sqm)</td><td>ASP (RMB/sqm)</td><td>Unit price (RMBm)</td><td>Sell-through rate</td></tr><tr><td colspan="9">Shanghai</td></tr><tr><td>陆家嘴太古源源邸</td><td>LujiazuiTaikoo Yuan Residences</td><td>Swire &amp; Lujiazui</td><td>12-Jun-26</td><td>72</td><td>113,000</td><td>191,800</td><td>24-190</td><td>97%</td></tr><tr><td>保利·外滩曜</td><td>Eternal Bud</td><td>Poly Development</td><td>30-Jun-26</td><td>103</td><td>95,500</td><td>145,200</td><td>17-24</td><td>57%</td></tr><tr><td>中海云锦华庭</td><td>Yunjin Huating</td><td>COLI</td><td>09-Jul-26</td><td>44</td><td>148,503</td><td>232,600</td><td>50-154</td><td>70%</td></tr><tr><td>嘉佰道·徐汇</td><td>CATANIA Xuhui</td><td>Cityscape Development</td><td>11-Jul-26</td><td>91</td><td>126,011</td><td>188,600</td><td>17-130</td><td>98%</td></tr><tr><td colspan="9">Shenzhen</td></tr><tr><td>中海安缇雅苑</td><td>Antee Bay</td><td>COLI</td><td>30-Jun-26</td><td>72</td><td>77,400</td><td>185,800</td><td>40-107</td><td>100%</td></tr><tr><td colspan="9">Beijing</td></tr><tr><td>保利熙瑞</td><td>Poly Xirui</td><td>Poly Development</td><td>27-Jun-26</td><td>157</td><td>78,400</td><td>125,000</td><td>15-41</td><td>69%</td></tr><tr><td colspan="9">Hangzhou</td></tr><tr><td>望天际</td><td>One Beyond</td><td>Binjiang/C&amp;D/Jinmao</td><td>17-Jul-26</td><td>66</td><td>77,409</td><td>142,346</td><td>25-152</td><td>100%</td></tr></table>

Source: CREIS, Fang.com, HSBC

Figure 5: Selected high-quality developers (i.e. CRL, COLI & Jinmao) market share rose c.1ppt from 2025 to 1H26  
![](images/51f6dfec6a62627669192fa5df390f24f29414f2e1a451a9087cc01fcea7f759.jpg)  
Source: CRIC, NBS, HSBC  
Note: Top 5/10/50 developers in terms of property sales value

Figure 6: The market share of our covered retail landlords almost doubled from 2021

<table><tr><td></td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>CRL</td><td>0.24%</td><td>0.26%</td><td>0.35%</td><td>0.40%</td><td>0.48%</td></tr><tr><td>Seazen</td><td>0.12%</td><td>0.13%</td><td>0.16%</td><td>0.19%</td><td>0.19%</td></tr><tr><td>Longfor</td><td>0.11%</td><td>0.10%</td><td>0.13%</td><td>0.15%</td><td>0.16%</td></tr><tr><td>Total as of national retail sales</td><td>0.47%</td><td>0.48%</td><td>0.64%</td><td>0.74%</td><td>0.84%</td></tr></table>

Source: Wind, company data, HSBC

## Valuation charts

Figure 7: SOE developers' forward PE (x)  
![](images/465b9d71eda4769c0bcf3d5a6411c25a534d5885835abf7ee97f63884fa46f77.jpg)  
Note: The average forward PE multiples of COLI, CRL, Vanke, Greentown, Yuexiu, C&D Int'l, and Longfor are based on Bloomberg consensus.
Source: Bloomberg, HSBC estimates

Figure 8: SOE developers' NAV discount (%)  
![](images/a4b4561e9e204caabcc1d9beaedcf82dbde167b6443c4baa83a8c31c4d310520.jpg)  
Source: Bloomberg, HSBC estimates

Figure 9: 2026 y-t-d share price performance  
![](images/b1af09daf752c9855bf1c52b82d0e87371dbb1f2f4438a0f3cc446cfcbf93809.jpg)  
Note: Priced as of 20 July 2026.
Source: Bloomberg, HSBC.

Figure 10: SOE developers' trailing PB (x)  
![](images/18becf0e08d16753ec7b3807ab1ced91cc632f209ac389ef68654bde80204e46.jpg)  
Note: The average trailing PB multiples of COLI, CRL, Vanke, Greentown, Yuexiu, and C&D International are based on monthly data.
Source: Bloomberg, HSBC.

Figure 11: Valuation summary

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Share price (HKD)</td><td rowspan="2">Target price (HKD)</td><td rowspan="2">Mkt cap (USDbn)</td><td rowspan="2">3M ADTV (USDm)</td><td rowspan="2">NAV (HKD/sh)</td><td rowspan="2">(Disc)/ Prem (%)</td><td colspan="3">PE (x)</td><td rowspan="2">Yield (%) 2026e</td><td rowspan="2">PB (x) 2025a</td><td rowspan="2">Net gearing (%)</td></tr><tr><td>2025a</td><td>2026e</td><td>2027e</td></tr><tr><td colspan="15">Property developers</td></tr><tr><td>C&amp;D Int&#x27;l</td><td>1908 HK</td><td>Buy</td><td>14.45</td><td>19.90</td><td>4.3</td><td>14.8</td><td>42.4</td><td>(66)</td><td>7.1</td><td>6.3</td><td>5.9</td><td>7.9</td><td>0.6</td><td>25</td></tr><tr><td>COLI</td><td>688 HK</td><td>Buy</td><td>13.66</td><td>16.50</td><td>19.1</td><td>64.6</td><td>25.7</td><td>(47)</td><td>9.9</td><td>10.9</td><td>10.2</td><td>3.5</td><td>0.3</td><td>33</td></tr><tr><td>CR Land</td><td>1109 HK</td><td>Buy</td><td>34.48</td><td>43.80</td><td>31.4</td><td>120.1</td><td>55.5</td><td>(38)</td><td>9.5</td><td>9.0</td><td>8.5</td><td>4.1</td><td>0.7</td><td>39</td></tr><tr><td>China Vanke</td><td>2202 HK</td><td>Reduce</td><td>2.44</td><td>2.50</td><td>5.2</td><td>8.4</td><td>5.9</td><td>(59)</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>-</td><td>0.3</td><td>108</td></tr><tr><td>CIFI</td><td>884 HK</td><td>Hold</td><td>0.04</td><td>0.08</td><td>0.1</td><td>0.5</td><td>0.5</td><td>(93)</td><td>n.m.</td><td>n.m.</td><td>n.m.</td><td>-</td><td>0.0</td><td>81</td></tr><tr><td>Country Garden</td><td>2007 HK</td><td>Hold</td><td>0.18</td><td>0.30</td><td>1.1</td><td>10.4</td><td>1.9</td><td>(91)</td><td>1.3</td><td>n.m.</td><td>n.m.</td><td>-</td><td>n.m.</td><td>n.m.</td></tr><tr><td>China Jinmao</td><td>817 HK</td><td>Hold</td><td>1.38</td><td>1.50</td><td>2.4</td><td>11.5</td><td>3.5</td><td>(61)</td><td>23.0</td><td>23.8</td><td>22.4</td><td>1.5</td><td>0.4</td><td>76</td></tr><tr><td>Greentown China</td><td>3900 HK</td><td>Hold</td><td>7.37</td><td>9.50</td><td>2.4</td><td>11.6</td><td>17.9</td><td>(59)</td><td>n.m.</td><td>24.1</td><td>9.0</td><td>1.9</td><td>0.5</td><td>65</td></tr><tr><td>Longfor</td><td>960 HK</td><td>Hold</td><td>6.71</td><td>8.60</td><td>6.1</td><td>20.8</td><td>25.4</td><td>(74)</td><td>n.m.</td><td>31.5</td><td>11.6</td><td>1.0</td><td>0.2</td><td>48</td></tr><tr><td>Seazen</td><td>1030 HK</td><td>Buy</td><td>1.42</td><td>3.00</td><td>1.3</td><td>5.4</td><td>7.4</td><td>(81)</td><td>22.8</td><td>6.5</td><td>4.7</td><td>-</td><td>0.2</td><td>59</td></tr><tr><td>Shenzhen Inv</td><td>604 HK</td><td>Hold</td><td>0.69</td><td>0.70</td><td>0.8</td><td>0.8</td><td>2.2</td><td>(69)</td><td>12.3</td><td>20.6</td><td>13.4</td><td>-</td><td>0.2</td><td>91</td></tr><tr><td>Yanlord (SGD)</td><td>YLLG SP</td><td>Hold</td><td>0.65</td><td>0.53</td><td>1.0</td><td>1.9</td><td>1.6<

[中间内容因长度限制已省略]

es Commission and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.
"""
