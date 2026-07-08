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
July 6, 2026 09:00 PM GMT

Greater China Semiconductors | Asia Pacific

# PC Semis: Divergent gross margin trends

FOMP (fear of missing procurement) will likely drive stable shipments for PC semis into 3Q, yet profitability may vary.

## Key Takeaways

We expect PC semi shipments to sustain into 3Q, likely due to FOMP.

\- With cost hikes (mainly from OSAT), supply chain management and customer mix will derive a divergent margin outlook.

\- Overall we maintain our view that new growth drivers are needed, but adjust PT/earnings based on our demand outlook for 2H.

3Q demand outlook better than feared? We believe 3Q demand outlook for most PC semis could be stable – PC semi customers could maintain a flattish Q/Q procurement target, with key components (e.g. CPU) showing further sequential growth. Major driver could be FOMP, driven by overall mature foundry and OSAT tightness (limited supply/cost hikes). Some customers may consider low inventory risks if there's pent-up demand into 2027, suggesting increasing inventory digestion risks, especially when Windows activation day is approaching 200+.

Margin could show divergent trend: We expect all PC semis to try to pass through foundry/OSAT cost hikes to customers in 3Q. However, impact to gross margin could be different than during Covid, as overall tightness is not driven by PCs, but indirectly from servers. We believe design house scale, supply chain divergence and customer portfolios will derive differing margin outlooks; large IC design houses' strong supply chain management and comprehensive product mix (e.g. Novatek, Realtek) to maintain or even increase gross margin. Conversely, some small design houses may not see margin increase (e.g. Parade/Elan).

New growth drivers major rating factors: Prefer small design houses, mainly on emerging new growth drivers. Elan to benefit from non-PCs (mainly drones), with potential mid-high single digit revenue contribution in 2027. Parade likely to show high 2027 growth thanks to chipset ramp up. Conversely, we await new growth drivers from Novatek on cloud ASIC, which likely will take a longer time. We believe Realtek will ramp up 100G DSP in 2026, but 400G will be in 2028.

Maintain OW on Parade/Elan, Realtek EW and Novatek UW: Revise up Elan earnings ests mainly due to margin improvement and new revenue opportunities from non PC businesses – it is likely to gain some share in touch pads post Synaptics acquisition announcement. Valuation is 17x 2026e P/E, undemanding vs IC design peers at \~30x. Trim Parade PT/earnings ests on lower GM assumption for major client Apple and its sales (higher Apple end-product pricing). Revise up Realtek's earnings ests/PT thanks to sustained 3Q outlook (both revenue and GM).

MS TAIWAN LIMITED+

Charlie Chan
Equity Analyst
Charlie.Chan@morganstanley.com +886 2 2730-1725

Ethan Jia
Research Associate
Ethan.Jia@morganstanley.com +852 3963-2287

Asia Summer School 2026

![](images/2f97bf3e6eb2183277eccccd4da414d023e133571410b9b8d198fee5d8b5bd9d.jpg)

<table><tr><td colspan="3">GREATER CHINA TECHNOLOGY SEMICONDUCTORS</td></tr><tr><td>Asia Pacific Industry View</td><td colspan="2">Attractive</td></tr><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>NT$180.00</td><td>NT$250.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>NT$1,000.00</td><td>NT$818.00</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>NT$570.00</td><td>NT$717.00</td></tr></table>

With this note, coverage of Elan Microelectronics (2458.TW) is transferred to Daniel Yen.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Parade: Earnings Estimate Revisions

We cut our EPS estimates by 14%/14% for 2027/28: We factor in the lower GM assumption from its major client (Apple) and lower Apple sales (due to higher Apple end product pricing).

Exhibit 1: Parade: Summary of estimate revisions

