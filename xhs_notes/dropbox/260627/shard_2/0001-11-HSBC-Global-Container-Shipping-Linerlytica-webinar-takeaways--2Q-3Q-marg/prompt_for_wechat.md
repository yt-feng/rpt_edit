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
\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

# Global Container Shipping

Linerlytica webinar takeaways: 2Q-3Q margin set to rise

\- Upcycle stronger than expected with demand structural (tech-led) and broad-based, not just frontloading; rates to hold...

\- ...into late summer, driving sequentially higher sector EBIT margins in 2Q-3Q; Maersk/HLAG guidance seem plausible

◆ Reiterate Buy on Maersk, EVG, CSH-H/A; key risk is Red Sea capacity release with bigger 2027-28 supply wave ahead

On 25 June 2026, HSBC hosted Linerlytica to discuss the outlook for container shipping. We discuss key takeaways below. Reach out here to request the replay and slides.

1) Upcycle looks stronger (and longer): Tight effective capacity and improving demand should keep the market firm at least through August, and potentially into September, rather than fading after a brief early peak spike.

2) Rates are still climbing, not rolling over: Freight indicators rose into late June, with carriers pushing July hikes. Spot rates are cUSD6,000/40ft to USWC and cUSD7,000–8,000/40ft to USEC. Charter rates stay high; charter-to-freight gap shrinks as freight rises.

3) Demand strength looks structural, not just frontloading: Traditional China exports were weak Jan-May (garments -1.6%, footwear -10.3%, toys -12.6%), inconsistent with expectations of a consumer surge. Instead, demand looks driven by AI/data centre buildout and clean tech (batteries, EVs, solar), plus data centre power infrastructure.

4) Volumes broad-based; EM absorbing capacity: Trans-Pacific volumes are up c4-5% y-o-y, May strong, and June firmer. European demand is above last year's peak. Africa demand +50% YTD and LatAm +12% absorbing capacity; North America lags.

5) Tariffs may add noise but don't change the near-term setup: IEEPA removal and Section 122 likely boosted exports and Transpacific rebound. With 122 expiring, proposed 301 tariffs look similar, so July/August volumes should hold.

6) Capacity remains tight; Red Sea return is the key downside: Linerlytica sees 2026 demand up $6 - 7\%$ vs supply $c5\%$ . Gulf normalisation could absorb $>2\%$ fleet but Red Sea return could unwind $c6\%$ , risking rates correction. Congestion supports tightness.

7) Earnings leverage is improving despite higher fuel: Fuel is c30% above pre-conflict, but opex should rise only c2-3%. With CCFI up c40-42%, profits should inflect: sector EBIT margin could rise from c5% in 1Q to c10% in 2Q, with 3Q upside if rates hold. Maersk and Hapag Lloyd could potentially raise FY26 guidance, we argue.

8) Alliances shift share but not competition or pricing power. Linerlytica says Gemini Cooperation underperforms due to contract exposure, spot discounting, and hub-and-spoke costs; schedule reliability premiums may be limited.

9) Medium-term reality check – the 2027-28 supply wave: Newbuild deliveries ramp-up in 2H27 and peak in 2028, with supply growth c14%, likely above demand. Ordering stays heavy (c5m TEU this year; c2m TEU YTD). Limited vessel demolition capacity (at most c1m TEU/year) leaves net 2028 growth c11-12%+. Consolidation may shift share, but utilisation-driven rate volatility remains amid high fixed costs.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

## Equities Marine

Global

## Parash Jain\*

Global Head of Transport & Logistics Research  
The Hongkong and Shanghai Banking Corporation Limited  
parashjain@hsbc.com.hk  
+852 2996 6717

## Deepak Maurya\*, CFA

Analyst, Asia Transport
The Hongkong and Shanghai Banking Corporation Limited
deepakmaurya@hsbc.com.hk
+852 2822 4292

## Bruce Chu\*, CFA

Analyst, Asia Transport
The Hongkong and Shanghai Banking Corporation Limited
bruce.y.h.chu@hsbc.com.hk
+852 2996 6621

## Cathy Huang\*, CFA

Associate, Asia Transport  
The Hongkong and Shanghai Banking Corporation Limited  
cathy.m.y.huang@hsbc.com.hk  
+852 2996 4506

## Pramod Doke\*

Associate Bangalore

## No country for bears

The $24^{\text{th}}$ edition of the EM Sentiment Survey Click to view

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

View HSBC Global Investment Research at: https://www.research.hsbc.com

## 1. Our key stock ideas in container shipping sector, ratings, and valuation summary

