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
## Prudence, Profits, and Growth

June 2024

<table><tr><td></td><td>BCG + QEDINVESTORS</td></tr></table>

Contents
03 Introduction
05 The Funding Winter Continues, but So Does Growth
12 Today's Fintech Landscape
19 Where We Go from Here: Five Calls to Action
24 Conclusion
25 About the Authors

## Introduction

It can be easy to forget what the financial services landscape looked like two decades ago, before fintechs emerged to dramatically reconfigure banking and transacting. In the ensuing 20 years, many individual fintechs have come and gone. Others have become integral components of financial services, but the true lasting legacy of fintech is the staggering impact on our day-to-day lives and our financial systems.

And there is so much more room for growth. With the advent of game-changing technologies such as GenAI and with still billions of unbanked and underbanked individuals worldwide, we reaffirm our forecast from last year's report: we are still only in the second chapter of a longer story and fintech has vast untapped potential.

But the rules of the game are changing. The current funding chill, once passed, will leave in its wake an environment in which fintechs must invoke a different set of capabilities to succeed and thrive. Prudence—the ability to avoid adding risk to the financial system—will be as important as the ability to generate profitable growth. The prize, and the rewards for customers, will be as significant as ever, but the path to success will be markedly more difficult.

We spoke to more than 60 global fintech CEOs and investors to understand their views on the future of the sector. Combined with our own experience in the industry, these perspectives inform this report. We see nine distinct trends shaping the current fintech landscape, some new, some long-standing. Coming out of these underlying trends, we see four major themes that fintechs and incumbent banks will need to confront given that these themes are of growing and critical importance for the sector. Finally, we will explore five imperatives for players in the new fintech ecosystem that has begun to emerge.

\$1.5T

With billions of unbanked and underbanked people worldwide and GenAI's boost to productivity, the potential for fintech remains vast—we expect a fintech market size of \$1.5 trillion in revenue by 2030, up from \$320 billion today.

![](images/84d7ef1a0df5faf0ee83f6d2e8f5176aa16f71b060110dac3dd1fe1d6273ce4b.jpg)

The new watchword is prudence. Fintechs need an end-to-end view of compliance—preemptively assessing applicable regulations and proactively implementing industry-grade guidelines and controls.

![](images/bab6770bde1a61c67287d26c2347551ce2ef2aa0c2946d09b46f70fa4a2c72e0.jpg)

With connected commerce, major banks finally have an opportunity to leverage their vast data on customer needs and behaviors.

14%

Global fintech revenues have continued to grow at a robust clip—14% annually over the past two years. The biggest performance gap is found between top- and bottom-quartile fintechs across segments.

![](images/c6f951295d70efe4fbd6669193813a277eb995603de129781f96d84add88f99b.jpg)

With Pix and UPI, respectively, Brazil and India have led the way in using digital public infrastructure to broaden access to financial services and spur innovation. But the success of DPI hinges on its comprehensiveness and its full integration across systems.

GenAI is delivering huge productivity gains in precisely the areas where fintech costs are centered: coding, customer support, and digital marketing. Fintechs, relative to other financial services players, will reap the biggest productivity rewards in the near term.

+25pp

Fintechs need to—
and can—improve
EBITDA by more than
25 percentage points.
Getting there will
require a scalable cost
structure that will
deliver compounding
returns as a fintech
grows.

100M

Digital challenger banks are star performers. In Brazil, Nubank has crossed the 100-million-user level, and in Europe, Monzo reached operational profitability in the first half of 2023 and recently received additional funding to fuel ambitious global growth plans.

![](images/c853322ff3d6fdaa373004b2874cac335873148853618e5a7dfeaef9cab18d33.jpg)

The fintech IPO market will eventually bounce back, but fintechs must now tell a comprehensive equity story about how they will attract users at sustainable costs, grow profitably, and meet increasing regulatory requirements.

\$320B

