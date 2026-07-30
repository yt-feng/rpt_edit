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
![](images/8a2edcf7b8727806196ea5d9b670fa152950e18c64d0784911b4919e8e69e59b.jpg)

BIOPHARMA

# Biopharma Carve-Outs Are Tricky. Here's How to Get Them Right.

By Hob Brooks, Ben Aylor, Megan DeFauw, Chrissy O'Brien, and André Kronimus

ARTICLE FEBRUARY 28, 2022

## “Through carve-outs, companies can create value, streamline portfolios, and reduce complexity. But the ultimate success of a deal hinges on focused, proactive execution.

As the health care environment evolves at an accelerating rate, biopharma companies increasingly respond through carve-outs. By reshaping their portfolios, firms can focus on fast-growing business units and unlock value from assets that add unnecessary complexity or might perform better with a different owner. Yet these transactions won’t achieve their full potential unless companies take the right approach to deal execution. Carve-outs are more challenging in biopharma than in other industries, leading to greater value creation for businesses that execute deals well—and greater risks of destroying value for those that don’t.

From our experience helping biopharma leadership teams execute large-scale carve-outs, we’ve learned that companies can proactively manage the complexity of these deals by keeping a laser focus on strategy from the outset and following a few clear supporting principles. In doing so, biopharma players can avoid unexpected one-time costs and ongoing entanglements—getting to the finish line faster. This is a more deliberate and thoughtful approach but yields superior value in the long run.

## Deal Execution Is Where Value Is Gained—or Lost

Across industries, carve-outs are on the rise. From July 2020 through June 2021, the quarterly average deal value was \$309 billion, 25% higher than the five-year average (\$247 billion per quarter). There is a clear logic behind this trend: carve-outs create value. From 2003 through mid-2021, returns for the Bloomberg Spin-Off Index more than doubled those of the S&P 500. Yet performance varies widely between the winners and losers. Only about 50% of deals create value in the medium term, and poor performers can lose significant value, producing total shareholder return that’s more than 100 percentage points below the leaders. (See Exhibit 1.)

## Exhibit 1 - Carve-Outs Offer Significant Value, but Performance Varies Widely

![](images/9a7d652c4e563f7fd3189b9d36287bd27a91366d398671eb7858f3a996d46ae8.jpg)  
Sources: S&P Capital IQ; Refinitiv Datastream; BCG analysis.

![](images/66ec3f863b37928fd11774575d230ae6e0299a26349753114b92ec71890e3823.jpg)  
Note: The Bloomberg Spin-Off Index tracks US spinoffs for the first three years of their independent operation. For the TSR chart, N = 195 spinoffs completed from 2010 through 2020. TSR = total shareholder return; p.p. = percentage points.

Often, the differentiating factor is deal execution. No matter how strategically sound a carve-out may seem on paper, if it is not executed in a thoughtful, deliberate way—considering and planning for all contingencies—it will likely fall short of expectations.

The carve-out trend in biopharma is just as strong as it is in other industries. Activity in 2020 was artificially low because of the pandemic, but 2019 was an all-time high, with \$44 billion in deal value, including four carve-outs of more than \$5 billion. (See Exhibit 2.) All signs suggest that divestitures will resume as the business environment slowly returns to normal. Strong valuations, the continued impacts from loss of exclusivity, and pricing pressures are together spurring an increase in carve-outs, as biopharma companies reshape their portfolios to better meet the needs of the market and create value for shareholders.

## Exhibit 2 - Biopharma Divestitures Reached an All-Time High in 2019

![](images/651b153d2c4e39b43622fcac6f2772d9ea1dfb9fd9021429539bdaa4a148d882.jpg)  
Sources: S&P Capital IQ; company reports; BCG analysis.  
Note: Includes both spinoffs and corporate divestitures; deals with unknown values not counted; numbers rounded.

# Why Biopharma Deals Are More Complex

The challenge is that executing carve-outs in biopharma is not easy, for several reasons.

Global Footprints with Local Operations. Most biopharma companies are multinational firms, yet they require highly localized operations because of the complex licensing required to import, distribute, and sell pharmaceuticals in different markets around the world. Any carve-out strategy must first define a local commercial strategy for each region (aligned to the overall global strategy) and then disentangle the local operations in every impacted market. This can result in dozens of local workstreams to separate the businesses.

Complex and Ever-Changing Regulations. Health care faces far stricter regulatory oversight than many other industries, and most biopharma carve-outs trigger thousands of regulatory implications, from manufacturing-site name changes to marketing-authorization transfers, many of which have potential supply implications. For a business being sold off, every product requires dozens—if not hundreds—of changes to marketing authorizations and artwork in each market where the products are sold. Executing these modifications while maintaining continuous supply is incredibly challenging and often takes several years to complete. During this time, the parent company and carve-out business remain entangled and rely upon one another’s compliance resources.

