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
# Americas Technology: Hardware: Server 1Q26 market share and outlook update

BOTTOM LINE: We update our industry server model to reflect the latest available 1Q26 data from 650 Group. Key takeaways:

AI server forecasts for 2026-2030 raised by \~18% on average, now expected to reach \~\$1.24 tr by 2030 (v. \$961 bn prior per 4Q25 forecasts), with +3% increased outlook across units and +15% increased outlook across ASPs.  
Traditional server forecasts for 2026-2030 raised by \~31% on average, now forecast to reach \~\$164 bn by 2030 (v. \$105 bn prior per 4Q25 forecasts), with +19% increased outlook across units and +10% increased outlook across ASPs.  
DELL's C1Q26 traditional server revenue was up +85% year-over-year, driven by a +24% year-over-year increase in units and a +49% year-over-year increase in ASPs (v. +92% yoy reported growth for F1Q27, three months ending April 30, 2026). By vertical, 650 Group estimates that Dell's C1Q26 traditional server revenue growth was balanced across neoclouds +102% yoy (+34% yoy units, +50% yoy ASPs) and enterprise +91% yoy (+29% units yoy, +48% ASPs yoy). DELL gained market share in traditional server revenue (30% in 1Q26 v. 20% in 1Q25), including share gains in neocloud (35% in 1Q26 v. 26% in 1Q25) and enterprise (38% in 1Q26 v. 25% in 1Q25).  
HPE's C1Q26 traditional server revenue was up $+20\%$ year-over-year driven by flat unit shipments and $+20\%$ increase in ASPs. HPE maintained $11\%$ market share in traditional server revenue (unchanged v. 1Q25), with $17\%$ enterprise traditional server market share (flat yoy) and $7\%$ neocloud market share (v. $8\%$ in 1Q25).

## Server forecast updates

650 Group upgraded its outlook for the server market, now expecting the overall server market to reach \$1.4 tr by 2030 at 38% 2025-2030 CAGR (v. \$1.1 tr on prior 4Q25 forecast). Estimates for the overall server market were raised by 20% on average, with unit shipment expectations revised up \~+13% and ASPs up \~+6% on average.

650 Group raised its annual AI server forecasts for 2026-2030 by \~18% on average, now expecting the AI server market to achieve \~\$1.24 tr by 2030 (v.

Katherine Murphy

+1(212)902-1151

katherine.a.murphy@gs.com

GS & Co. LLC

Michael Ng, CFA

+1(212)902-8618 | michael.ng@gs.com

GS & Co. LLC

Zorayda Montemayor

+1(212)357-6403

zorayda.montemayor@gs.com

GS & Co. LLC

\$961 bn prior per 4Q25 forecasts), with +3% increased outlook across units and +15% increased outlook across ASPs. By vertical, 650 Group raised its outlook for (1) neocloud AI server revenue growth for 2026-2030 by \~22% on average (+4% units, +17% ASPs), (2) hyperscale AI server revenue growth for 2026-2030 by \~17% on average (+3% units, +13% ASPs), and (3) enterprise AI server revenue growth for 2026-30 by \~16% (+1% units, +16% ASPs). 650 Group is forecasting the AI server revenue market to grow at a +45% 5-yr CAGR with +29% growth in units and +12% growth in ASPs.

650 Group raised its annual traditional server forecasts for 2026-2030 by \~31% on average, now expecting the traditional server market to achieve \~\$164 bn by 2030 (v. \$105 bn prior per 4Q25 forecasts), with +19% increased outlook across units and +10% increased outlook across ASPs. By vertical, 650 Group raised its outlook for (1) enterprise traditional server revenue growth for 2026-2030 by \~48% on average (+30% units, +13% ASPs) and (2) hyperscale traditional server revenue growth for 2026-2030 by \~47% on average (+32% units, +10% ASPs). 650 Group is forecasting the traditional server revenue market to grow at a +13% 5-yr CAGR with +5% growth in units and +8% growth in ASPs.

Exhibit 1: 650 Group expects the overall server market to grow to \$1.4 tr by 2030 on growth across both AI (+45% 5-yr CAGR) and traditional servers (+13% 5-yr CAGR)
Global data center server by vertical and AI/traditional (\$, mn)

