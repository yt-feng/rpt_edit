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
GLOBAL FINTECH REPORT 2026
4TH EDITION

# From Recovery to Resurgence

June 2026

![](images/b7da490814239fc30dcf51ab2d06b2da87483f26290b71dad3377a3c0014db99.jpg)

BCG +

FINANCIAL TECHNOLOGY PARTNERS

Contents
03 Key Highlights
04 Introduction
05 The State of Fintech:
From Recovery to Resurgence
11 Seven Trends That Will Shape the Industry
36 Now What? Calls to Action
38 Conclusion
39 About the Authors

\$504B

Total global fintech revenue surpassed half a trillion dollars, achieving record highs

22%

Global fintech revenues continued to show strong growth at 22%, with trading and investments and deposits leading the pack with about 38% and 30% YoY growth, respectively

400bps

Average EBITDA margin improvement for the largest public fintechs from 2024 to 2025

42

Number of global fintech IPOs in 2025, up 50% year over year

>\$3T

Digital asset market capitalization growing, with crypto at \~\$3 trillion, stablecoins at \~\$300 billion, and tokenized real-world assets at \~\$30 billion

4%

Share of global banking and insurance revenue pools penetrated by fintechs, with large, untapped opportunity in B2B verticals

>4x

The fintech revenue growth rate was more than four times greater than that of incumbents

\$58B

Fintech equity funding in 2025, up 53% year over year as investor appetite returned, albeit selectively

5x

Observed uplift in developer productivity at fintechs using AI

65%

Share of stablecoin holdings tied to crypto trading, underscoring how concentrated digital-asset adoption remains today

![](images/2caa4c7849cd9a6468f4e910bf78b05ba27324a0730cb10481d62f5f37f45df0.jpg)

## Introduction

After several years characterized by market correction, capital scarcity, and skepticism concerning the durability of many business models, the fintech sector showed strong revenue growth of 22% in 2025. Global fintech revenues surpassed half a trillion dollars and grew over four times as fast as incumbent revenues.

Growth has returned, but in a new form. The fintech sector has not simply recovered from the 2023/2024 reset, with its lower valuations and funding; it has matured into a demanding environment where scaled leaders are widening their advantage, new technologies are reshaping the economics of financial services, and profitable growth has become the expectation rather than an aspiration. And yet the opportunity ahead remains enormous: Fintech accounts for about $4\%$ of the global financial services revenue pool—large enough to be considered a distinct, mature sector, but not so large that there isn't meaningful white space to target.

Investors are placing more emphasis on which business models can capture the next wave of value, which technologies can create durable advantage, and how far players can extend into adjacent products, geographies, and infrastructure layers while navigating a more complex regulatory and geopolitical environment.

These dynamics are urgent in 2026 because the basis of competition is changing. AI is reshaping how financial services are built and delivered, with early proof of value concentrated in a set of operational and workflow-heavy use cases that are narrower than the hype would suggest. Digital assets have regained momentum; however, while the tech foundations have strengthened and regulations have become clearer, widespread adoption will depend on proven value creation. Regulators across the globe are resetting the distinction between banks and fintechs. At the same time, scaled fintechs and neobanks are expanding their offerings into fuller financial platforms, while a new generation of AI-native entrants is emerging alongside them.

This report draws on conversations with fintech executives, investors, and industry leaders across global markets, and our own expertise, research, analysis, and proprietary FinTech Control Tower platform. It begins with an assessment of where fintech stands today, then examines seven trends that are shaping the future of the industry. It closes with a set of implications for the institutions that hold a stake in the emerging new landscape.

![](images/a1d5276e78776e37919b28323519bf1b39d6ff7cd1e8667293a4b219034432e5.jpg)

# The State of Fintech: From Recovery to Resurgence

There has been a striking reversal of mood within the global fintech sector.

Two years ago, the sector was still working through the aftershocks of the 2021 reset, a period during which capital was scarce, valuations compressed sharply, and questions about the durability of many business models were mounting. Now, the tone has changed. Global fintech revenues surpassed half a trillion dollars in 2025, growing 22% year over year. (See Exhibit 1.) That also means fintechs outgrew traditional financial services four-fold and now account for approximately 4% of total global financial services revenue, up from 3% the year prior. Public fintech revenue multiples have also recovered, albeit modestly, rising 16% year over year. In other words, fintech has weathered the reset and is beginning to outgrow it.

