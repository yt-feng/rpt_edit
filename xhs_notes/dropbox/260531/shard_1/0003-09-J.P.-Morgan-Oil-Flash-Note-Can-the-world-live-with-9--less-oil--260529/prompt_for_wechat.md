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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
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
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Oil Flash Note

Can the world live with 9% less oil?

We spent last week in China, and the most striking takeaway from our meetings was not simply that oil demand has fallen. It was that it may have dropped by as much as 9% or 1.5 mbd—abruptly, unexpectedly, and with remarkably little visible disruption.

The sharpest hit has been in petrochemicals, but the weakness has spread to transportation fuels like gasoline and diesel. The decline does not appear to be the product of a formal government conservation campaign. There were no conspicuous appeals to save energy, no major limits on mobility, and no sense of crisis in daily life. Instead, it looks like consumers have made a quiet economic choice. Faced with higher gasoline, diesel and airfare, many seem to have shifted away from oil-based transportation toward cheaper, lower-carbon alternatives: electric buses, gas-powered trucks, subways, electrified high-speed rail, and electric taxis.

Feedback from Europe tells a similar story. Unlike 2022, when the energy shock registered as an acute macroeconomic crisis, this oil shock has, so far, felt oddly more manageable, even as it marks the largest disruption to oil markets on record. Even with oil prices nearing \$120 a barrel in April and May, electricity prices across most European countries continued to slip into negative territory, pushed down by massive surges in solar and wind generation.

This is not to suggest that the adjustment has been painless everywhere. Globally, we track demand losses of 2.8 mbd in March, 4.3 mbd in April, and 5.6 mbd in May, while acknowledging extremely limited visibility in parts of Africa and Southeast Asia. Roughly 40-60% of the decline reflects weaker petrochemical feedstock demand, with the remainder coming from transport fuels. Even so, the broader impact on global economic activity has been relatively contained: our economists have trimmed global growth by only about 24 basis points in 2026, while raising inflation by around 100 basis points.

Nor has China been immune, despite the presumed availability of large stocks of petrochemicals. China's economic growth weakened sharply in April, and high-frequency data suggest that softness carried into May. Industrial activity slowed, while nearly every segment tied to domestic demand weakened materially. Even so, China's shift toward alternative energy systems may have helped the country absorb the shock with far less pain than its roughly $70\%$ oil-import dependence alone would imply.

# Global Commodities Research

# Natasha Kaneva

(1-212) 834-3175

natasha.kaneva@JPM.com

# Lyuba Savinova

(1-212) 270-3781

lyuba.savinova@jpmchase.com

# Artem Fakhretdinov

(1-212) 272-1839

artem.fakhretdinov@JPM.com

JPM Chase Bank NA

Crucially, what we are seeing in China does not look like an outright collapse in activity. Road transport indicators have shown little material weakening beyond normal seasonality, yet gasoline and diesel demand fell sharply in April and May—a divergence that only makes sense if the miles are still being driven, but increasingly in different powertrains. Consistent with that interpretation, China’s highway EV charging volumes climbed to record highs during the Spring Festival holiday week in late February and then surged 55.6% year-on-year on the first day of the five-day May Day holiday in early May. China’s Ministry of Transport estimates that an average of 15.4 million electrified vehicles traveled during the May holiday period, accounting for a massive 24% of all vehicles on the road—up 33% from a year earlier.

A similar pattern is emerging in aviation. Chinese air travel is running $6.5\%$ below last year's pace so far in May, with the bulk of the weakness concentrated in the domestic market. Here again, the story may be substitution rather than retrenchment. Over the May Day holiday, China saw a record 1.52 billion inter-regional passenger trips—up $3.5\%$ from the same period a year earlier. Road travel remained the dominant mode, also up $3.5\%$ year on year, while rail trips rose $4.6\%$ and civil aviation fell $5.7\%$ . Against this backdrop, China's high-speed rail network is often faster, cheaper, and increasingly the default choice for domestic travel. In effect, some of the jet fuel demand may now be shifting to the power grid via electrified rail, rather than disappearing altogether.

