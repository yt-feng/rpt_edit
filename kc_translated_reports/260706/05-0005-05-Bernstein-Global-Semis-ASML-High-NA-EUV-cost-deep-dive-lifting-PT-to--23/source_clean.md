# ASML: High-NA EUV cost deep dive - lifting PT to €2300 on rising litho intensity

HNA EUV will likely be adopted first in DRAM than for logic due to lower cost of exposure for DRAM. A common concern from investors is that HNA is too expensive (as TSMC said so) and won't be adopted anytime soon. However, what's rarely discussed is the big difference between DRAM and logic: DRAM die size is much smaller than logic, and hence only uses 1 mask, while logic mostly needs 2 masks due to larger die size (stitching). The mask changing slows down throughput by $23\%$ (135WpH vs. 175WpH), and the cost of HNA exposure for DRAM is cheaper and easier to justify. So we believe DRAM will likely adopt HNA in 2027 in 1d, when LNA EUV double patterning is needed, earlier than logic.

Logic adoption of HNA is also in sight. The high cost of HNA exposure is largely associated to the low tool availability of 80-85%, while LNA is close to 95%. However, HNA tool availability is improving faster, and is targeted to reach \~95% by 2030. WpH is also expected to increase from 135 to 175 even with 2 masks. While the litho equipment cost of HNA exposure is currently \~3x LNA for logic, the gap will narrow to \~2x by 2030. Considering other costs and complexity of double patterning, it's justifiable for logic to migrate to HNA before that. We expect Intel to be the first to adopt HNA in 2028, while TSMC will be slower, but still likely to adopt in 2030.

Rising litho intensity from 24% in 2025 to 26% in 2028. When HNA replaces LNA multiple patterning, the other cost of double patterning (etch, depo, cleaning etc) can be greatly reduced. Hence litho intensity is expected to rise with HNA, just like how litho intensity increased when LNA EUV replaced DUV (ArFi) multiple patterning. We forecast DRAM litho intensity to increase from \~20% in 1z to \~30% in 1d, due to increase in EUV layer count and adoption of HNA in 1d. While logic litho intensity stabilizes at \~32% in N2 and A14 due to limited adoption of HNA, we expect it to rise in A10. Mostly driven by DRAM, we forecast litho intensity to increase from 24% in 2025 to 26% in 2028, and ASML to gain share.

We materially increase our ASML topline forecasts following the unprecedented AI-driven expansion in both advanced logic and DRAM capacity. We raise EUV (including HNA) shipment forecasts in 2027 to 91 systems (vs. old 86) and 113 (old 87) in 2028, and expect ASML to expand EUV capacity. This is on top of strong ASP expansion supported by throughput improvements. As a result, we now expect EUV revenue to grow at a 30% CAGR, reaching €42.7bn by 2030, more than 30% above street. We also revised our DUV estimates upward, particularly toward the end of the decade, and now expect DUV revenue to reach €20bn in 2030, from €13bn in 2026.

Top Pick, lifting PT on capex cycle and litho intensity. Higher revenue and operating leverage also support stronger profitability, and our 2028 EPS of €67 is 35% above consensus. We also don't see capex peaking, and expect ASML revenue to reach €80bn by 2030 (20% CAGR) and EPS €97 by 2030 (31% CAGR). ASML now trades at trough valuation vs. peers. Given the clear acceleration in capex cycle and rising peer valuation, we raise our target P/E multiple from 35x to 40x (1SD above mean), increasing our target price to €2,300.

## BERNSTEIN TICKER TABLE


## PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
INTC, MU estimate is Adjusted EPS; INTC, MU valuation is Adjusted P/E (x); 2330.TT, TSM valuation is P/B (x);
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate ASML Outperform, PT = €2,300, TSMC Outperform, PT = USD 430, Intel Outperform, PT = USD 100, Samsung Outperform, PT = KRW 440,000, SK Hynix Outperform, PT = KR 3,300,000, Micron Outperform, PT = USD 1,300.

## DETAILS

Our ASML Model and Industry models can be downloaded here (ASML.NA / ASML Holding NV; EUV Model; DUV Model).

