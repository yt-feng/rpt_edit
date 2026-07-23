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
# EUROPEAN ECONOMICS ANALYST

# Euro Area—Higher Energy Prices Undo Recent Inflation Progress

The outlook for inflation in the Euro area is caught between opposing forces. On the one hand, the incoming inflation data has been weaker in Europe and globally, and price surveys have started to cool. On the other hand, the resumption of military conflict in the Middle East and Russian refinery outages have driven sharp increases in the prices of crude oil, oil products, and natural gas.

Alexandre Stott
+33(1)4212-1108 |
alexandre.stott@gs.com
GS Bank Europe SE - Paris Branch

We study the transmission of energy shocks along the inflation pipeline with a new statistical model (a large Bayesian Vector Auto-Regression). Our model jointly considers 19 variables such as producer price indices, shorter-term inflation expectations, consumer price inflation, and wage growth. This approach is similar to that used by central banks, including the ECB.

\- Our model confirms that energy shocks usually have instantaneous and direct effects on consumer and producer energy prices. These effects then gradually appear in cost indicators, measures of shorter-term inflation expectations, and indirectly affected consumer prices, and can eventually lead to second-round effects on wage growth and longer-term inflation expectations.

Our results show that direct effects were initially very strong in March, that some indirect effects had built up by April but faded by June, and that there were no convincing signs of second-round effects throughout.

Our estimates suggest that, with the softer price data and energy forwards at their late-June lows, inflation had appeared on track to undershoot the ECB staff projections by 0.4pp for headline and around 0.2pp for core. However, the subsequent increase in energy prices has since brought our model's forecast for the inflation peak back in line with the staff's baseline. Our analysis therefore suggests that the renewed increase in energy prices has broadly undone the recent progress seen in price surveys and the inflation data.

As a result, we continue to expect the Governing Council to hike a second time at its September meeting. While our base case is that the ECB then remains on hold, the risks are skewed towards further tightening if persistently higher energy prices cause the inflation outlook to deteriorate further.

## Euro Area—Higher Energy Prices Undo Recent Inflation Progress

The outlook for inflation in the Euro area is caught between opposing forces. On the one hand, the incoming inflation data has been weaker in Europe and globally, and price surveys—such as the PMIs and the European Commission’s—have started to cool. On the other hand, the resumption of military conflict in the Middle East and Russian refinery outages have driven renewed increases in the prices of crude oil, oil products, and natural gas (Exhibit 1).

Exhibit 1: Europe Is Facing Renewed Energy Price Pressures  
![](images/eb19480c4257cc04f541ed9a15c398813294ab972ac98dbe78779f0f540fe06a.jpg)  
Source: GS Global Investment Research, Haver Analytics

Keeping precise track of the inflation pressures in the pipeline is a difficult task. Our preferred approach for studying large and complex datasets of this kind is to use a Bayesian Vector Auto-Regressive (BVAR) model. The auto-regressive structure allows for rich dynamics between variables, while the Bayesian estimation approach improves the stability of the results.

We jointly model the 19 variables listed in Exhibit 2. These either relate to the energy shock, are price indicators subject to direct, indirect, or second-round effects, or serve as macroeconomic controls. Most of the price variables are expressed in seasonally adjusted, month-over-month terms and are observed through May or June. We include six lags of each variable, and the sample begins in 2003.

Exhibit 2: We Use a Bayesian Vector Auto-Regression to Jointly Model 19 Variables

