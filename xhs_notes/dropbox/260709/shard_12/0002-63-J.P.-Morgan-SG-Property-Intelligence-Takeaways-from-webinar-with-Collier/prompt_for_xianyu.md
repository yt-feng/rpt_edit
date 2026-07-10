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
# SG Property Intelligence

Takeaways from webinar with Colliers' Head of Research; ASEAN Data Centers - SG optimizes efficiency; Malaysia adds MWs

Singapore Property & REITs - Takeaways from webinar with Colliers' Head of Research. We recently hosted Ms Catherine He, Colliers' Head of Research, on the Singapore property outlook. Colliers' view is that Singapore property markets remain fundamentally healthy, though growth is increasingly selective and bifurcated across sectors. The strongest themes are flight-to-quality in offices, resilience in suburban retail, selective opportunities in industrial assets, and moderation in residential demand. Across all sectors, supply remains constrained in the highest-quality segments, with prime CBD offices, premium suburban malls, modern logistics assets, and differentiated residential projects continuing to attract demand despite macro uncertainty. AI has emerged as an increasingly important demand driver, particularly for offices, business parks, and data centres. With the overall positive outlook for Singapore's commercial market, we reiterate our preference for Singapore-focused REITs with our top pick being CICT. Furthermore, we see value in "fallen angel" MPACT, powered by VivoCity and savings from lower SGD cost of debt. We also like CIT and UOL given their exposure to the resilient Singapore residential market and potential value unlock. We also believe the risk reward being attractive on the expected recovery in FLT and MLT. Link (Source: JPM)

ASEAN Data Centers - SG optimizes efficiency; Malaysia adds MWs Singapore's tightening of efficiency standards reinforces our positive view on Malaysia's data center (DC) sector. We see Singapore's proposed power usage effectiveness (PUE) requirements of \~1.25-1.3 (vs Malaysia's 1.4 threshold for hyperscalers) as a structural catalyst that sharpens the roles of both markets. Singapore remains the region's premium DC hub, optimizing scarce land and power resources, while Malaysia is emerging as the preferred destination for incremental hyperscale and AI capacity, supported by lower development costs (US\$7m/MW vs Singapore's US\$12m/MW, per Cushman & Wakefield estimates), faster execution and improving renewable energy access. In short, Singapore optimizes every MW; Malaysia captures the next MW. We remain constructive on both markets, with SCGB (OW) as our preferred Malaysia DC pure-play and KDCREIT (OW) as our preferred Singapore DC exposure. Link (Source: JPM)

## Companies

ESR-REIT is acquiring 5 freehold logistics assets in Melbourne for net A \$276.8m (c.S\$247.9m) at 5.5% initial NPI yield with total acquisition outlay of A\$303.0m (c.S\$271.3m), and completion targeted in 3Q 2026. On a FY2025 pro forma basis, the deal is guided to be +4.3% DPU accretive, while DPU accretion moderates to +1.3% assuming a Perpetual Securities Issuance of up to S\$175.0m. Pro forma aggregate leverage is expected at 41.9% post-acquisition, improving to 38.5% with the assumed S\$175.0m perpetuals. Funding is intended via divestment proceeds and debt financing with no new unit issuance, and the pro forma assumes new debt facilities of S\$271.3m at a 2.49% weighted-average all-in finance cost.

See page 7 for analyst certification and important disclosures, including non-US analyst disclosures.

Singapore/ASEAN Property and REITs

Terence M Khi AC (65) 6882-1518 terence.ml.khi@JPM.com

Mervin Song, CFA AC

(65) 6882-7829

mervin.song@JPM.com

JPM Securities Singapore Private Limited/JPM Securities (Asia Pacific) Limited/JPM Broking (Hong Kong) Limited

(Source: ESR REIT)

Frasers Property Limited will divest five freehold logistics assets in Australia to ESR-REIT for A\$288.6m (c.S\$258.4m) cash consideration. The consideration is subject to an estimated A\$11.8m (c.S\$10.5m) completion adjustment in favour of the purchasers for unutilised rent incentives and a rental guarantee, implying net A\$276.8m (c.S\$247.9m). Separately, FPL is also selling a Sydney mall, Ed.Square Town Centre for A\$248m to PGIM's Real Estate Investment Group and Assembly Funds Management (AFM). (Source: Frasers Property Limited, The Business Times)

