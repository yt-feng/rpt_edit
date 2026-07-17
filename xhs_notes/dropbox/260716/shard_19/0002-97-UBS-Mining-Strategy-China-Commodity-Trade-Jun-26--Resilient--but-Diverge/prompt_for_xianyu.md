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
# Mining Strategy China Commodity Trade Jun-26: Resilient, but Divergent outlook

## China June-26 commodities maintain momentum

China's June preliminary trade data continues to show resilient physical flows, but increasingly mixed fundamental signals. Bulk commodities remain weighed down by soft demand and rising supply, while copper and aluminium continue to benefit from structural demand and tighter supply conditions, albeit aluminium fundamentals are seen easing from here.

## Highlights: Iron Ore and Industrial Metals maintain strong momentum

Iron Ore imports rose to 112.6Mt (+6% y/y, +15% m/m, +6% YTD), reversing a weak May and returning to late-2025 levels (\~110-120Mt/mth). Annualised imports are running at \~1.35 Btpa, consistent with strong 2026 supply from Australia, Brazil, early Simandou ramp-up & Fe grade degradation (eg: BHP, RIO and FMG reducing Fe spec). However, the signals on demand remain muted. China net steel exports are -5% YTD, iron ore port stocks elevated at \~158.5Mt (but below all-time highs \~167Mt in March), and export shipments have continued to lift. This divergence suggests imports are being driven by plentiful supply and inventory dynamics and perhaps less so end demand. Even with spot at \~US\$98/t and inside cost support (95th percentile \~US\$99-101/t), we anticipate iron ore to drift lower towards \~US\$92/t through 2026/27/28 as supply growth (eg: Simandou) outpaces demand.

Copper concentrate imports were broadly flat (2.33Mt; -1% YTD), reflecting tight upstream supply (low TC/RCs) amidst continued competition for feedstock. Refined imports rose 5% m/m but remain -5% YTD. The shortage of concentrate (eg: Grasberg, Cobre Panama outages and generally muted Chile and Peru production trends) may see increased imports of refined to meet demand, which remains structurally strong (electrification/AIDC). The result of strong underlying demand and constrained supply is deficits likely over the next 1-3 years, anchoring prices around \~US\$6-6.50/lb.

Aluminium exports rose to 0.71Mt (+45% y/y, +12% m/m, +16% YTD) and running at \~8.5Mt annualised with strength reflecting robust demand ex-China given 2.5-3Mt of downstream supply offline (Middle East, Mozal). This is consistent with our near-term view, with the market in deficit in 2026 amid lingering Middle East disruptions. However, while prices remain supported by cost inflation, low visible inventories and the copper–aluminium substitution dynamic (Cu:Al ratio >4x), we see tightness easing over the next 6-12 months as \~3Mt of Middle East supply restarts and Indonesian capacity accelerates (driving \~5%/3% global supply growth in 2026/27 vs \~2.5–3% demand). Therefore, recent Chinese metal export strength likely reverses as markets normalise. We expect the market to rebalance into 2027-28 rather than move into surplus, with prices ultimately rebasing above the cost curve, albeit with less upside than implied by current tight conditions.

Steel exports reached 10.3Mt in June (+7% y/y, flat m/m), with net exports at 9.9Mt (+7% y/y, -5% YTD, 118Mtpa annualised). Volumes have recovered materially from the Jan/Feb trough (\~7.4Mt/month) following export licence tightening, but remain below late-2025 peaks (\~10.5-11.3Mt/month). Export arbitrage remains open and mills remain profitable, limiting downside to production despite weaker domestic demand. Imports remain negligible (\~0.4Mt; -11% YTD), reinforcing China's structural export surplus.

## Equities

Global
Basic Materials

Lachlan Shaw
Analyst
lachlan.shaw@ubs.com
+61-3-9242 6387

Annie Zhou
Associate Analyst
annie.zhou@ubs.com
+61-2-9324 2000

Dim Ariyasinghe
Analyst
dim.ariyasinghe@ubs.com
+61-3-9242 6385

Fintan Collins
Associate Analyst
fintan.collins@ubs.com
+61-3-9242 6179

