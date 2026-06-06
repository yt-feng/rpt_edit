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
Asia

Health Care

Pharmaceuticals / Biotechnology

Industry

# China Healthcare

Date

5 June 2026

Industry Update

# Market likely overreacted on geopolitical tensions, we think

The healthcare sector has been relatively weak year-to-date. Even after the disclosure of promising clinical data during the ASCO meeting, investors have tended to sell-on-news following announcements. Apart from the uncertainty with the interest rate environment, we attribute the weakness in healthcare sentiment to potential regulations on out-licensing deals given ongoing geopolitical tensions.

In our view, these potential regulations would likely do more harm than good to the US biotech industry. Furthermore, the legislation would likely be a long and lengthy process, facing significant opposition from industry leaders. As such, we believe the market seems to have overreacted to the news.

Cyrus Ng, CFA

Research Analyst

+852-2203-6208

Figure 1: YTD performance of HK-listed healthcare companies   
![](images/41cd9add7f99311eec431e5b11a0bc9ca97ca63c18c990c55cf81c462c0d936b.jpg)

<details>
<summary>line</summary>

| Date     | Drug manufacturers | Biotechs | Distributors | CROs/CDMOs | Device manufacturers | Healthcare services | Medtech / internet healthcare | Hang Seng Index |
|----------|--------------------|----------|--------------|------------|----------------------|---------------------|-------------------------------|-----------------|
| 5-Jun    | -20%               | -19.9%   | -4.2%        | 6.0%       | -1.6%                | -15.6%              | -30.2%                        | -2.5%           |
</details>

Source : Bloomberg Finance LP, DB

# US lawmakers have proposed tightening scrutiny of Chinese biotech investments

In February, some US officials sent a letter to the US Treasury Department, proposing to expand the coverage of the COINS Act to biotechnology, thereby prohibiting US investments in the Chinese biotechnology industry.

On May 21, Chairman John Moolenaar of the Select Committee on China wrote to Treasury Secretary Scott Bessent, requesting the inclusion of biotechnology as a prohibited technology under the COINS Act of 2025. This request stems from concerns over increased US investment and intellectual property transfer to China's biotech sector, highlighted by the deal between BMS and Hengrui.

On June 2, John Moolenaar and Congresswoman Debbie Dingell introduced the Biotech Investment National Security Act (BINSA). This legislation proposes to include biotechnology in the COINS Act of 2025. Under this bill, licensing deals, joint ventures, and equity investments in China could be subject to review by the Treasury Department and Secretary of Defense.

# Our take: May do more harm than good to US biotech industries

China has already become a global innovation hub in drug R&D, with its companies consistently investing in this area. Total pharmaceutical R&D spending in China grew from USD26bn in 2020 to an estimated USD39bn in 2025, representing an $8.5\%$ CAGR during this period. Throughout 2020-2025, China's R&D expenditure consistently comprised approximately $11 - 13\%$ of global pharmaceutical R&D spending. This sustained investment has fostered an R&D ecosystem characterized by efficiency, accumulated experience, successful candidates, and technical know-how. Despite China's relatively smaller share of global R&D spending, it has led the world in the number of innovative drugs entering clinical trials since 2020. Consequently, we believe China will likely continue to be a global R&D hub for the pharmaceutical industry.

In other words, China possesses a significant number of new drug candidates. Avoiding cooperation with Chinese companies would mean missing out on a substantial number of potential drug candidates, especially in emerging areas like ADCs and multi-specific antibodies.

Figure 2: Global and China R&D spending (USD bn)   
![](images/0a9c46a1588aa44909f9a5d186bd90b78636913569d3aa6fc89e0f8a6c799fac.jpg)

<details>
<summary>bar_line</summary>

| Year | Global pharmaceutical R&D spending | China pharmaceutical R&D spending | China R&D spending as a % of global (%) |
|---|---|---|---|
| 2020 | 205 | 26 | 12.7 |
| 2021 | 224 | 29 | 13.1 |
| 2022 | 242 | 32 | 13.2 |
| 2023 | 261 | 30 | 11.5 |
| 2024 | 278 | 34 | 12.3 |
| 2025E | 298 | 39 | 13.3 |
</details>

Source : DB estimates

Figure 3: Number of innovative drugs newly entered into clinical trials   
![](images/e24ca7d7dfdd37a7881a4f41aa21fb87346c2cced2a67ae2ad0c41d4531d5961.jpg)

<details>
<summary>line</summary>