<table><tr><td rowspan="2">($, mn)</td><td colspan="3">AI Servers</td></tr><tr><td>2025</td><td>2030</td><td>5-yr CAGR</td></tr><tr><td>Hyperscalers</td><td>$135,444</td><td>$611,663</td><td>35%</td></tr><tr><td>Tier 2 Cloud + SP</td><td>$45,209</td><td>$540,481</td><td>64%</td></tr><tr><td>Enterprise</td><td>$14,430</td><td>$91,472</td><td>45%</td></tr><tr><td>Total AI Data Center</td><td>$195,083</td><td>$1,243,616</td><td>45%</td></tr><tr><td rowspan="2"></td><td colspan="3">Traditional Servers</td></tr><tr><td>2025</td><td>2030</td><td>5-yr CAGR</td></tr><tr><td>Hyperscalers</td><td>$20,881</td><td>$35,164</td><td>11%</td></tr><tr><td>Tier 2 Cloud + SP</td><td>$29,539</td><td>$53,548</td><td>13%</td></tr><tr><td>Enterprise</td><td>$38,570</td><td>$74,844</td><td>14%</td></tr><tr><td>Total Traditional Data Center</td><td>$88,990</td><td>$163,556</td><td>13%</td></tr><tr><td rowspan="2"></td><td colspan="3">Total Servers</td></tr><tr><td>2025</td><td>2030</td><td>5-yr CAGR</td></tr><tr><td>Hyperscalers</td><td>$156,325</td><td>$646,827</td><td>33%</td></tr><tr><td>Tier 2 Cloud + SP</td><td>$74,748</td><td>$594,029</td><td>51%</td></tr><tr><td>Enterprise</td><td>$53,000</td><td>$166,315</td><td>26%</td></tr><tr><td>Total Data Center</td><td>$284,073</td><td>$1,407,171</td><td>38%</td></tr></table>

Source: 650 Group

Exhibit 2: 650 Group raised its annual AI server forecasts for 2026-2030 by \~18% on average, now expecting the AI server market to achieve \~\$1.24 tr by 2030 (v. \$961 bn prior per 4Q25 forecasts)  
Industry AI server estimate revisions (\$, mn)  
![](images/d892071fb86a7baaf012472ff7a27dbd710d38921202b80dc8fb00d23fb5ffba.jpg)

<details>
<summary>bar chart</summary>

| Year | Previous (As of 2Q25) ($ mn) | Previous (As of 3Q25) ($ mn) | Previous (As of 4Q25) ($ mn) | Current (As of 1Q26) ($ mn) |
|---|---|---|---|---|
| 2024 | 100,000 | 100,000 | 100,000 | 100,000 |
| 2025 | 200,000 | 200,000 | 200,000 | 200,000 |
| 2026 | 300,000 | 320,000 | 330,000 | 360,000 |
| 2027 | 420,000 | 450,000 | 480,000 | 540,000 |
| 2028 | 520,000 | 580,000 | 640,000 | 760,000 |
| 2029 | 580,000 | 680,000 | 790,000 | 990,000 |
| 2030 | - | 830,000 | 950,000 | 1250,000 |
</details>

Source: 650 Group

Exhibit 3: Traditional server forecasts for 2026-2030 were revised upwards by \~31% on average annually
Industry traditional server estimate revisions (\$, mn)  
![](images/303a17b014b1c0989b405a2ba567fd9fa4748bcfde94dc4606fde68b8e791620.jpg)

<details>
<summary>bar chart</summary>

| Year | Previous (As of 2Q25) ($ mn) | Previous (As of 3Q25) ($ mn) | Previous (As of 4Q25) ($ mn) | Current (As of 1Q26) ($ mn) |
|---|---|---|---|---|
| 2024 | 80,000 | 80,000 | 80,000 | 80,000 |
| 2025 | 82,000 | 83,000 | 107,000 | 107,000 |
| 2026 | 80,000 | 82,000 | 108,000 | 118,000 |
| 2027 | 78,000 | 81,000 | 114,000 | 128,000 |
| 2028 | 75,000 | 80,000 | 102,000 | 139,000 |
| 2029 | 73,000 | 79,000 | 103,000 | 151,000 |
| 2030 | - | 79,000 | 105,000 | 164,000 |
</details>

Source: 650 Group

## C1Q26 vendor market share

DELL gained share in the traditional & AI server markets, with broad-based growth across enterprise and neocloud verticals driven by both unit growth and ASP uplift. Per 650 Group estimates:

DELL's C1Q26 traditional server revenue was up +85% year-over-year (v. +92% reported), driven by a +24% increase in units and a +49% increase in ASPs. By vertical, 650 Group estimates that Dell's C1Q26 traditional server revenue growth was balanced across neoclouds +102% yoy (+34% yoy units, +50% yoy ASPs) and enterprise +91% yoy (+29% units yoy, +48% ASPs yoy). DELL's C1Q26 traditional server hardware revenue of \~\$8.0 bn was \~54% enterprise, \~40% neocloud, \~6% hyperscalers/service provider (v. 52%/36%/12% in C1Q25). DELL gained market share in traditional server revenue (30% in 1Q26 v. 20% in 1Q25), including share gains in neocloud (35% in 1Q26 v. 26% in 1Q25) and enterprise (38% in 1Q26 v. 25% in 1Q25).  
- DELL's C1Q26 AI server revenue was up +\$11.3 bn year-over-year (+622% year-over-year), driven by a +300% increase in units and a +81% increase in ASPs. By vertical, 650 Group estimates that Dell's C1Q26 AI server revenue growth was broadbased across neoclouds (+\$9 bn) and enterprise (+\$2 bn). DELL gained market share in AI server revenue (17% in 1Q26 v. 5% in 1Q25), including share gains in neocloud (48% in 1Q26 v. 24% in 1Q25) and enterprise (47% in 1Q26 v. 17% in 1Q25).

