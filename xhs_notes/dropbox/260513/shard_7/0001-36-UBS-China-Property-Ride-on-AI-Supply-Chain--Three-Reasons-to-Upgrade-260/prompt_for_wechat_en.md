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
# China Property

# Ride on AI Supply Chain; Three Reasons to Upgrade

# Demand: Rising industrial profits and positive PPI; Prefer tier 1 Cities

We are turning more positive on the China property sector, due to 1) increased housing demand visibility from rising industrial profits (AI supply chain) and positive PPI (our strategy note: Green shoots emerging?); 2) positive wealth effect from companies with rising profitability/share prices, and mapping of their headquarters indicates a strong concentration in Beijing and Shanghai; 3) falling vacancy rate in tier 1 Cities suburb districts, suggesting shadow inventory has been digested. In 2026, we expect property prices in tier 1 Cities to stabilize (previously -10%) and in tier 2 Cities to still decline by 5% (previously -10%). In 2027, we expect prices in tier 1 Cities to increase by 2% and in tier 2 Cities to stabilize (previously -5%). We upgrade COLI (added to Key Call list), BEKE, Jinmao and CMSK to Buy on their high exposure to tier 1 Cities. We also like CR Land for its high tier 1 Cities exposure and value unlock from asset securitization.

# Demand: Mapping the headquarters of emerging sectors/companies

The surge of AI-related materials, government anti-involution measures and export growth caused industrial profits to grow by 15% YoY in 1Q26 with positive PPI. Historically, industrial profits have a 0.63 correlation to tier 1 Cities property price. Among sectors, computer, communication, electronic equipment, non-ferrous metals and chemical sectors' profit surged the most and related sectors' share prices outperformed. Those companies' headquarters are located in Beijing, Shanghai, Suzhou and Dongguan, which is in line with a stronger secondary transaction volume YTD than other Cities. This makes us think the recovery this time could be different and more driven by improved profitability at industrial enterprises rather than policy previously.

# Supply: Falling vacancy rate in tier 1 Cities suburb districts vs three years ago

Apart from falling secondary listing in tier 1 Cities, vacancy rate in tier 1 Cities suburb districts improved compared to three years ago (2023), which we view as positive. Looking ahead, we expect a declining supply for commodity housing and social housing due to sUBStantial decline in new home starts/land sales during the past three years.

# Valuation: Further 30% upside potential

Despite recent share outperformance, we see potential for further 30% share price upside if the sector P/BV reverts to its 15-year average level of 0.85x, vs current trading P/BV at 0.66x. As the market recovery is more confined to tier 1 Cities, we prefer COLI, CMSK, Jinmao and BEKE for high tier 1 Cities exposure (\~41% vs peer group below 25%). We raise our price targets for CR Land and C&D and maintain our Buy ratings.

Figure 1: Rating and PT changes 

