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
# Korea Views: Korea—Riding Stronger and Longer AI Tailwinds

The AI capex boom is proving stronger and longer than expected for Korea's chip cycle, as reflected in our tech team's upgrade to the memory demand outlook. We expect the AI-driven super surplus to accelerate into year-end, pushing total exports above USD1 trillion and the current account surplus to a record high of around 15% of GDP.

We raise our real GDP growth forecasts to 2.7% in 2026 (+10bp) and 2.3% in 2027 (+40bp), both above consensus, on a stronger and more durable AI impulse through capex, R&D, and wealth effects. We leave inflation unchanged at 2.6% and 2.2%, under our updated base-case scenario for reopening of the Strait of Hormuz, and extend the hiking cycle into 2027 and lift our terminal policy-rate forecast to 3.25% from 3.0%.

Domestic transmission remains uneven. First-half data show a wider gap between semiconductors and the rest of the economy: memory-led exports are surging, while non-tech exports, retail sales, consumption, and tech-sector job creation remain subdued. Wage and inflation spillovers also look contained. The tech wage base is small, and low margins elsewhere should limit broad wage inflation. We expect headline inflation pressure to come mainly from import prices and forex rates, while core goods inflation has remained contained this time, unlike in 2022. Housing risks are more localized. Seoul metropolitan area prices have re-accelerated since mid-May, but prices elsewhere remain stable.

Fiscal balances could be substantially stronger than projected a year ago. We estimate additional memory-related tax revenue of about 2% of GDP in 2026, which together with a recent decision to save some excess revenues could reduce the consolidated deficit from a planned 1.9% of GDP to less than 0.5% of GDP.

The stronger fiscal and external positions reinforce our market view: KRW looks too weak relative to fundamentals and the policy direction, while rates markets are pricing in an increasingly hawkish policy path. Policy is already leaning towards countering potential overheating, as reflected in hawkish guidance on monetary policy and the decision to avoid procyclical spending increases. KRW stabilization is likely to become a broad policy priority, given strong forex pass-through to inflation and equity-rally-related forex pressures from rebalancing needs and leveraged positions. Monetary tightening is unlikely to move rapidly, however, given still-limited domestic demand pressures and high household debt-service burdens. Risks to our updated policy-rate views are balanced: upside from wage pressures and downside from KRW appreciation.

## Goohoon Kwon, CFA

+852-2978-0048 | goohoon.kwon@gs.com GS (Asia) L.L.C.

Irene Choi
+82(2)3788-1722 | irene.choi@gs.com
GS (Asia) L.L.C., Seoul Branch

Andrew Tilton
+852-2978-1802 |
andrew.tilton@gs.com
GS (Asia) L.L.C.

1. The AI boom is boosting Korea's chip demand more strongly and for longer than previously expected, as reflected in a recent upgrade to the memory demand outlook by our tech team.-Korea's current account reached a record high of $15\%$ of GDP in Q1, and we expect the AI-driven super surplus to accelerate into year-end, pushing total exports above USD1 trillion (Exhibit 1) and the current account surplus in excess of $15\%$ of GDP in 2026. High frequency data show that almost all the surplus in the first half was recycled offshore through record-high net foreign equity outflows (rebalancing needs and leveraged positions), weakening the KRW despite a sharp improvement in the current account balance (Exhibit 2).

Exhibit 1: Exports of goods on track to reach USD 1 trillion in 2026 on strong memory demand  
![](images/ba8446a9a7d16d987c4c728ad23ef9628309c43c02e9f1e4269e749527f4a0ca.jpg)  
Source: Haver Analytics, GS Global Investment Research  
Exhibit 2: Recent surge in foreign equity outflows outweighed gains in the current account, weakening KRW

![](images/2fa7f70cb2b7cbbc7bb54e5b60d368df4effe76db7e979757d061bdb0397fde6.jpg)  
Source: Haver Analytics, GS Global Investment Research

2. We raise our growth forecasts to 2.7% in 2026 (+10bp) and 2.3% in 2027 (+40bp), both above consensus, on a stronger and more durable AI impulse (Exhibit 3). The revision is driven mainly by capex, including R&D, with a smaller contribution from wealth effects. Consistent with a recent BOK study, we keep the estimated wealth effect modest, reflecting the concentration of equity investors among wealthy and older households, higher local equity-market volatility, and small financial assets relative to property assets, similar to Australia. Our inflation forecasts remain unchanged at 2.6% and 2.2%, versus consensus of 2.7% and 2.1%, under our updated base-case scenario for reopening of the Strait of Hormuz, which assumes normalization in oil exports from Gulf producers by late August. In line with these macro revisions, we now forecast the hiking cycle to extend into 2027 with a terminal policy rate of 3.25%, up from 3.0% previously.

