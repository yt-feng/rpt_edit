你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
Global Energy Storage

# Quick Take: Global Energy Storage: China announces consumption tax on batteries - Implications

![](images/c2f12b895fab2d0a730e20b8b4347cd82dc939a1a005fe9c55a61c59eda89cea.jpg)

Neil Beveridge, Ph.D.

+852 2123 2648

neil.beveridge@bernsteinsg.com

![](images/e3a6fb2af24e22e3bed3d5a9d4481c4f3ab63a0b1933fe1b76771cc39f240c62.jpg)

Brian Ho, CFA

+852 2123 2615

brian.ho@bernsteinsg.com

![](images/682b8f68eeab52586d5fd1228bac0fd94e2d65f58167f43e0d0fffee1506b6e1.jpg)

Kelvin Yuan, Ph.D., CFA

+852 2123 2612

kelvin.yuan@bernsteinsg.com

China has announced the introduction of a consumption tax on the lithium-ion battery industry after an 11-year exemption. Starting from September 1, 2026, a 2% consumption tax will be levied on lithium-ion batteries at the cell level. The tax rate will subsequently double to 4% beginning September 1, 2027. To prevent double taxation within the supply chain, batteries produced for internal use in the continuous production of other taxable battery products will be exempt, and taxes paid on externally purchased batteries used in continuous production can be deducted.

The impact on battery pack price will be relatively small but nevertheless will raise costs. Current battery prices for LFP and NMC are US\$54.8/kWh and US\$66.2/kWh respectively. While the increase in tax will raise the cost of battery cells by 2% (2026) and 4% by 2027, at the pack level the increase in costs will be 1% (2026) and 3% (2027) by 2027. For ESS systems the new tax will increase the cost by 1-2% by 2027 which should limit the demand impact.

Sodium ion and solid-state batteries will be exempt from the new consumption tax. The new tax covers all conventional lithium-based battery technology including LFP batteries, nickel-based batteries, and vanadium redox flow batteries. Emerging battery technologies such as sodium-ion batteries, solid-state batteries, and fuel cells will remain entirely exempt from the consumption tax through the end of 2028 and possibly beyond. We expect that by 2030, roughly $10 - 20\%$ of total battery production in China will be solid state or sodium-ion.

Battery exports will be unaffected by the new consumption tax. The consumption tax will only apply to domestic sales and not levied on imports. Currently, around 20% of total battery production in China is exported and will be impacted by the new tax.

While the policy could negatively impact demand or margins for the industry, it is aimed at curbing overcapacity as part of China's broader anti-involution policies and encouraging new technologies. The China battery industry is plagued by overcapacity at the Tier 2 level. Battery makers will either have to absorb this cost or pass on to OEM's. For Tier 2 battery makers on wafer thin margins, this policy is intended to curb excessive capacity expansion. It will also be a strong signal to encourage a shift towards battery technologies of the future, namely sodium-ion and solid state which are both on the cusp of large-scale commercialization.

On 16 July 2026, China's Ministry of Finance, General Administration of Customs, and State Taxation Administration issued Announcement No. 20 of 2026, introducing a phased consumption-tax regime for certain battery products. The policy primarily affects batteries produced, processed, sold, imported, or used domestically in China. Details o the impact on battery pricing is shown below.

EXHIBIT 1: Price & change for LFP and NMC under different tax rate

<table><tr><td colspan="4">Cell level (USD/kWh)</td><td colspan="3">Package level(USD/kWh)</td></tr><tr><td></td><td>Current</td><td>Post tax 2%</td><td>Post tax 4%</td><td>Current</td><td>Post tax 2%</td><td>Post tax 4%</td></tr><tr><td>LFP</td><td>54.8</td><td>55.9</td><td>57.0</td><td>79.3</td><td>80.4</td><td>81.5</td></tr><tr><td>NMC</td><td>66.2</td><td>67.5</td><td>68.8</td><td>101.5</td><td>102.8</td><td>104.1</td></tr><tr><td colspan="4">Price chage (USD/kWh)</td><td colspan="3">Price change (USD/kWh)</td></tr><tr><td>LFP</td><td></td><td>1.1</td><td>2.2</td><td></td><td>1.1</td><td>2.2</td></tr><tr><td>NMC</td><td></td><td>1.3</td><td>2.6</td><td></td><td>1.3</td><td>2.6</td></tr><tr><td colspan="4">% of change</td><td colspan="3">% of change</td></tr><tr><td>LFP</td><td></td><td>2%</td><td>4%</td><td></td><td>1%</td><td>3%</td></tr><tr><td>NMC</td><td></td><td>2%</td><td>4%</td><td></td><td>1%</td><td>3%</td></tr></table>

Source: Baiinfor, Bernstein analysis and estimates

## KEY TAX-RATE CHANGES

From 1 September 2026, the following battery products will be subject to a $2\%$ consumption tax:

• Lithium-ion rechargeable batteries;(LFP and NMC)

• Primary lithium batteries;

• Mercury-free primary batteries;

• Nickel-metal hydride batteries;

\- Vanadium redox-flow batteries.

The tax rate for these products will increase from 2% to 4% on 1 September 2027.

## TEMPORARY EXEMPTIONS FOR EMERGING TECHNOLOGIES

China will continue to exempt the following products from consumption tax from 1 September 2026 through 31 December 2028:

\- Sodium-ion batteries;

\- Solid-state batteries;

\- Fuel cells;

• Perovskite photovoltaic cells;

• Tandem photovoltaic cells;

• Gallium-arsenide photovoltaic cells.

The announcement does not specify the tax treatment of these emerging technologies after 31 December 2028.

## CONDITIONS FOR CLAIMING AN EXEMPTION

