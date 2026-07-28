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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
2026 GLOBAL INVESTOR SURVEY

# Investors Believe in AI— Now They Want Results

July 2026

## Amid market uncertainty, investors shared their expectations for the global economy and the companies they invest in

![](images/4aebb1f6d56083b5ef3d858afc141e6f6675bcc983d8285bb1c722d06bd6bb36.jpg)  
Sources: S&P Capital IQ; BCG's ValueScience Center.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific).

## 2026 survey

\- Investors were surveyed roughly three weeks after the start of the conflict in the Middle East

\- The S&P Global 1200 index was about 4,900 on March 23, 2026, approximately 6% below its January 2026 peak

\- Since the survey closed, the S&P Global 1200 has reached new all-time highs

## 2024 survey

\- Investors were surveyed immediately following the US presidential election

\- The S&P Global 1200 index was about 4,180 in November 2024—near an all-time high at the time of the survey

Investor sentiment for the medium term remains bullish, especially in North America and Asia-Pacific

Investors' sentiment for the next three years (%)

Investors' sentiment for the next three years, by region (%)

![](images/31f40e55fdd7886b9c8b8f32326457ad5d32ca0e568731a61ebae021f6da987a.jpg)  
Sources: BCG's global investor surveys.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). Bullishness measures the directional conviction of investors, not the magnitude of expected returns. Because of rounding, the percentages may not add up to 100.  
Survey question: Where would you place yourself on the bull-bear spectrum over the next three years?

## However, investors' market-average TSR expectations for the next three years are muted

Average TSR expected for the subsequent three years  
![](images/9b672960b084d2bdfb35aed441830cea1e1c8f271e3399e85c4044dd55f76eaa.jpg)  
Average TSR expected through year-end 2028, by region

![](images/f04ee09b9d4dfcb4d9e99df34b70858bfbd601f42fec026b5a3738c0a2842110.jpg)  
Sources: BCG's global investor surveys, 2010–2026.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). Expected TSR through year-end 2028 is calculated as a weighted average of the midpoint of the return range selected by respondents, annualized over three years, and including the annual dividend yield for each index. Results are weighted by the number of responses. Data from 2010 through 2014 and from 2017 through 2026 is based on all respondents across 16 indices (with the S&P 500 being over-represented). Data from 2015 through 2016 is based only on respondents using the S&P 500 as their benchmark. Any discrepancies when compared with prior survey results are due to rounding.  
Survey question: At what level do you expect the [index] to be three years from now (through year-end 2028)?

Too pessimistic $^{2}$ | Too optimistic $^{2}$

## Investors see the market as too bullish across key market drivers, especially on the future impact of AI

<table><tr><td colspan="7">Key geopolitical and macro factors influencing capital markets</td></tr><tr><td></td><td>Investors&#x27; top-three factors (%)</td><td>2026 vs. 2024 (pp)</td><td colspan="2">Investors&#x27; evaluation of the market&#x27;s view (%)</td><td>Net optimism (%)1</td><td>2026 vs. 2024 (pp)</td></tr><tr><td>War in Ukraine and the conflict in the Middle East</td><td>60</td><td>+29</td><td>15</td><td>30</td><td>15</td><td>+3</td></tr><tr><td>Interest rate policy</td><td>54</td><td>-5</td><td>15</td><td>30</td><td>15</td><td>-7</td></tr><tr><td>US federal policies</td><td>49</td><td>+3</td><td>21</td><td>31</td><td>10</td><td>-6</td></tr><tr><td>AI development and regulation</td><td>45</td><td>+22</td><td>15</td><td>56</td><td>41</td><td>+7</td></tr><tr><td>Cost of capital</td><td>21</td><td>-7</td><td>16</td><td>19</td><td>3</td><td>-12</td></tr><tr><td>China GDP outlook</td><td>17</td><td>-15</td><td>18</td><td>26</td><td>8</td><td>+2</td></tr><tr><td>Structural changes in asset management and allocation</td><td>10</td><td>+1</td><td>10</td><td>17</td><td>7</td><td>+2</td></tr><tr><td>Rest-of-Asia trade and economic acceleration</td><td>10</td><td>-5</td><td>13</td><td>19</td><td>6</td><td>0</td></tr><tr><td>BRICS expansion</td><td>9</td><td>-6</td><td>11</td><td>19</td><td>8</td><td>-3</td></tr><tr><td>Labor relations and cost</td><td>9</td><td>-8</td><td>13</td><td>20</td><td>7</td><td>+1</td></tr><tr><td>M&amp;A activity and regulation</td><td>6</td><td>-3</td><td>10</td><td>15</td><td>5</td><td>+3</td></tr><tr><td>Green industrial policy</td><td>6</td><td>-8</td><td>10</td><td>22</td><td>12</td><td>-7</td></tr></table>

