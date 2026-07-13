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
# AI Infrastructure: A Strategic Opportunity for Thailand

JULY 2026

By Aman Modi, Archit Choudhary, Haixu Wang, Clement Vellieux, Omar Zen, Papichaya Siriyontrakarn

![](images/000b3528cc1287d69e8d3b3f70c912e224813e5b0d94c2b26aeff145f6bcabbd.jpg)

## BCG

## About Boston Consulting Group

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change—bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.

# Table of Contents

## 01 Executive Summary

## 02 PART 1: Why Thailand must invest in AI infrastructure now to become an AI-forward economy

\- Thailand must localize its data center capacity to unlock its full AI potential

\- Thailand is not alone: peers are localizing, and their playbook shows what it takes

## 03 PART 2: Thailand must build on its advantages and close remaining gaps to deliver the 3 GW to 4 GW ambition

\- Thailand already has several winning conditions and a large pipeline in place

\- Seven levers for Thailand to deliver the ambition

\- Getting this right unlocks significant economic and strategic upside for Thailand, including US\$70 billion to \$100 billion in GDP contribution and 60,000 to 95,000 jobs

![](images/33788429596acb96e7a9ceb8e14330bb611bd4262674a8ca83a16e4cffb39797.jpg)

# Executive Summary

Artificial Intelligence (AI) is reshaping the global economy on a scale comparable to the First Industrial Revolution. As the era of AI agents takes hold and token consumption accelerates, the infrastructure powering it—and where it is built—will shape economic outcomes for decades.

Thailand has set a clear ambition to become ‘the AI hub of Southeast Asia’, and data centers are the foundational infrastructure that will deliver on this promise. They serve at once as a strategic asset facilitating low-latency and physical AI applications across Thailand’s key industries, a revenue anchor, and a sovereignty shield.

Singapore and Malaysia have each demonstrated that building domestic data center capacity is achievable. Both anchored their positions on the same foundation: governance with head-of-state sponsorship channeled through a dedicated executing authority, infrastructure pre-positioned ahead of demand, and bankable demand signals. Partnerships across the full AI stack and data governance certainty complete the formula.

Thailand holds the structural advantages that make it a credible destination for investment—competitive power tariffs, land availability and cost, fiscal incentives, and geopolitical neutrality that allows simultaneous engagement with both US and Chinese AI majors. The investment pipeline reflects this. The Thailand Board of Investment (BOI) received US\$23 billion in data center investment applications in 2025, and Chinese tech giant ByteDance committed US\$25 billion in 2026.

The window, however, is narrowing. Today's global data center shortage—and the upfront hyperscaler commitments and favorable economics it creates for operators—will not persist as supply and demand converge. Competition is intensifying across Southeast Asia and beyond, and commitments that flow to other markets are difficult to redirect.

Establishing 3 gigawatts (GW) to 4 GW of data center capacity by 2030 would position Thailand to serve growing domestic compute demand while capturing a share of regional workloads. Getting there requires building 1.6 GW to 2.4 GW of new capacity beyond what is currently operational or under construction in Thailand through coordinated action across seven fronts.

Governance is the key prerequisite. That will involve cross-ministry accountability, published capacity targets, and a single coordinating authority to streamline approvals. Two execution priorities follow. The first is partnerships across the full AI stack—hyperscalers, chip suppliers, frontier large language models (LLMs), and neo-clouds. The second is converting the Cloud First Policy and regional ambition into a bankable demand signal. Three supporting levers run alongside: (1) a clear cross-border data regime and sovereign cloud certification; (2) a Long-Term Resident (LTR) visa that draws in foreign AI specialists alongside a domestic engineering pipeline; and (3) structured pathways for Thai players to participate in the build-out.

The prize justifies the ambition. Direct returns from the data centers themselves are estimated at US\$25 billion to US\$35 billion in capital investment alongside US\$70 billion to US\$100 billion in cumulative GDP contribution over 15 years. At the same time, this industry growth could create between 60,000 to 95,000 jobs. The larger opportunity lies in the AI economy this infrastructure unlocks—an estimated US\$80 billion to US\$120 billion in cumulative GDP uplift by 2030, as productivity gains compound across Thailand’s key industries. Beyond the economics, Thailand’s AI build-out can provide a powerful platform to energize Thailand’s 2050 carbon-neutral commitment while securing Thai sovereignty over the data and compute that will underpin national growth for decades.

