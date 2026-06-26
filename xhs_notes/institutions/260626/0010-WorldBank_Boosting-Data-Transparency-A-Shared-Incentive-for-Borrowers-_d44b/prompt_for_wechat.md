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
# Boosting Data Transparency A Shared Incentive for Borrowers and Investors

Megumi Kubota

POLICY RESEARCH WORKING PAPER 11054

## Abstract

This paper shows that enhancing data transparency can help increase sovereign bond returns in countries with medium to higher levels of institutional quality. Bond returns are lower in countries with high levels of debt. However, the findings from the fixed effect instrumental variables for panel data analysis highlight that enhancing data transparency can mitigate the negative impact of debt even in a highly indebted country. The novelty of the study is that it examines the relationship between sovereign bond returns and data transparency, and then calculates the benefits accrued by external creditors from improved data transparency in the borrowing country. The determinants differ from the those of sovereign bond spreads. The paper also introduces S&P sovereign credit ratings and total reserves as additional explanatory variables. There are thresholds beyond which data transparency has a positive impact on bond returns. The estimated threshold effect levels show that a country needs to have an International Country Risk Guide score greater than 4.15 in logs for international creditors to reap the benefits from enhancing data transparency.

# Boosting Data Transparency: A Shared Incentive for Borrowers and Investors\*

Megumi Kubota

The World Bank

Keywords: Economic data transparency, threshold effects, investors' benefit, institution, sovereign bond returns, credit ratings

JEL Code: F33, F34, G14

## 1. Introduction

This paper examines whether enhancing data and economic transparency benefit investors' interests—as proxied by increasing sovereign bond returns. So far, most of the literature focuses on the benefits of sovereign borrowers from investing in data transparency—and, more specifically, its impact on external borrowing costs (as proxied by sovereign spreads). To the best of my knowledge, there has been no empirical evidence of the benefits of greater transparency of the borrowing country for global investors. Hence, this paper is one of the first studies to investigate the relationship between data transparency and sovereign bond returns and estimate the gains from transparency of private creditors—more specifically, international bondholders.

It is important to assess not only the borrowers' benefits (as many research papers have examined before), but also creditors' benefits; therefore, investors will be active in participants in domestic economic activities. In this paper, I ask whether global investors' (i.e. the creditor's side) can also reap the benefits from greater transparency. Greater returns would make sovereign bonds more attractive. A strand of the empirical literature provides evidence on the determinants of short- and long-term sovereign bond yields (Poghosyan 2014; Afonso et al. 2015; Salem et al. 2016). Some argue that the fiscal position in emerging economies is a significant determinant of sovereign bond yields when global risk aversion is high (Jaramillo and Weber 2013). There is also evidence that government debt, inflation, interest rates, oil prices and the Chicago Board Options Exchange's volatility index (VIX) can influence the US 10-year bond yield (Naidu et al. 2016). The novelty of my study is, therefore, to examine the relationship between sovereign bond returns and data transparency from the external creditors' point of view, including the sovereign credit ratings of the borrowing countries as a likely determinant of sovereign bond returns, and calculating the creditors' benefits from improving data transparency. Consequently, this paper studies the benefits to international investors from improvements in data and economic transparency in the borrowing country.

In contrast, Kubota and Zeufack (2020) focus on the impact of data and economic transparency from the debtors' standpoint. Therefore, both papers show that benefits resulting from investing in transparency of the issuance country can be reaped by both debtors and creditors. The results from both papers suggest that institutional quality amplifies the impact of transparency on sovereign bond spreads and returns. This paper finds that: 1) improving data transparency in countries with higher PPG debts tends to attract more global investors, and hence increase sovereign bond returns, and 2) unlike the estimates with sovereign bond spreads in Kubota et al. (2020), the improvement of data transparency conditional on higher PPG debts may increase bond returns. My results also show that sovereign credit ratings (as proxied by S&P sovereign credit ratings) are a useful signal for investors' decision making. My estimated coefficients would calculate and measure how much international creditors could additionally benefit from improving data transparency in the borrowing country (see Table 7).

My main message is that improved data transparency increases sovereign bond returns with medium to higher levels of institutional quality, and bond returns are lower in a country with high levels of debts. However, enhancing data transparency can mitigate the negative impact of debts even if a country is highly indebted. The novelty of my study is, therefore, examining the relationship between sovereign bond returns and data transparency, and then calculating the creditors' benefits from improving data transparency. The impact is non-linear: there are thresholds that signal the level of data transparency under which positive impacts on sovereign bond returns start to kick in.