One of the concerns from investors for our ASML long thesis is the delay of High-NA (HNA) adoption, notably by TSMC (ASML - High-NA EUV adoption postponed?). Investors often ask why is HNA not been adopted, and if TSMC doesn't want to adopt it, does it mean the slowdown of litho vs. other processes such as etch and depo. This report analyzes the HNA cost vs. Low-NA (LNA) EUV, and conclude that HNA will likely be adopted by memory first, followed by logic, which drives increase in litho intensity. We reiterate ASML long and lift PT to €2300.

HNA EUV greatly simplifies the process and is set to replace LNA EUV as the leading edge litho tool.

\- HNA EUV has demonstrated \~8 nm resolution versus \~13 nm for LNA EUV, driven by the move from 0.33 numerical aperture to 0.55 NA optics. In lithography, resolution scales roughly with wavelength divided by numerical aperture, so keeping EUV wavelength constant at 13.5 nm while increasing NA by \~67% allows ASML to print significantly smaller features.

\- That resolution shrink translates into roughly 2.8–2.9x higher theoretical patterning density. The simple intuition is area scaling: if the printable half-pitch improves from \~13 nm to \~8 nm, the density gain is approximately 2.8x, or about 1.7x smaller features, versus 0.33 NA EUV. The key change is the larger projection-optics aperture, from NA 0.33 to NA 0.55. A higher NA collects and projects light at wider angles, which improves image sharpness and contrast at smaller pitches. ASML also highlights that HNA delivers higher imaging contrast, which improves local CD uniformity, reduces variability, and can lower required exposure dose (Exhibit 1).

\- The benefit is not only smaller lines, but simpler patterning. At very tight pitches, LNA EUV increasingly needs double or triple patterning: multiple masks, multiple litho-etch loops, and extra cut/via steps. HNA can convert some of those critical layers back to single exposure, reducing mask count, process complexity, edge-placement error accumulation, cycle time, and defect opportunities.

Cost of HNA exposure is high now but is expected to come down significantly as availability improves. We estimate with 95% availability cost for HNA exposure can drop by 23%.

\- Current low tool availability: At the current stage, HNA tools suffer from lower availability, which is a common issue for a new litho tool. While HNA is already progressing through the expected maturity curve, running at \~80% availability in 2025, this is still meaningfully below LNA which reached close to 95% availability. ASML started HNA development already in 2014, reached first good exposed wafers in the HNA lab after system integration in 2023. By Sep-2025, EXE systems had exposed more than 500k wafers, providing a much larger data set to drive reliability learning and HVM readiness.

\- Improving availability in sight: ASML disclosed that HNA availability reached above 80% for the first time in 2025, with fleet availability maturing toward a 90% target in 2026. The main source of lower availability remains long unscheduled downs, especially >12-hour events, while scheduled downtime is also partly driven by monitoring, configuration updates and platform learning. ASML's maturity curve shows EXE availability tracking favorably versus LNA/NXE at a comparable stage, targeting \~95% over the next 3-4 years (Exhibit 2), (Exhibit 3).


EXHIBIT 1: HNA EUV moves 0.55 NA optics while keeping the same 13.5 nm wavelength, improving demonstrated resolution from \~13 nm to \~8 nm. This higher optical aperture increases image contrast and allows smaller pitches to be printed with fewer patterning steps.


[[KC_IMAGE_001]]


[[KC_IMAGE_002]]

Source: Company reports, Bernstein analysis

EXHIBIT 2: Unscheduled downtime is the primary driver of EXE unavailability and reducing it is the critical path to achieving the 90% availability target.

[[KC_IMAGE_003]]

Source: Company reports, Bernstein analysis
EXHIBIT 3: EXE availability is targeted to reach 90% by 26Q4 and converge with the NXE:3600 mature fleet performance of 95% over five years


[[KC_IMAGE_004]]

EXHIBIT 4: With HNA availability reaching 95%, the equipment cost of a HNA exposure drops by 23%.
HNA Cost per Exposure (1 Mask) vs Availability
Source: Company reports, Bernstein analysis.


[[KC_IMAGE_005]]

Source: Company reports, Bernstein analysis and estimates.

