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
FINANCIAL INSTITUTIONS
GLOBAL ASSET MANAGEMENT REPORT 2026
24TH EDITION

# An Imperative for Growth

April 2026

By Renaud Fages, Johannes Burkhardt, Edoardo Palmisani, Joppe Bijlsma, Peter Czerepak, Matt Egler, Dean Frankle, Kwonyoung Jang, Mayank Jha, Katsuyoshi Kurihara, Kedra Newsom Reeves, Neil Pardasani, Maël Robin, George Rudolph, Philippe Soussan, Matt Sweeny, Tjun Tang, Charles-Antoine Wallaert, André Xavier, and Ivana Zupa

![](images/2b29a6c310b566d82be8b310da517a95b6c8dd6b7e8812d4311cc208e4d4f0f6.jpg)

## Contents

03 The New Economics of Asset Management
13 Distribution Is the New Source of Advantage in Asset Management
19 Rebuilding Asset Management for an AI-First World
25 Appendix
29 About the Authors

![](images/af9ad589acd8ad92c3f760759599cd9ba0d45fc3ded0543693462a2d5de7f57a.jpg)

# The New Economics of Asset Management

For more than a decade, rising markets did most of the work. Assets grew, and revenues followed. This dynamic may not be over, but it will no longer carry the industry.

Global assets under management (AuM) reached \$147 trillion in 2025, up 11% year over year, while aggregate profit margins held above 30%. The industry appears resilient. But more than 80% of gross revenue growth in 2025 was driven by market appreciation, underscoring its continued reliance on external forces. (See Exhibit 1.)

This reliance is not new. What is changing is where growth comes from and who captures it. Capital is redistributing across regions, vehicles, and client segments. New gatekeepers are emerging, distribution is evolving, and technological forces—particularly AI—are reshaping the economics of asset management. As a result, market tailwinds no longer benefit incumbents by default. Capturing net new flows is now the central competitive differentiator.

This will require asset managers to operate differently. Firms that align with the next sources of capital and adapt how they compete will capture a disproportionate share of future growth.

## EXHIBIT 1

# Market Performance Drove Over 80% of Gross Revenue Growth Between 2024 and 2025

CHANGE IN REVENUE, 2024–2025 (%)

![](images/0db7a27ea3169bb6581909c78072a95eb08f774c8c8cbec392a67f4a41bad133.jpg)  
Sources: BCG EXPAND Global Asset Management Market Sizing 2026; BCG EXPAND Global Asset Management Benchmarking 2026.
Note: Scope of analysis is active core, active specialties, solutions, and passives and alternatives. Values differ from those in prior studies due to exchange rate fluctuations, revised methodology, and changes in source data.

## A Growth Formula Under Pressure

Industry assets continue to expand, but the benefits are increasingly uneven. This reflects changes in where demand is coming from, how it is captured, and how it translates into profitability.

## Sources of Growth Are Shifting

Retail investors are now the primary driver of AuM growth, accounting for 61% of global expansion between 2020 and 2025. Retirement systems are increasingly redirecting flows as defined contribution plans expand and defined benefit pools mature. Growth is also becoming more dispersed geographically, with Asia-Pacific posting the fastest gains at 9% annually over the same period, supported by strong net inflows. (See Exhibit 2.)

These patterns are also visible across asset classes. Retail investors dominate much of the traditional product landscape, including active equity, fixed income, exchange-traded funds (ETFs), and money market funds, while institutional investors remain the primary allocators to alternatives. As a result, the market is becoming more segmented, with client channel and product strategy increasingly intertwined. New distribution

channels are also emerging, with insurance likely to become a particularly important channel for private credit. (See "Private Credit's Insurance Opportunity.")

## Capturing Growth Is More Complex

In US passive mutual funds and ETFs, flows are highly concentrated among a small number of firms, with the top ten providers capturing more than 90% of net inflows since 2015. Active strategies show a different pattern. In the US, the top ten active managers' share of net inflows has fallen from 63% in 2015 to 56% in 2025 as flows spread across a larger number of competitors. In Europe and Asia-Pacific, both active and passive markets are becoming less concentrated, indicating increasingly competitive environments.

