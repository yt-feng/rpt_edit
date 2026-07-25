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
Global Aerospace & Defense

GE Aerospace

Rating

Outperform

Price Target

GE

421.00 USD (405.00 OLD)

![](images/e0493b98c40a00aea4eee1de62ad4d2a52569dad76c1e6e1991b122560f249fd.jpg)

Douglas S. Harned, Ph.D.
+1 917 344 8430
douglas.harned@bernsteinsg.com

![](images/d9a472d256fc42ea5650c3bf656fb592200f7bcd80f8b382eca9765bc07efd53.jpg)

Adrien Rabier
+44 20 7676 6820
adrien.rabier@bernsteinsg.com

![](images/0f1a5f00ec3a11643f131a108708af5ff26c88e5ff19b1c7317e5c4cdc73e728.jpg)

Nestor Wester
+44 20 7676 7067
nestor.wester@bernsteinsg.com

Specialist Sales

![](images/f0039406b22bd98ab19b89392af2bbaaaa44675f465bc4cfcfcf308b4f69b3a2.jpg)

Steve Song
+1 917 344 8401
steve.song@bernsteinsg.com

# GE Aerospace: Strength continues; Another big beat for Q2 - But, this time also a raise plus a positive Farnborough

GE Aerospace beat consensus and our estimates when they reported Q2 on July 16. Unlike the beat in Q1, GE this time raised guidance for the year, as confidence in the outlook appears stronger. Although there is still uncertainty regarding the outcome of the war in Iran and its effect on fuel prices, assumptions are (including ours) that the worst is likely over for fuel. Economic conditions remain solid, which is most important. The guide for reaching the high end of 2,300-2,400 shop visits for CFM56 in 2026 and 2027 was positive. We expect CFM56 shop visits to remain at these levels through 2030.

GE shares fell after reporting, which we attribute to expectations for a perfect quarter (which it largely was). One concern we heard was that service orders were down relative to Q1. But, we did not see an issue here, with orders up 22% YoY and shop visit backlogs already extended on each platform. The Farnborough Air Show has been positive for GE, including a 1,000 engine order from IndiGo.

In Commercial Engine & Services, we raise our estimates for widebody services, with more shop visits, heavier workscopes on the GE90, higher content and improved pricing on the GEnx. On narrowbodies, we expect better pricing on LEAP contracts signed after 2021 (shifting to time & materials) to flow to revenue from 2028/2029 onward. For CES OE, we have increased our LEAP delivery forecast in the outer years as Boeing raises 737 MAX production rates. DP&T should benefit from defense aftermarket activity and rising sustainment spending.

## Investment Implications

We maintain Outperform rating for GE and raise our target to \$421, up from \$405. The change comes from a stronger growth outlook for both CES and DPT.

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>GE (USD)</td><td>6.37</td><td>7.83</td><td>9.16</td></tr><tr><td>OLD</td><td>--</td><td>7.59</td><td>8.82</td></tr></table>

<table><tr><td>Close Date</td><td>22 Jul 2026</td></tr><tr><td>GE Close Price (USD)</td><td>341.19</td></tr><tr><td>Price Target (USD)</td><td>421.00</td></tr><tr><td>Upside/(Downside)</td><td>23%</td></tr><tr><td>52-Week Range</td><td>382.97/254.66</td></tr><tr><td>SPX</td><td>7,498.96</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>0.6%</td></tr><tr><td>Market Cap (USD) (M)</td><td>354,006</td></tr><tr><td>EV (USD) (M)</td><td>401,955</td></tr></table>

<table><tr><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>Revenues (M)</td><td>45,855</td><td>53,145</td><td>58,872</td><td>13.3%</td></tr><tr><td>FCF (M)</td><td>7,302</td><td>8,687</td><td>9,990</td><td>--</td></tr><tr><td>Reported EPS</td><td>8.07</td><td>8.64</td><td>10.43</td><td>--</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>10.8</td><td>(3.9)</td><td>15.7</td><td>31.7</td></tr><tr><td>SPX (%)</td><td>9.5</td><td>0.4</td><td>8.5</td><td>18.8</td></tr><tr><td>Relative (%)</td><td>1.2</td><td>(4.3)</td><td>7.2</td><td>12.9</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

