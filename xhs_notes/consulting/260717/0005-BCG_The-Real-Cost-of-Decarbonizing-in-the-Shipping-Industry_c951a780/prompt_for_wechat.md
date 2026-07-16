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
![](images/d505f9eef68c1408d7440b41bc6addf36942f65ac4f54843788742a3fc13c3ac.jpg)

SHIPPING INDUSTRY & MARINE PORTS

# The Real Cost of Decarbonizing in the Shipping Industry

By Peter Jameson, Ulrik Sanders, Camille Egloff, Mikkel Krogsgaard, Alex Dewar, Laurids Schack, and Daniel Caceres Larsen

ARTICLE MARCH 13, 2024 8 MIN READ

The maritime industry stands at the forefront of global trade, playing a pivotal role in connecting markets and fostering economic growth. Yet

despite being a highly efficient form of transporting goods, shipping is also responsible for roughly 3% of global carbon emissions. If the maritime industry were a country, it would rank among the top ten emitters worldwide a stark reality that underscores an urgent need for improvement to support global decarbonization efforts.

![](images/8a6e395ad34afecf69ef09032004481cec4c67a4daaad8d9bff56edbfb0c21bb.jpg)

On the positive side, for an industry that has long been perceived as an environmental laggard, 2023 marked a turning point. Key developments that will help enable decarbonization included:

\- Enhanced Regulatory Frameworks. The tightening of regulations by both the International Maritime Organization (IMO) and the EU have deepened the decarbonization conversation.

\- Technological Innovations. Breakthroughs on both engine designs and efficiency-enhancing mechanisms are redefining the energy efficiency potential of shipping.

\- Higher Availability of Alternative Fuels. The increased availability of biofuels and other clean fuels in ports worldwide is expanding fuel choices, although still not at the scale needed.

\- Corporate Commitment and Action. A rise in corporate commitment, demonstrated by the growing number of dual-fuel orders, reflects a more robust push toward environmental responsibility.

In BCG’s third annual Shipping Decarbonization Survey—a study aimed at assessing the readiness of shipping customers to pay a premium for green transportation methods—we engaged 125 decision makers in 2023. These survey participants included heads of logistics, supply-chain directors, and other executives who determine cargo owners’ choices of maritime providers. Among our principal findings is that the shipping industry is still struggling to convert commitments into measurable actions.

How can carriers speed up this process in the overall drive toward net zero? Although the barriers to progress are high, we see clear navigational paths that can overcome them.

## The Problem: Momentum Is Growing, but Barriers Remain

Green shipping is broadly gaining momentum, with significant developments in both the public and private sectors. The same can be said for related technologies and the development of alternative fuels. Our 2023 survey showed that more than 80% of shipping customers are prepared to pay a premium for green shipping, with the average premium currently at 4%—an increase of 33% from 2022 and double the rate of 2021. (See Exhibit 1.) Nonetheless, the projected growth rates still fall short of the levels required for significant decarbonization.

Exhibit 1 - Cargo Owners Are Willing to Pay Higher Premiums for Green Shipping, but Not Enough to Reach 2050 Decarbonization Goals

WtP Premium
How much are you willing to pay extra for carbon-neutral marine shipping, today?

![](images/35cce2daa13caa709b246913561fbbddd59d29eb1ed068c574e697aabeb678aa.jpg)  
WtP Premium in the future
Do you in the near future $^{1}$ expect to be more willing to pay extrafor zero carbon marine shipping, compared to what you are willing to pay today?

![](images/f096b835ecef6f51ca2b354f25082a427fe06ec929258452e7cdbffaf6077f6e.jpg)  
Sources: BCG Shipping Decarbonization Survey, June 2021, N = 125; BCG Shipping Decarbonization Survey, September 2022, N = 125, BCG Shipping Decarbonization Survey, September 2023, N = 125.  
Notes: 2021: 71% willing to pay a premium; 2022: 82% willing to pay a premium; 2023: 82% willing to pay a premium; WtP = willingness to pay. $^{1}$ Within five years from now.

According to a study coproduced by BCG and the Global Financial Markets Association (GFMA), a premium of 10% to 15% will be necessary to achieve complete decarbonization of the shipping sector by 2050. In the shorter term, the premium might need to be as high as 30% to 40% before the production of alternative fuels can be scaled up effectively. As of now, only a select group of companies is willing to pay a premium exceeding 10%.

Overall, we have identified three major barriers that continue to impede the progress of green shipping.

