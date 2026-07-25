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
![](images/1d1269ea578dd0a587770a12f947961ed67b89471954794a6cff92b206749ce4.jpg)

July 22, 2026 10:25 PM GMT

# Greater China Semiconductors | Asia Pacific

# Cloud Semis: Unlikely to slow down

We expect both CPU and GPU server TAM to expand into 2027. We reiterate our OW ratings on both Aspeed and Montage into earnings; accumulate into cloud capex prints.

## Key Takeaways

\- Our recent China World AI Congress trip suggests ongoing upside for CPU servers, from both China and US vendors.

The more diversified scale-up solutions for GPU servers in 2027 should translate into strong cloud semis growth.

■ Better product mix should support the high GMs for both Aspeed and Montage.

CPU server segment showing more upside, especially in China: We maintain our bull thesis (Cloud semis: Much Larger TAM Ahead) and expect further upside. In our July 17-20 Shanghai WAIC trip, we noted increasing adoption of AMD, Nvidia and Hygon solutions. AMD's multicore benefits, Nvidia's Vera bundle sales strategy, and Hygon's government support and performance catch-up with legacy 6 gen Intel CPU are now attracting increasing orders (see Hygon initiation). High-end x86 CPU pricing continued to trend up in China, nearly 2x Y/Y.

GPU servers strong, with potentially more SuperPods solutions: Almost every domestic GPU vendor displayed a 64- or 128-card scale-up system. Chinese AI GPUs are limited by wafer production/supply at the chip level, but try to connect each GPU together (WAIC note). Nvidia could also have a greater variety of racks in 2027 (see Joe Moore's Nvidia NDR note). We believe SuperPods could be one of the solutions, connecting multiple racks with optics (multi-racks scale-up). Kimi K3 also demonstrated the Nvidia GPU importance in training.

Margin likely to be maintained at high levels: We think cloud semis vendors will benefit from spec migration, driven by strong high-performance server demand. Gross margins for the new solutions (e.g., AST 2700 BMC, legacy BMC with software offering and DDR5 gen 3 interface) are usually higher than that of the prior solutions, which could help offset the higher cost burden, especially from OSAT.

Buy into cloud capex earnings; OW Aspeed and Montage: We believe the upcoming cloud capex announcements could see meaningful upward revision, mainly for memory, but also yielding positive signs for cloud semis companies. We factor in share dividend impact and cut our Aspeed price target, by 11%, to NT \$20,888. We think the Korean government's investigation (see results note) offers a good entry point for Montage.

MS TAIWAN LIMITED+

Charlie Chan
Equity Analyst
Charlie.Chan@morganstanley.com +886 2 2730-1725

Daisy Dai, CFA
Equity Analyst
Daisy.Dai@morganstanley.com +852 2848-7310

Tiffany Yeh
Equity Analyst
Tiffany.Yeh@morganstanley.com +886 2 7712-3032

## MS ASIA LIMITED+

Ethan Jia
Research Associate
Ethan.Jia@morganstanley.com +852 3963-2287

Asia Summer School 2026

<table><tr><td colspan="2">GREATER CHINA TECHNOLOGY SEMICONDUCTORS</td></tr><tr><td>Asia Pacific Industry View</td><td>Attractive</td></tr></table>

## WHAT'S CHANGED

<table><tr><td>Aspeed Technology(5274.TWO)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>NT$21,323.64</td><td>NT$20,888.00</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Key charts

The baseboard management controller (BMC) integrated circuit (IC) (i.e., a specialized microchip) is the key component on the server board. It helps enable remote control for the server firmware system and maintain datacenter stability. Previously, Aspeed indicated that general servers and AI ASIC servers actually generate higher efficiency in hyperscaler capex spending (Exhibit 1). As a result, as the CPU plays a critical role in enabling agentic AI (as the central coordinator that executes instructions, manages system resources, and ensures reliable, real-time decision-making), we expect the growing demand for CPUs/general servers to further lift Aspeed's BMC revenue in the coming years.

Currently, Aspeed has \~70% sales market share in the CPU server BMC market, with major US and Chinese hyperscalers being its end-customers, including Meta, AWS, Alibaba and Microsoft. As it migrates into the new generation BMC product – AST2700 – we expect it to expand its market share in customers including Dell and Google, which would help expand its revenue, as spec migration also brings 40-50% ASP increase.

Exhibit 1: General servers and AI ASIC servers generate the highest capex efficiency for BMCs  
![](images/bb850424117fb07526212e3d3df1eae0f343315f4729b35410c8f8472de91a84.jpg)  
Source: Company data, MS. Note: Capex efficiency is defined as the amount of server spend that will contribute to one BMC demand. The lower the capex efficiency, the better for Aspeed.

Aspeed, in April, announced an increase in its BMC TAM, from 46.5mn to 65.77mn units in 2030, driven by AI-related general server demand. We think agentic AI will be the key driving force behind this growth. General server growth should be stable at 6% over 2025-30, while AI-related general servers should account for: 1) 25% of total 2026 general server demand; 2) 45% in 2027; and 3) 20% throughout 2028-30 (see Exhibit 29).

