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
# U.S. Software

# Software Budget Trends – Latest Insights from Customer IT Execs and Procurement Officers

# Summary

Over the last month or so we've had \~25 conversations with enterprise IT execs and partners and in this report we focus narrowly on projected IT spending growth, what is being prioritized and deprioritized, how buyers are changing contract terms and how IT execs and procurement officers are reacting to software pricing model changes. Amidst all the investor debate about medium-term AI disruption risk to the software sector, near-term budget trends have taken a back seat but in our view are having a much larger impact on Mar/Apr quarter reported results. Bottom line, this is a challenging IT budget environment overall as growth outlooks become increasingly muted, with pressures most pronounced for SaaS and application software vendors, while demand remains relatively healthier across AI, data, security, and cloud infrastructure providers.

# Notable Budget Trends

We'd note: 1. This is a tough spending backdrop, as \~80% of our checks cited stable or slowing IT spending growth in 2026 given a combo of a) the impact of AI, b) the geopolitical situation, especially for B2C firms with customers exposed to higher fuel costs and inflation and c) slowing customer headcount growth. 2. There is a higher-than-normal degree of uncertainty in the customer base (it is not just investors that are looking through the fog) and some are reacting by signing shorter-term contracts. 3. The degree of pricing push-back against software suppliers is rising, especially for seat-based apps firms. 4. The rapid transition to a seat-plus-usage model seems inevitable but is going to be met with some resistance as some customers react by optimizing or cutting seats, putting firm usage guardrails in place and/or elongating deal negotiations.

# Budget Winners and Losers

While the weakening IT budget outlook poses a risk across all vendors, the more defining trend over the past year has been the pronounced shift in spending mix. Spending items being prioritized include: a) AI, by far the biggest focus, b) AI-enabling data investments, c) cybersecurity (surprisingly durable), and d) cloud infrastructure or hyperscaler spend. Spending items being deprioritized include: a) limit internal headcount growth or even to cut headcount, b) cut external IT staffing or offshore systems integration services spend, and c) the most frequent deprioritized budget item was spending on SaaS or application software, with a desire to contain incremental spend, seat growth and add-on modules. For some time now, the UBS Software team has had a long bias towards AI, data, infrastructure and security stocks and a more cautious view of SaaS or application software stocks, a framework that in our view is now consensus and reflected in stocks. These anecdotes reinforced this bias, keeping us tempered about chasing de-rated apps software stocks and keeping us constructive on Palantir and Snowflake.

# Equities

Americas

Software

Karl Keirstead

Analyst

karl.keirstead@ubs.com

+1-310-734 2455

Taylor McGinnis

Analyst

taylor.mcginnis@ubs.com

+1-212-713 1332

Roger Boyd

Analyst

roger.boyd@ubs.com

+1-212-713 1256

Radi Sultan, CFA

Analyst

radi.sultan@ubs.com

+1-212-882 0094

Madeline Tribendis

Associate Analyst

madeline.tribendis@ubs.com

+1-212-713 8151

# What We've Heard

Let's start with the unvarnished anecdotes from a variety of customer and partner conversations over the last several weeks, organized by subject area. We'll then summarize the common threads in the final section of the report.

# Overall 2026 IT Budget Outlook

The overall tone from these checks with respect to overall IT spending growth was mixed/cautious. Of the 14 conversations below, only 3/14 or \~20% cited still-healthy IT budget growth with 11/14 or \~80% citing stable or even shrinking IT spending growth in 2026. This makes for a challenging demand backdrop for enterprise software firms to be selling into, and in our view it is very likely that this spending pressure already impacted software company results over the last 1-2 quarters. In terms of the drivers of this cautious IT spending outlook, the most popular answers were a) the impact of AI, b) the geopolitical situation, especially for B2C firms with customers exposed to higher fuel costs and inflation and c) slower customer headcount growth or even cuts.

[Non-Text]

\- Customer 1: We are seeing the impact of tariffs and higher fuel prices, this requires us to be judicious around software spend and we're seeing IT budget compression. The geopolitical situation is driving a bit more of a conservative approach in overall investments. Also, AI investments are requiring us to double down on cost reduction strategies in other areas to fund these solutions. This just creates uncertainty in how we will be able to purchase and fund investments going forward. These things just compounded budget cuts, making us look at short-term horizon more.

\- Customer 2: A year ago, there was a lot of thought around how much we would need to invest beyond normal IT budget targets, usually sub-5% growth. But as geo pressures, inflation, oil, tariffs started to affect us, the uncertainty creates a scenario where we are now thinking about the need for cost mitigation. If we were thinking about these big bang projects, we pulled back a bit because of the uncertainty. Where we prior were seeking long-term cost savings, now we're seeking short-term cost-cutting so we can react.

\- Customer 4: The current plan is for our IT spend to increase between 10-15% this year and that's mostly in line with 2025, maybe slightly lower. A lot of it is due to growing business across the board with our large financial and fintech customers, but also with new AI initiatives. The budget growth is due partly to AI, but it's the normal growth of the business and the growth of IT infrastructure that we need to spend money on. It's a little bit less than 2025 because 2025 saw more budget going towards AI initiatives.

