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
# WHAT'S NEW AND NEXT FOR M&A IN AFRICA

By Seddik El Fihri, Othman Omary, Jesper Nielsen, Patrick Dupoux, and Alexis Bour

A FRICA IS A CHALLENGING region in which to execute successful mergers and acquisitions (M&A) for many reasons, but it is also one of the fastest growing and evolving parts of the world. Although Africa's recent GDP growth has slowed because of falling oil and commodity prices, and the coronavirus pandemic, both of which have hit its largest economies hard, now is the time to consider the long view of the continent's M&A investment opportunities.

Our analysis of Africa's M&A market activity and performance over the past decade, across countries and industries, reveals five trends that we believe can serve as critical guides to future investment strategies. We expect that these trends will become even more pronounced, and some will accelerate:

\- African-led acquisitions on the continent are rising.

\- More Africa-focused private equity (PE) investors are emerging.

\- Technology startups are attracting multiple investors.

\- African integration makes regional platform plays a reality.

\- State-owned enterprises may soon be open for private capital again.

Powered by those trends and overall GDP growth, M&A deal value rose at a compound annual growth rate of 15% from 2000 to 2015. That 15-year M&A growth streak ended abruptly; the annual compound growth in the value of African M&A fell by 21% between 2015 and 2019.

Despite negative 2020 GDP forecasts for most African countries, we expect that dealmaking activity on the continent will pick up ahead of the recovery in GDP growth. Indeed, an earlier-than-expected M&A revival in Europe in the third quarter of 2020 suggests that, even with the uncertainty around COVID-19, an M&A recovery globally has begun. We anticipate similar resilience in Africa.

Five M&A Trends in Africa
Hard commodities, oil and gas, and telecoms (Africa's smartphone and mobile payments markets are among the world's fastest growing) accounted for more than 50% of M&A value from 2016 to 2019. Tech opportunities in financial, health, agriculture, and energy-related services are among the main engines accelerating this activity. For example, in African countries on BCG's Middle Billion list, urban business and financial centers are blossoming, and first-generation African tech entrepreneurs are launching startups in need of local and global capital. Moreover, financial hubs such as Casablanca Finance City in Morocco connect the ecosystem of M&A players (corporate, law firms, private equity firms, financial institutions, and consultancies).

Meanwhile, the five trends we've identified as significant markers of activity and opportunity in Africa's M&A market over the last decade remain strong.

1. Rise of African Acquirers. Historically, non-African multinationals have been the dominant players in Africa. Today, many more local African entrepreneurs with professional capabilities, ambition, and technical skills are launching fast-growing companies competing against multinational corporations. From 2012 to 2019, African acquirers' share of deal value grew about 5% per year, although the average value of foreign investors' deals was twice that of African investors (\$60 million for non-African versus \$30 million for African). The African Continental Free Trade Area (AfCFTA) has been a significant driver of this activity. As we noted in our 2018 report, Pioneering One Africa, the AfCFTA and the economic integration of Africa has been a long time coming. It is also critical to Africa's future development and standing in global markets.

2. Growth of Africa-Based PE Funds.
Development institutions pioneered private equity investment in Africa in the early 1990s. Private equity investors followed. In the early 1990s, there were a dozen Africa-based funds with a total of \$1 billion under management. PE deal vol-

ume in Africa has been growing at about 6% per year since 2012. By 2016, there were more than 200 funds with upward of \$30 billion under management. A surge of private capital to Africa in 2016, just as the drop in commodity prices slowed economic growth across the continent, raised questions about the risks. We argued then, and remain confident now, that Africa holds great promise for private equity investors. The region’s rapidly expanding companies can absorb immense foreign investment and generate high returns for investors. Africa also needs private capital to fund its continued growth. From 2014 to 2019, the Africa Venture Capital Association reported 613 deals totaling \$3.9 billion, with 2019 alone recording \$1.4 billion of those transactions. The majority of those deals happened in South Africa, Kenya, Nigeria, Ghana, and Egypt. Interestingly, the most successful PE firms happen to be African, while global firms have struggled to adapt their model to the African context.

3. Attraction of Technology Sector Startups. M&A tech trends in Africa is consistent with what is happening globally. Fundraising for tech players increased by 64% per year from 2015 to 2019, driven mainly by investments in fintech, with a focus on financial inclusion. Startups in three countries—Nigeria, Kenya, and South Africa—captured 80% percent of those funds.

4. Developing and Securing Pan-African Platforms. Regional markets and multi-country roll-ups are opening up more opportunities for African acquirers and foreign players. The purpose of the multi-country platform is to create scale, hedge country risk, and capture industry synergies and operational cost efficiencies.

