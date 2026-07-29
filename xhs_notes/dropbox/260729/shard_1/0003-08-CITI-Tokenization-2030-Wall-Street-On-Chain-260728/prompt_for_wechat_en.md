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
## Tokenization 2030 Wall Street On-Chain

## Authors

![](images/2c41a69b71395725e59b0b99bc6de027e35390411d830c30e5aac6a8007a689c.jpg)

Ronit Ghose
Global Head, Future of Finance, Citi Institute
ronit.ghose@citi.com

![](images/0ee0a94c368389dabb156e258af817adcf0ee5139d6685b58bf5e82213ca818a.jpg)

Kaiwan Master
Future of Finance,
Citi Institute
kaiwan.hoshang.master@citi.com

![](images/7232cc142bcf5d22212918ea85564a334555a038fa65698f29867e8ed4b96b36.jpg)

Sophia Bantanidis
Future of Finance,
Citi Institute
sophia.bantanidis@citi.com

![](images/85585a49dbd6a9f7a6eab41345b1f7b77c32acf4f8765e33c42e7930bb2d9d2e.jpg)  
Ronak Shah
Future of Finance,
Citi Institute
ronak.sharad.shah@citi.com

![](images/9ec42b30f4eecbc7ed657970d1fa94a53da3d65ab0323c347b2ab79625e85112.jpg)

Prag Sharma
Future of Finance,
Citi Institute
prag.sharma@citi.com

![](images/add72a3d4f25d0ac747ddf7aebe47dd0375ee6c113f1941ee0f5bd85407e14ce.jpg)

Savina Chahal
Citi Institute
savina.chahal@citi.com

## Contributors

Peter Bain
Blockstream

Artem Korenyuk
Citi Client Business
Development

Chris Rayner-Cook
Brevan Howard Digital

Adi Ben-Ari
Applied Blockchain

Joseph Lubin
Ethereum/Consensys

Rob de Rozario
Alphaparty Capital

Matthew Blumenfeld
PwC

Blue Macellari
T. Rowe Price

Ryan Rugg
Citi Services

Jeff Boortz
Blockstream

Nate Marquiss
Blockstream

Gabriel Sadoun
Blockstream

Giang Bui
Securitize

Ryan Marsh
Citi Services

Suzy Singh
Securitize

Craig Chatfield
Citi Services

Alex Miller
Citi Institute

Germán Soto Sanchez
BroadRidge

David Cunningham
Consensys

Andrew Mulley
Citi Services

Solomon Tesfaye
Aptos Labs

Pablo Greco
Blockstream

Trevor Pritchard
Alphaparty Capital

Nadine Teychenne
Citi Services

Alexander Ivanov
Citi Investment Banking

Sebastian Pulido
Aave Labs

Ajit Tripathi
Asango Limited

Justin Karol
Citi Services

Lory Kehoe
Aave Labs

Deborah Querub
Citi Wealth

Ebba Wexler
Citi Investment Banking

![](images/d30e334071f1fd87e018655e4c95878ba9c19fadc793e07801b2b8e9106d4186.jpg)

## Contents

Summary and Key Takeaways 6   
Uneven Progress, But an Undeniable Shift 8   
Evolution, Not Revolution. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
Towards Operational Reality. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Why Do We Need Tokenization? 16 How Big is the Market? 19 Why Tokenization Lagged 24 Are Private Markets a Natural Fit for Tokenization? 26   
Implications for Capital Markets 28   
Reshaping Capital Market Structure. 29 Who Controls the Ecosystem? 34 Different Clients, Different Adoption Paths 38 Emergence of New Market Participants 40 Need for Incumbents to Evolve and Adapt 41 Infrastructure Design Choices 42 Risks Associated with Tokenization. 44   
Next Frontier: On-Chain Finance 46   
Crypto-Native DeFi to Institutional Adoption 47   
Appendix 50   
Global Standard Setters Perspectives on Tokenization 50 Tokenization Standards and Interoperability 51

## Tokenization 2030

Wall Street On-Chain

The tokenization of financial assets – the representation of securities as digital tokens on blockchain infrastructure – is moving from pilot stage toward operational deployment. After years of slow progress held back by regulatory uncertainty, fragmented infrastructure and the absence of on-chain settlement money, adoption is now accelerating.

