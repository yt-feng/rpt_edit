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
# SAP (SAPG.DE): 2Q26: CCB stronger while EBIT below; FY26 EBIT guidance trimmed to reflect acquisition dilution; Buy

## Results

We see scope for slight negative revisions to consensus operating profit forecasts for SAP on the back of the updated FY26 EBIT guidance, which now reflects the dilutive impact of the Dremio and Prior Labs acquisitions that closed in July, as well as modestly softer EBIT growth in the quarter. Having said that, we expect a broadly neutral share price reaction given the relief from the CCB beat.

SAP's 2Q26 results demonstrated continued top-line resilience, with CCB remaining sequentially steady at $26\%$ yoy ex-fx (c.25% yoy ex-fx organic), ahead of GSe and consensus expectations of $25\% / 24\%$ , driven by continued strength in the Cloud ERP Suite. Management also highlighted momentum across its Autonomous Suite and Business AI Platform, resulting in improved coverage and a stronger pipeline post SAPPHIRE. Total revenues came broadly in line with GSe and consensus expectations, while Non-IFRS EBIT came in below expectations ( $2\% / 5\%$ below GSe/consensus), growing $9\%$ yoy ex-fx (vs. GSe/consensus at $10\% / 14\%$ ). The sequential deceleration was driven by lower cloud growth, higher SBC (reversing the unusually low SBC in 1Q), slightly higher investment in R&D and S&M, and the dilutive impact of the Reltio acquisition. FCF, however, came in above expectations at c.€3.0bn (up $27\%$ yoy).

## Guidance

More importantly, SAP updated its FY26 operating profit outlook to €11.8-12.2bn (previously €11.9-12.3bn) at constant currencies, implying growth of 13-17% (vs. 14-18% previously). This is broadly in line with GSe at c.15% at the midpoint, while consensus sits slightly above at c.16%, and reflects the dilutive impact of the Dremio and Prior Labs acquisitions that closed in July. SAP reiterated its FY26 guidance on all other metrics. Based on GSe calculations, the midpoint of the FY26 cloud growth guidance implies 2H26 cloud revenue growth of c.22%. Given the CCB strength exhibited in 1H26, we see greater visibility into 2H cloud growth, which we view as broadly de-risked given the unchanged guidance. Management, however, reiterated its expectation of a slight deceleration in CCB through the year, largely on account of macro risks. Overall, we believe the market will continue to weigh the top-line strength against operating profit headwinds and await evidence of AI product traction and monetisation over the coming quarters.

Mohammed Moawalla
+44(20)7774-1726 |
mohammed.moawalla@gs.com
GS International

Deepshikha Agarwal
+1(212)934-6961 |
deepshikha.agarwal@gs.com
GS India SPL

Uzair Merchant
+44(20)7774-7645 |
uzair.merchant@gs.com
GS International

Ahlam Haouach  
+44(20)7051-8714 |  
ahlam.haouach@gs.com  
GS International

## Further details

Key takeaways from the conference call:

■ SAP reiterated ongoing global macroeconomic uncertainty: The company noted that the fluid situation in the Middle East continues to weigh on customer decision-making, particularly in directly affected industries and supply chains.

\- CCB growth sequentially accelerated, though management continues to expect a slight deceleration exiting the year: Current cloud backlog reached almost €23bn (+26% yoy ex-fx). While the underlying trajectory remains intact and the post-SAPPHIRE pipeline is tracking better than expected, management flagged that H2, when the bulk of bookings typically occurs, carries a wider range of outcomes than usual given the volatile backdrop.

Cloud revenue growth decelerated sequentially, reflecting tough comparables and the reversal of Q1-specific effects: Management noted that Q2 2025 benefited from a strong comparable base (roughly two percentage points higher growth than Q1 2025). Despite this sequential deceleration, SaaS and PaaS combined continue to perform strongly and significantly outpace the overall market, with the indirect channel serving as a strong growth pillar.

