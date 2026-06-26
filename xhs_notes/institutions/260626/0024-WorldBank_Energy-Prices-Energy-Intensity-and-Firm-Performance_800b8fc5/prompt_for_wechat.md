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
# Energy Prices, Energy Intensity, and Firm Performance

Reyes Aterido

Mariana Iootty

Martin Melecky

POLICY RESEARCH WORKING PAPER 11069

## Abstract

This paper estimates the effect of electricity prices on firm performance, focusing on firm productivity, sales, and employment. Using the World Bank Business Pulse Survey data for a sample of 24 emerging markets and developing economies during 2019–23, the paper estimates the average effect and the heterogeneous effects across industries of varying energy intensity and firms that implemented (or did not implement) energy efficiency measures (self-reported in the Business Pulse Survey). The findings show that increasing electricity prices by 1 percent reduces employment at firms in energy-intensive industries that did not adopt energy efficiency measures by about 1.5 percent, compared with similar firms in energy-non-intensive sectors. In parallel, energy-intensive firms may increase sales and productivity but this result is robust to all alternative specifications. Firms may increase sales while reducing employment after energy price hikes, by adopting energy-efficient technologies and by passing through costs to consumers in inelastic markets while reducing employment in energy-intensive sectors due to cost pressures. These results highlight the adoption of energy efficiency measures by firms as an important employment protection policy action to cope with future volatility in energy (electricity) prices.

# Energy Prices, Energy Intensity, and Firm Performance

Reyes Aterido, Mariana lootty, and Martin Melecky

World Bank

Keywords: World Bank Business Pulse Survey Data, Firm-level Panel Data, Energy Prices, Energy Intensity of Industries and Firms, Firm Performance, Productivity, Sales, Employment.

JEL Classifica ion: D22, L25, Q41, Q43, O13.

## 1. Introduction

The link between rising energy costs and firm performance has garnered increasing attention in academic and policy discussions due to the broader adoption of carbon pricing mechanisms and the gradual elimination of energy subsidies. As these policy changes elevate nonrenewable energy prices—a crucial input in the production processes of many industries—firms may experience notable performance implications. Higher energy costs generally affect profitability and operational efficiency by increasing production expenses, particularly in energy-intensive sectors. Firms with greater energy dependence often face heightened stock market volatility due to increased uncertainty and lower expected cash flows (Sadorsky 1999; Henriques & Sadorsky 2008). Moreover, rising energy costs may constrain corporate investment strategies, leading to reduced capital expenditures, especially in industries reliant on energy inputs (Kilian 2008; Bloom 2009).

The increased accessibility of firm-level data has opened new avenues for empirical studies of the complex link between energy price fluctuations and firm performance. Cali et al. (2022) show that, in Indonesia and Mexico, increases in electricity prices harm manufacturing plants' performance. However, fuel price hikes result in higher productivity and profits of manufacturing plants. Fuel prices incentivize plants to replace inefficient fuel-powered with more productive electricity-powered capital equipment. Their results help to re-evaluate the policy trade-off between reducing carbon emissions and improving economic performance, particularly in countries with large fuel subsidies, such as Indonesia and Mexico. Cali et al. (2023) studied firms from 12 sectors and 11 middle-income countries during 2002–2013, using World Bank Enterprise Survey data. The study did not consistently find that higher energy prices negatively affect economic performance; they may even enhance it in some cases. Firms might be able to offset increased energy costs through innovation or new market strategies. The impact of energy prices on firms is a multifaceted issue, depending on several characteristics, including energy intensity, firm size, ownership type, and previous experience with electricity outages—which made companies less sensitive to price increases, likely due to their familiarity with managing energy and input shortages.

The dynamic effects of energy price shocks on firm performance have also been explored. Andre et al. (2023) analyze firm-level data from 21 OECD countries (1995–2020) and show that energy price shocks impact firm productivity through immediate cost increases and longer-term adjustments. The study highlights sectoral and firm-level heterogeneity, finding that energy price hikes initially reduce productivity, particularly in energy-intensive sectors and firms under financial constraints. However, medium-term productivity improvements often follow as firms adapt, typically through increased investment. These findings align with the "pollution haven" hypothesis, which suggests that higher energy costs erode competitiveness and may drive firms to relocate (Copeland & Taylor 2004), and the Porter hypothesis, which posits that higher carbon prices can enhance productivity by incentivizing efficiency and innovation (Porter & van der Linde 1995). This dual perspective underscores the nuanced impact of energy price shocks on firm outcomes, blending short-term losses with potential long-term gains.

