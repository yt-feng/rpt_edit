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
# The Widening AI Value Gap

Build for the Future 2025

By Jessica Apotheker, Vinciane Beauchene, Nicolas de Bellefonds, Patrick Forth, Marc Roman Franke, Michael Grebe, Nina Kataeva, Santeri Kirvelä, Djon Kleine, Romain de Laubier, Vladimir Lukic, Amanda Luther, Mary Martin, Jeff Walters, and Christoph Schweizer

September 2025

## Contents

03 Are You Generating Value from AI?
• Critical Capabilities
• Future-Built Strategies

05 AI Value Generators Are Pulling Away
• The Expanding Value Gap
• Value from the Core
• On Come Agents
• Agents Do Not Work Alone
• Sidebar: AI Maturity Varies by Sector and Region

11 What Value Generators Do Differently
• Pursue a Multiyear Strategic AI Ambition
• Reshape and Invent with Impact
• Adopt an AI-First Operating Model
• Secure and Enable the Necessary Talent
• Use Fit-for-Purpose Technology and Data

17 How to Accelerate AI Value Creation

19 Appendix
• AI Definitions
• Survey Methodology

![](images/745c46e77e1cfb9fa089a9629f4c36907d7a454029a806dcfa8386f8e99406fe.jpg)

# Are You Generating Value from AI?

How much value is your company generating from your investments in AI? It’s a question more CEOs, boards, and investors are asking. More often than not, the answer is not encouraging.

BCG's latest research provides empirical proof that for a small number of companies AI is delivering significant bottom-line value in the form of revenue and cash flow increases and process and workflow improvements. The impact is sufficient to drive shareholder returns. But this typically does not happen. Only $5\%$ of companies in our 2025 study of more than 1,250 firms worldwide are achieving AI value at scale—a measure of how tough the full AI transformation is. Fully $60\%$ of companies are not achieving material value at all, reporting minimal revenue and cost gains despite substantial investment. Another $35\%$ (13 percentage points more than in 2024) are scaling up their efforts and seeing some returns, but many of them admit that they are not moving far enough or fast enough. (See Exhibit 1.)

## Critical Capabilities

The difference is that the top 5% of companies, which we call future-built, have put in place the critical capabilities needed to make AI work at the level of innovation and reinvention as well as to boost efficiencies. Not only are these companies outperforming the competition, but they have also opened a value gap and are pulling further ahead as they reinvest the proceeds from their earlier success in new capabilities, tools, and innovations. Future-built companies are achieving a transformative effect on value creation by catalyzing better decisions and faster and more efficient actions, targeting step changes that go far beyond what is possible from automation and productivity increases.

Much of this value is concentrated in core business functions, such as R&D, sales and marketing, and manufacturing, as well as in IT, where the expected value potential in multiple areas increased substantially over expectations in our 2024 report, Where's the Value in AI? The biggest value comes from client-related functions and IT.

All of this is happening much more rapidly than previous digital disruptions did, and it will continue to do so as AI's functionality improves. Agentic AI, which combines predictive and generative capabilities to reason, learn, and act autonomously, promises to be the biggest accelerator of the widening value gap. Agents, hardly spoken of at all in 2024, already account for $17\%$ of total AI value in 2025 and are expected to reach $29\%$ by 2028.

## Future-Built Strategies

Future-built companies are distinguished by five interlinked strategies that we identified in last year's report, starting with strong leadership and a clear and ambitious vision. They recognize the massive opportunity to drive a top-down multiyear agenda, they define their AI programs with ambitious cost and revenue targets from top management, and they mandate near-term bottom-line improvements while developing new skills, workflows, and technology that will fuel their success for years to come.

Share of companies

Only 5% of Companies Get Substantial Value from AI, While 60% Lag in Developing Critical AI Capabilities  
![](images/3e49a44fecbae9c682024db8c0e70d0fab011471e5b6cb99b80fa607945d8841.jpg)

<table><tr><td colspan="2">Value achieved by future-built2</td></tr><tr><td>1.7x</td><td>Revenue growth</td></tr><tr><td>3.6x</td><td>Three-year TSR3</td></tr><tr><td>2.7x</td><td>Return on invested capital</td></tr><tr><td>1.6x</td><td>EBIT margin</td></tr><tr><td>3.5x</td><td>Patents</td></tr></table>

