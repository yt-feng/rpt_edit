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
July 6, 2026 04:01 AM GMT

Semiconductors | North America

# Weekly: Meta GPU context; May SIA

We think that gpu compute remains in shortage, and recent events are more about stronger cloud demand vs. any excess compute capacity. Separately, May SIA #s were slightly below our forecast.

Last week, Bloomberg reported that Meta - covered by Brian Nowak & team - would develop a cloud services unit, competing with Azure, AWS, and others; the company has not finalized details about this offering. Our understanding is that this was at least part of the weakness in the stocks last week, in addition to a broader derisking.

To us, this points to excess demand for GPUs, more so than excess supply from any one hyperscaler: This is not the first report that we have heard of larger internally focused hyperscalers offering GPUs to others, and is something that we are hearing regularly. We would not jump to the negative conclusion that the market seems to be focused on - that these vendors have excess compute. An alternate explanation fits our checks more clearly - that there is a substantial shortage of GPU compute in the market right now, such that the most profitable use of GPUs might be to rent them to others. There is excess demand, more so than excess supply, at least on an industry-wide basis, and the highest utility use of a GPU might be to rent it to someone else.

While clearly some are doing better than others, we expect to hear about very strong cloud compute demand through earnings, across the board, and see this strong cloud backdrop as at least part of the story here.

Meta aside, this larger trend towards subletting GPUs - which we have seen in multiple places - should be a significant positive for NVIDIA market share, in our opinion. If there is a mismatch of compute - whether lower demand internally or higher demand externally - that demand is better served with the chip that is the defacto standard in the industry. ASIC capacity is much harder to sublet, especially for lower volume ASICs. AMD has more ubiquity than ASICs, which is helpful, but lower market share overall would point to a smaller secondary compute market.

NVIDIA made an important point at Computex, where they talked about NVDA offering by far the highest tokens per gigawatt by a large margin - but also offering better economics through faster bring up, longer mean time between failure, and longer asset life as driving better NVDA economics vs. competing solutions. We would certainly add ubiquity of compute as another key advantage.

Specifically at Meta, we do not perceive disruption, though their capex isn't the upside driver that we have seen in the past. At the moment, we are seeing upside in GPU demand from many places, and somewhat in contrast to prior years Meta

MS & CO. LLC

Joseph Moore
Equity Analyst
Joseph.Moore@morganstanley.com +1 212 761-7516

Nicole Kozhukhov
Research Associate
Nicole.Kozhukhov@morganstanley.com +1 212 761-1636

Research Associate
Ella.Tulchinsky@morganstanley.com +1 212 761-2222

Mason Wayne
Research Associate
Mason.Wayne@morganstanley.com +1 212 761-6012

Shane Brett
Equity Analyst
Shane.Brett@morganstanley.com +1 212 761-1022

## SEMICONDUCTORS

North America
Industry View
Attractive

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

isn't as notable an upside driver to GPU trends. We would not be alarmist about this, it's not a deceleration, as in each of the last few years leadership has transitioned from one customer to another.

We do expect Meta to be the early adopter of AMD Helios, though that doesn't seem to have impacted purchasing from NVIDIA that we can tell. The economics of the warrant structure is even more important given the appreciation in the share price of AMD; the warrants are effectively a 75% discount for at least the initial gigawatt, which is a substantial incentive for someone that has been AMD's biggest customer over the life of the MI300/350 families.

Overall SIA data was softer than expected for May, driven by both broad markets and memory. May Semiconductor Industry Association billings data reported on Saturday, July 4th, came in lower than our estimates and seasonality for broad markets and memory:

\- Overall: Sales were up 16.1% m/m, below our estimate of 22.0% though above the 10-yr average change of 6.9%. 3-month y/y growth accelerated to 104.2% from 93.9% in April, and one month y/y growth was 118.8%.

\- Trend by geography (y/y): The Americas (+150.7%) was followed by Asia Pacific (+126.3%), China (+101.9%), Europe (+83.7%), and Japan (+39.4%).

Broad markets decelerated following a strong April:

\- Discrete (miss): -6.9% m/m vs our estimate of -1.0% and the 10-yr average change of -0.9%. Units were below the 10-yr average (-4.1% vs -1.3%) and ASP was below (-2.9% vs -0.4%).

\- Analog (miss): -7.8% m/m vs our estimate of -2.0% and 10-yr average of -1.7%. Units were below the 10-yr average (-4.0% vs 1.5%) and ASP was below (-4.0% vs -3.0%).