Taken together, developments in China and Europe raise a larger set of questions: how much of today's demand weakness is likely to reverse once conditions normalize, and how much reflects a more durable shift in consumption? Put differently, could the world actually function with something like $9\%$ less oil?

The answer is nuanced. A decline of that magnitude would typically read as recessionary—especially when set against the Global Financial Crisis, when the world’s oil demand fell by only about 2% at its trough. But if a meaningful share of the reduction comes from substitution rather than forgone activity, the macro signal is materially different.

Consider the mechanics. Despite the relative calm in broader markets, the physical supply shock itself has been immense. Supply losses linked to the closure of the Strait of Hormuz were severe and intensified further after the US blockade effectively halted Iranian oil exports. As a closed-loop system that must clear daily, the oil market can only adjust through some combination of inventory draws and demand loss. Supply to the market fell by roughly 12.6 mbd in March, 14.1 mbd in April, and 16.4 mbd in May. These losses were offset through a mix of inventory draws—about 3 mbd in March, 6.5 mbd in April, and 7.4 mbd in May—alongside demand declines of roughly 2.8 mbd, 4.3 mbd, and 5.6 mbd over the same months, respectively.

The lessons of the 1973 oil shock are instructive precisely because the world today looks fundamentally different from the one that entered the first oil embargo. In 1973, oil was deeply embedded across nearly every part of the global economy: electricity generation was heavily oil-dependent, vehicle efficiency was poor, public transportation infrastructure was limited, and large-scale alternatives barely existed. The result was a severe macroeconomic shock that triggered recession, inflation, industrial weakness, and a lasting restructuring of global energy systems.

Much of the modern energy system was built in direct response to those vulnerabilities. In the US, the crisis led to the creation of the Strategic Petroleum Reserve, the establishment of the Department of Energy, the introduction of fuel economy standards, and even the national 55 mph speed limit aimed at reducing gasoline consumption. Across Europe and Japan, governments accelerated the buildout of nuclear power, expanded public transportation systems, improved building insulation standards, and diversified away from oil in electricity generation. The crisis also reshaped industrial processes, encouraged smaller and more fuel-efficient vehicles, and ultimately reduced the share of oil in the global energy mix over the following decades (Figures 1 & 2).

This raises the key question for today: should we expect structural changes of similar magnitude from the current shock? Possibly yes, but the direction of change may be different. The 1973 crisis pushed economies to use energy more efficiently. Two major wars involving large oil producers over the past five years could accelerate something broader: the steady decoupling of economic activity from oil consumption itself.

\- Gasoline demand may prove to be one of the clearest examples of crisis-driven behavioral adaptation. When fuel is scarce and prices surge, consumers and firms often respond by accelerating changes already underway: efficiency improvements, modal substitution, and adoption of alternative drivetrains. China sits at the center of this dynamic. Even before the current shock, gasoline demand was on a structurally weaker trajectory as rapid EV adoption displaced incremental gasoline use. The crisis is now acting as an accelerant, reinforcing the shift through higher fuel costs, energy-security concerns, supportive policy, and the continued rapid expansion of charging infrastructure. We estimate China's gasoline demand destruction at about 180 kbd, and expect $70\%$ of that loss may not return even after markets normalize (Figures 3 & 4). The reason is simple: once consumers switch to EVs, the change tends to be sticky. Outside China, the structural effects are likely smaller but still meaningful. In Europe, new car registrations climbed to their highest level since 2019 in March, led by hybrids, which overtook diesel and petrol cars in late 2025. History suggests that past oil shocks often left lasting declines in gasoline demand, and this episode may prove no different. On that basis, we expect that some portion of the 900 kbd loss in gasoline demand may never fully return. Diesel shows a similar, if more uneven, risk profile. Part of the roughly 850 kbd decline in diesel demand may also prove durable, with the risk of permanent substitution concentrated in China (Figures 5 & 6).

