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
# Asia Insights

Economics - Asia ex-Japan

## China: The contractionary fiscal policy stance in H1

The Ministry of Finance released June's fiscal data last week. Given the volatility in monthly figures, we use H1 data to gauge a broader trend. According to our estimates, augmented fiscal revenue growth, which includes off-budget revenues such as income from land sales, improved to $1.0\%$ y-o-y in H1 from $-2.9\%$ in 2025, driven mainly by faster tax revenue growth thanks to both reflation and more stringent tax collection enforcement. However, augmented fiscal expenditure turned negative, falling to $-2.9\%$ y-o-y in H1 from $3.7\%$ in 2025, dragged partially by a slow pace of government bond issuance. On a quarterly basis, there was a more pronounced improvement in fiscal revenue in Q2 alongside a sharper deterioration in fiscal spending compared with Q1.

## We expect less contractionary/more expansionary fiscal policy in H2

Faster fiscal revenue growth alongside slower expenditure growth reduces the fiscal impulse and can have a contractionary impact; it also helps to explain the apparent GDP growth slowdown in Q2. We expect Beijing to step up fiscal spending in H2 by speeding up government bond issuance and the deployment of the RMB800bn new policy financing tool. Assuming the full-year net government bond quota is fully utilized, we expect RMB6.80trn of net government bond financing (excluding debt swaps) to be conducted in H2, which would represent $57\%$ of full-year quota and surpass the RMB5.75trn recorded in H2 2025.

## July Politburo meeting: A large fiscal stimulus is unlikely

We expect Beijing to maintain an accommodative policy stance during this week's Politburo meeting, consistent with the symposium convened by Premier Li Qiang on 13 July. However, the scale of incremental fiscal policy measures might be limited for three reasons. First, surging export growth, despite being mainly driven by a rapid rise in the prices of AI-related goods, might alleviate some of Beijing's concerns about overall growth. Second, Given the fiscal budget set at the NPC meeting in March, fiscal spending is likely to pick up in H2. Third, Beijing recognizes that short-term policies like trade-in programs lead to payback effects and cannot be used too frequently. Fourth, policymakers are concerned about the potential downsides from fiscal stimulus and a rebound of local government debt.

## Fiscal revenue growth improved in H1

According to our estimates, augmented fiscal revenue growth improved to 1.0% y-o-y in H1 from -2.9% in 2025, driven by on-budget fiscal revenue, while growth in revenue from government-managed funds contracted more sharply. On-budget fiscal revenue rose to 4.7% y-o-y in H1 from -1.7% in 2025, above the 2.2% full-year target set at the March NPC meeting (Figure 1). Tax revenue growth rose to 5.3% y-o-y in H1 2026 from 0.8% in 2025, primarily driven by growth of value-added tax (VAT) and corporate income tax (CIT) collections, which rose to 6.0% y-o-y and 3.9%, respectively, in H1 2026 from 3.4% and 1.0% in 2025 (Figure 2). Non-tax revenue growth also rebounded to 2.3% y-o-y in H1 from -11.3% in 2025, thanks to a low base effect and higher revenue from paid use of state-owned resources, including mining rights.

Other major types of tax revenues exhibited notable divergences in H1. Stamp duty tax growth from stock trading jumped to $97.3\%$ y-o-y in H1 2026 from $57.8\%$ in 2025, buoyed by surging stock trading volumes amid the AI supercycle. Individual tax revenue growth edged higher to $13.1\%$ y-o-y in H1 from $11.5\%$ in 2025, supported by enhanced tax enforcement on overseas earnings and online streaming income, as well as rising capital gains tax collections amid the stock market rally. In contrast, consumption tax revenue growth turned negative, falling to $-3.4\%$ y-o-y in H1 from $2.0\%$ in 2025, weighed on by softer retail sales growth due to the payback effect from the trade-in program and weak consumer sentiment amid the perennial property sector downturn.

## Research Analysts

Asia Economics

Hannah Liu - NIHK
hannah.liu@NOM.com
+852 2252 1082

Jing Wang - NIHK
jing.wang@NOM.com
+852 2252 1011

Ting Lu - NIHK
ting.lu@NOM.com
+852 2252 1306

## Property-related revenue growth deteriorated further in H1

Growth in property-related tax revenue worsened to -5.8% y-o-y in H1 from -4.4% in 2025, as the property downturn persists (Figure 3). While second-hand property transactions showed some improvement in a few large cities, it was unable to fully offset the weakness in other cities. Land sales revenue plunged to -31.5% y-o-y in H1 from -14.7% in 2025. The deterioration in land sales revenue dragged growth in government-managed fund revenue to -21.6% y-o-y in H1 2026 from -7.0% y-o-y in 2025, falling short of the March NPC meeting's full-year revenue target of 0.6% growth for government-managed funds. The continued deterioration in property-related revenue is likely to exacerbate the fiscal strain on local governments.

## The recent improvement in VAT and CIT growth may be unsustainable

