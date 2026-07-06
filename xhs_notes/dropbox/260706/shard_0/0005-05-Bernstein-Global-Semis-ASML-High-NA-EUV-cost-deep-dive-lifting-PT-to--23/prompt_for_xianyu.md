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
Global Semis

# ASML: High-NA EUV cost deep dive - lifting PT to €2300 on rising litho intensity

![](images/b18de1591508ac18722e5d529017103ae5c7e3c498966e0b5129462d820c550e.jpg)

![](images/1fbf46d82ea0a3d13b36b8efc6e28b7b265d361de7b29dba2e39b4cfa2ebb2f8.jpg)

![](images/4be9d6068971c288ee4d7eb27ee1f6964d3cfc309784e6d9b093b0f89d4b69bf.jpg)

![](images/b2f54e6ad4bc7897e22aeb8462bfc5171f4a934d3f848e1010e0223794965836.jpg)

![](images/26423c20d065bcbfefb1187dd4b292a0da8b1eaeb8481cf4a43207169ab6d241.jpg)

David Dai, CFA
+852 2918 5704
david.dai@bernsteinsg.com

Mark Li
+852 2123 2645
mark.li@bernsteinsg.com

Stacy A. Rasgon, Ph.D.
+1 213 559 5917
stacy.rasgon@bernsteinsg.com

Carmine Milano, CFA

+44 20 7762 1857

![](images/8e758652a0bac7f21d6fbe0459d124bfa5f7555ec98503695e1f2807640a7eaf.jpg)

carmine.milano@bernsteinsg.com

Juho Hwang

+81 3 6777 6980

juho.hwang@bernsteinsg.com

Jack Lin
+852 2123 2683
jack.lin@bernsteinsg.com

HNA EUV will likely be adopted first in DRAM than for logic due to lower cost of exposure for DRAM. A common concern from investors is that HNA is too expensive (as TSMC said so) and won't be adopted anytime soon. However, what's rarely discussed is the big difference between DRAM and logic: DRAM die size is much smaller than logic, and hence only uses 1 mask, while logic mostly needs 2 masks due to larger die size (stitching). The mask changing slows down throughput by $23\%$ (135WpH vs. 175WpH), and the cost of HNA exposure for DRAM is cheaper and easier to justify. So we believe DRAM will likely adopt HNA in 2027 in 1d, when LNA EUV double patterning is needed, earlier than logic.

Logic adoption of HNA is also in sight. The high cost of HNA exposure is largely associated to the low tool availability of 80-85%, while LNA is close to 95%. However, HNA tool availability is improving faster, and is targeted to reach \~95% by 2030. WpH is also expected to increase from 135 to 175 even with 2 masks. While the litho equipment cost of HNA exposure is currently \~3x LNA for logic, the gap will narrow to \~2x by 2030. Considering other costs and complexity of double patterning, it's justifiable for logic to migrate to HNA before that. We expect Intel to be the first to adopt HNA in 2028, while TSMC will be slower, but still likely to adopt in 2030.

Rising litho intensity from 24% in 2025 to 26% in 2028. When HNA replaces LNA multiple patterning, the other cost of double patterning (etch, depo, cleaning etc) can be greatly reduced. Hence litho intensity is expected to rise with HNA, just like how litho intensity increased when LNA EUV replaced DUV (ArFi) multiple patterning. We forecast DRAM litho intensity to increase from \~20% in 1z to \~30% in 1d, due to increase in EUV layer count and adoption of HNA in 1d. While logic litho intensity stabilizes at \~32% in N2 and A14 due to limited adoption of HNA, we expect it to rise in A10. Mostly driven by DRAM, we forecast litho intensity to increase from 24% in 2025 to 26% in 2028, and ASML to gain share.

We materially increase our ASML topline forecasts following the unprecedented AI-driven expansion in both advanced logic and DRAM capacity. We raise EUV (including HNA) shipment forecasts in 2027 to 91 systems (vs. old 86) and 113 (old 87) in 2028, and expect ASML to expand EUV capacity. This is on top of strong ASP expansion supported by throughput improvements. As a result, we now expect EUV revenue to grow at a 30% CAGR, reaching €42.7bn by 2030, more than 30% above street. We also revised our DUV estimates upward, particularly toward the end of the decade, and now expect DUV revenue to reach €20bn in 2030, from €13bn in 2026.

