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
# Eoptolink (300502.SZ): Accelerated ramp up of 800G/1.6T optical modules; 2Q26 NI guidance beat; Buy

Eoptolink announced 1H26 net income guidance at Rmb7bn\~Rmb9bn, suggesting 2Q26 NI grew 78%\~163% YoY to Rmb4.2bn to Rmb6.2bn, with 2Q midpoint NI beating our previous estimate by 44%. Management highlights strong demand growth on rising AI capex spending, and the company's product mix upgrade towards high-speed optical modules. We attribute the stronger than expected revenues and NI QoQ growth to improving optics chipset supply and ramp up of the company's 800G/ 1.6T optical modules, along with its capacity expansion. We expect the shipment and value contribution from 800G+ optical modules continue to increase in 2H26E, and expansion from scale-out to scale-up/ scale across from 2027E. Maintain Buy with new TP at Rmb633.

Ting Song
+852-2978-6466 | ting.song@gs.com
GS (Asia) L.L.C.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

800G/ 1.6T optical module ramp up ahead: With improving optics chipset supply and the company's capacity expansion, we see shipment ramp up of 800G/ 1.6T optical modules will drive QoQ revenue growth. Looking into 2H, we expect the contribution from 1.6T modules and Silicon photonics products to continue to increase, supported by continuous improvement of chipset supply and rising demand from clients on 800G+ products. Despite near-term tight industry supply of optics chips, we expect rising Silicon Photonics penetration and industry capacity expansion to support shipment ahead.

Exhibit 1: Rising contribution from 800G/1.6T optical modules in 2026/27E  
![](images/3ab0f924c90c03aa17eeeef2bb8d44d42d00b66e85d0219c2db76d0911bc40ae.jpg)  
Source: Company data, GS Global Investment Research

Earnings revision: We factor in Eoptolink 2Q26E guidance, and revise up earnings by 7%/ 2%/ 2% in 2026-28E mainly on higher revenues of 800G/ 1.6T optical modules, reflecting higher shipment on the improving chipset supply and capacity expansion.

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

Exhibit 2: Earnings revision

<table><tr><td rowspan="2">Rmb m</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td></tr><tr><td>Revenues</td><td>48,395</td><td>51,457</td><td>6%</td><td>72,531</td><td>73,911</td><td>2%</td><td>83,196</td><td>84,975</td><td>2%</td></tr><tr><td>GP</td><td>23,233</td><td>24,807</td><td>7%</td><td>35,135</td><td>35,879</td><td>2%</td><td>40,408</td><td>41,356</td><td>2%</td></tr><tr><td>OP</td><td>21,957</td><td>23,528</td><td>7%</td><td>33,601</td><td>34,345</td><td>2%</td><td>38,537</td><td>39,483</td><td>2%</td></tr><tr><td>Net income</td><td>19,308</td><td>20,683</td><td>7%</td><td>29,429</td><td>30,080</td><td>2%</td><td>33,747</td><td>34,576</td><td>2%</td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GM</td><td>48.0%</td><td>48.2%</td><td></td><td>48.4%</td><td>48.5%</td><td></td><td>48.6%</td><td>48.7%</td><td></td></tr><tr><td>OPM</td><td>45.4%</td><td>45.7%</td><td></td><td>46.3%</td><td>46.5%</td><td></td><td>46.3%</td><td>46.5%</td><td></td></tr><tr><td>NM</td><td>39.9%</td><td>40.2%</td><td></td><td>40.6%</td><td>40.7%</td><td></td><td>40.6%</td><td>40.7%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We continue to derive our target price using a near-term P/E (2027E P/E). The target P/E multiple is derived from peers' avg. ratio of trading PE to forward year fundamentals (NI YoY and OPM). We use a 29.3x target 2027E P/E (vs. previously at 28.4x) based on the company's forward year avg. NI YoY and avg. OPM in 2027-28E. With higher earnings, our 12-month target price is revised up to Rmb633.0 (from Rmb600.71). The new target P/E at 29.3x is in line with Eoptolink's historical avg. forward P/E at 28x since Sep 2018.

Exhibit 3: Eoptolink P&L Summary

