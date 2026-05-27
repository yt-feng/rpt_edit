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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
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
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Property

Global China Summit Takeaways: Mixed views on recent green shoots

At the JPM Global China Summit held in Shanghai last week, we met with various experts & property companies. During the same week, on top of Shanghai, we also conducted channel checks in Hangzhou & Jiaxing. On the recent green shoots (improving secondary prices and transaction volumes), experts and stakeholders hold mixed views. Generally, state-owned developers, KE Holdings, and the Iceberg Index are relatively constructive, while private developers, Centraline, and the Beijing-based policy expert are more cautious. Sentiment is the strongest in Shanghai—supported by leaner secondary-market inventory and potential wealth effects from IPOs & the stock market—followed by Shenzhen; Beijing and Guangzhou remain constrained by higher inventory. Our field checks in Shanghai suggest better sentiment and higher conversion than last year, with some projects testing modest price increases, but the bears argue that the gains may largely reflect pent-up demand and local easing and could fade. Consensus does not expect an across-the-board recovery; instead, a K-shaped stabilization is possible, with top-tier cities and upgrade/luxury products outperforming. This is broadly in line with our base-case forecast (i.e., tier-1 cities to see a soft form of stabilization, but other cities may still see a decline, albeit likely narrower than 2025). Nationwide easing appears unlikely in the near term; policy is expected to remain city-specific, with scope mainly in better execution (e.g., inventory purchases). Alpha opportunities remain with COLI: despite already delivering 14% YoY growth in contracted sales year-to-date, growth could stay positive over the next 1–2 months, by our estimate, supported by launches in Shanghai and Shenzhen (sellable value of new launches will grow >10% Y/Y). We continue to like SOE developers with a strong focus on upgrade demand in tier-1 cities: COLI, CR Land & Jinmao.

\- Mixed views on recent green shoots in tier-1 cities: Despite stabilization in secondary home prices and a surge in secondary transaction volumes in tier-1 cities, stakeholders differ in their interpretations. State-owned developers, KE Holdings, and the Iceberg Index appear to be relatively more constructive, while private developers, Centraline, and a Beijing-based policy expert remain more cautious. That said, even the more constructive voices do not expect a sharp rebound like Hong Kong's recent recovery (where home prices have surged $16\%$ from the bottom). Among the four tier-1 cities, sentiment is most positive in Shanghai, followed by Shenzhen. Views on Beijing and Guangzhou are less bullish due to higher inventory levels. In Shanghai, some experts noted that secondary-market inventory has already fallen to an optimal level—explaining the modest price improvements in recent months—while others attribute the improvement to a wealth effect from IPO activity and a firmer equity market. During our property tour in Shanghai, sales managers reported improved sentiment versus last year (in both core and non-core districts), reflected in higher conversion rates, and some projects are even attempting marginal price increases. Bears argue the near-term improvement may be driven mainly by the release of pent-up demand and local easing measures (e.g., higher loan limits under housing provident fund mortgages), and

# Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC

(852) 2800-8513

karl.chan@JPM.com

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

Jocelyn Gao

(852) 2800-8529

jocelyn.gao@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

therefore may not be sustainable.

