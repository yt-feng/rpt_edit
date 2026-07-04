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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化。汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Consumption growth has slowed – what gives?

Growth in real consumer spending has slowed year-to-date, led by a slowdown across many services categories. Weak real income growth has weighed on spending. We expect a moderate acceleration in 2H based on our forecast for disinflation ahead.

AlphaWise α

## Key Takeaways

Real consumption growth is tracking a $1.2\%$ annualized pace in 1H vs. last year's $2.1\%$ . Services led the slowdown while growth in durable goods accelerated.

\- High prices are weighing on purchasing power. With tariffs, oil, and additional drag from residual seasonality, real income has declined.

Tax refunds provided a partial offset. We find evidence they could have boosted spending more than expected, explaining the acceleration in durable goods.

As real income growth recovers, we expect a moderate acceleration in 2H led by services, with consumption for the year ending at $1.7\%$ (4Q/4Q).

The categories that have accelerated this year are high-income dominated. In 2027, we expect more broadening across spending categories and income cohorts.

MS & CO. LLC
Heather Berger
Economist
Heather.Berger@morganstanley.com +1 212 761-2296
Michael T Gapen
Chief US Economist
Michael.Gapen@morganstanley.com +1 212 761-0571
Arunima Sinha
Global Economist
Arunima.Sinha@morganstanley.com +1 212 761-4125
Sam D Coffin
Economist
Sam.Coffin@morganstanley.com +1 212 761-4630
Carolyn L Campbell
Strategist
Carolyn.Campbell@morganstanley.com +1 212 761-3748
Diego Anzoategui
Economist
Diego.Anzoategui@morganstanley.com +1 212 761-8573
Lingdi Xu
Economist
Lingdi.Xu@morganstanley.com +1 212 761-2957
James Egan
Strategist
James.F.Egan@MorganStanley.com +1 212 761-4715
Raquel Kanner
Strategist
Raquel.Kanner@morganstanley.com +1 212 761-1103

Exhibit 1: Real consumption growth has slowed, with a deceleration in services  
Real Consumption Growth (annualized)  
![](images/24dc46a299ec6a25628d122fbf67854783db5780a01fc1dc5b0eca8f613790c7.jpg)  
Source: Census Bureau, MS

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

## Consumption growth has slowed – what gives?

Growth in real personal consumption has slowed this year, primarily reflecting high inflation that has eroded purchasing power. Residual seasonality in first-quarter inflation data likely exaggerated the slowdown, while tax refunds partially offset the weakness by boosting goods spending more than we expected. As inflation decelerates in the second half of the year, we expect real income growth to turn positive, supporting a moderate recovery in consumption. We expect the acceleration to be led initially by services before broadening somewhat across spending categories and income cohorts next year.

The main downside risk to our view would be if inflation remains elevated, or if tighter monetary policy is needed for inflation to decelerate, both of which would continue to pressure affordability. Upside risks would stem from smaller-than-expected oil effects on goods spending near-term, or a continuation of strong employment growth.

## Slower Consumption Growth with a Deceleration in Services

After last week's personal income and spending report and 1Q GDP revisions, we are tracking real consumption growth for the first half of the year at a $1.2\%$ annualized growth rate, a considerable deceleration from the $2.1\%$ growth last year. This includes a very slow 1Q, at $0.5\%$ , followed by an acceleration in 2Q, where we are currently tracking $1.9\%$ q/q saar.

Broadly speaking, the slowdown is in-line with our expectation coming into the year: we expected real consumption growth to slow as higher prices weighed on purchasing power, with larger effects in the first half. This was based primarily on tariff-based pass through effects, though subsequently reinforced by sharply higher energy prices.

That said, the composition of consumption has differed from our expectations. Services consumption growth is running much weaker than its 2025 pace, while goods consumption accelerated; through May, real goods spending was up $1.7\%$ (vs $1.4\%$ last year) while services was up $1.1\%$ (vs $2.4\%$ last year).

