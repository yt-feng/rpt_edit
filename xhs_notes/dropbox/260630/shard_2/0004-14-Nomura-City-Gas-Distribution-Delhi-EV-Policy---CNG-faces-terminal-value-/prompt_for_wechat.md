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
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
EQUITY: OIL & GAS/ CHEMICALS ASIA

# Delhi EV Policy – CNG faces terminal value risk Quick Note

The Delhi Cabinet approved its ‘EV Policy 2026–30’ on 29 June, effective 1 July, committing INR150bn over a period of four years in the form of subsidies, tax waivers, and charging infrastructure. The policy marks a structural shift from incentive-led to mandate-led EV adoption.

## Key timelines

• 1 Jul 2026: policy comes into effect.

\- 1 Jan 2027 onwards: only new electric (no petrol/diesel/CNG/hybrid) auto-rickshaws and N1 vehicles (small goods carriers) will be registered in Delhi.

\- 1 Apr 2028 onwards: only new electric two-wheelers (no petrol/CNG) will be eligible for registration in Delhi.

• 31 Mar 2030: policy expires.

## Incentives structure

\- 100% road tax and registration fee waiver on EVs priced up to INR3mn (ex showroom); strong hybrids get no incentives.

\- Electric two-wheeler purchase subsidies of INR30,000/INR20,000/INR10,000 in years 1/2/3, restricted to models priced below INR225,000 ex-showroom.

\- Electric three-wheeler purchase subsidies of INR50,000/INR40,000/INR30,000 in years 1/2/3.

• Full road tax and registration fee exemptions on EV cars priced up to INR3mn

\- Scrappage incentive of INR100,000/INR50,000/INR25,000/INR10,000 for four-wheeler/N1 commercial trucks/3-wheelers/2-wheelers. Scrappage incentive of INR100,000 for scrapping a BS-IV or older Delhi-registered car and purchasing an EV under INR3mn.

\- All eligible incentives will be transferred directly to beneficiaries' bank accounts through the Direct Benefit Transfer scheme.

## Hard transition deadlines vs incentives-led push earlier

Compared with the earlier 2020 EV policy, the new 2026 EV policy is more comprehensive with strict deadlines for EV-only new vehicle registrations, rather than only an incentive-led push earlier. The government has also set an aggressive target of 95% new vehicle registrations to be electric by 2027E, after it missed the target of 25% electric vehicle new registrations by 2024.

## Research Analysts

India Oil & Gas/Chemicals

Bineet Banka, CFA - NFASL

bineet.banka@NOM.com

+91(22)4037 4044

Fig. 1: Delhi EV Policy: 2020 vs 2026

<table><tr><td>Dimension</td><td>2020 Policy</td><td>2026 Policy</td></tr><tr><td>Core Philosophy</td><td>Incentive-led; asks people to go electric</td><td>Mandate-led; requires people to go electric</td></tr><tr><td>Primary Tool</td><td>Purchase subsidies + tax waivers</td><td>Hard registration bans + purchase subsidies + tax waivers</td></tr><tr><td>Registration Bans</td><td>None</td><td>CNG/petrol 3W banned from Jan 2027; Petrol 2W banned from Apr 2028</td></tr><tr><td>EV Penetration Target</td><td>25% of new vehicle registrations by 2024 — MISSED (actual: ~13%)</td><td>95% of new personal vehicle registrations electric by 2027</td></tr></table>

Source: NOM  
Production Complete: 2026-06-29 17:36 UTC

## See Appendix A-1 for analyst certification, important disclosures and the status of non-US analysts.

## CGD sector implications

