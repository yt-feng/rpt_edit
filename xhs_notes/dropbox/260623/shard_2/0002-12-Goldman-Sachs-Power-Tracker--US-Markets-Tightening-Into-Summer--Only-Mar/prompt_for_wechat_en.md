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
# Power Tracker: US Markets Tightening Into Summer, Only Marginally Eased by Coal Power Policy

■ Regional divergence in focus as summer starts. June 1 marks the rollover of 1-month forward contracts across regional power markets from trading June contracts to trading July contracts. This transition reveals market expectations on peak summer power market tightness, along with generation fuel costs. We see contrasting trends between PJM (Mid-Atlantic) and ERCOT (Texas) power markets:

□ PJM (Mid-Atlantic): The power price increased significantly more during this year's May-to-June rollover compared to the historical average in the past decade, both in terms of the absolute price level (+28 USD/MWh in 2026 vs +15 USD/MWh in 2016-2025) and the percentage change (+44% vs +30%, Exhibit 1), despite prices of marginal generation fuels, natural gas and coal, increasing much less. This larger price increase into the summer, combined with its upward trend since 2020 (Exhibit 1), is consistent with our view of a tightening power market in the region: PJM hosts 39% of US data center power demand capacity, where power demand growth has continued to outpace power supply growth.

☐ ERCOT (Texas): While the ERCOT market also experienced its typical seasonal price increase rolling over into June, the absolute price rise of \$24/MWh was smaller than the previous decade's average of \$30/MWh and the percentage increase was just above the historical average (61% versus 56%, Exhibit 1). In addition, the price levels in both May and June have been lower than in 2024/2025, driven by the recent softening in the Texas market $^{1}$ .

☐ Regional divergence: This rollover contrast between these two regional markets is consistent with our regional divergence view that ERCOT has entered a softening path since late-2025 with substantial expansion in power supply, while we expect PJM to remain critically tight in the next few years.

We expect federal support for coal power to offer marginal relief. To alleviate power market tightness, the US administration refreshed its support for coal power following President Trump's advocacy for "Beautiful Clean Coal Power" earlier this year. Earlier this month, the president announced a new plan to allocate nearly \$700 million to support coal power (and coal exports), mainly by

Hongcen Wei  
+1(212)934-4691 |  
hongcen.wei@gs.com  
GS & Co. LLC

Laura Cyr
+1(212)902-3435 | laura.x.cyr@gs.com
GS & Co. LLC

Daan Struyven +1(212)357-4172 | daan.struyven@gs.com GS & Co. LLC

Samantha Dart +1(212)357-9428 | samantha.dart@gs.com GS & Co. LLC

2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 financing delaying/canceling scheduled coal power retirements. While we expect this plan to effectively add incremental power supply relative to previous schedules, along with emergency orders of US Department of Energy (DOE) that direct coal power plants to remain online, we believe the overall impact on resolving market tightness could be marginal in 2026-2028 and after 2028 for the following reasons:

☐ Increasing difficulties for more retirement delays: A significant amount of scheduled coal retirements have already been delayed in the past year after the first DOE emergency order in May 2025, which pushed 2025/2026 retirements out to 2026-2029 (Exhibit 2). Remaining scheduled retirements could be subject to physical/financial constraints: already delayed retirements may face a higher bar to be delayed again and most coal plants are old, both lacking extensive maintenance given the original retirement schedules which could drive the cumulative maintenance costs beyond the scope of the \$700-million fund.

☐ Longer-term policy uncertainty: Coal power plants and coal producers continue to face regulatory and policy uncertainty beyond 2028, which disincentivizes significant capex to upgrade or even expand capacity. One example is the coal power retirement delays in the TVA (Tennessee) power market, where a total of 4.1 GW coal power generation capacity, all originally scheduled for retirement by the end of 2028, has been delayed, while retirement schedules beyond that window remain unchanged.

## Featured Charts

Exhibit 1: The rollover of power forward contracts show a higher-than-average June price level and May-to-June price increase in PJM vs lower-than-average in ERCOT

![](images/c2e167417cd3312dc65a17de29cfb9c8b26fdb9cf48b4b3d90904e8e11dab329.jpg)  
2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

![](images/c1ea60ee14881c617ce23175fcd597ab1d58735ab88de89c5376a8a042f1683b.jpg)  
Source: Bloomberg, GS Global Investment Research  
Prices of PJM in 2022 and of ERCOT in 2018 and 2022 are above 100 \$/MWh and not shown in the charts, but are counted in historical average calculations.

