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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Copper: Key Debates for GS 2026 Copper Week

We will host our annual virtual copper week from Jun 29th to Jul 1st. This is a C-level event and participating companies include: Antofagasta, Capstone, Ero Copper, First Quantum, Freeport, Hudbay, Lundin Mining, Southern Copper, Teck (not covered) and Vale Base Metals. Click here to register.

The key focus for us will be around companies' growth/project pipeline, as all the companies have either ongoing or planned projects. Investors questions have been around capex inflation risk, timeline update and funding/regulatory conditions.

In the short-term, cost headwinds related to energy and chemicals inflation are also on investors' minds, and this event will be an opportunity to understand how cost is performing against full year guidance, and whether we are past peak inflation risk. Structural challenges around grade decline, regulatory changes and replacement capex will also be debated.

## From a regulatory perspective, Latin America has navigated a round of

presidential elections, including in important copper producing countries Peru and Chile (Brazil due in 2H, Argentina in 2027). We will consult management regarding expectations on the regulatory environment following recent political changes.

On the copper side, investors have been recently concerned about rising inflation and macro uncertainties, the impact on interest rate expectations and ultimately GDP activity and copper demand growth. Elevated inventories in the US and tariffs discussion have also been key points of attention. We will gather mgmts' perspectives on copper supply/demand and pricing expectations.

We invite you to join us for this event; please see below for covered companies' investment thesis.

## Marcio Farid

+55(11)3371-4580 |
marcio.farid@gs.com
GS do Brasil CTVM S.A.

## Matt Greene

+44(20)7051-0489 | matt.greene@gs.com GS International

## Nick Cash

+1(212)357-6372 | nick.cash@gs.com GS & Co. LLC

## Emerson Vieira

+55(11)3372-0256 |
emerson.vieira@gs.com
GS do Brasil CTVM S.A.

## Henrique Marques

+55(11)3371-0778 | henrique.marques@gs.com GS do Brasil CTVM S.A.

## Riccardo D'Agata

+44(20)7051-0958 | riccardo.dagata@gs.com GS International

## Investment Summaries

## Antofagasta

ANTO (Buy) on (1) Copper gold leverage and scarcity premium: stands out as one of the few scalable, pure European copper gold equities, positioning it to capture the copper equity premium as investors seek targeted exposure to these commodities. (2) Proven execution and credible medium term growth targets: one of the few companies delivering growth in copper currently. The portfolio is anchored by Centinela and Pelambres, which together account for \~80% of current output and will drive \~95% of production growth this decade, on our estimates. (3) Centinela expansion is the key: The second concentrator (C2) is progressing as planned. The market is not fully appreciating the other brownfield growth options, including the C2E expansion. Together, C2 + C2E projects could position Centinela as one of the sector's largest, lowest cost operations, serving as a primary growth driver for the remainder of this decade.

## Capstone Copper

Capstone has among the highest operating leverage to copper prices, given its assets' high-cost base, so the stock could perform well in a copper price rally scenario. That said, the company's asset performance has also been volatile, increasing near term cash flow uncertainty and earnings momentum. We think the Santo Domingo project in Chile (sanctioning by late 2026) is a major milestone for the company to improve its overall cost positioning and medium-term FCF generation, but it is too soon to price it in, in our view. Moreover, we see shares implying a copper price of \$15,000/t (10% above spot), or \$14,400/t including Santo Domingo (5% above spot) and we think its FCF yield is not appealing in the near term (2-7% in 2026-27) given execution risks and higher operating leverage; for these reasons we are Neutral on CS shares.

## Ero Copper

We believe risk reward is less attractive due to limited copper price upside (GSe), some remaining operational uncertainties and less favorable valuation, driving our Neutral rating. We think Furnas project momentum is key to watch (link). Additionally, in terms of implied copper price, the company presents an above spot copper price of \$14,600/t (7% above spot), explained by the company's short-duration profile. On the other hand, the company's gold exposure, especially in 2026 and 2027 with its gold concentrate sales, could provide a boost of FCF and form a natural hedge to copper prices.

## First Quantum Minerals

