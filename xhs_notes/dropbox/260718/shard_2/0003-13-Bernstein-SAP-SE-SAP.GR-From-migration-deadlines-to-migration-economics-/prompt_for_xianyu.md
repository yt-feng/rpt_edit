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
European Technology/Software

SAP SE

Rating

Outperform

Price Target

SAP.GR

276.00 EUR

![](images/c45e9866de225f6ebc25ed0df3c33ae5cedd5de1d6c29fa6dfc017c5388f2ca4.jpg)

Richard Nguyen
+33 1 42 13 54 22
richard.nguyen@bernsteinsg.com

![](images/fe41e7fc31e549914649e7257dfb1f25249684e1e8d71733e23fa414392ce2af.jpg)

Mark L. Moerdler, Ph.D.
+1 917 344 8506
mark.moerdler@bernsteinsg.com

![](images/5f79bc5c4cd04153b9f3dd1b1e9589a055870434c1881e279b561520e1a69714.jpg)

Derric Marcon
+33 1 58 98 06 30
derric.marcon@bernsteinsg.com

Specialist Sales

![](images/6b7d36b83c06d37e6d02ed7a9afc5678907d147dde330ee9e7122f551f292716.jpg)

Kiran Shah, CFA
+44 20 3547 1533
kiran.shah@bernsteinsg.com

# SAP: From migration deadlines to migration economics

SAP's maintenance moat is weakening, but its installed base remains highly defensible. Building on our report two days ago, SAP: The end of deadline-driven migration, which argued the European Commission ruling shifts bargaining power toward customers, we extend the analysis to assess the implications for maintenance economics and monetization. Our key conclusion is that customer maintenance optionality - not revenue substitution - is the real risk. While bargaining power shifts incrementally toward customers, we remain Outperform, as long-term value creation should depend more on cloud, AI and ecosystem monetization than on maintenance lock-in.

Customer leverage matters more than third-party support. At roughly \$1bn at most, the addressable revenue pool for third-party support providers remains small compared with SAP's €10.5bn maintenance business. The greater risk is increased customer negotiating power on maintenance, cloud pricing, migration incentives and contract terms.

The ruling creates multiple migration pathways. Rather than a linear ECC-to-S/4 transition driven by deadlines, customers now have more strategic options, including delayed migration, hybrid support models and selective use of third-party support. Migration timing and economics become more important than migration volumes.

Migration economics are becoming the key investor debate. Greater flexibility is likely to pressure pricing power through higher discounts, stronger incentives and lower maintenance pricing, even if migration demand remains intact.

Investment Implications

We remain Outperform. The ruling weakens SAP's contractual leverage but not its competitive position. ERP complexity, switching costs, AI, BTP and the broader SAP ecosystem should support continued conversion of the installed base into higher-value cloud solutions.

relationships.

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>SAP:GR (EUR)</td><td>6.10</td><td>7.54</td><td>9.02</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>Revenues (M)</td><td>36,800</td><td>40,638</td><td>46,491</td><td>12.4%</td></tr><tr><td>Operating Earnings (M)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Net Earnings (M)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Revenue/Share</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Operating Margin (%)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Net Income Margin (%)</td><td>19.5</td><td>21.2</td><td>21.4</td><td>--</td></tr><tr><td>EPS Growth (%)</td><td>36.0</td><td>23.5</td><td>19.6</td><td>--</td></tr></table>

<table><tr><td>Close Date</td><td>16 Jul 2026</td></tr><tr><td>SAP.GR Close Price (EUR)</td><td>140.70</td></tr><tr><td>Price Target (EUR)</td><td>276.00</td></tr><tr><td>Upside/(Downside)</td><td>96%</td></tr><tr><td>52-Week Range</td><td>267.10/130.62</td></tr><tr><td>EDME</td><td>1,598.24</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>1.8%</td></tr><tr><td>Market Cap (EUR) (M)</td><td>172,851</td></tr><tr><td>EV (EUR) (M)</td><td>171,173</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>(32.5)</td><td>(1.0)</td><td>(30.2)</td><td>(46.5)</td></tr><tr><td>EDME (%)</td><td>8.7</td><td>0.7</td><td>4.7</td><td>18.0</td></tr><tr><td>Relative (%)</td><td>(41.2)</td><td>(1.8)</td><td>(34.9)</td><td>(64.5)</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.  
Price Performance, 1YR

