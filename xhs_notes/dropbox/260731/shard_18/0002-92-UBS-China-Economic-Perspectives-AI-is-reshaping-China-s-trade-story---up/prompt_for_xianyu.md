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
# China Economic Perspectives

# AI is reshaping China's trade story – upgrading 2026 trade forecasts

## AI has emerged as a key driver of China's trade

China's trade performance has consistently exceeded market expectations in 2026, with exports recording $18\%$ YoY and imports $26\%$ in 1H. We believe AI-related trade is the main driver, contributing nearly half of total export and import growth in 1H. The strength has been driven more by prices than volumes, reflecting an undersupplied market and product upgrading. A significant portion of China's AI trade is conducted with neighbouring economies in the region, facilitating both imports and exports and underscoring China's deeper integration into the global tech supply chain.

## Resilience extends beyond AI

Non-AI exports rose 11% YoY in 1H, driven by strong overseas sales of green products (batteries, solar, power equipment, etc.) as well as a surge in auto shipments, particularly EVs and hybrid vehicles. Consumer goods exports failed to match this momentum. Non-AI imports jumped 19% YoY led by gold, oil and other commodities, all supported by price increases. We expect this price tailwind to fade later in 2026.

## Upgrade 2026 trade growth forecasts

Reflecting sustained AI-led export strength and resilience elsewhere, we now expect exports to grow around 18% in 2026 in nominal USD terms. The strong AI-related exports should boost related imports, while non-AI imports may soften partly as commodity price growth decelerates. We therefore raise our 2026 import forecast to 24%. Excluding price effects, we expect net exports to contribute 0.8ppt to real GDP growth, notably smaller than 1.6ppt in 2025, highlighting the need to stabilize domestic growth. Key risks include the strength of the global AI cycle, commodity price swings, trade policy changes, and domestic growth momentum.

## Macro and policy implications

Despite strong exports and AI-related wealth effects, domestic weakening in 2Q points to a likely policy shift. In our view, any incremental demand for global commodities is more likely to come from AI and related infrastructure investment than from a strong rebound in China's property sector. Export prices have started to rebound in 2026 after falling $17\%$ over the past three years, led by tech products and domestic reflation. This may ease concerns about exported deflation, but could add to global inflation pressures in selected areas. Import prices are rising even faster, further eroding China's terms of trade. Even so, the RMB has remained resilient, with the PBoC allowing gradual appreciation, potentially as a signal of confidence and to help ease trade tensions.

## Economics

China

Jennifer Zhong

Economist

jennifer-a.zhong@ubs.com

+86-105-832 8324

Yu Song

Economist

S1460526010002

yu-za.song@ubs.com

+86-10-5832 8508

William Deng

Economist

william-w.deng@ubs.com

+852-2971 6765

Grace Wang

Economist

S1460524050003

grace-zc.wang@ubs.com

+86-105-832 8335

China's trade momentum has been surprisingly strong so far in 2026. Exports grew $17.6\%$ YoY in the first half of 2026, while imports jumped $26\%$ YoY, both far outpacing expectations. Stronger-than-expected export growth occurred despite renminbi appreciation against the US dollar (3% in 1H) and on a trade-weighted basis (NEER +5.5%, REER +3.1% in 1H).

This strength is largely price-related: export prices have bounced since early 2026 and increased by 6.5% YoY in 1H, while import prices surged by 18%. Both have been supported by a significant increase in tech product prices along with higher commodity prices across the board, not least crude oil. After adjusting for price effects, real export growth was largely stable at 10% YoY YTD (vs a 9.4% increase in 2025). Real imports rose notably by 9% (vs only a 0.5% increase last year), with momentum jumping in 1Q before softening in 2Q.

In this note, we examine the underlying sources of strength, identify the key growth drivers, and evaluate the sustainability of these trends.

Figure 1: Price increase explains a large portion of trade strength YTD  
![](images/ddd5ff9b894b75980fe71ecdc542934f791300c7e37531bbcb14d44ddc471e9a.jpg)  
Source: CEIC, UBS estimates

Figure 2: RMB strengthened in EER terms  
![](images/1d55e5dff985bd5c4cd1b9509515df2089a0cab44d929330cc3ca28139eaa0f2.jpg)  
Source: Haver, UBS estimates

## AI trade has emerged as a key driver

The global AI boom has become a pivotal force behind China's trade upswing. Over the past few years, the rapid development and deployment of AI worldwide have reshaped tech supply chains. China is now increasingly integrated into the AI hardware ecosystem and, as a large hardware-components supplier, is benefiting from these tailwinds.

To quantify this, we define "AI-related" goods using two reference lists: a WTO AI-enabling list (104 HS6 products), and a broader list from NBER (665 items at HS10 level). Both approaches show exceptional growth: AI-related exports grew a robust 40-47% YoY YTD, while AI-related imports grew by 44-47% YoY. Because differences between US and Chinese trade codes complicate mapping at the HS10 level, we primarily rely on the narrower WTO list.