| Year | Mainland China | US | Europe | Japan | Others |
|---|---|---|---|---|---|
| 2018 | 385 | 379 | 185 | 99 | 36 |
| 2019 | 341 | 398 | 214 | 101 | 47 |
| 2020 | 482 | 452 | 246 | 134 | 36 |
| 2021 | 602 | 454 | 217 | 156 | 66 |
| 2022 | 625 | 541 | 234 | 197 | 44 |
| 2023 | 661 | 432 | 246 | 182 | 51 |
| 2024 | 722 | 457 | 241 | 146 | 57 |
| 2025 | 827 | 482 | 219 | 130 | 84 |
</details>

Source : Pharmcube

Deals will likely flow to companies from other regions. US-related out-licensing activities accounted for approximately $42\%$ of the number of deals from 2020 to May 2026, and $57\%$ of total upfront payments in the same period. If the US decides to wall off in-licensed assets from Chinese pharmaceutical and biotech companies, we expect some of these deals would shift to companies in other regions

Figure 4: Geographical breakdown of out-licensing deals   
Geographical breakdown of out-licensing deals   
![](images/2ddde522297d07a0f26547f77cd14ed2a433760c6eb408ade24a21c96135f6e8.jpg)

<details>
<summary>pie</summary>

| Region | Percentage (%) |
| :--- | :--- |
| US | 42 |
| Europe | 28 |
| Asia | 18 |
| Others | 12 |
</details>

Note: This includes the deals in 2020 and May 2026; Japan, South Korea, India, Indonesia, Vietnam, Pakistan, Philippines, Malaysia, Bangladesh, Thailand, Singapore are included in Aisa  
Source: Pharmcube, DB

Figure 5: Geographical breakdown of upfront payments   
Geographical breakdown of upfront   
![](images/b72ff0ef3405670b94f52091b1133320460662071b771e1b1944b2ab940c74dc.jpg)

<details>
<summary>pie</summary>

| Region | Percentage (%) |
| :--- | :--- |
| US | 57 |
| Europe | 33 |
| Asia | 9 |
</details>

Note: This includes the deals in 2020 and May 2026; Japan, South Korea, India, Indonesia, Vietnam, Pakistan, Philippines, Malaysia, Bangladesh, Thailand, Singapore are included in Aisa
Source: Pharmcube, DB

Strong opposition from local industry players is expected. While some view Chinese biotechs as a threat to the US industry, others believe the potential legislation would actually harm Americans by restricting access to life-saving drugs. Moreover, while the public and government are demanding cheaper drugs in the US, this legislation would seemingly incur higher R&D expenses for pharmaceutical companies.

Continued out-licensing momentum in 5M26. Upfront payments reached USD4,833mn (+93% YoY) in 5M26, already representing approximately 68% of

2025's total. There were 93 deals, an increase of $31\%$ YoY. The upfront payment in May was significant, totaling USD1,250mn, mainly contributed by deals between Hengrui and BMS, and Innovent and Pfizer.

Figure 6: Out-licensing deals in China   
![](images/028913ac8dbdfba6c3635c5a9932d51777dbe618d264f07b8b988bf0f514d822.jpg)

<details>
<summary>bar_line</summary>

| Month | Upfront payment (USD mn) | Number of deals |
|---|---|---|
| Jan-25 | 324 | 26 |
| Feb-25 | 97 | 7 |
| Mar-25 | 475 | 12 |
| Apr-25 | 187 | 15 |
| May-25 | 1,420 | 23 |
| Jun-25 | 386 | 12 |
| Jul-25 | 620 | 11 |
| Aug-25 | 1,082 | 12 |
| Sep-25 | 290 | 17 |
| Oct-25 | 1,502 | 20 |
| Nov-25 | 95 | 19 |
| Dec-25 | 675 | 19 |
| Jan-26 | 2,265 | 30 |
| Feb-26 | 858 | 16 |
| Mar-26 | 310 | 15 |
| Apr-26 | 150 | 19 |
| May-26 | 1,250 | 13 |
</details>

Source : Pharmcube, DB

Figure 7: Out-licensing deals in China   
![](images/c8207fe245bc352963523a23e1dcb00fec85116382f34eb5ae54d998a1d1b8c0.jpg)

<details>
<summary>bar_line</summary>

| Year | Upfront payment (USD mn) | Number of deals |
|---|---|---|
| 2019 | 10 | 37 |
| 2020 | 575 | 74 |
| 2021 | 1,693 | 65 |
| 2022 | 1,459 | 74 |
| 2023 | 3,600 | 115 |
| 2024 | 4,139 | 131 |
| 2025 | 7,229 | 193 |
| 5M26 | 4,833 | 93 |
</details>

Source : Pharmcube, DB

