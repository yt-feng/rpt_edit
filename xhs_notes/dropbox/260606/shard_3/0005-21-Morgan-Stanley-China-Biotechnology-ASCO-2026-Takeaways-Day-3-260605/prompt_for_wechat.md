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
## China Biotechnology | Asia Pacific

# ASCO 2026 Takeaways - Day 3

## Key Takeaways

PD-1/IL-2: ANV600/AWT020 add validation for PD-1-directed IL-2, but $\beta\gamma$ -design IL-2s still show dose window constraints; IBI363 remains the druggable benchmark.  
PD-(L)1/VEGF: HB0025 20mg/kg Q3W + chemo showed high 1L NSCLC activity, led by PD-L1-all-comer sqNSCLC efficacy signal. Caveats remain but bears watching.  
LBA04/HARMONi-6: refer to our takeaway note - China Biotechnology: ASCO 2026 Takeaways – HARMONi-6 Plenary.  
LBA05/RASolute302: 2L focus now on exposure/rash-stomatitis management vs. allele-specific depth; 1L focus echoes Day 2 on mono vs combo/SOC/maintenance design.

## Posters:

- PD-(L)1/IL-2: ANV600 dosing remained confined to g/kg - with activity mixed across regimen/indications and IL-2-TRAEs incl. CRS/pyrexia/transaminitis elevated. AWT020 escalation remains at 0.3-1mg/kg levels w/priming explorations; solid-tumor basket ORR 30%/DCR 67% (n=27), but Gr3+ inflammatory TRAEs incl arthralgia/colitis/hematotox;. IBI363 contrast: 2L IO-resistant EGFRwt nsqNSCLC 3mg mOS to support upside and registrational path (note).  
- PD-(L1)/VEGF: HB0025: \~60 pts each sq/non-sq; ORR 84.5%/65.6%, mPFS 16.46/14.65mo, Sq PD-L1<1%/≥1% mPFS 16.72mo/16.46mo; caveats vs AK112 Ph2 data: PD-L1/stage/lower-mets skew, G3+ proteinuria/TRAE deaths.

## Plenary:

• LBA04 note.  
- LBA05/RASolute302: 2L tolerability proof points were disc. rate 1.2% vs 11.2% (chemo) with median dose intensity 93.1%. Rash 17% and stomatitis 6.6% were key dose reduction drivers. Discussant input was consistent with our day 2 takeaways, where KoL framed 1L hurdles as trial designs testing combo vs RAS mono vs SOC/maintenance, as well as parsing through differentiated clinical manifestation of each molecule.

MS ASIA LIMITED+

Jack Lin

Equity Analyst

Jack.Lin@morganstanley.com +852 3963-3746

Vanessa Liao

Research Associate

Vanessa.Liao@morganstanley.com +852 3963-0115

Asia Summer School 2026

![](images/01dc54a343ae131b4af026648d8b3fce35c0a54b38a3e3c63cbe2150e466b0ff.jpg)

## CHINA HEALTHCARE

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Jack Lin.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of April 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Abbisko Cayman Ltd, APT Medical Inc, Asymchem Laboratories. Inc, DaShenLin Pharmaceutical, Dian Diagnostics Group Co Ltd, InnoCare Pharma Ltd, Jiangsu Hengrui, Keymed Biosciences Inc., Pharmaron, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, Yifeng Pharmacy Chain Co Ltd, Yixintang Pharmaceutical.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of 3SBio, Akeso, Inc., Duality Biotherapeutics Inc, Everest Medicines Ltd, Hansoh Pharmaceutical Group Co Ltd, Innovent Biologics Inc, Insilico Medicine, Jiangsu Hengrui, Keymed Biosciences Inc., Medtide, Nanjing Leads Biolabs Co Ltd, Shenzhen Edge Medical, Simcere Pharmaceutical Group, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, WuXi XDC Cayman Inc..

Within the last 12 months, MS has received compensation for investment banking services from 3SBio, Akeso, Inc., Everest Medicines Ltd, Hansoh Pharmaceutical Group Co Ltd, Innovent Biologics Inc, Insilico Medicine, Jiangsu Hengrui, Keymed Biosciences Inc., Medtide, Shenzhen Edge Medical, Simcere Pharmaceutical Group, WuXi AppTec Co Ltd, WuXi Biologics Cayman Inc, WuXi XDC Cayman Inc..

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

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td><td>16%</td><td>201</td><td>12%</td></tr><tr><td>Total</td><td>3,667</td><td></td><td>920</td><td></td><td></td><td>1632</td><td></td></tr></table>

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

