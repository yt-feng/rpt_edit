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
COMMODITY ANALYST

# How China Is Buffering the Global Energy Supply Shock

We analyze Chinese energy balances since the start of the Middle East conflict and identify three reasons why a large hit to China's oil and natural gas imports—a key stabilizing force in LNG and especially oil markets during the Hormuz shock—led to only a moderate slowdown in overall economic activity (real Q2 GDP growth slowed to $3.6\%$ , quarterly annualized, down from $5.3\%$ in Q1, reflecting a negative fiscal impulse, higher energy prices, and adverse weather) with total energy demand growth remaining slightly positive at $+0.4\%$ YoY in April and May<sup>1</sup>:

First, we observe effective destocking of coal, oil, and natural gas. The YoY growth in the effective use of coal/oil/natural gas stocks—especially slower coal restocking and faster implied oil destocking than this time last year—contributed +3.0/+2.2/+0.2 percentage points to total energy demand YoY growth in April and May.

Second, fuel substitution to coal and renewables and the use of power has limited wider energy demand destruction. In April and May, China's lower use of oil/natural gas contributed -1.6/-0.1 percentage points to total energy demand YoY growth while greater use of coal/renewables contributed +1.4/+0.8pp. China's high EV penetration has allowed some switching to driving on electricity rather than gasoline: gasoline consumption was 23% lower and EV charging volume 60% higher YoY in April and May, buffering a larger fall in traffic.

Third, energy-related reductions in output have been concentrated in oil- and natural gas-intensive sectors. Sectors less able to substitute the use of oil or natural gas have had to reduce physical output, while sectors with flexible underlying energy sources have shifted to or continued using alternatives such as power.

Hongcen Wei  
+1(212)934-4691 |  
hongcen.wei@gs.com  
GS & Co. LLC

Daan Struyven
+1(212)357-4172 |
daan.struyven@gs.com
GS & Co. LLC

Samantha Dart
+1(212)357-9428 |
samantha.dart@gs.com
GS & Co. LLC

Yulia Zhestkova Grigsby
+1(646)446-3905 |
yulia.grigsby@gs.com
GS & Co. LLC

Lavinia Forcellese +44(20)7774-9243 | lavinia.forcellese@gs.com GS International

Laura Cyr +1(212)902-3435 | laura.x.cyr@gs.com GS & Co. LLC

Alexandra Paulus
+1(212)902-7111 |
alexandra.paulus@gs.com
GS & Co. LLC

Xinquan Chen  
+852-2978-2418 |  
xinquan.chen@gs.com  
GS (Asia) L.L.C.

Lisheng Wang
+852-3966-4004 |
lisheng.wang@gs.com
GS (Asia) L.L.C.

Chelsea Song
+852-2978-0106 |
chelsea.song@gs.com
GS (Asia) L.L.C.

Exhibit 1: Coal and Oil Effective Destocking and Higher Renewables Usage Helped Buffer China's Negative Fossil Fuel Import Shock

The units here are percentage point contributions to total energy demand growth.

![](images/88617dcae615c70d6aa8b01ca7cf91f4173b9f258918bfe715d24a39df251f4a.jpg)

“Oil Supply” is decomposed using changes in crude production, net imports, and inventory use, but scaled so that monthly total oil demand is aligned with monthly refined-products demand to better capture final energy consumption. “Stock Use” is the difference in average inventory drawdowns in April-May 2026 compared to April-May 2025, expressed as a percentage of average April-May 2025 total energy demand. We cite thermal coal inventory data from SX Coal. We cite SIA estimates of natural gas storage injections based on visible supply and demand. Owing to less visible oil inventories, we estimate oil inventory use as implied by NBS crude throughput and S&P products demand data, net imports data from Kpler and PetroLogistics, and production data from the IEA.

Source: IEA, Wind, SX Coal, SIA, Kpler, PetroLogistics, National Bureau of Statistics of China, Haver Analytics, S&P Global Market Intelligence, GS Global Investment Research

Exhibit 2: Traffic Congestion Remained Stable as Drivers Substituted Gasoline for Electricity  
![](images/3b5e53e3ed211175441055290da98a3bdaf6b09974498d5496f1c27353f48932.jpg)  
This references the Baidu map traffic congestion index which is calculated as the ratio of actual travel time to 'free flow' travel time, covering 98 cities.  
Source: Wind, Haver Analytics, Baidu, National Bureau of Statistics of China, National Energy Administration of China, GS Global Investment Research

## How China Is Buffering the Global Energy Supply Shock

## Major Fall in Net Imports, but Total Energy Demand Growth Still Positive

Ordinarily the largest importer of energy products shipped through the Strait of Hormuz, China has drastically reduced its net imports of fossil fuels, effectively acting as a shock absorber for global energy prices through reduced demand. Net imports of crude oil cratered in China and the rest of Asia beginning in March, but recovered in the rest of Asia to 2025 levels by June while continuing to fall in China through the first half of July (Exhibit 3).

