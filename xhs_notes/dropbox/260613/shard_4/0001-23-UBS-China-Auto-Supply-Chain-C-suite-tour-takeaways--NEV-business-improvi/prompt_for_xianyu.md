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

# China Auto Supply Chain

C-suite tour takeaways: NEV business improving, humanoid robotics in focus

## Key takeaways from the tour

On 10 June, we hosted a one-day field trip for investors in Jiaxing to visit Shuanghuan and Rongtai, touring factories and holding in-depth conversations with C-level executives. NEV is a key downstream market of Shuanghuan and Rongtai's traditional business, and both companies are actively entering the humanoid robotics business. The key takeaways are: 1) domestic NEV-related business improved sequentially in Q226; 2) rising penetration of NEV in European market likely to bring new growth momentum to the traditional businesses; 3) progress in the robotics business has been positive, the humanoid robotics of a leading North American humanoid robot maker is going into mass production soon.

## Shuanghuan: NEV gear leader diversifying to AIDC and humanoid robotics

Shuanghuan shared encouraging improvement on its NEV business: 1) shipment of NEV gears increased significantly QoQ in Q226, with capacity utilisation rate surpassing 90%; 2) adoption of coaxial reducers in China likely to accelerate; 3) target 1m set shipment of NEV gears in overseas market, with Hungary plant to ramp up steadily. Shuanghuan is diversifying the application of its gears to AIDC generators, with Caterpillar and Yuchai as its core customers, revenue contribution from this segment will start in 2026. Regarding humanoid robotics, Shuanghuan has been engaged in collaborative R&D with the leading North America humanoid robot maker since 2025 to develop customised new-type reducer products tailored to its technical specifications, management guided that the cooperation is progressing smoothly.

## Rongtai: high certainty on screws, actively expanding product portfolio

Rongtai's CEO noted that the company's precision screw for dexterous hand and body has received production part approval from the leading North America humanoid robot maker and observed order ramp up in June. The company is expediting the completion of its manufacturing facilities in Thailand to prepare for mass production in H226. Management guided that the progress on motors and gearboxes remains on track, and Rongtai is sampling additional products to the leading North America humanoid robot maker, such as structural parts. Management is positive on its traditional business (mica-based thermal runaway protection insulation for NEVs), driven by strong NEV sales in European market and the launch of new orders from Tesla for its semi truck and cybercab.

## Stock preference

Amid the broader industry trend of auto parts suppliers pivoting into the humanoid robotics sector, we view Kedali, Rongtai, Shuanghuan, and actuator leaders as the most likely winners in the humanoid robotics business among our coverage. Our top pick is Kedali (UBS APAC Key Call Buy), driven by its robust core business growth coupled with high visibility in its robotics business.

## Equities

China

Auto Parts

Nora Min

Analyst

nora.min@ubs.com

+86-21-3866 8905

Paul Gong

Analyst

paul.gong@ubs.com

+852-2971 7868

Jenny Wang

Analyst

S1460523110001

jenny-zb.wang@ubs.com

+86-21-3866 8837

## Valuation Method and Risk Statement

We think risks to China's auto parts sector include: 1) demand for auto parts being dampened by lower auto production; 2) automakers, with earnings squeezed by slowing car sales, passing price pressure onto parts suppliers; 3) price pressure brought by intensified competition; 4) higher auto part costs due to raw material cost inflation; 5) worse-than-expected sector consolidation; and 6) product recalls triggered by product quality issues.

Kedali: Our price target is based on DCF. We think the main company-specific risks facing Kedali are: 1) slower-than-expected capacity building and launch; 2) slower-than-expected capacity building at major customers; 3) significant loss of share at major customers; and 4) product quality issues. We think the main industry risks facing Kedali are: 1) a weaker-than-expected rise in EV penetration; 2) significant price pressure placed by battery firms on upstream structural parts businesses; 3) capacity launch by, and market share losses to, competitors; and 4) rising prices of main raw materials including copper and aluminum. We think the main macro and regional risks facing Kedali are: 1) declining passenger vehicle sales volume amid a macro downturn; and 2) adverse impact of trade friction on parts imports and exports.

Shuanghuan: We base our price target on DCF. We believe risks to our estimates include: 1) a slower rise in EV adoption than we expect; 2) weaker willingness of OEMs to apply dual-motor systems and coaxial reducers than we expect; 3) bottlenecks in overseas expansion; 4) humanoid applications falling short of our expectation.

