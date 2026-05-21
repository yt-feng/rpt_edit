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
# Japan: April Trade: Crude Oil Import Unit Price Surges while Import Volume Plunges. Stable LNG Import Price

BOTTOM LINE: April export volume maintained a similar pace of increase as the January-March average, at +3.4% yoy (+3.6% in Jan-Mar). However, on a seasonally adjusted mom basis (our calculation), volume declined by -2.9% in April (Jan-Mar quarter: +3.9% qoq). Regarding crude oil imports, the import unit price in yen terms rose by 57% in April compared to February, before the Middle East conflict, while import volume decreased by 63.7% yoy. Meanwhile, natural gas imports also decreased by 20.6% yoy, but the unit price in yen terms rose by only 4% compared to February.

# JP MAP:

Export value growth: +16 (relevance: 4; surprise: +4)

# KEY NUMBERS:

Trade Balance: April: +¥301.9 bn vs. GS forecast: -¥71.5 bn, BBG consensus: -¥72.5 bn, April 2025: -¥149.5 bn   
- Export Value (yoy): April: +14.8% vs. GS forecast: +10.0%, BBG consensus: +9.0%, March: +11.5%   
- Import Value (yoy): April: +9.7% vs. GS forecast: +9.0%, BBG consensus: +8.5%, March: +10.9%   
■ Export Volume (yoy): April: +3.4%, March: +3.6%,   
■ Import Volume (yoy): April: -3.4%, March: +2.4%

# MAIN POINTS:

Trade data for April show that export value posted double-digit growth for the second consecutive month, at +14.8% yoy. Import value maintained a similar pace of increase to March (+10.9%), at +9.7% yoy. As a result, the trade balance swung to a surplus of +¥301.9 bn, from a small deficit of -¥149.5 bn in April of last year.

Export volume maintained a similar pace of increase in April as the January-March average of +3.6%, at +3.4% yoy. However, on a seasonally adjusted mom basis (our calculation), volume declined by -2.9% mom in April (Jan-Mar quarter: +3.9% qoq). While export volume to the US and Europe increased sharply yoy, exports to Asia slowed.

Regarding crude oil imports, a point of concern since the worsening of the situation in the Middle East, the unit price calculated from import value and volume had not yet risen significantly as of March. However, prices rose sharply in April to ¥16,121/bl

Yuriko Tanaka

+81(3)4587-9964

yuriko.tanaka@gs.com

GS Japan Co., Ltd.

(March: ¥10,763/bl), or US\$101.4/bl (March: US\$68.7/bl) in US dollar terms. This represents a sharp rise of +57% and +54%, respectively, compared to February (pre-conflict). On a yoy basis, prices turned to an increase of +38% and +28% (they were down -10% yoy in March). Crude oil import volume dropped by -63.7% yoy.

On the other hand, the import unit price for natural gas rose by only 4% from February to ¥1,829/mmbtu, and in dollar terms, rose by only 2% to US\$11.5/mmbtu from US\$11.3 in February. Import volume was 4269 thousand tons in total, and decreased by -20.6% yoy. While natural gas imports from the Middle East decreased by 76% yoy to 139 thousand tons, imports from Russia increased by 30% yoy to 456 thousand tons.

Exhibit 1: Exports, Imports and Trade Balance   
![](images/a2cab23c9365cc6b49f99254150c1d20cb1235e44d79f6db5acf882b3d139f0e.jpg)

<details>
<summary>line</summary>

| Year | Trade Balance (RHS) | Export Value (LHS) | Imports Value (LHS) |
|------|---------------------|--------------------|---------------------|
| 2018 | -10                 | 5                  | 10                  |
| 2019 | -5                  | 0                  | 5                   |
| 2020 | -15                 | -10                | -5                  |
| 2021 | -20                 | 50                 | 30                  |
| 2022 | -30                 | 20                 | 40                  |
| 2023 | -40                 | 10                 | 50                  |
| 2024 | -35                 | 5                  | 10                  |
| Apr-2026 | -25              | 15                 | 10                  |
</details>

Source: Ministry of Finance

Exhibit 2: Export Volume by Region (Seasonally Adjusted Level)   
![](images/1b8d6929eed24905ba7465c081678c2ea92b77ff2e9544cafea79d67689a59c5.jpg)

<details>
<summary>line</summary>

| Year | Export volume overall | US   | EU   | China |
|------|------------------------|------|------|-------|
| 2018 | ~120                   | ~125 | ~130 | ~105  |
| 2019 | ~115                   | ~128 | ~132 | ~98   |
| 2020 | ~80                    | ~65  | ~110 | ~90   |
| 2021 | ~110                   | ~115 | ~125 | ~105  |
| 2022 | ~105                   | ~110 | ~120 | ~95   |
| 2023 | ~100                   | ~105 | ~115 | ~85   |
| 2024 | ~105                   | ~130 | ~125 | ~80   |
| 2025 | ~100                   | ~125 | ~110 | ~75   |
| 2026 | ~105                   | ~130 | ~115 | ~70   |
</details>