Sources: BCG's 2026 Global Investor Survey; BCG's 2024 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). Any discrepancies when compared with prior survey results are due to rounding.  
$^{1}$ Net optimism is the share of investors who considered the market to be too optimistic minus the share who considered the market to be too pessimistic. $^{2}$ The market being too optimistic implies downside risk, whereas the market being too pessimistic implies upside opportunity.  
Survey questions: Which of the following factors do you believe will most influence the overall direction of your region's equity market for the remainder of 2026? How accurately do you believe investors have captured the following factors in market pricing?

## A significant share of investors expect a near-term recession and elevated inflation to continue

Investors who are seeing their region currently in a recession or anticipating one before year-end 2026 (%)

![](images/55133f610dc58a70b59cc927372087d804e81b6f940603ff78dae574f3ae86c1.jpg)  
Source: BCG's 2026 Global Investor Survey.  
Investors' expected time period for inflation to remain elevated (%)

![](images/529bb1a03a6f8516764757531f30bc1364726207b447ee59d75f480a5b58e621.jpg)  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). Because of rounding, percentages may not add up to 100.  
Survey questions: When do you expect the next economic recession to start in [home country]? How long do you expect inflation (as measured by the Consumer Price Index) to remain elevated above the central bank's target level (e.g., roughly $2\%$ for the US)?

Investors believe tariffs will negatively affect corporate margins, consumer spending, stock market performance, and GDP growth

![](images/5145965bbd7d481fb35cb91eafe3a7e97591ff40c36ccf94c542267a89a30f4e.jpg)  
Source: BCG's 2026 Global Investor Survey.  
Note: NA = North America; EME = Europe and the Middle East; APAC = Asia-Pacific. n = 544 global investors (180 in NA, 184 in EME, and 180 in APAC). For consumer spending, a positive or negative impact reflects an increase or decrease in spending levels, respectively. For interest rates and consumer price levels, a negative impact reflects expectations that these will increase as a result of tariff policy, while a positive impact reflects expectations that these will decrease. $^{1}$ Net perspective is the share of investors who expected a positive impact minus the share who expected a negative impact, excluding investors who were unsure.  
The regional results were calculated separately using investors' responses in each region.  
Survey question: How would you rate the impact of the US tariff policy on the below metrics in [region] over the next 12 to 24 months?

Investors anticipate technology, health care, and exploration-based sectors to be macro beneficiaries, while consumer industries see macro headwinds

![](images/2a6f0071d6cd9553892930cacd5544f382f6c515ac35f39c4c46e76245a679c8.jpg)  
Source: BCG's 2026 Global Investor Survey.  
Note: NA = North America; EME = Europe and the Middle East; APAC = Asia-Pacific. n = 544 global investors (180 in NA, 184 in EME, and 180 in APAC).  
$^{1}$ Net perspective is the share of investors who expected a positive impact minus the share who expected a negative impact, excluding investors who were unsure.  
The regional results were calculated separately using investors' responses in each region.  
Survey question: How do you expect the current economic climate and political agenda to affect different sectors?

## Investors have shifted toward long-term structural winners and sectors that benefit from economic trends, while holding more dry powder

