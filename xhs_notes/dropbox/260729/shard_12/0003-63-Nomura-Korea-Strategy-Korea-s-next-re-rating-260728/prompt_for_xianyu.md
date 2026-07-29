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
EQUITY: EQUITY STRATEGY

## Korea's next re-rating

## From liquidity and leverage rally to fundamental recalibration

## Corporate buybacks to become next structural driver

We believe the Korean equity market's correction to 6,691 (24 July 2026) from a peak of 9,115 (22 June 2026) was driven by the following flow factors: (1) heavy selling by foreign investors (KRW158tn; USD108bn) as Korea's benchmark weight exceeded portfolio limits, (2) slowing institutional support as National Pension Service's domestic asset allocation approached practical limits, and (3) rapid growth in leveraged ETFs and newly launched single stock leveraged products creating volatility (Fig. 9). We believe these factors led to amplified volatility despite resilient corporate fundamentals. As market "deleveraging" progresses and foreign selling pressure eases, the next leg of Korea's re-rating is likely to be supported by corporate share buybacks and treasury-share cancellations, particularly from large-cap companies, in our view. We estimate Korea's share buybacks to be KRW116tn/274tn/328tn for 2026F/27F/28F, \~90% of which will likely stem from the two large semiconductor companies (including buybacks for employee bonus and shareholder return). This should become a new structural source of demand and help the KOSPI re-rate toward our 10,000-11,000 target.

## How Korea's ETFs intensified market volatility

Since the launch of the first leveraged ETF in the KOSPI in 2010, the number expanded to \~30/56 in 2020/26. Korea's total ETF market has \~KRW450tn in AUM (source: Bloomberg), of which leveraged ETFs account for KRW27tn (as of 23 July 2026), comprising \~6% of the total ETF market. Due to large leveraged ETF holdings by retail investors (\~85% as per our estimates) and their negative return of 53% since the KOSPI peaked on 22 June (vs the KOSPI's overall decline of 22% during the same period), the South Korean government announced a first round of measures to restrict and tighten investment qualifications in these single leveraged ETF products. In addition, a sharp increase in retail investors' forced liquidations (Fig. 11) relative to outstanding margin receivables triggered an alert signal to the government, in our view.

## Maintain KOSPI target of 10,000-11,000

We maintain our 2026 KOSPI target of 10,000-11,000 based on a 2026F P/E of 10.5-11.5x, P/BV of 2.5-2.8x, and ROE of 27% (currently trading at 2026/27F P/E of 7.0x/5.2x and P/BV of 1.7x/1.3x). We see the following as key catalysts for the KOSPI: 1) AI-driven earnings (including memory/ HBM, power equipment, ESS, and nuclear) to generate sustainable ROE for the next five years; 2) listed companies' shift toward better capital efficiency, shareholder return, and optimal leverage to support higher P/E and PBV; 3) active stewardship or activist campaigns; and 4) government enforcement for better target ROE disclosure and regulatory measures to facilitate non-core asset holdings, stricter listing requirement and governance structure. Downside risks to our view include: 1) corporate stock buyback falling short of our expectations of KRW116tn (2026F); 2) foreign investors' mechanical selling exacerbating once the KOSPI reaches above 7,500-9,000 (without KOSPI earnings or ROE upgrade); and 3) retail investors' rebuilding of steep leverage.

## Korea's equity market and tax reform measures in 2H26F

We believe key policy developments in 2H26F could include tighter regulations of single-stock leveraged ETFs (than what was announced on 16 July), publication of a low-PBR company list, incentives for higher dividends, stricter duplicate-listing rules and KOSDAQ reform. We believe the low-PBR list, expected around November, could become the most direct company-specific catalyst by encouraging treasury-share cancellation, higher dividends and disposal of non-core assets. Meanwhile, we also believe stricter duplicate-

## Research Analysts

Korea Strategy
Cindy Park - NFIK
cindy.park@NOM.com
+822 3783 2324

Dongmin Lee - NFIK
dongmin.lee@NOM.com
+822 3783 2338

Asia Pacific Technology

CW Chung - NIHK
cwchung@NOM.com
+852 2252 6075

YJ Kim, CFA - NFIK
yj.kim1@NOM.com
+82237832332

## Korea Autos & Auto Parts

Angela Hong - NFIK
angela.hong@NOM.com
+822 3783 2360

## Korea Tech/Industrials

Eon Hwang - NFIK
eon.hwang@NOM.com
+822 3783 2318

Production Complete: 2026-07-28 10:48 UTC

Source: Bloomberg Finance L.P., NOM estimates

listing rules and KOSDAQ reforms should improve shareholder protection, reduce parent-company discounts and strengthen overall market quality. Korea's late-July 2026 tax reform proposal, in our view, is likely to include: 1) higher tax incentives for long-term domestic equity investment through ISAs, pension accounts; 2) reforms to the inheritance and gift tax framework aimed at reducing controlling shareholders' incentive to suppress share prices; and 3) enhanced tax credits for AI, semiconductors, and other strategic industries, and regional investment incentives.

