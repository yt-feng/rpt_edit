你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Tech Hardware - Asia Pacific

# The essence of FAU: alignment and

automation

Industry Overview

## FAU: lots of new entrants, but few likely winners

FAU acts as a highway connecting fiber to the optical engine for data transmission, and is essential to pluggable transceiver/NPO/CPO. Currently, FAUs are mostly supplied by legacy Asia supply chains, and FAU for CPO is 100% supplied by a Chinese vendor. We see more new entrants aiming to ramp up CPO/FAU-related components – e.g. fiber array, micro lens, prism, etc. However, in our view, not many of them could succeed due to high entry barriers, and we see Largan's progress as faster than other new entrants as it has moved on to certification after sampling/testing for two quarters. We highlight two key bottlenecks: (1) micron-level alignment, i.e. controlling the pitch tolerance at ≤ ±0.5μm or even lower to ensure low-loss transmission; and (2) automatic alignment and testing to deliver consistent tolerance while lift efficiency. We note this know-how will take years of accumulated experience in precision optic manufacturing, mass production, as well as strong in-house automation capability.

## CPO to take off in '28-29; FAU at 5-10% BOM/ \$8bn TAM

Based on our checks, Nvidia's CPO switch volume may remain relatively low near-term, and a meaningful volume could happen in 2028-29, on rising penetration at scale-up. BofA tech team expects Nvidia CPO switch shipments to reach 14k/52k/190k units in 2026/27/28E. Among key components, we expect FAU to contribute 5-10% of the BOM, with the ASP ranging from US\$80-200. The TAM for FAU in Nvidia CPO switches could hit US\$8bn by 2030E. Amid multiple new optical solutions, we believe pluggable will remain a mainstream in scale-out into 2028-30. Within scale-up, the penetration of NPO and CPO depends on key CSPs' preference as well as CPO's overall yield and cost.

## GlassBridge: in early stage, not a replacement for FAU

Amid market's concern about potential threat from Corning's GlassBridge solution (to replace FAU), we argue that GlassBridge is still at an early stage, and is unlikely to be adopted in current and next-generation CPO design. Although GlassBridge could indeed improve the assembly yield, several bottlenecks need to be addressed, including misalignment with PIC due to the waveguide's uneven surface, rising manufacturing difficulty when channel numbers rise to $70+$ , etc. Also, under GlassBridge solution, a fiber array is still needed but likely with a lower precision-alignment requirement.

## Upgrade Largan to Buy, Neutral on Sunny Optical

We see the datacom supply chain as a more closed ecosystem vs consumer electronics, given much higher requirements. Besides capability, customer engagement is another key. We upgrade Largan to Buy from Neutral on faster progress at CPO (see Largan report). We reiterate Neutral on Sunny Optical given the lack of concrete projects.

## 14 July 2026

Equity
Asia Pacific
Tech Hardware

Katherine Zhu >>
Research Analyst
BofA (Hong Kong)
kexin.zhu@bofa.com

Robert Cheng >>
Research Analyst
BofA (Taiwan)
robert.cheng@bofa.com

Doris Kao >>
Research Analyst
BofA (Taiwan)
doris.kao@bofa.com

For acronyms, please refer to Exhibit 13

## FAU in CPO: \$8bn TAM by '30 on volume take-off from '28

Based on our supply chain check, Nvidia's CPO switch shipment may remain relatively low near-term, and a meaningful volume likely takes off in 2028-29 following rising penetration at scale-up. BofA tech team expects volume to reach 14k/52k/190k units in 2026/27/28E. Among key components, optical engine (OE) acts as the core to convert electric and light signals, while FAU acts as a highway connecting optical fiber and optical engine for data transmission. Outside of CPO switch, external laser source (ELS) is responsible for projecting laser that helps drive light signal through optical fiber, while MPO/MMC are connectors that connect optical fibers housed in the shuffle box to external ports. Looking at the BOM of a CPO switch, optical engine, ELS, and FAU are likely contribute $40 - 55\%$ , $10 - 15\%$ and $5 - 10\%$ of the total BOM, respectively.