Investors' top changes to capital allocation and investing practices $(\%)^{1}$  
![](images/5a3129e580a92fe049d96d4cb0bbf3dea8b3418bc1896d99c0b6b83c9635ece2.jpg)  
Source: BCG's 2026 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). FCF = free cash flow.  
$^{1}$ The percentage reflects the share of investors selecting each factor among their top five changes. $^{2}$ For example, AI, energy, and the energy transition.  
Survey question: How have your capital allocation and investing practices or recommendations changed compared with your choices 12 months ago? Select up to five changes and rank them by importance.

## Growth remains the clear-cut, number one investment consideration, but investors are also increasingly focused on returns on capital

Investors' top investment considerations (%)

<table><tr><td colspan="5">2026 vs. 2024 (pp)</td><td></td></tr><tr><td></td><td>+2</td><td>+8</td><td>+5</td><td>-3</td><td>-2</td></tr><tr><td>Long-term organic growth outlook</td><td>54</td><td></td><td></td><td></td><td></td></tr><tr><td><img src="images/17202d9f3057d2b7316489d83cbcd9122fd943b335f7928dadf61e37e16cd7ea.jpg"/></td><td>19</td><td>Short-term growth momentum</td><td>18</td><td>FCF conversion, generation, and/or yield</td><td>17</td></tr><tr><td>Potential for market share gains</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Sources: BCG's 2026 Global Investor Survey; BCG's 2024 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). Only the five highest-rated considerations are shown; respondents ranked 20 factors. FCF = free cash flow. Any discrepancies when compared with prior survey results are due to rounding.  
Survey question: How important are the following metrics or characteristics for your investment decisions and recommendations regarding financially healthy companies over the next 12 to 18 months? Please indicate your five most important considerations.

## Roughly 60% of investors support activist investors, but fewer believe that shareholder activism drives stronger midterm or long-term TSR

Investors' posture regarding activist investors (%)  
![](images/5b920d46401685add80904c1b2bc048c78ba40a9887eb3e41b5949ba33e54f74.jpg)  
Investors who believe that activism drives stronger mid- or long-term TSR (\%) $^{1}$

![](images/6b6fba60795a54de62edd408514e8a59efb62eed5f7e2b240d93e8bb92cac2b9.jpg)  
Sources: BCG's 2026 Global Investor Survey; BCG's 2024 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). Any discrepancies when compared with prior survey results are due to rounding.  
$^{1}$ The results reflect investors who somewhat agreed or strongly agreed. For comparability, the 2024 result excludes respondents who selected the neutral response.  
Survey question and statement: Where would you place yourself on the range of activism-related postures? Most of the activist campaigns I have witnessed  
have helped drive stronger mid- or long-term TSR for shareholders overall.

## Investors want companies to balance near-term EPS with longer-term investments, but when they are forced to choose, growth wins

Most investors consider it important for companies to deliver profitability and invest for growth...

...but when faced with a tradeoff, almost three times as many investors want companies to focus on growth

![](images/e68a3815ec802c33619260518fc1f91c158aebb7b1284991d690d145e7dcd007.jpg)  
Sources: BCG's 2026 Global Investor Survey; BCG's 2024 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). EPS = earning per share.  
Survey questions and statements: It is important for healthy companies to deliver EPS over the current fiscal year that at least meets guidance or consensus. (The results reflect the share of investors who somewhat agreed and strongly agreed.) It is important for healthy companies to prioritize building key business capabilities (for example, digital or technology infrastructure) that create advantage, deliver attractive returns, and/or reduce risk longer term, even if it means guiding to lower EPS or delivering below consensus. (The results reflect the share of investors who somewhat agreed and strongly agreed.) Which of the following best describes your view? Companies should prioritize near-term EPS, thread the needle and try to deliver on both, or prioritize long-term growth.

## Investors want companies to invest organically, reshape the portfolio, avoid leverage, and pay consistent dividends

Investors who agree with each statement (%)