# Global Fintech Revenues Break Half a Trillion Dollars in 2025

Global fintech revenue by vertical (2021–2025, \$B)

![](images/89ccc6a905f4700688f29717fc0546bdb01892018893b44c843c1f24e4557ce8.jpg)  
Global fintech revenue by region (2021–2025, \$B)

![](images/b1a978d4f0436471c08bec963ae4e949574373497281bc71e421f620127b29a9.jpg)  
Sources: S&P Capital IQ; BCG FinTech Control Tower; BCG Banking and Insurance Revenue Pools; BCG analysis.
Note: Revenues from prior years have been restated to include final reported revenues at the company level. Health insurance is excluded.

Growth has been broad, but not uniform. Some subsectors are clearly breaking away from the pack. Trading and investments, along with deposits, were among the fastest-growing segments, expanding 38% and 30%, respectively, in 2025. (See Exhibit 2.) Meanwhile, payments remains the dominant fintech vertical. (See Exhibit 3.) Regionally, Asia-Pacific (APAC) was the fastest-growing market at 25%, driven in part by digital banking and crypto trading platforms in Japan and South Korea, alongside Southeast Asia, notably Singapore and Indonesia. Europe also outperformed the global average, growing 24%, supported by neobanks moving into adjacent products and geographies, continued buy-now-pay-later momentum, and a more accommodating regulatory environment. North America, at 21%, grew roughly in line with the global market, while Latin America, though still strong at 15%, somewhat lagged the global average. However, the region has seen the highest overall growth in the years since 2021, with a CAGR of 44%. The Middle East and Africa (MEA), at 20%, maintained strong momentum, though growth was moderated by challenging regulatory conditions.

Trading and investments, along with deposits, were among the fastest-growing segments. Meanwhile, payments remains the dominant fintech vertical.

## EXHIBIT 2

## Fintechs Grew >4x the Rate of Incumbents

Fintechs account for \~4% of global financial services revenues

TOTAL GLOBAL REVENUE, 2025 (\$)

Fintech revenue growth outpaced incumbents across all verticals
FINTECH VS. INCUMBENT REVENUE GROWTH YOY, 2024–2025 (%) $^{1}$

![](images/534d6a528c0d757423bce096ffcd5f1b69fa2cfb75a2d9808058590995e3984c.jpg)  
Sources: S&P Capital IQ; Pitchbook; BCG FinTech Control Tower; BCG Banking and Insurance Revenue Pools; BCG analysis. $^{1}$ Excludes “financial infrastructure,” as the category is not relevant for incumbent financial institutions.

## EXHIBIT 3

Payments Remains the Dominant Fintech Vertical, with Deposits, Trading and Investments, and Lending Gaining Scale

REVENUE DISTRIBUTION OF FINTECHS GENERATING >\$0.5B IN 2025

![](images/d6db941504902e7db89b7ef6976bbb2126c550626051b0d4df8e2f849026def2.jpg)  
Sources: S&P Capital IQ; Pitchbook; company filings; BCG FinTech Control Tower; BCG analysis.

Financially excluded
M-PESA (at least one account)
Formally included $^{2}$ (no M-PESA account)

Part of this regional divergence reflects differences in operating conditions, not just differences in demand. In the United States, scaled fintechs are increasingly pursuing direct federal supervision through the Office of the Comptroller of the Currency national trust and banking charters. This allows them to bypass the intermediary costs of partner banking, move faster on product innovation without partner sign-off, and gain fuller end-to-end ownership of the customer experience. Similar moves are also visible in parts of Europe, where clearer licensing and market rules are supporting fintech expansion. By contrast, in markets such as China, India, and parts of the Gulf Cooperation Council (GCC), stringent regulations continue to make scaling more difficult for fintechs.

