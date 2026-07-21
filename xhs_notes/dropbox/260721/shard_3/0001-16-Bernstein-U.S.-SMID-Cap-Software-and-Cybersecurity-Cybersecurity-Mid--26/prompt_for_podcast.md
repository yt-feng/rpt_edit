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
# U.S. SMID-Cap Software and Cybersecurity

# Cybersecurity Mid-'26 CISO survey: AI-driven demand continues!

![](images/eca9148326c0cca016afc427158c67ab0c5724c6dfc2bf7f800b9f3ceb7ba315.jpg)

Peter Weed

+1 917 344 8390

peter.weed@bernsteinsg.com

![](images/f5ef4f82fc3906788fd7c99b0a3204f8ba00be8a84815973d5b2cd2d5b13216c.jpg)

Armin Hadavi, CFA

+1 917 344 8463

armin.hadavi@bernsteinsg.com

![](images/22818f33fc773929d2dc065cd1e295b14e146837009dc75865d9e5fad72629d0.jpg)

Luwei Yang

+1 917 344 8342

luwei.yang@bernsteinsg.com

This is the June '26 sample of our bi-annual CISO survey, with 100 US respondents.

Our Mid-2026 CISO survey showed expected cybersecurity spend outpacing IT growth more significantly than in our EOY '25 survey (which had only a slight tilt), with 43% expecting cyber budgets to grow faster vs. 20% with IT faster (rest equal). This seems consistent with the mid-year CIO survey findings with cyber being the top spend growth category (here). The strongest tailwinds are in Financials, Tech, and Services industries at \~6% YoY growth (although all industries expect >4% growth). More than half of CISOs raised their full-year spending expectations vs. earlier forecasts, implying stronger H2 spending as H1 remained largely in line with prior expectations.

The biggest budget winner seems to be software, but both staff and managed services were not far behind (hardware was positive, but mostly just in network security). Within software, identity, cloud sec, and endpoint remain the top investment priorities. Versus EOY '25, SecOps, Identity, and Threat Intelligence saw the largest incremental spend tailwinds (followed closely by Network Security, AppSec, and Internet/DDoS). On the other hand, despite its strong baseline, Endpoint Security saw the $2^{nd}$ largest decrease in +1 year spend plans, and the already least-growthy area of SSE saw the largest incremental weakness. Other less growthy areas from EOY '25 (SIEM, Email Security, and Secure Browsers) also decreased further. Interestingly Network Security, DDoS, and Data Security saw the greatest divergence in spend plans, with both budget increases and cuts become more common vs. EOY '25.

Within vendors, hyperscalers broadly saw reputational improvement, while other vendors remained more stable. This placed most hyperscalers at or above the large cybersecurity peer average. More broadly, we saw small upticks in the already most-loved Palo Alto and CrowdStrike, reinforcing their leading reputations. Splunk was the only vendor whose reputation declined (coinciding with the weakness in SIEM spend).

On overall cyber strategy, the shift toward software, vendor-hosted SaaS, and vendor consolidation was clear (across both SSE/SASE and broader cyber). However, moving away from physical firewalls and other appliance-based security was more of a future expectation than a present reality for most respondents, with the greatest delta between current execution and future plans. The asterisk on hardware is physical network security both for branches and data center had the lowest expectation for displacement.

