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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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
<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Joseph Moore</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joseph.Moore@morganstanley.com</td><td>+1 212 761-7516</td></tr><tr><td colspan="2">Ella Tulchinsky</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ella.Tulchinsky@morganstanley.com</td><td>+1 212 761-2222</td></tr><tr><td colspan="2">Nicole Kozhukhov</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Nicole.Kozhukhov@morganstanley.com</td><td>+1 212 761-1636</td></tr><tr><td colspan="2">Mason Wayne</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Mason.Wayne@morganstanley.com</td><td>+1 212 761-6012</td></tr><tr><td colspan="2">Shane Brett</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Shane.Brett@morganstanley.com</td><td>+1 212 761-1022</td></tr></table>

# Weekly: Earnings Week 8 MU & CBRS Preview

Raising Micron numbers again as shortages continue to intensify; higher capex and limited LTA disclosure shouldn't hold the story back. Separately we see CBRS posting in line #s for its first public qtr, with visibility into the coming ramp.

CBRS (OW, reporting after the market close on Tuesday, June 23rd): CBRS will report its first quarter as a public company, and while we are not expecting a major surprise, we remain constructive on what we view as a differentiated architecture with significant upside. With large take or pay agreements already in place, the near term story remains centered on execution rather than demand. We continue to view the pace of capacity deployment as the key driver of revenue and gross margin upside, and remain focused on management's progress toward bringing the initial 250MW tranche online, which we currently expect by mid 2027. Longer term, the more important question is whether the Wafer Scale Engine proves to be a durable competitive advantage. The company will need to demonstrate that the technology delivers meaningful value to customers and can scale economically. For now, however, we believe the investment debate is primarily about execution, and we remain constructive.

We model core revenue of \$180 million and core gross margin of 44% for the March quarter, in line with consensus expectations. Looking ahead, we expect core revenue to remain roughly flat in the June quarter while core gross margin declines to 24%, driven by G42 rent back arrangements that support the initial capacity ramp. We expect these arrangements to remain a drag on cloud margins until roughly mid 2027. On a GAAP basis, we forecast revenue of \$182 million in March and \$153 million in June, with the difference between GAAP versus core revenue reflecting mostly warrant related contra revenue. While we think the compute ramp may be somewhat messy near term, with pressure on margins and warrant related costs, we believe these headwinds are well understood by investors. Ultimately, what we are playing for is a differentiated architecture with leadership in one of the fastest growing segments of AI infrastructure, where successful execution could unlock significant upside beyond current expectations.

MU (OW, reporting after market closes on Wednesday, June 24th): Raising numbers again as demand continues to outstrip supply in memory and especially in DRAM, incremental commentary on SCAs (strategic customer agreements) a key focus. Micron's initial guidance for May was revenue growth of 40% q/q, implying ASP increases in both DRAM/NAND of 30-35% or so q/q. Micron has since said conditions are trending better but has not provided a numerical update for investors. We model DRAM ASP's up 45% vs 40% prior, and NAND up 50% vs 35% prior, with third party forecasts calling for \~60% increases in C2Q for DRAM and \~75% for NAND; we don't expect that to come as a surprise to investors. Our

## SEMICONDUCTORS

North America
Industry View
Attractive

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

resulting EPS of \$21.31 compares to consensus at \$20.57. For August we expect pricing up in the 20% range for both DRAM and NAND, with an upward bias to that number as our checks continue to point to very strong market conditions, although negotiations have not yet concluded and but we would expect Micron to remain conservative at the outset.

More important than strong results will be proofpoints on the durability of the current cycle, especially in light of downward LPDDR content adjustments for Rubin. To us that comes back to what are always the two key memory variables, demand and supply. On the demand side the company is unlikely to comment specifically on Rubin, but will likely emphasize that customers in all markets are being forced to make difficult decisions with regards to their volumes and content; to us that's a sign of an enduring shortage and think management at MU will make a similar case. As far as supply, the Tongluo acquisition from PSMC (covered by Daniel Yen) may start to see WFE deliveries quicker than initial expectations, putting an upward bias on current FY capex vs guidance for "above \$25bn" - we raise Aug quarter from \$8bn to \$10bn (FY from \$25bn to \$27bn). Supply growth in DRAM overall continues to come in above out expectations, and will accelerate next year given capital spending this year. But the levels are still much lower than headline WFE would suggest, with construction timelines, HBM trade ratio inputs, and lower node migration efficiency continuing to limit the speed of the supply response and we continue to see q/q bit shipment increases still in the mid single digits vs demand that seems to grow much faster.

