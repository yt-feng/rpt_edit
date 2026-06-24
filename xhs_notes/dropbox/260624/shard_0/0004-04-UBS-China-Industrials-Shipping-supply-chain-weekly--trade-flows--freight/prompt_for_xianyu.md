你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE)

[中间内容因长度限制已省略]

 is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
