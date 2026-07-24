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
CHINA CRO & CDMO

# 2Q/1H26 Preview: Resilient Order Momentum to Support Further Earnings Upgrades and Re-rating Sustainability

Chinese CDMOs (+27.9%) have led the Healthcare rebound (+11.8%) over the past month, outperforming the MXCN (+7.6%), in line with our preferred positioning for 2026 (our note in Feb and May). Beyond sector rotation into healthcare from AI/Tech, sentiment has been underpinned by resilient 2Q fundamentals, including sustained demand across key modalities such as GLP-1 and ADCs, continued NHP price inflation amid robust domestic clinical trial activity, and incremental demand catalysts from active global M&A and growing adoption of AI-driven drug discovery (AIDD). Importantly, despite ongoing geopolitical headlines, we have observed limited tangible impact on customer demand or project execution to date.

CDMO performance has gradually shifted from an alpha-driven story in 1H26 toward a broader beta-driven recovery, although companies with superior earnings durability and GLP-1 exposure continue to lead the outperformance, including WuXi AppTec H (+22%/+59% in 1M/YTD) and Asymchem H (+29%/+70%). At the same time, the market has increasingly rewarded companies delivering positive estimate revisions and improving order trends, as illustrated by Pharmaron H, which rebounded c.54% in 1M following stronger-than-expected order growth (+30% y/y overall orders; CDMO +50% y/y).

We believe the sustainability of the recent re-rating will hinge on continued earnings delivery, including resilient order intake (see Exhibit 2), commercial project conversion, and potential upward revisions to FY26 expectations. We remain constructive on the sector, and expect the technology depth, execution track record, and global delivery footprint of leading Chinese CDMOs to outweigh FX headwinds (USD/CNY down \~5.9% in 2Q26, versus -4.8%% in 1Q, see Exhibit 4) and geopolitical noise over the medium term. Ultimately, earnings revisions remain the primary driver of share-price returns, while valuation multiples are increasingly linked to the sustainability of earnings growth over the next 2–3 years. We revise up adjusted NP estimates across some of our coverage by 5%/10%/6% for FY26-28e and raise our TP by 5% on average.

Into 2Q earnings, we expect investors to focus on: WuXi AppTec (first to report on Aug 3rd)—GLP-1-driven backlog conversion (see peptide export data Exhibit 5), growth beyond peptides, and potential earnings upgrades; Asymchem—order intake across GLP-1, ADC, and oligonucleotide platforms; Pharmaron—scope for

Chris Pan, CFA
+852-2978-7993 | chris.pan@gs.com
GS (Asia) L.L.C.

Ziyi Chen
+852-2978-0526 | ziyi.chen@gs.com
GS (Asia) L.L.C.

Linhai Zhao, Ph.D.
+852-3966-4059 | linhai.zhao@gs.com
GS (Asia) L.L.C.

further estimate revisions following stronger CDMO order growth; Tigermed—order recovery from both domestic biotech and multinational pharma clients; and GenScript— more color on AIDD-related demand and full-year guidance.

## Investor feedback and key things to watch in 2Q26 earnings

Exhibit 1: Summary of investor feedback, GS view, and key things to watch for CRO/CDMO

