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
# Japan Industrials: Multiple cos. announce NVIDIA partnerships/physical AI initiatives; Omron is being overlooked, reiterate Buy

NVIDIA CEO Jensen Huang unveils made-in-Japan physical AI
On July 16, NVIDIA CEO Jensen Huang announced a series of collaborations with Japanese companies in Japan, centered on physical AI. The two formal releases directly relevant to our industrials coverage are: (1) Fujitsu, together with robot makers Fanuc, Yaskawa Electric, and Kawasaki Heavy Industries, has begun exploring business opportunities for the social implementation of physical AI with technical support from NVIDIA; and (2) Omron has expanded its collaboration with NVIDIA Omniverse to drive technological innovation in its printed circuit board (PCB) inspection equipment. In addition, Hitachi also announced on the same day a collaboration with NVIDIA for operational verification of its “autonomous factory”, marking a day on which NVIDIA’s wide-ranging engagement with Japan’s manufacturing and industrial sectors was announced in concentrated fashion.

In June, NVIDIA had already launched a developer collaboration framework (Cosmos Coalition), and announced that ten companies — including Fujitsu, Fanuc, Yaskawa Electric, and Kawasaki Heavy Industries — would join as part of an expansion of its robot foundation model Cosmos to Japanese companies. Also on July 16, CEO Huang appeared at an event hosted by the Ministry of Economy, Trade and Industry. It was announced that Noetra, a national-policy AI company established by SoftBank and others, will procure 27,500 units of the next-generation AI semiconductor Rubin. CEO Huang believes physical AI is the next industrial revolution, and that it will be born as ‘Made in Japan’, which aligns with the goals set out in the government’s 17 policy directives reported in June (link; in Japanese).

For comments from our analyst Chikai Tanaka regarding Fujitsu, please see here.

Robot stocks bucked the broader machinery sector decline, but Omron — which announced a direct technology collaboration expansion — fell on the day TOPIX fell 1.45% on July 16, and many stocks in our Japan industrials coverage also closed lower. Amid selling pressure on AI- and semiconductor-related names — and FA stocks in particular within our industrials coverage — Fanuc, Yaskawa Electric, and Kawasaki Heavy Industries each closed in positive territory.

Omron, on the other hand, fell $1.83\%$ despite also having an NVIDIA collaboration and partnership announcement, and failed to see a re-rating. Our impression is that the difference in media coverage — with the Nikkei's breaking news article

## Yuichiro Isayama

+81(3)4587-9806 |
yuichiro.isayama@gs.com
GS Japan Co., Ltd.

Takeru Adachi
+81(3)4587-4067 |
takeru.adachi@gs.com
GS Japan Co., Ltd.

Takato Enoki
+81(3)4587-1739 |
takato.enoki@gs.com
GS Japan Co., Ltd.

Chie Hu
+81(3)4587-6330 | chie.hu@gs.com
GS Japan Co., Ltd.

mentioning Omron only briefly, in a single paragraph toward the end of a piece focused on the partnerships involving Fanuc, Yaskawa and KHI — could explain the difference in share price reaction. However, as we discuss below, a closer examination of the release content leads us to conclude that among the stocks in our coverage related to today's announcements, it is Omron that is best positioned to directly benefit from the current shift in the demand environment through this expanded partnership — specifically in the context of AI server PCB inspection. Compared with the three robot-related companies, we have a strong impression that the benefits for Omron are being significantly underestimated. We maintain our Buy rating on the stock.

Fujitsu x three robot companies partnership: Still at the business exploration stage, but roles and technology stack are concrete

The scheme announced involves Fujitsu taking the lead and incorporating NVIDIA's physical AI platform — using the Cosmos world foundation model as a component for physical simulation, and Isaac/Omniverse with the Newton physics engine for robot development and verification — to develop a sovereign collaborative control platform, which will be offered as an open platform to participating companies and research institutions. The structure is designed to reduce concerns about the risk of confidential information leakage by establishing a domestically developed platform, with the aim of promoting adoption primarily at sites facing severe labor shortages. Fujitsu will supply the CPU, FUJITSU-MONAKA and the software. The roles of each robot company partner within this framework are clearly differentiated, as follows.