The current global tokenized asset market stands at approximately \$17 billion. Citi Institute projects this to reach \$5.5 trillion by 2030 in a base case scenario, with a bear case of \$2.7 trillion and a bull case of \$8.2 trillion.

Estimating tokenization market size by 2030 (\$ trillion)

![](images/69d92f4308b2f26861c70164aabf498a143a3e9410675ae7ab3fbcda15700509.jpg)

Growth is expected to be led by public market securities – particularly U.S. equities and treasuries – rather than private markets, where adoption remains early-stage and structurally constrained.

Three forces underpin this shift. First, major financial market infrastructure providers, including the Depository Trust & Clearing Corporation (DTCC), New York Stock Exchange (NYSE), and Nasdaq, are integrating tokenization into core issuance, trading and settlement workflows, moving well beyond experimentation. Second, the growth of regulated on-chain money, including stablecoins (projected at \$1.9 trillion by 2030) and tokenized deposits, is providing the settlement foundation that earlier tokenization efforts lacked. Third, regulatory clarity is improving across key jurisdictions, with the U.S. Clarity Act continuing to move toward a full Senate vote.

The transition will be gradual. Hybrid models – where tokenized and legacy systems operate in parallel – are expected to dominate in the near term. This is likely to introduce operational complexity before efficiency gains are fully realised. Interoperability across platforms, standards and settlement assets remains a prerequisite for scale.

This report identifies a reconfiguration across capital markets, with the emergence of institutions that control both asset issuance and settlement rails – termed “Structural Orchestrators”. Traditional post-trade intermediaries face structural pressure as settlement becomes faster and more automated. New market participants are also emerging across issuance, trading, custody, and identity layers.

The path forward for tokenization may depend less on technological capability and more on regulatory alignment, liquidity coordination and the ability to manage hybrid complexity.

![](images/954736177d377f72ffc7040d62481560633d1098845a3b0f77db9f1648389029.jpg)

## Key Takeaways

Growth predictions: We forecast a \$5.5 trillion base case for tokenized assets by 2030, rising to \$8 trillion in a bull case. $^{1}$ Public market securities and liquid collateral, particularly U.S. equities and treasuries, are likely to drive early adoption and expand distribution to digitally native investors.

Liquid assets on-chain: Modern, digitally native investors increasingly expect 24x7 access to financial assets. Equities, bonds and commodities could move on-chain as younger retail investors drive adoption. If 10% of U.S. retail investors use on-chain solutions by 2030, this could create about \$2.6 trillion of demand for tokenized public equities. $^{2}$

Institutional catalysts: Major market infrastructure providers, including DTCC, NYSE, and Nasdaq, are beginning to integrate tokenization into their core platforms. As pilot programs transition into production, supported by evolving regulation, adoption among traditional financial institutions could accelerate from 2026 onwards.

![](images/16cc49a7fcfd15260600483e1e06b912476447687f4cbcaa960f6585115f418c.jpg)

Digital money is the foundational enabler: Tokenization of financial assets is the companion to tokenized cash. Regulated stablecoins and tokenized deposits can help engender trust in on-chain settlement for Delivery-versus-Payment (DvP), improving capital efficiency and reducing settlement risk.

“Structural orchestrators” emerge: Tokenization could create new revenue pools through programmability, composability and vertically integrated business models. Institutions may look to control issuance, distribution and settlement rails (e.g., select banks, asset managers, stablecoin issuers) in order to capture value.

![](images/296902c7933139d736ac9ef3bf20bfffeee13e425c35543c337b79cf31b5956b.jpg)

Evolution, not revolution – hybrid models set to dominate: The transition will be gradual. We expect a “messy” period where tokenized and legacy systems operate side by side. Hybrid models and interoperability between on-chain and off-chain worlds are critical to scaling.

## 1.5/10

Tokenized financial assets on the adoption curve, measured on a scale of 0 to 10.

## \$5.5 trillion

Projected tokenized asset market size by 2030 (base case), driven primarily by public market securities and liquid collateral.

Source: Citi Institute

## \$1.9 trillion

Projected stablecoin market size (base case), enabling on-chain settlement and instant, programmable transfers.

Source: Base case Citi Institute estimate from report ‘Stablecoins 2030 – Web3 to Wall Street’ published in September 2025

