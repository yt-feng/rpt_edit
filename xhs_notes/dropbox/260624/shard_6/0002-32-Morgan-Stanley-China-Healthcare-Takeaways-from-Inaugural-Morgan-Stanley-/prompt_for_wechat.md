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
June 23, 2026 02:22 AM GMT

China Healthcare | Asia Pacific

# Takeaways from Inaugural MS China Biopharma Symposium

We attended the inaugural MS China Biopharma Symposium in Shanghai on June 17-18, themed "Bridging Biopharma Frontiers: China and Global Innovation". The event gathered representatives from 50+ China biopharma/biotech, 20+ global pharma and 10+ PE/VC investors. Below are our takeaways.

## Key Takeaways

Global recognition of China innovation is moving beyond engineering "ADCs/bsAb/GLP-1s" to more modalities, disease areas and next-gen technologies.

Correspondingly, BD deal models are broadening from pure out-licensing to NewCo, co-co and strategic partnerships to better unlock asset value.

\- Clean IP, corporate structure and globally translatable clinical development strategies are additional factors to consider when preparing for globalization.

\- AI-driven drug discovery is shifting from platform narrative to asset generation, as vertical players integrate AI, automation, and biology.

Hengrui offers a good example of China biopharma globalization, underpinned by end-to-end development capabilities and monetized via versatile BD models.

1) China Biopharma Innovation 2.0 Beyond ADCs, Multispecific Antibodies and GLP-1 Drugs: Innovation 1.0's core advantages – engineering capability, low development cost, and execution speed – validate China's role in global drug R&D. That said, global pharma and PE/VC representatives also credit China biopharma's shift from "fast-follow" to more differentiated biology and modalities. First-in-class innovation is emerging, although still early, and still carries high biology risk that investors may not have fully appreciated. The senior PE/VC investor panel highlighted opportunities in: (1) Ultra-long dosing platforms for chronic diseases, (2) extrahepatic delivery (e.g., siRNA and saRNA), (3) oral alternatives to biologics/peptides, (4) in vivo gene editing, and (5) cell therapy – across oncology, CNS, immunology and inflammation, and other therapeutics. Geopolitical risk remains an uncertain factor to monitor. However, participants at the symposium generally hold the view that asset-level licensing appears relatively safe vs. M&A, provided corporate and IP structures are diligence-ready.

(continued in next section).

MS ASIA LIMITED+

Alexis Yan, CFA
Equity Analyst
Alexis.Yan@morganstanley.com +852 2239-7953

Jack Lin
Equity Analyst
Jack.Lin@morganstanley.com +852 3963-3746

MS & CO. LLC
Sean Laaman, Ph.D.
Equity Analyst
Sean.Laaman@morganstanley.com +1 212 761-4947

Terence C Flynn, Ph.D.
Equity Analyst
Terence.Flynn@morganstanley.com +1 212 761-2230

Clinton Ng
Equity Analyst
Clinton.Ng@morganstanley.com +852 2848-6659

![](images/db2d3f69c52a91f3ddf62524f27bffe41528ac759b6c8a83c422c3b629dfd4f9.jpg)

CHINA HEALTHCARE

Asia Pacific
Industry View Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

2) Structuring Win-win Partnerships: The broadening of BD deal models is discussed in multiple panels. Traditional out-licensing remains the predominant model, particularly suited for clinical-stage assets with better-understood development strategies. Meanwhile, NewCo, co-co and strategic collaborations are rising as global pharma gradually builds confidence in China's discovery platforms to source earlier-stage assets. Speed, responsiveness and process discipline are critical in deal negotiations, alongside regular partner engagement and a professional BD strategy. Monetary terms aside, global biopharma buyers focus on intrinsic asset value, strategic fit and risk-adjusted milestones, while China biopharma/biotech sellers also increasingly weigh strategic fit and partner commitment alongside headline financial terms. Common "deal-breakers" cited by global pharma include weak scientific rationale, immature data, IP risk, poor global translatability, CMC uncertainty and complex cross-border structures. For China companies, the best preparation is to design clinical studies with BD prospect in mind: elect to use high-standard control arms, ensure data can migrate into US or global regulatory packages, include diverse patient representation where possible and keep IP ownership simple and diligence-ready.

