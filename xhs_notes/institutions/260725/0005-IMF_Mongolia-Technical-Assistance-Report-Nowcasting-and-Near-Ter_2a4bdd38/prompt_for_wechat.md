你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# TECHNICAL ASSISTANCE REPORT

## MONGOLIA

Nowcasting and Near-Term Forecasting System at the Bank of Mongolia

APRIL 2026

PREPARED BY

Martin Fukač

Authoring Departments
Caucasus, Central Asia and Mongolia
Capacity Development Center (CCAMTAC)

Institute for Capacity Development (ICD)

©2026 International Monetary Fund

JEL Classification Numbers: C53, E37, E47, E58

Keywords:

The contents of this document constitute technical advice provided by the staff of the International Monetary Fund to the authorities of Bank of Mongolia (the "CD recipient") in response to their request for technical assistance. Unless the CD recipient specifically objects to such disclosure, this document (in whole or in part) or summaries thereof may be disclosed by the IMF to the IMF Executive Director for Mongolia to other IMF Executive Directors and members of their staff, as well as to other agencies or instrumentalities of the CD recipient, and upon their request, to World Bank staff, and other technical assistance providers and donors with legitimate interest, members of the Steering Committee of CCAMTAC (see Staff Operational Guidance on the Dissemination of Capacity Development Information). Publication or Disclosure of this report (in whole or in part) to parties outside the IMF other than agencies or instrumentalities of the CD recipient, World Bank staff, other technical assistance providers and donors with legitimate interest, members of the Steering Committee of CCAMTAC shall require the explicit consent of the CD recipient and the IMF's ICD department.

The analysis and policy considerations expressed in this publication are those of the authors

## Acknowledgments

## MEMBERS

![](images/ba558bd3ea3480e77ef5d868057a8c5b5eea7dc460719c4f42e3e44bdab9ca68.jpg)  
Armenia

![](images/e9bf662b10d7752f1aca15563ba2f426706d891d03f6b59d7102274a6822a79f.jpg)  
Azerbaijan

![](images/d1a7bba0c695f24406aba3278dc06031691c16ebd0f3769321497069ca8e2c4b.jpg)

![](images/fd2ff40b3586ff56e6c5570d86870c3938f04ef73264ccf37038a724bbc5332a.jpg)

![](images/b1d8bdb1abd884dd97c671f6df056f7266daff309e14c304e4bb4ee3f18cf933.jpg)  
Tajikistan  
Georgia  
Mongolia

![](images/8b97d4f469ad027427c4afd8acf1bc1be7fe224850cbc0f0680b5a08ccd2917a.jpg)  
Turkmenistan

![](images/f6e9cc1b95c8a128a1e07b5964ae4911d7804785f2fccb76842d3c21d3c7b6a6.jpg)  
Kazakhstan

![](images/8c873403d00b816e2b22db110a0498350931d788e12ea1f0457fe8599f98eeea.jpg)

![](images/7ba10e2f3052e8e9d0ee3b3f0abcb6f0a19408f0555f0c91667a9555bc924c6b.jpg)  
Uzbekistan  
Kyrgyz Republic

## DEVELOPMENT PARTNERS

![](images/90a6fa9e81a1fd514c2d715af32de5a0cc78e03ef715511801c039fee04d60df.jpg)  
Switzerland

![](images/468dfd26f9e36f7803566b1d69c8b2a69b9845839c77180528fb42aacdbee711.jpg)  
Russia

![](images/8d7081eefa7e3f2833ea46fb76e87ce9966c941f0b7b6d1d919561bbd8b18a55.jpg)  
China

![](images/dea2030977bba8720794f559559d01f8b3f1807779f63a88b30f193e6e297d73.jpg)  
Ministry of Strategy and Finance
Republic of Korea

![](images/5710491b2730cd3f2122e00c8dcdf3b8fdbfe0d9abd2fe00e69b81ebbc53012e.jpg)  
United States of America

![](images/d6056a5d1791573ca87294d6162468adaf034dd42b6e52ea5eec0760244b0f0c.jpg)  
European Union

![](images/f1ca96d1cd0bebd4ccd5e8cbf210e5660a72b9d6d5e783910263a353327e9c2f.jpg)  
Asian Development Bank

