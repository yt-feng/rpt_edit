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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Semiconductors | North America

# Weekly: NVDA memory cuts? And Apr SIA

Potential reduction in Vera Rubin rack content is another indication of the intensity of the memory shortage; separately, we are raising our industry estimates post a strong April SIA report Friday.

NVDA DRAM cuts reflect tight supply conditions. There were reports this week from Semi Analysis that suggested NVIDIA was reducing LPDDR5 memory content from the Vera Rubin racks from 55 TB to 28 TB, reducing the SOCAMM memory module size from 192 GB to 96 GB.

While we are not sure that it will impact every rack, we were able to confirm that there have been some changes and that it least some racks will be shipped with this lower configuration. Given the importance of memory we suspect that the higher configurations will be available, if not immediately, then shortly after shipments begin in F3q.

The rack memory is a significant portion of overall global demand for DRAM; assuming that 53-70k racks are built next year, at 55 TB, the rack SOCAMM would approach 5% of global demand, so cutting that in half across the board - the most draconian figure - would be 2%+ impact (1.4 mm TB reduction for a 62mm TB market), but one which impacts a higher value portion of the market.

That said, all of our contacts would indicate that NVIDIA, and for that matter everyone in cloud, will buy every GB of SOCAMM that they can get, and our assumption would be that if they can catch up then they would return to higher configurations. This is entirely to ensure that the DRAM shortage has minimized impact to GPU rack sales, and is actually evidence that there is a true shortage not a double ordering window - and that incremental supply will be met wit incremental demand.

Overall SIA data was stronger than expected for April, driven by both broad markets and memory. April Semiconductor Industry Association billings data reported on Friday, June 5th, came in higher than our estimates and seasonality for broad markets and memory:

- Overall: Sales were down 2.2% m/m, above our estimate of -12.1% and above the 10-yr average change of -10.6%. 3-month y/y growth accelerated to 93.9% from 79.1%, and one month y/y growth was 106.4%.   
- Trend by geography (y/y): The Americas (+158.5%) was followed by Asia Pacific (+113.0%), China (+76.7%), Europe (+64.1%), and Japan (+25.7%).

Broad markets accelerated, following a broadly strong March:

MS & CO. LLC

# Joseph Moore

Equity Analyst

Joseph.Moore@morganstanley.com +1 212 761-7516

# Ella Tulchinsky

Research Associate

Ella.Tulchinsky@morganstanley.com +1 212 761-2222

# Nicole Kozhukhov

Research Associate

Nicole.Kozhukhov@morganstanley.com +1 212 761-1636

# Mason Wayne

Research Associate

Mason.Wayne@morganstanley.com +1 212 761-6012

# Shane Brett

Equity Analyst

Shane.Brett@morganstanley.com +1 212 761-1022

2026 EXTEL

ALL-AMERICA RESEARCH POLL

May 26 – June, 12 2026

VIEW OUR ANALYSTS >

# SEMICONDUCTORS

North America

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

- Discrete (beat): -3.4% m/m vs our estimate of -8.0% and the 10-yr average change of -9.7%. Units were above the 10-yr average (0.2% vs -7.2%) while ASP was below (-3.6% vs -2.6%).   
- Analog (beat): -2.7% m/m vs our estimate of -6.0% and 10-yr average of -9.1%. Units were above the 10-yr average (-7.1% vs -8.9%) and ASP was above (4.4% vs -3.5%).   
- MCU (beat): -3.1% m/m vs our estimate of -9.0% and 10-yr average change of -12.2%. Units were above the 10-yr average (-7.1% vs -8.9%) and ASP was above (4.4% vs -3.5%).   
- MPU (beat): -0.2% m/m vs our estimate of -2.5% and 10-yr average change of -6.3%.

April built on an accelerating March, continuing to align with positive JunQ guides from suppliers. From the commentary we have heard intra-quarter, the cycle continues to improve, with Industrial in particular re-accelerating from cyclical lows and broadening out to non-AI-related areas. And while we have seen pricing increases across the supply chain, we'd note that the largest driver is cost pass-through versus value recapture, ex a few companies such as ADI. AI continues to outpace, and while we still are hearing there is no replenishment cycle, visibility into a 2H acceleration looks stronger.

In analog, the 3-month average y/y growth accelerated from 21.9% to 22.4%, led by Application Specific. MCUs' 3-month average y/y growth decelerated to 13.2% from 16.9% in March, with growth decelerating in both General Purpose and Application Specific, though the latter at a slower rate.

