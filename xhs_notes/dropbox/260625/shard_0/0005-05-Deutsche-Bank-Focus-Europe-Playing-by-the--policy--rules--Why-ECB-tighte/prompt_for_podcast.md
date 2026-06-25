你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Playing by the (policy) rules: Why ECB tightening is warranted

The ECB has embarked on a path of measured policy tightening, with President Lagarde describing June's 25bp hike as "robust" but not "forceful." To assess the appropriate trajectory of policy and the potential quantum of further hikes, we have applied a suite of simple policy rules to the ECB's own staff projections. This report shows that the ECB's own outlook for inflation and growth warrants some further policy tightening ahead, even after the recent US-Iran MOU announcement.

## Conclusions and takeaways:

Further policy tightening is warranted: The ECB's June rate hike was robust, supported even by the milder scenario. Using the ex-energy HICP forecasts, the median policy prescription under the baseline scenario is consistent with rates rising to roughly 2.75% by end-2026 (consistent with two more hikes). Or under the milder scenario, the median prescription suggests rates topping out at a little less than 2.50% at the end of this year (more or less consistent with one more hike).

June's revisions to the baseline projection warrant some further policy tightening: The revision to inflation and activity between the March baseline projection and the June projection boost the prescribed path of policy rates by 25bp to 50bp on average across the various rules. Between March and June, market pricing moved to price in an additional 25bp policy hike this year – broadly consistent with the policy rules.

Rules are only a guide not a script: While policy rules provide a guide for "good" monetary policy, they do not capture all the complexities of monetary policy. During the pandemic and energy shock from Russia's invasion of Ukraine, the rules prescribed highly aggressive policy tightening. During the 2024 rate cutting cycle, actual rates broadly followed the prescribed paths for rates early on, but perhaps pushed actual rates towards the lower end of the prescribed range by the end of the cutting cycle.

What this means for the ECB policy outlook: The tone at the ECB press conference on 11 June was consistent with the risk of two more hikes, leading to a terminal policy rate of $2.75\%$ . We maintain our baseline call for one more hike to $2.50\%$ . There are already some signs of the inflation shock moderating (e.g., dbDIG inflation expectations) and oil prices are lower than what we were expecting after a US-Iran deal. Current energy futures suggest the path ahead lies somewhere between the ECB's baseline and milder scenarios. If that is the case, the policy rules

# Economics Focus Europe

are consistent with another one or two hikes.

## Methodology

This report examines what interest rates should do according to a range of simple policy rules. The suite of policy rules is taken from a set regularly monitored by the Federal Reserve (see here and here) and includes a range of different rules based on various common measures of inflation (headline HICP, core HICP) and activity (unemployment, the output gap). The table in Figure 1 details the policy rules used.

<table><tr><td colspan="2">Figure 1: The suite of policy rules considered</td></tr><tr><td>Rule</td><td>Equation</td></tr><tr><td>Taylor (1993) rule</td><td> $i_t = r_t^{LR} + \pi_t + 0.5(\pi_t - \pi^{LR}) + (u_t^{LR} - u_t)$ </td></tr><tr><td>Balanced-approach rule</td><td> $i_t = r_t^{LR} + \pi_t + 0.5(\pi_t - \pi^{LR}) + 2(u_t^{LR} - u_t)$ </td></tr><tr><td>Taylor (1993) rule with output gap</td><td> $i_t = r_t^{LR} + \pi_t + 0.5(\pi_t - \pi^{LR}) + \text{output gap}_t$ </td></tr><tr><td>Forward-looking rule</td><td> $i_t = r_t^{LR} + \pi^{F}_{t+3} + 0.5(\pi^{F}_{t+3} - \pi^{LR}) + 0.5(\text{output gap}_t)$ </td></tr><tr><td>Core inflation in Taylor (1999) rule</td><td> $i_t = r_t^{LR} + \pi_t^{\text{core}} + 0.5(\pi_t^{\text{core}} - \pi^{LR}) + \text{output gap}_t$ </td></tr><tr><td>First-difference</td><td> $i_t = i_{t-1} + 0.5(\pi_t - \pi^{LR}) + (u_t^{LR} - u_t) - (u_{t-4}^{LR} - u_{t-4})$ </td></tr><tr><td>First-difference (ver. 2)</td><td> $i_t = i_{t-1} + 1.74(\pi_t - \pi^{LR}) - 1.19(u_{t-1} - u_{t-2})$ </td></tr><tr><td>Inertial rule</td><td> $i_t = 0.8i_{t-1} + (1 - 0.8)[r_t^{LR} + \pi_t^{\text{core}} + 0.5(\pi_t^{\text{core}} - \pi^{LR}) + \text{output gap}_t]$ </td></tr><tr><td>Low weight on output gap rule</td><td> $i_t = 0.91i_{t-1} + (1 - 0.91)[r_t^{LR} + \pi_t^{\text{core}} + 1.58(\pi_{t+1}^F - \pi^{LR}) + 0.14(\text{output gap}_{t+1})]$ </td></tr></table>