First Quantum has a long track record of solid operational execution and successful delivery of brownfield/greenfield projects (S3 expansion, Cobre Panama). Moreover, the company has been making important balance sheet moves (e.g., gold stream agreement, asset sales, liability management), putting it into good shape for when/if the Cobre Panama mine restarts (not GS base case), which we believe is the stock's main catalyst. We think a Cobre Panama mine restart would place FM among the most attractive copper producers under our coverage (we see normalized FCFy 17% and EV/EBITDA at 3.2x on full restart by 2029 at spot). Notably, we have seen encouraging developments at Cobre Panama with the recent independent audit published and results broadly compliant (link) and the authorization by the government regarding the sale of stockpiled copper and the reactivation of its concentrator circuit (link). Additionally, a

resolution for Cobre Panama would allow the market to look forward and slowly price in growth optionally (e.g., the pending Taca Taca project in northwestern Argentina). We also see FQM shares implying a copper price of \$11,300/t including Cobre Panama, which is 17% below spot (more details here).

## Freeport-McMoRan

FCX offers best-in-class exposure to structural deficits in the copper market with supplemental gold exposure, in our view. We believe FCX's diverse geographic footprint provides the company with tailwinds ranging from low cost production to a hedge against US copper tariffs. We believe FCX is set to reaccelerate free cash flow as the company re-ramps its Grasberg mine, which is the lowest cost mine in the world per GSe (link), given its significant gold exposure. Currently Grasberg is targeted to be exiting FY2026 at a 60%-65% run-rate, then getting up to \~100% exiting FY2027. Additionally, in North America, FCX continues to progress on a leaching initiative which is set to both increase production volumes and meaningfully reduce cost/lb through 2030 as mix shifts. As a result of the incremental operating leverage plus elevated copper prices, we estimate FCX's gross profit/lb can increase from \$1.31 in 2025 to \$2.90 in 2027, an increase of 121%. As a result, our view is that we sit at an inflection point where the combined impact of Grasberg's ramp, leaching initiatives, and higher copper prices can result in EBITDA margin expansion from 34% in 2025 to 54% by 2028, with free cash flow accelerating significantly. Looking beyond the next 3 years, FCX has significant growth opportunities across each region. Across Baghdad, Safford/Lonestar, Kucing Liar, and El Abra expansions, FCX has projects capable of producing an incremental \~2bn lbs of copper which will be staggered in the early 2030s. We anticipate FCX will finance these organically while also continuing to return capital to shareholders. Despite the anticipated margin expansion, free cash flow acceleration and ample brownfield growth opportunities, FCX trades at a discount to its historical valuation as investors remain cautious on the ramp trajectory of the Grasberg asset. While we acknowledge the near-term risk, these lbs have only been pushed to the right and issues with Grasberg production are not permanent. Furthermore, the mining rights extension (Grasberg) signed earlier this year provides this asset with duration beyond 2041. As a result, we find the current risk reward provides an attractive entry point.

## Hudbay Minerals

We like HudBay's superior gold exposure (75%-50% of FCF generation in 2026-2028), which combined with Copper Mountain improvements supports attractive FCF (cumulative 26% in 2026-28). Copper is produced in stable jurisdictions (Canada, Peru) and there are significant near- and long-term growth options in the US (Copper World, the recently acquired Cactus and Mason projects — not GS base case). We estimate HBM's Copper World NAV at \$2.3B (18% of market cap at stake). Moreover, we see shares pricing in an implied copper price of \$13,500/t (1% below spot) and \$11,700/t including Copper World (14% below spot).

## Lundin Mining

LUN (Buy) on (1) relative Valuation: \~1x P/NAV (GSe) vs peers at >1x P/NAV (Visible Alpha Consensus Data). (2) leverage to copper: copper revenue now represents 85% of the total, one of the highest in the sector; (3) demonstration of strong operational performance, through continued production performance and cost discipline; and (4)

growth catalysts ahead: Vicuna FID in late 2026.

## Southern Copper

