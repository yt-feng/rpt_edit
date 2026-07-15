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
Americas Energy & Transition

# Americas Power & Energy Transition: Paying for speed vs. scale - The BTM/FTM/BYOG Framework for BE, FRVO, and ORA's Hyperscaler Deals

![](images/e601a2b224b803cce96981ca8deb22fbe2e36d951759e732af09501b8ead8f01.jpg)  
Sunaina Ocalan
.+1 917 344 8503
sunaina.ocalan@bernsteinsg.com

![](images/5144621a10c51c0b2e63938a0a88045de0247a95867d4c7cb56fdb3c98218683.jpg)

Anshika Bajpai

+1 917 344 8306

anshika.bajpai@bernsteinsg.com

![](images/2147c50bc493aeb7982cd258415a200a68ab8f772a9163e7f40c510e427e2309.jpg)

Raphael Lee
+1 917 344 8355
raphael.lee@bernsteinsg.com

\- BE, FRVO, and ORA now all have live, named hyperscaler or utility-anchored deals, but they sit in three structurally different boxes: Bloom is true behind-the-meter (BTM, zero interconnection exposure, \~90-day deployment); Ormat and most of Fervo's contracted volume are front-of-meter (FTM, grid-delivered, still queue-exposed); and Bloom's AEP deal is a third, hybrid category — utility-financed onsite generation ("BYOG") that could scale further than either pure model.

\- Bloom wins on speed and optionality —55- 90 days vs. 3–8 years for standard interconnection — but pays for it: illustrative LCOE of \$85–115/MWh driven by natural gas fuel exposure and a recurring stack-replacement cost.

\- Fervo's economics are a bet on its learning curve: Cape Station 1 wells were at \~\$7,000/kW, with the holy grail is hitting its stated \$3,000/kW target — which would make FTM geothermal cost-competitive with BTM fuel cells without the fuel-price exposure.

\- Ormat is the smallest, lowest-risk mover — brownfield uprate-style economics on existing geothermal assets — but its NV Energy Clean Transition Tariff deals are capped by resource availability (13–150 MW), not technology cost, and we don’t think will scale to gigawatt volumes the way Bloom or Fervo can.

As PJM, ERCOT, and FERC push interconnection reform (fast-track cycles, Order 2023, Batch Zero), the queue-bypass premium BTM currently commands should compress over the back half of this decade.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">10 Jul 2026</td><td>TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td colspan="2"></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td rowspan="2">Cur</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td></tr><tr><td>BE (Bloom Energy)</td><td>M</td><td>USD</td><td>244.61</td><td>276.00</td><td>843.0%</td><td>USD</td><td>0.82</td><td>2.30</td><td>4.27</td><td>296.9</td><td>106.2</td><td>57.3</td></tr><tr><td>FRVO (Fervo)</td><td>O</td><td>USD</td><td>27.13</td><td>47.00</td><td>NA</td><td>USD</td><td>(0.25)</td><td>(0.10)</td><td>(0.16)</td><td>(109.2)</td><td>(277.2)</td><td>(172.3)</td></tr><tr><td>ORA (Ormat Technologies)</td><td>U</td><td>USD</td><td>109.77</td><td>115.00</td><td>4.9%</td><td>USD</td><td>2.02</td><td>2.26</td><td>2.48</td><td>54.4</td><td>48.5</td><td>44.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,515.34</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

BE estimate is Adjusted EPS; BE valuation is Adjusted P/E (x);

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We are Market-Perform on Bloom, Outperform on Fervo, and Underperform on Ormat

## DETAILS

## 1. THE FRAMEWORK

Three structurally distinct models are now competing for the same hyperscaler capital, and the distinctions matter more than the shared "data center power" label suggests.

EXHIBIT 1: Different models of powering up

<table><tr><td>Model</td><td>Definition</td><td>Interconnection exposure</td><td>Representative deal</td><td>Typical speed</td></tr><tr><td>BTM (behind-the-meter)</td><td>Generation sited and consumed on the customer&#x27;s side of the utility meter; the utility interconnection process for that load is bypassed entirely.</td><td>None for the covered load — no generation or large-load interconnection queue involved.</td><td>Bloom/Oracle Project Jupiter — up to 2.8 GW MSA, full onsite power for the New Mexico AI campus.</td><td>~55-90 days from order to energized (Bloom&#x27;s stated figure).</td></tr><tr><td>FTM (front-of-meter)</td><td>Generation interconnects to the grid and sells through a utility or ISO; the customer&#x27;s load is served via a PPA sleeve, not a direct wire.</td><td>Full generation-interconnection queue exposure, plus transmission/delivery risk to the load.</td><td>Ormat/Switch Salt Wells (13 MW); Ormat/Google NV Energy portfolio (150 MW); most of Fervo&#x27;s SCE and NV Energy contracted volume.</td><td>2-4+ years from contract to energized power, even under expedited tariff structures.</td></tr><tr><td>BYOG (hybrid) (&quot;bring your own generation&quot;)</td><td>Utility contracts for and finances dedicated onsite/near-site generation to serve a large load its own grid capacity cannot accommodate — capital sits on the utility&#x27;s books, physically resembles BTM.</td><td>Utility-managed; avoids the large-load queue but the utility itself absorbs project and fuel-supply risk.</td><td>Bloom/AEP — $2.65B, up to 1 GW, 20-year offtake, announced Jan. 2026.</td><td>Faster than standard interconnection; slower than pure BTM given utility procurement processes.</td></tr></table>

