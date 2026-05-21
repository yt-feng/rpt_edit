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
# Investor Presentation | Asia Pacific

# China Property: An Inflection or Another False Start?

A potential housing inflection has re-emerged as a debate after secondary home sales unexpectedly rebounded since March. We stay prudent and suggest waiting for more clarity, as the first-stage valuation recovery has priced in continued sales growth.

MS ASIA LIMITED+

# Stephen Cheung, CFA

Equity Analyst

Stephen.Cheung@morganstanley.com +852 3963-0385

# Cara Zhu

Equity Analyst

Cara.Zhu@morganstanley.com +852 2848-7117

# CHINA PROPERTY

# Asia Pacific

Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Key difference of market and our views 

<table><tr><td colspan="2">Market</td><td>MS</td></tr><tr><td>Sustainability of secondary sales</td><td>Strong rebound in March-April without notable policy support may indicate an organic recovery in the making</td><td>Sustainability is in doubt given limited improvement in macro/housing indicators, divergent trends between new and secondary homes, and still-fragile resident sentiment</td></tr><tr><td>Diffusion into new homes</td><td>Secondary sales rebound could pull up primary sales volume via replacement demand from home sellers</td><td>Secondary sales pickup may cannibalize primary sales due to more competitive pricing, as home sellers are still eager to dispose of properties</td></tr><tr><td>Home prices in high-tier cities in 2026-27</td><td>Persistent m-m uptrend amid market recovery</td><td>Continued soft downtrend</td></tr><tr><td>Key focus</td><td>Whether the worst has passed in high-tier cities?</td><td>Whether the sales recovery is strong, broad and profitable enough to justify share prices?</td></tr><tr><td>Developers&#x27; normalized profit level</td><td>Core profits to witness dual expansion amid notable sales and margin improvement</td><td>Reduced primary market size, constrained leverage, homogeneous landbanking strategies, and continued drag from legacy inventory would limit medium-term earnings rebound potential</td></tr><tr><td>Valuation</td><td>P/B to recover to historical average level of ~0.8x (vs. ~0.5x now), suggesting at least high-double-digit % upside potential</td><td>2028E P/E and ex-IP EV/pre-sales have already exceeded bull-market levels; solid EPS uplift is key to driving share prices higher</td></tr><tr><td>Stock selection</td><td>Pure beta: COLI (0688.HK) / Jinmao (0817.HK)</td><td>Beta + Alpha: CR Land (1109.HK) / C&amp;D (1908.HK)</td></tr></table>

Source: MS.

# What has caused the unexpected secondary sales rebound?

# Observation 1: CNY-adjusted growth may suggest pend-up demand was released from 4Q25 amid improved resident sentiment

Weekly secondary real-time homes sales of 25 major cities on CNY-adjusted basis   
![](images/c1ba0f1fa2fc26510db4f956e5c7024930738cb83e9664060aa793608d89e642.jpg)

<details>
<summary>line</summary>

| Period | 2022 | 2023 | 2024 | 2025 | 2026 |
|--------|------|------|------|------|------|
| T-20   | 5    | 18   | 38   | 28   | 25   |
| T-18   | 15   | 25   | 35   | 38   | 35   |
| T-16   | 20   | 30   | 40   | 60   | 40   |
| T-14   | 22   | 32   | 42   | 58   | 38   |
| T-12   | 25   | 30   | 40   | 55   | 35   |
| T-10   | 28   | 28   | 38   | 50   | 33   |
| T-8    | 30   | 25   | 35   | 45   | 30   |
| T-6    | 32   | 28   | 33   | 40   | 35   |
| T-4    | 35   | 30   | 30   | 35   | 40   |
| T-2    | 38   | 35   | 28   | 30   | 45   |
| T      | 40   | 40   | 25   | 25   | 50   |
| T+2    | 70   | 75   | 50   | 60   | 70   |
| T+4    | 65   | 78   | 55   | 65   | 65   |
| T+6    | 60   | 70   | 50   | 60   | 60   |
| T+8    | 55   | 65   | 45   | 55   | 55   |
| T+10   | 50   | 60   | 40   | 50   | 50   |
| T+12   | 45   | 55   | 35   | 45   | 45   |
| T+14   | 40   | 50   | 30   | 40   | 40   |
| T+16   | 35   | 45   | 25   | 35   | 35   |
| T+18   | 30   | 40   | 20   | 30   | 30   |
| T+20   | 25   | 35   | 15   | 25   | 25   |
</details>

The weak 4Q25 and fast catch-up post-CNY of cumulative secondary home sales may suggest pend-up demand release in the 25 major cities   
![](images/0bddcd4fd079fc3b5fd8a636a62b325f9c9229cd5e038fbeab8723f091005925.jpg)