In private markets, investors continue to allocate significant capital to the asset class, but they are doing so with fewer managers. The top 50 private equity firms captured 37% of global fundraising in 2024, compared with a ten-year average of 22%, according to Preqin. Taken together, and as access to distribution increasingly determines which managers are even considered for shelf space, these shifts point to a more demanding growth environment.

# Private Credit's Insurance Opportunity

![](images/d09eefcc869eb7b889c2c9440c952f5d95313c1d25823bbde9ed9fa189b1951c.jpg)

For asset managers looking to scale private credit distribution, insurers represent one of the most attractive and underpenetrated channels. The role insurers play varies by region. In the US and Asia, they act primarily as institutional allocators. In Europe, they also serve as a retail distribution wrapper. Public credit no longer provides meaningful differentiation, leaving insurers with fewer ways to stand out in an increasingly crowded market. Private credit fills that gap.

Many insurers lack the capability to access private credit at scale on their own. That's where asset managers come in. Through sub-advisory mandates, joint ventures, or captive platforms, these partnerships create value on both sides. They bring the origination networks, structuring expertise, and portfolio capabilities that insurers need, while providing asset managers with seed capital, long-term institutional allocations, and shared marketing costs.

Over time, platforms are integrated into insurers' investment processes, aligned with asset-liability management frameworks, and connected to core operations. Asset managers are also engineering exposures directly, using rated notes and other capital-efficient vehicles to fit insurance capital frameworks. Early movers can build these capabilities into their product architecture. Once in place, that integration is difficult to unwind, making the asset managers that enable it hard to displace. As these structures scale, they become a more central part of capital deployment, effectively turning private credit into insurance-compatible instruments.

But executing these shifts well requires more than a compelling strategy. Retail clients have different liquidity expectations than institutional ones, and client segmentation across mass-affluent, high net worth, and institutional tiers needs to be rigorous. Any arrangement has to sit comfortably within the insurer's broader balance sheet logic, including asset-liability management constraints, duration matching, risk appetite, and solvency capital requirements. Getting this right requires optimizing capital efficiency, which introduces additional complexity in structuring, valuation, and risk management.

Some asset managers have begun building their insurance product portfolios, but the opportunity remains significant, and the market is still early. Here's how to get started.

Choose the right partnership model. Distribution-only arrangements, where an insurer offers an existing fund through its platform, are the natural starting point. Co-designed products, developed jointly within a unit-linked wrapper, require greater capability but deliver stronger economics and defensibility through deeper product integration and balance sheet commitment. Strategic capital partnerships—where the insurer provides seed capital or a balance sheet allocation—are the most ambitious and the hardest to replicate once established, given the depth of financial alignment and integration.

Secure your structural position. Access to an insurer's product shelf is not the same thing as being embedded in its core unit-linked platform. Formal inclusion determines volume steering, margin capture, and long-term defensibility. For managers still building their private credit offering, the priority is an anchor insurer relationship with genuine alignment on client base and scale ambition. Managers with more established offerings should diversify across insurers to broaden reach and reduce concentration risk.

Design the product for the insurance wrapper. Wealth accumulation and retirement income products have materially different portfolio construction and liquidity requirements, so the choice of use case matters. Asset duration needs to match insurance liabilities, enabling hold-to-maturity strategies rather than mark-to-market sensitivity. Returns expectations should be framed around stable spread generation and downside protection, not high internal rates of return. Liquidity mechanics, including evergreen formats and defined withdrawal windows, must map to underlying loan cash flows. Risk allocation also needs to be set upfront, including whether retail investors access only senior exposure and whether the insurer retains the junior or first-loss layer. Where capital-efficient structures are used, transparency, governance, and regulatory alignment become critical, as increasing scrutiny may shape how these solutions evolve.

Sources: BCG EXPAND Global Asset Management Market Sizing 2026; BCG analysis.