<table><tr><td rowspan="2">Company</td><td rowspan="2">Shr pr(LCY/shr)</td><td rowspan="2">Mkt cap(USD bn)</td><td colspan="3">Rating</td><td colspan="4">Price target(LCY/share)</td><td colspan="2">Earnings estimateNew vs Old</td><td colspan="2">P/BV</td><td colspan="2">PE</td></tr><tr><td>New</td><td>Old</td><td>Chg</td><td>New</td><td>Old</td><td>Chg</td><td>% upside</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td>COLI</td><td>16.0</td><td>22.4</td><td>Buy</td><td>Neutral</td><td>▲</td><td>25.00</td><td>13.80</td><td>81%</td><td>56%</td><td>14%</td><td>49%</td><td>0.38</td><td>0.38</td><td>13.0</td><td>11.4</td></tr><tr><td>BEKE</td><td>19.2</td><td>20.7</td><td>Buy</td><td>Neutral</td><td>▲</td><td>23.00</td><td>18.00</td><td>28%</td><td>20%</td><td>23%</td><td>30%</td><td>1.92</td><td>1.69</td><td>20.3</td><td>16.5</td></tr><tr><td>CMSK</td><td>9.7</td><td>12.8</td><td>Buy</td><td>Neutral</td><td>▲</td><td>12.00</td><td>9.80</td><td>22%</td><td>24%</td><td>-65%</td><td>-29%</td><td>0.89</td><td>0.87</td><td>75.1</td><td>30.4</td></tr><tr><td>Jinmao</td><td>1.9</td><td>3.3</td><td>Buy</td><td>Neutral</td><td>▲</td><td>2.30</td><td>1.50</td><td>53%</td><td>19%</td><td>-7%</td><td>42%</td><td>0.59</td><td>0.58</td><td>27.7</td><td>15.5</td></tr><tr><td>CR Land</td><td>38.1</td><td>34.7</td><td>Buy</td><td>Buy</td><td>■</td><td>45.00</td><td>36.00</td><td>25%</td><td>18%</td><td>4%</td><td>8%</td><td>0.78</td><td>0.74</td><td>10.2</td><td>9.7</td></tr><tr><td>C&amp;D International</td><td>18.2</td><td>5.2</td><td>Buy</td><td>Buy</td><td>■</td><td>21.00</td><td>17.00</td><td>24%</td><td>16%</td><td>-12%</td><td>6%</td><td>1.17</td><td>1.16</td><td>10.2</td><td>8.4</td></tr><tr><td>Greentown China</td><td>10.9</td><td>3.5</td><td>Buy</td><td>Buy</td><td>■</td><td>15.00</td><td>15.00</td><td>0%</td><td>37%</td><td>0%</td><td>0%</td><td>0.66</td><td>0.64</td><td>22.7</td><td>8.8</td></tr><tr><td>Seazen H</td><td>2.4</td><td>2.1</td><td>Buy</td><td>Buy</td><td>■</td><td>3.30</td><td>3.30</td><td>0%</td><td>40%</td><td>0%</td><td>0%</td><td>0.30</td><td>0.29</td><td>12.7</td><td>10.2</td></tr><tr><td>Simple Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>29%</td><td>29%</td><td>-5%</td><td>13%</td><td>0.84</td><td>0.79</td><td>24.0</td><td>13.9</td></tr></table>

Source: Company data, UBSe. Date as of 12 May 2026.

# Equities

China Emerging

Real Estate

John Lam, CFA

Analyst

john-za.lam@UBS.com

+852-2971 6358

Vera Gong, CFA

Analyst

vera.gong@UBS.com

+852-2971 8950

Mark Leung

Analyst

mark.leung@UBS.com

+852-2971 8636

Ben Ho

Associate Analyst

ben.ho@UBS.com

+852-3712 2819

# WHAT IS DIFFERENT THIS TIME?

# Breaking the negative feedback loop

Over the past five years, there have been false alarms on property recovery, due to a weak job market, enterprises' difficulties to make profit, and rising supply from shadow inventory (vacant property). Since there is a long supply chain related to the property sector, the decline in property sales/price acts as a further drag on industrial enterprise (IE) demand/profitability, i.e. more layoffs and lower income expectations, and hence is negative to housing demand. This causes a negative feedback loop and might explain why IE profit has a good correlation with tier 1 Cities property price at 0.63 correlation. See Figure 2 - Figure 4, and our strategy note on A-share Q126 earnings review.

Figure 2: A strong correlation between tier 1 Cities property price and IE profit   
![](images/1d4a3d1bf5fd79b5eecf292b26afb9984d604d8e7cab25aa2b03e86697986465.jpg)

<details>
<summary>line</summary>

| Date   | IE profit monthly rolling 12m | Tier-1 Cities property price index |
|--------|-------------------------------|------------------------------------|
| Jan-13 | 500                           | 400                                |
| May-13 | 550                           | 450                                |
| Sep-13 | 570                           | 480                                |
| Jan-14 | 580                           | 500                                |
| May-14 | 590                           | 520                                |
| Sep-14 | 600                           | 550                                |
| Jan-15 | 580                           | 580                                |
| May-15 | 570                           | 600                                |
| Sep-15 | 560                           | 620                                |
| Jan-16 | 550                           | 650                                |
| May-16 | 570                           | 700                                |
| Sep-16 | 580                           | 750                                |
| Jan-17 | 560                           | 800                                |
| May-17 | 550                           | 820                                |
| Sep-17 | 540                           | 830                                |
| Jan-18 | 530                           | 840                                |
| May-18 | 520                           | 850                                |
| Sep-18 | 510                           | 860                                |
| Jan-19 | 500                           | 870                                |
| May-19 | 490                           | 880                                |
| Sep-19 | 480                           | 890                                |
| Jan-20 | 470                           | 900                                |
| May-20 | 460                           | 910                                |
| Sep-20 | 450                           | 920                                |
| Jan-21 | 440                           | 930                                |
| May-21 | 430                           | 940                                |
| Sep-21 | 420                           | 950                                |
| Jan-22 | 410                           | 960                                |
| May-22 | 400                           | 970                                |
| Sep-22 | 390                           | 980                                |
| Jan-23 | 380                           | 990                                |
| May-23 | 370                           | 1000                               |
| Sep-23 | 360                           | 990                                |
| Jan-24 | 350                           | 980                                |
| May-24 | 340                           | 970                                |
| Sep-24 | 330                           | 960                                |
| Jan-25 | 320                           | 950                                |
| May-25 | 310                           | 940                                |
| Sep-25 | 300                           | 930                                |
| Jan-26 | 290                           | 920                                |
</details>

