你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
2026 Jan-Jun Exports YoY Growth Rate (RHS)

## China EV Monthly Chartbook: The Summer Lull

Domestic demand remained soft in Jun-26, with PV wholesale and retail sales down 6% and 23% YoY, while NEV penetration eased from May's peak. Exports stayed the key bright spot, surging 80% YoY to a record 905k units, led by Chery, BYD, Geely and SAIC, as Chinese brands continued gaining overseas share. Pricing pressure persisted, with retail ASP down 2% MoM to RMB170k and Chinese NEV prices falling 9% YoY. Details below.

## NEV insurance penetration eased to 60.3%.

\- PV wholesale volume reached 2.4mn units (-5.6% YoY, +6.6% MoM), with exports (+80% YoY to 904.5k) maintaining strong momentum. Retail came in at 1.66mn units (-23% YoY, +13% MoM).

\- NEV PV wholesale volume was 1.52mn units, up 21.3% YoY and 9.8% MoM. Domestic NEV insurance penetration eased to 60.3% (off May's record 62.3%); BEV at 41.6%, PHEV at 18.7%.

\- On market share, Leapmotor, Geely and NIO all outperformed in 1H26, with share up 1.3/1.2/1.2ppt YoY. Leapmotor stood out with 1H26 retail up 45% YoY (Jun-26 +73% YoY to 70k units), while NIO also accelerated (+68% 1H26 YoY; Jun-26 +88% YoY to 41k units). BYD continued to lose ground (-38% 1H26 YoY), while most JV/luxury brands (Ford, Honda, Mercedes all down 30%+ in Jun) continued to underperform.

## Exports remained the bright spot.

\- PV exports hit another record of 904.5k units in Jun-26 (+80% YoY, +12% MoM). Chery, BYD, Geely and SAIC continued to dominate, accounting for c.67% of total shipments. Geely was the clear winner, expanding export share by 5.8ppt YoY following a 213% surge in 1H26 exports, while SAIC lost 1.5ppt of share.

\- Share gains remained broad-based across regions. Chinese brands captured 9.1% of the European PV market and 19.7% of NEVs, with Chery (+1.1ppt YTD) and BYD (+0.8ppt) leading gains. Southeast Asia recovered to 15.4% share (56% in NEVs), while Latin America remained the deepest market at 16.3% share and \~87% of NEV sales. Across both regions, Chery, BYD and Geely remained the primary share gainers.

Average retail ASP slipped to RMB170k (-2% MoM, flat YoY), as the mix turned less supportive. BEV ASP nudged up 1% MoM while ICE fell 3%. Chinese NEV ASP declined 2% MoM and a steep 9% YoY (price competition still biting), and Chinese ICE ASP also gave back 2% MoM. Luxury stayed soft (-2% MoM, Mercedes -7%, BMW -6%, Audi -2% all down) and JVs eased 3% MoM. Within premium NEVs, the dispersion widened further: NIO (+15% MoM, hitting RMB443k), AITO (+19%), Tank (+1%) and Tesla (+4%) firmed up, while Li Auto (-1%), Zeekr (-1%) and Xiaomi (-2%) all weakened.

New models. The 409th MIIT catalog reads as a coordinated push into segments still held by JV and luxury brands. Xiaomi's first EREV (N90/N70) takes on Li Auto and AITO with class-leading pure-electric range and a rotating-seat, flat-floor interior; Li Auto i9 arrives at \~Rmb 450k with MEGA-class space; Geely BattleShip 700 and Chery iCAR V25 open a sub-Rmb 200k boxy-SUV lane against Haval H9 and Honda CR-V; BYD refreshes the top of its stack (new Tang, Denza Z9S) plus the entry Seagull. The pattern is consistent: larger footprints, longer EV-only range on PHEV/EREV, and pricing set to keep pressuring incumbents.

Reduce BAIC PT: We revise our FY26/FY27 forecasts for BAIC to reflect improving gross margins in the self-owned brand business. However, our FY26-FY27 sales volume forecasts

<table><tr><td colspan="3">KEY STOCKS FEATURED INCLUDE:</td></tr><tr><td>TICKER</td><td>RATING</td><td>PRICE TARGET</td></tr><tr><td>600733 CH</td><td>HOLD</td><td>Rmb4.50</td></tr></table>

KEY CHANGES INCLUDE:

<table><tr><td>TICKER</td><td>RATING</td><td>PRICE TARGET</td></tr><tr><td>600733 CH</td><td>HOLD</td><td>↓ Rmb4.50 (Rmb8.40)</td></tr></table>

Exhibit 1 - China NEV Monthly Insurance Sales Penetration Reached 60.3% in Jun-26  
![](images/5520d476e62500d61acd455dad90fcb9fdfc9a2f7552ef561cacd1e6f4e9b30a.jpg)  
Source: ThinkerCar, JEF

Exhibit 2 - Chery and BYD Led China's 1H26 PV Exports, Leapmotor Posted Sharpest YoY Gain  
![](images/1a6ff4b910a9ea5785c76c76be058de3385c6c94f00783e84f49b14460255f1b.jpg)  
Source: Marklines, JEF

Exhibit 3 - 1H26 Exports (+72%) and NEVs  
(+7%) Offset Weak Domestic Demand (-24%)

<table><tr><td></td><td colspan="2">JAN-20E 2016 YTD</td><td colspan="3">JAN-20E MONTHLY</td></tr><tr><td>Metric</td><td>Vol. (mm)</td><td>YoY</td><td>Vol. (mm)</td><td>YoY</td><td>YoY</td></tr><tr><td colspan="6">TOTAL VEHICLE WHOLESALE</td></tr><tr><td>Total Wholesale</td><td>15,916</td><td>-4.0%</td><td>2,810</td><td>-3.2%</td><td>6.9%</td></tr><tr><td>of which: NEV</td><td>7,445</td><td>7.4%</td><td>1,643</td><td>23.6%</td><td>9.8%</td></tr><tr><td>of which: ICE</td><td>7,571</td><td>-13.1%</td><td>1,817</td><td>-25.9%</td><td>3.0%</td></tr><tr><td colspan="6">PASISING CAR WHOLESALE</td></tr><tr><td>Passenger Car Total</td><td>13,719</td><td>-6.0%</td><td>2,402</td><td>-5.3%</td><td>6.6%</td></tr><tr><td>of which: NEV</td><td>6,006</td><td>5.6%</td><td>1,517</td><td>33.3%</td><td>9.8%</td></tr><tr><td>of which: ICE</td><td>5,823</td><td>-16.7%</td><td>8,085</td><td>-31.1%</td><td>1.5%</td></tr><tr><td>Domestic (Wholesale - Exporte)</td><td>8,287</td><td>-24.3%</td><td>1,457</td><td>-35.4%</td><td>3.7%</td></tr><tr><td>NEV Domestic</td><td>4,597</td><td>-18.6%</td><td>1,907</td><td>-4.5%</td><td>6.3%</td></tr><tr><td>ICE Domestic</td><td>3,930</td><td>-22.2%</td><td>6,649</td><td>-45.9%</td><td>-1.3%</td></tr><tr><td>Export (Passenger Car)</td><td>4,632</td><td>72.6%</td><td>9,005</td><td>88.2%</td><td>11.7%</td></tr><tr><td>NEV Export</td><td>2,300</td><td>118.3%</td><td>5,110</td><td>119.3%</td><td>17.3%</td></tr><tr><td>ICE Export</td><td>2,133</td><td>36.6%</td><td>3,284</td><td>19.3%</td><td>5.3%</td></tr><tr><td colspan="6">COMMERCIAL VEHICLE WHOLESALE</td></tr><tr><td>Truck Total</td><td>2,018</td><td>8.7%</td><td>3,347</td><td>9.7%</td><td>7.3%</td></tr><tr><td>Heavy Truck</td><td>9,001</td><td>37.6%</td><td>1,117</td><td>19.2%</td><td>6.0%</td></tr><tr><td>Light Truck</td><td>1,046</td><td>1.8%</td><td>0,185</td><td>8.9%</td><td>7.5%</td></tr><tr><td>Medium Truck</td><td>0,075</td><td>25.3%</td><td>0,013</td><td>36.4%</td><td>-2.0%</td></tr><tr><td>Mini Truck</td><td>0,237</td><td>6.7%</td><td>0,032</td><td>19.2%</td><td>12.9%</td></tr><tr><td>Total</td><td>1,278</td><td>5.6%</td><td>0,842</td><td>10.4%</td><td>10.4%</td></tr></table>

Source: CAAM, CBIRC, JEF

Xiaoyi Lei \* | Equity Analyst

852 3767 1126 | xiaoyi.lei@JEF.com

Aaron Wang \* | Equity Analyst

+852 3767 1121 | aaron.wang@JEF.com

Philippe Houchois ^ | Equity Analyst

44 (0) 20 7029 8983 | philippe.houchois@JEF.com

Vanessa Jeffriess ‡ | Equity Analyst
44 (0)20 7548 4123 | vjeffriess@JEF.com

Owen Paterson ‡ | Equity Analyst
+44 (0)20 7548 4745 | opaterson@JEF.com

remain below market expectations, as we think the overall PV market will continue to face pressures next year. Given the auto sector's derating year-to-date in 2026, we lower our price target to RMB4.5, based on 0.7x FY26E P/S, in line with the sector average multiple. Maintain Hold.

## Summary of Changes

<table><tr><td colspan="4"></td><td colspan="3">EPS Estimates</td><td colspan="3">P/E</td></tr><tr><td>Company</td><td>Rating</td><td>Price^</td><td>Price Target</td><td>2025</td><td>2026</td><td>2027</td><td>2025</td><td>2026</td><td>2027</td></tr><tr><td rowspan="2">BAIC EV 600733 CH</td><td rowspan="2">HOLD</td><td rowspan="2">Rmb4.62</td><td>Rmb4.50</td><td>RMB(0.82)</td><td>RMB(0.56)</td><td>RMB(0.28)</td><td rowspan="2">NM</td><td rowspan="2">NM</td><td rowspan="2">NM</td></tr><tr><td>↓ -46%</td><td>↑ +5%</td><td>↑ +22%</td><td>↑ +55%</td></tr><tr><td>Previous</td><td></td><td></td><td>Rmb8.40</td><td>RMB(0.86)</td><td>RMB(0.71)</td><td>RMB(0.63)</td><td></td><td></td><td></td></tr></table>

^Prior trading day's closing price unless otherwise noted.

## Table of Contents

Export Sales 5
Volume 14
Weekly New Orders 17
Pricing 18
New Models 19
Inventory 20
Cost 21
Bluepark (600733 CH) 22

Exhibit 4 - China Autos Market - Jun 2026 Monthly Sales & YTD Summary

<table><tr><td colspan="4">JAN-JUN 2026 YTD TOTAL SALES</td><td colspan="3">JAN-JUN 2026 YTD EXPORTS</td><td colspan="3">JAN-JUN 2026 YTD RETAILS</td></tr><tr><td>OEM</td><td>YTD Sales</td><td>YoY</td><td>MoM</td><td>YTD Exports</td><td>YoY</td><td>MoM</td><td>YTD Retails</td><td>YoY</td><td>MoM</td></tr><tr><td>BYD</td><td>1,808,511</td><td>-15.7%</td><td>28.7%</td><td>769,330</td><td>73.6%</td><td>28.6%</td><td>974,344</td><td>-37.7%</td><td>12.9%</td></tr><tr><td>Chery Group</td><td>1,279,172</td><td>6.75%</td><td>23.23%</td><td>914,859</td><td>72.47%</td><td>25.37%</td><td>431,191</td><td>-30.88%</td><td>17.90%</td></tr><tr><td>Geely + ZEEKR</td><td>1,676,725</td><td>3.3%</td><td>20.9%</td><td>576,232</td><td>155.3%</td><td>27.5%</td><td>958,221</td><td>-11.2%</td><td>3.9%</td></tr><tr><td>Great Wall Motor</td><td>583,358</td><td>2.39%</td><td>22.72%</td><td>256,000</td><td>52.77%</td><td>26.32%</td><td>265,229</td><td>-14.53%</td><td>11.98%</td></tr><tr><td>SAIC Group</td><td>1,987,273</td><td>-0.5%</td><td>23.8%</td><td>623,780</td><td>57.2%</td><td>24.1%</td><td>163,618</td><td>29.7%</td><td>31.2%</td></tr><tr><td>Leapmotor</td><td>356,487</td><td>60.82%</td><td>35.49%</td><td>96,294</td><td>372.61%</td><td>27.89%</td><td>258,719</td><td>44.86%</td><td>11.38%</td></tr><tr><td>NIO</td><td>191,123</td><td>67.4%</td><td>27.0%</td><td>N/D</td><td>—</td><td>—</td><td>195,860</td><td>67.6%</td><td>16.3%</td></tr><tr><td>Seres Group</td><td>190,032</td><td>-0.1%</td><td>22.8%</td><td>17,420</td><td>48.6%</td><td>20.5%</td><td>161,399</td><td>1.0%</td><td>-15.1%</td></tr><tr><td>Li Auto</td><td>193,472</td><td>-5.1%</td><td>19.0%</td><td>N/D</td><td>—</td><td>—</td><td>191,361</td><td>-8.1%</td><td>-5.8%</td></tr><tr><td>XPENG</td><td>165,977</td><td>-15.83%</td><td>31.88%</td><td>31,599</td><td>68.97%</td><td>31.30%</td><td>133,590</td><td>-25.74%</td><td>24.26%</td></tr><tr><td>Xiaomi Auto</td><td>185,055</td><td>17.2%</td><td>23.1%</td><td>N/D</td><td>—</td><td>—</td><td>186,189</td><td>17.7%</td><td>5.6%</td></tr></table>

Source: CAAM, CBIRC, JEF

Exhibit 5 - China Autos Market - 1H26 vs. 2025

<table><tr><td colspan="3">JAN-JUN 2026 YTD</td><td colspan="3">JUN 2026 MONTHLY</td></tr><tr><td>Metric</td><td>Vol. (mn)</td><td>YoY</td><td>Vol. (mn)</td><td>YoY</td><td>MoM</td></tr><tr><td colspan="3">TOTAL VEHICLE WHOLESALE</td><td colspan="3"></td></tr><tr><td>Total Wholesale</td><td>15.016</td><td>-4.0%</td><td>2.810</td><td>-3.2%</td><td>6.9%</td></tr><tr><td>of which: NEV</td><td>7.445</td><td>7.4%</td><td>1.643</td><td>23.6%</td><td>9.8%</td></tr><tr><td>of which: ICE</td><td>7.571</td><td>-13.1%</td><td>1.167</td><td>-25.9%</td><td>3.0%</td></tr><tr><td colspan="3">PASSENGER CAR WHOLESALE</td><td colspan="3"></td></tr><tr><td>Passenger Car Total</td><td>12.719</td><td>-6.0%</td><td>2.402</td><td>-5.3%</td><td>6.6%</td></tr><tr><td>of which: NEV</td><td>6.896</td><td>5.6%</td><td>1.517</td><td>21.3%</td><td>9.8%</td></tr><tr><td>of which: ICE</td><td>5.823</td><td>-16.7%</td><td>0.885</td><td>-31.1%</td><td>1.5%</td></tr><tr><td>Domestic (Wholesale - Exports)</td><td>8.287</td><td>-24.3%</td><td>1.497</td><td>-26.4%</td><td>3.7%</td></tr><tr><td>NEV Domestic</td><td>4.597</td><td>-16.8%</td><td>1.007</td><td>-4.5%</td><td>6.3%</td></tr><tr><td>ICE Domestic</td><td>3.690</td><td>-32.0%</td><td>0.490</td><td>-49.9%</td><td>-1.3%</td></tr><tr><td>Export (Passenger Car)</td><td>4.432</td><td>72.0%</td><td>0.905</td><td>80.2%</td><td>11.7%</td></tr><tr><td>NEV Export</td><td>2.300</td><td>128.0%</td><td>0.510</td><td>159.3%</td><td>17.3%</td></tr><tr><td>ICE Export</td><td>2.133</td><td>36.0%</td><td>0.394</td><td>29.3%</td><td>5.3%</td></tr><tr><td colspan="3">COMMERCIAL VEHICLE WHOLESALE</td><td colspan="3"></td></tr><tr><td>Truck Total</td><td>2.018</td><td>8.7%</td><td>0.347</td><td>9.7%</td><td>7.3%</td></tr><tr><td>Heavy Truck</td><td>0.661</td><td>22.6%</td><td>0.117</td><td>19.2%</td><td>6.5%</td></tr><tr><td>Light Truck</td><td>1.046</td><td>1.0%</td><td>0.185</td><td>9.9%</td><td>7.5%</td></tr><tr><td>Medium Truck</td><td>0.075</td><td>25.3%</td><td>0.013</td><td>30.4%</td><td>-2.0%</td></tr><tr><td>Mini Truck</td><td>0.237</td><td>6.7%</td><td>0.032</td><td>-19.2%</td><td>12.9%</td></tr><tr><td>Bus Total</td><td>0.278</td><td>5.0%</td><td>0.062</td><td>16.6%</td><td>16.4%</td></tr></table>

Source: CAAM, CBIRC, JEF

## Export Sales

Exhibit 6 - PV Exports Improved 80% YoY to 904.5k Units  
![](images/3bc319652e2bed22a098ad5d2b9abfc969f4611d94b808844a7b2fffa2097a99.jpg)  
Source: CAAM, JEF

Exhibit 7 - NEV Exports Improved 113% YoY to 434.7k Units  
![](images/cb8ef9279584719a41314e275555ca8adbb36e60c57b42495c4ab2a6b28ab5ba.jpg)  
Source: CAAM, JEF

Exhibit 8 - Export Volume by Major Domestic Brand

<table><tr><td>DEMs</td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>2025</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>YoY</td><td>MoM</td><td>6Mx YoY Change</td></tr><tr><td>SAIC</td><td>54,449</td><td>53,740</td><td>64,620</td><td>69,251</td><td>80,055</td><td>74,712</td><td>64,861</td><td>74,087</td><td>83,186</td><td>80,179</td><td>87,181</td><td>84,272</td><td>870,793</td><td>89,353</td><td>84,328</td><td>102,477</td><td>115,799</td><td>110,700</td><td>121,123</td><td>62.1%</td><td>9.4%</td><td>57.2%</td></tr><tr><td>Chery</td><td>78,481</td><td>84,711</td><td>83,529</td><td>84,220</td><td>97,030</td><td>102,472</td><td>115,379</td><td>123,624</td><td>131,507</td><td>120,598</td><td>131,940</td><td>140,786</td><td>1,294,277</td><td>116,985</td><td>116,829</td><td>146,030</td><td>172,114</td><td>177,742</td><td>185,159</td><td>80.7%</td><td>4.2%</td><td>72.5%</td></tr><tr><td>Tesla</td><td>29,535</td><td>3,911</td><td>4,701</td><td>29,728</td><td>23,074</td><td>10,115</td><td>27,269</td><td>26,040</td><td>19,287</td><td>35,491</td><td>13,555</td><td>3,328</td><td>226,034</td><td>50,644</td><td>20,393</td><td>29,563</td><td>53,522</td><td>38,701</td><td>36,171</td><td>257.6%</td><td>-6.5%</td><td>126.6%</td></tr><tr><td>GWM</td><td>23,871</td><td>25,805</td><td>26,641</td><td>27,837</td><td>28,525</td><td>34,896</td><td>35,831</td><td>39,875</td><td>44,832</td><td>51,690</td><td>50,775</td><td>51,704</td><td>442,282</td><td>34,612</td><td>36,947</td><td>40,897</td><td>45,015</td><td>45,188</td><td>53,341</td><td>52.9%</td><td>18.0%</td><td>52.8%</td></tr><tr><td>Geely</td><td>27,354</td><td>25,552</td><td>37,047</td><td>24,133</td><td>30,017</td><td>40,011</td><td>35,272</td><td>36,077</td><td>40,665</td><td>41,568</td><td>42,091</td><td>40,310</td><td>430,097</td><td>76,168</td><td>78,017</td><td>98,423</td><td>99,596</td><td>99,762</td><td>124,266</td><td>210.6%</td><td>24.6%</td><td>213.0%</td></tr><tr><td>Chang&#x27;an</td><td>47,023</td><td>34,821</td><td>31,172</td><td>23,694</td><td>23,883</td><td>29,033</td><td>31,725</td><td>35,172</td><td>38,827</td><td>32,828</td><td>28,462</td><td>16,825</td><td>373,465</td><td>24,305</td><td>45,278</td><td>70,216</td><td>49,253</td><td>46,388</td><td>61,735</td><td>112.6%</td><td>33.1%</td><td>56.7%</td></tr><tr><td>BYD</td><td>66,336</td><td>67,025</td><td>67,307</td><td>72,405</td><td>84,068</td><td>85,957</td><td>78,364</td><td>79,603</td><td>69,258</td><td>80,108</td><td>128,067</td><td>131,637</td><td>1,010,135</td><td>96,859</td><td>98,706</td><td>116,882</td><td>130,042</td><td>155,944</td><td>170,897</td><td>98.8%</td><td>9.6%</td><td>73.6%</td></tr><tr><td>JAC</td><td>9,010</td><td>8,794</td><td>9,229</td><td>9,745</td><td>11,201</td><td>6,753</td><td>8,079</td><td>13,712</td><td>11,130</td><td>9,428</td><td>11,515</td><td>8,661</td><td>117,257</td><td>5,270</td><td>4,317</td><td>6,843</td><td>7,944</td><td>5,670</td><td>9,846</td><td>45.8%</td><td>73.7%</td><td>-27.1%</td></tr><tr><td>GAC</td><td>3,186</td><td>4,742</td><td>12,788</td><td>7,572</td><td>8,539</td><td>13,391</td><td>10,389</td><td>8,349</td><td>12,594</td><td>12,869</td><td>17,286</td><td>13,451</td><td>135,156</td><td>13,324</td><td>17,024</td><td>26,852</td><td>17,653</td><td>16,372</td><td>21,149</td><td>57.9%</td><td>29.2%</td><td>123.8%</td></tr><tr><td>FAW</td><td>6,300</td><td>4,271</td><td>4,926</td><td>5,506</td><td>5,501</td><td>9,255</td><td>3,308</td><td>3,524</td><td>4,254</td><td>4,474</td><td>7,284</td><td>10,217</td><td>68,820</td><td>2,386</td><td>2,822</td><td>6,212</td><td>11,051</td><td>5,868</td><td>10,306</td><td>11.4%</td><td>75.6%</td><td>8.1%</td></tr><tr><td>Others</td><td>49,855</td><td>57,227</td><td>68,433</td><td>76,944</td><td>75,866</td><td>95,273</td><td>88,976</td><td>92,834</td><td>103,897</td><td>102,173</td><td>105,439</td><td>140,075</td><td>1,056,992</td><td>78,981</td><td>80,861</td><td>104,104</td><td>93,528</td><td>107,108</td><td>110,516</td><td>16.0%</td><td>3.2%</td><td>35.8%</td></tr><tr><td>Total</td><td>395,400</td><td>370,599</td><td>410,393</td><td>431,035</td><td>467,759</td><td>501,868</td><td>499,453</td><td>532,897</td><td>559,637</td><td>571,406</td><td>623,595</td><td>641,266</td><td>6,005,308</td><td>588,887</td><td>585,522</td><td>748,499</td><td>795,517</td><td>809,443</td><td>904,509</td><td>80.2%</td><td>11.7%</td><td>72.0%</td></tr></table>

Source: Marklines, JEF

Exhibit 9 - Export Market Share by Major Domestic Brand

<table><tr><td>OEMs</td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-26</td><td>2025</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>YoY</td><td>MoM</td><td>6M26 YoY Change</td></tr><tr><td>SAIC</td><td>13.8%</td><td>14.5%</td><td>15.7%</td><td>16.1%</td><td>17.1%</td><td>14.9%</td><td>13.0%</td><td>13.9%</td><td>14.9%</td><td>14.0%</td><td>14.0%</td><td>13.1%</td><td>14.5%</td><td>15.2%</td><td>14.4%</td><td>13.7%</td><td>14.6%</td><td>13.7%</td><td>13.4%</td><td>-1.5%</td><td>-0.3%</td><td>-1.2%</td></tr><tr><td>Chery</td><td>19.8%</td><td>22.9%</td><td>20.4%</td><td>19.5%</td><td>20.7%</td><td>20.4%</td><td>23.1%</td><td>23.2%</td><td>23.5%</td><td>21.1%</td><td>21.2%</td><td>22.0%</td><td>21.6%</td><td>19.9%</td><td>20.0%</td><td>19.5%</td><td>21.6%</td><td>22.0%</td><td>20.5%</td><td>0.1%</td><td>-1.5%</td><td>-0.

[中间内容因长度限制已省略]

lar investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