The acceleration in goods consumption has been driven by durable goods. Through May real durable goods spending had risen at a 2.3% annual rate compared to just 0.1% 4Q/4Q growth last year. Many of the categories driving the acceleration are big-ticket items, including motor vehicles, furniture, and appliances. Meanwhile, growth in nondurable goods spending, such as clothing and gasoline, has decelerated in real terms versus last year.

Exhibit 2: Acceleration in real goods consumption growth is largely driven by durable goods  
Real Goods Consumption: YTD 2026 Growth Minus 2025 Growth  
![](images/edbf82a32d9dd6db500723f5bfd1224a9d5fac1307c6eab966d47570f5bab999.jpg)  
Source: BEA, Haver Analytics, MS

In services, most of the April and May data will be revised when the BEA receives the data from the Quarterly Services Survey in August. These revisions are often large, so we focus for now on 1Q data. There, we see that the slowdown in consumption growth was widespread across many services categories, both discretionary and nondiscretionary. These include foreign travel, motor vehicle services, professional services, food services, health care, financial services, and others. The deceleration in health care spending could be related to the expiration of the ACA credits, but we do not think this was the only driver given the broad-based slowdown. As shown in Exhibit 3, more categories beyond health care exhibited weakness.

Exhibit 3: The slowdown in 1Q services consumption growth was widespread across categories  
![](images/e337e9e047d48107a8f29e9ada43030ce5eb9e9e10f91dec5174bda3f4a17779.jpg)  
Source: BEA, Haver Analytics, MS

## Fundamentals Support the Slowing, while Tax Refunds Likely Boosted Goods

We attribute the slowing in consumption growth to two main factors: soft real income growth due to tariff and oil pressures, and residual seasonality in inflation data that exaggerates the softness in both real income and consumption. Tax refunds likely provided a partial offset.

Real income growth is the largest driver of spending. Real disposable income growth was weak in the back half of 2025, down 0.9% q/q saar in 4Q25, and has remained soft this year. For 1H, we are tracking real disposable income down 0.6% (annualized). This is despite the boost from tax changes, so real labor income is even softer, tracking -1.0% in 1H. Nominal income growth has slowed from the faster pace of 2023 and 2024, but the weakness over the past couple quarters is largely due to elevated inflation as tariff and oil pressures peak.

Weak income growth alone could justify an even sharper slowdown in consumption. However, consumers have tapped savings to smooth through the price shock. The saving rate, as a percent of nominal personal disposable income, fell from 3.6% at the end of 2025 to 3.0% at the end of May. Wealth gains over the period likely justify part, but not all, of this decline in the saving rate.

We believe residual seasonality has also weighed on measured real income and consumption growth. Since Covid, the seasonal adjustments used by the BEA for inflation have not fully accounted for all seasonal differences. This has resulted in residual seasonality, which "artificially" boosts measured 1Q inflation (with giveback in monthly

rates of inflation later in the year). Since we look at consumption growth in real terms, this higher inflation mechanically means softer real consumption. We estimate this could have subtracted around 60-80bps from real consumption growth in 1Q. Without it, 1H real consumption growth would likely be around $1.6\%$ ; still a deceleration but less extreme.

Exhibit 4: Real income growth has been weak with high inflation  
![](images/8ba775fe08fe9f5f22b646af03d1123f9ab8f009d3d473ec61f462724144f5a4.jpg)  
Source: BEA, Haver Analytics, MS

Exhibit 5: Consumption growth has slowed but outpaced income growth  
![](images/7ef37fc18132bcef87ee8fac91c7a03c0d8b44c4e793645a00c45fe5eec0fdee.jpg)  
Source: BEA, Haver Analytics, MS

We think high tax refunds partially offset the higher prices and help explain the acceleration in goods spending. The acceleration in durable goods spending year-to-date is somewhat surprising given tariffs, oil prices, and higher rates. We had expected tax refunds to boost 1H consumption, but we think there is evidence consumers spent a larger share of refunds more immediately than we expected.

Tax refunds were broadly in-line with our expectation, up 19% YoY (\$57bn). Typically the largest uses of tax refunds are saving and paying down debt. Based on historical patterns, we estimated roughly 35% of tax refunds to be spent within three months, boosting 1Q and 2Q consumption, while the remainder would support spending gradually through the year.

