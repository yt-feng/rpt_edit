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
# ANCHOR REPORT

24 June 2026

![](images/0e21101cb5787e9ba02a1da295055368cf4f3d7a22c2ab167f11a8c658ed1b86.jpg)

## Global Batteries – ESS, robot batteries to drive value

## Battery industry entering a new, diverging phase

We expect global energy storage system (ESS) batteries to show attractive demand growth of 17% p.a. over 2026-30F to 926GWh in 2030F, with the US representing \~20% of demand driven by AI datacenter power demand, renewables integration, and grid modernization. In contrast, global electric vehicle (EV) battery demand growth should be slower at 11% p.a. over 2026-30F to 1.8TWh in 2030F. In this context, the industry's competitive landscape is becoming increasingly segmented. China is the clear volume leader, with 2026F global share at 78%/80% for EV/ESS batteries, despite tighter US/Europe regulations. Its dominance is underpinned by leadership in LFP batteries, which account for 61% of the global battery market, and a highly integrated supply chain. South Korea is repositioning toward higher-value EV and US ESS segments, where US/EU localization requirements create meaningful barriers to entry. Japan is focusing specifically on AIDC demand rather than mass-market batteries.

Key themes in this Anchor Report:

\- Global EV/ESS battery market outlook: Comparing the strategic positioning of Chinese, Korean and Japanese battery players

• Global xEV outlook: Cutting US EV and China PHEV volume forecasts

\- Global lithium supply-demand: Market to remain tightly balanced in 2026-27F

• CATL and Samsung SDI are our preferred Buy rated stock picks

Research Analysts

Global EV Batteries & Materials

Cindy Park - NFIK

Ethan Zhang - NIHK

Yu Okazaki - NSC

Dongmin Lee - NFIK

Global Autos
Anindya Das - NSC

Advanced Manufacturing
Frank Fan - NIHK

Production Complete: 2026-06-24 16:27 UTC

# Global Batteries

EQUITY: ALTERNATIVE ENERGY

## ESS, robot batteries to drive value

China dominates global market share; Korea eyes US ESS/premium EV space; Japan targets AIDC server batteries

The global battery landscape has become highly segmented such that China, South Korea, and Japan now seek to adopt varying growth strategies, in our view. China has become a clear volume leader in electric vehicle (EV) / energy storage system (ESS) batteries, with 2026F global market share of 78%/80% – despite regulatory restrictions being imposed by the US/Europe – due to its dominant LFP (61% global battery share) / integrated supply chain. South Korea is repositioning its market toward the higher-value EV and US ESS segments where localization requirements act as barriers to entry. Japan, rather than competing within mass-market batteries, has turned it focus on AI datacenter infrastructure demand, with a revenue target of JPY1.0tn for FY29E from AIDC battery backup units (BBU; installed inside AIDC server racks to provide instant back-up power) and a 20% ROIC target for the overall battery business.

EV battery – China dominant in scale, cost leadership; Korea eyes premium area

We project global EV battery demand to grow by 9.5% p.a. over 2026-35F, reaching 1.8TWh/2.7TWh in 2030F/35F (2025: 1.0TWh). Our projections are premised on NOM auto team's global EV/PHEV shipment growth forecasts of 6%/12%/11% (y-y) to 21.1mn/23.7mn/26.3mn units in 2026F/27F/28F and penetration rate forecasts of 23%/32%/40% in 2026F/30F/35F. We expect China to command 65%/78% share in global EV/battery markets in 2026F. Outside of China, China's battery market share currently stands at 58%, driven by superior cost leadership (LFP [lithium iron phosphate] chemistry), unrivalled scale, and supply-chain integration. Korean batteries (15% of global market share) remain competitive, in our view, in premium applications such as high-nickel chemistries (long range cars), cylindrical 4680 cells (Tesla), silicon-anode technologies, and US/EU localization strategies.

ESS battery – China leads global market share, Korea/Japan gain share in the US

We build in global ESS battery (BESS) demand growth of 17%/11% p.a. over 2026-30F/2026-35F to 1.3TWh in 2035F (2026F: 490GWh; 50% of 2030F EV batteries; US BESS demand of 113GWh/194GWh for 2026F/2030F; 14% p.a. growth over 2026-30F), driven by renewables integration, grid modernization, and AI datacenter power demand. We expect global BESS demand to be fueled by grid applications (70-80% of demand; renewables integration), and AIDC demand. China should remain dominant, in our view, through its leadership in LFP and increasingly through sodium batteries (NiB), with the latter potentially representing 15-20% of 2030F ESS demand. CATL (300750 CH, Buy), BYD (002594 CH, Buy), Hithium (unlisted), EVE (300014 CH, Buy) are leading players. We observe increasing penetration of Korean batteries into North America (mostly into the US), where tariff barriers, localization requirements, and AIDC investments are creating opportunities for non-Chinese suppliers. Japan’s leading battery maker Panasonic (6752 JP, Neutral) specifically focuses on AIDC BESS for server rack (high precision battery bundled with system) where it commands 60-70% global market share, on our estimate

