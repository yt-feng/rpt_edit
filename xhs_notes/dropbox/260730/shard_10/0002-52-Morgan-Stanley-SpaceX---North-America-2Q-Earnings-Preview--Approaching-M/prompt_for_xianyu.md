你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
§ = Consensus data is provided by Refinitiv Estimates
e = MS estimates

July 28, 2026 08:30 PM GMT

SpaceX | North America

# 2Q Earnings Preview: Approaching Max Q?

Revenues, EBITDA, Starlink subs, ARPU, AI pricing, Cursor ARR, FY capex guide... all of these matter. But with SPCX shares down nearly 50% from its highs and nearly 20% below IPO price investors are far more focused on the short term technical overhang. A window has opened for longer term investors.

Please see here for our SpaceX Initiation: SpaceX: AI's Final Frontier; Initiate at Overweight, PT \$300 (7 Jul 2026)

In rocketry, 'Max Q' stands for maximum dynamic pressure, the exact point during a rocket's launch when the physical aerodynamic stress on the airframe reaches its highest peak. Dynamic pressure depends on air density and the speed of the rocket squared (q = 1/2pv^2). We believe Max Q is analogous to what SpaceX shares are experiencing heading into its first reported quarter as a public company. The dynamic stress on the stock price from an unprecedented amount of unlocked shares following 2Q results. We'll see >930mn shares on Aug 6th (approximately \$100bn worth) the first of 8 tranches that will see nearly 4bn shares unlocked through January of 2027.

Stock price implications for 2Q results: We anticipate 2Q results to neither significantly change near-term consensus expectations or the long term story, leaving the share price largely at the mercy of technical forces (lockup expiry), investor positioning (cautious) and macroeconomic factors.

SPCX at $\frac{1}{2}$ a Walmart multiple discounting the AI opportunity for free? At \$100, SPCX would trade at 18x EV/EBIT (FY28). Zero to negative implied AI value, with space & connectivity results materially below our ests. At \$100, SPCX would trade at 16x FY28 PE, more than a 50% discount to WMT (33x FY28 PE) and a 40% discount to TJX (26.5x FY28 PE). See our What's In the Price analysis here. Walmart is covered by Simeon Gutman. TJX is not covered.

## Investor Thoughts, Concerns, & Sentiment Into the Print

\- While still active, our conversations overall have been quieter than we would have expected. Despite no clear fundamental changes to the story over the past few weeks, bears appear to have become gradually more convicted while bulls have become resigned to waiting past the initial lockup releases to avoid any potential wall of selling. Sentiment follows the share price.

\- Most investors see the first concrete potential upside catalyst as Starship Flight 14 (late Aug/early Sept) where the company will attempt a catch of the Starship upper stage, i.e. "the Ship", in a demonstration of progress towards reusability.

\- Most investors significantly discount Grok & Cursor and view the bulk of AI

MS & CO. LLC

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Adam Jonas, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Adam.Jonas@morganstanley.com</td><td>+1 212 761-1726</td></tr><tr><td colspan="2">William Tackett, CFA</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>William.Tackett@morganstanley.com</td><td>+1 212 761-6028</td></tr><tr><td colspan="2">Sean Diffley, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Sean.DIFFLEY@morganstanley.com</td><td>+1 212 761-5868</td></tr><tr><td colspan="2">Kristine T Liwag</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Kristine.Liwag@morganstanley.com</td><td>+1 212 761-2980</td></tr><tr><td colspan="2">Brian Nowak, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Brian.Nowak@morganstanley.com</td><td>+1 212 761-3365</td></tr><tr><td colspan="2">Justin M Lang</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Justin.Lang@morganstanley.com</td><td>+1 212 761-6251</td></tr><tr><td colspan="2">Julian Herrera</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Julian.Herrera@morganstanley.com</td><td>+1 212 761-1784</td></tr><tr><td colspan="2">Blake Netter, CPA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Blake.Netter@morganstanley.com</td><td>+1 212 761-4679</td></tr></table>

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$300.00</td></tr><tr><td>Shr price, close (Jul 27, 2026)</td><td>$113.50</td></tr><tr><td>52-Week Range</td><td>$225.64-108.66</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS ($)**</td><td>(1.69)</td><td>0.28</td><td>2.18</td><td>6.29</td></tr><tr><td>Prior EPS ($)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>P/E</td><td>NM</td><td>400.9</td><td>52.0</td><td>18.0</td></tr><tr><td>EPS ($)§</td><td>-</td><td>(0.43)</td><td>0.61</td><td>3.12</td></tr><tr><td>Div yld (%)</td><td>-</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

