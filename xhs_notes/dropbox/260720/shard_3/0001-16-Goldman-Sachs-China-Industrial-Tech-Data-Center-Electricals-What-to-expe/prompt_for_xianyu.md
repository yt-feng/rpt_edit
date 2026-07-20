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
CHINA INDUSTRIAL TECH: DATA CENTER ELECTRICALS

# What to expect in 2H26 on overseas expansion and domestic capex trend; 2Q26 preview; maintain Buy on Kstar, Neutral on Kehua/Megmeet

We outline the key things to look out for in 2H26 for the China data center electricals subsector and key debates for the stocks, given recent share price volatility with Kstar/Kehua/Megmeet -29% on average since July (vs. CSI 300 Index -9% and China Industrial Tech coverage avg. -16%). We note it will be key to watch (1) overseas expansion & new product rollouts: Progress in securing new international clients and commercializing next-gen architectures is critical. Key potential catalysts include Kstar's new UPS orders and 800VDC module onsite testing, Megmeet's Vera Rubin PSU ramp-ups, and Kehua's global certification efforts for power and cooling products. (2) domestic data center capex trend: Investors are actively looking for signs of accelerating domestic hyperscaler and colocation demand to offset the intense localized pricing pressures.

For 2Q26, while we expect headline numbers will demonstrate growth (Kstar earnings +20% yoy; Megmeet +110% yoy from a very low base), the underlying business momentum is likely to be affected by a few headwinds. Specifically, we believe Kstar will factor in \~Rmb20mn in FX losses; Kehua's pre-announced recurring net income (+9% yoy) missed expectations amid intense domestic competition, despite a one-off asset disposal gains; and Megmeet is navigating raw material cost inflation and continued investment for future growth, alongside domestic EV weakness. We maintain Buy on Kstar, Neutral on Kehua/Megmeet.

Hao Chen
+86(21)2401-8812 |
hao.z.chen@goldmansachs.cn
GS (China) Securities
Company Limited

Jacqueline Du  
+852-2978-1783 |  
jacqueline.du@gs.com  
GS (Asia) L.L.C.

Zhou Li  
+86(21)2401-8648 |  
zhou.li@goldmansachs.cn  
GS (China) Securities  
Company Limited

## Kstar (002518.SZ, Buy)

2Q26 preview: We forecast 2Q26 sales/GP/EBIT/NP at Rmb1,561mn/468mn/203mn/170mn (+28%/+34%/+45%/+20% yoy). Topline growth will likely be led by the energy storage products segment (>100% yoy sales growth in 2Q26 per GSe) given strong residential and C&I (commercial & industrial) ESS demand from Europe, Australia, and emerging markets with a low base in 1H25. We expect data center product segment sales to grow by >20% yoy in 2Q26, supported by strong overseas UPS ODM shipment and a gradual recovery of domestic data center construction demand. Meanwhile, solar inverter sales will see severe yoy contraction given the domestic solar installation weakness, in our view. We also model yoy and qoq improvement for both GPM and OPM at 30.0%/13.0% as overseas sales mix increases, but we model NP to grow slower after baking in \~Rmb20mn FX losses during the quarter due to CNY appreciation.

## Key debates and watchpoints:

1. Investors are worried that UPS will quickly be replaced by 800VDC products which is a key overhang for the share price and trading multiple, but we have been arguing the global UPS demand should remain intact in the mid term. Recent evidence includes: (1) Kstar's production line for large-power UPS (mainly for AI data centers) has been running at close to full utilization rate since May 2026 and they are expanding capacity by converting the ones for solar inverters to manufacture UPS; and (2) company has made much new progress in the overseas market so far this year, such as working with a new Taiwanese customer on supplying integrated power distribution solutions (including BESS, or battery energy storage system), getting certified by a new Japanese customer and a new European customer on supplying UPS systems as part of these 2 new customers' modular data center solutions, and winning a >Rmb200mn order from a new colocation customer for the UPS at a European data center project that will be rent to a major US hyperscaler. Going forward, we believe new customer wins and overseas orders will be key to monitor, and solid UPS sales growth in 2H26E and 2027E as confirmed by quarterly earnings could ease investor concerns and trigger a re-rating on the stock.

2. In our opinion, any commercialization update on 800VDC products will be the one of most important catalysts for the share price and valuation multiple, potentially showcasing that Kstar is able to remain globally competitive and ride through the upcoming technology shift from AC to 800VDC architecture that will start to happen at scale from 2H27 the earliest, in our view. For context, Kstar launched its AC-800VDC power conversion modules in May 2026, and targets to launch its 800 VDC systems (i.e. 800VDC power racks) and send to several overseas customers for onsite testing in 3Q26E, before receiving small batch orders for 800VDC products around as early as end-2026. We continue to be constructive on Kstar's positioning on 800VDC given its solid power conversion technology and manufacturing know-how, proven data center project track records, as well as trusted relationships with global electricals giants.