The recent energy price surge, triggered by the strong economic recovery following COVID-19 and the Russian invasion of Ukraine, has sparked renewed interest in the subject. Battistini et al. (2022) focus on EU economies during 2020-2022 and highlight a few interesting aspects. Energy price shocks disproportionately affect firms based on their energy dependence and hedging strategies. Energy-intensive sectors are particularly hard-hit, facing greater financial stress and profitability challenges due to heightened costs and supply chain disruptions. Spiking energy prices have triggered a significant worsening of the energy terms of trade in the euro area. This has impacted companies by reducing their purchasing power and increasing operational costs, affecting their profitability and investment decisions. Ari et al. (2022) employed the IMF-World Bank CPAT model and found clear evidence of a regressive impact on European households' finances. However, the effects on European businesses are less clear-cut, with mixed results regarding the loss of competitiveness. The increase in energy costs for energy-dependent and trade-sensitive industries within the European Union may not be disproportionately higher than for non-EU countries due to variations in natural gas reliance or the use of other energy products across different nations.

When evaluating the effects of fluctuating energy prices, the role of fossil fuel subsidies must be carefully considered. Accurately pricing fossil fuels is essential for the efficient allocation of an economy's scarce resources and investment across sectors and activities. An efficient price incorporates both the supply costs and the environmental externalities of fuel consumption (Coady et al. 2019). However, substantial subsidies or underpricing distort market signals, leading to the overconsumption of fossil fuels, exacerbating global warming, and intensifying local environmental degradation. For instance, Black et al. (2023) report that global fossil fuel subsidies reached an unprecedented \$7 trillion in 2023, as governments sought to shield consumers and businesses from energy price spikes triggered by the Russian Federation's invasion of Ukraine and the post-pandemic economic recovery. These subsidies, while aimed at providing short-term relief, may have inadvertently delayed firms' and households' consideration of environmental costs in consumption and investment decisions. As a result, the adoption of energy-efficient technologies and sustainable practices has likely been postponed, undermining long-term climate goals (Bovenberg & de Mooij 1994; Parry et al. 2021).

Against this backdrop, this paper contributes to the existing body of research by focusing on the impact of country-specific energy price fluctuations during 2019-2023 on firms in emerging economies using the World Bank Business Pulse Survey—a dataset not used yet for this type of analysis in the literature—together with the CPRS classification of Battiston et al. (2022) to gauge the risk exposure of sectors to (the intensity of treatment by) the energy price fluctuations. Furthermore, the paper contributes to the literature by shedding light on the specific context of emerging economies, employing rapid survey data to grasp the nuances of business cycles, using the quarterly country-specific electricity price tariffs for businesses, matching the latter with the month in which a firm was surveyed, and highlighting the differentiated effects of sectoral energy intensity in conjunction with firm-level energy efficiency measures as indicators of a firm's exposure to energy price fluctuations and preparedness to manage energy price shocks.

Using a different data set with larger country coverage, our baseline findings confirm prior evidence from Cali et al. (2022, 2023) that electricity price increases, on average, lead to higher productivity and sales for firms. However, the magnitude of this positive effect is significantly reduced for firms that have not implemented energy efficiency measures, suggesting that such initiatives are critical for firms to adapt to evolving energy market trends. In addition, when the baseline results are subjected to a battery of robustness tests the results do not survive in all alternative specifications. By contrast, we find that rising electricity prices exert a negative effect on employment, particularly in energy-intensive industries where energy efficiency measures are absent. This result highlights the vulnerability of labor markets in sectors heavily reliant on energy (electricity) inputs, especially in developing economies where the adoption of efficiency-enhancing technologies often lags.

These findings align with evidence from Aldy and Pizer (2015), who show that energy-intensive firms are disproportionately affected by energy price increases due to their limited flexibility in reducing energy consumption. Similarly, Sato et al. (2019) emphasize the employment risks in sectors with high energy dependency, particularly in regions with limited policy support for energy efficiency. Our study's integration of industry-level energy intensity with firm-level adaptations provides a novel contribution by offering deeper insights into how electricity price changes propagate through different economic layers. Compared to earlier studies, such as Martin et al. (2014), which primarily focused on advanced economies or treated energy price impacts in aggregate terms, this paper uniquely highlights the heterogeneity of these effects across firms in developing countries, where structural constraints and varying levels of technological adoption exacerbate disparities in energy price impacts.