Levi Spry
Analyst
levi.spry@ubs.com
+61-3-9242 6709

Al Harvey
Analyst
al.harvey@ubs.com
+61-3-9242 6071

Ben Wood
Analyst
ben.wood@ubs.com
+61-39-242 6709

Thomas Nightingale
Associate Analyst
thomas.nightingale@ubs.com
+61-3-9242 6176

Myles Allsop
Analyst
myles.allsop@ubs.com
+44-20-7568 1693

Sharon Ding
Analyst
sharon.ding@ubs.com
+852-2971 6284

Daniel Major
Analyst
daniel.major@ubs.com
+44-20-7568 3472

Coal imports rose to 42.8Mt (+30% y/y, +29% m/m; +2% YTD), rebounding sharply from a weak April/May period. Increased coal import demand likely reflects a combination of i) domestic supply disruptions (Shanxi mine explosion), ii) strong seasonal power demand growth, iii) focus on thermal coal strategic stockpiles, & iv) possible gas to coal switching.

Rare Earths exports declined to 5.1kt in June (-34% y/y, -7% m/m;,-6% YTD), extending the recent downtrend after a strong 2025. The weakness is largely policy-driven rather than demand-led, with tighter controls on the production and export of strategic materials weighing on outbound volumes. This reinforces the view that rare earth trade flows are increasingly decoupled from market fundamentals, with geopolitics and export regulation the dominant drivers.

## Equities: Copper constrained, Iron ore resilient, Aluminium easing

In Australian Miners, we see balanced risk/reward on BHP & RIO and are Neutral each, with BHP preferred. Resilient Chinese iron ore imports, as well as cost curve support; and lithium volume & price leverage, also has us Buy rated MIN. In Copper, we are Buy rated CSC and Neutral rated SFR.

## CHINA KEY TRADE FLOWS

Figure 1: China Key Trade Flows

