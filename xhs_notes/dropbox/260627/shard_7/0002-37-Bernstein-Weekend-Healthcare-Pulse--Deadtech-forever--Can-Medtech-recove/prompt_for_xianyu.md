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
# Weekend Healthcare Pulse: Deadtech forever? Can Medtech recover?

Lee Hambright +1 917 344 8429 lee.hambright@bernsteinsg.com

Courtney Breen +1 917 344 8407 courtney.breen@bernsteinsg.com

Nandan Kulkarni +91 22 6842 1436 nandan.kulkarni@bernsteinsg.com

Delphine Le Louet +33 1 42 13 92 93 delphine.le-louet@bernsteinsg.com

Rebecca Liang, Ph.D. +852 2123 2656 rebecca.liang@bernsteinsg.com

Susannah Ludwig +41 582 723 127 susannah.ludwig@bernsteinsg.com

William Pickering, MD +1 917 344 8340 william.pickering@bernsteinsg.com

Justin Smith +44 20 7762 5899 justin.smith@bernsteinsg.com

Miki Sogi, Ph.D. +81 3 6777 6991 miki.sogi@bernsteinsg.com

Lance Wilkes +1 917 344 8501 lance.wilkes@bernsteinsg.com

Jeffrey Walch, MD, Ph.D. +1 917 344 8613 jeffrey.walch@bernsteinsg.com

## Specialist Sales

Christian Moore +1 917 344 8555 christian.moore@bernsteinsg.com

U.S. Medtech stock performance has been abysmal. Our coverage has underperformed the S&P by 4600bps over the past year (Exhibit 1), and the medtech sector multiple has compressed by $30\%$ since November (Exhibit 2). While investors worry about several macro factors (slowing utilization, margin pressure, GLP-1 impact), we believe medtech weakness is more about single-stock stories that have gotten more complicated. In today's note, we reflect on some of the complications that have crept into medtech stock stories. Medtech fundamentals remain solid, in our view, and per Exhibit 4, valuations have come in dramatically for most of our coverage. For investors who are willing to live with stories that have a bit of hair on them, we see very attractive risk/reward for many quality medtech names across our coverage.

\- By Lee Hambright and Adam Chow

EXHIBIT 1: Over the last 12 months, U.S. Medtech has underperformed the S&P (by 4600bps!) and has lagged all other healthcare subsectors  
US Healthcare Stock Performance  
![](images/d7f019005b12cc054c6d738bf7d96ccab8ae7baa7856a461d321b43902d4b3ec.jpg)  
Equal weight based on Bernstein large-cap US coverage by sector; US Medtech includes ABT, BSX, DXCM, EW, ISRG, MDT, PODD, SYK, ZBH Source: Bloomberg; Bernstein analysis (25-Jun-2026 close)

U.S. Medtech stock performance has been horrendous. Over the last year, U.S. Medtech has underperformed the S&P 500 by just under 5000 bps (see Exhibit 1), making it the worst subsector within healthcare by a wide margin. The P/E multiple for the sector has been slashed by 30% over the last \~6 months (see Exhibit 2). Within our coverage, most stocks are down significantly year to date, with BSX and PODD as the most notable underperformers (Exhibit 3).

EXHIBIT 2: U.S. Medtech P/E multiples are down $30\%$ since November 2025. We haven't seen these levels sustainably since before 2017  
U.S. Medtech (S5HCEP\*) Price/Earnings Ratio (1BF)  
![](images/6b4da61d4c67bd30850e2abf147e55439ce36ad2982316b791aeb75668d1bbfe.jpg)  
Source: Bloomberg (S&P 500 Health Care Equipment Index; cap-weighted average of ABT, BAX, BDX, BSX, DXCM, EW, GEHC, IDXX, ISRG, MDT, PODD, RMD, STE, SYK, ZBH)

EXHIBIT 3: Year to date, BSX and PODD have been the worst performers in our coverage  
U.S. Medical Devices Stock performance; 2026 YTD  
![](images/133b2d5599e8ab65fbbb52bea38b454def786cfe3690abe7611cf85830b7c757.jpg)  
Source: Bloomberg; Bernstein analysis (25-Jun-2026 close)

## HOW DID WE GET HERE?

What's driving this weakness for medtech stocks? What has changed? As medtech multiples plunge to 10-year lows, investors have been questioning whether something is fundamentally wrong with the sector. Could procedure growth be slowing down? Will inflation (e.g., oil, resins, memory/semiconductors) put pressure on margins? Could GLP-1 growth disrupt medtech markets?

These are all red herrings, in our view. We see nothing wrong with medtech fundamentals. The problem for medtech, in our view, is more about stories. As investors remain captivated by AI-related stories, the stories for historically strong medtech stocks have gotten increasingly complicated. And in a world where a narrow set of AI winners are driving incredibly strong returns, investors have very little patience for complicated medtech stories.

## INCREASINGLY COMPLICATED STORIES