AI and SAP Business Data Cloud were embedded in more than 90% of the 50 largest deals: SAP detailed its new Business AI platform, emphasising its ability to combine deterministic, mission-critical data with probabilistic agentic AI. The recent acquisitions of Dremio and Prior Labs will enable a semantic data layer and highly accurate tabular predictions. Crucially, management noted that this shift allows SAP to transition towards outcome- and value-based pricing for its autonomous agents, representing a significant future growth lever and supporting healthy gross margins going forward.

AI driving significant internal productivity gains: The company noted that it is seeing productivity gains of up to 30% in R&D through internal AI tool adoption and is reinforcing this by shifting the development backlog from standard SaaS features to agentic AI development. To manage rising token costs, SAP also noted that it is leveraging model-routing technologies to dynamically switch to cheaper, non-frontier LLMs for certain tasks. Consequently, SAP plans to slow hiring over the next 12 months as it balances optimised AI token consumption with headcount optimisation while maintaining its commitment to an c.80-90% expense-to-revenue ratio.

FY26 operating profit guidance trimmed to reflect the dilutive impact of recent acquisitions: The operating profit outlook was lowered to absorb the impact of the Dremio and Prior Labs acquisitions, which are expected to weigh on H2 by c.€100mn. Despite elevated R&D investments and token costs in Q2, SAP expects 2H operating profit growth yoy to be broadly similar to 1H, supported by cost containment and optimised token routing.

Exhibit 1: Actuals vs GS/Consensus
€mn, except per share data. All figures are non-IFRS

<table><tr><td>2Q FY 26 Results</td><td>Actual</td><td>GS</td><td>% Variance</td><td>Consensus</td><td>% Variance</td></tr><tr><td>Current Cloud Backlog</td><td>22,929</td><td>21,601</td><td>6%</td><td>22,110</td><td>4%</td></tr><tr><td>yoy growth</td><td>27.0%</td><td>19.7%</td><td></td><td>22.5%</td><td></td></tr><tr><td>yoy growth ex-fx</td><td>26.0%</td><td>24.8%</td><td></td><td>24.3%</td><td></td></tr><tr><td>yoy growth org ex-fx*</td><td>24.7%</td><td>23.5%</td><td></td><td></td><td></td></tr><tr><td>License revenues</td><td>131</td><td>125</td><td>5%</td><td>136</td><td>-3%</td></tr><tr><td>yoy growth</td><td>-32.5%</td><td>-35.7%</td><td></td><td>-30.1%</td><td></td></tr><tr><td>yoy growth ex-fx</td><td>-32.0%</td><td>-35.0%</td><td></td><td>-30.1%</td><td></td></tr><tr><td>Maintenance</td><td>2,439</td><td>2,429</td><td>0%</td><td>2,427</td><td>0%</td></tr><tr><td>yoy growth</td><td>-7.7%</td><td>-8.1%</td><td></td><td>-8.1%</td><td></td></tr><tr><td>yoy growth ex-fx*</td><td>-7.0%</td><td>-7.0%</td><td></td><td>-7.1%</td><td></td></tr><tr><td>Cloud revenues</td><td>6,281</td><td>6,252</td><td>0%</td><td>6,245</td><td>1%</td></tr><tr><td>yoy growth</td><td>22.4%</td><td>21.9%</td><td></td><td>21.7%</td><td></td></tr><tr><td rowspan="2">yoy growth ex-fx</td><td>24.0%</td><td>23.2%</td><td></td><td>23.5%</td><td></td></tr><tr><td>23.8%</td><td>1.4%</td><td></td><td></td><td></td></tr><tr><td>Cloud &amp; Software</td><td>8,851</td><td>8,805</td><td>1%</td><td>8,806</td><td>1%</td></tr><tr><td>yoy growth</td><td>11.1%</td><td>10.5%</td><td></td><td>10.5%</td><td></td></tr><tr><td>yoy growth ex-fx</td><td>13.0%</td><td>11.8%</td><td></td><td>12.4%</td><td></td></tr><tr><td>Total revenues</td><td>9,878</td><td>9,894</td><td>0%</td><td>9,843</td><td>0%</td></tr><tr><td>yoy growth</td><td>9.4%</td><td>9.6%</td><td></td><td>9.0%</td><td></td></tr><tr><td>yoy growth ex-fx</td><td>11.0%</td><td>10.9%</td><td></td><td>10.8%</td><td></td></tr><tr><td>Non-IFRS Cloud Gross Profit</td><td>4,687</td><td>4,685</td><td>0%</td><td>4,715</td><td>-1%</td></tr><tr><td>Non-IFRS Cloud Gross Margin</td><td>74.6%</td><td>74.9%</td><td></td><td>75.5%</td><td></td></tr><tr><td>Non-IFRS Operating Profit</td><td>3,211</td><td>3,249</td><td>-1%</td><td>3,302</td><td>-3%</td></tr><tr><td>yoy growth</td><td>3.7%</td><td>4.9%</td><td></td><td>6.6%</td><td></td></tr><tr><td>yoy growth ex-fx**</td><td>5.1%</td><td>6.3%</td><td></td><td>8.0%</td><td></td></tr><tr><td>Non-IFRS Operating Margin</td><td>32.5%</td><td>32.8%</td><td></td><td>33.5%</td><td></td></tr><tr><td>SBC</td><td>468</td><td>460</td><td>2%</td><td>417</td><td>12%</td></tr><tr><td>Non-IFRS Operating Profit incl. SBC</td><td>2,743</td><td>2,789</td><td>-2%</td><td>2,885</td><td>-5%</td></tr><tr><td>yoy growth</td><td>6.8%</td><td>8.6%</td><td></td><td>12.3%</td><td></td></tr><tr><td>yoy growth ex-fx</td><td>9.0%</td><td>10.0%</td><td></td><td>13.7%</td><td></td></tr><tr><td>Non-IFRS Operating Margin incl. SBC</td><td>27.8%</td><td>28.2%</td><td></td><td>29.3%</td><td></td></tr><tr><td>Non IFRS PF EPS incl SBC</td><td>1.59</td><td>1.73</td><td>-8%</td><td>1.73</td><td>-8%</td></tr><tr><td>yoy growth</td><td>6.9%</td><td>16.3%</td><td></td><td>16.3%</td><td></td></tr><tr><td>FCF (company definition)</td><td>3,002</td><td></td><td></td><td>2840.84</td><td>6%</td></tr><tr><td>FCF Conversion (FCF/Non-IFRS Operating Profit incl.SBC)</td><td>109%</td><td></td><td></td><td>98%</td><td></td></tr><tr><td>yoy growth</td><td>27%</td><td></td><td></td><td>21%</td><td></td></tr></table>