- Petrochemicals are a harder case for substitution, because they run through supply chains in ways that are difficult to unwind. But even there, economies tend to adapt through efficiency gains, material substitution, and, at the margin, outright thrift. A small but telling example comes from Japanese snack maker Calbee. To help offset rising naphtha costs—a key petrochemical feedstock largely sourced from the Gulf—the company has temporarily shifted 14 of its iconic products (including potato chips) to black-and-white packaging. The move will likely be reversed once naphtha supplies normalize, not least because it imposes a real friction on consumers. Without the familiar color-coding (orange for lightly salted, green for seaweed), shoppers have to slow down and scrutinize labels, relying on text rather than instant visual cues to quickly grab their favorite flavors. That distinction matters. Measures like this reflect cost pass-through and short-term coping strategies more than a durable rewriting of demand. For that reason, we assume most of the roughly 2.4 mbd of lost petrochemical feedstock demand is likely to return as supply conditions normalize.   
- Jet fuel is the clearest case of the roughly 500 kbd demand loss that should mostly recover once supply chains stabilize. The pullback—concentrated in the Middle East and Asia—looks driven more by operational disruption than a lasting shock to mobility: airlines have rerouted flights, avoided certain Middle East refueling hubs, trimmed unprofitable routes, and run inventories more conservatively amid higher prices and elevated uncertainty. Long-haul aviation is also usually hard to substitute, particularly across Asia and on intercontinental routes. Scalable alternatives are limited, and sustainable aviation fuel remains a small, supply-constrained share of the mix. For that reason, our base case is that most of today’s jet fuel demand shortfall returns as availability normalizes. That said, higher fares and prolonged uncertainty could still leave structural fingerprints. They may accelerate the shift to remote business meetings, curb discretionary short-haul travel, and divert some passenger demand to rail where it is a viable substitute. Airlines, for their part, may prioritize profitability and load factors over rapid capacity expansion. The net result is that jet demand looks relatively resilient versus other refined products, with recovery likley, but with the key risk being a flatter long-term growth trajectory than the pre-crisis path.   
- Fuel oil demand destruction is estimated at 600 kbd so far, driven by weaker shipping and industrial activity, refinery disruptions, and lower oil-fired power burn. Unlike jet fuel, a meaningful share of this loss may not return even after crude flows normalize, because end users are adapting in ways that tend to persist. In shipping, higher bunker costs are accelerating slow steaming, route optimization, and fleet-efficiency upgrades. In power, governments are minimizing oil burn through conservation, grid optimization, faster renewable deployment, and in some cases greater coal use. In industry, firms are tightening processes, selectively electrifying systems, and reducing energy intensity (Figure 7). A relevant precedent is global shipping after the 2008 financial crisis and the IMO 2020 transition. Slow steaming began as a temporary response to higher costs, but became embedded as operators found they could materially cut fuel use with limited impact on supply chains, evolving into a structurally more fuel-efficient operating model for parts of the fleet (Figure 8). Because fuel oil is relatively easy to replace at the margin, even a partial step-down can become structural. The implication is an incomplete recovery and a faster long-term decline in fuel oil demand even once conditions stabilize.

Figure 1: Global energy stack   
![](images/d2206ffdb1213fee93abb63fb1f0a2cd5c8c460f5ea906f1d30a355bf95e84b9.jpg)

<details>
<summary>area_stacked</summary>

