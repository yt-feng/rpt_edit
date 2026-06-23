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
# China Spirits Tracker: Dragon Boat Festival sell-through lapping low base but demand remained polarized across pricing tier; More resilient

Dragon Boat Festival (Jun 19-21) consumption sentiment: Overall pax mobility recorded a -0.9% yoy decline at 648mn, per Ministry of Transport. Retail and catering demand: key 78 shopping areas had 4%/3.5% yoy growth in total traffic and retail sales for the first two days (MOFCOM monitored scope).

Dragon Boat Festival spirits demand remained highly polarized by price range and consumption scenario, with sell-through recovery mainly concentrated in super-premium category and selected regions, while the upper mid end segment remained under pressure. Our latest channel checks suggest Dragon Boat Festival sell-through improved slightly yoy but still meaningfully below the 2024 level (pre Anti-graft policy in May 2025) for the spirits sector. For the super-premium category, most regions saw 10\~20%+ yoy sell-out volume growth for Moutai/Wuliangye with prepayment of 60%+/55%-70%, respectively (while sell-out declined by DD% in Dragon Boat Festival in 2025, ie. down c.10\~20% for Feitian). Meanwhile, sub-premium/mass products are relatively muted yoy except for some key SKUs/regions like King's Luck's Danya reaching DD% sell-through growth (Exhibit 1). Online shared a similar trend, with JD 618 report indicating that overall spirits GMV increased 25% yoy driven by strong growth in Moutai (Feitian original package GMV reached Rmb300mn) and Wuliangye (Common 8th Wuliangye World Cup edition GMV increased over 13-fold). Overall, we noted that Dragon Boat Festival typically has a small seasonal impact on China's spirits consumption vs Mid Autumn Festival/National Holiday and 618 promotional intensity was relatively rational and less disruptive to offline wholesale pricing this year (e.g. Feitian online ASP post-subsidy had a small gap vs distribution channel wholesale prices).

On the demand side, traditional business-related/government related demand still remained significantly below historical levels, while gifting and mass self-consumption continued to serve as the key demand pillars. Banquet scenario consumption volume also remained weak. Gifting demand remained the key pillar for Feitian Moutai, while sell-through for regional mid-end brands (Rmb 100+\~300 price range) was still mainly driven by personal consumption/dining demand. Regional divergence persisted: Anhui remained relatively weak amid ongoing constrained commercial/government-related activities, while Jiangsu/Sichuan saw slight recovery. Jiangsu showed signs of easing policy impact, with mom improvements driven by development of technology sectors. In Sichuan, business demand increased by teens% yoy, although it remained 30%-40% below 2024 levels.

Feitian Moutai wholesale price slightly decreased, while Common Wuliangye

Leaf Liu
+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Christina Liu
+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

and Guojiao 1573 stayed largely flattish. In the past 1 week, original case Feitian Moutai's wholesale price/bottle decreased by Rmb25 from Rmb1,670 to Rmb1,645, and unpacked Feitian Moutai's wholesale price decreased by Rmb5 from Rmb1,635 to Rmb1,630. For non-standard Moutai SKUs, the wholesale price of Zodiac/Moutai 1L decreased by Rmb10/120 per bottle, Jingpin Moutai stayed flattish and Moutai 15 years increased by Rmb10 per bottle. Common Wuliangye's wholesale price/bottle stayed flattish/decreased by Rmb10 at Rmb840/to Rmb750 per "Daily Spirits Prices"/Bairong Wholesale Market, respectively. Guojiao 1573's wholesale price/bottle stayed flattish at Rmb840.

The authors would like to thank Lily Qi for her contribution to this report.

Exhibit 1: Post Dragon Boat Festival channel check summary table

