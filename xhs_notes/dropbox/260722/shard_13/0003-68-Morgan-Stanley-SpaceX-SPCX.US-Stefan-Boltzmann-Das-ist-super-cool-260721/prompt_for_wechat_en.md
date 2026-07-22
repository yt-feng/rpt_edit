You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
July 21, 2026 09:00 PM GMT

SpaceX | North America

# Stefan-Boltzmann: Das ist super cool

Space is 2.7 Kelvin (negative 455 degrees Fahrenheit)... but space is not cold. Confused yet? Don't panic. Two 19th-century Austrian physicists got your back. Engineers have been keeping satellites and other spacecraft from overheating for many decades. Really.

## Please see here for our SpaceX Initiation: SpaceX: AI's Final Frontier; Initiate at Overweight, PT \$300 (7 Jul 2026)

From our client discussions there seems to be a hearty contingent who believe that space-based AI infrastructure quickly confronts physical limitations of thermal management in a vacuum, where convective cooling through air or water cannot be used in space. This note is meant to outline how space-based computers, and other heat-generating apparatuses, may indeed be thermally managed within operating design limits. Some high level thoughts:

\- Thermal management in space is done through radiative cooling - ever since early satellites of the 1960s. The US even launched a nuclear reactor to space in 1965 (SNAP-10A) and operated it for 43 days.

\- The International Space Station (ISS) uses fluid loops with ammonia (stays liquid across a wide range of temperatures), pumped out to large radiator panels that 'glow' in infrared. Experts believe SpaceX will use a similar technique with some tweaks.

\- SpaceX is targeting an eventual 370 Kelvin (97 °C) operating temperature for its Al sats to benefit from greater heat-flux between chip and space and increase efficiency of the radiator. We assume \~360K (\~87 °C) at the high-end of terrestrial GPU operating temps for the initial version of the sats to launch in 2028.

\- For a 1kW computer running at \~90 degrees Celsius in space, the radiator panel surface area would need to be approximately 0.57 square meters (assuming \~0.90 emissivity for white thermal control paint and two radiating sides).

\- Deep space is 2.7 K, but environmental heat inputs (Earth IR, albedo) raise the equilibrium radiative sink seen by a radiator in LEO. NASA technical guidance on effective sink temperature does acknowledge this and suggests an equivalent LEO sink temp between 200 and 300 K (we assume 250 K in our model or negative 23 °C - still cold).

\- Emissivity is how good a surface is at radiating heat - measured on a scale of 0 to 1. A measure of 1.0 would be 'perfect' radiation of heat into space. A measure of 0.0 is a perfect reflector that does not radiate any heat at all.

\- In our model, we assume the Gen 1 SpaceX AI sat achieves 150kW of peak power (120kW of compute), implying a radiator size of 110 square meters per

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Adam Jonas, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Adam.Jonas@morganstanley.com</td><td>+1 212 761-1726</td></tr><tr><td colspan="2">William Tackett, CFA</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>William.Tackett@morganstanley.com</td><td>+1 212 761-6028</td></tr><tr><td colspan="2">Kristine T Liwag</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Kristine.Liwag@morganstanley.com</td><td>+1 212 761-2980</td></tr><tr><td colspan="2">Justin M Lang</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Justin.Lang@morganstanley.com</td><td>+1 212 761-6251</td></tr></table>

## SpaceX (SPCX.O, SPCX US)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$300.00</td></tr><tr><td>Shr price, close (Jul 20, 2026)</td><td>$119.85</td></tr><tr><td>52-Week Range</td><td>$225.64-119.68</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS ($)**</td><td>(1.69)</td><td>0.28</td><td>2.18</td><td>6.29</td></tr><tr><td>Prior EPS ($)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>P/E</td><td>NM</td><td>423.3</td><td>54.9</td><td>19.1</td></tr><tr><td>EPS ($)§</td><td>-</td><td>(0.42)</td><td>0.63</td><td>3.24</td></tr><tr><td>Div yld (%)</td><td>-</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework

\*\* = Based on consensus methodology

§ = Consensus data is provided by Refinitiv Estimates

e = MS estimates

<table><tr><td>Quarter</td><td>2025</td><td>2026e Prior</td><td>2026e Current</td><td>2027e Prior</td><td>2027e Current</td></tr><tr><td>Q1</td><td>(0.18)</td><td>-</td><td>(0.84)a</td><td>-</td><td>0.54</td></tr><tr><td>Q2</td><td>(0.34)</td><td>-</td><td>(0.35)</td><td>-</td><td>0.55</td></tr><tr><td>Q3</td><td>(0.36)</td><td>-</td><td>0.27</td><td>-</td><td>0.54</td></tr><tr><td>Q4</td><td>(0.80)</td><td>-</td><td>0.45</td><td>-</td><td>0.56</td></tr></table>

