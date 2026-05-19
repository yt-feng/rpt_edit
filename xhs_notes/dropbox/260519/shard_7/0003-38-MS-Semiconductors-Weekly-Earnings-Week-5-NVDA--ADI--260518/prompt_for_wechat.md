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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Semiconductors | North America

# Weekly: Earnings Week 5 (NVDA, ADI)

WHAT'S CHANGED 

<table><tr><td>NVIDIA Corp. (NVDA.O)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>$260.00</td><td>$285.00</td></tr></table>

Raising estimates and PT on NVDA, which remains our top pick in semis; also see a strong quarter from ADI, given company specific drivers as well as industry recovery.

NVDA (OW, reporting after market close on Wednesday, May 20th): Expecting continued upside to numbers and a bullish tone on key debates (market share vs ASIC, gross margin, rubin readiness). We elevated Nvidia to our top-pick in March (Moving NVIDIA back to top pick in semis) on the view that a below market multiple created an attractive entry in the primary generative AI winner. It has taken time for investor enthusiasm to return to the story as secondary and tertiary AI beneficiaries continue to outperform. But we think the quarter will be a positive step towards a stock rerating, that said Nvidia can only do so much on a Q1 earnings call to ease concerns on longer term debates. We think the typical beat and raise pattern (beat by \$3bn, guide \$4bn above) is a likley outcome. What we are focused on for earnings:

Trajectory to \$1T Blackwell+Rubin revenue CY25-CY27: We think CY25 included about \$25bn of hopper compute, maybe \~\$30bn or so including networking, removing that from the CY25 \$185bn in datacenter revenues leaves \$155bn, implying \$845bn of datacenter over CY26-27 before including products like Groq, standalone CPUs, and ICMS - which should be substantial upside. Despite that consensus estimates for total datacenter revenue over that period is just \$785bn (we raise our estimates today to \$884bn CY26-CY27, \$1.07T CY25-CY27). We think consensus is likley to move much closer to our estimates as Nvidia reaffirms their visibility to those numbers, which importantly should include a discussion of supply constraints that need to be managed in route to that. Constraints including powered shell availability, leading edge wafer capacity, and DRAM.

Managing rising input costs: With the line of sight to continued growth in revenues we highlighted above Nvidia has \$95bn in purchase commitments and \$21bn in inventories as of the 10k, if that represents 75% gross margin COGS (\$464bn in revenue) Nvidia should have the supply to cover much of what they intend to ship over the next 18 months before cost inflation becomes a significant margin headwind. That said the ramp of a new architecture in Rubin will be a headwind, and costs are rising beyond this year so we have derisked our estimates in that respect - and we are now modeling 72.7% gross margins in FY28. But we think that frontfootedness to secure supply puts Nvidia in an advantaged position vs the peer group as ASIC and merchant competition will either see greater margin headwinds or need to raise prices by more to offset those impacts.

MS & CO. LLC

# Joseph Moore

Equity Analyst

Joseph.Moore@morganstanley.com +1 212 761-7516

# Mason Wayne

Research Associate

Mason.Wayne@morganstanley.com +1 212 761-6012

# Ella Tulchinsky

Research Associate

Ella.Tulchinsky@morganstanley.com +1 212 761-2222

# Nicole Kozhukhov

Research Associate

Nicole.Kozhukhov@morganstanley.com +1 212 761-1636

# Shane Brett

Equity Analyst

Shane.Brett@morganstanley.com +1 212 761-1022

# SEMICONDUCTORS

North America

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

XPU marketshare and new product (Groq/ standalone CPUs) traction: Perhaps the most important debate for the stock is what Nvidia's marketshare in XPUs and in the datacenter broadly looks like out beyond next year. We are optimistic on this debate, ad think Nvidia represents the leading TCO across the market, but as compute remains in short supply that debate is difficult to disprove, and we don't think there's much incremental Nvidia can say on this earnings call to further the debate in either direction. However given how recently Nvidia has launched Groq and standalone CPUs this is an area where we may hear more about the potential revenue contribution in the near-term and how Nvidia see's their solutions for competing offerings.

We also believe that the share debate is somewhat secondary at these prices, if Nvidia's \$1T commentary is to be believed Nvidia's earnings should be in the range of \$4 per share (\$16 run rate) exiting 2027. A \$16 perpetuity at an 8% discount rate and 1% terminal growth rate has a present value of \$229 vs Nvidia's current share price of \$225. So investors believe that via margin compression, share loss, or a general slowdown in AI spending that there's very little in long term FCF and earnings growth set to come from Nvidia. All debates we think can to turn more in Nvidia's favor as rubin begins to ship in volume later this year and is key to our positive view on the risk reward.

