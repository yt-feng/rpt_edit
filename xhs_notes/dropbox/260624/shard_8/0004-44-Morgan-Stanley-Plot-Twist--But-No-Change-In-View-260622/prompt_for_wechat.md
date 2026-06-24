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
June 22, 2026 05:21 PM GMT

Global EM Strategist

# Plot Twist, But No Change In View

A new Fed doesn't mean a new bear market for EM. We continue to expect EM currencies to rally vs G3, as risk appetite remains strong, lower oil prices are helping and fundamentals & policy are improving. FX strength should help a recovery in bonds through more dovish CB pricing.

## Key Takeaways

■ EM local currency bond yields have not fallen as much as the drop in energy prices might suggest.

\- Higher core rates, a strong USD and continued market pricing for rate hikes at the index level have limited the duration rally.

Some of these headwinds should fade as we generally expect rate cuts from EM over the next 12m, not hikes, and are bullish EM currencies at least vs G3.

■ ZAR and HUF offer opportunities for investors looking to monetise rates risk premia.

EM FX continued to deliver positive total returns in June again G3 and we continue to recommend a diversified funding approach to focus on the value in EM and the uncertainty over the USD cycle.

## Must reads from Global EM Strategy

## Colombia Economics & Strategy Colombia Election Update: A Close Call Validates Base Case | 22-Jun-2026

De la Espriella secured one of the highest vote shares among recent presidents, but the narrow margin underscores the need for a mandate for policy change, rather than a blank check.

Fixed Income Strategy: Bloomberg Ticker Almanac | 18-Jun-2026

This new annual publication details our entire catalogue of data that we host on the Bloomberg Terminal. We provide clients access to time series data requiring complex transformations to make it more readily accessible - this bespoke data is a useful tool to help clients add alpha to their portfolios.

Colombia Fixed Income Strategy & Economics: Trip Takeaways: A Problem For Later | 15-Jun-2026

Markets price in a high probability of a De la Espriella win, consistent with on-the-ground sentiment. Initial announcements and a supportive backdrop could keep sovereign credit spreads supported, although the feasibility of a fiscal adjustment remains unclear in any election outcome.

India Economics & Strategy: Boosting Capital Flows – A Constructive Shift

## MS & CO. INTERNATIONAL PLC+

James K Lord
Strategist
James.Lord@morganstanley.com +44 20 7677-3254

Simon Waever
Strategist
Simon.Waever@morganstanley.com +1 212 296-8101

Ioana Zamfir
Strategist
Ioana.Zamfir@morganstanley.com +1 212 761-4012

Neville Z Mandimika
Strategist
Neville.Mandimika@morganstanley.com +44 20 7425-2509

Arnav Gupta
Strategist
Arnav.Gupta@morganstanley.com +44 20 7677-0382

Gek Teng Khoo
Strategist
Gek.Teng.Khoo@morganstanley.com +852 3963-0303

MS INDIA COMPANY PRIVATE LIMITED+

Nimish M Prabhune
Strategist
Nimish.Prabhune@morganstanley.com +91 22 6996-1862

Please add me to your distribution list.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## | 14-Jun-2026

The coordinated RBI-government package could draw US\$40-60bn of incremental capital inflows, helping keep the BoP in balance in F27. We expect liquidity to remain in surplus and funding conditions to ease. The RBI is likely to hold rates at 5.25%, but upside inflation risks could hasten tightening.

## CEEMEA Macro Strategy: South Africa: 1y1y-2y2y Steepener | 10-Jun-2026

South Africa rates reflect a gap between market pricing (\~75bp hikes) and our lower baseline of one more 25bp hike this year, with risks driven by inflation uncertainty and global rate dynamics. We see front-end steepeners (1y1y–2y2y) as attractive, given asymmetric upside from oil, politics, and FX risks. We remain neutral on USD/ZAR.

<table><tr><td rowspan="2">MS &amp; CO. INTERNATIONAL PLC</td><td>James LordJames.Lord@morganstanley.com</td><td>+44 20 7677-3254</td></tr><tr><td>Arnav GuptaArnav.Gupta@morganstanley.com</td><td>+44 20 7677-0382</td></tr><tr><td rowspan="2">MS &amp; CO. LLC</td><td>Ioana ZamfirIoana.Zamfir@morganstanley.com</td><td>+1 212 761-4012</td></tr><tr><td>Sofia PalaciosSofia.Palacios@morganstanley.com</td><td>+1 212 761-0428</td></tr><tr><td>MS ASIA LIMITED+</td><td>Gek Teng KhooGek.Teng.Khoo@morganstanley.com</td><td>+852 3963-0303</td></tr><tr><td>MS INDIA PRIVATE COMPANY LIMITED</td><td>Nimish PrabhuneNimish.Prabhune@morganstanley.com</td><td>+91 22 6996-1862</td></tr></table>

