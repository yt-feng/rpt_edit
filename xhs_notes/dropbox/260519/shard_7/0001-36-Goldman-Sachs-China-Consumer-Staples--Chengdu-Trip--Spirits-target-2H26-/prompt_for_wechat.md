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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
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
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Consumer Staples: Chengdu Trip: Spirits target 2H26 recovery but visibility low; value retailer store openings on-track; PoS optimization a

We visited Spirits companies and Chengdu retail markets this week to check on-the-ground consumption sentiment in Sichuan. Key takeaways:

1) Spirits players are looking for sell-in and profitability improvement in 2H26 supported by an easier base despite uneven 2QTD retail demand recovery and still low visibility on demand recovery. We visited two Sichuan-based upper mid end spirits companies and found mixed 2Q trends with one seeing positive growth during the Labor Day holiday and sales stabilizing in 2QTD while the other continues de-stocking efforts. Companies noted that residential banquet demand generally remains subdued with continued trading-down in Sichuan, where companies are stepping up investments to varying degrees to support volumes through price concessions for banquets. On the bright side, both companies noted they have reduced channel inventory to healthier levels and are targeting slight YoY topline recovery for full-year 2026 alongside improving profitability/OCF through tighter cost control/operating leverage/disciplined production.

2) F&B Value Retailers channel check in Sichuan/Southwest China: Our channel checks on value retailers in Sichuan/Southwest China highlighted what appears to be a high-growth triopoly landscape led by a dominant local chain (“Yummy Snacks”) and trailed by Wanchen and Busy Ming. Per our channel checks, all the players show store format skewed to discounter supermarket in this region but with different mix of daily essential SKUs (non snack & beverage). In terms of competition, our checks suggest the local chain has very high store density in Chengdu/Sichuan including sub-urban areas (our county level market visit in Pi County surrounding Chengdu City suggested a store distance at only 300\~400m with 6 Yummy Snack stores in the area). Our checks indicated that Wanchen now has c. 1.4k stores in the southwest region after adding 300\~400 new openings year to date in 2026, mainly fueled by deeper town-level penetration with c.30k population per town (currently only 1/2\~1/3 penetrated in Sichuan) and gaining market share mainly from fragmented traditional trade (particularly local, non-chain supermarkets with lower turnover and weaker product offerings) in the low-tier areas. Meanwhile, checks note that unit economics of this national brand remain robust with \~20% GPM and HSD% operating margins in Sichuan, with lower-tier county/town regions enjoying higher margins from cheaper rents despite lower per-store GMV. While per-store average monthly GMV has diluted since 2024 amid rapid roll-out, value retailers players adopted more disciplined site selection and competition strategies into 2025/26.

3) UPC investor day market visit - PoS optimization is a key growth lever: Our

# Leaf Liu

+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

# Christina Liu

+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

# Valerie Zhou

+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

meeting with UPC's regional management in Chengdu highlighted strong execution in Southwest China, where the company now directly covers 300k+ of the total 500k+ PoS with the rest reached by 1k+ distributors. PoS optimization has been the key focus in recent two years, with new high-potential outlets generating 2-3x sales vs. average and initiatives to refine consumption scenarios driving 30%+ sales uplift in the selected urban-rural hub we visited, with deeper penetration into restaurants/sports/leisure venues and non-F&B retail channels (e.g. pharmacies). In terms of POS competition, we saw broad-based expansion in coolers and smart vending machines, with 1k+ units already deployed and further upside from deeper cooperation with local CVS chains. In F&B value retail, UPC maintains pricing discipline, with differentiated products offering, and pricing floors set at 90% of suggested RSP for core SKUs and 70% for others.

The authors would like to thank Lily Qi for her contribution to this report.

# Market/Sales Site Visit Takeaways

# F&B Value Retailer Channel Checks

We performed channel checks to assess the footprint of F&B value retailers in Sichuan and the expansion outlook for Wanchen in Southwest China region (“the brand”). Store format of discounter supermarkets appear relatively more popular in Sichuan especially for the local chain Yummy Snacks. Key takeaways include:

Industry outlook: The brand continues to see meaningful room for expansion, backed by: 1) consolidating traditional trade: especially market share gain from small, predominantly non-chain supermarkets in lower-tier regions, while value retailers offer more affordable offerings with higher quality; 2) still-low penetration at the town level. Currently value retailers are moving into towns with $< 50k$ populations. The brand still sees whitespace in township (i.e. with c. 30k populations), while the brand has so far only penetrated $1/3 \sim 1/2$ of these towns. 3) incremental demand creation: value retailers stimulates additional snack and beverage consumption, with rich product offerings. Some stores opened near university campus have demonstrated new whitespaces for store locations.

Store UE for the brand in southwest region remains healthy, and lower-tier regions benefit from a lower rent-to-sales ratio: For some high performing stores in urban areas, store-level GPM generally stands at c.23% net of subsidies, against a cost structure comprised of rent at c.6% of sales, labor at c.6%, and utilities at c.2%, implying HSD% store-level OPM. Average monthly GMV per store for the brand was generally at c.Rmb320k\~330k in 2025 in Southwest China but UE is benefiting from lower opex cost.

