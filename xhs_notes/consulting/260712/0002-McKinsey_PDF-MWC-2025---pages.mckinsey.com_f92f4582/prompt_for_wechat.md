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
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## McKinsey & Company

## MWC 2025

Key Take-aways and Highlights

March 2025

MWC25

## Key take-aways from MWC 2025

Overarching theme: AI and its impact on operations, network and next generation enterprise and consumer products taking center stage while remaining industry defining trends continue to evolve

![](images/cb9b21c404de80542b244a1835bf239149e3e1a1f87d637dc432defbdffd02ca.jpg)

AI and Gen AI: Omnipresent – integral to nearly every launch, announcement, and demo. Uncertainty remains around what will endure and deliver sustainable value.

![](images/b60b76543bd42f214324245d8dae86c5c1f5ec8efd7e2c82a77726b6d2631bf2.jpg)

(Network) APIs: The number of implementations is increasing, but the timeline for achieving true scale and significant monetization remains uncertain

![](images/16da1756d861d88335ee5b27a4943eb5b40435e4aa52a8dcfaf2f2d19d754b12.jpg)

Energy efficiency: Advancements in RAN and fixed technology provide telcos with ample opportunities to lower energy costs while enhancing sustainability

![](images/6070f37e60086840cb7ae74fb2736387bb252e236e63d96c1a29685081096552.jpg)

Non-terrestrial networks: From concept to reality – a series of new partnerships unveiled which have to potential to bring direct-to-device satellite connectivity to hundreds of millions of users

![](images/c1eb36edb151bcc932466f6f39f81224ab7d784a023b242569ff5eb5f73769ca.jpg)

(○) 6G: AI, sensing, and 4-7 GHz spectrum lead 6G discussions, while Terahertz spectrum has limited traction

![](images/39d65e79c2e21173cf214e918b21a20d9d72f898a059ab31635df17fb42831c9.jpg)

Quantum computing: Quantum-safe cryptography is becoming an important topic for telcos to protect their networks while quantum safe networking emerges as a new proposition offered to enterprises

![](images/c88325b2235e059199527a12e2a2b1feeb3fa0d145f0722dc5b66e65fc529c57.jpg)

Other topics discussed: ORAN, private networks, 5G/6G for public safety and defense, consolidation & regulation and spectrum allocation reform

## Highlights overview at MWC 2025

![](images/6fb192326bf14cf7f0055ad27a1338e59add249792abef1dc903cc8b410303e8.jpg)

Relative relevance at MWC

Telecom products and services

![](images/1fba67b1d173a8916df9a11a58722806a53d5e4c63bf2ca1f389e8084568716d.jpg)

Telecom operations and infrastructure

Connectivity

![](images/a9db2e60391131eeccd5d151eb613a5bd396c495eb0eb1b99928498dd0c8b5b6.jpg)

Near Core

Beyond the Core

![](images/7dfa63e98ae0f54324a2a54c074302a35838ac3c754517b6c7b34b44fa222e8a.jpg)

![](images/2e1a74971494d40b9996daba3ca90b151f28f97b9056416aebe05200dea148dc.jpg)

![](images/ad237d142fcf26e60f16f9fb20d11bb1d03fd1b7a227fdb4d33c3f15cf7771ae.jpg)

Direct-to-Satellite/ NTN: From concept to reality

AI in operations

![](images/00157a8db23701f1b39a1dc638262cc99b07d54fa2be6a027f2817529c94f0dd.jpg)

APIs gaining momentum, but still early days. Supply ramping up—albeit slower than hoped

![](images/b2d2d9ad4c8885d94e1f7278755a3c42cc7416991694dd671ce733597b9969ba.jpg)

Mobile network equipment

Telcos are intensifying their focus on security offerings by capitalizing on internal expertise

Others

Fixed network equipment

![](images/796056e4bddb1d957e67dd450b71a8635da31057b2a0978fe6bcb541c3ae762f.jpg)

Telcos launching a range of AI services targeting consumers

Vendors and MNOs highlight (gen)-AI-driven use cases designed to enhance nw efficiency

