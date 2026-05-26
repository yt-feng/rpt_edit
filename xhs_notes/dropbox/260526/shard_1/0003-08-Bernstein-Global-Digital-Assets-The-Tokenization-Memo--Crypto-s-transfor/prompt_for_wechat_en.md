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
# Global Digital Assets

Gautam Chhugani +91 226 842 1416 gautam.chhugani@bernsteinsg.com

Mahika Sapra +91 226 842 1408 mahika.sapra@bernsteinsg.com

Sanskar Chindalia +91 226 842 1445 sanskar.chindalia@bernsteinsg.com

Harsh Misra +91 226 842 1457 harsh.misra@bernsteinsg.com

# The Tokenization Memo: Crypto's transformation to real world assets (1/n)

We are extending the Digital Assets memo to include three mega trends within our coverage - Tokenization, Stablecoins, Prediction Markets. Expect to see a weekly memo (rotating between tokenization, stablecoins and prediction markets) covering the latest industry dashboards, news and market commentary. The Digital Assets memo shall continue to cover the latest in crypto markets.

Tokenized RWA Industry Metrics - Tokenized real-world assets (RWA) are digital representation of real world assets like credit, equities, treasuries, commodities etc. on blockchain. Market cap of tokenized real-world assets has crossed \$51Bn (up 42% YTD), demonstrating strong resilience vs broader crypto markets that are down \~15% YTD (Exhibit 1). Private credit remains the dominant asset class at \~44% of total RWA market cap, followed by US Treasury at \~30% and commodities at \~14% (Exhibit 2). Ethereum and Provenance continue to host the bulk of onchain RWA activity, representing \~75% of total tokenized assets (Exhibit 5). Total RWA asset holders have crossed 810K, up \~40% YTD (Exhibit 7). We highlight recent trends on RWA tokenization:

1. RWA traction on Hyperliquid: Hyperliquid has emerged as leading venue for onchain RWA derivatives, with RWA open interest reaching an all-time high of \$2.6Bn in May. Hyperliquid's HIP-3 upgrade allows builder/developers to list perpetual futures referencing real world assets like equities, commodities, currencies etc. Developers can stake HYPE tokens and launch their own perpetual markets with Hyperliquid acting as the infrastructure layer. RWA derivatives on Hyperliquid has rapidly scaled up with HIP-3 now representing \~35% of total Hyperliquid perpetuals volume in less than eight months of launch (Exhibit 4). In April'26, RWA derivatives contributed \$65Bn volumes on Hyperliquid led by commodities (metals and oil) and indices (Exhibit 3).

2. Growing institutional participation in equity tokenization: The SEC has delayed the 'innovation exemption' on tokenized stocks that would have established a clear regulatory framework for third-party issued digital stock tokens. However, both crypto and traditional players are building tokenized equity offering that already fits within the existing SEC rules through the issuer-led model for equity tokenization. These blockchain native equity tokens represent real equity in the company and tokenholders are the registered shareholders with the transfer agents and hence are entitled to all the rights associated with share ownership (voting, dividends, corporate actions etc.). The penetration of tokenized equities remains nascent with just \~\$1.5Bn in tokenized stocks currently outstanding and \$3Bn monthly transfer volumes (Exhibit 9). We highlight recent moves by industry participants:

- Bullish has entered into a definitive agreement to acquire Equiniti, a global transfer agent serving \~3,000 issuer clients. This acquisition allows Bullish to operate a unified ledger recording ownership for both traditional and tokenized shares, and provides a ready target client base to accelerate the rollout of its issuer-led equity tokenization offering.   
- DTCC is collaborating with 50+ financial services firms, including Citi, Canton Network, Charles Schwab and JPM, to launch tokenization services for DTCC-custodied assets. The service is expected to launch in Oct'26.   
- Securitize has partnered with Jump Trading and Jupiter to launch fully onchain and regulated trading of tokenized equities. Jump will provide liquidity and price discovery, Jupiter handles distribution, and Securitize brings end-to-end regulatory infrastructure.