5. Revival of State-Owned Portfolio Activity. At the end of the 1990s and early 2000s, privatization was the main driver of government M&A. But since 2006, no privatization over \$1 billion has launched. We expect a reversal of this decline in government M&A activity for several reasons, starting with COVID-19 economic recovery interventions.

## The Effect of COVID-19 on African M&A

In June 2020, BCG surveyed 50 CEOs about the state of the M&A market in Africa. A full 80% of respondents reported that COVID-19 has disrupted their M&A agendas, including deals that were frozen or delayed. But they also said their rationales for being players in this market have not changed, although the pandemic's impact on their outlook is evident. For example, 83% percent of respondents said they were seeking “growth opportunities” before COVID-19, versus 71% in a post-COVID environment. Rationalization strategies, including divesting noncore assets or exiting a weak sector or a low-performing geographic region, jumped from 11% to 22%.

Exhibit 1 shows how some historical trends are accelerating faster than others due to COVID-19 and depending on the industry. For instance, pan-African platforms capture value when profits are diminishing and the economy is weak. A platform's geographic diversification play is also an effective way to neutralize country risk exposure. COVID-19 is also amplifying the potential benefit of building and securing pan-African platforms to mitigate country risk, find synergistic opportunities, and achieve scale quickly.

Smartphone and digital financial services are examples of two tech services reinforcing the growth of the other and growth in M&A. COVID-19 has put a spotlight on cashless transactions as a way to reduce the virus transmission risk associated with bills and coins. MFS Africa, a South Africa-based pan-African mobile payments hub, recently acquired Beyonic, a Uganda-based mobile payment technology services provider. Beyonic, which calls itself a provider of “cashless” transactions services, was founded in 2006 by a young software engineer and today serves clients in multiple African countries.

The rapid rise in remote work and virtual schooling is another COVID-19 effect stimulating technology investment opportunities. In the education sector, government action to keep K-12 schooling happening at home is significantly accelerating edtech digital innovations.

The economic fallout from the pandemic is also pushing governments to, on the one hand, shore up state-owned enterprises in strategically essential industries. On the other, governments may decide to privatize state assets to generate funds.

Multinationals seeking to lessen the risk in their portfolios could temporarily slow their activity in Africa and refocus on other regions. This would create specific opportunities, and white spaces, for African investors. Some private equity firms will be especially well-positioned to benefit if this happens.

EXHIBIT 1 | COVID-19's Impact on Historical M&A Trends, by Industry  
![](images/5811957b50b3c5fa661e468d61aac7d08d140e0ef879f6dbf98738613fca4079.jpg)

So far, the drop off in deal activity in Africa due to COVID-19 seems to be following a similar decline and recovery pattern to what we have observed following several global economic disruptions since 2000. (See Exhibit 2.) We expect a sharp fall in volume and value, possibly 40% in 2020-2021, but followed by a gradual recovery of deal volume within 18 to 24 months, and a return to 2019 total value within three to five years.

## Where African M&A Is Headed Post-COVID

Half the respondents to our M&A survey said they want to restructure their portfolios within the next five years. The motives that drove activity before the downturn will be roughly the same (70% finding new growth, 22% consolidating, and 7% acquiring new capabilities). Our own analysis captures these trends in six strategic archetypes. (See Exhibit 3.) Certain archetypes will be more prominent in some industries than in others. For example, before the pandemic, we were seeing more pan-African “grow the core”

deals emphasizing scale, synergies, and efficiencies in financial services. South African insurer Sanlam, Ltd., acquired 100% of Morocco Saham Finances in three deals between 2016 and 2018. The acquisition of Saham Finances gave Sanlam a footprint in 33 African countries, making it the continent's largest insurer.

We expect to see more pan-African platform deals in financial services as well as mining and health care. For example, in 2020, Endeavour Mining announced acquisitions of two mining companies with operations in West Africa. These acquisitions boost Endeavour's scale, making the company the largest gold producer in West Africa, and the $15^{\text{th}}$ largest in the world.