<table><tr><td colspan="2"></td><td>Jul-24</td><td>Aug-24</td><td>Sep-24</td><td>Oct-24</td><td>Nov-24</td><td>Dec-24</td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>%y/y</td><td>%m/m</td><td>%YTD</td></tr><tr><td>Iron Ore Imports</td><td>Mt</td><td>102.6</td><td>101.3</td><td>103.9</td><td>103.7</td><td>101.7</td><td>112.4</td><td>97.2</td><td>93.8</td><td>93.8</td><td>103.6</td><td>97.2</td><td>105.8</td><td>105.2</td><td>105.0</td><td>116.1</td><td>111.2</td><td>110.3</td><td>119.5</td><td>112.4</td><td>97.6</td><td>104.7</td><td>103.8</td><td>97.7</td><td>112.6</td><td>6%</td><td>15%</td><td>6%</td></tr><tr><td>Annualised Iron Ore Imports</td><td>Mt</td><td>1232</td><td>1215</td><td>1247</td><td>1244</td><td>1220</td><td>1349</td><td>1166</td><td>1126</td><td>1125</td><td>1244</td><td>1167</td><td>1269</td><td>1262</td><td>1261</td><td>1393</td><td>1334</td><td>1324</td><td>1434</td><td>1349</td><td>1172</td><td>1257</td><td>1246</td><td>1172</td><td>1351</td><td></td><td></td><td></td></tr><tr><td>Steel Exports</td><td>Mt</td><td>7.8</td><td>9.4</td><td>10.1</td><td>11.2</td><td>9.3</td><td>9.7</td><td>8.9</td><td>8.0</td><td>10.5</td><td>10.5</td><td>10.6</td><td>9.7</td><td>9.8</td><td>9.5</td><td>10.5</td><td>9.8</td><td>10.0</td><td>11.3</td><td>7.8</td><td>7.8</td><td>9.1</td><td>9.5</td><td>10.3</td><td>10.3</td><td>7%</td><td>0%</td><td>-6%</td></tr><tr><td>Annualised Steel Exports</td><td>Mt</td><td>93</td><td>113</td><td>121</td><td>134</td><td>111</td><td>117</td><td>107</td><td>96</td><td>125</td><td>126</td><td>127</td><td>116</td><td>118</td><td>114</td><td>126</td><td>117</td><td>120</td><td>136</td><td>93</td><td>94</td><td>110</td><td>114</td><td>124</td><td>124</td><td></td><td></td><td></td></tr><tr><td>Steel Imports</td><td>Mt</td><td>0.5</td><td>0.5</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.6</td><td>0.5</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.4</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.4</td><td>-6%</td><td>-1%</td><td>-11%</td></tr><tr><td>Annualised Steel Imports</td><td>Mt</td><td>6.1</td><td>6.1</td><td>6.6</td><td>6.4</td><td>5.7</td><td>7.5</td><td>6.0</td><td>6.7</td><td>6.0</td><td>6.2</td><td>5.9</td><td>5.7</td><td>5.2</td><td>6.0</td><td>6.7</td><td>6.1</td><td>6.0</td><td>6.2</td><td>5.5</td><td>4.4</td><td>6.1</td><td>5.5</td><td>5.4</td><td>5.4</td><td></td><td></td><td></td></tr><tr><td>Net Steel Exports</td><td>Mt</td><td>7.3</td><td>8.9</td><td>9.5</td><td>10.6</td><td>8.8</td><td>9.1</td><td>8.4</td><td>7.5</td><td>10.0</td><td>9.9</td><td>10.1</td><td>9.2</td><td>9.4</td><td>9.0</td><td>9.9</td><td>9.3</td><td>9.5</td><td>10.8</td><td>7.3</td><td>7.5</td><td>8.6</td><td>9.0</td><td>9.9</td><td>9.9</td><td>7%</td><td>0%</td><td>-5%</td></tr><tr><td>Annualised Net Steel Exports</td><td>Mt</td><td>87</td><td>107</td><td>115</td><td>127</td><td>106</td><td>109</td><td>101</td><td>90</td><td>119</td><td>119</td><td>121</td><td>110</td><td>113</td><td>108</td><td>119</td><td>111</td><td>114</td><td>129</td><td>87</td><td>90</td><td>103</td><td>108</td><td>119</td><td>118</td><td></td><td></td><td></td></tr><tr><td colspan="29"></td></tr><tr><td>Coal Imports</td><td>Mt</td><td>46.2</td><td>45.8</td><td>47.6</td><td>46.2</td><td>55.0</td><td>52.3</td><td>41.8</td><td>34.3</td><td>38.7</td><td>37.8</td><td>36.0</td><td>33.0</td><td>35.7</td><td>42.6</td><td>45.9</td><td>41.7</td><td>44.1</td><td>58.6</td><td>46.3</td><td>30.9</td><td>39.1</td><td>33.1</td><td>33.3</td><td>42.8</td><td>30%</td><td>29%</td><td>2%</td></tr><tr><td>Annualised Coal Imports</td><td>Mt</td><td>555</td><td>550</td><td>571</td><td>554</td><td>660</td><td>628</td><td>501</td><td>412</td><td>465</td><td>454</td><td>432</td><td>396</td><td>428</td><td>512</td><td>551</td><td>501</td><td>529</td><td>703</td><td>555</td><td>371</td><td>469</td><td>397</td><td>399</td><td>513</td><td></td><td></td><td></td></tr><tr><td colspan="29"></td></tr><tr><td>Copper Concentrate Imports</td><td>Mt</td><td>2.16</td><td>2.57</td><td>2.43</td><td>2.31</td><td>2.23</td><td>2.52</td><td>2.53</td><td>2.17</td><td>2.39</td><td>2.94</td><td>2.37</td><td>2.33</td><td>2.58</td><td>2.74</td><td>2.58</td><td>2.45</td><td>2.52</td><td>2.70</td><td>2.62</td><td>2.31</td><td>2.63</td><td>2.35</td><td>2.37</td><td>2.33</td><td>0%</td><td>-1%</td><td>-1%</td></tr><tr><td>Annualised Copper Concentrate Imports</td><td>Mt</td><td>25.9</td><td>30.8</td><td>29.2</td><td>27.7</td><td>26.8</td><td>30.2</td><td>30.4</td><td>26.1</td><td>28.7</td><td>35.3</td><td>28.4</td><td>28.0</td><td>30.9</td><td>32.9</td><td>31.0</td><td>29.4</td><td>30.3</td><td>32.4</td><td>31.4</td><td>27.8</td><td>31.5</td><td>28.2</td><td>28.4</td><td>28.0</td><td></td><td></td><td></td></tr><tr><td>Copper Metal Imports</td><td>Kt</td><td>437</td><td>414</td><td>479</td><td>506</td><td>528</td><td>559</td><td>420</td><td>414</td><td>469</td><td>439</td><td>423</td><td>464</td><td>484</td><td>423</td><td>483</td><td>437</td><td>424</td><td>440</td><td>380</td><td>320</td><td>415</td><td>455</td><td>443</td><td>478</td><td>3%</td><td>8%</td><td>-5%</td></tr><tr><td>Annualised Copper Metal Imports</td><td>Kt</td><td>5244</td><td>4968</td><td>5747</td><td>6073</td><td>6336</td><td>6708</td><td>5040</td><td>4968</td><td>5628</td><td>5268</td><td>5076</td><td>5572</td><td>5804</td><td>5076</td><td>5791</td><td>5249</td><td>5088</td><td>5280</td><td>4560</td><td>3840</td><td>4980</td><td>5460</td><td>5314</td><td>5739</td><td></td><td></td><td></td></tr><tr><td colspan="29"></td></tr><tr><td>Aluminium Exports</td><td>Mt</td><td>0.59</td><td>0.59</td><td>0.56</td><td>0.58</td><td>0.67</td><td>0.51</td><td>0.49</td><td>0.37</td><td>0.51</td><td>0.52</td><td>0.55</td><td>0.49</td><td>0.54</td><td>0.53</td><td>0.52</td><td>0.50</td><td>0.57</td><td>0.54</td><td>0.54</td><td>0.43</td><td>0.49</td><td>0.59</td><td>0.64</td><td>0.71</td><td>45%</td><td>12%</td><td>16%</td></tr><tr><td>Annualised Aluminium Exports</td><td>Mt</td><td>7.03</td><td>7.13</td><td>6.74</td><td>6.92</td><td>8.03</td><td>6.07</td><td>5.88</td><td>4.45</td><td>6.07</td><td>6.19</td><td>6.59</td><td>5.87</td><td>6.49</td><td>6.41</td><td>6.24</td><td>6.04</td><td>6.83</td><td>6.49</td><td>6.48</td><td>5.17</td><td>5.82</td><td>7.13</td><td>7.63</td><td>8.53</td><td></td><td></td><td></td></tr><tr><td colspan="29"></td></tr><tr><td>Crude Oil Imports</td><td>Mt</td><td>42.3</td><td>49.1</td><td>45.5</td><td>44.7</td><td>48.5</td><td>47.7</td><td>41.2</td><td>42.6</td><td>51.1</td><td>48.2</td><td>46.4</td><td>49.9</td><td>47.2</td><td>49.5</td><td>46.9</td><td>48.0</td><td>50.9</td><td>55.9</td><td>48.9</td><td>48.0</td><td>49.9</td><td>38.5</td><td>33.1</td><td>29.2</td><td>-41%</td><td>-12%</td><td>-11%</td></tr><tr><td>Annualised Crude Oil Imports</td><td>Mt</td><td>508</td><td>589</td><td>546</td><td>536</td><td>582</td><td>572</td><td>494</td><td>511</td><td>614</td><td>578</td><td>557</td><td>599</td><td>567</td><td>594</td><td>563</td><td>576</td><td>610</td><td>670</td><td>587</td><td>577</td><td>599</td><td>461</td><td>397</td><td>351</td><td></td><td></td><td></td></tr><tr><td colspan="29"></td></tr><tr><td>Rare Earths Exports</td><td>Kmt</td><td>4.9</td><td>4.7</td><td>4.2</td><td>4.8</td><td>4.4</td><td>3.3</td><td>5.3</td><td>3.2</td><td>5.7</td><td>4.8</td><td>5.9</td><td>7.7</td><td>6.0</td><td>5.8</td><td>4.0</td><td>4.3</td><td>5.5</td><td>4.4</td><td>6.1</td><td>4.4</td><td>4.1</td><td>5.3</td><td>5.5</td><td>5.1</td><td>-34%</td><td>-7%</td><td>-6%</td></tr><tr><td>Annualised Rare Earths Exports</td><td>Kmt</td><td>59</td><td>57</td><td>50</td><td>57</td><td>53</td><td>40</td><td>63</td><td>39</td><td>68</td><td>57</td><td>70</td><td>93</td><td>72</td><td>69</td><td>48</td><td>52</td><td>66</td><td>53</td><td>73</td><td>53</td><td>49</td><td>64</td><td>66</td><td>61</td><td></td><td></td><td></td></tr></table>

