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
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Copper

Where we're going, we don't need balances

\- With tight mine supply and structurally supported demand, the medium-term environment for copper prices remains supportive. However, at \~\$13,600/mt, up by more than 40% yoy in a surplus global refined market backdrop, it is hard to argue that copper prices look cheap.

\- The key 2H26 catalyst is policy, not balances: the structure/communication following the US review of Section 232 copper tariffs.

\- The market is effectively in a US–China tug of war for copper. The US has been pulling metal via an attractive COMEX/LME arb since early 2025, tightening the ex-US market and reducing China’s historical role as the marginal price setter.

\- Amid this competition, China's buying floor has shifted materially higher. Despite episodic buyer strikes/exports causing volatility, concentrate constraints and the US import pull on copper has forced China to tolerate significantly higher prices to meet overall import needs.

\- We believe the Trump administration will pursue a phased, escalating tariff on refined copper cathode imports following the upcoming review to 1) ensure all the copper that has already been imported into the US stays onshore and 2) keep this excess US inventory as a critical reserve, rather than enact policy which incentivizes it to quickly destock in the coming years.

\- Escalation is everything: For LME copper prices, the most important flip point between a bullish and bearish outcome is how any communication shapes expectations around the future rate of tariffs on refined copper cathode.

\- Escalation equals an incentive to still import copper into the US before tariffs come into force or increase, which is bullish as this US pull on metal continues and China is forced to react. No expectations of escalation, even if an outright tariff is immediately announced, is bearish for LME prices as it will result in a closed US import arb window and a long de-stocking period in the US, giving China its pricing power back.

\- As we see this tug of war continuing, we expect copper prices will likely persistently see higher floors and higher ceilings on a push towards \$15,000/mt over the coming quarters, with risks still skewed towards reaching a very bullish pinch point driven by rapidly dwindling ex-US inventories.

## Global Commodities Research

Gregory C. Shearer
(44-20) 7134-8161
gregory.c.shearer@JPM.com
JPM Securities plc

Ali A. Ibrahim

(44-20) 3493-6438

ali.ibrahim@JPM.com

JPM Securities plc

Ananyashree Gupta
(91-22) 6157 3627
ananyashree.gupta@jpmchase.com
JPM India Private Limited

## Where we're going, we don't need balances

A supportive backdrop, but copper also isn't exactly cheap. The medium-term environment for copper prices remains supportive. Continued tight copper mine supply

— ongoing weak production from Codelco, slower ramp up schedules at disrupted Kamoa Kakula and Grasberg—and structurally supported demand trends around electrification, which tie into insatiable investor appetite to participate in the data center capex megatrend, have not changed. Add in a global industrial upturn that our economists believe has further room to run as destructive energy price and inflation tail risks recede and stronger expected growth momentum in China in 2H26, aided in part by further fiscal support, and the investment narrative in copper looks solid, even with the threat of Fed hikes later this year. Yet, at \~\$13,600/mt, up by more than 40% yoy in a surplus global refined market backdrop, it is hard to argue that copper prices look cheap or aren't already pricing a lot of this good news in.

The structure of the US copper tariffs is the next major catalyst to unlock a push towards \$15,000/mt. So why then, after closely tracking our 2Q26 forecasts, do we remain bullish and now see copper prices continuing to push higher towards \$15,000/mt over the coming quarters (Figure 1)? In short, our expectations around US tariffs on copper cathode imports. In our view, the biggest single catalyst for copper fundamentals and pricing over 2H26 will be the results and actions following the US review of Section 232 copper tariffs. Since April, we have been flagging our view that the Trump administration will pursue a phased, escalating tariff on refined copper cathode imports following the upcoming review. The US’s almost relentless pull on copper from the rest of the world since early 2025 has been a material component to copper’s rise in the last year and we don’t think it's over as we expect the US to structure tariffs and their communication in a way that keeps the COMEX/LME arb open and attractive for continued imports. As we detail further below, despite global oversupply, this has left the rest of world copper market much tighter and has wrenched ultimate price-setting power away from China, the dominant consumer. While Chinese buyer strikes and opportunistic exports at higher prices haven't fully gone away and will still drive volatility, this arb tug of war between the US and China, which we think will continue, is a market where copper prices will likely persistently see higher floors and higher ceilings, and still risks reaching a very bullish pinch point in the coming quarters driven by rapidly dwindling ex-US inventories.

