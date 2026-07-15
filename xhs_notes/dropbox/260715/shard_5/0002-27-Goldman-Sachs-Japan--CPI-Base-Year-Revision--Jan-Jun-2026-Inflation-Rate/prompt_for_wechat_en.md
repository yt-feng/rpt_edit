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
# Japan: CPI Base-Year Revision: Jan-Jun 2026 Inflation Rate to be Revised Up, Likely to Exert Downward Pressure on Future Inflation Rates

BOTTOM LINE: This year marks the once-in-five-years base-year revision of the consumer price index (CPI), in which the weights of each item in the CPI will be reviewed, and the estimation methods for some price indices will also be changed. Accordingly, a retroactive revision of the CPI for January-June 2026 is scheduled for August 7. We expect slight upward revisions to both the core (excluding fresh foods) and new core (excluding fresh foods and energy) CPIs, but a degree of uncertainty remains as some price indices have not yet been released. We also note that this base-year revision is likely to exert downward pressure on our inflation forecasts for FY2026-27.

Tomohiro Ota
+81(3)4587-9984 |
tomohiro.ota@gs.com
GS Japan Co., Ltd.

## MAIN POINTS:

The consumer price index is estimated by calculating a weighted average of the price indices of various items, based on the consumption patterns (weights) of average consumers. However, because consumer behavior changes over time, a “base-year revision” is conducted once every five years to update the “average consumption pattern.” For the current CPI series, the average consumption pattern for 2019-2020 has been used as the base, but from August onwards, the average consumption pattern for 2025 will become the new base.

The revision to the 2025 base is scheduled for August 7, and the CPI for January-June 2026, estimated under the current (2020) base, will be retroactively revised (inflation rates up to December 2025 will not be revised). Exhibit 1 shows a comparison of the current and new core and new core CPI inflation rates estimated by us based on the new 2025 base consumption pattern released on July 10, which suggests that inflation rates for January-June 2026 are likely to be revised upward slightly under the new base.

■ Two main factors contribute to this. First, because the weights of high school tuition, school lunches, and nursery school fees will decrease in the new base, the negative contribution from the free tuition, school lunches and childcare policies implemented since 2025 in the current CPI will shrink, pushing up the inflation rate. Second, because the weight of rice prices—which drove inflation from 2025 to early 2026—will be nearly doubled in the new 2025 basis, the inflation rate for January–March 2026 in particular will likely be revised upward significantly (from April onward, rice prices have turned into a negative contribution).

However, it should be noted that the base-year revision involves not only changes to weights but also changes to the estimation methods for some price indices. Therefore, Exhibit 1 is merely a rough estimate at this stage, and a

degree of uncertainty remains.

We note that this 2025 base-year revision is likely to exert downward pressure on the future inflation outlook. We have been expecting the lower rice prices to suppress future inflation, and the increase in the weight of rice in the new basis (from 0.62% to 1.01%) would magnify the negative contribution of the drop in rice prices. In addition, the decline in the weight of mobile phones (from 0.90% to 0.58%), for which potential price hikes have been reported from the second half of this year through the first half of next year, would likely reduce this positive contribution.

A comparison of the weights of major CPI items is provided in Exhibit 2.

Exhibit 1: Core and New Core CPI Inflation for January-June 2026 Could Be Revised Up at the August CPI Base Year Revision  
![](images/722181ccd20edb635f3fabfefe764535156695e873a2feed2e06e8b4187d9932.jpg)  
Source: Ministry of Internal Affairs and Communications, GS Global Investment Research

Exhibit 2: Weights of CPI Main Categories  
2025 New Basis vs. 2020 Current Basis (per 10000)

