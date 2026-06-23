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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Power Tracker: US Markets Tightening Into Summer, Only Marginally Eased by Coal Power Policy

■ Regional divergence in focus as summer starts. June 1 marks the rollover of 1-month forward contracts across regional power markets from trading June contracts to trading July contracts. This transition reveals market expectations on peak summer power market tightness, along with generation fuel costs. We see contrasting trends between PJM (Mid-Atlantic) and ERCOT (Texas) power markets:

□ PJM (Mid-Atlantic): The power price increased significantly more during this year's May-to-June rollover compared to the historical average in the past decade, both in terms of the absolute price level (+28 USD/MWh in 2026 vs +15 USD/MWh in 2016-2025) and the percentage change (+44% vs +30%, Exhibit 1), despite prices of marginal generation fuels, natural gas and coal, increasing much less. This larger price increase into the summer, combined with its upward trend since 2020 (Exhibit 1), is consistent with our view of a tightening power market in the region: PJM hosts 39% of US data center power demand capacity, where power demand growth has continued to outpace power supply growth.

☐ ERCOT (Texas): While the ERCOT market also experienced its typical seasonal price increase rolling over into June, the absolute price rise of \$24/MWh was smaller than the previous decade's average of \$30/MWh and the percentage increase was just above the historical average (61% versus 56%, Exhibit 1). In addition, the price levels in both May and June have been lower than in 2024/2025, driven by the recent softening in the Texas market $^{1}$ .

☐ Regional divergence: This rollover contrast between these two regional markets is consistent with our regional divergence view that ERCOT has entered a softening path since late-2025 with substantial expansion in power supply, while we expect PJM to remain critically tight in the next few years.

We expect federal support for coal power to offer marginal relief. To alleviate power market tightness, the US administration refreshed its support for coal power following President Trump's advocacy for "Beautiful Clean Coal Power" earlier this year. Earlier this month, the president announced a new plan to allocate nearly \$700 million to support coal power (and coal exports), mainly by

Hongcen Wei  
+1(212)934-4691 |  
hongcen.wei@gs.com  
GS & Co. LLC

Laura Cyr
+1(212)902-3435 | laura.x.cyr@gs.com
GS & Co. LLC

Daan Struyven +1(212)357-4172 | daan.struyven@gs.com GS & Co. LLC

Samantha Dart +1(212)357-9428 | samantha.dart@gs.com GS & Co. LLC

2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 financing delaying/canceling scheduled coal power retirements. While we expect this plan to effectively add incremental power supply relative to previous schedules, along with emergency orders of US Department of Energy (DOE) that direct coal power plants to remain online, we believe the overall impact on resolving market tightness could be marginal in 2026-2028 and after 2028 for the following reasons:

☐ Increasing difficulties for more retirement delays: A significant amount of scheduled coal retirements have already been delayed in the past year after the first DOE emergency order in May 2025, which pushed 2025/2026 retirements out to 2026-2029 (Exhibit 2). Remaining scheduled retirements could be subject to physical/financial constraints: already delayed retirements may face a higher bar to be delayed again and most coal plants are old, both lacking extensive maintenance given the original retirement schedules which could drive the cumulative maintenance costs beyond the scope of the \$700-million fund.

☐ Longer-term policy uncertainty: Coal power plants and coal producers continue to face regulatory and policy uncertainty beyond 2028, which disincentivizes significant capex to upgrade or even expand capacity. One example is the coal power retirement delays in the TVA (Tennessee) power market, where a total of 4.1 GW coal power generation capacity, all originally scheduled for retirement by the end of 2028, has been delayed, while retirement schedules beyond that window remain unchanged.

## Featured Charts

Exhibit 1: The rollover of power forward contracts show a higher-than-average June price level and May-to-June price increase in PJM vs lower-than-average in ERCOT

![](images/c2e167417cd3312dc65a17de29cfb9c8b26fdb9cf48b4b3d90904e8e11dab329.jpg)  
2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

![](images/c1ea60ee14881c617ce23175fcd597ab1d58735ab88de89c5376a8a042f1683b.jpg)  
Source: Bloomberg, GS Global Investment Research  
Prices of PJM in 2022 and of ERCOT in 2018 and 2022 are above 100 \$/MWh and not shown in the charts, but are counted in historical average calculations.

Exhibit 2: Coal retirement delays since 2025 have effectively increased power supply in the next few years, but are more constrained going forward

