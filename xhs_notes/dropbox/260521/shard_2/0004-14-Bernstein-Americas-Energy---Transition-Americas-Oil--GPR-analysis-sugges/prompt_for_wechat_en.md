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
# Americas Energy & Transition

# Americas Oil: GPR analysis suggests oil price is stickier than expected

![](images/122683b6ed92c6c75c072db5c9f08c109b710dcb405bd667052b91a4c4cc8886.jpg)

Bob Brackett, Ph.D.

+1 917 344 8422

bob.brackett@bernsteinsg.com

![](images/8de9192edfdbc5cb6726da1e3a6a65a5bac41e87303645c9f6f7053068e2b0fd.jpg)

Minnie Xu

+1 917 344 8574

minnie.xu@bernsteinsg.com

![](images/c8a65bd14dacfe0c6d371f3b296d2d6c3b7a59218dcc714da7095bfa5839c40a.jpg)

Anshika Bajpai

+1 917 344 8306

anshika.bajpai@bernsteinsg.com

We use the well-regarded Geopolitical Risk Index (GPR) as a proxy for geopolitical tensions and compare it against Brent crude prices. Our analysis spans from 1988 through April 2026, allowing for a consistent comparison of the severity and market impact across different geopolitical episodes.

# Key conclusions - (1) key macro factors drive oil price, (2) geopolitical risk as a variable improves understanding, and (3) under this approach, oil could perhaps be \~\$120/bbl today.

It is important to note that the GPR does not rely on direct, on-the-ground reporting. Instead, it is constructed based on the intensity of media coverage of geopolitical events. We view this as a feature rather than a limitation, as market participants often react quickly to headlines.

Linear regression of key macro variables (with and without GPR) points to a \~\$120/bbl of Brent (Exhibit 1).

GPR can spike for non-oil reasons (9-11 for example) and oil price can spike without a GPR signal (the 2008 spike) but generally oil conflicts drive up both GPR and price, driving supply shocks (Exhibit 2). Further, GPR and VIX correlate during supply shocks (Exhibit 3).

Historical disruptions point to two categories of oil shocks (Exhibit 4). Supply shock events, such as the Kuwait invasion in August 1990 and the Russia /Ukraine war in early 2022 serve as proxies for today.

1). In past supply shock crisis, oil prices typically took around 30–50 days to peak after the initial shock, and then generally required a further 2–3 months to decline back toward pre-war levels (Exhibit 5 - Exhibit 9).

2). GPR is less sticky: The full “roller coaster” in GPR index play out over one month, even when the underlying conflict lasted for years.

While the market apparently insists in a return to normal, we continue to believe in a return to “not normal” (Americas Integrated: Updating target prices in a world back to not normal) i.e., higher than normal. The analysis here implies the return may be slower than consensus expects. While we don’t expect oil equities to significantly re-rate upwards significantly as price normalizes, we highlight that a slow return to normal generates real and strong cash flows for covered names allowing them eventually to be more valuable, ceteris paribus, versus where they were pre-crisis.

