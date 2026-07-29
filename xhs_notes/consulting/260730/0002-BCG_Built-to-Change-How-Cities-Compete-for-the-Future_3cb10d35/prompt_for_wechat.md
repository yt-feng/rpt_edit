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
## Built to Change: Cities of Choice 4.0

Global City Ranking

Full report

## Table of contents

![](images/e817d079bd1ce1ac81de22bde01d35da4d2458e5ccfd3776cbb2e6c6421ae013.jpg)

![](images/b871064f422a354014b71612486176e43cf55b22e0ebec8ea8581a80e69472c2.jpg)

![](images/d3b3219ae3a83f32241cc4a3852ee8fd34a6297b020f11c94dbd049074202430.jpg)

Section 1 - Our approach and key insights
Section 2 - Top 20 cities by dimensions
Section 3 - Ranking by groups
Section 4 - Key forward-looking themes
Section 5 - Appendix: ranking methodology

## Our approach and key insights

## Three editions of Cities of Choice have been published, and a fourth edition, Built to Change, was launched at World Urban Forum 13 in Baku in May

![](images/a31aa4322fc0b05edf922c3ca22665cfde461fba4ea3b642da8b8ab314283976.jpg)  
2019-2020

![](images/6c9a9877c316adac1045df4d913571d4983e44770afe0bd122d25ca4e224d531.jpg)  
2020-2021

![](images/2cca190ec49165255ebed171cdc5967e1d0608bdd6330f02014397b8af063c6f.jpg)  
2022-2023

![](images/9eaaeb1fa0aa6bb98c13206aa946c3146a487130cf536641225f8df9689f5a59.jpg)  
2025-2026
Deep dives

• Housing affordability

\- Longevity in the city - Online adepts - New AI and robotics wave and cities’ labor market

\- Connected cities

BCG's Cities of Choice 4.0 assesses cities across five dimensions of resident value proposition

• 80 cities

• 200+ indicators

\- 80% objective data

• 20% of data from survey of 24,000 residents

• 10 years longitudinal data

\- 5+ million data points

%

#

#

#

Speed of change

Engagement with governments

Social capital

Livability

Economic
opportunities

High speed of positive change outrunning residents' expectations across the other four dimensions of residents' needs

Governance favoring open and trusted dialogue with authorities where every resident can be heard and contribute to city development (e.g., responsiveness, confidence, and trust)

Conditions for social interaction, mutual respect, equality, and inclusivity (e.g., social connections; culture and history engagement; personal safety)

Affordability, accessibility, and quality of infrastructure and services (e.g., education, entertainment, recreation, goods and services)

Living standards and opportunities for professional realization (e.g., work and career opportunities, business opportunities, availability of resources)

## This edition also assesses 26 elements across five dimensions

![](images/740828e088686bffdb84cd745c56a9fc7ec1f1eacaf1c19429b1782a03959c06.jpg)

Economic opportunities

Opportunities for work, career, and earnings

Equality income

Opportunities for business

Availability of personal loans

#

Livability

Housing

Mobility

Medical care

Education and development

Public spaces

Consumption of goods and services

Entertainment and recreation

Ecology

Cleanliness and hygiene

Comfortable climate

Resilience to emergency situations

![](images/5cb74ebf4af2841e3ffca037802f0e7d24fd715611ef673c42348e147d892058.jpg)

Social capital

Social connections

Inclusivity and equality

Identity with culture and history

Safety

Engagement with governments

Ability to influence events

Government services

Business environment

![](images/c6bb13ace9f80cff002cd08f49e47eca578e22f9e812f94f45273110b43fb53d.jpg)

Speed of change

Speed of change in economic opportunities
Speed of change in livability

Speed of change in social capital

Speed of change in engagement with governments

## Cities of Choice 4.0 covers 80 cities

![](images/2594b6d70a52b71e632994d14d09680fd9b0b4eefa9cfe7a704ea6364b8bd3d8.jpg)

80 global cities included in the ranking, compared with 79 in the last edition (2023)

## Key insight: Speed of change is becoming a winning formula for the future

1. Urban competition has shifted from infrastructure to lived outcomes

\- Success is no longer measured by assets (roads, airports, utilities) but by what they deliver to residents