On the order visibility front, customers began providing forecasts at 7-8x Aspeed's single-month revenue. Although Aspeed could not roll out any double booking, the current dynamic is that shipments are well beyond all customers' needs. Customers also expect to double capacity Y/Y in 2027.

## Exhibit 2: Aspeed expects its BMC TAM to reach 65.7mn units in 2030

## BMC TAM Forecast Revised

\- We see huge demand for AI-related General Server for agentic AI workload and simple inference tasks.
- BMC TAM is estimated to be 65.77 million units in 2030.

![](images/5719d698d92319887be2a76c5354108f582aacbcf162a5c1cd5236ce67bdd3e0.jpg)  
Note : 1) BMC for General Servers will grow at 6% CAGR.
2) BMC for AI-related General Servers is estimated to be 8.5 million in 2026, with 45% growth rate in 2027 and 20% thereafter.
3) BMC for GPU servers and AI ASIC servers in 2026 is based on the estimate of GPU and AI ASIC shipment and the server architecture.
4) Assuming BMC for GPU Servers grow at 45% in 2027 and 20% afterwards. We also include BMCs for ICMS here.
5) Assuming BMC for AI ASIC Servers grow at 45% in 2027 and 20% afterwards.  
Source: Aspeed  
Delivering quantum-resilient OCP Caliptra security across the entire ASPEED product portfolio.

Exhibit 3: Aspeed's product roadmap

![](images/9584f6f8230cd7001a18b8c6bdbeb0e1f61b17a5f78426bb7139f7f7e0ab9981.jpg)  
Source: Aspeed

Exhibit 4: Aspeed Product Roadmap  
![](images/fbf403efd9778cc77a8d38442189da3f18b2b3c72a097814855a11e4704c51d9.jpg)  
Source: Aspeed

Exhibit 5: Server-related companies maintain high Y/Y revenue growth – but slowing a bit because of a high base  
![](images/b60e2a4edbeae2a41f8444fe16df08ed4c8091230ac7c28cac4be7e15acc7479.jpg)  
Source: Company data, MS. Note: Monthly revenue includes revenue from Aspeed, Wiwynn, Accton, Lotes, Inventec, Quanta, LandMark, Giga-Byte, TSMC, KYEC, AllRing, FOCI, AVC, Auras, Gold Circuit, Unimicron, and Hon Hai.

Exhibit 6: Full-year processor exports increased 68% y/y in 2025  
![](images/c5c253ac0875c3edfafbff5ebc6311494ee95e9ac140d65e0b1208b357fa430c.jpg)  
Source: International Trade Administration, MS.

Exhibit 7: Processor exports maintain strength, with 20 consecutive months of Y/Y growth  
![](images/780f38eb63d5192a819fb47d011f78c29d19c2a9724059abea12fab684c8bd35.jpg)  
Source: International Trade Administration, MS.

Exhibit 8: Data center construction spending rose 35% Y/Y while other office spending declined  
![](images/a6be339e983e6a77c1541fa1cbaf69f1b10957faa02d0dece0ab82cdbabc5937.jpg)  
Source: United States Census Bureau, MS.

Exhibit 9: 1Q26 US cloud capex increased 64% Y/Y, maintaining a level similar to the 65% Y/Y rise in 3Q25  
![](images/6c97c71c0552a3cccfee4b19c9bbcfad41a5e31b7952e3e579d39094ca7be38f.jpg)  
Source: Company data, MS. US cloud capex calculated from Alphabet, Microsoft, Amazon, and Meta.  
Top 14 Cloud Providers: Cloud Capex Y/Y Growth

