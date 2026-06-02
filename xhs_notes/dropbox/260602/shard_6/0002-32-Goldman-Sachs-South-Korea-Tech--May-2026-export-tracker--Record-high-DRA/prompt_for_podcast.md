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
# South Korea Tech: May 2026 export tracker: Record-high DRAM exports with 370% yoy growth

According to the MOTIE (Ministry of Trade, Industry and Energy) and the TRASS (Trade Statistics Service), exports for the major tech products we track (memory, OLED, Li-ion batteries, and MLCC) showed an overall positive trend. Export value for OLED (+3% yoy), Li-ion batteries (+53% yoy), MLCC (+14% yoy), and WFE equipment (+66% yoy) all achieved positive growth rates for May, with memory exports delivering significant growth of 255% yoy, marking 4 consecutive months of 200%+ yoy growth. WFE equipment import also showed strong growth of +99% yoy. There was 1 less working day compared to May 2025 (20.5 days in May 2026 vs 21.5 days in May 2025). Key points are: 1) memory exports continued their solid growth trend (+255% yoy) in May, 2) Hynix HBM epoxide resin imports and SEC plastic film imports for HBM increased 57% yoy and 96% yoy respectively, and 3) WFE equipment import increased 99% yoy.

Memory: 4 consecutive months of 200%+ yoy growth; DRAM exports 370% yoy; NAND chip exports continue strong trend with 7 consecutive months of triple-digit growth (+207% yoy)

Memory exports showed strong yoy growth of +255% yoy in May, extending 200%+ yoy growth trend to 4 consecutive periods. DRAM exports also showed robust growth of +370% yoy, the highest figure since tracking began in January 2008. Both NAND and SSD export showed strong results (NAND chip exports: +207% yoy, SSD exports: +338% yoy). MOTIE attributed the overall solid results to robust demand from Big Tech firms in major export markets (U.S. and China). For Korean companies, we expect Hynix's 2Q26 revenue to increase by 271% yoy and SEC's memory revenue to increase by 452% yoy, with SEC's stronger growth coming from its higher exposure to conventional memory products and a low base in HBM revenue.

HBM: April Hynix epoxide resin imports +57% yoy; SEC plastic film imports +96% yoy

We track 1) import data for epoxide resins from Japan to Icheon/Cheongju (where Hynix's HBM production bases are located) as we believe Hynix mainly sources its MR-MUF materials from the Japanese company Namics, and 2) import data for plastic film from Japan to Hwaseong/Pyeongtaek (where SEC's HBM production bases are located), as we believe SEC mainly sources its TC-NCF materials from Japanese company Resonac. Import trends for epoxide resins/plastic film have been showing a strong correlation with Hynix/SEC's HBM shipment (Hynix: Exhibit 1 / SEC: Exhibit 2), respectively; hence we believe these could be good proxies to gauge the

Giuni Lee

+82(2)3788-1177 | giuni.lee@gs.com

GS (Asia) L.L.C., Seoul

Branch

Daiki Takayama

+81(3)4587-9870

daiki.takayama@gs.com

GS Japan Co., Ltd.

Taeyong Lee

+82(2)3788-0981 | taeyong.lee@gs.com

GS (Asia) L.L.C., Seoul

Branch

HBM shipment scale of Hynix/SEC.

In April, the import value of epoxide resins from Japan to Icheon/Cheongju increased by 57% yoy and the import value of plastic film from Japan to Hwaseong/Pyeongtaek increased by 96% yoy.

# Display: High single-digit% yoy rebound

Display exports increased by 9% yoy in May, with OLED (+3% yoy) and LCD (+30% yoy) both showing positive growth. MOTIE noted that launch of new OLED mobile products contributed to this increase despite contraction of end-market demand due to higher semiconductor costs. For Korean display names, we expect 2Q26 LG Display revenue to decline by 5% yoy due to LCD business downsizing but Samsung Display revenue to increase by 15% yoy.

# MLCC: Export value growth turns positive in May after slight dip in April

MLCC exports returned to positive territory (+14% yoy) in May, after short decline (-4% yoy) in April ended its 12-month consecutive positive growth trend. For Samsung Electro-Mechanics (SEMCO), we expect MLCC revenue to grow by 22% yoy in 2Q26 mainly led by continued strength in AI server/auto MLCCs.

# Li-ion batteries: strong rebound again spotted

Li-ion battery export increased by 53% yoy in May after negative growth in April (-10% yoy). MOTIE commented that increase of EV and ESS battery export towards key markets (U.S. and China) along with ASP hike resulting from elevated price of key minerals contributed to the positive result.

# WFE: Strong yoy growth for exports and imports in May