<table><tr><td>Brand</td><td>Sell-through</td><td>Prepayment YTD</td><td>Distributor inventory</td><td>Wholesale price trend</td></tr><tr><td>Moutai</td><td>Feitian 20%+ yoy growth YTD</td><td>c.63% (Jun prepayment executed, 5% of full year)</td><td></td><td>Feitian at Rmb1,630-1,645/ bottle; non-standard SKUs price slightly decreased recently</td></tr><tr><td>Wuliangye</td><td>Common Wuliangye 20%+ yoy growth; 1618 is expected to grow at 15%</td><td>overall 55%-70% (divergent nationwide), 1618 at 70%</td><td></td><td>Common Wuliangye stable at Rmb750/bottle</td></tr><tr><td>Luzhou Laojiao</td><td>Decreased significantly, esp. in Henan</td><td>30%+ (40-60% last year for most distributors)</td><td></td><td>Guojiao 1573 price stable at Rmb850/bottle</td></tr><tr><td>Fen Wine</td><td>10%+ growth YTD, DD% growth for Bofen</td><td>45%-55% (55% in same period last year), no compulsory prepayment</td><td>Qing 20 at c.3.5 months</td><td>Qing 20 price stable at Rmb350/bottle</td></tr><tr><td>King&#x27;s Luck</td><td>slightly improved in 2Q; DD% growth for Danya driven by stable channel profit and strict pricing policy</td><td>55% for mid-Jun, expect to reach 60% in end-Jun, slower yoy</td><td>c.4 months+</td><td>largely stable for key SKUs</td></tr><tr><td>Yanghe</td><td>slightly decreased in 2Q</td><td>40%+</td><td>Ocean Blue &lt; 2 months</td><td>largely stable for key SKUs</td></tr><tr><td>Gujing</td><td>Dragon Boat Festival sell-through backed by Rmb200 below price range (mass product)</td><td>55%-60%+ (vs 70% target from company at end-2Q)</td><td>&gt;3 months</td><td>Resilient for Rmb300+ price range in Anhui</td></tr></table>

Source: Channel checks  
Weekly Momentum of China Spirits Sector

![](images/52ec476f2204e83d5075ee0a64973b8904c1e428c8121bdc357df625ce22ba82.jpg)  
Source: GS Global Investment Research

i-Moutai APP tracker: Our Quest Mobile database indicated monthly active users (MAU) on the i-Moutai app reached 10.2mn/10.1mn in May/Apr, up by 4.4%/0.4% yoy, normalized vs. 18mn MAU in 1Q26 on average and is still above the level before Feitian Moutai's launch (MAU at 5\~7mn in 4Q25). DAU/MAU penetration ratio was at 11%/11% in May/Apr.

Exhibit 2: I-Moutai active users surged from Jan 1st 2026 when Feitian was officially launched on i-Moutai  
![](images/4863b459c63e007d75581e040558ad796783ef335d7d9b0f040894f2da38e692.jpg)  
Source: Quest Mobile

## Key news this week:

Moutai announced its 2025 final dividend distribution (Jun 21): Moutai's 2025 dividend distribution was approved on Jun 21 with a cash amount of Rm35.033bn (2025 accumulated dividend at Rmb65.033bn after including interim dividend) and ex-dividend date on Jun 26.

JD released its 618 spirits report (Jun 19): JD released its 618 spirits report covering May 13 to Jun 18, showing 25% yoy growth for overall spirits GMV and strong growth for brands including Moutai/Wuliangye/Guotai etc. Moutai 26 Feitian (original package) GMV reached Rmb300mn and Common 8th Wuliangye (collaborating with World Cup 2026) GMV increased over 13-fold.

\- Jiugui collaborated with Hunan restaurant chains during Dragon Boat Festival (Jun 19): Jiugui launched its 2026 Dragon Boat Festival themed event with well-known Hunan cuisine restaurant chains including Huogongdian and Qinhuang shifu.

## Wholesale price summary of high-end liquors

## From Jun 12 to Jun 21, 2026:

Original case Feitian Moutai's wholesale price/bottle decreased by Rmb25 from Rmb1,670 to Rmb1,645, and unpacked Feitian Moutai's wholesale price decreased by Rmb5 from Rmb1,635 to Rmb1,630.

Common Wuliangye's wholesale price/bottle stayed flattish/decreased by Rmb10 at Rmb840/to Rmb750 per “Daily Spirits Prices”/Bairong Wholesale Market, respectively.

Guojiao 1573's wholesale price/bottle stayed flattish at Rmb840.

From Jan 1 to Jun 21, 2026:

Original case Feitian Moutai's wholesale price/bottle increased by Rmb140 from

Rmb1,505 to Rmb1,645. Unpacked Feitian Moutai's wholesale price/bottle increased by Rmb140 from Rmb1,490 to Rmb1,630.

Common Wuliangye's wholesale price/bottle decreased by Rmb10 to Rmb840 per "Daily Spirits Prices," and decreased by Rmb60 to Rmb750 per Bairong Wholesale Market.

Guojiao 1573's wholesale price/bottle stayed flattish at Rmb840.

Exhibit 3: 53% Feitian Moutai product prices  
![](images/c2ed777183542d6b1182e3968bcef3e689044daedde7bca6ee389f343659f2c4.jpg)  
Most recent data points as of Jun 21, 2026.  
Source: Daily Spirits Prices, Data compiled by GS Global Investment Research

Exhibit 4: 52% Common Wuliangye product prices  
![](images/b7887a67453be5ced47a7d9c29d8c97841b363de15f19cd46cc3f2cf1e08ef35.jpg)  
Most recent data points as of Jun 21, 2026. Source 1 = Spirits Price References; Source 2 = Daily Spirits Prices; Source 3 = Bairong Wholesale Market  
Source: Spirits Price References, Daily Spirits Prices, Bairong Wholesale Market, Data compiled by GS Global Investment Research

Exhibit 5: Guojiao 1573 product prices  
![](images/75d7e4b75c4e285d926adb91a0b7483b9694ee6ec29b5d0bde2786252cd4cfff.jpg)  
Most recent data points as of Jun 21, 2026.  
Source: Daily Spirits Prices, Data compiled by GS Global Investment Research

Moutai non-standard SKUs: In the past 1 week, the wholesale price of Zodiac/Moutai 1L decreased by Rmb10/120 per bottle, Jingpin Moutai stayed flattish and Moutai 15 years increased by Rmb10 per bottle.

Exhibit 6: Wholesale prices of Moutai's 4 non-standard SKUs  
![](images/62f9c22b05383cb04422714afe28392ffbd90c4aeeecf9c58214c9ffb507e990.jpg)  
Rmb/bottle Jingpin Moutai (53%, 500ml)

![](images/d7879f400ce86aca9682f092c22208f379baa08ddd7e9e73abd0698c29ead5f4.jpg)

![](images/ed7f962aa5cf6d1e13d0c5f97d2bddc5f24f3d2d8229b8f56fbb9df2c7ec35fb.jpg)  
Latest data as of Jun 21, 2026.

Rmb/bottle Moutai 15 years (53%, 500ml)  
![](images/27aaa06073ab9432507070f5b060265dc5e617b1d0b79056967ade558df751e1.jpg)

Exhibit 7: 2024-2026 channel policy and product launch summary of key spirits companies - Part I