\- Cities compete on time saved, friction reduced, and quality of everyday life

• Focus has moved from technical performance to resident-level value creation

2. Value today means surplus time, richer experiences, and investable prosperity

\- Mobility = surplus time enabled by smart transport and seamless digital services

\- Comfort = depth and variety of life (culture, community, learning, nature, opportunity)

\- Prosperity = investable surplus, not just salaries but also real take-home life value after costs

## 3. Speed of change is the new source of sustainable advantage

## #

\- Residents compare cities in real time; expectations evolve quickly

\- Faster learning and adaptation drives stronger resident advocacy

\- High-advocacy cities win by consistently improving outcomes—and proving they can do so again

## Advocacy $^{1}$ rises fast in most cities

Leaders remained leaders with increased score. The leading reasons are high speed of change, cultural traditions. Significant increase in advocacy in European cities (potentially post-COVID effect) and, in particular, in Baku, Seattle, Frankfurt, Astana, Munich, Almaty, Austin, and Vienna. Slight drop in Guangzhou, Shenzhen, and Milan

![](images/2a6af7cd969b7a2aa589674d991dc3be624f9fb4f627a51fac87879d860c1572.jpg)  
1. Resident advocacy measured with five questions: 1) Are you satisfied to live in [City]? 2) How likely are you to recommend [City] to a friend from another city as a place to live and work? 3) Have you recommended or criticized [City] as a place to live and work in the last 12 months? 4) Do you see your children living in [City] 20 years from now? 5) Do you believe [City] will prosper in the future?

## A high advocacy score indicates residents' commitment to a city

Cities with higher advocacy also see a greater share of residents planning to stay in the foreseeable future Advocacy is not just an attitude—it reflects genuine commitment and confidence in a city’s long-term prospects, which is a strong foundation for economic and social prosperity.  
![](images/ad72630323cd5947f3ffb0b19bec5d5058dec6e343680922a6570735fdf202c7.jpg)

Higher advocacy aligns closely with higher overall resident satisfaction
Cities that score well on advocacy are those delivering consistently positive everyday experiences; advocacy captures both emotional attachment and quality-of-life outcomes.  
![](images/daa1c4c35164272cc8c1bd303a687794ff38e34602df49caeb66a6eb530839ce.jpg)  
1. Share of respondents staying in the city in foreseeable future: measured through share of respondents who selected “No, I plan to stay in [City] in the foreseeable future” to question, “Would you seriously consider relocation to another city / country?” 2. Overall resident satisfaction measured by average score of all opinion-based survey questions.

Online adepts $^{1}$ outperform other residents in advocacy across more than 70 cities  
![](images/a6a4d5e0aff4148d2a43aae0ac7a0033c182adfe8baeb2338a4f4e04f6fd665d.jpg)  
1. Residents who perform at least four of the following activities entirely online, with no more than two activities entirely offline.  
Activities include groceries, shopping, health care, fitness, entertainment (films, series, theatre, sports), banking and personal finance (paying bills, sending money, applying for loans, etc.), city government services (utilities, applying for permits and IDs, reporting city issues, voting, etc.).

## Section 2

## Top 20 cities by dimension

## Executive summary (I/III) Ranking results by dimension

## Overall

\- The West leads in economic and livability fundamentals; ME, China, and Central Asia drive the fastest change

\- Advocacy and citizen engagement rise across most cities, led by the ME and Asia; Europe and the US show moderate recovery from post-COVID sentiment lows

![](images/e64d78b44714e768ba76e16cd02a271448c057c2a7e0584b00819167dd2374f7.jpg)

\- Middle Eastern, Chinese, and Central Asian cities, led by Tashkent, show the fastest transformation over the past decade, especially in livability and economic opportunities

## Speed of change

\- Europe’s pace remains slower, though Zurich and German cities advance through improvements in social capital and engagement with governments

\- Top 10 in speed of change in engagement with governments are UAE and KSA cities

\- Top 15 led by European and US cities and Dubai; Doha drops on weaker ecosystems and business momentum, while Europe gains; Central Asia improves on reforms sentiment

\- Clear income-equality tradeoff: US cities earn more but are more unequal; EU cities are more equal but have lower income