Source: NBS, Centraline, UBS

Figure 3: PPI in China picked up in Mar 2026 for the first time since Sept 2022   
![](images/f1dbdb21c2e23e88b2d6d10d6e8c45c17c4a2dd754f3c2ffa61b833257c33db4.jpg)

<details>
<summary>line</summary>

| Date   | Tier-1 Cities property price index | PPI YoY RHS |
|--------|------------------------------------|-------------|
| May-26 | 600                                | 2.8%        |
</details>

Source: NBS, Centraline, UBS.

Figure 4: All A-share profit (excl. financials, Sinopec & Petro China) recorded 12% growth in Q126   
![](images/575bd74efaba104e11582d383b9cbdaf86590e4b77682946bdb4ee304549e7b0.jpg)

<details>
<summary>line</summary>

| Date       | A share excl. financials, Sinopec & Petro China (quarterly) YoY |
| ---------- | --------------------------------------------------------------- |
| 3/1/2013   | ~15%                                                            |
| 9/1/2013   | ~25%                                                            |
| 3/1/2014   | ~10%                                                            |
| 9/1/2014   | ~-5%                                                            |
| 3/1/2015   | ~-20%                                                           |
| 9/1/2015   | ~-10%                                                           |
| 3/1/2016   | ~50%                                                            |
| 9/1/2016   | ~40%                                                            |
| 3/1/2017   | ~60%                                                            |
| 9/1/2017   | ~30%                                                            |
| 3/1/2018   | ~-5%                                                            |
| 9/1/2018   | ~-20%                                                           |
| 3/1/2019   | ~-30%                                                           |
| 9/1/2019   | ~-25%                                                           |
| 3/1/2020   | ~-40%                                                           |
| 9/1/2020   | ~-10%                                                           |
| 3/1/2021   | ~60%                                                            |
| 9/1/2021   | ~20%                                                            |
| 3/1/2022   | ~-20%                                                           |
| 9/1/2022   | ~-30%                                                           |
| 3/1/2023   | ~-40%                                                           |
| 9/1/2023   | ~-50%                                                           |
| 3/1/2024   | ~-60%                                                           |
| 9/1/2024   | ~-40%                                                           |
| 3/1/2025   | ~-30%                                                           |
| 9/1/2025   | ~-25%                                                           |
| 3/1/2026   | ~-15%                                                           |
</details>

Source: NBS, Centraline, UBS

# Which sectors drive industrial profit? AI-related

However, it seems the negative feedback loop is unwinding this year. In 1Q26, industrial enterprise profit grew by 15% YoY with rising PPI (Figure 3). Breaking down the industrial enterprise by sectors, the strongest profit growth is in AI-related sectors, i.e. manufacture of computers, communication and other electronic equipment. This sub-sector accounts for 13% of industrial profit, and grew by 125% YoY in 1Q26. Next are non-ferrous metals smelting & pressing, and chemical materials & products, due to rise in commodity prices, capacity reduction and government anti-involution campaign. If we break down the 15% growth in industrial profit, 8.2ppt is contributed by computer, communication & other electronic equipment (i.e. AI-related), 5.2ppt is from non-ferrous metal smelting & pressing, and 2.8ppt is from chemical materials & products. In addition, in April 2026, export growth accelerated to 14% YoY, and shipments of tech exports expanded 0.5% MoM (Figure 6). The continued strength in tech exports likely signals that China is becoming increasingly integrated into the AI supply chain.

Figure 5: Computer, communication & other electronic equipment contributed 8.2ppt to Q126 total profit growth   
![](images/871a9753c75b5ccaf8e39074780bb996bb7c61dacb2d53af6ad38216e2e30b67.jpg)

<details>
<summary>bar</summary>