Note: AuM market sizing corresponds to assets sourced from each region and professionally managed in exchange for management fees. It includes captive AuM of insurance groups or pension funds where AuM is delegated to asset management entities with fees paid. Overall, 44 markets are covered globally, including offshore AuM (which is not included in any region). For all markets where the currency is not US dollar, end-of-year 2025 exchange rate is applied to all years to synchronize current and historic data. AuM = assets under management. $^{1}$ Represents each core client segment's contribution to net global AuM increase from 2020 to 2025. $^{2}$ Institutional (other) comprises corporate, bank, endowment, foundation and other non-profit, sovereign wealth fund, and government.

# Opportunity Size Varies by Region and Core Client Segment

![](images/b7de65ec1024a1d33be6b3d3f33c8b012d4861067105fed935d196cd52ce1970.jpg)

## Rising AuM No Longer Translates into Higher Profitability

Global AuM has more than tripled and revenue more than doubled over the past 15 years. Yet industry profit margins remain close to 30%, roughly where they stood in 2010. Between 2010 and 2025, revenues grew at 5.1% annually while costs rose slightly faster at 5.4%, producing negative operating leverage.

Several forces are driving this dynamic. Institutional fees have declined by 3% annually, passive funds and ETFs now dominate net inflows, and active ETFs are gaining share at fee levels below the vehicles they are replacing. Each incremental dollar of AuM therefore carries a lower average fee.

Costs add to the pressure. Some expenses decline as firms scale, particularly investment management and support functions that benefit from operating leverage. However, technology investment is rising as a share of the cost base as firms build scalable infrastructure and advanced capabilities. These offsetting forces limit the margin benefits traditionally associated with scale. (See Exhibit 3.)

# AuM Nearly Tripled Since 2010 While Margins Barely Moved

![](images/6c3f3400875409888b75b3f259fcf76cb17fec70967c871931f5d3d9d1c024aa.jpg)  
Sources: BCG EXPAND Global Asset Management Benchmarking Database, 2026; BCG analysis.
Note: Analysis is based on a global benchmarking study of 98 leading asset managers, representing \$86 trillion in AuM, or about 59% of global AuM. Sample is primarily composed of traditional asset managers and excludes pure alternative players, as those economics are not comparable with total asset management revenues based on the global product trend analysis. AuM = assets under management.

## Three Structural Demand Shifts

Looking ahead, control of capital, retirement savings, and geopolitical confidence will determine where future flows originate.

## The Generational Succession

An unprecedented transfer of wealth is reshaping the retail investment landscape. It is estimated that nearly \$124 trillion will move between generations in the US through 2048. The recipients of that capital are increasingly digital-native investors whose relationship with financial services looks very different from their predecessors.

Digital-native investors enter markets earlier—30% of Gen Z begin investing in early adulthood versus 6% of Baby Boomers, according to a World Economic Forum investor survey. They expect integrated digital experiences and show greater openness to alternatives, including private markets and digital assets. They are also reached through fundamentally different channels. BCG research shows that comparison websites, social media, and YouTube now rank among the most influential sources shaping retail investment decisions—channels where the asset management industry has almost no meaningful presence.

Control of the investor relationship is also shifting. In Europe, neobroker assets surpassed €150 billion in 2023. In the US, retail investors now account for roughly 20% to 25% of daily equity trading volume, much of it intermediated through digital platforms. Across Asia-Pacific, retail investors are entering markets through digital channels, using mobile wallets and cash management products as primary entry points.

The rise of digital-native investors is concentrating flows in a smaller set of platforms that act as gatekeepers to capital. For asset managers, success will depend on being embedded in these ecosystems, with products and capabilities designed for how capital is allocated within them.

## Retirement System Transformation

Retirement systems are steadily moving away from defined benefit (DB) and pay-as-you-go structures toward funded defined contribution (DC) models, following a transition the US began several decades ago. The shift comes in response to two parallel structural pressures: a growing pension cliff as obligations outpace funded assets—and a rising demographic cliff driven by aging populations, shrinking workforces, and rapidly rising old-age dependency ratios. (See Exhibit 4.)

