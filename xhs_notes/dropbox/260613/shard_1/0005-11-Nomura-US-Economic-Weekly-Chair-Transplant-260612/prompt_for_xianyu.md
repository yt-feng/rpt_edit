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
## US Economic Weekly

Economics - North America

## Chair Transplant

- We expect the Fed to remain on hold at the June FOMC meeting. The meeting statement will likely drop the easing bias, and we expect the dot plot medians to show rates on hold through the end of 2027.  
- We think Chair Warsh will decline to submit his own economic and policy projections. In his first press conference, Warsh may continue to downplay the usefulness of forward guidance, while hinting at a future case for rate cuts.  
- CPI and PPI inflation data point to an acceleration in core PCE inflation to $0.345\%$ m-o-m or $3.426\%$ y-o-y in May. Pipeline price pressures measured by PPI data continued to grow and point to an upside risk to the inflation outlook.

## We expect the Fed to remain on hold and remove an easing bias

The Fed will likely keep the policy rate on hold for the fourth consecutive meeting at the June FOMC meeting. Since the April meeting, economic indicators show growing inflation risks, while labor markets have stabilized with some signs of acceleration.

Fig. 1: The Fed will likely keep the policy rate on hold  
![](images/c2ae3fe51175c523d0c55c405234c7156a028f799f91036b80ce3c1edb95b94f.jpg)

<details>
<summary>line chart</summary>

| Date   | March FOMC median forecast | OIS fwd rates (as of 11 Jun) | NOM's policy rate forecast |
|--------|----------------------------|------------------------------|-------------------------------|
| Mar 23 | 4.80                       | 4.80                         | 4.80                          |
| Dec 23 | 5.40                       | 5.40                         | 5.40                          |
| Sep 24 | 4.80                       | 4.80                         | 4.80                          |
| Jun 25 | 4.40                       | 4.40                         | 4.40                          |
| Mar 26 | 3.80                       | 3.80                         | 3.80                          |
| Dec 26 | 3.60                       | 3.60                         | 3.60                          |
| Sep 27 | 3.20                       | 3.80                         | 3.60                          |
</details>

Source: FRB, Bloomberg, NOM

## Research Analysts

## North America Economics

## Aichi Amemiya - NSI

aichi.amemiya@NOM.com

+1 212 667 9347

## Jeremy Schwartz - NSI

jeremy.schwartz@NOM.com

+1 212 667 9637

## Ruchir Sharma - NSI

ruchir.sharma@NOM.com

+1 212 667 9186

## Jacklyn Goloborodsky - NSI

jacklyn.goloborodsky@NOM.com

+1 212 298 4739

## Global Economics

## David Seif - NSI

david.seif@NOM.com

+1 212 667 9180

Fig. 2: We expect Chair Warsh to acknowledge the current hawkish macroeconomic environment, but make a case for policy easing in the medium term

<table><tr><td>Tool</td><td>Key assumptions</td></tr><tr><td colspan="2">Policy rate</td></tr><tr><td>2026</td><td>No rate cuts, EOP 3.625%</td></tr><tr><td>2027</td><td>No rate cuts, EOP 3.625%</td></tr><tr><td>Terminal</td><td>3.50 - 3.75%</td></tr><tr><td colspan="2">Balance sheet policy</td></tr><tr><td>Size</td><td>Reserve management purchases of $10bn/month. The NY Fed is actively managing reserve management purchases in response to seasonal liquidity demand and market conditions. We expect balance sheet growth to average $20bn per month in the medium term.</td></tr><tr><td>Composition</td><td>MBS rundown to continue, with proceeds reinvested into Treasuries. Both reinvestments and eventual reserve management purchases will be skewed towards Treasury bills.</td></tr></table>

Source: FRB, NOM

We expect the post-meeting policy statement will remove the easing bias from the forward guidance language with unanimous support. Fedspeak has turned more hawkish recently, with several FOMC participants explicitly discussing the possibility of a rate hike. That being said, a dovish faction on the Committee remains cautiously optimistic about the inflation outlook and sees policy as moderately restrictive.