Q126 industrial enterprise profit YoY growth contribution (%)
| Category | Contribution (%) |
| :--- | :--- |
| Total profit | 15.5 |
| Non Ferrous Metal Smelting & Pressing | 5.21 |
| Chemical Material & Product | 2.81 |
| Computer, Communication & Other Electronic Equipment | 8.19 |
| Other | -0.71 |
</details>

Source: CEIC, UBS

Figure 6: Tech dominated recent export growth, as of April 2026   
![](images/5ed44b7e63d2825bba51052aa11a5f0ee476a30785ee2565fdb18dbb086b418c.jpg)

<details>
<summary>line</summary>

| Date     | Hi-tech | Autos | Other products |
| -------- | ------- | ----- | -------------- |
| 4/2026   | 143     | 160   | 100            |
</details>

Source: CEIC, UBS estimate

# Where are they based? Beijing and Shanghai

Furthermore, we look at the stock market to see which companies outperformed the most and where they are located. There are 514 stocks with over Rmb10bn market cap whose share prices have increased by over 50% in the past 12 months. Most of them are located in Beijing, Shanghai and Shenzhen, followed by Suzhou and Chengdu. This is due to more AI or related supply chain companies being located in Beijing and Shanghai, which echoes with stronger secondary transactions in Beijing and Shanghai.

Figure 7: Beijing had 43 listed companies of Rmb10bn+ market cap with one-year return over 50%, followed by 50 in Shanghai and 48 in Shenzhen   
![](images/3528ff8290b8dfeaf95a90c634b544a89e7d1df5046c386a808c483b5809ffbf.jpg)

<details>
<summary>bar_line</summary>

Secondary transaction growth vs High growth stocks' market cap
| City | Market cap subtotal (rmb bn) | Secondary transaction 4M26 YoY - RHS (%) |
| :--- | :--- | :--- |
| Beijing | 8,981 | 18 |
| Shanghai | 4,623 | 14 |
| Shenzhen | 4,567 | 4 |
| Suzhou | 1,871 | 23 |
| Chengdu | 1,019 | -5 |
| Hangzhou | 698 | -25 |
| Guangzhou | 630 | -8 |
| Dongguan | 383 | 32 |
# of companies of Rmb10bn+ market cap with one-year return over 50%
</details>

Source: Wind, Bingshan, UBS. Note: Newly listed companies with a market cap of over Rmb10bn and a YTD performance above 50% are also included in our stock count.

# Improved vacancy rate for T1 Cities suburb districts

In the past five-year downcycle, inventory has been underestimated by the market, due to a rise in secondary listings and rental listings from vacant properties. In particular, the vacancy rate in suburb districts in tier 1 Cities was higher than city average due to more new home completions in those districts and speculative demand in the past. Those properties were resupplied to the rental or secondary market in 2022-25, which added to downward pressure in rental and property prices.

# Our take

In April 2026, we have seen an improvement in vacancy rate in those districts for four tier 1 Cities and Hangzhou, see Figure 8. We view this positively, as this means less supply shock to the secondary/rental market in future, i.e. a support to property/rental prices.

We attribute the improvement in vacancy rate to: 1) decline in new home completion in those districts over the past 1-2 years, 2) those vacant properties have been digested through rental or secondary transactions over the years. Looking ahead, we expect the supply from new home, secondary home, rental housing and government social housing should continue to decline, due to declining land sale, new starts and also the government's reduction of new build of social housing.

# Methodology

We collected the secondary listing data at individual districts among the five Cities from property portals in June 2023 and April 2026. We collected the data for both total secondary listing and bare shell listing, and use the \% of bare shell listing divided by total listing as a proxy for vacancy rate, as bare shell properties must be vacant. The April 2026 data showed a decline of 0.6-10.1ppt of vacant properties in suburban districts across tier 1 Cities and Hangzhou, compared to June 2023 data.

Figure 8: Vacancy rate in suburb districts across tier 1 Cities and Hangzhou have shown improvement after three years   
% of bare shell housing listing in suburb districts (2023 vs 2026)   
![](images/f554fb6bfd1e6333dcec7a6470ead8d42bf115dbdc6835e4644f677d7a24564c.jpg)

<details>
<summary>bar</summary>

| City | Jun-23 (%) | Apr-26 (%) |
| :--- | 

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, sUBSidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.UBS.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its sUBSidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/22fa7372c18df416231d3cab47f7061d207a1a80348758a18576a622de5a2071.jpg)
"""