## Retirement Systems Face a Demographic and Pension Cliff

![](images/68e87af7fbb11e0265c0b3e450c434e2c3dda7069a268c00e740ecf24c990056.jpg)  
Sources: United Nations; Organisation for Economic Co-operation and Development; government websites; BCG analysis.  
$^{1}$ Pension asset refers to all pension savings managed by pension providers. They can be either public or private, and occupational or personal, managed by banks or investment funds.  
$^{2}$ Ratio of people over 65 years old versus those 15–64 years old.  
$^{3}$ OECD countries do not include Brazil, China, India, Indonesia, South Africa.  
$^{4}$ Continental Europe average pension asset/GDP ratio is 33%. Countries include Austria, Belgium, the Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Italy, Latvia, Lithuania, Luxembourg, Netherlands, Norway, Poland, Portugal, Slovak Republic, Slovenia, Spain, Sweden, Switzerland, and Turkey.

# Nearly half of global investors plan to increase geographic diversification, with Europe (46%), Asia-Pacific (44%), and Emerging Asia (42%) the primary intended destinations.

The implications vary by region.

\- United States. The US system is already DC-led: DC accounts for over 50% of pension assets, with total pension assets at around 153% of GDP. Growth will center on income solutions, advice integration, personalization, and the ability to compete within workplace plans and retirement platforms that serve as primary distribution channels. A potential frontier is the inclusion of private market allocations within DC plans, though regulatory, liquidity, and operational hurdles mean adoption will be gradual.

\- Europe. Europe presents greater catch-up potential, albeit with significant variation across markets. Funded pension assets average roughly 33% of GDP across Continental Europe, with Germany, Italy, and Spain still in the low double digits. At the same time, many European systems face some of the steepest increases in old-age dependency ratios globally, intensifying pressure to shift toward funded and DC-style structures. The Netherlands offers a current illustration. Its Future Pensions Act requires the EU’s largest pension system—€1.8 trillion in assets—to transition from DB to DC by 2028, with the bulk of large funds moving through 2026 and 2027.

\- Asia-Pacific and emerging markets. Demographic pressure is acute across much of Asia and many emerging economies, though the development of funded retirement systems remains uneven and policy-driven. Where DC frameworks expand, retirement pools can scale quickly. Where reform is slower, savings tend to accumulate through wealth management, insurance products, and occupational arrangements.

Across markets, the shift from DB to DC is changing the structure of retirement investing. Assets that once flowed through a small number of institutional mandates are increasingly held in millions of individual accounts, raising customer acquisition costs, increasing service complexity, and placing greater emphasis on scale and distribution.

## The Geographic Confidence Shift

Geopolitical and policy uncertainty have introduced volatility into capital allocation decisions. Questions around US Federal Reserve independence, fiscal sustainability, trade policy, and political stability have moved from background considerations to active inputs in how investors think about geographic exposure. The US remains the world's dominant investment market, but that dominance is now being scrutinized in ways it has not been for a generation.

The sentiment shift is measurable. A Natixis Investment Managers survey found that $63\%$ of global investors believe the politicization of US institutions weakens the country's investment case, a view shared by more than half of US investors themselves. Nearly half of global investors plan to increase geographic diversification, with Europe $(46\%)$ , Asia-Pacific $(44\%)$ , and Emerging Asia $(42\%)$ the primary intended destinations, compared with just $25\%$ that intend to increase US exposure. Actual portfolio allocations, however, don't yet reflect that shift.

Whether these changes prove structural or cyclical remains an open question. What 

[中间内容因长度限制已省略]

rough 2030

AUM GROWTH (%), 2025–2030 E

![](images/6ac4a7270620c2a707b69c071fbb29df99cceaf6dfd25cfa7efdde85cf2d54d0.jpg)

Source: BCG EXPAND Global Asset Management Market-Sizing Database, 2026.

Note: ETF = exchange-traded fund; LDI = liability-driven investment.

$^{1}$ Management fees net of distribution costs.

$^{2}$ Includes actively managed equity instruments: developed market and global.