Specifically for FAU, we believe its TAM in Nvidia CPO switch could reach US\$8bn by 2030E, based on an assumption of 1.4mn units of CPO switch and 115 units of 1.6T equivalent OEs per switch. Our check suggests FAU's ASP ranges from US\$80-200, depending on current specs. General FAU consists of fiber array (V-groove and optical fiber), lid, substrate and casing, etc, while some high-end FAU also integrate optical components like micro lens, prism and MT ferrules. For example, Spectrum 6810 adopts 36 channels of dFAU, and dFAU pricing could be in the range of US\$150-200. With volume gradually rising into 2030, the ASP could fall to US\$100. However, as specs migrate to 70-100 channels and potential multi-layer design, FAU could witness content value upside.

Exhibit 1: We expect Nvidia CPO switch shipment to reach 14k/52k/190k units in 2026/27/28E
Nvidia CPO switch shipment, 2026-30E  
![](images/c1eacaa238c021171228ee2cde020672cae230d294ccb598bcb04e1ce31af389.jpg)  
Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 3: We estimate FAU value per switch could reach US\$6-7k Nvidia CPO switch BOM analysis

<table><tr><td>US$</td><td>Quantum Q3450</td><td>Spectrum 6810</td></tr><tr><td>Switch chip</td><td>12,000</td><td>5,000</td></tr><tr><td>OE</td><td>64,800</td><td>32,400</td></tr><tr><td>FAU</td><td>6,120</td><td>6,480</td></tr><tr><td>ELS</td><td>11,700</td><td>10,400</td></tr><tr><td>MPO &amp; shuffle box</td><td>8,760</td><td>9,400</td></tr><tr><td>Others (substrate, PCB, cooling, power, etc)</td><td>15,000</td><td>15,000</td></tr><tr><td></td><td>118,380</td><td>78,680</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 2: Spectrum 6810 features 36 FAUs (include 4 redundancy)
Nvidia CPO switch component summary

<table><tr><td></td><td>Quantum X800Q3450</td><td>Spectrum 6810</td><td>Spectrum 6800</td></tr><tr><td>Switch chip</td><td>4</td><td>1</td><td>4</td></tr><tr><td>OE</td><td>72</td><td>36</td><td>144</td></tr><tr><td>FAU</td><td>72</td><td>36</td><td>144</td></tr><tr><td>ELS</td><td>18</td><td>16</td><td>64</td></tr><tr><td>Laser</td><td>144</td><td>128</td><td>512</td></tr><tr><td>MPO/MMC</td><td>144</td><td>128</td><td>512</td></tr></table>

Source: Company data, BofA Global Research  
BofA GLOBAL RESEARCH

Exhibit 4: FAU roughly contributes $5 - 10\%$ BOM of a Nvidia CPO switch Nvidia Quantum and Spectrum CPO switch BOM analysis  
![](images/9c5b8db3ca34c89ff5d8b300c8adc6ce825fcc3f7bb90967d00631e7327d9fa8.jpg)  
Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 5: We expect FAU's TAM for CPO switch to reach US\$8bn by 2030E
FAU (for CPO) TAM analysis, 2026-30E

![](images/a28d13ef7d4365c7206b0b4d667d3ecb7fada562ee86e7851c60945dedca408d.jpg)  
Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH  
Exhibit 6: We see dFAU ASP at around USD180 in recent 1-2 years  
dFAU ASP trend (36-channel, 3.2T equivalent), 2026-30E

![](images/1c14d7f17467482bb3db5641968982341ff80692d2a94e330be44259ffeb735d.jpg)  
Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 7: FA likely to contribute 50% of the BOM, followed by micro lens at \~30%
BOM analysis of FAU (with micro lens, prism etc)  
![](images/e3aa8f016a25863c8faca3a58e1354e26acde3a4e6d4d379d588fbbac1719732.jpg)  
Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 8: Key FAU suppliers are mostly located in Asia (China, Japan, Taiwan)
Key suppliers in CPO supply chain

