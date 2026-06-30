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

## China monthly: June and Q2 data preview

Growth across major activity data slowed materially in April and May, confirming our view that the growth rebound in Q1 was short-lived, and we expect no major rebound in June. The export surge was largely fueled by a spike in chip prices amid the AI supercycle, which failed to provide a meaningful boost to real industrial production, while the Middle East conflict has severely disrupted factory operations across oil and chemical sectors. Growth of retail sales and fixed asset investment have turned negative again, as aggregate domestic demand is being weighed on by payback effects from the trade-in program, the prolonged property slump and a worsening of the double K-shapes. Based on an examination of both supply- and demand-side indicators, we maintain our forecast for real GDP growth to slow to $4.1\%$ y-o-y in Q2 from $5.0\%$ in Q1. With the renewed sharp declines in investment against Beijing's commitment to stabilize investment, we believe Beijing will likely accelerate bond issuance and step up fiscal spending in coming months.

## Both supply- and demand-side indicators point to weaker growth in Q2

We evaluate Q2 GDP growth by analyzing supply- and demand-side indicators for April-May alongside our projections for June. We maintain our forecast for a marked slowdown in real GDP growth to 4.1% y-o-y in Q2 from 5.0% in Q1, while nominal GDP growth might stabilize in Q2 on an anticipated higher GDP deflator, compared with 4.9% in Q1.

## The production side

On the supply side, monthly average growth for industrial and services output volumes slowed markedly to 4.3% y-o-y and 4.4%, respectively, in April-May. The quarterly growth of these data might both reach 4.5% y-o-y in Q2, down notably from 6.1% and 5.1%, respectively, in Q1. As industrial and services sectors account for 30% and 58% of GDP, respectively, a slowdown of this magnitude would shave 0.5pp and 0.4pp off of real GDP growth in Q2. Consequently, real GDP growth will likely slow noticeably to 4.1% y-o-y in Q2 from 5.0% in Q1, consistent with our current forecasts.

## The expenditure side

The slowdown might have been even more pronounced when demand-side indicators are examined. In April-May, average monthly nominal growth for retail sales and fixed asset investment fell sharply to -0.2% y-o-y and -9.5%, respectively, while export growth in USD terms increased to 16.7%. We project Q2 quarter growth for these data at 0.2% y-o-y, -9.0% and 16.5%, respectively, compared with their readings of 2.4%, 1.7% and 14.7% in Q1. Factoring in higher anticipated inflation, we expect both real sales and FAI to contract markedly in Q2 in real terms. Moreover, since surging chip and electronics prices drove roughly half of the export strength, real export growth should be much lower than the nominal figure, resulting in a much smaller growth boost from exports and leaving it far from sufficient to offset the declines in retail sales and FAI.

Although demand-side indicators point a much sharper growth slowdown in Q2, we expect the official GDP figure to align more closely with supply-side indicators, as China's GDP is calculated primarily from the production side.

## The GDP deflator is set to turn positive

Amid surging oil and chip prices, CPI and PPI inflation increased to 1.2% y-o-y and 3.4%, respectively, in April-May. We forecast the quarterly averages at 1.2% y-o-y and 3.6%, respectively, in Q2, up from 0.8% and -0.6% in Q1. With higher CPI and PPI inflation, we expect the GDP deflator to turn positive in Q2, rising to about 1.0% y-o-y from -0.1% in Q1 and breaking the trend in which it has been negative for 13 out of the past 14 quarters. However, the increase in inflation has been primarily driven by external factors, rather than a real recovery in domestic demand.

## Research Analysts

Asia Economics

Jing Wang - NIHK
jing.wang@NOM.com
+852 2252 1011

## Harrington Zhang - NIHK

harrington.zhang@NOM.com

+852 2252 2057

## Hannah Liu - NIHK

hannah.liu@NOM.com

+852 2252 1082

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

## June and Q2 data preview

Official manufacturing PMI in June: 49.8 (May: 50.0)

## Official non-manufacturing PMI in June: 49.8 (May: 50.1)

## RatingDog manufacturing PMI in June: 51.5 (May: 51.8)

We expect the official manufacturing PMI to drop to 49.8 in June from 50.0 in May, in view of sustained weakness in domestic demand, supply chain disruptions to upstream sectors despite recent easing of Middle East tensions and the weaker-than-usual EPMI. China's EPMI (Emerging Industries PMI), a non-seasonally adjusted leading indicator of the official PMI, dropped by 2.5pp to 50.4 in June from 52.9 in May, with the decline larger than the historical May-to-June average decrease of 1.4pp.

We expect the official non-manufacturing PMI to fall to 49.8 in June from 50.0 in May, as suggested by lackluster tourism spending during the Dragon Boat holiday. We believe household catering and entertainment demand could be further weighed down by ongoing K-shape property market and stock market rally amid the AI boom.

