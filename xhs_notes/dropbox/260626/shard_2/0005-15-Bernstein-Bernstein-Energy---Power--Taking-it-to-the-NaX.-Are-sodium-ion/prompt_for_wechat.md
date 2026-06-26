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
Source: Bloomberg, Baiinfo, Bernstein analysis and estimates

# Bernstein Energy & Power: Taking it to the NaX. Are sodium-ion batteries the key to solar baseload power?

Neil Beveridge, Ph.D. +852 2123 2648 neil.beveridge@bernsteinsg.com

Nikhil Nigania +91 226 842 1414 nikhil.nigania@bernsteinsg.com

Deepa Venkateswaran, ACA +44 20 7676 6990 deepa.venkateswaran@bernsteinsg.com

Guillaume Delaby +33 1 42 13 62 29 guillaume.delaby@bernsteinsg.com

Bob Brackett, Ph.D. +1 917 344 8422 bob.brackett@bernsteinsg.com

## Taking it to the NaX. Are sodium-ion batteries the key to solar base load power?

Our recent travels in Europe have highlighted two things. Firstly, how hot and sunny it is. In Germany this month roughly 25% of power generation came from solar while in Spain solar share of power generation reached as high as 70% on June 6th. Secondly, client interest in energy storage and particularly sodium-ion batteries has been eye-opening. Many will be aware sodium-ion batteries are the latest technology breakthrough in the battery market. As Elon Musk likes to point out, making batteries out of sodium and iron which are two of the most abundant elements in the earth's crust (unlike lithium and cobalt), seems like a smart thing to do. The challenge up to now is that making a sodium-ion battery has been expensive. Not because of the cost of the materials, but because of the complexity of the cathode and anode technology. This changed last year with a rapid reduction in the cost of sodium-ion cathodes. While sodium-ion batteries are still as expensive as LFP, all indications suggest they will get cheaper as battery makers scale up production. Robin Zeng, the Chairman of CATL, believes that the cost of sodium-ion batteries will fall to US\$50/kWh, which is lower than the US\$80-90/kWh for LFP and almost half the cost of NMC batteries at over US\$100/kWh.

EXHIBIT 1: Sodium-ion battery prices are expected to match LFP in 2026 and gain further cost advantage thereafter  
![](images/ae747c24b51907e2f11e7cc07ab28ac3be1c96cb1afcdd022424401a6c21a156.jpg)  
Estimated for 2026-2030

For polyanion-based sodium-ion batteries Source: Baiinfo, Bernstein analysis

Given that industrial grade sodium costs around US\$5000/t compared to lithium carbonate at over US\$20,000/t, the cost savings are obvious. But the advantages of sodium-ion batteries go beyond just cost. Firstly, the number of cycles that can be achieved with sodium-ion batteries are twice that of LFP. While an LFP battery may be capable of 6,000-8,000 cycles, a Na-ion battery can achieve 15,000 cycles. This means it is possible to charge and discharge a battery twice a day for 20 years, allowing them to be paired directly with solar and wind over the life of the project with no replacement needed. It also means that on a US \$/kWh/cycle basis, Na-ion could be one third the cost of LFP. Secondly, Na-ion batteries are lower temperature, which means that safety performance is better with thermal runaway limited to temperatures of around 200deg C. Thirdly, Na-ion batteries have better performance at low temperatures. According to CATL, energy retention is greater than $92\%$ at temperatures as low as -20deg C. Finally, while Na has a lower energy density than Li, the overall energy density of Na-ion batteries is getting close to LFP. The CATL Naxtra battery has an energy density of $185\mathrm{Wh/kg}$ at the pack level, which approaches that of LFP (190-210Wh/kg) making Na-ion batteries a serious challenger in the more price-sensitive mass vehicle market.

EXHIBIT 2: Based on the spot battery component prices, the cost of sodium-ion battery declined 15% yoy from US\$66/kWh to US\$55/kWh now  
![](images/7bcd8c2c8ac168d6e09d5b99aa4eafd290b05f131adad2cf1380a3349070d9c1.jpg)

The key benefit which Na-ion batteries bring is lower cost. We believe that this can significantly enhance the penetration of renewable energy and substantially increase the total addressable market for batteries. As everyone knows, solar and wind power is cheap, but not when the sun doesn't shine or the wind doesn't blow. The only way to make renewable power cheaper and more effective is to reduce energy storage costs. While lithium-ion batteries are the obvious way to do this, the problem is the high cost of storage. In 2020, it was not uncommon for a BESS to cost US \$500/kWh. This means that 1kW of capacity with 4 hour storage would cost US\$2000, which is almost the same cost as a combined cycle gas turbine plant (US\$2000/kW). Today, the cost of ESS has fallen along with LFP battery costs to around US\$150/kW (battery plus inverter and balance of plant). At the same time, given the demand growth for gas turbines, the capital cost of a gas-fired power plant has increased to as high as US\$4000/kW. Assuming

