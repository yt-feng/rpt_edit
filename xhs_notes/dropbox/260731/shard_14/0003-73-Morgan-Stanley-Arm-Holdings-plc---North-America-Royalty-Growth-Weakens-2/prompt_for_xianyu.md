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
e = MS estimates

§ = Consensus data is provided by Refinitiv Estimates

# Royalty Growth Weakens

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>US$202.00</td><td>US$212.00</td></tr></table>

Arm's Q1 beat and better guide were overshadowed by slowing royalties growth and a lack of updates longer term for the AGI CPU business. We maintain our Equal-weight rating and, given recent price action, think the stock now better reflects the new CPU opportunity.

## Key Takeaways

\- AGI CPU sales are now expected \$1bn+ across FY27-28 versus a \$2bn+ pipeline; supply coverage is the key constraint.

\- AGI is expanding into head-node and servers as well as agentic workloads, broadening the addressable use case.

Q2 royalty growth is pressured by smartphone mix; data-centre royalties are the key offset and should more than double y/y.

\- Opex remains elevated to fund silicon capability; Q1 under-spend was timing-related, with investment stepping up through FY27.

■ After the post-Arm Everywhere re-rating, valuation better discounts the CPU opportunity; TAM, execution, supply and differentiation remain the key debates.

AGI CPU: confidence rises, but supply visibility not yet complete. Management now expects AGI CPU sales to exceed \$1bn over FY27-28, versus c.\$1bn previously, while reiterating a demand pipeline above \$2bn. Customer breadth is improving across the US and China, supplementing existing engagements. The use case is also broadening: management positioned AGI not only for agentic application workloads, but also as a head-node system CPU and for traditional servers. The near-term constraint remains supply rather than demand. Progress is being made across wafers, memory, substrates and test, but management may not be able to confirm full coverage of the \$2bn+ pipeline until the Q3 print. Arm also intends to pass through higher input costs; the degree of customer acceptance remains an execution variable. Following a sharp re-rating since the March 2026 Arm Everywhere event, we think the stock now better reflects the new CPU opportunity. Key risks are supply availability, product differentiation versus competing CPU platforms and the power/TCO burden of deploying standalone orchestration CPUs at scale. We retain our c.\$125bn CPU TAM estimate for 2030; our implied Arm revenue estimates remain unchanged.

Royalties: weaker handset mix tempers the near-term setup; data centre remains the structural offset. Management guided to Q2 royalty growth to c.13% y/y, below prior expectations, as handset mix shifts towards mid-tier Android devices from

<table><tr><td colspan="2">Lee Simpson</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Lee.Simpson@morganstanley.com</td><td>+44 20 7425-3378</td></tr><tr><td colspan="2">Shawn Kim</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Shawn.Kim@morganstanley.com</td><td>+44 20 7677-1018</td></tr><tr><td colspan="2">Nigel van Putten</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Nigel.Putten@morganstanley.com</td><td>+44 20 7425-2803</td></tr><tr><td colspan="2">Amelia M Scicluna</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Amelia.Scicluna@morganstanley.com</td><td>+44 20 7425-6694</td></tr></table>

<table><tr><td>Stock Rating</td><td>Equal-weight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>US$212.00</td></tr><tr><td>Shr price, close (Jul 29, 2026)</td><td>US$224.89</td></tr><tr><td>52-Week Range</td><td>US$452.70-100.02</td></tr><tr><td>Mkt cap, curr (mn)</td><td>US$231,062</td></tr><tr><td>Net debt (03/27e) (mn)*</td><td>US$(5,435)</td></tr><tr><td>EV, curr (mn)*</td><td>US$228,311</td></tr></table>

\* = GAAP or approximated based on GAAP