What about LTAs? A quarter ago Micron disclosed signing a five year SCA (strategic customer agreement), but with limited information on the terms and sizing of relevant financial commitments. We think Micron may announce the closing of additional deals, but wouldn't necessarily expect more clarity on the terms - as they are likely in conversations with multiple customers and don't want to tip their hand. We think these deals are important for market sentiment around the case for further multiple expansion, and the stock may go down if there's limited new information. But in that we would be looking to add to positions as new disclosures don't change what we know - which is that customers see DRAM as increasingly tight over a multiyear time horizon – something not priced in at 9.3x our new FY27 EPS, in our view.

## Preview to earnings

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Cerebras Systems CBRS.O</td></tr><tr><td>Core Revenue</td><td>— In-line</td><td>— Largely unchanged</td></tr></table>

\- While we are not expecting significant upside, we remain constructive on what we view as a differentiated architecture with significant upside.

\*Likely impact to consensus EPS is for the next 12 months

Source: Company data, MS

## Cerebras Earnings Preview

The company is scheduled to report after the market close on Tuesday, June 23rd.

CBRS will report its first quarter as a public company, and while we are not expecting a major surprise, we remain constructive on what we view as a differentiated architecture with significant upside. With large take or pay agreements already in place, the near term story remains centered on execution rather than demand. We continue to view the pace of capacity deployment as the key driver of revenue and gross margin upside, and remain focused on management's progress toward bringing the initial 250MW tranche online, which we currently expect by mid 2027. Longer term, the more important question is whether the Wafer Scale Engine proves to be a durable competitive advantage. The company will need to demonstrate that the technology delivers meaningful value to customers and can scale economically. For now, however, we believe the investment debate is primarily about execution, and we remain constructive.

We model core revenue of \$180 million and core gross margin of 44% for the March quarter, in line with consensus expectations. Looking ahead, we expect core revenue to remain roughly flat in the June quarter while core gross margin declines to 24%, driven by G42 rent back arrangements that support the initial capacity ramp. We expect these arrangements to remain a drag on cloud margins until roughly mid 2027. On a GAAP basis, we forecast revenue of \$182 million in March and \$153 million in June, with the difference between GAAP versus core revenue reflecting mostly warrant related contra revenue. While we think the compute ramp may be somewhat messy near term, with pressure on margins and warrant related costs, we believe these headwinds are well understood by investors. Ultimately, what we are playing for is a differentiated architecture with leadership in one of the fastest growing segments of AI infrastructure, where successful execution could unlock significant upside beyond current expectations.

Exhibit 1: CBRS: MS estimates  
MS Estimates

<table><tr><td colspan="5">Figures in $ MMs</td></tr><tr><td></td><td>F1Q26E</td><td>F2Q26E</td><td>FY26E</td><td>FY27E</td></tr><tr><td>Core Rev</td><td>180.4</td><td>180.2</td><td>831.4</td><td>2,694.8</td></tr><tr><td>Q/Q Change</td><td>5.2%</td><td>-0.2%</td><td></td><td></td></tr><tr><td>GAAP Rev</td><td>182.8</td><td>153.0</td><td>792.4</td><td>3,174.3</td></tr><tr><td>Q/Q Change</td><td>6.6%</td><td>-16.3%</td><td></td><td></td></tr><tr><td>Core GM</td><td>43.8%</td><td>24.2%</td><td>29.5%</td><td>51.1%</td></tr><tr><td>Non-GAAP EPS</td><td>$ (0.21)</td><td>$ (0.40)</td><td>$ (1.22)</td><td>$ 0.88</td></tr></table>

Source: MS

## Micron Earnings Preview

The company is scheduled to report after the market close on Wednesday, June 24th.

