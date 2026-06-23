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
- 已识别机构名：`Bernstein`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
India Autos

# India Autos: Beyond E20 - What ethanol can and cannot deliver

![](images/cbbbd4f1bf62bd5496e23a927ec479fb39c0480808732787c74eb535a6213034.jpg)  
Venugopal Garre  
+65 6326 7643

venugopal.garre@bernsteinsg.com

![](images/103ce9d4890f045b31b1db90b1d3a121f36fc10a31beb39c30c8faefe14078fe.jpg)

Param Shah

+91 226 842 1417

param.shah@bernsteinsg.com

India crossed the 20 percent ethanol blending milestone in late 2025, making E20 its standard petrol grade about five years ahead of plan. The obvious next question is how much further this programme can go. Can it move to E25 or E27, and then beyond to flex-fuel vehicles and E85? More importantly, is the incremental reduction in crude imports worth the cost and complexity of building an entirely new fuel value chain?

We separate our arguments into two halves. First half - stretching the blend from E20 toward E25 or E27 by 2030 is directionally sensible but hard. Over 80% of vehicles on Indian roads are built for E10. Current E20 is already triggering mileage losses and fuel-system complaints in legacy vehicles, and Govt. has only just assigned ARAI to study E25's impact on existing fleet. The stretch is achievable for new vehicles, but for legacy fleet it is conditional on retrofit kits scaling or legacy fleet turning over faster vs current scrap rates.

The second half - going beyond the blend wall (E25 / E30) by building a national flex-fuel and E85 supply chain is a long industrial project whose payoff, when you model it, is small, increasingly duplicated by technologies arriving anyway, and justified mainly by a hedging logic that no longer fits India's moment. Battery costs are falling every year, EV TCO is converging on petrol, and charging infrastructure build out + range improvement are genuine advancements - the very alternatives that hedge oil dependence.

Feedstock is also a risk. India's ethanol comes primarily from sugarcane, molasses and maize - all hostage to water availability and hence monsoons. When a poor 2023 harvest forced distilleries to switch from sugar to grain, India briefly became a net maize importer paying foreign exchange for grain to make a fuel meant to save foreign exchange.

Having increased adoption of Flex fuel vehicles and E85 supply chain is attractive in theory - if crude prices spike, a country with flex-fuel cars can switch to cheaper ethanol and blunt the shock. But during normalcy, ethanol procurement costs for OMCs (INR 60-62/litre in a good monsoon) exceed the petrol it replaces (INR 55-58/litre at \$75/bbl crude). We modelled what a full flex-fuel push would deliver: even with aggressive adoption (new petrol PVs sales phased out by end of this decade, replaced by FFVs), stock petrol PVs would still make up 45-50% of the fleet by end-2030 (vs 65-70% today). The net crude-import saving from flex-fuel cars is around 1-2% of India's oil imports; overall savings reach \~4-5%, driven overwhelmingly by blending to E25-E27 and the rise of EVs, hybrids and CNG.

The global track record reinforces our scepticism. US built E85 infra and saw it languish at $<2\%$ of stations; China scrapped its ethanol mandate the moment grain turned scarce; Thailand's E85 demand collapsed when subsidies were cut in early 2026, with EVs stepping in. Only Brazil sustains high blends - but Brazil started in the 1970s long before EVs existed and has far more suitable conditions vs India.

Our verdict: India can stretch to E25-E27 by 2030. Going beyond would require FFVs and E85 value chain. We only see a \~5% crude imports savings by 2030 with both, >2/3rd of it from blending + EV, Hybrid, CNG adoption, <1/3rd from FFVs. Savings jump to 7-8% by 2035, and 10% by 2040. But with EVs, Hybrids, CNG taking off, a parallel supply chain is an expensive hedge whose moment has passed.

## BERNSTEIN TICKER TABLE