3) AI-Driven Drug Discovery in China: AI-driven drug discovery in China is shifting from platform narrative to clinical-ready asset generation, supported by a combination of foundation models, robotic labs, and AI-enabled antibody design. The strongest and more mature value proposition is compressing the path from hit identification to lead generation and optimization (e.g., an AIDD player shortened the process to \~9 months). China benefits from its large engineering talent pool, efficient CRO infrastructure and rapid wet-lab execution, complementing the AIDD to close up the drug discovery loop. Key bottlenecks in AIDD include proprietary data access (including failed datasets) and biology knowledge. AIDD companies that can integrate AI, automation, translational biology, and credible internal assets into clear monetization models are likely to enjoy a higher competitive moat, while pure model companies without asset validation may face increasing competition.

4) Hengrui as a Key Globalization Case Study: As the largest biopharma company in China, Hengrui's senior management presented its globalization path, offering a lens into how a leading China pharma could leverage domestic development and commercial strength to quickly expand global presence via versatile deal models, unlocking asset and platform potential. In particular, Hengrui's first NewCo, "Kailera", for the GLP-1 franchise (note) – one of the largest NewCo transactions led by a Chinese pharma – raised two rounds of private financing followed by NASDAQ IPO in 18 months. Hengrui retains long-term equity upside in addition to typical milestone/royalty payments. In addition, Hengrui has secured two broad strategic collaborators with GSK (note) and Bristol Myers Squibb (note), for a package of early Phase I, pre-IND and discovery-stage assets. The co-co arrangement can leverage each party's expertise to address target-, development- or commercialization-related bottlenecks, speeding up time to clinic.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Terence C Flynn, Ph.D.; Sean Laaman, Ph.D.; Jack Lin; Clinton Ng; Alexis Yan, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Alibaba Health Information Technology, APT Medical Inc, Asymchem Laboratories. Inc, DaShenLin Pharmaceutical, Dian Diagnostics Group Co Ltd, Hangzhou Tigermed Consulting, InnoCare Pharma Ltd, Jiangsu Hengrui, Keymed Biosciences Inc., Pharmaron, Shandong Weigao, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, Yifeng Pharmacy Chain Co Ltd, Yixintang Pharmaceutical.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of 3SBio, Akeso, Inc., Duality Biotherapeutics Inc, Everest Medicines Ltd, Hansoh Pharmaceutical Group Co Ltd, Innovent Biologics Inc, Insilico Medicine, Jiangsu Hengrui, Medtide, Nanjing Leads Biolabs Co Ltd, Shenzhen Edge Medical, Simcere Pharmaceutical Group, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, WuXi XDC Cayman Inc..

