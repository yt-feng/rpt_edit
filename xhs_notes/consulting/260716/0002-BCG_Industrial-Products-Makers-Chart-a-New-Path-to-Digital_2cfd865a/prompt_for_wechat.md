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
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
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
# INDUSTRIAL PRODUCTS MAKERS CHART A NEW PATH TO DIGITAL

By Michael Füllemann, Michael Dahle, Francisco Salmerón, and Verena Rossbach

INDUSTRIAL PRODUCTS COMPANIES' initial forays into digital services didn't go exactly as planned. Many had high expectations that expanding into digital would help them expand services, the most profitable part of their business, and lead to new sources of revenue, leaner field operations, and more targeted sales. But making digital happen was harder than they anticipated. Companies quickly realized that they lacked the foundational digital platforms and systems on which to build other applications in a scalable, competitive way, whether those applications were for new services, a more efficient way to manage their operations, or deeper insight into pricing and selling of services.

The realization led industrial products makers to rebalance their efforts to focus on establishing the core data platforms and systems that serve as the underpinnings of other digital services. The adjustment they made is clear from BCG's ongoing benchmarking survey of industrial products makers' digital services strategies. In 2016,

these “enabler” technologies had yet to appear on anyone’s radar. In 2020, they account for four of the participating companies’ top ten priorities.

Among the latest benchmarking company group, enabler technologies remain relatively immature. At many companies, projects are still in the pilot phase. To get the most out of their efforts, companies must work on a limited number of scalable pilots at a time, and prioritize those with the clearest potential to make or save money before moving on to the next opportunities.

## Why Initial Digital Services Didn't Take Off

BCG began benchmarking industrial products companies in order to understand their use of digitization to improve performance and efficiency. The benchmark group includes dozens of companies and business units of larger corporations, all of which manufacture heavy industrial equipment or the components that go into it. Whether they are standalone companies or business units of larger entities, all of them have a global presence, with an average annual revenue of about \$3 billion.

Digitization allows these companies to do three things: create revenue streams from new services and business models, sell more of their existing services, and make operations more efficient. In 2016, when BCG first polled benchmark companies, using digital to launch new services accounted for three of the top four use cases and four of the top ten. (See Exhibit 1.)

Initially, companies believed that predictive maintenance and remote monitoring and diagnostics for field service technicians would be the cases most relevant to their business. Predictive maintenance is a natural first pick because if industrial products suppliers know when equipment needs to be serviced, they can fix it before it breaks and avoid the costs associated with equipment downtime and last-minute repairs.

Remote monitoring and diagnostics for field service technicians is also an attractive initial use of digital because of the nature of the business. Many industrial goods makers have large contingents of technicians who work on customer equipment. If companies can remotely monitor how equipment is running, they can gather the data they need to identify problems in real time and dispatch technicians with the appropriate knowledge and spare parts. Companies can also use remote monitoring to collect the data needed to improve shift scheduling and workforce planning.

But launching those services was more technically challenging than companies anticipated. One of the most visible obstacles was lack of connectivity between companies and their installed base of equipment, which made it virtually impossible to offer services that relied on such connections. Some new services don't work without a critical mass of connected equipment. Consider predictive maintenance. Without a large installed base of connected equipment, algorithms that forecast maintenance needs don't have enough operating data to draw from. It's also difficult and

EXHIBIT 1 | Industrial Products Makers Rebalanced Their Digital Services Efforts

CHANGE IN BENCHMARK COMPANIES' TOP TEN DIGITAL SERVICES APPLICATIONS (BY AVERAGE RELEVANCE SCORE)

![](images/4620f597f915b3109cdccc96596c5878037ec65e136de24317abfc7d15f3948f.jpg)  
Source: BCG Digital Services and Service Excellence Benchmark data as of January 1, 2020.

expensive to retrofit legacy equipment with sensors and to connect those sensors to industrial products manufacturers' data systems. What's more, for competitive, privacy, and security reasons, customers shy away from adopting new services that require them to share data about their operations.

In addition to their lack of foundational systems, many manufacturers did not have a clear understanding of the value that customers would derive. Because of that, the companies could not adequately articulate the new offerings' value proposition, and without clear reasons, customers were reluctant to commit.

