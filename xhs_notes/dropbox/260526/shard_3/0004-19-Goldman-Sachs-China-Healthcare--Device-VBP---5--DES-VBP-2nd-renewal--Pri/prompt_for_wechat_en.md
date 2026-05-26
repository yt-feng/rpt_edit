You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# China Healthcare: Device VBP: #5: DES VBP 2nd renewal: Pricing Continues to Trend Up; MNC Participation Rebounds

The results from the second renewal of the national DES VBP were released on May 20 (see the result here), with key takeaways on pricing and competitive landscape as follows.

Pricing saw an uptick: Pricing increased to Rmb839-949, vs. Rmb730-848 in 2022 renewal, see our previous note, reinforcing our view that VBP is increasingly a one-off price reset rather than a sustained margin headwind (see our prior note). This also suggests that NHSA's focus is shifting towards stabilizing prices, supply and overall industry economics. The pricing uptake was attributable to consistent bidding framework and clear volume-price linkage, including a higher effective price ceiling to Rmb949 (from Rmb848) and tiered allocation mechanism (90%/75%/60%). Building on the 2022 renewal—where price increases of 5–76% helped ease margin pressure—the current mechanism allows companies to better balance pricing and guaranteed volume, reducing the risk of losing full allocation and supporting more rational pricing behavior and improved market stability.

MNCs becoming more active in China VBP participation: In contrast to the domestic substitution trend following the first round, major MNC players, such as Boston Scientific, Medtronic and Abbott saw volume share rising to c.41%, from c.32% in the first renewal. This aligns with our February field-trip takeaway (see our note), where Boston Scientific highlighted China as a strategically important market, supported by ongoing innovation, broad hospital coverage, and deeper local engagement. Under the VBP framework, innovation and portfolio breadth are increasingly critical to capturing incremental volume and supporting revenue per procedure. At the same time, improved affordability under VBP may help sustain patient and physician preference for MNC brands at comparable price points.

Underlying demand remain strong post VBP: Strong volume growth is supported by rising procedure demand and broader hospital participation. Submitted demand reached c.2.73mn units, implying a 14% CAGR vs. the 2022 renewal, underpinned by continued growth in PCI procedures (2.21mn in 2025 vs. 1.29mn in 2022, per F&S). Participating hospitals increased to 4,468 from 2,408, indicating both expanded coverage and deeper PCI penetration.

Chris Pan, CFA

+852-2978-7993 | chris.pan@gs.com

GS (Asia) L.L.C.

Ziyi Chen

+852-2978-0526 | ziyi.chen@gs.com

GS (Asia) L.L.C.

David Roman

+1(212)357-4617

david.roman@gs.com

GS & Co. LLC

Exhibit 1: Price of each round of DES VBP continue to increase   
![](images/06c34c751d59f5067cd86aea2a2c227079cdbfdf03d347c0e8f8432dd45c4161.jpg)

<details>
<summary>bar</summary>

Price range of each round of DES VBP (in Rmb)
| Round | Price Range (Rmb) |
| :--- | :--- |
| 1st round, Nov-2020 | 798 |
| 1st renewal, Nov-2022 | 848 |
| 2nd renewal, May-2026 | 839 |
The values for the next two bars are not explicitly labeled in the image. The data is already in English.
</details>

Source: Tianjin Medical Purchasing Center (TJMRC)

Exhibit 2: Submitted demand reached c.2.73mn units, implying a $14\%$ CAGR vs. the 2022 renewal   
![](images/fe4679b371c1a876986ecd5659bc150d096b2a8eb7a73b3f3cbf890e2231e252.jpg)

<details>
<summary>bar</summary>

First year guaranteed volume (mn units)
| Period | First year guaranteed volume (mn units) |
|---|---|
| 1st round, Nov-2020 | 1.07 |
| 1st renewal, Nov-2022 | 1.86 |
| 2nd renewal, May-2026 | 2.73 |
2-year CAGR
3-year CAGR 14%
</details>

Source: Tianjin Medical Purchasing Center (TJMRC)

Exhibit 3: MNC submitted volume increased to c.41% in the 2nd round renewal (vs. c.32% in the first round)   
![](images/f0cf194838c2222fb05c4aae5a6cf0d2229b3587a86c6722da6f58f8cba6ae7a.jpg)

<details>
<summary>bar_stacked</summary>

Total first-year procurement demand of major brands in the 1st and 2nd round renewal (units)
| Time Period | MNC brands (units) | Domestic brands (units) | MNC brands (%) | Domestic brands (%) |
| :--- | :--- | :--- | :--- | :--- |
| 1st renewal, Nov-2022 | 1,733,291 | 68 | 32 | |
| 2nd renewal, May-2026 | 2,652,190 | 59 | 41 | |
</details>

