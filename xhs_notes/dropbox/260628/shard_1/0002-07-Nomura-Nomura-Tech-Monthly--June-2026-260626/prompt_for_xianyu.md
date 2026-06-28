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
EQUITY: JAPAN ELECTRONICS

Sector view

Strengthening FDE capabilities to spur uptake of physical AI

Lead times lengthening even for analog products owing to rising demand from data centers

Advances in AI models continue to outpace system deployment, but even so major IT companies and private equity funds have been strengthening their forward deployed engineering (FDE) capabilities to spur uptake of AI agents. Japanese IT majors are targeting profit growth of over 15% on a CAGR basis in their medium-term business plans, and we see prospects for faster profit growth via increased uptake of AI agents. We think AI represents substantial business opportunities rather than a threat. Shipments of servers and networking equipment for AI have also been rising sharply as companies increase their supply capacity, and demand for conventional servers has been increasing substantially too. The increase in demand has caused supply-demand conditions to tighten, first for GPUs and HBM during the AI learning phase, spreading to ASICs and SSDs during the inference phase, and now to CPUs, analog semiconductors, and MLCCs in the AI agent phase.

## Memory prices: NAND contract price momentum remains strong

Commodity DRAM prices were solid in May, with the end-May spot price for DDR5 DRAM up 3.1% m-m at \$26.3/GB and the contract price up +2.0% at \$12.8/GB. The spot price of 512Gb TLC NAND remained high in May at \$0.36/GB (flat m-m). Monthly data from Taiwanese memory module manufacturer Adata suggests that NAND prices may have been rising faster than DRAM prices of late. Since the start of June, share prices of memory-related stocks have been negatively affected by news reports about a letter sent to the White House by memory customers and Nvidia's plan to halve LPDDR5X capacity per rack for its next-generation Vera Rubin systems. However, we do not see any signs of a slowdown in demand for these products, and if anything see evidence of ongoing structural supply shortages, on which basis we think a share price correction would represent a good entry point.

Special feature (Vol. 91): FDEs contributing to speedier deployment of AI agents

FDEs have been attracting attention of late. AI companies station FDEs at customer premises to oversee deployment of proprietary AI agents. When generative AI first appeared, prompt engineers were the focus of attention. With the growing uptake of AI agents, though, customers' needs have changed and FDEs are in demand. FDEs embedded at client companies communicate directly with clients about the challenges they face, moving swiftly to address those challenges and expedite AI deployment. AI companies then take the expertise thus gleaned and integrate it into their products, facilitating lateral expansion of service offerings. Hitachi plans to bolster its Physical AI FDE Team to facilitate integration of its IT technology (AI technology, security, and data infrastructure) and OT (operational technology: domain expertise). Fujitsu similarly plans to bolster its team of FDEs with specialist knowledge of its proprietary Takane AI model and Kozuchi AI platform.

## Research Analysts

Masaya Yamasaki, CFA - NSC
masaya.yamasaki@NOM.com
+81 3 6703 1190

Manabu Akizuki - NSC
manabu.akizuki@NOM.com
+81 3 6703 1185

Yu Okazaki - NSC
yu.okazaki@NOM.com
+81 3 6703 1210

Atsushi Yoshioka - NSC
atsushi.yoshioka@NOM.com
+81 3 6703 1176

Virginia Wang - NSC
virginia.wang@NOM.com
+81 3 6703 1215

Kosuke Hatanaka - NSC
kosuke.hatanaka@NOM.com
+81 3 6703 1127

Japan chemicals & textiles

Daiki Ban - NSC
daiki.ban@NOM.com
+81 3 6703 1124

Shigeki Okazaki - NSC
shigeki.okazaki@NOM.com
+81 3 6703 1170

Taiwan Technology

Aaron Jeng, CFA - NITB
aaron.jeng@NOM.com
+886(2) 21769962

## Asia Technology

CW Chung - NIHK
cwchung@NOM.com
+852 2252 6075

Japanese version published on 17 June 2026

## Table of contests

Tech sector overview.... 3
Monthly global semiconductor/electronic parts shipments.... 9
SPE.... 17
Semiconductor & display materials.... 20
Special feature (Vol. 91): FDEs contributing to speedier deployment of AI agents.... 25
Share price performance chart for select companies.... 27
Appendix A-1.... 30

## Tech sector overview

Lead times lengthening even for analog products owing to rising demand from data centers