![](images/e05e152e7870313ce2cec552e3632e9d97e4556772e59de0f0d93d590c8ab35e.jpg)  
Based on EIA generator schedules released in late May 2026, which do not include some recent announcements/DOE orders that adjust the timeline of coal power plants' retirements  
Source: EIA, GS Global Investment Research

## Prices

Exhibit 3: ERCOT (Texas) early summer power price remains weak yoy, remaining below 60 USD/MWh
ERCOT North 345kV Hub peak load prices

![](images/ab299c38297e3dadf17930a48b991fecd488d335cce229edb6eb766ceafbcba2.jpg)  
Source: Bloomberg

Exhibit 4: Power prices in PJM (Mid-Atlantic) rally into the 90 USD/MWh range with the forward contract rollover  
PJM western hub peak power swap prices  
![](images/9806dd7310c67e57078c6c109561170459571f60514eb8b5d020821a60f92277.jpg)  
Source: Bloomberg

## Market Tightness

Exhibit 5: The PJM (Mid-Atlantic) power market was tightened by heatwaves into June  
![](images/3070667604d074edfc67ea56ed9593e7ff22363ec56ee0d5583b7962b4969b81.jpg)  
Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a given power market, indicating critical tightness if below 15%. Not showing in the chart if above 100% (a very soft market).  
Source: Regional power ISOs and RTOs, EIA, Bloomberg, GS Global Investment Research

Exhibit 6: The MISO (Mid-Continental) power market also turned tighter into June before softening this week  
![](images/b49771764ccb7c4402b9d0ef15a998a98c03519a88e8c64339a2d0a9cab7d09a.jpg)  
Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a given power market, indicating critical tightness if below $15\%$ . Not showing in the chart if above $100\%$ (a very soft market).  
Source: Regional power ISOs and RTOs, EIA, Bloomberg, GS Global Investment Research

Exhibit 7: The ERCOT (Texas) power market maintained a soft balance with mild weather  
![](images/9f0dd1cab75a3e6f3389f83559deb65227839c441e3bbf369d91c8470e98ff3f.jpg)  
Effective spare capacity for a day is calculated using daily peak-hour power demand and effective power generation capacity in the month in a given power market, indicating critical tightness if below 15%. Not showing in the chart if above 100% (a very soft market).  
Source: Regional power ISOs and RTOs, EIA, Bloomberg, GS Global Investment Research

## Demand

## Aggregate Power Demand