<table><tr><td>Quarter</td><td>2025</td><td>2026e Prior</td><td>2026e Current</td><td>2027e Prior</td><td>2027e Current</td></tr><tr><td>Q1</td><td>(0.18)</td><td>-</td><td>(0.84)a</td><td>-</td><td>0.54</td></tr><tr><td>Q2</td><td>(0.34)</td><td>-</td><td>(0.35)</td><td>-</td><td>0.55</td></tr><tr><td>Q3</td><td>(0.36)</td><td>-</td><td>0.27</td><td>-</td><td>0.54</td></tr><tr><td>Q4</td><td>(0.80)</td><td>-</td><td>0.45</td><td>-</td><td>0.56</td></tr></table>

e = MS estimates, a = Actual Company reported data

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

monetization opportunity as neocloud. "What is the AI business and what multiple do I pay for it?" remains arguably the number one question for the direction of the stock price over the next year. Many ascribe zero or even negative value for AI given the high capex requirements relative Space & Connectivity, largely uncertain economics, and the degree of management time devoted to the business.

\- Across our recent meetings, >2/3 of the room on average was bearish SPCX shares through year end. Longer-term (12-18 months) is much more split. Bears are undoubtedly much louder than bulls during dinner debates.

\- Many investors have asked "Does this quarter matter?" - most expect commentary and general tone to be much more impactful than quarterly numbers. Most do not expect any major story-altering announcements.

## Key Numbers for the Print

• Revenue: \$6.9bn (Cons), \$6.75bn (MS)

• EBIT: -\$1.6bn (Cons), -\$1.7bn (MS)

\- Adj EBITDA: \$2.1bn (Cons), \$2.0bn (MS)

• Consumer Starlink Subs: 12.1mn (Cons), 12.0mn (MS)

\- Consumer Monthly ARPU: \$65.5 (Cons), \$65.5 (MS)

• End of Period (2Q) Compute: 1.4 GW (Cons), 1.4 GW (MS)

\- Adj Diluted EPS: -\$0.32 (Cons), -\$0.35 (MS)

\- Consensus sourced from Visible Alpha. Only including consensus published after 7/6/2026.

\- For 2026, investors will notice quite a wide skew in consensus likely due to different assumptions on share count, inclusion/non-inclusion of announced and reported neocloud deals, as well as Cursor. Outside of major surprises, we think that management commentary will be much more relevant to the stock than quarterly numbers for the next few quarters. More details below.

## Key Milestones & Expected Outlook

\- Similar to the style of Tesla earnings calls and the public investor marketing materials pre-IPO, we'd expect fairly limited explicit/quantitative guidance - especially given how much the economic profile of the AI business has shifted with the recent neocloud deals and Cursor. Most likely guidance, if any, is full year capex (we expect \$48bn) and year-end compute deployed (we expect 2 GW).

\- Expect high-level timelines for future Starship test launches, compute deployment cadence, v3 sat deployment, future Grok/Cursor model releases.

## Key Commentary to Watch for the Call

• AI

• We expect AI to get the most air time of the three businesses.

• We do not expect explicit financial color on Cursor given the deal is expected to be closed later this quarter and the lack of detail provided thus far. However, we would expect some commentary on joint SpaceX and Cursor work on future model releases. For reference, Elon

Musk recently posted that Grok 4.6 is coming on August 7th, Grok 4.7 'a few weeks later'. We expect Grok 5 in late 3Q or 4Q - all likely leverage proprietary Cursor coding data similar to Grok 4.5.

• Given the challenges in tracking Grok usage (tokens through X and Cursor are not captured by OpenRouter to our knowledge), we would hope for commentary on Grok 4.5 adoption and usage trends within the Cursor platform. Initial benchmarks were promising, but actual usage matters over all.

## - Starlink

• Expect color on recent drivers of Starlink broadband adoption and new enterprise connectivity deals, but do not expect explicit subscriber or ARPU guidance.

• Expect most commentary on Starlink Mobile to be around technical details of the mobile V2 satellites, partnerships with global MNOs, and near term geographic expansion. Do not expect specific commentary on future business model of Starlink Mobile (partnership vs. go alone) and detailed plans for use of EchoStar spectrum.

## - Starship

• Expect management to reiterate expectation to launch operational payloads on Starship before the end of the year, and give general expectations for the mission profiles of next few test launches.

## - Compute.

\- Expect a walk through of terrestrial compute scale out through at least the rest of the year in Memphis, and general pathway beyond 2 GW next year.

## Most likely potential upside surprises: Plans for more than 2 GW of new