Exhibit 10: Post-US hyperscaler C1Q26 earnings, our cloud capex tracker is now pointing to 92% Y/Y growth in 2026, up 5ppt from the prior forecast of +87% Y/Y in late March 2026

![](images/f4720de36ad3e627f15aa0227a906fabaf677bc9b6f2ea195e071dae33abe8b7.jpg)  
Source: Company data, FactSet, MS. Note: Cloud capex includes capex from Alphabet, Amazon, Microsoft, Meta Platforms, Alibaba, Tencent, Baidu, CoreWeave, Apple, IBM, Nebius, IREN, Tesla and Oracle. We start to include CRWV from 2024.

Exhibit 11: Cumulatively, the top 14 cloud players are expected to devote US\$916bn to capex in 2026 (MSe), up from US\$476bn in 2025

Cloud Capex Spending (\$ Billions)  
![](images/475d874ee28a1f412f0a28f88f4010e04c33d55faaab9573ad54e285a31c1127.jpg)  
Source: FactSet, MS (E) estimates. Note: ORCL forecasts not updated following latest earnings.

Exhibit 12: With stronger cloud capex now expected in 2026, overall capital intensity is now exceeding 31%, a new all-time high

Top 14 Cloud Providers: Capital Intensity  
![](images/bbeaf6f73030e90558438ae6c35e5b37c047e3d3d1a82ed56a1ab0ba639d16c2.jpg)  
Source: FactSet, MS (E) estimates. Note: Dark blue bars based on consensus estimates, light blue bar based on MSe. ORCL forecasts not updated following latest earnings.

Exhibit 13: Quarterly Aspeed shipments Y/Y and Intel + AMD CPU shipments Y/Y  
![](images/4e24ca69f5d680b9a3d5f0b5e71371ae4ab9f6fb357c3afe2187481414349aea.jpg)  
Source: Company data, MS (E) estimates.

## Gauging the AI ASIC BMC TAM

Aspeed maintains the lion's share in AI servers, including at NVIDIA, AMD and Trainium. Google TPU has long used MCUs for remote control. Starting with TPUv8t (codename: Sunfish), given better performance, we expect Google to adopt Aspeed's AST2700 BMC controller. Together with our latest updates on 2027e CoWoS and implied ASIC shipment, we estimate an additional $4\%$ revenue contribution in 2026 and $14\%$ in 2027.

Together with other ASICs (mainly TPU, MTIA, and Teton), we expect ASIC racks to contribute 10% and 21% of Aspeed's total revenue in 2026 and 2027, respectively. Further upside potential could come as orders beyond 2026 remain uncertain for now, and other ASIC players – including Microsoft, SoftBank/Arm, Apple, and Fujitsu – all plan to build ASIC servers in the coming years.

We therefore expect AI ASIC servers to strengthen Aspeed's growth over the next few years.

Exhibit 14: Gauging the ASIC TAM for Aspeed: We expect 2026-27 to see ASIC racks contribute respective 10% and 21% of its total revenue

