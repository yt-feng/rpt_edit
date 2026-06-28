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
GLOBAL FINTECH 2023

# Reimagining the Future of Finance

May 2023

By Deepak Goyal, Rishi Varma, Francisco Rada, Aparna Pande, Juan Jauregui, Patrick Corelli, Saurabh Tripathi, Yann Sénant, Stefan Dab, Yashraj Erande, JungKiu Choi, Jan Koserski, and Joseph Carrubba of the Boston Consulting Group

By Nigel Morris, Frank Rotman, Matt Risley, and Sahej Suri of QED Investors

BCG + QED
INVESTORS

## Contents

02 Introduction 25 A Tale of Two Cities on Spread Businesses
04 Fintechs Have Come of Age 29 Insuretech and Wealthtec Opportunities Are Mostly in B2B2X
09 Industry Fundamentals Remain Strong
15 Fintech Revenues Are Projected to Grow Sixfold by 2030 31 The Path Toward Growth Still Carries Risks, and Requires Action
20 While Payments Led the Last Era, B2B2X and B2b Are Expected to Lead the Next 41 About the Authors

![](images/d8ac01abfa0a35d9309ac73f124c1cc61daf2d13944012cee43fa1522dc76a7c.jpg)

## Introduction

“Fintech” is a word that’s barely a generation old. But in that nanosecond of historical time, this amalgam of “finance” and “technology”—or, more specifically, the array of products and services that fintech companies have brought to life—has had an impact on the daily lives of billions of people.

For the past two decades, the fintech industry has been shaped by the rise and rapid adoption of transformative technologies and the applications (“apps”) they enable. A key to success during this journey has been the ability of fintechs to identify and ease the points of friction customers have often had with traditional financial institutions (FIs). Many fintechs have delivered high-quality, service-focused digital experiences, provided access to unbanked and underserved customer segments, and introduced cost-effective ways of operating through a more efficient infrastructure and simplified processes.

In order to grasp where the fintech industry is going, and to understand its importance for a very diverse set of stakeholders, it’s critical to take stock of how fintechs have evolved.

## Key Highlights

![](images/8988ea6981eb030fe38cf8074709f43430083db3a8a0df6b505cadcb215d9840.jpg)

A period of great exuberance, 2020–2022 saw peak valuations for fintechs reach 20X revenue multiples.

![](images/5a534bbae5fa16ae34e5bc3c30f3162d27e6bf6448db6d814fc493af64b543ef.jpg)

With fundamentals remaining strong, the last 12 months have seen a necessary short-term correction in an otherwise progressively positive growth story.

![](images/67ec4267f5dcca4dcd5ffbd539df476170a49b5e7c4dd7ecf8ac62ab99cde5dd.jpg)

Today, almost 80% of adults in the world are still either underbanked or unbanked.

![](images/25845788e2109088b83900c80b5879c7f142d140633b34db16762a7e500c7cd3.jpg)

Annual fintech revenues are expected to reach \$1.5 trillion by 2030—a sixfold growth—with banking-related fintechs representing a quarter of all banking valuations.

![](images/394c039a989f29380b6f30e6e85d40ed44ed3bd4cbc69c6a58bac7db2b0dd63c.jpg)

Outpacing even the US with a $27\%$ growth rate, Asia-Pacific is poised to become the world's top fintech market by 2030.

![](images/131bbdc6a327aca8a74a6e90b4976cc6e5cb3b063213b4edea1771513a7fe8c1.jpg)

While the last era of fintech growth was led by payments, B2b and B2B2X will lead the next.

![](images/af633d5935f034e93cae1b79d2fbffc00fd7a1548774fb18f0d54e7bede3cb87.jpg)

Spread businesses such as neobanks and lending platforms will face challenges in the developed world while playing a critical role in emerging markets.

![](images/791d795326e469091bd550b6678515e52ae69144f61a4da67284f5ffb59f0923.jpg)

The time for stakeholders to act is now: Fintechs must play offense, incumbents need to accelerate their own digital journeys, and regulators must remain proactive in maintaining a level playing field.

![](images/8f37695f721136f685b2b9bb15b8d45654cb94182da721ff62e32411c210e1b2.jpg)

# Fintechs Have Come of Age

While fintechs were perceived as largely tangential to the financial services industry until about five years ago, the pandemic served as a catalyst for broad consumer adoption of digital financial services. As a result, fintechs have now become mainstream in certain segments, especially payments and transaction banking, which have been fundamentally transformed by players such as Stripe, Square, Alipay, and a few others. Some fintechs, such as PayPal in the US, Nubank in Brazil, and PayTM in India, have become household names. Today, there are roughly 32,000 fintechs globally.