(incremental) compute deployed next year (both MS and Consensus estimate - each incremental GW is a potential \$10-50bn in AI ARR), new chunky neocloud deals (talks with Reflection and the DoW are reported but nothing officially announced), Grok usage trends on Cursor showing material share gains vs. other frontier models, Cursor ARR showing acceleration from the \$4bn reported beginning of June (we model \$7bn for end of 3Q)

Most likely downside surprises: Capex projections materially above the \~\$50bn that we model in 2026, commentary that suggests additional funding raises are expected before year-end, plans to prematurely end/renegotiate current neocloud deals, Starlink subscriber figures suggesting a deceleration in adoption.

Exhibit 1: 2Q26 MS & Consensus: Income Statement

<table><tr><td colspan="4">SPACEXIncome Statement ($mn)</td></tr><tr><td></td><td>2Q26 Actual</td><td>Cons</td><td>MSe</td></tr><tr><td>Space</td><td></td><td>871</td><td>831</td></tr><tr><td>Connectivity</td><td></td><td>3,949</td><td>4,033</td></tr><tr><td>AI</td><td></td><td>2,104</td><td>1,882</td></tr><tr><td>Total Revenue</td><td></td><td>6,924</td><td>6,747</td></tr><tr><td>Y/Y Growth</td><td></td><td>70.1%</td><td>65.7%</td></tr><tr><td>Cost of Revenue</td><td></td><td>3,174</td><td>3,091</td></tr><tr><td>Gross Profit</td><td></td><td>3,750</td><td>3,655</td></tr><tr><td>% Gross Margin</td><td></td><td>54.2%</td><td>54.2%</td></tr><tr><td>R&amp;D</td><td></td><td>4,434</td><td>4,482</td></tr><tr><td>% of Sales</td><td></td><td>64.0%</td><td>66.4%</td></tr><tr><td>SG&amp;A</td><td></td><td>929</td><td>856</td></tr><tr><td>% of Sales</td><td></td><td>13.4%</td><td>12.7%</td></tr><tr><td>Other Expense</td><td></td><td>0</td><td>0</td></tr><tr><td>% of Sales</td><td></td><td>0.0%</td><td>0.0%</td></tr><tr><td>Space EBIT</td><td></td><td>(773)</td><td>(814)</td></tr><tr><td>% Margin</td><td></td><td>-88.7%</td><td>-98.0%</td></tr><tr><td>Connectivity EBIT</td><td></td><td>1,418</td><td>1,387</td></tr><tr><td>% Margin</td><td></td><td>35.9%</td><td>34.4%</td></tr><tr><td>AI EBIT</td><td></td><td>(2,214)</td><td>(2,256)</td></tr><tr><td>% Margin</td><td></td><td>-105.2%</td><td>-119.8%</td></tr><tr><td>Operating Income (EBIT)</td><td></td><td>(1,570)</td><td>(1,683)</td></tr><tr><td>% Margin</td><td></td><td>-22.7%</td><td>-24.9%</td></tr><tr><td>Stock-Based Comp</td><td>To be Announced</td><td>727</td><td>728</td></tr><tr><td>Depreciation &amp; Amortization</td><td></td><td>2,951</td><td>2,971</td></tr><tr><td>Restructuring, Impairment &amp; Other</td><td></td><td>0</td><td>0</td></tr><tr><td>Adj. EBITDA</td><td></td><td>2,108</td><td>2,015</td></tr><tr><td>% Margin</td><td></td><td>30.5%</td><td>29.9%</td></tr><tr><td>Interest Expense</td><td></td><td>645</td><td>757</td></tr><tr><td>Interest Income</td><td></td><td>282</td><td>178</td></tr><tr><td>Net Interest Expense</td><td></td><td>364</td><td>579</td></tr><tr><td>Other Income / (Expense)</td><td></td><td>(97)</td><td>0</td></tr><tr><td>Pre-Tax Income</td><td></td><td>(2,030)</td><td>(2,262)</td></tr><tr><td>Income Tax</td><td></td><td>51</td><td>0</td></tr><tr><td>% Tax Rate</td><td></td><td>-2.5%</td><td>0.0%</td></tr><tr><td>Net Income</td><td></td><td>(2,082)</td><td>(2,262)</td></tr><tr><td>Less: Preferred Div. &amp; Other</td><td></td><td>0</td><td>0</td></tr><tr><td>Net Income to Common</td><td></td><td>(2,082)</td><td>(2,262)</td></tr><tr><td>% Net Margin</td><td></td><td>-30.1%</td><td>-33.5%</td></tr><tr><td>GAAP Diluted EPS</td><td></td><td>($0.32)</td><td>($0.35)</td></tr><tr><td>Diluted Shares Out. (mn)</td><td></td><td>6,501</td><td>6,501</td></tr><tr><td>Cash from Operating Activities</td><td></td><td>(445)</td><td>(450)</td></tr><tr><td>Capital Expenditures</td><td></td><td>17,149</td><td>20,487</td></tr><tr><td>Free Cash Flow</td><td></td><td>(17,594)</td><td>(20,937)</td></tr></table>

