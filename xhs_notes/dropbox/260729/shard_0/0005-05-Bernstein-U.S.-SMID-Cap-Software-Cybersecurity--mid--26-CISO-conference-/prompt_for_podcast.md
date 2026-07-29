你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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

Sean: Yes. Hello. So I'm in the insurance sector on the commercial side. We have about 6,000 employees globally and the predominant number of those employees work remotely. Our focus this year is to increase probably our security spend between 12% to 15%.

We've been deployed with traditional security services from the endpoint side and, as Peter said, a lot of the SIEM stuff, mail stuff, but now we're really shifting to the focus on the AI side of the house. More and more of our users are obviously leveraging the tools. I'm sure that's the same across the board. We're trying to gain more insights into how they're using the tools and where the threat vectors are coming from. They seem to be moving and changing daily.

We're trying to wrap our heads around where we're going to spend those additional funds. We're talking with several different possible vendors to see what works with our deployment. We've got quite a variety of deployments on different sides, depending on how we service the client. So we don't have a one-size-fits-all approach. So we've got to be more flexible, and so I think that's been a little bit of a challenge for us, but we're definitely increasing double digits on the security spend, mostly focused on the AI side, though. You're muted.

PW: I am muted. I am securing you guys from my blather here. Just remind us the scale of your organization.

Sean: We're about 5,500 employees globally.

PW: Yes. Kristie, same question to you, just a little background on the industry and how your priorities have been changing and budgets have been changing.

Kristie: Sure. Yes. I'm in the manufacturing industry. My company is about 50,000 people in 170 locations in 29 countries, so we have a pretty big global footprint. So a lot of new regulations coming out of Europe drive a lot of the compliance activities that we're doing. Our industry, manufacturing globally, is always under a lot of cost pressure. So we are being pushed to try to maintain a flat budget going into 2027. Given the amount of AI adoption that the business is trying to push for, it's making that a little bit challenging.

Two areas we really need to invest in is better internal data classification, role-based access, least privilege enforcement as we're adding new language models into our environment to make sure that we're not overexposing our internal data. Then, also on the new proliferation of non-human identities is building out our IGA to make sure that we're really managing those identities properly and that we're not going to get into a situation where we have an agentic identity taking more action than they should be able to have privilege to do.

PW: Thank you, Kristie. Raj, same for you.

Raj: Good morning, good afternoon, and good evening, folks, wherever you are. My name is Raj. I am the CISO for a healthcare data analytics company. We're primarily based in the US market, but we have development centers across the globe. We're probably around 12,000 to 15,000 total emplo

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