At the same time, in many emerging markets, fintechs have made progress on consumer inclusion, often by building on top of enabling public payment infrastructure. Mobile money, digital wallets, low-cost payments, and simpler onboarding have expanded access at real scale. The Bank for International Settlements reports that Brazil's Pix had signed up 67% of adults a little over a year after launch, supported by free person-to-person payments and low merchant charges. The National Payments Corporation of India (NPCI) reports 22.64 billion Unified Payments Interface (UPI) transactions in March 2026 alone, and NPCI and BCG report that UPI now handles more than 20 billion transactions a month and 84% of India's digital retail payments. Furthermore, the Bank for International Settlements describes the UPI model as having made “rapid strides” in financial inclusion. In Kenya, M-PESA serves roughly 80% of the addressable population through mobile banking, while in the Philippines, GCash now reaches roughly 75% of the population with mobile payments, up from about 5% in 2015. (See Exhibit 4.) These examples are proof that fintechs can move from niche disruption to mass-market utility when the market structure and distribution model are right.

## EXHIBIT 4

# Fintechs Have Stepped in to Provide Solutions for the Underserved, Fostering Financial Inclusion in Emerging Markets

LEADING
CASE STUDY

Latin America
Nubank

Middle East and Africa
M-PESA

Since Nubank launched in 2014, the unbanked population in Brazil has declined from \~30% to 10% $^{1}$

Since M-PESA's launch in 2007, the financially excluded population in Kenya has declined from \~50% to \~10%

Asia-Pacific
GCash

Since GCash's explosive growth starting in 2015, the financially excluded population in the Philippines declined from \~70% to \~20%

Brazil

![](images/df0ce5837a867bd7d4bf5a7f0e107505aefb8608960186389ba05554035cbc15.jpg)  
Kenya

![](images/a993cbf1ab01d12c2b788f4f33bedfd8662181ce1f3646e8942cce3dd388f3e6.jpg)  
Philippines

![](images/14959d2fd13ef685c057e5dbba78c964584e0b330ffb38636204a62f040117e8.jpg)  
Sources: World Bank; UN World Population Prospects; Kenya National Bureau of Statistics; Central Bank of Kenya; Safaricom Reports; Philippine Statistics Authority, Bangko Sentral ng Pilipinas FIS, Globe Telecom/Mynt/Gcash Reports; BCG analysis.

## Investor funding has been much more selective than it was in 2021, rewarding players with clearer economics and credible paths to durable scale. This selectivity is a sign that the sector is maturing.

Growth is taking a more sustainable form than in the past. The fintech rebound is not being fueled by speculative optimism or cheap capital, but by operating performance. Among the largest 85 public fintechs, EBITDA margins increased 4 percentage points in 2025 to 20%, and 74% of these firms are now profitable versus 68% in 2024. (See Exhibit 5.) Investor funding has been much more selective than it was in 2021, rewarding players with clearer economics and credible paths to durable scale. This selectivity is a sign that the sector is maturing and is reflected in how investors are allocating capital across venture stages. From 2023 to 2025, Series E or later funding grew over 210%, while Series A and B grew roughly 15% and 30%, respectively, and seed and angel contracted by about 10%.

Maturation is also evident in where capital is going. Equity funding rose 53% to \$58 billion in 2025, but funding growth was not evenly distributed. (See Exhibit 6.) Trading and investment fintechs captured roughly one-third of all funding, up from about one-fifth the year before, while funding growth was strongest in the Americas and APAC, and more moderate in MEA.

## EXHIBIT 5

## Average EBITDA Margin Increased 4pp, While Share of Profitable Public Fintechs Grew

AVERAGE EBITDA MARGIN (%)

![](images/da8d097ef7af8ee68b4eae4e575a52b1014ab854f690382103b37653d843698b.jpg)  
SHARE OF FINTECHS THAT ARE PROFITABLE $(\%)^{1}$

![](images/7ddb662b02b436fbe44a61caa4ec2b875367b7afcfed8900a476842353ed4e25.jpg)  
SHARE OF FINTECHS ABOVE THE RULE OF $40^{2}$ (\%)

![](images/a72370adcbc7936ecbd36643fdf279425053be967a55c7bf311b21b6d179bc6b.jpg)  
Sources: Financial analysis of the top 85 fintechs, S&P Capital IQ; Pitchbook; BCG FinTech Control Tower; BCG analysis. $^{1}$ Profitability defined as EBITDA or EBT.  
$^{2}$ Rule of 40 is a financial metric measuring whether the sum of revenue growth (%) and EBITDA margin (%) is greater than 40.

REVENUE MULTIPLE FOR PUBLIC FINTECHS

## EXHIBIT 6

Equity Funding and IPO Activity Have Accelerated, While Valuations Have Grown Moderately