1. Fanuc — responsible for manufacturing. The aim is to optimize factory production planning and automate on-site adaptation. Fanuc’s physical AI strategy is characterized by an open platform approach of opening all models to AI, rather than embedding AI within products. In conjunction with iREX in December 2025, Fanuc open-sourced its ROS 2 driver (via GitHub) and incorporated Python as standard, enabling its full lineup — from small 3 kg payload models to large 2.3-tonne machines — to be driven by external AI, and unveiled its first physical AI application using NVIDIA Jetson as an external brain. By May 2026, the company had adopted Jetson Thor to increase AI computing performance by more than 7.5x, and had advanced to flexible object imitation learning using the foundation model Isaac GR00T N, as well as digital twin integration between ROBOGUIDE and Isaac Sim. Because the AI brain is external, a multi-vendor strategy is viable — allowing AI platforms to be swapped or used in combination, from NVIDIA (December 2025) to Google Gemini (May 2026) to Fujitsu Takane (this announcement) — and the current release explicitly states that ROS 2/Python-compatible robots paired with Takane will be deployed on-site as a flexible AI system accessible to anyone. As the world’s No. 1 industrial robot maker, Fanuc appears to be taking a long-term view of business opportunities, seeking to position its large existing install base as a receptacle for the AI ecosystem.

2. Yaskawa Electric — responsible for retail and distribution. The aim is to reduce labor and automate logistics operations through logistics planning that incorporates real-time sales and inventory data. In contrast to Fanuc, Yaskawa takes a vertically integrated approach of embedding AI within products and selling them. It is the only company already mass-producing and commercially selling MOTOMAN NEXT

(launched in 2023), an autonomous AI robot with NVIDIA GPUs built in as standard — the first in the industry to feature autonomous functions as standard. The company has the potential to monetize business opportunities early through Motoman Next, which delivers AI decision-making capability as standard out of the box, for non-routine tasks such as deli food plating and strawberry packing. Although Yaskawa is the only one of the three robot companies not to have issued a standalone release this time, it has been named as a partner since the announcement of the Fujitsu x NVIDIA strategic partnership in October 2025, and the concept of providing Fujitsu- and NVIDIA-jointly developed AI infrastructure to MOTOMAN NEXT had already been outlined at that time. This initiative is also consistent with the data-driven management approach advocated since the proposal of i³-Mechatronics in 2017, and ROS 2 compatibility is already in preparation. We note the July 15 demonstration of a continuously learning robot with SoftBank and media reports (Nikkei; in Japanese) of approximately ¥120 bn in physical AI-related investment.

3. Kawasaki Heavy Industries — responsible for healthcare. The aim is a hospital one-stop solution that integrates hospital operational systems such as electronic medical records with robots and AI to provide end-to-end support from patient arrival through consultation, treatment, surgery, and post-operative care. Specific applications include automation of in-hospital transport of pharmaceuticals and specimens, and AI agent-based outpatient reception and guidance. At the press conference, President Hashimoto mentioned combinations with the surgical support robot (hinotori) and robots for nurses and caregivers. Kawasaki Heavy Industries opened its Kawasaki Physical AI Center San Jose in Silicon Valley in May 2026 in collaboration with NVIDIA, Microsoft, and others, and today's series of announcements can be seen as an extension of that initiative. We believe in terms of the concreteness of the product concept as a measure of business development clarity, KHI's offering is on par with the other two companies, in our view.

It should be noted that all three companies are still at the beginning of the business exploration phase, with roadmaps to be formulated going forward. As there are no capital relationships or financial commitments, these announcements represent a direction and vision rather than firm commitments.

## Omron: AOI/AXI x Omniverse is a positive development that should lead to near-term monetization and higher value-added

