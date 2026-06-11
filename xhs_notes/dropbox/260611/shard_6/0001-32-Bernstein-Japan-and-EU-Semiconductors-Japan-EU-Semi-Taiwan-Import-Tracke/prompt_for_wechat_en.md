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
# Japan and EU Semiconductors

# Japan/EU Semi Taiwan Import Tracker (May 26): SPE import +23% YoY

![](images/d4a63f3515508c008b61e01e3c8d9882f8829fafca46fe4fd14aca830bf14990.jpg)

David Dai, CFA

+852 2918 5704

david.dai@bernsteinsg.com

![](images/44b5d3a847658ce66f5f3cec420ac53f176f6a6008bd67fe207f102ef7798bb6.jpg)

Juho Hwang

+852 2123 2632

juho.hwang@bernsteinsg.com

![](images/c7889228730677d85a754cd07e5d8440cbb6f69c13a9608453cf0f6049bc3f29.jpg)

Carmine Milano, CFA

+44 20 7762 1857

carmine.milano@bernsteinsg.com

![](images/ebbc82df3c5f7900fb7774769ed175a013dd3a732203544f1e2763d1df8aa90e.jpg)

Jack Lin

+852 2123 2683

jack.lin@bernsteinsg.com

MOF Taiwan released May 2026 semiconductor equipment import data on June 10 $^{th}$ . We have extracted and analyzed relevant information that has strong significance for our coverage companies. The relevant Taiwan SPE import data can be downloaded here: Taiwan SPE Import.

SPE import +23% YoY, -8% MoM. Overall, Taiwan semi equipment imports YoY in May was +23% globally / +6% from Japan. MoM shows another slight decline from April — globally -8% and -17% from Japan. 3-month moving average is up +10% for global, and +6% for Japan SPE. The strong capex from Taiwan foundry continues to drive strong YoY growth, which supports our positive view on Japan / EU SPE.

MoM increase in Tester import. Advantest SoC tester revenue is highly correlated to the Taiwan tester import data which was up +7% MoM, and +34% YoY. 3-month average was +4% MoM. Our regression analysis suggests +6% QoQ for Advantest Taiwan sales with 2-month data, which suggests slight upside to consensus JunQ revenue of +3% QoQ.

TW litho imports were €543mn in May, down 38% MoM but up 21% YoY (vs May 2025). On a quarterly basis, imports in the first two months of the quarter (April and May) were up \~80% QoQ. This was largely driven by the very strong April import, the third-highest monthly level on record, especially given the first month of the quarter is typically seasonally weaker. Our regression based on 2-month imports estimates TW quarterly system sales for ASML of €2.33bn, rising 61% QoQ and 19% YoY. This implies that Taiwan will account for 37% of the overall system sales. Taiwan lithography demand appears to be gaining momentum as TSMC's capacity expansion progresses

Another MoM decline for TEL. The Taiwan import data for the relevant categories to TEL (CVD, dry etching, cleaning, coater & developer, RTP, etc.) suggests a weak May for TEL's Taiwan revenue. May single-month was down -19% MoM, and up +7% YoY; 3-month moving average was +3% sequentially. Our regression suggests -24% QoQ for TEL's JunQ Taiwan revenue with a downside to consensus of flat QoQ.