Top Pick, lifting PT on capex cycle and litho intensity. Higher revenue and operating leverage also support stronger profitability, and our 2028 EPS of €67 is 35% above consensus. We also don't see capex peaking, and expect ASML revenue to reach €80bn by 2030 (20% CAGR) and EPS €97 by 2030 (31% CAGR). ASML now trades at trough valuation vs. peers. Given the clear acceleration in capex cycle and rising peer valuation, we raise our target P/E multiple from 35x to 40x (1SD above mean), increasing our target price to €2,300.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Cur</td><td rowspan="2">3 Jul 2026 Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>ASML.NA (ASML)</td><td>O</td><td>EUR</td><td>1,634.40</td><td>2,300.00</td><td>120.2%</td><td>EUR</td><td>24.72</td><td>32.73</td><td>48.68</td><td>66.1</td><td>49.9</td><td>33.6</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>1,700.00</td><td></td><td></td><td></td><td>32.69</td><td>46.98</td><td></td><td></td><td></td></tr><tr><td>ASML (ASML)</td><td>O</td><td>USD</td><td>1,769.32</td><td>2,623.00</td><td>103.5%</td><td>USD</td><td>27.95</td><td>37.01</td><td>55.05</td><td>55.4</td><td>41.8</td><td>28.1</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>1,971.00</td><td></td><td></td><td></td><td>36.96</td><td>53.13</td><td></td><td></td><td></td></tr><tr><td>INTC (Intel)</td><td>M</td><td>USD</td><td>120.35</td><td>100.00</td><td>416.0%</td><td>USD</td><td>0.43</td><td>1.07</td><td>1.50</td><td>282.3</td><td>112.4</td><td>80.0</td></tr><tr><td>005930.KS (SEC- Samsung)</td><td>O</td><td>KRW</td><td>314,500</td><td>440,000</td><td>359.0%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td>47.6</td><td>6.5</td><td>4.1</td></tr><tr><td>005935.KS (SEC-Pref - Samsung)</td><td>O</td><td>KRW</td><td>208,000</td><td>374,000</td><td>256.9%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td>31.5</td><td>4.3</td><td>2.7</td></tr><tr><td>SMSN.LI (Samsung)</td><td>O</td><td>USD</td><td>5,040.00</td><td>7,350.00</td><td>298.8%</td><td>USD</td><td>116.15</td><td>812.39</td><td>1,290.80</td><td>43.4</td><td>6.2</td><td>3.9</td></tr><tr><td>000660.KS (SK hynix)</td><td>O</td><td>KRW</td><td>2,424,000</td><td>3,300,000</td><td>758.3%</td><td>KRW</td><td>60,341</td><td>395,677</td><td>568,862</td><td>40.2</td><td>6.1</td><td>4.3</td></tr><tr><td>MU (Micron)</td><td>O</td><td>USD</td><td>975.56</td><td>1,300.00</td><td>678.6%</td><td>USD</td><td>8.29</td><td>67.39</td><td>158.99</td><td>117.7</td><td>14.5</td><td>6.1</td></tr><tr><td>2330.TT (TSMC)</td><td>O</td><td>TWD</td><td>2,445.00</td><td>2,780.00</td><td>87.5%</td><td>TWD</td><td>66.25</td><td>101.62</td><td>124.63</td><td>11.7</td><td>8.6</td><td>6.6</td></tr><tr><td>TSM (TSMC)</td><td>O</td><td>USD</td><td>434.16</td><td>430.00</td><td>65.7%</td><td>USD</td><td>10.48</td><td>16.07</td><td>19.70</td><td>13.1</td><td>9.7</td><td>7.4</td></tr><tr><td>EDME</td><td></td><td></td><td>1,622.79</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,483.24</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,977.84</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EM</td><td></td><td></td><td>1,835.33</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
INTC, MU estimate is Adjusted EPS; INTC, MU valuation is Adjusted P/E (x); 2330.TT, TSM valuation is P/B (x);
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate ASML Outperform, PT = €2,300, TSMC Outperform, PT = USD 430, Intel Outperform, PT = USD 100, Samsung Outperform, PT = KRW 440,000, SK Hynix Outperform, PT = KR 3,300,000, Micron Outperform, PT = USD 1,300.