\- MCU (in-line): -2.7% m/m vs our estimate of -2.0% and 10-yr average change of -2.1%. Units were above the 10-yr average (1.8% vs -0.8) and ASP was above (-4.4% vs -1.1%).

\- MPU (beat): 5.0% m/m vs our estimate of 3.2% and 10-yr average change of 1.8%.

May was softer than expected after a strong April, with both broad markets and memory coming in below our estimates. Even so, the broader cycle still appears to be improving and remains generally consistent with constructive JunQ supplier commentary. From our checks intra-quarter, Industrial continues to recover from cyclical lows and demand is broadening beyond AI-linked areas into more traditional end markets. On pricing, increases are still showing up across the supply chain, though the primary driver remains cost pass-through for the broader supply chain. AI remains the clear area of outperformance, and while we still do not see evidence of a true replenishment cycle, visibility into a stronger 2H continues to improve.

In analog, the 3-month average y/y growth held flat at 14.2%, led by General Purpose. MCUs' 3-month average y/y growth accelerated to 15.5% from 13.2% in April, led by General Purpose.

Exhibit 1: Global Semiconductor Sales  
![](images/b2da6a162d10d7b272549d0d12643f576b0c75f06982e7290d322f94b36efb9e.jpg)  
Source: SIA, MS

Exhibit 2: Semiconductor Sales by Region  
![](images/9800cbd3e19a82a8b6610e19026aeccf2e62d145b109055c37912cdb2a06f3cb.jpg)  
Source: SIA, MS

Memory was softer in May, likely reflecting supply constraints, with both NAND and DRAM underperforming our estimates while NAND was above seasonality:

\- DRAM: Below expectation and 5-yr average, coming in at 27.7% m/m vs our estimate of 43.0% m/m and 5-yr average of 45.9%. Bits were below our estimate (13.2% vs 30.0%) m/m, up 16.1% y/y), while ASP was above (12.9% vs 10.0%). On a 3-month y/y basis, total DRAM sales reached 304.8% in May, marking another new historical high since 2001, while ASP growth (218.3%) has now increased for ten consecutive quarters.

\- NAND: Slightly below expectation though above the 5-yr average, coming in at 40.7% m/m vs our estimate of 43.8% and 5-yr average of 25.6%. Bits were below our estimate (19.5% m/m vs 22.0%), while ASPs were in-line (up 17.8% m/m vs 17.9%- prices were up 281.6% y/y). On a 3-month average y/y basis, revenue reached 364.6% in May, also marking a new record in our dataset's history, while ASP growth of 277.5% also marked a new record. Volume decelerated slightly to 23.8% from 30.7% in April.

May data does not alter the core memory thesis; we have commented in the past that it is challenging to predict monthly trends when the drivers shifts from seasonal drivers to more linear supply drivers. What stands out now is not just constrained supply, but growing evidence that customers are trying to lock in access before the market loosens, reinforcing our view that this is a structurally constrained AI-led cycle rather than a conventional inventory recovery. DRAM remains the clearest bottleneck, while NAND is increasingly benefiting from tighter mix and better discipline than investors typically assume. Said differently, the key takeaway is no longer just that memory is tight, but that the industry is beginning to formalize that tightness in ways that could extend the earnings window. We continue to see memory as a key constraint on AI buildouts, supporting elevated DRAM pricing, a more durable NAND recovery, and continued preference for MU and SNDK.

Changes to our forecast: Our forecast comes down slightly from up 103% to up 99% for the year, mostly the moderation in memory volumes. Our CY26 memory forecast at \$847bn is slightly lower than our prior forecast but still up meaningfully from \$222bn last year. For CY27, we are assuming 24% growth y/y to \$1.95 trillion, mostly due to memory pricing rippling through - largely unchanged from our prior

## forecast.

Our take: May SIA being a bit slow is surprising given the generally positive tone of business across the broader markets during 2q, but it doesn't change our view that 2q will be generally a very strong quarter. Memory remains the clearest area of tightness, with DRAM still the main bottleneck to AI deployments and NAND also holding firmer than many expected. We continue to favor that exposure through MU and SNDK, given limited near-term supply flexibility and a pricing backdrop that still looks more durable than investors had expected. Outside memory, the May data is also supportive of a more constructive broad-market view, as improving conditions are no longer limited to AI-linked demand. That keeps us constructive on NVDA, AVGO, and CBRS in leading-edge logic, LRCX, KLAC, MKSI, and ON in cap equipment/supply-chain, and ADI and NXP in premium analog/MCU.

## SIA Note Charts