## Robot batteries are likely to emerge as a high-value specialty market

Humanoid robot commercialization is likely to accelerate over the next few years. Despite representing only a small portion of EV/ESS battery volume, the revenue opportunity for robot batteries may be larger than the GWh implication, supported by premium pricing (3x EV battery price per kWh; we estimate USD2-4bn market size in 2030F), customization, and high performance specification. Unlike EV batteries, robot batteries require high power density, high C-rate capability (a measure of how fast a battery can be charged), lightweight design, and advanced thermal control. Early-generation humanoids may favor high-nickel chemistries until \~2030F, in our view, but improving LFP performance and battery-swapping architectures could allow China to gain visible share in robot applications over time.

## Research Analysts

Global EV Batteries & Materials

Cindy Park - NFIK
cindy.park@NOM.com
+822 3783 2324

Ethan Zhang - NIHK
ethan.zhang@NOM.com
+852 2252 2157

Yu Okazaki - NSC
yu.okazaki@NOM.com
+81 3 6703 1210

Dongmin Lee - NFIK
dongmin.lee@NOM.com
+822 3783 2338

Global Autos
Anindya Das - NSC
adas@NOM.com
+81 3 6703 1164

Advanced Manufacturing
Frank Fan - NIHK
frank.fan@NOM.com
+852 2252 2195

Battery technology – China drives LFP, sodium and semi-solid state batteries; Korea and Japan focus on high nickel, and all solid-state batteries

LFP has become the industry's volume chemistry across EV/ESS applications, benefiting from superior cost, safety, and cycle life characteristics. Meanwhile, high-nickel NCM/NCA (nickel, cobalt, manganese/nickel, cobalt, aluminum) batteries are increasingly positioned as premium solutions for high-performance EVs, fast charging, and specialty applications. We expect sodium-ion batteries (SiBs) to become competitive as ESS energy density improves and costs decline. Given China's control over the sodium-ion supply chain and the rapid technological advancement, we expect China to dominate the SiB market in the coming years. Semi-solid state may be commercialized by China in the next two years, in our view, but all solid state batteries (ASSB) for EVs are likely to be delayed to beyond 2028F due to technical and cost issues. ASSB for robot batteries may be possible.

## Battery metal outlook – tighter supply, moderate price recovery

Across lithium, nickel and cobalt, the market is transitioning from oversupply concerns toward a more balanced environment, in our view. Demand from ESS, AI datacenter infrastructure, as well as policy directions from key producing markets and timing of mine starts are becoming important pricing drivers. For lithium, we expect a moderate price recovery in 2026/27F to USD22.0k/24.6k per tonne (lithium carbonate; 2025 USD9.7k/tonne) with supplies facing delays from major projects (e.g., CATL's Jianxiawo mine), Zimbabwe export restrictions, and lower production guidance from Greenbushes – albeit being offset by Australian mine restarts. On the other hand, nickel and cobalt pricing will likely have some support owing to tighter supply controls in Indonesia and the DRC (Republic of Congo).

Stock picks – CATL, Samsung SDI, L&F are top Buys; Neutral on Panasonic, SKI
CATL and Samsung SDI are our preferred stocks, with CATL leading globally across EV and ESS applications via scale and profitability, and emerging sodium-ion batteries, while SDI should deliver an earnings turnaround from 2H26F on ESS AIDC BBU batteries. EVE Energy appears well positioned to gain share in the global ESS and 4680 markets; L&F's cathode business supplying to a steady selling EV OEM as well as its chemistry diversification to LFP should support the positive outlook.

We have Neutral ratings on Panasonic (as we think the risk/reward profile is fairly priced) and SK Innovation (due to its weakened battery business, and a potential decline in the refining/chemical business amid signs of a de-escalation in the Iran-US conflict).

## Risks

Downside risks include: 1) weaker-than-expected EV demand outside China, particularly in the US and Europe, due to subsidy reductions, regulatory rollbacks, macroeconomic uncertainty, and slower charging infrastructure deployment; 2) policy and trade uncertainties, including changes to US government incentives, rising tariffs on Chinese battery materials and products, technology-transfer restrictions, and geopolitical tensions that disrupt global supply chains; 3) unexpected battery safety incidents involving EV, ESS resulting in recalls, project delays, stricter regulations, and higher warranty costs; 4) a sharp rebound in lithium, nickel, cobalt, graphite, copper, or rare-earth prices, increasing battery production costs and slowing battery cost reductions. Upside risks to our industry view include: 1) faster-than-expected EV demand recovery, driven by lower battery costs, a broader range of affordable EV/PHEV models, and improving charging infrastructure; 2) stronger-than-expected ESS demand growth; 2) faster commercialization of next-generation technologies, including dry-electrode manufacturing, high-nickel batteries, 4680 cells, sodium-ion batteries, and semi-solid-state batteries.

