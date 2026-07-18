你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
# Weekend Tech Byte: Compute capital markets - Hedging the trillion dollar AI capex cycle

Gautam Chhugani +91 226 842 1416 gautam.chhugani@bernsteinsg.com

Madison Rezaei +1 917 344 8622 madison.rezaei@bernsteinsg.com

Mark L. Moerdler, Ph.D. +1 917 344 8506 mark.moerdler@bernsteinsg.com

Richard Nguyen +33 1 42 13 54 22 richard.nguyen@bernsteinsg.com

Peter Weed +1 917 344 8390 peter.weed@bernsteinsg.com

Mark Shmulik +1 917 344 8508 mark.shmulik@bernsteinsg.com

Harshita Rawat, CFA +1 917 344 8485 harshita.rawat@bernsteinsg.com

Stacy A. Rasgon, Ph.D. +1 213 559 5917 stacy.rasgon@bernsteinsg.com

Mark C. Newman +1 212 845 7822 mark.newman@bernsteinsg.com

Nikhil Devnani, CFA +1 917 344 8425 nikhil.devnani@bernsteinsg.com

Laurent Yoon +1 917 344 8502 laurent.yoon@bernsteinsg.com

Mahika Sapra +91 226 842 1408 mahika.sapra@bernsteinsg.com

Sanskar Chindalia +91 226 842 1445 sanskar.chindalia@bernsteinsg.com

Harsh Misra +91 226 842 1457 harsh.misra@bernsteinsg.com

## By Gautam Chhugani & Madison Rezaei

## FINANCIALIZATION OF COMPUTE

Spot compute markets include transactions for immediate access to available GPU capacity, where compute resources are rented at prevailing market prices for near-term workloads and delivery. Compute derivatives, just like other commodity derivatives, allow participants to lock GPU rental prices through forward position in GPU capacity. Buyers can lock their cost of training and inferencing workloads, sellers can forward sell their capacity before it is built, and lenders can hedge the capital they have committed to GPU buildouts. Over the last few months, both CME Group and Intercontinental Exchange announced plans to roll out regulated GPU compute futures, subject to CFTC review. The notable feature is not simply the futures contracts themselves but the broader market structure forming around them. Compute is acquiring, layer by layer, the same architecture every traded commodity market has (Exhibit 1):

\- Exchanges: Exchanges offer a centralized venue to match long and short positions for compute future contracts, building a transparent orderbook for a series of derivative contracts (across maturities, GPU models etc). Offshore exchanges have had a head start in offering derivative contracts on GPU compute prices due to their light-touch regulatory structure, however onshore platforms like Kalshi, ICE and CME (all not covered) are now catching up. Kalshi already offers event

contracts based on GPU prices, while ICE and CME have announced plans to roll out regulated GPU compute futures in late 2026, subject to CFTC review.

\- Indices: Financial markets tend to settle around a few accepted reference prices because everyone wants to transact against the same benchmark. The current compute market is fragmented across different private and public players, without a transparent spot or forward pricing curve. Platforms like Silicon Data (partnered with CME), Ornn (partnered with ICE, Kalshi) and Compute Desk (partnered with Architect) are trying to aggregate data on GPU prices, standardize them for different variations and build benchmarks for GPU pricing.

\- Liquidity and participation: We are seeing constant product launches tailored for various market participants - hyperscalers (compute buyer), neoclouds (compute seller), lenders and arbitrageurs. Initial liquidity on existing products remain nascent and dominated by speculative flows. However, as regulatory structure around compute markets evolve and participants realize the product-market fit for compute markets, liquidity should follow.

We think the closest parallel for compute is power. Electricity was once dismissed as untradeable as it cannot be stored, varies by location and quality - until standardized hubs and reference prices turned forward procurement into a financial market. Compute is following the same sequence, because it shares the same physics - GPU hours cannot be stored, capacity varies by location, chip

generation and tenant. So the forward curve reflects expected scarcity rather than storage cost, and hedging is the only way to carry price risk.

Platforms are now trying to solve the problem of standardizing compute (benchmarks and per GPU hour approach), develop both cash settled and physical delivery rails for forward contracts and build structured financial products on underlying compute. Our view is that benchmarks and distribution are the key factors for growth of compute markets - not different from any commodity financial markets.

EXHIBIT 1: Participants in the compute market  
![](images/f4414f08be71332755c3df6940dcc2eccb87de698cdf4d6f7d6196478fe796a1.jpg)  
Source: Architect, Bernstein analysis

## THE COMMODITY TEST FOR COMPUTE - CLOSEST ASSET CLASS PARALLEL

The closest parallel for compute is the existing market for commodities, particularly electricity.

\- Fungibility & measurable supply - imperfect but workable: Fungibility means that individual units of an item are completely interchangeable. An H100 hour from Ohio (for instance) is not identical to that from Texas, due to different networking, SLA requirements, and deployment environments. Compute markets are broadly following two approaches for fungibility (i) rolling out contracts with standardized terms across chip models, server interfaces, duration etc; and (ii) allowing parties to directly negotiate the grade, timing and location of compute capacity using a basis (price adjustment) on the standard futures price.