- A nationwide recovery is still unlikely in the near term, but low-tier cities are also not entirely dead: The prevailing view is that even if tier-1 (and select tier-2) cities stabilize, the broader market will likely, at best, experience a K-shaped recovery, with top-tier cities—especially upgrade/luxury products—performing better. The outlook for lower-tier cities remains weak. However, our tour in Jiaxing (a tier-3 city between Shanghai and Hangzhou) suggests selective opportunities: while the overall market is still soft, some developers such as Greentown have been reinvesting, achieving normal margins and solid sell-through. The key support is limited supply of newly built upgrade products in core districts, alongside a substantial decline in land supply. From developers' perspectives, this creates pockets of opportunity in certain tier-3 cities.   
- Low likelihood of nationwide policy easing in the near term: Over the past 12 months, authorities have stopped using the phrase “stop falling and stabilize” (止跌回稳). In the recent Politburo, they reiterated efforts to stabilize the housing market but omitted “stop falling,” a phrase that previously boosted investor sentiment (notably in September 2024). A Beijing-based policy expert believes this reflects a view that the market is no longer in crisis mode, suggesting policy will remain city-specific. With recent green shoots, the probability of a nationwide easing is even lower. Many experts believe most major policy tools have already been used, though execution could improve (e.g., inventory purchases). On proposals to phase out the pre-sales system, the Beijing-based expert views this as the central government’s ultimate direction, but developers generally think implementation will be difficult in the near term without a clearer market recovery.   
- Alpha opportunities remain—COLI. The current housing market favors developers with strong exposure to tier-1 cities (especially Shanghai and Shenzhen) and a focus on upgrade products. COLI has delivered 14% YoY growth in contracted sales in 4M26 and noted : (1) YoY growth in inquiries/visits remained mildly positive in May; and (2) sellable resources over the next 1–2 months are expected to grow at a double-digit YoY rate, supported by launches in Shanghai and Shenzhen. If the projects launch as planned, we estimate that COLI may sustain positive YoY contracted sales growth over the next 2–3 months (despite a not-low base in June). Asked why land-banking has been slow year-to-date, COLI cited a shortage of high-quality land supply from local governments, and reiterated that it will continue to seek opportunities in top-tier cities (including Hong Kong).

# What are the experts saying?

# Plenary Session with Ms. QIN Hong (Beijing-based policy expert) & Mr. YANG Xin (CFO of CIFI Holdings)

- “The worst is over”, but a broad-based recovery is also unlikely: Both experts agree that the worst time of the housing market has already passed. However, a nationwide recovery remains unlikely in the near term, citing high inventory.   
- Tier-1 cities also diverge: Experts believe local-level policy easing plays a major role in recent stabilization of secondary sales volume & home prices in tier-1 cities. However, they believe tier-1 cities may also diverge in performance. Overall, experts are most upbeat about Shanghai, followed by Shenzhen. They remain relatively cautious on Beijing & Guangzhou.   
- Tier-3/4 cities likely will remain weak: Experts expect a K-shaped stabilization where top-tier cities may remain relatively solid, while low-tier cities may remain weak due to population outflows and higher inventories (inventory month in tier-1/2/3 cities is respectively 14/24/34 months).   
- Secondary market will continue to gain maket share: In half of the cities in China, secondary home sales volume already exceeds that of primary homes due to more attractive pricing (developers may not cut prices meaningfully). In the top 20 cities, the secondary market even accounts for 70% of transactions nowadays. This will be the new normal, and the trend is in line with other mature housing mrakets.   
- Nationwide policy easing is unlikely: From the government's perspective, experts believe the KPI for the housing market is price stabilization, although this may not be achieved until sales volume picks up to digest inventories. The recent data stabilization suggests a low likelihood for the central government to roll out stronger stimulus. In particular, policymakers understand that urbanization (and thus new home demand) is slowing down & thus they have no intention to strongly stimulate the housing market. Also, in some sense, most policy tools may have been utilized already, and thus the key thing to watch out for is execution. For example, despite the call for inventory purchases (收储), the scale has been very limited. Although the government no longer calls for the housing market to “stop falling” (止跌回稳) (which is what the politburo emphasized in September 2024), the experts believe this is because the government believes the worst is over, and thus the latest narrative on the sector is simply “continue to endeavor to stabilize the market”. Policy will likely remain city-specific.   
- Scrapping the pre-sale system (预售制度) is the ultimate goal, but it will be a long journey: The experts believe the government has made it very clear that the pre-sale system needs to be phased out, and ultimately, sales may only be allowed after building completion (现房销售). However, the journey will be long as developers may run into funding issues if the pre-sale system is eliminated abruptly.   
- Unfinished buildings (烂尾楼) are no longer a key issue: 7.5 million units of pre-sold-but-uncompleted homes have been delivered. Experts believe the task of “ensuring home delivery” (保交付) is mostly completed.   
- Distressed developers are looking for new ways to survive: CIFI, a non-SOE developer which has gone through debt restructuring, said the company endeavors to switch to adopt a new business model which no longer relies on property development. Rather, CIFI remains proactive in (1) building its recurring income

