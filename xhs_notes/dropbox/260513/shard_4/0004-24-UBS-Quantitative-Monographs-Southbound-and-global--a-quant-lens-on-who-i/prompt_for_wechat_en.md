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
# Quantitative Monographs

# Southbound and global: a quant lens on who is the smart money in the Hong Kong market

# Liquidity and dispersion improving driven by Southbound

Both market capitalisation and liquidity have traditionally been concentrated within large caps in Hong Kong's equity market. However, since Q424, we have observed a significant increase in liquidity flowing into smaller-cap bands, indicating that a broader universe in the Hong Kong market has become more tradable, especially for investors who are sensitive to trading costs and capacity. With this improvement in liquidity, return dispersion has also picked up, suggesting more alpha opportunities for stock picking investors. We believe this is partially driven by the growing trading activities and high retail investor participation ratio via the Southbound Stock Connect Scheme.

# Southbound: active or passive? institutional or retail?

While the Southbound investors have been growing in significance in the Hong Kong market, the accelerated inflows have been partially coming from passively-managed cross-border ETFs which have been well-acknowledged by retail investors from onshore China. Over the past year, this has changed the dynamics of Southbound flows, which have traditionally been driven more by active trading. Therefore, despite the accelerated inflows, Southbound investors' stock picking efficacy in aggregate has been fading since 2025. Removing the passive fund flows however, we are still able to extract the actively managed idiosyncratic stock ideas from the Southbound positioning data to generate more consistent alpha.

# Alpha from investor cohorts: both Southbound and global participants

In addition to ex-ETF Southbound flows, we also incorporate insights from the top 20 best performing participants on a dynamic rolling basis, including both brokers and custodian banks in the Hong Kong market, and our proprietary UBS Comprehensive Crowding Factor. These multiple sources of information result in a more consistent and less volatile strategy that has generated an annualised excess return of 12% per annum since 2019, from the long side, with a risk-adjusted return at 1.7, and a maximum drawdown of only 6%.

# Equities

Global

Quantitative

Cathy Fang, PhD

Analyst

cathy.fang@UBS.com

+86-21-3866 8891

Paul Winter

Analyst

paul-j.winter@UBS.com

+61-2-9324 2080

Jackson Shi

Associate

S1460124110003

jackson.shi@UBS.com

+86-21-3866 8878

Lynce Wang, FRM

Analyst

S1460522090001

lynce.wang@UBS.com

+86-21-3866 8638

Oliver Antrobus, CFA

Analyst

oliver.antrobus@UBS.com

+61-3-9242 6467

Amanda Belcaid

Analyst

amanda.belcaid@UBS.com

+44-20-7568 3072

James Cameron

Analyst

james-a.cameron@UBS.com

+61-2-9324 2074

# • What's changed in the Hong Kong market structure in recent years?

- Southbound Stock Connect Scheme has grown its coverage to most of the investable universe in Hong Kong's equity market. More than 80% of market capitalisation in Hong Kong has been accessible via the scheme, including up to 569 names with relatively large market cap and ample liquidity.   
- Interestingly, we have observed an increase in liquidity flowing into a broader universe in the Hong Kong market, to the relatively small-cap bands, starting from Q424, particularly driven by the more active trading activities within the Southbound universe.   
- With the increasingly ample liquidity, both return dispersion and alpha opportunities in the market have also picked up, which we believe has been partially driven by the active trading activities from onshore Chinese retail investors in the Southbound scheme.   
- The level of alpha has generally picked up since Q424, as reflected by the excess returns generated by a generic single factor such as size (market cap), value (book/price) and low-risk (12-month volatility), up to more than 20% per annum.

# • Emerging passive flows in Southbound

- To have a better understanding of the investor landscape in the Hong Kong market, we investigate a tale of two cohorts including Southbound investors from onshore China versus overseas and local investors from Hong Kong market.   
- The market share of Southbound investors has been steadily growing, but a shift from active to passive has emerged progressively starting from end of 2024, with ETF holdings accounting for more than 10% of all Southbound shareholdings as of January 2026.   
- Therefore, despite the accelerated inflows, Southbound investors' stock picking efficacy in the Hong Kong market has been fading away since then.   
- Removing the passive fund flows however, we are still able to extract the actively-managed idiosyncratic stock ideas from the Southbound positioning data to generate more consistent alpha.

