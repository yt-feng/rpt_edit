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
# The Digital Finance Opportunity in the Philippines

June 2026

By Sumit Kumar, Archit Choudhary, Shobhit Shubhankar, Omar Zen, Jaymes Shrimski, and Rachel Lee

![](images/2746b8a5f9cac7066dc86f4b7b92ee71419fe8ca293cecbe0b419a33520f2f64.jpg)

BCG

This report was commissioned by Maya.

This document has been prepared in good faith on the basis of information available at the date of publication without any independent verification. BCG does not guarantee or make any representation or warranty as to the accuracy, reliability, completeness, or currency of the information in this document nor its usefulness in achieving any purpose. Readers are responsible for assessing the relevance and accuracy of the content of this document. It is unreasonable for any party to rely on this document for any purpose and BCG will not be liable for any loss, damage, cost, or expense incurred or arising by reason of any person using or relying on information in this document. To the fullest extent permitted by law, BCG shall have no liability whatsoever to any party, and any person using this document hereby waives any rights and claims it may have at any time against BCG with regard to the document. Receipt and review of this document shall be deemed agreement with and consideration for the foregoing.

This document is based on a primary qualitative and quantitative research executed by BCG. BCG does not provide legal, accounting, or tax advice. Readers are responsible for obtaining independent advice concerning these matters. This advice may affect the guidance in the document. Further, BCG has made no undertaking to update the document after the date hereof, notwithstanding that such information may become outdated or inaccurate. BCG does not provide fairness opinions or valuations of market transactions, and this document should not be relied on or construed as such. Further, any evaluations, projected market information, and conclusions contained in this document are based upon standard valuation methodologies, are not definitive forecasts, and are not guaranteed by BCG. BCG has used data from various sources and assumptions provided to BCG from other sources. BCG has not independently verified the data and assumptions from these sources used in these analyses. Changes in the underlying data or operating assumptions will clearly impact the analyses and conclusions.

This document is not intended to make or influence any recommendation and should not be construed as such by the reader or any other entity. This document does not purport to represent the views of the companies mentioned in the document. Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise, does not necessarily constitute or imply its endorsement, recommendation, or favoring by BCG.

## Contents

06 Investment Attractiveness of the Philippines
14 The Financial Institutions Landscape in the Philippines
22 Digital Penetration in Payments and Lending
33 Landscape of Fintech Players

## Preface

The Philippines stands out among emerging markets for its rare combination of scale, sustained macro momentum, and favorable demographics. With a population exceeding 100 million, projected real GDP growth of \~6% over the next 5 years, and a young, digitally engaged population, the country offers a large and expanding addressable market. Growth is structurally consumption-led, supported by steady remittance inflows and a broadly stable, market-oriented policy environment.

While the macroeconomic landscape in Philippines is very favorable, financial services penetration has historically been low, particularly through digital channels. Roughly half of adults are unbanked, and household and MSME credit penetration lags peer countries. These gaps reflect persistent supply-side constraints – rather than lack of demand – most notably in terms of historically prevailing operating models, distribution economics, and risk assessment.

Digital infrastructure and regulation are easing historical supply constraints. Payments are now at scale; identity and credit-data plumbing is improving; and digital-first platforms are positioned to translate transaction engagement into deposits and credit.

The next stage of growth will be defined both by first-time access for the remaining underbanked population, and broader, more frequent engagement among existing customers. This sets up a step-change opportunity for digital-first models to leapfrog physical incumbents in segments where technology, data, and integrated platforms can materially improve reach, economics, and customer outcomes.

# Investment Attractiveness of the Philippines

The Philippines is one of the fastest-growing large economies with a large population globally, with its attractiveness anchored in four key factors: large scale with strong private institutions and a laissez-faire approach to the market, consumption-led growth buffered by remittances from overseas, favorable demographics, and high digital engagement that supports rapid adoption of digital-first services.

## Large economic scale supported by macro stability and market-oriented institutions

Philippines is one of the fastest growing large economies globally

Projected growth vs economic size, 50 largest economies (by nominal GDP)

![](images/4f826da339ce27e9560a489978c0a4edd2e2eacdb5882133cbbd2e97d86e8651.jpg)

![](images/f69551e5d424681adea7a680543d343696ec43645c72678ec860627515c213d9.jpg)

Notes: GDP and population data reflect latest available actuals (2025, nominal); Real GDP growth rates represent projected real GDP CAGR for 2025–2030; The Philippines ranks 33rd globally by nominal GDP; Real GDP growth may be positive even in high-inflation environments because real GDP adjusts output for price changes; Countries are segmented into income groups based on GDP per capita, nominal PPP (2025): Advanced > USD 40,000; Middle income USD 10,000–40,000; Emerging < USD 10,000