![](images/026c4cf0bf582f4ff3a35579f120028751688ede96c16a64620b3361bd23f4a9.jpg)  
Poland

## Contents

Acknowledgments....3   
Abbreviations....6   
Preface....8   
Executive Summary....9   
Recommendations....10   
I. Background....11   
A. Macroeconomic and Monetary Policy Context....11   
B. Project Beneficiary....11   
C. Project Objectives, Deliverables and Timeline....11   
D. Integration with Broader Forecasting and Policy Analysis System....12   
E. NNTF System Design Principles....12   
II. System Components....13   
A. Analytical Software Platform....13   
B. Database System and Data Management....13   
C. Data....13   
D. Target Variables....13   
E. Model Portfolio....15   
F. Dynamic Model Forecast Averaging....15   
G. Forecast Quality Monitor....17   
H. Human Resources and Their Organization....18   
III. System Architecture and Initial Setup....19   
A. Organization....19   
B. Object-Oriented Approach....19   
C. Deployment....19   
D. Initial Setup....20   
IV. System Validation....23   
A. System vs. Benchmark Performance....23   
B. Potential Additional Accuracy Gains....25   
V. Selected Operational Issues....29   
A. Incorporating Expert Judgement and Off-Model Information....29   
B. Formulating Economic Narratives....30   
C. Dealing with Data Revisions....33   
D. Integrating NNTF and QPM....34   
VI. System Deployment....35   
VII. Next Steps....36

VIII. Authorities’ Views......37
Annexes
A. Annex List of Delivered TA Missions......38
B. Annex List of Target Variables and Their Selected Predictors......39

## Abbreviations

<table><tr><td>AIC</td><td>Akaike Information Criterion</td></tr><tr><td>AR</td><td>Autoregression</td></tr><tr><td>ARIMA</td><td>Autoregressive Integrated Moving Average</td></tr><tr><td>AS-ARIMA(X)</td><td>Automated Stepwise ARIMA with Exogenous Variables</td></tr><tr><td>BIC</td><td>Bayesian Information Criterion</td></tr><tr><td>BoM</td><td>Bank of Mongolia</td></tr><tr><td>BRIDGE</td><td>Bridge regression nesting LASSO and RIDGE estimators</td></tr><tr><td>BVAR</td><td>Bayesian Vector Autoregression</td></tr><tr><td>CCAMTAC</td><td>Caucasus, Central Asia and Mongolia Capacity Development Center</td></tr><tr><td>CPI</td><td>Consumer Price Index</td></tr><tr><td>EAPD</td><td>Economic Analysis and Policy Division, Bank of Mongolia</td></tr><tr><td>FPAS</td><td>Forecasting and Policy Analysis System</td></tr><tr><td>GARCH</td><td>Generalized Autoregressive Conditional Heteroskedasticity model</td></tr><tr><td>GDP</td><td>Gross Domestic Product</td></tr><tr><td>GDP-P</td><td>Production-Based Gross Domestic Product</td></tr><tr><td>GDP-E</td><td>Expenditure-Based Gross Domestic Product</td></tr><tr><td>GFCF</td><td>Gross Fixed Capital Formation</td></tr><tr><td>ICD</td><td>Institute for Capacity Development</td></tr><tr><td>IMF</td><td>International Monetary Fund</td></tr><tr><td>JVI</td><td>Joint Vienna Institute</td></tr><tr><td>LASSO</td><td>Least Absolute Shrinkage and Selection Operator regression</td></tr><tr><td>LBVAR</td><td>Large Bayesian Vector Autoregression</td></tr><tr><td>MA</td><td>Moving Average</td></tr><tr><td>MIDAS</td><td>Mixed Data Sampling</td></tr><tr><td>MCD</td><td>Middle Eastern and Central Asia Department, IMF</td></tr><tr><td>MPC</td><td>Monetary Policy Committee</td></tr><tr><td>MPD</td><td>Monetary Policy Department, Bank of Mongolia</td></tr><tr><td>NNTF</td><td>Nowcasting and Near-Term Forecasting</td></tr><tr><td>NSO</td><td>National Statistics Office Mongolia</td></tr><tr><td>NTF</td><td>Near-Term Forecasting</td></tr><tr><td>QPM</td><td>Quarterly Projection Model</td></tr><tr><td>RIDGE</td><td>Regularized Linear Regressions</td></tr><tr><td>RMSE</td><td>Root Mean Squared Error</td></tr><tr><td>RMSFE</td><td>Root Mean Squared Forecast Error</td></tr><tr><td>SARIMA</td><td>Seasonal ARIMA</td></tr><tr><td>STI</td><td>Singapore Training Institute</td></tr><tr><td>TA</td><td>Technical Assistance</td></tr></table>

