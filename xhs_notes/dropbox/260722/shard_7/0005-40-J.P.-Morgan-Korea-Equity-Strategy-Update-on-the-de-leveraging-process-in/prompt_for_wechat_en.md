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
## Korea Equity Strategy

Update on the de-leveraging process in Korea

While the fundamentals of the Korea market remain on solid ground (despite some concerns – see below), an intense period of de-leveraging has driven equity prices lower. The KOSPI index is now down a sizable -28% from the peak on 22 June in a highly volatile move. What was triggered by routine fundamental concerns and rotational flow, was amplified by leveraged ETFs, and in recent days increasingly has the hallmarks of hedge fund positioning unwind (especially given the -30% Price Momentum factor drawdown). The rapid pace of gains in the Korea market over the past year made it an inevitable destination of leverage - from retail investors, equity L/S hedge funds as well as macro funds - compounding these gains. As we have noted for the past 6-7 weeks now (see here, here), some of the side effects of this growth have been the elevated volatility and forced foreign selling - producing a self-correcting mechanism. In the near term, our focus remains on the extent of normalization in these conditions (we estimate leveraged ETF unwind to be 75% through and equity H/F de-leveraging >50% through). Stepping back, though, our view remains that the fundamental strength in the market remains good for several years ahead (a combination of global AI spend, security/resilience spend, wealth effect across corporates/households/government and structural governance improvements), meaning that the market should be able to overcome positioning unwinds and persevere with the positive trend. We remain OW Korea in our regional allocations and our 12m-out base case KOSPI target remains 12,500.

\- Extent of leverage “normalization”: Of all the leverage channels in Korea, we see (1) futures & options largely an institutional market with limited signs of speculative excess, and (2) retail leverage via margin and bank loans as relatively modest (down a lot in KOSDAQ though). The issues around (3) swap capacity (globally rising funding costs compounded by Korea-specific capital constraints and concentration issues) and (4) volatility from outstanding leveraged ETFs – both remain but have materially eased (tactically, because the market is lower, and structurally, because the underlying issues are being addressed). We estimate leveraged ETF unwind to be 75% through (to an acceptable level of \~\$18bn) and equity H/F deleveraging more than 50% through (assuming L/S ratios reach the upper end of 2025’s range).

\- Leveraged ETFs: Leveraged ETFs with Korea underlyings grew to \$50bn in AUM (mostly due to the growth of the market) by late June. Relative to its market size, this was 4x larger than the US and led to very pronounced volatility (and forced de-leveraging on down-days) - the VKOSPI to VIX ratio is sill closer to 5x vs the usual 1x. Not only does this detract from vol-sensitive inflows, but it makes vol-based risk-management harder for asset managers and securities companies. Over Jun and July we have seen this excessive volatility compound the modest AI jitters seen elsewhere in global AI hardware stocks. Similar to previous deleveraging of leveraged products (Nikkei in 2015, Nasdaq in 2022, Oil in 2020, and most famously - even if somewhat differently - the inverse VIX products in 2018), this period of volatility has shrunk leveraged ETFs with Korea underlyings now to \$26bn. With new regulations aimed at keeping tighter checks on the growth of this space (minimum deposit requirement raised to KRW30mn from KRW10mn from

Equity Macro Research

Mixo Das AC (852) 2800-0511  
mixo.das@JPM.com  
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Stanley Yang  
(82-2) 758-5712  
stanley.yang@JPM.com  
JPM Securities (Far East) Limited, Seoul Branch

Rajiv Batra  
(65) 6882-8151  
rajiv.j.batra@JPM.com  
JPM Securities Singapore Private Limited

Joy Wang  
(852) 2800-2322  
joy.y.wang@JPM.com  
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 8 for analyst certification and important disclosures, including non-US analyst disclosures.

Aug 5 $^{th}$ , only cash will be recognized as the initial margin from Aug 19 $^{th}$ , new listings of single-stock levered ETF products are temporarily halted, minimum trading unit for single-stock leveraged products will be raised from 1 share to 20 shares starting in Nov), further moderation in size is likely ahead.

