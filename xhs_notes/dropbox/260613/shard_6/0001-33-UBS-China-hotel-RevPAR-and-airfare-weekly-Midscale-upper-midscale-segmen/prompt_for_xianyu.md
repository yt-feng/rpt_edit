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
## First Read

# China hotel RevPAR and airfare weekly

# Midscale/upper-midscale segment RevPAR - 3.4%/+2.6% YoY; domestic airfares +23% YoY

## Mainland China hotel RevPAR +3% YoY during May 31-Jun 6

According to STR, mainland China hotel RevPAR +3% YoY during May 31-Jun 6 2026 vs. the week of Jun 1-7 2025. The RevPAR growth decelerated from +8% YoY in the prior week; still better than that in May. Average daily rate (ADR)/occupancy rate (OCC) +1.7%/+0.7ppt YoY, respectively, vs. +1.7%/+3.8ppt in the prior week.

## Midscale/upper-midscale segment RevPAR -3.4%/+2.6% YoY; better than May

By segment, upper-midscale/midscale/economy hotels RevPAR posted +2.6%/-3.4%/+2.8% YoY, respectively; weaker than last week, but better than those in May. Notably, STR data indicates that RevPAR recovery in both midscale and upper-midscale segments was driven by lowering ADR to boost OCC. This marks a strategic shift from Q1, suggesting that hotel groups are actively adapting to changing dynamics in both business trip and leisure travel markets.

## Luxury and upscale segments RevPAR +3.5%/+3.1% YoY

On the other hand, luxury and upscale hotels saw RevPAR growth of +3.5%/+3.1% YoY, better than limited service segment, mainly due to: 1) relatively less incremental supply in the high-end and luxury segment; 2) increasing inbound travel boosting demand in the segment.

## Domestic airfares +23% YoY vs. pax traffic -13% YoY during Jun 1-7

According to Flight Master, a 23% YoY increase in domestic airfares weighed on demand, driving a 13% YoY decline in passenger traffic last week, widening from a 7% YoY decline in the prior week. Domestic passenger revenue growth slowed to 7% YoY (vs. 18% YoY in the prior week).

## Equities

China

Leisure Goods & Services

Xin Chen

Analyst

xin.chen@ubs.com

+86-21-3866 8864

Ingrid Zhang

Analyst

S1460517080003

ingrid.zhang@ubs.com

+86-21-3866 8853

Beini Du

Associate

S1460525090002

betty-za.du@ubs.com

+86-213-866 8753

Jarrod Castle, CFA

Analyst

jarrod.castle@ubs.com

+44-20-7568 8883

Robin M. Farley

Analyst

robin.farley@ubs.com

+1-212-713 2060

Sukrit Friestad

Analyst

sukrit.friestad@ubs.com

+662-613 5732

Figure 1: Mainland China RevPAR YoY change  
![](images/a1f19c2adb1602444efb997af82894526203b32a83e5e15cecfde70c560676f0.jpg)

<details>
<summary>bar chart</summary>

| Month       | RevPAR yoy change |
| ----------- | ----------------- |
| Jan-Sep     | -4.0%             |
| Feb-Mar     | -19.3%            |
| Mar-Apr     | -8.8%             |
| Apr-12     | -8.7%             |
| May-Apr     | -4.3%             |
| Jun-Apr     | -11.3%            |
| Jul-May     | -13.3%            |
| Aug-May     | -5.8%             |
| Sep-May     | -7.2%             |
| Oct-May     | -7.7%             |
| Nov-May     | -7.2%             |
| Dec-May     | -4.6%             |
| Jan-Jun     | -4.9%             |
| Feb-Jun     | -2.1%             |
| Mar-Jun     | -8.3%             |
| Apr-Jun     | 7.0%              |
| May-Jun     | 15.2%             |
| Jun-Jun     | 12.4%             |
| Jul-Aug     | 0.6%              |
| Aug-Aug     | 1.9%              |
| Sep-Aug     | 4.1%              |
| Oct-Aug     | 2.5%              |
| Nov-Aug     | 0.3%              |
| Dec-Aug     | 0.9%              |
| Jan-Oct     | -0.4%             |
| Feb-Oct     | -1.7%             |
| Mar-Oct     | 5.3%              |
| Apr-Oct     | 4.7%              |
| May-Oct     | -14.4%            |
| Jun-Oct     | -13.0%            |
| Jul-Nov     | -1.2%             |
| Aug-Nov     | -0.5%             |
| Sep-Nov     | 4.5%              |
| Oct-Nov     | 4.3%              |
| Nov-Nov     | 5.1%              |
| Dec-Nov     | 6.8%              |
| Jan-Dec     | -0.9%             |
| Feb-Dec     | -8.7%             |
| Mar-Dec     | 0%                |
| Apr-Dec     | 15.2%             |
| May-Dec     | 8.0%              |
| Jun-Dec     | 3.0%              |
</details>

Source: STR

Figure 2: China weekly domestic air seat capacity, pax volume and airfare YoY  
![](images/b8f4b770d1c40ae86716726356def1a79b91f91aa331e73f3f24197324c3e586.jpg)

<details>
<summary>line chart</summary>

