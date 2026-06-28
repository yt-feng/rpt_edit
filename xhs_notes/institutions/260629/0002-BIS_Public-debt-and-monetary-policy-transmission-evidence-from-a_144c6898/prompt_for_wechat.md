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
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/37327e42efcc31e58e000f2e9774e5c909cdcb093147818c56603ab35b98e18f.jpg)

## BIS Working Papers No 1365

Public debt and monetary policy transmission: evidence from advanced and emerging Europe

by Christopher Johns, Aaron Mehrotra and Fabrizio Zampolli

Monetary and Economic Department

June 2026

JEL classification: E31, E52, E62, E63

Keywords: monetary policy transmission, government debt, debt maturity, policy spillovers

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).

ISSN 1020-0959 (print)
ISSN 1682-7678 (online)

# Public debt and monetary policy transmission: evidence from advanced and emerging Europe

Christopher Johns\* Aaron Mehrotra† Fabrizio Zampolli‡

First version: 1 September 2025
Latest version: 25 June 2026

## Abstract

Using high-frequency euro area monetary policy shocks and panel local projections for the period 2001-2020, this paper examines how macroeconomic variables respond based on the level and the maturity structure of public debt. The results show that public debt plays a significant role in influencing monetary policy transmission. Higher public debt is associated with a weaker response of prices and inflation expectations to tighter monetary policy, while output declines at least as much as in low-debt economies. The maturity structure of debt also matters in a non-linear way: debt at intermediate maturities is associated with weaker effects, whereas debt at very short and long maturities is associated with stronger effects. Fiscal responses indicate a lack of contemporaneous fiscal backing, as primary balances tend to deteriorate following monetary tightening. Finally, for non-euro area European economies, the paper introduces a novel dataset on public debt maturity profiles and shows that spillovers from euro area monetary policy depend on the maturity structure in the receiving economy.

JEL Codes: E31; E52; E62; E63.

Keywords: Monetary policy transmission, government debt, debt maturity, policy spillovers.

## 1 Introduction

In standard models of monetary policy, public debt is assumed to have no role. Policy rate changes affect output through conventional channels such as intertemporal substitution, credit conditions and asset prices, and influence prices through the Phillips curve. While interest rate changes do have fiscal consequences, these models rely on the implicit assumption that such effects are offset by corresponding adjustments in fiscal policy (e.g. Woodford, 2001; Gali, 2015). Consequently, neither the level nor the maturity profile of public debt affects monetary transmission.

However, with high public debt levels, this assumption may no longer be innocuous. Changes in monetary policy affect not only private borrowing costs but also government interest payments, the income earned by government bondholders and the market value of outstanding public debt. Specifically, three channels are particularly relevant.

A first channel operates through fiscal risk repricing. When monetary policy tightens, government interest payments rise and the fiscal outlook may worsen. Financial investors may then reassess fiscal risk, causing spreads and term premia to widen (e.g. Corsetti et al., 2013; Gorea et al., 2026). This can amplify the tightening of financial conditions that normally follows higher policy rates and strengthen the contractionary effect on output. The impact on inflation is more ambiguous. Weaker output may be disinflationary, but a deterioration in the perceived fiscal outlook may also lead to currency depreciation and higher import prices, raise inflation expectations or make them less well anchored (Gorea et al., 2026; Bianchi et al., 2026).

A second channel operates through valuation effects. All else equal, a monetary tightening lowers the market value of outstanding government bonds. This generates capital losses for investors and financial institutions holding public debt. These losses can reduce wealth and weigh on spending (Caramp and Silva, 2023, 2024; Caramp and Feilich, 2024).

They can also erode the risk-bearing capacity of financial institutions and tighten credit supply, thereby reinforcing the contractionary effects of monetary policy on output. $^{1}$ Unlike fiscal risk repricing, this channel need not weaken the disinflationary effect of monetary policy. By weighing on demand, valuation losses can instead reinforce disinflation.

Finally, a third channel operates through interest income effects. Higher policy rates raise the income paid by the government to bondholders. If this additional income is not offset by higher taxes or lower transfers, it can support aggregate spending (Caramp and Silva, 2023, 2024; Caramp and Feilich, 2024). The interest income channel can therefore attenuate the contractionary effects of monetary tightening on output and weaken its disinflationary impact.