By 2030, embedded finance will account for \$320 billion in revenues worldwide, led by the small and medium-size business segment (\$150 billion), the consumer segment (\$120 billion), and the enterprise segment (\$50 billion).

![](images/476b229871c48285502d39e8fa69cf2b4e8471d61d0e57ccd8fe7ff430eef4d2.jpg)

# The Funding Winter Continues, but So Does Growth

There is no shortage of capital in fintech. There was just an overabundance in 2021.

HANS MORRIS, MANAGING PARTNER, NYCA PARTNERS

It has been a sobering three years for fintechs. Coming off the highs of 2021, revenue multiples have fallen from 20 times to 4 times on average, and funding is down by 70%—and almost 50% in the last year. (See Exhibit 1.) The declines are heavier in some areas than in others. Late-stage investments (series C to E+), for example, are down by 81% to 89%, compared with 54% to 73% for early-stage funding rounds. Overall, funding is down by at least half for all fintech segments except insurance and payments. However, we believe these challenges are part of the short-term correction—a tempering of investor enthusiasm—we discussed in last year’s report and that those challenges are now beginning to abate.

Fintech funding plummeted FINTECH EQUITY FINANCING (\$BILLION)

Revenue growth was strong PUBLIC AND PRIVATE FINTECH REVENUE (\$BILLION)

## Exhibit 1 Funding and Valuations Still Down but Revenues Are Thriving

![](images/2e208eb1ed13c46b86330069221a73c71827889bd0fc98ac8f05c76b78feb383.jpg)  
Revenue multiples stabilized but are still low
REVENUE MULTIPLE FOR PUBLIC FINTECHS $^{1}$

![](images/44fceae78ee2f64d4936ab3d029c2bcf08a619bfafd3a9575af2d334e8028d0c.jpg)

![](images/d70b1a2962dabcf770a4a6e1497a9250fe2ea0049673c1203cf7c7b0d7abd01a.jpg)  
Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech Control Tower; BCG analysis. $^{1}$ Average based on market capitalization and LTM revenue for the second quarter of each year.

## The new mantra is “Grow as fast as you can—subject to positive net income and neutral cash flow.”

SERGIO FURIO, FOUNDER AND CEO, CREDITAS

Simultaneously, global fintech revenues have continued to grow at a robust clip—14% over the past two years across the board, and 21% when crypto- and China-exposed fintechs are excluded. Growth during the two-year period comprising 2022 and 2023, in fact, compares well with the 29% rate from 2019 through 2023. Differences exist in growth rates across sectors and geographies, as always, but the most compelling performance gap, across segments, is between the emerging winners—the top-quartile performers—and the bottom-quartile fintechs. (See Exhibit 2.)

Exhibit 2 The Starkest Revenue Growth Gaps Are Between Top- and Bottom-Quartile Fintechs

Difference across select sectors and geographies
REVENUE CAGR, 2021–2023

![](images/fa9ad83ed4de2141147c6c536f11f4da3ad016a4210ec186c224db810752579d.jpg)

![](images/cdcd0a5df7835ac53a6cc87a70d9be312097c180fb6d8e5b09a271af11ad7439.jpg)  
Difference between top and bottom quartiles
CAGR FOR TOP AND BOTTOM QUARTILE, 2021–2023

![](images/d33b1896e3f6020f17821f125898cb00ba1cd65d3bb064fbd48efb1eaec5a99f.jpg)  
Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech Control Tower; BCG analysis.

![](images/90b756843672599a4ff9f209e5ddb7d83ee2452f2d9bd21d364523f727c4b5d8.jpg)

Exhibit 3 Public Fintechs Are Moving Toward Profitable Growth but Have a Long Way to Go  
![](images/3302251ba6f110bb80a346eb4747a96f56a9f763fc1713868934a393ae725f06.jpg)

![](images/305433b7631c6ed6edb0f3bce9907c06906b1cc8c093322bdb7e12c3fbb6daaa.jpg)  
Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech Control Tower; BCG analysis. Note: Data is based on the top 70 public fintechs from 2022 through 2023. pp = percentage point. $^{1}$ Rule of 40 is a financial metric summing revenue growth (%) and profit margin (%).