## Sector

URA's Controller of Housing issued updated guidance urging developers to apply anti-money laundering checks in a risk-proportionate way, clarifying that source-of-wealth and source-of-funds verification is not required for the vast majority of homebuyers. Developers can proceed once standard customer due diligence is done and there are no sanctions hits or adverse news, but must conduct enhanced due diligence, including source checks, for higher-risk profiles such as foreign politically exposed persons or links to higher-risk jurisdictions. (Source: The Business Times)

## Table 1: Upcoming events

\*If you are subject to the MiFID II Research Unbundling regime, you may only be eligible to participate in this event if you have the appropriate level of access to JPM. Please check your eligibility before participating/accessing. If you are unsure as to your eligibility, please reach out to your usual JPM contact.

<table><tr><td>Date / Time</td><td>Event</td><td>Speakers</td><td>Hosts</td><td>Call/Event description</td></tr><tr><td>23 Jul @ 12.30pm HK/SG</td><td>KDCREIT 1H26 results luncheon</td><td>Loh Hwee Long, CEO
Adam Lee, CFO
Charmaine Cai, Head of Portfolio Management
Ms Renee Goh, IR</td><td>Terence Khi</td><td>Physical luncheon for SG clients at Level 30, CapitaSpring. Virtual for overseas clients. Registration link</td></tr><tr><td>31 Jul @ 12.30pm HK/SG</td><td>FLT 3QFY26 business update luncheon</td><td>Ms Anthea Lee - CEO
Mr Ng Wah Keong - CFO
Mr Ng Chung Keat - Head of Investor Relations &amp; Sustainability</td><td>Mervin Song</td><td>Physical luncheon for SG clients at Level 30, CapitaSpring. Virtual for overseas clients. Registration link</td></tr><tr><td>6 Aug @ 12.30pm HK/SG</td><td>CLAR 1H26 results luncheon</td><td>Mr William Tay - CEO
Ms Koo Lee Sze - CFO
Mr James Goh - Head, Portfolio Management</td><td>Mervin Song</td><td>Physical luncheon for SG clients at Level 29, Capital Tower Virtual for overseas clients. Registration link</td></tr></table>

Source: JPM.

Table 2: Upcoming results/business updates

<table><tr><td>Company</td><td>Ticker</td><td>Date</td><td>Briefing Time/ Link</td></tr><tr><td>IGB REIT</td><td>IGBREIT.MK</td><td>22-Jul-26</td><td>PM</td></tr><tr><td>Keppel DC REIT</td><td>KDCREIT</td><td>23-Jul-26</td><td>AM</td></tr><tr><td>Mapletree Industrial Trust</td><td>MINT</td><td>23-Jul-26</td><td>PM</td></tr><tr><td>Suntec REIT</td><td>SUN</td><td>23-Jul-26</td><td>PM</td></tr><tr><td>CapitaLand Malaysia Trust</td><td>CLMT.MK</td><td>27-Jul-26</td><td>PM</td></tr><tr><td>KORE US REIT</td><td>KORE</td><td>28-Jul-26</td><td>AM</td></tr><tr><td>CapitaLand Ascott Trust</td><td>CLAS</td><td>28-Jul-26</td><td>AM</td></tr><tr><td>ESR REIT</td><td>EREIT</td><td>28-Jul-26</td><td>AM</td></tr><tr><td>CapitaLand India Trust</td><td>CLINT</td><td>29-Jul-26</td><td>AM</td></tr><tr><td>Keppel REIT</td><td>KREIT</td><td>29-Jul-26</td><td>AM</td></tr><tr><td>Digital Core REIT</td><td>DCREIT</td><td>29-Jul-26</td><td>PM</td></tr><tr><td>CDL Hospitality Trust</td><td>CDREIT</td><td>30-Jul-26</td><td>AM</td></tr><tr><td>Keppel Ltd</td><td>KEP</td><td>30-Jul-26</td><td>AM</td></tr><tr><td>Far East Hospitality Trust</td><td>FEHT</td><td>30-Jul-26</td><td>AM</td></tr><tr><td>Mapletree Pan Asia Commercial Trust</td><td>MPACT</td><td>30-Jul-26</td><td>PM</td></tr><tr><td>Seatrium Limited</td><td>STM</td><td>31-Jul-26</td><td>AM</td></tr><tr><td>CapitaLand China Trust</td><td>CLCT</td><td>5-Aug-26</td><td>AM</td></tr><tr><td>CapitaLand Ascendas REIT</td><td>CLAR</td><td>5-Aug-26</td><td>PM</td></tr><tr><td>CapitaLand Integrated Commercial Trust</td><td>CICT</td><td>12-Aug-26</td><td>AM</td></tr><tr><td>CapitaLand Investment Limited</td><td>CLI</td><td>13-Aug-26</td><td>AM</td></tr><tr><td>City Developments Limited</td><td>CIT</td><td>13-Aug-26</td><td>AM</td></tr></table>