Revisions to the economic projections will likely be concentrated in the inflation outlook. We expect the median inflation projection for both the headline PCE and core PCE price indices will rise over the near term (Fig. 3). We expect policymakers will make a mark-to-market adjustment to their unemployment rate projections for 2026 and 2027, reflecting recent strength in labor markets. We expect real GDP growth projections will remain unchanged from the March meeting.

Fig. 3: We expect the median inflation projection for both headline PCE and core PCE price indices to rise over the near term NOM's forecast for the June 2026 Summary of Economic Projections

<table><tr><td></td><td></td><td>2026</td><td>2027</td><td>2028</td><td>Longer-run</td></tr><tr><td rowspan="2">Change in real GDP</td><td>Jun-26</td><td>2.4</td><td>2.3</td><td>2.1</td><td>2.0</td></tr><tr><td>Mar-26</td><td>2.4</td><td>2.3</td><td>2.1</td><td>2.0</td></tr><tr><td rowspan="2">Unemployment rate</td><td>Jun-26</td><td>4.3</td><td>4.2</td><td>4.2</td><td>4.2</td></tr><tr><td>Mar-26</td><td>4.4</td><td>4.3</td><td>4.2</td><td>4.2</td></tr><tr><td rowspan="2">PCE inflation</td><td>Jun-26</td><td>3.6</td><td>2.2</td><td>2.0</td><td>2.0</td></tr><tr><td>Mar-26</td><td>2.7</td><td>2.2</td><td>2.0</td><td>2.0</td></tr><tr><td rowspan="2">Core PCE inflation</td><td>Jun-26</td><td>3.2</td><td>2.3</td><td>2.0</td><td></td></tr><tr><td>Mar-26</td><td>2.7</td><td>2.2</td><td>2.0</td><td></td></tr><tr><td colspan="6">Projected appropriate policy path: Median</td></tr><tr><td rowspan="2"></td><td>Jun-26</td><td>3.625</td><td>3.625</td><td>3.375</td><td>3.250</td></tr><tr><td>Mar-26</td><td>3.375</td><td>3.125</td><td>3.125</td><td>3.125</td></tr></table>

Source: FRB, Haver, NOM

We do not expect Chair Warsh to submit interest rate projections for the dot plot, consistent with his past criticisms of Fed forward guidance (Fig. 4). Such an omission would reduce the total number of dots to 18 from 19. Warsh cannot unilaterally eliminate any aspects of the summary of economic projections, but there is a precedent for participants declining to submit forecasts.

We expect the median dots for 2026 and 2027 will rise to $3.625\%$ , indicating no change from the current rate level for the next one and a half years. Given that most officials have discussed multiple scenarios, it is difficult to gauge individual dots for 2026, but we expect that 4-5 dots will indicate a rate hike, 7-9 dots will correspond to no changes, and 4-6 dots will be consistent with rate cuts. We expect the median 2028 dot to be $3.375\%$ , consistent with one rate cut, and the longer-run median dot (a proxy of the neutral rate of interest) to be revised up to $3.250\%$ from $3.125\%$ , as the FOMC participants' characterization of the policy stance suggests an upward revision to their estimate of neutral rate.

Fig. 4: We think Warsh will decline to submit his interest rate projections for the dot plot, which is consistent with his past criticisms of Fed forward guidance  
NOM's expectation for policymakers' 2026 dots

