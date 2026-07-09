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
# Cheap, but fundamentally challenged; Reinstating Underperform and \$190 PO

Reinstating Coverage: UNDERPERFORM | PO: 190.00 USD | Price: 218.07 USD

## AI-driven disruption narrows Adobe's competitive moat

We are reinstating coverage of Adobe (ADBE) with an Underperform rating and a \$190 PO, based on 7x CY27E EV/FCF. We flag rising risk to the growth profile as generative AI (GenAI) lowers barriers to content creation and increases competition from lower-cost and AI-native alternatives. We believe some professionals will remain focused on pixel level control and continue to utilize Adobe's tools, but AI will likely displace large parts of the core market over time, with likely pressure on pricing and seat expansion. We see Adobe's own AI strategy as largely defensive, supporting engagement and retention but limited on its ability to generate incremental high-quality ARR at scale.

## Growth reacceleration unlikely in the near term

Our report is centered on a key question: can Adobe reaccelerate growth in the age of AI? Adoption across AI products is notable, but we see limited evidence it translates into meaningful ARR uplift, with AI-first ARR still representing $<2\%$ of total ARR. Risk is concentrated in lower-end and prosumer cohorts, where “good enough” AI output can substitute for paid workflows, while professional and enterprise use cases remain more resilient but not immune. At the same time, the shift toward freemium and consumption-based pricing introduces monetization risk. We expect growth to decelerate over time and model it to decline from 10.5% in 2025 to 8.8% FY27E, with no clear path to near-term reacceleration.

## Valuation is tempting, but no catalyst in sight

The stock trades at the low end of the peer group, at 8x CY27E EV/FCF, but valuation alone is insufficient to drive outperformance, in our view. Our 7x CY27E EV/FCF multiple reflects structurally slower growth and increasing uncertainty around monetization quality. We expect margins and FCF generation to remain strong, but see limited multiple expansion without clear evidence of AI monetization and growth acceleration.

<table><tr><td>Estimates (Nov) (US$)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EPS</td><td>18.43</td><td>20.95</td><td>24.40</td><td>27.54</td><td>31.08</td></tr><tr><td>GAAP EPS</td><td>12.37</td><td>16.70</td><td>17.55</td><td>19.99</td><td>23.27</td></tr><tr><td>EPS Change (YoY)</td><td>14.8%</td><td>13.7%</td><td>16.5%</td><td>12.9%</td><td>12.9%</td></tr><tr><td>Consensus EPS (Bloomberg)</td><td></td><td></td><td>24.38</td><td>27.30</td><td>30.71</td></tr><tr><td>Consensus EPS (Visible Alpha)</td><td></td><td></td><td>18.03</td><td>20.99</td><td>23.99</td></tr><tr><td colspan="6">Valuation (Nov)</td></tr><tr><td>P/E</td><td>11.8x</td><td>10.4x</td><td>8.9x</td><td>7.9x</td><td>7.0x</td></tr><tr><td>GAAP P/E</td><td>17.6x</td><td>13.1x</td><td>12.4x</td><td>10.9x</td><td>9.4x</td></tr><tr><td>EV / EBITDA*</td><td>7.4x</td><td>6.8x</td><td>6.2x</td><td>5.8x</td><td>5.4x</td></tr><tr><td>Free Cash Flow Yield*</td><td>9.1%</td><td>11.4%</td><td>11.9%</td><td>12.9%</td><td>14.1%</td></tr><tr><td colspan="6">* For full definitions of iQmethodSMmeasures, see page 21.</td></tr></table>

## 07 July 2026

Equity

Tal Liani
Research Analyst
BofAS
+1 646 855 5107
tal.liani@bofa.com

Eden Vacnich
Research Analyst
BofAS
+1 646 855 1971
eden.vacnich@bofa.com

Kevin Niederpruem
Research Analyst
BofAS
+1 646 855-1540
kevin.niederpruem@bofa.com

## Stock Data

