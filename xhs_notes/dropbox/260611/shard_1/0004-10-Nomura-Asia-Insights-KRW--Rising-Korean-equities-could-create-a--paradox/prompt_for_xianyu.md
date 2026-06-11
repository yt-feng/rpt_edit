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
## Asia Insights

Foreign Exchange - Asia ex-Japan

## KRW: Rising Korean equities could create a "paradoxical phenomenon" of FX demand

There are still reasons to remain cautious on KRW, despite some positive shifts in external and local factors.

- Our negative stance on KRW is gradually shifting, due to recent external and local developments, but here are still reasons to be cautious.  
- Overall, we believe that, without an alignment of several factors – including de-escalation in US-Iran that drives a softer USD, an increase in Korean exporters' remittance and relatively less exuberance (but without risk negativity) on the global AI cycle – Korea's BoP dynamics will remain unfavorable.  
- We conducted a scenario analysis on Korea's BOP dynamics, taking into account three scenarios of FX demand.  
- One key driver of Korea BOP dynamics is National Pension Service's (NPS) revision of its 2026 asset allocation targets, which implies reduced local portfolio outflows.  
- However, in our assessment, rising domestic equity values are a bane to KRW, as the NPS may still need to rebalance some of its domestic equities allocation.  
- Furthermore, a further rally in Samsung Electronics and SK Hynix could trigger significant forced selling by funds that have a $10\%$ single-stock cap rule.  
- If Samsung Electronics and SK Hynix rally by 60%, and the broader market rallies by 10%, foreign outflows from these stocks could reach as much as USD48bn.  
- Interestingly, Korea Chief Presidential Secretary for Policy Mr Kim commented (Yonhap Infomax, 25 May) that recent KRW weakness is “a paradoxical phenomenon created by success, rather than a vulnerability of the Korean economy”.

Korea's surging current account surplus (as high as USD37.3bn in March 2026; \~23% of GDP annualised), driven by its strong tech exports, and the strong outperformance in KOSPI index (YTD: +87%; top performing major global index) should have resulted in KRW outperformance. However, KRW has instead weakened by \~5.5% year-to-date against both USD and its NEER basket, as one of the worst performers in AeJ.

## Our negative stance on KRW...

We have maintained a negative stance on KRW so far this year; we first initiated a short KRW versus CNH position on 8 January 2026, which reached our $6\%$ target on 31

March, and we have since remained cautious because of negative BoP pressures (i.e., higher energy prices, retail portfolio outflows, NPS overseas investments, FX hoarding, the K-shaped economy and limited impactful measures taken by Korean authorities, as discussed in our 14 April publication).

## ... is gradually turning due to recent external and local developments...

From here, we are turning less negative on KRW, owing to improvements in both external and local conditions, as any signing of a US-Iran agreement would likely represent a partial relief from the terms-of-trade shock across many local FX (i.e., broad USD should weaken). Locally in Korea, there have also been a few significant changes in capital flow dynamics, including the NPS announcing meaningful changes to its end-2026 portfolio allocation targets (i.e., increasing allocation to domestic equities; see below), as well as Korean retailers shifting to net small sellers of US portfolio assets in recent months (April and May 2026 also marked the first two consecutive months of net selling since June 2023).

## ... but there are still reasons to remain cautious

However, there are reasons to remain cautious on KRW until we see significant global

## Research Analysts

## Asia FX Strategy

Craig Chan - NSL

craig.chan@NOM.com

+65 6433 6106

Wee Choon Teo - NSL

weechoon.teo@NOM.com

+65 6433 6107

Vicky Chen - NSL

vicky.chen1@NOM.com

+65 6433 6540

Manthan Shingala - NSL

manthan.shingala1@NOM.com

+65 6433 6427

tailwind from a weaker broad USD. These include: 1) a lack of clarity over whether the recent near-zero Korean retail allocation into US equities is a temporary pause. The US remains the anchor of the global AI theme, and upcoming IPOs – including SpaceX (likely on 12 June), Anthropic and OpenAI (likely in H2 2026) – could attract significant Korean retail interest; 2) the change in NPS's asset allocation targets, which may not be sufficient to completely stop its overseas allocations, especially if NPS's AUM continues to grow, even if led only by gains in its domestic equities allocation (see below); 3) our analysis showing a risk of large foreign equity outflows, if Samsung Electronics and SK Hynix continue to outperform strongly, owing to the 10% single-stock cap rule on global funds (see below); and 4) statements by Korean authorities (Bloomberg, 8 June) and local media reports (Chosun, 26 May) suggesting Korean corporates are hoarding USD, which means a notable reduction in actual net trade settlement inflows.

