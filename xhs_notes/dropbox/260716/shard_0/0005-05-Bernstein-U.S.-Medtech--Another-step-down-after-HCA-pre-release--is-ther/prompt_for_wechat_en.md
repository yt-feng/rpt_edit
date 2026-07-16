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
U.S. Medical Devices

# U.S. Medtech: Another step down after HCA pre-release; is there any relief in sight for the sector?

![](images/6913073633ef76ed80780f341a66f419a19d15613a0b7ca3d7c85f9120cd1f16.jpg)

Lee Hambright

+1 917 344 8429

lee.hambright@bernsteinsg.com

![](images/12730f01cc5acc310703961db9951bf27857a7e0f973c535dcbd7356020d7d73.jpg)

Adam Chow

+1 212 845 7820

adam.chow@bernsteinsg.com

Specialist Sales

![](images/bf5a5416eae4147dcbac10e51e8df9aef9c977c95bde4f9c2960f7a94e3ca155.jpg)

Christian Moore

+1 917 344 8555

christian.moore@bernsteinsg.com

U.S. Medtech stocks took another punch yesterday, as HCA (covered by Lance Wilkes) pre-released 2Q26 revenue and highlighted a $2.3\%$ decline in same-facility inpatient surgery volumes and a $3.4\%$ decline in same-facility outpatient surgery volumes (see PR and Lance's take). HCA shares finished the day down $7\%$ , and several of our stocks were down almost as much (ISRG/SYK). JNJ reported mixed MedTech results this morning, which probably won't provide relief for medtech stocks after yesterday's weakness. We spoke to medtech management teams and offer thoughts on sector weakness below.

Investors are concerned, so the HCA announcement hit hard. U.S. Medtech stock performance has been abysmal. Our coverage has underperformed the S&P 500 by 5000bps over the past year (Exhibit 1), and the medtech sector multiple has compressed by over 30% since November (Exhibit 2). Given how bad medtech performance has been, investors naturally worry that something is fundamentally wrong with the sector. Concerns are focused around a few themes: slowing utilization growth, margin pressure, and (to a lesser extent) GLP-1 impact.

Hospital commentary has stoked fears that utilization growth could slow in 2H26, driven in part by declining enrollment in ACA plans and cuts to Medicaid. Recent alt data trends and survey work have not assuaged investor fears about the health of underlying medtech procedure volumes. With investors on edge, yesterday's announcement from HCA hit particularly hard, especially given the nature of the update—a couple of concerning numbers in a PR showing declines in inpatient and outpatient procedures with no public commentary from the company to put the numbers in context.

We have been on the road recently, and we have heard investor concerns loud and clear. We have defended the group, arguing that weakness has been more about single stock stories that have gotten more complicated than it is about a deteriorating macro environment (see our recent Deadtech forever? note). In a world where AI-related stories continue to command so much attention, investors have very little patience for complicated medtech stories.

Medtech management teams see healthy end markets. In our discussions with medtech companies, we do not hear concern about underlying market health. In fact, most companies point to continued steady/strong procedure volume growth. We caught up with ZBH yesterday, and they reiterated that (1) ACA is a LSD % of U.S. procedures, (2) Medicaid is LSD % of U.S. procedures, so (3) ACA and Medicaid together account for something at the low end of MSD % of U.S. procedures (say \~4%). Obviously, ACA and Medicaid programs are not going to zero, so ZBH felt the reaction to the HCA pre-release was overblown. The company wouldn't comment on Q2 procedures specifically, of course, but they characterized the market as "fine."

[continued on p2]

## DETAILS

## [continued from front page]

We also spoke with a private ortho company yesterday who hasn't noticed any change in market volume trends, and we connected with MDT who sees underlying markets as healthy and believes hospitals will push to do more elective procedures as hospital financials come under increased pressure.

No help from JNJ? This morning, JNJ reported 2Q26 MedTech sales of \$4.55bn in the U.S., which missed consensus by \~1.7% (\~\$80mn) on U.S. organic growth of 4.1%. Most of the U.S. weakness came from lower-than-expected Abiomed U.S. sales (\~\$60mn miss), which may be a JNJ-specific issue. U.S. Knees missed by 3% (\$6mn), and U.S. Spine missed by 1% (\$3mn), while U.S. Surgery was 1.5% ahead of expectations (+\$19mn). Outside the U.S., JNJ MedTech sales grew 3.2% organic to \$4.37bn, slightly ahead of consensus.

From the headline numbers and commentary in JNJ's Q2 earnings presentation, we do not see any flashing signs of a slowdown in U.S. procedure volumes, but these numbers probably will not provide any relief for medtech stocks. JNJ's weakness in cardiovascular may raise some eyebrows, and investors will not find comfort in JNJ's small misses in U.S. Knees and U.S. Spine. Medtech investors will be listening closely to JNJ's commentary about medtech market health.

What can get medtech going again? As of this morning, we have a hard time squaring HCA's declining Q2 procedure trend with the reassuring commentary we hear from medtech management teams regarding the health of underlying markets. At this point, we continue to believe medtech stock weakness is more about single stock stories that have gotten more complicated. Let's see what we hear from JNJ and from medtech management teams as they report Q2 results over the coming days and weeks.

Sadly, momentum has become an increasingly important factor driving medtech valuations. Medtech stocks that were loved in late 2024 at all-time-high valuations are now hated at 10-year-low valuations. We're not yet willing to concede that market health is deteriorating, but even if that turns out to be the case, there must be opportunity for investors at these valuations (see Exhibit 3). After all, these are quality companies operating in attractive oligopoly markets, medtech innovation continues at a rapid pace, and there are plenty of secular tailwinds that will continue to drive growth.

We forecast progressive recovery for the group as idiosyncratic risks are retired one by one. It doesn't look like medtech will get much help from JNJ's Q2 results. We don't expect to get much help from Abbott, either, but if ABT can show recovery in Nutrition and stabilization in Structural Heart, investors might start to get excited about broadening access for CGM and the growth opportunity in EP. Perhaps Intuitive Surgical's portfolio of launches (dV5, Ion, SP, XiR, AI) can continue to drive strong quarterly financial performance, and maybe investors will find it harder to ignore ISRG as estimates continue to march higher. Perhaps Stryker can deliver a healthy Q2 beat and restore confidence that the business will continue strong execution despite the cyberattack-related hiccup. Recovery for Boston Scientific would go a long way to restoring confidence in the group. Questions continue to swirl about decelerating growth for Watchman and EP. As we get clarity on when and where growth rates will bottom out for these key franchises, and as reset LRP expectations begin to come into focus, we see the potential for dramatic recovery over the next 12-24 months.

Bottom line: For investors who are willing to live with stories that have a bit of hair on them, we see very attractive risk/reward for many quality medtech names across our coverage. We believe ISRG is an incredible opportunity below \$400, and we like SYK going into Q2. We believe BSX shares have the potential to double over the next couple of years, though we admit it could take several quarters to get better visibility and rebuild investor confidence.

EXHIBIT 1: Over the last 12 months, U.S. Medtech has underperformed the S&P 500 (by 5000bps!) and has lagged all other healthcare subsectors  
US Healthcare Stock Performance  
![](images/d6bea622357808c304932cac095723bba27c2f490a242a75039735b7a028378e.jpg)  
Equal weight based on Bernstein large-cap US coverage by sector; US Medtech includes ABT, BSX, DXCM, EW, ISRG, MDT, PODD, SYK, ZBH Source: Bloomberg; Bernstein analysis (14-Jul-2026 close)

EXHIBIT 2: U.S. Medtech P/E multiples are down over 30% since November 2025. We haven't seen these levels sustainably since before 2017  
U.S. Medtech (S5HCEP\*) Price/Earnings Ratio (1BF)  
![](images/9ddf060e97cb66965aefd018cdc14cdc8028057d7ca48397ef8fa37952075a85.jpg)  
Source: Bloomberg; Bernstein analysis (14-Jul-2026 close)

EXHIBIT 3: For most of our coverage, multiples have been slashed by 20%-60% over the last 18 months
U.S. Medtech Valuation History - Absolute P/E and P/S Multiples

<table><tr><td>Ticker:</td><td>SPX</td><td>JNJ</td><td>MDT</td><td>EW</td><td>ZBH</td><td>DXCM</td><td>SYK</td><td>ABT</td><td>ISRG</td><td>PODD</td><td>TNDM</td><td>BSX</td></tr><tr><td>Metric:</td><td>P/E</td><td>P/E</td><td>P/E</td><td>P/E</td><td>P/E</td><td>P/S</td><td>P/E</td><td>P/E</td><td>P/E</td><td>P/S</td><td>P/S</td><td>P/E</td></tr><tr><td>Avg last 10yrs</td><td>19.2x</td><td>16.2x</td><td>17.2x</td><td>32.7x</td><td>15.1x</td><td>10.3x</td><td>24.0x</td><td>22.5x</td><td>49.0x</td><td>9.6x</td><td>5.0x</td><td>24.3x</td></tr><tr><td>Avg last 5yrs</td><td>20.0x</td><td>15.9x</td><td>16.1x</td><td>32.1x</td><td>14.4x</td><td>9.9x</td><td>25.5x</td><td>23.1x</td><td>54.7x</td><td>9.3x</td><td>3.3x</td><td>26.1x</td></tr><tr><td>12/31/2024</td><td>21.6x</td><td>13.6x</td><td>14.0x</td><td>30.3x</td><td>12.3x</td><td>6.6x</td><td>26.8x</td><td>21.9x</td><td>67.7x</td><td>7.5x</td><td>2.3x</td><td>31.9x</td></tr><tr><td>TODAY</td><td>20.2x</td><td>20.8x</td><td>13.1x</td><td>28.1x</td><td>10.4x</td><td>5.2x</td><td>19.6x</td><td>15.4x</td><td>34.1x</td><td>3.0x</td><td>0.9x</td><td>12.0x</td></tr><tr><td>vs Avg last 10yrs</td><td>6%</td><td>28%</td><td>-24%</td><td>-14%</td><td>-31%</td><td>-50%</td><td>-19%</td><td>-32%</td><td>-30%</td><td>-68%</td><td>-82%</td><td>-50%</td></tr><tr><td>vs Avg last 5yrs</td><td>1%</td><td>30%</td><td>-18%</td><td>-12%</td><td>-28%</td><td>-48%</td><td>-23%</td><td>-33%</td><td>-38%</td><td>-68%</td><td>-72%</td><td>-54%</td></tr><tr><td>vs 12/31/2024</td><td>-6%</td><td>53%</td><td>-6%</td><td>-7%</td><td>-16%</td><td>-22%</td><td>-27%</td><td>-30%</td><td>-50%</td><td>-60%</td><td>-60%</td><td>-62%</td></tr></table>

Source: Bloomberg; Bernstein analysis (14-Jul-2026 close)

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">14 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>ABT (Abbott)</td><td>O</td><td>USD</td><td>88.96</td><td>110.00</td><td>(52.7)%</td><td>USD</td><td>5.14</td><td>5.48</td><td>5.95</td><td>17.3</td><td>16.2</td><td>15.0</td></tr><tr><td>BSX (Boston Scientific)</td><td>O</td><td>USD</td><td>42.63</td><td>76.00</td><td>(79.1)%</td><td>USD</td><td>3.06</td><td>3.35</td><td>3.70</td><td>13.9</td><td>12.7</td><td>11.5</td></tr><tr><td>DXCM (DexCom)</td><td>O</td><td>USD</td><td>74.12</td><td>77.00</td><td>(32.9)%</td><td>USD</td><td>2.09</td><td>2.56</td><td>3.13</td><td>35.4</td><td>28.9</td><td>23.7</td></tr><tr><td>EW (Edwards)</td><td>M</td><td>USD</td><td>90.09</td><td>96.00</td><td>(3.1)%</td><td>USD</td><td>2.56</td><td>3.00</td><td>3.32</td><td>35.2</td><td>30.0</td><td>27.1</td></tr><tr><td>PODD (Insulet)</td><td>O</td><td>USD</td><td>159.12</td><td>200.00</td><td>(65.5)%</td><td>USD</td><td>4.97</td><td>6.59</td><td>8.28</td><td>32.0</td><td>24.1</td><td>19.2</td></tr><tr><td>ISRG (Intuitive Surgical)</td><td>O</td><td>USD</td><td>379.50</td><td>750.00</td><td>(46.3)%</td><td>USD</td><td>8.93</td><td>10.54</td><td>12.23</td><td>42.5</td><td>36.0</td><td>31.0</td></tr><tr><td>JNJ (J&amp;J)</td><td>M</td><td>USD</td><td>253.85</td><td>251.00</td><td>43.3%</td><td>USD</td><td>10.75</td><td>11.54</td><td>12.62</td><td>23.6</td><td>22.0</td><td>20.1</td></tr><tr><td>MDLN (Medline)</td><td>O</td><td>USD</td><td>38.66</td><td>54.00</td><td>NA</td><td>USD</td><td>0.01</td><td>1.50</td><td>1.68</td><td>N/M</td><td>25.8</td><td>23.0</td></tr><tr><td>SYK (Stryker)</td><td>O</td><td>USD</td><td>311.07</td><td>410.00</td><td>(40.7)%</td><td>USD</td><td>13.66</td><td>14.98</td><td>16.72</td><td>22.8</td><td>20.8</td><td>18.6</td></tr><tr><td>ZBH (Zimmer Biomet)</td><td>M</td><td>USD</td><td>91.03</td><td>91.00</td><td>(23.5)%</td><td>USD</td><td>8.22</td><td>8.50</td><td>8.95</td><td>11.1</td><td>10.7</td><td>10.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,543.59</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures:

Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of othe

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
