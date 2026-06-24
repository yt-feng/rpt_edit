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
# U.S. Semiconductors and Semiconductor Capital Equipment Bernstein Semi Cycle Tearsheet: The only game in town?

![](images/f16d8bd038a3618ecc41a1bc744b5b84ebf34c76a5c9fa73a13d46ef7b419ab4.jpg)

Stacy A. Rasgon, Ph.D.

+1 213 559 5917

stacy.rasgon@bernsteinsg.com

![](images/3d207974b298157df790004035d14b45ac2378da2d3d63043d08c14ba4a2ce22.jpg)

Alrick Shaw

+1 917 344 8454

alrick.shaw@bernsteinsg.com

![](images/95e0494e4c8fa49460295ac62e83d0b5ec5a17fd447b47e92f8bb68ab197bd59.jpg)

Arpad von Nemes

+1 917 344 8461

arpad.vonnemes@bernsteinsg.com

The only game in town? The AI theme has grown so large that it is now dragging everything in the space along with it (except, perversely, the AI compute names themselves). But the appetite to play the constraint/bottlenecks has continued as attention rolls from one to the other (hitting memory, semicap, optical/networking, analog/power, and, most recently, CPUs), and even intensified as investors pursue what, for many of them, remains the only game in town.

Step right up? But if you've been there, you've been rewarded with the SOX now returning $107\%$ YTD, dwarfing the S&P $(+9\%)$ . And while expectations and valuations have spiked over the last three months we continue to gain some solace in the fact that the performance so far this year has largely been driven by earnings growth, with forward EPS for the SOX up $75\%$ since the beginning of the year.

(Almost) everyone's a winner? So far AI demand continues to show no signs of slowing with all signs right now pointing to continued multi-year visibility and tight supply/capacity in virtually all needed components, and even many non-AI names have broadly been able to construct AI narratives. Overall we remain bullish on AI demand, and our AI compute names (perversely the only “losers” so far as “bottlenecks” have attracted more attention) are growing almost absurdly attractive if one believes the current trajectory has legs (which we suspect it does).

Own both NVDA and AVGO. We get the desire to play the bottlenecks instead, but they won't ultimately work if these don't; in the meantime demand shows no signs of slowing, and both stocks screen unreasonably cheap (NVDA and AVGO both rated OP).

Buy AMD on CPU and AI. We recently upgraded the stock (better late than never) on CPU and AI/GPU upside, and believe fundamentals can support a \$20 EPS in 2028, suggesting more to go. And we are feeling better about Intel than we have in a long time as both the market (CPU) and narrative (foundry, Trump etc.) grow more supportive, though fundamentals remain on the challenging side (AMD rated OP, INTC rated MP).

Semicap growing (much) more expensive but stay long as WFE still has upside, in our view. We like all names but lean toward AMAT if we had to pick on DRAM exposure and valuation (AMAT, KLAC, and LRCX all rated OP).

Torn on Qualcomm...We believe their smartphone business is in for some pain but clearly underestimated the appetite of investors to buy into any new halfway-credible datacenter story; we shall see if the upcoming analyst day can act as a further catalyst. (QCOM rated MP).

Analog in recovery, though expensive. In our coverage both TXN and ADI have already been growing double digits for a year or more, suggesting that not only have we hit bottom we might be heading (for some) into mid-cycle, and both stocks remain quite expensive especially as datacenter, while fast growing, remains small. NXPI is cheaper, and has admittedly handled this cycle well, but has a bit too much auto for us to be comfortable (TXN, ADI and NXPI all rated MP).

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">22 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>AMD (Advanced Micro)</td><td>O</td><td>USD</td><td>551.63</td><td>600.00</td><td>304.9%</td><td>USD</td><td>4.17</td><td>6.98</td><td>14.61</td><td>132.2</td><td>79.1</td><td>37.7</td></tr><tr><td>ADI (Analog Devices)</td><td>M</td><td>USD</td><td>445.48</td><td>430.00</td><td>69.9%</td><td>USD</td><td>7.79</td><td>12.40</td><td>14.65</td><td>57.2</td><td>35.9</td><td>30.4</td></tr><tr><td>AVGO (Broadcom)</td><td>O</td><td>USD</td><td>392.13</td><td>550.00</td><td>31.6%</td><td>USD</td><td>6.82</td><td>11.60</td><td>18.69</td><td>57.5</td><td>33.8</td><td>21.0</td></tr><tr><td>INTC (Intel)</td><td>M</td><td>USD</td><td>140.94</td><td>100.00</td><td>543.4%</td><td>USD</td><td>0.43</td><td>1.07</td><td>1.50</td><td>330.6</td><td>131.7</td><td>93.7</td></tr><tr><td>NVDA (NVIDIA)</td><td>O</td><td>USD</td><td>208.65</td><td>315.00</td><td>19.8%</td><td>USD</td><td>4.77</td><td>9.19</td><td>12.52</td><td>43.7</td><td>22.7</td><td>16.7</td></tr><tr><td>NXPI (NXP Semiconductors)</td><td>M</td><td>USD</td><td>323.24</td><td>270.00</td><td>29.4%</td><td>USD</td><td>11.81</td><td>14.58</td><td>16.45</td><td>27.4</td><td>22.2</td><td>19.6</td></tr><tr><td>QCOM (Qualcomm )</td><td>M</td><td>USD</td><td>221.90</td><td>140.00</td><td>21.4%</td><td>USD</td><td>12.03</td><td>10.64</td><td>9.77</td><td>18.4</td><td>20.9</td><td>22.7</td></tr><tr><td>TXN (Texas Instruments)</td><td>M</td><td>USD</td><td>332.28</td><td>250.00</td><td>42.4%</td><td>USD</td><td>5.45</td><td>7.62</td><td>8.22</td><td>61.0</td><td>43.6</td><td>40.4</td></tr><tr><td>AMAT (Applied Materials)</td><td>O</td><td>USD</td><td>640.18</td><td>525.00</td><td>252.6%</td><td>USD</td><td>9.42</td><td>12.17</td><td>15.56</td><td>68.0</td><td>52.6</td><td>41.2</td></tr><tr><td>LRCX (Lam Research)</td><td>O</td><td>USD</td><td>409.54</td><td>340.00</td><td>327.4%</td><td>USD</td><td>4.14</td><td>5.68</td><td>7.98</td><td>99.0</td><td>72.1</td><td>51.3</td></tr><tr><td>KLAC</td><td>O</td><td>USD</td><td>269.16</td><td>197.50</td><td>191.4%</td><td>USD</td><td>3.33</td><td>3.69</td><td>5.12</td><td>80.9</td><td>72.9</td><td>52.5</td></tr><tr><td>SPX</td><td></td><td></td><td>7,472.79</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