U-MIDAS

Unrestricted Mixed Data Sampling

VAR

Vector Autoregression

WA

Weighted Average

## Preface

The Caucasus, Central Asia, and Mongolia Capacity Development Center (CCAMTAC) of the International Monetary Fund (IMF), in collaboration with the IMF's Institute for Capacity Development (ICD), supported the Bank of Mongolia's (BoM) efforts in strengthening its economic surveillance capacities through enhancing and expanding its nowcasting and near-term economic forecasting (NNTF) apparatus. The apparatus is one of the key components of the central bank's broader forecasting and policy analysis system that constitutes the analytical technology supporting evidence-based advice and the formulation of prudent, forward-looking monetary policy aimed at supporting living standards by maintaining price stability in Mongolia. This technical assistance (TA) project commenced in July 2022 and concluded in October 2025.

The project outcomes are a result of teamwork. The project team consisted of the CCAMTAC team: Mr. Martin Fukač (Resident Adviser, CCAMTAC; project manager and activity lead); and the Economic Analysis and Policy Division (EAPD) team — the primary TA recipient: Ms. Khulan Bayarsaikhan (Economist), Mr. Tsend-Ayush Bold-Erdene (Division Chief), Mr. Chinzorig Chuluunbaatar (Economist), Mr. Khanbold Gombodorj (Economist), and Mr. Enkhbayar Jambaldorj (Former Economist).

This project would not have been possible without the support of Mr. Byadran Lkhagvasuren (Governor, BoM) and Mr. Dominique Desruelle (Former Director ICD). The project team further gratefully acknowledges the generous support of CCAMTAC's donor community and the International Monetary Fund. The authors further wish to extend heartfelt appreciation to Mr. Bayardavaa Bayarsaikhan (Director General of the Monetary Policy Department, MPD) for constant support and guidance, and to the staff of the MPD for their constructive feedback and contributions at various stages of the project. Gratitude is also extended to Ms. Angana Banerji (Former Mongolia Mission Chief, MCD), Mr. Andrew Berg (Deputy Director, ICD), Mr. Alexander Borodin (TA Review Team, ICD), Mr. Paul Cashin (Former Division Chief, ICD), Mr. Natan Epstein (Division Chief, ICD), Mr. Norbert Funke (Director, CCAMTAC), Mr. Thomas Harjes (Deputy Director, JVI), Mr. Yaroslav Hul (ICD), Mr. Tigran Poghosyan (IMF Resident Representative to Mongolia, MCD), Ms. Laure Redifer (Former ICD), Mr. Kai Song (ICD), Mr. SeokHyun Yoon (Former IMF Resident Representative to Mongolia, MCD), and Mr. Felipe Zanna (Deputy Division Chief, ICD) and numerous other colleagues for their support and expert guidance.

The project execution greatly benefited from the administrative, budget, logistics, and other coordination support from Ms. Irina Kouropatkina (ICD), Ms. Elisa Manarinjara (ICD), Ms. Aiymkan Talaibek kyzy (CCAMTAC), Ms. Grace Tiberi (ICD), Ms. Riham Yousif (ICD), Ms. Imel Yu (ICD), and Mr. Yerassyl Shayakhmetov (CCAMTAC).

## Executive Summary

This technical assistance (TA) report documents the development and implementation of a nowcasting and near-term forecasting (NNTF) system for the Bank of Mongolia (BoM). The system strengthens BoM's capacity for timely macroeconomic surveillance and supports the conduct of monetary policy by providing a more systematic and reliable assessment of near-term economic developments. In comparative terms, the NNTF framework ranks among the most advanced systems implemented with IMF support across the CCAMTAC region.

