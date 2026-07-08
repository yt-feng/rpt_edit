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
# Industry Global Semiconductors

Europe
Global
North America

Technology Semiconductors

Date
7 July 2026
Industry Update

# Auto Semi market tracker - pricing is gaining further momentum

## From destocking to restocking as allocation fears are resurfacing

Auto Semis pricing has potential to increase going forward due to low key component inventories and strong competition for capacity from AI datacenter In our last Auto Semis update from April (here), we pointed out an improving pricing environment for Auto Semis for the first time in over three years. We saw this as driven by: 1) reduced inventories of key Auto Semis across supply chains, 2) spill-over effects from AI-driven chip demand in categories like mid-voltage power MOSFETs but also memory (including specialized memory such as NOR Flash), and 3) continued strong content growth driven by SDVs (for high-end MCUs and Ethernet components, in particular). The above-mentioned areas, as well as analog components, remain the key drivers of a better pricing environment, in our view, while the situation for higher-voltage power semis for xEV drivetrains remains on the other end of the spectrum but is also set to improve into 2027 with demand drivers from AI datacenter accelerating from next year out to 2030 (SSCBs, SSTs and 800V architecture more broadly, as discussed here), Overall, we believe Auto Semis pricing is gaining further momentum on the back of the aforementioned drivers and despite a mixed Automotive end market. Our industry conversations indicate only low-single-digit price declines this year (vs. normal low- to mid-single-digit), but with scope for price increases (even on company Auto Semi portfolio levels and not just individual components) as we go into next year. Paired with ongoing strong content growth from SDV, ADAS and to some extent xEVs (especially in Europe), we believe the Auto Semis market can return to >10% growth this year and build further momentum in '27. Given margins for many players in this market remain somewhat depressed this year, we continue to see strong operating leverage ahead from better capacity utilization (helped by capacity reallocation towards AI), as well as pricing and we remain positive on the broader space, especially names with a strong AI story and potential to grow into existing capacity/cleanroom space. Our top picks are Infineon, NXP, onsemi and STMicro.

We believe general component and Auto semi destocking across the supply chain has largely played out in recent quarters. Our inventory analysis of the tier 1 auto supply chain shows a slight increase in \$ inventory value sequentially in Q1/26 and inventory as a percentage of sales in Q1/26 increased to 12.2% (vs. \~12% in Q4/25). Our industry conversations point to a desire by tier 1s and OEMs to rebuild strategic inventory in certain areas with some industry discussions raising fears over allocation and "golden screw" key component shortages ahead again given the strong demand from AI datacenter for semis capacity.

Johannes Schaller
Associate Director of Equity Research - Germany

Ross Seymore
Research Analyst

Robert Sanders
Research Analyst

Melissa Weathers
Research Analyst

Edison Yu
Research Analyst

Nicolas Herms
Research Analyst

DJ Sebastian
Research Associate

Yusuf Jamal
Research Associate

Kunal Gupta
Research Associate

We value stocks in the sector on a P/E, EV/Sales and/or DCF basis, benchmarking the multiples vs. peers and/or expected growth rates. Key downside/upside sector risks: a macro/auto production slowdown or improvement, and design and/or market share losses or gains.

## From destocking to restocking into Q2 and H2/26

Looking back at the recent near-term picture and relative performance in Q1 (in US dollar terms), Auto semi players saw a revenue increase of +1% q/q, on fairly lean inventory conditions, partly offset by other macro factors. On y/y basis, the acceleration stood at +11%, back in-line with the five-year average growth trendline. Dynamics by companies are interesting in hindsight with industry bellwethers such as Qualcomm (+20% q/q), Analog Devices (+8% q/q) and Renesas (+4% q/q) seeing strong growth while Infineon (+1% q/q), Texas Instruments (flat q/q), onsemi (flat q/q) and Rohm (flat q/q) showed flat to modest growth. STMicro (-9% q/q) and NXP (-5% q/q) witnessed a sequential decline in revenue growth. Among smaller companies, Lattice Semi (+35% q/q), Mobileye (+25% q/q), Ambarella (+13% q/q) saw strong growth, while Elmos (-10% q/q), Melexis (-6% q/q) and Nvidia (-5% q/q) saw a sequential decline. For Q2/26e, our bottom-up model suggests +5% revenue growth sequentially, well above the five-year average performance (+3% q/q), implying the beginning of a restocking cycle that should last into H2, in our view.