Raising numbers again as demand continues to outstrip supply in memory and especially in DRAM, incremental commentary on SCAs (strategic customer agreements) a key focus. Micron's initial guidance for May was revenue growth of 40% q/q, implying ASP increases in both DRAM/NAND of 30-35% or so q/q. Micron has since said conditions are trending better but has not provided a numerical update for investors. We model DRAM ASP's up 45% vs 40% prior, and NAND up 50% vs 35% prior, with third party forecasts calling for \~60% increases in C2Q for DRAM and \~75% for NAND for we don't expect that to come as a surprise for investors. Our resulting EPS of \$21.31 compares to consensus at \$20.57. For August we expect pricing up in the 20% range for both DRAM and NAND, with an upward bias to that number as our checks continue to point to very strong market conditions, although negotiations have not yet concluded and but we would expect Micron to remain conservative at the outset.

More important than strong results will be proofpoints on the durability of the current cycle, especially in light of downward LPDDR content adjustments for Rubin. To us that comes back to what are always the two key memory variables, demand and supply. On the demand side, the company is unlikely to comment specifically on Rubin, but will likely emphasize that customers in all markets are being forced to make difficult decisions with regards to their volumes and content; to us that's a sign of an enduring shortage and think management at MU will make a similar case. As far as supply, the Tongluo acquisition from PSMC (covered by Daniel Yen) may start to see WFE deliveries quicker than initial expectations, putting an upward bias on current FY capex vs guidance for "above \$25bn" - we raise Aug quarter from \$8bn to \$10bn (FY from \$25bn to \$27bn). Supply growth in DRAM overall continues to come in above our expectations, and will accelerate next year given capital spending this year. But the levels are still much lower than headline WFE would suggest, with construction timelines, HBM trade ratio inputs, and lower node migration efficiency continuing to limit the speed of the supply response and we continue to see q/q bit shipment increases still in the mid single digits vs demand that seems to grow much faster.

What about LTAs? A quarter ago Micron disclosed signing a five year SCA (strategic customer agreement), but with limited information on the terms and sizing of relevant financial commitments. We think Micron may announce the closing of additional deals, but wouldn't necessarily expect more clarity on the terms - as they are likely in conversations with multiple customers and don't want to tip their hand. We think these deals are important for market sentiment around the case for further multiple expansion, and the stock may go down if there's limited new information. But in that we would be looking to add to positions as new disclosures don't change what we know – which is that customers see DRAM as increasingly tight over a multiyear time horizon – something not priced in at 9.3x our new FY27 EPS, in our view.

Details on the May quarter: We model revenue of \$36.454bn (up 52.8% q/q and 291.9% y/y), above the Street at \$35.555bn. By segment, we model DRAM sequential bit shipments to increase 5.0% q/q and average selling prices to increase 45.0%; and NAND sequential bit shipments to rise 4.0%, with prices up 50.0%. Our gross margin estimate of

83.1% is above the Street at 81.7%, and our EPS estimate of \$21.31 is above the Street at \$20.57.

Outlook on August quarter: We model revenue of \$43.328bn (up 18.9% q/q and 282.9% y/y), ahead of the Street at \$42.688bn. By segment, we forecast DRAM sequential bit shipments to increase by 2.0%, and prices up 15.0%; and NAND bit shipments to increase 4.0%, with prices increasing by 20.0%. We forecast gross margin to come in at 85.1%, ahead of the street at 82.3%, and our EPS estimate of \$26.01 is also ahead of the Street at \$25.00.

Exhibit 2: MU: MS vs. Cons  
MS vs. Consensus

<table><tr><td colspan="9">Figures in $ MMs</td></tr><tr><td rowspan="2"></td><td colspan="2">F3Q26E</td><td colspan="2">F4Q26E</td><td colspan="2">CY2026E</td><td colspan="2">CY2027E</td></tr><tr><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td></tr><tr><td>Revenues</td><td>36,454</td><td>35,555</td><td>43,328</td><td>42,688</td><td>151,954</td><td>141,640</td><td>220,827</td><td>202,654</td></tr><tr><td>Q/Q Change</td><td>52.8%</td><td>49.0%</td><td>18.9%</td><td>20.1%</td><td></td><td></td><td></td><td></td></tr><tr><td>GMs</td><td>83.1%</td><td>81.7%</td><td>85.1%</td><td>82.3%</td><td>83.3%</td><td>79.5%</td><td>86.4%</td><td>78.3%</td></tr><tr><td>EPS</td><td>$ 21.31</td><td>$ 20.57</td><td>$ 26.01</td><td>$ 25.00</td><td>$ 86.99</td><td>$ 80.46</td><td>$ 128.04</td><td>$ 116.57</td></tr></table>

