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
IT Hardware and Communications Equipment

# Implied AI Multiples – Optical Taking A Break

We are back to looking biweekly at how our AI-bucketed stocks have trended. Material movement was focused around optical names with most others not seeing much movement since the last reading. We also took a look at 'non-AI' plays in our coverage.

Roughly two weeks ago (Implied AI Multiples - Rising Tides Lift Some, 06.01.26) we updated our biweekly AI exposure math that we debuted four months ago (AI Update, 02.11.26). We also now track how implied AI multiples have trended across our AI bucketed stocks since we started this series. Recall, we started this analysis to assess what was embedded for our AI-related stocks across different sub-segments and exposure percentages.

Since the last report, on average, our AI-bucketed stocks' share prices have trended down MSD (vs SPX -2% and NDX -2% from 5.29.26-6.17.26), with SMCI's (-40%), FN's (-11%), and CIEN's (-25%) share price movement driving down the average. HPE continues to see upward share price movement (+12% in the same time period), whereas most of the other stocks were up/down LSD%. AI multiples across the group moved down on average since the last reading, driven by SMCI, FN, CIEN, and GLW – with CIEN earnings also moving FN in sentiment. These AI-bucketed stocks' share prices are still up on average almost 80% YTD, despite the recent pullback.

As a reminder, the select companies under our coverage that are commonly bucketed as 'AI plays' represent \~20% of total Cloud/AI capex, per our estimates, and these companies are experiencing meaningful revenue growth in their respective Cloud/AI businesses. In our original report, most of these stocks implied AI multiples of 20-40x, with some much higher (GLW, KEYS, CIEN) and a few much lower (SMCI, HPE). In this latest update, most are now in the 40-60x range, with GLW, KEYS, CIEN still higher, and DELL, HPE, and CSCO significantly higher vs earlier readings and SMCI still much lower (due to company-specific issues).

Below is our latest breakdown of these AI-bucketed stocks' percent of revenue from Cloud/AI as well as as a percentage of total AI spend, and their estimated cloud AI revenue growth from CY25-27.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

IT Hardware and Communications Equipment
NEUTRAL

IT Hardware and Communications Equipment

Tim Long
+1 212 526 4043
tim.long@BARC.com
BCI, US

Alyssa Shreves
+1 212 526 7570
alyssa.shreves@BARC.com
BCI, US

Mary Lenox
+1 212 526 6277
mary.lenox@BARC.com
BCI, US

Clarisse Yu
+1 212 526 7025
clarisse.yu@BARC.com
BCI, US

FIGURE 1. Cloud AI revenue growth