Source: Nominal GDP, real GDP and population data from Oxford Economics

The Philippines sits within a defined group of seven emerging economies with populations exceeding 100 million—Mainland China, India, Indonesia, Vietnam, the Philippines, Mexico, and Brazil—where domestic market scale is sufficient to support sustained company growth and capital deployment. Within this group, Mainland China and India stand apart as scale-driven Asian markets, while the Philippines aligns with ASEAN growth markets such as Vietnam and Indonesia, but with comparatively stronger democratic institutions and governance metrics alongside sustained growth. By contrast, Mexico and Brazil represent more global, mature peers with slower growth trajectories [Exhibit 2].

The Philippines has delivered resilient, above-peer growth, with real GDP averaging above 5% over the past decade and forecast to hover around the 6% $^{1}$ mark through 2030 supported in the near term by household consumption and, over the medium term, by higher private investment and efficiency gains as recent structural reforms take hold in a young, services-led economy. Together, these drivers have enabled sustained expansion across consumer-facing and services sectors, underpinning a broad-based growth profile.

This performance has been reinforced by comparatively strong institutional foundations and a broadly market-led economic model, which have supported policy continuity, limited state intervention in commercial activity, and a stable operating environment for private investment. The restrained role of the state in most commercial sectors has allowed private firms to lead capital deployment and growth [Exhibit 3].

## EXHIBIT 2

Among 100 million+ population emerging markets, the Philippines stands out for growth and stability

<table><tr><td rowspan="2"></td><td colspan="2">Scale-driven Asian markets</td><td colspan="3">ASEAN growth markets</td><td colspan="3">Global, mature peers</td></tr><tr><td>China1</td><td>India</td><td>Vietnam</td><td>Indonesia</td><td>Philippines</td><td>Mexico</td><td>Brazil</td><td>Egypt</td></tr><tr><td>Population, 2025 (million individuals)</td><td>1,416</td><td>1,464</td><td>102</td><td>286</td><td>117</td><td>132</td><td>213</td><td>117</td></tr><tr><td>Real GDP growth &#x27;25-30 (% CAGR)</td><td>4.2%</td><td>6.4%</td><td>5.2%</td><td>5.0%</td><td>6.0%</td><td>1.8%</td><td>2.0%</td><td>4.2%</td></tr><tr><td>GDP per capita, PPP, nominal, 2025 (US$ thousand)</td><td>29.2</td><td>12.1</td><td>17.9</td><td>17.6</td><td>12.6</td><td>20.1</td><td>23.5</td><td>20.3</td></tr><tr><td>Democratic index score, 2024 (0-10 scale)</td><td>5.3</td><td>6.5</td><td>2.6</td><td>6.4</td><td>6.6</td><td>5.3</td><td>6.5</td><td>2.8</td></tr><tr><td>Credit rating (Fitch, 2025)</td><td>A</td><td>BBB-</td><td>BB+</td><td>BBB</td><td>BBB</td><td>BBB-</td><td>BB</td><td>B</td></tr><tr><td>FX volatility (10-yr, annualized)</td><td>6%</td><td>4%</td><td>3%</td><td>9%</td><td>6%</td><td>13%</td><td>16%</td><td>28%</td></tr></table>

Peer countries with comparable population scale, income levels, and macroeconomic performance over the last decade

![](images/eec0572ab7c5a6e3afff04fa0f3f41ba61e5e6ef32898e2921f13b6c21c70e7b.jpg)

This institutional and market-led foundation has been complemented by disciplined macroeconomic management. Inflation has remained largely within the BSP's 2–4% target band outside of shock years $^{2}$ , while the Philippines' sovereign credit rating has improved from sub-investment grade (BB+/Ba2) in the early 2010s to

sustained investment-grade status (BBB/Baa2) across major agencies today, supporting stable foreign direct investment inflows averaging \~2% of GDP over the past decade $^{3}$ , with recent moderation reflecting global macro headwinds rather than domestic weakness.

## EXHIBIT 3

# Philippines has a more laissez-faire approach to business compared to similarly sized Southeast Asia peers, Vietnam and Indonesia

## State ownership & market presence

![](images/851e492e62b1c8bad2b5c56e2856d4152c7beca8f0fa4e68f0d5a4cb1b1e7e0c.jpg)

## Limited state footprint; market-led delivery

State ownership is largely confined to policy or legacy institutions, with most commercial activity undertaken by private firms