Important disclosures regarding any material conflict of interest that can reasonably be expected to have influenced MS Smith Barney LLC's choice of a third-party research provider or the subject company of a third-party research report, are available on the MS Wealth Management disclosure website at www.morganstanley.com/online/researchd

[中间内容因长度限制已省略]

05/28/2020)</td><td>HK$99.45</td></tr><tr><td>Duality Biotherapeutics Inc (9606.HK)</td><td>O (05/22/2025)</td><td>HK$187.50</td></tr><tr><td>Everest Medicines Ltd (1952.HK)</td><td>E (03/15/2024)</td><td>HK$29.04</td></tr><tr><td>HUTCHMED (China) Ltd (0013.HK)</td><td>E (05/29/2026)</td><td>HK$17.86</td></tr><tr><td>HUTCHMED (China) Ltd (HCM.O)</td><td>E (05/29/2026)</td><td>US$11.17</td></tr><tr><td>InnoCare Pharma Ltd (9969.HK)</td><td>O (05/29/2026)</td><td>HK$10.76</td></tr><tr><td>Innovent Biologics Inc (1801.HK)</td><td>O (03/03/2026)</td><td>HK$76.40</td></tr><tr><td>Insilico Medicine (3696.HK)</td><td>O (02/03/2026)</td><td>HK$38.74</td></tr><tr><td>Keymed Biosciences Inc. (2162.HK)</td><td>O (08/10/2021)</td><td>HK$59.05</td></tr><tr><td>Nanjing Leads Biolabs Co Ltd (9887.HK)</td><td>E (09/02/2025)</td><td>HK$56.85</td></tr><tr><td>RemeGen Co., Ltd. (9995.HK)</td><td>E (05/08/2024)</td><td>HK$72.40</td></tr><tr><td>VISEN Pharmaceuticals (2561.HK)</td><td>O (04/29/2025)</td><td>HK$20.88</td></tr><tr><td>Zai Lab Ltd (ZLAB.O)</td><td>O (12/14/2023)</td><td>US$17.34</td></tr><tr><td>Zai Lab Ltd (9688.HK)</td><td>O (12/14/2023)</td><td>HK$13.26</td></tr></table>

Laurence Tam

