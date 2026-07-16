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
## Rating Buy

North America
United States

Industrials
Space Technology

![](images/dc258109bc4efda0ac1a1d5812d313adaf09185ca79e22c1cd6f34f541b3d3d0.jpg)

Date
14 July 2026

## Special Report

<table><tr><td>Price at 13 Jul 2026 (USD)</td><td>139.14</td></tr><tr><td>Price Target</td><td>255.00</td></tr><tr><td>52-week range</td><td>201.80 - 139.14</td></tr></table>

# Data Centers in Space Part 4

Following up on our initiation last week, we take a closer look at orbital data centers and continue our Data Centers in Space series, introducing a refreshed cost model (Excel available upon request) and further analysis around optical/lasers, spectrum, solar, radiator, and compute density. We factor in the latest disclosures from SpaceX regarding its AI1 satellite and Starmind constellation. Our high-level conclusion is the physics checks out and the biggest challenge will be cost/scale, which we think SpaceX can achieve through extreme vertical integration. Combined with Starship launches scaling up, we envision a scenario in the early 2030s where cost can be on par with terrestrial.

Figure 1: SpaceX AI1 satellite design  
![](images/7485ca751550360ea5757bf7abcd5a1a154fd793eb1eea5864fc63284e7008ff.jpg)  
Source : Company website

## Valuation & Risks

Edison Yu
Research Analyst
+1-212-250-7263

Bryan Kraft
Research Analyst
+1-212-250-0117

Corinne Blanchard
Research Analyst
+1-904-645-2360

Gary Zhou, CFA
Research Analyst
+852-2203-5889

Ross Seymore
Research Analyst
+1-415-617-3268

Roshan Ranjit, CFA
Research Analyst
+44-20-754-52908

Laura Li
Research Associate
+1-212-250-2266

## Optical lasers & spectrum

## Starmind

The AI1 satellites will rely on optical inter-satellite links (OISLs) to route traffic within the Starmind constellation and then into the Starlink constellation, whose laser mesh network then backhauls traffic to ground stations. As such, AI1 satellites do not require a complex multi-panel phased-array antenna onboard (i.e., no meaningful spectrum needed for communication except for possibly some Ka-band as a backup for telemetry). We estimate there are >10,000 Starlink satellites in orbit now with V2 minis each having 3 optical terminals capable of handling \~600 Gbps of capacity (200 Gbps per terminal). For the upcoming V3 satellites, we suspect there may be at least 2-3 Tbps of capacity per satellite. With the quantity of data increasing, we also anticipate SpaceX augmenting and/or upgrading its ground station network.

Figure 2: Starlink mini laser terminal  
![](images/d6abd822c1b10a4efa3ae47640aca60b30718a99fabe0ab7ff23fdfcd2c08108.jpg)  
Source : Company reports

Leading providers of optical terminals are Tesat-Spacecom (subsidiary of Airbus), Mynaric (acquired earlier this year), SA Photonics (acquired by CACI in 2021) and SpaceX (uses internally but also started selling “mini” laser terminals externally - Muon Space and Starcloud have announced plans to use).

## Starlink

Using such an architecture, this means the space-to-ground layer will bear the burden of a lot more traffic. Optical links make the Starmind constellation itself spectrum-free, but data that leaves the laser mesh network must ultimately funnel through Starlink's gateways, and orbital data centers change the shape of that data flow. Starlink's Gen1/Gen2 gateway authorizations were sized for a consumer broadband business whose traffic is asymmetrical (downlink heavy). As such, SpaceX is increasingly utilizing more unconventional spectrum bands beyond Ku-/Ka- such as:

E-band: already using for gateway backhaul; uplink+downlink

■ V-band: authorized for advanced user terminals and gateway; uplink +downlink

■ W-band: authorized for gateway backhaul; primarily uplink

D-band: proposed for gateway backhaul mainly for Al; primarily uplink

Higher bands historically face severe rain fade, oxygen absorption, and atmospheric attenuation that make them unreliable for consumer user terminals so it appears Starlink is mostly using them for high-capacity gateway backhaul links (where large dishes, site diversity, and optical inter-satellite routing can mitigate these issues), prioritizing proven Ku-/Ka- for consumer antennas while gradually adding V- for advanced users as hardware and regulations mature.

Separately, the FCC recently adopted new standards for satellites, replacing the 1990s-era Equivalent Power Flux Density (EPFD) limits that forced LEO systems like Starlink to severely restrict power and beam density to protect GEO satellites. Instead, the new rules use performance-based protection criteria that account for today's adaptive coding/modulation, beamforming, and real-world coordination. In the key Ku-/Ka- bands (10.7–12.7 GHz, 17.3–18.6 GHz, 19.7–20.2 GHz), this allows operators to run at higher power and many more co-frequency satellites/ beams serving the same area (e.g., 7–8 instead of effectively 1). The FCC cited up to 7× more capacity from the same number of satellites.

