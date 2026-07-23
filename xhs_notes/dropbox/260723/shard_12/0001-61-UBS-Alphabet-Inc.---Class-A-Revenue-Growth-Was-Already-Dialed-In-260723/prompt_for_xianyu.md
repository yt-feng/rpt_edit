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
# Alphabet Inc. - Class A Revenue Growth Was Already Dialed In

## Key Takeaways

This quarter there were fewer reasons to cheer with Search and Cloud growth roughly in line (vs beats 1Q26) alongside the company flagging two margin drags vs the 2Q26 level: 1) stepped up CapEx intensity for 2026 (which also drives up our 2027 estimate) and 2) ongoing higher hiring needs (with SBC coming in hotter than we anticipated). As such, our gross revenues change marginally for 2027E and 2028E, but our costs go up faster by \~2% and \~3%, respectively. We have been fielding more questions on Google about FCF growth returning to historic levels, and after today's update (where revenue is largely unchanged but costs work higher) we have no clearer answers. In fact we worry that CapEx for 2027 might climb further from here out as input costs rise and Google continues to invest in frontier model training, and that exacerbates potential for downward revisions to organic EPS (ex mark to market on equity investments). Given the near peak multiple and more likely downward vs upward revision to EPS, we think the risk reward skew remains more favorable on AMZN. We reduce our price target by \$21 to \$379 and maintain our Neutral rating.

## Upside Case

Bulls will argue: 1) \$510B backlog (higher than our \$482B projection) will result in some upward movement to cloud estimates (while we maintain are far-above-consensus 2026/2027 estimates); 2) better than expected 2Q26 revenue (\$119.8B vs \$107.0B St) supports improved mid-term ad dollar accretion - especially on YouTube; 3) broader customer base for TPUs than we thought with sales to not just AI labs but also algorithmic trading and capital market firms. Quantitatively, the upside scenario is \$465/share (41% upside potential) - 2-Year revenue CAGR growth of 26%, and 3Q27-2Q28E operating margin of 34%, implying 3Q27-2Q28E EPS of \$16.33, on a 29x P/E multiple.

## Downside Case

Bears will argue: 1) 2026 CapEx guide raised by \$15B to \$195B-\$205B above cons. of \$187B and commentary around 2027 implies higher D&A-related headwinds to EPS; 2) short-term margin compression anticipated as per GOOG mgmt. commentary and means shareholders for now have to discount QOQ margin improvement noted on Cloud; 3) higher employee costs to further add to pressure on EPS. Quantitatively, the downside scenario is \$253/share (24% downside potential) - 2-Year revenue CAGR growth of 15%, and 3Q27-2Q28E operating margin of 30%, implying 3Q27-2Q28E EPS of \$12.06, on a 21x P/E multiple.

## Valuation

We reduce our price target on GOOGL as well as GOOG to \$379 (from \$400 prior) based on 26x (unchanged) our full year ending 2Q28E GAAP diluted EPS of \$14.64 (vs \$15.16 prior). Please note that the EPS shown on the front cover is UBS-adjusted EPS and differs from the company's disclosed GAAP diluted EPS.

## Equities

<table><tr><td>Americas</td></tr><tr><td>Internet Services</td></tr></table>

12-month rating Neutral

12m price target US\$379.00

Price (22 Jul 2026) US\$342.09

RIC: GOOGL.O BBG: GOOGL US  
Trading data and key metrics