IGL (IGL IN, Buy): We believe the policy is structurally negative for IGL's Delhi auto-CNG volume trajectory. CNG two-wheelers are not material for IGL's CNG volumes, while CNG 3-wheelers sales have been on a structural downtrend (less than 20% of total 3-wheeler sales) due to faster EV adoption. We think the more significant risk is the car segment, as CNG cars/taxis constitute the bulk (\~65%) of IGL's CNG volumes. Near-term earnings impact appears limited given the existing fleet of vehicles, but new vehicle addition rates should structurally decelerate in Delhi from FY27F onwards, in our view. The PNG domestic (8% of volume in FY26) and industrial/commercial segments (13% of volume in FY26) are unaffected and remain growth levers.

MGL (MAHGL IN, Buy): We expect no direct policy impact to MGL, as it operates predominantly in Maharashtra. However, if Maharashtra follows Delhi's precedent, we think MGL might face a similar terminal risk in the future. We also note that Mumbai/Thane have still not banned diesel vehicles, that Delhi banned more than a decade ago, which we think could be the first to take the hit rather than CNG. Also, Mumbai being a coastal city also allows it to be less stringent in terms of pollution control measures, at least, in the near to medium term. We prefer MGL among the CGDs under our coverage due to its faster volume growth profile, and lower EV-mandate risk in the near to medium term.

Gujarat Gas (GUJGA IN, Buy): Gujarat Gas's volume mix is dominated by industrial and commercial PNG; auto-CNG is a small share of its portfolio. Therefore, if a similar policy is implemented in Gujarat, it may impact Gujarat Gas the least among its CGD peers.

Overall view: We believe ‘Delhi EV Policy 2026’ is a structural overhang on IGL's auto-CNG new additions trajectory, though near-term earnings impact may not be significant. In our view, IGL's volume growth will increasingly depend on geographic expansion (UP/Haryana Gas), PNG household additions, and LNG diversification, though all these are lower-margin relative to CNG. We believe CGDs may now need to start to aggressively pursue inorganic opportunities to grow volumes given the risk of pollution-led CNG mandates in large cities.

Gujarat Gas (GUJGA IN)

Rating and target price chart (three year history)

## Appendix A-1

This report has been produced by NOM Financial Advisory and Securities (India) Private Limited (NFASL), India. See Disclaimers for NOM Group entity details.

## Analyst Certification

I, Bineet Banka, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>Gujarat Gas</td><td>GUJGA IN</td><td>INR 335</td><td>29-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Indraprastha Gas</td><td>IGL IN</td><td>INR 165</td><td>29-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Mahanagar Gas</td><td>MAHGL IN</td><td>INR 1,142</td><td>29-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

INR 335 (29-Jun-2026) Buy (Sector rating: N/A)  
![](images/0528e313002c9b77ec9c2be6d0c02be863f72413f368101e5af5ed685881e410.jpg)  
Source: LSEG, NOM  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We use SoTP methodology to value Gujarat Gas and arrive at a TP of INR511. We value the Gas Trading business at 5x EV/EBITDA, CGD business at 12x EV/EBITDA, Gas Transmission business at 8x EV/EBITDA. We value the E&P, Power, and Regasification businesses at 0.5x book value. We value Associate Sabarmati Gas (unlisted) at 10x P/E. The benchmark index for this stock is the Nifty 50.
Risks that may impede the achievement of the target price Downside risks include a (1) lower than-anticipated increase in volumes, (2) sharp rise in spot/long-term LNG prices and, (3) sharp cut in Saudi propane prices.

