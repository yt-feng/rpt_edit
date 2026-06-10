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
## SNEC 2026 Day 1 Conference Feedback

In the day 1 of JEF SNEC 2026 trip, we met Huawei ESS expert, SMM expert, Envision expert, mgmt from Sigenergy, DQ, JKS, Sungrow. Key takeaways below:

Huawei ESS expert (Carvin Cao, Product Director, Huawei Digital Power). 1) Expert expects global ESS installation to exceed 150GWh in 2026, +80% YoY, with 20-30% annual growth projected post-2026. China leads with 60% global share. 2) Annual global residential ESS shipment is expected to grow by 14% YoY to 30GWh in 2026 (EU acc for around 50%). Key Resi ESS growth driver in EU mkt, expected to grow by 30% YoY in 2026, incl upgrades to larger ESS systems, rapid expansion of balcony ESS, etc. 3) Annual C&I ESS installation is expected to grow by 66% YoY to 32GWh in 2026 (China acct for 60% of total). Key growth drivers incl rapid expansion of AIDC in US, zero-carbon parks in China, etc. 4) Despite subsidy policy in Australia going to fade out, expert expects residential ESS installation in the mkt to grow by 20% YoY in 2026/27.

SMM expert (Henry Shi, Chief Analyst of Shanghai Nonferrous Network Photovoltaic). 1) The long-awaited industry reform is still in progress with production costs verification, and is expected to launch in August-September 2025. It will adopt a comprehensive approach combining energy consumption supervision, quality standards and price guidance but expert sees a gradual execution pace. Expert expects bankruptcy of major players as unlikely and govt intention is more likely to shut down old plants among players to maintain social stability; 2) Poly supply might reach 120k-130kt/mth in August while demand is likely staying weak at c.80-90kt/mth, along with high inventory level, Poly prices might continue falling while expert sees RMB30/kg as a relative low price point as Wafer players might start re-stocking at such level; 3) Expert expects modest GPM recovery for Wafer players in Q3 with potential policy support, while module prices will not exceed 1H highs this year; 4) Expert believes BC tech outperforms TOPCon in long-term with higher potential in efficiency, but its adoption is constrained by patent barriers; 5) A critical industry risk is upstream quality degradation for cost reduction, which may trigger large-scale warranty disputes in 1-2 years; 6) Global PV installations are expected to be 432GW in 2026, incl 211/66/40GW in China/EU/US and grow to 455GW in 2027, incl 218/68/46GW in China/EU/US.

Envision expert (Chen Zong, Head of Energy Storage Sales, Envision). 1) US AIDC ESS is a core growth driver, mostly deployed alongside gas turbines/diesel generators for load shaving to reduce impact on grid, company who may develop PCS that supports system availability of $99.999\%$ , will have an edge in the business, thus companies with mature power conversion technologies like Sungrow might prevail. 2) Envision's major client Fluence is developing reference architecture for AIDC running Vera Rubin NVL72 platform. Expert expects a c.1GWh shipments might happen in 1Q27. 3) Envision restructured its US production subsidiary to attract 3rd party investors and push capacity expansion/technical upgrades in South Carolina/Tennessee. 4) SST solutions will gradually be adopted in AIDC with growing power intensity of rack, that might promote demand for PCS if product specification is up to the standard and might replace UPS. 5) Currently, ESS installed by AIDC developers are mainly aiming to mitigate the impact of AIDC's high load volatility to grid for grid connection, thus ESS systems with $30\%$ of capacity with 2-4 hour would be sufficient, off-grid ESS installation will likely need much more.

Continued overleaf...

6) China ESS installation is expected at c.300GWh this year. Expect expects grid related ESS buildouts to be mostly completed in 1-2yrs. Installations after that will rely on integrated data center + RE + ESS projects.

Sigenergy (6656 HK, NC). Key takeaways include: 1) Australia remains a key market in 2026. Despite subsidy phase-down since May'26, demand remained robust in Jun/Jul and Mgmt expects Australian mkt will still grow to c.8-10GWh. 2) Residential ESS demand in EU is expected to grow by $20 - 30\%$ YoY. Mgmt guides EU to contribute revenue of RMB6-7bn in the year. 3) Sigenergy takes c.20-30% of mkt share in South Africa, from which revenue will acct for $6 - 7\%$ in 2026. Japan is expected to contribute annual revenue of USD100mn in 2026, with high margins vs other regions due to less competition with stricter certification requirements. 4) The budget-friendly Sigenstor Neo product with optimized features, will start delivery in 3Q26, targeting price-sensitive markets like Southeast Asia and Africa, with GPM targeting at $40\%+$ . 5) The company maintains a premium positioning with $20 - 30\%$ price premiums over peers, avoiding direct price competition and promoting AI integration across residential and utility energy management systems to deliver value to clients. 6) Mgmt guides a robust $60\%$ QoQ growth in 2Q26 revenue, excluding revenue from utility ESS shipment recorded in 1Q.

