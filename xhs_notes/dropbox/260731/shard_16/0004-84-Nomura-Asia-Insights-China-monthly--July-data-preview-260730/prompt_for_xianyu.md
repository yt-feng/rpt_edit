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

## China monthly: July data preview

With real GDP growth in Q2 the lowest post-Covid reading, June activity data continued to show a large divide between strong exports and weak domestic demand. We expect such a trend to continue in July. High-frequency data point to a modest rebound in crude oil imports in July, which could ease some supply disruptions to the oil-related sectors. However, such stabilization might prove short-lived, owing to the re-escalation of the Middle East conflict in mid-July. The sharp deterioration in domestic demand in Q2 prompted the Politburo meeting to emphasize the need to step up pro-growth policy measures and speed up fiscal spending, while we believe the scale of such measures might be limited, due to Beijing's concerns of diminishing returns on investment and unmanageable fiscal deficits. Moreover, as the fruits of AI-driven growth are mainly reaped by a few "smart" cities and the AI boom has led to a geographic K-shape, the K-shaped economy naturally reduces the urgency for an aggressive, sweeping stimulus.

## We expect mixed PMIs and activity data

As favourable seasonal factors have subsided, we expect the official manufacturing PMI to drop to 49.9 in July from 50.3 in June, while the official non-manufacturing PMI might also fall in July to 49.9 from 50.2 in June on lackluster domestic demand. By contrast, thanks to the export boom, the RatingDog manufacturing PMI, which surveys more SMEs and exporters in the eastern coastal region of China, is likely to remain elevated at 51.5 in July, little changed from 51.7 in June.

On major activity data, we expect IP growth to moderate to 5.0% y-o-y in July from 5.3% in June, due to disruptions caused by a string of severe typhoons in coastal southern China and the absence of a favourable working-day effect. Although imports of oil started to rebound in July, the magnitude looks moderate, with a limited boost to production activity in the oil and chemical industries. Amid the AI supercycle and rising demand for renewable goods, we expect export growth to remain elevated at 22.9% y-o-y in July, albeit moderating from a robust pace of 27.0% in June. By contrast, amid weak domestic demand, we forecast growth in retail sales and FAI at 1.5% y-o-y and -8.2%, respectively, little improved from 1.0% and -10.0% in June.

We expect inflation to remain steady on external forces, with steady credit growth

We expect CPI inflation to drop to 0.8% y-o-y in July from 1.0% in June, dragged down by food prices, with less of a boost from energy and core prices. In sequential terms, we expect CPI inflation to seasonally rebound to 0.2% m-o-m in July from -0.3% in June, but slower than the 0.4% in July 2025. We expect PPI inflation of 4.1% y-o-y in July, unchanged from June, owing to the resurgence of oil prices due to a re-escalation of the Middle East conflict. On a sequential basis, PPI inflation is likely to edge up to -0.2% m-o-m in July from -0.3% June, the same as last year. We expect credit growth, which is measured as year-on-year growth in outstanding aggregate financing (AF), to remain at 7.4% y-o-y in July, unchanged from June, as the weakness in bond financing could be largely offset by slightly faster bank loan issuance on an extremely low base.

## Research Analysts

Asia Economics

Jing Wang - NIHK
jing.wang@NOM.com
+852 2252 1011

Harrington Zhang - NIHK
harrington.zhang@NOM.com
+852 2252 2057

Hannah Liu - NIHK

hannah.liu@NOM.com

+852 2252 1082

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

## July data preview

## Official manufacturing PMI in July: 49.9 (June: 50.3)

## Official non-manufacturing PMI in July: 49.9 (June: 50.2)

## RatingDog manufacturing PMI in July: 51.5 (June: 51.7)

We expect official manufacturing PMI to drop to 49.9 in July from 50.3 in June, in view of sustained weakness in domestic demand, supply chain disruptions to upstream sectors and the falling EPMI. China's EPMI (Emerging Industries PMI), a non-seasonally adjusted leading indicator of the official PMI, came in at 47.8 in July, below the historical July average of 48.5. In sequential terms, it dropped by 2.6pp to 47.8 in July from 50.4 in June, with the decline smaller than the historical June-to-July average decrease of 3.9pp.

We expect the official non-manufacturing PMI to fall to 49.9 in July from 50.2 in June, as suggested by lackluster tourism spending during this summer holiday. We believe household catering and entertainment demand could be further weighed down by ongoing K-shaped property market and stock market rally amid the AI boom.

We expect the RatingDog manufacturing PMI (formerly the Caixin manufacturing PMI), which surveys more SMEs and exporters in the eastern coastal region of China, to remain elevated at 51.5 in July from 51.7 in June, supported by robust exports driven by the AI supercycle. Growth in imports from Korea climbed further to $94.1\%$ in 1-20 July from $92.0\%$ in June, while growth in exports to Korea eased to $21.8\%$ from $42.8\%$ over the same period.

## Industrial production growth in July: 5.0% y-o-y (June: 5.3%)