Within the last 12 months, MS has received compensation for investment banking services from 3SBio, Akeso, Inc., Everest Medicines Ltd, Hansoh Pharmaceutical Group Co Ltd, Innovent Biologics Inc, Insilico Medicine, Medtide, Shenzhen Edge Medical, Simcere Pharmaceutical Group, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, WuXi XDC Cayman Inc..

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from 3SBio, Abbisko Cayman Ltd, Adicon Holdings Ltd, Aier Eye Hospital Group, Akeso, Inc., Alibaba Health Information Technology, Angelalign Technology Inc, Beauty Farm Medical and Health Industry, China Medical System, CSPC Pharmaceutical Group, Duality Biotherapeutics Inc, Everest Medicines Ltd, Fosun Pharmaceutical, Fu Shou Yuan International Group Ltd, Genscript Biotech Corporation, Hansoh Pharmaceutical Group Co Ltd, HUTCHMED (China) Ltd, Hygeia Healthcare Holdings Co., Ltd., InnoCare Pharma Ltd, Innovent Biologics Inc, Insilico Medicine, Jiangsu Hengrui, Jinxin Fertility Group Ltd, Keymed Biosciences Inc., Medtide, MicroPort Scientific Corp., Mindray Bio-Medical, Nanjing Leads Biolabs Co Ltd, Peijia Medical Ltd, Ping An Healthcare and Technology, Shenzhen Edge Medical, Simcere Pharmaceutical Group, Sino Biopharmaceutical, Sinopharm Group, VISEN Pharmaceuticals, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, WuXi XDC Cayman Inc., Yifeng Pharmacy Chain Co Ltd, Yunnan Baiyao Group, Zhejiang Huahai Pharmaceutical Co. Ltd., Zylox-Tonbridge Medical Technology Co..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from 3SBio, Adicon Holdings Ltd, Angelalign Technology Inc, Hygeia Healthcare Holdings Co., Ltd., Simcere Pharmaceutical Group, Sino Biopharmaceutical, The United Laboratories, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, WuXi XDC Cayman Inc..

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: 3SBio, Abbisko Cayman Ltd, Adicon Holdings Ltd, Aier Eye Hospital Group, Akeso, Inc., Alibaba Health Information Technology, Angelalign Technology Inc, Beauty Farm Medical and Health Industry, China Medical System, CSPC Pharmaceutical Group, Duality Biotherapeutics Inc, Everest Medicines Ltd, Fosun Pharmaceutical, Fu Shou Yuan International Group Ltd, Genscript Biotech Corporation, Hansoh Pharmaceutical Group Co Ltd, HUTCHMED (China) Ltd, Hygeia Healthcare Holdings Co., Ltd., InnoCare Pharma Ltd, Innovent Biologics Inc, Insilico Medicine, Jiangsu Hengrui, Jinxin Fertility Group Ltd, Keymed Biosciences Inc., Medtide, MicroPort Scientific Corp., Mindray Bio-Medical, Nanjing Leads Biolabs Co Ltd, Peijia Medical Ltd, Ping An Healthcare and Technology, Shenzhen Edge Medical, Simcere Pharmaceutical Group, Sino Biopharmaceutical, Sinopharm Group, VISEN Pharmaceuticals, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, WuXi XDC Cayman Inc., Yifeng Pharmacy Chain Co Ltd, Yunnan Baiyao Group, Zhejiang Huahai Pharmaceutical Co. Ltd., Zylox-Tonbridge Medical Technology Co..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: 3SBio, Abbisko Cayman Ltd, Adicon Holdings Ltd, Akeso, Inc., Angelalign Technology Inc, Duality Biotherapeutics Inc, HUTCHMED (China) Ltd, Hygeia Healthcare Holdings Co., Ltd., Innovent Biologics Inc, Insilico Medicine, Jinxin Fertility Group Ltd, Keymed Biosciences Inc., Medtide, Nanjing Leads Biolabs Co Ltd, Peijia Medical Ltd, RemeGen Co., Ltd., Simcere Pharmaceutical Group, Sino Biopharmaceutical, The United Laboratories, VISEN Pharmaceuticals, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, WuXi XDC Cayman Inc., Zylox-Tonbridge Medical Technology Co..

MS & Co. LLC makes a market in the securities of Zai Lab Ltd.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.
Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

## (as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overw

[中间内容因长度限制已省略]