Semi WFE exports and import showed yoy growth of +66% yoy and +99% yoy in May respectively, which we believe the strong import growth comes from the increasing capex of the memory suppliers in an effort to alleviate the supply tightness, and the solid export growth from the strong global spending in building semis capacity.

Exhibit 1: Import trends of epoxide resins have been showing a strong correlation with Hynix's HBM shipments
Imports trend for epoxide resins from Japan to Hynix   
![](images/406553bbabf25f17b0d206fa1aa5be7c6e3e0dea13b17ec36d8133a23939f6e8.jpg)

<details>
<summary>bar_line</summary>

| Quarter | Hynix HBM shipment (bn Gb) (RHS) ($ mn) | Hynix MR-MUF import value (US$mn) (LHS) ($ mn) |
| :--- | :--- | :--- |
| 1Q23 | 1.5 | 0.1 |
| 2Q23 | 3.5 | 0.4 |
| 3Q23 | 5.0 | 0.7 |
| 4Q23 | 6.5 | 0.6 |
| 1Q24 | 7.0 | 0.7 |
| 2Q24 | 13.0 | 2.0 |
| 3Q24 | 21.5 | 2.8 |
| 4Q24 | 33.5 | 3.1 |
| 1Q25 | 32.0 | 2.3 |
| 2Q25 | 36.0 | 3.6 |
| 3Q25 | 38.5 | 4.2 |
| 4Q25 | 41.0 | 3.9 |
| 1Q26 | 51.5 | 2.7 |
</details>

Epoxide resins import (JP to Hynix) = Import value of epoxide resins from Japan to Icheon/Cheongju where Hynix's HBM production bases are located.

Exhibit 2: Imports trend for plastic film has been showing a strong correlation with SEC's HBM shipment
Import trend of plastic film from Japan to SEC   
![](images/c42bcf556ac102c7ef725b3f0f58b112b92e060be45554daf390a6825e982ba0.jpg)

<details>
<summary>bar_line</summary>

| Quarter | SEC HBM shipment (bn Gb) (RHS) ($ mn) | SEC TC-NCF import value (US$mn) (LHS) ($ mn) |
|---|---|---|
| 1Q23 | 2 | 0.05 |
| 2Q23 | 3 | 0.08 |
| 3Q23 | 4.5 | 0.15 |
| 4Q23 | 6.5 | 0.4 |
| 1Q24 | 7 | 0.9 |
| 2Q24 | 10.5 | 1.5 |
| 3Q24 | 17.5 | 2.0 |
| 4Q24 | 32.5 | 2.4 |
| 1Q25 | 8.5 | 0.8 |
| 2Q25 | 11.5 | 1.1 |
| 3Q25 | 21 | 1.9 |
| 4Q25 | 22 | 1.8 |
| 1Q26 | 21.5 | 1.1 |
</details>

Plastic film import (JP to SEC) = Import value of plastic film from Japan to Hwaseong/Pyeongtaek where SEC's HBM production bases are located.   
Source: MOTIE, TRASS, GS Global Investment Research   
Source: MOTIE, TRASS, GS Global Investment Research

Exhibit 3: Monthly exports/imports trends of South Korea Tech companies' major products 

