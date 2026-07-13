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
## Global Digital Assets

Gautam Chhugani +91 226 842 1416 gautam.chhugani@bernsteinsg.com

Mahika Sapra +91 226 842 1408 mahika.sapra@bernsteinsg.com

Sanskar Chindalia +91 226 842 1445 sanskar.chindalia@bernsteinsg.com

Harsh Misra +91 226 842 1457 harsh.misra@bernsteinsg.com

# The Tokenization Memo: Robinhood Chain's strong debut launch (3/n)

Robinhood Chain's launch expands Robinhood's product offering across tokenized stocks, decentralized lending and perpetual futures products. Strong early adoption highlights the growing convergence of tokenized real world assets with the broader DeFi ecosystem, as industry participants continue to innovate across multiple business models for regulated asset tokenization.

Tokenized RWA Industry Metrics - Market cap of tokenized real-world assets has grown from \$35Bn in 2025 YE to over \$51Bn today, up 50% YTD (Exhibit 6-Exhibit 7). Tokenized real world assets have demonstrated strong resilience vs broader crypto markets that are down \~25% YTD. Private credit remains the dominant asset class at 48% of total RWA market cap, followed by U.S. Treasuries (29%) and commodities (9%). Ethereum and Provenance continue to host the bulk of onchain RWA activity, representing \~70% of total tokenized assets (Exhibit 8). Total RWA asset holders have crossed 1Mn, up \~75% YTD (Exhibit 10).

## Robinhood Chain launches with strong traction across DeFi and tokenized assets

Robinhood launched the public mainnet of Robinhood Chain (link), expanding its product offering across tokenized stocks, decentralized lending and perpetual futures products. Early traction on the Robinhood Chain has been strong in terms of trading volumes and user adoption.

Robinhood Chain DEX volumes vs other chains: In the last 7 days, Robinhood Chain has grown to be among the Top 5 chains in terms of DEX volumes - with \$3.1Bn in cumulative DEX volumes over the last 7 days (Exhibit 3-Exhibit 4). Early trading volumes on Robinhood Chain were led by meme coins but shows strong liquidity and tractions from crypto native traders. Over time, Robinhood is focused on dominating RWA (equities, commodities and perpetual futures) trading with Robinhood Chain and Bitstamp's growing product suite and market liquidity. Since the launch of Robinhood Chain on July 1, over \~65K users now hold \$13Mn of stock tokens and \$300Mn in stablecoin balances on the chain (Exhibit 1-Exhibit 2).

Key partnerships and offerings: Robinhood Chain is an Arbitrum-based Ethereum L2, built for financial services, tokenized real world assets with a permissionless environment for blockchain builders. Robinhood's blockchain ecosystem is continuously growing with deep integration from industry players like Uniswap (liquidity protocol), Pleiades (prop trading), Lighter, Morpho, BitGo (not covered), and Chainlink. Key offerings include:

\- Stock tokens: Robinhood Chain integrates Robinhood's tokenized stocks with the broader DeFi ecosystem. The new stock tokens are now available in 120+ countries (not currently available in US), support 24x7 trading (on decentralized exchanges like Uniswap, Lighter etc.) and improves token utility as lending and trading collateral.

\- Decentralized lending: Robinhood has partnered with Morpho, allowing eligible US users to lend their USDG (dollar-backed stablecoin) directly on the main Robinhood app. Currently, users can earn up to 7% APY through Robinhood's decentralized lending product.

\- Perpetual futures: Eligible users can now access perpetual future contracts through Lighter, a decentralized exchange. Lighter is offering incentives for Robinhood users to trade perpetuals (committed \$11Mn of LIT tokens for the community).

## Custodial tokenized equity model - DeFi integration enhances token utility while regulated U.S models emerge

Equity tokenization continues to attract mainstream interest with tokenized equities growing 170% YTD from \$0.7Bn to \$1.9Bn. Multiple business models are being attempted for equity tokenization, while the industry still awaits regulatory clarity for securities tokenization including potential expectation of an ‘innovation exemption’. Broadly, the issuer-sponsored tokenization model uses blockchain native shares issued directly by the issuing company. While the custodial model involves a third party sponsor buying the underlying shares, custody them in a secured account and issuing a blockchain token against them.