<table><tr><td>Component</td><td colspan="6">Key suppliers</td></tr><tr><td>Optical engine</td><td>Nvidia</td><td>Broadcom</td><td>Marvell</td><td colspan="3">TSMC (foundry)</td></tr><tr><td colspan="7">FAU</td></tr><tr><td>V-groove</td><td>TFC</td><td>Senko</td><td>Orbray</td><td>Corning</td><td>Focuslight</td><td></td></tr><tr><td>Optical fiber</td><td>Corning</td><td>Fujikura</td><td>YOFC</td><td></td><td></td><td></td></tr><tr><td>Micro lens</td><td>TFC</td><td>Coherent</td><td>Focuslight</td><td>Largan</td><td>Himax</td><td></td></tr><tr><td>FAU</td><td>TFC</td><td>Senko</td><td>FOCI</td><td>Coherent</td><td>Corning</td><td>Largan (potential)</td></tr><tr><td colspan="7">ELS</td></tr><tr><td>Laser</td><td>Lumentum</td><td>Coherent</td><td>Broadcom</td><td>Furukawa</td><td>Yuanjie</td><td>DS Precision</td></tr><tr><td>Module</td><td>TFC</td><td>Lumentum</td><td>Coherent</td><td>Innolight</td><td>Eoptolink</td><td>DS Precision</td></tr><tr><td>Shuffle box</td><td>Corning (T&amp;S)</td><td>Browave</td><td>Senko</td><td>Molex</td><td>TFC</td><td></td></tr><tr><td>MPO/MMC</td><td>US Conec</td><td>Senko</td><td>T&amp;S</td><td></td><td></td><td></td></tr><tr><td>Assembly/testing</td><td>Fabrinet</td><td>Hon Hai/FII</td><td>ASE/SPIL</td><td>USI</td><td></td><td></td></tr><tr><td>Equipment</td><td>Chroma</td><td>FiconTEC</td><td></td><td></td><td></td><td></td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH

## Alignment and automation lift entry barrier

FAU acts as a highway connecting optical fiber to the optical engine for data transmission, and is essential to pluggable transceiver/NPO/CPO. Currently, FAUs are mostly supplied by legacy Asia supply chains, while FAU for CPO is 100% supplied by Chinese vendors. We highlight two key bottlenecks faced by the supply chain: (1) micron-level alignment, i.e. controlling the pitch error tolerance at $\leq\pm0.5\mu m$ (or even $\leq\pm0.3\mu m$ ) to ensure light signal efficiency; and (2) automatic alignment to deliver consistent accuracy while lifting efficiency.

## Alignment: solving the pitch tolerance

Fiber array used in FAU acts as a multi-lane highway for light, allowing multiple data channels to be connected simultaneously with the optical engine for conversion of electronic and light signals. Under a fiber array, multiple optical fibers are densely seated on a V-groove (features parallel and microscopic V-shaped channels). The process requires highly precise alignment to achieve low-loss transfer. To compare, an optical

transceiver usually has a pitch tolerance (i.e. alignment accuracy) of $\pm0.5\mu m$ to $\pm1.0\mu m$ . NPO's pitch tolerance is likely at $\leq\pm0.5\mu m$ , while CPO's pitch tolerance could be $\leq\pm0.3\mu m$ . As V-groove and fiber also have their own geometric tolerance, alignment error could accumulate linearly when channel numbers rise. V-groove's etching depth and angle variation could introduce misalignment from channel to channel. Even if a V-groove is perfectly etched, optical fiber could also lead to alignment difficulties. A single-mode fiber generally has a diameter of 80-125 $\mu m$ (core at 6-10 $\mu m$ ); any diameter variation of a fiber could cause it to sit higher or lower on a V-groove, leading to alignment mismatch. Additionally, for dFAU, maintaining positioning tolerance after multiple detach/plug processes is also key.

