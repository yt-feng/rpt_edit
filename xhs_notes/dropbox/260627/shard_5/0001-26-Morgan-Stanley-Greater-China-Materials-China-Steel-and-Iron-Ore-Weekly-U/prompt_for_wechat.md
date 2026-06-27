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
<table><tr><td colspan="2">GREATER CHINA MATERIALS</td></tr><tr><td>Asia Pacific Industry View</td><td>Attractive</td></tr></table>

# China Steel and Iron Ore Weekly Update

## Key Takeaways

\- Apparent consumption of long products declined 12.7% WoW, while that of flat products decreased 3.1% WoW.

Weekly output slipped for long products and flat products; inventory rose at traders and mills. Utilization rates inched up at electric arc furnaces (EAF).

Iron ore inventory grew at mills: Operating rates improved, along with daily output.

Iron ore shipments: Combined shipments from Australia and Brazil were down by 0.32Mt WoW for the period 15th June to 21st June. Shipments from Australia were up by 0.86Mt WoW. Shipments from Brazil were down by 1.18Mt WoW.

Exhibit 1: Weekly data summary

<table><tr><td rowspan="2"></td><td colspan="3">Steel</td><td rowspan="2" colspan="3">Iron Ore</td></tr><tr><td>Volume (kt) / rate (%)</td><td>WoW</td><td>YoY</td></tr><tr><td>Inventory - Traders</td><td>11,449</td><td>1.7%</td><td>26.3%</td><td>Inventory - Ports</td><td>156,720</td><td>-0.2%</td></tr><tr><td>Inventory - Mills</td><td>4,561</td><td>5.8%</td><td>5.2%</td><td>Inventory - Per Mill</td><td>238</td><td>5.6%</td></tr><tr><td>Weekly Consumption - Long</td><td>2,681</td><td>-12.7%</td><td>-12.2%</td><td>Operating rate</td><td>63.1%</td><td>0.3 ppts</td></tr><tr><td>Weekly Consumption - Flat</td><td>5,469</td><td>-3.1%</td><td>-4.8%</td><td>Average daily output</td><td>398.7</td><td>0.4%</td></tr><tr><td>Weekly Output - Long</td><td>2,997</td><td>-2.0%</td><td>-1.4%</td><td>Shipments - Australia</td><td></td><td>+0.86Mt</td></tr><tr><td>Weekly Output - Flat</td><td>5,593</td><td>-0.5%</td><td>-3.1%</td><td>Shipments - Brazil</td><td></td><td>-1.18Mt</td></tr><tr><td>Utilization - 247 mills</td><td>90.8%</td><td>0.5 ppts</td><td>(0.0 ppts)</td><td></td><td></td><td></td></tr><tr><td>Utilization - EAF</td><td>64.5%</td><td>0.1 ppts</td><td>10.0 ppts</td><td></td><td></td><td></td></tr></table>

Source: Mysteel, MS. Note: EAF = electric arc furnace.

Exhibit 2: Weekly steel demand  
![](images/fd0dfca487c31d6c88ddcc3b7f3d6a92707fbd74e9fb377a568b571707a4fdc2.jpg)

MS ASIA LIMITED+

Rachel L Zhang  
Equity Analyst  
Rachel.Zhang@morganstanley.com +852 2239-1520

Hannah Yang, CFA  
Equity Analyst  
Hannah.Yang1@morganstanley.com +852 2239-7079

Chris Jiang  
Equity Analyst  
Chris.Jiang@morganstanley.com +852 3963-1593

Cynthia Tang  
Research Associate  
Cynthia.Tang@morganstanley.com +852 3963-4360

MS & CO. INTERNATIONAL PLC+

Amy Gower (Amy Sergeant), CFA
Commodities Strategist
Amy.Gower1@morganstanley.com +44 20 7677-6937

![](images/e6e9ff8df8568ee5151ec0f93fa07cc1e8a783a0f647ad8539d996f156e263df.jpg)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Amy Gower (Amy Sergeant), CFA; Chris Jiang; Hannah Yang, CFA; Rachel L. Zhang.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Aluminum Corp. of China Ltd., Anhui Honglu Steel Construction, Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Flat Glass Group Co Ltd, Ganfeng Lithium Co. Ltd., GEM Co Ltd, Jiangxi Copper, JL Mag Rare-Earth Co. Ltd, Shandong Gold Mining Co. Ltd, Shenzhen Kedali Industry Co Ltd, Sinomine Resource Group Co Ltd, Tianqi Lithium Industries Inc., Zijin Mining Group.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of CNGR Advanced Material Co., Ltd., MMG Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for investment banking services from Ganfeng Lithium Co. Ltd., MMG Ltd, Zijin Mining Group.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from China Jushi, China Steel Corp., CMOC Group Ltd, Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Mining Group.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: China Jushi, China Steel Corp., CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Gold International, Zijin Mining Group.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment Services Clients (MISC)</td></tr><tr><td>Stock Rating Category</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of Rating Category</td><td>Count</td><td>% of Total Other MISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td><td>16%</td><td>201</td><td>12%</td></tr><tr><td>Total</td><td>3,667</td><td></td><td>920</td><td></td><td></td><td>1632</td><td></td></tr></table>

