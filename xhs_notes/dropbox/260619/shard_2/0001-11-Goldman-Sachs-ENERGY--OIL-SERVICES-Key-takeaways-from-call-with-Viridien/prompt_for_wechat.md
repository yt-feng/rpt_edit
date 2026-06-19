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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

Conventional discoveries have remained low, with Oil & Gas capex/boe still c.40% below the peak and exploration down c.60%, tilting the sources of new reserves increasingly toward revisions and M&A, rather than organic, exploration-led additions. Total capex per barrel continued its downward trend to \$14.7/boe in 2024, down 39% from its \$24.2/boe peak in 2013. In particular, exploration capex was down 59% from its peak at \$1.8/boe in 2024.

Exhibit 4: Exploration capex was down 59% from its peak at \$1.8/boe in 2024  
Exploration capex per bboe per FAS69 data  
![](images/dde71319f245dc44472d977fb614a5a41921b6a6101f0bea853e6e55982ad479.jpg)

<details>
<summary>bar chart</summary>

| Year | Exploration capex ($/boe) |
| ---- | -------------------------- |
| 1986 | 1.75                       |
| 1987 | 1.35                       |
| 1988 | 1.55                       |
| 1989 | 1.50                       |
| 1990 | 1.80                       |
| 1991 | 1.70                       |
| 1992 | 1.50                       |
| 1993 | 1.30                       |
| 1994 | 1.25                       |
| 1995 | 1.30                       |
| 1996 | 1.45                       |
| 1997 | 1.85                       |
| 1998 | 2.00                       |
| 1999 | 1.25                       |
| 2000 | 1.35                       |
| 2001 | 1.45                       |
| 2002 | 1.30                       |
| 2003 | 1.40                       |
| 2004 | 1.50                       |
| 2005 | 1.80                       |
| 2006 | 2.40                       |
| 2007 | 2.85                       |
| 2008 | 3.35                       |
| 2009 | 3.00                       |
| 2010 | 3.15                       |
| 2011 | 3.75                       |
| 2012 | 4.50                       |
| 2013 | 4.75                       |
| 2014 | 4.00                       |
| 2015 | 2.65                       |
| 2016 | 1.75                       |
| 2017 | 1.85                       |
| 2018 | 1.90                       |
| 2019 | 1.85                       |
| 2020 | 1.75                       |
| 2021 | 1.85                       |
| 2022 | 2.15                       |
| 2023 | 2.25                       |
| 2024 | 1.85                       |
</details>

Source: Company data, GS Global Investment Research

2) The market is rewarding reinvestment again: After years of demanding capital discipline and cash returns, the market appears to be shifting back towards rewarding capex and growth. Across our integrated oil universe, companies with higher

reinvestment ratios (Capex/CFO) have outperformed lower-reinvestment peers by 14pp over the past 6 months. Among the supermajors, TotalEnergies (+30%) has outperformed Shell (+14%) and BP (+18%) in Europe; in the US the relationship is more pronounced over the last 12m while 6m shows

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
