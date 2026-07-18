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
HSBC (0005.HK/HSBA.L)

# 2Q26 Preview: Another robust quarter, with focus on NII guidance and wealth trends

HSBC will report 2Q26 results on 4th August; we expect the bank to deliver underlying PBT of US\$10.2bn,+25% yoy /+2% qoq (4% ahead of Visible Alpha Consensus Data). Quarterly growth is supported by a lower cost of credit of 40bps as we do not anticipate further overlays related to the Middle East conflict, while 1Q's elevated provisioning was also impacted by a large one-off credit-related charge. Banking NII should also increase 3% qoq, supported by slightly higher HIBOR. Offsetting this, we expect some moderation in non-banking NII following seasonally stronger 1Q trends. Beyond the quarter, investor focus is likely to remain on wealth management, particularly any updates on Chinese cross-border regulations and the potential implications for wealth inflows, the broader wealth outlook, and whether the higher rate environment drives an upward revision to NII guidance.

## Key call-outs for the quarter:

■ Banking NII in focus. We expect Banking NII to increase 3% qoq, supported by uptick in HIBOR throughout the quarter (+6bps qoq), a higher day count and continued balance sheet growth. The outlook has also become more constructive, with HIBOR rising more meaningfully towards the end of the quarter, suggesting a larger benefit in 3Q26. In addition, the higher-for-longer rate environment and steeper yield curve should remain supportive through structural hedge reinvestment and balance sheet repricing. Given the higher rate environment and the anticipation of higher for longer rates, we revise our NII forecast by +0.4%/+2%/+2% for 2026-2028E and are now 3% above VA consensus for banking NII. We expect key focus on the 2026 Banking NII guidance and potential upgrades given the stronger interest rate outlook and improving HIBOR backdrop.

