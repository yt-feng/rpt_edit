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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global LNG Supply & Shipping Tracker

First LNG tanker enters the Strait

ADNOC's Mubaraz which was the first laden LNG ship to exit the Strait of Hormuz on April 26, has now re-entered the Strait on June 3 and is signalling its location near Das Island likely loading LNG cargo. Meanwhile, Qatar Energy exported one more cargo outside Hormuz, as Al Daayen exited the Strait today on June 8, signaling China as its destination (Figure 1).

Figure 1: Recent LNG tanker movements across the Strait of Hormuz  
![](images/8cde91cf5a51426ea5763dc46c1dd1486fbc218a6aceb4ab748fbbcbf2ff1810.jpg)

<details>
<summary>text_image</summary>

Vessels
All Types
Vessel History
AL DRAYEN
FIRISRAZ
500 km
</details>

Source: Bloomberg Finance L.P.

Following the two observed crossings, we count nine available LNG vessels inside the Strait of Hormuz (Figure 2). We continue to treat sporadic transits as exceptions rather than a new norm until Hormuz fully reopens, with the finite pool of vessels currently inside the strait naturally capping the volume of ready-to-ship cargoes. Beyond these cargoes, volumes will need to come from renewed upstream and liquefaction operations (as well as normalizing port logistics). Consistent with our base case for a June reopening, we model Qatar Energy ramping to 83% utilisation by September, implying a full-year 2026 utilisation rate of 57% — down sharply from 105% in 2025 (Global LNG Analyzer: Initiating JKM forecasts with a declining premium to TTF, 19 May 2026). Since the onset of the conflict, we have argued that restarting Qatari LNG facilities would hinge on complex operational, security, and strategic considerations, and would take two to three months to restore full output, excluding the two damaged trains (Thoughts on Ras Laffan 2.0, 19 March 2026). This view aligns closely with Qatar Energy’s communications and was recently reinforced by the CEO, who stated that “Qatar’s return to normal LNG exports from its undamaged trains will still take two to three months at a minimum to establish, even after the Strait of Hormuz is fully open to vessels.”

## Global Commodities Research

## Otar Dgebuadze, CFA

(44-20) 3493-8246

otar.dgebuadze@JPM.com

JPM Securities plc

## Aradhaya Makkar

aradhaya.makkar@jpmchase.com

JPM India Private Limited

Figure 2: LNG vessels in the Persian Gulf  
As of June 8, 2026

<table><tr><td>Vessel Name</td><td>Beneficial Owner</td><td>DWT</td><td>Insurer</td><td>Insurance country</td><td>Comment</td></tr><tr><td>Umm Al Amad</td><td>Qatar Energy</td><td>121,730</td><td>Japan P&amp;I Club</td><td>Japan</td><td></td></tr><tr><td>Al Sahla</td><td>Qatar Energy</td><td>104,666</td><td>UK P&amp;I</td><td>UK</td><td></td></tr><tr><td>Al Ghashamiya</td><td>Qatar Energy</td><td>108,988</td><td>NorthStandard</td><td>UK</td><td></td></tr><tr><td>Patris</td><td>Chandris Group (Greece)</td><td>95,743</td><td>Japan P&amp;I Club</td><td>Japan</td><td></td></tr><tr><td>Mraikh</td><td>Chandris Group (Greece)</td><td>93,124</td><td>Skuld</td><td>Norway</td><td></td></tr><tr><td>Gaslog Skagen</td><td>China Development Bank</td><td>81,847</td><td>West of England</td><td>UK</td><td></td></tr><tr><td>Lebrethah</td><td>SK Shipping (South Korea)</td><td>94,326</td><td>Skuld</td><td>Norway</td><td></td></tr><tr><td>Disha</td><td>Petronet</td><td>81,097</td><td>NorthStandard</td><td>UK</td><td></td></tr><tr><td>Mubaraz</td><td>ADNOC</td><td>72,950</td><td>NorthStandard</td><td>UK</td><td>Departed laden on April 26, re-entered June 3</td></tr><tr><td>Seapeak Bahrain</td><td>Seapeak</td><td>95,289</td><td>NorthStandard</td><td>UK</td><td>Last signal on March 5</td></tr><tr><td>Rasheeda</td><td>Qatar Energy</td><td>130,208</td><td>NorthStandard</td><td>UK</td><td>Signalled outside of Hormuz on May 15</td></tr><tr><td>Al Daayen</td><td>Seapeak</td><td>90,617</td><td>Skuld</td><td>Norway</td><td>Departed laden on June 8</td></tr><tr><td>Fuwairit</td><td>Mitsui</td><td>74,067</td><td>UK P&amp;I</td><td>UK</td><td>Departed laden on May 24</td></tr><tr><td>Al Rayyan</td><td>Qatar Energy</td><td>72,430</td><td>Britannia P&amp;I</td><td>UK</td><td>Departed laden on May 25</td></tr><tr><td>Mihzem</td><td>China LNG Shipping Holdings</td><td>93,035</td><td>Britannia P&amp;I</td><td>UK</td><td>Departed laden on May 12</td></tr><tr><td>Al Kharaitiyat</td><td>Qatar Energy</td><td>107,153</td><td>NorthStandard</td><td>UK</td><td>Departed laden on May 9</td></tr><tr><td>SoharLng</td><td>Mitsui</td><td>71,997</td><td>UK P&amp;I</td><td>UK</td><td>Departed ballast on April 2</td></tr></table>

