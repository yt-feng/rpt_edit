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
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Global Memory

EQUITY: TECHNOLOGY

# Real AI boom is here, embrace the new regime

Expect memory stock re-rating driven by exponential demand growth from AI

# Exponentially growing AI-driven demand vs limited memory supply

The memory industry entered a structural growth phase following the launch of ChatGPT [owned by OpenAI (unlisted)] in December 2022, which triggered considerable growth in GPU and HBM (high-bandwidth memory) demand. SUBSequently, the adoption of Retrieval-Augmented Generation (RAG) and agentic AI applications has accelerated demand for conventional servers and SSDs, and initiated a triple memory super-cycle (commodity DRAM, HBM, and SSD) since 3Q25.

As AI semiconductor demand shifts from training toward inference workloads, memory demand is entering a period of exponential expansion. This reflects the rapid growth in KV-cache memory requirements, driven by increases in user base, user engagement time, AI task complexity (Fig. 6), reasoning-token consumption, and the emergence of agentic AI, where token usage per user is surging exponentially. Memory demand effectively scales as the multiplicative function of these variables (10 x 200 x 30 x 10 x ...), implying that memory demand could rise by several thousand-fold over the next five years, in our view. In contrast, we believe industry supply growth is likely to remain constrained to roughly 5-6x over the same period (CAGR of c.30%), raising serious questions around whether structural undersupply can realistically be resolved.

At present, the industry is attempting to narrow this widening supply-demand gap through multiple software- and architecture-level optimizations, including technologies such as KV-cache compression and selective cache eviction. However, we believe these solutions merely slow the pace of growth rather than reversing the trend. Therefore, every available approach – including NAND offloading (which offers over 100x higher capacity despite slower speeds) and the adoption of ultra-high-bandwidth NAND (HBF) – will likely need to be deployed simultaneously, in our view.

Meanwhile, we believe the rise of agentic AI is significantly improving AI productivity while simultaneously driving a considerable increase in token consumption. Agentic AI is also creating entirely new categories of semiconductor demand, including CPUs and commodity memory. However, these developments ultimately reinforce the usage expansion of AI servers themselves, thereby driving another leg of sUBStantial growth in GPU- and memory-related demand, in our view.

Fig. 1: Memory – stocks for action 

<table><tr><td>Company</td><td>Ticker</td><td>Rating</td><td>Target price (KRW)</td><td>Current price (KRW)</td><td>Upside</td></tr><tr><td>Samsung Electronics</td><td>005930 KS</td><td>Buy</td><td>590,000</td><td>270,500</td><td>118.1%</td></tr><tr><td>SK Hynix</td><td>000660 KS</td><td>Buy</td><td>4,000,000</td><td>1,819,000</td><td>119.9%</td></tr></table>

Note: Share price as of 15 May 2026.   
Source: NOM

(continued on the next page)

# Research Analysts

# Asia Technology

# CW Chung - NIHK

cwchung@NOM.com

+852 2252 6075

# Korea Technology

# Eon Hwang - NFIK

eon.hwang@NOM.com

+822 3783 2318

# YJ Kim, CFA - NFIK

yj.kim1@NOM.com

+82237832332

# AI-based innovations are actually happening and will create a self-reinforcing investment cycle

The advancement of agentic AI could finally unlock a step-function improvement in enterprise productivity. Combined revenue for leading AI software and service vendors such as Anthropic (unlisted), Gemini (provided by Google [GOOGL US, Not rated]), and Open AI could potentially expand by more than 100x over the next five years from the current level of approximately USD70bn, in our view. Until recently, such forecasts appeared detached from reality, but they are increasingly becoming plausible. Anthropic is reportedly expected to achieve a breakeven point by 2027E, while Open AI is targeting profitability around 2029E (link). Despite still generating losses today, these companies are already raising capital at unprecedented valuations, with aggregate equity values now approaching the trillion-dollar range (link 1, link 2).

