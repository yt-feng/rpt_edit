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
US ECONOMICS ANALYST

# Mid-Year Inflation Outlook: Oil and AI vs. Wages and Rent

Core PCE inflation has reaccelerated this year, partly reflecting a combination of energy price passthrough, AI-related price pressures amplified by measurement issues, and financial services inflation driven by higher equity prices. In this week's Analyst, we take stock of the inflation outlook.

The US-Iran agreement has reduced upside risks to inflation from higher energy prices. Our commodity strategists lowered their oil forecasts to \$80 on average in 2026Q4 and \$75 in 2027 (vs. \$90 and \$80 previously), which implies about 0.2pp and 0.05pp less upward pressure on headline and core PCE inflation this year than our previous assumptions. In the near term, lower gasoline prices will translate into soft headline inflation prints in June, and our preliminary headline CPI and PCE estimates for June stand at -0.13% and 0.07%, respectively. The prices of several other non-oil Gulf exports have also declined meaningfully in recent days. We now estimate that commodity prices will deliver a roughly 0.4pp boost to year-over-year core PCE inflation through 2026Q4.

AI-related pressure on memory prices has pushed up computer software and accessories inflation, generating an especially large boost to core PCE because of measurement distortions. We expect monthly software and accessories inflation to slow from about 4-5% in recent months to about 0.6% by 2026Q4, reflecting a sharp slowdown in memory price inflation in recent months. We also expect higher memory prices to increase phone and computer inflation throughout 2026, though with smaller contributions to overall core PCE than software and accessories. Taken together, we estimate that AI-related price pressures will boost year-over-year core PCE inflation by about 0.4pp in December 2026 (with a peak of 0.6pp earlier in 2026H2, vs. 0.25pp already realized) and core CPI inflation by about 0.1pp.

We continue to have a benign outlook for underlying core inflation outside AI-related components and energy price passthrough. We expect rent growth to slow to below its pre-pandemic pace, reflecting soft new-tenant rent growth. We also expect slow nominal wage growth to put downward pressure on core nonhousing services inflation, though we expect healthcare inflation to remain around its current pace as prices continue to catch up to costs. Our indicators of persistent inflation risk and pipeline inflation pressures suggest that underlying inflation risk rose slightly in recent months but remains modest.

We forecast year-over-year core PCE inflation of 3.2% in December 2026,

Manuel Abecasis
+1(212)902-8357 |
manuel.abecasis@gs.com
GS & Co. LLC

followed by a slowdown to 2.2% by December 2027 as the AI and energy effects wane. In the near term, we expect strong increases in lagged equity prices to boost monthly core PCE inflation by 0.10pp in May and 0.05pp in June. We expect core CPI—which is less affected by AI measurement issues and stock market swings—to slow to 2.6% year-over-year by December 2026 and 2.2% by December 2027. We see risks to our forecast skewed to the upside on net, particularly if the situation in the Middle East deteriorates or if higher inflation expectations cause businesses to raise prices beyond increases in their input costs.

## Mid-Year Inflation Outlook: Oil and AI vs. Wages and Rent

Core PCE inflation has reaccelerated this year, partly reflecting a combination of energy price passthrough, AI-related price pressures amplified by measurement issues, and higher equity prices. In this week's Analyst, we take stock of the inflation outlook.

## Relief From the US-Iran Agreement

The US-Iran agreement and recent decline in oil prices have reduced upside risks to inflation. Our commodity strategists lowered their oil forecasts to \$80 on average in 2026Q4 and \$75 in 2027 (vs. \$90 and \$80 previously). In an upside scenario where the Strait of Hormuz remains disrupted through 2027, they expect Brent would rise to \$130 in 2026 and average \$105 in 2027. In a downside scenario with greater flows and stronger supply, they expect Brent would average just under \$70 in 2026Q4 and just under \$60 in 2027 (Exhibit 1).

Our strategists' new forecasts imply about 0.2pp and 0.05pp less upward pressure on headline and core PCE inflation by year-end than our previous assumptions. In the meantime, the recent decline in Brent and gasoline prices will translate into soft headline inflation prints in June, and our preliminary headline CPI and PCE estimates for the month stand at -0.13% and 0.07%, respectively.

