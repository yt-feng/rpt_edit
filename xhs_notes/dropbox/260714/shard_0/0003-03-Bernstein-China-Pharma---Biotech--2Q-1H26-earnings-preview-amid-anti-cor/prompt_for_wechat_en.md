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
China Pharma and Biotech

# China Pharma & Biotech: 2Q/1H26 earnings preview - amid anti-corruption and VBP, innovative leaders separate from the pack

![](images/a067273c3c7154ed547bb26967b9481943ef137ea5b155e276280f7c804dee73.jpg)  
Rebecca Liang, Ph.D.  
+852 2123 2656  
rebecca.liang@bernsteinsg.com

![](images/b5f46cfb2d87eb496cc9699841a509b36cf498ea6bc1897faa3efefb0c9729d3.jpg)

Ellie Li

+852 2123 2621

ellie.li@bernsteinsg.com

China's healthcare anti-corruption campaign intensified in 2Q26, but the impact has so far been more targeted and compliance-focused than the broad freeze seen in 2023. Company feedback points to uneven effects across the sector: Hengrui highlighted temporary disruptions to academic promotion and hospital formulary listing processes, particularly in lower-tier cities, while Innovent indicated limited impact. We expect near-term friction in physician engagement and promotional activities to modestly slow prescription growth, particularly for crowded therapeutic categories and me-too products. However, longer term, the campaign should favor companies with clinically differentiated products as prescribing decisions become increasingly driven by efficacy, safety and real-world outcomes rather than promotional intensity.

VBP Batch 12 was announced in late June covering 65 molecules across several large off-patent therapeutic categories. Within our coverage, Hengrui and Hansoh are the most exposed names, although the earnings implications appear manageable at the company level. For Hengrui, Sevoflurane alone contributes c.7% of sales and could see cumulative revenue erosion of CNY0.5–1.3 Bn over the next 2-3 years, while Hansoh has exposure through two mature products. Nevertheless, both companies now derive the majority of growth from innovative products, limiting the company-level significance of VBP despite potentially meaningful product-level pressure.

Drug sales update: Online GLP-1 sales continued to expand strongly despite tightening oversight of obesity-drug prescriptions, with combined sales of tirzepatide, mazdutide and semaglutide approaching CNY3 Bn in 1H26. TZP remained the category leader, and MAZ was the key share gainer, having surpassed SEMA. In hospital channels, the fastest-growing segments remain next-generation oncology modalities, led by PD-(L)1 bispecific antibodies (+238% YoY) and TROP2 ADCs (+149% YoY). Kelun's sac-TMT continues taking share in the domestic TROP2 market, while the rapid emergence of ivonescimab highlights continued momentum in BsAbs.

Heading into 2Q/1H26 results, we expect Kelun-Biotech and Innovent to remain the strongest performers in our coverage. Kelun continues to benefit from robust sac-TMT uptake in the fast-growing TROP2 ADC segment, while Innovent is supported by both mazdutide's strong commercial ramp and continued share gains from tafolecimab.