Source: Haver, Bloomberg, UBS

## CHINA TRADE SIGNALS

Figure 2: Iron Ore Imports - mthly and ann'd  
![](images/eb3b5ff1661ff2d29a55e0f7207a281de7b845a36d89bf1c4b97c59871ced5cf.jpg)  
Source: Haver/UBS

Figure 3: Iron Ore Imports - %3m/3m and %y/y  
![](images/31c5398550ba3ef962043b2e218bd8a90b2a792c9b5abbcfeac5c46b8594cfce.jpg)  
Source: Haver/UBS

Figure 4: Copper Concentrate Imports - mthly and ann'd  
![](images/7ef7976eaaf535e3365cee4b65af45e1aded4cae8e927e6548e457f0a2a2fb4a.jpg)  
Source: Haver/UBS

Figure 5: Copper Concentrate Imports - %3m/3m and %y/y  
![](images/9b752d21702835cc54a747f703a6edfa3a4a628945103eedf758045fe9465e46.jpg)  
Source: Haver/UBS

Figure 6: Copper Metal Imports - mthly and ann'd  
![](images/fc7df3b5bffb178bfe4f739daaed208a696d0d463987c58e8d796962d8c6df71.jpg)  
Source: Haver/UBS

Figure 7: Copper Metal Imports - %3m/3m and %y/y  
![](images/bddb3004144d4a9813e6174180296ea0ecb6bb81b1c7a79d736657ab2deae4a0.jpg)  
Source: Haver/UBS

