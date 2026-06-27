你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`Citi`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Economic Outlook & Strategy

## The Resilient Global Economy—Cascading Supply Shocks

![](images/ad92b51d5d6b7c5872e1020da1291e1f95f6e8a455dfcad0e2e368eeb86a641b.jpg)

## CITI'S TAKE

The interim agreement between the US and Iran has eased some key headwinds restraining the global economy. Even so, it's too soon to say that the challenges are behind us. The durability of the deal remains to be seen, and the conflict has damaged infrastructure across the Middle East. The good news is that the global economy has absorbed a sustained period of oil prices above \$100/barrel, and we judge that global growth is tracking at 2½%, down from 2.9% prior to the conflict. Meanwhile a new risk to the global economy may be emerging. NOAA ascribes a greater than 95% probability to an El Niño event lasting through March 2027, with a 63% chance it reaches very strong or super status by year-end. Historical episodes of this severity have generated substantial and long-lasting economic costs, primarily through disrupting agricultural output, energy generation, supply chain logistics, and reducing labor productivity.

Nathan Sheets $^{AC}$ +1-212-816-2991
nathan.sheets@citi.com

Josh Williamson AC
+61-2-8225-4904
josh.williamson@citi.com

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

Jamie Searle $^{AC}$

+44-20-7986-9493

jamie.searle@citi.com

Tomohisa Fujiki $^{AC}$

+81-3-6776-4684

tomohisa.fujiki@citi.com

Next Issue: 23 July

## Contents

The Resilient Global Economy—Cascading Supply Shocks 3
Implications for Macroeconomic Projections 6
El Niño: Hello to a Weather-Induced Supply Shock 7
Region-Specific El Niño considerations 12
Global Commodities: (Strong) El Niño is a real threat to global agricultural yields 19
Select Economy Discussion 24
North America 24
United States 24
Canada 25
Euro Area 26
Germany 27
France 27
Italy 27
Spain 28
United Kingdom 28
Scandi 30
Sweden 30
Norway 30
Japan 30
Australia & New Zealand 31
Australia 31
New Zealand 32
China 33
India 34
South Korea & Indonesia 35
Hong Kong, Singapore & Taiwan 36
Czech Republic, Hungary & Poland 37
Turkey 38
Nigeria, Saudi Arabia & South Africa 39
Brazil & Mexico 40
Argentina, Chile & Colombia 41
Global Equity Strategy 43
Developed Markets Rates Strategy 44
US Rates 44
Core Europe and EGB spreads 44
UK 45
Japan 45
Commodities 46
Global Foreign Exchange Outlook 48
Appendix A-1 50

# The Resilient Global Economy—Cascading Supply Shocks

Joshua Williamson
+61 (2) 8225-4904
josh.williamson@citi.com

Faraz Syed
+61 (2) 8225-4943
faraz.syed@citi.com

Cole Langlois
+1-212-816-7649
cole.langlois@citi.com

The global economy has remained resilient despite numerous headwinds. Whether measured by PMIs (Figure 1), the performance of equities or surprise indices, global activity metrics have remained broadly consistent with moderate growth not too far below trend. This is despite the propagation of cyclical negative supply shocks from various conflicts, protectionist trade policies and broader structural factors such as ageing populations and low productivity growth. Some of the resilience reflects stronger AI spending, support from fiscal policy and slightly accommodative monetary policy settings. However, a net-balance of the number of central banks Citi covers are starting to normalise monetary policy (Figure 2), while increased scrutiny over rising levels of public debt suggests fiscal policy cannot indefinitely support global growth to the same degree.

