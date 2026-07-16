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
## Rio Tinto Ltd. (RIO.AX): 2Q26 result: Big assets perform strongly, Fe & metal prices strong, although working cap builds US\$1.2bn; Neutral

RIO reported a solid June Q with group copper equivalent (CuEq) production up 3% YoY in 1H26, supported by the highest first-half Pilbara iron ore production since 2018, another strong result from Escondida, and a continued strong ramp-up of the Oyu Tolgoi copper/gold underground (1H +31% YoY). That said, group copper production of 213kt in 2Q was down 7% QoQ (below GSe and Visible Alpha Consensus Data), impacted by lower Kennecott output due to reduced concentrate availability, geotechnical issues, and a flash converting furnace breach in June (requiring a \~75-day rebuild). Realised pricing for Fe/Al/Cu was broadly in-line with our estimates. Notably, RIO cut copper C1 net unit cost guidance to US30-50c/lb (from US65-75c/lb), in-line with our prior forecasts of US43c/lb (vs. Visible Alpha Consensus Data at US51c/lb), on higher gold prices and productivity. All other production and sales guidance for 2026 was maintained. Working cap increased by US\$1.2bn in the half and cash tax to Mongolia by \~US\$0.44bn.

Paul Young  
+61(2)9321-8302 |  
paul.young1@gs.com  
GS Australia Pty Ltd

Chris Bulgin
+61(2)9321-8936 | chris.bulgin@gs.com
GS Australia Pty Ltd

## 1H 2026 result preview

RIO will release 1H26 results on 29 July. We forecast underlying EBITDA US\$14.9bn (vs. Visible Alpha Consensus Data of US\$15.1bn; prior to the 2Q26 result), underlying earnings of \~US\$6.2bn, and net debt of \~US\$14.8bn, and an interim dividend of US\$1.90/share (based on a payout ratio of 50%, policy: 40%-60%, final dividend typically \~70%). We expect an update on the US\$5-10bn (vs GSe \~US\$10bn) of non-core divestments and cost out initiatives that were announced at the CMD last year.

## Key 2Q26 takeaways

Copper: Consolidated copper production of 213kt was down 7% QoQ/YoY (below GSe and Visible Alpha Consensus Data). Oyu Tolgoi metal-in-concentrate of 97kt (+12% YoY) drove 1H growth of +31% YoY, remaining on track to reach \~500ktpa (100%) from 2028-2036. Kennecott refined copper of 20kt was down 49% YoY, impacted by reduced high-quality concentrate availability, mine resequencing, a June concentrator maintenance (23 days), an April safety stand-down and, critically, a flash converting furnace breach in late June requiring an \~75-day rebuild (which will reduce refined copper and gold production in 2H 2026.). Total copper production estimates for the year are unchanged (unsold matte to convert to cathode and contribute to 2027 cash flows). Escondida refined production rose on improved Full SaL leach

performance. C1 net unit cost guidance was cut to US30-50c/lb (from US65-75c/lb) on higher gold prices (US\$4,026/oz assumption) and productivity.

☐ Resolution copper: RIO commenced surface drilling in newly accessible areas following the land exchange, with underground drilling scheduled to commence in 3Q26 (in-line with the schedule in our recent deep dive report on the project) to support further resource definition and geological data collection.

Iron ore: Pilbara production was stable YoY with 1H the highest since the 2018 record. 2Q Pilbara sales of 85.3Mt (100%) were up 7% YoY (+2% vs. GSe and Visible Alpha Consensus Data), the highest since 2020, with SP10 at 8% of sales. Pilbara unit cost guidance was held at US\$23.5-25/t (vs. GSe at US\$25.6/t) despite diesel headwinds, with the company noting a \~US\$0.8/t YoY impact from diesel (excludes impacts from inflation and FX etc). RIO achieved Pilbara pricing of US\$85.2/wmt FOB in 1H26 (vs US\$83.2 in 1H25) above our US\$82.4/t estimate. RIO noted port outload capacity will reduce to below 360Mtpa during some quarters in 2H 2026, 2027 and 2028 with several scheduled major capital projects underway (including Parker Point reclaimers) to improve system flexibility and prepare for Rhodes Ridge. We note RIO's medium term guidance of 345-360 vs. GSe at \~340Mtpa. IOC (Canada) production was down 22% YoY, with full-year shipments guidance (15-18Mt) subject to Canadian forest fire risk.