<table><tr><td>Rmb m</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="7">Income statement</td></tr><tr><td>Revenue</td><td>3,098</td><td>8,647</td><td>24,842</td><td>51,457</td><td>73,911</td><td>84,975</td></tr><tr><td>Gross profit</td><td>960</td><td>3,867</td><td>11,876</td><td>24,807</td><td>35,879</td><td>41,356</td></tr><tr><td>OP income</td><td>696</td><td>3,125</td><td>10,708</td><td>23,528</td><td>34,345</td><td>39,483</td></tr><tr><td>Pretax income</td><td>789</td><td>3,234</td><td>10,866</td><td>23,714</td><td>34,377</td><td>39,515</td></tr><tr><td>Net income</td><td>688</td><td>2,838</td><td>9,532</td><td>20,683</td><td>30,080</td><td>34,576</td></tr><tr><td>EBITDA</td><td>822</td><td>3,336</td><td>11,096</td><td>24,141</td><td>35,192</td><td>40,517</td></tr><tr><td>EPS, diluted (Rmb)</td><td>0.53</td><td>2.04</td><td>6.85</td><td>14.86</td><td>21.62</td><td>24.85</td></tr><tr><td colspan="7">Margins</td></tr><tr><td>Gross margin</td><td>31.0%</td><td>44.7%</td><td>47.8%</td><td>48.2%</td><td>48.5%</td><td>48.7%</td></tr><tr><td>Operating margin</td><td>22.5%</td><td>36.1%</td><td>43.1%</td><td>45.7%</td><td>46.5%</td><td>46.5%</td></tr><tr><td>Pretax margin</td><td>25.5%</td><td>37.4%</td><td>43.7%</td><td>46.1%</td><td>46.5%</td><td>46.5%</td></tr><tr><td>Net margin</td><td>22.2%</td><td>32.8%</td><td>38.4%</td><td>40.2%</td><td>40.7%</td><td>40.7%</td></tr><tr><td>EBITDA margin</td><td>26.5%</td><td>38.6%</td><td>44.7%</td><td>46.9%</td><td>47.6%</td><td>47.7%</td></tr><tr><td colspan="7">YoY</td></tr><tr><td>Revenue</td><td>-6%</td><td>179%</td><td>187%</td><td>107%</td><td>44%</td><td>15%</td></tr><tr><td>Gross profit</td><td>-21%</td><td>303%</td><td>207%</td><td>109%</td><td>45%</td><td>15%</td></tr><tr><td>OP income</td><td>-21%</td><td>349%</td><td>243%</td><td>120%</td><td>46%</td><td>15%</td></tr><tr><td>Pretax income</td><td>-23%</td><td>310%</td><td>236%</td><td>118%</td><td>45%</td><td>15%</td></tr><tr><td>Net income</td><td>-24%</td><td>312%</td><td>236%</td><td>117%</td><td>45%</td><td>15%</td></tr><tr><td>EBITDA</td><td>-16%</td><td>306%</td><td>233%</td><td>118%</td><td>46%</td><td>15%</td></tr><tr><td colspan="7">QoQ</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross profit</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>OP income</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pretax income</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net income</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBITDA</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td>4,052</td><td>6,385</td><td>6,068</td><td>8,337</td><td>8,338</td><td>11,283</td><td>15,164</td><td>16,671</td></tr><tr><td>1,972</td><td>2,978</td><td>2,848</td><td>4,078</td><td>4,099</td><td>5,384</td><td>7,300</td><td>8,024</td></tr><tr><td>1,753</td><td>2,641</td><td>2,575</td><td>3,740</td><td>3,835</td><td>5,105</td><td>7,001</td><td>7,587</td></tr><tr><td>1,773</td><td>2,675</td><td>2,602</td><td>3,815</td><td>3,247</td><td>5,313</td><td>7,259</td><td>7,895</td></tr><tr><td>1,573</td><td>2,370</td><td>2,385</td><td>3,205</td><td>2,774</td><td>4,649</td><td>6,352</td><td>6,908</td></tr><tr><td>1,850</td><td>2,738</td><td>2,672</td><td>3,837</td><td>3,989</td><td>5,258</td><td>7,154</td><td>7,740</td></tr><tr><td>1.13</td><td>1.71</td><td>1.71</td><td>2.30</td><td>1.99</td><td>3.34</td><td>4.56</td><td>4.96</td></tr><tr><td>48.7%</td><td>46.6%</td><td>46.9%</td><td>48.9%</td><td>49.2%</td><td>47.7%</td><td>48.1%</td><td>48.1%</td></tr><tr><td>43.3%</td><td>41.4%</td><td>42.4%</td><td>44.9%</td><td>46.0%</td><td>45.2%</td><td>46.2%</td><td>45.5%</td></tr><tr><td>43.8%</td><td>41.9%</td><td>42.9%</td><td>45.8%</td><td>38.9%</td><td>47.1%</td><td>47.9%</td><td>47.4%</td></tr><tr><td>38.8%</td><td>37.1%</td><td>39.3%</td><td>38.4%</td><td>33.3%</td><td>41.2%</td><td>41.9%</td><td>41.4%</td></tr><tr><td>43.3%</td><td>41.4%</td><td>42.4%</td><td>44.9%</td><td>46.0%</td><td>45.2%</td><td>46.2%</td><td>45.5%</td></tr><tr><td>264%</td><td>295%</td><td>153%</td><td>137%</td><td>106%</td><td>77%</td><td>150%</td><td>100%</td></tr><tr><td>322%</td><td>321%</td><td>185%</td><td>141%</td><td>108%</td><td>81%</td><td>156%</td><td>97%</td></tr><tr><td>383%</td><td>365%</td><td>197%</td><td>181%</td><td>119%</td><td>93%</td><td>172%</td><td>103%</td></tr><tr><td>376%</td><td>339%</td><td>193%</td><td>180%</td><td>83%</td><td>99%</td><td>179%</td><td>107%</td></tr><tr><td>385%</td><td>338%</td><td>205%</td><td>169%</td><td>76%</td><td>96%</td><td>166%</td><td>116%</td></tr><tr><td>383%</td><td>365%</td><td>197%</td><td>181%</td><td>119%</td><td>93%</td><td>172%</td><td>103%</td></tr><tr><td>15%</td><td>58%</td><td>-5%</td><td>37%</td><td>0%</td><td>35%</td><td>34%</td><td>10%</td></tr><tr><td>16%</td><td>51%</td><td>-4%</td><td>43%</td><td>1%</td><td>31%</td><td>36%</td><td>10%</td></tr><tr><td>32%</td><td>51%</td><td>-2%</td><td>45%</td><td>3%</td><td>33%</td><td>37%</td><td>8%</td></tr><tr><td>30%</td><td>51%</td><td>-3%</td><td>47%</td><td>-15%</td><td>64%</td><td>37%</td><td>9%</td></tr><tr><td>32%</td><td>51%</td><td>1%</td><td>34%</td><td>-13%</td><td>68%</td><td>37%</td><td>9%</td></tr><tr><td>34%</td><td>48%</td><td>-2%</td><td>44%</td><td>4%</td><td>32%</td><td>36%</td><td>8%</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We derive our target price using a near-term P/E. We use a 29.3x target 2027E P/E. Our 12-month target price is Rmb633. Our target multiple is in line with the company's average forward P/E of 29x since 2018.