Exhibit 2: Coal retirement delays since 2025 have effectively increased power supply in the next few years, but are more constrained going forward

![](images/e05e152e7870313ce2cec552e3632e9d97e4556772e59de0f0d93d590c8ab35e.jpg)  
Based on EIA generator schedules released in late May 2026, which do not include some recent announcements/DOE orders that adjust the timeline of coal power plants' retirements  
Source: EIA, GS Global Investment Research

## Prices

Exhibit 3: ERCOT (Texas) early summer power price remains weak yoy, remaining below 60 USD/MWh
ERCOT North 345kV Hub peak load prices

![](images/ab299c38297e3dadf17930a48b991fecd488d335cce229edb6eb766ceafbcba2.jpg)  
Source: Bloomberg

Exhibit 4: Power prices in PJM (Mid-Atlantic) rally into the 90 USD/MWh range with the forward contract rollover  
PJM western hub peak power swap prices  
![](images/9806dd7310c67e57078c6c109561170459571f60514eb8b5d020821a60f92277.jpg)  
Source: Bloomberg

## Market Tightness

Exhibit 5: The PJM (Mid-Atlantic) power market was tightened by heatwaves into June  
![](images/3070667604d074edfc67ea56ed9593e7ff22363ec56ee0d5583b7962b4969b81.jpg)  
Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a given power market, indicating critical tightness if below 15%. Not showing in the chart if above 100% (a very soft market).  
Source: Regional power ISOs and RTOs, EIA, Bloomberg, GS Global Investment Research

Exhibit 6: The MISO (Mid-Continental) power market also turned tighter into June before softening this week  
![](images/b49771764ccb7c4402b9d0ef15a998a98c03519a88e8c64339a2d0a9cab7d09a.jpg)  
Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a given power market, indicating critical tightness if below $15\%$ . Not showing in the chart if above $100\%$ (a very soft market).  
Source: Regional power ISOs and RTOs, EIA, Bloomberg, GS Global Investment Research

Exhibit 7: The ERCOT (Texas) power market maintained a soft balance with mild weather  
![](images/9f0dd1cab75a3e6f3389f83559deb65227839c441e3bbf369d91c8470e98ff3f.jpg)  
Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a given power market, indicating critical tightness if below 15%. Not showing in the chart if above 100% (a very soft market).  
Source: Regional power ISOs and RTOs, EIA, Bloomberg, GS Global Investment Research

## Demand

## Aggregate Power Demand