Pharma names face a more challenging backdrop, balancing anti-corruption, VBP pressure and increasing competition across several innovative drug classes including CDK4/6 and IL-17. For Hengrui, we lower generic-drug assumptions to a roughly 10% annual decline through 2028E and modestly reduce innovative-drug expectations. We also adopt a longer recognition period for licensing upfronts and milestones, reducing long-term BD income forecasts despite incorporating the recent BMS transaction. These changes lower our 12-month target price to CNY65 from CNY71. For Hansoh, operating assumptions are largely unchanged, but we similarly delay recognition of upfront payments and milestones, resulting in modestly lower long-term licensing income forecasts and a slightly reduced TP (HK\$44 from HK\$47).

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">13 Jul 2026</td><td colspan="2">TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td></td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>9926.HK (Akeso)</td><td>M</td><td>HKD</td><td>95.25</td><td>130.00</td><td>(51.1)%</td><td>CNY</td><td>(0.60)</td><td>(0.52)</td><td>0.70</td><td>(136.2)</td><td>(159.5)</td><td>117.8</td><td></td></tr><tr><td>ONC (BeOne)</td><td>O</td><td>USD</td><td>298.70</td><td>412.00</td><td>(1.3)%</td><td>USD</td><td>2.63</td><td>5.65</td><td>8.93</td><td>113.5</td><td>52.8</td><td>33.4</td><td></td></tr><tr><td>1093.HK (CSPC)</td><td>M</td><td>HKD</td><td>8.16</td><td>10.70</td><td>(32.5)%</td><td>HKD</td><td>0.37</td><td>0.52</td><td>0.56</td><td>19.1</td><td>13.7</td><td>12.6</td><td></td></tr><tr><td>3692.HK (Hansoh)</td><td>O</td><td>HKD</td><td>32.52</td><td>44.00</td><td>(32.0)%</td><td>CNY</td><td>0.93</td><td>0.97</td><td>0.88</td><td>30.2</td><td>29.0</td><td>32.0</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>47.00</td><td></td><td></td><td></td><td>1.01</td><td>1.10</td><td></td><td></td><td></td><td></td></tr><tr><td>1801.HK (Innovent)</td><td>O</td><td>HKD</td><td>89.10</td><td>120.00</td><td>(24.7)%</td><td>HKD</td><td>0.48</td><td>0.71</td><td>2.90</td><td>183.7</td><td>125.5</td><td>30.7</td><td></td></tr><tr><td>600276.CH (Hengrui)</td><td>O</td><td>CNY</td><td>55.75</td><td>65.00</td><td>(37.3)%</td><td>CNY</td><td>1.18</td><td>1.42</td><td>1.78</td><td>47.2</td><td>39.4</td><td>31.3</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>71.00</td><td></td><td></td><td></td><td>1.54</td><td>1.92</td><td></td><td></td><td></td><td></td></tr><tr><td>6990.HK (Kelun-Biotech)</td><td>O</td><td>HKD</td><td>504.00</td><td>526.00</td><td>13.0%</td><td>CNY</td><td>(1.66)</td><td>(2.75)</td><td>0.85</td><td>43.4</td><td>44.1</td><td>27.2</td><td></td></tr><tr><td>1177.HK (Sino BioPh)</td><td>M</td><td>HKD</td><td>5.16</td><td>7.90</td><td>(48.3)%</td><td>CNY</td><td>0.19</td><td>0.20</td><td>0.22</td><td>23.3</td><td>21.9</td><td>20.1</td><td></td></tr><tr><td>9688.HK (Zai Lab)</td><td>M</td><td>HKD</td><td>15.89</td><td>15.00</td><td>(74.6)%</td><td>USD</td><td>(0.16)</td><td>(0.15)</td><td>(0.09)</td><td>0.5</td><td>0.5</td><td>0.4</td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,947.59</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,575.39</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended 6990.HK, 9688.HK valuation is EV/Sales (x); 9926.HK, 1093.HK, 1177.HK base year is 2024; Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Hansoh, Jiangsu Hengrui, Kelun-Biotech, BeOne Medicines, and Innovent Outperform; and Akeso, Zai Lab, Sino Biopharm, and CSPC Market-Perform.

## DETAILS

## POLICY UPDATES

## Anti-corruption efforts intensified since 2Q26

Renewed enforcement, but more targeted than the 2023 campaign. China authorities have intensified healthcare anti-corruption efforts in 2Q26, with the National Health Commission (NHC) and 13 government departments launching a nationwide campaign targeting misconduct in pharmaceutical promotion, healthcare services and procurement activities (source). Recent measures have also placed greater scrutiny on marketing activities conducted under the guise of academic meetings, research collaborations and patient programs, alongside tighter oversight of medical insurance fund usage and procurement compliance. Compared with the broad-based disruption seen during the 2023 anti-corruption campaign, the current round appears more compliance-focused and targeting specific behaviors and payment practices rather than causing a widespread suspension of hospital activities.

Company feedback suggests limited and uneven commercial impact so far. Management commentary across our coverage indicates a varying range of potential impact. Hengrui has highlighted disruptions to academic promotional activities and hospital formulary listing processes, particularly in lower-tier cities where hospital decision-making has become more cautious; however, management views these disruptions as temporary rather than structural. In contrast, Innovent has indicated limited impact, reflecting the resilience differentiated products particularly in chronic diseases. Overall, current feedback points to localized execution headwinds rather than the broad commercial freeze experienced in 2023.

Our view: near-term friction, but long-term supportive for innovation. We expect anti-corruption measures to create temporary friction in physician engagement, promotion and hospital access activities, leading to a modest near-term slowdown in prescription growth across parts of the industry. There is likely more impact for crowded therapeutic classes and metoo products that rely heavily on promotional intensity, while differentiated innovative therapies should remain relatively resilient. Over the longer term, we view anti-corruption as supportive for industry quality, as prescribing decisions should increasingly be driven by clinical efficacy, safety profiles and real-world outcomes rather than commercial promotion. In this environment, companies with truly innovative pipelines and clear product differentiation should be the principal beneficiaries.

## VBP batch 12: Hengrui and Hansoh implicated moderately