## The 2020 Benchmark Findings: Companies Rebalance

The 2020 benchmarking survey makes it clear not only that industrial products companies have reprioritized toward enabler technologies but also that they continue to be slow in connecting with their entire equipment base and in moving digital services applications out of the pilot stage. That's a problem. But it's also an opportunity. It means that for this industry the journey to digital is still in its early days. Companies that get it right still have the chance to succeed ahead of the competition.

Enablers are the key. Enabler technologies are the digital platforms and systems through which information flows. They include the embedded sensors and other devices that collect the data, the networks that move the data, and the software applications and other technologies that ensure that the data being collected is accurate, secure, and sharable.

In the 2020 benchmarking survey, companies included four enabler technologies among the ten applications of digital services that they believe are most relevant to their business:

\- Data management systems. Data management systems store and share data in a way that is efficient and scalable, with the appropriate levels of security and reliability. They are centrally governed and provide a single point of reference for each piece of information. In the 2020 benchmarking survey, companies ranked data management systems as the digital element most relevant to their business.

\- Smart equipment. Smart equipment includes sensors that measure basic parameters such as pressure, rotation, and vibration—information that serves as the basis for equipment monitoring and other services. Smart equipment also includes the retrofit kits that are used to bring older products online. This equipment uses edge analytics to process information that the devices gather. It either reacts autonomously or sends only the relevant information, thus saving time and bandwidth. Benchmark companies pegged smart equipment as the second most relevant digital service for their business.

\- IoT backbone architecture. IoT backbone systems are the conduits that allow data from devices and controls to seamlessly integrate with cloud systems and with a company's applications and interfaces. Companies ranked IoT backbone architecture sixth among the top ten digital services applications.

\- Equipment connectivity. This enabler technology transmits data in real time and reacts to actions from a company's systems, such as requests for information. Equipment connectivity ranked eighth among the top ten applications of digital services.

As the name implies, enabler technologies don't create value on their own. Rather, they lay the groundwork for value that is created by other applications and services. Enablers also have a multiplier effect, allowing companies to introduce multiple value-added initiatives simultaneously and efficiently.

Connecting new and existing equipment remains a major challenge. Connectivity is a key enabler of digital services. If equipment is connected, companies can collect the data that they need to improve service and sales operations and offer new services. Nevertheless, industrial goods companies' connections with their new equipment and installed base remain limited.

Among companies in the 2020 survey, 78% have connections of some kind with their installed base of equipment. (See Exhibit 2.) However, the average penetration rate is just 13%.

The picture is brighter—though not much—for new equipment. Although fewer benchmark companies (65%) have remote connections with the new equipment, the average penetration rate (31%) is much higher than it is with the installed base.

Increasing connectivity isn't just a technical challenge. As noted earlier, customers are generally not willing to share data about their business and operations—even with a trusted business partner—unless there's a convincing value proposition attached to it. They might be more willing to share, for example, if doing so could improve their equipment utilization rates or decrease their operating costs. Customers also balk at sharing data out of concern that it could weaken their competitive edge or make them more vulnerable to a security breach.

Some industrial goods companies offer incentives to help customers overcome their reluctance to connect new or previously installed equipment. One US heavy-machine manufacturer took a two-pronged approach to encourage customers to connect to its data platform, an integral step toward collecting the data that it needed to create new services. First, the company sold all new equipment with built-in sensors and telematics at no extra charge. Second, for customers with existing equipment, the company offered two options: customers could get free kits to retrofit existing machinery with sensors and other connectivity equipment themselves, or they could pay a small fee to have the company do the installation.

But providing customers with the ability to connect wasn't enough. The company also needed to give them a reason to connect. It engaged with customers to understand how it could better support their business operations. Then it used customers' feedback to design an application suite. By offering the support that customers wanted, connecting their equipment became a win-win. Over a three-year period, the manufacturer doubled the number of units connected to its

EXHIBIT 2 | Connections to New and Installed Equipment Remain Low

CONNECTIONS TO INSTALLED BASE data platform to 1 million, about half of its total assets in the field. The level of connectivity paved the way for the company to offer new data-based services, which helped it be more effective in selling and executing services.

![](images/53c26190857821397bf249007b2fbf52a59fa53c0891963fcb35eda7e27a7c12.jpg)  
Source: BCG Digital Services and Service Excellence Benchmark data as of January 1, 2020.