Figure 1: JPM copper price forecasts  
LME cash in US\$ per metric tonne, quarterly and annual averages

<table><tr><td colspan="2"></td><td>4Q2025A</td><td>2025A</td><td>1Q2026A</td><td>2Q2026</td><td>3Q2026</td><td>4Q2026</td><td>2026</td><td>1Q2027</td><td>2Q2027</td><td>3Q2027</td><td>4Q2027</td><td>2027</td></tr><tr><td rowspan="3">Copper</td><td>New</td><td>11,105</td><td>9,947</td><td>12,824</td><td>13,415</td><td>14,500</td><td>14,800</td><td>13,885</td><td>14,000</td><td>13,800</td><td>13,800</td><td>13,600</td><td>13,800</td></tr><tr><td>Old (Feb 2026)</td><td>11,105</td><td>9,947</td><td>12,875</td><td>13,500</td><td>13,000</td><td>12,500</td><td>12,969</td><td>11,800</td><td>11,600</td><td>11,600</td><td>11,500</td><td>11,625</td></tr><tr><td>Change</td><td>0%</td><td>0%</td><td>0%</td><td>-1%</td><td>12%</td><td>18%</td><td>7%</td><td>19%</td><td>19%</td><td>19%</td><td>18%</td><td>19%</td></tr></table>

Source: JPM Commodities Research

## Global S&D balances don't really matter in copper tug of war

Many of our regular balance updates drill deep into our outlook and assumptions for copper supply and demand. This one won't. Given the uncertainty around future tariffs, the persistently open US import arb window for copper cathode and the accompanying material pull of metal into the US means that the global picture of the copper supply and demand balance has significantly lost its pricing power, for now. To this end, our latest balance now shows a refined market surplus of over 500 kmt in 2025, yet LME copper prices were up by 42% on the year. Looking to this year, despite mine supply remaining very tight (this is still very important), our global refined balance has swung to a surplus of around 360 kmt. A slight decrease in our demand growth estimates (+2.2% yoy in '26) loosens things somewhat, but most of this swing comes from another sharp boost to our assumptions of scrap volumes flowing into the supply chain at smelters and refiners, mainly in China, which leaves global refined production growing by +1.6% yoy in 2026 despite flat mine supply growth (Figure 2 & Figure 3). While a tightening in tax invoice regulations disrupted Chinese scrap supply in the last quarter, we largely see this as a bottleneck which will eventually ease, rather than a structural sea change which will diminish available scrap over the long-term.

Figure 2: Global copper mine supply and refined production growth
Percent change, yoy  
![](images/b7399a0427ebcf15d34849c9ee15a1d28f351dfd1fb3d6a99edbf11fab110475.jpg)  
Source: Company Reports, Government and Industry data, CRU, Wood Mackenzie, BGRIMM, JPM Commodities Research

Figure 3: Global copper scrap usage growth  
![](images/e1b1d7a7f471ca045fe254bec4b0851712d2688cbdf0848ab818c69a4377291e.jpg)  
Source: CRU, BGRIMM, JPM Commodities Research

In summary, despite continued tight concentrate markets, Chinese refined production continues to refuse to yield, utilizing any and all available copper units to maintain output and ultimately leaving the global refined copper market well supplied. For a real life sense check, the US importing another nearly 400 kmt YTD above its implied needs (after 870 kmt of excess imports last year), demonstrably shows we are not in a deficit global refined copper market in our view. The thing is, for as long as the U.S. continues to vacuum up excess copper from the rest of the world, this global oversupply is somewhat irrelevant, as the ex-US refined copper market will remain tight, leaving LME copper prices caught in the middle of a tug of war between the US and China for copper.

## As the US vacuums up copper, China has had to react too

