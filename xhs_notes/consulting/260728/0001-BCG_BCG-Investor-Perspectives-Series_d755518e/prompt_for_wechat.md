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
## BCG Investor Perspectives Series

US Edition, Q2 2026

SURVEY CONDUCTED JUNE 22–23, 2026

## BCG Investor Perspectives Series | US Edition, Q2 2026

BCG surveyed leading investors June 22–23, 2026, to understand their perspectives on the US economy and US stock market, as well as their expectations for the companies they invest in or cover. This survey has important implications for the strategic decisions being made by senior executives and boards of directors.

This is BCG's 34th US investor pulse check since March 2020. In addition, we have conducted three European investor pulse checks since April 2025.

BCG conducted this pulse check survey to help corporate executives and boards of directors understand investors' perspectives in this rapidly changing environment.

\- Approximately 63% of the participants in the June 2026 survey overlap with the respondents in the survey conducted March 23–27, 2026, and 82% of the March participants overlapped with those surveyed September 25–28, 2025

\- Across the three most recent surveys (September 25–28, 2025, March 23–27, 2026, and June 22–23, 2026), the overlap in respondents is 57%

## About the respondents:

\- They represent investment firms that have approximately \$10 trillion in combined assets under management

\- Over $90\%$ are portfolio managers and senior buy-side analysts who are responsible for buy, sell, and hold decisions

\- They cover a broad spectrum of investor types and investment styles, including deep value, income, quality value, growth at a reasonable price (GARP), and core growth; they also include some quantitative, technical, and special situation investors

## The survey focused on three key topics:

## 1

Investors' views of and expectations for the US economy and stock market, and their views on key risks and opportunities in the current environment

2

Investors' expectations regarding the future impact of AI and GenAI as well as their related priorities for companies they invest in or cover

3

Investors' perspectives on and implications for important decisions that corporate executives and boards are considering and making

\- Because the market environment is evolving, especially regarding macroeconomic conditions, some questions from prior surveys were not asked or were replaced with new ones in this edition

\- The analysis shared in this document represents an aggregated view that is not segmented by investor type; it is important for corporate executives and boards of directors to keep in mind their current and target investor types while interpreting the results

\- The results represent surveyed investors’ views only—reflecting current investor sentiment and currently priced-in expectations—both of which are subject to change as new information becomes available; to understand BCG’s point of view on current topics, please visit bcg.com

## This edition compares the findings from the June 2026 US pulse check to the March 2026 and September 2025 pulse checks

## June 22–23

![](images/d6976d485de1a2893a3b9d92442922f7c1143663c636ee126827bd1f39bc32c2.jpg)  
New tariff policies announced, Apr 2, 2025  
Middle East ceasefire announced, Apr 8, 2026

Start of conflict in the Middle East, Feb 28, 2026

## Pulse check #34

\- Followed a strong market upswing (since April) and renewed market volatility in June

\- S&P 500 closed at 7,472 points on June 22, 2026 (about $1.8\%$ below current all-time high $^{1}$ )

## Pulse check #33

\- Initiated over three weeks after the start of the conflict in the Middle East

\- S&P 500 closed at 6,506 points on March 20, 2026 (about $6.7\%$ below prior all-time high²)

## Pulse check #32

\- Initiated after the market had recovered from the correction following the April 2025 new tariff policy announcement

\- S&P 500 closed at 6,638 points on September 24, 2025 (about $0.8\%$ below prior all-time high $^{3}$ )

## Investor Pulse Check, Q2 2026 | Highlights

## June 22–23

\- Investor sentiment improved materially, with 46% of investors bullish for the rest of 2026 (up from 26% in March 2026). At the same time, increased concerns about the S&P 500 being overvalued (raised by 67% of investors vs. 62% in March 2026) and potential profitability headwinds (raised by 51% of investors) led to market-average TSR expectations remaining muted at 6.2% over the next three years (versus 6.3% in March).