Only the brands with $>100\mathrm{k}$ units volume is included   
Source: Tianjin Medical Purchasing Center (TJMRC)

Exhibit 4: ...notably market share gain for Abbott Sort by submitted volume for 2nd round renewal 

<table><tr><td>Company</td><td>1st round renewal (units)</td><td>2nd round renewal (units)</td><td>volume growth</td><td>1st round renewal mkt share</td><td>2nd round renewal mkt share</td><td>change of mkt share</td></tr><tr><td>MicroPort</td><td>581,806</td><td>669,141</td><td>15%</td><td>31%</td><td>25%</td><td>-7%</td></tr><tr><td>Boston Scientific</td><td>275,931</td><td>403,423</td><td>46%</td><td>15%</td><td>15%</td><td>0%</td></tr><tr><td>Abbott</td><td>20,421</td><td>358,190</td><td>1654%</td><td>1%</td><td>13%</td><td>12%</td></tr><tr><td>Jiwei Medical</td><td>278,198</td><td>345,026</td><td>24%</td><td>15%</td><td>13%</td><td>-2%</td></tr><tr><td>Medtronic</td><td>250,141</td><td>336,019</td><td>34%</td><td>13%</td><td>12%</td><td>-1%</td></tr><tr><td>Lepu</td><td>215,374</td><td>257,129</td><td>19%</td><td>12%</td><td>9%</td><td>-2%</td></tr><tr><td>Sinomed</td><td>36,579</td><td>181,609</td><td>396%</td><td>2%</td><td>7%</td><td>5%</td></tr><tr><td>Kinhely</td><td>74,841</td><td>101,653</td><td>36%</td><td>4%</td><td>4%</td><td>0%</td></tr></table>

Source: Tianjin Medical Purchasing Center (TJMRC)

Exhibit 5: Tiered volume allocation ratios for coronary drug-eluting stents 

<table><tr><td>Product category</td><td>Winning price range (Rmb/unit)</td><td>Base committed-volume ratio</td></tr><tr><td rowspan="3">Coronary drug-eluting alloy stents</td><td>Winning price ≤ 848</td><td>90%</td></tr><tr><td>848 &lt; Winning price ≤ 898</td><td>75%</td></tr><tr><td>898 &lt; Winning price ≤ 949</td><td>60%</td></tr><tr><td rowspan="3">Coronary drug-eluting stainless-steel stents</td><td>Winning price ≤ 757</td><td>90%</td></tr><tr><td>757 &lt; Winning price ≤ 802</td><td>75%</td></tr><tr><td>802 &lt; Winning price ≤ 848</td><td>60%</td></tr></table>

Source: Tianjin Medical Purchasing Center (TJMRC)

# VBP tracker

# Exhibit 6: VBP for consumables likely to see full coverage by YE26, likely extending to capital equipment

As of May 21, 2026

![](images/697f579c87ff8ba3935b9591f0abc814b0eb4970d5195c1d2ef681e852cf0ad0.jpg)  
Numbers refer to # of provinces that announced/implemented VBP; N denotes the number of provinces to be announced.

Source: National/Regional Healthcare Security Administration

Exhibit 7: Accelerating progress in VBP since Oct 25; expecting additional announcements towards year end 2026 

