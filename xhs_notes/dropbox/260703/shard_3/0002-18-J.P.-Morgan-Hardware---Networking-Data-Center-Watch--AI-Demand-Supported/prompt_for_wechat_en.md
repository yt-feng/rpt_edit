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
## Hardware & Networking

## Data Center Watch: AI Demand Supported as LLM Usage and GPU Pricing Climb; Meanwhile, Memory Spot Prices Diverge

In the Data Center Watch report, we outline key data points relevant to AI infrastructure demand, including LLM token volumes and prices, GPU rental prices, and memory costs. Taken together, the latest data suggest positive trends for the AI infrastructure demand environment, including the expansion of LLM usage, which is more than offsetting year-on-year LLM token price declines, while GPU rental prices continue to grind higher month-on-month. Importantly, based on our sample and simplified assumptions, we estimate that token economics are directionally tracking favorably for model providers, even assuming conservative token prices. Meanwhile, DRAM prices continue to rise, albeit at a slower rate, while NAND spot prices have contracted modestly for three months in a row. Key highlights from Data Center Watch report:

\- LLM trends re-accelerate on OpenRouter for the month of June. LLM trends on OpenRouter in June broadly re-accelerated, with token volume (+70% m/m, 20x y/y), pricing (up modestly m/m but still -5% y/y, with U.S. models bucking the trend by rising y/y), and spending (+70% m/m, 16x y/y) all increasing. Interestingly, while U.S.-based models lost volume share (35%), they dominated spend (85%+), with Anthropic's Claude Opus 4.7 standing out as the only model ranking top five in both volume usage and spending.

\- GPU rental prices rise across all tiers in the month of June. GPU rental price sequential growth continued across the board in June for non-hyperscaler capacity, with prices for all three tiers of Nvidia GPUs (A100, H100, B200) tracking higher m/m. A100s led the m/m gains, posting the steepest sequential increase among the three, while H100s and B200s expanded at a more measured pace. Pricing for B200s was \~2x that of H100s, and H100 pricing was \~1.7x that of A100s, with both ratios ticking marginally lower for the second month in a row.

\- Memory prices remained elevated in the month of June but diverged, with DRAM and NAND moving in opposite directions. DRAM spot prices climbed sequentially again in June, a third straight monthly gain that puts it up more than 8x y/y, while NAND spot prices slipped modestly, a third consecutive small monthly decline after a strong 1Q26 run-up, yet still sitting over 5x higher y/y.

## LLM Token Tracker

Our LLM Token Tracker captures a single week of usage and pricing data each month, providing a monthly snapshot or sampling of trends across \~300 LLMs listed on OpenRouter, an aggregation platform that routes API requests to models through a single endpoint. Keep in mind, OpenRouter skews towards developer, startup, and agentic-coding traffic and excludes first-party API volume (direct OpenAI/Anthropic, hyperscaler-hosted endpoints).

Key takeaways:

\- Token volume growth accelerated in the month of June, following a

See page 5 for analyst certification and important disclosures.

IT Hardware/ Telecom & Networking Equipment

Joseph Cardoso AC
(1-212) 622-9036
joseph.cardoso@jpmchase.com

Manmohanpreet Singh
(1-212) 622-4527
manmohanpreet.singh@jpmchase.com

Marc Vitenzon
(1-212) 622-3342
marc.vitenzon@jpmchase.com

Akanksh Chauhan
(1-212) 622-0045
akanksh.chauhan@JPM.com
JPM Securities LLC

moderation in growth through the start of 2026. Token volume growth accelerated in June, expanding +70% m/m (vs. +33% in May and +5% in April) and 20x y/y (vs. 12x in May and 15x in April). By comparison, volumes for U.S.-based models (OpenAI, Anthropic, Google, xAI, etc.), which represent 35% of the total (vs. 46% in May and 56% in April), also saw growth accelerate in June, expanding +30% m/m (vs. +9% in May and +23% in April) and 8x y/y (vs. 6x in May and 10x in April).

