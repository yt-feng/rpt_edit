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
# NAND Industry Outlook: Diverging Trends

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>Rmb300.00</td><td>Rmb673.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td></td><td></td></tr><tr><td>Price Target</td><td>US$155.00</td><td>US$400.00</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td></td><td></td></tr><tr><td>Price Target</td><td>NT$2,248.00</td><td>NT$2,588.00</td></tr></table>

AI continues to create shortages in the NAND industry into 2027, while supply and demand dynamics depend on supply discipline moving into 2028 and beyond. We still like suppliers for LTA downside protection and enhanced shareholder returns, and are starting to see consumer pricing plateau.

What's changed? We update our global NAND supply and demand forecast for 2026-27 and conducted a scenario test on greenfield expansion vs. AI demand growth for 2028. Our calculation shows significant shortages should persist into 2027. Moving into 2028, node migration and greenfield expansion may ease some supply tightness (-5% shortage if 60% YoY AI NAND growth with current base case capacity expansion), while in a bear case scenario where both China restrictions and supply discipline ease, there is potential risk of oversupply.

Bifurcation – AI vs. consumer: We see overall server demand remaining strong as LTAs have provided downside protections on pricing. On the consumer side, inventory levels have increased at module makers and distributors, and smartphone and PC customers are facing increasing pressure on the volume vs. margin trade-off. This is not new to the market, but we have begun to see actual order cuts after 2Q26 price hikes, indicating pricing for consumer products might hit a ceiling very soon while volume remains muted as suppliers shift capacity to AI.

Stock implications: We remain bullish on the memory cycle and continue to like supplier names with LTA supporting valuation expansion and shareholder returns. Tactically, we prefer DRAM over NAND due to better LTA terms, higher demand visibility, supply discipline capped by EUV and a potential HBM4E capacity squeeze. In NAND, we prefer suppliers over module makers, reflecting margin durability.

Global perspective: In DRAM, Samsung Electronics is Asia Tech team's Top Pick for its market leadership and potentially stronger shareholder returns. In NAND, Kioxia is our Japan Semi team's Top Pick for solid FCF generation and shareholder return potential while Macronix is our GC Semi team's Top Pick. We remain OW on Micron, SK hynix and SanDisk amid a durable memory cycle, as well as Fadu, a key eSSD controller supplier to SanDisk. We raise our SIMO PT to reflect the eSSD opportunity. We remain EW on Longsys and Phison on concerns around muted volume growth but raise our PTs on stronger pricing and margin assumptions.

<table><tr><td colspan="2">Duan Liu</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Duan.Liu@morganstanley.com</td><td>+852 2239-7357</td></tr><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="2">Shawn Kim</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Shawn.Kim@morganstanley.com</td><td>+44 20 7677-1018</td></tr><tr><td colspan="2">Cindy Huang</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Cindy.Huang@morganstanley.com</td><td>+44 20 7425-2915</td></tr><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Charlie Chan</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Charlie.Chan@morganstanley.com</td><td>+886 2 2730-1725</td></tr><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Joseph Moore</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Joseph.Moore@morganstanley.com</td><td>+1 212 761-7516</td></tr><tr><td colspan="2">MS MUFG SECURITIES CO., LTD.+</td></tr><tr><td colspan="2">Kazuo Yoshikawa, CFA</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Kazuo.Yoshikawa@morganstanleymufg.com</td><td>+81 3 6836-8408</td></tr><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Daniel Yen, CFA</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Daniel.Yen@morganstanley.com</td><td>+886 2 2730-2863</td></tr><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC, SEOUL BRANCH+</td></tr><tr><td colspan="2">Ryan Kim</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Ryan.G.Kim@morganstanley.com</td><td>+82 2 399-4939</td></tr><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Mason Wayne</td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Mason.Wayne@morganstanley.com</td><td>+1 212 761-6012</td></tr><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Tiffany Yeh</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Tiffany.Yeh@morganstanley.com</td><td>+886 2 7712-3032</td></tr><tr><td colspan="2">S. KOREA TECHNOLOGY</td></tr></table>

Asia Pacific
Industry View Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Global Perspectives

## Sandisk/Micron

## Joseph Moore

