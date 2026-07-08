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
CHINA CONSUMER STAPLES

# Pork: 2Q26 preview: Earnings headwinds; lowering packaged meat in China; elevated costs overseas

We expect WH Group's OP growth to turn soft into 2Q26 at HSD% yoy OP decline, bringing 1H26 yoy down to broadly flattish, specifically:

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

1) China business (also Shuanghui):, we expect a decline in OP at 11% yoy due to the lowering unit profits (-13% yoy) for packaged meat business to drive volume growth of 2%. Hog production remains soft on top of dropping hog prices, albeit showing narrowing losses versus 1Q thanks to the Company's operation improvement.

Leaf Liu
+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Christina Liu
+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

2) International business: our US team hosted SFD mgmt meeting on 12 Jun, highlighting elevated costs for beef and freight/diesel costs for packaged meat, but hog production remains in a supportive commodity backdrop. We present hypothetical trackers in Exhibit 1 & Exhibit 2. Europe business: was seeing major headwinds at high-DD% yoy decline, given tough base for hog production business, meanwhile packaged meats in Europe continues to be strong at DD% yoy growth.

Looking into 2H26, while current consumer backdrop stays mixed, we highlight Company's flexibility to control packaged meat promotions in China and improvement across its cost structure in US business. With hog prices to be stabilized, hog business in Europe would show narrowing losses from 3Q26.

We adjust our NI for WH Group/Shuanghui by -2% to 1%/-9% to -10% for softer 2Q26, but we still look for a broadly stable full year OP yoy and high dividend yield at 7%. For WH Group, we lowered our TP from HK\$11.8 to HK\$11.1 on updated earnings, but unchanged SOTP methodology. We maintain Neutral on Shuanghui on fair valuation, with a 12m TP at Rmb25.0 (prior Rmb27.0) while maintaining target multiple unchanged at 17X 2026PE.

Exhibit 1: North America Hypothetical Hog Margin per Head  
![](images/a006092a82ab04f5f383aed05abb0c558e164ba28e74bcb85ee9d644fe13caf6.jpg)  
Hog Margin is calculated by 1) Mixed Feed Cost (10 bu corn + 150 lb soybean meal per head), subtracted by 2) North America live hog prices  
Source: Bloomberg, GS Global Investment Research

Exhibit 2: North America Hypothetical Packer Margin per Head  
![](images/2d2bb6d3068e5a3f9c26e962381db87658b653385dded716a43f9830e32b1fb2.jpg)  
Packer Margin is calculated by 1) Revenue per Hog, subtracted by 2) Cost per Hog

## Exhibit 3: WH Group Earnings Summary

<table><tr><td colspan="8">(USD mn)</td></tr><tr><td>Consolidated P&amp;L (US$mn)</td><td>FY2022Dec-22</td><td>FY2023Dec-23</td><td>FY2024Dec-24</td><td>FY2025Dec-25</td><td>FY2026EDec-26</td><td>FY2027EDec-27</td><td>FY2028EDec-28</td></tr><tr><td>Revenue</td><td>28,136</td><td>26,236</td><td>25,941</td><td>28,026</td><td>29,502</td><td>30,257</td><td>31,241</td></tr><tr><td>Underlying EBIT (excl. bio adj.)</td><td>2,093</td><td>1,471</td><td>2,404</td><td>2,612</td><td>2,577</td><td>2,544</td><td>2,582</td></tr><tr><td>Underlying NPAT (excl. bio adj.)</td><td>1,401</td><td>604</td><td>1,464</td><td>1,591</td><td>1,559</td><td>1,567</td><td>1,622</td></tr><tr><td>Net one-offs</td><td>114</td><td>67</td><td>53</td><td>(26)</td><td>(25)</td><td>(25)</td><td>(24)</td></tr><tr><td>Adj. underlying NPAT (excl. bio adj.)</td><td>1,288</td><td>537</td><td>1,411</td><td>1,617</td><td>1,584</td><td>1,592</td><td>1,646</td></tr><tr><td colspan="8">YoY Growth %</td></tr><tr><td>Sales</td><td>3%</td><td>-7%</td><td>-1%</td><td>8%</td><td>5%</td><td>3%</td><td>3%</td></tr><tr><td>EBIT</td><td>6%</td><td>-30%</td><td>63%</td><td>9%</td><td>-1%</td><td>-1%</td><td>1%</td></tr><tr><td>EBITDA</td><td>9%</td><td>-22%</td><td>40%</td><td>7%</td><td>-4%</td><td>-2%</td><td>1%</td></tr><tr><td>Underlying NPAT (excl. bio adj.)</td><td>34%</td><td>-57%</td><td>142%</td><td>9%</td><td>-2%</td><td>0%</td><td>3%</td></tr></table>