e = MS estimates, a = Actual Company reported data

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

side assuming 2 radiating sides or roughly half the size of a standard singles tennis court.

\- This is largely based on the AI1 sat design initially shared by Elon Musk/SpaceX last month. While Musk has since suggested peak power could rise by $\sim 2\frac{1}{3}$ with battery assistance, the impact on sustained compute density is not yet clear. We expect the design to iterate significantly before 2028 deployment and will update our assumptions when more technical details are released.

\- The AI compute portion of our SpaceX model makes detailed assumptions about the satellite radiator, incorporating emissivity coefficients and the Stefan-Boltzmann constant (more details in following section).

\- Radiator mass accounts for $>1/3$ of the total mass of an AI satellite. The hotter you can run the chips, the smaller you can keep the radiator. Running an AI chip at a $20\%$ higher temperature requires $50\%$ less radiator mass.

19th and Early 20th Century Physics. The fundamentals of managing temperatures in space traces its roots to 19th century physicists including the work of Josef Stefan, Ludwig Boltzmann, and Max Planck.

Black body radiation. Any object with temperature above absolute zero emits electromagnetic radiation.

The Stefan-Boltzmann Law in simple language: The hotter something is, the much more energy it radiates. If you double the temperature of an object, it radiates at 16x as much heat.

Exhibit 1: Stefan-Boltzmann Law lets you size the radiator surface area needed to reject a given heat load, based on the surface's temperature and emissivity.

![](images/87e7494de8e7f0939476f773391ad6d47e726229d860bf9ddc73672dade4c07a.jpg)  
Source: MS

Max Planck. A pioneer of quantum mechanics. Objects in space lose heat by radiating it into the vaccum (black body) - almost entirely infra red light. This is the same principle that we see with everyday objects that get hot on earth such as a glowing stove burner or a hot coal in your smoker. In 1900, Planck figured out that energy is emitted in discrete packets (quanta). Planck ultimately won the Nobel Price in 1918 for his discovery of energy quanta.

None of this is to say that building data centers in space is easy. Thermal management is solvable within well-understood physics, but it is only one problem among several, and arguably not the binding constraint. Orbital compute still has to contend with radiation damage beyond the protection of Earth's magnetosphere, the physical security of assets in a domain no one owns, lack of maintenance that must be handled remotely through built-in redundancy rather than hands-on repair, a launch cadence that potentially yields only single-digit megawatts per flight at first, reliance on the same capacity-constrained chip supply chains as terrestrial AI, and a growing orbital-debris hazard in low Earth orbit. The point of the thermal discussion above is deliberately narrow: heat rejection in a vacuum is not the physical showstopper some assume, which shifts the real debate to cost, reliability, scalability, and time-to-power.

We thank Herr Doktor Stefan and Herr Doktor Boltzmann for their contributions to science - we wouldn't have data centers in space without them.

Exhibit 2: Max Planck  
![](images/5334bb75dec5fd538988202d7327a189fbeffc4040bdf2fd6f6f7dd0d5565697.jpg)

Exhibit 3: Josef Stefan and Ludwig Boltzmann

![](images/402401ea57bfaeeec705114e254d421684897814513e6afca3c4cbdf034a0fff.jpg)  
Source: Wikipedia

![](images/fb9ef47e83d9a7a71f22b4de6c83875198b09ac72d55e1ae9e8b5b4b87f11536.jpg)  
Source: Wikipedia

## SpaceX Orbital Compute Estimates

We model SpaceX reaching GW-scale orbital compute in 2030, with orbital capacity becoming the majority of deployed compute in 2032. Our forecast assumes first orbital compute deployments in 2028 at 160 MW, rising to approximately 2.7 GW in 2030. From there, orbital compute reaches 21.2 GW in 2032, or 58% of total compute capacity, before scaling to 111 GW in 2035, or 88% of total, and 364 GW in 2040, or 96% of total. Long term, we envision terrestrial compute primarily supporting model training, while most inference moves to orbit.

When accounting for total operating costs, our estimates imply that incremental orbital compute becomes cost-advantaged versus current industry terrestrial costs in 2031. We believe investors should evaluate cost parity on an all-in basis, particularly opex, because most ongoing costs associated with orbital compute are depreciation, while terrestrial compute has meaningful recurring power, cooling, land, staffing, maintenance, and site operating costs. Based on our internet team's recent estimate of industry avg Blackwell costs of \~\$6.8 per watt per year, we estimate incremental SpaceX orbital compute falls below that level in 2031, at \$32.4 per watt of capex divided by a five-year useful life, or approximately \$6.5 per watt per year.