| Date       | Domestic tax volume yoy | Domestic seat capacity yoy | Domestic airfare yoy (RHS) |
|------------|--------------------------|----------------------------|-----------------------------|
| 20-Oct-24  | ~10%                     | ~0%                        | ~0%                         |
| 20-Nov-24  | ~10%                     | ~0%                        | ~0%                         |
| 20-Dec-24  | ~10%                     | ~0%                        | ~0%                         |
| 20-Jan-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Feb-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Mar-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Apr-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-May-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Jun-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Jul-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Aug-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Sep-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Oct-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Nov-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Dec-25  | ~10%                     | ~0%                        | ~0%                         |
| 20-Jan-26  | ~10%                     | ~0%                        | ~0%                         |
| 20-Feb-26  | ~10%                     | ~0%                        | ~40%                        |
| 20-Mar-26  | ~10%                     | ~0%                        | ~30%                        |
| 20-Apr-26  | ~10%                     | ~0%                        | ~25%                        |
| 20-May-26  | ~10%                     | ~0%                        | ~30%                        |
</details>

Source: Flight Master

Figure 3: RevPAR YoY performance by segment (May 31-Jun 6)  
![](images/5004ecf308eea7b2029535cf1926be313e7e4d067d50a28f884d4f30b1dee49f.jpg)

<details>
<summary>bar chart</summary>

RevPAR (YoY change %)
| Category | RevPAR (YoY change %) |
|---|---|
| Mainland China | 3.0 |
| Luxury-Upper Upscale | 3.5 |
| Upscale | 3.1 |
| Upper Midscale | 2.6 |
| Midscale | -3.5 |
| Economy | 2.8 |
</details>

Source: STR

Figure 4: ADR YoY performance by segment (May 31-Jun 6)  
![](images/c44aaef867da643aad53dae6d84128766c0c260c58db1b002222333425275fdb.jpg)

<details>
<summary>bar chart</summary>

ADR (YoY change %)
| Category | ADR (YoY change %) |
|---|---|
| Mainland China | 2.0 |
| Luxury-Upper Upscale | 0.5 |
| Upscale | -3.0 |
| Upper Midscale | -2.5 |
| Midscale | -2.5 |
| Economy | 2.5 |
</details>

Source: STR

Figure 5: OCC YoY performance by segment (May 31-Jun 6)  
![](images/65bdcd5b8b644c49d379e9ab8b3c6c9ce81389ab1e2fb39e0e84f2dae8aab3db.jpg)

<details>
<summary>bar chart</summary>

Occ (YoY change ppt)
| Category | Occ (YoY change ppt) |
|---|---|
| Mainland China | 0.5 |
| Luxury-Upper Upscale | 2.0 |
| Upscale | 3.0 |
| Upper Midscale | 2.8 |
| Midscale | -1.0 |
| Economy | 0.6 |
</details>

Source: STR

Figure 6: Hotel booking APP weekly active users trend  
![](images/a1a5219a543941d3df011af87455f45387eb2740e0727800d24cca2a65c82610.jpg)

<details>
<summary>line chart</summary>

| Date   | Home Inns 首旅如家 | Huazhu 华住会 | Jinjiang Hotel 锦江酒店 | A Tour 亚朵 |
|--------|-------------------|---------------|------------------------|------------|
| Jan-17 | ~0.03%            | ~0.05%        | ~0.02%                 | ~0.01%     |
| Jan-18 | ~0.04%            | ~0.07%        | ~0.03%                 | ~0.01%     |
| Jan-19 | ~0.05%            | ~0.10%        | ~0.04%                 | ~0.01%     |
| Jan-20 | ~0.06%            | ~0.12%        | ~0.05%                 | ~0.01%     |
| Jan-21 | ~0.07%            | ~0.15%        | ~0.06%                 | ~0.01%     |
| Jan-22 | ~0.08%            | ~0.20%        | ~0.07%                 | ~0.01%     |
| Jan-23 | ~0.09%            | ~0.25%        | ~0.08%                 | ~0.01%     |
| Jan-24 | ~0.10%            | ~0.35%        | ~0.09%                 | ~0.01%     |
| Jan-25 | ~0.11%            | ~0.50%        | ~0.10%                 | ~0.01%     |
</details>

Source: UBS Evidence Lab (>Access Dataset)

\*UBS Evidence Lab is a sell-side team of experts that work across numerous specialized labs creating insight-ready datasets. The experts turn data into evidence by applying a combination of tools and techniques to harvest, cleanse, and connect billions of data items each month. Since 2014, UBS analysts have utilized the expertise of UBS Evidence Lab for insight-ready datasets on companies, sectors, and themes, resulting in the production of thousands of differentiated UBS reports. UBS Evidence Lab does not provide investment recommendations or advice but provides insight-ready datasets for further analysis by UBS and by clients. All published UBS Evidence Lab content is available via UBS Neo. The amount and type of content available may vary. Please contact your UBS sales representative if you wish to discuss access.

## China Hotel Booking App Usage Monitor (>Access Dataset)

This report leverages the following UBS Evidence Lab asset: China Hotel Booking App Usage Monitor. UBS Evidence Lab uses App Analytics by QuestMobile, a leading provider of business intelligence in China's mobile internet market. UBS Evidence Lab tracks various usage trends including active users, sessions, time spent, retention rate and user stickiness, and aggregated by week and month.

## Valuation Method and Risk Statement

The main downside risks facing China's travel, lodging and leisure sector are: 1) continued economic sluggishness; 2) slower-than-expected growth in peak season tourist traffic; 3) bad weather affecting travel; 4) earthquakes, air accidents, epidemics and other disasters; and 5) China loosening policies limiting entry into the duty-free industry.

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 11 June 2026 08:14 AM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>54%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 31 March 2026.  
1: Percentage of companies under coverage globally within the 12-month rating category.  
2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discoun

[中间内容因长度限制已省略]

legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/a07814770bf24aab83bd4cccd080e303a632525b88d515806736c42b2d20485e.jpg)
"""
