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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

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
# Investor Feedback on Sodium-Ion Batteries

Investor discussions regarding sodium-ion batteries have centered on three key areas: 1) supply chain validation and scalability, 2) suitability for AIDC applications vs. Lithium Iron Phosphate (LFP) batteries, and 3) the new breed's competitive landscape.

## Key Takeaways

On Monday in Munich, Germany, CATL unveiled TENER Sodium ESS – the world's first field-validated sodium-ion battery energy storage system.

CATL is targeting TENER Sodium shipments of 1GWh by end-2026, with global deliveries scheduled to commence in June 2027.

>10GWh of material supply has been secured now; further supply chain expansion is on the way

\- Superior rate capability vs. LFP makes batteries particularly well suited for AIDC storage, apart from cheaper cost and cold performance.

Sodium-ion chemistry sets higher technical barriers to entry given extensive material science innovations, resulting in concentrated supply structure.

Sodium-ion batteries are better positioned than LFP in AIDC storage: Sodium-ion batteries appear particularly well suited to AIDC applications in view of their superior rate capability relative to conventional LFP batteries. Though energy density remains somewhat lower, sodium-ion chemistry generally exhibits faster ion transport kinetics, lower polarization under high-current operation, and better power retention at low temperatures. These characteristics enable stronger charge/discharge performance during frequent acceleration, braking and power-demand fluctuations, which are often seen in AIDCs.

Thus, sodium-ion batteries are especially valuable for AIDC use cases, which require rapid response, high peak power output, and repeated cycling. As a result, we believe they could offer a more compelling balance of performance, durability, and cost than LFP in AIDC applications, making them a natural early-adoption segment for sodium-ion commercialization.