The paper uses the Fixed Effect Instrumental Variables (FE-IV) for panel data to estimate the impact on sovereign bond returns caused from data transparency through the levels of institutional quality and the government public debts or PPG external debts. Internal instrumental variables (lagged values of explanatory variables and/or lagged dependent variable) and external variables (Freedom of Information) are used to control for endogeneity in the regressions. The explanatory variables are macro and financial variables that can be classified as push and pull factors driving sovereign bond returns. I avoid clustering errors in regressions where my variable of interest (data transparency) is proxied by a binary or a categorical indicator. For instance, the IMF indicator of transparency used in this analysis is a binary variable, and I treat S&P sovereign credit ratings as a categorical indicator.

The remainder of the paper is organized as follows. Section 2 describes the estimation technique and data, and Section 3 investigates the relationship between sovereign bond returns and data transparency variables while controlling for a set of macroeconomic and financial variables. Section 4 calculates creditors' benefits from improving data transparency. Section 5 concludes.

## 2. Estimation Technique and Data

## 2.1 Econometric Methodology

This paper regresses sovereign bond returns on pull and push factors—including indicators of data transparency—using instrumental variables (IV) estimations. External (push) factors and internal (pull) factors can impact sovereign bond returns through investors' behavior. The Fixed Effect Instrumental Variables (FE-IV) estimations for panel data overcome two main challenges: one, they control for the presence of unobserved period- and country-specific effects, and another, data transparency is highly likely to be jointly endogenous with shocks to sovereign bond returns. For instance, it is likely that future shocks to borrowing costs can have an impact on transparency. Arellano and Bond (1991) and Arellano and Bover (1995) propose a methodology that accounts for endogeneity or reverse causality by using lags of the explanatory variables in the regression analysis.

To address those challenges, I include country and time effects in the regression, and then I control for biases due to the presence of simultaneous or reverse causality in the regression analysis. The IV approach in this paper accounts for the likely endogeneity of data transparency by using the external instrumental variable of ‘Freedom of Information’ (FOI) and internal instrumental variables (lagged values of the explanatory variables). Data transparency instrumented with the lagged sovereign returns and other lagged explanatory variables can predict bond returns and cannot predict future shocks to bond returns because the instrumental variables are correlated with data transparency and uncorrelated with shocks to sovereign bond returns.

I avoid clustering some regressions which include the IMF data transparency indicators because these regression specifications involve a binary or a categorical indicator. The IMF indicator of transparency used in this paper is a binary variable.

My baseline regression equation of returns of sovereign bond flows presents the following specification:

$$
\Phi_ {i t} = \alpha_ {i} + \beta_ {t} + \gamma^ {\prime} X _ {i t} + \mu_ {i t}
$$

where the dependent variable $\Phi_{it}$ represents the sovereign bonds return for country i in period t. $\alpha_{i}$ is a country effect and $\beta_{t}$ is a time effect. In my regression analysis, time effects are captured by the US 10-year Treasury bond yield and the VIX index, while country dummies are used to proxy country effects. The matrix $X_{it}$ contains information on the pull and/or push factors including data transparency variables while $\gamma$ is its coefficient vector. $\mu_{it}$ captures the residuals.

## 2.2 Data Description

I gathered annual data of sovereign bond returns for an effective sample of 76 countries from 1995 to $2020^{1}$ from the JPMorgan Markets database (please see Table 1). My dependent variable is the sovereign return index, which is measured by the emerging market bond index (EMBI), a benchmark that captures the performance of international government bonds. The JP Morgan Emerging Market Bond Index is an unmanaged index that tracks total returns for dollar-denominated Brady Bonds, Eurobonds, traded loans and local market debt instruments issued by sovereign and quasi-sovereign entities of emerging market countries.

The explanatory variables consist of pull (internal) and push (external) factors. Pull factors include the GDP per capita (in US dollars at 2010 prices), CPI inflation (average percentage change in consumer prices), general government primary balance (as percentage of GDP), current account balance (as a percentage of GDP), general government gross debt (as percentage of GDP), public external debt stocks (as percentage of GDP), and the total reserves minus gold to GDP ratio from the World Bank's World Development Indicators (WDI).