Exhibit 1: Our Oil Strategists Now Expect Brent to Average \$80 in 2026Q4 and \$75 in 2027 (vs. \$90 and \$80 Previously)  
![](images/3d76d783d00cfafc1770818ab9a1376dafb75679579a4036f5f157af3af9c031.jpg)  
Source: GS Global Investment Research, Department of Energy

Beyond oil, we incorporate two other developments related to the conflict in the Middle East. First, the prices of non-oil Gulf exports like nitrogen and polyethylene have declined after rising sharply after the start of the war. Several products' prices are now close to their pre-war levels, though others remain elevated—particularly sulfur and ammonia (left side of Exhibit 2). Second, margins on refined oil products like jet fuel and gasoline rose significantly in May in the US, though they have since retraced some of their earlier increases (right side of Exhibit 2). Goods transportation costs also rose meaningfully in May, with the relevant PPI increasing a bit more than its typical relationship with oil prices would imply. Going forward, we expect refined product

spreads and goods transportation costs to normalize gradually as supply conditions in the Middle East improve.

Exhibit 2: Beyond Oil, the Prices of Several Gulf Exports Have Retraced From Their Recent Peaks, and Some Are Now Close to Pre-War Levels; US Refined Product Spreads Rose Sharply in May  
![](images/dd75a87d8e4289357c3616645fc3cd93100438fbf8dfa44a808b09b0415babdc.jpg)  
Source: GS Global Investment Research, Bloomberg

![](images/cd425e1d6e0d9e86e265494047d3575b1dbbbae95e9b588a51fc1655f97f2c98.jpg)  
Note: Weighted average refined product cash prices of gasoline, diesel, jet fuel, fuel oil, and naphtha. Weights based on relative demand for each product in 2025.

In Exhibit 3, we update our commodity price passthrough framework, including our oil strategists' latest forecasts, changes in goods transportation costs, and refined product spreads. We assume that refined product spreads gradually normalize over the next couple of months and that transportation costs behave in line with their usual relationship with oil. Taken together, we estimate that commodity prices will deliver a roughly 0.4pp boost to year-over-year core PCE inflation this year, with a smaller sequential boost in 2026H2.

Exhibit 3: We Estimate That Higher Commodity Prices Will Deliver a Roughly 0.4pp Boost to Year-over-Year Core PCE Inflation This Year, Which We Expect to Fade in 2027  
![](images/6feb997f83b7d953f1754026bcb66083526d3af736754b09d341aa6042a58191.jpg)  
Source: GS Global Investment Research

Exhibit 4 shows the implications of our commodity strategists' updated oil price scenarios for headline and core PCE inflation. In our baseline forecast, we expect year-over-year headline PCE inflation to start normalizing in June. In their upside scenario, we estimate a boost to core PCE inflation of 0.2pp and to headline PCE inflation of 1.1pp relative to our baseline. In their downside scenario, we estimate a drag on core PCE inflation of 0.1pp and on headline PCE inflation of 0.4pp relative to our baseline.

Exhibit 4: We Expect Headline Inflation to Slow From Here; Our Strategists' Upside Scenario Would Add Another 1.1pp to Headline PCE and 0.2pp to Core PCE, While Their Downside Scenario Would Subtract 0.4pp and 0.1pp  
![](images/792d3a13f2d822ba438eb7e3e6efa3605fe15760ee18d121944f0d34b7c37ef2.jpg)

![](images/39a6944898ab371fd96a773662c74443c59ef67e0347b7740804603046bf93e3.jpg)  
Note: Includes GS estimate for May PCE based on CPI, PPI, and import prices. Baseline assumes oil prices average \$88 in June and \$86 in July before declining to \$80 by 2026Q4. Downside scenario assumes oil prices average \$88 in June and \$84 in July before declining to \$70 by 2026Q4. Upside scenario assumes oil prices average \$88 in June and peak at \$130 in 2026 before declining to \$105 on average in 2027.  
Source: GS Global Investment Research, Department of Commerce

## The Inflationary Impulse From AI: Larger for PCE Than for CPI

The AI infrastructure boom led to a spike in memory prices as companies sought to buy chips to equip data centers. Prices for some types of memory rose 10-15x in a few months between 2025Q4 and 2026Q1 (left side of Exhibit 5). More recently, spot memory prices have remained very high relative to pre-2025Q4, but the pace of increases has slowed significantly. Contract prices faced by electronics manufacturers can lag spot prices by a few months, but the pace of increases has slowed for those too.