<details>
<summary>line</summary>

| Period | 2022 (k units) | 2023 (k units) | 2024 (k units) | 2025 (k units) | 2026 (k units) |
|---|---|---|---|---|---|
| T-20 | ~50 | ~50 | ~50 | ~50 | ~50 |
| T-18 | ~100 | ~100 | ~100 | ~100 | ~100 |
| T-16 | ~150 | ~150 | ~150 | ~150 | ~150 |
| T-14 | ~200 | ~200 | ~200 | ~250 | ~250 |
| T-12 | ~250 | ~250 | ~250 | ~350 | ~350 |
| T-10 | ~300 | ~300 | ~300 | ~450 | ~450 |
| T-8 | ~350 | ~350 | ~350 | ~550 | ~550 |
| T-6 | ~400 | ~400 | ~400 | ~650 | ~650 |
| T-4 | ~450 | ~450 | ~450 | ~750 | ~750 |
| T-2 | ~500 | ~500 | ~500 | ~850 | ~850 |
| T | ~400 | ~550 | ~650 | ~900 | ~750 |
| T+2 | ~450 | ~600 | ~700 | ~950 | ~750 |
| T+4 | ~550 | ~750 | ~850 | ~1100 | ~850 |
| T+6 | ~650 | ~950 | ~1050 | ~1300 | ~950 |
| T+8 | ~750 | ~1150 | ~1250 | ~1450 | ~1150 |
| T+10 | ~850 | ~1350 | ~1450 | ~1650 | ~1350 |
| T+12 | ~950 | ~1450 | ~1550 | ~1750 | ~1450 |
| T+14 | ~1050 | ~1450 | ~1650 | ~1850 | ~1550 |
| T+16 | ~1150 | ~1450 | ~1750 | ~1950 | ~1650 |
| T+18 | ~1250 | ~1450 | ~1850 | ~2050 | ~1750 |
| T+20 | ~950 | ~1400 | ~1480 | ~1780 | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
</details>

Source: Bingshan, MS. Note: T stands for Chinese New Year week.

# Observation 2: Diverging performance between new and secondary home sales may suggest market shift

Housing with less than Rmb5mn/Rmb3mn lump-sum accounted for $>80\%$ of secondary home sales in top-tier cities in April 2026

![](images/9339629e698b895815559dc25d577300d3c656962b35f8cba909fe08042e8226.jpg)

<details>
<summary>bar_stacked</summary>