<table><tr><td>EBIT</td><td>7.4%</td><td>5.6%</td><td>9.3%</td><td>9.3%</td><td>8.7%</td><td>8.4%</td><td>8.3%</td></tr><tr><td>USD mn</td><td>FY2022</td><td>FY2023</td><td>FY2024</td><td>FY2025</td><td>FY2026E</td><td>FY2027E</td><td>FY2028E</td></tr><tr><td>China Operations</td><td>Dec-22</td><td>Dec-23</td><td>Dec-24</td><td>Dec-25</td><td>Dec-26</td><td>Dec-27</td><td>Dec-28</td></tr><tr><td>Segment revenue</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Packaged meats</td><td>4,009</td><td>3,697</td><td>3,409</td><td>3,246</td><td>3,378</td><td>3,294</td><td>3,277</td></tr><tr><td>Fresh pork</td><td>4,415</td><td>3,805</td><td>3,799</td><td>3,761</td><td>4,062</td><td>4,062</td><td>4,062</td></tr><tr><td>Others</td><td>1,112</td><td>1,246</td><td>1,210</td><td>1,482</td><td>1,629</td><td>1,790</td><td>1,968</td></tr><tr><td>Total</td><td>9,536</td><td>8,748</td><td>8,418</td><td>8,489</td><td>9,068</td><td>9,145</td><td>9,307</td></tr><tr><td>Segment profit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Packaged meats</td><td>910</td><td>879</td><td>924</td><td>891</td><td>882</td><td>824</td><td>809</td></tr><tr><td>Fresh pork</td><td>100</td><td>104</td><td>73</td><td>57</td><td>56</td><td>56</td><td>56</td></tr><tr><td>Others</td><td>30</td><td>(35)</td><td>(54)</td><td>(14)</td><td>(34)</td><td>(34)</td><td>(34)</td></tr><tr><td>Total</td><td>1,040</td><td>948</td><td>943</td><td>934</td><td>904</td><td>846</td><td>832</td></tr><tr><td>YoY Growth</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total Sales</td><td>-9%</td><td>-8%</td><td>-4%</td><td>1%</td><td>7%</td><td>1%</td><td>2%</td></tr><tr><td>EBIT</td><td>12%</td><td>-9%</td><td>-1%</td><td>-1%</td><td>-3%</td><td>-6%</td><td>-2%</td></tr><tr><td>Margin</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBIT</td><td>10.9%</td><td>10.8%</td><td>11.2%</td><td>11.0%</td><td>10.0%</td><td>9.2%</td><td>8.9%</td></tr><tr><td>Packaged meats</td><td>22.7%</td><td>23.8%</td><td>27.1%</td><td>27.4%</td><td>26.1%</td><td>25.0%</td><td>24.7%</td></tr><tr><td>Fresh pork</td><td>2.3%</td><td>2.7%</td><td>1.9%</td><td>1.5%</td><td>1.4%</td><td>1.4%</td><td>1.4%</td></tr></table>

Source: Bloomberg, GS Global Investment Research

