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
The SOFC opportunity; undersupplied through 2030

\- SOFC penetrates AIDC BTM prime power due to 3-4 month lead times, zero-NOx operation, and efficient native-DC output

US/Korea/Taiwan/EU driving adoption; by 2030: capacity is scaling up to 5GW+; DOE targets at USD900/kW system cost

\- We like Buy-rated Bloom (global SOFC leader) and Weichai (gas/diesel engine; SOFC capacity ramping)

SOFC is penetrating AIDC for “behind-the-meter” prime power (ex. 2), despite high CAPEX and recurring 5-7 years’ stack replacement costs, due to:

1) shorter lead time of 3-4 months vs 1-2 years for engines, 3-5 years for turbines;  
2) clean with no NOx emission via electrochemical reactions versus combustion;  
3) efficient high electrical efficiency (55-65%), native direct current eliminating costly AC-DC conversion losses. Aligning 800V HVDC architectures is a next-gen approach that reduces USD1-2bn of BOP conversion equipment and improves token/kW.

Beyond the US and AIDC: Ceres estimates SOFC TAM will reach 22GW by 2030. Apart from 24% US market and c50% DC usage, other highlights include: 1) South Korea: Utility scale commercialization is supported by National Clean Hydrogen Portfolio Standard; 2) Taiwan: grid fragility, stringent RE100 requirements for semi fabs and subsidies accelerate localized microgrid deployments; 3) EU: carbon pricing and marine propulsion decarbonization drive broader SOFC adoption.

Scale-up and cost-down pathway: Bloom targets 2GW before YE-2026 and possibly 5GW by 2030, while Ceres's partners (Weichai, Doosan, Delta) targets c100MW by end 2026 and c1GW by 2030. Key bottlenecks include the supply of Scandium, ceramic electrolytes, and Balance of Plant components (c70% of system cost). Economies of scale and lower-temperature metal-supported architecture will drive cost reduction in longer term. We believe Bloom has largely de-risked its expansion plans while management's double-digit annual cost-down target will be aided by Moore's Law. Rystad estimates SOFC system costs will fall 20-25% by 2030, vs DOE total system CAPEX of USD900/kW by 2030e (from USD3,000/kW).

Related companies along the value chain include Ceres (SOFC tech developer), Doosan Fuel Cell (SOFC leader in South Korea), Delta (SOFC leader in Taiwan), Three-Circle (BE's key electrolyte supplier), Kaori (BE's hot box supplier).

We like Buy-rated Bloom (global SOFC leader) and Weichai (gas/diesel engine; SOFC capacity ramping). Key downside risks include slower AIDC buildout, elevated SOFC capital costs, and quicker capacity ramp of gas turbines and gensets.

Global

## Helen Fang\*

Head of Industrials Research, Asia Pacific
The Hongkong and Shanghai Banking Corporation Limited
helen.c.fang@hsbc.com.hk
+852 2996 6942

## Samantha Hoh, CFA

Senior Analyst, Clean Tech
HSBC Securities (USA) Inc.
samantha.hoh@us.hsbc.com
+1 212 525 8783

## Sean McLoughlin\*

Senior Global Industrials Analyst
HSBC Bank plc
sean.mcloughlin@hsbcib.com
+44 20 7991 3464

## Sunny SUN\*

Associate, Asia Industrials
The Hongkong and Shanghai Banking Corporation Limited
sunny.x.y.sun@hsbc.com.hk
+852 3945 3230

## Jennifer Pan\*

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

Our global coverage of companies that provide SOFC

<table><tr><td>Company</td><td>Ticker</td><td>Currency</td><td>Current price</td><td>TP Unchanged</td><td>Rating Unchanged</td><td>Upside/ downside</td><td>Market cap (USDm)</td><td>3m ADTV (USDm)</td><td>P/B 2026e</td><td>P/E 2026e</td><td>ROE 2026e</td></tr><tr><td>Bloom Energy</td><td>BE US</td><td>USD</td><td>302.70</td><td>350.00</td><td>Buy</td><td>15.6%</td><td>86,101</td><td>2,851.5</td><td>61.4</td><td>127.2</td><td>67.6</td></tr><tr><td>Weichai Power – H</td><td>2338 HK</td><td>HKD</td><td>34.10</td><td>50.00</td><td>Buy</td><td>46.6%</td><td>35,400</td><td>102.5</td><td>3.0</td><td>17.5</td><td>12.2</td></tr><tr><td>Weichai Power – A</td><td>000338 CH</td><td>CNY</td><td>27.25</td><td>42.00</td><td>Buy</td><td>54.1%</td><td>35,400</td><td>530.4</td><td>2.7</td><td>16.1</td><td>12.2</td></tr></table>

