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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Bernstein`。标题格式建议：`# Bernstein：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Asia Tech Hardware

# Asia Tech Hardware: Insights from a 15-year balance sheet & cash flow analysis; Chroma ATE and Sunny Optical model update

![](images/4a0144c501b5ba7a7e64ee7895810bdff2ca145cc9f3bd04ee8a60855a0f28e6.jpg)

Alex Wang, CFA

+852 2123 2613

alex.wang@bernsteinsg.com

![](images/40eb60b1abfb33f1b9932e46c99cb85df29a3e4b04de1bf91efcb9ad9291cc0c.jpg)

Ethan Xu

+852 2123 2634

ethan.xu@bernsteinsg.com

![](images/a0fc3b3e3eb0a57ae3c9b3ffe63ddf4bedcfc322555e983ea910279e28a65d60.jpg)

Shirley Yang, CFA

+852 2123 2660

shirley.yang@bernsteinsg.com

Following our 2025 balance sheet & cash flow deep dive, we update analysis across our coverage with a focus on business models, profitability, solvency, and efficiency.

AI demand is driving a sharp ROE upcycle, with AI-exposed names significantly outperforming consumer electronics peers. Chroma, Delta, and Quanta are all likely reaching 30%+ ROE in 2026E, and we expect Unimicron's ROE to recover from previous cyclical trough. In contrast, consumer names (Luxshare, Largan, Sunny) are set to improve more gradually to mid-teens to low-20% ROE, reflecting the nascent contribution of AI businesses. 3-year DuPont analysis shows Largan's high \~40% NPM is offset by low leverage and asset turnover (cash-heavy balance sheet). Chroma leads in both ROE and ROIC, supported by structurally high margins and low capital intensity. In PCB supply chain, Japanese leaders' dominance in raw material doesn't yield outstanding ROIC, likely due to a limited AI revenue mix. Server-exposed firms (Elite, Gold Circuit, WUS, Victory Giant; all not covered)) show higher ROIC.

Balance sheets remain strong across coverage: most companies maintain net cash positions, with stable to declining D/E ratios, except Quanta where leverage is rising with AI server expansion. Cash conversion cycles are generally under 120 days, reflecting solid operational efficiency and bargaining power; Chroma is an outlier due to longer inventory and qualification cycles. For capex intensity, Unimicron and Largan have demonstrated relatively high capex levels, driven by strong demand in PCB markets and Apple's stringent requirements for lens manufacturing equipment, respectively. On shareholder returns, Quanta and Chroma lead with 75–85% payout ratios, while none of our covered companies have established regular share buyback plans.

Model update: for Chroma, we model sales/operating profit CAGR of 46%/65% through 2028. We raise topline estimates meaningfully on surging AI datacenter power demand, ESS recovery, and semi/photonics growth. ATS revenue is projected to grow 80%/45% in 2026/2027 on AIDC power testing, while SLT revenue should rise \~80% in 2026 and reach record levels in 2027 on next-gen platforms for Rubin Ultra and Google. For CPO, we model Chroma's TAM to be NT\$5B+ in 2027 (mainly from insertion 3), and to likely contribute to 7% of company revenue. Our 2026-27 EPS are above consensus. We raise our price target to NT\$2,750 (38x P/E unchanged) based on 2027-28 avg. EPS estimate of NT\$72.4 (vs. old 2027 EPS NT\$43.7). Outperform.

