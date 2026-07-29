你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
U.S. SMID-Cap Software

# Cybersecurity: mid-'26 CISO conference call transcript covering budget trends and priorities + AI-impact

![](images/64fcec7bad98ae41e335ec2f9096eabe6a28fa389e3c5f0748dbccb84ddc5870.jpg)

Peter Weed

+1 917 344 8390

peter.weed@bernsteinsg.com

![](images/74abb7f01cc1f149d8cc4979f4599c7a152bc3ae86e4adffd04667c5000a38cc.jpg)

Armin Hadavi, CFA

+1 917 344 8463

armin.hadavi@bernsteinsg.com

![](images/e07be812c45ee2a9ae7a2045cbcb9a28b4082889123e8abc482502b2b8a5808f.jpg)

Luwei Yang

+1 917 344 8342

luwei.yang@bernsteinsg.com

We recently hosted a conference call with three CISOs discussing the latest budget trends, AI-impact, and priorities. A full edited transcript is below and replay is here.

Cybersecurity spending continues to outpace broader IT spending, driven primarily by AI. Security leaders consistently described AI as the biggest catalyst for new investments, both because organizations must defend against AI-enabled attacks and because they need to securely enable internal AI adoption.

Identity has become the new security perimeter, and non-human identities are now a top concern. The focus is shifting to securing AI agents (human-in-the-loop + independent) — how to allocate identities for data / system / application access and apply privileged access and governance frameworks that ensure least-privilege time constrained access across both human and non-human actors.

Organizations are struggling to balance AI adoption with control and visibility. Security leaders reported sharp increases in employee experimentation across multiple LLMs leading to concerns around what data is being entered into models, what systems agents can access, what actions they can perform, and how those actions are monitored and audited. As a result, organizations are investing in AI governance through either centralized AI routers or endpoint, network, and data-layer controls that provide visibility into prompts, agent behavior, data access, and potential exfiltration risks.

Beyond increased budgets, vendor consolidation is the main funding mechanism for new security priorities. CISOs are retiring legacy platforms, reevaluating existing security stacks, and looking to add features from current vendors as this is generally much cheaper than adding best-of-breed standalone products. ...but vendor consolidation is at the key cyber pillar level, not end-to-end. Participants generally preferred maintaining dedicated leaders within “core pillars” such as identity, endpoint, network, web security, cloud security, and email. CrowdStrike, Wiz, Palo Alto, and Okta were frequently praised for innovation.

Security operations are moving toward automation because human-speed response is no longer sufficient. Participants agreed that AI-enabled attackers are accelerating the pace of threats forcing organizations to actively evaluate Agentic SOC platforms and autonomous response capabilities to reduce investigation times, improve resilience, and operate closer to machine speed. "Switzerland" VC-backed startups (e.g., Torq, Tines) that could look across cyber pillars seemed to be preferred. The discussion also suggested that traditional SIEM is becoming less strategic vs. an Agentic ITDR/SOC model.

The overarching message from the discussion was that AI is forcing a redesign of cybersecurity strategy. Budgeting, identity management, security operations, vendor selection, governance, and risk management are all being reevaluated through an AI lens. Security leaders are no longer treating AI as an emerging trend; they are restructuring security programs around the assumption that AI will define both the future threat landscape and the future technology environment.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">27 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td colspan="2"></td><td rowspan="2">ClosingPrice</td><td rowspan="2">PriceTarget</td><td colspan="4"></td><td colspan="3"></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>NET (Cloudflare)</td><td>M</td><td>USD</td><td>265.61</td><td>136.00</td><td>17.8%</td><td>USD</td><td>0.92</td><td>1.33</td><td>1.73</td><td>287.2</td><td>200.4</td><td>153.5</td></tr><tr><td>CRWD (CrowdStrike)</td><td>M</td><td>USD</td><td>180.11</td><td>103.00</td><td>37.9%</td><td>USD</td><td>0.93</td><td>1.25</td><td>1.66</td><td>193.2</td><td>144.7</td><td>108.3</td></tr><tr><td>FTNT (Fortinet)</td><td>M</td><td>USD</td><td>152.38</td><td>92.00</td><td>29.3%</td><td>USD</td><td>2.76</td><td>3.37</td><td>3.93</td><td>55.2</td><td>45.2</td><td>38.7</td></tr><tr><td>OKTA (Okta)</td><td>O</td><td>USD</td><td>137.43</td><td>141.00</td><td>19.9%</td><td>USD</td><td>3.50</td><td>3.91</td><td>4.64</td><td>39.3</td><td>35.1</td><td>29.6</td></tr><tr><td>PANW (Palo Alto Networks)</td><td>O</td><td>USD</td><td>317.32</td><td>253.00</td><td>40.1%</td><td>USD</td><td>3.43</td><td>3.63</td><td>4.89</td><td>92.6</td><td>87.3</td><td>64.9</td></tr><tr><td>S (SentinelOne)</td><td>O</td><td>USD</td><td>18.14</td><td>19.00</td><td>(23.3)%</td><td>USD</td><td>0.20</td><td>0.36</td><td>0.59</td><td>90.5</td><td>50.0</td><td>30.6</td></tr><tr><td>ZS (Zscaler)</td><td>O</td><td>USD</td><td>147.30</td><td>224.00</td><td>(64.6)%</td><td>USD</td><td>3.28</td><td>4.21</td><td>5.42</td><td>45.0</td><td>35.0</td><td>27.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,413.18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

