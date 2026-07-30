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
# SK Hynix

# Significant de-rating unwarranted - reiterate Buy

## Fundamentals still in place, buybacks could follow

SK Hynix shares are down 52% from their 22 June peak, although still up 115% YTD, while consensus/UBS estimates have been lifted 361%/281% for '27E OP. This now leaves the stock at 1.66x NTM Book, which implies a LT ROE of 18.9%, compared to UBSe 40.2% for '27-31E (average) and post DRAM consolidation (2012), pre AI (2022) average of 17.7%. Yet, the memory semis industry has dramatically changed. We continue to expect agentic AI to boost up memory bit demand growth into 2027 with DRAM bit demand growth moving up to 36% YoY from 22% in 2026, NAND to 23% from 20% (see our recent APAC Focus report for a detailed analysis: link). Revised Long Term Agreements are also being put in place by SK Hynix at a faster pace than we expected, with 10 signed and more being negotiated. We believe customers signed up to date include US hyperscalers but also large OEMs. This may shave off some of the ASP upside near term, but will likely be accretive to margins/returns longer term. HBM negotiations for 2027 and beyond have progressed. The main risk remains memory affordability, especially as it drives hyperscaler capex further up (link). With more stable profits longer term and elevated FCFs, we believe SK Hynix may initiate share buybacks in 2H26 with a more comprehensive update to follow.

## DRAM ASP downside in 2Q, increasing capex estimates

1/ DRAM ASPs: Only up 30% QoQ in 2Q26. We see three key factors: a/ Mobile DRAM increased in the DRAM revenue mix to 19% of total, with pricing below other segments; b/ The fixed portion of LTA pricing kicked in for some large contracts; c/ HBM4 shipments started in volumes, but late in the quarter. 2/ Capex: SK Hynix guided '26 to "high Won40tn". We raise our forecast to Won47tn (was Won45tn) or +71% YoY, '27E to Won62tn (was Won60tn) or +31% YoY, and '28 to Won67tn (was Won63tn) or +8% YoY. Yongin 1 first clean room is due to take on equipment in Feb '27 (as expected), and the second clean room later in 2027. M17 (NAND) could ramp from 2029.

## First earnings forecast cut in a while, but OP est. still 17% above '27E consensus

We lower 3Q26E OP to Won86tn from Won100tn, slightly ahead of consensus. This comes from us assuming a higher LTA coverage ratio and hence DRAM ASPs +19% QoQ (was +21% from higher base), with NAND unchanged +25% QoQ. For similar reasons, we lower our DRAM ASP estimates for '27/'28, more than offsetting higher bit growth ests., and cut our '27/'28E OP to Won505tn/Won544tn (-19%/-18% from prior) (and hence EPS ests. down by 19/19%). We continue to forecast substantial FCF generation in '26/'27/'28E at Won188tn/Won320tn/Won374tn respectively.

## Valuation: PT Won3.00m from Won3.20m; maintain Buy

We value SK Hynix shares at 3.65x NTM P/BV (was 3.67x) based on our long-term ROE forecast of 40.2% (was 42.3%) and CoE of 11.5%.

## Equities

<table><tr><td>Korea</td></tr><tr><td>Semiconductors</td></tr></table>

12-month rating Buy

12m price target Won3,000,000

Price (29 Jul 2026) Won1,401,000

RIC: 000660.KS BBG: 000660 KS  
Trading data and key metrics

