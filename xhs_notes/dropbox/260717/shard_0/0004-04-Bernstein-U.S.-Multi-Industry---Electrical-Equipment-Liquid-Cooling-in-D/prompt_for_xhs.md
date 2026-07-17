你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
# U.S. Multi Industry & Electrical Equipment

# Liquid Cooling in Data Centers: What comes after single phase DTC? With CoolIT's 15kW cold plate, does anything even need to?

![](images/ac3bf935477a62b394e15aafca65c19ef8764e9c69c2e77aa1336bc4350f6804.jpg)

![](images/4ca769075ad28f5d23efeb1b41acc515d775d5e8fb0c0c902563a37aeb67e6da.jpg)

![](images/51350124eb3cc60bdd30d8a547ca1ef4c91cf3f6c3bdda5010bae35fe689e0c5.jpg)

![](images/db2f771299f0e602494784460e24006b32d57fd9430a37396125136126389e46.jpg)

![](images/8a7c3d78630a74c06e1c5024ac0ff9829d438be0c3571fd0f414840f5c033009.jpg)

Varun Govindaraj
+1 917 344 8543
varun.govindaraj@bernsteinsg.com

Chad Dillard
+1 917 344 8469
chad.dillard@bernsteinsg.com

Alasdair Leslie
+44 20 7762 4952
alasdair.leslie@bernsteinsg.com

Miguel Marques, CFA
+1 917 344 8432
miguel.marques@bernsteinsg.com

Om Kela
+44 20 7550 2192
om.kela@bernsteinsg.com

Specialist Sales

![](images/be6255847588a25760c890157e4b2322337b1aeb1be1df6680213d1179d89e60.jpg)

Steve Song
+1 917 344 8401
steve.song@bernsteinsg.com

When you hear the term “liquid cooling” today, most people are referring to single phase direct to chip (DTC). It’s called single phase because the coolant stays in a liquid state (and doesn’t undergo a phase change to vapor). The broader market seems to believe we are coming up on a theoretical limit on future generations of GPUs being cooled with single phase (especially as you start to reach TDPs around Rubin Ultra which are above \~2.5kW). Two technologies are seen as successors to single-phase DTC; (i) two-phase DTC and (ii) direct to die. These have been explained in more detail below.

Two-phase DTC: The more likely to see commercial viability in the next \~12- 18 months around the same time as Rubin Ultra. Undergoes a phase change (evaporation) of the coolant in a cold plate enabling it to capture more heat vs. single phase DTC operating at similar conditions. Most major players are likely investing in the space, either directly (e.g., VRT, CoolIT) or through partnerships (e.g., JCI with Accelsius, Carrier with ZutaCore, etc.). Still has real engineering challenges to solve for (backward flow, refrigerant choice, etc.) so it is by no means a done deal.

Direct-to-die: Eliminates the need for cold plates entirely by cooling through the silicon die itself. Far more technically complex and R&D is extremely early stage but could theoretically offer materially better heat flux vs. DTC. We do not expect to see anything happen at scale before 2030. Microsoft and TSMC are both making investments and have signalled activity (potentially manufacturing in 2026) but we're yet to hear anything about widespread adoption because of more practical challenges (e.g., deionized water causing corrosion to silicon).