DQ New Energy (DQ US, BUY). Key takeaways include: 1) Execution of Price Law which prohibited selling below production costs remained muted, as the process of production costs verification under 3rd party review is still ongoing. Mgmt is still uncertain on whether Price Law will be enforced eventually, and expects poly prices to increase to RMB 40+/kg with implementation or stay at RMB 30-35/kg if authority is not enforcing it afterall. 2) DQ maintains 50% UTR, accumulating a record-high 60k-ton inventory so far. Industry poly invty reaches c.400-550kt, with 300-400/100-150kt in poly/wafer players. Mgmt expects 20-30% sequential demand growth in 2H to drive destocking. 3) Daqo's cash cost stands at RMB30-32/kg with full production cost near RMB40/kg. 4) Daqo plans to expand into solid state transformer, switch and ESS sector to target the AIDC market, with first-generation prototypes completed and early customer discussions underway. 5) The company has around 35,000 tons of outdated capacity built before 2019, which might be gradually shut down in the next 2-3 years. 6) Its semiconductor-grade poly remains in small-batch trial production with ongoing process optimization.

Jinko Solar (JKS US, BUY). Key takeaways include: 1) JinkoSolar maintains active talks with US partner on cooperation in both space and terrestrial solar. Terrestrial collaboration progresses well, and the company plans to build up a team to be responsible for it. As for space solar, JKS is developing thinner TOPCon products to reduce weight and plans to do on-orbit verification in 1H26. 2) The company targets 3Q26 profit to turn +ve, driven by ramp-up of high-efficiency module (70GW production capacity) after upgrades in 1H26 with price premium of USD1c/W, along with silver-coated copper paste adoption that reduce costs by c.RMB0.03/W. 3) Full-year module shipments are guided at 75-85GW with profit prioritization over market share. 4) ESS is a strategic growth driver, JKS is targeting 15GWh shipments (10GWh recognized revenue) in 2026 with $80\%$ from overseas market. JKS's ESS shipment is expected to maintain high growth in next 2-3 years. 5) Mgmt guides ESS GPM in NA/EU/Latin America at $30+ / 20 / 15\%$ . 6) Southeast Asian solar production capacity runs at high utilization as it is still supplying EU mkt. The Saudi project is now delayed with policy uncertainty.

Sungrow (300274 CH, BUY). Key takeaways include: 1) Mgmt explained significant decline in 4Q25 GPM was mainly due to revenue recognition of a large project in Latin America with very low GPM. LiC price hikes are still hurting margins on legacy orders. Cost pass-through situation varies in different regions, depending on competitive landscape, while Sungrow is maintaining c.10% price premium vs. peers. 2) Sungrow shipped 4GWh of C&I and residential ESS and records revenue of c.RMB8-10bn in 2025. Mgmt guides NPM for residential ESS of c. 20%. The company is focusing more on C&I and residential ESS in 2026 with 40-50% GPM which might partially offset pressure on utility-scale ESS. 3) The solid-state transformer (SST) product (incl 10kV to 800V, 800V to 50V products) will launch in 2H26 with immediately sales. Sungrow's full-stack in-house R&D capability is industry-leading with many other players are procuring components from supply chain. This supports customized product requirement for hyperscalers like Amazon and Google. 4) US AIDC ESS demand is set to double to 10GWh in 2026 and grow further to 70-80GWh in 2030 to resolve issues including grid capability, power quality, load smoothing and shaving. 5) Mgmt thinks sodium battery has comparative advantages vs. lithium battery on high power rating and high C-rating charging/discharging. Battery cycle life is now improved to 10,000 times as well, while its better tolerance to extreme temperatures might lead to savings in liquid-cooling. The primary constraint to mass adoption now is still relatively expensive costs. 6) Co sees mkt expectation of China's ESS installation at 300GWh aggressive, and installation may normalize in 2027 as well after rush installation in 2026. Overseas market demand is expected to maintain 40-50% YoY growth in 2027.

We would like to thank Wade Wu, employee of Evalueserve Inc., for providing research support services to our preparation of this report.

## Company Valuation/Risks

## Alphabet, Inc.

