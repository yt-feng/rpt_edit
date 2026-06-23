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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Get Ready For the Noisiest US Front End In a Generation

The toolkit the Fed uses determines the rates regime, and 36 years of data say the front end and the shape of the curve, not the level of yields, define it. A return to a short statement, little forward guidance, and a small balance sheet should bring back the noisiest front end in a generation.

## Key Takeaways

The level of yields does not separate the four Chairs in any clean way. Front-end volatility does, and it has fallen with every Chair since Greenspan took over.

Under Greenspan the front end was the curve's engine, a 2-year move pulling the whole curve along. Under Yellen the front end sat still and the long end led.

We measure it directly. Correlation between 2-year moves and slope moves runs negative under Greenspan and positive under Yellen, near-perfect mirror images.

■ Curve-shape volatility tells the same story. Greenspan ran the highest curvature volatility of the four Chairs, and Yellen ran the lowest by a wide margin.

A Greenspan toolkit – short statement, little guidance, small balance sheet – means a noisier front end and a more volatile curve shape, even at a flat level.

Matthew Hornbach

Strategist
Matthew.Hornbach@morganstanley.com +1 212 761-1837

Martin W Tobias, CFA

Strategist
Martin.Tobias@morganstanley.com +1 212 761-6076

Shaun Zhou

Strategist
Shaun.Zhou@morganstanley.com +1 212 761-3348

Strategist
Aryaman@morganstanley.com +1 212 761-1993

Eli P Carter

Eli.Carter@morganstanley.com +1 212 761-4703

# Interest Rate Strategy

MS & CO. LLC

## United States | It's the hammer more so than the carpenter

<table><tr><td colspan="2">Matthew Hornbach, CMT</td></tr><tr><td>Matthew.Hornbach@morganstanley.com</td><td>+1 212 761-1863</td></tr><tr><td colspan="2">Martin Tobias, CFA, CMT</td></tr><tr><td>Martin.Tobias@morganstanley.com</td><td>+1 212 761-6076</td></tr><tr><td colspan="2">Shaun Zhou</td></tr><tr><td>Shaun.Zhou@morganstanley.com</td><td>+1 212 761-6076</td></tr><tr><td colspan="2">Aryaman Singh</td></tr><tr><td>Aryaman@morganstanley.com</td><td>+1 212 761-1993</td></tr><tr><td colspan="2">Eli Carter</td></tr><tr><td>Eli.Carter@morganstanley.com</td><td>+1 212 761-4703</td></tr></table>

## Do Fed Chairs determine the rates regime or the tools they use?

Do different rates regimes march to the beat of different Fed Chairs? We think the toolkit used by the Fed determines rates regimes more so than any other factor. How do we define each regime? Let's start with how not to sort them.

Sorting the last four Fed Chairs (Greenspan, Bernanke, Yellen, Powell) by the level of yields just sorts them by the era they served in. Yields under Greenspan look high because yields in the 1990s were high. Yields under Yellen look low because she ran policy at the zero bound. The level of yields reflects the cycle, not the Chair.

Front-end volatility works far better. We take the 3m yield, measure how much it moves over rolling 63-day windows, and annualize it (Exhibit 1). The data suggest that the front end was noisier under Greenspan, quieted through the crisis, went nearly silent under Yellen, and woke back up under Powell.

Exhibit 1: Front-end volatility: 3m par yield, daily changes, 63-day standard deviation, annualized  
![](images/67228684118e763c7960f2b36ddcff57ed5761b2756776375107811aa4415fcd.jpg)  
Source: MS, Bloomberg  
Exhibit 2: Front-end vs back-end volatility by Fed Chair: 3m yield, 10y yield, period standard deviation

![](images/8a56ab08ab89eec6c70f0e5f9c1789ecb7c1126f0eb7bb299f584f09889f6f26.jpg)  
Source: MS, Bloomberg

The ranking across the four Chairs is stark (Exhibit 2). Front-end volatility falls from roughly 110 basis points (bp) annualized under Greenspan to 21bp under Yellen, then recovers to 60bp under Powell. The long end hardly moves across the four. It sits near 90 to 100bp for everyone except Yellen. The Chairs differ at the front end, not the back.

Consider Yellen's 21bp. A policy rate pinned at zero cannot move, and neither can the front end attached to it. That number reflects the rate environment and the tools she used, not Janet Yellen. The same logic runs in reverse for a Chair who steps back from guidance and lets the front end trade.

## Under Greenspan, the front end drove the whole curve

This is the part that matters most for the Warsh question. In some regimes, the front end leads and the rest of the curve follows. In others the front end sits anchored and the long end moves the curve around it. We can tell which regime we are in.

We take the daily change in the 2y yield and the daily change in the 2s10s curve slope, and ask whether they move together (see Exhibit 3). When the front end drives, a 2y selloff flattens the curve, so the two move in opposite directions and the correlation turns negative. When guidance pins the front end, the long end sets the slope, and the correlation turns positive.