Data include common stock and ADRs currently assigned ratings. Investment Banking Clients are companies from whom MS received investment banking compensation in the last 12 months. Due to rounding off of decimals, the percentages provided in the "% of total" column may not add up to exactly 100 percent.

## Analyst Stock Ratings

Overweight (O). The stock's total return is expected to exceed the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Equal-weight (E). The stock's total return is expected to be in line with the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Not-Rated (NR). Currently the analyst does not have adequate conviction about the stock's total return relative to the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Underweight (U). The stock's total return is expected to be below the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Unless otherwise specified, the time frame for price targets included in MS is 12 to 18 months.

## Analyst Industry Views

Attractive (A): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be attractive vs. the relevant broad market benchmark, as indicated below.

In-Line (I): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be in line with the relevant broad market benchmark, as indicated below. Cautious (C): The analyst views the performance of his or her industry coverage universe over the next 12-18 months with caution vs. the relevant broad market benchmark, as indicated below. Benchmarks for each region are as follows: North America - S&P 500; Latin America - relevant MSCI country index or MSCI Latin America Index; Europe - MSCI Europe; Japan - TOPIX; Asia - relevant MSCI country index or MSCI sub-regional index or MSCI AC Asia Pacific ex Japan Index.

## Important Disclosures for MS Smith Barney LLC Customers

Important disclosures regarding any material conflict of interest that can reasonably be expected to have influenced MS Smith Barney LLC's choice of a third-party research provider or the subject company of a third-party research report, are available on the MS Wealth Management disclosure website at www.morganstanley.com/online/researchdisclosures. For MS specific disclosures, you may refer to https://www.morganstanley.com/eqr/disclosures/webapp/generalresearch.

Each MS report is reviewed and approved on behalf of MS Smith Barney LLC. This review and approval is conducted by the same person who reviews the research report on behalf of MS. This could create a conflict of interest.

## Other Important Disclosures

MS policy is to update research reports as and when the Research Analyst and Research Management deem appropriate, based on developments with the issuer, the sector, or the market that may have a material impact on the research views or opinions stated therein. In addition, certain Research publications are intended to be updated on a regular periodic basis (weekly/monthly/quarterly/annual) and will ordinarily be updated with that frequency, unless the Research Analyst and Research Management determine that a different publication schedule is appropriate based on current conditions.

MS is not acting as a municipal advisor and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of Section 975 of the Dodd-Frank Wall Street Reform and Consumer Protection Act.

MS produces an equity research product called a "Tactical Idea." Views contained in a "Tactical Idea" on a particular stock may be contrary to the recommendations or views expressed in research on the same stock. This may be the result of differing time horizons, methodologies, market events, or other factors. For all research available on a particular stock, please contact your sales representative or go to Matrix at http://www.morganstanley.com/matrix.

MS is provided to our clients through our proprietary research portal on Matrix and also distributed electronically by MS to clients. Certain, but not all, MS Rese