## The rules:

Taylor rule: The rule is inspired by the original 1993-version of Taylor's rule. Nominal interest rates should be raised by 1.5 times the inflation gap (more than one-for-one in order to satisfy the Taylor principle). Rates should also be raised when the unemployment rate is below its long-run value.

Balanced-approach rule: This rule modifies the previous rule to place more importance on the unemployment gap. Although the ECB does not have a dual mandate (like the Fed), because of the lags in inflationary pressure, targeting the current unemployment gap has similarities to also targeting future inflation (which unemployment affects through the Phillips curve).

Taylor rule with output gap: This rule replaces the unemployment gap with the output gap, an alternative measure of the slack in the economy.

Forward-looking rule: This rule targets future inflation rather than current inflation, which can help the central bank look through near-term variability they cannot affect due to the lags of monetary policy.

Core inflation in Taylor rule: An alternative approach to looking through near-term variability is to replace headline inflation with core inflation in the policy rule.

First-difference rules: These rules say the change in the policy rate should be related to inflation gaps and changes in the unemployment rate. If either of these two terms are non-zero, it suggests the economy is not in equilibrium, and policy should be adjusted to compensate. Version 2 does not rely on the long-run unemployment rate (which is unobservable), and could thus be more robust in real-time policy setting.

Inertial rule: This rule adds policy smoothing to the rule in an attempt to

better replicate the gradual nature of policy adjustments.

\- Low weight on output gap rule: This inertial-type rule lowers the weight on the output gap and increases it on inflation to focus more on inflation.

For forecasts of the variables in the rules we use the ECB's latest set of staff projections (released at the June meeting). $^{1}$

## Policy rule prescription for future interest rates

We begin the analysis by considering the central question: what do the policy rules suggest the ECB should do with interest rates over the near term?

Feeding the ECB's own June staff projections into the suite of policy rules, we have produced the path of interest rates prescribed by each rule over 2026-27 (Figure 2, LHS).

The suggested paths of interest rates broadly fall into three main groupings:

Taylor-type rules predicated on headline HICP inflation suggest monetary policy should be tightened aggressively and quickly in response to the inflationary pressures from the energy price shock. The rules suggest rates should be hiked to around 4% by the end of this year, a significant increase from current levels.

First-difference rules prescribe a steady tightening of policy. While less aggressive than the Taylor-type rules the fact that inflation is well above target in 2026, and further on unemployment is steadily falling (driven by the economic recovery) the rule interpret the data as signals we are still below equilibrium throughout this period.

Policy rules that incorporate smoothing of policy rates or based on core inflation suggest policy paths that are more in line with what markets and economists (the SMA) are predicting. The smoothing parameter helps the rule look through the near-term inflationary spike that is assumed in the forecasts to be temporary and take a more medium-term view.

The ECB can probably ignore the signal from policy rules based on headline inflation in an energy supply shock. Policy can do nothing about the direct energy effects and will instead focus on the spillovers or second-round effects from energy prices. For this reason, we also run the rules on HICP excluding energy as the inflation measure within the rules. These results are presented on the right-hand side of Figure 2.

Figure 2: Path of policy rates (ESTR) prescribed by a suite of monetary policy rules produced using the ECB's June staff baseline projections  
![](images/38b4f36a340faefa39771bdb9348fb62a0b140433346bb47b7b1212b913b1431.jpg)  
Source : DB, ECB, Haver Analytics, Bloomberg Finance LP
Notes: SMA = Survey of Monetary Analysts. Colour of lines group rules based on the "type" of rule

