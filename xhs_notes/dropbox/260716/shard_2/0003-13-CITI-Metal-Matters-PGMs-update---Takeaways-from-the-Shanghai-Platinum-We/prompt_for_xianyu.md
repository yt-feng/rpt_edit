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
# Metal Matters

## PGMs update – Takeaways from the Shanghai Platinum Week

## CITI'S TAKE

We keep our 0-3m point price targets unchanged at \$1,950/oz for platinum (vs \~\$1,640/oz spot) and at \$1,500/oz for palladium (vs \~\$1,300/oz spot). We expect PGM trading to continue to track gold with high beta, dominated by investment demand (see Figure 1). Strait of Hormuz (SoH) reescalation and Fed hawkishness remain near-term downside risks, but we expect PGM prices to recover as easing inflation relieves the pressure on the Fed to hike rates, which will lead to an eventual rebound in investor sentiment.

PGMs outperformed gold in 2025 after consecutive years of underperformance attracted bargain hunters seeking catchup trades to gold. Bullish PGM headlines throughout the year, including China jewelry restocking, Critical Minerals S232 investigations, GFEX PGM futures listing, EU pushback on ICE vehicle ban, etc., also helped PGM prices. In contrast, PGM fundamentals have been relatively quiet YTD in 2026, and in turn PGM trading has been largely tracking gold with high beta.

Investment demand has been the single most important driver of the epic rally, which saw platinum prices jumping from sub-1K in May 2025 to \~\$2,800/oz in Jan 2026 then down to \~\$1,600/oz. Despite bigger autocatalyst exposure and less investment demand, palladium largely followed platinum in direction while lagging in performance. As is the case with gold, PGM prices faced macro headwinds of strong US\$ and higher real rates since the start of the US-Iran war (see Figure 3). We expect easing inflation to relieve the pressure on the Fed to hike and lead to a rebound in investment demand on PGMs. A major SoH reescalation and Fed staying hawkish remain the top downside risks for precious metal prices.

Conversations with onshore market participants at the Shanghai Platinum Week last week suggest broad weakness in China platinum jewelry and investment demand. China jewelry restocking was an early trigger of the 2025 bull market, but end-use consumption has failed to gain traction as 1) platinum jewelry remains less competitive than gold, and 2) jewelry demand has been losing out to bar & coin investment (for both gold and platinum). Chinese retail investors have shown strong tendency to follow trends, i.e. buying on the way up and fading when the rally stops. We expect this pattern to continue, with investors staying put for now amid weak price action and returning to the market when prices eventually rebound. This can help fuel the rally (like CTAs do), though the buying ahead is likely weaker than in the prior rally as many investors are still underwater after the recent selloff.

AI-related demand for PGMs was highlighted as a green shoot amid weak outlook for traditional sectors (e.g. autocatalyst). Some event participants presented very positive outlook through the 2030s, though it's hard to quantify AI demand in our view as the applications are still in early stage of development. We see demand gains in AI-related chemical, electrical and glass sectors partially offsetting the structural decline in autocatalyst demand for platinum this year and next, but the scale of longer-term growth remains less clear for now. While AI demand themes could draw investor attention and boost actual demand when the applications become mature, this is a longer-term theme, and we still expect macro and geopolitical factors (e.g. SoH and the Fed) to dominate PGM trading over the coming months.

Kenny Hu, CFA $^{AC}$ +65-6657-3873
kenny.x.hu@citi.com

Maximilian J Layton $^{AC}$ +44-20-7986-4556
max.layton@citi.com

Viswanathrao Kintali $^{AC}$ +44-20-7986-4982
viswanathrao.kintali@citi.com

Wenyu Yao $^{AC}$ +44-20-7986-4551
wenyu.yao@citi.com

Tom Mulqueen $^{AC}$ +44-20-7986-4559
tom.mulqueen@citi.com

Shreyas Madabushi $^{AC}$ +91-22-4277-5048
shreyas.madabushi@citi.com

Ephrem Ravi
+44-20-7986-2462
ephrem.ravi@citi.com

Jack Shang, CFA
+852-2501-2441
jack.shang@citi.com

## Alexander Hacking, CFA

+1-212-816-6232
alex.hacking@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations.