![](images/ecba5d9c19cffa6acd4e6ef200862bf7f0e3aa2b6dda9d6f9bab6148eacbd7f2.jpg)  
Price Performance, 1YR

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Adjusted P/E (x)</td><td>53.6</td><td>43.6</td><td>37.3</td></tr><tr><td>EV/EBITDA (x)</td><td>39.2</td><td>33.3</td><td>28.8</td></tr><tr><td>EV/EBIT (x)</td><td>39.8</td><td>37.3</td><td>31.1</td></tr><tr><td>FCF Yield (%)</td><td>2.00</td><td>2.43</td><td>2.83</td></tr></table>

## DETAILS

In Q2, GE beat consensus revenues and earnings. Guidance was raised for 2026 with adjusted revenue growth expected in the high-teens range (previously LDD). CES revenue expected to grow in the \~20% range which is up from prior midteens guidance. We raise our 2026 and 2027 adj EPS estimates to \$7.83 and \$9.16 from \$7.59 and \$8.82, primarily from a better outlook at both CES (largely from widebody services) and DP&T.

Our outlook for widebody services revenue has been revised upward, reflecting increased revenue contributions from both the GE90 and GEnx. We expect GE90 shop visits to continue to grow through 2030. With roughly 70% of the GE90 fleet yet to undergo its second, higher-value shop visit, the mix shift toward heavier workscopes should support aftermarket growth. For the GEnx program, we expect services revenue to grow in the mid-teens range between 2025 and 2030, driven by higher shop visit volumes, increasing workscope content, and improved pricing.

For CES OE, we have increased our LEAP delivery forecast in the outer years as Boeing raises 737 MAX production rates. We model rate increasing from 52 to 57 per month in Q2 2028 and from 57 to 62 per month in Q2 2029, and then from 62 to 65 per month in Q2 2030. We have raised CES margins in the outer years, as we now expect GE9X losses to peak in 2028 and subsequently decline, driven by lower losses per engine as production volumes increase.

Defense continues to have a strong backlog with solid growth ahead. 30% of this business is in international markets. We have raised our revenue estimates for DP&T, as we expect the business to benefit from defense aftermarket activity and rising sustainment spending.

## Q2 EARNINGS

Guidance was raised for 2026 with adjusted revenue growth expected in the high-teens range (previously LDD). For the CES segment, GE's new 2026 revenue growth stands at +20% growth, up vs prior guide of mid-teens. The primary difference comes from Services, where GE now expects growth in the low-20s vs the previous mid-teens expectation. This implies over \~\$1bn improvement in commercial services revenue. We see the improved revenue expectations driven partly by a better CFM56 shop visit outlook and higher material availability. For CES Equipment, revenue is expected to grow in the +20% range, up from prior guide of mid/high teens range. This implies a \$200mn improvement in OE revenue as the LEAP delivery guide was also raised for the year. For DPT, revenue is expected to grow in the low double-digit range, up from prior guide of mid to high single digits.

CFM56 shop visits are expected to trend toward the high end of the 2,300 to 2,400 range for the year. Management noted that CFM56 work scopes are expected to remain stable through 2028 and 2029, with revenue growth driven by higher volumes, improved pricing, and better material availability. As a result, revenue per shop visit is increasing, not because of broader work scopes, but because the company is now able to complete some of the heavier maintenance work that could not previously be performed due to material constraints. GE expects CFM56 shop visits to remain in the 2,300–2,400 range through 2028, with a modest decline thereafter. We expect shop visits for CFM56 to move slightly higher and extend further than we see in GE's guidance. We see spare parts and MRO shop capacity as the limiting factor that keeps GE's forecast below the demand level.

Widebody engine program workscopes remain favorable. For the GEnx, shop visit workscopes are expected to expand as the mix shifts from quick turns toward higher-value performance restoration visits. For the GE90, approximately 70% of the fleet has yet to undergo its second shop visit. As these second shop visits, which carry significantly larger workscopes than the first shop visits, begin to flow through, they should support continued aftermarket revenue growth.