However, HNA exposure cost is not the same for all. HNA EUV throughput (and hence cost) gets impacted from half field stitching, which results in slower throughput & higher cost for larger dies.

\- The main trade-off with HNA EUV is field size. Standard LNA NXE systems use a 4×/4× reduction ratio, meaning the mask image is reduced by 4× in both x and y on the wafer, preserving the conventional full EUV exposure field. HNA EXE uses an anamorphic 4×/8× optical design: 4× reduction in one direction and 8× in the other. This helps fit the much larger 0.55 NA projection optics and control mask-side angles, but it also halves the exposed field in one dimension. As a result, EXE prints a half field, roughly 16.5 mm in the reduced direction instead of the classic \~33 mm full-field height (Exhibit 5, Exhibit 6).

\- For products with many small die, such as some DRAM or smaller logic die, this is manageable: the scanner can expose twice as many half-fields using the same mask, with no need to stitch a single large die. For a single large logic die such as GPU dies, however, the chip can exceed one EXE half-field. In that case, stitching will be required. Stitching means splitting a large die across two EXE half-field exposures (Mask A and Mask B), and designing an overlap/stitch zone where the two exposures connect. The chip floorplan and routing are then made stitch-aware, so layout features crossing the boundary can be connected while controlling overlay and placement errors (Exhibit 7).

EXHIBIT 5: The H100/B100 GPU die size is already approaching the physical reticle limit of $33 \times 26 \, mm^2$ . With HNA, this limit is reduced to $16.5 \times 26 \, mm^2$ . Consequently, large logic dies require stitching.


[[KC_IMAGE_006]]

Source: ASML, Nvidia, Bernstein analysis.

EXHIBIT 6: In HNA, anamorphic optics use 4× demagnification in one axis and 8× in the other, so the 0.55-NA scanner prints only a half-field on the wafer. Larger logic dies must be split across two mask fields.


[[KC_IMAGE_007]]

Source: ASML, Bernstein analysis

EXHIBIT 7: ASML HNA EUV stitching process using AB mask overlap to reconstruct full field logic die beyond reticle limits highlighting precise overlay control across 16.5 millimeter exposure boundaries for advanced chip manufacturing.

[[KC_IMAGE_008]]


[[KC_IMAGE_009]]

Scanner enables overlap between AB on top of $16.5\mathrm{mm}$
Source: ASML, IMEC, Intel, Bernstein analysis

Our simulation shows that the cost for HNA is significantly lower for smaller dies then larger dies due to stitching, especially in the first few years.

\- For larger dies, HNA's half-field exposure requires two reticles (AB) and die stitching, which lowers effective throughput versus AA exposures where the same reticle can be reused. ASML's roadmap shows this clearly: The current EXE:5200B runs at 175 WpH in AA but 135 WpH in AB, a \~23% reduction.

\- This results in a big difference in HNA exposure cost; based on our calculation, the litho equipment cost for each HNA exposure is 2.4x of LNA with 1 mask (AA) and 3.1x of LNA with 2 masks (AB) in 2025.

\- The gap between AA and AB is narrowing. Next gen EXE:5200C improves to 190 WpH AA and 160 WpH AB, narrowing the gap to \~16%. The roadmap then points to further productivity gains, with EXE:5200D at ≥195 WpH AA / ≥175 WpH AB and EXE:5400E at ≥210 WpH AA / ≥180 WpH AB (Exhibit 8).

\- This means the litho equipment cost for HNA reduces overall, and the cost gap between larger dies and smaller dies narrows. By 2030, with the expected availability improvement, we expect the difference narrows to 1.9x for HNA AA and 2.1x for HNA AB, with still a significant gap between HNA AA and AB. (Exhibit 9)

\- This means that for smaller dies (most typical example would be DRAM), HNA litho equipment cost of exposure is lower and is easier to justify, compared to larger dies. For larger dies, HNA litho equipment is only lower than complex EUV double patterning or 3x patterning, or over time when HNA cost comes down further. However, the trend of migration to HNA doesn't change.

EXHIBIT 8: AB HNA throughput is expected to remain materially lower than AA over the next decade, driven by the requirement for dual masks and stitching.