The quantitative importance of these channels depends on level of public debt, its maturity profile and the fiscal response. The debt level determines the scale of the effects: a larger debt magnifies the increase in interest payments, the transfer to bondholders, the valuation losses and the scope for fiscal risk repricing. The maturity profile determines their timing and relative strength. Shorter maturities speed up the pass-through of policy rates to government interest payments and bondholder income, strengthening the income channel and potentially increasing rollover risk. Longer maturities delay the rise in interest income but make bond prices more sensitive to changes in yields, strengthening the valuation channel. Finally, the fiscal response determines whether these income and valuation effects are offset or allowed to affect aggregate demand. If fiscal policy provides full backing, the effects of public debt on monetary transmission may be muted. If fiscal backing is partial, delayed or negative, the level and maturity structure of public debt can materially affect the response of output and prices to monetary policy shocks.

Recent theoretical studies have explored some of these mechanisms. Namely, Caramp and Silva (2023), Caramp and Silva (2024) and Caramp and Feilich (2024) study the valuation and income effects associated with public debt holdings and the role of fiscal backing. Yet they do not consider financial intermediation or default risk. Other work highlights the importance of the fiscal response to monetary policy (Kaplan et al., 2018). Despite the valuable insights provided by these studies, the net effect of various channels remains difficult to sign ex-ante. Fiscal risk repricing, valuation, and interest income effects may operate in opposite directions. Thus, whether public debt ultimately strengthens or weakens monetary policy transmission remains an empirical question.

In this paper, we address this question for the euro area and for European economies outside the euro area. The euro area is a useful setting because, despite sharing a common monetary policy, member states differ substantially in their fiscal positions and debt management policies. This diversity provides a rich setting for testing the "public debt channels" of monetary policy transmission. Moreover, while some recent studies explore these channels in the context of the United States (De Luigi and Huber, 2018; Caramp and Feilich, 2024; Andreolli, 2023) and the United Kingdom (Andreolli, 2023), there remains a gap in the literature for the euro area. Euro area monetary policy also affects European countries outside the euro area, not least given tight trade and financial linkages (e.g. Pot-jagailo, 2017). Thus, this paper also examines whether the level and maturity structure of domestic public debt also help to explain cross-country differences in the strength of monetary policy spillovers to non-euro area European economies.

Our empirical approach is to estimate the effects of euro area monetary policy shocks using panel local projections (Jordà, 2005) over the period 2001-2020. Monetary policy shocks for the euro area are obtained from Jarociński and Karadi (2020), who identify them at high frequency around monetary policy announcements. We interact these shocks with variables capturing the level and the maturity composition of public debt. $^{2}$

In particular, we represent public debt using detailed security-level data from De Graeve and Mazzolini (2023), which we extend by constructing comparable data for Greece after 2012. For each country-quarter, we decompose the government's repayment schedule into four maturity buckets: debt falling due within 9 months, between 9 months and 4 years, between 4 and 8 years, and after 8 years. This four-bin structure provides a parsimonious way to capture the main points along the maturity spectrum (Barrett and Johns, 2024): $^{3}$ very short-term debt, where policy rates pass quickly into fiscal costs and bondholder income; intermediate maturities; and longer-term debt, where valuation effects are stronger. Each bucket is measured as the amount of debt in that maturity range, expressed as a share of GDP. Since the four buckets add up to total public debt as a share of GDP, the specification allows us to study not only whether total debt matters for monetary transmission, but also whether the effects depend on where debt is located along the maturity profile. We do so by interacting the monetary policy shock with the lagged debt-to-GDP ratio in each maturity bucket.

We first use the estimated model to examine the role of the size of public debt. To separate debt size from maturity composition, we compare monetary transmission under counterfactual debt ratios of 60% and 120% of GDP while keeping the maturity profile fixed at the sample average. In practice, this means that the higher and lower debt stocks are distributed across the four maturity buckets in the same proportions. The results suggest that high debt does alter monetary transmission. Under higher public debt, contractionary monetary policy shocks are associated with a weaker response of prices – the difference relative to the low debt case is statistically significant. Inflation expectations also fall by less in high-debt countries than in low-debt ones. The output contraction is larger under high debt, although the difference is mostly not statistically significant. The weaker response of prices under high debt is consistent with the "stepping on a rake" logic in Sims (2011), whereby higher interest rates may have less disinflationary traction when fiscal backing is incomplete. $^{4}$

