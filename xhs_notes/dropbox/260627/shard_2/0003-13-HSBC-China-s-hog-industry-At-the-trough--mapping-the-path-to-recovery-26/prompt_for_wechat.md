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
- 已识别机构名：`HSBC`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份HSBC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China's hog industry

At the trough, mapping the path to recovery

\- Second-worst loss cycle since 2014 with self-breeding losses for around 9 months

\- Sow inventory reduction accelerates through 2Q26; supply contraction from 4Q26e driving hog price recovery

\- Maintain Buy ratings on Muyuan, Wens and Haid Group with unchanged TPs

Review: a record-breaking downcycle. China's hog sector is navigating its second-deepest loss cycle since 2014. The national hog price hit RMB9/kg in April 2026 – an all-time low since 2014 – and is currently oscillating around RMB9.5/kg. Self-breeding losses exceed RMB300/head, with over-RMB200/head losses persisting for over three months, making this the second-worst loss amplitude and the second-longest severe-loss episode on record. Despite pork being the cheapest animal protein source (supporting resilient demand evidenced by cold-storage inventory at a three-year high), oversupply has kept prices suppressed. The root cause traces back to May 2025, when MARA guided corporate producers to cut sow inventories, and while they complied, non-corporate producers expanded capacity, worsening the supply overhang for 1H26. Our estimates show that adding 10,000 head of sows against the policy tide in May 2025 would have incurred significant losses in March 2026 and onward.

## Outlook: capacity depletion underway; hog price inflection in 4Q26e. We

maintain our view that the decline in sow inventories will accelerate through 2Q26, driven by three forces: 1) financially strained non-corporate producers being forced to reduce sow herds (below, we analyze the losses from expanding sow heads against policy guidance in May 2025); 2) corporate producers maintaining sow levels per MARA guidance; and 3) piglet-specialist farms likely to cut capacity if 7kg piglet prices fall below RMB200/head. Production efficiency gains will partially offset the sow inventory reduction, but with the national sow inventory already down 3.3% y-o-y as of March 2026 and on track to reach MARA's 37.5 million target, we expect y-o-y hog supply to contract from 4Q26e onward, driving a moderate price recovery. Looking into 2027, sustained supply contraction should support a y-o-y price improvement.

Maintain Buy ratings on Muyuan, Wens and Haid. From a valuation standpoint, Muyuan Foods and Wens Foodstuff have both priced in this prolonged loss cycle and are trading at what we view as mid-cycle bottoms — levels that imply permanent impairment of earnings power, a scenario we believe is overly pessimistic given the hog cycle's self-correction mechanism. Haid Group offers an earlier earnings recovery catalyst in 3Q26e. We maintain our Buy ratings on Muyuan, Wens, and Haid. See valuation and key risks on page 2.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

China

Yihui Sha\* (Reg. No. S1700519100001)

Head of A-share Agriculture Research

HSBC Qianhai Securities Limited

yihui.sha@hsbcqh.com.cn

+86 21 5066 2004

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

No country for bears

The $24^{\text{th}}$ edition of the EM Sentiment Survey Click to view

Issuer of report: HSBC Qianhai Securities Limited

View HSBC Qianhai Securities Research at: https://www.research.hsbc.com

Source: Wind, HSBC Qianhai Securities estimates

Valuation and risks