<table><tr><td>52-wk range</td><td>US$402.62-189.13</td></tr><tr><td>Market cap.</td><td>US$4,211b</td></tr><tr><td>Shares o/s</td><td>12,309m (COM)</td></tr><tr><td>Free float</td><td>100%</td></tr><tr><td>Avg. daily volume (&#x27;000)</td><td>32,132</td></tr><tr><td>Avg. daily value (m)</td><td>US$11,771.1</td></tr><tr><td>Common s/h equity (12/26E)</td><td>US$740b</td></tr><tr><td>P/BV (12/26E)</td><td>5.6x</td></tr><tr><td>Net debt to EBITDA (12/26E)</td><td>NM</td></tr></table>

EPS (UBS, diluted) (USD)

<table><tr><td rowspan="2"></td><td colspan="4">12/26E</td></tr><tr><td>From</td><td>To</td><td>% ch</td><td>Cons.</td></tr><tr><td>Q1</td><td>5.11</td><td>5.11</td><td>0</td><td>5.11</td></tr><tr><td>Q2</td><td>6.45</td><td>9.11</td><td>41</td><td>2.89</td></tr><tr><td>Q3E</td><td>2.78</td><td>2.68</td><td>-4</td><td>3.02</td></tr><tr><td>Q4E</td><td>4.40</td><td>4.09</td><td>-7</td><td>3.33</td></tr><tr><td>12/26E</td><td>18.73</td><td>20.99</td><td>12</td><td>14.23</td></tr><tr><td>12/27E</td><td>17.67</td><td>17.21</td><td>-3</td><td>14.67</td></tr><tr><td>12/28E</td><td>14.08</td><td>13.52</td><td>-4</td><td>17.30</td></tr></table>

Stephen Ju
Analyst
stephen.ju@ubs.com
+1-212-882 5192

Esha Vaish
Analyst
esha.vaish@ubs.com
+1-212-713 3328

<table><tr><td>Highlights (US$m)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>Revenues</td><td>307,394</td><td>350,018</td><td>402,836</td><td>519,818</td><td>668,945</td><td>660,514</td><td>736,635</td><td>801,402</td></tr><tr><td>EBIT (UBS)</td><td>84,293</td><td>112,390</td><td>129,039</td><td>177,663</td><td>252,457</td><td>200,540</td><td>228,383</td><td>234,355</td></tr><tr><td>Net earnings (UBS)</td><td>73,795</td><td>100,118</td><td>132,170</td><td>258,534</td><td>214,512</td><td>169,457</td><td>191,151</td><td>195,415</td></tr><tr><td>EPS (UBS, diluted) (US$)</td><td>5.80</td><td>8.04</td><td>10.81</td><td>20.99</td><td>17.21</td><td>13.52</td><td>15.18</td><td>15.46</td></tr><tr><td>DPS (net) (US$)</td><td>0.00</td><td>0.60</td><td>0.83</td><td>0.88</td><td>0.88</td><td>0.88</td><td>0.88</td><td>0.88</td></tr><tr><td>Net (debt) / cash</td><td>97,663</td><td>84,774</td><td>80,296</td><td>148,353</td><td>143,277</td><td>57,084</td><td>15,133</td><td>3,063</td></tr></table>

<table><tr><td>Profitability/valuation</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>EBIT (UBS) margin %</td><td>27.4</td><td>32.1</td><td>32.0</td><td>34.2</td><td>37.7</td><td>30.4</td><td>31.0</td><td>29.2</td></tr><tr><td>ROIC (EBIT) %</td><td>59.9</td><td>63.0</td><td>55.1</td><td>48.9</td><td>41.9</td><td>22.7</td><td>19.8</td><td>16.8</td></tr><tr><td>EV/EBITDA (UBS core) x</td><td>14.6</td><td>15.0</td><td>16.2</td><td>18.9</td><td>12.7</td><td>13.9</td><td>11.6</td><td>10.4</td></tr><tr><td>P/E (UBS, diluted) x</td><td>20.5</td><td>20.4</td><td>19.5</td><td>16.3</td><td>19.9</td><td>25.3</td><td>22.5</td><td>22.1</td></tr><tr><td>Equity FCF (UBS) yield %</td><td>4.5</td><td>3.6</td><td>2.8</td><td>0.3</td><td>(0.6)</td><td>(1.6)</td><td>(0.6)</td><td>0.4</td></tr><tr><td>Dividend yield (net) %</td><td>0.0</td><td>0.4</td><td>0.4</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td></tr></table>

Source: Company accounts, LSEG Eikon, UBS estimates. Metrics marked as (UBS) have had analyst adjustments applied. Valuations: based on an average share price that year, (E): based on a share price of US\$ 342.09 on 22-Jul-2026

## Investment Case: Revenue Growth Was Already Dialed In

2Q26 gross revenue was \$119.8B versus UBSe \$119.5B and consensus of \$116.5B. 2Q26 GAAP diluted EPS was \$9.11 versus UBSe \$6.45 and consensus \$2.88. We do note that EPS was helped by an increase in unrealized gain related to equity securities, which we think partially relates to SpaceX's IPO and partially to Anthropic's post 1Q26 raise and revaluation. As we flow through the reported results and make changes to our estimates, our GAAP diluted EPS for 2026E, 2027E, and 2028E are now \$21.00, \$17.22 and \$13.52 versus prior \$18.74, \$17.68, and \$14.08, respectively. Our price target is now \$379 versus \$400 prior.

The biggest topic in our conversations with investors remains Cloud. In that area, Google reported better-than-expected Cloud backlog, which hit about \$510B as of 2Q26 close vs \~\$462B at 1Q26 close. For context, we were modeling \$482B in backlog for 2Q26. At 50% on average converting to revenue in two years, Google is putting forth the case for shareholders to underwrite for 2026E / 2027E Google Cloud Platform revenues of \$127.5B, or Cloud all in revenues of \~\$147B (assuming steady state dollar addition to Workspace and other non-backlog linked cloud revenues). This is squarely above pre-earnings consensus of \~\$95B for 2026 and \~\$144B or 2027. However, we had revised our Cloud growth rates alongside our June note "Stacking the Backlog from the AI Labs, Meta, and Vertex" and were sitting materially above consensus. As such, this update more so alters our QOQ revenue growth rates for cloud rather than changing our overall expectations. We now model Cloud revenues for 2026, 2027, and 2028 of \$127.8B, \$232.2B, and \$178.7B versus prior \$126.1B, \$232.0B, and \$181.1B, respectively.

For Search, Google posted YOY reported growth of 17% - beating consensus of 16% - but the magnitude of beat was more modest compared to previous quarters. Google noted that Search saw retail and finance vertical strength, which were the biggest contributors. We were not surprised as our ad checks also implied for outperformance on 2Q26 results, and given upward revisions we made to our Search estimates post 1Q26 print and heading into 2Q26 earnings, this print leaves little room for upward revisions. Our Search revenue estimates for 2026, 2027, and 2028 are marginally changed at \$259.6B, \$293.8B, and \$330.6B versus prior \$259.8B, \$293.7B, and \$330.3B, respectively.

YouTube came in above expectations with reported revenue of \$11.1B versus consensus \$10.8B, with benefits from the soccer world cup and related brand as well as in living room spending on clickable ads. We flag for investors that the world cup benefits will also hit 3Q26 (given that the latter matches, including the final, happened in July) and note that US mid-term elections related spend is likely to benefit 2H26. Our ad checks have noted that political spend levels are matching the 2024 Presidential Election, and thus we give YouTube more credit than for historical midterm elections. Our YouTube revenue forecasts for 2026, 2027, and 2028 are now at \$44.8B, \$48.5B, and \$52.9B versus prior \$43.8B, \$47.8B, and \$52.2B, respectively.

On the cost side, Google guided CapEx at \$195B-\$205B versus \$180B-\$190B earlier and compared to consensus at \$186.5B and UBSe at \$196.2B. We also raise our 2028 CapEx on the back of this disclosure, recognizing that input costs are higher than we have anticipated and perhaps spend intensity to generate incremental dollar of Cloud revenue is higher in this cycle than in past ones. The related D&A flowthrough does take up our total expense estimates. We also note that while 2Q26 Cloud margins were higher than anticipated, a QOQ ramp in TPU sales to AI labs, capital markets and algorithmic trading firms. Google management also noted ongoing hiring needs, which we account for in our compensation and SBC estimates. As a result, our 2026, 2027, and 2028 total expenses move to \$342.2B, \$416.5B, and \$460.0B versus prior \$338.9B, \$410.3B, and \$456.0B, respectively.

Net/net, our 2026, 2027 and 2028 GAAP diluted EPS estimates are now \$21.00, \$17.22 and \$13.52 versus prior \$18.74, \$17.68, and \$14.08, respectively. Applying an increased P/E multiple of 26x (unchanged) to our 3Q27-2Q28E GAAP diluted EPS, our PT moves to \$379 from \$400.

We keep our Neutral rating as there are wide potential impacts to Google's businesses from competition and other factors. Our investment thesis remains based on the

## following factors:

\- ROIC from incremental investments into AI driven products as well as monetization path for AI Overviews still remains to be determined. Although Google claims that AI Overviews is monetizing at the same rate as regular search, feedback from our ad checks has been mixed, which suggests that greater proliferation and what may be benefits to both query volume and CPCs remain unresolved. Conceptually, we continue to look for telltale signs from advertisers that ROAS is improving.

\- Unresolved if not intensifying competition risk from GenAI search products, including a potential Meta AI search product, as well as threat of share loss to GenAI challengers Perplexity and OpenAI, whose ChatGPT product now has a chatbot integrations with merchant supply (Shopify, Etsy, Booking, Expedia, among some of the recent announcements).

\- Potential for short-term escalation in costs and investments related to GenAI build, with Google likely to spend incrementally more in 2026E on engineering headcount/personnel expenses.

## Estimate Changes

Changes to our estimates for 3Q26, 4Q26, 2026, 2027 and 2028 financial and operating metrics are as summarized below:

Figure 1: Alphabet Inc. - Summary Changes

<table><tr><td>Figures in $M, Except Per Share Amounts</td><td>3Q26 Prior</td><td>3Q26 Current</td><td>% Δ</td><td>4Q26 Prior</td><td>4Q26 Current</td><td>% Δ</td><td>2026 Prior</td><td>2026 Current</td><td>% Δ</td><td>2027 Prior</td><td>2027 Current</td><td>% Δ</td><td>2028 Prior</td><td>2028 Current</td><td>% Δ</td></tr><tr><td>Google Search and Other</td><td>64,870</td><td>64,870</td><td>0.0%</td><td>71,100</td><td>71,100</td><td>0.0%</td><td>259,762</td><td>259,640</td><td>0.0%</td><td>293,694</td><td>293,820</td><td>0.0%</td><td>330,332</td><td>330,604</td><td>0.1%</td></tr><tr><td>YouTube Ads</td><td>11,008</td><td>11,275</td><td>2.4%</td><td>12,260</td><td>12,584</td><td>2.6%</td><td>43,798</td><td>44,797</td><td>2.3%</td><td>47,769</td><td>48,493</td><td>1.5%</td><td>52,161</td><td>52,940</td><td>1.5%</td></tr><tr><td>Google Properties</td><td>75,878</td><td>76,145</td><td>0.4%</td><td>83,360</td><td>83,683</td><td>0.4%</td><td>303,560</td><td>304,437</td><td>0.3%</td><td>341,463</td><td>342,312</td><td>0.2%</td><td>382,493</td><td>383,544</td><td>0.3%</td></tr><tr><td>Google Network Members&#x27; Properties</td><td>6,735</td><td>6,705</td><td>-0.4%</td><td>8,026</td><td>8,026</td><td>0.0%</td><td>28,536</td><td>29,005</td><td>1.6%</td><td>28,718</td><td>29,189</td><td>1.6%</td><td>29,133</td><td>29,613</td><td>1.6%</td></tr><tr><td>Google Cloud</td><td>26,888</td><td>32,733</td><td>21.7%</td><td>55,119</td><td>50,282</td><td>-8.8%</td><td>126,129</td><td>127,811</td><td>1.3%</td><td>231,964</td><td>233,220</td><td>0.5%</td><td>181,073</td><td>178,668</td><td>-1.3%</td></tr><tr><td>Google Other</td><td>15,370</td><td>15,370</td><td>0.0%</td><td>16,447</td><td>16,447</td><td>0.0%</td><td>58,397</td><td>57,112</td><td>-2.2%</td><td>64,136</td><td>62,646</td><td>-2.3%</td><td>68,719</td><td>67,049</td><td>-2.4%</td></tr><tr><td>Other Bets</td><td>354</td><td>354</td><td>0.0%</td><td>381</td><td>381</td><td>0.0%</td><td>1,530</td><td>1,528</td><td>-0.1%</td><td>1,579</td><td>1,576</td><td>-0.1%</td><td>1,641</td><td>1,638</td><td>-0.1%</td></tr><tr><td>Gross Revenue</td><td>125,225</td><td>131,307</td><td>4.9%</td><td>163,333</td><td>158,818</td><td>-2.8%</td><td>517,972</td><td>519,818</td><td>0.4%</td><td>667,859</td><td>668,945</td><td>0.2%</td><td>663,058</td><td>660,514</td><td>-0.4%</td></tr><tr><td>Traffic Acquisition Costs</td><td>16,237</td><td>16,261</td><td>0.2%</td><td>18,371</td><td>18,418</td><td>0.3%</td><td>66,143</td><td>66,086</td><td>-0.1%</td><td>73,101</td><td>72,973</td><td>-0.2%</td><td>80,913</td><td>80,746</td><td>-0.2%</td></tr><tr><td>Net Revenue</td><td>108,988</td><td>115,046</td><td>5.6%</td><td>144,962</td><td>140,400</td><td>-3.1%</td><td>451,829</td><td>453,732</td><td>0.4%</td><td>594,758</td><td>595,972</td><td>0.2%</td><td>582,145</td><td>579,768</td><td>-0.4%</td></tr><tr><td>GAAP Operating Income</td><td>39,696</td><td>38,084</td><td>-4.1%</td><td>63,592</td><td>59,112</td><td>-7.0%</td><td>179,078</td><td>177,663</td><td>-0.8%</td><td>257,523</td><td>252,457</td><td>-2.0%</td><td>207,028</td><td>200,540</td><td>-3.1%</td></tr><tr><td>Total Expenses</td><td>85,529</td><td>93,223</td><td>9.0%</td><td>99,740</td><td>99,706</td><td>0.0%</td><td>338,894</td><td>342,155</td><td>1.0%</td><td>410,336</td><td>416,487</td><td>1.5%</td><td>456,030</t

[中间内容因长度限制已省略]

d not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/4eff7b6f38d2dcb23a74f1010ad5c9cb80632cf791d8333f118eddca1e1b0728.jpg)
"""