The exemptions are not automatic. Battery products manufactured or processed under commission must comply with the applicable Chinese national standards. Products that do not meet the relevant national standard—or for which no national standard exists—cannot qualify for the preferential treatment.

Before filing the first consumption-tax exemption claim, a taxpayer must obtain a product testing report from a qualified testing institution. The institution must hold a valid CMA-accredited Inspection and Testing Institution Qualification Certificate, and its approved testing scope must include the relevant battery-testing items.

## DEDUCTION FOR TAX ALREADY PAID ON BATTERY INPUTS

Where a company purchases, imports, or receives from commissioned processing battery products on which consumption tax has already been paid, and then uses those products to continuously manufacture other taxable battery products, the company may deduct the consumption tax already paid on the inputs. The deductible amount is determined based on the quantity actually used in production during the relevant period.

Similarly, taxable batteries produced and used internally for the continuous production of other taxable batteries are not subject to consumption tax at the point of internal transfer. However, if the batteries are used to manufacture non-taxable products or for other purposes, consumption tax becomes payable when they are transferred for such use.

## EXPORT TREATMENT: NO CHANGE TO CONSUMPTION-TAX EXPORT RELIEF

Importantly, the new consumption-tax adjustment is mainly a domestic-market measure. It primarily applies at the following stages:

• Domestic production and sale;

• Commissioned processing;

\- Importation into China; and

\- Internal use outside the continuous production of taxable batteries.

For battery products that are exported, the existing consumption-tax refund or exemption treatment remains unchanged. In other words, the announcement does not impose an additional consumption-tax burden on qualifying battery exports.

A careful distinction should nevertheless be made between:

Consumption-tax export refund/exemption, which was not changed by this policy; and VAT export rebates, which are governed by a separate policy.

## BUSINESS IMPLICATIONS

The policy represents a shift from broad tax exemptions toward differentiated treatment based on technological maturity:

\- Established technologies, particularly conventional lithium-ion batteries, will gradually move to the standard 4% consumption-tax rate;

\- Emerging technologies, such as solid-state and sodium-ion batteries, will continue to receive tax support;

\- Domestic manufacturers and importers will need to review pricing, product classifications, contracts, and tax-accounting systems;

\- Export-oriented companies should separate the consumption-tax impact from the separate VAT export-rebate changes;

\- Companies claiming exemptions must maintain national-standard compliance documents and valid CMA-accredited testing reports;

• Manufacturers should establish detailed records for tax-paid battery inputs to support consumption-tax deductions.

## INVESTMENT IMPLICATIONS

The introduction of a consumption tax on lithium-ion batteries is a surprise. We think this will do nothing to help long term demand, which is unfortunate given the strategic role batteries will play in electrification of China's energy system. However, the increase needs to be seen in context. Assuming the 4% increase in consumption tax by September 2027, increase in price for battery packs will be <3%, while for ESS systems the overall increase in cost will be 1-2%, which is unlikely to have a material impact on demand. If the tax is not passed through however, it will impact the margins of battery makers, which are already wafer thin for some of the Tier 2 battery makers. Given the exuberance in the industry following triple digit ESS demand, the rationale for the new tax is likely aimed at curbing overcapacity within the industry and dampening down capex expansion plans. It is also designed as clear signal for battery makers in China to pivot into sodium-ion and solid state batteries which will be exempt from the tax. For China's leading player CATL, the new tax possibly explains why the stock has been so weak over the past month, despite strong industry fundamentals, which makes us think that the reaction to this announcement on Friday evening may not be significant. While this is not a positive for CATL, we think it will help curb over capacity efforts by Tier 2 players leading to greater industry consolidation longer term. It will also not impact CATL's exports or Na-ion/solid state batteries which CATL is at the forefront of the industry in commercializing. Overall, while this is not a positive headline for CATL, given the P/E valuation of 13x (A-share) and 18x (H-share), for a company growing revenues at 20-30% CAGR overt the next 5 years, the risk reward continues to look attractive. We rate CATL as Outperform.

## BERNSTEIN TICKER TABLE

<table><tr><td colspan="3"></td><td rowspan="2">16 Jul 2026 Closing Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>3750.HK (CATL)</td><td>O</td><td>HKD</td><td>621.00</td><td>770.00</td><td>40.1%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>33.2</td><td>24.5</td><td>18.7</td></tr><tr><td>300750.CH (CATL)</td><td>O</td><td>CNY</td><td>366.20</td><td>800.00</td><td>12.0%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>22.7</td><td>16.7</td><td>12.7</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,865.18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's "affiliates" relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Contemporary Amperex Technology Co Ltd

We value CATL (A) using the DCF approach using a WACC of 9.6% and a terminal growth rate of 3%. Our DCF model is based on annual free cash flow forecasts until 2050, plus a terminal value estimate to capture the continuing value of the company. Our price target is RMB800.

We value CATL (H) using the DCF approach using a WACC of 10.4% and a terminal growth rate of 3%. Our DCF model is based on annual free cash flow forecasts until 2050, plus a terminal value estimate to capture the continuing value of the company. Our price target is HKD770.

## RISKS

## Contemporary Amperex Technology Co Ltd

For CATL (A), key risks include: 1) overcapacity of battery manufacturing in China 2) geopolitical factors which restrict CATL market share and 3) increased competition from vertically integrated OEM's.

For CATL (H), key downside risks include: 1) overcapacity of battery manufacturing in China 2) geopolitical factors which restrict CATL market share and 3) increased competition from vertically integrated OEM's.

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

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

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

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in

this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand h

[中间内容因长度限制已省略]

gence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan

KK（サンフォード・C・バーンスタイン株式会社）。All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
