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
# Global PMI Monitor: Elevated Manufacturing Suppliers' Delivery Times

## DM trends:

☐ The DM composite flash PMI rose by +1.6pt to 52.8 in July, reflecting rises in both services (+1.9pt to 52.6) and manufacturing (+0.1pt to 53.2).

Sarah Dong
+1(212)357-9741 | sarah.dong@gs.com
GS & Co. LLC

□ Manufacturing suppliers' delivery times eased in ex-US DMs but remain near all-time highs.

## ■ Country-level trends:

☐ The manufacturing flash PMI rose by +0.6pt to 52.0 in the Euro area and fell by -0.2pt to 53.8 in the US.

☐ The services flash PMI rose by +3.1pt to 51.8 in the UK and fell by -0.3pt to 51.9 in Japan.

## ■ Activity components:

☐ The DM flash forward-looking component rose for both manufacturing (orders-to-inventories ratio +0.03 to 1.10) and services (future activity component +1.9pt to 61.9).

☐ The composite flash employment PMI rose by +1.6pt to 50.7 in the US and ticked down by -0.1pt to 51.6 in Japan.

## Inflation-related components:

□ Manufacturing suppliers' delivery times eased slightly but remained elevated across major DMs in July (DM average +1.0pt to 41.8).

☐ The DM input price PMI fell by -3.3pt to 68.4 for manufacturing and rose by 0.4pt to 62.4 for services; the DM output price PMI fell by -1.6pt to 59.6 for manufacturing and rose by +0.6pt to 56.6 for services.

Exhibit 1: Manufacturing Suppliers' Delivery Times Eased in ex-US DMs but Remain Near All-Time Highs  
![](images/dc61eb49a4b5379ea5d46deb4d9b8799d2dfe0a2ad351860ec64e03390eba4b8.jpg)  
Source: S&P Global, GS Global Investment Research

## Elevated Manufacturing Suppliers' Delivery Times

## DM Trends

Exhibit 2: The DM Composite Flash PMI Rose by +1.6pt to 52.8 in July, Reflecting Rises in Both Services (+1.9pt to 52.6) and Manufacturing (+0.1pt to 53.2)

![](images/e1e19ad2fcb67e3411d20b7ed2e8978b0413da013fcbffa4019cd7200865f037.jpg)  
DM is a GDP weighted sum of PMI indices for the US, the Euro area, the UK, Australia, and Japan.  
Source: S&P Global, Haver Analytics, GS Global Investment Research

Exhibit 3: The Manufacturing Flash PMI Rose by +0.6pt to 52.0 in the Euro Area and Fell by -0.2pt to 53.8 in the US  
![](images/b2ec63cbf2823c88d3a25b11b2a4e97b7bb87349013a9890a0e47570a1b147d7.jpg)  
Source: S&P Global, Haver Analytics, GS Global Investment Research

Exhibit 4: The Services Flash PMI Rose by +3.1pt to 51.8 in the UK and Fell by -0.3pt to 51.9 in Japan  
![](images/1699ae07a7ac9bf2ac5c12a49763fbf423841f06b530ce40dab7d41227c4da65.jpg)  
Source: S&P Global, Haver Analytics, GS Global Investment Research

Exhibit 5: Early US Business Surveys Showed Positive Signals for Both Manufacturing and Services Activity in July  
![](images/77d3f5fcf1261131270c24bc30876c950122c80aff7a2e2883d78b0f95abf60a.jpg)  
Source: S&P Global, Federal Reserve, Haver Analytics, GS Global Investment Research

## Activity Components

Exhibit 6: The DM Flash Forward-Looking Component Rose for Both Manufacturing (Orders-to-Inventories Ratio +0.03 to 1.10) and Services (Future Activity Component +1.9pt to 61.9)  
![](images/85ed8d99ba472f7ad82def7e7d5cd4171d5aeb622b3ac34506a160268458ea4f.jpg)  
Note: Grey bars denote US recession.  
Source: S&P Global, Haver, GS Global Investment Research

DM is a GDP weighted sum of PMI indices for the US, the Euro Area, the UK, Australia, and Japan.

Exhibit 7: Early US Business Surveys Provided Negative Signals for Manufacturing Future Activity and Positive Signals for Services Future Activity in July  
![](images/87a5f4a1b93bd4e2c29d9333d00f4ae89a0d6449f3846fe7741734525c9a00c2.jpg)  
Source: S&P Global, US Federal Reserve Bank, Haver, GS Global Investment Research

Exhibit 8: The Composite Flash Employment PMI Rose by +1.6pt to 50.7 in the US and Ticked Down by -0.1pt to 51.6 in Japan  
![](images/87595e0f2533f21cc2bca33fc310e41b46d18bf9ea0d1608e2ad32ef0dad63aa.jpg)  
Source: S&P Global, Haver Analytics, GS Global Investment Research

Exhibit 9: Early US Business Surveys Show Slightly Positive Signals for Manufacturing Employment and Mixed-to-Positive Signals for Services Employment in July  
![](images/6d5e635a9c1d473e3397b7281d5c3bd29d9fcb8a614766bdde1cd889122f79dd.jpg)  
Source: S&P Global, Haver Analytics, GS Global Investment Research

## Inflation-Related Components

Exhibit 10: Manufacturing Suppliers' Delivery Times Eased Slightly but Remained Elevated Across Major DMs in July (DM Average +1.0pt to 41.8)  
![](images/8ebd39458b1d1e0bc3e64d83b2db36f69317514355c0850a51bad15f6a229a60.jpg)  
Source: S&P Global, Haver, GS Global Investment Research

