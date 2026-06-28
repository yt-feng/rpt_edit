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
BCG

# MY Family

## Understanding How Malaysian Families Make Decisions

A Companion to MY Impian: Uncovering the Malaysian Dream

June 2026

By Nurlin Mohd Salleh, Anis Mohd Nor, Aditi Bhatia, Omar Akbar Khan, and Haris Mohd Zukki

![](images/f20d63c30bd37092ef6bd4e481bdec5aeb2c8182144f911b541d93cf800574f4.jpg)

## BCG

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.

## Table of Contents

01 Foreword

03 Methodology

04 Who is the Malaysian Family?

13 What do the Malaysian Family Prioritize?

16 How do Families Spend?

26 How are Trade-offs Made?

35 Final Thoughts

![](images/ba150069872a441b30f5f7fd4238317651a505402ad8b2a79dab73ef7d22a066.jpg)

# Foreword

# In most Malaysian homes, the most important conversations don't happen in offices or meeting rooms. They happen after dinner, when the plates have been cleared and the family is still at the table.

A father mentions the car insurance is due. A mother says the children's tuition fees have gone up again. A grandmother wonders aloud whether it is time to see a doctor about her knee. A son or daughter, just back from their first job, quietly offers to chip in.

No agenda is set. No minutes are taken. But by the time everyone gets up from the table, something has been decided. Money has been allocated. Someone's needs have been prioritized. Someone else's has been deferred.

This happens every day, in households across the country—whether in a terraced house in Petaling Jaya, a kampung home in Kelantan, a flat in Penang, or a longhouse in Sarawak. The details differ, but the dynamic is the same. The Malaysian family is where individual aspirations meet collective reality, and where trade-offs are negotiated with limited resources and unlimited responsibility.

Last year, BCG's MY Impian report delved into what individual Malaysians dream of. The answer was clear: financial freedom alongside physical and mental wellbeing. But MY Impian also left a question unanswered. Dreams belong to individuals. Decisions belong to families. What happens when a husband's priority meets a wife's trade-off? When Gen Z aspirations collide with the cost of an elder family member's medication?

MY Family was designed to answer that question. Through a nationally representative survey of over 1,500 households, we set out to understand how Malaysian families actually make decisions as a unit—who earns, who spends, who decides, and what happens when priorities compete for limited resources.

What we found is a nation of families that are more collective, and more resourceful than they are often given credit for. But, when seen in focus, it is also more fragile than they would like to admit.

We hope these findings are useful to anyone who serves Malaysian families, whether through products, policies, or public services. Because the more accurately we understand the family, the better we can support it.

![](images/c99709c65fced64514f88f5f6e3bdd1925f9af60ceb9ba3d423a19eb0b2cd0f4.jpg)  
NURLIN MOHD SALLEH
Managing Director & Partner, and
Head of BCG Malaysia

![](images/5b0a0e418d7f350f1015b53992aae7d48e3c036bea14be7a39adaca321ee01c3.jpg)  
Image generated by AI

## Introduction

Family is a cornerstone of our lived experience. But what does that mean in a modern Malaysia? MY Family is designed to bridge the gap between the dreams of the individual uncovered in MY Impian and how decisions are made as a family. Where MY Impian asked ‘What do Malaysians dream of?’, this report asks: Who is the Malaysian Family? What do they prioritize? How do families choose? How are trade-offs made?

We all have a sense of what family means to us, but we must also recognize that our circumstances—both personal and

national—influence the lived reality. The economic backdrop matters a lot. Medical inflation currently runs at approximately 15% annually. Housing affordability is a national concern. Only 36% of families trust the school system enough to skip private tuition. These pressures do not affect individuals in isolation, they affect families—yours, your neighbor’s, your friend’s.

The demographic context is also shifting, providing new pressures and possibilities for families. Fertility dropped to an estimated 1.6 children per family in 2025, below the rate required for a steady population. Life expectancy is rising. The combination of fewer children and longer-lived elders intensifies pressure on working-age Malaysians in the so-called ‘sandwich generation’.

The stakes are rising for the nation and the rakyat. Subsidy rationalization is on the national agenda. Healthcare costs are outpacing wages. The generation that built Malaysia's middle class is aging, while the generation replacing them earns less in real terms and has fewer children. The multigenerational household, once a cultural choice, is increasingly an economic necessity. Understanding how families actually function, who earns, who decides, who absorbs the cost when something gives, is no longer optional. It is the starting point for any institution that wants to serve Malaysians as they actually live. Because if we don't understand our families, can we truly understand our nation?