Source: BCG Build for the Future 2025 Global Study (n = 1,250).  
$^{1}$ This score assesses AI maturity across 41 dimensions.  
$^{2}$ Future-built versus stagnating + emerging.  
$^{3}$ External metrics (Capital IQ): total shareholder return (June 22–May 25 for three-year TSR).

Future-built firms go well beyond automation and incremental productivity improvements to reshape current workflows and invent new ones. They prioritize the latest advances, such as generative AI (GenAI) and agentic AI, to create new revenue streams. Big value comes not from AI pilots or isolated use cases, but from reshaping and reinventing core business workflows end-to-end.

Future-built firms have adopted an AI-first approach and installed and achieved organizational buy-in for an AI-first operating model that combines strong leadership with decentralized execution and shared ownership between business and IT. They are moving toward hybrid workflows based on human–AI collaboration supported by necessary upskilling, governance guardrails, and partnerships. They aggressively source or train the talent they need, now and for the future, especially through broad-based upskilling of current staff (more than 50% of the internal workforce). They also build out a flexible, modular, and interoperable technology stack and a data foundation that leverage central AI platforms, reusable agents, interoperable architectures, and governed access to trusted enterprise data.

The good news for other companies is that the playbook that these future-built firms follow is clearly delineated and available to all. It’s a roadmap that the other 95% can use to build AI maturity and achieve value at scale. But these trailing firms, especially the 60% that have little or no value to show for their investment in AI so far, need to move fast or risk being left in the wake of this latest powerful wave of digital disruption.

![](images/933a311700d4b6f5e205818b91e06d11b1d9b5ff1cc714f6a24373a6bf96c7e8.jpg)

# AI Value Generators Are Pulling Away

The goal of AI, of course, is to create business value. Such value has been elusive until recently, leading to skepticism among executives about the importance of the technology to their companies and among investors about whether the immense investments being made in AI (more than \$250 billion in 2024 alone, according to Stanford University) will pay off by driving higher corporate usage.

But our research indicates that for the best companies, value is achievable and substantial. Future-built companies already generate 1.7 times more revenue growth and 1.6 times higher EBIT margins than the 60% of companies in the categories we term stagnating or emerging. The AI portfolio of initiatives at one large multiformat retailer has produced cost, margin, and revenue impacts of hundreds of millions of dollars over the past five years, adding more than 10% to the company EBITDA today. A company executive told us, “The investor community sees this, as we do, as a strategically important driver of value.”

## The Expanding Value Gap

AI-driven value accrues over time, creating a compounding effect. (See Exhibit 2.) Future-built companies that moved early enjoy outsized benefits across financial and operational fronts, and this performance gap is widening. Future-built firms plan to spend 26% more on IT (representing almost a full percentage point of revenue) and dedicate up to 64% more of their IT budget to AI in 2025. As a result of this investment, they expect twice the revenue increase and 1.4 times greater cost reductions than laggards in the areas where they apply AI.

This creates a cycle that is virtuous for some and vicious for others. In the latter camp are companies that started to experiment but struggled to scale and generate value (the 46% we call emerging) and stagnating companies that have taken little or no action (the remaining 14%). We refer to all of these companies collectively as laggards; about a third admit that they have made no progress. (See “AI Definitions” in the appendix.) As future-built companies reinvest their AI returns in stronger people and additional tech capabilities, they accelerate value creation. Laggards, which lack foundational capabilities and generate almost no value, risk being locked into a vicious cycle of losing ground.

## EXHIBIT 2

Future-Built Companies Create a Virtuous Cycle by Higher Spending on IT and Reinvestment of Gains from AI

![](images/7cc557353cc62bb21240c4e2651b7835f143e4e94f1a681927b0433cc3f239ee.jpg)  
Source: BCG Build for the Future 2025 Global Study (n = 1,250).  
Note: Results reflect the business area respondents know best, not always the full company. Revenue increase and cost reduction are calculated as a percentage of annual revenue through AI efficiency gains in areas where AI is applied.