Overall, we believe an alignment of several factors is necessary for KRW to outperform ahead. The first being a de-escalation in US-Iran (softer USD) and RMB appreciation, which could lead to an increase in Korean exporter remittances. Another factor is a reduction in the exuberance (but no risk negativity) over the global AI cycle, which could sustain the slowdown in Korean retail portfolio outflows into the US, lower the risk of foreign equity selling because of the $10\%$ single-stock cap rule and slow the NPS's AUM growth (thereby lowering the need to diversify overseas). However, we are likely not there yet: Korea's BoP dynamics could remain unfavorable without an alignment of these aforementioned factors.

## A scenario analysis on Korea's BoP dynamics

We conducted a scenario analysis on Korea's BOP dynamics, taking into account three scenarios of FX demand over a 12-month period from: i) Korean corporates' USD hoarding; ii) Korea government's commitment for a USD200bn cash investment into the US, capped at USD20bn annually; iii) NPS's and Korean retailers' local portfolio outflows; and iv) foreign portfolio outflows (i.e., $10\%$ single-stock cap rule and WGBI inclusion).

1. In a negative BOP scenario (A), where Korean corporate repatriate $40.4\%$ (based on China's weak corporate repatriation ratio between January and November 2025) of the USD325bn current account surplus (i.e., NOM's forecast from Q3 2026 to Q2 2027), retail investors purchase foreign portfolio assets at a very strong pace (i.e., the pace observed in the 12 months to March 2026; USD47.2bn) and strong outperformances by Samsung and SK Hynix (100% gains) trigger foreign investors to aggressively limit their holdings (among other assumptions; see Figure 1), Korea's major BOP flows would be very negative, with net outflows of USD204.7bn.