<table><tr><td rowspan="2"></td><td colspan="3">National CPI</td><td colspan="3">Tokyo CPI</td></tr><tr><td>New</td><td>Current</td><td>Chg</td><td>New</td><td>Current</td><td>Chg</td></tr><tr><td>Overall CPI</td><td>10000</td><td>10000</td><td>(+0)</td><td>10000</td><td>10000</td><td>(+0)</td></tr><tr><td>Core CPI (excl. fresh food)</td><td>9621</td><td>9604</td><td>(+17)</td><td>9621</td><td>9615</td><td>(+6)</td></tr><tr><td>New core CPI (excl. fresh food and energy)</td><td>8872</td><td>8892</td><td>(-20)</td><td>9162</td><td>9145</td><td>(+17)</td></tr><tr><td>Global core CPI (excl. food and energy)</td><td>6609</td><td>6781</td><td>(-172)</td><td>6959</td><td>7111</td><td>(-152)</td></tr><tr><td>Food and beverages</td><td>2754</td><td>2626</td><td>(+128)</td><td>2682</td><td>2529</td><td>(+153)</td></tr><tr><td>Fresh food</td><td>379</td><td>396</td><td>(-17)</td><td>379</td><td>385</td><td>(-6)</td></tr><tr><td>Food excluding fresh food</td><td>2375</td><td>2230</td><td>(+145)</td><td>2304</td><td>2144</td><td>(+160)</td></tr><tr><td>Rice</td><td>101</td><td>62</td><td>(+39)</td><td>74</td><td>48</td><td>(+26)</td></tr><tr><td>Eating out</td><td>491</td><td>434</td><td>(+57)</td><td>631</td><td>515</td><td>(+116)</td></tr><tr><td>School lunch</td><td>17</td><td>25</td><td>(-8)</td><td>1</td><td>19</td><td>(-18)</td></tr><tr><td>Housing</td><td>2182</td><td>2149</td><td>(+33)</td><td>2720</td><td>2760</td><td>(-40)</td></tr><tr><td>Housing rent</td><td>1861</td><td>1833</td><td>(+28)</td><td>2441</td><td>2454</td><td>(-13)</td></tr><tr><td>House rent, private</td><td>217</td><td>225</td><td>(-8)</td><td>383</td><td>391</td><td>(-8)</td></tr><tr><td>Imputed rent</td><td>1634</td><td>1580</td><td>(+54)</td><td>2048</td><td>2000</td><td>(+48)</td></tr><tr><td>Repairs &amp; maintenance</td><td>321</td><td>316</td><td>(+5)</td><td>278</td><td>306</td><td>(-28)</td></tr><tr><td>Fuel, light and water charges</td><td>698</td><td>693</td><td>(+5)</td><td>506</td><td>555</td><td>(-49)</td></tr><tr><td>Electricity</td><td>376</td><td>341</td><td>(+35)</td><td>279</td><td>262</td><td>(+17)</td></tr><tr><td>Furniture and household utensils</td><td>372</td><td>387</td><td>(-15)</td><td>325</td><td>335</td><td>(-10)</td></tr><tr><td>Clothes and footwear</td><td>299</td><td>353</td><td>(-54)</td><td>314</td><td>375</td><td>(-61)</td></tr><tr><td>Medical care</td><td>466</td><td>477</td><td>(-11)</td><td>487</td><td>471</td><td>(+16)</td></tr><tr><td>Transportation and communication</td><td>1444</td><td>1493</td><td>(-49)</td><td>1008</td><td>1007</td><td>(+1)</td></tr><tr><td>Transportation</td><td>177</td><td>167</td><td>(+10)</td><td>273</td><td>235</td><td>(+38)</td></tr><tr><td>Mobile phone charges</td><td>231</td><td>271</td><td>(-40)</td><td>161</td><td>206</td><td>(-45)</td></tr><tr><td>Cellular phones</td><td>58</td><td>90</td><td>(-32)</td><td>40</td><td>69</td><td>(-29)</td></tr><tr><td>Eductaion</td><td>311</td><td>304</td><td>(+7)</td><td>413</td><td>465</td><td>(-52)</td></tr><tr><td>High school fees</td><td>24</td><td>56</td><td>(-32)</td><td>13</td><td>77</td><td>(-64)</td></tr><tr><td>College &amp; university fees</td><td>160</td><td>121</td><td>(+39)</td><td>220</td><td>189</td><td>(+31)</td></tr><tr><td>Culture &amp; Recreation</td><td>906</td><td>911</td><td>(-5)</td><td>1015</td><td>939</td><td>(+76)</td></tr><tr><td>Hotel charges</td><td>118</td><td>81</td><td>(+37)</td><td>191</td><td>100</td><td>(+91)</td></tr><tr><td>Miscellaneous</td><td>570</td><td>607</td><td>(-37)</td><td>532</td><td>564</td><td>(-32)</td></tr><tr><td>Nursery school fees</td><td>33</td><td>52</td><td>(-19)</td><td>41</td><td>54</td><td>(-13)</td></tr><tr><td colspan="7">Regrouped</td></tr><tr><td>Energy</td><td>749</td><td>712</td><td>(+37)</td><td>460</td><td>470</td><td>(-10)</td></tr><tr><td>Goods</td><td>5036</td><td>5046</td><td>(-10)</td><td>4297</td><td>4341</td><td>(-44)</td></tr><tr><td>Services</td><td>4964</td><td>4954</td><td>(+10)</td><td>5703</td><td>5659</td><td>(+44)</td></tr><tr><td>Public services</td><td>1079</td><td>1219</td><td>(-140)</td><td>992</td><td>1101</td><td>(-109)</td></tr><tr><td>General services</td><td>3886</td><td>3735</td><td>(+151)</td><td>4712</td><td>4557</td><td>(+155)</td></tr></table>

Source: Ministry of Internal Affairs and Communications, Data compiled by GS Global Investment Research

## Disclosure Appendix

## Reg AC

I, Tomohiro Ota, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Tomohiro Ota GS Japan Co., Ltd..

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

Japan: GS Japan Co., Ltd. is a Financial Instrument Dealer registered with the Kanto Financial Bureau under registration number Kinsho 69, and a member of Japan Securities Dealers Association, Financial Futures Association of Japan Type II Financial Instruments Firms Assoc

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