Competitive landscape in Southwest region: Southwest China features a high-growth triopoly landscape led by a dominant local chain and trailed by two national players (including the brand), with the brand at c.1.4k stores vs. the local brand (as the largest player in Southwest) at c.2k+ stores in Sichuan. Our market visit showed us that the local chain has very high store density in Chengdu/Sichuan including sub-urban areas (our county level market visit in Pi County surrounding Chengdu City showed a store distance at only 300\~400m with 6 Yummy Snack stores in the area). In terms of product offering, this local incumbent is differentiated by a stronger emphasis on the discount

supermarket format, with more meaningful exposure to daily essentials alongside snacks and beverages, as well as a higher mix of white-label products and more localized sourcing. Improving balance between per-store GMV vs. unit expansion: Our channel checks noted that after 2\~3 years of radical store expansion by elevated new-store subsidies with focus more on quantity over quality especially in 2023-24, competition has turned more rational since 2H24 with subsidy intensity easing, site selection becoming more disciplined, and KPIs for BD teams skewing to success ratio, which has supported a broad-based recovery in per-store GMV since 2H25, with the improvement likely extending into 2026.

Current trends in Southwest region: 1) More refined operation and localized sourcing: with store density increases and procurement scale reaching critical mass, local sourcing has become more viable, driving a higher local procurement ratio catering to local customer preferences/taste. 2) New stores are now predominantly discount supermarkets: More than $80\%$ of recent openings still fall into this category, first-mover advantage for local incumbents and stronger consumer association with the format. 3) Category expansion is extending into cold-chain frozen foods: Operators are selectively adding frozen products (now small, at LSD% of GMV), particularly hotpot-related convenience foods given their relatively higher margin profile.

Retail Pricing comparison: We visited several stores of the dominant local chain in Chengdu's urban-rural fringe and a smaller local operator in a commercial district. Our checks suggest that pricing for key beverage SKUs from Nongfu/Eastroc/Alienergy/Mizone/UPC, as well as purified water SKUs from Nongfu/Wahaha, are broadly comparable across the two stores. By contrast, Tingyi's sweetened tea and C'estbon water were 10\~20% cheaper at the leading local chain. Pricing differences were more pronounced in noodles: the leading local player offered better value on certain top SKUs from tier-1 brands, for example, at a 10% discount to suggested RSP for a core UPC SKU, vs. only c.5% at the smaller local brand's store. Less prominent brands were priced even more aggressively, at up to 40% lower in the leading brand's store vs. in the smaller local brand's store. That said, we note different target customer profiles between stores located in the urban-rural fringe and those nearer the CBD.

# Beverage Market/Point of Sales site visit We visited a core commercial district in central Chengdu and observed UPC's execution for POS optimization/performance improvement in the region. In

Southwest regions, UPC has already directly covered $60\% + / \mathrm{or} 300\mathrm{k}+$ of the c.500k+ retail PoS and part of the rest covered by $1\mathrm{k}+$ distributors. In Sichuan, UPC has directly covered close to 130k traditional PoS.

# Key observations:

We see broad-based stepped-up investment in coolers and smart vending machines across leading beverage brands in Southwest China. Per the company, UPC has deployed 1k+ smart vending machines across Southwest China, and the local team remains confident in sustaining rapid growth this year.

According to UPC's Southwest regional manager, meaningful whitespace remains for further expansion in the Southwest region, with the region delivering DD% top-line growth in 1Q26. First, the company sees multiple levers to improve per-POS productivity: 1) Ongoing optimization of the PoS base should lift overall average sales per PoS, as developed higher-potential new PoS can generate 2-3x per-PoS sales vs. previous avg. level. 2) Further scenario development can also enhance PoS productivity: In one urban-rural fringe commercial hub that we visited, monthly sales increased by $30\%+$ after refining/expanding relevant consumption scenarios. Penetration of both coolers and smart vending machines into restaurants and sports/leisure venues (e.g. billiard halls and internet cafés) also continues to improve, with some locations operated through direct partnerships with professional smart-vending machine operators. Meanwhile, new PoS development remains another key growth driver. 1) Expanding cooperation with fast-growing CVS chains including local chains such as Hongqi Chain (c.3.5k stores in Sichuan), and Wudongfeng (c.1.7k stores), as well as national brand Meiyijia (c.1.5k-1.6k stores). 2) Smart vending machines are also creating new PoS by increasingly being deployed outside traditional food-and-beverage retail outlets, such as pharmacies and optical stores, where they have been well received as an ancillary revenue stream for merchants. 3) Both noodles and beverages have already penetrated most leading national and local F&B value retail chains, with the companies maintaining tight pricing discipline by requiring retail prices to remain at no less than $90\%$ of suggested retail price for core SKUs and $70\%$ for other SKUs.

