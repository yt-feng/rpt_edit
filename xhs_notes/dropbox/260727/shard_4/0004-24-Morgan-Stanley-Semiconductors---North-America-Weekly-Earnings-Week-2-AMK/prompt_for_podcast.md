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
# Weekly: Earnings Week 2 (AMKR, NVTS, NXPI, SWKS, QCOM, ALGM, ON); Thoughts on MRVL/Frozen, MCHP/Hailo

Stocks continue to see some downward pressure - but the numbers have been good and for the most part we see that continuing this week. We also touch on Google "Frozen" and Microchip's acquisition of Hailo.

Google Frozen could be a Marvell opportunity. Google (covered by Brian Nowak) is reportedly exploring “Frozen v2,” a new chip designed specifically to run Gemini models more efficiently. Unlike a general-purpose TPU, Frozen v2 could hardwire elements of Gemini’s architecture directly into the silicon, improving inference speed and power efficiency. Our checks suggest the chip will use on-chip SRAM, eliminating the need for CoWoS packaging, with limited production beginning in 2027 and a broader ramp in 2028. Per industry checks, we believe Marvell is a likely development partner, although the supplier has not been confirmed. More broadly, Frozen v2 reinforces the emerging trend toward SRAM-based solutions optimized for inference workloads. While volumes are expected to be modest initially, the program could still support Marvell’s custom silicon outlook, particularly given management’s guidance for more than 100% growth in 2027.

Microchip announced a definitive agreement to acquire Hailo on Friday while COO Richard Simoncic has resigned to become CEO of Menlo Microsystems (private). Hailo is a provider of accelerated edge AI processors, advanced vision processing solutions, and robotics processors - with financial terms undisclosed, the deal expected to remain immaterial, and closing targeted by end of September 2026. The deal fits a broader trend of semis positioning at the Physical AI/edge intersection, validated by ON's acquisition of Synaptics, and is consistent with Microchip's long history of acquisitions - having executed roughly 17 deals between 2009 and 2018 alone, including Atmel, Microsemi, and PMC-Sierra. While the strategic rationale is clear, with so many acquisitions over the years it can be difficult to track where value is being created - not necessarily a negative, but a complexity worth acknowledging given the core business remains deeply embedded in product markets where AI-driven revenue uplift is slow to materialize.

AMKR (EW, reporting after the market close on Monday, July 27th): Looking for additional details on the NVIDIA and TSMC deals and the pace of GM% expansion. With the stock up 50% YTD and advanced packaging continuing to see momentum, the focus around the Arizona opportunity has continued to intensify

Joseph Moore
Equity Analyst
Joseph.Moore@morganstanley.com +1 212 761-7516

Nicole Kozhukhov
Research Associate
Nicole.Kozhukhov@morganstanley.com +1 212 761-1636

Ella Tulchinsky
Research Associate
Ella.Tulchinsky@morganstanley.com +1 212 761-2222

Mason Wayne
Research Associate
Mason.Wayne@morganstanley.com +1 212 761-6012

Shane Brett
Equity Analyst
Shane.Brett@morganstanley.com +1 212 761-1022

## SEMICONDUCTORS

North America
Industry View Attractive throughout the quarter. The Analyst Day in May provided greater clarity on the Arizona build-out, though we continue to view estimate revisions as more likely to be driven by later in the year - particularly around the HDFO ramp cadence and the 2H margin bridge. For the print, we're focused on:

1.) Potential for AMKR pricing benefit as OSAT capacity tightens. The broader backend capacity environment is clearly tight: industry utilization overall is running at \~90% (while AMKR is at mid-70's%), ASE has raised advanced packaging quotes by more than 20%, and non-TSMC CoWoS capacity (Amkor + ASE) is expected to reach \~80kwpm by end-2027 with Amkor growing from 20kwpm to 30kwpm (MSe). TSMC confirmed its own advanced packaging capacity is "so tight that it is limited by customers' growth," welcoming third-party OSATs to absorb overflow. The question is how much of this pricing power flows through to Amkor's P&L - mgmt cited pricing, utilization, and mix as the three levers for 2H GM% expansion, but substrate and material constraints (advanced silicon, memory, BT substrate up 20-30%) are creating nonlinear loading that could limit the capture. We want to hear how much of the industry price upcycle is already in guidance vs. still to come.

2.) Whether the Arizona dilution path has changed since the Analyst Day. The key overhang on the stock in our view remains the pace of GM% recovery and is the primary driver of our EW rating. Mgmt guided for 1-2% operating income dilution starting in 2027 as Arizona construction costs flow through OpEx before programs qualify in \~2028, and the 2028 EPS target of \$2.50 came in below both our estimate and consensus. The \$1.5bn NVIDIA deal and TSMC procurement agreement are strategically important validations of the demand side, though it remains to be seen whether they materially change the dilution math - higher depreciation from front-loaded HDFO equipment and ongoing material supply constraints are real offsets, and we think the earnings power inflection timeline warrants watching closely. We are modestly more conservative than the Street on the pace of the bridge and look to the print for any update to the 2028 framework.