Fig. 1: Our Korea stock picks

<table><tr><td>Company</td><td>Code</td><td>Rating</td><td>Mkt cap (USDmn)</td><td>Avg. TO (USDmn)</td><td>Target price</td><td>Price 24-Jul</td><td>Upside (%)</td></tr><tr><td>Samsung Electronics</td><td>005930 KS</td><td>Buy</td><td>994,435</td><td>2,515</td><td>670,000</td><td>249,500</td><td>168.5%</td></tr><tr><td>SEMCO</td><td>009150 KS</td><td>Buy</td><td>67,524</td><td>135</td><td>2,500,000</td><td>1,326,000</td><td>88.5%</td></tr><tr><td>Kia Corp</td><td>000270 KS</td><td>Buy</td><td>34,734</td><td>136</td><td>250,000</td><td>130,500</td><td>91.6%</td></tr><tr><td>Celltrion</td><td>068270 KS</td><td>Buy</td><td>28,157</td><td>102</td><td>270,000</td><td>177,600</td><td>52.0%</td></tr><tr><td>Samsung SDI</td><td>006400 KS</td><td>Buy</td><td>23,514</td><td>193</td><td>900,000</td><td>428,000</td><td>110.3%</td></tr><tr><td>Hyundai Rotem</td><td>064350 KS</td><td>Buy</td><td>11,786</td><td>117</td><td>310,000</td><td>158,400</td><td>95.7%</td></tr><tr><td>NC</td><td>036570 KS</td><td>Buy</td><td>3,349</td><td>23</td><td>310,000</td><td>228,000</td><td>36.0%</td></tr></table>

Note: Pricing as of 24 July close

## Korea's next re-rating: from liquidity and leverage rally to fundamental recalibration

From a flow perspective, the Korean equity market's correction to 6,691 (24 July 2026) from a peak of 9,115 (22 June 2026 close) was largely due to: 1) a large amount of foreign selling of KRW158tn year-to-date, (2) a rapid increase in leveraged ETF investments and the introduction of single-stock leveraged products (16/3 newly launched in Korea/Hong Kong at end-May 2026/May 2025) steepening market volatility; and (3) institutional flow becoming less supportive due to asset allocation rebalancing by pension funds (Korea's National Pension Service has steadily increased its domestic equity allocation from $14.9\%$ to $20.8\%$ , but has also reached limits in overall fund allocation). The KOSPI's volatility index hit all-time high of 96.9 on 29 June 2026.

As most foreign institutional investors operate under portfolio risk-management rules, they are forced to reduce exposure when an individual stock weighting exceeds a position limit (e.g., 10% of a fund) or Korea's weighting in global benchmarks such as MSCI rises beyond target allocations. In retrospect, this mechanical selling intensified when the KOSPI reached 7,500/9,000 in mid-May/end-June (Fig. 6) and to a less extent in Feb-March when the KOSPI reached \~6,000.

## Corporate share buybacks to re-rate the KOSPI

We believe as market “deleveraging” progresses (discussed further in The ongoing deleveraging may be a “re-setting” process) and foreign selling pressure eases, the next leg of Korea's re-rating is likely to be supported by corporate share buybacks and treasury-share cancellations, particularly from large-cap companies. We estimate Korea’s buybacks to be KRW116tn/274tn/328tn for 2026F/27F/28F, \~90% of which will likely stem from the two large semiconductor companies (including buyback for employee bonus and shareholder return). This should become a new structural source of demand and help the KOSPI re-rate toward our 10,000–11,000 target (Korea Strategy - New KOSPI target of 10,000-11,000, 20 May 2026), in our view.

Fig. 2: KOSPI equity market investor flow by investor type and forecast  
![](images/40d81d0f3b38a305cdfe39b85761aff9cf871b25093a9d2d4a844a7d7b4714bf.jpg)  
Source: KRX, NOM

Fig. 3: KOSPI: quarterly share buyback forecasts