3. On the ESS segment, demand from Europe, Australia, Middle East, and SEA has been robust in 1H26, per company. That said, as investors find it hard to model future growth rates for residential/C&I ESS, which has a much shorter business cycle vs.

utility-scale projects, any positive commentaries or guidance from management or new long-term orders will be helpful to justify the growth sustainability for Kstar's overseas ESS business.

Earnings and TP changes: We revise down 2026E net income forecasts by $2\%$ mainly to factor in the FX headwinds, but we keep 2027-30E net income forecasts largely unchanged given Kstar's solid customer progress in the global data center supply chain. Accordingly, our TP remains at Rmb67.0, still based on 26x 2028E P/E discounted back to 2026E with $11\%$ CoE. Maintain Buy with the stock trading at an attractive evaluation of 23x/16x 2026/27E P/E with $56\% / 43\%$ earnings growth.

## Kehua (002335.SZ, Neutral)

2Q26 preview: Post market close on Jul 13, 2026, Kehua pre-announced 1H26 net income in the range of Rmb365mn\~390mn (+50%\~60% yoy) with most of the growth driven by the one-off gains from the sales of a data center asset as recurring NI was only Rmb230\~254mn (+3%\~14% yoy). Per company announcement in Apr, the one-off gain (before-tax) was roughly Rmb147mn. Implied 2Q26 net income was Rmb287mn\~312mn (+65%\~79% yoy), but the 2Q26 recurring NI was Rmb165mn\~189mn (+2%\~17%), below our expectation. Following the announcement, we now forecast 2Q26 sales/GP/EBIT/NP at Rmb2,793mn/609mn/155mn/300mn (+11%/+7%/-9%/+72% yoy). We believe the sales growth will be mostly driven by (1) the data center products segment as data center capacity buildout is improving in China with easing domestic AI chip supply constraints; also Kehua is penetrating into domestic CSP supply chain, gaining >Rmb100mn orders from Alibaba on modular power distribution products and CDU (coolant distribution unit) in 1H26; and (2) the overseas energy storage segment as Kehua takes orders from local ESS integrators from diverse regions such as Bulgaria and India, and ramps up its PCS (power conversion system) supply for international integrators. On the other hand, domestic energy storage and solar inverters will likely be major drags on growth and margins due to solar industry weakness and higher lithium costs, and we expect muted growth for the macro-sensitive smart power segment as well. All in, we expect 2Q26 GPM to decline yoy from 22.5% to 21.8% as the high-margin overseas energy storage business is offset by the intense competition in the domestic data center products segment.

## Key debates and watchpoints

1. Kehua continues to be viewed as a proxy for domestic hyperscaler capex. While domestic data center buildout activities are picking up sequentially in 2Q26 based on our industry checks, investors are looking for signs of accelerating industry capex and hyperscaler tending activities into 2H26E-2027E. Kehua's orders directly from major hyperscalers such as Tencent and Alibaba as well as indirectly from colos in China and in SEA are key to monitor to gauge its data center products segment growth ahead, although domestic margins are tough given intense competition and strong pricing pressure from the domestic hyperscalers.

2. We believe the market currently has limited expectation on Kehua gaining significant breakthroughs in the global (especially US) data center supply chain in the near term, based on our conversations with investors, so any updates on this front could potentially drive the share price as the company has been in touch with several global customers and is trying to get its power distribution and CDU certified since 2025.

3. While we model strong overseas energy storage sales growth in 2026E from an easy base, guidance on 2027E growth and margins is key to watch given the increasing number of Chinese companies getting into the global utility-scale ESS market which might lead to intense competition. Geopolitical tensions such as potential restrictions on Chinese inverters in Europe and US also raise investor concerns on the export sustainability of Kehua's utility-scale ESS products.

Earnings and TP changes: We revise down our 2026-30E net income forecasts by 5% to reflect the cost pressure in the domestic energy storage business as well as higher SG&A expense as a result of the 2026 ESOP plan recently granted in early Jul, partially offset by the one-off gains in 2Q26 and solid overseas energy storage progress. Accordingly, our 12m TP moves to Rmb35.0 (vs. Rmb37.24 previously), still based on 30x 2027E P/E. Maintain Neutral.

## Megmeet (002851.SZ, Neutral)

## 2Q26 preview: We forecast 2Q26 sales/GP/EBIT/NP at

Rmb3,300mn/759mn/173mn/140mn (+40%/+52%/+256%/+110% yoy). We expect server power supplies sales will ramp up in 2Q26 and drive >60% yoy sales growth for the overall power supplies segment as company noted during 1Q26 call that they haven been receiving orders for GB200/GB300. Home appliance control will also be a major growth contributor in 2Q26, growing >40% yoy in sales on the back of a low base in 2Q25 when the intermittent rainfall affected air-conditioner demand in India, in our view. According to multiple news reports (link 1, link 2), the AC industry sales in India saw strong growth this summer driven by the extended summer heat wave. Meanwhile, we model still soft growth for the EV components business during the quarter as a result of the broader domestic EV sales weakness. We look for 32% yoy SG&A expense growth as the company continues to invest heavily on R&D for future-gen products, sales & marketing to gain more customer access, and capacity expansion. That said, our strong NP growth forecasts (from a low base) are based on favorable product mix changes towards higher-margin businesses offsetting the raw material cost inflation pressure as well as slight improvement on operating leverage.