CRWD, OKTA, S base year is 2026;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

No impact to target prices or investment recommendations.

## DETAILS

We recently hosted a conference call with three CISOs from three different industries: Insurance, Manufacturing, and Healthcare Software to get their perspectives on cybersecurity spending. This note provides a summary of our key takeaways and a full edited transcript and a replay of the call is available through this link.

For complete results of our recent CISO survey, please check out link.

## Detailed takeaways:

Cybersecurity spending continues to outpace broader IT spending, driven primarily by AI. Across industries, security budgets are either growing faster than overall IT budgets or being protected while other IT functions face cuts. Security leaders consistently described AI as the biggest catalyst for new investments, both because organizations must defend against AI-enabled attacks and because they need to securely enable internal AI adoption.

Identity has become the new security perimeter, and non-human identities are now a top concern. CISOs emphasized that remote work, AI agents, and autonomous workflows have fundamentally changed access management requirements. The focus is shifting beyond employee / customer accounts toward identity for independent AI agents — how to allocate identities for data/system/application access and apply privileged access and governance frameworks that ensure least-privilege time constrained access across both human and non-human actors.

Organizations are struggling to balance AI adoption with control and visibility. AI usage is growing rapidly across engineering and business teams, often faster than expected. Security leaders reported sharp increases in token consumption, employee experimentation across multiple LLMs, and growing concerns around what data is being entered into models, what systems agents can access, what actions they can perform, and how those actions are monitored and audited. As a result, organizations are investing in AI governance through either centralized AI routers or endpoint, network, and data-layer controls that provide visibility into prompts, agent behavior, data access, and potential exfiltration risks. The discussion was less about restricting AI usage and more about establishing guardrails around data protection, access rights, and agent autonomy.

Particularly in budget-constrained environments, CISOs are retiring legacy platforms, reevaluating existing security stacks, and looking to add features from current vendors as this is generally much cheaper than adding best-of-breed standalone products. Rather than purchasing standalone point solutions, many are adding capabilities from existing strategic vendors where possible because add-on modules are typically far cheaper than introducing new products. The goal is to free resources for higher-priority initiatives.

Vendor consolidation is at the key cyber pillar level, not end-to-end. While companies like Microsoft and Palo Alto continue to expand their security portfolios, participants generally preferred maintaining dedicated leaders within “core pillars” such as identity, endpoint, network, web security, cloud security, and email. CrowdStrike, Wiz, Palo Alto, and Okta were frequently praised for innovation, while concerns were raised about vendors that have been slower to evolve around AI and modern identity requirements.

Participants agreed that AI-enabled attackers are accelerating the pace of threats, making traditional SOC models increasingly difficult to sustain. Organizations are actively evaluating Agentic SOC platforms and autonomous response capabilities to reduce investigation times, improve resilience, and operate closer to machine speed — "Switzerland" startups that could look across cyber pillars seemed to be preferred. The discussion also suggested that traditional SIEM is becoming less strategic than integrated threat detection, threat intelligence, orchestration, and response capabilities that can convert signals into action. The end state is increasingly an Agentic ITDR/SOC model that combines detection, enrichment, investigation, prioritization, and response into a largely automated workflow.

