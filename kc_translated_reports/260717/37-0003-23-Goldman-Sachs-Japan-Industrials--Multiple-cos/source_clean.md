# Japan Industrials: Multiple cos. announce NVIDIA partnerships/physical AI initiatives; Omron is being overlooked, reiterate Buy

On July 16, NVIDIA CEO Jensen Huang announced a series of collaborations with Japanese companies in Japan, centered on physical AI. The two formal releases directly relevant to our industrials coverage are: (1) Fujitsu, together with robot makers Fanuc, Yaskawa Electric, and Kawasaki Heavy Industries, has begun exploring business opportunities for the social implementation of physical AI with technical support from NVIDIA; and (2) Omron has expanded its collaboration with NVIDIA Omniverse to drive technological innovation in its printed circuit board (PCB) inspection equipment. In addition, Hitachi also announced on the same day a collaboration with NVIDIA for operational verification of its “autonomous factory”, marking a day on which NVIDIA’s wide-ranging engagement with Japan’s manufacturing and industrial sectors was announced in concentrated fashion.

In June, NVIDIA had already launched a developer collaboration framework (Cosmos Coalition), and announced that ten companies — including Fujitsu, Fanuc, Yaskawa Electric, and Kawasaki Heavy Industries — would join as part of an expansion of its robot foundation model Cosmos to Japanese companies. Also on July 16, CEO Huang appeared at an event hosted by the Ministry of Economy, Trade and Industry. It was announced that Noetra, a national-policy AI company established by SoftBank and others, will procure 27,500 units of the next-generation AI semiconductor Rubin. CEO Huang believes physical AI is the next industrial revolution, and that it will be born as ‘Made in Japan’, which aligns with the goals set out in the government’s 17 policy directives reported in June (link; in Japanese).

For comments from our analyst Chikai Tanaka regarding Fujitsu, please see here.

Robot stocks bucked the broader machinery sector decline, but Omron — which announced a direct technology collaboration expansion — fell on the day TOPIX fell 1.45% on July 16, and many stocks in our Japan industrials coverage also closed lower. Amid selling pressure on AI- and semiconductor-related names — and FA stocks in particular within our industrials coverage — Fanuc, Yaskawa Electric, and Kawasaki Heavy Industries each closed in positive territory.

Omron, on the other hand, fell $1.83\%$ despite also having an NVIDIA collaboration and partnership announcement, and failed to see a re-rating. Our impression is that the difference in media coverage — with the Nikkei's breaking news article

## Yuichiro Isayama

GS Japan Co., Ltd.

GS Japan Co., Ltd.

GS Japan Co., Ltd.

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