Non-interest income is expected to remain resilient, with underlying non-banking NII of US\$7.4bn (+6% yoy / -7% qoq in 1Q26), 3% ahead of VA consensus. We anticipate some moderation following seasonally stronger 1Q trends and a normalisation in transaction banking fees from elevated levels in 1Q. Looking ahead, investor focus will likely remain on wealth management, particularly any updates on Chinese cross-border regulations and their implications for wealth inflows, growth momentum and the broader wealth outlook. We note that 1Q26 included \$39bn in Wealth net new money (of which

Melissa Kuang, CFA
+65-6889-2869 |
melissa.kuang@gs.com
GS (Singapore) Pte

Chris Hallam  
+44(20)7552-2958 |  
chris.hallam@gs.com  
GS International

Benjamin Caven-Roberts
+44(20)7552-7066 | benjamin.d.caven-roberts@gs.com
GS International

Sachin Nayar  
+44(20)7051-2598 |  
sachin.x.nayar@gs.com  
GS International

Wayne Wang  
+65-6889-2866 |  
wayne.q.wang@gs.com  
GS (Singapore) Pte

$34bn in Asia$ , well ahead of the prior quarter and prior year ( $26bn in 4Q25 and$ 23bn in 1Q25) — as a result, although we see solid core trends continuing, we see potential for a sequential slowdown in Q2, simply reflecting the high comp.

Credit costs should decline, with our forecast at 40bps versus 52bps in 1Q26. We do not anticipate any further overlays related to the Iran conflict, while 1Q's elevated provisioning was also impacted by a large one-off credit charge that is unlikely to recur. As a result, we expect credit costs to normalise in 2Q26.

■ Capital and shareholder returns will be another key focus. We expect HSBC to resume share buybacks this quarter following a three-quarter pause related to the HSB acquisition, as previously indicated by management. We model US\$1.5bn of share repurchases being announced with 2Q26, which should still leave the bank with a strong CET1 ratio of c.14.0% after accruals.

We raise our EPS estimates by up to 1.6% for FY26–29E, primarily reflecting a more supportive interest rate outlook, partly offset by higher opex as we anticipate increased investment in growth initiatives and technology to support revenue expansion. As a result, we raise our 12-month two-stage DDM TP for 0005.HK to HK\$181 (from HK\$165) and our TP for HSBC.L to 1,725p (from 1,700p). We maintain Buy ratings on 0005.HK and HSBC.L (on EMEA CL).

Exhibit 1: Our underlying PBT are up to 5% ahead of visible alpha consensus for 2026-2028E and 4% ahead for 2Q26E

<table><tr><td rowspan="2">HSBC</td><td colspan="4">2Q26E</td><td colspan="4">2026E</td><td colspan="4">2027E</td><td colspan="4">2028E</td></tr><tr><td>GS</td><td>VA</td><td>%</td><td>mn</td><td>GS</td><td>VA</td><td>%</td><td>mn</td><td>GS</td><td>VA</td><td>%</td><td>mn</td><td>GS</td><td>VA</td><td>%</td><td>mn</td></tr><tr><td>Banking NII</td><td>11,541</td><td>11,486</td><td>0%</td><td>55</td><td>46,769</td><td>46,424</td><td>1%</td><td>345</td><td>49,546</td><td>48,121</td><td>3%</td><td>1,425</td><td>50,996</td><td>49,740</td><td>3%</td><td>1,256</td></tr><tr><td>Fees and Other Income</td><td>7,357</td><td>7,165</td><td>3%</td><td>192</td><td>28,715</td><td>28,501</td><td>1%</td><td>214</td><td>30,737</td><td>30,188</td><td>2%</td><td>550</td><td>32,704</td><td>32,463</td><td>1%</td><td>241</td></tr><tr><td>Underlying Revenues</td><td>18,898</td><td>18,651</td><td>1%</td><td>247</td><td>75,483</td><td>74,925</td><td>1%</td><td>559</td><td>80,283</td><td>78,309</td><td>3%</td><td>1,975</td><td>83,700</td><td>82,203</td><td>2%</td><td>1,497</td></tr><tr><td>Significant Revenue Adjustments</td><td>0</td><td>-50</td><td>-100%</td><td>50</td><td>-501</td><td>-880</td><td>-43%</td><td>379</td><td>0</td><td>-85</td><td>-100%</td><td>85</td><td>0</td><td>-245</td><td>-100%</td><td>245</td></tr><tr><td>Total Revenues</td><td>18,898</td><td>18,601</td><td>2%</td><td>297</td><td>74,982</td><td>74,045</td><td>1%</td><td>938</td><td>80,283</td><td>78,224</td><td>3%</td><td>2,060</td><td>83,700</td><td>81,958</td><td>2%</td><td>1,742</td></tr><tr><td>Underlying Operating Expenses</td><td>-8,337</td><td>-8,444</td><td>-1%</td><td>107</td><td>-34,359</td><td>-34,344</td><td>0%</td><td>-15</td><td>-35,536</td><td>-35,294</td><td>1%</td><td>-242</td><td>-36,753</td><td>-36,292</td><td>1%</td><td>-461</td></tr><tr><td>Significant Cost Adjustments</td><td>-343</td><td>-239</td><td>44%</td><td>-104</td><td>-1,200</td><td>-1,032</td><td>16%</td><td>-168</td><td>-200</td><td>-751</td><td>-73%</td><td>551</td><td>-200</td><td>-800</td><td>-75%</td><td>600</td></tr><tr><td>Total Operating Expenses</td><td>-8,680</td><td>-8,682</td><td>0%</td><td>3</td><td>-35,559</td><td>-35,377</td><td>1%</td><td>-182</td><td>-35,736</td><td>-36,045</td><td>-1%</td><td>309</td><td>-36,953</td><td>-37,093</td><td>0%</td><td>140</td></tr><tr><td>Credit Costs</td><td>-1,005</td><td>-1,049</td><td>-4%</td><td>44</td><td>-4,261</td><td>-4,501</td><td>-5%</td><td>239</td><td>-3,747</td><td>-4,059</td><td>-8%</td><td>312</td><td>-3,682</td><td>-4,134</td><td>-11%</td><td>452</td></tr><tr><td>Operating Profit - Reported</td><td>9,213</td><td>8,870</td><td>4%</td><td>344</td><td>35,162</td><td>34,167</td><td>3%</td><td>995</td><td>40,801</td><td>38,120</td><td>7%</td><td>2,681</td><td>43,065</td><td>40,731</td><td>6%</td><td>2,333</td></tr><tr><td>Operating Profit - Underlying</td><td>9,556</td><td>9,158</td><td>4%</td><td>398</td><td>36,863</td><td>36,079</td><td>2%</td><td>784</td><td>41,001</td><td>38,956</td><td>5%</td><td>2,044</td><td>43,265</td><td>41,777</td><td>4%</td><td>1,488</td></tr><tr><td>P/L from Associates and JV</td><td>677</td><td>717</td><td>-6%</td><td>-41</td><td>2,815</td><td>2,528</td><td>11%</td><td>287</td><td>2,845</td><td>2,745</td><td>4%</td><td>100</td><td>2,902</td><td>2,742</td><td>6%</td><td>160</td></tr><tr><td>PBT - Reported</td><td>9,890</td><td>9,587</td><td>3%</td><td>303</td><td>37,977</td><td>36,695</td><td>3%</td><td>1,282</td><td>43,646</td><td>40,865</td><td>7%</td><td>2,781</td><td>45,967</td><td>43,473</td><td>6%</td><td>2,494</td></tr><tr><td>PBT - Underlying</td><td>10,233</td><td>9,876</td><td>4%</td><td>357</td><td>39,678</td><td>38,607</td><td>3%</td><td>1,071</td><td>43,846</td><td>41,702</td><td>5%</td><td>2,144</td><td>46,167</td><td>44,519</td><td>4%</td><td>1,648</td></tr><tr><td>Income Taxes</td><td>-2,241</td><td>-2,013</td><td>11%</td><td>-227</td><td>-8,462</td><td>-7,818</td><td>8%</td><td>-645</td><td>-9,889</td><td>-8,660</td><td>14%</td><td>-1,229</td><td>-10,415</td><td>-9,257</td><td>13%</td><td>-1,157</td></tr><tr><td>PAT - Reported</td><td>7,649</td><td>7,574</td><td>1%</td><td>76</td><td>29,515</td><td>28,877</td><td>2%</td><td>637</td><td>33,757</td><td>32,206</td><td>5%</td><td>1,551</td><td>35,552</td><td>34,216</td><td>4%</td><td>1,337</td></tr><tr><td>Minorities</td><td>-38</td><td>-31</td><td>21%</td><td>-7</td><td>-249</td><td>-145</td><td>71%</td><td>-104</td><td>-254</td><td>-125</td><td>103%</td><td>-129</td><td>-259</td><td>-115</td><td>125%</td><td>-144</td></tr><tr><td>Net Income - Reported</td><td>7,611</td><td>7,542</td><td>1%</td><td>69</td><td>29,266</td><td>28,732</td><td>2%</td><td>534</td><td>33,503</td><td>32,081</td><td>4%</td><td>1,422</td><td>35,293</td><td>34,101</td><td>3%</td><td>1,193</td></tr><tr><td>Preferred Stock</td><td>-155</td><td>-181</td><td>-14%</td><td>26</td><td>-1,198</td><td>-1,231</td><td>-3%</td><td>33</td><td>-1,198</td><td>-1,238</td><td>-3%</td><td>40</td><td>-1,198</td><td>-1,242</td><td>-4%</td><td>44</td></tr><tr><td>Ordinary Net Income - Reported</td><td>7,456</td><td>7,361</td><td>1%</td><td>95</td><td>28,068</td><td>27,501</td><td>2%</td><td>566</td><td>32,305</td><td>30,843</td><td>5%</td><td>1,462</td><td>34,095</td><td>32,859</td><td>4%</td><td>1,236</td></tr><tr><td colspan="17">Per Share Data</td></tr><tr><td>EPS - Basic</td><td>0.43</td><td>0.43</td><td>1%</td><td>0.01</td><td>1.64</td><td>1.63</td><td>0%</td><td>0.01</td><td>1.90</td><td>1.87</td><td>1%</td><td>0.02</td><td>2.03</td><td>2.05</td><td>-1%</td><td>-0.02</td></tr><tr><td>DPS - Declared</td><td>0.10</td><td>0.10</td><td>0%</td><td>0.00</td><td>0.84</td><td>0.82</td><td>2%</td><td>0.02</td><td>0.95</td><td>0.92</td><td>4%</td><td>0.03</td><td>1.02</td><td>1.00</td><td>2%</td><td>0.02</td></tr><tr><td colspan="17">Capital (bn)</td></tr><tr><td>CET1 Capital</td><td>126</td><td>127</td><td>-1%</td><td>-1</td><td>121</td><td>131</td><td>-8%</td><td>-10</td><td>129</td><td>137</td><td>-6%</td><td>-8</td><td>138</td><td>145</td><td>-5%</td><td>-7</td></tr><tr><td>RWAs</td><td>903</td><td>894</td><td>1%</td><td>9</td><td>921</td><td>911</td><td>1%</td><td>10</td><td>963</td><td>946</td><td>2%</td><td>18</td><td>1,004</td><td>984</td><td>2%</td><td>20</td></tr><tr><td>CET1 Ratio</td><td>14.0%</td><td>14.2%</td><td>-26 bps</td><td>-</td><td>13.2%</td><td>14.4%</td><td>-124 bps</td><td>-</td><td>13.4%</td><td>14.5%</td><td>-110 bps</td><td>-</td><td>13.8%</td><td>14.7%</td><td>-95 bps</td><td>-</td></tr><tr><td colspan="17">Balance Sheet (bn)</td></tr><tr><td>Total Assets</td><td>3,327</td><td>3,323</td><td>0%</td><td>4</td><td>3,382</td><td>3,359</td><td>1%</td><td>23</td><td>3,490</td><td>3,449</td><td>1%</td><td>42</td><td>3,586</td><td>3,554</td><td>1%</td><td>32</td></tr><tr><td>Total Equity</td><td>195</td><td>197</td><td>-1%</td><td>-2</td><td>203</td><td>204</td><td>0%</td><td>-1</td><td>213</td><td>212</td><td>0%</td><td>1</td><td>223</td><td>220</td><td>1%</td><td>2</td></tr><tr><td>Tangible Equity</td><td>160</td><td>162</td><td>-1%</td><td>-2</td><td>168</td><td>167</td><td>0%</td><td>1</td><td>178</td><td>175</td><td>2%</td><td>3</td><td>188</td><td>183</td><td>3%</td><td>5</td></tr><tr><td>Loans</td><td>1,011</td><td>1,013</td><td>0%</td><td>-2</td><td>1,031</td><td>1,028</td><td>0%</td><td>3</td><td>1,077</td><td>1,065</td><td>1%</td><td>12</td><td>1,121</td><td>1,105</td><td>1%</td><td>16</td></tr><tr><td>Deposits</td><td>1,805</td><td>1,804</td><td>0%</td><td>1</td><td>1,852</td><td>1,834</td><td>1%</td><td>18</td><td>1,950</td><td>1,903</td><td>2%</td><td>47</td><td>2,036</td><td>1,969</td><td>3%</td><td>67</td></tr><tr><td colspan="17">Ratios</td></tr><tr><td>Net Interest Margin</td><td></td><td></td><td></td><td>-</td><td>4.58%</td><td>4.55%</td><td>3 bps</td><td>-</td><td>4.70%</td><td>4.60%</td><td>10 bps</td><td>-</td><td>4.64%</td><td>4.58%</td><td>6 bps</td><td>-</td></tr><tr><td>CIR - Reported</td><td>46%</td><td>47%</td><td>-0.7 pp</td><td>-</td><td>47%</td><td>48%</td><td>-0.4 pp</td><td>-</td><td>45%</td><td>46%</td><td>-1.6 pp</td><td>-</td><td>44%</td><td>45%</td><td>-1.1 pp</td><td>-</td></tr><tr><td>CIR - Underlying</td><td>44%</td><td>45%</td><td>-1.2 pp</td><td>-</td><td>46%</td><td>46%</td><td>-0.3 pp</td><td>-</td><td>44%</td><td>45%</td><td>-0.8 pp</td><td>-</td><td>44%</td><td>44%</td><td>-0.2 pp</td><td>-</td></tr><tr><td>Cost of Risk</td><td></td><td></td><td></td><td>-</td><td>42 bps</td><td>44 bps</td><td>-2 bps</td><td>-</td><td>36 bps</td><td>39 bps</td><td>-3 bps</td><td>-</td><td>34 bps</td><td>38 bps</td><td>-5 bps</td><td>-</td></tr><tr><td>Effective Tax Rate - Reported</td><td>23%</td><td>21%</td><td>1.7 pp</td><td>-</td><td>22%</td><td>21%</td><td>1.0 pp</td><td>-</td><td>23%</td><td>21%</td><td>1.5 pp</td><td>-</td><td>23%</td><td>21%</td><td>1.4 pp</td><td>-</td></tr><tr><td>ROTE (post AT1)</td><td></td><td></td><td></td><td>-</td><td>17.1%</td><td>16.7%</td><td>0.4 pp</td><td>-</td><td>18.7%</td><td>18.0%</td><td>0.6 pp</td><td>-</td><td>18.6%</td><td>18.4%</td><td>0.2 pp</td><td>-</td></tr><tr><td>Loans / Deposits</td><td>56%</td><td>56%</td><td>-0.1 pp</td><td>-</td><td>56%</td><td>56%</td><td>-0.4 pp</td><td>-</td><td>55%</td><td>56%</td><td>-0.7 pp</td><td>-</td><td>55%</td><td>56%</td><td>-1.1 pp</td><td>-</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 2: We made changes to our NII forecast baking in higher rates offset by slightly higher opex

<table><tr><td rowspan="2">(US$mn)</td><td colspan="2">FY2026E</td><td colspan="2">FY2027E</td><td colspan="2">FY2028E</td><td colspan="2">FY2029E</td><td colspan="4">% change</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Group - Underlying basis</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Banking NII</td><td>46,592</td><td>46,769</td><td>48,627</td><td>49,546</td><td>50,018</td><td>50,996</td><td>51,441</td><td>52,527</td><td>0.4</td><td>1.9</td><td>2.0</td><td>2.1</td></tr><tr><td>Non-NII</td><td>28,715</td><td>28,715</td><td>30,737</td><td>30,737</td><td>32,704</td><td>32,704</td><td>34,595</td><td>34,595</td><td>0.0</td><td>-0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Revenue</td><td>75,307</td><td>75,483</td><td>79,364</td><td>80,283</td><td>82,722</td><td>83,700</td><td>86,036</td><td>87,123</td><td>0.2</td><td>1.2</td><td>1.2</td><td>1.3</td></tr><tr><td>Operating expenses</td><td>(34,359)</td><td>(34,359)</td><td>(35,390)</td><td>(35,536)</td><td>(36,451)</td><td>(36,753)</td><td>(37,545)</td><td>(37,856)</td><td>-0.0</td><td>0.4</td><td>0.8</td><td>0.8</td></tr><tr><td>PPP</td><td>40,948</td><td>41,125</td><td>43,975</td><td>44,748</td><td>46,271</td><td>46,947</td><td>48,491</td><td>49,267</td><td>0.4</td><td>1.8</td><td>1.5</td><td>1.6</td></tr><tr><td>Provision</td><td>(4,535)</td><td>(4,261)</td><td>(3,747)</td><td>(3,747)</td><td>(3,682)</td><td>(3,682)</td><td>(3,722)</td><td>(3,722)</td><td>-6.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Operating profit</td><td>36,413</td><td>36,863</td><td>40,228</td><td>41,001</td><td>42,589</td><td>43,265</td><td>44,769</td><td>45,545</td><td>1.2</td><td>1.9</td><td>1.6</td><td>1.7</td></tr><tr><td>Pre-tax profits</td><td>

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