We recently upgraded SCCO to Neutral from Sell, mostly supported by a copper scarcity premium that we see as larger than ever due to expectations of structural supply/demand tightness. With SCCO being 1) the largest pure publicly traded copper producer, 2) with a great operational track record, 3) long life of mine reserves in friendly jurisdictions, 4) sizable and liquid trading in the US, and 5) the potential to grow production, we believe it deserves a large premium. Additionally, our copper down-cycle analysis points to SCCO's strong defensive positioning in a copper downturn given its low cost profile and relatively lower operating leverage. Lastly, the company's implied copper price stands at \$11,600/t, 15% below spot prices even though the company trades at a premium valuation.

## Vale

We think Vale has a solid strategy in place to balance iron ore portfolio and to grow on copper. Valuation is also attractive on a relative basis with Vale trading at 8% FCFy at spot vs. 4-6% for peers BHP/RIO. Vale also has a cleaner capital allocation strategy with limited M&A risk and improving operational performance. Vale stands out in terms of dividend carry and could be relatively defensive going into an electoral year in 2026.

## Valuation and Key Risks

## Antofagasta

Our 12-month TP of £46 is set at a 25/75 blend of 1.3x NAV and EV/EBITDA with an 8.5x target multiple.

Downside investment risks to our view and price target: (1) Commodity price movements — particularly unexpected US tariff related events (this is the key near-term risk to our call), (2) operational delivery in light of broader challenges facing the industry, (3) execution risk at Centinela — 50% complete; on track and budget, but unforeseen weather/safety/technical/design issues could delay the project and increase costs. And (4) value destructive M&A — we would view positively asset level transactions that unlock industrial synergies versus corporate transactions.

## Capstone Copper

We are Neutral-rated on Capstone Copper with a 12-month price target of C\$13/sh based on an equal-weighted blended DCF and 1-yr fwd EV/EBITDA target multiple of 7.1x, based on 5-yr historical avg + 1 std.deviation. Our DCF model assumptions include a 1.8 beta and 9.9% nominal WACC, based on 35%/65% D/E capital structure and 30% tax rate, consistent with the assumptions we used for other copper names in our coverage. We do not include Santo Domingo and other non-sanctioned projects into our DCF, an approach that is consistent with the assumptions we use for other copper names in our coverage.

Upside risks: 1) Given the company's high operating leverage, higher than expected copper prices could potentially lead to better than expected performance; 2)

faster-than-expected delivery of its Santo Domingo project (potential to reach 60% production growth; not in GS numbers).

Downside risks: 1) Slower-than-expected ramp up in Mantoverde's MVDP and eventually in Mantoverde's MVO could represent downside risk to production and costs. We also note potential capex overrun risks for MVO; 2) copper projects being approved and executed faster than expected, leading to lower copper prices and consequently lower earnings; 3) macroeconomic and tariff uncertainty which could potentially decelerate copper demand and impact Capstone's volumes; 4) regulatory environment could impact profitability in view of limited earnings' diversification (Capstone's assets are increasingly concentrated in Chile, >70%).

## Ero Copper

We are Neutral-rated on Ero Copper with a 12-month price target of \$31.0 based on our equal-weighted blended DCF/1-yr fwd EV/EBITDA target multiple of 6.5x. Our DCF model assumptions include a 1.4 beta and 10.7% nominal WACC.

Upside risks: 1) faster than expected turnaround on current operational issues at Tucumã and Caraíba mines; 2) higher-/longer-than-expected copper prices, which could potentially increase investor interest in copper assets; and 3) higher-than-expected gold prices, which could impact positively the company's profitability and increase interest from investors.

Downside risks: 1) production and cost disappointments during the Tucumã project ramp up; 2) lower-than-expected copper prices, which could potentially reduce investor interest in copper assets; and 3) lower-than-expected gold prices, which could impact the company's profitability and reduce interest from investors.

## First Quantum Minerals

We are Buy-rated on First Quantum with a 12-month target price of C\$44.0/sh based on our EV/EBITDA multiple-based valuation. Our multiple-based valuation consists of an equal-weighted blended multiple of 9.2x for 2026E and 2027E EV/EBITDA (5-yr historical avg + 1 std.deviation).

