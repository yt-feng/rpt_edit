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
POWERING UP EUROPE

# Who pays for Electrification and Artificial Intelligence?

We explore the cost of electrifying Europe and of rolling out datacenters to support artificial intelligence. Our analysis suggests that electricity bill increases over the coming ten years will be much lower than anticipated, averaging 2-4% pa. This should ease concerns over affordability-driven regulatory intervention and strongly corroborates our thesis of an “earnings super cycle” in Utilities and ongoing multiple expansion.

Even with electrification and AI, power bill growth would be just 2-4% pa. Over the past ten years, power bills for a typical European household have increased by +5% pa. Over the coming ten years, we estimate that electricity bills will increase at a slower pace, despite accelerating electrification and rising AI adoption. Our base case (EU targets largely missed, slow DC roll-out) implies +2% annual growth in bills, while our hyper-adoption scenario for electrification and datacenters increases this to +4% pa. These figures are significantly below prevailing expectations and reflect two common misconceptions about capex and power demand.

North vs South divide. We estimate that annual electricity bill increases could reach the mid-to-high single digits in the UK and Germany, driven primarily by rising grid fees, although Germany may be better positioned to mitigate the impact through fiscal support. In Italy and Spain, we forecast largely unchanged power bills until 2035, supported by more modest grid-fee growth and normalizing power prices.