![](images/a175424d01930e7b4308bba0ac41bac6b9196d52c685bcab7fd8e9e35337b236.jpg)

# PART 1: Why Thailand must invest in AI infrastructure now to become an AI-forward economy

## Thailand must localize its data center capacity to unlock its full AI potential

The world has entered an era of economic transformation as consequential as the First Industrial Revolution. AI use cases are reshaping how industries and governments operate, and the returns are measurable. Every dollar spent on AI is estimated to generate an additional US\$4.90 in economic benefit. As investment continues to scale, the cumulative global impact is projected to reach US\$22.3 trillion by 2030.

The advent of autonomous AI agents is set to further accelerate this economic impact. Agents can execute complex tasks with minimal human intervention but consume up to

1,000 times more tokens per interaction than conversational AI, driving a step-change in compute demand.

The cost dynamics of AI are also undergoing drastic realignment. The cost of running AI has fallen roughly 10x per year since 2023. AI is within reach of more users and more use cases than ever before, with adoption accelerating at an unprecedented pace.

Thai enterprises and government are already acting on this shift. Enterprises are moving from pilots to full-scale deployment. The Cloud First Policy mandates migration of public sector workloads to cloud infrastructure. Thailand's National AI Strategy sets a clear ambition: ‘to become the artificial intelligence hub of Southeast Asia’.

Delivering on that ambition requires the right infrastructure. For AI, that infrastructure is the data center. (Exhibit 1.) AI-era data centers are not simply larger versions of what came before. Higher power densities, purpose-built cooling systems, and networking speeds that conventional facilities cannot

support make them an entirely new asset class. They are larger in footprint, longer in build cycle, and more capital-intensive. Where this infrastructure lands is a strategic decision in its own right.

## EXHIBIT 1

## Data centers are the foundational infrastructure for AI, as critical as roads & electricity were to industry

![](images/5e5b4f90a1a78886e8ede2fb1fcf9d2bbd213bbdd91ca5af4b1941c96abc9cc1.jpg)  
Source: BCG analysis

For Thailand, the case for building domestic data center capacity rests on four imperatives:

1. Unlocking the impact of AI for the full Thai economy

2. Stemming economic leakage

3. Securing data sovereignty

4. Safeguarding national resilience

IMPERATIVE 1: UNLOCKING THE IMPACT OF AI FOR THE FULL THAI ECONOMY

AI is moving off screens and into the physical world—into machines, vehicles, and production lines. These applications require sub-10 millisecond (ms) response times that only local compute can deliver. This has important implications for AI

expansion in Thailand given existing industry dynamics, with the \~1,400 km round-trip from Bangkok to data-center hub Singapore requiring 15ms to 20ms before any data compute occurs.

The considerations for Thailand's major economic sectors are clear. Manufacturing alone accounts for more than a quarter (27%) of Thailand's GDP. BCG research reveals that end-to-end AI implementation—combining virtual and physical AI—could unlock more than 30% productivity gains for manufacturers, if the right data ecosystem is in place.

The same shift is playing out across global manufacturing, as AI adoption increasingly represents a competitive baseline for cost, product quality, and speed to market. In Thailand, early applications such as vision systems for quality control are already taking hold, and manufacturers are setting their sights on higher-impact use cases including zero-stop production lines and autonomous assembly. Domestic data center capacity provides the compute foundation for these use cases and could give rise to a generation of Thai AI-powered local champions. (Exhibit 2.)

## IMPERATIVE 2: STEMMING ECONOMIC LEAKAGE

A large share of Thai spending on AI and data centers flows offshore. Repatriating that spend would generate direct GDP contribution, high-skilled employment, and a growing tax base. Onshoring AI capabilities will convert Thailand from a customer to owner within the AI economy.

IMPERATIVE 3: SECURING DATA SOVEREIGNTY
Thailand’s most sensitive citizen records, corporate IP, and government data face growing cyber risks as cloud migration accelerates with AI adoption. Without control over where data sits, Thailand cannot fully govern who accesses it or remedy a breach. Thailand’s Personal Data Protection Act and Cloud Government Guidelines already mandate that sensitive data remain onshore—domestic data center capacity is what gives those mandates practical force.

