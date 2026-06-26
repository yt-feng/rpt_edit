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
- 已识别机构名：`国际货币基金组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际货币基金组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Central Bank Communication in Times of Uncertainty: AI- assisted Decoding of Recent Trends in Europe

Francesca Caselli, Luisa Charry, Larry Cui, Pragyan Deb, Allan Gloe Dizioli, Alexandra Fotiou, Ben Park and Sebastian Weber

WP/26/133

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUN

![](images/d354b4a281ea66eb7f2909cd0ac7fd6d7c148c0aab7ba12be7e88a996fd68d6a.jpg)

# IMF Working Paper European Department

# Central Bank Communication in Times of Uncertainty: AI-assisted Decoding of Recent Trends in Europe\*

Authorized for distribution by Helge Berger
June 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: More frequent large macroeconomic shocks since the global financial crisis have entrenched uncertainty, particularly in Europe. This has increased the premium on central bank communication in guiding expectations and strengthening macroeconomic resilience. European central banks have responded by adapting their communication toolkits and styles. This study provides a systematic assessment of recent central bank communication across advanced and emerging European economies, combining a survey of institutional communication frameworks with novel text-miningbased indicators on monetary policy guidance in these economies over 2009-2025. While communication toolkits are broadly similar, their intensity and transparency differ markedly, with central banks in advanced economies making greater use of forward-looking tools. Central banks in both groups respond primarily to inflation uncertainty. However, communication strategies diverge, as central banks in advanced economies increasingly shift toward forward-looking language, whereas those in emerging markets shift toward more backward-looking communication. These patterns highlight credibility and institutional capacity as key determinants of central bank communication under uncertainty.

RECOMMENDED CITATION: Caselli, Francesca, Luisa Charry, Larry Cui, Pragyan Deb, Allan Gloe Dizioli, Alexandra Fotiou, Ben Park, and Sebastian Weber, “Central Bank Communication in Times of Uncertainty: AI-assisted Decoding of Recent Trends in Europe,” IMF Working Paper WP/26/133.

<table><tr><td>JEL Classification Numbers:</td><td>D80, E37, E43, E52, E58.</td></tr><tr><td>Keywords:</td><td>Central bank communication; uncertainty; forward guidance; monetary policy</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>fcaselli@imf.org,lcharry@imf.org,lcui@imf.org,pdeb@imf.org,afotiou@imf.org,bpark@imf.org,adizioli@imf.org,sweber@imf.org</td></tr></table>

WORKING PAPERS

# Central Bank Communication in Times of Uncertainty: AI-assisted Decoding of Recent Trends in Europe

Prepared by Francesca Caselli, Luisa Charry, Larry Cui, Pragyan Deb, Allan Gloe Dizioli, Alexandra Fotiou, Ben Park and Sebastian Weber

## ContentsPage

I. Introduction 4
II. A survey of central bank communication practices in Europe 7
III. Indices of central bank communication 9
IV. Stylized facts on central bank communication 10
A. Stylized fact I: AE central banks make greater use of forward-looking language 10
B. Stylized fact II: Central banks commonly use forward-looking and backward-looking communication at the same time 12
C. Stylized fact III: Inertia in central banks communication 13
V. How do central banks react to uncertainty 13
A. Net forward-looking language as an anchoring device 19
VI. How do central banks communicate uncertainty 20
VII. Conclusion 27
References 28
Appendices
A. Appendix 31
A.1. Data 31
A.2. Robustness with static equation 31
A.3. Robustness with equation in 12-months difference 32
A.4. Robustness controlling for the zero lower bound 35
A.5. Robustness to different dictionary: the ECB index 36
List of Tables
1. Dynamic model - lag net forward-looking index 15
2. Dynamic model - lag net forward-looking index with more uncertainty measures 18
3. Correlates of forward-/backward-looking communication - decomposing the net forward-looking index 19
4. Anchoring of market interest rate expectations 21
5. Description of variables used among different specifications 31
6. Static model - Net forward-looking index with more uncertainty measures 32
7. Explaining the change in net forward-looking index all sample 33
8. Explaining the change in net forward-looking index advanced 34
9. Explaining the change in net forward-looking index developing 34
10. Dynamic model - lag net forward-looking index with more uncertainty measures 36

## List of Figures

1. Financial market and economic policy uncertainty 4  
2. Central banks' use of key communication tools 8  
3. Content of central banks' monetary policy communication 8  
4. Distribution of the net forward-looking index across country groups 11  
5. Net forward-looking index evolution over time for selected countries 11  
6. Correlations between backward- and forward-looking communication indices 12  
7. Inertia in the forward-looking communication index 13  
8. AE central banks' communication responses to inflation uncertainty over time 16  
9. Monetary policy uncertainty and net forward-looking communication 20  
10. Central bank uncertainty aligns with large shock events 22  
11. Cross-country correlation of the CBUI and policy rates 22  
12. Rolling correlation of CBUI 23  
13. What drives central banks to talk about uncertainty 24  
14. CBUI Highly Correlated with Policy Rate Pricing Uncertainty During Certain Periods 25  
15. ECB's backward-looking communication index: Robustness to dictionary 37

## I. INTRODUCTION

Successive large shocks—including pandemics, armed conflicts, geopolitical fragmentation, and trade tensions—have pushed uncertainty to historically high levels (Figure 1). Many policy makers expect the environment of elevated uncertainty to become the new normal (e.g., Bailey 2025, Georgieva 2025, and Lagarde 2025), posing new challenges to central banks. They point out that elevated uncertainty complicates forecasting, weakens signals of traditional policy tools, and risks reducing the effectiveness of conventional monetary policy. In this context, central bank communication has assumed greater importance as a policy instrument in its own right to help anchor and guide expectations. Gauging the effectiveness of central bank communication and improving its design are therefore central to maintaining effective monetary policy in times of enduring uncertainty.

Figure 1. Financial market and economic policy uncertainty  
![](images/9e1cdd34fe32c61bedd461324c399f15a7ff049c94b247cb2e0c09f3c7e4dddc.jpg)  
Note: The figure shows the European VSTOXX index (left axis), capturing financial market uncertainty, and the Global Economic Policy Uncertainty (EPU) index (right axis).

European central banks have increasingly relied on communication tools to support monetary policy since the 1990s, particularly after the Global Financial Crisis (GFC). The move toward central bank independence, the establishment of the European Central Bank (ECB), and the expansion of monetary policy tools to include quantitative measures reinforced the need for transparent, systematic, and clear communication to help establish credibility and anchor expectations (Blinder, Ehrmann, Fratzscher, De Haan, and Jansen 2008; Blinder, Ehrmann, de Haan, and Jansen 2024; Armelius, Bertsch, Hull, and Zhang 2018). The GFC accelerated this process, as unconventional policies—such as large-scale asset purchases, and negative interest rates—required more frequent and clearer explanations to signal central banks' intentions and maintain policy credibility. This shift extended across many European central banks, which gradually increased the frequency, transparency, and scope of their communications to shape market and public expectations. Today, they face additional challenges, including persistent inflation pressures and heightened uncertainty from the Russian war in Ukraine, the war in the Middle East, and evolving geopolitical and trade tensions, making effective communication even more critical.

Given persistently elevated uncertainty, this paper examines how central banks in Europe communicate and adjust messaging in response to different sources of uncertainty. We address four key questions: First, how have these central banks communicated when responding to heightened uncertainty: more cautious and “data-dependent” by using backward-looking language for flexibility, or more assertive and forward-looking to anchor agents’ expectations? Second, do central banks react differently depending on the source of uncertainty—whether it is directly influenced by monetary policy (e.g., inflation uncertainty) or largely outside of their control (e.g., financial or stock market-implied uncertainty)? Third, do emerging market (EM) central banks react differently from their advanced economy (AE) counterparts? Fourth, how do central banks’ own assessment of uncertainty and monetary policy outlook compare with market participants’ perceptions?

To address these questions, we survey the landscape of communication practices of major European central banks and develop AI-based numerical indicators that track how central banks adjust communication styles over time. Focusing on monetary policy statements—comparable documents released by central banks following policy decisions and available over sufficiently long time series—we measure the shifts in the balance between forward- and backward-looking language as the magnitude and sources of uncertainty evolve. A key distinction in this paper concerns different forms of forward-looking communication. While the literature often associated forward-looking communication with commitment-based forward guidance (i.e., explicit signals about the future path of policy instruments), our focus is broader. We capture forward-looking language as information-based communication about the economic outlook, risks, and likely policy reactions, which may or may not involve explicit commitments.

This paper contributes to three strands of the literature on monetary policy and central bank communication. First, it examines how central bank communication mitigates information frictions and anchors inflation expectations, particularly under heightened uncertainty. Theory provides rich guidance on how monetary policy should react to different uncertainty: gradual adjustments under uncertain monetary policy transmission (Brainard, 1967) but aggressive if faced with inflation uncertainty (Dupraz, Guilloux-Nefussi, and Penalver, 2023; Soederstroem, 2002; Gust, Herbst, and López-Salido, 2025). But theory offers limited insight on optimal central bank communication under heightened uncertainty. Markets and households often lack knowledge of the central bank reaction function, weakening transmission (Blinder and others 2008, Blinder and others 2024, Bernanke 2025). Empirical evidence shows that greater transparency increases the extent to which private agents rely on public central bank information, thereby improving expectations formation, especially during volatile periods (Crowe and Meade (2008); Altavilla, Gürkaynak, Kind, and Laeven 2025). Clear but state-contingent communication of credible monetary policy rules can reduce uncertainty about policy intentions and limits discretionary errors (Orphanides 2019, Orphanides 2025), though micro evidence highlights that transmission effects also depend on agents' ability to internalize signals (Albrizio, Dizioli, Simon, and Zhang (2025)). Historical surveys document that formal monetary policy statements became routine as central banks shifted from secrecy toward transparency, later expanding to more elaborate monetary policy reports and meeting minutes (Blinder and others 2008; Jeanneau (2009)).

In addition, recent research highlights that effective central bank communication hinges on balancing forward-looking and backward-looking messaging under specific circumstances. Under heightened uncertainty, structured risk disclosure, scenario-based analysis, and timely narrative framing help markets interpret policy intentions and reduce misaligned inflation expectations (Fadda, Hanifi, Istrefi, and Penalver 2025; Garga, Herbst, McKay, Nicolo, and Paustian 2025, BIS (2025)). Theory provides ambiguous guidance on the relative effectiveness of forward- and backward-looking communication, as optimal strategies depend on economic conditions, the heterogeneity of agents and shocks, and the severity of information frictions (Angeletos and Lian

2018 and Hagedorn, Luo, Manovskii, and Mitman 2019). Empirical evidence shows substantial cross-country differences driven by AE and EM contexts and varying uncertainty sources (Blinder and others (2024); BIS (2025)). An emerging theme concerns the complementary roles in communication: forward-looking communication conveys conditional policy paths and helps anchor expectations, while backward-looking communication explains past decisions, reinforces accountability, and supports institutional credibility (Blinder and others 2008, Blinder and others 2024, Bernanke 2025, and Christiano Silva, Moriya, and Veyrune (2025)). Consistent with this, Evdokimova, Mohácsi, Ponomarenko, and Ribakova (2023) find that EM central banks adapt more dynamically to real-time conditions, and Brandão-Marques and Nguyen 2024 show that forward-looking communication conditioned on scenarios strengthens credibility under uncertain inflation persistence.

Furthermore, this paper relates to a growing literature using artificial intelligence (AI) and natural language processing (NLP) to systematically quantify central bank communication and its impact. Text-as-data methods now enable large-scale analysis of speeches, statements, minutes, and reports across countries and over time, capturing features such as tone, thematic emphasis, and policy signals (Bholat, Hansen, Santos, and Schonhardt-Bailey 2015; Evdokimova and others 2023; Christiano Silva, Moriya, and Veyrune 2025). For example, Bholat and others 2015 provide an early framework for converting unstructured text into quantitative indicators relevant for policy analysis. Building on this, Evdokimova and others 2023 use NLP to compare the clarity and timeliness of communication across AE and EM central banks, showing that communications by several EM central banks have matched or exceeded those by the Fed and ECB in readability and inflation focus. Christiano Silva, Moriya, and Veyrune (2025) apply large language models to a broad cross-country dataset, showing that communication evolves with institutional frameworks such as inflation targeting, and that NLP can generate consistent measures to study communication effects across countries. They also construct forward- and backward-looking indexes using a broad set of communication documents including speeches. These studies demonstrate that AI-assisted text analysis provides a systematic, comparable, and policy-relevant tool for benchmarking central bank communication.

We show that, across a sample of twenty European central banks, formal communication toolkits are similar, particularly regarding publications such as monetary policy statements and online presence. Yet the degree of transparency and the intensity with which these tools are used differ significantly. AE central banks are more likely to publish meeting minutes, hold press conferences, and employ forward-looking tools such as scenarios, fan charts, and projected interest rate paths. These differences are also reflected in how central banks adjust their communication in response to uncertainty. Using a net indicator of forward- versus backward-looking communication across different sources of uncertainty, we find that, in a reduced sample of eleven central banks, both AE and EM central banks react mostly to inflation uncertainty, a source of uncertainty central banks can influence. However, while AE central banks shift toward a more forward-looking messaging as expected, EM central banks tend to shift in the opposite direction. Beyond constraints of available tools, this pattern may reflect credibility as a precondition for effective forward-looking communication (Cole, Martinez-Garcia, and Sims 2023). Rolling-window regressions point to an evolution in communication practices. In earlier periods, European AE central banks placed less emphasis on forward-looking communication in response to inflation uncertainty. During the low inflation (and low inflation uncertainty) environment following the euro area debt crisis, these central banks' forward-looking communication appears mostly driven by the low interest rate and the constraints of the effective lower bound. Only in recent years have they responded to rising inflation uncertainty by adopting more forward-looking messaging, accompanied by increased emphasis on the conditionality in messaging. More broadly, while the distinction between advanced and emerging economies provides a useful organizing framework, it may likely capture a range of underlying structural characteristics. Differences in institutional credibility, monetary policy frameworks, and exchange rate regimes may more directly account for cross-country variation in communication strategies. The AE/EM split should therefore be interpreted as a reduced-form proxy for these deeper characteristics.

The rest of paper is organized as follows: Section II provides an overview of central bank communication practices across a sample of twenty European central banks. Section III presents our methodology to build text-mining numerical indicators that summarize central bank communication, and Section IV provides some stylized facts of these indices for eleven European central banks. Section V and VI provide the empirical analyses using these indexes. Section VII concludes and provides some policy recommendations.

## II. A SURVEY OF CENTRAL BANK COMMUNICATION PRACTICES IN EUROPE

As a first step, we survey the existing European central bank communication toolkits and their use in practice. Having been disproportionately affected by a sequence of recent shocks, European central banks have increasingly converged on a similar set of communication tools, albeit with different usage intensity (Figure 

[中间内容因长度限制已省略]

nomies. In advanced economies, the change in net forward-looking index over the course of a year is strongly and positively associated with professional forecasters uncertainty in inflation forecasts, highlighting the importance of expectations management and the use of forward-looking language when inflation dynamics become less predictable. In contrast, emerging economies show a more modest and less consistent response to uncertainty in inflation forecasts. Overall, these results suggest that while central banks in both advanced and emerging economies adjust their communication in response to rising uncertainty, advanced economies tend to reinforce forward-looking guidance in the face of uncertainty in inflation forecasts, whereas emerging economies show a less pronounced shift toward forward-looking communication.

## A.4. Robustness controlling for the zero lower bound

This section includes a dummy variable for the zero lower bound period. In our sample Czech Republic, ECB, the United Kingdom, Poland and Sweden all experienced some periods of the zero lower bound. Results do not change much when controlling for the zero lower bound.

Table 10. Dynamic model - lag net forward-looking index with more uncertainty measures

<table><tr><td></td><td>(1)All sample</td><td>(2)AE</td><td>(3)EM</td></tr><tr><td>Lag financial volatility</td><td>0.018(0.033)</td><td>-0.122***(0.036)</td><td>0.056(0.048)</td></tr><tr><td>Lag net forward-looking index</td><td>0.558***(0.033)</td><td>0.509***(0.058)</td><td>0.529***(0.041)</td></tr><tr><td>Lag GDP uncertainty</td><td>0.827(1.064)</td><td>-0.873(1.901)</td><td>1.175(1.250)</td></tr><tr><td>Lag EPU</td><td>0.000(0.003)</td><td>0.010**(0.004)</td><td>-0.002(0.005)</td></tr><tr><td>Lag inflation uncertainty</td><td>-0.281**(0.137)</td><td>3.303***(0.812)</td><td>-0.436***(0.136)</td></tr><tr><td>Lag policy rate</td><td>-0.043(0.034)</td><td>-0.992***(0.185)</td><td>-0.005(0.038)</td></tr><tr><td>Interaction financial volatility</td><td>-0.068(0.070)</td><td>0.064(0.069)</td><td>-0.985***(0.278)</td></tr><tr><td>Interaction net forward-looking index</td><td>-0.024(0.044)</td><td>0.024(0.048)</td><td>-0.510**(0.205)</td></tr><tr><td>Interaction GDP uncertainty</td><td>-1.553(1.903)</td><td>-0.417(2.387)</td><td>3.706(3.049)</td></tr><tr><td>Interaction economic policy uncertainty</td><td>-0.003(0.006)</td><td>-0.007(0.006)</td><td>-0.029***(0.010)</td></tr><tr><td>Interaction inflation uncertainty</td><td>2.996(2.257)</td><td>1.162(2.259)</td><td>60.520***(7.326)</td></tr><tr><td>Interaction policy rate</td><td>-0.845(1.768)</td><td>-0.480(1.630)</td><td>34.184***(9.874)</td></tr><tr><td>Zero lower bound</td><td>3.267*(1.867)</td><td>-0.821(1.889)</td><td>0.594(1.752)</td></tr><tr><td>Constant</td><td>12.993(.)</td><td>4.478(.)</td><td>1.573(1.509)</td></tr><tr><td>Observations</td><td>1512</td><td>756</td><td>756</td></tr><tr><td>Adj. R-squared</td><td>0.758</td><td>0.861</td><td>0.454</td></tr></table>

Standard errors in parentheses  
Country fixed effects included. Standard errors clustered at the country level.  
\* $p < {0.10},{}^{* * }p < {0.05},{}^{* *  * }p < {0.01}$

## A.5. Robustness to different dictionary: the ECB index

A central bank should always be data dependent, but the term has been used in different ways and in different contexts across central banks. As a result, interpreting "data dependence" as inherently backward-looking may be misleading. In the case of the ECB, one could argue that the term is often used in a forward-looking sense, namely to communicate that future policy decisions will depend on incoming information—including updated projections—while avoiding pre-commitment to a particular policy path. From this perspective, references to data dependence may be better interpreted as an absence of forward guidance rather than as evidence of backward-looking communication. Given these alternative interpretations, this appendix evaluates the extent to which data-dependence-related terms affect the backward-looking index constructed in the main text.

Figure 15 plots the original index identified in the main text (orange line) alongside an alternative index constructed using the same dictionary but excluding terms related to data dependence (blue line). By construction, the blue line is lower than the orange line because the latter is based on a broader set of terms. More importantly, the two indices exhibit a high degree of co-movement, with a correlation coefficient of 0.85. In recent years, the ECB has made more frequent use of data-dependence-related language, which is reflected in the larger increase in the original index relative to the alternative measure. Nevertheless, the upward trend remains evident even after excluding these terms, indicating that ECB communication has become more backward-looking over time irrespective of how data dependence is classified.

Finally, it is important to emphasize that a shift toward more backward-looking communication does not necessarily imply a less sophisticated communication strategy. Indeed, in July 2022 the ECB deliberately discontinued commitment-based forward guidance and adopted a meeting-by-meeting, data-dependent approach. This reflected a strategic decision to preserve policy flexibility in an environment characterized by exceptionally high forecast uncertainty.

![](images/a2b9784eb33d734e65eb3d3769a9aacc0446109038fe1e13c18a9244316df027.jpg)  
Figure 15. ECB's backward-looking communication index: Robustness to dictionary  
This figure reports the backward-looking index excluding the terms related to data dependence.

![](images/3860c88f179bca3b584a7839cdc3e9c655b75ee1c97a9e3db69b2ec8ee680919.jpg)
"""