China's net imports of oil/natural gas/coal fell 24%/7%/24% YoY in April and May reflecting YoY price jumps of 59%/49%/38% (Exhibit 4). These reductions in fossil fuel net imports were the largest source of negative total energy demand growth, representing -3.7pp/-0.3pp/-1.2pp of China's total YoY energy demand growth of +0.4% (Exhibit 5).

Exhibit 3: China Crude Oil Net Imports Continue to Fall While the Rest of Asia Recovers to 2025 Levels  
![](images/abe5c85cccc5bba180a5495812e8cd6e77237035be1a135bf715b8b40a10d016.jpg)  
Source: Kpler, GS Global Investment Research  
Charts reference visible net imports of crude oil by sea from Kpler data.  
Net Imports of Crude Oil/Condensate (Seaborne)

![](images/fc58a4714dbd410800a1ec40d3ef9d41b146f2593433bbf6fa3aefe058af6735.jpg)

Exhibit 4: China Fossil Fuel Net Imports Have Fallen Amid Higher Prices YoY% Change in April-May Average, 2026  
China Net Imports and Price YoY% by Energy Source, April-May 2026  
![](images/d355072d06c5be4b41a75930ba7516e932f245aa7cfee75cb6d57a6bc50bd932.jpg)  
“Oil” net imports cites data on net seaborne crude imports from Kpler and pipeline crude imports from Petrologistics.  
Source: Wind, SX Coal, SIA, Kpler, PetroLogistics, Platts, GS Global Investment Research

Chinese total energy consumption in April and May increased by an average of 0.4%, or 52 petajoules, year-over-year. To roughly estimate the impact of the supply shock on energy consumption, we estimate counterfactual consumption growth as the average +3.1% annual total energy demand growth rate from 2014-2023. $^{2}$ Applying this rate to China's average total monthly consumption in April and May 2025 would imply 375 PJ counterfactual YoY energy demand growth. This would suggest roughly 323 PJ of demand destruction for April and May, or 2.7pp reduction in the potential YoY growth rate. China's Q2 real GDP growth fell to 3.6% after 5.3% Q1 growth quarterly annualized, slightly exceeding our China team's nudged-down June forecast of 3.5% Q2 growth but missing market expectations. Lower GDP growth reflected mostly slower government spending, but also higher energy prices and unfavorable weather conditions.

Below, we highlight three factors that helped mitigate the total demand shock.

#1 Effective Destocking of Coal, Oil and Natural Gas Filled in for Fall in Fossil Fuel Imports and Production

Importing less of its energy needs from abroad, China has turned to its domestic inventories—rather than domestic production growth—to supplement the supply of fossil fuels.

■ Total domestic fossil fuel production actually fell slightly YoY in April and May, with lower coal production comprising a 0.5 percentage point reduction in total energy supply growth (Exhibit 5). Domestic crude oil production was unchanged compared

Exhibit 5: Effective Fossil Fuel Destocking Filled in for Lower Imports and Production The units here are percentage point contributions to total energy demand growth.

to April and May of last year, likely constrained by high extraction costs in China's aging brownfields.

The bulk of the rise in total energy consumption has been driven by the effective destocking of fossil fuels.

☐ Thermal coal inventory levels increased by 1.6%/3.7% during April/May 2026, significantly lower than the 4.7%/5.8% MoM increase of April/May 2025. Though China’s coal inventory level rose this April and May, we consider the reduction in MoM additions compared to last year’s flows—in other words, how much less China added to its coal inventory this April/May compared to April/May 2025—as effective destocking. Defined this way, coal stock use contributed 3.0 percentage points to total YoY demand growth (Exhibit 5).

We estimate that oil destocking also accelerated, contributing 2.2pp to total YoY demand growth (Exhibit 5). Moreover, changes in China's visible crude oil stocks also appear directionally consistent with our implied destocking estimates of around 1mb/d in May and June, suggesting a shift from restocking in Q2 2025 to greater inventory use this year (Exhibit 6).

☐ Effective natural gas destocking accounted for 0.2pp of total YoY energy demand growth (Exhibit 5).

![](images/cb9478126bcf5a5b963c4e4a352e13634999f238f6cf989bc0d03f38833345af.jpg)  
“Stock Use” is the difference in average inventory drawdowns in April-May 2026 compared to April-May 2025, expressed as a percentage of average April-May 2025 total energy demand. We cite thermal coal inventory data from SX Coal. We cite SIA estimates of natural gas storage injections based on visible supply and demand. Owing to less visible oil inventories, we estimate oil inventory use as implied by S&P and NBS crude throughput and products demand data, net imports data from Kpler, and production data from the IEA.

Source: IEA, Wind, SX Coal, SIA, Kpler, PetroLogistics, National Bureau of Statistics of China, Haver Analytics, S&P Global Market Intelligence, GS Global Investment Research

Exhibit 6: China's Visible Crude Inventories Grew in 2025 but have Fallen During the War  
![](images/dd1e89a5146dddb9c81d5bdc946cc64c93a56103b9e897d76a079a77e0dba289.jpg)  
Source: Kpler, GS Global Investment Research

