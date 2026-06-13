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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`UBS`。标题格式建议：`# UBS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份UBS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
| 01-Oct-24  | -                  | ~20               |
| 01-Dec-24  | -                  | ~25               |
| 01-Feb-25  | -                  | ~30               |
| 01-Apr-25  | -                  | ~35               |
| 01-Jun-25  | -                  | ~40               |
| 01-Aug-25  | -                  | ~50               |
| 01-Oct-25  | -                  | ~80               |
| 01-Dec-25  | -                  | ~75               |
| 01-Feb-26  | -                  | ~85               |
| 01-Apr-26  | -                  | ~60               |
| 01-Jun-26  | ~110               | ~80               |
</details>

<table><tr><td>Date</td><td>Stock Price (Rmb)</td><td>Price Target (Rmb)</td><td>Rating</td></tr><tr><td>2023-03-10</td><td>NaN</td><td>-</td><td>No Rating</td></tr><tr><td>2026-05-21</td><td>80.18</td><td>105.60</td><td>Buy</td></tr></table>

Source: UBS Global Research; LSEG Eikon as of 10-Jun-2026. All prices as of local market close. Ratings as of date shown.

Shenzhen Kedali Industry (Rmb)  
![](images/89cf3a1a283d9d098a9414f4da27fabb72c54df0e8172ef170200b9d615e5086.jpg)

<details>
<summary>line chart</summary>

| Date       | Price Target (Rmb) | Stock Price (Rmb) |
|------------|--------------------|-------------------|
| 01-Apr-23  | 180                | 120               |
| 01-Jun-23  | 180                | 125               |
| 01-Aug-23  | 180                | 120               |
| 01-Oct-23  | 180                | 110               |
| 01-Dec-23  | 180                | 100               |
| 01-Feb-24  | 120                | 60                |
| 01-Apr-24  | 120                | 70                |
| 01-Jun-24  | 120                | 80                |
| 01-Aug-24  | 120                | 70                |
| 01-Oct-24  | 120                | 80                |
| 01-Dec-24  | 120                | 90                |
| 01-Feb-25  | 180                | 120               |
| 01-Apr-25  | 180                | 110               |
| 01-Jun-25  | 180                | 120               |
| 01-Aug-25  | 180                | 130               |
| 01-Oct-25  | 180                | 150               |
| 01-Dec-25  | 240                | 170               |
| 01-Feb-26  | 280                | 180               |
| 01-Apr-26  | 280                | 190               |
| 01-Jun-26  | 280                | 180               |
</details>

<table><tr><td>Date</td><td>Stock Price (Rmb)</td><td>Price Target (Rmb)</td><td>Rating</td></tr><tr><td>2023-03-10</td><td>129.46</td><td>190.00</td><td>Buy</td></tr><tr><td>2023-04-17</td><td>141.89</td><td>195.00</td><td>Buy</td></tr><tr><td>2023-04-24</td><td>128.16</td><td>190.00</td><td>Buy</td></tr><tr><td>2023-10-27</td><td>85.59</td><td>172.00</td><td>Buy</td></tr><tr><td>2024-01-16</td><td>78.74</td><td>115.00</td><td>Buy</td>

[中间内容因长度限制已省略]

d Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/a2fc8462a9562ede9663fde3dfd3695571c59fa461ed37211ebb4e867ce1c47e.jpg)
"""