Most of China's AI exports are intermediate inputs, with integrated circuits (ICs) at the core. Under the WTO definition, over three-quarters of China's AI exports are intermediate inputs and the rest are mostly equipment, while China exports very little chemicals or raw materials. The AI export basket features ICs, computer parts and components, communications equipment (e.g., optical modules), printed circuit boards (PCBs), data storage devices, power equipment and more. While micro-level observations suggest some products are tailored specifically for AI usage such as optical components and PCBs, a large portion consists of mature-node chips also used in automobiles or industrial manufacturing that fall on the WTO list of AI-enabling products. This could overstate the AI-specific contribution.

China's AI trade is deeply embedded in global supply chains, especially Asia. Over $70\%$ of the trade is connected with other Asian economies. Hong Kong is the top export destination with most of the shipments likely re-exported to other destinations - overall re-exports consistently account for more than $98\%$ of Hong Kong's merchandise exports even though detailed re-export data for AI-related products are unavailable. Vietnam, Korea and Taiwan are the top three export destinations within Asia, taking a quarter of the AI exports directly, reflecting China's ties with other major AI exporters and the Asian supply chain.

On the import side, chips dominate: more than 60% of AI-related imports are various semiconductors (memory, processors and amplifiers), alongside advanced computer components, data storage units, and semiconductor fabrication equipment. A large share of China's AI exports is "processing trade", which inherently relies on imported components at earlier stages of production.

Figure 3: AI exports cover a broad mix of tech hardware  
![](images/9a883e082a6f7f4201d95614eabdf67f70833c64ad27bfe7f6c6f344640c5554.jpg)  
Source: CEIC, WTO, China Customs, UBS estimates

Figure 4: AI imports are dominated by ICs  
![](images/147bf903b16c4c8ed84ea9e9f419004618e52f60e2e85edb8c3e2ba504d32017.jpg)  
Source: CEIC, WTO, China Customs, UBS estimates

AI-related products already make up nearly half of trade growth in 2026. In the first half, approximately $23\%$ of China's total exports and $30\%$ of its imports were AI-related, marking a notable increase from $17\%$ and $22\%$ in 2023, respectively. Both imports and exports of AI related products have grown robustly by $47\%$ YoY YTD, contributing around half of overall export/import growth ( $49\%/47\%$ , respectively).

Figure 5: AI products contributed 49% of export growth and 47% of import growth in 1H  
![](images/3eae193d6c3245444e3f1dc1a2988b9ac26a014447c46596a9254ff2dc843fd5.jpg)  
Source: CEIC, WTO, China Customs, UBS estimates

The AI trade boom is mainly a nominal price story rather than a volume cycle. The rise in AI trade is much more reliant on price changes than previous cycles. Take electronic integrated circuits as an example. China's exports of electronic ICs jumped by an impressive $96\%$ YoY in 1H in value terms, but volumes crept up by only $6\%$ YoY and they have decelerated lately (in units). The slowdown in volume terms likely reflects a combination of base effects and softer demand in some submarkets. On the import side, values climbed 56% YoY but volumes increased by just 8% YoY. Prices drove much of the growth. The sharp price increase reflects AI-driven demand in a supply-constrained market, with capacity shifting toward high-end AI-related products, tightening supply elsewhere and pushing up tech product prices more broadly. Changes in product content per export/import unit may also have lifted average selling prices.

Figure 6: Price surge has been a major driver  
![](images/b551c95ac9d48aacfdad973a756c57d39493c9a087f2f5d3aac6dbd6b25893d5.jpg)  
Source: CEIC, UBS estimates

## Can China's AI trade boom last?

Al Capex will likely expand further in the coming quarters based on the UBS tech team's projections (see here). The UBS team foresees an unprecedented memory upcycle, with DRAM/NAND undersupply lasting into 2Q28/4Q27. On pricing, they estimate that Long Term Agreements (LTAs) could fix c. 20-30% of total industry volumes and pricing for the next 2-3 years (see here). Additionally, with demand continuing to far outstrip supply, they forecast ex-LTA DDR contract pricing to rise +32% QoQ in 3Q26 and +18% QoQ in 4Q26, after +67% QoQ in 2Q26; and for NAND they forecast pricing up +30% QoQ in 3Q and +12% QoQ in 4Q after +67% QoQ also in 2Q (see here). Consequently, the YoY growth is likely to peak around mid-2026 and slow later in the year, nonetheless to an elevated level. Export prices for China's major tech products will continue to benefit in the near term.

On the external demand side, given China's existing scale of production and early connection to the supply chain, we expect China's manufacturers to continue to benefit from further global AI Capex expansion and other tech-related demand. On the import side, a substantial portion of China's tech imports are processing inputs destined for further processing before re-exports, so booming AI exports mechanically drive AI imports. The relaxation of import bottlenecks in 2026 – for example, the US approval of sales of Nvidia H200 AI chips to some Chinese firms after President Trump's visit – offers some relief for domestic data centres to access advanced GPUs, but we believe this falls short of a breakthrough (see here).