Exhibit 2: 2Q26 MS & Consensus: Segment Detail and Key KPIs

<table><tr><td colspan="4">SPACEXSegment Detail &amp; KPIs</td></tr><tr><td></td><td>2Q26</td><td>Cons</td><td>MSe</td></tr><tr><td>Starlink Subs &amp; ARPU</td><td></td><td></td><td></td></tr><tr><td>Consumer Subs (000s)</td><td></td><td>12,072</td><td>11,951</td></tr><tr><td>Consumer ARPU ($/mo)</td><td></td><td>$65.47</td><td>$65.48</td></tr><tr><td>Connectivity Revenue ($mn)</td><td></td><td></td><td></td></tr><tr><td>Consumer &amp; Business</td><td></td><td>2,490</td><td>2,476</td></tr><tr><td>Government &amp; Enterprise</td><td></td><td>1,274</td><td>1,380</td></tr><tr><td>Mobile</td><td></td><td>185</td><td>178</td></tr><tr><td>Total Connectivity Revenue</td><td>TBA</td><td>3,949</td><td>4,033</td></tr><tr><td>Total Broadband</td><td></td><td>3,764</td><td>3,856</td></tr><tr><td>AI Revenue &amp; Compute ($mn)</td><td></td><td></td><td></td></tr><tr><td>Advertising Revenue</td><td></td><td>277</td><td>249</td></tr><tr><td>AI Solutions &amp; Infrastructure</td><td></td><td>1,828</td><td>1,634</td></tr><tr><td>Total AI Revenue</td><td></td><td>2,104</td><td>1,882</td></tr><tr><td>End of Period Compute (MW)</td><td></td><td>1,400</td><td>1,397</td></tr><tr><td>Rev / Watt (Avg Compute, Annualized, $)</td><td></td><td>$7.14</td><td>$6.39</td></tr></table>

Source: Visible Alpha Consensus, MS  
Source: Visible Alpha Consensus, MS

Exhibit 3: 2028 EV/EBIT: SpaceX vs. Key Comps  
![](images/d9405852058acbe5a080642034f3d567307ae10ab4adb6839ae4bbf09dbfab38.jpg)  
Note: Market data as of 7/27/2026  
Source: FactSet (consensus for all but SPCX), MS estimates

Exhibit 4: Short Interest vs. Key Comps  
![](images/f13b00ce71103e21df736306dd26c1ad139ce6c79acc1038edbf84d533a37f3b.jpg)  
Note: Market data as of 7/27/2026  
Source: FactSet, NASDAQ, MS

Exhibit 5: Historical Stock Performance

[中间内容因长度限制已省略]

. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Space Technology

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/27/2026)</td></tr><tr><td>Adam Jonas, CFA</td><td></td><td></td></tr><tr><td>SpaceX (SPCX.O)</td><td>O (07/07/2026)</td><td>$113.50</td></tr><tr><td>Gogo Inc (GOGO.O)</td><td>E (08/14/2025)</td><td>$3.99</td></tr><tr><td>Iridium Communications Inc (IRDM.O)</td><td>E (01/16/2026)</td><td>$45.96</td></tr><tr><td>MDA Space Ltd (MDA.TO)</td><td>O (01/16/2026)</td><td>C$42.18</td></tr><tr><td>Viasat Inc (VSAT.O)</td><td>E (12/15/2017)</td><td>$74.87</td></tr><tr><td colspan="3">Kristine T Liwag</td></tr><tr><td>Firefly Aerospace Inc (FLY.O)</td><td>E (09/02/2025)</td><td>$19.88</td></tr><tr><td>HawkEye 360 Inc (HAWK.N)</td><td>O (06/01/2026)</td><td>$19.78</td></tr><tr><td>Planet Labs PBC (PL.N)</td><td>E (01/22/2023)</td><td>$21.00</td></tr><tr><td>Rocket Lab USA Inc (RKLB.O)</td><td>O (01/16/2026)</td><td>$66.94</td></tr><tr><td>Virgin Galactic Holdings Inc (SPCE.N)</td><td>U (11/22/2023)</td><td>$2.53</td></tr><tr><td>Voyager Technologies Inc (VOYG.N)</td><td>U (07/15/2026)</td><td>$26.25</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

## © 2026 MS
"""