For Sunny Optical, we forecast a 12% / 19% revenue / EPS CAGR over 2025-28, We raise 2027-28 revenue forecasts on iPhone camera module share gains. While we lower GM estimates due to memory cost pressure in 2026, we expect it to recover by \~1ppt in 2027. Communication optics remains early-stage; further updates expected at Investor Day and 1H26 results (CPO optics primer). Increasing target P/E to 18x from 17x on potential Apple camera module share gain and rolling forward to 2027 EPS of RMB4.5 (vs. prior 2026-27 avg. EPS of RMB3.9), we raise price target to HK\$94. Outperform.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">17 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>2308.TT (Delta)</td><td>O</td><td>TWD</td><td>2,155.00</td><td>2,620.00</td><td>400.7%</td><td>TWD</td><td>23.09</td><td>37.09</td><td>58.40</td><td>93.3</td><td>58.1</td><td>36.9</td></tr><tr><td>2360.TT (Chroma ATE)</td><td>O</td><td>TWD</td><td>2,230.00</td><td>2,750.00</td><td>479.8%</td><td>TWD</td><td>27.50</td><td>41.39</td><td>63.61</td><td>81.1</td><td>53.9</td><td>35.1</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>1,660.00</td><td></td><td></td><td></td><td>33.22</td><td>43.66</td><td></td><td></td><td></td></tr><tr><td>2382.TT (Quanta)</td><td>U</td><td>TWD</td><td>374.00</td><td>250.00</td><td>(12.7)%</td><td>TWD</td><td>18.91</td><td>21.07</td><td>23.08</td><td>19.8</td><td>17.7</td><td>16.2</td></tr><tr><td>3008.TT (Largan)</td><td>O</td><td>TWD</td><td>5,145.00</td><td>5,150.00</td><td>71.3%</td><td>TWD</td><td>158.08</td><td>187.55</td><td>208.38</td><td>32.5</td><td>27.4</td><td>24.7</td></tr><tr><td>002475.CH ( Luxshare )</td><td>O</td><td>CNY</td><td>67.32</td><td>86.00</td><td>61.2%</td><td>CNY</td><td>2.26</td><td>2.66</td><td>3.45</td><td>29.8</td><td>25.3</td><td>19.5</td></tr><tr><td>3037.TT (Unimicron)</td><td>O</td><td>TWD</td><td>988.00</td><td>990.00</td><td>836.1%</td><td>TWD</td><td>4.36</td><td>14.06</td><td>25.10</td><td>226.5</td><td>70.3</td><td>39.4</td></tr><tr><td>2382.HK (Sunny Optical)</td><td>O</td><td>HKD</td><td>79.35</td><td>94.00</td><td>(24.3)%</td><td>CNY</td><td>4.25</td><td>3.44</td><td>4.52</td><td>16.1</td><td>19.9</td><td>15.2</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>76.00</td><td></td><td></td><td></td><td>3.39</td><td>4.46</td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,032.93</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD  
O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Delta Electronics (model): We rate Delta Electronics Outperform, with PT = NT\$2,620.00.

Chroma ATE (model): We rate Chroma ATE Outperform, with PT = NT\$2,750.00.

Quanta Computer (model): We rate Quanta Computer Underperform, with PT = NT\$250.00.

Unimicron Technology (model): We rate Unimicron Technology Outperform, with PT = NT\$990.00.

Luxshare Precision (model): We rate Luxshare Precision Outperform, with PT = RMB86.00.

Sunny Optical (model): We rate Sunny Optical Outperform, with PT = HK\$94.00.

Largan Precision (model): We rate Largan Precision Market-Perform, with PT = NT\$5,150.00.

## Table Of Contents

Profitability....3

Return on equity (ROE)....3

Return on invested capital (ROIC; including cash in the invested capital)....7

Solvency....11

Operational efficiency....12

Capital Expenditure and depreciation....16

Shareholder return....18

Model update....19

Chroma ate (OP, PT=NT\$2,750.00)....19

Sunny Optical (OP, PT=HK\$94.00) 23

## DETAILS

## PROFITABILITY

## RETURN ON EQUITY (ROE)

The trend of ROE among companies reflects broader sector trends and cycles, and individual company competitiveness in each market (Exhibit 1):

\- Equipment supplier: Chroma's ROE has increased over the past 15 years primarily driving by its rising profitability. The company's NPM has risen from 12% in 2010 to 20%+ in 2021, partially attributed to the divestment of its low-margin material trading segment in 2022 (c. 15% of revenue in 2021). The ROE further increased to 40%+ starting from 2025. This is attributed to its ability to capitalize on strong demand from SLT and photonics testers for AI chips & optical transceiver, and its expertise in AI power testers. We project an 46%/65% CAGR for revenue/operating profit in 2025–28, fueled by the robust AI demand (for both semi and power testers) and significant operating leverage (more details are available in Model Update Section).