# • Capturing alpha from investor cohorts

- Southbound investors from onshore China have been generally overweight in high-volatility names in the sectors such as information technology, whilst global participants tend to favour value stocks with high dividend yield in sectors of utilities and communication services.   
- Considering the low correlation between investor cohorts, we use an augmented model to bring in the diversification. We devised the HK Composite Ownership Factor, to capture the information content from below three sources, and the diversification results in a more consistent and less volatile strategy.

- Southbound ex. ETF: actively-managed investors from onshore China   
- Top 20 participants: best performing participants among overseas and local HK investors over a rolling 52-week window   
• UBS Crowding Factor: proprietary combination of multiple datasets quantifying global institutional investors' positions in the Hong Kong market

Figure 1: Performance of the top portfolios from each investor cohort   
![](images/075dd06a2fe126f83b6320f1afafd70503c066d9857eb87fa863be36a7a6dccb.jpg)

<details>
<summary>line</summary>

| Year | Southbound ex. ETF | Top 20 participants | Crowding factor | Composite Score |
|------|---------------------|---------------------|-----------------|-----------------|
| 2019 | 100%                | 100%                | 100%            | 100%            |
| 2020 | ~110%               | ~120%               | ~105%           | ~115%           |
| 2021 | ~130%               | ~140%               | ~110%           | ~135%           |
| 2022 | ~135%               | ~150%               | ~115%           | ~145%           |
| 2023 | ~145%               | ~165%               | ~125%           | ~160%           |
| 2024 | ~155%               | ~175%               | ~135%           | ~170%           |
| 2025 | ~165%               | ~185%               | ~145%           | ~185%           |
| 2026 | ~180%               | ~200%               | ~150%           | ~200%           |
</details>

Source: DataYes, FactSet, UBS Quant Research; Note: the above chart shows the backtest results run within an investable universe in the Hong Kong market, cross-sectionally sorted into three baskets based on the corresponding type of investors' positions and flows, on a weekly basis. The performance is the cumulative excess returns of the top positions from each investor type, relative to the cap-weighted universe benchmark.

Figure 2: Performance statistics of the top portfolios from each cohort 

<table><tr><td></td><td>Southbound ex. ETF</td><td>Top 20 participants</td><td>Crowding factor</td><td>Composite score</td></tr><tr><td>Annualised Return</td><td>10%</td><td>12%</td><td>6%</td><td>12%</td></tr><tr><td>Annualised Volatility</td><td>8%</td><td>8%</td><td>8%</td><td>7%</td></tr><tr><td>Risk-adjusted Return</td><td>1.3</td><td>1.5</td><td>0.8</td><td>1.7</td></tr><tr><td>Maximum Drawdown</td><td>-8%</td><td>-12%</td><td>-11%</td><td>-6%</td></tr><tr><td>Weekly Turnover</td><td>45%</td><td>57%</td><td>51%</td><td>35%</td></tr><tr><td>Average Liquidity (US$m)</td><td>46.5</td><td>52.3</td><td>53.7</td><td>56.9</td></tr></table>

Source: DataYes, FactSet, UBS Quant Research

# Table of contents: Alpha from Investor Cohorts

Section 1 Executive summary 2

Section 2 A tale of two universes 6

Section 3 Investor landscape 18

Section 4 What works in Hong Kong market? 27

Section 5 Conclusion 46

# Section 2

A tale of two universes

• After more than one decade of rapid development, Southbound has grown its coverage to most of the Hong Kong equity market's investable universe.

- As of April 2026, there are 569 Southbound eligible names making up more than $80\%$ of the float market capitalization. In liquidity terms, the trading activities for Southbound eligible names, including trading from both onshore China and overseas investors, now account for more than $90\%$ of the total daily value traded across the entire market.   
• Moreover, we note that around 60% of the Southbound eligible names are Chinese companies, whilst within the non-Southbound universe, more than 70% originate from the local Hong Kong market.