\- Customer 6: Honestly, I think the budget is going to shrink this year. They're trying to shrink the budget more than 10%. Our insurance products are not the cheapest options, so in order to compete with the ones out there you have to be able to reduce cost. Either you take a little margin, or you start cutting costs. This was the plan going into this year. I don't think there has been much accounting for the things in Iran.

\- Customer 7: Our IT budget is going to increase hundreds of millions. It's increasing because we always want to challenge ourselves on the technology side. It's up 10% this year. For sure that's going to be driven by AI. In order to be aligned with the regulations and stuff that we're supposed to respect.

\- Customer 9: I would say the IT budget this year is stable with last year. We haven't had budget cuts so far at the end of 1Q.

\- Customer 14: In our luxury retail industry, we typically think long-term and spend in Middle East is minimal compared to overall budget. It does not have an impact on our IT spend. We heavily invest in our intelligence and technical layer, but our IT spend in 2026 and 2027, independent of macro, is going to remain the same.

\- Customer 15: I would say not necessarily having to cut into our IT budget, especially for AI workloads and Agent AI capabilities. We managed to create net new budget for our organization, but we are more impacted by the shortage in memory in RAM and the increase in price of hardware from laptop to desktop to servers.

\- Customer 16: We need to reduce costs due to the situation in the automotive market and our business model situation. And one of the main use cases of IT is to reduce costs, not only from an FTE point of view, but also to gain process efficiency. In 2024, we had an increase in IT spend of 12% compared to 2023, in 2025 the increase was a bit lower, about 10%. The increase for 2026 will be around 15-18%.

\- Customer 17: From an IT budget standpoint, we are about a MSD increase this year, in some cases flat depending on the different cross sections. We had some hiring freezes across the organization through the back half of last year with the exception being AI and data. We're trying to drive productivity gains within G&A, things like marketing and HR. Sales and tech are mostly insulated. We will have more of that in 2026. This is both in high-cost geos and back-office locations.

\- Partner 1: For IT budgets, there are no reductions although no significant increases. There were reductions for the last 3-4 years where CIOs were pushed to cut costs.

\- Partner 2: Closing out the year we did not see the growth we were expecting with our business clients in all sectors, gov is still suffering which is a huge part of economy, retail still suffering with uncertainty around tariffs last year and oil prices this year. Retail segment is hesitant, keeping low inventory on shelves, back-ordering, seeing longer cycle times on ecommerce shipments. Folks are less willing to sit on inventory but have started to see a bit of a shift in 2Q26, where if someone sees a deal, they're stocking up. Really a muted environment between Q4 and moving into Q1 of this year, specifically gov and retail suffering. I think everyone is holding onto cash in a lot of cases, and a lot around uncertainty. Not seeing lines of credit cut like during the pandemic but seeing balances in checking accounts higher than we've ever seen. In Q4 of last year there was an increase in late payments, people are holding onto cash till the last moment and reluctant to spend. Businesses are reluctant to spend, just uncertainty with war and oil prices.

\- Partner 5: We were expecting more growth in 1Q, but there is still this sentiment of cautiousness and worriedness with war and people getting laid off, so as a company they need to be able to justify to spend money. Companies are taking more cautious steps, that is the sentiment I am seeing. Things are getting more expensive, gas prices, etc. so companies taking more cautious steps, sentiment is more conservative. So things are still slow, people are not extensively hiring like they were in 2022-2023. We are not seeing project implementation delays, we are just not seeing many upgrades or enhancements to HR or ERP systems or new modules. People are being more conservative right now.

\- Partner 6: In terms of IT budgets, there's been no real change with respect to the exit 2025 position, meaning that enterprise software continues to be under the same sort of squeeze position. In the context of enterprise software specifically at large, the overall posture is that, yes, we want to spend, but we want to take a very, very cautious approach. This is why I say that the exit 2025 position hasn't changed because the macro variability has generally remained the same. In fact, if anything, it has only become more complicated. Secondly, AI and what AI can potentially do continues to create more ripples all over. So these 2 factors at large have caused customers to basically sit tight and only spend where absolutely required in the form of either an additional module or some feature. But barring ServiceNow none of the enterprise software players in my radar have registered what I would call as growth. I mean it has been either just about there as in steady or it has been on the decline a little bit.

# What is Being Prioritized

The bigger IT budget story over the last year, certainly evident in these checks over the last month or so, has been the change in the mix of IT budgets, what is getting prioritized and deprioritized. For some time, the UBS Software team has favored infrastructure, data, and security stocks, while remaining more cautious on SaaS and application software (with the exception of pockets tied to ongoing on-premise to cloud migration—especially ERP modernization—and consolidation toward scaled platform vendors over point solutions). This framework has been and continues to be very rooted in the budget mix commentary we’ve been hearing from enterprise customers and partners. The most recent conversations below reinforce this theme, though it’s worth noting that the increasingly cautious IT budget outlook across our checks presents a growing risk across the broader software landscape.