Source: Bloomberg Finance L.P., JPM Commodities Research

## US LNG remains more attractive to Asia

JKM remains about \$2/mmbtu premium to TTF prices, supported by approaching summer cooling demand and further strengthened by potential (super) El Niño weather event, which usually implies warmer than normal summer temperatures in Asia. However, US Gulf Coast LNG exports to Europe have recently recovered to levels comparable to this time last year (300 Mcm/day), while all incremental output from US facilities is still heading towards Asian destinations (Figures 3 & 4).

We continue to argue for higher prices (especially in 3Q2026) to support European storage injections by slowing down Asian spot LNG demand as the region enters its summer cooling season, and by incentivising greater coal-over-gas use in the European power sector.

Figure 3: USGC LNG exports to Europe/Mediterranean  
![](images/dc5944391f21e8bdbd51105e85bb392482cac72fff912ef751673d36d28372a7.jpg)

<details>
<summary>line chart</summary>

| Month | 2024 | 2025 | 2026 |
|-------|------|------|------|
| Jan   | ~250 | ~280 | ~320 |
| Feb   | ~270 | ~300 | ~450 |
| Mar   | ~240 | ~320 | ~400 |
| Apr   | ~200 | ~300 | ~350 |
| May   | ~150 | ~280 | ~250 |
| Jun   | ~180 | ~260 | ~280 |
| Jul   | ~160 | ~270 | ~290 |
| Aug   | ~170 | ~290 | ~300 |
| Sep   | ~180 | ~310 | ~320 |
| Oct   | ~190 | ~330 | ~350 |
| Nov   | ~210 | ~350 | ~380 |
| Dec   | ~250 | ~380 | ~420 |
</details>

Based on loading dates, in transit volumes based on the current location of the vessels  
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 4: USGC LNG exports to Asia/RoW  
![](images/f4d72eddaef57ff3972d817b37a10a418228c42a2e3e90dac6377eae3a42d42b.jpg)

<details>
<summary>line chart</summary>

| Month | 2024 | 2025 | 2026 |
|-------|------|------|------|
| Jan   | ~130 | ~80  | ~90  |
| Feb   | ~100 | ~40  | ~50  |
| Mar   | ~140 | ~80  | ~130 |
| Apr   | ~160 | ~100 | ~170 |
| May   | ~180 | ~120 | ~250 |
| Jun   | ~200 | ~140 | ~260 |
| Jul   | ~180 | ~130 | ~180 |
| Aug   | ~160 | ~110 | ~150 |
| Sep   | ~180 | ~130 | ~210 |
| Oct   | ~160 | ~110 | ~170 |
| Nov   | ~140 | ~90  | ~130 |
| Dec   | ~120 | ~70  | ~100 |
</details>