The US has built a $\sim 1.2$ mmt stockpile in 18 months. Since the door was opened for potential refined copper tariffs in early 2025 (and was left open last summer), US monthly refined unwrought copper imports have averaged around $140\mathrm{kmt}$ (Jan 2025-May 2026), nearly double the $75\mathrm{kmt}$ a month average in 2024 (Figure 4 & Figure 5). Adding in estimates for US refined copper supply and demand, excess US imports of copper likely amounted to close to 870 kmt last year. And it has continued so far this year, with estimates through May pointing to nearly an additional 400 kmt excess build YTD. To put this in more general context, actual US refined copper demand is about 6% of global, but in the last year and a half it has been pulling on the market like it's an importer consuming closer to 9% of global demand, a very big shift.

Figure 4: Monthly US refined copper imports
Thousand mt, dashed line is 2021-2024 average  
![](images/3615aab6f901aea720eae2dacce98966275b933e438bd344e2d1f9329447e93e.jpg)  
Note: 01 May - 16 Jun 2026 estimated based on bill of lading data.
Source: US Census Bureau, IHS Markit, Bloomberg Finance L.P., JPM Commodities Research

Figure 5: Jul'26 COMEX/LME copper spread
LHS: US\$/mt, RHS: Percent of LME price  
![](images/0726daff6c3548b510aa9dcf513893cf6159af71497120469a604fde1eaed598.jpg)  
Source: Bloomberg Finance L.P.

This US pull on metal has driven China to alter its behavior too. To be clear, the US is importing more copper because price differentials, embedding the potential for tariffs, are incentivizing it, not because it is consuming all this extra metal. But this diversion of copper and dislocation in global inventory has nonetheless driven serious ripple effects (Figure 6). On the other end of the rope in this game of tug of war is China. Given the tightness in global concentrate supply, which limits China's ability (even with greater scrap use) to fully ramp up all its planned smelter/refined supply, China still needs to import serious amounts of copper cathode to feed its own domestic demand, and these imports need to be attracted by an open SHFE/LME import arb. Our balances, which assume around 13.3 mmt of Chinese refined supply (+3.3% yoy) this year and 15.9 mmt of Chinese refined demand (+2.5%), show a net import cathode requirement of around 2.6 mmt in 2026 (this is where balances still do matter quite a lot).

Figure 6: Global visible copper inventories by location
Thousand mt  
![](images/c2a62001740b754f2db22928900ecbe4ca0852000c1da6c44db233ac907b5519.jpg)  
Includes LME (+ off warrant), COMEX, SHFE, Chinese bonded stocks
Source: CRU, LME, SHFE, COMEX. Includes Chinese bonded stocks in Shanghai, Guangdong and Qingdao. As of 19 $^{th}$ June 2026, LME off-warrant as of 16 $^{th}$ June 2026.

Figure 7: Chinese spot copper import arbitrage and onshore spot premium/discount  
![](images/53319e58421a97c768062ae27880ae83e9a339b80be7c486a58d8a4a0c6f8f10.jpg)  
Source: SMM, Bloomberg Finance L.P., JPM Commodities Research. \*Arb as of 8:00 AM London.