An investor partnership announced in November 2020 involving the private equity firm Development Partners International (through its ADP III fund), the CDC Group (the UK's publicly-owned impact investment firm), and the European Bank for Reconstruction and Development will create the first of its kind \$750 million biopharmaceutical pan-African platform. The platform will leverage a manufacturing and R&D center of excellence in India to strengthen its African manufacturing operations while capturing synergies from centralized supply chain management and business development.

EXHIBIT 2 | Africa's M&A Market Responses to Global Economic Shocks 2000-2020  
![](images/b1b8daa778038a0d4cbd622ecf2ade2bfbcf370a5d09b02fdb62ced29b9c537d.jpg)  
Sources: Zephyr; Bureau Van Dijk; S&P Capital IQ. 1 January to September 2020 values.

Source: BCG analysis.

<table><tr><td>STRATEGIC ORIENTATION</td><td>ARCHETYPE</td><td>RATIONALE</td></tr><tr><td rowspan="2">SAVE THE CORE</td><td>1 Shrink to value</td><td>Divest noncore assets to preserve and refocus on the core</td></tr><tr><td>2 Protect the too-big-to-fail1</td><td>Save nonprofitable companies with positive externalities for the country through privatization or, potentially, nationalization</td></tr><tr><td rowspan="2">GROW THE CORE</td><td>3 Consolidate locally</td><td>Acquire direct competitors to grow scale and increase market share and/or boost cost efficiency</td></tr><tr><td>4 Set up a pan-African platform</td><td>Acquire direct competitors crossborders to mitigate country risk while enhancing regional capabilities and market access</td></tr><tr><td rowspan="2">EXTEND THE CORE</td><td>5 Integrate on value chain</td><td>Integrate upstream or downstream to capture synergies and secure supply chain</td></tr><tr><td>6 Enter adjacencies opportunistically</td><td>Invest selectively in (distressed) assets to take strategic options, integrate on value chain, and reposition portfolio</td></tr></table>

$^{1}$ Archetype 2 is specific to government assets and direct foreign investment.

BCG's 2020 research on M&A markets globally shows alternative deals (joint ventures and alliances) have seen a surge in popularity in recent years. Companies are using alternative deals to gain access to capabilities that have helped with pandemic-related issues while continuing to respond to ongoing trends such as technology-driven disruption and the convergence of industries.

## The Long Game of M&A in Africa

Africa's slice of the global M&A market is relatively small—about 2% of the \$3.1 trillion global M&A market in 2019—but it is a solid alternative to other regional markets where growth is slowing. Still, the continent remains one of the most difficult places in the world to do business. Almost 90% of buy-side M&A decision makers in our survey said that managing uncertainty—economic volatility and other country risks—is their primary challenge.

The pandemic simply adds another layer of complexity. Sixty percent of respondents anticipate approaching acquisitions more selectively. In our view, the winners will

adapt quickly to new realities (sectors and archetypes). Cash capabilities will of course be critical drivers to carry out corporate M&A agendas.

Ultimately, there are good reasons to be optimistic about Africa's future and the future of the region's M&A market. Africa's youthful demographics and fast-growing consumer class bode well for bold investors. Economic integration through the AfCFTA also creates a major opportunity to help African countries diversify their exports, accelerate growth, and attract foreign direct investment. Significant investment will be needed in Africa to meet rising consumer demand for goods and services, to continue building basic economic infrastructure, and to meet sustainable development goals on climate-change mitigation and poverty reduction.

To succeed in Africa's promising and challenging M&A environment, investors will need to be prudent, adaptable, and bold. Incorporating the five trends driving M&A in Africa into decision making going forward can provide guidance and guardrails for investing in the future of this complicated continent.

## About the Authors

Seddik El Fihri is a partner and director in the Casablanca office of Boston Consulting Group and the head of the BCG Transaction Center for Africa. You may contact him by email at elfihri.seddik@bcg.com.

Othman Omary is a managing director and partner in BCG's Casablanca office and a member of the firm's Financial Institutions practice. You may contact him by email at omary.othman@bcg.com.

Jesper Nielsen is a managing director and senior partner in BCG's London office and leads the firm's Social Impact practice as well as BCG's business in M&A and post-merger integration in Western Europe, South America, and Africa. You may contact him by email at nielsen.jesper@bcg.com.

Patrick Dupoux is a managing director and senior partner in the firm's Casablanca office and is head of the BCG Africa system. You may contact him by email at dupoux.patrick@bcg.com.

Alexis Bour is a managing director and partner in BCG's Johannesburg office and is a core member of the firm's Industrial Goods practice and the firm's TURN unit. You may contact him by email at bour.alexis@bcg.com.

## Acknowledgments

The authors wish to thank Josephine Parmentier, Amine Menouni, and Alexandre Clauzet for their research, analysis, and contributions to this publication.

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation—inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact.

To succeed, organizations must blend digital and human capabilities. Our diverse, global teams bring deep industry and functional expertise and a range of perspectives to spark change. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures—and business purpose. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, generating results that allow our clients to thrive.

© Boston Consulting Group 2021. All rights reserved. 1/21

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
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
