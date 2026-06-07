你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# All the Data Center Demand in the World, Still Not Enough Supply

Demand for data centers continues to outpace supply, with hyperscaler capex accelerating and chip volume forecasts implying GWs of capacity ahead of feasible data center delivery. Demand is not the issue, but the supply chain is. Our DC Capacity data pulls show only 8.9 GW was lit in '25, while data center demand was nearly 21.1 GW, a \~12 GW deficit, highlighting a tight DC market, and supporting a favorable backdrop for DC REITs and AI DC Developers.

Demand Signals Are Unambiguous Across Every Metric: Hyperscaler capex is on pace for \$770B in CY26E, up 74% YoY and nearly 5x the \$156B deployed in CY23. Combined cloud backlog surged to \$2T in 1Q26, growing 3x faster than capex since CY23. Bottom-up accelerator sales volumes from our semiconductor team imply \~30 GW of global AI power demand in 2026E from GPU/XPU shipments alone, with 19 GW going to North America, nearly 2x the 10.3 GW of new capacity we expect to come online.

Six Physical Supply Constraints Set the Ceiling on Deliverable Capacity: Our proprietary DC Capacity Delivery Model calibrates supply ceilings across six constraint categories. We estimate EPC/Labor as the binding constraint in 2026E, with a ceiling of 10.4 GW. Cooling is nearly co-binding at 11.4 GW and becomes the binding constraint from 2028E onward.

Structural Undersupply Benefits Operators, Suppliers, and New Entrants Across the DC Ecosystem: With vacancy rates at 1-3% across primary markets and wholesale rents accelerating, the demand/supply imbalance continues to benefit operators, suppliers, and new entrants alike. DC REITs (DLR, EQIX, IRM) have realized meaningful growth in leasing volumes and pricing over the past several years, with rents and bookings accelerating alongside AI-driven demand. Supply chain tightness is equally favorable for equipment suppliers, where order growth continues to outpace revenue delivery across cooling, electrical, and power transformer manufacturers, with backlogs expanding at 2-4x the rate of revenue. The demand and supply imbalance is also supporting the emergence of new entrants, including those from the Bitcoin mining industry. CORZ, CIFR, HUT, RIOT, and WULF are converting existing infrastructure to serve AI/HPC workloads, leveraging energized sites and established grid connections to deliver capacity on compressed timelines that other developers, constrained by the multi-year interconnection queue and equipment lead times, struggle to match. See our initiation, AI Data Center Developers: Fresh Faces, Same Math, for more detail on the BTC-to-HPC thesis.

Our Data Validates the Trend; With the Data Center Industry Exiting 2025 With a 12 GW Deficit: According to Aterio's comprehensive site database, only 3.4 GW of lit data center capacity came online that were not hyperscaler self-builds in North America in 2025, against 15.6 GW of leases signed (per Data Center hawk), a 12.2 GW deficit. This gap has been growing significantly, from 2.9 GW in 2023 to 4.3 GW in 2024 and nearly tripling to 12.2 GW in 2025. From 2021 to 2025, the cumulative deficit has reached 20.4 GW of undelivered data center capacity, a trend we expect to worsen as demand continues to outpace the supply chain's ability to deliver. We expect hyperscalers to continue to commit to capacity further into the future. Currently, they tend to commit to capacity deliverable within 12-18 months, but we could see that widen to 24+ months given supply constraints.

Exhibit 4 - In 2025, Data Center Leases Signed Exceeded Actual Delivered Capacity by Over 12 GWs   
![](images/c239a5ae31a91c35998063ba9ad36e0d319f7947745ef7d6073fd806f37242c4.jpg)

<details>
<summary>bar</summary>

| Year | Colocation Leases Signed (DC Hawk) | Lit Colocation Capacity (Aterio) | Gap |
|------|------------------------------------|----------------------------------|-----|
| 2017 | 0                                  | 0                                | 0   |
| 2018 | 0                                  | 0                                | 0   |
| 2019 | 0                                  | 0                                | 0   |
| 2020 | 0                                  | 0                                | 0   |
| 2021 | 0                                  | 0                                | 0   |
| 2022 | 2                                  | 1                                | -1  |
| 2023 | 4                                  | 1                                | -3  |
| 2024 | 6                                  | 2                                | -5  |
| 2025 | 15                                 | 3                                | -12 |
</details>

