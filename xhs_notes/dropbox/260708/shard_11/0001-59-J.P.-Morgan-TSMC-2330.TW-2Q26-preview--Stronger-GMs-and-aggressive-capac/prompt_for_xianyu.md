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
# JPM

## TSMC

## 2Q26 preview: Stronger GMs and aggressive capacity plans to match rising AI demand; Raise PT to NT\$3100

Ahead of TSMC's 2Q26 earnings conference, we are raising our FY26/27/28E EPS estimates by $5\% / 10\% / 16\%$ and raising our Jun-27 PT to NT\$3100 (20x 12m forward earnings), to reflect stronger near-term profitability, better visibility on AI demand, stronger capacity build and firmer pricing into 2028. TSMC's stock has lagged the TWSE index by $8\%$ in the last three months due to (1) increased concerns on market share losses in leading edge, (2) concerns on TSMC being too conservative on capacity expansion, and (3) more attractive price increase narratives in higher beta parts of the supply chain such as tier-2 foundries, wafers, MLCC etc. On the upcoming earnings conference call, we expect TSMC to push back strongly against market share loss and show clear intent to expand capacity meaningfully in 2027-29. In addition, near-term GMs are also likely to remain strong, nudging $70\%$ levels. We also expect broader price hikes in 2027, given the widening supply-demand gap, and a stronger Datacenter AI CAGR (we now estimate $69\%$ CAGR from 2024-29E, including higher accelerator estimates and sharply increased AI CPU numbers). The stock is likely to continue to move up, along with EPS upgrades, but do not expect it to significantly outperform the broader Asian semis at this point in the semi cycle.

\- Strong near-term Gross Margins; N3 improvement, high UTR and pricing should offset N2 and overseas dilution: We expect TSMC's 2Q26 GMs to reach close to $70\%$ levels (JPMe $69.5\%$ ), due to better utilization, increased ASPs from expedited wafers and better overall efficiency. We now expect GMs to remain in the high $60\%$ range in 2H26 and 1H27 despite increased dilution from N2 ramp and overseas Fab ramp, since N3 is likely to cross over to corporate average GMs in 2H26, and better pricing in 2027 should keep margins high for newly ramped capacity in Fab 18P9 and AZ. Overall, we expect TSMC to be able to keep GMs around high 60s-to $70\%$ levels for the next few quarters.

\- Raise Datacenter AI CAGR to 69% growth, including sharp CPU ramp and stronger accelerator build: We update our Datacenter AI revenue forecast to reflect stronger accelerator build and much faster demand growth for AI CPUs, and now expect a CAGR of 69% from 2024-29E (prior 59%, TSMC guidance of mid-to-high-50%). AI accelerators will remain the primary growth driver for TSMC's datacenter AI demand, driven by larger die sizes, adoption of multi-die chiplets and faster growth in ASICs. But CPUs are likely to grow the fastest from 2026 onwards, accounting for \~14% of the datacenter AI revenues by 2029. We believe that TSMC is likely to indicate upside for its own DC AI forecasts, given the upside from CPUs, networking and ASIC demand since Jan-26.

\- Capacity plans becoming more aggressive, raise FY26/27/28 capex to \$58/\$78/\$84 bn: Our checks indicate that TSMC is turning more aggressive on capacity buildout since the start of 2026, and is continuing to accelerate N2 and N3 buildout plans, with multiple new Fab shells construction kicking off in 1H26 and increased equipment orders from 2Q26 onwards. Hence, we are raising our capex estimates and now expect \$58/\$78/\$84 bn in capex for 2026/27/28 respectively. For 2026, we expect TSMC to raise its capex range

## Overweight

2330.TW, 2330 TT
Price (06 Jul 26):NT\$2460.0

▲ Price Target (Jun-27):NT\$3100.0
Prior (Dec-26):NT\$2500.0

## Technology and Telecoms

Gokul Hariharan AC
(852) 2800-8564
gokul.hariharan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Jennifer Hsieh

(886-2) 2725-9868
jennifer.hsieh@JPM.com
JPM Securities (Taiwan) Limited

## David Chou

(886-2) 2725-9618
david.chou@JPM.com
JPM Securities (Taiwan) Limited

Jason Chen
(886-2) 2725-9864
jason.bh.chen@JPM.com
JPM Securities (Taiwan) Limited