## Global EM Strategy

EM bond yields have not fallen as much as oil and broader energy prices would have suggested, based on their tight correlations over the past few months. Higher core rates, EM currency weakness and continued market pricing for tighter monetary policy from EM central banks over the coming year all help to explain this.

Yet, with energy prices continuing to fall we expect risk appetite to be robust, helping EM currencies stay strong on at least a trade weighted basis. We see a Fed on hold this year, which will also help EM central banks to deliver a more dovish path than the markets expect. In other words, EM local bond yields should move lower in coming weeks and months.

## Local markets trades overview

\- Rates: CEEMEA: SA 1y1y-2y2y steepener, HUF 5Y5Y receiver versus PLN 5Y5Y payer, long NGOMOB 22-Sep-26 (FX-unhedged); Asia: Pay 5y HKD IRS versus USD IRS, pay 5y INR NDOIS, 1s5s THB NDTHOR steepener; LatAm: Buy 2028 MBonos, Pay Jan 29 DI

\- FX: CEEMEA: Short EUR/HUF, short 3m USD/TRY forward; LatAm: Short PEN/CLP

## Why are yields not lower?

Oil prices closed last week at the same level they opened on the first day of trading following the start of the US-Iran conflict. There are still risk premia in markets clearly, but oil prices have come a long way down from the highs.

EM local currency government bond yields have not made as much progress as oil prices. EM local currency index yields and oil prices were tightly correlated in the first 2 $\frac{1}{2}$

Source: Bloomberg, MS

months after the outbreak of the conflict, but have started to diverge over the past month, with index yields failing to fall as fast as oil prices (Exhibit 1).

If we use a broader measure of energy prices, like the Bloomberg Energy Index, the gap is not so large, but some 10-15bp cheapness is observable based on this relationship.

Exhibit 1: Yields have lagged the move in oil prices  
![](images/884c03ea48084f918835b80266617a4ba82677f46c4977b893d879c719dbf940.jpg)  
Source: Bloomberg, MS

Exhibit 2: Even using a broader measure of energy prices, yields look 10-15bp too high  
![](images/5075fb14dc5bb3a44f7bb61e56cab4411cb59edeec41c3a28b289f6042d2eaac.jpg)  
There are a few reasons EM yields have not fallen further

US yields have moved higher: Strong US data and a hawkish FOMC have led to an unfavourable backdrop for EM local bonds, pushing UST yields higher as energy prices have fallen.

It is notable though that EM has outperformed, with nominal yield differentials breaking below the pre US-Iran conflict lows and narrowing \~50bp from the highs. (Exhibit 3)

In real terms, EM has also outperformed the US as energy prices have come lower, with ex ante real yield differentials compressing almost back to the pre-conflict levels (Exhibit 4).

Exhibit 3: EM yield compression vs USTs continues in nominal terms...  
![](images/850d6b29e9a8c94ae4eb638a03849e1619aa9202f98501240fe5887d305eb7c9.jpg)  
Source: Bloomberg, MS

Exhibit 4: ... and in real terms EM has reversed US-Iran conflict underperformance  
![](images/910b5d8f364616db2ae917c546c620ca77b2e07793996db05c5d572b16e06e95.jpg)  
Source: Bloomberg, MS

USD strength. There continues to be a good correlation between movements in EM currency and EM rates and unsurprisingly the markets that have seen the biggest FX moves are also those markets with the largest moves in bond yields, with COP, HUF and ILS at the bullish end of the scale and TRY (not shown on chart for scale), IDR, KRW, INR and THB on the bearish end. BRL is an outlier, with a significant move higher in bond yields despite a resilient currency since Feb 27th.

Despite the role exchange rates can play in helping to explain the relative performance of different EM bond markets, adjusting for exchange rate movements doesn't improve relationship between movements in energy prices and yields.

If we add energy prices in EM local currency terms (on an index-weighted basis) to Exhibit 2, rebasing the series so the local currency version is the same value as the USD version on 27th Feb, then we can see that energy prices in EM local currency terms are only a touch higher than in USD terms over that time period, reflecting the 3% weakening in EM FX on a spot basis. This does little to explain the more limited drop in index yields vs energy prices.