<table><tr><td>(KRWtn)</td><td>1Q26</td><td>2Q26</td><td>3Q26F</td><td>4Q26F</td><td>2026F</td><td>1Q27F</td><td>2Q27F</td><td>3Q27F</td><td>4Q27F</td><td>2027F</td><td>1Q28F</td><td>2Q28F</td><td>3Q28F</td><td>4Q28F</td><td>2028F</td></tr><tr><td>KOSPI buyback (total)</td><td>12</td><td>8</td><td>42</td><td>54</td><td>116</td><td>56</td><td>45</td><td>74</td><td>100</td><td>274</td><td>101</td><td>75</td><td>66</td><td>87</td><td>328</td></tr><tr><td>Memory &quot;big 2&quot;</td><td>8</td><td>5</td><td>39</td><td>51</td><td>103</td><td>50</td><td>39</td><td>68</td><td>94</td><td>251</td><td>97</td><td>71</td><td>62</td><td>83</td><td>314</td></tr><tr><td>Shareholder return</td><td>0</td><td>0</td><td>23</td><td>35</td><td>58</td><td>35</td><td>23</td><td>52</td><td>78</td><td>189</td><td>78</td><td>52</td><td>43</td><td>65</td><td>239</td></tr><tr><td>Employee bonus</td><td>8</td><td>5</td><td>16</td><td>16</td><td>45</td><td>15</td><td>15</td><td>15</td><td>15</td><td>61</td><td>19</td><td>19</td><td>19</td><td>19</td><td>75</td></tr><tr><td>Other companies</td><td>4</td><td>3</td><td>3</td><td>3</td><td>13</td><td>6</td><td>6</td><td>6</td><td>6</td><td>23</td><td>4</td><td>4</td><td>4</td><td>4</td><td>15</td></tr></table>

Note: SEC announced that its 2024-26 shareholder return budget will be 50% of three years' combined FCF. Out of the budget, we assume that remaining amount after paying out cash dividends will be spent for share buyback.
Source: Company data, NOM estimates

Fig. 4: KOSPI: annual share buyback forecasts

<table><tr><td>(KRWtn)</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026F</td><td>2027F</td><td>2028F</td></tr><tr><td>KOSPI share buyback</td><td>6</td><td>4</td><td>6</td><td>4</td><td>5</td><td>7</td><td>17</td><td>19</td><td>116</td><td>274</td><td>328</td></tr><tr><td>% of KOSPI mkt cap</td><td>0.4%</td><td>0.3%</td><td>0.3%</td><td>0.2%</td><td>0.3%</td><td>0.3%</td><td>0.9%</td><td>0.6%</td><td>2.2%</td><td>-</td><td>-</td></tr><tr><td>Share buyback excl. memory</td><td>3</td><td>4</td><td>6</td><td>4</td><td>5</td><td>7</td><td>15</td><td>11</td><td>13</td><td>23</td><td>15</td></tr><tr><td>KOSPI Net profit</td><td>128</td><td>71</td><td>85</td><td>191</td><td>160</td><td>107</td><td>169</td><td>217</td><td>853</td><td>1,156</td><td>1,263</td></tr><tr><td>Buyback ratio (%)</td><td>4.5%</td><td>5.4%</td><td>6.7%</td><td>2.0%</td><td>3.0%</td><td>6.1%</td><td>9.8%</td><td>8.8%</td><td>13.5%</td><td>23.7%</td><td>26.0%</td></tr><tr><td>Net profit excl. memory</td><td>69</td><td>47</td><td>54</td><td>142</td><td>103</td><td>102</td><td>115</td><td>130</td><td>258</td><td>270</td><td>200</td></tr><tr><td>Buyback ratio (%)</td><td>4.6%</td><td>8.1%</td><td>10.5%</td><td>2.7%</td><td>4.6%</td><td>6.4%</td><td>12.7%</td><td>8.4%</td><td>4.9%</td><td>8.7%</td><td>7.3%</td></tr></table>

Note: Market cap data as of end of year (24 July close for 2026)
Source: KRX, NOM estimates

Fig. 5: Korea market weighting in MSCI EM  
![](images/6d05c60dc4dd53a820cabc5cf01c76957f82d4decd88fe60f011f4802fec4215.jpg)  
Source: Bloomberg Finance L.P., LSEG, NOM

Fig. 6: Foreign monthly net buy and sell vs KOSPI  
![](images/e78f9704dca51c9617b1d179c0adef37cc3f552b042f939056c0505fbd0f9223.jpg)  
Source: Quantiwise, NOM

Fig. 7: Foreign investors' net buying of Asian/EM equities