Source: LSEG Eikon, HSBC estimates. Priced as of close on 30 June 2026

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

View HSBC Global Investment Research at: https://www.research.hsbc.com

1: Simplified power structure of a datacentre  
![](images/429fab600c90f4e2649010a2c9cba9efec8485ad715358ee15a526670a00987d.jpg)  
Source: Company data, coresite.com, Blueocean, HSBC; \*We highlight some relevant companies for utility power and grid operation companies, i.e., American Electric Power (AEP US, not rated), PJM Interconnection (PJM, private), SG (State Grid group, private) and CSG (China Southern Power Grid, private). ATS continuously monitors utility power and shifts the load to backup generators during power outages. UPS is a battery-backed solution used to bridge the grid operation for servers until the backup generators take over the grid supply. Most UPSs have an average capacity of 50 to 300kW, providing around 20-30 minutes of backup power in case of sudden outages. BESS is essentially large-scale rechargeable battery banks with intelligent controls, capable of storing electricity and discharging it on demand. In a datacentre, a BESS typically integrates with the facility's power infrastructure (often alongside UPS units and generators) to provide a reservoir of instantly available energy.

## Comparison of major behind-the-meter prime power solutions

2: Comparison of major prime power solution in the US

<table><tr><td>Metric</td><td>Solid Oxide Fuel Cells (SOFC)</td><td>Aeroderivative GT</td><td>Industrial GT</td><td>Small / Medium CCGT</td><td>H-Class CCGT</td><td>Medium-Speed RICE</td><td>High-Speed RICE</td></tr><tr><td>Typical Unit Size (MW)</td><td>0.3 - 1.0 (Modular Blocks)</td><td>30 - 60</td><td>5 - 50</td><td>40 - 100</td><td>600 - 1,000</td><td>7 - 20</td><td>3 - 5</td></tr><tr><td>Equipment Lead Time</td><td>3 - 4 Months</td><td>18 - 36 Months</td><td>12 - 36 Months</td><td>18 - 36 Months</td><td>36 - 60 Months</td><td>15 - 24 Months</td><td>15 - 24 Months</td></tr><tr><td>Electrical Efficiency</td><td>55% - 65%</td><td>35% - 40%</td><td>35% - 40%</td><td>40% - 55%</td><td>50% - 60%</td><td>40% - 50%</td><td>40% - 50%</td></tr><tr><td>Equipment Cost (USD/kW)</td><td>3,500 - 5,000;2,100-3,500 post subsidies, incl. BOP</td><td>1,000 - 1,200</td><td>1,000 - 1,500</td><td>1,100 - 1,600</td><td>1,000 - 1,400</td><td>700 - 1,100</td><td>500 - 900</td></tr><tr><td>Fully Installed Capital Cost (USD/kW)</td><td>2,800 - 4,500 post subsidies</td><td>1,600 - 1,800</td><td>1,400 - 1,800</td><td>1,700 - 2,300</td><td>1,600 - 2,000</td><td>1,400 - 1,800</td><td>1,200 - 1,600</td></tr><tr><td>LCOE (USD/MWh)</td><td>100 - 200</td><td>80 - 130</td><td>65 - 110</td><td>85 - 160</td><td>60 - 100</td><td>80 - 150</td><td>120 - 200</td></tr><tr><td>Major Maintenance</td><td>Every 5-7 years: complete stack replacements</td><td>Every 3-4 years: Hot gas path overhauls, turbine blade degradation</td><td>Every 4-5 years: Scheduled combustion overhauls</td><td>Every 4-6 years: Complex steam-cycle integration, turbine overhauls.</td><td>Every 4-5 years: Major statutory outage overhauls</td><td>Every 4-5 years: Mid-life top overhauls, bearing inspections</td><td>Every 1-2 years: Frequent lube oil/filter changes, valve adjustments</td></tr><tr><td>Native Output</td><td>Direct Current, Native 800V</td><td>Alternating Current</td><td>Alternating Current</td><td>Alternating Current</td><td>Alternating Current</td><td>Alternating Current</td><td>Alternating Current</td></tr><tr><td>Criteria Emissions</td><td>Negligible / Zero (No combustion)</td><td>Moderate to High (Requires costly SCR)</td><td>Moderate to High</td><td>Moderate (Thermal NOx generation)</td><td>Low to Moderate (Highly optimized utility scale)</td><td>High (Strict local air permit bottlenecks)</td><td>High (Strict local air permit bottlenecks)</td></tr><tr><td>Major Suppliers</td><td>Bloom Energy, Ceres – partnered with Doosan Fuel Cell, Weichai, Delta</td><td>GE Vernova, Siemens Energy, Solar Turbines (CAT)</td><td>Solar Turbines (CAT), Siemens Energy, Kawasaki</td><td>GE Vernova, Siemens Energy, Mitsubishi Power</td><td>GE Vernova, Siemens Energy, Mitsubishi Power</td><td>Wartsila, Everllence, Caterpillar</td><td>Caterpillar, INNIO, Rolls-Royce (MTU), Cummins, Weichai, Yuchai</td></tr></table>