| Year | Oil | Natural gas | Coal | Nuclear | Hydro | Solar | Wind | Geo/Biomass/Other | Biofuels |
|------|-----|-------------|------|---------|-------|-------|------|-------------------|----------|
| 1965 | 70  | 30          | 40   | 10      | 10    | 5     | 10   | 5                 | 5        |
| 1969 | 80  | 40          | 50   | 15      | 10    | 5     | 10   | 5                 | 5        |
| 1973 | 90  | 50          | 60   | 20      | 10    | 5     | 10   | 5                 | 5        |
| 1977 | 100 | 60          | 70   | 25      | 10    | 5     | 10   | 5                 | 5        |
| 1981 | 110 | 70          | 80   | 30      | 10    | 5     | 10   | 5                 | 5        |
| 1985 | 120 | 80          | 90   | 35      | 10    | 5     | 10   | 5                 | 5        |
| 1989 | 130 | 90          | 100  | 40      | 10    | 5     | 10   | 5                 | 5        |
| 1993 | 140 | 100         | 110  | 45      | 10    | 5     | 10   | 5                 | 5        |
| 1997 | 150 | 110         | 120  | 50      | 10    | 5     | 10   | 5                 | 5        |
| 2001 | 160 | 120         | 130  | 55      | 10    | 5     | 10   | 5                 | 5        |
| 2005 | 170 | 130         | 140  | 60      | 10    | 5     | 10   | 5                 | 5        |
| 2009 | 180 | 140         | 150  | 65      | 10    | 5     | 10   | 5                 | 5        |
| 2013 | 190 | 150         | 160  | 70      | 10    | 5     | 10   | 5                 | 5        |
| 2017 | 200 | 160         | 170  | 75      | 10    | 5     | 10   | 5                 | 5        |
| 2021 | 210 | 170         | 180  | 80      | 10    | 5     | 10   | 5                 | 5        |
| Exajoules (Year) - Hydro / Solar / Biofuels (Geo/Biomass/Other) (Biofuels) (Geo/Biomass/Other) (Biofuels) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (Geo/Biomass/Other) (GeoBiomass/Other) (Geo/Biomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (Geo Biomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ Other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (Geo Biomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ Other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (GeoBiomass/ other) (Geo Biomass / Other) (GeoBiomass / Other) (GeoBiomass / Other) (GeoBiomass / Other) (GeoBiomass / Other) (GeoBiomass / Other) (GeoBiomass / Other) (Geo Biomass / Other) (GeoBiomass / Other) (Geo Biomass / Other) (Geo Biomass / Other) (Geo Biomass / Other) (Geo Biomass / Other)
</details>

Source: EI Statistical Review, JPM Commodities Research

Figure 3: China electrified vehicle sales   
LHS: Number of electrified vehicles sold. RHS: share of total vehicle sales   
![](images/c50e51aefce61cbf2c392f8454034999804d427271353f88c70566fa443564b2.jpg)

<details>
<summary>line</summary>

| Date   | Electrified vehicle sales | % of total sales (RHS) |
|--------|----------------------------|------------------------|
| Apr-26 | ~1.3M                      | ~60%                   |
| Oct-25 | ~1.8M                      | ~50%                   |
| Apr-24 | ~1.3M                      | ~45%                   |
| Oct-23 | ~1.2M                      | ~40%                   |
| Apr-23 | ~1.0M                      | ~35%                   |
| Oct-22 | ~800,000                   | ~30%                   |
| Apr-22 | ~600,000                   | ~25%                   |
| Oct-21 | ~400,000                   | ~20%                   |
| Apr-21 | ~200,000                   | ~15%                   |
| Oct-20 | ~100,000                   | ~10%                   |
| Apr-19 | ~50,000                    | ~5%                    |
| Oct-18 | ~30,000                    | ~3%                    |
| Apr-18 | ~20,000                    | ~2%                    |
| Oct-17 | ~10,000                    | ~1%                    |
| Apr-17 | ~5,000                     | ~0.5%                  |
| Oct-16 | ~3,000                     | ~0.3%                  |
| Apr-16 | ~2,000                     | ~0.2%                  |
| Oct-15 | ~1,500                     | ~0.1%                  |
</details>

Note: Electrified vehicles include 

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 29 May 2026 03:14 AM EDT

Disseminated 29 May 2026 07:00 AM EDT
"""