Product cycle: Vera Rubin ready to go, albeit with some normal startup issues. We continue to see Vera Rubin tracking to schedules, ramping in 2h, though there are some normal week to week ramp challenges that could mean racks are a few weeks later than initial estimates. We see strength in both Rubin and Blackwell demand through 2h and do not see any disruptions.

Raising estimates: We move revenue/GM/EPS (all non-gaap) for the April quarter from \$78.25bn/74.9%/\$1.69 to 79.264/75.0%/\$1.72, July from \$84.837bn/75.0%/\$1.93 to \$87.88bn/75.1%/\$2.01, FY27 from \$353.8bn/74.4%/\$7.93 to \$380.591bn/74.4%/\$8.61 and finally FY28 from \$452.4bn/74.2%/\$10.14 to \$587.45/72.7%/\$13.11.

Raising PT: Our prior PT of \$260 was based on \~26 our MW CY27 (FY28) EPS estimate of \$10.05. We are lowering our multiple assumption to \~22x, in-line with the broader market and a discount to compute semis peers (AMD/AVGO/INTC) as high marketshare and gross margins leave create limited levers for multiple expansion in the near term. On our now higher \$12.99 of EPS that brings the target to \$285.

ADI (OW, reporting before market open on Wednesday, May 20th): The base case is a beat and raise, and while the bar has moved higher throughout analog earnings, we believe ADI can still surprise to the upside, particularly as the stock has lagged the broader analog rally. We view the relative underperformance as largely driven by perceived lower torque, given both MSe and Street already model ADI surpassing prior peak revenue levels this year - a distinction shared only with NXP in our analog coverage. We think this misses the setup, as ADI has accelerating AI-linked revenue, large Industrial exposure (\~50% of revenue), and GM% near prior peaks, creating a cleaner path for upside if Industrial recovery broadens and AI momentum continues. What we are focused on for earnings:

1.) AI-related revenue: Data center within Comms continues to gain momentum, with strength across both optical and power. ADI's AI-related revenue consists of \~\$800mn from ATE within Industrial, plus power/optical exposure within Comms, where power and optical represent \~2/3 of the segment. Combined, AI-related revenue is running at a >\$2bn run-rate, or \~20% of total revenue, grew \~50% in FY25, and continued to accelerate in Q1 FY26. Mgmt guided Communications up +HSD q/q in AprQ, or \~60% y/y, driven by AI data center demand and a wireless infrastructure recovery. We view AI momentum as still in the early innings for ADI as both power and optical are seeing significant tailwinds in the supply chain from shortages linked to demand. The former is supported by ADI's vertical power delivery solution, while the latter remains an underappreciated asset given strong optical momentum in DC. We expect DC revenue to double in 2026, driven by both areas.

2.) Industrial strength: Industrial remains a key recovery lever for ADI, with near-term strength led by ATE and A&D, which together comprise \~1/3 of the segment and are reaching new highs. ATE is expected to grow >30% q/q in AprQ, while the broader Industrial business outside ATE/A&D remains below prior peaks, leaving room for further cyclical recovery. Mgmt guided Industrial up \~20% q/q and \~50% y/y in AprQ, with positive book-to-bill across all submarkets and geographies. We expect Industrial to reach new highs over time as continued ATE momentum is complemented by a broader recovery across the rest of the segment, supporting both revenue upside and mix-driven GM expansion.

Preview to earnings 

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Analog Devices Inc. ADI.O</td></tr><tr><td>JulQ Guide</td><td> $\uparrow$  Likely upside surprise</td><td> $\uparrow$  Modest revision higher</td></tr><tr><td colspan="3">NVIDIA Corp. NVDA.O</td></tr><tr><td>JulQ Guide</td><td> $\uparrow$  Very likely upside surprise</td><td> $\uparrow$  Meaningful revision higher</td></tr></table>

\*Likely impact to consensus EPS is for the next 12 months   
Source: Company data, MS

# NVIDIA Corp Earnings Preview

The company is scheduled to report after the market close on Wednesday, May 20th.

