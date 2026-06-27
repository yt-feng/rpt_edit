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
- 已识别机构名：`Bernstein`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Weekend Healthcare Pulse: Deadtech forever? Can Medtech recover?

Lee Hambright +1 917 344 8429 lee.hambright@bernsteinsg.com

Courtney Breen +1 917 344 8407 courtney.breen@bernsteinsg.com

Nandan Kulkarni +91 22 6842 1436 nandan.kulkarni@bernsteinsg.com

Delphine Le Louet +33 1 42 13 92 93 delphine.le-louet@bernsteinsg.com

Rebecca Liang, Ph.D. +852 2123 2656 rebecca.liang@bernsteinsg.com

Susannah Ludwig +41 582 723 127 susannah.ludwig@bernsteinsg.com

William Pickering, MD +1 917 344 8340 william.pickering@bernsteinsg.com

Justin Smith +44 20 7762 5899 justin.smith@bernsteinsg.com

Miki Sogi, Ph.D. +81 3 6777 6991 miki.sogi@bernsteinsg.com

Lance Wilkes +1 917 344 8501 lance.wilkes@bernsteinsg.com

Jeffrey Walch, MD, Ph.D. +1 917 344 8613 jeffrey.walch@bernsteinsg.com

## Specialist Sales

Christian Moore +1 917 344 8555 christian.moore@bernsteinsg.com

U.S. Medtech stock performance has been abysmal. Our coverage has underperformed the S&P by 4600bps over the past year (Exhibit 1), and the medtech sector multiple has compressed by $30\%$ since November (Exhibit 2). While investors worry about several macro factors (slowing utilization, margin pressure, GLP-1 impact), we believe medtech weakness is more about single-stock stories that have gotten more complicated. In today's note, we reflect on some of the complications that have crept into medtech stock stories. Medtech fundamentals remain solid, in our view, and per Exhibit 4, valuations have come in dramatically for most of our coverage. For investors who are willing to live with stories that have a bit of hair on them, we see very attractive risk/reward for many quality medtech names across our coverage.

\- By Lee Hambright and Adam Chow

EXHIBIT 1: Over the last 12 months, U.S. Medtech has underperformed the S&P (by 4600bps!) and has lagged all other healthcare subsectors  
US Healthcare Stock Performance  
![](images/d7f019005b12cc054c6d738bf7d96ccab8ae7baa7856a461d321b43902d4b3ec.jpg)  
Equal weight based on Bernstein large-cap US coverage by sector; US Medtech includes ABT, BSX, DXCM, EW, ISRG, MDT, PODD, SYK, ZBH Source: Bloomberg; Bernstein analysis (25-Jun-2026 close)

U.S. Medtech stock performance has been horrendous. Over the last year, U.S. Medtech has underperformed the S&P 500 by just under 5000 bps (see Exhibit 1), making it the worst subsector within healthcare by a wide margin. The P/E multiple for the sector has been slashed by 30% over the last \~6 months (see Exhibit 2). Within our coverage, most stocks are down significantly year to date, with BSX and PODD as the most notable underperformers (Exhibit 3).

EXHIBIT 2: U.S. Medtech P/E multiples are down $30\%$ since November 2025. We haven't seen these levels sustainably since before 2017  
U.S. Medtech (S5HCEP\*) Price/Earnings Ratio (1BF)  
![](images/6b4da61d4c67bd30850e2abf147e55439ce36ad2982316b791aeb75668d1bbfe.jpg)  
Source: Bloomberg (S&P 500 Health Care Equipment Index; cap-weighted average of ABT, BAX, BDX, BSX, DXCM, EW, GEHC, IDXX, ISRG, MDT, PODD, RMD, STE, SYK, ZBH)

EXHIBIT 3: Year to date, BSX and PODD have been the worst performers in our coverage  
U.S. Medical Devices Stock performance; 2026 YTD  
![](images/133b2d5599e8ab65fbbb52bea38b454def786cfe3690abe7611cf85830b7c757.jpg)  
Source: Bloomberg; Bernstein analysis (25-Jun-2026 close)

## HOW DID WE GET HERE?

What's driving this weakness for medtech stocks? What has changed? As medtech multiples plunge to 10-year lows, investors have been questioning whether something is fundamentally wrong with the sector. Could procedure growth be slowing down? Will inflation (e.g., oil, resins, memory/semiconductors) put pressure on margins? Could GLP-1 growth disrupt medtech markets?