Exhibit 8: Total US yoy power demand growth strengthens to $2.3\%$ in March, but still below the annual yoy growth rate of $2.4\%$ in 2025  
![](images/af37a60079237c5818e66cc8de7c3793f082a67a36d0c5f6aa0a76764a2e0d1b.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 9: After weather adjustment, US total power demand growth in Jan-Mar2026 was $1.2\%$ , also below last year's growth  
![](images/84b760673f903218b32c04d0eb5aceea954ac5835815dbb5ae6470c385bd98dc.jpg)  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 10: The commercial sector continues to be the strongest sector in power demand growth in Jan-Mar2026 with a $2.7\%$ yoy growth rate  
![](images/d5492a00368d668451b86fb6729bb229405627d50af138779ae83c48741badfc.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research  
Exhibit 11: After a weak start of the year in Jan2026, US residential power demand remained flattish yoy in Feb-Mar

![](images/3da694ddda0497cf13cf2b39055a4417efa629b76941b8d9d2ca6445c027e25d.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 12: Industrial power demand strengthened into March after Jan-Feb2026 yoy weakness  
![](images/346a3b205ee2994b145659aa9058c0fb3c7c61e8b52eaad5bd79102bd73d8395.jpg)  
Not weather adjusted  
Source: EIA, Bloomberg, GS Global Investment Research

Exhibit 13: US power demand growth remained below US GDP growth through Apr2026 Weather-adjusted US total power demand (including small-scale solar power use) and US real GDP yoy, monthly  
![](images/57d0776233a3a3e176a85409043ae37e8baf4f50e9bf1192c70f1e2f282a2e9e.jpg)  
To avoid underestimating power demand, we include all small-scale solar power generation in US total power demand  
Source: EIA, Bloomberg, Haver, GS Global Investment Research

## Data Center Power Demand

Exhibit 14: Estimated data center power demand in Virginia continued to edge higher  
![](images/07e92786bf926dff23e039832a2225ec017ac06d0bdd4a5bb576f655412e9c8c.jpg)  
Not weather adjusted  
Source: Haver, GS Global Investment Research

Exhibit 15: US data center capacity continued to grow, which we expect to accelerate in June and also in 2H2026  
![](images/6b1c91082ce9eedc28f80b5146ab9d22562fcceadbc0d3cad30df57d72ed7874.jpg)  
Source: Aterio, GS Global Investment Research

Exhibit 16: Texas and Virginia led data center expansions in the past year, along with Arizona, Indiana, Ohio and Georgia

YoY Data Center Capacity Additions Across US States  
![](images/dd789f4dcf91d82b5f2253faa3d5c0f19d9f805386c7f530310075e8b39dae04.jpg)  
Source: Aterio, GS Global Investment Research

Exhibit 17: Ohio, Texas, and Virginia are leading data center development in 2026Q2  
Data Center Capacity Additions Across US States in 2026Q2  
![](images/5cb0228835929fa7d17c31b7500c9194d1757a2053ad67c97d4dd81b239bc4ec.jpg)  
Source: Aterio, GS Global Investment Research

Exhibit 18: We expect significant data center growth acceleration in both the US national and key regional power markets in 2026/27  
![](images/963da2565e7851c38a30516f46e4081924b5852d280aa9744e756f61969df124.jpg)  
Source: Aterio, GS Global Investment Research  
Exhibit 19: Construction employment related to US data center expansion continued its growing trend

![](images/90f8bc473a1d9b76d9af7c36740f4cf4ba91e4f50cbc76b128362bd9b28d768b.jpg)  
Source: Haver, GS Global Investment Research

## Supply

## Generation and Stack

Exhibit 20: US total power generation stayed in line in most of May before gaining strength into early-summer  
![](images/ef46e5db392563636b239b5346aa96b5485455c3e328f1d5bbddc4fa3b0c2306.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 21: After adjusting for weather, US total power generation holds in line with early-summer year-ago levels  
![](images/57fbe89e1b17f1415cda0a3d4ec34dadc383a25a86554e944b09c2a7f4e4e35a.jpg)  
Source: EIA, Bloomberg, GS Global Investment Research

Source: EIA, GS Global Investment Research

Exhibit 22: The thermal (natural gas and coal) share in US power supply continues to increase from mid-April given yoy weaker hydro and nuclear  
![](images/d1414fb2f5bffb43f72aa071e10145ab4b75e6ab3118c1955228ecd99411fa99.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research  
Exhibit 23: Within thermal power generation, the natural gas share remained higher yoy given price competitiveness

![](images/f450376b1b30cb0700c7b8a3f88ab2df1d5163d3359d3d3e168e7a2478fdf8d5.jpg)  
Not weather adjusted

Exhibit 24: US power transmission and distribution losses continued to increase into 2026, though marginally lower in Apr/May  
![](images/332014f4fc4e47bf67319b81682a1ddc4b09aeee3fbf6430849e73a40317a350.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

## Generation by Fuels

Exhibit 25: YoY growth in natural gas-fired generation has moved sequentially lower June-to-date vs March and April but remains positive  
![](images/19c49822b6fa3f16834a01af61ab4ef77a997b55b8c562086022f7e252e54d3d.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 26: Higher gas competitiveness keeps coal power generation lower yoy most of the time from mid-Feb to Jun  
![](images/8142b1fa897b29b78bf166a31c33d4ef34af7e7754880476a36cd683599b9451.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 27: Nuclear power generation turns higher yoy into May and June following April maintenance  
![](images/d5829aa3dcad6ba18543826ef790a06a60c900d434a1e0269309371a7f781628.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 28: Wind generation moves higher yoy in May and June  
![](images/9352110195c734270a012ca5d8ff8ae795a11e58eb0c647fe7c607e9793d4813.jpg)  
Not weather adjusted  
Source: EIA, GS Global Investment Research

Exhibit 29: Solar generation has continued to seasonally ramp up, driven by yoy capacity additions of over 30 GW  
![](images/431f80d368ed93a940a7ac62a37621f36e4eadb160d111d9dafe15d190754549.jpg)  
Source: EIA, GS Global Investment Research

Exhibit 30: Hydro power generation remains weak yoy due to droughts in more than half of the country  
![](images/77b3b2c21f1fc4085e3040fa6bc143fe4a2e0649e3d91e818fe32f9362e80483.jpg)  
Source: EIA, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Hongcen Wei, Laura Cyr, Daan Struyven and Samantha Dart, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Hongcen Wei GS & Co. LLC, Laura Cyr GS & Co. LLC, Daan Struyven GS & Co. LLC, Samantha Dart GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this r

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
