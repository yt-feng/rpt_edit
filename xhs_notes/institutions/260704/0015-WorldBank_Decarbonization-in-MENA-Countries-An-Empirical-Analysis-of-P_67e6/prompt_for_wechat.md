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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Decarbonization in MENA Countries An Empirical Analysis of Policy Impacts

Hamid Mohtadi

Željko Bogetić

POLICY RESEARCH WORKING PAPER 11064

## Abstract

This paper empirically examines the multiple impacts of alternative, major fiscal instruments on decarbonization in countries in the Middle East and North Africa. It also examines the effects of decarbonization pathways on decarbonization, using a database covering 41 countries, including countries in the Middle East and North Africa region. The analysis uses several methods to compare and contrast the findings and test their robustness. These new estimates contribute to the literature seeking to understand the pros and cons and effectiveness of various policy instruments in promoting decarbonization, with particular focus on the Middle East and North Africa region. The principal findings include the following. Oil subsidies among the region's oil producers strongly and positively impact higher carbon dioxide emissions. This effect seems to work through the energy consumption path. Even after controlling the consumption effect, there remains a direct net effect of subsidies on carbon dioxide, likely arising from other sources such as manufacturing. Comparing three groups—all 41 countries, only countries in the Middle East and North Africa, and only oil producers in the Middle East and North Africa—the adverse effect of oil subsidies on carbon dioxide emissions matters only for oil producers in the Middle East and North Africa, not the other two groups. Flaring contributes to carbon dioxide emissions for oil producers in the Middle East and North Africa. Oil subsidies do not have a significant effect on short-run or long-run economic growth. Thus, reducing subsidies does not adversely impact economic growth. This is true for all countries, including oil exporters, in the Middle East and North Africa.

# Decarbonization in MENA Countries: An Empirical Analysis of Policy Impacts\*

Hamid Mohtadi and Željko Bogetić

JEL Classification: O44 (Environment and Growth), O47 (Empirical Studies of Economic Growth), H2 (Taxation, Subsidies and Revenues), Q4 (Energy), Q5 (environmental economics), O53 (Asia including Middle East), O55 (Africa)

## Decarbonization in MENA Countries: An Empirical Analysis of Policy Impacts

## 1. Introduction

The MENA countries collectively produced about only 5% of global greenhouse gas (GHG) emissions in 2019, a relatively small contribution compared, for example, to East Asia (27%) (Lienard, Brussels International Center, 2022) $^{1}$ (see the caveat at the end of this paragraph). Despite this modest contribution, there are several reasons to consider addressing GHG emissions in the Middle East and North Africa (MENA) region, of high priority. First, MENA's GHG emissions of 13 tons of CO2 per capita per year are just below North America's 19 tons and above Europe's 7.8 tons per capita per year (ibid.). Second, GHG production has been increasing in this region at a breathtaking pace (World Resources Institute, Insights, May 8, 2023). The case is even more dramatic among the Persian Gulf states. Qatar, for example, had the highest GHG emissions per capita in the world, rising by 30% over only 5 years from 2010 to 2015 (Lienard, Brussels International Center, 2022). Third, we will show in this paper that removal of carbon subsidies can be growth enhancing in the long run, even if not in the short run. Fourth, if mitigation strategies involve removal of subsidies, there may be local externality benefits (besides global ones) such as better health outcomes. This is because industrial processes that use or produce fossil fuels often involve health hazards with attendant impacts on fatalities and worker productivity (e.g., black lung disease in coal mining, and multiple diseases due to air pollution). Air pollution has been shown to result in large impacts, “causing more deaths globally than malnutrition, AIDS,

tuberculosis, and malaria combined." (Fuchs et al. 2023). As such, a transformation of the industrial base to renewables may well confer additional health benefits and reduce substantial fatalities. Finally, we will find in the paper that, while a large carbon tax is CO2-reducing, where fossil subsidies are large, their removal is the first best strategy. Since both subsidy removal and carbon taxes are needed to support decarbonization to a significant extent, this is a matter of practical sequencing because the introduction of the carbon tax requires more time than subsidy rationalization.

