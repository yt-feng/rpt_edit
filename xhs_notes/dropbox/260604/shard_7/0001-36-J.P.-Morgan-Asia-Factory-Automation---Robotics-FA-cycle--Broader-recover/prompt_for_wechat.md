你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# Asia Factory Automation & Robotics

FA cycle: Broader recovery, sharper differentiation—GCS takeaways and MIR 1Q26 review

China’s FA sector entered 2026 with a much firmer footing, as momentum broadened well beyond a handful of end-markets and the narrative shifted from “is demand recovering” to “which players can convert robust order flow into profitable shipments.” MIR’s 1Q26 review shows FA sales up 7% Y/Y—the strongest since 4Q22—while IA and PA rose 2% Y/Y and 1% Y/Y, respectively. MIR also raised its full-year FA outlook by 3%, now forecasting 13% Y/Y growth in 2026E and 10% Y/Y in 2027E, citing a better demand pulse and support from structurally growing sectors. Notably, Inovance’s IA order growth sustained above 40% Y/Y in May, extending the strong YTD momentum and underscoring the strength of the upcycle for leading platforms. The cycle is increasingly quality-led: PLCs and AC servos sustained over 10% Y/Y growth (with AC servo up 17% Y/Y), and industrial robots maintained double-digit growth at 14% Y/Y, with electronics and auto electronics still the key swing factors. At the same time, input-cost volatility and component tightness are resurfacing, making pricing discipline and delivery execution central to outcomes. Tier-one platforms with stronger solution breadth and supply-chain resiliency are better positioned to pass through costs and defend GPM, while smaller players risk being squeezed by faster cost resets and price-sensitive customers. Market share shifts reinforce this winner-takes-more setup: Inovance gained 6, 2, and 2 ppts Y/Y in small PLC, mid-to-large PLC, and AC servo, respectively, while Estun further strengthened its top-player status in robotics with a clearer mix upgrade angle. Humanoid robots remain a secondary option for 2026 earnings, but are already influencing capacity planning for precision components, with Leader Drive standing out as a direct beneficiary.

From a stock and sentiment perspective, the market reflects that much of the easy re-rating occurred in 2025, and 2026 is increasingly about execution—especially margin delivery—rather than just order momentum. Year-to-date, Japan and Taiwan have outperformed China on stronger order prints, while China FA and robotics names have shown a more two-speed pattern: Leader Drive and Estun have been the standout performers, supported by their respective drivers—humanoid-linked volume ramp for Leader Drive, and margin recovery off a low base with demand supported by lithium battery, energy storage, and AI-linked capex for Estun. Over the past month, sector sentiment has improved, with the group up c.7% on average versus a 16% YTD gain, helped by incremental Tesla supply chain progress, FA players' order growth pick-up in April–May, and 4Q25/1Q26 earnings risks being absorbed. Outside China, leadership has been underpinned by tangible order acceleration, with Fanuc's quarterly orders up 19% Y/Y in 1Q26 (vs. 9% Y/Y in 4Q25), and AirTAC and Hiwin's April sales reaccelerating to over 20% Y/Y, reinforcing a synchronized

# Infrastructure, Industrials & Transport

Karen Li, CFA AC

(852) 2800-8589

karen.yy.li@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Sunny Su

(852) 2800 8551

sunny.su@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Arjun Joshi

(91-22) 6157-3745

arjun.joshi@JPM.com

JPM India Private Limited

# Jenny Qiu, CFA

(852) 2800 8503

jenny.qiu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Mufan Shi

(852) 2800-8502

mufan.shi@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Beatrice Lam

(852) 2800-8738

beatrice.lam@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

upturn even as investors remain focused on which platforms can translate volume into margin amid ongoing raw material cost pressures.