<table><tr><td colspan="2"></td><td>Valuation</td><td>Risks</td></tr><tr><td>Haid Group002311 CH</td><td rowspan="2">Current price:RMB42.40Target price:RMB63.50Up/downside:+49.8%</td><td rowspan="2">Methodology: Target PE multiple (unchanged).Assumptions: We forecast a net profit CAGR of 13% in 2025-28e, 19% lower than the historical average in 2014-25; our target multiple is therefore 21.9x, 19% lower than the historical average in 2014-25. Based on our 2026e EPS of RMB2.90, we derive a target price of RMB63.50 (all unchanged). Our TP implies c50% upside to the current share price; we therefore retain our Buy rating on the stock.Yihui Sha* (Reg no: S1700519100001) | yihui.sha@hsbcqh.com.cn | +86 21 5066 2004</td><td rowspan="2">Downside risks◆ Overseas expansion below expectations◆ An avian flu outbreak◆ Unexpected surge in raw material prices◆ 2Q26e net profit under pressure due to drag of hog segment</td></tr><tr><td>Buy</td></tr><tr><td>Muyuan Foods002714 CH</td><td rowspan="2">Current price:RMB33.02Target price:RMB54.50Up/downside:+65.1%</td><td rowspan="2">Methodology: EV/EBITDA multiple (unchanged)Assumptions: We use an EV/EBITDA multiple of 10x, which is the 2014-24 historical average of its peers with high dividend payout ratio. Applying this target multiple to our 2026-27 average EBITDA of RMB38,133m, we derive a target price of RMB54.50 (all unchanged). Our TP implies c65% upside. Combined with the company&#x27;s cost leadership, industrial chain extension and expected industry cycle reversal, we maintain our Buy rating.Yihui Sha* (Reg no: S1700519100001) | yihui.sha@hsbcqh.com.cn | +86 21 5066 2004</td><td rowspan="2">Downside risks◆ African Swine Fever or other hog diseases◆ Slower-than-expected industry capacity reduction◆ Higher-than-expected raw material price hikes.◆ 2Q26e net profit under pressure due to sluggish hog price</td></tr><tr><td>Buy</td></tr><tr><td>WensFoodstuff300498 CH</td><td rowspan="2">Current price:RMB12.15Target price:RMB18.00Up/downside:+48.1%</td><td rowspan="2">Methodology: PB-ROEAssumption: Based on our 2026-27 average ROE estimate of 18%, we use a 2.52x target PB. Based on our 2026-27 average BVPS estimate of RMB7.16, we derive a target price of RMB18.00 (all unchanged). Our target price implies c48% upside. We maintain our Buy rating on this stock.Yihui Sha* (Reg no: S1700519100001) | yihui.sha@hsbcqh.com.cn | +86 21 5066 2004</td><td rowspan="2">Downside risks◆ African Swine Fever or other hog diseases.◆ Slower-than-expected industry capacity reduction.◆ Higher-than-expected raw material price hikes.◆ 2Q26e net profit under pressure due to sluggish hog price</td></tr><tr><td>Buy</td></tr></table>

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations  
Note: Priced as of 23 June 2026

## Where are hog prices now?

Absolute price: In April 2026, the national average hog price (source: National Bureau of Statistics, NBS) hit RMB9/kg, the lowest point since 2014 (Exhibit 1). The market has since recovered modestly to \~RMB9.5/kg but remains deeply depressed by historical standards.

Relative price (protein substitution): Pork prices relative to chicken, beef, eggs, and fish have all fallen to historical trough levels (Exhibit 2), making pork the one of the cheapest animal-protein sources in the current consumer environment. This provides a structural demand floor for pork consumption.