Exhibit 5: FX performance helps to explain relative bond performance...  
2y LCY Bond Yield (chg since 27-Feb, bp)  
![](images/990e4103a37b19d77cdc2ef34acbe4016def9d608da6ee801d1d96fb43b16a1a.jpg)  
Source: Bloomberg, MS

Exhibit 6: ...but does little to explain the lag in index yields vs energy prices  
![](images/ec2c8399ec698ded08437a5cd8b1a4fd8974b16be4ed0c5e97a939bc630c2f8c.jpg)  
Source: Bloomberg, MS

EM monetary policy still points to hikes: Markets continue to price higher policy rates across EM, at least at an index level. The extent to which markets are pricing higher policy rates has come down a touch relative to the levels seen at the time we published our Mid-Year Outlook in mid May (Exhibit 8), and when concern about high oil prices was greater. But nonetheless, continued market pricing of higher policy rates has limited the rally in bonds.

Higher short-term rates can be seen in 1y1y swap rates which remain comfortably above the Feb 27th levels, even if down from the highs seen at the peak of concerns about the inflation outlook. (Exhibit 7). MS economists remain more dovish than the market on the path for central bank policy more or less across the board in EM, and this supports a more constructive view on at least the front-end of EM curves (Exhibit 8).

Exhibit 7: 1y1y rates are higher in EM than Feb 27th levels  
![](images/2b4789d355d3fb3176646bc3c8c91eb4f1a66dbfc3ef762951437d36760cd40d.jpg)  
Source: Bloomberg, MS

Exhibit 8: MS more dovish than market on central bank pricing  
![](images/b2fad08db8d7d969931d9e626c3cd5bbecc798beaa24f671d5e3ac57806fcf14.jpg)  
Source: Bloomberg, MS

## Stay Long EM vs Basket

We argued in our last EM strategist (see Global EM Strategist: Finding Your Funder) that EM would likely continue to perform well vs a range of different DM currencies. With the USD on a stronger footing following the last FOMC meeting, this thesis is being tested.

So far, so good: Our index of EM currency total returns continues to make new highs vs G3 (USD, EUR, JPY) a diversified DM basket (G3 + CHF, AUD, CAD). Over the past month, quarter and year to date, EM currencies have delivered positive returns against all funding currencies with the exception of AUD (on a ytd basis) and USD (just, on a mtd basis) (Exhibit 9 & Exhibit 10).

We continue to believe in our bottom up thesis that the asset class is well placed to take advantage of continued strong risk appetite, limited global investor allocation to EM local and generally positive fundamentals. With continued debate over the USD cycle, investors looking to position to isolate the EM exposure as best as possible could consider a G3 or broader DM funding basket.

Exhibit 9: EM vs DM Gains Continue  
![](images/7384470b929b64f7f064e632748b2ba8bcd629f14e399bd0749307752b26c82e.jpg)  
Source: Bloomberg, MS

Exhibit 10: Broad EM FX gains vs many DM funders  
![](images/619506f95251be4a5eb4a27e174f3eb063a48729de26b8e37c3ec8b8d10069b3.jpg)  
Source: Bloomberg, MS

## What can we say about positioning?

In EM local currency bond markets, our flow tracker covers 9 EM markets – all benchmark countries – that report data on foreign holdings of local currency government bonds on a reasonably high frequency basis. Some of the data are more timely than others, but overall we can get a reasonable sense of foreign flows by making valuation and exchange rate adjustments.

As of Friday June 19th, we had data from 5 of the 9 countries. The data are a good approximation for trends in the overall market (see our primer here)

\- Picking up. After heavy outflows in March, and stability in May, flows have started to pick up again in June. YTD inflows are similar to what we saw in 2025. We expect to see inflows pick up as we move through the year, particularly if oil prices fall further and we see great global fixed income stability.

\- 3m sum flows rebounding: Rolling 3m sum flows dropped from \$40bn in mid Feb to around -\$20bn at the end of May but are now rebounding. As the heavy outflows from March gradually fall out of the rolling 3m sum and we see greater stability in new flow, this indicator should continue to rise.

\- YTD returns are flat: Total returns for EM local markets peaked in 2H Feb and now stand at around 1.5% YTD, with coupon/carry offsetting losses from spot FX and duration.

Source: Haver, National Sources, Bloomberg