The National Organization for Drug Joint Procurement formally launched the 12th national VBP on 23 June 2026, with the final procurement list covering 65 drug varieties after an earlier information pre-fill process (source). The basket is concentrated in large off-patent therapeutic categories, including cardiovascular, oncology and metabolic products, and represents one of the larger VBP rounds by market value in recent years. Companies are currently preparing tender submissions, with bidding and award announcements expected over the coming months, followed by gradual provincial implementation.

## Hengrui likely the most exposed name in our coverage, although the earnings impact should be manageable.

Sevoflurane remains one of Hengrui's larger legacy generic products and has already experienced revenue pressure during 2025 following provincial procurement initiatives. Based on our assumptions for price reduction and tender allocation, we estimate cumulative sales erosion of roughly CNY0.5–1.3 Bn over the next two to three years (Exhibit 1). While meaningful at the product level, this represents a relatively limited headwind compared with Hengrui's CNY30 Bn-plus revenue base and should be increasingly offset by growth from innovative products. Hansoh also has exposure through two products included in the procurement basket. We expect pressure on the affected mature products, although the overall portfolio impact should be limited given the company's growing contribution from innovative medicines close to 80%.

Overall we view Batch 12 primarily as a product-level modeling adjustment rather than a material change to Hengrui or Hansoh's broader earnings trajectory.

EXHIBIT 1: VBP Batch 12 exposure is concentrated in Hengrui and Hansoh

<table><tr><td>Company</td><td>TTM company sales as of 1Q26 (CNY Mn)</td><td>Drug name</td><td>TTM drug sales as of 1Q26 (CNY Mn)</td><td>Sales contribution</td></tr><tr><td rowspan="6">Hengrui</td><td rowspan="6">24,931</td><td>Sevoflurane</td><td>1,645</td><td>7%</td></tr><tr><td>Mycophenolate sodium</td><td>152</td><td>1%</td></tr><tr><td>Tolvaptan</td><td>88</td><td>0%</td></tr><tr><td>Leucovorin calcium</td><td>59</td><td>0%</td></tr><tr><td>Tacrolimus</td><td>50</td><td>0%</td></tr><tr><td>Compound amino acid</td><td>3</td><td>0%</td></tr><tr><td rowspan="3">Hansoh</td><td rowspan="3">8,832</td><td>Enzalutamide</td><td>369</td><td>4%</td></tr><tr><td>Paliperidone</td><td>314</td><td>4%</td></tr><tr><td>Deferasirox</td><td>1</td><td>0%</td></tr><tr><td rowspan="8">CSPC</td><td rowspan="8">17,203</td><td>Ertapenem sodium</td><td>257</td><td>1%</td></tr><tr><td>Pentoxifylline</td><td>202</td><td>1%</td></tr><tr><td>Paliperidone</td><td>83</td><td>0%</td></tr><tr><td>Tramadol hydrochloride</td><td>25</td><td>0%</td></tr><tr><td>Estazolam</td><td>22</td><td>0%</td></tr><tr><td>Vitamin B6</td><td>8</td><td>0%</td></tr><tr><td>Sacubitril/Valsartan sodium</td><td>3</td><td>0%</td></tr><tr><td>Mesalazine</td><td>0</td><td>0%</td></tr><tr><td rowspan="7">SBP</td><td rowspan="7">21,938</td><td>Tolvaptan</td><td>302</td><td>1%</td></tr><tr><td>Sitagliptin phosphate/metformin hydrochloride</td><td>195</td><td>1%</td></tr><tr><td>Iguratimod</td><td>69</td><td>0%</td></tr><tr><td>Compound amino acids injection</td><td>43</td><td>0%</td></tr><tr><td>Ceftazidime/Avibactam</td><td>37</td><td>0%</td></tr><tr><td>Iopromide</td><td>10</td><td>0%</td></tr><tr><td>Saxagliptin hydrochloride/metformin hydrochloride</td><td>0</td><td>0%</td></tr></table>

Source: SMPAA, Pharmcube, Bernstein analysis

## 1H26 DRUG SALES UPDATE

## GLP-1: TZP the category leader; MAZ on track to reach CNY2 Bn in 2026

GLP-1 retail demand remained robust in 1H26 despite regulatory noise around online obesity-drug sales. Online sales of the three leading GLP-1 products—tirzepatide (TZP), mazdutide (MAZ) and semaglutide (SEMA)—continued to grow strongly through 1H26, with combined online retail sales approaching CNY3 Bn based on channel tracking (Exhibit 2, Exhibit 3). In May, media reports indicated tighter controls on online sales of obesity medicines, including stricter prescription verification requirements and restrictions on internet-hospital prescriptions in certain regions. However, GLP-1 products largely remained accessible because they are also approved for type 2 diabetes (source). While all three products experienced modest sequential moderation in June, we think it is too early to conclude that the regulatory tightening has materially altered underlying demand trends.