\- PCB supplier: Unimicron's ROE has been volatile over the past 15 years, reflecting the fluctuation in the HDI and substrate markets. The overall PCB market saw sluggish demand in 2010\~2016 due to declining PC market and FX headwind. Early investment for ABF substrate and intensifying competition on Apple HDI business further impact Unimicron's financial performance. Despite these challenges, its ROE began recovering in 2017 and saw a surge in 2021-22, due to severe shortage of ABF substrate. Although the market turned to oversupply post-COVID, the capacity digestion was over and ABF market turned tight in 2H25 due to rising demand from both AI accelerators and CPU this year. As we model Unimicron's gross margin to see a strong recovery from mid-teens in 2025 to mid-30s by 2028, ROE should rise from 7% last year to 30%+ (1Q26 PCB market update & Unimicron model update).

\- Power/cooling supplier: Prior to 2025, Delta Electronics' ROE fluctuate between mid-teens % to low-20s amid market volatility across consumer electronics, industrial and server. In 2014-18, Delta faced challenges with its OPM decreased from 12% to 7% and ROE dropping from 21% to 14% in the same period. During this period, the company has acquired Eltek (Telecom power), and VIVOTEK (building automation), resulting in a 6% CAGR in revenue. However, challenges such as pricing war in PC power electronics, rising material cost, slower-than-expected cost synergies from acquisition, and further investment in EV and factory automation have weighed on profitability. Since 2025, 40% of Delta's revenue comes from AI datacenter across different power components and cooling solutions. We expect its ROE to rise from 24% to 40%+ in 2025-26, driven by the accelerated revenue and profitability growth from surging AI demand (Delta Electronics 1Q26: adding capacity for long-term AI demand. PT raise to NT\$2,620).

- ODMs: Luxshare's ROE was stable in recent years as its diversification effort offset the slower growth in consumer electronics market. Management also follows a disciplined M&A strategy with a target of 20% and above ROE for acquired assets over the long term. We model its ROE to trended up to 24% as AI server components bear fruit and newly acquired Leoni business becomes more profitable (Luxshare deep dive: the Next AI Server Winner; PT raised to RMB 86, Outperform). As world's largest ODM for the PC market, Quanta's financial have been very much relied on the PC market before Gen-AI wave. The PC market downturn from 2011 to 2016 negatively impacted Quanta's ROE, but the surge in PC shipments during the work-from-home trend amid COVID-19 greatly improved it. Since 2H23, the robust AI server assembly business become the second growth engine, driving the ROE to low-30% last year. Despite the impressive ROE, we see downside risk for consensus estimates for Quanta and rate Quanta Underperform (Quanta 1Q26: a sharp decline in profitability; Reiterate Underperform).  
- Camera/lens suppliers: The global smartphone market witnessed strong growth until 2015, followed by a decline from 2018 due to longer replacement cycle. Nonetheless, the increasing number of camera per phone allowed total handset lens shipment to grow until 2021. This explains the exceptionally strong ROE demonstrated by Largan in early years, and Sunny Optical's aggressive market share gains in the Android market narrowed the gap. Both companies faced deteriorated ROE in 2022-23, impacted by the camera de-spec trend amid COVID, but showed signs of recovery in 2024-25. The inflationary memory price is a headwind to consumer electronics this year, particularly for Android camp. We recently upgraded Largan to Outperform as we expect the company will successfully expand to CPO area, which will likely contribute $5\%$ of revenue by 2028 (Largan: deep dive of communication optics (CPO) market; Upgrading to Outperform; PT=NT\$5,150).

EXHIBIT 1: The trend of ROE among companies reflects broader sector trends and cycles, and individual company competitiveness in each market  
![](images/8ab96685d0a9bcfe59b8247b733961b002a377cb21f69b6d07da3c2393a5bc94.jpg)