## Solar power

## Current solutions

Satellites mainly use multi-junction or silicon solar cells. Multi-junction delivers higher performance (\~30% or higher efficiency) by stacking different materials such as gallium arsenide (GaAs) and germanium (Ge) which enable broader spectrum capture of sunlight; these materials also provide greater radiation resistance. However, the production of these two materials is highly concentrated in China especially gallium which can be produced as a byproduct aluminum refining and similarly for germanium, as a byproduct of zinc smelting. Spectrolab (subsidiary of Boeing), AZUR Space (based in Germany; acquired by 5N Plus in 2021), and SolAero (acquired in 2022) are leading providers of multi-junction space grade cells. Silicon is materially cheaper (up to 80%) benefitting from much larger industrial scale but performs worse (usually 15-20% efficiency), and is not as durable due to lower radiation resistance. Within silicon, the main type of cell is referred to as a passivated emitter and rear cell (PERC). Taiwan Solar Energy Corp (TSEC) is a supplier of this type of cell to SpaceX. Amazon LEO also uses PERC but it is unclear who the supplier is.

## What's coming next?

In the next few years, we think a new type of approach can emerge for satellites: heterojunction (HJT). This type of cell combines crystalline silicon with thin layers of amorphous silicon to improve performance. Interestingly, HJT uses a simpler (5-7 steps vs. typical 12-13), lower-temperature production process that could save up to 70% on energy usage although upfront equipment costs will be higher; there is also potential to remove silver from the coating and use copper instead, saving cost. Performance wise, efficiency has been recorded to be as high as 27% and the symmetrical design allows the cell to absorb almost equal light from both sides. Lastly, HJT is very radiation hardened and degrades slowly in orbit. In the US, Solestial (recently acquired by York Space Systems) is working on development of ultrathin, flexible silicon HJT solar cells, leveraging equipment from Meyer Burger.

Beyond HJT, the use of perovskite tandem cells may be the future. Perovskite is a synthetic crystal structure that essentially can be printed or sprayed onto a surface, meaning it is very lightweight and theoretically as efficient as multi-junction. Solar cells today are all rigid but with perovskite, the ability to utilize thin-film or flexible panels becomes possible. Rigid (whether multi-junction or silicon) means the cells are mounted onto a honeycomb-like substrate made of aluminum or carbon fiber composite. These panels then are stacked and use mechanical hinges and springs to unfold once in orbit.

In China, Drinda (2865.HK) showcased a dedicated “space PV” zone at SNEC in May, highlighting its efforts to develop perovskite-based solar solutions for space applications. The company displayed its perovskite/TOPCon tandem technology (with \~33.5% small-area efficiency), alongside flexible CPI-based substrates and a commercial satellite model. The company has been an early mover in the space-based solar business. Xuntian, a subsidiary of the company, plans to manufacture and deploy 12-15 satellites in 2026 (with an order backlog of 54 satellites). GCL’s (3800.HK) booth design and product display at SNEC reflected a clear shift in focus beyond traditional PV, with both battery materials (cathode and anode) and space solar prominently positioned at the front of its exhibition area. For space solar, the company showcased a flexible perovskite solar cell sample alongside satellite-related use cases.

## SpaceX roadmap

SpaceX is currently building a solar cell manufacturing facility in Bastrop, Texas near Austin, as part of a much larger ambition for domestic solar cell production. Bastrop is targeting 10 GW in solar cell capacity with two floors (5 GW each). The facility is permitted for \~1.1m square feet, with potential expansion to 1.6 million, and is co-located with SpaceX's existing Starlink production site. Construction on the solar factory began in late March 2026, with equipment installation having already begun. The plant aims for production ramp-up and "reasonable volume" by the end of 2027. Our understanding is that the plant will initially produce silicon solar cells, delivering around 19% efficiency.

Figure 3: SpaceX ODC satellite production site  
![](images/02fc45b8c0348ed8345020f03be7441839851df146beabe934542780596dc825.jpg)  
Source : Company website

Looking ahead, SpaceX may switch to HJT or perovskite cells but we suspect this will not occur in the near-term option as they likely can not secure the appropriate equipment in time for the AI1 satellite deployment. Ultimately, Elon Musk has indicated plans to put up 100 GW of domestic solar cell capacity within three years.

## Radiator

## Thermal management

Satellites operate in the vacuum of space, meaning there's no air or medium for heat to dissipate via conduction or convection like on Earth. Instead, satellites rely on thermal radiation to reject excess heat generated by onboard electronics and other components. Radiators function by emitting electromagnetic energy, primarily in the infrared spectrum, which carries away heat as photons. The process follows the Stefan-Boltzmann law, where the rate of heat radiation is dependent on temperature and surface area.