<table><tr><td>Variable</td><td>Unit</td><td>Seasonally Adjusted</td><td>Last Observation</td><td>Category</td></tr><tr><td>World Oil Production</td><td>Percent, mom</td><td>No</td><td>July</td><td>Shock</td></tr><tr><td>Brent Oil Price</td><td>Percent, mom</td><td>No</td><td>July</td><td>Shock</td></tr><tr><td>TTF Natural Gas Price</td><td>Percent, mom</td><td>No</td><td>July</td><td>Shock</td></tr><tr><td>European Diesel Prices</td><td>Percent, mom</td><td>No</td><td>July</td><td>Shock</td></tr><tr><td>HICP Energy</td><td>Percent, mom</td><td>Yes</td><td>June</td><td>Direct</td></tr><tr><td>PPI Energy</td><td>Percent, mom</td><td>Yes</td><td>May</td><td>Direct</td></tr><tr><td>Farm Gate Prices</td><td>Percent, mom</td><td>No</td><td>June</td><td>Indirect</td></tr><tr><td>PPI Intermediate</td><td>Percent, mom</td><td>Yes</td><td>May</td><td>Indirect</td></tr><tr><td>PMI Composite Input Prices</td><td>Level</td><td>No</td><td>June</td><td>Indirect</td></tr><tr><td>12m Consumer Inflation Expectations</td><td>Level</td><td>No</td><td>June</td><td>Indirect</td></tr><tr><td>HICP NEIG</td><td>Percent, mom</td><td>Yes</td><td>June</td><td>Indirect</td></tr><tr><td>PMI Composite Output Prices</td><td>Level</td><td>No</td><td>June</td><td>Indirect</td></tr><tr><td>HICP Food</td><td>Percent, mom</td><td>No</td><td>June</td><td>Indirect</td></tr><tr><td>7q Mean Inflation Forecast</td><td>Percent, yoy</td><td>No</td><td>Q2</td><td>Second-round</td></tr><tr><td>Negotiated Wages</td><td>Percent, yoy</td><td>No</td><td>March</td><td>Second-round</td></tr><tr><td>HICP Services</td><td>Percent, mom</td><td>Yes</td><td>June</td><td>Second-round</td></tr><tr><td>PMI Composite Output</td><td>Index</td><td>No</td><td>June</td><td>Control</td></tr><tr><td>Unemployment Gap</td><td>Percentage Points</td><td>No</td><td>May</td><td>Control</td></tr><tr><td>Global Supply Chain Pressure Index</td><td>Index</td><td>No</td><td>June</td><td>Control</td></tr></table>

Source: GS Global Investment Research

We can visualise our model with a heatmap (similar to the one ECB Chief Economist Lane presented in a recent speech) showing the average strength and delay with which price indicators have historically responded to oil supply, gas price, and diesel price shocks (Exhibit 3). The variables are ordered from most upstream at the top to most downstream at the bottom; the time elapsed since the shock increases from left to right; and the colour gradient indicates the strength of the response.

Our estimates confirm that energy shocks have instantaneous and direct effects on consumer and producer energy prices. These effects then gradually appear in cost indicators, measures of shorter-term inflation expectations, and indirectly affected consumer prices, and can eventually lead to second-round effects on wage growth and longer-term inflation expectations.

Exhibit 3: We Can Visualise Our Model With a Heatmap  
![](images/500ff3ee2034a30bc4bac8b53d327b124abe9871563b8b3267049cf55ba49f4d.jpg)

The heatmap shows the standardised response of price indicators to the oil supply shock, gas price shock, and diesel price shock identified in March 2026. We use sign restriction on oil production and oil prices to identify oil supply shocks, and zero sign restrictions for gas price and and diesel price shocks. Response at-or-above one standard deviations are shown with the darkest shade of red, while zero and negative responses are shown in white.

## Source: GS Global Investment Research