\- Interest rates and inflation have risen to become the top two macro risk factors, highlighted by 61% and 47% of investors, respectively (up from 47% and 35%, respectively, in March 2026), with geopolitics dropping from number one to number three, highlighted by 44% of investors (down from 69% in March).

\- AI now is the number one expected market driver (highlighted by 66% of investors, up from 54% in March 2026), with 56% seeing the market as too optimistic on AI (up from 55% in March), and 77% expecting future TSR headwinds as a result of elevated valuation levels due to AI (up from 63% in March).

\- Investors anticipate that AI will have a material impact on companies' financial performance (80% expect this to be reflected in revenue growth and/or profitability within the next two years), with more than 60% of investors expecting AI to primarily deliver efficiency gains or temporary first-mover advantages, compared with only 25% of investors seeing AI as a source of durable competitive advantage for AI winners.

\- As a result, investor scrutiny of AI is high, with 78% of investors specifically analyzing companies’ AI strategies (up from 72% in March 2026), and three times as many investors believing companies are overinvesting in AI rather than underinvesting (45% vs. 15%).

\- More broadly, investors remain strongly focused on companies' growth prospects (cited by $60\%$ as a key investment criterion, up from $55\%$ in March 2026), but most investors expect companies to also fully deliver on near-term EPS guidance and consensus ( $58\%$ , up from $52\%$ in March).

\- Investors want capital allocation to be disciplined and balanced across high-return investments (with 33% focusing on returns on capital) while maintaining healthy balance sheets (69% of investors avoid companies with over three times leverage) and paying consistent dividends (expected by 79%).

\- Investors want companies to actively shape their portfolios, with 79% saying that companies should consider divesting businesses and 78% supporting focused tuck-in acquisitions.

## US investors' current perspectives on the US economy and stock market

June 22–23

## Macroeconomic outlook

## INVESTORS WERE ASKED ABOUT THEIR VIEWS ON US RECESSION RISKS

17%

Investors that believe the US will experience a recession by the end of 2026

Below the March 2026 and September 2025 survey results of 43% and 53%, respectively

## INVESTORS WERE ASKED HOW LONG THEY EXPECT INFLATION TO REMAIN ABOVE THE FEDERAL RESERVE'S 2% TARGET

49%

Investors that believe inflation will remain elevated beyond year-end 2026

Above the March 2026 and September 2025 survey results of 47% and 38%, respectively

3.6%

3.3%

The average expected inflation rate for year-end 2026

The average expected inflation rate for 2027 and 2028

## Bull vs. bear sentiment

## INVESTORS WERE ASKED TO PLACE THEMSELVES ON THE BULL-BEAR SPECTRUM OVER DIFFERENT TIME PERIODS

46%

Investors that are
bullish for the
remainder of 2026

Above the March 2026 and September 2025 survey results of 26% and 36%, respectively

## INVESTORS WERE ASKED ABOUT THEIR INFLATION EXPECTATIONS

68%

Investors that are bullish for the next three years $^{1}$

Between the March 2026 and September 2025 survey results of 71% and 63%, respectively

## INVESTORS WERE ASKED ABOUT THEIR SENTIMENT TODAY, COMPARED WITH THREE MONTHS AGO

50%

Investors that are more bullish on the economy

Above the March 2026 survey result of 22% and equal to the September 2025 survey result

46%

Investors that are more bullish on the stock market

Between the March 2026 and September 2025 survey results of 28% and 57%, respectively

## Expected stock market low

S&P 500 market low

## Implied potential S&P decline from current level $^{2}$

6,946

Timing of low

7%

Matches series low vs. 8% in both March 2026 and September 2025 surveys

Q4 2026

## Stock market level in three years

S&P 500 level of... $^{2}$

8,664

...implies an average annual TSR for the next three years $^{1}$

6.2%

Near the March 2026 result of 6.3% and equal to the September 2025 result