Fig. 1: Stocks for action – global battery sector

<table><tr><td>Company</td><td>Currency</td><td>Ticker</td><td>Rating</td><td>Mkt cap (USDmn)</td><td>Turnover (USDmn)</td><td>Target Price (local)</td><td>Price (local) 22/Jun/26</td><td>Upside (%)</td></tr><tr><td>Contemporary Amperex Technology</td><td>CNY</td><td>300750 CH</td><td>Buy</td><td>266,005</td><td>2,041</td><td>612.00</td><td>408.98</td><td>49.6%</td></tr><tr><td>LG Energy Solution</td><td>KRW</td><td>373220 KS</td><td>Buy</td><td>58,656</td><td>194</td><td>600,000</td><td>385,500</td><td>55.6%</td></tr><tr><td>Samsung SDI</td><td>KRW</td><td>006400 KS</td><td>Buy</td><td>27,929</td><td>571</td><td>900,000</td><td>533,000</td><td>68.9%</td></tr><tr><td>EVE Energy</td><td>CNY</td><td>300014 CH</td><td>Buy</td><td>22,303</td><td>678</td><td>100.00</td><td>70.23</td><td>42.4%</td></tr><tr><td>LG Chem</td><td>KRW</td><td>051910 KS</td><td>Buy</td><td>14,826</td><td>118</td><td>440,000</td><td>323,000</td><td>36.2%</td></tr><tr><td>Wuxi Lead</td><td>CNY</td><td>300450 CH</td><td>Buy</td><td>10,942</td><td>478</td><td>73.00</td><td>47.35</td><td>54.2%</td></tr><tr><td>EcoproBM</td><td>KRW</td><td>247540 KS</td><td>Buy</td><td>10,604</td><td>181</td><td>280,000</td><td>166,700</td><td>68.0%</td></tr><tr><td>L&amp;F</td><td>KRW</td><td>066970 KS</td><td>Buy</td><td>3,316</td><td>128</td><td>200,000</td><td>125,700</td><td>59.1%</td></tr><tr><td>Panasonic Holdings</td><td>JPY</td><td>6752 JP</td><td>Neutral</td><td>66,692</td><td>198</td><td>3,600</td><td>4,393</td><td>-18.1%</td></tr><tr><td>Ganfeng Lithium</td><td>HKD</td><td>1772 HK</td><td>Neutral</td><td>14,729</td><td>118</td><td>31.00</td><td>57.25</td><td>-45.9%</td></tr><tr><td>POSCO Future M</td><td>KRW</td><td>003670 KS</td><td>Neutral</td><td>11,105</td><td>110</td><td>200,000</td><td>192,000</td><td>4.2%</td></tr><tr><td>SK Innovation</td><td>KRW</td><td>096770 KS</td><td>Neutral</td><td>11,014</td><td>91</td><td>118,000</td><td>100,200</td><td>17.8%</td></tr><tr><td>Yunnan Energy</td><td>CNY</td><td>002812 CH</td><td>Neutral</td><td>10,292</td><td>339</td><td>32.00</td><td>72.05</td><td>-55.6%</td></tr><tr><td>Putailai</td><td>CNY</td><td>603659 CH</td><td>Neutral</td><td>9,744</td><td>232</td><td>17.00</td><td>30.90</td><td>-45.0%</td></tr><tr><td>Gotion High-Tech</td><td>CNY</td><td>002074 CH</td><td>Neutral</td><td>8,168</td><td>243</td><td>22.50</td><td>30.72</td><td>-26.8%</td></tr><tr><td>Tianqi Lithium</td><td>HKD</td><td>9696 HK</td><td>Neutral</td><td>1,348</td><td>46</td><td>41.00</td><td>44.76</td><td>-8.4%</td></tr></table>