<table><tr><td>Date of announcement</td><td>Product categories</td><td>Covered regions</td><td>Domestic companies</td><td>MNCs</td></tr><tr><td>Mar-26</td><td>Incision Protector</td><td>Shangdong-led regional VBP, 4 provinces</td><td>Kangji Medical, Weigao, Bluesail Surgical, etc.</td><td>Applied Medical, Medtronic, J&amp;J, etc.</td></tr><tr><td>Mar-26</td><td>Bronchoscopy internversion: Tracheal &amp; Bronchial stent, Airway balloon dilation catheter, Electronic bronchoscope/ imaging catheter, etc.</td><td>Hunan-led regional VBP</td><td>Microtech, Aohua Endoscopy, SonoScape, etc.</td><td>Boston Scientific, Olympus, Medtronic, Cook, etc.</td></tr><tr><td>Mar-26</td><td>Coronary balloon</td><td>Henan-led regional VBP, 16 provinces/ regions</td><td>Lepu, MicroPort Rhythm, Sinomed, Brosmed, DK Medtech, etc.</td><td>Boston Scientific; Nipro</td></tr><tr><td>Mar-26</td><td>Snare devices, Peripheral vascular constraint-type balloon dilation catheter, Powered irrigation device (orthopedic and trauma surgery)</td><td>Hebei-led regional VBP</td><td>Zylox-Tonbridge, Acotec, Lepu, BrosMed, Shunmei, Double Medical, etc</td><td>Medtronic, Boston Scientific, Cook, Becton Dickinson, Stryker, etc.</td></tr><tr><td>Feb-26</td><td>Neurointerventional microcatheter, Peripheral interventional microcatheter, Pacemaker consumables</td><td>Zhejiang-led regional VBP, 27/29 provinces/ regions</td><td>MicroPort NeuroTech, HeartCare, Zylox-Tonbridge, Peijia Medical, Shunmei, Lepu, MicroPort CRM, etc.</td><td>Medtronic, Abbott, Boston Scientific, Stryker, Terumo, Biotronik, etc.</td></tr><tr><td>Dec-25</td><td>PFA catheter</td><td>Beijing</td><td>APT Medical, Dinova, Jinjiang, MicroPort Everpace, Shineyo Medical, etc.</td><td>Boston Scientific, Medtronic, J&amp;J</td></tr><tr><td>Dec-25</td><td>Vena cava filter, ablation electrode</td><td>Heilongjiang-led regional VBP, 23 provinces/ regions</td><td>LifeTech, Hope Med, APT Med, etc.</td><td>Cook, Becton Dickinson, B. Braun, etc.</td></tr><tr><td>Dec-25</td><td>Dural patch (for hard meninges), incl. chemically synthesized and animal-derived materials</td><td>Tianjin-led 3+N alliance, GSe 20+ provinces/ regions</td><td>Guanhao Bio, Medprin etc.</td><td>B. Braun, Cook. J&amp;J, etc.</td></tr><tr><td>Dec-25</td><td>Indwelling needles</td><td>Tianjin-led 3+N alliance, GSe 20+ provinces/ regions</td><td>Weigao, Kindly Medical etc.</td><td>Becton Dickinson, Terumo etc.</td></tr><tr><td>Nov-25</td><td>Ureteral stent</td><td>Chongqing-led regional VBP, 26 provinces/ regions</td><td>Ruibang Medical, Lakh Medical, Weili Medical, Microport</td><td>Boston Scientific, Cook, Becton Dickinson, B. Braun</td></tr><tr><td>Nov-25</td><td>Heart occluder device</td><td>Fujian-led VBP, covering all provinces/ regions</td><td>Lepu ScienTech, LifeTech, Balance Medical, Kewei Medical, etc.</td><td>Abbott, Boston Scientific, etc.</td></tr><tr><td>Nov-25</td><td>High-frequency electrosurgical unit and neutral electrode</td><td>Hunan-led regional VBP, 29 provinces/ regions</td><td>Mindray, Beijing Kangwei, Shandong Huabo, etc.</td><td>Covidien, Erbe, Conmed, etc.</td></tr><tr><td>Nov-25</td><td>TCM acupuncture needles</td><td>Guangxi-led regional VBP, 25 provinces/ regions</td><td>Yuwell, Jiajian Medical, Yunlong Medical</td><td>-</td></tr><tr><td>Nov-25</td><td>TCM decoction pieces, covering 41 categories</td><td>Joint VBP covering all provinces/ regions</td><td>Gushengtang, Kangmei Pharma, Tongrentang, Liliangji, China TCM, etc.</td><td>-</td></tr><tr><td>Oct-25</td><td>Heart valve, incl. biological valve, mechanical valve, transcatheter valve</td><td>Gansu-led regional VBP, over 20 provinces/ regions</td><td>Venus, Peijia, Microport Cardioflow, Lepu, Balance Medical, Genesis, etc.</td><td>Medtronic, Abbott, Edward, etc.</td></tr><tr><td>Oct-25</td><td>Medical film, incl. laser film and thermal film</td><td>Tianjin-led 3+N alliance, GSe 20+ provinces/ regions</td><td>Luckyfilm, Clear etc.</td><td>Carestream, Fujifilm, etc.</td></tr><tr><td>Oct-25</td><td>Hemostatic materials, incl. in-body use, surface use, and ENT</td><td>Tianjin-led 3+N alliance, GSe 20+ provinces/ regions</td><td>Medprin, Borayer etc..</td><td>Becton Dickinson, B. Braun, Baxter, J&amp;J, etc.</td></tr><tr><td>Oct-25</td><td>Coronary drug-coated balloon</td><td>6th batch national VBP for medical consumables</td><td>Microport, Acotec, Lepu, Grand Pharma, etc.</td><td>Biotronik, Medtronic, Boston Scientific, etc.</td></tr><tr><td>Oct-25</td><td>Peripheral vascular drug-coated balloon, for arteriovenous fistula dialysis access, above-the-knee sites, and below-the-knee sites</td><td>6th batch national VBP for medical consumables</td><td>Acotec, Lepu, Zylox, etc.</td><td>Medtronic, Biotronik, TriReme Medical, etc.</td></tr><tr><td>Oct-25</td><td>Urological interventional consumables, incl. guidewire, sheath, balloon dilation catheter, stone retrieval basket, single-use flexible ureteroscope sheath/catheter, percutaneous nephrostomy kit</td><td>6th batch national VBP for medical consumables</td><td>Weigao, Microport, Innovex, Ruibang Medical, etc.</td><td>Boston Scientific, Becton Dickinson, Medtronic, Cook Medical, etc.</td></tr></table>