CONNECTIONS TO NEW EQUIPMENT  
![](images/e2dad6c9475436c517c3c2f71c99757e8b09b5ad505a1d4e37230d3cf9fd0e04.jpg)

Even work on the most mature digital services is just getting started. If companies believe that data management systems and smart equipment are the digital services enablers that are most relevant to their businesses, it’s easy to understand why work to launch them is further along than other efforts. But that’s not saying much. Only about half of the benchmark companies have created a functional pilot for either of the top enablers, rolled out an initial service that could use some additional work, or have a fully functioning service up and running. (See Exhibit 3.) Some companies are even further behind—24% report that they have not begun to implement any kind of smart equipment pilot, and 21% report that they have yet to implement a data management pilot.

Work on other enabler technologies has been even slower. For example, no benchmark companies have rolled out fully functional IoT backbone architecture or equipment connectivity enablers.

Even so, work on enabler technologies has progressed faster than work on the other digital services identified as top use cases. That makes sense because companies can't begin to offer those services until the foundational enabler technologies are in place. In the areas of predictive maintenance systems and customer enablement alone, nearly $70\%$ of the benchmark companies have not implemented a pilot.

It's evident from the benchmark data that companies are working on many pilots at once, rather than concentrating resources on a smaller number of initiatives. That could help explain why so few fully functional applications have been rolled out. Companies may be unsure which use cases will provide the most value, so they have spread resources across many projects instead of going all in with just a few.

EXHIBIT 3 | Even the Top Use Cases Lack Maturity  
![](images/c0e92a8573f1b3e1508a57eb0c70d777ab3709cfb06bba9fc57629a5113294f6.jpg)  
Source: BCG Digital Services and Service Excellence Benchmark data as of January 1, 2020.

Bringing Enabler Technologies and Digital Use Cases to Life
Digital services hold significant promise for industrial goods companies to generate value. On the basis of their customers' pain points and how solving those points could create internal value, companies must decide which digital services to launch first, and then develop an attractive value proposition.

Make the value proposition clear and simple. To overcome customers' reluctance to share data, spell out in as much detail as possible and quantify how a new offering can help solve their problems.

Launch enabler technologies to support initial use cases. Avoid generic platform building. Use top-priority use cases as a starting point to implement basic enabler technologies in an efficient, scalable way. Once those value drivers have been identified, avoid distraction by limiting the number of use cases that are pursued at any one time.

Adopt a minimum viable product (MVP) mindset. Take a page from agile ways of working. Start by creating MVPs that can be tweaked and improved in response to customer feedback.

Dedicate resources. It’s not enough to identify which digital service use cases would be best to pilot first. For pilots to have the best chance of succeeding, they must have adequate financial and human resources attached to them.

WHEN INDUSTRIAL PRODUCTS companies realized that insufficient infrastructure and connectivity would make it difficult to launch digital services, they reprioritized their efforts toward building out the relevant foundational systems and platforms. But progress has been slow, too slow. That gives fast movers a chance to move ahead of their competitors. To do that and realize the full value that digital services can bring to their businesses, they must double down on moving enabler technologies from pilots to functioning applications.

## About the Authors

Michael Füllemann is managing director and senior partner in the Zurich office of Boston Consulting Group and a coleader of the firm's global competence center for services in engineered products. You may contact him by email at fuellemann.michael@bcg.com.

Michael Dahle is a managing director and partner in BCG's Geneva office and a coleader of the firm's global competence center for services in engineered products. You may contact him by email at dahle.michael@bcg.com.

Francisco Salmerón is a partner and associate director in BCG's Madrid office and a coleader of the firm's global competence center for services in engineered products. You may contact him by email at salmeron.francisco@bcg.com.

Verena Rossbach is a project leader in BCG's Zurich office. You may contact her by email at rossbach.verena@bcg.com.

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation—inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact.

To succeed, organizations must blend digital and human capabilities. Our diverse, global teams bring deep industry and functional expertise and a range of perspectives to spark change. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures—and business purpose. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, generating results that allow our clients to thrive.

## © Boston Consulting Group 2020. All rights reserved. 4/20

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and Twitter.
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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