![](images/4f077cebdbe460be2a9bce84d9139ab7be7262c20a55f966519b56b12a6856b2.jpg)

Energy efficiency increasingly becomes a key selling point across network equipment categories

![](images/4e651ddff6f51b5edcd99e8f1af2fe74ceaaaac32b6f1c535fc470552a1a282b.jpg)

5G use case narrative shifted from technology-centric to emphasizing business outcomes

![](images/e42d77a41b6256a363015ede0eeb605bbaa00fbe55ec75f37e5fd2ba56cae13a.jpg)

![](images/75e6a157ef5682f63cad3b1dd9f30993fc3722d897a1002f849b1bd3ccadf15a.jpg)

AI-driven solutions tailored for enterprise needs are emerging within Telco B2B portfolios

Telcos leverage AI agents to transform customer experience

![](images/a98417645150cc70f5d432eb8fcd5a0fe2222a838c017d5bb5670ffd732e758c.jpg)

AI, sensing and 4-7 GHz spectrum dominate 6G discussions

![](images/3cddcf00d85964a201bc66dc5f1a5d8e7cb6943a89999f79642a6a5e000844c7.jpg)

![](images/1f8313bebc94b24bcc140b9da084b6b4509406864dc17d802bda943a230b51df.jpg)

![](images/d0aebfa7267adaf62c0e2492a3126d86902c322f41c06fbf6ff04199092f082a.jpg)

![](images/bcce718260b8e43c519124f9fb9de55410a4fe32e0d4ff6b99a2c325f76559a9.jpg)

Quantum networks positioned the next strategic frontier for equipment vendors

own networks against threats arising from quantum computing

Quantum safe networks emerging a new B2B proposition

Sovereignty emerges as a core component of the cloud value proposition

![](images/4d92fe67a86b3c8ddfd335733908b872a13e8638dc0b4b010a86aeafc47704e7.jpg)

AI-RAN: Moving RAN workloads to GPUs is under exploration

![](images/a63d6507751e573c0f66b6fa15c20ce8a53ed86db51c51e6fe26690fae857e33.jpg)

Long tail of smaller RAN vendors targeting private networks opportunities

\- Telcos to consumers
- Network vendors to telcos ○ Telcos to enterprises
● Others

Deep Dives

![](images/49d0a738d2f760d91c4dfceee093542e6c41f6ee154ea9a49424ecfe58023033.jpg)

"Build your own MVNO platform" launched by tech/ wholesale players

![](images/c405d179c8397bd1a449729ddee9f0a1423132f32732a2af243a8cb96839acb8.jpg)

5G/6G for defense and public safety is emerging as a promising growth opportunity for vendors and MNOs

![](images/f7c42d0bf066934146d40533783fab9c4bf9f41b1ce8c174ba6d317e1ce295ce.jpg)

Several operators unveil plans to introduce GPUaaS for enterprises

![](images/57c5376e4281cb4c3a747786aa081982150afea3a8303e32e2a16d7a5975f90b.jpg)

New AI alliances between telcos announced

![](images/04868529cc36a93d299c7c415c1b3a3ec3f4f4fd64704c02ebee56d547a5fe90.jpg)

ORAN compliant equipment choice increases but weakening traction

## 1. Direct-to-Satellite/ NTN: From concept to reality

## Why it is relevant

![](images/2b5382a4f445966991733157194941e6590007fc30f61438798604c232523036.jpg)

Direct to Satellite / NTN technology makes mobile communication available everywhere

Europe's ambition to become relevant and autonomous in satellite connectivity

![](images/909d180842729e34ed69df4a5e71c540814a8c9a5a1e70f6f2d7c20de4d8adf5.jpg)

of the global mobile subscriber base are served by one of the 91 operators which already have agreements with satellite providers in place

10 bn €

Deal between the European Commission and SpaceRISE consortium

## Key observations

![](images/8f3bb449e3da1e5d01c309fc7d5509f3426a0644d00a6e2058cd6b7988f61272.jpg)

Wave of new partnerships announced: Vodafone and AST SpaceMobile SatCo, KDDI and Starlink, Verizon's' partnership with Singtel and Skylo