Our research and client experience finds plenty of reasons for lack of progress. One of the biggest is lack of top management commitment. Among laggards, top management may talk the talk, but it fails to articulate any clear value ambition and doesn't put in place a program to track progress regularly. It delegates AI to people in middle or lower management, who are unsure what to do or are fearful of the technology's future impact on them. Some company leaders move slowly because they worry about adverse impacts, such as poor customer experience. Others are told by operational management that they are already using AI in many places and the value will come if the leaders are patient. Still others experiment too widely, spreading their resources over scores of complex workflows and automating processes here and there, instead of focusing end-to-end on a few important functions or workflows that can generate value and illustrate the benefits of scale. The outcome is often a proliferation of disconnected initiatives that consume resources without generating coordinated value.

In the end, too many companies have approached AI too incrementally, as a way to do more of the same a little faster or better, when the need is for strategic reinvention: What matters to my customers and differentiates my business? How will AI and agents change how I deliver those outcomes? Where do humans still have the biggest impact?

## Value from the Core

Our research has found that 70% of potential value from AI is concentrated in core business functions such as sales and marketing, manufacturing, supply chain, and pricing. R&D and innovation alone account for 15% of the total potential value. This continues a trend that we identified in our 2024 report, which reported that 62% of value came from core business functions.

The big exception is IT, whose share of AI value jumped by 6 percentage points to 13% in 2025. (See Exhibit 3 and the sidebar, “AI Maturity Varies by Sector and Region.”)

# 70% of AI's Value Is Concentrated in Core Businesses

Distribution of AI value potential across functions in 2025 (%)

![](images/096f3d0d4e517637b22dcef8f545dc9323e0ef9b340ec26cc47839396c8f1f49.jpg)  
Source: BCG Build for the Future 2025 Global Study (n = 1,250).  
Note: Customer service is considered a core business function in some industries (e.g., banking, insurance, and real estate) but a support function in others (e.g., consumer products, automotive, and logistics).

AI is already creating tangible value in multiple core business workflows. For example, AI-powered infrastructure monitoring and predictive maintenance helps energy companies reduce costly downtime, driving strong cost-avoidance benefits. Some 45% of these firms have either scaled or fully deployed this workflow, leading to avoidance of 30% of addressable costs when fully deployed.
(See Exhibit 4.)

GenAI helps these and other firms leverage predictive AI in the service of wider adoption by facilitating nontechnical communication and engagement. Future-built companies, which put predictive AI on their CEO agendas as early as 2021, are now much faster than others at enabling broad adoption.

## On Come Agents

The emergence of agentic AI in the past 12 months represents a critical development in making AI more relevant to businesses. Agentic AI combines predictive AI and GenAI in core business workflows across the entire value chain. The workflows can be simple, such as performing reconciliation in the procurement function, but companies can also integrate multiple agents into more complex workflows, such as supply chain management or consolidated supply and demand workflows in call center rostering.

The most successful examples involve embedding agents across entire workflows rather than running them as isolated pilots. In this sense, AI agents can be thought of as digital workers. They perform alongside or under the supervision of human workers to digest large volumes of data, perform logic and reasoning functions, make decisions, and act. Internal feedback loops enable them to learn and improve outcomes.

# AI Maturity Varies by Sector and Region

AI maturity, which we define as the ability to create value at scale, varies by sector. Maturity has advanced across most industries—but not evenly. New front-runners have emerged, legacy sectors continue to struggle, and sharp contrasts are visible in both capability adoption and workforce readiness. And though maturity varies across sectors, companies in each one have made cutting-edge progress.

Software, telecommunications, and payments and fintech lead the maturity race in 2025, showing strong year-over-year development and boosting their positions on our index by 13 points, 11 points, and 7 points, respectively. Fashion and luxury, chemicals, and real estate and construction remain at the lower end of the AI maturity curve.

In sectors such as airlines and telecommunications, AI's contribution to value in core functions pushes 80% (up 15 percentage points (pp) and 8 pp, respectively, from 2024). Chemicals, oil and gas, and machinery and automation show the highest shift toward AI use in core functions, with increases of 14 to 19 pp.

There are big disparities in access to AI tools. In relatively immature sectors, less than 50% of employees have access to GenAI tools such as Copilot and ChatGPT. In relatively mature sectors, more than 70% of staff have access. We found disparities in training as well. Software companies plan to upskill 55% of their staff in the coming year while chemicals and machinery and automation firms plan to train less than 15%. Although access to tools and training is insufficient by itself to drive meaningful value, it is a strong indicator of whether a company or sector takes AI seriously.

