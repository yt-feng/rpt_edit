你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
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
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
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
# D2D in MENA: Resilience Tool, Connectivity Bridge, or Commercial Add-On?

July 2026

By Ruediger Schicht, Thibault Werle, Marc Nasr, Hamza Najmi

## BCG

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

## Table of Contents

04 Direct-to-device (D2D): A resilient, space-based, way to connect

06 Not "5G from space": Key constraints and barriers to scale

08 Implications for MENA: Connectivity enabler, resilience mechanism, or complementary add-on

10 Immediate actions for governments and telcos: Thoughtfully integrate and leverage the emerging technology

![](images/f19528fdfd8224d79817fec0119c55f2b02ac854258e493fab9d33f10130f1b2.jpg)

# Direct-to-device (D2D): A resilient, space-based, way to connect

Direct-to-device (D2D) internet systems are on the rise and were a key area of focus at the 2026 Mobile World Congress (MWC). Starlink's keynote, for example, presented Starlink Mobile – a D2D system operated by SpaceX. Such systems promise the elimination of cellular “dead zones” by enabling standard smartphones and IoT devices to connect directly to satellites. While the technology is evolving fast, it still faces hurdles that require diligent consideration.

Each region is subject to different commercial set ups and connectivity objectives, and even within MENA the technology's potential use and uptake vary considerably by country. Local regulators and telcos will play a vital role in shaping the trajectory and reaping the benefits of D2D adoption.

Starlink originally began providing broadband services in 2020 for both consumers and businesses. By March 2026, it had connected 10M broadband customers globally across 150+ countries and territories.

In simple terms, D2D satellites act as a “cell towers in space,” connecting unmodified smartphones to the internet using mobile spectrum (or adjacent). What makes D2D unique is the ‘ubiquitous coverage’ it can provide around the globe (including poles), eliminating digital divides, and leveling the digital access playing field for all nations. At the same time, D2D technology offers promising resilience, providing connectivity during incidents that terrestrial networks cannot.

The leading D2D providers differ across key technical dimensions, including satellite count, altitude, channel bandwidth, peak download speeds, satellite capacity and access to relevant spectrum, and those differences directly determine what each configuration can serve. Larger, lower-altitude constellations can serve a large number of users with a potentially smaller antenna size, whereas higher-altitude systems will rely on greater channel capacity and antenna size to connect a larger number of users per satellite.

Though it is still an early-stage technology, Starlink Mobile already claims to support 10M+ active users through its D2D service and aims to reach 26M customers by the end of 2026. The company predicts that its future wave of dedicated D2D satellites will provide levels of speed and coverage that approach those of (very rural) terrestrial networks. Looking ahead, D2D has the potential to become a standard add-on feature offered by premium network packages.