$^{4}$ Includes actively managed equity instruments: global (excluding US), emerging market, all sector and thematic, and undefined if market is not known.

$^{5}$ Includes these actively managed fixed-income instruments: global (excluding US), emerging market, high yield, convertible, inflation linked, and undefined if market is not known.

$^{6}$ Includes these instruments: target date funds, target maturity, and outsourced chief investment officer.

$^{7}$ Includes these instruments: absolute return, long/short, market neutral, and trading-oriented mutual funds.

## About the Authors

Renaud Fages is a managing director and partner in the Los Angeles office of BCG. You may contact him by email at fages.renaud@bcg.com.

Johannes Burkhardt is a managing director and partner in BCG's Munich office. You may contact him by email at burkhardt.johannes@bcg.com.

Edoardo Palmisani is a managing director and partner in the Rome office of BCG. You may contact him by email at palmisani.edoardo@bcg.com.

Joppe Bijlsma is a managing director and partner in BCG's New York office. You may contact him by email at bijlsma.joppe@bcg.com.

Peter Czerepak is a managing director and senior partner in the Boston office of BCG. You may contact him by email at czerepak.peter@bcg.com.

Matt Egler is a managing director and partner in BCG's Sydney office. You may contact him by email at egler.matthias@bcg.com.

Dean Frankle is a managing director and partner in BCG's London office. You may contact him by email at frankle.dean@bcg.com.

Kwonyoung Jang is a managing director and partner in the Seoul office of BCG. You may contact him by email at jang.kwonyoung@bcg.com.

Mayank Jha is a managing director and partner in the Mumbai office of BCG. You may contact him by email at jha.mayank@bcg.com.

Katsuyoshi Kurihara is a managing director and partner in BCG's Tokyo office. You may contact him by email at kurihara.katsuyoshi@bcg.com.

## For Further Contact

If you would like to discuss this report, please contact the authors.

Kedra Newsom Reeves is a managing director and partner in the Chicago office of BCG. You may contact her by email at newsom.kedra@bcg.com.

Neil Pardasani is a managing director and senior partner in BCG's Los Angeles office. You may contact him by email at pardasani.neil@bcg.com.

Maël Robin is a managing director and partner in the Paris office of BCG. You may contact him by email at robin.mael@bcg.com.

George Rudolph is a managing director and partner in BCG's New York office. You may contact him by email at rudolph.george@bcg.com.

Philippe Soussan is a managing director and senior partner in BCG's Paris office. You may contact him by email at soussan.philippe@bcg.com.

Matt Sweeny is a managing director and partner in the Tokyo office of BCG. You may contact him by email at sweeny.matt@bcg.com.

Tjun Tang is a managing director and senior partner in the Hong Kong office of BCG. You may contact him by email at tang.tjun@BCG.com.

Charles-Antoine Wallaert is a managing director and partner in BCG's Paris office. You may contact him by email at wallaert.charles-antoine@bcg.com.

André Xavier is a managing director and senior partner in the Sao Paulo office of BCG. You may contact him by email at xavier.andre@bcg.com.

Ivana Zupa is a managing director and partner in BCG's Zurich office. You may contact her by email at zupa.ivana@bcg.com.

## Acknowledgments

The authors would like to thank the core team for their contributions to this work, including Kyle Johnson, Sam Kittross-Schnell, Rae Liu, Michele Millosevich, Eva Niadi, Claire Song, and Andrea Walbaum.

In addition, the authors extend the appreciation to Jatin Bajwa, Lorenzo Girardi, Mukul Gupta, Christopher Hill, Teddy Hung, Bernhard Kronfellner, Sonali Maheshwari, Bas NieuweWeme, Daniel Ollgaard, Christian Schmid, and Himakshi Srivastava. This year's report was enriched with data and insights provided by the BCG Henderson Institute and Expand Research, a wholly owned subsidiary of Boston Consulting Group.

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X.

![](images/b289ca9fabf62c91cf18a36dc7a4ba063c1dbc86b2cf0c1dc2636fb06ff44f71.jpg)
"""