Our findings underline the importance of energy efficiency measures not only as a tool for enhancing productivity and sales, but also as a critical buffer against adverse employment effects associated with rising electricity prices. This aligns with evidence from Bloom et al. (2010), who emphasize that firm-level innovations, including energy efficiency improvements, are key to maintaining competitiveness during economic transitions. Our findings also complement those by Newell et al. (2021), which highlight the role of energy efficiency in mitigating the labor market disruptions associated with volatile energy prices, particularly in energy-intensive sectors.

By focusing on developing economies, this study expands the literature on energy price shocks—which has predominantly centered on advanced economies—and addresses critical gaps in understanding the shocks’ differentiated effects. Consistent with Popp (2019), our results suggest that fostering widespread adoption of energy efficiency practices is essential for mitigating the employment risks of transitioning to greener energy systems. Particularly for energy-intensive industries in developing countries, these measures are crucial for safeguarding jobs and ensuring firms remain competitive amid fluctuating electricity prices and shifting global energy markets.

The rest of the paper is organized as follows. Section 2 describes the employed data. Section 3 explains the estimation methodology and identification. Section 4 discusses the estimation results and their robustness checks. Section 5 concludes.

## 2. Data

Our analysis uses data from the Business Pulse Surveys (BPS) developed by the World Bank to monitor the impact of the COVID-19 pandemic on the private sector. The questionnaire collects information on several dimensions of firm performance, spanning from basic economic indicators—such as the operating status of the business, year of establishment, sales, and employment—as well as firm-specific practices such as managerial practices, technology adoption, and implementation of energy-efficient measures. Firms were surveyed from April 2020 (about end-2019 performance) to June 2023 in several waves, providing a unique perspective on the private sector's response to the pandemic and the subsequent economic disturbances caused by the fast post-COVID-19 recovery, Russia's invasion of Ukraine, and the associated energy price surges and fluctuations.

Our sample comprises an unbalanced panel of 63,716 observations drawn from 24 countries across four regions (Eastern and Central Europe, Latin America and the Caribbean, South Asia and the Pacific, and Sub-

Saharan Africa). $^{1}$ Due to data availability issues, the analysis is limited to 16 countries. This reduction stems primarily from misreporting in the sales variable but is also due to incomplete data for control variables, and electricity prices; the latter is, for example, not available for Tajikistan. Furthermore, self-reported energy efficiency measures are not available in all countries. Consequently, regressions that include energy efficiency measures are based on data from 13 countries. The sample covers micro, small, medium, and large businesses across all main sectors (agriculture, manufacturing, retail, and other services, including construction). $^{2}$

Table A1 (a-c) in the Annex describes the sample distribution across years, sectors, and firm sizes at the country level. This breakdown is instrumental for categorizing sectors by their energy usage intensity. The sectors are meticulously disaggregated to the most granular level the sampling methodology allows. Within the sample, agriculture accounts for 6 percent of the firms, manufacturing for 25 percent, wholesale and retail for 24 percent, and a diverse array of other services for 45 percent. Within the service sector, food services and accommodation represent 23 percent, transportation and information and communication technology (ICT) account for 13 percent, and construction for 12 percent. The remaining firms are engaged in financial activities, real estate, education, health, and other sectors.

Table A2 in the Annex shows the summary statistics of the main variables used in the analysis. The dependent variables used in the estimations are employment, sales, and sales per worker as a measure of labor productivity. $^{3,4}$ The median firm has sales of \$12,312, 6 workers, $^{5}$ with a labor productivity of \$1,950 per worker, and has been operating for 15 years. Figure 1 depicts the trends of our outcome variables, labor productivity, sales, and employment.

To address the effects of energy price shocks on firm performance, our paper carefully manages four critical aspects of the data. The first aspect involves classifying sectors based on their energy intensity following the Climate Policy Relevant Sectors (CPRS) framework introduced by Battiston et al. (2017). The CPRS taxonomy identifies energy-intensive sectors through a multifaceted lens, considering (i) the emissions produced by each sector's economic activities, (ii) the sector's contribution to the Greenhouse Gas (GHG) emissions chain, (iii) the sector's engagement in specific policy processes, including its lobbying capacity; and (iv) the transition risk associated with the sector, which inversely relates to the level of fuel substitutability. A sector is deemed energy-intensive if its activities result in emissions, utilizes fuel (or a mix of fuels) as a primary input, and has a low potential for substituting these fuels. The sector classification by energy usage is systematically outlined in Table A3 in the Annex.