## Methodology

The MY Family study is based on a nationally representative survey of over 1,500 Malaysian citizen households, conducted in April 2026. [Exhibit 1].

## EXHIBIT 1

## Survey sample composition

Location $^{2,3}$

![](images/d31ef7ec3436075b386fed83d792ea6d07d4cca155f7f345292de6f61d6730a2.jpg)  
Urban/Rural $^{3}$

![](images/249ab5b5a3c14a82f811e033cf7357dd8abd20c0f7c69ecabcbf344343c80271.jpg)  
Monthly Household Income $^{2}$

![](images/5ede15535e483e6e5aeee19d1349255e8019e5d3df7610265b1d76b8c69b371e.jpg)  
Ethnicity $^{2}$

![](images/d0452864bdc561f5f6b0f974a8db4f2bc13fb2561a69409228c27d26636491ad.jpg)  
1. Malaysians Citizens only; Sample Size = 1500 ; 2. Department of Statistics Malaysia (DOSM), Household Income and Expenditure Survey 4. DOSM, Population and Housing Census of Malaysia, 2020 4. Eastern Region: Pahang, Kelantan, Terengganu; Northern Region : Penang, Perlis, Perak, Kedah; South Region : Johor ; Central Region : Selangor, Negeri Sembilan, Melaka, Federal Territories of Kuala Lumpur and Putrajaya; East Malaysia: Sabah, Sarawak, Federal Territory of Labuan

The research was carried out in partnership with a leading quantitative research firm. The sample reflects Malaysia's household profile by location, urbanicity, household income, and ethnicity, benchmarked against the Department of Statistics Malaysia's (DOSM) Household Income and Expenditure Survey.

To complement the quantitative data, we partnered with a specialized ethnographic research firm to add qualitative depth. This included four video interviews with Malaysian families representing different family structures, with varied geographic locations, and income levels.

All qualitative work was conducted by a third-party organization through a moderator with deep expertise in Malaysian customs and behaviors, ensuring that foreign biases did not influence the results.

With this rigorous process, we are confident in the quality and integrity of our findings, which are presented in the pages that follow.

# Who is the Malaysian Family?

## Four family structures, each member with a role to play

Malaysia's families are broadly characterized across four family structures of (1) multigenerational, (2) nuclear, (3) nested, and (4) independent, where each member has their own role to play. [Exhibit 2.]

## EXHIBIT 2

## Structures and roles within the Malaysian Family

![](images/ce7c34dd6500e36586b49b352d75509a962c8f71348c8d7a0c5f2ac997c8de01.jpg)

## Each with a role to play; the husband the pillar, the wife the engine, elders the safety net turned dependent, children the rising influence

## Husband Primary decision-maker, breadwinner and spender

![](images/9a25ec14a1a5fd7b8ef911617adfb51402c1abbd333cda0276a3dfd670848a09.jpg)

\- Most involved, with \~70% involved in decisions made by the family

## Wife Runs the day-to-day, while also bearing responsibility to provide

• Primary decision maker for family finances, and long-term capital spending

\- Main decision maker in day-to-day spend such as groceries, dining out, and baby care

## Elders Safety net now, dependent later

\- Declining influence over time, receding decision making to the husband and wife

\- Earner in \~80% of families, highest of any family member

\- Gaining influence over time, as they age and mature

\- More than half (\~60%) earn for their families

\- When they earn, they make almost as much as the husband

\- \~40% earn in nested families, but only \~10% in multigenerational

\- Under 18 and don’t contribute to income

![](images/15db2c896aba0893ce46f63369b91f2fd5051b9c07a45dd10f5da5ed331778e3.jpg)

If structures differ, and everyone has their own role to play, are products and policies designed to target the right family members?

## Husband – the primary decision maker, breadwinner and spender

The most involved family member in household decisions, with 73% of husbands involved in all decisions made. He leads on family finances and long-term capital spending: investments, vehicles, housing. He earns in approximately 80% of families, the highest of any member. And he is the primary spender, directing roughly 60% of the family budget. In most Malaysian households, the husband holds the broadest role: he earns the most, spends the most, and has the final say on the biggest financial commitments.

## Wife – the engine running the day-to-day, while also responsible to contribute financially