FINTECH EQUITY FINANCING (\$B)

![](images/0fc1f40440d4e496cf24eb1dbef9bdd1ff0f73194a0f8d7c1b8f3ca4484667f8.jpg)  
2025 funding rebound has continued into 2026, with Q1 equity funding reaching \$14.8B, surpassing 2025 Q1–Q3  
Sources: S&P Capital IQ; Pitchbook; BCG FinTech Control Tower; FT Partners proprietary database; BCG analysis. $^{1}$ Region based on company headquarters, not listing location.

A similar, focused approach is visible in exit markets. In 2025, fintech IPOs rose 50% year over year, from 28 to 42. According to FT Partners' proprietary database, M&A accelerated even more sharply, climbing from \$105 billion in deal volume in 2023 to \$184 billion in 2024 and \$251 billion in 2025. This increase was consistent across most regions, with deal volume up most notably in Asia (roughly 110% YoY) and in North America (40% YoY).

Even so, public markets remain a constraint on the sector. The 30 largest global fintech IPOs of the last five years have trailed the broader financial services sector by roughly 24 percentage points in annual total shareholder returns (TSR). That underperformance is an important reminder that the sector's improved operating profile has not yet translated into public market confidence. Fintechs may be growing faster, but public investors are still asking hard questions about profitability, customer concentration, compliance maturity, and the durability of growth.

For years, it has been understood that technology-enabled players could provide an easier, faster, cheaper offering than incumbent banks. This remains true, but it is no longer sufficient to describe the sector. Today's fintech leaders are not just conquering their niche. They are increasingly building broader financial ecosystems, embedding themselves into customer workflows, and in some cases serving as foundational rails for financial activity.

These developments make the current moment materially different from both the “correction years” and the earlier boom years. Fintech has rebounded, but into a market that is more mature, more selective, and more strategically consequential for the long-term structure of financial services. Growth persisted strongly. Capital returned. Ambition returned. But the basis of competition is changing. It is no longer enough to be digitally native, fast-growing, or category-creating. The market is increasingly rewarding fintechs that can scale with discipline, meet more demanding regulatory and capital market expectations, and translate new technologies into real operating advantage.

The state of fintech in 2026 is a sector in resurgence, but without unfounded euphoria—more established, but still expanding into meaningful white space. The fintech spring is in full bloom.

![](images/59ff21182c9c912d2c6d01254ffeb75113fd62abf2d30644edbeb81ed02e4820.jpg)

# Seven Trends That Will Shape the Industry

## Growth alone will not determine the next fintech winners.

Success will be determined by how decisively firms navigate a volatile landscape of shifting regulations, evolving market structures, and intensified technological competition. The following trends will exert the most influence on the fintech sector in the coming years.

## AI at Scale: Not Yet, Not Equal

AI is now the most important technology theme in fintech. But the industry's relationship to AI is still characterized more by aspiration than execution. Over the last year, the conversation has shifted from whether AI matters to where it is beginning to create material value, where it is overhyped, and which players are structurally best positioned to use it to develop lasting advantage. This is where we see an emerging divergence in adoption maturity between companies that are AI-native and those applying AI to their existing operations.

One point is clear: AI will meaningfully reshape financial services. Predictive, generative, and agentic AI are already improving how fintechs build products, manage risk, serve customers, and run internal operations. But the industry remains in the early stages of scaling these capabilities. The strongest near-term gains are coming in operational and workflow-heavy domains rather than in fully autonomous consumer experiences.

In 2024 and 2025, much of the AI debate centered on possibility. In 2026, the sharper question concerns proof of value. AI is already delivering real value in underwriting, fraud, anti-money-laundering (AML), know-your-customer (KYC), document extraction, customer support, software development, and a range of finance and compliance workflows. It is reducing cycle times, compressing labor-heavy tasks, and allowing firms to do more with the same or smaller teams. What it has not yet done, at least broadly, is reinvent financial services on the customer-facing side. That part of the story is still to come.

## Generative AI is proving itself first in process-heavy domains, particularly in engineering excellence.

Generative AI is starting to reach enterprise scale in use cases that are operationally intensive: software development, document extraction, compliance and risk workflows, and customer support. The biggest gains are not coming from isolated copilots, but from redesigning how work gets done. Firms seeing the most value are redesi