Beyond the above factors regarding the potential benefits of decarbonization for MENA's own citizens, there is an overwhelming reason why the world, as a whole, should care about decarbonization in MENA: its massive contribution to global climate change as the largest producer and exporter of fossil fuels to the world. In 2023 MENA's share of total world oil production stood at 36.1 percent and that of gas production in 2022 stood at 21.7 percent (U.S. Energy Information Agency, World Bank, and Tagliapietra 2019). Oil and gas production contribute 15 percent of global GHG as reported by the International Energy Agency (IEA 2023). Importantly, this figure does not include GHG produced in the “usage” or consumption of fossil fuels, such as, for example, in the transport sector. In 2021, CO2 emissions in the transport sector alone was 23 percent of all CO2 emissions worldwide (United Nations 2021). $^{2}$ With the transport sector added, this means that MENA's figure of 5% of global CO2 emission is likely vastly underestimated.

Much of the recent literature on decarbonization transition in oil producing countries has focused on the stranded asset problem (van der Ploeg and Rezai 2020, Semieniuk et al. 2022, Daumas, 2023). While this issue is of great importance for the oil producing MENA countries, little has been said about the actual

effectiveness of decarbonization policies in terms of actual reduction of GHGs as well as on the growth prospect of a future without oil in MENA. The latter is important because it can counter the secular economic downturn for MENA oil producers associated with a potential stranded assets risk.

Against this backdrop, the aim of this paper is (a), to gauge the effectiveness of GHG mitigation measures on CO2 emission reduction in MENA countries (b), to examine the pathway through which such GHG mitigation measure would work, and (c), to assess the impact of GHG mitigation measures on economic growth in MENA countries in both the short run and the long run. We do this by studying and comparing the effects of mitigation measures for three groups of countries: the MENA countries as a whole, the MENA oil producers, and the world.

Certainly, removing fuel subsidies or imposing a carbon tax are two effective ways in which countries can reduce their carbon footprint. While a carbon tax has been discussed as the most efficient carbon mitigation policy among various other policy instruments, for example by Timilsina (2022), such a comparison does not include comparing carbon taxes with the removal of fossil fuel subsidies as an alternative policy. Yet fossil fuel subsidies are the dominant fiscal instrument that results in underpricing of carbon, certainly among oil producers. So imposing a carbon tax alone will not be effective in changing the relative prices without eliminating massive underpricing of carbon as a result of fuel subsidies. For example, the International Energy Commission (2021) reports that most oil producers are the top subsidizers of fossil fuel (Figure 1). Given this background, the issue of eliminating fuel subsidies versus imposing carbon taxes raises efficiency issues and practical, policy sequencing issues. On one hand, subsidizing production of renewables and/or imposing a

carbon tax or are Pareto superior strategies because they either reduce a negative externality or increase the production of a positive externality. $^{3}$ On the other hand, subsidizing the production or consumption of a product with negative externality, such as fossil fuels, creates an economic distortion which, if combined with a carbon tax, produces further economic distortion and therefore even greater inefficiency, as is well known from the theory of second best. For example, this would imply removing fossil fuel subsidies first, before imposing a carbon tax. Policy sequencing in the context of decarbonization, however, has emphasized political economy factors over efficiency considerations. This form of sequencing has been followed, in the European Union, California, and currently China (Meckling, Sterner, and Wagner, 2017). In this form of sequencing, interest groups are formed through subsidizing innovation in renewables, before embarking on less popular carbon pricing (ibid). In such cases carbon pricing is often the last policy in the sequence, (Linsenmeier, Mohommad and Schwerhof 2022). However, in this paper we show that removal of fossil fuel subsidies can also be growth enhancing. $^{4}$ The question then is whether this provides the political justification for considering a sequencing in which the removal of subsidy of a negative externality would have higher priority than subsidizing a positive externality. Despite the importance of this question, however, we ignore the sequencing of policies in this paper, as our focus is not the social or political economy efficiency of policies but rather, their impact in reducing GHG emissions.

Figure 1: Fossil Fuel Subsidies by Country (latest year available)  
![](images/87a6f5b22067fd6915578a8ddd1eb0aade7c99669a231d057c5f2aed11688d8d.jpg)  
Source: https://www.iea.org/topics/energy-subsidies

## 2. Fossil Fuel Subsidies, Resource Rent and Carbon Emissions among Oil Exporters

