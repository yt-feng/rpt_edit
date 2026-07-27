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
# Global Economics Comment: More Chinese Exports, Fewer Chinese Imports, Lower Global Inflation

Chinese exports to non-US DMs have grown rapidly since the pandemic, reflecting both trade reallocation away from the US and overall export strength. At the same time, Chinese imports from the rest of the world have pulled back amid an increased push for self-sufficiency. In this Global Economics Comment, we check in on how these shifting trade patterns are affecting inflation.

Megan Peters
+44(20)7051-2058 |
megan.l.peters@gs.com
GS International

Leveraging a harmonized cross-country trade-inflation panel, we find that each 1pp increase in Chinese exports to other countries (as a share of total consumption in the recipient countries) since 2024 is associated with a $0.5\%$ decline in goods prices. On average, we estimate this channel has lowered goods prices by $0.6\%$ across non-US DMs so far.

Using the same harmonized panel, we find that for a country-product pair with complete import dependence, a 1pp decline in China's share of global imports of that product would lower prices by $1.3\%$ . This channel implies a modest incremental drag of around $0.1\%$ on realized goods prices.

Combined, our analysis suggests that these dynamics have lowered goods prices by $0.7\%$ across non-US DMs over the last two years—corresponding to a 0.1-0.2pp drag on annual headline and core inflation in DMs—with larger effects in Japan $(1.1\%)$ and the Euro area $(1.0\%)$ . We expect these effects to build moving forward, both because realized trade shifts will take time to fully pass through to consumer prices, and because our China economics team expects the current account surplus will continue to widen.

## More Chinese Exports, Fewer Chinese Imports, Lower Global Inflation

China's exports to non-US DMs have grown rapidly since the pandemic, while China's imports from the rest of the world have pulled back amid an increased push for self-sufficiency. We have previously argued that increased goods supply from China should exert a meaningful disinflationary impulse across DMs, especially in Europe (as highlighted by our European economics team). In this Global Economics Comment we check in on how these shifting trade patterns are affecting inflation to date.

Exhibit 1 shows that China's nominal exports to non-US DMs have grown around $20\%$ since 2024, whereas exports to the US have dropped sharply amid ongoing trade tensions. While part of the increase in exports to other DMs likely reflects trade reallocation, overall export growth has also been robust despite the pullback in US demand.

Exhibit 1: China's Total Exports Have Grown Rapidly Despite a Pullback in the US  
![](images/516b12e1e6ee33f751119e985026454f00af237bfbbf9154c09deabb9073c72a.jpg)  
Source: Haver Analytics, GS Global Investment Research

In addition to the rapid growth in China's exports, China's imports from other countries have undershot their pre-pandemic trend across a range of products (Exhibit 2), reflecting an ongoing push by Chinese policymakers to increase self-sufficiency.

Exhibit 2: Chinese Import Growth Has Undershot Its Pre-Pandemic Trend  
![](images/e029dacadee965f8a1e916253697f4446617547a0558b02390c997c6b1f74c8d.jpg)  
Source: Haver Analytics, GS Global Investment Research

These trade shifts should put downward pressure on DM prices via two channels. First, increased Chinese exports should directly increase supply and lower consumer prices in recipient economies. Second, lower Chinese demand for imports from the rest of the world should free up supply in global goods markets, providing an additional disinflationary impulse. Our previous review of the literature suggested that, on average, a 1% increase in foreign goods supply (measured as a share of overall domestic goods demand) lowers consumer prices by 0.8%.

To assess how much these dynamics have played out so far, we build a cross-country panel linking inflation and trade data. We map trade data at the 6-digit harmonized system (HS) level to goods inflation categories at the 3-digit COICOP (Classification of Individual Consumption According to Purpose) level in two steps. First, we use a UN Statistics Division (UNSD) crosswalk to convert trade data into Eurostat's Classification of Products by Activity (CPA). Second, we apply Eurostat bridging matrices to allocate CPA-level imports across COICOP consumption categories. In countries that do not report inflation data according to COICOP, we construct harmonized measures of inflation using the closest available analogues.

Leveraging this panel, we quantify the effect of the first channel by relating Chinese import penetration (defined as Chinese exports as a share of total consumption in recipient countries) to prices across major non-US economies that have reported detailed trade data for Q1 of this year. The pooled scatter on the left-hand side of Exhibit 3—which controls for country fixed-effects—shows a negative and statistically significant correlation between Chinese import penetration and goods prices. Each 1pp increase in Chinese import penetration between 2024Q1 and 2026Q1 is associated with a $0.5\%$ decline in prices over the same period.