She leads on groceries, dining, and baby care, the daily consumption decisions that keep the household functioning. But she is not only a spender. More than half of wives ( $\sim 60\%$ ) earn for their families, and when they do, they earn almost as much as the husband. She directs approximately $30\%$ of the family budget. The wife's role defies simple categorization: she is simultaneously a provider and a household manager, contributing nearly equal income but shouldering a disproportionate share of the daily spending decisions.

## Elders – safety net now, dependent later

In nested families, 37% of elders earn and contribute to household income. In multigenerational families, only 12% do. Their decision-making influence declines over time, gradually receding to the husband and wife as the family matures. They spend less than they earn, functioning as a quiet financial buffer for the household. But the trajectory is clear: today's safety net becomes tomorrow's dependent. The elder who subsidizes the family now will eventually need the family to subsidize them.

## Children – the rising influence

Under 18 and not contributing to income, but not invisible either. Children account for approximately 5% of family spending, and their influence over household decisions grows as they age and mature. They are the emerging voice in the family, not yet shaping the big financial calls, but increasingly present in the conversations that lead to them.

![](images/9a451fdf19db16abd735bd9547b951c1e316429379d36cdf23f593cfe7f6f3b0.jpg)

We sit together and talk about what we want. Although they look to me for the final decision, I actually base my decision on their reactions.

ALIA
Mother, Multigenerational Family

## Structure

The majority (73%) of Malaysian families have children under 18. Half live with their elders. This demonstrates that the Malaysian family is, in most cases, built on a dynamic of care

## EXHIBIT 3

and support—regardless of which way the age gap leans. Together, these form four primary structures of the Malaysian family. [Exhibit 3.]

## Four Malaysian family structures

## Not with elders

![](images/9eb6578558d926d7cd5b2fc95ede757731448f3e4a87d72f4a047d542960cf7c.jpg)

Children

![](images/4bf4874c6cd32b27a4784ba1af93a2644ed462bfb76af98c66c6ccfde6eface7.jpg)

![](images/caf40bab1570b9b5b8443e48b7fced0d826ad26cac936d3c25a59bc14e3c3178.jpg)

No Kids

Independent (DINK/SINK)

![](images/8558db4154da05c7efdc42d6ace56c69dfeeb8e786b16e45bf9fda05bc8585a6.jpg)

![](images/a2649f411301e958be0f170bc599403ee1baedb35fb9c7c07cb1b1e13231722c.jpg)

![](images/52fee55b9df01a3c9b12d8becda00119ae6e2b36eccbff37eddfe61b64edabc3.jpg)  
37% Multigenerational

## Together with elders

![](images/a858ae12c6f73547dff9cd615bb5c669716ecebaa34f1f23203b8d1321c1cbfa.jpg)

![](images/cfa104a7cd071d4413f929debf06bb2408912d85b921fe299b64e1cd5854957f.jpg)  
14% Nested

![](images/e545c57858ead41c01a5d6bb33d5def313f0aba8148d08d04d318d142dae4cde.jpg)

![](images/1b58f70806897215770fb0f6336875b6c2cfa9ac972b908ee54989c004c6c8ec.jpg)

## Decision-making roles

While earnings may be equal, the guiding factors for family decisions are less evenly split [Exhibit 4]. 73% of husbands are involved in all decision making for families. On the other hand, only 56% of wives are involved in all decisions.

However, patriarchal does not mean unilateral. Our findings show that Malaysian families often act in consensus, with the majority of decisions made by many, not by one.

## EXHIBIT 4

## Involvement in household decision-making

\~70% of husbands are involved in all decision making, while wives are in \~50%; children have least say  
![](images/27940a33dcb3752ea25685ea44990bd104b6b2afe387abbbc60fad21b33c9a62.jpg)  
Source: BCG Survey on the Malaysian Family, April 2026 (n=1,502)

There is a clear division of domains in Malaysian households, a lived experience which many of us may recognize. [Exhibit 5.] Our research shows that husbands set the family budget and lead decision making when it comes to long-term capital spend: vehicles, housing, appliances, healthcare and

education. Wives largely take control of day-to-day consumption expenses: groceries, dining, baby products and travel. The lines of a Malaysian household are relatively consistent, and few venture beyond them.

## EXHIBIT 5

## Primary decision-maker by spending category

While husband or wife is the primary decision maker, decision-making still takes consideration from multiple family members

Primary decision maker and number of people involved in the decision

![](images/80b836348b831f43fdae5a84e57ac6bd11c110f62e257df4459d2d146af46c0c.jpg)  
Source: BCG Survey on the Malaysian Family, April 2026 (n=1,502)