Cleaning equipment recovers. Taiwan cleaner import data is +11% MoM and +14% YoY. 3-month moving average is +14% sequentially. Our regression suggests -11% QoQ for Screen's JunQ Taiwan revenue, in-line with consensus.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">10 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>6857.JP (Advantest)</td><td>O</td><td>JPY</td><td>25,235</td><td>39,200</td><td>161.6%</td><td>JPY</td><td>534.21</td><td>735.65</td><td>870.09</td><td>47.2</td><td>34.3</td><td>29.0</td></tr><tr><td>ASML (ASML)</td><td>O</td><td>USD</td><td>1,777.77</td><td>1,971.00</td><td>103.5%</td><td>USD</td><td>27.95</td><td>36.96</td><td>53.13</td><td>55.2</td><td>41.7</td><td>29.0</td></tr><tr><td>ASML.NA (ASML)</td><td>O</td><td>EUR</td><td>1,508.40</td><td>1,700.00</td><td>107.4%</td><td>EUR</td><td>24.72</td><td>32.69</td><td>46.98</td><td>61.0</td><td>46.1</td><td>32.1</td></tr><tr><td>8035.JP (Tokyo Electron)</td><td>O</td><td>JPY</td><td>61,830</td><td>59,200</td><td>118.2%</td><td>JPY</td><td>1,250.88</td><td>1,504.14</td><td>1,848.77</td><td>49.4</td><td>41.1</td><td>33.4</td></tr><tr><td>7735.JP (Screen)</td><td>M</td><td>JPY</td><td>12,980</td><td>12,600</td><td>100.2%</td><td>JPY</td><td>486.61</td><td>572.60</td><td>662.24</td><td>26.7</td><td>22.7</td><td>19.6</td></tr><tr><td>JPL</td><td></td><td></td><td>2,555.22</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,386.65</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,533.88</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Advantest (PT=¥39,200), Tokyo Electron (PT=¥59,200), and ASML (PT=€1,700.00) Outperform.

We rate Screen (PT=¥12,600) Market-Perform.

## DETAILS

## TAIWAN SEMI EQUIPMENT IMPORT OVERALL

- Taiwan semi equipment import in May 2026 declined MoM once again from an exceptionally strong March but still continued strength, with YoY growth of +23% globally / +6% YoY from Japan; MoM was -10% globally and -16% from Japan (Exhibit 1, Exhibit 2).  
• 3-month moving average MoM was up +13% globally and +13% from Japan.

EXHIBIT 1: May Taiwan import for SPE was \$4.4bn, -8% MoM.  
![](images/fbcbb28d9c1af88177d0dbf837a9e311e49bd7492d958519230f919fc0eef636.jpg)

<details>
<summary>line chart</summary>

| Date    | Global SPE | 3 per. Mov. Avg. (Global SPE) |
|---------|------------|-------------------------------|
| Jan-16  | ~1,000     | ~1,000                        |
| May-16  | ~1,800     | ~1,700                        |
| Sep-16  | ~2,200     | ~1,900                        |
| Jan-17  | ~1,800     | ~1,800                        |
| May-17  | ~1,500     | ~1,400                        |
| Sep-17  | ~1,600     | ~1,300                        |
| Jan-18  | ~1,500     | ~1,400                        |
| May-18  | ~1,400     | ~1,300                        |
| Sep-18  | ~1,700     | ~1,500                        |
| Jan-19  | ~1,500     | ~1,400                        |
| May-19  | ~2,700     | ~2,500                        |
| Sep-19  | ~2,500     | ~2,300                        |
| Jan-20  | ~3,900     | ~2,900                        |
| May-20  | ~2,200     | ~2,000                        |
| Sep-20  | ~2,300     | ~2,100                        |
| Jan-21  | ~3,100     | ~2,700                        |
| May-21  | ~3,700     | ~3,400                        |
| Sep-21  | ~3,300     | ~3,200                        |
| Jan-22  | ~3,500     | ~3,400                        |
| May-22  | ~3,600     | ~3,500                        |
| Sep-22  | ~3,900     | ~3,700                        |
| Jan-23  | ~3,800     | ~3,600                        |
| May-23  | ~2,500     | ~2,300                        |
| Sep-23  | ~1,400     | ~1,300                        |
| Jan-24  | ~2,500     | ~2,300                        |
| May-24  | ~2,400     | ~2,200                        |
| Sep-24  | ~2,600     | ~2,400                        |
| Jan-25  | ~4,300     | ~3,800                        |
| May-25  | ~4,100     | ~3,700                        |
| Sep-25  | ~3,900     | ~3,600                        |
| Jan-26  | ~3,100     | ~3,400                        |
| May-26  | ~5,300     | ~4,800                        |
</details>

Source: Customs Administration of Taiwan, Bernstein analysis

EXHIBIT 2: Likewise, May Taiwan SPE import from Japan was \$700mn, -17% MoM.  
![](images/3e5f1a60a8f5c01160483505c0b208b863bbd9072ae9daa754efbec657d5402d.jpg)

<details>
<summary>line chart</summary>

