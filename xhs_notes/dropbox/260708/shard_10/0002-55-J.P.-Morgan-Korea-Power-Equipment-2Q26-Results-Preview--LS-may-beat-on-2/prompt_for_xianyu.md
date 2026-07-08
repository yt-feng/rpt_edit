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
## Korea Power Equipment

## 2Q26 Results Preview: LS may beat on 2Q new orders, Hyosung may miss on earnings on ME impact

Korea power equipment companies will report 2Q results during the last two weeks of July. We forecast divergent trends among the companies we cover. LS Electric is likely to beat on its new orders growth (\~KRW 2 trillion, vs KRW 1 trillion in 1Q), and the company may consider revising up its FY26 new orders guidance from KRW 5 trn to KRW 6 trn. On the other hand, Hyosung Heavy's operating profit may miss consensus estimates on the back of the impact of the Middle East conflict (5-10% of new orders in FY25). The company also had a high base of new orders (KRW 4 trillion in 1Q), and sequential order momentum may ebb. Key focus areas for the results include: 1) Assessment of local opportunities after the Korean memory behemoths announcing their long-term investment plans; 2) AIDC order wins for Hyundai Electric and Hyosung Heavy, as both companies have the majority of orders from utilities/grids instead of DCs; and 3) Progress on tariff rebates, margin expansion, and potential revision of FY new orders/profit guidance. See page 3 for earnings previews and page 4 for earnings/PT changes.

\- Hyosung Heavy: High base for new orders: We forecast operating profit for Hyosung Heavy to reach KRW 266bn (+62%/74% YoY/QoQ, 6% below consensus). Key focus areas for the results include: 1) Orders momentum in 2Q and whether management will revise up its FY26 guidance (10% growth yoy) following a doubling of orders in 1Q; 2) The pace of order wins for 765kV new orders and the impact of the delay in progress for 765kV projects (like in Texas); 3) More details on the joint venture established with Quanta Services (link) and the company's strategy for AIDC orders in the US.

\- LS Electric: New orders likely to beat, core earnings in line: We forecast operating profit for LS Electric to reach KRW167bn (+54%/32% YoY/QoQ, >5% above consensus). Its new orders were likely strong at >KRW 2 tn during 2Q, much higher than \~KRW1 tn in 1Q. This is a function of strong order intake momentum from the data centers in the US during the quarter. While the company already revised up its FY26 new orders guidance from KRW 4 tn to KRW 5 tn earlier this year (note), there is a possibility for the company to further revise it up to KRW 5-6 tn on our estimates. Key focus areas for the results include: 1) More details about the recent capacity expansion plan in the US (in Utah), and whether the company will further add capacity for other products in the States; 2) Details about AIDC project wins and the progress of product wins from new customers; 3) Potential revision of full year guidance (such as the KRW 600bn operating profit target); and 4) Mgmt comments on tailwinds from Korea’s massive AI expansion project (see note by our Korea Tech analyst).

\- Hyundai Electric: Key focus on AIDC new orders and FY26 order guidance: We forecast operating profit for Hyundai Electric to be KRW 301bn (in line with consensus). Key focus areas for the results include: 1) The impact of the Middle East conflict on the company's earnings in the region; (\~10% the total orders in ME in FY25); 2) More details about project wins of AIDC orders in the US. Note that local news (Korea JoongAng Daily) reported that the company won a >\$700mn order from an AIDC earlier; 3) New order momentum in 2Q after a strong beat in 1Q, and potential revision of FY new orders guidance; and 4) trends in subsidiaries' revenues (which declined in 1Q due to a scheduled delay in product delivery in Atlanta).

See page 17 for analyst certification and important disclosures, including non-US analyst disclosures.

Power Equipment and Utilities

Stephen Tsui, CFA AC
(852) 2800-8592
stephen.tsui@JPM.com

Vento Suen

(852) 2800-8546

vento.suen@JPM.com

Alan Hon

(852) 2800-8573

