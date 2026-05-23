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
# JPM CHINA SUMMIT: Day 2 Wrap - ESS & NEV

Joann Kim
+852 2800 8016
joann.kim@JPM.com

\*\* Sales Commentary only

Day 2 investor feedback continues to show a cautious but selective stance on China, given weak domestic demand and the property overhang, which leads to muted market beta. However, conviction in AI/tech and supply-chain leaders remains strong despite growing concerns about crowding and valuations. Within industrials, sentiment is relatively constructive, with a preference for globally competitive, export-oriented, and scale-driven players—such as machinery, robotics, and batteries—seen as key beneficiaries of China’s manufacturing edge. In autos, views are more mixed due to weak domestic demand, while strong overseas demand and a slightly easing competition landscape in the domestic market (with Leapmotor noting eased domestic competition) are providing some support. For ESS/batteries, long-term structural demand is well recognized (driven by AI power and energy transition), but investors are increasingly wary of mid-cycle risks due to aggressive capacity expansion over the next 12 months and margin pressure concerns from higher lithium pricing—reinforcing a focus on dominant players like CATL. Flagging Rebecca Wen’s downgrade on Yunnan Energy (002812 CH) to Neutral due to a series of capacity announcements across the battery separator industry that may cap the potential for further price hike.(Rebecca Wen)

Stay Tuned for our 3rd day for BYD, Weichai Power & Robotics/ESS Panel Sessions! Also, happy to discuss details of my meetings when I am back in HK next week!

# ESS - Robust Demand Amid Cost Inflation: Focusing on Overseas & New Products

\- While investors acknowledge robust demand in ESS with global ESS shipments recording +109% YoY in 4M26, investors focus shifts to lithium price tolerance and demand implications. (Rebecca Wen's ESS Industry update note). Gotion High-Tech (002074 CH) highlighted a structurally robust China ESS demand backdrop but with increasing discipline around project economics, set against an intensely competitive domestic market and ongoing cost volatility driven by lithium prices. Management emphasized overseas expansion as a key margin lever and reiterated a longer-term technology roadmap anchored by sodium-ion batteries for ESS and solid-state batteries for premium applications. Post the meeting, investor feedback was mixed with concerns focusing on: 1/ the risk that ESS industry demand may slow, with Gotion projecting >60% YoY industry demand growth (vs 4M26 +109% YoY) amid aggressive capacity addition by key industry players; and 2/ cost inflation impact on margin, with raw material now accounting for \~50% of battery cost and potential for negative demand impact if domestic ESS proves most sensitive. Prefers CATL with dominance and clear cost leadership with scale.

# NEV - Shipment Outlook, Model Cycle, Overseas Strategy in Focus

\- Attended meetings with Geely (175 HK) and Leapmotor (9863 HK) today, investors focused on the feasibility of shipment guidance, the impact of cost inflation—particularly from batteries and raw materials—on profitability, and the companies' mitigation strategies.

\- The most interesting takeaways from the Geely meeting were the potential upside risk to its overseas shipment guidance supported by policy tailwinds in ASEAN, rising NEV adoption in EU, and an improving product mix (domestic/overseas). Geely commented that its 2026 export target of \~640k units looks achievable, with scope to exceed \~750k as high oil prices, policy tailwinds (notably Malaysia), and premium penetration drive demand across Europe, Southeast Asia, and emerging markets, with Europe's export momentum already trending above its target. Upside is anchored in a product-led strategy led by Zeekr, where flagship models such as the 9S deliver strong margins and brand validation overseas, while the phased rollout of 9S (from Q3) and 8S (2H26) broadens the addressable market without diluting positioning. Crucially, management is

focused on disciplined model-cycle management—using complementary models, derivatives, and staggered launches—to keep products fresh, sustain buyer interest, stabilize pricing, and protect profitability to offset the impact of cost inflation.

\- Leapmotor management reiterated confidence in a Q2 recovery, but investor discussion centered on the feasibility of volume guidance and margin improvement amid ongoing cost pressures. Key questions focused on whether the Q2 volume target of 240–250k units is achievable given recent momentum and the ME-driven situation impacting export timelines, which has resulted in a two-week longer delivery period due to taking a longer route. Additional concerns included the impact of battery and raw material costs—particularly lithium—on margins, with management highlighting cost pass-through, supplier negotiations, and simplification of battery packs as partial offsets. Domestic competition was seen as stabilizing versus prior years, with loss-making models discontinued post Govt's anti-involution guidelines, while overseas strategy remains a core lever for mix and margin improvement, supported by Stellantis' distribution network and partnership, planned CKD production in Europe at Stellantis' factory, and a growing contribution from higher-margin models such as D19.

\- Investors' feedback on Chinese OEMs was mixed due to weak domestic demand (with high-frequency data tracking below the market's 2Q25 expectation of industry-wide 25–30% QoQ recovery), while strong overseas demand and a slightly easing competition landscape in the domestic market (with Leapmotor noting eased domestic competition) are providing some support. Feedback suggested investors are most constructive on Geely for its right product cycle, strong shipments in both domestic and overseas markets, and mix improvement amid cheap valuation. Debate on BYD continues, with long-term investors shifting focus to overseas market-driven margin support, as BYD has recently de-emphasized the domestic market; LT investors' key question is whether BYD could be the next Toyota, driving most profit from the overseas market, with clear market share leadership in key demand markets (Europe for BYD's case).