<table><tr><td>Price</td><td>218.07 USD</td></tr><tr><td>Price Objective</td><td>190.00 USD</td></tr><tr><td>Date Established</td><td>7-Jul-2026</td></tr><tr><td>Investment Opinion</td><td>B-3-9</td></tr><tr><td>52-Week Range</td><td>190.12 USD - 386.60 USD</td></tr><tr><td>Mrkt Val (mn) / Shares Out (mn)</td><td>86,683 USD / 397.5</td></tr><tr><td>Free Float</td><td>99.8%</td></tr><tr><td>Average Daily Value (mn)</td><td>1683.91 USD</td></tr><tr><td>BofA Ticker / Exchange</td><td>ADBE / NAS</td></tr><tr><td>Bloomberg / Reuters</td><td>ADBE US / ADBE.OQ</td></tr><tr><td>ROE (2026E)</td><td>83.2%</td></tr><tr><td>Net Dbt to Eqty (Nov-2025A)</td><td>6.7%</td></tr></table>

## See Glossary on page 19

<table><tr><td>Company Sector</td></tr><tr><td>Software</td></tr></table>

## iQprofile $^{SM}$ Adobe

## iQmethod $^{SM}$ – Bus Performance\*

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Return on Capital Employed</td><td>37.6%</td><td>44.3%</td><td>46.6%</td><td>47.9%</td><td>47.8%</td></tr><tr><td>Return on Equity</td><td>54.1%</td><td>69.5%</td><td>83.2%</td><td>84.3%</td><td>79.7%</td></tr><tr><td>Operating Margin</td><td>46.6%</td><td>46.2%</td><td>45.0%</td><td>45.1%</td><td>45.0%</td></tr><tr><td>Free Cash Flow</td><td>7,873</td><td>9,852</td><td>10,323</td><td>11,161</td><td>12,245</td></tr></table>

## iQmethod $^{SM}$ – Quality of Earnings\*

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash Realization Ratio</td><td>1.0x</td><td>1.1x</td><td>1.1x</td><td>1.1x</td><td>1.1x</td></tr><tr><td>Asset Replacement Ratio</td><td>0.1x</td><td>0.1x</td><td>0.1x</td><td>0.1x</td><td>0.1x</td></tr><tr><td>Tax Rate</td><td>19.8%</td><td>18.4%</td><td>23.2%</td><td>23.2%</td><td>22.6%</td></tr><tr><td>Net Debt-to-Equity Ratio</td><td>-14.1%</td><td>6.7%</td><td>4.8%</td><td>-17.5%</td><td>-40.2%</td></tr><tr><td>Interest Cover</td><td>NM</td><td>41.8x</td><td>46.3x</td><td>49.4x</td><td>NM</td></tr></table>

Income Statement Data (Nov)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales</td><td>21,505</td><td>23,769</td><td>26,531</td><td>28,857</td><td>31,357</td></tr><tr><td>% Change</td><td>10.8%</td><td>10.5%</td><td>11.6%</td><td>8.8%</td><td>8.7%</td></tr><tr><td>Gross Profit</td><td>19,264</td><td>21,489</td><td>23,843</td><td>25,825</td><td>28,075</td></tr><tr><td>% Change</td><td>12.2%</td><td>11.6%</td><td>11.0%</td><td>8.3%</td><td>8.7%</td></tr><tr><td>EBITDA</td><td>11,852</td><td>12,928</td><td>14,104</td><td>15,225</td><td>16,343</td></tr><tr><td>% Change</td><td>11.4%</td><td>9.1%</td><td>9.1%</td><td>7.9%</td><td>7.3%</td></tr><tr><td>Net Interest &amp; Other Income</td><td>142</td><td>(15)</td><td>(62)</td><td>(108)</td><td>(45)</td></tr><tr><td>Net Income (Adjusted)</td><td>8,284</td><td>8,946</td><td>9,748</td><td>10,574</td><td>11,545</td></tr><tr><td>% Change</td><td>12.3%</td><td>8.0%</td><td>9.0%</td><td>8.5%</td><td>9.2%</td></tr></table>