HPE maintained its share in the traditional server market but ceded some share in AI servers. Per 650 Group estimates:

HPE's C1Q26 traditional server revenue was up $+20\%$ year-over-year driven by flat unit shipments and $+20\%$ increase in ASPs. By vertical, 650 Group estimates that HPE's C1Q26 traditional server revenue balanced growth across enterprise $+22\%$ $(+1\%$ units, $+21\%$ ASPs) and neoclouds $+18\%$ $(-1\%$ units, $+19\%$ ASPs). HPE

maintained 11% market share in traditional server revenue (unchanged v. 1Q25), with 17% enterprise traditional server market share (flat YoY) and 7% neocloud market share (v. 8% in 1Q25).

HPE's C1Q26 AI server revenue was up +11% year-over-year (\~flat sequentially), with units -6% year-over-year and ASPs +18%. By vertical, 650 Group estimates that HPE's C1Q26 AI server revenue growth was balanced across neoclouds (+11%) and enterprise (+10%). HPE lost market share in the overall AI server revenue market in enterprise, with 17% share in 1Q26 v. 30% share in 1Q25.

## SMCI lost AI server market share, but gained +1 pt of traditional server market share. Per 650 Group estimates:

SMCI's C1Q26 traditional server revenue was up $+58\%$ year-over-year, with a $-23\%$ decrease in units offset by a $+104\%$ increase in ASPs. Per 650 Group, SMCI primarily sold traditional servers to neoclouds, where it had $10\%$ market share in the quarter (v. $2\%$ market share in 1Q25).  
SMCI's C1Q26 AI server revenue was up +\$5.3 bn year-over-year (+173%), driven by a +164% increase in units and a +4% increase in ASPs. By vertical, 650 Group estimates that SMCI's C1Q26 AI server revenue growth was driven by neoclouds (+260% year-over-year). SMCI gained market share in AI server revenue (11% in 1Q26 v. 8% in 1Q25), with share gains in enterprise (4% share in 1Q26 v. 2% in 1Q25) and service provider (42% v. 9% in 1Q25) more than offsetting weaker market share in neocloud (33% v. 37% in 1Q25)

