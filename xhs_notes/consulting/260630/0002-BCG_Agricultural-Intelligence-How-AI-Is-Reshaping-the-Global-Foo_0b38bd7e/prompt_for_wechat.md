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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
BCG

![](images/59c03cc52eaf71e64628758167d6f2de4093d17de6508dc41c47c66e959e304d.jpg)

AGRIBUSINESS INDUSTRY

# Agricultural Intelligence: How AI Is Reshaping the Global Food System

By David Potere, Sonya Hoo, Michael Glotter, Emily Wu, and Adam Haidermota

ARTICLE JUNE 25, 2026 12 MIN READ

In September 1898, Sir William Crookes, president of the British Association for the Advancement of Science, delivered a warning for civilization: the world’s supply of usable nitrogen, the element underpinning all plant growth, was finite. Within a generation, he maintained, food production would hit a ceiling; after that, its decline would be simple arithmetic. His appeal was direct: unless chemistry could produce nitrogen from the atmosphere itself, mass starvation would follow.

Eleven years later, Fritz Haber found the answer, and Carl Bosch industrialized it. For the first time, agriculture was no longer bound by the natural nitrogen cycle.

But removing a hard constraint is not the same as solving the problem. What followed was a cascade of innovation: new seed genetics that could exploit large-scale artificial crop nutrition, generating yield potential previously out of reach; mechanization that opened up production across vast new acreage; and agronomy that reorganized itself around a fundamentally different input base. Each layer reinforced the others. Together, they reshaped how food was grown, traded, and consumed across the planet. Roughly half the nitrogen in human bodies now traces back to that moment.

Today, the global agrifood system feeds more than 8.2 billion people, five times the population when Crookes issued his warning. Despite the enormous gains made over the past 125 years, the industry currently faces three threats to the agrifood system: climate volatility, geopolitical realignment, and regulatory shifts.

A fourth force is now gaining momentum: AI across every stage of the agrifood system. Its timing is critical. We call it agricultural intelligence, and it will likely further revolutionize how our food is researched, grown, distributed, and sold.

This article examines the potential transformative power of agentic AI across the agricultural value chain: its expected impact on researchers, farmers, seed and input companies, traders, distributors, and retailers. How each of these players manages through the transformation will determine just how beneficial its impact is and which ones will be the new winners and losers in the agrifood system of the future.

## Three Threats

The global agrifood system is under pressure from three increasingly powerful threats. (See Exhibit 1.) The first is climate-related volatility, which is making three of the foundational inputs of agriculture—precipitation, temperature, and seasonal variability—measurably less predictable. These key inputs have become a source of systemic risk rather than a reliable given, requiring far greater precision in monitoring and reacting to changes in growing patterns.

Three of Four Structural Drivers Are Reshaping the Global Agrifood System, and One—Agricultural Intelligence—Offers a Response

## Climate volatility

![](images/1c4c89e935be705a26a8b755a9ca93510917c936363af2c2a1c9472e846e561a.jpg)

## Regulatory paradigm shift

## Agricultural intelligence

## Geopolitical realignment

Source: BCG analysis.

The second is geopolitical realignment and disruption, which has made supply chain shock a permanent feature of commodity markets. The restructuring of US-China tariffs has compounded instability for a decade; the war in Ukraine redrew the wheat map overnight; and the closing of the Strait of Hormuz is affecting the supply of fertilizer in the middle of the northern hemisphere's planting season. Now, whichever company reads such signals earliest and hedges their exposure most precisely stands to gain an advantage.

The third threat is a major regulatory paradigm shift. The European Union's deforestation rules, Scope 3 carbon reporting, and carbon market protocols (coupled with shifting consumer demand for transparency, verified sustainability, and provenance) are mandating a data infrastructure that the agriculture industry has never had at scale. Increasingly, food companies must be able to determine, precisely and verifiably, where every input was grown, under what conditions, and using what practices.

This is where agricultural intelligence comes in, both as a counter to these threats and as a transformation of how the business of agriculture is carried out, from research into new types of crops to the retailing of the industry's final products.

# The Role of Agricultural Intelligence

Agricultural intelligence uses agentic AI to sequence decisions and act autonomously, with minimal human handoff at each step. Going beyond the precision agriculture of the past two decades, it acts on behalf of humans in the field, at the trading desk, and in the breeding lab. In doing so, it erodes the information asymmetries and expertise premiums that have underpinned margins across the food system for generations. Wherever human expertise, skilled labor, or proprietary information has historically been the source of competitive advantage, companies will have to find new sources of outperformance. (See Exhibit 2.)

## EXHIBIT 2