\* based on Gse assumption for inorganic contribution  
\* consensus Non-IFRS operating profit ex-fx % based on GSe FX impact

<table><tr><td>FY 26 Guidance vs GSe/consensus</td><td>Actual</td><td>GS</td><td>% variance</td><td>Consensus</td><td>% variance</td></tr><tr><td>Cloud revenues (€bn) (ex-fx)</td><td>€25.8bn-€26.2bn(unchanged)</td><td>26.1</td><td>0%</td><td>26.0</td><td>0%</td></tr><tr><td>yoy growth</td><td></td><td>22.4%</td><td></td><td>22.1%</td><td></td></tr><tr><td>yoy growth ex-fx</td><td>23% to 25%(unchanged)</td><td>24.0%</td><td></td><td>23.8%</td><td></td></tr><tr><td>Cloud &amp; Software (€bn) (ex-fx)</td><td>€36.3bn-€36.8bn(unchanged)</td><td>36.5</td><td>0%</td><td>36.5</td><td>0%</td></tr><tr><td>yoy growth</td><td></td><td>10.8%</td><td></td><td>10.7%</td><td></td></tr><tr><td>yoy growth ex-fx</td><td>12% to 13%(unchanged)</td><td>12.2%</td><td></td><td>12.5%</td><td></td></tr><tr><td>Non-IFRS Operating Profit incl. SBC (€bn) (ex-fx)</td><td>€11.8bn-€12.2bn(previously €11.9bn-€12.3bn)</td><td>12.0</td><td>1%</td><td>12.1</td><td>0%</td></tr><tr><td>Non-IFRS operating Margin incl. SBC</td><td></td><td>29.2%</td><td></td><td>29.7%</td><td></td></tr><tr><td>yoy growth ex-fx</td><td>13% to 17%(previously 14% to 18%)</td><td>14.8%</td><td></td><td>16.1%</td><td></td></tr><tr><td>FCF (€bn) (company definition)</td><td>c.€10bn(unchanged)</td><td>9.7</td><td>3%</td><td>9.9</td><td>1%</td></tr></table>

