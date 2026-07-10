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
# Metal Matters

# We expect copper price upside from September with medium-term bullish view intact.

## CITI'S TAKE

We publish April and May data for our global copper end-use consumption tracker. Negative headline implied y/y copper end-use growth reflects the distortive base effect of the policy-led spike in reported China renewable additions in 2Q'25. Implied growth in global copper end-use elsewhere has been tepid, but headline manufacturing sentiment remains robust. We expect renewed price upside from September and see copper touching \$15k/t within a year even as copper tariff dynamics and gold market headwinds threaten to limit gains through the summer (July and August).

Our conviction in near-term copper price direction is limited. We think copper will struggle to rally through the summer in our base case that US copper tariff fears fade and if bearish gold-price momentum is sustained — Our call for copper upside through June failed to materialise as a hawkish Fed surprised us, despite reliance versus June's broader commodity price pullback (e.g. gold, oil, aluminium). However, fading fears of potential Section 232 US tariffs on copper cathode risk weighing on sentiment in the coming weeks (given President Trump's end-June review deadline has passed and assuming our base case of no tariff announcement holds).

That said, we see positive price catalysts re-emerging from September including a more dovish Fed, greater focus on tighter copper physical market dynamics in 2027, and the structural medium-term bullish backdrop (please see our 114-slide Copper Book 2026 published late-June). We see copper averaging \$14,500/t through 4Q'26 as risks skew in our view towards a more dovish Fed on easing inflation and a softer US labour market, the potential for an eventual US-Iran deal, lower real interest rates, and a generally more supportive backdrop for demand and growth expectations.

Global manufacturing PMIs implied further expansion in activity in June, supported by AI-related investment and defence spending, despite softer sequential readings in the US and Europe. Resilience in manufacturing activity and these metal-intensive demand segments likely continue to support copper demand, a tailwind that our global end-use consumption tracker may be understating given it does not currently track these segments directly. Productivity gains from AI investment also have the potential to support copper pricing by supporting growth and quelling above-target inflation.

Headline implied global copper end-use declined by \~10% y/y in May'26, an anomaly due to the reporting spike in China renewable installations in May'25 (when GCET rose 13.5% y/y). Stripping out these distortions, underlying end-use appears tepid but resilient, with implied end-use growing \~1% y/y. Policy driven front-loading of China solar and wind installation reporting peaked in May'25 heavily distorting growth on a y/y comparison this year. Relying solely on headline copper-end use thus overstates the weakness in copper demand. Adjusting for solar/wind distortions, implied global copper end-use has risen 1.4% YTD vs a decline of 2.1% YTD on an unadjusted basis.

Tom Mulqueen $^{AC}$ +44-20-7986-4559
tom.mulqueen@citi.com

Shreyas Madabushi $^{AC}$ +91-22-4277-5048
shreyas.madabushi@citi.com

Maximilian J Layton $^{AC}$ +44-20-7986-4556
max.layton@citi.com

Wenyu Yao $^{AC}$ +44-20-7986-4551
wenyu.yao@citi.com

Kenny Hu, CFA $^{AC}$ +65-6657-3873
kenny.x.hu@citi.com

Ephrem Ravi $^{AC}$ +44-20-7986-2462
ephrem.ravi@citi.com

Jack Shang, CFA $^{AC}$ +852-2501-2441
jack.shang@citi.com

Alexander Hacking, CFA $^{AC}$ +1-212-816-6232
alex.hacking@citi.com

# Copper upside from September, medium-term bullish view intact

We expect renewed upside for copper prices after the summer as we look for prices to average \$14,500/t in 4Q'26 and to touch \$15k/t within a year. We think copper will struggle to rally sustainably through July and August given our expectation that the market will fade the tail risk of US import tariffs on cathodes over the coming months and given the potential for further bearish gold (and broader precious) price momentum near-term. By September, we see bullish catalysts re-emerging, including a more dovish Fed in response to softening US labour market conditions, a renewed focus on projected tighter physical copper market dynamics in 2027 and the structural copper bull case (see our 114-slide note published mid-June: Copper Book 2026 – Structural tailwinds and cyclical sensitivity pave path to \$15 k/t copper). We think lower real interest rates, an eventual and more sustainable US-Iran deal and a more supportive backdrop for demand and growth expectations should further improve sentiment towards copper later in the year.

Our base case remains that copper cathode will not be subject to a Section 232 US import tariff. We think the market will be inclined to fade the tail-risk of tariffs through the summer since more than a week has passed since the June $30^{\text{th}}$ review deadline without an announcement. The June 30th deadline set by President Trump last July for the review of Section 232 tariffs on copper cathode was over a week ago without any acknowledgement from the administration. Tariffs could still be announced in the coming weeks, but we don't think this is likely and we believe it is in the US administration's interest to maintain strategic ambiguity by neither implementing tariffs nor ruling them out. This can act as a headwind for copper pricing through July/August (more so for US copper prices given the current premium, Fig 1) if market participants opt to fade tariff tail risks although needs to be balanced against more bullish longer-term structural market themes and volatility in rates expectations around Fed comments and Strait of Hormuz developments.