- NYSE has entered into an MoU with Securitize to develop digital transfer agent infrastructure supporting NYSE's upcoming tokenized securities platform, with Securitize designated as its first digital transfer agent.   
- Figure has announced the listing of OpenWorld's securities on OPEN (On-chain Public Equity Network), marking the second equity issuance on OPEN after Figure's own blockchain shares.

3. Figure leads tokenized credit growth: Onchain private credit assets continue to demonstrate robust growth, led by Figure (FIGR). Figure's credit and tokenization infrastructure is driving institutional adoption of tokenized credit, supported by a network of 380+ loan originators and 15+ bluechip private credit investors. In CY26 YTD, Figure alone has tokenized \$5Bn consumer loans on blockchain, with an all-time high monthly loan volume of \$1.3Bn in April'26 (Exhibit 8). Figure's blockchain marketplace for credit (Connect) contributed 56% of total loan volumes in Q1'26. Democratized Prime is Figure's blockchain alternative to traditional warehouse that allows originators to access DeFi and institutional capital pools for short-term financing at attractive rates (SOFR+200bps recently).

4. Asset managers adopt onchain funds: Tokenized money market funds and treasury products have emerged as the entry point for bluechip asset managers to launch onchain funds. Tokenization enables fund managers to offer instant subscriptions and redemptions, atomic settlement and programmable yield distribution, replacing the T+1/T+2 NAV cycle with real-time onchain execution. Blackrock's BUIDL fund has grown to >\$2.5Bn in AUM and Blackrock is planning to launch two new tokenized funds on blockchain. Standard Chartered and OKX now allow clients to post BUIDL as trading margin without forfeiting yield, integrating tokenized collateral with trading markets.

# RWA TOKENIZATION DASHBOARD

EXHIBIT 1: Tokenized RWA - Market Cap (\$Bn)   
![](images/92646da07ce3b941ddfa52e0ac4720bc31f85f531a072a5593a456c5cbcba23e.jpg)

<details>
<summary>area</summary>

| Date    | Private Credit | US Treasury Debt | Commodities | Stock | Others |
|---------|----------------|------------------|-------------|-------|--------|
| May-26  | ~$51Bn         | ~$4.5Bn          | ~$3.5Bn     | ~$2.5Bn | ~$1.5Bn |
</details>

Private credit includes Figure tokenized credit  
Source: RWA.xyz, Bernstein analysis

EXHIBIT 2: Tokenized RWA market cap split by asset class   
Tokenized RWA - Asset Class Split (%)   
![](images/6f6db226b2ec2c2a7c655f382925a49b7cc3a8e2973fe908d1f942c00402e32e.jpg)

<details>
<summary>bar_stacked</summary>

