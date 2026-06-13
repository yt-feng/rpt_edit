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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Power Equipment

## Notes from the road; takeaways from industry conferences in Shanghai

We attended industry exhibitions last week in Shanghai, including the Data Center Industry Exhibition and the Smart Energy/PV conference, and came away with the following takeaways: first, a larger-than-expected number of Chinese electrical equipment suppliers are receiving orders from the U.S., suggesting their competitiveness on lead times and pricing is resonating with more U.S. customers; second, many electrical equipment companies are investing in R&D for solid-state transformers (SSTs) and HVDC products, and while most have not yet commercialized these offerings, Eaton (ETN.US) has launched a medium-voltage SST for AI data centers in China and Southeast Asia. TGOOD also announced a strategic cooperation with Eaton to jointly develop fully prefabricated data-center power solutions, combining Eaton's SST and medium-voltage DC capabilities with TGOOD's high-voltage prefabricated cabin systems, targeting a full-chain 220kV-to-800V DC architecture for next-generation AI data centers. There is ongoing debate about SST adoption in China, as some industry participants cite cost concerns and the pace of the shift toward higher-density solutions. (3) Companies are generally bullish on electrical equipment demand from U.S. data centers in 2027, noting that the larger AI data-center procurement cycle has not fully started and many projects remain in the pipeline; (4) factory prefabricated modules are gaining traction due to shorter lead times and lower capex, which could drive stronger demand amid China's RMB2 trillion data-center capex plan, according to Bloomberg. With rising domestic data-center capex and opportunities in the U.S., we remain positive on the sector; our top picks include Wasion Holdings (low-teens P/E with $>20\%$ CAGR) and TGOOD Electric (growing opportunities in prefabricated solutions for both T&D networks and data centers).

\- A larger-than-expected number of Chinese power equipment suppliers are gaining traction in the U.S. Our channel checks suggest rising penetration across HV/LV equipment, driven by tight supply and lead-time advantages. One T&D equipment supplier cited transformer delivery of 6–12 months versus 2–3 years for Western peers, while several companies are expanding capacity to meet overseas demand. U.S. economics are also stronger, with one supplier citing transformer gross margins of potentially 30–40%+ versus only \~teens in China, and ASPs several times domestic levels while still undercutting Western alternatives. Data centers are the main entry point and U.S. distributors / CSPs are evaluating Chinese suppliers; some CSPs reportedly visited Chinese factories earlier this year and have placed orders. Companies with U.S. exposure include Eaglerise Electric (002922 CH, NC), Ankara Intelligent Power (300617 CH, NC), Shanghai Electric (2727 HK / 601727 CH, NC; SOE), and Shandong Taikai (private). Utility exposure remains limited given stricter requirements for track record, certification and procurement-list access. Suppliers typically work through local sales teams, EPCs / contractors / distributors, while U.S. standards require additional product redesign, testing, and certification before meaningful scale-up.

\- SST remains an emerging product under the 800V DC architecture, with Eaton providing reference cases in Asia. Eaton launched its MV SST 2.0 (solid state transformers) in China at IDCE 2026, based on a 10kV medium-

## Power Equipment and Utilities

## Stephen Tsui, CFA AC

(852) 2800-8592

stephen.tsui@JPM.com

## Vento Suen

(852) 2800-8546

vento.suen@JPM.com

## Alan Hon

(852) 2800-8573

alan.hon@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

voltage AC input to 800V DC output architecture for AI data centers. Disclosed specifications include 2.5MW single-system capacity, 98.5% end-to-end efficiency and >99.999% availability, alongside claimed footprint and delivery-cycle savings versus traditional architectures. Eaton indicated it has a domestic reference project that has been operating for over a year, supporting product validation, though broader market adoption still appears to be at an early stage. The product mainly targets China and Southeast Asia, while Eaton's U.S. MV SST product uses different design parameters, including voltage level and cooling method, reflecting differences in grid standards and customer requirements.

- Competitive interest in SST is high, but adoption timing remains uncertain. We met with multiple electrical equipment companies (\~10 companies) working on SST/HVDC products, including transformer suppliers, LV electrical companies and SOEs, but most offerings still appear to be in prototype, sample, certification or early reference-project stages. Views on China adoption are mixed: some suppliers see 800V DC/SST becoming necessary as AI rack density rises and traditional AC architecture becomes less suitable, while others believe high-density demand remains limited and AC will likely remain the mainstream architecture over the next few years. SST remains more expensive than traditional solutions today, though suppliers expect ASPs to decline with scale and technology maturity; broader shipments may become more visible in 2027–28.  
- TGOOD launched “AI PowerHouse,” a system-level AI data-center power solution centered on prefabrication and green-power integration. The product integrates high-voltage transformers, GIS, medium-voltage switchgear, SST, protection and controls into factory-prefabricated modules, with 110/220kV input and 800V DC output to the data hall. TGOOD claims 150-day full-station delivery versus 12–18 months for traditional substations, 20% lower station capex, 30% lower token power cost through green-power direct connection / storage / compute-power coordination, and 99.9998% reliability. Its self-developed high-voltage SST is expected to complete grid-connected demonstration in 2027. TGOOD has recently won / signed data center projects with China telcos, Huaneng and Tencent.  
- U.S. data-center demand for electrical equipment will be even stronger in 2027. One company we visited cited around Rmb1bn of U.S. data-center-related T&D orders YTD, but noted that the larger AI data-center procurement cycle has not fully started, with many projects still in the pipeline and constrained by power availability, grid connection and long equipment lead times. Some demonstration projects are already pre-ordering transformers given lead times of over a year. Looking ahead, more data-center grid connections and behind-the-meter generation projects should drive even stronger demand for electrical equipment. On the procurement strategies for data centers, customers still appear to prefer leading global electrical brands for critical components, such as Schneider, Siemens and ABB, especially in high-spec projects. Chinese suppliers may still have opportunities in more cost-conscious projects or where customer requirements allow local substitution, but broader adoption will likely depend on product validation, certification and end-customer acceptance.  
- EE companies are seeking differentiated ESS Solutions. Some companies noted weaker 1Q ESS profitability and more selective new order intake due to lithium battery price volatility and limited cost pass-through, with suppliers increasingly seeking price-adjustment clauses, customer-supplied cells or stricter payment terms. Others are differentiating through grid-forming ESS, frequency regulation and hybrid supercapacitor + battery systems. Supercapacitors address the second- / minute-level high-power needs, batteries cover the hour-level backup, while diesel/gas or longer-duration resources can sit further behind in a layered backup architecture.

