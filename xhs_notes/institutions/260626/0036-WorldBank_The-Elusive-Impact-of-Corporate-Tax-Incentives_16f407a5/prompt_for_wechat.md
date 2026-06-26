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
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# The Elusive Impact of Corporate Tax Incentives

Massimiliano Calì

Giorgio Presidente

Thiago Scot

POLICY RESEARCH WORKING PAPER 11061

## Abstract

Despite the large fiscal footprint of corporate tax incentives, limited causal evidence exists on their impact on economic outcomes. This paper helps fill this gap by exploiting the phasing out of a large income tax exemption scheme for export-oriented firms in Tunisia. Using data on the universe of registered Tunisian firms, the analysis shows that the reform caused a decline in the entry of new firms in the sector previously benefiting from the incentives. However, the reduced entry did not translate into any effects on employment, revenue, or the wage bill, as the reform did not impact the activities of incumbent firms, which account for the bulk of economic activity in Tunisia. The findings are robust to addressing various threats to the empirical identification, and they confirm emerging evidence casting doubt on the importance of tax incentives to determine investments relative to other factors in an economy.

![](images/b6c03d33941146a2a04a4998f26c388f0b90b042163e6452c25c63933003b1b1.jpg)

# The Elusive Impact of Corporate Tax Incentives

Massimiliano Calì $^{*1}$ , Giorgio Presidente $^{2}$ , and Thiago Scot $^{3}$

$^{1}$ World Bank

$^{2}$ Bocconi University

$^{3}$ World Bank

Keywords: Tax Incentives, Corporate Income Tax, Export-oriented firms, Business Investment

JEL classification: H25, H32

## 1 Introduction

Tax incentives are a ubiquitous component of policies aiming to attract investment and boost exports. OECD (2022) estimates that in 2022, 87% of the 52 developing economies surveyed had at least one type of Corporate Income Tax (CIT) exemption, while 69% and 65% had at least one type of reduced CIT rate or tax allowance, respectively. These incentives are economically significant. According to data collected by Redonda et al. (2024), tax relief schemes to businesses amounted to 1.4% of global GDP and 7.8% of global tax revenues in 2021.

In spite of the large footprint of these incentives, there is limited evidence on their causal impact on economic outcomes. A key reason is that changes in taxation are often bundled within broader policy packages that provide a wide range of benefits for affected firms. Special Economic Zones are a case in point. These regimes often include preferential customs rules, flexibility in labor regulations, and a range of tax benefits such as exemption from import duties, VAT on local purchases and, often, exemption on CIT. As the precise mix of benefits being offered varies among countries and over time, any assessment of one specific intervention will necessarily bundle all of these benefits together.

In this paper, we make progress in addressing the paucity of causal evidence by leveraging the phasing out of a large CIT exemption for export-oriented firms in Tunisia, during a period in which all other benefits remained unchanged. Tunisia is a lower-middle income country that has extensively relied on special regimes, the most important of which is the so-called offshore regime. This entails radically different institutions and rules for firms that export the majority of their sales. Until 2013, these firms were subject to a zero CIT rate on their profits, whereas onshore firms (i.e. all other firms outside the regime) faced a 30 percent CIT rate. This was the largest tax exemption scheme in Tunisia in the past decades. $^{1}$

Our identification leverages a large, arguably unanticipated policy shock. After almost a decade-long process to reduce the tax disparities between the two regimes, the CIT rate for offshores was raised to 10%, while the rate for onshore firms was reduced to 25%. Importantly, all other institutional features that benefited export-oriented firms remained unaffected.

We employ a differences-in-differences approach to assess the impact of the CIT rate increase on firms by comparing outcomes of interest for offshores versus onshore firms before and after the shock. The comparison is based on the universe of registered Tunisian firms, for which we collect administrative data from registries, social security, customs and tax records, to estimate the causal impact of the CIT reform on economic activity.

The key identifying assumption is that trends in the offshore and onshore sectors would have been similar absent the reform. We provide evidence in favor of that assumption, showing that onshore and offshore sectors often had very similar pre-reform trends, and also by documenting that our results are robust to a wide battery of aggregate and firm-level tests. These include robustness checks based on alternative samples which maximize the comparability of treated and untreated firms, as well as on a propensity-score matching estimator re-weighting firms on their observable characteristics. The results are also robust to controlling for possible shocks which could have differential impacts on offshore and onshore firms, including EU import demand, exchange rate and domestic demand.