Subscale Alternative-Fuel Production. A 2023 BCG study coproduced with the World Economic Forum (WEF) indicated a rising demand for alternative fuels, as demonstrated by the order of more than 180 dual-fuel ships. However, over 95% of projects focused on producing these fuels are still in the pre-final investment decision (FID) stage. The study outlines 10 key challenges to scaling up the zero-emission fuel supply, including issues related to macroeconomics, regulation, supply chains, and organizational structures.

Shifting Regulatory Requirements. Although 2023 witnessed significant regulatory actions by the IMO and the EU, the regulatory landscape remains in flux particularly regarding vital decisions on fuel standards and the size and timing of a potential carbon tax. Such shifting regulation can prompt companies to stay on guard and remain hesitant to invest rapidly and confidently in green shipping.

A Budget Gap Among Cargo Owners. Although more than 60% of our survey respondents have committed to reducing Scope 3 shipping emissions—those for which a carrier is indirectly responsible throughout its value chain but does not generate itself—less than half report having an adequate budget to achieve their targets. Clearly, the gap between admirable ambitions and required financial resources is still fairly wide.

## The Solution: Search Out Growth Areas and Take Action

The present state of the maritime industry calls for a shift from mere promises to tangible investments in green initiatives. The key enabling developments are robust, and commitments from both public and private sectors are in place. The real challenge lies in converting these commitments into concrete actions. In this crucial phase, the cargo carriers cannot wait for optimal regulations to take shape or for customers to take the lead. They must proactively identify and seize opportunities for growth in green shipping. There are two principal imperatives.

Capture untapped segments. We believe that untapped pockets of growth in the market can finance the development of a viable and sustainable green shipping product. But carriers must first identify prospects that are willing to invest in carbon-neutral transportation. Overall, current WtP premiums vary widely both by industrial sector and level of green commitments. (See Exhibit 2.)

Exhibit 2 - WtP Premiums Vary Widely by Industrial Sector and Level of Green Commitments

Companies across all sectors willing to pay average premium of 4%
Avg WtP of companies by sector and commitment types (i.e., with or without Scope 3) in 2023

% premium vs. current marine shipping fuel

![](images/4bd62b1a1806c0bbc1c3bf0aac1f8fab64bffa5be6ffa7bc484a3cd9087da74b.jpg)  
Source: BCG shipping customer survey 2023, n = 125.  
Note: WtP = willingness to pay.  
$^{1}$ WtP of companies with Scope 3 commitments vs. WtP of companies without Scope 3 commitments.

Our survey has revealed several promising segments:

\- Customers with Scope 3 Commitments. Roughly 60% of respondents have Scope 3 commitments, showing an average WtP premium of 5.2%, compared with 2.3% among those without commitments.

\- Customers That See Regulation as an Opportunity. About 40% of respondents view tightening regulations as an opportunity and are willing to pay a 6% premium for green shipping (compared with 3.5% among those who see regulations as a threat). There is thus a significant opening for cargo carriers to collaborate with these forward-thinking customers. Notably, in the basic materials sector, customers that are committed to Scope 3 emissions targets show a WtP premium of 5.7%, compared with only 0.5% among those without such commitments.

\- Industry-Specific Customers. The automotive and health care industries exhibit the highest WtP premiums, at 6.1% and 6.0%, respectively.

\- Region-Specific Customers. Europe leads with a WtP premium of 5.1%, significantly higher than North America, at 3.3%, and South America, at just 1%.

\- Combined Customer Groups. When combining specific groups, such as European food and drinks customers with Scope 3 targets, the average willingness to pay reaches a premium of $11.3\%$ —a level closer to that truly needed to decarbonize the shipping industry.

Be an early mover. The unexploited commercial opportunities in green shipping are fundamentally the result of a gap in market offerings and customer needs. Despite a clear willingness among many cargo owners—especially those with Scope 3 commitments—to pay a premium for green shipping, they often face limited access to such options. Our survey revealed that only about 35% of customers have been presented with green shipping options, with the percentage slightly higher (at around 40%) for those with Scope 3 commitments.

This disconnect may stem from two primary issues. First, shipping companies currently providing green transportation might not be effectively segmenting their target market, or they may lack a robust go-to-market strategy. Second, companies not yet offering green options may be unaware of the existing demand from their customers, causing them to miss out on substantial business development potential.

Companies not yet offering green options may be unaware of the existing demand from their customers, causing them to miss out on substantial business development potential.

