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
# Global Economics Comment: Spending Headwinds Still to Come on Both Sides of the Pond

The interim US-Iran peace deal has diminished upside tail risks to energy prices: our oil strategists now see Brent declining to \$80 per barrel in 2026Q4 (vs. \$90 previously) and our gas strategists also forecast slightly lower near-term prices (although they leave their year-end forecasts unchanged). Moreover, consumer spending has so far held up reasonably well on both sides of the Atlantic since the start of the conflict. While these are both welcome developments for the growth outlook, we see three reasons why it is too early for complacency on real income and consumer spending in the coming months.

First, while gasoline prices jumped shortly after the start of the war (and may ease following the recent interim deal), the passthrough from wholesale gas and electricity prices to consumers is more drawn out. Second, seasonal spending patterns should amplify the hit to income this winter when energy demand peaks, especially in Europe. Lastly, while outsized tax refunds dampened the real income hit in the US this spring, this temporary boost is now behind us and we expect real cash flow to stagnate on a year-on-year basis in H2.

Based on historical statistical relationships, we estimate that each $1\%$ pullback in real cash flow from an energy shock results in a $0.6\%$ decline in consumer spending after two quarters. Our model is able to explain the limited consumption impact of higher energy prices so far but projects more meaningful weakness in H2, even with our new energy price forecasts. These predictions align with consumer surveys that show DM consumers anticipate making fewer large purchases over the next 6-12 months.

## Spending Headwinds Still to Come on Both Sides of the Pond

The interim US-Iran peace deal has diminished upside tail risks to energy prices: our oil strategists now see Brent declining to \$80 per barrel in 2026Q4 (vs. \$90 previously) and our gas strategists also forecast slightly lower near-term prices (although they leave their year-end forecasts unchanged due to inventory rebuilding). Moreover, consumer spending has so far held up reasonably well on both sides of the Atlantic since the start of the conflict (Exhibit 1). While these are both welcome developments for the growth outlook, we see three reasons why it is too early for complacency on real income and consumer spending.

## Megan Peters

+44(20)7051-2058

megan.l.peters@gs.com

GS International

Exhibit 1: Consumer Spending Has Held Up So Far Despite the Surge in Energy Prices  
![](images/e30d26ce365828d6f4add76928e03604ac57dd1ec0bf7c967feab347b4b6baf1.jpg)

<details>
<summary>line chart</summary>

| Date   | US    | Euro Area |
|--------|-------|-----------|
| Jan-25 | 101.5 | 103.5     |
| May-25 | 98.5  | 98.0      |
| Sep-25 | 100.5 | 99.0      |
| Jan-26 | 101.0 | 100.0     |
| May-26 | 117.5 | 110.5     |
</details>

![](images/2e2173e3bdfaae5d9e3725356535b9c9a3a3a048c16864a8ed6680e0e02116dc.jpg)

<details>
<summary>line chart</summary>

| Date   | US    | Euro Area |
|--------|-------|-----------|
| Jan-25 | 99.0  | 98.8      |
| May-25 | 99.5  | 99.7      |
| Sep-25 | 100.8 | 100.4     |
| Jan-26 | 101.4 | 101.0     |
| May-26 | 101.8 | 101.3     |
</details>

Source: Haver Analytics, GS Global Investment Research

First, while gasoline prices have already risen sharply, the increase in natural gas and electricity prices has been more limited so far. Our commodity strategists expect further price increases as countries build stocks ahead of next winter (especially as China begins rebuilding inventories after destocking this spring) while our European economists highlight that fixed contracts and government regulations have historically led to more gradual price increases relative to wholesale prices. As a result, a large share of the relevant consumer price increases has yet to be realized.

Second, seasonal energy demand will amplify the hits to actual cash flow this winter (particularly in Europe) beyond what official seasonally adjusted income measures will suggest.

In Exhibit 2, we use the changes in our country teams' energy price forecasts since the onset of the conflict—which incorporate our commodities strategists' latest forecast downgrades—to estimate how rising energy prices will affect realized cash flow after correcting for seasonal swings in nominal spending. To separate the price and seasonal demand channels, we first calculate the implied hit under fixed consumption shares (the darker-coloured bars) and then recalculate the impulse allowing for typical seasonal demand fluctuations. The difference between these two estimates captures the seasonal effect (the lighter-coloured bars).

Accounting for higher winter demand implies a more backloaded impulse in Europe, with the trough shifting to early 2027 compared to mid-2026 under fixed consumption shares. While higher prices account for most of the hit to cash flow, seasonal demand poses a meaningful incremental drag in winter: in 2027Q1 it lowers real incomes by a further 14bp in Europe (over $20\%$ of the combined impulse) and by 5bp in the US (around $10\%$ of the total drag).