alan.hon@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td colspan="2">Cur End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>HD Hyundai Electric</td><td>267260 KS</td><td>21,726</td><td>KRW</td><td>922,000</td><td>OW</td><td>n/c</td><td>1,375,000</td><td>Jun-27</td><td>1,315,000</td><td>Dec-26</td></tr><tr><td>Hyosung Heavy Industries</td><td>298040 KS</td><td>18,940</td><td>KRW</td><td>3,107,000</td><td>OW</td><td>n/c</td><td>4,100,000</td><td>Jun-27</td><td>3,900,000</td><td>Dec-26</td></tr><tr><td>LS Electric</td><td>010120 KS</td><td>21,229</td><td>KRW</td><td>216,500</td><td>N</td><td>n/c</td><td>200,000</td><td>Jun-27</td><td>190,000</td><td>n/c</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 06 Jul 26.

## 2Q26 Earnings Preview

Table 1: KR power equipment 2Q26E earnings preview

<table><tr><td>KRW bn</td><td>2Q25</td><td>1Q26</td><td>2Q26E</td><td>YoY</td><td>QoQ</td><td>Consensus</td><td>Difference</td></tr><tr><td colspan="8">HD Hyundai Electric</td></tr><tr><td>Revenue</td><td>906</td><td>1,037</td><td>1,187</td><td>31%</td><td>15%</td><td>1,126</td><td>5%</td></tr><tr><td>Operating profit</td><td>209</td><td>258</td><td>301</td><td>44%</td><td>16%</td><td>296</td><td>2%</td></tr><tr><td>OP margin</td><td>23.1%</td><td>24.9%</td><td>25.3%</td><td>2.3ppt</td><td>0.4ppt</td><td>26.3%</td><td>-0.9ppt</td></tr><tr><td>NP</td><td>142</td><td>208</td><td>219</td><td>54%</td><td>5%</td><td>224</td><td>-2%</td></tr><tr><td colspan="8">Hyosung Heavy</td></tr><tr><td>Revenue</td><td>1,525</td><td>1,358</td><td>1,769</td><td>16%</td><td>30%</td><td>1,804</td><td>-2%</td></tr><tr><td>Operating profit</td><td>164</td><td>152</td><td>266</td><td>62%</td><td>74%</td><td>284</td><td>-6%</td></tr><tr><td>OP margin</td><td>10.8%</td><td>11.2%</td><td>15.0%</td><td>4.2ppt</td><td>3.8ppt</td><td>15.7%</td><td>-0.7ppt</td></tr><tr><td>NP</td><td>93</td><td>87</td><td>201</td><td>118%</td><td>131%</td><td>211</td><td>-5%</td></tr><tr><td colspan="8">LS Electric</td></tr><tr><td>Revenue</td><td>1,193</td><td>1,377</td><td>1,607</td><td>35%</td><td>17%</td><td>1,494</td><td>8%</td></tr><tr><td>Operating profit</td><td>109</td><td>127</td><td>167</td><td>54%</td><td>32%</td><td>158</td><td>6%</td></tr><tr><td>OP margin</td><td>9.1%</td><td>9.2%</td><td>10.4%</td><td>1.3ppt</td><td>1.2ppt</td><td>10.6%</td><td>-0.2ppt</td></tr><tr><td>NP</td><td>67</td><td>121</td><td>119</td><td>77%</td><td>-1%</td><td>114</td><td>4%</td></tr></table>

Source: Company data, Bloomberg Finance L.P. (for consensus), JPM estimates.

Hyundai Electric: Key focus on AIDC new orders and FY26 order guidance: We forecast operating profit for Hyundai Electric to be KRW 301bn (in line with consensus). Key focus areas for the results include: 1) The impact of the Middle East conflict on the company's earnings in the region; (\~10% the total orders in ME in FY25); 2) More details about project wins of AIDC orders in the US. Note that local news (Korea JoongAng Daily) reported that the company won a >\$700mn order from an AIDC earlier; 3) New order momentum in 2Q after a strong beat in 1Q, and potential revision of FY new orders guidance; and 4) trends in subsidiaries' revenues (which declined in 1Q due to a scheduled delay in product delivery in Atlanta).