\- HF leverage and swap capacity: Swap capacity limits (for investors to access Korea equities via brokers) have been tightening for a while - faced with rapidly rising interest from global equity and macro investors (gross and net exposure towards Korea in the JPM Prime book have risen rapidly since April). This is partly a global story, where higher demand for financing (due to growth in markets and shift in AUM mix to higher leveraged entities) and tightening regulations having driven funding rates higher. It is also partly a Korea story, given the higher capital needed to match higher trading volumes (6-7x over the past year) and difficulty in managing concentration risks of investors unanimously preferring positions in the memory space. With the decline in market size and underperformance of memory names, though, this capacity tightness has eased substantially (a full normalization is still some distance away as brokers and investors work through these constraints). Similarly, in the present de-leveraging process, L/S ratios in the JPM Prime book have declined from highs of $>5.5\mathrm{x}$ to now $<4\mathrm{x}$ .

\- Retail leverage and margins: Margin balances have declined somewhat from a high of >\$25bn to \~\$21bn now. Notably, most of the declines and margin calls have been in smaller-cap KOSDAQ market, and not in KOSPI. But at \$21bn, this is just 0.5% of equity market cap (vs 1.9% of market cap in the US and 2.8% in China A-shares). In addition, unlike leveraged ETFs that undergo a process of forced de-leveraging on any spot price declines, margin lending comes with buffers and discretion. Korean retail investors still have ample equity gains, cash balances, higher incomes and overseas assets to tap into to absorb any margin calls should they want to keep the position. We are thus less concerned about margin calls and de-leveraging through this channel becoming a systemic problem.

\- Record foreign outflows are slowing: There has been >\$110bn of foreign outflows from Korea YTD - which would handily break the record of annual outflows from any market in Asia. The two memory names had become so large that they started to hit mandate limits for EM investors - which we estimated to be affecting roughly 10% of the foreign ownership in both stocks in 2Q. This forced investors to sell on rallies. Indeed, \~90% of YTD foreign outflows from Korea come from the memory names alone. This selling pressure has eased tactically as Korea (and particularly the memory names) has underperformed, meaning that the two heavyweights are now only 7.5% and 5.7% weights in MSCI EM (vs 9.5% and 8.3% in late June).

\- Fundamentals: We remain bullish on the AI cycle and related fundamentals. Earnings growth rate in Korea will slow from the scorching pace of 2026, but the question in Korea now is less about growth and more about sustainability (how much visibility can we have about higher earnings levels). While monetization at the model layer is being questioned again (with very positive reception to open-source models), at the hyperscaler layer the rental economics for data centers remain very positive. This means that hyperscalers should keep spending up. All our indicators on this are currently green across model capability, funding availability and rental rates. And external risks (like regulation, recession, etc.) don’t look imminent. Memory demand has been questioned recently with reported technological and process breakthroughs reducing memory demand – but we are yet to see this in reality. And in terms of supply, the supply of memory equity should not be conflated with supply of physical memory. Outside of AI, there are earnings tailwinds from growth in a variety of (AI-adjacent and other) Industrials, potential wealth-effect boost to Financials and Consumer, and ongoing (if incremental) valuation tailwinds from the governance reforms (which will likely come back to prominence later this year).