Source: Aterio, Data Center Hawk, JEF

Exhibit 5 - Under Construction GW in North America is Over 6x the Capacity Delivered in 2025   
![](images/c521906525f6b2404dc5fddd45b486077b508a4fd852b4ef0c558a54cea5f90e.jpg)

<details>
<summary>bar_line</summary>

| Year | Hyperscaler Self Builds (Construction) | Colocation (Construction) | Under Construction / Annual Lift Capacity |
|---|---|---|---|
| 2010 | 0.0 | 0.0 | 0.0 |
| 2011 | 0.0 | 0.0 | 1.0 |
| 2012 | 0.0 | 0.0 | 1.5 |
| 2013 | 0.0 | 0.0 | 1.5 |
| 2014 | 0.0 | 0.0 | 1.5 |
| 2015 | 0.0 | 0.0 | 1.5 |
| 2016 | 0.0 | 0.0 | 2.0 |
| 2017 | 0.0 | 0.0 | 1.5 |
| 2018 | 0.0 | 0.0 | 2.5 |
| 2019 | 0.0 | 0.0 | 2.5 |
| 2020 | 0.0 | 0.0 | 2.5 |
| 2021 | 0.0 | 0.0 | 3.5 |
| 2022 | 0.0 | 0.0 | 4.5 |
| 2023 | 0.0 | 0.0 | 5.5 |
| 2024 | 1.4x | 1.4x | 6.7x |
| Jun-26 | 6.7x | 4.5x | 8.5x |
</details>

Source: JEF, Aterio

Jonathan Petersen \* | Equity Analyst

(212) 284-1705 | jpetersen@JEF.com

Stephen Volkmann, CFA \* | Equity Analyst

(212) 284-2031 | svolkmann@JEF.com

Julien Dumoulin-Smith \* | Equity Analyst

+1 (281) 774-2066 | jds@JEF.com

Brent Thill \* | Equity Analyst

(415) 229-1559 | bthill@JEF.com

Blayne Curtis \* | Equity Analyst

+1 (212) 336-7493 | bcurtis@JEF.com

Roger Samuel, CFA ^ | Equity Analyst

+612 9364 2931 | rsamuel@JEF.com

Paul Zimbardo \* | Equity Analyst

+1 (212) 778-8497 | pzimbardo@JEF.com

Aniket Shah, PhD \* | Head of Sust. & Transition Strategy

(212) 323-3976 | ashah14@JEF.com

Edison Lee, CFA ‡ | Equity Analyst

852 3743 8009 | edison.lee@JEF.com

Stephanie Dossmann § | Equity Analyst

+33 1 8665 6367 | sdossmann@JEF.com

Mike Prew || | Equity Analyst

44 (0) 20 7029 8422 | mprew@JEF.com

Sarim Chaudhry || | Equity Analyst

+44 (0)20 7029 8423 | schaudhry1@JEF.com

Jan Aygul \* | Equity Associate

+1 (917) 344-1839 | jaygul@JEF.com

Matthew Roberts \* | Equity Associate

+1 (212) 778-8524 | mroberts1@JEF.com

Our Top Picks to Play DC Supply Chain Tightness (see inside for more details): DLR, EQIX, CORZ, WULF, CAT, ETN, WCC, PRIM, MTZ, NI, ETR, GEV, CRDO, AMZN, CRWV, GOOGL, MSFT, MRL SM, BBOX LN, SGRO LN.