We believe the improvement in VAT and CIT growth in H1 was primarily driven by external forces rather than underlying domestic strength. Surging global oil prices have temporarily boosted revenue and profits among the upstream enterprises, many of which are large state-owned entities with higher tax compliance rates. However, as China remains a major net oil importer, the worsening terms of trade could ultimately squeeze most domestic producers and consumers, potentially eroding the tax base over the longer term.

## Fiscal expenditure growth turned negative in H1

According to our estimate, augmented fiscal expenditure turned negative, falling to -2.9% y-o-y in H1 2026 from 3.7% in 2025. On-budget fiscal expenditure rose only by 1.5% y-o-y in H1, slightly higher than the 1.0% growth in 2025, marking the slowest pace of H1 fiscal spending growth since 2020, and well below the full-year fiscal spending target of 4.4% set at the NPC meeting. The slowdown in off-budget was even sharper, with growth in government-managed fund expenditure plunging to -16.4% y-o-y in H1 from 11.3% in 2025. The contraction deepened in Q2, reaching -31.0% y-o-y from 3.1% in Q1, weighed on by local government fiscal strain amid the sharp decline in land sales revenue.

By major category of on-budget fiscal expenditure, growth in aggregate infrastructure spending remained negative at $-4.8\%$ y-o-y in H1, little improved from $-7.8\%$ in 2025. On a quarterly basis, the slowdown in infrastructure spending worsened in Q2, falling by $7.9\%$ y-o-y after a $1.8\%$ decline in Q1. Healthcare spending growth was the strongest growth among major expenditure categories, rising to $10.8\%$ y-o-y in H1 from $5.7\%$ in 2025, supported by front-loaded disbursements of childbirth subsidies. Other public welfare spending trends were mixed, with education expenditure growth dropping to $0.6\%$ y-o-y in H1 from $3.2\%$ in 2025, while social security and employment spending growth edged higher to $7.6\%$ y-o-y from $6.7\%$ in 2025.

## Fiscal spending is likely to pick up in H2

By our estimates, total government bond net issuance reached RMB6.64trn in H1, accounting for 48% of the RMB13.89trn annual government bond quota set at the March NPC meeting (Figure 5) and below the RMB7.25trn recorded in H1 2025. Excluding special refinancing bonds used for debt swaps, which do not contribute to incremental fiscal spending, net government bond issuance amounted to RMB5.09trn in H1, which represented just 43% of the full-year quota and trails the RMB6.09trn issued in H1 2025. Assuming the full-year bond quota is fully utilized, we expect net government bond issuance excluding debt swaps to rise to RMB6.80trn in H2, surpassing the RMB5.75trn recorded in H2 2025. Given the expected rise in government bond issuance and the implementation of new policy financing tools, we expect fiscal spending growth to pick up in the second half of the year.

Fig. 1: Annual growth of tax and non-tax revenues  
![](images/04c660b46966a1cccf0d9de2baca1450e3e3cf32cdc28e310318ce71bb659a29.jpg)  
Note: Tax revenue in 2022-23 is adjusted by excluding distortions due to a large-scale VAT credit refunds.  
Source: Wind, NOM Global Economics.

Fig. 2: Growth in major categories of tax revenue  
![](images/f02f80ac35b21941eda5fcf324669727ba48472d18696dfe8e96bb0caf457c70.jpg)  
Source: Wind, NOM Global Economics.

Fig. 3: Property-related revenue growth  
![](images/26d9c452437bcc1be68cd9d507eced9ee11074088dbbb644910ce4c7fe005723.jpg)  
Source: Wind, NOM Global Economics.

Fig. 4: Annual growth of fiscal spending  
![](images/4766b58f8122736cf670799ccfc10fef56545cb76cdc606e5f346429ddee3f1b.jpg)  
Source: Wind, NOM Global Economics.

Fig. 5: A review of government bond financing in H1

<table><tr><td>Governmnet bond net issuance</td><td>2026 quota RMBbn</td><td>H1 2026</td><td>Share</td></tr><tr><td>Central government general bond (CGGB)</td><td>5,090</td><td>2,120</td><td>42%</td></tr><tr><td>Central government special bond (CGSB)</td><td>1,300</td><td>572</td><td>44%</td></tr><tr><td>CGSB for state-bank capital injection</td><td>300</td><td>0</td><td>0%</td></tr><tr><td>Central government bond (CGB)</td><td>6,690</td><td>2,692</td><td>40%</td></tr><tr><td>Local government general bond (LGGB)</td><td>800</td><td>330</td><td>41%</td></tr><tr><td>Local government special bond (LGSB)</td><td>4,400</td><td>2,070</td><td>47%</td></tr><tr><td>Special refinancing bond for debt swap</td><td>2,000</td><td>1,548</td><td>77%</td></tr><tr><td>Local government bond (LGB)</td><td>7,200</td><td>3,948</td><td>55%</td></tr><tr><td>Total</td><td>13,890</td><td>6,640</td><td>48%</td></tr><tr><td>Total (excluding LGSB for debt swap)</td><td>11,890</td><td>5,092</td><td>43%</td></tr></table>

Source: Wind, NOM Global Economics.

Fig. 6: Major fiscal indicators