<table><tr><td colspan="7"></td><td colspan="3">2026e chip shipment</td><td colspan="3">2027e chip shipment</td></tr><tr><td>CSP</td><td>Rack</td><td>Rack MP time</td><td>Accelerator name</td><td>BMC Generation</td><td>BMC to ASIC per rack %</td><td>BIC to ASIC per rack %</td><td>Accelerator chip shipment (k units)</td><td>BMC (k units)</td><td>BIC (k units)</td><td>Accelerator chip shipment (k units)</td><td>BMC (k units)</td><td>BIC (k units)</td></tr><tr><td rowspan="2">AWS</td><td>Teton3</td><td>2H26-2027</td><td>Trainium 3</td><td>AST2700</td><td>69%</td><td></td><td>1,700</td><td>1,181</td><td></td><td>2,380</td><td>1,653</td><td></td></tr><tr><td>Teton4</td><td>1H28</td><td>Trainium 4</td><td>AST2700</td><td>69%</td><td></td><td></td><td></td><td></td><td>150</td><td>104</td><td></td></tr><tr><td rowspan="3">Google</td><td>TPU v8i</td><td>2026</td><td>Sunfish</td><td>AST2700</td><td>70%</td><td></td><td>900</td><td>630</td><td></td><td>4,000</td><td>2,800</td><td></td></tr><tr><td>TPU v8t</td><td>2026</td><td>Zebrafish</td><td>AST2700</td><td>70%</td><td></td><td>500</td><td>350</td><td></td><td>3,000</td><td>2,100</td><td></td></tr><tr><td>TPU v9</td><td>2027</td><td>Humufish</td><td>AST2700</td><td>70%</td><td></td><td></td><td></td><td></td><td>150</td><td>105</td><td></td></tr><tr><td>Meta</td><td>Santa Babara</td><td>2026-2027</td><td>MTIA 3 Iris &amp; 3.5 Arke</td><td>AST2700</td><td>100%</td><td></td><td>150</td><td>150</td><td></td><td>550</td><td>550</td><td></td></tr><tr><td colspan="7">Total BMC and BIC shipment (k units)</td><td colspan="3">2,311</td><td colspan="3">7,312</td></tr><tr><td colspan="7">AST2700</td><td colspan="3">2,311</td><td colspan="3">7,312</td></tr><tr><td colspan="13">BIC</td></tr><tr><td colspan="13">BMC ASP (US$)</td></tr><tr><td colspan="7">AST2700</td><td colspan="3">25</td><td colspan="3">25</td></tr><tr><td colspan="13">BIC ASP (US$)</td></tr><tr><td colspan="7">Revenue contribution from ASIC (US$mn)</td><td colspan="3">57,764</td><td colspan="3">182,799</td></tr><tr><td colspan="7">Revenue contribution from ASIC (NT$bn)</td><td colspan="3">1,733</td><td colspan="3">5,484</td></tr><tr><td colspan="7">Aspeed CY Revenue (NT$bn)</td><td colspan="3">17,866</td><td colspan="3">26,027</td></tr><tr><td colspan="7">% of total revenue</td><td colspan="3">9.7%</td><td colspan="3">21.1%</td></tr></table>

Source: MS (e) estimates

Exhibit 15: We estimate AWS's Trainium/Teton racks will contribute 5% and 5.1% of TAM revenue in 2026 and 2027, respectively

<table><tr><td></td><td>2026e</td><td>2027e</td></tr><tr><td>Total ASIC shipment</td><td>1,700</td><td>2,530</td></tr><tr><td>Trainium2</td><td>-</td><td>-</td></tr><tr><td>Trainium3</td><td>1,700</td><td>2,380</td></tr><tr><td>Trainium4</td><td></td><td>150</td></tr><tr><td>BMC to ASIC per rack ratio</td><td>70.2%</td><td>69.4%</td></tr><tr><td>AST2700 ASP (US$)</td><td>25</td><td>25</td></tr><tr><td>Revenue contribution from AWS (US$mn)</td><td>29,846</td><td>43,924</td></tr><tr><td>Revenue contribution from AWS (NT$bn)</td><td>895</td><td>1,318</td></tr><tr><td>Implied CY Revenue (%)</td><td>5.0%</td><td>5.1%</td></tr></table>

Source: MS (e) estimates

Exhibit 16: AWS Trainium3 UltraServer  
![](images/483639c28c4f1da72487d8d3e50af9c291a7e9ab5fdb79b1a94403b1ab868689.jpg)  
Amazon EC2 Trn3 UltraServer  
Source: AWS.

Up to 144 Trainium3 Chips | 362 FP8 PFLOPS | 706 TB/s aggregate bandwidth

Exhibit 17: AWS Trainium3 UltraServer architecture  
![](images/8b2721b9a0b96fad2137d0364926ed4ce7e5246d2b0df3cee6b3f7708119b308.jpg)  
Source: AWS, MS.

Exhibit 18: We estimate Google TPU will contribute 4.1% and 14.4% of TAM total revenue in 2026 and 2027, respectively

<table><tr><td></td><td>2026e</td><td>2027e</td><td>2028e</td></tr><tr><td>Total ASIC shipment</td><td>1,400</td><td>7,150</td><td>6,500</td></tr><tr><td>TPUv8i (3nm, Sunfish; by Broadcom)</td><td>900</td><td>4,000</td><td>2,500</td></tr><tr><td>TPUv8t (3nm, Zebrafish; by MediaTek)</td><td>500</td><td>3,000</td><td>1,000</td></tr><tr><td>TPUv9 (2nm, Humufish; by MediaTek)</td><td>-</td><td>150</td><td>3,000</td></tr><tr><td>BMC to ASIC per rack ratio</td><td>70.0%</td><td>70.0%</td><td>70.0%</td></tr><tr><td>AST2700 ASP (US$)</td><td>25</td><td>25</td><td>25</td></tr><tr><td>Revenue contribution from Google (US$mn)</td><td>24,500</td><td>125,125</td><td>113,750</td></tr><tr><td>Revenue contribution from Google (NT$bn)</td><td>735</td><td>3,754</td><td>3,413</td></tr><tr><td>Implied CY Revenue (%)</td><td>4.1%</td><td>14.4%</td><td>9.4%</td></tr></table>