Two important family dynamics shift over time—children gain more say as they grow older, while elders gradually cede ground. In multigenerational households, elders and husbands compete for influence at early stages, but in a familiar pattern, elders step back as the family matures. [Exhibit 6.]

## EXHIBIT 6

## Decision-making trends over time

![](images/363373b6632e75bf7f060bf0ce9624b4c71a30f6d48baa3c8fe4277573b3eb93.jpg)  
Source: BCG Survey on the Malaysian Family, April 2026 (n=1,502)

## Income dynamics

Most families are dual-income households with approximately 70% of families having at least two income earners. [Exhibit 7.] The husband is most likely to be the breadwinner, being the income earner in 72% to 89% of families, followed by the wife at 60% to 66%. Elders support where they can, with 13% to 37% of families with three income earners across

multigenerational and nested structures. Elders tend to be earners in nested structures, typically while they are still young. As they age and the family progresses towards a more multigenerational structure, fewer elders earn and transition towards dependents.

## EXHIBIT 7

## Who are the earners in the household

## Husbands earn in \~80% of families, wives earn in \~60%

## Who are the income earners by family structure (% of families)

![](images/d84ce1454640a93c4a08b8c8beb8184464deffe42e0cce20e541567fe79d20e4.jpg)

## “

He is still the breadwinner. I feel a man, a father, a husband should take that role. [But when it comes to the day-to-day, groceries, bills], Usually I handle it. If I do not handle it, someone will forget to pay, especially my husband.

ALIA Mother, Multigenerational Family

![](images/a6b3fa0a2d74b9f9051948754d7295ae972344f142a20ab8b3099864adf01eef.jpg)

![](images/5d8b1f48d59d9a98c609bacff93d9ccad9deb6ac3b18307419fae46d068f887a.jpg)

![](images/e4b1faea6931f5f44785b46b55beaeacc7f220b8981255ab5d651f217e11af88.jpg)

If wives contribute nearly half of household income but remain largely invisible in labor force statistics, what are we missing about women's economic participation?

![](images/ae3f47565d0652d51b48560654098486b04f6a7e82b72f309c350597a0aaaf75.jpg)

When both spouses work, the split of earnings is equal. That's shown in the fact that dual-income, nuclear families have broadly the same split between husbands (52%) and wives (48%). [Exhibit 8.] Even multigenerational families, with three earners in a household, have a roughly equal split between husbands (50%) and wives (45%), with a small top up from elders (5%). Meanwhile, in nested households, elders contribute up to 21%.

This shows clearly that women are active income earners across all family constructs. This is an important snapshot for policymakers, providing a valuable window into earnings for women who typically represent approximately 70% of those outside Malaysia's formal labor force. These earnings demonstrate that women's contribution and economic participation extends beyond formal employment, potentially through informal or unrecognized channels.

## EXHIBIT 8

## Income split in dual and multi-earner households

Income is almost a 50/50 split in dual income families; in 3 income families the load is partially redistributed to elders

## What is the median income split among income earners?

![](images/777429999da5fa9f633afa9f97fa49a3baa8c97307ff7e48de3b76c102cfd2dc.jpg)

![](images/2544155ff345ac12568951050441ec30f3ffd6e816e5683b259d2f79c51cfff7.jpg)

![](images/5a09cf3c91ce55eaea579fc9e9e40fb3545193cc5d86f6d3981e4b069c212bfb.jpg)  
Earns \~50% of the family's income across structures  
Independent (Dual income)

![](images/3d3cc96a71e73833c62e2b4df22049b122beec63cf3ecc654f00c684e814eb28.jpg)

![](images/9fe68550a0ad2553c55e751a88e124bdf0b768e5dfef9b24d51e98a2eafe9b67.jpg)  
Contributes almost equally in dual income families

![](images/e8d1de62a8281e3cbc8d02541d182ea077e184a9a8906232

[中间内容因长度限制已省略]

7e5.jpg)

supplementary activities, structured savings through the National Education Savings Scheme (SSPN), and private tuition. Firefighters share the same ambitions but are cost-constrained at every turn. The gap between these two is not one of values—both dream of a better life for their children. The difference is one of means.

## EXHIBIT 38

## Education priorities for Firefighters and Builders

![](images/bf60a8952e447a5c9372d02da2f4602ce2c6fa0a0f11fdd8efad7d046c5398e0.jpg)  
Note: Aspirants and Trailblazers excluded as most of these households have no kids

## Final Thoughts

