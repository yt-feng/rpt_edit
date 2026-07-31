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
US Life Science Tools & Diagnostics Illumina Inc

Rating Market-Perform

Price Target

ILMN

215.00 USD (185.00 OLD)

![](images/1d610e3d1e0ae8cebac08c446c851016601cb0e55b823b31fb25fe2cf68994fd.jpg)

Estimate Change
Eve Burstein
+1 917 344 8313
eve.burstein@bernsteinsg.com

![](images/93843b2fe0cbac65c36d2f66494ed5b5dbbfbd3a11aeaa0d0d0ac90fb82cbfd0.jpg)

Louisa Qiu  
+1 917 344 8495  
louisa.qiu@bernsteinsg.com

Specialist Sales

![](images/c519ca8906ac9b405578ae5aac9e3d8cd7c047dd364f1ac10877cbc16f2f6e65.jpg)

Christian Moore
+1 917 344 8555
christian.moore@bernsteinsg.com

## Illumina 2Q26: Ride the (clinical) wave

Illumina reported 2Q26 numbers after market close on Thursday. Revenue of \$1,159M was 4% above consensus of \$1,110, and EPS of \$1.31 was 7% above consensus of \$1.23. The company raised FY26 revenue guidance to \$4.60B - \$4.64B (from \$4.52B - \$4.62B), ROW organic growth to 5+% (from 2% - 4%) and EPS \~13 cents at the midpoint.