Source: SemiAnalysis, NREL (National Renewable Energy Lab), EIA (Energy Information Administration), Gas Turbine World, DOE (Department of Energy), HSBC; LCOE = Levelized cost of energy, which is a metric that calculates the average cost to generate one unit of electricity over the entire lifetime of a power plant, including initial capital costs, fuel, operations, maintenance, and decommissioning; Fully installed capital cost include all expenses beyond the bare equipment price, such as transportation, civil works, balance-of-plant systems (incl. fuel storage, emissions treatment, cooling, electrical switchgears and transformers, etc.), electrical interconnection, permitting, commissioning, etc., representing the full capital outlay required to bring the system into commercial operation; GT = Gas turbine; CCGT = combined cycle gas turbines; RICE = reciprocating internal combustion engines.

## Rising BTM

Rystad estimates c40% of 2026-30e US data center capacity additions will be located behind-the-meter (BTM). Of a total of 11 GW announced BTM projects, 85% have plans to utilize natural gas for firm power delivery while 10% target renewables and 4% will build out new nuclear capacity. The gap between renewables and nuclear is notable as it highlights the value of dispatchable power for hyperscale's navigating between scaling infrastructure and decarbonization.

3: US data center cumulative upcoming added capacity by power sourcing strategy (GW)  
![](images/91e7d094e88aa093031d249ae39e7c0d9af33e10b75bb31edcdce0c54a902994.jpg)  
Source: Rystad Energy estimates, HSBC  
4: Announced BTM fuel mix

![](images/ff8f364ae9882a13beb85e2613c7820aa8f9519660c78d3ae8d16a8b394a02a8.jpg)  
Source: Rystad Energy, HSBC

Bloom's bi-annual survey of US-based data centre developers find access to power remains the leading constraints for new projects. Longer and less predictable grid interconnection timelines are driving operators to develop materially larger data center campuses and incorporating onsite power generation, signaling a structural shift away from the traditional reliance on the grid. One-third of developers expect to operate fully permanent onsite power by 2030, rising to $45\%$ by the end of 2035.

5. Access to power is the main consideration for US DC developers  
![](images/1125e0b576b92dd6491a127879753f29d2668d161bc6fc727f8c806b0597a5bf.jpg)  
Source: Bloom Energy 2026 Mid-Year Data Center Power Report, HSBC

6. % of data center developers anticipating 100% onsite power  
![](images/c6215cdb2960b9526a7c31dcc8f881740bd70bdfb6b63f56d2892d3593ce4296.jpg)  
Source: Bloom Energy 2026 Data Center Power Report, HSBC

## Comparison of Bloom Energy and Ceres Power

## 7: Global SOFC system competitive landscape, 2023

■ Bloom Energy (US commercial and industrial market, incl. AIDC, with 100-1,000kW system)

■ Mitsubishi Heavy Industries (mainly JP commercial and industrial market with 200-1,000kW system, even combined with gas turbines - MEGAMIE)

■ Aisin Seiki (mainly JP residential market with 700w output per stack)

Others

Source: Global Market Monitor, HSBC

![](images/8c848be1d98b1afde52745301cd3477ddd1bfd233d2c2bb0fdd5010394a19373.jpg)

## 8: Comparison of Bloom Energy and Ceres Power