Bullish

Neutral

Bearish

## Interest rates and inflation have become the top two macro risk factors, while geopolitical risks dropped to number three

![](images/d84626924993cbcfdb719c528512462733052c1ba127991efbddb58f6e741a4f.jpg)

## Two-thirds of investors view the S&P 500 as overvalued

June 22–23

Investor perspectives on current S&P 500 valuation level $(\%)^{1}$

![](images/571706e43bc837e8fe76f2bee58d4047fb51613c59ac63c69e1c8e8e8aabb140.jpg)

77% | Investors that anticipate TSR headwinds due to the current market valuation level and bullish AI expectations (up 14pp since March 2026). $^{2}$

51% | Investors that expect meaningful earnings resets over the next 12 to 24 months. $^{3}$

As a result, it will be important to have a clear and compelling value-creation agenda to offset lower profitability and/or valuation multiple compression.

## Investors see the market as too bullish on all market drivers, especially the future impact of AI, US federal policies, and interest rates

![](images/676e83d165564349cc976b8fabd75fcb3ac1699320656b8665ba8907c53c64fb.jpg)

While the expected impact of US tariffs remains broadly negative across macro and corporate indicators, it has moderated

![](images/e01de714e3abd3e68f6be714f45b7d703572ad25f285de5795bf9dbffbeea819.jpg)  
Sources: BCG Investor Perspectives Series, Q2 2026 (June 22–23, 2026, n = 151), Q1 2026 (March 23–27, 2026), and Q3 2025 (September 25–28, 2025).  
Note: Series may not sum to 100 because a small share of respondents reported being unsure of the prospective impact of US tariffs on a given indicator. Any apparent discrepancies in totals or comparisons with prior survey results are due to rounding. $^{1}$ Survey question: How would you rate the impact of the US tariff policy over the next 12 to 24 months? $^{2}$ Net perspective is the share of investors expecting positive impact minus the share of investors expecting negative impact. $^{3}$ Change in net perspective compared with the results from the same question asked in the surveys conducted March 23–27, 2026, and September 25–28, 2025, respectively. $^{4}$ Negative impact on consumer prices means the consumer price index will increase from current levels. $^{5}$ Positive impact on US interest rates means that interest rates will decline from current levels. $^{6}$ Percentage of investors agreeing with this statement: The US stock market has so far underreacted to the likely macroeconomic impact of tariffs.

Exploration-based industries, financial institutions, and tech sectors are seen as macro winners, while consumer sectors are expected to lag

![](images/0b2318e1643b69079a28c488aabc529b012af2932741917ed8a26db075e785c2.jpg)  
Sources: BCG Investor Perspectives Series, Q2 2026 (June 22–23, 2026, n = 151), Q1 2026 (March 23–27, 2026), and Q3 2025 (September 25–28, 2025).

Investors are confident in their understanding of macroeconomic factors.

For example, 79% of survey respondents say that they have a strong grasp of the likely tariff impact on the companies they invest in, compared with 71% in March 2026 and 75% in September 2025. $^{3}$

## Most investors expect AI to have a material impact on fundamentals, but only 25% think AI will create durable competitive advantages

Investors' views on the expected impact of AI

![](images/13ea1a6d8d66983a339d94779c2d67f418caada26458f0367530619c36705bff.jpg)  
Sources: S&P Capital IQ; BCG Investor Perspectives Series, Q2 2026 (June 22–23, 2026, n = 151) and Q1 2026 (March 23–27, 2026).  
$^{1}$ Survey question: When do you expect AI and GenAI to have a materially positive impact on corporate fundamentals and profitability across most industries, excluding technology companies focused on AI? $^{2}$ Changes relative to corresponding time frames in prior survey. Series does not sum to 100% because 2% of investors do not believe there will be an impact on growth or margins. $^{3}$ Survey question: Which of the following best describes your overall view on the likely average impact of AI and GenAI on corporate value creation over the next one to two years?