TXN estimate is Reported EPS; TXN valuation is Reported P/E (x); NVDA base year is 2026;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

AMD (Outperform, \$600.00): Expectations remain high, but exposure to AI demand driving both a CPU and GPU story can provide substantial growth.

ADI (Market-Perform, \$430.00): ADI is executing well with both cyclical and idiosyncratic drivers, though may be closer to peak, and valuations remain elevated.

AVGO (Outperform, \$550.00): A strong 2026 AI trajectory seems set to accelerate into 2027 and beyond, bolstered by software, cash deployment, and superb margins & FCF.

INTC (Market-Perform, \$100.00): Server strength is helping the company get back on their feet, and narrative/headlines may fuel the vibe for now.

NVDA (Outperform, \$315.00): The datacenter opportunity is enormous, and still early, with material upside still possible.

NXPI (Market-Perform, \$270.00): The pace and makeup of recovery remains open for debate.

QCOM (Market-Perform, \$140.00): Memory headwinds appear likely to pressure smartphone builds and numbers appear high; we shall see if datacenter dream is enough to attract buyers.

TXN (Market-Perform, \$250.00): TXN shares feel fully valued in the current environment.

AMAT (Outperform, \$525.00): Exposure to key inflections is strong & valuation vs peers is attractive.

LRCX (Outperform, \$340.00): The company is benefiting from key inflections (GAA, packaging, HBM, NAND upgrades) and CY26/27

commentary seems supportive.

KLAC (Outperform, \$197.50): Amid positive WFE trends KLAC possesses structural growth drivers, a strong and durable competitive position, lower China replacement risk, and disciplined capital allocation, warranting premium valuation.

## DETAILS

The AI theme has grown so large that it is now dragging almost everything in the space along with it (except, perversely, the AI compute names themselves even as their own fundamentals look like they continue to move up and to the right). But the appetite to play the constraint/bottlenecks has continued as attention rolls from one to the other (hitting memory, semicap, optical/networking, analog/power, and, most recently, CPUs), and even intensified as investors pursue what, for many of them, remains the only game in town.

But if you've been there, you've been significantly rewarded with the SOX now returning an astonishing 107% YTD, dwarfing the S&P by over 11x (9%) with many names up even more than that. And while expectations and valuations have spiked over the last three months (and with “bubble” commentary increasing apace) we continue to gain some solace in the fact that the performance so far this year has largely been driven by earnings growth, with forward EPS for the SOX up 75% since the beginning of the year (hence we feel we there could be far more craziness to come before we enter the true realm of the bubble...).

So far AI demand continues to show no signs of slowing; indeed all signs right now point to continued multi-year visibility and tight supply/capacity in virtually all needed components (something we suspect will not be resolving anytime soon); even non-AI names (with areas, especially in consumer electronics that will likely be adversely impacted especially on memory shortages as datacenters hoover up precious bits) have broadly been able to construct AI narratives. Overall we remain bullish on AI demand, and our AI compute names (perversely the only “losers” so far as “bottlenecks” have attracted more attention) are growing almost absurdly attractive if one believes the current trajectory has legs (which we suspect it does).