<table><tr><td>Acrobiosystems Co Ltd (301080.SZ)</td><td>O (09/11/2025)</td><td>Rmb37.39</td></tr><tr><td>Apeloa Pharmaceutical Co Ltd (000739.SZ)</td><td>O (02/28/2025)</td><td>Rmb16.05</td></tr><tr><td>Asymchem Laboratories. Inc (002821.SZ)</td><td>E (08/01/2025)</td><td>Rmb119.62</td></tr><tr><td>Asymchem Laboratories. Inc (6821.HK)</td><td>E (06/06/2023)</td><td>HK$91.45</td></tr><tr><td>Beijing Tongrentang (600085.SS)</td><td>U (11/03/2014)</td><td>Rmb24.85</td></tr><tr><td>Beijing Tongrentang Chinese Medicine (3613.HK)</td><td>O (01/14/2015)</td><td>HK$6.98</td></tr><tr><td>China National Accord Medicines Corp Ltd (000028.SZ)</td><td>U (07/25/2022)</td><td>Rmb22.70</td></tr><tr><td>China Resources Pharmaceutical Group Ltd (3320.HK)</td><td>O (06/16/2022)</td><td>HK$4.74</td></tr><tr><td>China Resources Sanjiu Medical &amp; Pharma (000999.SZ)</td><td>O (08/30/2019)</td><td>Rmb23.93</td></tr><tr><td>China Traditional Chinese Medicine (0570.HK)</td><td>U (01/17/2025)</td><td>HK$1.55</td></tr><tr><td>DaShenLin Pharmaceutical (603233.SS)</td><td>O (07/25/2022)</td><td>Rmb16.08</td></tr><tr><td>Dong E E Jiao Co. (000423.SZ)</td><td>O (05/16/2024)</td><td>Rmb48.60</td></tr><tr><td>Fu Shou Yuan International Group Ltd (1448.HK)</td><td>E (03/19/2025)</td><td>HK$2.64</td></tr><tr><td>Genscript Biotech Corporation (1548.HK)</td><td>O (08/14/2024)</td><td>HK$12.99</td></tr><tr><td>Hangzhou Tigermed Consulting (300347.SZ)</td><td>O (08/01/2025)</td><td>Rmb39.58</td></tr><tr><td>Jiangzhong Pharmaceutical Co. Ltd. (600750.SS)</td><td>O (02/08/2024)</td><td>Rmb25.51</td></tr><tr><td>Joinn Laboratories China Co Ltd (603127.SS)</td><td>E (06/06/2023)</td><td>Rmb33.42</td></tr><tr><td>Joinn Laboratories China Co Ltd (6127.HK)</td><td>E (02/26/2024)</td><td>HK$17.42</td></tr><tr><td>Jointown Pharmaceutical Group (600998.SS)</td><td>U (07/26/2021)</td><td>Rmb4.95</td></tr><tr><td>LBX Pharmacy Chain (603883.SS)</td><td>O (03/14/2022)</td><td>Rmb11.76</td></tr><tr><td>Medtide (3880.HK)</td><td>E (08/06/2025)</td><td>HK$19.88</td></tr><tr><td>Nanjing King-friend Biochemical (603707.SS)</td><td>O (02/28/2025)</td><td>Rmb7.93</td></tr><tr><td>Pharmaron (3759.HK)</td><td>O (09/25/2024)</td><td>HK$16.21</td></tr><tr><td>Pharmaron (300759.SZ)</td><td>E (09/25/2024)</td><td>Rmb22.98</td></tr><tr><td>Shandong Xinhua Pharmaceutical Co Ltd (000756.SZ)</td><td>U (02/28/2025)</td><td>Rmb12.76</td></tr><tr><td>Shanghai Pharmaceutical (601607.SS)</td><td>E (08/17/2021)</td><td>Rmb16.10</td></tr><tr><td>Shanghai Pharmaceutical (2607.HK)</td><td>O (08/17/2021)</td><td>HK$11.46</td></tr><tr><td>Shenzhen Hepalink Pharmaceutical (002399.SZ)</td><td>U (06/16/2023)</td><td>Rmb9.45</td></tr><tr><td>Sinopharm Group (1099.HK)</td><td>O (02/10/2023)</td><td>HK$17.15</td></tr><tr><td>Tasly Pharmaceutical Group Co. Ltd (600535.SS)</td><td>E (07/19/2024)</td><td>Rmb14.06</td></tr><tr><td>The United Laboratories (3933.HK)</td><td>E (06/13/2017)</td><td>HK$8.66</td></tr><tr><td>Tofflon Science &amp; Technology Group (300171.SZ)</td><td>E (09/11/2025)</td><td>Rmb11.17</td></tr><tr><td>WuXi AppTec Co Ltd (603259.SS)</td><td>O (01/17/2019)</td><td>Rmb96.75</td></tr><tr><td>WuXi AppTec Co Ltd (2359.HK)</td><td>O (01/17/2019)</td><td>HK$123.50</td></tr><tr><td>WuXi Biologics Cayman Inc (2269.HK)</td><td>O (07/17/2017)</td><td>HK$32.42</td></tr><tr><td>WuXi XDC Cayman Inc. (2268.HK)</td><td>O (12/22/2023)</td><td>HK$50.50</td></tr><tr><td>Yantai Dongcheng Biochemicals Co Ltd (002675.SZ)</td><td>E (02/28/2025)</td><td>Rmb12.57</td></tr><tr><td>Yifeng Pharmacy Chain Co Ltd (603939.SS)</td><td>O (07/25/2022)</td><td>Rmb19.70</td></tr><tr><td>Yixintang Pharmaceutical (002727.SZ)</td><td>E (07/25/2022)</td><td>Rmb11.18</td></tr><tr><td>Yunnan Baiyao Group (000538.SZ)</td><td>O (10/11/2021)</td><td>Rmb48.60</td></tr><tr><td>Zhangzhou Pientzehuang Pharmaceutical (600436.SS)</td><td>U (01/21/2022)</td><td>Rmb121.33</td></tr><tr><td>Zhejiang Hisun Pharmaceutical Co. Ltd. (600267.SS)</td><td>U (06/01/2023)</td><td>Rmb9.68</td></tr><tr><td>Zhejiang Huahai Pharmaceutical Co. Ltd. (600521.SS)</td><td>O (06/01/2023)</td><td>Rmb15.04</td></tr><tr><td>Zhejiang Jiuzhou Pharmaceutical Co Ltd (603456.SS)</td><td>E (02/28/2025)</td><td>Rmb12.34</td></tr><tr><td>Zhejiang Medicine Co. Ltd. (600216.SS)</td><td>E (02/28/2025)</td><td>Rmb12.08</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
