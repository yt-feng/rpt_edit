You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
![](images/f5170623c2ddf2566bf10bdd3e80d18cba30b19b8135ae0e879ab52b746cbbe8.jpg)

AMERICAS TECHNOLOGY

## Analyzing the Impact of AI on Industry Profit Pools - Part III (Staffing Case Study)

AI investment is entering a phase where hyperscaler capex approaching \~\$1tn by 2027E requires a clearer link between infrastructure spend and profit pool capture. We use staffing as a case study to provide a measurable lens into how AI reallocates enterprise spend away from human-driven intermediation and toward technology platforms. Our framework identifies a demand-side impact, where AI-driven hiring demand compression exposes \~\$10bn of temp, \~\$41bn of perm and \~\$12bn of freelance profit pools, reflecting lower labor volume and hiring activity, part of which is reallocated to technology and the remainder accruing to enterprises and end users. Against this backdrop, we identify downstream monetization pools, including a \~\$38bn recruiter workflow opportunity and a \~\$17bn online marketplace opportunity as spend shifts from discovery toward matching, verification and hiring outcomes. Investment implications favor scaled platforms, integrated workflows and advisory models, while pressuring volume-driven staffing. Buy-rated beneficiaries include KFY, supported by its high-touch advisory model that is less sensitive to AI-driven workflow automation, alongside FVRR, UPWK and Recruit as marketplace models evolve. RHI is Sell given exposure to AI-sensitive white-collar staffing, while ZIP and MAN remain Neutral given mixed dynamics between innovation, AI-driven productivity and macro-sensitive hiring demand.

George K. Tong, CFA
+1(415)249-7421
|george.tong@gs.com
GS & Co. LLC

Aarshiya Sachdeva
+1(212)855-6184
aarshiya.sachdeva@gs.com
GS & Co. LLC

Eric Sheridan
+1(917)343-8683
eric.sheridan@gs.com
GS & Co. LLC

Achal Gupta
+1(332)245-7973
achal.gupta@gs.com
GS India SPL

Minami Munakata
+81(3)4587-9830
minami.munakata@gs.com
GS Japan Co., Ltd.

Haruki Kubota
+81(3)4587-4059
haruki.kubota@gs.com
GS Japan Co., Ltd.

Sami Nasir, CFA
+1(415)834-7967
sami.nasir@gs.com
GS & Co. LLC

Anna Wu
+1(415)249-7235
anna.wu@gs.com
GS & Co. LLC

Alex Lakritz
+1(415)249-7072
alex.lakritz@gs.com
GS & Co. LLC

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

Executive Summary 3
Hyperscaler Spend Requires Downstream Profit Pool Capture 7
Where Are We Now? The Current State of AI in the Staffing Industry 10
How AI Could Be Disruptive in the Staffing Industry 12
Existing Profit Pools That Could be Disrupted by AI 12
New “TAM Expansionary” Opportunities Enabled by AI 34
Where Value Accrues as AI Adoption Scales 36
Where Could We Be Wrong 40
How Can This Analysis Be Expanded 41
Investment Conclusions 42
Valuation and Risks 44
Rating and pricing information 45
Financial advisory disclosure 45
Logo disclosure 45
Disclosure Appendix 46

## Executive Summary

## ■ Hyperscaler capex requires monetizable downstream AI profit pools.

Hyperscaler AI investment has reached a scale that requires large downstream profit pool capture to justify returns. Combined hyperscaler capex across AWS, Microsoft, Google and Meta has moved from sub-\$200bn in 2020 to \~\$740bn in 2026E and approaches \~\$1tn by 2027E, reflecting a broad-based infrastructure cycle across the major platforms. This spending is increasingly concentrated in AI infrastructure including compute, networking and datacenter capacity, with the magnitude of investment lifting the bar for durable revenue and profit conversion. Meanwhile, AI model capability continues to improve, with Epoch AI's Capabilities Index showing newer frontier models clustering in the 145-160 range versus earlier GPT-4-era models in the mid-120s. As models move from task augmentation toward multi-step workflow substitution, the range of disruptable profit pools expands from narrow productivity tools into broader labor and service-driven revenue pools. We analyze staffing as a case study because labor intermediation is large, measurable and directly exposed to AI-driven reallocation of work from people toward software, models and infrastructure.