Sector results so far provide positive read-throughs, with 1Q26 earnings and YTD price action highlighting margin repair and constructive demand outlook. Our stock views remain constructive: we recommend buying on dips amid volatile share price swings in recent months, as we believe the FA upcycle remains intact and humanoid robot commercialization is still a key theme, despite near-term profit taking and ongoing sector rotation. We continue to favor leading names such as Inovance, Hengli Hydraulic, UBTech, Sanhua-A/H, Leader Drive, Estun, and Yiheda, which we believe are best positioned to benefit from accelerating market-share gains, robust new product launches, and the ongoing shift towards higher-value, innovation-driven growth in both automation and robotics.

# China's FA data started 2026 on a firmer footing, with momentum broadening beyond a narrow set of end-markets

MIR's 1Q26 review shows China FA segment sales grew 7% Y/Y (the strongest since 4Q22), while the broader IA market rose 2% Y/Y and PA rose 1% Y/Y. The headline reads encouraging, but the quarter also highlighted a familiar reality: winners are separating via end-market mix (notably exposure to AIDC-linked electronics and high-end manufacturing) and supply-chain execution, as input-cost volatility and component constraints resurfaced. The key debate into 2H26 is less “is demand recovering” and more “who can convert demand into profitable shipments.”

A stronger 1Q26 print strengthens the cycle narrative, while PA remains the laggard. MIR's 1Q26 data points to a solid start to 2026, with FA sales +7% Y/Y, IA +2% Y/Y, and PA +1% Y/Y. Importantly, MIR lifted its full-year FA outlook by 3%, now forecasting FA +13% Y/Y in 2026E and +10% Y/Y in 2027E, citing a better demand pulse and support from structurally growing sectors. The growth mix matters: electronics, semiconductors, robotics, NEV-related capex, and aerospace remain the cleaner demand pools, while PA is poised to stay muted given slower capex in oil & gas, metallurgy, and petrochemical, alongside softer replacement demand. In other words, the tape is improving, but it still rewards “right exposure + right execution” rather than broad beta.

Pricing actions are re-emerging, and the market is polarizing around who can pass through. Raw material inflation and periodic component tightness are bringing pricing discipline back into focus. Some suppliers (e.g., Inovance) have implemented price hikes to protect profitability, but the early signal from channel checks is that pricing is not moving uniformly across the stack. The mid-to-high end is showing clearer polarization: tier-one players with stronger product competitiveness, delivery reliability, and solution breadth are in a better position to push pricing through, while smaller players risk being squeezed between customers that remain price-sensitive and cost lines that reset faster than selling prices. This sets up a familiar “share shift + margin dispersion” pattern, where pricing power becomes a market-share tool rather than a purely defensive lever.

Product momentum remains healthiest in control and motion, with clear end-market drivers behind it. At the product level, PLCs and AC servos sustained $>10\%$ Y/Y growth in 1Q26, with AC servo +17% Y/Y leading the pack, consistent with a cycle that is upgrading toward higher content and higher-value motion/control. Low-voltage inverters posted a rebound to +4% Y/Y in 1Q26, but the read-through is that demand remains more mixed and sensitive to project cadence and export-linked EPC dynamics. The demand drivers look “quality” rather than purely cyclical: lithium battery-related activity surprised positively (including supporting infrastructure such as substations), auto customers accelerated production-line equipment procurement, and AI supply-chain capex (PCB/electronics/semiconductors) created spillover into selected adjacent categories (e.g., laser equipment). This mix supports the view that the cycle is increasingly shaped by advanced manufacturing capex rather than broad industrial volume alone.

Robotics growth moderated but stayed double-digit, with electronics still the key swing factor. MIR data shows the industrial robot market retained double-digit growth in 1Q26 (+14% Y/Y, vs +17% Y/Y in 4Q25), indicating moderation from a strong exit rate but not a break in trend. End-demand looks broadly positive Y/Y, including solar, with electronics (including auto electronics) leading at >20% Y/Y. Auto parts and lithium battery demand also stayed robust at +19% Y/Y. The more important takeaway for investors is that robotics demand is increasingly “application- and customer-specific,” which tends to reward suppliers with a proven portfolio, fast iteration, and service capability, rather than a pure price-led strategy. This also links back to the broader FA theme: robotics is amplifying the premium on reliability, delivery, and solution integration.