This level of precision alignment usually requires years of accumulation, deep know-how in optic coupling and mass production experiences. Although smartphone optic suppliers could leverage their active alignment (AA) know-how used in lens/module, the level of precision still has a big gap (for example, telephoto camera's AA tolerance is $\leq \pm 5\mu \mathrm{m}$ ).

## Automation: crucial when channel numbers continue rising

As optical fiber channel numbers are expected to increase to 60-100 from the current 20-36 channels while CPO volume is waiting for take-off in 2028-29, fiber array alignment based on labor-intensive process looks increasingly difficult. Thus, automation becomes crucial. It could not only reduce labor intensity and lift efficiency, but more importantly help troubleshoot alignment issues and improve accuracy. As the industry has no standard automation/testing at current stage, suppliers able to ramp up automation faster or have in-house automation capability could have a better edge.

Exhibit 9: FAU assembles PM fibers on a V-groove to direct light, and leverages micro lens and prism to project light onto PIC
Illustration of FAU under grating coupler solution  
![](images/92d5138093df96c801d4ac49396c1282bd1573be4269de3783c926f8f03a5129.jpg)

Exhibit 10: CPO has the lowest pitch error tolerance at ≤ ±0.3μm
FAU spec summary under different applications

<table><tr><td></td><td>Pluggable transceiver</td><td>NPO</td><td>CPO</td></tr><tr><td>FAU location</td><td>Inside module</td><td>On host PCB</td><td>On substrate</td></tr><tr><td>Pitch error tolerance</td><td>±0.5μm - ±1.0μm</td><td>≤ ±0.5μm</td><td>≤ ±0.3μm</td></tr><tr><td>Channel count</td><td>4 to 16</td><td>16 to 32</td><td>32 to 128+</td></tr><tr><td>Insertion loss target</td><td>&lt;0.5dB</td><td>&lt;0.3dB</td><td>&lt;0.2dB</td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH  
Source: FOCI  
BofA GLOBAL RESEARCH

## GlassBridge not a threat near-term, also not a replacement

We note market's concern about Corning's GlassBridge, a wafer-based fiber-to-PIC technology, which could be an alternative solution to FAU. We argue that GlassBridge is still at an early stage and is unlikely to be adopted in current and next-generation CPO design. Although GlassBridge could indeed improve the assembly yield, several bottlenecks need to be addressed, including misalignment with PIC due to the waveguide's uneven surface (due to edge coupling), rising manufacturing difficulty when channel numbers rise to 70+, etc. Further, GlassBridge uses edge coupling technology – i.e. horizontal coupling, with light projected directly into the PIC horizontally. Compared with grating coupling (vertical coupling), edge coupling is not able to conduct wafer-scale testing, leading to potentially lower efficiency. The horizontal design also faces space limitations and demands an extreme alignment requirement.

Exhibit 11: GlassBridge is a wafer-based fiber-to-PlC technology platform
Corning's GlassBridge connector  
![](images/dff1da71a0e818f22e951595369d5ff5661982892c87bd8ac16be32014c50dcc.jpg)

Exhibit 12: Edge coupling is more efficient in insertion loss, but faces limitation in terms of wafer-level testing and spatial constraint
Comparison of grating coupling and edge coupling

<table><tr><td></td><td>Grating coupling</td><td>Edge coupling</td></tr><tr><td>Coupling type</td><td>Vertical</td><td>Horizontal</td></tr><tr><td>Insertion loss</td><td>Good efficiency</td><td>High efficiency</td></tr><tr><td>Alignment tolerance</td><td>High</td><td>Extreme</td></tr><tr><td>Wafer level testing</td><td>Yes</td><td>No</td></tr><tr><td>Spatial constraint</td><td>No</td><td>Yes</td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH  
Source: Corning  
BofA GLOBAL RESEARCH

Exhibit 13: Summary of acronyms used in this report
Acronym

<table><tr><td colspan="2">Acronym</td></tr><tr><td>AI</td><td>Artificial Intelligence</td></tr><tr><td>ASP</td><td>Average Selling Price</td></tr><tr><td>BOM</td><td>Bill of Materials</td></tr><tr><td>CPO</td><td>Co-packed Optics</td></tr><tr><td>ELS</td><td>External Laser source</td></tr><tr><td>FA</td><td>Fiber Array</td></tr><tr><td>FAU</td><td>Fiber Array Unit</td></tr><tr><td>dFAU</td><td>Detachable Fiber Array Unit</td></tr><tr><td>MPO</td><td>Multi-fiber Push-On</td></tr><tr><td>MMC</td><td>Multiport Modular Connector</td></tr><tr><td>MT</td><td>Mechanical Transfer</td></tr><tr><td>NPO</td><td>Near-packaged Optics</td></tr><tr><td>OE</td><td>Optical Engine</td></tr><tr><td>PIC</td><td>Photonic Integrated Circuit</td></tr><tr><td>PCB</td><td>Printed Circuit Board</td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH  
Source: BofA Global Research

Exhibit 14: Stocks mentioned in this report
Stocks mentioned

<table><tr><td>BofA Ticker</td><td>Bloomberg Ticker</td><td>Company Name</td><td>Price (LC)</td><td>Rating</td></tr><tr><td>LGANF</td><td>3008 TT</td><td>Largan Precision</td><td>4345.00</td><td>B-1-7</td></tr><tr><td>SNPTF</td><td>2382 HK</td><td>Sunny Optical</td><td>55.05</td><td>C-2-8</td></tr></table>

BofA GLOBAL RESEARCH

## Investment Rationale

## Largan Precision

We have a Buy rating on Largan, eyeing on rising visibility on potential CPO project gain. We believe CPO will drive valuation a re-rating and a potential earning upside from 2028E. Besides, legacy business should stay resilient thanks to iPhone's multi-year spec upgrade cycle.

## Price objective basis & risk

## Largan Precision (LGANF)

Our PO of NT\$5,600 is based on 25x 2028E P/E. 25x is at Largan's historical peak P/E during last earnings upcycle. We believe CPO take-off from 2028 will drive another new multi-year earnings upcycle for Largan, justifying our valuation multiple.

Downside risks are: 1) weaker than expected end-demand, which leads to pressured topline and margin on lower utilization rate, 2) more intense competition from Greater China competitors including Sunny Optical, Genius and AAC, 3) slower than expected spec upgrade, and 4) slower than expected progress at CPO.