Exhibit 8: Total US yoy power demand growth strengthens to $2.3\%$ in March, but still below the annual yoy growth rate of $2.4\%$ in 2025  
![](images/af37a60079237c5818e66cc8de7c3793f082a67a36d0c5f6aa0a76764a2e0d1b.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 9: After weather adjustment, US total power demand growth in Jan-Mar2026 was $1.2\%$ , also below last year's growth  
![](images/84b760673f903218b32c04d0eb5aceea954ac5835815dbb5ae6470c385bd98dc.jpg)  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 10: The commercial sector continues to be the strongest sector in power demand growth in Jan-Mar2026 with a $2.7\%$ yoy growth rate  
![](images/d5492a00368d668451b86fb6729bb229405627d50af138779ae83c48741badfc.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research  
Exhibit 11: After a weak start of the year in Jan2026, US residential power demand remained flattish yoy in Feb-Mar

![](images/3da694ddda0497cf13cf2b39055a4417efa629b76941b8d9d2ca6445c027e25d.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 12: Industrial power demand strengthened into March after Jan-Feb2026 yoy weakness  
![](images/346a3b205ee2994b145659aa9058c0fb3c7c61e8b52eaad5bd79102bd73d8395.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 13: US power demand growth remained below US GDP growth through Apr2026 Weather-adjusted US total power demand (including small-scale solar power use) and US real GDP yoy, monthly  
![](images/57d0776233a3a3e176a85409043ae37e8baf4f50e9bf1192c70f1e2f282a2e9e.jpg)  
To avoid underestimating power demand, we include all small-scale solar power generation in US total power demand  
Source: EIA, Bloomberg, Haver, GS Global Investment Research

## Data Center Power Demand

Exhibit 14: Estimated data center power demand in Virginia continued to edge higher  
![](images/07e92786bf926dff23e039832a2225ec017ac06d0bdd4a5bb576f655412e9c8c.jpg)  
Not weather adjusted  
Source: Haver, GS Global Investment Research

Exhibit 15: US data center capacity continued to grow, which we expect to accelerate in June and also in 2H2026  
![](images/6b1c91082ce9eedc28f80b5146ab9d22562fcceadbc0d3cad30df57d72ed7874.jpg)  
Source: Aterio, GS Global Investment Research

Exhibit 16: Texas and Virginia led data center expansions in the past year, along with Arizona, Indiana, Ohio and Georgia

YoY Data Center Capacity Additions Across US States  
![](images/dd789f4dcf91d82b5f2253faa3d5c0f19d9f805386c7f530310075e8b39dae04.jpg)  
Source: Aterio, GS Global Investment Research

Exhibit 17: Ohio, Texas, and Virginia are leading data center development in 2026Q2  
Data Center Capacity Additions Across US States in 2026Q2  
![](images/5cb0228835929fa7d17c31b7500c9194d1757a2053ad67c97d4dd81b239bc4ec.jpg)  
Source: Aterio, GS Global Investment Research

Exhibit 18: We expect significant data center growth acceleration in both the US national and key regional power markets in 2026/27  
![](images/963da2565e7851c38a30516f46e4081924b5852d280aa9744e756f61969df124.jpg)  
Source: Aterio, GS Global Investment Research  
Exhibit 19: Construction employment related to US data center expansion continued its growing trend

![](images/90f8bc473a1d9b76d9af7c36740f4cf4ba91e4f50cbc76b128362bd9b28d768b.jpg)  
Source: Haver, GS Global Investment Research

## Supply

## Generation and Stack

Exhibit 20: US total power generation stayed in line in most of May before gaining strength into early-summer  
![](images/ef46e5db392563636b239b5346aa96b5485455c3e328f1d5bbddc4fa3b0c2306.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 21: After adjusting for weather, US total power generation holds in line with early-summer year-ago levels  
![](images/57fbe89e1b17f1415cda0a3d4ec34dadc383a25a86554e944b09c2a7f4e4e35a.jpg)  
Source: EIA, Bloomberg, GS Global Investment Research

Source: EIA, GS Global Investment Research

Exhibit 22: The thermal (natural gas and coal) share in US power supply continues to increase from mid-April given yoy weaker hydro and nuclear  
![](images/d1414fb2f5bffb43f72aa071e10145ab4b75e6ab3118c1955228ecd99411fa99.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research  
Exhibit 23: Within thermal power generation, the natural gas share remained higher yoy given price competitiveness

![](images/f450376b1b30cb0700c7b8a3f88ab2df1d5163d3359d3d3e168e7a2478fdf8d5.jpg)  
Not weather adjusted

Exhibit 24: US power transmission and distribution losses continued to increase into 2026, though marginally lower in Apr/May  
![](images/332014f4fc4e47bf67319b81682a1ddc4b09aeee3fbf6430849e73a40317a350.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

## Generation by Fuels

Exhibit 25: YoY growth in natural gas-fired generation has moved sequentially lower June-to-date vs March and April but remains positive  
![](images/19c49822b6fa3f16834a01af61ab4ef77a997b55b8c562086022f7e252e54d3d.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 26: Higher gas competitiveness keeps coal power generation lower yoy most of the time from mid-Feb to Jun  
![](images/8142b1fa897b29b78bf166a31c33d4ef34af7e7754880476a36cd683599b9451.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 27: Nuclear power generation turns higher yoy into May and June following April maintenance  
![](images/d5829aa3dcad6ba18543826ef790a06a60c900d434a1e0269309371a7f781628.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 28: Wind generation moves higher yoy in May and June  
![](images/9352110195c734270a012ca5d8ff8ae795a11e58eb0c647fe7c607e9793d4813.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 29: Solar generation has continued to seasonally ramp up, driven by yoy capacity additions of over 30 GW  
![](images/431f80d368ed93a940a7ac62a37621f36e4eadb160d111d9dafe15d190754549.jpg)  
Source: EIA, GS Global Investment Research

Exhibit 30: Hydro power generation remains weak yoy due to droughts in more than half of the country  
![](images/77b3b2c21f1fc4085e3040fa6bc143fe4a2e0649e3d91e818fe32f9362e80483.jpg)  
Source: EIA, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Hongcen Wei, Laura Cyr, Daan Struyven and Samantha Dart, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Hongcen Wei GS & Co. LLC, Laura Cyr GS & Co. LLC, Daan Struyven GS & Co. LLC, Samantha Dart GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this r

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