My paper introduces S&P sovereign credit ratings and total international reserves as additional explanatory variables. The S&P sovereign ratings are the sovereign credit rating on long-term foreign currency debt for emerging markets. The ratings scale runs from AAA to D (default). I record these categories from 1 as default (D) to 21 (AAA). Note that higher values indicate better ratings. Consequently, this variable is considered as a categorical indicator. The quality of institutions is proxied by the International Country Risk Guide (ICRG) index from the PRS group, which captures the level of the quality of domestic institutions. Push factors include the VIX index (which measures the implied volatility computed from S&P 500 index options) as an indicator of global risk aversion, and the US 10-year Treasury bond yield from the Federal Reserve Bank of St. Louis's FRED database. My instrumental variables are the lag of sovereign bond returns and lagged values of the ICRG index, public or external debts, the interaction terms of ICRG with data transparency indicator and (public or external) debt with data transparency indicator as instrumental variables.

## Transparency data

Data transparency indicators are proxied by public data transparency indices from the World Bank and IMF. The World Bank's statistical capacity indicator (SCI) captures the availability, collection and practices in the production of official statistics by the country, and the IMF's subscription and compliance to the Special Data Dissemination Standard (SDDS) are binary variables. I refer to the indicator of the World Bank as the WB data transparency and the indicator of the IMF as the IMF data transparency.

The World Bank's Statistical Capacity Indicator (SCI) measures a country's ability to collect, analyze, and disseminate high quality public data of an economy. This indicator is a composite score that evaluates the capacity of a country's statistical system. It is based on a diagnostic framework assessing the following areas: (i) methodology, (ii) data sources, and (iii) periodicity and timeliness. Countries are scored against 25 criteria in these areas, using publicly available information and/or country input. Therefore, the overall Statistical Capacity score is calculated as the simple average of all three dimensions (i.e. practice, collection, availability) with a scale of 0-100. Higher scores mean that a country has a stronger statistical capacity. The methodology indicator (or practice score) measures the country's ability to adhere to internationally recommended standards and methods. This score is calculated from the weighted average of 10 underlying indicator scores. The data source indicator (or collection score) quantifies whether a country conducts data collection activity in line with internationally recommended periodicity, and whether data from administrative systems are available. Its score is computed from the weighted average of 5 underlying indicator scores. The periodicity and timeliness indicator (or availability score) assesses the availability and periodicity of key socioeconomic indicators if data is available to the public users in time. The score is based on the weighted average of 10 underlying indicator scores.

The IMF's Special Data Dissemination Standard (SDDS) measures if a country releases more frequent, timely and accurate macroeconomic statistics. This indicator captures the timing of subscribing to SDDS and/or the data when the subscribing country meets the SDDS specification (and first posted its e-GDDS national data summary data page) which varies across countries and is primarily determined by internal IMF procedures that are not associated to events in these countries. Once a country adopts this standard of data transparency, the country has less incentive to reverse this system and, consequently, this becomes a long-term commitment. In my empirical analysis, I use two binary data transparency indicators from the IMF: (a) a dummy variable that takes the value of 1 for the years after the country subscribes with the SDDS, and (b) a dummy variable that takes the value of 1 when country comes into compliance with SDDS specifications (and/or posts its first national data summary page).

## 3. Empirical Analysis

This section analyzes the empirical results from the Fixed Effect Instrumental Variable (FE-IV) estimations for panel data. My IV estimations show that data transparency instrumented with IV variables can predict bond spread returns and that my IV variables cannot predict future shocks to bond returns. My regressions produce robust results when the interaction term between data transparency and ICRG is included in the specification: a negative and significant coefficient estimate for data transparency and a positive and significant for the interaction term. My empirical results prove my main findings: 1) improving data transparency increases sovereign bond returns in countries with medium to higher levels of institutional quality; 2) bond returns are lower when a country holds high levels of debts; 3) despite the fact that the sovereign is highly leveraged, enhancing data transparency can mitigate the negative effects on bond returns caused from debts; and 4) there are thresholds beyond which the positive impact of transparency on bond returns kicks in.

Table 2 presents the baseline regression analysis of sovereign bond returns on domestic and global factors using FE-IV estimation. The regressions results prove that enhancing data transparency leads to higher bond returns if a country has medium to higher levels of institutional quality. The regressions in columns [2] to [6], for instance, show positive and significant coefficients of the interaction term between the World Bank data transparency and ICRG. Consequently, greater data transparency coupled with better institutional quality would increase bond returns—thus, benefitting investors. The estimated threshold levels of institutional quality (as measured by the ICRG index in logs) from the estimated coefficients for [2] \~ [6] are, for instance, 4.15, 4.14, 4.22, 4.12 and 4.09, respectively. Consequently, the average threshold level is quite stable around 4.15 which lies between 4.09 and 4.22. For example, international private creditors will enjoy the benefits from enhancing transparency in the issuing country when its level of institutional quality is at least 4.15 (that is, medium to high quality of institutions). Figure 1a plots the conditional sensitivity of sovereign bond returns to overall data transparency conditional on the level of institutional quality (using the coefficient estimates in Table 2, column [2]). The exponential of threshold of data transparency against the level of institutional quality is 64 basis points. Therefore, if a country needs a level of institutional quality of at least 63.66 to kick-in the data transparency to start working, this means improving data transparency to obtain higher bond returns.