through rental apartments & property management; (2) engaging more in project management (asset-light model). CIFI believes there are still alternative ways for some distressed developers to stay in the business.

# Centaline (Research Director Mr. LIU Yuan)

- The housing market has entered the phase of “structural but divergent stabilization”: The expert believes that tier-1 cities will be resilient but nationwide data may remain weak; secondary homes will be stable, but new homes may still be soft.   
- “Do not be overly optimistic”: The expert noted that, while the recent data improvement in tier-1 cities is real, the expert does not anticipate an across-the-board recovery, in particular: (1) secondary asking prices in tier-1 cities, based on their monitoring, remain soft; (2) the improvement has a barbell structure, led by the smallest units and luxury units; (3) weak income expectations (especially from the middle class) remain a hurdle; (4) high inventory (currently 31 months, vs. the optimal level of 12-18 months).   
- Lots of potential from home provident fund (公积金) mortgages: Current Tier-1 provident fund loan rates (\~2.5%) are close to, or even below, rental yields on some homes (2.5–3%). But the benefit is not fully realized due to age restrictions, strict approvals, and low coverage (a small share of total mortgages). Expanding eligibility (e.g., easing rules for older homes), raising loan caps, and enabling smoother commercial-to-provident refinancing could meaningfully reduce effective purchase costs and accelerate achievement of the key price-bottom signal of positive carry (i.e., rental yield > mortgage rate).   
- 2026 outlook: Centraline expects primary sales volume to drop 7% Y/Y (in line with JPM estimate), of which tier-1/2 cities to drop 3% Y/Y. For secondary sales volume, Centraline expects it will be flattish Y/Y (more conservative than the 5-10% estimate by JPM). For construction, Centraline forecasts new starts/completions to drop 20%/11% Y/Y (JPM estimate: -18%/-19% Y/Y).   
- 3 prerequisites for true stabilization: Centraline quoted 3 scenarios: (1) rental yield (currently <2%) to be higher than mortgage rates (currently 3.05%); (2) price-to-income ratio returns to a reasonable range; (3) inventory months fall to 12-18 months (now 31). [In JPM view, while we agree all 3 are supportive factors, we believe the most important one is inventory, and we'd put slightly less emphasis on rental yield and affordability, as globally there have been many examples of positive home price growth even if rental yield is lower than mortgage rates and affordability is weak.]

# Iceberg Index (General Manager)

- From a “sharp decline” to “mild decline”: The expert believes the Chinese housing market is transitioning into a “mild decline” stage in 2026, with key cities’ average M/M decline narrowing from >1% per month last year to \~0.3% in recent months. The home price index may still see a 9% downside, if we benchmark to the bottom in 2015. The expert believes the sector is building a structural bottom driven by rebalancing of supply & demand.   
- Secondary sales volume in non-core cities is even rebounding stronger: Post CNY, the secondary sales volume in non-core cities (e.g. Xuzhou, Dongguan) has rebounded $>30\%$ Y/Y, even stronger than the 15% Y/Y growth in core cities. The expert believes this is more of a “nationwide repair” rather than just a K-shaped

recovery. This is supported by: (1) wealth effect from an improving stock market; (2) easing in home provident fund (HPF) mortgages, which also helps as HPF mortgages (which have a lower mortgage rate of mid-2%) can cover 80% of listings in low-tier cities.

- No more “panic selling”: Typically, secondary listings surge after CNY (seasonality). Last year, the listings jumped substantially after CNY. However, this year, the increase has been very mild. This shows that secondary owners are switching from “panic selling” to “rational balancing”.   
- Shanghai's improvement is not exactly driven by policy easing: While other experts may argue that the recent data improvement in Shanghai is driven by the easing of home purchase restrictions and home provident fund mortgages in mid-February, the expert holds a different view, quoting (1) similar easing did not trigger volume/prices to improve in August 2025; (2) a typical transaction period (from building inspection to sales completion) is 4-5 months, and thus the impact of policy easing, if any, would only be reflected later, but the data has already improved.   
- Shanghai's secondary inventory month is even lower than HK: The expert pointed out that the number of secondary listings in Shanghai has dropped from 120K units last year to now 85K units (down \~30%). The implied inventory month in Shanghai is only 6, which is even lower than Hong Kong (>7 months). Units with a lower value (<Rmb3 million) have led the price increases. However, in the recent 1-2 months, the expert also noticed that units valued at Rmb3-5 million have also started to see price stabilization. Going forward, the expert believes that stabilization in secondary listings (rather than transactions alone) would be a more critical bottom signal.   
- Shanghai has confirmed a bottom, but a big recovery is still unlikely: The expert believes Shanghai has already reached the bottom, and now the market's tone has switched from “neutral with cautious bias” to “neutral”. However, the low willingness to leverage up (as seen by the weak loan demand) still constrains the upside. Therefore, in the near term, the expert would categorize the recovery as “range-bound at the bottom” (横盘修复型底部).

# What are property companies saying?

Several SOE developers, private developers and property agencies participated in our China Summit. Below are the key takeaways:

- Sentiment in top-tier cities (especially Shanghai) has turned more positive: SOE developers commented that the market sentiment in select top-tier cities has indeed turned better this year. One SOE also quoted that, despite the volume of showroom visits having only been flat Y/Y, the sales volume has improved Y/Y, suggesting a higher conversion rate. This is encouraging and different from previous policy-induced improvements (like 4Q24-1Q25), because back then, despite a surge in the volume of showroom visits, the conversion rate did not actually improve. Therefore, the recent improvement is more organic & shows stronger buyers' confidence.   
- Not aggressively raising prices: Despite the recent green shoots, SOE developers said they are not aggressively raising prices (only selectively in some projects in top-tier cites) as they (1) still prefer velocity; (2) are not 100% confident in the sustainability of the recent green shoots. At the same time, they are also not expanding discounts. The pricing strategy will remain market-dependent.

- Slower land-banking YTD is due to land quality: SOE developers have generally slowed down in land-banking YTD, and they attribute the reason to be the lower quality of lands being rolled out. Leading SOE developers' land capex budgets for FY26 are actually flattish or even higher vs. FY25. Leading SOEs noted that LGFVs' participation has significantly come down, and thus high-quality land in top-tier cities will likely only be acquired by the top 5-8 SOE developers.   
- Recently acquired projects fetch $>15\%$ margin: Leading SOE developers said the margin of lands recently acquired is generally $>15\%$ . If home prices stabilize going forward, impairment risk should come down.   
- KE Holdings expects secondary GTV Y/Y growth to remain positive in 2Q: KE Holdings expects the primary market GTV to be flat Y/Y in 2Q, but the secondary market GTV may still see positive single-digit Y/Y growth in 2Q. Overall, KE expects a mild stabilization trend in the housing market, while KE will continue to gain market share.

# Channel checks in Shanghai, Hangzhou & Jiaxing

# Shanghai - sentiment has improved:

• We visited projects in both core districts & non-core districts.   
- All sales managers said the sentiment has improved in terms of showroom visits & enquiries, and the sell-through rates so far have exceeded their internal expectations.   
- Demand for upgrade products remains robust, and some projects have been marginally raising prices (by 1-2%) vs. last batches.   
- Although primary pricing is typically at a 10-30% premium vs. nearby secondary homes, sales managers remain confident that they can achieve a good sell-through rate as the efficiency rate of new homes has greatly improved ( $>90\%$ ) under the direction of “the 4 $^{th}$ generation of housing” (四代宅), with higher ceilings (e.g. 3 meters vs. 2.8-2.

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 25 May 2026 08:50 PM HKT

Disseminated 25 May 2026 08:50 PM HKT
"""