These are all red herrings, in our view. We see nothing wrong with medtech fundamentals. The problem for medtech, in our view, is more about stories. As investors remain captivated by AI-related stories, the stories for historically strong medtech stocks have gotten increasingly complicated. And in a world where a narrow set of AI winners are driving incredibly strong returns, investors have very little patience for complicated medtech stories.

## INCREASINGLY COMPLICATED STORIES

Stories have become increasingly complicated for many medtech stocks. Boston Scientific (BSX) has had a particularly dramatic fall from grace, and we attribute a fair amount of sector weakness to BSX's collapse. But sadly, BSX is not alone. Below, we summarize several medtech stock stories that have grown increasingly complicated over the past year.

Boston Scientific (BSX). BSX's P/E multiple has been slashed from a high of over 36x in early 2025 to 12.5x today. After establishing itself as a reliable high-single-digit grower, BSX's organic growth shot up to 16% (!) in both 2024 and 2025, driven primarily by two key franchises: Farapulse (PFA) and Watchman (LAAC). Watchman revenue doubled from \~\$1bn in 2022 to \~\$2bn in 2025, and Farapulse drove BSX's EP business to quadruple from \$800mn in 2023 to \$3.3bn in 2025. After CMS reimbursement coding for concomitant Farapulse+Watchman procedures went live Oct 2024, concomitant procedures drove Watchman organic growth from 18% in 3Q24 to a peak of 35% in 3Q25. Investor concerns about PFA competition started to percolate during the course of 2025 as BSX EP growth began to decelerate. Then in 4Q25, BSX U.S. EP sales missed consensus by 6%, and Watchman organic growth inflected from its peak of 35% to 29%. Both franchises continued to decelerate in 1Q26 and Urology growth was weak on Axonics integration hiccups, leading to a dramatic guidance cut after Q1, where FY26 organic growth was cut from 10%-11% to 6.5%-8.0% (see our 1Q26 recap). It was a gutsy move for management to cut the FY26 guide after one quarter of a new 12-quarter long-range plan (for 10%+ organic growth) issued in Sep 2025. Just 5 weeks after the 1Q26 call, BSX lowered Watchman expectations again at our Bernstein Strategic Decisions Conference (see our BSX SDC recap). Additional complications to the story include a couple of controversial deals: the \$14.5bn Penumbra acquisition in January (larger than the typical tuck-in deals to which investors have become accustomed) and the \$1.5bn MiRus investment in May (which triggered investor skepticism given BSX's two previous high-profile failures in TAVR).

Abbott (ABT). In 4Q25, sales growth slowed to $3.0\%$ organic (a $3\%$ miss), driven largely by an unexpected $9\%$ decline in ABT's Nutrition business (missed by $12\%$ ) (see our 4Q25 recap). The decline was driven by price cuts (primarily in the Adult segment) and infant formula market share losses stemming from the loss of a large WIC contract in 3Q25. Abbott had been raising Nutrition prices since 2022 in an attempt to offset higher manufacturing costs, but those increases began to weigh on volume. Management took price down in the quarter to address this and guided the Nutrition business to a challenged 1H26 with a return to growth in 2H26. The story did not get any cleaner in 1Q26, as sales ex-Exact acquisition and other adjustments continued growing slowly at \~3.0% organic. ABT's continuous glucose monitor (CGM) sales continued to decelerate (on market weakness + ABT recall in 4Q25) and the company's Structural Heart division lost market share (see our 1Q26 recap). ABT has dropped \~26% YTD.

Stryker (SYK) suffered a cyberattack on March 11 which disrupted global operations. Although the company primed investors for disappointing Q1 results through a series of 8-Ks, the disruption impacted Q1 sales more heavily than expected. Organic growth landed at 2.4% in 1Q26, 5% short of consensus, as the cyberattack delayed revenue recognition and disrupted manufacturing and supply chain operations. Management reiterated FY26 guidance on revenue-recognition tailwinds and backlog recovery on capital equipment. However, some investors remained concerned that the severity of the disruption could make guidance difficult to achieve, particularly now that 2H26 expectations call for 11% organic growth (see our 1Q26 recap). SYK has dropped \~10% YTD.