Stories have become increasingly complicated for many medtech stocks. Boston Scientific (BSX) has had a particularly dramatic fall from grace, and we attribute a fair amount of sector weakness to BSX's collapse. But sadly, BSX is not alone. Below, we summarize several medtech stock stories that have grown increasingly complicated over the past year.

Boston Scientific (BSX). BSX's P/E multiple has been slashed from a high of over 36x in early 2025 to 12.5x today. After establishing itself as a reliable high-single-digit grower, BSX's organic growth shot up to 16% (!) in both 2024 and 2025, driven primarily by two key franchises: Farapulse (PFA) and Watchman (LAAC). Watchman revenue doubled from \~\$1bn in 2022 to \~\$2bn in 2025, and Farapulse drove BSX's EP business to quadruple from \$800mn in 2023 to \$3.3bn in 2025. After CMS reimbursement coding for concomitant Farapulse+Watchman procedures went live Oct 2024, concomitant procedures drove Watchman organic growth from 18% in 3Q24 to a peak of 35% in 3Q25. Investor concerns about PFA competition started to percolate during the course of 2025 as BSX EP growth began to decelerate. Then in 4Q25, BSX U.S. EP sales missed consensus by 6%, and Watchman organic growth inflected from its peak of 35% to 29%. Both franchises continued to decelerate in 1Q26 and Urology growth was weak on Axonics integration hiccups, leading to a dramatic guidance cut after Q1, where FY26 organic growth was cut from 10%-11% to 6.5%-8.0% (see our 1Q26 recap). It was a gutsy move for management to cut the FY26 guide after one quarter of a new 12-quarter long-range plan (for 10%+ organic growth) issued in Sep 2025. Just 5 weeks after the 1Q26 call, BSX lowered Watchman expectations again at our Bernstein Strategic Decisions Conference (see our BSX SDC recap). Additional complications to the story include a couple of controversial deals: the \$14.5bn Penumbra acquisition in January (larger than the typical tuck-in deals to which investors have become accustomed) and the \$1.5bn MiRus investment in May (which triggered investor skepticism given BSX's two previous high-profile failures in TAVR).

Abbott (ABT). In 4Q25, sales growth slowed to $3.0\%$ organic (a $3\%$ miss), driven largely by an unexpected $9\%$ decline in ABT's Nutrition business (missed by $12\%$ ) (see our 4Q25 recap). The decline was driven by price cuts (primarily in the Adult segment) and infant formula market share losses stemming from the loss of a large WIC contract in 3Q25. Abbott had been raising Nutrition prices since 2022 in an attempt to offset higher manufacturing costs, but those increases began to weigh on volume. Management took price down in the quarter to address this and guided the Nutrition business to a challenged 1H26 with a return to growth in 2H26. The story did not get any cleaner in 1Q26, as sales ex-Exact acquisition and other adjustments continued growing slowly at \~3.0% organic. ABT's continuous glucose monitor (CGM) sales continued to decelerate (on market weakness + ABT recall in 4Q25) and the company's Structural Heart division lost market share (see our 1Q26 recap). ABT has dropped \~26% YTD.

Stryker (SYK) suffered a cyberattack on March 11 which disrupted global operations. Although the company primed investors for disappointing Q1 results through a series of 8-Ks, the disruption impacted Q1 sales more heavily than expected. Organic growth landed at 2.4% in 1Q26, 5% short of consensus, as the cyberattack delayed revenue recognition and disrupted manufacturing and supply chain operations. Management reiterated FY26 guidance on revenue-recognition tailwinds and backlog recovery on capital equipment. However, some investors remained concerned that the severity of the disruption could make guidance difficult to achieve, particularly now that 2H26 expectations call for 11% organic growth (see our 1Q26 recap). SYK has dropped \~10% YTD.

Insulet (PODD) has been a popular short since the company's November 2025 investor day, as investors worry about competitive patch pumps and potential price pressure in the pharmacy channel. PODD shares came under more pressure when the company announced a voluntary medical device correction on March 12 (see 8-K), identifying a manufacturing issue whereby certain pods from specific lots may have a small tear in the internal tubing that delivers insulin. The issue can lead to insulin leaking inside the pod rather than being fully infused in the body. At the time, Insulet had received 18 reports of serious adverse events associated with high blood glucose levels, including hospitalization and diabetic ketoacidosis (DKA), and no deaths had been reported. The company informed users about affected lots (pods involved amounted to \~1.5% of annual Omnipod 5 production globally) and offered replacement pods at no cost to users. On April 10, PODD confirmed 11 additional adverse events (bringing the total to 29) and no deaths associated with the manufacturing issue. On April 29, the FDA mischaracterized the manufacturing issue as having resulted in "476 serious injuries and no deaths," further hitting the stock by -12.5% on the day (see our thoughts on the March 12 recall and follow-ups). On May 26, the company announced a separate voluntary medical device correction, identifying a manufacturing issue that resulted in 24 reports of serious adverse events (no deaths) and affected \~8.5% of 2025 Omnipod 5 production. PODD has fallen \~46% YTD.