The NNTF system provides real-time monitoring of incoming data and supports early identification of deviations from baseline projections, improving the information set available for policy discussions. Validation exercises show that the system delivers materially stronger forecast performance than historical staff forecasts, especially at the nowcasting and one-quarter-ahead horizons, with forecast errors reduced by up to 25 percent for key indicators such as consumer prices and major GDP components.

Beyond technical gains, the introduction of the NNTF system has enhanced how near-term analysis is used in the policy process. Compared with the previous framework, the upgraded system supports a more structured incorporation of judgment, clearer economic narratives accompanying numerical forecasts, and a more disciplined treatment of data revisions—elements that are essential for timely, transparent, and well-informed monetary policy decisions.

Looking ahead, sustained operational use, continued staff engagement, and targeted system refinement will be important to preserve these gains and to ensure that near-term analysis feeds reliably into medium-term policy assessments under the broader forecasting and policy analysis system.

## Recommendations

<table><tr><td colspan="3">Institutionalization</td></tr><tr><td>1.</td><td>Institutionalize regular use of the NNTF system in MPD forecasting rounds.</td><td>Short term / MPD</td></tr><tr><td colspan="3">Maintenance and Further Development</td></tr><tr><td>2.</td><td>Establish a structured internal feedback mechanism on forecast performance.</td><td>Short term / EAPD</td></tr><tr><td>3.</td><td>Focus technical refinements on selected high-priority variables.</td><td>Short term / EAPD</td></tr><tr><td>4.</td><td>Expand automation of routine reporting where feasible.</td><td>Short term / EAPD</td></tr><tr><td colspan="3">Human Resources</td></tr><tr><td>5.</td><td>Formalize internal training and onboarding for NNTF users.</td><td>Short term / MPD</td></tr></table>

## I. Background

## A. Macroeconomic and Monetary Policy Context

1. Mongolia is a small, open, commodity-exporting economy, with coal and copper accounting for a large share of exports, fiscal revenues, and economic activity. As a result, macroeconomic performance is highly sensitive to commodity price cycles and external demand conditions. In addition, the agricultural sector—employing a significant share of the population—is vulnerable to adverse weather conditions, contributing to volatility in output and consumer prices.

2. The Law on the Central Bank establishes price stability as the primary objective of monetary policy. In practice, monetary policy is conducted under an inflation-targeting framework, with a medium-term inflation target of 6 percent $\pm2$ percentage points. The Monetary Policy Committee (MPC) determines the policy rate, while liquidity conditions are managed through open market operations.

3. The exchange rate follows de jure floating regime. In practice, the exchange rate regime functions as a crawl-like arrangement, allowing flexibility while smoothing volatility through interventions.

4. These structural features underscore the importance of timely and reliable near-term economic monitoring tools to support policy decisions.

## B. Project Beneficiary

5. The Economic Analysis and Policy Division (EAPD) of the Monetary Policy Department (MPD) is the primary beneficiary of the TA project. The core team comprises: Mr. Tsend-Ayush Bold-Erdene (Division Chief), Mr. Enkhbayar Jambaldorj (Economist, senior NNTF operator), Ms. Khulan Bayarsaikhan (Economist, junior NNTF operator), Mr. Chinzorig Chuluunbaatar (Economist, second NNTF operator), Mr. Khanbold Gombodorj (Economist).

6. The division's core functions include monitoring current economic developments, assessing risks to price and macroeconomic stability, and contributing to the formulation of monetary policy advice. EAPD staff produce near-term forecasts of key macroeconomic variables, which serve as inputs into the Bank's medium-term projection models and policy scenario analysis.

7. Strengthening near-term forecasting capacity is therefore directly aligned with EAPD's operational mandate and supports the effectiveness of the Bank's inflation-targeting framework.

## C. Project Objectives, Deliverables and Timeline

8. The primary objective of the TA project was to strengthen the Bank of Mongolia's near-term forecasting capacity through the development of a comprehensive NNTF system. Specific objectives included improving forecast accuracy, broadening sectoral coverage, strengthening automation, and enhancing the sustainability of analytical tools.

