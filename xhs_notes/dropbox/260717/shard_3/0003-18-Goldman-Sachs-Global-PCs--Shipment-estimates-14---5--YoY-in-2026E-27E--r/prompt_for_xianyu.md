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
# Global PCs: Shipment estimates -14% / -5% YoY in 2026E-27E; rising AI PC penetration

We further trim our global PC shipment estimates for 2026-27E, considering the near-term pressures of higher memory and CPU costs, and the flattening replacement cycle following the end of Win 10. We now expect global PC shipments to be down -14%/ -5% YoY in 2026E/ 27E, followed by zero growth in 2028E (vs. -10%/ +3%/ +3% YoY previously). Our updated PC shipment forecasts are 255m/ 243m/ 244m in 2026-28E, respectively.

As raw material costs increase, we expect AI PC to outperform given their lower sensitivity to price increases and the increasing need for AI edge computing. We model AI PC shipments to be 150m / 175m/ 199m in 2026-28E (+39% / +17%/ +14% YoY), representing 59% / 72%/ 82% penetration (penetration ratio largely unchanged). Our updated PC TAM model is based on the latest GS forecasts for key suppliers including Apple, Lenovo, HP, Dell, ASUS, Samsung, Microsoft, LG, Xiaomi and Gigabyte. Details within.

Exhibit 1: Taiwan ODM Notebook: shipment MoM increase in Jun on better seasonality  
![](images/a6be64ea7caa758f8362671e0869f2602bc27333825b56e64f57586e648dcd89.jpg)  
Source: Company data

Related reports:

Global Tech: PCs, smartphones, servers: Quantifying market opportunities (Launching Global TAMs on Oct 3, 2023)

Global Tech: PC/Server/Smartphone TAM updates: PC +5%, General server +3%, AI server +57%, Smartphone +3% YoY in 2025E (Updates on June 12, 2024)

## Allen Chang

+852-2978-2930 | allen.k.chang@gs.com GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Katherine Murphy
+1(212)902-1151 |
katherine.a.murphy@gs.com
GS & Co. LLC

Michael Ng, CFA
+1(212)902-8618 | michael.ng@gs.com
GS & Co. LLC

James Schneider, Ph.D.
+1(212)357-2929 |
jim.schneider@gs.com
GS & Co. LLC

Gabriela Borges, CFA
+1(212)902-7839 |
gabriela.borges@gs.com
GS & Co. LLC

Daiki Takayama
+81(3)4587-9870 |
daiki.takayama@gs.com
GS Japan Co., Ltd.

Giuni Lee
+82(2)3788-1177 | giuni.lee@gs.com
GS (Asia) L.L.C., Seoul Branch

Timothy Zhao
+852-2978-2673 |
timothy.zhao@gs.com
GS (Asia) L.L.C.

Chao Wang
+886(2)2730-4195 | kuan-
chao.wang@gs.com
GS (Asia) L.L.C., Taipei
Branch

Ting Song
+852-2978-6466 | ting.song@gs.com
GS (Asia) L.L.C.

Yifan Hu
+852-2978-0996 | yifan.hu@gs.com
GS (Asia) L.L.C.

Zorayda Montemayor
+1(212)357-6403 |
zorayda.montemayor@gs.com
GS & Co. LLC

Anmol Makkar
+1(212)357-1366 |
anmol.makkar@gs.com
GS & Co. LLC

Selina Zhang
+1(212)357-9979

Global Tech: PC TAM +2% / +3% YoY in 2024E / 2025E; AI PC new models in Sep-Oct (Updates on Oct 21, 2024)

Global Tech: PC TAM +4% / +4% YoY in 2025E / 2026E; AI PC to account for 31% / 50% of shipment (Updates on Feb 19, 2025)

Global Tech: PC TAM +2% / +3% YoY in 2025E / 2026E; AI PC shipments ramping up (Updates on May 12, 2025)

Global Tech: PC TAM +3% / +3% YoY in 2025E / 2026E; AI PC/ Gaming PC drive mix upgrade (Updates on Aug 22, 2025)

Global PCs: TAM +3% / +3% YoY in 2025E / 26E; Gaming PCs at 11% / 13% penetration rate in 2025/28E (Updates on Dec 13, 2025)

Global PCs: Trimming to -5% / +3% YoY in 2026E / 27E; AI PC remains the growth driver (Updates on Jan 23, 2026)

Global PCs: Shipment -10% / +2% YoY in 2026E / 27E; AI PC will outperform (Updates on Mar 14, 2026)

## PCs: -14% / -5% YoY in 2026E-27E