\- Storability - Compute is non-storable: An unused GPU-hour disappears forever, with no possibility of warehousing, shipping or holding inventory against future demand. This makes compute resemble electricity where forward markets reflect expected scarcity rather than inventory dynamics.

\- Price volatility - high, hence demand for hedging is real: Volatility is a prerequisite for any derivative market to grow.

GPU chip shortages and hardware generation change (e.g., H100 to B200) cause price volatility in compute markets. On one side sit neoclouds/cloud operators, many owning large fleets of depreciating GPUs. On the other side, we have AI labs and enterprises whose economics depend on future costs of compute, hence there is a presence of both natural buyers and natural sellers in the market.

The market structure for compute markets is still evolving with constant new product announcements and strategic partnerships. The market is still trying to solve for three key questions - (i) Standardizing compute: standardizing the spot and forward pricing curve for compute and building commonly accepted indices; (ii) Product-market fit: building various financial products like futures, perpetuals, event prediction contracts and determining the right fit for different participants; and (iii) Settlement: building infrastructure for both cash and physical settlement of contracts. Industry participants are experimenting with multiple approaches to build a market structure that integrates pricing, product and settlement. We outline a few approaches in the next sections.

## STANDARDIZING COMPUTE - BUILDING BENCHMARKS

Every commodity market begins by answering: what exactly is one unit? Oil solved it decades ago through standardization - a specific grade, quantity and delivery specification. Compute is beginning to solve the same problem but the task of an index provider is similar to an electricity market operator - taking a highly heterogeneous product and building a tradeable reference price for it. The problem is that raw compute prices are not comparable across the market as the same H100 can be priced differently (Exhibit 7) depending on whether rented from neocloud, hyperscaler tiers or public listings. This spread reflects material differences in technical factors (networking) or non technical factors (SLA, support, value add, counterparty quality).

The solution comes from building a benchmark that takes scattered, non-comparable prices from various sources and produces one number the market can transact on. The process can be envisaged in 3 steps:

Step 1 - Data collection and standardization: The index provider needs to define the 'unit', for instance, NVIDIA H100 SXM 80GB (includes server, memory, bandwidth etc.). Further specifications include tier (neocloud/hyperscaler), type of lease (on-demand/committed term) and normalization steps for region and configuration. To ensure that the index moves because of the market and not because of error in sampling, all observations/transactions are normalized to the 'reference unit'. Silicon Data (Exhibit 2) collects a broad set of data -150K daily verified pricing records across 50 regions/countries covering 50-100 platforms across hyperscalers, neoclouds and marketplaces, (link). The data undergoes capture and standardization across pricing structures (lease type/duration), providers and locations and granular hardware specifications and then normalizes prices of heterogeneous physical units to a standard configuration to ensure only comparable price signals are aggregated. Ornn works on transaction based pricing basis ‘negotiated transaction prices’ between data centers and compute buyers tracking rental pricing across GPU models with pricing normalized across hardware configuration, provider, and deployment context.

Step 2 - Benchmark/index: The standardized data becomes a reference index. Silicon Data indices capture prices on every business day, use statistical techniques to filter out stale or non-representative data and undergoes validation procedures to ensure integrity of the index. The need for a benchmark has prompted even legacy financial exchanges such as CME, ICE to partner with Silicon Data and Ornn. CME/Silicon Data and ICE/Ornn partnerships focus on financialization of the compute market and that largest demand will come from investors looking to hedge AI spending rather than physical delivery of GPUs. CME and ICE are leveraging their established positions and existing ecosystem to promote trading activity.

A new exchange focused on AI compute, Architect (private) has multiple partnerships - (i) Ornn for its compute perpetuals whose benchmarks are based on live GPU data from spot markets, which is already live. AX is Architect's offshore (Bermuda-regulated) exchange for perpetual futures across traditional assets and compute; (ii) ComputeDesk (brand of The Compute Index Inc.) for ComputeConnect, and EFP (Exchange for Physical) network that links compute futures on the AI Exchange with actual GPU capacity delivery via Compute Desk's Compute Clear platform.

Step 3 - Forward curves: As compute cannot be stored (electricity analogy), there is no cost of carry to pin forward prices to spot prices and the curve must be derived from market observations. Forward curve is currently published by Silicon Data and Kalshi (Exhibit 6). The shape of the curve is based on expectation of future scarcity rather than a function of inventory. The two main concepts regarding the curve are:

\- Curve in Contango: Upward sloping with future prices above spot prices, means that the market expects scarcity to persist or worsen.

\- Curve in Backwardation: Downward sloping with future prices below spot prices, means the market expects supply wave to come in and hardware depreciation to take a toll, hence, buyers expect to pay less later.

EXHIBIT 2: Data collection methodologies for compute price calculation

