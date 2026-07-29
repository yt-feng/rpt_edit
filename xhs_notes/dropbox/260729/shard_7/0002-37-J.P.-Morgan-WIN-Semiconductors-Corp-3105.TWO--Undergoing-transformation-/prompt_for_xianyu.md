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
## WIN Semiconductors Corp

## Undergoing transformation led by LEO and optical

\- 2Q26 slight beat from optical; 3Q momentum decent. Win's 2Q26 rev/margins (+16%/2ppt QoQ) were largely in-line with street expectations, while EPS was a strong beat on investment income and USD appreciation. The revenue growth was driven by 1) earlier-than-expected optical receiver chip (PD) mass production (late 2Q vs 2H26), and 2) infrastructure (LEO plus datacenter related demand). Smartphone (cellular) demand was resilient on higher exposure to the high-end smartphone market, while Wi-Fi was the sole weak spot due to a memory shortage. Overall, Win's UTR increased 5ppt to 65% in 2Q. Looking ahead, we expect 3Q rev to grow 11% QoQ on 1) further PD volume ramp, and 2) rising LEO shipment. We believe the momentum from optical and Infra should continue to rise throughout 2026e, with optical fueling decent upside. As a result, we are now modelling 30% rev growth for 2026 (40%+/50%+ growth for Infra/Optical) vs our previous \~10% rev growth estimates. We are also revising up rev growth from 13% to 20% for 2027e. Our new 2026/27e EPS estimates are 5/11% above our previous numbers.

\- Positive LT outlook for optical: with big order and more engagement ongoing. For the PD, Win so far only has one project in the mass-production stage. However, Win mentioned that the order scale of this customer (likely a major US design house) alone is capable of driving AI-related optical comm to reach a high-single-digit mix of total revenue in 2H26e, which has more than doubled vs 2025. We are modelling $50 + / 25\%+$ growth for Win's optical business in 2026/27e, with the AI optical mix reaching double digit of total rev in 2027e. In addition, Win also has multiple optical projects ongoing – including a short distance VCSEL laser chip project and long distance EML laser chip project that have entered mass production in 2025. Meanwhile, there are more projects in the early stages, including the CW laser project with a major US optical chip IDM (mass production should take place in YE27). As the largest compound semi foundry globally (with decent optical chip capabilities), we don't rule out the possibility of Win capturing more projects.

\- LEO growth on track; return to the expansion cycle. On the LEO front, we believe the LEO mix has reached double-digits, which is much earlier than our previous expectation of 2027e. We believe the strong demand brought by LEO together with optical could drive Win's overall UTR to $70\%+$ in 3Q26 ( $65\%$ in 2Q). The steadily rising UTR also drives Win Semi to return to the expansion cycle – although no massive capacity expansion yet, the company has started to conduct project-based capex starting 2H25, for de-bottleneck purpose for LEO and optical chips. The company re-iterated its 2026 capex plan to be NT \$2-3bn, which is significantly higher than the annual capex in prior years.

\- A transformation story: buy on pullback. After the strong rally in early 2026, Win's stock has corrected significantly in the past three months (-38% vs +12% of TaiEx). We believe this is due to 1) weak sentiment on both LEO and optical communications, and 2) concerns for Win's relatively slower mix rise in optical vs other companies in the same basket (as Win has exposure in other areas). However, Win's datacenter-related optical comm mix is growing rapidly and should reach double digits in 2027e (while LEO 15%+ mix in 2027e). We believe this could shift sentiment and drive Win's share once

Sources for: Style Exposure – JPM Global Markets Strategy; all other tables are company data and JPM estimates.

## Overweight

3105.TWO, 3105 TT
Price (24 Jul 26):NT\$341.50

▲ Price Target (Dec-26):NT\$373.00

Prior (Dec-26):NT\$336.00

## Technology

Jerry Tsai AC
(886-2) 2725-9867
jerry.tsai@JPM.com
JPM Securities (Taiwan) Limited

Josie Yu
(886-2) 2725-9877
josie.yu@JPM.com
JPM Securities (Taiwan) Limited

Gokul Hariharan
(852) 2800-8564
gokul.hariharan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Key Changes (FYE Dec)

<table><tr><td></td><td>Prev</td><td>Cur</td><td> $\Delta$ </td></tr><tr><td>Adj. EPS - 26E (NT$)</td><td>6.64</td><td>8.01</td><td>20.7%</td></tr><tr><td>Adj. EPS - 27E (NT$)</td><td>9.77</td><td>10.83</td><td>10.8%</td></tr></table>

## Quarterly Forecasts (FYE Dec)