![](images/94f59c53d688ea321ed0b0daab6e36731c86a6f6a0d46663308f8ae1283ea17c.jpg)

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Adjusted P/E (x)</td><td>23.1</td><td>18.7</td><td>15.6</td></tr><tr><td>PEG Adjusted (x)</td><td>0.6</td><td>0.8</td><td>0.8</td></tr><tr><td>EV/Sales (x)</td><td>4.7</td><td>4.2</td><td>3.7</td></tr><tr><td>PEG Reported (x)</td><td>0.6</td><td>0.8</td><td>0.8</td></tr><tr><td>EV/EBIT (x)</td><td>16.2</td><td>14.0</td><td>12.0</td></tr><tr><td>Div Yield (%)</td><td>1.7</td><td>2.0</td><td>2.0</td></tr></table>

## Table Of Contents

Investment summary....2   
From migration deadlines to customer choice....4   
The European Commission ruling changes the balance of power....5   
The real threat is customer maintenance optionality, not third-party support....7   
Five strategic paths for SAP customers....9   
Why SAP's installed base remains defensible....13   
How SAP can preserve its economic moat....15   
The new investor debate: Monetization, not migration....17   
From migration volume to migration economics....20

## DETAILS

## INVESTMENT SUMMARY

SAP's maintenance moat is becoming more contestable, but its installed base remains highly defensible. Following the European Commission's ruling on SAP's maintenance practices, we revisit a debate that has largely focused on migration volumes and third-party support disruption. Our key conclusion is that investors are asking the wrong question. The primary risk is not maintenance revenue displacement, but increased customer optionality and negotiating leverage. While the ruling incrementally shifts bargaining power toward customers, we remain Outperform, as SAP's long-term value creation should depend more on cloud, AI, and ecosystem monetization than on maintenance lock-in.

The real risk is pricing power, not revenue substitution. Investors often focus on whether third-party support providers can materially erode SAP's maintenance revenues. We believe the direct revenue opportunity remains modest relative to SAP's c. €10.5bn maintenance base. However, the presence of credible alternatives strengthens customers' hand in negotiations short-term, not only on maintenance renewals but also on cloud pricing, migration incentives, and contractual flexibility. The debate should therefore move from revenue disruption to pricing power.

SAP still controls when they end-of-life their software. While customers could shift maintenance temporarily, SAP decides when they will cease to support and upgrade the older versions of their software. This means that while a customer could temporarily shift ECC support to a third-party provider, once SAP ceases to support ECC the customer has the decision of using software that will no longer be upgraded or enhanced by the developer. This means that the software will age out relatively quickly unless the customer - or the customer in conjunction with third-party supports - takes on the responsibility for upgrading and enhancing the software which can be an expensive venture and places the customer at risk of missing legal or regulatory requirements and more exposed if accounting or business issues arise. We would argue that while customers may move short term the pending end-of-life is a major overhang and business risk that has not disappeared with this agreement.

Customers also assume competitive risks related to not leveraging AI. The other problem that customers who decide to switch to third-party support is that they lose the option of leveraging SAP's AI - the customer must instead develop those AI functionalities themselves which are likely going to be more expensive both initially and to support.

SAP's installed base remains resilient. The ruling lowers barriers to alternative support models but does not reduce ERP complexity, switching costs, customization dependence, regulatory requirements, or reliance on SAP's roadmap. Industry feedback points to coexistence rather than wholesale maintenance abandonment. SAP also retains important defenses through AI, Business Data Cloud, BTP, licensing expertise, and its broader application ecosystem.

The ruling creates multiple migration paths. The market has generally assumed a linear transition from ECC to S/4 driven by support deadlines. We see a broader set of strategic options, including immediate migration, negotiated migration, hybrid support arrangements, prolonged ECC usage, and eventual ERP replacement (which has a very low probability). Importantly, the ruling changes the timing and economics of modernization decisions rather than the underlying need to modernize. Investors should focus less on whether customers migrate and more on when they migrate and under what terms.

Migration economics matter more than migration volumes. Greater customer maintenance flexibility is unlikely to change SAP's long-term migration opportunity, but it could pressure monetization through higher discounts (to expedite a customer's migration vs delaying longer and using third-party support temporarily), stronger incentives, and lower maintenance pricing. Given maintenance gross margins exceed 90%, even modest attrition could have an out-sized impact on earnings, shifting the debate from migration volumes to profit capture.

Investment conclusion. The ruling weakens SAP's contractual leverage, not its strategic position. The key question is no longer how many customers migrate, but how much value SAP captures from the transition. We believe SAP remains well positioned to convert its installed base into higher-value cloud relationships, supporting our Outperform rating despite greater customer optionality.

## FROM MIGRATION DEADLINES TO CUSTOMER CHOICE

The European Commission's recent ruling on SAP's maintenance practices has fundamentally changed the economics of SAP's installed base. In our previous report, SAP: The end of deadline-driven migration, we argued that the ruling incrementally shifts some bargaining power toward customers by allowing greater flexibility around support termination, landscape segmentation, and third-party support adoption. The debate is no longer whether customers will migrate to S/4, but when they migrate, under what commercial terms, and how much economic value SAP ultimately captures from the transition.