We then examine the role of the maturity profile itself. The evidence points to a highly non-linear relationship between debt maturity and monetary transmission. Debt at intermediate maturities is associated with smaller responses of output and prices to monetary policy shocks. By contrast, debt at very short and long maturities is associated with larger responses. These results are consistent with the interaction of the three channels described above: very short maturities make fiscal balances and refinancing needs more sensitive to policy rates, intermediate maturities may allow interest income effects to partly offset valuation effects, and longer maturities strengthen valuation effects. We also show that the results do not depend on including periods of elevated sovereign risk in the estimation and are therefore more general in nature.

The fiscal response helps to explain why public debt matters for monetary transmission. Following contractionary monetary policy shocks, primary balances deteriorate and public debt rises relative to GDP. Expected long-term sovereign yields also increase, while expected bond returns fall. These findings suggest that the effects of monetary policy on the government balance sheet, bondholder income and bond valuations are not fully neutralised by fiscal policy.

Finally, we examine spillovers to European economies outside the euro area. We first show that euro area monetary tightening has contractionary spillover effects on output and prices in advanced and emerging European economies outside the monetary union. This is consistent with close trade integration with the euro area and with previous evidence on spillovers to central and eastern Europe (Colabella, 2021; Feldkircher and Schuberth, 2023; Potjagailo, 2017; Horvath and Voslarova, 2017). We then construct a new security-level dataset of central government debt maturity profiles for ten central and eastern European (CEE) economies. $^{5}$ The maturity profile of public debt in the "receiving" economy matters for these spillovers: effects are strongest when more debt matures between 4 and 8 years. This suggests that valuation effects of government debt holdings are also relevant for the international transmission of monetary policy.

Relationship with the literature. This paper contributes to several strands of literature. The first is the literature on fiscal-monetary interactions and the role of public debt in monetary policy transmission. Standard New Keynesian models typically assume that the fiscal consequences of monetary policy are offset by fiscal policy so that public debt does not independently influence monetary transmission (Woodford, 2001; Gali, 2015). $^{6}$ Recent work relaxes this assumption and shows that government debt can affect monetary transmission through valuation and interest income effects generated by changes in interest rates. It also shows that the macroeconomic relevance of these effects depend on fiscal backing and debt maturity (e.g. Kaplan et al., 2018; Caramp and Feilich, 2024; Caramp and Silva, 2023, 2024; Cochrane, 2022, 2023; Smets and Wouters, 2024). Our paper brings these mechanisms to the data by estimating how the level and maturity structure of public debt condition the response of output and prices to monetary policy shocks.

A second, closely related, strand of literature studies whether these debt-related channels are empirically relevant. Evidence remains limited. Caramp and Feilich (2024) find that monetary policy has less traction on industrial production and unemployment in the

United States when federal debt is high, while De Luigi and Huber (2018) find that the effects of monetary policy are stronger when the debt-to-GDP ratio is rising. Andreolli (2023) also studies related channels in the United States and the United Kingdom. Our paper differs in three respects. First, it focuses on the euro area, where a common monetary policy coexists with heterogeneous national fiscal positions and debt management policies. Second, it studies not only the level of public debt but also its maturity distribution. Third, it shows that maturity matters in a non-linear way: debt at intermediate maturities is associated with weaker transmission, while debt at very short and longer maturities is associated with stronger effects.

The paper also contributes to the literature on fiscal policy and monetary transmission in the euro area. Afonso et al. (2023) and Kloosterman et al. (2024) show that the fiscal stance and fiscal regimes affect the transmission of monetary policy. We add to this literature by focusing on the maturity structure of the public debt stock rather than only the fiscal stance or fiscal reaction function. The results show that primary balances deteriorate and debt rises following contractionary monetary policy shocks, pointing to a lack of contemporaneous fiscal backing over the sample period. This helps explain why the interest income and valuation effects associated with public debt holdings are not fully neutralised by fiscal policy.

