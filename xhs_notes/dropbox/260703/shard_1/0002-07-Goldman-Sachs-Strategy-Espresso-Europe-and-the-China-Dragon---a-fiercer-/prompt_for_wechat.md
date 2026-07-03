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
# Strategy Espresso: Europe and the China Dragon – a fiercer fight

Is China continuing to take share in Europe? Yes, more than ever. China's exports to Europe have grown double-digit p.a. in recent months, and China has been increasing share in third markets. China now accounts for $23\%$ of EU imports. Meanwhile, China's share of EU exports has fallen sharply since 2020.

What are the drivers? China's companies are seeking growth outside given weak domestic demand and over-capacity in many industries. China also has huge cost advantages in labour, borrowing, energy and land use as well as a significantly undervalued currency. These, combined with Europe's own growth impediments—regulation, planning laws, lack of investment—have all meant China is rapidly gaining share in manufacturing.

Who is exposed? Stocks in the China competition basket (GSXECHNX); mainly in Autos, Medtech, Chemicals and select Industrials. This basket has consistently underperformed both STOXX 600 and our Asia team's China Going Global basket (GSXACHGG); the underperformance tallies closely to the widening trade deficit with China.

Is it in the price? Underperformance has largely been a function of EPS downgrades. Given the ongoing export share gains by China and continued weak earnings outlook for these exposed stocks we continue to expect earnings-driven under-performance rather than further valuation declines given the discount for these stocks is already steep.

Is Europe defending itself? Less than $10\%$ of Chinese imports into the EU currently face tariffs—a sharp contrast with the US approach. The EU is unlikely to copy the broad-based US approach but our economists do expect the EU to target reducing reliance on Chinese components and tariffs on specific sectors.

\- Does this matter for European indices? Not as much as investors tend to think. Autos and Chemicals combined are smaller than Aerospace & Defence or Renewables. Tech Hardware and Autos had roughly the same market-cap just three years ago, now Tech Hardware is 4x the size of Autos.

What does this mean for global investors? While China is clearly gaining market share, this does not necessarily translate into shareholder returns. Much of China's success has been driven by aggressive pricing, often resulting in subdued profitability. As a result, Chinese equities have not been the primary beneficiaries of China's export expansion. European equities have outperformed over most medium- and long-term horizons, supported by stronger earnings quality, higher returns on capital, and greater diversification by sector.

## Sharon Bell

+44(20)7552-1341 | sharon.bell@gs.com GS International

Guillaume Jaisson  
+44(20)7552-3000 | guillaume.jaisson@gs.com GS International

Peter Oppenheimer +44(20)7552-5782 | peter.oppenheimer@gs.com GS International

Giovanni Ferrannini  
+44(20)7051-2589 |  
giovanni.ferrannini@gs.com  
GS International

Elena Porfidia  
+44(20)7051-5240 |  
elena.porfidia@gs.com  
GS International

## Q&A on Europe Equity & the China Dragon – A fiercer fight

1. Is China continuing to take share in Europe, and in third markets? Yes, most certainly. China exports to Europe have been growing at a double digit annual pace in recent months, and China has been increasing share in third markets too. China now accounts for $23\%$ of EU imports (Exhibit 1) and the share of China in Europe's exports has fallen sharply since 2020. In other words, China is buying less from Europe but selling more into Europe, representing a competitive threat to European manufacturing companies. We have seen several companies warn or lower guidance over China competition in recent weeks, including Signify and BMW.

Autos: The figures are stark, our analysts report that Chinese domestic brands gained over 400 bps of Europe market share in the year to end May (their overall share of the European market is now 6–7%), corresponding to a roughly 400bps share loss from mass-market brands in Europe. They argue that this share gain trend appears to be accelerating, with every mass-market brand losing ground except Tesla. Relative to the mass market, the European premium brands have proven more resilient but even these are losing share.

Chemicals: Our analyst recently downgraded several names arguing that China's export-oriented pivot over the course of the Middle East conflict has effectively extinguished any short-lived hopes of a revival in European competitiveness. With other Asian countries suffering feedstock supply issues and domestic Chinese demand remaining low, excess capacity is forcing product out of China with chemical exports from China to the rest of Asia rising $70\%$ in March and April according to ICIS data. In addition, China is beginning to lead not only in commodities but increasingly in semi-specialty chemicals too.