| Month | Private Credit (%) | US Treasury Debt (%) | Commodities (%) | Stock (%) | Others (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Jan-25 | ~60 | ~18 | ~7 | ~1 | ~1 |
| Feb-25 | ~60 | ~17 | ~7 | ~1 | ~1 |
| Mar-25 | ~63 | ~16 | ~7 | ~1 | ~1 |
| Apr-25 | ~60 | ~17 | ~7 | ~1 | ~1 |
| May-25 | ~58 | ~18 | ~7 | ~1 | ~1 |
| Jun-25 | ~55 | ~19 | ~7 | ~1 | ~1 |
| Jul-25 | ~55 | ~19 | ~7 | ~1 | ~1 |
| Aug-25 | ~56 | ~18 | ~7 | ~1 | ~1 |
| Sep-25 | ~54 | ~19 | ~7 | ~1 | ~1 |
| Oct-25 | ~53 | ~19 | ~7 | ~1 | ~1 |
| Nov-25 | ~50 | ~20 | ~8 | ~1 | ~1 |
| Dec-25 | ~51 | ~19 | ~8 | ~1 | ~1 |
| Jan-26 | ~50 | ~19 | ~8 | ~1 | ~1 |
| Feb-26 | ~48 | ~20 | ~9 | ~1 | ~1 |
| Mar-26 | ~47 | ~20 | ~9 | ~1 | ~1 |
| Apr-26 | ~45 | ~20 | ~9 | ~1 | ~1 |
| May-26 | ~44 | ~20 | ~9 | ~1 | ~1 |
The chart displays a stacked area chart with categories: Private Credit (cyan), US Treasury Debt (blue), Commodities (gray), Stock (dark green), and Others (dark blue). The values for each category are labeled on the chart. The percentages above each segment are annotated: Private Credit at 44%, US Treasury Debt at 30%, Commodities at 14%, Stock at 14%, and Others at 14%. The chart is created from Jan-25 through May-26. The data is already in English.
</details>

Source: RWA.xyz, Bernstein analysis

EXHIBIT 3: Commodities and Indices dominate HIP-3 trading volumes   
HIP-3 Trading Volumes - By Assets (\$Bn)   
![](images/c907dec099f67dd37cdcb9bf2084fa98bad6b8fc28d6a5ed2bc6ea980f1f6f6c.jpg)

<details>
<summary>bar_stacked</summary>

| Month | Commodities | Indices | Equity | Others |
|---|---|---|---|---|
| Oct-25 | 1 | 0 | 0 | 0 |
| Nov-25 | 0 | 4 | 1 | 0 |
| Dec-25 | 0 | 6 | 1 | 8 |
| Jan-26 | 13 | 7 | 1 | 5 |
| Feb-26 | 22 | 9 | 2 | 7 |
| Mar-26 | 42 | 13 | 3 | 10 |
| Apr-26 | 40 | 13 | 3 | 7 |
</details>

Source: The Block, Bernstein analysis

EXHIBIT 4: HIP-3 represented $35\%$ of hyperliquid perp volumes in April'26   
HIP-3 Volume Market Share of Hyperliquid Perpetuals (%) - April'26   
![](images/ce3644e79466ca3a13561f1c2a0fd04f28a526f7667c9061e6975b74c92ae37d.jpg)

<details>
<summary>pie</summary>

| Category | Percentage (%) |
| :--- | :--- |
| HIP 3 | 35 |
| Others | 65 |
</details>

Source: The Block, Bernstein analysis

EXHIBIT 5: Tokenized RWA split by blockchain network   
Tokenized RWA - Blockchain network split (%)   
![](images/4bb476c4b8f22bc133a0d53dd7903c985bb796e793f19cd58f56642f1e9db049.jpg)

<details>
<summary>pie</summary>

| Category | Percentage (%) |
| :--- | :--- |
| Ethereum | 39 |
| Provenance | 37 |
| BNB | 7 |
| Solana | 5 |
| Stellar | 4 |
| Others | 8 |
</details>

Source: RWA.xyz, Bernstein analysis

EXHIBIT 6: Top RWA tokenization platform 

<table><tr><td></td><td>Platform</td><td>Asset Class</td><td>Tokenized Assets ($Bn)</td></tr><tr><td>1</td><td>Figure</td><td>Private Credit</td><td>18.0</td></tr><tr><td>2</td><td>Securitize</td><td>Treasury, stocks</td><td>4.2</td></tr><tr><td>3</td><td>Paxos</td><td>Commodities</td><td>4.2</td></tr><tr><td>4</td><td>Ondo</td><td>Treasury, stocks</td><td>3.8</td></tr><tr><td>5</td><td>Circle</td><td>Treasury</td><td>3.0</td></tr><tr><td>6</td><td>Tether</td><td>Commodities</td><td>2.6</td></tr><tr><td>7</td><td>Franklin Templeton</td><td>Treasury</td><td>2.4</td></tr><tr><td>8</td><td>Spiko</td><td>Private Credit</td><td>1.8</td></tr><tr><td>9</td><td>Centrifuge</td><td>Treasury, credit</td><td>1.5</td></tr><tr><td>10</td><td>STOKR</td><td>Private Credit</td><td>1.5</td></tr></table>

Source: RWA.xyz, Bernstein analysis

EXHIBIT 7: Tokenized real world asset holders   
![](images/4d0d890186f18811b80a8861174c55687951605e69b48fedf1b5f9ace62af1c6.jpg)

<details>
<summary>bar</summary>

RWA Asset Holders (in '000)
| Month | RWA Asset Holders (in '000) |
|---|---|
| May-25 | 130 |
| Jun-25 | 270 |
| Jul-25 | 396 |
| Aug-25 | 436 |
| Sep-25 | 467 |
| Oct-25 | 517 |
| Nov-25 | 540 |
| Dec-25 | 578 |
| Jan-26 | 650 |
| Feb-26 | 675 |
| Mar-26 | 718 |
| Apr-26 | 743 |
| May-26 | 811 |
</details>

Source: RWA.xyz, Bernstein analysis

EXHIBIT 8: FIGR - Consumer loan volumes   
![](images/e36bf93b995adca42cbd2aa2ae7b97fbb2f9f4e3e22d3a3fd6e9e7ea8b84b667.jpg)

<details>
<summary>bar</summary>

Consumer loan volume ($Bn)
| Quarter | Consumer loan volume ($Bn) |
| :--- | :--- |
| Q1'25 | 1.4 |
| Q2'25 | 1.8 |
| Q3'25 | 2.5 |
| Q4'25 | 2.7 |
| Q1'26 | 2.9 |
| Q2'26 -QTD | 2.1 |
+7% QoQ +113% YoY; Q2'26 guidance $3.8-4.1Bn
</details>

Q2'26 actual loan volumes as of 15 May, 2026 sourced from Provenance Pulse API Source: Company filings, Bernstein analysis

EXHIBIT 9: Tokenized Equities - Monthly Transfer Volumes   
![](images/bf2b7e225950d69cb8c8591e459483814d890312d1423dd065bf951d0305e4e1.jpg)

<details>
<summary>bar</summary>

Tokenized Equity - Transfer Volumes ($Bn)
| Month | Tokenized Equity ($Bn) |
|---|---|
| Sep-25 | 0.5 |
| Oct-25 | 0.9 |
| Nov-25 | 1.1 |
| Dec-25 | 2.6 |
| Jan-26 | 1.8 |
| Feb-26 | 1.6 |
| Mar-26 | 3.0 |
| Apr-26 | 2.7 |
| May-26* | 2.8 |
</details>

\*As of May 25, 2026  
Source: RWA.xyz, Bernstein analysis

BERNSTEIN TICKER TABLE 

<table><tr><td colspan="3"></td><td rowspan="2">22 May 2026 Closing Price Target</td><td rowspan="2">Price</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>FIGR (Figure)</td><td>O</td><td>USD</td><td>33.95</td><td>67.00</td><td>NA</td><td>USD</td><td>0.54</td><td>0.98</td><td>1.52</td><td>62.9</td><td>34.6</td><td>22.3</td></tr><tr><td>BLSH (Bullish)</td><td>M</td><td>USD</td><td>35.18</td><td>50.00</td><td>NA</td><td>USD</td><td>0.09</td><td>0.07</td><td>0.14</td><td>406.9</td><td>484.1</td><td>251.4</td></tr><tr><td>COIN (Coinbase )</td><td>O</td><td>USD</td><td>184.99</td><td>330.00</td><td>(58.5)%</td><td>USD</td><td>4.85</td><td>5.97</td><td>13.20</td><td>38.2</td><td>31.0</td><td>14.0</td></tr><tr><td>HOOD (Robinhood)</td><td>O</td><td>USD</td><td>73.64</td><td>130.00</td><td>(12.2)%</td><td>USD</td><td>2.12</td><td>2.65</td><td>3.70</td><td>34.7</td><td>27.8</td><td>19.9</td></tr><tr><td>SBET (Sharplink)</td><td>O</td><td>USD</td><td>6.23</td><td>24.00</td><td>(36.1)%</td><td>USD</td><td>2.93</td><td>0.00</td><td>1.73</td><td>2.1</td><td>N/M</td><td>3.6</td></tr><tr><td>SPX</td><td></td><td></td><td>7,473.47</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended BLSH estimate is Adjusted EPS; BLSH valuation is Adjusted P/E (x); BLSH, SBET base year is 2024; Source: Bloomberg, Bernstein estimates and analysis.

# I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's "affiliates" relate to both SG and AB and their respective affiliates.

# VALUATION METHODOLOGY

# Figure Technology Solutions

We value FIGR on 25x EV/27E EBITDA, at a premium to traditional exchanges and crypto peers, led by FIGR's structural growth prospects as pure-play tokenization platform and profitable core lending business. We rate Figure Outperform (PT\$67).

# Bullish

We value BLSH using 34x EV/Adjusted EBITDA'27E, at a premium on COIN and HOOD, considering the early stage of business and wide array of growth opportunities ahead. We rate BLSH Market-Perform with PT \$50.

# Coinbase Global Inc.

We value COIN using a 25x Price/2027E Earnings, in-line with the average of similar crypto/fintech/broker peers, to arrive at our price target of \$330.

# Robinhood Markets Inc

Robinhood is scaling up rapidly and is a cyclical business. As a consequence, we value HOOD using a \~35x Price/2027E Earnings to arrive at our price target of \$130.

# Sharplink Gaming

We value SBET using a 10-year ETH treasury holding model based on our ETH forecasts and SBET's ETH growth strategy. We discount back the estimated 2035E SBET price to arrive at 2026E SBET equity, implying a long-term 15% premium to SBET's 2026E ETH treasury NAV. We rate SBET Outperform (PT\$24).

# RISKS

# Figure Technology Solutions

1. FIGR's business model involve some macro risks, for example, aggressive interest rate decline makes mortgage refinancing more competitive, impacting the demand for HELOCs.   
2. FIGR's business model is dependent on continued growth of private credit, any risks emerging leading to a slowdown in private credit could impact uptake for tokenized credit on Figure's marketplace.   
3. We expect non-HELOC loans to contribute $\sim 20\%$ of FIGR's total loan volumes by 2027E, any delay in expansion into new loan categories can affect Figure's loan growth.

# Bullish

Upside Risk to our price target include:

1. Early roll-out of BLSH's U.S and crypto derivatives business can front load the growth in their trading volumes vs our estimates. We expect Bullish to launch U.S spot trading in 2026E and roll out options trading (ex-US) in 2026E.

2. Rapid scaling of Bullish's subscription services (new multi-year liquidity services contract, increased index adoption etc.) can further grow the subscription revenue lines.

Downside risks to our price target include:

1. Risk of fresh competition from U.S based and international exchanges (e.g Coinbase, Binance) and brokers (e.g Robinhood, Schwab) causing pricing & market share pressure in the U.S as well as international markets.

2. We expect $\sim 15\%$ of Bullish's transaction revenues from U.S by 2027E, any delay in receiving the U.S NY DFS license, delaying the US spot or derivatives launch could affect U.S revenues.

3. Digital Assets are a new asset class with limited price history and often display high-beta volatility to changes in macro including any recessionary challenges in U.S.

# Coinbase Global Inc.

1. Risk of fresh competition from international exchanges (e.g., Binance) and brokers (e.g., Robinhood, Schwab) causing pricing & market share pressure in the US home market.

2. Any delay in passing key regulation to establish the Digital assets regulatory framework in the U.S including risk of regulatory volatility from political changes (e.g., mid-term US elections).

3. Digital Assets are a new asset class with limited price history and often display high-beta volatility to changes in macro including any recessionary challenges in the US.

# Robinhood Markets Inc

Robinhood faces regulatory risks on its revenue model, particularly its PFOF model from SEC and other regulatory bodies. This also applies to the crypto trading business.

SEC has historically been harsh on crypto trading businesses, with focus on token trading platforms, as some tokens maybe considered securities.

Digital assets are a new asset class, with limited price history i.e Bitcoin itself is less than 14 years old. The remaining digital assets industry reflected by smart contracts and other blockchain applications is even younger and still evolving into its utility phase.

# Sharplink Gaming

1. Digital Asset treasury management involves significant balance sheet and liquidity risk, if companies deploy short term callable debt. 

[中间内容因长度限制已省略]

learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient

makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