![](images/361065703374fc4456c63f6c275e085fb0569f0fdb4f332c2a5fd54d7446a5bc.jpg)

\- Not all cities with strong business ecosystems translate them into higher incomes; even efficient performers can lose their income edge if business conditions stagnate

## Economic opportunities

• Business environment is driven by emergence of new coworking spaces (4.5x on average since 2021) and business incubators

\- Europe (except Istanbul) gained on new indicators: venture capital investment, airport connectivity, and economic land use score confirming strong fundamentals but also early-stage entrepreneur activity increased

• Sentiment on work and business opportunity availability improved across cities, notably in Central Asia

## Executive summary (II/III) Ranking results by dimension

## Overall

• Europe retains leadership (London, Zurich, Oslo); Shanghai and Central Asian cities rapidly close the gap - Developing cities get strongest gains in livability, and if trend continues, talent flow will be redirected strongly to developing cities in search for better living conditions

\- Housing affordability and mobility pressures intensify globally; education and health care gains support Europe’s lead and Asia’s catch-up

Housing: largest challenge across continents

• Higher per square meter prices (+25% in Europe and North America)

\- Increased mortgage rates (doubled in Europe and North America, +40% globally)

• Housing drives happiness and already now 62 cities out of 80 develop city-level housing affordability programs

Mobility: situation worsens despite talks about “new mobility”

![](images/cbe4899599ab042fc5fa60df7793323aa4bbd50149b01273ac055603679d502a.jpg)

\- Despite public transport initiatives, time to commute has increased by $6\%$ across all cities and growing number of cars (by $7.5\%$ from 2023) is the main contribution

• However, 15-minute city and public transport promotion initiatives start paying off and their adepts are improving (Vienna, Paris)

## Livability

Outdoor: conditions deteriorate despite physical improvements and high importance for residents - Air quality deteriorating: over 90% of cities show NO $_{2}$ levels higher than WHO guidelines; in 80% cities in ME and Asia, the highest PM2.5 and PM10

\- Europe and Canada lead globally in public and green spaces, with Europe holding 10 of the top 15 spots; ME lags in green zones; Riyadh, Tashkent, and Warsaw showed strong gains in access to public spaces

\- Despite continuous effort in public and green spaces, time outside decreased by 9.2%, while weight of public spaces in residents' needs is high in all cities

Initial traction on health span and longevity capital

\- Cities across all groups promote healthy lifestyles (55 cities) and prevention programs; high participation in wellness programs (56%) and telehealth access (80+%); in 80 cities, residents had checkups this year

\- Most cities introduced healthy lifestyle programs for older adults (92% participation in wellness programs among elderlies) to be socially and health-wise active and build longevity capital

## Consumption

\- US and European cities lead in offline retail density, while ME and Asia are very much behind. At the same time, they are leaders in ordering goods online, while US and European cities are outsiders. Accessibility of grocery stores: the first 30 are in Asia, ME, and LA $_{14}$

Note: $NO_{2}$ = nitrogen dioxide; WHO = World Health Organization; PM = particulate matter; LA = Latin America.

## Executive summary (III/III) Ranking results by dimension

## Social capital

• European cities rebound post-COVID, while Asian and Middle Eastern cities continue to lead on social connectedness and resilience

\- Inclusivity improves globally, with major gains in developing cities (Almaty, Cairo, Riyadh) and stronger accessibility across transport and employment

\- In social capital, cities are “departing” from countries and forming their own “social capital”

## Engagement with governments

\- Western cities still lead, but the Middle East is catching up quickly; Dubai enters top 10, while some Western cities (Rome, Milan, Budapest) decline

\- Technology penetration drives improvement: +20% feel able to influence decisions; 3x better at solving problems online; 2x more participation apps

\- Online adepts demonstrate stronger advocacy than general population; apparently work from home and online convenience create sufficient comfort for people to praise their cities

• Significant improvement in ability to influence events:

\- +20% increase in residents reporting that they feel able to influence decisions in their city

\- 3x improvement in ability to solve the most common city problems using online tools

\- 2x improvement in the availability of dedicated mobile apps that enable citizens to influence city development