☐ Simandou: 2Q production increased \~16% QoQ following the 1Q fatality, with a phased restart. The SimFer mine (\~77% complete) and port/marine infrastructure (85% complete) are both progressing, though production remains constrained by temporary crushing facilities pending permanent plant delivery in 2H with first ore through the primary crusher expected 4Q 2026 and SimFer port commissioning in 1Q 2027. First customer collections completed in April with 2Q sales of 0.4Mt (100%) at 65.8% Fe. 7.6Mt of uncrushed ore stockpiled at the mine (9.6Mt across the system). Ramp-up toward full production rate (60Mtpa) is still expected in 2H 2028.

Aluminium: production was flat QoQ/YoY, with Kitimat, NZAS and AP60 ramping and Arvida's final two potlines closed as planned in June. Bauxite recovered 14% QoQ. Alumina production reduced QoQ on reliability events at Yarwun and Vaudreuil. Tariff costs of US\$773mn in 1H26 were in-line with our estimates and largely offset by a higher US Midwest premium (average MWP duty paid US\$2,406/t). The US\$1.5bn AP60 expansion was commissioned in May, with full ramp-up expected by end-2026.

Lithium: Lithium Carbonate Equivalent (LCE) production rose 15% QoQ to 14.6kt (in-line with GSe), driven by the Rincon starter plant ramp-up and first tonnes delivered at Sal de Vida and Fénix 1B, both ahead of plan. RIO reported realised LCE price for the first time of US\$18,960/t for 1H26.

Cashflow movements: Oyu Tolgoi paid \~US\$443mn in disputed Mongolian tax assessments in March (reserving its rights), and a \~US\$1.2bn working capital outflow occurred in 1H (higher iron ore inventory post-cyclones and Simandou ramp). We forecast net debt of \~US\$14.8bn as at 30 Jun 2026, increasing by \~US\$500mn HoH.

## EBITDA/NAV changes and Investment thesis

Overall, we adjust our 2026/27/28 EBITDA by -1%/1%/0% after incorporating the result and aligning to guidance, with our NAV largely unchanged at \~A\$196/sh. Our 12-month price target is up marginally to A\$178.9/sh (from A\$178.4/sh).

We continue to rate RIO at Neutral based on:

## 1. Attractive FCF and relative valuation, but prefer BHP on near term

outlook/catalysts: RIO is trading at \~0.85x NAV (\~A\$196/sh) vs. peers (BHP \~0.9x NAV and FMG \~1x NAV), and RIO.AX is trading at \~7x NTM EBITDA, in-line with BHP.AX on \~7x, and the 25-yr historical average of 6.5-7x, but still below pure play base metal companies. Additionally, FCF/dividend looks attractive at \~5% in 2026E (\~6% at spot), driven by our bullish view on aluminium and copper (\~45-50% of group EBITDA in 2026E, and \~60% by 2030E). However, we still prefer Buy-rated BHP on near term outlook/catalysts: Although valuations are comparable, with both stocks trading on \~7x EBITDA and \~0.9xNAV, and NTM EBITDA estimates are higher at spot commodity prices, we think BHP has more positive momentum near term with higher exposure to copper vs. RIO on an EBITDA basis (\~50% vs. \~35%) and a stronger balance sheet (US\$8.5bn net debt vs. RIO at \~US\$14.8bn end of June 26). We think BHP's final dividend payout could be 60-65% with the FY26 results, and continue to think BHP can maintain a 60% dividend payout through the forecast dip in Cu Eq production in FY27.

2. Compelling simplification strategy and medium term CuEq and EBITDA growth: RIO maintains sector leading production and EBITDA growth over the medium term and should benefit from rising aluminium prices following major supply disruption from the Middle East. The company's compelling strategy remains unchanged, anchored on the 'stronger, sharper, simpler' agenda presented at the recent capital markets day, which includes US\$5-10bn (vs GSe \~US\$10bn) of non-core divestments and cost out. We forecast RIO's Cu Eq production to grow by \~10% and EBITDA by \~30% from 2025 to 2030, driven mostly by the ramp-up of the Oyu Tolgoi UG copper mine, higher grades at Bingham Canyon copper from 2027, the ramp-up of the Simandou iron ore mine in Guinea, higher Pilbara Fe shipments with the ramp-up of new mines, growth in lithium in Argentina, and a rebound in aluminium production. However, we forecast Cu Eq production growth of just \~1% p.a. over the next two years, and growth is mostly weighted to 2028-2030E. Longer dated growth projects include Resolution & La Granja copper and lithium options.

3. Pilbara turnaround (\~50% of group NAV) on track: we see potential for FCF/t improvement in the Pilbara by 2028-2030 with the 5 replacement mines, and over the long run driven by Rhodes Ridge (first production expected \~2030-31). RIO's 2023 Pilbara visit outlined medium-term shipments guidance of 345-360Mtpa by 2028 (GSe \~340Mtpa by 2028 and \~350Mtpa by 2031 with Rhodes Ridge).