The magnitudes of global subsidies of fossil fuels are staggering. Black et al. (2023) in an IMF working paper estimate that the total global subsidies of fossil fuels amounted to \$7 trillion in 2022, equivalent to the size of the economies of Germany and France, combined. The scale of this issue is not always appreciated. Simply put, governments around the world—especially in MENA—are paying producers and consumers of fossil fuel as much money as the annual GDP of France and Germany in order to produce and consume fossil fuels, with attendant impact on global GHG emissions. So, it would not be an exaggeration to state that fossil fuel subsidies are one of the most inefficient and climate damaging policies on a global scale. This figure includes total subsidies that encompass explicit subsidies, i.e., undercharging relative to true supply costs as well as implicit subsidies, i.e. undercharging relative to negative externalities of climate change and local pollution (Figure 2). To put this in perspective, the World Food Programme estimates that it would take only \$330 billion by 2030 to end world hunger according to the International Institute for Sustainable Development.

Figure 2. Global Fossil Fuel Subsidies: historical and projected  
![](images/fea25cdc94dc329d471e494177b74d7e91beb6f1af7625490b581fa5f13da642.jpg)

However, the above report and other studies of fossil fuel subsidies, such as one by Kojum and Koplow (2017), focus on oil consuming/importing countries or fossil fuel consuming sectors of the economy. The oil and gas producing countries, on the other hand, face a very different structure that has been far less investigated. For one, they sell at world market prices far above their cost of production. For example, in 2016 the average cost of production in Saudi Arabia and the Islamic Republic of Iran was about \$8.5 per barrel, $^{5}$ while the price of oil averaged to about \$43. Adding the cost of refining of \$3-\$5 per barrel (Favenec, 2022) and estimating domestic transport cost from refining to retail by pipelines for domestic use (approximately 37 cents per barrel), $^{6}$ the total cost would be about \$14 in 2016, as the unsubsidized retail cost of petroleum. This is far less than the international price. How does the classical case of oil subsidy work in this case? For one thing, an explicit subsidy is when the price is below the cost of production, while a typical MENA oil producer enjoys an international price far above the cost of production as we have seen above. Naturally, while governments can use the production cost of approximately \$14 per barrel in the above example as a point of reference to subsidize the price, oil producing companies may consider any price below the international price as foregone profits and thus lobby for subsidy levels relative to the international market, rather than the domestic marginal cost of production. In such a case, the level of subsidy will vary depending on the prevailing world oil price.

To better understand the relation between these variables for a typical oil exporter, Figure 3, developed by the authors, provides further insights. To streamline the modeling, we abstract from the monopoly power of individual oil producers and assume that all sell at a set international price of P\*. This is partly because, except for Saudi Arabia, no other single OPEC member has full price setting capability. Further, even in the case of Saudi Arabia, we can imagine that the geopolitical process by which P\* is arrived at precedes the value of P\* and focus instead on the implication of this for subsidies. For a typical oil producer, especially those in MENA, P\* exceeds the marginal cost of production at that point, as captured in the figure. The market is segmented into the domestic and the world market. But the price faced by domestic users differs from the world price, due to two factors; that the cost of production is far less than the world price, and that the governments further subsidize the production and transportation of oil for domestic consumption, but not world exports.

Several key takeaways from this analysis. First that producer gain may be quite substantial if government subsidizes production relative to the world price than relative to the domestic cost of production as a point of reference. This is depicted by the difference between the vertically shaded area versus the vertically and horizontally shaded areas combined (including the checkered area). Naturally, in the latter case, the magnitude of subsidy by the government to the producers, and thus producers' rents, will vary depending on the world price of oil. In Figure 3, the producer added rents from the subsidy are not only limited to the domestic market but extended the to export market. The question is why. One reason is that apart from the rather small subsidy associated with the cost of transporting oil and gas to the domestic users (in the case of Saudi Arabia we estimated this as only 37 cents per barrel as shown in Appendix 1), the most significant subsidy may occur in the production process itself, in which case one cannot distinguish between subsidy for domestic use versus for the world market. An alternative scenario in which the government subsidizes the oil producer only for domestic sales via monetary compensation at the point of sale, does limit the producer gain rectangle somewhat as depicted in Figure 3a. Second, consumer gains from the subsidy, while they may be substantial, are likely to be significantly smaller than the producer gain in rents as the scale of world demand for any single oil producer will be far larger than the size of domestic demand. This cannot be captured in the figure, due to space limitation. Figure 3 assumes domestic consumer subsidies are relative to the cost of production, while in practice, free market forces imply that the domestic market would be governed by the world price. In such a case, the subsidy would be relative to the world demand as depicted in Figure 3a. Third, implicit subsidies, i.e., the difference between the private supply price and external costs to the climate and local pollution, are quite significant. While in Figures 3 and 3a, per unit size of the implicit and explicit subsidies are close, we saw in Figure 2 that total magnitude of implicit subsidies dwarfs explicit subsidies. This is, again, because the scale of world demand for any single oil producer will be far larger than the size of domestic demand that can be captured in the figure due to space limitation. Fourth, for a similar reason as above, every single oil producer contributes far more to greenhouse gas emissions from its exports to the world market than from domestic overuse. The somewhat larger gap in Figures 3 and 3a between the socially efficient consumption and private consumption levels in the export sector ( $Q_{w,p} - Q_{w,soc}$ ) versus the domestic consumption ( $Q_{D,sub} - Q_{D,soc}$ ), is again not fully captured due to space limitations.