![](images/83bb98d750e25c504c12a6b8a9b5a3786f5a63643808098e5c0fc64e9a4a2197.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>20-May-26</td><td></td><td>200.00</td><td>155.00</td></tr><tr><td>15-Feb-26</td><td></td><td>225.00</td><td>167.00</td></tr><tr><td>16-Dec-25</td><td>Buy</td><td></td><td>183.00</td></tr><tr><td>16-Dec-25</td><td></td><td>230.00</td><td>183.00</td></tr><tr><td>14-Nov-25</td><td></td><td>215.00</td><td>213.00</td></tr><tr><td>01-Aug-25</td><td></td><td>225.00</td><td>202.00</td></tr><tr><td>16-Jun-25</td><td></td><td>210.00</td><td>212.00</td></tr><tr><td>28-Apr-25</td><td></td><td>200.00</td><td>185.00</td></tr><tr><td>29-Jan-25</td><td>Neutral</td><td></td><td>195.00</td></tr><tr><td>29-Jan-25</td><td></td><td>195.00</td><td>195.00</td></tr><tr><td>18-Nov-24</td><td>Reduce</td><td></td><td>163.00</td></tr><tr><td>18-Nov-24</td><td></td><td>170.00</td><td>163.00</td></tr><tr><td>29-Oct-24</td><td></td><td>185.00</td><td>209.00</td></tr><tr><td>09-May-24</td><td></td><td>223.00</td><td>220.00</td></tr><tr><td>29-Jan-24</td><td></td><td>228.00</td><td>210.00</td></tr><tr><td>20-Oct-23</td><td>Neutral</td><td></td><td>202.00</td></tr><tr><td>20-Oct-23</td><td></td><td>238.00</td><td>202.00</td></tr><tr><td>26-Jul-23</td><td></td><td>278.00</td><td>235.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We use a DCF methodology to value IGL, assuming a WACC of 12% and a terminal growth rate of 2%. This derives a target price of INR200. The benchmark index for this stock is the Nifty 50.
Risks that may impede the achievement of the target price Downside risks: 1) lower-than-anticipated volumes; 2) lower-than-anticipated margins; 3) lower-than-anticipated allocation of domestic gas; and 4) higher-than-anticipated LNG prices.

![](images/ffeb356ac67f52584e828f71a216b193e1199cfecffef6b678063c182e1c6bc9.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>10-May-26</td><td></td><td>1,430.00</td><td>1,173.00</td></tr><tr><td>09-Feb-26</td><td></td><td>1,505.00</td><td>1,181.00</td></tr><tr><td>31-Oct-25</td><td></td><td>1,510.00</td><td>1,277.00</td></tr><tr><td>24-Jul-25</td><td></td><td>1,580.00</td><td>1,429.00</td></tr><tr><td>16-Jun-25</td><td>Buy</td><td></td><td>1,390.00</td></tr><tr><td>16-Jun-25</td><td></td><td>1,680.00</td><td>1,390.00</td></tr><tr><td>29-Jan-25</td><td>Neutral</td><td></td><td>1,267.00</td></tr><tr><td>29-Jan-25</td><td></td><td>1,350.00</td><td>1,267.00</td></tr><tr><td>18-Nov-24</td><td></td><td>1,130.00</td><td>1,130.00</td></tr><tr><td>27-Oct-24</td><td>Reduce</td><td></td><td>1,497.00</td></tr><tr><td>12-May-24</td><td></td><td>1,250.00</td><td>1,300.00</td></tr><tr><td>31-Oct-23</td><td>Neutral</td><td></td><td>1,032.00</td></tr><tr><td>31-Oct-23</td><td></td><td>1,110.00</td><td>1,032.00</td></tr><tr><td>07-Aug-23</td><td></td><td>1,250.00</td><td>1,064.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We use a DCF methodology to value Mahanagar Gas, assuming a WACC of 12% and a terminal growth rate of 2%. This derives a target price of INR1,430. The benchmark index for this stock is the Nifty 50.
Risks that may impede the achievement of the target price Downside risks:(1) a sharp increase in spot/long-term LNG prices and the company's inability to increase prices across segments, (2) lower-than expected volume growth for CNG/PNG, and (3) lower-than-anticipated EBITDA margin.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

57% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 34% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

41% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

2% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 0% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

As at 31 March 2026.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

## Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at: http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise stated in the valuation methodology; Japan: Russell/NOM Large Cap.

## SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

## Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or the market, and may not occur if the company's earnings differ from estimates.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'),

Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 

[中间内容因长度限制已省略]

AL

ADVISER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM Financial Advisory and Securities (India) Private Limited, India. All rights reserved.
"""