The second element is measuring energy price shocks. We use the commercial electricity rate shown in Figure 1, compiled quarterly by Global Petrol Prices for each country. For the countries included in the sample, electricity rates, on average, fell during 2020 and 2021, reaching their nadir in the last quarter of 2021. Subsequently, there was a recovery in the rates during 2022. The price fluctuation ranged from \$0.03 to \$0.38 per kWh. In the case of oil prices, the range was between \$33.7 and \$113.

The third aspect refers to fossil fuel subsidies. We measure this aspect using the IMF data (Black et al., 2023), which provide, for 170 countries, the estimates of explicit subsidies for fossil fuels, i.e., undercharging for the supply cost of fossil fuels. All but five countries in the dataset, among them Tajikistan, have no (zero) petroleum subsidies. In the case of explicit subsidies for electricity, only three countries in the dataset do not have subsidies. Considering countries with explicit subsidies, the petroleum subsidies range from 0.00004 to 3.58 percent of GDP, while electricity subsidies range from 0.04 to 9.76 percent of GDP. The distributions of such subsidies overtime are depicted in Figures 3 (panels a and b).

The fourth data aspect concerns firms' adoption of energy efficiency practices. This is a crucial factor because it can significantly influence a firm's resilience to energy price fluctuations. To account for these practices, we draw on data from the BPS, which features a module focused on firms' energy efficiency measures. The survey queries firms on implementing technologies or methods to improve energy usage efficiency. Those who have adopted energy efficiency solutions are prompted to detail the specific technologies or practices in use. These practices encompass questions about LEED certification for buildings, adopting efficient lighting systems, adherence to ISO 14001 or 50001 standards, or engagement in carbon trading schemes. 

[中间内容因长度限制已省略]

td></td><td></td><td>-0.835***(0.192)</td><td></td><td></td></tr><tr><td>log Price elect*Energy inefficient IV2</td><td></td><td>0.307(1.109)</td><td></td><td></td><td>-0.0870(1.123)</td><td></td><td></td><td>-0.596***(0.219)</td><td></td></tr><tr><td>log Price elect*Energy inefficient IV3</td><td></td><td></td><td>1.935(1.214)</td><td></td><td></td><td>1.680(1.230)</td><td></td><td></td><td>-0.483**(0.232)</td></tr><tr><td>log Price elect*Energy intense</td><td>1.368***(0.322)</td><td>1.190**(0.516)</td><td>1.690***(0.554)</td><td>1.421***(0.327)</td><td>1.283**(0.522)</td><td>1.809***(0.559)</td><td>-0.141(0.118)</td><td>0.260**(0.121)</td><td>0.306**(0.121)</td></tr><tr><td>log Price electricity</td><td>-2.385***(0.507)</td><td>-3.092***(0.494)</td><td>-3.693***(0.515)</td><td>-2.353***(0.517)</td><td>-3.068***(0.501)</td><td>-3.726***(0.522)</td><td>0.217(0.166)</td><td>-0.0739(0.102)</td><td>-0.0294(0.0998)</td></tr><tr><td>Constant</td><td>-48.26***(2.628)</td><td>-51.50***(2.303)</td><td>-51.39***(2.346)</td><td>-43.55***(2.656)</td><td>-47.00***(2.327)</td><td>-46.93***(2.370)</td><td>10.10***(0.787)</td><td>8.543***(0.480)</td><td>8.076***(0.417)</td></tr><tr><td>Observations</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td></tr><tr><td>R-squared</td><td>0.233</td><td>0.232</td><td>0.232</td><td>0.335</td><td>0.334</td><td>0.334</td><td>0.571</td><td>0.803</td><td>0.848</td></tr><tr><td>Country FE</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr></table>

Robust standard errors in parentheses, \*\*\* p<0.01, \*\* p<0.05, \* p<0.1  
Weighted by country sample size; Controls for size $^{[1]}$ , age, wave, and subsector  
[1] Sales if dependent variable is employment

Table B2: Summary estimation results based on Equation (3) with different specifications regarding FEs, clustering, weights, and energy price