<table><tr><td rowspan="2">Share Price</td><td rowspan="2">Company</td><td rowspan="2">Rating</td><td>CY26E</td><td>CY26E</td><td colspan="3">Cloud AI rev</td></tr><tr><td>% from Cloud/AI</td><td>% of total AI spend</td><td>CY25 growth</td><td>CY26 growth (E)</td><td>CY27 growth (E)</td></tr><tr><td>$27.78</td><td>SMCI</td><td>EW</td><td>86.9%</td><td>4.1%</td><td>57.7%</td><td>69.8%</td><td>20.8%</td></tr><tr><td>$584.38</td><td>FN</td><td>OW</td><td>82.5%</td><td>0.4%</td><td>23.0%</td><td>40.6%</td><td>18.6%</td></tr><tr><td>$380.37</td><td>CLS</td><td>OW</td><td>82.3%</td><td>1.6%</td><td>65.1%</td><td>51.1%</td><td>46.5%</td></tr><tr><td>$164.93</td><td>ANET</td><td>OW</td><td>72.0%</td><td>0.9%</td><td>34.5%</td><td>35.5%</td><td>25.9%</td></tr><tr><td>$436.72</td><td>CIEN</td><td>OW</td><td>56.2%</td><td>0.4%</td><td>71.6%</td><td>55.4%</td><td>39.4%</td></tr><tr><td>$374.98</td><td>JBL</td><td>OW</td><td>40.0%</td><td>1.5%</td><td>65.1%</td><td>51.1%</td><td>46.5%</td></tr><tr><td>$143.13</td><td>FLEX</td><td>OW</td><td>29.9%</td><td>1.0%</td><td>42.0%</td><td>52.3%</td><td>94.9%</td></tr><tr><td>$419.32</td><td>DELL</td><td>OW</td><td>35.8%</td><td>6.3%</td><td>164.1%</td><td>144.1%</td><td>33.0%</td></tr><tr><td>$350.70</td><td>KEYS</td><td>OW</td><td>19.2%</td><td>0.1%</td><td>86.4%</td><td>43.9%</td><td>21.3%</td></tr><tr><td>$48.20</td><td>HPE</td><td>OW</td><td>16.6%</td><td>0.8%</td><td>1.4%</td><td>34.1%</td><td>14.7%</td></tr><tr><td>$175.40</td><td>GLW</td><td>EW</td><td>17.4%</td><td>0.3%</td><td>101.8%</td><td>54.6%</td><td>71.7%</td></tr><tr><td>$117.33</td><td>CSCO</td><td>EW</td><td>13.1%</td><td>0.9%</td><td>45.3%</td><td>127.2%</td><td>42.9%</td></tr><tr><td></td><td>Average</td><td></td><td>46.0%</td><td></td><td>63.2%</td><td>63.3%</td><td>39.7%</td></tr><tr><td></td><td>Total</td><td></td><td></td><td>18.5%</td><td></td><td></td><td></td></tr></table>

Priced as of 6/17/26. Delta share price is vs our last report's pricing (5/29/26). Industry view: Neutral. OW = Overweight; EW = Equal Weight; UW = Underweight. For full disclosures on each covered company, including details of our company-specific valuation methodology and risks, please refer to https://publicresearch.barcap.com. Source: BARC Estimates, Bloomberg, 650 Group

With Cloud AI growth moving higher across the industry, and the latest round of hyperscaler earnings highlighting increased capex expectations, our average cloud AI revenue growth CAGR for 2023-27E is \~62% on average vs our initial estimate of \~53%.

Below is a side-by-side comparison of current implied AI multiples vs May 29th.

FIGURE 2. Summary of Implied Current AI P/E

<table><tr><td>Share Price</td><td>Company</td><td>Rating</td><td>p/e on CY27</td><td>core p/E</td><td>implied Al p/e</td></tr><tr><td>$27.78</td><td>SMCI</td><td>EW</td><td>7x</td><td>11x</td><td>3x</td></tr><tr><td>$584.38</td><td>FN</td><td>OW</td><td>32x</td><td>14x</td><td>35x</td></tr><tr><td>$380.37</td><td>CLS</td><td>OW</td><td>26x</td><td>12x</td><td>31x</td></tr><tr><td>$164.93</td><td>ANET</td><td>OW</td><td>38x</td><td>32x</td><td>41x</td></tr><tr><td>$436.72</td><td>CIEN</td><td>OW</td><td>44x</td><td>18x</td><td>76x</td></tr><tr><td>$374.98</td><td>JBL</td><td>OW</td><td>21x</td><td>12x</td><td>31x</td></tr><tr><td>$143.13</td><td>FLEX</td><td>OW</td><td>23x</td><td>12x</td><td>38x</td></tr><tr><td>$419.32</td><td>DELL</td><td>OW</td><td>19x</td><td>10x</td><td>58x</td></tr><tr><td>$350.70</td><td>KEYS</td><td>OW</td><td>28x</td><td>22x</td><td>68x</td></tr><tr><td>$48.20</td><td>HPE</td><td>OW</td><td>12x</td><td>11x</td><td>58x</td></tr><tr><td>$175.40</td><td>GLW</td><td>EW</td><td>45x</td><td>19x</td><td>134x</td></tr><tr><td>$117.33</td><td>CSCO</td><td>EW</td><td>24x</td><td>18x</td><td>69x</td></tr><tr><td></td><td>Average</td><td></td><td>27x</td><td>16x</td><td>54x</td></tr></table>