<table><tr><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td>6,745</td><td>6,375</td><td>6,658</td><td>6,459</td><td>6,182</td><td>6,113</td><td>6,835</td><td>6,810</td><td>6,554</td><td>6,836</td><td>7,306</td><td>7,330</td><td>6,994</td><td>7,068</td><td>7,507</td><td>7,679</td></tr><tr><td>366</td><td>277</td><td>405</td><td>424</td><td>501</td><td>634</td><td>641</td><td>629</td><td>598</td><td>661</td><td>667</td><td>686</td><td>643</td><td>598</td><td>632</td><td>704</td></tr><tr><td>174</td><td>211</td><td>184</td><td>35</td><td>301</td><td>389</td><td>391</td><td>383</td><td>364</td><td>401</td><td>401</td><td>425</td><td>396</td><td>363</td><td>401</td><td>412</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>-87</td><td></td><td></td><td></td><td>121%</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>302</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2.9%</td><td>-6.9%</td><td>-8.9%</td><td>-13.1%</td><td>-8.3%</td><td>-4.1%</td><td>2.7%</td><td>5.4%</td><td>6.0%</td><td>11.8%</td><td>6.9%</td><td>7.6%</td><td>6.7%</td><td>3.4%</td><td>2.8%</td><td>4.8%</td></tr><tr><td>-43%</td><td>-52%</td><td>-7%</td><td>-5%</td><td>37%</td><td>129%</td><td>58%</td><td>48%</td><td>19%</td><td>4%</td><td>4%</td><td>9%</td><td>8%</td><td>-9%</td><td>-5%</td><td>3%</td></tr><tr><td>-56%</td><td>-30%</td><td>-15%</td><td>-93%</td><td>73%</td><td>84%</td><td>113%</td><td>994%</td><td>21%</td><td>3%</td><td>3%</td><td>11%</td><td>9%</td><td>-10%</td><td>0%</td><td>-3%</td></tr><tr><td>5.4%</td><td>4.3%</td><td>6.1%</td><td>6.6%</td><td>8.1%</td><td>10.4%</td><td>9.4%</td><td>9.2%</td><td>9.1%</td><td>9.7%</td><td>9.1%</td><td>9.4%</td><td>9.2%</td><td>8.5%</td><td>8.4%</td><td>9.2%</td></tr><tr><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td>1,030</td><td>930</td><td>973</td><td>764</td><td>935</td><td>762</td><td>944</td><td>768</td><td>759</td><td>772</td><td>937</td><td>778</td><td>913</td><td>780</td><td>942</td><td>743</td></tr><tr><td>1,020</td><td>961</td><td>948</td><td>876</td><td>835</td><td>821</td><td>1,062</td><td>1,081</td><td>919</td><td>873</td><td>973</td><td>996</td><td>899</td><td>809</td><td>1,158</td><td>1,196</td></tr><tr><td>271</td><td>277</td><td>331</td><td>368</td><td>255</td><td>289</td><td>326</td><td>339</td><td>325</td><td>367</td><td>384</td><td>405</td><td>361</td><td>407</td><td>407</td><td>453</td></tr><tr><td>2,321</td><td>2,168</td><td>2,252</td><td>2,008</td><td>2,025</td><td>1,872</td><td>2,332</td><td>2,189</td><td>2,003</td><td>2,012</td><td>2,294</td><td>2,179</td><td>2,173</td><td>1,996</td><td>2,507</td><td>2,392</td></tr><tr><td>238</td><td>215</td><td>242</td><td>184</td><td>262</td><td>198</td><td>264</td><td>200</td><td>203</td><td>208</td><td>278</td><td>202</td><td>255</td><td>199</td><td>254</td><td>174</td></tr><tr><td>53</td><td>17</td><td>25</td><td>9</td><td>17</td><td>26</td><td>14</td><td>16</td><td>19</td><td>13</td><td>8</td><td>17</td><td>19</td><td>9</td><td>15</td><td>13</td></tr><tr><td>-11</td><td>7</td><td>1</td><td>-33</td><td>-28</td><td>-33</td><td>10</td><td>-2</td><td>-7</td><td>-1</td><td>3</td><td>-9</td><td>-23</td><td>-9</td><td>-9</td><td>6</td></tr><tr><td>280</td><td>240</td><td>268</td><td>160</td><td>251</td><td>191</td><td>288</td><td>214</td><td>215</td><td>220</td><td>289</td><td>210</td><td>251</td><td>199</td><td>261</td><td>193</td></tr><tr><td>5.4%</td><td>0.0%</td><td>-9.1%</td><td>-25.4%</td><td>-12.7%</td><td>-13.6%</td><td>3.6%</td><td>9.0%</td><td>-1.1%</td><td>7.5%</td><td>-1.6%</td><td>-0.4%</td><td>8.5%</td><td>-0.8%</td><td>9.2%</td><td>9.8%</td></tr><tr><td>-7.7%</td><td>3.0%</td><td>11.4%</td><td>-39.2%</td><td>-10.5%</td><td>-20.5%</td><td>7.3%</td><td>33.7%</td><td>-14.3%</td><td>15.2%</td><td>0.4%</td><td>-1.5%</td><td>16.7%</td><td>-9.2%</td><td>-9.8%</td><td>-8.3%</td></tr><tr><td>12.1%</td><td>11.1%</td><td>11.9%</td><td>8.0%</td><td>12.4%</td><td>10.2%</td><td>12.3%</td><td>9.8%</td><td>10.7%</td><td>10.9%</td><td>12.6%</td><td>9.7%</td><td>11.6%</td><td>10.0%</td><td>10.4%</td><td>8.1%</td></tr><tr><td>23.1%</td><td>23.1%</td><td>24.9%</td><td>24.1%</td><td>28.0%</td><td>26.0%</td><td>28.0%</td><td>26.0%</td><td>26.7%</td><td>26.9%</td><td>29.7%</td><td>26.0%</td><td>27.9%</td><td>25.5%</td><td>27.0%</td><td>23.4%</td></tr><tr><td>5.2%</td><td>1.8%</td><td>2.6%</td><td>1.0%</td><td>2.0%</td><td>3.2%</td><td>1.3%</td><td>1.5%</td><td>2.1%</td><td>1.5%</td><td>0.8%</td><td>1.7%</td><td>2.1%</td><td>1.1%</td><td>1.3%</td><td>1.1%</td></tr></table>