NVDA (OW, reporting after market close on Wednesday, May 20th): Expecting continued upside to numbers and a bullish tone on key debates (market share vs ASIC, gross margin, rubin readiness). We elevated Nvidia to our top-pick in March (Moving NVIDIA back to top pick in semis) on the view that a below market multiple created an attractive entry in the primary generative AI winner. It has taken time for investor enthusiasm to return to the story as secondary and tertiary AI beneficiaries continue to outperform. But we think the quarter will be a positive step towards a stock rerating, that said Nvidia can only do so much on a Q1 earnings call to ease concerns on longer term debates. We think the typical beat and raise pattern (beat by \$3bn, guide \$4bn above) is a likley outcome. What we are focused on for earnings:

Trajectory to \$1T Blackwell+Rubin revenue CY25-CY27: We think CY25 included about \$25bn of hopper compute, maybe \~\$30bn or so including networking, removing that from the CY25 \$185bn in datacenter revenues leaves \$155bn, implying \$845bn of datacenter over CY26-27 before including products like Groq, standalone CPUs, and ICMS - which should be substantial upside. Despite that consensus estimates for total datacenter revenue over that period is just \$785bn (we raise our estimates today to \$884bn CY26-CY27, \$1.07T CY25-CY27). We think consensus is likley to move much closer to our estimates as Nvidia reaffirms their visibility to those numbers, which importantly should include a discussion of supply constraints that need to be managed in route to that. Constraints including powered shell availability, leading edge wafer capacity, and DRAM.

Managing rising input costs: With the line of sight to continued growth in revenues we highlighted above Nvidia has \$95bn in purchase commitments and \$21bn in inventories as of the 10k, if that represents 75% gross margin COGS (\$464bn in revenue) Nvidia should have the supply to cover much of what they intend to ship over the next 18 months before cost inflation becomes a significant margin headwind. That said the ramp of a new architecture in Rubin will be a headwind, and costs are rising beyond this year so we have derisked our estimates in that respect - and we are now modeling 72.7% gross margins in FY28. But we think that frontfootedness to secure supply puts Nvidia in an advantaged position vs the peer group as ASIC and merchant competition will either see greater margin headwinds or need to raise prices by more to offset those impacts.

XPU marketshare and new product (Groq/ standalone CPUs) traction: Perhaps the most important debate for the stock is what Nvidia's marketshare in XPUs and in the datacenter broadly looks like out beyond next year. We are optimistic on this debate, ad think Nvidia represents the leading TCO across the market, but as compute remains in short supply that debate is difficult to disprove, and we don't think there's much incremental Nvidia can say on this earnings call to further the debate in either direction. However given how recently Nvidia has launched Groq and standalone CPUs this is an area where we may hear more about the potential revenue contribution in the near-term and how Nvidia see's their solutions for competing offerings.

We also believe that the share debate is somewhat secondary at these prices, if Nvidia's \$1T commentary is to be believed Nvidia's earnings should be in the range of \$4 per share (\$16 run rate) exiting 2027. A \$16 perpetuity at an 8% discount rate and 1% terminal growth rate has a present value of \$229 vs Nvidia's current share price of \$225. So investors believe that via margin compression, share loss, or a general slowdown in AI spending that there's very little in long term FCF and earnings growth set to come from Nvidia. All debates we think can to turn more in Nvidia's favor as rubin begins to ship in volume later this year and is key to our positive view on the risk reward.

Product cycle: Vera Rubin ready to go, albeit with some normal startup issues. We continue to see Vera Rubin tracking to schedules, ramping in 2h, though there are some normal week to week ramp challenges that could mean racks are a few weeks later than initial estimates. We see strength in both Rubin and Blackwell demand through 2h and do not see any disruptions.

Raising estimates: We move revenue/GM/EPS (all non-gaap) for the April quarter from \$78.25bn/74.9%/\$1.69 to 79.264/75.0%/\$1.72, July from \$84.837bn/75.0%/\$1.93 to \$87.88bn/75.1%/\$2.01, FY27 from \$353.8bn/74.4%/\$7.93 to \$380.591bn/74.4%/\$8.61 and finally FY28 from \$452.4bn/74.2%/\$10.14 to \$587.45/72.7%/\$13.11.

Raising PT: Our prior PT of \$260 was based on \~26 our MW CY27 (FY28) EPS estimate of \$10.05. We are lowering our multiple assumption to \~22x, in-line with the broader market and a discount to compute semis peers (AMD/AVGO/INTC) as high marketshare and gross margins leave create limited levers for multiple expansion in the near term. On our now higher \$12.99 of EPS that brings the target to \$285.

Exhibit 1: NVDA: MS vs Consensus 

