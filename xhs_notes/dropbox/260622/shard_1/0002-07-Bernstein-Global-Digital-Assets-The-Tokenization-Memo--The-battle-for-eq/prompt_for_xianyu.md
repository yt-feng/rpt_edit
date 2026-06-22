你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
## Global Digital Assets

Gautam Chhugani +91 226 842 1416 gautam.chhugani@bernsteinsg.com

Mahika Sapra +91 226 842 1408 mahika.sapra@bernsteinsg.com

Sanskar Chindalia +91 226 842 1445 sanskar.chindalia@bernsteinsg.com

Harsh Misra +91 226 842 1457 harsh.misra@bernsteinsg.com

## The Tokenization Memo: The battle for equity tokenization (2/n)

Multiple business models are being attempted for equity/real-world asset tokenization, while the industry still awaits regulatory clarity for securities tokenization including potential expectation of an ‘innovation exemption’. Meanwhile, industry players are laying out their early ‘chess moves’ with early product launches, acquisitions and strategic partnerships.

Tokenized RWA Industry Metrics - Market cap of tokenized real-world assets has crossed \$51Bn (up 40% YTD), demonstrating strong resilience vs broader crypto markets that are down \~20% YTD (Exhibit 1). Private credit remains the dominant asset class at \~47% of total RWA market cap, followed by U.S. Treasuries at \~30% and commodities at \~9% (Exhibit 2). Ethereum and Provenance continue to host the bulk of onchain RWA activity, representing over 70% of total tokenized assets (Exhibit 3). Total RWA asset holders have crossed 900K, up \~60% YTD (Exhibit 5).

Equity tokenization continues to attract mainstream interest with tokenized equities growing 130% YTD from \$0.7Bn to \$1.6Bn. The current offerings leverage existing regulatory structure to offer tokenized equities (largely restricted for US investors). However, recent SEC actions have been encouraging for the industry. Recently, SEC proposed rescinding rule 611 and 610 (e) that would allow tokenized stocks to trade more freely on decentralized venues without mandatory trade through compliance with traditional exchanges. In Dec'25, SEC issued a no action letter to DTC (not covered) for a tokenized equity pilot and approved NYSE's and NASDAQ's proposal to permit trading of tokenized securities on the exchanges. The industry still awaits regulatory clarity for securities tokenization including potential expectation of an 'innovation exemption' that could allow trading of tokenized US stocks onshore.

We are seeing the tokenization industry broadly evolving across two business models - neutral infrastructure positioning (enabling tokenization for traditional financial market participants like exchanges, asset managers, loan originators) and trading model (using tokenization to offer multi-asset class exposure on a single trading venue).

\- Tokenized Securities - Trading Infrastructure: In the current model, regulated broker-dealer platforms offer trading services in tokenized stocks, allowing global investors to access bluechip regional equities (like Robinhood offering tokenized US stocks to EU investors). The third party sponsor buys underlying shares, custodies them in a secured account and issues a blockchain token against them. The tokens can be traded on blockchain 24x7 with real time settlement, allowing platforms to earn incremental trading commission. However, these trading tokens operate only on blockchain rails with no reconciliation with the actual shareholder registry. The third-party sponsor (and not the tokenizer) is the registered owner of the underlying shares. Hence, tokenholders are not entitled to rights associated with ownership of the shares, such as dividend, voting, etc.

\- Tokenized Securities - Settlement and Exchange Infrastructure: The issuer-sponsored tokenization model uses blockchain as the settlement layer for actual company issued shares. Shareholders benefit from faster and capital efficient settlement cycles, while receiving full ownership and protection rights of traditional exchange listed shares. Players like Figure, Bullish and Securitize (not covered) are building regulated infrastructure layer for tokenized equities (compliant with existing SEC rules) using SEC-registered transfer agents, regulated ATS (Alternative Trading System), broker-dealers and custody solutions. Figure has already launched its own tokenized shares on OPEN, with another listing in the pipeline. Bullish's Equiniti acquisition allows it to operate a unified ledger for traditional and tokenized securities, while offering services related to token design and liquidity. Securitize has partnered with NYSE (not covered) for NYSE's tokenized securities platform, Computershare (not covered) to enable tokenized shares for US issuers and Jump Trading (not covered) to launch DEX-style onchain trading of tokenized equities.

\- Multi-asset single exchange: Coinbase is exploring tokenized equities including use of perpetual futures product structure to offer exposure to real-world assets. Over the past few weeks, Coinbase has launched tokenized equities, equity perpetuals, pre-IPO perpetuals for non-US investors, and regulated crypto derivatives market for US investors. Coinbase's tokenized stocks (backed 1:1 by underlying shares) enable non-US investors to access US equities and ETFs, with features like automatic dividend payout and programmatic utility of the onchain economy. Further, Coinbase's global perpetual futures offering now spans across equities (including pre-IPO), ETFs and crypto, strengthening its ‘everything exchange’ proposition. In March, Coinbase launched 24x7 USDC settled equity (stock and ETF) perpetual markets for both retail and institutional investors outside the US, followed by pre-IPO perpetuals. Global crypto derivative market so far was restricted for US investors with institutions setting up offshore entities to access the liquid crypto futures market. Coinbase has now become the only CFTC-regulated FCM offering US investors access to global crypto derivatives (futures and options).

