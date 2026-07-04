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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化。汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
July 1, 2026 10:00 AM GMT

US Rates Strategy | North America

# Buy 10y TIPS with Payer Protection

10 year TIPS appear attractive to us at current levels. A potentially lower Fed policy trough rate, continued downside surprises in CPI prints, and a normalizing core CPI-core PCE wedge can act in favor of this trade. Beta weighted breakevens near lows suggest TIPS are cheap versus nominals.

## Key Takeaways

10y TIPS offer attractive risk/reward, as real yields are near high end of its range and current Fed pricing looks hawkish versus our economists' outlook.

5y5y and 2y3y CPI swap forwards have moved alongside lower oil prices, signaling confidence in the Fed's price stability mandate

Core CPI ex-airfares and hotels continues to cool. Eight of the past 12 headline CPI prints surprising to the downside also signal a cooling inflation trend.

Beta-weighted breakevens are near range lows, implying TIPS look cheap versus nominal Treasuries. Long 10y TIPS also has a positive carry.

The upcoming payrolls print is a risk to the trade, and investors can partially hedge their portfolios by owning a 1m10y payer swaption.

MS & CO. LLC

Aryaman@morganstanley.com +1 212 761-1993

Shaun Zhou
Strategist
Shaun.Zhou@morganstanley.com +1 212 761-3348

Strategist
Matthew.Hornbach@morganstanley.com +1 212 761-1837

Martin W Tobias, CFA
Strategist
Martin.Tobias@morganstanley.com +1 212 761-6076

Strategist
Eli.Carter@morganstanley.com +1 212 761-4703

# Inflation Linked Bonds

## United States | Buy 10y TIPS at attractive levels

<table><tr><td rowspan="10">MS &amp; CO. LLC</td><td>Aryaman Singh</td><td rowspan="2">+1 212 761-1993</td></tr><tr><td>Aryaman@morganstanley.com</td></tr><tr><td>Shaun Zhou</td><td></td></tr><tr><td>Shaun.Zhou@morganstanley.com</td><td>+1 212 761-3348</td></tr><tr><td>Matthew Hornbach, CMT</td><td rowspan="2">+1 212 761-1863</td></tr><tr><td>Matthew.Hornbach@morganstanley.com</td></tr><tr><td>Martin Tobias, CFA, CMT</td><td rowspan="2">+1 212 761-6076</td></tr><tr><td>Martin.Tobias@morganstanley.com</td></tr><tr><td>Eli Carter</td><td rowspan="2">+1 212 761-4703</td></tr><tr><td>Eli.Carter@morganstanley.com</td></tr></table>

With the US-Iran MOU now in place, inflation forwards have moved lower as oil prices have declined over the past few weeks. This shows that investors trust the Fed's ability to maintain price stability over the longer horizon. 5y5y and 2y3y CPI swaps are near levels when we had cuts priced in February 2026 (Exhibit 1).

Brent is now below \$80/bbl and our strategists have lowered their forecasts for the coming quarters. Despite normalized oil prices, Fed's pricing of trough rate is still at 3.6% (MSTRUFUS Index on Bloomberg), around 75bp higher than it was three months ago. With this rise in trough rate, real yields across the curve have moved higher (Exhibit 2).

This move can be attributed to a perceived hawkish stance from the Fed, continued upside surprises in past three payroll prints and a wide core PCE - core CPI wedge. On a year-over-year basis, core CPI fixings also seem elevated, with part of the move pointing to a growth-related inflation premium being priced in.

On the other hand, the previous eight out of 12 headline CPI prints have surprised to the downside as the underlying trend in inflation seems to be cooling versus expectations. Our economists' forecast moderating inflation over the coming months with core CPI at 2.4% Y/Y by May 2027 and our NFP forecasts for June is at 90k below consensus at 115k.

We suggest investors buy 10 year TIPS at current levels based on the following reasons:

1. 10-year real yields are near high end of its range. If two cuts based on our economists' forecasts realize, trough rate can move lower taking 10y TIPS yield lower with it.

2. Inflation is on a cooling trend and continues to surprise to the downside. The burden of proof is on upcoming prints to show a hot print.

3. Our economists note that methodology changes to PCE prices are forthcoming and if applied retroactively, they might lower core PCE y/y inflation up to 20bp.

4. Recent decline in Treasuries was led by breakevens. Beta weighted breakevens near lows imply that TIPS are cheap versus nominals.

5. The carry profile for this trade is positive in the direction of long.

The upcoming payrolls and CPI prints for June are risks to the trade and investors can hedge this risk by owning 1m10y payer swaption along with 10 year TIPS.