The overarching message from the discussion was that AI is forcing a redesign of cybersecurity strategy. Budgeting, identity management, security operations, vendor selection, governance, and risk management are all being reevaluated through an AI lens. Security leaders are no longer treating AI as an emerging trend; they are restructuring security programs around the assumption that AI will define both the future threat landscape and the future technology environment.

## Full transcript:

This transcript has been edited for clarity and consistency.

## Speaker Key:

## Bernstein analyst: PW: Peter Weed (US SMID-Cap Software)

CIOs: Sean (Insurance); Kristie (Manufacturing); Raj (Healthcare Software)

PW: Good morning, everyone. We're going to give it 30 seconds or so for attendees to file in. I know it takes a little bit to get everything connected. Just bear with us as that goes on. Well, I think I'm going to jump in and hopefully everybody was able to get connected.

Just a little bit of housekeeping just from the top. A reminder, there's a Pigeonhole link for anybody who is joining. If you have questions, please feel free to submit them there and we will take a look at them. As you know, we do a series of these type of webinars. Obviously, we just did one around CIOs. I've asked the panelists here to be actually off video, given that we're dealing with perhaps a slightly more sensitive topical area of cybersecurity as part of this.

Where I'd really love to start is just with a really quick reflection on the CISO survey that we had. Then I'm going to introduce the panelists and we're going to go into some of their experience. But hopefully, many, if not most, of you saw earlier this week we published the results of 100-CISO survey, our biannual survey. This is the mid-year one. It very much focuses on US cyber practitioners.

What were the large findings? Not surprising, very consistent with what we even saw in our CIO survey, what was the number-one budgetary line item for CIOs to be increasing? Cybersecurity. In cybersecurity, what did we hear from the cybersecurity professionals? We heard that their budgets, by and large, are going up and, on average, going up greater than IT budgets.

In fact, if you looked across all the responses we had, we had budgets going up, depending on the industry, between, say, four and six-plus percent on average. But there's a bit of a bell curve. There are some organizations increasing it as much as the teens and some increasing it in the lower single digits.

From a topical standpoint, I think it's also not surprising to say that a lot of what was driving some of the energy is AI, both threats from attacks coming in as well as the demands of their organization to secure the projects, the AI projects, that the businesses were trying to get done.

There's a lot of, obviously, nuanced detail in the overall report that we have. When we looked at the categories of cybersecurity within there that get invested in, certain categories are seeing much greater than others and it implicitly suggests that those areas are probably where people are investing around these threats as well as supporting this infrastructure.

That includes topical areas that I think a lot of conversation has been around. Identity is front and center. Some of the other categories like endpoint security continue to end up near the top, threat intelligence.

But, really interesting, where we're seeing a bunch of movement is also in security operations itself. At least my personal experience is that the human side of cybersecurity can be up to 40% of budgets. Those areas are places where both more expertise is needed, but also the application of tools may be coming in to those organizations. I think that'll be some of the interesting conversations we'll have with the participants here.

On the other end of the spectrum, the things that actually continue to do more poorly, the worst of the worst was Security Service Edge. Again, I think it'll be interesting to understand with some of the CISOs on the call here why that is and how its position is not a priority today. I don't think it means that people are probably ripping these things out. It just means that, relative to other things that could be done, that is not a top-of-mind topic right now.

Other tail, lower investment areas included SIEM. Think of this as more of the traditional SIEM, the things that, say, a Splunk is doing as opposed to what I really think of more as threat intelligence, which would be the next-generation SIEM or XIM or some of these things that you're hearing from some other vendors, at least in my opinion, email security, secure browser. Those are going to be areas of lower investment focus today.

So, anyway, with some of that context out of the way... And again, please go into the CISO survey. If you have other questions, please surface them as part of this conversation. What I'd love to do is actually go around the horn with the participants today where they can introduce their organization. Obviously, they're not going to get into their company name but more of, what

industry are they in? What size of organization and cybersecurity budget are we talking about?

I guess, just because I see you first on my screen here, Sean, I'm going to ask you that first. Tell us a little bit about your context as an organization, what industry, what budget, and really help us understand how that budget is changing this year. What's really driving that change? How have those priorities changed and where are you putting money to work?

Sean: Yes. Hello. So I'm in the insurance sector on the commercial side. We have about 6,000 employees globally and the predomin

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