<table><tr><td>52-wk range</td><td>Won2,919,000-245,000</td></tr><tr><td>Market cap.</td><td>Won1,019,931b/US$704b</td></tr><tr><td>Shares o/s</td><td>728m (ORD)</td></tr><tr><td>Free float</td><td>66%</td></tr><tr><td>Avg. daily volume (&#x27;000)</td><td>5,652</td></tr><tr><td>Avg. daily value (m)</td><td>Won11,930,310.2</td></tr><tr><td>Common s/h equity (12/26E)</td><td>Won397268b</td></tr><tr><td>P/BV (12/26E)</td><td>2.5x</td></tr><tr><td>Net debt to EBITDA (12/26E)</td><td>NM</td></tr></table>

EPS (UBS, diluted) (Won)

<table><tr><td></td><td>From</td><td>To</td><td>% ch</td><td>Cons.</td></tr><tr><td>12/26E</td><td>375,858</td><td>396,943</td><td>6</td><td>317,543</td></tr><tr><td>12/27E</td><td>713,786</td><td>576,936</td><td>-19</td><td>455,640</td></tr><tr><td>12/28E</td><td>839,779</td><td>680,722</td><td>-19</td><td>473,683</td></tr></table>

Nicolas Gaudois
Analyst
nicolas.gaudois@ubs.com
+65-6495 5148

Jimmy Yoon
Analyst
jimmy.yoon@ubs.com
+65-6495 4617

Luke Yoo
Analyst
luke.yoo@ubs.com
+82-2-3702 8132

<table><tr><td>Highlights (Wonb)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>Revenues</td><td>32,766</td><td>66,193</td><td>97,147</td><td>364,681</td><td>612,749</td><td>681,271</td><td>587,048</td><td>673,181</td></tr><tr><td>EBIT (UBS)</td><td>(7,730)</td><td>23,467</td><td>47,206</td><td>286,637</td><td>504,523</td><td>544,469</td><td>429,368</td><td>492,456</td></tr><tr><td>Net earnings (UBS)</td><td>(9,138)</td><td>19,797</td><td>42,948</td><td>281,375</td><td>393,950</td><td>425,386</td><td>335,797</td><td>385,122</td></tr><tr><td>EPS (UBS, diluted) (Won)</td><td>(12,552)</td><td>27,193</td><td>58,994</td><td>396,943</td><td>576,936</td><td>680,722</td><td>608,171</td><td>828,890</td></tr><tr><td>DPS (net) (Won)</td><td>1,200</td><td>2,205</td><td>3,000</td><td>22,725</td><td>51,125</td><td>66,125</td><td>106,125</td><td>121,125</td></tr><tr><td>Net (debt) / cash</td><td>(20,548)</td><td>(8,527)</td><td>12,694</td><td>170,674</td><td>429,829</td><td>680,257</td><td>873,509</td><td>1,051,763</td></tr></table>

<table><tr><td>Profitability/valuation</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>EBIT (UBS) margin %</td><td>(23.6)</td><td>35.5</td><td>48.6</td><td>78.6</td><td>82.3</td><td>79.9</td><td>73.1</td><td>73.2</td></tr><tr><td>ROIC (EBIT) %</td><td>(10.9)</td><td>32.4</td><td>56.0</td><td>193.2</td><td>208.9</td><td>178.9</td><td>125.8</td><td>133.1</td></tr><tr><td>EV/EBITDA (UBS core) x</td><td>15.6</td><td>3.9</td><td>3.4</td><td>3.0</td><td>1.3</td><td>0.8</td><td>0.5</td><td>0.1</td></tr><tr><td>P/E (UBS, diluted) x</td><td>(8.6)</td><td>6.6</td><td>5.2</td><td>3.5</td><td>2.4</td><td>2.1</td><td>2.3</td><td>1.7</td></tr><tr><td>Equity FCF (UBS) yield %</td><td>(8.2)</td><td>10.5</td><td>12.0</td><td>18.1</td><td>31.4</td><td>36.6</td><td>30.7</td><td>34.3</td></tr><tr><td>Dividend yield (net) %</td><td>1.1</td><td>1.2</td><td>1.0</td><td>1.6</td><td>3.6</td><td>4.7</td><td>7.6</td><td>8.6</td></tr></table>

Source: Company accounts, LSEG Eikon, UBS estimates. Metrics marked as (UBS) have had analyst adjustments applied. Valuations: based on an average share price that year, (E): based on a share price of Won 1,401,000 on 29-Jul-2026

PIVOTAL QUESTIONS

## UBS THESIS MAP a guide to our thinking and what's where in this report

## Q: Will memory undersupply continue into 2028?

Yes, in our view. Agentic AI is boosting further memory demand on multiple fronts beyond HBM, including DDR5/LPDDR5 for conventional servers and CPU head nodes in AI servers, as well as NAND flash for KV Cache and Storage. We now forecast an acceleration of memory demand growth into 2027 with DRAM bit end-consumption growing 36% YoY vs 22% in 2026E, and NAND flash 23% from 20%. As almost all of the incremental wafer capacity addition for DRAM is going to HBM, and no new capacity ex China is being added to NAND, supply is not catching up with demand. The main risk remains affordability as memory industry revenues are approaching US\$1.8tn in 2027E.

## Q: Will SK Hynix retain the lead in HBM in 2026 and 2027?

We estimate the capacity deployed for HBM will reach 230k wpm by the end of 2026 and 270k by end 2027. This leads us to forecast 17.2bn Gb of HBM shipment in 2026 (+37% YoY) and 23.0bn in 2027 (+34% YoY). We forecast SK Hynix to retain the #1 market share in HBM with 48% of industry bit shipments in 2026, but fall slightly below Samsung in 2027 with 39% of industry bit shipments (Samsung 41%; Micron 20%).

## Q: Will SK Hynix engage in material shareholder returns?

Yes. In spite of continuous upward revision of capex forecasts, we expect SK Hynix to generate FCF of Won188tn/Won320tn/Won374tn in 2026E/2027E/2028E. We believe SK Hynix may initiate share buybacks in 2H26 (UBSe Won12tn) with a more comprehensive update on the company's shareholder returns policy (possibly during the 3Q26 conference call). Over time, we remain of the view that SK Hynix will move towards returning 50% of FCF to shareholders, combining both dividends and share buybacks.

SK Hynix shares are now down 52% from their 22 June peak. Despite the recent sell-off, however, we believe fundamentals remain strong with agentic AI driving a significant uplift in memory demand. At current valuation, we do not believe SK Hynix shares fully reflect structurally higher memory profitability, stronger FCF generation and significantly enhanced returns to shareholders.

1) HBM demand is resulting in more capacity allocation away from DDR, which may moderate possible cyclical corrections in the longer run. We estimate front-end DRAM capacity for HBM could reach 500k/690k wpm by the end of 2026/2027, or 25%/31% of industry capacity. 2) LTAs continue to be signed by memory players, which should narrow margins through the cycle and be ROE accretive. 3) Agentic AI continues to level up memory demand, as evidenced with strong server CPU and conventional server demand.