Based on loading dates, in transit volumes based on the current location of the vessels  
Source: Bloomberg Finance L.P., JPM Commodities Research

## Shipping rates

An important driver of JKM/TTF netbacks, LNG shipping rates in the West of Suez basin remained unchanged at \$80,000/day. Similarly, rates in the East of Suez and one-year charter rate assessment also remained unchanged WoW at \$45,000/day and \$50,500/day (Figure 5). Overall, spot shipping rates are now down by more than 60% from their peaks in the second week of the conflict, when they reached \$200,000 and \$110,000 in the West and East of Suez, respectively.

Figure 5: Shipping costs  
![](images/5e391af4cd8bff403a7e2753b1fe4d1e8da1555ea227d1fd46e01e55a1a0f33f.jpg)

<details>
<summary>line chart</summary>

| Year | East of Suez | West of Suez | 1 yr Time Charter |
|------|--------------|--------------|-------------------|
| 2022 | ~50,000      | ~50,000      | ~100,000          |
| 2023 | ~350,000     | ~375,000     | ~180,000          |
| 2024 | ~50,000      | ~150,000     | ~50,000           |
| 2025 | ~25,000      | ~25,000      | ~25,000           |
| 2026 | ~50,000      | ~200,000     | ~50,000           |
</details>

Source: Fearnley Securities, Bloomberg Finance L.P., JPM Commodities Research

## Weekly export/import trends

During the week of June 1-7, LNG deliveries increased overall by 2 Bcm WoW, with half of the increase attributed to higher deliveries into Asian markets, driven by India (0.5 Bcm WoW, 0.6 Bcm YoY) and Singapore (0.3 Bcm WoW, 0.1 Bcm YoY). The other half of the increase was driven by Europe (0.4 Bcm WoW, -0.6 Bcm YoY), Egypt (0.3 Bcm WoW, 0.3 Bcm YoY) and the Latam region (0.2 Bcm WoW, 0.1 Bcm YoY) (Figure 6). With regard to LNG exports, overall weekly loadings increased by 1 Bcm WoW, led by Africa (0.5 Bcm WoW, 0.5 Bcm YoY), Australia (0.2 Bcm WoW, 0.1 Bcm YoY) and the APAC region (0.2 Bcm WoW, 0.2 Bcm YoY) (Figure 7).

Figure 6: Change in LNG imports  
![](images/d63d4df76375bc4e9372bd031931e604e38647fef513b8ad19d5b9e680ad1504.jpg)

<details>
<summary>bar chart</summary>

Bcm, 1-7 June 2026
| Region | WoW (Bcm) | YoY (Bcm) |
| :--- | :--- | :--- |
| Kuwait | 0.1 | -0.05 |
| UAE | 0.0 | 0.0 |
| Bahrain | 0.0 | -0.1 |
| Egypt | 0.3 | 0.3 |
| Turkey | 0.0 | 0.0 |
| China | -0.05 | 0.55 |
| JKM | 0.05 | -0.2 |
| India | 0.48 | 0.58 |
| Taiwan | 0.1 | 0.25 |
| APAC | 0.45 | 0.48 |
| Europe | 0.35 | -0.6 |
| Latam | 0.2 | 0.05 |
</details>

Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 7: Change in LNG exports (loadings)  
![](images/af0cb98040352a0bfe3058f73b76a5400641f2bcaff512d7e02ccd5222db499e.jpg)

<details>
<summary>bar chart</summary>

