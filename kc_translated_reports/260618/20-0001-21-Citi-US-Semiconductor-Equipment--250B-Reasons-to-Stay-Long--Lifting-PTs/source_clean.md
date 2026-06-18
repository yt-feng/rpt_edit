# US Semiconductor Equipment
## CITI'S TAKE

We update our bull case WFE to \$145B/\$200B/\$250B in 2026/27/28, align AMAT/LRCX/KLAC estimates to our revised WFE model, and lift PTs to \$710/\$450/\$290 respectively as we roll forward our price targets based on CY28 earnings powers. Incrementally, we are bullish on NAND equipment demand as a widening gap between required DRAM and available supply helps adoption of complementary solutions such as KV cache off-loading.

Introducing 2028 WFE of \$250B — We update our top-down WFE analysis for 2026/2027, and introduce 2028 WFE forecasts based on Citi's updated hyperscaler capex model of 84%/56%/38% growth in CY26/27/28. We now see bull case WFE of \~\$145Bn/\$200Bn/\$250Bn in 2026/27/28, implying another solid 25% growth in 2028. We are more constructive on 2028 WFE given continued capacity constraints and expansion at both TSMC and memory makers, as well as recent progress at Intel and Samsung foundries.

DRAM Bottleneck is Good for NAND Demand — The rise of agentic AI is driving a structural increase in NAND demand as memory requirements surge and DRAM supply tightens. Multi-step inference workflows are dramatically expanding KV cache footprints, pushing total memory requirements well beyond what high-cost HBM and DRAM can efficiently support, especially in an environment of constrained DRAM supply and elevated pricing. This pressure is already driving architectural trade-offs, as evidenced by report that Nvidia has reduced SoCAMM2 DRAM capacity in its Vera Rubin NVL72 systems by roughly 50% due to supply limitations and cost considerations (see note). This underscores a widening gap between required and available memory, and we are seeing companies accelerating the adoption of complementary solutions as a result, such as KV cache offloading where intermediate model state is shifted to lower-cost, higher-capacity storage tiers. Assuming a modern 150k wspm NAND fab can do \~15EB per year, implies we need 2-4 new greenfield fabs or \$20-40Bn capex, or \$15-\$30Bn NAND WFE to overcome DRAM bottlenecks.

## Atif Malik $^{AC}$


1 = Buy, 2 = Neutral, 3 = Sell, H = High Risk
Source: Citi
ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change
^Catalyst Watch


## Lifting TPs on AMAT, LRCX, & KLAC

## Updated Top-down WFE

We update our top-down WFE analysis for 2026/2027, and introduce 2028 WFE forecasts based on Citi's updated hyperscaler capex model of 84%/56%/38% growth in CY26/27/28. We now see bull case WFE of \~\$145Bn/\$200Bn/\$250Bn in 2026/27/28, implying another solid 25% growth in 2028. We are now more constructive on 2028 WFE given continued capacity constraints and expansion at both TSMC and memory makers, as well as recent progress at Intel and Samsung foundries. On the foundry side, in addition to the news on Terafab (see our prior note), Intel foundry is gaining traction at Google and Apple at various capacities, and Samsung is reported to be accelerating Taylor fab and working with Google TPU v10 on memory I/O die at 2nm, as well as in discussion with BYD on 2nm and 4nm autonomous driving chips. The capacity expansion plans and incremental customers engagement at Samsung/Intel all bode well for WFE, and the semi cap companies have been adding capacity for the past few years and will continue to do so to ensure they do not become a bottleneck for the industry.

Figure 1. WFE reaching \$200Bn/\$250Bn in CY27/28


Source: Citi

## DRAM bottleneck is good for NAND demand

