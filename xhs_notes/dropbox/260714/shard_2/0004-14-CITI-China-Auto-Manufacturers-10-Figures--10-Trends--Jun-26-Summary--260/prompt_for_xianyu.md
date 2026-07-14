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
# China Auto Manufacturers

## 10 Figures; 10 Trends (Jun-26 Summary)

## CITI'S TAKE

Summary below on Jun-26 insurance retail sales trend.

Figure 1: Who gained NEV market shares – BYD, SAIC Motor, Xpeng, Nio, etc., gained NEV market shares MoM in Jun-26; Insurance retail data suggest Jun-26 China domestically produced NEV-PV sales were +9% MoM (-10% YoY), slightly beating CPCA retail MoM pace. Further reading: (1) China Auto Manufacturers - CPCA Jun Update; Export Strong, NEV Wholesale Slight Miss; (2) China Auto Manufacturers - Auto Policies & Demand Outlook for 2H

Figure 2: ICE penetration up MoM in Jun – Jun-26 PV insurance data suggests ICE sales penetration increased to 39.7% (+2.0ppt MoM) as falling crude oil prices could boost ICE purchase, while BEV/PHEV/EREV trending at -1.0/-0.3/-0.7ppt MoM.

Figure 3: Nio/Changan/Xpeng gained BEV market share MoM in Jun – Nio/Changan/Xpeng/GAC gained BEV market share at +0.3/+0.3/+0.1/+0.1ppt MoM, while Seres/Geely/BYD lost BEV market share at -0.7/-0.4/-0.3ppt MoM.

Figure 4: BYD/Dongfeng/GAC gained PHEV market share MoM in Jun – BYD/Dongfeng/GAC gained PHEV market share by +2.9/+0.8/+0.4ppt MoM in Jun, while Geely/Changan/GWM lost share by -3.1/-0.7/-0.5ppt MoM.

Figure 5: Seres/Li Auto lost EREV market share MoM in Jun – Leapmotor/Changan gained EREV market share by +2.2/+0.4ppt MoM in Jun, while Seres/Li Auto lost share by -2.1/-1.9ppt MoM.

Figure 6: Chinese brands' ICE market shares down MoM in Jun – Chinese brands ICE market share decreased by -2.0ppt MoM to 32.8% in Jun, while German/Japanese/US brands were trending at +2.2/-0.2/-0.3ppt MoM.

Figure 7: Geely led Chinese brands' ICE market in Jun – Among Chinese brands (ICE), Chery/GWM/FAW gained ICE share by +2.0/+0.7/+0.7ppt MoM in Jun, while SAIC Motor/Geely/Changan lost share by -1.3/-1.3/-1.2ppt MoM. Geely led Chinese brands' ICE market in the month with market share of 30.3%.

Figure 8: Tesla summary – Tesla Insurance retail (domestically produced) saw -15% YoY/ +9% MoM to 52,078 units. Its wholesales reached 89,091 units in Jun (+24% YoY/ +4% MoM) and export volume reached 36,171 units (+258% YoY/ -7% MoM).

Figure 9: PV inventory down MoM in Jun – Based on our estimation, PV inventory at end-Jun declined by 0.5 month MoM to 2.7 months; NEV inventory at end-Jun declined by 0.2 month MoM to 1.9 months, and ICE inventory at end-Jun decreased by 1.0 month MoM to 4.0 months.

Figure 10: Local Chinese brands' NEV market shares – Chinese brands NEV market share remained high level of 83.9% (+0.3ppt MoM) in Jun, versus US brands' 11.1% (-0.5ppt MoM).

Jeff Chung $^{AC}$ +852-2501-2787
jeff.m.chung@citi.com

Kyle Wu

+852-2501-8483

kyle.wu@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations. Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

Figure 1. NEV Insurance Retail by OEM

