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
EQUITY: TECHNOLOGY

## Microsoft's June quarter results read-through Quick Note

Microsoft (MSFT US, Not rated) reported 4QFY26 (Jun-26 quarter) earnings on 30 July 2026 after the US market close, and management hosted an earnings call on the same day, discussing AI infrastructure, AI platform, applications and agents, as well as its outlook for 1QFY27E and FY27E. Management expects capex of over USD50bn in 1QFY27E, while its actual capex guidance for calendar year 2026 is unchanged but adjusted to USD175bn from an accounting perspective (previously USD190bn), due to some DCs shifting from finance lease to operating lease, and management expects capex to continue to grow in FY27E. Management also expects free cash flow to remain positive in FY27E. We note that AIDC infra stocks have faced a sharp sell-off lately, partially due to concerns about the sustainability of capex growth and free cash flow pressure from hyperscale AI platforms. We think MSFT's outlook for continued capex growth and positive free cash flow in FY27E may help to relieve the concern on AI infra stocks, and we like global optical transceiver leader Zhongji Innolight (300308 CH, Buy), and major PCB / CCL suppliers such as Shengyi Tech (600183 CH, Buy) and WUS PCB (002463 CH, Buy, covered by Anne Lee).

\- Microsoft Cloud's revenue surpassed USD59.3bn in 4QFY26, up $27\%$ y-y, reflecting strong demand for Azure and AI applications.

\- Commercial bookings increased 18% y-y (excl. the impact from OpenAI [unlisted]), and bookings increased 10% y-y (11% in constant currency) when including Azure commitments from OpenAI. RPO increased 25% y-y when excluding OpenAI, driven by commitments from customers outside of frontier model companies.

• Revenue from productivity and business processes was USD37.8bn, up 14% y-y, driven by M365 Commercial Cloud.

\- M365 Commercial Cloud revenue increased 16% y-y, and M365 Copilot seats surpassed 30mn. Premium offerings, including Copilot, E5, and early traction in E7, drove ARPU growth this quarter.

\- Dynamics 365 revenue increased $13\%$ y-y (12% in constant currency) with continued moderation in bookings.

\- M365 commercial products revenue increased 19% y-y, driven by large, long-duration M365 contracts that resulted in a higher in-period revenue recognition from the Windows Commercial on-premises component.

## Core business performance

\- Intelligent Cloud revenue was USD39.3bn and grew $32\%$ y-y (31% in constant currency) in 4QFY26, driven by Azure. In Azure and other Cloud services, revenue grew $43\%$ y-y, and customer demand continued to exceed available capacity.

\- M365 Consumer Cloud revenue increased 24% y-y (22% in constant currency), driven by ARPU growth. M365 consumer subscriptions grew 7% y-y.

\- Capex was USD41.0bn (including financial leases) in 4QFY26 (+69% y-y or -29% q-q). Roughly two-thirds of capex was for short-lived assets, primarily GPUs and CPUs.

## Capex guidance and 1QFY27E / FY27E outlook

## Research Analysts

\- Capex guidance for CY26E is unchanged, but the capex from an accounting

China Technology

joel.ying@NOM.com

Joel Ying, CFA - NIHK

+852 2252 2153

Bing Duan - NIHK

bing.duan1@NOM.com

+852 2252 2141

perspective is down from USD190bn to USD175bn, due to the shift from finance to operating leases.

\- Capex guidance of 1QFY27E is USD50bn+, including the lease reclassification impact from useful life update. Management expects FY27E capex to grow y-y.

\- For 1QFY27E, management expects total revenue of USD89.85-90.95bn, representing growth of 18%-19% y-y.

\- Management expects to see acceleration in commercial cloud revenue growth through this fiscal year.

## AI infrastructure

\- Management expects to have Cobalt 200 racks in over 25 data centers around the world.

\- MSFT is co-designing some reasoning models with its silicon, and is seeing $40\%$ better performance per watt when running MAI models on Maia 200.

## Monetization progress of AI Agent, app and platform

\- MSFT now has over 40,000 paid Fabric customers, up $60\%+$ y-y and over 17,000 customers now use foundry and Fabric, up $60\%$ y-y.

\- MSFT has 100,000 Foundry customers, and 4QFY26 revenue more than doubled y-y, and the number of foundry customers at 1tn tokens annualized run rate increased 4x y-y.

\- The company has over 30mn paid Microsoft 365 Copilot seats with net seat adds more than doubling q-q. Copilot is evolving rapidly from chat to co-work to autopilots.

\- The number of customers with more than 50,000 seats increased over 7x y-y in 4QFY26, and the number of enterprise customers deploying Copilot to the majority of their information workers grew nearly $75\%$ q-q.

\- GitHub now has 225 million users, while GitHub Copilot has 50 million users, and Copilot revenue accelerated over $60\%$ q-q. MSFT introduced usage-based billing and have continued to see Business and Enterprise seat growth.

Fig. 1: Microsoft - quarterly earnings summary