[[KC_IMAGE_010]]

Source: Company reports, Bernstein analysis

EXHIBIT 9: Due to the lower throughput of AB HNA, the litho equipment cost per exposure is approximately 3× that of a LNA exposure, while for AA HNA the cost is only about 2.4× that of LNA. We expect these costs to decline by 2030 to around 2.1× and 1.9×, respectively.


[[KC_IMAGE_011]]

Source: Company reports, Bernstein analysis and estimates.

We conclude that it's likely for DRAM to adopt HNA earlier than logic, due to the absence of mask changing.

\- Based on the logic and DRAM roadmaps, HNA adoption becomes viable for logic at A14 (2028) and DRAM D1d (2027/28). However, as we mentioned above DRAM die size is smaller in nature and hence doesn't require stitching. Logic, especially high performance GPU/CPU dies, are of reticle size and would require two masks for HNA, which slows down the process (Exhibit 5).

\- Our simulation shows that for DRAM, HNA is almost certainly cheaper than LNA LELE double patterning. The gap widens when considering more complex SALELE with 4 exposures (2x LNA EUV and 2x ArFi), or LNA EUV LELELE (3x LNA EUV). (Exhibit 10)

\- However, for large logic die requiring stitching (AB), it is only justifiable over time to replace SALELE with either 2x EUV + 2x ArFi or 3x EUV. In fact, although the litho equipment cost ratio between HNA SE and 2 LNA decreases significantly, by around 50% from 1.6x in 2025 to 1.1x, it will still remain cheaper to use double exposure LNA rather than single exposure HNA over the next five years (Exhibit 11)

The above analysis only considered the cost of litho tool itself. There are other factors to consider. Considering the total cost, we believe HNA will be more cost competitive as availability increases, even for larger logic dies.

\- HNA also drives overall process simplification, non-litho cost cuts, yield improvements, hence should drive higher Litho Intensity. HNA enables process simplification because its higher resolution and contrast allow critical layers that would otherwise require LNA EUV multi-patterning — e.g., line/cut split flows such as SALELE — to be printed with a single HNA exposure. This reduces the number of masks, litho-etch loops, cut steps and related non-litho processing, while also improving pattern fidelity, local CDU and defectivity (Exhibit 12).

\- This simplification shifts value from non-litho processing into lithography: even if the HNA exposure itself is more expensive, the total process flow can become cheaper and more productive. As availability, throughput and ecosystem cost roadmaps improve, HNA should therefore support higher litho intensity, because customers replace complex non-litho-heavy patterning schemes with more lithography-enabled single-expose solutions, including for larger logic dies where stitching solutions are available. ASML estimates a significant increase in litho intensity when transitioning from LELE LNA to single-exposure HNA. Litho CapEx and OpEx are expected to rise by approximately 1.2×, while non-litho costs are projected to decline (Exhibit 13, Exhibit 14).

\- Considering the total cost, we believe HNA will be more cost competitive as availability increases, even for larger logic dies.

EXHIBIT 10: We estimate that, for DRAM, HNA is more cost-effective than LNA LELE double patterning. The advantage becomes more pronounced when considering more complex schemes, such as SALELE with 4 exposures (2× LNA and 2× ArFi), or LNA LELELE (3× LNA).


[[KC_IMAGE_012]]

Source: Company reports, Bernstein analysis and estimates

EXHIBIT 11: However, for logic, we estimate that HNA is economically justified only for replacing SALELE with 2× EUV + 2× ArFi or 3× EUV over time.
HNA:LNA Cost for Logic - Litho Tool Only, 1 Mask (AB)

[[KC_IMAGE_013]]

Source: Company reports, Bernstein analysis and estimates

EXHIBIT 12: HNA simplifies critical layer patterning by replacing low-NA SALELE line/cut multi-patterning with single exposure, reducing masks, litho-etch loops, process steps and non-litho cost, while materially increasing litho intensity.


[[KC_IMAGE_014]]

Source: IEEE VLSI Symposium 2026, Bernstein Analysis


[[KC_IMAGE_015]]

EXHIBIT 13: HNA EUV reduces process complexity and lithography exposures compared to SALELE, enabling more efficient patterning, lower cost and improved throughput.
Process Steps and Litho Exposure SALELE vs HNA SE