## DETAILS

Our ASML Model and Industry models can be downloaded here (ASML.NA / ASML Holding NV; EUV Model; DUV Model).

One of the concerns from investors for our ASML long thesis is the delay of High-NA (HNA) adoption, notably by TSMC (ASML - High-NA EUV adoption postponed?). Investors often ask why is HNA not been adopted, and if TSMC doesn't want to adopt it, does it mean the slowdown of litho vs. other processes such as etch and depo. This report analyzes the HNA cost vs. Low-NA (LNA) EUV, and conclude that HNA will likely be adopted by memory first, followed by logic, which drives increase in litho intensity. We reiterate ASML long and lift PT to €2300.

HNA EUV greatly simplifies the process and is set to replace LNA EUV as the leading edge litho tool.

\- HNA EUV has demonstrated \~8 nm resolution versus \~13 nm for LNA EUV, driven by the move from 0.33 numerical aperture to 0.55 NA optics. In lithography, resolution scales roughly with wavelength divided by numerical aperture, so keeping EUV wavelength constant at 13.5 nm while increasing NA by \~67% allows ASML to print significantly smaller features.

\- That resolution shrink translates into roughly 2.8–2.9x higher theoretical patterning density. The simple intuition is area scaling: if the printable half-pitch improves from \~13 nm to \~8 nm, the density gain is approximately 2.8x, or about 1.7x smaller features, versus 0.33 NA EUV. The key change is the larger projection-optics aperture, from NA 0.33 to NA 0.55. A higher NA collects and projects light at wider angles, which improves image sharpness and contrast at smaller pitches. ASML also highlights that HNA delivers higher imaging contrast, which improves local CD uniformity, reduces variability, and can lower required exposure dose (Exhibit 1).

\- The benefit is not only smaller lines, but simpler patterning. At very tight pitches, LNA EUV increasingly needs double or triple patterning: multiple masks, multiple litho-etch loops, and extra cut/via steps. HNA can convert some of those critical layers back to single exposure, reducing mask count, process complexity, edge-placement error accumulation, cycle time, and defect opportunities.

Cost of HNA exposure is high now but is expected to come down significantly as availability improves. We estimate with 95% availability cost for HNA exposure can drop by 23%.

\- Current low tool availability: At the current stage, HNA tools suffer from lower availability, which is a common issue for a new litho tool. While HNA is already progressing through the expected maturity curve, running at \~80% availability in 2025, this is still meaningfully below LNA which reached close to 95% availability. ASML started HNA development already in 2014, reached first good exposed wafers in the HNA lab after system integration in 2023. By Sep-2025, EXE systems had exposed more than 500k wafers, providing a much larger data set to drive reliability learning and HVM readiness.

\- Improving availability in sight: ASML disclosed that HNA availability reached above 80% for the first time in 2025, with fleet availability maturing toward a 90% target in 2026. The main source of lower availability remains long unscheduled downs, especially >12-hour events, while scheduled downtime is also partly driven by monitoring, configuration updates and platform learning. ASML's maturity curve shows EXE availability tracking favorably versus LNA/NXE at a comparable stage, targeting \~95% over the next 3-4 years (Exhibit 2), (Exhibit 3).

\- Cost-per-exposure drops: With higher availability, we estimate the litho equipment cost for HNA exposure can drop by 23% from 2025-2030. Higher availability is an important lever, but not the only driver of HNA cost reduction. Cost per exposure also improves with throughput: EXE:5200B has achieved 175 WpH in AA, up from 110 WpH on EXE:5000, with ASML's roadmap moving toward 190+ WpH (Exhibit 4).