On our capex estimates alone, orbital is significantly higher than terrestrial in the initial years of deployment before falling to within 50% more than terrestrial in 2031 and parity around 2035 due to falling launch costs, cheaper satellite hardware, and GPU costs that get closer to parity with terrestrial. However, this is 1) comparing SpaceX orbital and SpaceX terrestrial capex estimates in the same year while SpaceX has materially cheaper cost to deploy compute terrestrial vs. the industry (potentially <50% ex-compute); and 2) only looking at capex costs whereas a significant portion of savings from orbital compute is due to the lack of material opex, i.e., no power/cooling or maintenance costs.

Exhibit 4: Our estimates imply orbital has cost advantage vs. current industry terrestrial costs in 2031 (Bars are orbital capex for newly deployed capacity divided by 5 year useful life, i.e., ongoing depreciation expense for new capacity, since vast majority of ongoing orbital compute expense is depreciation on upfront capex)

![](images/9857adefad16fb7e8ee212c44fce2700b3aadce9af6dd4c64464281cae0d32ae.jpg)  
Note: For orbital compute, uses newly deployed capacity in any given year not avg compute in use. \$6.8 calculated using \$23.5 chip capex per watt at a 5 year useful life, \$9.3 infrastructure capex at a 15 year useful life, and \$1.5 of power and other operating costs.
Source: MS estimates

Orbital Compute helps drive materially lower cash costs/watt into the 2030s and long-term EBIT margins of >50%. We estimate overall cash costs per watt (inclusive of capex and non-D&A operating costs) declines from a current \~\$35-40/watt to <\$9/watt in 2035 and \$3.7/watt in 2040. This helps drive EBIT margins from \~42% in 2028 (first year of deployment) to roughly 50%+ in the 2030s. This compares to 2025 EBIT margins for Amazon AWS of \~35%, Microsoft Intelligence Cloud of \~42%, and Meta of \~41%. Note that EBIT margin increase is limited beyond this point because we are assuming SpaceX passes savings onto customers as a trade-off for growth, with total AI revenue/watt declining from \$16.6 in 2028 to \$7.3 by 2040.

\- To help justify our opex savings, we estimate electricity costs of SpaceX's AI over time given that this is one major cost item only relevant to terrestrial compute. In 2028 (first year of orbital deployment), we estimate electrical costs at \~10% of revenue which declines to 5% by 2033, 2% by 2035, and 1% by 2040.

Cost alone doesn't tell the full story. Cost is one aspect of scalability, but orbital compute could also have advantages in time-to-power, access to energy, permitting risk, local land and water constraints, and the ability to deploy repeatable infrastructure in parallel. In AI infrastructure, customers may pay a premium for near-term access to large-scale compute if terrestrial capacity remains constrained by grid interconnect queues, equipment availability, and site development timelines. This has been recently evidenced by SpaceX's two neocloud deals, which appear to have commanded a meaningful premium to industry averages, likely reflecting the scarcity value of high-end, large-scale GPU clusters that can be accessed relatively quickly. In other words, even if orbital compute does not initially reach cost parity with terrestrial compute, the company may still be able to charge a material premium if it becomes the most scalable AI infrastructure provider available. This would be analogous to SpaceX's current launch business, where prices have continued to rise despite steadily declining underlying costs. The key debate, in our view, is whether SpaceX can use Starship, satellite manufacturing, space-based solar power, and optical networking to become one of the most scalable sources of AI compute in the 2030s.

Exhibit 5: Annual SpaceX Nameplate Compute (GW): Orbital vs. Terrestrial  
![](images/b2fb5b3b9c09a0b11cf950bfd2ac6e9a73b2c134a9f7b21472b7f0e797fe4204.jpg)  
Source: Company Data, MS estimates  
Note: Slight dip in early 2030s is due to initial depreciation on orbital compute which is assumed to have higher initial capex cost vs. terrestrial.

Exhibit 6: Orbital Compute Deployed Becomes Meaningful in 2030; Helps Drive Materially Lower Cash Costs Long-Term for AI  
![](images/2870bbf729b0f9616927ad52f29bff15d1cc7db80c72f3c42b95d295ac3655df.jpg)  
Exhibit 7: Estimated AI EBIT Margins. We assume long-term savings are partially offset by declining revenue/watt.  
Source: Company Data, MS estimates  
Source: Company Data, MS estimates

![](images/b3539dd9f1442958376504e3800ee216c070593768f44937b91727c2fdc322e4.jpg)

Exhibit 8: Estimated Electricity Costs for AI Compute (\$mn)  
![](images/77c9228c2667d3183ad59a47a7323dde3a9c0df7f2f3430e722b1c94e8a4d499.jpg)  
Note: Estimated as terrestrial compute watts \* \$0.15 kWh, assuming a PUE of 1.2 and 24/7 operations.
Source: Company Data, MS estimates

