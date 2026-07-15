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
# Shengyi Tech (600183.SS): CCL shipments growth and price increase driving growth; 2Q26 NI guidance beat; Buy

Shengyi reported its 2Q26 preliminary result (link), with net income mid-point up $136\%$ YoY / $76\%$ QoQ, or $37\%$ / $44\%$ higher than our estimate / Bloomberg consensus. Management attributes the strong net income growth to (1) strong growth of high-end CCL business, supported by shipments growth and ASP improvement, (2) subsidiary's, Shengyi Electronics, strong AI PCB shipments growth, driven by the rising end demand from AIDC. We remain positive on Shengyi's growth ahead, supported by its capacity expansion, product mix upgrades toward AI CCL, price increases that offset rising raw material costs, and its accumulated experience in high-end CCL design and mass production. We factor in Shengyi's 2Q26 net income guidance and raise our 12M TP to Rmb247. Maintain Buy.

Allen Chang  
+852-2978-2930 |  
allen.k.chang@gs.com  
GS (Asia) L.L.C.

Verena Jeng  
+852-2978-1681 | verena.jeng@gs.com  
GS (Asia) L.L.C.

Yifan Hu  
+852-2978-0996 | yifan.hu@gs.com  
GS (Asia) L.L.C.

Exhibit 1: Shengyi 2Q26 net income guidance

<table><tr><td rowspan="2">Rmb m</td><td colspan="3">2Q26 pre-announcement</td><td rowspan="2">2Q26 GSe</td><td rowspan="2">Vs. Mid-point</td><td rowspan="2">2Q26 Consensus</td><td rowspan="2">Vs. Mid-point</td><td rowspan="2">2Q25</td><td rowspan="2">YoY</td><td rowspan="2">1Q26</td><td rowspan="2">QoQ</td></tr><tr><td>Low-end</td><td>High-end</td><td>Mid-point</td></tr><tr><td>Net income</td><td>1,941</td><td>2,140</td><td>2,040</td><td>1,486</td><td>37%</td><td>1,419</td><td>44%</td><td>863</td><td>136%</td><td>1,158</td><td>76%</td></tr></table>

Global Server TAM update: We updated our Global Server TAM in late Jun (report link) and raised: (1) AI servers implied AI chips shipments by 14% / 22% / 14% in 2026-28E, (2) US cloud service providers (CSPs) capex by 8% / 27% / 25% in 2026-28E, and (3) China CSP capex by 37% / 44% / 55% in 2026-28E. We expect Shengyi to benefit from the global cloud capex uptrend in coming years, considering its leading position in AI CCL and close partnership with leading AI PCB players, which would support Shengyi's revenue growth and profitability improvement.