BERNSTEIN TICKER TABLE 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Cur</td><td rowspan="2">18 May2026ClosingPrice</td><td rowspan="2">PriceTarget</td><td rowspan="2">TTMRel.Perf.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>APA (APA)</td><td>M</td><td>USD</td><td>40.15</td><td>40.00</td><td>110.9%</td><td>USD</td><td>2.83</td><td>7.20</td><td>6.42</td><td>14.2</td><td>5.6</td><td>6.3</td></tr><tr><td>CVX (Chevron)</td><td>M</td><td>USD</td><td>196.12</td><td>204.00</td><td>18.7%</td><td>USD</td><td>8.43</td><td>16.58</td><td>13.26</td><td>23.3</td><td>11.8</td><td>14.8</td></tr><tr><td>COP (ConocoPhillips)</td><td>O</td><td>USD</td><td>124.54</td><td>121.00</td><td>14.9%</td><td>USD</td><td>6.18</td><td>13.89</td><td>10.88</td><td>20.2</td><td>9.0</td><td>11.4</td></tr><tr><td>DVN (Devon Energy)</td><td>O</td><td>USD</td><td>49.68</td><td>59.00</td><td>28.4%</td><td>USD</td><td>4.17</td><td>10.06</td><td>8.43</td><td>11.9</td><td>4.9</td><td>5.9</td></tr><tr><td>FANG (Diamondback)</td><td>O</td><td>USD</td><td>205.62</td><td>241.00</td><td>25.1%</td><td>USD</td><td>4.57</td><td>32.21</td><td>27.22</td><td>45.0</td><td>6.4</td><td>7.6</td></tr><tr><td>EOG (EOG)</td><td>M</td><td>USD</td><td>142.99</td><td>155.00</td><td>2.8%</td><td>USD</td><td>9.88</td><td>18.93</td><td>16.25</td><td>14.5</td><td>7.6</td><td>8.8</td></tr><tr><td>EQT (EQT)</td><td>O</td><td>USD</td><td>57.45</td><td>69.00</td><td>(16.6)%</td><td>USD</td><td>3.31</td><td>8.15</td><td>8.58</td><td>8.9</td><td>5.5</td><td>5.3</td></tr><tr><td>XOM (ExxonMobil)</td><td>O</td><td>USD</td><td>160.49</td><td>182.00</td><td>29.0%</td><td>USD</td><td>7.37</td><td>16.37</td><td>14.49</td><td>21.8</td><td>9.8</td><td>11.1</td></tr><tr><td>KOS (Kosmos Energy)</td><td>M</td><td>USD</td><td>3.21</td><td>2.40</td><td>59.4%</td><td>USD</td><td>(1.58)</td><td>1.13</td><td>0.75</td><td>(2.0)</td><td>2.8</td><td>4.3</td></tr><tr><td>KOS.LN (Kosmos Energy)</td><td>M</td><td>GBp</td><td>240.00</td><td>177.00</td><td>71.5%</td><td>GBP</td><td>(1.17)</td><td>0.83</td><td>0.56</td><td>(2.1)</td><td>2.9</td><td>4.3</td></tr><tr><td>SPX</td><td></td><td></td><td>7,353.61</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,514.18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended   
EQT estimate is Reported EPS; EQT valuation is EV/EBITDA (x);   
Source: Bloomberg, Bernstein estimates and analysis.

# INVESTMENT IMPLICATIONS

We introduce a framework incorporating the geopolitical index. Under this approach, oil could be \~\$120/bbl today. We like oily E&Ps and integrated: FANG, DVN and XOM.

# DETAILS

# PUNCHLINE - OIL PRICE DRIVEN BY MARGINAL COST, INVENTORY, DOLLAR STRENGTH AND A SMATTERING OF GEOPOLITICAL RISK

Our equity models are driven by a more conventional oil price prediction, but if we perform linear regression of oil price against key variables and include/exclude geopolitical risk, we conclude:

1. key variables do in fact inform oil price   
2. geopolitical risk improves the forecast

3. the simple model predicts prices today of \~\$120/bbl Brent (above where forward curve sits).

Real Brent (\$/bbl, in 2026 dollars) = 121 + 0.75·MC - 0.04·Inventory - 1.33·DXY + 0.13·GPR + 2.3·FedFunds + 0.003·SpareCap

EXHIBIT 1: Across over 90 quarters of data, the model explains \~70% of the variation in real oil prices.   
![](images/7b6fa76c61408f8e64f1af388ae07a6e1a8ad44343af91a6a3c8fd022a30f9b1.jpg)  
Source: Caldara, Dario and Matteo Iacoviello (2022), “Measuring Geopolitical Risk,” American Economic Review, April, 112(4), pp.1194-1225., Bloomberg, EIA, OPEC, Bernstein

# THE FOUR DRIVERS THAT ACTUALLY MATTER

Ranking by economic impact — how much a one-standard-deviation move in each variable shifts the predicted Brent price:

1. Marginal Cost of Production: a \$10 increase in marginal cost raises brent by \~\$7.5   
2. Strength of US Dollar: Every 1 pt. rise in the Dollar Index lowers real Brent by \~\$1.3.   
3. OECD Inventory: Every 100 mln bbl increase in OECD stocks lowers real Brent by \~\$4.   
4. GPR (Geopolitical Risk Index): Positive sign as expected (war and supply disruption fears lift prices). The market prices them in fast and then forgets within \~6 months.   
5. (less significant) Fed Funds Rate   
6. (less significant) OPEC Spare Capacity: more spare capacity = higher predicted price

