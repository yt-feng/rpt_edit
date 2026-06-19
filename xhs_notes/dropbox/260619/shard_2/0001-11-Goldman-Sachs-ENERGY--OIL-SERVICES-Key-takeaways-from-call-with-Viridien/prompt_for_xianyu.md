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
ENERGY: OIL SERVICES

# Key takeaways from call with Viridien post EAGE conference: “Frontier Exploration is back”

The 86th EAGE Annual Conference & Exhibition was held in Aberdeen on 8–11 June 2026, bringing together the full seismic and subsurface supply chain. On 16 June, we hosted Viridien (ex-CGG) CFO Jerome Serve for a fireside chat to share feedback from the event and discuss the broader state of the seismic market post-consolidation. Key takeaways include:

1. EAGE 2026 was the strongest signal in years. Record attendance of >6k delegates, with C-suite engagement stepping up vs 2025, underpinned by reserve replacement and reserve life firmly back on the agenda and reinforced by post-war energy security concerns. This has not yet flowed into seismic revenues — 2026 budgets were locked pre-war — with the inflection expected by Viridien in 2027 (Equinor CMD +9% capex a directional positive); we see this as a disciplined multi-year up-cycle, not a repeat of 2010–15.  
2. The dominant theme was the return of frontier exploration. According to Viridien, historically \~80% of activity was near-field, but near-field alone is insufficient to offset falling reserve life; the last few months show a clear reopening of frontier work, with rising client interest across Uruguay, Equatorial Margin Brazil, Angola, Egypt, Liberia and a broadening GoA. Majors will need time to rebuild frontier expertise after years of underinvestment according to the company.  
3. Reprocessing-led demand was the clear second theme and plays directly to seismic companies. According to Viridien, it's clients' own budgets show more reprocessing in frontier basins, often ahead of drilling, as they look to lock up data early. Behavioural shifts reinforce the trend: prefunding traction is rising, exploration success rates remain low (\~20–25%, basin-dependent) so image quality remains the differentiator, and NOCs increasingly outsource the full image-to-prospect stack to seismic players rather than build it in-house.  
4. Vessel availability is not a constraint today according to the company; day rates stable but with upside if capacity tightens. Streamer fleet consolidated at \~16–17 active vessels (TGS/Shearwater dominant) with stacked capacity reactivatable on a lag; OBN supply is unconstrained but \~4–5x more expensive than streamer-equivalent. Pricing has not increased yet despite consolidation,

Michele Della Vigna, CFA

+39(02)8022-2242

michele.dellavigna@gs.com

GS Bank Europe SF - Milan

branch

Anastasia Shalaeva

+971(4)214-9908

anastasia.shalaeva@gs.com

GS International

Will Chen

+971(4)214-9942 | will.y.chen@gs.com

GS International

Yulia Bocharnikova

+44(20)7051-6299

yulia.bocharnikova@gs.com

GS International

Quentin Marbach

+44(20)7774-7644

quentin.marbach@gs.com

GS International

with Viridien expecting streamer cost inflation to pass through into MCL pricing and OBN pricing to fall over time as deployment efficiency improves.

## 5. AI in seismic is accretive, not substitutive — image quality remains the moat.

Viridien believes that AI cannot solve the physics-based wave equations underpinning imaging; HPC capacity is the structural moat. Its contribution is concentrated in denoising, workflow acceleration and faster delivery, while end-clients increasingly layer their own AI on top of the underlying images, raising rather than commoditising the value of high-quality data. Disintermediation risk is low, in Viridien's view, as its in-house computing still requires data from the multi-client library, while NOCs and independent players will likely choose to rely on seismic player's specialized capabilities.

## Key takeaways from the fireside chat with Viridien post EAGE conference

EAGE 2026 was the strongest signal in years; exploration is “back, or soon to be back”.