Tirzepatide remained the category leader, and mazdutide was the key share gainer in 1H26. Based on our channel data, TZP generated approximately CNY1.8 Bn of retail sales during 1H26, representing about 60% share of the tracked GLP-1 market. Nevertheless, Innovent's MAZ continued to gain share against SEMA and surpassed it in monthly sales from March onward. At the current trajectory, we estimate MAZ online sales could reach approximately CNY1.3–1.5 Bn in 2026. Assuming online sales account for roughly 60–70% of total retail sales, we believe total MAZ sales remain on track to achieve the company's \~2Bn target for 2026.

Pricing competition has eased since early 2026. Following the significant price reset for TZP in January, average selling prices have largely stabilized through 2Q26 even as volumes continued to expand. MAZ prices have gradually moved lower over recent months and are now much closer to TZP levels. We expect pricing across the leading GLP-1 products to be broadly stable in 2H26, while the next major catalyst for MAZ will be the 2026 NRDL negotiations in November–December, which could meaningfully expand patient access in hospital channels and support another leg of volume growth in 2027.

EXHIBIT 2: Tirzepatide online sales grew the most in recent months; mazdutide had surpassed semaglutide sales since March

China leading GLP-1 sales from major e-commerce platforms: Sales by product (LHS) vs ASP (RHS)

![](images/d19e6ebf43f52549488b015cf495774b34b1ca29f21f5d844b1f7499d605b828.jpg)  
Semaglutide: include ozempic and wegovy  
Source: Moojing Intelligence (Taobao + Tmall + JD), Bernstein analysis  
EXHIBIT 3: Mazdutide recorded over CNY 600 Mn online sales in 1H26, getting 22% of share as 2nd place among Top 3 GLP1s  
26H1 GLP-1 online sales by product

![](images/eddcf33b1c25c1af84a7b9fb9af99e9d4d25b6b1738a2374f3aed8a735485642.jpg)  
Semaglutide: include ozempic and wegovy
Source: Moojing Intelligence (Taobao + Tmall + JD), Bernstein analysis

## 1Q26 sample hospital sales

Kelun's sac-TMT has been major beneficiary of the fast-growing TROP2 ADC market (Exhibit 7), which expanded 149% YoY in 1Q26. The product continued taking share from Trodelvy and strengthened its leadership position in the domestic TROP2 ADC segment. Among our coverage names, Kelun has the most clean-cut gain of commercial momentum as a single-asset company (aside from a few much smaller products).

Innovent remained steady, with Tafolecimab continuing share gain in the rapidly expanding PCSK9 market (Exhibit 15), where sales grew 75% YoY; meanwhile sintilimab has lost share to smaller PD-1 players but remained a solid second after tislelizumab (Exhibit 9). Combined with strong mazdutide momentum outside hospital channels, Innovent continues to demonstrate broad-based growth across multiple innovative franchises.

BeOne Medicines: BRUKINSA continued to demonstrate strong commercial momentum in the U.S. BTKi market, with sales steadily increasing and market share rising from 30% in 4Q25 to 36% in 2Q26 (Exhibit 6). The product consistently gained share at the expense of IMBRUVICA, becoming a key growth driver within the expanding BTKi class.

Hengrui: mixed trends in recently launched drugs. Rezvilutamide continued gaining share in the androgen receptor (AR) market, which accelerated to +23% YoY (Exhibit 11), while dalpiciclib lost share in the +36% YoY CDK4/6 market (Exhibit 12). Vunakizumab, new to the IL-17/23 market, was yet to get meaningful share (Exhibit 14).

Hansoh's key product aumolertinib continued to benefit from expansion of the 3rd-generation EGFR-TKI market, although category growth slowed to +18% YoY and osimertinib regained share to roughly 49% (Exhibit 13). The company remains exposed to a healthy oncology market backdrop, but momentum appears more stable than accelerating compared with prior quarters. Overall, 1Q26 suggests steady growth rather than a material inflection in hospital sales performance.

(Note: in late May 2026, Pharmcube expanded its sample hospital universe from 1,600 to 3,000 institutions. This restructuring enhances coverage by capturing a broader volume of Class II and lower-tier county hospitals in China, and thus leads to a ballooning of historical absolute sales data.)

EXHIBIT 4: Overall drug sales declined 4% YoY in 1Q26, reflecting continued weakness in generics, biosimilars, and TCMs despite resilient innovative sales

<table><tr><td>Drug category</td><td>LTM sales (in CNY Bn)</td><td>LTM sales YoY %</td><td>1Q26 sales (in CNY Bn)</td><td>1Q26 sales YoY %</td><td>Q1 2-year averag

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