\- Token pricing continued to trend lower year-over-year into June, albeit more modestly than in recent months. While average token pricing rose +7% m/m in June (vs. +5% in May and +19% in April), year-over-year declines continued, albeit at a more moderate rate, tracking down -5% y/y (vs. -21% in May and -24% in April). We believe this moderation in the rate of decline was led by strong pricing trends for U.S.-based models, as evident in volume-weighted average pricing, which rose +27% m/m for U.S. models (vs. +19% in May and +10% in April) and +77% y/y (vs. +36% in May and +4% in April) vs. flat m/m for total models (vs. -8% in May and +15% in April) and -20% y/y (vs. -25% in May and -23% in April).

\- Token spending also accelerated in June, following a moderation in growth over the past two months. Token spending growth accelerated in June, expanding +70% m/m (vs. +23% in May and +21% in April) and 16x y/y (vs. 9x in May and 12x in April). By comparison, spending for U.S.-based models, which represent 85%+ of the total (vs. 90% in May and 85% in April), also saw growth accelerate in June, expanding +65% m/m (vs. +30% in May and +35% in April) and 14x y/y (vs. 8x in May and 10x in April).

\- Opus 4.7 ranks as a top five model across both usage and spending. The top five models in June based on token usage were: 1) DeepSeek V4 Flash; 2) MiMo-V2.5; 3) MiniMax M3; 4) Hy3 preview; and 5) Claude Opus 4.7, accounting for $45\%$ of total token volume. However, on a spending basis, the top five models in June were: 1) Claude Opus 4.7; 2) Claude Opus 4.8; 3) GPT-5.5; 4) Claude Sonnet 4.6; and 5) GLM 5.2, accounting for $75\%$ of total token spend.

Figure 1: Token Volumes  
![](images/c8ef66c4c1d47fc7f13af47afe4397a9bb91a78fc10b1ff9e429146c3730a208.jpg)  
Source: OpenRouter, JPM Estimates
Note: "U.S. Weekly Tokens" includes U.S.-based models

Figure 2: Average Token Pricing  
![](images/ade1d6d2658cbdd281b7a80b8e12b85d48fa7a2b59500189b585c89a04a7db38.jpg)  
Source: OpenRouter, JPM Estimates

Figure 3: Volume-Weighted Average Token Pricing  
![](images/784e98ede88090e30438e28da76383a942404eb6d4f69100809c9bb1edcd0f20.jpg)  
Source: OpenRouter, JPM Estimates
Note: "U.S. VWAP" includes U.S.-based models

Figure 4: Snapshot of Weekly Token Spend \$ in Million  
![](images/75ad5b918e335cb047fd0e58139a927a1c0f13055a021ad18eba81539f50ac10.jpg)  
Source: OpenRouter, JPM Estimates
Note: "U.S. Spend" includes U.S.-based models

Figure 5: Top 20 Models Based on Volume Weekly Tokens in Trillion  
![](images/20a4c40657f7ed9b84a588570a80e90fb2d3a348c0b02b91f218c7d34d613e81.jpg)  
Source: OpenRouter, JPM Estimates

Figure 6: Token Pricing vs. Volume  
![](images/8af20e4caf1911cfecd824a76b9907549be534aafe47f9e59fa87c3644c58c93.jpg)  
Source: OpenRouter, JPM Estimates

## GPU Rental Price Tracker

Key takeaways based on Bloomberg indices:

\- A100 rental prices grew sharply m/m in June; H100-to-A100 ratio ticks lower. A100 rental prices tracked to \$1.63/GPU-hour on average in June, up +6.3% m/m (vs. +6.6% m/m in May and +1.8% m/m in April), representing a fifth straight month of sequential growth.

\- H100 rental prices continued m/m gains in June. H100 rental prices tracked to \$2.72/GPU-hour on average during June, a +3.7% m/m increase (vs. +3.2% m/m in May and +2.1% m/m in April), marking a seventh straight month of sequential growth. The H100-to-A100 price ratio tracked to 1.67x on average in June (vs. 1.71x in May and 1.77x in April).