<details>
<summary>line chart</summary>

| Year | Quanta | Luxshare | Largan | Sunny Optical | Unimicron | Delta Electronics | Chroma |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2010 | 18% | 12% | 28% | 10% | 18% | 22% | 26% |
| 2011 | 19% | 13% | 29% | 11% | 14% | 15% | 24% |
| 2012 | 18% | 14% | 27% | 12% | 10% | 18% | 18% |
| 2013 | 19% | 15% | 30% | 13% | 5% | 19% | 15% |
| 2014 | 20% | 16% | 50% | 14% | 0% | 20% | 14% |
| 2015 | 19% | 17% | 45% | 15% | 0% | 19% | 13% |
| 2016 | 18% | 18% | 35% | 20% | 0% | 18% | 15% |
| 2017 | 17% | 19% | 30% | 45% | 0% | 17% | 20% |
| 2018 | 16% | 20% | 25% | 35% | 5% | 16% | 18% |
| 2019 | 15% | 22% | 20% | 30% | 8% | 15% | 15% |
| 2020 | 14% | 24% | 15% | 35% | 10% | 14% | 14% |
| 2021 | 13% | 26% | 14% | 30% | 25% | 13% | 20% |
| 2022 | 12% | 28% | 13% | 25% | 40% | 12% | 25% |
| 2023 | 11% | 30% | 12% | 5% | 15% | 11% | 20% |
| 2024 | 10% | 32% | 11% | 8% | 5% | 10% | 25% |
| 2025 | 9% | 34% | 10% | 15% | 7% | 9% | 35% |
| 2026E | 8% | 36% | 9% | 14% | 15% | 8% | 45% |
| 2027E | 7% | 38% | 8% | 13% | 25% | 7% | 55% |
| E* | - | - | - | - | - | - | - |
| E* | - | - | - | - | - | - | - |
| E* | - | - | - | - | - | - | - |
| E* | - | - | - | - | - | - | - |
| E* | - | - | - | - | - | ~43% | ~65% |
| E* | - | - | - | - | - | ~44% | ~63% |
| E* | - | - | - | - | - | ~43% | ~64% |
| E* | - | - | - | - | - | ~44% | ~63% |
| E* | - | - | - | - | - | ~44% | ~63% |
| E* | - | - | - | - | - | ~44% | ~63% |
| E* | - | - | - | - | - | ~44% | ~63% |
</details>

2026E - 2028E numbers are based on Bernstein estimates  
Source: Bloomberg, Bernstein analysis and estimates

EXHIBIT 2: Global PCB market has been highly cyclical over the past 16 years and is now experiencing a strong upcycle  
![](images/cc84e0ac17326c5d6accff1650abe0504c4a08534e5ffaafc6d21fe59fd558a6.jpg)

<details>
<summary>bar-line hybrid chart</summary>

Global PCB market size & YoY growth
| Year | PCB Market Size (US$B) | YoY (%) |
| :--- | :--- | :--- |
| 2010 | 52 | 120 |
| 2011 | 55 | 78 |
| 2012 | 56 | 58 |
| 2013 | 56 | 66 |
| 2014 | 58 | 67 |
| 2015 | 54 | -3 |
| 2016 | 55 | 54 |
| 2017 | 59 | 86 |
| 2018 | 62 | 79 |
| 2019 | 55 | 54 |
| 2020 | 66 | 79 |
| 2021 | 80 | 120 |
| 2022 | 82 | 65 |
| 2023 | 70 | -16 |
| 2024 | 73 | 77 |
| 2025 | 85 | 16 |
| 2026 | 103 | 13 |
| 2027 | 108 | 8 |
| 2028 | 110 | 6 |
</details>

2026 - 2028 numbers are estimates  
Source: Prismark estimates and Bernstein analysis