Hyosung Heavy: We forecast operating profit for Hyosung Heavy to reach KRW 266bn (+62%/74% YoY/QoQ, 6% below consensus). Key focus areas for the results include: 1) Orders momentum in 2Q and whether management will revise up its FY26 guidance (10% growth yoy) following a doubling of orders in 1Q; 2) The pace of order wins for 765kV new orders and the impact of the delay in progress for 765kV projects (like in Texas); 3) More details on the joint venture established with Quanta Services (link) and the company's strategy for AIDC orders in the US.

LS Electric: New orders likely to beat, core earnings in line: We forecast operating profit to reach KRW167bn (+54%/32% YoY/QoQ, >5% above cons.). New orders were likely strong at >KRW 2tn during 2Q, much higher than \~KRW1 tn in 1Q. This is a function of strong order intake momentum from the data centers in the US during the Q. While the company already revised up its FY26 new orders guidance from KRW 4 tn to KRW 5 tn earlier this year (note), there is a possibility for the company to further revise it up to KRW 5-6 tn on our estimates. Key focus areas for the results: 1) More details about recent capacity expansion plan in the US (Utah), and whether the co will further add capacity for other products in the States; 2) Details about AIDC project wins and the progress of product wins from new customers; 3) Potential revision of full year guidance (such as the KRW 600bn operating profit target); 4) Mgmt comments on tailwinds from Korea's massive AI expansion project (note by our Korea Tech analyst).

## Model updates

Hyundai Electric: We revise up our 27-28E earnings by 2-3% to reflect higher assumptions for power equipment sales in the US on the back of its project wins of >US \$700mn in new orders from a hyperscaler, which is a break-through to the AIDC market. We also roll forward our PT from Dec 26 to Jun 27, and we trim our multiple for the North America segment from 40x to 35x to reflect slightly slower growth CAGR ahead on a higher earnings base after a few years of stellar earnings performance since 2023. All in all, we lift our PT from KRW 1,315k/sh to KRW 1,375k. We maintain an OW rating.

Hyosung Heavy: We revise up our 27-28E earnings by 3% to reflect higher assumptions for power equipment sales in the US on the back of its recent initiatives of forming a JV with Quanta Services (PWR US, OW, covered by Mark Strouse). We also roll forward our PT from Dec 26 to Jun 27, and we trim our multiple for the US LPT business from 40x to 35x to reflect slightly slower growth CAGR ahead on a higher earnings base after a few years of very strong earnings performance since 2023. All in all, lift our PT from KRW 3,900k/sh to KRW 4,100k. We maintain an OW rating.

LS Electric: We revise up 26-28E earnings by 1-4% to reflect stronger-than-expected order wins during 2Q and the potential revision of FY26 new order guidance (from KRW 5 trillion to KRW 6 trillion). Accordingly, we lift our Jun-27 PT from KRW 190k to KRW 200k and maintain a Neutral rating on the back of rich valuation.

Table 2: Earnings and PT changes
KRW bn