Agricultural Intelligence Is Shifting Competitive Advantage Across the Value Chain

![](images/c18dff6775434cf97524c35bbf2e963035e8846f091473c0b38c4137cb41d992.jpg)  
Source: BCG analysis.
Note: IP = intellectual property; CPG = consumer packaged goods.

What is compressing most quickly is the advice premium: AI tools now deliver field-specific recommendations that rival the best crop scientists, making the advice available to any grower with a smartphone and a basic subscription to an AI tool. How agricultural intelligence transforms the industry depends on each player's position across the value chain.

\- The Producers. Farmers and ranchers are the origin point of the data, labor, and production on which every other player depends, putting them squarely at the center of the transition. Growers are both the most exposed to climate volatility and the most surveilled by new sensing infrastructure, making the deployment of agentic AI on farms and ranches especially valuable. And many are small and medium-sized business owners with direct access to frontier AI tools, making them increasingly capable of understanding what their data is worth and acting on that understanding.

\- The Agriculture Input Companies. Depending for their profits on proprietary intellectual property and agronomic advice, these players accumulated expertise about which chemistry or seed performs best in which soil type, rotation, and season. The patent-protected

molecule is likely to survive, though agricultural intelligence is opening even this frontier to new challengers in trait discovery and R&D.

\- The Agriculture Retailers and Cooperatives. These organizations built their businesses on relationship-based input sales and a patchwork of custom application services. Currently, farmers typically buy field scouting services from one provider, fertilizer and crop-protection inputs from another, and seed advice from a third. This fragmented model is now under pressure from two directions. First, agentic purchasing systems are expected to seek competitive prices transparently across suppliers, compressing the wholesale-to-retail margin. Second, the potential is emerging for the development of integrated, whole-season intelligence that bundles the sensing, deciding, and acting dimensions for a single field into one closed intelligence loop. The company that assembles that loop first, rather than sells the pieces separately, can redefine the value proposition.

\- The Equipment Manufacturers. These companies sit closer to the physical act of farming than almost any other player aside from the growers themselves. The rich operational data generated through their machines (every pass, every yield map, and every application record) is a genuine and defensible asset. The structural risk for them lies in the likelihood that the switching cost that has anchored their business models migrates from their hardware to AI-powered software as crop insights become increasingly independent of which brand of iron is responsible.

\- The Originators and Trading Houses. More than any other segment, these companies have thrived on information asymmetry, leveraging their physical and logistical capabilities to buy and sell commodity crops as they move farm production down the supply chain. They have a local edge in knowing which farmer has grain in the bin and how much and a global edge through visibility into supply and demand flows that few other players can match. But that premium is compressing as real-time market data, AI-generated analysis, and satellite monitoring reach deeper into the system. The sharpest players are using AI to move up the intelligence stack.

\- The Food Companies and Retailers. At the consumer-facing end, food processors, consumer packaged goods (CPG) companies, and retailers have historically gained an advantage through demand-signal asymmetry: knowing what consumers want before upstream players could see it. That advantage is compressing as agricultural intelligence gives every layer of the value chain better forecasting, more granular supply chain visibility, and new tools for verifying food safety and provenance. In addition, AI-accelerated alternative protein development and precision fermentation could, over time, reshape the raw material economics on which commodity processing businesses depend.

## Intelligent Actors

Agricultural intelligence is not a single technology, and treating it as one is a costly mistake. The four distinct dimensions of agricultural intelligence—sensing, deciding, acting, and creating—provide a map of what these systems do simultaneously, not a hierarchy to climb.

\- Creating is the long bet and the dimension that most closely mirrors what Haber and Bosch achieved. GenAI models working on genomic and scientific literature data are beginning to design new traits, new molecules, and new biologicals at machine speed. Instead of optimizing for current constraints, these models are redesigning the inputs themselves.

Bayer's Icafolin herbicide, submitted for registration in major markets in 2025, is the company's first crop-protection product to be developed under their CropKey approach. The technology uses AI and data science to design candidate molecules against defined targets, rather than screening thousands of compounds.

\- Sensing turns the physical world into data. Tractors, sprayers, and combine harvesters generate a continuous stream of operational data. Combined with data from satellites, drones, Internet of Things sensors, and computer vision technology, this data converts field conditions into labeled signals that can be queried at costs inconceivable a decade ago. For most agribusinesses, sensing is the lowest-risk entry point and the data foundation on which every other dimension depends.

InnerPlant's InnerSoy soybean varieties illustrate where sensing is heading: the soybean itself emits an optical stress signal that InnerPlant's CropVoice system reads and translates into real-time farmer alerts, turning the plant itself into the sensor.