NovaSeq X placements were without a doubt the standout in the quarter; the >95 placements were a nice sequential step-up from 83 in Q1. Notably, 70% of these placements went to clinical customers (although we wouldn't have expected too many placements into the research setting in this funding environment). It is easy to imagine that many of these purchases went to diagnostics players expecting to meaningfully ramp up existing tests (e.g., like Guardant ramping up Shield and Reveal). However, it is also easy to imagine that some of them went to clinical R&D - which is perhaps a sign of customers recommitting to Illumina after having had time to consider pricing and performance from the other major new entrants out there.

The clinical consumable cliff has turned into a... wave to be surfed? Previously, there was a concern that when clinical customers switched from the 6000 to the X they would quickly start to pay less per sample, but they wouldn't ramp up volumes accordingly and revenue would hit a "cliff." However, more and more of the clinical transition is now behind us: in Q2 the X was $79\%$ of high throughput Gb shipped and $59\%$ of high throughput consumables revenue). And with clinical consumable growth remaining strong ( $+15\%$ ROW, $>20\%$ in the U.S... though bears may pick at the fact that growth was $+20\%$ ROW in Q1), this risk continues to be less and less compelling. CEO Jacob Thaysen opined, "It's not a cliff. It's a wave. And we are surfing it."

## Investment Implications

We come out of this earnings print much more positive than we went in. However, the market was much more positive going in than we were (stock up 16.6% over the last month and 5.3% on the day), so it's possible we won't see too much of a reaction (down 1% in the aftermarket). We maintain our Market-Perform rating. We raise our PT to \$215 based on raising our estimates, and raising our multiples to the current 2026 levels (EV/EBITDA increase from 22x to 25x 2027, P/E increased from 34 to 40x 2027). WACC of 9.25% and a terminal growth of 3% remain unchanged. Models: Company model for ILMN

<table><tr><td>Close Date</td><td>30 Jul 2026</td></tr><tr><td>ILMN Close Price (USD)</td><td>205.09</td></tr><tr><td>Price Target (USD)</td><td>215.00</td></tr><tr><td>Upside/(Downside)</td><td>5%</td></tr><tr><td>52-Week Range</td><td>205.47/88.00</td></tr><tr><td>SPX</td><td>7,437.63</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>NA</td></tr><tr><td>Market Cap (USD) (M)</td><td>31,030</td></tr><tr><td>EV (USD) (M)</td><td>32,339</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>56.4</td><td>16.6</td><td>41.6</td><td>92.3</td></tr><tr><td>SPX (%)</td><td>8.6</td><td>(0.8)</td><td>7.2</td><td>16.9</td></tr><tr><td>Relative (%)</td><td>47.7</td><td>17.5</td><td>34.4</td><td>75.4</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

Price Performance, 1YR  
![](images/f28d7a2ec56d03fd01d43f1b8d6694668b8f7028c619ed25b15e3df26864e0c0.jpg)

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>ILMN (USD)</td><td>4.86</td><td>5.34</td><td>6.14</td><td>Revenues (M)</td><td>4,343</td><td>4,632</td><td>4,937</td><td>--</td><td>Adjusted P/E (x)</td><td>42.2</td><td>38.4</td><td>33.4</td></tr><tr><td>OLD</td><td>--</td><td>5.22</td><td>5.94</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

## DETAILS

## QUARTERLY PERFORMANCE

See below for a comparison of Illumina's 2Q results vs. consensus and Bernstein estimates (Exhibit 1), as well as results vs. 2Q guidance (Exhibit 2).

EXHIBIT 1: ILMN quarterly performance vs. consensus and Bernstein

<table><tr><td colspan="6">Current quarter: 2Q26</td><td colspan="2">YoY comparison: 2Q25</td><td colspan="2">QoQ Comparison: 1Q26</td></tr><tr><td></td><td>Actual</td><td>Consensus</td><td>Reported vs Consensus</td><td>Bernstein</td><td>Reported vs Bernstein</td><td>Actual</td><td>YoY change</td><td>Actual</td><td>QoQ change</td></tr><tr><td>Product</td><td>982</td><td>965</td><td>2%</td><td>968</td><td>1%</td><td>912</td><td>8%</td><td>917</td><td>7%</td></tr><tr><td>Consumables</td><td>852</td><td>841</td><td>1%</td><td>846</td><td>1%</td><td>811</td><td>5%</td><td>797</td><td>7%</td></tr><tr><td>Instruments</td><td>130</td><td>123</td><td>6%</td><td>123</td><td>6%</td><td>101</td><td>29%</td><td>120</td><td>8%</td></tr><tr><td>Service &amp; other</td><td>177</td><td>165</td><td>7%</td><td>162</td><td>9%</td><td>147</td><td>20%</td><td>174</td><td>2%</td></tr><tr><td>Income statement (adj)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>1,159</td><td>1,110</td><td>4%</td><td>1,131</td><td>2%</td><td>1,059</td><td>9%</td><td>1,091</td><td>6%</td></tr><tr><td>Cost of revenue</td><td>369</td><td>349</td><td>6%</td><td>363</td><td>2%</td><td>324</td><td>14%</td><td>347</td><td>6%</td></tr><tr><td>Gross profit</td><td>790</td><td>761</td><td>4%</td><td>768</td><td>3%</td><td>735</td><td>7%</td><td>744</td><td>6%</td></tr><tr><td>Gross margin</td><td>68.2%</td><td>68.6%</td><td>-0.4 pp</td><td>67.9%</td><td>0.3 pp</td><td>69.4%</td><td>-1.2 pp</td><td>68.2%</td><td>0.0 pp</td></tr><tr><td>SG&amp;A</td><td>278</td><td>270</td><td>3%</td><td>263</td><td>6%</td><td>241</td><td>15%</td><td>267</td><td>4%</td></tr><tr><td>R&amp;D</td><td>252</td><td>252</td><td>0%</td><td>253</td><td>0%</td><td>243</td><td>4%</td><td>239</td><td>5%</td></tr><tr><td>Operating income</td><td>260</td><td>251</td><td>3%</td><td>251</td><td>3%</td><td>252</td><td>3%</td><td>239</td><td>9%</td></tr><tr><td>Operating margin</td><td>22.5%</td><td>22.1%</td><td>0.4 pp</td><td>22.2%</td><td>0.3 pp</td><td>23.8%</td><td>-1.3 pp</td><td>21.9%</td><td>0.6 pp</td></tr><tr><td>Income tax</td><td>52</td><td>48</td><td>8%</td><td>49</td><td>7%</td><td>54</td><td>-4%</td><td>46</td><td>13%</td></tr><tr><td>Net income</td><td>201</td><td>189</td><td>6%</td><td>188</td><td>7%</td><td>187</td><td>7%</td><td>177</td><td>14%</td></tr><tr><td>EPS (diluted)</td><td>1.31</td><td>1.23</td><td>7%</td><td>1.22</td><td>7%</td><td>1.19</td><td>10%</td><td>1.15</td><td>14%</td></tr><tr><td>Diluted share count</td><td>153</td><td>154</td><td>0%</td><td>153</td><td>0%</td><td>157</td><td>-3%</td><td>154</td><td>-1%</td></tr></table>

Source: Company reports, Bloomberg, Bernstein analysis and estimates

EXHIBIT 2: ILMN quarterly results vs. guidance

<table><tr><td></td><td>Reported</td><td>2Q26 guidance</td></tr><tr><td>Total revenue</td><td>$1.16B</td><td>$1.12B - $1.14B</td></tr><tr><td>Reported revenue growth</td><td>9.50%</td><td>6% to 8%</td></tr><tr><td>ROW Organic Growth (Ex-China)</td><td>8.10%</td><td>4% to 6%</td></tr><tr><td>Non-GAAP operating margin</td><td>22.5%</td><td>~22%</td></tr><tr><td>Non-GAAP EPS</td><td>$1.31</td><td>$1.20 - $1.25</td></tr></table>

Source: Company reports, Bernstein analysis

## GUIDANCE

Illumina raised its guidance for FY26; the key metrics are in Exhibit 3 for FY26 and in Exhibit 4 for 3Q26, with additional notes below.

EXHIBIT 3: ILMN FY guidance

<table><tr><td>FY26 guidance as of</td><td>2Q26</td><td>1Q26</td><td>4Q25</td></tr><tr><td>Revenue</td><td>$4.60B - $4.64B</td><td>$4.52B - $4.62B</td><td>$4.50B - $4.60B</td></tr><tr><td>Reported revenue growth</td><td>Not Reiterated</td><td>4% to 6%</td><td>4% to 6%</td></tr><tr><td>ROW Organic Growth (Ex-China)</td><td>&gt;5%</td><td>2% to 4%</td><td>2% to 4%</td></tr><tr><td>Revenue from Greater China</td><td>Not Reiterated</td><td>Not Reiterated</td><td>$210M - $220M</td></tr><tr><td>Non-GAAP operating margin</td><td>23.4% - 23.6%</td><td>23.4% - 23.6%</td><td>23.3% to 23.5%</td></tr><tr><td>Sequencing instruments (CC, Ex-China)</td><td>+LSD</td><td>Flat to +LSD</td><td>-LSD to Flat</td></tr><tr><td>Sequencing consumables (CC, Ex-China)</td><td>+MSD</td><td>+LSD to +MSD</td><td>+LSD to +MSD</td></tr><tr><td>Non-GAAP tax rate</td><td>Not Reiterated</td><td>Not Reiterated</td><td>20.5%</td></tr><tr><td>Non-GAAP diluted EPS</td><td>$5.30 - $5.40</td><td>$5.15 - $5.30</td><td>$5.05 - $5.20</td></tr></table>

Source: Company reports, Bernstein analysis

## EXHIBIT 4: ILMN 3Q26 guidance

<table><tr><td></td><td>3Q26 guidance</td></tr><tr><td>Total revenue</td><td>$1.14B - $1.16B</td></tr><tr><td>Reported revenue growth</td><td>Not Guided</td></tr><tr><td>ROW Organic Growth (Ex-China)</td><td>~4.5%</td></tr><tr><td>ILMN Organic Growth</td><td>~4.5%</td></tr><tr><td>Non-GAAP operating margin</td><td>~24%</td></tr><tr><td>Non-GAAP EPS</td><td>$1.33 - $1.38</td></tr></table>

Source: Company reports, Bernstein analysis

## Additional notes on guidance

## - 2H26

\- NovaSeq X placements are expected to remain elevated in 2H26, with some moderation in YoY growth rates.

\- Consumables growth is expected to remain steady, while quarterly variability could arise from instrument placements, which are expected to remain elevated in 2H26 but were already elevated beginning in 2H25.

\- 3Q26 is expected to reflect usual seasonality, with 4Q26 remaining the company's largest quarter of the year.

\- The extra selling week in 4Q26 is expected to add approximately 50 bps to FY26 revenue growth, primarily through consumables

## - FY26 & Beyond

\- Clinical sequencing consumables growth is expected to be mid-teens, while Research & Applied consumables are expected to decline mid- to high-single digits in FY26.

\- Recent NovaSeq X placement outperformance is expected to provide a modest FY26 consumables revenue benefit, with most of the benefit coming in FY27 as clinical customers typically require at least six to nine months to reach normalized consumables pull-through.

\- Continues to target high-single-digit revenue growth in FY27, including 1 to 2 percentage points from new products.

## COMMENTARY FROM THE CALL & CALLBACK

## SEQUENCING RESULTS

\- Placed over 95 NovaSeq X instruments, supported by several multi-unit capacity expansion orders from large clinical customers, including orders related to new clinical trials. In the call back, management suggested they didn't see pull forward of instrument orders.

• Approximately 70% of NovaSeq X placements were clinical and 30% were research.

\- In the call back, management noted that most X research placements are incremental (vs. upgrades from the 6000) since the transition is largely complete. Approximately $50\%$ of clinical placements are incremental (vs. upgrades from the 6000), with reimbursement, new trials, and capacity expansion driving demand.

\- Placed over 10 NovaSeq 6000s, as some customers expect to remain on the platform for years. Existing on-market clinical tests are more likely to remain on NovaSeq 6000 during replacement activity, while new tests are more likely to begin on NovaSeq X.

\- Sequencing consumables grew 5% YoY, primarily driven by high-throughput volume as the NovaSeq X installed base expanded and pull-through increased.

\- Clinical consumables grew 15% ex-China, including growth above 20% in U.S.-Canada, and represented approximately 65% of sequencing consumables revenue. The Middle East and LATAM weakness contributed to the slowdown to 15% growth ex-China in 2Q, vs. 20% in Q1.

\- Research & Applied consumables declined 7% YoY ex-China, but improved 9% sequentially. Management said it remains too early to call an end-market recovery.

\- NovaSeq X represented approximately 83% of HT sequencing volume and 59% of HT consumables revenue with approximately 78% of clinical volume on the platform. Clinical volume conversion remains expected to reach 80% to 85% by year-end 2026.

\- Oncology remained the leading clinical application. Therapy selection remains larger in dollar terms, while MRD is beginning to drive momentum; rare disease, screening, and NIPT also continued to grow.

\- Low-throughput demand remained strong, supported by MiSeq i100, while mid-throughput demand remained more muted as they are sensitive to the macro environment.

## OTHER COMMENTARY

\- Research customers remain cautious amid funding uncertainty. U.S. funding releases and quoting activity improved late in 2Q26, but it remains too early to call a recovery.

\- Pricing has become more disciplined, with limited discounts on multipack and multiple-box consumables orders but no broad-based discounting. Investment placements remain available for strategic sectors and large-volume opportunities.

\- The Billion Cell Atlas began generating revenue, with over 300M cells delivered and six biopharma partners, supporting AI-enabled drug discovery and predictive biological models.

\- Higher memory and freight costs affected 2Q26, but Illumina secured critical-component supply for the next several quarters and is addressing inflation through pricing and operating efficiencies.

\- Repurchased 0.9M shares for \$122M at an average price of \$129.07 per share. At the end of 2Q26 there was approximately \$1.8B remaining under existing share-repurchase authorizations and plans to continue repurchasing shares opportunistically.

\- Generated \$162M of free cash flow; operating cash flow was affected by tax-payment timing and inventory purchases to secure critical components.

## MODEL UPDATES

## EXHIBIT 5: ILMN Model updates

<table><tr><td></td><td>3Q26E</td><td>4Q26E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Revenues (Core)</td><td>1,152</td><td>1,229</td><td>4,632</td><td>4,937</td><td>5,312</td></tr><tr><td>Previous</td><td>1,127</td><td>1,222</td><td>4,571</td><td>4,813</td><td>5,135</td></tr><tr><td>Difference</td><td>2%</td><td>1%</td><td>1%</td><td>3%</td><td>3%</td></tr><tr><td colspan="6"></td></tr><tr><td>Instruments</td><td>111</td><td>145</td><td>506</td><td>467</td><td>472</td></tr><tr><td>Previous</td><td>102</td><td>146</td><td>490</td><td>460</td><td>465</td></tr><tr><td>Difference</td><td>9%</td><td>-1%</td><td>3%</td><td>1%</td><td>1%</td></tr><tr><td>Consumables</td><td>861</td><td>892</td><td>3,402</td><td>3,723</td><td>4,069</td></tr><tr><td>Previous</td><td>852</td><td>890</td><td>3,384</td><td>3,634</td><td>3,927</td></tr><tr><td>Difference</td><td>1%</td><td>0%</td><td>1%</td><td>2%</td><td>4%</td></tr><tr><td>Core Operating margin</td><td>24%</td><td>26%</td><td>24%</td><td>25%</td><td>26%</td></tr><tr><td>Previous</td><td>24%</td><td>25%</td><td>24%</td><td>25%</td><td>26%</td></tr><tr><td>Difference</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td colspan="6"></td></tr><tr><td>Diluted EPS</td><td>1.36</td><td>1.52</td><

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
