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
Source: Bloomberg, Baiinfo, Bernstein analysis and estimates

# Bernstein Energy & Power: Taking it to the NaX. Are sodium-ion batteries the key to solar baseload power?

Neil Beveridge, Ph.D. +852 2123 2648 neil.beveridge@bernsteinsg.com

Nikhil Nigania +91 226 842 1414 nikhil.nigania@bernsteinsg.com

Deepa Venkateswaran, ACA +44 20 7676 6990 deepa.venkateswaran@bernsteinsg.com

Guillaume Delaby +33 1 42 13 62 29 guillaume.delaby@bernsteinsg.com

Bob Brackett, Ph.D. +1 917 344 8422 bob.brackett@bernsteinsg.com

## Taking it to the NaX. Are sodium-ion batteries the key to solar base load power?

Our recent travels in Europe have highlighted two things. Firstly, how hot and sunny it is. In Germany this month roughly 25% of power generation came from solar while in Spain solar share of power generation reached as high as 70% on June 6th. Secondly, client interest in energy storage and particularly sodium-ion batteries has been eye-opening. Many will be aware sodium-ion batteries are the latest technology breakthrough in the battery market. As Elon Musk likes to point out, making batteries out of sodium and iron which are two of the most abundant elements in the earth's crust (unlike lithium and cobalt), seems like a smart thing to do. The challenge up to now is that making a sodium-ion battery has been expensive. Not because of the cost of the materials, but because of the complexity of the cathode and anode technology. This changed last year with a rapid reduction in the cost of sodium-ion cathodes. While sodium-ion batteries are still as expensive as LFP, all indications suggest they will get cheaper as battery makers scale up production. Robin Zeng, the Chairman of CATL, believes that the cost of sodium-ion batteries will fall to US\$50/kWh, which is lower than the US\$80-90/kWh for LFP and almost half the cost of NMC batteries at over US\$100/kWh.

EXHIBIT 1: Sodium-ion battery prices are expected to match LFP in 2026 and gain further cost advantage thereafter  
![](images/ae747c24b51907e2f11e7cc07ab28ac3be1c96cb1afcdd022424401a6c21a156.jpg)  
Estimated for 2026-2030

For polyanion-based sodium-ion batteries Source: Baiinfo, Bernstein analysis

Given that industrial grade sodium costs around US\$5000/t compared to lithium carbonate at over US\$20,000/t, the cost savings are obvious. But the advantages of sodium-ion batteries go beyond just cost. Firstly, the number of cycles that can be achieved with sodium-ion batteries are twice that of LFP. While an LFP battery may be capable of 6,000-8,000 cycles, a Na-ion battery can achieve 15,000 cycles. This means it is possible to charge and discharge a battery twice a day for 20 years, allowing them to be paired directly with solar and wind over the life of the project with no replacement needed. It also means that on a US \$/kWh/cycle basis, Na-ion could be one third the cost of LFP. Secondly, Na-ion batteries are lower temperature, which means that safety performance is better with thermal runaway limited to temperatures of around 200deg C. Thirdly, Na-ion batteries have better performance at low temperatures. According to CATL, energy retention is greater than $92\%$ at temperatures as low as -20deg C. Finally, while Na has a lower energy density than Li, the overall energy density of Na-ion batteries is getting close to LFP. The CATL Naxtra battery has an energy density of $185\mathrm{Wh/kg}$ at the pack level, which approaches that of LFP (190-210Wh/kg) making Na-ion batteries a serious challenger in the more price-sensitive mass vehicle market.

EXHIBIT 2: Based on the spot battery component prices, the cost of sodium-ion battery declined 15% yoy from US\$66/kWh to US\$55/kWh now  
![](images/7bcd8c2c8ac168d6e09d5b99aa4eafd290b05f131adad2cf1380a3349070d9c1.jpg)

The key benefit which Na-ion batteries bring is lower cost. We believe that this can significantly enhance the penetration of renewable energy and substantially increase the total addressable market for batteries. As everyone knows, solar and wind power is cheap, but not when the sun doesn't shine or the wind doesn't blow. The only way to make renewable power cheaper and more effective is to reduce energy storage costs. While lithium-ion batteries are the obvious way to do this, the problem is the high cost of storage. In 2020, it was not uncommon for a BESS to cost US \$500/kWh. This means that 1kW of capacity with 4 hour storage would cost US\$2000, which is almost the same cost as a combined cycle gas turbine plant (US\$2000/kW). Today, the cost of ESS has fallen along with LFP battery costs to around US\$150/kW (battery plus inverter and balance of plant). At the same time, given the demand growth for gas turbines, the capital cost of a gas-fired power plant has increased to as high as US\$4000/kW. Assuming

US $W1000/kW$ for a solar module, this means that solar plus 20 hours of battery storage (20 x US $150/kW = US3000/kW$ ) could cost as much as a combined cycle gas fired power plant CCGT(US $4000/kW$ ). But assuming that the cost of Na-ion batteries falls to as low as US $50/KW$ , then solar plus battery storage could be even cheaper. It could be possible in the near future that the cost of solar plus 48 hours of Na-ion storage could be as cheap as a gas-fired power plant. On our analysis, the break-even gas price for solar (US $550/kW$ ) paired with a Na-ion ESS system (US $100/KWh$ ) and a CCGT US $2,500/kW$ could be as low as US $5/mscf$ . At a CCGT with a cost of US $4000/kW$ the breakeven could be as low at US $2/mscf$ . This is not to say that 12 hours of storage would suffice in every location, but the cheaper battery storage becomes the higher the penetration could be.