US $W1000/kW$ for a solar module, this means that solar plus 20 hours of battery storage (20 x US $150/kW = US3000/kW$ ) could cost as much as a combined cycle gas fired power plant CCGT(US $4000/kW$ ). But assuming that the cost of Na-ion batteries falls to as low as US $50/KW$ , then solar plus battery storage could be even cheaper. It could be possible in the near future that the cost of solar plus 48 hours of Na-ion storage could be as cheap as a gas-fired power plant. On our analysis, the break-even gas price for solar (US $550/kW$ ) paired with a Na-ion ESS system (US $100/KWh$ ) and a CCGT US $2,500/kW$ could be as low as US $5/mscf$ . At a CCGT with a cost of US $4000/kW$ the breakeven could be as low at US $2/mscf$ . This is not to say that 12 hours of storage would suffice in every location, but the cheaper battery storage becomes the higher the penetration could be.

EXHIBIT 3: Solar with Na-ion storage could compete with CCGT at \$2-5/mmcf gas price  
Levelized cost of electricity (US\$/MWh)
Solar + Storage (12hrs) vs Combined-Cycle Gas Plant  
![](images/fbb31c4bb76d807cfb17bfaf7340857a4ee4b0ce372ac8efc3af43aa55ae4894.jpg)  
Source: Bernstein analysis

Already in the UAE, Masdar is developing the world first baseload power project with solar and storage. In the project, solar will be paired with 19GWh of battery storage to provide continuous base load solar power for a 1GW of power with a 99.7% power reliability. As battery storage costs come down, longer duration solar plus battery projects could emerge as more serious competitors to gas for baseload power. This could not only expand the penetration of solar and wind in the grid, but it will help lower power prices and could lead to a significant expansion of battery storage. As of last year there was almost 5,000GW of combined installed solar and wind capacity worldwide.

EXHIBIT 4: Assuming every GW of solar and wind capacity is backed up by 1GW of ESS with 10 hours duration, this could amount to a cumulative demand of 100,000GWh  
![](images/3057c21cce8504f9512b63e1b34f260b4144153c1678e33876c6558549d9c4e6.jpg)  
Source: Bloomberg, Bernstein estimates and analysis

By 2030, we think this number could reach close to 10,000GW. Assuming every GW of solar and wind capacity is backed up by 1GW of battery capacity with a duration of 10 hours this could amount to a cumulative demand of 100,000GWh. This is two orders of magnitude more than the 700GWh of cumulative installed battery capacity that exists today and would imply significant

upside to the 1000GWh of annual capacity additions we expect this year.

The key investment implication is that Na-ion batteries could enable a step change reduction in energy storage costs allowing solar and wind to not only increase their penetration in the grid but also

to compete more effectively with gas for baseload power supply. This is positive for renewables supply chains but in particular CATL which is the industry leader in Na-ion battery technology and with their recently announced TENER sodium-ion storage system, likely to be an early winner.

## BERNSTEIN TICKER TABLE

<table><tr><td colspan="3"></td><td colspan="2">24 Jun 2026</td><td>TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>300750.CH (CATL)</td><td>O</td><td>CNY</td><td>395.36</td><td>800.00</td><td>17.5%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>24.5</td><td>18.0</td><td>13.7</td></tr><tr><td>3750.HK (CATL)</td><td>M</td><td>HKD</td><td>721.50</td><td>770.00</td><td>88.8%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>38.8</td><td>28.6</td><td>21.8</td></tr><tr><td>051910.KS (LG Chem)</td><td>M</td><td>KRW</td><td>298,000</td><td>298,000</td><td>0.9%</td><td colspan="2">KRW(13,258.70)</td><td>3,030.56</td><td>27,968</td><td>(22.5)</td><td>98.3</td><td>10.7</td></tr><tr><td>373220.KS (LGES)</td><td>M</td><td>KRW</td><td>366,000</td><td>347,000</td><td>(16.5)%</td><td>KRW</td><td>(5,308.10)</td><td>1,811.04</td><td>9,452.97</td><td>(69.0)</td><td>202.1</td><td>38.7</td></tr><tr><td>006400.KS (SDI)</td><td>M</td><td>KRW</td><td>490,500</td><td>520,000</td><td>140.3%</td><td>KRW</td><td>(9,933.80)</td><td>2,099.51</td><td>18,376</td><td>(49.4)</td><td>233.6</td><td>26.7</td></tr><tr><td>247540.KS (EcoPro BM)</td><td>U</td><td>KRW</td><td>151,800</td><td>140,000</td><td>4.7%</td><td>KRW</td><td>403.00</td><td>854.00</td><td>1,963.00</td><td>376.7</td><td>177.8</td><td>77.3</td></tr><tr><td>300274.CH (Sungrow)</td><td>O</td><td>RMB</td><td>154.80</td><td>185.00</td><td>96.0%</td><td>RMB</td><td>6.55</td><td>8.22</td><td>9.33</td><td>23.6</td><td>18.8</td><td>16.6</td></tr><tr><td>002466.CH (Tianqi Lithium)</td><td>O</td><td>CNY</td><td>66.13</td><td>80.00</td><td>70.5%</td><td>CNY</td><td>0.28</td><td>3.90</td><td>7.75</td><td>234.3</td><td>16.9</td><td>8.5</td></tr><tr><td>9696.HK (Tianqi Lithium)</td><td>O</td><td>HKD</td><td>43.32</td><td>65.00</td><td>18.2%</td><td>CNY</td><td>0.28</td><td>3.90</td><td>7.75</td><td>133.3</td><td>9.6</td><td>4.9</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,996.75</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action. Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

\- Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within $+/-10$ pp

• Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as 'Feature' (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Ban

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