## Free Cash Flow Data (Nov)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net Income from Cont Operations (GAAP)</td><td>5,560</td><td>7,130</td><td>7,013</td><td>7,676</td><td>8,645</td></tr><tr><td>Depreciation &amp; Amortization</td><td>1,833</td><td>1,942</td><td>2,155</td><td>2,224</td><td>2,224</td></tr><tr><td>Change in Working Capital</td><td>(165)</td><td>(167)</td><td>(264)</td><td>157</td><td>193</td></tr><tr><td>Deferred Taxation Charge</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Other Adjustments, Net</td><td>828</td><td>1,126</td><td>1,633</td><td>1,392</td><td>1,497</td></tr><tr><td>Capital Expenditure</td><td>(183)</td><td>(179)</td><td>(213)</td><td>(289)</td><td>(314)</td></tr><tr><td>Free Cash Flow</td><td>7,873</td><td>9,852</td><td>10,323</td><td>11,161</td><td>12,245</td></tr><tr><td>% Change</td><td>13.4%</td><td>25.1%</td><td>4.8%</td><td>8.1%</td><td>9.7%</td></tr><tr><td>Share / Issue Repurchase</td><td>(9,500)</td><td>(11,281)</td><td>(8,811)</td><td>(8,444)</td><td>(8,444)</td></tr><tr><td>Cost of Dividends Paid</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Change in Debt</td><td>0</td><td>(1,500)</td><td>0</td><td>0</td><td>0</td></tr></table>

## Balance Sheet Data (Nov)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; Equivalents</td><td>7,613</td><td>5,431</td><td>6,080</td><td>8,973</td><td>12,950</td></tr><tr><td>Trade Receivables</td><td>2,072</td><td>2,344</td><td>2,181</td><td>2,519</td><td>2,737</td></tr><tr><td>Other Current Assets</td><td>1,547</td><td>2,388</td><td>2,070</td><td>2,168</td><td>2,439</td></tr><tr><td>Property, Plant &amp; Equipment</td><td>1,936</td><td>1,873</td><td>1,506</td><td>897</td><td>251</td></tr><tr><td>Other Non-Current Assets</td><td>17,062</td><td>17,460</td><td>19,046</td><td>19,142</td><td>19,174</td></tr><tr><td>Total Assets</td><td>30,230</td><td>29,496</td><td>30,884</td><td>33,699</td><td>37,550</td></tr><tr><td>Short-Term Debt</td><td>1,499</td><td>0</td><td>1,843</td><td>1,843</td><td>1,843</td></tr><tr><td>Other Current Liabilities</td><td>9,022</td><td>10,200</td><td>10,797</td><td>12,061</td><td>13,452</td></tr><tr><td>Long-Term Debt</td><td>4,129</td><td>6,210</td><td>4,802</td><td>4,802</td><td>4,802</td></tr><tr><td>Other Non-Current Liabilities</td><td>1,475</td><td>1,463</td><td>1,622</td><td>1,717</td><td>1,753</td></tr><tr><td>Total Liabilities</td><td>16,125</td><td>17,873</td><td>19,064</td><td>20,423</td><td>21,850</td></tr><tr><td>Total Equity</td><td>14,105</td><td>11,623</td><td>11,820</td><td>13,276</td><td>15,701</td></tr><tr><td>Total Equity &amp; Liabilities</td><td>30,230</td><td>29,496</td><td>30,884</td><td>33,699</td><td>37,550</td></tr></table>

\* For full definitions of IQmethod $^{SM}$ measures, see page 21.

## Company Description

Adobe is a diversified software company providing cloud-based solutions across digital media, document workflows, and enterprise marketing. The company's core offerings include Creative Cloud, Document Cloud, and Experience Cloud, serving creative professionals, enterprises, and a broad base of prosumer and business users. Adobe's platforms are built around industry standards such as Photoshop and Acrobat, with increasing integration of AI capabilities across products.

## Investment Rationale

We see increasing risk to Adobe's growth trajectory driven by: 1) AI compressing barriers of entry for competition from point solutions and AI-natives, 2) slowing adoption with potential seat reduction in the core creative professional market segment, and 3) AI consumption may weigh on margins and profitability. This is balanced by: 1) large Creative Cloud subscriber base 2) distribution channel & marketing personnel 3) breadth & depth of the digital content and experience software suite.

## Stock Data

<table><tr><td>Average Daily Volume</td><td>7,721,867</td></tr></table>

## Quarterly Earnings Estimates