Regional differences are subtle. North America tends to be slightly ahead on most adoption metrics. Asia-Pacific follows, with Europe somewhat farther behind, though all regions have a mix of future-built and lagging companies.

Asia-Pacific companies allocate the highest share of their IT budget to AI (5.2% versus 4.6% in Europe and 4.4% in North America), and these companies are reporting slightly higher value. Looking ahead to 2028, Asia-Pacific expects a revenue increase of 10% (versus 7% for Europe and 8% for North America) and cost reduction of 12% (versus 10% for others).

Agentic AI adoption varies, too: 51% of firms in North America are experimenting with or deploying agents versus 45% in Asia-Pacific and 41% in Europe. Interestingly, Asia-Pacific allocates the largest share of AI budget to agentic development (32% versus 29% in North America and 22% in Europe).

![](images/d04e9ba1406651c01022a5d8dab7b484ed3c8db281a4e70ce3e0c382149bec03.jpg)

No Matter the Industry, Scaled Workflows in the Core Business Are Already Creating Value  
![](images/0ecb75abb74a734d7ed5b2c5a79fe78b3c117f3dc6028ac6c9d03e2e85e607b9.jpg)  
Source: BCG Build for the Future 2025 Global Study (n = \~900 for workflows).  
$^{1}$ Estimate based on the predominant AI type in each workflow, even if there is always some of the other.  
$^{2}$ Scaled or fully deployed stage of adoption for the workflow.

Companies should view agentic AI as the next step in AI implementation, not as the starting point. The prerequisites for agents include strong data foundations, scaled AI capabilities, and clear governance. The best way to deploy agents is through a few high-value workflows with clear implementation plans and workforce training, rather than in a massive rollout of agents everywhere at once.

For example, a global beauty products company implemented a step change in its sales and marketing as it sought to address multiple issues with customers' online experience. These problem areas included highly fragmented sources of information, a lack of personalized guidance, and an inability to access important product information before making a purchase decision. The company's solution was to introduce the industry's first large-scale virtual beauty assistant, integrated into the company's websites and e-commerce journeys extending across more than 20 markets and covering eight brands.

The automated assistant combines AI-powered consultation with real-time personalization, supported by a unified data and cloud platform. The virtual assistant was deployed in less than 12 months, and the company expects to gain \$100 million in incremental revenue from the initiative—doubling the ROI of traditional e-commerce customer pathways, and enabling a new model of always-on, personalized customer engagement.

A leading electronic device manufacturer sought to integrate GenAI across infrastructure, manufacturing, and frontline operations. Its previous digital efforts were fragmented; it needed central orchestration, governance, and a technician-focused transformation. The answer lay in assembling and stocking a “company store” of centralized agentic AI solutions to govern, scale, and monitor AI use cases across the manufacturer’s more than 200 factories. Companies can use core agents repeatedly, accelerating deployment of new workflows and supporting 80%

automation in complex operational workflows such as defects diagnos

[中间内容因长度限制已省略]

 for the Future 2025 Global Study (n = 1,250). Note: B = billion. $^{1}$ Europe includes data points from Africa and South America.

![](images/d13f0612463f20b855f8f1fe8fa4f53f72f24c1c24df6d75afcba18b439249f4.jpg)  
Profile of respondents (%)

![](images/651d69ff7db7842f84313c8f4b3862c81f401e762d07c672ef5b3f2bf89c1cd3.jpg)

![](images/3207a6fc642f0fff7f4762def6c94b5edbdfb25b695f2c218f28e1795095c9c3.jpg)

## About the Authors

![](images/4685517a72957fa4b545e11c907aa52c9bbfb2dbbbf98397f32b4fd950a0b986.jpg)

Jessica Apotheker is a managing director and senior partner in the Paris office of Boston Consulting Group, and the global CMO for BCG and BCG X. You may contact her by email at apotheker.jessica@bcg.com.

![](images/8099d2b57baee2e377ea5c528cfb31d8826de49ea5dd816a25072bb3ae7cae32.jpg)

Nicolas de Bellefonds is a managing director and senior partner in BCG's Paris office. You may contact him by email at debellefonds.nicolas@bcg.com.