Bcm, 1-7 June 2026
| Country | WoW (Bcm) | YoY(Bcm) |
| :--- | :--- | :--- |
| Qatar | 0.1 | -1.8 |
| UAE | -0.05 | -0.1 |
| Oman | 0.0 | 0.1 |
| US | -0.05 | 0.5 |
| CA+MX | 0.05 | 0.4 |
| Australia | 0.25 | 0.05 |
| Russia | -0.05 | 0.15 |
| APAC | 0.15 | 0.15 |
| Africa | 0.45 | 0.5 |
| RoW | 0.05 | 0.05 |
</details>

Source: Bloomberg Finance L.P., JPM Commodities Research

## Weekly loadings from recently started projects decreased

Loadings from existing projects, which are expected to increase supply year-over-year, decreased over the week (Figure 8). The decline was primarily due to lower loadings from LNG Canada, Arctic LNG 2, Plaquemines and Tortue, which was only partially offset by higher loadings from Congo, while other projects saw broadly unchanged weekly profiles.

LNG Canada loaded two cargoes, following four the week before, and is tracking at close to a 75% utilisation rate on a 4-week moving average basis, while Arctic LNG 2 loaded one cargo, following two the week before (34% utilization). Loadings in Plaquemines declined by 0.1 Bcm to 0.6 Bcm from 0.7 Bcm the week before. Meanwhile, the decline in loadings from Tortue (no cargoes, following one the week before) was offset by the increase in loadings from Congo (one cargo, following none the week before) (Figures 13-25).

We are watching closely the Golden Pass facility, where feedgas flows dropped again to near zero over the last 3-4 days, following a similar drop in mid-May after the facility exported its second cargo. After achieving its first LNG at the end of March, the facility is operating below our projected utilization rate of 80%, potentially putting up to 5 Bcm of 2026 output at risk.

Figure 8: LNG supply decomposition (2025-27)  
Bcm