![](images/0876063f9645788aaceb449beaa45961e3e17c5d38b99178a472b2635a1dce82.jpg)  
Sources: BCG's 2026 Global Investor Survey; BCG's 2024 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). The results shown reflect the share of investors who somewhat agreed and strongly agreed.

## Investors believe AI will affect corporate fundamentals in the near term...

Investors' expectations for when AI will have a materially positive impact on corporate fundamentals (%)

![](images/3cd3a8a9e9e2ceef6c656341895cc4fb4b984c3a7055ef0835a817bfdd599269.jpg)  
Source: BCG's 2026 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). Because of rounding, the percentages may not add up to 100.  
Survey question: When do you expect AI to have a materially positive impact on corporate fundamentals (growth, profitability) across most industries, excluding technology companies focused on AI infrastructure?

## ...but a minority of investors view AI as a source of sustained competitive differentiation longer term

Investors' perspectives on AI as a competitive advantage (%)

![](images/acf7ba033222a15d1bac545dc8d0215c6992bfecd79bb3907d176301a37b0e67.jpg)  
Source: BCG's 2026 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). Because of rounding, the percentages may not add up to 100.  
Survey question: What is your perspective on the AI investments being made by companies you invest in or cover that compete in industries where AI will likely play an important role, excluding technology companies focused on AI infrastructure, tools, etc.?

The impact of AI is expected to be strongest on labor productivity, corporate fundamentals, and growth, but at the cost of jobs and wages

![](images/2119eb4580f5778d0e2902fc53c06fc43629d8562f5f4d01406fbc1be83c5aa0.jpg)  
Source: BCG's 2026 Global Investor Survey.  
Note: NA = North America; EME = Europe and the Middle East; APAC = Asia-Pacific. n = 544 global investors (180 in NA, 184 in EME, and 180 in APAC).  
$^{1}$ Net perspective is the share of investors who expected a positive impact minus the share who expected a negative impact, excluding investors who were unsure.  
The regional results were calculated separately using investors' responses in each region. $^{2}$ A reduction in consumer price levels and unemployment is considered a positive impact.  
Survey question: What impact do you expect AI to have in the following areas over the next 24 months in [your region]?

![](images/b94997988e5a645616442bfc3121b0e7f1b433a5349f5835d404c1c2a3a68d01.jpg)  
Investors' views on how accurately AI development and regulation is reflected in market valuations (%)

## Investors believe the market is overly optimistic on AI's potential, raising concerns about market valuations and headwinds for future returns

![](images/aabdb23b89e61f7b1fa1afb01a1a49d6eefeefba0ec7485b1740be9b4abb215e.jpg)  
Investors who think market valuations and AI expectations are likely to hinder returns (%)

![](images/784eff951cba3fbb854fe26642773c9ea4e876b171d48bba1492b63d6f836853.jpg)  
The potential compression of valuation multiples may cause companies' TSR to depend on improved fundamentals, such as growth, margin expansion, and free cash flow generation  
Source: BCG's 2026 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific).

## Most investors deliberately evaluate companies' AI strategies and see room for improvement

Investors who agree with each statement (%)  
![](images/b69f6678fdfe277faf3a91ea1ac3182cef1a4bb6d7f87fe01988f3700f9b6098.jpg)

## Investors are concerned about AI execution capabilities but see current AI investments as too aggressive and sizable margin dilution as unacceptable

Investors who agree with each statement (%)  
![](images/f1baaded59470b83a7905f2617f5fd0c8d79aea71dd08d2d27ca7bb4c2120fc7.jpg)  
Source: BCG's 2026 Global Investor Survey.  
Note: n = 544 global investors (180 in North America, 184 in Europe and the Middle East, and 180 in Asia-Pacific). The results reflect investors who somewhat agreed and strongly agreed. The questions excluded technology companies focused on AI, including infrastructure and tools.

## Investors ultimately expect AI to create meaningful value, especially in health care, technology, financial institutions, and industrials