Higher memory prices have pushed up computer software and accessories inflation, generating an especially large boost to core PCE because of measurement distortions. While this component measures both software and accessories prices, in practice most of its variation can be explained by changes in memory prices that largely affect accessories costs (right side of Exhibit 5). We model computer software and accessories inflation using high-frequency memory prices, data from memory manufacturers, and our equity analysts' forecasts. Our model suggests that software and accessories inflation will slow from about 4–5% month-over-month in recent months to about 0.6% by year-end, reflecting the recent slowdown in memory price inflation.

![](images/788794d59e19c9b51df45b1840bfd5b9fe3d00759fec788a66d57a368a8992d2.jpg)  
Exhibit 5: Memory Prices Rose Sharply in 2025Q4 and 2026Q1 but Have Stalled Since; As a Result, We Expect Computer Software and Accessories Inflation to Slow in Coming Months  
Source: GS Global Investment Research, Trendforce, Department of Commerce

Computer software and accessories prices were flat in the May CPI report, suggesting that some of this slowdown is already underway. That said, this component is not seasonally adjusted by the BLS, and it has slowed by about 3pp relative to its prior trend in each of the last three Mays (reversing consistent accelerations earlier in the year), so much of the slowdown this May was likely residual seasonality. Going forward, we expect software prices to increase by 2-3% for the next couple of months and to slow further for the rest of the year.

We also expect higher memory prices to boost phone and computer inflation throughout 2026 as manufacturers pass through higher production costs. That said, the boost to core PCE should be smaller than that of software and accessories, in part because these categories receive smaller weights in PCE. Taken together, we estimate that AI-related pressure will boost year-over-year core PCE inflation by about 0.4pp in December 2026 (vs. 0.25pp so far, and a 0.6pp peak in 2026H2). We estimate a much smaller boost to core CPI inflation, of about 0.1pp, largely because CPI does not suffer from the same methodological issues as PCE.

Exhibit 6: We Expect AI-Related Price Pressures to Boost Year-over-Year Core PCE Inflation by 0.4pp by December 2026, With a 0.6pp Peak Earlier in H2; We Expect AI-Related Price Pressures to Boost Core CPI by About 0.1pp by December 2026

![](images/2a4f1815e00fc6c5f5cd2bb00bb77c2de6d32c3fb2b2da7185e90b97793d994c.jpg)  
Source: GS Global Investment Research, Department of Commerce, Department of Labor

## Disinflation From Rent and Wages

We continue to see a relatively benign outlook for core inflation outside of AI pressure and energy passthrough. We expect rent growth to slow to below its pre-pandemic pace, reflecting continued softness in new-lease rent growth (Exhibit 7). Monthly housing inflation has been volatile recently, spiking in April as the negative bias from last year's government shutdown unwound. Housing prices also rose at an above-trend pace in May, but most of the acceleration relative to the prior trend was concentrated in the Northeast, which we suspect reflected statistical noise. Going forward, we continue to expect housing inflation to slow and to settle at a pace roughly $1 - 1\frac{1}{2}$ pp below the pre-pandemic pace.

\*Average of Costar, Yardi, and Zillow measures of rent growth.

Exhibit 7: We Expect Housing Inflation to Continue to Slow This Year, Reflecting Soft New-Tenant Rent Inflation  
![](images/2a517b62ef30e3566ba76a8dd69928b39ea539e3e235d4b2f45e146683606ae7.jpg)  
Source: GS Global Investment Research, Department of Commerce, CoStar, Yardi, Zillow

We also expect slower wage growth to put downward pressure on nonhousing services inflation, excluding airfares—which are largely driven by oil price changes—and portfolio management—which are driven by equity prices. Wage growth has continued to slow this year, and we expect wage-sensitive PCE services to follow suit over the next several months. We think that the World Cup has likely temporarily boosted hotel prices but expect that to fade as the reservation window moves past the tournament’s end.

Exhibit 8: Slower Wage Growth in Labor-Intensive Services Should Provide an Additional Disinflationary Impulse This Year  
![](images/df0b0fc8953c97e2785c9eedd2f2ec48c6ee41d0ae8ba4896b7533cfe2fa2670.jpg)  
\* Includes food services, hotels and casinos, other recreational services, nursing homes, motor vehicle services, personal services, social services, household maintenance.

## Source: GS Global Investment Research, Department of Commerce

