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
# Global AI Trend Tracker

EQUITY: TECHNOLOGY

# Alphabet's 2Q26 results read-through

## Quick Note

Alphabet (GOOG US, Not rated) reported its June quarter earnings on 22 July after US market close, following which management hosted an earnings call at 1:30pm PT. During the call, management discussed the company's AI cloud business performance, its progress on monetizing AI chips and AI products, as well as outlook for FY26E. The company recorded strong capex of USD44.9bn (+100.1% y-y) in 2Q26, and management raised FY26E capex guidance to USD195-205bn (from USD180-190bn, with the midpoint of USD200bn indicating +118.7% y-y growth). Given Google's continuous robust investment in AI infrastructure in 2026 and 2027, we believe Google supply chain companies, which in our view include optical transceiver players such as Innolight (300308 CH, Buy) and PCB companies such as WUS PCB (002463 CH, Buy, covered by Anne Lee) and Victory Giant (300476 CH / 2476 HK, Buy), are well positioned to benefit from the sequential tech upgrades and infra spending in the next few quarters.

Top-line growth beats consensus estimates in 2Q26; strong uptick in Google Cloud with $81.8\%$ y-y revenue growth

\- Alphabet reported $24.2\%$ y-y $(+9.0\%$ q-q) revenue growth in 2Q26, beating the Bloomberg consensus estimate by $2.4\%$ , while it recorded net profit growth of $297.6\%$ y-y, due partially to net unrealized gains on equity securities.

\- The company booked Google Cloud revenue growth of $81.8\%$ y-y (23.7% q-q) to USD24.8bn in 2Q26, beating the consensus by $10\%$ , while its operating margin improved 2.6pp q-q to $35.6\%$ in 2Q26.

\- Alphabet had negative free cash flow of USD5.9bn in 2Q26, driven by its investments in capex.

\- In terms of capex, Alphabet spent USD44.9bn in 2Q26 (+100.1% y-y and 25.9% q-q), beating the consensus by 2%, with majority of investment in tech infrastructure – \~60% in servers and \~40% in data centers and networking equipment, according to management.

\- Management raised FY26E capex guidance to USD195-205bn (previously USD180-190bn), primarily for AI compute capacity to support cloud customer demand. Moreover, management continues to expect capex to increase significantly in 2027E.

Google Cloud: significant revenue growth driven by strong demand for AI infra and AI solutions

\- Cloud revenue grew $82\%$ y-y and cloud backlog grew to USD514bn, powered by strong demand for AI infrastructure and AI solutions.

\- Google Cloud's product differentiation is driving expansion in three ways: 1) Winning new customers, more than doubling the acquisition velocity y-y.2) Deepening relationships with existing customers who are expanding their usage and exceeding their commitments by more than $50\%$ . 3) Driving growth with partners with transactions on Google Cloud Marketplace growing over 7x y-y.

AI progress: Gemini app now has 950 million MAUs; Gemini 4 in pre-training

\- Gemini 3.5 Pro is currently under testing, and Google's team is building the next generation of models (Gemini 4).

## Research Analysts

China Technology

Bing Duan - NIHK
bing.duan1@NOM.com
+852 2252 2141

Joel Ying, CFA - NIHK
joel.ying@NOM.com
+852 2252 2153

\- Google's model APIs are now processing \~22 billion tokens per minute, up from 16 billion a quarter ago. Over the last 12 months, more than 2,000 enterprises consumed over 100 billion tokens, and nearly 500 cloud customers each processed more than 1 trillion tokens in the last year.

\- Gemma family have been downloaded over 900 million times and the latest Gemma 4 models have been downloaded over 300 million times since the launch in April.

\- Agentic development platform Antigravity has more than 2.4 million weekly active users.

\- Gemini app now has 950 million monthly active users with daily active users tripling in the last year.

\- Google has reduced the cost of AI mode responses for Search to its lowest level since its launch, thanks to engineering and hardware optimization.

AI infra: TPU started shipment to external customers in 2Q26

\- The new agent-optimized Axion CPU provides 30% better performance per dollar compared to peer offerings, and management are seeing strong growth in demand for AI infrastructure offerings.

\- TPU system delivered to customer data centers for the first time in 2Q26. Management expects to recognize a relatively small portion of revenue from existing TPU system sales agreements this year, and believes the vast majority of revenue from these agreements will be realized in 2027E.

\- Given the supply-constrained environment, management plans to expand the use of third-party capacity in 3Q26 as a bridging strategy while it builds out more internal capacity. However, it will create modest margin pressure in the near term as it utilizes this capacity.

Fig. 1: Google – quarterly financial summary