Market share shifts are becoming more visible, and supply-chain execution is a differentiator again. The latest market landscape highlights two differentiators: (1) supply-chain resiliency amid renewed noise around chips and input costs, and (2) exposure to growth sectors such as AIDC-linked demand. Inovance expanded market share in small PLC / mid-to-large PLC / AC servo by 6/2/2 ppts Y/Y to 14%/6%/33%, while losing share in low-voltage inverter as capacity and delivery priorities were tilted toward PLC and servo. In aggregate, Inovance stood out as the most visible share gainer, while most other share changes were small (typically <1 ppt). Among global peers, Mitsubishi lost 2 ppts Y/Y share in servo, while Siemens gained 2 ppts Y/Y in servo and low-voltage inverter, consistent with the theme that consolidation is playing out in favor of scaled, tier-one platforms.

Robot vendor dynamics show domestic leaders consolidating, but product mix still matters for “quality of share.” Competitive dynamics in industrial robots continue to evolve, with Estun strengthening its “top player” status. Estun regained the No.1 position in 1Q26, together with Inovance and KUKA, each at 9.7% share. Inovance was the most visible share gainer in the quarter (+0.7 ppt Y/Y), though its mix skews more toward smaller-sized robots versus Estun, which matters for ASPs, application mix, and margin structure. For Fanuc, ABB, and Yaskawa, shares broadly stabilized at around \~10% / \~5% / \~5% over the past three years, albeit with a mild declining bias. Net-net, the structure suggests domestic players are gaining relevance, but investors still need to underwrite where the share is being won (product tier, applications, and customer quality), not just the headline share number.

# China Summit takeaways point to a capacity-constrained upcycle with sharper winner-takes-more dynamics.

Shenzhen Inovance, Estun Automation, Leader Drive, and UBTech collectively reinforced a 2026 setup where demand is improving, but outcomes are poised to diverge based on who can scale capacity, protect margin via mix/solution attach, and convert structural opportunities (AI capex spillover + localization) into repeatable share gains.

2026 was consistently framed as an IA-led upcycle where “orders are not the bottleneck, delivery is.” Multiple checks suggested 2026 demand is poised to be better than 2025 on a broader capex recovery and a firmer FAI backdrop, but the more actionable constraint is capacity and delivery capability—particularly in PLC/servo and select precision components where supply tightness can reappear. Management commentary emphasized near-term capacity expansion to clear backlog (one large player targeting \~30% capacity lift in 2Q26 to digest 1Q26 order accumulation), alongside a deliberate reallocation of capex toward IA versus NEV-type investments made in prior years. The implication is that reported revenue may lag order momentum in the near term (order-to-delivery commonly 1–3 months for standard products), but the strategic direction favors those who can scale without introducing margin leakage.

IA demand is broad-based, with AI capex providing both direct pull and spillover into “traditional” segments. Summit discussions converged on a view that 2026 demand is not a single-theme AI trade, even if AI/data center buildout is a key accelerant. Orders were described as strong across lithium battery & energy storage, electronics/3C, and semiconductor-adjacent supply chains, with a meaningful spillover into machine tools and adjacent equipment where compute/server buildout drives thermal/precision processing and manufacturing upgrades. Several speakers highlighted improving conditions in selected “traditional” sectors (e.g., injection molding, machine tools, pockets of process industries), suggesting a more durable upgrade cycle rather than a narrow stimulus pulse. The practical read-through is that end-market diversity is becoming a competitive advantage: suppliers exposed to both “new economy” capex and structurally upgrading legacy industries are better positioned to sustain growth if macro conditions remain uneven.