The results at the extensive margin show that the number of firms in both the offshore and onshore sectors were growing significantly in the four years before the reform. $^{2}$ However, these trends diverged starkly in 2014, the first year of the reform. We estimate that relative to the counterfactual growth proxied by onshore firms, the number of offshore firms dropped by 20% four years after the reform. This effect is almost completely driven by a reduction in entry of new offshore firms after the change in policy, not by an increase of exit among incumbents.

The stark relative decrease in the number of offshore firms did not translate into a relative decrease in economic activity in the offshore sector. The differences-in-differences estimates of the impact of CIT rate increase on employment, wage bill and gross revenue of the offshore sector are all null. If anything, we find small increases in aggregate economic activity among manufacturing firms in the offshore sector, but the estimates are imprecise.

To explain the apparently inconsistent findings of a large fall in the number of entrants and no changes in aggregate activity, we turn to more granular data. First, we find that entrant firms are typically very small and that economic activity in the offshore sector is highly concentrated in a few, large incumbents remaining largely active in the post-reform period. Second, the differences-in-differences analysis on a balanced firm-level panel shows that the CIT reform has no significant effects on the employment, wage bill and revenue of offshore incumbents.

Taken together, our results strongly reject the hypothesis that the increase in corporate income taxes led to a decrease in aggregate economic activity, or that they hampered the performance of firms subject to the CIT rate increase.

Like our paper, several other empirical contributions document a limited economic effect of CIT reform. Buba and Wong (2017) review the literature on SEZ and conclude that despite their ability to attract foreign investment and boost exports, their impacts on employment and spillovers to other local firms are unclear. Interviewing management from firms in SEZ across countries, Frick and Rodríguez-Pose (2023) document that factors such as infrastructure, labor costs and political stability are more important for investment than tax benefits. We add to this evidence by focusing on the specific role of corporate income taxes in developing economies – which is crucial given their typical fiscal needs – independently of other policy measures.

Beyond developing economies, survey evidence from small and medium enterprises (SMEs) often points to other barriers such as financial constraints and regulatory burden, as much more relevant to business decisions (Ravšelj et al., 2019; Wang, 2016). Gordon and Li (2009) conclude that the most important tax provision to encourage risk-taking by corporations is beneficial treatment of losses (e.g. allowing it to be deducted from payroll taxes), rather than lowering tax rates. Akcigit and Ates (2023) use an estimated general equilibrium model to perform policy simulations and do not find significant effects of increasing CIT. Harju et al. (2022) estimate null effects of a corporate tax cut in Finland on the average level of investment for affected firms. In a review of 42 studies, Gechert and Heimberger (2022) find that corporate tax cuts have very limited, if any, effect on growth. $^{3}$ This result is also consistent with other studies analyzing the impact of tax competition for foreign direct investment (FDI) across countries. Using a panel of 40 economies in Latin America and the Caribbean, Klemm and Van Parys (2012) find that CIT incentives attract FDI, but do not boost gross private fixed capital formation or growth.

Yet, there does exist evidence that firms respond to changes in the tax rate (e.g. Ohrn, 2019; Ohrn et al., 2022; Cummins et al., 1994). Ohrn (2018) finds that a 1 p.p. decrease in effective tax rate in a program to encourage domestic manufacturing in the US, increased investment by more than 4%. Zwick and Mahon (2017) show that accelerated depreciation provisions in the US were effective in increasing eligible capital, particularly for small firms. Bilicka (2020) shows that the investment of Canadian firms responds strongly to a tax reform that changed cash flow availability. Our contribution is closely related to Chen et al. (2023), who study the impacts of a tax cut for domestic firms versus foreign-oriented firms in China. Their focus is on explaining how CIT cuts affect the structure of exports, documenting an increase in product concentration in response to a decrease in CIT rates.

