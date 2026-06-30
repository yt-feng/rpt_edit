你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

We expect fixed asset investment (FAI) growth to improve slightly to -8.4% y-o-y in June from -10.7% in May, which implies cumulative year-to-date growth of -5.3% for H1. Despite this modest monthly improvement, we see no material recovery in FAI growth in June. The persistent weakness reflects subdued fiscal support, with issuance of government bonds – both central and local – again falling below year-earlier levels in June. This continued shortfall in bond issuance has constrained public investment spending, limiting the scope for a meaningful rebound in overall FAI activity.

## Property investment growth in June (single-month): -25.0% y-o-y (May: -24.3%)

Property investment growth in June (year-to-date): -18.2% y-o-y (May: -16.2%) We expect the deep contraction in property investment to extend in June, at -25.0% y-o-y, worsening from -24.3% in May. On high-frequency data, growth in new home sales by

floor space in the Wind survey of 20 major cities fell to -6.2% y-o-y in June from 0.0% in May. Growth in existing home sales volumes in a sample of 18 cities moderated to 12.8% y-o-y in June from 17.5% in May.

Amid the AI boom, existing home prices in tier-1 cities have shown further signs of stabilization, with three consecutive months of $0.4\%$ m-o-m gains, while a couple of tier-2 cities have improved mildly. Shanghai emerged as the best performer among the NBS 70 surveyed cities, with existing home prices rising by $0.6\%$ m-o-m in May and a cumulative gain of $1.9\%$ from the January lows. Shenzhen reported a $0.6\%$ gain in May, on par with Shanghai, backed by the latest easing of home purchase restrictions. Beijing and Guangzhou also posted consecutive mild price upticks. Hangzhou and Hefei are among the few tier-2 cities showing tentative positive market signals. By contrast, housing price declines worsened in most lower-tier cities, leading to a wider decline in national average housing prices again to $0.26\%$ m-o-m in May, after the price decline narrowed over four straight months to a $0.23\%$ decrease in April.

The home price data for May are largely in line with the Iceberg index, a leading indicator based on the lowest listing housing prices, which recorded a 0.3% m-o-m decline in May, following a 0.4% decrease in April. As the Iceberg index weekly data indicated a decline of 0.4% m-o-m in the first two weeks of June, we see a limited rebound in June.

# Aggregate financing (AF) in June: RMB3,477bn (May: RMB2,026bn)

New RMB loans in June: RMB1,647bn (May: RMB520bn)

Outstanding AF growth in June: 7.4% y-o-y (May: 7.7%)

## Outstanding RMB loan growth in June: $5.3\%$ y-o-y (May: $5.5\%$ )

M2 growth in June: 8.4% y-o-y (May: 8.6%)

We expect credit growth – measured as the year-on-year growth in outstanding aggregate financing (AF) – to decline further to 7.4% y-o-y in June from 7.7% in May, as strong corporate bond issuance was once again largely offset by weak new RMB loans. This is also likely to be weighed on by soft government bond issuance. Growth in outstanding RMB loans is also lik

[中间内容因长度限制已省略]

34. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

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