\*\*GS/ consensus estimate do not include SBC  
Variance at mid point calculated based on ex-fx numbers and fx impact indicated by the company in the guidance  
Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

## Price Target Risks and Methodology

We are Buy rated. Our 12m PT of €230 and our ADR PT of US\$265 are based on c.24x 2Q27-1Q28E P/E (including SBC).

Key risks to our view and price target are as follows: (1) macro risks given broad-based exposure across geographies; (2) cloud and subscription risks, such as customer churn during the transition phase, would pose downside risks to our estimates; (3) difficulty in gaining traction in S/4 HANA/cloud and not being able to draw benefits from cross-selling synergies in its installed base could cause headwinds to overall cloud growth and margins; (4) increase in opex spending would result in stronger headwinds to margins, and (5) further management changes.

<table><tr><td>SAPG.DE</td><td>12m Price Target: €230.00</td><td>Price: €128.32</td><td>Upside: 79.2%</td></tr><tr><td>SAP</td><td>12m Price Target: $265.00</td><td>Price: $146.38</td><td>Upside: 81.0%</td></tr></table>

<table><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: €149.7bn / $170.3bn</td><td>Revenue (€ mn)</td><td>36,800.0</td><td>40,329.9</td><td>45,446.3</td><td>51,528.2</td></tr><tr><td>Enterprise value:</td><td>EBIT (€ mn)</td><td>9,830.0</td><td>11,369.3</td><td>13,480.4</td><td>16,303.9</td></tr><tr><td>€147.9bn / $168.2bn</td><td>EPS (€)</td><td>6.29</td><td>7.01</td><td>8.70</td><td>10.61</td></tr><tr><td>3m ADTV: €415.4mn / $480.6mn</td><td>EV/sales (X)</td><td>7.8</td><td>3.6</td><td>3.0</td><td>2.5</td></tr><tr><td>Germany</td><td>EV/EBITDA (X)</td><td>25.6</td><td>11.6</td><td>9.3</td><td>7.2</td></tr><tr><td>Europe Technology</td><td>P/E (X)</td><td>38.6</td><td>18.3</td><td>14.7</td><td>12.1</td></tr><tr><td>M&amp;A Rank: 3</td><td>FCF yield (%)</td><td>2.9</td><td>6.7</td><td>8.0</td><td>9.5</td></tr><tr><td>Leases incl. in net debt &amp; EV?: No</td><td>Org. sales grth (%)</td><td>10.1</td><td>10.6</td><td>12.1</td><td>13.4</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (€)</td><td>1.66</td><td>1.66</td><td>1.78</td><td>1.91</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 23 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Mohammed Moawalla, Deepshikha Agarwal, Uzair Merchant and Ahlam Haouach, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Mohammed Moawalla GS International, Deepshikha Agarwal GS India SPL, Uzair Merchant GS International, Ahlam Haouach GS International.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for SAP is/are relative to the other companies in its/their coverage universe: Adyen NV, Capgemini, Dassault Systemes, Indra, Nemetschek, Nexi, Ovh Groupe, SAP, SECO, Sage Group, Sinch AB, TeamViewer, Temenos, TietoEVRY, Wise Group, Worldline

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: SAP (€128.32) and SAP (\$146.38)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: SAP (€128.32) and SAP (\$146.38)

GS has received compensation for non-investment banking services during the past 12 months: SAP (€128.32) and SAP (\$146.38)

GS had an investment banking services client relationship during the past 12 months with: SAP (€128.32) and SAP (\$146.38)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: SAP (€128.32) and SAP (\$146.38)

GS had a non-securities services client relationship during the past 12 months with: SAP (€

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for

equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