## Results by dimension for 80 cities—top 20 cities

![](images/64b4aa1eb220fe695e66fab78c1ec40add43205205c3455b4eca7e2baf7b7443.jpg)

## Speed of change

<table><tr><td>City</td><td>Total dimension score</td></tr><tr><td>Shenzhen</td><td>92</td></tr><tr><td>Riyadh</td><td>91</td></tr><tr><td>Tashkent</td><td>88</td></tr><tr><td>Doha</td><td>87</td></tr><tr><td>Guangzhou</td><td>85</td></tr><tr><td>Shanghai</td><td>83</td></tr><tr><td>Mecca</td><td>81</td></tr><tr><td>Beijing</td><td>81</td></tr><tr><td>Jeddah</td><td>80</td></tr><tr><td>Mumbai</td><td>80</td></tr><tr><td>Dammam</td><td>79</td></tr><tr><td>Medina</td><td>77</td></tr><tr><td>Astana</td><td>77</td></tr><tr><td>Abu Dhabi</td><td>73</td></tr><tr><td>Bengaluru</td><td>72</td></tr><tr><td>Almaty</td><td>71</td></tr><tr><td>Jakarta</td><td>67</td></tr><tr><td>Delhi</td><td>64</td></tr><tr><td>Kuwait City</td><td>64</td></tr><tr><td>Baku</td><td>64</td></tr></table>

![](images/5bc03265f3079159b35c1d14c2a330f4212a87994081a1438564c32d192fc841.jpg)

## Economic opportunities

<table><tr><td>City</td><td>Total dimension score</td></tr><tr><td>London</td><td>81</td></tr><tr><td>Zurich</td><td>80</td></tr><tr><td>Paris</td><td>80</td></tr><tr><td>Atlanta</td><td>79</td></tr><tr><td>Dubai</td><td>77</td></tr><tr><td>Amsterdam</td><td>76</td></tr><tr><td>Frankfurt</td><td>75</td></tr><tr><td>San Francisco</td><td>75</td></tr><tr><td>Munich</td><td>73</td></tr><tr><td>Washington, DC</td><td>72</td></tr><tr><td>Austin</td><td>71</td></tr><tr><td>Seattle</td><td>71</td></tr><tr><td>Dublin</td><td>71</td></tr><tr><td>Oslo</td><td>70</td></tr><tr><td>New York City</td><td>70</td></tr><tr><td>Boston</td><td>69</td></tr><tr><td>Seoul</td><td>68</td></tr><tr><td>Copenhagen</td><td>66</td></tr><tr><td>Denver</td><td>66</td></tr><tr><td>Madrid</td><td>66</td></tr></table>

![](images/ef45610e3856baebed83574e7b48c22a4b8e96428086e203a11155a393daebef.jpg)

## Livability

<table><tr><td>City</td><td>Total dimension score</td></tr><tr><td>Zurich</td><td>74</td></tr><tr><td>London</td><td>74</td></tr><tr><td>Oslo</td><td>73</td></tr><tr><td>Frankfurt</td><td>72</td></tr><tr><td>Vienna</td><td>72</td></tr><tr><td>Washington, DC</td><td>71</td></tr><tr><td>Copenhagen</td><td>70</td></tr><tr><td>Sydney</td><td>69</td></tr><tr><td>Berlin</td><td>69</td></tr><tr><td>Munich</td><td>68</td></tr><tr><td>Vancouver</td><td>64</td></tr><tr><td>Stockholm</td><td>64</td></tr><tr><td>Seattle</td><td>64</td></tr><tr><td>Shanghai</td><td>63</td></tr><tr><td>Brisbane</td><td>62</td></tr><tr><td>Austin</td><td>62</td></tr><tr><td>Denver</td><td>61</td></tr><tr><td>Dubai</td><td>61</td></tr><tr><td>Melbourne</td><td>61</td></tr><tr><td>San Francisco</td><td>61</td></tr></table>

![](images/a40c6d23415f7f41d63fa2604b9a98fda7a2b952b4ab227cf7ce46cdfe5e4dfb.jpg)

## Social capital