GenAI has a large strategy impact and demand urgency on cybersecurity spend. But this isn't about AI coding agents building solutions in-house and displacing vendor budgets. Not to mention cyber budget seems safe from broader AI-driven budget pressures from things like Tokenmaxxing. Perhaps surprisingly, Identity did not come up as a strong beneficiary of GenAI adoption (counter a narrative in the market). But we do note that Identity was reported as a leading space of investment, so this may reflect the priority already being high and GenAI not really turning it up even further. The biggest AI investment area is SecOps, although tempered by concerns around model hallucinations / accuracy. And post Mythos, perhaps it's not surprising that AppSec is expected to see significant disruption from AI coding agents.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">20 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td colspan="2"></td><td rowspan="2">ClosingPrice</td><td rowspan="2">PriceTarget</td><td colspan="4"></td><td colspan="3"></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>NET (Cloudflare)</td><td>M</td><td>USD</td><td>272.42</td><td>136.00</td><td>19.8%</td><td>USD</td><td>0.92</td><td>1.33</td><td>1.73</td><td>294.6</td><td>205.5</td><td>157.4</td></tr><tr><td>CRWD (CrowdStrike)</td><td>M</td><td>USD</td><td>198.49</td><td>103.00</td><td>48.6%</td><td>USD</td><td>0.93</td><td>1.25</td><td>1.66</td><td>212.9</td><td>159.4</td><td>119.4</td></tr><tr><td>FTNT (Fortinet)</td><td>M</td><td>USD</td><td>160.36</td><td>92.00</td><td>33.9%</td><td>USD</td><td>2.76</td><td>3.37</td><td>3.93</td><td>58.1</td><td>47.6</td><td>40.8</td></tr><tr><td>OKTA (Okta)</td><td>O</td><td>USD</td><td>148.41</td><td>141.00</td><td>37.3%</td><td>USD</td><td>3.50</td><td>3.91</td><td>4.64</td><td>42.4</td><td>37.9</td><td>32.0</td></tr><tr><td>PANW (Palo Alto Networks)</td><td>O</td><td>USD</td><td>348.66</td><td>253.00</td><td>59.9%</td><td>USD</td><td>3.43</td><td>3.63</td><td>4.89</td><td>101.7</td><td>96.0</td><td>71.3</td></tr><tr><td>S (SentinelOne)</td><td>O</td><td>USD</td><td>19.46</td><td>19.00</td><td>(10.2)%</td><td>USD</td><td>0.20</td><td>0.36</td><td>0.59</td><td>97.1</td><td>53.6</td><td>32.8</td></tr><tr><td>ZS (Zscaler)</td><td>O</td><td>USD</td><td>149.82</td><td>224.00</td><td>(66.3)%</td><td>USD</td><td>3.28</td><td>4.21</td><td>5.42</td><td>45.7</td><td>35.6</td><td>27.7</td></tr><tr><td>SPX</td><td></td><td></td><td>7,443.28</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

CRWD, OKTA, S base year is 2026;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

## No impact to target prices or investment recommendations.

We refer to our recently published note (here) regarding company-specific expectations into H2. But relative to that perspective, we thought a few insights were incrementally notable from our CISO survey:

\- Zscaler vs. survey's SSE weakness: We believe Secure Service Edge ("SSE") remains a strategic priority for enterprises moving to cloud-first SaaS vendors where they want global cyber consistency across those offerings and the benefits of zero-trust architectures. But spending growth expectations were the weakest of all cybersecurity categories we tested in this survey. This may reflect that in existing adopters, their organizations have already completed most of their deployments, and for non-adopters that they have other near term priorities due to GenAI adoption that put SSE rollout on the back burner. For existing customers, it seems to imply CISOs view SSE as a maturing market where functionality across leading vendors is converging, shifting purchasing decisions toward consolidation rather than incremental expansion. In a tighter spending environment, organizations are often optimizing existing SSE investments rather than adding new capabilities, which reduces the urgency of spend growth relative to other security categories.

\- CrowdStrike / SentinelOne vs. Endpoint downticking in investment: We believe endpoint security continues to be mission-critical, and this downtick in growth could run counter to the narrative we heard from the leading vendors at their latest earnings. They made the case that endpoint demand was actually accelerating, on the back of GenAI generating a renewed urgency to modernize the remaining \~50% of enterprises that have yet to adopt EDR. The point being that desktop AI Agents need to be secured, and the endpoint cyber solutions are well positioned to be part of that. We wonder if this is a mixed signal, with non-adopters being strong net buyers, while existing adopters are already mature and not growing spend. (there are other priorities because they already have EDR / XDR in place). As a result, spending often centers on renewals, vendor consolidation, and platform optimization rather than large net-new deployments. CISOs are also directing a larger share of incremental security budgets toward emerging risks such as AI, identity, and data protection, reducing endpoint's relative growth profile despite its importance.