Exhibit 3: May 2026 Semiconductor Sales by Product (Y/Y)  
![](images/fb3286cb3d5dca55be3e3e7234fd44126722e6a78b1e2e0a17519ca0fc9cab91.jpg)  
Source: SIA, MS

Exhibit 4: Variance Table

<table><tr><td>Reported Item ($ mn)</td><td>May 2026 Actual</td><td>May 2026 Est.</td><td>Difference (Act-Est)</td><td>Last Mth</td><td>MoM</td><td>Last Yr</td><td>YoY</td><td>Last Mth (Before Revision)</td><td>Last Mth Revised vs. Reported</td></tr><tr><td>Discrete / Opto / Sensors Sales</td><td>7,936</td><td>8,435</td><td>-5.9%</td><td>8,521</td><td>-6.9%</td><td>6,923</td><td>14.6%</td><td>8,521</td><td></td></tr><tr><td>Analog Sales</td><td>7,297</td><td>7,758</td><td>-6.0%</td><td>7,917</td><td>-7.8%</td><td>6,548</td><td>11.4%</td><td>7,917</td><td></td></tr><tr><td>MCU Sales</td><td>1,993</td><td>2,008</td><td>-0.7%</td><td>2,049</td><td>-2.7%</td><td>1,666</td><td>19.6%</td><td>2,049</td><td>0</td></tr><tr><td>MPU Sales</td><td>6,034</td><td>5,929</td><td>1.8%</td><td>5,745</td><td>5.0%</td><td>4,615</td><td>30.8%</td><td>5,745</td><td>0</td></tr><tr><td>Total Micro Sales</td><td>8,257</td><td>8,160</td><td>1.2%</td><td>8,017</td><td>3.0%</td><td>6,515</td><td>26.7%</td><td>8,017</td><td>0</td></tr><tr><td>Total Logic (ex Micro) Sales</td><td>33,853</td><td>33,546</td><td>0.9%</td><td>32,569</td><td>3.9%</td><td>22,800</td><td>48.5%</td><td>32,569</td><td></td></tr><tr><td>Total Logic Sales</td><td>42,109</td><td>41,706</td><td>1.0%</td><td>40,586</td><td>3.8%</td><td>29,314</td><td>43.6%</td><td>40,586</td><td></td></tr><tr><td>DRAM Sales</td><td>47,978</td><td>53,720</td><td>-10.7%</td><td>37,566</td><td>27.7%</td><td>11,730</td><td>309.0%</td><td>37,566</td><td>0</td></tr><tr><td>DRAM Gigabit Equivalents</td><td>32,158,182</td><td>36,942,211</td><td>-13.0%</td><td>28,417,085</td><td>13.2%</td><td>27,705,526</td><td>16.1%</td><td>28,417,085</td><td>0</td></tr><tr><td>DRAM Price per Gb Equivalent</td><td>$1.4919</td><td>$1.4542</td><td>2.6%</td><td>$1.3220</td><td>12.9%</td><td>$0.4234</td><td>252.4%</td><td>$1.3220</td><td>$0.0000</td></tr><tr><td>NAND Sales</td><td>25,811</td><td>26,377</td><td>-2.1%</td><td>18,349</td><td>40.7%</td><td>5,410</td><td>377.1%</td><td>18,349</td><td></td></tr><tr><td>NAND 1 Gigabit Equivalent</td><td>732,553,576</td><td>747,996,074</td><td>-2.1%</td><td>613,243,576</td><td>19.5%</td><td>662,338,864</td><td>10.6%</td><td>613,243,576</td><td></td></tr><tr><td>NAND Price per Gb Equivalent</td><td>$0.0352</td><td>$0.0353</td><td>-0.1%</td><td>$0.0299</td><td>17.8%</td><td>$0.0082</td><td>331.4%</td><td>$0.0299</td><td></td></tr><tr><td>Total Memory Sales</td><td>74,596</td><td>80,835</td><td>-7.7%</td><td>56,654</td><td>31.7%</td><td>17,522</td><td>325.7%</td><td>56,654</td><td>0</td></tr><tr><td>Total ICs</td><td>124,002</td><td>130,299</td><td>-4.8%</td><td>105,156</td><td>17.9%</td><td>53,384</td><td>132.3%</td><td>105,156</td><td>0</td></tr><tr><td>Semiconductor Sales</td><td>131,938</td><td>138,734</td><td>-4.9%</td><td>113,677</td><td>16.1%</td><td>60,307</td><td>118.8%</td><td>113,677</td><td>0</td></tr></table>

Source: SIA, MS

Exhibit 5: Quarterly SIA Data