Family is our heart. It is the motivation for so many of our dreams and goals. It is a unit which is at once the reason for what we do, and the foundation of how we enjoy it. But what's clear from our research is the Malaysian family is stretched—stretched between generations, between earning and spending, between what it wants and what it can afford.

The fabric of Malaysian families is not fraying, but it is under pressure. Our study shines a spotlight on a rakyat making difficult trade-offs with remarkable discipline and very little margin for error. The question for anyone who serves Malaysian families—whether through products, policies, or public services—is whether they are designing for the family as a collective, rather than individual units.

Malaysia's demographic makeup comprises a diverse tapestry of people and possibilities—a reality reflected in the families which underpin our dynamic and ambitious nation. Recognizing those differences provides a pathway to addressing their struggles, but doing so requires a nuanced look at where hurdles are positioned for different families across the nation.

## Struggles are different, but priorities converge

Malaysian families may share dreams, but they face differing struggles. Firefighter families and Builder families share the same educational aspirations for their children, but their capacity to act is radically different. This is a prominent example of how a one-size-fits-all approach risks serving no family well.

## Husband and wife play different roles; both matter

Husbands manage the budget and lead on capital decisions. Wives drive daily spend. Marketing an investment product to mothers, or a grocery service to fathers, may not fully reflect the common architecture of the Malaysian family.

## Decisions are made as a family

Malaysian families share decisions and investment. Fifty-eight percent pool income. Fifty-seven percent save collectively. Travel is the most collectively decided expense. There is a prime opportunity to inform strategic product design based on the family as the customer.

## Families prioritise the most vulnerable first, particularly children and elders

Adult decision-makers are willing to defer their own needs but prioritize others. In healthcare, families rush children and seniors to the doctor while adults wait. Often the economic realities inform these decisions—with only 27% able to cover RM5,000, the protective instinct outpaces the financial capacity.

## Parents sacrifice their own future for their children

Children are our love and our legacy. That's why half (46%) of parents would give up retirement savings for their children's education. A third (37%) would go into debt for the same goal. Policymakers should be aware of this risk—households who sacrifice retirement savings create a future generation of elderly Malaysians without financial security, perpetuating the multigenerational dependency structures families are already navigating.

## Looking ahead

Malaysia is a nation of dreamers, and in many cases, families are at the heart of those dreams. Recognizing how our families plan and react is fundamental to understanding our shared national future.

There are firm points to anchor on in a sea of change. The multigenerational household is not going away, but Gen Z is likely to reshape family financial behavior. We will all still want what's best for our children, but the education gap between Firefighters and Builders will compound due to their differing abilities to achieve this. We all want the best healthcare, but with an overdependence on government facilities, are we equipped to support an aging population? Against this backdrop, the broader question of subsidy efficiency will only become more pressing.

MY Family is a portrait of a nation's households at a specific moment, and when it comes to family, now is often the most important moment we have. The structures, priorities, and trade-offs we illustrated here will evolve, but the fundamental insight will endure. The Malaysian family is the unit that matters—recognizing it, respecting it, and celebrating it is the best path to serving it well.

## About the Authors

![](images/a4f5f5976a964d5c4c2bc6b171a4c4ccaa82dc96fdbedf2640519cfa1b6882f8.jpg)  
Nurlin Mohd Salleh
Managing Director & Partner, and
Head of BCG Malaysia
Salleh.Nurlin@bcg.com

![](images/68ea8be7f47b7f46356f5e03c78c45114d66f51d3eda026d58bad98bc9286995.jpg)  
Anis Mohd Nor
Partner
Core Member of Kuala Lumpur Office
MohdNor.Anis@bcg.com

![](images/ee1699f066338691a697592dd2c0946a3ed90f4679d9b41542d5ae8341141319.jpg)

Aditi Bathia
Project Leader
Core Member of Singapore Office
Bathia.Aditi@bcg.com

![](images/b3af5a31c4b25111dd7ea34e4024828765a0c2b4482354297060b7408e48a32f.jpg)  
Omar Akbar Khan
Project Leader
Core Member of Kuala Lumpur Office
AkbarKhan.Omar@bcg.com

![](images/6458fade1ab5706becc3b2d639a03e6b0890023b9d5047cbafb20d6fee2ecb41.jpg)  
Haris Mohd Zukki
Consultant
Core Member of Kuala Lumpur Office
MohdZukki.Haris@bcg.com

![](images/7516226f6bde51729582c90100319676723d552955dc35d5e6ab49ee5acd62d2.jpg)
"""