About 35-40% of electrification capex is non-inflationary or deflationary. We estimate c.35-40% of investments in the power system over the coming ten years (€2.2-3.5 trn on our two scenarios) will be non-inflationary (eg power grids' maintenance) or deflationary (eg onshore renewable additions, as seen in Spain).

Power demand growth should reduce unit fixed costs. Rising power consumption from new sources – EVs, heat pumps, industrial electric boilers, aircon, datacenters – should spread fixed costs (eg grid fees) over a larger base, thereby reducing unit costs. In our base case, we forecast power demand growth of c.1.5-2.5% pa until 2030, accelerating to c.3-3.5% thereafter. Our hyper-adoption scenario (EU goals being met, higher AI Agents penetration) implies 4.5-5% growth from 2030.

Household energy spending could fall by -30%. We estimate electrifying a typical household could lead to c.30% savings in fuel costs – equivalent to an annual reduction in energy costs of €1,200 per family. Given these benefits, policymakers may seek to encourage switching to help alleviate the burden of upfront costs.

## Alberto Gandolfi

+39(02)8022-0157 |
alberto.gandolfi@gs.com
GS Bank Europe SE - Milan branch

Mafalda Pombeiro
+44(20)7552-9425 |
mafalda.pombeiro@gs.com
GS International

## Ajay Patel

+44(20)7552-1168 | ajay.patel@gs.com
GS International

## Dhwani Khenwar

+1(332)245-7724 | dhwani.khenwar@gs.com GS India SPL

## Lawrence Lavizani

+44(20)7051-1060 | lawrence.lavizani@gs.com GS International

## Table of Contents

Executive Summary 3
Electrification: 2-4% growth in bills pa, much lower than anticipated 9
Electrification capex: c.35-40% is non-inflationary or deflationary 13
Power demand growth would lower unit fixed costs 16
Households’ energy spending would fall 19
Europe spends c.€1 trn pa on fossil fuel 21
Utilities entering an “earnings super-cycle” 23
Investment thesis, valuation & key risks 26
Disclosure Appendix 34

## Executive Summary

Many investors worry that the scale of infrastructure investment required for electrification (€2.2-3.5 trn over the next decade on our estimates) could create affordability challenges, ultimately derailing our organic growth/earnings super-cycle re-rating thesis for the sector. Our analysis, based on both a base-case and a hyper-adoption scenario for electrification and datacentres, suggests these concerns are overstated. On these two scenarios, we estimate electricity bill increases over the coming ten years will average between +2% and +4% pa, respectively. These figures are significantly below prevailing expectations, and also lower than the +5% annual increase in electricity bills, experienced by European consumers over the past ten years. As a result, we believe the electrification process is likely to prove much more manageable from both a social and economic perspective than many investors anticipate. Two factors underpin this seemingly counter-intuitive conclusion: (1) not all capex is inflationary: c.35-40% of the electrification investments that we project are non-inflationary (eg maintenance of power grids) or deflationary (eg onshore renewable additions), and (2) power consumption growth from new sources would lower unit fixed costs, such as grid fees. In our view, these findings strongly support our thesis of an “earnings super cycle” in Utilities and ongoing multiple expansion.

## Even with electrification and AI, power bill growth would be well below prevailing perceptions

Over the past ten years, power bills for a typical European household have increased by +5% pa. Over the coming ten years, we estimate that electricity bills will increase at a slower pace, despite accelerating electrification and rising AI adoption. Our base case (EU targets largely missed, slow DC roll-out) implies +2% annual growth in bills, while our hyper-adoption scenario for electrification (EU targets met) and datacenters (higher penetration rate of AI Agents) increases this to +4% pa. These figures are significantly below prevailing expectations and reflect two common misconceptions about capex and power demand.

## Exhibit 1: We expect European electricity bills to grow at a +2% CAGR to 2035 (base case), or at +4% in a hyper-adoption scenario

EU-27 + UK electricity bills evolution under different scenarios, 2026E-35E (€/MWh, average retail and industrial)

![](images/397bf79b6d8e94ae1bea30f7fe5256070edfd1c8ab478eb913072a0aad4d2a57.jpg)  
Source: GS Global Investment Research

## North vs South divide: meaningful regional differences

Our estimates suggest that annual electricity bill increases in the UK and Germany could reach mid-to-high single digit, primarily driven by greater investments in power grids vs the rest of Europe. The situation might potentially be more manageable in Germany given the likely ability to fiscally support consumers. In Italy and Spain, we forecast largely unchanged power bills until 2035 owing to a more muted evolution in grid fees and the likely normalization in power prices.

## Exhibit 2: Germany and the UK may face the highest growth in electricity bills owing to rising grid fees

Unit electricity bills 2026E-35E CAGR in GSe base case, breakdown by country (%, average retail and industrial)

![](images/7c4e8bd0de3b559c7268cf62378a2dc979fd8f09f1cb44cb4367b804046e9d8a.jpg)  
Source: GS Global Investment Research

About 35-40% of electrification capex is non-inflationary or deflationary
We estimate c.35-40% of the electrification capex that we project over the coming ten years (€2.2-3.5 trn on our two scenarios) will be non-inflationary (eg power grids' maintenance) or deflationary (eg onshore renewable additions, as seen in Spain).

Exhibit 3: We expect 35-40% of electrification capex to be non-inflationary or deflationary EU power sector 10-year cumulative capex, breakdown by impact on inflation (€ trn)

![](images/e16da77bb13f067f47a90c27947b1262469ba72bc175fe932d96fa4c93bc9db8.jpg)  
Source: GS Global Investment Research

## Power demand growth from new sources should lower unit fixed costs

Rising power consumption from new sources – EVs, heat pumps, industrial electric boilers, aircon, datacenters – should spread fixed costs (eg grid fees) across a wider base, thereby reducing unit costs. In our base case, we forecast power demand growth of c.1.5-2.5% pa until 2030, accelerating to c.3-3.5% thereafter. Our hyper-adoption scenario (EU goals being met, higher AI Agents penetration rate) implies 4.5-5% annual growth from 2030.

Exhibit 4: We see power demand growth accelerating from 1.5-2% pa to potentially 4-5% pa, depending on the pace of electrification and datacenter rollout
EU power demand evolution across different GS scenarios, 2026E-35E (percentage)

![](images/b1ec6ee4b13ff3255672db75f02709fcb0453dd8cd0d4fc0f9224e96a3356307.jpg)  
Source: GS Global Investment Research

Households' energy spending could fall by -30%: €1,200 savings pa per family
We estimate electrifying a typical household could lead to c.30% annual savings in fuel – equivalent to an annual reduction in energy costs of €1,200 per family. Essentially, running an EV or electric heating would lead to meaningful monthly savings for European households. Given these benefits, policymakers may seek to encourage switching to help alleviate the burden of upfront costs.

Exhibit 5: Despite higher electricity volumes, electrification could reduce household bills by c.30%

Household annual energy bill breakdown by source, 2026-35E (€ per year)

![](images/696d5ff3b82404a23275dbd0b31f0bef92d7987b0fc1f6932ac7a5f9313b7a65.jpg)  
Source: GS Global Investment Research

## Europe spends c.€1 trn pa on fossil fuel

Each year, Europe spends around €1 trn pa on oil and derivative products, natural gas and coal. The rising share of electricity in the primary energy mix would imply meaningful savings in fossil fuel spending, which we estimate at €100-150 bn per annum as of 2030-35.

Exhibit 6: European end-users spend €1 trn in fossil fuels per year, mostly in oil EU-27 + UK fossil fuel end-user spending in 2024, breakdown by commodity (percentage)

![](images/f1ce1e789ab93169db329316e53baa1bc52bdc496f0d67144084c5522a65ed99.jpg)

## Electrification and AI to drive a generational earnings super-cycle

A growing electricity infrastructure deficit is likely to support higher returns across Renewables and FlexGen, while driving increased investment requirements throughout the electricity value chain – including power grids. Over the coming ten years, we estimate electrification will require €2.2-3.5 trn of investments, a meaningful acceleration vs the past ten years. For the main electrification compounders, this should support high-single-digit to low-double-digit average earnings growth into the 2030s, on our estimates (see here). We see this supporting an “earnings super-cycle” for the industry extending well into the 2030s. As the investment cycle unfolds, earnings expectations are likely to move materially higher into 2030-31, thus supporting further multiple expansion. This may also weaken the sector’s correlation with cost of capital and commodity prices.

Exhibit 7: European Utilities' re-rating is underpinned by higher (and better-quality) structural earnings growth
SX6P 1-year forward PE evolution, 2019-26 (x)  
![](images/20a520d6ebc307076d4dd2b5af248f56ce37cd9627ce1b7e7b08543f9cea535e.jpg)  
\* Updated as of 13 July  
Source: Bloomberg

## Favor transformative electrification stories, renewables and energy security infrastructure providers

We favor three clusters of companies: (1) Transformative electrification stories include companies where electrification capex is set to accelerate meaningfully (Naturgy, Enel, Engie and PPC), significantly transforming these portfolios on a 3-5 year basis; (2) Renewable developers, which should benefit from rising returns and organic growth opportunities (RWE, EDPR, Solaria, Orsted). RES manufacturers that should benefit from rising orders and margins (eg Vestas and Nordex); and (3) Energy security infrastructure providers, such as Siemens Energy, EON and Snam.

## Electrification: 2-4% growth in bills pa, much lower than anticipated

Over the past ten years, the main cost items for a typical European household — housing, food and energy — have increased by +4% pa on average. Electricity bills have risen at an annual rate of +5%. Over the coming ten years, we estimate that electricity bills will increase at a slower rate of between 2% pa and 4% pa based on two scenarios: (1) our base case, which assumes a slower pace of electrification (c.40-50% below EU electrification goals) alongside a gradual datacenters roll out (lagging the US by more than five years), and (2) our hyper-adoption scenario, where we simulate faster electrification (in line with EU goals on EVs and HPs) and stronger adoption rates for AI Agents, requiring a more substantial expansion of datacenter infrastructure. This projected evolution in electricity bills is much lower than commonly perceived, and hence we believe the electrification process is likely to prove much more manageable from both a social and economic perspective than many investors anticipate. Two factors underpin this conclusion: the share of non-inflationary (eg power grids maintenance) and deflationary capex (onshore wind and solar) is higher than prevailing expectations, and power demand growth from new customers should lower unit fixed costs (eg grid fees).

Households' main cost items have been growing +4% over the past ten years
According to Eurostat, household cost inflation averaged +c.4% CAGR across the main spending categories over the past ten years (2016-25). Electricity and gas bills saw the steepest increase, at 5% and 6% CAGR, respectively, while housing costs increased more moderately at c.2% CAGR.

Exhibit 8: European household cost inflation averaged c.4% CAGR over the past ten years (+5% for power bills)
EU-27 HCPI average annual increase by category, 2016-25 (percentage)  
![](images/3e69391d7115b8428718bd3b50246d8a06106d85b967988f9bdd4e42308b063f.jpg)  
Source: Eurostat

## Electricity bills to grow 2-4% pa to 2035

Our base case power demand forecast implies slow progress on electrification and only a gradual roll-out in datacenters. More specifically, by 2030, electrification would remain c.40–50% below EU targets, and our 2031 datacentre forecast is c.15% below the EUDCA's (already conservative) expectations. Under this scenario, power demand would grow by 1.5–2.5% pa to 2030, rising to 3–3.5% thereafter until 2035 as the pace of electrification and, particularly, datacenters development picks up. We estimate that meeting this demand would require c.€2.2 trn of electrification capex over the coming ten years. Our analysis suggests that this would lead to a +2% annual increase in electricity bills over 2026–35E, for Europe. This is less than half of the annual increase experienced by households over the past ten years.

Our hyper-adoption scenario assumes a stronger pace of electrification and a faster datacenters roll-out. Specifically, we assume adoption rates broadly in line with the EU's 2030 targets for mobility and heating: c.30 mn EVs vs around 10 mn in 2026, and c.60 mn HPs vs around 30 mn in 2026. This would require an acceleration in investments across power grids and, in particular, power generation (renewables, gas plants, batteries). Under this scenario, power demand growth would reach 4.5-5% pa over 2030-35.

Exhibit 9: Our hyper-adoption scenario assumes faster electrification and datacenter build-out
Infographic

<table><tr><td></td><td>Base Case (+2%)</td><td>Hyper-adoption (+4%)</td></tr><tr><td>Datacenters</td><td>c.60 GW capacity by 203520-30% share of Agentic AI queries by 2035</td><td>c.80 GW capacity by 203535% share of Agentic AI queries by 2035</td></tr><tr><td>Electric Vehicles</td><td>35% of new EV sales by 2030</td><td>55% of new EV sales by 2030 (EU target)</td></tr><tr><td>Heat Pumps</td><td>Half of the 2030 EU target (30 mn)</td><td>100% of the 2030 EU target (60 mn)</td></tr></table>

Source: GS Global Investment Research

Under our hyper-adoption scenario, electricity bills would grow by +4% CAGR over the coming ten years, we

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