We expect industrial production (IP) growth to moderate to $5.0\%$ y-o-y in July from $5.3\%$ in June, due to disruptions caused by a string of severe typhoons in coastal southern China and the absence of favourable working-day effect. The rebound in June was partly due to one extra working day, while the number of working days in July is 23, the same as last July. Although imports of oil started to rebound in July, the magnitude looks moderate, with a limited boost to production activity of oil and chemical industries.

According to Bloomberg citing data from Kpler, China's monthly seaborne oil imports rebounded for the first time since the Iran war in late February, edging up to 7.8mn bpd in July from 6.2mn bpd in June. Although the oil import level is still $34\%$ below the pre-war levels in February, the resumption of oil imports should modestly ease the supply disruptions, as evidenced by improved production activity in oil-related sectors.

High-frequency data related to the oil and chemical industries

\- The operating rate of Shandong oil teapot refineries rebounded to 54.2% at end-July from 46.9% at end-June and 53.6% at end-May, but is still below 59.9% reading from end-April. Its monthly average operating rate rose to 3.2pp above last year's July levels from 1.4pp above in June, but still below 6.2pp above in May, 7.0pp above in April and 9.7% above in March.

\- The operating rate of purified terephthalic acid (PTA) factories rebounded further to $61.1\%$ at end-July from $55.6\%$ at end-June and $55.5\%$ at end-May, while its monthly average operating rate dropped to 23.2pp below last year's July levels from 15.5pp below in June.

\- The operating rate of polyester filament yarns (PFY) factories in Jiangsu and Zhejiang provinces edged up to 74.4% at end-July from 73.8% at end-June, and its monthly average operating rate dropped to 18.0pp below last year's July levels from 16.7pp below in June.

## Other high-frequency data

\- The weekly operating rate of cement factories moderated to 2.4pp above last year's July levels from 2.7pp above in June.

\- The weekly cement shipment-to-output ratio moderated to 0.3pp above last year's July levels from 0.6pp above in June.

\- Growth in weekly steel rebar output at major steel mills fell to $-5.1\%$ y-o-y in July from $0.2\%$ in June, while output growth of crude steel also fell to $-4.7\%$ from $-3.6\%$ .

\- Growth in the daily average volume of coal burned at power plants in eight provinces in South China dropped to $-10.8\%$ y-o-y in July from $0.6\%$ in June.

Export growth in July: 22.9% y-o-y (June: 27.0%)

Import growth in July: $31.5\%$ y-o-y (June: $36.0\%$ )

## Trade balance in July: USD100bn (June: USD126bn)

We expect export growth to remain elevated at $22.9\%$ y-o-y in July, slowing moderately from the strong reading of $27.0\%$ in June, as we forecast persistently strong export momentum in the near term.

We expect import growth to edge down modestly to $31.5\%$ y-o-y in July from $36.0\%$ in June, driven by a slightly higher base and strong price effects. We also expect the crude oil price declines taking place in late June and early July start to feed into in China's import data in July, given the approximate 20-day shipping window from the Persian Gulf to China. That said, we expect China's imports of crude in volume terms to remain depressed in July. Additionally, ongoing price increases across a range of semiconductor products – particularly memory chips – are adding further upward pressure to import values.

As a result, we expect the trade surplus to narrow to USD100.4bn in July from USD125.6bn in June.

## Higher-frequency trade-related data

According to the Ministry of Transport, growth in weekly container throughput at major ports edged up marginally to -1.7% y-o-y on a month-to-date basis (as of 26 July) from 5.1% in June.

On imports, the year-over-year change in the China Import Dry Bulk Freight Index (CDFI), which reflects freight rates for dry bulk cargo (including iron ore, coal, grain and nickel ore) imported into China, moderated to 39.6% y-o-y on a month-to-date basis in July from 46.6% in June. Brent crude oil price growth moderated to 15.6% y-o-y on a month-to-date basis in July from 19.8% in June but remains somewhat elevated.

## CPI inflation in July: $0.8\%$ y-o-y (June: $1.0\%$ )

We expect CPI inflation to drop to 0.8% y-o-y in July from 1.0% in June, dragged by food prices, with less of a boost from energy and core prices. In sequential terms, we expect CPI inflation to seasonally rebound to 0.2% m-o-m in July from -0.3% in June, but slower than the 0.4% m-o-m growth from July 2025.

We expect food price inflation to drop to $-1.7\%$ y-o-y in July from $-1.6\%$ in June. In sequential terms, it is likely to seasonally improve to $-0.3\%$ m-o-m in July from $-0.4\%$ in June, below the $-0.2\%$ m-o-m recorded a year ago. According to high-frequency data from the MARA, the Agricultural Product Wholesale 200 Price Index dropped to $-1.1\%$ y-o-y in July from $-0.4\%$ in June. Egg price inflation eased to $35.3\%$ y-o-y in July from $40.6\%$ in June, while pork price inflation remained muted at $-24.4\%$ y-o-y July, though it improved from $-28.3\%$ in June.