<table><tr><td>NT$ mn</td><td>Current 2026E</td><td>Previous 2026E</td><td>Diff.</td><td>Current 2027E</td><td>Previous 2027E</td><td>Diff.</td><td>Current 2028E</td><td>Previous 2028E</td><td>Diff.</td></tr><tr><td>Net sales</td><td>15,865</td><td>15,865</td><td>0%</td><td>18,478</td><td>20,041</td><td>-8%</td><td>20,064</td><td>21,808</td><td>-8%</td></tr><tr><td>COGS</td><td>9,215</td><td>9,205</td><td></td><td>10,597</td><td>11,458</td><td></td><td>11,400</td><td>12,344</td><td></td></tr><tr><td>Gross profit</td><td>6,650</td><td>6,660</td><td>0%</td><td>7,881</td><td>8,583</td><td>-8%</td><td>8,665</td><td>9,464</td><td>-8%</td></tr><tr><td>Operating expenses</td><td>4,259</td><td>4,259</td><td></td><td>4,406</td><td>4,480</td><td></td><td>4,572</td><td>4,654</td><td></td></tr><tr><td>Operating profit</td><td>2,390</td><td>2,401</td><td>0%</td><td>3,475</td><td>4,103</td><td>-15%</td><td>4,092</td><td>4,810</td><td>-15%</td></tr><tr><td>Non-op. income (exp.)</td><td>216</td><td>216</td><td></td><td>230</td><td>230</td><td></td><td>230</td><td>230</td><td></td></tr><tr><td>Pretax Income</td><td>2,606</td><td>2,617</td><td>0%</td><td>3,705</td><td>4,333</td><td>-14%</td><td>4,322</td><td>5,040</td><td>-14%</td></tr><tr><td>Taxes</td><td>235</td><td>236</td><td></td><td>333</td><td>390</td><td></td><td>389</td><td>454</td><td></td></tr><tr><td>Net income</td><td>2,371</td><td>2,381</td><td>0%</td><td>3,371</td><td>3,943</td><td>-14%</td><td>3,933</td><td>4,586</td><td>-14%</td></tr><tr><td>Reported Diluted EPS</td><td>30.34</td><td>30.47</td><td>0%</td><td>43.14</td><td>50.45</td><td>-14%</td><td>50.33</td><td>58.69</td><td>-14%</td></tr><tr><td colspan="10">Margins</td></tr><tr><td>Gross margin</td><td>41.9%</td><td>42.0%</td><td>0 ppt</td><td>42.7%</td><td>42.8%</td><td>0 ppt</td><td>43.2%</td><td>43.4%</td><td>0 ppt</td></tr><tr><td>Operating margin</td><td>15.1%</td><td>15.1%</td><td>0 ppt</td><td>18.8%</td><td>20.5%</td><td>-2 ppt</td><td>20.4%</td><td>22.1%</td><td>-2 ppt</td></tr><tr><td>Pretax margin</td><td>16.4%</td><td>16.5%</td><td>0 ppt</td><td>20.0%</td><td>21.6%</td><td>-2 ppt</td><td>21.5%</td><td>23.1%</td><td>-2 ppt</td></tr><tr><td>Net margin</td><td>14.9%</td><td>15.0%</td><td>0 ppt</td><td>18.2%</td><td>19.7%</td><td>-1 ppt</td><td>19.6%</td><td>21.0%</td><td>-1 ppt</td></tr></table>

Source: MS (E) estimates

Exhibit 2: Quarterly earnings summary