Profitability and loss cycle duration: deep and persistent losses. Self-breeding farmers are currently losing \~RMB300/head (source: Wind, Exhibit 3). Losses have endured for over 9 months (since Sep 2025, averaging RMB215/head). This is the second-deepest loss amplitude (after 2021's RMB318/head).

## Why are prices so low?

Supply-side driven, not demand-side. Pork's relative-value advantage as the cheapest animal protein should sustain resilient consumer demand. Indeed, downstream cold-storage inventory hit a three-year high year-to-date (source: SCI), signalling robust off-take from the processing channel and strong underlying consumption. The evidence points to oversupply as the primary driver, not weak demand.

Exhibit 1. Hog price (RMB/kg): lowest since 2014  
![](images/95a4d88ce28fe9d1dba9ee44905ad6e72078fb5ae24e8efa245f24f706bf58ee.jpg)  
Source: NBS, HSBC Qianhai Securities

Exhibit 2. Pork price near multi-year lows vs. other meats – lowest since 2014  
![](images/d699dc72ded053cfb7e1fda8415f51362398ee5a46beeceec3843d0886a3c99c.jpg)  
Source: Wind, HSBC Qianhai Securities

Exhibit 3. Profitability of self-breeding farmers since 2014 (RMB/head)  
![](images/f76aa89455c07a9ca05e881edc618728cf19abc79441ff26f0449dac8dd4e492.jpg)  
Source: Wind, HSBC Qianhai Securities  
Note: If a loss cycle is interrupted only by a brief period of profitability with profits under RMB50/head before reverting to losses, we treat the entire period as one continuous loss cycle.

Exhibit 4. Historical loss cycle of self-breeding farmers (since 2014)

<table><tr><td>Loss cycle</td><td>Duration</td><td>Avg Loss (RMB/head)</td></tr><tr><td>Jan ~ Jul 2014</td><td>6 months</td><td>-151</td></tr><tr><td>end-Oct 2014 ~ Apr 2015</td><td>6months</td><td>-70</td></tr><tr><td>Mar ~ Jul 2018</td><td>5 months</td><td>-198</td></tr><tr><td>Jan ~early Mar 2019</td><td>1.5 months</td><td>-70</td></tr><tr><td>Jun 2021~ Jun 2022 (excl. Nov 2021)</td><td>11 months (combined)</td><td>-318</td></tr><tr><td>Jan 2023 ~May 2024</td><td>16 months</td><td>-211</td></tr><tr><td>Sep 2025 – present (Jun 2026)</td><td>~9 months (ongoing)</td><td>-215</td></tr></table>

Source: Wind, HSBC Qianhai Securities

## Why the oversupply?

Hog supply from March 2026 onward is determined by the breeding sow inventory \~10 months prior, i.e., the sow herd dynamics starting May 2025.

In May 2025, the Ministry of Agriculture and Rural Affairs (MARA) held multiple meetings urging large-scale corporate farms to cap or reduce their sow herds, signaling an impending sector-wide contraction. The market turned more optimistic on 2026e hog prices in anticipation of reduced supply.

By end-September 2025, Muyuan's sow reduction alone exceeded the national total decline (Exhibit 5), suggesting that while corporate players complied with MARA's guidance to reduce or stabilise sow herds, non-corporate (smallholder) producers were still expanding capacity.

This is consistent with our previously published view: corporate players would pare sow numbers under policy direction but would simultaneously optimise their sow herd structure (higher PSY, better survival rates), boosting per-sow productivity and partially offsetting the headcount reduction. Meanwhile, non-corporate producers continued adding sows through at least September 2025, further inflating the supply pipeline for March-July 2026. This is the very reason we held a bearish view on 1H26 hog prices in our earlier reports (see Hog price downtrend continues in 1H26, 13 October 2025).

Exhibit 5. Quarterly changes in sow inventories since 2025 (m head)

<table><tr><td></td><td>Mar-25</td><td>Jun-25</td><td>Sep-25</td><td>Dec-25</td><td>Mar-26</td></tr><tr><td>National sow inventories (NBS)</td><td>40.39</td><td>40.43</td><td>40.35</td><td>39.61</td><td>39.04</td></tr><tr><td>changes (q-o-q, m head)</td><td></td><td>+0.04</td><td>-0.08</td><td>-0.74</td><td>-0.57</td></tr><tr><td>Muyuan&#x27;s sow inventories</td><td>3.49</td><td>3.43</td><td>3.31</td><td>3.23</td><td>3.13</td></tr><tr><td>changes (q-o-q, m head)</td><td></td><td>-0.05</td><td>-0.13</td><td>-0.07</td><td>-0.10</td></tr></table>

Source: NBS, Wind, company announcement, HSBC Qianhai Securities

## How much did adding 10,000 sows in May 2025 lose?

We simplify the hog production chain to two cases for breeding sows: 1) selling piglets; or 2) selling finishing hogs.

Scenario 1: Purchasing culled sows as breeding sows. Culled sows typically weigh 180kg+. In May 2025, the average culled-sow price was RMB11.7/kg, implying a total outlay of RMB21.1m for 10,000 head.