Record attendance of >6k delegates (all-time high per organisers), with EAGE the largest seismic event globally alongside IMAGE in Houston, and all key service players and key clients were present.  
C-suite engagement stepped up vs 2025, with the improved sentiment underpinned by reserve replacement and reserve life firmly back on the agenda and reinforced by post-war energy-security concerns.  
This has not yet translated into seismic companies revenues, as 2026 client budgets were locked pre-war, with the inflection expected by Viridien in 2027 budgets (Equinor's CMD +9% capex guide a directional positive).

Main themes: return of frontier exploration, with reprocessing-led demand a clear second and regional interest broadening

- Appetite for genuine frontier work has clearly increased: According to Viridien, historically \~80% of activity was near-field; near-field exploration continues but is not sufficient to offset the falling reserve life, with it’s clients’ own budgets showing more reprocessing in frontier basins, often ahead of drilling, as they look to lock up data early. The last few months show a genuine return to frontier, per Viridien, but majors have lost frontier-basin expertise after years of underinvestment and will need time to rebuild it.  
Viridien flagged rising client interest across Uruguay (Namibia analogue), Equatorial Margin Brazil (completely unexplored, massive area, Petrobras drilling its first well), Angola (multiple majors back in), Egypt, Liberia, and a broadening US Gulf of America as more independents return — with MoUs being signed including with countries Viridien had never engaged before.  
Viridien believes its Earth Data library is best positioned in Norway, GoM and Brazil, all currently seeing significant client interest.  
Reprocessing is the near-term workhorse and plays directly into Viridien's edge (proprietary AI + in-house HPC), offering clients a cheaper route to better basin understanding than new acquisition.

Cycle outlook: a disciplined multi-year up-cycle, not a repeat of 2010–15

■ Management was explicit and believes that the industry will not return to the spending exuberance of 10–15 years ago, when the prior cycle peaked at \~60 active streamer vessels — a level unlikely to be revisited. It believes clients are permanently more shareholder-return focused and selective.  
■ Management is convinced that 2027 budgets will be set materially higher, marking the inflection point for the new cycle.  
A sustained, multi-year up-cycle through the decade is plausible, per the company, supported by reserve-replacement pressure, frontier re-engagement, a rising

sovereign MoU pipeline, growing prefunding, and replacement-driven new streamer/OBN technology sales.

## Client appetite for seismic is shifting to reprocessing first, with a behavioural shift toward prefunding and outsourcing.

Viridien said that refunding traction is rising (the ability to assemble prefunded surveys is itself a signal of client intent), and the outsourcing trend is accelerating, with NOCs (e.g. ADNOC) increasingly handing the full image-to-prospect workflow to Viridien rather than building it in-house.  
Exploration success rates remain low (\~20–25%, basin-dependent), so image quality remains the differentiator.

## Vessel availability is not a constraint today; day rates stable but with potential for upside if capacity tightens

The streamer fleet is consolidated at \~16–17 active vessels, dominated by TGS and Shearwater (PXGEO, Dubai, Chinese players on the fringe); no issue sourcing vessels and stacked capacity can be reactivated (with a lag) if the market tightens, according to Viridien.  
- OBN is a different supply curve: no specialised vessels needed and competition small, but absolute price remains \~4–5x more expensive than streamer-equivalent; its clients want more OBN but are price-restrained, and the industry is working to reduce sensor deployment time.  
- Pricing has not increased yet despite consolidation; if streamer costs rise, Viridien will pass through into MCL pricing, while OBN pricing is expected to fall over time.

## AI in seismic is accretive, not substitutive — image quality remains the moat, and Viridien is positioned to capture it.

At the industry level, Viridien believes that AI cannot solve the physics-based wave equations that underpin imaging — those remain iterative, HPC-intensive problems — so HPC capacity is still the structural moat.  
AI's contribution is concentrated in denoising, data cleaning and workflow acceleration, while end-clients increasingly layer their own AI tools on top of seismic images to refine prospectivity — image quality is the binding constraint on the value those tools can extract, which raises (rather than commoditises) the value of high-quality underlying data.  
For Viridien specifically, AI is being deployed across its processing workflow and a new cloud delivery interface now ships terabyte-scale image volumes in \~1 day vs \~4 weeks historically, accelerating client re-engagement.  
Sophisticated clients combine Viridien images with their own interpretation tools; less sophisticated NOCs outsource the full image-to-prospect stack to Viridien, supporting the structural outsourcing trend.  
- Disintermediation risk is low, according to the company, as their in-house computing still requires data from the multi-client library, while NOCs and

## independent players will likely choose to rely on seismic player's specialized capabilities.

E&P spending cycle: the beginning of a new oil capex upcycle?

The seismic industry is an amplified derivative of the E&P capital expenditure cycle, in our view, with exploration expenses acting as one of the most volatile components of upstream budgets. The sector experienced a severe, multi-year contraction between 2014 and 2021, during which time the global seismic market shrank. The marine seismic industry has seen a c.85%-90% contraction in streamer fleet capacity since 2014.

## The revival of exploration

We are starting to see early signs of a revival in exploration activity, with both management commentary and analyst questions turning incrementally more constructive on new resource discovery, seismic work and frontier acreage. As shown in Exhibit 1, mentions of exploration-related themes—which troughed in 2020-22 following years of capital discipline—are now clearly inflecting upwards and approaching the high levels of 2014. This shift is consistent with a gradual rebalancing of capital allocation as balance sheets have strengthened and companies look to replenish resource bases after a prolonged period of underinvestment. While still early-cycle, the change in tone suggests that exploration is moving back up the agenda for the majors, supporting a recovery in seismic demand over time.

Exhibit 1: While still early cycle, the change in tone suggests that exploration is moving back up the agenda for the majors, supporting a recovery in seismic demand over time  
![](images/0b93c481dd89cedfa41d423ade9c42acfa5d43a3925d2957089f445944e507f2.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | Answer (mgmt Q&A) | Question (analyst) | 4Q rolling avg |
|---|---|---|---|
| 2010 | 31 | 25 | 42 |
| 2011 | 27 | 28 | 39 |
| 2012 | 50 | 35 | 60 |
| 2013 | 32 | 28 | 57 |
| 2014 | 21 | 38 | 46 |
| 2015 | 21 | 28 | 58 |
| 2016 | 18 | 25 | 41 |
| 2017 | 20 | 28 | 43 |
| 2018 | 15 | 18 | 33 |
| 2019 | 16 | 25 | 21 |
| 2020 | 12 | 15 | 17 |
| 2021 | 7 | 8 | 16 |
| 2022 | 8 | 9 | 9 |
| 2023 | 7 | 9 | 13 |
| 2024 | 30 | 30 | 30 |
| 2025 | 20 | 18 | 25 |
| 2026 | 30 | 35 | 51 |
Peak: 2014Q3 (84 mentions)
Oil price crash
Coverage (11 cos): XOM, CVX, COP, BP, RDSa, TOTF, OMVV, GALP, ENI, EQNR, REP.
</details>

Source: GS Data Works, Data compiled by GS Global Investment Research

We believe the sector is poised for a significant oil capex upcycle, similar to that of the early 2000s. With OPEC global spare capacity running down, US shale reaching maturity, and reserve life eroded by under-investment, we were already seeing increasing signs of a new oil capex cycle returning, similar to the 2000s. The escalation of geopolitical tensions in the Middle East since late-February has acted as a catalyst to

accelerate and bring forward what we see as a structural capex upcycle coming in 2027E, driven by the following:

1) The industry needs to re-invest in reserve life with more exploration capex: The resource life of Top Projects (recoverable resources/production) has fallen to c.20 years in 2026E from c.55 years in 2012, a 60% decrease over the past decade, as the industry has focused on short-cycle and brownfield (to support lower decline rates in the near term, at the expense of longer reserve life).

Exhibit 2: Industry reserve life was broadly flat at 10.2 years in 2024  
Reserve life (year) per FAS69 data  
![](images/59cc0bac2a85f656e80e0958af748556ae9a47f3abdceb125b0b4cd4b1b1f9ba.jpg)

<details>
<summary>bar chart</summary>

| Year | total reserves Life |
| ---- | ------------------- |
| 1986 | 16.0                |
| 1988 | 15.0                |
| 1990 | 16.0                |
| 1992 | 13.0                |
| 1994 | 13.0                |
| 1996 | 12.0                |
| 1998 | 13.0                |
| 2000 | 13.0                |
| 2002 | 13.0                |
| 2004 | 13.0                |
| 2006 | 13.0                |
| 2008 | 13.0                |
| 2010 | 13.0                |
| 2012 | 13.0                |
| 2014 | 13.0                |
| 2016 | 11.0                |
| 2018 | 11.0                |
| 2020 | 10.0                |
| 2022 | 11.0                |
| 2024 | 10.0                |
</details>

Source: Company data, GS Global Investment Research

Exhibit 3: Top Projects oil reserve life has fallen 35 years since 2012  
Top Projects reserve life, by year of report and breakeven  
![](images/01ef3660ed5dae2bebf6af934e71f4e42138ee8bfec4a1debb2b96c20e32b046.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year   | Producing | <$30 | $30-$40 | $40-$50 | $50-$60 | $60-$70 | $70-$80 | $80+ |
|--------|------------|------|---------|---------|---------|---------|---------|------|
| 2011   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 10   |
| 2012   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 12   |
| 2013   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 12   |
| 2014   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 16   |
| 2015   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 18   |
| 2016   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 18   |
| 2017   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 20   |
| 2018   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 22   |
| 2019   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 25   |
| 2020   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 25   |
| 2021   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 25   |
| 2022   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 25   |
| 2023   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 25   |
| 2024   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 25   |
| 2025   | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 25   |
| 2026E  | 14         | 6    | 4       | 4       | 4       | 4       | 4       | 25   |
The chart includes a line graph (Production) on the right Y-axis and a stacked bar chart (Reserve Life) on the left Y-axis. The legend indicates categories: Production (RHS). The X-axis represents years from '2011 to '2026E. Values are estimated based on the chart's axis labels.
</details>

Source: GS Global Investment Research

Conventional discoveries have remained low, with Oil & Gas ca

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