We remain OW on Sandisk and MU, as supply demand outcomes continue to look compelling for both NAND and DRAM. With AI now the principal driver of memory bits and little to no inventory across the supply, the biggest risk to memory stocks is a broader AI capex slowdown, which we do not expect to peak in the near term, supporting a path to higher earnings power well beyond 2027 (when consensus currently assumes pricing will begin to normalize). We expect continued upward revisions to estimates, and at <10x P/E for both SNDK and MU multiples should still have room to benefit from extended visibility. LTAs are part of what's enabling that higher level of visibility, and are symptomatic of a market that could should stay tight for another 2-3 years. Meanwhile, MU and Sandisk should continue to be attractive capital return stories, as we expect both to pursue meaningful buybacks in 2027.

## KIOXIA

## Kazuo Yoshikawa

We maintain KIOXIA as our Top Pick within our Japan semiconductor coverage, reflecting solid FCF generation and shareholder return potential.

KIOXIA appears well positioned to capture AI-driven storage demand with a broad SSD lineup. The CM Series addresses high-throughput, low-latency KV cache needs for inference AI, while the GP Series targets Super High IOPS applications that can complement HBM. The LC Series supports large-scale AI storage demand with 245TB QLC SSDs, with mass-production shipments already underway.

On capital allocation, KIOXIA plans to use FCF for both growth investments and shareholder returns. We see scope for stronger returns, supported by expected annual FCF generation of ¥4.0-5.0trn in FY3/27-3/28 even under our conservative ASP assumptions, and management's indication that a substantial portion of excess accumulated FCF could potentially be returned to shareholders.

KIOXIA is also progressing LTA discussions, mainly with data center and enterprise customers. LTAs are expected to cover more than 50% of CY27 shipments, while CY28 coverage is likely to remain around 50% to preserve flexibility.

## Samsung Electronics/SK hynix

## Shawn Kim

We maintain OW ratings for both Samsung Electronics (Top Pick) and SK hynix as key beneficiaries to AI compute and agentic AI trends (see Agentic AI – The Surge Begins). We estimate more than 20-30% DRAM price hikes in 3Q26, enough to keep the YoY rate of change accelerating. Pricing power is translating into earnings revisions that in turn support P/E stability, at 5.2x 2027e earnings.

However, we are mindful of the rate of change that still matters for memory stocks. With YoY pricing likely to plateau in 4Q26 vs. supply discipline visibility in 2028, we believe

stocks might lack near-term cyclical catalysts until supply and demand dynamics become more clear into 2028 and beyond. That said, multiples could continue to re-rate on the back of favorable LTAs.

## Longsys

## Duan Liu

We have significantly raised our estimates for Longsys on better-than-expected pricing trends and high conviction levels on 2027 shortages. We expect Longsys's long-term margin profile to improve due to its better product mix. Its TCM business model will likely bring a more stable margin profile over the long term (25-35%) as inventory pressure is shifted to customers, and the company's in-house controller development could further increase the value add on firmware and customized services. We are slightly concerned about muted volume growth due to suppliers' shifting capacity to CSP customers, which should cap near-term volume growth, but this should be well understood by the market and already in the price.

## Phison

## Charlie Chan

2Q26 preliminary results were a strong beat vs. estimates, driven by more resilient pricing hike intervals and shipments than expected. 3Q26 is expected to be the peak quarter of the year, supported by additional supply support from Kioxia's dummy die, which could drive around 20% QoQ revenue growth and a better-than-feared flat QoQ margin. However, this strength appears cyclical rather than sustainable; gross margin expansion is still expected to peak around 2Q26–3Q26 as low-cost NAND inventory is depleted and higher-cost supply begins to flow through under FIFO accounting. By 4Q26, emerging weakness in consumer tech and a more moderate pricing environment are expected to drive revenue down around 20% QoQ, with margins normalizing to roughly 50%. Although the better 2026 pricing environment supports stronger-than-expected profitability into 2027, this upside is partially offset by continued R&D investment and broader structural risks, including constrained NAND supply, weakening consumer SSD demand, limited raw NAND supplier support, modest eSSD revenue contribution of only around 10–20% for most Asia-based SSD vendors and hyperscalers' tendency to purchase directly from NAND fab owners or negotiate long-term supply agreements, which may limit the long-term addressable market for module vendors such as Phison.