<table><tr><td>%</td><td colspan="2">2026 dot as of June (NOM&#x27;s expectation)</td><td></td></tr><tr><td>3.875</td><td>Goolsbee</td><td>One rate hike</td><td>1</td></tr><tr><td>3.875</td><td>Schmid</td><td>One rate hike</td><td>2</td></tr><tr><td>3.875</td><td>Hammack</td><td>One rate hike</td><td>3</td></tr><tr><td>3.875</td><td>Musalem</td><td>One rate hike</td><td>4</td></tr><tr><td>3.875</td><td>Logan</td><td>One rate hike</td><td>5</td></tr><tr><td>3.625</td><td>Collins</td><td>No more rate cuts</td><td>6</td></tr><tr><td>3.625</td><td>Barkin</td><td>No more rate cuts</td><td>7</td></tr><tr><td>3.625</td><td>Kashkari</td><td>No more rate cuts</td><td>8</td></tr><tr><td>3.625</td><td>Barr</td><td>No more rate cuts</td><td>9</td></tr><tr><td>3.625</td><td>Venable</td><td>No more rate cuts</td><td>10</td></tr><tr><td>3.625</td><td>Cook</td><td>No more rate cuts</td><td>11</td></tr><tr><td>3.625</td><td>Waller</td><td>No more rate cuts</td><td>12</td></tr><tr><td>3.375</td><td>Jefferson</td><td>One more rate cut</td><td>13</td></tr><tr><td>3.375</td><td>Powell</td><td>One more rate cut</td><td>14</td></tr><tr><td>3.375</td><td>Daly</td><td>One more rate cut</td><td>15</td></tr><tr><td>3.375</td><td>Paulson</td><td>One more rate cut</td><td>16</td></tr><tr><td>3.375</td><td>Williams</td><td>One more rate cut</td><td>17</td></tr><tr><td>3.125</td><td>Bowman</td><td>Two more rate cuts</td><td>18</td></tr><tr><td>3.125</td><td>Warsh</td><td>Two more rate cuts</td><td>19</td></tr></table>

Source: FRB, NOM

In the press conference, we think Warsh is unlikely to call for an immediate rate cut given the current hawkish macroeconomic environment. However, we think Warsh could make a case for policy easing in the medium term, suggesting that a pause in easing is largely driven by uncertainty around the Iran war. As he did at his confirmation hearing, we expect Warsh to reiterate his view that AI will boost productivity and lead to disinflation. Warsh may also characterize currently elevated inflation as a temporary phenomenon due to the Iran war.

Warsh may continue to downplay the usefulness of core PCE inflation and instead propose alternative inflation measures. He may also discuss the possibility of balance sheet reduction, possibly laying out a roadmap or timeframe for a smaller balance sheet. In addition, he could discuss how he might make changes to the Fed's communication strategy.

## May CPI and PPI reports point to an acceleration in core PCE inflation

Incorporating CPI and PPI data, we forecast core PCE inflation of $0.345\%$ m-o-m in May from $0.23\%$ in April. This would translate into y-o-y core PCE inflation of $3.426\%$ , the highest reading since October 2023.

Fig. 5: Core PCE inflation likely accelerated in May, driven by components derived from PPI data  
Decomposition of m-o-m core PCE inflation by data source  
![](images/676b24a4bc560fdfaaf9113948e72d788da1be90d353ff2dc2e7b9b5c24cac03.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date | Other components (m-o-m %) | Contributions from components that are covered by PPI (m-o-m %) | Contributions from components that are covered by CPI (m-o-m %) | Core PCE inflation (m-o-m %) |
|---|---|---|---|---|
| Jan-23 | 0.05 | 0.15 | 0.25 | 0.45 |
| Jul-23 | -0.05 | 0.05 | 0.10 | 0.20 |
| Jan-24 | 0.05 | 0.15 | 0.25 | 0.50 |
| Jul-24 | 0.05 | 0.10 | 0.15 | 0.25 |
| Jan-25 | 0.05 | 0.15 | 0.25 | 0.45 |
| Jul-25 | 0.05 | 0.10 | 0.15 | 0.25 |
| Jan-26 | 0.05 | 0.15 | 0.25 | 0.45 |
forecast
(m o-m %)
</details>

Source: BLS, BEA, Haver, NOM

Fig. 6: Y-o-y core PCE inflation likely rose to $3.4\%$ in May  
![](images/737f1fc5bc94169dccf5f28c8cca47f384d1df66af41228e86495ecf84a4374b.jpg)

<details>
<summary>line chart</summary>

| Date    | 3-month annualized | 6-month annualized | y-o-y core PCE inflation |
|---------|--------------------|--------------------|--------------------------|
| Jan-23  | 4.8                | 5.0                | 5.0                      |
| Jul-23  | 2.0                | 3.0                | 4.0                      |
| Jan-24  | 4.8                | 3.5                | 3.0                      |
| Jul-24  | 2.0                | 3.5                | 2.8                      |
| Jan-25  | 3.8                | 3.0                | 3.0                      |
| Jul-25  | 2.5                | 3.0                | 2.8                      |
| Jan-26  | 4.8                | 4.0                | 3.5                      |
| forecast| forecast           | forecast           | forecast                 |
</details>

Source: BEA, Haver, NOM

Core CPI inflation moderated to $0.208\%$ m-o-m from $0.376\%$ in April. Core CPI goods inflation turned negative for the first time since May 2025. The tariff impact appears to have continued to wane, while inflationary pressures from global shortages of semiconductors on consumer electronics diminished. We expect core PCE goods inflation also turned negative in May. By contrast, Core CPI service inflation remained resilient. Rent-related components remained elevated, and supercore CPI components continued to increase at a decent pace. Transportation service prices (e.g., airline fares and auto insurance prices) were volatile.

Compared with our expectations, PCE-relevant PPI data were mixed, as the strength in portfolio management and investment advice prices was partially offset by an unexpected decline in domestic airline fares. CPI and PPI data suggest that supercore PCE inflation likely accelerated to 0.5% m-o-m, the highest since January 2026. Backward revisions to PPI data suggest that January core PCE inflation will likely be revised up, while March and April core PCE inflation will likely be revised down.

Details of PPI data for manufacturers' production costs and selling prices indicate upward pressure on core goods inflation in the coming months. Production costs for US manufacturers kept growing as PPI's processed materials and components for manufacturing continued to increase, in line with the recent increase in factory surveys' prices paid indices (Fig. 7).

Despite the softness in core CPI goods prices, manufacturers continued to pass higher hosts on to their consumers, as PPI for finished consumer goods excluding food and energy increased in May (Fig. 8). Regional manufacturing surveys' prices received indices also point to pass-through of higher costs into consumer product prices.

Fig. 7: Recent business surveys' show firming of prices  
Manufacturing prices paid index vs. PPI's input costs for manufacturing  
![](images/4660a5f7e3d333188f1e1b64a370b63c4285c30deb55644ed902035f4c153934.jpg)

<details>
<summary>line chart</summary>

| Date   | ISM mfg prices paid index (LHS) | S&P: US Mfg PMI: Prices paid index (LHS) | PPI: processed materials and components prices for manufacturing (RHS) |
|--------|----------------------------------|---------------------------------------------|---------------------------------------------------------------|
| Jan-18 | 75                               | 65                                          | 60                                                            |
| May-19 | 50                               | 45                                          | 55                                                            |
| Sep-20 | 90                               | 85                                          | 100                                                           |
| Jan-22 | 85                               | 80                                          | 70                                                            |
| May-23 | 40                               | 35                                          | 45                                                            |
| Sep-24 | 65                               | 60                                          | 65                                                            |
| Jan-26 | 80                               | 75                                          | 70                                                            |
</details>

Source: BLS, ISM, S&P, Haver, NOM

Fig. 8: PPI's finished consumer goods prices excluding food and energy continued to increase in May, suggesting pass-through of higher costs into consumer goods prices  
![](images/eee6d3b6d5b56c2e1cb19aade2bc8422042903f1a27dbdffa784e74cb68296ba.jpg)

<details>
<summary>line chart</summary>

| Date    | PPI: Finished Consumer Goods Less Foods & Energy (LHS) | CPI's core goods prices excluding used vehicle prices (LHS) | GDP-weighted prices received index from regional Fed factory surveys (RHS) |
|---------|--------------------------------------------------------|---------------------------------

[中间内容因长度限制已省略]

ansmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Securities International, Inc., US. All rights reserved.
"""