The readings line up with the toolkit. Greenspan averages about -0.28. The front end led. Yellen averages about +0.29. The long end led while the front end sat at zero. Powell sits at -0.13, partway back toward the Greenspan pattern. Bernanke sits near zero, the handoff between the two worlds.

Exhibit 4 makes the same point another way. We compare how much the front of the curve moves against how much the whole curve moves, over rolling one-year windows. Under Greenspan the front end accounted for about $90\%$ of the curve's variation. Under Yellen it accounted for roughly $10\%$ .

Exhibit 3: Correlation between daily changes in 2y yields and the 2s10s yield curve shape  
![](images/9f721d51e9819368b5f3458081f23586e97734e18631a456049a32cdea12818a.jpg)  
Source: MS, Bloomberg

Exhibit 4: Front-end share of yield curve variance: average daily change of 1m-2y yields vs. 1m-30y  
![](images/542dffa227d379c73811e8beb684e3d585b9a84481731fbfcdf8430a823ed310.jpg)  
Source: MS, Bloomberg

Readings above 100% mean the front end moved more than the curve as a whole. Put differently, the front end was the curve under Greenspan and barely mattered to it under Yellen.

## Less guidance means a more volatile curve shape

A Chair who guides less hands more of the work back to the market. That uncertainty does not stay in the front end. It moves out along the curve and shows up in the shape. A step back toward the Greenspan toolkit should therefore lift the volatility of the slope and the curvature, not only the level.

The data already shows it. We measure how much the slope moves over rolling 63-day windows and annualize it (see Exhibit 5). We do the same for curvature, the 2s10s30s butterfly, a standard gauge of how bowed the curve sits (see Exhibit 6).

Curvature gives the cleaner read. Greenspan ran the highest curvature volatility of the four Chairs at about 80bp. Yellen ran the lowest at about 44bp. Powell sits in between near 52bp. The forward-guidance era did not only calm the front end; it pressed down on the whole shape of the curve.

Investors underappreciate this part of the story. Most watch front-end volatility. Fewer watch the volatility of the curve's shape. If the next Chair guides less, both rise together, and we suspect the move in curve shape catches the most investors offside.

Exhibit 5: Yield curve slope volatility: 2s10s curve, daily changes, 63-day standard deviation, annualized  
![](images/d71ce264a187900a49de1270d5b81a01fad47ba66ba5546142b366f1802cfd8e.jpg)  
Source: MS, Bloomberg

Exhibit 6: Yield curve curvature volatility: 2s10s30s butterfly, daily changes, 63-day standard deviation, annualized  
![](images/71e996a19d3d4e034ce39e3452ec5b6018c3b35377a0bc9c337c4d225b5f12e3.jpg)  
Source: MS, Bloomberg

## What a return to the Greenspan toolkit would look like

Front-end volatility and curve-shape volatility move together. When the front end is more volatile, so is the shape of the curve (Exhibit 7). The Greenspan months sit to the upper right, high on both measures. The Yellen months sit to the lower left, low on both. Powell sits between them, nearer to Greenspan.

The scorecard ranks all four Chairs on the three volatility measures at once (Exhibit 8). Greenspan ranks high across front-end, slope, and curvature volatility. Yellen ranks low across all three. Bernanke and Powell land in the middle, with the crisis and its aftermath lifting Bernanke's slope volatility.

A Chair who runs policy the way Greenspan did, i.e., a short statement, little forward guidance, a small balance sheet, would not necessarily change the level of yields. The economy sets the level. What changes is the behavior of the curve. The front end moves more. The slope and curvature move more. The market takes back the work that guidance has done since 2009.

That is the regime shift to watch for. Not a new level for yields, but a front end and a curve shape that move the way they did before guidance took over.

Exhibit 7: Front-end vol vs. curve slope vol: 3m vs. 2s10s curve  
![](images/540ac84aaec461a1affdeec88860cd17f1e6b90faa63817df0e7a8aaf494487a.jpg)  
Source: MS, Bloomberg

Exhibit 8: Regime scorecard: three volatility dimensions  
![](images/fac17a26d0de69bbd14d504b1b4c5863a7f7c2f427f7494ec410048366b94743.jpg)  
Source: MS, Bloomberg

## Investment implications

A move back toward the Greenspan toolkit argues for owning curve-shape and front-end volatility rather than fading it, and for less conviction in the tight, range-bound trading that defined the guidance era. If the next Chair guides less, realized volatility in the front end and in curve shape rises from today's compressed levels, and positioning built for a quiet curve carries the most risk.

We would rather own low front-end and curvature volatility here than lean against it. This speaks to the distribution of outcomes, not the level of yields.

\- Trade idea: Maintain SFRZ6M7 curve flatteners at 2bp with a target of -10bp and an initial stop of 20bp.