<table><tr><td>Country</td><td>Project</td><td>JPMe start date</td><td>Capacity (Bcm/Year)</td><td>2025 Output</td><td>2026 Output</td><td>2027 Output</td><td>2025 y/y</td><td>2026 y/y</td><td>2027 y/y</td></tr><tr><td colspan="10">Projects started in 2025</td></tr><tr><td>US</td><td>Plaquemines LNG Phase 1 + 2</td><td>Jan-25</td><td>38.4</td><td>22.8</td><td>37.4</td><td>37.4</td><td>22.8</td><td>14.5</td><td>-</td></tr><tr><td>Canada</td><td>LNG Canada</td><td>Jul-25</td><td>19.2</td><td>2.7</td><td>15.3</td><td>16.2</td><td>2.7</td><td>12.5</td><td>1.0</td></tr><tr><td>US</td><td>Corpus Christi LNG Stage 3</td><td>Jan-25</td><td>16.4</td><td>2.9</td><td>10.8</td><td>15.6</td><td>2.9</td><td>7.8</td><td>4.8</td></tr><tr><td>Russia</td><td>Arctic LNG 2 - Train 1 + 2</td><td>Jul-25</td><td>18.1</td><td>1.6</td><td>5.8</td><td>6.0</td><td>1.6</td><td>4.2</td><td>0.3</td></tr><tr><td>Mauritania/Senegal</td><td>Tortue Phase 1 FLNG</td><td>Apr-25</td><td>3.3</td><td>1.8</td><td>3.3</td><td>3.3</td><td>1.8</td><td>1.5</td><td>-</td></tr><tr><td colspan="10">Projects starting in 2026</td></tr><tr><td>Australia</td><td>Darwin Restart</td><td>Jan-26</td><td>5.1</td><td>-</td><td>2.1</td><td>3.5</td><td>-</td><td>2.1</td><td>1.5</td></tr><tr><td>Congo</td><td>Nguya FLNG</td><td>Mar-26</td><td>3.3</td><td>-</td><td>2.0</td><td>2.6</td><td>-</td><td>2.0</td><td>0.6</td></tr><tr><td>US</td><td>Golden Pass Export - Train 1</td><td>Apr-26</td><td>8.3</td><td>-</td><td>5.3</td><td>7.8</td><td>-</td><td>5.3</td><td>2.5</td></tr><tr><td>Mexico</td><td>Costa Azul Phase 1</td><td>Sep-26</td><td>4.5</td><td>-</td><td>1.0</td><td>3.6</td><td>-</td><td>1.0</td><td>2.5</td></tr><tr><td>Australia</td><td>Pluto Expansion</td><td>Nov-26</td><td>6.9</td><td>-</td><td>0.7</td><td>5.8</td><td>-</td><td>0.7</td><td>5.1</td></tr><tr><td colspan="10">Projects starting in 2027</td></tr><tr><td>US</td><td>Golden Pass Export - Train 2</td><td>Feb-27</td><td>8.3</td><td>-</td><td>-</td><td>4.6</td><td>-</td><td>-</td><td>4.6</td></tr><tr><td>US</td><td>CP2 LNG Phase 1 + 2</td><td>Sep-27</td><td>39.7</td><td>-</td><td>-</td><td>4.2</td><td>-</td><td>-</td><td>4.2</td></tr><tr><td>US</td><td>Port Arthur LNG - Phase 1 - Train 1</td><td>Dec-27</td><td>8.9</td><td>-</td><td>-</td><td>0.1</td><td>-</td><td>-</td><td>0.1</td></tr><tr><td>Nigeria</td><td>NLNG Seven - Train 1</td><td>Jul-27</td><td>5.3</td><td>-</td><td>-</td><td>1.3</td><td>-</td><td>-</td><td>1.3</td></tr><tr><td>Indonesia</td><td>Genting FLNG</td><td>Jul-27</td><td>1.6</td><td>-</td><td>-</td><td>0.4</td><td>-</td><td>-</td><td>0.4</td></tr><tr><td>Qatar</td><td>Qatar North Field East - Train 1</td><td>Sep-27</td><td>11.0</td><td>-</td><td>-</td><td>1.7</td><td>-</td><td>-</td><td>1.7</td></tr><tr><td>Gabon</td><td>Gabon FLNG</td><td>Sep-27</td><td>1.0</td><td>-</td><td>-</td><td>0.2</td><td>-</td><td>-</td><td>0.2</td></tr><tr><td>Mexico</td><td>Altamira FLNG 1</td><td>Dec-27</td><td>1.9</td><td>-</td><td>-</td><td>0.0</td><td>-</td><td>-</td><td>0.0</td></tr><tr><td></td><td>Total 2025 projects</td><td></td><td></td><td>32.0</td><td>72.5</td><td>78.5</td><td>32.0</td><td>40.5</td><td>6.0</td></tr><tr><td></td><td>Total 2026 projects</td><td></td><td></td><td>-</td><td>11.2</td><td>23.4</td><td>-</td><td>11.2</td><td>12.3</td></tr><tr><td></td><td>Total 2027 projects</td><td></td><td></td><td>-</td><td>-</td><td>12.5</td><td>-</td><td>-</td><td>12.5</td></tr><tr><td></td><td>Total 2025-27 projects</td><td></td><td></td><td>32.0</td><td>83.6</td><td>114.5</td><td>32.0</td><td>51.7</td><td>30.8</td></tr><tr><td>Qatar</td><td>Existing 14 trains</td><td></td><td></td><td>112.6</td><td>60.2</td><td>87.3</td><td>4.7</td><td>-52.4</td><td>27.0</td></tr><tr><td>UAE</td><td>Existing 2 trains</td><td></td><td></td><td>6.3</td><td>4.6</td><td>6.7</td><td>-1.2</td><td>-1.8</td><td>2.1</td></tr><tr><td></td><td>Rest of the world</td><td></td><td></td><td>448.0</td><td>451.6</td><td>451.6</td><td>2.3</td><td>3.6</td><td>-</td></tr><tr><td></td><td>Grand total</td><td></td><td></td><td>598.9</td><td>600.1</td><td>660.1</td><td>37.8</td><td>1.2</td><td>60.0</td></tr></table>