Our paper contributes to partially reconcile these mixed findings by documenting a nuanced effect of a CIT reform: significant aggregate effects do not necessarily imply significant economic effects. In this sense, our paper is closely related to Gordon and Li (2009), who study how the tax system affects the decision of individuals to start businesses. They conclude that changes in corporate tax rates might affect the decision of entrepreneurs to incorporate – akin the decline in entry documented in this paper – but that does not mean that new economic activity is being generated, just that income is being shifted from unincorporated activities to incorporated ones. That is a similar result to Damgaard et al. (2024), who separate phantom FDI, investments into empty corporate shells with no link to the local real economy, and real FDI. They find a positive impact of lower CIT rates on total FDI across countries, but zero impact on real FDI.

The rest of the paper is organized as follows. The next section provides the institutional context including the background of the tax reform; sections 3 and 4 describe the data and the empirical methodology, respectively; section 5 presents the results at the sectoral- and firm-levels; and section 6 concludes and discusses the policy relevance of the findings.

## 2 Institutional Context and Policy Background

Tunisia has long maintained a preferential regime aimed to attract and facilitate the activities of exporting firms, which are defined as those that export at least 70% of their output. This regime comprised generous tax and fiscal benefits since its creation in 1972, including duty-free imports and income tax exemptions. Additional benefits include "streamlined customs procedures, corresponding to significant costs savings" and the possibility of holding bank accounts in foreign currency, which protects against currency risks (Nucifora and Rijkers, 2014). $^{4}$

While the establishment of the offshore regime was associated with growth in export oriented investment, it also came at a high fiscal cost. A study by the IFC and ECOPA (2012) estimates that the offshore income tax exemption accounted for two-thirds of the total fiscal and financial incentives granted by Tunisia in 2009. Using administrative firm-level data (described below), we estimate that the fiscal cost of this offshore exemption was worth 2.4 billion Tunisian dinars in 2013, equivalent to 6.8% of GDP or 14.7% of overall tax revenues. $^{5}$ While this is an upper-bound estimate, it illustrates the significant order of magnitude of the offshore tax holiday scheme. $^{6}$

## 2.1 The corporate tax reform

The desire of harmonizing the tax treatment between the two regimes paved the way for the 2014 corporate tax reform, which is the focus of our study. This was the first and arguably most important step in the process of convergence of tax rates between the offshore and onshore sectors. Up to that moment, offshore firms were fully exempt from paying income tax on their profits, while onshore firms paid a standard rate of 30%. This full exemption had been applied since the establishment of the offshore regime in 1972 (Law 72-38). The law established this exemption for the first 10 years of the offshore firm, after which it would face a reduced rate of 10% for a further 10 years before paying the full general rate.

However, the full exemption was eventually renewed upon its expiration by successive laws so that it remained in force for the subsequent decades. At the end of 2006 the authorities decided to eliminate this tax exemption altogether by applying a reduced tax rate of 10% on new offshore firms' profits starting in 2008 (Law 2006-80). Once again subsequent budget laws postponed the application of this new regime, thus leaving the full exemption in place until 2013, when the law 2006-80 was finally applied (see Figure 1 for a summary of the timeline). The continuous postponements over four decades created an environment where firms would consider this exemption valid indefinitely. Discontinuing this tradition of postponements in 2013 with the subsequent enforcement of the phase-out in 2014 arguably came as a surprise for firms, which helps the identification of its effects.

The 2006-80 law maintained a 10-year grace period from the date of incorporation for all existing firms as of the end of 2013. That means, for instance, that a firm incorporated in 2004 would immediately face the new CIT rate in 2014, while one incorporated in 2008 would only face the new rate starting in 2018; those incorporated in 2013 would face zero rate until 2023. We discuss below in more details how we deal with that lagged implementation in our empirical exercises, including by isolating the effects for firms liable to pay corporate taxes upon the enactment of the reform. However we note here that in a fundamental sense this implementation does not mean that some firms were only "treated" after 2014. Forward-looking firms make entry, investment and hiring decisions, for example, with the goal of maximizing firm value, taking into account the entire flow of future after-tax profits, not only the present period. In that sense, we can consider this staggered adoption as treating all firms but with somewhat different intensities.