</td><td>O (05/28/2020)</td><td>HK$82.95</td></tr><tr><td>Duality Biotherapeutics Inc (9606.HK)</td><td>O (05/22/2025)</td><td>HK$178.40</td></tr><tr><td>Everest Medicines Ltd (1952.HK)</td><td>E (03/15/2024)</td><td>HK$25.50</td></tr><tr><td>HUTCHMED (China) Ltd (0013.HK)</td><td>E (05/29/2026)</td><td>HK$15.85</td></tr><tr><td>HUTCHMED (China) Ltd (HCM.O)</td><td>E (05/29/2026)</td><td>US$9.99</td></tr><tr><td>InnoCare Pharma Ltd (9969.HK)</td><td>O (05/29/2026)</td><td>HK$10.69</td></tr><tr><td>Innovent Biologics Inc (1801.HK)</td><td>O (03/03/2026)</td><td>HK$75.35</td></tr><tr><td>Insilico Medicine (3696.HK)</td><td>O (02/03/2026)</td><td>HK$40.02</td></tr><tr><td>Keymed Biosciences Inc. (2162.HK)</td><td>O (08/10/2021)</td><td>HK$56.70</td></tr><tr><td>Nanjing Leads Biolabs Co Ltd (9887.HK)</td><td>E (09/02/2025)</td><td>HK$52.55</td></tr><tr><td>RemeGen Co., Ltd. (9995.HK)</td><td>E (05/08/2024)</td><td>HK$66.75</td></tr><tr><td>VISEN Pharmaceuticals (2561.HK)</td><td>O (04/29/2025)</td><td>HK$19.26</td></tr><tr><td>Zai Lab Ltd (ZLAB.O)</td><td>O (12/14/2023)</td><td>US$18.48</td></tr><tr><td>Zai Lab Ltd (9688.HK)</td><td>O (12/14/2023)</td><td>HK$13.93</td></tr><tr><td colspan="3">Laurence Tam</td></tr><tr><td>Acrobiosystems Co Ltd (301080.SZ)</td><td>O (09/11/2025)</td><td>Rmb40.13</td></tr><tr><td>Apeloa Pharmaceutical Co Ltd (000739.SZ)</td><td>O (02/28/2025)</td><td>Rmb16.37</td></tr><tr><td>Asymchem Laboratories. Inc (002821.SZ)</td><td>E (08/01/2025)</td><td>Rmb125.81</td></tr><tr><td>Asymchem Laboratories. Inc (6821.HK)</td><td>E (06/06/2023)</td><td>HK$97.30</td></tr><tr><td>Beijing Tongrentang (600085.SS)</td><td>U (11/03/2014)</td><td>Rmb23.55</td></tr><tr><td>Beijing Tongrentang Chinese Medicine (3613.HK)</td><td>O (01/14/2015)</td><td>HK$6.53</td></tr><tr><td>China National Accord Medicines Corp Ltd (000028.SZ)</td><td>U (07/25/2022)</td><td>Rmb22.55</td></tr><tr><td>China Resources Pharmaceutical Group Ltd (3320.HK)</td><td>O (06/16/2022)</td><td>HK$4.49</td></tr><tr><td>China Resources Sanjiu Medical &amp; Pharma (000999.SZ)</td><td>O (08/30/2019)</td><td>Rmb23.50</td></tr><tr><td>China Traditional Chinese Medicine (0570.HK)</td><td>U (01/17/2025)</td><td>HK$1.42</td></tr><tr><td>DaShenLin Pharmaceutical (603233.SS)</td><td>O (07/25/2022)</td><td>Rmb15.87</td></tr><tr><td>Dong E E Jiao Co. (000423.SZ)</td><td>O (05/16/2024)</td><td>Rmb45.30</td></tr><tr><td>Fu Shou Yuan International Group Ltd (1448.HK)</td><td>E (03/19/2025)</td><td>HK$2.64</td></tr><tr><td>Genscript Biotech Corporation (1548.HK)</td><td>O (08/14/2024)</td><td>HK$11.04</td></tr><tr><td>Hangzhou Tigermed Consulting (300347.SZ)</td><td>O (08/01/2025)</td><td>Rmb41.20</td></tr><tr><td>Jiangzhong Pharmaceutical Co. Ltd. (600750.SS)</td><td>O (02/08/2024)</td><td>Rmb23.35</td></tr><tr><td>Joinn Laboratories China Co Ltd (603127.SS)</td><td>E (06/06/2023)</td><td>Rmb36.67</td></tr><tr><td>Joinn Laboratories China Co Ltd (6127.HK)</td><td>E (02/26/2024)</td><td>HK$16.82</td></tr><tr><td>Jointown Pharmaceutical Group (600998.SS)</td><td>U (07/26/2021)</td><td>Rmb4.79</td></tr><tr><td>LBX Pharmacy Chain (603883.SS)</td><td>O (03/14/2022)</td><td>Rmb11.74</td></tr><tr><td>Medtide (3880.HK)</td><td>E (08/06/2025)</td><td>HK$22.92</td></tr><tr><td>Nanjing King-friend Biochemical (603707.SS)</td><td>O (02/28/2025)</td><td>Rmb7.08</td></tr><tr><td>Pharmaron (3759.HK)</td><td>O (09/25/2024)</td><td>HK$15.25</td></tr><tr><td>Pharmaron (300759.SZ)</td><td>E (09/25/2024)</td><td>Rmb23.67</td></tr><tr><td>Shandong Xinhua Pharmaceutical Co Ltd (000756.SZ)</td><td>U (02/28/2025)</td><td>Rmb12.22</td></tr><tr><td>Shanghai Pharmaceutical (601607.SS)</td><td>E (08/17/2021)</td><td>Rmb15.96</td></tr><tr><td>Shanghai Pharmaceutical (2607.HK)</td><td>O (08/17/2021)</td><td>HK$11.84</td></tr><tr><td>Shenzhen Hepalink Pharmaceutical (002399.SZ)</td><td>U (06/16/2023)</td><td>Rmb8.88</td></tr><tr><td>Sinopharm Group (1099.HK)</td><td>O (02/10/2023)</td><td>HK$16.31</td></tr><tr><td>Tasly Pharmaceutical Group Co. Ltd (600535.SS)</td><td>E (07/19/2024)</td><td>Rmb13.69</td></tr><tr><td>The United Laboratories (3933.HK)</td><td>E (06/13/2017)</td><td>HK$8.06</td></tr><tr><td>Tofflon Science &amp; Technology Group (300171.SZ)</td><td>E (09/11/2025)</td><td>Rmb11.31</td></tr><tr><td>WuXi AppTec Co Ltd (603259.SS)</td><td>O (01/17/2019)</td><td>Rmb106.83</td></tr><tr><td>WuXi AppTec Co Ltd (2359.HK)</td><td>O (01/17/2019)</td><td>HK$132.80</td></tr><tr><td>WuXi Biologics Cayman Inc (2269.HK)</td><td>O (07/17/2017)</td><td>HK$30.74</td></tr><tr><td>WuXi XDC Cayman Inc. (2268.HK)</td><td>O (12/22/2023)</td><td>HK$48.16</td></tr><tr><td>Yantai Dongcheng Biochemicals Co Ltd (002675.SZ)</td><td>E (02/28/2025)</td><td>Rmb12.56</td></tr><tr><td>Yifeng Pharmacy Chain Co Ltd (603939.SS)</td><td>O (07/25/2022)</td><td>Rmb19.75</td></tr><tr><td>Yixintang Pharmaceutical (002727.SZ)</td><td>E (07/25/2022)</td><td>Rmb10.62</td></tr><tr><td>Yunnan Baiyao Group (000538.SZ)</td><td>O (10/11/2021)</td><td>Rmb48.66</td></tr><tr><td>Zhangzhou Pientzehuang Pharmaceutical (600436.SS)</td><td>U (01/21/2022)</td><td>Rmb114.29</td></tr><tr><td>Zhejiang Hisun Pharmaceutical Co. Ltd. (600267.SS)</td><td>U (06/01/2023)</td><td>Rmb9.69</td></tr><tr><td>Zhejiang Huahai Pharmaceutical Co. Ltd. (600521.SS)</td><td>O (06/01/2023)</td><td>Rmb14.29</td></tr><tr><td>Zhejiang Jiuzhou Pharmaceutical Co Ltd (603456.SS)</td><td>E (02/28/2025)</td><td>Rmb12.91</td></tr><tr><td>Zhejiang Medicine Co. Ltd. (600216.SS)</td><td>E (02/28/2025)</td><td>Rmb11.71</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.
"""