<table><tr><td rowspan="2"></td><td colspan="3">Previous</td><td colspan="3">Current</td><td colspan="3">Change</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Hyundai Electric (KRW bn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>4,830</td><td>5,632</td><td>6,368</td><td>5,040</td><td>5,746</td><td>6,535</td><td>4%</td><td>2%</td><td>3%</td></tr><tr><td>Operating profit</td><td>1,262</td><td>1,648</td><td>1,927</td><td>1,332</td><td>1,689</td><td>1,988</td><td>5%</td><td>2%</td><td>3%</td></tr><tr><td>Attributable profit</td><td>997</td><td>1,287</td><td>1,515</td><td>1,007</td><td>1,316</td><td>1,562</td><td>1%</td><td>2%</td><td>3%</td></tr><tr><td>PT (KRW/sh)</td><td></td><td></td><td>1,315,000</td><td></td><td></td><td>1,375,000</td><td></td><td></td><td>5%</td></tr><tr><td>Rating</td><td></td><td></td><td>OW</td><td></td><td></td><td>OW</td><td></td><td></td><td></td></tr><tr><td>Hyosung Heavy (KRW bn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>6,975</td><td>8,411</td><td>9,780</td><td>6,975</td><td>8,669</td><td>10,088</td><td>0%</td><td>3%</td><td>3%</td></tr><tr><td>Operating profit</td><td>1,054</td><td>1,458</td><td>1,811</td><td>1,054</td><td>1,498</td><td>1,863</td><td>0%</td><td>3%</td><td>3%</td></tr><tr><td>Attributable profit</td><td>785</td><td>1,102</td><td>1,412</td><td>794</td><td>1,133</td><td>1,452</td><td>1%</td><td>3%</td><td>3%</td></tr><tr><td>PT (KRW/sh)</td><td></td><td></td><td>3,900,000</td><td></td><td></td><td>4,100,000</td><td></td><td></td><td>5%</td></tr><tr><td>Rating</td><td></td><td></td><td>OW</td><td></td><td></td><td>OW</td><td></td><td></td><td></td></tr><tr><td>LS Electric (KRW bn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>6,289</td><td>7,378</td><td>8,347</td><td>6,321</td><td>7,450</td><td>8,476</td><td>1%</td><td>1%</td><td>2%</td></tr><tr><td>Operating profit</td><td>724</td><td>971</td><td>1,186</td><td>729</td><td>1,001</td><td>1,232</td><td>1%</td><td>3%</td><td>4%</td></tr><tr><td>Attributable profit</td><td>501</td><td>679</td><td>836</td><td>505</td><td>700</td><td>869</td><td>1%</td><td>3%</td><td>4%</td></tr><tr><td>PT (KRW/sh)</td><td></td><td></td><td>190,000</td><td></td><td></td><td>200,000</td><td></td><td></td><td>5%</td></tr><tr><td>Rating</td><td></td><td></td><td>N</td><td></td><td></td><td>N</td><td></td><td></td><td></td></tr></table>

Source: JPM estimates.

## Overweight

267260.KS, 267260 KS
Price (06 Jul 26):W922,000

▲ Price Target (Jun-27):W1,375,000  
Prior (Dec-26):W1,315,000

## Power Equipment and Utilities

Stephen Tsui, CFA AC
(852) 2800-8592
stephen.tsui@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Quarterly Forecasts (FYE Dec)

<table><tr><td colspan="4">Adj. EPS (W)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>4,274</td><td>5,772A</td><td>9,112</td></tr><tr><td>Q2</td><td>3,951</td><td>6,083</td><td>8,458</td></tr><tr><td>Q3</td><td>5,301</td><td>7,067</td><td>8,612</td></tr><tr><td>Q4</td><td>6,797</td><td>9,003</td><td>10,336</td></tr><tr><td>FY</td><td>20,324</td><td>27,927</td><td>36,517</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>80</td><td>77</td><td>60</td><td>42</td><td>12</td></tr><tr><td>Growth</td><td>10</td><td>12</td><td>7</td><td>40</td><td>72</td></tr><tr><td>Momentum</td><td>16</td><td>11</td><td>26</td><td>2</td><td>28</td></tr><tr><td>Quality</td><td>1</td><td>4</td><td>3</td><td>11</td><td>87</td></tr><tr><td>Low Vol</td><td>75</td><td>95</td><td>91</td><td>89</td><td>98</td></tr></table>

## HD Hyundai Electric

## Revise earnings/PT to reflect higher US sales assumptions

We revise up our 27-28E earnings by 2-3% to reflect higher assumptions of power equipment sales in the US on the back of its project wins of >US\$700mn in new orders from a hyperscaler, which is a break-through to the AIDC market. We also roll forward our PT from Dec 26 to Jun 27, we trim our multiple for the North America segment from 40x to 35x to reflect slightly slower growth CAGR ahead on a higher earnings base after a few years of stellar earnings performance since 2023. All in all, we lift our PT from KRW 1,315k/sh to KRW 1,375k. We maintain an OW rating.

Price Performance  
![](images/1a4feb17756bd95a38bf6bb2ca49b60f6b84edebb806cbdfef4bb7081aaf516f.jpg)

— 267260.KS Price (W) — KOSPI (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>18.4%</td><td>-3.6%</td><td>1.6%</td><td>113.4%</td></tr><tr><td>Rel</td><td>-72.7%</td><td>-2.2%</td><td>-46.1%</td><td>-49.7%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>36</td></tr><tr><td>52-week range (W)</td>

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