Exhibit 1: Global Semiconductor Sales   
![](images/4391b201e770fb056dabce6460c55eeed3ff2c8c8d99640e39810488d5cbd287.jpg)

<details>
<summary>bar_line</summary>

| Date   | Sales (Thous, LHS) | T3M Y/Y Growth (RHS) |
|--------|--------------------|----------------------|
| Apr-16 | ~45,000            | ~45%                 |
| Apr-18 | ~65,000            | ~65%                 |
| Apr-20 | ~40,000            | ~40%                 |
| Apr-22 | ~70,000            | ~70%                 |
| Apr-24 | ~30,000            | ~30%                 |
| Apr-26 | ~120,000           | ~120%                |
</details>

Source: SIA, MS

Exhibit 2: Semiconductor Sales by Region   
![](images/4eb656473cf3f6fd04fbbd76feac30fd42a41bb37951d1900bcec1a1aefe9575.jpg)

<details>
<summary>line</summary>

| Date   | Americas | Europe | Japan | China | Asia Pacific |
|--------|----------|--------|-------|-------|--------------|
| Apr-21 | ~30%     | ~40%   | ~20%  | ~20%  | ~30%         |
|        |          |        |       |       |              |
</details>

Source: SIA, MS

Memory was strong in April, with both NAND and DRAM outperforming seasonality and our estimates:

\- DRAM: Above expectation and 5-yr average, coming in at -3.7% m/m vs our estimate of -24.2% m/m and 5-yr average of -27.6%. Bits were above our estimate (-16.5% vs -31.7%) m/m, up 52.8% y/y), while ASP was above (15.3% vs 10.0%). On a 3-month y/y basis, total DRAM sales reached 298.5% in April, marking a new historical high since 2001, while ASP growth (188.1%) has now increased for nine consecutive quarters.

\- NAND: Above expectation and the 5-yr average, coming in at -4.2% m/m vs our estimate of -11.2% and 5-yr average of -13.9%. Bits were above our estimate (-20.9% m/m vs -22.8%) again likely reflecting constraints, while ASPs were above (up 21.0% m/m vs 15.0%- prices were up 281.6% y/y). On a 3-month average y/y basis, revenue reached 307.0% in April, also marking a new record in our dataset's history, while ASP growth of 213.4% also marked a new record and volume decelerated slightly to 30.7% from 36.8% in March.

The April data reinforces our view that there is no quick fix to the memory shortage, with DRAM increasingly the principal bottleneck to the AI buildout and NAND also very tight as hyperscalers continue to absorb higher-performance supply. We think the strength is still primarily supply/demand driven rather than an inventory-led cycle, with HBM wafer intensity, cleanroom/EUV constraints, and limited incremental NAND capacity all supporting a higher-for-longer pricing environment. While investors remain focused on the durability debate, we would view LTAs as a symptom of tight supply and hyperscaler urgency to secure capacity, rather than the cause of the cycle. We continue to view memory supply as a critical constraint on AI, which should support unusually strong DRAM pricing, a more durable NAND recovery, and continued ownership of that exposure through MU and SNDK.

Changes to our forecast: Our forecast comes up from +91% to +103% for this year, reflecting strength across the board but mainly memory, where our CY26 forecast increases from \$807bn to \$880bn, as 3q pricing is starting to look higher than our previous forecast. For CY27, we are assuming 22% growth y/y to \$1.96 trillion, mostly due to memory pricing rippling through.

Our take: April SIA adds another datapoint that this is less of a narrow AI cycle and increasingly a broader supply-constrained upcycle. Memory remains the most obvious expression of that, with DRAM now a principal bottleneck to the AI buildout and NAND also tightening as hyperscalers absorb higher-performance supply. We would continue to own that exposure through MU and SNDK, particularly given the lack of a quick supply response and the increasing evidence that pricing strength can last longer than investors had expected. At the same time, the better-than-seasonal broad-market data reinforces what suppliers have been saying intra-quarter: Industrial is re-accelerating from cyclical lows, demand is broadening into non-AI areas, and inventory digestion is moving further into the rear-view. That combination keeps us constructive on leading-edge logic beneficiaries including NVDA, AVGO, and ALAB, cap equipment / supply-chain beneficiaries including LRCX, KLAC, and MKSI, and broader analog / MCU suppliers such as ADI, NXP, and ALGM as the broad-market cycle accelerates.

# SIA Note Charts