## IMPERATIVE 4: SAFEGUARDING NATIONAL RESILIENCE

Reliance on foreign-owned infrastructure creates a structural vulnerability. In the era of rising geopolitical uncertainty, that dependency exposes Thailand to unilateral allocation decisions, commercially driven price changes, and potential service disruptions.

EXHIBIT 2
Local data centers unlock the next AI wave:

<table><tr><td></td><td>Automotive</td><td>Electronics</td><td>Heavy industry/petrochemical</td><td>Logistics</td><td>Other sectors</td></tr><tr><td>Importance to Thailand</td><td>Largest SEA auto producer (~11% of GDP, ~15% of exports)</td><td>World&#x27;s #2  $HDD^1$  producer and E&amp;E $^2$ hub (~15% of exports)</td><td>~10% of GDP contribution $^3$ </td><td>SEA key logistics hub</td><td>...</td></tr><tr><td>AI use cases</td><td>AI-powered robotic welding and assembly, to maintain cost advantage</td><td>Automated precision assembly and real-time defect detection, to safeguard quality</td><td>Autonomous drone and robot inspection,real-time leak detection to improve site safety</td><td>Autonomous vehicles and smart port/warehouse operations,to prevent collisions</td><td>E.g., fraud screening and trading (BFSI $^4$ ), patient-monitoring and diagnostics (Health)</td></tr><tr><td>Why localization is required</td><td>Latency delays halt production lines and amplify production cost</td><td>High-speed lines with narrow defect detection window</td><td>Risks escalate in seconds, delays trigger safety incidents</td><td>Moving assets require split-second responses, delays create legal exposure</td><td>Time-critical decision-making and data sensitivity</td></tr></table>

1. Hard disk drive; 2. Electrical and electronics; 3. Including refining; 4. Banking, Financial Services, Insurance  
Source: Ministry of Commerce Thailand; NESDC Thailand

## Building domestic capacity also creates an opportunity that extends beyond Thailand's borders. Tier-1

hyperscalers and colocation providers are rapidly expanding across Southeast Asia, investing in regional hubs that can offer the required scale and operating conditions. At the right scale and with the right governance, domestic capacity could anchor a self-sufficient Thai AI economy while positioning Thailand as a credible Southeast Asian hub for regional AI workloads. Peer markets across the region are navigating the same opportunity, as Southeast Asia's data center landscape adapts to this third wave of growth.

## Thailand is not alone: peers are localizing, and their playbook shows what it takes

Southeast Asia's data center market has grown substantially over the past decade across two distinct waves of investment—and is now entering a third wave of energized growth. The third wave is expected to surpass what came before, underpinned by AI compute demands. This new expansion is also projected to be more geographically distributed across established and emerging data center providers. Markets that were previously on the periphery are building infrastructure and opening their regulatory frameworks to compete for their share.

The first wave of growth took place from 2014–2018 and gave rise to Singapore as the Southeast Asian hub. Singapore assembled an investment-grade combination of connectivity, talent, anchor demand, and regulatory stability when hyperscalers first entered the region. By 2016, seventeen subsea cables provided direct routes to the US, Europe, and across Asia.

AI Singapore launched in 2017 with SG\$150 million committed to AI research, industry adoption, and talent development. It rapidly established a domestic engineering pipeline before hyperscalers needed to staff at scale. Demand signals were established by 2018, with 80 of the world's top 100 technology companies already headquartered in the market, and a cloud-first policy pushing government cloud migration. Regulatory clarity completed the picture. Policies allowing 100% foreign ownership, a Personal Data Protection Act enacted in 2012, and sovereign cloud certification in 2013 gave operators the certainty they needed to commit. Singapore has since sustained its position with AI partnerships beyond infrastructure—securing OpenAI's APAC headquarters in November 2024 and a US\$5.5 billion commitment from Microsoft announced in 2026, among others.

Malaysia anchored the second wave of growth from 2019–2024. When Singapore imposed a moratorium on data center expansion, Malaysia was positioned to absorb the overflow. Its proximity to Singapore, ready infrastructure, and supportive policy made it an ideal location.

