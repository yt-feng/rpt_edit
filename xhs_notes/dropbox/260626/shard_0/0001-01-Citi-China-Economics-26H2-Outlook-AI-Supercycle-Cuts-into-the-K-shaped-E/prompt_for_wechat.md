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
# China Economics

## 26H2 Outlook: AI Supercycle Cuts into the K-shaped Economy

## CITI'S TAKE

AI is now front and center in China's K-shaped economy. The AI supercycle further powers the strong leg – exports, production and the new economy. Meanwhile, AI-driven job displacement weighs on consumer confidence, and the significant AI buildout risks crowding out old economy investment. Overall trickle-down has been limited, with the weak leg fragmenting into distinct winners and losers across sectors and geographies. Policy will likely stay targeted against this backdrop. We maintain our 4.7% growth forecast for 2026E, with 26Q2 likely the low point. The July Politburo should signal piecemeal consumer support – not broad-based stimulus, in our view. An outright deficit expansion is not our base case, but we believe fiscal deployment is set to accelerate. While monetary policy is not in the driver's seat, we keep our call for a symbolic 10bps rate cut in 26H2E.

Xiangrong Yu $^{AC}$ +852-2501-2754
xiangrong.yu@citi.com

Xinyu Ji $^{AC}$ +852-2501-2792
xinyu.ji@citi.com

Yuanliu Hu $^{AC}$

+852-2501-2746

yuanliu.hu@citi.com

AI has become the defining force shaping China's K-shaped economy. We have characterized China's post-Covid recovery along two dimensions: [1] supply consistently outpacing domestic demand, with exports filling the gap; and [2] the new economy outperforming the old (see: China Outlook 2026: Mind the Gap). The DeepSeek moment in early 2025 helped materially accelerate the AI-centric new economy, which has since broadened its macro footprint through intensifying AI deployment. The AI supercycle deepens the existing fault lines (Figure 1).

■ Widening divergence: The AI supercycle is powering production, exports, and new economy activity, reinforcing the strong leg of the K. At the same time, AI-driven labor displacement risks – while not yet material – are weighing on consumer confidence (see: The Macro-Micro Disconnect of AI-Driven New Economy). The significant AI buildout also risks crowding out old economy investment.

■ Domestic fragmentation: The AI supercycle is creating distinct winners and losers across sectors and geographies, even as overall trickle-down to the old economy has been limited. The weak leg is no longer monolithic – AI-adjacent industries, cities, and even individuals are pulling ahead, against an otherwise sluggish backdrop.

■ "AI-first policy": Despite the policy rhetoric of "employment-first" and "investing in people", the "AI+" initiative is clearly the strategic focus in practice. We believe, so long as social stability holds, facilitating the AI transition sits at the top of the policy hierarchy. With the growth target revised down, the urgency for broad-based cyclical stimulus appears low to us – reinforcing a selective, tech-oriented policy posture.

Figure 1. AI is now front and center in China's K-shaped economy  
![](images/f1f7232fcee766d6b21844657dc3e813e685be5307917184fb398bc67ee61e78.jpg)

We maintain our growth forecast at 4.7% YoY for 2026E. The AI supercycle anchors the headline number, particularly through supply-side strength. 26Q2 is likely to be a low point in the quarterly trajectory, partly due to the Middle East shock and lagging fiscal deployment. On prices, the energy shock has driven the first leg of PPI reflation; we believe anti-involution and AI inflation are poised to drive the next. We reckon nominal growth could reach a five-year high of 6.7% in 2026E.

Source: MIIT, news reports, Citi

We expect targeted, piecemeal support to domestic demand ahead – not broad-based big stimulus. Structural efforts such as the "Six Networks" initiative are underway, enabling AI adoption and stabilizing investment. We see a good chance that the July Politburo meeting (held on the 30 $^{th}$ in 2025) may signal incremental measures to support consumption and household income. That said, an outright increase in the budget deficit or special government bond quota is not our base case. While monetary policy is not in the driver's seat, we keep our call for a symbolic 10bps rate cut in 26H2E. We expect the PBoC to maintain its managed appreciation bias on the exchange rate to facilitate RMB internationalization and see USDCNY edging towards 6.7.

## The AI economy takes off

The AI economy is shifting from intangible algorithm development to tangible infrastructure buildout. The DeepSeek moment settled a pivotal question – China can innovate in AI. OpenClaw and the rise of agentic AI have since recharged the momentum, further cementing the trend as the most significant technological transition for China in decades (Figure 2). The shift is visible across at least three dimensions:

■ Token: China's daily token usage hit 140trn in March 2026, up from 0.1trn at the beginning of 2024 (Figure 3).

■ Computing power: China's intelligent computing tripled in 2025 vs. 2024, according to MIIT data (Figure 4).

■ Equity market: AI-related outperformance has rotated from internet giants to semiconductor manufacturers and materials providers – mirroring the broader shift from intangible algorithm development to tangible infrastructure buildout (Figure 5).

AI is now front and center in China's K-shaped economy. The post-Covid recovery has been bifurcated with supply outpacing demand (Figure 6), external demand ahead of domestic demand (Figure 7), and the new economy leading the old. The unfolding AI supercycle is set to widen the divergence and create further fragmentation within the weak leg, in our view.

Figure 2. China is now perhaps in the most significant technological transition in decades  
![](images/075dcd023049e8a14d6e4740629c8716ea534024c24f0a875576c5911ebe5923.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: GenAI Adoption Tracker, MIIT, Citi

Figure 3. China's daily token usage hit 140trn in March, up from 0.1trn in early 2024  
![](images/e653d9a3a99de390845589350c48941b5109aa607c56db0630887c3049c3c5ef.jpg)

Figure 4. China's intelligent computing tripled in 2025 vs. 2024  
![](images/f4f4c38e24c51d0af1489fa318416f42e7719200ed390d39a7e455f9d605afd9.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: MIIT, news reports, Citi  
Figure 5. AI-related outperformance has rotated from internet giants to semiconductor supply chains  
![](images/335d63be3deaca15971d7902e3897c7e17b88500d8dd268f60afde8249248481.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission.
Note: AI models (Tencent, Meituan, Alibaba, Kuaishou, Baidu, SenseTime, Ubtech, Zhipu and Minimax) and semiconductor supply chains as compiled by Wind.  
Source: Wind, Citi

Figure 6. China's post-Covid recovery has been bifurcated with supply outpacing demand  
![](images/39902217a8b25d053723a0f79e04ccde78b34077a9d76e9662511c155e6243c4.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: NBS, Wind, Citi

Figure 7. External demand fills the gap between supply and domestic demand  
![](images/aa03ad34f92bda6b6b9b4206ed3498a63ac6b497335da53defaa27d434d6c054.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission.
Source: NBS, Wind, Citi

## A further boost to the strong leg

The AI supercycle serves as another boost to exports, as evidenced by the strong growth seen so far. Even if export momentum were to subside, we believe China's own AI-transition demand could sustain production.

## Exports: from cyclical strength to structural tailwind

China's export boom this year is more structural than cyclical. Three features stand out:

■ AI hardware: AI-related exports – spanning upstream chips, midstream power equipment, and downstream personal electronics – accounted for 20.3% of China's total exports in 2025 (Figure 8). Growth accelerated to 34.8% YoY in Jan-May 2026, contributing 6.8 ppts to headline export growth of 15.6% YoY over the © 2026 Citi Inc. No redistribution without Citi's written permission.
Source: China Customs, Citi same period (Figure 9). With the global AI transition still in its early stages, this strength is unlikely to falter soon.

Prices: PPI reflation, which kicked in from March, contributed \~5ppts to export growth of 14.0%YoY in April (latest available), with AI-related items logging price surges across the supply chain (Figure 10). This dynamic is translating into meaningful revenue and profit growth – profits in telecom equipment manufacturing jumped 107.7%YoY in Jan–April.

■ Energy transition: The global energy transition, amplified by the Middle East conflict, provides a further tailwind to China's "New Three" exports (Figure 11). Growth reached 51.5% YoY in the first five months of 2026, contributing 2.2ppts to the headline.

We revise up our export growth forecast to 13.0%YoY for 2026E. Imports could also stay buoyant at 22.0%YoY, leaving the trade surplus at US\$1.1trn. Structural drivers – unlike the competitiveness-led cyclical support of 2024–25 – are likely to prove more resilient.

Protectionism poses downside risks but is unlikely to derail China's export growth. On the US-China front, risks appear well contained following the IEEPA ruling and the summit between President Trump and President Xi in Beijing, not to mention potentially more presidential meetings in 26H2E. EU risks are rising, with further measures against Chinese exporters in preparation (Reuters, Jun 18, 2026). That said, the US precedent could be instructive: despite accounting for 14.6% of China's exports in 2024 and peak tariffs of \~145%, China's exports held up throughout the year. The EU now represents a similar 14.9% share; how aggressive its measures will be remains to be seen. Protectionism risk may be real but not significant enough to derail growth, in our view.

Figure 8. AI-related exports generally accounted for $20.3\%$ of China's total exports in 2025

<table><tr><td>Category</td><td>Subcategory</td><td>CN Exports, US$ bn (2025)</td></tr><tr><td>Upstream</td><td>Semiconductors &amp; Integrated Circuits</td><td>216.4</td></tr><tr><td>Upstream</td><td>Printed Circuit Boards &amp; Electronic Assembly</td><td>35.9</td></tr><tr><td>Upstream</td><td>Memory &amp; Storage Components</td><td>4.0</td></tr><tr><td>Upstream</td><td>Passive Components &amp; Connectors</td><td>24.4</td></tr><tr><td>Upstream</td><td>Cables &amp; Interconnects</td><td>28.6</td></tr><tr><td>Midstream</td><td>Semiconductor Manufacturing Equipment</td><td>5.7</td></tr><tr><td>Midstream</td><td>Testing &amp; Inspection Equipment</td><td>7.6</td></tr><tr><td>Midstream</td><td>Servers &amp; Data Processing Equipment</td><td>49.8</td></tr><tr><td>Midstream</td><td>Networking &amp; Communication Infrastructure</td><td>41.8</td></tr><tr><td>Midstream</td><td>Power Supply &amp; Management</td><td>115.1</td></tr><tr><td>Midstream</td><td>Cooling &amp; Thermal Management</td><td>21.4</td></tr><tr><td>Midstream</td><td>Displays &amp; Interface Components</td><td>1.7</td></tr><tr><td>Downstream</td><td>Mobile Devices &amp; Personal Computing</td><td>213.9</td></tr></table>

Figure 9. Their growth accelerated to 34.8%YoY in Jan-May 2026, contributing 6.8ppts to headline growth  
![](images/dbce3332f9224464437ed53d2e70caba038d5bfe533c9f0014302c12ae6e033b.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission.
Source: China Customs, Citi

Figure 10. AI-related items also logged strong price momentum across the supply chain  
![](images/e595c635560da711305c6f86cb36b6dde57cc346e122a6ab7538e2b33c114a13.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission.
Source: China Customs, Citi

Figure 11. Global energy transition amplified by the Middle East conflict provides a further tailwind to Chinese exports  
![](images/0a548d283865fae6cd6658385decfd6d15a89145c3dba868f69f6d00b61094ca.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission.
Source: China Customs, Wind, Citi

## Production: high-tech takes the wheel

Production could prove even more resilient than the export cycle. China's own AI-driven demand is pushing high-tech production higher – and could sustain momentum even if export growth were to subside.

■ High-tech IP rose 13.1% YoY Ytd, with the monthly rate accelerating to a five-year high of 15.1% YoY in May. Despite carrying a weight of \~17%, its contribution to headline IP has exceeded 50% (Figure 12). Elsewhere in the industrial complex, resilience is wearing thin.

■ AI-related output growth is gaining momentum. IC output expanded 25.4%YoY in Jan-May, while export volumes only grew 8.8%YoY – with 3% of the increase directed towards domestic use. Industrial robot output grew 28.1%YoY, reflecting AI's growing footprint in manufacturing (Figure 13).

Figure 12. High-tech IP rose 13.1% YoY Ytd, contributing >50% to headline growth  
![](images/d99b829d84b212cd554a1da67e45db70e59cff781d51d56e159e3dafdf44ba95.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission.
Source: NBS, Wind, Citi

Figure 13. AI's footprint in manufacturing grew with output growth standing out for ICs and industrial robots  
![](images/3e2d320fe8be441cc4fc2159b14226cfabd8794fdddb6b7bf491ae7cdf7d6b29.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission.
Source: NBS, Wind, Citi

## Rising fragmentation in the weak leg

The booming new economy offers little relief to the weak leg of the K-shaped economy. The AI supercycle is creating distinct winners and losers across sectors and cities, rather than supporting a broad-based recovery. At best, the new economy generates sporadic rebounds in domestic demand.

Consumption & property: sporadic gains, no broad recovery

AI-driven job displacement risks could weigh further on already subdued consumer confidence. Early to assess AI's job market impact in China, we estimate that \~70.3mn jobs face displacement risk from AI deployment. With adoption gaining traction, displacement could start to surface – most visibly in new hiring, particularly among college graduates.

■ Consumer confidence dipped further in April from an already subdued level (Figure 14). The index has been trending below the neutral benchmark of 100 for 50 consecutive months since April 2022. The decline coincided with rising equity market volatility and the above-seasonal increase in unemployment in March – before normalization in April.

■ Household risk appetite stays low. Net loan repayments reached RMB631bn in the first five months of 2026 (Figure 15), with deposit reallocation only beginning to stir. Households still hold RMB28.4trn in excess deposits as of May relative to the linear trend, and the saving rate remained elevated at 41.8% in 26Q1 vs. 38.5% in 19Q1.

■ Policy impulse is fading. Consumption policies have been steady, yet the high base from 2025 and lagging fiscal deployment drove an outright contraction in retail sales of -0.6% YoY in May – the first decline since Covid (Figure 16).

The new economy could, at best, generate sporadic gains within the weak leg. In property, Tier-1 city prices have stabilized, while the national index continues to search for a bottom (Figure 17), with AI startups and hardware suppliers concentrated in major city clusters. Luxury sales have also held up despite the headwind from the Middle East conflict (SCMP, May 25, 2026).

Figure 14. Consumer confidence dipped further in April from an already subdued level  
![](images/fbbd4121d72809a985f0a67061bee678ec24796ee987ec016dd1d784215ce5b7.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: NBS, Wind, Citi

Figure 15. Household risk appetite stays low with net loans repayment of RMB631bn in Jan-May  
![](images/d199021f9a141e317689955404cbc32d93e218e80236e70eab3fac9869fd80af.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission.
Source: PBoC, Wind, Citi

Figure 16. Fading trade-in subsidies drove an outright negative reading of retail sales growth in May  
![](images/28cb58cb77c131d88b5253ff05ca661dbbcf247fc8fdaa99cea8e1464df644cb.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission.
Source: NBS, Wind, Citi

Figure 17. Home prices in Tier-1 cities have held up, while the national index continues to search for a bottom  
![](images/298bbfcb6be8486bf51bb15563cb39bdf2d1b0fd22e76d824cc539ec0b40b3fc.jpg)  
©2026 Citi Inc. No redistribution without Citi's written permission. Source: NBS, S&P/Case-Shiller, Haver Analytics, Wind, Citi

## Investment: AI buildout leads, the rest lags

AI-related investment is building its own momentum, while headwinds gather for the rest. With fiscal resources constrained, the significant AI buildout also risks crowding out old economy investment.

■ AI: IT-related FAI stays buoyant even as headline FAI retreats. Citi's tech team estimates \~RMB641bn in domestic capex across hyperscalers and third-party data centers. IT services FAI surged 13.8%YoY in Jan-May, and telecom equipment manufacturing FAI rose 6.7%YoY over the same period (Figure 18). The ongoing "Six Networks" initiative should provide an additional tailwind.

■ Other: Headwinds for the rest are mounting, driven by [1] lagging fiscal deployment, [2] uncertainty from the Middle East conflict, [3] anti-involution pressures, and [4] squeezed margin in downstream sectors. Notably, infrastructure investment posted a double-digit decline in May, despite the buoyant new-infrastructure buildout (Figure 19).

Figure 18. IT-related FAI stays buoyant even as headline FAI retreats, with IT services at 13.8% YoY  
![](images/48defe271ee72126edd2d18dff877fc14e00e6153fcb8e3fa012d9eb5ac68927.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: NBS, Wind, Citi

Figure 19. AI buildout could even crowd out old economy investment, particularly in traditional infrastructure  
![](images/16974572c10e066d7a0d4a8428259ac7366b5b8f978ac3066c46390b945a4b0c.jpg)  
Source: NBS, Wind, CitiResearch

©2026 Citi Inc. No redistribution without Citi's written permission.
Source: NBS, Wind, Citi

## Reflation: not all boats are lifted

The long-awaited PPI reflation has arrived, broader than an energy shock but very uneven. The Middle East conflict drove the initial leg, while broad AI supply chains and construction costs are now extending the recovery (Figure 20). Profit rebounds t

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the "Product"), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