<table><tr><td rowspan="2">Stock</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">HSBC rating</td><td rowspan="2">Share price</td><td rowspan="2">Target price</td><td rowspan="2">Upside/Downside</td><td rowspan="2">Mkt cap (USDm)</td><td colspan="4">2026e</td><td colspan="2">Share price changes**</td></tr><tr><td>P/B (x)</td><td>P/E (x)</td><td>ROE</td><td>Yield*</td><td>6M</td><td>YTD</td></tr><tr><td>AP Moller Maersk</td><td>MAERSKB DC</td><td>DKK</td><td>Buy</td><td>16,060.00</td><td>19,000.00</td><td>+18.3%</td><td>35,192</td><td>0.6</td><td>31.4</td><td>2.1%</td><td>1.0%</td><td>13%</td><td>13%</td></tr><tr><td>COSCO Shipping-H</td><td>1919 HK</td><td>HKD</td><td>Buy</td><td>13.28</td><td>17.20</td><td>+29.5%</td><td>30,479</td><td>0.7</td><td>8.6</td><td>8.9%</td><td>5.8%</td><td>-1%</td><td>0%</td></tr><tr><td>COSCO Shipping-A</td><td>601919 CH</td><td>CNY</td><td>Buy</td><td>14.00</td><td>18.50</td><td>+32.1%</td><td>30,479</td><td>0.9</td><td>10.4</td><td>8.9%</td><td>4.8%</td><td>-9%</td><td>-8%</td></tr><tr><td>OOIL</td><td>316 HK</td><td>HKD</td><td>Hold</td><td>121.10</td><td>130.00</td><td>+7.3%</td><td>10,200</td><td>0.7</td><td>9.8</td><td>7.7%</td><td>5.1%</td><td>0%</td><td>-1%</td></tr><tr><td>Evergreen Marine</td><td>2603 TT</td><td>TWD</td><td>Buy</td><td>186.50</td><td>255.00</td><td>+36.7%</td><td>12,716</td><td>0.7</td><td>11.4</td><td>6.4%</td><td>4.5%</td><td>7%</td><td>6%</td></tr><tr><td>Hapag Lloyd</td><td>HLAG GY</td><td>EUR</td><td>Reduce</td><td>115.90</td><td>90.00</td><td>-22.3%</td><td>23,138</td><td>1.2</td><td>n/m</td><td>-2.6%</td><td>0.0%</td><td>4%</td><td>1%</td></tr><tr><td>SITC</td><td>1308 HK</td><td>HKD</td><td>Hold</td><td>31.70</td><td>31.00</td><td>-2.2%</td><td>10,963</td><td>4.0</td><td>13.2</td><td>32.4%</td><td>7.7%</td><td>23%</td><td>24%</td></tr></table>

Source: Bloomberg, LSEG Datastream, HSBC estimates. Notes: Share prices at close on 24 June 2026. \*Dividend yield including share buybacks. \*\*Price changes consider dividends paid (if any).

Valuation and risks

