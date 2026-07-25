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
# Asia Vital Components

## 2Q preview: Another strong GM beat; key beneficiary of ASIC and GPU cooling upgrade; OW

We expect AVC's 2Q26 results to beat on stronger-than-expected GM expansion (new JPMe $32.5\%$ vs BBGe $\sim 30\%$ ), despite the reported weaker revenue momentum given VR200 delay. The company's share price has underperformed the Taiex by $\sim 35\%$ in the past 3 months, owing to the VR cold plate order push-out from June to August. As the issues seem largely resolved, we believe AVC's revenue should resume momentum with VR mass production in August. The potential 2Q26 GM beat coupled with the reaccelerating revenue growth should revive sentiment on AVC, in our view. Looking further out, we see multiple catalysts ahead, including AWS Trainium 3 and Google TPU v8 cold plates entering mass production in 4Q26, as well as the VR Ultra cold plate content increase. OW.

\- 2Q26 preview. Reported 2Q26 revenue of NT\$49.1bn (flat QoQ, +66% YoY) was below both JPMe and consensus by 3%, given the delay in VR200 shipment. Despite softer revenue, we believe the company's 2Q26 GM could reach 32.5% (above old JPMe of 31.0%), which could likely beat the current Bloomberg estimate of \~30%, thanks to its decent yield and enhanced production efficiency. Coupled with well-managed opex and higher non-op income, we revise up our 2Q26 EPS estimate by 14% to NT\$24.5, meaningfully higher vs BBGe of NT\$21.4.

\- Revenue momentum expected to resume from Aug. Post the flattish 2Q26, we model AVC's 3Q26 revenue to resume momentum with $15\%$ QoQ growth, driven by the mass production of Nvidia's VR200 cold plate expected to start from August. In addition, we believe the liquid-cooled version of AWS Trainium 3 and Google TPU v8 cold plates will also start ramping up in 4Q26 with higher content value vs Nvidia systems. These new ASIC liquid cooling projects should drive another $16\%$ QoQ revenue growth in 4Q26, based on JPMe. In terms of GM, we think the increasing liquid cooling mix along with decent yield will contribute to further GM expansion to $34\%$ and $35\%$ in 3Q and 4Q26 (vs consensus still at $30.5\%$ and $31.4\%$ ).

\- VR Ultra liquid cooling content likely to further increase. Looking forward to future generations, we think AVC will continue to benefit from the structural content increase trend. For VR Ultra, we believe the liquid cooling content of its compute tray could further grow (after the $>50\%$ increase in VR vs GB), driven by the additional cold plate and QD unit adoption due to higher spec and power density. The design should be confirmed in the next few months.

\- Implications. We raise 2026 and 2027E EPS by 4% and 10% on accelerating GM growth and continued content increase in future GPU and ASIC systems. Hence, our Dec-26 PT is revised up to NT\$3,500 (from NT\$3,200) based on an unchanged 22x 2027E P/E, above AVC's historical average given its stronger 2024-27E \~100% earnings growth.

## Overweight

3017.TW, 3017 TT
Price (22 Jul 26):NT\$2,265.00

▲ Price Target (Dec-26):NT\$3,500.00
Prior (Dec-26):NT\$3,200.00

## Technology

William Yang AC (886-2) 2725-9899 william.yang@JPM.com

Megan Hsueh
(886-2) 2725-9249
megan.hsueh@JPM.com
JPM Securities (Taiwan) Limited

<table><tr><td colspan="4">Key Changes (FYE Dec)</td></tr><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 26E (NT$)</td><td>100.36</td><td>104.50</td><td>4.1%</td></tr><tr><td>Adj. EPS - 27E (NT$)</td><td>146.02</td><td>160.04</td><td>9.6%</td></tr></table>

## Quarterly Forecasts (FYE Dec)

<table><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>8.28</td><td>20.17A</td><td>31.93</td></tr><tr><td>Q2</td><td>10.30</td><td>24.52</td><td>36.79</td></tr><tr><td>Q3</td><td>13.67</td><td>27.04</td><td>42.97</td></tr><tr><td>Q4</td><td>17.01</td><td>32.77</td><td>48.36</td></tr><tr><td>FY</td><td>49.29</td><td>104.50</td><td>160.04</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>49</td><td>54</td><td>64</td><td>52</td><td>23</td></tr><tr><td>Growth</td><td>9</td><td>3</td><td>11</td><td>26</td><td>60</td></tr><tr><td>Momentum</td><td>34</td><td>12</td><td>4</td><td>4</td><td>49</td></tr><tr><td>Quality</td><td>3</td><td>15</td><td>15</td><td>15</td><td>32</td></tr><tr><td>Low Vol</td><td>76</td><td>85</td><td>93</td><td>83</td><td>74</td></tr></table>