Figure 8: Companies under coverage 

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Recommendations</td><td rowspan="2">Price (LC)</td><td rowspan="2">Price target (LC)</td><td rowspan="2">Mkt cap (HK$ mn)</td><td rowspan="2">2025</td><td colspan="3">PER</td><td colspan="3">PBR</td></tr><tr><td>2026E</td><td>2027E</td><td>2025</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>WuXi AppTec Co Ltd</td><td>2359</td><td>BUY</td><td>124.50</td><td>167.40</td><td>338,925</td><td>13.5</td><td>18.0</td><td>15.3</td><td>3.4</td><td>3.5</td><td>2.9</td><td></td></tr><tr><td>BeOne Medicines Ltd</td><td>6160</td><td>BUY</td><td>163.00</td><td>213.00</td><td>261,805</td><td>156.3</td><td>41.0</td><td>27.7</td><td>7.6</td><td>5.8</td><td>4.6</td><td></td></tr><tr><td>Hansoh Pharmaceutical Group Co</td><td>3692</td><td>BUY</td><td>29.26</td><td>44.00</td><td>177,437</td><td>34.8</td><td>25.8</td><td>23.3</td><td>5.5</td><td>3.9</td><td>3.5</td><td></td></tr><tr><td>Shenzhen Mindray Bio-Medical E</td><td>300760</td><td>BUY</td><td>144.39</td><td>252.00</td><td>175,064</td><td>28.4</td><td>19.2</td><td>17.0</td><td>6.1</td><td>4.1</td><td>3.6</td><td></td></tr><tr><td>Wuxi Biologics Cayman Inc</td><td>2269</td><td>BUY</td><td>32.74</td><td>48.00</td><td>135,577</td><td>23.1</td><td>19.4</td><td>16.1</td><td>2.5</td><td>2.1</td><td>1.8</td><td></td></tr><tr><td>Innovent Biologics Inc</td><td>1801</td><td>BUY</td><td>76.60</td><td>126.00</td><td>133,149</td><td>142.6</td><td>48.0</td><td>30.3</td><td>6.1</td><td>5.2</td><td>4.3</td><td></td></tr><tr><td>Sino Biopharmaceutical Ltd</td><td>1177</td><td>BUY</td><td>4.65</td><td>8.50</td><td>87,166</td><td>42.8</td><td>18.2</td><td>15.8</td><td>3.4</td><td>2.1</td><td>1.8</td><td></td></tr><tr><td>Akeso Inc</td><td>9926</td><td>BUY</td><td>93.80</td><td>162.00</td><td>86,403</td><td>N/A</td><td>2,795.9</td><td>70.3</td><td>10.1</td><td>8.0</td><td>7.2</td><td></td></tr><tr><td>Remegen Co Ltd</td><td>9995</td><td>HOLD</td><td>70.60</td><td>95.00</td><td>56,517</td><td>50.1</td><td>10.5</td><td>38.6</td><td>10.1</td><td>4.8</td><td>4.4</td><td></td></tr><tr><td>Pharmaron Beijing Co Ltd</td><td>3759</td><td>BUY</td><td>16.48</td><td>26.90</td><td>45,241</td><td>30.1</td><td>12.5</td><td>10.1</td><td>3.4</td><td>1.5</td><td>1.3</td><td></td></tr><tr><td>XtalPi Holdings Ltd</td><td>2228</td><td>BUY</td><td>7.50</td><td>12.10</td><td>32,275</td><td>283.1</td><td>N/A</td><td>196.5</td><td>3.9</td><td>2.9</td><td>2.9</td><td></td></tr><tr><td>United Laboratories Internatio</td><td>3933</td><td>BUY</td><td>8.68</td><td>13.40</td><td>17,126</td><td>9.4</td><td>11.8</td><td>9.4</td><td>1.1</td><td>0.8</td><td>0.7</td><td></td></tr><tr><td>Guangzhou Innogen Pharmaceutic</td><td>2591</td><td>BUY</td><td>10.01</td><td>34.60</td><td>4,573</td><td>N/A</td><td>N/A</td><td>66.6</td><td>11.0</td><td>4.4</td><td>4.4</td><td></td></tr><tr><td>HUTCHMED China Ltd</td><td>HCM</td><td>BUY</td><td>11.17</td><td>24.40</td><td>1,949</td><td>N/A</td><td>43.3</td><td>22.3</td><td>N/A</td><td>2.0</td><td>1.9</td><td></td></tr></table>

Source : DB estimates, Bloomberg Finance LP; Based on closing price on 5 June 2026

# Appendix 1

# Important Disclosures

\*Other information available upon request

\*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

# Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst about the subject issuers and the securities of those issuers. In addition, the undersigned lead analyst has not and will not receive any compensation for providing a specific recommendation or view in this report. Cyrus Ng.

Equity rating dispersion and banking relationships   
![](images/e9ee87a01eb38e141427e7a659c717701901bbaa5c9abba146b0da4f673d97b9.jpg)