Figure 1: KOSPI index has declined $-29\%$ from the peak of 22 Jun  
![](images/97bfff5d72c608a0f287a2109a73c0563e3121699e423a70eef0640a179036b5.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 2: Bringing the index RSI to lowest levels since the start of this rally post Liberation Day in 2025  
![](images/4b78bf52af8a754f88e475038e31616b8806d19d68357ce034d97614ed287e60.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 3: Korea is still the best performing market in the region YTD in USD terms  
![](images/e4a14f97f531dd2e443f85451ce96e75e137648ffc32878df8d2f06de83eed57.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 4: KOSPI has largely been a reflection of memory upside in recent months  
![](images/7a8923e25ba17384aa5df37964ee5745f34e7e6c495e5368563e13779c90b4f7.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 5: Margin balances and leveraged products are the primary channels for retail investors to access leveraged upside - in Korea margin balances are very acceptable, but leveraged ETFs outstanding are still large

<table><tr><td>$bn</td><td>Market cap</td><td>Margin balances</td><td>% of Mcap</td><td>Leveraged ETFs outstanding</td><td>% of Mcap</td></tr><tr><td>US</td><td>80000</td><td>1502</td><td>1.9%</td><td>250</td><td>0.3%</td></tr><tr><td>Korea</td><td>4000</td><td>21</td><td>0.5%</td><td>26</td><td>0.7%</td></tr><tr><td>Japan</td><td>8800</td><td>43</td><td>0.5%</td><td>5</td><td>0.1%</td></tr><tr><td>China A</td><td>15000</td><td>422</td><td>2.8%</td><td>1</td><td>0.0%</td></tr><tr><td>Taiwan</td><td>5000</td><td>19</td><td>0.4%</td><td>8</td><td>0.2%</td></tr></table>

Source: Bloomberg Finance L.P., FINRA, KOFIA, JPX, JPM Equity Macro Research.

Figure 6: For retail investors, margin leverage is not too high (and falling vs market cap)  
![](images/0f913d87ae2be07d2b67b7471959766b2d7816cedd1dbdee2d0a3fe8643d3c9a.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 8: In terms of leveraged ETFs, their AUM has declined from highs of \$50bn to now \$26bn  
![](images/d3e32e2dda2804005044a4e554b877b272ca8c03edb9290135bcca166d7d6735.jpg)

Figure 7: Similarly there is little evidence at the aggregate level that Korean households are borrowing from banks to invest in equities loans to households %y-y. Data as of April 2026  
![](images/b46ad7cb234095a6b986b096bac0511481855415529be72713c0d347006ad384.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 9: To be sure, much of this is simply due to the decline in the market, as flows have continued to actually be positive
cumulative inflows, USD mn  
![](images/15a8e7fd0a37266ce24545b9e13f91ad9c28f3ad1958b221aaa75f26ac4fb750.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 10: Largely as a result of leveraged ETF hedging, volatility in Korea has notably disconnected from volatility elsewhere - and yet to normalize  
X  
![](images/27e95acd2d1ab58341b1a4727df5ae2c5e8e41ecc801f5ee5b349d0ef04dc103.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 12: Separately, Korean equities have seen >\$110bn of outflows YTD, but most of this is due to mandate constraints for LOs on owning large-caps

cumulative flow, \$mn, KRX data

![](images/c8e4992ffe0bb130e893d50fca8067f545e7dc9ddab5de48ad5077199adeff04.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.  
Figure 11: The open interest of single stock futures (implementation channel of the leveraged ETFs) has started to decline now USD mn  
cumulative flow, \$mn

![](images/505bfbf5ce804a49f4e9eff64a7b39b9177d18c2065ada00a5af3fc9610317b0.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 13: Indeed, $90\%$ of the outflow is from the two memory names. The decline in EM index weights of these stocks has substantially slowed outflows

![](images/d74474c117ed1817b0a88b1752d298e0581a708862b665b89b533ceeb57a1413.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 18: Price momentum factor has seen a deep drawdown in recent weeks - similar to US, Japan etc indicative performance of L/S quintiles

Figure 14: L/S ratios for hedge funds in the JPM Prime book has declined from highs, but not fully normalized  
![](images/5b52e97a78650e70bd6dbd254d1312840a07c9d981a2f6d1bbf688c342442d1d.jpg)  
Source: Bloomberg Finance L.P., JPM Positioning Intelligence.

Figure 15: EM LO investors have become more UW Korea YTD as mandate constraints bite  
weightings relative to the MSCI benchmark and net OW/UW  
![](images/65e126524cb87298b78394513d34eb4df8d01f855498b8aef8c1d5e6e843a4ee.jpg)  
Source: Bloomberg Finance L.P., EPFR, MSCI, JPM Equity Macro Research.

Figure 16: Retail investors have been the main buyers of Korean equities - sentiment about equities and leverage is still strong KRW bn, KRX data  
![](images/133e97636985b058725453251c75514c48896c7945e3bb7706aa4f3315f23887.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 17: Since the beginning of June, most purchased overseas stocks by Korean retail investors include several leveraged products \$bn  
![](images/e4c223bde643cdd8e559c2679b7d114e594b084dba2e956dd620fc06552b037b.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

<table><tr><td></td><td>Px Momentum</td><td>EPS revision</td><td>Growth</td><td>Quality</td><td>Value</td><td>Low Vol</td></tr><tr><td>Week ending 03-Jul</td><td>-10.8%</td><td>-4.9%</td><td>-0.8%</td><td>3.3%</td><td>0.9%</td><td>8.7%</td></tr><tr><td>Week ending 10-Jul</td><td>-7.9%</td><td>-3.1%</td><td>-2.1%</td><td>0.8%</td><td>5.6%</td><td>7.9%</td></tr><tr><td>Week ending 17-Jul</td><td>-6.3%</td><td>-3.0%</td><td>0.6%</td><td>1.9%</td><td>1.3%</td><td>7.0%</td></tr><tr><td>Week ending 24-Jul</td><td>-1.7%</td><td>0.4%</td><td>-1.0%</td><td>-0.2%</td><td>1.3%</td><td>3.4%</td></tr></table>

Figure 19: Momentum crowding is now starting to come off  
![](images/27e33f927e6448f4036a2803c67ea2d9ee6e6f692648c934aaec4c77dc44f531.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 20: Drawdown in Price Momentum factor still leaves strong YTD performance

indicative performance of L/S quintile - log scale

![](images/4a9f1e5da43a05bc8de20c1d4aa531693eea7077c4f0c6d8361ff02ce8d47e34.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 21: 3Q tends to be reasonably strong seasonally for Price Momentum factor performance in Korea - 4Q is more challenging Average performance over past five years  
![](images/4e94cd57382fa67ffe79d035ec671f57bf672589887d4ea41371a6906072c405.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 22: Korea sector EPS revisions remain strong as earnings get underway

<table><tr><td rowspan="2"></td><td colspan="3">2026 EPS</td><td colspan="3">2027 EPS</td></tr><tr><td>1m</td><td>3m</td><td>6m</td><td>1m</td><td>3m</td><td>6m</td></tr><tr><td>Market</td><td>7.8%</td><td>35.5%</td><td>143.4%</td><td>12.2%</td><td>53.7%</td><td>199.8%</td></tr><tr><td>Tech</td><td>8.5%</td><td>42.2%</td><td>215.5%</td><td>13.1%</td><td>63.1%</td><td>303.3%</td></tr><tr><td>Financials</td><td>1.7%</td><td>5.7%</td><td>9.8%</td><td>2.3%</td><td>6.5%</td><td>11.1%</td></tr><tr><td>Industrials</td><td>11.8%</td><td>42.6%</td><td>91.0%</td><td>18.1%</td><td>59.4%</td><td>108.6%</td></tr><tr><td>Discretionary</td><td>0.5%</td><td>-4.5%</td><td>-8.9%</td><td>0.8%</td><td>-3.3%</td><td>-6.8%</td></tr><tr><td>Materials</td><td>-5.8%</td><td>-9.0%</td><td>-13.9%</td><td>-2.3%</td><td>-1.2%</td><td>1.4%</td></tr><tr><td>Staples</td><td>3.0%</td><td>7.5%</td><td>11.7%</td><td>3.2%</td><td>8.2%</td><td>12.8%</td></tr><tr><td>Healthcare</td><td>0.6%</td><td>-3.2%</td><td>1.6%</td><td>0.9%</td><td>-6.3%</td><td>-3.0%</td></tr><tr><td>Comm Serv</td><td>-0.9%</td><td>-5.4%</td><td>-10.0%</td><td>-0.2%</td><td>0.1%</td><td>-4.5%</td></tr><tr><td>Energy</td><td>-4.5%</td><td>92.5%</td><td>127.7%</td><td>1.0%</td><td>34.2%</td><td>52.6%</td></tr></table>

Source: Refinitiv, JPM Equity Macro Research.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-cover

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 21 Jul 2026 03:22 AM HKT

Disseminated 21 Jul 2026 03:22 AM HKT
"""