\- Trade idea: Maintain long 2-year (Sep '27) UST SOFR swap spreads at -9.6bp with a target of -10bp and a trailing stop of -15bp.

## Valuation Methodology and Risks

Below you will find a list of our current trade ideas, entry levels, entry dates, rationales, and risks.

<table><tr><td>Interest Rate Strategy</td><td></td><td></td><td></td><td></td></tr><tr><td>TRADE</td><td>ENTRY LEVEL</td><td>ENTRY DATE</td><td>RATIONALE</td><td>RISKS</td></tr><tr><td>Maintain SFRZ6M7 curve flattener</td><td>10.5bp</td><td>5/22/2026</td><td>We think SFRZ6M7 curve flatteners offer a compelling way to express the view that market pricing places too much weight on hawkish Fed tail risks, in response to the oil shock, and the allure of a AI-driven industrial activity renaissance. This relative value expression allows investors to exploit a substantial insurance premium against rate hikes, removes outright duration beta, while not requiring a near-term dovish pivot by the Fed.</td><td>The main risk is if fiscal stimulus arrives before the mid-term elections, which would justify currently elevated levels of near-term inflation expectations.</td></tr><tr><td>Long 2y (Sep &#x27;27) UST SOFR swap spread</td><td>-21.6</td><td>10/3/2025</td><td>We expect softer funding conditions and a steepening of the very front end to cause swap spreads in the front end to widen given recent relationships.</td><td>Risks to the trade include firmer funding than expected or a stabilizing job market.</td></tr></table>

## Global Macro Strategy Team

<table><tr><td>MS &amp; CO. LLC</td><td>Matthew Hornbach, CMT
Matthew.Hornbach@morganstanley.com</td><td>Global Head of Macro Strategy</td><td>+1 212 761-1837</td></tr><tr><td></td><td>Martin Tobias, CFA, CMT</td><td>US Rates Strategist</td><td>+1 212 761-6076</td></tr><tr><td></td><td>Shaun Zhou</td><td>US Rates Strategist</td><td>+1 212 761-3348</td></tr><tr><td></td><td>Aryaman Singh</td><td>US Rates Strategist</td><td>+1 212 761-1993</td></tr><tr><td></td><td>Eli Carter</td><td>US Rates Strategist</td><td>+1 212 761-4703</td></tr><tr><td rowspan="2">MS &amp; CO. LLC</td><td>Andrew Watrous</td><td>G10 FX Strategist</td><td>+1 212 761-5287</td></tr><tr><td>Molly Nickolin</td><td>G10 FX Strategist</td><td>+1 212 761-3592</td></tr><tr><td></td><td>Simon Waever
Simon.Waever@morganstanley.com</td><td>Head of EM Sovereign Credit and Latin America Fixed Income Strategy</td><td>+1 212 296-8101</td></tr><tr><td></td><td>Ioana Zamfir</td><td>Latin America Macro Strategist</td><td>+1 212 761-4012</td></tr><tr><td></td><td>Emma Cerda</td><td>Latin America Sovereign Credit</td><td>+1 212 761-2344</td></tr><tr><td>MS &amp; CO. INTERNATIONAL PLC</td><td>James K. Lord
James.Lord@morganstanley.com</td><td>Global Head of FXEM Strategy</td><td>+44 20 7677-3254</td></tr><tr><td></td><td>Gianluca Salford
Luca.Salford@morganstanley.com</td><td>Head of European Rates Strategy</td><td>+44 20 7677-1337</td></tr><tr><td></td><td>Fabio Bassanin, CFA</td><td>UK Rates Strategist</td><td>+44 20 7425-1869</td></tr><tr><td></td><td>Maria Chiara Russo</td><td>Euro Area Rates Strategist</td><td>+44 20 7677-3499</td></tr><tr><td></td><td>David S. Adams, CFA
David.S.Adams@morganstanley.com</td><td>Head of G10 FX Strategy</td><td>+44 20 7425-3518</td></tr><tr><td></td><td>Neville Mandimika</td><td>CEEMEA Sovereign Credit Strategist</td><td>+44 20 7425-2509</td></tr><tr><td></td><td>Arnav Gupta</td><td>CEEMEA Rates Strategist</td><td>+44 20 7677-0382</td></tr><tr><td>MS ASIA LIMITED+</td><td>Gek Teng Khoo</td><td>AXJ Macro Strategist</td><td>+852 3963-0303</td></tr><tr><td>MS MUFG SECURITIES CO., LTD.</td><td>Koichi Sugisaki
Koichi.Sugisaki@morganstanleymufg.com</td><td>Head of Japan Macro Strategy</td><td>+81 3 6836-8428</td></tr><tr><td></td><td>Hiromu Uezato</td><td>Japan Macro Strategist</td><td>+81 3 6836-8431</td></tr></table>

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Eli P Carter; Matthew Hornbach; Aryaman Singh; Martin W Tobias, CFA; Shaun Zhou.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from United States of America.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: United States of America.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a st

[中间内容因长度限制已省略]

ce Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Aryaman Singh; Shaun Zhou; Eli P Carter; Matthew Hornbach; Martin W Tobias, CFA.

© 2026 MS
"""
