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
# U.S. Multi Industry & Electrical Equipment

# Data Center Chillers (1/3): Primer and free cooling economics

![](images/2d92f063532cd3e658f9ba79f9196f04f9412a3f6e9087271ea60c73c83f965d.jpg)  
Varun Govindaraj

+1 917 344 8543

varun.govindaraj@bernsteinsg.com

Specialist Sales

![](images/33c4e8f7ea650f0e27750430b3c96823f452fbefde675035cf30f6511742303f.jpg)

Steve Song

+1 917 344 8401

steve.song@bernsteinsg.com

Chillers are a critical part of data center cooling infrastructure both in liquid-cooled and air-cooled environments. They are responsible for creating chilled facility water that then pumps to CDUs to extract heat from the coolant or to CRAHs to reduce the temperature of air blowing through the data center. We size this as a \~\$8B market in 2026 (fully loaded cost including installation and ancillaries), but the growth outlook can vary significantly based on how you think chiller penetration changes. Assuming no such changes (our base case), we project a \~20% CAGR for the market with 2030 estimated at \~\$16.5B.

We often hear debates of when it makes sense to use air-cooled vs. water cooled units. As a quick primer, both types of chillers operate using a refrigerant cycle, but air-cooled units reject heat from the refrigerant into ambient air, while water-cooled units reject to another water loop (either a cooling tower or a dry cooler). Air-cooled units are lower capex, but much less energy efficient. Water-cooled units need more upfront investment and consume large quantities of water (if a cooling tower is used), but tend to consume less power for the same tonnage. So it really is a sensitivity analysis of what you think your operating conditions and input costs will be when making the decision.

To illustrate this, we looked at how much it would cost to run an 800 ton chiller (roughly 2.5 MW) - assuming it was air-cooled or water-cooled. When the compressor of the chiller ran 24X7, annual operating costs were roughly 25% higher for an air-cooled chiller vs. a water-cooled unit, implying a \~3 year payback on the cost differential. So water-cooled units are always better, right?

It is not that simple. This dynamic can change quite drastically when you take free-cooling into account. Free-cooling is a when the ambient temperature drops enough for the data center operator to tone down (and in some cases switch off) the compressor in the chiller. It's a bit of a misnomer, the cooling isn't entirely free (you still need some power) but it's a fraction of what you'd need with the compressor running at 100%.

Energy consumption drops significantly for both air-cooled and water-cooled units. However, water costs stay relatively constant for water-cooled chillers (assuming a cooling tower is used). So as you spend more time in a free cooling environment, you may run into a situation where it is actually cheaper to operate an air-cooled chiller vs. a water-cooled chiller. This could be why we are hearing people talk about air-cooled chillers gaining share in the market.

We also spent some time benchmarking chiller offerings by key players available or announced in the market (like we did with our earlier primer on CDUs). We do not find the differences to be as stark; while there are some variations between companies, and they all have their own edge, we think these variations in specs are far outweighed by the overwhelming supply shortage and demand we are seeing for chillers today.

This is the first of our three part series on chillers. In part two, we will discuss “chiller gate” in more depth and in part three dive into the economics of servicing a chiller unit.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">18 Jun 2026</td><td>TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td></td><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td rowspan="2">Cur</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td></tr><tr><td>TT (Trane)</td><td>O</td><td>USD</td><td>483.40</td><td>550.00</td><td>(10.5)%</td><td>USD</td><td>13.06</td><td>14.96</td><td>17.61</td><td>37.0</td><td>32.3</td><td>27.4</td></tr><tr><td>CARR (Carrier)</td><td>M</td><td>USD</td><td>71.81</td><td>75.00</td><td>(22.9)%</td><td>USD</td><td>2.57</td><td>2.81</td><td>3.20</td><td>27.9</td><td>25.6</td><td>22.4</td></tr><tr><td>JCI (Johnson Controls)</td><td>O</td><td>USD</td><td>144.82</td><td>176.00</td><td>14.3%</td><td>USD</td><td>3.78</td><td>5.06</td><td>6.04</td><td>38.3</td><td>28.6</td><td>24.0</td></tr><tr><td>VRT (Vertiv)</td><td>O</td><td>USD</td><td>333.05</td><td>416.00</td><td>154.0%</td><td>USD</td><td>4.20</td><td>6.52</td><td>9.21</td><td>79.3</td><td>51.1</td><td>36.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,500.58</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate TT Outperform with a target price of \$550.

We rate CARR Market-perform with a target price of \$75.

We rate JCI Outperform with a target price of \$176.

We rate VRT Outperform with a target price of \$416.

Annual Operating costs (water + power)