[[KC_IMAGE_016]]

EXHIBIT 14: ASML estimates a significant increase in litho intensity when transitioning from LELE LNA to single-exposure HNA. Litho CapEx and OpEx are expected to rise by approximately 1.2×, while non-litho costs are projected to decline.
Source: IEEE VLSI Symposium 2026, Bernstein Analysis
LELE LNA vs SE HNA Litho Intensity


[[KC_IMAGE_017]]

Source: ASML, Bernstein analysis


\- Our best guess of HNA adoption is: Samsung / Hynix DRAM in 2027 (D1d), Intel in 2028 (A14), Samsung logic in 2029 (SF1.4), TSMC in 2030 (A10). SK hynix has the clearest early signal: the company announced in September 2025 that it had assembled ASML's TWINSCAN EXE:5200B, the first production-oriented HNA system, at its M16 fab for next-generation DRAM development. Samsung is also moving quickly, with industry reports indicating that it ordered two ASML EXE:5200B tools, with the first expected by late 2025 and the second in H1 2026. There is no official HNA disclosure from

Micron yet, but they could adopt HNA slightly later, consistent with its more conservative EUV LNA strategy in DRAM. In logic, Intel is likely to be the first adopter, having received and assembled the industry's first commercial HNA EUV tool from ASML in 4Q2023 probably for the manufacturing of A14. Samsung logic should follow shortly after, while TSMC appears likely to delay broad HNA insertion until around 10A, after prioritizing R&D first and extending LNA for earlier nodes (Exhibit 15, Exhibit 16, Exhibit 17).

\- TSMC's announcement to adopt HNA slower than Intel and Samsung doesn't change the view that HNA is better. It probably reflects 1. TSMC's prudence and conservativeness to adopt new technologies vs. optimizing existing technologies, and 2. Economically it's better to wait for HNA to further improve in availability and throughput, which results in lower cost per exposure (but at the risk of not benefiting from HNA immediately).

Financially, slower HNA adoption is probably even better for ASML... at least in the near term.

\- As shown above, from litho tool perspective, it's economically better to sell more LNA EUV machines than fewer HNA machines. this is especially the case when considering the much higher margin for LNA over HNA EUV.

\- On the other hand, HNA adoption will further increase litho intensity and hence ASML's market share in WFE, as more value goes from non-litho steps (etch, depo, cleaning, etc) to litho when 1 HNA replaces multiple LNAArFi steps.

EXHIBIT 15: DRAM players could begin to adopt HNA at the 1d node around 2027 to 2028, when feature size F is expected to decline to around 10nm or below.


[[KC_IMAGE_018]]

Source: TEL, ASM International, Bernstein analysis

EXHIBIT 16: We estimate that logic will adopt HNA at around A14, likely in the 2028 to 2030 timeframe, when metal pitch is expected to decline to approximately 21nm.


[[KC_IMAGE_019]]

Source: Company reports, Imec, Bernstein analysis and estimates

EXHIBIT 17: DRAM HNA adoption likely starts with SK hynix and Samsung at 1d. Logic insertion should begin with Intel A14, then Samsung SF1.4, before TSMC eventually adopts HNA around 10A at the end of the decade


[[KC_IMAGE_020]]

Source: Company reports, Bernstein analysis and estimates

We expect litho intensity to increase in DRAM, and remains elevated in logic. Overall litho intensity is going up from 24% to 26%.

\- We estimate litho intensity increased from around 20% in 1Y and 1Z to 28% in 1c. This significant growth was driven by the rising number of EUV exposures, starting with 3 to 4 exposures in 1a, increasing to 4 to 6 in 1b, and then to 6 to 7 in 1c. With 1c penetration expected to increase substantially over the next few years, we expect total DRAM litho intensity to grow considerably. Additionally, with the introduction of double patterning EUV or HNA at the 1d node, we expect litho intensity to rise further to around 30% (Exhibit 18).