Figure 1. We expect the COMEX premium over LME to ease further through July and August as tariff risk is faded (assuming our base case that no tariff is announced)  
![](images/594c1163be2e5bd5162888305fe7a11c4ec74ad7be767cc7e0ed42765d954803.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Bloomberg, CME Group, LME

Figure 2. China's copper-in-scrap imports close to flat y/y through to end-May suggested a muted global scrap response to much-higher copper prices.  
![](images/5526e2243fa37127b4bc7dea531d8131a97e92a6fa4a0750362334a515ce4248.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, TDM, China Customs, LME, Bloomberg

Broadly flat y/y China copper-in-scrap imports through May (Fig 2) despite much higher copper prices y/y imply a relatively price-inelastic scrap market.

Combined with flat mine supply anticipated in 2026, it suggests a very constrained supply-picture that can offset implied weakening of China demand growth this year. China's copper scrap imports were close to flat year-on-year through May, with April and May broadly in line with 2025 levels. Given the significantly higher copper price environment, the lack of a stronger import response suggests continued tightness in global scrap supply and a muted scrap availability response to price incentives. We see a balanced copper market in 2026 (Fig 3) swinging to a \~400kt deficit in 2027 basis current prices assuming a modest cyclical demand recovery, sustained energy transition and AI demand growth, versus around half-trend supply growth next year.

Figure 3. Citi copper supply and demand balance 2020-2030

<table><tr><td>kt Cu</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026f</td><td>2027f</td><td>2028f</td><td>2029f</td><td>2030f</td></tr><tr><td>Mine Production</td><td>20,752</td><td>21,179</td><td>21,808</td><td>22,395</td><td>23,128</td><td>23,398</td><td>23,334</td><td>23,739</td><td>24,509</td><td>25,272</td><td>25,880</td></tr><tr><td>% Change</td><td>0.7%</td><td>2.1%</td><td>3.0%</td><td>2.7%</td><td>3.3%</td><td>1.2%</td><td>-0.3%</td><td>1.7%</td><td>3.2%</td><td>3.1%</td><td>2.4%</td></tr><tr><td>Of Which Disr. Allowance (t)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>973</td><td>1,805</td><td>1,926</td><td>1,964</td><td>2,023</td></tr><tr><td>Of Which Disr. Allowance (%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>4.0%</td><td>7.1%</td><td>7.3%</td><td>7.2%</td><td>7.2%</td></tr><tr><td>Refined Production</td><td>23,591</td><td>24,374</td><td>25,067</td><td>25,561</td><td>26,450</td><td>27,300</td><td>27,505</td><td>27,866</td><td>28,716</td><td>29,557</td><td>30,248</td></tr><tr><td>% Change</td><td>-0.3%</td><td>3.3%</td><td>2.8%</td><td>2.0%</td><td>3.5%</td><td>3.2%</td><td>0.8%</td><td>1.3%</td><td>3.0%</td><td>2.9%</td><td>2.3%</td></tr><tr><td>Refined Consumption</td><td>23,103</td><td>24,769</td><td>24,841</td><td>25,704</td><td>26,311</td><td>26,943</td><td>27,522</td><td>28,267</td><td>28,820</td><td>29,446</td><td>29,928</td></tr><tr><td>% Change</td><td>-3.4%</td><td>7.2%</td><td>0.3%</td><td>3.5%</td><td>2.4%</td><td>2.4%</td><td>2.2%</td><td>2.7%</td><td>2.0%</td><td>2.2%</td><td>1.6%</td></tr><tr><td>End-Use Consumption</td><td>24,165</td><td>25,908</td><td>25,984</td><td>26,886</td><td>27,521</td><td>28,182</td><td>28,788</td><td>29,567</td><td>30,146</td><td>30,800</td><td>31,305</td></tr><tr><td>Surplus/Deficit</td><td>489</td><td>-395</td><td>226</td><td>-143</td><td>139</td><td>357</td><td>-18</td><td>-401</td><td>-104</td><td>111</td><td>320</td></tr><tr><td>Av. Price (US$/t ex-US)</td><td>6,183</td><td>9,318</td><td>8,830</td><td>8,485</td><td>9,145</td><td>9,950</td><td>13,700</td><td>14,250</td><td>14,000</td><td>14,000</td><td>14,000</td></tr></table>

\*Updated 12-Jun-26, forecast production and consumption basis current \~\$13.5k/t spot price

© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: Citi, Bloomberg, Wood Mackenzie, BGRIMM, IWCC, ICSG, Company Reports

## Global factory output expanding even as near-term outlook clouded by more hawkish Fed and geopolitical uncertainty

Global June PMI prints suggest expanding manufacturing activity (see Figure 4 and 5) across all major economies including China, US and Europe. This is generally a supportive signal for cyclical copper consumption even as investor's increased pricing-in of Fed rate hikes has weighed on sentiment in recent weeks. China's manufacturing PMI has nudged back into expansion with the latest prints coming at 50.3. Export orders continued to lead the recovery, with high-tech manufacturing outperforming old-economy sectors. Our China economists expect further imminent targeted easing but not a policy pivot. The July Politburo meeting is the next catalyst to watch from a China policy perspective.

European PMI implied manufacturing expansion for a fifth consecutive month while US prints suggest modest growth in activity. Although June prints edged down slightly versus May for both Europe and the US, activity was supported by supply-chain disruptions linked to the Middle East conflict as consumers accumulated inventory ahead of feared price rises. The US manufacturing sector continues to show momentum as the buildout of AI infrastructure remains a tailwind. In addition, defence spending is emerging as a likely contributor to activity. Our US economists expect manufacturing PMIs to remain in expansion this year as these tailwinds persist.

Figure 4. Copper fund positioning remains net bullish amid structural demand drivers, supply constraint, and improving PMIs now also imply support.  
![](images/8eefc2ba33a79c029879e406bf58dcccf1819971c96b0970aeb11b4cfbb02d38.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Bloomberg, LME, CME Group

Figure 5. Global PMIs in expansion in recent months amid supply-chain stockpiling on Middle East tensions and AI/Datacentre buildout  
![](images/8de0baa381cb1fd7cc7a4a90b945b9cdbcba2fedaeebc78fa154962b80f911d5.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, Rating Dog, Platts, Bloomberg, NBS, SMM

## China's renewables base effect negatively distorting tracked global copper end-use, otherwise growing but sluggish

Implied global copper end-use from our proprietary GCET tracker declined by \~10% y/y in May 2026. This largely reflects a statistical base effect stemming from comparison against a record reporting spike in China's renewables installations in May 2026. Aggregate demand across all other segments rose +1% y/y. The weak headline print is not surprising and is consistent with our expectations in prior publications, where we highlighted the outsized impact of policy- and trade-driven shifts in China's renewable installations last year. Notably, May 2025 saw implied copper end-use growth of \~13% y/y, driven by exceptionally strong reported China solar installations, with energy transition-related demand surging \~120% y/y. More normalised reported installations through 2Q'26 look far weaker by comparison. China's renewables installation reporting is an imperfect proxy for underlying copper consumption given the policy-sensitive volatility which must be acknowledged when interpreting implied y/y growth rates from our tracker. The base effect is likely to reverse and drive more positive implied growth in 2H'26.

Figure 6. China renewable power installations weigh on tracked copper end use growth y/y amid strong base effect  
![](images/f937fa8c8a017c1cd9a078a5de6b275f91b688f2a965eae05a2b151f1be37c83.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, ICA, Wood Mackenzie, Bloomberg

Figure 7. Global implied copper end-use grew \~1% y/y in May'26 after excluding consumption implied by China solar and wind reported capacity additions.  
![](images/09b0dd73e6c5ec5fcc32b0cd0b6c4a264df05c450e799f087ddf02de540404b4.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, ICA, Wood Mackenzie, Bloomberg

Figure 8. Total implied copper end-use (based on our tracker) annualizing at 27Mt  
![](images/53764580245a7949bb73d3940374600d54448b4e57139bf2331c230016b3de0c.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

Figure 9. Weaker China implied copper end-use due to statistical effects weighs on global implied copper end-use  
![](images/95b7233d17fdb5478fe807f4e8e89e498abd7c3402999da391cfee40556d8b00.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

China's weak headline copper end-use (as implied by our tracker) has been the primary drag on global consumption. China's copper end-use declined by \~17% y/y in May 2026. However, adjusting for distortions from the renewable sector, the underlying picture (see Figure 8) is more stable. Excluding solar and wind installations, China's copper end-use grew by \~0.6% y/y, indicating modest resilience in broader industrial demand. The key drag remains the sharp slowdown in renewable installations. China installed \~8.7GW of solar capacity in May—the lowest monthly run-rate this year—compared to an outsized \~93GW in May 2025. Similarly, wind installations came in at \~3.8GW versus \~26GW in the same period last year. This normalization following last year's front-loaded build-out has significantly reduced copper demand from the energy transition segment.

In addition, softer domestic EV demand has weighed on energy-transition-related copper consumption. EV wholesales are up just \~2% YTD, while retail sales have contracted \~15% y/y, pointing to weak domestic uptake. That said, this has

been partially offset by robust export demand, with EV exports surging \~115% y/y. Despite the sluggish start to EV sales in 2026, implied copper

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
