你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# Japan Equity Strategy: Monthly Wrap

Widening share price and earnings gap amid AI rally: AI stocks vs non-AI stocks

Amid the global rally in AI stocks, Japanese equities rose in May, with both the Nikkei 225 (up 11.9%) and TOPIX (up 6.2%) reaching record highs. The Nikkei 225, which has a high weighting of AI semiconductor stocks, surpassed 66,000 for the first time and briefly exceeded 67,000 on June 1. TOPIX, which represents the overall market, recovered to high levels seen before the Middle East conflict. The acceleration of the AI-driven market and momentum trading since April has widened the gap in share price performance between AI and non-AI stocks. Meanwhile, as earnings forecasts for AI semiconductor companies were quickly revised upward in May, P/E ratios declined (to levels seen in November 2025 during heightened concerns over excessive AI investment), easing signs of overheating. In Japan, memory and wire/cable stocks are the main reason behind the upward revisions to consensus estimates for FY2026 EPS to grow 60% at AI semiconductor stocks. As the performance gap between AI stocks and IT services/games, and between external demand and domestic demand stocks continues to widen in one direction, we are closely monitoring the outlook for earnings at AI-related (memory, wire/cable) stocks and non-AI stocks. Regarding the macro environment, the rise in long-term interest rates following the mid-May supplementary budget has become a key theme. The government will announce its Basic Policy on Economic and Fiscal Management and Reform in early July. The government has indicated that it intends to use bridge JGBs to fund growth investments, and while the outlook for comprehensive medium-term fiscal policy may remain uncertain for some time, the current administration has consistently emphasized market credibility and has delivered solid fiscal results since taking office. As a base case scenario, we therefore believe an immediate negative reaction in the equity market is unlikely. With an 80% probability of a rate hike already priced in for the June BoJ MPM, we also focus on the impact of forex.

\- Share price performance in May: Japanese equities rose in May, with both the Nikkei 225 (up $11.9\%$ ) and TOPIX (up $6.2\%$ ) reaching record highs. The Nikkei 225, which has a high weighting of AI semiconductor stocks, surpassed 66,000 for the first time and briefly exceeded 67,000 on June 1 (our end-2026 forecast: 70,000). TOPIX recovered to high levels seen before the Middle East conflict. The NT ratio (Nikkei Stock Average/TOPIX ratio) reached a record high of 16.8x (16.2x at end-April; Figure 4). In May, the S&P 500 rose $5.1\%$ , the Nasdaq climbed $8.4\%$ to a record high, and the STOXX 600 gained $2.4\%$ (Figure 1). Asian technology markets, including KOSPI and MSCI Taiwan, also posted sharp gains across the board. Aside from AI, strong corporate earnings (with March fiscal year results exceeding expectations) and continued inflows from overseas investors supported the Japanese equity market. However, there were periods when rising long-term interest rates were perceived as a risk. In mid-May, as crude oil prices remained elevated and news reports emerged about the government's supplementary budget, the 10-year JGB yield briefly exceeded $2.8\%$ , reaching a 29-year high, which weighed on share prices (see report). Toward the end of the month, reports of a US-Iran agreement including a 60-day ceasefire and reopening of the Strait of Hormuz supported share price gains. Breaking down the drivers of May share price

# Equity Strategy

# Rie Nishihara AC

(81-3) 6736-8629

rie.nishihara@JPM.com

JPM Securities Japan Co., Ltd.

# Yong Guo, CFA

(81-3) 6736-8623

yong.guo@JPM.com

JPM Securities Japan Co., Ltd.

# Mansi Das

(91) 2261 573343

mansi.das@jpmchase.com

JPM India Private Limited

# Mislav Matejka, CFA

(44-20) 7134-9741

mislav.matejka@JPM.com

JPM Securities plc

# Rajiv Batra

(65) 6882-8151

rajiv.j.batra@JPM.com

JPM Securities Singapore Private Limited

# Dubravko Lakos-Bujas

(1-212) 622-3601

dubravko.lakos-bujas@JPM.com

JPM Securities LLC

performance, EPS contributed +4.1 points and P/E valuation expansion contributed +2.7 points, indicating that profit growth led the performance gains (Figure 8).