<table><tr><td>City</td><td>Total dimension score</td></tr><tr><td>Beijing</td><td>78</td></tr><tr><td>London</td><td>72</td></tr><tr><td>Berlin</td><td>70</td></tr><tr><td>Shanghai</td><td>70</td></tr><tr><td>Copenhagen</td><td>70</td></tr><tr><td>Vienna</td><td>67</td></tr><tr><td>Shenzhen</td><td>65</td></tr><tr><td>Doha</td><td>64</td></tr><tr><td>Sydney</td><td>64</td></tr><tr><td>Amsterdam</td><td>63</td></tr><tr><td>Stockholm</td><td>62</td></tr><tr><td>Dubai</td><td>62</td></tr><tr><td>Paris</td><td>61</td></tr><tr><td>Seoul</td><td>61</td></tr><tr><td>Munich</td><td>60</td></tr><tr><td>New York City</td><td>60</td></tr><tr><td>Helsinki</td><td>59</td></tr><tr><td>Zurich</td><td>59</td></tr><tr><td>Madrid</td><td>59</td></tr><tr><td>Manchester</td><td>58</td></tr></table>

![](images/668ba61032593a4a0041a3ee668f37438dafbb44fb4ba1fd0f41c31fc3e4ac6a.jpg)

## Engagement with governments

<table><tr><td>City</td><td>Total dimension score</td></tr><tr><td>Frankfurt</td><td>80</td></tr><tr><td>Zurich</td><td>79</td></tr><tr><td>Munich</td><td>77</td></tr><tr><td>Austin</td><td>77</td></tr><tr><td>San Francisco</td><td>75</td></tr><tr><td>Riyadh</td><td>75</td></tr><tr><td>London</td><td>74</td></tr><tr><td>Atlanta</td><td>73</td></tr><tr><td>Dubai</td><td>72</td></tr><tr><td>Washington, DC</td><td>71</td></tr><tr><td>Abu Dhabi</td><td>70</td></tr><tr><td>Singapore</td><td>70</td></tr><tr><td>Miami</td><td>69</td></tr><tr><td>Denver</td><td>69</td></tr><tr><td>New York City</td><td>67</td></tr><tr><td>Seoul</td><td>67</td></tr><tr><td>Berlin</td><td>67</td></tr><tr><td>Mecca</td><td>66</td></tr><tr><td>Copenhagen</td><td>66</td></tr><tr><td>Dammam</td><td>66</td></tr></table>

## Speed of change, 2014-2024—top 20 cities

<table><tr><td>Rank</td><td>City</td><td>Total dimension score</td><td>SoC in economic opportunities</td><td>SoC in livability</td><td>SoC in social capital</td><td>SoC in engagement with governments</td></tr><tr><td>1</td><td>Shenzhen</td><td>92</td><td>86</td><td>100</td><td>100</td><td>90</td></tr><tr><td>2</td><td>Riyadh</td><td>91</td><td>84</td><td>100</td><td>81</td><td>100</td></tr><tr><td>3</td><td>Tashkent</td><td>88</td><td>97</td><td>51</td><td>84</td><td>95</td></tr><tr><td>4</td><td>Doha</td><td>87</td><td>82</td><td>88</td><td>100</td><td>84</td></tr><tr><td>5</td><td>Guangzhou</td><td>85</td><td>78</td><td>80</td><td>100</td><td>86</td></tr><tr><td>6</td><td>Shanghai</td><td>83</td><td>78</

[中间内容因长度限制已省略]

