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
## GS China Econ Proprietary Indicators: July

Please find an update on our proprietary economic indicators below. The data behind our proprietary economic indicators can be downloaded here (methodology notes available in the appendix).

Chelsea Song
+852-2978-0106 |
chelsea.song@gs.com
GS (Asia) L.L.C.

## GS Proprietary Economic Indicators

Exhibit 1: Our China Current Activity Indicator (CAI) rose to +5.3% mom annualized sa in June, vs. +4.2% in May

![](images/5c9c3a554f331b8ababda5aae93e798ef752dbd8417133712dbdeac4a1326e9a.jpg)  
Source: GS Global Investment Research, NBS, CEIC

Exhibit 2: June's improvement in CAI was driven by manufacturing and consumption  
![](images/60c9964f59deb52216d7ad8f2ba220cc6fa5e5a2543ef0e5a6ae93a0c3fd3fdb.jpg)  
Source: GS Global Investment Research, NBS, CEIC  
Exhibit 3: Our proprietary import-implied domestic demand proxy suggests still-weak domestic demand growth in Q2

![](images/ad9ee36ccac4d78d0f9d7a9f735b98969cc9cd705dc40a610bc50dfd2b0adccd.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 4: Our MAP surprise index (21-day moving average) shows recent macro data have been on average above market expectations  
![](images/ef105b70420c9db500e992b7e7bb83570bd2e39ffc12b38478d8cdef701c47bf.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 5: Our manufacturing growth proxy and construction growth proxy both ticked up in June  
![](images/ad1a52e743706bd55a5d52f4e4c3b137f2887557e66f34d91850aa1be2d18fcb.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 6: Our preliminary investment tracker (on a real value-added basis) points to weaker growth in Q2  
![](images/d0765ead4401ec8b5240ad20d12c499b1d44a2828ad42ff30da85d5a8ead55db.jpg)  
Source: GS Global Investment Research

Exhibit 7: Our China inventory tracker suggests inventory levels may have increased in Q2 2026  
![](images/d2a7ae2c6b444c51bd172c303b6a2a62720b14515a6957e3958c1f75d40f8b37.jpg)  
Source: GS Global Investment Research, Haver Analytics

Exhibit 8: The boost from inventory changes to sequential GDP growth likely increased in Q2 2026  
![](images/06996ca32e0c385ff3d23ad4f3e38f77793f352a921f705dcf5997c5e76cc1a5.jpg)  
Source: GS Global Investment Research, Haver Analytics, CEIC, Bloomberg  
Exhibit 9: Our China outside-in export tracker is generally in line with the official export growth data in May

![](images/89f36712c7e65995534a89e0b68d4151bd00746001a5a29f41953b09d2cd0215.jpg)  
Note: May 2026 data print is estimated using countries with imports data available, which account for $31.1\%$ of value of Chinese exports in 2025.  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 10: Our China outside-in import tracker slightly underperformed the official import growth data in May  
![](images/c81bc00a95e1f6e8e9e0ae102ef9adc0934ae7ff8873949fc63833c19ddd144c.jpg)  
Note: May 2026 data print is estimated using countries with exports data available, which account for $65.5\%$ of value of Chinese imports in 2025.  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 11: China Financial Conditions Index (FCI; including credit quantities) tightened in June  
![](images/924c1995b629df066779e43a912d2b97e7526ea1a3d5d147d709f8597fc76263.jpg)  
Source: GS Global Investment Research, CEIC, Bloomberg

Exhibit 12: June's tightening in FCI was mainly driven by FX appreciation against the trade-weighted basket  
![](images/a747abc32dd27d3600c79cbaf236604381f42a81d869721f1c9bbfebde75e6f2.jpg)  
Source: GS Global Investment Research, CEIC, Bloomberg

Exhibit 13: We estimate credit impulse has turned negative this year due to weak credit growth  
![](images/58fc7cffbd58228d93e5a890d2e0f1424095a3e51aefe806d4ef09cd5597e019.jpg)  
The impulses assume that credit extension stays flat through the remainder of this year.  
Source: GS Global Investment Research

Exhibit 14: Our preferred gauge suggests continued FX inflows in June  
![](images/8afc67c769473569e82e878ff1659959e867aabc0d3f95b51f0c9cd4607afb9a.jpg)  
Source: GS Global Investment Research, SAFE

Exhibit 15: Our China domestic macro policy proxy tightened further in June  
![](images/2a5cb7cd2ec35bc5e1ee1ef8f2f767cb6cd535ea2d8a550a128211e057d4361e.jpg)  
Source: GS Global Investment Research, Wind, Haver Analytics, CEIC

Exhibit 16: June's tightening in GS China macro policy proxy was driven by tighter fiscal policy  
![](images/0c3628786fa0a4ab4d553131d0765dd79ce3ee0e7392582486a331c0f1e2352e.jpg)  
Source: GS Global Investment Research, Wind, Haver Analytics, CEIC

Exhibit 17: Our augmented fiscal deficit (AFD) metric narrowed further in June  
![](images/fd3a96ff82f32e18b7de06294d32092bcfcc314bde43fc72aeb36a8c1ae0f60b.jpg)  
Source: GS Global Investment Research, CEIC, Wind

Exhibit 18: China's fiscal "spend-through" ratio rose in June  
![](images/1e8cd51746690156455e10e93bfef253f588f73a6d3dad4bc438763ba49ee9f1.jpg)  
Shaded areas refer to periods when China's year-to-date real GDP growth was equal to or below the full-year growth target. Note that the Chinese government did not set a national growth target for 2020.  
Source: MOF, Wind, CEIC, GS Global Investment Research

Exhibit 19: Government bond net issuance is set to accelerate in the coming months  
![](images/48999a3779e9e163583ff29471af7b9bd3f72ecc0f0b2c510df86cdfc56027d7.jpg)  
Local government refinancing bond issuance for debt resolution is not included.  
Source: Wind, CEIC, GS Global Investment Research

Exhibit 20: Our city-level property relative tightness index suggests continued housing easing  
![](images/48449d8d06015bf5f6d6ea7f26a5c2024b1240276a7963ee5b79584a91d3136a.jpg)  
Source: GS Global Investment Research, local governments, Sofang.com

## Methodology notes for GS proprietary economic indicators

1. Exhibit 1 and Exhibit 2: China Current Activity Indicator (Bloomberg ticker: GSCNCAI) is the “first principal component” of several real activity indicators including industrial production, electricity consumption, PMIs, etc., expressed in GDP-equivalent units. (See the latest GS CAI methodology note here and the revamped methodology for China CAI here.) These indicators can be recategorized to measure sequential momentum in different areas of the economy — manufacturing, consumption and others (i.e., housing and the labor markets).

2. Exhibit 3: Our import-implied real domestic demand infers China's domestic demand by assigning all Chinese imports by sector to an ultimate source of final demand using China's input-output tables. (See a brief summary of the methodology here.) The real domestic demand implied by national accounts is estimated from national accounts data (GDP – (Exports – Imports)), as a cross-check for the validity of the sectoral imports based domestic demand.

3. Exhibit 4: Our China MAP surprise index summarizes the importance and strength (relative to consensus expectations) of economic indicators for the country. Aggregating MAP over time allows us to examine whether economic data are outperforming or underperforming consensus expectations for a certain period.

4. Exhibit 5: Our construction growth proxy is the median year-on-year growth of housing starts, production of steel, cement and glass. Our manufacturing growth proxy is the median year-on-year growth in production of metal cutting machines, autos, power generating equipment and microcomputers. (See our explanations here.)

5. Exhibit 6: Our revamped investment tracker is based on seven underlying investment indicators, including commodity demand and output, equipment sales, construction output, and new construction contracts. After data cleaning, we derive the first principal component, which explains $62\%$ of the total variation across the seven series, and then map it to Gross Fixed Capital Formation (GFCF) to measure investment on a real value-added basis.

6. Exhibit 7 and Exhibit 8: Our revised inventory tracker is based on six underlying inventory indicators, including commodities, PMI sub-indices, industrial enterprises' finished goods inventory, and auto inventory. After data cleaning, we derive the first principal component, which explains $25\%$ of the total variation of the six series, and then map it into percentage of GDP terms as our tracker for inventory changes.

7. Exhibit 9 and Exhibit 10: Our revised “outside-in” trade measures estimate China’s export growth and import growth using “mirror” statistics reported by its major trading partners, based on the country-specific lead-lag relationship, as a cross-check for the validity of China Customs trade data.

8. Exhibit 11 and Exhibit 12: Our revised GS China Financial Conditions (GSFCI) Index tracks liquidity conditions by 1) funding index: AA MTN yield, 3m SHIBOR, M2 and TSF flows; 2) equity market P/E ratio; 3) RMB on a trade-weighted basis. Accordingly, the sequential change in FCI can be attributed to factors through four major channels, i.e., FX, equity, credit and rates.

