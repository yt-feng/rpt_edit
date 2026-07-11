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
# Global Technology & Communications

## Citi CIO Survey: IT Budgets Improve As AI Moves Higher In Priority

## CITI'S TAKE

Our 2Q26 survey (N=100) of key IT decision makers suggests an improved spending backdrop vs. last Q with both US and EMEA NTM IT budgets accelerating as AI continues to rise in investment prioritization. Overall forward IT budget growth expectations rose to +3.3% from +2.6% in the Mar-26 survey, which was 0.8 pts above the 7-year historical average. Data/AI remained the top priority for respondents and gained further share followed by cybersecurity, (2) digital transformation, (3) and customer-facing applications (#4). We summarize takeaways by sector for Software, European Tech, Internet, Hardware, IT Services, and Communications Services and Infrastructure.

Global IT Budgets Accelerate with Growth in Both US and EMEA — CIOs are expecting IT budgets to grow +3.3% over the next twelve months, seeing an acceleration of 0.7 pts from the March Survey, which is above the historical average. EMEA saw another modest acceleration, moving up 0.8 pts to 3.9%, while the US accelerated by 0.6 pts to +3.0%.

Data Analytics/AI Top Investment Priority, Ahead of Cybersecurity — NTM cyber budget growth decelerated \~1pt with the remaining $2^{nd}$ -ranked in CIO investment priorities, with a widened gap to data analytics/AI in 1st-place. We continue to see positive trends in tokenization helping to fuel the #1 category. We'd note respondents citing GenAI investments fueling cyber spend and cyber holding the #1 spot as a tool consolidation destination as reasons to stay constructive on category spend trends, and by extension platform consolidators with broad AI portfolio exposure/tangible momentum. Interestingly, web security leapt into top-priority cohort (likely spurred by surge in malicious and legitimate agentic/bot internet traffic vols + expanded API surfaces which we prognosticated), while Identity, Endpoint, Cloud, Network security practices collectively continue to demonstrate budgetary resilience.

AI Trends — MSFT remained the top vendor that CIO are considering increasing spend on with AI followed by Amazon and Google. In terms of cutting spend for AI investments, the most noted vendors included Cisco, Dell, IBM and ServiceNow. It's estimated that AI currently represents \~6.5% of the IT Budget with 69% (previously 73%) of funding coming from new/additional funding and 50% (previously 47%) majority of CIOs expecting AI to drive headcount reduction over the next 6-12 months, and an increase in CIOs seeing AI spending cannibalizing other areas of the budget (nearly \~50% vs. 40% in March and 30% in December). There was also a slightly positive trend of AI use cases moving into production which increase to 24% (previously 22%) while PoC went up to 40% (previously 37%).

Tyler Radke $^{AC}$ +1-415-951-1660
tyler.radke@citi.com

Fatima Boolani
+1-212-816-9115
fatima.boolani@citi.com

Steven Enders, CFA
+1-415-951-1745
steven.enders@citi.com

Michael Rollins, CFA
+1-212-816-1116
michael.rollins@citi.com

Balajee Tirupati, CFA
+44-20-7500-6682
balajee.tirupati@citi.com

Asiya Merchant, CFA
+1-415-951-1752
asiya.merchant@citi.com

Ronald Josey
+1-212-816-4545
ronald.josey@citi.com

Pavan Daswani, CFA

George Kurosawa, CFA

Mark Zhang

Yitchuin Wong

Peter Griffith

Andrew Girard, CFA

Joel Omino

Roberta Versiani

Michael Cadiz

Adrienne Colby

## Sector-Specific Impacts

■ Application + Data/Analytics Software (Radke) – We continue to see mixed and bifurcated enterprise software read-throughs following our CIO survey as AI spending is increasingly cannibalizing other parts of the portfolio. Data analytics/AI remains the top priority, while digital transformation stayed at (#3) and consumer-facing apps moving up 2 spots to #4.

For hyperscaler and cloud consumption peers, survey results were relatively positive with 38% of CIOs seeing consumption spending growth YoY uptick slightly (vs. 31% in the March survey) and 52% seeing consistent spending vs. last year (from 50% in the March Survey). LTM public cloud infrastructure spending expectations downticked to \~6% and NTM public cloud downticked to 7% (vs. 8% for NTM/LTM in our last survey). It is unsurprising to see Data Analytics/GenAI at the top spot again as recent data points from multiple conferences intra Q, Snowflake Summit, Databricks events, AWS Summits and Cannes all reinforced the strategic imperative of a modern data architecture platform on the path to productionalizing Agentic and AI PoCs. While we continued to see an increasing demand for Agentic AI among enterprises, we did witness a much greater % of respondents indicating AI funding is negatively impacting the overall IT Budget, which signal increasing cannibalization. Overall, we continue to see the most positive read-throughs to hyperscalers such as (MSFT and CRWV,) and AI platform/consumption names (MDB, SNOW, PLTR), which can benefit from increased enterprise AI workloads that could start to contribute more meaningfully over the next few quarters.

Customer-facing applications moved to #4 (previously #6) in the list of most important CIO priorities. In terms of vendor consolidation, customer-facing app development/deployed was less of a priority moving to #11 from #8 last survey. Salesforce (CRM) shifted down to $6^{th}$ (previously $4^{th}$ ) on rankings for vendors that CIOs are considering cutting spending to invest on AI which could point to positive demand signals in the 2H. We also view this trend as a positive readthrough for design and UI-focused providers like Figma.

Cloud communications (MSFT, NICE, ZM, and CRM) moved to the #9 CIO priority (previously #8). CIOs are increasingly looking to consolidate spending in the category with cloud communications moving to the #4 priority (from #7 previously). In terms of GenAI funding, customer support has been one of the first categories to exhibit customer-facing production use cases as companies take advantage of copilot (agent, supervisor, and back-office workflows) and virtual agents (self-service) to improve the customer and employee experience. Data transformation within large organizations has led to increased importance for modern UC/CCaaS platform as legacy vendors near EOL dates. We remain focused on trends at BPO customers who we believe will be the first to show agent headcount reductions.

■ Cybersecurity (Boolani) – Identity, Endpoint, and Web security are the top 3 cyber sub-categories that CIOs rank as a top investment priority, displacing Cloud and Network security. Regarding CIO's top 3 priorities collectively, Identity, Cloud and Network security are the top sub-categories, with Network returning to this cohort and displacing Analytics QoQ. We'd also note the much tighter distribution of rankings QoQ (\~10pts between 1 $^{st}$ place and 7 $^{th}$ place in top-3 rankings vs \~26pts last Q). Web security earning top investment priority status intrigues, and we believe this stems from the potential for faster and more volumetric AI-crafted DDoS attacks and malicious bot traffic, and overall explosive growth trends of AI/Agentic internet traffic. We'd also argue that a significantly larger and growing volume of API surfaces/interfaces (thanks to AI overall and capabilities like MCP) are potentially necessitating a renewed emphasis around security as another potential contributing factor. We surmise security for Agents/NHI's is also fueling the continued high prioritization of Identity security (treating Agents as identities that need to be protected/routed/authenticated), while endpoint security likely remains high-priority as this is also a ‘frontline defense’ against AI-driven threats. From a CIO wallet share perspective, CRWD, PANW (including CyberArk), MSFT remain the largest share winners over the NTM.

\- Identity security climbed to overall top priority status (from $3^{\text{rd}}$ -place-tie last Q) at 18% of CIOs, and continues to lead from a top-3-ranking perspective (though down to 40% from 49%). This across-the-board high priority ranking continues to reinforce that in an agentic world, ID hygiene is a critical first line of defense and architectural investment focus, designed to tackle privilege sprawl increasingly spanning humans and machine/NHI risks. Higher propensity to procure identity security from hyperscalers QoQ leans more favorable for MSFT vs. independents OKTA and PANW/Idira (but sample size is arguably small here).

\- Web security earning the $3^{\text{rd}}$ -highest top investment priority status likely signals growing concern and preparation for AI-driven attacks to web properties and web-facing infra as AI/Agentic automation enables/enhances the speed, volumes and efficacy of DDoS, bot attacks, while also stoking financial burdens of illegitimate traffic (agents, crawlers, NHI traffic that is costly to absorb but not revenue-generating and potentially revenue exfiltrating as LLMs trawl for content to train on). This bodes well for CDN vendors (NET/AKAM/FSLY with WAF/DDoS/bot protection/API security capabilities) in addition to cyber platforms. While loathe to call this a trend, we think there are enough ingredients here to advocate for a steady "web security spending renaissance".

\- Although Cloud security lost its status as the overall top CIO priority (identity/endpoint/web/user security leapfrogged it), from a top-3 perspective the sub-sector remains in $2^{\text{nd}}$ place, demonstrating some sustained cyber budget and mindshare resiliency. We believe the growing/maturing AI adoption we've highlighted should also drive cloud usage/migration, in turn expanding the 'attackable' cloud infrastructure estate for enterprises and sustaining cloud security demand.

\- Network security fell from #3 to #5 in top priority rankings, though improved from #7 to #3 regarding CIO's top 3 priorities. Similar to Cloud security, the stability/improvement in the top-3 rankings despite ceding ground as a top-most priority demonstrates some budgetary/mindshare resilience, even as growing AI/Agentic implementations bring other security sub-categories to the forefront. We surmise this has to do with a combo of exploding network traffic, raising capacity demands and pre-buying as the component environment remains punitive.

\- Endpoint security retained $2^{\text{nd}}$ place across CIO's highest priority list and $5^{\text{th}}$ place when CIOs ranked their top 3 priorities, sustaining key vendor observations that AI adoption is driving acceleration in endpoint demand as the sub-category is a critical defense/enforcement line against AI-driven attacks.

\- Data security remained $9^{\text{th}}$ -ranked as a top priority and tied for $5^{\text{th}}$ place as a top-3 priority (vs $6^{\text{th}}$ last Q). Despite its importance in enabling/securing AI adoption, we believe the space continues to be fractionalized with varying vendor strategies/use cases (cyber resilience, backup, DLP) and asset consolidations (platform vendors acquiring into the space).

■ Back Office Software (Enders) – Improving budget growth expectations ahead of historical average levels indicates a largely healthy overall spend backdrop and sets up an improved beat-and-raise profile into Q2 where companies should be in a better position to roll Q1 upside into full year outlooks. The main point of caution we see is potentially EMEA where survey data indicates a net worsening of 3mo macro conditions, although EMEA budget growth expectations still appear healthy which could mean enterprises are proceeding with purchases despite macro uncertainty. The rank order of priority across Back Office categories is largely unchanged with Automation remaining a top priority, Fins/ERP largely neutral, and Productivity and HR apps as still net negatives. From a q/q perspective, Fins/ERP, Productivity, and HR categories saw improvements in the absolute level of budget prioritization, which could help set up better-than-feared results, while Automation saw a slight decline. AI budgets continue to be largely funded by incremental funding, although we note an increasing share of respondents expecting traditional IT budgets to face some level of disruption, increasing pressure on companies in our coverage space to rapidly prove out commercial AI strategies and drive accelerating growth in order to be viewed as net beneficiaries. Similarly, we have seen a generally increasing share of respondents anticipating AI to drive reductions in organizational headcount over time, with the largest cohort expecting impacts in the 6-12mo timeframe, leaving us incrementally cautious on primarily seat-based models (MNDY, ASAN, BOX, BL, HR Software).

■ Internet (Josey) – Cloud Providers Benefiting from GenAI Demand: Our 2Q CIO Survey points to a stronger cloud-demand backdrop, with participants expecting public cloud infrastructure services spend growth to accelerate to +6.9% over the NTM vs. 5.5% over the LTM with 38% of respondents suggesting consumption spending growth is ahead of last year (vs. 31% in March and 36% in December). Our survey participants expect global IT budgets to grow 3.3% over the NTM, an acceleration vs. +2.6% in 1Q with US IT budgets to grow 3.0% over the NTM (vs. +2.4% in 1Q). Net-net, we are incrementally confident in our 2Q26 revenue growth projections for both AWS (+29.5% Y/Y) and Google Cloud (+65% Y/Y), both of which might prove conservative.

\- AI Spending Continues to be Additive to IT Budgets: Data Analytics and AI were listed as the top CIO investment priorities. 69% of respondents note GenAI funding is coming from new/additional sources, down slightly from 73% in 1Q, and 59% of CIOs expect AI investments and related savings to reduce headcount (same as 1Q) with 86% expecting these savings within the next 2 years (same as 1Q). And while our survey suggests AI accounts for \~6.5% of CIO budgets today, CIOs expect to increase spend on AI by \~10% over the NTM. significantly above overall budget growth of +6.9%, with most planning to do so with Microsoft followed by Amazon and Google.

\- LLM usage—Google's Gemini was the #4 (14% of CIOs) most used LLM in production, two AI labs, and Microsoft, which had 25%, 23%, and 20% of CIO adoption, respectively. New this quarter, we asked CIOs average LLM contract length and 96% are longer than 1 year, with 31% 2+ years in length. To that, 53% of CIOs (vs. 56% in 1Q) are most likely to run LLM workloads on the public cloud vs. on-prem or private cloud environments, further supporting our view that AI adoption remains a core driver of public cloud infrastructure demand.

\- European Technology (Tirupati) –The survey suggests rather resilient European CIO investment sentiment despite continued adverse opinion of the macro evolution. For European CIOs we highlight: i) macro sentiment remained cautious with \~62% of respondents stating macro condition has deteriorated over the quarter, ii) continued sequential recovery in expenditure expectation with NTM IT budget growth view of +3.9% (highest in 9-qtrs), and ahead of the trend rate and the LTM estimated growth (of +3.8%), and iii) average change in the IT budget over the trailing three month period at +1.8% with \~12% of respondents citing decrease in budget vs. \~38% citing increase. The budget sentiment for France appears to have recovered in this survey after muted investment view since 2024 – we acknowledge limited size (n=9) and adverse macro view of respondents, but note a reversal in investment sentiment in France could be particularly positive for Capgemini. AI is overarching theme for the sector – where survey takeaways are broadly consistent with previous quarters in majority of respondents (\~69%) citing AI funding being incremental, while \~50% also expecting AI investments having negative impact on traditional IT budgets and leading to headcount reduction. Data and AI stay top investment priority and both back office and front office projects continue to be seen as most impacted categories (from the increased spend in AI projects). Into the earnings season investor sentiment for the sector is in check and focus is on the implications of macro uncertainty and possible growth deceleration (also on tougher comps) when a broader sector de-rating has limited room for relative outperformance. We expect another quarter of steady updates and appreciate the sector’s resilience credentials (against macro volatility), still do not see in line prints to be catalyst enough for sentiment / trade reversal. For relative appeal, SAP stands out where we see relative valuation headroom and scope of slightly better than expected bookings evolution being received favourably.