<table><tr><td>Year</td><td>Month</td><td>Kweichow Moutai (600519.SS)</td><td>Wuliangye Yibin (000858.SZ)</td><td>Luzhou Laojiao (000568.SZ)</td><td>Jiangsu Yanghe (002304.SZ)</td><td>Shanxi Fen Wine (600809.SS)</td><td>Jian Nan Chun(Private, Not Covered)</td></tr><tr><td>2026</td><td>May</td><td>Week 3: Moutai raised the RSP of select non-standard SKUs on a Moutai APP effective May 16. The scope of price hikes include 53% vol 500ml Moutai 15 years (Rmb4,199/bottle to Rmb4,279/bottle), Jingpin Moutai (Rmb2,299/bottle to Rmb2,359/bottle), Zodiac Moutai (Horse precious) (Rmb2,499/bottle to Rmb2,669/bottle) and 1L Moutai (Rmb2,989/bottle to Rmb3,119/bottle).</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2026</td><td>Mar</td><td>Week 4: raised the ex-factory price of Feitian Moutai (53% vol, 500ml, 2026 edition) from Rmb1,169/bottle to c.Rmb1,269 per bottle (mainly cover wholesale channels), and the RSP of Feitian Moutai from Rmb1,499 to Rmb1,539 (mainly cover direct sales channels, esp. i-Moutai platform), effective immediately from Mar 31, 2026.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2026</td><td>Mar</td><td>Week 3: introduced a consignment sales policy for non-standard Moutai products participating distributors must apply and pay a deposit and will receive a c.5% rebate on these products sales</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2026</td><td>Jan</td><td>Week 3: plans to employ a more market-driven pricing framework to optimize channel investments and safeguard channel profitability, presented new RSP for Feitian Moutai vintage and other non-standard SKUs and lowered ex-factory price for some non-standard/series products</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Dec</td><td>Week 5: officially announced the launch of Feitian Moutai across 53% vol 500ml (years 2019-2026), 100ml/1,000ml Feitian, and multiple series on i-Moutai, including Jingpin, Zodiac, Vintage, Cultural, and lower-alcohol variants (Dec 30)</td><td>Week 2: nominal prepayment price for Common Wuliangye lowered to Rmb900 from Rmb1,019 for 2026 and distributor cost below c.Rmb850 (more rebate will be announced on 18 Dec)</td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Nov</td><td>Week 4: New series of Moutai Prince (Black Gold) new version released</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Aug</td><td>W4: New version of Moutai 1935 was launched with suggested retail price set at Rmb998&#x27;</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Jun</td><td>W3: Suspended the shipment of 53% 500ml Feitian Moutai for all channels; Implemented disciplinary measures to distributors including punishments against selling below RMB2,000/bottle and restrictions from shipping to certain retailers.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Apr</td><td>W4: Updated bundled sales policy in self-operated specialty stores for registered enterprise and individual customers</td><td></td><td>W4: Suspended order taking and shipment until pre-Dragon Boat Festival for all SKUs</td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Feb</td><td></td><td></td><td>W3: Suspended order taking and shipment of Tequ 60 and Old Touqu</td><td>W2: Suspended order taking for 6th Ocean Blue in Jiangsu; Suspended order taking for Guijiu - Gold/Red in Henan since Feb 14</td><td>W2: Suspended shipment of Qinghua 20; Laobafen 10</td><td></td></tr><tr><td>2025</td><td>Jan</td><td></td><td>W2: Suspended shipment of 8th Common Wuliangye since Jan 9</td><td></td><td>W3: Online Shipment suspension for Sky and Ocean Blue since Jan 17 2025</td><td></td><td></td></tr><tr><td>2024</td><td>Dec</td><td></td><td></td><td></td><td></td><td></td><td>W4: Launched Zodiac Spirits for the Snake year:at::RSP of::Rmb1,299/bottle</td></tr><tr><td>2024</td><td>Nov</td><td>W1: Suspended shipment from distributors to retail terminals of all SKUs in some regions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2024</td><td>Aug</td><td></td><td></td><td></td><td></td><td>W4: Launched new super premium::products..&quot;Master&quot;:series on Aug 21</td><td></td></tr><tr><td>2024</td><td>Jul</td><td>W1: Suspended shipment of Moutai 1935 from Jul 2</td><td></td><td>W1: Hiked the within-quota price of 38C Guojiao 1573 by Rmb30 per bottle effective from Jul 2; Laojiao distribution company suspended order-taking and shipment of 52C Laojiao effective from Jul 3</td><td></td><td></td><td></td></tr><tr><td>2024</td><td>Jun</td><td>W1: Asked distributors to split prepayment to two times for June (3%-4% of annual); Suspended direct sales of Feitian to enterprises at Rmb1,499 in some regions and suspended evaluation of qualifying enterprises W2/W3: Ceased &quot;open case&quot; policy of Feitian::Moutai and distribution of Feitian in large cases, Controlled shipment quota for June; Suspended 375ml Feitian::on Xunfeng; Suspended shipments of 15-year and Jingpin::Moutai; Communicated with distributors to control wholesale prices above Rmb2,400; Requested supply suspension::on channels of::Guizhou distributors</td><td></td><td>W4: Ceased the order-taking and shipment of 38° Guojiao 1573 since Jun 28</td><td></td><td>W1: Hiked the ex-factory price of Laobafen series by Rmb5/bottle, effective since Jun 20</td><td></td></tr><tr><td>2024</td><td>May</td><td></td><td>W2: Launched 45% common Wuliangye in 1st-batch 52 cities with ex-If suggested retail price at Rmb839/1,199</td><td></td><td></td><td></td><td></td></tr><tr><td>2024</td><td>Apr</td><td></td><td></td><td>W1: Hiked the outside quota price of Touqu by Rmb14 per bottle, effective immediately</td><td>W1: Hiked the ex-factory price of M6+ by Rmb20 per bottle, effective from:-Apr&#x27; 1st 2024</td><td></td><td></td></tr><tr><td>2024</td><td>Mar</td><td></td><td>W1: Launched new retail sales platform; hiked the Jianzhuang Large glass bottle ex-factory price by 12%</td><td></td><td></td><td></td><td></td></tr><tr><td>2024</td><td>Feb</td><td></td><td>W4: Guided the wholesale price of the 8th Common Wuliangye::and 1618 to not lower than Rmb970/bottle, retail price to not lower than::Rmb1,000 per bottle (&gt;Rmb1,020 in featured stores, &gt;Rmb1,059 in KA malla); targets to maintain the wholesale price of Common Wuliangye and 1618 at not lower than Rmb1,000/1,020 per bottle by Dragon Boat Festival/Mid-Autumn Festival</td><td></td><td></td><td>W4: The presale price of Qinghua 20 will be raised by Rmb20 to Rmb448 from Rmb428 per bottle, effective::on March 20..Some regional distributors also commented that the presale price of Laobafen::is also to be raised by Rmb10 per bottle.</td><td></td></tr><tr><td>2024</td><td>Jan</td><td></td><td>W4: Wuliangye communicated with distributors to hike the ex-factory price by Rmb50 to Rmb1,019 for 8th Common Wuliangye starting from 5 Feb 2024, and prices of other SKUs with different size will increase accordingly</td><td></td><td></td><td></td><td></td></tr></table>