## Subham Singhania

(91-22) 6157-3801
subham.singhania@JPM.com
JPM India Private Limited

## Key Changes (FYE Dec)

<table><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 26E (NT$)</td><td>99.31</td><td>103.97</td><td>4.7%</td></tr><tr><td>Adj. EPS - 27E (NT$)</td><td>125.11</td><td>138.24</td><td>10.5%</td></tr></table>

## Quarterly Forecasts (FYE Dec)

<table><tr><td colspan="4">Adj. EPS (NT$)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>13.94</td><td>22.08A</td><td>31.09</td></tr><tr><td>Q2</td><td>15.36</td><td>24.72</td><td>32.67</td></tr><tr><td>Q3</td><td>17.44</td><td>27.39</td><td>36.83</td></tr><tr><td>Q4</td><td>19.50</td><td>29.79</td><td>37.66</td></tr><tr><td>FY</td><td>66.24</td><td>103.97</td><td>138.24</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>43</td><td>47</td><td>33</td><td>44</td><td>78</td></tr><tr><td>Growth</td><td>29</td><td>18</td><td>11</td><td>23</td><td>24</td></tr><tr><td>Momentum</td><td>32</td><td>17</td><td>29</td><td>68</td><td>42</td></tr><tr><td>Quality</td><td>14</td><td>14</td><td>10</td><td>13</td><td>7</td></tr><tr><td>Low Vol</td><td>29</td><td>32</td><td>37</td><td>44</td><td>29</td></tr><tr><td>ESGQ</td><td>27</td><td>84</td><td>27</td><td>16</td><td>3</td></tr></table>

Price Performance  
![](images/a4b118e7af1632893a81c0fd415a49f846d077b4bb97624d6b329b347d9358ed.jpg)