We believe the revenues and capital generated by these AI service providers will, in turn, flow back to hyperscalers and CSPs such as Amazon (AMZN US, Not rated), Google, and Microsoft (MSFT US, Not rated) through cloud infrastructure spending, thereby creating a powerful self-reinforcing investment cycle in data center expansion. We believe the true Fourth Industrial Revolution is now beginning.

In our view, this transition represents an unprecedented new regime, including AI robots and autonomous driving. We believe the resulting wealth disparities, cross-country gaps, and social/political impacts are likely to exceed current expectations, while institutional and regulatory preparedness remains extremely limited. Nevertheless, AI appears to be an irreversible trend, and the Rubicon has already been crossed. AI's growth trajectory is unlikely to slow organically, in our view. In fact, leading AI experts are increasingly less concerned about whether AI will succeed, and more concerned about whether AI could become excessively powerful.

# LTAs and structural supply shortage to reduce risk premiums and drive re-rating for memory suppliers

Until recently, investors questioned whether LTAs between memory vendors and CSPs (cloud service providers) could truly differ from unsuccessful LTA structures seen in previous cycles, and whether the eventual slowdown of memory price increases could once again become a negative catalyst for stock prices. However, we believe investor perception is now beginning to improve materially. Contracts under the conditions reportedly embedded within current LTAs are progressing not only with CSPs but also with a broad range of memory customers. Three-to-five years of minimum contract periods, prepayments, and capex support commitments appear increasingly common, making cancellation difficult and enhancing binding aspects of contracts, effectively guaranteeing near-current level of profitability.

Importantly, we believe customer demand for HBM and high-performance memory already appears to exceed the industry's mid- to long-term supply capabilities. Therefore, we think the stable earnings outlook for memory vendors is becoming less dependent on LTAs themselves and more anchored by the underlying structural demand environment that effectively forces customers to accept such conditions. In our view, semiconductors are equivalent to AI, and memory is one of the key bottlenecks within the AI value chain.

Against this structural backdrop, we believe memory vendors have entered an unprecedented phase of rapid revenue growth and margin expansion in a short period of time. Over the next 3-5 years, and at minimum through 2027-31F, we expect annual revenue and earnings growth of approximately 30% following 7-8x profit increase in 2026F, backed by: (1) annual volume growth of \~30%, (2) stable or a slight increase in commodity memory prices based on LTAs, and (3) improvement in HBM profitability, converging to that of commodity DRAM, although we believe a likely KRW appreciation impact could reduce reported revenue by 10-20%. We believe this resembles a growth outlook comparable to TSMC's (2330 TT, Buy) 30% CAGR (over 2025-28F), which currently trades at a 12MF P/E of \~20x.

(continued on the next page)

# SEC and Hynix trade at unfairly low valuations; raise TP by factoring in lower risk premiums

For 2027F, which represents year one of this new LTA cycle, we forecast combined OP for Samsung Electronics (SEC; 005930 KS, Buy) and SK Hynix (000660 KS, Buy) to reach multiples of TSMC's expected earnings and sUBStantially exceed those of competitor Micron (MU US, Not rated). However, both SEC and Hynix still trade at a 12MF P/E of \~6x.

We believe this resulting implied risk premium (19% for SEC, 24% for Hynix; calculated as 1/[P/E – risk-free rate], with a risk-free rate of 4%) is unfairly high. Historically, weak shareholder return policies and high earnings volatility justified valuation discounts. However, we believe many of these discount factors are now structurally diminishing, or could largely disappear over at least the next five years.

As highlighted in our pervious report on SEC and Hynix, we expect these discount factors to gradually normalize, resulting in sustained valuation multiple expansion. We now believe the market should increasingly reflect the strength of long-term demand visibility and the durability of the emerging LTA framework, and therefore, we are beginning to incorporate this lower risk premium into our TP.

# Key risks currently being debated by the market regarding memory demand

First, investors continue to question whether CSPs can sustain their aggressive capex, or more fundamentally, whether AI demand could ultimately disappoint