Over the past decade, fintechs have attracted more than \$500 billion in funding. More recently, since 2019, they have received roughly 20% of global venture capital outlays—attracting large amounts of capital from generalist, technology private investors and hedge funds—beyond the financial services specialists who had historically funded these businesses. Such funding was fueled at times by a frenzy of speculation in sub-segments such as crypto, and its supporting technologies. Crypto accounted for more than \$50 billion in funding in 2021 and 2022 combined, or roughly 75% of all crypto funding received through 2022.

At their peak in 2021, fintechs represented roughly 9% of all financial services valuations globally, with public valuations reaching \$1.3 trillion—a multiple of 20 times annual revenue compared with the historical, pre-2018 multiple of six times annual revenue. (See Exhibit 1.) Also in 2021, the mega-fintechs PayPal and Ant Financial were among the top-10 financial services companies in the world by market capitalization.

# Exhibit 1 - In Q2 2021, Peak Valuations Reached an Inflated 20x Revenue Multiple

Q4 2017 – Q4 2022, average revenue multiples for public fintechs (simple average, market Cap/LTM revenues)

![](images/4f85e28d849b98df9a7d5d2b0928dd7526616e94e4cff1d4fc230a74310c5401.jpg)  
Sources: Fintech Control Tower, Capital IQ, BCG analysis.  
Note: The Public Fintech list considers market capitalization and revenues for each quarter from 85 public fintechs from different geos and segments.

## The Last 12 Months Have Been Humbling

Since April 2022, however, fintech exuberance has been dealt a strong dose of reality, with valuations plummeting across all segments and geographies by an average of more than 60%—all while revenue growth has continued (albeit at a slower pace). New funding has decreased by 43%, with early-stage companies still seeing venture capital infusions, but later-stage companies witnessing steep drops in funding rounds. Series C+ companies have faced the toughest challenges. (See Exhibit 2.)

These dynamics have occurred owing to rising interest rates that have raised the cost of capital and essentially stopped the supply of zero-priced funding. This rise has resulted from persistent inflation, which in turn was caused by a variety of factors including geopolitical tensions, supply-chain issues, and recovery from the pandemic. The consequent shifts in the financial landscape have been felt both by fintechs and investors, and fintech CEOs are now targeting profitable growth as their top priority. (See Exhibit 3.)

Exhibit 2 - Since 2021, Funding Levels for Later Stages (Series C+) Have Dropped More Drastically Than for Earlier Stages (Seed/Series A/B)

2021–2022, Average Funding (\$B) by Stage

![](images/ca551cdcdae40b72a257a5363b6545ae3a1a8ce69cd07fe2c07807ac715e1076.jpg)  
Sources: Fintech Control Tower, BCG analysis.

## This Is a Short-Term Correction

We believe that the challenges fintechs have recently faced represent a short-term correction in an otherwise long-term growth story, as the fundamentals of the sector haven't changed. Essentially, we are witnessing a shakeout and tempering of enthusiasm for growth-stage (series B-D) companies that have unclear product and/or market fits.

Additionally, as is typical for nascent industries, profitability in fintech has not come easily—even for highly valued, conventionally “successful” late-stage companies. Of the roughly 85 public fintechs BCG analyzed across all regions and segments in 2022, less than half (45%) were profitable—despite shareholder pressure for public companies to deliver a healthy bottom line. $^{1}$

Now, however, overvaluations have become more difficult to justify without strong fundamentals—such as good unit economics, recurring revenues, patents, strong brands, and loyal customer bases. Some of this filtering is good for the industry, as weaker business models are becoming stressed and effectively being weeded out.

Currently, fintechs are employing different playbooks to survive the funding winter, with many focusing on unit economics as opposed to unbridled revenue growth at any cost. Some are raising debt to avoid down rounds. Many are also switching their focus toward the LTV (lifetime value) element of the LTV-to-CAC (customer acquisition cost) ratio as a tracked metric. Most are prioritizing longer-term sustainable revenues, monthly recurring customers, and investments in innovations that are core to their revenue-generating products and services. We expect that, by focusing on the basics, some will emerge stronger and more resilient, well-positioned to become the future leaders of the financial services industry.

## Fintech CEOs Focused on Strengthening Fundamentals and Driving Profitable Growth Over Next 12–18 Months

![](images/909d3731d39c8bb29d480b3f5215a8833457aaf6912b42f50ca22f328b168988.jpg)

Top Challenges for Fintech CEOs in the next 12-18 months (selected by % of CEOs)