\- B200 rental prices expanded m/m in June; B200-to-H100 ratio continued to move lower. B200 rental prices tracked to \$5.33/GPU-hour on average in June, up +2.7% m/m (vs. +0.4% m/m in May and +1.3% m/m in April), with the m/m increase trailing the H100 and A100 sequential gains. The B200-to-H100 price ratio tracked to 1.96x on average in June (vs. 1.98x in May, 2.04x in April, and 2.58x around index launch in Sep-25).

Figure 7: Avg. Monthly Rental Prices (Non-Hyperscaler)  
![](images/a7185b126b4e73a7d36d5c8602c974805fc1eff8e899c536a3959647b24a567b.jpg)  
Source: Bloomberg Finance L.P.  
Figure 8: Avg. Monthly Rental Prices (M/M %Change)

![](images/508197e95d6ae22cb5af1ca0df6a975f88b601cf8a2e47d0251a0a11f7235999.jpg)  
Source: Bloomberg Finance L.P.

## Memory Price Tracker

Key takeaways based on Bloomberg data:

\- DRAM spot prices continued to rise in June, with DDR5 16Gb up more than 8x y/y. DDR5 16Gb spot prices reached \$43.14 in June, rising +10% m/m (vs. \$39.24 in May and \$33.12 in April) and +740% y/y (vs. \$5.13 in June-25), marking a third consecutive m/m increase following modest sequential declines in February and March.

\- NAND spot prices decline modestly m/m in June; NAND 1Tb still up over 5x y/y. NAND 1Tb spot prices tracked to \$27.03 in June, a modest decline of -0.3% m/m (vs.

27.12 in May and 27.43 in April) and an increase of +412% y/y (vs. 5.28 in June-25), marking a third consecutive month of modest m/m declines following the strong run-up through 1Q26.

Figure 9: Memory Prices (M/M %Change)  
![](images/074c8f24ebd7f449042b8650a3f969493a43f8c207f31161714285c39be73e11.jpg)  
Source: Bloomberg Finance L.P.

Figure 10: Memory Prices (Y/Y % Change)  
![](images/b16f760a606c0abe066ee5524617d3534cce6d7eec3c8ded9184e6ccdf666075.jpg)  
Source: Bloomberg Finance L.P.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Cardoso, Joseph : Amphenol (APH), Arista (ANET), Axon (AXON), CDW (CDW), Calix (CALX), Celestica (CLS), Ceva (CEVA), Ciena (CIEN), Cisco (CSCO), Coherent Corp (COHR), Corning (GLW), Credo (CRDO), Dell Technologies (DELL), Everpure (P), F5 Inc (FFIV), Fabrinet (FN), Flex Ltd (FLEX), Garmin Ltd. (GRMN), HP Inc (HPQ), Hewlett Packard Enterprise (HPE), Ingram Micro (INGM), Insight Enterprises (NSIT), Jabil Inc (JBL), Keysight Technologies (KEYS), Logitech International (LOGI), Lumentum (LITE), Mobileye (MBLY), Motorola Solutions Inc (MSI), NetApp, Inc. (NTAP), Nutanix (NTNX), Qualcomm (QCOM), Seagate (STX), Super Micro (SMCI), TD SYNNEX (SNX), Teradyne (TER), Vistance Networks (VISN), Western Digital (WDC), Wolfspeed Inc (WOLF), Xerox Holdings Corp (XRX)

## JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used,

please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance obligations when making investment decisions.

Any digital or crypto assets discussed in this research report are subject to a rapidly changing regulatory landscape. For relevant regulatory advisories on crypto assets, including bitcoin and ether, please see https://www.JPM.com/disclosures/cryptoasset-disclosure.

The author(s) of this research report may not be licensed to carry on regulated activities in your jurisdiction and, if not licensed, do not hold themselves out as being able to do so.

Exchange-Traded Funds (ETFs): JPM Securities LLC (“JPMS”) acts as authorized participant for substantially all U.S.-listed ETFs. To the extent that any ETFs are mentioned in this report, JPMS may earn commissions and transaction-based compensation in connection with the distribution of those ETF shares and may earn fees for p

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 30 Jun 2026 10:04 PM EDT

Disseminated 01 Jul 2026 06:00 AM EDT
"""