For energy prices, due to the U-turn in Middle East tensions and the resurgence in oil prices, the NDRC hiked retail petrol prices by RMB300/tone on 18 July after cutting by RMB950/tonne on 4 July. The NDRC raised petrol prices by RMB105/tonne last July. We expect domestic retail fuel price inflation to drop to $0.2\%$ y-o-y in July from $18.6\%$ in June, which could provide a limited boost to headline CPI inflation.

We expect core inflation to drop to $0.9\%$ y-o-y in July from $1.0\%$ in June, driven by weak domestic demand as suggested by lackluster tourism activity during the summer holiday, as well easing global gold price inflation. These dragging forces should more than offset supporting forces from the recent rise in consumer electronics prices driven by surging chip prices amid the AI supercycle.

## PPI inflation in July: 4.1% y-o-y (June: 4.1%)

We expect PPI inflation to remain at 4.1% y-o-y in July, unchanged from June, supported by the resurgence of oil prices due to the end of the Middle East ceasefire. Support from prices of non-ferrous metals, AI-related products and new energy products is likely to remain intact. On a sequential basis, PPI inflation is likely to edge up to -0.2% m-o-m in July from -0.3% June, the same as last year.

Brent oil price inflation eased only slightly to $15.3\%$ y-o-y in July from $19.8\%$ in June, due to the resurgence of oil prices following the end of ceasefire. In sequential terms, Brent oil price inflation turned less negative, rising to $-4.4\%$ m-o-m in July from $-20.8\%$ in June. The easing of oil price inflation should ease PPI inflation in oil-related sectors, which together take up $14.1\%$ of the PPI basket, according to our estimates.

Despite easing global oil prices, we see sustained drivers that support PPI inflation from non-ferrous metal prices and rising chip prices amid the AI boom. Global LME price inflation remained elevated at 37.9% y-o-y in month-to-date July from 38.0% in June, which should continue to support price inflation in non-ferrous related industries that take up 7.3% of the PPI basket. Also, surging global chip prices should continue to push up PPI inflation in the computer, communication and other electronic equipment manufacturing sector, which accounts for 12.8% of the PPI basket.

Amid rising global demand for new energy products, prices of raw materials for solar panels and EV batteries remained elevated, which should provide support for PPI inflation in the electrical machinery and equipment manufacturing sectors that account for 8.4% of the PPI basket.

## Retail sales growth in July: 1.5% y-o-y (June: 1.0%)

We expect retail sales growth to tick up to $1.5\%$ y-o-y in July from $1.0\%$ in June, thanks to a low base from last year. Underlying momentum of consumption is still weighed down by payback effects of the scaled-back trade-in program, subdued consumer confidence, as well as negative price effects from domestic fuel and consumer electronics, driven by imported inflation. By components, we expect retail sales growth in autos, catering and merchandise excluding autos of $-16.0\%$ y-o-y, $1.1\%$ and $3.7\%$ , respectively, in July versus $-16.1\%$ , $1.2\%$ and $5.8\%$ in June.

On auto sales, according to early estimates from the CPCA, volume growth in passenger car retail sales is likely to remain subdued at -16.8% y-o-y in July, rising from -23.2% in June. We expect auto sales to be a main drag for headline retail sales due to the scaled-back trade-in program and the increase in EV purchase tax from 0% to 5%.

For other components, growth in the catering sector is likely to remain soft, given the lackluster tourism spending during summer holiday, despite a low base from last year due to the new austerity rule. Growth in merchandise sales excluding autos is likely to continue to fall back across major durable goods categories on the payback effect from the trade-in program. Households are also likely to cut spending on petroleum products and consumer electronics, given rising prices led by imported inflation.

## FAI growth in July: -8.2% y-o-y (June: -10.0%)

## FAI growth in July: year-to-date: -6.1% y-o-y (June: -5.7%)

We expect fixed asset investment (FAI) growth to improve slightly to -8.2% y-o-y in July from -10.0% in June, which implies cumulative year-to-date growth of -6.1% for July. Despite this modest monthly improvement, we see no material recovery in FAI growth in July. The persistent weakness reflects subdued fiscal support, with net issuance of government bonds again falling below year-earlier levels in July. This continued shortfall in bond issuance has constrained public investment spending, limiting the scope for a meaningful rebound in overall FAI activity.

## Property investment growth in July (single-month): -23.0% y-o-y (June: -24.1%)

Property investment growth in July (year-to-date): -18.6% y-o-y (June: -18.0%) We expect the steep decline in property investment to persist in July, dropping by 23.0% y-o-y, little changed from the 24.1% decline in June. On high-frequency data, growth in new home sales by floor space in the Wind survey of 20 major cities increased to 2.1% y-o-y in July from -6.7% in June, due mainly to a low base. Growth in existing home sales volumes in a sample of 18 cities slowed further to 9.1% y-o-y in July from 12.3% in June.

As the fruits of AI-driven growth are mainly reaped by a few “s

[中间内容因长度限制已省略]

ed or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