Top Priorities for Fintech CEOs in the next 12-18 months (selected by % of CEOs)

59%

Customer acquisition

30%

Customer acquisition

33%

40%

29%

25%

Slowdown in economic growth

34% Higher interest rates

Challenges scaling business model

Managing Costs

Product Innovation

14%

17%

27%

12%

4%

New Products

Need to reduce costs

Managing credit risk or fraud

Regulatory/Compliance

Improving
governance/compliance

12%

12%

Partnerships

Hiring/Talent

Sources: BCG/QED Future of Fintech survey (N=81), conducted across fintech CEOs and C-Suite leaders in February 2023; BCG analysis. Q. What are the top 3 challenges facing your company in the next 12–18 months? Q. What are the top actions your company is taking to address challenges over the next 12–18 months? Note: Responses collected as free-form text and then sorted into discrete categories.

Fintechs are employing different playbooks to survive the funding winter, with many focusing on unit economics as opposed to unbridled revenue growth at any cost.

![](images/cc55626b28d98062eeb7d55992527bd1ddc9baa1e514bb99827c3a95fd1ad739.jpg)

# Industry Fundamentals Remain Strong

Despite the turbulent interlude, the fundamentals of the fintech industry remain sturdy for various reasons, notably that the financial services industry remains fertile ground for disruption. A number of factors are relevant.

First, the financial services industry is one of the largest and most profitable segments of the global economy, representing \$12.5 trillion in annual revenue pools and creating an estimated \$2.3 trillion in annual net profits or additional value—based on one of the highest average profit margins across all industries of 18%. (See Exhibit 4.)

Another factor is the overall customer experience in financial services (including the insurance sector) has historically been among the lowest-ranked compared with other industries. Although incumbents have made progress over the past few years, they still significantly underperform fintechs. The average customer loyalty score for the banking industry in the US stands at 23 (out of 100)—compared with some US fintechs whose scores reach as high as 90. (See Exhibit 5.)

Further, there is more than ample room for growth in the fintech sector, especially in emerging markets, given that 1.5 billion adults globally are still unbanked, with an additional 2.8 billion adults underbanked (defined as not having a credit card, using data from the World Bank Financial Inclusion Project). The total represents more than half the world's population. Moreover, almost $44\%$ of adults globally are still heavily dependent on cash for major transactions, while $89\%$ use a mobile phone or smartphone. (See Exhibit 6.)

## Exhibit 4 - Financial Services Is One of the Most Profitable Sectors of the Global Economy

Net Margin (%) by Industry, Global  
![](images/8b444f7479909bd80919b7275703480564db8d26fb36229741f5bb625a223859.jpg)  
Sources: NYU Damodaran, Federal Reserve Bank of St. Louis, BCG analysis.
Note: Others include construction, education, hospitality, air transport.

There is also still significant room for growth in digital usage in banking—currently at about 39%, compared with 98% in computer software. The figure dips as low as 17% on average for countries in the Middle East and Africa. (See Exhibit 7.)

Lastly, it is important to note that although the fintech sector is coming of age, it is still at a very early stage of development, representing less than 2% of annual financial services revenues globally—or roughly \$245 billion out of \$12.5 trillion, with ample room to grow. We think of fintech's chronological evolution in terms of phases—defined periods of time in which one or more trends came to the fore.

Phase One: Digital Disruption (1998–2008). With the increasing availability and adoption of internet-enabled devices, financial services went digital for the first time. This challenged the legacy systems of national and regional FIs. Digital offered greater convenience and accessibility to consumers, eliminating pain points. Online banking, lending, and e-commerce (notably through marketplaces such as

Amazon and eBay) gradually became mainstream. Online payments, with players such as PayPal leading the charge, emerged as the largest area of innovation, disrupting the transaction-banking industry. Digital lenders, such as Capital One, led a wave of innovation in lending using data and analytics.

## Phase Two: Mobile and Social Adoption (2009–2014).

Following the 2008 financial crisis, amid new regulatory scrutiny and shifting consumer behaviors, the “wait-and-see” perspective of incumbent banks opened the door for fintechs. A credit boom and rapid innovation in mobile and cloud allowed consumers to access financial services in real time, spurring the hypergrowth of disruptive players. An intentional focus on user experience/user interface (UX/UI) and the introduction of APIs eliminated many points of friction during both the onboarding process and, later, the customer’s digital journey. Social media and data analytics began to play a key role, allowing companies to gather granular information. Fintech success grew by providing digital-first solutions with a high degree of personalization.

## Exhibit 5 - Customer Experience Across Value Chains Is Relatively Poor for Incumbent Financial Institutions