We further break down the 5-year average ROE with DuPont analysis to explore the drivers for each segment Exhibit 3: starting with profitability, the gross margin of the tech supply chain follows a smile curve Exhibit 4. Companies in the upstream (equipment and material) typically enjoy 30%+ gross margin due to technology leadership, engineering experience and resource control. They also need certain level of gross margin to compensate their high R&D investment and relatively smaller revenue scale compared to players in the other part of the supply chain. As we move along the supply chain, suppliers' revenue (bubble size) becomes bigger because it includes externally bought components from the upstream. Therefore, ODM/EMS companies typically face the lowest GM, which emphasizes the importance of business scale and operating efficiency in this sub-sector. The profitability then moves towards customers (OEM/brand) where design, branding and software demonstrate their values. Other observations for ROE drivers include:

- Equipment suppliers: Chroma delivers an impressive ROE, driving by a strong NPM from its customized products targeting niche markets.  
- Hardware component suppliers: over the past five years, Largan and Sunny Optical's ROEs were similar, despite significant difference in their NPM. Largan's asset turnover ratio was considerably lower than that of Sunny Optical's, indicating a heavier reliance on asset due to its focus on high-end lenses, particularly for Apple. Additionally, c.70% of Sunny's revenue comes from camera module, in which capex intensity is lighter than lens production due to a lower tech threshold. Moreover, Largan demonstrates lower equity leverage than Sunny Optical, bolstered by its substantial cash reserves. Sunny Optical saw significantly higher earnings volatility than Largan (Exhibit 5-Exhibit 6), reflecting greater GPM fluctuation amid Android-driven cycles and highly competitive module business, while Largan is supported by more resilient iPhone demand and higher tech threshold in lens market. Similarly, Unimicron exhibits high earnings volatility due to GPM fluctuations across the PCB cycle.  
- ODM suppliers: Luxshare and Quanta presented the highest 5-year average ROE in our Coverage, driven by their exceptional asset turnover and high equity multiplier, despite having lowest NPMs. This underscores that value creation in ODM companies stems from operation efficiency and capital leverage. Regarding the sales volatility in Exhibit 5, Quanta demonstrates the highest sales volatility, as buy-sell business model for AI server significantly boost reported revenue.

EXHIBIT 3: The DuPont analysis to break down the ROE drivers

<table><tr><td rowspan="3">Sub-sector</td><td rowspan="3">Sub-sector/Company</td><td colspan="13">Past 3 years average</td><td colspan="4">2022-2025</td><td colspan="2">2025-2028</td><td></td></tr><tr><td rowspan="2">ROE</td><td>=</td><td colspan="7">Net margin</td><td>X</td><td>Turnover</td><td>X</td><td>Leverage</td><td colspan="2">CAGR</td><td colspan="2">Earning volatility</td><td colspan="2">CAGR</td><td></td></tr><tr><td></td><td>NPM</td><td>=</td><td>(</td><td>GM</td><td>-</td><td>R&amp;D</td><td>-</td><td>SG&amp;A</td><td>-</td><td>Other</td><td>)</td><td>Sales/Asset</td><td></td><td>Asset/Equity</td><td>Sales</td><td>Net profit</td><td>Sales</td><td>Net profit</td></tr><tr><td>Equipments</td><td colspan="21">Equipment suppliers</td></tr><tr><td>Equip.</td><td>Chroma</td><td>27%</td><td></td><td>30%</td><td></td><td>59%</td><td></td><td>10%</td><td></td><td>22%</td><td></td><td>(2%)</td><td></td><td>58%</td><td></td><td>147%</td><td></td><td>9%</td><td>32%</td><td>22%</td><td>59%</td></tr><tr><td colspan="22">Smartphone c Hardware component suppliers</td></tr><tr><td rowspan="4">Hardware component</td><td>Largan</td><td>12%</td><td></td><td>39%</td><td></td><td>51%</td><td></td><td>9%</td><td></td><td>3%</td><td></td><td>(0%)</td><td></td><td>27%</td><td></td><td>117%</td><td></td><td>9%</td><td>(2%)</td><td>12%</td><td>19%

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
