You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# JPM

## Nanya Technology

## 2Q26 a slight beat; rising server mix coupled with favorable LTAs to bode well for mid-long term earnings; reiterate OW

NYT's 2Q results were a slight beat vs. JPMe/consensus thanks to sustained pricing momentum (DRAM ASPs up $>60\%$ ) alongside a flattish bit shipment trend. Management raised its 2026E bit growth guidance to high-teens $\%$ Y/Y (from teens $\%$ in 1Q26), citing lower inventory levels vs historical trends, and reiterated its 2026 capex guidance of NT\$52bn, pointing to severe industry-wide shortages (S-D shortage continuing into 2028E, consistent with Micron commentary). We expect both DDR5 and DDR4 pricing to trend higher in 2H26E as the demand outstripping supply environment continues. We found NYT's server sales mix exposure increase as a positive development and its product diversification into LPDDR5 (likely for server applications in our view) and other line-ups. Mid-to-long term capex plan of US\$16bn for 45k wspm capacity sounded higher than our initial expectation; however, we view overall capital intensity under control and expect an increase in R&D spending to support NYT's product diversification initiatives amidst its flexibility to move around between DDR5 and DDR4. We expect volatile NYT share sentiment to continue in the near-term until CSP's capex guidance upward revision is confirmed in July earnings result call season. Risk-reward profile remains favorable on a medium-term horizon and we recommend investors accumulate the stock on our bullish top-down memory upcycle view ("higher for longer"). Next catalysts are: 1) CSP's hardware capex spending and AI monetization progress update, 2) Asian memory peers' outlook commentary, 3) DDR4/DDR5 monthly pricing update, and 4) China memory competitor's mid-term business plan update post IPO.

\- 2Q26 result flash and 2H26E update. NYT reported OP of NT\$60.8bn on sales of NT\$82.5bn (OPM: 74%), driven by flat bit shipment growth (JPMe: -MSD%) and high-60% ASP growth (JPMe: 70%+ growth), which together delivered strong operating leverage. Before new capacity installation translates into a production bit growth (post flattish H/H bit shipment trend in 1H26, implied 2H26E bit shipment is likely to be down H/H), we expect pricing to be the key earnings driver in 2H26E and expect blended ASP increase of +20%/+11% each respectively in 3Q26E/4Q26E. Of note, DDR4 pricing momentum remained stronger vs. DDR5 in 2Q26, and we expect such a trend to continue in the short-term. Interestingly, AI infrastructure and server applications accounted for >20% of NYT's sales and we found the progress constructive given the firm's historical server compute sales exposure has ranged between 10-15% in the past. Including eSSD (indirect server exposure), we believe actual server compute exposure to be higher. We continue to view NYT's attempt to enter the server ARM CPU supply chain via the LPDDR5X stacked solution product offering as the next major driver and expect a rising server exposure to bode well for NYT's earnings profile in the near to mid term as highlighted in our recently published OW upgrade note (link).

\- Various LTAs to help dampen earnings cyclicality. Management noted that, amid supply tightness expected to persist for multiple quarters, customers are increasingly entering into multi-year LTAs, which improve planning visibility

## Overweight

2408.TW, 2408 TT
Price (09 Jul 26):NT\$435.50

Price Target (Jun-27): NT\$710.00

## Technology - Semiconductors

Jay Kwon AC
(82-2) 758-5725
jay.h.kwon@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

See page 8 for analyst certification and important disclosures, including non-US analyst disclosures.

Sangsik Lee
(82-2) 758 5146
sangsik.lee@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

Neelay Y Kamath
(91-22) 6157 3764
neelay.kamath@jpmchase.com
JPM India Private Limited