Figure 3. Fossil Fuel Subsidies, Resource Rents and Carbon emission among Oil Exporters: Case 1  
![](images/3ff0ce95305116592dd7535a61c1e9596ae1b10c2bf0fd3be306aefc43ad2e25.jpg)  
Note: The figure assumes producers are subsidized at the production level and thus for full output aimed at domestic and world markets. It also assumes domestic consumer subsidy occurs relative to domestic production cost rather than world price. For alternative assumption on both,

see Figure 3a. Produced by the authors based on stylized facts regarding the structure of the oil markets among oil producers.

Figure 3a. Fossil Fuel Subsidies, Resource Rents and Carbon emission among Oil Exporters: Case 2  
![](images/23077aaf71fc2de00fbc300a67618655adb4c053b73b9065e1f3886fb094fe65.jpg)

Note: The figure assumes producers are subsidized only for production in the domestic market. It also assumes domestic consumer subsidy occurs relative to the world price. For alternative assumption on both, see Figure 3. Produced by the authors based on stylized facts regarding the structure of the oil markets among oil producers.

We will examine whether a higher world price might require higher domestic subsidies if the domestic demand is to stay constant (Figure 3a). This proposition is empirically examined in Section 5 and is found to hold for MENA oil exporters.

## 3. Method and Data

Our data is from International Energy Agency (IEA, 2021) and covers the years 2011-2018 for 41 countries for which complete data for our purposes exists. The data covers subsidies for four distinct products, oil, gas, electricity, and coal. It also provides separate coverage of “Transport subsidy.” Although the data nominally covers most countries, there are numerous missing observations with the result that 328 observations corresponding to 41 countries are covered (Appendix 2, Table A2.1). 

[中间内容因长度限制已省略]

es as it would otherwise drop out due to time fixed effects. For this reason, price x MENA and price x MENA oil exporters is being presented in the full sample as interaction effect.

Table 4. Short-run and long-run effects of oil subsidies on economic growth: all countries, MENA, and MENA oil group

<table><tr><td rowspan="2">Dependent Variable:</td><td colspan="3">Rate of Growth</td></tr><tr><td>Full Sample</td><td>MENA subsample</td><td>MENA oil Group subsample</td></tr><tr><td>Long run results:</td><td></td><td></td><td></td></tr><tr><td>log GDP</td><td>-0.168***(-11.00)</td><td>-0.301***(-9.34)</td><td>-0.316***(-6.87)</td></tr><tr><td>log population</td><td>0.132***(2.59)</td><td>0.0493(0.45)</td><td>0.0849(0.61)</td></tr><tr><td>log subsidy</td><td>-0.000469(-0.26)</td><td>-0.00311(-0.23)</td><td>-0.000923(-0.05)</td></tr><tr><td>Short run results:</td><td></td><td></td><td></td></tr><tr><td>Error correction coeff.</td><td>-1.014***(-85.40)</td><td>-1.022***(-55.14)</td><td>-1.020***(-42.38)</td></tr><tr><td>d (log GDP)</td><td>1.180***(65.36)</td><td>1.213***(41.52)</td><td>1.220***(33.05)</td></tr><tr><td>d (log population)</td><td>0.942***(4.96)</td><td>0.359(1.12)</td><td>0.332(0.56)</td></tr><tr><td>d (log subsidy)</td><td>0.000281(0.17)</td><td>0.0118(0.65)</td><td>0.0165(0.58)</td></tr><tr><td>lagged d(log subsidy)</td><td>0.000209(0.13)</td><td>-0.00573(-0.35)</td><td>-0.0179(-0.71)</td></tr><tr><td>constant</td><td>2.261**(2.41)</td><td>7.413***(3.85)</td><td>7.232***(2.84)</td></tr></table>