It is very clear reading these anecdotes that 2026 is the year that traditional enterprises are leaning into AI investments. Of the 16 conversations below, 13/16 or 80%+ overtly flagged a material uptick in focus on AI, consistent with our recently-published Enterprise AI Survey (see link to report here). As we've said, it's now "game on" in terms of the ripple effect of AI on enterprise IT budgets. This will not come as a surprise to most tech investors. In terms of the other priority budget items, three stood out, a) data investments, in order to enable a high-ROI on AI investments, b) cybersecurity was flagged almost as often as data and c) cloud infrastructure or hyperscaler spend. These spending priorities—data, security and cloud infra—remain consistent with what we've been hearing for some time and shape our bias towards infrastructure, data and security software stocks.

\- Customer 1: The biggest gating factor to enabling AI tends to be data quality or lack thereof. As an example, we want to be able to on the procurement side really drive a CLM, contract lifecycle management, solution to automate a lot of our processes. But we have challenges with standardization of MSE terms, where is all the data housed? Because we have poor data mgmt, we're finding the AI use cases have not been able to prove the ROI case, so we need to invest more there. Also, I definitely think cybersecurity is a priority for our company. We're also moving away from on-prem and more toward SaaS. We try to double down on enterprise vendors like Microsoft, SAP, Oracle, and Salesforce, but do have a long-tail of software providers and one of our strategies is to compress that tail over time. We are an SAP ERP shop and moving to SI4HANA. There's a lot of ancillary applications like Finance and HR, so can we consolidate to a single provider? In some cases, we do and some we need to look at our point solutions.

\- Customer 2: Especially with tariff pressure, now oil and inflation, the immediate focus has become risk mitigation, particularly on our supply chain, to have unified data on that so we can see it and using AI for that. We didn't have a clear unified view of supply chain in terms of risk and sourcing data, so that became #1 priority. There is also an absolutely increased urgency in the last year or so to invest in cybersecurity. We'll be spending more in that space. It's not just on providers, there is a need to potentially increase headcount in the security area too. SaaS and data are other priorities. There is also a push to consolidate more spend on one cloud provider. Usage on our cloud provider is going up significantly because of AI.

\- Customer 3: We're definitely reallocating spend to AI vendors. There are also small pockets of opportunity in data catalogue and data management spend, maybe business intelligence although that is getting tricky with AI. Areas where we are not pulling back on because they are required, include data privacy and preventing data breaches, a lot of that is more important with AI. So we're investing more in cloud management, security management. There is no pressure to reduce data management and security because they are critical. Observability is also definitely a big one we are investing in. Also, there is a lot of hope and optimism around AI coding agents, we're testing Cursor, OpenAI Codex and Anthropic Claude, and we have been hesitant to lock into one just yet.

\- Customer 4: In the budget we're always prioritizing and focusing on security. I don't know if it's an increased focus because you always focus on security, but that's the only one I can think about aside from AI.

\- Customer 5: The AI dollars are definitely getting prioritized for sure. That's corresponding with the rapid innovation and iteration in the space. That's a good thing. It's a major investment, we have to look at all of our workflows and really invest there. Obviously it's not a net zero change, so it's dependent on two factors: 1) how forward thinking your enterprise is for adopting these technologies. 2) what portion of your existing spend needs to be re-allocated. A lot of the integrations that exist today in products like AVS Bedrock you don't actually have to shift the spend to the model vendors, you can piggyback on existing engagements to get some of the benefits.

\- Customer 8: The total spend on cloud compute is growing, probably 8-9% annually. We’ve largely completed our migrations. Everything we wanted to migrate has been migrated. We have sensitive data on-prem for things like algorithms. We’re about 90% on the cloud and that 10% remaining is sensitive patient data.

\- Customer 9: The end-of-2025 budget is what we received for 2026 but with much more focus on AI. We are facing a hockey stick ramp on AI. Until last year, we were cautiously optimistic on AI. Since November, the whole trajectory has changed. This year, it remains much in focus. We recently bought a massive supplement of Copilot licenses for the whole organization, a very high amount irrespective of the geopolitical and macro situation. We have chatbots and self-service programs, using Copilot for product requirements or AI for Jira tickets.

\- Customer 12: Top few areas where we're shifting top priorities or increasing spend is network infrastructure. We've been investing so much in fiber, 5G, and resiliency in our network, so that will be top priority still and it's critical infrastructure that becomes strategic down the road. Also, we're focusing more on AI and automation, like helping to reduce labor costs down the road and increase efficiency in labor force. Deploying new AI tools to employees and testing the waters, with hiring freezes in locations due to deploying automation tools. Running our own AB tests, and if it's generating more productivity, then we'll run it out in more places across the organization. AI tools we are shifting to are OpenAI, etc. Last piece is cyber security with the things going around in geopolitics and cyber risk. We're increasing cyber security because we are a regulated company and our customers are the government, hospitals, etc. We've been hiring like crazy there and our infrastructure controls the nation.

\- Customer 13: Security compliance is something that has grown year-over-year anywhe

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/ee4476fff04cf81cb20f18692e0dbc29d16bb48423af91d27f51e2eb8de8f3c1.jpg)
"""