Before this huge pull into the US emerged, China was the behemoth in the seaborne copper market, making it the ultimate marginal price setter. If prices got too high, Chinese buying would slow (e.g. buyer's strike), closing or even reversing the SHFE/LME import arb (Figure 7). China would then wait for the fever to break and re-engage again after prices had pulled back materially. We can see classic examples of this back when prices pushed up towards \$11,000/mt in early 2022 and mid-2024 (Figure 8). However, the combined pressure from concentrate constraints and boosted US imports have diminished China's price-setting ability, leading to a sharp push higher in Chinese buying floors as China looks to secure its required imports. To be clear, China's influence is far from dead, but they have had to be willing to accept materially higher prices recently.

Figure 8: China's buying floor has moved sharply higher in the last year LME 3M Copper prices (US\$/mt) vs an open Chinese spot copper import arb window  
![](images/a3300573af5ec18343bbe9c188a98220bd3efe32b6a9097e7c036e675c9c65ef.jpg)  
Source: LME, Bloomberg Finance L.P., JPM Commodities Research. \*Arb as of 8:00 AM London.

Case in point, Chinese purchasing went ice cold (buyer's strike, boosted copper cathode exports to the LME) over late 2025 and early 2026 as copper prices first ran up to \$14,000/mt. Come March, a war-driven wobble in risk sentiment drove a correction lower in copper prices. Yet as soon as we approached a still lofty \$12,500/mt China's import arb window jerked open and inventory draws sharply accelerated. This marked more than a \$2,000-3,000/mt jump higher in China's buying floor (Figure 8). And it's continued to creep even higher recently, with the arb window fluttering open on dips to \$13,500/mt.

## US tariffs: Escalation is everything for LME prices

By June 30, 2026 the US Commerce Secretary is to provide President Trump with an update on domestic copper markets so that the President can assess whether additional Section 232 tariff modifications are necessary. More specifically, in the June 30, 2025 report, the Commerce Secretary already recommended “imposing a phased universal import duty on refined copper of 15 percent starting on January 1, 2027, and 30 percent starting on January 1, 2028.” This was not implemented last year but is up for review now.

While high conviction in tariff-related decision-making is admittedly hard to come by, our base case remains that the Trump administration will in fact move forward with enacting a phased tariff approach. Why? Now that the US has likely built more than 1 mmt stockpile of refined copper in the last 18 months and the groundwork for Project Vault has been laid out, we think the administration will tailor a strategic tariff policy on refined copper to accomplish two goals: 1) ensure all the copper that has already been imported into the US stays onshore and 2) keep this excess US inventory as a critical reserve, rather than enact policy which incentivizes it to quickly destock in the coming years. Hence, in our view, the simplest way to ensure both is to follow through by enacting an escalating tariff. Once enacted, the tariff rate sets a very high bar for ex-US prices to incentivize any onshore copper to leave while the escalatory nature of tariffs keeps attracting imports to the US, disincentivizing a destock of inventory already in the US and allowing the government to generate tariff income on these imports. With 50% tariffs already in place on downstream semi-finished copper products, the administration also has some runway for this escalation on copper cathode imports to progress.

Escalation is everything. There are countless iterations of what might be announced, if anything... there is no requirement or specified timeline for a response from President Trump. For LME copper prices, the most important flip point between a bullish and bearish outcome is how any communication shapes (whether formally or informally) expectations around the future rate of tariffs on refined copper cathode. Escalation equals an incentive to still import copper into the US before tariffs come into force or increase, which is bullish as this US pull on metal continues and China is forced to react. No expectations of escalation, even if an outright tariff is immediately announced (e.g. an immediate jump to 50% tariffs on cathode), is bearish for LME prices as it will result in a closed US import arb window and a long de-stocking period in the US. Current implied US inventory of \~1.2 mmt would cover almost 20 months of average 2024 imports. With the US out of the import market, the tug of war pressure is off China and they regain pricing power and are unlikely to re-engage fully until prices are much lower, say \$10,000-\$11,000/mt or below.

Very bullish pinch point risks could return into focus under a forward-starting, escalatory tariff. With our expectation being that the US wants to protect this copper stockpile (not have it disappear via destocking over the next two years), we think any communication will at least re-enforce the threat of future tariffs, even if they are not formally enacted yet. But even within this “escalatory” branch of potential outcomes, there can be differences.

\- A forward-starting, escalatory tariff regime is the most bullish outcome for LME prices as there could be another immense rush to get copper to the US in the coming months ahead of the start date. Even with \~50% of LME copper stocks being of Chinese origin, which won’t go directly to the US, this metal could still quickly be drawn as swap agreements are struck to free up as much US-deliverable metal as possible to divert to the US ahead of the tariff. Under this scenario, as LME inventory likely draws dramatically, we think the risk is skewed towards an overshoot of our already bullish forecasts in 2H26 ahead of the tariff start as LME curve structure likely punches into a sharp backwardation (Figure 9 & Figure 10) (See Metals Weekly: Copper—It’s only the end of the beginning, 04 Dec 2025). Volatility will remain though as opportunistic Chinese exports likely ramp up again to deliver into this backwardation. However, this isn't a long-term solution, just a give and take cycle, as China still remains structurally net short copper cathode.

Moreover, there remains the risk that Chinese policy makers impose more stringent restrictions on copper exports if they start to become more concerned about supply security.

\- Other “escalatory” regimes likely still keep the tug of wa

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 21 Jun 2026 09:01 PM BST

Disseminated 21 Jun 2026 09:01 PM BST
"""