Exhibit 9: MW of Compute in Orbit  
![](images/b1a1c38e816a043644e3d8e6f4a913c01369af74406ca5d6ac8093f4059f7923.jpg)  
Source: Company Data, MS estimates

Exhibit 10: Annual Orbital Compute Launches  
![](images/0eb3e4595f1a430c5c352d3769190fa1b46d5aa829d926bcc94b921013bfe820.jpg)  
Source: Company Data, MS estimates

## Detailed Orbital Compute Engineering & Capex Assumptions

We have constructed a detailed bottom-up build of SpaceX orbital compute (recently dubbed 'Starmind') which informs our capex estimates. We model 3 generations of SpaceX orbital compute aligning with estimated variants of Starship. We align our initial generation of orbital compute to the Al1 Sats shared recently by Elon Musk (70 kW/ton or 56 kW/ton - compute only; 150 kW peak power; \~2.1 tons) which we expect to launch on Starship V3. We assume this is largely a prototype version for the company and that future iterations will be both larger and more compute dense to get closer (and eventually greater than) the targeted 100 kW of compute per ton targeted by the company. Orbital compute sats, while novel concepts, are based on existing satellite technology leveraged on Starlink. The satellite can largely be divided into 3 parts: 1) Thermal Radiator; 2) Solar Array; 3) Compute Payload. We outline our assumptions for the solar array and thermal radiator below.

## • Thermal Radiator Design:

We would like to address up-front that there has been a major debate recently on the ability to radiate heat in space which we think is significantly overblown. Thermal radiation in space has been a field of study since the advent of spacecraft (all electronics radiate heat), and the constraints are relatively known and well-documented in scientific research. Investors also frequently point to the fact that heat of compute is much higher than that of typical satellite hardware, which is true, but also overlooks the multi-decades of international research on even hotter payloads such as in-space nuclear power where test satellites have been launched and operated in space since the mid-1960s.

• Thermal radiator specifications are guided by the Stefan-Boltzmann Law which defines the required surface area to radiate a given level of heat. After that, we estimate the areal density (kg/m $^{2}$ ) of the radiator to determine the total mass.

\- Compute Temp. To benefit from Stefan-Boltzmann's law which states that radiation efficiency is directly related to the heat differential between the radiator and background temp, we assume chips are designed to run slightly hotter than on Earth at \~90 °C (362 K) initially which rises to 97 °C and 99 °C in later generations. Note that space radiators currently operate as hot as 300 to 400 K depending on the application. This likely does require new compute designs – see below for more.

\- Emissivity Factor. We assume a 0.91 emissivity factor in all generations corresponding to the advertised emissivity of spacecraft thermal control paint.

• Background Temp of LEO. We assume the background temperature of LEO is 250 K or -23 °C. The background temperature of deep space is much lower at just 2.7 K. However, spacecraft radiator sizing in LEO should use an effective sink temperature materially higher due to environmental heat inputs (Earth 

[中间内容因长度限制已省略]

s affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Space Technology

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/20/2026)</td></tr><tr><td>Adam Jonas, CFA</td><td></td><td></td></tr><tr><td>SpaceX (SPCX.O)</td><td>O (07/07/2026)</td><td>$119.85</td></tr><tr><td>Gogo Inc (GOGO.O)</td><td>E (08/14/2025)</td><td>$3.51</td></tr><tr><td>Iridium Communications Inc (IRDM.O)</td><td>E (01/16/2026)</td><td>$46.41</td></tr><tr><td>MDA Space Ltd (MDA.TO)</td><td>O (01/16/2026)</td><td>C$42.17</td></tr><tr><td>Viasat Inc (VSAT.O)</td><td>E (12/15/2017)</td><td>$69.51</td></tr><tr><td colspan="3">Kristine T Liwag</td></tr><tr><td>Firefly Aerospace Inc (FLY.O)</td><td>E (09/02/2025)</td><td>$19.67</td></tr><tr><td>HawkEye 360 Inc (HAWK.N)</td><td>O (06/01/2026)</td><td>$17.44</td></tr><tr><td>Planet Labs PBC (PL.N)</td><td>E (01/22/2023)</td><td>$22.15</td></tr><tr><td>Rocket Lab USA Inc (RKLB.O)</td><td>O (01/16/2026)</td><td>$65.74</td></tr><tr><td>Virgin Galactic Holdings Inc (SPCE.N)</td><td>U (11/22/2023)</td><td>$2.56</td></tr><tr><td>Voyager Technologies Inc (VOYG.N)</td><td>U (07/15/2026)</td><td>$24.96</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
