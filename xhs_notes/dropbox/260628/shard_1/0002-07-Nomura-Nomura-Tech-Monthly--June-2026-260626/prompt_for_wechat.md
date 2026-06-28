你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

<table><tr><td>Results date</td><td>Ticker</td><td>Company</td><td>Segment</td><td>Development</td></tr><tr><td>5/13</td><td>CSCO US</td><td>Cisco Systems</td><td>Telecommunication equipment</td><td>Results announcementFY26 Q3 sales up 12% y-y to $15.8bn, slightly above the midpoint of the guidance range ($15.5bn). Non-GAAP gross margin of 66.0% and non-GAAP operating margin of 34.2%, versus guidance of 66.0% and 34.0%. Product orders up 35% y-y overall, with rises of 18% at enterprise segment, 27% at public segment, and 105% at cloud and telecom services segment. AI infrastructure orders from hyperscalers totaled $5.3bn on a Q1-3 basis, and company raised FY26 full-year guidance for orders from over $5bn to $9bn and for sales from $3bn to $4bn. Guiding for Q4 sales of $16.8bn, non-GAAP gross margin of 66.0%, and non-GAAP operating margin of 34.5%. Looking for price hikes to offset higher memory costs to some extent.</td></tr><tr><td>5/20</td><td>ADI US</td><td>Analog Devices</td><td>Semiconductors</td><td>Results announcementFY26 Q2 sales of $3.63bn (up 37% y-y, up 15% q-q), versus guidance of $3.5bn ±$0.1bn, adjusted gross margin of 73.0%, and adjusted operating margin of 49.0%. Sales up 20% q-q at industrial segment, up 8% at automotive segment, up 22% at communications &amp; data center segment, and flat at consumer electronics segment. Midpoints of Q3 guidance are $3.9bn for sales, 49.0% for non-GAAP operating margin, and 8% for q-q sales growth. Guiding for q-q sales growth of mid- to high-single digit growth at industrial segment, low- to mid-teen growth at communications &amp; data center segment, but a sales decline at the consumer segment.</td></tr><tr><td>5/20</td><td>NVDA US</td><td>NVIDIA</td><td>GPU/MPU</td><td>Results announcementFY27 Q1 sales up 85% y-y at $82.0bn (guidance: $78bn), non-GAAP gross margin of 75.0% (75.0%), and non-GAAP operating margin of 65.9%. Data center orders up 92% y-y and 21% q-q, with hyperscaler orders up 115% and 12% q-q, other orders up 74% and 31% q-q and edge orders up 29% y-y and 10% q-q. Q2 guidance calls for sales of $91.0bn and gross margin of 75.0%. It estimates CY26 CPU TAM of $200.0bn, with its share at just over $20bn.</td></tr><tr><td>5/27</td><td>HPQ US</td><td>HP</td><td>IT hardware/services</td><td>Results announcementFor Q2 (from Feb-Apr 2026), the company reported revenue growth of 9% y-y (up 6% in constant currency terms) and adjusted EPS of $0.86 (up 21%), versus the 27 May Bloomberg consensus forecasts of $14.0bn and $0.71 respectively. PC shipment volume fell 7% y-y. The company said that there had been some rush demand for commercial PCs. Printer shipment volumes were down 7% and consumable sales volumes were up 1% (flat y-y on a constant currency basis). The company is guiding for 26/10 adjusted EPS of $2.9–3.1 (previously $2.9–3.2). Price revisions helped sales at the personal systems segment to rise 10% y-y on a constant currency basis even though PC shipment volumes fell. Margins at the segment rose y-y, partly thanks to the use of strategic inventories, but the company said it expected them to deteriorate through Q4 as the boost from strategic inventories fades. The company still expects the hardware market to contract by low single digits in 2026 H2 and sales of consumables to also fall by low single digits on a constant currency basis. It said that while companies had been prioritizing investment in PCs recently, it expected a recovery in due course.</td></tr></table>

Source: NOM; consensus forecasts are by Bloomberg, comments on business conditions are taken from results documents, etc

Fig. 6: Developments at major overseas electronics companies (2)

<table><tr><td>Results date</td><td>Ticker</td><td>Company</td><t

[中间内容因长度限制已省略]

nd fluctuations in the nationwide consumer price index. The notional principal of inflation-indexed JGBs changes in line with the rate of change in nationwide CPI inflation from the time of its issuance. The amount of the coupon payment is calculated by multiplying the coupon rate by the notional principal at the time of payment. The maturity value is the amount of the notional principal when the issue becomes due. For JI17 and subsequent issues, the maturity value shall not undercut the face amount. Purchases of investment trusts (and sales of some investment trusts) are subject to a purchase or sales fee of up to 5.5% (tax included) of the transaction amount. Also, a direct cost that may be incurred when selling investment trusts is a fee of up to 2.0% of the unit price at the time of redemption. Indirect costs that may be incurred during the course of holding investment trusts include, for domestic investment trusts, an asset management fee (trust fee) of up to 5.5% (tax included/annualized basis) of the net assets in trust, as well as fees based on investment performance. Other indirect costs may also be incurred. For foreign investment trusts, indirect fees may be incurred during the course of holding such as investment company compensation.

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