Source: Regional healthcare security administration

# Top level

China Healthcare: Device VBP : #4: Full Consumables Coverage on Track, Capital Equipment Broadening in 2026   
China Healthcare: Device VBP #3: Accelerating VBP implementations in 4Q after a slower start YTD   
China Healthcare: Medical Devices: Accelerating VBP expansion; focus on targets for next round, with direction likely to remain consistent (Mar 11, 2025)   
Investor feedback on VBP policy: increasing visibility at national level; monitoring regional pilots (Nov 9, 2022)   
China Healthcare Mapping the regulatory paths in China healthcare; eyeing opportunities in divergence (Aug 8, 2021)

# Capital equipment

China Healthcare: Aug 2025 China hospital equipment bidding: Better-than-expected MoM growth, with both MNC/domestic to thrive (Sep 10, 2025)   
China Healthcare: Addressing VBP risks for medical equipment; three debates after NHSA guidelines (Nov 25, 2024)   
China Healthcare: Anhui VBP on large medical equipment, market share/ASP changes since 2019 (Feb 22, 2024)

# DES renewal

China Healthcare: Medical Devices: Price increase in DES VBP renewal; positive signs for long-term post-VBP pricing (Nov 30, 2022)

# Artificial joints

China Healthcare: Medical Devices: VBP update: National joints renewal results as expected; FY24 notice focuses on regional alliance (May 21, 2024)   
AK Medical (1789.HK): Joint VBP renewal rules released, largely inline with our expectation; final bidding on May 21st (May 1, 2024)   
AK Medical (1789.HK): Call takeaway: Encouraging volume uptake for hip/knee post VBP; Raised guidance for revenue/NP; Buy (Aug 21, 2022)   
AK Medical (1789.HK): VBP uncertainty cleared, eyeing long term growth after 2022; Buy (Sep 15, 2021)   
AK Medical Holdings (1789.HK): Updated VBP rules - Better than expected ceiling prices; continue to favor leading brands; Buy (Aug 24, 2021)   
AK Medical Holdings (1789.HK): Final joints VBP rules released; Favors leader brands; Buy (Jun 22, 2021)

# IVD

China Healthcare: Medical Devices: 2024 IVD VBP in-line; leading domestic players to see continued share gain; Buy Mindray, SNIBE (Jan 2, 2025)   
China Healthcare: Diagnostics and Clinical Labs: IVD regional VBP final result of avg 51% cut in line with prior market expectations (Jan 2, 2024)   
China Healthcare: Diagnostics and Clinical Labs: Biochemistry reagent volume-based procurement draft (Oct 14, 2022)

# Spine VBP

China Healthcare: Medical Devices: Encouraging final results for Spine VBP released; potentially sets positive tone for future rounds (Sep 28, 2022)   
China Healthcare: Medical Devices: Mixed signs from Spine VBP's latest bidding rule; eyes on final result on Sep 27th (Sep 13, 2022)   
China Healthcare: Expert call: Orthopedics industry back to healthy recovery; accelerating import substitution post VBP implementation (Aug 15, 2022)   
Shandong Weigao Group (1066.HK): Spine VBP results could be mild; focusing on volume uptake (June 29, 2022)

# Trauma

China Healthcare: Price increase in regional trauma VBP renewal; reaffirming long-term post-VBP pricing stability (Sep 27, 2023)

# Ophthalmology

China Healthcare: Medical Devices: China IOL VBP bid price released, in-line price cut for monofocal and bifocal but significant cut for trifocal (Nov 30, 2023)   
Aier Eye Hospital (300015.SZ): Planned OK lens VBP in Hebei province and scenario analysis (Oct 27, 2022)

# Dental

Americas Dental: China's implant VBP results released: NVST & XRAY receive majority of submitted volume, pricing in-line (Jan 12, 2023)   
Angelalign Technology (6699.HK): Manageable price cut in 15-province VBP on clear aligners; minimal volume impact in near-term (Dec 20, 2022)   
First take on dental implant pricing guidelines: Better-than-market-feared amid ongoing step-up in regulatory oversight; Neutral (Sep 12, 2022)   
China Healthcare: Medical Devices: Draft guideline released for regional orthodontics VBP; awaiting submitted volume/final bidding in Nov/Dec (Oct 24, 2022)

# Disclosure Appendix

# Reg AC

We, Chris Pan, CFA, Ziyi Chen and David Roman, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Chris Pan, CFA GS (Asia) L.L.C., Ziyi Chen GS (Asia) L.L.C., David Roman GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

# GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis fo

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
