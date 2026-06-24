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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# GS China Econ Proprietary Indicators: June

Please find an update on our proprietary economic indicators below. The data behind our proprietary economic indicators can be downloaded here (methodology notes available in the appendix).

Chelsea Song +852-2978-0106 | chelsea.song@gs.com GS (Asia) L.L.C.

## GS Proprietary Economic Indicators

Exhibit 1: Our China Current Activity Indicator (CAI) edged up to +4.6% mom annualized sa in May, vs. +2.9% in April

![](images/1bf2b5e243cca980e781bd323ba989209a087e02753244d8d23af46902a06bba.jpg)  
Source: GS Global Investment Research, NBS, CEIC

Note: Others include the housing sector and labor markets.

Exhibit 2: May's improvement in CAI was mainly led by manufacturing sectors  
![](images/8892e364b98e8b2c3d94432d40512403b354eb57682901354a3a4bae10877815.jpg)  
Source: GS Global Investment Research, NBS, CEIC  
Exhibit 3: Our proprietary import-implied domestic demand proxy suggests weak domestic demand growth in Q2

![](images/6c93aaff7280b2a929b874d1055a6b20bae4ec21588d3fee052b2d2b338a06f9.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 4: Our MAP surprise index (21-day moving average) shows recent macro data have come in below market expectations  
![](images/6663b23f215563cda36a3f54e867b3cd38f51f9930e0b55cc278291db0908b99.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 5: Our manufacturing growth proxy and construction growth proxy both ticked up in May  
![](images/0639c1cad569f3900d2d0d08cffecefe7f0c632b9a5d1c8a9cff3db8c2352698.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 6: Our preliminary investment tracker (on a real value-added basis) points to slightly weaker growth in Q2  
![](images/27924c2073302bb932ad28b4f42e2aa4797169a8d9f292fd5b5ef612f06605db.jpg)  
Source: GS Global Investment Research

Exhibit 7: Our China inventory tracker suggests inventory levels may stay roughly flat in Q2 2026  
![](images/08ae1af7697f76c46f2393605b6b61bb0e0713883ccc9a4fbe14723f7925d2cf.jpg)  
Source: GS Global Investment Research, Haver Analytics

Exhibit 8: The boost from inventory changes to sequential GDP growth is likely to decline in Q2 2026  
![](images/eb39f2d33c394993143e778c517ef45ba6e9372ce193d6b2eb6589a666080114.jpg)  
Source: GS Global Investment Research, Haver Analytics, CEIC, Bloomberg  
Exhibit 9: Our China outside-in export tracker outperformed the official export growth data in April

![](images/3cd411531382eed1c0c2e4615e1fa157082d6d7601f922f105280d0abe4fdbb1.jpg)  
Note: April 2026 data print is estimated using countries with imports data available, which account for $31.1\%$ of value of Chinese exports in 2025.  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 10: Our China outside-in import tracker underperformed the official import growth data in April  
![](images/5324b51746e9e81435254ef30fd95189eaa731e1bf4f3cc2b254eca53ed38d9c.jpg)  
Note: April 2026 data print is estimated using countries with exports data available, which account for 65.5% of value of Chinese imports in 2025.  
Source: Haver Analytics, CEIC, GS Global Investment Research  
Exhibit 11: China Financial Conditions Index (FCI; including credit quantities) tightened slightly in May

![](images/ad06d5d0d98596b4b100b773a379519446eed32df48093bc421f6dc82584b505.jpg)  
Source: GS Global Investment Research, CEIC, Bloomberg

Exhibit 12: May's slight tightening in FCI was driven by FX appreciation against the trade-weighted basket and weaker equity performance  
![](images/563aa46db6c46cc62e772d47bc3bca9558dc993aecf6c4ed5d4729e7e63d66d8.jpg)  
Source: GS Global Investment Research, CEIC, Bloomberg

Exhibit 13: We estimate credit impulse may stay negative in H2 due to weak credit growth  
![](images/8baf64a1ae91630669ec05ba03582d5d70b732be16c817bdbb8128233f9d91bd.jpg)  
The impulses assume that credit stays flat through the remainder of this year.  
Source: GS Global Investment Research

Exhibit 14: Our preferred gauge suggests increased FX inflows in May  
![](images/23c5de8c5fe28071d78cbb479ed306e287bf2e10bb0cbf2b0a0ef12e44d8f65f.jpg)  
Source: GS Global Investment Research, SAFE

Exhibit 15: Our China domestic macro policy proxy tightened slightly in May  
![](images/3439b762d141937420720ecae14f4f6f81be8a1a44b92fa47cfdf5f09ba1fe39.jpg)  
Source: GS Global Investment Research, Wind, Haver Analytics, CEIC

Exhibit 16: May's tightening in GS China macro policy proxy was driven by tighter fiscal policy and slower credit growth  
![](images/920de852ca1578098b192ebd7fe7b3ea1863e18d4a2661c856cbd293e9ed6cc1.jpg)  
Source: GS Global Investment Research, Wind, Haver Analytics, CEIC

Exhibit 17: Our augmented fiscal deficit (AFD) metric narrowed further in May  
![](images/cbc7173476b75390144fe132a119caa0f9f3014fada5fa7676dc5b80ffcb09d0.jpg)  
Source: GS Global Investment Research, CEIC, Wind

Exhibit 18: China's fiscal "spend-through" ratio rose slightly in May  
![](images/47e23925e343d9c8be97e9ab07156ad8609670fe6cfb427fa35a2d79c97f0bec.jpg)  
Shaded areas refer to periods when China's year-to-date real GDP growth was equal to or below the full-year growth target. Note that the Chinese government did not set a national growth target for 2020.  
Source: MOF, Wind, CEIC, GS Global Investment Research

Exhibit 19: Government bond net issuance is set to accelerate in the coming months  
![](images/e832e1d89f2078c4208888ebc1453b5bb3ba23e06163c524b17ae82d1d47a2bf.jpg)  
Local government refinancing bond issuance for debt resolution is not included.  
Source: Wind, CEIC, GS Global Investment Research

Exhibit 20: Our city-level property relative tightness index suggests continued housing easing  
![](images/937caa56ffcfb26c42fcb999643d2ba13bf56bc89342ddac49d2695acc962251.jpg)  
Source: GS Global Investment Research, local governments, Sofang.com

## Methodology notes for GS proprietary economic indicators

1. Exhibit 1 and Exhibit 2: China Current Activity Indicator (Bloomberg ticker: GSCNCAI) is the “first principal component” of several real activity indicators including industrial production, electricity consumption, PMIs, etc., expressed in GDP-equivalent units. (See the latest GS CAI methodology note here and the revamped methodology for China CAI here.) These indicators can be recategorized to measure sequential momentum in different areas of the economy — manufacturing, consumption and others (i.e., housing and the labor markets).

2. Exhibit 3: Our import-implied real domestic demand infers China's domestic demand by assigning all Chinese imports by sector to an ultimate source of final demand using China's input-output tables. (See a brief summary of the methodology here.) The real domestic demand implied by national accounts is estimated from national accounts data (GDP – (Exports – Imports)), as a cross-check for the validity of the sectoral imports based domestic demand.

3. Exhibit 4: Our China MAP surprise index summarizes the importance and strength (relative to consensus expectations) of economic indicators for the country. Aggregating MAP over time allows us to examine whether economic data are outperforming or underperforming consensus expectations for a certain period.

4. Exhibit 5: Our construction growth proxy is the median year-on-year growth of housing starts, production of steel, cement and glass. Our manufacturing growth proxy is the median year-on-year growth in production of metal cutting machines, autos, power generating equipment and microcomputers. (See our explanations here.)

5. Exhibit 6: Our revamped investment tracker is based on seven underlying investment indicators, including commodity demand and output, equipment sales, construction output, and new construction contracts. After data cleaning, we derive the first principal component, which explains $62\%$ of the total variation across the seven series, and then map it to Gross Fixed Capital Formation (GFCF) to measure investment on a real value-added basis.

6. Exhibit 7 and Exhibit 8: Our revised inventory tracker is based on six underlying inventory indicators, including commodities, PMI sub-indices, industrial enterprises' finished goods inventory, and auto inventory. After data cleaning, we derive the first principal component, which explains $25\%$ of the total variation of the six series, and then map it into percentage of GDP terms as our tracker for inventory changes.

7. Exhibit 9 and Exhibit 10: Our revised “outside-in” trade measures estimate China’s export growth and import growth using “mirror” statistics reported by its major trading partners, based on the country-specific lead-lag relationship, as a cross-check for the validity of China Customs trade data.

8. Exhibit 11 and Exhibit 12: Our revised GS China Financial Conditions (GSFCI) Index tracks liquidity conditions by 1) funding index: AA MTN yield, 3m SHIBOR, M2 and TSF flows; 2) equity market P/E ratio; 3) RMB on a trade-weighted basis. Accordingly, the sequential change in FCI can be attributed to factors through four major channels, i.e., FX, equity, credit and rates.

