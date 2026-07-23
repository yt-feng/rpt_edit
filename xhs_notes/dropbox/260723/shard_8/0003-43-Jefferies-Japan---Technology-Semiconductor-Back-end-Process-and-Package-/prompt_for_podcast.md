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
# Semiconductor Back-end Process and Package Trends

We held a seminar on the topic with Professor Fumihiro Inoue from Yokohama National University. He is the top Japanese researcher in the field of advanced packages. AI application has significantly expanded the market for advanced packages. Professor Inoue believes that optimization of the overall system will be important for package technology as well. Below we summarize the content of his presentation.

Fumihiro Inoue:

• Professor, Yokohama National University

\- Semiconductor and Quantum Integrated Electronics Research Center, Deputy Center Head and Professor

• Cross-Appointment Professor, Hokkaido University

• LSTC, 3D Packages Deputy Division Head

• 2011-21 imec Researcher

\- Main research areas: Semiconductor back-end process, chiplets, 3D integration, process development

AI system configuration: In contrast to traditional CPU-centric configurations in PCs, smartphones, and other devices, AI systems utilize a configuration with memory (DRAM, SSD, and HBM) that conduct high-speed data interaction with CPU and GPU devices. CPU importance is growing again amid future expansion of the edge AI market, in addition to cloud AI. Chiplets, which integrate multiple chips, are essential systems for the realization of AI systems due to the increasing difficulty of delivering cost and power consumption improvements for monolithic devices via finer processes. Chiplets connect individual devices manufactured at high productivity using optimal technology nodes and facilitate advantages in power consumption and costs and optimal interconnection designs. Back-end processes are not just simple assembly steps and actually generate added value. While GPU computation performance has been steadily rising each year, data movements between GPUs, GPU and memory (HBM), and racks have become bottlenecks. It is necessary to review the AI system concept to resolve these issues. AI will be experiencing transformation from a "computation device" to a "communication system."

Dominance structure in cloud AI: NVIDIA builds a software ecosystem based on CUDA. It provides "platforms" rather than just standalone GPUs. TSMC has an overwhelming position in supply capacity for advanced processes and advanced packages and influences the possibility of shipping AI GPUs. Investors and customers have confidence in the combination of NVIDIA (design) and TSMC (production, mounting). The next hurdles are interconnections and power. Co-packaged optics (CPO) technology offers a "solution" to the limits of copper interconnections. NVIDIA and TSMC are leaders in co-packaged optics as well. (continued next page)

TSMC's COUPE connects EIC (electronic integrated circuits) and PIC (photonic integrated circuits) using TSMC-SolC bonding technology. It supports high-precision connections between chips. Results announced at the ECTC event in 2025 were low impedance in the chip-chip interface, bond density of at least 16 times, and $85\%$ reduction of stray capacity. This format raises speed by $170\%$ or more at the same power consumption and can reduce power usage by $40\%$ . SolC narrow-pitch bonding improves power integrity and signal integrity and is suitable for high-speed data communications. COUPE utilizes a shared 3D multilayer structure as the substrate and supports grating coupler (GC) and edge coupler (EC) types. It exhibits structural flexibility. For optical design, the GC type curtails optical loss with an embedded microlens at the optical-path end, rear-side metal reflection panel under the GC, and optimized anti-reflection coating (ARC) surface. Process optimization has reduced insertion loss from the COUPE additional optical path to effectively zero dB.

The real significance of co-packaged optics (CPO) is not "replacement of copper interconnections with light." Reduced power for SerDes (conversion from parallel communication to serial communication (Ser) and restoration (Des)), I/O, and re-timer (repair and regeneration of digital signals degraded and distorted on the transmission path) components that account for the bulk of power usage is a major issue. Co-packaged optics changes the I/O position and role. The key point is "the extent to which it is possible to lower power usage for connecting to the outside" rather than "how quickly it is possible to carry out calculations."

There is interest in technologies from Broadcom, Marvell, and Ayar Labs for the future "I/O-driven era."

Japanese companies possess global top-level materials and parts but are lagging in systems and mounting. They have core technologies. However, their package design and volume-production mounting capabilities premised on co-packaged optics are weak. There is also an absence of simultaneous optimized design of light, electricity, and heat, and the concept of "how to integrate and sell" is lacking. Japanese companies have approached co-packaged optics as a future technology and research theme and thereby divorced design, mounting, and business perspectives from the research initial stage. Globally, meanwhile, co-packaged optics is on the cusp of volume production, and the industry is advancing in "architecture x package" building.

## Cloud AI isn't everything