Such a scenario presents a lucrative chance to capture market share for early movers. By developing a strong go-to-market strategy that clearly identifies and serves customers that are ready to invest in green shipping, cargo carriers can secure a sizable competitive advantage. At the same time, they can help drive the industry's progress toward sustainability. This type of proactive approach is critical to the quest for a greener and more sustainable maritime future.

## Strategic Recommendations for Carriers

At this pivotal moment in the maritime industry's shift toward sustainability, it's mandatory for shipping companies to successfully develop and market green products. Based on the overall BCG framework for successfully navigating climate change and sustainability issues, we see a number of imperatives for shippers.

Develop a holistic go-to-market strategy for green shipping. To effectively launch green shipping products, carriers need a comprehensive, strategic approach that goes beyond merely creating an operational product. They must also align their offerings with market demands and customer needs. Key aspects of this strategy include the following:

\- Target Segmentation. Identifying and focusing on customer segments that are willing to pay a premium for green shipping is critical. Forging an effective strategy that includes evaluating various segments for business potential, engaging early adopters, and exploring customer partnerships to co-invest and codevelop products will help carriers tailor their offerings.

\- Pricing Strategy. A nuanced pricing strategy is essential to scaling green products successfully—starting with early adopters that are most willing to pay a premium and progressively targeting mainstream buyers. Such a domino strategy should be shaped based on the unique characteristics and needs of each customer segment.

\- Sales Channel Development. Given the growing trend among cargo owners toward digital purchasing, it’s important to establish diverse sales channels that include digital platforms. This approach not only aligns with evolving purchasing behaviors but also ensures greater transparency on emissions and costs, a characteristic that is increasingly valued by customers.

Collaborate across the value chain. The 2023 BCG/WEF report highlights the substantial benefits of collaboration between fuel producers and their customers to develop a green-fuel value chain. This partnering approach significantly reduces risks and facilitates the launch of large-scale fuel projects, as evidenced by the benefits below:

Collaboration between fuel producers and their customers to develop a green-fuel value chain reduces risks and facilitates the launch of large-scale fuel projects.

\- Pooling Expertise and Sharing Risks. Collaboration is instrumental in combining expertise, sharing risks, and managing costs, thereby driving demand for green transportation. About 70% of cargo owners indicate a willingness to join buyers' clubs for green fuels, with 31% definitely willing and 41% considering it (particularly if their competitors also participate). (See Exhibit 3.) Such clubs are especially advantageous for smaller customers with contractual limitations, as these groups help secure long-term offtake agreements (which bind counterparties to buy or sell fuel in the future). The creation of the Zero Emission Maritime Buyers Alliance, a coalition established to fast-track commercial deployment of zero-emission shipping, highlights the power of bundling demand to spur supply.

Exhibit 3 - Roughly 70% of Cargo Owners Are Willing to Join Buyers' Clubs for Green Fuels

Scope 3 commitments with access to green shipping
Do you have access to green shipping?
(Respondents with Scope 3 commitments)

Respondents in contact with green shipping providers
To source green transport, would you be interested in joining a "buyers club"?

![](images/294e8c67ff2c22371241d2a2ce4e448d867440de8a4a478d072f0513a981bab1.jpg)  
Note: WtP = willingness to pay.  
Sources: BCG Shipping Decarbonization Survey, June 2021, N = 125; BCG Shipping Decarbonization Survey, September 2022, N = 125, BCG Shipping Decarbonization Survey, September 2023, N = 125.

\- Cost Sharing. Spreading out costs among industry participants is also important, particularly as initial green shipping projects are likely to be more expensive until economies of scale and learning curves reduce the required spending. Sharing costs both with customers and fuel producers makes it more feasible for shippers to commit to green initiatives. A prime example is the partnership between Amazon, Inditex, and Maersk that utilizes Maersk’s ECO Delivery ocean logistics service.

\- New Funding Mechanisms. The BCG/WEF report also highlights the need for alternative funding mechanisms to mitigate offtake risks. The current gap in appropriate financing options can be bridged by innovative financial structures such as minimum revenue or capacity payments, dynamic contract pricing, and equity stakes for strategic buyers. Such methods, coupled with a mix of senior and junior debt, special-purpose vehicles, and government incentives, can provide the necessary financial backing.

\- Transparency. Approximately 40% of stakeholders see the lack of traceability and trust in emissions reductions as a major investment barrier in green shipping. Transparency in emissions and costs is crucial to strengthening market confidence and upholding commitments to green practices.