Exhibit 4: Nvidia leads the AI server market with 44% share as of 1Q26, followed by whitebox players (22%), Dell (17%), and Super Micro (11%)  
AI server revenue market share (%)  
![](images/946442ae1274319da5434ea0460d47127da13dc7506ffd832c1ab52cf2adc207.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell  | HPE   | Super Micro | Nvidia | Others - White Box |
|---------|-------|-------|-------------|--------|--------------------|
| 1Q23    | 10%   | 10%   | 10%         | 15%    | 50%                |
| 2Q23    | 5%    | 5%    | 15%         | 40%    | 20%                |
| 3Q23    | 5%    | 5%    | 15%         | 65%    | 15%                |
| 4Q23    | 5%    | 5%    | 15%         | 60%    | 10%                |
| 1Q24    | 5%    | 5%    | 15%         | 60%    | 10%                |
| 2Q24    | 5%    | 5%    | 15%         | 60%    | 10%                |
| 3Q24    | 5%    | 5%    | 15%         | 55%    | 10%                |
| 4Q24    | 5%    | 5%    | 15%         | 55%    | 15%                |
| 1Q25    | 5%    | 5%    | 10%         | 50%    | 20%                |
| 2Q25    | 10%   | 5%    | 10%         | 45%    | 20%                |
| 3Q25    | 10%   | 5%    | 10%         | 45%    | 20%                |
| 4Q25    | 10%   | 5%    | 10%         | 40%    | 20%                |
| 1Q26    | 15%   | 5%    | 10%         | 40%    | 20%                |
</details>

Source: 650 Group

Exhibit 5: Neocloud AI server market share leadership oscillates between DELL and SMCI  
Neocloud AI server revenue market share (%)  
![](images/be0b62804bfdd1c7b51f4d0b91079f97f95754a99bd655e80b5e11014466ad12.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell  | Nvidia | Super Micro |
|---------|-------|--------|-------------|
| 1Q23    | 10%   | 20%    | 30%         |
| 2Q23    | 15%   | 10%    | 70%         |
| 3Q23    | 20%   | 15%    | 45%         |
| 4Q23    | 25%   | 10%    | 55%         |
| 1Q24    | 30%   | 10%    | 40%         |
| 2Q24    | 40%   | 10%    | 35%         |
| 3Q24    | 35%   | 10%    | 40%         |
| 4Q24    | 30%   | 10%    | 45%         |
| 1Q25    | 25%   | 10%    | 35%         |
| 2Q25    | 45%   | 5%     | 30%         |
| 3Q25    | 40%   | 5%     | 25%         |
| 4Q25    | 35%   | 5%     | 50%         |
| 1Q26    | 45%   | 5%     | 30%         |
</details>

Source: 650 Group

Exhibit 6: Dell gained significant share in enterprise AI servers in 1Q26 (47%)  
Enterprise AI server revenue market share  
![](images/d5206e8604fe73a50d16e070a0a1830b61eb8a4c54e656b7e45ec6d41e85022a.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell | HPE | Nvidia | Super Micro | Others - White Box |
|---------|------|-----|--------|-------------|---------------------|
| 1Q21    | 10%  | 65% | 10%    | 0%          | 0%                  |
| 2Q21    | 10%  | 65% | 10%    | 0%          | 0%                  |
| 3Q21    | 10%  | 70% | 10%    | 0%          | 0%                  |
| 4Q21    | 10%  | 55% | 10%    | 0%          | 0%                  |
| 1Q22    | 10%  | 55% | 10%    | 0%          | 0%                  |
| 2Q22    | 10%  | 55% | 10%    | 0%          | 0%                  |
| 3Q22    | 10%  | 55% | 10%    | 0%          | 0%                  |
| 4Q22    | 10%  | 60% | 10%    | 0%          | 0%                  |
| 1Q23    | 30%  | 30% | 20%    | 0%          | 0%                  |
| 2Q23    | 30%  | 30% | 20%    | 0%          | 0%                  |
| 3Q23    | 30%  | 30% | 20%    | 0%          | 0%                  |
| 4Q23    | 30%  | 30% | 20%    | 0%          | 0%                  |
| 1Q24    | 30%  | 35% | 20%    | 0%          | 0%                  |
| 2Q24    | 30%  | 45% | 20%    | 0%          | 0%                  |
| 3Q24    | 30%  | 45% | 20%    | 0%          | 0%                  |
| 4Q24    | 30%  | 45% | 20%    | 0%          | 0%                  |
| 1Q25    | 30%  | 35% | 20%    | 0%          | 0%                  |
| 2Q25    | 30%  | 35% | 20%    | 0%          | 0%                  |
| 3Q25    | 30%  | 35% | 20%    | 5%          | 0%                  |
| 4Q25    | 35%  | 35% | 15%    | 10%         | 0%                  |
| 1Q26    | 45%  | 15% | 10%    | 5%          | 0%                  |
</details>

Source: 650 Group

Exhibit 7: Dell lead the traditional server market in 1Q26 (30% share), followed by white-box (24%), HPE (11%), Lenovo (7%), and IBM (6%).  
Traditional server revenue market share (%)  
![](images/91aa922ddd44078929a86c3d2e139ce8dc6bbf62fb83d2beef36cb6cdc2e5e4b.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell  | HPE   | IBM   | Lenovo | Others - White Box |
|---------|-------|-------|-------|--------|---------------------|
| 1Q23    | 17.5% | 17.0% | 6.0%  | 7.0%   | 31.0%               |
| 2Q23    | 17.5% | 17.0% | 6.0%  | 7.0%   | 30.0%               |
| 3Q23    | 17.5% | 17.0% | 6.0%  | 7.0%   | 30.0%               |
| 4Q23    | 17.5% | 17.0% | 6.0%  | 7.0%   | 30.0%               |
| 1Q24    | 15.0% | 14.0% | 6.0%  | 8.0%   | 35.0%               |
| 2Q24    | 15.0% | 13.0% | 6.0%  | 9.0%   | 34.0%               |
| 3Q24    | 20.0% | 12.0% | 6.0%  | 9.0%   | 32.0%               |
| 4Q24    | 20.0% | 12.0% | 6.0%  | 10.0%  | 27.0%               |
| 1Q25    | 20.0% | 12.0% | 6.0%  | 11.0%  | 28.0%               |
| 2Q25    | 15.0% | 13.0% | 6.0%  | 12.0%  | 28.0%               |
| 3Q25    | 22.0% | 12.0% | 6.0%  | 11.0%  | 26.0%               |
| 4Q25    | 19.0% | 12.0% | 8.0%  | 12.0%  | 27.0%               |
| 1Q26    | 30.0% | 11.0% | 6.0%  | 7.0%   | 24.0%               

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