Figure 3: Comparison of Southbound vs non-Southbound eligible companies listed in HK market   
![](images/5576e828a1776b326cf7a91a753282ea1f946008e0251c00f115d575b55960de.jpg)

<details>
<summary>bar_stacked</summary>

| Category | non-Southbound | Southbound |
| :--- | :--- | :--- |
| Stock Number | 1,493 | 569 |
| Market Cap (US$trn) | 1.0 | 5.3 |
| Liquidity (ADV, US$bn) | 1.7 | 22.0 |
</details>

Source: DataYes, FactSet, UBS Quant Research; Note: above statistics are based on float market capitalisation as of April 2026.

Figure 4: Comparison of market capitalisation (US\$trn) by company region   
![](images/8abfc67f678096081cb81615d0ea984221b4a0ffadb6cdd2c38fb392ea2a9a16.jpg)

<details>
<summary>bar_stacked</summary>

| Category | Chinese companies (%) | Domestic HK companies (%) |
| :--- | :--- | :--- |
| non-Southbound | 0.3 | 0.8 |
| Southbound | 3.4 | 1.9 |
</details>

Source: DataYes, FactSet, UBS Quant Research; Note: above statistics are based on float market capitalisation as of April 2026.

# Investable universe and market concentration

- Amongst both Southbound and non-Southbound names, market structure has been highly concentrated in the large caps and liquid names.   
- In terms of distribution, the largest 10% of large caps by market capitalisation account, respectively, for more than 70% and 80% of the total market capitalisation within the Southbound and non-Southbound) universes, and the top 10% most liquid names represent, respectively, for more than 60% and 90% of market turnover.   
- Within the top decile of each universe, by comparison, the average market capitalisation per stock amongst non-Southbound eligible names has been much smaller than those within Southbound universe (US\$3.8bn vs US\$63bn) and liquidity much lower (US\$10m vs US\$272m).

Figure 5: Market capitalisation distribution   
![](images/620e55d8491a11a71cc5bef06a6ca2c32c53f07f1105ca492df2bcc7fe576f8e.jpg)

<details>
<summary>bar_line</summary>

| Category | % Market cap (LHS) Southbound (%) | % Market cap (LHS) non-Southbound (%) | Average market cap (US$ bn, RHS) Southbound | Average market cap (US$ bn, RHS) non-Southbound |
| :--- | :---: | :---: | :---: | :---: |
| Small: D1 | 0.3 | 0.3 | 0.3 | 0.3 |
| D2 | 0.8 | 0.8 | 0.8 | 0.8 |
| D3 | 1.1 | 1.1 | 1.1 | 1.1 |
| D4 | 1.5 | 1.5 | 1.5 | 1.5 |
| D5 | 2.0 | 2.0 | 2.0 | 2.0 |
| D6 | 2.6 | 2.6 | 2.6 | 2.6 |
| D7 | 3.9 | 3.9 | 3.9 | 3.9 |
| D8 | 6.1 | 6.1 | 6.1 | 6.1 |
| D9 | 11.3 | 11.3 | 11.3 | 11.3 |
| Large: D10 | 63.4 | 63.4 | 63.4 | 63.4 |
| Small: D1 | 0.3 | 0.3 | 0.3 | 0.3 |
| D2 | 0.8 | 0.8 | 0.8 | 0.8 |
| D3 | 1.1 | 1.1 | 1.1 | 1.1 |
| D4 | 1.5 | 1.5 | 1.5 | 1.5 |
The chart displays two data series: one for market cap and another for non-market cap, both plotted against a vertical axis labeled with percentages and numerical values respectively. The red dots represent the average market cap for each category, while the pink dots represent the average market cap for non-market cap, both plotted on the right y-axis.
</details>

Source: DataYes, FactSet, UBS Quant Research; Note: above statistics are based on float market capitalisation as of April 2026.

Figure 6: Liquidity (average daily value traded) distribution   
![](images/9516a110a060edbcbe04547e33de0bb1729919bbbecd1c1f85d551463b653ba8.jpg)