Exhibit 2: We Expect Backloaded Cash Flow Headwinds from Gas Price Increases in Europe  
Real Cashflow Hit from Energy Price Increases  
![](images/7e354ad67d979b8242e5fa99d54d823fab0bf60e68ce3240861ac23729fc968a.jpg)

<details>
<summary>stacked bar chart</summary>

| Quarter | US Gasoline (%) | US Household Energy (%) | Total (%) |
| :--- | :--- | :--- | :--- |
| Q1 | -0.08 | -0.13 | -0.15 |
| Q2 | 0.03 | -0.64 | -0.59 |
| Q3 | 0.04 | -0.45 | -0.51 |
| Q4 | -0.03 | -0.41 | -0.52 |
| 2026 Q1 | 0.01 | -0.59 | -0.58 |
| 2027 Q1 | 0.02 | -0.41 | -0.58 |
| 2027 Q2 | 0.03 | -0.41 | -0.51 |
| 2027 Q3 | 0.06 | -0.36 | -0.49 |
| 2027 Q4 | 0.01 | -0.43 | -0.53 |
</details>

![](images/dbaae5ab5053e8c36d90b1bbdccf3af7c00dd18cd04b8909982125777a88ee58.jpg)

<details>
<summary>stacked bar chart</summary>

| Quarter | Total (Percent) | Household Energy (Percent) | Gasoline (Percent) |
|---|---|---|---|
| Q1 2026 | -0.18 | -0.12 | -0.15 |
| Q2 2026 | -0.58 | -0.49 | -0.73 |
| Q3 2026 | -0.45 | -0.43 | -0.68 |
| Q4 2026 | -0.56 | -0.37 | -0.59 |
| Q1 2027 | -0.68 | -0.33 | -0.49 |
| Q2 2027 | -0.41 | -0.31 | -0.45 |
| Q3 2027 | -0.27 | -0.35 | -0.39 |
| Q4 2027 | -0.31 | -0.25 | -0.34 |
The chart displays two vertical bars for 'Euro Area' and 'Euro Area' on the left, each labeled 'Percent', but the right shows the same Y-axis label 'Percent'. The legend indicates 'Total' represented by black diamonds.
</details>

![](images/99ef820941238e754f9eb5f8021f56bc57fbc61d1e552387fddcc723a801ac66.jpg)

<details>
<summary>stacked bar chart</summary>

| Quarter | Canada Gasoline (%) | Canada Household Energy (%) | Total (%) |
|---|---|---|---|
| Q1 | -0.15 | -0.05 | -0.22 |
| Q2 | 0.03 | -0.08 | -0.79 |
| Q3 | 0.02 | -0.09 | -0.88 |
| Q4 | -0.65 | -0.06 | -0.71 |
| Q1 | 0.01 | -0.06 | -0.68 |
| Q2 | 0.03 | -0.06 | -0.61 |
| Q3 | 0.02 | -0.05 | -0.61 |
| Q4 | -0.65 | -0.05 | -0.61 |
</details>

![](images/71a6b2218113bbdcc9795f077bc48eacfe099fb6e9702e4592ceb70f5771144c.jpg)

<details>
<summary>stacked bar chart</summary>

| Quarter | Total (Percent) | Household Energy (Percent) | Gasoline (Percent) |
|---|---|---|---|
| Q1 | -0.08 | 0.01 | -0.05 |
| Q2 | -0.48 | -0.35 | -0.65 |
| Q3 | -0.4 | -0.3 | -0.6 |
| Q4 | -0.45 | -0.25 | -0.55 |
| Q1 | -0.18 | 0.04 | -0.25 |
| Q2 | -0.13 | -0.2 | -0.65 |
| Q3 | -0.13 | -0.18 | -0.45 |
| Q4 | -0.1 | -0.15 | -0.35 |
The chart displays two vertical bars for 'UK' and 'Percent', likely representing different time periods or categories. The 'Total' series is marked by black diamonds on each bar.
</details>

Note: Lighter bars indicate seasonal demand effects.  
Source: GS Global Investment Research

Third, in the US, larger-than-usual tax refunds in the first half of this year temporarily boosted real cash flow by $0.8\%$ in Q1 and $1.2\%$ in Q2. But this boost should reverse in H2 now that tax refunds have been fully paid out, with year-over-growth growth set to temporarily turn negative in Q3 (Exhibit 3). Combining this impulse with the energy price drag in Exhibit 2 implies a sharp swing from a $0.7\%$ boost to real cash flows in Q2 to a drag of $0.6\%$ in Q3.

Exhibit 3: In the US, Larger Tax Refunds Boosted Real Cash Flow by $0.8\%$ in Q1 and $1.2\%$ in Q2  
![](images/02a3c4257e024f6ad462ef507e91076d1b0536e5e1e3b8e9836549575156ed06.jpg)

<details>
<summary>bar-line hybrid</summary>