## AI is expected to positively impact GDP growth, stock market performance, and corporate fundamentals, at the cost of jobs and wages

![](images/1f32075cc37ce3c70d42eac3eb05219f9fae011ac1fb03bae3fcd40e7490118c.jpg)  
Sources: S&P Capital IQ; BCG Investor Perspectives Series, Q2 2026 (June 22–23, 2026, n = 151) and Q1 2026 (March 23–27, 2026).  
Note: Series may not sum to 100 because a small share of respondents reported being unsure. Any apparent discrepancies in totals or comparisons with prior survey results are due to rounding.  
$^{1}$ Survey question: What impact do you expect AI to have in the following areas over the next 24 months in [your region]? $^{2}$ Net perspective is the share of investors expecting positive impact minus the share of investors expecting negative impact.

![](images/7f62afe8a91b702a9653e9bc1be94785aafbd0dd5c6224bd156ea0eaa26df2d2.jpg)  
Investors are actively evaluating AI strategies...  
I analyze and evaluate the AI and GenAI strategies of the companies that I invest in or cover

## About 80% of investors are actively evaluating companies' AI strategies and stress the importance of having a clear AI narrative

June 22–23

...and emphasize the importance of a clear AI narrative, with a majority preferring AI leaders...

...whereas views on companies' AI reporting and valuation impact are mixed but improving

![](images/249f1c57d64fb4491f9177c6fd4c35cd08c3ea539b969b15b7a32d03d62bce18.jpg)  
It is critical for management teams to have a clear and authentic narrative regarding their AI and GenAI strategies

![](images/158d723d245afa30180507077351ee9af7b15d50467309db8d55610121f8c46b.jpg)  
I prefer companies to pursue leadership in AI and GenAI rather than be fast followers

![](images/691a13e791a68db4852e57076a58a40ac42a4b7fd8079e3f6036d103b3467a32.jpg)  
The companies I invest in or cover provide good reporting on their AI and GenAI agendas and their impact

![](images/4a89c4bdf532a660ec07249e3d34eeb04e1f7f15c8db50d03f96da00c174bd5c.jpg)  
The AI strategies, public commitments, and investments of companies are reflected in their market valuations

Investors' responses excluded technology companies focused on AI, including infrastructure and tools

Significant increase

Limited or no change

Significant decrease

![](images/fa67f31b4055388dfbe1181615353e600f0b5facec992c97c5d2ec290047935f.jpg)  
...but many investors view current AI investments as too aggressive

## Many investors view AI investments as too aggressive, but they are increasingly willing to accept margin dilution to build AI capabilities

June 22–23

Investors are concerned about companies' technical and organizational capabilities...

...and are increasingly willing to accept moderate margin dilution to fund AI...

Jun 2026 vs. Mar 2026 (pp)

![](images/479dd9a7dabb7b7830032f97b3b0720a901ada496e1f81ee24c5ef058fcd99be.jpg)

Investors that agree with each statement (%)

![](images/110f8152673e1bc45a56cd32b8d078686417e0ac4e314b9bc188e1f7c3dc5c90.jpg)

![](images/f523076f0ebfdc25f95f1717d05c9d18f48a4194db830a94f2f54b34c74b1d0e.jpg)  
I am concerned about the data and technological capabilities to successfully execute AI  
I am concerned about the people and nontechnical capabilities to deliver AI

![](images/9583469f43af7c8a261701cad8f9a782f58280c8ccf5eea83225f6ba67a3ad67.jpg)  
I am willing to accept a moderate level of margin dilution (1pp to 2pp) temporarily (one to two years)

![](images/778792d4c88ecd59af6050833e4080c8202c2fefe955038201fd12a273b465bd.jpg)  
Investors' views on AI investments (%)  
I am willing to accept a significant level of margin dilution (3pp to 5pp) temporarily (one to two years)

