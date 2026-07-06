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
# China Internet & New Media

6 July 2026

EQUITY: INTERNET & NEW MEDIA

# Takeaways from Moonshot AI expert call

Commercial acceleration and strategic pivot

Key highlights

The NOM China internet team recently hosted a group call with an expert from Moonshot AI (unlisted), a leading Chinese generative AI startup. Its annualized recurring revenue (ARR) is projected by management to surpass USD1bn by year-end, driven primarily by overseas API usage and robust AI coding capabilities. Beyond AI coding, the expert believes that the next growth frontiers will be AI solutions for healthcare, education, and finance industries, where high-quality proprietary data will be a critical differentiator aside from specialised AI capabilities. To protect margins and improve monetization, Moonshot is shifting toward a closed-source strategy for its flagship models, while utilizing domestic chips to lower inference costs. While experts suggest pure-play AI labs like Moonshot could outcompete large internet platforms by maintaining pure focus, we continue to believe that major internet platforms such as Alibaba (BABA US, Buy) and ByteDance (unlisted) remain formidable competitors due to their vast capital, data ecosystems, and strategic need to own state-of-the-art (SOTA) LLMs (large language models).

## Who is Moonshot AI

Moonshot AI (Moonshot) is a Beijing-based AI startup focused on LLMs and AI assistant products. Founded in early 2023 by Dr. Yang Zhilin—a former Google Brain and Meta/FAIR engineer – alongside a group of his Tsinghua University alumni, the company has rapidly established a prominent position in China's generative AI landscape.

Moonshot's product and model ecosystem is built around the Kimi assistant and K-series foundation models. Its flagship foundation model, Kimi K2, is a trillion-parameter model featuring advanced coding and agentic capabilities. Subsequent iterations include Kimi K2 Thinking, Kimi K2.5, Kimi K2.6, and Kimi K2.7 Code. Moonshot has also expanded into specialized AI agent products, notably Kimi Code, Kimi Agent/Agent Swarm, and Kimi Work, with the latter positioned as a dedicated desktop AI agent for office workers.

The company is backed by a premier group of Chinese technology corporations and venture capital investors, including Alibaba, Tencent, HongShan, ZhenFund, and IDG Capital. Chinese media reported that Moonshot completed its latest funding round in May 2026, raising USD2bn at a post-money valuation of USD20bn. This round was led by Meituan, with participation from China Mobile, Tsinghua Capital, and other venture capital investors.

## ARR likely to surpass USD1bn by the year-end

According to the expert, Moonshot's annualized ARR reached USD400-500mn by mid-2026, with monthly ARR rising $10 - 20\%$ sequentially. Growth was particularly robust early in the year, expanding 2-2.5x y-y, supported by new product launches and accelerating model adoption driven by the hype around the desktop agent, OpenClaw. The expert projects that Moonshot's ARR could exceed USD1bn by the year-end.

Revenue composition is shifting materially toward API calls. According to the expert, API usage has become the primary revenue driver, followed by consumer-oriented subscriptions. Private deployment, including licensing and maintenance fees, contributes a relatively small share and has been declining as a proportion of revenue.

The expert attributed API growth primarily to continuous model iteration, increased usage by overseas developers, and the release of useful vertical capabilities such as coding. Subscription revenue is also growing, but at a slower pace than API revenue.

## Research Analysts

China Internet & New Media

Jialong Shi - NIHK
Jialong.shi@NOM.com
+852 2252 1409

Rachel Guo - NIHK

rachel.guo@NOM.com

+852 2252 1400

Geographically, the revenue mix has increasingly pivoted toward international markets. Overseas revenue contribution has risen steadily since the beginning of the year and now represents a larger share of total revenue than domestic operations. Sustained future growth remains heavily dependent on the continued expansion of overseas API calls, international subscriptions, model upgrades, and the deployment of specialized vertical capabilities, according to the expert.

The next major product catalyst is expected to be K3, which the expert suggests could be released around September 2026. However, the launch window remains flexible and may be adjusted depending on the release schedules of competitors such as MiniMax, Zhipu, DeepSeek, and Alibaba's Qwen.

K3's key areas of improvement are expected to include multimodal capability, enhanced coding performance, agent task orchestration, and enriched vertical capabilities, according to the expert.

In coding, the expert views GLM and Kimi as among the leading domestic models. DeepSeek and Qwen are also viewed by the expert as strong competitors.

Healthcare, education and finance likely to become the next battlefields for AI agents, after coding

AI coding currently represents one of the clearest commercialization paths for LLM developers, a trend heavily validated by the rapid monetization of overseas peers like Anthropic's Claude Code. However, the expert thinks that the long-term total addressable market (TAM) for AI coding may face constraints. The core addressable user base requiring sophisticated, high-frequency coding assistance is relatively price-insensitive but modest in absolute size. Further, international players like Anthropic and OpenAI have already captured a meaningful portion of high-value global demand, according to the expert.