Source: Yunjiu Toutiao, Jiuyejia, Company reports, Data compiled by GS Global Investment Research

Exhibit 8: 2024-2025 channel policy and product launch summary of key spirits companies - Part II

<table><tr><td>Year</td><td>Month</td><td>Anhui Gujing (000596.SZ)</td><td>Sichuan Swellfun (600779.SS)</td><td>Jiugui Liquor (000799.SZ)</td><td>King&#x27;s Luck (603369.SS)</td><td>ZJLD (6979.HK)</td><td>Shede Spirits (600702.SS)Not Covered</td></tr><tr><td>2025</td><td>Feb</td><td colspan="2"></td><td>W3: Jiugui suspended order taking for 52°/42° 500ml Jiugui Spirits (transparent packaging)</td><td>W1: King&#x27;s Luck has ceased accepting orders for Guoyuan 4K/2K</td><td colspan="2"></td></tr><tr><td>2025</td><td>Jan</td><td colspan="6"></td></tr><tr><td>2024</td><td>Dec</td><td colspan="4"></td><td>W2: ZJLD launched fourth-gen Zhen 15</td><td></td></tr><tr><td>2024</td><td>Nov</td><td colspan="3"></td><td>W3: King&#x27;s Luck launched 3 new SKUs for Planet□Large-bottle series named &quot;Grand moon&quot;/&quot;Grand Earth&quot;/&quot;Grand Sun&quot; (42%, 700ml) at□RSP of Rmb168/388/268 per bottle.</td><td colspan="2"></td></tr><tr><td>2024</td><td>Oct</td><td></td><td>W1: Raised price of Zhenniang series 52° 500ml by Rmb10 per bottle, effective since Oct 1; W3: suspended order taking of Zhenniang No.8 38c/42c/52c</td><td colspan="4"></td></tr><tr><td>2024</td><td>Aug-Sep</td><td colspan="6"></td></tr><tr><td>2024</td><td>July</td><td></td><td>W2: Adjusted suggested retail prices for Zhenniang No.8; price of 52-degree SKU up by Rmb20 per bottle, and that of 42/38-degree up by Rmb10 per bottle to□Rmb578/538/528 respectively. effective since Jun 20</td><td colspan=

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