EXHIBIT 1: SAP ERP support deadline by software version

<table><tr><td>ERP software version</td><td>Mainstream maintenance (EoM)</td><td>Extended maintenance (EoE)</td><td>Default CSM on-premises</td><td>SAP Private Cloud offering S/4: SAP SafekeeperECC: SAP ERP private</td></tr><tr><td>ECC 6 EHP 0-5</td><td>2027</td><td>2027</td><td>2028</td><td>Not eligible</td></tr><tr><td>ECC 6 EHP 6-8</td><td>2027</td><td>2030</td><td>2031</td><td>SAP ERP, private edition, transition option 2033</td></tr><tr><td>S/4 Finance 1503 &amp; 1605</td><td>2025</td><td>NA</td><td>2026</td><td>2029</td></tr><tr><td>S/4 1709</td><td>2022</td><td>2025</td><td>2026</td><td>2027</td></tr><tr><td>S/4 1809</td><td>2023</td><td>2025</td><td>2026</td><td>2027</td></tr><tr><td>S/4 1909</td><td>2024</td><td>2025</td><td>2026</td><td>2027</td></tr><tr><td>S/4 2020</td><td>2025</td><td>NA</td><td>2026</td><td>2027</td></tr><tr><td>S/4 2021</td><td>2026</td><td>NA</td><td>2027</td><td>2028</td></tr><tr><td>S/4 2022</td><td>2027</td><td>NA</td><td>2028</td><td>2029</td></tr><tr><td>S/4 2023</td><td>2030</td><td>NA</td><td>2031</td><td>2032</td></tr></table>

CSM: Customer-specific maintenance  
Source: SAP, Gartner Group, Bernstein analysis

We believe the next phase of this debate is increasingly centered on SAP's maintenance revenues. Maintenance has historically been one of SAP's most attractive businesses: highly recurring, highly profitable (gross margin $>90\%$ ), and strategically important because it reinforced the migration path from ECC toward S/4 and cloud offerings. SAP generated €10.5bn of support revenue in 2025, representing one of the largest maintenance revenue streams across enterprise software.

At first glance, the threat from third-party support appears limited. Based on our estimates, SAP-related third-party support revenues for on-premises ERP solutions such as ECC may total approximately \$1bn at best. Roughly half of this opportunity is likely already captured by specialist third-party support providers such as Rimini Street, Spinnaker Support, Support Revolution and Origina, while the remaining half is likely serviced through large IT services providers such as TCS, Infosys, Cognizant, Accenture and Capgemini. Relative to SAP's €10.5bn maintenance revenue base, this does not suggest a material displacement threat to SAP's overall revenue model.

However, we believe this interpretation misses the more important implication. The significance of third-party support is not the absolute size of the market. Rather, it is the optionality that it creates for customers. Historically, customers faced meaningful barriers to leaving SAP support, including reinstatement fees, back-maintenance obligations and the difficulty of applying different support models across different parts of their SAP estate. The Commission's ruling materially lowers those barriers and transforms third-party support from a niche cost-optimization strategy into a credible negotiating tool. But it does not remove the legal, regulatory or business risks associated with not receiving constant upgrades and enhances.

As a result, customers now have a broader range of options than simply migrating to S/4 according to SAP's preferred timeline. They can selectively apply third-party support across their landscape, potentially combine SAP support and third-party providers, extend the life of stable ECC environments, optimize maintenance spending, negotiate improved migration incentives, or delay modernization until technical debt and business readiness improve. Industry feedback reinforces this view, positioning third-party support not only as a substitute for SAP maintenance but also as a provisional, supplemental, or contingent mechanism that allows customers to modernize at their own pace.

The key question is therefore not how much revenue third-party providers can capture from SAP. We think that the more important question is how customer behavior changes when maintenance is no longer an all-or-nothing decision. In this note, we examine the range of strategic paths available to SAP customers following the ruling, assesses which customer segments are most likely to adopt each option, evaluates the potential implications for SAP's maintenance economics, and analyzes the actions SAP can take to mitigate these risks and preserve long-term value creation.

## THE EUROPEAN COMMISSION RULING CHANGES THE BALANCE OF POWER

Historically, SAP maintenance was more than a support contract. It functioned as a strategic mechanism that reinforced customer dependence on the SAP ecosystem and increased the likelihood of an eventual migration to S/4. The value of maintenance was therefore not limited to incident resolution or software updates; it also helped secure SAP's future product adoption.

The recent European Commission ruling weakens this mechanism. While the decision does not fundamentally alter SAP's product strategy or customer relationships overnight, it reduces SAP's ability to use maintenance policies as a lever to influence long-term customer deci

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