Integrated Supply Chains. Most multinational biopharma firms are exceedingly efficient in their operations, through tightly integrated global supply chains. Products for the carve-out business will likely be commingled with the parent company's products across the supply chain, including manufacturing sites, distribution centers, and third-party suppliers or contract manufacturing organizations (CMOs). The carve-out process needs to separate those production streams and consider the tax, legal, and regulatory implications of each decision.

Combined IT Systems. Like manufacturing processes, biopharma IT systems are validated and audited by regulators around the world. Separating the systems and data that the carve-out will need to operate—and ensuring that each system is not only operational but approved by all relevant health authorities—takes time and will almost certainly require transitional service agreements (TSAs) after the deal closes, to ensure business continuity.

Patient-Critical Products. Biopharma companies sell medically necessary products that carry life-and-death implications for patients. Unlike in other industries—where production errors or out-of-stock items may be a minor annoyance for customers—business continuity is mandatory in health care.

# Key Areas to Get Right During Execution

Mitigating the complexities requires significant forethought and planning. In our work helping biopharma companies execute large and successful carve-outs, we have identified five core areas for management teams to prioritize during the execution phase (corresponding to the five challenges discussed in the previous section).

Mitigating the complexities of biopharma carve-outs requires significant forethought and planning.

Structure governance to address global and local considerations. It’s essential to set up an agile governance model—a global, centralized workstream to oversee all local separation activities and coordinate the work of lawyers and other advisors. In this way, companies can ensure that separation activities are conducted consistently around the world.

Build a program to address regulatory and supply implications. At an early stage of the program, management teams need to assess the regulatory consequences of a carve-out; doing so can dramatically reduce the timeline as well as the costs incurred from inventory buildups and write-offs. This workstream is highly technical, inherently cross-functional, and very dynamic given that the regulatory environment and supply requirements evolve over the course of the divestiture process.

Develop a clear upfront strategy to disentangle supply chains. Decisions made early in the program about the acceptable level of supply chain entanglement at close can have a material impact on the timeline, tax implications, and overall cost of the carve-out process. Carefully designing long-term supply agreements between the two entities can mitigate some—though not all—challenges of commingled supply chains.

Engage the business early in separating IT systems. A robust and strategic inventory of IT systems—and the options for dividing them—is essential at the outset of a carve-out program. This needs to be a collaboration between the IT experts and business owners for all key systems. For example, some carve-out programs entail developing systems for highly complex, critical technology. That approach improves information flow and data security once the parent company and divested business begin to operate independently and provides additional time to stand up the long-term IT solutions for the unit being sold or spun off.

Prioritize the continuity of supply for medically necessary products. Because biopharma products are so critical to patients, carve-out programs need to factor in all potential effects on supply. Companies must coordinate cross-functional governance—including regulatory, supply chain, and commercial considerations—to ensure that the project plans will enable continuous supply throughout the carve-out timeline. Activities and workstreams related to separating the business need to be isolated from the activities and workstreams required to run the business—though any separation activity with potential supply implications must be clearly identified and flagged to the business owner well in advance.

Carve-outs are a highly attractive means for biopharma companies to create value, streamline portfolios, and reduce complexity. But merely deciding to conduct a deal is not enough; the ultimate success of a deal hinges on its execution. By understanding the challenges in advance and thinking through the potential ramifications of key decisions, management teams can make sure that they get to the close on time and with a clear plan to capture all possible value.

## Authors

![](images/21671a928e85df2d0128bcb91034efa3151c075655408c78def5a3bc64adbba3.jpg)

![](images/4f13d06ffd36d764a60b5814126decc3030b01bbc7bea397c5dc657069b97cec.jpg)

![](images/59cdd37fcfb15bc084fbd1843655f19130b99e0090ecb80c8a8177735aeb1907.jpg)  
Hob Brooks  
Alumnus

![](images/2eb099f3449e2665f67d99f61fec82c7af706d4933db327aa2f8a398dd38a09d.jpg)  
Ben Aylor  
Alumnus  
Megan DeFauw

Managing Director & Partner Dallas

![](images/e50e50f8d6b7dbefaeda1a2b7d8df328c922223af6450505750032c3f04d97f4.jpg)

## André Kronimus

Managing Director & Senior Partner
Frankfurt

![](images/30e477d5c9f40fd71b9acfa6fe493aaa86cee6e52b31b18501997a0b7f582ec2.jpg)

![](images/ada7aa7f16e9df66e3ab88fcf564afc794b96adbe46940960f8bf2ccdfc4e204.jpg)

## Chrissy O'Brien

![](images/ef92af334b1cc6c9805a079f3e77097c84493b72dc373c1a3bb685ec426db40a.jpg)  
Managing Director & Senior Partner
Boston

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

## © Boston Consulting Group 2025. All rights reserved.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and X (formerly Twitter).
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