We expect the RatingDog manufacturing PMI (formerly Caixin manufacturing PMI), which surveys more SMEs and exporters in the eastern coastal region of China, to remain elevated at 51.5 in June, albeit down from 51.8 in May, supported by robust exports driven by the AI supercycle. Growth in imports from Korea accelerated further to $86.9\%$ in 1-20 June from $80.9\%$ in May, and growth in exports to Korea surged to $41.1\%$ from $33.2\%$ during the same period.

## Industrial production growth in June: 4.5% y-o-y (May: 4.5%)

We expect industrial production (IP) growth to remain subdued in June, unchanged from $4.5\%$ y-o-y in May, as supply disruptions from the Middle East conflict remain largely in place and as one additional working day should provide a modest technical lift. There are 21 working days this June, compared to 20 a year ago.

High-frequency data related to the oil and chemical industries

\- The operating rate of Shandong oil teapot refineries slipped further to $48.8\%$ at end-June from $53.6\%$ in late May and $60.0\%$ in late April. Its monthly average operating rate fell further to 1.4pp above last year's June levels from 6.2pp above in May, 7.0pp above in April and $9.7\%$ above in March.

\- The operating rate of purified terephthalic acid (PTA) factories rebounded to $62.3\%$ at end-June from $55.5\%$ at end-May, while its monthly average operating rate dropped to 15.0pp below last year's June levels from 9.6pp below in May.

\- The operating rate of polyester filament yarns (PFY) factories in Jiangsu and Zhejiang provinces dropped to $73.8\%$ at end-June from $79.2\%$ at end-May, and its monthly average operating rate dropped to 16.4pp below last year's June levels from 10.3pp below in May.

\- The operating rate of asphalt factories dropped further to 17.3pp below last year's June levels from 14.6pp below in May.

## Other high-frequency data

\- The weekly operating rate of cement factories increased to 2.4pp above last year's June levels from 0.3pp above in May.

\- The weekly cement shipment-to-output ratio increased to 0.5pp above last year's June levels from 0.2pp above in May.

\- Growth in weekly steel rebar output at major steel mills increased to 1.5% y-o-y in June from -8.2% in May, while output growth of crude steel also increased to -2.9% from -4.4%.

\- Growth in the daily average volume of coal burned at power plants in eight provinces in South China moderated to 1.1% y-o-y in June from 2.6% in May.

Export growth in June: 16.2% y-o-y (May: 19.4%)

Import growth in June: 26.2% y-o-y (May: 27.4%)

Trade balance in June: USD111.3bn (May: USD105.4bn)

We expect export growth to remain elevated at $16.2\%$ y-o-y in June, slowing only moderately from $19.4\%$ in May, as we forecast persistently strong export momentum in the near term.

We expect import growth to edge down marginally to 26.2% y-o-y in June from 27.4% in May, driven by a higher base and strong price effects. We also expect the previous surge in global crude oil and natural gas prices to continue feeding into China's import data in June, given the approximate, 20-day shipping window from the Persian Gulf to China. We do not expect the recent pullback in crude prices to be reflected in June import data yet, although imports of crude in volume terms could remain highly depressed. Additionally, ongoing price increases across a range of semiconductor products – particularly memory chips – are adding further upward pressure to import values.

As a result, we expect the trade surplus to widen to USD111.3bn in June from USD105.4bn in May.

## Higher-frequency trade-related data

According to the Ministry of Transport, growth in weekly container throughput at major ports edged up marginally to 4.3% y-o-y on a month-to-date basis (as of 21 June) from 4.2% in May.

DM manufacturing PMIs remain generally strong, despite some marginal pullback. The manufacturing PMIs for the US and Japan strengthened to 55.7 and 54.9, respectively, in June from 55.1 and 54.5 in May, while the euro area index edged down to 51.3 from 51.6.

On imports, the year-over-year change in the China Import Dry Bulk Freight Index (CDFI), which reflects freight rates for dry bulk cargo (including iron ore, coal, grain and nickel ore) imported into China, moderated to 48.4% y-o-y on a month-to-date basis in June from 76.3% in May. Brent crude oil price growth moderated notably to 21.8% y-o-y on a month-to-date basis in June from 68.3% in May but remains somewhat elevated.

## CPI inflation in June: $1.2\%$ y-o-y (May: $1.2\%$ )

We expect CPI inflation to remain flat at 1.2% y-o-y in June, unchanged from May, as a smaller drag from food prices is largely offset by less support from energy and core prices. In sequential terms, we expect CPI inflation to remain at -0.1% m-o-m in June, unchanged from May and its year-ago level.

For energy prices, easing geopolitical tensions in the Middle East drove down global oil prices, prompting the NDRC to cut retail petrol prices by RMB1,040/tonne in month-to-date June, against a price hike of RMB325/tonne last year. We expect domestic retail fuel price inflation to drop to -3.1% m-o-m in June from -0.3% in May. However, due to a low base from last year (-12.0% m-o-m in June 2025), fuel price inflation still provides support to headline CPI inflation in year-on-year terms, albeit to a lesser extent. We expect domestic retail fuel price inflation to remain elevated at 21.3% y-o-y in June from 25.6% in May, which could boost headline CPI inflation by 0.64pp, given its weighting of 3%.