JPM Research: China Auto's OEM In Europe - Structural share gains, broadening mix, and the localization race - Nick Lai

# J.P Morgan Industrials & Auto Contacts

![](images/80a99c9df2d280d2da4480e358c1bd40faed3653540350364f5193630919b3c1.jpg)

<details>
<summary>natural_image</summary>

Black-and-white headshots of two individuals: one in a business attire holding a book, the other in glasses with a beard (no text or symbols visible)
</details>

# Sector Specialists:

APAC Industrials: Joann Kim joann.kim@JPM.com +852 2800 0816

EU Industrials: Sam Edmunds sam.edmunds@JPM.com +44 207 742 8733

# APAC Industrials Trading:

Jonathan Malts jonathan.maltz@JPM.com +852 2800 8820

# APAC Electric Equipment & Multi-Industry Research:

Junya Ayada (Japan) junya.ayada@anmol.com +81 3 6736 8631

Stephen Tsui (Korea & China) stephen.tsui@JPM.com +852 2800 8592

# APAC Aerospace & Defense Research:

Atul Tiwari (India) atul.tiwari@JPM.com +91 22 6157 3582

Simon Han (Korea) simon.x.han@JPM.com +82 2 758 5711

Karen Li (Singapore) karen.yy.li@JPM.com +852 2800 8589

# APAC Machinery & FA Research:

Karen Li (China) karen.yy.li@JPM.com +852 2800 8589

# APAC Engineering/Construction & Heavy Transportation Equipment Research:

Lee Power (Australian Heavy Transportation) Lee.Power@JPM.com +61 2 9003 8725

Karen Li (China Heavy Transportation) karen.yy.li@JPM.com +852 2800 8589

Nick Lai (China Heavy Transportation) nick.yc.lai@JPM.com +86 21 6106 6353

Jenny Qiu (China E&C) jenny.qiu@JPM.com +852 2800 8503

Amyn Pirani (India Heavy Transportation) amyn.pirani@JPM.com +91 22 6157 3583

Atul Tiwari (India E&C) atul.tiwari@JPM.com +91 22 6157 3582

Akira Kishimoto (Japan Heavy Transportation) akira.x.kishimoto@JPM.com +81 3 6736 8646

Simon Han (Korea Shipbuilding) simon.x.han@JPM.com +82 2 758 5711

Yen Voo (Malaysia E&C) yen.voo@JPM.com +60 3 2718 0914

# APAC Homebuilders and Building Products:

Mio Shikanai (Japan) mio.shikanai@JPM.com +81 3 6736 1313

# APAC Autos & Auto Parts Research:

Lee Power (Autos & Auto Parts) Lee.Power@JPM.com +61 2 9003 8725

Nick Lai (China Auto) nick.yc.lai@JPM.com +86 21 6106 6353

Rebecca Wen (China Auto Parts & EV Battery) rebecca.y.wen@JPM.com +852 2800 8505

Inda Li (China EV supply chain) inda.li@JPM.com +852 2800 8507

Amyn Pirani (India Auto) amyn.pirani@JPM.com +91 22 6157 3583

Vibhav Zutshi (India EV Battery) vibhav.zutshi@JPM.com +91 22 6157 3585

Benny Kurniawan (Indonesia Auto) benny.kurniawan@JPM.com +62 21 5291 8024

Akira Kishimoto (Japan) akira.x.kishimoto@JPM.com +81 3 6736 8646

Jay Kwon (Korea EV Battery) jay.h.kwon@JPM.com +82 2 758 5725

# US Industrials & Auto Research Team:

Jamie Baker (Airlines) jamie.baker@JPM.com +1 212 622 6713

Ryan Brinkman (Auto & Auto Parts) ryan.j.brinkman@JPM.com +1 212 622 6581