EU reigniting European ambition on satellite connectivity by signing a 10Bn Eur deal to develop satellite constellations with SpaceRise Consortium by 2030, aimed at bridging digital divide and strengthening European autonomy in this space

MNOs position NTNs value proposition clearly as a mean to expand coverage beyond cellular footprints: “We have a mission to finish the job of covering the last 400 million people and satellite service is the solution to filling coverage gaps” – Bharti Airtel CEO

![](images/e8f7015a34042d8bdd792e847122eeab57ac82a5cc8a84113953143e9f8ba62f.jpg)

![](images/87849aa6c5e9d7ab56c1d631ff352998e6ffefe1d4c4869293303ff9b0a21bdd.jpg)

## Implications

![](images/552ca245cadd14735ae4381807a3dd4ae98c8d07a0edad877dc005fed1d0742a.jpg)

1) No dominant player has emerged in the satellite market, with key players (AST, Starlink, Eutelsat) forming the majority of partnerships

2) Wide consensus that satellites will complement, not replace mobile connectivity provided by MNOs

3) However, technology competition between LEO and cellular connectivity exists in IoT and FWA

## 4. APIs gaining momentum, but still early days. Supply is ramping up—albeit slower than hoped

## Why it is relevant

![](images/a7f5b931718ec9d8413582043994f6f1576bcd95cc59c42a5a97d023cf5d224b.jpg)

At MWC 2025 APIs became a topics for all major telco operators
Current use case focus is on verification, security and quality of services

## 20+

International telcos have formed a global JV to monetize the Network API opportunity

## 20 bn €

Commutative opportunity between 2025 and 2028

## Key observations

![](images/7ec8cbe8c9a23c6d530317cb05abe132b9e21de27acd341853391d0f09341c0b.jpg)

Two days ahead of MWC Orange announced LiveNet, a dedicated business unit aimed at marketing network APIs. At MWC Orange demonstrated their Industry 4.0 network APIs in action. Further use cases demonstrated were fixed and mobile connectivity QoD use cases and security APIs designed to combat fraud

Network APIs are not a single-company game. Operators like Telefonica leveraged MWC to get the developer community together in API hackathons

Deutsche Telekom's T Wholesale and Nokia announced a deal to drive and simplify developer-created applications for Network APIs

![](images/3c86db9095794ddc3b623b1fe2e977106dadea10d2b1a66394301c0408ba1b33.jpg)

![](images/8f04cedf80008120ede3649421c536207d477df09f1b3b3a89fe63c6dc07548c.jpg)

## Implications

![](images/4593d757b515b81342b7b90c226e4a56f06eef24ceaf2db67a41b2043675aa98.jpg)

1) This is an ecosystem game. The industry needs to collaborate along the full value chain to ramp up the network API business

2) Network APIs are gaining momentum, but still early days, operators should focus on use cases gaining traction like fraud prevention and QoD (Quality on Demand)

3) The big question: the business model. Real revenue remains low so far, but are expected to grow over the next years, so operators need to think strategically about this

# 9. AI is part of almost every launch, announcement, and demo

Unclear what exactly will stay and generate sustainable value yet - Telcos to consumers
- Network vendors to telcos - Telcos to enterprises
- Others

## Gen AI play presented at MWC

## Telcos and (Gen) AI

## A Telcos launching a range of AI services targeting consumers AI-powered consumer products and services, including AI Phone, personal AI Agents and AI-enabled XR/VR glasses

## B AI-driven solutions tailored for enterprise needs are emerging within Telco B2B portfolios Tailored solutions for business customers, including AI digital assistants for SMBs, proprietary GPT models, and targeted industrial applications such as AI-driven smart maintenance

## Several operators unveil plans to introduce GPUaaS for enterprises On-demand GPU service for enterprises. Telcos see a right to win to host GPUs in the RAN i.e. closer to the customers reducing latency while leveraging synergies with hosting RAN workloads

## Players (non exhaustive)

![](images/f2def513817fb4dc34e89ef9109c09198d69a8e23f0928eececc103ef74e1227.jpg)