Key downside risks: 1) slower-than-expected 800G ramp pace; 2) geopolitical issues that may impact the optical transceiver supply chain; 3) fiercer competition than expected, which could lead to price erosion and a margin drop.

<table><tr><td>300502.SZ</td><td colspan="2">12m Price Target: Rmb633.00</td><td colspan="2">Price: Rmb482.88</td><td colspan="2">Upside: 31.1%</td></tr><tr><td colspan="2">Buy</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td colspan="2">Market cap:</td><td>Revenue (Rmb mn) New</td><td>24,841.9</td><td>51,456.5</td><td>73,910.6</td><td>84,975.4</td></tr><tr><td colspan="2">Rmb672.0bn / $99.2bn</td><td>Revenue (Rmb mn) Old</td><td>24,841.9</td><td>48,394.7</td><td>72,531.4</td><td>83,196.2</td></tr><tr><td colspan="2">Enterprise value:</td><td>EBITDA (Rmb mn)</td><td>11,096.2</td><td>24,140.9</td><td>35,192.3</td><td>40,516.7</td></tr><tr><td colspan="2">Rmb656.7bn / $96.9bn</td><td>EPS (Rmb) New</td><td>6.85</td><td>14.86</td><td>21.62</td><td>24.85</td></tr><tr><td colspan="2">3m ADTV: Rmb26.2bn / $3.9bn</td><td>EPS (Rmb) Old</td><td>6.85</td><td>13.87</td><td>21.15</td><td>24.25</td></tr><tr><td colspan="2">China</td><td>P/E (X)</td><td>20.6</td><td>32.5</td><td>22.3</td><td>19.4</td></tr><tr><td colspan="2">Greater China Technology</td><td>P/B (X)</td><td>10.9</td><td>18.3</td><td>10.5</td><td>7.1</td></tr><tr><td colspan="2">M&amp;A Rank: 3</td><td>Dividend yield (%)</td><td>0.5</td><td>0.3</td><td>0.4</td><td>0.5</td></tr><tr><td colspan="2">Leases incl. in net debt &amp; EV?: Yes</td><td>CROCI (%)</td><td>123.4</td><td>131.4</td><td>126.3</td><td>107.1</td></tr><tr><td colspan="2"></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td colspan="2"></td><td>EPS (Rmb)</td><td>1.99</td><td>3.34</td><td>4.56</td><td>4.96</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 17 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Ting Song, Allen Chang and Verena Jeng, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Ting Song GS (Asia) L.L.C., Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or

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