## Source: Bernstein Analysis, Company filings

BTM revenue is largely insulated from the interconnection crisis that is otherwise the sector's central bottleneck (see prior notes on PJM capacity auctions and the interconnection queue). FTM revenue is not — it is simply competing for the same constrained queue slots as everyone else, with a corporate offtaker's name attached. BYOG is the wildcard: it turns the utility itself into the entity racing the queue on the customer's behalf, which is a different risk profile (utility credit, utility execution) than either pure model.

EXHIBIT 2: Speed to Power: BTM vs. FTM, vs. the last standard nuclear plant built in the US for reference  
![](images/ef64d18cbebf848b4c90fbabd8da47aa22f5032f1b98a1ae1072982c23980723.jpg)  
Source: Bernstein Analysis, Company filings, Deal announcements for Bloom

## 2. WHERE BE, FRVO, AND ORA SIT

## Bloom Energy – BTM plus a new BYOG wrinkle

Bloom's \~2.8 GW Oracle master services agreement (April 2026, 1.2 GW already contracted for 2026–2027 delivery) is textbook BTM: fuel cells sited at Oracle's Project Jupiter campus, DC-coupled via Bloom's native 800V DC architecture directly into IT racks, bypassing both the AC/DC conversion stack and the grid interconnection process for that load. The January 2026 AEP agreement (\$2.65B, up to 1 GW, 20-year offtake) is a different animal: AEP is contracting for Bloom capacity to serve large loads its own grid cannot accommodate quickly enough. The generation is still physically onsite/near-site, but the offtake counterparty is a utility, not the end customer — a hybrid structure with the utility bearing the credit and financing risk rather than the hyperscaler.

## Fervo Energy – FTM at scale, betting on the cost curve

Fervo's March 2026 Geothermal Framework Agreement with Google — up to 3 GW through 2033, with 1 GW prioritized in the first two years — is FTM: power is delivered through utility intermediaries (NV Energy, Southern California Edison) under conventional PPA structures, meaning every megawatt is still subject to generation-interconnection review even where NV Energy's Clean Transition Tariff is designed to streamline the commercial and regulatory path. Fervo's IPO filing discloses Cape Station is being built today at roughly \$7,000/kW — competitive with nuclear, but more than three times the cost of a gas plant — with a stated target of cutting that to \$3,000/kW through repeatable drilling and pad design.

## Ormat – the smallest, most de-risked mover

Ormat's two 2026 data center deals — the 13 MW Switch PPA at its existing Salt Wells plant (January 2026) and the up to 150 MW Google/NV Energy portfolio PPA (February 2026) — are also FTM, and notably conservative: Salt Wells is a brownfield upgrade to an already-interconnected facility, the geothermal equivalent of CEG's Braidwood/Byron uprate playbook rather than a greenfield EGS bet. Both deals run through NV Energy's Clean Transition Tariff and await PUCN approval (expected second half of 2026), with the Google portfolio not online until 2028–2030. Ormat is monetizing existing, de-risked assets at small scale.

EXHIBIT 3: Installed Capex - Fuel cells vs. EGS vs. gas or nuclear for reference  
![](images/3929c94e3245e03f9db066e28b2ec2a23e082cac037b2a831bc422e9a9789900.jpg)  
Source: Bernstein Analysis, Fervo S1 filing, Lazard LCOE 2025

## 3. ILLUSTRATIVE ECONOMICS: PAYING FOR SPEED VS. PAYING FOR SCALE

Bloom's installed cost runs \$3,100–4,000/kW pre-incentive, falling to roughly \$2,200–2,800/kW after the restored Section 48E investment tax credit (30%, technology-neutral, in effect through 2033). Layering in natural gas fuel cost (running \~10% above a combined-cycle plant given Bloom's \~54% electrical efficiency, close to CCGT heat rates) and a recurring stack-replacement reserve (roughly \$1,000/kW every five - seven years, about 30% of system cost), an illustrative LCOE lands in the \$82–115/MWh range — pre- vs. post-ITC. That is a real premium to grid wholesale power in most markets, and Bloom's own pitch is explicit that the value proposition is speed and reliability (up to five-nines availability), not lowest-cost energy.