■ Communication Services and Infrastructure (Rollins) – We view survey results as neutral to positive for the communications infrastructure industry, as overall trends continue to move in an encouraging direction. IT budget expectations NTM accelerated to +3.3% from +2.6% in March, which represents 120bps growth from the year ago level. US expectations went up to 3.0% NTM, up from 2.4% in March and above last year's 2.8%. EMEA performance was also stronger, up 3.9% NTM vs March level of 3.1% and significantly above last year's 0.6%. Data analytics/AI/data warehouse stayed as #1 priority in the next 12 months, followed by IT security and digital transformation projects, which is consistent with the prior period priorities and a good indication for our comms Business and Infrastructure companies. Within comm infrastructure and data centers specifically, overall demand indicators remain positive for both hyperscale and retail. The majority of IT budget revisions stayed the same in the last 3 months, while upward budget revisions increased slightly and downward budget revisions decreased slightly. The average trailing IT budget revision was +2.0%, which is above March's level and a positive to neutral indication in our view. Cloud consumption is also generally consistent with last year, but now with a slightly higher percentage stating consumption spending is ahead of last year with no plans to pull back (from 31% in March to 38% in June), which we view favorably. We maintain our Buys on EQIX and DLR, and we maintain Neutral ratings on CCOI and LUMN. EQIX is our top-ranked stock within our coverage, and we continue to view the company as a beneficiary as the demand for agentic AI for the enterprise expands and companies also employ a hybrid/multi-source architecture for AI workloads.

\- Hardware (Merchant) – According to survey respondents, on an NTM vs LTM basis spending on Datacenter infrastructure and public cloud are better, while PC 

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