The paper is also related to the literature on sovereign risk, financial fragility and heterogeneous monetary transmission. Corsetti et al. (2013) show how sovereign risk can amplify macroeconomic fluctuations by tightening private sector financing conditions. Gorea et al. (2026) provide evidence that fiscal risk shocks tighten financial conditions, weigh on activity and affect inflation, with the effects depending on the monetary policy response. Previous studies further show that sovereign risk can affect the bank lending channel and contribute to cross-country differences in the transmission of monetary policy in the euro area (Cantero-Saiz et al., 2014; Ciccarelli et al., 2014; Grandi, 2019; Cantero-Saiz et al.,

2022). Other studies document heterogeneous effects of unconventional monetary policy across euro area countries, in part depending on sovereign risk and financial fragility (Al-tavilla et al., 2016; Boeckx et al., 2017; Burriel and Galesi, 2018; Hristov et al., 2021). Our contribution is to show that debt maturity provides an additional source of heterogeneity. The maturity profile affects the relative strength of fiscal risk repricing, valuation effects and interest income effects. The results do not appear to be driven only by periods of elevated sovereign stress.

Finally, the paper contributes to the literature on euro area monetary policy spillovers to central and eastern Europe. Existing work shows that euro area monetary policy shocks affect output, prices and financial conditions in non-euro European economies, reflecting close trade and financial linkages (Potjagailo, 2017; Horvath and Voslarova, 2017; Colabella, 2021; Feldkircher and Schuberth, 2023). To our knowledge, this literature has not examined whether the level and debt maturity structure of public debt in the receiving economy conditions these spillovers. We address this gap by constructing a new security-level dataset of central government debt maturity profiles for ten central and eastern European economies and showing that spillovers are strongest when more debt matures between 4 and 8 years.

The rest of this paper is structured as follows. Section 2 describes the methodology and the data. Section 3 presents the empirical results. Section 4 concludes.

## 2 Methodology and data

In order to examine how public debt affects the transmission of monetary policy, we analyse the effects of monetary policy shocks conditional on the level and maturity of public debt. As the estimation framework, we use panel local projection regressions. These amount to flexible sequential regressions where the dependent variable is shifted forwa

[中间内容因长度限制已省略]

c activity,” NBER Working Paper 830, National Bureau of Economic Research.

GALI, J. (2015): Monetary Policy, Inflation, and the Business Cycle: An Introduction to the New Keynesian Framework and Its Applications Second edition, vol. None of Economics Books, Princeton University Press, 2 ed.

GARCIA-DE ANDOAIN, C. AND M. KREMER (2017): “Beyond spreads: Measuring sovereign market stress in the euro area,” Economics Letters, 159, 153–156.

GOREA, D., D. X. NG, AND F. ZAMPOLLI (2026): “The financial and real effects of fiscal risk,” Bis working papers, Bank for International Settlements, forthcoming.

GRANDI, P. (2019): “Sovereign stress and heterogeneous monetary transmission to bank lending in the euro area,” European Economic Review, 119, 251–273.

HORVATH, R. AND K. VOSLAROVA (2017): “International spillovers of ECB’s unconventional monetary policy: the effect on Central Europe,” Applied Economics, 49, 2352–2364.

Hristov, N., O. Hülsewig, and J. Scharler (2021): “Unconventional Monetary Policy Shocks in the Euro Area and the Sovereign-Bank Nexus,” International Journal of Central Banking, 17, 337–383.

JAROCIŃSKI, M. AND P. KARADI (2020): “Deconstructing Monetary Policy Surprises—The Role of Information Shocks,” American Economic Journal: Macroeconomics, 12, 1–43.

JOHNS, C., A. MEHROTRA, AND F. ZAMPOLLI (2026): “Sovereign risk and monetary policy transmission: Evidence from the euro area,” Economics Letters, 260, 112817.

JORDÀ, O. (2005): “Estimation and Inference of Impulse Responses by Local Projections,” American Economic Review, 95, 161–182.

KAPLAN, G., B. MOLL, AND G. L. VIOLANTE (2018): “Monetary Policy According to HANK,” American Economic Review, 108, 697–743.

KLOOSTERMAN, R., D. BONAM, AND K. VAN DER VEER (2024): “The effects of monetary policy across fiscal regimes,” Journal of Macroeconomics, 81.

MEHROTRA, A. AND J. YETMAN (2018): “Decaying Expectations: What Inflation Forecasts Tell Us about the Anchoring of Inflation Expectations,” International Journal of Central Banking, 14, 55–101.

