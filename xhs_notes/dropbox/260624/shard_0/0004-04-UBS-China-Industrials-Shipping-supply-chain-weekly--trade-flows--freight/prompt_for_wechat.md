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
- 已识别机构名：`UBS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份UBS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
First Read

# China Industrials Shipping supply chain weekly: trade flows, freight and Hormuz updates (week 25)

## Key highlights from high-frequency data

We compile weekly data from UBS Evidence Lab, the Ministry of Transport, UBS Evidence Lab and other third-party data providers to track the latest trade flows across shipping, shipbuilding and ports.

## Hormuz reopen may result in recovery of VLCC average earnings

Based on Clarksons data, daily vessel transits through the Strait of Hormuz picked up last week, reaching 25 vessels up from \~10 previously but still well below the pre-conflict level of 125. An initial rush for VLCC to the Persian Gulf has resulted in a spike in spot rates, while most operators are still waiting to monitor the progress of the release of vessels in the gulf. Our Maritime Trade Disruption Monitor (>Access Dataset) indicated a notable increase in the tankers departing eastbound from Hormuz since last Friday. VLCC average earnings from Middle East/West Africa to China rose notably last week to reflect expectations of the reopening of the Persian Gulf, with average earnings +87% to \~\$195k/day.

## Container shipping volume keeps rising

Container throughput at key ports in China increased 3% WoW and 2% YoY last week. Amid a pick-up in shipping demand, main lane freight rates saw further gains: overall SCFI freight rates increased by 5% WoW last week (+67% YoY), with Shanghai-Europe +3% WoW and Transpacific +9-11% WoW; Port of LA imports were down 12% YoY in week 25 and estimated to decrease \~6% YoY in week 25. Intra-Asia containership chartering index recovered by 1% WoW last week. Based on our Maritime Destination Monitor (>Access Dataset), the container shipping volume in the Asia-US route showed strong YoY growth since May.

## BDI & earnings of bulker and new build price remained elevated

The bulker market softened last week; BDI decreased 4% WoW and average earnings of capesize bulker increased 11% WoW, with BDI YTD + 43%. The shipbuilding newbuild price index remained flattish WoW last week, with sustained demand for VLCC and gas carriers.

Equities

China
Industrial

Robin Xu
Analyst
bin.xu@ubs.com
+86-21-3866 8872

Zed Sheng
Analyst
S1460525030003
zed.sheng@ubs.com
+86-21-3866 8730

Cristian Nedelcu, CFA
Analyst
cristian.nedelcu@ubs.com
+44-20-7568 4375

William Deng
Economist
william-w.deng@ubs.com
+852-2971 6765

Xin Chen
Analyst
S1460511050002
xin.chen@ubs.com
+86-21-3866 8864

Figure 1: Middle East/US Gulf/West Africa-China VLCC TCE +122%/+6%/-20% vs. pre-conflict level  
![](images/87411b81e3790b4ddd47f18db48a7f4234c2b9dd8e898bb84153f9613275717f.jpg)  
Source: Clarksons, data as of 19 June

Figure 2: VLCC 1 year charter rate remained stable  
![](images/407117450daaf34c0a5fbad29e21cc77ad85052c24048b37e3b1a4666102288e.jpg)  
Source: Clarksons, data as of 19 June

Figure 3: Average earnings of Capesize rallied by 11% WoW last week  
![](images/9911c2da503c705f57712f3041d8577057b0df43951ba7165ab23e560634d37a.jpg)  
Source: Clarksons, data as of 19 June

Figure 4: Vessels passage at Hormuz picked up while still notably below pre-conflict level  
![](images/60eb9b3dcba46b920d90e21a41caebd92b43ea270604ea259ae21754ee4d98cc.jpg)  
Source: Clarksons, data as of 20 June

Figure 5: Container throughput at China's key ports +3% WoW, +2% YoY last week  
![](images/f5410df86011cd75e64866aa112b0d80d14e1e74a47c075bb8a8fc2344e6fff9.jpg)  
Source: Ministry of Transport

Figure 6: Container volume new in transit from Asia to US has been showing a front loading pattern  
![](images/eae66c6f61b590701f92620dae9e3282b4ce4e8b836009927b6f32b3fdc3b4ab.jpg)  
Source: UBS Evidence Lab (> Access Dataset)

Figure 7: SCFI +5% WoW and +67% YoY

<table><tr><td>WoW/YoY</td><td>SCFI</td><td>CCFI</td><td>SCFI Europe</td><td>SCFI W/C US</td><td>SCFI E/C US</td><td>NCFI Thailand&amp;Vietnam</td></tr><tr><td>2026-05-15</td><td>10%/45%</td><td>0%/16%</td><td>14%/57%</td><td>10%/1%</td><td>11%/4%</td><td>6%/29%</td></tr><tr><td>2026-05-22</td><td>4%/40%</td><td>3%/19%</td><td>5%/45%</td><td>1%/-4%</td><td>2%/1%</td><td>1%/15%</td></tr><tr><td>2026-05-29</td><td>16%/24%</td><td>4%/22%</td><td>30%/56%</td><td>31%/-20%</td><td>24%/-15%</td><td>-1%/10%</td></tr><tr><td>2026-06-05</td><td>6%/22%</td><td>3%/22%</td><td>5%/56%</td><td>10%/-19%</td><td>8%/-17%</td><td>-5%/10%</td></tr><tr><td>2026-06-12</td><td>9%/43%</td><td>5%/19%</td><td>18%/66%</td><td>12%/24%</td><td>10%/-6%</td><td>-5%/11%</td></tr><tr><td>2026-06-19</td><td>5%/67%</td><td>8%/19%</td><td>3%/72%</td><td>11%/105%</td><td>9%/28%</td><td>-11%/4%</td></tr></table>

Source: Shanghai Shipping Exchange, Clarksons, data as of 19 June 2026

Figure 8: SCFI Shanghai-WC America Container Freight Rate +11% WoW and 105% YoY  
![](images/cf9a16de06b768a9698949d82b581c1e88a78fc6e7db97394550b68ec55d7acd.jpg)  
Source: Clarksons; Note: data as of 19 June 2026

Figure 9: Container ships re-routing away from Red Sea still at high levels (+4-5% YoY)  
![](images/eadad134e94b33cccbc286b1c2a6f29c757a82e625a09715745f85f37d684ab2.jpg)  
Source: Clarksons; Note: data as of 19 June 2026

Figure 10: Intra-Asia chartering index recovered WoW last week  
![](images/70b8d0490b93e095ed8b836592c38e96f09114abad5d7eb17558e1622bcc9733.jpg)  
Source: Company data

Figure 11: Strong VLCC demand drives up YTD strong global shipbuilding demand  
![](images/1ea760d5457d1fa7a8efec70cd8d5d080374d3b7a9a77e27b3fe276c82398003.jpg)  
Source: Clarksons

Figure 12: Both Clarksons and CNPI indicate new build price remain elevated  
![](images/4603ed60371a87be3d0b4cb218eff26c048a710a6b54255d494a9f15ddd7b7b0.jpg)  
Source: Clarksons, CNPI, as of 21 June 2026

\*UBS Evidence Lab is a sell-side team of experts that work across numerous specialized labs creating insight-ready datasets. The experts turn data into evidence by applying a combination of tools and techniques to harvest, cleanse, and connect billions of data items each month. Since 2014, UBS analysts have utilized the expertise of UBS Evidence Lab for insight-ready datasets on companies, sectors, and themes, resulting in the production of thousands of differentiated UBS reports. UBS Evidence Lab does not provide investment recommendations or advice but provides insight-ready datasets for further analysis by UBS and by clients. All published UBS Evidence Lab content is available via UBS Neo. The amount and type of content available may vary. Please contact your UBS sales representative if you wish to discuss access.

## Global Maritime Destination Monitor (>Access Dataset)

This report leverages the following UBS Evidence Lab asset: Global Maritime Destination Monitor. UBS Evidence Lab uses hourly AIS (Automated Identification System) data to monitor the locations of more than 35,200 commercial maritime vessels sailing around the globe. Each ship has a unique identification number (IMO number), which is linked to vessel characteristics such as cargo type, size, and capacity, enabling the calculation of vessel counts and aggregated cargo tonnage (DWT) moving through global maritime points of interest (regions, ports). In addition, Bill of Lading data offers a detailed view of shipment activity, providing further insight into the flow of goods being transported across global trade routes. UBS Evidence Lab has conducted thorough benchmarking and has designed proprietary cleaning techniques to ensure the data is accurate by reducing the noise associated with AIS data.

## Global Maritime Fleet Monitor (>Access Dataset)

This report leverages the following UBS Evidence Lab asset: Global Maritime Fleet Monitor. UBS Evidence Lab uses hourly AIS (Automated Information System) data to monitor the locations of more than 35,200 commercial maritime vessels (tankers, bulkers, containers) sailing around the globe. Each ship has a unique identification number (IMO number) which is connected to vessel characteristics data including cargo type, size, and capacity in order to calculate the quantity and aggregated cargo tonnage moving through global maritime points of interest (regions, and ports). UBS Evidence Lab has conducted thorough benchmarking and has designed proprietary cleaning techniques to ensure the data is accurate by reducing the noise associated with AIS data.

## Global Maritime Trade Monitor (>Access Dataset)

This report leverages the following UBS Evidence Lab asset: Global Maritime Trade Monitor. UBS Evidence Lab uses hourly AIS (Automated Information System) data to monitor the locations of more than 35,200 commercial maritime vessels (tankers, bulkers, containers) sailing around the globe. Each ship has a unique identification number (IMO number) which is connected to vessel characteristics data including cargo type, size, and capacity in order to calculate the quantity and aggregated cargo tonnage (DWT) moving through global maritime points of interest (regions, ports, and choke points). AIS data is noisy, so UBS Evidence Lab has designed proprietary cleaning algorithms and benchmarking techniques to ensure the data is accurate. UBS Evidence Lab uses statistical methods combined with reported draft level for each vessel to calculate a proprietary indicator of amount of cargo each ship is carrying.

## Daily Maritime Trade Disruption Monitor (>Access Dataset)

This report leverages the following UBS Evidence Lab asset: Daily Maritime Trade Disruption Monitor. UBS Evidence Lab uses hourly AIS (Automated Information System) data to monitor the locations of more than 35,200 commercial maritime vessels sailing around the globe. Each ship has a unique identification number (IMO number) which is connected to vessel characteristics data including cargo type, size, and capacity in order to calculate the quantity and aggregated cargo tonnage (DWT) moving through global maritime points of interest (choke points, ports and regions).

Investment downsizing at the macroeconomic level remains a key risk for China's industrial sector. If China's economy remains weak, demand for industrial goods or import/export volume could shrink, resulting in slow growth. If preferential policies, such as tax incentives for high-tech companies, are cancelled it could affect earnings. Intense competition with domestic or foreign enterprises could cause market share losses.

## Valuation Method and Risk Statement

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 22 June 2026 04:41 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>54%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 31 March 2026.  
1: Percentage of companies under coverage globally within the 12-month rating category.

2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE): Exceptions to the standard +/-6% bands may be granted by the Investment Review Consultation (IRC). Factors considered by the IRC include the stock's volatility and the credit spread of the respective company's debt. As a result, stocks deemed to be very high or low risk may be subject to higher or lower bands as they relate to the rating. When such exceptions apply, they will be identified in the Company Disclosures table in the relevant research piece.

Research analysts contributing to this report who are employed by any non-US affiliate of UBS LLC are not registered/qualified as research analysts with FINRA. Such analysts may not be associated persons of UBS LLC and therefore are not subject to the FINRA restrictions on communications with a subject company, public appearances, and trading securities held by a research analyst account. The name of each affiliate and analyst employed by that affiliate contributing to this report, if any, follows.

UBS AG Hong Kong Branch: William Deng. UBS AG London Branch: Cristian Nedelcu, CFA. UBS Co. Limited: Robin Xu, Xin Chen, Zed Sheng.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies discussed in this report, including information on valuation and risk, please contact UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research.

The Disclaimer relevant to Global Wealth Management clients follows the Global Research Disclaimer. The Disclaimer relevant to CS Wealth Management follows the Global Wealth Management Disclaimer.

## UBS Global Research Disclaimer

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

Any opinions expressed in this document may change without notice and are only current as of the date of publication. Different areas, groups, and personnel within UBS may produce and distribute separate research products independently of each other. For example, research publications from UBS CIO are produced by UBS Global Wealth Management. UBS Global Research is produced by UBS Investment Bank. Research methodologies and rating systems of each separate research organization may differ, for example, in terms of investment recommendations, investment horizon, model assumptions, and valuation methods. As a consequence, except for certain economic forecasts (for which UBS CIO and UBS Global Research may collaborate), investment recommendations, ratings, price targets, and valuations provided by each of the separate 

[中间内容因长度限制已省略]

lated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