Consequently, the expert believes that the next phase of enterprise competition is expected to shift toward larger vertical markets, specifically healthcare, education, and finance. Healthcare represents the most immediate opportunity due to the acute demand for AI capabilities in medical consultations, diagnostic assistance, imaging interpretation, automated report generation, complex case discussions, and pharmaceutical R&D. Both education and finance sectors present abundant use cases, though AI penetration in finance will likely lag education due to stringent regulatory and compliance constraints, according to the expert.

Value of high-quality data elevates for vertical AI agents

According to the expert, securing high-quality vertical data remains a key prerequisite for sharpening vertical model capabilities. Because this data is rarely accessible in the public domain due to commercial sensitivity and privacy regulations, internet platforms with proprietary transaction, operational, or user-behavior data hold a structural advantage.

The expert believes this data dynamic explains why large vertical platforms are opting to build proprietary models rather than relying on external foundation model providers. The expert cited Meituan as an example that has developed its own LLM, LongCat, specifically to prevent proprietary operational data leakage.

While the general-purpose foundation model market is expected to consolidate over time, the expert anticipates that highly viable, industry-specific solution providers will continue to emerge across the healthcare, education, travel, and finance sectors.

Unit inference costs on the decline due to increased adoption of domestic chips and improved infrastructure efficiency

On the infrastructure side, the expert said Moonshot has increased the proportion of domestic inference chips in its infrastructure, while still using NVIDIA H20 and other NVIDIA GPUs for part of its inference workload. Under the current compute mix, the expert indicated that the gross margin for K2.7-related inference workloads is approaching the $\sim 30\%$ level.

API price reductions are likely to remain an industry trend, driven by competition and declining inference costs. However, the expert does not believe price cuts necessarily imply significant margin compression. As domestic chip usage rises, inference concurrency improves, and resource utilization increases, unit inference costs should continue to decline which could offset the pressure from price cutting.

Pivoting towards a closed-source strategy for easier monetisation Moonshot's open-source framework serves as a balanced mechanism for developer outreach, public relations, and commercial monetization. Open-source models are highly effective for building brand equity and developer mindshare – particularly in overseas markets – by lowering the entry barriers for initial testing and showcasing technical capability under resource-constrained environments, according to the expert.

Conversely, unrestricted open-source distribution can dilute direct commercialization, as enterprise users may favor free local deployment over paid API integrations, dampening conversion rates. To mitigate this, the expert stated that AI labs like Moonshot are inclined to adopt a tiered model strategy over time. Under such a strategy, mid-tier and lower-tier models may be open-sourced to support developer ecosystems and market awareness, while flagship models are likely to remain closed-source and priced at a premium to protect monetization and gross margin, according to the expert. We note that Alibaba's Qwen initially favored broad open-source deployment but chose a closed-source, premium API delivery model for its latest flagship model, Qwen 3.7 Max.

## AI labs likely triumph over big internet platforms

The expert believes the general-purpose LLM market would undergo structural consolidation, ultimately leaving only a select group of players. The expert thinks that pure-play LLM developers like Moonshot and DeepSeek are well-positioned to compete effectively against large internet conglomerates like Alibaba and ByteDance, arguing that big internet platforms may risk diluting their focus by expanding across the entire AI value chain. In the expert's view, big platforms should and eventually will, focus primarily on cloud and AI infrastructure services, which are lucrative and easier to commercialise.

We do not fully agree with the expert's view regarding the ultimate landscape of the Chinese LLM industry. While independent AI labs currently hold a tactical lead in specific verticals like AI coding – owing to their first-mover focus – we believe large internet platforms remain formidable competitors in the broader LLM market. They possess deep technical know-how, unmatched capital reserves, and significant data ecosystems generated by their core internet operations.

We view it as highly unlikely that major tech platforms will de-emphasize their proprietary LLM initiatives simply because they are happy with the abundant revenue being generated from underlying infrastructure services. The strategic significance of owning a proprietary LLM extends far beyond standalone commercial monetization; it serves as the foundational core framework ("the brain") powering all existing and future consumer and enterprise AI applications. This strategic necessity will continue to drive large internet platforms to invest heavily to maintain SOTA model performance, in our view.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Rachel Guo and Jialong Shi, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

58% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 33% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

39% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

3% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 15% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

## Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at:

http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise

stated in the valuation methodology; Japan: Russell/NOM Large Cap.

## SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

## Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or the market, and may not occur if the company's earnings differ from estimates.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated b

[中间内容因长度限制已省略]

ULAR NEEDS BEFORE MAKING A COMMITMENT TO PURCHASE ANY SECURITIES, INCLUDING SEEKING ADVICE FROM AN INDEPENDENT FINANCIAL ADVISER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page: http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
