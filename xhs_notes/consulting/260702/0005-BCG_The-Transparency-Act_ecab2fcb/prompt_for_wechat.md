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
# BCG BOSTON CONSULTING GROUP

## About Transparency Act/Åpenhetsloven

The Transparency Act (Åpenhetsloven) was effective July 2022 and its purpose is to ensure companies respect human rights and decent working conditions throughout their supply chain and own operations. The Act applies to the Norwegian branch of The Boston Consulting Group Nordic AB.

## About BCG

Boston Consulting Group (BCG) is a global consulting firm that partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation - inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures, and business purpose. BCG's Norwegian branch office has approximately 221 employees and is seated in Oslo.

## Our policies and values

BCG's Code of Conduct $^{1}$ encapsulates our commitment to acting responsibly, backed by individual integrity and professional and ethical conduct. Integrity is at the center of who we are at BCG – as an organization and as individuals that make up the organization – we are committed to instilling bold, truth-telling leadership and we will not tolerate any form of human rights abuse in any part of our business. BCG's commitment to respecting internationally recognized human rights is further outlined in our Global Human Rights Statement $^{2}$ , which describes our expectations and approach across our operations and value chain.

Our Code of Conduct sets out that all colleagues in the BCG community are personally accountable for behaving in a manner that is professional, lawful, and serves as a bridge between our purpose, our values and our processes and policies. We encourage BCG colleagues to report any behaviors or activities that they believe to be unethical or unlawful either to a trusted member of staff or via our Ombudsman process. Our Code of Conduct is distributed annually to all staff who by return must confirm they understand and are compliant with the Code. We work in adherence to our company values, which include Integrity, Respect for the Individual and Diversity.

At BCG, we know our greatest asset is our people. We are committed to cultivating a respectful and inclusive workplace that supports wellbeing, ensures a safe and healthy working environment, and promotes continuous professional development. The branch is seen as having a positive work environment, and we are actively working to sustain and enhance it where needed.

## Risk assessment

When onboarding new vendors, we look for strong recommendations from current customers and online reviews, established companies where their provided services/goods shares BCG's vision on good quality – throughout the supply chain. Due to the nature of our business, we purchase goods and services from a range of sectors and countries, although mainly in Norway. Our main vendors would be related to professional services, IT and development and facility management.

Our vendors mainly consist of large and reputable companies, which we have a good overview of and dialogue with. In general, we consider the risk of adverse impacts on human rights or decent working conditions in our supply chain to be low. In particular, we consider our usage of Norwegian vendors as low risk for human rights violations due to inter alia the fact that they are contained by the same laws and reporting obligations, such as Transparency Act, as ourselves.

In industries, or geographical areas, known for a potential higher risk, we have particularly made sure to address our expectations to our vendors for them to ensure they have routines in place to ensure that human rights and decent working conditions are respected and that any risks are prevented or mitigated. One measure is by the distribution of our Supplier code of conduct. Our Supplier Code of Conduct (SCOC) $^{3}$ outlines the minimum requirements that suppliers must meet in order to do business with BCG. The SCOC forms the foundation of our systematic approach to cultivating a more sustainable and responsible supply chain. To that end, BCG includes a link to the SCOC in all of our standard supplier contract templates. The SCOC establishes requirements across four broad categories: business practices and ethics; labour practices and human rights; environmental regulations and protection; and protection of assets, intellectual property, and data.

It also delineates the process for suppliers to use in reporting on their compliance, as well as the range of potential BCG responses to suppliers' failure to meet SCOC requirements.

Our due diligence for the period of 1 January 2025 to 31 December 2025 has not revealed any actual adverse impacts or significant risks requiring concrete measures further to our general measures implemented. However, the work on human rights and due diligence is a continuous effort, and we therefore continue to develop and evaluate our measures and assessment criteria to capture any risk of human rights violation in our operations or among our vendors.

## Due diligence and our commitment

BCG expects its Suppliers to share its commitment to human rights, inclusion and the principle of non-discrimination in the workplace. Suppliers shall conduct their employment practices in full compliance with all applicable laws and regulations. As any violation to human rights is unacceptable to any BCG partner, we continuously monitor our vendors and validate, their provided services, on any risk measure.

## Grievance Communication Channels

Grievances can be reported through BCG's existing grievance mechanisms set out in our current Whistleblower Policy, which is available through the BCG Speak Up Line, found on the Company's Internal Navigator page, as well as on the Company's external website $^{4}$ . Internal BCG complaints may also be reported directly to any member of the Ombuds team as set out in the above-mentioned Whistleblower Policy.

This document is an English translation of the signed original.
"""