<table><tr><td>Export Value (US$ mn)</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Total semiconductor</td><td>13,794</td><td>14,972</td><td>14,714</td><td>15,098</td><td>16,611</td><td>15,733</td><td>17,258</td><td>20,768</td><td>20,541</td><td>25,143</td><td>32,829</td><td>31,895</td><td>37,157</td></tr><tr><td>Total memory</td><td>9,054</td><td>10,442</td><td>9,473</td><td>10,492</td><td>11,785</td><td>10,919</td><td>12,780</td><td>16,126</td><td>15,720</td><td>21,021</td><td>28,170</td><td>26,973</td><td>32,137</td></tr><tr><td>DRAM</td><td>3,962</td><td>4,504</td><td>4,292</td><td>4,603</td><td>5,099</td><td>4,857</td><td>6,222</td><td>7,646</td><td>8,667</td><td>11,697</td><td>15,423</td><td>15,392</td><td>18,614</td></tr><tr><td>Flash memory</td><td>561</td><td>621</td><td>469</td><td>645</td><td>709</td><td>673</td><td>1,101</td><td>1,276</td><td>1,435</td><td>1,406</td><td>2,545</td><td>1,674</td><td>1,722</td></tr><tr><td>MCP</td><td>4,007</td><td>4,688</td><td>4,195</td><td>4,604</td><td>5,225</td><td>4,749</td><td>4,674</td><td>6,161</td><td>4,883</td><td>6,749</td><td>8,578</td><td>8,157</td><td>9,620</td></tr><tr><td>SSD*</td><td>908</td><td>1,135</td><td>752</td><td>1,032</td><td>1,073</td><td>824</td><td>1,205</td><td>1,796</td><td>1,366</td><td>2,418</td><td>3,190</td><td>3,836</td><td>3,972</td></tr><tr><td>Total display</td><td>1,341</td><td>1,125</td><td>1,573</td><td>1,649</td><td>1,747</td><td>1,477</td><td>1,442</td><td>1,489</td><td>1,379</td><td>1,215</td><td>1,439</td><td>1,285</td><td>1,466</td></tr><tr><td>OLED</td><td>1,021</td><td>818</td><td>1,183</td><td>1,359</td><td>1,457</td><td>1,211</td><td>1,172</td><td>1,183</td><td>1,032</td><td>929</td><td>1,023</td><td>931</td><td>1,050</td></tr><tr><td>LCD</td><td>320</td><td>307</td><td>390</td><td>290</td><td>290</td><td>266</td><td>270</td><td>306</td><td>347</td><td>286</td><td>416</td><td>354</td><td>416</td></tr><tr><td>Total battery</td><td>524</td><td>594</td><td>583</td><td>485</td><td>635</td><td>535</td><td>673</td><td>716</td><td>543</td><td>593</td><td>867</td><td>653</td><td>688</td></tr><tr><td>Li-ion battery</td><td>284</td><td>353</td><td>338</td><td>290</td><td>369</td><td>332</td><td>435</td><td>453</td><td>297</td><td>366</td><td>591</td><td>364</td><td>434</td></tr><tr><td>MLCC</td><td>113</td><td>115</td><td>125</td><td>126</td><td>133</td><td>123</td><td>121</td><td>118</td><td>119</td><td>107</td><td>122</td><td>105</td><td>129</td></tr><tr><td>WFE Equipment</td><td>158</td><td>238</td><td>215</td><td>153</td><td>182</td><td>132</td><td>108</td><td>163</td><td>111</td><td>148</td><td>304</td><td>275</td><td>263</td></tr><tr><td>Import Value (US$ mn)</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>HBM production related datapoints</td><td>17.2</td><td>25.1</td><td>27.6</td><td>25.1</td><td>25.7</td><td>23.3</td><td>21.0</td><td>24.9</td><td>15.2</td><td>15.9</td><td>13.1</td><td>27.6</td><td></td></tr><tr><td>Epoxide resins import (JP to Hynix)</td><td>13.3</td><td>19.8</td><td>19.4</td><td>17.3</td><td>14.5</td><td>14.5</td><td>12.4</td><td>16.0</td><td>11.8</td><td>11.7</td><td>5.8</td><td>15.5</td><td></td></tr><tr><td>Plastic film import (JP to SEC)</td><td>3.9</td><td>5.3</td><td>8.2</td><td>7.9</td><td>11.1</td><td>8.8</td><td>8.6</td><td>9.0</td><td>3.4</td><td>4.2</td><td>7.3</td><td>12.0</td><td></td></tr><tr><td>WFE Equipment</td><td>937</td><td>1,291</td><td>921</td><td>715</td><td>1,716</td><td>1,037</td><td>1,241</td><td>1,573</td><td>1,714</td><td>1,977</td><td>2,137</td><td>1,798</td><td>1,861</td></tr><tr><td colspan="14">MoM, YoY change (%)</td></tr><tr><td>Export (MoM, %)</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Total semiconductor</td><td>18%</td><td>9%</td><td>-2%</td><td>3%</td><td>10%</td><td>-5%</td><td>10%</td><td>20%</td><td>-1%</td><td>22%</td><td>31%</td><td>-3%</td><td>16%</td></tr><tr><td>Total memory</td><td>27%</td><td>15%</td><td>-9%</td><td>11%</td><td>12%</td><td>-7%</td><td>17%</td><td>26%</td><td>-3%</td><td>34%</td><td>34%</td><td>-4%</td><td>19%</td></tr><tr><td>DRAM</td><td>14%</td><td>14%</td><td>-5%</td><td>7%</td><td>11%</td><td>-5%</td><td>28%</td><td>23%</td><td>13%</td><td>35%</td><td>32%</td><td>0%</td><td>21%</td></tr><tr><td>Flash memory</td><td>30%</td><td>11%</td><td>-24%</td><td>38%</td><td>10%</td><td>-5%</td><td>64%</td><td>16%</td><td>12%</td><td>-2%</td><td>81%</td><td>-34%</td><td>3%</td></tr><tr><td>MCP</td><td>41%</td><td>17%</td><td>-11%</td><td>10%</td><td>14%</td><td>-9%</td><td>-2%</td><td>32%</td><td>-21%</td><td>38%</td><td>27%</td><td>-5%</td><td>18%</td></tr><tr><td>SSD*</td><td>93%</td><td>25%</td><td>-34%</td><td>37%</td><td>4%</td><td>-23%</td><td>46%</td><td>49%</td><td>-24%</td><td>77%</td><td>32%</td><td>20%</td><td>4%</td></tr><tr><td>Total display</td><td>2%</td><td>-16%</td><td>40%</td><td>5%</td><td>6%</td><td>-15%</td><td>-2%</td><td>3%</td><td>-7%</td><td>-12%</td><td>18%</td><td>-11%</td><td>14%</td></tr><tr><td>OLED</td><td>5%</td><td>-20%</td><td>45%</td><td>15%</td><td>7%</td><td>-17%</td><td>-3%</td><td>1%</td><td>-13%</td><td>-10%</td><td>10%</td><td>-9%</td><td>13%</td></tr><tr><td>LCD</td><td>-8%</td><td>-4%</td><td>27%</td><td>-26%</td><td>0%</td><td>-8%</td><td>2%</td><td>13%</td><td>13%</td><td>-18%</td><td>45%</td><td>-15%</td><td>18%</td></tr><tr><td>Total battery</td><td>-25%</td><td>13%</td><td>-2%</td><td>-17%</td><td>31%</td><td>-16%</td><td>26%</td><td>6%</td><td>-24%</td><td>9%</td><td>46%</td><td>-25%</td><td>5%</td></tr><tr><td>Li-ion battery</td><td>-29%</td><td>24%</td><td>-4%</td><td>-14%</td><td>27%</td><td>-10%</td><td>31%</td><td>4%</td><td>-34%</td><td>23%</td><td>62%</td><td>-38%</td><td>19%</td></tr><tr><td>MLCC</td><td>3%</td><td>2%</td><td>9%</td><td>1%</td><td>6%</td><td>-8%</td><td>-2%</td><td>-3%</td><td>1%</td><td>-10%</td><td>15%</td><td>-14%</td><td>23%</td></tr><tr><td>WFE Equipment</td><td>-10%</td><td>51%</td><td>-10%</td><td>-29%</td><td>19%</td><td>-27%</td><td>-19%</td><td>52%</td><td>-32%</td><td>33%</td><td>106%</td><td>-9%</td><td>-5%</td></tr><tr><td>Import (MoM, %)</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>HBM production related datapoints</td><td>7%</td><td>46%</td><td>10%</td><td>-9%</td><td>2%</td><td>-9%</td><td>-10%</td><td>19%</td><td>-39%</td><td>5%</td><td>-17%</td><td>110%</td><td></td></tr><tr><td>Epoxide resins import (JP to Hynix)</td><td>34%</td><td>49%</td><td>-2%</td><td>-11%</td><td>-16%</td><td>-1%</td><td>-14%</td><td>28%</td><td>-26%</td><td>-1%</td><td>-50%</td><td>167%</td><td></td></tr><tr><td>Plastic film import (JP to SEC)</td><td>-36%</td><td>34%</td><td>56%</td><td>-5%</td><td>42%</td><td>-21%</td><td>-3%</td><td>5%</td><td>-63%</td><td>24%</td><td>76%</td><td>65%</td><td></td></tr><tr><td>WFE Equipment</td><td>-10%</td><td>38%</td><td>-29%</td><td>-22%</td><td>140%</td><td>-40%</td><td>20%</td><td>27%</td><td>9%</td><td>15%</td><td>8%</td><td>-16%</td><td>3%</td></tr><tr><td>Export (YoY, %)</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Total semiconductor</td><td>21%</td><td>12%</td><td>32%</td><td>27%</td><td>22%</td><td>25%</td><td>39%</td><td>43%</td><td>103%</td><td>161%</td><td>151%</td><td>173%</td><td>169%</td></tr><tr><td>Total memory</td><td>32%</td><td>18%</td><td>39%</td><td>44%</td><td>35%</td><td>48%</td><td>60%</td><td>64%</td><td>154%</td><td>262%</td><td>220%</td><td>278%</td><td>255%</td></tr><tr><td>DRAM</td><td>36%</td><td>23%</td><td>44%</td><td>49%</td><td>38%</td><td>57%</td><td>86%</td><td>72%</td><td>167%</td><td>322%</td><td>265%</td><td>343%</td><td>370%</td></tr><tr><td>Flash memory</td><td>-18%</td><td>-8%</td><td>-13%</td><td>66%</td><td>13%</td><td>53%</td><td>130%</td><td>108%</td><td>366%</td><td>378%</td><td>383%</td><td>289%</td><td>207%</td></tr><tr><td>MCP</td><td>48%</td><td>25%</td><td>41%</td><td>38%</td><td>37%</td><td>36%</td><td>30%</td><td>42%</td><td>118%</td><td>195%</td><td>134%</td><td>187%</td><td>140%</td></tr><tr><td>SSD*</td><td>7%</td><td>18%</td><td>-22%</td><td>-17%</td><td>-14%</td><td>16%</td><td>5%</td><td>43%</td><td>114%</td><td>289%</td><td>219%</td><td>715%</td><td>338%</td></tr><tr><td>Total display</td><td>-18%</td><td>-36%</td><td>-9%</td><td>-9%</td><td>1%</td><td>-9%</td><td>-3%</td><td>1%</td><td>26%</td><td>-4%</td><td>-2%</td><td>-3%</td><td>9%</td></tr><tr><td>OLED</td><td>-14%</td><td>-39%</td><td>-10%</td><td>-5%</td><td>4%</td><td>-2%</td><td>6%</td><td>2%</td><td>33%</td><td>0%</td><td>-10%</td><td>-5%</td><td>3%</td></tr><tr><td>LCD</td><td>-27%</td><td>-25%</td><td>-7%</td><td>-24%</td><td>-12%</td><td>-31%</td><td>-28%</td><td>-3%</td><td>10%</td><td>-14%</td><td>29%</td><td>2%</td><td>30%</td></tr><tr><td>Total battery</td><td>-17%</td><td>-18%</td><td>-20%</td><td>-31%</td><td>-8%</td><td>-13%</td><td>4%</td><td>-12%</td><td>5%</td><td>-6%</td><td>36%</td><td>-7%</td><td>31%</td></tr><tr><td>Li-ion battery</td><td>-32%</td><td>-33%</td><td>-31%</td><td>-41%</td><td>-22%</td><td>-17%</td><td>6%</td><td>-21%</td><td>-2%</td><td>0%</td><td>60%</td><td>-10%</td><td>53%</td></tr><tr><td>MLCC</td><td>5%</td><td>11%</td><td>12%</td><td>17%</td><td>25%</td><td>15%</td><td>10%</td><td>11%</td><td>16%</td><td>0%</td><td>14%</td><td>-4%</td><td>14%</td></tr><tr><td>WFE Equipment</td><td>-27%</td><td>-9%</td><td>14%</td><td>10%</td><td>-20%</td><td>-17%</td><td>-48%</td><td>-27%</td><td>-17%</td><td>-9%</td><td>26%</td><td>57%</td><td>66%</td></tr><tr><td>Import (YoY, %)</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>HBM production related datapoints</td><td>35%</td><td>42%</td><td>35%</td><td>51%</td><td>12%</td><td>-5%</td><td>-2%</td><td>13%</td><td>81%</td><td>95%</td><td>-37%</td><td>72%</td><td></td></tr><tr><td>Epoxide resins import (JP to Hynix)</td><td>84%</td><td>101%</td><td>54%</td><td>75%</td><td>49%</td><td>41%</td><td>13%</td><td>14%</td><td>80%</td><td>424%</td><td>-67%</td><td>57%</td><td></td></tr><tr><td>Plastic film import (JP to SEC)</td><td>-29%</td><td>-33%</td><td>4%</td><td>15%</td><td>-15%</td><td>-38%</td><td>-18%</td><td>11%</td><td>87%</td><td>-30%</td><td>123%</td><td>96%</td><td></td></tr><tr><td>WFE Equipment</td><td>32%</td><td>35%</td><td>41%</td><td>25%</td><td>21%</td><td>4%</td><td>-14%</td><td>-10%</td><td>81%</td><td>62%</td><td>-4%</td><td>73%</td><td>99%</td></tr></table>

SSD is included in computer (not memory) based on MTI standard.   
Source: MOTIE, TRASS, Compiled by GS Global Investment Research.

# Price Target Risks and Methodology - Samsung Electronics

Valuation methodology: Our 12m 2026-2027E EV/EBITDA-based SOTP target price for the common share is W480,000. Our 12-month target price for the preference share is W360,000, which is based on our target pref to common shares discount of 25%, derived from averaging: 1) the pref discount of the 2-factor model and 2) the average preference share discount to common shares during the past 1 month. We are Buy rated on both the common and preference shares.

Key downside risks: 1) major deterioration in memory supply/demand, 2) sharp contraction in smartphone margins, and 3) mobile OLED market share loss.

# Pri

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