More notably, the industry has made good on initiating the shift from a “growth at all costs” model toward profitable growth, with EBITDA margins improving 9 percentage points on average. But this shift is still in its early stages, with the strong majority of the top 70 public fintechs still operating below the “rule of 40” threshold (a financial metric that sums revenue growth and profit margin percentages). (See Exhibit 3.)

## Conditions Continue to Favor Fintech Growth

Despite the current funding challenges, the fundamentals that have fueled the fintech sector from the beginning remain in place and promise continued growth. In 2023, challenger banks in particular proved their value to investors and customers. (See Spotlight #1.) We continue to expect fintechs to reach a market size of \$1.5 trillion in revenue by 2030—growth of roughly five times over the period from 2023 to 2030. Fintechs still maintain and press their well-known advantages: a laser focus on solving customer pain points, compelling user experiences, and rapid innovation. These strengths will continue to power growth—even as the regulatory playing field is becoming more balanced and equitable, presenting a challenge of sorts for many fintechs, which have until recently operated under the regulatory radar.

The upside for fintechs continues to be vast—with 1.5 billion unbanked and 2.8 billion underbanked adults across the world. Of course, these potential customers are also available to incumbent banks, which will have their own opportunities to grow. The question is whether—and how—they will do so.

The emergence of new technologies seems to favor fintechs, at least in the near term. GenAI, for one, is proving to be an immediate boon for the sector, already delivering huge productivity gains in precisely the areas where fintechs' costs are centered: coding, customer support, and digital marketing (with improved targeting). GenAI, alongside API-based connectivity and distributed ledger technology, will provide a rapid boost for fintechs; banks, too, will benefit from these technologies, but over a longer time scale. In short, GenAI arrives at a moment when many fintechs are strapped for cash. It may well keep a number of them afloat while they address the pressing need for profitable growth.

Here are four examples:

SPOTLIGHT #1

# From Upstarts to Contenders: Challenger Banks Achieving Profitability at Scale After a Record 2023

Digital challenger banks were star performers in 2023. (See the exhibit below.) Nubank, for example, crossed the 100-million-user milestone in May 2024 and aspires to become Latin America's largest and most profitable bank in the near future—roughly one in two adult Brazilians is a Nubank customer. Meanwhile, in Europe, Monzo reached operational profitability in the first half of 2023 and recently received additional funding to fuel its ambitious global growth plans. More than half of the profitable challenger banks are located in Asia—South Korea's KakaoBank, for example—often as part of an integrated ecosystem.

Notably, there is no single recipe for a successful challenger bank. Leaders have taken unique paths to scale and profitability; what they have in common is that they have staked a claim to a lasting presence in the industry.

Leading Challenger Banks Have Demonstrated Profitability at Scale After a Record 2023

453

The number of digital challenger banks around the world

23

The number that are operationally profitable

![](images/246312800073892abc996eec551a1ce33c717aa884d87580a1cc7ba7244a4dc4.jpg)

Nubank
Crossed the 100-million-user milestone in May 2023 and is on track to be the largest and most profitable bank in Latin America

![](images/408f530aeede0630e1de85b75aef100c6cdb6d42fc776803d8ee599d6abcef0b.jpg)

Now the seventh-largest bank in the UK; it reached operational profitability in the first half of 2023 with revenue of £356 million

![](images/435882e2a537f7e937ba2ec28036cea4fd7708fb4d91f85fcfc84c7831af6053.jpg)

Grew to \$1.3 billion in revenue in 2023 with 14.5 million customers and was profitable in Q1 2024; preparing for a possible IPO in 2025

![](images/4d5b91dd9776fc30ba33bd1fca42b46f43ed2e4aa52fef438a657b89d96294ba.jpg)

Revolut
Hit \$2 billion in revenue and double-digit net profit in 2023, with more than 40 million customers worldwide

Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech Control Tower; BCG analysis.

## Nine Trends Influencing the Evolution of Fintech

Over the past year, nine trends have shaped the evolution of fintech; some of them are concentrated in specific sectors and geographies. A few are long-standing, and others represent emergent influences.

1. The Persistence of High Interest Rates. Globally, we are entering a prolonged period of higher interest rates that will continue to increase funding costs for fintechs, while private capital continues to push for profitable growth that will ultimately yield investment returns. The days of “growth at all costs,” funded by cheap capital, are well and truly over.

2. Convergence of the Regulatory Playing Field. On the regulatory front, the past year has seen a narrowing of the regulatory advantage that fintechs have enjoyed since the birth of the sector. Regulatory actions have included consent orders against several fintech sponsor banks, increased scrutiny of banking as a service (BaaS) overall, moves against crypto firms, and the proposal from the US Consumer Financial Protection Bureau (CFPB) on the supervision of big tech companies and other providers of digital wallets and payment apps. Though much work remains to create a level and fair regulatory operating environment for banks and fintechs, we believe things are trending in the right direction.

3. The Emergence of New Regulatory Frameworks Globally. Regulatory frameworks and standards governing or impacting the global fintech sector have been coming into focus. India, for example, has released new notifications to reemphasize and clarify know-your-customer (KYC) and co-lending standards for fintechs, and the CFPB is currently gearing up to develop concrete guidelines under Section 1033, a part of the Dodd-Frank act aimed at clarifying rules regarding how customer data is accessed and used.

4. The Global Proliferation of DPI. Digital public infrastructure has accelerated the adoption of real-time payments in countries including India (whose DPI is Unified Payments Interfaces, or UPI) and Brazil (Pix). (See Spotlight #2.) This three-tiered infrastructure—a national digital identity system, a payments layer, and a data exchange—creates a fertile context for fintech development. Many countries, particularly emerging markets, are looking to emulate the success of UPI and Pix. However, while the success of the India and Brazil DPIs is unequivocal, it is by no means certain that other countries—including developed markets—will be able to replicate it. Much depends upon the current market context and the maturity of the various layers.

Where the regulator has stepped in to define a framework, it's caused a huge, dynamic change in the market. When the regulator provides clarity, as in crypto and AI underwriting, all stakeholders can build more constructively.

GAL KRUBINER, COFOUNDER AND CEO, PAGAYA

SPOTLIGHT #2

# Brazil's Activist Regulators Are Cultivating a Landscape for Fintech Innovation and Growth

Brazil has become a hothouse of fintech innovation, with a thriving, vibrant ecosystem that is drawing attention globally. The most notable fintech name in the country is Nubank, which has managed the trick of building a—wildly—successful digital bank in a once cash-heavy country. But Nubank is not alone: it is one of 17 unicorns in Brazil. Other big fintech names include Creditas (a lending platform), Dock (a fintech infrastructure provider), and Ebanx (a payments provider), all with significant success in their areas of focus.

Credit is due to Brazil's central bank and regulators—primarily the National Monetary Council—which has taken an active stance in paving the way for creating infrastructure that helps enable fintech solutions to scale. (See the exhibit below.) In addition to supporting the development of the digital public infrastructure, including the real-time payments platform Pix, regulators have not been shy about regulating big tech and ensuring competition in the market. Brazil also has a flexible licensing approach, issuing both standard banking and instituição de pagamentos licenses—which allow institutions to initiate and process payments, with relatively lighter regulatory constraints.

## In Brazil, Regulation Supports Innovation and Growth

Brazil has set a clear example for how to implement integrated DPI...

Vision
"The project will be the embryo of . . . a total transformation in the country's future financial intermediation, and will consolidate . . . new forms of payment methods with the fintech industry and with open banking."
ROBERTO CAMPOS, PRESIDENT, BANCO CENTRAL DO BRASIL (BCB) IN 2020

Protocols BCB manages and operates SPI, the Instant Payments System, underpinning Pix and protocols for BR code (standard QR code)

Governance While BCB manages the directory and payments, the Pix Forum comprises representatives from banks and other stakeholders

Directory BCB also operates the DICT, the national database linking aliases (e.g., email, QR code, or a random key) and account information

Pricing

Pix is free for individuals and costs an average of 0.22% per transaction for merchants (per the Bank for International Settlements)

Sources: Companies' investor presentations; desktop research; BCG analysis.

... reshaping the financial landscape of the country

1.5x

Growth in banked population in ten years (from 57% in 2011 to 84% in 2021)

17

Fintech unicorns in Brazil

Fraud is a huge issue for everyone, everywhere. Fraud is a natural part of payments, but once it becomes too much, it's a problem. More government support is key, but as fintechs we must work together to tackle this problem.

GB AGBOOLA, FOUNDER AND CEO, FLUTTERWAVE PAYMENTS

5. Heightened Attention on Fraud and Cybersecurity. As real-time payments and GenAI become increasingly integral parts of consumer fina

[中间内容因长度限制已省略]

rtner
New York
paddington.alexander@bcg.com

## Andrew Janssens

Project Leader
New York
janssens.andrew@bcg.com

## Sooahn Choi

Consultant
New York
choi.sooahn@bcg.com

## Aaron Cormier

Lead Knowledge Analyst
Toronto
cormier.aaron@bcg.com

## QED Investors

## Nigel Morris

Cofounder & Managing Partner
nigel@qedinvestors.com

## Frank Rotman

Cofounder, Partner, & CIO
Head of Early-Stage US
frank@qedinvestors.com

## Bill Cilluffo

Partner, Head of International bill@qedinvestors.com

## Tommy Blanchard

Chief Operating Officer
tommy@qedinvestors.com

## Stefan Dab

Managing Director & Senior Partner Brussels
dab.stefan@bcg.com

## Yashraj Erande

Managing Director & Partner Mumbai
erande.yashraj@bcg.com

## Aparna Pande

Project Leader
New York
pande.aparna@bcg.com

## Yann Sénant

Managing Director & Senior Partner
Paris
senant.yann@bcg.com

## Saurabh Tripathi

Managing Director & Senior Partner
Global Leader, Financial Institutions Practice
Mumbai
tripathi.saurabh@bcg.com

## Rishi Varma

Managing Director & Senior Partner
New Jersey
varma.rishi@bcg.com

## Mike Packer

Partner, Head of Latin America
mike@qedinvestors.com

## Sandeep Patil

Partner, Head of Asia
sandeep@qedinvestors.com

## Amias Gerety

Partner, Early-Stage US amias@qedinvestors.com

## Acknowledgments

This report is a joint initiative of Boston Consulting Group (BCG) and QED Investors (QED). The authors thank their colleagues from each organization for their contributions to the development and production of the report. In addition, the authors are extremely grateful to all the participants in one-on-one interviews and panel discussions for their valuable contributions toward the enrichment of the insights presented here.

## For Further Contact

If you would like to discuss this report, please contact one of the authors.

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

## QED INVESTORS

QED Investors is a global leading venture capital firm based in Alexandria, Va. Founded by Nigel Morris and Frank Rotman in 2007, QED is focused on investing in disruptive financial services companies worldwide. QED is dedicated to building great businesses and uses a unique, hands-on approach that leverages its partners' decades of entrepreneurial and operational experience, helping companies achieve breakthrough growth. QED has invested in more than 200 companies, including 28 unicorns, across 18 countries. Notable investments include AvidXchange, Betterfly, Bitso, Caribou, ClearScore, Current, Creditas, Credit Karma, Flywire, Greensky, Kavak, Klarna, Konfio, Loft, Mission Lane, Nubank, QuintoAndar, Remitly, SoFi, Wagestream, and Wayflyer.

© Boston Consulting Group 2024. All rights reserved. 6/24

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and X (formerly known as Twitter).

bcg.com

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>
"""