Pricing and raw material inflation are shaping margin dispersion, not just headline demand. Input pressure points cited included copper-related items, memory shortages affecting certain automation components, and PCB/inverter-linked costs, with PLC mentioned as a more impacted category YTD due to component sensitivity and demand intensity. Some players referenced two rounds of pricing actions in 1Q–2Q26, with additional rounds possible if cost inflation persists, while also acknowledging that pass-through cadence can lag cost resets quarter-to-quarter. The margin narrative was generally “stable to slightly improving” through mix upgrade, productivity gains, and supply-chain optimization (localization, longer-term supplier agreements), but with acknowledged noise around component availability and timing mismatch. The investor-relevant point is that the upcycle is rewarding discipline: players with pricing power and solution attach are more likely to hold GPM steady, while price-takers risk a margin squeeze even if revenue prints look fine.

Industrial robots are moving toward higher-quality growth, led by payload/mix upgrades and foreign substitution. Industrial robot discussions emphasized a shift toward mid-to-large payload and higher-end scenarios as the key “quality lever,” with foreign-brand substitution still the structural runway—especially where system value-add, engineering requirements, and integration knowhow matter more than unit price. Demand remained concentrated in autos/auto parts, lithium battery & energy storage, and electronics, with broader general industrial applications improving at the margin. YTD growth sequencing was described as lithium battery/energy storage fastest, then electronics, then construction machinery and autos, broadly consistent with AI-capex-linked activity and manufacturing upgrade. OEMs increasingly emphasized “high-quality growth” (selective bidding, higher-margin scenarios, standardized workstations, after-sales expansion) rather than pure volume share, which is supportive for steadier margin progression even if commoditized segments remain highly competitive.

Humanoid robots remain a secondary optionality for 2026 earnings, but they are already influencing capacity planning and component tightness. Most IA players positioned humanoids as early-stage exploration leveraging existing industrial automation know-how rather than a core 2026 earnings driver; near-term financial outcomes are still dominated by IA and industrial robots. The more immediate implication is indirect: incremental humanoid-related demand adds to capacity tightness for certain precision components and increases the premium on scalable manufacturing, quality consistency, and supply-chain control. Leader Drive stood out as the more explicit humanoid supply-chain beneficiary due to harmonic reducer intensity in humanoids.

# Peer read across from Asia and Europe underscores a selective but accelerating China FA upturn.

Asian and European peers are converging on the same message: China's FA recovery is real, but the “where” matters— electronics/semis, data centers, and selected advanced manufacturing are doing the heavy lifting. Taiwan suppliers are the cleanest early-cycle read given their short-cycle order visibility, Japan is showing the sharpest China growth contribution in several platforms, and Europe is framing China as improving but still selective, with strength concentrated in electrification, motion, and localized automation portfolios.

The practical implication for investors is that China exposure is increasingly a quality filter rather than a simple beta call. Companies with (i) China-local product portfolios, (ii) ability to serve high-tech capex, and (iii) operating discipline to defend margins through mix and productivity are poised to show the most consistent earnings conversion as the cycle broadens.

Taiwan suppliers are signaling a synchronized upturn, with order backlogs and lead times pointing to continued strength. Taiwan automation and component suppliers continue to provide one of the clearest early-cycle reads for China FA, and the tone is constructive on both demand breadth and order conversion. Hiwin flagged “very hot” demand in tool machines and semiconductors, with China order lead times now at 3.5–5 months, which typically indicates both improved end-demand and tighter near-term capacity allocation at the customer level. AirTAC reported record monthly revenue and record order-booked amount in Apr 2026 despite fewer working days, and highlighted that orders are still outpacing shipments, pushing backlog to new highs—an important sign that the cycle is not just a one-off restocking event. The common thread across both is that the strongest demand pools remain electronics, batteries, machine tools, and general machinery, while the margin narrative is framed around production efficiency and mix, rather than price-led growth alone—consistent with a healthier cycle phase where “delivery + mix” becomes the P&L bridge.

Japanese players are increasingly calling out China as a fast-growing region, with orders and profit leverage improving on volume and mix. Japan's FA leaders are also seeing

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