In our monthly AlphaWise Consumer Pulse survey, we ask consumers each February and March how they intend to use their tax refunds. This year, there were slight YoY declines in intentions to save and pay debts, and slight increases in intentions in some spending categories, including home improvement and big ticket purchases. These increases align with the categories of goods spending that have accelerated. Many of these spending areas, such as furniture and motor vehicles, had weak growth in 2H25, so there was likely pent up demand.

Exhibit 6: Intentions to save and pay debts were still high but down slightly YoY  
![](images/881700285ac528166ced7b97568fcfe9329928836a139664bfa3c16e4fb20e6f.jpg)  
Source: AlphaWise, MS

Exhibit 7: While intentions for some spending categories rose YoY  
![](images/d6d8c52b84554dd19fbf7688d3380e710be84e6ca5cc80585a48dc1084a72d05.jpg)  
Source: AlphaWise, MS

Consumer credit performance also suggests that a larger share of refunds could have been put towards spending instead of towards debt paydown. Historically, larger real tax refunds are associated with larger improvements in auto ABS delinquency rates as consumers use refunds to pay down debt. This year, delinquency improvement in both prime and subprime auto ABS was weaker than the historical relationship would imply. Delinquencies in prime auto ABS declined $15\%$ versus the expected $19\%$ , while delinquencies in subprime auto ABS declined $17\%$ versus expected $21\%$ (Exhibit 8 and Exhibit 9). Bank credit card performance has improved more noticeably, but those data skew toward higher-income consumers and historically have shown a weaker relationship with refund size.

Overall, we think the survey data and ABS data support the idea that a larger share of refunds was spent immediately this year. If roughly 50% of refunds were spent within the first three months, rather than our assumed 35%, and if most of that went towards goods, it would explain the strength in 2Q goods spending versus our forecast.

Exhibit 8: The decline in delinquencies in prime auto ABS from tax refunds was less than the historical relationship would imply  
![](images/59b8328f4308c1e21a2a4455a16a9af69a4baa06d6860f927024f1560d680612.jpg)  
Source: Intex, IRS, MS

Exhibit 9: ... and the same was true in subprime auto ABS  
Subprime Auto ABS: Jan - May Change in DQs vs Real Avg. Refund  
![](images/2220efe917f1bc5bbef7fb1259a9775edd51fa98855c367ad4560910a3207201.jpg)  
Source: Intex, IRS, MS

While weak income growth justifies a slowdown in consumption growth overall, the sudden slowdown in services is still surprising to us. Services spending is typically more persistent. While there could have been rotation from goods to services, employment

growth in many services industries has rebounded recently, somewhat contradicting a sudden slowdown in spending. The BEA often revises services spending heavily when they incorporate data from the Quarterly Services Survey. Last year, we saw a similar slowing in 1Q services consumption, followed by a rebound in the subsequent quarters. We expect there could be some upward revisions to April and May services spending when the QSS data is incorporated in August.

Since inflation – like the US economy – is skewed toward services, it may also be the case that residual seasonality affects real services spending more than goods.

## We Expect Moderate Re-acceleration Ahead

We continue to expect a slight pickup in consumption growth in 2H, with more strength in services. We expect 3Q and 4Q consumption growth of $\sim 2.0\%$ , around half a percentage point stronger than 1H. Consumption growth for the year moderates to around $1.7\%$ versus last year's $2.1\%$ .

After adjusting for the residual seasonality boost and the tax refund payback, these forecasts are incorporating a slight pickup in underlying consumption growth. We remain more sanguine than the Fed on the outlook for inflation, with headline and core PCE inflation of 3.3% and 3.0% 4Q/4Q this year and falling towards the Fed's 2.0% target thereafter. In contrast, the Fed sees inflation 30-50bp higher this year and less deceleration next year. Based on our outlook for decelerating inflation, we expect real income growth to recover, growing 2.2% (annualized in 2H). This should support spending, but consumption growth remains capped by the lagged effects of high prices earlier in the year.