Malaysia had already laid important infrastructure foundations. Telekom Malaysia (TM) connected to around 20 subsea cable systems and extended its reach by joining SEA-ME-WE 6 (SMW 6) in 2022, linking to Europe via the Middle East, and the Asia Link Cable (ALC) in 2023, connecting to Hong Kong and across Southeast Asia.

On power, Malaysia moved equally early to solve the grid constraint standing between its generation surplus and reliable power delivery. Between 2018 and 2020, Tenaga Nasional Berhad (TNB) committed MYR18.8 billion to expand transmission networks and deploy grid automation—growing lines and substations by 21% and 16% respectively and delivering a 65% improvement in transmission reliability—including a dedicated Main Intake Substation directly supporting Johor’s data center corridor. This public backbone was paired with private investment at the connection layer, with TNB funding the transmission network, while operators funded their own dedicated connections to it.

Alongside power, Malaysia also committed the necessary land infrastructure, with over 1,200 acres across Nusajaya and Sedenak Tech Parks pre-packaged as investment-ready sites.

With the infrastructure in place, Malaysia turned its focus to policy—compressing time-to-market, attracting talent, and reducing the financial burden on investors. Two parallel tracks for permitting were introduced to accelerate approvals. The Green Lane Pathway, launched in 2023, cut grid connection timelines from three to four years to as little as 12 months. The One Stop Centre (OSC) 3.0 Plus initiative, operational since 2019, helped accelerate construction-permit approvals to 22–29 days for qualifying projects.

Coordination was later consolidated under the Data Center Task Force, established in 2025, which subsequently appointed Malaysia Investment Development Authority (MIDA) as the single approval window for all investment applications.

Talent was also a key consideration, with the Foreign Knowledge Worker (FKW) and the Malaysia My Second Home (MM2H) immigration programs both creating pathways for foreign talent to fill near-term gaps.

Investment incentives were also introduced to stimulate growth. The Digital Ecosystem Acceleration Scheme (DESAC), announced under Budget 2022, provides duty-free equipment imports alongside a choice of investment tax allowances (ITAs) or concessionary corporate income tax (CIT) rates to ease tax burdens through the first critical decade of operations.

Singapore and Malaysia proved that building domestic data center capacity at scale is achievable. Now the region is entering a third wave where growth is spreading more widely across markets. Each market is carving out its position through a combination of policy, infrastructure, and demand levers.

Indonesia created a hard onshoring pull by combining strict localization mandates with investment-ready infrastructure and incentives in Batam's Special Economic Zone. Vietnam addressed the barriers that had held it back—removing foreign ownership caps and streamlining permitting—to draw in hyperscaler commitments.

Thailand, meanwhile, is charting its own path with structural advantages in resources, incentives, and geopolitical neutrality—key points we will touch on in the following section.

Similar dynamics are playing out beyond Southeast Asia. In the UAE, Dubai anchored the first wave of enterprise and hyperscaler colocation demand as the region's established finance and business hub. The next wave of growth in the region is increasingly flowing to Abu Dhabi, with local AI and cloud technology company G42 anchoring sovereign compute to draw in hyperscalers.

The growth trajectories of these markets, while distinct, highlight five consistent strategies to deliver successful AI growth:

1. Elevating AI infrastructure to a national priority, championed at the highest level

2. Pre-positioning enabling infrastructure ahead of demand

3. Se

[中间内容因长度限制已省略]

e clearest precedent, benefitting from grid power from the national utility, priority NVIDIA chip access secured through G2G engagement, and captive demand from government-directed sovereign AI workloads. YTL now operates its self-developed 600 MW Green Data Center Park in Johor, with full capacity targeted by 2027. With the right facilitation, Thai land developers and infrastructure owners could occupy a similar role.

# Getting this right unlocks significant economic and strategic upside for Thailand, including US\$70 billion to \$100 billion in GDP contribution and 60,000 to 95,000 jobs

Achieving the ambition of 3 GW to 4 GW capacity by 2030 would generate returns that extend well beyond the data center itself. These gains will compound across the broader AI economy, as supporting infrastructure delivers a step-change in Thailand's strategic position.