Excluding energy prices from the inflation measure produces policy prescriptions that lie much closer to current market pricing. The rules suggest that further tightening of policy is warranted under the ECB's baseline projects which incorporate a broadening of inflation throughout the economy. The median rule implies rates at roughly 2.75% by end-2026 (consistent with two more hikes).

Caveat for interpreting the policy prescriptions: The path of inflation and GDP used in the policy rules are drawn from the staff's baseline projections which are conditioned on market pricing (three interest rate hikes). There is no endogenous feedback from the path of prescribed policy from each policy rule back to inflation and output. In reality, if the ECB did follow the Taylor-type rules prescription at the last meeting and hike to around 3.75% rather than 2.25%, the future path of inflation and GDP growth would be different from what is assumed in the baseline projections. This in turn would affect the values of the prescribed policy from the rule further out in the projection horizon.

## How to respond to the alternative scenarios

The ECB staff projections introduced a new milder scenario to the downside of their baseline projection. With the recent announcement of the memorandum of understanding (MOU) between the US and Iran, the spot prices of oil and gas have fallen significantly, and with them the near-term energy futures as well. Over the rest of 2026, energy futures now lie closest to the ECB's milder scenario. However, further out in the forecast horizon, energy futures remain closer to the baseline projection (Figure 3).

During the press conference, Lagarde said that "the decision to raise rates is robust across a range of scenarios mapping out how the shock might evolve and affect the medium-term outlook for the euro area".

We have re-run the policy rules on all three alternative scenarios (Milder, Adverse, and Severe) to see how the policy prescription of each rule would differ from the baseline.

One important caveat is that the alternative scenario projections published by the ECB do not include their forecast for unemployment. Therefore, we can only analyse how some of the rules differ across scenarios – those that rely on the output gap rather than unemployment.

Figure 3: Oil and gas futures contracts vs the ECB's June alternative scenarios  
![](images/0499d5682b0b7d9b0ed9d4b2af7ea2cc6e948c1ecf1b3273a72b228e9a039b32.jpg)  
Source : DB, ECB, Bloomberg Finance LP

![](images/80746915ec49f06519d29a36b5cf8cf40927f6d9c72e0e7e38d5cd5de0e3fcb5.jpg)

Figure 4 to Figure 6 shows the policy prescriptions of the various rules under the alternative scenarios the ECB published.

Milder scenario: The median prescribed interest rate from the policy rules (excluding energy from HICP) is consistent with policy rates around 2.50% from the end of 2026 onwards (consistent with one more hike this year).

Adverse and severe scenarios: Both rules have similar prescriptions to the baseline and milder scenario over 2026. This is because the alternative scenarios only begin to differ from Q3 2026, and it takes time for the higher energy prices under these scenarios to filter through to HICP excluding energy prices. But over 2027, both rules prescribe further steady tightening of policy throughout the year.

The ECB's claim that the June hike was robust is supported by the analysis of this framework. Even in the milder scenario, the rules suggest the 25bp hike in June was justified under the ECB's staff projections, and one further hike (to $2.50\%$ ) could also be appropriate. The fact that interest rates in the adverse and severe scenarios begin to deviate significantly only in 2027 suggests the ECB should be happy to leave some tightening risk premia in the market after it hikes to $2.50\%$ in September – if there is any risk of the adverse or severe scenarios still materialising.

Figure 4: Mild scenario – policy rule prescriptions  
![](images/1f0d363b7b5d8df1e3ad7d3b04c0baa1c8f82069d7e7839955a654b95fa880ce.jpg)  
Source : DB, ECB, Haver Analytics, Bloomberg Finance LP.
Notes: Only a subset of policy rules can be analysed as the ECB does not publish unemployment data for their alternative scenarios. Colour of lines group rules based on the "type" of rule.

Figure 5: Adverse scenario – policy rule prescriptions  
![](images/4f4e9ae6165995648e2828b8bd5038d4bbe5f7084da5c2791a65e76ed30cca88.jpg)  
Source : DB, ECB, Haver Analytics, Bloomberg Finance LP. Notes: Only a subset of policy rules can be analysed as the ECB does not publish unemployment data for their alternative scenarios. Colour of lines group rules based on the "type" of rule.

