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
# Global Markets Comment: Distinguishing AI Risks—Size of the Pie vs. Share of the Pie

We showed recently that as the value built into AI-related equities has grown, more optimistic assumptions about the ultimate economic gains for US companies from AI are needed to justify it. This likely makes the market more vulnerable to challenges to the more optimistic story. Although robust earnings may dominate valuation concerns for now, we think investors should focus on the potential challenges to the theme and their consequences for portfolios.

In weighing those risks, a key distinction is whether a shock or risk shifts views on the likely aggregate value of AI-related innovation or on the distribution of that value (or both). Put simply, some worries are about the size of the pie and some are about how the pie is shared. We illustrate that this distinction is critical to understanding the impact of different challenges to the AI theme on markets and volatility.

Vickie Chang
+1(212)902-6915 |
vickie.chang@gs.com
GS & Co. LLC

Dominic Wilson
+1(212)902-5924 |
dominic.wilson@gs.com
GS & Co. LLC

Only aggregate shocks are likely to have reliable, broad cross-asset impacts. For those with broad exposure to US equities, these are the shocks that matter most and macro hedges are likely to be available to protect against them. For those with more specific AI-related exposures, hedging is more challenging, since distributional shocks may also affect portfolios but have less reliable impacts on macro assets.

For aggregate shocks to AI exposures, equity indices and rates so far appear to show clearer responses than FX and commodities. Except when higher rates are themselves the source of the risk, worries about the aggregate gains from AI are likely to push US yields lower. Aggregate shocks also have more scope to push equity index volatility higher than distributional shocks.

## Distinguishing AI Risks—Size of the Pie vs. Share of the Pie

Pressure on semiconductor stocks over the last month has revived questions about the potential risks to AI-related equities and ways to hedge against those risks.

A month ago, we looked again at what a macro approach to valuing the gains from AI says about the value that the market has assigned to AI relative to what the economy can deliver. That exercise showed that the value that had been built into AI-related equities has continued to grow and that more optimistic assumptions about the Present Discounted Value (PDV) of economic gains from AI that will accrue to companies were now needed to justify it. We also highlighted how the market has disproportionately rewarded the companies supplying the AI investment boom over the last 6-9 months. So alongside the risks to the market view of the aggregate gains from AI, there might also be risks to the market's view of the distribution of winners and losers.

This set-up has, in our view, left the market vulnerable to any challenges to the more optimistic story. Robust earnings may dominate valuation concerns with the investment boom likely to continue to extend, but we still think investors should focus on the potential challenges to the theme and their consequences for portfolios. Our general view is that precision about the nature of any potential “shock” is key to understanding its cross-asset impact. The challenge is that there are a bewildering number of different possible narratives that could create risk to the current AI story. Although each may have its own specific characteristics, we think it useful to try to think of ways to organize and simplify these different kinds of worries.

## Aggregate value or its distribution

In weighing those risks, we think a key distinction is whether a shock/risk shifts views on the likely aggregate value of AI-related innovation or on the distribution of that value (or both). Put simply, some worries are about the size of the pie, and some are about how the pie is shared. We have already shown that this distinction is critical to understanding recent trends in equity volatility, but it is also critical to the cross-asset footprint.

This distinction is embedded in the macro approach we have taken to looking at the value that we expect from AI. Our global economics team has calculated the Present Discounted Value of the additional GDP from the productivity gains that they expect from AI under our baseline assumptions. This defines the expected aggregate value of AI gains measured from today. To derive the value that should accrue to equity holders, we then need expectations of how that value is distributed. As Exhibit 1 shows, some portion of that should accrue to US companies in the form of higher profits. Those higher profits in turn will ultimately be shared among different types of companies: hyperscalers; infrastructure providers, like semiconductor, memory and power producers; model builders and other AI companies; and non-AI companies. $^{1}$ Some portion of those gains will also accrue to US consumers and workers and the same potential corporate and consumer beneficiaries are represented on the non-US side too.

![](images/212834498e2943d397a5458661d51d0c1cb35541f3efbb41366e95831a7a93b5.jpg)  
Source: GS Global Investment Research

So far, most of the AI-related value has accrued to US AI-focused companies and some key non-US companies, especially in Asia. The focus of our work so far has largely been on comparing estimates of the economic gains for US companies and the distribution of those gains across the major categories of US companies Exhibit 2. From that narrower perspective, anything that distributes value away from US companies—away from the top-left segment of Exhibit 1—including an increased share or AI gains going to consumers or non-US producers, is a shock to the “aggregate” value for the US equity market, even if the overall value of AI to the global economy does not change. We stick here to this narrower distinction between dynamics that affect the “aggregate” value of AI gains for the US corporate sector and those that affect its distribution across US companies. But it is easy to expand that view of what “aggregate” means through the lens of the framework that we set out here.