Exhibit 1: CPI swap forwards signal Fed credibility is established  
![](images/0276f17ae1301abc62bd9546f5312bc8275fb5a8c71950244fd964da1ad52a51.jpg)  
Source: MS, Bloomberg

Exhibit 2: 10 year real yields near higher end of the range and moves with Fed policy terminal rate  
![](images/8b71c13738f472b5e415204506868bbbf3d463393e0345d73ac4baa74131fe87.jpg)

10 year real yields show 51% R-squared if regressed over weekly changes on Fed policy terminal rate for the past five years rate. Essentially a lower 10 year real yields is a view on market pricing a dovish Fed policy than what is currently priced in.

From a relative value perspective, beta weighted breakevens help us identify if TIPS are rich or cheap versus nominals. TIPS beta is defined as the slope when real yields are regressed on nominal yields. The beta on 10-year real yield changes versus 10-year Treasuries for the past 10 years of data is \~ 0.7 to 0.8. In other words, under normal trading conditions, a +1bp move in nominals results in a +0.75 bp move in RY, and thus a 0.25bp widening in breakevens.

Beta-weighted 10 year breakevens defined as beta times 10 year nominals minus 10 year real yields is near range lows, indicating that TIPS have cheapened versus nominal Treasuries after adjusting for their historical relationship (Exhibit 3). If beta weighted breakevens revert and move higher from current levels, TIPS can outperform Treasuries. We have shown before that if volatility moves higher, beta weighted breakevens tend to mean revert from extreme levels.

Exhibit 3: Beta weighted breakevens near range lows  
![](images/8e9fa71bbe388e0c468dbde5b9d6e665cf15274db405701f9b07aa39ae09be72.jpg)  
Source: MS, Bloomberg

Exhibit 4: New BEA methodology may help normalize this wedge  
![](images/19a6fc53cfaa973076d24fb38636b9cb2f3719518e9eec74b582b73145cbf6e5.jpg)  
Source: MS, Bloomberg

Fed's inflation target is PCE and a core PCE has moved higher versus core CPI, opposite to its usual trend (Exhibit 4). The core PCE/core CPI wedge is pushed wider by components like memory, software and categories like healthcare and financial-services which carry larger weights in PCE than in CPI. Our economists have this wedge normalizing for future months. A normalizing CPI-PCE wedge should act in favor of rate cuts.

Investors can track 1m TIPS carry for 10 year TIPS on Bloomberg using MST1001C Index which is currently at 5.8bp making this trade attractive from a carry perspective (Exhibit 5).

Headline CPI fixings are at 1.8% for May 2027 aided lower by negative energy commodities component of the CPI basket whereas core CPI fixings is at 2.9%, up 15bp in past two weeks (Exhibit 6). Core CPI fixings further out the curve depend on the market perception of inflation expectations and the strength in the economy. We have observed that year over year core CPI curve peak is susceptible to moves in the range of 60bp in a period of a month during the conflict (see here and here).

Exhibit 5: 1 month Carry for long 10 year TIPS is positive  
![](images/7f7c232896bc451cbe623fa749413caa1f2f412aae16996130cf41b5d3484730.jpg)  
Source: MS, Bloomberg

Exhibit 6: Realised and fixings implied CPI  
![](images/e5cec13a1124c112341ac025753276be039a617c5a2206f27c79ac1cd81c693f.jpg)  
Source: MS, Bloomberg

We enter 10 year TIPS at 2.21% with a target of 1.8% and a stop of 2.35%. Investors can partial hedge their portfolio by owning a payer swaption keeping in mind upcoming NFP and CPI prints.

## 1m10y payer swaption to hedge the trade for near term risk events

NFP releases are inherently volatile and difficult to forecast and are a near term risk to this trade. If payrolls print above our economists' expectations, the market could interpret the result as a continuation of past upside surprises signalling underlying strength in the economy. Investors looking to hedge against this risk may consider buying 1m10y payer swaptions.

In a recent note, we argued that Warsh's proposed communication framework would increase the market's sensitivity to economic data surprises. However, the volatility market has yet to reprice this thesis, with 1m10y implied volatility still trading near the lower end of its recent range (Exhibit 7). This week's NFP release will provide the first meaningful test of whether market sensitivity to a Tier 1 macroeconomic data release has indeed increased.

Currently a 1m10y ATM payer costs 63c, implying that the underlying 10y rate needs to move up by 7.7bps for this payer to break-even at expiry (Exhibit 8).

Exhibit 7: Historical 1m10y implied vol  
![](images/3e89fa42bd77150be61693b085940d3f9f4452565d08959068a703441981a291.jpg)  
Source: MS, Bloomberg