Figure 8: Aluminium Exports - mthly and ann'd  
![](images/71d29509a0205687de25e9f554245b82293f9f3a13c6bf30316810c1eab9f103.jpg)  
Source: Haver/UBS

Figure 9: Aluminium Exports - %3m/3m and %y/y  
![](images/e8866e7d5c1224d07e28ea2b511f4c22073a94a84ace7dac638f905dce59f49c.jpg)  
Source: Haver/UBS

Figure 10: Net Steel Exports - mthly & ann'd  
![](images/ee091596cc0428a1edbabd729b045cb70c232978cc9a2648ad2edbc596db39bc.jpg)  
Source: Haver/UBS

Figure 11: Net Steel Exports - %3m/3m and %y/y  
![](images/b4da10ce950aa0fd79828dd1dbf14be47c844ca79926ad96aff5c5a081a122b2.jpg)  
Source: Haver/UBS

Figure 12: Coal Imports - mthly and ann'd  
![](images/f98dbc37cc621f8bc4e10c19caf62b8ed76d37e29e6f68b92604d6923b157bb6.jpg)  
Source: Haver/UBS

Figure 13: Coal Imports - %3m/3m and %y/y  
![](images/c577285f552383e513b39acb1e372b4c89d38b047a1ec31e60d8d1ea55b604ee.jpg)  
Source: Haver/UBS

Figure 14: Rare Earth Exports - mthly and ann'd  
![](images/17bb41bbdad8a3a44d570fbd90d1050dbf5c075ee1de8e533e419c759d53bb06.jpg)  
Source: Haver/UBS

Figure 15: Rare Earth Exports - %3m/3m and %y/y  
![](images/d71631f47e54ab797338dc3ae877e8aa115645bc49ac3a750a15675b9bc706a9.jpg)  
Source: Haver/U

[中间内容因长度限制已省略]

 not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/22ad2b5ee2284a77c4790d38c25f6f7f275388a6dd27ad2acd64472b3e94397f.jpg)
"""