We estimate the second channel using the same harmonized panel. This time our variable of interest is the interaction between the change in China's import demand for a given product (as a percentage of global import demand) and global import exposure at the country-product level (as a share of total consumption) across DMs. The right-hand side of Exhibit 3 shows that most country-product pairs experienced small, slightly negative changes in China's share of global import demand (scaled by overall import exposure). However, larger changes have generally translated into intuitive price shifts, with a positive and statistically significant relationship between demand for imports from abroad and prices in other major economies. The slope coefficient in the pooled scatter implies that, for a country-product pair that is fully import-dependent, a 1pp decline in China's share of global import demand would lower prices by $1.3\%$ .

Exhibit 3: Higher Exports and Lower Imports in China Are Both Associated with Lower DM Prices  
![](images/8aac470b918bb9f5a6f5fcc64e508454c7b463b88e77c29af2b3aaeb6f5991ed.jpg)

![](images/7a1f7a7053b1c614d33cf935980e58bbdda7cde32fa2d85c039dfd356b04d3d2.jpg)  
Source: UN Comtrade, UNSD, Eurostat, Haver Analytics, GS Global Investment Research

Combining the results of our pooled regressions with realized trade data suggests that shifts in Chinese trade patterns have lowered goods prices by 0.7% on average over the last two years (Exhibit 4), corresponding to a 0.1-0.2pp drag on annual headline and core inflation in DMs. The effect is driven mainly by higher Chinese exports, which have reduced goods prices by 0.6% on average, with a modest incremental drag of around 0.1% from lower Chinese imports. The impacts are largest in the Euro area (1.0%), primarily because of greater Chinese import penetration into European markets, and in Japan (1.1%), where weaker Chinese demand for imports from Japan has had a somewhat larger effect. By contrast, the impact is smaller in Canada (0.2%), where Chinese import penetration has risen less.

Exhibit 4: Changes to Chinese Trade Patterns Have Reduced Prices by $0.7\%$ Across Non-US DMs Over the Last Two Years

![](images/7a6a3e63f10d09681b5ba278bf07d63dbc5353f1cfb15e01cb3adece7328e4fc.jpg)  
Source: GS Global Investment Research

We expect these effects to continue to build going forward, both because the impacts of realized trade shifts may not yet be fully reflected in consumer prices, and because our China economics team expects the current account surplus will continue to widen. Although the main driver of our relatively benign inflation outlook is that domestic supply and demand broadly appear in balance, these Chinese trade dynamics are another reason why inflation will likely return to near-target levels in major DMs in the upcoming years.

## Megan Peters

## The Global Economics Team

Jan Hatzius +1(212)902-0394 jan.hatzius@gs.com GS & Co. LLC

Joseph Briggs +1(212)902-2163 joseph.briggs@gs.com GS & Co. LLC

Sarah Dong
+1(212)357-9741
sarah.dong@gs.com
GS & Co. LLC

Megan Peters  
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

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant information and disclosures can be found at this link:

https://www.goldmansachs.com/worldwide/india/research-analyst. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no responsibility for any investment decisions that may be taken by a client or any other person based on this research report. Singapore: GS (Singapore) Pte. (Company Number: 198602165W), which is regulated by the Monetary Authority of Singapore, accepts legal responsibility for this research, and should be contacted with respect to any matters arising from, or in connection with, this research. Taiwan: This material is for reference only and must not be reprinted without permission. Investors should carefully consider their own investment risk. Investment results are the responsibility of the individual investor. United Kingdom: Persons who would be categorized as retail clients in the United Kingdom, as such term is defined in the rules of the Financial Conduct Authority, should read this research in conjunction with prior GS on the covered companies referred to herein and should refer to the risk warnings that have been sent to them by GS International. A copy of these risks warnings, and a glossary of certain financial terms used in this report, are

available from GS International on request.

European Union and United Kingdom: Disclosure information in relation to Article 6 (2) of the European Commission Delegated Regulation (EU) (2016/958) supplementing Regulation (EU) No 596/2014 of the European Parliament and of the Council (including as that Delegated Regulation is implemented into United Kingdom domestic law and regulation following the United Kingdom's departure from the European Union and the European Economic Area) with regard to regulatory technical standards for the technical arrangements for objective presentation of investment recommendations or other information recommending or suggesting an investment strategy and for disclosure of particular interests or indications of conflicts of interest is available at https://www.gs.com/disclosures/europeanpolicy.html which states the European Policy for Managing Conflicts of Interest in Connection with Investment Research.

Japan: GS Japan Co., Ltd. is a Financial Instrument Dealer registered with the Kanto Financial Bureau under regist

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