EXHIBIT 1: When should you buy an air-cooled vs. water-cooled chiller?  
Annual OpEx differential in an 800-ton chiller (air-cooled vs. water-cooled)  
![](images/6af81d57c3f770314d309d6a71cb98ebdc48008641b3f1cac027d02a602b1952.jpg)  
If cooling tower needs to be active (which we think it does) to enable free cooling in a water-cooled chiller, water usage makes an air-cooled chiller seem more attractive in free-cooling heavy environments  
However, this is based on national averages for power and water costs; reality-will look quite different based on the region of operation  
Source: Bernstein Analysis and Estimates

EXHIBIT 2: Trade-offs by chiller type and regional variation  
Deciding between air-cooled and water-cooled chillers based on geography  
![](images/fae5fd5c704dd345de906797de48765297d59874bf561e1132daa94ee0b96b87.jpg)  
Note: Power costs are \$10.25, \$6.26, \$6.7, \$9.19 per 100 kWh for NoVa, DFW, ATL, ORD from EIA; Water costs are \$12.5, \$11, \$20, \$10 for NoVa, DFW, ATL, ORD pulled from regional sites (actual industrial rates may vary); Numbers by region assume an 800-ton chiller operating

![](images/b978e33c91f1e72028954058aa51fc15486e68053709be44eeb7ba2c6f1fdf57.jpg)

Source: Bernstein Analysis

## What is a chiller?

A chiller is a piece of equipment, which, as the name suggests, reduces the temperature of a stream of matter (usually a liquid). In the context of a data center, chillers are useful not only for liquid cooling (to cool the FWS) but also in air cooled environments where cold water flows to a CRAH to reduce the temperature of air that flows through it. Any chiller runs through a refrigerant compression cycle; this has four stages of operation as described below.

Evaporator: The warm liquid that needs to be chilled exchanges heat with cold liquid refrigerant in the chiller. This refrigerant picks up heat from the warm water and cools it, evaporating in the process.

Compressor: The most energy intensive part of a chiller. A compressor (scroll, screw, centrifugal) compresses the gaseous refrigerant, increasing its temperature. This is done to create a higher temperature gradient which makes heat transfer easier at a later stage.

Condenser: The hot, high-pressure, gaseous refrigerant comes into thermal contact with another stream of heat rejection (usually cool water in the case of a water-cooled chiller or ambient air in the case of an air-cooled chiller). The difference in temperature between the hot refrigerant and the cool heat sink facilitates heat rejection from the former to the latter. The refrigerant temperature lowers, and it condenses as a result (reverting to a liquid state).

Expansion valve: High pressure, liquid refrigerant passes through an expansion valve. This rapidly reduces pressure, which in turn reduces the temperature of the refrigerant (but keeps it in a liquid state). From here, the liquid refrigerant flows back to the evaporator and the cycle repeats.

EXHIBIT 3: Physics of Chiller Operation  
![](images/6dcd6a142214db143eef56f7fa8128117ab3a1866af7651a02faa444d10bed68.jpg)

## Types of chillers

In general, comparisons are made between two types of chillers - air-cooled and water-cooled. The differences due to how the condenser rejects heat to the environment; if air is used it is air-cooled, if water is used (either through a dry cooler, or more commonly a cooling tower) it is water-cooled. There are some performance trade-offs from choosing one type of chiller vs. another. Air-cooled units are much less energy efficient (\~30% worse than water-cooled unit) but have lower up front capex and do not require any water to operate. In contrast, water cooled chillers are much better at heat transfer to the environment, so the compressor needs to do less work reducing their energy bill. But they do need water in most cases (although some dry cooler configurations solve that issue) which can shift the balance (especially in free-cooling environments where power usage for both air-cooled and water-cooled chillers drops significantly while water consumption stays relatively constant). We explore this cost-benefit analysis later in our note.

EXHIBIT 4: Air-cooled vs. Water-cooled Chillers  
![](images/0f1aed57bc5d063446552c0c445400e6387c556380d09312d8d6b8a48e68ad16.jpg)  
Source: Bernstein Analysis and Estimates, Company Reports

More as a point of clarification, we would also like to highlight the different types of compressors in chillers. OEMs regularly talk about scroll vs. screw vs. centrifugal chillers, and it is worth understanding how they differ. Scroll chillers generally do not see data center applications; they are small, simple, silent units with limited ability to scale. Screw compressors are mid-sized units and see data center deployment. They are more complex and better at handling variable loads. Finally, centrifugal compressors see deployment in large scale data center environments; most OEM flagship products launched today are centrifugal chillers. These are the most complex, and require significant engineering to stand up but also deliver the most cooling power.