Figure 1. ETF holdings (moz) - heavy ETF liquidations YTD have weighed on PGM prices  
![](images/18bd5f6656bcda28bd2ac71fbaa3c185a728b295f5911e7bc4d5bba94ae15ae6.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Bloomberg

Figure 2. CFTC net managed money positioning (moz) – funds moderated longs on platinum and turned net short again on palladium  
![](images/1c896eb8e24aa3f19acabda2f2b657c43673bd724e4dd60d49f5fe233f9f083e.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Bloomberg, CFTC

Figure 3. PGM prices have seen strong negative correlation to US\$/real rates since the start of the US-Iran war  
![](images/a3f2fa36b6c52ab4763a4d17177c5d47cab9f40fe1f0c87ab460a2386bb2c603.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Bloomberg

![](images/44dd8dc6ec1713b1d28ea29a6539db0e4a5696d06985962f47945d3013ae1bb4.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 4. Normalizing lease rates suggest easing physical market tightness  
![](images/b8f43c4f306ae91bbc011acda654839ae0950e6faea36af2969f9665fdb40143.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, Bloomberg

Figure 5. Nymex platinum inventory dropped significantly amid lower tariff risks  
![](images/acb35176def99293fa71b01dbc2d2f4dd1195e8544420ae0fd9d50346acde6cd.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Bloomberg

Figure 6. EFP markets implying much lower tariff chances - our base case (since Jan 2026) has been no S232 tariffs on PGMs  
![](images/2e4a77786dba5bb2e31481c1e42adb692e1e2309e90d778776a83b5a06cbfe44.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Bloomberg

Figure 7. Global platinum S&D balances

<table><tr><td>Pt koz</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Autocatalyst</td><td>2,466</td><td>2,766</td><td>3,204</td><td>3,108</td><td>3,031</td><td>2,948</td><td>2,764</td><td>2,668</td></tr><tr><td>Other Industrial:</td><td>2,474</td><td>2,288</td><td>2,491</td><td>2,526</td><td>2,049</td><td>2,228</td><td>2,380</td><td>2,447</td></tr><tr><td>Chemical</td><td>622</td><td>690</td><td>829</td><td>631</td><td>578</td><td>604</td><td>681</td><td>616</td></tr><tr><td>Electrical</td><td>135</td><td>106</td><td>89</td><td>93</td><td>99</td><td>111</td><td>111</td><td>119</td></tr><tr><td>Glass</td><td>713</td><td>436</td><td>491</td><td>692</td><td>206</td><td>358</td><td>391</td><td>487</td></tr><tr><td>Medical</td><td>267</td><td>278</td><td>292</td><td>308</td><td>320</td><td>326</td><td>336</td><td>348</td></tr><tr><td>Petroleum</td><td>169</td><td>193</td><td>160</td><td>159</td><td>182</td><td>137</td><td>161</td><td>172</td></tr><tr><td>Jewelry</td><td>1,953</td><td>1,880</td><td>1,849</td><td>2,008</td><td>2,214</td><td>1,970</td><td>1,926</td><td>1,856</td></tr><tr><td>Retail bar &amp; coin</td><td>340</td><td>273</td><td>314</td><td>205</td><td>402</td><td>325</td><td>354</td><td>395</td></tr><tr><td>Total demand</td><td>7,233</td><td>7,206</td><td>7,859</td><td>7,847</td><td>7,697</td><td>7,472</td><td>7,424</td><td>7,366</td></tr><tr><td>Mining:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Southern Africa</td><td>5,164</td><td>4,395</td><td>4,464</td><td>4,645</td><td>4,473</td><td>4,375</td><td>4,385</td><td>4,313</td></tr><tr><td>Russia</td><td>652</td><td>663</td><td>674</td><td>677</td><td>677</td><td>645</td><td>655</td><td>677</td></tr><tr><td>North America</td><td>272</td><td>265</td><td>278</td><td>265</td><td>212</td><td>200</td><td>183</td><td>184</td></tr><tr><td>Total Refined Supply</td><td>6,200</td><td>5,568</td><td>5,620</td><td>5,787</td><td>5,561</td><td>5,412</td><td>5,415</td><td>5,365</td></tr><tr><td>Autocatalyst Recycling</td><td>1,619</td><td>1,370</td><td>1,114</td><td>1,163</td><td>1,241</td><td>1,347</td><td>1,423</td><td>1,504</td></tr><tr><td>Industrial Recycling</td><td>67</td><td>69</td><td>71</td><td>76</td><td>81</td><td>81</td><td>88</td><td>90</td></tr><tr><td>Jewelry Recycling</td><td>422</td><td>372</td><td>331</td><td>298</td><td>356</td><td>330</td><td>337</td><td>339</td></tr><tr><td>Total Secondary Supply</td><td>2,107</td><td>1,811</td><td>1,515</td><td>1,536</td><td>1,678</td><td>1,758</td><td>1,848</td><td>1,934</td></tr><tr><td>Total Supply</td><td>8,307</td><td>7,378</td><td>7,135</td><td>7,323</td><td>7,240</td><td>7,170</td><td>7,263</td><td>7,299</td></tr></table>

<table><tr><td>Balance</td><td>1,074</td><td>172</td><td>(724)</td><td>(524)</td><td>(457)</td><td>(301)</td><td>(161)</td><td>(67)</td></tr><tr><td>Change in ETF Holdings (YTD for 2026)</td><td>(259)</td><td>(567)</td><td>(76)</td><td>265</td><td>70</td><td>(517)</td><td>-</td><td>-</td></tr><tr><td>Balance after change in ETF holdings</td><td>1,333</td><td>739</td><td>(648)</td><td>(789)</td><td>(527)</td><td>216</td><td>(161)</td><td>(67)</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Metals Focus, Johnson Matthey, WPIC

Figure 8. Global palladium S&D balances

<table><tr><td>Pd koz</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Autocatalyst</td><td>8,062</td><td>7,989</td><td>8,502</td><td>8,121</td><td>7,943</td><td>7,801</td><td>7,930</td><td>7,961</td></tr><tr><td>Other Industrial:</td><td>1,564</td><td>1,493</td><td>1,433</td><td>1,415</td><td>1,460</td><td>1,469</td><td>1,443</td><td>1,472</td></tr><tr><td>Chemical</td><td>434</td><td>445</td><td>455</td><td>440</td><td>475</td><td>477</td><td>472</td><td>509</td></tr><tr><td>Medical</td><td>258</td><td>232</td><td>209</td><td>192</td><td>173</td><td>159</td><td>148</td><td>142</td></tr><tr><td>Electrical</td><td>760</td><td>706</td><td>654</td><td>661</td><td>701</td><td>737</td><td>721</td><td>718</td></tr><tr><td>Jewelry</td><td>209</td><td>225</td><td>232</td><td>234</td><td>218</td><td>208</td><td>214</td><td>223</td></tr><tr><td>Total demand</td><td>9,858</td><td>9,726</td><td>10,167</td><td>9,774</td><td>9,624</td><td>9,480</td><td>9,588</td><td>9,656</td></tr><tr><td>Mining:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Southern Africa</td><td>3,133</td><td>2,642</td><td>2,743</td><td>2,777</td><td>2,669</td><td>2,669</td><td>2,668</td><td>2,698</td></tr><tr><td>Russia</td><td>2,617</td><td>2,790</td><td>2,692</td><td>2,762</td><td>2,725</td><td>2,465</td><td>2,672</td><td>2,749</td></tr><tr><td>North America</td><td>893</td><td>829</td><td>855</td><td>827</td><td>686</td><td>644</td><td>546</td><td>474</td></tr><tr><td>Total Refined Supply</td><td>6,880</td><td>6,496</td><td>6,519</td><td>6,593</td><td>6,312</td><td>6,021</td><td>6,124</td><td>6,159</td></tr><tr><td>Autocatalyst Recycling</td><td>3,048</td><td>2,602</td><td>2,071</td><td>2,259</td><td>2,424</td><td>2,692</td><td>2,878</td><td>3,114</td></tr><tr><td>Industrial Recycling</td><td>387</td><td>403</td><td>397</td><td>395</td><td>396</td><td>365</td><td>378</td><td>395</td></tr><tr><td>Jewelry Recycling</td><td>117</td><td>112</td><td>93</td><td>65</td><td>60</td><td>51</td><td>52</td><td>46</td></tr><tr><td>Total Secondary Supply</td><td>3,552</td><td>3,117</td><td>2,561</td><td>2,719</td><td>2,880</td><td>3,108</td><td>3,308</td><td>3,555</td></tr><tr><td>Total Supply</td><td>10,432</td><td>9,613</td><td>9,080</td><td>9,313</td><td>9,192</td><td>9,129</td><td>9,432</td><td>9,714</td></tr></table>

<table><tr><td>Balance</td><td>574</td><td>(113)</td><td>(1,086)</td><td>(461)</td><td>(432)</td><td>(351)</td><td>(155)</td><td>58</td></tr><tr><td>Change in ETF Holdings (YTD for 2026)</td><td>36</td><td>(92)</td><td>69</td><td>246</td><td>359</td><td>(164)</td><td>-</td><td>-</td></tr><tr><td>Balance after change in ETF holdings</td><td>537</td><td>(21)</td><td>(1,155)</td><td>(707)</td><td>(791)</td><td>(187)</td><td>(155)</td><td>58</td></tr></table>

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