Corpus Christi LNG stage 3 capacity includes potential de-bottlenecking (2mtpa across 9 mid-scale trains). CP2 capacity excludes bolt-on 10mtpa, which is expected in 2028 Source: Wood Mackenzie, company data, Bloomberg Finance L.P., JPM Commodities Research

# LNG shipments through major maritime routes

Figure 9: LNG vessels through the Strait of Hormuz  
n of vessels, 7 day moving sum  
![](images/01d3f928d9eb1e7dae439d5e7d0c52e7ee3e331690ad842da655cc23c0631587.jpg)

<details>
<summary>line chart</summary>

| Date     | Range 2021-24 | Avg 2021-24 | 2025 | 2026 |
|----------|---------------|-------------|------|------|
| 01-Jan   | ~40           | ~40         | ~40  | ~50  |
| 01-Feb   | ~45           | ~45         | ~45  | ~45  |
| 01-Mar   | ~50           | ~45         | ~60  | 0    |
| 01-Apr   | ~45           | ~45         | ~50  | 0    |
| 01-May   | ~45           | ~45         | ~50  | 0    |
| 01-Jun   | ~45           | ~45         | ~50  | 0    |
| 01-Jul   | ~45           | ~45         | ~50  | 0    |
| 01-Aug   | ~45           | ~45         | ~50  | 0    |
| 01-Sep   | ~45           | ~45         | ~50  | 0    |
| 01-Oct   | ~45           | ~45         | ~50  | 0    |
| 01-Nov   | ~45           | ~45         | ~50  | 0    |
| 01-Dec   | ~45           | ~45         | ~50  | 0    |
</details>

Includes all passages by laden and ballast vessels  
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 11: LNG vessels through the Panama Canal  
n of vessels, 7 day moving sum  
![](images/2e4e3dc16160bbc42f12b91dec11ae7b9734c2cdf1732f5a1adaeb0ad9898936.jpg)

<details>
<summary>line chart</summary>

| Date     | Range 2020-24 | Avg 2020-24 | 2025 | 2026 |
|----------|---------------|-------------|------|------|
| 01-Jan   | ~10           | ~6          | ~1   | ~3   |
| 01-Feb   | ~17           | ~7          | ~1   | ~1   |
| 01-Mar   | ~10           | ~5          | ~1   | ~1   |
| 01-Apr   | ~10           | ~5          | ~1   | ~3   |
| 01-May   | ~10           | ~5          | ~1   | ~4   |
| 01-Jun   | ~10           | ~5          | ~1   | ~3   |
| 01-Jul   | ~18           | ~7          | ~3   | ~3   |
| 01-Aug   | ~15           | ~8          | ~4   | ~3   |
| 01-Sep   | ~10           | ~6          | ~3   | ~3   |
| 01-Oct   | ~10           | ~6          | ~3   | ~3   |
| 01-Nov   | ~10           | ~6          | ~3   | ~3   |
| 01-Dec   | ~10           | ~6          | ~3   | ~3   |
</details>

Includes all passages by laden and ballast vessels  
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 10: LNG vessels through the Suez Canal  
n of vessels, 7 day moving sum  
![](images/a2f0cbd92c9bd6278731eb610e5c0e4b3167bc4fa007ab689afd21b260455220.jpg)

<details>
<summary>line chart</summary>

| Date     | Range 2021-24 | Avg 2021-24 | 2025 | 2026 |
|----------|---------------|-------------|------|------|
| 01-Jan   | ~15           | ~12         | ~3   | ~5   |
| 01-Feb   | ~25           | ~13         | ~4   | ~7   |
| 01-Mar   | ~18           | ~11         | ~3   | ~6   |
| 01-Apr   | ~28           | ~14         | ~5   | ~8   |
| 01-May   | ~20           | ~13         | ~6   | ~7   |
| 01-Jun   | ~15           | ~11         | ~4   | ~

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 08 Jun 2026 10:18 PM BST

Disseminated 08 Jun 2026 10:22 PM BST
"""