See the following section – Key Themes (cont'd)

MS ASIA LIMITED+
Jack Lu
Equity Analyst
Jack.Lu@morganstanley.com +852 2848-5044

MS ASIA (SINGAPORE) PTE.+

Mayank Maheshwari
Equity Analyst
Mayank.Maheshwari@morganstanley.com

+65 6834-6719

MS EUROPE S.E., MADRID BRANCH+
Javier Martinez de Olcoz Cerdan
Equity Analyst
Javier.Martinez.Olcoz@morganstanley.com

+34 9141-81289

MS & CO. INTERNATIONAL PLC+
Amy Gower (Amy Sergeant), CFA
Commodities Strategist
Amy.Gower1@morganstanley.com +44 20 7677-6937

MS ASIA LIMITED+

Tim Hsiao
Equity Analyst
Tim.Hsiao@morganstanley.com +852 2848-1982

MS & CO. LLC

Andrew S Percoco
Equity Analyst
Andrew.Percoco@morganstanley.com

+1 212 296-4322

MS & CO. INTERNATIONAL PLC, SEOUL BRANCH+

Young Suk Shin
Equity Analyst
Young.Shin@morganstanley.com

+82 2 399-4994

MS ASIA LIMITED+

Kaylee Xu
Equity Analyst
Kaylee.Xu@morganstanley.com +852 2239-1506

![](images/412a37a85b4a8015c946273cbf8cfe0fa3667d4bee2ec13e36b7baad1ce5803c.jpg)

## CHINA ENERGY & CHEMICALS

Asia Pacific
Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Key Themes (cont'd)

Further progress, a new milestone: CATL officially launched the TENER Sodium ESS on Monday this week (the same day we published our Global Insight report on sodium-ion batteries), marking an important milestone in the commercialization of sodium-ion batteries. It is the world's first field-validated sodium-ion energy storage system, indicating that the technology, manufacturing capability, and supply chain have reached commercial readiness. Management targets cumulative shipments of 1GWh by end-2026, with initial deliveries in China scheduled to begin in September 2026 and global deliveries commencing in June 2027.

We view this announcement as a meaningful validation of sodium-ion technology. It moves the industry beyond laboratory demonstrations and pilot projects toward GWh-scale deployment. More importantly, CATL's willingness to commit to commercial volume targets suggests increasing confidence in supply-chain maturity and cost competitiveness. In our view, the TENER Sodium launch could represent a key inflection point for broader sodium-ion adoption in ESS.

Supply chain validation: While sodium-ion batteries benefit from abundant raw materials and significant overlap with existing lithium-ion manufacturing processes, investors are looking for evidence that the entire value chain – from cathode materials and hard carbon anodes to cell manufacturing and system integration – can achieve commercial-scale production with consistent quality and costs.

CATL's recent launch of the TENER Sodium ESS also provided an important validation of supply-chain readiness. Management disclosed that the company has already secured tens of thousands of tonnes of sodium-ion cathode and anode material supply, which is sufficient to support more than 10GWh of sodium-ion battery production, according to our calculation.

We expect CATL to continue expanding its materials ecosystem and supplier base, particularly given its stated target to build 40GWh of sodium-ion manufacturing capacity by the end of this year. In our view, the ability to secure upstream materials at scale may become a key competitive differentiator, further reinforcing the advantages of early movers with integrated R&D, supplier relationships, and manufacturing scale.

Higher barriers to entry in the new breed: We believe sodium-ion batteries carry higher technical barriers to entry than LFP, stemming from the extensive material science innovations required across cathode chemistry, hard-carbon anodes or anode-free solutions, electrolyte formulation, and cell architecture. Unlike LFP, whose supply chain has become largely mature and commoditized after a decade of industry scaling, sodium-ion remains in an earlier stage where performance differentiation depends heavily on proprietary materials and manufacturing know-how. This has resulted in a more concentrated industry structure, with CATL and a small number of leading players holding meaningful technology, capacity, and supply-chain advantages. As commercialization accelerates, we expect the sodium-ion market to remain more consolidated than the LFP market, supporting stronger pricing power for incumbents, with higher barriers to entry for newcomers.

## Key technical challenges in producing high-quality sodium-ion batteries include:

Cathode material optimization: Sodium-ion cathodes suffer from greater structural instability than LFP, requiring sophisticated materials engineering, surface coating, and elemental doping to simultaneously improve energy density, cycle life and safety. Different pathways (layered oxides, Prussian Blue, polyanion systems) each present unique trade-offs.

Anode development: Unlike lithium batteries, which typically use mature graphite anodes, sodium-ion batteries rely predominantly on hard carbon. Achieving high initial Coulombic efficiency, low irreversible capacity loss, and consistent pore structure remains a major technical hurdle and manufacturing challenge.

Importantly, CATL has also developed an anode-free sodium-ion battery architecture for EV applications, which significantly improves energy density and narrows the gap versus LFP. Management has indicated that next-generation sodium-ion batteries are approaching high-end LFP-level energy density, potentially removing one of the last major obstacles to broader adoption in passenger vehicles. The achievement is technologically significant because anode-free designs require sophisticated control of sodium plating/stripping behavior, electrolyte stability, interface engineering and cycle-life management.

In our view, this further reinforces the notion that sodium-ion batteries are not merely a lower-cost alternative chemistry, but a technology platform requiring deep materials-science expertise and substantial R&D investment. Such capabilities are concentrated among a small number of industry leaders, potentially resulting in a more consolidated market structure than the commoditized LFP industry.

Electrolyte and SEI engineering: Sodium-ion batteries require highly customized electrolyte formulations to stabilize the solid-electrolyte interphase (SEI), improve cycle life and support wide-temperature operation. This remains a key area of proprietary differentiation among leading players.

Low-temperature and high-rate performance balancing. While sodium-ion batteries naturally exhibit strong low-temperature and high-rate characteristics, achieving these advantages without sacrificing cycle life, energy density and safety requires substantial cell-level optimization.

Manufacturing yield and consistency: Although sodium-ion production can leverage much of the lithium-ion manufacturing infrastructure, achieving automotive- and utility-grade consistency requires extensive process tuning. Yield management and cell consistency are especially important given the relatively immature state of the supply chain.

System integration and commercialization validation: Utility-scale deployments require validation of long-duration performance, thermal stability, safety and degradation characteristics. CATL's recent launch of the TENER Sodium ESS highlights the importance of proving readiness not only at the cell level, but across manufacturing, supply chain and system integration.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Tim Hsiao; Jack Lu; Mayank Maheshwari; Javier Martinez de Olcoz Cerdan; Andrew S Percoco; Young Suk Shin; Kaylee Xu.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: China Oilfield Services Ltd., Contemporary Amperex Technology Co. Ltd., EVE Energy Co Ltd, PetroChina, Shandong Sinocera Functional Material, Shenzhen Senior Technology Material Co, Sunresin New Materials Co Ltd.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Bluestar Adisseo Co, Contemporary Amperex Technology Co. Ltd.. Within the last 12 months, MS has received compensation for investment banking services from Bluestar Adisseo Co, Contemporary Amperex Technology Co. Ltd..

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Bluestar Adisseo Co, China Petroleum & Chemical Corp., Contemporary Amperex Technology Co. Ltd., EVE Energy Co Ltd, Hengli Petrochemical Co Ltd, Ningbo Ronbay New Energy Technology, REPT Battero Energy Co, Rongsheng Petrochemical Co Ltd, Shanghai Putailai New Energy Tech Co Ltd, Shenzhen Senior Technology Material Co, Wanhua Chemical, Yunnan Energy New Material Co Ltd, Zhejiang NHU Co. Ltd..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from China Petroleum & Chemical Corp., CNOOC, PetroChina, Wanhua Chemical.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Bluestar Adisseo Co, China Petroleum & Chemical Corp., Contemporary Amperex Technology Co. Ltd., EVE Energy Co Ltd, Hengli Petrochemical Co Ltd, Ningbo Ronbay New Energy Technology, REPT Battero Energy Co, Rongsheng Petrochemical Co Ltd, Shanghai Putailai New Energy Tech Co Ltd, Shenzhen Senior Technology Material Co, Wanhua Chemical, Yunnan Energy New Material Co Ltd, Zhejiang NHU Co. Ltd..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: China Petroleum & Chemical Corp., CNOOC, PetroChina, Wanhua Chemical.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend 

[中间内容因长度限制已省略]

or Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Energy & Chemicals

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/25/2026)</td></tr><tr><td colspan="3">Jack Lu</td></tr><tr><td>Bluestar Adisseo Co (600299.SS)</td><td></td><td>Rmb9.04</td></tr><tr><td>China Oilfield Services Ltd. (2883.HK)</td><td>E (03/28/2026)</td><td>HK$6.43</td></tr><tr><td>China Oilfield Services Ltd. (601808.SS)</td><td>U (03/28/2026)</td><td>Rmb11.09</td></tr><tr><td>China Petroleum &amp; Chemical Corp. (600028.SS)</td><td>E (08/19/2024)</td><td>Rmb4.55</td></tr><tr><td>China Petroleum &amp; Chemical Corp. (0386.HK)</td><td>O (07/29/2025)</td><td>HK$4.10</td></tr><tr><td>CNOOC (0883.HK)</td><td>O (03/17/2021)</td><td>HK$21.22</td></tr><tr><td>Contemporary Amperex Technology Co. Ltd. (300750.SZ)</td><td>O (06/25/2025)</td><td>Rmb401.90</td></tr><tr><td>Contemporary Amperex Technology Co. Ltd. (3750.HK)</td><td>O (05/04/2026)</td><td>HK$716.50</td></tr><tr><td>EVE Energy Co Ltd (300014.SZ)</td><td>E (05/31/2022)</td><td>Rmb66.81</td></tr><tr><td>Gotion High Tech Co Ltd (002074.SZ)</td><td>E (04/17/2023)</td><td>Rmb28.66</td></tr><tr><td>Guangzhou Tinci Materials Technology Co (002709.SZ)</td><td>E (01/08/2026)</td><td>Rmb55.20</td></tr><tr><td>Hengli Petrochemical Co Ltd (600346.SS)</td><td>++</td><td>Rmb18.21</td></tr><tr><td>Ningbo Ronbay New Energy Technology (688005.SS)</td><td>U (10/27/2025)</td><td>Rmb32.80</td></tr><tr><td>Ningxia Baofeng Energy Group Co., Ltd. (600989.SS)</td><td>E (04/15/2026)</td><td>Rmb21.17</td></tr><tr><td>PetroChina (601857.SS)</td><td>O (08/19/2024)</td><td>Rmb9.06</td></tr><tr><td>PetroChina (0857.HK)</td><td>O (03/17/2021)</td><td>HK$8.73</td></tr><tr><td>REPT Battero Energy Co (0666.HK)</td><td>E (10/20/2025)</td><td>HK$13.34</td></tr><tr><td>Rongsheng Petrochemical Co Ltd (002493.SZ)</td><td>E (07/29/2025)</td><td>Rmb11.71</td></tr><tr><td>Shanghai Putailai New Energy Tech Co Ltd (603659.SS)</td><td>U (10/27/2025)</td><td>Rmb28.55</td></tr><tr><td>Shenzhen Senior Technology Material Co (300568.SZ)</td><td>E (01/08/2026)</td><td>Rmb17.82</td></tr><tr><td>Yunnan Energy New Material Co Ltd (002812.SZ)</td><td>O (10/27/2025)</td><td>Rmb68.27</td></tr><tr><td colspan="3">Kaylee Xu</td></tr><tr><td>Jiangsu Cnano Technology Co Ltd (688116.SS)</td><td>U (03/10/2025)</td><td>Rmb40.10</td></tr><tr><td>Jiangsu Yangnong Chemical (600486.SS)</td><td>O (06/12/2026)</td><td>Rmb53.80</td></tr><tr><td>Shandong Sinocera Functional Material (300285.SZ)</td><td>E (03/23/2026)</td><td>Rmb98.40</td></tr><tr><td>Shenzhen Capchem Technology Co Ltd (300037.SZ)</td><td>E (06/07/2023)</td><td>Rmb90.29</td></tr><tr><td>Sunresin New Materials Co Ltd (300487.SZ)</td><td>E (10/25/2024)</td><td>Rmb60.15</td></tr><tr><td>Wanhua Chemical (600309.SS)</td><td>O (04/10/2026)</td><td>Rmb73.61</td></tr><tr><td>Zhejiang NHU Co. Ltd. (002001.SZ)</td><td>E (01/26/2026)</td><td>Rmb30.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