CES should see margin expansion in 2028 and beyond. The company expects CES margins to improve as LEAP aftermarket margins move closer to segment-wide aftermarket levels and as GE9X losses, which are expected to peak in 2028, begin to decline thereafter. GE9X losses are expected to double this year as shipments double, putting pressure on CES OE margins. These losses should be more pronounced in the second half of the year, particularly in Q4, as deliveries remain weighted toward the latter part of the year.

LEAP delivery outlook - For 2026, GE guided to high-teens increase in LEAP deliveries, up from its prior guidance of 15%. This implies between 1,096 and 1,130 LEAP deliveries in the second half of the year. This outlook is supported by production rate increases that Boeing and Airbus have planned on the 737 MAX and A320neo aircraft. Airbus is looking to increase A320 family production to between 70 and 75 aircraft per month by the end of 2027. For the 737, Boeing expects to move to 47/

month by the summer of 2026. LEAP related AOGs have come down from improved spare engine availability in the field and reduced shop turnaround times. While spare engine ratio is coming down, the spare engine deliveries continue to grow as install engine shipments grow. Over the life of the LEAP program, the company expects the spare engine ratio for LEAP to be in low-double digits (10% to 12%).

2027 outlook - At our SDC conference in May, GE mentioned that it expects CES services revenue to grow in the double-digit range in 2027. This was reiterated on the Q2 call. Shop visits are backed up by 12-18 months of backlog on major programs. The engines already off-wing and planned removals in the third quarter exceed the company's full-year shop visit guidance by more than 40%, thereby de-risking its 2026 outlook.

LEAP-1B durability kit - GE completed certification of the LEAP-1B durability kit, which includes upgraded HPT blades. The kit is expected to deliver a twofold improvement in time on wing, with full MRO and new-make cutover expected in early 2027. The company has already equipped more than 40% of the LEAP 1A installed base with these durability kits. Retrofitting the LEAP-1A and LEAP-1B fleets is a multi-year effort, and management does not expect the fleets to be fully retrofitted before early 2030s.

CES Services Orders - We heard concerns on order intake as an indicator of aftermarket demand slowing down in Q2 (up +22%YoY). But orders can be lumpy and were up +49% in Q1'26, while GE has a large backlog it needs to deliver on. Our understanding is that shop visits are effectively sold out for 18 months across platforms. We rarely see new orders come in for MRO slots beyond that timeframe.

EXHIBIT 1: Reported results vs Bernstein, consensus and guidance

<table><tr><td>GE</td><td>Q2</td><td colspan="3">Full Year</td><td>Q2</td><td colspan="3">Full Year</td></tr><tr><td></td><td>2026</td><td>2025</td><td>2026E</td><td>2027E</td><td>2026</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>Reported</td><td>12.6</td><td>42.3</td><td></td><td></td><td>$2.02</td><td>$6.37</td><td></td><td></td></tr><tr><td>Bernstein (Pre)</td><td>11.8</td><td></td><td>48.5</td><td>53.6</td><td>$1.83</td><td></td><td>$7.59</td><td>$8.82</td></tr><tr><td>Consensus (Pre)</td><td>11.9</td><td></td><td>48.7</td><td>53.7</td><td>$1.86</td><td></td><td>$7.56</td><td>$8.69</td></tr><tr><td>New Guidance</td><td></td><td></td><td>High teens</td><td></td><td></td><td></td><td>$7.65 - $7.85</td><td></td></tr><tr><td>Bernstein (Post)</td><td></td><td></td><td>49.9</td><td>55.3</td><td></td><td></td><td>$7.83</td><td>$9.16</td></tr></table>

Source: Company reports, Bernstein analysis and estimates

## SEGMENT RESULTS

GE reported non-GAAP EPS of \$2.02, above consensus \$1.86. Adjusted revenue of \$12.6bn was above consensus expectations of \$11.9bn. At a segment level, revenues at CES of \$9.73bn were above consensus \$9.16bn (Exhibit 2). Segment profit of \$2.66bn was ahead of consensus estimate of \$2.47bn. Revenues of \$3.44bn at DPT were above consensus of \$3.20bn and segment profit of \$475mn was above consensus estimate of \$395mn.

