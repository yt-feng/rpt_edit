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
COMMODITY VIEWS

# From Energy to Metals: Why to Still Diversify Into Commodities

As energy flows start to normalize through the Strait of Hormuz, we take stock of how commodities have performed year to date, highlighting that the energy supply shock triggered by the Iran conflict is only the most recent of several examples seen over the past year of why strategic investment portfolios can benefit from diversifying into commodities.

Investing in different commodities can help diversify risks inherent to equity/bond portfolios under different circumstances, including (1) commodity supply shocks, like the Hormuz disruption, which might lead to higher inflation and lower economic growth, (2) structural demand support for commodities that face challenges to growing supply, and (3) a flight to real assets when fiscal sustainability or other financial risks arise. We see many of the drivers behind such circumstances, which are supportive of commodity returns, remaining relevant going forward.

In particular, we think that the Iran conflict ultimately reinforces many of the themes supporting power and metals demand, more so than oil and gas. From a potential increased reliance on EVs, to further investment into renewable power generation, both of which require further grid investment, to potentially larger defense spending, and growing competition to win the AI race, these themes are highly supportive of power, copper, lithium and aluminum demand.

Combined with the fact that power infrastructure can face bottlenecks and that metals refining remains highly geographically concentrated, this strong structural support to power and metals demand leaves these markets vulnerable to tightening shocks. As a result, while oil and gas have traditionally had a bigger impact on inflation, and its supply concentration and associated geopolitical risks remain, sharp price increases might start to also appear more often across power and industrial and precious metals markets going forward.

## Samantha Dart

Samantha Dart +1(212)357-9428 | samantha.dart@gs.com GS & Co. LLC

Daan Struyven +1(212)357-4172 | daan.struyven@gs.com GS & Co. LLC

Lina Thomas  
+1(212)902-8376 | lina.thomas@gs.com  
GS & Co. LLC

Yulia Zhestkova Grigsby
+1(646)446-3905 |
yulia.grigsby@gs.com
GS & Co. LLC

Hongcen Wei  
+1(212)934-4691 |  
hongcen.wei@gs.com  
GS & Co. LLC

Lavinia Forcellese +44(20)7774-9243 | lavinia.forcellese@gs.com GS International

Aurelia Waltham  
+44(20)7051-2547 |  
aurelia.waltham@gs.com  
GS International

Filippo Cuscito  
+44(20)7051-9073 |  
filippo.cuscito@gs.com  
GS International

Laura Cyr
+1(212)902-3435 | laura.x.cyr@gs.com
GS & Co. LLC

Alexandra Paulus +1(212)902-7111 | alexandra.paulus@gs.com GS & Co. LLC

## Commodities Can Help Diversify Equities/Bonds' Risks Under a Broad Range of Circumstances

1. A large energy shock, the second in only five years. While the 2022 energy crisis impacted mostly natural gas supply, lifting liquefied natural gas (LNG) prices across Europe and Asia, this year's 16-week Strait of Hormuz disruption significantly reduced supply of both oil and gas, causing a broad increase in energy prices, while threatening the global economic outlook. Even as crude oil prices now recede following the US-Iran deal to re-open the Strait of Hormuz, broad commodity price gains year to date, combined with a strong oil roll yield $^{1}$ during the conflict, have supported year-to-date commodity returns well above those of equity and bonds (Exhibit 1), though with higher volatility.

Exhibit 1: The Strait of Hormuz disruption contributed to commodity returns outperforming other assets year to date, especially as a strong roll yield for oil combined with higher prices  
![](images/e4c4c037233f460a562c599cc87f8513e669e1eaa010a748b80325678fd9657e.jpg)  
Source: Bloomberg, GS Global Investment Research

Importantly, the upside to energy prices during the conflict was limited by what proved to be a more flexible global market than what we originally expected. In particular, the sharp drop in China liquefied natural gas (LNG) imports in Mar/Apr, the first two months of the conflict, and in oil imports to this day, helped limit global market tightness. Still, by May, three months into the conflict, crude oil and oil product (like gasoline, diesel and jet fuel) prices had rallied 43% and 63%, respectively, vs pre-war levels, while European gas and Asia LNG prices rallied 50% and 70%. And while crude oil prices have come off sharply over the past couple of weeks, the same cannot be said of gasoline or diesel, where we expect demand to rebound faster than supply, keeping balances tight for longer, and prices slower to come down.