<table><tr><td rowspan="3"></td><td colspan="3">Country-Year FE</td><td colspan="3">Clustered by country-sector</td><td colspan="3">Not weighted by country size</td><td colspan="3">Not weighted excl. India</td><td colspan="3">3-month MA energy price</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>Sales per worker (log)</td><td>Sales (log)</td><td>Employment (log)</td><td>Sales per worker (log)</td><td>Sales (log)</td><td>Employment (log)</td><td>Sales per worker (log)</td><td>Sales (log)</td><td>Employment (log)</td><td>Sales per worker (log)</td><td>Sales (log)</td><td>Employment (log)</td><td>Sales per worker (log)</td><td>Sales (log)</td><td>Employment (log)</td></tr><tr><td>Price electricity, log</td><td>0.199(1.699)</td><td>-0.248(1.734)</td><td>-0.915**(0.390)</td><td>-2.711**(1.152)</td><td>-2.842**(1.175)</td><td>-0.538**(0.231)</td><td>-2.290***(0.481)</td><td>-2.336***(0.488)</td><td>-0.190(0.143)</td><td>-0.741(0.483)</td><td>-0.859*(0.490)</td><td>-0.0628(0.146)</td><td>3.796***(0.624)</td><td>3.828***(0.630)</td><td>-0.608***(0.188)</td></tr><tr><td>log Price elect*Energy intense</td><td>0.308(0.299)</td><td>0.362(0.305)</td><td>-0.109(0.119)</td><td>1.662**(0.755)</td><td>1.611**(0.735)</td><td>-0.316(0.219)</td><td>0.762***(0.271)</td><td>0.807***(0.274)</td><td>-0.109(0.0876)</td><td>0.399(0.278)</td><td>0.465*(0.280)</td><td>-0.169*(0.0876)</td><td>1.649***(0.341)</td><td>1.625***(0.345)</td><td>-0.276**(0.123)</td></tr><tr><td>log Price elect*Energy inefficient</td><td>-1.976***(0.574)</td><td>-2.188***(0.586)</td><td>-0.981***(0.211)</td><td>0.155(0.426)</td><td>0.176(0.432)</td><td>0.151(0.227)</td><td>-0.727(0.488)</td><td>-0.811(0.495)</td><td>-0.380**(0.155)</td><td>-1.927***(0.497)</td><td>-1.867***(0.504)</td><td>-0.425***(0.155)</td><td>-0.718(0.587)</td><td>-1.012*(0.597)</td><td>-0.970***(0.211)</td></tr><tr><td>log El. Price*Energy intense*Energy inefficient</td><td>0.566(0.580)</td><td>0.126(0.594)</td><td>-0.678***(0.229)</td><td>-0.644(0.470)</td><td>-0.729(0.466)</td><td>-0.516*(0.305)</td><td>0.675(0.582)</td><td>0.404(0.588)</td><td>-0.443***(0.159)</td><td>1.074*(0.583)</td><td>0.792(0.588)</td><td>-0.463***(0.159)</td><td>-0.512(0.629)</td><td>-0.741(0.640)</td><td>-0.441*(0.231)</td></tr><tr><td>Constant</td><td>-0.103(5.092)</td><td>1.907(5.187)</td><td>-1.077(1.310)</td><td>-30.01***(7.498)</td><td>-26.29***(7.595)</td><td>6.583***(1.018)</td><td>-36.97***(2.267)</td><td>-32.74***(2.294)</td><td>7.530***(0.672)</td><td>-13.86***(2.306)</td><td>-10.23***(2.337)</td><td>6.389***(0.703)</td><td>-6.419***(2.261)</td><td>-3.465(2.292)</td><td>1.993***(0.675)</td></tr><tr><td>Observations</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>19,237</td><td>13,916</td><td>13,916</td><td>13,916</td><td>19,237</td><td>19,237</td><td>19,237</td></tr><tr><td>R-squared</td><td>0.306</td><td>0.396</td><td>0.580</td><td>0.215</td><td>0.321</td><td>0.490</td><td>0.212</td><td>0.310</td><td>0.552</td><td>0.215</td><td>0.321</td><td>0.466</td><td>0.225</td><td>0.330</td><td>0.567</td></tr><tr><td>Country FE</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr></table>

Robust standard errors in parentheses
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1
Weighted by country sample size
Controls for size[1], age, wave, and subsector [1] Sales if dependent variable is employment
"""