![](images/df8240f5759be47ce65a5f2ee07b6f390d43521e7368d6ea4a326bb40decbaf7.jpg)

![](images/1cee311232a76693298112a7858fbb946745ccf074268ee552a09af5222a6057.jpg)

![](images/4ddd9743ec7f65c2b0b9e9af51e238e1e4afe8a3d1db946358079d86e0e7db68.jpg)

![](images/a331946094ac7bc09b8b85a06f76d45cd8a84e19035f7142df9b0b527c326dcb.jpg)

## D Vendors and MNOs highlight (gen)-AI-driven use cases designed to enhance nw efficiency LLM are leveraged to use unstructured dataset to further advance towards zero-touch network operations

![](images/d463bbbf8c5818f71f3443c69893e1c1e8a7d97298d8875683d8586b6094c9df.jpg)

![](images/4754492d432586e1fbcf0e404e2f406ce62ee682e666ad359251a581b4576076.jpg)

![](images/712d07390b9242003fb042836d7058e4655ce491d7186dc81404a3b3668d5860.jpg)

![](images/cb929af5e852cddde179e970c4d1c49e971777d61bcd84035d0476e09dc592d7.jpg)

![](images/5d356fa6c12d3f3842143ffae4cc1535e59f56edac88fcff9b435ac0f702b0e4.jpg)

## Telcos leverage GenAI to transform customer experience across consumer contact points AI agents transform customer service by shifting from basic chatbot task handling to delivering AI-powered, tailored experience journeys

![](images/0c1c46b70e9c0c94f28f0dcad93ab2b7eef94f108ecddc0f838202d5a2441301.jpg)

![](images/a7a053763de231664fa6976c4589c757996c5db8a0fa54c32c2ec80e7d9f676b.jpg)

![](images/f6be03ae9c765d1b75a9da55bcae979f168b313497dd8de070bc1192368cb52e.jpg)

## F AI-RAN: GPUaaS and moving RAN workloads to GPUs is under exploration

TelCos did not capture a fair share of growth from tech disruptions (increased video consumption, introduction of 5G) in the last decade; AI-RAN provides a monetization opportunity through GPUaaS

![](images/f3ec999cabbc8cda9e3109a0641e6dbfe8f69964525938538cdb559305a8f8d6.jpg)

![](images/7ae127a6578e4942dd8ac8fa4831ae0b46d843fdd04c700febcc1ff945e82163.jpg)

## G New AI alliances between telcos announced

AI-RAN Alliance membership including now 7 service providers, 43 tech companies, 15 academic institutions, 6 industry associations, and 4 laboratories (from 11 to 75 members in 12 months), Telco LLM

![](images/2333ea056ff2f1b7936050e008a46e135b600e263ab1cf8208d60d19f969547c.jpg)

![](images/3e28003c3309c9758639b98d71c190879ddb94394adfdd435a4f09255af7cabd.jpg)

## 9A. Telcos launching a range of AI services targeting consumers

## Why it is relevant

![](images/e9eccbb5ed156a8f91dc781d042d800dac88622f721a87c8d33e05b35af061d7.jpg)

AI consumers propositions are moving beyond concepts and becoming a reality, potentially restoring appetite for diversified revenues streams in B2C

![](images/8b51ebc435a511e048378dc9acc51e07292fffa97b6525a54eb4e9866cdc3893.jpg)

AI demand in mobile communications by 2030, according to SKT projections

![](images/a69bddd88c2eb49bac65a1ab05d3cf5faa9e685fe4509abcd155be100ef8c8c4.jpg)

Population in countries like US and UK, still not using Gen AI

## Key observations

![](images/aa7b99730d457b4a5acb85e47117d13e1d4d44f83f616062d99b8946dfb07a57.jpg)

AI Phone soon to become reality: From MWC 2024 vision to MWC 2025 reality, DT's Magenta AI phone expected launch in H2 2025, featuring “virtual butler” by Perplexity's AI. AI Phone allows multiple tasks w/o switching apps