<table><tr><td>Company (Ticker, Rating)</td><td>Earnings Release Date</td><td>Investor feedback</td><td>GS view</td><td>Key things to watch (earnings / near-term)</td></tr><tr><td>WuXi AppTec (2359.HK/603259.SH) B*/B*</td><td>3-Aug</td><td>Investors are increasingly focused on the specific product and pipeline drivers that can sustain growth beyond 2026, given crowded positioning and strong share-price performance. While near-term execution has improved meaningfully, conviction remains tied to sustained multi-quarter delivery, particularly around GLP-1 backlog conversion and growth beyond peptides. Geopolitical headlines continue to drive share-price volatility, although investors generally acknowledge limited observable impact on customer behavior to date.</td><td>We expect 2Q26 results to further reinforce earnings visibility, supported by continued order execution, GLP-1 demand across both peptide and small-molecule programs, and diversified growth beyond GLP-1. A rising mix of late-stage and commercial projects should continue to support margin resilience. We also see potential for a guidance upgrade, which could further underpin share-price outperformance.</td><td>1) Guidance upgrade in 2Q; 2) Order intake trend and backlog conversion; include GLP-1 / TIDES contribution; 3) margin trajectory; 4) Growth diversification beyond GLP-1</td></tr><tr><td>Pharmaron (3759.HK/300759.SZ, B/N)</td><td>20-Aug</td><td>Investor sentiment has turned increasingly constructive following stronger-than-expected order growth in 2Q, particularly in CDMO (+50% y/y). Despite the recent rebound, Pharmaron remains viewed as a relative laggard within the CDMO recovery trade, with investors debating whether stronger order trends can translate into earnings upgrades and a possible guidance revision.</td><td>We see improving earnings visibility driven by stronger small-molecule CDMO demand under the CRDMO model. While margins may face near-term pressure from RMB appreciation and competition in clinical development, CDMO growth is tracking ahead of expectations. LLY&#x27;s partnership strengthens Pharmaron&#x27;s strategic positioning within the domestic GLP-1 supply chain, with longer-term optionality extending beyond its immediate revenue contribution.</td><td>1) Disclosure on commercial model and order volumes; 2) Timing of orforglipron China approval; 3) Margin sustainability post-prelims; 4) Broader GLP-1 related capacity utilization.</td></tr><tr><td>Asymchem (6821.HK/002821.SZ, B/N)</td><td>24-Aug</td><td>The debate has increasingly shifted toward peptide order visibility and utilization of the company&#x27;s aggressive TIDES capacity expansion. Investors remain constructive on structural GLP-1 demand, although questions remain regarding utilization ramp, margin sustainability, and whether current valuation already reflects much of the medium-term opportunity.</td><td>We remain positive on operating momentum, supported by expanding exposure to peptides, ADCs and oligonucleotides. Visibility on peptide and oligo pipelines continues to improve, supporting ongoing capacity expansion and future utilization. We also see early signs of stabilization in traditional small-molecule demand, providing additional support to earnings growth and margin expansion</td><td>1) Commercial revenue mix; 2) Utilization ramp and margin progression; 3) Visibility on GLP-1-related projects</td></tr><tr><td>WuXi XDC (2268.HK, B)</td><td>24-Aug</td><td>Following the YTD correction, valuation concerns have moderated and investor attention has shifted toward commercial execution. Key debates focus on late-stage ADC conversion, commercial-order visibility, and the pace of ramp-up at the Singapore facility as proof points for medium-term growth.</td><td>We continue to view Wuxi XDC as one or the clearest beneficiaries of the ADC cycle. ADC demand remains healthy, supported by improving industry sentiment and increasing clinical activity. We see current backlog and project progression as supportive of growth objectives, while Singapore represents an important medium-term capacity and commercial expansion opportunity. Any near-term margin volatility during the ramp-up phase should be transient</td><td>1) Orders / backlog conversion (late-stage ADCs); 2) Singapore ramp-up (utilization, initial orders) and margins during capacity absorption; 3) Client concentration &amp; pipeline progression;</td></tr><tr><td>WuXi Biologics (2269.HK, N)</td><td>TBA</td><td>Investors remain focused on commercial execution and margin sustainability, with debate centered on PPQ conversion, commercial manufacturing ramp-up, and overseas delivery capabilities. Greater evidence of revenue quality and scalability remains necessary to support a broader re-rating.</td><td>We expect growth to accelerate in 2027 onwards as project onboarding normalizes and commercial-stage programs continue to ramp. Increasing contribution from milestone and royalty income should support structurally higher margins and improve earnings quality. We view execution on PPQ conversion, commercial delivery, and project additions as the key factors required to rebuild investor confidence.</td><td>1) New order momentum; 2) Capacity utilization; 3) 2026 revenue growth outlook.</td></tr><tr><td>Tigermed (3347.HK/300347.SZ, B/B)</td><td>28-Aug</td><td>Investors acknowledge improving order momentum, but confidence remains tempered by recent earnings misses, AI-related investment spending, pricing pressure, and uncertainty surrounding the CSRC investigation. The key debate is whether accelerating order growth can sustainably translate into earnings recovery.</td><td>We see early evidence of demand recovery, supported by accelerating order intake from domestic innovative biopharma companies and improving activity from multinational clients. Order growth accelerated through April-May, while pricing trends have begun to stabilize. Near-term margins may remain under pressure from legacy contracts and AI investment, but improving scale should gradually drive operating leverage.</td><td>(1) Sustainability of MNC China-only POC trial momentum; 2) RFP conversion and backlog build; 3) Results of the CSRC investigation; 4) Pricing recovery trajectory</td></tr></table>