![](images/fe7d64693d3c6235ef267a729565c51f6c10778bd8a4808b3e15b729871f7bd3.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, S&P Global, Haver Analytics

Figure 2. Global Central Bank Rate Cycle (Net)\* Number of Central Banks  
![](images/db3010f5a4d648df0b4ba2bb7c7ddd677a6a26f90bfd9c2a8be29343fcb36624.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
\*Net number of hikes or cuts across 27 central banks.  
Source: Citi, Bloomberg

The most recent supply-side shock is (hopefully) ending. The performance of risk assets and energy markets in recent days portends a turning point in the Middle East conflict. The confidence of markets was validated with the Presidents of the United States and Iran signing a memorandum of understanding (MoU) aimed at ending the conflict. This document now provides 60 days to find solutions for the issues that have undermined stability in the region. These issues include a number of nuclear, financial and trade sanctions and regional security arrangements. History suggests these issues will not be solved quickly, but with both sides at least at the negotiating table, the health of the global economy no longer appears to be hostage to the price and availability of liquid fuels.

The Strait of Hormuz should re-open... Negotiations between previously warring parties will hopefully lead to sustained higher Strait of Hormuz (SoH) vessel flows after four months of substantially reduced crossing (Figure 3). Even if the recent agreement proves durable and the Strait remains open, we see Brent oil prices averaging roughly \$75/barrel in the second half of the year. This is \$15/barrel higher than we anticipated before the conflict, reflecting damages to production, pipeline, and refining capacity, as well as increased demand for oil to restock inventories. On the other hand, the MOU allows Iran to significantly increase its oil exports, which could be an important source of additional oil supply.

Figure 3. Strait of Hormuz Large Vessel Crossings Per Day  
![](images/5954a3cdd2040262d09cfc5607e4e51a6984504ce19aafad3ad21bd81215c0b9.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Bloomberg

Figure 4. Brent Oil Price: February vs. Current Forecast (Citi) \$/Barrel  
![](images/dae2d6aa35d6dbc58d2a00620d1711fd63464caea2d308b189b71bcb97201bd9.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Bloomberg

...but this may take some time. A political agreement to reopen the SoH (Figure 5) is not the same thing as restoring confidence that vessels can safely navigate it. First, mines that have been laid will need to be disarmed and removed. Minesweeping and independent verification of safe water could take months not weeks. Second, ship captains, vessel owners and insurers are likely to want to know details of how sea traffic will operate including designated shipping lanes, control systems and who will manage shipping traffic including what role the US Navy and Iran will have in vessel management. Third, insurance premiums remain high and some voyages may not be commercially feasible until insurance costs decline. Fourth, Iran expects to charge some form of transit or administration fees for vessel crossings after the 60-day MoU period. The compatibility of doing so with international law and sanction compliance needs to be agreed between all parties. Fifthly, roughly 500 commercial vessels occupy the Strait. This will need to be cleared before incoming sea traffic can return to normal. Nevertheless, these issues are solvable, meaning tanker and other sea traffic movement through the SoH will eventually return to normal. Symbolic examples of reopening such as news of an LNG tanker and a few very large crude carriers successfully transiting the Strait are, at the very least, an encouraging sign.

Figure 5. Summary of MoU arrangements for the SoH

<table><tr><td>Feature</td><td>Description</td></tr><tr><td>Initial Arrangement</td><td>60-day period; Iran to make &quot;best efforts&quot; for safe, toll-free passage of commercial vessels.</td></tr><tr><td>Toll-Free Traffic</td><td>Passage is free of charge for an initial 60-day period.</td></tr><tr><td>Reopening Timeline</td><td>Immediate traffic; military obstacles and de-mining operations fully cleared within 30 days.</td></tr><tr><td>Future Management</td><td>Iran to hold dialogue with Oman and other regional Gulf states for long-term administration in line with international law.</td></tr><tr><td>Conflicting Views</td><td>U.S. &amp; Regional Partners: Seek permanently free navigation.Iran: Expects transit fee/service charge after 60-day period.</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.
\* Dotted bars indicate Citi forecasts.
Source: Citi

## Implications for Macroeconomic Projections

The US-Iran interim agreement has eased key headwinds for the global economy, with Brent oil prices declining towards \$75/barrel. That said, the jury is still out on whether this resolution proves lasting, with thorny issues remaining — particularly regarding Iran's nuclear program and Strait toll rights. The good news is that the resilience of recent years appears to be prevailing yet again. The global economy has absorbed a sustained period of oil prices above \$100/barrel, and we judge that global growth is tracking at 2½%, down from 2.9% prior to the conflict (Figure 6).

Figure 6. Global Real GDP Growth (Annual Average)\*  
![](images/e218e1d79a0e47442a4a693cc9aa93af46ab29152592c866daaf370a3e899569.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
\*Dotted bars indicate Citi forecasts.

Figure 7. 2026 Growth Forecasts: Delta Since Feb (Citi)  
![](images/cc01e627c1cd82639e358741a6f643633cddc15a3f4f07bd24ee35c28682e885.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi

Figure 8. Global Headline Inflation (Annual Average)\*  
![](images/153bd270fa53de34c5091c940f18d8993627484732ad80a0acfb0801b4359fc0.jpg)  
Source: Citi

Figure 9. 2026 Headline Inflation Forecast Revisions (Citi)\*  
![](images/bf60e3a1ee2f11e0aafdd6d13423253b98cbc519865171144b53b4edca1be6f0.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
\*Change from February forecasts; US forecast is for PCE.
Source: Citi

The impact on growth has shown differing severity across economies (Figure 7). Several highly exposed oil importers—including the Philippines, Vietnam, and Sweden—have seen the largest markdowns since the conflict erupted, tipping the scales at $\frac{3}{4}$ ppt or greater. We have marked down euro area growth somewhat further, as US tariffs continue to exert downward pressure on growth.

Cumulatively, growth in the euro area has been revised down by 1 ppt since February to 0.3%, but a large share of the markdown reflects volatility in Irish trade data. In contrast, the Big Four euro area economies have fared a notch better, with a downward revision of $\frac{1}{4}$ ppt since February.

Our forecast also highlights that the AI revolution has provided an important source of support for the global economy. This has been seen in buoyant AI-related investment in the United States. During the first quarter, it surged to well over \$400 billion (annual rate), from just \$300 billion last year. Surging AI demand has provided a boost to other countries as well, with a number of Asian economies — including Korea, Taiwan, and Singapore — registering upward revisions to their growth forecasts on the back of soaring tech exports.

Global headline inflation is tracking at 3.4% this year, slightly lower than last month as oil prices have eased (Figure 8), but still up almost a full percentage point since the conflict erupted. That said, we expect the pass-through of elevated oil prices to unwind and headline inflation to fall back to 2.7% next year.

At the country level, the mark-ups in our inflation forecasts have been significant and broad-based (Figure 9). The largest mark-ups have been among Asian economies — including the Philippines, Thailand, and Vietnam — which have all been revised up by 1½ ppt or more. A few European countries, mainly Italy and France, have also seen meaningful mark-ups. Notably, our projections for the US and the euro area are both up 1 ppt from February.

## El Niño: Hello to a Weather-Induced Supply Shock

While one supply shock is abating, another one may be around the corner. The Pacific Ocean's El Niño Southern Oscillation (ENSO) is a large driver of climate variability. Consisting of three phases; neutral, La Niña (cooler temperatures) and El Niño (warmer temperatures), the El Niño phase occurs every three to five years and lasts for roughly one year in duration. This weather system tends to develop in Q2, strengthen in Q3 with the full impact occurring in Q4 and subsequent Q1 of the following year. Monitoring of ENSO occurs via the sea surface temperature (SST) in the tropical Pacific Ocean. This can be done via comparing temperature differences against a baseline period (traditional method) or by comparing temperature differences against an average for the broader tropical region (relative index method). The latter method makes it clearer when Pacific Ocean temperature differences are a sign of ENSO activity, rather than part of the long-term warming trend. A strong El Niño can vary temperature and rainfall over the US, Mexico, South America, Australia, Oceania, India and Sri Lanka, South East Asia, southern and equatorial Africa (Figure 10).

Figure 10. El Niño and Precipitation  
![](images/1f911fba30bbc01acd972cf8dae68dbbc7419aea00386c6c37b9ceec13939d65.jpg)  
Source: Citi, noaa.gov

A super El Niño event is now expected. The US National Oceanic and Atmospheric Administration (NOAA) threshold for an El Niño event is when tropical Pacific Ocean SST anomalies are above +0.5 degrees Celsius for five consecutive overlapping three-month periods. Secondary evidence for El Niño comes from wind pressure patterns as measured by the Southern Oscillation Index (SOI). SST anomalies meant the probability of an El Niño event increased from 20% across April, May and June to 61% in May, June and July. This assessment was issued by NOAA in April this year. Since then, the probability of an El Niño starting in Q2 and lasting until March 2027 has increased above 95% (Figure 11). Furthermore, NOAA estimates that the strength of the El Niño will increase to a very strong or super El Niño (> +2 degrees Celsius). By the end of the year, NOAA ascribes a 63% probability to this occurring. Further support for a 2026 super El Niño comes from the fact that the rate of warming this year is already the fastest since 1943. The Australian Bureau of Meteorology's seasonal model is forecasting a record peak warming greater than 3 degrees Celsius, above the previous post-1900 record of 2.65 degrees Celsius recorded in 1902.

Figure 11. ENSO Strength Probabilities (issued June 2026)  
![](images/3609cbf46e5a4569d32d9fa744c245d413193cd1b097224762f7d98caa60b821.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, NOAA

## Potential economic impacts of El Niño

El Niño significantly impacts the global economy by disrupting agricultural output, damaging infrastructure, and reducing labor productivity. Historically, these cycles have resulted in substantial economic losses. The primary economic impacts are observed across the following sectors:

Agriculture and Food Security: El Niño alters rainfall patterns, which can lead to droughts in regions like Southeast Asia, India, and Australia, but excessive rainfall and the risk of flooding in the southern United States and parts of South America (Figure 10 again). This can negatively affect the supply of crops, increasing global food prices and consumer inflation.

■ Energy Generation and Utilities: Countries that use hydro-electric power, such as Brazil, Colombia, Venezuela, Zambia, and Zimbabwe are at risk of reduced water levels due to drier conditions and heatwaves. This places pressure on power grids, increasing reliance on more expensive fossil fuels. Power fluctuations and outages can occur, disrupting commercial and industrial activities.

■ Supply Chain and Trade Logistics: Extreme weather and reduced water levels (e.g., in the Panama Canal) force ships to carry lighter loads and restrict shipping capacity. Flooding can damage critical infrastructure like roads, warehouses, and ports, leading to logistical bottlenecks and delivery delays.

■ Mining and Commodities: Changes in rainfall patterns can hinder natural resource extraction. For example, excessive rain in Chile's mountains affects copper mining, while droughts in Indonesia impact water supply for nickel operations.

■ Fisheries: El Niño disrupts the upwelling of cold, nutrient-rich waters in the Pacific, depriving small fish species (like anchovies and sardines) of food. This can impact the commercial fishing industry and local coastal economies.

■ Labor Productivity and Health: Extreme heatwaves decrease outdoor labor productivity and increase heat-related illnesses, especially in tropical and developing nations.

## Potential policy Impacts of El Niño

Strong El Niño events directly influence fiscal policy, especially when associated with natural disasters. From the perspective of public finances, strong El Niños can represent a contingent liability. The immediate effects include extra social transfers including spending on income and housing support for affected households, subsidies for affected businesses and other disaster relief payments. Medium- and long-term liabilities include recovery and reconstruction costs for infrastructure alongside some ongoing tax and loan concessions for businesses. Countries with recurring strong El Niño events are more likely to require countercyclical buffers to absorb disaster related spending. This can include mitigation spending to decrease future fiscal liabilities. But contingency reserves are not budget-neutral and come with opportunity costs to other policy areas. However, public authorities facing recurring El Niño events are more likely to view these events as real supply shocks that influence allocative efficiency. The role of the public sector is to distribute that loss efficiently, protect vulnerable sectors and households, and preserve the productive capacity of the economy.

For central banks, the response is less clear. As an isolated event, El Niño can be a relative price shock for agricultural commodities. Energy provision can also be affected when this depends

[中间内容因长度限制已省略]

r investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not

reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