Within CES, services grew by +26% with internal shop visit revenue up 25% and spare parts revenue up over 25%. CES Equipment revenue grew 30%, driven by unit volume up 26%, including LEAP up 24%. LEAP deliveries were up 24% YoY (\~510 engines), which puts YTD LEAP deliveries at 1,030. Margins of 27.3% in CES and 13.8% in DPT each beat our estimates (27.1% and 12.4%, respectively). On a YoY basis, margins at CES contracted from install engine growth (including GE9X), investments and inflation. Total orders increased +17% year-over-year, driven by a 18% increase in CES and a +12% increase in DPT.

EXHIBIT 2: Segment results

<table><tr><td></td><td colspan="3">Revenues</td><td colspan="4">Margins</td></tr><tr><td>Segment</td><td>Reported</td><td>Bernstein</td><td>Year ago</td><td>Reported</td><td>Bernstein</td><td>Last Q</td><td>Year ago</td></tr><tr><td>CES</td><td>9,731</td><td>9,093</td><td>7,646</td><td>27.3%</td><td>27.1%</td><td>26.4%</td><td>28.9%</td></tr><tr><td>D&amp;PT</td><td>3,443</td><td>3,173</td><td>2,978</td><td>13.8%</td><td>12.4%</td><td>11.8%</td><td>13.5%</td></tr><tr><td>Adjusted</td><td>12,634</td><td>11,760</td><td>10,151</td><td>21.7%</td><td>21.6%</td><td>21.8%</td><td>23.2%</td></tr></table>

Source: Company reports, Bernstein analysis and estimates

The guidance was raised across the board for FY2026 (Exhibit 3) with adj revenue growth expected in high-teens range (previously LDD). CES now expects revenue growth of \~20%, up from our prior outlook of mid-teens. This is driven by higher services revenue, which is now expected to grow low 20s, up from mid-teens, and equipment revenue growth of \~20%, up from mid-to-high teens. CES operating profit raised to \$10.25-\$10.35bn, up from prior guide of \$9.6-\$9.9bn. For DPT, revenue is expected to grow in the low double-digit range, up from prior guide of mid to high single digits. Adjusted EPS is now expected to be in the range \$7.65-\$7.85 (previously \$7.10-\$7.40).

EXHIBIT 3: 2026 Updated Guidance

<table><tr><td>After 2026Q2, for 2026</td><td>Guidance</td><td>Previous</td></tr><tr><td>CES</td><td>~20%</td><td>Mid-teens</td></tr><tr><td>DPT</td><td>+LDD</td><td>MSD-HSD</td></tr><tr><td>Adj. Revenue Growth</td><td>High teens</td><td>LDD</td></tr><tr><td>CES segment profit</td><td>$10.25 - $10.35bn</td><td>$9.6bn - $9.9bn</td></tr><tr><td>DPT segment profit</td><td>$1.6bn - $1.7bn</td><td>$1.55bn - $1.65bn</td></tr><tr><td>Corporate &amp; Eliminations</td><td>$(1.2)bn - $(1.3)bn</td><td>$(1.2)bn - $(1.3)bn</td></tr><tr><td>Adj. operating profit</td><td>$10.55B - $10.75B</td><td>$9.85bn - $10.25bn</td></tr><tr><td>Adj. EPS</td><td>$7.65 - $7.85</td><td>$7.10 - $7.40</td></tr><tr><td>FCF</td><td>$8.9B - $9.2B</td><td>$8.0bn - $8.4bn</td></tr></table>

Source: Company reports, Bernstein analysis

## CES

Within CES, services grew by +26% with internal shop visit revenue up 25% and spare parts revenue up over 25%. CES Equipment revenue grew 30%, driven by unit volume up 26%, including LEAP up 24%. LEAP deliveries were up 24% YoY (\~510 engines), which puts YTD LEAP deliveries at 1,030. However, margins at CES contracted 160bps to 27.3% (still beating our 27.1% estimate) from install engine growth (including GE9X), investments and inflation. Cash ou

[中间内容因长度限制已省略]

 you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient

makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