Government-Owned or Controlled Corporations (GOCCs) play a supporting or enabling role, rather than acting as dominant market players

![](images/054365bc8a5a9794d38e45935e206d22a28be67f079a5911d16e65826c0bc434.jpg)

## Material state presence in key sectors

## Indonesia

State-owned enterprises (SOEs) play a central role in strategic sectors including energy, utilities, mining, and banking

Large state-owned banks $^{1}$ and enterprises act as anchors for investment and policy execution

![](images/dec6291e2e32a4dff93a8c4481983984022703fe79b19e1995c8f02ea842824b.jpg)

## Extensive state ownership across the economy

## Vietnam

State-owned enterprises (SOEs) remain deeply embedded across strategic and commercial sectors, including energy, telecoms, transport, and finance

State-owned banks and enterprises retain a systemic role in credit provision $^{2}$

![](images/e032a41fc27f8e93e20f9ce36ce429b3ff6fa017a4303ac07cea1b7d9b7b6d5f.jpg)

## Private-sector-led economy; limited SOE dominance outside of energy

Predominantly private-sector driven at the economy level, with very selective state influence in strategic sectors like energy

State-owned enterprises (e.g., Pemex, CFE $^{3}$ ) act as policy and investment anchors

## Market-based economy; limited state ownership

![](images/a3651319dc2fc66b5cde0f5e1ef5746d0f0f0ae448e6eb7a2d4c37644e3c1e61.jpg)

Predominantly private-sector driven across manufacturing, agribusiness, and consumer markets

State ownership is limited to a set of strategic sectors (e.g., energy, utilities, transport infrastructure, and development finance)

Market-led/laissez-faire

![](images/5f4ed6eb5f0b2dbcfbeec669ef2f0d54e505577555552e69d3adf83929621447.jpg)

Moderate intervention

![](images/a69b91c02a2a9548fe817d7d9547efbfd4fbb36155e5f539c658e9e22dfecb32.jpg)

## Industrial planning

## Market-driven, liberalized planning setup

Policy focused on creating enabling conditions for private investment, rather than directing sector outcomes

Sector development primarily guided by market demand and private actors

## Selective, policy-guided development

Industrial policy used to support priority sectors (e.g., natural resources, manufacturing)

Policy tools: targeted incentives and regulatory measure to encourage use of domestic resources

## Coordinated, state-guided development

Economic direction set by state through five-year socio-economic plans

![](images/5c7374654707365f99ce220c9326646a2e061b5b93b89e307199fbf904452e27.jpg)

Explicit national targets guide industrial and investment policy based on priority sectors and development objectives

## Market-driven industrial planning, with selective intervention

Sector policies are generally market-responsive, but in energy and infrastructure there has been targeted state support and legal frameworks that strengthen the role of state enterprises $^{4}$

## Selective, state-coordinated development

Economic development shaped through targeted industrial policy and public development finance, rather than economy-wide planning

Public banks (notably BNDES $^{5}$ ) and sector programs are used selectively to steer investment toward priority areas

## State-led/interventionist

The Philippines follows a relatively market-led approach, with limited state ownership, liberal investment rules, and a preference for rules-based policy frameworks

The Philippines stands out among similarly sized regional peers for its market-led approach to business, with limited state ownership, relatively liberal investment rules, and a preference for neutral, rules-based policy frameworks

Economic activity outside of utilities and core infrastructure is largely driven by private firms, while recent reforms have focused on lowering economy-wide costs and barriers to entry rather than directing sector outcomes

1. The three large Indonesian state-owned banks collectively account for about 47% of total assets, 52% of loans, and 47% of deposits (2024);
2. State-owned commercial banks were estimated to account for roughly 43 per cent of total credit (2025); GOCC – Government-owned or Controlled Corporation; SOE – State-owned Enterprise

# Consumption-led growth reinforced by rising incomes and structurally resilient remittances

## EXHIBIT 4

## A consumption-led model differentiates the Philippines from Southeast Asia peers

PH is a highly consumption-oriented economy relative to peers, similar to Mexico...

Private consumption 2020-2025 (% of GDP)

![](images/92bdd7c3f591a298194f8612890cd3b5d451a57ec6514a8a9a6675a5903e2784.jpg)  
Source: Private consumption and GDP data from Oxford Economics  
population and steady household income support from remittances. Over time, institutional and economic frameworks shaped by prolonged Western engagement—particularly during the American period—have reinforced household-driven demand as the central engine of growth [Exhibit 4].

The Philippine growth model is structurally consumption-led, with private consumption accounting for approximately 76% of GDP $^{4}$ —well above most Southeast Asian peers and closer to levels observed in more consumption-driven Western economies such as the United States. This structure reflects underlying income dynamics and demographic factors, including a large working-age