<table><tr><td colspan="2"></td><td>Valuation</td><td>Risks</td></tr><tr><td>AP Moller Maersk MAERSKB DC</td><td rowspan="2">Current price: DKK16,060.00Target price: DKK19,000.00Up/downside: +18.3%</td><td rowspan="2">Methodology: Price-to-book multiple (P/B).Assumptions: A 0.72x 2026e P/B (0.25 SD below the average since mid-2011) to 2026e BVPS of USD3,833. After adding back 2026 share buyback yet to be completed, plus a 5% ESG premium for Maersk based on the stronger positioning in its ESG efforts, we have a target price of DKK19,000.00 (all unchanged).Our target price implies c18% upside and we maintain our Buy rating as although cost pressures have increased, we think a delayed Red Sea resumption remains a positive. Ocean profits may gradually normalise as vessel deliveries catch up and disruptions normalise, but we believe stable Terminals and recovering Logistics margins and the ongoing buyback provide downside protection.Parash Jain* | parashjain@hsbc.com.hk | +852 2996 6717</td><td rowspan="2">Downside risksIncrease in competitionSlower-than-expected trade growthWider-than-expected spreads between VLSFO and HSFOScrutiny from regulators curbing market-based pricingStricter environmental regulationsQuicker-than-expected resolution to the Red Sea issueHigher-than-expected costs from the Red Sea disruptionExecution risks from any potential big-ticket M&amp;APotentially higher-than-expected cost from the USTR proposal to levy port fees</td></tr><tr><td>Buy</td></tr><tr><td>SITC 1308 HK</td><td rowspan="2">Current price: HKD31.70Target price: HKD31.00Up/downside: -2.2%</td><td rowspan="2">Methodology: Price-to-book multiple (PB)Assumptions: 3.63x 2026 P/B, 1.3 SD above average since mid-2011, applied to our 2026e average BVPS of USD1.00. We add back a final dividend for 2025 and interim dividend payable in 2026. All assumptions are unchanged. We have a target price of HKD31.00 which implies c2% downside. We maintain our Hold rating as we think the current valuation is fair for SITC, despite its better pricing power and low-cost base.Parash Jain* | parashjain@hsbc.com.hk | +852 2996 6717</td><td rowspan="2">Upside risks:Higher-than-expected economic development in mainland ChinaA speed-up in intra-Asia trade growthA sharp drop in fuel prices; and easing protectionismNarrower-than-expected impacts on intra-Asia trades from the US&#x27;s universal reciprocal tariffsDownside risks:Slower-than-expected economic development in mainland ChinaA slowdown in intra-Asia trade growthA sharp rise in fuel prices and an increase in trade protectionismWider-than-expected impacts on intra-Asia trades from the US&#x27;s universal reciprocal tariffs</td></tr><tr><td>Hold</td></tr><tr><td>Evergreen Marine 2603 TT</td><td>Current price: TWD186.50Target price: TWD255.00Up/downside: +36.7%</td><td>Methodology: Price-to-book multiple (P/B)Assumptions: 0.9x 2026e P/B (average since mid-2011), applied to our 2026 BVPS of TWD261. We do not apply an ESG premium given its relative ESG positioning vs peers (all unchanged). After adding back the FY25 dividend, we have a target price of TWD255.00, which implies c37% upside. We rate the stock Buy as we think Evergreen&#x27;s share price should continue to strengthen as disruption-led spot freight rate momentum continues.Parash Jain* | parashjain@hsbc.com.hk | +852 2996 6717</td><td>Downside risks:Shorter-than-expected congestion and supply chain inefficienciesMilder-than-expected rally in freight ratesWeaker-than-expected consumption demand from world ex-USWeaker-than-expected US retail consumption demand</td></tr></table>