<details>
<summary>bar</summary>

| Category | companies covered (%) | Cos. w/ Banking Relationship (%) | MIFID Investment & Ancillary Services (%) |
|---|---|---|---|
| BUY | 81 | 30 | 67 |
| HOLD | 15 | 16 | 56 |
| SELL | 4 | 0 | 50 |
Asia Universe
</details>

![](images/5f0b4c7fd4ad882376d60829f2e40a2577293090bb9568fdeb6878c87950500d.jpg)

<details>
<summary>bar</summary>

DBSI companies under coverage
| Category | companies covered (%) | Cos. w/ Banking Relationship (%) | MIFID Investment & Ancillary Services (%) |
| :--- | :--- | :--- | :--- |
| BUY | 57 | 42 | 61 |
| HOLD | 43 | 36 | 52 |
| SELL | 0 | 0 | 67 |
</details>

# Equity Rating and Dispersion Key

The Equity Rating Dispersion Chart depicts the following:

The proportion of recommendations that are rated "buy", "sell" and "hold" over the previous 12 months. This is shown for securities issued in the stated region e.g. "Europe Universe". See rating definitions below. This is represented by the "Companies Covered" bars in the chart. The percentage value displayed above the bar is the proportion as a percentage. E.g. $50\%$ above the "buy" / "Companies Covered" bar means that $50\%$ of DB's equity research covered companies over the past 12 months have a "buy" rating.

Next to each of the three respective bars showing the proportion of "buy", "sell" and "hold" recommendations we provide two additional bars to show:

\- The proportion of "buy", "sell" or "hold recommendations where DB and or/Affiliates provided MIFID Investment or Ancillary Services in the past 12 months. This is represented in the "MIFID Investment and Ancillary Services" bar. The percentage value displayed above the bar shows the proportion of Companies Covered with the given rating where DB has also provided MIFID Investment and Ancillary Services in the past 12 months. E.g. $50\%$ above the "Cos. w/ MIFID Investment and Ancillary Services" bar means $50\%$ of the Companies Covered with the rating stated have also received MIFID Investment and Ancillary Services from DB.

\- The proportion of "buy" (or "sell" or "hold") recommendations where DB and or/Affiliates has provided Investment Banking services in the past 12 months for which it has received compensation. The percentage value displayed above the bar shows the proportion of Companies Covered with the stated rating where DB has also provided Investment Banking services in the past 12 months. E.g. $50\%$ above the "Cos. w/ Investment Banking relationship" bar means $50\%$ of the Companies Covered with the rating stated also have an Investment Banking Relationship with DB.

Buy: Based on a current 12- month view of TSR, we recommend that investors buy the stock.

Sell: Based on a current 12-month view of TSR, we recommend that investors sell the stock.

Hold: We take a neutral view on the stock 12-months out and, based on this time horizon, do not recommend either a Buy or Sell.

TSR = Total Shareholder Return. Percentage change in share price from current price to projected target price plus projected dividend yield

Newly issued research recommendations and target prices supersede previously published research.

# Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. DB and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of DB AG and its affiliates, which includes investment banking, trading and principal trading revenues.

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of DB and are subject to change without notice. DB provides liquidity for buyers and sellers of securities issued by the companies it covers. DB analysts sometimes have shorter-term trade ideas that may be inconsistent with DB's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website (https://research.db.com/Research/), and can be found on the general coverage list and also on the covered company's pag

[中间内容因长度限制已省略]

 site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau   
Group Chief Economist and Global Head of Research 

<table><tr><td>Pam Finelli 
Global Chief Operating Officer Research</td><td>Steve Pollard 
Global Head of Company Research and Sales</td><td>Jim Reid 
Global Head of Macro and Thematic Research</td><td>Tim Rokossa 
Head of Germany Research</td></tr><tr><td>Gerry Gallagher 
Head of European 
Company Research</td><td>Matthew Barnard 
Head of Americas 
Company Research</td><td>Peter Milliken 
Head of APAC 
Company Research</td><td>Debbie Jones 
Global Head of Sustainability and Data Innovation, Research</td></tr><tr><td>Sameer Goel 
Global Head of EM &amp; APAC Research</td><td>Francis Yared 
Global Head of Rates Research</td><td>George Saravelos 
Global Head of FX Research</td><td>Peter Hooper 
Vice-Chair of Research</td></tr></table>

International Production Locations 

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields</td><td>The DB Center</td><td>Filiale Singapur</td><td></td></tr><tr><td>London EC2Y 9DB</td><td>1 Columbus Circle</td><td>One Raffles Quay, South</td><td></td></tr><tr><td>United Kingdom</td><td>New York, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>
"""
