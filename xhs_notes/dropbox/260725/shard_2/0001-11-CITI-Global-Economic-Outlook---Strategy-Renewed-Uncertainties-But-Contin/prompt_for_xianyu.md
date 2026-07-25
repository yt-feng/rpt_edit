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
# Global Economic Outlook & Strategy

## Renewed Uncertainties—But Continued Resilience

## CITI'S TAKE

The global economy has absorbed a significant shock with the higher oil prices that have followed the Iran conflict and the closure of the Strait of Hormuz. While the resulting pressures and uncertainties have taken a bite out of performance, the pain to date has remained manageable and the global economy has shown continued resilience. Notably, our forecast for global growth this year continues to run near $2 \frac{1}{2}\%$ , which is down only a couple of tenths from when the year began. This observation leaves us correspondingly more sanguine about the prospects for the remainder of the year, even if pressures in oil markets linger. The reality is that the global economy is less dependent on oil than in previous decades. In addition, only part of last year's sizable accumulation of petroleum inventories has been reversed, and global inventory levels generally remain ample.

A range of scenarios for oil prices remain in play—If shipments through the Strait resume, oil prices could plausibly fall back to \$70/barrel. However, if the tensions return in a more sustained way, oil prices above \$100/barrel are possible. With the November midterms fast approaching, President Trump looks to prefer a path of de-escalation, at least to the extent that Iran is willing to negotiate and follow through on its agreements. Accordingly, our baseline forecast continues to envision lower oil prices.

Surging AI spending is supporting global growth this year—By our reckoning, US AI investment has increased from just under \$300 billion last year (1% of GDP) to \$430 billion in Q1. Industry estimates for the entirety of this year see investment surging to \$600 billion. AI spending is also supporting activity in other economies, including China, Taiwan, Korea, Japan, and Singapore.

Our forecast for global headline inflation is up $\frac{3}{4}$ ppt from February—This reflects the direct effects of higher oil prices, as well as indirect pressures from supply-chain disruptions, increased transportation costs, and lingering second-round effects. At the country level, our forecasts for a range of economies including the US, euro area, Vietnam, and Brazil have been raised a full percentage point, while the mark-ups for Thailand and the Philippines are significantly larger.

Central banks have shifted to less accommodative policy stances—Across our panel of 27 major central banks, we now expect that twelve will be hiking this year, and another seven will be on hold. Of the eight projected cutters, six of them will be easing by 50 bp or less. Only Brazil and Hungary are slated to see more appreciable cuts.

Global resilience is a recurrent theme in our work—In recent years, the global economy has shown a remarkable capacity to shake off shocks and maintain solid growth. We think that this reflects increased flexibility and adaptability on the supply-side of the economy, perhaps driven by technological innovations that allow broad access to information and real-time communication.

![](images/3317c25d7fd7e34941b138de670220113716eab1614fd9cc1f5677f3098b19e3.jpg)

## Nathan Sheets $^{AC}$

+1-212-816-2991
nathan.sheets@citi.com

Johanna Chua $^{AC}$ +852-2501-2357
johanna.chua@citi.com

Arnaud Marès $^{AC}$ +44-20-7986-3299
arnaud.mares@citi.com

Ernesto Revilla $^{AC}$ +1-212-816-2621
ernesto.revilla@citi.com

Gina Schoeman $^{AC}$ +27-11-944-0813
gina.schoeman@citi.com

Daniel Tobon $^{AC}$ +1-212-816-8340
daniel.tobon@citi.com

Jason Williams $^{AC}$ +1-212-723-1837
jason1.williams@citi.com

Jamie Searle $^{AC}$ +44-20-7986-9493
jamie.searle@citi.com

## Tomohisa Fujiki $^{AC}$

+81-3-6776-4684

tomohisa.fujiki@citi.com

## Next Issue: 20 August

## Contents

Renewed Uncertainties—But Continued Resilience 3
Global Central Banks 6
Select Economy Discussion 13
North America 13
United States 13
Canada 14
Euro Area 15
Germany 16
France 16
Italy 16
Spain 17
United Kingdom 17
Scandi 19
Sweden 19
Norway 19
Japan 19
Australia & New Zealand 21
Australia 21
New Zealand 21
China 22
India 23
South Korea & Indonesia 24
Hong Kong, Singapore & Taiwan 25
Czech Republic, Hungary & Poland 26
Turkey 28
Egypt, Saudi Arabia & South Africa 28
Brazil & Mexico 30
Argentina, Chile & Colombia 31
Global Equity Strategy 33
Developed Markets Rates Strategy 34
US Rates 34
Euro rates and EGB spreads 34
UK 35
Japan 35
Commodities 36
Global Foreign Exchange Outlook 38
Appendix A-1 40

© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