## Key debates and watchpoints:

1. With the shipment of Vera Rubin racks ramping up in 2H26E, we await management comments on Megmeet's latest updates (e.g. wallet share allocation) for the 18.5kW PSU / 110kW power shelf. Megmeet management noted during 1Q26 earnings call that they are aligned with global peer in terms of overall product development, sampling and verification timeline. Meanwhile, we believe the server power supplies sales in 2026E will still mainly be supported by GB200/GB300 related products, and it will be key to watch if there is any new customer win for the 5.5kW products.

2. We note there were more than a half dozen brands showcasing their 800VDC sidecar prototypes during Computex Taiwan exhibition in June 2026, so the commercialization of 800VDC products is key to watch to determine Megmeet's industry positioning in 2028 and beyond. Management previously guided they would receive more sampling orders for 800VDC power racks around mid-2026E.

3. As the company recently announced a broad-based ASP increase across most product segments due to raw material price cost inflation, it would be key to learn about customers' feedback and how the price adjustment affects company's expectations on growth and margins for different product segments. At the moment, we believe that the core control & automation businesses will see some pressure on volume growth post the price hike especially in the pricing-sensitive domestic market, while server power supplies will likely see smoother pass-through to overseas customers.

4. Megmeet filed for a HK IPO application in June 2026: Some investors see this as a sign that the company is confident in share gains in the future, while some question whether there are sufficient orders to support the future capacity.

Earnings and TP changes: We keep our 2026-30E net income largely unchanged, as our higher home appliance control sales forecasts are mostly offset by the lowered EV components revenue. Our 12m TP remains at Rmb112.0, still based on 32x 2028E P/E discounted back to 2026E with $11\%$ CoE. Maintain Neutral.

Investment thesis, valuation methodology and risks

## Kstar (002518.SZ, Buy)

Investment thesis: Kstar specializes in electric power conversion technology, providing data centers and energy storage systems (ESS) with a constant and stable power supply. It has achieved the largest UPS (uninterruptible power supply) shipments in China for more than 20 years. For Kstar, we expect the company to deliver solid revenue/net income growth, mainly driven by: (1) overseas AIDC customer expansion and product innovation (including high-power UPS, 800 VDC, SST etc.) serving broader regions including the North American market; (2) domestic data center revenue growth pick-up, riding on increased capex from both SOE and POE hyperscalers and expanding customer base in the domestic data center market, and (3) overseas ESS business recovery benefiting from channel inventories normalization and C&I ESS demand. We are Buy-rated on the stock considering the attractive P/E valuation on its long-term growth profile and better margin and returns vs. peers.

Price target risks & methodology: Our 12m target price of Rmb67.0 is based on 2028E P/E of 26x discounted back to 2027E at 11% CoE. Key downside risks: (1) Lower-than-expected US ODM order growth; (2) Slower new product launches especially 800V DC products; (3) Lower-than-expected overseas ESS growth and margin.

<table><tr><td>002518.SZ</td><td>12m Price Target: Rmb67</td><td colspan="2">Price: Rmb33.53</td><td colspan="2">Upside: 99.8%</td></tr><tr><td>Buy</td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: Rmb19.5bn / $2.9bn</td><td>Revenue (Rmb mn) New</td><td>5,270.3</td><td>7,137.4</td><td>9,144.3</td><td>11,336.1</td></tr><tr><td>Enterprise value: Rmb18.9bn / $2.8bn</td><td>Revenue (Rmb mn) Old</td><td>5,270.3</td><td>7,266.2</td><td>9,345.6</td><td>11,378.4</td></tr><tr><td>3m ADTV :Rmb852.3mn/ $125.5mn</td><td>EBITDA (Rmb mn)</td><td>731.2</td><td>1,181.2</td><td>1,588.0</td><td>2,021.8</td></tr><tr><td>China</td><td>EPS (Rmb) New</td><td>0.99</td><td>1.55</td><td>2.22</td><td>2.86</td></tr><tr><td rowspan="2">China Industrial Tech &amp; Machinery</td><td>EPS (Rmb) Old</td><td>0.99</td><td>1.59</td><td>2.23</td><td>2.86</td></tr><tr><td>P/E (X)</td><td>31.1</td><td>21.6</td><td>15.1</td><td>11.7</td></tr><tr><td>M&amp;A Rank: 3</td><td>P/B (X)</td><td>3.7</td><td>3.6</td><td>3.1</td><td>2.6</td></tr><tr><td rowspan="2">Leases incl. in net debt &amp; EV?: No</td><td>Dividend yield (%)</td><td>1.5</td><td>2.1</td><td>3.3</td><td>4.3</td></tr><tr><td>CROCI (%)</td><td>18.2</td><td>23.9</td><td>25.8</td><t

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