![](images/9e2219c8b590d3909ddfcb968c6f189b0955aa0681837eb1f4e7a97d7df1ef21.jpg)

## Uneven Progress, But an Undeniable Shift

Tokenization of securities is part of a broader shift toward programmable assets, digitally native settlement, and more always-on finance.

The convergence of tokenized assets with on-chain money underpins the future of finance: on chain finance, where settlement, collateral management and liquidity flows operate in real time and across borders based on ‘atomic settlement’. $^{3}$

Institutional participation is now moving beyond experimentation with tokenization being used in issuance, trading, and post-trade workflows. Regulatory clarity is improving across major jurisdictions, providing some legal certainty for institutional adoption.

A key catalyst is the emergence of digitally native money which enables on-chain settlement. This has been a key constraint of earlier tokenization efforts. Digital asset market infrastructure is also evolving, with advances in custody, compliance, and interoperability.

## Evolution, Not Revolution

Importantly, we think this transformation will not arrive as a single disruptive change. We do not expect a sudden flip from traditional markets to fully tokenized ones.

Adoption remains early and uneven across asset classes and jurisdictions, constrained by interoperability challenges, legal frameworks, liquidity coordination, investor behavior and market conventions.

As with previous infrastructure shifts, the benefits of tokenization are likely to accrue gradually rather than immediately.

Institutions will seek to integrate issuance, trading and settlement at scale within regulated frameworks and existing client relationships, since control of these layers can drive a larger share of the transaction lifecycle.

The value of scaling depends on interoperability, common standards, regulatory alignment, trusted digital identity frameworks and coordination across a complex ecosystem, which will take time. Specialist native on-chain firms will also look to gain market share as on-chain transactions increase in size and scope.

![](images/09eb2d83f66dada5d8b33899f90a149f07a5d67eede552a68185ffa2dbdf7d60.jpg)

The tokenization of financial assets is more than just technology; it is unlocking Wall Street for the digitally-native generation.

Artem Korenyuk, Head of Enterprise
Digital Assets, Citi Client Business Development

![](images/fb324e0901697cf3572fadd975b8235c575ec492d3dc2542d3583a850a139d61.jpg)

## “

The transition to tokenized markets is best understood through the E-ZPass $^{4}$ tollbooth analogy.

We didn't move to full automation overnight. Parallel systems run first, the road got wider with lanes for automated and legacy flows, adding cost and complexity before convergence. The key question is how quickly can we reach the automated end state?

Blue Macellari, Head of Digital Assets Strategy, T. Rowe Price

![](images/f8cbc805202c2d0b27cd616d18b8d74edc5da15162c80e54ea3751c2becd7ffe.jpg)

## Towards Operational Reality

Tokenization is not new. We first outlined its potential in Citi GPS: Money, Tokens, and Games: Blockchain's Next Billion Users and Trillions in Value (2023), noting it could unlock trillions in value by enabling more efficient and programmable financial markets.

Many early industry forecasts on the growth of tokenization markets, including some of the more bullish ones with target market size in the tens of trillions of dollars, have proven too aggressive.

Previous tokenization waves struggled to scale meaningfully due to a variety of factors. Regulatory uncertainty constrained implementation and enforceability, secondary market liquidity was limited, infrastructure was fragmented, and critically, there was no regulated on-chain cash.

These constraints are now beginning to ease. Several independent catalysts are now aligning to move tokenization from experimentation towards broader adoption.

## What is Tokenization?

Tokenization refers to the digital representation of ownership, rights, or claims on assets as tokens recorded on a blockchain or distributed ledger. Tokenization can involve either the on-chain representation of an existing asset or the native issuance of a new asset directly on distributed ledger infrastructure.

These tokens are pieces of code that embed information about an asset's attributes, ownership, transaction history, and rules governing its transfer. Unlike traditional records, tokenized assets enable direct, peer-to-peer transfer of value with near real-time settlement and a single, shared source of truth.

Tokenization can apply across a wide spectrum of assets. This includes financial assets such as equities, bonds, investment funds, and deposits, as well as real-world and less liquid assets such as real estate, private credit, infrastructure, and even intellectual property or carbon credits.

Beyond digitization, tokenization introduces programmability. Rules and logic can be embedded directly into the asset via smart contracts, enabling automated actions such as coupon payments, compliance checks, collateral management, and corporate actions.