EXHIBIT 5: Comparison of compressors  
![](images/ab239313df6ab8afd5d2f07392bf67d9d1a3c260fa1d157cced00457e55052da.jpg)  
Source: Images from Atlas Copco and Engineeringlearn.com

Most appropriate for data center loads

Source: Bernstein Analysis

## How big is the market?

We have seen a wide dispersion of market sizes for chillers. Part of it also depends on what you are referencing - just the unit, or all the ancillary pieces that come with it? We have used a top-down estimate to size the overall market using GW added as a starting point. While we do have a base / bull / bear case for chillers in the exhibit below, these are based on variation in chiller penetration (not in terms of GW added). Our approach is as follows.

First, we look at new GW capacity being added each year. This creates a thermal baseline in terms of power consumed. Most of that power is released from chips, with an additional factor (assumed to be 1.2x in our model) to account for power wastage and headroom for safety. Next, we assume a cost per ton of \$1,500. This is a blend of both air cooled and water cooled chiller capex and includes the unit, engineering + commissioning + any supporting equipment that is needed (pumps, cooling towers, etc.). Finally, we multiply this by the share of GW that are cooled using chillers (75% in 2026 since it is how the majority of cooling takes place, but with base, bear, and bull cases for chillers based on how that could evolve). We size the fully loaded market for chillers at \~\$8B in 2026, growing to \~\$16.5B in 2030 assuming chillers continue to cool the same share of DC compute. In our bear case, where dry coolers steal share, the number drops to \~\$9B, while in the bull case where chillers gain share we size it at \~\$20B. This implies annual growth rates of \~20%, <5%, and >25% in the base, bear, and bull cases respectively.

Naturally, this model is sensitive to any assumptions you may have (especially GW added which can vary substantially between sources). The benefit of our approach is that one can relatively easily modify these assumptions and see what the market would be accordingly.

EXHIBIT 6: Chiller Market Size (Fully loaded) by Scenario  
![](images/f13686c112d0e19e53cd5822f750545784bd4c284241ea4147abee1da00b615e.jpg)  
Source: Bernstein Analysis and Estimates, McKinsey Data Center Model (for GW), CSE mag for cost per ton with 3% annual inflation

## Air vs. Water ... what's better?

Both air-cooled and water-cooled chillers have clear niches. Generally, air-cooled chillers make more sense when power costs are low (because they consume more power at a given tonnage vs. water-cooled chillers) or if water costs are high / water is limited / unavailable. In contrast, water-cooled chillers make sense in water-rich environments / when water costs are low or when power costs are high (since they are more energy efficient). When running at 100%, the extra cost of using water in a water-cooled chiller is more than offset by the savings in power.

However, this dynamic does change when you start to leverage free cooling (especially if you have a water-side economizer). In this environment, the compressor is switched off / used less, significantly reducing power consumption. But water consumption from a cooling tower continues, which keeps water costs relatively constant. At very high free cooling ratios, this could mean that the power savings from using a water-cooled chiller are actually offset by the cost of water. Given the increased focus on

water management in data centers (some counties have even capped the amount of water a data center can consume) we think it could help make the case for air-cooled chillers long-term over water-cooled units. The only exception is when the water-cooled chiller uses a dry cooler vs. a cooling tower (which JCI now advertises as possible with their new York HT chiller unit, although this likely comes with higher power costs due to higher lift).

EXHIBIT 7: Water costs can overtake power in modes with high free cooling (assumes use of cooling tower)  
![](images/ca49a0e6511e9ffd654e54e277e0ff7b47f88a5b9e5df89db7c9574d77fd763d.jpg)  
However, this is based on national averages for power and water costs; reality-will look quite different based on the region of operation

## Source: Bernstein Analysis and Estimates

There is some variation by geography, largely dependent on the ration of power to water costs. In areas like Atlanta, where water costs seem to be high, air-cooled outperform water cooled chillers with as little as 50% free cooling while in most other key data center markets in the US, it takes more free cooling before the attractiveness flips. We are hearing from players in the space that air-cooled chillers are gaining popularity over water-cooled units (although the latter still remains important).

EXHIBIT 8: Air-cooled vs. Water-cooled; when do you deploy it?  
![](images/6dc0dcbafa47114b80c660b0ff34571a50ce2bb71c35263a2e396404bad31e4d.jpg)  
Note: Power costs are \$10.25, \$6.26, \$6.7, \$9.19 per 100 kWh for NoVa, DFW, ATL, ORD from EIA; Water costs are \$12.5, \$11, \$20, \$10 for NoVa, DFW, ATL, ORD pulled from reg

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