At the same time in 2014, the general corporate tax rate was lowered from 30% to 25%. Thus, half of the onshore-offshore rate differential was eliminated in 2014. This convergence process continued in 2019 when the tax rate for offshore firms was further increased to 13.5% and was finalized in 2021 when both the onshore and offshore tax rates were set to 15%. We do not include this further convergence period in the analysis for two reasons. First, it was arguably not as unexpected as the 2014 reform, which came on the heel of many years of deferral. Second, these additional reforms coincided with the Covid period, which would make the identification of impacts particularly challenging. It is also worth noting that onshore firms in a number of sectors faced a higher rate (35%) than the general rate throughout the period. These sectors, including for instance credit, insurance, oil refining, car dealership and hyper-markets, comprise a relatively small share of firms, which we exclude from the subsequent analysis.

According to data from Tunisia's Ministry of Finance, the tax reform was associated with a reduction in corporate income tax revenues for the fiscal year 2014 (and collected in 2015). Overall tax revenues from non oil companies dropped by $28\%$ to TD 1.6 billion dinars mainly driven by the rate reduction for onshores, which still represented the bulk of CIT collection. $^{7}$ Revenues from offshore represented around $4.4\%$ of total CIT revenues, a share which eventually increased to $9.4\%$ by 2018.

Importantly for our analysis, the aggregate data also suggest that the reform was not accompanied by other tax relief measures that limited the increased tax burden for offshores in the face of the rate increase. In fact the effective tax rate imposed on offshores (calculated as paid tax/taxable profit) hovered even slightly above the actual 10% rate in the period 2014-18 (11.8%-13.8%). $^{8}$ That is due to the fact that offshores can sell up to 30% of their production in the domestic market, and the related profits are taxed at the general rate.

Figure 1: Timeline of reform.  
![](images/3dd5e5c19bc368e445221014b06d8890b1daef8ba7a42b84a16f4f58b61c3c52.jpg)  
Note: This timeline depicts the subsequent budget law postponements of the enforcement of the Corporate Income Tax (CIT) reform for Offshore firms, thus leaving the full exemption in place until 2013, when the law 2006-80 was finally applied.

## 3 Data and Descriptive Statistics

The main source of data we use are administrative records on Tunisian registered firms, the Repertoire National des Entreprises (RNE). This data spans the universe of all private and public sector firms and includes information such as firms' 4-digit economic activity sector, location, age and whether owners are foreign. $^{9}$ In joint collaboration with the Tunisian Statistics Institute (INS), the RNE microdata has been merged with tax returns to include yearly measures of firms' declared turnover, profits, and revenue from exports; social security data on total employment and wage bill; and customs data on total value of exports and imports. $^{10}$

We clean the data in a number of ways. In Figure A1 in the Appendix, we provide the key steps we take to arrive at our analysis sample. We start with a full panel of almost 16 million observations and almost 1.5 million firms between 1995 and 2021. First, we focus on the 2009 - 2018 period, since further corporate income tax reforms were introduced after 2018. We also drop firms that are not liable for income tax regimes; stat

[中间内容因长度限制已省略]

d of 2010). But note that in this setting the pre-trends suggest that, if there are any deviation from pre-trends, they might suggest a catch-up in the number of offshore firms, and not a divergence. Nonetheless, it is possible that, despite what we observe in the pre-trends, some other shock different from the reform we studied generated differential trends for the two groups - and this is precisely the sensitivity evaluated in this method. So what the results suggest is that, as long as parallel trends violation was smaller than approximately $4\%$ per year (100% of the largest pre-treatment violation), our results still suggest a significant impact of the reform.

In panels (d) and (e), we provide the analogous sensitive test for the full sample of firms, including all economic sectors. Here we note that the sensitivity CI are much larger, and considering deviations from parallel trends larger than 20% of the reference deviation yields CI that encompass zero effect. That effect is mostly driven by the fact that, in the period 2010, we estimate a large coefficient for offshore firms, of approximately 10%. Therefore, deviations of 40% are equivalent to 4%, or the reference deviation for the manufacturing sector. If we consider that deviations from parallel trends should not be substantially different in the full sample when compared to the manufacturing one, and that the 2010 coefficient is an outlier, then our results are similarly robust in the full sample, up to deviations of approximately 4% per year in the number of firms.

Figure A21: Honest DID - Industry-level impacts on Log(number of firms)  
![](images/57bec0236be577ebb58e7e2ba5ef041d41dfea76861ee38313a9f30d178a06b2.jpg)