Capital goods: In their machinery export tracker our Asia analysts talk about strong growth in Europe of $+50\% / +19\%$ yoy in volume/value, mainly on accelerated China exports. And our European team argues that while Europe still leads in exports of capital goods within their tracked products, accounting for $43\%$ of global volumes, its share has decreased from $54\%$ in 2005. Meanwhile, China is steadily increasing its export presence in the global marketplace, gaining 17pp of market share, from $7\%$ in 2005 to $24\%$ in 2025. Chinese competition acceleration has been most noticeable in recent months for LED lighting, excavators, heat pumps, light commercial vehicles, heavy-duty trucks and tractors.

Exhibit 2: Machinery accounts for almost one third of EU imports from China  
EU Imports from China (% of total import from China)  
Exhibit 1: Europe imports more from China but exports less  
![](images/99cb2c0a658f36f6fc23339164f3fcd9477b5dd4f4469f510df39bdeaae520a5.jpg)  
Source: Haver Analytics, GS Global Investment Research

![](images/82e83985929883438cd920dea9f3be9359c9cd9bbd28db16b02a3be34eb586d5.jpg)  
Source: UNCTADstat, GS Global Investment Research

2. What are the drivers? China's companies are looking for growth outside given weak domestic demand and over-capacity in many industries. Our Asia economists argue China has huge manufacturing cost advantages: (i) lower labour costs, (ii) borrowing costs are very low in targeted sectors facilitated by a state banking system with a large pool of low-yielding deposits, (iii) China has a large, low-cost (though high-pollution) energy source in coal while government policies have also encouraged rapid development of solar energy, as well as a broader shift away from reliance on imported energy (e.g. via development of the EV sector). China's manufacturing firms enjoy very competitive power costs, especially versus Europe (Exhibit 3), (iv) on land, top-down planning means households pay high residential property prices and in effect subsidize manufacturing land use, (v) currency weakness, despite China outpacing world growth over the past decade and an improvement in manufacturing productivity the renminbi has slid in recent years and while it is true that the currency has strengthened since the lows in early 2025, it remains significantly undervalued on our FX teams' currency frameworks (Exhibit 4).

The combination of all these, along with some of Europe's own impediments to growth – regulation, planning laws and lack of investment – have all meant China is rapidly gaining share in manufacturing.

Exhibit 3: China's low power costs rival those in the United States
Power prices for industrial sectors  
![](images/17f4fc406b2038b291f5c8822d7b2398ae5191c192ea1059aeb5413bfb385097.jpg)  
Industrial power prices including taxes in 2023 for all except for Japan, where data is only available for 2021, and for China, where data is only available for 2018 and average power prices for all sectors instead of the industrial sector only

Exhibit 4: CNY has appreciated since the 2025 lows but remains under-valued compared with China's strong economic and productivity growth in recent years Index, 2019 = 100  
![](images/1e86e395ca5aaa2483eaa1f4df3d9dbb116032760ff7b10bde3094f71f9eddcb.jpg)  
Source: Haver Analytics, GS Global Investment Research  
Source: Penn World Table (PWT), Haver Analytics, GS Global Investment Research

3. Who is most exposed to China competition; how have they performed? Exhibit 5 shows the correlation of European sector EBITDA margins with China PPI inflation. The sectors with the highest sensitivity to this weak pricing dynamic, measured by the correlation of margins to China prices, have been Chemicals, Autos and Basic Resources (mining). On the flip-side, lower prices in China manufactured goods have been associated with better margins in some consumer and services sectors in Europe.

Of course there is always potential for these dynamics to shift either via Europe putting tariffs or other regulations on China goods, or by China making inroads into other previously insulated industries. Most recently internet retailing platform, JoyBuy, launched in the UK and users quickly rose to being $10\%$ of those for Argos, owned by Sainsbury's.