4. Compelling high margin aluminium exposure: Rio has the world's highest margin low emission aluminium business, with over 2.2Mt of Ali production powered by hydro. A +10% move in the aluminium price would result in a \~US\$1.1bn or \~4% increase to NTM EBITDA.

Exhibit 1: RIO operating and financial summary

<table><tr><td>RIO 12m PT</td><td>US$/sh</td><td>A$/sh</td></tr><tr><td>NAV</td><td>137.3</td><td>196.1</td></tr><tr><td>NTM EV/EBITDA</td><td>113.1</td><td>161.6</td></tr><tr><td>Price Target (RIO.AX)</td><td></td><td>178.9</td></tr><tr><td>Current Share Price</td><td>-</td><td>165.5</td></tr><tr><td>Upside / (Downside)</td><td>%</td><td>8%</td></tr></table>

<table><tr><td colspan="2">Commodity and FX assumptions</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>AUD:USD</td><td>x</td><td>0.66</td><td>0.64</td><td>0.69</td><td>0.68</td><td>0.69</td><td>0.69</td><td>0.70</td></tr><tr><td>CAD:USD</td><td>x</td><td>0.73</td><td>0.72</td><td>0.72</td><td>0.72</td><td>0.73</td><td>0.75</td><td>0.76</td></tr><tr><td>Iron ore fines (CFR, 62% Fe)</td><td>US$/t</td><td>110</td><td>102</td><td>101</td><td>96</td><td>97</td><td>98</td><td>99</td></tr><tr><td>Iron ore lump (CFR, 63.5% Fe)</td><td>US$/t</td><td>120</td><td>109</td><td>108</td><td>107</td><td>109</td><td>110</td><td>112</td></tr><tr><td>Bauxite</td><td>US$/t</td><td>64</td><td>79</td><td>67</td><td>70</td><td>70</td><td>70</td><td>70</td></tr><tr><td>Alumina</td><td>US$/t</td><td>502</td><td>386</td><td>318</td><td>355</td><td>370</td><td>380</td><td>406</td></tr><tr><td>Aluminium</td><td>USc/lb</td><td>110</td><td>119</td><td>145</td><td>122</td><td>129</td><td>136</td><td>142</td></tr><tr><td>Copper</td><td>USc/lb</td><td>415</td><td>451</td><td>606</td><td>626</td><td>621</td><td>612</td><td>605</td></tr><tr><td>Lithium carbonate</td><td>US$/t</td><td>11,167</td><td>9,319</td><td>21,022</td><td>16,875</td><td>15,375</td><td>16,762</td><td>18,548</td></tr><tr><td colspan="9">Operating assumptions</td></tr><tr><td colspan="9">Production</td></tr><tr><td>Iron ore - Pilbara Prod (RIO share)</td><td>Mt</td><td>278</td><td>280</td><td>284</td><td>289</td><td>292</td><td>291</td><td>287</td></tr><tr><td>Iron ore - Pilbara Sales (RIO share)</td><td>Mt</td><td>277</td><td>279</td><td>281</td><td>289</td><td>292</td><td>291</td><td>287</td></tr><tr><td>Iron ore - Pilbara Prod (100%)</td><td>Mt</td><td>328</td><td>327</td><td>333</td><td>337</td><td>342</td><td>341</td><td>343</td></tr><tr><td>Iron ore - Pilbara Sales (100%)</td><td>Mt</td><td>329</td><td>326</td><td>330</td><td>337</td><td>342</td><td>341</td><td>343</td></tr><tr><td>Guidance</td><td>Mt</td><td></td><td></td><td>323-338</td><td></td><td>Med term ~345-360</td><td></td><td></td></tr><tr><td>IOC Canada</td><td>Mt</td><td>9.4</td><td>9.3</td><td>8.7</td><td>9.3</td><td>9.4</td><td>9.4</td><td>9.4</td></tr><tr><td>Guidance</td><td></td><td></td><td></td><td>8.9-10.6</td><td></td><td></td><td></td><td></td></tr><tr><td>Simandou Prod (RIO share)</td><td>Mt</td><td></td><td>1</td><td>4</td><td>13</td><td>22</td><td>27</td><td>27</td></tr><tr><td>Simandou Prod (100%)</td><td>Mt</td><td></td><td>2</td><td>8</td><td>29</td><td>48</td><td>60</td><td>60</td></tr><tr><td>Simandou Sales (100%)</td><td></td><td></td><td>0</td><td>6</td><td>28</td><td>48</td><td>60</td><td>60</td></tr><tr><td>Copper - Mined (consolidated)</td><td>kt</td><td>697</td><td>883</td><td>864</td><td>895</td><td>989</td><td>1,024</td><td>1,016</td></tr><tr><td>Guidance</td><td></td><td></td><td></td><td>800-870</td><td></td><td></td><td></td><td></td></tr><tr><td>Copper - Mined (equity)</td><td>kt</td><td>624</td><td>766</td><td>726</td><td>748</td><td>813</td><td>832</td><td>826</td></tr><tr><td>Copper - Refined (consolidated)</td><td>kt</td><td>248</td><td>190</td><td>171</td><td>222</td><td>239</td><td>239</td><td>241</td></tr><tr><td>Guidance</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gold (mined)</td><td>koz</td><td>352</td><td>619</td><td>633</td><td>414</td><td>447</td><td>478</td><td>516</td></tr><tr><td>Bauxite</td><td>Mt</td><td>59</td><td>62</td><td>60</td><td>61</td><td>62</td><td>61</td><td>62</td></tr><tr><td>Guidance</td><td></td><td></td><td></td><td>58-61</td><td></td><td></td><td></td><td></td></tr><tr><td>Alumina</td><td>Mt</td><td>7.3</td><td>7.6</td><td>8.0</td><td>7.0</td><td>7.1</td><td>7.1</td><td>7.1</td></tr><tr><td>Guidance</td><td></td><td></td><td></td><td>7.6-8.0</td><td></td><td></td><td></td><td></td></tr><tr><td>Aluminium (excludes recycling)</td><td>Mt</td><td>3.3</td><td>3.4</td><td>3.4</td><td>3.5</td><td>3.5</td><td>3.5</td><td>3.5</td></tr><tr><td>Guidance</td><td></td><td></td><td></td><td>3.25-3.45</td><td></td><td></td><td></td><td></td></tr><tr><td>TiO2 slag</td><td>Mt</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.2</td><td>1.2</td><td>1.2</td><td>1.1</td></tr><tr><td>Guidance</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Lithium carbonate (RIO share)</td><td>kt (LCE)</td><td></td><td>56</td><td>61</td><td>88</td><td>120</td><td>150</td><td>172</td></tr><tr><td>Lithium carbonate (100%)</td><td>kt (LCE)</td><td></td><td>70</td><td>76</td><td>98</td><td>131</td><td>162</td><td>184</td></tr><tr><td></td><td></td><td></td><td></td><td>61-64</td><td></td><td></td><td></td><td></td></tr><tr><td>CuEq Prod. (GS LR prices)</td><td>Mt</td><td>4.51</td><td>4.94</td><td>4.98</td><td>5.09</td><td>5.34</td><td>5.46</td><td>5.47</td></tr><tr><td>CuEq YoY %</td><td>%</td><td>2.9%</td><td>9.7%</td><td>0.8%</td><td>2.1%</td><td>5.1%</td><td>2.2%</td><td>0.2%</td></tr><tr><td colspan="9">Unit Costs</td></tr><tr><td>Pilbara Cash Costs (FOB)</td><td>US$/t</td><td>23.0</td><td>23.5</td><td>25.6</td><td>25.1</td><td>24.6</td><td>24.9</td><td>24.1</td></tr><tr><td>Guidance</td><td></td><td></td><td></td><td>23.5-25.0</td><td></td><td>Med term ~20 (real $)</td><td></td><td></td></tr><tr><td>Aluminium</td><td>USc/lb</td><td>98</td><td>124</td><td>126</td><td>129</td><td>134</td><td>140</td><td>127</td></tr><tr><td>Alumina</td><td>US$/t</td><td>385</td><td>385</td><td>358</td><td>356</td><td>363</td><td>370</td><td>378</td></tr><tr><td>Bauxite (FOB)</td><td>US$/t</td><td>19</td><td>20</td><td>25</td><td>25</td><td>26</td><td>27</td><td>28</td></tr><tr><td>Copper</td><td>USc/lb</td><td>151</td><td>96</td><td>34</td><td>102</td><td>92</td><td>90</td><td>89</td></tr><tr><td>Guidance</td><td></td><td></td><td></td><td>30-50</td><td></td><td></td><td></td><td></td></tr><tr><td>Financial summary</td><td>Units</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenue</td><td>US$bn</td><td>53.7</td><td>57.6</td><td>60.4</td><td>60.1</td><td>64.2</td><td>66.9</td><td>67.2</td></tr><tr><td>Underlying EBITDA</td><td>US$bn</td><td>23.3<

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