Looking further ahead, the medium-term challenge is how much China can continue moving up the value chain. China's existing industry scale offers China the early advantage to be a large hardware components supplier, but currently the most advanced AI infrastructure in global trade, such as GPUs and HBMs, are dominated by other economies. In addition, China's access to advanced semiconductor manufacturing equipment is constrained. Thus, there could be limited further market share gains and domestic value-added gains in the medium term.

## Resilience Beyond AI

Beyond the rapidly growing AI-linked sectors, other exports have also held up well. Non-AI exports expanded by 11% YoY in 1H26.

Autos remain an important source of resilience. China's auto export growth accelerated to $60\%$ YoY in 1H, driven by hybrid vehicles (115% YoY) and EVs (57% YoY). The appeal of EVs has strengthened further in 2026 amid energy transition trends and after the Middle East conflict. Since becoming a net car exporter in 2023, Chinese automakers are projected to capture one-third of global market share by 2030 (UBSe), leveraging advanced EV technology and expanding international presence.

Green trade has become another key growth engine, supported by electrification and infrastructure demand. "Green exports", including batteries, solar, wind, electrical equipment, and optical fiber, expanded 31% YoY in 1H26 (vs 15% in 2025), contributing 8% to headline export growth. In particular, battery exports climbed 40% YoY, solar equipment 24%, and electrical equipment 24%. Heightened urgency for electrification and resilient infrastructure—particularly post-Middle East conflict—has boosted demand for China's green technologies, supported by their cost competitiveness, improving product quality, and proven manufacturing scale. However, future growth will hinge on policy shifts in key markets, especially Europe, China's largest customer (see UBS ESG team's note and monthly tracker; note the analysis excludes products overlapped with AI list), as well as China's own policies such as the removal of export VAT rebates for solar.

Traditional consumer goods exports remained weak. Categories like textiles and apparel (up 1.4% YoY in 1H), footwear and hats (-5%), furniture and lighting (0.6%), and toys and sporting goods (-12%) have struggled, reflecting muted global consumer demand amid persistent inflation. In June, exports of furniture and home appliances accelerated significantly, possibly reflecting increased demand related to heatwaves (see June reading). Thus, robust export growth YTD has been mainly driven by tech and industrial demand, while traditional goods have lagged behind.

Figure 7: China has shifted from a net auto importer to an exporter  
![](images/41209111f7afd80e4a6cd9e0c8405537d5c78768d5d19f68cfa463ff02c113c1.jpg)  
Source: CEIC, China Customs, UBS estimates

Figure 8: Green exports gained momentum in 2026  
![](images/153cf69147ce8f5e3c1e40f40c0854eb402528537d19953aec8ac7c2fd7d8770.jpg)  
Source: CEIC, China Customs, UBS estimates

Non-AI import strength does not signal a broad domestic-demand rebound. China's non-AI imports grew $19\%$ YoY in 1H, with precious metals (particularly gold) and commodities standing out. In our view, the strength mainly reflects price gains, selective industrial demand, and financial investment demand, rather than a broad-based recovery in domestic activity.

Price effects lifted import values. In 1H26, import prices rose 38% YoY for copper ore and 36% for unwrought copper, 20% for crude oil and 24% for petroleum products, while iron ore prices increased 5%. This explains a meaningful share of headline import strength, suggesting value growth should not be read as a broad volume rebound.

Import volumes of key commodities were mixed. Crude oil is the clearest example: during the 2Q price spike following Middle East tensions, volumes fell -30% YoY (9% in Q1) and -76% QoQ Saar (-5% in Q1). This likely reflected weaker downstream demand, as seen in lower chemical-sector utilization (until signs of SOE utilization improvements in the week of July 20), combined with inventory drawdowns in downstream sectors on expectations that the oil shock would prove temporary. Among industrial commodity imports, copper ore volumes were broadly flat YoY, unwrought copper fell 5% YoY, and iron ore held up at 6% YoY. On a seasonally adjusted basis, copper ore volumes declined 12% QoQ Saar (0% in Q1), while iron ore edged up 4% (-21% in Q1). In our view, real commodity demand is increasingly tied to electrification, EVs, power infrastructure, and export-oriented manufacturing. With property new starts still trending lower through 2Q, a property-led restocking cycle remains absent, despite policy easing and signs of sales recovery in some cities.

Gold imports mainly reflect financial investment demand. YTD gold imports surged 189% YoY and contributed over a quarter of total import growth. Chinese investment demand for gold typically follows price gains with a lag: as prices rose, demand for 

[中间内容因长度限制已省略]

ofessional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) Unit 2901, Level 29 Altimus, Pandurang Budhkar Road, Worli, Mumbai – 400 018. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email : parameshwaran.s@ubs.com, Name of Grievance Officer Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company / companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch to professional institutional investors and/or persons permitted under applicable regulation. Unless permitted by applicable Taiwan laws and regulations, this material is for reference and information only and should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reprinted, reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/3bb399bfd65820a763b0950191476e97d1e44aa56bc811811680c05ce2886da7.jpg)
"""