#2 Fuel Substitution to Coal and Renewables Has Limited the Demand Destruction To avoid wider demand destruction caused by lower fossil fuel imports and production, China has increased its reliance on coal and renewables in its wider energy mix. Lower oil/natural gas use in China's overall energy demand contributed -1.6/-0.1 percentage points to its total YoY energy demand growth in April and May, while greater reliance on coal/renewables contributed +1.4/+0.8pp (Exhibit 7).

Exhibit 7: Coal and Renewables Pick Up the Slack of Lower Oil Supply The units here are percentage point contributions to total energy demand growth.  
![](images/1c253d401ae1b3424103dea1f335a4e8646c55de32d178f2026965f743f29edd.jpg)  
Source: IEA, Wind, SX Coal, SIA, Kpler, National Bureau of Statistics of China, Haver Analytics, S&P Global Market Intelligence, GS Global Investment Research

As an example of this fuel switching in practice, we observe China substituting driving with gasoline for driving with electricity. Gasoline consumption fell 23%/23%/21% YoY in April/May/June, but EV charging growth rose to 62%/60%/57% YoY. Despite much lower gasoline consumption, traffic congestion remained relatively stable, falling only 1.2% YoY in April before growing by 0.2% and 2.1% YoY in May and June (Exhibit 8). These findings are consistent with our prior reporting on China's uptick in domestic EV sales since the start of the Iran war (despite seasonally-adjusted total passenger car sales remaining flat) and may reflect substitution both in car purchases (more EVs bought) and especially in choosing which kind of energy to drive on. $^{3}$

Exhibit 8: Large Fall in Gasoline Consumption, but More EV Charging Keeps Traffic Relatively Stable  
![](images/5e8ac0cb50ba8a569f294db7f020c15c5d1552d65fd9122fc27b8c718741a6dd.jpg)  
This references the Baidu map traffic congestion index which is calculated as the ratio of actual travel time to 'free flow' travel time, covering 98 cities.  
Source: Wind, Haver Analytics, Baidu, National Bureau of Statistics of China, National Energy Administration of China, GS Global Investment Research

## #3 Energy-Related Reductions in Output Are Concentrated in Oil- and Natural Gas-Reliant Sectors

Several industries that are highly oil- or natural gas-intensive have slowed production. Physical output of processed crude oil fell by 10.9% YoY in Q2 reflecting lower crude oil inputs (Exhibit 9). $^{4}$ Sulfuric acid, produced as a byproduct during oil and natural gas refining, saw 4.6% lower Q2 physical output YoY. Chemical fibers, produced with either oil or natural gas feedstocks like ethane or naphtha as inputs, saw 3.7% lower Q2 physical output YoY.

The production of the industrial chemical ethylene increased in Q2 by $1.2\%$ YoY, rebounding from a $4.1\%$ YoY fall in April to $+2.1\%$ and $+5.5\%$ YoY growth in May and June. Though conventional ethylene production involves steam cracking of oil feedstocks like ethane or naphtha, the recent rebound in ethylene output growth may reflect China's significant acceleration in modern coal-to-chemicals pathways like Coal-to-Olefins (CTO) where coal is gasified into syngas, synthesized into methanol, and dehydrated to form ethylene. China's use of coal in chemical production rose by $11.5\%$ in April YoY amid the energy supply shock according to DBX Commodities, with coal-to-chemicals facilities residing atop domestic coal reserves well-positioned to facilitate the transition.

Furthermore, energy-intensive products more reliant on power than oil or natural gas feedstocks saw more resilient output growth. The production of caustic soda, a major industrial chemical, is highly electricity-intensive but does not require oil or natural gas as unique inputs. Physical output of caustic soda grew by 2.4% YoY in Q2. EV production, more reliant on power than on materials made with oil and natural gas, also increased 17.0% YoY.

Exhibit 9: Lower Physical Output for Oil- and Natural Gas-Reliant Sectors  
![](images/5c5a67c63f7e47dde46e09da23526aecf113addcad83c20f71b50e5cd9658921.jpg)  
Source: Wind, National Bureau of Statistics of China, GS Global Investment Research  
The commodities research team would like to thank Milan Chander for his major contributions to this project during his internship at GS Global Investment Research in summer 2026.

## Disclosure Appendix

## Reg AC

We, Hongcen Wei, Daan Struyven, Samantha Dart, Yulia Zhestkova Grigsby, Lavinia Forcellese, Laura Cyr, Alexandra Paulus, Xinquan Chen, Lisheng Wang and Chelsea Song, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Hongcen Wei GS & Co. LLC, Daan Struyven GS & Co. LLC, Samantha Dart GS & Co. LLC, Yulia Zhestkova Grigsby GS & Co. LLC, Lavinia Forcellese GS International, Laura Cyr GS & Co. LLC, Alexandra Paulus GS & Co. LLC, Xinquan Chen GS (Asia) L.L.C., Lisheng Wang GS (Asia) L.L.C., Chelsea Song GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States
The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by 

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