Medline (MDLN) reported strong revenue growth results in their first full quarter after their IPO, but adj EBITDA of \$776mn missed consensus (\$784mn) by 1% (see our 1Q26 recap). Management explained that the team had decided to accelerate investments in the business given strong revenue performance, but the small

EBITDA miss carried outsize weight given market expectations that companies should execute cleanly in their first full quarter as a public company, and MDLN shares plunged by 12% before settling at -7.3% on the day. An FDA recall on April 17, FDA warning letter on May 28, news of a fire destroying a California distribution center on June 12, and general concerns about oil prices and sponsors selling down their positions have also put pressure on the name. MDLN has dropped \~10% YTD.

Medtronic (MDT) was the top-performer in medtech in 2025, but the story has become a bit more complicated this year. Disappointing long-term data released in February was a setback for MDT's TAVR business, and the March IPO of MiniMed (MMED, not covered) fell short of the company's expectations. FY27 is a high-stakes year for MDT, as the company needs to capitalize on several high-profile launches including Affera, RDN, Altaviva, and Hugo. After weaker EPS growth over the past 4 years (-5%, -2%, +6%, +1%), MDT needs to pull it all together in FY27 and deliver real EPS growth. MDT has fallen \~16% YTD.

Intuitive Surgical (ISRG) continues to deliver strong financial performance, with 1Q26 sales growth of 23% and EPS growth of 38%, both strong beats vs. consensus (see our 1Q26 recap). Forward estimates continue to move up, but the multiple has been dragged down by weakness across the medtech sector. When BSX was trading at a 35x P/E multiple, investors didn't mind paying 70x or more for ISRG. But with BSX at 12.5x, some investors worry that ISRG looks expensive at 36x. Fundamentals have been strong, but as the share price has struggled, investors ponder questions about the durability of procedure growth, remanufactured instruments, Chinese competitors, and new systems from MDT and JNJ. ISRG is down \~29% YTD.

## IS THERE SOMETHING WRONG WITH MEDTECH FUNDAMENTALS?

With such notable, sustained weakness across the majority of stocks in the medtech sector, investors have understandably wondered whether there's something fundamentally wrong with the space. Several thematic factors have been teed up as possible explanations for sector weakness. As we noted above, we believe these are all red herrings. We believe the problem is more about single stock stories getting more complicated across the group. We discuss a few of these thematic factors below.

Slowing utilization growth. Hospital utilization has been strong for some time, and investors worry utilization growth could slow at some point, perhaps driven in part by some people getting kicked off insurance (ACA exchanges and Medicaid) and losing access to certain procedures. Some large hospital systems have speculated that utilization growth may begin to decelerate in 2H26. Medtech companies have told a different story, with teams fairly unanimously reporting continued strength in underlying procedure growth despite some mostly immaterial weather-related impact in 1Q26:

"What I will say in terms of the underlying market is that it's solid and underlying demand is what we expected. Now we did see some procedural softness early in the quarter, but nothing that we would define really as material. While certain regions, particularly here in the U.S., you will recall we experienced some periods of severe weather in late January and early February, that was largely consistent with normal seasonal patterns" - JNJ 1Q26 call

"Turning to the environment, underlying demand across our businesses remained healthy in Q1, even as the cyber incident created operational disruption. Procedural volumes were solid, supported by favorable demographics and the continued adoption of robotic assisted surgery. The hospital CapEx environment also remains steady, and our capital order book remains elevated as we enter the remainder of the year." - SYK 1Q26 call

Hospitals and MCOs saw a bit of softness in 1Q26 due to a mild flu season and weather-related disruptions, but most are calling for stable growth in utilization overall:

"As we monitor underlying utilization trends, they remain consistent with the high levels we saw in the prior year. At this distance, we anticipate trend to remain at the anticipated levels for 2026." - UNH 1Q26 call

Margin pressures. The Iran conflict led to a period of higher freight costs and created supply chain issues and gross margin concerns (e.g., higher resin prices). Higher input costs for semiconductors and memory has raised concerns as well. Investors remember that medtech stocks did not fare well during inflation concerns in 2022, and they worry inflation could continue to cause problems for the group. So far, medtech companies appear unfazed by these margin pressures:

"As it relates to oil costs, I mean I think that's an impact that it's too early to tell. We're not seeing any of that in our cost right now. We're not seeing freight rates increase from our suppliers right now." - ABT 1Q26 call

"Today, we have seen no material supply disruptions, a minor freight cost increase in the quarter that we're able to absorb. From a supply standpoint, most of our key products are dual-source, if not three sources. We got at least one year of pulling, so this is not something that we're concerned about. So, we're not seeing any distribution challenges there. So, again, so far, life is good." -ZBH 1Q26 call

GLP-1 impact. Growing access to weight loss medications has raised questions about impact on medical device businesses, particularly in certain end markets (e.g., bariatric surgery, diabetes, OSA). We all remember the impact on medtech stocks in 2H23, and though most medtech stocks recovered and have appeared to shrug off GLP-1-related fears, growing access to oral weight loss

drugs could revive concerns.

## WHAT CAN GET MEDTECH GOING AGAIN?

As we explain above, we 

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