| Date    | Japan SPE | 3 per. Mov. Avg. (Japan SPE) |
|---------|-----------|------------------------------|
| Jan-16  | ~350      | ~300                         |
| May-16  | ~500      | ~450                         |
| Sep-16  | ~650      | ~600                         |
| Jan-17  | ~500      | ~450                         |
| May-17  | ~400      | ~350                         |
| Sep-17  | ~350      | ~300                         |
| Jan-18  | ~400      | ~350                         |
| May-18  | ~450      | ~400                         |
| Sep-18  | ~400      | ~350                         |
| Jan-19  | ~450      | ~400                         |
| May-19  | ~800      | ~550                         |
| Sep-19  | ~400      | ~350                         |
| Jan-20  | ~600      | ~550                         |
| May-20  | ~800      | ~650                         |
| Sep-20  | ~400      | ~350                         |
| Jan-21  | ~650      | ~550                         |
| May-21  | ~700      | ~600                         |
| Sep-21  | ~950      | ~750                         |
| Jan-22  | ~850      | ~700                         |
| May-22  | ~750      | ~650                         |
| Sep-22  | ~780      | ~720                         |
| Jan-23  | ~750      | ~700                         |
| May-23  | ~650      | ~600                         |
| Sep-23  | ~400      | ~350                         |
| Jan-24  | ~350      | ~300                         |
| May-24  | ~550      | ~450                         |
| Sep-24  | ~800      | ~650                         |
| Jan-25  | ~1000     | ~800                         |
| May-25  | ~800      | ~750                         |
| Sep-25  | ~650      | ~600                         |
| Jan-26  | ~800      | ~750                         |
| May-26  | ~1000     | ~850                         |
</details>

Source: Customs Administration of Taiwan, Bernstein analysis

## ADVANTEST – TAIWAN TESTER IMPORT DATA

- Advantest SoC tester revenue is highly correlated to the Taiwan tester import (Exhibit 4). TW import of testers in May from Japan and Malaysia was collectively +7% MoM and +34% YoY. 3-month average data is +4% MoM (Exhibit 3).  
- Our regression indicates a JunQ Taiwan sales for Advantest of +6% QoQ (Exhibit 5, Exhibit 6), with slight upside vs. consensus JunQ revenue of +3% QoQ.

EXHIBIT 3: May tester import from Japan and Malaysia collectively was \$613mn, +7% MoM.  
![](images/d56e2e0c3b58dd97455c2829f89fed6fa4da11ff6ecee760fea8488fc3f28b5c.jpg)

<details>
<summary>line chart</summary>

| Date    | Testers (Japan/Malaysia) | 3 per. Mov. Avg. (Testers (Japan/Malaysia)) |
|---------|--------------------------|---------------------------------------------|
| Jan-16  | ~50                      | ~60                                         |
| May-16  | ~100                     | ~90                                         |
| Sep-16  | ~70                      | ~80                                         |
| Jan-17  | ~80                      | ~70                                         |
| May-17  | ~90                      | ~80                                         |
| Sep-17  | ~100                     | ~90                                         |
| Jan-18  | ~110                     | ~100                                        |
| May-18  | ~150                     | ~140                                        |
| Sep-18  | ~130                     | ~120                                        |
| Jan-19  | ~120                     | ~110                                        |
| May-19  | ~140                     | ~130                                        |
| Sep-19  | ~150                     | ~140                                        |
| Jan-20  | ~130                     | ~120                                        |
| May-20  | ~160                     | ~150                                        |
| Sep-20  | ~140                     | ~130                                        |
| Jan-21  | ~170                     | ~160                                        |
| May-21  | ~150                     | ~140                                        |
| Sep-21  | ~180                     | ~170                                        |
| Jan-22  | ~160                     | ~150                                        |
| May-22  | ~190                     | ~180                                        |
| Sep-22  | ~170                     | ~160                                        |
| Jan-23  | ~150                     | ~140                                        |
| May-23  | ~180                     | ~170                                        |
| Sep-23  | ~160                     | ~150                                        |
| Jan-24  | ~190                     | ~200                                        |
| May-24  | ~250                     | ~240                                        |
| Sep-24  | ~330                     | ~320                                        |
| Jan-25  | ~450                     | ~440                                        |
| May-25  | ~600                     | ~580                                        |
| Sep-25  | ~550                     | ~530                                        |
| Jan-26  | ~750                     | ~730                                        |
| May-26  | ~650                     | ~630                                        |
</details>