<table><tr><td rowspan="3">Figures in $ MMs</td><td colspan="8">NVDA: MS vs. Consensus</td></tr><tr><td colspan="2">F1Q27E</td><td colspan="2">F2Q27E</td><td colspan="2">2027E</td><td colspan="2">2028E</td></tr><tr><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td></tr><tr><td>Revenue</td><td>79,264</td><td>78,821</td><td>87,880</td><td>87,025</td><td>380,591</td><td>369,735</td><td>587,450</td><td>491,746</td></tr><tr><td>Q/Q Change</td><td>16.3%</td><td>15.7%</td><td>10.9%</td><td>10.4%</td><td></td><td></td><td></td><td></td></tr><tr><td>Gross margin</td><td>75.1%</td><td>75.0%</td><td>75.1%</td><td>74.6%</td><td>74.5%</td><td>73.9%</td><td>72.7%</td><td>73.8%</td></tr><tr><td>EPS</td><td>$1.72</td><td>$1.75</td><td>$2.01</td><td>$1.95</td><td>$8.61</td><td>$8.32</td><td>$13.11</td><td>$11.29</td></tr></table>

Source: Factset, MS

# Risk Reward – NVIDIA Corp. (NVDA.O)

Top Pick

OW as large language model enthusiasm is transforming cloud capex

# PRICE TARGET \$285.00

\~22 our MW CY27 EPS estimate of \$12.99, in-line with large cap AI peer AVGO, in-line with the broader market and a discount to compute semis peers (AMD/AVGO/INTC) as high marketshare and gross margins leave create limited levers for multiple expansion in the near term.

![](images/89cf09c6ba22b679990d373fc0f0c39ade9d5a227660f4f9fc038605e6651cfd.jpg)

<details>
<summary>bar_line</summary>

| Category             | Value    |
| -------------------- | -------- |
| MS PT                | $268.03  |
| MS Estimates | $432.78  |
| Mean                 | $138.00  |
</details>

RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)   
![](images/c7ea9e627f9863944a43d7c637deb513a35c580f746963e47d31ed735fea64d0.jpg)

<details>
<summary>line</summary>

| Date       | Current Stock Price | Price Target |
| ---------- | ------------------- | ------------ |
| MAY '25    | $225.32             | -            |
| MAY '26    | -                   | -            |
| MAY '27    | $160.00 (-28.99%)  | $338.00 (-33.8%) |
| MAY '27    | $285.00 (+26.49%)  | $330.00 (+46.46%) |
| MAY '27    | -                   | -            |
</details>

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 15 May 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

# OVERWEIGHT THESIS

■ Blackwell remains the premiere solution for gen-AI workloads, where compute demand continues to outstrip supply   
■ We see continued upward pressure to estimates as demand strength continues, with Rubin expected to maintain Nvidia's performance leadership position

Consensus Rating Distribution   
![](images/d983e91a4ac19e1100f51882c410cf954dd02d0b3da9b16fd6290791a871a7f3.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| Overweight | 93 |
| Equal-weight | 5 |
| Underweight | 2 |
MS Rating
</details>

Source: Refinitiv, MS

# Risk Reward Themes

New Data Era: Positive
Pricing Power: Positive
Secular Growth: Positive

View descriptions of Risk Rewards Themes here

# BULL CASE

# \$330.00

\~30x bull case MW CY27 EPS of \$11

Bull case has DC revenues continuing to grow through 2027. Upside from networking, GB300 based systems, networking, and software create potential for a full stack AI computing company worthy of an even greater valuation premium

- Higher margin data center and AI-focused software and services growth accelerates   
- GPU based AI PC gains traction, widely increasing the client TAM   
- Automotive opportunity takes off, allowing the company to earn recurring, per-car licensing revenue

# BASE CASE

\~22x o

[中间内容因长度限制已省略]

 or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.   
INDUSTRY COVERAGE: Semiconductors 

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (05/15/2026)</td></tr><tr><td>Joseph Moore</td><td></td><td></td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$424.10</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$20.48</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$43.10</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$81.16</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$70.35</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$417.49</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$232.68</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$425.19</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$71.03</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$108.77</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$51.95</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$176.89</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$93.85</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$724.66</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$21.32</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$225.32</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$291.50</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>E (05/11/2025)</td><td>$113.11</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$92.25</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>U (02/10/2026)</td><td>$201.49</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,407.61</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$137.64</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$216.59</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$68.53</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$302.73</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$62.13</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$209.16</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$347.24</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$502.42</td></tr></table>

© 2026 MS
"""