Exhibit 2: 2025-30E waterfall chart: AI CCL and PCB as key drivers  
![](images/2cb228a8dc2032deea23aeb13073e729a2f5b29a2b7a79e7faa288b4faa81fdc.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: US CSP Capex trend  
Exhibit 3: Shengyi's revenue and GM trends  
![](images/50a05587e3151aca93fd47862198faecfdbbcdbb593857f47c197722f30d7b45.jpg)  
Source: Company data, GS Global Investment Research

![](images/f46238c74530a7bb9d42ae4c9d091db78d5e224cf0485ab96e02c0bc44f1a3c5.jpg)  
Data include Microsoft, Amazon, Meta, Alphabet and Oracle. For Microsoft, we use capex incl. financial lease. In FY24, 50% of the capex of Microsoft was spent on land and 50% on AI/Cloud.

Exhibit 5: China CSP capex trend  
![](images/1e084edb91405d0e701631018c40605b967a44276e4a3e6378c09c483c19faee.jpg)  
Data include Bytedance, Tencent, Alibaba, Baidu. We calculate Bytedance (private) relevant operating metrics by analyzing the industry and companies that our China Internet team cover, and then extrapolating them to Bytedance.  
Source: Company data, GS Global Investment Research  
Source: Company data, GS Global Investment Research

Earnings revision: We factor in Shengyi's 2Q26 net income guidance and raise our 2026-28E net incomes by $17\%$ / $1\%$ / $1\%$ , mainly on higher revenues. Our 2026-28E revenues are revised up by $11\%$ / $4\%$ / $3\%$ , mainly on higher contribution from CCL and PCB business, considering the company's price increases and capacity expansion. We raise our 2026-28E opex ratios, mainly on higher R&D spending, supporting the specification upgrades for AI CCL and PCB. Our estimate shows a GM uptrend in coming years, driven by the product mix upgrade towards AI CCL and PCB.

Exhibit 6: Earnings revision

<table><tr><td rowspan="2">Rmb mn</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td></tr><tr><td>Revenue</td><td>40,436</td><td>45,067</td><td>11%</td><td>68,034</td><td>70,931</td><td>4%</td><td>97,158</td><td>100,484</td><td>3%</td></tr><tr><td>GP</td><td>11,694</td><td>13,167</td><td>13%</td><td>21,018</td><td>21,934</td><td>4%</td><td>30,494</td><td>31,691</td><td>4%</td></tr><tr><td>OP</td><td>7,475</td><td>8,338</td><td>12%</td><td>14,241</td><td>14,415</td><td>1%</td><td>20,719</td><td>20,939</td><td>1%</td></tr><tr><td>Net income</td><td>5,821</td><td>6,790</td><td>17%</td><td>11,577</td><td>11,722</td><td>1%</td><td>16,975</td><td>17,158</td><td>1%</td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GM</td><td>28.9%</td><td>29.2%</td><td></td><td>30.9%</td><td>30.9%</td><td></td><td>31.4%</td><td>31.5%</td><td></td></tr><tr><td>OPM</td><td>18.5%</td><td>18.5%</td><td></td><td>20.9%</td><td>20.3%</td><td></td><td>21.3%</td><td>20.8%</td><td></td></tr><tr><td>NM</td><td>14.4%</td><td>15.1%</td><td></td><td>17.0%</td><td>16.5%</td><td></td><td>17.5%</td><td>17.1%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We continue to derive our 12M TP from near-term P/E, and we increase our 2027E target P/E to 50.4x (vs. 45x previously), based on the updated forward year earnings growth and trading P/E multiple of our peer group. This reflects our positive view on Shengyi's ability to benefit from the global growth trend in AI infrastructure. With our updated earnings estimates and target multiple, our 12M TP increases to Rmb247.0 (vs. Rmb217.6 previously). Maintain Buy.

Exhibit 7: The target P/E multiple is derived from correlation between peers P/E and earnings YoY  
![](images/4d3249cf0f01938e6d1c717af2df22c11ebfcda37037d3e735c7375a32981eb4.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 8: Shengyi 12M forward P/E  
![](images/93659ce5f222fcd5585c2a86b99f53f712420ebc3046a972c5454f4fcffc14ab.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 9: Shengyi P&L Summary

<table><tr><td>Rmb m</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>Rmb m</td></tr><tr><td colspan="5">Income statement</td><td colspan="4"></td><td colspan="8"></td><td>Income statement</td></tr><tr><td>Revenues</td><td>5,611</td><td>7,069</td><td>7,934</td><td>7,818</td><td>8,141</td><td>11,848</td><td>12,495</td><td>12,583</td><td>16,586</td><td>20,388</td><td>28,431</td><td>45,067</td><td>70,931</td><td>100,484</td><td>123,253</td><td>143,039</td><td>Revenues</td></tr><tr><td>GP</td><td>1,380</td><td>1,898</td><td>2,233</td><td>2,015</td><td>2,288</td><td>3,495</td><td>3,706</td><td>3,679</td><td>3,182</td><td>4,486</td><td>7,526</td><td>13,167</td><td>21,934</td><td>31,691</td><td>38,678</td><td>44,833</td><td>GP</td></tr><tr><td>OP</td><td>699</td><td>1,079</td><td>1,416</td><td>1,107</td><td>1,441</td><td>2,333</td><td>2,331</td><td>2,232</td><td>1,291</td><td>1,998</td><td>4,300</td><td>8,338</td><td>14,415</td><td>20,939</td><td>25,736</td><td>29,670</td><td>OP</td></tr><tr><td>Net income</td><td>564</td><td>863</td><td>1,017</td><td>891</td><td>1,158</td><td>2,060</td><td>1,830</td><td>1,743</td><td>1,164</td><td>1,739</td><td>3,334</td><td>6,790</td><td>11,722</td><td>17,158</td><td>20,973</td><td>24,277</td><td>Net income</td></tr><tr><td>EPS (Rmb)</td><td>0.23</td><td>0.36</td><td>0.35</td><td>0.37</td><td>0.48</td><td>0.86</td><td>0.76</td><td>0.73</td><td>0.50</td><td>0.74</td><td>1.31</td><td>2.84</td><td>4.90</td><td>7.17</td><td>8.76</td><td>10.14</td><td>EPS (Rmb)</td></tr><tr><td colspan="5">Margins</td><td colspan="4"></td><td colspan="8"></td><td>Margins</td></tr><tr><td>GM</td><td>24.6%</td><td>26.9%</td><td>28.1%</td><td>25.8%</td><td>28.1%</td><td>29.5%</td><td>29.7%</td><td>29.2%</td><td>19.2%</td><td>22.0%</td><td>26.5%</td><td>29.2%</td><td>30.9%</td><td>31.5%</td><td>31.4%</td><td>31.3%</td><td>GM</td></tr><tr><td>OPM</td><td>12.4%</td><td>15.3%</td><td>17.8%</td><td>14.2%</td><td>17.7%</td><td>19.7%</td><td>18.7%</td><td>17.7%</td><td>7.8%</td><td>9.8%</td><td>15.1%</td><td>18.5%</td><td>20.3%</td><td>20.8%</td><td>20.9%</td><td>20.7%</td><td>OPM</td></tr><tr><td>NM</td><td>10.0%</td><td>12.2%</td><td>12.8%</td><td>11.4%</td><td>14.2%</td><td>17.4%</td><td>14.6%</td><td>13.9%</td><td>7.0%</td><td>8.5%</td><td>11.7%</td><td>15.1%</td><td>16.5%</td><td>17.1%</td><td>17.0%</td><td>17.0%</td><td>NM</td></tr><tr><td colspan="5">Ratios</td><td colspan="4"></td><td colspan="8"></td><td>Ratios</td></tr><tr><td>Opex ratio</td><td>12.2%</td><td>11.6%</td><td>10.3%</td><td>11.6%</td><td>10.4%</td><td>9.8%</td><td>11.0%</td><td>11.5%</td><td>11.4%</td><td>12.2%</td><td>11.3%</td><td>10.7%</td><td>10.6%</td><td>10.7%</td><td>10.5%</td><td>10.6%</td><td>Opex ratio</td></tr><tr><td>Tax rate</td><td>11.6%</td><td>12.0%</td><td>10.8%</td><td>13.2%</td><td>12.9%</td><td>12.9%</td><td>12.9%</td><td>12.9%</td><td>9.6%</td><td>9.7%</td><td>11.9%</td><td>12.9%</td><td>13.0%</td><td>14.0%</td><td>15.0%</td><td>15.0%</td><td>Tax rate</td></tr><tr><td colspan="5">YoY</td><td colspan="4"></td><td colspan="8"></td><td>YoY</td></tr><tr><td>Revenues</td><td>27%</td><td>36%</td><td>55%</td><td>39%</td><td>45%</td><td>68%</td><td>57%</td><td>61%</td><td>-8%</td><td>23%</td><td>39%</td><td>59%</td><td>57%</td><td>42%</td><td>23%</td><td>16%</td><td>Revenues</td></tr><tr><td>GP</td><td>47%</td><td>68%</td><td>91%</td><td>62%</td><td>66%</td><td>84%</td><td>66%</td><td>83%</td><td>-20%</td><td>41%</td><td>68%</td><td>75%</td><td>67%</td><td>44%</td><td>22%</td><td>16%</td><td>GP</td></tr><tr><td>OP</td><td>58%</td><td>86%</td><td>189%</td><td>127%</td><td>106%</td><td>116%</td><td>65%</td><td>102%</td><td>-32%</td><td>55%</td><td>115%</td><td>94%</td><td>73%</td><td>45%</td><td>23%</td><td>15%</td><td>OP</td></tr><tr><td>Net income</td><td>44%</td><td>60%</td><td>131%</td><td>143%</td><td>105%</td><td>139%</td><td>80%</td><td>96%</td><td>-24%</td><td>49%</td><td>92%</td><td>104%</td><td>73%</td><td>46%</td><td>22%</td><td>16%</td><td>Net income</td></tr><tr><td colspan="5">QoQ</td><td colspan="4"></td><td colspan="8"></td><td>QoQ</td></tr><tr><td>Revenues</td><td>-1%</td><td>26%</td><td>12%</td><td>-1%</td><td>4%</td><td>46%</td><td>5%</td><td>1%</td><td rowspan="4" colspan="8"></td><td>Revenues</td></tr><tr><td>GP</td><td>11%</td><td>37%</td><td>18%</td><td>-10%</td><td>14%</td><td>53%</td><td>6%</td><td>-1%</td><td>GP</td></tr><tr><td>OP</td><td>44%</td><td>54%</td><td>31%</td><td>-22%</td><td>30%</td><td>62%</td><td>0%</td><td>-4%</td><td>OP</td></tr><tr><td>Net income</td><td>54%</td><td>53%</td><td>18%</td><td>-12%</td><td>30%</td><td>78%</td><td>-11%</td><td>-5%</td><td>Net income</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We derive our 12M TP of Rmb247 on a target P/E multiple of 50.4x 2027E EPS. Our target P/E of 50.4x is derived from the correlation between P/E and EPS growth of Shengyi Tech's peers, based on the company's 2027-28E EPS YoY growth.

Key risks: Lower-than-expected AI infrastructure investment, Lower-than-expected allocation, Change in the direction of technology.

<table><tr><td>600183.SS</td><td>12m Price Target: Rmb247.00</td><td colspan="2">Price: Rmb147.90</td><td colspan="2">Upside: 67.0%</td></tr><tr><td colspan="6"></td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap:</td><td>Revenue (Rmb mn) New</td><td>28,431.1</td><td>45,067.3</td><td>70,930.8</td><td>100,484.1</td></tr><tr><td>Rmb354.1bn / $52.2bn</td><td>Revenue (Rmb mn) Old</td><td>28,431.1</td><td>40,436.2</td><td>68,034.0</td><td>97,157.9</td></tr><tr><td>Enterprise value:</td><td>EBITDA (Rmb mn)</td><td>5,212.6</td><td>9,362.3</td><td>15,753.0</td><td>22,592.1</td></tr><tr><td>Rmb358.9bn / $52.9bn</td><td>EPS (Rmb) New</td><td>1.31</td><td>2.84</td><td>4.90</td><td>7.17</td></tr><tr><td>3m ADTV: Rmb9.6bn / $1.4bn</td><td>EPS (Rmb) Old</td><td>1.31</td><td>2.43</td><td>4.83</td><td>7.09</td></tr><tr><td>China</td><td>P/E (X)</td><td>30.8</td><td>52.2</td><td>30.2</td><td>20.6</td></tr><tr><td>Greater China Technology</td><td>P/B (X)</td><td>5.4</td><td>17.3</td><td>15.6</td><td>13.9</td></tr><tr><td>M&amp;A Rank: 3</td><td>Dividend yield (%)</td><td>2.8</td><td>1.7</td><td>2.9</td><td>4.2</td></tr><tr><td>Leases incl. in net debt &amp; EV?: No</td><td>CROCI (%)</td><td>29.3</td><td>32.0</td><td>46.1</td><td>56.5</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (Rmb)</td><td>0.48</td><td>0.86</td><td>0.76</td><td>0.73</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 14 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Yifan Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Yifan Hu GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis f

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