Upside risks are: 1) better than expected end demand and faster than expected spec upgrade, 2) higher than expected ASP and market on competitors' inferior execution, 3) eased competition from key peers, and 4) faster than expected progress at CPO.

## Sunny Optical (SNPTF)

We set our PO at HK\$69, on 17x 2026E P/E, we view 17x, around -0.5SD, is justified by potentially slower margin improvement amid uncertainties at smartphone shipment and spec into 2026, while reflect business diversification into datacom.

Downside risk: (1) demand at consumer electronics further deteriorate with continuous de-spec, (2) slower than expected share gain at iPhone, (3) slower-than-expected auto momentum and slower ADAS penetration, (4) intensified competition at both smartphone and auto. (5) Government subsidy is removed.

Upside risk: (1) better than expected demand/spec at consumer electronics, (2) faster than expected share gain at iPhone, (3) strong auto momentum and faster ADAS penetration, (4) eased competition at both smartphone and auto, and (5) faster than expected progress at datacom.

## Analyst Certification

We, Katherine Zhu and Robert Cheng, hereby certify that the views each of us has expressed in this research report accurately reflect each of our respective personal views about the subject securities and issuers. We also certify that no part of our respective compensation was, is, or will be, directly or indirectly, related to the specific recommendations or view expressed in this research report.

## 

[中间内容因长度限制已省略]

use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