Although the stock market overlooked this today, Omron's announcement differs significantly from the three robot companies' framework in that it is not at the exploration stage — it is an announcement of results already implemented. The company has expanded its digital twin technology collaboration with NVIDIA, which began in 2022, and announced the following immediately deployable technologies that are directly beneficial for capturing today's demand: (1) a technology that uses physical simulation to visualize PCB component “warping” in real time, enabling pre-adjustment of heat sources to predict and prevent solder joint defects; (2) a technology that overlays 3D surface data from AOI (automated optical inspection) equipment with internal structural data from AXI (3D-CT X-ray inspection) equipment in digital space, enabling immediate identification of causal relationships such as internal voids behind surface misalignments; and (3) a technology using NVIDIA's VSS (VLM + Graph RAG) AI agent that enables even novice operators to perform inspection tasks.

In our view, this series of announcements is squarely aligned with the current trend of increasingly sophisticated mounting and quality control demand for AI data center PCB and semiconductor package substrates. It should enable Omron to steadily capture the benefits of the tightening AI data center-related supply chain and the associated increase in capital goods demand that we have been highlighting this quarter (see our Taiwan research trip report). The inspection equipment business, including AXI and AOI, had been growing rapidly to revenues of few tens of billion yen, but profitability had been a challenge. The results of today's expanded partnership appear to address this concern — pointing toward improvements in value-added ratios — and our impression is positive. Despite being an announcement that is clearly close to monetization and likely to contribute to profit growth, the stock appears to have received no credit whatsoever today. This reinforces our impression that the relative attractiveness of Omron's shares has increased. We reiterate our Buy rating.

## Price Target Risks and Methodology - Kawasaki Heavy Industries (7012.T)

Our 12-month target price of ¥3,500 is based on FY3/28E EV/EBITDA, applying the Japan Aerospace & Defense subsector-average multiple of 14X and a 30% sector-relative discount.

The key upside and downside risks include (1) yen depreciation/appreciation relative to our assumed exchange rate, (2) faster-/slower-than-expected expansion of defense order and revenue momentum, (3) lower-/higher-than-expected cost variability in PS&E, particularly promotional expenses in the North American four-wheeler business, and (4) faster-/slower-than-expected progress on portfolio restructuring and the turnaround of low-profitability segments, with implications for the conglomerate discount.

## Price Target Risks and Methodology - Yaskawa Electric (6506.T)

Our 12-month target price of ¥9,000 is based on FY2/28E EV/EBITDA, applying the sector-average multiple of 10X and a 90% sector-relative premium.

Key downside risks include (1) a slowdown in semiconductor and AI Capex related business, (2) slower-than-expected results from cost optimization measures, and (3) disappointment in the capital policy and growth strategy in the next medium-term plan and long-term vision.

## Price Target Risks and Methodology - Omron (6645.T)

Our 12-month target price of ¥8,000 is based on FY3/28E EV/EBITDA, applying the sector-average multiple of 10X and a 20% sector-relative premium.

Key downside risks include weaker-than-expected growth in solutions sales in the IAB segment, a slower-than-expected expansion of the IAB business in developed markets, and a shift to a less favorable business portfolio mix.

## Price Target Risks and Methodology - Fanuc (6954.T)

Our 12-month target price of ¥5,600 is based on FY3/28E EV/EBITDA, applying the sector-average multiple of 10X and a 70% sector-relative premium.

Key upside risks include sales in the FA business recovering to levels above past peaks, greater-than-expected improvement in robot business margins, and share buybacks or other moves to strengthen shareholder returns.

## Disclosure Appendix

## Reg AC

We, Yuichiro Isayama, Takeru Adachi, Takato Enoki and Chie Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yuichiro Isayama GS Japan Co., Ltd., Takeru Adachi GS Japan Co., Ltd., Takato Enoki GS Japan Co., Ltd., Chie Hu GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-

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