9. The project emphasized three complementary pillars. The first pillar focused on the technical design and implementation of the NNTF system, including model development, forecast-combination techniques, and system architecture. The second pillar emphasized capacity development, with targeted training aimed at enabling staff to operate, maintain, and further develop the system independently. The third pillar focused on operational integration, including communication of results and alignment with the broader forecasting and policy analysis framework.

10. TA was delivered through a sequence of missions between June 2021 and October 2025, combining hands-on system development with training and validation exercises. A complete list of missions is provided in Annex A.

## D. Integration with Broader Forecasting and Policy Analysis System

11. The NNTF system is an integral component of the Bank's broader forecasting and policy analysis system (FPAS). It addresses information gaps arising from publication lags in key macroeconomic statistics, particularly national accounts and balance-of-payments data, by synthesizing signals from high-frequency indicators.

12. Near-term forecasts generated by the system provide initial conditions for medium-term projection models, including semi-structural quarterly models used in policy analysis. The accuracy of these initial conditions is critical, as forecast errors at short horizons can propagate into medium-term projections and affect policy conclusions.

13. Beyond its original role in supporting medium-term projections, the NNTF system provides a stand-alone platform for real-time macroeconomic monitoring. It supports sectoral analysis, enhances cross-sectoral consistency, and strengthens the flow of structured information to policymakers.

## E. NNTF System Design Principles

14. The design of the NNTF system reflects institutional constraints and operational needs within EAPD. Staff rotation, evolving analytical priorities, and limited programming expertise necessitate a framework that is robust yet easy to operate.

## 15. Three design principles guided system development:

Scalability ensures that the system can accommodate expanding data coverage, additional target variables, and a growing user base without fundamental restructuring.

Flexibility allows new models, variables, and methodological approaches to be incorporated with minimal disruption. Models can be activated or deactivated as analytical needs evolve.

Trainability ensures that staff can operate the system reliably following structured training and limited hands-on practice. This reduces dependence on a small number of technical specialists and supports institutional sustainability.

16. An object-oriented architecture underpins these principles and supports long-term maintainability.

## II. System Components

## A. Analytical Software Platform

17. Selection of the analytical software platform was guided by long-term sustainability, availability of documentation and peer support, ease of use, cost effectiveness, and academic adoption. Following assessment of alternatives, the Bank retained its existing platform, which meets o

[中间内容因长度限制已省略]

nts.

## Annex A. List of Delivered TA Missions

<table><tr><td>MISSION DATES</td><td>MISSION&#x27;S OBJECTIVES</td></tr><tr><td>March 6-10, 2023</td><td>Scoping. Review of the existing nowcasting and near-term forecasting (NNTF) processes, tools, data, human and IT resources with the aim to identify opportunities for improving the system&#x27;s accuracy in forecasting (non-mining) GDP growth and (unregulated) CPI inflation.</td></tr><tr><td>October 16-27, 2023</td><td>Initial development of the NNTF system, including setting up model portfolios and adapting the framework for Mongolian data. Introduced dynamic model averaging and tested forecasting performance. System expanded beyond non-mining GDP growth and CPI inflation.</td></tr><tr><td>April 15-26, 2024</td><td>Enhance internal communication of NNTF outputs for Monetary Policy Committee (MPC) briefings. Developed presentation templates for numerical results and economic narratives. Established a data release calendar and expanded the database for high-frequency indicators</td></tr><tr><td>September 13-27, 2024</td><td>Consolidate and optimize the NNTF system. Improve communication strategies and strengthen junior staff skills. Reviewed forecasting blocks for imports and refined database integration. Documented system results and assigned responsibilities for final reporting. Enhanced NNTF inputs into monetary policy review rounds.</td></tr><tr><td>October 29, 2024</td><td>On-line workshop on Bayesian vector autoregressions.</td></tr><tr><td>March 24 – April 5, 2025</td><td>Refine presentation templates for MPC briefings and train sectoral experts. Improve communication of risks and interest rate strategy. Assessed high-frequency data for enhancing near-term monitoring.</td></tr><tr><td>October 13 – 24, 2025</td><td>Final mission to conclude the project. Assisted in drafting system documentation, resolving operational issues, and formally launching the NNTF system into full operation. Institutional acceptance of the system and closure of the TA project.</td></tr></table>

## Annex B. List of Target Variables and Their Selected Predictors

