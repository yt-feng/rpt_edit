你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

<table><tr><td colspan="14">xEV forecasts</td></tr><tr><td>(k units)</td><td>2023</td><td>2024</td><td>2025</td><td>2026F</td><td>2027F</td><td>2028F</td><td>2029F</td><td>2030F</td><td>2031F</td><td>2032F</td><td>2033F</td><td>2034F</td><td>2035F</td></tr><tr><td>Global auto shipment</td><td>88,147</td><td>89,616</td><td>91,904</td><td>91,031</td><td>93,091</td><td>95,031</td><td>97,005</td><td>98,949</td><td>100,701</td><td>102,506</td><td>104,366</td><td>106,281</td><td>108,255</td></tr><tr><td>EV/PHEV shipment</td><td>12,950</td><td>16,717</td><td>19,925</td><td>21,147</td><td>23,667</td><td>26,251</td><td>28,525</td><td>31,192</td><td>34,021</td><td>36,309</td><td>38,619</td><td>40,876</td><td>43,306</td></tr><tr><td>Global EV/PHEV penetration (%)</td><td>14.7%</td><td>18.7%</td><td>21.7%</td><td>23.2%</td><td>25.4%</td><td>27.6%</td><td>29.4%</td><td>31.5%</td><td>33.8%</td><td>35.4%</td><td>37.0%</td><td>38.5%</td><td>40.0%</td></tr><tr><td>New energy vehicle shipment</td><td>21,775</td><td>27,074</td><td>31,425</td><td>34,922</td><td>39,562</td><td>44,566</td><td>49,741</td><td>55,153</td><td>61,039</td><td>65,124</td><td>69,686</td><td>72,595</td><td>75,734</td></tr><tr><td>EV/PHEV shipment</td><td>12,950</td><td>16,717</td><td>19,925</td><td>21,147</td><td>23,667</td><td>26,251</td><td>28,525</td><td>31,192</td><td>34,021</td><td>36,309</td><td>38,619</td><td>40,876</td><td>43,306.</td></tr><tr><td>US</td><td>1,483</td><td>1,588</td><td>1,631</td><td>1,616</td><td>1,775</td><td>1,981</td><td>2,265</td><td>2,614</td><td>2,990</td><td>3,365</td><td>3,702</td><td>3,975</td><td>4,271</td></tr><tr><td>EU</td><td>3,010</td><td>2,945</td><td>3,858</td><td>4,122</td><td>4,520</td><td>4,983</td><td>5,587</td><td>6,480</td><td>7,147</td><td>7,762</td><td>8,133</td><td>8,749</td><td>9,429</td></tr><tr><td>Japan</td><td>138</td><td>99</td><td>104</td><td>156</td><td>225</td><td>284</td><td>359</td><td>454</td><td>556</td><td>681</td><td>806</td><td>955</td><td>1,133</td></tr><tr><td>China</td><td>7,715</td><td>11,360</td><td>13,438</td><td>13,756</td><td>15,442</td><td>17,091</td><td>18,217</td><td>19,168</td><td>20,029</td><td>20,917</td><td>21,774</td><td>22,658</td><td>23,569</td></tr><tr><td>Korea</td><td>169</td><td>152</td><td>232</td><td>264</td><td>313</td><td>338</td><td>354</td><td>369</td><td>384</td><td>398</td><td>412</td><td>427</td><td>442</td></tr><tr><td>Others</td><td>436</td><td>572</td><td>663</td><td>1,233</td><td>1,393</td><td>1,574</td><td>1,743</td><td>2,106</td><td>2,916</td><td>3,186</td><td>3,792</td><td>4,112</td><td>4,463</td></tr><tr><td>HV shipment</td><td>8,810</td><td>10,346</td><td>11,484</td><td>13,757</td><td>15,876</td><td>18,295</td><td>21,191</td><td>23,928</td><td>26,980</td><td>28,769</td><td>31,015</td><td>31,657</td><td>32,354</td></tr><tr><td>US</td><td>1,800</td><td>2,200</td><td>2,799</td><td>3,219</td><td>3,863</td><td>5,021</td><td>6,528</td><td>7,703</td><td>8,550</td><td>9,491</td><td>10,155</td><td>10,663</td><td>11,196</td></tr><tr><td>EU</td><td>3,401</td><td>4,068</td><td>4,567</td><td>5,336</td><td>5,937</td><td>6,115</td><td>6,237</td><td>6,300</td><td>5,985</td><td>5,686</td><td>5,401</td><td>4,861</td><td>4,375</td></tr><tr><td>Japan</td><td>1,865</td><td>2,035</td><td>1,992</td><td>2,091</td><td>2,259</td><td>2,371</td><td>2,490</td><td>2,590</td><td>2,667</td><td>2,721</td><td>2,693</td><td>2,640</td><td>2,508</td></tr><tr><td>China</td><td>902</td><td>992</td><td>947</td><td>1,136</td><td>1,534</td><td>2,147</td><td>2,899</td><td>3,914</td><td>4,892</td><td>5,626</td><td>6,188</td><td>6,683</td><td>7,218</td></tr><tr><td>Korea</td><td>375</td><td>494</td><td>579</td><td>699</td><td>799</td><td>896</td><td>979</td><td>1,053</td><td>1,093</td><td>1,114</td><td>1,124</td><td>1,129</td><td>1,132</td></tr><tr><td>Others</td><td>467</td><td>556</td><td>600</td><td>1,276</td><td>1,486</td><td>1,744</td><td>2,057</td><td>2,369</td><td>3,793</td><td>4,133</td><td>5,452</td><td>5,681</td><td>5,925</td></tr><tr><td>FCV shipment</td><td>15</td><td>11</td><td>16</td><td>18</td><td>18</td><td>20</td><td>25</td><td>33</td><td>38</td><td>45</td><td>53</td><td>62</td><td>75</td></tr><tr><td>US</td><td>3</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>2</td><td>3</td><td>4</td><td>6</td><td>9</td><td>14</td></tr><tr><td>EU</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><

[中间内容因长度限制已省略]

no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

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