Following the recent sell-off, SK Hynix shares now trade at 1.66x NTM P/BV, discounting a long-term ROE of 18.8% vs our estimate of 40.2%.

![](images/fc61324645cac811cbca8ee7a83dafc8ae907bf2d8e6ed05b35e00245c14349f.jpg)

<table><tr><td>Value drivers</td><td>DRAM ASP % YoY&#x27;26E/&#x27;27E</td><td>NAND ASP % YoY&#x27;26E/&#x27;27E</td><td>Operating Profit (Won)&#x27;26E/&#x27;27E</td></tr><tr><td>Won3.30m upside</td><td>+182%/+56%</td><td>+264%/+50%</td><td>292tn/583tn</td></tr><tr><td>Won3.00m base</td><td>+177%/+39%</td><td>+260%/+41%</td><td>287tn/505tn</td></tr><tr><td>Won800k downside</td><td>+172%/+26%</td><td>+232%/+27%</td><td>274tn/426tn</td></tr></table>

Source: UBS estimates

SK Hynix is a pure-play memory semiconductor company, specialising in DRAM (68% of sales in 2024) and NAND flash memory chips (29% of sales). It is also the leading supplier of HBM devices.

## UBS FORECASTS

Figure 1: SK Hynix – 2Q26 results summary

<table><tr><td colspan="2">(Won bn)</td><td>2Q26Actual</td><td>UBSe</td><td>Cons</td><td>1Q26Actual</td><td>% QoQ</td><td>2Q25Actual</td><td>% YoY</td></tr><tr><td colspan="2">Revenues</td><td>79,319</td><td>86,458</td><td>79,964</td><td>52,576</td><td>51%</td><td>22,232</td><td>257%</td></tr><tr><td colspan="2">Gross Profit</td><td>65,991</td><td>73,647</td><td></td><td>41,679</td><td>58%</td><td>11,983</td><td>451%</td></tr><tr><td></td><td>% GM</td><td>83.2%</td><td>85.2%</td><td></td><td>79.3%</td><td></td><td>53.9%</td><td></td></tr><tr><td colspan="2">Operating Profit</td><td>60,543</td><td>68,501</td><td>60,522</td><td>37,610</td><td>61%</td><td>9,213</td><td>557%</td></tr><tr><td></td><td>% OpM</td><td>76.3%</td><td>79.2%</td><td>75.7%</td><td>71.5%</td><td></td><td>41.4%</td><td></td></tr><tr><td colspan="2">EPS (Won)</td><td>128,874</td><td>75,035</td><td>66,876</td><td>56,610</td><td>128%</td><td>9,610</td><td>1241%</td></tr><tr><td colspan="9">DRAM</td></tr><tr><td colspan="2">Revenues</td><td>57,903</td><td>66,465</td><td></td><td>41,005</td><td>41%</td><td>17,130</td><td>238%</td></tr><tr><td colspan="2">Bit Growth % QoQ</td><td>Up HSD%</td><td>+7.5%</td><td></td><td>-0.3%</td><td></td><td>+25.0%</td><td></td></tr><tr><td colspan="2">ASP % QoQ</td><td>Up c. 30%</td><td>+42.6%</td><td></td><td>+65.1%</td><td></td><td>+2.1%</td><td></td></tr><tr><td colspan="9">NAND</td></tr><tr><td colspan="2">Revenues</td><td>21,416</td><td>19,744</td><td></td><td>11,342</td><td>89%</td><td>4,732</td><td>353%</td></tr><tr><td colspan="2">Bit Growth % QoQ</td><td>Up mid-10s%</td><td>+15.0%</td><td></td><td>-10.4%</td><td></td><td>+73.6%</td><td></td></tr><tr><td colspan="2">ASP % QoQ</td><td>Up mid-50s%</td><td>+43.3%</td><td></td><td>+71.2%</td><td></td><td>-9.6%</td><td></td></tr><tr><td colspan="9">Inventory</td></tr><tr><td colspan="2">Inventory</td><td>17,986</td><td>16,848</td><td></td><td>15,974</td><td></td><td>13,408</td><td></td></tr><tr><td colspan="2">Inventory days</td><td>123</td><td>120</td><td></td><td>134</td><td></td><td>119</td><td></td></tr></table>