# HERE ARE TWO TYPES OF CRISIS IN THE PAST 40 YEARS

GPR can spike for non-oil reasons (9-11 for example) and oil price can spike without a GPR signal (the 2008 spike) but generally oil conflicts drive up both GPR and price, driving supply shocks.

EXHIBIT 2: GPR can spike for non-oil reasons (9-11 for example) and oil price can spike without a GPR signal (the 2008 spike) but generally oil conflicts drive up both GPR and price, driving supply shocks   
![](images/14086fc04e8e38ecd665fdb65510474ab6cb964fd31642f6290a0dd1354702f2.jpg)

<details>
<summary>line</summary>

| Date       | Brent Price ($) | GPR Index |
|------------|-----------------|---------|
| 6/23/1986  | ~40             | ~50     |
| 6/23/1989  | ~50             | ~70     |
| 6/23/1990  | ~60             | ~100    |
| 6/23/1991  | ~70             | ~150    |
| 6/23/1992  | ~50             | ~70     |
| 6/23/1993  | ~40             | ~50     |
| 6/23/1994  | ~30             | ~40     |
| 6/23/1995  | ~40             | ~60     |
| 6/23/1996  | ~50             | ~80     |
| 6/23/1997  | ~40             | ~60     |
| 6/23/1998  | ~30             | ~40     |
| 6/23/1999  | ~20             | ~30     |
| 6/23/2000  | ~30             | ~50     |
| 6/23/2001  | ~40             | ~70     |
| 6/23/2002  | ~50             | ~100    |
| 6/23/2003  | ~60             | ~150    |
| 6/23/2004  | ~70             | ~200    |
| 6/23/2005  | ~80             | ~250    |
| 6/23/2006  | ~90             | ~300    |
| 6/23/2007  | ~100            | ~350    |
| 6/23/2008  | ~150            | ~400    |
| 6/23/2009  | ~180            | ~350    |
| 6/23/2010  | ~170            | ~300    |
| 6/23/2011  | ~160            | ~250    |
| 6/23/2012  | ~150            | ~200    |
| 6/23/2013  | ~140            | ~150    |
| 6/23/2014  | ~130            | ~100    |
| 6/23/2015  | ~110            | ~70     |
| 6/23/2016  | ~100            | ~50     |
| 6/23/2017  | ~90             | ~40     |
| 6/23/2018  | ~80             | ~30     |
| 6/23/2019  | ~70             | ~20     |
| 6/23/2020  | ~60             | ~15     |
| 6/23/2021  | ~70             | ~25     |
| 6/23/2022  | ~80             | ~35     |
| 6/23/2023  | ~90             | ~45     |
| 6/23/2024  | ~100            | ~55     |
| 6/23/2025  | ~110            | ~65     |
</details>

GPX index is over 1050 in Sep 2021   
Source: Caldara, Dario and Matteo Iacoviello (2022), "Measuring Geopolitical Risk," American Economic Review, April, 112(4), pp.1194-1225., Bloomberg, Bernstein

Further, GPR and VIX correlate during supply shocks.

EXHIBIT 3: GPR and VIX correlate during oil supply shocks   
![](images/4e4a67a039844184187bff0456758574bc564640f1d6ef5a4c9769d7e522fe0c.jpg)

<details>
<summary>line</summary>

| Date       | GPR  | VIX  |
| ---------- | ---- | ---- |
| 1/2/1990   |      |      |
| 1/2/1991   |      |      |
| 1/2/1992   |      |      |
| 1/2/1993   |      |      |
| 1/2/1994   |      |      |
| 1/2/1995   |      |      |
| 1/2/1996   |      |      |
| 1/2/1997   |      |      |
| 1/2/1998   |      |      |
| 1/2/1999   |      |      |
| 1/2/2000   |      |      |
| 1/2/2001   |      |      |
| 1/2/2002   |      |      |
| 1/2/2003   |      |      |
| 1/2/2004   |      |      |
| 1/2/2005   |      |      |
| 1/2/2006   |      |      |
| 1/2/2007   |      |      |
| 1/2/2008   |      |      |
| 1/2/2009   |      |      |
| 1/2/2010   |      |      |
| 1/2/2011   |      |      |
| 1/2/2012   |      |      |
| 1/2/2013   |      |      |
| 1/2/2014   |      |      |
| 1/2/2015   |      |      |
| 1/2/2016   |      |      |
| 1/2/2017   |      |      |
| 1/2/2018   |      |      |
| 1/2/2019   |      |      |
| 1/2/2020   |      |      |
| 1/2/2021   |      |      |
| 1/2/2022   |      |      |
| 1/2/2023   |      |      |
| 1/2/2024   |      |      |
| 1/2/2025   |      |      |
| 1/2/2026   |      |      |
</details>