and can help underpin pricing. In parallel, incremental “greenfield” capacity additions appear to be tied to multi-year LTAs extending beyond 2028, giving NYT a clearer line of sight into both near-term requirements and longer-term demand commitments. The company also emphasized that LTAs vary in structure: some lock in both volume and price for the contract term (with renewal upon expiry), while others commit to volumes but set pricing based on prevailing market conditions, typically reset on a quarterly cadence. Overall, we expect Nanya Technology to continue expanding its use of LTAs, which should help dampen earnings cyclicality relative to what the memory industry has historically experienced over the past two decades.

\- Capex update and implications to 2027E-2028E bit production. The company reiterated its plan to spend NT\$52bn (in-line with JPMe) on capex in 2026 (1H run-rate of NT\$6.9bn, highlighting an unprecedented 2H spend of \~NT\$45bn) driven by the severe memory shortage being experienced in the industry. While the first phase of the new fab capacity expansion is planned to reach 30k wspm by 2028, peak output is expected to reach 45k wspm, with total capex estimated at NT\$480 billion, with construction cost near US\$3bn in total. Compared to our NT\$172bn estimate for 2026E-28E, this is significantly higher. We would like to highlight that such higher capex spending is a strong supply debottlenecking signal from NYT management amidst growing LTA discussions which should support the memory cycle moving with a lot more mid-to-long term stability. As a result of higher capex, we foresee a meaningful bit increase from 2028E onwards (JPMe: 2027E/2028E bit supply growth assumption at: +5%/+27%).

\- Stock implications. NYT stock gained 114% (vs. TWSE +39%) in the 2Q26 driven by strong DRAM pricing momentum as well as positive EPS upgrades. However, following strong MU results in late June'26 (link), memory share sentiment has been weak with NYT shares declining 17% from its peak (vs. Global memory peers -14% or SOX/TWSE -4%/-1%) due mainly to growing AI capex, continuity concerns post Meta headline (link). However, following a strong monthly update and Meta's 2x capacity build plan release (link), the stock has started to bounce back and is up 10% from the recent bottom. Until CSP's hardware capex guidance upward revisions signal becomes evident, we expect volatile range-bound share sentiment could continue. From an overall impression standpoint, we came back with more positives (near-term price strength, product mix improvement toward servers, solid LTA progress, and top-down S-D shortage view extending into 2028E) vs. negatives (substantially higher capex spending into 2028E) from the NYT results, and view the stock as risk-reward favorable from a midterm horizon. Maintain OW view on the stock and recommend investors accumulate.

Table 1: NYT 2Q earnings review table

<table><tr><td>(NT$ mn)</td><td>2Q25</td><td>1Q26</td><td>2Q26 Actuals</td><td>Q/Q (%)</td><td>Y/Y (%)</td><td>JPMe</td><td>Diff. (%)</td><td>BBG</td><td>Diff. (%)</td></tr><tr><td>Sales</td><td>10,526</td><td>49,087</td><td>82,549</td><td>68.2%</td><td>684.2%</td><td>81,279</td><td>2%</td><td>81,185</td><td>2%</td></tr><tr><td>Gross profit</td><td>(2,165)</td><td>33,316</td><td>65,619</td><td>97.0%</td><td>na</td><td>63,158</td><td>4%</td><td>64,061</td><td>2%</td></tr><tr><td>Gross Margin</td><td>-21%</td><td>68%</td><td>79%</td><td>1162 bps</td><td>10006 bps</td><td>78%</td><td>-179 bps</td><td>79%</td><td>58 bps</td></tr><tr><td>Operating profit</td><td>(4,501)</td><td>30,111</td><td>60,826</td><td>102.0%</td><td>na</td><td>59,244</td><td>3%</td><td>60,159</td><td>1%</td></tr><tr><td>Operating Margin</td><td>-43%</td><td>61%</td><td>74%</td><td>1234 bps</td><td>11645 bps</td><td>73%</td><td>-80 bps</td><td>72%</td><td>195 bps</td></tr><tr><td>Net Income</td><td>(4,102)</td><td>26,059</td><td>50,192</td><td>92.6%</td><td>na</td><td>49,454</td><td>1%</td><td>48,930</td><td>3%</td></tr><tr><td>Net Income Margin (%)</td><td>-39%</td><td>53%</td><td>61%</td><td>771 bps</td><td>9977 bps</td><td>61%</td><td>4 bps</td><td>60%</td><td>53 bps</td></tr><tr><td>New Taiwan GAAP EPS</td><td>(1.32)</td><td>8.41</td><td>14.55</td><td>73%</td><td>na</td><td>14.33</td><td>1%</td><td>14.57</td><td>0%</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates.  
![](images/6e6900205779453eb985e59304aa2c7997ad8ec587361454436dc576a09dad8a.jpg)  
Source: Bloomberg Finance L.P., Company data, JPM estimates