EXHIBIT 1: HNA EUV moves 0.55 NA optics while keeping the same 13.5 nm wavelength, improving demonstrated resolution from \~13 nm to \~8 nm. This higher optical aperture increases image contrast and allows smaller pitches to be printed with fewer patterning steps.

![](images/f575111d003d2a9f6c78fb41202e5306df6d58ab9b014fae8586317d6345a90e.jpg)

![](images/b470807119ea7c9ee692200501f01fbc851a292b1be278e543c258af1c5695b4.jpg)  
Source: Company reports, Bernstein analysis

EXHIBIT 2: Unscheduled downtime is the primary driver of EXE unavailability and reducing it is the critical path to achieving the 90% availability target.  
![](images/5d6169ef701d33660dff8e86a08914754a79d9853a52edd71f10c461ddd56de7.jpg)  
Source: Company reports, Bernstein analysis  
EXHIBIT 3: EXE availability is targeted to reach 90% by 26Q4 and converge with the NXE:3600 mature fleet performance of 95% over five years

![](images/96d66a9a3bfb48c0c792e94d4b52add28323f650578b9c1a96e982ee600c38f4.jpg)  
EXHIBIT 4: With HNA availability reaching 95%, the equipment cost of a HNA exposure drops by 23%.  
HNA Cost per Exposure (1 Mask) vs Availability  
Source: Company reports, Bernstein analysis.

![](images/d038264b18a90adc1cb282a71a33f88e4b646d10dca9474ba4bc24de9967a5ce.jpg)  
Source: Company reports, Bernstein analysis and estimates.

However, HNA exposure cost is not the same for all. HNA EUV throughput (and hence cost) gets impacted from half field stitching, which results in slower throughput & higher cost for larger dies.

\- The main trade-off with HNA EUV is field size. Standard LNA NXE systems use a 4×/4× reduction ratio, meaning the mask image is reduced by 4× in both x and y on the wafer, preserving the conventional full EUV exposure field. HNA EXE uses an anamorphic 4×/8× optical design: 4× reduction in one direction and 8× in the other. This helps fit the much larger 0.55 NA projection optics and control mask-side angles, but it also halves the exposed field in one dimension. As a result, EXE prints a half field, roughly 16.5 mm in the reduced direction instead of the classic \~33 mm full-field height (Exhibit 5, Exhibit 6).

\- For products with many small die, such as some DRAM or smaller logic die, this is manageable: the scanner can expose twice as many half-fields using the same mask, with no need to stitch a single large die. For a single large logic die such as GPU dies, however, the chip can exceed one EXE half-field. In that case, stitching will be required. Stitching means splitting a large die across two EXE half-field exposures (Mask A and Mask B), and designing an overlap/stitch zone where the two exposures connect. The chip floorplan and routing are then made stitch-aware, so layout features crossing the boundary can be connected while controlling overlay and placement errors (Exhibit 7).

EXHIBIT 5: The H100/B100 GPU die size is already approaching the physical reticle limit of $33 \times 26 \, mm^2$ . With HNA, this limit is reduced to $16.5 \times 26 \, mm^2$ . Consequently, large logic dies require stitching.

![](images/764f337a2171993aa8b20e5f16c484cf6d5426f833923f601f74e17aa1938489.jpg)  
Source: ASML, Nvidia, Bernstein analysis.

EXHIBIT 6: In HNA, anamorphic optics use 4× demagnification in one axis and 8× in the other, so the 0.55-NA scanner prints only a half-field on the wafer. Larger logic dies must be split across two mask fields.

![](images/bf0548e35e428311c402dbeef3de74c4ff1c9e442fb0ac31654830bb0544b074.jpg)  
Source: ASML, Bernstein analysis

EXHIBIT 7: ASML HNA EUV stitching process using AB mask overlap to reconstruct full field logic die beyond reticle limits highlighting precise overlay control across 16.5 millimeter exposure boundaries for advanced chip manufacturing.  
![](images/eb7ded0238db66cbb8ea2bdd053c06a5e15c44f699881414a2e7ccab8056fb4f.jpg)

![](images/67b99942d3c313b2ed3d9d74d31fa55856959ef9ecafe081f7b9a4d4d185bf83.jpg)  
Scanner

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