Price Performance  
![](images/efffc166aade6797f30dfd68c2528af285e8d6d68295a98ae90381363b6a13da.jpg)

— 3017.TW Price (NT\$) — TSE (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>50.0%</td><td>-6.4%</td><td>-16.0%</td><td>165.8%</td></tr><tr><td>Rel</td><td>-4.8%</td><td>-0.3%</td><td>-34.3%</td><td>70.8%</td></tr></table>

<table><tr><td colspan="2">Company Data</td></tr><tr><td>Shares O/S (mn)</td><td>383</td></tr><tr><td>52-week range (NT$)</td><td>3,010.00-836.80</td></tr><tr><td>Market cap ($ mn)</td><td>26,800</td></tr><tr><td>Exchange rate</td><td>32.40</td></tr><tr><td>Free float (%)</td><td>74.5%</td></tr><tr><td>3M ADV (mn)</td><td>5.01</td></tr><tr><td>3M ADV ($ mn)</td><td>394.9</td></tr><tr><td>Volatility (90 Day)</td><td>70</td></tr><tr><td>Index</td><td>TAIEX</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>20|1|0</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>NT$ in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td></tr><tr><td colspan="4">Financial Estimates</td></tr><tr><td>Revenue</td><td>139,639</td><td>220,045</td><td>316,613</td></tr><tr><td>Adj. EBIT</td><td>27,556</td><td>61,072</td><td>95,329</td></tr><tr><td>Adj. EBITDA</td><td>30,802</td><td>65,416</td><td>100,301</td></tr><tr><td>Adj. net income</td><td>19,186</td><td>41,016</td><td>62,814</td></tr><tr><td>Adj. EPS</td><td>49.29</td><td>104.50</td><td>160.04</td></tr><tr><td>BBG EPS</td><td>49.50</td><td>94.69</td><td>137.25</td></tr><tr><td>Cashflow from operations</td><td>36,758</td><td>37,554</td><td>71,369</td></tr><tr><td>FCFF</td><td>29,528</td><td>29,921</td><td>67,260</td></tr><tr><td colspan="4">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>94.6%</td><td>57.6%</td><td>43.9%</td></tr><tr><td>EBIT margin</td><td>19.7%</td><td>27.8%</td><td>30.1%</td></tr><tr><td>EBIT Growth Y/Y (%)</td><td>154.6%</td><td>121.6%</td><td>56.1%</td></tr><tr><td>EBITDA margin</td><td>22.1%</td><td>29.7%</td><td>31.7%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>131.8%</td><td>112.4%</td><td>53.3%</td></tr><tr><td>Net margin</td><td>13.7%</td><td>18.6%</td><td>19.8%</td></tr><tr><td>Adj. EPS growth</td><td>131.9%</td><td>112.0%</td><td>53.1%</td></tr><tr><td colspan="4">Ratios</td></tr><tr><td>Adj. tax rate</td><td>27.2%</td><td>27.8%</td><td>28.0%</td></tr><tr><td>Interest cover</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROE</td><td>45.7%</td><td>64.7%</td><td>63.6%</td></tr><tr><td colspan="4">Valuation</td></tr><tr><td>FCFF yield</td><td>3.3%</td><td>3.4%</td><td>7.6%</td></tr><tr><td>Dividend yield</td><td>0.4%</td><td>0.9%</td><td>2.0%</td></tr><tr><td>EV/Revenue</td><td>4.3</td><td>4.5</td><td>3.0</td></tr><tr><td>EV/EBITDA</td><td>19.3</td><td>15.0</td><td>9.3</td></tr><tr><td>Adj. P/E</td><td>46.0</td><td>21.7</td><td>14.2</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

We are OW on AVC for its strong earnings growth potential, which we think is supported by the content increase in AI servers. We expect AVC to see increasing upside from more liquid cooling opportunities, with much higher ASP and margin, while its competitive advantages vs peers could give it further market share gains as the industry's structural trends develop.

## Valuation

Our Dec-26 PT of NT\$3,500 is based on 22x 2027E P/E, above the company's historical average P/E, given its stronger earnings growth of \~100% during 2024-27E.

Performance Drivers  
![](images/5219f64807ee56cfc262cb8d7b9bb7dd4f36e5d972ff5991438bb62093efcaae.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>0.10</td><td>0.23</td></tr><tr><td>Region: Taiwan</td><td>0.52</td><td>0.44</td></tr><tr><td colspan="3">Macro:</td></tr><tr><td>Emerging Economies CPI(YoY)</td><td>-0.23</td><td>-0.36</td></tr><tr><td>Citi Economic Surprise - EM</td><td>0.18</td><td>0.25</td></tr><tr><td>Emerging Central Bank Rate</td><td>0.26</td><td>-0.18</td></tr><tr><td colspan="3">Quant Styles:</td></tr><tr><td>Quality</td><td>0.37</td><td>0.26</td></tr><tr><td>Momentum</td><td>0.06</td><td>0.19</td></tr><tr><td>Size</td><td>0.12</td><td>0.14</td></tr></table>

## Earnings review and estimate revisions

Table 1: JPM estimates – New vs old

<table><tr><td rowspan="2">(NT$M)</td><td colspan="4">Revised</td><td colspan="4">Prior</td><td colspan="4">Change</td></tr><tr><td>2Q26E</td><td>3Q26E</td><td>2026E</td><td>2027E</td><td>2Q26E</td><td>3Q26E</td><td>2026E</td><td>2027E</td><td>2Q26E</td><td>3Q26E</td><td>2026E</td><td>2027E</td></tr><tr><td>Sales</td><td>49,121</td><td>56,313</td><td>220,045</td><td>316,613</td><td>50,399</td><td>61,274</td><td>228,609</td><td>310,552</td><td>-3%</td><td>-8%</td><td>-4%</td><td>2%</td></tr><tr><td>Gross profit</td><td>15,953</td><td>19,120</td><td>72,602</td><td>111,563</td><td>15,626</td><td>19,632</td><td>72,227</td><td>102,860</td><td>2%</td><td>-3%</td><td>1%</td><td>8%</td></tr><tr><td>GM</td><td>32.5%</td><td>34.0%</td><td>33.0%</td><td>35.2%</td><td>31.0%</td><td>32.0%</td><td>31.6%</td><td>33.1%</td><td>147 bps</td><td>191 bps</td><td>140 bps</td><td>211 bps</td></tr><tr><td>Operating profit</td><td>13,423</td><td>16,107</td><td>61,072</td><td>95,329</td><td>12,778</td><td>16,292</td><td>59,863</td><td>86,836</td><td>5%</td><td>-1%</td><td>2%</td><td>10%</td></tr><tr><td>OPM</td><td>27.3%</td><td>28.6%</td><td>27.8%</td><td>30.1%</td><td>25.4%</td><td>26.6%</td><td>26.2%</td><td>28.0%</td><td>197 bps</td><td>201 bps</td><td>157 bps</td><td>215 bps</td></tr><tr><td>Net Income</td><td>9,624</td><td>10,614</td><td>41,016</td><td>62,814</td><td>8,420</td><td>10,707</td><td>39,384</td><td>57,304</td><td>14%</td><td>-1%</td><td>4%</td><td>10%</td></tr><tr><td>EPS (NT$)</td><td>24.5</td><td>27.0</td><td>104.5</td><td>160.0</td><td>21.5</td><td>27.3</td><td>100.4</td><td>146.0</td><td>14%</td><td>-1%</td><td>4%</td><td>10%</td></tr></table>

Source: JPM estimates.

Table 2: JPM estimates vs Bloomberg consensus

<table><tr><td rowspan="2">(NT$M)</td><td colspan="4">JPMe</td><td colspan="4">Bloomberg</td><td colspan="4">Diff</td></tr><tr><td>2Q26E</td><td>3Q26E</td><td>2026E</td><td>2027E</td><td>2Q26E</td><td>3Q26E</td><td>2026E</td><td>2027E</td><td>2Q26E</td><td>3Q26E</td><td>2026E</td><td>2027E</td></tr><tr><td>Sales</td><td>49,121</td><td>56,313</td><td>220,045</td><td>316,613</td><td>50,465</td><td>57,590</td><td>220,165</td><td>298,353</td><td>-3%</td><td>-2%</td><td>0%</td><td>6%</td></tr><tr><td>Gross profit</td><td>15,953</td><td>19,120</td><td>72,602</td><td>111,563</td><td>15,272</td><td>17,659</td><td>67,133</td><td>93,692</td><td>4%</td><td>8%</td><td>8%</td><td>19%</td></tr><tr><td>GM</td><td>32.5%</td><td>34.0%</td><td>33.0%</td><td>35.2%</td><td>30.3%</td><td>30.7%</td><td>30.5%</td><td>31.4%</td><td>221 bps</td><td>329 bps</td><td>250 bps</td><td>383 bps</td></tr><tr><td>Operating profit</td><td>13,423</td><td>16,107</td><td>61,072</td><td>95,329</td><td>12,421</td><td>14,550</td><td>55,199</td><td>78,861</td><td>8%</td><td>11%</td><td>11%</td><td>21%</td></tr><tr><td>OPM</td><td>27.3%</td><td>28.6%</td><td>27.8%</td><td>30.1%</td><td>24.6%</td><td>25.3%</td><td>25.1%</td><td>26.4%</td><td>271 bps</td><td>334 bps</td><td>268 bps</td><td>368 bps</td></tr><tr><td>Net Income</td><td>9,624</td><td>10,614</td><td>41,016</td><td>62,814</td><td>8,463</td><td>9,899</td><td>37,361</td><td>53,893</td><td>14%</td><td>7%</td><td>10%</td><td>17%</td></tr><tr><td>EPS (NT$)</td><td>24.5</td><td>27.0</td><td>104.5</td><td>160.0</td><td>21.4</td><td>25.0</td><td>94.7</td><td>137.3</td><td>15%</td><td>8%</td><td>10%</td><td>17%</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates.

## Valuation

Table 3: AVC's trading multiple (from January 2023 to date, when AI server started booming)

<table><tr><td>x</td><td>12M trailing P/E</td><td>12M fwd P/E</td><td>12M trailing P/B</td><td>12M fwd P/B</td></tr><tr><td>Standard deviation</td><td>8.6</td><td>4.6</td><td>3.8</td><td>2.4</td></tr><tr><td>Max</td><td>47.1</td><td>24.7</td><td>19.1</td><td>12.4</td></tr><tr><td>Minimum</td><td>8.8</td><td>5.4</td><td>2.1</td><td>1.5</td></tr><tr><td>Median</td><td>26.5</td><td>14.4</td><td>7.2</td><td>5.1</td></tr><tr><td>Average</td><td>26.2</td><td>14.4</td><td>7.8</td><td>5.4</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates.

Figure 1: AVC's 1yr forward P/E  
![](images/a3be4d97ee3efb47315b5231f390b032af2dd84281b269e181bc994de5404d06.jpg)  
Source: Bloomberg Finance L.P., JPM estimates.

Figure 2: AVC's 1yr forward P/E vs mean  
![](images/b5c7a1a6887d62743e239ecd24860dcc6ecca9617c3c00614834174356b9310f.jpg)  
Source: Bloomberg Finance L.P., JPM estimates

Figure 3: AVC's 1yr forward P/B  
![](images/e6654f01606a42a8ccb80097937c0fa7907e3de402eb20f0ed190f47de6e2999.jpg)  
Source: Bloomberg Finance L.P., JPM estimates.

Figure 4: AVC's 1yr forward P/B vs mean  
![](images/ef7eac6a41180f306d3a2a1d6c4d9a709d20aebbc86f14c563ee131c395bfc62.jpg)  
Source: Bloomberg Finance L.P., JPM estimates.

Table 4: Income statement

<table><tr><td></td><td colspan="4">2023</td><td colspan="4">2024</td><td colspan="4">2025</td><td colspan="4">2026E</td><td colspan="4">2027E</td><td rowspan="2">2023</td><td rowspan="2">2024</td><td rowspan="2">2025</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td></tr><tr><td>(NT$ in Mn, year-end December)</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2QE</td><td>3QE</td><td>4QE</td><td>1QE</td><td>2QE</td><td>3QE</td><td>4QE</td></tr><tr><td>Revenue</td><td>11,835</td><td>14,871</td><td>15,769</td><td>16,720</td><td>15,309</td><td>16,484</td><td>19,065</td><td>20,904</td><td>23,333</td><td>29,595</td><td>38,937</td><td>47,775</td><td>49,038</td><td>49,121</td><td>56,313</td><td>65,573</td><td>65,431</td><td>73,092</td><td>84,471</td><td>93,619</td><td>59,194</td><td>71,761</td><td>139,639</td><td>220,045</td><td>316,613</td></tr><tr><td>Depreciation</td><td>427</td><td>452</td><td>498</td><td>512</td><td>537</td><td>572</td><td>609</td><td>666</td><td>748</td><td>727</td><td>815</td><td>896</td><td>996</td><td>1,040</td><td>1,099</td><td>1,124</td><td>1,165</td><td>1,198</td><td>1,238</td><td>1,273</td><td>1,889</td><td>2,384</td><td>3,186</td><td>4,260</td><td>4,429</td></tr><tr><td>COGS</td><td>9,498</td><td>11,880</td><td>12,353</td><td>13,075</td><td>11,936</td><td>12,690</td><td>14,584</td><td>15,680</td><td>17,305</td><td>22,370</td><td>28,765</td><td>35,165</td><td>34,441</td><td>33,168</td><td>37,193</td><td>42,641</td><td>42,869</td><td>47,402</td><td>54,611</td><td>60,168</td><td>46,806</td><td>54,891</td><td>103,605</td><td>147,443</td><td>205,050</td></tr><tr><td>Gross profit</td><td>2,336</td><td>2,991</td><td>3,416</td><td>3,645</td><td>3,372</td><td>3,794</td><td>4,480</td><td>5,224</td><td>6,028</td><td>7,224</td><td>10,172</td><td>12,610</td><td>14,597</td><td>15,953</td><td>19,120</td><td>22,932</td><td>22,562</td><td>25,690</td><td>29,860</td><td>33,451</td><td>12,388</t

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