<table><tr><td>Target variable</td><td>Explanatory variables</td></tr><tr><td colspan="2">Consumer prices</td></tr><tr><td>Consumer Price Index, headline</td><td>China CPIExchange rate (MNT/RMB)Household income</td></tr><tr><td>Beef</td><td>Monthly electricity production indexBusiness loan</td></tr><tr><td>Mutton</td><td>Monthly beef priceHousehold incomeLivestock loss rate</td></tr><tr><td>Other Meat</td><td>Monthly beef priceHousehold incomeLivestock loss rate</td></tr><tr><td>Milk</td><td>Monthly beef priceHousehold income</td></tr><tr><td>Flour</td><td>Household income</td></tr><tr><td>Vegetable</td><td>China CPI</td></tr><tr><td>Other Food</td><td>USA CPIHousehold incomeChina CPI</td></tr><tr><td>Imported Food</td><td>Exchange rate (MNT/RMB)Household income</td></tr><tr><td>Imported Good</td><td>China CPIConsumer loanUnit price of imported fuel</td></tr><tr><td>Domestic Good</td><td>USA CPIBusiness Loan</td></tr><tr><td>Service</td><td>Unit price of imported fuelHousehold income</td></tr><tr><td colspan="2">GDP production side</td></tr><tr><td>Manufacture</td><td>Monthly manufacture production index</td></tr><tr><td>Electricity</td><td>Monthly electricity production index</td></tr><tr><td>Trade</td><td>Total loanGoods import</td></tr><tr><td>Communication</td><td>Household incomeNominal effective exchange rate</td></tr><tr><td>Other service</td><td>Current expenditureConsumer loan</td></tr><tr><td>Net tax</td><td>Monthly tax revenueConsumer loan</td></tr><tr><td colspan="2">GDP expenditure side</td></tr><tr><td>Household consumption</td><td>Consumer loanWageTax revenueTotal import</td></tr><tr><td>Gross fixed capital formation</td><td>Machinery importChina GDPConsumer loan</td></tr><tr><td colspan="2">Credit</td></tr><tr><td>Business credit</td><td>Non-mining, non-agricultural sector growthPolicy rateTotal nonperforming loan</td></tr><tr><td>Consumer credit</td><td>Nominal wageTotal importPolicy rateTotal nonperforming loan</td></tr><tr><td colspan="2">Goods import</td></tr><tr><td>Consumer goods</td><td>Nominal Effective Exchange RateLending rateUS CPIGovernment expenditureImport price indexTotal new loan</td></tr><tr><td>Nondurable goods</td><td>Exchange rate (RMB/USD)Deposit rateRussia CPIConsumer loanImport Price IndexReal wage</td></tr><tr><td>Passenger cars</td><td>Exchange rate indexConsumer loanUS CPIIron ore export volumeService imports</td></tr><tr><td>Durable goods ex. passenger cars</td><td>Consumer loanRussian CPIDeposit rateExchange rate (MNT/USD)Export price indexReal Non-Mining GDP</td></tr><tr><td>Capital Goods</td><td>Export price indexEurozone CPIIron ore exportLending rateHousehold consumptionImport deflator</td></tr><tr><td>Construction materials</td><td>Consumer loanExchange rate (MNT/USD)</td></tr><tr><td rowspan="3"></td><td>Copper export volume</td></tr><tr><td>Deposit rate</td></tr><tr><td>Tax revenue</td></tr><tr><td rowspan="6">Equipment</td><td>Consumer Loan</td></tr><tr><td>US CPI</td></tr><tr><td>Export price index</td></tr><tr><td>OT Imported Payment of Service</td></tr><tr><td>Trade (GDP)</td></tr><tr><td>Government expenditure deflator</td></tr><tr><td rowspan="5">Vehicles</td><td>Iron ore export</td></tr><tr><td>Main commodities export volume</td></tr><tr><td>China CPI</td></tr><tr><td>Export price index</td></tr><tr><td>Real non-mining GDP</td></tr><tr><td rowspan="5">Industrial products</td><td>Deposit rate</td></tr><tr><td>Exchange rate index</td></tr><tr><td>Industrial production index</td></tr><tr><td>OT Imported Payment of Operation</td></tr><tr><td>Tax revenues</td></tr></table>
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