AI adoption is broad, but labor displacement remains limited. AI usage across knowledge work has scaled rapidly, with \~75% of global knowledge workers regularly using AI tools and \~84% of developers using or planning to use AI tools, including \~51% using them daily. Despite this adoption, AI remains primarily assistive rather than fully substitutive, with most workflows still requiring oversight, validation, compliance judgment and client interaction. Staffing demand therefore remains largely intact today across many professional and financial functions, where AI can automate elements such as reconciliation or documentation but has not yet replaced end-to-end work. Within staffing itself, adoption is more visible in recruiter workflows, where AI is increasingly embedded in high-volume, standardized and repeatable stages of execution. Manpower's PowerSuite case study illustrates this shift, with \~90% of front-office activity supported, \~100bn data points in the global data layer, 25k+ AI-led interviews, a \~67% screening time reduction and a \~7% increase in placement rates as tools expand. This suggests AI is currently reshaping how recruiting work is executed before it structurally replaces recruiter roles.

AI disrupts staffing by shifting economics from labor intermediation toward technology-enabled execution. As AI automates a growing share of enterprise work, the need for incremental labor declines, reducing demand for temporary workers, permanent hires and contingent labor. This disruption is not primarily the elimination of entire roles, but the reduction in labor volume required to produce the same output, which pressures billed labor volumes in temp staffing and placement events in perm and freelance models. Accounting represents an example, where AI-enabled reconciliation, reporting and workflow automation can reduce the need for temporary accountants during peak periods and limit new permanent placements. A portion of avoided labor cost is then reallocated toward AI tools and infrastructure, although some value can be retained by enterprises and end users through margins or pricing. AI also creates an offset by improving recruiter

throughput, as integrated workflows translate role requirements into structured inputs, prioritize candidate pipelines and automate coordination across stakeholders. The net effect is a dual mechanism: staffing profit pools tied to hiring activity come under pressure while recruiter productivity and software monetization expand.

\- Temp staffing profit pool is sized through labor volume, wage intensity, automation exposure and staffing spread. The temp staffing model is driven by bill-pay spread economics, where staffing firms capture the difference between client bill rates and wages paid to workers. We size the temp staffing profit pool by starting with BLS temp headcount and wage data by job function, applying GS Macro task-level automation assumptions mapped to BLS sub-functions, then applying segment-specific staffing gross margins across white-collar and blue-collar roles. This approach converts labor scale, wage intensity, task exposure and spread capture into a function-level view of profitability. We size the temp staffing profit pool at \~\$10bn, concentrated in office & admin at \~\$1.9bn, business & financial at \~\$1.9bn, IT at \~\$1.6bn and healthcare at \~\$1.6bn. These categories combine meaningful employment bases, higher wages, 30-50% automation exposure and structurally higher 30%+ margins. In contrast, large blue-collar categories such as transportation contribute less to the exposed profit pool despite scale, given lower margins and lower automation exposure.

Perm placement profit pool is transaction-driven, with hiring events and compensation replacing temp spread economics. Perm placement differs from temp because revenue is tied to discrete hiring outcomes, with staffing firms earning a one-time fee typically structured as 30-35% of first-year compensation. Our methodology starts with BLS employment and wage data by function, applies GS Macro task-level automation assumptions to estimate reduced hiring demand, introduces a hiring rate to convert the adjusted labor base into annual placement volumes and then applies the placement fee. This differs from temp because perm monetizes hiring events rather than ongoing labor volumes, making hiring rate a critical throughput variable. The hiring rate was 3.3% as of May 2026 vs a 3.7% long-term average since 2001, and we use hiring rates to link labor demand compression to fee-generating placement activity. We size the perm staffing profit pool at \~\$41bn, led by management at \~\$10.8bn and healthcare at \~\$5.4bn, followed by business & financial, office & admin and IT. Higher-skill roles contribute disproportionately because fees scale with compensation, while lower-wage categories such as transportation and food services contribute less despite large employment bases.