Valuation and risks (cont'd)

<table><tr><td colspan="2"></td><td>Valuation</td><td>Risks</td></tr><tr><td>COSCO Shipping Holding 1919 HK 601919 CH</td><td rowspan="2">Current price:HKD13.28RMB14.00Target price:HKD17.20RMB18.50Up/downside:H: +29.5%A: +32.1%</td><td rowspan="2">Methodology: Price-to-book multiple (P/B).Assumptions: We use 2026 PB multiple of 0.93x, which is 0.5 S.D. below the historical average of 1.15x; and exchange rate of 1.17 based on the HSBC FX team&#x27;s latest end-2026 RMB-HKD forecast. We add back interim dividend for 2026. We arrive at an H-share target price of HKD17.20 (all unchanged). Our target price implies c30% upside and we have a Buy rating on the stock. We think the near-term earnings trajectory and improved industry structure warrant a higher valuation, supported by a clearer shareholder return framework (50% payout over 2026-28e).To derive our A-share target price, we apply a year-to-date average A-H premium of 32% to our H-share target PB multiple to arrive at a target PB of 1.11x. Based on this approach, we arrive at a target price for the A-shares of RMB18.50 (all unchanged), which implies c32% upside. We have a Buy rating on the stock.Parash Jain* | parashjain@hsbc.com.hk | +852 2996 6717</td><td rowspan="2">Downside risks for the A-shares and H-shares:◆ Easing of disruptions and congestion in Europe and the Middle East;◆ trade recession as a result of higher energy prices hitting downstream demand;◆ faster-than-expected demand and freight rate normalisation in 2026-27e;◆ loss of capacity discipline as liners are racing to expand capacity and engage in price competition;◆ and lower-than-expected scrapping.</td></tr><tr><td>H: BuyA: Buy</td></tr><tr><td>Hapag Lloyd HLAG GY</td><td rowspan="2">Current price:EUR115.90Target price:EUR90.00Up/downside:-22.3%</td><td rowspan="2">Methodology: Price-to-book multiple (P/B)Assumptions: 0.9x P/B (0.7 SD below average since mid-2011), applied to our 2026e average BVPS of EUR96.40, after reflecting a 5% ESG premium given its relatively strong ESG positioning among our covered peers and adding back the FY25 dividend (all unchanged). We have a target price of EUR90.00 which implies c22% downside; therefore we maintain our Reduce rating. We think elevated fuel prices are likely to pressure margins and the share price.Parash Jain* | parashjain@hsbc.com.hk | +852 2996 6717</td><td rowspan="2">Upside risks:◆ Longer-than-expected congestion and supply chain inefficiencies◆ Stronger-than-expected rally in freight rates◆ Stronger-than-expected consumption demand from world ex-US◆ Stronger-than-expected US retail consumption demand</td></tr><tr><td>Reduce</td></tr><tr><td>OOIL 316 HK</td><td>Current price:HKD121.10Target price:HKD130.00Up/downside:+7.3%</td><td>Methodology: Price-to-book multiple (P/B)Assumptions: We apply a target PB multiple of 0.70x, average since mid-2011, to our 2026e average BVPS of USD21.03. We do not apply an ESG premium given its relatively fair positioning on ESG efforts across its peer group. All inputs are unchanged.After adding back the dividends payable in 2025 and interim dividend in 2026, we have a target price of HKD130.00, based on a USD-HKD exchange rate of c7.8. Our target price implies c7% upside. We rate the stock Hold. We think current disruption and congestion may keep near-term freight rates elevated.Parash Jain* | parashjain@hsbc.com.hk | +852 2996 6717</td><td>Upside risks:◆ Stronger-than-expected container demand in 2026 driven by potential frontloading◆ More effective capacity discipline than expected◆ Slower-than-expected delivery of new containerships; higher-than-expected scrapping◆ Prolonged disruptions in Red Sea region◆ Higher-than-expected dividend payout from OOIL (we model for 50% in 2026e).Downside risks:◆ Weaker-than-expected container demand in 2026 driven by higher inflation◆ Less effective capacity discipline than expected◆ Faster-than-expected delivery of new containerships◆ Lower-than-expected scrapping◆ Shorter-than-expected disruptions in Red Sea region◆ Lower-than-expected dividend payout from OOIL (we model for 50% in 2026e).</td></tr></table>

2. Global container shipping – valuation comparison summary

<table><tr><td rowspan="2">Company</td><td rowspan="2">Bloomberg ticker</td><td rowspan="2">Ccy</td><td rowspan="2">HSBC rating</td><td rowspan="2">Share price</td><td rowspan="2">Target price</td><td rowspan="2">Mkt cap (USDm)</td><td rowspan="2">Turnover (USDm)</td><td rowspan="2">Free float (%)</td><td colspan="2">P/B (x)</td><td colspan="2">EV/EBITDA (x)</td><td colspan="2">ROE (%)</td><td colspan="2">P/E (x)</td><td colspan="2">Div yield (%)</td><td rowspan="2">Net debt/equity</td><td colspan="4">Share price performance</td></tr><tr><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>1M</td><td>6M</td><td>1Y</td><td>YTD</td></tr><tr><td>AP Moller Maersk</td><td>MAERSKB DC</td><td>DKK</td><td>Buy</td><td>16,060</td><td>19,000</td><td>35,192</td><td>44.9</td><td>51%</td><td>0.6</td><td>0.6</td><td>4.0</td><td>4.8</td><td>2.1%</td><td>0.2%</td><td>31.4</td><td>337.7</td><td>1.0%</td><td>0.1%</td><td>0.0x</td><td>5%</td><td>13%</td><td>41%</td><td>13%</td></tr><tr><td>COSCO Shipping-H</td><td>1919 HK</td><td>HKD</td><td>Buy</td><td>13.28</td><td>17.20</td><td>30,479</td><td>42.5</td><td>94%</td><td>0.7</td><td>0.7</td><td>2.3</td><td>2.7</td><td>8.9%</td><td>6.3%</td><td>8.6</td><td>11.8</td><td>5.8%</td><td>4.2%</td><td>-0.3x</td><td>-9%</td><td>-1%</td><td>4%</td><td>0%</td></tr><tr><td>COSCO Shipping-A</td><td>601919 CH</td><td>CNY</td><td>Buy</td><td>14.00</td><td>18.50</td><td>30,479</td><td>198.5</td><td>36%</td><td>0.9</td><td>0.9</td><td>2.3</td><td>2.7</td><td>8.9%</td><td>6.3%</td><td>10.4</td><td>14.3</td><td>4.8%</td><td>3.5%</td><td>-0.3x</td><td>-4%</td><td>-9%</td><td>-4%</td><td>-8%</td></tr><tr><td>OOIL</td><td>316 HK</td><td>HKD</td><td>Hold</td><td>121.10</td><td>130.00</td><td>10,200</td><td>20.7</td><td>15%</td><td>0.7</td><td>0.7</td><td>2.5</td><td>2.6</td><td>7.7%</td><td>6.7%</td><td>9.8</td><td>10.8</td><td>5.1%</td><td>4.6%</td><td>-0.4x</td><td>-14%</td><td>0%</td><td>-4%</td><td>-1%</td></tr><tr><td>Evergreen Marine</td><td>2603 TT</td><td>TWD</td><td>Buy</td><td>186.50</td><td>255.00</td><td>12,716</td><td>118.7</td><td>75%</td><td>0.7</td><td>0.7</td><td>4.9</td><td>5.1</td><td>6.4%</td><td>5.8%</td><td>11.4</td><td>12.4</td><td>4.5%</td><td>4.1%</td><td>0.0x</td><td>-8%</td><td>7%</td><td>-3%</td><td>6%</td></tr><tr><td>Hapag Lloyd</td><td>HLAG GY</td><td>EUR</td><td>Reduce</td><td>115.90</td><td>90.00</td><td>23,138</td><td>3.2</td><td>14%</td><td>1.2</td><td>1.3</td><td>12.1</td><td>14.3</td><td>-2.6%</td><td>-5.6%</td><td>n/m</td><td>n/m</td><td>0.0%</td><td>0.0%</td><td>0.2x</td><td>3%</td><td>4%</td><td>-7%</td><td>1%</td></tr><tr><td>SITC</td><td>1308 HK</td><td>HKD</td><td>Hold</td><td>31.70</td><td>31.00</td><td>10,963</td><td>19.6</td><td>47%</td><td>4.0</td><td>4.1</td><td>10.4</td><td>11.3</td><td>32.4%</td><td>28.0%</td><td>13.2</td><td>14.8</td><td>7.7%</td><td>6.9%</td><td>-0.2x</td><td>-8%</td><td>23%</td><td>40%</td><td>24%</td></tr></table>

Source: LSEG Datastream, HSBC estimates  
Notes: Latest prices at of close on 24 June 2026. Turnover is based on the average over the past three months. Net debt/equity is as of end-2025. Share price performances include dividends if any.

![](images/36ff0a5d9bc41d80da594cb89fafb67bc520e59dbc0378a331b4bc716d2f89c5.jpg)

# Disclosure appendix

## Analyst Certification

The following analyst(s), economist(s), or strategist(s) who is(are) primarily responsible for this report, including any analyst(s) whose name(s) appear(s) as author of an individual section or sections of the report and any analyst(s) named as the covering analyst(s) of a subsidiary company in a sum-of-the-parts valuation certifies(y) that the opinion(s) on the subject security(ies) or issuer(s), any views or forecasts expressed in the section(s) of which such individual(s) is(are) named as author(s), and any other views or forecasts expressed herein, including any views expressed on the back page of the research report, accurately reflect their personal view(s) and that no part of their compensation was, is or will be directly or indirectly related to the specific recommendation(s) or views contained in this research report: Parash Jain, Deepak Maurya, CFA, Bruce Chu, CFA and Cathy Huang, CFA

## Important disclosures

## Equities

[中间内容因长度限制已省略]

pecified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures". If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB.

© Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.

## Stay connected to our topical and timely thought leadership

![](images/07522f175e3947551cb29e7501be75c699347d81ac0dec7139ad348fc7115724.jpg)

## Download the HSBC Global Investment Research app

From Apple's App Store or Google Play The app features topical and timely curated reports, multimedia, and upcoming events

![](images/9375d814bc7ff76bd7f03a45ae2acc994ea2ed7ac7d3bcd06c4bc930a6cd8a1a.jpg)

## Log on to the Global Investment Research website

To access all reports and videos, visit research.hsbc.com

![](images/272bac2be327143f0c41f6e5a77c388efcfae464dde2eecb97e2b60131eff9fd.jpg)

## Connect with Global Investment Research on LinkedIn

Search #HSBCResearch for free to view insights that can easily be shared with clients and prospects

![](images/0057317b5fb6d9c7066a08b31355827e7ca0643b934ccedbcd50cc015001c065.jpg)

## Subscribe and listen

Under the Banyan Tree by HSBC Global Investment Research on Apple, Spotify or YouTube

The Macro Brief by HSBC Global Investment Research on Apple, Spotify or YouTube

![](images/bd1e265a9d50a9bd6e2fcc9983e872ad4629a45502969c10f305d487cac398b8.jpg)

## Newsletters

Subscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points
"""