<table><tr><td></td><td colspan="4">22 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2026A</td><td>2027E</td><td>2028E</td></tr><tr><td>MSIL.IN (Maruti Suzuki)</td><td>O</td><td>INR</td><td>13,421</td><td>18,200</td><td>(43.7)%</td><td>INR</td><td>459.46</td><td>468.95</td><td>531.43</td><td>29.2</td><td>28.6</td><td>25.3</td></tr><tr><td>MM.IN (Mahindra &amp; Mahindra)</td><td>O</td><td>INR</td><td>3,063.40</td><td>4,200.00</td><td>(51.7)%</td><td>INR</td><td>126.00</td><td>148.62</td><td>168.58</td><td>24.3</td><td>20.6</td><td>18.2</td></tr><tr><td>HMCL.IN (Hero MotoCorp)</td><td>M</td><td>INR</td><td>4,983.70</td><td>5,010.00</td><td>(32.2)%</td><td>INR</td><td>269.77</td><td>273.44</td><td>313.43</td><td>18.5</td><td>18.2</td><td>15.9</td></tr><tr><td>EIM.IN (Eicher Motors)</td><td>M</td><td>INR</td><td>7,639.50</td><td>7,000.00</td><td>(11.8)%</td><td>INR</td><td>203.46</td><td>227.92</td><td>266.94</td><td>37.5</td><td>33.5</td><td>28.6</td></tr><tr><td>BJAUT.IN (Bajaj Auto)</td><td>O</td><td>INR</td><td>10,191</td><td>11,500</td><td>(26.4)%</td><td>INR</td><td>386.25</td><td>409.45</td><td>471.05</td><td>26.4</td><td>24.9</td><td>21.6</td></tr><tr><td>TVSL.IN (TVS Motor)</td><td>M</td><td>INR</td><td>3,488.70</td><td>3,460.00</td><td>(23.8)%</td><td>INR</td><td>76.97</td><td>100.78</td><td>118.73</td><td>45.3</td><td>34.6</td><td>29.4</td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,072.31</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Our assessment of the ethanol blending programme points to meaningful execution challenges on two fronts. First, scaling the ability of passenger vehicles to handle higher blends, particularly within the existing fleet, remains uncertain. Second, sustaining higher blend levels on the feedstock side is constrained by structural dependence on monsoon-driven agricultural output.

We believe the impact on reducing fuel imports is likely to be limited over this decade. At the same time, there is a risk that policy and capital allocation shift toward extending legacy fuel technologies that may become less relevant over time, given the parallel evolution of electrification, hybrids and alternative fuels.

From a stock market perspective, the direct implications for the OEM supply chain appear modest. However, there could be indirect benefits for select players such as Maruti (rated Outperform), which remains relatively underpenetrated in electric vehicles. A stronger ethanol pathway may help bridge this gap by supporting its positioning in internal combustion and hybrid segments.

## INDIA HAS FINISHED THE EASY PART - BLENDING TILL E20

The first thing to understand about India's ethanol programme is why it succeeded so fast because the reasons are precisely why the next leg is hard. Blending rose from under 2% a decade ago to 20% in 2025 (Exhibit 1), ahead of every official timeline, on three favourable conditions: the blend went into engines India already owned, the feedstock came from crops India already grew, and the consumer was asked for nothing. A programme that asks nothing of anyone scales easily.

It was not entirely costless. The government puts the mileage loss at E20 at 1–6%, but a meaningful share of owners of pre-2023 vehicles report closer to 10%, alongside complaints of corrosion and fuel-system wear. The political signal is real - and every step up the blend ladder sharpens exactly these complaints.

But the issue starts even before the blend wall. More than 80% of petrol vehicles currently on Indian roads were manufactured before April 2023 and are only E10-compliant; E20 alone is already triggering rubber seal degradation, fuel pump complaints and mileage losses of 6–10% in legacy vehicles - issues that sharpen materially with every percentage point higher.

EXHIBIT 1: India's current capacity far exceeds the demand for ethanol (20bn litres of capacity vs \~11 bn litres of consumption)  
![](images/c1c939061da777137e0ec818d652eae872763b36238905bc38ba5ba3366b04e5.jpg)  
MoPNG, Bernstein analysis and estimates

## ETHANOL STOPS NEAR E25/E27 AND THAT IS THE CEILING

There is a physical ceiling to how much ethanol a conventional petrol engine can accommodate, and it is not a question of policy ambition. Ethanol contains roughly 65 to 67 percent of petrol's energy by volume, is hygroscopic, and can be corrosive to materials that petrol typically does not affect. At low blend levels, these properties have limited impact. As the blend rises, however, the effects become progressively more significant. Both global experience and India's own engineering standards converge on a threshold of around 20 percent for the existing vehicle base. This is the blend wall, and it is defined by underlying physical and chemical constraints rather than regulatory choice.

