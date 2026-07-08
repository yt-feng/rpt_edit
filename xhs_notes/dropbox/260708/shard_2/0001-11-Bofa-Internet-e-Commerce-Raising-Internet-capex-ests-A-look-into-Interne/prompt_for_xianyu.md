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
# Internet/e-Commerce

# Raising Internet capex ests: A look into Internet capex, capacity and monetization

Industry Overview

## AI capex returns remain the top hyperscaler debate

The biggest debate for the Internet hyperscaler stocks remains the return profile on AI capex spend, while biggest concern in 2Q results is that higher capex (and lower FCF ests.) will overshadow strong revs. In our view, this concern has outweighed recent positive cloud pricing (Amazon) and capacity monetization data points. In this report, we raise our capex estimates, translate capex into estimated data center GW capacity, and review monetization estimates on that capacity. We also conduct an internet hyperscaler valuation analysis & list potential catalysts that could improve hyperscaler sentiment.

## Raising capex estimates as hyperscalers prioritize capacity

Given the recent capital raise by Alphabet, reported server order increases by Amazon, LLM capacity use comments from Meta, and higher memory costs, we are raising our sector capex estimates. For Alphabet, we now expect Capex of \$195bn in 2026 (vs \$187bn previously), \$290bn in 2027 (vs \$257bn). For Meta, we expect Capex of \$145bn in 2026 (vs \$130bn previously) and \$185bn in 2027 (vs \$157bn). For Amazon AWS (excludes retail), we expect Capex of \$159bn in 2026 (unchanged), \$230bn in 2027 (vs \$196bn). (We will adjust our ests for related revenues & depreciation as additional June advertising and Cloud data points come in.)

## Sizing hyperscaler data center GW capacity through 2030

We est. capacity by triangulating capex results and outlooks, Amazon's GW disclosures, and industry estimates on costs to build data center capacity. We estimate the Big-3 Internet mega caps had \~27GW capacity exiting 2025, which will grow to 39GW in 2026 and 57GW in 2027. We estimate Amazon will add the most capacity in 2026-2027 at 15GW, followed by Google at 9GW and Meta at \~6GW, with Amazon's capacity additions at a lower cost than peers (at around \$24bn in AWS capex per GW per 2025 disclosures).

## Recent capacity deals suggest growing capacity value

Assuming 70% of Amazon's AWS capacity is used for Cloud (vs 30% for core), we estimate AWS revenue per GW of capacity at \$10.6bn in 2026, with Google Cloud at \$15.7bn. These revenues/GW are well below recent capacity deals by Anthropic and Google with SpaceX at up to \$50bn per GW (for specialized AI capacity), which give us optimism on future capacity related revenue upside. For Meta, we estimate the company could have up to \~23GW of capacity by 2030, and if 40% is available for AI enterprise sales, we estimate a \$110bn potential enterprise opportunity (assuming \$12bn/GW).

## Internet hyperscaler valuation analysis

For our valuation analysis, we back out est. valuations for core advertising and retail revenues (at 12-15x implied P/Es) and look at valuations imbedded in hyperscaler stocks per unit of GW capacity. While our analysis is subject to numerous assumptions & excludes the impact of projects like Leo and Reality Labs., we think our analysis identifies the limited implied value the Street is giving to Meta's capacity build. Our analysis suggests an implied value for Google at \$110bn per 2028 Cloud GW (assuming 70% of capacity for Cloud), Amazon at \$59bn per AWS GW, and Meta at \$4bn per AI GW. We note that Meta is the major beneficiary with proof points on capacity revenue levers. See our other conclusions on the next page.

## 07 July 2026

Equity
United States

Justin Post
Research Analyst
BofAS
+1 415 676 3547
justin.post@bofa.com

## Nitin Bansal, CFA

Research Analyst

BofAS

+1 415 676 3551

nbansal7@bofa.com

AI: Artificial Intelligence

FCF: Free Cash Flow

GW: Gigawatt

API: Application Programming Interface

MTIA: Meta Training and Inference Accelerator