Note: Pricing as of 22 June 2026  
Source: Bloomberg Finance L.P., NOM estimates

## Global EV/battery – China likely to account for 65%/78% market share in 2026F

NOM's auto team forecasts global EV/PHEV shipments will grow by 6%/12%/11% (y-y) to 21.1mn/23.7mn/26.3mn units in 2026F/27F/28F. Based on these forecasts, we project EV battery demand to grow by 9.5% p.a. over 2026-35F, reaching 2.7TWh in 2035F. We project that EV/PHEV sales will slow down to 8.3% p.a. over 2026-35F, from 52% p.a. over 2020-24.

China remains the largest EV market representing 65% of global shipments, but we expect the growth rate to slow down to 6.2% p.a. over 2026-35F as EV/PHEV penetration exceeds 50%. The regulatory landscape in Europe (which accounts for a 19.5% share of global shipments) now makes it the most policy-driven EV market globally due to tightening CO $_{2}$ regulations and in order to protect its domestic auto industry from the increasing market share of China (15% share of the EU EV market). While North America – namely, the US – is likely to see a decline in EV/PHEV shipments in 2026F, the country’s EV/battery shipments might see upside risks post 2029 in a scenario of a change in government/administration and resumption of EV adoption.

Fig. 2: Global xEV forecasts by region

<table><tr><td colspan="14">xEV forecasts</td></tr><tr><td>(k units)</td><td>2023</td><td>2024</td><td>2025</td><td>2026F</td><td>2027F</td><td>2028F</td><td>2029F</td><td>2030F</td><td>2031F</td><td>2032F</td><td>2033F</td><td>2034F</td><td>2035F</td></tr><tr><td>Global auto shipment</td><td>88,147</td><td>89,616</td><td>91,904</td><td>91,031</td><td>93,091</td><td>95,031</td><td>97,005</td><td>98,949</td><td>100,701</td><td>102,506</td><td>104,366</td><td>106,281</td><td>108,255</td></tr><tr><td>EV/PHEV shipment</td><td>12,950</td><td>16,717</td><td>19,925</td><td>21,147</td><td>23,667</td><td>26,251</td><td>28,525</td><td>31,192</td><td>34,021</td><td>36,309</td><td>38,619</td><td>40,876</td><td>43,306</td></tr><tr><td>Global EV/PHEV penetration (%)</td><td>14.7%</td><td>18.7%</td><td>21.7%</td><td>23.2%</td><td>25.4%</td><td>27.6%</td><td>29.4%</td><td>31.5%</td><td>33.8%</td><td>35.4%</td><td>37.0%</td><td>38.5%</td><td>40.0%</td></tr><tr><td>New energy vehicle shipment</td><td>21,775</td><td>27,074</td><td>31,425</td><td>34,922</td><td>39,562</td><td>44,566</td><td>49,741</td><td>55,153</td><td>61,039</td><td>65,124</td><td>69,686</td><td>72,595</td><td>75,734</td></tr><tr><td>EV/PHEV shipment</td><td>12,950</td><td>16,717</td><td>19,925</td><td>21,147</td><td>23,667</td><td>26,251</td><td>28,525</td><td>31,192</td><td>34,021</td><td>36,309</td><td>38,619</td><td>40,876</td><td>43,306.</td></tr><tr><td>US</td><td>1,483</td><td>1,588</td><td>1,631</td><td>1,616</td><td>1,775</td><td>1,981</td><td>2,265</td><td>2,614</td><td>2,990</td><

[中间内容因长度限制已省略]

 version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM Financial Investment (Korea) Co., Ltd., Korea. All rights reserved.

NOM Asian Equity Research Group