\- Similarly, logic litho intensity increased significantly from around 20% at 10nm, driven by a sharp rise in EUV exposures, peaking at 5nm and 3nm at above 35% intensity. While logic litho intensity declined from 3nm to 2nm due to the adoption of GAA, which requires more non litho steps, it remains elevated at around 32%. We expect it to stay at similar levels or higher with HNA at 1.4nm, and to increase further at the 1nm node (Exhibit 19).

\- Blended litho intensity for ASML is increasing and is expected to continue its upward trend, driven by the faster growth of DRAM and advanced logic relative to the overall semiconductor market. Both segments carry considerably higher litho intensity compared to mature logic and NAND, supporting a structurally higher blended litho intensity over time (Exhibit 20).

EXHIBIT 18: We anticipate an increase in lithography intensity in DRAM. The introduction of double-patterning EUV (or HNA) at the 1d node is expected to drive lithography intensity up to \~30%


[[KC_IMAGE_021]]

Source: Company reports, Bernstein analysis and estimates
EXHIBIT 19: Logic litho intensity declined from 3nm to 2nm but remains elevated at \~32%. We expect it to stay at similar levels or increase further with HNA at 1.4nm, and likely rise again at the 1nm node.
Logic Litho and EUV Intensity


[[KC_IMAGE_022]]

Source: Company reports, Bernstein analysis and estimates

EXHIBIT 20: We expect litho intensity to continue its upward trend, driven by the increasing penetration of 1c and 1d nodes in DRAM, which command higher litho intensity, as well as advanced logic, which has considerably higher litho intensity compared to mature logic.


[[KC_IMAGE_023]]

Source: Company reports, Bernstein analysis and estimates

## MODEL UPDATES

Following the unprecedented AI-driven demand, which has led to a massive expansion in capacity for AI accelerators and DRAM memory, we now expect ASML's demand for LNA EUV to be significantly higher than previously anticipated and have raised our PT accordingly.

\- To reflect the very strong positive developments in DRAM capacity expansion, highlighted by Micron announcing almost doubling of capex next year, alongside Samsung and Hynix each outlining large-scale domestic investment plans of approximately \$1.3tn, we have revised our DRAM capacity estimates using EUV. We now expect the strong growth observed over the past two years to persist, with capacity nearly tripling over the next five years.

\- Similarly, we have significantly revised upward our advanced logic estimates. Specifically regarding TSMC's capacity outlook, we expect substantial growth driven by sustained demand for AI accelerators, which shows no signs of slowing. TSMC's capacity is projected to accelerate meaningfully toward the end of the decade. The 2nm and A14 nodes are expected to experience the strongest growth.

For these reasons, we have considerably revised upward our EUV unit shipment estimates from 2027 onwards, with the largest increase occurring toward the end of the decade. We have raised our 2027 estimate to 91 units (vs. old 86), as ASML indicated that its capacity should reach the low nineties. To support the strong demand, we believe shipments in the 2028 to 2030 period will need to be significantly higher, requiring ASML to expand capacity substantially and exceed 100 units, reaching 125 units in 2030 (Exhibit 21).

Additionally, we anticipate EUV blended ASP to continue expanding over the next five years, driven by: (1) strong improvements in LNA throughput, which is expected to exceed 300 WPH by 2030 at ASML and has historically shown a strong correlation with ASP; and (2) the growing penetration of HNA toward the end of the decade, which carries roughly double the ASP. This translates into a significant increase in our EUV revenue over the next five years, with a CAGR of 30%, reaching €42.7bn by 2030. We are well above consensus throughout the forecast period and estimate revenue that is more than 30% above street by 2030 (Exhibit 22, Exhibit 23).

EXHIBIT 21: We have significantly revised our projections upward for DRAM and advanced logic capacity expansion over the 2027–30E period. As a result, expected EUV shipments have risen substantially, approaching around 125 units by 2030.

EUV Shipments New vs Old

[[KC_IMAGE_024]]

Source: Company reports, Bernstein analysis and estimates
EXHIBIT 22: We expect EUV blended ASP to continue increasing over the next five years, supported by its historically strong correlation with throughput improvements and the growing penetration of HNA toward the end of the decade


[[KC_IMAGE_025]]