Figure 2. 2026 Global Growth Revisions (Citi Forecasts)
Change Since Dec-25 (Pct Pts)

Nathan Sheets
+1-212-816-2991
nathan.sheets@citi.com

Cole Langlois
+1-212-816-7649
cole.langlois@citi.com

## Renewed Uncertainties—But Continued Resilience

Tensions between the United States and Iran continue to cast a long shadow over the global oil market. Only few weeks ago, oil prices were approaching \$70/barrel and shipments through the Strait of Hormuz looked to be normalizing (Figure 1). More recently, however, the conflict has resurged, and oil prices have jumped back up. This week, Brent prices have moved above \$90/barrel, and market participants are on heightened alert as they await further news from the region.

Clearly, a range of scenarios for oil prices remain in play. If the United States and Iran resume negotiations—and shipments through the Strait resume—we could see oil prices fall back to \$70/barrel. However, if the tensions return in a more sustained way, oil prices stubbornly above \$100/barrel are also possible. With the November midterms fast approaching, our view is that President Trump prefers a path of de-escalation, at least to the extent that Iran is willing to negotiate and follow through on its agreements. Accordingly, our baseline forecast calls for lower oil prices. But for now, this key source of uncertainty persists.

Figure 1. Brent Oil Prices (2026)  
![](images/87816f3b1c5b15deddd7f80ee1111bf6cd7cf2473e9faa142f1e32f3fb010f60.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Bloomberg

![](images/e91602dd836194ca7b6ae4b4784dc56df0d8a977cf8e3f19785b76da27e70c67.jpg)

The good news is that the global economy has shown continued resilience. Our forecast for growth this year is running near 2½%, which is down only a few tenths from when the conflict erupted (Figure 2). In recent years, the global economy has shown a remarkable capacity to shake off shocks and continue to record solid growth. We think that this has reflected increased flexibility and adaptability on the supply-side of the economy, driven by technological innovations that facilitate access to information and real-time communication.

Figure 3. Global PMIs: Manufacturing & Services
50+=Expansion  
![](images/9c22a34aa6731c98b72948f1269ac00411658fc8d6043985c3fc4e5989d60517.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, S&P Global, Haver Analytics

Figure 4. Global Electronics PMI & Computing Subindex 50+=Expansion (3mma)  
![](images/a70a030e5e1d0cb4c32ce5a065bf699da8f62dc671df0174bbb3f7ec44d24eb3.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, S&P Global, Haver Analytics

This theme is reinforced by the recent performance of the global PMIs (Figure 3). The global services PMI retreated as the tensions erupted, but it has since moved back up and is running comfortably above 50, the breakpoint between expansion and contraction. The manufacturing PMI has been on an upward climb since late last year. This reflects burgeoning AI spending following the release of powerful agentic tools in late-2025. Consistent with this observation, the global electronics PMI has surged upward in recent months (Figure 4). The manufacturing PMI has also reflected more temporary factors, including a surge of inventory demand in an effort to front run disruptions from the conflict.

Despite the higher oil prices, the global economy has been broadly supported by rising AI spending. By our reckoning, US AI investment—where we have the cleanest data—has surged from just under \$300 billion last year (1% of GDP) to \$430 billion in Q1. For 2026 as a whole, industry estimates put likely spending at \$600 billion (nearly 2% of GDP). $^{1}$

In our view, this AI spending has considerable momentum, and it looks robust and likely to continue. However, given the pace of its ascent and the lofty valuations that have emerged, a slackening in the pace of increase—or even a temporary reversal—are plausible downside possibilities that remain on our radar screen. Despite the risks of near-term volatility, we’re convinced that AI is a robust technology that will significantly raise levels of productivity growth over the longer term. $^{2}$

These themes are also echoed at the country level. Figure 5 displays revisions to our growth forecasts since the onset of the US-Iran conflict. Notably, three tech intensive economies—Taiwan, Korea, and Singapore—have seen significant mark-ups in recent months, as soaring AI demand has supported growth. Conversely, our projections have been lowered appreciably for oil importers that don’t produce AI, including the Philippines, Sweden, Chile, and the euro area. Our US forecast is down just a couple of tenths.

Figure 6 reproduces this exercise for our headline inflation forecasts. Our global projection is up $\frac{3}{4}$ ppt from February. This reflects both the direct effects of higher oil prices, as well as indirect pressures due to supply-chain disruptions, increased transportation costs, and lingering second-round effects. $^{3}$

At the country level, headline inflation forecasts for a range of economies including the US, euro area, Vietnam, and Brazil have been raised a full percentage point, while the mark-ups for Thailand and the Philippines are significantly larger. Of those countries posting smaller increases, several of them—including Indonesia, China, and India—have mechanisms in place to constrain the pass-through of higher oil prices to domestic inflation.

Figure 5. 2026 Growth Forecasts: Delta Since Feb (Citi)
Pct Pts  
![](images/dafb1037542bdeced3705bed4afb0c008d6cff7a8c798bbb66f893b8ed044e1d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi

Figure 6. 2026 Headline Inflation Forecast Revisions (Citi)\* Pct Pts  
![](images/eea238d3f5bc710b786181e298ecf0588269bc3991377a839065974087c418e2.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
\*Change from February forecasts; US forecast is for PCE.
Source: Citi

Clearly, there are both upside and downside risks to our inflation forecasts, depending on the trajectory of oil prices through year-end. If the US and Iran return to negotiations and oil shipments through the Strait resume, inflation could yet undershoot our projections. However, there are also risks of higher inflation in the event that oil prices return to over \$100/barrel.

In sum, the global economy has absorbed a significant shock with the higher oil prices that followed the Iran conflict and the closure of the Strait of Hormuz. As recent developments highlight, this shock remains very much in play. While the resulting pressures and uncertainties have taken a bite out of global performance, the pain to date has been more manageable than we had expected.

Figure 7. Energy Intensity of GDP  
![](images/a54c830a2cfc08a7069f82ad5d0c69bcba96659a55f805c7358f45ff40fd1c48.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, Energy Institute, Haver Analytics

Figure 8. Global Inventories: Oil & Refined Products  
![](images/3d11bbcc224aee062baa366f4109c933c82ce2d01961d0414595bbabeeec9ef4.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, OilX, OECD

This observation leaves us correspondingly more sanguine about the prospects for the remainder of the year, even if pressures in oil markets linger. The reality is that the global economy is less dependent on oil than in previous decades (Figure 7). In addition, only part of last year's sizable accumulation of petroleum inventories has been reversed, and global inventory levels are generally still ample (Figure 8).

The remainder of our essay draws on this discussion to examine the shifting terrain and associated policy challenges facing global central banks. Relative to our expectations before the conflict erupted, monetary policy looks to be on a less supportive trajectory, as central banks seek to get inflation back to their targets.

## Global Central Banks

As the year began, major global central banks were in the midst of an easing cycle, which was unwinding the rate hikes in the aftermath of the pandemic (Figure 9). Since the onset of the Iran conflict, however, central banks have faced increased inflationary pressures and, in many cases, slippage in efforts to achieve their targets. While this slippage was driven primarily by higher oil prices (Figure 10), many central banks were hesitant to reprise their post-pandemic strategy of “looking through” an evolving supply shock. Although this more muscular response risks “overlearning” the lessons of the previous episode, central bank communication and market pricing have shifted markedly in the direction of tighter policy.

Figure 9. Global Central Banks: Hikers vs. Cutters
Number of Central Banks  
![](images/7b230bf423108fed9ae39424696ad4ccf3b9a8d775149fe4c93b9213e591021a.jpg)  
\*Across 27 major central banks, net number hiking (+) or cutting (-) rates. Source: Citi, National Statistical Sources, Haver Analytics

Figure 10. Global Inflation\*  
![](images/2670c2e4dc018eef50fd0030a7feb34a1a660aca22560b244b4016c2fa9441f6.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
\*Headline, core, and energy inflation cover 15 economies.
Source: Citi, National Statistical Sources, Haver Analytics

Figure 11. Policy Rate Changes in 2026 (Citi Forecast)  
![](images/700a2ccdedda9645cdb8f9afe6ab0c8e4afa768aebcc72c79fb1957828a1108e.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

Figure 12. Policy Rate 26Y/E Forecasts: Delta Since Feb (Citi)  
![](images/eaa51f023629f93cd9a4c63a6740854c3cdc650bd65f1e83ef81dc057b4c5981.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

Across our panel of 27 major central banks, the balance between cutters and hikers has moved toward less-supportive policy. For example, during June, five central banks lifted rates, including the ECB, the Bank of Japan, and the Bank of Indonesia. Accordingly, we now expect that twelve of these 27 central banks will be hiking this year, and another seven will be on hold (Figure 11). Of the eight projected cutters, six of them would be easing by 50 bp or less. Only Brazil and Hungary are projected to record more sizable cuts.

This story is distinctly different than before the Iran conflict. Across our panel, seventeen now have less supportive policy paths than in late February, and for nine others the policy path is unchanged (Figure 12). Projected policy rates at year-end are tighter by over 200 bp in Brazil and 100 bp or more in the Philippines, the UK, Indonesia, and South Africa. Only Hungary is slated to see easier policy; in this

case, currency appreciation following Orban's defeat in the presidential election has given the central bank increased scope to provide support.

A convincing (and sustained) resolution of the conflict in Iran could yet bring a markedly lower trajectory for oil prices. But at present, such resolution does not look imminent. While we expect that negotiations will res

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