Chiplets are progressing. On the business front, key issues are (1) advances in standardization but limited genuine compatibility, (2) under-developed analysis for EDA and PPA, (3) lack of clarity regarding responsibility roles and yield risk when defects occur, (4) pursuit of vertically integrated models by TSMC, Intel, and Samsung and lack of an open model leader, and (5) many cases of activity stopping at the prototype level because of inability to overcome test, supply, and cost issues after functional verification (volume production wall). The industry has moved into an era in which technology advantages are not enough to win. Trustworthy rules, frameworks, and partnerships will determine whether businesses succeed or not.

Cloud AI is currently the centerpiece of AI systems. However, it is not a perfect solution from power, latency, communication cost, and geopolitical and infrastructure control perspectives. It is not possible to handle everything in the cloud. In particular, edge AI is necessary in industrial, automotive-based, robot, and infrastructure monitoring areas. Role division is cloud AI for learning and consolidation and edge AI for inference and immediate decisions. The AI semiconductor market was worth US\$236bn in 2025 (including cloud AI at roughly US\$160bn and edge AI at about US\$80bn). According to the VLSI forecast, this should expand to US\$371bn in 2028 with cloud AI at US\$250bn and edge AI at US\$120bn.

Edge AI is not a substitute for cloud AI. It is a core technology that has necessarily emerged from the limits of cloud AI. Cloud AI faces limitations in terms of infrastructure (power and environmental constraints accompanying explosive increase in computation volume), society and systems (information security and data sovereignty), and value and UX (personalization and realtime features, ultralow latency, and constant inference requests). These aspects are powerful drivers of edge AI.

HBM is a "technology that speeds up AI." In contrast, edge AI is a "technology that distributes AI in massive amounts." HBM is not suited for the edge from the perspective of power consumption, package costs, and volume scale. The main presence in edge AI is likely to be DDR x 3D layering.

Qualcomm announced a roadmap for data centers in the Agentic AI era. The structure of connecting HBM and compute via an interposer consumes power through data passage over a physical "bridge." With wider bandwidth, the additional portion consumes more energy. HBC Gen1 advocated by Qualcomm (used in Qualcomm's AI250 AI-inference chip for data centers), meanwhile, places a multilayer structure on a 2D organic substrate (it does not use TSMC's CoWoS). It realizes 133TB/s effective memory bandwidth per card without using memory devices that support the bandwidth available from HBM. The value is 18 times more than the AI200's LPDDR5.

## Areas and materials disrupted by technology innovation

Advanced packages that include HBM (such as CoWoS) currently mainly rely on a silicon interposer. Finer processing for substrate RDL and glass-core substrate mounting technology, meanwhile, are rapidly advancing. Silicon interposers face structural redundancy, scalability, and cost risks. Another risk is relative dilution of interposer value by the technology advancement pace on the substrate side. If the substrate side becomes capable of supporting the same interconnection density as the passive interconnection layer, this might undermine the assumption that the interposer is an essential part (redefining the function division).

When the organic RDL interposer is integrated into a glass-core substrate, this might reduce the usage frequency and market scale of carrier glass, temporary adhesives, and TMV (through mold via) and mega-pillar formation thick-coat resist and plating solutions (anticipated occurrence from 2030 as a timeline).

To address these technology innovations, materials manufacturers need to strengthen proposal capabilities from "selling standalone materials" to "offering process + evaluation + design." Since this response requires more than just domestic capabilities, it is essential to build back-end process co-creation sites abroad (particularly in the US).

Resonac launched the US-JOINT consortium of 10 Japanese and US companies in Silicon Valley and has defined a framework to move forward with back-end process technologies in the US.

There will also be a shift from wafers to panels and large surface areas. Since prototype approaches change with organic interposers and substrate scale, materials manufacturers are striving to attract participant companies under a "shared prototype line" banner. Resonac has launched the JOINT3 consortium that has 27 companies with the aim of building a panel-level (515 x 510mm) organic interposer prototype line.

## New era that enables CMOS2.0 and hybrid bonding

Huawei has proposed Tau Scaling Law at ISCAS2026. This is a new scaling strategy beyond Moore's Law.

Process migration confronts physical limits and increased costs. For China, it is necessary to have a new strategy for improving performance amid access restrictions to EUV lithography equipment. Huawei proposes a new indicator of shrinking the signal transmission time (Tai) rather than focusing on the number of transistors. More Moore makes smaller transistors. In contrast,

Huawei's Beyond Moore is a CMOS2.0-type concept. It aims to comprehensively optimize devices, circuits, chips, and systems and thereby reduce overall system delay.

The current semiconductor industry structure consists of leading companies in design, production, EDA< equipment, and mounting and test areas, such as NVIDIA and TSMC. This makes it difficult to achieve simultaneous optimization of design, process, mounting, and systems required by CMOS2.0. China, meanwhile, can develop design, production, mounting, and AI systems in a vertically integrated manner led by the government. It can optimize performance for the overall eco-system rather than achieving the top level worldwide for individual technologies. Huawei's announcement shows that China has started to genuinely seek verification of this direction.