India does, however, have some room beyond this level. From April 2025 onward, all new vehicles are required to be equipped with E20-tuned engines. These engines are designed to take advantage of ethanol's higher octane rating through higher compression ratios, partially offsetting the energy penalty. As the fleet gradually transitions, the tolerable blend level can edge higher, which forms the basis for a measured progression toward E25, and potentially E27, by 2030.

The regulatory framework to support this transition is already taking shape. Fuel specifications up to E30 have been notified, and excise duties have been adjusted to support higher blends. However, this framework remains largely regulatory rather than mechanical. The underlying question is one of fleet readiness. The government's recent decision to task ARAI with a 60,000 to 70,000 kilometre durability study on the impact of E25 on existing E10 and E20 vehicles reflects a clear recognition that moving from E20 to E25 is a meaningful technical step, not a routine extension.

Until these results are available, and until either retrofit solutions scale efficiently or original equipment manufacturers upgrade a much larger share of the vehicle base, the transition remains uneven. More than 80 percent of the current fleet is still not fully E20-optimised. In this context, E25 appears achievable for new vehicle sales, but considerably more challenging across the existing stock. We therefore view E25 as a credible base case for new additions to the fleet, but only a conditional outcome for the broader parc. That outcome depends on either the rapid scaling of retrofit ecosystems or a faster-than-expected turnover of legacy vehicles, which current scrappage trends do not yet support.

EXHIBIT 2: Fuel Properties E0 to E100: The physics are clear - energy density drops from 32 MJ/L at E0 to 21 MJ/L at E100, while the RON rises from 91 to 120. The jump from E20 to E85 is not incremental; it requires entirely new engine hardware, cold-start systems, and ECU calibration.  
![](images/1b8d2cbbb6c8fd5378eea533ed82f7da69110bd61ff7145e210de238f5e57739.jpg)  
Source: ARAI, News Articles, Bernstein analysis and estimates

## ETHANOL BLENDING REQUIRES WATER AND HENCE, IT IS ALSO INFLUENCED BY MONSOONS

India does not face a shortage of distillation capacity. Installed capacity stands at roughly 18 to 20 billion litres, well above the approximately 11 billion litres required for E20. Capacity is not the constraint. If anything, the system is operating with surplus capacity. The real limitation lies in sustainable feedstock. Independent estimates place this at around 6 to 10 billion litres, while the government's more optimistic assessment is about 13.5 billion. This gap is critical. It is the difference between a view where E20 already represents the practical ceiling and one where E25 still offers headroom. The answer is not fixed. It shifts each year with rainfall patterns and water availability.

The events of 2023 illustrate this dynamic clearly. A weak monsoon and drought-like conditions hit the key cane-producing states, with Maharashtra and Karnataka seeing yields fall sharply from 120 to 130 tonnes per hectare to closer to 80. As sugar availability tightened, the government restricted the diversion of sugarcane juice toward ethanol. Distilleries pivoted toward maize, but the outcome ran counter to the programme's intent. India, historically a maize exporter of 2 to 4 million tonnes annually, turned into a net importer for the first time in many years. By 2024, it was importing close to a million tonnes from countries such as Myanmar and Ukraine, even as maize-based ethanol became the most expensive option at roughly INR72 per litre. In effect, a programme designed to reduce oil imports ended up relying on imported grain.

ESY refers to Ethanol Supply Year (Oct-Nov)
Source: MoPNG, SIAM, News Articles, Bernstein analysis

The subsequent reversal in September 2025 reinforces the same point. With a recovery in the monsoon, two consecutive good rainfall years replenished reservoirs and revitalized cane output. Sugar moved back into surplus, and cane juice and molasses returned to the ethanol stream in large volumes. The key takeaway is not about whether the system is cane-led or grain-led. It is neither in a structural sense. It is fundamentally driven by water availability. As blending targets rise, the system becomes increasingly exposed to a single weak monsoon year.

This vulnerability is amplified by India's underlying water constraints. The higher the blending ambition, the more sensitive the programme becomes to rainfall variability. At elevated blend levels, even one year of poor rainfall can disrupt the balance, forcing a shift toward imports and undermining the programme's core objective.

EXHIBIT 3: Shift in ethanol feedstock mix showing a temporary pivot toward maize during ESY'24–ESY'25 amid sugarcane shortages, with a rebalancing back to cane-based sources following improved availability and policy easing

![](images/4a5e91b52fd794dfd53fadf2a91c2d5c3e3e19e667af1af6f863ea91224a17fe.jpg)