Source: MS estimates

Exhibit 19: We estimate Meta MTIA to contribute a respective 0.6% and 1.6% of TAM total revenue in 2026 and 2027, respectively

<table><tr><td></td><td>2025e</td><td>2026e</td><td>2027e</td></tr><tr><td>Total ASIC shipment</td><td>50</td><td>150</td><td>550</td></tr><tr><td>MTIA 2</td><td>50</td><td></td><td></td></tr><tr><td>MTIA 3</td><td></td><td>150</td><td>550</td></tr><tr><td>MTIA 3.5</td><td></td><td></td><td></td></tr><tr><td>BMC to ASIC per rack ratio</td><td>71.9%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>AST2600 ASP (US$)</td><td>15</td><td></td><td></td></tr><tr><td>AST2700 ASP (US$)</td><td></td><td>25</td><td>25</td></tr><tr><td>BIC to ASIC per rack ratio</td><td>78.1%</td><td></td><td></td></tr><tr><td>BIC ASP (US$)</td><td>6</td><td></td><td></td></tr><tr><td>Revenue contribution from Meta (US$mn)</td><td>234</td><td>3,750</td><td>13,750</td></tr><tr><td>Revenue contribution from Meta (NT$bn)</td><td>7</td><td>113</td><td>413</td></tr><tr><td>Implied CY Revenue (%)</td><td>0.1%</td><td>0.6%</td><td>1.6%</td></tr></table>

Source: MS estimates

## Aspeed: Estimate Revisions

We decrease our EPS estimates by 19% for 2026, 17% for 2027 and 15% for 2028: We factor in the preliminary 2Q26 revenue, and increase our respective revenue projections by 3% for 2026 to factor in a slower ramp of AST2700 in 2026, for which we now expect a slightly slower pace of ASP climb vs our previous outlook. However, we do expect steeper ramp for AST2700 into 2027, as demand for next-generation CPU remains very strong amid greater ASIC server ramp. The decline in our EPS estimates mainly stems from share dividend payout.

Exhibit 20: Aspeed: Earnings estimate revisions

<table><tr><td rowspan="2">NT$ mn</td><td colspan="2">Current Previous</td><td rowspan="2">Diff.</td><td colspan="2">Current Previous</td><td rowspan="2">Diff.</td><td colspan="2">Current Previous</td><td rowspan="2">Diff.</td></tr><tr><td>2026E</td><td>2026E</td><td>2027E</td><td>2027E</td><td>2028E</td><td>2028E</td></tr><tr><td>Net sales</td><td>17,866</td><td>18,507</td><td>-3%</td><td>26,027</td><td>25,891</td><td>1%</td><td>36,206</td><td>35,207</td><td>3%</td></tr><tr><td>COGS</td><td>5,534</td><td>5,469</td><td></td><td>7,584</td><td>7,546</td><td></td><td>10,218</td><td>9,943</td><td></td></tr><tr><td>Gross profit</td><td>12,332</td><td>

[中间内容因长度限制已省略]

ctor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$161.50</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$585.00</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$295.00</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb74.07</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$3,850.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb845.00</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$445.50</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb764.00</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb101.98</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$1,915.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb106.11</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$483.50</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$72.90</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,400.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$139.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$171.00</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$359.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$169.10</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb63.10</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb98.13</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb33.19</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb331.60</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$47.10</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb85.78</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$26.76</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb99.47</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb86.77</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb66.24</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb24.39</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb96.30</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$908.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,415.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$15,510.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$101.00</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$174.50</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb112.47</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb470.00</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$135.00</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$319.40</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb223.00</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$501.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$143.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$612.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$67.90</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$743.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb50.56</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$171.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$118.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$197.50</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb120.15</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb388.45</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,055.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$566.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$13.62</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,405.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,000.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$281.68</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$6,500.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