TAM: Total Addressable Market

LLM: Large Language Model

## Introduction

We think the biggest debate for the Internet hyperscaler stocks, in our view, remains the return profile on AI capex spend. The elevated capex spend has increased hyperscalers fixed costs, lowered competitive differentiation and increased long-term margin risk. While risk of incremental near-term FCF pressure is increasing, there have been recent positive cloud pricing (Amazon), capacity leasing (Anthropic deal with SpaceX) and LLM data points (Meta improvements with Watermelon) that suggest strong monetization potential. However, despite strong and accelerating Cloud sector revenue growth, Amazon and Meta P/E valuations are well below historical averages, and Google has underperformed since announcing a capital raise on June 3 $^{rd}$ , suggesting investors remain skeptical on AI capex spend ROIs.

In this report, we update our capex estimates, translate capex into implied installed GW data center capacity, and estimate the potential monetization value of that capacity through a revenue-per-GW analysis. We also analyze for Internet hyperscaler capacity, and potential catalysts that could drive stock multiple expansion.

Our key conclusions:

\- Amazon will add most capacity in 2026-2027 and therefore has potential for most capacity driven incremental revenue growth in the group. We estimate Amazon will add 15GW of capacity over the 2-year period, followed by Google at 9GW and Meta at \~6GW. Reiterate Buy on Amazon.

We estimate that Amazon will have the lowest cost per incremental GW of capacity. We estimate Amazon capacity additions at \$25bn/GW in 2026 vs Google at \$37bn/GW and Meta at \$45bn/GW, which reflects AWS's scale advantage, use of internal chips, and more balanced mix of core cloud workloads (vs AI). Higher costs at Google and Meta in 2026 partially reflect additional upfront facilities spend (vs chips), more specialized AI capacity (GPUs vs CPUs).

\- Google has higher revenue per GW of estimated AI / Cloud capacity, which is due to its premium cloud mix and differentiated AI infrastructure anchored by TPUs. However, with estimated 2026 AWS revenue per AWS GW at roughly \$10bn versus Alphabet Cloud at \$16bn, there is potential upside to our AWS revenue estimates as AI workloads grow as a percent of total.

\- There is significant upside potential to our Cloud revenue estimates based on recent capacity deals. We estimate annual Cloud revenues per GW of capacity for Amazon and Google ranging from \$10bn to \$17bn, well below recent capacity deals signed by Anthropic and Google with SpaceX at over \$40bn a GW (estimated). We also use a conservative \$12bn per GW in estimating Meta's enterprise revenue potential, which could have significant upside considering specialized AI capacity that Meta is building.

\- Meta is getting little to negative value on its capacity build. Even using a conservative 5x 2027 revenues on Meta's ads business (which translates to around 12x P/E assuming $50\%$ margins) and assuming a relatively high $60\%$ of capacity will be used for the core ad business, Meta's stock valuation embeds a $\$4bn/GW$ AI capacity valuation based on our capacity estimates. Reiterate Buy on Meta.

## Section 1: Raising Capex Estimates

Given the recent capital raises by Alphabet and Amazon, combined with a DigiTimes report that AWS has asked server supply chain partners to increase 3Q26 shipments, comments from Meta's management on increase capacity needs for its new LLM (Watermelon), Google's commentary emphasizing a significant step-up in capex next year, and DRAM spot pricing data that suggests pricing is up $40\%$ q/q, we are raising our capex estimates. We believe hyperscalers will prioritize capacity availability over near-term FCF optimization, as demand for AI training, inference, cloud workloads and internal AI product deployment remains supply constrained. Recent commentary supporting our outlook for higher capex:

\- In June Google indicated plans to raise \$80 in capital to fund infrastructure investment,

In early July, Meta said its next-gen AI model 'Watermelon' uses 10x more compute,

In early July, Amazon Web Services has told its server supply chain partners to raise shipment volumes for 3Q'26 (per Digitimes), and

In mid-June, per Bloomberg, Meta signed a 1.6GW capacity agreement with neo cloud provider, Crusoe