A wave of recent actions by Starlink highlights the need to move simultaneously on multiple fronts – from technology & spectrum advancements (e.g., acquisition of additional spectrum, patent for bandwidth optimization in D2D, announcement of bigger and better Gen2 D2D satellites) to telecom partnerships (e.g., with T-Mobile in the USA, and operators spanning 10+ EU countries and 14 African countries) and future plans (e.g., as a possible bidder in FCC's spectrum auction) – to bring this vision to fruition. Other major technology players are entering the market, making headlines through different acquisitions. [1,2,3].

![](images/acfdb227d1849c1eeccaf76824611accc85f755496d4a864c0930b336bb2edea.jpg)

![](images/4a02b1c8f4358caaa797790080e0ced3b5ed9227e497c146ecba5a0cd9616dbe.jpg)

# Not “5G from space”: Key constraints and barriers to scale

However, the industry is learning quickly that D2D is not “5G from space”. It’s a different type of coverage, with physical, economic, and regulatory/competitive constraints.

## Physical limitations

Indoor coverage and dense urban areas. D2D can only provide outdoor coverage, but 50-90% of global mobile traffic occurs indoors. Additionally, D2D cannot competitively serve dense urban or suburban areas, where its limited capacity must be shared by millions of people. For example, GSMA - assuming a 15,000 satellite constellation and using all MSS spectrum - notes that D2D can serve 2Mbps for 10% of the population in a density of <40 people per sq. km. Compare this to Dubai, which has 700+ people per sq. km.

## Economic considerations

Satellites are ongoing costs, which are passed to users. Each satellite will last \~5 years (or less in the lower D2D orbit of \~340 km), and currently costs \~USD 2-3M to manufacture and launch. At Starlink's scale, this represents hundreds of millions every year in capital expenses. Translating this cost to users, the current D2D add-on packages globally at c. \$7-10/month (\$80-120 annually) position the service as a luxury add-on, and not a mass commodity.

Spectrum is the gatekeeper. D2D requires either access to IMT $^{1}$ spectrum, typically via a mobile operator partnership (e.g., T-Mobile carved out 10MHz for its Starlink Mobile partnership), or MSS $^{1}$ spectrum rights (like major technology players making significant acquisitions). The necessary spectrum is only available through telco partnerships or high-cost acquisitions.

Handset capabilities impact adoption. While most modern handsets allow for satellite connection (e.g., over 60 modern handsets are supported by the available D2D services currently), universal smartphone compatibility will limit adoption. This is especially true in rural areas where people are more likely to use lower-to-mid range smartphones.

## Regulatory/competitive landscape

Regulatory approvals take time. Regulators globally are still assessing the rapidly evolving technology, and more importantly, the guardrails that will be needed to minimize commercial and sovereign disruptions. In this context, the US Federal Communications Commission (FCC) is paving the way for leadership in D2D connectivity. In April 2026, decisions provided a permanent license for AST SpaceMobile, and reaffirmed existing licensees' exclusive rights to use certain D2D bands.

Strong competition from terrestrial networks. The Global System for Mobile Communications Association's (GSMA) most recent publication $^{2}$ highlights that $96\%$ global population is already covered by terrestrial mobile, and D2D covers only

edge cases. BCG analysis indicates that in rural areas, LEO can only provide \~14% of capacity density vs. current terrestrial mobile networks. T-mobile's CEO has noted that its T-Satellite D2D service is seeing lower usage (1.8M free beta signups, limited paid engagement) than projected since the company's terrestrial network leaves few coverage gaps for consumers, and free satellite messaging services from device manufacturers compress the addressable market. [4]

Despite these challenges, remember that the space sector has been subject to disruptive innovation in the past. The last decade alone has seen the introduction of re-usable rockets, LEO broadband, and direct-to-device internet systems. As such, the constraints, while real, should not be considered ‘permanent’. They may potentially be resolved to a material degree, especially through the efforts of proven innovation champions.

![](images/bdba790850376c1b6798c2a5b34456d52bc101b9cc3d3e29165c648e0aba2623.jpg)

$^{2}$ GSMA, “The Limits of D2D: Modelling the extent of D2D connectivity”, February 2026, https://www.gsma.com/connectivity-for-good/spectrum/wp-content/uploads/2026/03/The-Limits-of-D2D-v2.pdf, accessed 20 April 2026

![](images/5983af02ebe0f3b1327cfc462354b6d7772bf4600a12122bae7904154317e61c.jpg)

# Implications for MENA: Connectivity enabler, resilience mechanism, or complementary add-on

D2D is not yet commercially available in any MENA country, but momentum is building. Bahrain, for example, has approved D2D, though not yet made it available. By 2030, the number of D2D users across MENA is estimated to reach $\sim 6\mathrm{M}^3$ , in a population of $500\mathrm{M}+$ .

As the technology gains traction in the region, it is likely to function as either a resilience overlay or a primary mode of connectivity, depending on the country. D2D is predicted to be relevant for a range of use-cases, including:

\- B2C remote and border zones: desert ranges, off-road safety, and remote tourism

\- Tool for resilience: civil security, disaster response

$^{3}$ \~100M global D2D users, prorated to MENA

• B2B IoT: Energy infrastructure, logistics nodes

However, the relative uptake will significantly vary by country, based on the levels of existing terrestrial coverage, D2D affordability, and population concentration in urban areas. As a result, three archetypes are predicted to emerge (Exhibit 1):

A) LEVER TO BRIDGE THE CONNECTIVITY GAP
A few countries with large rural populations and limited terrestrial coverage and affordability may be able to leverage D2D as a lever to bridge the connectivity gap. However, the uptake will depend on service providers reducing costs to improve affordability, finding the right balance between demand (uptake) and supply (price) – as the connectivity gap for consumers is generally high in markets with low ARPUs.

## B) COMMERCIALLY ATTRACTIVE (NOT NECESSARILY SUFFICIENT) DUE TO SCALE