Advances in AI models continue to outpace system deployment, but even so major IT companies and private equity funds have been strengthening their FDE capabilities to spur uptake of AI agents. Japanese IT majors are targeting profit growth of over 15% on a CAGR basis in their medium-term business plans, and we see prospects for faster profit growth via increased uptake of AI agents. We think AI represents substantial business opportunities rather than a threat. Shipments of servers and networking equipment for AI have also been rising sharply as companies increase their supply capacity, and demand for conventional servers has been increasing substantially too. The increase in demand has caused supply-demand conditions to tighten, first for GPUs and HBM during the AI learning phase, spreading to ASICs and SSDs during the inference phase, and now to CPUs, analog semiconductors, and MLCCs in the AI agent phase.

## Demand for Al-related semiconductors remains strong

We have seen brisk growth in demand for Nvidia's GPUs and custom AI accelerators from Broadcom and Marvell Technology. Results for Feb–Apr also showed a 92% y-y (21% q-q) rise in data center-related sales at Nvidia, including a sharp 115% (12%) rise in sales to hyperscalers. Management expects sales to continue rising strongly, and is guiding for May–Jul companywide sales of \$91bn (up 11% q-q). Broadcom also reported Feb–Apr semiconductor sales of \$10.8bn (up 143% y-y), slightly ahead of guidance, and is projecting May–Jul sales of \$20.5bn (up 124%). Marvell Technology reported Feb–Apr sales of \$2,418mn (up 28% y-y), again slightly ahead of guidance. The company had said it was expecting sales growth of at least 25% y-y in full-year 27/1 in December, but hiked this to at least 40% three months later, and again to 50% when it released its latest results. It also hiked its outlook for 28/1 sales growth from 40% to nearly 50% and again to 55% at the same time.

Fig. 1: Data center-related sales at major semiconductor companies  
![](images/50d3fd3a8dbfbb0c73601202e5bb796df35b92bc9176cdf7341fa993a8f7ac41.jpg)  
Source: NOM, based on data disclosed by each company

Fig. 2: Global semiconductor shipment value, domestic inventory ratio for electronic parts & devices, and sector share prices  
![](images/3dc20011aa139619b7cbe79639ff9a1a3e985a25e4250912a8db93432dfce5cf.jpg)

![](images/118ecf4e96a21f91fdd619f055bd7a0785e546711f4d5bdd1082c48e5333fa32.jpg)

![](images/9e8b0226e69e1f9e29c73e70a0a1589659c6f45b3ebde6ebf69cbb22a1c6fffa.jpg)

![](images/efc24b2ec62e292d88a0220df6a98d53af96db2267d1571ffb4b409932fa85e7.jpg)  
Note: (1) Electronic parts & devices inventory ratio excludes impact of cathode ray tubes (CRTs). (2) Electronics, ICT, and machinery data shows performance versus the TOPIX based on industry share price indices covering all stocks listed on TSE-1.  
Source: NOM, based on WSTS data, METI's Indices of Industrial Production, and other materials

Fig. 3: Market cap versus the TOPIX by subsector in 2025  
![](images/3531653045d4e52e813d2730f3245a660e82f80e007aed3176024a9e64baa797.jpg)  
Note: Shows relative share price for combined market cap of major companies covered by NOM in each sector.
Source: NOM

Fig. 4: Market cap versus the TOPIX by subsector in 2026  
![](images/01e3bc3ffb2ec8ab1a401055c6695353304d3d491fc472d6645cefa4def2c1e4.jpg)  
Note: Shows relative share price for combined market cap of major companies covered by NOM in each sector.
Source: NOM

## Markets other than AI also heading toward recovery, but gap with AI growing

Anthropic, OpenAI, Google, and others have continued to make advances in AI agents, and uptake in white-collar parts of the B2B market has been gathering pace. While rapid advancements have been made in AI models, deployment in client systems has failed to keep pace. In view of this, we have seen moves to step up rollout at large firms via collaboration with conventional system integration and SaaS companies and at SMEs via involvement from private equity funds. Japanese IT majors have also adopted a multi-AI agent strategy of using third-party products for commodity AI models and in-house-developed products for industry-specific AI. We think investment in AI servers and related data centers will remain brisk as long as competition between AI agents continues in these B2B markets. Tight supply-demand for many components is leading to price hikes, which is increasing capex as well. In the past, tight supply-demand created a trade-off in which higher component costs suppressed PC/smartphone demand via price elasticity. In contrast, in the AI server market, price hikes are actively accepted to secure greater procurement volumes, which in turn encourages more aggressive capital investment by suppliers. Thus, while the cyclical nature of the business model in which prices fluctuate in line with the supply-demand balance remains unchanged, there is a possibility that supply-demand conditions for various products will remain tight for longer than previously. Meanwhile, price-sensitive B2C markets such as PCs/smartphones may see demand shrink after preemptive buying, a negative impact on the price-sensitive mass market zone from price hikes, and potential PC supply contraction on CPU shortages.