Insulet (PODD) has been a popular short since the company's November 2025 investor day, as investors worry about competitive patch pumps and potential price pressure in the pharmacy channel. PODD shares came under more pressure when the company announced a voluntary medical device correction on March 12 (see 8-K), identifying a manufacturing issue whereby certain pods from specific lots may have a small tear in the internal tubing that delivers insulin. The issue can lead to insulin leaking inside the pod rather than being fully infused in the body. At the time, Insulet had received 18 reports of serious adverse events associated with high blood glucose levels, including hospitalization and diabetic ketoacidosis (DKA), and no deaths had been reported. The company informed users about affected lots (pods involved amounted to \~1.5% of annual Omnipod 5 production globally) and offered replacement pods at no cost to users. On April 10, PODD confirmed 11 additional adverse events (bringing the total to 29) and no deaths associated with the manufacturing issue. On April 29, the FDA mischaracterized the manufacturing issue as having resulted in "476 serious injuries and no deaths," further hitting the stock by -12.5% on the day (see our thoughts on the March 12 recall and follow-ups). On May 26, the company announced a separate voluntary medical device correction, identifying a manufacturing issue that resulted in 24 reports of serious adverse events (no deaths) and affected \~8.5% of 2025 Omnipod 5 production. PODD has fallen \~46% YTD.

Medline (MDLN) reported strong revenue growth results in their first full quarter after their IPO, but adj EBITDA of \$776mn missed consensus (\$784mn) by 1% (see our 1Q26 recap). Management explained that the team had decided to accelerate investments in the business given strong revenue performance, but the small

EBITDA miss carried outsize weight given market expectations that companies should execute cleanly in their first full quarter as a public company, and MDLN shares plunged by 12% before settling at -7.3% on the day. An FDA recall on April 17, FDA warning letter on May 28, news of a fire destroying a California distribution center on June 12, and general concerns about oil prices and sponsors selling down their positions have also put pressure on the name. MDLN has dropped \~10% YTD.

Medtronic (MDT) was the top-performer in medtech in 2025, but the story has become a bit more complicated this year. Disappointing long-term data released in February was a setback for MDT's TAVR business, and the March IPO of MiniMed (MMED, not covered) fell short of the company's expectations. FY27 is a high-stakes year for MDT, as the company needs to capitalize on several high-profile launches including Affera, RDN, Altaviva, and Hugo. After weaker EPS growth over the past 4 years (-5%, -2%, +6%, +1%), MDT needs to pull it all together in FY27 and deliver real EPS growth. MDT has fallen \~16% YTD.

Intuitive Surgical (ISRG) continues to deliver strong financial performance, with 1Q26 sales growth of 23% and EPS growth of 38%, both strong beats vs. consensus (see our 1Q26 recap). Forward estimates continue to move up, but the multiple has been dragged down by weakness across the medtech sector. When BSX was trading at a 35x P/E multiple, investors didn't mind paying 70x or more for ISRG. But with BSX at 12.5x, some investors worry that ISRG looks expensive at 36x. Fundamentals have been strong, but as the share price has struggled, investors ponder questions about the durability of procedure growth, remanufactured instruments, Chinese competitors, and new systems from MDT and JNJ. ISRG is down \~29% YTD.

## IS THERE SOMETHING WRONG WITH MEDTECH FUNDAMENTALS?

With such notable, sustained weakness across the majority of stocks in the medtech sector, investors have understandably wondered whether there's something fundamentally wrong with the space. Several thematic factors have been teed up as possible explanations for sector weakness. As we noted above, we believe these are all red herrings. We believe the problem is more about single stock stories getting more complicated across the group. We discuss a few of these thematic factors below.

Slowing utilization growth. Hospital utilization has been strong for some time, and investors worry utilization growth could slow at some point, perhaps driven in part by some people getting kicked off insurance (ACA exchanges and Medicaid) and losing access to certain procedures. Some large hospital systems have speculated that utilization growth may begin to decelerate in 2H26. Medtech companies have told a different story, with teams fairly unanimously reporting continued strength in underlying procedure growth despite some mostly immaterial weather-related impact in 1Q26:

"What I will say in terms of the underlying market is that it's solid and underlying demand is what we expected. Now we did see some procedural softness early in the quarter, but nothing that we would define really as material. While certain regions, particularly here in the U.S., you will recall we experienced some periods of severe weather in late January and early February, that was largely consistent with normal seasonal patterns" - JNJ 1Q26 call

"Turning to the environment, underlying demand across our businesses remained healthy in Q1, even as the cyber incident created operational disruption. Procedural volumes were solid, supported by favorable demographics and the continued adoption of robotic assisted surgery. The hospital CapEx environment also remains steady, and our capital order book remains elevated as we enter the remainder of the year." - SYK 1Q26 call