Overall, assuming that the re-opening process continues, the Hormuz shock will likely have a limited scarring effect on global economic activity and hence on energy demand. Our economists expect global GDP growth at 2.4% this year, 0.4pp down from 2025.

Had the Iran conflict lasted longer, its negative impact on global growth might have been significantly larger at -2pp from our pre-war expectations, underscoring the potential value of diversifying into commodities in strategic investment portfolios.

2. Long-term structural support for copper prices, with a near-term policy boost. The pairing of strong structural support to copper demand with a long-cycle supply side, where it can take an extended period of time for supply to respond to price incentives, sets the stage for a well supported price environment for copper.

On the demand side, growth has been increasingly tied to strategic sectors, with grid and power infrastructure likely driving over 60% of copper demand growth by 2030 (vs. 2025), alongside direct boosts from defense, electric vehicles, renewable generation capacity, and data centers. Importantly, we see investment in aging Western power grids as a national security priority, due to its critical role in AI and energy security. This shifts copper demand from being mainly cyclical to increasingly strategic, making it less sensitive to economic slowdowns and high prices than traditional demand sources such as construction or white goods.

At the same time, copper supply might struggle to grow fast enough (Exhibit 2). Multiple recent mine incidents highlight the growing structural challenges in copper mining as copper mines get deeper, grades get lower and ore gets harder, requiring greater investment. This adds to operating costs and sustaining capex, and limits the ability of supply to respond quickly. As a result, copper prices have to rise to solve this gap by incentivizing higher scrap supply and potential demand substitution into alternative materials such as aluminum.

Exhibit 2: We expect copper demand growth to continue to outpace that of mined supply  
![](images/c1ef996f292247394d1ae8ed9c766e8297bc9176102cd4ce3308c1c9a66cad2d.jpg)  
Source: Wood Mackenzie, CRU, S&P Global Market Intelligence, SMM, ICSG, GS Global Investment Research

While the copper balance tightening we expect is gradual in nature, shifts in policy have brought some of that tightness forward. Specifically, since the US imposed import tariffs on steel and aluminum last year, copper imports into the US picked up significantly in anticipation of a potential US copper import tariff being implemented. While there remains no US tariffs on refined $^{2}$ copper imports, copper tonnes have continued to head to the US, causing the ex-US copper balance to tighten significantly (Exhibit 3), and prices to briefly reach an all-time high of over \$14,000/t in May, before moderating to the low-to-mid \$13,000s.

These tighter copper balances led us to recently raise our end-2026/average 2027 LME copper forecasts to \$13,735/\$13,800. Our longer-term view remains that prices will need to rise further by the next decade to balance the market. By 2035, we think a price of \$15,000/t will be needed to keep aging mines in operation, lift scrap collection rates, deliver additional substitution and support the development of new mines.

Exhibit 3: Policy-risk-driven copper flows into the US drove the ex-US market into a deficit this year  
![](images/69afdb13b50697f967d4b1417e54cff2e7dde22b7bc28e91f746866d3695f700.jpg)  
Source: Wood Mackenzie, CRU, SMM, ICSG, S&P Global Market Intelligence, GS Global Investment Research

3. Gold is not done. Despite gold's strong rally since 2022 (up $123\%$ ), we continue to see further upside, driven by both structural and eventually cyclical factors. Structurally, EM central bank diversification—following the 2022 freezing of Russia's reserves—remains the anchor of our $\$4,900/$ toz end 2026 forecast (Exhibit 4). While the pace of central bank gold purchases has moderated to $\sim50$ tonnes/month on a 3-month (seasonally adjusted) and 12-month moving average basis, we view the ongoing diversification trend as structural. A recent World Gold Council survey supports our view: a record $45\%$ of the 76 central banks surveyed between February and May expect to increase their own gold reserves over the next 12 months, while $\sim90\%$ expect global reserves to rise with the remainder expecting broadly stable holdings (Exhibit 5). We therefore assume continued central bank accumulation of 50t/month in 2026 and 40t/month in 2027.