Source: Caldara, Dario and Matteo Iacoviello (2022), "Measuring Geopolitical Risk," American Economic Review, April, 112(4), pp.1194-1225., Bloomberg, Bernstein

This GPR event with a supply shock resembles previous ones (Kuwait invasion, Iraq War, Russia-Ukraine).

EXHIBIT 4: This GPR event with a supply shock resembles previous ones (Kuwait invasion, Iraq War, Russia-Ukraine)   
![](images/8f88f70603f9d3dc4d271f698f31de1d966ac3cf0a9f912c3f6bfe37490078e1.jpg)

<details>
<summary>line</summary>

| Date       | GPR / Real Brent Ratio |
| ---------- | ---------------------- |
| 1988-07    | ~2.0                   |
| 1989-07    | ~2.5                   |
| 1990-07    | ~3.5                   |
| 1991-07    | ~7.5                   |
| 1992-07    | ~2.5                   |
| 1993-07    | ~3.0                   |
| 1994-07    | ~3.5                   |
| 1995-07    | ~3.0                   |
| 1996-07    | ~2.5                   |
| 1997-07    | ~3.0                   |
| 1998-07    | ~3.5                   |
| 1999-07    | ~3.0                   |
| 2000-07    | ~2.0                   |
| 2001-07    | ~1.5                   |
| 2002-07    | ~16.5                  |
| 2003-07    | ~9.0                   |
| 2004-07    | ~3.0                   |
| 2005-07    | ~2.5                   |
| 2006-07    | ~2.0                   |
| 2007-07    | ~1.5                   |
| 2008-07    | ~1.0                   |
| 2009-07    | ~1.5                   |
| 2010-07    | ~1.5                   |
| 2011-07    | ~1.5                   |
| 2012-07    | ~1.5                   |
| 2013-07    | ~1.5                   |
| 2014-07    | ~1.5                   |
| 2015-07    | ~3.5                   |
| 2016-07    | ~3.0                   |
| 2017-07    | ~2.5                   |
| 2018-07    | ~2.5                   |
| 2019-07    | ~2.5                   |
| 2020-07    | ~3.5                   |
| 2021-07    | ~3.5                   |
| 2022-07    | ~3.5                   |
| 2023-07    | ~3.5                   |
| 2024-07    | ~3.5                   |
| 2025-07    | ~3.5                   |
| 2026-07    | ~3.5                   |
</details>

Source: Caldara, Dario and Matteo Iacoviello (2022), “Measuring Geopolitical Risk,” American Economic Review, April, 112(4), pp.1194-1225., Bloomberg, Bernstein

Interestingly, from the chart below, we find that Brent prices typically flatten about 180 days before the onset of hostilities, which is often roughly two weeks prior to a formal announcement of the conflict.

EXHIBIT 5: Brent prices exhibit greater persistence than the GPR index during past supply shock episodes   
![](images/5486fe1b434aeb39fe87fb88db699503ad62c5ce47bb68e847281b6da21e2682.jpg)

<details>
<summary>bar</summary>