\- Weaned piglet path. Weaned piglets from these sows would be ready by October 2025. At that time, the weaned-piglet price was RMB172/head vs. a cost of RMB292/head, resulting in a loss of \~RMB12.4m if all piglets were sold immediately.

\- Finishing hog path. We believe most non-specialised piglet producers would not sell piglets at a loss; they would instead raise piglets to finishing weight. The corresponding ready date would be March 2026. The average loss per finishing hog in March was RMB242/head, implying a total loss of \~RMB23.0m.

Scenario 2: Converting replacement gilts to breeding sows. In May 2025, the cost of a replacement gilt (50kg → breeding-ready) was RMB2,849/head. For 10,000 head, the upfront outlay was RMB28.5m. Subsequent piglet/hog losses are identical to Scenario 1.

Net-net: adding 10,000 sows between May and August 2025 would have incurred upfront costs of RMB20-30m. In addition, finishing hog sales may generate a further RMB20m in losses. We believe the combined sow purchase costs and finishing hog losses impose significant financial strain on hog breeding farmers.

Exhibit 6. Analysis of purchasing 1 breeding sow starting from May 2025 (RMB)

<table><tr><td></td><td>May 2025</td><td>Jun 2025</td><td>Jul 2025</td><td>Aug 2025</td><td>Sep 2025</td></tr><tr><td>Scenario 1</td><td>2,106</td><td>1,974</td><td>1,934</td><td>1,832</td><td>1,734</td></tr><tr><td>Scenario 2</td><td>2,849</td><td>2,840</td><td>2,837</td><td>2,855</td><td>2,859</td></tr><tr><td>Corresponding weaned piglet sale date</td><td>Oct 2025</td><td>Nov 2025</td><td>Dec 2025</td><td>Jan 2026</td><td>Feb 2026</td></tr><tr><td># of weaned piglet</td><td>10.3</td><td>10.3</td><td>10.1</td><td>10.2</td><td>10.3</td></tr><tr><td>Weaned piglet price(RMB/head)</td><td>172</td><td>207</td><td>218</td><td>292</td><td>360</td></tr><tr><td>Weaned piglet cost(RMB/head)</td><td>292</td><td>288</td><td>287</td><td>289</td><td>284</td></tr><tr><td>Profit/loss if selling weaned piglet</td><td>-1,240</td><td>-832</td><td>-702</td><td>30</td><td>785</td></tr><tr><td>Corresponding finishing hog sale date</td><td>Mar 2026</td><td>Apr 2026</td><td>May 2026</td><td>Jun 2026</td><td>Jul 2026</td></tr><tr><td># of finishing hogs</td><td>9.5</td><td>9.5</td><td>9.3</td><td>9.4</td><td>9.5</td></tr><tr><td>Profit/loss if selling finishing hogs</td><td>-2,298</td><td>-3,135</td><td>-2,831</td><td>-2,965</td><td>NM</td></tr></table>

Source: SCI, Wind, HSBC Qianhai Securities estimates

## Why will capacity continue to deplete?

Non-corporate producers who expanded against policy guidance are under severe financial strain. Our analysis suggests these players suffered meaningful losses from the May 2025 expansion and are now being forced to reduce capacity, even if their price outlook remains optimistic.

Corporate producers have already reduced sow inventory in line with MARA guidance. Absent further policy intervention, we expect corporate sow herds to stabilise at current levels. Additional policy pressure could trigger further reductions.

Other self-breeding farmers, even those who did not expand in May 2025, are being squeezed by the March – June 2026 deep-loss environment. The sustained losses will push these operators to reduce sow inventory as working capital depletes.

Piglet-specialist farms. Weaned-piglet prices held up relatively well through 1H26, keeping losses modest and not yet triggering this capacity exit, in our view. However, if the 7kg weaned-piglet price falls and stays below RMB200/head, we expect this segment to accelerate capacity reduction as well.

Conclusion: We maintain our view that hog industry capacity will accelerate its decline through 2Q26e.