<table><tr><td colspan="13">Weekly foreign equity flows (except stated otherwise); data in USD mn</td><td colspan="9">ETF flows</td><td colspan="3"></td></tr><tr><td>Week Ending</td><td>India (Total)</td><td>India (Scndry.)</td><td>Indo</td><td>Korea</td><td>Phils.</td><td>Taiwan</td><td>Thailand</td><td>Malaysia</td><td>Shanghai (SB)</td><td>Shenzhen (SB)</td><td>EM Asia ex CH</td><td>Japan</td><td>China A onshore ETFs</td><td>US listed China ETFs</td><td>China Tech-related US/HK</td><td>EM ETF</td><td>Bitcoin ETFs</td><td>EM ex China ETFs</td><td>India offshore ETFs</td><td>Korea offshore ETFs</td><td>Korea onshore domestic ETFs</td><td>Korea onshore Int. ETFs</td><td>TW onshore ETFs</td><td></td></tr><tr><td>02-Jan-26</td><td>(1,464)</td><td>(1,478)</td><td>124</td><td>(317)</td><td>4</td><td>1,038</td><td>(21)</td><td>(115)</td><td>185</td><td>(675)</td><td>(749)</td><td>(96)</td><td>(1,684)</td><td>(14)</td><td>(432)</td><td>433</td><td>(1,106)</td><td>129</td><td>27</td><td>136</td><td>789</td><td>309</td><td>(458)</td><td></td></tr><tr><td>09-Jan-26</td><td>(946)</td><td>(950)</td><td>121</td><td>464</td><td>36</td><td>(864)</td><td>(153)</td><td>88</td><td>1,537</td><td>2,662</td><td>(1,254)</td><td>7,757</td><td>(229)</td><td>125</td><td>2,674</td><td>3,206</td><td>(655)</td><td>331</td><td>(30)</td><td>419</td><td>(237)</td><td>1,497</td><td>(439)</td><td></td></tr><tr><td>16-Jan-26</td><td>(1,283)</td><td>(1,341)</td><td>249</td><td>(306)</td><td>51</td><td>2,063</td><td>241</td><td>233</td><td>916</td><td>372</td><td>1,248</td><td>4,936</td><td>(28,882)</td><td>177</td><td>(422)</td><td>5,163</td><td>2,457</td><td>171</td><td>(23)</td><td>689</td><td>1,256</td><td>684</td><td>(860)</td><td></td></tr><tr><td>23-Jan-26</td><td>(1,066)</td><td>(1,126)</td><td>(192)</td><td>813</td><td>4</td><td>(522)</td><td>44</td><td>136</td><td>2,115</td><td>902</td><td>(783)</td><td>1,234</td><td>(54,597)</td><td>(2)</td><td>281</td><td>4,173</td><td>(1,861)</td><td>55</td><td>23</td><td>533</td><td>1,241</td><td>783</td><td>(320)</td><td></td></tr><tr><td>30-Jan-26</td><td>301</td><td>109</td><td>(831)</td><td>(1,037)</td><td>127</td><td>561</td><td>9</td><td>36</td><td>(247)</td><td>593</td><td>(834)</td><td>1,033</td><td>(54,223)</td><td>(40)</td><td>(1,247)</td><td>5,015</td><td>(2,435)</td><td>587</td><td>50</td><td>679</td><td>2,724</td><td>1,811</td><td>(453)</td><td></td></tr><tr><td>06-Feb-26</td><td>1,078</td><td>1,043</td><td>(68)</td><td>(7,502)</td><td>23</td><td>(3,306)</td><td>332</td><td>102</td><td>4,026</td><td>3,150</td><td>(9,341)</td><td>1,747</td><td>(1,810)</td><td>(33)</td><td>906</td><td>784</td><td>(433)</td><td>41</td><td>310</td><td>217</td><td>4,899</td><td>(387)</td><td>618</td><td></td></tr><tr><td>13-Feb-26</td><td>216</td><td>(48)</td><td>(326)</td><td>2,221</td><td>23</td><td>6,467</td><td>1,013</td><td>151</td><td>2,356</td><td>1,201</td><td>9,765</td><td>8,070</td><td>(3,747)</td><td>(343)</td><td>(1,449)</td><td>3,296</td><td>(595)</td><td>657</td><td>284</td><td>1,039</td><td>3,286</td><td>294</td><td>(16)</td><td></td></tr><tr><td>20-Feb-26</td><td>340</td><td>344</td><td>123</td><td>(715)</td><td>11</td><td>0</td><td>354</td><td>(7)</td><td>0</td><td>0</td><td>105</td><td>3,500</td><td>0</td><td>(99)</td><td>271</td><td>1,179</td><td>(619)</td><td>32</td><td>89</td><td>812</td><td>(252)</td><td>(867)</td><td>0</td><td></td></tr><tr><td>27-Feb-26</td><td>54</td><td>(108)</td><td>292</td><td>(7,693)</td><td>88</td><td>4,837</td><td>45</td><td>(29)</td><td>111</td><td>746</td><td>(2,406)</td><td>5,069</td><td>(3,887)</td><td>(141)</td><td>(222)</td><td>4,385</td><td>1,290</td><td>795</td><td>118</td><td>1,501</td><td>1,142</td><td>727</td><td>(444)</td><td></td></tr><tr><td>06-Mar-26</td><td>(2,381)</td><td>(2,414)</td><td>131</td><td>(3,212)</td><td>(16)</td><td>(8,891)</td><td>(424)</td><td>96</td><td>(1,014)</td><t

[中间内容因长度限制已省略]

rofessional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM Financial Investment (Korea) Co., Ltd., Korea. All rights reserved.
"""