## Direct economic impact from the data centers themselves

Capital investment and GDP contribution form the first layer of direct returns. A program of this scale could draw US25 to US35 billion $^{1}$ in capital investment into data center construction. This excludes IT equipment, which analysis indicates could account for up to half of total program costs. It could also generate a projected cumulative GDP contribution of US70 to US100 billion $^{2}$ over 15 years according to industry analysis, as capital expenditure and sustained operational spending compound across the economy.

The employment impact spans construction and operations, with an estimated 60,000 to 95,000 $^{3}$ jobs supported in total. During construction, 45,000 to 65,000 roles could be supported across civil works, fiber, power infrastructure, and mechanical, electrical, and plumbing (MEP) installation. Once operational, a further 15,000 to 30,000 permanent high-skill roles in IT, engineering, network management, and facility operations could follow, with wider employment generated across the supply chain and local economy. A portion of roles will be filled by high-skilled international specialists, with knowledge transfer to domestic talent over time.

The fiscal contribution extends beyond GDP and employment. Personal income tax from construction and operational roles, and VAT and CIT from contractors and equipment suppliers serving the build-out accrue from the outset. Standard CIT from the data center operators follows once the BOI exemption period lapses.

Beyond the financial returns, Thailand gains direct control over the data, infrastructure, and compute capacity that will underpin its digital economy for decades. This represents a sovereignty dividend that offshore infrastructure cannot replicate.

## Indirect economic impact: The AI economy this infrastructure enables

Domestic data center capacity is the entry point. The larger prize is the AI economy it enables. AI adoption could lift GDP by 13% to 18% by 2030 $^{4}$ , with productivity gains and new revenue streams compounding across every sector that adopts AI at scale. This could translate into a cumulative GDP uplift for Thailand of US\$80 billion to US\$120 billion by 2030.

Securing hyperscaler commitments also transforms the investment case for enabling infrastructure beyond the data center itself. Power grid, subsea cable, and connectivity upgrades all carry demand risk. AI infrastructure buildout can nudge these developments towards commercial viability for private investors and Thailand's state enterprises, mobilizing capital into critical infrastructure at a pace and scale that government spending alone could not achieve.

The same demand signal has the potential to accelerate Thailand's energy transition. High-volume, long-duration offtake would give EGAT, independent power producers, and renewable developers the bankable commitment needed to accelerate green generation and grid investment. This in turn converts the data center build-out into a catalyst for Thailand's 2050 carbon-neutral commitment.

The investment also builds human capital over time. Greater domestic compute capacity drives broader AI adoption across Thai enterprises, government, and households, deepening digital literacy and AI fluency across the workforce. Hyperscalers have consistently amplified this effect by co-investing in AI enablement programs alongside their infrastructure commitments.

In Singapore, Microsoft's Elevate program has committed free AI training and access to its AI-integrated productivity suite to more than 200,000 tertiary students, educators, and nonprofit leaders. Meanwhile, AWS's AI Springboard extends up to US\$470,000 each in cloud credits, training, and co-funded consultancy to 300 enterprises to accelerate enterprise-level AI adoption. Thailand could consider embedding similar commitments into its hyperscaler partnerships from the outset.

The key takeaway is clear: Achieving Thailand's 3 GW to 4 GW ambition can deliver a powerful platform for economic growth, and in doing so catalyze the transformation of the data ecosystem to deliver widespread benefits for the nation and its businesses.

## About the Authors

## Aman Modi

Managing Director & Partner, and Head of BCG Thailand Bangkok

Modi.Aman@bcg.com

## Archit Choudhary

Managing Director & Partner

Singapore

Choudhary.Archit@bcg.com

## Haixu Wang

Managing Director & Partner

Shanghai

Wang.Haixu@bcg.com

## Clement Vellieux

Partner

Singapore

Vellieux.Clement@bcg.com

This publication was commissioned by XSpring Capital Public Company Limited.

## Omar Zen

Consultant

Jakarta

Zen.Omar@bcg.com

## Papichaya Siriyontrakarn

Associate

Bangkok

Siriyontrakarn.Papichaya@bcg.com

![](images/43d864629bb727bae96d9482f99b4e5054c4cc71b087fa6236800299adebe664.jpg)
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