Exhibit 1: We are raising our capex estimates to reflect recent Cloud industry data points. Updated Capex Estimates for Alphabet, Meta and Amazon AWS (\$ bn)  
![](images/9a58f6ef346bd5b2110f0a2dcde8c43f482613556ef3bd63e123d95f9e35bf73.jpg)  
Source: BofA Global Research Estimates  
BofA GLOBAL RESEARCH

## Revised estimates:

\- Alphabet: We now expect Capex of \$195bn in 2026 (vs \$187bn previously), growing 49% y/y to \$290bn in 2027 (vs \$257bn previously) and 14% y/y in 2028 to \$330bn (vs \$310bn previously).

■ Meta: We now expect Capex of \$145bn in 2026 (vs \$130bn previously), growing 28% y/y to \$185bn in 2027 (vs \$157bn previously) and 14% y/y in 2028 to \$210bn (vs \$171bn previously).

\- Amazon AWS: We expect Capex of \$159bn in 2026 (unchanged), growing 44% y/y to \$230bn in 2027 (vs \$196bn previously) and 20% y/y in 2028 to \$276bn (vs \$221bn previously).

Note: Our updated Alphabet, Amazon and Meta models just reflect revisions to our capex estimates only. We will incorporate the associated impact on depreciation, EPS, FCF and other financial metrics as we receive June revenue data points.

## Section 2: Estimating installed GW Capacity

Using our capex estimates, we estimate historical and future installed GW data center capacity for Alphabet, Meta and Amazon AWS. Our analysis uses company-level capex as the starting point, then applies an estimated cost to build and equip AI-oriented data center capacity. While the exercise is high-level given limited company-level disclosures, we believe it helps in sizing the scale of hyperscaler infrastructure deployment and the potential monetizable compute base. Our key assumptions include:

## Cost to Build a GW of Capacity

We estimate that in 2026, the cost to build 1GW of data center capacity is \$25bn to \$45bn, inclusive of the major infrastructure and compute components. The range reflects differences in accelerator mix, rack density, power redundancy, cooling architecture, land and construction costs, and whether the capacity is optimized for training, inference or mixed workloads. We think capex cost per GW could be elevated for Meta and Google in 2026 as land and construction costs are elevated ahead of chip deployment, and capacity is more specialized for AI workloads than various Cloud competitors. Future offsets could include improving chip performance, use of proprietary chips, and rapid growth in memory and other supply availability.

Using data from multiple secondary sources, we estimate that the largest component of AI data center build cost is AI servers and GPUs, which account for roughly 55% to 60% of total cost. This reflects the high cost of accelerators, server systems and related compute hardware required to support training and inference workloads. Power infrastructure is the next largest cost category at approximately 12% to 18%, including substations, transformers, switchgear, backup generation and power distribution equipment needed to support dense AI workloads. Networking represents another 8% to 12% of total cost, driven by high-performance interconnects, switches and optical networking required to link large GPU or TPU clusters. Beyond compute and power, we estimate building, land and site work account for roughly 8% to 12% of total cost, including land acquisition, shell construction, site preparation and related civil work. Cooling and mechanical systems represent approximately 6% to 10%, and other costs and contingency account for \~3% to 5%.

Exhibit 2: We estimate \$25bn to \$45bn to build 1GW of AI data center capacity
Cost Build-up of 1GW Capacity Data center (\$ bn)