FIGURE 3. Summary of Implied AI P/E as of 5/29/26

<table><tr><td>Share Price</td><td>Company</td><td>Rating</td><td>p/e on CY27</td><td>core p/E</td><td>implied Al p/e</td></tr><tr><td>$46.09</td><td>SMCI</td><td>EW</td><td>11x</td><td>11x</td><td>7x</td></tr><tr><td>$654.16</td><td>FN</td><td>OW</td><td>36x</td><td>14x</td><td>40x</td></tr><tr><td>$385.39</td><td>CLS</td><td>OW</td><td>26x</td><td>12x</td><td>31x</td></tr><tr><td>$159.47</td><td>ANET</td><td>OW</td><td>37x</td><td>32x</td><td>40x</td></tr><tr><td>$580.23</td><td>CIEN</td><td>OW</td><td>64x</td><td>18x</td><td>115x</td></tr><tr><td>$364.56</td><td>JBL</td><td>OW</td><td>23x</td><td>12x</td><td>37x</td></tr><tr><td>$150.78</td><td>FLEX</td><td>OW</td><td>26x</td><td>12x</td><td>40x</td></tr><tr><td>$420.91</td><td>DELL</td><td>OW</td><td>19x</td><td>10x</td><td>58x</td></tr><tr><td>$338.33</td><td>KEYS</td><td>OW</td><td>27x</td><td>22x</td><td>63x</td></tr><tr><td>$43.04</td><td>HPE</td><td>OW</td><td>15x</td><td>11x</td><td>55x</td></tr><tr><td>$181.16</td><td>GLW</td><td>EW</td><td>47x</td><td>19x</td><td>141x</td></tr><tr><td>$120.42</td><td>CSCO</td><td>EW</td><td>25x</td><td>18x</td><td>72x</td></tr><tr><td></td><td>Average</td><td></td><td>30x</td><td>16x</td><td>58x</td></tr></table>

Industry view: Neutral. OW = Overweight; EW = Equal Weight; UW = Underweight. For full disclosures on each covered company, including details of our company-specific valuation methodology and risks, please refer to https://publicresearch.barcap.com Source: Company Documents, Bloomberg, BARC estimates.  
Industry view: Neutral. OW = Overweight; EW = Equal Weight; UW = Underweight. For full disclosures on each covered company, including details of our company-specific valuation methodology and risks, please refer to https://publicresearch.barcap.com Source: Company Documents, Bloomberg, BARC estimates.

In the last update, within our illustrative math, we moved DELL's, HPE's, and CSCO's core business multiples up by a turn, given each's recent legacy business outperformance (on-prem seems to be doing better), ability to handle the current constrained component environment, and AI business momentum.

Despite CIEN's strong earnings print, given the run-up in the stock intra-Q (+107% vs SPX +11%, NDX +22% from 3.05.26-6.03.26), the print was not enough to drive the stock price higher, tumbling the stock and implied AI multiple. FN also saw downward pressure given its CM relationship to CIEN. SMCI announced \$7Bn equity and equity-linked financing transactions to fund AI orders early June, tumbling the stock on the implied dilution expectations.

Priced as of 6/17/26

FIGURE 4. AI Bucketed Stocks Implied AI Multiple Timeline