<table><tr><td></td><td>2025</td><td>2026</td></tr><tr><td>Q1</td><td>5.08A</td><td>6.05A</td></tr><tr><td>Q2</td><td>5.06A</td><td>5.97A</td></tr><tr><td>Q3</td><td>5.31A</td><td>6.08E</td></tr><tr><td>Q4</td><td>5.50A</td><td>6.30E</td></tr></table>

## Can growth reaccelerate in the GenAI era?

Adobe remains deeply entrenched across creative, document, and marketing workflows, and its products remain the standard for many creative professionals and enterprises. The install base gives Adobe meaningful advantages: broad distribution, strong brand recognition, workflow familiarity, high switching costs in professional use cases, and a large subscription revenue base.

However, the stock is down 70% since its 2024 peak (vs. +68% NASDAQ index) on growing concerns that GenAI could structurally disrupt Adobe's core value proposition by lowering the skill barrier for content creation, enabling cheaper and simpler AI-native competitors, and shifting value away from tools and toward models and workflows. This threatens Adobe's pricing power, seat-based revenue model, and growth durability. Even with solid AI product execution, the risk is that Adobe becomes less valuable in a world where creation is increasingly simplified, resulting in sustained growth slowdown.

The Company responded by introducing its own AI based solutions, and we see evidence of initial traction. In 2Q26, AI-first ARR more than tripled YoY to \~\$500mn and in 1Q26, generative credit consumption grew 45% QoQ. This traction remains early in the monetization cycle, representing less than 2% of total ARR, and we believe will unlikely drive meaningful growth reacceleration.

We frame our views across five key points in this report:

\- Asymmetrical risk of AI disruption across different customer segments: risk is highest in lower-end non-professional use cases, while professional and enterprise use cases remain more resilient, but not immune.

\- AI monetization is progressing, but not yet material: We see strong adoption across Firefly with +50% ARR growth QoQ, Acrobat and Express also saw +21% MAUs growth QoQ, and Creative Freemium MAUs were up +70% YoY However, this growth has not translated into meaningful ARR uplift or revenue acceleration as the company is focusing on freemium attach.

\- Cannibalization of legacy products: Progress in AI capabilities has begun to pressure paid assets and incremental seats, creating downside risk to higher-margin businesses. Adobe has acknowledged pressure on certain monetization vectors, including continued declines in Adobe Stock, though it does not quantify the impact. Looking ahead, we see broader risk to seat expansion and pricing as free or low-cost alternatives substitute for paid workflows.

\- Leadership departure adds execution risk at key AI transition: simultaneous CEO and CFO turnover heightens risk around strategy, continuity, and leadership stability.

\- Valuation is attractive, but the stock lacks catalysts given the fundamental challenges. Stock valuation already discounts slower growth and AI risk, and we believe downside risk is limited. However, the potential for AI monetization and growth reacceleration remains constrained, and we don't see a clear near-term catalyst for multiple expansion.

Our view: AI risk is real; low valuation is insufficient for a more positive view

Current valuation reflects 8x CY27E EV/FCF, compared to historical range of \~25-30x. We also flag strong operating margins of 45% and FCF margins of 39%, supporting robust FCF generation. Nevertheless, we reinstate coverage with an Underperform rating, as we believe the company will face challenges to maintain its base due to AI disruption, which could pressure a large part of its revenue base. We believe the company will have difficulty converting its AI innovation to meaningful ARR contribution, and that the current AI growth is mostly related to Freemium attach rather than new product monetization.

The key issue is both adoption and economics, in our view. We see Adobe's AI strategy as largely defensive and believe structural disruption makes recovery challenging. We see the market as fabricated to a small group of power users who require pixel-based control and the unique tools Adobe is providing, and a larger group of occasional users, where AI represents a serious risk of displacement and migration to cheaper AI-native solutions, which brings up potential risks to the number of seats, and potential cannibalization of high-margin legacy revenues.

## Eroding moat in the age of AI

Advancements in GenAI capabilities lower the barriers of entry for creative software, and we see clear evidence of pressure on growth.

Subscription revenues account for 97% of total revenues, and until FY26 were reported in two segments: Digital Media (\~75% of sub revenue) and Digital Experience (\~25%). The Company no longer provides this disclosure and now reports subscription revenue across two customer-oriented groups: Creative & Marketing Professionals (\~71% of sub revenue) and

[中间内容因长度限制已省略]

barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.
"""