Source: Company data.

Table 3: Developer peer valuations comparison

<table><tr><td rowspan="2">Developer</td><td rowspan="2">Ticker</td><td rowspan="2">JPM Rating</td><td rowspan="2">Mkt Cap (US$ m)</td><td rowspan="2">Sh price 07-Jul (S$)</td><td rowspan="2">Price Target (S$)</td><td rowspan="2">Upside (%)</td><td rowspan="2">RNAV (S$)</td><td rowspan="2">RNAV Disc/Prem (%)</td><td rowspan="2">P/B (x)</td><td colspan="2">Dividend Yield</td><td rowspan="2">20 Day ADTV (US$m)</td><td rowspan="2">ROE FY26E (%)</td><td colspan="2">EV EBITDA</td><td rowspan="2">YTD Sh Perf (%)</td></tr><tr><td>FY26E (%)</td><td>FY27E (%)</td><td>FY26E</td><td>FY27E</td></tr><tr><td>City Developments</td><td>CIT</td><td>OW</td><td>5,498</td><td>7.95</td><td>10.45</td><td>31.4%</td><td>13.90</td><td>-43%</td><td>0.76</td><td>1.5%</td><td>1.5%</td><td>13.1</td><td>1.5%</td><td>22.7</td><td>18.7</td><td>-0.6%</td></tr><tr><td>UOL Group</td><td>UOL</td><td>OW</td><td>6,290</td><td>9.59</td><td>12.00</td><td>25.1%</td><td>15.00</td><td>-36%</td><td>0.69</td><td>2.6%</td><td>2.6%</td><td>8.3</td><td>4.2%</td><td>15.2</td><td>14.4</td><td>9.7%</td></tr><tr><td>Total/Wtd Avg</td><td></td><td></td><td>11,788</td><td></td><td></td><td>28.1%</td><td></td><td>-39%</td><td>0.72</td><td>2.1%</td><td>2.1%</td><td></td><td></td><td>18.7</td><td>16.4</td><td>4.9%</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates.

Table 4: Regional REIM peer valuations comparison

<table><tr><td rowspan="2">Cty</td><td rowspan="2">REIT/Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap (US$m)</td><td rowspan="2">LCY</td><td rowspan="2">Sh Px 07-Jul (LC)</td><td rowspan="2">TP (LC)</td><td rowspan="2">Upside (%)</td><td rowspan="2">JPM Rtg</td><td colspan="2">EV/EBITDA</td><td colspan="2">PE</td><td colspan="2">Div Yield</td><td rowspan="2">PB (x)</td><td rowspan="2">ADTV 20D (US$m)</td><td rowspan="2">ROE 1FY (%)</td><td rowspan="2">YTD (%)</td></tr><tr><td>1FY (x)</td><td>2FY (x)</td><td>1FY (x)</td><td>2FY (x)</td><td>1FY (%)</td><td>2FY (%)</td></tr><tr><td>SG</td><td>CapitaLand Invest.</td><td>CLI SP</td><td>9,664</td><td>SGD</td><td>2.50</td><td>3.10</td><td>24.0%</td><td>OW</td><td>16.2</td><td>16.3</td><td>22.8</td><td>22.4</td><td>4.8%</td><td>4.8%</td><td>1.0</td><td>20</td><td>4.4%</td><td>-7.7%</td></tr><tr><td>SG</td><td>Keppel Ltd</td><td>KEP SP</td><td>15,249</td><td>SGD</td><td>10.94</td><td>12.05</td><td>10.1%</td><td>OW</td><td>16.4</td><td>14.6</td><td>19.0</td><td>16.4</td><td>3.8%</td><td>4.0%</td><td>1.9</td><td>27</td><td>9.9%</td><td>6.8%</td></tr><tr><td>AU</td><td>Charter Hall Group</td><td>CHC AU</td><td>7,309</td><td>AUD</td><td>22.25</td><td>22.00</td><td>-1.1%</td><td>N</td><td>15.3</td><td>13.7</td><td>21.4</td><td>19.3</td><td>2.3%</td><td>2.4%</td><td>3.5</td><td>32</td><td>17.1%</td><td>-9.0%</td></tr><tr><td>AU</td><td>Goodman Group</td><td>GMG AU</td><td>43,569</td><td>AUD</td><td>30.68</td><td>37.00</td><td>20.6%</td><td>OW</td><td>23.4</td><td>20.6</td><td>23.7</td><td>21.4</td><td>1.0%</td><td>1.0%</td><td>2.5</td><td>117</td><td>11.0%</td><td>-1.0%</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates.