## Global PCs market opportunity

(Shipments in m units)

Our Bottom up method

Global PCs shipments = sum of shipments by brands

Global PCs revenues = Desktops ASP x shipments + Notebooks ASP x shipments + Workstations ASP x shipments

PCs shipments by region (2025)

![](images/e3fbe742dc777757d3847d9a31123456c1c8400862c7ad8fe436a2aa2463428c.jpg)  
PCs shipments growth by region

![](images/ba56b5d908f2f803e469e82e8132f9018391ae8ae79e78e32f182cfbf4ea291f.jpg)

![](images/186e77ea3066f9b5c7a2fcc983f23abfcfd7d93e8d7dbcc8ebf275454203fd2f.jpg)

![](images/9ecb84a1c107c5b2a998f11005fd713573eee92cfd5a3df951ab019573a12657.jpg)  
Western Europe YoY

![](images/fa0a43fc3d06f82043bfd54c227f91c753b2b997fa2f7b226ad4afbb5f212bf5.jpg)

<table><tr><td>Shipments by product</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Global PCs shipments (m units)</td><td>66</td><td>72</td><td>79</td><td>81</td><td>68</td><td>61</td><td>63</td><td>63</td><td>260</td><td>269</td><td>297</td><td>255</td><td>243</td><td>244</td></tr><tr><td>Desktops</td><td>18</td><td>19</td><td>22</td><td>23</td><td>18</td><td>16</td><td>17</td><td>17</td><td>72</td><td>72</td><td>84</td><td>69</td><td>62</td><td>61</td></tr><tr><td>Notebooks</td><td>46</td><td>50</td><td>54</td><td>55</td><td>47</td><td>43</td><td>44</td><td>44</td><td>181</td><td>188</td><td>205</td><td>178</td><td>173</td><td>176</td></tr><tr><td>Workstations</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>7</td><td>8</td><td>8</td><td>8</td><td>7</td><td>7</td></tr><tr><td>YoY</td><td>8%</td><td>10%</td><td>11%</td><td>12%</td><td>3%</td><td>-15%</td><td>-19%</td><td>-22%</td><td>-14%</td><td>3%</td><td>10%</td><td>-14%</td><td>-5%</td><td>0%</td></tr><tr><td>Desktops</td><td>10%</td><td>12%</td><td>19%</td><td>19%</td><td>-2%</td><td>-16%</td><td>-23%</td><td>-26%</td><td>-16%</td><td>0%</td><td>15%</td><td>-18%</td><td>-10%</td><td>-3%</td></tr><tr><td>Notebooks</td><td>9%</td><td>9%</td><td>8%</td><td>10%</td><td>4%</td><td>-15%</td><td>-18%</td><td>-20%</td><td>-13%</td><td>4%</td><td>9%</td><td>-13%</td><td>-3%</td><td>2%</td></tr><tr><td>Workstations</td><td>-28%</td><td>5%</td><td>4%</td><td>11%</td><td>21%</td><td>4%</td><td>-14%</td><td>-24%</td><td>-9%</td><td>21%</td><td>-4%</td><td>-4%</td><td>-11%</td><td>0%</td></tr><tr><td>Mix</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr><tr><td>Desktops</td><td>28%</td><td>27%</td><td>28%</td><td>29%</td><td>27%</td><td>27%</td><td>27%</td><td>27%</td><td>28%</td><td>27%</td><td>28%</td><td>27%</td><td>26%</td><td>25%</td></tr><tr><td>Notebooks</td><td>69%</td><td>70%</td><td>69%</td><td>68%</td><td>70%</td><td>70%</td><td>70%</td><td>70%</td><td>70%</td><td>70%</td><td>69%</td><td>70%</td><td>71%</td><td>72%</td></tr><tr><td>Workstations</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td></tr><tr><td>Revenues by product</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Global PCs revenues (US$ m)</td><td>60,032</td><td>65,945</td><td>73,876</td><td>76,757</td><td>68,768</td><td>61,822</td><td>65,214</td><td>65,622</td><td>222,164</td><td>240,238</td><td>276,610</td><td>261,426</td><td>255,904</td><td>262,519</td></tr><tr><td>Desktops</td><td>13,251</td><td>13,959</td><td>15,930</td><td>16,602</td><td>14,152</td><td>12,775</td><td>13,421</td><td>13,302</td><td>49,894</td><td>50,658</td><td>59,742</td><td>53,650</td><td>50,004</td><td>51,745</td></tr><tr><td>Notebooks</td><td>42,735</td><td>47,789</td><td>53,513</td><td>55,107</td><td>48,862</td><td>44,275</td><td>47,659</td><td>48,126</td><td>157,767</td><td>173,821</td><td>199,144</td><td>188,922</td><td>188,852</td><td>193,513</td></tr><tr><td>Workstations</td><td>4,046</td><td>4,197</td><td>4,433</td><td>5,048</td><td>5,753</td><td>4,772</td><td>4,135</td><td>4,195</td><td>14,503</td><td>15,759</td><td>17,724</td><td>18,855</td><td>17,048</td><td>17,261</td></tr><tr><td>YoY</td><td>15%</td><td>17%</td><td>13%</td><td>15%</td><td>15%</td><td>-6%</td><td>-12%</td><td>-15%</td><td>-16%</td><td>8%</td><td>15%</td><td>-5%</td><td>-2%</td><td>3%</td></tr><tr><td>Shipments by vendor</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Global PCs shipments (m units)</td><td>66</td><td>72</td><td>79</td><td>81</td><td>88</td><td>61</td><td>63</td><td>63</td><td>260</td><td>269</td><td>297</td><td>255</td><td>243</td><td>244</td></tr><tr><td>Lenovo</td><td>15</td><td>17</td><td>19</td><td>19</td><td>16</td><td>16</td><td>18</td><td>18</td><td>59</td><td>62</td><td>70</td><td>68</td><td>73</td><td>76</td></tr><tr><td>HP</td><td>13</td><td>14</td><td>14</td><td>15</td><td>12</td><td>12</td><td>11</td><td>12</td><td>54</td><td>54</td><td>56</td><td>47</td><td>46</td><td>47</td></tr><tr><td>Dell</td><td>10</td><td>9</td><td>9</td><td>11</td><td>9</td><td>9</td><td>8</td><td>8</td><td>37</td><td>39</td><td>39</td><td>34</td><td>31</td><td>31</td></tr><tr><td>Apple</td><td>6</td><td>6</td><td>7</td><td>7</td><td>6</td><td>7</td><td>8</td><td>8</td><td>22</td><td>23</td><td>26</td><td>29</td><td>33</td><td>34</td></tr><tr><td>ASUS</td><td>4</td><td>5</td><td>6</td><td>5</td><td>4</td><td>4</td><td>5</td><td>4</td><td>17</td><td>18</td><td>19</td><td>18</td><td>19</td><td>19</td></tr><tr><td>Samsung</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>8</td><td>8</td><td>8</td><td>6</td><td>7</td><td>7</td></tr><tr><td>Microsoft</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>LG</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Xiaomi</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Others</td><td>16</td><td>18</td><td>22</td><td>21</td><td>18</td><td>10</td><td>11</td><td>11</td><td>60</td><td>62</td><td>77</td><td>50</td><td>32</td><td>27</td></tr><tr><td>YoY</td><td>8%</td><td>10%</td><td>11%</td><td>12%</td><td>3%</td><td>-15%</td><td>-19%</td><td>-22%</td><td>-14%</td><td>3%</td><td>10%</td><td>-14%</td><td>-5%</td><td>0%</td></tr><tr><td>Global market share</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr><tr><td>Lenovo</td><td>23%</td><td>24%</td><td>24%</td><td>23%</td><td>23%</td><td>27%</td><td>29%</td><td>28%</td><td>23%</td><td>23%</td><td>24%</td><td>27%</td><td>30%</td><td>31%</td></tr><tr><td>HP</td><td>20%</td><td>19%</td><td>17%</td><td>19%</td><td>17%</td><td>20%</td><td>18%</td><td>19%</td><td>21%</td><td>20%</td><td>19%</td><td>19%</td><td>19%</td><td>19%</td></tr><tr><td>Dell</td><td>14%</td><td>12%</td><td>12%</td><td>13%</td><td>14%</td><td>14%</td><td>13%</td><td>12%</td><td>14%</td><td>15%</td><td>13%</td><td>13%</td><td>13%</td><td>13%</td></tr><tr><td>Apple</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td><td>11%</td><td>12%</td><td>13%</td><td>8%</td><td>9%</td><td>9%</td><td>11%</td><td>14%</td><td>14%</td></tr><tr><td>ASUS</td><td>6%</td><td>6%</td><td>7%</td><td>6%</td><td>6%</td><td>7%</td><td>8%</td><td>7%</td><td>6%</td><td>7%</td><td>6%</td><td>7%</td><td>8%</td><td>8%</td></tr><tr><td>Samsung</td><td>3%</td><td>3%</td><td>3%</td><td>2%</td><td>2%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td></tr><tr><td>Microsoft</td><td>1%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>0%</td><td>1%</td><td>1%</td><td>1%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>LG</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Xiaomi</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Others</td><td>24%</td><td>26%</td><td>28%</td><td>26%</td><td>27%</td><td>16%</td><td>17%</td><td>17%</td><td>23%</td><td>23%</td><td>26%</td><td>20%</td><td>13%</td><td>11%</td></tr><tr><td>ASP</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Global PC ASP (US$)</td><td>911</td><td>919</td><td>941</td><td>953</td><td>1,013</td><td>1,011</td><td>1,031</td><td>1,044</td><td>854</td><td>893</td><td>933</td><td>1,025</td><td>1,055</td><td>1,077</td></tr><tr><td>YoY</td><td>7%</td><td>7%</td><td>3%</td><td>2%</td><td>11%</td><td>10%</td><td>10%</td><td>9%</td><td>-2%</td><td>5%</td><td>4%</td><td>10%</td><td>3%</td><td>2%</td></tr><tr><td>AI PCs</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>AI PC shipment (m units)</td><td>18</td><td>23</td><td>30</td><td>37</td><td>35</td><td>36</td><td>39</td><td>40</td><td></td><td>52</td><td>108</td><td>150</td><td>175</td><td>199</td></tr><tr><td>YoY</td><td></td><td>89%</td><td>67%</td><td>71%</td><td>93%</td><td>58%</td><td>29%</td><td>9%</td><td></td><td></td><td>109%</td><td>39%</td><td>17%</td><td>14%</td></tr><tr><td>Penetration</td><td>27%</td><td>32%</td><td>39%</td><td>46%</td><td>51%</td><td>59%</td><td>62%</td><td>64%</td><td></td><td>19%</td><td>36%</td><td>59%</td><td>72%</td><td>82%</td></tr><tr><td>AI PC revenues (US$ m)</td><td>20,591</td><td>26,573</td><td>31,586</td><td>40,062</td><td>39,660</td><td>40,592</td><td>43,532</td><td>45,044</td><td></td><td>62,898</td><td>118,811</td><td>168,828</td><td>194,672</td><td>220,737</td></tr><tr><td>YoY</td><td></td><td>68%</td><td>50%</td><td>53%</td><td>93%</td><td>53%</td><td>38%</td><td>12%</td><td></td><td></td><td>89%</td><td>42%</td><td>15%</td><td>13%</td></tr><tr><td>Penetration</td><td>34%</td><td>40%</td><td>43%</td><td>52%</td><td>58%</td><td>66%</td><td>67%</td><td>69%</td><td></td><td>26%</td><td>43%</td><td>65%</td><td>76%</td><td>84%</td></tr><tr><td>Gaming PCs</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Gaming PC shipment (m units)</td><td>7</td><td>8</td><td>9</td><td>8</td><td>7</td><td>6</td><td>7</td><td>6</td><td></td><td>28</td><td>31</td><td>26</td><td>27</td><td>28</td></tr><tr><td>YoY</td><td>9%</td><td>16%</td><td>13%</td><td>15%</td><td>0%</td><td>-18%</td><td>-22%</td><td>-25%</td><td></td><td></td><td>13%</td><td>-17%</td><td>2%</td><td>6%</td></tr><tr><td>Penetration</td><td>10%</td><td>11%</td><td>11%</td><td>11%</td><td>10%</td><td>10%</td><td>11%</td><td>10%</td><td></td><td>10%</td><td>11%</td><td>10%</td><td>11%</td><td>12%</td></tr><tr><td>Gaming PC revenues (US$ m)</td><td>10,531</td><td>12,131</td><td>13,521</td><td>13,219</td><td>12,073</td><td>11,139</td><td>11,693</td><td>10,964</td><td></td><td>40,518</td><td>49,401</td><td>45,869</td><td>48,470</td><td>52,186</td></tr><tr><td>YoY</td><td>19%</td><td>27%</td><td>20%</td><td>23%</td><td>15%</td><td>-8%</td><td>-14%</td><td>-17%</td><td></td><td></td><td>22%</td><td>-7%</td><td>6%</td><td>8%</td></tr><tr><td>Penetration</td><td>18%</td><td>18%</td><td>18%</td><td>17%</td><td>18%</td><td>18%</td><td>18%</td><td>17%</td><td></td><td>17%</td><td>18%</td><td>18%</td><td>19%</td><td>20%</td></tr><tr><td>Shipments by markets</td><td>1Q25</td><td>2Q25

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