9. Exhibit 13: Our estimated growth impact of FCI impulse measures the impact of FCI changes on GDP growth (see related studies on China FCI and credit impulse here, here and here).

10. Exhibit 14: Our preferred gauge of FX flows tracks SAFE monthly net FX sales/settlement as well as the net cross-border flows of RMB.

11. Exhibit 15 and Exhibit 16: Our China domestic macro policy proxy summarizes China domestic macro policy stance from four aspects: 1) fiscal policy; 2) monetary policy; 3) credit policy; and 4) housing policy.

12. Exhibit 17: Our measure of augmented fiscal deficit is a sum of effective on-budget fiscal deficit and off-budget fiscal deficit. We estimate the off-budget spending by major channels that finance quasi-fiscal activities, which includes new local government special bonds (LGSB), land sales revenue, local government financing vehicle (LGFV) bonds, policy banks support, shadow banking loans, etc.

13. Exhibit 18: We define the fiscal spend-through ratio as a function of government revenue, government bond net issuance, and the sequential change in fiscal deposits, among others, to measure the degree to which policymakers are deploying the funds raised from government revenue and bond issuance.

14. Exhibit 19: Our government bond financing tracker measures the pace of government bond net issuance on a monthly basis and its breakdown by bond type, including central government general bond (CGGB), central government special bond (CGSB), local government general bond (LGGB) and LGSB. We also provide our projections for their monthly net issuance schedule through the remainder of the year, based on annual government bond issuance quotas, fiscal policy stance and seasonal patterns, but these may be subject to further changes when more data/policy signals come in.

15. Exhibit 20: Our property policy relative tightness index tracks the relative tightness of property policies in over 100 cities from the following aspects: 1) demand: purchase restrictions (household registration, social welfare contribution, etc.), credit restrictions (mortgage rate, down payment), sales restrictions; 2) supply: caps on selling prices, presales restrictions, land transaction tax, etc.; 3) others: property speculation, land supply.

## The China Economics Team

Andrew Tilton  
+852-2978-1802  
andrew.tilton@gs.com  
GS (Asia) L.L.C.

Xinquan Chen  
+852-2978-2418  
xinquan.chen@gs.com  
GS (Asia) L.L.C.

Hui Shan  
+852-2978-6634  
hui.shan@gs.com  
GS (Asia) L.L.C.

Yuting Yang
+852-2978-7283
yuting.y.yang@gs.com
GS (Asia) L.L.C.

Lisheng Wang
+852-3966-4004
lisheng.wang@gs.com
GS (Asia) L.L.C.

Chelsea Song
+852-2978-0106
chelsea.song@gs.com
GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Chelsea Song, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Chelsea Song GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant information and disclosures can be found at this link:

https://www.goldmansachs.com/worldwide/india/research-analyst. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets A

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