## Order momentum and FX impact remain top investor focus

Exhibit 2: We expect new order momentum to continue in 2Q, with market expectation at range of $+20 - 30\%$ CDMO new order and backlog growth summary

<table><tr><td colspan="10">Note: 1) * for continuing operations; 2) new order based on backlog within 3 years for WuXi Biologics; 3) cal. denotes new order based on calculation, rest is per company</td></tr><tr><td>New order growth, y/y</td><td>2023</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td><td>1H26</td></tr><tr><td>WuXi AppTec</td><td>-1% (cal.)</td><td>30%*</td><td>25%*</td><td>12%*</td><td>18%*</td><td>n.a.</td><td>n.a.</td><td>ex-FX 25%*</td><td></td></tr><tr><td>WuXi Biologics</td><td>15% (cal.)</td><td>13%-15%*</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td></td></tr><tr><td>WuXi XDC</td><td>n.a.</td><td>75% (cal.)</td><td>n.a.</td><td>1H25 48%</td><td>n.a.</td><td>2H25 29%(cal.)</td><td>41%</td><td>n.a.</td><td></td></tr><tr><td>Asymchem</td><td>n.a.</td><td>20%</td><td>Maintain themomentum</td><td>n.a.</td><td>9M25double digit</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td></td></tr><tr><td>Tigermed</td><td>-19%</td><td>7%</td><td>20%</td><td>Aug YTD midteens</td><td>9M25mid teens</td><td>n.a.</td><td>21%</td><td>High doubledigit</td><td></td></tr><tr><td>Pharmaron</td><td>n.a.</td><td>&gt;20%</td><td>10%</td><td>1H25 10%</td><td>9M25 13%</td><td>n.a.</td><td>14%</td><td>30%</td><td>30%</td></tr><tr><td>Lab service</td><td>n.a.</td><td>15%</td><td>10%</td><td>1H25 10%</td><td>9M25 12%</td><td>n.a.</td><td>12%</td><td>20%</td><td>20%</td></tr><tr><td>CMC</td><td>n.a.</td><td>35%</td><td>10%</td><td>1H25 20%</td><td>9M25 20%</td><td>n.a.</td><td>13%</td><td>50%</td><td>50%</td></tr></table>

<table><tr><td>Backlog growth, y/y</td><td>2023</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td></tr><tr><td>WuXi AppTec</td><td>7%</td><td>47%*</td><td>47%*</td><td>1H25 37%*</td><td>9M25 41%*</td><td>n.a.</td><td>29%* or ex-FX 34%*</td><td>24%* or ex-FX 29%*</td></tr><tr><td>WuXi Biologics</td><td>6%</td><td>11%*</td><td>n.a.</td><td>1H25 29%*</td><td>n.a.</td><td>n.a.</td><td>24%*</td><td>n.a.</td></tr><tr><td>WuXi XDC</td><td>82%</td><td>71%</td><td>n.a.</td><td>1H25 58%</td><td>n.a.</td><td>n.a.</td><td>50%</td><td>n.a.</td></tr><tr><td>Asymchem</td><td>n.a.</td><td>&gt;20%</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>32%</td><td>n.a.</td></tr><tr><td>Chemical macromolecule</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>1H25 90%</td><td>n.a.</td><td>n.a.</td><td>128%</td><td>n.a.</td></tr><tr><td>Biological macromolecule</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>1H25 60%</td><td>n.a.</td><td>n.a.</td><td>56%</td><td>n.a.</td></tr><tr><td>Drug products</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>1H25 35%</td><td>n.a.</td><td>n.a.</td><td>49%</td><td>n.a.</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 3: FX headwinds from RMB strength largely expected by the market