Exhibit 8: 10y SOFR rate and terminal breakeven for a 1m10y ATM payer  
![](images/5f0418761375605abc1ead1a2e201d9c6b991aa20c0dd235e261d11432b86450.jpg)  
Source: MS, Bloomberg

• Trade idea: Enter long 10 year TIPS at 2.22% with a target at 1.8% and a stop at 2.35%

## Valuation Methodology and Risks

Below you will find a list of our current trade ideas, entry levels, entry dates, rationales, and risks.

Exhibit 9: Trade table

<table><tr><td colspan="5">Inflation-Linked Bonds</td></tr><tr><td>TRADE</td><td>ENTRY LEVEL</td><td>ENTRY DATE</td><td>RATIONALE</td><td>RISKS</td></tr><tr><td>Buy 10 year TIPS</td><td>2.22%</td><td>7/1/2026</td><td>10y TIPS offer attractive risk/reward, as real yields are near high end of its range and current Fed pricing looks hawkish versus our economists&#x27; outlook. Beta-weighted breakevens near lows suggest TIPS are cheap versus nominals. It also has a positive 1m carry.</td><td>An upside surprise in NFP and CPI prints</td></tr></table>

Source: MS

## Global Macro Strategy Team

<table><tr><td>MS &amp; CO. LLC</td><td>Matthew Hornbach, CMT Matthew.Hornbach@morganstanley.com</td><td>Global Head of Macro Strategy</td><td>+1 212 761-1837</td></tr><tr><td rowspan="4"></td><td>Martin Tobias, CFA, CMT</td><td>US Rates Strategist</td><td>+1 212 761-6076</td></tr><tr><td>Shaun Zhou</td><td>US Rates Strategist</td><td>+1 212 761-3348</td></tr><tr><td>Aryaman Singh</td><td>US Rates Strategist</td><td>+1 212 761-1993</td></tr><tr><td>Eli Carter</td><td>US Rates Strategist</td><td>+1 212 761-4703</td></tr><tr><td rowspan="2">MS &amp; CO. LLC</td><td>Andrew Watrous</td><td>G10 FX Strategist</td><td>+1 212 761-5287</td></tr><tr><td>Molly Nickolin</td><td>G10 FX Strategist</td><td>+1 212 761-3592</td></tr><tr><td rowspan="4"></td><td>Simon Waever Simon.Waever@morganstanley.com</td><td>Head of EM Sovereign Credit and Latin America Fixed Income Strategy</td><td>+1 212 296-8101</td></tr><tr><td>Ioana Zamfir</td><td>Latin America Macro Strategist</td><td>+1 212 761-4012</td></tr><tr><td>Emma Cerda</td><td>Latin America Sovereign Credit</td><td>+1 212 761-2344</td></tr><tr><td>Sofia Palacios</td><td>Latin America Macro Strategist</td><td>+1 212 761-0428</td></tr><tr><td>MS &amp; CO. INTERNATIONAL PLC</td><td>James K. Lord James.Lord@morganstanley.com</td><td>Global Head of FXEM Strategy</td><td>+44 20 7677-3254</td></tr><tr><td rowspan="3"></td><td>Gianluca Salford Luca.Salford@morganstanley.com</td><td>Head of European Rates Strategy</td><td>+44 20 7677-1337</td></tr><tr><td>Fabio Bassanin, CFA</td><td>UK Rates Strategist</td><td>+44 20 7425-1869</td></tr><tr><td>Maria Chiara Russo</td><td>Euro Area Rates Strategist</td><td>+44 20 7425-3499</td></tr><tr><td></td><td>David S. Adams, CFA David.S.Adams@morganstanley.com</td><td>Head of G10 FX Strategy</td><td>+44 20 7425-3518</td></tr><tr><td rowspan="2"></td><td>Neville Mandimika</td><td>CEEMEA Sovereign Credit Strategist</td><td>+44 20 7425-2509</td></tr><tr><td>Arnav Gupta</td><td>CEEMEA Rates Strategist</td><td>+44 20 7677-0382</td></tr><tr><td>MS ASIA LIMITED+</td><td>Gek Teng Khoo</td><td>AXJ Macro Strategist</td><td>+852 3963-0303</td></tr><tr><td rowspan="2">MS MUFG SECURITIES CO., LTD.</td><td>Koichi Sugisaki Koichi.Sugisaki@morganstanleymufg.com</td><td>Head of Japan Macro Strategy</td><td>+81 3 6836-8428</td></tr><tr><td>Hiromu Uezato</td><td>Japan Macro Strategist</td><td>+81 3 6836-8431</td></tr></table>

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Eli P Carter, Matthew Hornbach; Aryaman Singh; Martin W Tobias, CFA; Shaun Zhou.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from United States of America.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: United States of America.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

## (as of June 30, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><

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