9. Exhibit 13: Our estimated growth impact of FCI impulse measures the impact of FCI changes on GDP growth (see related studies on China FCI and credit impulse here, here and here).

10. Exhibit 14: Our preferred gauge of FX flows tracks SAFE monthly net FX sales/settlement as well as the net cross-border flows of RMB.

11. Exhibit 15 and Exhibit 16: Our China domestic macro policy proxy summarizes China domestic macro policy stance from four aspects: 1) fiscal policy; 2) monetary policy; 3) credit policy; and 4) housing policy.

12. Exhibit 17: Our measure of augmented fiscal deficit is a sum of effective on-budget fiscal deficit and off-budget fiscal deficit. We estimate the off-budget spending by major channels that finance quasi-fiscal activities, which includes new local government special bonds (LGSB), land sales revenue, local government financing vehicle (LGFV) bonds, policy banks support, shadow banking loans, etc.

13. Exhibit 18: We define the fiscal spend-through ratio as a function of government revenue, government bond net issuance, and the sequential change in fiscal deposits, among others, to measure the degree to which policymakers are deploying the funds raised from government revenue and bond issuance.

14. Exhibit 19: Our government bond financing tracker measures the pace of government bond net issuance on a monthly basis and its breakdown by bond type, including central government general bond (CGGB), central government special bond (CGSB), local government general bond (LGGB) and LGSB. We also provide our projections for their monthly net issuance schedule through the remainder of the year, based on annual government bond issuance quotas, fiscal policy stance and seasonal patterns, but these may be subject to further changes when more data/policy signals come in.

15. Exhibit 20: Our property policy relative tightness index tracks the relative tightness of property policies in over 100 cities from the following aspects: 1) demand: purchase restrictions (household registration, social welfare contribution, etc.), credit restrictions (mortgage rate, down payment), sales restrictions; 2) supply: caps on selling prices, presales restrictions, land transaction tax, etc.; 3) others: property speculation, land supply.

## The China Economics Team

Andrew Tilton  
+852-2978-1802  
andrew.tilton@gs.com  
GS (Asia) L.L.C.

Xinquan Chen  
+852-2978-2418  
xinquan.chen@gs.com  
GS (Asia) L.L.C.

Hui Shan  
+852-2978-6634  
hui.shan@gs.com  
GS (Asia) L.L.C.

Yuting Yang  
+852-2978-7283  
yuting.y.yang@gs.com  
GS (Asia) L.L.C.

Lisheng Wang +852-3966-4004 lisheng.wang@gs.com GS (Asia) L.L.C.

Chelsea Song +852-2978-0106 chelsea.song@gs.com GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Chelsea Song, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Chelsea Song GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annu

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