## Passive or active?

There are generally two types of radiators: passive and active. Passive radiators reject heat using nothing but material properties and geometry. This exploits the intrinsic thermal properties of materials, surfaces, and geometric configurations to manage heat flow without consuming any electrical power. The main drawback is that the radiator area is limited by the spacecraft's form factor, which caps passive heat rejection capacity. Active radiators are part of a powered thermal loop — pumps circulate fluid from cold plates on the electronics to the radiator panel. This costs power and adds failure modes, but handles much higher heat loads and holds tighter temperature control than passive designs. Nearly all satellites use passive radiator(s). Active radiators are essentially only used on space stations (ISS, Tiangong) and capsules (Dragon, Starliner).

Historically, primes built most of their own radiator panels in-house. Merchant suppliers include Advanced Cooling Technologies (ACT), Paragon Space Development, Redwire, Beyond Gravity, Iberespacio, and Admatis.

## SpaceX roadmap

SpaceX produces the radiator on current Starlink satellites in-house (passive) and will continue to do so for Al1 satellite (active). Al1 will use a double-sided active deployable liquid radiator capable of dissipating $1,400 \, W/m^{2}$ ( $700 \, W/m^{2}$ per face) covering a $110 \, m^{2}$ surface area. This type of radiator requires electrical power and/or moving parts to transport heat from the compute module to the radiator panels. This is necessary given the high power 120–150 kW payload, where heat fluxes are too high for purely passive conduction. Active radiators have typically been very low volume components so SpaceX will be the first to mass produce such a design.

## Compute density

SpaceX is targeting prototype deployments of its AI1 satellites late next year. FCC-filings outline a constellation of up to one million satellites in LEO. Because each satellite has a fixed power and heat budget, the imperative is to maximize computational density. SpaceX is targeting density of 100 kW per ton but AI1 will not meet this threshold, starting off at \~70 kW, implying about 6 MW of compute per Starship launch initially (assumed 85 ton payload capacity). SpaceX expressed openness to hosting all types of chip payloads for its AI1 satellites including Nvidia GPUs, Google TPUs, Amazon Trainium, and of course Tesla's AI chips which prioritize energy efficiency. AI1 is expected to run sustainably at about 120 kW, roughly in line with the power consumption of a NVIDIA GB300 NVL72 rack. In our model, we assume compute density improves to closer to 85-90 kW in 2032E and then 100 kW with the AI3 satellite beyond that.

## Economics can eventually be compelling

To set a baseline, we assume upfront capex for 1 GW of AI compute on the ground is \$38bn and requires \$900m in annual opex (power, maintenance, labor, etc...), translating into \$42.5bn over 5 years (based on Epoch AI analysis). Of this amount, compute represents \$21bn and we assume this carries over to orbital data centers at a 10% mark-up to account for overprovisioning in case of GPU failures. Our sense is GPU failures will not be addressed directly by maintenance but simply each satellite will just operate at lower power in the event of a failure. Therefore, the non-compute costs for terrestrial are \$21.5bn and ODC essentially has to break below this level post overprovisioning or \$19.5bn to be at parity. Looking forward, we assume the cost of terrestrial increases going forward. To illustrate, NVIDIA's CEO Jensen Huang recently commented at GTC Taipei 2026 that a new 1 GW "AI factory" could approach \$100bn in cost with roughly half being compute-related.

Using current SpaceX launch vehicles and satellite designs, we estimate the near-term cost of deploying a 1 GW space data center constellation would be 6x higher than terrestrial (ex-compute). This gap can narrow to 1.0-1.5x later by end of the decade and then eventually be cheaper in the early-mid 2030s. This reduction is primarily driven by Starship (rapid reusability) and aggressive optimization/scaling of the AI-series satellites. We also refresh the DB Orbital Data Center Model which goes deeper into the economic viability of launching AI infrastructure into orbit (Excel available upon request).

Figure 4: Terrestrial vs. orbital data center deployment cost

<table><tr><td></td><td>2027 (generic)</td><td>2029 (AI1)</td><td>2032 (AI2)</td><td>Beyond (AI3)</td></tr><tr><td>Launch cost per kg</td><td>$1,429</td><td>$398</td><td>$170</td><td>$43</td></tr><tr><td>Satellite cost ex compute ($/kW)</td><td>50,133</td><td>13,256</td><td>8,857</td><td>5,008</td></tr><tr><td>Compute density (W/kg)</td><td>33</td><td>56</td><td>87</td><td>98</td></tr><tr><td>Orbital cost ($bn)</td><td>115</td><td>27</td><td>15</td><td>9</td></tr><tr><td>Terrestrial cost (ex compute)</td><td>20</td><td>23</td><td>25</td><td>25</td></tr><tr><td>Cost difference factor</td><td>5.9x</td><td>1.2x</td><td>0.6x</td><td>0.3x</td></tr></table>