Over the last few weeks, we have seen two major developments gaining momentum in the custodial equity tokenization model - leveraging DeFi ecosystem to enhance stock token utility and first live application of a U.S regulated custodial tokenization model. Robinhood Chain enables Robinhood to expand its custodial model for equity tokenization. So far, the stock tokens were only available in EU, with limited utility beyond tracking the price of the underlying shares. However, with Robinhood Chain, Robinhood issued stock tokens are now available in 120+ countries (not currently available in US). The stock tokens can be traded 24x7 on decentralized exchanges, used as collateral in trading, or deposited in lending pools for additional yield. This enhances the utility of broker-issued stock tokens vs previous model. Currently, \~\$13Mn stock tokens are held on Robinhood Chain, across 90+ stocks.

Recently, Ondo Finance (not covered) announced (link) the first third-party tokenized securities compliant with existing US regulations. Under this model, Ondo's registered transfer agent mints security tokens backed 1:1 by underlying shares. The tokenizer will receive the same shareholder rights - via a common voting and shareholder communication platform. Ondo has tokenized an ETF and a stock to demonstrate the application of this model.

EXHIBIT 1: Robinhood Chain TVL is currently dominated by stablecoins, with \$13Mn in tokenized stocks  
![](images/86d97a49926c8967a2ed94151f2b99afbe347289277cf24b40ba32a2d669b05c.jpg)  
Source: RWA.xyz, Bernstein analysis