<table><tr><td>NT$ in million</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>1Q28E</td><td>2Q28E</td><td>3Q28E</td><td>4Q28E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Total Revenues</td><td>4,152</td><td>4,114</td><td>4,377</td><td>3,888</td><td>3,990</td><td>4,049</td><td>4,038</td><td>3,788</td><td>3,933</td><td>4,506</td><td>5,109</td><td>4,931</td><td>4,727</td><td>4,900</td><td>5,463</td><td>4,974</td><td>16,531</td><td>15,865</td><td>18,478</td><td>20,064</td></tr><tr><td>Sequential Change</td><td>0.8%</td><td>-0.9%</td><td>6.4%</td><td>-11.2%</td><td>2.6%</td><td>1.5%</td><td>-0.3%</td><td>-6.2%</td><td>3.8%</td><td>14.6%</td><td>13.4%</td><td>-3.5%</td><td>-4.1%</td><td>3.7%</td><td>11.5%</td><td>-9.0%</td><td></td><td></td><td></td><td></td></tr><tr><td>Change vs Year Ago</td><td>8.8%</td><td>5.2%</td><td>-0.5%</td><td>-5.6%</td><td>-3.9%</td><td>-1.6%</td><td>-7.7%</td><td>-2.6%</td><td>-1.4%</td><td>11.3%</td><td>26.5%</td><td>30.2%</td><td>20.2%</td><td>8.8%</td><td>6.9%</td><td>0.9%</td><td>1.8%</td><td>-4.0%</td><td>16.5%</td><td>8.6%</td></tr><tr><td>Cost of Sales</td><td>2,385</td><td>2,341</td><td>2,517</td><td>2,254</td><td>2,382</td><td>2,326</td><td>2,320</td><td>2,187</td><td>2,257</td><td>2,583</td><td>2,926</td><td>2,831</td><td>2,694</td><td>2,776</td><td>3,097</td><td>2,832</td><td>9,496</td><td>9,215</td><td>10,597</td><td>11,400</td></tr><tr><td>Percent of Revenues</td><td>57%</td><td>57%</td><td>57%</td><td>58%</td><td>60%</td><td>57%</td><td>57%</td><td>58%</td><td>57%</td><td>57%</td><td>57%</td><td>57%</td><td>57%</td><td>57%</td><td>57%</td><td>57%</td><td>57%</td><td>58%</td><td>57%</td><td>57%</td></tr><tr><td>Gross Margin</td><td>1,767</td><td>1,774</td><td>1,860</td><td>1,634</td><td>1,608</td><td>1,723</td><td>1,718</td><td>1,601</td><td>1,676</td><td>1,922</td><td>2,183</td><td>2,100</td><td>2,033</td><td>2,124</td><td>2,366</td><td>2,142</td><td>7,035</td><td>6,650</td><td>7,881</td><td>8,665</td></tr><tr><td>Percent of Revenues</td><td>42.6%</td><td>43.1%</td><td>42.5%</td><td>42.0%</td><td>40.3%</td><td>42.5%</td><td>42.5%</td><td>42.3%</td><td>42.6%</td><td>42.7%</td><td>42.7%</td><td>42.6%</td><td>43.0%</td><td>43.3%</td><td>43.3%</td><td>43.1%</td><td>42.6%</td><td>41.9%</td><td>42.7%</td><td>43.2%</td></tr><tr><td>Incremental Margin</td><td>91%</td><td>NM</td><td>33%</td><td>NM</td><td>-26%</td><td>194%</td><td>NM</td><td>NM</td><td>52%</td><td>43%</td><td>43%</td><td>NM</td><td>NM</td><td>52%</td><td>43%</td><td>NM</td><td>46%</td><td>NM</td><td>47%</td><td>49%</td></tr><tr><td>Total Opex</td><td>1,110</td><td>1,065</td><td>1,048</td><td>1,103</td><td>1,068</td><td>1,055</td><td>1,074</td><td>1,063</td><td>1,069</td><td>1,096</td><td>1,125</td><td>1,116</td><td>1,126</td><td>1,135</td><td>1,161</td><td>1,150</td><td>4,326</td><td>4,259</td><td>4,406</td><td>4,572</td></tr><tr><td>Percent of Revenues</td><td>26.7%</td><td>25.9%</td><td>23.9%</td><td>28.4%</td><td>26.8%</td><td>26.1%</td><td>26.6%</td><td>28.1%</td><td>27.2%</td><td>24.3%</td><td>22.0%</td><td>22.6%</td><td>23.8%</td><td>23.2%</td><td>21.3%</td><td>23.1%</td><td>26.2%</td><td>26.8%</td><td>23.8%</td><td>22.8%</td></tr><tr><td>R&amp;D</td><td>744</td><td>723</td><td>700</td><td>742</td><td>728</td><td>728</td><td>748</td><td>748</td><td>748</td><td>748</td><td>748</td><td>748</td><td>768</td><td>768</td><td>768</td><td>780</td><td>2,910</td><td>2,953</td><td>2,993</td><td>3,084</td></tr><tr><td>Percent of Revenues</td><td>17.9%</td><td>17.6%</td><td>16.0%</td><td>19.1%</td><td>18.3%</td><td>18.0%</td><td>18.5%</td><td>19.8%</td><td>19.0%</td><td>16.6%</td><td>14.6%</td><td>15.2%</td><td>16.2%</td><td>15.7%</td><td>14.1%</td><td>15.7%</td><td>17.6%</td><td>18.6%</td><td>16.2%</td><td>15.4%</td></tr><tr><td>General &amp; administrative</td><td>156</td><td>143</td><td>134</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>569</td><td>545</td><td>545</td><td>545</td></tr><tr><td>Percent of Revenues</td><td>3.7%</td><td>3.5%</td><td>3.1%</td><td>3.5%</td><td>3.4%</td><td>3.4%</td><td>3.4%</td><td>3.6%</td><td>3.5%</td><td>3.0%</td><td>2.7%</td><td>2.8%</td><td>2.9%</td><td>2.8%</td><td>2.5%</td><td>2.7%</td><td>3.4%</td><td>3.4%</td><td>3.0%</td><td>2.7%</td></tr><tr><td>Selling &amp; marketing</td><td>210</td><td>199</td><td>213</td><td>225</td><td>203</td><td>190</td><td>190</td><td>178</td><td>185</td><td>212</td><td>240</td><td>232</td><td>222</td><td>230</td><td>257</td><td>234</td><td>847</td><td>762</td><td>868</td><td>943</td></tr><tr><td>Percent of Revenues</td><td>5.1%</td><td>4.8%</td><td>4.9%</td><td>5.8%</td><td>5.1%</td><td>4.7%</td><td>4.7%</td><td>4.7%</td><td>4.7%</td><td>4.7%</td><td>4.7%</td><td>4.7%</td><td>4.7%</td><td>4.7%</td><td>4.7%</td><td>4.7%</td><td>5.1%</td><td>4.8%</td><td>4.7%</td><td>4.7%</td></tr><tr><td>Operating Income</td><td>657</td><td>709</td><td>812</td><td>531</td><td>540</td><td>668</td><td>644</td><td>539</td><td>607</td><td>826</td><td>1,058</td><td>984</td><td>907</td><td>989</td><td>1,205</td><td>992</td><td>2,709</td><td>2,390</td><td>3,475</td><td>4,092</td></tr><tr><td>Percent of Revenues</td><td>15.8%</td><td>17.2%</td><td>18.6%</td><td>13.7%</td><td>13.5%</td><td>16.5%</td><td>15.9%</td><td>14.2%</td><td>15.4%</td><td>18.3%</td><td>20.7%</td><td>20.0%</td><td>19.2%</td><td>20.2%</td><td>22.1%</td><td>19.9%</td><td>16.4%</td><td>15.1%</td><td>18.8%</td><td>20.4%</td></tr><tr><td>Change vs Year Ago</td><td>25.7%</td><td>38.7%</td><td>7.8%</td><td>-20.1%</td><td>-17.9%</td><td>-5.7%</td><td>-20.8%</td><td>1.5%</td><td>12.4%</td><td>23.7%</td><td>64.4%</td><td>82.6%</td><td>49.4%</td><td>19.7%</td><td>13.9%</td><td>0.8%</td><td>10%</td><td>-12%</td><td>45%</td><td>18%</td></tr><tr><td>Total Non-operating Income(Loss)</td><td>71</td><td>69</td><td>69</td><td>65</td><td>42</td><td>59</td><td>58</td><td>57</td><td>57</td><td>57</td><td>57</td><td>57</td><td>57</td><td>57</td><td>57</td><td>57</td><td>273</td><td>216</td><td>230</td><td>230</td></tr><tr><td>Profit Before Taxes</td><td>728</td><td>777</td><td>881</td><td>596</td><td>582</td><td>727</td><td>702</td><td>596</td><td>664</td><td>883</td><td>1,116</td><td>1,041</td><td>964</td><td>1,046</td><td>1,262</td><td>1,049</td><td>2,982</td><td>2,606</td><td>3,705</td><td>4,322</td></tr><tr><td>Percent of Revenues</td><td>18%</td><td>19%</td><td>20%</td><td>15%</td><td>15%</td><td>18%</td><td>17%</td><td>16%</td><td>17%</td><td>20%</td><td>22%</td><td>21%</td><td>20%</td><td>21%</td><td>23%</td><td>21%</td><td>18%</td><td>16%</td><td>20%</td><td>22%</td></tr><tr><td>Taxes</td><td>64</td><td>75</td><td>66</td><td>51</td><td>53</td><td>65</td><td>63</td><td>54</td><td>60</td><td>80</td><td>100</td><td>94</td><td>87</td><td>94</td><td>114</td><td>94</td><td>256</td><td>235</td><td>333</td><td>389</td></tr><tr><td>Tax Rate</td><td>8.8%</td><td>9.6%</td><td>7.4%</td><td>8.6%</td><td>9.1%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td><td>8.6%</td><td>9.0%</td><td>9.0%</td><td>9.0%</td></tr><tr><td>Net Income, Cont Ops</td><td>664</td><td>702</td><td>816</td><td>544</td><td>529</td><td>661</td><td>638</td><td>542</td><td>605</td><td>804</td><td>1,015</td><td>947</td><td>877</td><td>952</td><td>1,149</td><td>955</td><td>2,727</td><td>2,371</td><td>3,371</td><td>3,933</td></tr><tr><td>Percent of Revenues</td><td>16%</td><td>17%</td><td>19%</td><td>14%</td><td>13%</td><td>16%</td><td>16%</td><td>14%</td><td>15%</td><td>18%</td><td>20%</td><td>19%</td><td>19%</td><td>19%</td><td>21%</td><td>19%</td><td>16%</td><td>15%</td><td>18%</td><td>20%</td></tr><tr><td>Reported Income (TW GAAP)</td><td>664</td><td>702</td><td>816</td><td>544</td><td>529</td><td>661</td><td>638</td><td>542</td><td>605</td><td>804</td><td>1,015</td><td>947</td><td>877</td><td>952</td><td>1,149</td><td>955</td><td>2,727</td><td>2,371</td><td>3,371</td><td>3,933</td></tr><tr><td>Percent of Revenues Change vs Year Ago</td><td>16% 0%</td><td>17% 0%</td><td>19% 0%</td><td>14% 0%</td><td>13% 0%</td><td>16% 0%</td><td>16% 0%</td><td>14% 0%</td><td>15% 0%</td><td>18% 0%</td><td>20% 0%</td><td>19% 0%</td><td>19% 0%</td><td>19% 0%</td><td>21% 0%</td><td>19% 0%</td><td>16% 5%</td><td>15% -13%</td><td>18% 42%</td><td>20% 17%</td></tr><tr><td>Reported EPS (NT$, TW GAAF Change vs Year Ago)</td><td>8.38 16%</td><td>8.95 25%</td><td

[中间内容因长度限制已省略]

ronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,295.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb139.60</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$605.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$77.60</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,445.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$170.50</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$193.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$411.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$204.80</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb83.60</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$184.00</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb102.77</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb47.25</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb325.40</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$60.65</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb90.88</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$30.92</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb145.60</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb129.35</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb81.76</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb30.59</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb129.46</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$987.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,530.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$17,265.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$117.50</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb120.11</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb677.77</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$142.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$382.60</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb266.80</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$538.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$176.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$654.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$73.40</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$783.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb59.03</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$184.50</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$110.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$221.50</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb178.80</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb618.02</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,030.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$581.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$13.15</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,865.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$7,380.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$300.71</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,900.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