Our \$445 PT is based on 20x EV/EBITDA our forward NTM estimates, which is above the 12.5x 10-year historical average given its superior fundamentals relative to peers. Risks include impact from macro, regulatory overhang, margin pressure from ongoing investments, and impacts from shift toward generative AI, mobile, in-app, and voice-to-core search.

## Amazon.com, Inc

Valuation: Our \$320 PT is based on \~14.7x 2027E EV/EBITDA. Risks: Ongoing need to invest keeps a lid on margin expansion; regulatory pressure leads to increasing costs; macroeconomic headwinds cause top-line growth to slow.

## DAQO New Energy

We value DQ based on 0.5x FY26E PBR (net cash per share level), which gives us a PT of US\$31.87. We assume poly prices normalize at RMB65/kg level. Risks include lower-than-expected utilization rates downstream and solar installation below expectations.

## JinkoSolar Holding Co., Ltd.

We apply a 10x FY28E PE to arrive at our PT of USD32.61. This is assuming normalized NPM and discounted at a $10\%$ discount rate for 2 year. Risks include unfavorable business conditions for ADRs listed on the NYSE, higher-than-expected upstream prices, lower-than-expected solar installations, and unexpected trade barriers affecting overseas sales.

## Sungrow Power Supply Co Ltd

We are using SOTP valuation, applying PER of 20 x FY2027 EPS + discounting market cap of Sungrow's AIDC ESS and power supply (incl SST) in 2030 of RMB162bn by 3 years, to get the company TP of RMB236.35 per share. Risks include lower-than-expected solar installations and lower-than-expected growth in energy storage system.

## Analyst Certification:

I, Alan Lau, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

Registration of non-US analysts: Alan Lau is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst. As is the case with all JEF employees, the analyst(s) responsible for the coverage of the financial instruments discussed in this report receives compensation based in part on the overall performance of the firm, including investment banking income. We seek to update our research as appropriate, but various regulations may prevent us from doing so. Aside from certain industry reports published on a periodic basis, the large majority of reports are published at irregular intervals as appropriate in the analyst's judgement.

## Investment Recommendation Record

## (Article 3(1)e and Article 7 of MAR)

Recommendation Published

June 8, 2026 13:26 P.M.

Recommendation Distributed

June 8, 2026 13:26 P.M.

## Company Specific Disclosures

Rayyan Matraji owns shares of Amazon.com common stock.

## Explanation of JEF Ratings

Buy - Describes securities that we expect to provide a total return (price appreciation plus yield) of $15\%$ or more within a 12-month period.

Hold - Describes securities that we expect to provide a total return (price appreciation plus yield) of plus $15\%$ or minus $10\%$ within a 12-month period.

Underperform - Describes securities that we expect to provide a total return (price appreciation plus yield) of minus 10% or less within a 12-month period. The expected total return (price appreciation plus yield) for Buy rated securities with an average security price consistently below \$10 is 20% or more within a 12-month period as these companies are typically more volatile than the overall stock market. For Hold rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is plus or minus 20% within a 12-month period. For Underperform rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is minus 20% or less within a 12-month period.

NR - The investment rating and price target have been temporarily suspended. Such suspensions are in compliance with applicable regulations and/or JEF policies.

CS - Coverage Suspended. JEF has suspended coverage of this company.

NC - Not covered. JEF does not cover this company.

Restricted - Describes issuers where, in conjunction with JEF engagement in certain transactions, company policy or applicable securities regulations prohibit certain types of communications, including investment recommendations.

Monitor - Describes securities whose company fundamentals and financials are being monitored, and for which no financial projections or opinions on the investment merits of the company are provided.

## Valuation Methodology

JEF' methodology for assigning ratings may include the following: market capitalization, maturity, growth/value, volatility and expected total return over the next 12 months. The price targets are based on several methodologies, which may include, but are not restricted to, analyses of market risk, growth rate, revenue stream, discounted cash flow (DCF), EBITDA, EPS, cash flow (CF), free cash flow (FCF), EV/EBITDA, P/E, PE/growth, P/CF, P/FCF, premium (discount)/average group EV/EBITDA, premium (discount)/average group P/E, sum of the parts, net asset value, dividend returns, and return on equity (ROE) over the next 12 months.

## JEF Franchise Picks

JEF Franchise Picks include stock selections from among the best stock ideas from our equity analysts over a 12 month period. Stock selection is based on fundamental analysis and may take into account other factors such as analyst conviction, differentiated analysis, a favorable risk/reward ratio and investment themes that JEF analysts are recommending. JEF Franchise Picks will include only Buy rated stocks and the number can vary depending on analyst recommendations for inclusion. Stocks will be added as new opportunities arise and removed when the reason for inclusion 

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