The rise of agentic AI is driving a structural increase in NAND demand as memory requirements surge and DRAM supply tightens. Multi-step inference workflows are dramatically expanding KV cache footprints, pushing total memory requirements well beyond what high-cost HBM and DRAM can efficiently support, especially in an environment of constrained DRAM supply and elevated pricing. This pressure is already driving architectural trade-offs, as evidenced by report that Nvidia has reduced SoCAMM2 DRAM capacity in its Vera Rubin NVL72 systems by roughly 50% due to supply limitations and cost considerations (see note). Rather than indicating weaker demand, this underscores a widening gap between required and available memory, and we are seeing companies accelerating the adoption of complementary solutions as a result, such as KV cache offloading (as demonstrated by Nvidia's CMX earlier this year), where intermediate model state is shifted to lower-cost, higher-capacity storage tiers. More recently on Jun 15, AMD acquired MEXT, which focuses on memory optimization and has developed a predictive memory software solution that makes flash storage appear as DRAM-speed memory, which could expand usable memory capacity and potentially also reduce costs. Moreover, Apple's AFM 3 announced on Jun 8 also highlighted a new architecture that stores the LLM models in NAND instead of DRAM in order to

maximizing on-device AI capabilities. Coupled with ongoing innovation in high-performance NAND such as HBF and XL-Flash, we view this transition as structurally positive for NAND demand, as both cloud computing and on-device applications are increasingly rely on NAND to scale capacity, manage costs, and support the growing complexity of agentic AI workloads.

KV Cache offloading - KV cache offloading refers to the architectural technique of dynamically transferring intermediate attention states (key-value tensors) from HBM into lower-cost, higher-capacity tiers such as DRAM and, increasingly, NAND flash, effectively extending the usable memory footprint for LLM inference. As KV cache grows with agentic AI workload, it can quickly overwhelm GPU memory, and offloading mitigates this “memory wall” by creating a hierarchical system in which hot data remains on-GPU with HBM, while colder, less frequently accessed context is migrated to DRAM and further to SSDs and reloaded on demand. This shift directly drives NAND demand because enterprise SSDs become an active inference memory tier rather than passive storage - they are needed to deliver high-throughput, low-latency access to massive, persistent KV datasets that can span petabytes at scale.

Samsung and Micron both talked about their solution of TLC based PCIe Gen6 SSD for such AI workload. Sandisk is in the development of HBF and the timeline has recently been pulled forward by 6 months to 2H 26 pilot line (see note)

Kioxia's XL-Flash – The memory bottleneck is also driving innovation for storage companies. Kioxia's XL-FLASH is a low-latency, high-performance NAND-based flash memory designed to bridge the widening gap between ultra-fast but expensive DRAM and higher-capacity but slower conventional flash, especially for AI workloads. It addresses growing challenges in the memory hierarchy—where DRAM is limited by cost and scalability, and traditional flash cannot deliver memory-like responsiveness—by offering a non-volatile solution that can serve as an intermediate performance tier. XL-FLASH is compatibility with the CXL protocol, which allows flash-based memory to be accessed coherently as an extension of host memory rather than just as storage. Through CXL, XL-FLASH can function as part of a tiered memory architecture, expanding effective system memory at lower cost than DRAM while delivering near-memory performance for certain workloads, helping overcome bottlenecks such as limited memory slots, PCIe bandwidth constraints, and the increasing data demands of GPUs.

Figure 2. Kioxia's XL-Flash

[[KC_IMAGE_001]]


Source: Citi, Kioxia

## Raising Estimates on AMAT/LRCX/KLAC

As investor focus shifts beyond 2027 toward 2028, we introduce CY28 estimates for AMAT, LRCX, and KLAC and roll forward our price targets based on CY28 earnings power.

AMAT – We model total revenue growth of 30%/22% Y/Y in CY27/28, including 35%/25% from Silicon, and 14%/13% from AGS. We lift our TP to \$710 from \$550 prior, based on 31x P/E applied to CY28 EPS. The 31x P/E is consistent with our prior valuation and 55% above historical average of 20x on group AI re-rating and extended strong WFE upcycle, but 15% below peak P/E of 36x.

LRCX - We model total revenue growth of 28%/22% Y/Y in CY27/28, including 36%/25% from Systems, and 12%/13% from CSBG. We lift our TP to \$450 from \$315 prior, based on 40x P/E applied to CY28 EPS. The 40x P/E is up from 37x prior, 67% above historical average of 24x on group AI re-rating, extended strong WFE upcycle, and over-indexed NAND exposure, and 15% below peak P/E of 48x.

KLAC - We model total revenue growth of 24%/22% in CY27/28, including 28%/25% from SPC-systems, and 14%14% for SPC-services, and 15%/15% for EPC. We lift our TP to \$290 from \$206.4 prior, based on 40x P/E applied to CY28 EPS. The 40x P/E is up from 36x prior, 60% above historical average of 25x on group AI re-rating and extended strong WFE upcycle, and 20% below peak P/E of 50x.

Figure 3. Big 5 Semi Cap Historical P/E

[[KC_IMAGE_002]]


Source: Citi, FactSet

## Bull/Bear: Applied Materials Inc (AMAT.O)


[[KC_IMAGE_003]]


Spread 60pp
Current Price and expected returns (upside/downside) as of 16 Jun 2026

## BULL Assumptions


[[KC_IMAGE_004]]


WFE +30%/+40%/30% in 2026/27/28

• Market share gains in 3D logic deposition and etch drive revenue higher
- 35x P/E multiple expansion on faster secular growth

## BASE Assumptions


[[KC_IMAGE_005]]


WFE +25%/+35%/25% in 2026/27/28
• Stable market share in dep and etch in 2026/27
- 31x P/E

## BEAR Assumptions


[[KC_IMAGE_006]]


WFE digest in 2028 due to macro slowdown and slower AI data center investment
• 20x P/E - share loss

## Bull/Bear: KLA Corp (KLAC.O)


[[KC_IMAGE_007]]


Spread 62pp
Current Price and expected returns (upside/downside) as of 16 Jun 2026

## BULL Assumptions


[[KC_IMAGE_008]]


• WFE +30%/+35%/+30% in 2026/27/28

\- 45x P/E - Multiple expansion on share gains in new products and above average WFE growth led by SPC sales

## BASE Assumptions


[[KC_IMAGE_009]]


WFE 25%/+35%/25% in 2026/27/28

\- 40x P/E - Stable share and modestly better relative WFE growth

## BEAR Assumptions


[[KC_IMAGE_010]]


WFE digestion in 2028

• 25x P/E - Multiple contraction

## Bull/Bear: Lam Research Corp (LRCX.O)


[[KC_IMAGE_011]]


Spread 61pp
Current Price and expected returns (upside/downside) as of 16 Jun 2026

## BULL Assumptions


[[KC_IMAGE_012]]


WFE +25%/40%/30% in 2026/27/28

• Memory market share gains in deposition and etch drive increased revenue opportunity
• P/E 45x multiple expansion on faster secular growth

## BASE Assumptions


[[KC_IMAGE_013]]


• WFE +25%/35%25% in 2026/27/28
- Stable market share in deposition and etch
• P/E 40x 3D devices to drive outsized WFE growth

## BEAR Assumptions


[[KC_IMAGE_014]]


• WFE enter into digestion period in 2028
- Slow memory recovery lowers capex spend and limits top and bottom line growth
- P/E 25x - loss in market share in deposition and etch

## Applied Materials Inc

## Company description

Applied Materials is the leader in materials engineering solutions used to produce virtually every new chip and advanced display in the world. Applied's expertise in modifying materials at atomic levels and on an industrial scale enables customers to transform possibilities into reality.

## Investment strategy

We are Buy-rated on AMAT as we see it well exposed to multi-year WFE upcycle and secular megatrends like GAA, advanced packaging, and ICAPS in the next 2-3 years.

## Valuation

We value AMAT at \$710 using a 31x P/E multiple on 2028E EPS. We view a 31x multiple, above AMAT's 3-year average multiple of 20x, as appropriate given multi-year WFE upcycle, secular tailwinds, and incremental AI data center investment.

## Risks

Downside risks to the achievement of our target price include the following: 1) As fab utilization and capital equipment orders are closely linked to the stock price, any material differences to our supply/demand model (e.g. demand drops suddenly, or supply increases more rapidly than we predict) may cause our valuation methodology to be inaccurate. 2) As the market share leader in multiple sub-segments of semiconductor equipment, AMAT is uniquely positioned to capitalize on inflections as well as face tough competition from large peers in industry cycles.