Rongtai: Our piece target is based on a DCF methodology. We believe major sector risks include: 1) slower-than-expected EV penetration in overseas markets; 2) weaker-than-expected adoption of the 800V architecture and battery integration; 3) the emergence of new materials to exert the application of mica materials in thermal runaway protection insulation in NEVs; 4) slower-than-expected commercialization progress of humanoid robotics. We believe major company risks include: 1) new customer expansion bottlenecks; 2) slower-than-expected adoption of high value-added products; 3) customers cancel or delay orders.

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 11 June 2026 02:56 AM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

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

UBS AG Hong Kong Branch: Paul Gong. UBS Co. Limited: Jenny Wang, Nora Min.

Company Disclosures

<table><tr><td>Company Name</td><td>Reuters</td><td>12-month rating</td><td>Price</td><td>Price date</td></tr><tr><td>Shenzhen Kedali Industry</td><td>002850.SZ</td><td>Buy</td><td>Rmb187.53</td><td>10 Jun 2026</td></tr><tr><td>Zhejiang Rongtai Electric Material</td><td>603119.SS</td><td>Buy</td><td>Rmb70.19</td><td>10 Jun 2026</td></tr><tr><td>Zhejiang Shuanghuan Driveline</td><td>002472.SZ</td><td>Buy</td><td>Rmb42.69</td><td>10 Jun 2026</td></tr></table>

Source: UBS Global Research; LSEG Eikon. All prices as of local market close. Ratings in this table are the most current published ratings prior to this report. They may be more recent than the stock pricing date.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies discussed in this report, including information on valuation and risk, please contact UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research.

Zhejiang Shuanghuan Driveline (Rmb)  
![](images/49908d767cb07e31a2ee50d631d9d978dc6e979c78a50335a86bf75282b03ce5.jpg)

<details>
<summary>line chart</summary>

| Date       | Price Target (Rmb) | Stock Price (Rmb) |
|------------|--------------------|-------------------|
| 01-Apr-23  | 24                 | 24                |
| 01-Jun-23  | 24                 | 24                |
| 01-Aug-23  | 24                 | 36                |
| 01-Oct-23  | 24                 | 36                |
| 01-Dec-23  | 24                 | 24                |
| 01-Feb-24  | 24                 | 18                |
| 01-Apr-24  | 24                 | 24                |
| 01-Jun-24  | 24                 | 24                |
| 01-Aug-24  | 24                 | 18                |
| 01-Oct-24  | 24                 | 24                |
| 01-Dec-24  | 24                 | 36                |
| 01-Feb-25  | 24                 | 36                |
| 01-Apr-25  | 24                 | 36                |
| 01-Jun-25  | 48                 | 36                |
| 01-Aug-25  | 48                 | 36                |
| 01-Oct-25  | 56                 | 48                |
| 01-Dec-25  | 56                 | 36                |
| 01-Feb-26  | 56                 | 48                |
| 01-Apr-26  | 56                 | 36                |
| 01-Jun-26  | 56                 | 36                |
</details>

<table><tr><td>Date</td><td>Stock Price (Rmb)</td><td>Price Target (Rmb)</td><td>Rating</td></tr><tr><td>2023-03-10</td><td>24.70</td><td>-</td><td>No Rating</td></tr><tr><td>2025-05-21</td><td>33.73</td><td>48.60</td><td>Buy</td></tr><tr><td>2025-08-27</td><td>36.51</td><td>49.80</td><td>Buy</td></tr><tr><td>2025-09-22</td><td>50.48</td><td>56.50</td><td>Buy</td></tr><tr><td>2026-04-24</td><td>36.63</td><td>53.00</td><td>Buy</td></tr></table>

Source: UBS Global Research; LSEG Eikon as of 10-Jun-2026. All prices as of local market close. Ratings as of date shown.

Zhejiang Rongtai Electric Material (Rmb)  
![](images/0ff8fcb396aa81e4fe428dee14e3dd0316e8aeed6f9e037396ea884d00a437c5.jpg)

<details>
<summary>line chart</summary>

| Date       | Price Target (Rmb) | Stock Price (Rmb) |
|------------|--------------------|-------------------|
| 01-Apr-23  | -                  | -                 |
| 01-Jun-23  | -                  | -                 |
| 01-Aug-23  | -                  | ~20               |
| 01-Oct-23  | -                  | ~20               |
| 01-Dec-23  | -                  | ~20               |
| 01-Feb-24  | -                  | ~20               |
| 01-Apr-24  | -                  | ~20               |
| 01-Jun-24  | -                  | ~20               |
| 01-Aug-24  | -                  | ~20               |
| 01-Oct-24  | -                

[中间内容因长度限制已省略]

legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/a2fc8462a9562ede9663fde3dfd3695571c59fa461ed37211ebb4e867ce1c47e.jpg)
"""