Figure 1: Auto Semi sales growth for CY24/25/26e  
![](images/0355cb86581378313147b133e2b5defa286f1da002a5bc64bdad742e385d27a5.jpg)  
Source : DB Estimates, Bloomberg Finance LP (growth is computed on US\$ sales); ) \*IFX & ADI include Cypress and Maxim contribution on pro-forma basis, respectively.

Figure 2: Auto Semi market growth (2011-2026e)  
![](images/f0cc273ed1a141e14dac0c6ac1296af4f05c26f4073408883640f6cb8010667f.jpg)  
Source : DB Estimates, Bloomberg Finance LP (growth is computed on US\$ sales) \* The annual growth is calculated based on consolidated auto semi sales of companies mentioned in figure 1.

Figure 3: Current price/earnings ratio (1y fwd) vs. 5y avg  
![](images/4a2073a9f221751e3dc712712a18683aa4bd7ae03f250cae1b5a46aa66a2a6c8.jpg)  
Source : Bloomberg Finance LP (pricing as on 3rd July 2026)

Figure 4: Current price/earnings ratio (1y fwd)  
![](images/929916bc6144f8f6182a1b8b61bcd670df51dc611374b43adeab0294f02950da.jpg)  
Source : Bloomberg Finance LP (pricing as on 3rd July 2026)

## Auto Semi revenues up 11% y/y in Q1/26; \~11% y/y growth expected for Q2/26e

![](images/7e84bb5da6058807bbb1cda75669c4fd8e09dd2c91b079f0d5b71dad40bcbd40.jpg)  
Source : Company data, DB estimates

Figure 6: Tier-1 Auto Semi players  
![](images/7bb03ac19a2067dba41e8142ccf1d2b21fea9623d827f461117889cb28215b42.jpg)  
Source : Company data, DB, (in US\$ m); \*:-Intersil acquired by Renesas on 24 February 2017; IFX acquired Cypress on 20th Apr 2020

Figure 7: Tier-2 Auto Semi players  
![](images/ef4aefb51c065e7defc3fb57f2dbb7aa14eded5e9c7793e3c52bad3526363d0d.jpg)  
Source : Company data, DB, (in US\$ m);\*ADI+Maxim PF numbers

Long-term content-driven growth story remains intact, cyclical bottom behind us

## Figure 8: Auto Semi vendors management commentary