<table><tr><td></td><td>Mar/24A</td><td>Jun/24A</td><td>Sep/24A</td><td>Dec/24A</td><td>Mar/25A</td><td>Jun/25A</td><td>Sep/25A</td><td>Dec/25A</td><td>Mar/26A</td><td>Jun/26E</td><td>Sep/26E</td><td>Dec/26E</td></tr><tr><td colspan="13">Revenues ($ Millions)</td></tr><tr><td>Discretes / Optos / Sensors</td><td>22,185</td><td>21,383</td><td>24,285</td><td>23,191</td><td>21,519</td><td>22,629</td><td>25,449</td><td>24,905</td><td>23,996</td><td>25,106</td><td>27,392</td><td>27,254</td></tr><tr><td>Analog</td><td>19,276</td><td>19,011</td><td>20,648</td><td>20,653</td><td>19,813</td><td>20,186</td><td>23,052</td><td>23,396</td><td>22,756</td><td>23,531</td><td>25,365</td><td>25,727</td></tr><tr><td>MCU</td><td>5,751</td><td>5,409</td><td>5,512</td><td>5,087</td><td>4,950</td><td>5,326</td><td>5,694</td><td>5,628</td><td>5,788</td><td>6,433</td><td>6,700</td><td>6,688</td></tr><tr><td>MPU</td><td>12,124</td><td>13,276</td><td>13,911</td><td>14,860</td><td>13,606</td><td>13,943</td><td>15,894</td><td>17,615</td><td>16,548</td><td>18,295</td><td>19,644</td><td>20,826</td></tr><tr><td>Other</td><td>651</td><td>658</td><td>690</td><td>703</td><td>728</td><td>752</td><td>813</td><td>758</td><td>565</td><td>683</td><td>100</td><td>100</td></tr><tr><td>Total Micro</td><td>18,526</td><td>19,343</td><td>20,114</td><td>20,650</td><td>19,284</td><td>20,021</td><td>22,401</td><td>24,011</td><td>22,902</td><td>25,412</td><td>26,445</td><td>27,614</td></tr><tr><td>Logic (ex Micro)</td><td>48,462</td><td>49,479</td><td>56,194</td><td>61,634</td><td>65,356</td><td>68,892</td><td>78,853</td><td>88,783</td><td>91,117</td><td>101,967</td><td>110,263</td><td>117,750</td></tr><tr><td>Total Logic</td><td>66,988</td><td>68,822</td><td>76,307</td><td>82,283</td><td>84,640</td><td>88,913</td><td>101,254</td><td>112,794</td><td>114,019</td><td>127,379</td><td>136,708</td><td>145,364</td></tr><tr><td>DRAM</td><td>18,175</td><td>22,269</td><td>26,173</td><td>28,243</td><td>27,074</td><td>31,635</td><td>39,949</td><td>51,939</td><td>93,436</td><td>135,769</td><td>155,616</td><td>177,742</td></tr><tr><td>NAND</td><td>13,472</td><td>17,813</td><td>18,003</td><td>17,140</td><td>12,617</td><td>15,404</td><td>17,382</td><td>22,282</td><td>42,794</td><td>66,484</td><td>81,979</td><td>89,151</td></tr><tr><td>Other</td><td>1,039</td><td>1,010</td><td>1,133</td><td>1,048</td><td>1,070</td><td>1,154</td><td>1,310</td><td>1,329</td><td>1,544</td><td>7,459</td><td>7,459</td><td>7,459</td></tr><tr><td>Total Memory</td><td>32,685</td><td>41,092</td><td>45,308</td><td>46,431</td><td>40,761</td><td>48,193</td><td>58,641</td><td>75,550</td><td>137,775</td><td>209,712</td><td>245,055</td><td>274,352</td></tr><tr><td>Total ICs</td><td>118,949</td><td>128,925</td><td>142,263</td><td>149,367</td><td>145,214</td><td>157,293</td><td>

[中间内容因长度限制已省略]

ly to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/02/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$517.82</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$23.98</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$55.49</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$78.36</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$69.65</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$377.16</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$406.42</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$360.45</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$204.86</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$69.84</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$120.35</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$49.12</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$245.29</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$84.64</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$975.56</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$14.46</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$194.83</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$273.36</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>++</td><td>$91.22</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$87.57</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>E (06/24/2026)</td><td>$176.25</td></tr><tr><td>Quantinuum (QNT.O)</td><td>E (06/29/2026)</td><td>$74.56</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,745.00</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$135.27</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$218.22</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$62.56</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$293.08</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$40.00</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$315.28</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$373.14</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$437.16</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