Source : Company reports, DB

Figure 5: Starship launch cost trajectory assumptions

<table><tr><td>($mn)</td><td>BOM</td><td>Variable</td><td>Fixed</td><td>Total</td><td>Payload (tons)</td><td>Price/kg</td></tr><tr><td>Starship (early, no ship reuse)</td><td>52</td><td>2</td><td>267</td><td>321</td><td>65</td><td>$4,933</td></tr><tr><td>Starship (partial reuse)</td><td>5</td><td>2</td><td>27</td><td>34</td><td>85</td><td>$398</td></tr><tr><td>Starship (full reuse)</td><td>2</td><td>2</td><td>13</td><td>17</td><td>100</td><td>$170</td></tr><tr><td>Starship (full+rapid)</td><td>1</td><td>1</td><td>4</td><td>6</td><td>200</td><td>$32</td></tr></table>

Source : Company reports, DB

Figure 6: Orbital data center satellite cost trajectory assumptions

<table><tr><td>($000)</td><td>2027(generic)</td><td>2029 (AI1)</td><td>2032 (AI2)</td><td>Beyond(AI3)</td></tr><tr><td>Solar</td><td>1,750</td><td>600</td><td>375</td><td>300</td></tr><tr><td>Radiator</td><td>709</td><td>438</td><td>204</td><td>127</td></tr><tr><td>Compute</td><td>1,620</td><td>2,880</td><td>1,440</td><td>720</td></tr><tr><td>Bus structure</td><td>500</td><td>600</td><td>500</td><td>400</td></tr><tr><td>Laser</td><td>300</td><td>150</td><td>100</td><td>75</td></tr><tr><td>Other</td><td>250</td><td>200</td><td>150</td><td>100</td></tr><tr><td>Total</td><td>5,129</td><td>4,868</td><td>2,769</td><td>1,722</td></tr><tr><td>Ex compute</td><td>3,509</td><td>1,988</td><td>1,329</td><td>1,002</td></tr><tr><td>Satellite size (kW)</td><td>70</td><td>150</td><td>150</td><td>200</td></tr><tr><td>Satellite compute (kW)</td><td>50</td><td>120</td><td>130</td><td>195</td></tr><tr><td>PUE</td><td>1.40</td><td>1.25</td><td>1.15</td><td>1.03</td></tr><tr><td>Satellite hardware cost ($/W)</td><td>73</td><td>32</td><td>18</td><td>9</td></tr><tr><td>Ex compute ($/W)</td><td>50</td><td>13</td><td>9</td><td>5</td></tr><tr><td>Mass (kg)</td><td>1,500</td><td>2,140</td><td>1,500</td><td>2,000</td></tr><tr><td>Power density (W/kg)</td><td>47</td><td>70</td><td>100</td><td>100</td></tr><tr><td>Compute density (W/kg)</td><td>33</td><td>56</td><td>87</td><td>98</td></tr><tr><td>Solar cell efficiency</td><td>20%</td><td>19%</td><td>24%</td><td>30%</td></tr><tr><td>Solar Constant (AMO)</td><td>1,366</td><td>1,366</td><td>1,366</td><td>1,366</td></tr><tr><td>Degradation + pointing margin</td><td>5%</td><td>5%</td><td>5%</td><td>5%</td></tr><tr><td>Solar area ( $m^2$ )</td><td>270</td><td>600</td><td>482</td><td>514</td></tr><tr><td>Solar performance ( $W/m^2$ )</td><td>260</td><td>250</td><td>311</td><td>389</td></tr><tr><td>$/W</td><td>$25.00</td><td>$4.00</td><td>$2.50</td><td>$1.50</td></tr><tr><td>$/ $m^2$ </td><td>$6,489</td><td>$999</td><td>$779</td><td>$584</td></tr><tr><td>Radiator area ( $m^2$ )</td><td>89</td><td>110</td><td>102</td><td>127</td></tr><tr><td>Radiator heat rejection ( $W/m^2$ )</td><td>750</td><td>1,300</td><td>1,400</td><td>1,500</td></tr><tr><td>$/ $m^2$ </td><td>$8,000</td><td>$4,000</td><td>$2,000</td><td>$1,000</td></tr><tr><td>Cost per chip ($)</td><td>$45,000</td><td>$40,000</td><td>$20,000</td><td>$10,000</td></tr><tr><td># of chips (GB300e)</td><

[中间内容因长度限制已省略]

out prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