Column [3] in Table 2 shows that bond returns are lower when levels of public debt are high, but the estimated coefficient of the latter variable is not statistically significant. Despite being a highly leveraged country, enhancing data transparency can mitigate the negative effects on bond returns caused by elevated government debt. The regression in column [4] of Table 2 shows that better data transparency can still make a highly indebted country attractive, and hence increase bond returns in such a highly leveraged sovereign.

Table 3 shows the estimation results for the components of the WB transparency index; namely, the methodology assessment, periodicity and timeliness assessment, and data source assessment, as well as the IMF indicators of transparency—i.e. subscription and standard compliance—in my baseline regression specification. Significant and positive coefficient estimates of the interaction terms between

[中间内容因长度限制已省略]

td>Constant</td><td>-1.115(1.656)</td><td>211.5***(30.43)</td><td>210.6***(31.00)</td><td>203.8***(31.98)</td><td>225.7***(31.70)</td><td>173.1***(27.76)</td></tr><tr><td>Observations</td><td>465</td><td>444</td><td>442</td><td>442</td><td>400</td><td>400</td></tr><tr><td>Number of countries</td><td>40</td><td>40</td><td>40</td><td>40</td><td>36</td><td>35</td></tr></table>

Standard errors in parentheses  
\*\*\* p<0.01, \*\* p<0.05, \* p<0.1

Figure 1a: Response of Government Bond Yields to World Bank Overall Transparency Conditional on Institutional Quality  
![](images/ff84fde3059013284ecab87a6affe4727f86cc0f7de4c8d3e46d0b9a3e69e0b6.jpg)

Figure 1b: Response of Government Bond Yields to World Bank Methodology Transparency Conditional on Institutional Quality  
![](images/e401dd47c105e8576d1c7bfec057646c5e9d4951fcf4fb1aab8f6a8239da0ace.jpg)

Figure 1c: Response of Government Bond Yields to World Bank Periodicity and Timeliness Transparency Conditional on Institutional Quality  
![](images/557069a62e6502b1a5d0fbd3a71528c75064e1fe7776887b8d67827ff73ab11a.jpg)

Figure 1d: Response of Government Bond Yields to World Bank Data Source Transparency Conditional on Institutional Quality  
![](images/53191aecbcd538c1751d139c6a27e309a3caa221af53b304801d9f71fe60fd17.jpg)

Table 7: Additional Benefits from Improving Data Transparency