Figure 1: Eaton's MV SST 2.0 launched in IDCE 2026  
![](images/fc09e7d986d7c6dc2654900430bfb1b3f001ac725756cd5986264e78aa42cfcf.jpg)

<details>
<summary>natural_image</summary>

Exterior view of a large industrial control room with multiple panels and control panels (no visible text or symbols)
</details>

Source: Company data.

Figure 2: TGOOD's AI PowerHouse  
![](images/ea0d97ee44a290a832e64e1f25e4f9e497ad87d4b5c2e9567accb4bde57e037b.jpg)

<details>
<summary>natural_image</summary>

Exterior view of a modern industrial building with green and white facade signage, featuring a large 'Xingtong' logo and Chinese text on the facade (no other signage visible)
</details>

Source: Company data.

Companies Discussed in This Report (all prices in this report as of market close on 11 June 2026, unless otherwise indicated) Qingdao TGOOD Electric(300001.SZ/Rmb36.31/OW), Wasion Holdings Ltd - H(3393.HK/HK\$19.88/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

• Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Qingdao TGOOD Electric or related entities.  
- Market Maker/ Liquidity Provider (Hong Kong): JPM Securities (Asia Pacific) Limited and/or JPM Broking (Hong Kong) Limited and/or an affiliate is a market maker and/or liquidity provider in the securities of Wasion Holdings Ltd - H or related entities and/or warrants or options thereon, which are listed or traded on The Stock Exchange of Hong Kong Limited.  
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Wasion Holdings Ltd - H or related entities.  
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Wasion Holdings Ltd - H or related entities.  
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Wasion Holdings Ltd - H or related entities.  
• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Wasion Holdings Ltd - H or related entities.  
- Debt Position: JPM may hold a position in the debt securities of Qingdao TGOOD Electric, Wasion Holdings Ltd - H or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Qingdao TGOOD Electric (300001.SZ, 300001 CH) Price Chart  
![](images/9bab99995c1a8648beff5e3a4add7216d63584b9ff1e1cbbe59a4c4e8a694e9b.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(Rmb) |
| ---------- | ---------- |
| Sep 23     | ~20        |
| Jan 24     | ~18        |
| May 24     | ~20        |
| Sep 24     | ~17        |
| Jan 25     | ~25        |
| May 25     | ~23        |
| Sep 25     | ~28        |
| Jan 26     | ~30        |
| May 26     | ~40        |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>21-Nov-23</td><td>N</td><td>19.22</td><td>19</td></tr><tr><td>12-Aug-24</td><td>N</td><td>19.09</td><td>19.5</td></tr><tr><td>19-Dec-25</td><td>N</td><td>25.15</td><td>23</td></tr><tr><td>21-Apr-26</td><td>OW</td><td>29.80</td><td>35</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Dec 14, 2021. All share prices are as of market close on the previous business day.

Wasion Holdings Ltd - H (3393.HK, 3393 HK) Price Chart  
![](images/9090011a321f466eac7b77ee819f994efae54877505230d270e760fb1c4f8969.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(HK$) |
| ---------- | ---------- |
| Jan 26     | 35         |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target (HK$)</td></tr><tr><td>26-Feb-26</td><td>OW</td><td>27.24</td><td>35</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Nov 21, 2014. All share prices are as of market close on the previous business day. Break in coverage Aug 07, 2018 - Feb 26, 2026.  
The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period. JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Tsui, Stephen T: CK Infrastructure (1038.HK), CLP Holdings (0002) (0002.HK), China Gas Holdings (0384.HK), China Resources Gas (1193.HK), China Resources Power (0836.HK), ENN Energy (2688.HK), ENN Natural Gas – A (600803.SS), HD Hyundai Electric (267260.KS), Hangzhou Oxygen (002430.SZ), Hong Kong & China Gas (0003.HK), Huaming Equipment - A (002270.SZ), Huaneng

Power - H (0902.HK), Hyosung Heavy Industries (298040.KS), Kunlun Energy (0135.HK), LS Electric (010120.KS), Nari Technology - A (600406.SS), Power Assets (0006.HK), Qingdao TGOOD Electric (300001.SZ), Sieyuan Electric - A (002028.SZ), Wasion Holdings Ltd - H (3393.HK), Xuji Electric - A (000400.SZ)

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 11 Jun 2026 06:17 PM HKT

Disseminated 11 Jun 2026 06:17 PM HKT
"""