| Month | Real Disposable Personal Income (Percent, year ago) | Real Disposable Personal Cash Flow* (Percent, year ago) | Effect of 2026 Tax Cuts on Personal Cash Flow (Percent of Personal Income) | Effect of 2026 Tax Cuts on Personal Cash Flow (Billions of Dollars) |
|---|---|---|---|---|
| Jan | 1.85 | 0.5 | -0.5 | 10 |
| Feb | 1.8 | 1.65 | 35 | 10 |
| Mar | 1.05 | 0.55 | -0.5 | 10 |
| Apr | 0.7 | 3.25 | 70 | 10 |
| May | 0.05 | 0.55 | -0.5 | 10 |
| Jun | -0.05 | -0.4 | -0.9 | 0 |
| Jul | 0.0 | 0.0 | 0.0 | 0 |
| Aug | 0.0 | 0.0 | 0.0 | 0 |
| Sep | 0.0 | 0.0 | 0.0 | 0 |
| Oct | 0.0 | 0.0 | 0.0 | 0 |
| Nov | 0.0 | 0.0 | 0.0 | 0 |
| Dec | 0.85 | 0.35 | 35 | 10 |
</details>

Source: Department of Commerce, GS Global Investment Research

We estimate that each $1\%$ decline in real income due to an energy shock has historically lowered the level of spending by around $0.6\%$ after 2 quarters. Applying this estimate to the cash flow headwinds in Exhibits 2 and 3 implies a peak drag on real spending of $0.5\%$ in Canada, $0.4\%$ in the Euro area, and $0.3\%$ in the US and UK (left chart, Exhibit 4). Our estimated spending impulses imply that spending headwinds are yet to materialize in the US, while only around half of the peak spending hit will be realized in the Euro area, UK and Canada by the end of Q2.

Forward-looking survey evidence also suggests that spending headwinds lie ahead. Most DM consumers anticipate making fewer large purchases over the next 6-12 months than they did before the onset of the war (right chart, Exhibit 4). And while US spending intentions picked up notably this spring on the back of fiscal support, they pulled back in May (consistent with our US economists' estimate that consumers cut back disproportionately on discretionary durable goods in response to an energy shock).

Exhibit 4: We Estimate that the Spending Drag is Yet to Materialize in the US, While Only Half of the Peak Drag Has Been Realized in the Euro Area; Consumer Spending Intentions Also Suggest Further Spending Drags Remain in the Pipeline  
![](images/5169b274566b39c13f632711c03308ef6ceaa3cb24c55bb241816f32e818b702.jpg)

<details>
<summary>line chart</summary>

Effect of Energy Prices and Fiscal Transfers on Real Spending
| Quarter | US (%) | Euro Area (%) | Canada (%) | UK (%) |
|---|---|---|---|---|
| Q1 2026 | 0.2 | -0.05 | -0.05 | -0.02 |
| Q2 2026 | 0.43 | -0.18 | -0.35 | -0.1 |
| Q3 2026 | 0.1 | -0.3 | -0.5 | -0.25 |
| Q4 2026 | -0.3 | -0.3 | -0.5 | -0.25 |
| Q1 2027 | -0.35 | -0.35 | -0.4 | -0.15 |
| Q2 2027 | -0.35 | -0.35 | -0.35 | -0.1 |
| Q3 2027 | -0.3 | -0.2 | -0.35 | -0.05 |
| Q4 2027 | -0.3 | -0.15 | -0.35 | -0.05 |
</details>

![](images/c45f0bb2661871777b1d07586579f14ff7e0a52e5067cf5e77a22a52cfa25304.jpg)

<details>
<summary>bar chart</summary>

| Country | March 2026 - May 2026 avg. | May 2026 |
|---------|-----------------------------|----------|
| US      | 1.1                         | 0.3      |
| Italy   | 0.0                         | 0.1      |
| UK      | -0.4                        | -0.2     |
| Germany | -0.4                        | -0.4     |
| Portugal| -0.5                        | -0.7     |
| France  | -0.7                        | -1.1     |
</details>

Source: Haver Analytics, GS Global Investment Research

Taken together, drawn-out energy passthrough, winter heating fuel demand, and the reversing US fiscal boost suggest spending headwinds remain in the pipeline despite the resilience of spending data so far.

## Megan Peters

## The Global Economics Team

## Jan Hatzius

+1(212)902-0394

jan.hatzius@gs.com

GS & Co. LLC

## Joseph Briggs

+1(212)902-2163

joseph.briggs@gs.com

GS & Co. LLC

## Sarah Dong

+1(212)357-9741

sarah.dong@gs.com

GS & Co. LLC

## Megan Peters

+44(20)7051-2058

megan.l.peters@gs.com

GS International

## Disclosure Appendix

## Reg AC

I, Megan Peters, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Megan Peters GS International.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. 

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