<table><tr><td></td><td>Silicon Data</td><td>Ornn</td><td>Kalshi</td></tr><tr><td>Model (Data aggregation)</td><td>Aggregated and Normalized</td><td>Wholesale transaction based</td><td>Prediction Markets</td></tr><tr><td>Methodology</td><td>Gather global data points, use statistical techniques for normalization</td><td>Only cleared/settled transaction data</td><td>Price emerges from event trading contracts - positions forecast future price</td></tr><tr><td>Core product</td><td>SDH100RT index family (per SKU, tier, tenor)</td><td>OCPI reference index</td><td>Market implied forward curve from event contracts</td></tr><tr><td>Partners</td><td>CME - compute futures</td><td>ICE - compute futures + Kalshi contracts + AX* perps</td><td>Ornn (Kalshi contracts settle on Ornn index)</td></tr></table>

\*AX - Architect's offshore AX Exchange;  
Silicon Data, Ornn, Kalshi, Architect, ICE, CME - not covered
Source: Company websites, ICE, CME, Bernstein analysis

## PRODUCTS - FUTURES, PERPETUALS, EVENT CONTRACT

A layered market of financial instruments is now emerging for compute, with different instruments tailored for different use cases. Players like ICE, CME, Architect and Kalshi are developing a series of derivative products on compute prices (Exhibit 3) including index settled futures, physically settled futures, perpetual futures and compute event contracts. These products are still at a nascent stage of adoption as companies are still building the required distribution and settlement infrastructure.

ICE, CME, Architect's American Innovation Exchange (Index settled futures) CME (using Silicon Data), ICE (using Ornn) and Architect (using Compute Desk) have announced futures contracts on GPU rental rates targeted for late 2026, pending regulatory review. Index settled futures are standardized contracts on GPU rental price indexes, just like futures on other commodities. Buyers of compute lock in training and inference costs, sellers forward-sell capacity that they are planning to build and lenders can hedge the value of GPU collateral. The contracts are quoted in dollars per GPU hour and get settled in cash against the benchmark index. No hardware changes hands as contracts settle in dollars against the reference index, exactly like cash-settled equity derivatives.

Kalshi and Polymarket (Event contracts) Prediction market platforms like Kalshi (CFTC-regulated) and Polymarket offer event contracts on GPU rental prices. For example, a typical compute event contract listed on Kalshi can be “Price of NVIDIA B200 above \$7 by end of 2026?” - specifying the GPU model, prices and duration. The contract pays \$1 if the price is above \$7 on the settlement date and \$0 if not. Further, if the contract is trading at \$0.4, there is a 40% implied probability that B200 rental rates will exceed \$7 by the end of the year. Hence, compute contracts on prediction markets also help in building a probability distribution of future GPU prices. Kalshi is now aggregating data across multiple live contracts to derive a forward pricing curve for different GPU models.

## Architect's ComputeConnect (Exchange-for-physical)

Architect has announced ComputeConnect, an exchange that turns cash-settled compute futures into real, delivered GPU capacity. Exchange for physical products allows a futures position to be converted into actual GPU capacity through a physical settlement system. ComputeConnect operates with a network of neoclouds and capacity providers, allowing physical settlement (actual GPU capacity) through bilateral negotiations. Participants can swap a futures position for compute delivery, by negotiating the grade, timing and location of the physical delivery. Other compute market derivative products like index-settled futures, event contracts and perpetuals are mostly cash settled, only providing economic exposure to the participants and with no mechanism to actually fulfill their delivery requirements.

Architect's AX Perpetual Futures exchange: Architect's AX exchange already lists perpetual-style compute futures in the offshore markets. Perpetual futures are contracts with no expiry that track the spot index through a funding-rate mechanism, a structure that evolved in crypto markets. Perpetuals are among the early derivative products built for compute due to faster launch (via offshore structures) and bootstrapped liquidity from speculative flow. When perps trade above the tracked index, longs periodically pay shorts, which pushes the price back down (and vice versa). A persistent positive funding rate means the market is bullish on spot prices. Perpetual contracts can be a good hedge for neoclouds selling capacity on demand without having exposure to one future date or an enterprise buying on-demand compute.

EXHIBIT 3: Summary of market players by underlying financial structure and market mechanism

<table><tr><td></td><td>CME &amp; ICE</td><td>Architect (AX)</td><td>Architect - American Innovation Exchange</td><td>Kalshi</td></tr><tr><td>Contracts</td><td>Futures</td><td>Perps</td><td>EFP and Futures</td><td>Binary/Event contracts</td></tr><tr><td>Settlement</td><td>Cash settled</td><td>Cash settled</td><td>Physical (GPUs) or Cash</td><td>Cash (Binary payout)</td></tr><tr><td>Index</td><td>CME - Silicon Date ICE - Ornn</td><td>Ornn</td><td>Compute Desk</td><td>Ornn</td></tr><tr><td>Regulation</td><td>CFTC regulated - DCM, traditional clearing houses</td><td>Offshore (Bermuda), outside CFTC purview</td><td>US-DCM, Compute futures pending CFTC review</td><td>CFTC regulated - DCM (event driven binary options)</td></tr></table>

Forward curves are only live on Kalshi currently, rest may launch in future
Source: Company websites, Bernstein analysis

## SETTLEMENT INFRASTRUCTURE - CASH VS PHYSICAL DELIVERY

There are two settleme

[中间内容因长度限制已省略]

tained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