Hospitals and MCOs saw a bit of softness in 1Q26 due to a mild flu season and weather-related disruptions, but most are calling for stable growth in utilization overall:

"As we monitor underlying utilization trends, they remain consistent with the high levels we saw in the prior year. At this distance, we anticipate trend to remain at the anticipated levels for 2026." - UNH 1Q26 call

Margin pressures. The Iran conflict led to a period of higher freight costs and created supply chain issues and gross margin concerns (e.g., higher resin prices). Higher input costs for semiconductors and memory has raised concerns as well. Investors remember that medtech stocks did not fare well during inflation concerns in 2022, and they worry inflation could continue to cause problems for the group. So far, medtech companies appear unfazed by these margin pressures:

"As it relates to oil costs, I mean I think that's an impact that it's too early to tell. We're not seeing any of that in our cost right now. We're not seeing freight rates increase from our suppliers right now." - ABT 1Q26 call

"Today, we have seen no material supply disruptions, a minor freight cost increase in the quarter that we're able to absorb. From a supply standpoint, most of our key products are dual-source, if not three sources. We got at least one year of pulling, so this is not something that we're concerned about. So, we're not seeing any distribution challenges there. So, again, so far, life is good." -ZBH 1Q26 call

GLP-1 impact. Growing access to weight loss medications has raised questions about impact on medical device businesses, particularly in certain end markets (e.g., bariatric surgery, diabetes, OSA). We all remember the impact on medtech stocks in 2H23, and though most medtech stocks recovered and have appeared to shrug off GLP-1-related fears, growing access to oral weight loss

drugs could revive concerns.

## WHAT CAN GET MEDTECH GOING AGAIN?

As we explain above, we see nothing wrong with medtech fundamentals. These are quality companies operating in attractive oligopoly markets, medtech innovation continues at a rapid pace, and there are plenty of secular tailwinds that will continue to drive growth. The problem for medtech, in our view, is more about single stock stories that have gotten a bit more complicated over the past year. As long as captivating AI-related stories continue to drive outperformance for a narrow basket of names, it's difficult to get investors interested in medtech stories that have some hair on them. So, where do we go from here? What can get medtech going again?

First off, it certainly wouldn't hurt if a bit of air came out of the AI balloon. Our macro team believes breadth is the story and forecasts a period of rotation/dispersion. We're seeing a bit of that today, and we'd certainly welcome a bit more.

More broadly, we forecast progressive recovery for idiosyncratic risks are retired one by one. Perhaps Stryker can deliver a big Q2 beat and restore confidence that the business will continue strong execution despite the cyberattack-related hiccup. If Abbott can show recovery in Nutrition and stabilization in Structural Heart, investors might start to get excited about broadening access for CGM and the growth opportunity in EP. Perhaps Intuitive Surgical's portfolio of launches (dV5, Ion, SP, XiR, AI) can continue to drive strong quarterly financial performance, and maybe investors will find it harder to ignore ISRG as estimates continue to march higher.

Recovery for Boston Scientific would go a long way to restoring confidence in the group. Questions continue to swirl about decelerating growth for Watchman and EP. As we get clarity on when and where growth rates will bottom out for these key franchises, and as reset LRP expectations begin to come into focus, we see the potential for dramatic recovery over the next 12-24 months.

Per Exhibit 4, valuations have come in dramatically for most of our coverage. For investors who are willing to live with stories that have a bit of hair on them, we see very attractive risk/reward for many quality medtech names across our coverage.

EXHIBIT 4: For most of our coverage, multiples have been slashed by $25\% -60\%$ over the last 18 months U.S. Medtech Valuation History - Absolute P/E and P/S Multiples

<table><tr><td>Ticker:</td><td>SPX</td><td>JNJ</td><td>EW</td><td>ZBH</td><td>MDT</td><td>SYK</td><td>DXCM</td><td>TNDM</td><td>ABT</td><td>ISRG</td><td>BSX</td><td>PODD</td></tr><tr><td>Metric:</td><td>P/E</td><td>P/E</td><td>P/E</td><td>P/E</td><td>P/E</td><td>P/E</td><td>P/S</td><td>P/S</td><td>P/E</td><td>P/E</td><td>P/E</td><td>P/S</td></tr><tr><td>Avg last 10yrs</td><td>19.1x</td><td>16.2x</td><td>32.7x</td><td>15.1x</td><td>17.2x</td><td>24.0x</td><td>10.3x</td><td>5.0x</td><td>22.5x</td><td>48.9x</td><td>24.3x</td><td

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