expectations, leading companies such as Anthropic, Open AI, and Gemini (provided by Google) to face monetization or funding challenges that could interrupt the current virtuous cycle. However, we increasingly view such concerns as outdated. We believe AI demand has already passed the singularity point, and its primary drivers are now enterprise and sovereign AI demand. In our view, while CSPs' FCF could temporarily decline, this largely reflects their conviction in future profit generation. In fact, we believe their OCF is already growing materially faster than the market's overly conservative expectations.

# Second, we think there remains significant concern that US data center

construction could proceed more slowly than expected, particularly due to structural power shortages. Going forward, we expect a broad range of new solutions to emerge, including unprecedented innovations in power-efficiency technologies and the mobilization of new energy sources. Nevertheless, we continue to view this issue – particularly in the US – as a meaningful bottleneck risk. Compared with the highly optimized productivity of Asian memory suppliers, US construction sites remain materially slower and less efficient, while the power infrastructure supply chain, which has experienced years of underinvestment, still appears insufficiently prepared for the scale of the current AI-driven expansion cycle, in our view. As a result, we believe the memory industry may need to monitor data center construction progress, even through satellite imagery if needed.

Third, in our view, while direct CSP investment currently accounts for roughly half of total data center investments, a sUBStantial portion of the remaining investment appears to be financed by non-cloud operators leveraging long-term cloud purchase agreements signed with CSPs. These project financing structures are highly sensitive to funding costs. Therefore, if long-term bond yields rise sharply due to inflationary pressures, we believe project-related risks could increase meaningfully. In our view, memory price increases alone could contribute more than 0.8% to the US CPI this year, while higher oil prices driven by the Middle East geopolitical tensions may keep inflation and interest rates elevated for longer than currently expected. However, provided end-demand remains sufficiently strong, we believe refinancing markets should remain accessible even in a higher-rate environment, suggesting there is not yet a need for excessive concern.

(continued on the next page)

Fig. 2: DDR5 spot vs contract price trend   
![](images/e7f0d18da8720c3e62fad137454ef196e93307b0b52887700d27e0fd827a5bb8.jpg)

<details>
<summary>line</summary>

| Date   | Spot (session high) | Contract |
|--------|---------------------|----------|
| Jan-25 | 3.0                 | 3.0      |
| Apr-25 | 3.0                 | 3.0      |
| Jul-25 | 4.0                 | 3.0      |
| Oct-25 | 5.0                 | 3.0      |
| Jan-26 | 18.0                | 4.0      |
| Apr-26 | 26.0                | 13.0     |
</details>

Note: Spot price based on DDR5 16Gb (2Gx8) 4800/5600 session high prices; contract prices based on DDR5 16GB U-  
DIMM; both prices converted into USD/GB terms.   
Source: DRAMeXchange, NOM

Fig. 3: Global memory sales and y-y growth   
![](images/928b384e0eb74a2b9b0286f4bb96d56e50ebd1e0ee14074b6aa177132d6b77c9.jpg)

<details>
<summary>line</summary>

| Year | Memory sales (LHS) (bn USD) | Memory sales y-y growth (%) |
|------|------------------------------|-----------------------------|
| 80   | ~0                           | ~50                         |
| 81   | ~0                           | ~30                         |
| 82   | ~0                           | ~20                         |
| 83   | ~0                           | ~40                         |
| 84   | ~0                           | ~150                        |
| 85   | ~0                           | ~140                        |
| 86   | ~0                           | ~10                         |
| 87   | ~0                           | ~30                         |
| 88   | ~0                           | ~60                         |
| 89   | ~0                           | ~90                         |
| 90   | ~0                           | ~20                         |
| 91   | ~0                           | ~30                         |
| 92   | ~0                           | ~40                         |
| 93   | ~0                           | ~50                         |
| 94   | ~0                           | ~60                         |
| 95   | ~0                           | ~70                         |
| 96   | ~0                           | ~80                         |
| 97   | ~0                           | ~10                         |
| 98   | ~0                           | ~20                         |
| 99   | ~0                           | ~30                         |
| 00   | ~0                           | ~40                         |
| 01   | ~0                           | ~50                         |
| 02   | ~0                           | ~60                         |
| 03   | ~0                           | ~70                         |
| 04   | ~0                           | ~60                         |
| 05   | ~0                           | ~50                         |
| 06   | ~0                           | ~40                         |
| 07   | ~0                           | ~30                         |
| 08   | ~0                           | ~20                         |
| 09   | ~0                           | ~10                         |
| 10   | ~0                           | ~5                          |
| 11   | ~0                           | ~3                          |
| 12   | ~0                           | ~2                          |
| 13   | ~0                           | ~1                          |
| 14   | ~0                           | ~0                          |
| 15   | ~0                           | ~1                          |
| 16   | ~0                           | ~2                          |
| 17   | ~0                           | ~3                          |
| 18   | ~0                           | ~4                          |
| 19   | ~0                           | ~5                          |
| 20   | ~0                           | ~6                          |
| 21   | ~0                           | ~7                          |
| 22   | ~0                           | ~8                          |
| 23   | ~0                           | ~9                          |
| 24   | ~0                           | ~10                         |
| 25   | ~0                           | ~15                         |
| 26F  | ~5                           | ~35                         |
| F    | ~15                          | ~45                         |
| F27F | ~25                          | ~45                         |
</details>