## EXHIBIT 5

Remittances to the Philippines continue to grow and exceed peers as a share of GDP

...with a consistent flow of remittances, contributing meaningfully to domestic consumption

Remittances to Philippines per year (USD bn)  
![](images/34670048a2d049c22959f2ce863824d921f6e584baa4753dcd7ce5208826b1e5.jpg)

Remittances as share of GDP (%)  
![](images/28b9928b7dcafa3e8e5506d37fc85cf97d3e51843b954f27f3e16dce598c523f.jpg)  
Remittances to PH by source country 2024 (%)

![](images/59996b63e7bd93ddad95bead64839b881536fb84cf1d597a4690aaa31116900f.jpg)  
Source: Bangko Sentral ng Pilipinas (BSP) Overseas Filipino Cash Remittances; GDP from Oxford Economics

This demand base is reinforced by large and predictable overseas remittances—consistently 8–9% of GDP—anchored by mature diaspora networks and stable transfer behavior. By comparison, remittances account for a materially smaller share of GDP in peer markets, such as Mexico (3.7%) and Vietnam (3.5%) $^{5}$ [Exhibit 5].

Rising incomes are further broadening the spending base. Middle-class households are projected to reach 8.8 million by 2035, up from 5.8 million in 2025 $^{6}$ , growing the middle-class share of households by over 50%. This expansion is already reshaping consumption patterns, supporting a shift toward more discretionary categories such as leisure, durables, education, and financial services. As a result, per-capita consumer spending is forecast to grow at 5.1% CAGR between 2025 and 2030, outpacing most regional peers (vs Indonesia, 4.4%) and global, mature markets (vs Brazil, 1.2%) [Exhibit 7].

## EXHIBIT 6

# Philippines to have \~70M middle-class & affluent consumers by 2030, fueling continued consumption

Total population in the Philippines (million)

![](images/e7e823f686a5507b7e79c089994b2fc2b0cf4413bc7e103cf54d5c5ef457b1c1.jpg)  
Source: BCG Center for Consumer Insights, BCG analysis
A + = Affluent (>1,938,769); A = Affluent (1,246,352 - 1,938,769); B= Established (553,934 - 1,246,352); D= Aspirant (152,332-304,664); E= Poor (<152,332)

## EXHIBIT 7

# Larger middle class and rising affluence expected to drive continued consumer spending growth

## Consumer spending per capita growth 2025-2030F CAGR (%)

![](images/43942df3c6c5bf3cf4d23b4def0dd0aefb49b1a06312ad9bcbfd76c4cf39c053.jpg)  
Source: Consumer spend, real, PPP\$ total (millions, 2015 prices), Population Data from Oxford Economics; World Bank; BCG analysis

Consumer spending growth in the Philippines is expected to outpace major regional peers, supported by rising incomes, a young demographic profile, and an expanding middle class, underpinning solid per-capita consumption growth over the medium term; greater consumption fuels demand for payments and lending

This strength is reinforced by structural demand drivers, including:

\- Young demographic profile sustaining a large pipeline of consumers and labor force entrants

\- Consumption-heavy economic mix with household consumption at \~76% of GDP (vs. global ave. 55%) converting income gains to spending quickly