<table><tr><td colspan="4">Adj. EPS (NT$)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>0.03</td><td>1.26A</td><td>2.29</td></tr><tr><td>Q2</td><td>(1.00)</td><td>2.30A</td><td>2.67</td></tr><tr><td>Q3</td><td>2.52</td><td>2.12</td><td>2.90</td></tr><tr><td>Q4</td><td>2.42</td><td>2.33</td><td>2.97</td></tr><tr><td>FY</td><td>3.99</td><td>8.01</td><td>10.83</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>88</td><td>94</td><td>72</td><td>82</td><td>70</td></tr><tr><td>Growth</td><td>76</td><td>74</td><td>93</td><td>82</td><td>76</td></tr><tr><td>Momentum</td><td>34</td><td>4</td><td>96</td><td>90</td><td>95</td></tr><tr><td>Quality</td><td>87</td><td>90</td><td>89</td><td>95</td><td>56</td></tr><tr><td>Low Vol</td><td>93</td><td>77</td><td>68</td><td>79</td><td>66</td></tr></table>

See page 8 for analyst certification and important disclosures, including non-US analyst disclosures.

Price Performance  
![](images/46a15927974f4137aee1f24a9c9f96b59fb58f76500990488fc44be2f1a54a3d.jpg)

— 3105.TWO Price (NT\$) — TSE (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>86.6%</td><td>-28.6%</td><td>-37.6%</td><td>289.0%</td></tr><tr><td>Rel</td><td>35.9%</td><td>-23.4%</td><td>-49.7%</td><td>202.2%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>423</td></tr><tr><td>52-week range (NT$)</td><td>637.00-80.30</td></tr><tr><td>Market cap ($ mn)</td><td>4,461</td></tr><tr><td>Exchange rate</td><td>32.38</td></tr><tr><td>Free float (%)</td><td>80.5%</td></tr><tr><td>3M ADV (mn)</td><td>26.91</td></tr><tr><td>3M ADV ($ mn)</td><td>410.3</td></tr><tr><td>Volatility (90 Day)</td><td>87</td></tr><tr><td>Index</td><td>TAIEX</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>11|5|4</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>NT$ in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td></tr><tr><td colspan="4">Financial Estimates</td></tr><tr><td>Revenue</td><td>16,639</td><td>21,679</td><td>26,040</td></tr><tr><td>Adj. EBIT</td><td>711</td><td>3,094</td><td>5,382</td></tr><tr><td>Adj. EBITDA</td><td>4,704</td><td>6,297</td><td>8,655</td></tr><tr><td>Adj. net income</td><td>1,690</td><td>3,397</td><td>4,591</td></tr><tr><td>Adj. EPS</td><td>3.99</td><td>8.01</td><td>10.83</td></tr><tr><td>BBG EPS</td><td>2.65</td><td>6.29</td><td>9.78</td></tr><tr><td>Cashflow from operations</td><td>6,276</td><td>5,515</td><td>6,999</td></tr><tr><td>FCFF</td><td>6,685</td><td>5,912</td><td>7,422</td></tr><tr><td colspan="4">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>(4.7%)</td><td>30.3%</td><td>20.1%</td></tr><tr><td>EBIT margin</td><td>4.3%</td><td>14.3%</td><td>20.7%</td></tr><tr><td>EBIT Growth Y/Y (%)</td><td>(6.2%)</td><td>335.3%</td><td>74.0%</td></tr><tr><td>EBITDA margin</td><td>28.3%</td><td>29.0%</td><td>33.2%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>(13.8%)</td><td>33.8%</td><td>37.5%</td></tr><tr><td>Net margin</td><td>10.2%</td><td>15.7%</td><td>17.6%</td></tr><tr><td>Adj. EPS growth</td><td>121.1%</td><td>101.0%</td><td>35.2%</td></tr><tr><td colspan="4">Ratios</td></tr><tr><td>Adj. tax rate</td><td>21.5%</td><td>17.9%</td><td>20.0%</td></tr><tr><td>Interest cover</td><td>9.0</td><td>13.0</td><td>16.4</td></tr><tr><td>Net debt/Equity</td><td>0.1</td><td>0.1</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>1.3</td><td>0.5</td><td>NM</td></tr><tr><td>ROE</td><td>4.2%</td><td>7.8%</td><td>9.8%</td></tr><tr><td colspan="4">Valuation</td></tr><tr><td>FCFF yield</td><td>4.6%</td><td>4.1%</td><td>5.1%</td></tr><tr><td>Dividend yield</td><td>0.3%</td><td>0.6%</td><td>0.0%</td></tr><tr><td>EV/Revenue</td><td>9.0</td><td>6.8</td><td>5.5</td></tr><tr><td>EV/EBITDA</td><td>32.0</td><td>23.5</td><td>16.6</td></tr><tr><td>Adj. P/E</td><td>85.7</td><td>42.6</td><td>31.5</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

We are OW on Win Semi, given its increasing exposure to LEO (Low Earth Orbital) and the long-term optical communication theme. Meanwhile, we expect the cellular business to remain stable as Win is more exposed to premium smartphones. In addition, the company's self-disciplined capex leads to a decrease in depreciation, which should also benefit margins in the next few years.

## Valuation

Our Dec-26 PT of NT\$373 is based on 34x 2027e EPS. 34x is 1.2-STD above the average multiple since 2016 (which excludes extremes). We believe the multiple assigned is justifiable given Win is riding on dual catalysts, and emerging drivers have effectively lifted multiples in the past.

![](images/e342f73c983780aba21cba5a37fa9720a7ee167103439488cba449071b423152.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>0.46</td><td>0.41</td></tr><tr><td>Region: Taiwan</td><td>0.32</td><td>0.25</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>HSI Volatility Index</td><td>-0.48</td><td>-0.37</td></tr><tr><td>JPM Global Equity Sentiment</td><td>0.39</td><td>0.37</td></tr><tr><td>JPM EMBI Global Spread</td><td>0.22</td><td>0.24</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>Value</td><td>-0.49</td><td>-0.34</td></tr><tr><td>DivYld</td><td>-0.52</td><td>-0.33</td></tr><tr><td>Growth</td><td>0.48</td><td>0.32</td></tr></table>

investors' spotlight is back to optical communications (or LEO). With an increasing mix of infrastructure and optical, Win is transforming from a cyclical cellular name to a datacomm enabler in the HPC/satellite era. Our new TP of NT\$373 is based on 34x (same as previous) 2027e EPS.

Figure 1: Win Semi annual revenue trend by application  
![](images/6f3d5da6c83a835e87fb9dfb1c5c7bd571652489a24add5b167e6f9b65c30146.jpg)  
Source: JPM estimates, Company data.

Figure 2: Win Semi revenue mix by application %  
![](images/9da7a0fb2ff8e0644e883f48a2f68f184fb5c4203b6ed76c73fc5c95aea0c2ac.jpg)  
Source: JPM estimates, Company data.

Figure 3: Win Semi capex trend  
![](images/842055a95803d662c95fc84a1e20871dded30263955808c3edca0e054022da1e.jpg)  
Source: JPM estimates, Company data.

Table 1: Win Semi 2Q26 earnings summary
NT\$mn

<table><tr><td></td><td colspan="3">2Q26</td><td colspan="2">Variance</td><td colspan="2">Growth</td></tr><tr><td>NT$ million</td><td>Actual</td><td>JPM est.</td><td>Consensus</td><td>vs. JPM</td><td>vs. Consensus</td><td>Q/Q</td><td>Y/Y</td></tr><tr><td>Revenue</td><td>5,257</td><td>4,546</td><td>5,298</td><td>16%</td><td>-1%</td><td>15%</td><td>39%</td></tr><tr><td>Gross profit</td><td>1,485</td><td>1,459</td><td>1,550</td><td>2%</td><td>-4%</td><td>23%</td><td>113%</td></tr><tr><td>Operating profit</td><td>742</td><td>636</td><td>705</td><td>17%</td><td>5%</td><td>73%</td><td>N.A.</td></tr><tr><td>Net profit</td><td>977</td><td>766</td><td>656</td><td>28%</td><td>49%</td><td>84%</td><td>N.A.</td></tr><tr><td>Adjusted EPS (NT$)</td><td>2.30</td><td>1.81</td><td>1.51</td><td>27%</td><td>53%</td><td>84%</td><td>N.A.</td></tr><tr><td>Gross margin</td><td>28.2%</td><td>32.1%</td><td>29.3%</td><td>-386bps</td><td>-101bps</td><td>191bps</td><td>979bps</td></tr><tr><td>Operating margin</td><td>14.1%</td><td>14.0%</td><td>13.3%</td><td>12bps</td><td>81bps</td><td>475bps</td><td>1,729bps</td></tr><tr><td>Net margin</td><td>18.6%</td><td>16.8%</td><td>12.4%</td><td>173bps</td><td>620bps</td><td>699bps</td><td>2,975bps</td></tr></table>

Source: JPM estimates, Company data, and Bloomberg Finance L.P.

Table 2: I/S Highlights: Annual Revised vs Previous NT\$ mn except for EPS

<table><tr><td rowspan="2"></td><td colspan="3">Revised</td><td colspan="3">Previous</td><td colspan="3">Change</td></tr><tr><td>FY25</td><td>FY26E</td><td>FY27E</td><td>FY25</td><td>FY26E</td><td>FY27E</td><td>FY25</td><td>FY26E</td><td>FY27E</td></tr><tr><td>Revenues</td><td>16,639</td><td>21,679</td><td>26,040</td><td>16,638</td><td>17,955</td><td>20,236</td><td>0%</td><td>21%</td><td>29%</td></tr><tr><td>Gross profit</td><td>4,026</td><td>6,463</td><td>9,308</td><td>4,027</td><td>5,488</td><td>7,054</td><td>0%</td><td>18%</td><td>32%</td></tr><tr><td>GM (%)</td><td>24.2%</td><td>29.8%</td><td>35.7%</td><td>24.2%</td><td>30.6%</td><td>34.9%</td><td>0bps</td><td>-75bps</td><td>89bps</td></tr><tr><td>Operating profit</td><td>711</td><td>3,094</td><td>5,382</td><td>712</td><td>2,250</td><td>3,797</td><td>0%</td><td>38%</td><td>42%</td></tr><tr><td>OPM (%)</td><td>4.3%</td><td>14.3%</td><td>20.7%</td><td>4.3%</td><td>12.5%</td><td>18.8%</td><td>-1bps</td><td>174bps</td><td>190bps</td></tr><tr><td>Pre-Tax profit</td><td>1,383</td><td>3,742</td><td>5,316</td><td>1,384</td><td>2,269</td><td>3,929</td><td>0%</td><td>65%</td><td>35%</td></tr><tr><td>Net profit</td><td>1,690</td><td>3,397</td><td>4,591</td><td>1,691</td><td>2,815</td><td>4,143</td><td>0%</td><td>21%</td><td>11%</td></tr><tr><td>Net Margin</td><td>10.2%</td><td>15.7%</td><td>17.6%</td><td>10.2%</td><td>15.7%</td><td>20.5%</td><td>-1bps</td><td>-1bps</td><td>-284bps</td></tr><tr><td>EPS (NT$)</td><td>3.99</td><td>8.01</td><td>10.83</td><td>3.99</td><td>6.64</td><td>9.77</td><td>0%</td><td>21%</td><td>11%</td></tr></table>

Source: JPM estimates.

Table 3: I/S Highlights: Annual JPMe vs Consensus NT\$ mn except for EPS

<table><tr><td rowspan="2"></td><td colspan="3">JPMe</td><td colspan="3">Consensus</td><td colspan="3">Difference</td></tr><tr><td>FY25</td><td>FY26E</td><td>FY27E</td><td>FY25</td><td>FY26E</td><td>FY27E</td><td>FY25</td><td>FY26E</td><td>FY27E</td></tr><tr><td>Revenues</td><td>16,639</td><td>21,679</td><td>26,040</td><td>16,518</td><td>21,060</td><td>24,387</td><td>1%</td><td>3%</td><td>7%</td></tr><tr><td>Gross profit</td><td>4,026</td><td>6,463</td><td>9,308</td><td>3,802</td><td>6,314</td><td>8,587</td><td>6%</td><td>2%</td><td>8%</td></tr><tr><td>GM (%)</td><td>24.2%</td><td>29.8%</td><td>35.7%</td><td>23.0%</td><td>30.0%</td><td>35.2%</td><td>118bps</td><td>-17bps</td><td>53bps</td></tr><tr><td>Operating profit</td><td>711</td><td>3,094</td><td>5,382</td><td>514</td><td>2,832</td><td>3,917</td><td>38%</td><td>9%</td><td>37%</td></tr><tr><td>OPM (%)</td><td>4.3%</td><td>14.3%</td><td>20.7%</td><td>3.1%</td><td>13.4%</td><td>16.1%</td><td>116bps</td><td>82bps</td><td>460bps</td></tr><tr><td>Pre-Tax profit</td><td>1,383</td><td>3,742</td><td>5,316</td><td>780</td><td>2,966</td><td>3,604</td><td>77%</td><td>26%</td><td>47%</td></tr><tr><td>Net profit</td><td>1,690</td><td>3,397</td><td>4,591</td><td>1,125</td><td>2,787</td><td>3,244</td><td>50%</td><td>22%</td><td>42%</td></tr><tr><td>Net Margin</td><td>10.2%</td><td>15.7%</td><td>17.6%</td><td>6.8%</td><td>13.2%</td><td>13.3%</td><td>335bps</td><td>244bps</td><td>433bps</td></tr><tr><td>EPS (NT$)</td><td>3.99</td><td>8.01</td><td>10.83</td><td>2.65</td><td>6.57</td><td>7.65</td><td>50%</td><td>22%</td><td>42%</td></tr></table>

Source: JPM estimates, Bloomberg Finance L.P.

Table 4: JPM Quarterly and Annual Estimates
NT\$mn, year-end December

<table><tr><td></td><td colspan="4">FY24</td><td colspan="4">FY25</td><td colspan="4">FY26E</td><td colspan="4">FY27E</td><td colspan="6">Annual</td></tr><tr><td></td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2Q</td><td>3Q</td><td>

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