Source: UBS estimates

Figure 2: SK Hynix – changes to estimates

<table><tr><td rowspan="2">(Won bn)</td><td colspan="3">3Q26E</td><td colspan="3">4Q26E</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td><td colspan="3">2029E</td></tr><tr><td>New</td><td>Old</td><td>Chg %</td><td>New</td><td>Old</td><td>Chg %</td><td>New</td><td>Old</td><td>Chg %</td><td>New</td><td>Old</td><td>Chg %</td><td>New</td><td>Old</td><td>Chg %</td><td>New</td><td>Old</td><td>Chg %</td></tr><tr><td>Total sales</td><td>106,805</td><td>120,751</td><td>-11.5%</td><td>125,982</td><td>143,804</td><td>-12.4%</td><td>364,681</td><td>403,589</td><td>-9.6%</td><td>612,749</td><td>726,083</td><td>-15.6%</td><td>681,271</td><td>795,236</td><td>-14.3%</td><td>587,048</td><td>590,945</td><td>-0.7%</td></tr><tr><td>DRAM sales</td><td>79,148</td><td>94,234</td><td>-16.0%</td><td>94,278</td><td>113,007</td><td>-16.6%</td><td>272,907</td><td>314,711</td><td>-13.3%</td><td>455,803</td><td>572,799</td><td>-20.4%</td><td>555,962</td><td>672,820</td><td>-17.4%</td><td>513,044</td><td>521,308</td><td>-1.6%</td></tr><tr><td>NAND Flash sales</td><td>27,384</td><td>26,220</td><td>4.4%</td><td>31,449</td><td>30,515</td><td>3.1%</td><td>90,614</td><td>87,483</td><td>3.6%</td><td>155,939</td><td>152,167</td><td>2.5%</td><td>124,275</td><td>121,270</td><td>2.5%</td><td>72,959</td><td>68,478</td><td>6.5%</td></tr><tr><td>Operating profit</td><td>85,682</td><td>100,219</td><td>-14.5%</td><td>102,802</td><td>120,680</td><td>-14.8%</td><td>286,637</td><td>327,010</td><td>-12.3%</td><td>504,523</td><td>622,651</td><td>-19.0%</td><td>544,469</td><td>667,048</td><td>-18.4%</td><td>429,368</td><td>445,177</td><td>-3.6%</td></tr><tr><td>DRAM OP</td><td>65,518</td><td>80,739</td><td>-18.9%</td><td>79,080</td><td>97,594</td><td>-19.0%</td><td>222,978</td><td>264,838</td><td>-15.8%</td><td>383,548</td><td>502,886</td><td>-23.7%</td><td>460,918</td><td>582,674</td><td>-20.9%</td><td>403,305</td><td>415,541</td><td>-2.9%</td></tr><tr><td>NAND Flash OP</td><td>20,221</td><td>19,542</td><td>3.5%</td><td>23,778</td><td>23,148</td><td>2.7%</td><td>63,483</td><td>61,596</td><td>3.1%</td><td>121,168</td><td>119,979</td><td>1.0%</td><td>83,727</td><td>84,569</td><td>-1.0%</td><td>26,192</td><td>29,779</td><td>-12.0%</td></tr><tr><td>% OP margin</td><td>80.2%</td><td>83.0%</td><td></td><td>81.6%</td><td>83.9%</td><td></td><td>78.6%</td><td>81.0%</td><td></td><td>82.3%</td><td>85.8%</td><td></td><td>79.9%</td><td>83.9%</td><td></td><td>73.1%</td><td>75.3%</td><td></td></tr><tr><td>EPS</td><td>94,463</td><td>110,365</td><td>-14.4%</td><td>114,087</td><td>133,848</td><td>-14.8%</td><td>396,943</td><td>375,858</td><td>5.6%</td><td>576,936</td><td>713,786</td><td>-19.2%</td><td>680,722</td><td>839,779</td><td>-18.9%</td><td>608,171</td><td>634,958</td><td>-4.2%</td></tr></table>

Source: UBS estimates

Figure 3: SK Hynix – UBSe vs consensus

<table><tr><td rowspan="2">(Won bn)</td><td colspan="3">3Q26E</td><td colspan="3">4Q26E</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td><td colspan="3">2029E</td></tr><tr><td>UBSe</td><td>Cons</td><td>Delta</td><td>UBSe</td><td>Cons</td><td>Delta</td><td>UBSe</td><td>Cons</td><td>Delta</td><td>UBSe</td><td>Cons</td><td>Delta</td><td>UBSe</td><td>Cons</td><td>Delta</td><td>UBSe</td><td>Cons</td><td>Delta</td></tr><tr><td>Revenues</td><td>106,805</td><td>105,040</td><td>1.7%</td><td>125,982</td><td>116,9

[中间内容因长度限制已省略]

d not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

![](images/493acc9e7b563fed958becd729c91d286a5dde088b48a6eb7f3de434986f63f1.jpg)

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