Exhibit 3: We expect growth meaningfully higher in 2027 than consensus

<table><tr><td colspan="4">Macro forecasts</td></tr><tr><td></td><td>2025</td><td>2026</td><td>2027</td></tr><tr><td colspan="4">Real GDP growth</td></tr><tr><td>GS forecast</td><td>1.1</td><td>2.7</td><td>2.3</td></tr><tr><td>BOK forecast</td><td></td><td>2.6</td><td>2.1</td></tr><tr><td>BBG consensus</td><td></td><td>2.6</td><td>2.0</td></tr><tr><td colspan="4">Headline CPI inflation</td></tr><tr><td>GS forecast</td><td>2.1</td><td>2.6</td><td>2.2</td></tr><tr><td>BOK forecast</td><td></td><td>2.7</td><td>2.3</td></tr><tr><td>BBG consensus</td><td></td><td>2.6</td><td>2.1</td></tr></table>

Source: GS Global Investment Research

3. The stronger AI cycle is lifting Korea's external balances and growth outlook, but its domestic transmission remains narrow. First-half data show a widening divergence between semiconductors and the rest of the economy (Exhibit 4). Memory-led exports continued to surge, while non-tech exports remained stagnant and retail sales stayed subdued (Exhibit 4). Overall consumption also remained soft, despite recent pickups in luxury goods sales.

Exhibit 4: K-shaped cycle—tech vs non-tech and production vs consumption  
![](images/e90abd030b6d43c27c2e025846a472591ea5bddc602bce11e95261d890b9fc4c.jpg)

![](images/9d9faa1ad6968ba6eac60368be1983fae496c7401a617e9fd7f670ea08d329a0.jpg)  
Source: Haver Analytics, GS Global Investment Research

4. This uneven transmission is also visible in the labor market. Job growth has shifted increasingly toward public services, including healthcare, public administration, and defense, rather than the tech sector. Public services have more than fully accounted for job growth since 2025, after contributing less than $50\%$ in 2019. This reflects demographic headwinds and related government job programs that have expanded public employment for more than a decade, largely at the expense of non-tech manufacturing jobs (Exhibit 5). Overall labor markets remain lackluster, with subdued wage growth and little support from tech-sector hiring, as semiconductor job creation has been broadly flat since 2024 given the sector's heavy capex orientation.

Exhibit 5: Increasing dominance of public sector jobs in labor markets in Korea  
![](images/e5db0e7bb620e5a8cbdb6de7844c0def5c930f01a30f70dfe36c982a4a54ec91.jpg)  
Source: Haver Analytics, Korea Statistics Office

![](images/c268cf750299c6e01744369bdc7c4e7230ca1fe2ed4b166379fb8f9eac3df49e.jpg)

5. The same limited labor-market transmission should also contain wage spillovers. Recent wage agreements at major semiconductor companies should have only a limited near-term impact on overall wage growth, given the small tech wage base. Tech-sector wages accounted for around 3% of total wage bills, or 1.2% of GDP in 2025—less than one-third of Taiwan’s share—while wage bills of major memory companies accounted for just 0.4% of GDP (Exhibit 6). Tech-sector wages are set to rise on strong chip earnings and related performance payments. Even so, we estimate that post-tax bonus payments at major memory companies would remain around 0.5% of GDP in 2026 and 0.9% of GDP in 2027, equivalent to a relatively small supplementary budget early this year. The main offsets are special-bonus payment terms, mostly in locked-up equities, and high tax rates of nearly 50%, reflecting the top personal income tax rate and various mandatory social contributions.

Exhibit 6: Korea's tech sector accounts for far smaller jobs and total wages paid than Taiwan  
![](images/a422858aa82877ab5c89d937117a23958d71a75ad354447bce8636da44d28318.jpg)  
Source: CEIC, Haver Analytics, GS Global Investment Research

6. The key question, then, is whether higher memory-sector wages could spill over to the rest of the economy. We think this spillover risk is constrained by weak profitability outside semiconductors. Nearly 80% of jobs are in non-manufacturing sectors such as retail, construction, education, and healthcare, where margins have historically been below 5%. Within manufacturing, non-tech profit margins have also weakened in recent years to cyclical lows of around 5%, due to sustained regional overcapacity and competitive global markets. The divergence in earnings is also stark: operating profits of semiconductor companies will rise more than 6 times year-on-year in 2026, compared with just 40% for non-tech listed companies and 10% for non-manufacturing companies (Exhibit 7).