NECESSARILY SUFFICIENT) DUE TO SCALE
In countries with better terrestrial coverage and affordability, but large rural populations, D2D can provide a meaningful alternative on a case-by-case basis (e.g., limited period add-ons, very niche geographies, emergency lines, etc.). But due to the scale of customers and relatively affordable services, D2D is expected to be a commercially attractive business model for operators and local telcos.

C) COMPLEMENTARY SERVICE BACKUP
For the remaining MENA countries – which operate near-universal mobile networks (e.g., very high 5G coverage of the population, with best-in-class speeds in GCC) $^{4}$ – D2D will be a complementary add-on, used for tourism, ubiquitous connectivity, and industrial digitalization.

## EXHIBIT 1

# Three MENA D2D uptake archetypes are expected to emerge

## MENA network coverage score (GSMA) vs. rural population

Comparing mobile connectivity coverage with rural population across MENA countries

![](images/e9bd067b341dc8c7445bb333eab52d7bce78ba7d5cb7df382852803e69022ad6.jpg)

D2D also has the potential to become a key resilience overlay. Its attractiveness in this respect is highlighted by the current geopolitical threats to public infrastructure and connectivity backbones, like sub-sea cables in the Strait of Hormuz. In addition, D2D can create a competitive advantage for telcos by strengthening their service offerings and reducing the need for last-mile infrastructure investments to expand coverage. Together, these benefits make the technology an attractive proposition for adoption - equally, if not more, than its direct economic benefits

$^{45}$ out of the Top 10 on Ookla Speed Test index for mobile are GCC countries

![](images/4e1ad61470472547fbf13795fbb341c9233aca1335389908b771227d08c09272.jpg)

# Immediate actions for governments and telcos: Thoughtfully integrate and leverage the emerging technology

In summary, while there are constraints, direct-to-device internet systems are growing rapidly in capability, availability, and potential. Given the current geopolitical risks and longer-term opportunities, the question for MENA governments and telcos is twofold: what will an integrated telco/D2D world look like, and how can we make the most of it?

Government leaders are invited to assess and consider accelerating their adoption of direct-to-device internet systems. Rapid action could help to secure resilient connectivity for their residents in the short-term. Governments may enable this

through the national telecommunications champion partnering with D2D providers, while rapidly transforming policy and regulatory frameworks to accommodate the technology.

Local telecommunications operators can initiate partnership discussions to capture the new opportunities. They are expected to remain firmly in control of customer relationships and orchestrate the service provisioning. This stems from their access to the spectrum required for direct-to-device connectivity (in the short-term, until IMT-adjacent MSS spectrum becomes the global norm).

However, D2D (and more broadly, satellite communication) carries far-reaching implications for both governments and telcos. If the technology advances over the long term, it could challenge last-mile segments in the terrestrial backbones. With this in mind, governments may consider short-term regulatory tools to protect their terrestrial infrastructure investments while evaluating their long-term connectivity investments and aspirations. India, for example, employed a duration cap, issuing Starlink a 5 year license. The goal for the end-user is a continuous and seamless fabric of connectivity, merging terrestrial and space-based technologies.

![](images/7d63cb147280eacefa8696c0a098780d282275062c882f5e0c9beb0fe3fd52b5.jpg)

## About the Authors

![](images/79e7c65f8ddcffcc94c59462635260e963cf5555b1195ee3bfdd776e1781b098.jpg)  
Ruediger Schicht
Managing Director and Senior Partner
Schicht.Ruediger@bcg.com

![](images/214250a03fb31b48866f99d9b022b0b6c82238992f0368e986cbbd20264b98cc.jpg)  
Thibault Werle
Managing Director and Partner
Werle.Thibault@bcg.com

![](images/4d4e3775460cc2e10d754b206ccdc7883053ba903a51431486a5b64ce26261ae.jpg)  
Marc Nasr
Managing Director and Partner
Nasr.Marc@bcg.com

![](images/997658af186ffeda81ca5d2d4b9d149bbcb6c27e3aadc8cfcf1f1f7b3a2c5acc.jpg)  
Hamza Najmi
Principal
Najmi.Hamza@bcg.com

Acknowledgments

![](images/ce2f6d0591dd4c8308708abcaf98f687d1a9efdf6dd4f89d9e351ad8ea4d4ccb.jpg)
"""