Exhibit 11: Early US Business Surveys Continue to Suggest Above-Average Supplier Delivery Times in July  
![](images/80d94fd051e2b4c8b44aa6a8ea8d575187d02293bc482bdc2620de7c12b4936d.jpg)  
Source: S&P Global, Haver Analytics, GS Global Investment Research

Exhibit 12: The DM Input Price PMI Fell by -3.3pt to 68.4 for Manufacturing and Rose by 0.4pt to 62.4 for Services; the DM Output Price PMI Fell by -1.6pt to 59.6 for Manufacturing and Rose by +0.6pt to 56.6 for Services

Latest Output Prices PMIs (Incl. Flash)  
Latest DM Prices PMIs (Incl. Flash)  
![](images/d5101afa46debef02b9663324ed439501513f2c4537e6b11380403aee714a24e.jpg)  
Note: Grey bars denote US recession.

DM is a GDP weighted sum of PMI indices for the US, the Euro Area, the UK, Australia, and Japan.  
![](images/98cf309118abcf6843a942b9fccf8c26021e845c78b546553a03158226af224a.jpg)  
Source: S&P Global, Haver Analytics, GS Global Investment Research

Exhibit 13: The Manufacturing Output Price PMI Fell by -3.2pt to 57.4 in the Euro Area and the Services Output Price PMI Rose by +3.7pt to 57.2 in Australia

![](images/6a51797278b9d386e69ef687b4312a5ea421ce0c53e07b68d586f926c7b7fb77.jpg)  
Note: Grey bars denote US recession.

![](images/cb1c918b52c4a9cda9cfeabf4f2ea3fcb7ea220dc0949f14e2e1573d4d0c5665.jpg)  
Source: S&P Global, Haver Analytics, GS Global Investment Research

## Analysis of Early Business Surveys From Our Economics Team

USA: S&P PMIs Mixed as Services Increase but Manufacturing Edges Down, July 24

USA: Philly Fed Manufacturing Highest Since 2021, July 16

USA: Empire Manufacturing Above Consensus Expectations, July 15

Europe July Flash PMIs: Firming Activity and Moderating Price Pressures, July 24

## The Global Economics Team

Jan Hatzius

+1(212)902-0394

jan.hatzius@gs.com

GS & Co. LLC

Joseph Briggs
+1(212)902-2163
joseph.briggs@gs.com
GS & Co. LLC

Sarah Dong +1(212)357-9741 sarah.dong@gs.com GS & Co. LLC

Megan Peters

+44(20)7051-2058

megan.l.peters@gs.com

GS International

## Disclosure Appendix

## Reg AC

I, Sarah Dong, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Sarah Dong GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant information and disclosures can be found at this link:

https://www.goldmansachs.com/worldwide/india/research-analyst. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no responsibility for any investment decisions that may be taken by a client or any other person based on this research report. Singapore: GS (Singapore) Pte. (Company Number: 198602165W), which is regulated by the Monetary Authority of Singapore, accepts legal responsibility for this research, and should be contacted with respect to any matters arising from, or in connection with, this research. Taiwan: This material is for reference only and must not be reprinted without permission. Investors should carefully consider their own investment risk. Investment results are the responsibility of the individual investor. United Kingdom: Persons who would be categorized as retail clients in the United Kingdom, as such term is defined in the rules of the Financial Conduct Authority, should read this research in conjunction with prior GS on the covered companies referred to herein and should refer to the risk warnings that have been sent to them by GS International. A copy of these risks warnings, and a glossary of certain financial terms used in this report, are

available from GS International on request.

European Union and United Kingdom: Disclosure information in relation to Article 6 (2) of the European Commission Delegated Regulation (EU) (2016/958) supplementing Regulation (EU) No 596/2014 of the European Parliament and of the Council (including as that Delegated Regulation is implemented into United Kingdom domestic law and regulation following the United Kingdom's departure from the European Union and the European Economic Area) with regard to regulatory technical standards for the technical arrangements for objective presentation of investment recommendations or other information recommending or suggesting an investment strategy and for disclosure of particular interests or indications of conflicts of interest is available at https://www.gs.com/disclosures/europeanpolicy.html which states the European Policy for Managing Conflicts of Interest in Connection with Investment Research.

Japan: GS Japan Co., Ltd. is a Financial Instrument Dealer registered with the Kanto Financial Bureau under registration number Kinsho 69, and a member of Japan Securities Dealers Association, Financial Futures Association of Japan Type II Financial Instruments Firms Association, and Investment Management Association of Japan. Sales and purchase of equities are subject to commission pre-determined with clients plus consumption tax. See company-specific disclosures as to any applicable disclosures required by Japanese stock exchanges, the Japanese Securities Dealers Association or the Japanese Securities Finance Company.

## Global product; distributing entities

GS Global Investment Research produces and distributes research products for clients of GS on a global basis. Analysts based in GS offices around the world produce research on industries and companies, and research on macroeconomics, currencies, commodities and portfolio strategy. This research is disseminated in Australia by GS Australia Pty Ltd (ABN 21 006 797 897); in Brazil by GS do Brasil Corretora de Títulos e Valores Mobiliários S.A.; Public Communication Channel GS Brazil: 0800 727 5764 and / or contatogoldmanbrasil@gs.com. Available Weekdays (except holidays), from 9am to 6pm. Canal de Comunicação com o Público GS Brasil: 0800 727 5764 e/ou contatogoldmanbrasil@gs.com. Horário de funcionamento: segunda-feira à sexta-feira (exceto feriados), das 9h às 18h; in Canada by GS & Co. LLC; in Hong Kong by GS (Asia) L.L.C.; in India by GS (India) Securities Private Ltd.; in Japan by GS Japan Co., Ltd.; in the Republic of Korea by GS (Asia) L.L.C., Seoul Branch; in New Zealand by GS New Zealand Limited; in Russia by OOO GS; i

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