## 1. Rising institutional participation

Asset managers have been launching tokenized funds for several years. Now systemic financial market infrastructure firms are launching tokenization offerings.

\- Depository Trust & Clearing Corporation (DTCC) received regulatory clearance in late 2025 to offer a tokenization service for DTCC-custodied assets, with a three-year pilot planned for late 2026. The scope includes highly liquid instruments such as Stocks, ETFs and U.S. Treasuries, enabling tokenized representation while preserving existing legal ownership and investor protections. $^{5,6}$

\- New York Stock Exchange (NYSE) announced plans for a tokenized securities platform by late 2026, subject to regulatory approval. This would enable 24x7 trading of U.S.-listed equities and ETFs with near-instant settlement and stablecoin-based funding, potentially operating alongside or outside traditional clearing infrastructure. $^{7}$

\- Nasdaq has received SEC approval to enable certain stocks and ETFs to be issued, traded and settled in tokenized form, embedding tokenization within existing market structure with securities continuing to leverage established post-trade infrastructure. $^{8}$

![](images/eec1829f7ea5b8a7e225d5e89215df9eded5817e685e2a07510bad2a23a959d9.jpg)

You're seeing the full weight of American financial power and the global reserve currency moving on-chain at scale. When DTCC and the NYSE embed tokenization into capital markets, this marks a tipping point.

David Cunningham, Global Head of Institutional Business, Consensys

![](images/5d2af2ed1f5da1e2ee080d14bdfa17952fbae9a809e7329a1711edc34919f0ea.jpg)

Why is this significant? These organizations are not crypto-native firms pushing blockchain, but some of the oldest and largest financial institutions adopting new infrastructure. These examples represent only part of a broader set of uses emerging across markets.

Rather than build parallel, crypto native systems, incumbents such as DTCC and NYSE are integrating tokenization into core issuance, trading and settlement rails.

This approach prioritizes legal certainty, investor protection and institutional adoption over speed of disruption, positioning existing market rails as a bridge to digitally native, on-chain financial systems.

## 2. On-chain money enabling native settlement

Earlier tokenization implementations had to rely on fiat rails for settlement, limiting efficiency gains and introducing operational friction. This is now changing with stablecoins gaining broader acceptance and increasingly being integrated info financial flows.

As highlighted in Citi GPS: Stablecoins 2030 – Web3 to Wall Street (2025), we forecast stablecoin issuance value could be \$1.9 trillion by 2030. Major banks are also developing tokenized deposit infrastructure, which could be even larger in size.

The coexistence of stablecoins and tokenized deposits enables seamless settlement and provides the liquidity foundation required for tokenized securities to scale, enabling atomic Delivery-versus-Payment (DvP) and supporting continuous market operations.

We expect on-chain money in the United States to be a mix of stablecoins and tokenized deposits. In other geographies, including Europe, India and Mainland China, we believe CBDCs and tokenized deposits will be the digital money policy focus, not stablecoins.

## 3. Increasing regulatory clarity

A gradual shift toward clearer and more coordinated regulatory frameworks is strengthening the legal foundation for institutional adoption. However, this progress is uneven and increasingly highlights a double-edged dynamic.

While greater clarity supports scalability and market confidence, the emergence of divergent regional rules risks fragmenting markets, increasing compliance costs, and diluting some of the efficiency gains that tokenization promises.

Figure 1. Regulatory developments across key jurisdictions  
![](images/2d5d90de9dd534377acabdcc2d9f69e270ea44af6e94126df64459dba3e4db7a.jpg)

Europe: The Markets in Crypto-Assets (MiCA) Regulation has introduced a harmonized, EU-wide framework for crypto assets.

For tokenized securities, existing capital market rules and the EU's DLT Pilot Regime further support testing of issuance, trading and settlement models.

Recent developments from trade bodies suggest that while the EU DLT pilot regime represents an important step towards regulatory clarity, its limited scope and design are limiting its effectiveness for scaling tokenized capital markets. $^{9}$

U.S.: Securities and Exchange Commission (SEC) has provided clarity on the application of federal securities law to tokenized securities in January 2026, reaffirming technology neutrality, i.e., digital wrapper on an asset does not change its regulatory treatment. $^{10,11}$ This clarity enables institutions to treat tokenization as a market infrastructure question rather than a regulatory experiment.