## SIMO (PT increases to US\$400 from US\$155)

## Tiffany Yeh

For FY2026, the company expects record revenue, sequential growth every quarter, margin expansion, and an improving mix. Some important incremental growth vectors are: 1) Boot drive storage, where SIMO is expanding from current DPU boot-drive shipments into broader next-gen AI GPU/CPU platform content, including DPU, Ethernet, and NVLink-related switch opportunities. We expect boot drive and other SSD solutions to account for 23%/26% of SIMO's 2026e/2027e total revenue, see more detailed analysis in AI Module: Boot Drive Bottom-up Updates section.

2) Enterprise SSD / MonTitan: SIMO's enterprise SSD business, MonTitan, has started production with two customers. The company expects to add five more Tier 1 CSPs by late

2026 and targets MonTitan to contribute 5–10% of expanded 2026 revenue on an exit run-rate basis. However, as we see SIMO continuing to make progress, we expect its eSSD (MonTitan) business to account for 5%/13%/19% of SIMO's total revenue in 2026e/2027e/2028e, as besides off-the-shelf eSSD controllers, we also see the possibility for SIMO to customize eSSD controllers for CSPs in the long run.

3) Although overall consumer demand remains lukewarm, we continue to see SIMO gaining market share in mobile, PC and edge AI products even into 2H26. As a result, we raise our price target to US\$400 from US\$155, implying 23x 2027e EPS, above its historical average of 20x since 2019. We view this as justifiable as SIMO is diversifying into more AI-exposed areas. Overall, we expect to see continual upward inflection in SIMO's enterprise/AI storage strategy, with 2026 the first meaningful ramp year and 2027-28 as the scaling phase.

## Fadu

## Ryan Kim

We believe Fadu is gradually transitioning from a recovery story to a structurally scaling AI storage semiconductor story. Although the company remains relatively small in absolute revenue today, management commentary increasingly suggests the key uncertainty is shifting away from demand visibility and toward execution/ramp timing. Importantly, management now frames 2026 revenue of W300bn+ as effectively secured, supported by hyperscaler-related enterprise SSD controllers, while also guiding for meaningful operating leverage due to a controller-heavy mix and limited incremental SG&A. The broader debate is no longer whether hyperscaler exposure exists, but rather how far the company can penetrate AI-centric storage architectures over the next 3-5 years. The company believes it can eventually cover 3-4 of the top global hyperscalers through indirect and direct engagement models. If realized, this could materially expand both the revenue visibility and valuation frameworks vs. historical perceptions.

## Macronix, Winbond, GigaDevice

## Daniel Yen

For SLC/MLC NAND, we have seen supply tightness for a while with mainstream vendors existing the market and only a handful of legacy players able to maintain or even increase capacity. In addition, we are now seeing demand upside. High-density SLC NAND can support datacenter eSSD as they have fast reading and writing speeds (link). In addition, given the MLC NAND shortfall, enterprise HDDs are likely shifting to high-density SLC NAND. Enterprise HDDs previously used MLC NAND for firmware, hot data and defect mapping. We believe strong pricing momentum will continue into 4Q, following 50–60% increases in 3Q.

We remain OW on Macronix (Top Pick; SLC/MLC NAND), Winbond (SLC NAND) and GigaDevice (SLC NAND).

Exhibit 1: Order of Preference