(a) Original dynamic estimates (Fig 5a)  
![](images/74637225655f65d9df43b604dc4f721c0e97b1613c433914c8bde8084bd197b4.jpg)  
(b) Manufacturing - average post-period

![](images/b4e9bbf4c8a82e41deda1c1474da7b13ff7c2407d3cfb822212e980fa6098065.jpg)  
(c) Manufacturing - last post-period

![](images/384474981ab4f76ffc220eac996b859c67a3cb9485cab7488d403c923fba3389.jpg)  
(d) Full sample - average post-period

![](images/91ff875772f35bb40ae58e7f2dea15f1997ae666a15186e00a74671d25e13ad4.jpg)  
(e) Full sample - last post-period  
Note: Panel (a) reproduces Figure 5(a) in the main text, while remaining panels report results from the sensitivity tests in Rambachan and Roth (2023) for the described outcomes in the industry-level analysis. Mbar refers to multiples of the largest deviation from parallel trends in the pre-period (i.e. Mbar = 0.8 considers a deviation equals to 80% of the largest pre-period deviation).

Below we report similar results for the other main outcomes of interest - entry, exit, employment, wage bill and gross revenue. We first show results for the entire sample in Figure A22 and then for manufacturing firms only in Figure A23. In both cases, the only robust result to deviations from parallel trends is the decrease in firm entry for offshore firms after the reform: in both cases, deviations in parallel trends up to 40-50% of the largest pre-period deviation are still consistent with the significant results we estimate. For all other outcomes, in both samples, any small deviations yield insignificant results. As seen in Table 2, all estimates for average post-treatment effects are insignificant for the full sample, and any deviations would make CI even larger. For manufacturing, we estimate a marginally significant positive impact for offshore firms, but here we show that it is not robust to deviations from parallel trends: a 20% deviation would already yield CI that include null effects. These results are again consistent with our main findings of null effects across a range of economically relevant outcomes for offshore firms.

Figure A22: Honest DID - Industry-level impacts on full sample  
![](images/82297e7ecfe98160461d8ac2400189e7498375a9d7830c0e0a0e5b9eee169803.jpg)

(a) Entry  
![](images/12cdca40c7001df0321111301287abd1f3b2d04027ba5b8135145355f6ba9108.jpg)  
(b) Exit

![](images/3ddcf0b7db08705ce21fdb1e7cf70f4def7f568186032144ecd333f0b7f19ac3.jpg)  
(c) Employment

![](images/da665b537970ec457b7ee3eb7b1e8a3b63d91558fdcf42249aa95421c73a0f8f.jpg)  
(d) Wage Bill

![](images/285ec314085694e8a4e14bdcd61fd09fbf7a567645216a72e82e1ecc03410abb.jpg)  
(e) Revenue  
Note: These figures report results from the sensitivity tests in Rambachan and Roth (2023) for the described outcomes in the industry-level analysis. Estimates are for the average post-treatment effect. Mbar refers to multiples of the largest deviation from parallel trends in the pre-period (i.e. Mbar = 0.8 considers a deviation equals to 80% of the largest pre-period deviation).

Figure A23: Honest DID - Industry-level impacts on manufacturing sample  
![](images/b5c91993bd2c6ad56936b213f21dc4606cb3ffe01cd984ca613b350a975021f2.jpg)

(a) Entry  
![](images/408d28a342a78d88f31df54e6b70b77ad87e9a41848dc2d871e910b0649ddd5d.jpg)  
(b) Exit

![](images/91c29f543a6dc5b08c340587a5d01bf3c6744ca32c3be2186714f181bcfff1ae.jpg)  
(c) Employment

![](images/3a6e9166d468396585a31fe076d44352f00f10b3c4038db348dd6cad9fd9e5d8.jpg)  
(d) Wage Bill

![](images/9c796a2a9d79bfa3d13a78082a191903c1dd05ef62d3adf72d54570c80338053.jpg)  
(e) Revenue  
Note: These figures report results from the sensitivity tests in Rambachan and Roth (2023) for the described outcomes in the industry-level analysis. Estimates are for the average post-treatment effect. The sample is restricted to firms in the manufacturing sector. Mbar refers to multiples of the largest deviation from parallel trends in the pre-period (i.e. Mbar = 0.8 considers a deviation equals to 80% of the largest pre-period deviation).
"""