<table><tr><td>Company</td><td>Management commentary on automotive business</td></tr><tr><td>Analog Devices</td><td>&quot;So if we look at what we think at the midpoint of the guide, what we expect to see in FQ3 (June ending) is continued above-seasonal growth across industrial, automotive and communication...So from an industrial and automotive perspective, we&#x27;d expect to grow sort of mid to high single-digits sequentially. &quot; &quot;Now, on the inventory build-up question, we&#x27;re not seeing that yet, right? After the digestion, which we talked about, particularly in BMS, we feel like automotive customers are fairly lean on inventory, at least the ones we talk to and which is very supportive of our growth expectation going forward.&quot;</td></tr><tr><td>Infineon</td><td>&quot;Generally speaking, the near-term outlook for the automotive market remains relatively muted. In its April update, market researchers S&amp;P Global revised down its light vehicle production numbers for 2026. They are now more or less in line with our view. As you know, what matters more than car units is structural content growth. Here, we see the adoption of software-defined vehicles accelerating. Also, the trend towards E-mobility is intact. However, xEV penetration is progressing more slowly than predicted.&quot; &quot;we expect revenues of around EUR4.1bn for our fiscal third quarter, corresponding to 8% growth quarter-over-quarter. By segment, for ATV (automotive), a slight revenue growth is predicted.&quot; &quot;For the full year 2026 fiscal year, we now expect revenues to be significantly up compared to the previous fiscal year, translating into a level of EUR16bn...ATV should see slight revenue growth, driven by its broad product portfolio and the early adoption of software-defined vehicles burdened by the decrease of the high voltage drivetrain business.&quot;</td></tr><tr><td>Melexis</td><td>&quot;One quarter ago, actually, two months ago, we have indeed mentioned that our customer has informed us that the second half of the year will be better than the first half. And I would say this is indeed confirmed in the order intake. We see clearly order intake improving week after week, day after day.&quot; &quot;We are seeing increased opportunities in ADAS as the industry continues its structural shift towards steer-by-wire and break-by-wire architecture.&quot;</td></tr><tr><td>NXP Semiconductor</td><td>&quot;Our outlook is better than we anticipated 90 days ago. We are guiding second quarter revenue to $3.45bn, up 18% year-over-year, and up 8% sequentially. This sequential growth represents an acceleration of our company&#x27;s specific drivers . Automotive is expected to be up in the low-double digit percent range year-on-year, and up in the high-single digit range sequentially.&quot; &quot; our auto business NXP is performing well. You can see from the front, in Q1, it grew 10% after you account for the sensor business. And Q2 guidance implies a high-teens year-over-year growth on the same basis. So, you can see that clearly the momentum is improving. And so, that tells you already that this is not necessarily a story about unit growth. This is a story about the transformation, the architecture transformation that is driving content growth.&quot;</td></tr><tr><td>onsemi</td><td>&quot;So, automotive in Q2/26, we think it will be roughly flat. So, as I said, we think we&#x27;re shipping to natural demand. We haven&#x27;t seen the full recovery or the replenishment cycle in automotive yet. If that were to happen later in the year, that&#x27;s going to be a good thing. But right now in Q2/26, we&#x27;re looking at flat.&quot; &quot;I talked about China specifically, given you brought it up. Q1 is seasonally down. The number of passenger vehicle was down 6%. Our revenue was actually up. Therefore, that tells you it is a content story. In certain areas, it is a share gain story as well. So, we are both gaining share, but also gaining more and more content.&quot;</td></tr><tr><td>ST Micro</td><td>&quot;Automotive design momentum progressed with various OEM and Tier 1 ecosystems. We had design wins across electric, hybrid, and traditional vehicles spanning onboard chargers, DC-DC converters, powertrain active suspension, and vehicle control electronics.&quot; &quot;Well, then what will be, again, positive on the year 2026, looking at the current dynamic in terms of growth? Well, in automotive, we confirm that &#x27;26 will be a growth for ADAS, for sensor, of course, and also with the boost of the acquisition of MEMS from NXP and for silicon carbide.&quot;</td></tr><tr><td>Texas Instruments</td><td>&quot;I want to see automotive and see how it develops in Q2. It&#x27;s too soon to call it. I will remind us, though, that during the COVID cycle, even automotive was the last to join in, also the last to peak, right? So, I&#x27;m not surprised by the behavior of this market. I will say that secular growth in automotive continues for the foreseeable future, and that is my encouragement. We are seeing cars adding features, we are seeing more content added to vehicles across the powertrains, whether it&#x27;s BEV or ICE or the hybrids.&quot;</td></tr></table>

Source : DB, company data

## Q1/26 Auto Semi revenue performance

Figure 10: Q1/26 Auto Semi revenue growth q/q  
![](images/2ac9d10c6a6af8d839e77532161b0b033bd19e9a64bedb49e4570faf83fe71f1.jpg)  
Source : Company data, DB; Growth is calculated on US\$-based revenue

Figure 11: Q1/26 Auto Semi revenue growth y/y (USD)  
![](images/b3c497c703abc520542f30ae0ea61d21da637cf4b3f5b4b98dcc143255fbb155.jpg)  
Source : Company data ; Growth is calculated on US\$ based revenue; \*IFX+Cypress PF numbers are used for growth calculation

Figure 12: Q1/26 Auto q/q growth (in reported currency)  
![](images/2d696959ae818d6bb68f51be5a82755043f8d97ea9a3e716a1db13beb8340dd2.jpg)  
Source : Company data, DB

Figure 13: Q1/26 Auto y/y growth (in reported currency)  
![](images/eecc4d6661bc559ea850440b866f3dc2e3a7435d7330add3947d724829f0c1bb.jpg)  
Source : Company data, DB