“..our AI Phone, will help you in many situations: find reliable answers with reference to the source. Conveniently book a restaurant or taxi. (...) All without having to switch between apps. Intuitively and preferably by voice. This is the future of AI innovation for consumers” – DT BoD Member

AI Personal Agents pervasive especially among Asian Telcos offerings: LGU+, China Mobile, SKT all showcasing personal AI Agents whether within existing caring app or as different solution. SKT Astar soon to launch in NA in 2025

![](images/1c5fa9808a5e61864ac33349e619adc24483ddc6d09375e68d4c40fb66f193a6.jpg)

![](images/1844c6d234b0bb46b15fcc86a53adbb8be099d99f1947aba558a208c3d686495.jpg)

![](images/553127fcc7b8cb5721fb43e24712e7cf02edb12bffa209ed560d7e74c2c8c773.jpg)

## Implications

![](images/8ce0f3f2db4cb2df1e8f091fea46018a835fc59c202db39d6282401cfbcfc75b.jpg)

1) Partners are key for success – Telcos shouldn't do it on their own and partners like Perplexity, Google are instrumental to offer AI products / services,

2) Potential to offer AI Personal Agents as a service to non-customers to unlock additional revenues stream

3) Focus on user experience: importance to have an intuitive, user-friendly UX to drive adoption

## 9E. Telcos leverage GenAI agents to transform customer experience across consumer contact points

## Why it is relevant

![](images/6cca35a7d55378fb57f4de1b4b9781ea6216fce1ebc4e1c60f5e4f20d551f018.jpg)

Telco customer service is evolving from chatbot-based task resolution to AI-driven, personalized experience journeys

![](images/4af0ade33f03b0d64a604ad2cc024b0e852f0e6b8e77f0d89b27d102ff61e51f.jpg)

Vodafone's investment in Customer Experience transformation

![](images/69ba7013529f7ffa33cf2b3192d451d002e6a01ff8a706bd0bbf8a9ca04d06aa.jpg)

Investment commitment on AI services in the next 4 years by LGU+

![](images/77bda8e01be99e36a99f3db6c2ccae236017107c66eb7ce276ecbb77acb7cef1.jpg)

Improvement of first-time resolution rate for complex journeys for Vodafones' SuperTobi

## Key observations

![](images/cc178cd6f226153af191248640d8d11589774fcca847556a5ff58bdca023b566.jpg)

AI Agents in the spotlight with telcos showcasing how they are integrating Gen AI/AI into existing chatbots, revolutionizing how telcos interact with their customers

\- Vodafone Super TOBI delivers personalized interactions in 15 languages, improving first-time resolution up to 50%. Super TOBI uses retrieval-augmented generation to handle complex queries with contextual accuracy

\- LG U+: Introduced multiple AI agents, such as the U+ Counseling Agent, providing tailored recommendations for services like roaming plans based on user travel.

AI support tools for human agents are increasingly seen as critical for consistent support and employee skills expansion (e.g., Vodafone's Super Agent)

![](images/dcfc35c0ffc82f1bb214a2dcb285969948e23d16f7b3cf0d0e8882563954b5b7.jpg)

![](images/09d41dd14c633a28a0fc1ca0695dfbc419168148d3d7e2aaafb82f60710e6171.jpg)

![](images/70f4d9e8c7252d6c6df27455d0b1e650c4b3ff8c8589e884cc6534026fe7c738.jpg)

## Implications

![](images/0a32f1fceaac99fa667e00dcca1518a146dfc54c429ce3592585d58a6b010d63.jpg)

1) Robust data analytics and AI training models are critical investments for Telcos to ensure the AI Agents can accurately understand and respond to diverse customer needs

2) Provide adequate training for human agents to effectively collaborate with AI Agents and leverage their capabilities, turning them into human "super agents"

3) Establish clear AI frameworks and governance structures to address ethical concerns proactively, mitigate potential biases, and ensure that AI-driven decisions align with core values

## 9C/ F. AI-RAN: GPUaaS and moving RAN workloads to GPUs is under exploration

## Why it is relevant

![](images/15557f4bb13c9952ae15b61bae24ed2257652e185627c6c633cf5b8356d443cb.jpg)