Figure 6: Severe scenario – policy rule prescriptions  
![](images/569240d7e7ebe5828aba307f5473b9ddc154221ac7e749e8ff870a1fde27a462.jpg)  
Source : DB, ECB, Haver Analytics, Bloomberg Finance LP.
Notes: Only a subset of policy rules can be analysed as the ECB does not publish unemployment data for their alternative scenarios. Colour of lines group rules based on the "type" of rule.

Caveat on policy rules under alternative scenarios: It is important to keep in mind that the paths of inflation and output in the ECB's alternative scenarios are predicated on the same path of monetary policy (3 hikes) and fiscal policy as in the baseline. As the rules show, monetary policy should tighten under the adverse and sever scenarios, and be a little looser under the milder scenario (all relative to the baseline). Therefore, if any of these scenarios were to actually materialise, it is highly likely that monetary policy (and possibly fiscal policy) would respond differently to what the projections for inflation and GDP assume, which in turn would influence the actual outcomes of inflation and GDP. This means that we should keep in mind the policy rules give prescriptions for the specific path of inflation and GDP in the scenario, not how monetary policy should respond to the specific energy shocks underlying the alternative scenarios.

## How the policy prescriptions have evolved: March vs June staff projections

At the June meeting, the ECB staff revised up there forecasts for inflation noticeably in 2026-27, and revised down their growth only marginally over the projection. $^{2}$ Figure 7 and Figure 8 plot the difference in policy prescriptions based on the staff's June baseline projections and those based on the March baseline projections. This difference shows how the policy rules have evolved with the changes in inflation, unemployment, and growth outlooks under the two baseline projections.

Because of the large number of rules, we present the range of differences (represented by the grey bars) alongside the average and median differences across all the rules in the suite.

Figure 7: Difference between the policy rule prescriptions (pp) using the June staff projections vs the March projections – when headline HICP is used as the inflation measure in the rules

![](images/8327261f1974dde2656c836435e011f676903f3c57fe6a90c9249638bee2d0dc.jpg)  
Source : DB, ECB, Haver Analytics, Bloomberg Finance LP. Notes: Range denotes the maximum-minimum difference in policy prescription between June and March staff projections

Figure 8: Difference between the policy rule prescriptions (pp) using the June staff projections vs the March projections – when HICP ex energy is used as the inflation measure in the rules

![](images/88843ccecb4a37603e22870096fe9d96890790ec0ef44667877584fa6d814e94.jpg)  
Source : DB, ECB, Haver Analytics, Bloomberg Finance LP. Notes: Range denotes the maximum-minimum difference in policy prescription between June and March staff projections

Focusing on the results excluding energy prices, the revisions made to inflation and activity projections between the March and June staff projections would be consistent with around 50bp of additional tightening in early 2027, and 25-50bp further out in the projection (relative to the March policy rule prescriptions). Between the March and June projections, market pricing has moved to price in one further hike over the next year, broadly in the range suggested by the rules.

## The ECB has not always followed these rules

Simple policy rules (like the ones in this report), serve as valuable benchmarks for assessing monetary policy but are not rigid prescriptions. While these rules provide a theoretical anchor based on core macroeconomic variables, actual policy rates often diverge. These divergences do not always necessarily reflect "policy mistakes". Central bankers incorporate a wider array of real-time data and forward-looking judgments not captured by stylized rules. But as benchmarks, the rules can stimulate debate as to why actual policy deviates from the what the rules recommend as "good" policy actions.

Below we look at how actual interest rates compare to the policy prescriptions from the rules over the last few years. The results show that the ECB does not follow any one specific rule.

## 2021-2022 pandemic and energy shock

Figure 9 plots the interest rate prescriptions from the policy rules over the period 2021-23 against the ESTR rate at the time. Even excluding the direct impact of energy prices, and assuming that interest rates are smoothed over time, the policy rules suggested interest rates should have started increasing by mid-2021, during the pandemic. The rates should then have further accelerated in early 2022 with Russia's invasion of Ukraine.

Figure 9: ESTR vs policy rule prescriptions (%) during the 2021-22 pandemic and energy shock  
![](images/23144f6abe55354f66a443ff9c44aff759e1b9535b2f07bf5762b521498c9466.jpg)  
Source : DB, ECB, Haver Analytics, Bloomberg Finance

[中间内容因长度限制已省略]

t whether to acquire the product. In preparing this report, the primary analyst or an individual who assisted in the preparation of this report has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
