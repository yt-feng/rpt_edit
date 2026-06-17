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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Defense | North America

# Reflections from MS's Inaugural National Security Innovation Summit

Defense is at an inflection point as the sector navigates technology diffusion, capital disruption, policy shifts, and a wave of new entrants. We recap key themes from our inaugural National Security Innovation Summit below.

## Wrapping our Inaugural MS NatSec Innovation Summit

We thank all the participants that contributed to a successful, first-ever MS National Security Innovation Summit. We hosted 30+ corporates and 150+ investors for a full-day of panels spanning capital formation, space-based defense, battlefield autonomy, missile production, dual-use technology, rare earths, and more. It's clear to us that Defense is approaching a defining moment as the sector digests harsh lessons from recent conflict, unlearns past practices that have constrained efficiency, and confronts a new outlook colored by rapid technological change (e.g., diffusion of AI / autonomy), shifting industry structures (e.g., the rise of neoprimes), and novel industrial policies. We distill key takeaways across yesterday's 10 panel discussions below. For further discussion, please don't hesitate to reach out to the MS A&D Team.

## Financing the Future: Capital Formation for Defense & Frontier Tech

- A wave of consolidation post-Cold War effectively hollowed out mid-tier Defense assets, but we are now witnessing a Peace Dividend unwind where the pendulum is swinging back.  
- Twin unlocks have fueled the rise of a new Defense middle tier: the commercialization of Defense hardware and the rise of disruptive capital willing to fund risk-tasking in a historically risk-averse sector.  
- As the defense investor base broadens beyond traditional A&D specialists, valuation frameworks increasingly resemble those used in growth sectors, creating a larger pool of capital for companies that can demonstrate category leadership and scalable production.  
- With defense budgets expanding, disruption shifts from industry displacement to technology enablement, allowing both incumbents and new entrants to grow.  
- The potential for greater specialization and deconsolidation among large platforms may enhance agility and unlock meaningful shareholder value.

## Eyes in the Sky: Space-Based Intelligence 2.0

\- Across space-based intelligence modalities, reducing latency is increasingly becoming the primary design objective as operators prioritize faster decision-

MS & CO. LLC

## Kristine T Liwag

Equity Analyst

Kristine.Liwag@morganstanley.com +1 212 761-2980

## Justin M Lang

Equity Analyst

Justin.Lang@morganstanley.com +1 212 761-6251

## Adam Jonas, CFA

Equity Analyst

Adam.Jonas@morganstanley.com +1 212 761-1726

## Stephen C Byrd

Equity Analyst

Stephen.Byrd@morganstanley.com +1 212 761-3865

## Jason T Holcomb

Research Associate

Jason.Holcomb@morganstanley.com +1 212 761-5592

## Gabrielle Knafelman

Research Associate

Gaby.Knafelman@morganstanley.com +1 212 761-4838

## Shaina C Zuber

Research Associate

Shaina.Zuber@morganstanley.com +1 212 761-6353

## DEFENSE

## North America

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

making over incremental gains in collection quality.

- In some cases, efforts outside the United States to build intelligence collection capabilities from the ground up create greater opportunities for U.S. companies, though companies selling abroad continue to face customer concerns about the U.S. government's ability to restrict or disable capabilities.  
- The limiting factor in intelligence fusion increasingly appears organizational rather than technological, suggesting future value creation may accrue to companies that simplify data access and decision workflows rather than solely improving collection hardware.

## Machines in Motion: The Future of Battlefield Autonomy

- Autonomy itself is not a new concept; what's new is the push for autonomy at scale and the diffusion of autonomy beyond exquisite systems to higher-volume, lower-cost systems.  
- Rather than replacing exquisite platforms, autonomy appears poised to expand force structure by enabling a larger quantity of affordable systems to operate alongside traditional assets, increasing overall combat mass at lower marginal cost.  
- USG reticence to mothball outdated defense programs is partly driven by a desire to preserve US jobs; it is incumbent upon new entrants to spur economic activity that empowers policymakers to make better decisions around future defense capabilities.  
- Autonomous drone technology emanating from Ukraine can now be accessed by non-state actors (e.g., cartels); the US must invest in C-UAS technology with this new reality in mind.

## Power Projection: Missiles and Hypersonic Weapon Systems

- The US is ramping hypersonic missile testing in response to adversary advancements / focus, driving US systems closer to operational deployment.  
- Less-discussed, but notable bottlenecks in the missile supply chain include memory, chemicals, high-temperature materials, and other inputs.  
- The defense ecosystem continues to grapple with the tension between customization and scale, as evolving threat environments reward adaptable systems while procurement processes remain optimized for bespoke requirements.

## Defense Manufacturing in an Era of Increased Demand

- Production capacity itself is increasingly emerging as a strategic asset, as recent conflicts have demonstrated that industrial resilience can be as important as technological superiority.  
- The next generation of defense manufacturers may derive advantage less from product innovation alone and more from compressing qualification, certification, and production timelines.  
- The Pentagon operates on one-year budget cycles with multiple CRs per year on average; political solutions are required to unlock multi-year pathways

and provide important industry visibility.

## A New Paradigm: The Pentagon's Novel Approach to Defense Procurement

- The core challenge before the DoW is how to effectively absorb / integrate fast-changing technological advances across areas like autonomy, AI, drones, and cyber.  
- As geopolitical competition intensifies, industrial capacity is becoming a national-security constraint rather than simply a manufacturing challenge, elevating the strategic importance of production assets across missiles, munitions, and shipbuilding.  
- U.S. industrial policy is evolving, with government support for strategic industries increasingly designed to align public investment with participation in the economic value created by those industries.

## Dual Use Technologies: Commercial Space and Defense Applications