Source: WSTS, NOM

Fig. 4: SEC – 2026F/27F OP NOM vs BBG   
![](images/6ae1fada909529078bfe3a74bb8a4649a64ee9821a4452a55d45af0f7b2a2adf.jpg)

<details>
<summary>line</summary>

| Date     | 2026F NMR est. | 2026E BBG | 2027F NMR est. | 2027E BBG |
|----------|----------------|-----------|----------------|-----------|
| 2024-07  | 100            | 80        | 100            | 90        |
| 2025-01  | 50             | 40        | 50             | 40        |
| 2025-07  | 50             | 40        | 50             | 40        |
| 2026-01  | 150            | 130       | 350            | 300       |
| 2026-07  | 350            | 300       | 450            | 400       |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 5: Hynix – 2026F/27F OP NOM vs BBG   
![](images/52d8866beb659a2f3c664d751f8656d9f1cf91bd67ec221d6db498248a267766.jpg)

<details>
<summary>line</summary>

| Date     | 2026F NMR est. | 2026E BBG | 2027F NMR est. | 2027E BBG |
| -------- | -------------- | --------- | -------------- | --------- |
| 2024-07  | ~60            | ~30       | ~60            | ~30       |
| 2025-01  | ~40            | ~30       | ~40            | ~30       |
| 2025-07  | ~50            | ~40       | ~60            | ~40       |
| 2026-01  | ~100           | ~80       | ~150           | ~90       |
| 2026-07  | ~280           | ~240      | ~380           | ~320      |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 6: Estimated token consumption by prompt cases 

<table><tr><td rowspan="2"></td><td rowspan="2">Mainhardware</td><td colspan="8">Estimated token consumption per case</td></tr><tr><td>Simultaneousinterpretation</td><td>Simplequestion</td><td>Structuredconstraint</td><td>Styleexpansion</td><td>RAGquestion</td><td>Imagegeneration</td><td>Agent AI (report +model)</td><td>1-hour video generation</td></tr><tr><td>User&#x27;s prompt input</td><td>CPU +DRAM</td><td>(instanttranslation)</td><td>&quot;How&#x27;s the weather today?&quot;</td><td>&quot;How&#x27;s the weather toady? Please answer in 5 words or less&quot;</td><td>&quot;How&#x27;s the weather today? Please answer like a poet.&quot;</td><td>&quot;Explain about reasons behind national debt increase&quot;</td><td>&quot;Please describe today&#x27;s weather in an abstract painting.&quot;</td><td>&quot;Make earnings models and company note based on the model&quot;</td><td>&quot;Make a 1-hour video describing recent weather&quot;</td></tr><tr><td>Scheduling</td><td>CPU +DRAM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Input token</td><td>GPU + HBM</td><td>10</td><td>10</td><td>20</td><td>25</td><td>40</td><td>20</td>

[中间内容因长度限制已省略]

 SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian Citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are Citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its sUBSidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