Cyclically, however, gold faces near term headwinds from the potential hit to demand for macro policy hedges (as a hawkish Fed helps fade the debasement theme) and as markets are pricing in Fed hikes this year amid inflation concerns, weighing on rate-sensitive ETF demand. We expect these headwinds to at least partly reverse over time. While we assume stable macro-policy hedges demand for gold, we expect ETF positioning to gradually rise, consistent with our economists' view of a delayed but ongoing easing cycle in 2027H2. Over the medium term, risks to our gold price forecast remain skewed to the upside on net. Gold's share in private portfolios remains small, and the Iran episode — together with broader geopolitical developments (e.g., Greenland, Venezuela) — may eventually accelerate private diversification into gold, including by weighing on perceptions of Western fiscal sustainability.

Exhibit 4: Continued central bank diversification remains the main driver of our constructive gold price outlook  
![](images/6df4576968a14ba3f6ec7acbe02709429dea44c944d0436d0ba0ca6be1fd9f07.jpg)  
Source: GS Global Investment Research

Exhibit 5: The recent World Gold Council central bank survey suggests continued gold demand  
![](images/171c0824c642e6cb7d8a671732da58de0419a80c6556ca1b934d96c8684d097d.jpg)  
Source: World Gold Council, GS Global Investment Research

## To Each (Inflation Shock) Their Own (Inflation Hedge)

While the Hormuz shock has illustrated how commodities exposure can work as a hedge against inflation, it also demonstrated with the sharp sell off in gold in the period that not all commodities work equally well as a hedge under any inflation shock. In practice, inflation typically arises through three distinct regimes – late cycle inflation, supply disruptions, and institutional credibility risk – and each calls for a different hedge.

## Regime #1: Late Cycle – Hedge With Cyclical Commodities

When the business cycle runs hot, equities initially benefit from strong growth. But as the economy begins to outpace its productive capacity – what economists call a positive output gap – inflation pressures build and real bond returns weaken. Over time, rising input costs compress margins and equity growth starts to soften. It is at this point – when bond prices weaken and equity returns begin to lose momentum – that commodities tend to provide diversification through stronger returns. Commodity performance typically strengthens late in the cycle because a positive output gap implies demand exceeds supply. In commodity markets, this imbalance shows up as sustained inventory drawdowns. Late in the cycle, inventories have been drawing for long enough to approach depletion, pushing prices higher – especially for cyclical commodities like oil and industrial metals.

## Regime #2: Supply Disruption – Hedge With a Broad Commodity Basket (Ex. Precious Metals)

When a supply disruption hits – as just exemplified during the Iran conflict – inflation rises while growth weakens, weighing on bond and equity prices simultaneously. Commodities, as the disrupted input, are then among the few assets to deliver positive real returns. Because the source and timing of disruptions are inherently unpredictable, a broad commodity basket (ex. precious metals) offers the most robust protection.

## Regime #3: Institutional Credibility Risk – Hedge With Gold

In the first two inflation regimes – late cycle inflation and supply disruptions – gold is not an effective hedge. If anything, gold often sells off initially: higher inflation can lead markets to price in rate hikes, raising the opportunity cost of holding a non yielding asset, while equity drawdowns can trigger margin call liquidations in gold, whose liquidity makes it a ready source of cash. Gold hedges a narrow inflation regime: when inflation expectations rise due to concerns around institutional credibility or macro policy, causing bonds and equities to sell off together in real terms. Gold then stands apart as the key neutral asset whose value does not rely on any government backing.

## The Iran Conflict Appears on Its Way to a Resolution. What Next?

While oil demand will rebound in the aftermath of the Iran conflict, including what we expect will be an over 1 mb/d push for the rebuilding of strategic petroleum reserves, we think that the Iran conflict ultimately reinforces many of the themes supporting power and metals demand in particular. From a potential increased reliance on EVs, to further investment into renewable power generation, both of which require further grid investment, to potentially larger defense spending, and growing competition to win the AI race, these themes are highly supportive of power, copper, lithium and aluminum demand, while potentially weighing on long-term demand growth of oil and natural gas (Exhibit 6 and Exhibit 7).

Exhibit 6: Global EV sales have sharply accelerated during the Iran conflict...  
![](images/404f18dd580d5047198208413e9674886d7b1810a0e0c1c4751d556faf51fd63.jpg)  
Source: Government Data, IEA, GS Global Investment Research

