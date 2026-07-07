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
# Sanhua Intelligent Controls (002050.SZ): 2Q26 looks stable with commercial HVAC and liquid cooling as key growth drivers

We hosted an in-person meeting with Sanhua Board Secretary Zhimi Li on July 6. Overall, 2Q26 trends appear broadly in line with our expectations. HVAC components are trending positive in 2Q26E per company comments, vs. +2% yoy per GSe, with overseas demand outperforming domestic and commercial HVAC demand outpacing residential, although the segment remains pressured by domestic policy fade and normalization of North America demand after last year's high base. Auto thermal management products continued to grow in 2Q26E, with growth likely slightly weaker than or broadly in line with 1Q26 growth, consistent with our +13% yoy GSe for 2Q26.

Jacqueline Du  
+852-2978-1783 |  
jacqueline.du@gs.com  
GS (Asia) L.L.C.

We were encouraged by the stronger momentum in commercial HVAC, with cold-chain transportation highlighted as a key growth area. Liquid cooling also continues to progress, with management expecting revenue to grow $50\%$ yoy in 2026E and highlighting potential project breakthroughs in the AIDC space into 2H, where Sanhua is supplying multiple components.

Raw material cost pressure appears manageable, as HVAC component pricing is linked to copper prices, North American auto thermal management customer pricing is also linked to raw material movements, and European exposure is partly hedged. The company is also continuing to improve internal operating efficiency and reduce SG&A expenses, supporting OP margin improvement. 2Q26 may still see some FX losses, but management expects the impact to be smaller than in 1Q26.

## Our detailed takeaways are below.

HVAC components: Management indicated HVAC components should see a flattish 1H26E or likely positive 2Q26 performance (GSe: $2\%$ yoy), narrowing from the $6\%$ yoy decline in 1Q26, with overseas demand trending better than domestic and commercial HVAC outpacing residential.

Residential HVAC remains under pressure from last year's high base, normalization after pre-buy from North America market last year, and domestic policy fade. That said, higher energy-efficiency requirements in China should support new product launches, while Europe, India and Japan remain overseas growth opportunities, helped by hotter summers and still-rising AC penetration, as well as adjacent product opportunities.

Commercial HVAC: faster-growing, higher-margin opportunity; 2026E liquid-cooling revenue expected to grow $50\%+$ yoy. Commercial HVAC is growing well this year, with cold-chain transportation a highlight. In liquid cooling, Sanhua built a dedicated team last year and is expanding from primary-side (data center to CDU) microchannel products into higher-value secondary-side (CDU to server/chip) components including pumps, cold plates, valves and sensors. The company does not plan to make full CDU systems, but will supply components to players such as Vertiv and Envicool. Management highlighted potential project breakthroughs in self-designed ASIC server supply chains. Sanhua works directly with cloud customers on qualification, while shipments are mainly to server supply-chain manufacturers. Current products are mainly CDU internal valves and sensors, while future opportunities include cold plates on the server side. Management expects liquid-cooling revenue to grow $50\%+$ yoy in 2026E, reaching Rmb3bn revenue in 2026E vs Rmb2bn in 2025.

Auto thermal management: 2Q26E still growing; overseas shipment strength offsets China uncertainty. Auto thermal management revenue is expected to grow positively yoy in 2Q26E (GSe: 13% yoy), though growth may be similar to or weaker than 1Q26 growth of 15% yoy, with May-June demand improved versus April. Sanhua management believes domestic NEV industry retail sales could decline, but overseas vehicle shipments remain strong, especially from export-oriented OEMs such as Leapmotor, Geely and BYD. Tesla demand also showed some recovery in May-June versus 1Q26. Sanhua's 3Q26E production schedule appears busy, with some new products, including oil pumps and expansion valves, facing tight capacity. While management believes the company is internally prepared to achieve its 15-20% CAGR, external risks remain, including domestic demand, and overseas policy uncertainty and export tariffs uncertainty, where we forecast 12% yoy growth for the segment in 2026E and 16% CAGR in 2026-30E. Sanhua continues to shift from individual components toward integrated modules, supporting content-per-vehicle growth. New opportunities include sensors, sensor-cleaning valves, as well as oil pumps that are used in autonomous driving, as well as thermal management for in-car refrigerators. Annual price-downs remain normal, while they will continue to differentiate in technology and optimize cost internally. Raw material impact is roughly manageable, as North American customer pricing is linked to copper and aluminum, while European exposure is partly hedged.

The author would like to thank Zhou Li, Hao Chen, Zhihan Ye, and Junfang Zhang for their contributions to this report.

## Investment Thesis - Sanhua Intelligent Controls

Sanhua is a global leader in HVAC control & thermal management components. We like its growth potential in humanoid robot actuators on top of a solid market leadership position in its core business, and expect it to deliver 16%/17% revenue/net profit CAGR in 2025-30E. On the HVAC component segment, we believe the company is well positioned to deliver revenue growth above the residential HVAC industry, driven by commercial HVAC market share gain and ramp up in sensor products. On the EV thermal management segment, we believe the company's revenue growth will be driven by further global EV penetration increase and modest content value gain. In addition, we see humanoid robots as a significant long-term technology trend, with Sanhua likely to secure a key role in the supply chain, as a high visibility actuator assembler. Catalysts include technology advancement in humanoid robot functionality, volume production for humanoid robot big customers, and further EV penetration in Europe. However, we think the market has priced in a too bullish outlook for humanoid robots compared to rather a delayed timeline of Optimus production. We are Neutral/Buy-rated on Sanhua-A/H.