Exhibit 2: Our dominant focus has been on comparing value built into US companies and the potential capital revenues from AI

Change in Market Cap/Valuation From Nov. 30 2022 to Jul. 22 2026 vs. GS Estimates of PDV of Potential AI Capital Revenues

![](images/430643417e573db3ba23e060e163062d0da4d99c289f1752eaa3f4a775b9c674.jpg)  
"Semiconductors", "hyperscalers", and "other AI-related" are constituents of the GS TMT AI basket (developed by GS Global Banking & Markets)  
\*“US Combined Positive" assumes high capital share, faster adoption, and higher productivity gains from AI  
Source: Bloomberg, FactSet, GS FICC and Equities, GS Global Investment Research

## Different drivers of aggregate and distributional shocks

The forces driving market views of the aggregate value of AI and its distribution are generally different. Perceptions of the aggregate value from AI are most likely to be affected by things that shift one or more of the five key parameters that underpin our global team's estimates of the value of future AI revenues to US companies (Exhibit 3):

1. Productivity growth: the overall value of the innovation in improving work practices.

2. Adoption rate: how quickly those productivity gains are being realized.

3. Capital share: how much of those gains accrue to companies, which depends in turn on the ability to monetize the innovations.

4. International share: how much can US companies capture a share of non-US gains or vice versa.

5. Discount rate: the cost of capital for AI-related companies given financing needs and the uncertainty around potential revenues.

Exhibit 3: Views on the value of AI will shift if investors adjust their views on the key parameters  
![](images/9e03880dd95026bbbb7ca3a8713e8658b5d2c676a68efcc16977f619bd8a75d2.jpg)  
Source: GS Global Investment Research

Estimates of the PDV of AI revenues to US companies are sensitive to assumptions about each of these parameters, as we have illustrated. Macro shocks, which reduce the expected value for the entire corporate sector through assumptions about profits and the discount rate, even if the shock is not specifically related to AI. will also affect the aggregate value of US companies including AI-related companies.

For any given expectation of the aggregate value, the market can then make assumptions about who the winners and losers are likely to be, distributing that value across different parts of the corporate sector. Views on who will capture the benefits have shifted significantly over time. A prime example is the sharp increase in memory prices since late 2025, driven by shortages in the face of accelerating AI-related demand. That price increase is effectively a “terms of trade” shock that has helped producers and hurt consumers of chips. But beyond this dynamic, the market has also implicitly made judgments about the split between AI-related companies and the ultimate corporate users of AI products (assigning the bulk of AI-related value to the former) and about the capacity of AI disruption to shift profits away from incumbent firms in non-AI related industries (software, insurance, real estate). Shifts in views on issues that affect those divisions may not change expectations of aggregate profitability but will change how it is allocated.

## Classifying AI concerns

We think using this framework to specify how a particular risk reduces or distributes value is a helpful exercise. Classifying different concerns along this axis can still be challenging (and open to challenge!). Some shocks are more obviously aggregate shocks; some are more obviously distributional; and for some it is less clear:

\- Worries that focus on slower adoption or concern about the scope of use cases are likely to be aggregate shocks. They would lower estimates of some key parameters that drive aggregate value (lower productivity growth, lower adoption rates).

Difficulties in monetizing AI-related products or competition in models or applications that lower the cost of the innovation (as opposed to pessimism about the innovation itself) could function as a shock to the aggregate value that will accrue to US companies by distributing the gains more to consumers (lower capital share). But US corporate consumers could also benefit, and lower-cost products could accelerate adoption, which could shift the potential distribution of value towards them and mitigate the aggregate impact. Innovations by non-US companies could also distribute value away from US companies even if the broad value of AI-related innovations remains high.

\- Reduced willingness from the market to finance the AI investment boom would also look more like an aggregate shock. But a decision to slow capital spending because infrastructure looks sufficient could have more of a distributional flavor, reallocating value to hyperscalers from suppliers of the investment boom.

■ Capacity expansion or competition in the semis/memory space or model innovation to rely on fewer or cheaper chips could hurt semiconductor producers, but by alleviating shortages would benefit corporate consumers, so would potentially be a distributional impact. To the extent that those gains are passed through to final consumers too (instead of accruing to companies), it could also have some aggregate impact.

Displacement or disruption of incumbent companies through fear of AI are obviously distributional at some level but could also have aggregate implications for US public market profits if they result in increased gains to consumers or if the corporate winners are outside the US public markets.

■ Macro shocks—tighter monetary policy, a renewed rise in oil prices or a weakening in the labor market (AI-related or otherwise)—would function more like aggregate shocks, affecting value in the overall space. Given the value that has been built into AI-related companies, heavy positioning in many of these areas, and the financing needs of the AI boom, macro shocks could disproportionately affect AI beneficiaries vs. the rest of the broader market. But the nature of the macro shock likely matters here too, given that some shocks (higher oil prices, for instance) may affect other market segments disproportionately.