POTJAGAILO, G. (2017): “Spillover effects from Euro area monetary policy across Europe: A factor-augmented VAR approach,” Journal of International Money and Finance, 72, 127–147.

SIMS, C. A. (2011): “Stepping on a rake: The role of fiscal policy in the inflation of the 1970s,” European Economic Review, 55, 48–56, special Issue on Monetary and Fiscal Interactions in Times of Economic Stress.

SMETS, F. AND R. WOUTERS (2024): “Fiscal backing, inflation and US business cycles,” CEPR Discussion Papers 19791, Centre for Economic Policy Research.

SWINKELS, L. (2019): “Treasury Bond Return Data Starting in 1962,” Data, 4.

TENREYRO, S. AND G. THWAITES (2016): “Pushing on a String: US Monetary Policy Is Less Powerful in Recessions,” American Economic Journal: Macroeconomics, 8, 43–74.

TOBIN, J. (1963): “An essay on principles of debt management,” in Fiscal and Debt Management Policies, Englewood Cliffs, NJ: Prentice-Hall, 143–218, in Commission on Money and Credit; reprinted in J. Tobin, Essays in Economics, Vol. 1, North-Holland, Amsterdam, 1971.

WOODFORD, M. (2001): “Fiscal Requirements for Price Stability,” Journal of Money, Credit and Banking, 33, 669–728.

ZAMPOLLI, F. (2012): “Sovereign debt management as an instrument of monetary policy: an overview,” in BIS Papers, Bank for International Settlements, 65, 97–118.

## Appendix A: Additional Tables and Figures

![](images/0236afe73eb0c95ca325818f5d5f483288eddf2f39c5534f3f3a227e242f11ae.jpg)  
Figure A.1: Euro area government debt maturity profile, by select maturity bins. Note: The maturity profile is shown relative to the size of total debt. The line denotes the median, the box the interquartile range, and the whiskers the 25th (75th) percentiles minus (plus) 1.5 times the interquartile range. The dots correspond to outliers.

![](images/1c47761d9bd4923dd2f6e7efc9586553cb74dc8cb0a12e686d4d8d8ea2ecb723.jpg)  
Figure A.2: Comparison of responses of one-year-ahead inflation expectations to MP shock for countries at different levels of public debt, with a fixed maturity structure. Note: Hollow points denote statistical insignificance (< 90% confidence) between responses under high and low debt.

## A.1 Novel government debt maturity data for Greece and 10 CEE countries

Table A.1: Novel government debt maturity structure sources

<table><tr><td>Country</td><td>Date Range</td><td>Source</td></tr><tr><td>Greece</td><td>2012Q1 - 2020Q4</td><td>Public Debt Management Agency</td></tr><tr><td>Bulgaria</td><td>2006Q4 – 2020Q4</td><td>Ministry of Finance</td></tr><tr><td>Croatia</td><td>2004Q1 – 2020Q4</td><td>Ministry of Finance</td></tr><tr><td>Czech Republic</td><td>2009Q1 – 2020Q4</td><td>Ministry of Finance</td></tr><tr><td>Hungary</td><td>2004Q4 – 2020Q4</td><td>Government Debt Management Agency (AKK)</td></tr><tr><td>Latvia</td><td>1999Q1 – 2020Q4</td><td>Treasury</td></tr><tr><td>Lithuania</td><td>1999Q1 – 2020Q4</td><td>Ministry of Finance</td></tr><tr><td>Poland</td><td>1999Q1 – 2020Q4</td><td>Ministry of Finance</td></tr><tr><td>Romania</td><td>2008Q4– 2020Q4</td><td>Ministry of Finance</td></tr><tr><td>Slovakia</td><td>1999Q1 –2020Q4</td><td>National Bank of Slovakia&amp; Debt and Liquidity Management Agency</td></tr><tr><td>Slovenia</td><td>1999Q1–2020Q4</td><td>Ministry of Finance</td></tr></table>

![](images/143f393046704b792071759d1879b667876c9b8d71442f53fc8095a63296ab86.jpg)  
Figure A.3: Detailed maturity structure of CEE countries at the end of 2019

![](images/39df40569e6a974a6dd5194605040035751087d23dacb26c300dd0485026bf21.jpg)  
Residual Maturity (years)  
Figure A.4: Detailed maturity structure of CEE countries at the end of 2019, as percent of GDP
"""