\- May sector, style and individual stock trends: By sector, AI semiconductor-related stocks (electric equipment & precision instruments, non-ferrous metals) and AI-infrastructure beneficiaries led the market higher (Nikkei Semiconductor Index MTD +23.5%). Domestic sectors such as real estate, energy, food, transportation, and utilities declined on rising rates and the Middle East conflict (Figure 6: domestic demand index -0.9%, overseas demand index +17.0%; Figure 1). During the mid-month yield spike, AI semiconductor-related stocks sold off and triggered a rotation into banks and lagging domestic demand sectors, though this proved short-lived as yields stabilized. By style, momentum, risk, capex, and growth stocks outperformed, while quality, dividend, and EPS revision stocks lagged (Figure 13). Among Nikkei 225 stocks, the best performers in May included MLCC-related stock names such as Taiyo Yuden, Murata, Kioxia, Ibiden and Sumco, whereas worst performers included Sumitomo Realty, Fujikura, Nippon Electric Glass and Mitsubishi Heavy Industries.

\- EPS forecasts and valuations: As of end-May 2026, TOPIX EPS growth was +10.8% YoY, above our forecast of +8.4% for FY2025, and IBES consensus estimates for FY2026 stand at +9.8% (-3.3 ppt versus one month ago, we forecast +10.4%), and +11.7% (+0.1 ppt versus one month ago) for FY2027. Estimates for FY2026 were reduced across the food, pharma, power, and transportation sectors due to the Middle East conflict, but were subsequently revised higher for FY2027 as the conflict's impact eased (Figure 28). 2026 EPS consensus forecasts are +23.5% YoY (+3.7 ppt versus one month ago) for the US and +16.9% (+1.0 ppt) for Europe (IBES consensus estimates; Figure 27). Looking at valuations, TOPIX's 12-month forward P/E as of end-May was 16.9x, so it has settled into the center of a new range after the rapid rise following Japan's February election (IBES consensus estimate basis; Figure 29). By sector, valuations seem somewhat high for basic materials & chemicals, electric appliances, trading companies & wholesalers, and transportation, while valuations are low for energy & resources, IT & services, retail, food, power, and real estate (versus averages over the past year; Figure 11).

\- Flows and positions: According to TSE trading data through May 22, overseas investors were net buyers of Japanese equities by ¥0.8 trillion in May, bringing their YTD cumulative net buying to ¥6.24 trillion (breaking down into cash market net buying of ¥10.9 trillion and futures net selling of ¥4.6 trillion). Trust banks, investment trusts and retail investors were marginally net sellers (Figure 37). According to the May QUICK Survey (response period: May 12–May 14), investors maintained overweight positions in electric machinery & precision instruments, steel, machinery, communications and financials, and expanded their overweight positions in real estate and construction. Meanwhile, they expanded underweight positions in autos and utilities, downgraded pharma and foods to underweight, and were neutral on materials and consumer goods (Figure 47& Figure 48).

# • Key reports:

(1) Japan Equity Monthly Strategy: Sustainability of AI rally amid rising rates   
(2) Japanese equities heading into a phase of 3% yields; where to go, AI and financials?   
(3) FY2025 earnings wrap: Stronger-than-expected FY2025 results driven by AI semiconductors and banks

# Share price performance

Figure 1: Equities, rates, and FX movement 