## RWA TOKENIZATION DASHBOARD

EXHIBIT 1: Tokenized RWA - Market Cap (\$Bn)  
Tokenized RWA - Market Cap (\$Bn)  
![](images/056f987b4eac0bf2bf4655f91fedbde82f6fe714ab1ee28cbffa5127158ab1a4.jpg)  
Private credit includes Figure tokenized credit
Source: RWA.xyz, Bernstein analysis

EXHIBIT 2: Tokenized RWA market cap split by asset class  
![](images/6ec16102066a9850516d28e65d552c225baf5603271ba33e452daed9a210f4f0.jpg)  
Private credit includes Figure tokenized credit
Source: RWA.xyz, Bernstein analysis

## EXHIBIT 3: Tokenized RWA split by blockchain network

Tokenized RWA - Blockchain network split (%)

![](images/c440ed0fb4687d4b76168cc4bac6c164811d206ab3f6a00f345248abc4f658b6.jpg)  
Source: RWA.xyz, Bernstein analysis

EXHIBIT 4: Top RWA tokenization platforms

<table><tr><td></td><td>Platform</td><td>Asset Class</td><td>Tokenized Assets ($Bn)</td></tr><tr><td>1</td><td>Figure</td><td>Private Credit</td><td>18.9</td></tr><tr><td>2</td><td>Securitize</td><td>Treasury, stocks</td><td>4.3</td></tr><tr><td>3</td><td>Ondo</td><td>Treasury, stocks</td><td>3.8</td></tr><tr><td>4</td><td>Circle</td><td>Treasury</td><td>3.0</td></tr><tr><td>5</td><td>Tether</td><td>Commodities</td><td>2.5</td></tr><tr><td>6</td><td>Franklin Templeton</td><td>Treasury</td><td>2.5</td></tr><tr><td>7</td><td>Paxos</td><td>Commodities</td><td>1.9</td></tr><tr><td>8</td><td>Spiko</td><td>Private Credit</td><td>1.8</td></tr><tr><td>9</td><td>Centrifuge</td><td>Treasury, credit</td><td>1.6</td></tr><tr><td>10</td><td>Maple</td><td>Credit, Treasuries</td><td>1.4</td></tr></table>

Source: RWA.xyz, Bernstein analysis

EXHIBIT 5: Tokenized real world asset holders  
RWA Asset Holders (in '000)  
![](images/e33e28abd30882f9f567f6f11d7aee7fa295e5e40a76ffe64b69f1f1f9caab08.jpg)  
Source: RWA.xyz, Bernstein analysis

EXHIBIT 6: FIGR - Consumer Loan Volumes (\$Bn)  
FIGR - Consumer Loan Volumes (\$Bn)  
![](images/0d1ca5fa60d810a71f0d0657b7a01bf4eb419ce5c946fd57e48345be0787b647.jpg)  
Q2'26 actual loan volumes as of May, 2026; June'26 runrate based on Provenance Pulse Source: Company filings, Bernstein analysis

EXHIBIT 7: Tokenized Equities - Monthly Transfer Volumes  
Tokenized Equity - Transfer Volumes (\$Bn)  
![](images/ab2fc2d803c8b570170c84544570bc1c4dd4ae447c51c0fc856823114254bfc1.jpg)  
June'26 numbers based on runrate as of June 19, 2026
Source: RWA.xyz, Bernstein analysis

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">18 Jun 2026</td><td>TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>FIGR (Figure)</td><td>O</td><td>USD</td><td>28.55</td><td>67.00</td><td>NA</td><td>USD</td><td>0.54</td><td>0.98</td><td>1.52</td><td>52.9</td><td>29.1</td><td>18.7</td></tr><tr><td>BLSH (Bullish)</td><td>M</td><td>USD</td><td>24.10</td><td>50.00</td><td>NA</td><td>USD</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COIN (Coinbase )</td><td>O</td><td>USD</td><td>163.26</td><td>330.00</td><td>(70.4)%</td><td>USD</td><td>4.85</td><td>5.97</td><td>13.20</td><td>33.7</td><td>27.3</td><td>12.4</td></tr><tr><td>HOOD (Robinhood)</td><td>O</td><td>USD</td><td>108.15</td><td>130.00</td><td>12.4%</td><td>USD</td><td>2.12</td><td>2.65</td><td>3.70</td><td>51.0</td><td>40.9</td><td>29.2</td></tr><tr><td>SBET (Sharplink)</td><td>O</td><td>USD</td><td>5.29</td><td>24.00</td><td>(72.8)%</td><td>USD</td><td>(7.37)</td><td>1.73</td><td>(4.59)</td><td>(0.7)</td><td>3.1</td><td>(1.2)</td></tr><tr><td>SPX</td><td></td><td></td><td>7,500.58</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
BLSH estimate is Adjusted EPS; BLSH valuation is Adjusted P/E (x); BLSH base year is 1999;

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

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, v

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