We next use our model to ask how price variables would have evolved in the absence of war in the Middle East (obtained from the model's forecast before March) and if they had responded to the observed changes in oil production, as well as oil, gas, and diesel prices, in line with their historical behaviour.

We find that some price surveys (such as the European Commission's measure of shorter-term inflation expectations) initially reacted more strongly than usual but have since June returned in line with our model's prediction (Exhibit 4, left). In contrast, our model suggests that the response of non-energy industrial (or core) goods inflation has so far been more muted than in the past and no longer looks different from the no-war counterfactual (Exhibit 4, right).

Exhibit 4: The Response of Core Goods Inflation to Higher Energy Prices Has Been More Muted than Usual

![](images/292128651e661d7907334c1f935e384b8846b7b72ad7e0e784398eff65c1d65e.jpg)

![](images/c1bca7417a727de6bf1819ba0a5e5102ba1c0dba07b2e61b8929a99989967584.jpg)  
The no-war counterfactual is the model's unconditional forecast using realised data until February 2026. The path predicted by the energy shock is the model's forecast conditional on the realised data for oil production, oil prices, gas prices, and diesel prices between March and June 2026.  
Source: GS Global Investment Research, Haver Analytics

The difference between the realised data and our model's no-war counterfactual can be interpreted as a measure of the strength of direct, indirect, or second-round effects, depending on the variable considered. We standardise this difference for every variable and plot the values as dots between March and June, with dashes indicating the average by type of effect (Exhibit 5).

Our results show that direct effects were initially very strong in March, that some indirect effects had built up by April but faded by June, and that there were no convincing signs of second-round effects throughout.

Of course, the model itself would suggest that it is simply too early to detect signs of second-round effects at this stage. But in the case of wage growth, for instance, the decrease in one-year-ahead wage growth expectations reported by small and medium-sized firms in the ECB's SAFE survey is consistent with the absence of second-round effects so far.

Exhibit 5: Our Model Finds No Convincing Signs of Second-Round Effects So Far  
![](images/4710ca7079e7b5adfa8a4f85ee2b99d3a5d5099fe6a74e39f80a225aee87b295.jpg)  
Source: GS Global Investment Research

Finally, we use our model to quantify the effect of higher energy prices on the inflation outlook. To do so, we first condition the model's forecast on energy forwards at their late-June lows (the light blue dashed lines in Exhibit 6) and then repeat the exercise with energy forwards at their current levels (dark blue).

Exhibit 6: We Condition Our Model's Forecast on Energy Forwards at Their Late-June Lows and at Their Current Levels  
![](images/321ecd74ddee71e90bde8d75623caea212f3f4b9ad97edba578bacd0d315d940.jpg)

![](images/3a626c95bfc8b9b4cbe8d69e28edf277b21b9b989f7593bb66a1fac7d427904c.jpg)  
Source: Data compiled by GS Global Investment Research, Haver Analytics

The results for headline and core inflation are shown in Exhibit 7, with the June ECB staff projections included for comparison. Initially, with the softer price data and energy forwards at their lows, inflation appeared on track to undershoot the ECB staff projections by 0.4pp for headline and around 0.2pp for core. However, the subsequent increase in energy prices has brought our model's forecast for the inflation peak back in line with the staff's baseline.

## Exhibit 7: The Increase in Energy Prices Has Brought Our Model's Forecast Back in Line With the ECB Staff Projections

![](images/40dbcaa944fab2969c7e968992d7a6358b0a3bd08c36ace6f8f23cfc9df245ad.jpg)  
The conditional forecasts use oil and gas price forwards from July and August 2026 until the end of 2027, while oil production and diesel prices evolve in line with the model.  
Source: GS Global Investment Research, Haver Analytics, ECB

Our analysis therefore suggests that the renewed increase in energy prices has broadly undone the recent progress seen in price surveys and the inflation data. As a result, we continue to expect the Governing Council to hike a second time at the September meeting. While our base case is that the ECB then remains on hold, the risks are skewed towards further tightening if persistently higher energy prices cause the inflation outlook to deteriorate further.

## Alexandre Stott

## The European Economics Team

Sven Jari Stehn  
+44(20)7774-8061  
jari.stehn@gs.com  
GS International

## James Moberly

+44(20)7774-9444

james.r.moberly@gs.com

GS International

## Giovanni Pierdomenico

+44(20)7051-6807

giovanni.pierdomenico@gs.com

GS International

Filippo Taddei  
+44(20)7774-5458  
filippo.taddei@gs.com  
GS International

Niklas Garnadt
+49(69)7532-1537
niklas.garnadt@gs.com
GS Bank Europe SE

Alexandre Stott  
+33(1)4212-1108  
alexandre.stott@gs.com  
GS Bank Europe SE - Paris Branch

Katya Vashkinskaya +44(20)7774-4833  
katya.vashkinskaya@gs.com  
GS International

## Disclosure Appendix

## Reg AC

I, Alexandre Stott, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Alexandre Stott GS Bank Europe SE - Paris Branch.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