EXHIBIT 4: Ethanol cost trends across feedstocks, highlighting a temporary surge in maize-based ethanol prices during the inversion phase- driven by drought-led sugarcane shortages in Maharashtra and Karnataka  
![](images/80242fc52d539c7fddd1b74f2850466cbc2a60a18c8ad03bc83657b05e152b90.jpg)  
Source: MoPNG, SIAM, Bernstein analysis

EXHIBIT 5: Water requirement is extremely high across ethanol feedstocks highlighting a key sustainability concern.  
![](images/2d676e7c40a7adc3a8a70db0b6fc0a170439c89232df623b694586ec98365edb.jpg)  
Source: Niti Aayog 2021, News Articles, Bernstein analysis

EXHIBIT 6: India has a 4.11 water stress score on a scale of 1 (low stress) to 5 (extremely high stress) vs Brazil's 1.04  
![](images/e1a874f9411ae3840698c48b42063738897c6b6fedc8a333440e71becb17f4d5.jpg)  
Source: World population review 2023, Bernstein analysis

## ETHANOL IS NOT CHEAPER THAN PETROL - SO THE CASE FOR GOING FURTHER RESTS ON ONE IDEA: A HEDGE

Confront the fact that quietly undermines the economic premise. At \~\$75 a barrel, a litre of crude costs India about INR 45, and a litre of petrol costs around INR55–58 to make before tax. A litre of ethanol is procured at about INR60–62 today on the cane-led mix, and rose above INR71 during the grain pivot. On every comparison that matters, ethanol costs as much as or more than the petrol it displaces, before a rupee of tax - set aside the more volume requirements due to mileage loss.

Strip away the rhetoric and one serious answer remains for why to push further at all: a hedge. Brazil's genius is to let the anhydrous blend float and to put flex-fuel in 90% of its cars, so drivers switch to ethanol en masse when crude spikes and petrol turns dear, then switch back when crude falls. When the Strait of Hormuz crisis drove crude above \$100 in May and June 2026, a country with Brazil's fleet could have leaned on ethanol precisely when oil turned expensive. We take this argument seriously - it is the strongest case for a flex-fuel future. But the question the rest of this report asks is not whether the hedge has value, but whether it is worth what India would have to spend to build it.

Mileage loss with increasing ethanol blend

EXHIBIT 7: Mileage loss due to increasing ethanol blend % as per govt studies; however consumers seem to report more mileage loss than the below estimates

![](images/71ecf36040d647b972a6d2b106065af4bc6e661c861936216b5c603d1ddc6440.jpg)  
Source: ARAI, Niti Aayog, Bernstein analysis and estimates

## THE HEDGE PAYS ONLY IN A SPIKE - AND BRAZIL BUILT IT OVER FIFTY YEARS, BEFORE ELECTRIC CARS EXISTED

Grant the hedge its due, then weigh it honestly. The first cut: the hedge pays only in a crude spike. Because ethanol is not cheaper than petrol at ordinary crude prices, the flex driver switches to ethanol only when oil climbs high enough that petrol's making-cost finally exceeds ethanol's. That is a real but occasional event - tail-risk insurance, not an everyday saving. For most of any given decade, with crude in the \$60–80 range, an Indian flex fleet would run mostly on petrol, exactly as Brazil's does in cheap-oil years. You would have built an entire parallel fuel system to capture a benefit that materialises in the minority of years when oil spikes.

The second cut is about timing. Brazil began building this hedge in 1975 with Proálcool (short for Programa Nacional do Álcool - National Alcohol Program), at a moment when there was no alternative to oil for a car - no EVs, no lithium-ion cost curve, no charging networks. If you wanted to insure a transport system against oil, home-grown ethanol was the only instrument available. The hedge made sense because it was the only hedge on offer.

That is no longer true, and it is the heart of our scepticism. India in 2026 has alternatives Brazil in 1975 could not imagine. Battery costs are falling year on year; strong hybrids cut petrol consumption 30-40% with no new fuel and no new infrastructure; CNG penetration is rising across the fleet. Each of these reduces oil dependence - the very thing the ethanol hedge is for and several decarbonise more durably as the grid greens. The opportunity cost of a single-purpose E85 supply chain is everything that same capital could do to accelerate these alternatives.

## WE MODELLED IT: EVEN PHASING OUT EVERY PETROL CAR BY 2030 BARELY IMPACTS CRUDE IMPORTS

This is the calculation that should anchor the investment decision. We built a stock-and-flow model of

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