## KLA Corp

## Company description

KLA develops industry-leading equipment and services that enable innovation throughout the electronics industry. It provides advanced process control and process-enabling solutions for manufacturing wafers and reticles, integrated circuits, packaging, printed circuit boards, and flat panel displays.

## Investment strategy

We are Buy rated on KLAC as a good play on growing process control intensity and AI-driven WFE multi-year upcycle.

## Valuation

We value KLAC at \$290 using a 40x P/E multiple on 2028E earnings power. We view a 40x multiple or above 3-year average of 25x on multiple re-rating in the group due to growing AI WFE exposure.

## Risks

The key upside/downside risks that could impede the stock from achieving our target price are: 1) lower/higher competition from competitors like AMAT/ASML; 2) foundry inventory correction risk on 10nm/7nm; and 3) fast/slow adoption of new Gen 4/5 and EUV products.

## Lam Research Corp

## Company description

Lam Research Corporation is a global supplier of innovative wafer fabrication equipment and services to the semiconductor industry. Today, nearly every advanced chip is built with Lam technology.

## Investment strategy

We are Buy-rated on LRCX as a good stock play on the 3D devices megatrend in the next 2-3 years and beneficiary of AI-driven data center capex spending with muti-year WFE upcycle.

## Valuation

We value LRCX at \$450 using 40x P/E multiple on CY2028 earnings. We view a 40x multiple vs 3-yr average of 24x but below peak of 48x as appropriate given extended WFE cycle, secular AI tailwinds, higher services or one third of total sales contribution, share gains, and rising equipment capital intensity.