Figure 2: Global memory makers' share price performance including SOX (Philadelphia Semiconductor index)  
![](images/f82350596da49decacce2601bfbe152964d548b99185d4a6012d4adf8ecd7e75.jpg)  
Source: Bloomberg Finance L.P. Note: Past performance is not an indicator of future results

## Q&A highlights

## Q. What is the pricing trend for DDR4 and DDR5 into 3Q26?

A. Pricing continues to move higher. Short-term agreements offer greater room for ASP upside, while long-term agreements provide better stability.

## Q. What is the magnitude of further price increases?

A. No specific guidance. LTA pricing should remain relatively stable, while short-term pricing may continue to improve as contracts renew.

## Q. How do the DRAM S/D dynamics look into 2028-2029 as peers add new capacity?

A. The S/D environment is not expected to change drastically by 2028E. Despite new capacity additions, AI/server demand and supply constraints across non-AI applications should keep the overall market tight.

## Q. Was the key driver of 2Q26 earnings the $60\%+$ ASP increase despite flat bit shipments and limited cost changes?

A. Yes. Bit shipments were flat Q/Q and the cost structure was broadly stable, with limited cost reduction. The sharp earnings improvement was mainly driven by higher ASP.

## Q. Does $60\%+$ Q/Q ASP growth imply most of the business is still based on monthly price negotiations despite prior LTA announcements?

A. LTAs are generally based on fair market pricing at the time of negotiation. LTAs do not prevent price upside in a rising market.

## Q. Are LTAs designed to fix price, volume, or both?

A. LTA structures differ by customer. Some agreements fix volume, some include pricing commitments, and some include both. Pricing and volume terms are often reviewed with reference to market trends, typically on a quarterly basis.

## Q. What is the outlook for 3Q/4Q ASP and operating results?

A. 3Q operating results are expected to further improve, with OPM already at a high level and likely to move higher. For 4Q, visibility depends on market conditions.

## Q. Any impact from local Chinese DRAM makers' revenue or production increase?

A. There is no direct impact on NYT currently. The business remains stable globally, and customer/product overlap appears limited.

## Q. What is the product revenue mix?

A. DDR4 remains the largest contributor. DDR4 and LPDDR4 together account for roughly 60-70% of revenue, while DDR3 and DDR5 each account for approximately 10%, with the remainder split across other products.

## Q. Any color on the NT\$16 billion capex for 45K WSPM?

A. Construction costs are less than NT\$3bn and the rest is equipment including EUV. EUV adoption is expected around 2028E, potentially for 1C/1D/1E depending on equipment arrangement and technology timing.

## Q. Are there any updates on customized DRAM/AI solutions and HBM development?

A. Customized DRAM projects are progressing with multiple customers. Projects are also ongoing on HBM-related extensions, including wafer-to-wafer bonding, with product timing dependent on customer project schedules.

## Q. What is the outlook for non-AI products into 2028?

A. High-end non-AI products are performing better than low-end products. NYT will continue to support non-AI customers across DDR3/LDDR4/DDR4/KDDR4 and other DRAM products, while prioritizing higher-value applications where supply remains tight.

## Q. Given that DDR5 demand is strong, why is DDR5 only around 10% of total revenue?