<table><tr><td>USD mn</td><td>FY2022</td><td>FY2023</td><td>FY2024</td><td>FY2025</td><td>FY2026E</td><td>FY2027E</td><td>FY2028E</td></tr><tr><td>US and international</td><td>Dec-22</td><td>Dec-23</td><td>Dec-24</td><td>Dec-25</td><td>Dec-26</td><td>Dec-27</td><td>Dec-28</td></tr><tr><td colspan="8">Segment revenue</td></tr><tr><td>Hog production</td><td>4,456</td><td>3,317</td><td>3,002</td><td>3,003</td><td>3,210</td><td>3,182</td><td>3,182</td></tr><tr><td>Packaged meats</td><td>9,260</td><td>8,279</td><td>8,317</td><td>8,754</td><td>8,956</td><td>9,090</td><td>9,273</td></tr><tr><td>Fresh pork</td><td>5,568</td><td>5,189</td><td>4,935</td><td>5,986</td><td>5,464</td><td>5,546</td><td>5,658</td></tr><tr><td>International &amp; Others</td><td>3,479</td><td>4,103</td><td>4,508</td><td>5,039</td><td>5,543</td><td>6,097</td><td>6,707</td></tr><tr><td>Less: intersegment sales</td><td>(4,163)</td><td>(3,400)</td><td>(3,239)</td><td>(3,245)</td><td>(2,754)</td><td>(2,805)</td><td>(2,886)</td></tr><tr><td>Total consolidated</td><td>18,600</td><td>17,488</td><td>17,523</td><td>19,537</td><td>20,418</td><td>21,111</td><td>21,934</td></tr><tr><td>Segment profit</td><td></td><td></td><td></td><td></td><td>1.7%</td><td></td><td></td></tr><tr><td>Hog production</td><td>-133</td><td>-754</td><td>-94</td><td>227</td><td>231</td><td>166</td><td>156</td></tr><tr><td>Packaged meats</td><td>1,058</td><td>1,072</td><td>1,174</td><td>1,097</td><td>1,113</td><td>1,167</td><td>1,195</td></tr><tr><td>Fresh pork</td><td>90</td><td>130</td><td>264</td><td>217</td><td>223</td><td>238</td><td>247</td></tr><tr><td>International &amp; Others</td><td>113</td><td>193</td><td>274</td><td>285</td><td>195</td><td>217</td><td>241</td></tr><tr><td>Total</td><td>1,128</td><td>641</td><td>1,618</td><td>1,826</td><td>1,762</td><td>1,787</td><td>1,840</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>-3.5%</td><td></td><td></td></tr><tr><td colspan="8">YoY Growth</td></tr><tr><td>Sales</td><td>10.9%</td><td>-6.0%</td><td>0.2%</td><td>11.5%</td><td>4.5%</td><td>3.4%</td><td>3.9%</td></tr><tr><td>Operating profit</td><td>1.6%</td><td>-50.3%</td><td>179.3%</td><td>14.9%</td><td>-0.3%</td><td>1.5%</td><td>3.1%</td></tr></table>