<table><tr><td></td><td>SMCI</td><td>FN</td><td>CLS</td><td>ANET</td><td>CIEN</td><td>JBL</td><td>FLEX</td><td>DELL</td><td>KEYS</td><td>HPE</td><td>GLW</td><td>CSCO</td></tr><tr><td>CY26 % Cloud/AI Revenue</td><td>86.9%</td><td>82.5%</td><td>82.3%</td><td>72.0%</td><td>56.2%</td><td>40.0%</td><td>29.9%</td><td>35.8%</td><td>19.2%</td><td>16.6%</td><td>17.4%</td><td>13.1%</td></tr><tr><td>CY26 Cloud/AI Revenue Growth</td><td>69.8%</td><td>40.6%</td><td>51.1%</td><td>35.5%</td><td>55.4%</td><td>51.1%</td><td>52.3%</td><td>144.1%</td><td>43.9%</td><td>34.1%</td><td>54.6%</td><td>127.2%</td></tr><tr><td>CY27 Cloud/AI Revenue Growth</td><td>20.8%</td><td>18.6%</td><td>46.5%</td><td>25.9%</td><td>39.4%</td><td>46.5%</td><td>94.9%</td><td>33.0%</td><td>21.3%</td><td>14.7%</td><td>71.7%</td><td>42.9%</td></tr><tr><td>Current Multiple</td><td>6.5x</td><td>32.4x</td><td>25.8x</td><td>38.1x</td><td>43.7x</td><td>20.7x</td><td>23.2x</td><td>19.1x</td><td>28.4x</td><td>11.9x</td><td>45.1x</td><td>24.1x</td></tr><tr><td>Core Multiple</td><td>11.0x</td><td>14.0x</td><td>12.0x</td><td>32.0x</td><td>18.0x</td><td>12.0x</td><td>12.0x</td><td>10.0x</td><td>22.0x</td><td>11.0x</td><td>18.5x</td><td>18.0x</td></tr><tr><td>Current Implied AI Multiple</td><td>3.3x</td><td>35.4x</td><td>30.5x</td><td>41.3x</td><td>76.0x</td><td>31.0x</td><td>38.0x</td><td>58.0x</td><td>68.4x</td><td>58.0x</td><td>134.0x</td><td>68.5x</td></tr><tr><td>Implied AI Multiple - 5/29/26</td><td>7.3x</td><td>39.9x</td><td>31.0x</td><td>39.5x</td><td>115.3x</td><td>36.5x</td><td>40.3x</td><td>58.3x</td><td>63.2x</td><td>55.0x</td><td>141.0x</td><td>72.0x</td></tr><tr><td>Implied AI Multiple - 5/20/26</td><td>4.5x</td><td>40.5x</td><td>27.8x</td><td>33.5x</td><td>109.5x</td><td>33.8x</td><td>34.0x</td><td>35.3x</td><td>65.0x</td><td>35.5x</td><td>141.0x</td><td>70.0x</td></tr><tr><td>Implied AI Multiple - 5/7/26</td><td>4.8x</td><td>38.1x</td><td>31.0x</td><td>34.0x</td><td>106.3x</td><td>34.3x</td><td>34.5x</td><td>32.0x</td><td>88.5x</td><td>27.0x</td><td>142.0x</td><td>48.0x</td></tr><tr><td>Implied AI Multiple - 4/22/26</td><td>4.5x</td><td>41.7x</td><td>43.5x</td><td>55.0x</td><td>109.0x</td><td>39.0x</td><td>34.0x</td><td>33.8x</td><td>92.0x</td><td>33.0x</td><td>185.0x</td><td>33.0x</td></tr><tr><td>Implied AI Multiple - 4/08/26</td><td>3.0x</td><td>37.0x</td><td>33.5x</td><td>41.5x</td><td>111.0x</td><td>31.8x</td><td>27.5x</td><td>26.0x</td><td>83.0x</td><td>18.0x</td><td>190.0x</td><td>25.0x</td></tr><tr><td>Implied AI Multiple - 3/18/26</td><td>4.6x</td><td>30.7x</td><td>28.3x</td><td>37.0x</td><td>85.0x</td><td>26.6x</td><td>21.0x</td><td>18.5x</td><td>65.0x</td><td>6.5x</td><td>126.0x</td><td>17.0x</td></tr><tr><td>Implied AI Multiple - 2/26/26</td><td>5.5x</td><td>33.5x</td><td>28.5x</td><td>35.5x</td><td>69.8x</td><td>28.0x</td><td>20.0x</td><td>10.0x</td><td>75.5x</td><td>6.0x</td><td>157.0x</td><td>17.0x</td></tr><tr><td>Implied AI Multiple - 2/11/26</td><td>6.0x</td><td>30.0x</td><td>34.0x</td><td>42.0x</td><td>58.0x</td><td>27.0x</td><td>22.0x</td><td>13.0x</td><td>39.0x</td><td>8.0x</td><td>127.0x</td><td>34.0x</td></tr></table>