\- Shelf-date differences across brands in local CVS / POSs in Chengdu (note that regional checks may not be representative of nationwide situation): We observed a noticeable difference in production-dates across brands in the PoS we visited in Chengdu. In the CVS/smart vending machines that we visited, CR Beverage products appeared relatively older, with some batches carrying February production dates; in contrast, UPC's green tea and sugar-free tea/Eastroc's Bushuila and Special Drink, were mostly from late-March to April batches. Nongfu's Oriental Leaf appeared even fresher, with most products from April batches.

# Spirits company mgmt meeting takeaways – Disciplined on supply side, but meaningful demand recovery still not in sight

We visited two upper-mid-end spirits companies in Sichuan. On the pricing/volume side, both companies are cautious on the effectiveness of price cuts to drive volume pick-up. Instead, the mgmt of company A mentioned consumer promotions (QR code scan) to boost bottle-open rate while company B is focused on brand power/channel promotions esp. on banquets. Both companies are also cutting production volume/supply with controlled cellar capacity utilization, and will focus on operating efficiency gains to support profitability in 2026.

# Company A

Brand performance and 2026 outlook: 2Q26 still saw pressured topline (esp. in Apr/Labor Day) although lapping on gradually easing comp. While the company is expected to resume profitability in 2Q26 vs. a net loss in 2Q25, partially driven by operating efficiency improvements and expense control since 2H25. Mgmt also noted weak Labor Day banquet demand from their sales team. 2026 outlook: Under narrowing industry-wide decline, the company is looking for a flattish to slightly higher 2026 revenue vs. 2025 (c.Rmb3bn) with a more favorable set-up for 3Q26/4Q26 (easy comp from nationwide shipment control in Jul-Sep 2025) post a relatively tough 1H26. The company had a nation-wide shipment suspension in 3Q25 to digest channel inventory and support pricing system, and expect sales growth to resume positive in 3Q26 with pricing system gradually stabilized especially for its Rmb200\~300 range core SKU.

Channel inventory and cash flow: The company's distributor inventories are c.3 months vs. targeted 2 months since Jun 25, better than some other upper mid end brands at 4-5 months with weaker branding power. Operating cash flow turned negative in 2025 on extending distributor payments, transferring bill receivables to banks for factoring arrangements, and continued raw material throughput and expenses related to production base.

More disciplined supply side: The company has suspended construction of some projects under its capacity plan set a few years ago, and has started production control of base liquor, to lower inventory level, control supply and improve OCF.

By region/product update: In North China, Hebei/Shandong/Inner Mongolia remained resilient with still positive growth driven by strong distributors' channel competence and Rmb200-300 price range products. In South China, Jiangsu/Zhejiang slowed down and Henan/Hunan faced higher pressure. New products launched since Sep 2025 had some growth on a relatively small scale.

# Company B

Brand performance and 2026 outlook: The company had returned to positive sales growth in 1Q26, and also saw stabilizing and even slightly recovering sales with a mild growth during Labor Day Holiday (vs. $60 - 70\%$ decline in the same period last year due to very low gifting demand) for 2Q26. Mgmt commented that key to watch will be 3Q/4Q growth recovery although they don't expect a significant rebound from 2H25's low base and expect the demand level to remain lower vs. 2024 level. On th profitability side, the company looks for NPM improvement from the trough level in 2025 driven by operating efficiency improvements (i.e. in employee streamlining), and narrowing net OCF outflow in 2026 (vs. negative OCF in 2025-end) with further improvements in 2027.

By region/product performance: Mgmt highlighted stable performance in Shandong/North East China and home-market (Sichuan) saw bottoming-out signs while East/North China are still in adjustment. Core products sell-through remained stable in 1Q26, mainly driven by banquet occasions (sell through declined if excl. banquet).

More disciplined supply side: The company's inventory build-up has slowed down since 4Q25 as the company started production control of base liquor and production line staff streamlining, to lower inventory level, control supply and improve OCF.

Industry comments: However, the company noted a still weak industry-wide retail demand, with weak sell-through and bottle-open rate for residential banquet, and competitors making significant investment in banquet to boost volume which is still disrupting the pricing system in traditional trade (i.e. distributors reselling products at lower prices to wholesale market with the subsidies/discounts granted to banquet

scenarios by spirits brands). The company also hasn't seen a meaningful recovery in commercial consumption scenario or wholesale channels.

# Price Target Risks and Methodology - Uni-President China

Valuation methodology: We are Neutral rated on UPC. Our 12-m TP of HK\$8.2 is based on a 15X 2027E avg. P/E discounted back to end-2026 using a 7.8% CoE.

Key upside risks: 1) More favorable raw material price movements; 2)

Better-than-expected performance of convenience food driven by demand recovery or new product launch; 3) Better-than-expected competition in instant noodles/beverage.

Key downside risks: 1) Higher-than-expected raw material cost pressures; 2) more intense competition in instant noodles/beverage; 3) food quality issue.

# Disclosure Appendix

# Reg AC

We, Leaf Liu, Christina Liu and Valerie Zhou, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Leaf Liu GS (Asia) L.L.C., Christina Liu GS (Asia) L.L.C., Valerie Zhou GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

# GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the 

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
