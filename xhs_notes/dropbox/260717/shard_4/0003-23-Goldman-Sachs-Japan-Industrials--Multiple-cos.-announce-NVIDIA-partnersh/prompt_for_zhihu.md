你是知乎商业/行业研究作者，擅长把英文/中文研报改写成适合知乎发布的长文。

【目标】
- 基于下面研报解析内容，生成一篇中文知乎文章。
- 风格接近微信公众号文章，但更适合知乎：论证更完整、语气更克制、有问题意识、有推理链条。
- 文章不需要把研报所有内容讲完，要留下继续阅读完整报告或加入社群讨论的空间。
- 目标长度：约 2200 字，允许上下浮动 20%。

【结构要求】
1. 第一行：知乎标题，直接讲观点，不要标题党，不要夸张极限词。
2. 开头 2-3 段：用一个真实问题或市场分歧切入，说明为什么这份报告值得看。
3. 正文按金字塔原则组织：先给核心判断，再展开 3-5 个支撑逻辑。
4. 每个小标题都要像观点句，不要写“核心判断”“支撑逻辑一”“对读者的启发”这种模板名。
5. 内容要比小红书更理性，比微信更像问答式分析，可以适度提出反问。
6. 结尾自然留下讨论空间，可使用这类表达：`完整报告里还有不少细节，适合放在社群里继续拆。`

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- 不要写“非投资建议”“仅做学习交流”这种免责声明，也不要出现包含“投资”的免责声明。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要使用“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词。

【内容要求】
- 只能基于研报原文和解析内容推导，不要编造数据、页数、作者、结论或引用。
- 可以基于报告内容做适度发散，但必须明确哪些是报告内容，哪些是你的延展观察。
- 默认避免具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或使用 GS/JPM/MS 等缩写。
- 不要输出解释说明，只输出知乎文章正文。

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

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Fanuc, Kawasaki Heavy Industries, Omron and Yaskawa Electric is/are relative to the other companies in its/their coverage universe: AeroEdge, CKD, Daifuku, Daikin Industries, Fanuc, Harmonic Drive Systems, Hoshizaki, IHI, Japan Steel Works, Kawasaki Heavy Industries, Keyence, Makita, Misumi Group, Mitsubishi Heavy Industries, Okuma, Omron, SKY Perfect JSAT Corp, SMC, THK, Yaskawa Electric

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Kawasaki Heavy Industries (¥2,738), Omron (¥5,594) and Yaskawa Electric (¥5,494)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Kawasaki Heavy Industries (¥2,738) and Omron (¥5,594)

GS had an investment banking services client relationship during the past 12 months with: Kawasaki Heavy Industries (¥2,738) and Omron (¥5,594)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Kawasaki Heavy Industries (¥2,738) and Omron (¥5,594)

GS had a non-securities services cl

[中间内容因长度限制已省略]

 or may discuss in this report, trading strategies that reference catalysts or events that may have a near-term impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