Hybrid bonding is not "next-generation bonding after bumps." Current micro-bumps (up to 40 microns) have an I/O boundary between chips, and design fundamentally takes place at the chip unit. Interconnections temporarily stop at the chip boundary. In hybrid bonding (100nm-level), however, BEOL links chips (interconnections extend beyond the boundary), and this supports design division at the interconnection layer unit and removes the boundary between chips. Hybrid bonding is not just a bonding technology. It is a technology that redefines system setup across the BEOL (bringing it outside).

## Current situation in Japan

Chiplets deliver Scale-up (higher integration = front-end process merger) x Scale-out (planar rollout = large substrates, co-packaged optics). The Scale-up portion is more important than Scale-out for functions and composition required by edge AI. Japan's current back-end process R&D activity, meanwhile, is overly skewed toward Scale-out. Panel/PLP is an excessive boom and cannot handle the edge AI trend.

For NAND, a Japanese company advocates MAS-CBA, an approach that separately manufactures NAND CMOS circuit and memory cell wafers and directly bonds them with CU. This technology significantly raises I/O speed, reduces electrical resistance, boosts writing speed, and achieves low latency and power consumption. This is a competitive technology.

Key technologies for next-generation packaging are hybrid bonding and fine-pitch substrates (glass core, bridge (EMIB-T), and advanced RDL on substrate). System mounting that does not rely on an interposer will be important (creating post-CoWoS).

## Analyst Certification:

I, Masahiro Nakanomyo, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Hisako Furusumi, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

Registration of non-US analysts: Masahiro Nakanomyo is employed by JEF Japan Company Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst.

Registration of non-US analysts: Hisako Furusumi is employed by JEF Japan Company Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst.

As is the case with all JEF employees, the analyst(s) responsible for the coverage of the financial instruments discussed in this report receives compensation based in part on the overall performance of the firm, including investment banking income. We seek to update our research as appropriate, but various regulations may prevent us from doing so. Aside from certain industry reports published on a periodic basis, the large majority of reports are published at irregular intervals as appropriate in the analyst's judgement.

## Investment Recommendation Record

(Article 3(1)e and Article 7 of MAR)

Recommendation Published July 20, 2026 23:20 P.M.

Recommendation Distributed

July 20, 2026 23:20 P.M.

## Explanation of JEF Ratings

Buy - Describes securities that we expect to provide a total return (price appreciation plus yield) of 15% or more within a 12-month period.

Hold - Describes securities that we expect to provide a total return (price appreciation plus yield) of plus 15% or minus 10% within a 12-month period. Underperform - Describes securities that we expect to provide a total return (price appreciation plus yield) of minus 10% or less within a 12-month period. The expected total return (price appreciation plus yield) for Buy rated securities with an average security price consistently below \$10 is 20% or more within a 12-month period as these companies are typically more volatile than the overall stock market. For Hold rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is plus or minus 20% within a 12-month period. For Underperform rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is minus 20% or less within a 12-month period.

NR - The investment rating and price target have been temporarily suspended. Such suspensions are in compliance with applicable regulations and/or JEF policies.

CS - Coverage Suspended. JEF has suspended coverage of this company.

NC - Not covered. JEF does not cover this company.

Restricted - Describes issuers where, in conjunction with JEF engagement in certain transactions, company policy or applicable securities regulations prohibit certain types of communications, including investment recommendations.

Monitor - Describes securities whose company fundamentals and financials are being monitored, and for which no financial projections or opinions on the investment merits of the company are provided.

## Valuation Methodology

JEF' methodology for assigning ratings may include the following: market capitalization, maturity, growth/value, volatility and expected total return over the next 12 months. The price targets are based on several methodologies, which may include, but are not restricted to, analyses of market risk, growth rate, revenue stream, discounted cash flow (DCF), EBITDA, EPS, cash flow (CF), free cash flow (FCF), EV/EBITDA, P/E, PE/growth, P/CF, P/FCF, premium (discount)/average group EV/EBITDA, premium (discount)/average group P/E, sum of the parts, net asset value, dividend returns, and return on equity (ROE) over the next 12 months.

## JEF Franchise Picks

JEF Franchise Picks include stock selections from among the best stock ideas from our equity analysts over a 12 month period. Stock selection is based on fundamental analysis and may take into account other factors such as analyst conviction, differentiated analysis, a favorable risk/reward ratio and investment themes that JEF analysts are recommending. JEF Franchise Picks will include only Buy rated stocks and the number can vary depending on analyst recommendations for inclusion. Stocks will be added as new opportunities arise and removed when the reason for inclusion changes, the stock has met its desired return, if it is no longer rat

[中间内容因长度限制已省略]

ular investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