## Industrial electronics: Ongoing solid infrastructure-related demand amid tight memory supply-demand

While the materialization of geopolitical risks has raised uncertainty over the macroeconomy, we see little direct impact from the Middle East conflict at industrial electronics majors and semiconductor producers, thanks in part to business portfolio reforms, and expect ongoing growth in earnings on continued strong investment in data centers, especially for AI, and electric power infrastructure. Industrial electronics majors generated record-high profits in 26/3 and we expect earnings to continue to grow from 27/3 onwards. We think the era of full-fledged deployment of AI agents will provide large tailwinds for major IT firms with AI platforms, system architecture, and domain knowledge, leading to growth in their own services. We recommend: Kioxia Holdings, which stands to benefit from growth in AI-related demand; Hitachi, where HMAX services using physical AI are likely to start making a full-scale contribution; Mitsubishi Electric, on strong performance in infrastructure-related businesses such as defense; Fujitsu, on progress with the transformation of its business model in the direction of Uvance and modernization; Fuji Electric, on strong performance in power supplies for data centers and energy management; and NEC, on growth driven by defense and BluStellar.

## Electronic parts: Focus on new products for AI data centers

The 10 major Japanese electronic parts suppliers under our coverage generated aggregate sales of ¥2,862.6bn (up 12.8% y-y) and operating profits of ¥269.8bn (up 66.2%) in Jan–Mar 2026. Sales were 5.3% higher and operating profits were 9.5% higher than our pre-release estimates of ¥2,716.2bn and ¥245.9bn. The main factor behind the overshoot in operating profits was better-than-expected sales. By application, there was strong growth for data center and general industrial applications, and strong demand for high-end automotive, smartphone, and wearable applications. We estimate that yen depreciation buoyed sales by 3.5ppt and operating profits by 4.1ppt in Jan–Mar. Excluding forex effects and business divestments, we estimate that sales rose 10.3%. We think a number of companies will benefit from sustained positive impacts from new AI-related products. They include Hirose Electric's probe application products, Murata Manufacturing's advanced compact, high-capacitance capacitors, TDK's battery backup units (BBUs) for 400V/800V data centers, Ibiden's EMIB, and Niterra's electrostatic chucks for ultra-low-temperature etching.

## Consumer electronics: We recommend Sony Group, Fujifilm Holdings, Canon

Although the consumer electronics industry is expected to face cost increases due to surging memory prices and the impact of conditions in the Middle East, this has not yet led to production halts caused by supply shortages. In addition to companies taking a proactive stance on passing higher costs on to prices, there are also favorable factors such as the positive impact of a weaker yen and lower US tariff rates, on which basis we expect solid earnings at sector companies. On the demand side, demand related to AI and data centers has remained buoyant, while sales of hobby-oriented products such as cameras and watches have been strong, and even the previously sluggish musical instrument segment is showing signs of bottoming out. In sectors with many diversified companies, we still think it is important to closely examine each company's business portfolio strategy. We recommend: Fujifilm Holdings, which has been developing its business portfolio strategy based on proprietary technologies it has built up in photographic film; Sony Group, which has been reinforcing its position as a platform provider within the entertainment industry; and Canon on the prospect of stable cash generation from printers and cameras.

## SPE: We see near-term upside for front-end equipment, look to qualitative changes too

Demand for front-end SPE has been gathering pace, and we think investors are likely to carry on focusing on demand upside in the short term (2026 and 2027). We also get the impression that the nature of growth has been changing. (1) Improved earnings at advanced foundries other than TSMC has increased investment upside for 2027 onwards. (2) Memory producers have been drafting more concrete investment plans as their customers have been signing long-term contracts, and this has made it easier for SPE companies to come up with demand forecasts with longer-term horizons and given greater clarity to front-end equipment demand over the medium term. (3) Tokyo Electron, Japan's biggest front-end SPE producer, has become more confident about hiking prices to pass on cost increases, and while this does not necessarily apply to all Japanese front-end companies, we now see increased expectations for cost pass-throughs rather than inflation being a negative for the sector overall. Earnings at back-end SPE companies have also been improving, but we expect investors to carry on preferring front-end SPE. Among back-end SPE companies, we recommend Tokyo Seimitsu, where we expect margins to improve as its sales exposure to the high value-added AI market increases.