In the near term, we expect the growth to shift back towards services. If it is true that tax refunds supported goods spending more than expected in 1H, that should mean less support later in the year. Our oil model also suggests the shock should weigh on goods spending with a lag, likely in 3Q. While lower gas prices now may mitigate the effects, we still expect some drag on goods. Payback from residual seasonality may also benefit services.

As we progress into 2027, we expect continued disinflation and productivity gains to support real income and consumption growth, leading to an acceleration back to the 2025 consumption growth pace. At that point, we expect goods spending to recover as well, especially if our expectation for a Fed on hold this year comes to fruition and financial conditions ease.

Structurally, we expect factors leading to greater income and wealth inequality will continue to favor upper-income household spending, but our outlook is for some cyclical improvement and broadening out in consumer spending in 2027 on account of falling inflation.

Before last week's 1Q revisions, risks to consumption and growth looked skewed to the upside, but we now view risks as evenly balanced. Upside risk could stem from a smaller oil shock effect on goods spending than we have factored in, stronger wealth effects, or a continuation of the strong employment gains of the past few months. Upside risk could also materialize if oil prices move lower over the next year on account of a greater re-organization in energy supply lines and energy supply than our commodity

analysts forecast (our commodity analysts foresee dated Brent at \$70-75 between now and the end of 2027).

Key downside risks would be if the currently reported services spending is revised down (and thus the underlying trend is weaker than we have assumed), or if we do not get the deceleration in inflation we expect. If inflation remains elevated, that could also mean tighter monetary policy and financial conditions, which could further weigh on consumption. Finally, inflation may decelerate, but it may take higher interest rates from the Fed to deliver that outcome. Hence, whether its firmer inflation or higher borrowing costs, the affordability crisis and K-shaped consumer remains a key downside risk to our forecast.

## Are High-Income Consumers Still Driving Spending?

When the oil shock hit, we pushed out our expectation for a broadening in consumption, given that higher prices would weigh more heavily on low- and middle-income consumers that base their spending decisions primarily on labor market income. We expected the deceleration in consumption growth this year to largely be driven by further slowdown from these cohorts, before some improvement in 2027. Although real-time spending data by cohort are limited, the categories that have accelerated so far this year largely support the idea that high-income consumers are driving consumption growth.

The top 20% income cohort makes up around 40% of all spending. Within that, they make up a similar 40% of services spending, 55% of durable goods spending, and 30% of nondurable goods spending. Among durable goods, the top 20% makes up the largest share of motor vehicle purchases, one of the strongest categories year-to-date. They also make up relatively large shares of other categories that have accelerated this year such as furniture, household equipment, and recreational vehicles.

If tax refunds were used for these purchases, spending could have been more evenly spread across cohorts than usual; typically a smaller share of high-income consumers receive refunds, but for those who do, their refunds are larger. We had expected most of the benefit from the OBBBA provisions to accrue to middle- and high-income consumers, so these groups could have both driven the acceleration in these categories.

The picture is more mixed for services. Some services categories that are more high-income dominated, such as transportation services, recreation services, and other services, slowed considerably in 1Q. If softer stock prices weighed on high-income spending in 1Q, this could have resulted in the weakness in these categories, and it is hard to know if they have rebounded in 2Q until we get the QSS data.

Overall, the slowing in services may signal a deceleration in spending growth for the high-income group as well. Even if the slowdown proved broad-based, we find it hard to believe the K-shape dynamic has improved this year. Low- and middle-income consumers are disproportionately affected by the decline in real income, and the few spending categories that have accelerated are still high-income

## dominated.

We continue to believe that if our baseline expectation of decelerating inflation and a Fed on hold this year comes to fruition, then there could be recovery ahead for low- and middle-income consumers next year. Lower gas prices and lower inflation more broadly in 2H should lead to a pickup in real income growth, and wage growth for lower cohorts specifically has shown some sign of acceleration recent

[中间内容因长度限制已省略]

ited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are neither Equity Research Analysts/Strategists nor Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity or fixed income securities: Michael T Gapen; Lingdi Xu; Heather Berger; Arunima Sinha; Diego Anzoategui; Sam D Coffin.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Carolyn L. Campbell; Raquel Kanner; James Egan.

## © 2026 MS
"""