- Effective strategies around dual-use tech can help diversify revenue bases and mitigate customer concentration risk.  
- Alt-PNT is an emerging area of interest to government and commercial customers alike where multiple approaches (e.g., MagNav, AI-assisted visual navigation) may be combined to offset GPS signal loss.  
- LEO-based infrastructure may also support both government and commercial needs, including astronaut training, pharma / bio research in microgravity, and advanced manufacturing (e.g., semis, fiber optics).

## Space as Warfighting Domain: Orbital Access, Defense and Space Domain Awareness

- Space Domain Awareness (SDA) is moving from tracking objects on orbit to understanding behaviors and intentions; the SDA mission is enhanced by highly mobile spacecraft that can conduct RPO missions and inspect satellites at close range.  
- As launch becomes more accessible, competitive advantage may increasingly migrate from reaching orbit to maneuvering within it.  
- Vertical integration strategies vary across Space Defense companies; some have eschewed vertical integration where supply is robust / readily available, while others have embraced vertical integration as a means of gaining greater control over schedules and costs.  
- Areas flagged for underappreciated growth over the next decade include MW / MT, on-orbit maintenance, rocket cargo, the proliferation of commercial space stations, space-based interceptors, and GEOINT.

## Critical Supply Chains: Rare Earths, Magnetics & Uranium

- Adversaries are weaponizing their supply chains and as a result are spawning new opportunities for domestic sourcing.  
- The defense industry in particular needs decoupled options for critical inputs, particularly as Chinese rare earths supply will increasingly get absorbed by internal needs.

- Public-sector funding is increasingly serving as a catalyst for private investment by absorbing early-stage execution and demand risk in strategically important supply chains.  
- Domestic uranium mining is transitioning from a long period of hibernation to a sprint; permitting, equipment lead times, and other regulations need to come up to speed.

## The AI-Enabled Battlefield: Software, Sensors & Data

- Battlefield advantage is shifting from standalone hardware platforms toward integrated hardware/software architectures as unmanned systems, sensors, and data nodes are deployed at greater scale and require a software layer to coordinate activity.  
- Fragmentation across the unmanned ecosystem may create opportunities for orchestration layers that provide interoperability, supply-chain coordination, and production visibility across otherwise disconnected vendors.  
- The lower-altitude airspace threat is growing more urgent; drone proliferation is driving C-UAS systems up the adoption curve.

## MS National Security Innovation Summit - Presenting Company List

Panels included representatives from the following companies:

• Applied Energetics  
- Axiom Space  
- BlackSky  
- Castelion  
- CesiumAstro  
- Cyclic Materials  
- Divergent  
- Firestorm Labs  
- Forterra  
• Frequency Electronics  
- Hawkeye 360  
- Ignium  
- Impulse Space  
- Karman Space & Defense  
- Leolabs  
- Lockheed Martin  
- Niron Magnetics  
- Ondas  
- Palantir Technologies  
- Redwire  
- Stratolaunch  
- Tiberius Aerospace  
- True Anomaly  
- Turion Space  
- Uranium Energy  
- Ursa Major  
- USA Rare Earth  
- Vantor  
- Voyager  
- Vulcan Elements  
- X-Bow Systems

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Kristine T Liwag.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Curtiss-Wright Corp., General Dynamics Corp., L3Harris Technologies Inc, Lockheed Martin Corp, Moog Inc., Northrop Grumman Corp.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of HawkEye 360 Inc, Lockheed Martin Corp.

Within the last 12 months, MS has received compensation for investment banking services from HawkEye 360 Inc, Lockheed Martin Corp, Northrop Grumman Corp..

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Curtiss-Wright Corp., General Dynamics Corp., HawkEye 360 Inc, L3Harris Technologies Inc, Leonardo DRS Inc, Lockheed Martin Corp, Moog Inc., Northrop Grumman Corp..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from L3Harris Technologies Inc, Leonardo DRS Inc, Lockheed Martin Corp, Northrop Grumman Corp..

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Curtiss-Wright Corp., General Dynamics Corp., HawkEye 360 Inc, L3Harris Technologies Inc, Leonardo DRS Inc, Lockheed Martin Corp, Moog Inc., Northrop Grumman Corp..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: L3Harris Technologies Inc, Leonardo DRS Inc, Lockheed Martin Corp, Northrop Grumman Corp..

MS & Co. LLC makes a market in the securities of Curtiss-Wright Corp., General Dynamics Corp., Leonardo DRS Inc, Moog Inc..

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td>

[中间内容因长度限制已省略]

s contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Defense

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/15/2026)</td></tr><tr><td colspan="3">Kristine T Liwag</td></tr><tr><td>Curtiss-Wright Corp. (CW.N)</td><td>O (08/06/2023)</td><td>$762.59</td></tr><tr><td>General Dynamics Corp. (GD.N)</td><td>O (12/16/2025)</td><td>$359.53</td></tr><tr><td>HawkEye 360 Inc (HAWK.N)</td><td>O (06/01/2026)</td><td>$25.12</td></tr><tr><td>L3Harris Technologies Inc (LHX.N)</td><td>O (12/16/2025)</td><td>$304.17</td></tr><tr><td>Leonardo DRS Inc (DRS.O)</td><td>E (05/24/2024)</td><td>$46.68</td></tr><tr><td>Lockheed Martin Corp (LMT.N)</td><td>E (12/16/2025)</td><td>$530.36</td></tr><tr><td>Moog Inc. (MOGa.N)</td><td>E (11/22/2023)</td><td>$398.03</td></tr><tr><td>Northrop Grumman Corp. (NOC.N)</td><td>O (09/07/2020)</td><td>$544.73</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