## Different drivers, different asset footprints

The distinction between aggregate and distributional shock matters for two main reasons. It affects the cross-asset footprint; and it affects the volatility footprint.

For the cross-asset footprint, the main distinction is that aggregate shocks are likely to have much clearer impacts on the broad equity market and on a larger range of macro assets, especially interest rates, than distributional ones. We can illustrate this from the response to five market-moving events over the last 18 months.

1. Deepseek (27 Jan 2025). Release of DeepSeek's R1 model raised fears that US AI producers and their suppliers would capture less of the gains from AI.

2. Broad AI worries (3 Feb-5 Feb 2026). Hyperscaler earnings fueled worry about the

ability to sustain capital spending at high rates.

3. Payroll-driven rates spike (5 Jun 2026). Strong payrolls release led to increased expectations of Fed tightening and higher yields across the US curve.

4. Google issuance (2 Jun 2026). Google announces equity issuance to fund AI capex needs.

5. Meta cloud business (1 Jul 2026). Meta announced that it would build out a new cloud business and sell excess compute.

Exhibit 4: Recent events illustrate the differing cross-asset footprint to different kind of shocks

<table><tr><td rowspan="2"></td><td colspan="3">&quot;Aggregate&quot;/&quot;Macro&quot;</td><td colspan="2">&quot;Distributional&quot;</td></tr><tr><td>DeepseekJan. 27 2025</td><td>Broad AI WorriesFeb. 3 - Feb. 5 2026</td><td>Payroll-DrivenRates SpikeJun. 5 2026</td><td>Google IssuanceJun. 2 2026</td><td>Meta CloudBusinessJul. 1 2026</td></tr><tr><td colspan="6">Equities</td></tr><tr><td>S&amp;P 500</td><td>-1.5%</td><td>-1.7%</td><td>-2.6%</td><td>0.1%</td><td>-0.2%</td></tr><tr><td>Russell 2000</td><td>-1.0%</td><td>-2.7%</td><td>-3.5%</td><td>0.9%</td><td>-0.4%</td></tr><tr><td>Nasdaq 100</td><td>-3.0%</td><td>-3.1%</td><td>-4.8%</td><td>0.5%</td><td>-1.5%</td></tr><tr><td>Europe</td><td>-0.6%</td><td>-1.2%</td><td>-0.4%</td><td>1.4%</td><td>-0.6%</td></tr><tr><td>Japan</td><td>-3.5%</td><td>-0.4%</td><td>-5.5%</td><td>0.4%</td><td>-2.2%</td></tr><tr><td>Mainland China</td><td>0.9%</td><td>-1.3%</td><td>-2.0%</td><td>2.9%</td><td>1.2%</td></tr><tr><td>EM</td><td>-1.8%</td><td>-1.8%</td><td>-6.5%</td><td>1.0%</td><td>-2.8%</td></tr><tr><td>Korea</td><td>-2.4%</td><td>-3.3%</td><td>-14.1%</td><td>-1.0%</td><td>-8.1%</td></tr><tr><td>Taiwan</td><td>-5.6%</td><td>-1.4%</td><td>-7.3%</td><td>0.6%</td><td>-2.7%</td></tr><tr><td>VIX</td><td>20.5%</td><td>20.9%</td><td>39.7%</td><td>-1.7%</td><td>0.9%</td></tr><tr><td>GS US Cyclicals (GSXUCYCL)</td><td>-0.2%</td><td>0.5%</td><td>-1.5%</td><td>1.0%</td><td>0.3%</td></tr><tr><td>GS US Defensives (GSXUDEFS)</td><td>1.9%</td><td>1.3%</td><td>1.1%</td><td>0.2%</td><td>0.5%</td></tr><tr><td>SPX ex. AI (SPXXAI)</td><td>1.2%</td><td>0.0%</td><td>0.0%</td><td>-0.2%</td><td>0.8%</td></tr><tr><td>GS US Broad AI Basket (GSTMTAIP)</td><td>-9.5%</td><td>-6.0%</td><td>-6.8%</td><td>3.2%</td><td>-4.5%</td></tr><tr><td>Semiconductors (SOXX)</td><td>-7.8%</td><td>-4.3%</td><td>-10.4%</td><td>5.8%</td><td>-6.4%</td></tr><tr><td>GS Power Up America (GSENEPOW)</td><td>-13.7%</td><td>-4.9%</td><td>-3.5%</td><td>2.6%</td><td>-3.6%</td></tr><tr><td>GS US Hyperscalers (GSXUHYPR)</td><td>-2.8%</td><td>-5

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