NVTS (UW, reporting after the market close on Monday, July 27th): Expectations are high for an 800V sampling update and additional detail on recent NVTS announcements. As we move through 2H26 and closer to 2027, investors are hyperfocused on evidence of progress in Navitas' 800V roadmap. The company delivered final production samples to customers last quarter and recently announced a licensing deal with Magnachip for GeneSiC Gen 4/5 TAP SiC technology - though we view the Magnachip opportunity as immaterial to the Navitas story near-term, as Magnachip is only just beginning its SiC journey and investors remain squarely focused on the 800V GaN HVDC theme. Legal actions from Renesas and Wolfspeed against Navitas remain an overhang on the stock.

We continue to acknowledge that Navitas 2.0 is moving in the right direction and give credit for the HSD q/q growth mgmt has guided to - but significant proof points remain in question. The stock has pulled back \~70% from its June ATH of \$34 - a meaningful reset, but one that still leaves a wide gap between where the stock is and where the fundamentals are, with a sub-\$10mn quarterly run rate and a long-duration catalyst path. We continue to see more favorable risk/reward elsewhere for high-power themes such as GaN in other MS-covered names such as Innoscience (Daisy Dai), Renesas (Kazuo Yoshikawa), and Infineon (Lee Simpson), which already have incumbency status.

NXPI (OW, reporting after the market close on Tuesday, July 28th): We expect NXP to report an above-consensus JunQ and SepQ guide as peer read-throughs have been quite strong. In our 2Q26 Distributor Survey, auto expectations were notably mixed relative to Industrial, with respondents recording weaker-than-seasonal expectations increasing from 6% to 15%. That said, after overall strong results from TI and STMicro last week - with auto in particular outperforming (+HSD % q/q for TI and +14% q/q for STMicro) - the setup for NXP's print has become more de-risked. More broadly, TI reported a beat and raise, characterizing this point in time as "the start of a cycle that is very, very broad." STMicro similarly beat its JunQ guide, led by auto and Industrial, book-to-bills close to 2 overall, and distribution inventory now below its standard target. With NXP having guided 2Q26 revenue of \$3.45bn (+18% y/y, +8% q/q) and auto at +HSD q/q, the peer data de-risks the JunQ guide and raises the bar for a SepQ raise. What we are focused on for earnings:

1. Lead times and supply tightness: TI confirmed lead times ticked up a couple of weeks in 2Q26 - from below 13 weeks to slightly above - "simply because the demand is growing," with competitors now quoting 52-week lead times. Additionally, CEO Haviv Ilan called out auto dynamics: I think our automotive customers have taken their inventory to very low levels. And now, as there is a little bit more demand, they find themselves in a situation that is not sustainable. I think that also drove part of the demand." Backlog built throughout 2Q26 for both immediate and forward shipment, with short lead time orders a meaningful driver of TI's above-range result. For NXP, which at 1Q26 noted "slight bottlenecks in certain parts of the supply chain" and was already taking selective pricing adjustments, the TI data suggests tightness has intensified further through the quarter - any commentary on lead time extension or escalating customer urgency would be a meaningful positive signal for 2H visibility.

2. Automotive strength driven by China EV/hybrid momentum: TI's automotive inflection was led by China EVs/hybrids, with demand having "developed throughout the quarter" - not visible at the April call and building as the quarter progressed, suggesting the cycle is still early. STMicro confirmed automotive performed "above what we expect and what the market is expecting," guiding the segment to grow \~13-14% y/y for the full year. The read-through for NXP is particularly strong: unlike TI's analog/power-heavy auto exposure, NXP's growth is driven by SDV architecture transitions - S32N, S32K5, imaging radar, 10-gigabit Ethernet - which are content-per-vehicle stories independent of SAAR. NXP's accelerated growth drivers were already north of 45% of auto revenue in 1Q26 and growing double digits, positioning it to capture the tailwinds seen by TI and STMicro.