Source: Customs Administration of Taiwan, Bernstein analysis

EXHIBIT 4: Taiwan tester imports data shows good directional correlation with Advantest's Taiwan sales.  
![](images/139aecf8993ae5670be21cbe839ad466a791f86b8c55bb13571d101486344aba.jpg)

<details>
<summary>line chart</summary>

| Date   | Advantest Taiwan Revenue (Quarterly/3) (JPY bn) | Monthly Taiwan Import (JPY bn) |
|--------|--------------------------------------------------|-------------------------------|
| Jan-16 | ~5                                               | ~5                            |
| Apr-16 | ~5                                               | ~7                            |
| Jul-16 | ~4                                               | ~5                            |
| Oct-16 | ~3                                               | ~5                            |
| Jan-17 | ~4                                               | ~6                            |
| Apr-17 | ~5                                               | ~7                            |
| Jul-17 | ~5                                               | ~6                            |
| Oct-17 | ~6                                               | ~8                            |
| Jan-18 | ~7                                               | ~9                            |
| Apr-18 | ~8                                               | ~10                           |
| Jul-18 | ~9                                               | ~11                           |
| Oct-18 | ~10                                              | ~10                           |
| Jan-19 | ~8                                               | ~7                            |
| Apr-19 | ~9                                               | ~10                           |
| Jul-19 | ~10                                              | ~11                           |
| Oct-19 | ~8                                               | ~9                            |
| Jan-20 | ~5                                               | ~7                            |
| Apr-20 | ~6                                               | ~10                           |
| Jul-20 | ~7                                               | ~11                           |
| Oct-20 | ~8                                               | ~10                           |
| Jan-21 | ~9                                               | ~12                           |
| Apr-21 | ~10                                              | ~13                           |
| Jul-21 | ~10                                              | ~12                           |
| Oct-21 | ~11                                              | ~13                           |
| Jan-22 | ~12                                              | ~14                           |
| Apr-22 | ~13                                              | ~15                           |
| Jul-22 | ~14                                              | ~16                           |
| Oct-22 | ~13                                              | ~15                           |
| Jan-23 | ~12                                              | ~18                           |
| Apr-23 | ~10                                              | ~10                           |
| Jul-23 | ~8                                               | ~8                            |
| Oct-23 | ~10                                              | ~10                           |
| Jan-24 | ~8                                               | ~8                            |
| Apr-24 | ~10                                              | ~10                           |
| Jul-24 | ~15                                              | ~15                           |
| Oct-24 | ~20                                              | ~20                           |
| Jan-25 | ~45                                              | ~40                           |
| Apr-25 | ~55                                              | ~50                           |
| Jul-25 | ~35                                              | ~55                           |
| Oct-25 | ~30                                              | ~40                           |
| Jan-26 | ~60                                              | ~80                           |
| Apr-26 | ~65                                              | ~90                           |
</details>

Source: Company disclosures, Customs Administration of Taiwan, Bernstein estimates and analysis

EXHIBIT 5: Our regression analysis indicates JunQ Taiwan sales of +6% QoQ for Advantest.

<table><tr><td rowspan="2"></td><td colspan="2">Revenue (JPY bn)</td><td rowspan="2">QoQ</td></tr><tr><td>4QFY26(1QCY26)</td><td>1QFY27E(2QCY26E)</td></tr><tr><td>Taiwan Sales</td><td>189</td><td>199</td><td>6%</td></tr><tr><td>Total Sales</td><td>328</td><td></td><td></td></tr><tr><td>Bernstein</td><td></td><td>346</td><td>5%</td></tr><tr><td>Consensus</td><td></td><td>337</td><td>3%</td></tr><tr><td>Taiwan %</td><td>58%</td><td></td><td></td></tr><tr><td>Bernstein</td><td></td><td>58%</td><td>0%</td></tr><tr><td>Consensus</td><td></td><td>59%</td><td>2%</td></tr></table>

Source: Company disclosures, Bloomberg, Customs Administration of Taiwan, Bernstein estimates and analysis

EXHIBIT 6: Advantest Taiwan sales show good correlation with Taiwan imp

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