— 2330.TW Price (NT\$) — TSE (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>58.7%</td><td>4.0%</td><td>35.9%</td><td>126.7%</td></tr><tr><td>Rel</td><td>-2.0%</td><td>0.7%</td><td>-7.0%</td><td>19.2%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>25,930</td></tr><tr><td>52-week range (NT$)</td><td>2535.0-1065.0</td></tr><tr><td>Market cap ($ mn)</td><td>1,996,767</td></tr><tr><td>Exchange rate</td><td>31.95</td></tr><tr><td>Free float (%)</td><td>92.1%</td></tr><tr><td>3M ADV (mn)</td><td>42.31</td></tr><tr><td>3M ADV ($ mn)</td><td>2,994.6</td></tr><tr><td>Volatility (90 Day)</td><td>36</td></tr><tr><td>Index</td><td>TAIEX</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>39|1|0</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>NT$ in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>3,809,054</td><td>5,342,260</td><td>7,192,208</td><td>8,813,415</td></tr><tr><td>Adj. EBIT</td><td>1,936,092</td><td>3,175,201</td><td>4,275,861</td><td>5,262,336</td></tr><tr><td>Adj. EBITDA</td><td>2,624,188</td><td>3,968,123</td><td>5,280,152</td><td>6,544,105</td></tr><tr><td>Adj. net income</td><td>1,717,883</td><td>2,696,350</td><td>3,584,875</td><td>4,411,972</td></tr><tr><td>Adj. EPS</td><td>66.24</td><td>103.97</td><td>138.24</td><td>170.13</td></tr><tr><td>BBG EPS</td><td>64.73</td><td>99.38</td><td>127.22</td><td>157.50</td></tr><tr><td>Cashflow from operations</td><td>2,437,716</td><td>3,413,412</td><td>4,421,425</td><td>5,578,226</td></tr><tr><td>FCFF</td><td>1,292,759</td><td>1,860,700</td><td>1,949,175</td><td>3,105,976</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>31.6%</td><td>40.3%</td><td>34.6%</td><td>22.5%</td></tr><tr><td>EBIT margin</td><td>50.8%</td><td>59.4%</td><td>59.5%</td><td>59.7%</td></tr><tr><td>EBIT Growth Y/Y (%)</td><td>46.4%</td><td>64.0%</td><td>34.7%</td><td>23.1%</td></tr><tr><td>EBITDA margin</td><td>68.9%</td><td>74.3%</td><td>73.4%</td><td>74.3%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>32.2%</td><td>51.2%</td><td>33.1%</td><td>23.9%</td></tr><tr><td>Net margin</td><td>45.1%</td><td>50.5%</td><td>49.8%</td><td>50.1%</td></tr><tr><td>Adj. EPS growth</td><td>46.4%</td><td>57.0%</td><td>33.0%</td><td>23.1%</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>16.0%</td><td>17.7%</td><td>17.7%</td><td>17.7%</td></tr><tr><td>Interest cover</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROE</td><td>35.4%</td><td>41.4%</td><td>40.1%</td><td>36.9%</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>2.0%</td><td>2.9%</td><td>3.1%</td><td>4.9%</td></tr><tr><td>Dividend yield</td><td>0.9%</td><td>1.2%</td><td>1.4%</td><td>1.7%</td></tr><tr><td>EV/Revenue</td><td>16.2</td><td>11.3</td><td>8.3</td><td>6.5</td></tr><tr><td>EV/EBITDA</td><td>23.5</td><td>15.2</td><td>11.3</td><td>8.8</td></tr><tr><td>Adj. P/E</td><td>37.1</td><td>23.7</td><td>17.8</td><td>14.5</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

We expect TSMC's structural growth drivers to remain very strong as leading-edge supply (N4, N3, and N2) stays tight well into 2027 or early 2028, given accelerating AI demand, continued growth in N3, N2 and advanced back-end revenues, and long lead time for capacity build despite accelerated capex. Near-term, we believe GM is also likely to remain strong, nudging $70\%$ levels, given N3 improvement, high UTR and decent pricing, despite N2 and overseas dilution. We expect broader price hikes in 2027, given the widening supply-demand gap and a stronger Datacenter AI CAGR (we now estimate $69\%$ CAGR from 2024-29E, driven by both higher accelerator estimates and a surge in AI CPU numbers).

## Valuation

Our Jun-27 PT of NT\$3,100 is based on \~20x 12-month forward P/E and reflects stronger near-term profitability, better visibility on AI demand, stronger capacity build and firmer pricing into 2028. Our target multiple is higher than TSMC's five-year average historical multiple.

![](images/c50e191cf8f80c014b8e9f78fdf3c7dbfe964edc2732ed5dae4d6a10df298ce5.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>0.88</td><td>0.83</td></tr><tr><td>Region: Taiwan</td><td>0.83</td><td>0.89</td></tr><tr><td colspan="3">Macro:</td></tr><tr><td>JPM EM Currency(EMCI) Fixing</td><td>-0.24</td><td>-0.22</td></tr><tr><td>JPM GBI-EM Global Div</td><td>-0.17</td><td>-0.17</td></tr><tr><td>Emerging Central Bank Rate</td><td>-0.07</td><td>-0.16</td></tr><tr><td colspan="3">Quant Styles:</td></tr><tr><td>Momentum</td><td>0.18</td><td>0.20</td></tr><tr><td>Quality</td><td>0.14</td><td>0.15</td></tr><tr><td>DivYld</td><td>-0.18</td><td>-0.10</td></tr></table>

modestly, but the company is unlikely to give a 3-year guidance for capex (JPMe \~\$219bn cumulative capex from 2026-28).

\- N3 capacity addition on track with increased cross-fab in 2026, two new Fabs in 2027: We now expect TSMC's N3 capacity to reach 167/213/240k wfpm by end 26/27/28, representing a stronger ramp in response to unprecedented leading edge demand. We estimate that the supply-demand gap for N3 is \~600k wafers, and the recent upside in AI CPU demand is unlikely to ebb before late 2027. TSMC appears to have increased its cross-fab collaboration, leveraging N7, N12 and even 28nm Fab capacity to fulfill back-end metal layer wafer processing demand for N3 and N5 process nodes. We now expect Fab18 P9 (25-30k wfpm of new N3 capacity) to ramp in 1Q27, with \~20k wfpm of Arizona P2 coming online in late 2027, along with 20-30k wfpm of additional N3 capacity from Japan P2 in mid 2028.

\- N2 ramp looks very strong, with further upside from Fab 22 P7-9 buildout: TSMC appears to be ramping up N2 build out very aggressively, and is incentivizing HPC customers to migrate to N2 within a shorter lead-time, given improved yields and better performance. TSMC has up to 9 Fab phases ramping up N2/ A16 in the next 3 years (1-2 phases in Fab 20 in Baoshan, 5 phases in Fab 22 in Kaohsiung, 1 phase in AZ F3, and recently added Fab 22 P7 -out of P7-P9, in Tainan). We believe that N2 will reach 170k wfpm capacity by end 2028, a much faster ramp than any prior process node, with eventual capacity reaching 240-250k wfpm by 2029-30.

\- Faster advanced package ramp to respond to CoWoS and SoIC demand: Given the recent upside in accelerator demand and the very fast ramp in CPU orders (especially for Vera and Venice, which require CoWoS), we expect TSMC to accelerate its advanced packaging capacity ramp further in 2027, with CoWoS capacity likely to approach 2M wafers per year (up \~80-90% YoY). We believe that TSMC's AP7 Phase 2 is likely now to be a hybrid of CoWoS and SoIC capacity (prior 100% SoIC capacity), with interposer outsourcing to foundries like VSMC securing even more capacity in 2027-28.

\- No mid-year price hike in 2H26, but bigger and broader price increases in 2027: Contrary to certain press articles, we do not see TSMC raising baseline pricing for leading edge nodes in 2H26, although blended ASP will keep rising for N3 due to increasing HPC mix. For 2027, however, we are expecting \~8-10% price increases for N3 and N2, while other nodes (N5, N7) and CoWoS could also see mild price increases. Even mature nodes are likely to see flattish pricing, since slack capacity has been increasingly taken up by cross-fab collaboration to accommodate leading edge demand. As a result, we expect TSMC's blended ASPs to grow \~26% YoY in 2027, helping to drive another year of 30+% YoY revenue growth.

\- Market share and competitive status remains intact; expect management to be forceful: As we indicated in our prior note (see link), we expect increased noise around leading edge competition during a period of severe shortage of wafers from TSMC. However, TSMC's technology leadership (TSMC N2P should be in production well ahead of Intel 14A) should remain quite strong, and the company is building additional moats such as COUPE for CPO, and SoIC for 3D packaging, similar to CoWoS for 2.5D packaging. The acceleration in N2 capacity ramp should also address the supply challenges that customers may be facing in the 2028-29 timeframe, which is the earliest when much of the competition (Intel, Samsung Foundry, TeraFab etc.) would have real capacity. We expect TSMC to retain $95 + \%$ of market share for the first two waves of N2 products, similar to N3 and N5 process nodes, and continue to gain overall Foundry share.

\- Key messages to look out for from the conference call: Key messages from TSMC's management are likely to be (1) Strong message on near-term GM strength, with 2Q GM to reach 69.5% and 3Q GMs guided to 67-68% range; (2) Confident qualitative commentary on demand and capacity buildout, with 2026 revenue guidance moving to mid-late 30% in USD terms, and 3Q26 growing \~10% QoQ; (3) Aggressive pushback on competitive concerns, both in leading edge and mature process tech; (4) Modest uptick to 2026 capex (we expect \$58bn), while indicating a meaningful jump in 2027-28; and (5) high likelihood for some updates on Datacenter AI TAM, given the stronger demand upside for accelerators and emergence of AI CPUs as a new growth category.

Figure 1: Expected TSMC guidance and JPMe key assumptions

<table><tr><td></td><td>TSMC (likely) guidance</td><td>JPMe</td></tr><tr><td>2Q26E revenue growth (USD)</td><td>9% - 12%</td><td>12%</td></tr><tr><td>3Q26E revenue growth (USD)</td><td>8% - 10%</td><td>9%</td></tr><tr><td>2Q26E GM</td><td>65.5% - 67.5%</td><td>69.5%</td></tr><tr><td>3Q26E GM</td><td>67% - 68%</td><td>67.6%</td></tr><tr><td>2026-28 cumulative capex (USD)</td><td>NA</td><td>~$219bn</td></tr><tr><td>2026E CoWoS capacity growth</td><td>NA</td><td>93%</td></tr><tr><td>2024-2029 DC AI revenue CAGR</td><td>mid 60%</td><td>69%</td></tr></table>

Source: JPM estimates, Company data.

## Strong near-term Gross Margin

[中间内容因长度限制已省略]

ent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Completed 07 Jul 2026 02:26 AM HKT
"""