Exhibit 5: Margins of Chemicals, Autos, and Mining are the most sensible to China pricing dynamics
Correlation between China PPI and EBITDA Margin across European sectors since 2005  
![](images/dab0990dab6bd77a707e568952eaeab736e36c95ea6c93c1aaf2bc60304e07e5.jpg)  
Source: Haver Analytics, Datastream, GS Global Investment Research

In terms of companies, in our original work on Fighting the China Dragon we screened for companies that mention China as a competitive threat or potential threat. We found that across the STOXX 600 index China has been mentioned almost 10,000 times by around 300 companies since Q1 2024, although mostly these mentions are positive mentions about growth/demand, they are increasingly also about risk and competition. We screened the companies for the more negative comments which concerned competition and our Global Banking and Markets (GBM) division created a basket optimising for liquidity – GSXECHNX.

The companies are mainly in Autos, Medtech, Chemicals and select industrials. These companies have consistently underperformed both versus the STOXX 600 and versus our China Going Global companies from our Asia team, GSXACHGG (Exhibit 6).

Exhibit 9: Companies exposed to China competition trade on a substantial discount to the market  
12m fwd P/E Premium/Discount vs. STOXX 600. European sectors and baskets. China Exposure = GSSTCHNA; China Competition = GSXECHNX  
Exhibit 6: European companies exposed to China competition have consistently underperformed the market  
![](images/60617ee3b7cecfce470f32cdc2d70d4f76f5814542a88223f18c7fbb90ff2688.jpg)  
Source: Bloomberg, Datastream, GS Global Investment Research, GS FICC and Equities

Exhibit 7: Europe's widening trade deficit with China
Price performance and trade balance between Euro Area and China (RHS)  
![](images/22f675b8b78fb6f780eaba93eaedd01f46ed9dd30873cbc6ba064194901b9ea8.jpg)  
Source: Datastream, Haver Analytics, GS Global Investment Research, GS FICC and Equities

4. Is the weakness now well priced? We continue to argue for an under-weight in companies with high China-competition exposure, for example we recommend an underweight in Autos and Chemicals for this reason. The basket of China-competition exposed companies (GSXECHNX) has performed consistently poorly, both in terms of earnings and price performance (Exhibit 8). That said, these companies do trade on a substantial discount to the market c. 25-30%, a contrast to companies with high China sales exposure (GSSTCHNA) but not necessarily competition threat (Exhibit 9). Given the ongoing export share gains by China and continued weak earnings growth for these stocks we continue to expect earnings-driven under-performance (Exhibit 7) rather than further valuation declines given the discount for these stocks is already steep.

Exhibit 8: The basket of China-competition exposed companies has performed consistently poorly EU China competition basket (GSXECHNX)  
![](images/dc80fa2137af062d2da76c9ec573f4c7bcd0dc8189034b1e018cdebd36b10f00.jpg)  
Source: Bloomberg, GS Global Investment Research, GS FICC and Equities

![](images/4ef0556f68048dcef97957221a4fb44244793153eb3c245eb84b2b57a1e93870.jpg)  
Source: Datastream, Bloomberg, GS Global Investment Research, GS FICC and Equities

5. EU policy-makers are starting to focus on the threat posed by low-cost China manufacturing to Europe's industries. In its June meeting, the EU Council mandated the EU Commission with the task to propose the appropriate response to China, marking a shift in European policy. The EU has so far taken a relatively cautious stance toward

Chinese products. Although most EU trade-defence investigations have targeted China, less than 10% of Chinese imports into the EU currently face tariffs—a sharp contrast with the US approach (Exhibit 11). The main exceptions have been tariffs on battery electric vehicles, introduced in October 2024, and the abolition of the EUR 150 customs-duty exemption for small parcels from July 2026.

Our economists expect the Commission to continue to raise trade barriers, but in a targeted way consistent with the new trade-diversion monitoring framework:

Near-term measures are likely to focus on sectors where evidence of diversion or injury is strongest, such as tightening steel safeguards to prevent Chinese steel from being rerouted through third countries.

\- Expect anti-subsidy duties to be extended to hybrid vehicles, alongside faster anti-dumping investigations into machinery, wind-turbine components, and basic chemicals.