Proposed market structure reforms also aim to establish a clearer framework for digital assets, distinguishing commodities and securities, clarifying SEC and Commodity Futures Trading Commission (CFTC) oversight.

![](images/891c01d16385fe9bcaa22844e404c15dd2cc49e2a4cb3eff6833

[中间内容因长度限制已省略]

flect the views of their employer or any affiliated entity or the other authors, may differ from the views of other personnel at such entities, and may change without notice. You should assume the following: The Firm may be the issuer of, or may trade as principal in, the financial instruments referred to in this communication or other related financial instruments. The author of this communication may have discussed the information contained herein with others within the Firm and the author and such other Firm personnel may have already acted on the basis of this information (including by trading for the Firm's proprietary accounts or communicating the information contained herein to other customers of the Firm). The Firm performs or seeks to perform investment banking and other services for the issuer of any such financial instruments. The Firm, the Firm's personnel (including those with whom the author may have consulted in the preparation of this communication), and other customers of the Firm may be long or short the financial instruments referred to herein, may have acquired such positions at prices and market conditions that are no longer available, and may have interests different or adverse to your interests. This communication is provided for information and discussion purposes only. It does not constitute an offer or solicitation to purchase or sell any financial instruments. The information contained in this communication is based on generally available information and, although obtained from sources believed by the Firm to be reliable, its accuracy and completeness is not guaranteed. Certain personnel or business areas of the Firm may have access to or have acquired material non-public information that may have an impact (positive or negative) on the information contained herein, but that is not available to or known by the author of this communication. The Firm shall have no liability to the user or to third parties, for the quality, accuracy, timeliness, continued availability or completeness of the data nor for any special, direct, indirect, incidental or consequential loss or damage which may be sustained because of the use of the information in this communication or otherwise arising in connection with this communication, provided that this exclusion of liability shall not exclude or limit any liability under any law or regulation applicable to the Firm that may not be excluded or restricted. The provision of information is not based on your individual circumstances and should not be relied upon as an assessment of suitability for you of a particular product or transaction. Even if we possess information as to your objectives in relation to any transaction, series of transactions or trading strategy, this will not be deemed sufficient for any assessment of suitability for you of any transaction, series of transactions or trading strategy. The Firm is not acting as your advisor, fiduciary or agent and is not managing your account. The information herein does not constitute investment advice and the Firm makes no recommendation as to the suitability of any of the products or transactions mentioned. Any trading or investment decisions you take are in reliance on your own analysis and judgment and/or that of your advisors and not in reliance on us. Therefore, prior to entering into any transaction, you should determine, without reliance on the Firm, the economic risks or merits, as well as the legal, tax and accounting characteristics and consequences of the transaction and that you are able to assume these risks. Financial instruments denominated in a foreign currency are subject to exchange rate fluctuations, which may have an adverse effect on the price or value of an investment in such products. Investments in financial instruments carry significant risk, including the possible loss of the principal amount invested. Investors should obtain advice from their own tax, financial, legal and other advisors, and only make investment decisions on the basis of the investor's own objectives, experience and resources. This communication is not intended to forecast or predict future events. Past performance is not a guarantee or indication of future results. Any prices provided herein (other than those that are identified as being historical) are indicative only and do not represent firm quotes as to either price or size. You should contact your local representative directly if you are interested in buying or selling any financial instrument, or pursuing any trading strategy, mentioned herein. No liability is accepted by the Firm for any loss (whether direct, indirect or consequential) that may arise from any use of the information contained herein or derived herefrom. Although the Firm is affiliated with Citibank, N.A. (together with its subsidiaries and branches worldwide, "Citibank"), you should be aware that none of the other financial instruments mentioned in this communication (unless expressly stated otherwise) are (i) insured by the Federal Deposit Insurance Corporation or any other governmental authority, or (ii) deposits or other obligations of, or guaranteed by, Citibank or any other insured depository institution. This communication contains data compilations, writings and information that are proprietary to the Firm and protected under copyright and other intellectual property laws, and may not be redistributed or otherwise transmitted by you to any other person for any purpose. © 2026 Citi Global Markets Inc. Member SIPC. All rights reserved. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. or its affiliates and are used and registered throughout the world.
"""