\- Deciding turns data into the right recommendation at the right moment. In markets where expert advice has been unavailable, it creates access to expertise that never existed before.

FarmerChat, already deployed in Africa, India, and Brazil, has reached more than 830,000 farmers and answered over 5 million queries, delivering agronomic guidance previously requiring a trained extension worker and bringing the cost down from \$35 per interaction to just 35 cents.

\- Acting closes the loop between recommendation and execution, translating decisions into automated, site-specific actions without the need for a human handoff at each step.

John Deere's See & Spray uses computer vision to distinguish crops from weeds at speeds of up to 15 mph, reducing chemical use by half, on average. No longer a pilot, the system covered 5 million acres in North America in 2025, up from just 1 million in 2024.

These four dimensions interact as a network. The data infrastructure that makes sensing so powerful can sharpen deciding. The quality of the deciding process enables acting. And the data generated by acting augments sensing while feeding the creating dimension. Companies

investing in any one dimension currently are building a compounding advantage that competitors starting later may not be able to shortcut.

# The Questions Your Leadership Team Should Be Asking

Every major player in the agrifood value chain (whether an input company, equipment manufacturer, agriculture retailer, processor, CPG company, or food retailer) needs to understand that the following questions are not hypothetical. They are critical to your future competitive advantage and business success.

Strategy. What part of your business model was built on something your organization knew that your counterparties did not? Name it precisely: not “relationships” or “scale,” but rather the specific informational or expertise advantage that has allowed you to maintain and grow your margins. Then answer honestly what happens to it as AI democratizes the knowledge layer, climate volatility erodes historical patterns, and geopolitical disruption punishes the slowest to build alternatives. Does your organization have the strategic will to build something truly new before someone else does?

Data. Have you solved the farmer data problem, or are you assuming someone else will? Current systems are fragmented and subscale (aside from a few exceptions), and a solid, whole-farm perspective is needed. In part, it is a trust problem, not a data problem. And it is getting harder to address: farmers are already gaining direct access to frontier AI tools and increasingly capable of getting direct, personalized value from their own data themselves, with no external platform needed. The organizations closest to the farmer may be best positioned to win the infrastructure race of the next decade, but only if they move quickly.

Operations. Are you treating agricultural intelligence as a nice feature or restructuring your core operations around it? Is there anyone at your company who can see clearly what this moment means for your company? Are you willing to make the moves required to stay ahead of all these developments and make your organization essential in the farm system of the future, before the restructuring happens to you rather than with you?

The application of AI to the global agriculture value chain is likely to be rapid and transformative. Big gains in input innovation, data capture and analysis, decision making, and operations on the farm and in the marketplace can restructure not only how our food is grown but what kinds of food we eat.

Producers, input providers, machinery makers, traders, food companies, and retailers can all gain by adopting these new AI-driven capabilities. But the advantage will go to those who move first.

Agriculture's new nitrogen-moment window is open. It will not stay that way.

## Authors

![](images/1a72b485aab0fe17f98bac6f24dbaeaf8cd1cc05ffb0d51fdbae5e31a19d291b.jpg)  
David Potere

![](images/2adc2b92d495aa6a89f4f34e47e14983cc10249c5fed29f6e94ebb870e4dbc64.jpg)

![](images/b04374a6ca47a05b3dcd7ea251b676c1ce2674ff275982e08d90764faafc1324.jpg)  
Managing Director & Partner
Boston

![](images/99be727037f3c4ba3d0121a151fdd87bf0e2fc5d2b4a4f481f8e212852707739.jpg)  
Sonya Hoo  
Managing Director & Partner
Washington, DC

![](images/8b40930e91abae6cb10d5d953c1bab32ab0679584a924fef164386398fa43b94.jpg)

![](images/411857180281b2c623dff7bfc2104c57353afd01d7ea9454500baf47ec373bf0.jpg)

## Michael Glotter

![](images/2a44425d44d810bf4e178f42846181cd4cad16e8a1f7db4da11b3328f6242b5a.jpg)

Managing Director & Partner
Chicago

![](images/d15ae9443e9b2fafc00b039a5b9aaee2afc805d6b4d3bdfca1acdb2652537dd9.jpg)  
Emily Wu

Principal Auckland

![](images/65cd44da8efc8b5afd2c196738d7727733c83e6b4d61de60e701bb49d69aea59.jpg)  
Adam Haidermota

![](images/96c8844e3dc25dd338e740155688644faaa4f91d1173573ca2ea104bd2f6456c.jpg)

Senior Analyst, BCG Vantage Chicago

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