The EU is also discussing broader and more aggressive trade barriers by forcing procurement of “made in Europe” goods, limiting foreign direct investment in strategic sectors (Industrial Accelerator Act), restricting access to European market for Chinese technologies (Cybersecurity Act), and forcing European companies to diversify their supplies (“Anti-Dependency” instrument). Talking to corporates, we find that supply-chain resilience is already an area in which most managements are focused.

This structural shift under discussion could allow the EU Commission to impose sweeping tariffs and import quotas on sectors deemed critical to the bloc's "economic security". Benefitting from the WTO national security exceptions, the EU could target advanced manufacturing sectors—such as semiconductors, batteries, and robotics—where Chinese state subsidies are challenging the survival of Europe's industrial base.

Why does Europe not go further? Our economists expect the Commission to avoid US-style blanket tariffs for four reasons: (i) China retains leverage as a key supplier of refined rare earths, (ii) broad tariffs would do little to address the main source of the growth drag, which comes from lost market share in third countries, (iii) China still accounts for c. $8\%$ of total EU goods exports with US tariffs still elevated, European policymakers have an incentive to preserve access to China, and (iv) China's cost advantage is sufficiently large that tariffs may not materially close price gaps in some sectors.

Given these barriers, our economists expect a dual-track strategy: a diversification instrument to reduce reliance on Chinese components, and a protective instrument to raise targeted tariffs and quotas after due process and sector-specific investigations.

## Exhibit 10: Chinese Manufacturers Enjoy a Large Cost Advantage

Industrial subsidies in selected industrial sectors as a share of revenue (2024)

![](images/a174b99fd2d120e379c75e35dab1bd3ca441fec91fb8f82ccb70262976a0e4cc.jpg)  
Source: OECD, GS Global Investment Research  
Exhibit 11: Less than $10\%$ of Chinese imports into the EU currently face tariffs  
Share of imports from China covered by ad-hoc tariffs\*

![](images/3461dfd0099078fa7faf7189f04ff6800b2913706d28cd4383b3179a1be71cf4.jpg)  
Tariffs imposed on top of MFN rates  
Source: Haver Analytics, European Commission, GS Global Investment Research

6. How about innovation and investment? Europe has under-invested in recent years, at both the economy and corporate level, while in contrast China has been raising investment as part of the economic and political ambition to increase manufacturing and export share. For the market ex financials both US and China companies have spent in the last 5-years c.40-45% of their cash flow from operations (CFO) on growth investments, defined as R&D and capex over depreciation. In contrast, the European market share of growth-investment to CFOs is about 20%.

We show in Exhibit 12 the share of R&D and capex to CFO for tradable goods (ex food), technology and resources sectors. In almost all cases, Chinese companies have spent more in the last five years. For Chemicals the difference is especially large, but China also consistently spent more on growth-investment in Autos, Electronic/electrical equipment, Med tech, Software and computer services, Basic resources, Energy and Industrial transport.

Exhibit 12: Where do Chinese companies invest more? Share of R&D and capex to CFO for tradable goods (ex food), technology and resources sectors (last 5-years)  
![](images/f1272713b173792282990237154588a49954162fe7d825e2783a1e4a88894289.jpg)  
Source: FactSet, Datastream, GS Global Investment Research

The only areas where Europe has spent to a similar degree as China are Pharmaceuticals, Tech hardware, and Utilities:

In Technology, ASML is considerably ahead with China having neither EUV tools nor DUV immersion tools. Our analysts argue the ecosystem around EUV IE lenses and lasers and mirrors plus engineering know-how as well as feedback from leading edge customers will be challenging or even impossible to replicate. In a recent CEO visit note they contextualised Chinese efforts with stacking which validate that they do not have equivalent EUV technology. We continue to recommend an OW in Technology.

European utilities are investing heavily in renewables and in electrification and power grids more broadly, which should improve Europe's aged power infrastructure, improve energy independence, and provide energy for the data centre roll out which will enable greater use of AI across industries. Our utilities analysts expect power-requirements to drive €3.5 trn of investment needs in power generation (largely renewables) and power grids over 2026-35, thus supporting a generational ear

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