Exhibit 3: April 2026 Semiconductor Sales by Product (Y/Y)   
April 2026 Semiconductor Sales by Product (Y/Y)   
![](images/e77bbbd4ec2031fba3beda313c43ee206d500feb91d78d6c99a2c3f3de7a79d3.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
| :--- | :--- |
| Discrete | 10.5 |
| Analog | 17.2 |
| MCU | 16.4 |
| MPU | 32.0 |
| Total Logic | 43.0 |
| DRAM | 375.3 |
| NAND | 366.0 |
| Total ICs | 122.1 |
| Total | 106.4 |
</details>

Source: SIA, MS

Exhibit 4: Variance Table 

<table><tr><td>Reported Item ($ mn)</td><td>April 2026 Actual</td><td>April 2026 Est.</td><td>Difference (Act-Est)</td><td>Last Mth</td><td>MoM</td><td>Last Yr</td><td>YoY</td><td>Last Mth (Before Revision)</td><td>Last Mth Revised vs. Reported</td></tr><tr><td>Discrete / Opto / Sensors Sales</td><td>8,521</td><td>8,117</td><td>5.0%</td><td>8,823</td><td>-3.4%</td><td>7,714</td><td>10.5%</td><td>8,823</td><td></td></tr><tr><td>Analog Sales</td><td>7,917</td><td>7,650</td><td>3.5%</td><td>8,138</td><td>-2.7%</td><td>6,757</td><td>17.2%</td><td>8,138</td><td></td></tr><tr><td>MCU Sales</td><td>2,049</td><td>1,924</td><td>6.5%</td><td>2,114</td><td>-3.1%</td><td>1,760</td><td>16.4%</td><td>2,114</td><td>0</td></tr><tr><td>MPU Sales</td><td>5,745</td><td>5,614</td><td>2.3%</td><td>5,758</td><td>-0.2%</td><td>4,352</td><td>32.0%</td><td>5,758</td><td>0</td></tr><tr><td>Total Micro Sales</td><td>8,017</td><td>7,754</td><td>3.4%</td><td>8,088</td><td>-0.9%</td><td>6,361</td><td>26.0%</td><td>8,088</td><td>0</td></tr><tr><td>Total Logic (ex Micro) Sales</td><td>32,569</td><td>31,417</td><td>3.7%</td><td>32,388</td><td>0.6%</td><td>22,026</td><td>47.9%</td><td>32,388</td><td></td></tr><tr><td>Total Logic Sales</td><td>40,586</td><td>39,171</td><td>3.6%</td><td>40,476</td><td>0.3%</td><td>28,387</td><td>43.0%</td><td>40,476</td><td></td></tr><tr><td>DRAM Sales</td><td>37,566</td><td>29,573</td><td>27.0%</td><td>39,028</td><td>-3.7%</td><td>7,904</td><td>375.3%</td><td>39,028</td><td>0</td></tr><tr><td>DRAM Gigabit Equivalents</td><td>28,417,085</td><td>23,447,461</td><td>21.2%</td><td>34,037,628</td><td>-16.5%</td><td>18,598,712</td><td>52.8%</td><td>34,037,628</td><td>0</td></tr><tr><td>DRAM Price per Gb Equivalent</td><td>$1.3220</td><td>$1.2613</td><td>4.8%</td><td>$1.1466</td><td>15.3%</td><td>$0.4250</td><td>211.1%</td><td>$1.1466</td><td>$0.0000</td></tr><tr><td>NAND Sales</td><td>18,349</td><td>17,016</td><td>7.8%</td><td>19,160</td><td>-4.2%</td><td>3,937</td><td>366.0%</td><td>19,160</td><td></td></tr><tr><td>NAND 1 Gigabit Equivalent</td><td>613,243,576</td><td>598,396,859</td><td>2.5%</td><td>774,855,320</td><td>-20.9%</td><td>502,098,632</td><td>22.1%</td><td>774,855,320</td><td></td></tr><tr><td>NAND Price per Gb Equivalent</td><td>$0.0299</td><td>$0.0284</td><td>5.2%</td><td>$0.0247</td><td>21.0%</td><td>$0.0078</td><td>281.6%</td><td>$0.0247</td><td></td></tr><tr><td>Total Memory Sales</td><td>56,654</td><td>47,174</td><td>20.1%</td><td>58,772</td><td>-3.6%</td><td>12,208</td><td>364.1%</td><td>58,772</td><td>0</td></tr><tr><td>Total ICs</td><td>105,156</td><td>93,994</td><td>11.9%</td><td>107,386</td><td>-2.1%</td><td>47,351</td><td>122.1%</td><td>107,386</td><td>0</td></tr><tr><td>Semiconductor Sales</td><td>113,677</td><td>102,112</td><td>11.3%</td><td>116,210</td><td>-2.2%</td><td>55,066</td><td>106.4%</td><td>116,210</td><td>0</td></tr></table>

Source: SIA, MS

Exhibit 5: Quarterly SIA Data 

<table><tr><td></td><td>Mar/24A</td><td>Jun/24A</td><td>Sep/24A</td><td>Dec/24A</td><td>Mar/25A</td><td>Jun/25A</td><td>Sep/25A</td><td>Dec/25A</td><td>Mar/26A</td><td>Jun/26E</td><td>Sep/26E</td><td>Dec/26E</td></tr><tr><td colspan="13">Revenues ($ Millions)</td></tr><tr><td>Discretes / Optos / Sensors</td><td>22,185</td><td>21,383</td><td>24,285</td><td>23,191</td><td>21,519</td><td>22,629</td><td>25,449</td><td>24,905</td><td>23,996</td><td>26,151</td><td>28,532</td><td>28,388</td></tr><tr><td>Analog</td><td>19,276</td><td>19,011</td><td>20,648</td><td>20,653</td><td>19,813</td><td>20,186</td><td>23,052</td><td>23,396</td><td>22,756</td><td>24,209</td><td>26,095</td><td>26,468</td></tr><tr><td>MCU</td><td>5,751</td><td>5,409</td><td>5,512</td><td>5,087</td><td>4,950</td><td>5,326</td><td>5,694</td><td>5,628</td><td>5,788</td><td>6,466</td><td>6,735</td><td>6,722</td></tr><tr><td>MPU</td><td>12,124</td><td>13,276</td><td>13,911</td><td>14,860</td><td>13,606</td><td>13,943</td><td>15,894</td><td>17,615</td><td>16,548</td><td>18,078</td><td>19,410</td><td>20,579</td></tr><tr><td>Other</td><td>651</td><td>658</td><td>690</td><td>703</td><td>728</td><td>752</td><td>813</td><td>768</td><td>565</td><td>669</td><td>100</td><td>100</td></tr><tr><td>Total Micro</td><td>18,526</td><td>19,343</td><td>20,114</td><td>20,650</td><td>19,284</td><td>20,021</td><td>22,401</td><td>24,011</td><td>22,902</td><td>25,213</td><td>26,245</td><td>27,400</td></tr><tr><td>Logic (ex Micro)</td><td>48,462</td><td>49,479</td><td>56,194</td><td>61,634</td><td>65,356</td><td>68,892</td><td>78,853</td><td>88,783</td><td>91,117</td><td>101,338</td><td>109,583</td><td>117,024</td></tr><tr><td>Total Logic</td><td>66,988</td><td>68,822</td><td>76,307</td><td>82,283</td><td>84,640</td><td>88,913</td><td>101,254</td><td>112,794</td><td>114,019</td><td>126,550</td><td>135,828</td><td>144,424</td></tr><tr><td>DRAM</td><td>18,175</td><td>22,269</td><td>26,173</td><td>28,243</td><td>27,074</td><td>31,635</td><td>39,949</td><td>51,939</td><td>93,436</td><td>147,692</td><td>163,222</td><td>177,551</td></tr><tr><td>NAND</td><td>13,472</td><td>17,813</td><td>18,003</td><td>17,140</td><td>12,617</td><td>15,404</td><td>17,382</td><td>22,282</td><td>42,794</td><td>76,274</td><td>84,702</td><td>89,738</td></tr><tr><td>Other</td><td>1,039</td><td>1,010</td><td>1,133</td><td>1,048</td><td>1,070</td><td>1,154</td><td>1,310</td><td>1,329</td><td>1,544</td><td>2,214</td><td>2,214</td><td>2,214</td></tr><tr><td>Total Memory</td><td>32,685</td><td>41,092</td><td>45,308</td><td>46,431</td><td>40,761</td><td>48,193</td><td>58,641</td><td>76,550</td><td>137,775</td><td>226,179</td><td>250,138</td><td>269,503</td></tr><tr><td>Total ICs</td><td>118,949</td><td>128,925</td><td>142,263</td><td>149,367</td><td>145,214</td><td>157,293</td><td>182,946</td><td>211,740</td><td>274,550</td><td>376,939</td><td>412,061</td><td>440,396</td></tr><tr><td>Total Semiconductor</td><td>141,134</td><td>150,308</td><td>166,547</td><td>172,558</td><td>166,732</td><td>179,921</td><td>208,395</td><td>236,645</td><td>298,546</td><td>403,090</td><td>440,593</td><td>468,783</td></tr><tr><td>Q/Q Change</td><td>-3.3%</td><td>6.5%</td><td>10.8%</td><td>3.6%</td><td>-3.4%</td><td>7.9%</td><td>15.8%</td><td>13.6%</td><td>26.2%</td><td>35.0%</td><td>9.3%</td><td>6.4%</td></tr><tr><td>Y/Y Change</td><td>18.1%</td><td>18.6%</td><td>23.7%</td><td>18.2%</td><td>18.1%</td><td>19.7%</td><td>25.1%</td><td>37.1%</td><td>79.1%</td><td>124.0%</td><td>111.4%</td><td>98.1%</td></tr></table>

Source: SIA, MS

Exhibit 6: Annual SIA Data 

<table><tr><td></td><td>2010A</td><td>2017A</td><td>2018A</td><td>2019A</td><td>2020A</td><td>2021A</td><td>2022A</td><td>2023A</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td colspan="13">Revenues ($ Millions)</td></tr><tr><td>Discretes / Optos / Sensors</td><td>48,406</td><td>69,087</td><td>75,446</td><td>78,953</td><td>79,164</td><td>92,945</td><td>99,591</td><td>98,359</td><td>91,044</td><td>94,502</td><td>107,066</td><td>114,712</td></tr><tr><td>Analog</td><td>42,285</td><td>53,069</td><td>58,380</td><td>53,939</td><td>55,658</td><td>73,816</td><td>88,919</td><td>81,146</td><td>79,588</td><td>86,447</td><td>99,529</td><td>108,504</td></tr><tr><td>MCU</td><td>14,799</td><td>16,430</td><td>17,027</td><td>15,808</td><td>15,484</td><td>19,622</td><td>25,030</td><td>27,861</td><td>21,758</td><td>21,597</td><td>25,711</td><td>28,489</td></tr><tr><td>MPU</td><td>39,927</td><td>44,370</td><td>46,371</td><td>47,974</td><td>51,812</td><td>56,766</td><td>51,299</td><td>45,480</td><td>54,172</td><td>61,059</td><td>74,614</td><td>83,018</td></tr><tr><td>Other</td><td>5,908</td><td>3,286</td><td>3,262</td><td>2,658</td><td>2,382</td><td>2,845</td><td>3,217</td><td>3,172</td><td>2,702</td><td>3,062</td><td>1,434</td><td>400</td></tr><tr><td>Total Micro</td><td>60,633</td><td>64,086</td><td>66,660</td><td>66,440</td><td>69,678</td><td>79,234</td><td>79,546</td><td>76,513</td><td>78,633</td><td>85,718</td><td>101,760</td><td>111,907</td></tr><tr><td>Logic (ex Micro)</td><td>77,377</td><td>102,196</td><td>109,411</td><td>106,535</td><td>118,408</td><td>153,710</td><td>176,097</td><td>178,493</td><td>215,768</td><td>301,883</td><td>419,062</td><td>500,028</td></tr><tr><td>Total Logic</td><td>138,010</td><td>166,281</td><td>176,071</td><td>172,975</td><td>188,086</td><td>232,944</td><td>255,643</td><td>255,006</td><td>294,401</td><td>387,601</td><td>520,822</td><td>611,935</td></tr><tr><td>DRAM</td><td>39,210</td><td>72,802</td><td>98,604</td><td>62,475</td><td>64,324</td><td>92,960</td><td>77,769</td><td>51,945</td><td>94,860</td><td>150,598<

[中间内容因长度限制已省略]

roducts or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.   
INDUSTRY COVERAGE: Semiconductors 

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/05/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$466.38</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$23.01</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$46.39</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$63.52</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$64.95</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$401.39</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$317.06</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$385.73</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$75.53</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$99.17</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$56.78</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$263.47</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$88.34</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$864.01</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$25.08</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$205.10</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$295.96</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>E (05/11/2025)</td><td>$117.26</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$98.28</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>U (02/10/2026)</td><td>$215.94</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,559.32</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$151.02</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$218.11</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$73.57</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$285.06</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$55.06</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$342.93</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$376.19</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$464.85</td></tr></table>

© 2026 MS
"""