Exhibit 7. Self-breeding profits (RMB/head)  
![](images/17b17d8878098e1448dacc1e382dd15a0995d48c95432aa7c90dc1304e470ad2.jpg)  
Source: SCI, HSBC Qianhai Securities

Exhibit 8. Piglet (7kg) price (RMB/head)  
![](images/d3d627f79f5a02ae25b6c74d0f4c6477c5074ee786b083929e8833ea055281c7.jpg)  
Source: SCI, HSBC Qianhai Securities

## The impact of efficiency gains

Efficiency improvements will partially offset the impact of sow inventory reduction. We estimate the sow efficiency corresponding to finishing hog volumes in:

◆ 1H26e: Production efficiency +2-3% y-o-y

2H26e: Further improvement to +4-5% y-o-y, though persistent losses may cap actual gains below this range

2027e: Efficiency improvement of \~2-3% y-o-y, driven primarily by:

\- Sow structure optimisation at corporate farms

\- Elimination of low-efficiency capacity from non-corporate producers forced out of the market

This is consistent with the production efficiency trajectory observed among leading corporate players since 2024.

As of March 2026, the national breeding sow inventory was down $3.3\%$ y-o-y. MARA has lowered the target sow inventory threshold to 37.5m head. Given deep losses in 2Q26, if the sequential monthly decline averages $0.5 - 1\%$ , the sow herd could reach MARA's target by 3Q26e, implying a y-o-y decline of approximately $7\%$ .

We therefore expect China's hog supply to contract y-o-y in 2027e, driving a year-on-year price recovery.

## When is the inflection point?

Based on breeding sow inventory trends combined with production efficiency indicators, we expect y-o-y supply contraction to begin in 4Q26e. However, the rising cold-storage inventory (at a three-year high y-t-d) will partially absorb the supply reduction.

Our base case: a moderate price recovery in 4Q26e, rather than a sharp rebound. A full-cycle recovery would require sustained depletion of both live-hog and cold-storage inventories.

# Disclosure appendix

## Analyst Certification

The following analyst(s), economist(s), or strategist(s) who is(are) primarily responsible for this report, including any analyst(s) whose name(s) appear(s) as author of an individual section or sections of the report and any analyst(s) named as the covering analyst(s) of a subsidiary company in a sum-of-the-parts valuation certifies(y) that the opinion(s) on the subject security(ies) or issuer(s), any views or forecasts expressed in the section(s) of which such individual(s) is(are) named as author(s), and any other views or forecasts expressed herein, including any views expressed on the back page of the research report, accurately reflect their personal view(s) and that no part of their compensation was, is or will be directly or indirectly related to the specific recommendation(s) or views contained in this research report: Yihui Sha

## Important disclosures

## Equities: Stock ratings and basis for financial analysis

HSBC and its affiliates, including the issuer of this report (“HSBC”) believes an investor’s decision to buy or sell a stock should depend on individual circumstances such as the investor’s existing holdings, risk tolerance and other considerations and that investors utilise various disciplines and investment horizons when making investment decisions. Ratings should not be used or relied on in isolation as investment advice. Different securities firms use a variety of ratings terms as well as different rating systems t

[中间内容因长度限制已省略]

cation has been distributed by HSBC Continental Europe or by such other HSBC affiliate from which the recipient receives relevant services.

In Japan, this publication has been distributed by HSBC Securities (Japan) Co., Ltd.. It may not be further distributed in whole or in part for any purpose. In Korea, this publication is distributed by either The Hongkong and Shanghai Banking Corporation Limited, Seoul Securities Branch ("HBAP SLS") or The Hongkong and Shanghai Banking Corporation Limited, Seoul Branch ("HBAP SEL") for the general information of professional investors specified in Article 9 of the Financial Investment Services and Capital Markets Act ("FSCMA"). This publication is not a prospectus as defined in the FSCMA. It may not be further distributed in whole or in part for any purpose. Both HBAP SLS and HBAP SEL are regulated by the Financial Services Commission and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc., a US-registered broker-dealer and member of FINRA, accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Qianhai Securities Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Qianhai Securities Limited.
"""