One exception within nonhousing services is the healthcare services category, which we expect to remain elevated this year. Healthcare services costs, as measured by the Centers for Medicare & Medicaid Services' Medicare Economic Index, have increased by 26% since 2020Q1, while consumer prices have increased 18%, making healthcare the last major remaining example of “catch-up inflation.” At the same time, we expect slowing wage growth for healthcare workers and a smaller Medicare fee update this year—an important anchor point in negotiations between healthcare providers and insurance companies—to keep healthcare inflation around its current 3% pace, roughly 1-1½pp above the pre-pandemic pace.

With housing and healthcare receiving roughly equal weight in core PCE, we expect the overshoot in healthcare inflation to roughly offset the similarly-sized undershoot in housing inflation, leaving their combined contribution around the pre-pandemic level.

Exhibit 9: Continued Catch-Up to Costs Will Put Upward Pressure on Healthcare Inflation, Though a Smaller Medicare Fee Increase (and Slowing Wage Growth) Should Limit the Upside  
![](images/05770468dadfb512ab86244755b373e237c08deb7a6f45cef5cf25237dae64a9.jpg)  
Source: GS Global Investment Research, Department of Commerce, Department of Health and Human Services

## Broader Inflation Risk

Our indicators of persistent inflation risk and pipeline inflation pressures suggest that underlying inflation risk rose slightly in recent months but remains modest. Exhibit 10 shows that our measure of pipeline pressures based on the signal from the PPIs accelerated in recent months, but most of this reflected price increases in energy and related products.

Exhibit 10: Our Tool for Tracking Input Cost Pressures Across the Supply Chain Accelerated Somewhat in Recent Months, but This Largely Reflected Energy Passthrough

![](images/84f7ebed1e6eb0995ea78804be0f980cbafe253686f709742a8e2068fbedb0a4.jpg)  
\* Sports and recreational vehicles, household appliances, clothing and footwear, pets and related products, food services, and other services.  
Note: We adjust both the PCE series and our intermediate demand PPIs for our estimates of the indirect effect of tariffs on input prices across the supply chain.  
Source: GS Global Investment Research, Department of Labor

Exhibit 11 shows our persistent inflation risk indicator, which combines key signals including slack and wage pressures, medium- and long-term inflation expectations, and the breadth of inflation. Our indicator suggests that persistent inflation risk has increased somewhat in recent months but remains broadly in line with its 2000s level and significantly below the aftermath of the pandemic.

Exhibit 11: Our Persistent Inflation Risk Indicator Ticked Up Somewhat in Recent Months but Remains Broadly in Line With Its Post-1995 Average

![](images/7cac63453571dc65fc3420c9072cd81d570dbfc4840ece12d65b9a33623a5c13.jpg)  
Note: We exclude our estimates of the effects of tariffs on each PCE category, as well as the computer software and accessories component (see "US Economics Analyst: AI and (Measured) Inflation: Up Then Down," May 2026).  
Source: GS Global Investment Research

## The Inflation Outlook

We forecast year-over-year core PCE inflation of $3.2\%$ in December 2026, as last year's tariff boost fades but AI and oil-related pressures keep inflation elevated (left side of

Exhibit 12). We then expect core PCE inflation to slow to 2.2% by December 2027 as the energy and AI effects wane. In the near term, we expect strong increases in equity prices to boost monthly core PCE inflation by about 0.10pp in May and 0.05pp in June. We expect core CPI to slow to 2.6% year-over-year by December 2026 and 2.2% by December 2027, as it is less affected by AI measurement issues and financial services pressures (right side of Exhibit 12).

We see risks to our forecast skewed to the upside, particularly if the situation in the Middle East deteriorates or if higher inflation expectations cause businesses to raise prices beyond the increase in their input costs. Inflation could prove lower than we expect if shelter inflation slows more quickly than we assume, oil prices fall by more than we expect, or the AI-related memory crunch resolves faster than we anticipate.

Exhibit 12: We Expect Energy Price Passthrough, AI-Related Pressure, and the Stock Market Boom to Keep Year-over-Year Core PCE Inflation at 3.2% in December 2026, Even as Core CPI Inflation Slows to 2.6%; We Expect Both PCE and CPI Inflation to Be Close to 2% by December 2027  
![](images/b84e29fd7c0a9e98233403af0704ee145b3fd14f89367c6168cf9afc3de9ea72.jpg)  
\* Computer software and accessories, phone

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