SWKS (EW, reporting after the market close on Tuesday, July 28th): Skyworks has continued to execute well despite a challenging smartphone environment, and we see a relatively balanced setup heading into the June-quarter print. We model mobile revenue declining \~4% q/q, consistent with management's outlook for an LSD decline, with Broad Markets remaining relatively stable. Apple demand appears to be the most resilient part of the smartphone market, and our hardware team does not anticipate any meaningful changes in iPhone builds in the C2H (Apple covered by Erik Woodring). Given Skyworks' concentration in premium smartphones, we believe the company should hold up better than suppliers with greater exposure to lower-end devices, although rising memory costs and the resulting pressure on handset pricing and demand remain an industry-wide headwind to watch. Blended RF content at Apple should remain roughly flat near term.

Looking to September, we model total revenue increasing 10% q/q, including mobile growth of 16%. Mobile growth is slightly below seasonal, which is typically \~20% q/q, but we are remaining conservative given memory-related cost inflation that is a significant risk, and September iPhone builds that are tracking below seasonal, which may be partly due to Apple's staggered launch. We continue to view the Qorvo acquisition positively, with management targeting an early-2027 close or possibly late 2026.

QCOM (EW, reporting after the market close on Wednesday, July 29th): We moved off Underweight after Qualcomm's data center investor day, as the \$5bn FY27 target made the diversification story far more tangible. Handsets remain under pressure from Android weakness, memory inflation and Apple modem share loss, but the debate has shifted to whether data center can scale fast enough to offset those headwinds. We expect challenging handset fundamentals for the next few quarters.

Double-digit chipset pricing could cushion the Android downturn. We model June handset revenue of \$4.9bn, in line with guidance, with management calling June the bottom for China Android. Bloomberg reported that Qualcomm is raising chipset prices by double digits to offset higher costs, which should support margins, though the benefit will take time and could further pressure demand. We model flattish Android revenue in September and see limited recovery thereafter, with some weakness broadening beyond the low end. Qualcomm should outperform given its premium mix, but we remain below consensus for September at \$9.5bn of revenue (1.5% q/q and -15.5% y/y), including \$4.6bn of handset revenue (-7% q/q and -33% y/y). Apple share loss also becomes more material, with Qualcomm's share of iPhone units falling from roughly 70% in September to 40% in December, though this is well understood. We updated our model to reflect our hardware team's latest Apple assumptions and our revised expectations for Qualcomm's share, with no material change to our full-year estimates.

Diversification is gaining traction, with automotive as the foundation and data center the key swing factor, with possible Trainium participation. Automotive should remain a bright spot, with Qualcomm on track to exit FY26 at approximately a \$6bn revenue run rate according to the latest guidance. In data center, the \$5bn FY27 target appears largely driven by custom silicon, including at least two \$1bn-plus programs, with little contribution from Qualcomm's own CPU or merchant

accelerator products. Alphawave's existing wins should be a meaningful part of the ramp. Qualcomm also continues to develop a custom AI XPU for ByteDance that uses LPDDR rather than HBM, with shipments expected next year. We have also heard Qualcomm could receive a portion of the Trainium opportunity alongside Marvell and Alchip, potentially supported by its access to 3nm wafers. Qualcomm remains our least-preferred AI exposure and the longer-term roadmap is still a show-me story, but \$5bn in FY27 would materially help fill the handset hole and validate the diversification strategy.

ALGM (OW; reports before market open Thursday, July 30th): Strong quarter with continued secular momentum expected, though expectations for auto strength are elevated. We expect Allegro to come in at the high end of its JunQ revenue range with a strong SepQ guide. Following last quarter which was squarely in-line amidst exceptionally high expectations, Allegro is expected to report near the high-end of guidance this quarter as peers TI and STMicro have noted a clear and durable acceleration in automotive demand and overall cyclical dynamics continue to improve.

Since last earnings, the stock has seen significant volatility concentrated in late June/early July which we believe was driven by excitement in Physical AI following ON's acquisition of Synaptics. While Allegro has clarified that material revenue from humanoid robotics is a 2030 opportunity, the company has continued to highlight customer engagement and design win activity. Peer TI flagged that Physical AI was one of the strongest areas within Industrial outside of A&D and energy, and greater detail may provide upside to the stock. For earnings, we are focused on the following:

1) Auto e-Mobility momentum. Auto was flat sequentially in MarQ due largely to seasonal CNY impacts. For JunQ, MSe is +2.1% q/q (+16.0% y/y) to \$167mn, with further acceleration in SepQ to \$174mn (+4.0% q/q, +11.7% y/y). Lean OEM inventories and continued PHEV/BEV content gains support the recovery. TI reported auto up mid-teens y/y and upper-single digits q/q in JunQ, characterizing demand as "everywhere" and noting "a cycle that is very, very broad," led by China EVs/hybrids and unsustainably low customer inventory levels. STM reported auto up 16% y/y and 14% q/q in Q2, with design momentum building across OEM and Tier 1 ecosystems in onboard chargers, powertrain and ADAS.

2) Data Center momentum and progress on the current sensor ramp. Data center reached \~14% of MarQ revenue (up from \~10% in DecQ), and mgmt guided it to reach 16-17% of revenue in JunQ - a new record, implying 20-25% sequential growth. The fastest-growing component is now current sensors, which represented 18% of data center shipments in MarQ (up from zero at the start of FY26), driven by content gains replacing resistors in power racks. Data center and broader Industrial momentum remains according to peers. Critically, current sensors are one of Allegro's higher-margin products - previously data center was margin dilutive driven by motor drivers, but as current sensor mix increases, data center GM is approaching fleet average and is expected to exceed it in the back half of FY27.

ON (++, reporting after the market close on Monday, August 3rd): Expectations have moderated following the stock's sell-off along with power semi peers. While the company reiterated 2Q guidance, we still see potential for a beat and raise as the setup is more favorable than it appears given +ve peer read-throughs. For the print, we are focused on:

1.) Power market recovery: STMicro's 2Q26 earnings call this week highlighted that SiC revenue grew low-teens year-over-year and mid-30s% quarter-over-quarter in 2Q, supported by a book-to-bill well above 1 and a growing backlog - with mgmt confirming SiC revenues will grow double-digit in 2026 versus 2025 based on existing design wins and backlog. STM also noted confidence in a strong 2026, citing "on top of ADAS, SiC, sensor, general-purpose micro, clearly, AI infrastructure and low-earth-orbit satellite will be a very strong contributor to the performance of ST in 2026," along with improving demand in SiC-based power solutions for data center and continued traction in auto design wins. We do believe the broader power market environment has improved, which could have positive netting effects for 2H if replenishment remains muted or does not materialize as expected.

2.) GM% expansion: As of 4Q25, ON had \~700bps of GM% headwinds as a result of underutilization charges (driven by topline). The company gave guidance toward an uptick in utilization in 1Q - which came in at 77%, up from 68% - and an expected trend toward the mid-70s% for the year with progression weighted toward 2H, with utilization guided flat to up slightly in 2Q. With ON already having announced \$200-\$300mn of impairment charges to be recognized through 1H of this year, an associated \$45-\$50mn depreciation benefit in 2026 hitting the P&L in 2H as inventory bleeds through, pricing actions now offsetting input cost headwinds in 2H, and the July 7 announcement of two fab divestitures expected to generate \~\$35mn in annual cost savings starting in 2027, we do see upside toward the year's GM% with the potential for a 4-handle (vs. MSe and Street at 39.6%), which we would see as a surprise relative to buyside expectations.

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Skyworks Solutions Inc SWKS.O</td></tr><tr><td>Mobile Revenue</td><td>- In-line</td><td>- Larg

[中间内容因长度限制已省略]

ry criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/24/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$521.95</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$14.85</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$46.03</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$68.06</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$64.96</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$371.86</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$291.58</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$381.92</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$199.12</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$53.53</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$92.32</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$32.84</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$194.23</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$78.86</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$920.95</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$10.92</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$206.84</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$269.24</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>++</td><td>$86.81</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$86.51</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>E (06/24/2026)</td><td>$166.97</td></tr><tr><td>Quantinuum (QNT.O)</td><td>E (06/29/2026)</td><td>$52.29</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,436.56</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$125.92</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$216.88</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$60.21</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$279.58</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$23.09</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$260.01</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$326.24</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$373.47</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
