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
# China Property

## Conference Takeaways: More Sales Launches From Sep after Weak 1H26 Earnings; Positive View Despite Recent Sell-off

## CITI'S TAKE

19 property firms attended Citi Conference: Despite recent stock sell-off on 10% mom decline of weekly secondary volume & tighter stock market liquidity on period end, we are increasingly positive on property sector given resilient volume, low base from Jul-25, more new sales launches from Sep & expected supportive tone in Jul Politburo. That said, with weak 1H26 earnings expected, we re-arranged our top pick orders for Jul/Aug: CRL, C&D, Beike, Jinmao & COLI. We are more positive on C&D after its product upgrades, accelerated lands (HZ, Suzhou) & expansion in SZ in Jun.

Positive takeaways — [1] sales: 5 names posted >10% sales growth in 5M26 despite less new launches (on better existing project sales) & plans more launches from Sep; [2] land: reduced land supply in key cities (GFA -30%yoy) pushed up land prices in 5M. COLI, Jinmao, C&D slows in 5M26 but will accelerated when land market cools in 2H26 when supply picks up. CRL is consistently strong; [3] 1H26 earnings risk: COLI, Longfor, Poly, Yuexiu see a high base in 1H25 & margin pressure; CRL relatively stable given REIT spin off in 1H26. [4] 5M26 same-store sales beat: +10%/9%yoy for CRL/ Longfor despite weak national retail. [5] policy: expect supportive tone in Jul Politburo after Quishi article on 18 Jun, which calls to stabilize property market; [6] mgmt change: expect new CEO for Greentown & chairman change for COLI in 2H26.

Sales: 10%+growth on existing project sales; more launches from Sep—5 names (COLI, Jinmao, CRL, COGO, CMSK) posted >10%yoy sales growth in 5M26 on better existing project sales in core cities. We expect yoy growth to continue for 6 names (incl C&D) given more new launches from Sep & low base from Jul-25. Sector overall -15%yoy in 5M given fewer new launches. Sell-through for luxury homes slowed in weak T2 cities given more supply but some upgrade products picked up.

Land: reduced supply pushed up prices for quality plots; awaiting 2H window — 5M26 land acquisition -48%yoy for listed names given reduced land supply In key cities (300 cities: -32%by GFA, a 20 year low). COLI, Jinmao, C&D, Greentown are to acquire in 2H when supply picks up on better land prices, given a strong 2025. Yuexiu, Poly China are active in 1H26. CRL is strong in SZ. C&D picked up in June (SZ, HZ, etc.).

1H26 earnings risk — We expect down 35-40%yoy on high base in 1H25 (COLI: 68% of FY25 profits in 1H25, Jinmao: 77%, Yuexiu, Seazen, Poly). With margin pressure from inventory sales, we expect loss for Longfor & Poly Property. CRL's recurring income +8%yoy in 5M with est. Rmb2bn+ REIT disposal gains from Chengdu mall & we est. 1H earnings down 10%. Beike 2Q GTV beat & we estimate earnings +26%yoy.

Recurring income: 10% SSSG in 5M; REITs — CRL +10%/ Longfor +9%yoy tenant remix & AEIs. CRL's REIT spin-off on Chengdu mall added est.Rmb2bn+ gains in 1H.

Tour takeaways: Changsha weak but not deteriorating; SZ is good — [1] Changsha: new land supply reduced to 1mn in 5M26 (vs 5.4msm GFA sold in 2025), a 20-year low. Secondary prices were stable at c.Rmb8k in Jan-Jun, not dropping more. With 22 months of inventory (& 7 years incl. lands) we expect home price to stay at bottom for a prolonged 3+ years with stable volume. [2] Shenzhen: 100k units at secondary for sales but 50% are listed for more than a year (not a real seller). Sell-through for luxury home slows a bit but still strong, as some buyers flow into HK from Shenzhen.

Griffin Chan AC

+852-2501-2438

griffin.chan@citi.com

## Cindy Li

+852-2501-2710