Exhibit 1 - Data Center Capacity Additions in North America (GW)   
![](images/8b2d4703361956c1dd72521eb2c74014fcce24407f53c9c23fd526f88f6f7f2f.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Colocation (Delivered GWs) | Hyperscaler Self Builds (Delivered GWs) |
|---|---|---|
| 2011 | 0.3 | 0.2 |
| 2012 | 0.3 | 0.2 |
| 2013 | 0.5 | 0.3 |
| 2014 | 0.3 | 0.7 |
| 2015 | 0.6 | 0.8 |
| 2016 | 0.3 | 0.9 |
| 2017 | 0.8 | 1.1 |
| 2018 | 0.6 | 1.1 |
| 2019 | 0.4 | 2.1 |
| 2020 | 0.3 | 2.2 |
| 2021 | 0.3 | 2.0 |
| 2022 | 0.3 | 1.6 |
| 2023 | 0.3 | 2.7 |
| 2024 | 0.3 | 3.9 |
| 2025 | 3.4 | 5.5 |
</details>

Source: JEF, Aterio

Exhibit 2 - Installed Data Center Capacity Total in North America (GW)   
![](images/752d3709188b48a4c42a3a269559f8c5da762de76c77ccec32bcebc51a8c9267.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Colocation | Hyperscaler Self Builds |
|---|---|---|
| 2011 | 5 | 1 |
| 2012 | 6 | 1 |
| 2013 | 6 | 1 |
| 2014 | 7 | 2 |
| 2015 | 7 | 2 |
| 2016 | 8 | 3 |
| 2017 | 8 | 4 |
| 2018 | 9 | 5 |
| 2019 | 10 | 6 |
| 2020 | 11 | 9 |
| 2021 | 12 | 11 |
| 2022 | 13 | 12 |
| 2023 | 14 | 15 |
| 2024 | 17 | 19 |
| 2025 | 20 | 24 |
</details>

Source: JEF, Aterio

Exhibit 3 - Top 15 Data Center Operators/Owners in North America by Power (GW)   
![](images/42d97dec3050d59fe6df1fc333b0d42cd4817cc8a4bd0b876fa1e9f35099900b.jpg)

<details>
<summary>bar</summary>

| Company | Value |
| :--- | :--- |
| Amazon Aws | 10.6 |
| Microsoft | 5.5 |
| Google | 5.2 |
| Facebook | 4.8 |
| Digital Realty | 2.5 |
| Qts Data Centers | 2.5 |
| Cyrusone | 1.2 |
| Vantage Data Centers | 1.2 |
| Switch Data Centers | 1.2 |
| Xai | 0.9 |
| Aligned Data Centers | 0.9 |
| Equinix | 0.7 |
| Ntt Global Data Centers | 0.6 |
| Cloudhq | 0.6 |
| Centersquare | 0.6 |
</details>

Source: JEF, Aterio

# Table of Contents

<table><tr><td>Best Investments in a Data Center Supply Constraint World</td><td>4</td></tr><tr><td>Our Data Center Capacity Model</td><td>7</td></tr><tr><td>Data Center Demand is Robust</td><td>8</td></tr><tr><td>Supply Chain Constraints: What are They and Which Companies?</td><td>13</td></tr><tr><td>What About the NIMBYs?</td><td>19</td></tr><tr><td>International Opportunity: If We Can&#x27;t Build it Here, Build it Over There</td><td>21</td></tr></table>

# Best Investments in a Data Center Supply Constraint World

# Jon Petersen (REITs and Digital Infrastructure)

- CORZ is the pioneer of the BTC-to-AI data center developer movement, as the company was the first to make the pivot with a 590 MW development for CoreWeave. The company trades at a discount to peers, despite having the largest powered land bank to drive future growth.   
- DLR is a data center REIT with a combined wholesale and enterprise Colo platform seeing meaningful demand acceleration as AI workloads scale. Enterprise Colo bookings have accelerated from roughly \~\$50M per quarter to nearly \~\$100M per quarter, with AI now representing \~33-50% of aggregate bookings and \~20% of enterprise Colo activity, up from low-teens levels last year.   
- EQIX operates the most interconnected data center platform globally, enabling low-latency infrastructure across its ecosystem and positioning it as the natural hub for inference and edge compute. Four of the top five neocloud providers and eight of the top ten AI labs are deployed across its network.   
- WULF is an AI data center developer that repositioned its BTC mining land sites to turn key data centers built for neoclouds and hyperscalers. Management's deep experience and legacy in the power & utilities market positions the company well to continue to procure powered land sites and build AI data centers.

# Stephen Volkmann (Machinery and Industrials)

\- CAT remains our top pick in Machinery despite upside from power gen already largely baked into estimates and consensus. We see upside in the gas cycle, which will need to come given increased demand from data centers.

# Blayne Curtis (Semiconductors)

\- CRDO: We believe AEC adoption across XPU and CPU platforms is still in its early stages, supporting durable unit growth through C28+. Ramp of the 1.6T AECs in late '26 and early '27 should provide a material ASP uplift, bolstering our above-consensus revenue forecasts. ZF Optics provides a meaningful NT revenue opportunity, expanding the addressable market and diversifying the portfolio beyond electrical.

# Brent Thill (Internet Software)

- AMZN. We believe the stock screens as a mispriced AI/cloud/retail compounder, with AWS positioned to reaccelerate as AI capacity comes online, backlog converts to revenue, and Anthropic/OpenAI-related demand scales. Retail and ads remain durable margin drivers, while Trainium, Bedrock, Kiro, and longer-term opportunities like Leo add incremental upside that we believe is not fully reflected in the stock.   
- CRWV. CRWV is one of the best in the industry at scaling HPC infrastructure, with 1GW of active capacity today and plans to scale toward 8GW by FY30. The company already counts many of the largest hyperscalers, including MSFT, META and GOOGL, as well as leading AI natives such as OpenAI, Cursor and Anthropic, as customers. At a \$63B market cap versus \$99B of RPO and a multi-trillion-dollar AI infrastructure buildout ahead, we view valuation as compelling. We believe the stock can inflect in 2H as margins inflect and RPO continues to benefit from unrelenting AI demand.

- GOOGL. One of the best-positioned AI platforms given its vertically integrated stack spanning custom silicon/TPUs, Gemini models, developer tooling, and scaled consumer/enterprise surfaces. Gemini traction, combined with Google's unmatched data moat across Search, YouTube, Android, Workspace, and Cloud, creates a structural advantage that is difficult to replicate and should support durable AI monetization across both advertising and Cloud.   
- MSFT. MSFT is positioned to be an enterprise AI winner, with a differentiated end-to-end stack across Copilot, Azure AI, identity, and infrastructure supporting durable double-digit revenue and operating income growth despite elevated AI investment. Copilot paid seats are scaling, Azure AI demand continues to build, and we believe investor concerns around AI-related margin pressure are likely to prove overstated as monetization broadens.

# Julien Dumoulin-Smith (Power and Utilities)

- GEV. Provider of natural gas turbine and power generation infrastructure as well as grid electric components and wind turbines. Long lead cycle generation remains a key constraint but is not the critical path item for many projects. We are bullish on the long-term services value in the 2030s that is not fully appreciated.   
- NI. Indiana focused regulated utility with innovative 'GenCo' structure which allows for premium returns on building generation for hyperscalers. Current customers are Amazon and Alphabet with potential for more, as well as expansions.   
- PRIM. Engineering, procurement, and construction (EPC) company focused with power generation, power delivery, and pipeline focus. Renewables has been a challenging area for the company but are well positioned to execute on simple cycle gas combustion turbine (CT) build out. Access to skilled labor is the single most significant constraint in the power and thus data center ecosystem from our conversations.

# Stephanie Dossman (European REITs)

\- MRL has accelerated its pivot from traditional real estate to DC development in Iberia since 2024. The group is backed by well-located land and strong partnerships across both energy (notably Solaria) and operations, with Edge and CoreWeave. We expect +15% FFOps CAGR over 2025-32E and +11% NTAs CAGR over 2025-32E.

# Edison Lee (Chinese Tech and Telecom)

\- VNET is well-positioned to benefit from the China AI demand surge, supported by its rich power resources in Ulanqab - a desirable location for AI demand. Recent improving D-S dynamics in China also generates a more favorable project economics for IDC operators. Trading at \~10x 2026E EV/EBITDA vs 22% EBITDA Cagr (2026-29E), VNET remains highly attractive (here and here).

# Roger Samuel (Australian TMT)

\- MP1 AU: Megaport is transforming into a neocloud, benefiting from rising AI demand. Given that its core networking business already has a presence in over 1100 data centres around the world, Megaport is able to spread AI servers across these data centres and connect them using its mesh network. Latest note here

\- IFT AU/IFT NZ: Infratil owns a 50% stake in CDC, the largest data centre operator in Australia. Recently CDC signed the largest deal ever in the country: a 555MW contract with a US customer at premium pricing to its peers. With over 1.6GW in data centre pipeline, CDC is well-positioned to deliver further large contracts, especially when there is a power constraint in the US.

# Mike Prew (UK REITs)

- BBOX - Tritax management has incubated a power-backed, comprehensive DC business with 1GW of potential DC capacity. We think the

[中间内容因长度限制已省略]

 the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