Rajat Gupta (Auto & Auto Parts) rajat.gupta@JPM.com +1 212 622 6382

Brian Ossenbeck (Airfreight & Surface Transportation) brian.p.ossenbeck@JPM.com +1 212 622 1023

Michael Rehaut (Homebuilders & Building Products) michael.rehaut@JPM.com +1 212 622 6696

Seth Seifman (Aerospace & Defense) seth.m.seifman@JPM.com +1 212 622 5597Tami Zakaria (Machinery, Engineering & Construction) tami.zakaria@jpmchase.com +1 212 622 9888

# EU Industrials & Auto Research Team:

David Perry (Aerospace & Defense) David.h.perry@JPM.com +44 20 7742 5606

Jose Asumendi (Auto & Auto Parts) jose.m.asumendi@JPM.com +44 20 7742 5315

Elodie Rall (Building & Construction and Infrastructure) elodie.rall@JPM.com +44 20 7134 5911

Akash Gupta (Capital Goods) Akash.z.gupta@JPM.com +44 20 7742 7978

Chitrita Sinha (Capital Goods) Chitrita.sinha@JPM.com +44 20 7742 7176

# Disclaimer:

FOR INSTITUTIONAL & PROFESSIONAL CLIENTS ONLY – Do not forward to any non-institutional clients. This material is from a Sales and Trading department and is not a product of the Research Department. It may include non-independent research (investment recommendations) which, for the purposes of MiFID 2 compliance (which term includes, where applicable, compliance with UK legislation which implements, amends or replaces Directive 2014/65/EU on MiFID 2), may also constitute a marketing communication. As such, this material has not been prepared in accordance with legal requirements designed to promote the independence of Investment Research, including but not limited to the prohibition on dealing ahead of the dissemination of Investment Research. It is not a product of JPM's Research Department. It is not a research report, investment research or independent research and is not intended as such. This message is confidential and subject to terms at www.JPM.com/emaildisclaimerand http://www.JPM.com/pages/disclosures/materialdisclaimer including on confidentiality, legal privilege, viruses and monitoring of electronic messages. If you are not the intended recipient, please delete this message and notify the sender immediately. Any unauthorized use is strictly prohibited.

For details, please refer to Section 8 – Trader Commentary of the Global Communications Policy. https://gcrm.jpmchase.net/ContentRestService/service/download/?docId={A4FF7A24-B633-40D6-B180-ECE0AB681FD6}

Access to any conference calls, meetings or events linked above will be, where relevant, subject to availability. These events are not suitable for retail clients but are intended for professional and institutional clients only. Equally, these events are not accessible to JPM corporate clients, including their management teams and investor relations contacts. Some of the events referenced above will only be available to and can only be attended by High Touch clients who have subscribed to certain JPM packages. Any research analyst meetings will be charged for in accordance with the research pricing we have agreed with you.

All materials and information shared with you are, unless otherwise indicated to you, proprietary and confidential to JPM. You are hereby notified that any disclosure, dissemination, copying, distribution, or use of the information provided to you, in whole or in part, other than as expressly permitted by JPM, is STRICTLY PROHIBITED. You are permitted to disclose the materials and information to your officers and employees on a need to know basis.

If you consider the facilitation component of any of these events to be a non-monetary benefit, please contact your normal JPM sales advisor to discuss making a payment for this service which is unbundled from any research payment. The event is intended for JPM clients only.

If you have any questions in this regard, please contact your normal JPM representative.

For further information in respect of non-research content please visit: https://www.JPM.com/pages/disclosures/materialdisclaimer.

For disclosures and disclaimers in respect of research content please visit: https://www.jpmm.com/research/disclosures.

© 2025 JPM Chase & Co. All rights reserved. JPM is a marketing name for businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide. JPM Chase Bank N.A. (member of FDIC), JPM Securities LLC (member of FINRA, NYSE and SIPC), JPM Securities plc (member of the London Stock Exchange) and authorized by the Prudential Regulation Authority (PRA) and regulated by the Financial Conduct Authority and the PRA) and JPM SE (authorized by the BaFin and regulated by the BaFin, the German Central Bank and the European Central Bank) are principal subsidiaries of JPM Chase & Co. For legal entity and regulatory disclosures, visit: www.JPM.com/disclosures. For additional regulatory disclosures, please consult: www.JPM.com/disclosures.

Joann Kim - Specialist Sales - APAC Industrials & Autos AC

Asia Pacific Specialist Sales 22 May 2026

joann.kim@JPM.com

Completed 22 May 2026 07:31 AM HKT

Disseminated 22 May 2026 07:31 AM HKT
"""