\- Rising affluence and middle-class expansion, as strong GDP per capita growth (\~7%+ CAGR thro

[中间内容因长度限制已省略]

ed toward intermediate inputs (supplier payments) was approximated at 75-80% based on PSA ASPBI. Finally, digital penetration of MSME supplier payments was estimated using expert interviews and triangulated against national and international databases and benchmarks.

MSME2B lending flows were sized by estimating outstanding loan balances for MSME unsecured loans and MSME secured loans using BCG's bottom-up lending model and BSP data. Average loan tenors and interest rates were derived from expert input and bank data. Outstanding balances were then converted into annual repayment flows using the following formula. Digital penetration assumptions were then applied based on expert interviews and triangulated with national and international databases and benchmarks.

## Bibliography

1. International Monetary Fund, World Economic Outlook Database, accessed via IMF DataMapper, 2025. https://www.imf.org/external/datamapper/NGDP\_RPCH@WEO/OEMDC/ADVEC/WEOWORLD/LIE

2. Bangko Sentral ng Pilipinas, Price Statistics – Consumer Price Index (CPI): Monthly Inflation Data, BSP, 2025. https://www.bsp.gov.ph/SitePages/Statistics/Prices.aspx?TabId=1

3. Oxford Economics, Global Economic Databank, "Foreign direct investment, inward, US\$," Oxford Economics, accessed 2025

4. Oxford Economics, Global Economic Databank, "Consumption, private, nominal, share of GDP (%)," Oxford Economics, accessed 2025

5. World Bank, “Personal remittances, received (current US\$),” World Bank Open Data, accessed 2025. https://data.worldbank.org/indicator/BX.TRF.PWKR.CD.DT

6. NRISG, Part 2—Rising GDP Per Capita and the Filipino Middle Class, accessed 2025. https://nrisg.com/part-2-rising-gdp-per-capita-and-the-filipino-middle-class/

7. World Bank, “Gross enrollment ratio, tertiary (% of relevant age group)–Philippines,” World Bank Open Data, accessed 2025. https://data.worldbank.org/indicator/SE.TER.ENRR?locations=PH

8. Temasek and Google, e-Conomy SEA, accessed 2025. https://economysea.withgoogle.com/

9. We Are Social and Hootsuite, Global Digital Report 2025, “Filipinos aged 16 + who are active internet users owning cryptocurrency (15% vs global average 9.6%),” We Are Social, accessed 2025. https://wearesocial.com/wp-content/uploads/2025/02/GDR-2025-v2.pdf

10. Bangko Sentral ng Pilipinas and the Financial Inclusion Steering Committee, Philippine Financial Inclusion Dashboard, “Bank branch concentration and financial intermediation patterns,” accessed 2025. https://financialinclusion.gov.ph/fi-dashboard/

11. Bangko Sentral ng Pilipinas, Loans Outstanding for Production and Household Consumption and Compliance with the Magna Carta for Micro, Small and Medium Enterprises, BSP Financial Statements Statistics, accessed 2025. https://www.bsp.gov.ph/SitePages/Statistics/Statistics.aspx

12. Bangko Sentral ng Pilipinas, Payments and Settlements Bulletin, Payment and Settlements Department, BSP, accessed 2025. https://www.bsp.gov.ph/PaymentAndSettlement/PPDD\_Payments\_Bulletin.pdf

13. Credit Information Corporation, 2024 Annual Report: Increasing Credit Visibility and Accessibility, Promoting Sustainability through Finance, CIC, Manila, 2025

14. Bangko Sentral ng Pilipinas and the Financial Inclusion Steering Committee, Philippine Financial Inclusion Dashboard, accessed 2025. https://financialinclusion.gov.ph/fi-dashboard/

15. Philippine Statistics Authority, PSA Gathers Financial and Private Institutions for Exchange of Insights on National ID Integration, PSA, accessed 2025. https://philsys.gov.ph/psa-gathers-financial-private-institutions-for-exchange-of-insights-experiences-on-national-id-integration/

## About the authors

![](images/891744c84bac3d51fa4da6b38bb9a40a917c361112c0c4639c685f56acd27988.jpg)

Sumit Kumar is a Managing Director and Partner in BCG's Singapore office. You may contact him by email at kumar.sumit@bcg.com

![](images/22981bdb3be0097b1567a426219ebbd09e8fd48b832dd3e6b8d154c621acd593.jpg)

Archit Choudhary is a managing director and partner in bcg's singapore office. you may contact him by email at choudhary.archit@bcg.com

![](images/449824f19aaefad2c760b082f9ca1ad194400c0620b54ddcf11b10381dd50cf5.jpg)

Shobhit Shubhankar is a Partner in BCG's Singapore office. You may contact him by email at shubhankar.shobhit@bcg.com

![](images/7712c20217db8174a24be511f177a91a7c0a25dce2e57569bd939a99d3081281.jpg)

![](images/ecb824031d72296d6ffaf542aa0cc2d3d38580cfb1504c6bb28c406987f77a55.jpg)

Jaymes Shrimski is a consultant in bcg's manila office. you may contact him by email at
shrimski.jaymesnicholas@bcg.com

Omar Zen is a Consultant in BCG's Jakarta office. You may contact him by email at zen.omar@bcg.com

![](images/8b463267ec96fa5a5d5714416dfa6efd19a9f0c1460ac2ea490e9dfd33a7eafb.jpg)

Rachel Lee is a Senior Associate in BCG's Singapore office. You may contact her by email at lee.rachel@bcg.com

## Acknowledgements

The authors would like to thank Christabel Dewani and Eugenia Siah for their support in preparing this report.

## For Further Contact

If you would like to discuss this report, please contact the authors.

## BCG

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.

![](images/63d4b7a21b24f48d0ba97d4413cb1443e05f17871790fb46e664917d8a4e94cb.jpg)

BCG
"""