<details>
<summary>bar_line</summary>

| Sample | % Liquidity (LHS) Southbound (%) | % Liquidity (LHS) non-Southbound (%) | Average Liquidity (US$ mn, RHS) Southbound | Average Liquidity (US$ mn, RHS) non-Southbound |
| :--- | :---: | :---: | :---: | :---: |
| Illiquid: D1 | 0.0 | 0.0 | 1.9 | 0.0 |
| D2 | 1.3 | 1.4 | 3.8 | 0.0 |
| D3 | 1.6 | 1.7 | 5.7 | 0.0 |
| D4 | 2.2 | 2.3 | 8.3 | 0.0 |
| D5 | 3.1 | 3.2 | 11.6 | 0.0 |
| D6 | 3.8 | 4.0 | 16.6 | 0.0 |
| D7 | 5.2 | 5.3 | 24.2 | 0.0 |
| D8 | 7.5 | 7.6 | 34.6 | 0.0 |
| D9 | 13.5 | 13.6 | 59.6 | 0.0 |
| Liquid: D10 | 62.0 | 90.0 | 272.0 | 10.1 |
</details>

Source: DataYes, FactSet, UBS Quant Research; Liquidity is calculated based on average daily value traded (ADV) over the past 3 months, as of April 2026.

# Investable universe and market concentration

- We use a threshold of market capitalisation larger than US\$5bn and average daily value traded (ADV) higher than US\$5mn to screen out a fairly investable universe and to filter out extreme outliers. This naturally narrows the sample to around the top three deciles over time.   
- The universes of both Southbound and non-Southbound eligible names have been highly concentrated in large caps, with the top-10 largest companies representing up to 41% and 48% of total market capitalisation.   
- Within the top 10 names, in comparison, the index weights in the Hang Seng Tech Index (HSTECH) have been adjusted and are hence more balanced and diversified.

Figure 7: Top-10 large caps among Southbound names   
![](images/9e651d349e43ac49cf969387c9b84135ba7a8ed73658bcd0396173df7ff44f9b.jpg)

<details>
<summary>bar_stacked</summary>

| Company | Sub-category | Percentage (%) |
| :--- | :--- | :--- |
| TENCENT (700-HK), 10% | ALIBABA (9988-HK), 6% | 35 |
| TENCENT (700-HK), 10% | HSBC (5-HK), 6% | 35 |
| TENCENT (700-HK), 10% | CCB (939-HK), 5% | 42 |
| TENCENT (700-HK), 10% | CNOOC (883-HK), 3% | 25 |
| TENCENT (700-HK), 10% | AIA (1299-HK), 2% | 25 |
| TENCENT (700-HK), 10% | XIAOMI (1810-HK), 1% | 15 |
| TENCENT (700-HK), 10% | ICBC (1398-HK), 1% | 15 |
| TENCENT (700-HK), 10% | HKEX (388-HK), 1% | 15 |
</details>

Source: DataYes, FactSet, UBS Quant Research

Figure 8: Top-10 large caps among non-Southbound eligible names   
![](images/ea0f394a0e09aca547bbb9e91ebc32a6ca7058fe03eca4d2694777a9a222e5ac.jpg)

<details>
<summary>treemap</summary>

| Entity | Value (%) |
| :--- | :--- |
| NETEASE (9999-HK), 11% | |
| MANULIFE FINANCIAL (945-HK), 9% | |
| TRIP.COM (9961-HK), 5% | |
| BIDU (9888-HK), 5% | |
| JID (9618-HK), 5% | |
| KNOWLEDGE ATLAS (2513-HK), 4% | |
| MINIMAX (100-HK), 3% | |
| H WORLD (1179-HK), 2% | |
| NIO (9866-HK), 2% | |
| ILIVATAR COREX (9903-HK), 2% | |
</details>

Source: DataYes, FactSet, UBS Quant Research

Figure 9: Top-10 large caps within HSTECH (index weights)   
![](images/19286771be3c59e72add951cf22171c08b2ca3126603de74a3ab9c3c625ff3ef.jpg)