Exhibit 7: ...as have China solar panel exports  
![](images/d5b81f21930cbc0820cb4125e87f16532cb3b7df9f2ca34c9ee2f2b48c44580a.jpg)  
Source: Ember, GS Global Investment Research

Combined with the fact that power infrastructure can face bottlenecks, as has been the case in the US Mid-Atlantic power market, and that metals refining remains highly geographically concentrated (Exhibit 8), this strong structural support to power and metals demand leaves these markets vulnerable to tightening shocks.

As a result, while oil and gas have traditionally had a bigger impact on inflation, and their supply concentration and associated geopolitical risks remain, sharp price increases might start to also appear more often across power and industrial and precious metals markets going forward. In particular, our economists have flagged that higher industrial metals prices and China's export controls on rare earths and related products were among the main drivers of the recent acceleration in the US' core producer price index, while expecting that higher US electricity prices will continue to boost consumer electricity inflation.

Exhibit 8: Commodity supply is currently heavily concentrated, with a large share of supply in geopolitical or trade-dispute hot spots

![](images/896f978bb65c7ed22b8f10fb4736088c3529aba2665b52688003ec46d264acbe.jpg)  
Source: EIA, IEA, WoodMac, CRU, GS Global Investment Research

![](images/0c0c49ba5bf8b20a2fb9eb1b7aa2e9430650578a3fc34cc81a297a8d2fd8b51b.jpg)

## Appendix

Exhibit 9: The recent Hormuz energy supply disruption is the latest example of why it pays to diversify into commodities Total returns

<table><tr><td rowspan="2"></td><td colspan="5">Historical Performance</td><td colspan="2">GS Forecast</td></tr><tr><td>Dollar Weight</td><td>2023</td><td>2024</td><td>2025</td><td>YTD</td><td>Balance of Year</td><td>2027</td></tr><tr><td>BCOM</td><td>100</td><td>-8</td><td>5</td><td>16</td><td>15</td><td>3</td><td>1</td></tr><tr><td>BCOM ex. Agriculture &amp; Livestock</td><td>63</td><td>-10</td><td>8</td><td>22</td><td>19</td><td>7</td><td>1</td></tr><tr><td>S&amp;P GSCI</td><td>100</td><td>-4</td><td>9</td><td>7</td><td>26</td><td>7</td><td>1</td></tr><tr><td>S&amp;P GSCI ex. Agriculture &amp; Livestock</td><td>76</td><td>-3</td><td>11</td><td>11</td><td>37</td><td>10</td><td>0</td></tr><tr><td>Energy</td><td>52</td><td>-5</td><td>10</td><td>-5</td><td>55</td><td>10</td><td>-2</td></tr><tr><td>Industrial Metals</td><td>14</td><td>-4</td><td>3</td><td>29</td><td>7</td><td>4</td><td>-2</td></tr><tr><td>Precious Metals</td><td>10</td><td>12</td><td>26</td><td>69</td><td>-8</td><td>17</td><td>12</td></tr><tr><td>Agriculture</td><td>14</td><td>-8</td><td>0</td><td>-8</td><td>0</td><td>-3</td><td>2</td></tr><tr><td>Livestock</td><td>9</td><td>0</td><td>20</td><td>27</td><td>5</td><td>3</td><td>1</td></tr></table>

We highlight the commodity indices ex Agriculture & Livestock because we currently don't forecast agriculture and livestock prices, and instead use forwards.

Source: GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Samantha Dart, Daan Struyven, Lina Thomas, Yulia Zhestkova Grigsby, Hongcen Wei, Lavinia Forcellese, Aurelia Waltham, Filippo Cuscito, Laura Cyr and Alexandra Paulus, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Samantha Dart GS & Co. LLC, Daan Struyven GS & Co. LLC, Lina Thomas GS & Co. LLC, Yulia Zhestkova Grigsby GS & Co. LLC, Hongcen Wei GS & Co. LLC, Lavinia Forcellese GS International, Aurelia Waltham GS International, Filippo Cuscito GS International, Laura Cyr GS & Co. LLC, Alexandra Paulus GS & Co. LLC.

Un

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