Source: FactSet, MS estimates

## Risk Reward – Micron Technology Inc. (MU.O)

See multiple quarters of upward revisions, with AI driving a higher multiple

## PRICE TARGET \$1,050.00

\~29.5x through-cycle earnings of US \$35.00, a premium to history reflecting new opportunities in AI, in-line with broader semis.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/d5e5ada9df81ab6e5bb44bdaad7a8acaa54a11c4f25d7eca7c01701c5dff42ae.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/23ddd70a2f3c6574ab39d2b052685e332e337b57f1918dca571a496df0fb6198.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 18 Jun 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## OVERWEIGHT THESIS

\- DRAM fundamentals are in uncharted territory, and should continue to improve as datacenter/AI markets continue their upward trajectory
- Execution on AI is underappreciated, and we expect Micron to maintain HBM share in CY26 vs the competition. Supporting margins and driving a higher multiple than prior cycles
- Cycle longevity will be key, and S/D may stay tight for 2-3 more years

![](images/040e21ef14ce902249ba05d643171b7ec5c9f87f476e862fa829aa6d1c7f63cd.jpg)  
Source: Refinitiv, MS

## Risk Reward Themes

New Data Era: Positive
Secular Growth: Positive
View descriptions of Risk Rewards Themes here

## BULL CASE

\$1,650.00

## 33x through-cycle earnings of US\$50

Gross margin improvement continues, driven by scale, AI mix, and cost improvements in new products. Pricing pressure alleviates as demand sustainably moves above supply driven by HBM's wafer intensity, a product category where MU cements performance leadership on future products.

## BASE CASE

## \$1,050.00 BEAR CASE

## \~29.5x through-cycle earnings of US\$35

Our through-cycle earnings estimate of US\$35.00 is a small premium to our new FY21-FY28 average (\$34) as we continue to assume peaks and valleys in earnings over time. Our 29.5x multiple reflects the market's enthusiasm for the AI opportunity, and at the midpoint of the semis group

\$675.00

## 27x through-cycle earnings of US\$25.00

Memory begins to enter a downturn in early 2027. As the strength attributed to demand in the early part of the year ended up being inventory build at customers. Multiple compresses severely after an underwhelming peak

## Risk Reward – Micron Technology Inc. (MU.O)

## KEY EARNINGS INPUTS

<table><tr><td>Drivers</td><td>Oct 2025</td><td>Oct 2026e</td><td>Oct 2027e</td><td>Oct 2028e</td></tr><tr><td>GAAP Revenue ($, mm)</td><td>37,378</td><td>117,286</td><td>211,737</td><td>191,967</td></tr><tr><td>Non Gaap Gross Margin (%)</td><td>40.9</td><td>79.1</td><td>86.3</td><td>81.8</td></tr><tr><td>Non-GAAP EPS ($)</td><td>8.29</td><td>64.37</td><td>122.05</td><td>105.91</td></tr><tr><td>Inventory ($, mm)</td><td>8,355</td><td>8,564</td><td>10,152</td><td>12,393</td></tr><tr><td>DOI</td><td>133.7</td><td>123.5</td><td>124.2</td><td>126.2</td></tr></table>

## INVESTMENT DRIVERS

\- Improved pricing and demand strength drive earnings growth

## GLOBAL REVENUE EXPOSURE

<table><tr><td rowspan="8"></td><td>0-10%</td><td>APAC, ex Japan, Mainland China and India</td></tr><tr><td>0-10%</td><td>India</td></tr><tr><td>0-10%</td><td>Japan</td></tr><tr><td>0-10%</td><td>MEA</td></tr><tr><td>0-10%</td><td>Mainland 

[中间内容因长度限制已省略]

o a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/18/2026)</td></tr><tr><td>Joseph Moore</td><td></td><td></td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$537.37</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$24.39</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$59.00</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$69.97</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$90.46</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$434.46</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$417.07</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$411.35</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$234.71</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$85.83</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$133.99</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$56.55</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$310.58</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$99.77</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$1,133.99</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$24.02</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$210.69</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$313.27</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>E (05/11/2025)</td><td>$121.62</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$98.42</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>U (02/10/2026)</td><td>$226.11</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$2,184.75</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$158.23</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$219.75</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$72.45</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$322.86</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$57.41</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$439.46</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$387.39</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$455.51</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