<table><tr><td>MSFT</td><td>Quarter</td><td colspan="3">Jun-26</td></tr><tr><td>Revs in USDmn except capex</td><td>Revs</td><td>y-y</td><td>q-q</td><td>Coming quarter guidance</td></tr><tr><td>Total revenue</td><td>90,007</td><td>18%</td><td>9%</td><td></td></tr><tr><td>Productivity and Business Processes</td><td>37,847</td><td>14%</td><td>8%</td><td>USD36.7-37.0bn, +11~12% y-y</td></tr><tr><td>Intelligent Cloud</td><td>39,306</td><td>32%</td><td>13%</td><td>USD40.95-41.25bn, +37~38%y-y</td></tr><tr><td>More Personal Computing</td><td>12,854</td><td>-4%</td><td>-3%</td><td>USD12.2-12.7bn, -6~-9% y-y</td></tr><tr><td>Capex (in USD bn)</td><td>41.0</td><td>69%</td><td>29%</td><td>USD50+bn</td></tr></table>

Source: Company data, NOM

Fig. 2: Microsoft - Capex growth trend  
![](images/e14d91ee350bdc27099430438302d4c02c3bdbf7a1fa2ed351907c67dcc10ae2.jpg)  
Source: Company data, NOM

Fig. 3: Microsoft's revenue breakdown (USD mn)  
![](images/88d900dc95a8084d7e56708f930f42026c5c0b314f827f5b21624219aa172197.jpg)  
Source: Company data, NOM

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

I, Bing Duan, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

## Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>WUS Printed Circuit</td><td>002463 CH</td><td>CNY 96.55</td><td>30-Jul-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Zhongji InnoLight</td><td>300308 CH</td><td>CNY 864.00</td><td>30-Jul-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Shengyi Technology</td><td>600183 CH</td><td>CNY 100.08</td><td>30-Jul-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

CNY 96.55 (30-Jul-2026) Buy (Sector rating: N/A)  
![](images/84dda5c549741caf5234a9691800e3915ea2473d27bfcab921266a79a6c81b73.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our TP of CNY86.8 is based on 38x 2026F EPS of CNY2.28. Our target P/E multiple of 38x is close to the high-end of its historical 13-40x range. The benchmark index for this stock is CSI 300 Index.
Risks that may impede the achievement of the target price 1) Slower-than-expected PCB growth from 5G basestation PCBs, 2) weaker-than-expected datacenter demand, 3) slower-than-expected network product/platform upgrades from Intel and AMD, 4) worse-than-expected auto demand.

Zhongji InnoLight (300308 CH)  
Rating and target price chart (three year history)

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>06-Jul-26</td><td></td><td>1,325.00</td><td>1,098.92</td></tr><tr><td>16-Apr-26</td><td></td><td>1,015.00</td><td>809.61</td></tr><tr><td>09-Jan-26</td><td></td><td>799.00</td><td>583.20</td></tr><tr><td>31-Oct-25</td><td></td><td>612.00</td><td>473.01</td></tr><tr><td>27-Aug-25</td><td></td><td>375.00</td><td>325.10</td></tr><tr><td>16-Jul-25</td><td></td><td>208.50</td><td>170.76</td></tr><tr><td>21-Apr-25</td><td></td><td>125.00</td><td>81.19</td></tr><tr><td>04-Mar-25</td><td></td><td>150.00</td><td>102.46</td></tr><tr><td>06-Nov-24</td><td></td><td>190.00</td><td>142.90</td></tr><tr><td>06-Sep-24</td><td></td><td>180.00</td><td>99.42</td></tr><tr><td>16-Jul-24</td><td></td><td>200.00</td><td>148.12</td></tr><tr><td>10-May-24</td><td></td><td>149.29</td><td>122.29</td></tr><tr><td>29-Feb-24</td><td></td><td>128.57</td><td>110.83</td></tr><tr><td>29-Jan-24</td><td></td><td>91.43</td><td>74.16</td></tr><tr><td>17-Nov-23</td><td></td><td>100.00</td><td>75.42</td></tr><tr><td>06-Oct-23</td><td>Buy</td><td></td><td>82.71</td></tr><tr><td>06-Oct-23</td><td></td><td>98.57</td><td>82.71</td></tr></table>

CNY 864.00 (30-Jul-2026) Buy (Sector rating: N/A)  
![](images/5c37bdee379848ac308bd3696bea9421c632862c8ac597aef52f5d41c5567b60.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)  
Valuation Methodology Our TP of CNY1,325.00 is based on 20x 2027F EPS of CNY66.06, in line with the WIND China's A share tech / electronic component sector median P/E range. The benchmark index is CSI300. Risks that may impede the achievement of the target price Downside risks: 1) weaker-than-expected demand for high-end optical modules in both the datacom and telecom markets; 2) fierce competition in the 400G and 800G optical modules segments; 3) slower-than-expected product upgrades (i.e., 800G, 1.6T); and 4) escalated price war which may affect company's export to global customers.

Shengyi Technology (600183 CH)  
CNY 100.08 (30-Jul-2026) Buy (Sector rating: N/A)  
![](images/c3aaaf6e9521aecec47962082874cea2e5be2e750516348c0cc5cdb15f916b53.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our TP of CNY195.00 is based on 43x 2027F EPS of CNY4.51, in line with FY26-28F earnings CAGR of 43%. The benchmark index is CSI 300.

Risks that may impede the achievement of the target price Downside risks include: 1) lower-than-expected PCB demand in downstream sectors such as 5G, servers, auto electronics; and 2) more intensified market competition in the CCL market leading to margin pressures.

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

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that

[中间内容因长度限制已省略]

bai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