## Price Target Risks and Methodology - Sanhua Intelligent Controls

Valuation: Our 12m target price for Sanhua A/H is Rmb39.8/HK\$41.2, based on 2030E P/E of 25X, discounted back to 2026E with a COE of 9.5%.

Sanhua-A key upside/downside risks: (1) Faster/Slower-than-expected revenue contribution from humanoid robots; (2) Better/Worse-than-expected global EV sales; (3) Better/Worse-than-expected home appliance sales.

Sanhua-H key downside risks: (1) Slower-than-expected revenue contribution from humanoid robots; (2) Worse-than-expected global EV sales; (3) Worse-than-expected home appliance sales.

<table><tr><td>002050.SZ</td><td>12m Price Target: Rmb39.80</td><td>Price: Rmb48.99</td><td>Downside: 18.8%</td></tr><tr><td>2050.HK</td><td>12m Price Target: HK$41.20</td><td>Price: HK$30.32</td><td>Upside: 35.9%</td></tr></table>

<table><tr><td>Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap:</td><td>Revenue (Rmb mn)</td><td>31,011.7</td><td>33,010.1</td><td>37,729.6</td><td>45,800.6</td></tr><tr><td>Rmb206.2bn / $30.4bn</td><td>EBITDA (Rmb mn)</td><td>5,743.7</td><td>6,272.5</td><td>7,220.1</td><td>8,597.2</td></tr><tr><td>Enterprise value:</td><td>EPS (Rmb)</td><td>0.97</td><td>1.08</td><td>1.24</td><td>1.49</td></tr><tr><td>Rmb195.5bn / $28.8bn</td><td>P/E (X)</td><td>34.5</td><td>45.5</td><td>39.4</td><td>33.0</td></tr><tr><td>3m ADTV: Rmb6.7bn / $988.4mn</td><td>P/B (X)</td><td>4.4</td><td>5.9</td><td>5.3</td><td>4.8</td></tr><tr><td>China Industrial Tech &amp; Machinery</td><td>Dividend yield (%)</td><td>1.2</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td>M&amp;A Rank: 3</td><td>N debt/EBITDA (ex lease,X)</td><td>(1.8)</td><td>(1.8)</td><td>(1.7)</td><td>(1.6)</td></tr><tr><td>Leases incl. in net debt &amp; EV?:</td><td>CROCI (%)</td><td>23.5</td><td>20.9</td><td>21.2</td><td>21.9</td></tr><tr><td>Yes</td><td>FCF yield (%)</td><td>1.4</td><td>1.2</td><td>1.2</td><td>1.4</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (Rmb)</td><td>0.22</td><td>0.31</td><td>0.30</td><td>0.24</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 3 Jul 2026 close.

## Disclosure Appendix

## Reg AC

I, Jacqueline Du, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Jacqueline Du GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Sanhua Intelligent Controls (A) and Sanhua Intelligent Controls (H) is/are relative to the other companies in its/their coverage universe: AVIC Jonhon, Best, Bochu, CRRC Corp. (A), CRRC Corp. (H), Centre Testing Intl Group, Estun Automation Co.(A), Estun Automation Co.(H), Faratronic, Haitian International Holdings, Han's Laser Technology, HangKe Technology, Hongfa Technology, Huaming, Kehua Data Co., Lead Intelligent (A), Lead Intelligent (H), Leader Harmonious Drive Systems Co., Luster LightTech Co., Megmeet, Moons' Electric, NARI Technology, Nantong Jianghai Capacitor Co., OPT Machine Vision Tech Co., Sanhua Intelligent Controls (A), Sanhua Intelligent Controls (H), Shanghai Baosight Software, Shenzhen Envicool Technology, Shenzhen Inovance Technology Co., Shenzhen Kstar Science & Tech, Shuanghuan Driveline, Sieyuan Electric, Techtronic Industries, Wuhan Raycus Fiber Laser Tech, Yiheda Automation, Yingliu, Zhejiang Supcon Technology Co., Zhuzhou CRRC Times Electric Co. (A), Zhuzhou CRRC Times Electric Co. (H)

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the second most recent month end: Sanhua Intelligent Controls (A) (Rmb48.99) and Sanhua Intelligent Controls (H) (HK\$30.32)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/b7b6b232bc45bae46ed7e35ce8d9e0e2970b5d01be7cfee93e80c53083b76094.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/8616c77e02dfdcbec980c9436e973b801fa89a345ce1e88e5f8798decc9cf90f.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

Sanhua Intelligent Controls (A) (002050.SZ)

<table><tr><td>Date of report</td><td>Target price (Rmb)</td

[中间内容因长度限制已省略]

es, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