EXHIBIT 2: RWA holders on Robinhood Chain have surpassed 67K users  
Robinhood Chain - RWA Holders (in '000s)  
![](images/d94afc67b5800c4063ab159804dd14d42dc180b9380a635a11c1708f26ad54a9.jpg)  
Source: RWA.xyz, Bernstein analysis

EXHIBIT 3: DEX volumes have crossed \$3Bn in last 7 days  
Top Chains by DEX Volumes (\$Bn) - Last 7 days  
![](images/05192aae264eb34422d047ed5691e979843c59bdce3121b9b074261fbfe69433.jpg)  
Source: DeFiLlama, Bernstein analysis

EXHIBIT 4: Robinhood Chain has surpassed leading chains in daily DEX volumes  
Top Chains by DEX Volumes (\$Mn) - Last 24 hrs  
![](images/aa5d7931ad53a1a76b8475b4cc2dfe4f4a50c050c34017e95087d2699ea63cf1.jpg)  
Source: DeFiLlama, Bernstein analysis

EXHIBIT 5: DeFi TVL has crossed \$100Mn in less than 15 days of launch on Robinhood Chain  
Robinhood Chain - DeFi TVL (\$Mn)  
![](images/027af125efa60a61b840ee78b3566133edf9670a0985ee96c523cd23df465d1c.jpg)  
Source: DeFiLlama, Bernstein analysis

RWA TOKENIZATION DASHBOARD
EXHIBIT 6: Tokenized RWA - Market Cap (\$Bn)  
![](images/b2ce0e209e2c5231af3468dff142c32f6d69c5f2cb385e32664a0e49a90d880a.jpg)  
Private credit also includes Figure tokenized credit  
Source: RWA.xyz, Bernstein analysis

EXHIBIT 7: Tokenized RWA market cap split by asset class  
![](images/708f59c6a993431b2ec68c72c7bb760e3cad9683862ce7fafb8bd3c4dc32616b.jpg)  
Private credit includes Figure tokenized credit
Source: RWA.xyz, Bernstein analysis

## EXHIBIT 8: Tokenized RWA split by blockchain network

Tokenized RWA - Blockchain network split (%)

![](images/f0ffe77a1315c7613d99aa15ea98bb2d70c4c4daf7efdc42643fc4d8a7ca5481.jpg)  
Source: RWA.xyz, Bernstein analysis

EXHIBIT 9: Top RWA tokenization platform

<table><tr><td></td><td>Platform</td><td>Asset Class</td><td>Tokenized Assets ($Bn)</td></tr><tr><td>1</td><td>Figure</td><td>Private Credit</td><td>19.9</td></tr><tr><td>2</td><td>Securitize</td><td>Treasury, stocks</td><td>5.1</td></tr><tr><td>3</td><td>Ondo</td><td>Treasury, stocks</td><td>3.6</td></tr><tr><td>4</td><td>Circle</td><td>Treasury</td><td>3.1</td></tr><tr><td>5</td><td>Tether</td><td>Commodities</td><td>2.5</td></tr><tr><td>6</td><td>Franklin Templeton</td><td>Treasury</td><td>2.5</td></tr><tr><td>7</td><td>Spiko</td><td>Private Credit</td><td>2.1</td></tr><tr><td>8</td><td>Paxos</td><td>Commodities</td><td>1.8</td></tr><tr><td>9</td><td>Centrifuge</td><td>Treasury, credit</td><td>1.6</td></tr><tr><td>10</td><td>Maple</td><td>Credit, Treasuries</td><td>1.4</td></tr></table>

Source: RWA.xyz, Bernstein analysis

EXHIBIT 10: Tokenized real world asset holders  
RWA Asset Holders (in '000)  
![](images/0eee9b31bd69ebf8cf6043808b025e552676e488d831251db9ad925110ea5297.jpg)  
Current as of July 11, 2026  
Source: RWA.xyz, Bernstein analysis  
137% YoY growth, 47% QoQ growth

EXHIBIT 11: FIGR - Consumer Loan Volumes (\$Bn)

![](images/d4f8d61a7cc4bdbced49e94b97caf0dd97b712cee410efc29b53e795de25ca01.jpg)  
Source: Company filings, Bernstein analysis

EXHIBIT 12: Tokenized Equities - Monthly Transfer Volumes  
Tokenized Equity - Transfer Volumes (\$Bn)  
![](images/3a34934f7796daa1f2053da27a68305577ecb4af9e455281a953e03d23091bd1.jpg)  
Source: RWA.xyz, Bernstein analysis

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">10 Jul 2026</td><td rowspan="2">TTMRel.Perf.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>ClosingPrice</td><td>PriceTarget</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>FIGR (Figure)</td><td>O</td><td>USD</td><td>31.80</td><td>67.00</td><td>NA</td><td>USD</td><td>0.54</td><td>0.98</td><td>1.52</td><td>58.9</td><td>32.4</td><td>20.9</td></tr><tr><td>BLSH (Bullish)</td><td>M</td><td>USD</td><td>24.23</td><td>50.00</td><td>NA</td><td>USD</td><td>0.09</td><td>0.07</td><td>0.14</td><td>280.2</td><td>333.4</td><td>173.1</td></tr><tr><td>COIN (Coinbase )</td><td>O</td><td>USD</td><td>159.07</td><td>330.00</td><td>(79.5)%</td><td>USD</td><td>4.85</td><td>5.97</td><td>13.20</td><td>32.8</td><td>26.6</td><td>12.0</td></tr><tr><td>HOOD (Robinhood)</td><td>O</td><td>USD</td><td>111.97</td><td>130.00</td><td>(6.8)%</td><td>USD</td><td>2.12</td><td>2.65</td><td>3.70</td><td>52.8</td><td>42.3</td><td>30.2</td></tr><tr><td>SBET (Sharplink)</td><td>O</td><td>USD</td><td>5.51</td><td>24.00</td><td>(95.2)%</td><td>USD</td><td>(7.37)</td><td>1.73</td><td>(4.59)</td><td>(0.7)</td><td>3.2</td><td>(1.2)</td></tr><tr><td>SPX</td><td></td><td></td><td>7,575.39</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
BLSH estimate is Adjusted EPS; BLSH valuation is Adjusted P/E (x); BLSH base year is 2024;

Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Figure Technology Solutions

We value FIGR on 25x EV/27E EBITDA, at a premium to traditional exchanges and crypto peers, led by FIGR's structural growth prospects as pure-play tokenization platform and profitable core lending business. We rate Figure Outperform (PT\$67).

## Bullish

We value BLSH using 34x EV/Adjusted EBITDA'27E, at a premium on COIN and HOOD, considering the early stage of business and wide array of growth opportunities ahead. We rate BLSH Market-Perform with PT \$50.

## Coinbase Global Inc.

We value COIN using a 25x Price/2027E Earnings, in-line with the average of similar crypto/fintech/broker peers, to arrive at our price target of \$330.

## Robinhood Markets Inc

Robinhood is scaling up rapidly and is a cyclical business. As a consequence, we value HOOD using a \~35x Price/2027E Earnings to arrive at our price target of \$130.

## Sharplink Gaming

We value SBET using a 10-year ETH treasury holding model based on our ETH forecasts and SBET's ETH growth strategy. We discount back the estimated 2035E SBET price to arrive at 2026E SBET equity, implying a long-term 15% premium to SBET's 2026E ETH treasury NAV. We rate SBET Outperform (PT\$24).

## RISKS

## Figure Technology Solutions

1. FIGR's business model involve some macro risks, for example, aggressive interest rate decline makes mortgage refinancing more competitive, impacting the demand for HELOCs.

2. FIGR's business model is dependent on continued growth of private credit, any risks emerging leading to a slowdown in private credit could impact uptake for tokenized credit on Figure's marketplace.

3. We expect non-HELOC loans to contribute \~20% of FIGR's total loan volumes by 2027E, any delay in expansion into new loan categories can affect Figure's loan growth.

## Bullish

Upside Risks to our price target include:

1. Early roll-out of BLSH's U.S and crypto derivatives business can front load the growth in their trading volumes vs our estimates. We expect Bullish to launch U.S spot trading in 2026E and roll out options trading (ex-US) in 2026E.

2. Rapid scaling of Bullish's subscription services (new multi-year liquidity services contract, increased index adoption etc.) can further grow the subscription revenue lines.

Downside risks to our price target include:

1. Risk of fresh competition from U.S based and international exchanges (e.g Coinbase, Binance) and brokers (e.g Robinhood, Schwab) causing pricing & market share pressure in the U.S as well as international markets.

2. We expect \~15% of Bullish's transaction revenues from U.S by 2027E, any delay in receiving the U.S NY DFS license, delaying the US spot or derivatives launch could affect U.S revenues.

3. Digital Assets are a new asset class with limited price history and often display high-beta volatility to changes in macro including any recessionary challenges in U.S.

## Coinbase Global Inc.

1. Risk of fresh competition from international exchanges (e.g., Binance) and brokers (e.g., Robinhood, Schwab) causing pricing & market share pressure in the US home market.

2. Any delay in passing key regulation to establish the Digital assets regulatory framework in the U.S including risk of regulatory volatility from political changes (e.g., mid-term US elections).

3. Digital Assets are a new asset class with limited price history and often display high-beta volatility to changes in macro including any recessionary challenges in the US.

## Robinhood Markets Inc

Robinhood faces regulatory risks on its revenue model, particularly its PFOF model from SEC and other regulatory bodies. This also applies to the crypto trading business.

SEC has historically been harsh on crypto trading businesses, with focus on token trading platforms, as some tokens maybe considered securities.

Digital assets are a new asset class, with limited price history i.e Bitcoin itself is less than 14 years old. The remaining digital assets industry reflected by smart contracts and other blockchain applications is even younger and still evolving into its utility phase.

## Sharplink Gaming

1. Digital Asset treasury management involves significant balance sheet and liquidity risk, if companies deploy short term callable debt.

If Ethereum price is weak especially during maturity of debt, they will have to sell its ETH holdings to repay debt or refinance its debt at unfavourable terms.

2. SBET and other ETH Digital asset treasury companies deploy ETH in staking strategies. Native staking might pose some custody and liquidity issues due to long unstaking queues.

3. SBET might use decentralised finance and other applications to offer higher than market staking yield on ETH. DeFi yield strategies involve smart contract risk and may add to volatility in ETH rewards.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price

Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Pric

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