Proactively take key transformational steps. Thoroughly preparing an organization for transformation is vital to success. The key elements for readiness involve these action steps:

\- Enable leadership excellence. Shippers need to enable leadership in spearheading change, emphasizing skills development, and aligning incentives. Building a culture that is supportive of sustainability objectives is crucial for long-term viability.

\- Optimize organizational structure and human resources. Securing the necessary talent and establishing accountable governance structures are table stakes for true transformation. Defining clear KPIs and targets, along with rigorous progress tracking, will facilitate effective implementation.

\- Drive digital capabilities. Carriers need to develop a comprehensive digital infrastructure that enhances transparency and provides clear insights into the organization’s emissions. This step is pivotal to establishing productive management and accurate reporting on sustainability efforts.

\- Align financial incentives. Financial strategies should be in harmony with the company’s sustainability goals. Implementing mechanisms such as internal carbon taxes and focusing on sustainable capital management are effective ways to reinforce commitment to green objectives.

\- Sharpen marketing and communication. Companies should adopt robust communication strategies, both internally to align the workforce with sustainability goals and externally to publicly position the company as a leader in green initiatives. Clear and user-friendly communication enhances reputational value and supports market positioning.

By following these strategic recommendations, carriers can not only champion the cause of green shipping but also leverage it as a significant business opportunity—one that contributes to a sustainable future and positions cargo carriers as leaders in the green transformation of the maritime industry.

The maritime industry stands at a key juncture. It is facing the dual challenges of taking on environmental responsibility and seizing the business opportunities presented by green shipping. This inflection point demands strong leadership and a collaborative spirit among customers seeking green solutions and companies that are capable of delivering them.

For cargo carriers, the current moment offers a unique chance to lead the way in sustainability. By developing and marketing green transportation products, backed by effective go-to-market strategies, they can significantly contribute to a more sustainable future.

Long-term success will not come easily, of course. It calls for bold, early-mover leadership. But by acting decisively, shipping pacesetters can make great progress in steering their own industry and the greater business community toward a truly net-zero future.

## Authors

![](images/54a0aceca22e9b8771eb828bd3ad034f88c2e8600757dd9cfa3cab598023347a.jpg)

![](images/6f10523c2cb0128444881d9e9c3d5ddf01f43ec13b1d881982b1a3344ed16832.jpg)

![](images/65044d886a6645d1000d1563a7178c518edc38b98b44ef2193ab9e6218b008d0.jpg)

![](images/ff469e558ef07c869f6a3540c155efd800ba712f73925958fd604b2251198cbd.jpg)  
Managing Director & Partner
Copenhagen

## Peter Jameson

![](images/d9c388e151ab2367c7845e57545eb693f14d3487d8edacd6805c68d056737edb.jpg)

## Camille Egloff

Managing Director & Senior Partner
Athens

![](images/4225efc351556b6b76825f0fa5f385289b708956eca1f77e179f342d20185288.jpg)

## Alex Dewar

Managing Director & Partner
Washington, DC

![](images/8176695dd524da96c2cc4c5a6b4e7eafc657238993afa968edc5583169f483f9.jpg)  
Daniel Caceres
Larsen

Consultant
Copenhagen

![](images/4e34a1dfbadc4494d078612ca01a2efd1df533a794b35855ea25d10496296bbd.jpg)

![](images/867b472e487e0b66d3b929fa108712605cfbbb7bd3b6250920e38e8e597db054.jpg)

## Ulrik Sanders

Managing Director & Senior Partner
Copenhagen

![](images/b5866f459bd6216f4175f2e5be3a708ddd11bbef2bfee48502b52c56f7b866b2.jpg)

![](images/bec9f6f6a3e99a9398337697e803bbfe2f1013dbca30cc5fded103bf7cb17cee.jpg)

## Mikkel Krogsgaard

![](images/e59dc0caacbf45fbeb658b808458cd878cb0a76acdc82410beb1ca60c70fa893.jpg)

Managing Director & Senior Partner
Copenhagen

![](images/b78ae51c3b5f3d4f7c93de4cfa0da05f66768c11c7ab4072767dc09cef5adbc4.jpg)

## Laurids Schack

Project Leader
Copenhagen

![](images/74a336e7f08f32bb4cd3ca0cf4811e02cb9802021b62cd8a71e322fd3178427f.jpg)

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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