cindy.li@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations.

Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

## Other takeaways:

Physical market outlook by Mr. Ding Zuyu, Chairman of SH Proptech Innovations — Mr. Ding noted that physical market has yoy improved in 2026, but unlikely for a rapid turnaround. He believes the market bottom to be anchored by price stabilization in older/smaller secondary units, with the bottoming cycle likely extending through 2026–2030E and led by core cities (SH/ CJ/ SZ/ GZ/ HZ/ CD, etc). He views the recent “little spring” rally peaked in late May, as project visits and subscriptions moderated into June, likely due to (i) equity market weakness and (ii) demand pull-forward in Mar–May. He observed a “K-shaped” divergence, with high-end luxury and low-end older/smaller units outperforming mid-tier projects. New home sales growth is limited by reduced land supply so national is on decline. Secondary market is stable. After the emerging of “new standard” homes that having higher GFA efficiency, the pre-2H24 “old standard” projects are now the weakest segment to destock. Mr. Ding does not expect any nationwide policy stimulus in 2026 but sees big development on REIT market and urban renewals in 2026.

Figure 1. 5M26 Contracted Sales (YoY change) – Five Names Posted more than 10%yoy growth  
![](images/102dd5ac2a0122ff75e797b78c08683ea7eefd7ccba87c2d2717e83a1b134ed0.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Companies, CRIC, Citi estimates

Figure 2. May 2026: more names reported positive contracted sales growth in May-26  
![](images/237b8acbe5547b4b4433287f46d3ef3f181738353a4e7095088d3f651fd8c428.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Companies, CRIC, Citi estimates

Figure 3. Attributable land acquisition -48%yoy in 5M26 given reduced land supply in key cities

<table><tr><td colspan="2">(Rmb bn)</td><td colspan="2">Land Acq (attri. value)</td><td colspan="2">5M26 vs. 5M25</td></tr><tr><td>Company</td><td>RIC</td><td>5M25</td><td>5M26</td><td>YoY (value)</td><td>YoY (%)</td></tr><tr><td colspan="6">12 Names with Land Acq in 5M26</td></tr><tr><td>Yuexiu</td><td>0123.HK</td><td>13.7</td><td>27.1</td><td>13.4</td><td>98%</td></tr><tr><td>Longfor</td><td>0960.HK</td><td>1.8</td><td>1.2</td><td>-0.5</td><td>-30%</td></tr><tr><td>CR Land</td><td>1109.HK</td><td>31.2</td><td>29.7</td><td>-1.5</td><td>-5%</td></tr><tr><td>COGO</td><td>0081.HK</td><td>4.6</td><td>0.3</td><td>-4.3</td><td>-94%</td></tr><tr><td>Poly Prop</td><td>0119.HK</td><td>11.8</td><td>4.5</td><td>-7.4</td><td>-62%</td></tr><tr><td>Jinmao</td><td>0817.HK</td><td>21.5</td><td>9.6</td><td>-11.9</td><td>-55%</td></tr><tr><td>Poly Dev</td><td>600048.SS</td><td>36.1</td><td>23.9</td><td>-12.2</td><td>-34%</td></tr><tr><td>CMSK</td><td>001979.SZ</td><td>20.7</td><td>8.4</td><td>-12.3</td><td>-59%</td></tr><tr><td>Binjiang</td><td>002244.SZ</td><td>26.4</td><td>8.1</td><td>-18.3</td><td>-69%</td></tr><tr><td>C&amp;D Int&#x27;l</td><td>1908.HK</td><td>26.6</td><td>5.2</td><td>-21.4</td><td>-80%</td></tr><tr><td>COLI</td><td>0688.HK</td><td>29.1</td><td>7.7</td><td>-21.4</td><td>-74%</td></tr><tr><td>Greentown</td><td>3900.HK</td><td>33.7</td><td>8.8</td><td>-24.9</td><td>-74%</td></tr><tr><td colspan="2">Total</td><td>257</td><td>134</td><td>(123)</td><td>-48%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: CREIS, Company Reports, Citi Estimates

Figure 4. China Property – Listed Property Names' Contracted Sales in May 2026

<table><tr><td rowspan="2">Company</td><td rowspan="2" colspan="2">RIC</td><td rowspan="2">May-25</td><td colspan="3">2026</td><td colspan="2">May-26</td><td colspan="2">YTD Sales</td><td colspan="2">2026E Citi Est</td><td rowspan="2">2025 Actual</td><td rowspan="2">2025 YoY</td><td rowspan="2">2026E Citi Est.</td><td rowspan="2">2026E YoY</td></tr><tr><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>MoM %</td><td>YoY %</td><td>5M26 YTD</td><td>YoY (%)</td><td>FY26E Est.</td><td>% of FY26 est.</td></tr><tr><td>Binjiang</td><td>002244.SZ</td><td>RMB</td><td>10.1</td><td>5.9</td><td>9.3</td><td>9.3</td><td>0%</td><td>-8%</td><td>33.6</td><td>-23%</td><td>90</td><td>37%</td><td>101.8</td><td>-9%</td><td>90.0</td><td>-12%</td></tr><tr><td>C&amp;D Int&#x27;l (attr)</td><td>1908.HK</td><td>RMB</td><td>9.5</td><td>8.6</td><td>9.7</td><td>10.8</td><td>11%</td><td>13%</td><td>39.8</td><td>-5%</td><td>82</td><td>48%</td><td>90.9</td><td>-12%</td><td>90.9</td><td>0%</td></tr><tr><td>CIFI</td><td>0884.HK</td><td>RMB</td><td>1.7</td><td>1.2</td><td>0.7</td><td>0.8</td><td>24%</td><td>-51%</td><td>3.9</td><td>-56%</td><td>12</td><td>33%</td><td>16.1</td><td>-52%</td><td>12.0</td><td>-25%</td></tr><tr><td>CMSK</td><td>001979.SZ</td><td>RMB</td><td>17.3</td><td>17.9</td><td>21.7</td><td>20.8</td><td>-4%</td><td>20%</td><td>75.9</td><td>13%</td><td>185</td><td>41%</td><td>196.0</td><td>-11%</td><td>185.0</td><td>-6%</td></tr><tr><td>COGO</td><td>0081.HK</td><td>RMB</td><td>3.0</td><td>3.4</td><td>3.3</td><td>3.6</td><td>8%</td><td>20%</td><td>15.0</td><td>20%</td><td>33</td><td>46%</td><td>32.2</td><td>-20%</td><td>33.0</td><td>3%</td></tr><tr><td>COLI (incl. COGO)</td><td>0688.HK</td><td>RMB</td><td>23.9</td><td>28.6</td><td>24.2</td><td>27.3</td><td>13%</td><td>14%</td><td>103.0</td><td>14%</td><td>250</td><td>41%</td><td>251.2</td><td>-19%</td><td>252.0</td><td>0%</td></tr><tr><td>Country Gdn (attr.)</td><td>2007.HK</td><td>RMB</td><td>3.1</td><td>2.2</td><td>2.5</td><td>2.6</td><td>5%</td><td>-15%</td><td>11.8</td><td>-15%</td><td>25</td><td>47%</td><td>33.0</td><td>-30%</td><td>25.0</td><td>-24%</td></tr><tr><td>CRL (gross)</td><td>1109.HK</td><td>RMB</td><td>18.4</td><td>22.4</td><td>25.9</td><td>25.3</td><td>-2%</td><td>38%</td><td>95.3</td><td>10%</td><td>220</td><td>43%</td><td>233.6</td><td>-11%</td><td>220.0</td><td>-6%</td></tr><tr><td>Gemdale</td><td>600383.SS</td><td>RMB</td><td>3.1</td><td>1.5</td><td>2.5</td><td>2.0</td><td>-21%</td><td>-36%</td><td>7.8</td><td>-44%</td><td>25</td><td>31%</td><td>30.0</td><td>-56%</td><td>25.0</td><td>-17%</td></tr><tr><td>Greentown</td><td>3900.HK</td><td>RMB</td><td>18.6</td><td>15.1</td><td>9.6</td><td>12.9</td><td>34%</td><td>-31%</td><td>48.5</td><td>-27%</td><td>155</td><td>31%</td><td>153.4</td><td>-11%</td><td>130.0</td><td>-15%</td></tr><tr><td>Jinmao</td><td>0817.HK</td><td>RMB</td><td>12.4</td><td>9.5</td><td>8.8</td><td>10.5</td><td>19%</td><td>-16%</td><td>41.7</td><td>11%</td><td>120</td><td>35%</td><td>113.5</td><td>16%</td><td>120.0</td><td>6%</td></tr><tr><td>Longfor (gross)</td><td>0960.HK</td><td>RMB</td><td>6.5</td><td>3.0</td><td>2.9</td><td>3.4</td><td>17%</td><td>-48%</td><td>13.7</td><td>-52%</td><td>48</td><td>29%</td><td>63.2</td><td>-38%</td><td>48.0</td><td>-24%</td></tr><tr><td>Poly China</td><td>600048.SS</td><td>RMB</td><td>28.5</td><td>26.0</td><td>25.9</td><td>27.6</td><td>7%</td><td>-3%</td><td>105.3</td><td>-9%</td><td>230</td><td>46%</td><td>253.0</td><td>-22%</td><td>230.0</td><td>-9%</td></tr><tr><td>Poly Property</td><td>0119.HK</td><td>RMB</td><td>3.9</td><td>5.2</td><td>4.2</td><td>4.5</td><td>7%</td><td>15%</td><td>19.8</td><td>-9%</td><td>51</td><td>39%</td><td>50.2</td><td>-7%</td><td>51.0</td><td>2%</td></tr><tr><td>Seazen</td><td>1030.HK</td><td>RMB</td><td>2.0</td><td>1.8</td><td>1.0</td><td>1.0</td><td>-2%</td><td>-49%</td><td>5.0</td><td>-43%</td><td>16</td><td>32%</td><td>19.3</td><td>-52%</td><td>16.0</td><td>-17%</td></tr><tr><td>Sunac</td><td>1918.HK</td><td>RMB</td><td>4.8</td><td>2.2</td><td>1.2</td><td>1.1</td><td>-8%</td><td>-77%</td><td>8.1</td><td>-50%</td><td>28</td><td>29%</td><td>36.8</td><td>-22%</td><td>28.0</td><td>-24%</td></tr><tr><td>SZI</td><td>0604.HK</td><td>RMB</td><td>1.2</td><td>1.0</td><td>0.5</td><td>1.4</td><td>187%</td><td>14%</td><td>4.9</td><td>-12%</td><td>13</td><td>38%</td><td>13.3</td><td>-22%</td><td>13.0</td><td>-2%</td></tr><tr><td>Vanke</td><td>000002.SZ</td><td>RMB</td><td>11.1</td><td>7.5</td><td>4.8</td><td>6.2</td><td>29%</td><td>-44%</td><td>27.7</td><td>-52%</td><td>100</td><td>28%</td><td>133.9</td><td>-46%</td><td>100.0</td><td>-25%</td></tr><tr><td>Yuexiu</td><td>0123.HK</td><td>RMB</td><td>9.6</td><td>10.1</td><td>8.5</td><td>11.3</td><td>33%</td><td>18%</td><td>37.0</td><td>-27%</td><td>92</td><td>40%</td><td>106.2</td><td>-7%</td><td>92.0</td><td>-13%</td></tr><tr><td>Weighted Avg</td><td></td><td></td><td></td><td></td><td></td><td></td><td>10%</td><td>-6%</td><td></td><td>-15%</td><td></td><td>39%</td><td></td><td>-21%</td><td></td><td>-15%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: CREIS, Company Reports, Citi Estimates

Figure 5. China Property Sector — Quant Screen on Investor Position (1-month change by 19-Jun-2026)  
![](images/4fa9c9e6683ba7dacedee215a4b450d842b7740fb8f57742b32d9f1ac7754dac.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: CREIS, Company Reports, Citi Estimates

© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 6. China Property Sector — Valuations (26 Jun 2026 close) Citi Rating: 1 – Buy; 2 – Neutral; 3 – Sell; H – High Risk

<table><tr><td rowspan="2">Stock</td><td rowspan="2">RIC</td><td rowspan="2">26-Jun-26 Price</td><td rowspan="2">Mkt Cap (USDm)</td><td rowspan="2">Citi Rating</td><td rowspan="2">Est. NAV</td><td rowspan="2">NAV Disc</td><td rowspan="2">Target Price</td><td colspan="3">P/E</td><td colspan="3">P/B</td><td colspan="3">Yield</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="8">China Property Names (H-share)</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>C&amp;D int&#x27;l</td><td>1908.HK</td><td>12.85</td><td>3,671</td><td>1</td><td>24.72</td><td>-48%</td><td>18.80</td><td>6.8</td><td>6.7</td><td>6.4</td><td>0.5</td><td>0.5</td><td>0.5</td><td>7.7%</td><td>7.8%</td><td>8.2%</td></tr><tr><td>CIFI</td><td>0884.HK</td><td>0.04</td><td>92</td><td>3H</td><td>0.31</td><td>-87%</td><td>0.06</td><td>N/A</td><td>N/A</td><td>N/A</td><td>0.0</td><td>0.0</td><td>0.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>COGO</td><td>0081.HK</td><td>2.16</td><td>981</td><td>1</td><td>6.93</td><td>-69%</td><td>2.68</td><td>7.6</td><td>7.3</td><td>6.7</td><td>0.2</td><td>0.2</td><td>0.2</td><td>4.5%</td><td>4.7%</td><td>5.1%</td></tr><tr><td>COLI</td><td>0688.HK</td><td>12.17</td><td>16,988</td><td>1</td><td>34.32</td><td>-65%</td><td>18.20</td><td>9.0</td><td>9.1</td><td>8.8</td><td>0.3</td><td>0.3</td><td>0.3</td><td>3.9%</td><td>3.8%</td><td>3.9%</td></tr><tr><td>Country Garden</td><td>2007.HK</td><td>0.17</td><td>1,005</td><td>3H</td><td>0.83</td><td>-80%</td><td>0.25</td><td>N/A</td><td>N/A</td><td>N/A</td><td>-0.3</td><td>-0.2</td><td>-0.1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>CR Land</td><td>1109.HK</td><td>30.16</td><td>27,430</td><td>1</td><td>71.70</td><td>-58%</td><td>43.00</td><td>8.2</td><td>8.0</td><td>7.7</td><td>0.6</td><td>0.6</td><td>0.6</td><td>4.5%</td><td>4.6%</td><td>4.8%</td></tr><tr><td>Greentown</td><td>3900.HK</td><td>6.41</td><td>2,076</td><td>1</td><td>18.60</td><td>-66%</td><td>11.80</td><td>4.6</td><td>4.3</td><td>4.3</td><td>0.4</td><td>0.3</td><td>0.3</td><td>8.1%</td><td>8.6%</td><td>8.7%</td></tr><tr><td>Jinmao Group</td><td>0817.HK</td><td>1.25</td><td>2,154</td><td>1</td><td>3.80</td><td>-67%</td><td>1.90</td><td>10.2</td><td>9.5</td><td>8.5</td><td>0.2</td><td>0.2</td><td>0.2</td><td>2.5%</td><td>2.5%</td><td>3.0%</td></tr><tr><td>Longfor</td><td>0960.HK</td><td>6.03</td><td>5,458</td><td>1</td><td>22.25</td><td>-73%</td><td>11.10</td><td>NM</td><td>7.8</td><td>7.0</td><td>0.2</td><td>0.2</td><td>0.2</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Midea Real Esta

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing

such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