<table><tr><td>Major fiscal indicators</td><td>unit</td><td>Jun 26</td><td>May 26</td><td>Q2 26</td><td>Q1 26</td><td>H1 26</td><td>2025</td><td>2024</td></tr><tr><td>On-budget revenue growth</td><td>% y-o-y</td><td>8.7</td><td>6.6</td><td>7.3</td><td>2.4</td><td>4.7</td><td>-1.7</td><td>1.3</td></tr><tr><td>Tax revenue</td><td>% y-o-y</td><td>10.8</td><td>6.8</td><td>8.6</td><td>2.2</td><td>5.3</td><td>0.8</td><td>-3.4</td></tr><tr><td>Value-added tax (VAT)</td><td>% y-o-y</td><td>4.9</td><td>7.9</td><td>7.4</td><td>4.9</td><td>6.0</td><td>3.4</td><td>-3.8</td></tr><tr><td>Corporate income tax</td><td>% y-o-y</td><td>29.7</td><td>3.3</td><td>11.3</td><td>-5.6</td><td>3.9</td><td>1.0</td><td>-0.5</td></tr><tr><td>Property-related tax</td><td>% y-o-y</td><td>-12.3</td><td>-2.6</td><td>-5.3</td><td>-6.3</td><td>-5.8</td><td>-4.4</td><td>0.0</td></tr><tr><td>Consumption tax</td><td>% y-o-y</td><td>-5.3</td><td>-2.0</td><td>-2.0</td><td>-4.4</td><td>-3.4</td><td>2.0</td><td>2.6</td></tr><tr><td>Individual income tax</td><td>% y-o-y</td><td>17.0</td><td>12.4</td><td>16.4</td><td>10.5</td><td>13.1</td><td>11.5</td><td>-1.7</td></tr><tr><td>Stamp duty tax on stock trading</td><td>% y-o-y</td><td>145.3</td><td>145.9</td><td>118.2</td><td>78.3</td><td>97.3</td><td>57.8</td><td>-29.1</td></tr><tr><td>Non-tax revenue</td><td>% y-o-y</td><td>2.9</td><td>5.6</td><td>1.6</td><td>2.9</td><td>2.3</td><td>-11.3</td><td>25.4</td></tr><tr><td>Revenue growth from government-managed funds</td><td>% y-o-y</td><td>-31.1</td><td>-20.5</td><td>-26.5</td><td>-16.2</td><td>-21.6</td><td>-7.0</td><td>-12.2</td></tr><tr><td>Revenue from land sales</td><td>% y-o-y</td><td>-42.2</td><td>-35.8</td><td>-38.0</td><td>-24.4</td><td>-31.5</td><td>-14.7</td><td>-16.0</td></tr><tr><td>On-budget expenditure growth</td><td>% y-o-y</td><td>4.0</td><td>-1.6</td><td>0.2</td><td>2.6</td><td>1.5</td><td>1.0</td><td>3.6</td></tr><tr><td>Infrastructure</td><td>% y-o-y</td><td>-0.5</td><td>-11.3</td><td>-7.9</td><td>-1.8</td><td>-4.8</td><td>-7.8</td><td>7.3</td></tr><tr><td>Healthcare</td><td>% y-o-y</td><td>8.8</td><td>10.7</td><td>9.3</td><td>12.1</td><td>10.8</td><td>5.7</td><td>-9.1</td></tr><tr><td>Education</td><td>% y-o-y</td><td>5.4</td><td>-0.5</td><td>1.6</td><td>-0.3</td><td>0.6</td><td>3.2</td><td>2.0</td></tr><tr><td>Social security and employment</td><td>% y-o-y</td><td>13.2</td><td>1.3</td><td>5.9</td><td>9.0</td><td>7.6</td><td>6.7</td><td>5.6</td></tr><tr><td>Science &amp; technology</td><td>% y-o-y</td><td>2.6</td><td>13.0</td><td>4.9</td><td>-3.7</td><td>1.3</td><td>4.8</td><td>5.7</td></tr><tr><td>Environmental protection</td><td>% y-o-y</td><td>-15.7</td><td>-19.1</td><td>-19.8</td><td>-1.1</td><td>-10.3</td><td>6.1</td><td>-1.4</td></tr><tr><td>Expenditure growth from government-managed funds</td><td>% y-o-y</td><td>-44.0</td><td>-11.2</td><td>-31.0</td><td>3.1</td><td>-16.4</td><td>11.3</td><td>0.2</td></tr><tr><td>Fiscal balance</td><td>RMB bn</td><td>-887</td><td>-201</td><td>-919</td><td>-1,309</td><td>-2,228</td><td>-2,333</td><td>-1,887</td></tr><tr><td>Fiscal balance (12m rolling sum)</td><td>RMB bn</td><td>-6,793</td><td>-6,843</td><td>-6,793</td><td>-7,182</td><td>-6,793</td><td>-7,135</td><td>-6,491</td></tr></table>

Note: \*refers to fiscal revenue excluding VAT credit refund.  
Source: Wind, NOM Global Economics.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Hannah Liu, Jing Wang and Ting Lu, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, 

[中间内容因长度限制已省略]

ed or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

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

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