EXHIBIT 23: We are well above consensus on EUV over the next five years, driven by growth in advanced logic and especially DRAM capacity. We estimate EUV revenue will grow at 30% CAGR 25-30E reaching above EUR 42bn.
EUV Revenue Estimates Bern vs Cons


[[KC_IMAGE_026]]

Source: Company reports, Bernstein analysis and estimates
Source: Company reports, Bernstein analysis and estimates.

The massive increase in semiconductor demand driven by the expansion of AI infrastructure will also fuel significant growth in DUV, which remains the industry's primary workhorse and continues to grow alongside EUV. ArF immersion systems, in particular, are still used extensively for less critical layers across DRAM, NAND, and Logic. As a result, we have revised our DUV revenue estimates upward, especially toward the end of the decade, and now expect DUV revenue to reach approximately €20bn by 2030. We continue to be materially above consensus on DUV over the next five years (Exhibit 24,

DUV Revenue (New vs Old)

Exhibit 25).

Looking at overall revenue, we expect ASML to deliver a 20% CAGR over the next five years, significantly above both consensus and the high end of management guidance, reaching €80bn by 2030. We are now 24% above street expectations in 2030, which stand at €64bn. We are also above consensus on margins, primarily driven by substantially higher revenue and the resulting operating leverage. As a result, we are 50% above consensus on EPS in 2030 (Exhibit 26).

The combination of strong revenue growth and margin expansion translates into EPS growth of 31% CAGR over the next five years, reaching almost €97 by 2030. This is significantly above street expectations, which imply EPS growth of only 21% over the same period (Exhibit 27).

This translates into our FY25-28 EPS estimate being revised upward to €56.7, an increase of 15% vs. our previous estimate of €49.2. We also raise our target P/E multiple from 35x to 40x, implying a target price of €2,300. Notably, ASML is trading below parity with the SPE median for the first time, compared with its historical valuation premium of 1.7x relative to the WFE sector. We strongly believe ASML deserves to trade at a premium to other WFE players, given its monopolistic position and the expected increase in lithography intensity over time (Exhibit 28, Exhibit 29, Exhibit 30, Exhibit 31).

EXHIBIT 24: To reflect the significant increase in semiconductor demand driven by AI, we have revised our DUV estimates upward and now expect DUV revenue to reach EUR 20bn by 2030.


[[KC_IMAGE_027]]

Source: Company reports, Bernstein analysis and estimates
EXHIBIT 25: We are significantly above consensus on DUV as well over the next 5 years.
DUV Revenue (Bern vs Cons)


[[KC_IMAGE_028]]

Source: Company reports, Bernstein analysis and estimates

EXHIBIT 26: We are considerably above consensus on system sales across both EUV and Non-EUV, as well as on Installed Base Management over the next 5 years.

ASML Revenue Bern vs Cons
There is a notable gap between the sum of the three segment consensus estimates and the total revenue estimate. Source: Bloomberg, Bernstein analysis and estimates.

EXHIBIT 27: We've revised up our estimates, now forecasting revenue of EUR 80bn by 2030, $24\%$ above consensus, driven by higher EUV and DUV. We are above consensus on margins and $50\%$ above consensus on EPS in 2030.


Source: Company reports, Bloomberg, Bernstein analysis and estimates.

EXHIBIT 28: ASML is currently trading at \~45x above its historical average of 35x. We increase our Target P/E from 35x to 40x.
Source: Bloomberg, Bernstein analysis

EXHIBIT 29: ASML avarage premium over the SPE median was on average 1.7X but is now for the first time trading below par.
Source: Bloomberg, Bernstein analysis
EXHIBIT 30: After a recent increase over the past nine months, ASML is now trading in line with its historical premium to the SOX.

Source: Bloomberg, Bernstein analysis
EXHIBIT 31: ASML premium over EDM increased considerably over the last ten years and is now trading above +2SD with the historical average.

Source: Bloomberg, Bernstein analysis

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 32: ASML Income Statement


Source: Company reports, Bernstein analysis and estimates.

EXHIBIT 33: ASML Balance Sheet


Source: Company reports, Bernstein analysis and estimates

EXHIBIT 34: ASML Cash Flow Statement


Source: Company reports, Bernstein analysis and estimates