<table><tr><td></td><td>Bloom Energy (BE US)</td><td>Ceres Power (CWR LN) ecosystem</td></tr><tr><td>Business model</td><td>Asset-heavy integration &amp; equipment sales:builds its own factories; manufactures stacks, integrates BOP systems, and provides long-term O&amp;M services.</td><td>Asset-light IP licensing:earns licence fees, engineering/technical service fees, and long-duration royalties from system integrators (licensees).</td></tr><tr><td>Stack output</td><td>325kW to 80MW (under construction)</td><td>100kW to 108MW (in theory)</td></tr><tr><td>SOFC tech</td><td>Ceramic-base (high cost)</td><td>Steel-base (lower cost)</td></tr><tr><td>Operating temperature</td><td>900°C</td><td>450-630°C</td></tr><tr><td>Cold-start</td><td>Slow</td><td>Faster</td></tr><tr><td>Manufacturing partners</td><td>None. Production is in-house via its Silicon Valley facility and assembly plants in Delaware and Korea.</td><td>Doosan Fuel Cell (336260 KS), Weichai Power (2338 HK/000338 CH), Delta (2308 TT).</td></tr><tr><td>Capacity targets</td><td>2026: 2GW;2030: 5GW.</td><td>2026: Doosan&#x27;s 50 MW plant ready in July 2025; Weichai&#x27;s c30-200 MW plant in 2026-27E; Delta&#x27;s c10 MW by end-2026.2030: Weichai c1 GW.</td></tr><tr><td>AIDC order visibility</td><td>Very high: Oracle (2.8 GW indicative order) and AEP (1 GW framework agreement); USD20bn backlog extends beyond 2028 and excludes a USD25bn strategic AI infrastructure partnership to build AI factories globally with Brookfield Asset Management</td><td>Nil data centre orders yet, but inflection is approaching, as Doosan, Weichai and Delta are ramping up capacity.</td></tr><tr><td>Current average selling price</td><td>USD3,400 per kW (equipment CAPEX only; excludes long-term services and reforming/expansion options).</td><td>Weichai are estimated to price SOFC systems at USD3,000 per kW (RMB20,000 per kW).</td></tr><tr><td>Future ASP reduction targets</td><td>Double digit decline per year.</td><td>Ceres expects 30% cost cut in Endura platform at scale.</td></tr></table>

## Ceres's forecast on SOFC opportunity

9: Global market opportunity for solid oxide by end use case, 2030e

![](images/ff9b8fd39de9f4b3fd1f803af675627cf6dc5f27782a7c50f24af7e20972ad63.jpg)  
Source: Ceres Power forecast, HSBC  
10: Global market opportunity for solid oxide by region, 2030e

![](images/1a93ddcbacda18e786200c6bed4d13e6ec85728ed1abedbc996921761a0b30d3.jpg)  
Source: Ceres Power forecast, HSBC

11: Global market opportunity for SOFC

<table><tr><td>Region</td><td>Key Demand Drivers</td><td>Major Suppliers</td></tr><tr><td>South Korea</td><td>CHPS mandate; national hydrogen roadmap</td><td>Doosan; SK Ecoplant + Bloom</td></tr><tr><td>Taiwan</td><td>Semi/AI power needs vs weak grid; RE100; subsidies (up to NTD70k/kW)</td><td>Bloom; Doosan; Delta</td></tr><tr><td>Japan</td><td>Hydrogen strategy; ENE-FARM CHP legacy</td><td>Kyocera; MHI; Aisin; Bloom</td></tr><tr><td>Southeast Asia</td><td>Data centers shifting to Malaysia/Indonesia with unstable grid conditions</td><td>Weichai; Delta (local ops planned); Bloom in Singapore</td></tr><tr><td>Europe</td><td>High EU-ETS carbon price; IMO marine net-zero targets</td><td>Ceres (licensor); Alfa Laval (marine SOFC); Bloom in Italy, UK</td></tr><tr><td>Australia/India</td><td>Remote/off-grid (mining); DC backup</td><td>Early-stage; local partners with global SOFC players; Bloom in India</td></tr></table>

Source: government website, company data, HSBC; CHPS (Clean Hydrogen Portfolio Standard) mandate forces utilities to procure clean power; RE100 is a global corporate initiative led by the Climate Group, requiring members to source 100% of their electricity from renewable sources by 2050; ENE-FARM is Japan's residential fuel cell cogeneration system that extracts hydrogen from city gas to generate electricity while capturing waste heat for water heating. EU-ETS = EU Emission Trading System. IMO = International Maritime Organization

## Typical structure of a SOFC system

A Solid Oxide Fuel Cell (SOFC) is a high-temperature electrochemical device that converts the chemical energy of a fuel – hydrogen ( $H_{2}$ ), carbon monoxide (CO), natural gas/methane ( $CH_{4}$ ), syngas (CO + $H_{2}$ ), and biogas ( $CH_{4}$ + $CO_{2}$ ) – directly into electricity