Figure 14: Auto Semis average quarterly sales (LTM; USD)  
![](images/2bdd6c267c8b2401955da034dadbd54a93cc84ccd6b7c62ec3a6e8e521977406.jpg)  
Source : Company data, DB

Figure 15: Auto Semis average quarterly sales LTM (y/y growth in USD terms)  
![](images/24822311badf584b65818e8f3a480fbd70c820b9f74dcd6af40f0478c322395e.jpg)  
Source : Company data, DB; ADI + Maxim PF numbers are used for calculation

Figure 16: Global Auto Semi revenues vs SAAR - destocking headwinds subsiding into 2026  
![](images/0742a9a8722493cc672d5ddaca7b99bd0c449ee9d2cea1009af8737d5ff67336.jpg)  
Source : Company data, IHS, DB estimates; Content gain = Automotive Semi revs (y/y) – Global SAAR (y/y); average Q1/13 – Q1/26 = \~10.0%

## So who has gained share over time?

Figure 17: Renesas is underperforming ...  
![](images/23ba6c78c9caf36c93b24b16c0d1490fdfd4cffcc191ff6dd0eab546f1d8b847.jpg)  
Source : Company data, DB

Figure 18: ...and Mobileye trends are remaining volatile  
![](images/4bc98dfb19ecaafbf3582468d2734de7eb7d0feb2e68aba859923c8088cdf515.jpg)  
Source : Company data, DB; ADI + Maxim PF numbers are used for calculation

## Auto Semis sales exposure and market share by product

Figure 19: Total Auto Semi market (including non-listed companies)  
![](images/ec94d08a7aafe89590a470e111186539093bfb1af57ba34654a6c9e35a27d210.jpg)  
Source : Company data, DB  
Figure 20: Automotive Semiconductor supplier share (Market Size: \~\$68.4b in FY24)

![](images/1f445cbbc1934fa92e27ea2e4ad2a7498ca52345328f9daa808fe4e13bf55160.jpg)  
Source : Infineon investor presentation (FQ2/25 results); company data, TechInsights (March 2025); DB  
Figure 21: Automotive Semiconductor supplier share (Market Size: \~\$74.4b in FY25)

![](images/53a1417d7bf22e653f4b602bf34ce549d1631804d224cf16394b69c34efb268c.jpg)  
Source : Infineon investor presentation (FQ2/26 results); company data, TechInsights (April 2026); DB

Figure 22: Automotive as percentage of total sales (Q1/26)  
![](images/7c89904021bf1838ccf10d47c393ebdcb4ce1de7ac11df1b8f289785788cc3a5.jpg)  
Source : DB, company data

Figure 23: Infineon Auto revenue split by products  
![](images/9a7312f283f064d27fc588db494beb47b3ed83b2b80a8ae9d68161c6ed8cc122.jpg)  
Source : Company data (based on FY25 revenue)

Figure 24: STM Auto revenue split by products  
![](images/43cadf23339fe43425540a31439fff54021e2aa91ce9d1d1a84175748d61fcd6.jpg)  
Source : Source : DB estimates, company data (based on FY25 revenue)

Figure 25: Market share in Auto power semis  
![](images/dffa943f2bd3f17a2dd0fcb9fdcb822b416b7d798200e7de0a40ab1210b5277b.jpg)  
Source : Infineon, company data, TechInsights (2025)

Figure 26: Market share in Auto sensors  
![](images/da73f7a0994cd9acdc81e38c4ec44b9f7690836f7e2505f7d4596c591c58582d.jpg)  
Source : Infineon, company data, S&P Global (2025)

Figure 27: Market share in Auto microcontrollers  
![](images/e0621706a149918f05e45c2356b7ac3bbfbcd6d92b4d1dace511e09bf6b0ea17.jpg)  
Source : Infineon, company data, TechInsights (2025)

Figure 28: Auto radar market share\*  
![](images/e2ac0340e13bb29c68454ea90653ab1cca33cdc6594acf4fb55ac83be1554e3b.jpg)  
Sour

[中间内容因长度限制已省略]

ted performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