\- Freelance profit pool reflects demand compression and mix-driven exposure to AI automation. We size the freelance profit pool at \~\$12bn by starting with global platform-mediated GSV and applying a blended take rate alongside GS Macro task-level automation assumptions to translate activity into AI-exposed revenue. This approach mirrors temp and perm by mapping an underlying economic base into a function-level view of profit pools, with GSV substituting for wages and take rate for spread or fees. Within this framework, AI impacts freelance through both volume compression in low-value highly automatable tasks and mix shifts toward

higher-value complex and AI-related work. Automation exposure varies by category based on task structure, with rules-based and information-intensive segments carrying higher exposure and creative or judgment-driven work remaining more resilient. As a result, profit pool impact is concentrated in categories that combine scale, monetization and exposure, including software development, design, data and writing.

\- Recruiting services create a \~\$38bn US AI-addressable workflow monetization pool. We frame recruiting services as a revenue-derived profit pool generated by recruiter-driven placement activity across temp, perm and freelance hiring. Using US 2027E TAM of \~\$270bn for temp staffing and \~\$45bn for perm placements, we convert temp revenue into a recruiter execution layer using a blended \~24% gross margin while treating perm placement revenue as fee-based monetization of recruiting activity. This yields a combined \~\$109bn execution-layer pool spanning temp spreads and perm fees generated by recruiter workflows. Applying a 35% task-level automation assumption produces an AI-addressable recruiter profit pool of \~\$38bn, representing gross workflow monetization and not demand-side hiring compression, which is incorporated separately. RPO is an important subset, with the US RPO market estimated at \~\$6bn in 2027E, representing a low-single-digit share of total staffing TAM and roughly low-teens penetration of the \~\$109bn execution layer. Because RPO centralizes standardized, data-intensive and enterprise-scale recruiting activity, it serves as a leading indicator of where AI-enabled workflow monetization can emerge first.

Online job advertising shifts from discovery monetization toward AI-enabled matching and workflow outcomes. The global online job advertising market is projected by SIA to reach \$37.6bn in 2026, up 7% from \$35.2bn in 2025, with the top two players holding \~50% market share versus \~25% in 2015. LinkedIn and Indeed lead the market with \~29.2% and \~20.6% share, respectively, while legacy job boards and localized classifieds remain fragmented. AI changes the value proposition by shifting spend away from posting, clicks and traffic toward matching, verification, screening and hiring outcomes. We size the online job advertising and recruitment marketing profit pool at \~\$17bn by segmenting the \$37.6bn market into traditional job boards at 45% share, professional networks at 35% and programmatic software at 20%, then applying AI automation assumptions of 70%, 35% and 10%, respectively. Indeed illustrates the scaled platform response, with Premium Sponsored Job using AI to recommend candidates, retention 20% higher than Standard tier and US ARPJ rising 25% y/y in 4Q FY3/26 despite US job posting volume declining 7% y/y. ZipRecruiter is also investing in AI-enabled matching through Smart Outreach, ZipIntro, Phil and a ChatGPT app, although its smaller scale limits the immediate profit pool impact.

AI expands staffing TAM through new hiring demand, wage premium and recruiter throughput. We offset the disruption thesis with AI-enabled TAM expansion, as AI-related job postings have grown at a \~29% annual rate over 15 years versus \~11% for the broader labor market. More than 80k US job postings referenced generative AI skills in 2025, up from \~3.8k in 2010, and more than 50% of roles requiring AI skills now sit outside traditional IT and computer science. AI roles