Exhibit 11: Flows have stabilised  
![](images/81bb40459948a396f15316eaf10d9e27c61d255a8603f55aa631e37882227183.jpg)  
Source: Haver, National Sources, Bloomberg

Exhibit 12: 3m flows negative but the weakness is back-loaded  
![](images/8c5d5bf205658d7966fb73b9dec0de4b30a45565c46f1822d46dada9b20cf5a8.jpg)

Our flow tracker into 9 EM local markets is correlated with the returns of the overall local currency government bond market. This is not surprising, but confirms the validity of our tracker. Over the past 6m, returns and flows are very much in the neutral zone, though some modest divergence is opening up with returns softening.

Exhibit 13: Inflows are correlated with returns. So if we hit extremes on outflows (not there yet) the risk/reward to enter the market could be strong  
![](images/da972bcc11b0d0a4f85c0a2edf9bb4b316be7d05d3deb9a0054ecd26f94344fb.jpg)  
Source: MS, Bloomberg

In FX markets, we use FX options data to gauge positioning, and these data continue to show a long USD bias for investors.

\- Long USD positions: The DXY, BBDXY and the Broad USD are USD indices that investors track. Aggregating the individual currency pairs to reflect these indices shows that investors remain long USD, and added to these positions modestly in the last week, particularly against GBP and CAD.

Recent data have shown the resilience of the US economy amid high oil prices, with more weakness shown in Europe. US equity market outperformance and a more hawkish than expected FOMC meeting had led to renewed talk of US exceptionalism – a vaguely defined term but generally associated with USD strength.

Across EM, the heavy long HUF position remains unchanged – a position we share with our expectation that EURHUF can fall to 340. We have seen some modest profit taking here but expect investors to remain engaged with the theme. Investors remain constructive EM though broadly speaking, adding to long ZAR, CNH, IDR and INR positions recently. BRL exposure is now neutral. We stay bullish on EM currency and share the optimism reflected in FX options data.

Exhibit 14: Positioning in the FX Options Market  
![](images/11a9e73c006df16a8cf2562f9d069e5da3e5963d29c2a13fa45274dc6ef1ca6c.jpg)  
Source: DTCC, Bloomberg, MS; Note: Using options that were traded in the past three months and expire in the coming one month. Notionals are delta-adjusted. Data as of Friday, April 19. See FX Trading Signals From Options Data and Assessing FX Positioning with Currency Options

EM total returns for the year remain around 1.5% though with significant regional variation. Latin America remains the only region with broad positive total returns across multiple countries, with duration and FX both positive. Optimism about policy change in Colombia has led to significant returns in recent returns and the country has overtaken Hungary as the asset class' biggest outperformer. In CEEMEA Hungary is the standout performer, with ZAR contributing somewhat too. Asia continues to lag with only China providing positive returns.

Exhibit 15: Much of CEEMEA and Asia have underperformed ytd)  
![](images/d9bee97a7b5b8b737ec276e2fed07dd8c1418b814b2b369e29b91cd679c01dfd.jpg)  
Source: Bloomberg, MS

## Required reading

## Senegal Sovereign Credit Strategy: Local Currency Auction Tracker - 19 June 2026 | 22-Jun-2026

Senegal's local currency auctions are an important driver of sovereign credit valuations. In this tracker, we break down the latest auction and place the results in the context of historical trends.

## Fixed Income Strategy: Bloomberg Ticker Almanac | 18-Jun-2026

This new annual publication details our entire catalogue of data that we host on the Bloomberg Terminal. We provide clients access to time series data requiring complex transformations to make it more readily accessible - this bespoke data is a useful tool to help clients add alpha to their portfolios.

## Indonesia – Economics, Macro & Equity Strategy: Value Re-established but Stay Underweight for Now | 18-Jun-2026

Although the equity risk premium has risen substantially it could well rise further creating a better buying opportunity later. The upcoming MSCI decision point is a less important signpost than a return to positive earnings growth

Czech Republic Economics and Macro Strategy: CNB Review: One Move, Open Risks | 18-Jun-2026

The CNB raised its key policy rate by 25bp to 3.75%, somewhat earlier than we expected. The statement pointed at extra caution for additional action. We continue to expect no additional tightening this year, but see risks skewed to the upside. We stay neutral on Czech rates

[中间内容因长度限制已省略]

ardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i)

are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Nimish M Prabhune; Simon Waever; Ioana Zamfir; Emma C Cerda; Gek Teng Khoo; Neville Z Mandimika; James K Lord.

## © 2026 MS
"""
