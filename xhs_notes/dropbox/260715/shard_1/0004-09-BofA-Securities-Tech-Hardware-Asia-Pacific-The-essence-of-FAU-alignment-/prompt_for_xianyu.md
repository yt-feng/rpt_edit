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

Exhibit 14: Stocks

[中间内容因长度限制已省略]

een BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

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