<table><tr><td>Unit: USD mn</td><td></td><td>1Q26</td><td>2Q26 actual</td><td>2Q26E</td><td>Actual vs BBG Cons</td></tr><tr><td>Revenue</td><td></td><td>109,896</td><td>119,796</td><td>117,022</td><td>2.4%</td></tr><tr><td></td><td>y-y %</td><td>21.8%</td><td>24.2%</td><td>21.4%</td><td></td></tr><tr><td></td><td>q-q %</td><td>-3.5%</td><td>9.0%</td><td>6.5%</td><td></td></tr><tr><td>Gross Profit</td><td></td><td>68,625</td><td>73,853</td><td>70,934</td><td>4.1%</td></tr><tr><td></td><td>Gross margin %</td><td>62.4%</td><td>61.6%</td><td>60.6%</td><td></td></tr><tr><td>Operating profit</td><td></td><td>39,696</td><td>40,770</td><td>40,484</td><td>0.7%</td></tr><tr><td></td><td>Operating margin %</td><td>36.1%</td><td>34.0%</td><td>34.6%</td><td></td></tr><tr><td>Net profit</td><td></td><td>62,578</td><td>112,107</td><td>35,432</td><td>216.4%</td></tr><tr><td></td><td>y-y %</td><td>81.2%</td><td>297.6%</td><td>25.7%</td><td></td></tr></table>

Note: Significant increase in net profit is primarily attributable to an increase in other income due to the result of net unrealized gains on equity securities  
Source: Bloomberg Finance L.P., NOM

Fig. 2: Google - quarterly capex trend  
![](images/716a39c66336d5c3d12db049433b1cf81ca083ff68a14dd250bd973f82ee8452.jpg)  
Source: Company data, Bloomberg Finance L.P., NOM

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

I, Bing Duan, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

## Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td rowspan="2">WUS Printed Circuit</td><td rowspan="2">002463 CH</td><td>CNY 114.23</td><td>22-Jul-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>CNY 1,060.80</td><td></td><td></td><td></td><td></td></tr><tr><td>Zhongji InnoLight</td><td>300308 CH</td><td></td><td>22-Jul-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Victory Giant</td><td>300476 CH</td><td>CNY 240.40</td><td>22-Jul-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

## WUS Printed Circuit (002463 CH)

CNY 114.23 (22-Jul-2026) Buy (Sector rating: N/A)  
![](images/314617133391535bf79444ecc0c68dc53af1f2f5abb4038df4874d8d4f16124c.jpg)  
Source: LSEG, NOM  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our TP of CNY86.8 is based on 38x 2026F EPS of CNY2.28. Our target P/E multiple of 38x is close to the high-end of its historical 13-40x range. The benchmark index for this stock is CSI 300 Index.
Risks that may impede the achievement of the target price 1) Slower-than-expected PCB growth from 5G basestation PCBs, 2) weaker-than-expected datacenter demand, 3) slower-than-expected network product/platform upgrades from Intel and AMD, 4) worse-than-expected auto demand.

Zhongji InnoLight (300308 CH)  
CNY 1,060.80 (22-Jul-2026) Buy (Sector rating: N/A)  
![](images/deb79ba16ef0fb203949586e1709b66b4ecf851726d3cd1dc165c6dbb0265d2d.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our TP of CNY1,325.00 is based on 20x 2027F EPS of CNY66.06, in line with the WIND China's A share tech / electronic component sector median P/E range. The benchmark index is CSI300. Risks that may impede the achievement of the target price Downside risks: 1) weaker-than-expected demand for high-end optical modules in both the datacom and telecom markets; 2) fierce competition in the 400G and 800G optical modules segments; 3) slower-than-expected product upgrades (i.e., 800G, 1.6T); and 4) escalated price war which may affect company's export to global customers.

CNY 240.40 (22-Jul-2026) Buy (Sector rating: N/A)  
![](images/97aed25b7a4d0af4da2c58d1d6f80e3660677fccf9dadaea55b987353a40b7d4.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our target price of CNY389.00 is based on 27x 2027F EPS of CNY14.41, in line with company's historical median P/E of 27x. The benchmark index is CSI300.

Risks that may impede the achievement of the target price Downside risks include: 1) key customers' supply chain diversification and more intensified competition from peers; 2) technology changes such as COWOP which may change the competition landscape and threat company's market shares; 3) slower technology upgrade in AI PCB market; and 4) escalations on geopolitical tensions.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

58% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 33% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

39% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

3% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 15% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

## Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at: http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise stated in the valuation methodology; Japan: Russell/NOM Large Cap.

## SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

## Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or t

[中间内容因长度限制已省略]

a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