<table><tr><td></td><td>Fadu440110.KQ</td><td>Macronix2337.TW</td><td>Winbond2344.TW</td><td>Silicon MotionSIMO.O</td><td>Kioxia285A.T</td><td>Samsung Electronics005930.KS</td><td>GigaDevice603986.SS</td><td>MicronMU.O</td><td>SK hynix000650.KS</td><td>SanDiskSNDK.O</td><td>Phison8292.TWO</td><td>Longsys301306.SZ</td></tr><tr><td>Rating</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Equal-Weight</td><td>Equal-weight</td></tr><tr><td>Trading Currency</td><td>KRW</td><td>TWD</td><td>TWD</td><td>USD</td><td>JPY</td><td>KRW</td><td>CNY</td><td>USD</td><td>KRW</td><td>USD</td><td>TWD</td><td>CNY</td></tr><tr><td>Price Target</td><td>150,000.0</td><td>220.0</td><td>288.0</td><td>400.0</td><td>110,000.0</td><td>381,000.0</td><td>888.0</td><td>1,200.0</td><td>2,600,000.0</td><td>1,750.0</td><td>2,588.0</td><td>673.0</td></tr><tr><td>Current Price</td><td>82,600.0</td><td>143.5</td><td>190.0</td><td>317.0</td><td>88,130.0</td><td>314,500.0</td><td>772.0</td><td>1,154.3</td><td>2,560,000.0</td><td>2,273.7</td><td>2,270.0</td><td>667.8</td></tr><tr><td>Upside/(Downside) (%)</td><td>82%</td><td>53%</td><td>52%</td><td>26%</td><td>25%</td><td>21%</td><td>15%</td><td>4%</td><td>2%</td><td>-23%</td><td>14%</td><td>1%</td></tr><tr><td>Market Cap (in USD mm)</td><td>2,565.2</td><td>8,149.8</td><td>24,992.1</td><td>10,649.9</td><td>300,468.2</td><td>1,449,7

[中间内容因长度限制已省略]

 your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The following companies do business in countries which are generally subject to comprehensive sanctions programs administered or enforced by the U.S. Department of the Treasury's Office of Foreign Assets Control ("OFAC") and by other countries and multi-national bodies: Samsung Electronics.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: S. Korea Technology

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/02/2026)</td></tr><tr><td colspan="3">Ryan Kim</td></tr><tr><td>Ecopro BM (247540.KQ)</td><td>U (03/20/2023)</td><td>W125,500</td></tr><tr><td>Fadu Inc (440110.KQ)</td><td>O (09/21/2025)</td><td>W76,000</td></tr><tr><td>Hanmi Semiconductor Co. Ltd. (042700.KS)</td><td>O (08/16/2024)</td><td>W219,500</td></tr><tr><td>HD Hyundai Electric Co Ltd (267260.KS)</td><td>O (03/25/2025)</td><td>W969,000</td></tr><tr><td>Isu Petasys Co. Ltd. (007660.KS)</td><td>O (02/03/2025)</td><td>W119,800</td></tr><tr><td>L&amp;F Co Ltd (066970.KS)</td><td>E (04/03/2025)</td><td>W106,700</td></tr><tr><td>Leeno Industrial Inc. (058470.KQ)</td><td>O (04/03/2025)</td><td>W75,100</td></tr><tr><td>Lotte Energy Materials Corp (020150.KS)</td><td>U (04/03/2025)</td><td>W39,200</td></tr><tr><td>LS Electric (010120.KS)</td><td>O (01/22/2026)</td><td>W236,500</td></tr><tr><td>POSCO FUTURE M (003670.KS)</td><td>U (04/03/2025)</td><td>W163,600</td></tr><tr><td>SK IE Technology (361610.KS)</td><td>U (04/03/2025)</td><td>W16,030</td></tr><tr><td>SK Square Co Ltd. (402340.KS)</td><td>O (05/06/2026)</td><td>W1,525,000</td></tr><tr><td>Wonik IPS Co Ltd (240810.KQ)</td><td>O (08/08/2025)</td><td>W131,600</td></tr><tr><td colspan="3">Shawn Kim</td></tr><tr><td>LG Display (034220.KS)</td><td>E (06/11/2025)</td><td>W10,980</td></tr><tr><td>LG Electronics (066570.KS)</td><td>E (04/07/2025)</td><td>W192,300</td></tr><tr><td>LG Innotek (011070.KS)</td><td>E (03/12/2025)</td><td>W874,000</td></tr><tr><td>Samsung Electro-Mechanics (009150.KS)</td><td>O (07/31/2025)</td><td>W1,926,000</td></tr><tr><td>Samsung Electronics (005935.KS)</td><td>O (11/18/2019)</td><td>W188,700</td></tr><tr><td>Samsung Electronics (005930.KS)</td><td>O (11/18/2019)</td><td>W286,000</td></tr><tr><td>SK hynix (000660.KS)</td><td>O (09/21/2025)</td><td>W2,187,000</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