## Risks

The key downside risks to our investment thesis and target price on LRCX include: 1) increasing competition in deposition and etch; 2) weaker-than-expected overall semi market demand, especially memory; and 3) slower-than-expected demand in China due to US-China trade and IP tensions.


## Appendix A-1


## IMPORTANT DISCLOSURES

## KLA Corp (KLAC)

Ratings and Target Price History


[[KC_IMAGE_015]]


\*Indicates Change
Rating/target price changes above reflect Eastern Time

## Applied Materials Inc (AMAT)

Ratings and Target Price History


[[KC_IMAGE_016]]


\*Indicates Change
Rating/target price changes above reflect Eastern Time

## Lam Research Corp (LRCX)

Ratings and Target Price History


[[KC_IMAGE_017]]


\*Indicates Change
Rating/target price changes above reflect Eastern Time

## KLA Corp (KLAC)

Short-Term View/Catalyst Watch Research


[[KC_IMAGE_018]]


CW - Catalyst Watch, STV - Short-Term View
Rating/target price changes above reflect Eastern Time

## Applied Materials Inc (AMAT)

Short-Term View/Catalyst Watch Research


[[KC_IMAGE_019]]


CW - Catalyst Watch, STV - Short-Term View
Rating/target price changes above reflect Eastern Time

## Lam Research Corp (LRCX)

Short-Term View/Catalyst Watch Research


[[KC_IMAGE_020]]


CW - Catalyst Watch, STV - Short-Term View
Rating/target price changes above reflect Eastern Time

Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of Applied Materials Inc.

Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from Applied Materials Inc, KLA Corp.

Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from KLA Corp.

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Applied Materials Inc, KLA Corp, Lam Research Corp in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): Applied Materials Inc, KLA Corp.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Applied Materials Inc, KLA Corp, Lam Research Corp.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Applied Materials Inc,KLA Corp,Lam Research Corp.
Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to Applied Materials Inc,KLA Corp,Lam Research Corp. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)


For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.


For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.


## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks.

Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

## Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share price to rise (fall) in absolute terms over a specified period of 30 or 90 days in reaction to one or more specific near-term catalysts or events impacting the company or the market. A Catalyst Watch will be published when Analyst confidence is high that an impact to share price will occur; it will be a STV when confidence level is moderate. A Catalyst Watch or STV Upside/Downside call will automatically expire at the end of the specified 30/90 day period. The Catalyst Watch will also be automatically removed if share price performance (calculated at market close) exceeds 15% against the direction of the call (unless over-ridden by the analyst). The analyst may also remove a Catalyst Watch or STV call prior to the end of the specified period in a published research note. A Catalyst Watch/STV Upside or Downside call may be different from and does not affect a stock's fundamental equity rating, which reflects a longer-term total absolute return expectation. For purposes of FINRA ratings-distribution-disclosure rules, a Catalyst Watch/STV Upside call corresponds to a buy recommendation and a Catalyst Watch/STV Downside call corresponds to a sell recommendation. Any stock not assigned to a Catalyst Watch Upside, Catalyst Watch Downside, STV Upside, or STV Downside call is considered Catalyst Watch/STV No View. For purposes of FINRA ratings distribution-disclosure rules, we correspond Catalyst Watch/STV No View to Hold in our ratings distribution table for our Catalyst Watch/STV Upside/Downside rating system. However, we reiterate that we do not consider No View to be a recommendation. For all Catalyst Watch/STV Upside/Downside calls, risk exists that the catalyst(s) and associated share-price movement will not materialize as expected.


## OTHER DISCLOSURES

Any price(s) of instruments mentioned in recommendations are as of the prior day's market close on the primary market for the instrument, unless otherwise stated.

The completion and first dissemination of any recommendations made within this research report are as of the Eastern date-time displayed at the top of the Product. If the Product references views of other analysts then please refer to the price chart or rating history table for the date/time of completion and first dissemination with respect to that view.

Regulations in various jurisdictions require that where a recommendation differs from any of the author's previous recommendations concerning the same financial instrument or issuer that has been published during the preceding 12-month period that the change(s) and the date of that previous recommendation are indicated. For fundamental coverage please refer to the price chart or rating change history within this disclosure appendix or the issuer disclosure summary at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures.

Citi has implemented policies for identifying, considering and managing potential conflicts of interest arising as a result of publication or distribution of investment research. A description of these policies can be found at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures.

The proportion of all Citi recommendations that were the equivalent to "Buy", "Hold", "Sell" at the end of each quarter over the prior 12 months (with the % of these that had received investment firm services from Citi in the prior 12 months shown in brackets) is as follows; Q1 2026 Buy 33%(63%), Hold 44% (52%), Sell 23% (46%), RV 0.5% (89%): Q4 2025 Buy 33% (63%), Hold 44% (50%), Sell 23% (46%), RV 0.4% (91%); Q3 2025 Buy 33% (61%), Hold 44% (52%), Sell 23% (50%), RV 0.4% (80%); Q2 2025 Buy 33%(63%), Hold 44% (51%), Sell 23% (49%), RV 0.4% (86%). For the purposes of disclosing recommendations other than for equity (whose definitions can be found in the corresponding disclosure sections), "Buy" means a positive directional trade idea; "Sell" means a negative directional trade idea; and "Relative Value" means any trade idea which does not have a clear direction to the investment strategy.

European regulations require a 5 year price history when past performance of a security is referenced. CitiVelocity's Charting Tool (https://www.citivelocity.com/cv2/#go/CHARTING\_3\_Equities) provides the facility to create customisable price charts including a five year option. This tool can be found in the Data & Analytics section under any of the asset class menus in CitiVelocity (https://www.citivelocity.com/). For further information contact CitiVelocity support (https://www.citivelocity.com/cv2/go/CLIENT\_SUPPORT). The source for all referenced prices, unless otherwise stated, is DataCentral, which sources price information from LSEG Data & Analytics. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance.

Investors should always consider the investment objectives, risks, and charges and expenses of an ETF carefully before investing. The applicable prospectus and key investor information document (as applicable) for an ETF should contain this and other information about such ETF. It is important to read carefully any such prospectus before investing. Clients may obtain prospectuses and key investor information documents for ETFs from the applicable distributor or authorized participant, the exchange upon which an ETF is listed and/or from the applicable website of the applicable ETF issuer. The value of the investments and any accruing income may fall or rise. Any past performance, prediction or forecast is not indicative of future or likely performance. Any information on ETFs contained herein is provided strictly for illustrative purposes and should not be deemed an offer to sell or a solicitation of an offer to purchase units of any ETF either explicitly or implicitly. The opinions expressed are those of the authors and do not necessarily reflect the views of ETF issuers, any of their agents or their affiliates.