| Region | <2mn (%) | 2-3mn (%) | 3-5mn (%) | 5-7mn (%) | 7-10mn (%) | >10mn (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Beijing | 27 | 26 | 28 | 14 | 4 | 3 |
| Shanghai | 33 | 23 | 22 | 14 | 4 | 5 |
| Shenzhen | 30 | 29 | 23 | 10 | 4 | 4 |
| Guangzhou | 70 | 14 | 10 | 4 | 1 | 1 |
| Hangzhou | 53 | 21 | 15 | 8 | 3 | 3 |
| Xiamen | 53 | 23 | 15 | 6 | 1 | 1 |
</details>

Housing lump-sum index has been dropping faster than transaction home prices y-y since 2025, indicating increased share of small lump-sum housing

![](images/f4bcbb652a19906eb7ed2043df9290d41c431906c9ab8825f91d6557dfc9fe4b.jpg)

<details>
<summary>line</summary>

| Date   | Lump-sum Index | Transaction price |
|--------|----------------|--------------------|
| Jan-17 | 30%            | 30%                |
| Jul-17 | 35%            | 35%                |
| Jan-18 | 20%            | 20%                |
| Jul-18 | 10%            | 10%                |
| Jan-19 | 5%             | 5%                 |
| Jul-19 | 0%             | 0%                 |
| Jan-20 | -5%            | -5%                |
| Jul-20 | 5%             | 5%                 |
| Jan-21 | 15%            | 10%                |
| Jul-21 | 5%             | 5%                 |
| Jan-22 | 0%             | 0%                 |
| Jul-22 | -5%            | -5%                |
| Jan-23 | -10%           | -10%               |
| Jul-23 | -15%           | -15%               |
| Jan-24 | -20%           | -20%               |
| Jul-24 | -15%           | -15%               |
| Jan-25 | -10%           | -10%               |
| Jul-25 | -5%            | -5%                |
| Jan-26 | -15%           | -15%               |
</details>

Source: Bingshan, MS.

# What Do We Expect on Sales Recovery?

# Drag 1. Limited improvement on household income and leverage

Employment PMI suggests non-manufacturing sectors are still under pressure

![](images/332ef28625039e2277aa6e9f40ca103215a0f46b6a292f26879b6ee9a719b1b9.jpg)

<details>
<summary>line</summary>

| Date   | Manufacturing | Non-manufacturing |
|--------|---------------|-------------------|
| Apr-15 | 48            | 49                |
| Apr-16 | 47            | 49                |
| Apr-17 | 50            | 50                |
| Apr-18 | 49            | 49                |
| Apr-19 | 47            | 48                |
| Apr-20 | 51            | 48                |
| Apr-21 | 49            | 48                |
| Apr-22 | 48            | 47                |
| Apr-23 | 45            | 43                |
| Apr-24 | 48            | 46                |
| Apr-25 | 48            | 45                |
| Apr-26 | 49            | 46                |
</details>

China household leverage remains elevated with limited improvement, despite home sales having cumulatively shrunk by \~40%

![](images/e472dd3bdea705ecda0ddd95c5cc6f26108dce492043b9ac35ed3b26b9a19044.jpg)

<details>
<summary>line</summary>

| Year | Value (%) |
|---|---|
| 2001 | 9 |
| 2003 | 10 |
| 2005 | 12 |
| 2007 | 11 |
| 2009 | 25 |
| 2011 | 28 |
| 2013 | 34 |
| 2015 | 40 |
| 2017 | 51 |
| 2019 | 58 |
| 2021 | 64 |
| 2023 | 63 |
| 2025 | 63 |
</details>

Home ownership ratio of China urban households reached $\sim 80\%$ in 2020, indicating that housing needs has been largely satisfied

![](images/639b86a63752ac905cd0a0b0b06fd8ac8d8d3c3fcc7d8952f9a04edec3d9602e.jpg)

<details>
<summary>bar</summary>

| Country/Region | Percentage (%) |
| :--- | :--- |
| China (all) | 85 |
| China (urban) | 78 |
| Japan | 77 |
| Spain | 75 |
| Italy | 73 |
| Netherlands | 69 |
| USA | 65 |
| UK | 64 |
| France | 64 |
| Korea | 61 |
| Germany | 49 |
| Switzerland | 42 |
</details>

Source: NBS. Census. CEIC. Eurostat. US Census Bureau. Statista. Statistics Korea. MS.

# Drag 1. Limited improvement on household income and leverage (con't)

Housing affordability in Tier 1 cities has dropped back to 2014-15 levels...   
![](images/5dea433ab1e3215f3e32031386323fac6a00a685514214c158d5e0872774e0b3.jpg)

<details>
<summary>line</summary>

| Year | National | Tier 1 | Tier 2 | Rest of China |
|------|----------|--------|--------|---------------|
| 2005 | 9.5      | 10.5   | 8.5    | 7.0           |
| 2006 | 9.0      | 11.0   | 8.0    | 6.8           |
| 2007 | 8.8      | 12.5   | 8.2    | 6.5           |
| 2008 | 8.0      | 11.5   | 7.5    | 6.0           |
| 2009 | 8.5      | 13.0   | 8.8    | 6.5           |
| 2010 | 8.8      | 15.0   | 9.0    | 7.0           |
| 2011 | 8.5      | 14.0   | 8.5    | 6.8           |
| 2012 | 8.2      | 13.0   | 8.2    | 6.5           |
| 2013 | 8.0      | 13.5   | 8.0    | 6.3           |
| 2014 | 7.8      | 13.0   | 7.8    | 6.0           |
| 2015 | 7.5      | 14.0   | 7.5    | 6.2           |
| 2016 | 7.8      | 16.5   | 7.8    | 6.5           |
| 2017 | 8.0      | 16.0   | 8.0    | 6.8           |
| 2018 | 8.2      | 17.0   | 8.2    | 7.0           |
| 2019 | 8.5      | 18.0   | 8.5    | 7.2           |
| 2020 | 8.8      | 19.0   | 8.8    | 7.5           |
| 2021 | 8.5      | 18.5   | 8.5    | 7.3           |
| 2022 | 8.2      | 18.0   | 8.2    | 7.0           |
| 2023 | 7.8      | 17.0   | 7.8    | 6.5           |
| 2024 | 7.5      | 16.0   | 7.5    | 6.0           |
| 2025 | 7.0      | 14.0   | 7.0    | 5.5           |
</details>

But remains much higher than global metropolitan areas   
![](images/55a6778c52bf9cd1e7a5662f92f83a8ca49aecddcd672f76d515719601b488b0.jpg)

<details>
<summary>bar</summary>

| Region | Value (x) |
|---|---|
| Hong Kong | 14.5 |
| China Tier 1 | 14.5 |
| Sydney | 13.8 |
| Vancouver | 11.7 |
| Los Angeles | 11.2 |
| San Francisco | 10.0 |
| Melbourne | 9.7 |
| Australia | 9.7 |
| Toronto | 8.3 |
| New Zealand | 7.6 |
| China Tier 2 | 7.6 |
| China | 7.1 |
| UK | 5.6 |
| Canada | 5.3 |
| USA | 4.8 |
| Singapore | 4.2 |
</details>

Source: NBS, Census, CEIC, MS

# Drag 2. Rental rates are declining

Rental rates have cumulatively dropped $\sim 15\%$ since July 2021, and started to re-weaken again in April 2026

![](images/fb8f77fbd21bd6ddefbb663623d86653ab61b2c7b1cc49ad36578c73457e5b9a.jpg)

<details>
<summary>line</summary>

| Date   | National | Beijing | Guangzhou | Shenzhen | Shanghai |
|--------|----------|---------|-----------|----------|----------|
| Jul-21 | 100      | 100     | 100       | 100      | 100      |
| Oct-21 | 99       | 99      | 99        | 99       | 99       |
| Jan-22 | 98       | 98      | 98        | 98       | 98       |
| Apr-22 | 97       | 97      | 97        | 97       | 97       |
| Jul-22 | 96       | 96      | 96        | 96       | 96       |
| Oct-22 | 95       | 95      | 95        | 95       | 95       |
| Jan-23 | 94       | 94      | 94        | 94       | 94       |
| Apr-23 | 93       | 93      | 93        | 93       | 93       |
| Jul-23 | 92       | 92      | 92        | 92       | 92       |
| Oct-23 | 91       | 91      | 91        | 91       | 91       |
| Jan-24 | 90       | 90      | 90        | 90       | 90       |
| Apr-24 | 89       | 89      | 89        | 89       | 89       |
| Jul-24 | 88       | 88      | 88        | 88       | 88       |
| Oct-24 | 87       | 87      | 87        | 87       | 87       |
| Jan-25 | 86       | 86      | 86        | 86       | 86       |
| Apr-25 | 85       | 85      | 85        | 85       | 85       |
| Jul-25 | 84       | 84      | 84        | 84       | 84       |
| Oct-25 | 83       | 83      | 83        | 83       | 83       |
| Jan-26 | 82       | 82      | 82        | 82       | 82       |
| Apr-26 | 81       | 81      | 81        | 81       | 81       |
</details>

More cities have seen their rental yields re- weaken amid falling rental rates in recent months, adding downside pressure on home prices

![](images/5ca35f577e3e158fe186912f4de537ef4f871e0cd5898307e58741156530681c.jpg)

<details>
<summary>bar_stacked</summary>

| Month | Up (%) | Flat (%) | Down (%) |
| :--- | :--- | :--- | :--- |
| Aug-21 | 41 | 37 | 18 |
| Dec-21 | 35 | 43 | 19 |
| Apr-22 | 42 | 38 | 16 |
| Aug-22 | 54 | 34 | 11 |
| Dec-22 | 60 | 21 | 10 |
| Apr-23 | 76 | 14 | 8 |
| Aug-23 | 83 | 10 | 6 |
| Dec-23 | 85 | 8 | 4 |
| Apr-24 | 89 | 6 | 4 |
| Aug-24 | 75 | 13 | 10 |
| Dec-24 | 95 | 3 | 1 |
| Apr-25 | 99 | 2 | 1 |
| Aug-25 | 91 | 6 | 4 |
| Dec-25 | 93 | 4 | 3 |
| Apr-26 | 33 | 30 | 30 |
</details>

Source: Bingshan, MS.

# Drag 3. Primary inventory level remains elevated and disposal plans of secondary home owners are urgent

Primary inventory of 70 cities increased to 32 months in March 2026   
![](images/e20345effed94d83f49c2448a53d2fc739709d5f9839c40be4492cc1552d05e1.jpg)

<details>
<summary>bar_line</summary>

| Date       | Inventory GFA (mn sqm) | Inventory months (RHS) | Inventory months average (RHS) |
|------------|------------------------|------------------------|--------------------------------|
| 2011-01    | ~280                   | ~18                    | 15                             |
| 2011-09    | ~380                   | ~35                    | 15                             |
| 2012-05    | ~420                   | ~30                    | 15                             |
| 2013-01    | ~450                   | ~25                    | 15                             |
| 2013-09    | ~480                   | ~28                    | 15                             |
| 2014-05    | ~550                   | ~33                    | 15                             |
| 2015-01    | ~560                   | ~32                    | 15                             |
| 2015-09    | ~540                   | ~28                    | 15                             |
| 2016-05    | ~480                   | ~22                    | 15                             |
| 2016-17    | ~380                   | ~15                    | 15                             |
| 2017-01    | ~390                   | ~16                    | 15                             |
| 2017-09    | ~380                   | ~17                    | 15                             |
| 2018-05    | ~400                   | ~18                    | 15                             |
| 2019-01    | ~420                   | ~17                    | 15                             |
| 2019-09    | ~430                   | ~18                    | 15                             |
| 2020-05    | ~480                   | ~20                    | 15                             |
| 2021-01    | ~500                   | ~22                    | 15                             |
| 2021-09    | ~490                   | ~20                    | 15                             |
| 2022-05    | ~480                   | ~25                    | 15                             |
| 2023-01    | ~460                   | ~33                    | 15                             |
| 2023-09    | ~440                   | ~30                    | 15                             |
| 2024-05    | ~470                   | ~35                    | 15                             |
| 2024-17    | ~460                   | ~33                    | 15                             |
| 2025-01    | ~440                   | ~36                    | 15                             |
| 2025-09    | ~430                   | ~38                    | 15                             |
</details>

>60% of homeowners with home sales plans are willing to take losses, including 13% who could accept losses of >20%, as of March 2026   
![](images/00a978c17945a715c45bea059fc4f3287ac6914e9a3b9797b722b91712ef4ebb.jpg)

<details>
<summary>bar_stacked</summary>

| Month | Above (%) | Comparable (%) | Up to 10% lower (%) | Up to 20% lower (%) | ASAP (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Dec-23 | 25 | 33 | 32 | 6 | 4 |
| Mar-24 | 25 | 32 | 35 | 6 | 2 |
| Jun-24 | 15 | 31 | 47 | 5 | 2 |
| Sep-24 | 19 | 35 | 40 | 5 | 1 |
| Dec-24 | 25 | 25 | 36 | 11 | 2 |
| Apr-25 | 21 | 35 | 26 | 14 | 2 |
| Jul-25 | 18 | 27 | 42 | 12 | 2 |
| Oct-25 | 17 | 31 | 38 | 11 | 2 |
| Mar-26 

[中间内容因长度限制已省略]

Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of China Overseas Land & Investment Ltd., China Resources Land Ltd., China Vanke Company Ltd., Longfor Group Holdings Ltd. listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.   
INDUSTRY COVERAGE: China Property 

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (05/18/2026)</td></tr><tr><td>Stephen Cheung, CFA</td><td></td><td></td></tr><tr><td>C&amp;D International Investment Group Ltd (1908.HK)</td><td>O (08/01/2024)</td><td>HK$16.41</td></tr><tr><td>China Jinmao Holdings Group Ltd (0817.HK)</td><td>E (03/28/2024)</td><td>HK$1.72</td></tr><tr><td>China Merchants Shekou Industrial Zone (001979.SZ)</td><td>E (05/06/2021)</td><td>Rmb9.04</td></tr><tr><td>China Overseas Land &amp; Investment Ltd. (0688.HK)</td><td>E (01/20/2025)</td><td>HK$15.92</td></tr><tr><td>China Resources Land Ltd. (1109.HK)</td><td>O (01/02/2019)</td><td>HK$35.92</td></tr><tr><td>China Vanke Company Ltd. (2202.HK)</td><td>E (11/07/2023)</td><td>HK$2.93</td></tr><tr><td>China Vanke Company Ltd. (000002.SZ)</td><td>U (11/30/2022)</td><td>Rmb3.71</td></tr><tr><td>Gemdale Corporation (600383.SS)</td><td>U (01/28/2026)</td><td>Rmb2.85</td></tr><tr><td>Greentown China Holdings (3900.HK)</td><td>U (08/26/2025)</td><td>HK$9.93</td></tr><tr><td>Longfor Group Holdings Ltd. (0960.HK)</td><td>E (05/17/2024)</td><td>HK$8.54</td></tr><tr><td>Poly Developments and Holdings Group (600048.SS)</td><td>E (05/17/2024)</td><td>Rmb6.17</td></tr><tr><td>Seazen Group Ltd (1030.HK)</td><td>O (01/28/2026)</td><td>HK$2.05</td></tr><tr><td>Seazen Holdings Company Ltd. (601155.SS)</td><td>O (11/03/2025)</td><td>Rmb14.21</td></tr><tr><td>Yuexiu Property Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.40</td></tr></table>

© 2026 MS
"""