<table><tr><td>Fiscal Year Ending</td><td>03/26</td><td>03/27e</td><td>03/28e</td><td>03/29e</td></tr><tr><td>Sales / Revenue (US$ mn)**</td><td>4,920</td><td>6,088</td><td>8,954</td><td>11,637</td></tr><tr><td>EBITDA (US$ mn)**</td><td>2,364</td><td>2,810</td><td>4,675</td><td>6,277</td></tr><tr><td>EBIT (US$ mn)**</td><td>2,115</td><td>2,531</td><td>4,545</td><td>6,152</td></tr><tr><td>EPS (US$)**</td><td>1.77</td><td>2.06</td><td>3.69</td><td>5.13</td></tr><tr><td>Prior EPS (US$)**</td><td>-</td><td>1.93</td><td>3.51</td><td>4.91</td></tr><tr><td>EPS (US$)§</td><td>1.75</td><td>2.15</td><td>3.01</td><td>3.84</td></tr><tr><td>P/E**</td><td>85.5</td><td>108.9</td><td>60.9</td><td>43.8</td></tr><tr><td>EV/revenue*</td><td>32.1</td><td>37.1</td><td>24.8</td><td>18.7</td></tr><tr><td>EV/EBITDA**</td><td>66.7</td><td>80.3</td><td>47.5</td><td>34.7</td></tr><tr><td>EV/EBIT**</td><td>74.6</td><td>89.1</td><td>48.9</td><td>35.4</td></tr><tr><td>DPS (US$)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Div yld (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>FCF yld ratio (%)*</td><td>(0.1)</td><td>0.7</td><td>0.9</td><td>1.2</td></tr><tr><td>Net debt (US$ mn)*</td><td>(2,751)</td><td>(5,435)</td><td>(8,865)</td><td>(13,277)</td></tr><tr><td>Net debt/EBITDA**</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>RNOA (%)*</td><td>41.5</td><td>48.1</td><td>90.0</td><td>105.0</td></tr><tr><td>ROE (%)*</td><td>27.7</td><td>26.9</td><td>37.5</td><td>37.6</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework  
\*\* = Based on consensus methodology

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Armv8 partners and iOS gains share within premium smartphones. Licensing, expected to grow c.30% y/y, should offset part of the pressure, but the royalty deceleration is likely to disappoint investors positioned for a faster smartphone recovery. Armv9 and CSS penetration should still support handset royalty growth y/y, but the mix effect is weaker than expected. By contrast, data-centre royalties remain robust: Q1 revenue more than doubled y/y and management expects at least 100% annual growth for the next two to three years, supported by hyperscaler CPUs, NVIDIA's Grace and Vera ramps, and broader DPU/SmartNIC adoption. We see this as the cleaner structural driver, but it is not yet large enough to fully offset near-term smartphone volatility near term. Arm now guides FY27 royalty growth to the high teens y/y.

Opex: investment intensity remains elevated as Arm builds silicon capability. Q1 non-GAAP operating expenses were \$733m, up 18% y/y and c.\$27m below guidance due to timing. Q2 opex guidance of c.\$780m is broadly in line with consensus and confirms a continued step-up in R&D. We expect sequential opex growth through the balance of FY27 as Arm funds AGI CPU execution and adjacent silicon opportunities. This is strategically consistent with the scale of the opportunity, but it limits near-term operating leverage and raises the bar for revenue conversion. Arm expects to disclose silicon revenue separately once it reaches at least 10% of group revenue, which it anticipates in FY28. For investors, the key markers are therefore supply-backed AGI orders, evidence of pricing power on higher input costs, and a clearer path from elevated R&D to durable silicon gross profit.

Reiterate EW, PT up to \$212. We make slight adjustments to our model, in line with company guidance on licensing and royalties growth. This marginally increases our FY27 EPS estimate to \$2.06 (prior \$1.93) and FY28 estimate to \$3.69 (prior \$3.51). Maintaining the same valuation framework, this lifts our PT to \$212 (from \$202). We continue to value Arm on an SOTP basis to reflect distinct IP and chip business opportunities. We apply a 50x EV/EBIT multiple to the IP business, toward the upper end of Arm's historical range, reflecting cloud AI as an increasingly important growth driver. We value the chip business at 20x, still at a discount to global chipmakers (low-margin peer), but better reflecting Arm's longer-term growth potential. We remain Equal-weight as, although we like the CPU story, we think the stock already reflects a large part of the 2030 opportunity.

## Guidance and Financials

## Solid Q1 but no long-term updates

Arm reported a solid print for 1Q27 (April-June quarter), but gave little in the way of update to the longer-term story in CPUs. Instead, the company reiterated \$1bn+ CPU sales over FY27-28 and again suggested demand for c.\$2bn.

1Q27: Sales/EPS for Q1 of \$1.29bn/45c, ahead of consensus, with both licensing and royalties just ahead of the street at \$574m/\$715m (vs \$563m/\$700m expected). Royalties were in line with our estimate, despite what we think would have been robust cloud AI royalties this Q.

2Q27 guide: The guidance to Q2 talked of a sales range of \$1.33-1.43bn (vs. street at \$1.34bn) and EPS of 47c (vs street at 44c), or c.7% ahead at the mid-point. The company is again guiding for strong Q2 opex in line with that expected (c.\$780m non-GAAP), which we think is supportive of long-term development needs.

FY27: The company did not guide on full-year FY27, but did make some framework commentary for modelling, including royalties to grow high teens% with licensing up 25-30% y/y. Opex to grow 5-6% q/q through the rest of the year and SoftBank licensing contribution to be c.\$200m per quarter for the rest of the year (Q1: \$193m).

Exhibit 1: Arm Annual Income Statement

<table><tr><td>Annual Income Statement</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td><td>2027e</td><td>2028e</td><td>2029e</td></tr><tr><td>Revenues</td><td>2,027</td><td>2,703</td><td>2,679</td><td>3,233</td><td>4,007</td><td>4,920</td><td>6,088</td><td>8,954</td><td>11,637</td></tr><tr><td>Cost of goods Sold</td><td>-145</td><td>-131</td><td>-106</td><td>-154</td><td>-121</td><td>-121</td><td>-263</td><td>-1,068</td><td>-1,757</td></tr><tr><td>Gross profit</td><td>1,882</td><td>2,572</td><td>2,573</td><td>3,079</td><td>3,886</td><td>4,799</td><td>5,825</td><td>7,886</td><td>9,880</td></tr><tr><td>R&amp;D</td><td>-814</td><td>-995</td><td>-1,133</td><td>-1,979</td><td>-2,071</td><td>-2,776</td><td>-3,323</td><td>-3,840</td><td>-4,356</td></tr><tr><td>SG&amp;A</td><td>-826</td><td>-897</td><td>-762</td><td>-983</td><td>-984</td><td>-1,115</td><td>-1,234</td><td>-1,308</td><td>-1,386</td></tr><tr><td>Other income/(expenses)</td><td>-3</td><td>-47</td><td>-7</td><td>-6</td><td>0</td><td>-8</td><td>0</td><td>0</td><td>0</td></tr><tr><td>EBIT (reported)</td><td>239</td><td>633</td><td>671</td><td>111</td><td>831</td><td>900</td><td>1,268</td><td>2,738</td><td>4,137</td></tr><tr><td>Adjusted EBIT</td><td>304</td><td>731</td><td>783</td><td>1,382</td><td>1,818</td><td>2,115</td><td>2,531</td><td>4,545</td><td>6,152</td></tr><tr><td>Adjusted EBITDA</td><td>505</td><td>916</td><td>953</td><td>1,544</td><td>2,001</td><td>2,364</td><td>2,810</td><td>4,675</td><td>6,277</td></tr><tr><td>Net Financials &amp; other</td><td>458</td><td>153</td><td>0</td><td>101</td><td>-111</td><td>257</td><td>336</td><td>262</td><td>491</td></tr><tr><td>PBT (reported)</td><td>697</td><td>786</td><td>671</td><td>212</td><td>720</td><td>1,157</td><td>1,604</td><td>3,000</td><td>4,628</td></tr><tr><td>Income Tax</td><td>-153</td><td>-110</td><td>-147</td><td>94</td><td>72</td><td>-253</td><td>-177</td><td>-420</td><td>-648</td></tr><tr><td>discont. Ops.</td><td>-156</td><td>-127</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net Income (reported)</td><td>388</td><td>549</td><td>524</td><td>306</td><td>792</td><td>904</td><td>1,427</td><td>2,580</td><td>3,980</td></tr><tr><td>Net Income (non-GAAP)</td><td>595</td><td>663</td><td>657</td><td>1,307</td><td>1,820</td><td>1,889</td><td>2,226</td><td>3,980</td><td>5,537</td></tr><tr><td>EPS ($) Adjusted - Basic</td><td>0.58</td><td>0.65</td><td>0.64</td><td>1.27</td><td>1.73</td><td>1.78</td><td>2.09</td><td>3.73</td><td>5.19</td></tr><tr><td>EPS ($) Adjusted - Diluted</td><td>0.58</td><td>0.65</td><td>0.64</td><td>1.25</td><td>1.71</td><td>1.77</td><td>2.06</td><td>3.69</td><td>5.13</td></tr><tr><td>DPS ($)</td><td>0.73</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>

<table><tr><td></td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td><td>2027e</td><td>2028e</td><td>2029e</td></tr><tr><td>Sales growth - yy</td><td>7%</td><td>33%</td><td>-1%</td><td>21%</td><td>24%</td><td>23%</td><td>24%</td><td>47%</td><td>30%</td></tr><tr><td>Gross margin</td><td>92.8%</td><td>95.2%</td><td>96.0%</td><td>95.2%</td><td>97.0%</td><td>97.5%</td><td>95.7%</td><td>88.1%</td><td>84.9%</td></tr><tr><td>EBIT Margin</td><td>11.8%</td><td>23.4%</td><td>25.0%</td><td>3.4%</td><td>20.7%</td><td>18.3%</td><td>20.8%</td><td>30.6%</td><td>35.6%</td></tr><tr><td>Adjusted EBIT Margin</td><td>15.0%</td><td>27.0%</td><td>29.2%</td><td>42.7%</td><td>45.4%</td><td>43.0%</td><td>41.6%</td><td>50.8%</td><td>52.9%</td></tr><tr><td>EBITDA Margin</td><td>21.7%</td><td>30.3%</td><td>31.4%</td><td>8.4%</td><td>25.3%</td><td>23.4%</td><td>25.4%</td><td>32.0%</td><td>36.6%</td></tr><tr><td>Adjusted EBITDA Margin</td><td>24.9%</td><td>33.9%</td><td>35.6%</td><td>47.8%</td><td>49.9%</td><td>48.0%</td><td>46.2%</td><td>52.2%</td><td>53.9%</td></tr><tr><td>PBT margin</td><td>34.4%</td><td>29.1%</td><td>25.0%</td><td>6.6%</td><td>18.0%</td><td>23.5%</td><td>26.3%</td><td>33.5%</td><td>39.8%</td></tr><tr><td>Net margin (reported)</td><td>19.1%</td><td>20.3%</td><td>19.6%</td><td>9.5%</td><td>19.8%</td><td>18.4%</td><td>23.4%</td><td>28.8%</td><td>34.2%</td></tr><tr><td>Net margin - Adjusted</td><td>29.4%</td><td>24.5%</td><td>24.5%</td><td>40.4%</td><td>45.4%</td><td>38.4%</td><td>36.6%</td><td>44.5%</td><td>47.6%</td></tr><tr><td>Effective tax rate</td><td>-22%</td><td>-14%</td><td>-22%</td><td>44%</td><td>10%</td><td>-22%</td><td>-11%</td><td>-14%</td><td>-14%</td></tr></table>

Source: Company data, MS estimates (e). Note: March year-end.

Exhibit 2: Arm Quarterly Income Statement

<table><tr><td>Quarterly Income Statement</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>2026</td><td>1Q27</td><td>2Q27e</td><td>3Q27e</td><td>4Q27e</td><td>2027e</td></tr><tr><td>Revenues</td><td>1,053</td><td>1,135</td><td>1,242</td><td>1,490</td><td>4,920</td><td>1,289</td><td>1,412</td><td>1,606</td><td>1,781</td><td>6,088</td></tr><tr><td>Cost of goods Sold</td><td>-30</td><td>-29</td><td>-30</td><td>-32</td><td>-121</td><td>-36</td><td>-50</td><td>-58</td><td>-119</td><td>-263</td></tr><tr><td>Gross profit</td><td>1,023</td><td>1,106</td><td>1,212</td><td>1,458</td><td>4,799</td><td>1,253</td><td>1,362</td><td>1,548</td><td>1,661</td><td>5,825</td></tr><tr><td>R&amp;D</td><td>-650</td><td>-691</td><td>-737</td><td>-698</td><td>-2,776</td><td>-838</td><td>-791</td><td>-824</td><td>-870</td><td>-3,323</td></tr><tr><td>SG&amp;A</td><td>-259</td><td>-252</td><td>-284</td><td>-320</td><td>-1,115</td><td>-317</td><td>-298</td><td>-305</td><td>-314</td><td>-1,234</td></tr><tr><td>Other income/(expenses)</td><td>0</td><td>0</td><td>-6</td><td>-2</

[中间内容因长度限制已省略]

me preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/29/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>US$429.56</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>US$13.99</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>US$42.21</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>US$69.19</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>US$42.73</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>US$353.37</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>US$249.74</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>US$370.32</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>US$169.39</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>US$47.07</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>US$81.88</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>US$31.99</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>US$163.40</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>US$71.37</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>US$739.00</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>US$9.74</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>US$190.01</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>US$240.98</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>++</td><td>US$78.86</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>US$89.50</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>E (06/24/2026)</td><td>US$155.68</td></tr><tr><td>Quantinuum (QNT.O)</td><td>E (06/29/2026)</td><td>US$47.34</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>US$1,015.89</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>US$103.55</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>US$216.44</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>US$61.19</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>US$271.30</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>US$20.06</td></tr></table>

Lee Simpson

<table><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>US$224.89</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>US$332.76</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>US$373.69</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
