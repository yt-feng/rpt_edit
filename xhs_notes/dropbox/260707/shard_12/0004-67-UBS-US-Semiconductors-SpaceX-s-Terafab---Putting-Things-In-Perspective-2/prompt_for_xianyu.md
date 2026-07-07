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
# US Semiconductors SpaceX's Terafab - Putting Things In Perspective

## The What, Why, and When of Musk's Terafab plans

In conjunction with UBS' initiation of SpaceX (covered by John Hodulik), we outline the size, scale, and potential impact to the broader Semi Equipment supply chain. While it is fair to question the magnitude, Elon Musk has set forth a clear vision to build a vertically integrated semiconductor complex capable of producing terawatt-scale AI compute to resemble what has been demonstrated with Tesla's battery strategy (i.e., the Gigafactory). In that case, when the industry could not meet Tesla's battery capacity requirements in 2014, the company effectively built its own fully integrated battery production supply chain. Similarly, Terafab appears to target the full semiconductor complex including mask shop, leading foundry/logic & memory process flows, packaging and testing, all under one roof - enabling rapid "design/build/test/redesign" cycles (Figure 1). Importantly, we believe our supply chain datapoints appear more credible than many investors still seem willing to underwrite. Grimes County (TX) public hearing notices, recent executive hires and an extensive list of Terafab-related process engineering jobs are now being further substantiated by our discussion with equipment suppliers indicating orders having been placed for a pilot line that looks to us to be something in the \~\$5B range in C2027. Taken at face value, Terafab will essentially grow to something in the range of TSMC's scale in terms of WFE within 4-5yrs - obviously, a huge game changer for how high WFE can go over the coming years and putting \$300B + WFE in sight for C2029. We expect this to be a major theme over the next few earnings seasons as the project takes shape and tool orders are placed.

## WFE math for Terafab - A new >\$50B/yr WFE spender