2. In a moderate BOP scenario (B), where Korean corporate repatriate $60.1\%$ (based average of A and C) of the USD325bn current account surplus (i.e., NOM's forecast from Q3 2026 to Q2 2027), retail investors slow purchases of foreign portfolio assets to $50\%$ of scenario (A), and outperformances by Samsung and SK Hynix $(60\%)$ trigger a rather large unwinding of foreign investor positioning (among other assumptions; see Figure 1), Korea's major BOP flows would be slightly negative, with net outflows of USD16.7bn.

3. In a positive BOP scenario (C), where Korean corporate repatriate $79.8\%$ (based on China's strong corporate repatriation ratio over the past five months to April 2026) of the USD325bn current account surplus (i.e., NOM's forecast from Q3 2026 to Q2 2027), retail investors slow their purchases of foreign portfolio assets to zero, and modest outperformances by Samsung and SK Hynix $(30\%)$ trigger a limited unwinding of foreign investor positioning (among other assumptions; see Figure 1), Korea's major BOP flows would be very positive, with net inflows of USD149.6bn.

Fig. 1: Simulation of Korea's major BOP components

<table><tr><td colspan="12">Korea major BOP components</td></tr><tr><td>USD bn</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>Avg fr 2020</td><td>Past 12M</td><td>Scenario A (12M)</td><td>Scenario B (12M)</td><td>Scenario C (12M)</td></tr><tr><td>Current Account</td><td>76</td><td>84</td><td>23</td><td>33</td><td>100</td><td>123</td><td>75</td><td>202</td><td>131</td><td>195</td><td>259</td></tr><tr><td>Financial Account</td><td>-59</td><td>-64</td><td>-48</td><td>-35</td><td>-90</td><td>-117</td><td>-71</td><td>-174</td><td>-336</td><td>-212</td><td>-109</td></tr><tr><td>FDI Asset</td><td>-35</td><td>-66</td><td>-66</td><td>-32</td><td>-50</td><td>-41</td><td>-43</td><td>-57</td><td>-115</td><td>-96</td><td>-77</td></tr><tr><td>FDI Liability</td><td>9</td><td>22</td><td>25</td><td>19</td><td>13</td><td>16</td><td>16</td><td>22</td><td>22</td><td>22</td><td>22</td></tr><tr><td>PI Asset (Eqt+Dbt)</td><td>-59</td><td>-78</td><td>-46</td><td>-45</td><td>-67</td><td>-140</td><td>-70</td><td>-128</td><td>-114</td><td>-66</td><td>-22</td></tr><tr><td>PI Liability (Eqt+Dbt)</td><td>17</td><td>59</td><td>20</td><td>37</td><td>21</td><td>53</td><td>26</td><td>13</td><td>-92</td><td>-41</td><td>-8</td></tr><tr><td>Net OI</td><td>9</td><td>0</td><td>19</td><td>-14</td><td>-7</td><td>-4</td><td>1</td><td>-24</td><td>-37</td><td>-31</td><td>-24</td></tr><tr><td>Net of major BOP components</td><td>17.1</td><td>20.2</td><td>-24.3</td><td>-2.9</td><td>10.2</td><td>5.6</td><td>4.0</td><td>27.6</td><td>-204.7</td><td>-16.7</td><td>149.6</td></tr></table>

Note: 1) CA is NOM forecasts – Q3 2026 to Q2 2027 (USD325bn surplus). Scenario (A): assume 40.4% of CA are converted back to KRW, based on China's weak corporate repatriation ratio between Jan to Nov 2025; (B): average ratio of (A) and (C); and (C): 79.8% of CA, based on China's strong corporate repatriation ratio in the past 5M to April 2026.  
2) FDI Asset: (A): 1.5x of past 12M realised net FDI plus pledged US investment of USD20bn per annum cap; (B): average of (A) and (C); (C): past 12M realised net FDI plus pledged US investment of USD20bn per annum cap.  
3) PI Asset: i) on Korean retail portfolio outflows: (A): assume strong retail outflows portfolio of USD47.2bn observed in the 12 months to Mar 2026; (B): assume half of (A); (C): assume zero outflows. ii) on NPS outflows: (A): assume rebalancing outflows of USD67.1bn (away from domestic equities) if Samsung/SK Hynix up $100\%$ , others up $10\%$ ; (B): outflows of USD42.9bn if Samsung/SK Hynix up $60\%$ , others up $10\%$ ; (C) outflows of USD22.0bn if Samsung/SK Hynix up $30\%$ , others up $5\%$ .  
4) PI Liability: i) on foreign equity outflows: Scenario (A): assume outflows of USD95.3bn if Samsung/SK Hynix up 100%, others up 10%; (B): outflows of USD47.9bn if Samsung/SK Hynix up 60%, others up 10%; (C) outflows of USD18.9bn if Samsung/SK Hynix up 30%, others up 5%. ii) on foreign bond inflows from FTSE WGBI inclusion wt at 2.05% (AUM USD2.75trn) from April 2026 over 8 months of equal allocation: (A) 90% FX hedged; (B) 80% FX hedged; and (C) 70% FX hedged.  
5) Net OI: (A): assume OI outflows picked up to 1.5 times of (C) over the past 12 months; (B): average of (A) and (C); (C): past 12M Net OI. Source: Bloomberg, CEIC, Korea NPS, NOM.

## NPS's revised 2026 asset allocation targets implies reduced portfolio outflows...

Following its fifth fund management committee meeting, NPS announced adjustments to its target weightings for 2026, as well as approved the medium-term asset allocation for 2027-2031. Focusing on NPS's 2026 asset allocation target, the key changes are:

- Increase the end-2026 target weighting of domestic stocks to 20.8% (from 14.9%) in order to “enhance the fund's long-term profitability... mitigate the market impact of rebalancing... possibility of structural changes in the domestic stock market”.  
- NPS also temporarily expanded the allowable range for Strategic Asset Allocation (SAA) “to flexibly respond to the highly volatile domestic equity market” (MOHW press release, 28 May). Although NPS did not disclose the new SAA range, Yonhap Infomax (29 May) reported that the range has been temporarily expanded from 3% to 6%. Including NPS’s 2% Tactical Asset Allocation range, this implies NPS may temporarily hold up to 28.8% in domestic equities before mandatory rebalancing.  
- The new target will only be applicable “from end-June, when the rebalancing grace period ends” (MOHW press release, 28 May). Recall that, at its first fund management committee meeting, NPS had also temporarily refrained from rebalancing its portfolio when the SAA tolerance (i.e., +/-3%) was exceeded.  
- Overall, by our calculations, NPS's new target allocation into domestic assets (i.e., equities, bonds and alternatives) will rise to $45.3\%$ from $41.3\%$ , based on its previous 26 January 2026 revision. Based on latest asset allocation data from March 2026 and NPS's new targets, we estimate that NPS's outflows to overseas assets for the remaining of 2026 may be close to zero (i.e., USD1.2bn), from outflows of USD43.9bn based on previous targets set in January 2026 (Figure 2).