also carry a \~28% salary premium, or roughly \~\$18k higher annual pay on average, supporting higher staffing monetization because placement fees scale with compensation. Supply is increasing through education channels, with \~193 undergraduate and \~310 master's AI-focused programs across \~304 US institutions as of 2025, and master's programs increasing 167% from 2022 to 2025. We size the current AI hiring TAM at \$1-3bn, add \$0.6-2.4bn from the graduate pipeline, apply a 1.25-1.75x adjacency multiplier and incorporate 20-30% recruiter productivity gains. This yields an estimated AI-related staffing TAM of \~\$2-12bn, with a mid-case of \~\$6bn.

Value accrues to workflow platforms, scaled marketplaces, technology layers and defensible advisory models. As AI adoption scales, value capture reflects both hiring demand compression and the shift from manual recruiting execution toward system-driven workflows. Our value transfer framework separates demand-side compression from workflow monetization, with hiring demand compression sized at \~\$10bn for temp and \~\$41bn for perm, AI workflow monetization at \~\$38bn and online marketplace workflow opportunity at \~\$17bn. Within the technology layer, value is split between model providers capturing compute and API usage and application platforms monetizing workflow integration through end-to-end hiring systems. Scaled platforms with proprietary data, closed-loop feedback and workflow control, including LinkedIn and Indeed, are better positioned as monetization shifts from discovery toward outcomes. Integrated staffing platforms such as MAN can defend economics through centralized systems and operational data, while KFY is relatively insulated through advisory-led executive search, consulting and digital offerings. RHI faces greater risk given its concentration in finance and accounting, technology and administrative/customer support end markets, where hiring demand is closely tied to incremental workload and AI-driven efficiency gains.

## ■ Key risks center on adoption, labor demand, automation ceilings and

monetization capture. Our sizing of staffing profit pools could be too aggressive if AI augments labor demand more than it compresses hiring volumes, with enterprises reinvesting productivity gains into incremental work instead of reducing headcount. Early adoption patterns still show AI increasing output per worker without structural labor displacement, which could sustain or even increase hiring volumes in some functions. Workflow integration could also take longer than modeled because current deployment remains more focused on discrete execution tasks than end-to-end orchestration, with data fragmentation, enterprise complexity and regulatory constraints slowing system-level adoption. Human oversight could limit automation penetration in higher-value segments where client interaction, candidate evaluation, compliance and accountability remain central to service delivery. Technology providers may also capture less economic value than our framework assumes if competition across hyperscalers, software vendors and open-source models compresses pricing. In that scenario, labor costs may decline but savings could accrue more to enterprises and end users than to AI providers, changing the distribution of profit pool reallocation.

■ Future work can improve timing, role-level precision and non-linear workflow effects. Our current framework treats labor demand reductions and recruiter productivity gains as partially offsetting forces, but integrated AI workflows could create dynamic feedback loops that compound over time. Modeling these feedback loops would help quantify scenarios where higher recruiter productivity accelerates placement efficiency and delays or offsets volume-driven disruption. The perm methodology currently applies a standardized hiring rate across functions, so adding role-level differentiation based on turnover, tenure and cyclicality would create a more granular view of placement fee exposure. The automation model also remains task-level, while workflow-level disruption could be non-linear if AI integrates sourcing, screening, matching and coordination into a single system. For example, a 20% task-level efficiency gain could translate into a 40-50% staffing volume reduction when multiple steps and handoffs are removed simultaneously. Additional refinements could incorporate pricing, placement fee compression, margin sensitivity, mix shifts, adoption curves and enterprise readiness by function.

Investment conclusions favor advisory-led and scaled platform models over exposed white-collar staffing. KFY, Buy, is positioned as a strategic beneficiary of long-term labor market change because executive search, consulting, digital and workforce transformation are less exposed to pure workflow automation and more tied to client advisory, senior talent access

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