<table><tr><td colspan="3">FX Impact</td></tr><tr><td>Company name</td><td>Full year guidance</td><td>1Q26 / 1H26</td></tr><tr><td>WuXi Apptec</td><td>-18-22% y/y growth for continuing business (22-26% at constant currency/ccy)Effective hedging in 1Q in place to secure certainty for full year guidance delivery</td><td>1Q26: FX at ~1-2ppt gross margin headwind; Excluding Fx, GM stays on par vs. 2H25.</td></tr><tr><td>WuXi Bio</td><td>Full year revenue + 13-17% versus 16-20% at ccy</td><td>Revenu impact likely at 4-5% and 1-2% on GPM (GSe)</td></tr><tr><td>WuXi XDC</td><td>~35% growth on US$ term, FX impact likely 2-3%.</td><td>Revenue Impact likely 4-5% (GSe)</td></tr><tr><td>Asymchem</td><td>Revenue + 19-22% y/y considering FX impact</td><td>For 1Q, margin improve by 0.5%, if ccy +1.7%. FX loss of Rmb126mn versus 4mn FX gain in 1Q</td></tr><tr><td>Pharmaron</td><td>+ 12-18% growth y/y, with 3% FX embedded</td><td>1Q: Gross margin declined y/y (32.6% vs 33.7%), mainly reflecting FX headwinds (~150bps impact),</td></tr></table>

Source: Company data, GS Global Investment Research

## Exhibit 4: USD/CNY down \~5.9% in 2Q26 average vs 2Q25 average

![](images/370901a511306ee668350a1a5616130bec1c391b3beaef85508530114dac292f.jpg)  
Source: Bloomberg

Strong peptide export supports our confidence in WuXi Apptec's TIDEs growth in

Quarterly value for peptide export vs WXAT TIDES sales (in Rmbmn)

## 2Q

Exhibit 5: The peptide export grew +137% y/y in 2Q26  
![](images/4090a4fcefe8e73d9221ca1480557c24b26c12fb9858cc4fa5c25b9c154958de.jpg)  
Source: China Customs, Company data, Wind, GS Global Investment Research

## Exhibit 6: The peptide export reached Rmb3.3bn in 2Q26

![](images/31c638a429b19f88b98416e8fe953ae91684c7af5c5da39db57a2d423bbfb148.jpg)  
Source: China Customs, Company data, Wind, GS Global Investment Research

Exhibit 7: We expect a guidance upgrade from WuXi AppTec to provide further support for share-price outperformance

<table><tr><td></td><td>2023Jan-Mar</td><td>Apr-Jun</td><td>Jul-Sep</td><td>Oct- Dec</td><td>2024Jan-Mar</td><td>Apr-Jun</td><td>Jul-Sep</td><td>Oct- Dec</td><td>2025Jan-Mar</td><td>Apr-Jun</td><td>Jul-Sep</td><td>Oct- Dec</td><td>2026Jan-Mar</td><td>Apr-May</td><td>The latest guidance</td></tr><tr><td>Samsung Bio</td><td>—</td><td>▲</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>—</td><td>FY26 revenue growth of +15-20% y/y</td></tr><tr><td>WuXi AppTec</td><td>—</td><td>—</td><td>—</td><td>▼</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>▲</td><td>—</td><td>—</td><td>FY26 revenue growth of 18-22% (or 22-26% at constant currency) for continuing operations</td></tr><tr><td>WuXi Bio</td><td>—</td><td>—</td><td>—</td><td>▼</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>—</td><td>FY26 revenue growth guidance of 13-17% y/y (16-20% at constant currency)</td></tr><tr><td>WuXi XDC</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>—</td><td>35% group revenue growth for FY26 on a constant-currency, like-for-like basis (including BioDlink) or 40% on a pro forma basis</td></tr><tr><td>Pharma

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