Stakeholders across the value chain hold varying perspectives on the necessity of GPUs in the RAN to achieve these RAN-related advancements

## Key observations

![](images/026535c93b511e2b65a4c40ee786e8ea3f6c3b72865455ab4ffc9dabcc4c77f1.jpg)

## Telecom operators

\- TelCos are planning to use AI to optimize their networks and prepare for AI traffic growth

\- E.g., SoftBank and Viavi have a concept on using AI to improve spectral efficiency, KDDI planning to deploy disaggregated backbone routers to scale with traffic

## Equipment manufacturers

\- Vendors claim RAN optimization using AI does not require GPUs

\- E.g. Nokia claims AI for RAN optimization performing on Marvell accelerators, Intel claims that AI optimization for RAN only needs additional cores on Xeon 6

Potential global demand for GPUaaS addressable by TelCos by 2030

## New entrants

\- There are new players entering the value chain to challenge traditional players

## \$ 35-70 bn

\- E.g., Capgemini claims to have AI-RAN implementation which includes L2/L3 software traditionally built by OEMs and orchestrator between AI and RAN workloads

![](images/47001de7f53a529ef20396334fcf9a392747e0ba333e6831133eafe6f7b19cef.jpg)

![](images/f6ded69caac7b484b6b95a0ba6219e5777aa7f6b53404ca0a256f3c7b022955c.jpg)

## Implications

![](images/522bc19d2e2a564ddb81ec0af15b4ce5efe7e77174fc1f984f5768056f3b7dd2.jpg)

![](images/3dac3a11f61958a437fa799660f3cf4717b10fa656b71c1aabbf4f65c79b5ffd.jpg)

1) There is interest in the value chain for AI-driven network optimization

2) Stakeholders across the value chain hold varying perspectives on the necessity of GPUs in the RAN to achieve these RAN-related advancements

3) The opportunity for GPUaaS has more traction

## 10. Energy efficiency increasingly becomes a key selling point across network equipment categories

## Why it is relevant

![](images/14fe86400b1e6d6a6eaf59afef1cdeb71ccee4fff3881daa41fa88b8e05b15f8.jpg)

GSMA presented its new Telecom energy efficiency benchmark on Day 2 of MWC

Energy efficiency becomes an important key purchasing factors and was on top of all vendors/ exhibitors' minds

## 30-40%

Of energy reduction possible with new energy efficient equipment

## Key observations

![](images/e464442ddb853645715dca535354d25c394e2b569238f01837fa82057d5a43c1.jpg)

Areas of energy consumptions are the RAN with 76% of all energy consumed, followed by core & datacenters with 19% and other operations with 5%

On average 29% of energy is consumed by passive infrastructure (reasons: cooling, site design and older power sources)

Ahead of MWC Ericsson expanded the portfolio with seven new energy-efficient and high-performing Massive MIMO and Remote radios, Indoor 5G solutions, and new open fronthaul products called RAN Connect to reduce energy consumption by up to 30 percent

Rohde & Schwarz and VIAVI Solutions have collaborated with Analog Devices to showcase the potential of network energy saving (NES) in open radio access networks to which saves up to 40% of energy during low traffic load

![](images/8c5569e9363463900f139f6f866d4d5df8c2bc17012a05e13b6ad894864dc74a.jpg)

![](images/3ae89036509cbb89e6522ea755b01c677d293add0231e8ad3e46bfd13d8c9a20.jpg)

## Implications

![](images/e1c71dd6a4283093d0193dadcfd285b7bfbe95f07d944f2c3a34e4146d90c8ed.jpg)

1) Focus on RAN: the Radio Access Network is the largest energy consumer, accounting for 76% of total energy usage. Prioritizing energy-saving initiatives in this area can yield the most significant impact

2) Evaluate upgrading passive infrastructure components as well

3) Leverage advancements in energy-efficient technologies by reviewing current supplier base based on energy efficiency metrics

## 11. AI, sensing and 4-7 GHz spectrum dominate discussions on 6G

## Why it is relevant

![](images/db06ca5c85bc0772bcb0e8169fe3c23c3d13d714127b523723b4edc209eb4b3d.jpg)