Customer loyalty scores aggregates, major U.S. financial institutions

![](images/9c550381224241071f28f37b5ec501b0bcc9a77db62ff8278b0cdac99f156ffa.jpg)

![](images/f749326d4f459b318cedaf0fe4378f69eac3af25c0713b585625f6353a4e2684.jpg)  
Customer loyalty scores, Major Fintechs with U.S. Operations

![](images/c19b97452097d17c46fdeb461383b54529753ec52f621829f3ee706929bf6025.jpg)  
Sources: Forrester - The US Net Promoter Rankings, 2022/Customer Gauge Benchmarks in Financial Services 2022.

Phase Three: Relevance and Scale (2015–2021). The fintech industry grew rapidly alongside smartphone adoption, with a step-function acceleration during the COVID-19 pandemic. Consumers now expect all financial services to be available online 24/7. Fintechs such as Ant Financial, Nubank, PayTM, Square, Stripe, and some neobanks became household names in the evolving landscape. Fintechs grew, owing to expanded customer access to financial services, new demand-generation channels, updated UX/UI, and reduced costs. Fintech funding surged to \$440 billion between 2014 and 2022. Amid a low-interest-rate climate and easy availability of capital, valuations spiked, as did the number of companies and amount of talent in the industry. The sector experienced increased competition for market share and a flurry of mergers and acquisitions (M&A) activity.

Phase Four: Looking Ahead (2022 and Beyond). We foresee a more proactive regulatory environment paving the way for supportive infrastructure investments (e.g., digital public goods) and unlocking innovation in parts of the world that are still seeking to expand financial inclusion. Moreover, the stage is set for new technological disruptions such as generative AI and DLT, which are already making their presence felt. Despite tall challenges, fintech CEOs remain optimistic in the long term. (See Exhibit 8.)

## New Technologies Are Emerging, but Their Impact Has Yet to Play Out

Multiple innovative technologies, some of which touch the realm of the futuristic, are either entering the fintech arena for the first time or strengthening a nascent presence. Their impact will likely be felt not only by all types of financial services players—which must get a firm handle on their capabilities to optimally leverage their potential use cases—but by society at large. Among these technologies are generative AI; API-based open connectivity; DLT; quantum and edge computing; and embedded-hardware Internet of Things (IoT) and biometrics.

% of unbanked and underbanked adults across major global regions

# Exhibit 6 - Over Three-Quarters of Adults Remain Unbanked or Underbanked Globally

<table><tr><td></td><td>Unbanked</td><td>Underbanked</td><td></td><td>Unbanked adults (M)</td><td>Underbanked adults (M)</td><td>Cash Usage (%)</td><td>Mobile Penetration (%)</td></tr><tr><td></td><td>27%</td><td>50%</td><td>World</td><td>1,546</td><td>2,829</td><td>44%</td><td>89%</td></tr><tr><td></td><td>5%</td><td>27%</td><td>North America</td><td>15</td><td>83</td><td>21%</td><td>93%</td></tr><tr><td></td><td>8%</td><td>52%</td><td>Europe</td><td>54</td><td>357</td><td>23%</td><td>96%</td></tr><tr><td></td><td>25%</td><td>55%</td><td>APAC</td><td>820</td><td>1,787</td><td>59%</td><td>85%</td></tr><tr><td></td><td>35%</td><td>42%</td><td>LATAM</td><td>164</td><td>199</td><td>60%</td><td>87%</td></tr><tr><td></td><td>52%</td><td>43%</td><td>MEA</td><td>493</td><td>403</td><td>58%</td><td>83%</td></tr></table>

Source: World Bank Financial Inclusion Project.  
Note: “Underbanked” defined as % of adults without a credit card; mobile penetration defined as % of adults who own a mobile phone; cash usage defined as % of adults who made a utility payments using cash only.

\*Generative AI. This new frontier in artificial intelligence has created a step change in the human-digital interfa

[中间内容因长度限制已省略]

d39b12e614fbe34eec78e6ef7489b5d556127f8b07d09a1217.jpg)

Loyalty scores for partnerships and preparedness of themselves vs. partners

Selected areas of least preparedness of partner companies (by % of CEOs)

![](images/4d6a2c6828c65e8723188738e3e70edbf160e890c190610badb8d54a2986ace4.jpg)

Your company's partnerships

![](images/670d9367e9cf4f73fc985612b2f94b9783769b029e55a9e6a40e6cec1e4c0b83.jpg)

The preparedness of the partner company

2

The preparedness of your company

Technology stack

Organizational structure

![](images/36cbc130aa7e8e5482adb4b11cde494be8d8f28ca4f68af90b14177f0256ba56.jpg)