\- Okta vs. Identity conflicting messages. The narrative is that identity is a critical investment for AI Agent adoption — how to manage user access rights when using AI as well as the rights of independent AI Agents operating without a human in the loop. The survey calls out Identity as one of the strongest areas of investment, and this makes sense because it sits at the center of modern attack vectors and is becoming even more critical with the rise of GenAI, agents, machine identities, and cloud-native environments. BUT! We also saw a more modest agreement when CISOs were asked if GenAI would increase Identity spend. We note two important nuances here 1) Identity was ALREADY a top growth area, so it may more indicate they are unclear what incremental they need to do vs. their existing plans (particularly when it is human-in-the-loop AI, it would probably use the current user's Identity infrastructure), 2) we actually did see a strong step up in expectation around AI driving Identity spend, and this could reflect the organizations that are first to deploy AI-powered applications and autonomous workflows — they are discovering the incremental Identity problems they need to invest in covering. Specifically they may be finding the number of human and non-human identities expands significantly, increasing demand for IAM, PAM, IGA, and machine identity solutions. Unlike endpoint or SSE, identity is still benefiting from both structural growth and expanding use cases, making it one of the few security categories where CISOs continue to prioritize meaningful incremental spending.

## DETAILS

Our mid-'26 survey showed CISOs' cyber budget outpacing IT budget growth at a greater pace, with H2 2026 implicitly even stronger. Overall cyber spend +12 month outlook modestly improved vs. our EOY '25 survey with 39% of CISOs seeing H1'26 cyber spend higher than expected over the past few months. Looking to full year 2026, 62% saw cyber spend expectations grow, suggesting H2 could be even stronger. Only a very small minority, \~4%, expected cybersecurity spend growth lower relative to their earlier expectations. On a growth basis in 2026, the distribution of increase was pretty wide between low-single digits to 10%+, and for 43% of respondents that cyber growth rate is reported to be faster than IT growth (only 20% expected IT growth to outpace cyber growth).

Cybersecurity spend is expected to keep growing in '26, particularly in Software / SaaS — 70% of respondents expected Software / SaaS growth over +12 months and almost none expected shrinking. While many categories of software are expected to see at least some increased investment, the areas of Identity, Endpoint, and Cloud Security are most broadly anticipated to increase (55-60% of respondents). On the other hand some topics more distant from “Securing AI” narrative use cases like SIEM and Secure Browser are least growthy (20-30% anticipating growth). The weakest was SSE pulling up the rear, with <20% anticipating growth — these vendors are trying to spin a story of AI security, but that may not be resonating well today. Many other categories were pretty similar with 40-50% of respondents anticipating at least modest growth expected. Human costs are also expected to increase, both in-sourced staff/compensation and outsource/managed services, but not at the level of software (and there was a meaningful \~10% who believed both would decrease, most of which thought it would decrease significantly — perhaps some of these CISOs are the early adopters of SecOps AI tools? On the other hand hardware/appliance based cybersecurity was expected to be flat (increasing slightly). Although if we double-click on hardware we do see network security equipment is the one area with at least some moderate spend increase expectations.

CISOs' threat priorities are pulling them in many directions. CISOs are continuing to prioritize software-based network security and vendor-hosted cloud-delivered cybersecurity tools. And incremental investment that is going on is mostly focused on enhancing existing vendors, perhaps reflecting the frustration with vendor sprawl.

Across cybersecurity vendors CrowdStrike and Palo Alto were seen distinctly most positive vs. all others, with hyperscalers AWS and Microsoft just a bit behind in the next most positive tier. On the other hand, most others we asked about had a more similar slightly “Above average” reputation. There were a few interesting exceptions in cyber specific vendors, with Wiz and Arista coming in lowest. We also expanded to ask about the hyperscalers themselves, and perhaps not surprisingly Amazon AWS and Microsoft Security came in with the highest marks at levels just below the top pure play cybersecurity vendors. On the other hand, Oracle and Google Cloud were more controversial, with the largest number of below average scores.

CISOs widely perceive GenAI/LLMs as a driver for increased cybersecurity spending, motivated by the need to defend against sophisticated AI-enhanced attacks and the desire to automate security operations and incident response. Most CISOs believe GenAI/LLM investments are net new budget and they are NOT replacing cyber budget. While many plan to increase budgets for AI agent-driven solutions, some express caution regarding model accuracy and false positives, leading them to favor established vendors over new startups for these enhancements. Concurrently, AI's impact on company budgets presents a dual dynamic: initial high investment costs for advanced defense mechanisms are expected to lead to significant long-term savings through faster threat detection and automated responses, enabling companies to shift to a more proactive cybersecurity posture.

## CISO SURVEY SHOWS 2026 CYBERSECURITY SPEND AVERAGES \~8% OF IT, WITH VARIATION ACROSS INDUSTRIES

Our mid-2026 CISO survey (in-market June) includes 100 US respondents across different industries and Enterprise-size FY revenue sizes (Exhibit 17). On average, CISOs expect cybersecurity spending to represent \~8% of total IT budgets in 2026 (Exhibit 1), which is consistent with our level based on our EOY 2025 survey (in-market Oct-Nov '25). Most respondents expect cyber spending to account for 3%-11% of IT spending, while only 8 CISOs expect it to exceed 12% — this was a slightly tighter range than our prior survey. The highest spenders came from financial, manufacturing, services, and utilities sectors, perhaps reflecting their “critical” infrastructure positioning (and in some cases lighter other IT spend as we see in Exhibit 3). However, each of these sectors also includes respondents reporting materially lower cybersecurity spending ratios, highlighting the wide dispersion of cybersecurity investment profiles within these industries. Within the 3%-11% range, respondents are distributed relatively evenly across the three spending brackets.

We do not observe meaningful variation in cyber spending as a percentage of IT spending across company size cohorts, with averages falling in the 7-8% range (Exhibit 2). This contrasts with our EOY 2025 survey, where the largest and smallest companies reported the highest cybersecurity spending levels (both above 8% of IT budgets), while mid-sized companies allocated only 6%-7%. The convergence observed in the Mid-2026 survey could reflect differences in the respondent sample, but it may also indicate growing recognition of cybersecurity as a strategic priority among companies with \$1 billion-\$10 billion in annual revenue.

EXHIBIT 1: Our mid-year 2026 survey shows a little less extreme variation in cybersecurity spend as a % of IT than the EOY 2025 survey did. The overall average remained about the same.

Total annual cyber spending as % of IT

![](images/9d74d40a9947f9c146f4c4028aee19561755582c9fc3de7174ee9b464864215a.jpg)  
EXHIBIT 2: Companies with all revenue categories show 7-8% cyber spending as % of IT spending.  
2026 average spend expectation: Cyber % of IT by company revenue size

![](images/6cd63bb4f372a6bb382f78f72dffaa00c3c1e4601bfeefa7edee4dddaef00bf0.jpg)  
Source: Bernstein CISO Survey  
Source: Bernstein CISO Survey

Comparing across industries, Utilities and Manufacturing report the highest % allocation of IT budgets to cybersecurity (but IT is a smaller % of revenue), while Financial, Technology and Government spend the largest % of Revenue (Exhibit 3). This may reflect the regulatory emphasis on securing critical infrastructure in these top spenders as a % of IT and % of revenue. All these industries are often called out in those political discussions. In addition, technology providers themselves are expected to be the outsourced security for their customers, so it might seem logical they would spend more. Our EOY '25 survey also showed a similar result with Utilities, Technology, and Manufacturing being the leading industries with the highest IT budget allocation to cybersecurity. On the other hand, Retail and Media have been the ones with the lowest cyber budget in both surveys. These industries tend to under-index in their technical talent vs. other industries. They can include lower margin players, and may be faced with ongoing industry disruption pressures. Thus, they may not have the budget, strategic focus, or internal talent on IT. That said, the sample sizes for three industries are relatively small — Media, Communications and Utilities. Therefore, those industry findings should be interpreted with more caution and may not fully reflect broader industry spending trends.

EXHIBIT 3: As a % of revenue, Financial, Tech and Government are spending the most on cybersecurity. But in some industries with smaller IT spend, but real cyber risks, such as Utilities and Manufacturing, their cybersecurity budget as a % of IT spend is higher than all other industries.

![](images/294187340b3bc9b19784cdf3fb69e894d2d33824f4a0e09e65ec9851692c559d.jpg)  
Source: Bernstein CISO survey; Gartner and Bernstein analysis

## CYBERSECURITY SPENDING EXPECTED TO INCREASE BY 7% IN 2026 VS. 2025

On average, CISOs expect cybersecurity spending 

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