Source: Bloomberg, Company Documents, BARC Estimates

\- SMCI saw the largest share price movement in the bucket of stocks (-40% since 5.29.26) due to the financing announcement mentioned above and the implied share dilution expectations. In conjunction with the financing announcement, SMCI highlighted it received \~\$39Bn of incremental AI orders since Q-end that are expected to be fulfilled in the next \~2-3 Qs. However, the company has had issues in the past with hitting top-line expectations (with customer readiness usually cited), so it is unclear to us the realistic timeline on this order fulfillment.

\- CIEN also saw material downward share price movement (-25% since 5.29.26), though we believe this largely due to the run-up in the stock into earnings \~two weeks ago. We do not view this as a slowdown in the optical space, but more so earnings not matching the high bar set by the share price run-up. However, because CIEN's earnings failed to meet street expectations, the stock also dragged down other optical plays, notably FN.

\- HPE was a notable share gainer (+12% since 5.29.26), given strong earnings, news circulating around another activist fund taking a stake in the company, and follow-on effects from the positive sentiment from DELL earnings late last month. Interestingly, the implied AI multiple saw rapid acceleration since we began this series, moving from HSD to now >50x. We continue to like the stock, given the company's higher margin networking business and conservative guide for the year.

We also take a look at companies under our coverage that have been excluded from the AI wave (i.e., AAPL, GRMN, AXON, MSI, etc.) and look at how their multiples compare since our last report and also vs their respective 'core' P/E multiples. These stocks, on average, are down HSD since our last reading on May 29th (vs SPX -2%).

FIGURE 5. Summary of non-AI plays multiples as of current pricing

<table><tr><td>Share Price</td><td>Delta Share Price</td><td>Company</td><td>p/e on CY27</td><td>core p/e</td></tr><tr><td>$295.95</td><td>-5%</td><td>AAPL</td><td>29x</td><td>17x</td></tr><tr><td>$231.89</td><td>-1%</td><td>GRMN</td><td>23x</td><td>22x</td></tr><tr><td>$105.94</td><td>-13%</td><td>LOGI</td><td>17x</td><td>22x</td></tr><tr><td>$72.67</td><td>-9%</td><td>P</td><td>26x</td><td>70x</td></tr><tr><td>$154.81</td><td>-11%</td><td>NTAP</td><td>16x</td><td>15x</td></tr><tr><td>$23.18</td><td>-14%</td><td>HPQ</td><td>7x</td><td>10x</td></tr><tr><td>$46.47</td><td>-11%</td><td>NTNX</td><td>20x</td><td>50x</td></tr><tr><td>$384.88</td><td>0%</td><td>FFIV</td><td>21x</td><td>17x</td></tr><tr><td>$423.01</td><td>-6%</td><td>AXON</td><td>41x</td><td>68x</td></tr><tr><td>$400.70</td><td>-1%</td><td>MSI</td><td>21x</td><td>19x</td></tr><tr><td></td><td></td><td>Average</td><td>22x</td><td>31x</td></tr></table>

FIGURE 6. Summary of non-AI plays multiples as of 5/29/26

<table><tr><td>Share Price</td><td>Delta Share Price</td><td>Company</td><td>p/e on CY27</td><td>core p/e</td></tr><tr><td>$312.06</td><td>3%</td><td>AAPL</td><td>31x</td><td>17x</t

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