The wildcard, CoolIT's 15kW single phase cold plate: About a month ago, CoolIt also announced that they're proven single-phase DTC could work with a cold plate rated at 15kW under relatively standard operating conditions (1.2 lpm, $45^{0}\mathrm{C}$ inlet temperatures, thermal paste, PG25 coolant, etc.). This is counter to the narrative that single phase won't work at GPU TDPs $>2.5\mathrm{kW}$ (CoolIT's number is 6x that). While the technology was tested in a lab scale setup as per their white paper, we do think this is a credible product. If it can be commercialized at scale, it essentially pushes out the need for two-phase DTC well beyond 2030. Most technological evolution on power and cooling in a data center is driven by necessity, and if we don't NEED two-phase or direct-to-die anymore, it's easier for data center operators to continue using single-phase cooling setups. If the 15kW cold plate can be commercialized, we think it has mixed implications on white space cooling equipment (CDUs and cold plates). On one side, there's less of a structural shift to new technologies that could create pricing pressure on these components (because the innovation premium starts to dry up) and commoditization may be accelerated. To be clear, it is unlikely to materially impact revenues or margins in the next couple of years since demand far outstrips supply, but it is a risk beyond that. It depends on how quickly competitors can replicate CoolIT's approach (which may not be immediate since they do have a patent on the underlying technology). On the positive side (for cold plates in particular), it does eliminate the obsolescence risk (since there's no real need for direct-to-die) for the foreseeable future.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">15 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>VRT (Vertiv)</td><td>O</td><td>USD</td><td>304.57</td><td>416.00</td><td>117.8%</td><td>USD</td><td>4.20</td><td>6.52</td><td>9.21</td><td>72.6</td><td>46.7</td><td>33.1</td></tr><tr><td>NVT (nVent)</td><td>O</td><td>USD</td><td>159.46</td><td>220.00</td><td>92.6%</td><td>USD</td><td>3.34</td><td>4.84</td><td>6.26</td><td>47.7</td><td>33.0</td><td>25.5</td></tr><tr><td>TT (Trane)</td><td>O</td><td>USD</td><td>480.20</td><td>555.00</td><td>(11.2)%</td><td>USD</td><td>13.06</td><td>14.98</td><td>17.82</td><td>36.8</td><td>32.0</td><td>26.9</td></tr><tr><td>CARR (Carrier)</td><td>M</td><td>USD</td><td>68.74</td><td>75.00</td><td>(30.1)%</td><td>USD</td><td>2.57</td><td>2.79</td><td>3.20</td><td>26.7</td><td>24.6</td><td>21.5</td></tr><tr><td>JCI (Johnson Controls)</td><td>O</td><td>USD</td><td>142.76</td><td>173.00</td><td>13.4%</td><td>USD</td><td>3.78</td><td>4.97</td><td>5.93</td><td>37.8</td><td>28.7</td><td>24.1</td></tr><tr><td>ETN (Eaton)</td><td>O</td><td>USD</td><td>412.86</td><td>534.00</td><td>(7.3)%</td><td>USD</td><td>12.07</td><td>13.45</td><td>16.37</td><td>34.2</td><td>30.7</td><td>25.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,572.40</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate VRT Outperform with a TP of \$416

We rate NVT Outperform with a TP of \$220

We rate TT Outperform with a TP of \$555

We rate JCI Outperform with a TP of \$173

We rate CARR Market-Perform with a TP of \$75

We rate ETN Outperform with a TP of \$534

## RECAP: OVERVIEW OF SINGLE-PHASE DTC COOLING

The predominant format of liquid cooling today is single-phase DTC. DTC stands for Direct-To-Chip. It involves cold plates (which are aptly named slabs of metal that have reduced temperature due to refrigerant that circulates inside them) coming into contact with GPUs to extract heat. Inside the cold plates, liquid flows through arrays and flow loops with the intent of maximizing the amount of heat they are able to extract from the GPU. Coolant Distribution Units (CDUs) pump low temperature coolant (usually a water - propylene glycol mix in single-phase setups) through the cold plates and recollect the spent liquid once they have extracted heat from the server.

The heat is then extracted from the coolant (making it cold again) and the process repeats. It is called single phase because the coolant stays in a single phase (liquid) and does not change phases from to gas via evaporation. This loop (i.e., circulating from the CDU through cold plates in the server) is called the TCS or technology cooling system. Once spent coolant reaches the CDU, it passes through a heat exchanger where it transfers heat to another cooling loop called the FWS or Facility Water System. The FWS connects to a chiller or dry cooler to reject this heat outside a data center. However, as rack power densities continue to increase, single phase DTC is seemingly reaching the theoretical limit of how much heat it can extract.

EXHIBIT 1: Direct-to-chip process overview  
![](images/2c4e37f46042efa82aa1e3cfb37d55b3d51374b2357eeece474515518a0a1ad2.jpg)  
Source: Bernstein Analysis

Generally, at current surface areas of GPUs, single-phase DTC has been expected to hit its thermal limit at GPU TDPs of between 2 - 2.5kW. Rubin GPUs start to push against this 2 - 2.5kW limit, and Rubin Ultra is expected to surpass it. After this point, the technological consensus has been that more aggressive forms of heat transfer (e.g., two-phase or direct to die) would be needed instead.

There is also the alternative of just reducing the temperature of the coolant flowing through the cold plate, but in the interest of managing energy consumption, this has not been preferred. Immersion cooling is also not considered a viable alternative since it involves submerging the server in coolant which is unweildy and much harder to maintain than current tray based approaches. So the two real options are either two-phase DTC or “direct to die” which are explained below.

EXHIBIT 2: Liquid cooling format by GPU TDP  
![](images/0a7cde6e0e570d6e5e11833ef041b6a4a7993162e54662b7505c3ca5b9b7ec7b.jpg)  
Source: Bernstein Analysis and Estimates

EXHIBIT 3: Multiple formats of liquid cooling delivery  
![](images/25a1c747c341062d8c9a38cfb55bd20a47bc57642906968a1e7cff50e97dd082.jpg)

Coolant evaporates (phase changes) when it absorbs heat from GPUs (extracting much more heat than single-phase)

Microfluidics channels etched directly into the silicon wafers

Source: Bernstein Analysis and Estimates

<table><tr><td colspan="2">Mechanics of heat transfer</td></tr><tr><td colspan="2">Q = m * c * ΔT + m * L</td></tr><tr><td>Sensible Heat(normal heating)</td><td>Latent Heat(Heat needed to change phase from liquid to vapor)</td></tr><tr><td>Q = Total heat energy absorbed by the liquid (measured in kilo-Joules)</td><td></td></tr><tr><td>m = Mass of the liquid (measured in kg)</td><td></td></tr><tr><td>C = Specific heat capacity (amount of heat required to raise temperature of 1kg of liquid by 1°C, measured in kilo-Joules/kg-0C)</td><td></td></tr><tr><td>ΔT = Temperature change (measured in °C)</td><td></td></tr><tr><td>L = Specific latent heat (amount of heat required to boil the liquid, measured in Joules/0C)</td><td></td></tr></table>

EXHIBIT 4: Sensible vs. latent heat; what's the difference?  
Illustration (consider water as an example)  
1 kg of water heats up by $1^{\circ}$ C

## TWO PHASE DTC

## Overview

As the name suggests, two-phase DTC cooling involves two phases of matter in the cooling process. In single-phase DTC, the TCS coolant (a water glycol mix) remains in a liquid state through the entire heat transfer process as it passes through the cold plate. However, in two-phase DTC, the coolant (another compound, not water-based) evaporates into a gaseous state in the cold plate before being cooled again into a liquid and repeating the cycle. The process of evaporation is able to capture a large amount of heat without a significant change in the underlying temperature of a refrigerant.

To understand how this works, we need to define a few scientific terms; sensible heat and latent heat. Sensible heat refers to the amount of heat needed to increase the temperature of a substance without a phase change. Latent heat refers to the amount of heat needed to cause a phase change (e.g., liquid to gas via evaporation) while maintaining the temperature of the matter undergoing a phase change.

$Q_{sensible heat} = m * c * \Delta T$ where m is the mass of the substance, c is it's specific heat (i.e., the amount of heat needed to increase temperature of 1 kilogram of material by $1^{0}C$ ), and $\Delta T$ is the change in temperature.

$Q_{latent heat} = m * L$ where m is still the mass of the substance while L is the specific “latent” heat (i.e., the amount of heat needed to cause a phase change of 1 kg of material). Notice how the temperature change doesn’t matter like with sensible heat; this is because when a phase change takes place, it happens at constant temperatures. If a coolant or refrigerant has a large enough latent heat, it can essentially capture a lot more thermal load while maintaining relatively constant temperatures vs. sensible heat transfer. This is the same principle applied in a refrigerant compression cycle, where refrigerant evaporates when it captures heat and condenses before cycling back into the system.

$$
Q = (1) \times (4. 1 8) \times (1) = 4. 1 8 \mathrm{kJ}
$$

Core principle of single-

phase DTC (coolant just

"heats" up) - amount of

heat taken out is 4.18 kJ

1 kg of water boils up (constant temperature process)

$$
\mathrm{Q} = (1) \times (2 2 6 0) = 2 2 6 0 \mathrm{kJ}
$$

Core principle of two-phase

DTC (coolant "boils") – amount

of heat taken out is 2260 kJ

Source: Bernstein Analysis and Estimates

EXHIBIT 5: Two-phase cooling mechanism (illustrative)  
![](images/d73523a0c71428fa5f86f654213f53cc360c151b17aae578fa48db791d98b331.jpg)  
Source: Bernstein Analysis; images generated using AI to showcase representative process

## Advantages of Two Phase DTC

The key advantage of two-phase DTC is the higher heat flux vs. single phase operations; you can just capture a lot more heat under the same conditions when the coolant can evaporate (often >3x). This allows you to develop GPUs with much higher TDPs while maintaining the same footprint. Since evaporation also maintains the coolant at the same temperature, you have an even, uniform thermal profile through the cold plate which helps manage hotspots better. Depending on the coolant used and the chip TDP, you can also use smaller pumps, less volume of coolant, and spend less energy pumping it through the system compared to similar thermal loads with single phase. Since these refirgerants / coolants are not likely to be water-based, they are also less likely to see corrosion or bacterial growth. It also enables the coolant to be dielectric (not electrically conducting), so in case of a liquid leak it does not fry the GPU. And by nature, two phase coolants evaporate when spilt, vs. pool on the tray.

## Disadvantages of Two Phase DTC

The biggest engineering problem to solve relates to flow in a two phase system. Most matter flows from regions of high pressure to regions of low pressure. With liquids this is simple, even in a complex microchannel array within a cold plate. However, when evaporation takes place, gas could create high pressure pockets, which push it in the opposite direction vs. where it should be flowing. This has still not been resolved at scale. Another disadvantage is complexity; a two-phase system has significantly more variables than a single phase CDU / cold plate setup. Refrigerants / coolants that meet required properties are often PFAS (forever chemicals) which are not ideal for deployment. So there is still research that needs to happen to develop and then produce these compounds at scale.

## Who's leading the pack on R&D?

It's hard to say because companies offer differing levels of visibility. From what we've publicly seen, Vertiv and Accelsius are the closest to having commercially ready products. Accelsius in fact advertises CDUs on their website. Zutcore focuses heavily on the topic but we've not seen specific products on their website (although they do have demos). We know CoolIT is also doing work in the space; they also presented on the topic at the OCP forum a couple of years ago. Boyd has a history of two-phase expertise, even if not for CDUs specifically while Schneider recently put out a blog post on the topic. JCI and Carrier have invested in Accelsius and Zutacore respectively. We've not seen announcements from nVent and Trane yet, although as NVIDIA reference design partners we believe they'll have the products when they need to.

## EXHIBIT 6: Two-phase R&D status by liquid cooling players

![](images/2a606d848c2a234cd162f0ed84253b5a7ad99e862c666b10d82ad2a96e35ef0d.jpg)

## Source: Bernstein Analysis, Company Reports

## EXHIBIT 7: Key challenges preventing two-phase commercialization

![](images/059ab2dfef1844ba80ca53dbc7fd7539aa3d9284eb3db987e8ac00cbf0d2e845.jpg)  
Source: Bernstein Analysis

## 1 Concurrent management of fluid and vapor is a fundamental challenge

\- Two-phase cooling requires dual-path channel array on the cold plates (larger diameter for low-density vapor and smaller diameters for liquid)

\- This leads to flow maldistribution – where some channels predominantly carry vapor and some liquid on the plate, which can lead to localized hotspots (which can then lead to non-uniform cooling)

## 2 High degree of control complexity

• Active management of multiple variables is required: refrigerator temperature, avoidance of vapor superheating, condensate cooling, and overall system pressure

\- Modern GPU workloads are non-steady: inference batching creates rapid power transients (0 ->100% in milliseconds) which requires constant monitoring

\- This requires finely calibrated sensors and control algorithms than single-phase; control software complexity can be a significant burden

## 3 Polyfluoroalkyl substances (PFAS) regulations

\- Industry currently relies

[中间内容因长度限制已省略]

tained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