A. Demand is strong across DDR4, LPDDR4, DDR3, and DDR5, but capacity is limited. DDR3/DDR4 supply is more constrained, and economics remain attractive, so NYT continues to allocate meaningful capacity to these products rather than shifting more aggressively to DDR5.

## Q. What applications are driving demand?

A. Consumer-related applications include auto, industrial, and communications. These applications account for roughly 60% of revenue, with the remainder coming from cloud, PC, and mobile.

## Q. What is the shareholder return outlook?

A. Dividend payouts will be balanced against capital needs for capex and equipment. There is still room for shareholder returns, with a potential dividend payout of around 40% of net profit.

## Q. Were employee bonuses expenses included in 2Q results?

A. Employee bonus expense was included in 1H26 results.

## Q. What are the details on the timing of capex spending?

A. Capex cash outflows will follow construction and equipment payment schedules. Payments are generally made after inspection and acceptance, so actual cash spending will lag committed capex.

## Q. Is the NT\$52bn 2026 capex plan based on commitments rather than cash payments?

A. Yes. Only NT\$6.9bn was paid in 1H26, and cash payments should increase in coming quarters as projects progress.

## Q. Could NYT receive stronger government support?

A. Government support remains fragmented across central, local, and departmental levels, but NYT continues to seek more unified support for Taiwan's DRAM industry.

## Q. How does Taiwan's foundry ecosystem help wafer-to-wafer product development?

A. Taiwan's advanced semiconductor ecosystem should help streamline customized memory projects. Several projects are pending, and proximity to leading foundry/packaging capabilities may support wafer-to-wafer development.

## Q. Would NYT consider LTA structures such as cash prepayment/price floors/take-or-pay to reduce default risk during downturns? A. Yes, such structures will be considered.

## Q. Given the cyclical nature of memory, what is the outlook from here?

A. Memory remains cyclical, especially for lower-value non-AI products. However, the overall market remains in shortage, supported by AI/server demand and tight capacity across applications.

## Q. Comment on NYT LPDDR potentially entering NVIDIA's Vera Rubin supply chain?

A. No comment due to customer confidentiality.

Q. What is the impact of the recent wafer price increases on gross margin?
A. The focus remains on ASP momentum. 2Q ASP increases are expected to continue into 3Q, which should help offset cost pressures.

Q. Is there better pull-in momentum from customers after earlier consumer price resistance?
A. Supply remains tight, limiting the ability to support incremental pull-in momentum.

# Investment Thesis, Valuation and Risks

Nanya Technology (Overweight; Price Target: NT\$710.00)

Investment Thesis

We are OW on NYT, given the resilient legacy DRAM pricing coupled with leading memory makers phasing out DDR4 to drive pricing leverage higher in 2H26E and 2027E. NYT's entry into the NVIDIA supply chain will help it to extend its server industry exposure well beyond the 20% level, while simultaneously reducing its large CE exposure, making its pricing trend less volatile and more stable. While we expect quarterly earnings y-y momentum to slightly decelerate as we head into 2H26, we see NYT as having a relatively favorable risk/reward in the near-mid term as we expect all memory stocks to move up together during an up-cycle.

## Valuation

Our June-27 PT of NT\$710 is based on 8x FY27E EPS, on par with the Korean DRAM makers driven by our higher-for-longer thesis (vs. previously diverging pricing momentum expectations between DDR4 and DDR5).

## Risks to Rating and Price Target

Downside risks include:

\- Shorter-than-expected legacy DRAM spot price momentum into 2H26.

\- A shorter-than-expected D4 16Gb die shelf cycle from the consumer market (i.e., customers' willingness to transition from D4 to D5, could result in weaker than expected D4/LPD4 pricing from 2026-end to 2027 onwards).

\- Unsuccessful AI-related memory product development, allowing the company to de-rate (a failure in next-gen technology migration, creating room for competitors to catch up).

\- Faster-than-expected DDR5 yield improvement from CXMT.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

• Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Nanya Technology or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Nanya Technology or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Nanya Technology or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered com

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