t statistics in parentheses. $^{*}p<0.1$ , $^{**}p<0.05$ , $^{***}p<0.01$ . Based on panel autoregressive distributive lag model with error correction (ARDL-EC). Subsidies do not have an adverse effect on long-run and short-run growth. The long-run results are consistent with the single country projections from CPAT which until 2036. Error correction coefficient is negative and significant indicating co-integration among variables as expected. ARDL-EC accounts for this cointegration without the need to test for it. In all regressions robust errors are reported. Using clustered error option did not significantly impact the general direction of the results, although in some instances the significance dropped slightly as would be expected under clustered error.

## Appendix 1. Approximating Oil Transport Cost from refinery to final use in Saudi Arabia

Nearly all refined oil in Saudi Arabia is transported via pipelines. The following figures are used, along with their sources:

\- Total pipeline for refined products for domestic use (as opposed to heavy crude oil for exports) = 1,183 km in 2015, which is the approximate date for our estimation in the main text (https://en.wikipedia.org/wiki/List\_of\_countries\_by\_total\_length\_of\_pipelines).

\- Approximate cost of pipeline: US estimate is \$4.75 million per mile for 2015-2016, about same time as our estimate. Global cost is \$2.34 million per mile https://www.gem.wiki/Oil\_and\_Gas\_Pipeline\_Construction\_Costs. Averaging the two the total cost of pipeline for domestic consumption is approximately \$2.8 billion. Since this is a fixed cost, and we assume rental cost of capital at 5%, the annual rental cost of pipeline capital will be \$138 million.

\- Saudi Arabia produced 10.2 million barrels per in 2015 on average amounting to 3.7 billion barrels. The domestic cost of transport per barrel of oil produced for all purposes (local and exports) is therefore,

138 million / 3.7 billion = 37 cents per barrel

Table A.2.1. List of Countries in the Sample

<table><tr><td>Angola</td><td>Kuwait</td></tr><tr><td>United Arab Emirates</td><td>Libya</td></tr><tr><td>Argentina</td><td>Sri Lanka</td></tr><tr><td>Azerbaijan</td><td>Mexico</td></tr><tr><td>Bangladesh</td><td>Malaysia</td></tr><tr><td>Bahrain</td><td>Nigeria</td></tr><tr><td>Bolivia</td><td>Oman</td></tr><tr><td>China</td><td>Pakistan</td></tr><tr><td>Colombia</td><td>Qatar</td></tr><tr><td>Algeria</td><td>Russian Federation</td></tr><tr><td>Ecuador</td><td>Saudi Arabia</td></tr><tr><td>Egypt, Arab Rep.</td><td>El Salvador</td></tr><tr><td>Gabon</td><td>Thailand</td></tr><tr><td>Ghana</td><td>Turkmenistan</td></tr><tr><td>Indonesia</td><td>Trinidad and Tobago</td></tr><tr><td>India</td><td>Taiwan, Republic of China</td></tr><tr><td>Iran, Islamic Rep.</td><td>Ukraine</td></tr><tr><td>Iraq</td><td>Uzbekistan</td></tr><tr><td>Kazakhstan</td><td>Venezuela, RB</td></tr><tr><td>Korea, Rep.</td><td>Viet Nam</td></tr><tr><td></td><td>South Africa</td></tr></table>

Appendix 2. Data Characteristics  
Figure A.2.1: Distribution of CO2 in the sample  
![](images/220420e5519072311dbd3f5c9ea2c62b3398525e2d2dd8010beebdf5d0268439.jpg)

Table A.2.2: Descriptive Statistics

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Variable</td><td>Observations</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CO2 emission: all countries</td><td>369</td><td>503.9498</td><td>1525.388</td><td>4.783</td><td>10353.88</td></tr><tr><td>CO2 emission: MENA</td><td>369</td><td>55.86151</td><td>138.721</td><td>0</td><td>700.938</td></tr><tr><td>CO2 emission: MENA oil exporters</td><td>369</td><td>45.8137</td><td>136.6791</td><td>0</td><td>700.938</td></tr><tr><td>subsidy share of GDP: all countries</td><td>369</td><td>8.74E-09</td><td>1.43E-08</td><td>0</td><td>9.97E-08</td></tr><tr><td>subsidy share of GDP: MENA</td><td>369</td><td>5.06E-09</td><td>1.34E-08</td><td>0</td><td>9.97E-08</td></tr><tr><td>subsidy share of GDP: MENA oil exporters</td><td>369</td><td>4.11E-09</td><td>1.32E-08</td><td>0</td><td>9.97E-08</td></tr></table>
"""