<table><tr><td rowspan="2">Indicators (as of 2026/05/29)</td><td rowspan="2">2026</td><td colspan="5">Quarterly</td><td colspan="13">Monthly</td><td colspan="5">Weekly</td></tr><tr><td>25-Q2</td><td>25-Q3</td><td>25-Q4</td><td>26-Q1</td><td>26-Q2</td><td>25-May</td><td>25-Jun</td><td>25-Jul</td><td>25-Aug</td><td>25-Sep</td><td>25-Oct</td><td>25-Nov</td><td>25-Dec</td><td>26-Jan</td><td>26-Feb</td><td>26-Mar</td><td>26-Apr</td><td>26-May</td><td>05/01</td><td>05/08</td><td>05/15</td><td>05/22</td><td>05/29</td></tr><tr><td>TOPIX</td><td>16.1%</td><td>7.3%</td><td>10.0%</td><td>8.6%</td><td>2.6%</td><td>13.1%</td><td>5.0%</td><td>1.8%</td><td>3.2%</td><td>4.5%</td><td>2.0%</td><td>6.2%</td><td>1.4%</td><td>0.9%</td><td>4.6%</td><td>10.4%</td><td>-11.2%</td><td>6.6%</td><td>6.2%</td><td>0.3%</td><td>2.7%</td><td>0.9%</td><td>0.7%</td><td>1.7%</td></tr><tr><td>Nikkei 225</td><td>31.8%</td><td>13.7%</td><td>11.0%</td><td>12.0%</td><td>1.4%</td><td>29.9%</td><td>5.3%</td><td>6.6%</td><td>1.4%</td><td>4.0%</td><td>5.2%</td><td>16.6%</td><td>-4.1%</td><td>0.2%</td><td>5.9%</td><td>10.4%</td><td>-13.2%</td><td>16.1%</td><td>11.9%</td><td>-0.3%</td><td>5.4%</td><td>2.1%</td><td>3.1%</td><td>4.7%</td></tr><tr><td>Nikkei Semiconductor Index</td><td>100.0%</td><td>26.0%</td><td>12.3%</td><td>21.1%</td><td>18.9%</td><td>68.2%</td><td>11.1%</td><td>17.5%</td><td>0.4%</td><td>-2.5%</td><td>14.7%</td><td>24.0%</td><td>-7.4%</td><td>5.4%</td><td>28.7%</td><td>9.4%</td><td>-15.5%</td><td>36.2%</td><td>23.5%</td><td>1.2%</td><td>11.0%</td><td>-4.3%</td><td>8.5%</td><td>7.4%</td></tr><tr><td>Nikkei Domestic-demand 50</td><td>1.0%</td><td>5.6%</td><td>13.6%</td><td>6.4%</td><td>2.7%</td><td>-1.7%</td><td>2.4%</td><td>1.0%</td><td>3.5%</td><td>8.1%</td><td>1.6%</td><td>-0.7%</td><td>7.5%</td><td>-0.3%</td><td>1.8%</td><td>12.6%</td><td>-10.4%</td><td>-0.8%</td><td>-0.9%</td><td>0.7%</td><td>0.5%</td><td>-0.1%</td><td>-0.8%</td><td>0.3%</td></tr><tr><td>Nikkei Overseas-demand 50</td><td>30.5%</td><td>5.5%</td><td>11.8%</td><td>11.6%</td><td>-1.0%</td><td>31.7%</td><td>4.7%</td><td>3.7%</td><td>2.8%</td><td>3.8%</td><td>4.9%</td><td>8.9%</td><td>1.0%</td><td>1.4%</td><td>4.6%</td><td>11.2%</td><td>-14.8%</td><td>12.6%</td><td>17.0%</td><td>0.8%</td><td>5.7%</td><td>1.3%</td><td>0.9%</td><td>8.2%</td></tr><tr><td>S&amp;P500</td><td>10.7%</td><td>10.6%</td><td>7.8%</td><td>2.3%</td><td>-4.6%</td><td>16.1%</td><td>6.2%</td><td>5.0%</td><td>2.2%</td><td>1.9%</td><td>3.5%</td><td>2.3%</td><td>0.1%</td><td>-0.1%</td><td>1.4%</td><td>-0.9%</td><td>-5.1%</td><td>10.4%</td><td>5.1%</td><td>0.9%</td><td>2.3%</td><td>0.1%</td><td>0.9%</td><td>9.4%</td></tr><tr><td>US Magnificent 7</td><td>7.6%</td><td>20.9%</td><td>17.5%</td><td>4.4%</td><td>-12.1%</td><td>22.5%</td><td>13.3%</td><td>6.1%</td><td>5.8%</td><td>1.9%</td><td>9.0%</td><td>4.9%</td><td>-1.2%</td><td>0.7%</td><td>0.6%</td><td>-7.3%</td><td>-5.7%</td><td>14.9%</td><td>6.6%</td><td>0.6%</td><td>4.0%</td><td>0.4%</td><td>-0.8%</td><td>8.3%</td></tr><tr><td>S&amp;P500 ex. Mag 7</td><td>11.5%</td><td>6.3%</td><td>4.1%</td><td>1.7%</td><td>-1.0%</td><td>12.6%</td><td>3.7%</td><td>3.8%</td><td>0.0%</td><td>2.2%</td><td>1.9%</td><td>0.5%</td><td>1.4%</td><td>-0.2%</td><td>2.2%</td><td>2.1%</td><td>-5.2%</td><td>7.9%</td><td>4.4%</td><td>0.9%</td><td>1.3%</td><td>-0.1%</td><td>2.0%</td><td>1.5%</td></tr><tr><td>Nasdaq</td><td>16.1%</td><td>17.7%</td><td>11.2%</td><td>2.6%</td><td>-7.1%</td><td>24.9%</td><td>9.6%</td><td>6.6%</td><td>3.7%</td><td>1.6%</td><td>5.6%</td><td>4.7%</td><td>-1.5%</td><td>-0.5%</td><td>0.9%</td><td>-3.4%</td><td>-4.8%</td><td>15.3%</td><td>8.4%</td><td>1.1%</td><td>4.5%</td><td>-0.1%</td><td>0.5%</td><td>2.4%</td></tr><tr><td>The Philadelphia Semiconductor</td><td>81.1%</td><td>29.9%</td><td>14.8%</td><td>11.2%</td><td>7.1%</td><td>69.1%</td><td>12.5%</td><td>16.6%</td><td>1.1%</td><td>1.1%</td><td>12.4%</td><td>13.5%</td><td>-2.8%</td><td>0.8%</td><td>12.9%</td><td>1.2%</td><td>-6.3%</td><td>38.4%</td><td>22.1%</td><td>0.8%</td><td>11.1%</td><td>-1.3%</td><td>5.3%</td><td>6.1%</td></tr><tr><td>NY Dow</td><td>6.2%</td><td>5.0%</td><td>5.2%</td><td>3.6%</td><td>-3.6%</td><td>10.1%</td><td>3.9%</td><td>4.3%</td><td>0.1%</td><td>3.2%</td><td>1.9%</td><td>2.5%</td><td>0.3%</td><td>0.7%</td><td>1.7%</td><td>0.2%</td><td>-5.4%</td><td>7.1%</td><td>2.8%</td><td>0.5%</td><td>0.2%</td><td>-0.2%</td><td>2.1%</td><td>9.9%</td></tr><tr><td>Russel 2000</td><td>17.6%</td><td>8.1%</td><td>12.0%</td><td>1.9%</td><td>0.6%</td><td>16.9%</td><td>5.2%</td><td>5.3%</td><td>1.7%</td><td>7.0%</td><td>3.0%</td><td>1.8%</td><td>0.8%</td><td>-0.7%</td><td>5.3%</td><td>0.7%</td><td>-5.2%</td><td>12.2%</td><td>4.3%</td><td>0.9%</td><td>1.7%</td><td>2.4%</td><td>2.7%</td><td>8.7%</td></tr><tr><td>Euro STOXX 600</td><td>5.7%</td><td>1.4%</td><td>3.1%</td><td>6.1%</td><td>-1.5%</td><td>7.3%</td><td>4.0%</td><td>-1.3%</td><td>0.9%</td><td>0.7%</td><td>1.5%</td><td>2.5%</td><td>0.8%</td><td>2.7%</td><td>3.2%</td><td>3.7%</td><td>-8.0%</td><td>4.8%</td><td>2.4%</td><td>0.1%</td><td>0.1%</td><td>-0.6%</td><td>3.0%</td><td>0.1%</td></tr><tr><td>CSI300</td><td>5.7%</td><td>1.3%</td><td>17.9%</td><td>-0.2%</td><td>-3.9%</td><td>9.9%</td><td>1.8%</td><td>2.5%</td><td>3.5%</td><td>10.3%</td><td>3.2%</td><td>0.0%</td><td>-2.5%</td><td>2.3%</td><td>1.7%</td><td>0.1%</td><td>-5.5%</td><td>8.0%</td><td>1.8%</td><td>0.8%</td><td>1.3%</td><td>-0.1%</td><td>-0.3%</td><td>8.0%</td></tr><tr><td>KOSPI</td><td>101.1%</td><td>23.8%</td><td>11.5%</td><td>23.1%</td><td>19.9%</td><td>67.8%</td><td>5.5%</td><td>13.9%</td><td>5.7%</td><td>-1.8%</td><td>7.5%</td><td>19.9%</td><td>-4.4%</td><td>7.3%</td><td>24.0%</td><td>19.5%</td><td>-19.1%</td><td>30.6%</td><td>28.4%</td><td>1.9%</td><td>13.6%</td><td>-0.1%</td><td>4.7%</td><td>8.0%</td></tr><tr><td>UST2Y (%)</td><td>4.01</td><td>3.72</td><td>3.61</td><td>3.48</td><td>3.80</td><td>4.01</td><td>3.90</td><td>3.72</td><td>3.96</td><td>3.62</td><td>3.61</td><td>3.57</td><td>3.49</td><td>3.48</td><td>3.52</td><td>3.38</td><td>3.80</td><td>3.87</td><td>4.01</td><td>3.88</td><td>3.89</td><td>4.07</td><td>4.12</td><td>4.01</td></tr><tr><td>UST10Y (%)</td><td>4.44</td><td>4.23</td><td>4.15</td><td>4.17</td><td>4.32</td><td>4.44</td><td>4.40</td><td>4.23</td><td>4.38</td><td>4.23</td><td>4.15</td><td>4.08</td><td>4.02</td><td>4.17</td><td>4.24</td><td>3.94</td><td>4.32</td><td>4.37</td><td>4.44</td><td>4.37</td><td>4.36</td><td>4.59</td><td>4.56</td><td>4.44</td></tr><tr><td>JGB10Y (%)</td><td>2.66</td><td>1.43</td><td>1.64</td><td>2.06</td><td>2.35</td><td>2.66</td><td>1.49</td><td>1.43</td><td>1.55</td><td>1.59</td><td>1.64</td><td>1.66</td><td>1.81</td><td>2.06</td><td>2.24</td><td>2.11</td><td>2.35</td><td>2.52</td><td>2.66</td><td>2.50</td><td>2.47</td><td>2.71</td><td>2.75</td><td>2.66</td></tr><tr><td>USDJPY (Yen)</td><td>159.3</td><td>144.0</td><td>147.9</td><td>156.7</td><td>158.7</td><td>159.3</td><td>144.0</td><td>144.0</td><td>150.8</td><td>147.1</td><td>147.9</td><td>154.0</td><td>156.2</td><td>156.7</td><td>154.8</td><td>156.1</td><td>158.7</td><td>156.6</td><td>159.3</td><td>157.0</td><td>156.7</td><td>158.7</td><td>159.2</td><td>159.3</td></tr><tr><td>VIX</td><td>15.3</td><td>16.7</td><td>16.3</td><td>15.0</td><td>25.3</td><td>15.3</td><td>18.57</td><td>16.73</td><td>16.72</td><td>15.36</td><td>16.28</td><td>17.44</td><td>16.35</td><td>14.95</td><td>17.44</td><td>19.86</td><td>25.25</td><td>16.89</td><td>15.32</td><td>17.0</td><td>17.2</td><td>18.4</td><td>16.7</td><td>15.3</td></tr><tr><td>Overseas flow (Spot)</td><td>10.87</td><td>4.40</td><td>0.20</td><td>2.82</td><td>2.92</td><td>7.95</td><td>2.28</td><td>0.93</td><td>1.74</td><td>(0.12)</td><td>(1.41)</td><td>3.44</td><td>(0.34)</td><td>(0.28)</td><td>2.36</td><td>2.84</td><td>(2.28)</td><td>5.34</td><td>2.61</td><td>0.36</td><td>1.24</td><td>0.56</td><td>0.46</td><td>-</td></tr><tr><td>Overseas flow (Future)</td><td>(4.39)</td><td>(0.81)</td><td>2.75</td><td>(0.79)</td><td>(1.30

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 02 Jun 2026 09:50 PM JST

Disseminated 02 Jun 2026 09:52 PM JST
"""