<table><tr><td></td><td colspan="4">Additional Gains for Global Investors from PPG Bonds Issued in a Domestic Country: if data transparency improved to: Top decile of upper middle income</td></tr><tr><td>Country</td><td>basis points</td><td>(US$ billion)</td><td>(% GDP)</td><td>(% Export)</td></tr><tr><td>East Asia</td><td>566</td><td>317.80</td><td>1.82</td><td>8.52</td></tr><tr><td>China</td><td>870</td><td>250.64</td><td>1.71</td><td>9.18</td></tr><tr><td>Indonesia</td><td>111</td><td>20.21</td><td>1.91</td><td>11.01</td></tr><tr><td>Mongolia</td><td>114</td><td>0.39</td><td>2.93</td><td>5.08</td></tr><tr><td>Philippines</td><td>344</td><td>8.96</td><td>2.48</td><td>9.83</td></tr><tr><td>Viet Nam</td><td>277</td><td>0.21</td><td>0.06</td><td>0.07</td></tr><tr><td>South Asia</td><td>193</td><td>17.53</td><td>0.50</td><td>3.00</td></tr><tr><td>India</td><td>96</td><td>6.82</td><td>0.26</td><td>1.36</td></tr><tr><td>Pakistan</td><td>337</td><td>1.79</td><td>0.59</td><td>6.39</td></tr><tr><td>Sri Lanka</td><td>150</td><td>2.10</td><td>2.49</td><td>16.15</td></tr><tr><td>Latin America &amp; Caribbean</td><td>527</td><td>292.82</td><td>7.32</td><td>30.96</td></tr><tr><td>Argentina</td><td>44</td><td>3.76</td><td>0.98</td><td>5.88</td></tr><tr><td>Belize</td><td>445</td><td>0.25</td><td>12.05</td><td>32.52</td></tr><tr><td>Brazil</td><td>680</td><td>32.57</td><td>2.21</td><td>13.41</td></tr><tr><td>Colombia</td><td>284</td><td>13.80</td><td>5.11</td><td>37.74</td></tr><tr><td>Costa Rica</td><td>74</td><td>0.52</td><td>0.83</td><td>2.60</td></tr><tr><td>Dominican Republic</td><td>632</td><td>14.01</td><td>17.76</td><td>97.10</td></tr><tr><td>Ecuador</td><td>593</td><td>10.49</td><td>10.57</td><td>48.36</td></tr><tr><td>El Salvador</td><td>111</td><td>0.68</td><td>2.71</td><td>11.15</td></tr><tr><td>Guatemala</td><td>133</td><td>0.78</td><td>1.00</td><td>6.12</td></tr><tr><td>Jamaica</td><td>379</td><td>2.12</td><td>15.33</td><td>63.64</td></tr><tr><td>Mexico</td><td>297</td><td>74.50</td><td>6.83</td><td>17.30</td></tr><tr><td>Peru</td><td>493</td><td>10.27</td><td>5.09</td><td>22.40</td></tr><tr><td>East &amp; Central Europe</td><td>161</td><td>49.47</td><td>1.66</td><td>5.65</td></tr><tr><td>Azerbaijan</td><td>142</td><td>0.53</td><td>1.25</td><td>3.50</td></tr><tr><td>Belarus</td><td>38</td><td>0.13</td><td>0.22</td><td>0.36</td></tr><tr><td>Georgia</td><td>45</td><td>0.03</td><td>0.21</td><td>0.57</td></tr><tr><td>Kazakhstan</td><td>11</td><td>0.19</td><td>0.11</td><td>0.37</td></tr><tr><td>Russia Federation</td><td>593</td><td>46.91</td><td>3.14</td><td>12.31</td></tr><tr><td>Serbia</td><td>172</td><td>1.08</td><td>2.03</td><td>4.21</td></tr><tr><td>Türkiye</td><td>365</td><td>32.79</td><td>4.55</td><td>15.84</td></tr><tr><td>Ukraine</td><td>327</td><td>8.35</td><td>5.33</td><td>13.73</td></tr><tr><td>Middle East &amp; North Africa</td><td>395</td><td>33.43</td><td>2.65</td><td>12.07</td></tr><tr><td>Egypt, Arab Rep.</td><td>84</td><td>2.18</td><td>0.57</td><td>4.56</td></tr><tr><td>Iraq</td><td>4065</td><td>8.13</td><td>4.49</td><td>16.19</td></tr><tr><td>Jordan</td><td>142</td><td>1.31</td><td>3.00</td><td>12.63</td></tr><tr><td>Lebanon</td><td>569</td><td>17.83</td><td>56.22</td><td>343.36</td></tr><tr><td>Morocco</td><td>120</td><td>1.31</td><td>1.08</td><td>3.50</td></tr><tr><td>Tunisia</td><td>147</td><td>1.01</td><td>2.38</td><td>6.28</td></tr><tr><td>Sub Saharan Africa</td><td>825</td><td>112.62</td><td>6.61</td><td>32.13</td></tr><tr><td>Angola</td><td>1195</td><td>9.56</td><td>19.03</td><td>50.04</td></tr><tr><td>Côte d&#x27;Ivoire</td><td>809</td><td>6.90</td><td>10.96</td><td>52.17</td></tr><tr><td>Gabon</td><td>3885</td><td>9.46</td><td>61.80</td><td>130.10</td></tr><tr><td>Ghana</td><td>556</td><td>5.68</td><td>8.11</td><td>39.14</td></tr><tr><td>Nigeria</td><td>350</td><td>3.90</td><td>0.90</td><td>11.13</td></tr><tr><td>Senegal</td><td>248</td><td>1.03</td><td>4.20</td><td>20.30</td></tr><tr><td>South Africa</td><td>572</td><td>45.55</td><td>13.49</td><td>48.88</td></tr><tr><td>Zambia</td><td>340</td><td>1.02</td><td>5.64</td><td>12.05</td></tr></table>

Figure 2: Impact of a 10% Change in Data Transparency on Sovereign Bond Returns Conditional on the Level of PPG External Debt in 2020 by Region  
![](images/109884ab3b56e4ebeeefa2c6448ef2f33ccb3f25d0b85da3b034bb7e85acd2fd.jpg)
"""