Post-Crisis Persistence (Supply Shocks Only)
| Country/Region | Brent Δ +30d (%) | GPR Δ +30d (%) | Brent Δ +90d (%) | GPR Δ +90d (%) | Brent Δ +180d (%) | GPR Δ +180d (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Kuwait 1990-91 | -70 | -80 | -40 | -80 | -5 | -30 |
| Iraq 2003 (buildup) | -25 | -50 | -10 | -35 | -5 | -60 |
| R-U 2022 | -20 | -50 | -15 | -35 | -5 | -25 |
</details>

Source: Caldara, Dario and Matteo Iacoviello (2022), "Measuring Geopolitical Risk," American Economic Review, April, 112(4), pp.1194-1225., Bloomberg, Bernstein

After one week, GPR declines \~28% while Brent declines 1%. Four months later, Brent still shows 89% of persistent while GPR is almost fully reverted (shown from the blue line below).

EXHIBIT 6: Brent prices exhibit greater persistence than GPR during each of the time frame (10-day, 30-day, 30-day 60-day, 90-day, 120-day duration)   
![](images/688f59ade1226e3d102af958b9e641ceb85c6e7737c80aab9564fbcf097bbddd.jpg)

<details>
<summary>line</summary>

| Days (duration) | Brent Autocorrelation | GPR Autocorrelation |
| --------------- | --------------------- | ------------------- |
| 1               | 1.0                   | 0.82                |
| 5               | 1.0                   | 0.72                |
| 10              | 1.0                   | 0.62                |
| 30              | 0.97                  | 0.38                |
| 60              | 0.93                  | 0.25                |
| 90              | 0.90                  | 0.19                |
| 120             | 0.87                  | 0.18                |
</details>

Source: Caldara, Dario and Matteo Iacoviello (2022), "Measuring Geopolitical Risk," American Economic Review, April, 112(4), pp.1194-1225., Bloomberg, Bernstein

# PREVIOUS CASE STUDIES

GPR captured headline, so does oil price.

Even in severe supply shocks, the oil price premium quickly catches up to GPR in 5-8 weeks while wars last years.

It took \~50 days for oil to peak in Kuwait war in 1990, and took \~20 days for oil to peak during Russia/Ukraine in 2022.

# SUPPLY-SHOCK CASE STUDY #1: KUWAIT CONFLICT IN 1990S

EXHIBIT 7: Oil peaked roughly 50 days after the Kuwait war began, and then took about 60 days to decline back to pre-war levels.

![](images/f24b1ca2d58b6b920fa844dac58e79120f4dc7ce50fcf3cf9bf96fa98728bbc3.jpg)

<details>
<summary>line</summary>

| Date       | Brent $ (Real) | GPR  |
| ---------- | -------------- | ---- |
| 6/13/1990  | ~40            | ~100 |
| 7/13/1990  | ~45            | ~120 |
| 8/13/1990  | ~65            | ~200 |
| 9/13/1990  | ~75            | ~250 |
| 10/13/1990 | ~95            | ~300 |
| 11/13/1990 | ~80            | ~250 |
| 12/13/1990 | ~70            | ~200 |
| 1/13/1991  | ~65            | ~150 |
| 2/13/1991  | ~50            | ~100 |
| 3/13/1991  | ~45            | ~80  |
| 4/13/1991  | ~45            | ~70  |
| 5/13/1991  | ~45            | ~60  |
| 6/13/1991  | ~45            | ~50  |
</details>

Source: Caldara, Dario and Matteo Iacoviello (2022), “Measuring Geopolitical Risk,” American Economic Review, April, 112(4), pp.1194-1225., Bloomberg, Bernstein

In August 1990, Iraq's invasion and occupation of Kuwait abruptly removed roughly 4.3 mln bod of Iraqi and Kuwaiti exports (\~7% of global oil supply at the time) under UN sanctions, triggering a textbook supply shock. Spot prices jumped from about \$21/bbl at the end of July to a peak near \$46/bbl in two months. Brent prices remained elevated for about six months, while the GPR index fell back below 200 just two months after the initial spike (the charts are showing past brent prices are expressed in today's dollars).

# SUPPLY-SHOCK CASE STUDY #2: IRAQ WAR SINCE MARCH 2003

Oil prices began to strengthen once the U.S. signaled its intention to invade Iraq in late 2002, and they remained elevated around the +\$50/bbl level even after geopolitical risk indicators declined in mid 2003.

EXHIBIT 8: While the GPR index has gradually normalized to the 200 level, Brent prices have shown greater stickiness   
![](images/748352ccc654faa41c0dc9fbf6a8038ce6cb6b8f99d8b4c234dfa9c5d933d60e.jpg)

<details>
<summary>line</summary>

| Date       | Brent $ (Real) | GPR  |
| ---------- | -------------- | ---- |
| 9/24/2002  | ~50            | ~50  |
| 10/24/2002 | ~48            | ~55  |
| 11/24/2002 | ~45            | ~40  |
| 12/24/2002 | ~50            | ~55  |
| 1/24/200

[中间内容因长度限制已省略]

 learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