Fig. 2: Korea NPS's new 2026 asset allocation targets as announced on 28 May 2026

<table><tr><td>Financial Investments</td><td colspan="2">Actual as of Mar-2026</td><td colspan="2">NPS target as of End-2026 (Jan)</td><td colspan="2">NPS target as of End-2026 (May)</td><td colspan="2">Flow impact by end 2026 JAN (Mar-26 Act. to end-26 Tgt.)</td><td colspan="2">Flow impact by end 2026 MAY (Mar-26 Act. to end-26 Tgt.)</td></tr><tr><td></td><td>%</td><td>KRW trn</td><td>%</td><td>KRW trn</td><td>%</td><td>KRW trn</td><td>KRW trn</td><td>USD bn</td><td>KRW trn</td><td>USD bn</td></tr><tr><td>Domestic Equities</td><td>21.1%</td><td>321</td><td>14.9%</td><td>242</td><td>20.8%</td><td>337</td><td>-79.3</td><td>-52.1</td><td>16.4</td><td>10.8</td></tr><tr><td>Domestic Bonds</td><td>19.2%</td><td>293</td><td>24.9%</td><td>404</td><td>23.1%</td><td>375</td><td>111.2</td><td>73.1</td><td>82.0</td><td>53.9</td></tr><tr><td>Domestic Alternatives*</td><td>1.6%</td><td>24</td><td>1.5%</td><td>24</td><td>1.4%</td><td>22</td><td>-0.4</td><td>-0.3</td><td>-2.0</td><td>-1.3</td></tr><tr><td>Overseas Equities</td><td>36.6%</td><td>557</td><td>37.2%</td><td>603</td><td>34.7%</td><td>563</td><td>46.2</td><td>30.4</td><td>5.7</td><td>3.7</td></tr><tr><td>Overseas Bonds</td><td>6.9%</td><td>105</td><td>8.0%</td><td>130</td><td>7.4%</td><td>120</td><td>24.4</td><td>16.1</td><td>14.7</td><td>9.7</td></tr><tr><td>Overseas Alternatives*</td><td>14.7%</td><td>223</td><td>13.5%</td><td>220</td><td>12.6%</td><td>205</td><td>-3.9</td><td>-2.6</td><td>-18.6</td><td>-12.2</td></tr><tr><td>Total**</td><td></td><td>1523</td><td></td><td>1622</td><td></td><td>1622</td><td>98</td><td>65</td><td>98</td><td>65</td></tr><tr><td>Domestic</td><td>41.9%</td><td>638</td><td>41.3%</td><td>669</td><td>45.3%</td><td>734</td><td>31.5</td><td>20.7</td><td>96.4</td><td>63.3</td></tr><tr><td>Overseas</td><td>58.1%</td><td>886</td><td>58.7%</td><td>953</td><td>54.7%</td><td>888</td><td>66.7</td><td>43.9</td><td>1.8</td><td>1.2</td></tr></table>

Note: \*Assume breakdown of domestic (9.7%) versus overseas (90.3%) alternatives asset is similar to that of Mar-2026. \*\* 2026 AUM growth is based on NPS's projection of KRW131trn (scaled linearly) on top of the latest available AUM as of Mar-2026. Use USD/KRW rate at 1,522 as of 10-Jun-2026. May allocation is based on NPS' 28 May 2026 announcement that it will increase its 2026 allocation to domestic equities (+5.9pp).  
Source: Bloomberg, NPS, NOM.

... however, rising domestic equities value is a bane to KRW, as NPS may still need to rebalance some of its domestic equities allocation...

However, this may severely understate potential NPS portfolio outflows into overseas assets amid a surging domestic stock market. Indeed, our Korea equity strat

[中间内容因长度限制已省略]

efined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved.
"""