UBS' analyst John Hodulik forecasts SpaceX's AI business alone (ex-Connectivity and ex-Launch segments) to spend a total of \~\$1.1T in capex over the next 5yrs, with \~20% of this capex (or \~\$225B) dedicated to Terafab. Assuming the typical 60% capex split to WFE, this would imply \~\$135B in WFE spend over the next 5yrs - about the size of the entire global WFE TAM this year. Because this will grow over time and start with a pilot line that we believe to be in the \~\$5B range for C2027 and grow to \~\$10B in C2028 (already assumed in our \~\$250B WFE for '28), the math would suggest that Terafab's WFE spending would have to grow above \~\$50B/yr in the C2030/2031 timeframe - which is akin to adding spending in the same ballpark as TSMC's WFE spend over the next few years. Based on the magnitude of the investment and existing filings thus far (specifically, plans that outline an initial \$55B semiconductor fab investment by SpaceX with the potential to expand to \$119B if all planned phases are completed (all in Grimes County, TX)), we infer SpaceX could be initially planning for a very large fab cluster - potentially something in the range of \~80k wsm for memory and two \~20k wsm foundry/logic fabs, alongside a mask shop and back-end test/assembly capacity. Our assessment is based on Intel's Ohio project (leading-edge greenfield fabs without a pre-existing semiconductor ecosystem) which initially carried an estimated \~\$28B investment and, similarly, Boise ID1 fab requiring a \~\$15B investment (for \~80k wsm of capacity). We would note that Terafab has indicated an initial focus on memory prior to building out other capabilities - we discuss this more in light of the fact that it has already engaged with INTC (see below). This is all consistent with our recent checks suggesting that INTC may be helping it to secure some slots at toolmakers. Ultimately, even if part of the potential Terafab WFE spend was to materialize, it would reinforce our long-held conviction (here) that industry WFE could approach \~\$300B by C2029.

## Read to INTC + Memory suppliers (MU/SK Hynix/Samsung)

We think of INTC's engagement with SpaceX as potentially serving as the "knowledge owner" in the Terafab - in other words, being potentially structured as a technology licensing arrangement, similar to historical models such as the IBM-AMD technology

## Equities

Americas
Semiconductors

Timothy Arcuri
Analyst
timothy.arcuri@ubs.com
+1-415-352 5676

Gianmarco Vella
Associate Analyst
gianmarco.vella@ubs.com
+1-415-352 4555

Alex Kivali
Analyst
alex.kivali@ubs.com
+1-212-713 3945

Natalia Winkler, CFA
Analyst
natalia.winkler@ubs.com
+1-415-352 4626

Aaryan Wadhwa
Associate Analyst
aaryan.wadhwa@ubs.com
+1-212-821 6481

transfer framework that ultimately supported GFS. Under such a structure, INTC could provide access to process flows, manufacturing IP, PDKs, design rules, tool recipes, and potentially operational know-how, while retaining ownership of the underlying technology and collecting a license/royalty payments. Another potential scenario (upon successful pilot) could be INTC dedicating an entire site to Terafab in a JV format. This could be its "Ohio One" site, which is large enough to support two (2) leading-edge fabs - as one of Terafab's campuses. We could also foresee a scenario in which SpaceX invests in INTC further down the road, with the likelihood increasing if Terafab ultimately proved unsuccessful. On the memory front, Musk's comments (Figure 1) explicitly call out memory as part of the effort, although a lot of questions remain unanswered here - most notably, we are unclear where Terafab would source memory IP and see limited incentives for existing memory suppliers to license their IP. However, the emergence of another potential supplier capable of producing memory at scale - if successful - could ultimately prompt Korean companies to invest in US front-end manufacturing for memory (more likely for DRAM – more here), also noting that, for example, Samsung has ample land available to add capacity in Taylor, TX. Overall, we continue to view this development as supportive of SPE suppliers.

Figure 1: Notable comments from the Terafab presentation (Mar-2026)

<table><tr><td>Topic</td><td>Commentary</td></tr><tr><td>Today&#x27;s compute capacity</td><td>The current output of AI compute is roughly 20 GW per year [...] we need to build the terafab because all of the rest of the output from Earth is about 2% of what we need. So if you add up all the fabs on Earth combined, they&#x27;re only about 2% of what we need for the terawatt project or Terafab project.</td></tr><tr><td>Capacity expansions by TSMC, Samsung, Micron</td><td>[...] to be clear, we&#x27;re very grateful to our existing supply chain — to Samsung, TSMC, Micron and others. And we would like them to expand as quickly as they can. [...] But there&#x27;s a maximum rate at which they&#x27;re comfortable expanding, but that rate is much less than we would like. And so we either build the terafab or we don&#x27;t have the chips and we need the chips so we&#x27;re going to build the terafab. And we&#x27;re starting off with an advanced technology fab here in Austin.</td></tr><tr><td>100-200GW of Terrestrial compute, rest in Space</td><td>[...] for the space compute my guess is that is the vast majority of the compute because you&#x27;re power constrained on Earth. That&#x27;s why I think it&#x27;s probably 100-200 GW a year of terrestrial chips and probably on the order of a terawatt of chips in space. Just because of power constraints on the ground is probably how it ends up.</td></tr><tr><td>Silicon for Inference first, and then Space</td><td>[...] we expect to make two kinds of chips. One will be optimized for edge inference. So that&#x27;ll be used primarily in Optimus [...] because I expect the robots — humanoid robots — to be made 10 to 100 times more than the volume of cars. [...] And then we need a high power chip that is designed for space. [...] It&#x27;s a hostile environment in space. So you want to design the chip — you want to optimize it for space. And you also want to generally run it a little hotter than you would normally run a chip on Earth to minimize the radiator mass.</td></tr><tr><td>Logic, Memory, Packaging, Test, Masks</td><td>In the advanced technology fab, we will have all of the equipment necessary to make a chip of any kind, logic or memory, and we will also have all of the equipment necessary to make the lithography masks. So in a single building we can create a lithography mask, make the chip, test the chip, make another mask and have an incredibly fast recursive loop for improving the chip design [...] you&#x27;ve got everything necessary [...] and just keep looping it</td></tr></table>

Source: Company Presentation

## Valuation Method and Risk Statement

We use various valuation techniques such as P/E, EV/FCF for valuing the companies in this report. Risk factors include but are not limited to macroeconomic factors such as a downturn in the economy, a disruption of international trade, technological disruption due to new inventions, or business model innovation whereby structural changes in the industry alter the future course of unit sales, ASPs, and revenues.

## Intel Corp.:

Our PT is based on a SOTP analysis of the five contributing segments (Intel Products, Intel Foundry, Altera, Mobileye and All Other) each one valued using a tailored P/S multiple applied to F2026E revenues. NVDA has built a formidable moat for new compute-intensive workloads in the data center and could ultimately leverage its GPU architecture to more broadly displace INTC. New client and server CPUs from AMD also present a threat that we could be underestimating.

## SpaceX:

Our price target is SOTP and multiples based. Risks include dependence on Elon Musk as a key decision-maker, delays in achieving technological milestones, failure to scale and monetize AI initiatives, regulatory, geopolitical, and competitive pressures, and high capital intensity with execution risks around supply chains and unproven space-based compute models.

## Required Disclosures

This document has been prepared by UBS LLC, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 07 July 2026 04:05 AM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>55%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 30 June 2026.  
1: Percentage of companies under coverage globally within the 12-month rating category.

2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE): Exceptions to the standard +/-6% bands may be granted by the Investment Review Consultation (IRC). Factors considered by the IRC include the stock's volatility and the credit spread of the respective company's debt. As a result, stocks deemed to be very high or low risk may be subject to higher or lower bands as they relate to the rating. When 

[中间内容因长度限制已省略]

 is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