We expect food price inflation to improve to -1.3% y-o-y in June from -1.7% in May. In sequential terms, it is likely to improve to 0.0% m-o-m in June from -0.4% in May, also above the -0.4% recorded a year ago. According to high-frequency data from the MARA, the Agricultural Product Wholesale Price Index 200 improved to -0.1% y-o-y in June from -0.7% in May. The improvement was mostly led by egg prices, while pork prices remain a drag. Amid sustained unprofitability caused the mass culling of older hens and delayed restocking, egg price inflation surged to 41.8% y-o-y in month-to-date June from 17.8% in May, boosting headline inflation by 0.25pp, given its 0.6% weighting in the CPI basket. On the other hand, pork price inflation remained deeply muted at -28.2% y-o-y in June, little changed from -28.5% in May, dragging headline inflation by 0.53pp.

We expect core inflation to drop to 1.0% y-o-y in June from 1.1% in May, driven by weak domestic demand as suggested by lackluster sales data during the 618 shopping festivals and the Dragon Boat holiday. This could be partly offset by the recent rise in consumer electronics prices, driven by surging chip prices amid the AI supercycle.

## PPI inflation in June: 4.0% y-o-y (May: 3.9%)

We expect PPI inflation to climb further to $4.0\%$ y-o-y in June from $3.9\%$ in May, due to a low base from last year, despite the retreat of global oil prices. On a sequential basis, PPI inflation is likely to turn negative at $-0.3\%$ m-o-m in June, down from $0.5\%$ in May but

above -0.4% recorded a year ago. As Brent oil prices retreated, support from prices of non-ferrous metals, Al-related products and new energy products is likely to remain intact.

Brent oil price inflation fell notably to 21.8% y-o-y in June from 68.3% in May, amid easing tensions in the Middle East. In sequential terms, Brent oil price inflation turned more negative, falling to -19.5% m-o-m in June from -10.4% in May. Falling oil prices should ease PPI inflation in oil-related sectors, which together comprise 14.1% of the PPI basket, according to our estimates.

Despite easing global oil prices, we see sustained drivers that support PPI inflation from non-ferrous metal prices and rising chip prices amid the AI boom. Global LME price inflation remained elevated at 38.4% y-o-y in month-to-date June (May: 41.7%); this should continue to support price inflation in non-ferrous related industries, which take up 7.3% of the PPI basket. Also, surging global chip prices should continue to push up PPI inflation in the computer, communication and other electronics equipment manufacturing sector, which accounts for 12.8% of the PPI basket.

Amid rising global demand for new energy products, prices of raw materials for solar panels and EV batteries remained elevated; this should provide support for PPI inflation in the electrical machinery and equipment manufacturing sectors, which account for 8.4% of the PPI basket.

## Retail sales growth in June: $0.9\%$ y-o-y (May: $-0.6\%$ )

We expect retail sales growth to remain soft at 0.9% y-o-y in June, little improvement from -0.6% in May, weighed down by payback effects from the scaled-back trade-in program, subdued consumer confidence and negative price effects from domestic fuel and consumer electronics, driven by imported inflation. By components, we expect retail sales growth in autos, catering and “merchandise excluding autos” of -16.0% y-o-y, 2.0% and -10.3%, respectively, in June from -16.1%, 0.6% and 3.3% in May.

On auto sales, according to early estimates from the CPCA, volume growth in passenger car retail sales is likely to remain subdued at -19.4% y-o-y in June (May: -22.1%). We expect auto sales to be the main drag for headline retail sales, due to the scaled-back trade-in program and the increase in the EV purchase tax to 5% from 0%.

For other components, growth in the catering sector is likely to remain soft, given the lackluster tourism revenue from the Dragon Boat holiday, but in year-on-year terms, it is likely to rebound slightly, as the new austerity rule rolled out last May significantly dragged down catering sales growth in June last year. Growth in merchandise sales excluding autos is likely to continue to fall back across major durable goods categories on the payback effect from the trade-in program. Households are also likely to cut spending on petroleum products and consumer electronics, given the rising prices led by imported inflation.

## FAI growth in June: -8.4% y-o-y (May: -10.7%)

## FAI growth in June: year-to-date: -5.3% y-o-y (May: -4.1%)

We expect FAI growth to rise slightly to -8.4% y-o-y in June from -10.7% in May, implying year-to-date growth of -5.3%. We see no material improvement in FAI growth in June, and the issuance of government bonds (both central and local) was again lower than the same period last year.

We expect fixed asset investment (FAI) growth to improve slightly to -8.4% y-o-y in June from -10.7% in May, which implies cumulative year-to-date growth of -5.3% for H1. Despite this modest monthl

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