Commercial terms

Culture

Product offering

Customer acquisition and service

Talent

Source: BCG/QED Future of Fintech survey (N-55), conducted across fintech CEOs and C-Suite leaders in February 2023; BCG analysis. $^{1}$ Loyalty scores are calculated as the % of promoters (rated >/=8 on a 10-point scale) minus the % of detractors (rated >/=6 on a 10-point scale). Q. Thinking about your company's most recent material partnerships, please rate the following on a scale of 1–10: How satisfied are you with your company's partnerships? How prepared was your company to enter these partnerships? How prepared was the other company to enter these partnerships?

## About the Authors

## BCG

Deepak Goyal, Goyal.Deepak@bcg.com, Managing Director and Senior Partner, NYC

Rishi Varma, Varma.Rishi@bcg.com, Managing Director and Partner, NJY

Francisco Rada, Rada.Francisco@bcg.com, Project Leader, NYC

Aparna Pande, Pande.Aparna@bcg.com, Consultant, NYC

Juan Jauregui, Jauregui.Juan@bcg.com, Consultant, NYC

Patrick Corelli, Corelli.Patrick@bcg.com, Consultant, NYC

## QED Investors

Nigel Morris, Nigel@qedinvestors.com, Co-founder and Managing Partner

Frank Rotman, Frank@qedinvestors.com, Co-founder, Partner, and CIO

## For Further Contact

If you would like to discuss this report, please contact the authors.

Saurabh Tripathi, Tripathi.Saurabh@bcg.com, Managing Director and Senior Partner, MUM

Yann Sénant, Senant.Yann@bcg.com, Managing Director and Senior Partner, PAR

Stefan Dab, Dab.Stefan@bcg.com,
Managing Director and Senior Partner, BRU

Yashraj Erande, Erande.Yashraj@bcg.com, Managing Director and Partner, MUM

JungKiu Choi, Choi.JungKiu@bcg.com, Managing Director and Partner, SIN

Jan Koserski, Koserski.Jan@bcg.com, Managing Director and Partner, FRA

Joseph Carrubba, Carrubba.Joseph@bcg.com, Managing Director and Partner, NY

Matt Risley, Matt@qedinvestors.com, Partner

Sahej Suri, Sahej@qedinvestors.com, Chief of Staff

## Acknowledgments

This report is a joint initiative of Boston Consulting Group (BCG) and QED Investors (QED). The authors would like to thank the members of BCG and QED for their contributions to the development and production of the report. In addition, the authors are extremely grateful to all Fintech survey, 1-on-1 discussion, and panel discussion participants for their valuable contributions toward the enrichment of the report.

Furthermore, the authors extend their sincere appreciation to Gbenga Ajayi, Tommy Blanchard, Laura Bock, Bill Cillufo, Adams Conrad, Amias Gerety, Christian Limon, Ashley Marshall, Lauren Morton, Tim O'Shea, Yusuf Ozdalga, Mike Packer, and Sandeep Patil, from the QED team for their contributions to enriching the report.

The authors would also like to thank their BCG colleagues for their valuable contributions to this report. In particular, they thank Inderpreet Batra, Harsha Chandra Shekar, Aaron Cormier, Boris Goutkin, Evan Hunter, Micah Jindal, Rahel Lebefromm, Marshall Lux, Michael Marcus, Reihan Nadarajah, Kamila Rakhimova, Hanjo Seibert, Steven Thogmartin, and Michael Zhang, the numerous local analysts from the Financial Institutions Knowledge Team, the Banking and Insurance Revenue Pools team, the Fintech Control Tower team, the Data & Research Services, and the editorial, PR, marketing, and design teams.

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

## QED INVESTORS

QED Investors is a global leading venture capital firm based in Alexandria, Va. Founded by Nigel Morris and Frank Rotman in 2007, QED is focused on investing in disruptive financial services companies worldwide. QED is dedicated to building great businesses and uses a unique, hands-on approach that leverages its partners' decades of entrepreneurial and operational experience, helping companies achieve breakthrough growth. QED has invested in more than 200 companies, including 28 unicorns, across 18 countries. Notable investments include AvidXchange, Betterfly, Bitso, Caribou, ClearScore, Current, Creditas, Credit Karma, Flywire, Greensky, Kavak, Klarna, Konfio, Loft, Mission Lane, Nubank, QuintoAndar, Remitly, SoFi, Wagestream, and Wayflyer.

![](images/249b59a7b18857e62313700e25affe0db17ac9ef102e2d1f69a00347930b2729.jpg)
"""