<details>
<summary>treemap</summary>

| Company | Value (HK) (%) | Percentage (%) |
| :--- | :--- | :--- |
| MEITUAN | 3690 | 9 |
| BYD | 1211 | 9 |
| NETEASE | 9999 | 7 |
| XIAOMI | 1810 | 7 |
| SMIC | 981 | 9 |
| ALIBABA | 9988 | 7 |
| TENCENT | 700 | 7 |
| JD | 9618 | 5 |
| BIDU | 9888 | 4 |
| KUAISHOU | 1024 | 4 |
</details>

Source: DataYes, FactSet, UBS Quant Research

- Due to a highly concentrated market structure, liquidity has historically been a challenge for small caps in the Hong Kong market. Both positions and flows used to be concentrated within large caps.   
- However, we have observed a significant increase in liquidity flowing into the broader universe of the Hong Kong market since Q424, despite all the IPO issuances absorbing and diverting the existing market liquidity.   
- By comparing Southbound and non-Southbound universes, we note that the increase in liquidity has been particularly driven by the rising trading activities within the Southbound eligible universe.

Figure 14: Daily market turnover (US\$bn) in Southbound universe vs non-Southbound   
![](images/b93cf5cd24c00778a795f16fa945a8def6018cbd11469c9e9a5a8538d07d899f.jpg)

<details>
<summary>line</summary>

| Year | Southbound (LHS) | non-Southbound (RHS) |
|------|------------------|----------------------|
| 2017 | ~6.0             | ~5.0                 |
| 2018 | ~15.0            | ~6.0                 |
| 2019 | ~8.0             | ~4.0                 |
| 2020 | ~10.0            | ~5.0                 |
| 2021 | ~25.0            | ~3.0                 |
| 2022 | ~15.0            | ~2.0                 |
| 2023 | ~10.0            | ~1.5                 |
| 2024 | ~12.0            | ~1.0                 |
| 2025 | ~30.0            | ~2.0                 |
</details>

Source: DataYes, FactSet, UBS Quant Research

- Using a three-month average daily value (3M ADV) traded of more than US\$5m as a threshold, it is evident that the number of active stocks in Hong Kong has expanded significantly from around 200 in 2024 to 500 now   
- Indicating the Hong Kong market's broader universe has become more tradable over the past year, especially for investors that are sensitive to fund capacity and trading from a systematic perspective.

Figure 15: Number of stocks with an average daily value traded (3M ADV) of more than US\$5m   
![](images/2979cfe0a22abceb64df53465fc88ab48016d5b75549bf875a639ca4f8ebb94f.jpg)

<details>
<summary>line</summary>

| Year | # of Stocks |
|------|-------------|
| 2017 | ~230        |
| 2018 | ~280        |
| 2019 | ~210        |
| 2020 | ~250        |
| 2021 | ~380        |
| 2022 | ~300        |
| 2023 | ~250        |
| 2024 | ~230        |
| 2025 | ~500        |
</details>

Source: DataYes, FactSet, UBS Quant Research

# ... along with the alpha opportunity

- With this increasingly ample liquidity, it is not surprising to see that dispersion in the market has also picked up.   
- To better assess alpha opportunities and return dispersion in the Hong Kong market, we investigate the long-short performance based on a variety of traditional quant and fundamental factors within an investable scope and the changes in performance over the past decade.

Figure 16: Return dispersion picking up over time   
![](images/2104e1bd090a01500e723a0defa1093610944d86e80f878b896049b392077599.jpg)

<details>
<summary>line</summary>

| Year | Southbound | non-Southbound |
|------|------------|----------------|
| 2018 | 2.2%       | 3.5%           |
| 2019 | 2.4%       |

[中间内容因长度限制已省略]

ns in such this publication or material are not made or provided to you, and (ii) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material and (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSJ/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr. Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email : parameshwaran.s@UBS.com, Name of Grievance Officer Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email: ol-UBS-sec-compliance@UBS.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.UBS.com/global/en/about\_UBS/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.UBS.com/UBSsi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a sUBSidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian Citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian Citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