EXHIBIT 3: Solar with Na-ion storage could compete with CCGT at \$2-5/mmcf gas price  
Levelized cost of electricity (US\$/MWh)
Solar + Storage (12hrs) vs Combined-Cycle Gas Plant  
![](images/fbb31c4bb76d807cfb17bfaf7340857a4ee4b0ce372ac8efc3af43aa55ae4894.jpg)  
Source: Bernstein analysis

Already in the UAE, Masdar is developing the world first baseload power project with solar and storage. In the project, solar will be paired with 19GWh of battery storage to provide continuous base load solar power for a 1GW of power with a 99.7% power reliability. As battery storage costs come down, longer duration solar plus battery projects could emerge as more serious competitors to gas for baseload power. This could not only expand the penetration of solar and wind in the grid, but it will help lower power prices and could lead to a significant expansion of battery storage. As of last year there was almost 5,000GW of combined installed solar and wind capacity worldwide.

EXHIBIT 4: Assuming every GW of solar and wind capacity is backed up by 1GW of ESS with 10 hours duration, this could amount to a cumulative demand of 100,000GWh  
![](images/3057c21cce8504f9512b63e1b34f260b4144153c1678e33876c6558549d9c4e6.jpg)  
Source: Bloomberg, Bernstein estimates and analysis

By 2030, we think this number could reach close to 10,000GW. Assuming every GW of solar and wind capacity is backed up by 1GW of battery capacity with a duration of 10 hours this could amount to a cumulative demand of 100,000GWh. This is two orders of magnitude more than the 700GWh of cumulative installed battery capacity that exists today and would imply significant

upside to the 1000GWh of annual capacity additions we expect this year.

The key investment implication is that Na-ion batteries could enable a step change reduction in energy storage costs allowing solar and wind to not only increase their penetration in the grid but also

to compete more effectively with gas for baseload power supply. This is positive for renewables supply chains but in particular CATL which is the industry leader in Na-ion battery technology and with their recently announced TENER sodium-ion storage system, likely to be an early winner.

## BERNSTEIN TICKER TABLE

<table><tr><td colspan="3"></td><td colspan="2">24 Jun 2026</td><td>TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>300750.CH (CATL)</td><td>O</td><td>CNY</td><td>395.36</td><td>800.00</td><td>17.5%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>24.5</td><td>18.0</td><td>13.7</td></tr><tr><td>3750.HK (CATL)</td><td>M</td><td>HKD</td><td>721.50</td><td>770.00</td><td>88.8%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>38.8</td><td>28.6</td><td>21.8</td></tr><tr><td>051910.KS (LG Chem)</td><td>M</td><td>KRW</td><td>298,000</td><td>298,000</td><td>0.9%</td><td colspan="2">KRW(13,258.70)</td><td>3,030.56</td><td>27,968</td><td>(22.5)</td><td>98.3</td><td>10.7</td></tr><tr><td>373220.KS (LGES)</td><td>M</td><td>KRW</td><td>366,000</td><td>347,000</td><td>(16.5)%</td><td>KRW</td><td>(5,308.10)</td><td>1,811.04</td><td>9,452.97</td><td>(69.0)</td><td>202.1</td><td>38.7</td></tr><tr><td>006400.KS (SDI)</td><td>M</td><td>KRW</td><td>490,500</td><td>520,000</td><td>140.3%</td><td>KRW</td><td>(9,933.80)</td><td>2,099.51</td><td>18,376</td><td>(49.4)</td><td>233.6</td><td>26.7</td></tr><tr><td>247540.KS (EcoPro BM)</td><td>U</td><td>KRW</td><td>151,800</td><td>140,000</td><td>4.7%</td><td>KRW</td><td>403.00</td><td>854.00</td><td>1,963.00</td><td>376.7</td><td>177.8</td><td>77.3</td></tr><tr><td>300274.CH (Sungrow)</td><td>O</td><td>RMB</td><td>154.80</td><td>185.00</td><td>96.0%</td><td>RMB</td><td>6.55</td><td>8.22</td><td>9.33</td><td>23.6</td><td>18.8</td><td>16.6</td></tr><tr><td>002466.CH (Tianqi Lithium)</td><td>O</td><td>CNY</td><td>66.13</td><td>80.00</td><td>70.5%</td><td>CNY</td><td>0.28</td><td>3.90</td><td>7.75</td><td>234.3</td><td>16.9</td><td>8.5</td></tr><tr><td>9696.HK (Tianqi Lithium)</td><td>O</td><td>HKD</td><td>43.32</td><td>65.00</td><td>18.2%</td><td>CNY</td><td>0.28</td><td>3.90</td><td>7.75</td><td>133.3</td><td>9.6</td><td>4.9</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,996.75</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action. Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

\- Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within $+/-10$ pp

• Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as 'Feature' (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Ban

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