![](images/6c44fe1373a998f4f46595d697a7bc722c1686519537a62849735c1f3e6d034c.jpg)  
Source: BCG's 2026 Global Investor Survey.  
Note: NA = North America; EME = Europe and the Middle East; APAC = Asia-Pacific. n = 544 global investors (180 in NA, 184 in EME, and 180 in APAC).  
$^{1}$ Net perspective is the share of investors who expected a positive impact minus the share who expected a negative impact, excluding investors who were unsure. The regional results were calculated separately using investors' responses in each region. $^{2}$ Financial institutions includes insurance companies.  
Survey question: How do you expect the development of AI to affect the financial fundamentals (e.g., revenue growth, margins, profitability, and free cash flow generation) of companies across different sectors within the next three years (by year-end 2028)?

In the current investment environment, it is critical for companies to align their business, financial, and investor strategies

Integrated TSR strategy

![](images/d2ba9352fd192c22b72064c1674e8dc8cc553f5242d0c603b5325021a9b36bd2.jpg)  
Source: BCG analysis.
Note: EPS = earnings per share.

![](images/3a37574249bfb3a11fbb0cfd4d6cfe227ac8cb6b53aee20685ea5268c34401fc.jpg)

## Business strategy

Growth, margins,
portfolio, M&A, and risk

\- Deliver near-term EPS while investing for long-term growth

\- Invest in the core with a credible path to returns

\- Articulate how AI creates competitive advantage specific to the business

\- Actively reshape the portfolio by divesting noncore businesses and pursuing focused tuck-in M&A, but avoid transformative deals that stretch the balance sheet

![](images/14d3a322e7fb7acb8f1b9248269351e077a2441669227d8579434689dce5f352.jpg)

## Financial strategy

Capital structure,
dividends, and buybacks

\- Avoid high leverage by staying below three times net debt to EBITDA

\- Maintain dividends at historical levels, and buy back shares opportunistically, not aggressively

\- Treat AI capex as an investment with accountable payback, but avoid diluting margins significantly or levering up to fund it

![](images/a883e96302094000bfd29c888d31b015127b2e5b95c57f576d2b6065f65435f9.jpg)

## Investor strategy

Investor type, valuation multiple, and messaging

\- Know your investor base, understanding how focused your shareholders are on growth versus profitability versus cash flow generation

\- Communicate a clear capital-allocation strategy, showcasing reinvestment discipline, limited leverage, and healthy cash returns through dividends and/or buybacks

\- Expect increased activist scrutiny, and proactively strengthen near- and medium-term fundamentals

## About the survey

BCG's 2026 Global Investor Survey is the 14th edition and captures the views of 544 institutional investors. It was conducted March 23, 2026—April 10, 2026.

The findings are presented at the global level, reflecting areas of broad consensus and those where investor perspectives vary. Select regional differences are noted where they are most meaningful.

![](images/af76a86824685a44b988a7302581f467767d7e449f67bcfc87ecb30fe762049a.jpg)

![](images/e04665978da054fc477602e8b84d9d396839fd77b89ff6a1ed69a46c1edeac8e.jpg)

![](images/75de338f436b5ad2585ad1cf69d8c8606ce917ebc74f938d2b5f2712337f623e.jpg)

![](images/39eb85ac4ecf72635f205dbce6eeb91869bf3d376e96dff865a6f0f817289f09.jpg)

544

Investors
surveyed

## 16

Countries globally

180
North
America

## 91%

## \$35T

Buy-side
professionals $^{1}$

2 North America

Combined AUM $^{2}$

## 94%

North America

\$11T North America

## 184

Europe and the Middle East

Europe and the Middle East

## 88%

Europe and
the Middle East

\$10T
Europe and
the Middle East

180
Asia-
Pacific

7 Asia-Pacific

90%
Asia-
Pacific

\$14T Asia-Pacific

Source: BCG's 2026 Global Investor Survey. $^{1}$ Portfolio managers and buy-side analysts. $^{2}$ AUM represents the assets managed by the respondents' firms in each region.
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