Source: MOF

Exhibit 3: Japan's Imported Crude Oil and LNG Volume   
![](images/edbb461482695b9ca37db4278f42a6da1ab9fd76960925b70832d48d76f67f7c.jpg)

<details>
<summary>line</summary>

| Year | Japan's imported crude oil volume (lhs) (million KL) | Japan's imported LNG volume (rhs) (million Tons) |
|------|--------------------------------------------------------|--------------------------------------------------|
| 2022 | ~13.5                                                  | ~7.0                                             |
| 2023 | ~15.0                                                  | ~6.5                                             |
| 2024 | ~12.0                                                  | ~5.5                                             |
| 2025 | ~14.0                                                  | ~6.0                                             |
| Apr 2026 | ~4.0                                               | ~1.0                                             |
</details>

Source: MOF

Exhibit 4: Japan's Imported Oil Price and Dubai Oil Price   
![](images/794d49ade532c426d6d2a9bed1f6fc824f8f5e6245b778b175bb3f1d77a0e4ec.jpg)

<details>
<summary>line</summary>

| Year | Japan's imported crude oil price (USD per barrel) | Dubai crude oil price (USD per barrel) |
|------|--------------------------------------------------|----------------------------------------|
| 2020 | ~70                                              | ~65                                    |
| 2021 | ~45                                              | ~40                                    |
| 2022 | ~85                                              | ~80                                    |
| 2023 | ~115                                             | ~110                                   |
| 2024 | ~90                                              | ~85                                    |
| 2025 | ~75                                              | ~70                                    |
| 2026 | ~105                                             | ~130                                   |
</details>

Source: MOF, Datastream, Data compiled by GS Global Investment Research

Exhibit 5: Japan's Imported LNG Price and JMK LNG Price   
![](images/defd136fcd1e7e16502de330d77fe5ccb6bc5894eaf5cc752898a99a845c6b31.jpg)

<details>
<summary>line</summary>

| Year | Japan's imported LNG price (USD/mmbtu) | JMK LNG price (USD/mmbtu) |
|------|------------------------------------------|---------------------------|
| 2020 | ~10                                      | -                         |
| 2021 | ~8                                       | -                         |
| 2022 | ~15                                      | -                         |
| 2023 | ~20                                      | ~55                       |
| 2024 | ~13                                      | ~15                       |
| 2025 | ~12                                      | ~13                       |
| 2026 | ~11                                      | ~18                       |
</details>

Source: MOF, Bloomberg, Data compiled by GS Global Investment Research

# The Japan Economics Team

# Akira Otani

+81(3)4587-9960

akira.otani@gs.com

GS Japan Co., Ltd.

# Tomohiro Ota

+81(3)4587-9984

tomohiro.ota@gs.com

GS Japan Co., Ltd.

# Yuriko Tanaka

+81(3)4587-9964

yuriko.tanaka@gs.com

GS Japan Co., Ltd.

# Disclosure Appendix

# Reg AC

I, Yuriko Tanaka, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yuriko Tanaka GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

# Disclosures

# Regulatory disclosures

# Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

# Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annual audit compliance report can be found at this link: https://publishing.gs.com/content/site/india-annual-compliance-report.html. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no responsibility for any investment decisions that may be taken by a client or any other person based on this research report. Singapore: GS (Singapore) Pte. (Company Number: 198602165W), which is regulated by the Monetary Authority of Singapore, accepts legal responsibility for this research, and should be contacted with respect to any matters arising from, or in connection with, this research. Taiwan: This material is for reference only and must not be reprinted without permission. Investors should carefully consider their own investment risk. Investment results are the responsibility of the individual investor. United Kingdom: Persons who would be categorized as retail clients in the United Kingdom, as such term is defined in the rules of the Financial Conduct Authority, should read this research in conjunction with prior GS on the covered

companies referred to herein and should refer to the risk warnings that have been sent to them by GS International. A copy of these risks warnings, and a glossary of certain financial terms used in this report, are available from GS International on request.

European Union and United Kingdom: Disclosure information in relation to Article 6 (2) of the European Commission Delegated Regulation (EU) (2016/958) supplementing Regulation (EU) No 596/2014 of the European Parliament and of the Council (including as that Delegated Regulation is implemented into United Kingdom domestic law and regulation following the United Kingdom's departure from the European Union and the European Economic Area) with regard to regulatory technical standards for the technical arrangements for objective presentation of investment recommendations or other information recommending or suggesting an investment strategy and for disclosure of particular interests or indications of conflicts of interest is available at https://www.gs.com/disclosures/europeanpolicy.html which states the European Policy for Managing Conflicts of Interest in Connection with Investment Research.

Japan: GS Japan Co., Ltd. is a Financial Instrument Dealer registered with the Kanto Financial Bureau under registration number Kinsho 69, and a member of Japan Securities Dealers Association, Financial Futures A

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

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

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