![](images/f43992f8f55aa6bd201a99dd5de4441f0f8fe89749a1e6ec1df16951ca83cb7f.jpg)

Marc Roman Franke is a partner and associate director, AI and digital transformation, in BCG's Berlin office. You may contact him by email at franke.marcroman@bcg.com.

![](images/895a6453da35793f928d144581ead859d8a875d7d837ff81e3138f501655be22.jpg)

Nina Kataeva is a managing director and partner in BCG's Zurich office. You may contact her by email at kataeva.nina@bcg.com.

![](images/1e5724dbabf7eb8b304e911c98693323a1f4b0a8e37534d2951b4a47f7435329.jpg)

Vinciane Beauchene is a managing director and partner in the firm's Paris office. You may contact her by email at beauchene.vinciane@bcg.com.

![](images/0f31e674ea84f80f2aec3c4292034aecca57631b1bb75f94998fa39645f1f1e3.jpg)

Patrick Forth is a senior advisor and senior partner emeritus in the firm's Sydney office. You may contact him by email at forth.patrick@advisor.bcg.com.

![](images/82c271152506ca8a1f82554611203c9956ae3a24e969f7b25be2c00a1b543e6d.jpg)

Michael Grebe is a managing director and senior partner in the firm's Munich office. You may contact him by email at grebe.michael@bcg.com.

![](images/77da002fb77e764451578aa3b5dd26fea587691c59c9eecc45f861161a08e29c.jpg)

Santeri Kirvelä is a managing director and senior partner in the firm's Helsinki office. You may contact him by email at kirvela.santeri@bcg.com.

![](images/e77aebe0ed0a4e937ed9ec1c34abd4196548208efa512a84ea6348734a1cb300.jpg)

Djon Kleine is a managing director and partner in BCG's Los Angeles office. You may contact him by email at kleine.djon@bcg.com.

![](images/c9312a545d35bbdcb1c1d415c0ffbd033060de170a90299233e3125f48f41c5a.jpg)

Vladimir Lukic is a managing director and senior partner in BCG's Boston office and is the global leader of the firm's Tech and Digital Advantage practice. You may contact him by email at lukic.vladimir@bcg.com.

![](images/c1829b4980b99a08e4476eeb7488ade23ce066edc17991c1cf688a2deca57a15.jpg)

Mary Martin is a managing director and senior partner in BCG's Denver office. You may contact her by email at martin.mary@bcg.com.

![](images/d4a4ffbd4d349348e58dd99fc20206104241d77c285b8145f147651f3967f044.jpg)

Christoph Schweizer is CEO of Boston Consulting Group.

## For Further Contact

If you would like to discuss this report, please contact the authors.

![](images/66078d57b6f802d07ab4759e4bcfb7c3becbc947ea57ddc1c7755e176c6e8432.jpg)

Romain de Laubier is a managing director and senior partner in the firm's Singapore office. You may contact him by email at delaubier.romain@bcg.com.

![](images/0cac2ff57fe5eedf24787ab347157b4825cbdd16e8fda7c8dc8f9f16fce53501.jpg)

Amanda Luther is a managing director and senior partner in the firm's Austin office. You may contact her by email at luther.amanda@bcg.com.

![](images/d9a510722a1238a50ec1bc92bf233726951909054ce81c9912d66b506e2685a7.jpg)

Jeff Walters is a managing director and senior partner in the firm's Hong Kong office. You may contact him by email at walters.jeff@bcg.com.

## Acknowledgments

The authors extend their gratitude to everyone who contributed to the research and development of this report, including Charles Adamo, Florence Adida, Julie Bedard, Giuseppe Colombo, Maunoir de Kerros, Cyprien d'Harcourt, Anna Dorkel, Camille Duranton, Eva Engelhardt, Caroline Girard, Rim Hachani, Matthew Kropp, Nikolaus Lang, Michael Leyh, Deborah Lovich, Clemens Nopp, Lucas Quarta, Clémentine Remy, Lee Robertson, and Jürgen Rogg.

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X (formerly Twitter).

![](images/1d7bfc57d3a1e9ad701ad9cbe653c75cfee078efb6aa3451e45868acc2c36836.jpg)

BCG
"""