Source: Company data, GS Global Investment Research

<table><tr><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td>587</td><td>881</td><td>815</td><td>1,035</td><td>540</td><td>810</td><td>778</td><td>874</td><td>438</td><td>643</td><td>619</td><td>1,303</td><td>439</td><td>796</td><td>831</td><td>814</td></tr><tr><td>2,076</td><td>1,871</td><td>1,928</td><td>2,404</td><td>1,999</td><td>1,944</td><td>1,916</td><td>2,458</td><td>2,023</td><td>2,079</td><td>2,089</td><td>2,563</td><td>2,148</td><td>2,208</td><td>2,068</td><td>2,532</td></tr><tr><td>1,443</td><td>1,310</td><td>1,460</td><td>977</td><td>1,241</td><td>1,207</td><td>1,423</td><td>1,064</td><td>1,563</td><td>1,507</td><td>1,664</td><td>1,251</td><td>1,477</td><td>1,366</td><td>1,442</td><td>1,180</td></tr><tr><td>954</td><td>1,060</td><td>1,050</td><td>1,039</td><td>987</td><td>1,128</td><td>1,230</td><td>1,163</td><td>1,074</td><td>1,358</td><td>1,394</td><td>1,213</td><td>1,358</td><td>1,494</td><td>1,464</td><td>1,226</td></tr><tr><td>(635)</td><td>(915)</td><td>(848)</td><td>(1,003)</td><td>(610)</td><td>(849)</td><td>(843)</td><td>(937)</td><td>(547)</td><td>(763)</td><td>(755)</td><td>(1,179)</td><td>(601)</td><td>(792)</td><td>(804)</td><td>(466)</td></tr><tr><td>4,424</td><td>4,207</td><td>4,406</td><td>4,451</td><td>4,157</td><td>4,241</td><td>4,503</td><td>4,622</td><td>4,551</td><td>4,824</td><td>5,011</td><td>5,151</td><td>4,821</td><td>5,071</td><td>5,001</td><td>5,286</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1%</td><td>0.03</td><td>0.06</td></tr><tr><td>(271)</td><td>(271)</td><td>(82)</td><td>(130)</td><td>(173)</td><td>9</td><td>59</td><td>11</td><td>17</td><td>22</td><td>103</td><td>85</td><td>14</td><td>59</td><td>91</td><td>68</td></tr><tr><td>301</td><td>277</td><td>187</td><td>307</td><td>288</td><td>326</td><td>240</td><td>320</td><td>266</td><td>303</td><td>227</td><td>301</td><td>278</td><td>281</td><td>234</td><td>320</td></tr><tr><td>53</td><

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