Downside risks: 1) Zambia currently generates $100\%$ of the company's EBITDA and asset concentration is now elevated (production issues in Zambia—e.g., energy availability, accidents—could significantly reduce the company's ability to honor cash obligations); 2) a longer-than-expected resolution at Cobre Panama could limit FM's ability to deleverage; 3) lower-than-expected copper prices could reduce investor interest in owning copper assets; and 4) a potential reopening of Cobre Panama with worse-than-expected economics could pose a risk.

## Freeport-McMoRan

Our 12-month price target of \$75 based on a through-cycle EV/EBITDA valuation (85%) and an M&A component (15%). Our fundamental valuation of \$72 is based on a 7.1x EV/EBITDA multiple to 2026-2028 average estimates. As for the M&A valuation, we apply a 9.0x multiple to FY2026-2028 estimates to arrive at an \$94 price target.

Risks. 1) Commodity prices lower than anticipated; 2) Higher energy costs; 3) Labor strikes in Indonesia and South America; 4) Mine operating disruptions resulting in less output than anticipated; 5) Higher than anticipated capital costs; 6) Cost reduction less than anticipated.

## Hudbay Minerals

We are Buy-rated on HudBay Minerals Inc with a 12-month price target of C\$39/sh with a PT methodology of an equal-weighted blended DCF/1-yr fwd EV/EBITDA target multiple of 5.2x. Our DCF model assumptions include a 1.2 beta (long-term historical average) and 8% WACC (nominal), based on 35%/65% Debt/Equity capital structure and 35% tax rate, all unchanged. We include in our DCF neither the NAV contribution of Copper World nor those from other non-sanctioned projects, which is consistent with the assumptions we use for other copper names in our coverage.

Downside risks: Downside risks to our price target and investment view include: 1) copper/gold prices below GS macro forecasts, mainly impacting the higher cost Copper Mountain asset, the principal FCF growth enabler before Copper World, 2) Peru's copper production decline if throughput ramp-up is not achieved/delayed as the high-grade Pampacancha deposit depletes, 3) failure to optimize Copper Mountain and expand mine throughput through the ball to SAG mill conversion leading to still-negative FCF generation, 4) Failure to extend Manitoba's hub gold production while capex is being disbursed for exploration activities, 5) Delayed sanctioning and/or capex overrun at Copper World, 6) Social unrest activities in Peru impacting copper production, 7) Wildfires in the Manitoba region impacting gold production.

## Lundin Mining

We are Buy rated on LUN.TO/LUMIN.ST with TP of C\$47.8/SEK311. Our TPs are based on a blend of 1x NAV and EV/EBITDA and a 10x target multiple on consolidated NTM EBITDA.

Key risks to our view and price target: (1) commodity price movements — in particular unexpected US tariff related events (we believe this is the key near-term risk to our call), (2) operational delivery in light of broader challenges facing the industry, (3) geopolitical risk in Argentina and/or unforeseen weather/safety/technical/design issues, which could delay the Vicuna project and increase costs, and (4) value destructive M&A — we believe asset level transactions that unlock industrial synergies would carry lower risks than corporate transactions.

## Southern Copper

We are Neutral-rated on SCCO with a 12-month price target of US\$176.24 based on equal-weighted DCF and 1-yr fwd EV/EBITDA target multiple of 13.7x, based on 5-yr historical avg + 1 std.deviation.

Upside risks: 1) Stronger than expected copper and/or by-products prices (namely silver and molybdenum), 2) Capacity to deliver better-than-expected costs despite the near-term production decline, 3) Faster-than-expected ramp-up of board-approved projects (namely Tia Maria) we consider in our model, 4) Southern Copper has a strong project pipeline for the coming years and some of these projects are still not board-approved and not considered in our model (El Arco, Los Chancas, Michiquillay, Ilo and Empalme smelters). A successful delivery of these projects at competitive costs could represent an upside risk. 5) Increased valuation premium due to scarcity value if

we see rotation out of other large cap pure copper producers into SCCO.

Downside risks: 1) Softer-than expected copper and/and by-products prices (namely silver and molybdenum), 2) Higher-than-expected costs due to operating deleverage as production decline, 3) Faster-than-expected mine depletion in select assets, 4) capex overrun on ongoing growth projects, mainly Tia Maria, 5) Political and regulatory risks in Mexico and Peru (ongoing reforms include shortening mining conce

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS.

This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