gs in the city, score</td></tr><tr><td rowspan="2">Government services</td><td>E-Government Development Index (EGDI)</td></tr><tr><td>Survey: Easiness and effectiveness of obtaining public services, score</td></tr><tr><td rowspan="7">Business environment</td><td>Number of coworkings per 100,000 population</td></tr><tr><td>Number of business incubators &amp; accelerators per 100,000 population</td></tr><tr><td>Cost of business start-up procedures, % of GNI per capita</td></tr><tr><td>Time required to start a business, days</td></tr><tr><td>Survey: Availability of support for starting a business, score</td></tr><tr><td>Survey: Efficiency of the business startup process, score</td></tr><tr><td>Survey: Favorability of regulatory, tax, and law enforcement systems for business operations, score</td></tr><tr><td rowspan="5">Speed of change in economic opportunities</td><td>Real household income: average annual growth rate (2014 - 2024)</td></tr><tr><td>GINI coefficient: average annual growth rate (2014 - 2024)</td></tr><tr><td>Survey: Job opportunities &amp; cost of living have improved over past five years, score</td></tr><tr><td>Survey: Financial situation has improved over the past three years, score</td></tr><tr><td>Average annual change in unemployment (2014-2024)</td></tr><tr><td rowspan="3">Speed of change in engagement with governments</td><td>E-Government Development Index (EGDI): change in score over the last 10 years (2014 - 2024)</td></tr><tr><td>Survey: Government services have improved over the past five years, score</td></tr><tr><td>Survey: I trust the city authorities more today than I did three years ago, score</td></tr></table>

<table><tr><td rowspan="9">Speed of change in livability</td><td>Average mortgage payment relative to average monthly household disposable income (2024 / 2014)</td></tr><tr><td>Average cost of renting an apartment versus the average monthly income: average annual growth rate (2014 - 2024)</td></tr><tr><td>Number square meters of living space per person: average annual growth rate (2014 - 2024)</td></tr><tr><td>Number of new subway stations built within the last 10 years (2014 - 2024)</td></tr><tr><td>Average life expectancy at birth: average growth rate (2014 - 2024)</td></tr><tr><td>Students&#x27; results in the PISA test: change over 10 years</td></tr><tr><td>Number of retail outlets per 100,000 population: average annual growth rate (2014 - 2024)</td></tr><tr><td>Air quality: PM2.5 content, average annual growth rate (2014 - 2024)</td></tr><tr><td>Survey: In general, over the past three years, the city has become better as a place to live, score</td></tr><tr><td rowspan="6">Speed of change in social capital</td><td>Number of crimes per year per 100,000 population: average annual growth rate (2014 - 2024)</td></tr><tr><td>Number of murders per year per 100,000 population: average annual growth rate (2014 - 2024)</td></tr><tr><td>Helping a stranger: average annual growth rate (2014 - 2024)</td></tr><tr><td>Share of people participating in donating money: average annual growth rate (2014 - 2024)</td></tr><tr><td>Survey: Safety has improved over the past five years, score</td></tr><tr><td>Survey: Over the past three years, people in the city have become more open to communication and tolerant, score</td></tr></table>

## Disclaimer

The services and materials provided by Boston Consulting Group (BCG) are subject to BCG's Standard Terms (a copy of which is available upon request) or such other agreement as may have been previously executed by BCG. BCG does not provide legal, accounting, or tax advice. The Client is responsible for obtaining independent advice concerning these matters. This advice may affect the guidance given by BCG. Further, BCG has made no undertaking to update these materials after the date hereof, notwithstanding that such information may become outdated or inaccurate.

The materials contained in this presentation are designed for the sole use by the board of directors or senior management of the Client and solely for the limited purposes described in the presentation. The materials shall not be copied or given to any person or entity other than the Client (“Third Party”) without the prior written consent of BCG. These materials serve only as the focus for discussion; they are incomplete without the accompanying oral commentary and may not be relied on as a stand-alone document. Further, Third Parties may not, and it is unreasonable for any Third Party to, rely on these materials for any purpose whatsoever. To the fullest extent permitted by law (and except to the extent otherwise agreed in a signed writing by BCG), BCG shall have no liability whatsoever to any Third Party, and any Third Party hereby waives any rights and claims it may have at any time against BCG with regard to the services, this presentation, or other materials, including the accuracy or completeness thereof. Receipt and review of this document shall be deemed agreement with and consideration for the foregoing.

BCG does not provide fairness opinions or valuations of market transactions, and these materials should not be relied on or construed as such. Further, the financial evaluations, projected market and financial information, and conclusions contained in these materials are based upon standard valuation methodologies, are not definitive forecasts, and are not guaranteed by BCG. BCG has used public and/or confidential data and assumptions provided to BCG by the Client. BCG has not independently verified the data and assumptions used in these analyses. Changes in the underlying data or operating assumptions will clearly impact the analyses and conclusions.

## BCG BOSTON CONSULTING GROUP
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