![](images/9b8d92b24f86beaf1f9bd599980c9f3c5ebc1214e7a753fd5e19b4b0cc9c23df.jpg)

Investors' responses excluded technology companies focused on AI, including infrastructure and tools

Significant increase

Limited or no change

Significant decrease

Investors ultimately expect AI to create meaningful value, especially in health care, technology, financial institutions, and industrials

![](images/9516bc04f53b8dfecedfbe746e6b28fa21f9cb2b314f49cd3ead0d0120a6f053.jpg)  
Sources: S&P Capital IQ; BCG Investor Perspectives Series, Q2 2026 (June 22–23, 2026, n = 151) and Q1 2026 (March 23–27, 2026).  
Note: Any apparent discrepancies in sums or comparisons with prior survey results are due to rounding.  
$^{1}$ Survey question: How do you expect the development of AI to affect the financial fundamentals (for example, revenue growth, margins, profitability, and free cash flow generation) of companies across different sectors within the next three years (by year-end 2028)? $^{2}$ Net perspective is the share of investors expecting positive impact minus the share of investors expecting negative impact.

## Changes in investment practices and priorities

Investors that report making the following changes to capital allocation and investing practices or recommendations since the beginning of 2025 $(\%)^{1}$

## Investors are prioritizing structural growth and macro beneficiaries, while being cautious by increasing cash holdings and smaller positions

June 22–23

![](images/adfb4d642f29defb663f707bb8985b921347e06919b69c784bfe5ec22bfd0e02.jpg)

## Long-term organic growth remains the dominant investment consideration, followed by strong returns on capital

Most important company-specific factors driving investment decisions or recommendations

![](images/f055be861cdac19696a0aa01dd5c063062daf0a1d9a82d84f61da95dbeb1bd73.jpg)  
Sources: BCG Investor Perspectives Series, Q2 2026 (June 22–23, 2026, n = 151) and Q1 2026 (March 23–27, 2026).  
Note: FCF = free cash flow; EPS = earnings per share. Any apparent discrepancies in comparisons with prior survey results are due to rounding. The ranking for climate and sustainability factors would likely be very different for sectors where environmental considerations are central to the investment thesis.

## A clear majority of investors want companies to deliver on near-term EPS expectations while making disciplined growth investments

June 22–23

Investors' priorities for financially healthy com

[中间内容因长度限制已省略]

td>15%</td><td>21%</td><td>13%</td><td>12%</td><td>10%</td><td>-2pp</td></tr><tr><td>Portfolio strategy, (re)shaping, and turnover</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>5%</td><td>7% ↑</td><td>1% ↓</td><td>3%</td><td>5%</td><td>5%</td><td>6%</td><td>5%</td><td>5%</td><td>7% ↑</td><td>5%</td><td>2%</td><td>1% ↓</td><td>-1pp</td></tr><tr><td>Management credibility and track record</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>12%</td><td>14% ↑</td><td>7%</td><td>8%</td><td>9%</td><td>8%</td><td>9%</td><td>11%</td><td>8%</td><td>11%</td><td>11%</td><td>3% ↓</td><td>5%</td><td>+2pp</td></tr><tr><td>Management incentives and stock ownership</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>4%</td><td>1%</td><td>2%</td><td>1%</td><td>1%</td><td>1%</td><td>2%</td><td>4%</td><td>5% ↑</td><td>3%</td><td>2%</td><td>0% ↓</td><td>0% ↓</td><td>No change</td></tr><tr><td>Climate and sustainability2</td><td>6%</td><td>6%</td><td>7% ↑</td><td>7% ↑</td><td>3%</td><td>4%</td><td>3%</td><td>6%</td><td>1%</td><td>1%</td><td>2%</td><td>3%</td><td>0% ↓</td><td>2%</td><td>2%</td><td>1%</td><td>1%</td><td>No change</td></tr><tr><td>Climate and carbon footprint</td><td>5%</td><td>5%</td><td>4% ↓</td><td>6% ↑</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>NA</td></tr><tr><td>Other material environmental factors</td><td>1% ↓</td><td>1% ↓</td><td>3% ↑</td><td>1% ↓</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>Not asked</td><td>NA</td></tr><tr><td>Material social factors and stakeholder impact</td><td>5% ↑</td><td>3%</td><td>3%</td><td>2%</td><td>1%</td><td>0% ↓</td><td>0% ↓</td><td>1%</td><td>1%</td><td>0% ↓</td><td>1%</td><td>1%</td><td>1%</td><td>3%</td><td>1%</td><td>1%</td><td>0% ↓</td><td>-1pp</td></tr><tr><td>Corporate governance3</td><td>5% ↑</td><td>5% ↑</td><td>4%</td><td>5% ↑</td><td>3%</td><td>1% ↓</td><td>1% ↓</td><td>1% ↓</td><td>1% ↓</td><td>2%</td><td>2%</td><td>1% ↓</td><td>1% ↓</td><td>4%</td><td>1% ↓</td><td>1% ↓</td><td>1% ↓</td><td>No change</td></tr></table>