Exhibit 7: Large divergence in profits between chip and other sectors  
![](images/99d1183f5b31336de62f48a0e7136a4941b9827e7ce2a812f978f040c06388bb.jpg)  
Note: Showing consensus estimates for 2026

## Source: Quantiwise

7. With broader wage spillovers likely contained, inflation pressures should come mainly through imported goods prices and exchange rates. Headline inflation has picked up on surging energy prices, largely as expected. Core price pressures, however, remain contained. Core goods prices, excluding food and fuel, rose only moderately through May, unlike in 2022, when they had increased a cumulative 3.4% from March to December and 4.0% yoy in December (Exhibit 8). In contrast, core services prices, excluding eating out, utilities, and transportation services, increased only moderately in Korea in both cycles, rendering further support for limited second-round effects from imported inflation.

Exhibit 8: Korea's core goods prices have been stable relative to those during the post-pandemic inflation cycle  
![](images/e3ab3b085eb2f2a78f71cd38b3b5f96dae3c782ea25b70799ff9f0b95c9b890f.jpg)  
Source: Haver Analytics, GS Global Investment Research

8. The main domestic policy concern, however, is shifting from broad inflation to localized financial-stability risks. Seoul metropolitan housing prices have re-accelerated since early May, while housing prices elsewhere have remained stable since early April, after initial signs of modest recovery. This stands in sharp contrast to the broad housing boom during the pandemic period (Exhibit 9). This combination points to a policy mix that can remain targeted rather than broadly restrictive, especially as stronger fiscal and external balances create additional room for macro stabilization as discussed before.

Exhibit 9: Housing prices in Seoul metropolitan area have recently re-accelerated but those elsewhere have remained stable

![](images/cf90276e54d25cdf479a1781c58abf94979644162ec707aceab5fcecca4443ff.jpg)

Source: Haver Analytics, Kookmin Bank

9. Fiscal balances in 2026 and 2027 could be substantially stronger than projected a year ago. The 2026 budget assumed a consolidated deficit of KRW52.7trn on KRW390trn of tax revenue. Given the sharp improvement in semiconductor earnings prospects, we estimate roughly KRW60trn of additional tax revenue (approximately $2\%$ of GDP) could be collected in 2026, on top of the KRW25trn already reflected in the government's March supplementary budget (Exhibit 10). As a result, the consolidated budget deficit could fall from a planned $1.9\%$ of GDP to less than $0.5\%$ of GDP, even if a second supplementary budget were passed in the second half with spending similar to the first one. $^{1}$ Semiconductor-related corporate tax upside could remain significant in 2027 as well, at roughly $5\%$ of GDP above the amounts projected last year.

Exhibit 10: The AI boom strengthens Korea's fiscal outlook materially  
![](images/817e2c478e112eaf5c9e1a60d0aea887be8e2bed5072ecaef37f85c39fd915ac.jpg)  
Source: Haver Analytics, GS Global Investment Research

10. Korea's stronger external and fiscal positions together with narrow domestic transmission reinforce our market view: KRW looks too weak relative to fundamentals and policy direction, while rates markets price an increasingly more hawkish policy path (Exhibit 11). Policy is already leaning towards countering potential overheating. The government has chosen to save large excess revenues to lift growth potential rather than increase procyclical spending, while the BOK has provided hawkish guidance on monetary policy. KRW stabilization is likely to become a broad policy priority, given strong forex pass-through to inflation and equity-rally-related forex pressures from rebalancing needs and leveraged positions. Even so, monetary tightening is unlikely to proceed rapidly, given still-limited domestic demand pressures and an elevated household debt-service burden. The BOK is hence more likely to focus on managing inflation expectations and supporting broader policy efforts to counter overheating in metropolitan housing markets. Risks to our updated policy-rate views are balanced, with upside risk from wage pressures and downside risk from KRW appreciation.

Exhibit 11: Market pricing of policy rates is more hawkish than our view  
![](images/52777bfe1bfd34ec4d865d3c53d761497b702d3a12c86e788bbe1b4767add5b9.jpg)  
Source: Haver Analytics, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Goohoon Kwon, CFA, Irene Choi and Andrew Tilton, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Goohoon Kwon, CFA GS (Asia) L.L.C., Irene Choi GS (Asia) L.L.C., Seoul Branch, Andrew Tilton GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, 

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