Fervo's math is the mirror image. At today's \~\$7,000/kW, Cape Station's illustrative LCOE is comparable to Bloom's — roughly \$92–112/MWh — but with no fuel-price exposure and a resource that doesn't degrade. If Fervo hits its stated \$3,000/kW target, that LCOE compresses to roughly \$48–60/MWh, cheaper than Bloom's post-ITC case and competitive with new gas. Cape Station Phase I is Fervo's first commercial-scale project, and the company has to demonstrate the learning curve. Ormat's brownfield economics are directionally the cheapest of the three (existing infrastructure, no new wells), but the model doesn't scale the way Fervo's repeatable GeoBlock design is designed to.

EXHIBIT 4: Directional LCOE for Fuel Cells and EGS  
![](images/849f16d4025e17d28c4cf49d438dd78f63e677179b3ac72b48c831cecb02eb61.jpg)  
Source: Bernstein Analysis, Lazard LCOE 2025

## 4. WHO ACTUALLY WINS THE QUEUE-BYPASS RACE?

Short-run (2026–2028 delivery): Bloom. The gap between a 90-day BTM deployment and a 3–4-year FTM interconnection wait for even the most privileged data center projects in PJM and ERCOT is the whole story. Hyperscalers with near-term capacity gaps — Oracle's Project Jupiter is the clearest example — have no substitute for BTM at this horizon, and AEP's willingness to underwrite Bloom capacity as a utility-financed BYOG asset suggests utilities themselves are starting to view onsite generation as a capacity-planning tool rather than a customer workaround.

Medium-run (2028–2033 delivery): If Fervo can demonstrate EGS at scale at \$3,000/KW, FTM geothermal becomes both cheaper than BTM fuel cells and free of fuel-price risk, which should pull incremental hyperscaler capital toward Fervo on any deal with a delivery date past 2028 — provided the interconnection queue for that specific project clears on schedule, which is the load-bearing assumption Google's Nevada 115 MW deal (targeting 2030) and the broader Google GFA are making. Ormat's brownfield model wins on risk-adjusted terms but is structurally capped by how many uprate-able geothermal assets actually exist near data center clusters — in our view, it is a scarce, not a scalable, source of supply.

Structural risk to the entire BTM premium: interconnection reform is a real, funded policy priority — PJM's fast-track cycles, FERC Order 2023 cluster studies, and ERCOT's Batch Zero process are all explicitly aimed at cutting queue times. If any of these reforms bite meaningfully before 2030, the speed premium that justifies Bloom's \$82–115/MWh over FTM alternatives narrows, and premium should flow toward whichever FTM name has the better underlying cost curve — which, on current disclosures, points to Fervo if it executes.

## 5. RISK AND CATALYSTS

<table><tr><td>Risk</td><td>Detail</td><td>Why it matters</td></tr><tr><td>Bloom&#x27;s gas-price and 45V exposure</td><td>BTM LCOE is directly geared to natural gas prices; hydrogen fuel-flexibility optionality depends on 45V credit economics that remain a smaller, less certain lever than the 48E ITC.</td><td>A sustained rise in gas prices would erode Bloom&#x27;s cost advantage relative to grid power in exactly the markets where hyperscalers have the most FTM alternatives.</td></tr><tr><td>Fervo&#x27;s journey ahead</td><td>Cape Station Phase I is Fervo&#x27;s first commercial-scale project; the $3,000/kW target is a company target that needs to be achieved when EGS gets to scale</td><td>If Fervo&#x27;s cost curve stall, the medium-run &quot;FTM wins&quot; case for geothermal weakens and BTM&#x27;s premium continues.</td></tr><tr><td>Interconnection reform pace</td><td>PJM fast-track, FERC Order 2023, and ERCOT Batch Zero are all designed to cut queue times but are early in implementation.</td><td>Faster-than-expected reform compresses BTM&#x27;s speed premium; slower-than-expected reform extends Bloom&#x27;s runway and the case for further utility BYOG deals.</td></tr><tr><td>48E ITC and tax-credit transferability</td><td>Bloom&#x27;s post-ITC economics depend on continued 48E availability and monetization mechanics (direct pay, transferability) remaining intact.</td><td>Any legislative or IRS-guidance change to 48E treatment would move Bloom&#x27;s illustrative LCOE back toward the pre-incentive end of the range.</td></tr></table>

## BOTTOM LINE

BE, FRVO, and ORA are not really competing in the same race. Bloom is selling speed and is priced accordingly; Ormat is selling low-risk incrementalism on a resource base that we don't believe lends itself to scale (unless they crack the EGS puzzle); Fervo is the only one of the three underwriting a cost-curve bet, and it is the name most exposed to execution risk and most rewarded if that bet pays off. For a coverage universe organized around "who wins the interconnection bypass," the honest answer is that Bloom wins today, Fervo wins the argument if Cape Station's cost curve proves out by 2028, and Ormat wins on risk-adjusted return without ever needing to be the largest name in the room. We'd treat Fervo's Phase I commissioning (Q4 2026 target) and any updated cost disclosure toward its \$3,000/kW target as the single highest-signal near-term catalyst for the FTM side of this framework.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted 

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