[中间内容因长度限制已省略]

 continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Greater China Materials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/25/2026)</td></tr><tr><td colspan="3">Chris Jiang</td></tr><tr><td>Anhui Honglu Steel Construction (002541.SZ)</td><td>U (12/16/2025)</td><td>Rmb16.56</td></tr><tr><td>CGN Mining Co Ltd (1164.HK)</td><td>O (01/18/2023)</td><td>HK$2.59</td></tr><tr><td>Chengxin Lithium Group Co. Ltd. (002240.SZ)</td><td>E (12/16/2025)</td><td>Rmb46.51</td></tr><tr><td>GEM Co Ltd (002340.SZ)</td><td>U (04/20/2026)</td><td>Rmb7.13</td></tr><tr><td>Shenzhen Kedali Industry Co Ltd (002850.SZ)</td><td>O (08/21/2023)</td><td>Rmb182.28</td></tr><tr><td>Sinomine Resource Group Co Ltd (002738.SZ)</td><td>O (12/16/2025)</td><td>Rmb58.15</td></tr><tr><td>Yongxing Special Materials Technology (002756.SZ)</td><td>E (11/25/2022)</td><td>Rmb60.48</td></tr><tr><td>Zhejiang Huayou Cobalt Co Ltd (603799.SS)</td><td>O (10/08/2025)</td><td>Rmb50.21</td></tr><tr><td colspan="3">Hannah Yang, CFA</td></tr><tr><td>China Hongqiao Group (1378.HK)</td><td>O (09/15/2023)</td><td>HK$20.64</td></tr><tr><td>Chuangxin Industries Holdings Ltd. (2788.HK)</td><td>O (03/19/2026)</td><td>HK$14.27</td></tr><tr><td>Flat Glass Group Co Ltd (6865.HK)</td><td>O (07/30/2020)</td><td>HK$6.07</td></tr><tr><td>Flat Glass Group Co Ltd (601865.SS)</td><td>O (07/30/2020)</td><td>Rmb10.45</td></tr><tr><td>MMG Ltd (1208.HK)</td><td>O (12/16/2024)</td><td>HK$7.01</td></tr><tr><td>Shandong Pharmaceutical Glass Co. Ltd. (600529.SS)</td><td>U (04/20/2026)</td><td>Rmb18.23</td></tr><tr><td>Shenhuo Coal and Power (000933.SZ)</td><td>O (09/02/2025)</td><td>Rmb22.22</td></tr><tr><td>Tianshan Aluminum (002532.SZ)</td><td>O (03/19/2026)</td><td>Rmb11.62</td></tr><tr><td>Xinyi Glass Holding Limited (0868.HK)</td><td>U (05/14/2024)</td><td>HK$8.62</td></tr><tr><td>Zhongfu Shenying Carbon Fiber Co Ltd (688295.SS)</td><td>O (08/25/2023)</td><td>Rmb55.95</td></tr><tr><td colspan="3">Rachel L Zhang</td></tr><tr><td>Aluminum Corp. of China Ltd. (601600.SS)</td><td>O (11/30/2020)</td><td>Rmb8.80</td></tr><tr><td>Aluminum Corp. of China Ltd. (2600.HK)</td><td>O (11/30/2020)</td><td>HK$7.75</td></tr><tr><td>Baoshan Iron &amp; Steel (600019.SS)</td><td>O (01/16/2016)</td><td>Rmb5.49</td></tr><tr><td>Beijing New Building Materials (000786.SZ)</td><td>O (04/09/2024)</td><td>Rmb18.41</td></tr><tr><td>Beijing Oriental Yuhong Waterproof Techn (002271.SZ)</td><td>E (09/25/2024)</td><td>Rmb12.25</td></tr><tr><td>China Jushi (600176.SS)</td><td>O (12/22/2020)</td><td>Rmb70.80</td></tr><tr><td>China Lesso Group Holdings Ltd (2128.HK)</td><td>U (10/08/2025)</td><td>HK$3.78</td></tr><tr><td>China Steel Corp. (2002.TW)</td><td>U (12/16/2025)</td><td>NT$19.05</td></tr><tr><td>CMOC Group Ltd (3993.HK)</td><td>O (09/24/2019)</td><td>HK$15.50</td></tr><tr><td>CMOC Group Ltd (603993.SS)</td><td>O (06/21/2024)</td><td>Rmb18.07</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (300919.SZ)</td><td>E (01/12/2026)</td><td>Rmb46.77</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (2579.HK)</td><td>O (01/12/2026)</td><td>HK$25.82</td></tr><tr><td>FangDa Carbon New Material Co. Ltd. (600516.SS)</td><td>U (12/16/2024)</td><td>Rmb6.77</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (002460.SZ)</td><td>O (04/20/2026)</td><td>Rmb68.36</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (1772.HK)</td><td>O (12/16/2025)</td><td>HK$52.75</td></tr><tr><td>Henan Liliang Diamond Co. Ltd (301071.SZ)</td><td>U (04/20/2026)</td><td>Rmb102.96</td></tr><tr><td>Jiangsu Dingsheng New Materials (603876.SS)</td><td>U (04/20/2026)</td><td>Rmb29.14</td></tr><tr><td>Jiangxi Copper (0358.HK)</td><td>O (10/08/2025)</td><td>HK$32.52</td></tr><tr><td>Jiangxi Copper (600362.SS)</td><td>O (10/08/2025)</td><td>Rmb45.43</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (6680.HK)</td><td>O (04/23/2025)</td><td>HK$17.85</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (300748.SZ)</td><td>O (04/23/2025)</td><td>Rmb32.38</td></tr><tr><td>Nine Dragons Paper (2689.HK)</td><td>E (01/04/2023)</td><td>HK$6.71</td></tr><tr><td>Shandong Gold Mining Co. Ltd (600547.SS)</td><td>O (04/23/2025)</td><td>Rmb23.93</td></tr><tr><td>Shandong Gold Mining Co. Ltd (1787.HK)</td><td>O (12/12/2024)</td><td>HK$17.62</td></tr><tr><td>Shandong Nanshan Aluminium Co. (600219.SS)</td><td>O (11/30/2020)</td><td>Rmb4.29</td></tr><tr><td>Tianqi Lithium Industries Inc. (9696.HK)</td><td>O (12/16/2025)</td><td>HK$41.42</td></tr><tr><td>Tianqi Lithium Industries Inc. (002466.SZ)</td><td>O (04/20/2026)</td><td>Rmb64.64</td></tr><tr><td>Weixing New Building Materials (002372.SZ)</td><td>U (10/08/2025)</td><td>Rmb8.28</td></tr><tr><td>Zhaojin Mining Industry (1818.HK)</td><td>O (06/21/2024)</td><td>HK$16.68</td></tr><tr><td>Zijin Gold International (2259.HK)</td><td>O (11/06/2025)</td><td>HK$92.95</td></tr><tr><td>Zijin Mining Group (2899.HK)</td><td>O (11/06/2025)</td><td>HK$28.04</td></tr><tr><td>Zijin Mining Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb25.92</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