<table><tr><td>Hong Kong</td><td>NOM International (Hong Kong) Limited30/F Two International Finance Centre, 8 Finance Street, Central, Hong KongTel: +852 2536 1111 Fax: +852 2536 1820</td></tr><tr><td>Singapore</td><td>NOM Singapore Limited10 Marina Boulevard Marina Bay Financial Centre Tower 2, #36-01,Singapore 018983, SingaporeTel: +65 6433 6288 Fax: +65 6433 6169</td></tr><tr><td>Taipei</td><td>NOM International (Hong Kong) Limited, Taipei Branch17th Floor, Walsin Lihwa Xinyi Building, No.1, Songzhi Road, Taipei 11047, Taiwan, R.O.C.Tel: +886 2 2176 9999 Fax: +886 2 2176 9900</td></tr><tr><td>Seoul</td><td>NOM Financial Investment (Korea) Co., Ltd.17th floor, Seoul Finance Center, 136, Sejong-daero, Jung-gu, Seoul 04520, KoreaTel: +82 2 3783 2000 Fax: +82 2 3783 2500</td></tr><tr><td>Kuala Lumpur</td><td>NOM Securities Malaysia Sdn. Bhd.Suite No 16.5, Level 16, Menara IMC, 8 Jalan Sultan Ismail, 50250 Kuala Lumpur, MalaysiaTel: +60 3 2027 6811 Fax: +60 3 2027 6888</td></tr><tr><td>India</td><td>NOM Financial Advisory and Securities (India) Private LimitedCeejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road,Worli, Mumbai- 400 018, IndiaTel: +91 22 4037 4037 Fax: +91 22 4037 4111</td></tr><tr><td>Indonesia</td><td>PT NOM Sekuritas IndonesiaSuite 209A, 9th Floor, Sentral Senayan II BuildingJl. Asia Afrika No. 8, Gelora Bung Karno, Jakarta 10270, IndonesiaTel: +62 21 2991 3300 Fax: +62 21 2991 3333</td></tr><tr><td>Sydney</td><td>NOM Australia Ltd.Level 25, Governor Phillip Tower, 1 Farrer Place, Sydney NSW 2000Tel: +61 2 8062 8000 Fax: +61 2 8062 8362</td></tr><tr><td>Tokyo</td><td>Equity Research DepartmentFinancial &amp; Economic Research CenterNOM Securities Co., Ltd.17/F Urbannet Building, 2-2, Otemachi 2-chome Chiyoda-ku, Tokyo 100-8130, JapanTel: +81 3 5255 1658 Fax: +81 3 5255 1747, 3272 0869</td></tr></table>

Caring for the environment: to receive only the electronic versions of our research, please contact your sales representative.

## NOM

NOM Asian Equity Research Group

<table><tr><td>Hong Kong</td><td>NOM International (Hong Kong) Limited30/F Two International Finance Centre, 8 Finance Street, Central, Hong KongTel: +852 2536 1111 Fax: +852 2536 1820</td></tr><tr><td>Singapore</td><td>NOM Singapore Limited10 Marina Boulevard Marina Bay Financial Centre Tower 2, #36-01,Singapore 018983, SingaporeTel: +65 6433 6288 Fax: +65 6433 6169</td></tr><tr><td>Taipei</td><td>NOM International (Hong Kong) Limited, Taipei Branch17th Floor, Walsin Lihwa Xinyi Building, No.1, Songzhi Road, Taipei 11047, Taiwan, R.O.C.Tel: +886 2 2176 9999 Fax: +886 2 2176 9900</td></tr><tr><td>Seoul</td><td>NOM Financial Investment (Korea) Co., Ltd.17th floor, Seoul Finance Center, 136, Sejong-daero, Jung-gu, Seoul 04520, KoreaTel: +82 2 3783 2000 Fax: +82 2 3783 2500</td></tr><tr><td>Kuala Lumpur</td><td>NOM Securities Malaysia Sdn. Bhd.Suite No 16.5, Level 16, Menara IMC, 8 Jalan Sultan Ismail, 50250 Kuala Lumpur, MalaysiaTel: +60 3 2027 6811 Fax: +60 3 2027 6888</td></tr><tr><td>India</td><td>NOM Financial Advisory and Securities (India) Private LimitedCeejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road,Worli, Mumbai- 400 018, IndiaTel: +91 22 4037 4037 Fax: +91 22 4037 4111</td></tr><tr><td>Indonesia</td><td>PT NOM Sekuritas IndonesiaSuite 209A, 9th Floor, Sentral Senayan II BuildingJl. Asia Afrika No. 8, Gelora Bung Karno, Jakarta 10270, IndonesiaTel: +62 21 2991 3300 Fax: +62 21 2991 3333</td></tr><tr><td>Sydney</td><td>NOM Australia Ltd.Level 25, Governor Phillip Tower, 1 Farrer Place, Sydney NSW 2000Tel: +61 2 8062 8000 Fax: +61 2 8062 8362</td></tr><tr><td>Tokyo</td><td>Equity Research DepartmentFinancial &amp; Economic Research CenterNOM Securities Co., Ltd.17/F Urbannet Building, 2-2, Otemachi 2-chome Chiyoda-ku, Tokyo 100-8130, JapanTel: +81 3 5255 1658 Fax: +81 3 5255 1747, 3272 0869</td></tr></table>

Caring for the environment: to receive only the electronic versions of our research, please contact your sales representative.

## NOM
"""