To that end, we would still own both NVDA and AVGO as key beneficiaries of AI demand and with valuations that scream attractive. We have turned more positive on the CPU trade as well (recently upgrading AMD partially on that call) and actually feel better about Intel than we have in some time (though while narrative and market are going their way fundamentals remain somewhat challenging for now). Semicap is growing more expensive but we would stay long as WFE outlook clearly has further upside; we like all our names but would lean a bit more toward AMAT on valuation. We are torn on QCOM; we believe their smartphone business is likely in for some pain but clearly underestimated the appetite for investors to latch onto any new halfway-credible datacenter story. And while our analog coverage looks to be well into recovery, valuations keep us sidelined.

We would own both NVDA and AVGO. The biggest question we are getting right now is “what will make these go up?” We suppose we get the sustainability worries but the companies actually doing the spending continue to show no signs of slowing, and ultimately the “bottlenecks” don’t work if these two don’t. Both appear unreasonably cheap as well, on numbers that are probably still too low; NVDA’s new “\$1T” number for Blackwell/Rubin through CY27 suggests likely material upside to current estimates, and AVGO’s \$100B AI revenue number (even without a raise) feels conservative to us (NVDA and AVGO rated OP, AMD rated MP).

Buy AMD on CPU and AI. We are growing more positive on the agentic CPU trend and in fact recently upgraded the stock (better late than never) on both CPU and AI/GPU upside, and believe fundamentals can support a \$20 EPS in 2028, suggesting more to go. And we are admittedly feeling better about Intel than we have in a long time as both the market (CPU demand so strong they are able to sell off products that by their own admission remain deficient) and narrative (yield progress, foundry datapoints, and Trump's largesse) grow more supportive, though fundamentals still remain on the challenging side for us (AMD rated OP, INTC rated MP).

Semicap is growing (much) more expensive but we would remain long. We think WFE continues to have an upward bias with particular strength in DRAM, leading edge, and packaging, and everything we are hearing on the AI demand side ultimately translates to more chips, more wafers, and more tools. We like all our names (AMAT, KLAC, and LRCX), and would likely lean a bit toward the first on DRAM exposure and valuation (AMAT, KLAC, LRCX all rated OP, and correcting KLAC model/PT for recent 10:1 split).

Torn on Qualcomm...We admittedly made a bad call on QCOM, downgrading the stock to Market Perform in March after pushing it as a top pick all last year, right in front of a datacenter love-fest that sent the stock up 70%+ in a matter of weeks (oops). Our rationale however was that their smartphone business is likely in for a world of pain on the back of memory-induced demand destruction (which seems to be happening) though we clearly underestimated appetite to buy any new halfway-credible datacenter story. The company has an analyst day this week though that we shall see if it can act as a further catalyst... (QCOM rated MP).

Analog in recovery, though expensive...In our coverage both TXN and ADI appear in solid recovery, though both remain quite expensive (30-40x P/FE) especially as the datacenter portions, while fast-growing, remain relatively small (\~10% of revenues or so). NXPI is cheaper, and has admittedly handled this cycle well, but has a bit too much auto for us to be comfortable (with auto seemingly later cycle than industrial) and is now filling their channel. Of the three TXN's story is now probably resonating the most given the end of their capex cycle and consequent increase in FCF though If we had to own one we'd probably go for ADI (better mix in industrial with solid defense and ATE exposure, and more honesty about possibility of auto pull-forward, and 10 turns cheaper than TXN) (TXN, ADI and NXPI all rated MP).

## TEARSHEET

1. Near-term revenue estimates are above seasonal. Negative impact, and similar vs March.

2. Q2/Q3 estimates are above seasonal. Negative impact, and worse vs March.

3. Negative revisions appear to have troughed. Recall that one typically wants to buy semi stocks after numbers have come down, but before they trough. Neutral impact, and mostly unchanged vs March.

4. Channel inventory days ticked down slightly and now sit above average though a bit below the high end of the historical range; \$ are still growing. Neutral to negative impact, though a bit better vs March.

5. Semiconductor company days of inventory ticked up again and remain very high, and \$ are growing. Negative impact, and mostly unchanged vs March.

6. Relative valuations at a \~60% premium to the S&P, up hugely vs our check 3 months ago (+6%). Negative impact, and worse vs March.

7. Sector crowding is very high relative to the market and above the high end of the historical range vs TMT. Negative impact, and worse vs March.

EXHIBIT 1: Expectations and valuations have risen in Q2

<table><tr><td>Indicator</td><td>Dec-25</td><td>Mar-26</td><td>Jun-26</td><td>Notes</td></tr><tr><td>Current Qtr Revenue Estimates</td><td></td><td></td><td></td><td>2Q26 growth expectations are above seasonal (Exhibits 45-46)</td></tr><tr><td>Forward Revenue Estimates</td><td></td><td></td><td></td><td>Q3/Q4 estimates are above seasonal (Exhibits 45-46)</td></tr><tr><td>Earnings Revisions</td><td></td><td></td><td></td><td>The pace of negative revisions appears to have troughed( Exhibits 47-48)</td></tr><tr><td>Channel Inventories</td><td></td><td></td><td></td><td>Inventory days ticked down bit and remain above aver

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