Major industry meetup ahead of key 3GPP meeting in South Korea with pivotal discussions on the goals and properties of 6G networks to advance 6G standardization

ITU vision has been published after last year's MWC, now the industry needs to translate it into a roadmap requiring consensus to be built

## Key observations

![](images/1fa26f225150af47ebbdb876f54d217df68d551d4fbfdfceebcb18f51a33b825.jpg)

Sensing demos evolved from purely technical PoCs to PoCs of first-use cases:

NOKIA Real-life 6G demo, pinpointing location and distance

Large-scale private network digital twin showcasing the importance of 6G for sensing systems

Strong industry preference for 6G to utilize 4-7 GHz spectrum, while Terahertz discussion remained muted

Growing consensus that 6G will be AI-native, however, key stakeholders have yet to align on its exact implications

![](images/db5b82597613ca7cc69c0428bdc25e4e8982efd0a8585bba013b04b8c0e43db5.jpg)

![](images/b6c532abcff5dab954c3be981ed3cca7c7b37ce08d2f6b9b08ceb04355ca8fdb.jpg)

![](images/bc32b0f104d762cc05446627c5777f308af87d58566294e933e638c12806794e.jpg)

## Implications

![](images/d5a73997cd4722d8bf1ad3e8fe72603ae2852d239683d121c18e315893f8d1a3.jpg)

1) 3GPP meeting more decisive than MWC

2) First implications can be drawn on the directions for R&D with the highest likelihood to meet WTP from customers – sensing, 4—7 Ghz support, AI

3) Wide consensus that AI native will be a key differentiator, however unclear what 6G should deliver incrementally over AI-RAN, GPUaaS and AI in operations

![](images/9e20f3a235dfc9dc33cb4da6befed4ee9125088088cd79100a8bc5a8a9c030ed.jpg)

6/13. 5G/6G for defense and public safety is emerging as a promising growth opportunity, longtail of smaller equipment players targeting PNs

## Why it is relevant

![](images/8eaf3c263f83c13f8588fa466ff13e3248e2e0b3eaa93567497e361e13624103.jpg)

Public safety organizations are transitioning from non-3GPP standards like TETRA and P25 to cellular systems to enable broadband services, as governments worldwide expand defense budgets in response to rising tensions

Smaller RAN equipment vendors have faced a declining market share in public networks over recent years and are now seeking areas to return to growth

![](images/618f34755056c3d8fb5a7a9c0be1d37eb25fd83dc197f11c41cf2120b2aaa436.jpg)

PNs deployed in defense and public safety, while spending is significantly (e.g., vs. factories) higher due to larger areas covered per PN

## Key observations

![](images/0e080ce6642ae9133df8384b7c87680a5f272151141dc7330e7f1c725c8bfd1f.jpg)

Private networks have shown reduced momentum compared to last years, particularly in respect to announced growth ambitions of the leading vendors

Emerging RAN vendors
focusing on private
network opportunities

Bacells
Comba
ZTT 中天科技

Defense and public safety stand out as the most prominent verticals in recent announcements

![](images/903c56bb7c444199f0ef10792293e40a36946b23f2c0ded8865e875e2afb4092.jpg)

mcX MCPTT service leveraging its 4G and 5G networks

Launched a range of mcX solutions, e.g. The MCPPT service platform Hy Talk MC and the 5G mcX handset PNC660

![](images/5ac7d354a7fb60ccb141f8245f53e3d4af0f819012f0b2df6d7a88c8dab96a55.jpg)

Nokia and Verizon integrated Nokias' military-grade NOKIA 5G solution in Lockhead Martins' hybrid base verizon station

## Implications

![](images/3f2a4901f1683b292dede94a3276d508e009a3bd0a6a927e687685e9793ffe4c.jpg)

1) Consolidation among ORAN vendors presents a significant opportunity going forward

2) Vendors and MNOs may benefit from prioritizing the public safety and military verticals in their G2M strategy, as a significant portion of spending will be committed in the coming years with many agencies globally transitioning to 3GPP standards
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