Citi Global Markets India Private Limited and/or its affiliates may have, from time to time, actual or beneficial ownership of 1% or more in the debt securities of the subject issuer.

Please be advised that pursuant to Executive Order 13959 as amended (the “Order”), U.S. persons are prohibited from investing in securities of any company determined by the United States Government to be the subject of the Order. This research is not intended to be used or relied upon in any way that could result in a violation of the Order. Investors are encouraged to rely upon their own legal counsel for advice on compliance with the Order and other economic sanctions programs administered and enforced by the Office of Foreign Assets Control of the U.S. Treasury Department.

This communication is directed at persons who are "Eligible Clients" as such term is defined in the Israeli Regulation of Investment Advice, Investment Marketing and Investment Portfolio Management law, 1995 (the "Advisory Law"). Within Israel, this communication is not intended for retail clients and Citi will not make such products or transactions available to retail clients or to non-Eligible Clients. The presenter is not licensed as investment advisor or investment marketer by the Israeli Securities Authority ("ISA") and this communication does not constitute investment or marketing advice. The information contained herein may relate to matters that are not regulated by the ISA. Any securities which are the subject of this communication may not be offered or sold to any Israeli person except pursuant to a security offering exemption according to the Israeli Securities Law, 1968 and the public offering rules provided thereunder.

Citi broadly and simultaneously disseminates its research content to the Firm’s institutional and retail clients via the Firm’s proprietary electronic distribution platforms (e.g., Citi Velocity and various Global Wealth platforms). As a convenience, certain, but not all, research content may be distributed through third party aggregators. Clients may receive published research reports by email, on a discretionary basis, and only after such research content has been broadly disseminated. Certain research is made available only to institutional investors to satisfy regulatory requirements. The level and types of services provided by Citi analysts to clients may vary depending on various factors such as the client’s individual preferences as to the frequency and manner of receiving communications from analysts, the client’s risk profile and investment focus and perspective (e.g. market-wide, sector specific, long term, short-term etc.), the size and scope of the overall client relationship with the Firm and legal and regulatory constraints.

Pursuant to Comissão de Valores Mobiliários Resolução 20 and ASIC Regulatory Guide 264, Citi is required to disclose whether a Citi related company or business has a commercial relationship with the subject company. Considering that Citi operates multiple businesses in more than 100 countries around the world, it is likely that Citi has a commercial relationship with the subject company.


Investing in non-U.S. securities, including ADRs, may entail certain risks. The securities of non-U.S. issuers may not be registered with, nor be subject to the reporting requirements of the U.S. Securities and Exchange Commission. There may be limited information available on foreign securities. Foreign companies are generally not subject to uniform audit and reporting standards, practices and requirements comparable to those in the U.S. Securities of some foreign companies may be less liquid and their prices more volatile than securities of comparable U.S. companies. In addition, exchange rate movements may have an adverse effect on the value of an investment in a foreign stock and its corresponding dividend payment for U.S. investors. Net dividends to ADR investors are estimated, using withholding tax rates conventions, deemed accurate, but investors are urged to consult their tax advisor for exact dividend computations. Investors who have received the Product from the Firm may be prohibited in certain states or other jurisdictions from purchasing securities mentioned in the Product from the Firm. Please ask your Financial Consultant for additional details. Citi Global Markets Inc. takes responsibility for the Product in the United States. Any orders by US investors resulting from the information contained in the Product may be placed only through Citi Global Markets Inc.

## The Citi legal entity that takes responsibility for the production of the Product is the legal entity which the first named author is employed by.


This Product is available in Chile through Banchile Corredores de Bolsa S.A., an indirect subsidiary of Citi Inc., which is regulated by the Comisión Para El Mercado Financiero. Enrique Foster Sur, 20, piso 6, Las Condes, Santiago, Chile.