Table 5: S-REIT peer valuations comparison

<table><tr><td rowspan="2">S-REITs</td><td rowspan="2">Ticker</td><td colspan="2">JPM</td><td>Sh Price</td><td colspan="3">Price</td><td colspan="3">Yield</td><td colspan="2">Yield excl Top-Ups</td><td colspan="2">Yield excl top ups, 100% fees in cash, 100% payout</td><td colspan="2">20 Day</td><td>YTD Sh</td><td></td></tr><tr><td>Rtg</td><td>Mkt Cap (US$ m)</td><td>7-Jul (S$)</td><td>Target (S$)</td><td>Upside (%)</td><td>P/B (x)</td><td>1FY (%)</td><td>2FY (%)</td><td>1FY (%)</td><td>2FY (%)</td><td>1FY (%)</td><td>2FY (%)</td><td>1FY (%)</td><td>2FY (%)</td><td>ADTV (US$m)</td><td>Gearing (%)</td><td>Perf (%)</td></tr><tr><td>CAPL Ascendas REIT</td><td>CLAR</td><td>OW</td><td>9,667</td><td>2.50</td><td>2.85</td><td>14.0%</td><td>1.09</td><td>6.0%</td><td>6.2%</td><td>6.0%</td><td>6.2%</td><td>5.8%</td><td>6.0%</td><td>38.7</td><td>42.0%</td><td>-11.0%</td><td></td><td></td></tr><tr><td>CAPL Ascott Trust</td><td>CLAS</td><td>N</td><td>2,710</td><td>0.91</td><td>0.90</td><td>-1.1%</td><td>0.78</td><td>6.7%</td><td>6.7%</td><td>6.3%</td><td>6.3%</td><td>5.5%</td><td>5.5%</td><td>5.6</td><td>38.9%</td><td>-3.3%</td><td></td><td></td></tr><tr><td>CAPL China Trust</td><td>CLCT</td><td>N</td><td>884</td><td>0.65</td><td>0.66</td><td>1.5%</td><td>0.63</td><td>7.3%</td><td>7.3%</td><td>7.3%</td><td>7.3%</td><td>6.2%</td><td>6.2%</td><td>1.3</td><td>41.4%</td><td>-16.1%</td><td></td><td></td></tr><tr><td>CAPL India Trust</td><td>CLINT</td><td>OW</td><td>1,186</td><td>1.03</td><td>1.28</td><td>24.3%</td><td>0.75</td><td>7.7%</td><td>8.2%</td><td>7.7%</td><td>8.2%</td><td>6.8%</td><td>7.3%</td><td>2.9</td><td>35.7%</td><td>-14.5%</td><td></td><td></td></tr><tr><td>CAPL Integ Comm</td><td>CICT</td><td>OW</td><td>14,840</td><td>2.41</td><td>2.75</td><td>14.1%</td><td>1.13</td><td>5.1%</td><td>5.3%</td><td>5.1%</td><td>5.3%</td><td>4.9%</td><td>5.2%</td><td>57.5</td><td>38.5%</td><td>0.9%</td><td></td><td></td></tr><tr><td>CDL Hospitality Trusts</td><td>CDREIT</td><td>N</td><td>758</td><td>0.77</td><td>0.85</td><td>11.1%</td><td>0.50</td><td>6.8%</td><td>6.8%</td><td>6.8%</td><td>6.8%</td><td>6.2%</td><td>6.2%</td><td>0.8</td><td>35.3%</td><td>-8.0%</td><td></td><td></td></tr><tr><td>Far East Hospitality Tr.</td><td>FEHT</td><td>N</td><td>908</td><td>0.57</td><td>0.60</td><td>5.3%</td><td>0.65</td><td>6.5%</td><td>6.6%</td><td>6.5%</td><td>6.6%</td><td>6.5%</td><td>6.6%</td><td>0.5</td><td>33.4%</td><td>-6.4%</td><td></td><td></td></tr><tr><td>Frasers Centrepoint Tr.</td><td>FCT</td><td>OW</td><td>3,518</td><td>2.23</td><td>2.60</td><td>16.6%</td><td>0.99</td><td>5.6%</td><td>5.8%</td><td>5.6%</td><td>5.8%</td><td>5.2%</td><td>5.4%</td><td>9.7</td><td>40.0%</td><td>-4.3%</td><td></td><td></td></tr><tr><td>Frasers Log. and Com.</td><td>FLT</td><td>OW</td><td>2,854</td><td>0.970</td><td>1.12</td><td>15.5%</td><td>0.87</td><td>5.8%</td><td>6.1%</td><td>5.6%</td><td>6.1%</td><td>4.7%</td><td>4.8%</td><td>7.4</td><td>33.7%</td><td>-1.3%</td><td></td><td></td></tr><tr><td>Keppel DC REIT</td><td>KDCREIT</td><td>OW</td><td>4,204</td><td>2.22</td><td>2.60</td><td>17.1%</td><td>1.30</td><td>5.0%</td><td>5.2%</td><td>5.0%</td><td>5.2%</td><td>4.8%</td><td>4.9%</td><td>18.2</td><td>35.1%</td><td>-0.8%</td><td></td><td></td></tr><tr><td>Keppel REIT</td><td>KREIT</td><td>OW</td><td>3,422</td><td>0.89</td><td>1.01</td><td>13.5%</td><td>0.70</td><td>5.8%</td><td>6.3%</td><td>5.3%</td><td>6.1%</td><td>4.1%</td><td>4.9%</td><td>11.8</td><td>40.2%</td><td>-8.7%</td><td></td><td></td></tr><tr><td>Mapletree Industrial Tr.</td><td>MINT</td><td>UW</td><td>4,265</td><td>1.93</td><td>1.85</td><td>-4.1%</td><td>1.05</td><td>6.0%</td><td>6.0%</td><td>6.0%</td><td>6.0%</td><td>5.9%</td><td>5.9%</td><td>11.1</td><td>34.0%</td><td>-6.6%</td><td></td><td></td></tr><tr><td>Mapletree Logistics Tr.</td><td>MLT</td><td>OW</td><td>4,835</td><td>1.22</td><td>1.40</td><td>14.8%</td><td>0.96</td><td>6.0%</td><td>6.1%</td><td>6.0%</td><td>6.1%</td><td>5.1%</td><td>5.2%</td><td>14.3</td><td>40.6%</td><td>-6.5%</td><td></td><td></td></tr><tr><td>Mapletree Pan Asia</td><td>MPACT</td><td>OW</td><td>5,359</td><td>1.31</td><td>1.45</td><td>10.7%</td><td>0.76</td><td>6.1%</td><td>6.2%</td><td>6.1%</td><td>6.2%</td><td>5.9%</td><td>5.9%</td><td>15.2</td><td>36.5%</td><td>-10.7%</td><td></td><td></td></tr><tr><td>Suntec REIT</td><td>SUN</td><td>OW</td><td>3,367</td><td>1.47</td><td>1.60</td><td>8.8%</td><td>0.72</td><td>5.1%</td><td>5.4%</td><td>5.1%</td><td>5.4%</td><td>4.4%</td><td>4.7%</td><td>7.0</td><td>41.6%</td><td>2.1%</td><td></td><td>

[中间内容因长度限制已省略]

t may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1)

Completed 08 Jul 2026 09:11 AM HKT
"""