Fig. 5: Developments at major overseas electronics companies (1)

<table><tr><td>Results date</td><td>Ticker</td><td>Company</td><td>Segment</td><td>Development</td></tr><tr><td>5/13</td><td>CSCO US</td><td>Cisco Systems</td><td>Telecommunication equipment</td><td>Results announcementFY26 Q3 sales up 12% y-y to $15.8bn, slightly above the midpoint of the guidance range ($15.5bn). Non-GAAP gross margin of 66.0% and non-GAAP operating margin of 34.2%, versus guidance of 66.0% and 34.0%. Product orders up 35% y-y overall, with rises of 18% at enterprise segment, 27% at public segment, and 105% at cloud and telecom services segment. AI infrastructure orders from hyperscalers totaled $5.3bn on a Q1-3 basis, and company raised FY26 full-year guidance for orders from over $5bn to $9bn and for sales from $3bn to $4bn. Guiding for Q4 sales of $16.8bn, non-GAAP gross margin of 66.0%, and non-GAAP operating margin of 34.5%. Looking for price hikes to offset higher memory costs to some exte

[中间内容因长度限制已省略]

f holding investment trusts include, for domestic investment trusts, an asset management fee (trust fee) of up to 5.5% (tax included/annualized basis) of the net assets in trust, as well as fees based on investment performance. Other indirect costs may also be incurred. For foreign investment trusts, indirect fees may be incurred during the course of holding such as investment company compensation.

Investment trusts invest mainly in securities such as Japanese and foreign equities and bonds, whose prices fluctuate. Investment trust unit prices fluctuate owing to price fluctuations in the underlying assets and to foreign exchange rate fluctuations. As such, investment trusts carry the risk of losses. Fees and risks vary by investment trust. Maximum applicable fees are subject to change; please thoroughly read the written materials provided, such as prospectuses or documents delivered before making a contract.

In interest rate swap transactions and USD/JPY basis swap transactions (“interest rate swap transactions, etc.”), only the agreed transaction payments shall be made on the settlement dates. Some interest rate swap transactions, etc. may require pledging of margin collateral. In some of these cases, transaction payments may exceed the amount of collateral. There shall be no advance notification of required collateral value or collateral ratios as they vary depending on the transaction. Interest rate swap transactions, etc. carry the risk of losses owing to fluctuations in market prices in the interest rate, currency and other markets, as well as reference indices. Losses incurred as such may exceed the value of margin collateral, in which case margin calls may be triggered. In the event that both parties agree to enter a replacement (or termination) transaction, the interest rates received (paid) under the new arrangement may differ from those in the original arrangement, even if terms other than the interest rates are identical to those in the original transaction. Risks vary by transaction. Please thoroughly read the written materials provided, such as documents delivered before making a contract and disclosure statements.

In OTC transactions of credit default swaps (CDS), no sales commission will be charged. When entering into CDS transactions, the protection buyer will be required to pledge or entrust an agreed amount of margin collateral. In some of these cases, the transaction payments may exceed the amount of margin collateral. There shall be no advance notification of required collateral value or collateral ratios as they vary depending on the financial position of the protection buyer. CDS transactions carry the risk of losses owing to changes in the credit position of some or all of the referenced entities, and/or fluctuations of the interest rate market. The amount the protection buyer receives in the event that the CDS is triggered by a credit event may undercut the total amount of premiums that he/she has paid in the course of the transaction. Similarly, the amount the protection seller pays in the event of a credit event may exceed the total amount of premiums that he/she has received in the transaction. All other conditions being equal, the amount of premiums that the protection buyer pays and that received by the protection seller shall differ. In principle, CDS transactions will be limited to financial instruments business operators and qualified institutional investors. Transfers of equities to another securities company via the Japan Securities Depository Center are subject to a transfer fee of up to ¥11,000 (tax included) per issue transferred depending on volume. No account fee will be charged for marketable securities or monies deposited.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved.
"""