↑ Series high ↓ Series low  
Much more important

Less important

Sources: BCG's investor pulse checks, March 2020 through June 2026; n = \~150 for each survey.

No change

Note: The questions on this slide were added to the survey in October 2021. NA = not applicable; EPS = earnings per share.

$^{1}$ This factor was a compelling strategy to win in previous surveys. $^{2}$ This factor was asked as climate and carbon footprint and other material environmental factors. $^{3}$ This factor was best-in-class

## BCG contact information

## If you would like to discuss our findings, please reach out to one of the authors

Jeff Kotzen
kotzen.jeffrey@bcg.com

Greg Rice
rice.gregory@bcg.com

Callan Sainsbury
sainsbury.callan@bcg.com

Hady Farag
farag.hady@bcg.com

Daniel Riff
riff.daniel@advisor.bcg.com

Alexis Colombo
colombo.alexis@bcg.com

Julien Ghesquieres
ghesquieres.julien@bcg.com

The services and materials provided by Boston Consulting Group (BCG) are subject to BCG's Standard Terms (a copy of which is available upon request) or such other agreement as may have been previously executed by BCG. BCG does not provide legal, accounting, or tax advice. The Client is responsible for obtaining independent advice concerning these matters. This advice may affect the guidance given by BCG. Further, BCG has made no undertaking to update these materials after the date hereof, notwithstanding that such information may become outdated or inaccurate.

The materials contained in this presentation are designed for the sole use by the board of directors or senior management of the Client and solely for the limited purposes described in the presentation. The materials shall not be copied or given to any person or entity other than the Client (“Third Party”) without the prior written consent of BCG. These materials serve only as the focus for discussion; they are incomplete without the accompanying oral commentary and may not be relied on as a stand-alone document. Further, Third Parties may not, and it is unreasonable for any Third Party to, rely on these materials for any purpose whatsoever. To the fullest extent permitted by law (and except to the extent otherwise agreed in a signed writing by BCG), BCG shall have no liability whatsoever to any Third Party, and any Third Party hereby waives any rights and claims it may have at any time against BCG with regard to the services, this presentation, or other materials, including the accuracy or completeness thereof. Receipt and review of this document shall be deemed agreement with and consideration for the foregoing.

BCG does not provide fairness opinions or valuations of market transactions, and these materials should not be relied on or construed as such. Further, the financial evaluations, projected market and financial information, and conclusions contained in these materials are based upon standard valuation methodologies, are not definitive forecasts, and are not guaranteed by BCG. BCG has used public and/or confidential data and assumptions provided to BCG by the Client. BCG has not independently verified the data and assumptions used in these analyses. Changes in the underlying data or operating assumptions will clearly impact the analyses and conclusions.
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