<table><tr><td rowspan="2"></td><td colspan="6">Jun-26</td><td colspan="4">6M26</td></tr><tr><td>Sales</td><td>YoY</td><td>MoM</td><td>Mkt Shr</td><td>YoY</td><td>MoM</td><td>Sales</td><td>YoY</td><td>Mkt Shr</td><td>YoY</td></tr><tr><td>BYD</td><td>220,837</td><td>-35%</td><td>13%</td><td>22.1%</td><td>-8.3ppt</td><td>0.7ppt</td><td>974,385</td><td>-38%</td><td>21.5%</td><td>-8.1ppt</td></tr><tr><td>Geely</td><td>112,970</td><td>-11%</td><td>2%</td><td>11.3%</td><td>-0.1ppt</td><td>-0.8ppt</td><td>527,667</td><td>-13%</td><td>11.7%</td><td>0.2ppt</td></tr><tr><td>LeapMotor</td><td>70,207</td><td>73%</td><td>11%</td><td>7.0%</td><td>3.4ppt</td><td>0.1ppt</td><td>258,758</td><td>45%</td><td>5.7%</td><td>2.3ppt</td></tr><tr><td>Chang&#x27;an Local</td><td>65,209</td><td>-8%</td><td>11%</td><td>6.5%</td><td>0.1ppt</td><td>0.1ppt</td><td>281,086</td><td>-13%</td><td>6.2%</td><td>0.1ppt</td></tr><tr><td>SAIC GM Wuling</td><td>47,377</td><td>-18%</td><td>2%</td><td>4.7%</td><td>-0.5ppt</td><td>-0.3ppt</td><td>205,896</td><td>-37%</td><td>4.6%</td><td>-1.7ppt</td></tr><tr><td>Tesla</td><td>52,078</td><td>-15%</td><td>9%</td><td>5.2%</td><td>-0.3ppt</td><td>0.0ppt</td><td>238,885</td><td>-10%</td><td>5.3%</td><td>0.3ppt</td></tr><tr><td>Seres</td><td>29,524</td><td>-34%</td><td>-15%</td><td>3.0%</td><td>-1.0ppt</td><td>-0.9ppt</td><td>159,488</td><td>8%</td><td>3.5%</td><td>0.7ppt</td></tr><tr><td>Li Auto</td><td>31,139</td><td>-13%</td><td>-6%</td><td>3.1%</td><td>-0.1ppt</td><td>-0.5ppt</td><td>191,488</td><td>-8%</td><td>4.2%</td><td>0.3ppt</td></tr><tr><td>GAC Local</td><td>27,334</td><td>-15%</td><td>18%</td><td>2.7%</td><td>-0.1ppt</td><td>0.2ppt</td><td>125,397</td><td>-24%</td><td>2.8%</td><td>-0.3ppt</td></tr><tr><td>GreatWall</td><td>24,942</td><td>-20%</td><td>5%</td><td>2.5%</td><td>-0.3ppt</td><td>-0.1ppt</td><td>115,596</td><td>-18%</td><td>2.6%</td><td>-0.1ppt</td></tr><tr><td>DF Local</td><td>21,179</td><td>-33%</td><td>5%</td><td>2.1%</td><td>-0.7ppt</td><td>-0.1ppt</td><td>115,190</td><td>-12%</td><td>2.5%</td><td>0.1ppt</td></tr><tr><td>SAIC Motor</td><td>36,159</td><td>206%</td><td>32%</td><td>3.6%</td><td>2.5ppt</td><td>0.6ppt</td><td>142,048</td><td>146%</td><td>3.1%</td><td>2.0ppt</td></tr><tr><td>Nio</td><td>41,457</td><td>89%</td><td>16%</td><td>4.1%</td><td>2.2ppt</td><td>0.2ppt</td><td>195,835</td><td>68%</td><td>4.3%</td><td>2.1ppt</td></tr><tr><td>Chery Local</td><td>37,726</td><td>-8%</td><td>9%</td><td>3.8%</td><td>0.1ppt</td><td>0.0ppt</td><td>161,749</td><td>-30%</td><td>3.6%</td><td>-0.8ppt</td></tr><tr><td>Xiaomi</td><td>34,818</td><td>36%</td><td>6%</td><td>3.5%</td><td>1.2ppt</td><td>-0.1ppt</td><td>186,131</td><td>18%</td><td>4.1%</td><td>1.1ppt</td></tr><tr><td>Xpeng</td><td>32,133</td><td>-1%</td><td>24%</td><td>3.2%</td><td>0.3ppt</td><td>0.4ppt</td><td>133,568</td><td>-26%</td><td>3.0%</td><td>-0.5ppt</td></tr><tr><td>SAIC-VW</td><td>8,450</td><td>29%</td><td>16%</td><td>0.8%</td><td>0.3ppt</td><td>0.1ppt</td><td>28,690</td><td>-25%</td><td>0.6%</td><td>-0.1ppt</td></tr><tr><td>Brilliance BMW</td><td>2,216</td><td>-56%</td><td>-6%</td><td>0.2%</td><td>-0.2ppt</td><td>0.0ppt</td><td>11,945</td><td>-59%</td><td>0.3%</td><td>-0.3ppt</td></tr><tr><td>Others</td><td>115,395</td><td>8%</td><td>14%</td><td>11.5%</td><td>1.9ppt</td><td>0.5ppt</td><td>511,705</td><td>8%</td><td>11.3%</td><td>2.3ppt</td></tr><tr><td>Total domestically produced NEV PV</td><td>1,000,484</td><td>-10%</td><td>9%</td><td></td><td></td><td></td><td>4,524,872</td><td>-14%</td><td></td><td></td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 2. Sector Volume and Penetration by Fuel Type (Domestically Produced)  
![](images/6b3d5d4731a285394777c8bfe59e66e030f02d682f6b5c967576bb2ca6daa7a2.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 3. BEV Insurance Retail Mkt Share by OEM (Domestically Produced)  
![](images/334a97b721e26a8fd269e6094d175aceb3f8ef4e03cbcfa18a6135d3808db324.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Thinkercar

Figure 4. PHEV Insurance Retail Mkt Share by OEM (Domestically Produced)  
![](images/036dd68cad558d6ec41bbd41f2cf1bb9d0eec0b53f7533363cf238afa18ecc96.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Thinkercar

Figure 5. EREV Insurance Retail Mkt Share by OEM (Domestically Produced)  
![](images/2ca8caf0d2351b1086278944f47451cf6ca7f472779fdbd7861925afe68c9c43.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 6. ICE Insurance Retail Mkt Share by Series (Domestically Produced)  
![](images/538a431f24e3cc094c6f8a1f986c4078501baaeb62326499515b6ecffb2cfda4.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: Citi, Thinkercar

Figure 7. ICE Insurance Retail Mkt Share by Brand (Domestically Produced)  
![](images/3f8abc2c11d39b7bf162c69aee4f2e14bf9788ec16cc0191e22f7d60a8ce8bff.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 8. Tesla China Insurance Retail Summary

<table><tr><td></td><td>Jun-26</td><td>Jun-25</td><td>YoY</td><td>MoM</td><td>6M26</td><td>6M25</td><td>YoY</td></tr><tr><td>Domestically Produced</td><td>52,078</td><td>61,406</td><td>-15%</td><td>9%</td><td>238,885</td><td>264,651</td><td>-10%</td></tr><tr><td>Model 3</td><td>13,993</td><td>17,308</td><td>-19%</td><td>-25%</td><td>66,326</td><td>92,836</td><td>-29%</td></tr><tr><td>Model Y</td><td>30,442</td><td>44,098</td><td>-31%</td><td>21%</td><td>140,821</td><td>171,815</td><td>-18%</td></tr><tr><td>Model Y L EV</td><td>7,643</td><td>-</td><td>na</td><td>86%</td><td>31,738</td><td>-</td><td>na</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 9. PV/NEV/ICE Inventory

<table><tr><td>PV</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td>Wholesales volume (CPCA)</td><td>2,490,237</td><td>2,243,361</td><td>2,481,169</td><td>2,796,051</td><td>2,935,761</td><td>2,998,113</td><td>2,789,139</td><td>1,972,882</td><td>1,518,264</td><td>2,378,062</td><td>2,110,049</td><td>2,212,337</td><td>2,358,247</td></tr><tr><td>PV Insurance retail sales (Thinkercar)</td><td>2,093,395</td><td>1,799,515</td><td>1,942,913</td><td>2,204,735</td><td>2,064,746</td><td>1,989,610</td><td>2,268,881</td><td>1,509,640</td><td>1,115,794</td><td>1,435,144</td><td>1,340,343</td><td>1,468,652</td><td>1,660,019</td></tr><tr><td>Exports volume (CPCA)</td><td>480,964</td><td>484,150</td><td>499,341</td><td>528,082</td><td>550,544</td><td>600,768</td><td>587,930</td><td>580,690</td><td>554,644</td><td>688,049</td><td>766,497</td><td>786,547</td><td>876,742</td></tr><tr><td>Inventory level (units)</td><td>4,334,897</td><td>4,294,593</td><td>4,133,508</td><td>4,196,742</td><td>4,417,213</td><td>4,824,948</td><td>4,757,276</td><td>4,639,828</td><td>4,487,654</td><td>4,742,523</td><td>4,745,732</td><td>4,702,870</td><td>4,524,356</td></tr><tr><td>Inventory level (months)</td><td>2.1</td><td>2.4</td><td>2.1</td><td>1.9</td><td>2.1</td><td>2.4</td><td>2.1</td><td>3.1</td><td>4.0</td><td>3.3</td><td>3.5</td><td>3.2</td><td>2.7</td></tr></table>

<table><tr><td>PV (CPCA reported number)</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Inventory level (units)</td><td>3,320,000</td><td>3,290,000</td><td>3,160,000</td><td>3,280,000</td><td>3,410,000</td><td>3,790,000</td><td>3,650,000</td><td>3,570,000</td><td>3,330,000</td><td>3,450,000</td><td>3,540,000</td><td>3,480,000</td></tr><tr><td>Inventory level (days)</td><td>49</td><td>47</td><td>42</td><td>39</td><td>44</td><td>61</td><td>66</td><td>70</td><td>60</td><td>61</td><td>62</td><td>66</td></tr></table>

<table><tr><td>NEV-PV</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td>Wholesales volume (CPCA)</td><td>1,241,055</td><td>1,188,602</td><td>1,294,166</td><td>1,493,767</td><td>1,612,213</td><td>1,706,921</td><td>1,563,915</td><td>864,732</td><td>720,290</td><td>1,144,085</td><td>1,225,232</td><td>1,352,027</td><td>1,481,452</td></tr><tr><td>NEV Insurance retail sales (Thinkercar)</td><td>1,110,664</td><td>976,537</td><td>1,096,600</td><td>1,287,271</td><td>1,189,321</td><td>1,218,266</td><td>1,331,320</td><td>563,958</td><td>429,534</td><td>797,810</td><td>818,301</td><td>914,785</td><td>1,000,484</td></tr><tr><td>NEV Exports volume (CPCA)</td><td>197,511</td><td>217,814</td><td>203,560</td><td>211,806</td><td>238,030</td><td>284,094</td><td>272,663</td><td>289,543</td><td>269,229</td><td>342,884</td><td>406,743</td><td>424,464</td><td>499,120</td></tr><tr><td>Inventory level (units)</td><td>1,842,449</td><td>1,836,700</td><td>1,630,706</td><td>1,625,396</td><td>1,710,258</td><td>1,914,819</td><td>1,874,751</td><td>1,885,982</td><td>1,907,509</td><td>1,910,900</td><td>1,911,088</td><td>1,923,866</td><td>1,905,714</td></tr><tr><td>Inventory level (month)</td><td>1.7</td><td>1.9</td><td>1.5</td><td>1.3</td><td>1.4</td><td>1.6</td><td>1.4</td><td>3.3</td><td>4.4</td><td>2.4</td><td>2.3</td><td>2.1</td><td>1.9</td></tr></table>

<table><tr><td>ICE-PV</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td>Wholesales volume (CPCA)</td><td>1,249,182</td><td>1,054,759</td><td>1,187,003</td><td>1,302,284</td><td>1,323,548</td><td>1,291,192</td><td>1,225,224</td><td>1,108,150</td><td>797,974</td><td>1,233,977</td><td>884,817</td><td>860,310</td><td>876,795</td></tr><tr><td>Insurance retail sales (Thinkercar)</td><td>982,731</td><td>822,978</td><td>846,313</td><td>917,464</td><td>875,425</td><td>771,344</td><td>937,561</td><td>945,682</td><td>686,260</td><td>637,334</td><td>522,042</td><td>553,867</td><td>659,535</td></tr><tr><td>Exports volume (CPCA)</td><td>283,453</td><td>266,336</td><td>295,781</td><td>316,276</td><td>312,514</td><td>316,674</td><td>315,267</td><td>291,147</td><td>285,415</td><td>345,165</td><td>359,754</td><td>362,083</td><td>377,622</td></tr><tr><td>Inventory level (units)</td><td>2,492,448</td><td>2,457,893</td><td>2,502,802</td><td>2,571,346</td><td>2,706,955</td><td>2,910,129</td><td>2,882,525</td><td>2,753,846</td><td>2,580,145</td><td>2,831,623</td><td>2,834,644</td><td>2,779,004</td><td>2,618,642</td></tr><tr><td>Inventory level (month)</td><td>2.5</td><td>3.0</td><td>3.0</td><td>2.8</td><td>3.1</td><td>3.8</td><td>3.1</td><td>2.9</td><td>3.8</td><td>4.4</td><td>5.4</td><td>5.0</td><td>4.0</td></tr></table>

Source: Citi Estimates, Thinkercar, CPCA

Figure 10. NEV Insurance Retail Mkt Share by Brand (Domestically Produced)
NEV Market Share by Series  
![](images/bf0c2eba52c2e02e1917e938302c6b8e34722654410e6cbe8ddb794252a2b2d4.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

## Companies Mentioned:

BAIC Motor (1958.HK; HK\$0.79; 2; 10 Jul 26; 16:10) | Brilliance (1114.HK; HK\$1.99; 1H; 10 Jul 26; 16:10) | BYD (1211.HK; HK\$84.9; 1; 10 Jul 26; 16:10) | BYD (002594.SZ; Rmb90.0; 1; 10 Jul 26; 15:00) | Chery (9973.HK; HK\$26.76; 1; 10 Jul 26; 16:10) | Chongqing Changan Automobile (000625.SZ; Rmb7.11; 2; 10 Jul 26; 15:00) |

DongFeng Automobile Co Ltd (600006.SS; Rmb5.27; Not Rated; 10 Jul 26; 15:00) | Geely Automobile (0175.HK; HK\$18.64; 1; 10 Jul 26; 16:10) | Great Wall Motor (2333.HK; HK\$8.64; 1; 10 Jul 26; 16:10) | Great Wall Motor (601633.SS; Rmb15.26; 3; 10 Jul 26; 15:00) | Guangzhou Automobile (2238.HK; HK\$2.19; 2; 10 Jul 26; 16:10) | Guangzhou Automobile (601238.SS; Rmb5.19; 2; 10 Jul 26; 15:00) | Leapmotor (9863.HK; HK\$37.74; 1; 10 Jul 26; 16:10) | Li Auto (LI.O; US\$12.1; 2; 10 Jul 26; 16:00) | Li Auto Inc (2015.HK; HK\$47.42; 2; 10 Jul 26; 16:10) | NIO (NIO.N; US\$4.78; 1; 10 Jul 26; 16:00) | NIO (9866.HK; HK\$38.66; 1; 10 Jul 26; 16:10) | SAIC Motor (600104.SS; Rmb10.12; 2; 10 Jul 26; 15:00) | Seres Group (601127.SS; Rmb59.9; 3; 10 Jul 26; 15:00) | Seres Group (9927.HK; HK\$47.8; 2; 10 Jul 26; 16:10) | Tesla (TSLA.O; US\$407.76; Not Rated; 10 Jul 26; 16:00) | Xiaomi (1810.HK; HK\$25.84; 1; 10 Jul 26; 16:10) | XPeng (XPEV.N; US\$13.03; 1; 10 Jul 26; 16:00) | XPeng (9868.HK; HK\$51.2

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing

such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