[中间内容因长度限制已省略]

 part of the core infrastructure of financial activity. That progress does bring more demanding expectations, such as stronger public-market scrutiny and heavier compliance burdens. It also reflects something more important: Fintech is no longer just proving it belongs, it is helping shape the ongoing evolution of financial services.

At the same time, the significant opportunities that lie ahead will be captured by firms that adopt AI beyond workflows and into operating models, expand into new markets with a strong core product that meets local pain points, and translate early product gains into durable advantages in trust, distribution, and regulatory footing.

A great deal of white space still remains, and the next chapter should be one of the most exciting yet. There is ample room for continued disruption across B2B financial services, digital assets, consumer platforms, and the software and payments layers underpinning modern finance. The firms that combine scale, innovation, and regulatory readiness with real execution discipline will be best positioned to capture that opportunity and turn it into lasting advantage.

## “

In the short term, AI disruption is clearly a way for companies to get ahead: things become cheaper, faster, and more efficient. But over the longer term, everyone will have access to the same technology and what looks like an advantage today could disappear. It’s not yet clear what competitive differentiation will look like five years from now, but execution speed will likely remain one of the few durable moats.”

Sergio Furio, Founder & CEO, Creditas

## About the Authors

## BCG

Deepak Goyal
Managing Director & Senior Partner, New York
goyal.deepak@bcg.com

## Inderpreet Batra

Managing Director & Senior Partner, New York
batra.inderpreet@bcg.com

## Alexander Paddington

Managing Director & Partner, New York paddington.alexander@bcg.com

## Stefan Dab

Stefan Dab
Senior Advisor, Brussels
dab.stefan@advisor.bcg.com

Samer Dib
Principal, New York
dib.samer@bcg.com

Peter Clark
Project Leader, New York
clark.peter@bcg.com

## FT Partners

Steve McLaughlin
Founder, CEO & Managing Partner
steve.mclaughlin@ftpartners.com

## For Further Contact

If you would like to discuss this report, please contact the authors.

Michelle Jeong
Consultant, New York
jeong.michelle@bcg.com

Thomas Lloyd
Manager, London
lloyd.thomas@bcg.com

## Saurabh Tripathi

Managing Director & Senior Partner; Global Leader, Financial Institutions Practice, London
tripathi.saurabh@bcg.com

## Matthew Kropp

Managing Director & Senior Partner, San Francisco kropp.matthew@bcg.com

## Kunal Jhanji

Managing Director & Partner, London
jhanji.kunal@bcg.com

Peter Dewey
Managing Director & Partner, Seattle
dewey.peter@bcg.com

Greg Smith
Managing Director
greg.smith@ftpartners.com

## Acknowledgments

This report is a joint initiative of Boston Consulting Group (BCG) and Financial Technology Partners (FT Partners). The authors thank their colleagues from each organization for their contributions to the development and production of the report. In addition, the authors are extremely grateful to all the participants in one-on-one interviews and panel discussions for their valuable contributions toward the enrichment of the insights presented here.

## Boston Consulting Group

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X.

## FT Partners

FT Partners is the leading investment bank exclusively focused on FinTech. Founded in 2001 by Steve McLaughlin—formerly a senior banker in Goldman Sachs' Financial Technology and Financial Institutions Groups—the Firm has established itself as the premier advisor in the industry, closing hundreds of M&A, capital raises, and IPO transactions across all sectors of FinTech globally, including Payments, Digital Banking, Blockchain & Crypto, WealthTech, InsurTech, and Office of the CFO. FT Partners' deep industry expertise and tailored approach have earned the Firm its reputation for delivering exceptional results for its clients.

FT Partners has advised on many of the industry's most significant transactions, including Revolut's \$1.25 billion Series E at a \$33 billion valuation, Deribit's \$4.3 billion sale to Coinbase, Divvy's \$2.5 billion sale to Bill.com, Truebill's \$1.3 billion sale to Rocket Companies, and Bilt's \$250 million financing at a \$10.75 billion valuation.

![](images/5208938f8aac64690ee682cdf49cfa96b3939091639a16bfe9980e8ccf39088f.jpg)

BCG +

FINANCIAL TECHNOLOGY PARTNERS

![](images/b3e517083cc6425278ea17bb2538e0b674db9c9074c0172d5cbc3260759a241a.jpg)
"""