12: Typical structure of a SOFC system  
![](images/c185658e63ee4212cf851f4435017058a9260fbb2bba5afecdc316d89b3f42a7.jpg)  
Source: chibaogao.com, HSBC

13: Typical structure of a SOFC cell  
![](images/68c19db0c3d7f539b752de3e14fb992f2bc7747237346804f6a2e2613efc450d.jpg)  
Source: Fuel, HSBC  
A system

14: Cost breakdown of a SOFC system and a stack (based on DOE's analysis in 2017 for the production of 1,000 units of 250kW stack per year)

![](images/6ab754eb29f0e502f2f5e0090ee322321f2a116938a3a90536710c515f5c8185.jpg)  
Source: DOE, HSBC

## Other fuel cell techs

Quick review of the major applications of hydrogen and the major fuel cell types

15: Major applications of hydrogen products

<table><tr><td>Category</td><td>Typical power range</td><td>Typical fuel cell type</td><td>Example</td></tr><tr><td>Portable</td><td>1W to 20kW</td><td>PEMFC, DMFC, SOFC</td><td>Portable power, unmanned aerial vehicles</td></tr><tr><td>Stationary</td><td>0.5kW to 2MW</td><td>PEMFC, DMFC, SOFC, MCFC, PAFC</td><td>Combined heat and power, uninterruptible power system, power generators</td></tr><tr><td>Transportation</td><td>1kW to 300kW</td><td>PEMFC, DMFC</td><td>PVs, trucks, buses and coaches, aviation, marine, e-bike</td></tr><tr><td colspan="4">Source: E4Tech, HSBC</td></tr></table>

16: Types of fuel cells by electrolyte used

<table><tr><td>Item</td><td>Proton exchange membrane (PEMFC)质子交换膜燃料电池</td><td>Alkaline (AFC)碱性燃料电池</td><td>Molten carbonate (MCFC)熔融碳酸盐燃料电池</td><td>Phosphoric Acid (PAFC)磷酸燃料电池</td><td>Solid Oxide (SOFC)固体氧化物燃料电池</td><td>Direct Methanol (DMFC)直接甲醇燃料电池</td></tr><tr><td>Fuel</td><td> $H_2$ , Methanol</td><td> $H_2$ </td><td>Natural gas; Liquefied petroleum gas; Gas</td><td>Natural gas; Liquefied petroleum gas; Methanol</td><td>Natural gas; Liquefied petroleum gas; Gas</td><td>Methanol</td></tr><tr><td>Electrolyte</td><td>Fluorinated proton membrane</td><td>Potassium hydroxide (KOH)</td><td> $Li_2CO_2-K_2CO_2$ </td><td>Phosphate</td><td>Yttria-stabilized zirconia (YSZ)</td><td>Fluorinated proton membrane</td></tr><tr><td>Electrolyte condition</td><td>Solid-based</td><td>Water-based</td><td>Water-based</td><td>Water-based</td><td>Solid-based</td><td>Solid-based</td></tr><tr><td>Cathode</td><td>Pt/C</td><td>Pt/Ag</td><td>Li/NiO</td><td>Pt/C</td><td>Sr/LaMnO3</td><td>Pt/C</td></tr><tr><td>Anode</td><td>Pt/C</td><td>Pt/Ni</td><td>Ni/Al; Ni/Cx</td><td>Pt/C</td><td>Ni/YSZ</td><td>Pt/C; Ru/C</td></tr><tr><td>Core temp</td><td>50–100°C;80°C typical<

[中间内容因长度限制已省略]

is publication has been distributed by HSBC Continental Europe or by such other HSBC affiliate from which the recipient receives relevant services.

In Japan, this publication has been distributed by HSBC Securities (Japan) Co., Ltd.. It may not be further distributed in whole or in part for any purpose. In Korea, this publication is distributed by either The Hongkong and Shanghai Banking Corporation Limited, Seoul Securities Branch ("HBAP SLS") or The Hongkong and Shanghai Banking Corporation Limited, Seoul Branch ("HBAP SEL") for the general information of professional investors specified in Article 9 of the Financial Investment Services and Capital Markets Act ("FSCMA"). This publication is not a prospectus as defined in the FSCMA. It may not be further distributed in whole or in part for any purpose. Both HBAP SLS and HBAP SEL are regulated by the Financial Services Commission and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.
"""