<table><tr><td>Capex bucket</td><td>Approx. % of total</td><td>Lower ($ bn)</td><td>Higher ($ bn)</td><td>What it includes</td></tr><tr><td>AI servers / GPUs</td><td>55%-60%</td><td>$14</td><td>$28</td><td>GPU servers, CPUs, memory, storage inside servers</td></tr><tr><td>Networking</td><td>8%-12%</td><td>$2</td><td>$5</td><td>Switches, optical modules, NICs, cables, back-end GPU networking</td></tr><tr><td>Power infrastructure</td><td>12%-18%</td><td>$3</td><td>$8</td><td>Substations, transformers, switchgear, UPS, PDUs, backup generation</td></tr><tr><td>Cooling / mechanical systems</td><td>6%-10%</td><td>$2</td><td>$5</td><td>Liquid cooling, chillers, cooling distribution, heat rejection</td></tr><tr><td>Building / land / site work</td><td>8%-12%</td><td>$2</td><td>$5</td><td>Land, shell, security, physical construction, permitting</td></tr><tr><td>Other / contingency</td><td>3%-5%</td><td>$1</td><td>$2</td><td>Design, engineering, commissioning, spares, buffers</td></tr><tr><td>Total</td><td>100%</td><td>$25</td><td>$45</td><td>1GW AI data center</td></tr></table>

Source: BofA Global Research Estimates, Epoch AI, JLL

BofA GLOBAL RESEARCH

Company specific assumptions: Google and Amazon custom silicon Advantage
For company-specific assumptions, we use a 2026 cost per GW of \~\$45bn for Meta, \$37bn for Alphabet and \$25bn Amazon. For Amazon, we can triangulate cost per GW based on Amazon's capex and 2-year GW capacity growth outlook. The higher Meta assumption reflects greater upfront costs for data center land/building (ahead of GPU deployment) and reliance on external GPU infrastructure. For Alphabet and Amazon, we assume lower cost per GW to reflect custom silicon usage, particularly the ability to use internally developed TPUs and Trainium/Graviton chips, which we believe can lower effective compute cost versus a more GPU-heavy architecture.

## Alphabet Installed Capacity Estimates

We estimate Alphabet had 5.5W of capacity in 2025, which will increase $62\%$ y/y to 8.9GW in 2026 and $66\%$ y/y to 14.7GW in 2027. By 2030, we project Alphabet's installed capacity to reach 32.4GW.

Exhibit 3: We estimate Alphabet capacity will grow to 15GW by 2027 Estimated Alphabet Installed Data Center Capacity (GW)  
![](images/c7c50f7ca722ae65d7c445e689aa305d39b371dd18b3af898e3cfc46f5f157e1.jpg)  
Source: BofA Global Research Estimates  
BofA GLOBAL RESEARCH

We est. Alphabet's capex of \$195bn in 2026 and \$290bn in 2027. Assuming share of capex directed towards Cloud business and AI data centers increases from 45% in 2024, to 60% in 2025 and 70% by 2030 and avg. cost to add 1GW of capacity increases from \~\$31bn in 2024 to \~\$46bn by 2030, we estimate Alphabet's capacity will increase from \~8.9GW in 2026 to 32.4GW by 2030. The increase in cost per GW in 2026, followed by a decline in 2027, reflects timing dynamics in the capacity buildout (physical infrastructure before chips are deployed). We expect revenue per GW to fall in 2027 to reflect timing of capacity deployment, and then increase again in 2028.

Exhibit 4: We estimate Alphabet's capacity will increase from \~8.9GW in 2026 to \~32.4GW by 2030
Alphabet's Capex and Commissioned capacity estimates by year

<table><tr><td></td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Existing Capacity</td><td>3.0</td><td>3.8</td><td>5.5</td><td>8.9</td><td>14.7</td><td>20.7</td><td>26.6</td></tr><tr><td>GW Addition</td><td>0.8</td><td>1.7</td><td>3.4</td><td>5.8</td><td>6.0</td><td>5.9</td><td>5.8</td></tr><tr><td>Total Capacity</td><td>3.8</td><td>5.5</td><td>8.9</td><td>14.7</td><td>20.7</td><td>26.6</td><td>32.4</td></tr><tr><td>Alphabet Capex ($ bn)</td><td>$52.5</td><td>$91.4</td><td>$195.0</td><td>$290.0</td><td>$330.0</td><td>$356.4</td><td>$384.9</td></tr><tr><td>Y/Y</td><td>63%</td><td>74%</td><td>113%</td><td>49%</td><td>14%</td><td>8%</td><td>8%</td></tr><tr><td>% for Cloud</td

[中间内容因长度限制已省略]

the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
