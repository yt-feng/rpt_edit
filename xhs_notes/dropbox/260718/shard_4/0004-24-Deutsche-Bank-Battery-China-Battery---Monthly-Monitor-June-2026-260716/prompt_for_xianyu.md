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
Asia China

Consumer Autos & Auto Technology

Industry Battery

# China Battery – Monthly Monitor: June 2026

This chartbook tracks monthly volumes and price data for China electric-vehicle (xEV) batteries and energy storage system (ESS) batteries, including upstream materials.

Date 16 July 2026

Industry Update

Wei Huang
Research Associate
+852-2203-7057

Bin Wang

Research Analyst

+852-220-35496

Figure 1: China xEV and ESS battery volume summary

<table><tr><td>Volume</td><td>Jun-26</td><td>YoY</td><td>MoM</td><td>6M 2026</td><td>YoY</td></tr><tr><td colspan="6">Production (GwH)</td></tr><tr><td>Total xEX &amp; ESS battery Production</td><td>206.0</td><td>59%</td><td>7%</td><td>1,068.9</td><td>53%</td></tr><tr><td>xEX &amp; ESS battery (LFP)</td><td>169.2</td><td>70%</td><td>9%</td><td>874.8</td><td>58%</td></tr><tr><td>xEX &amp; ESS battery (NCM)</td><td>36.6</td><td>24%</td><td>3%</td><td>193.3</td><td>34%</td></tr><tr><td>xEX &amp; ESS battery (Others)</td><td>0.2</td><td>0%</td><td>-33%</td><td>0.9</td><td>-10%</td></tr><tr><td colspan="6">Sales (GwH)</td></tr><tr><td>Total xEX &amp; ESS battery Sales</td><td>196.0</td><td>49%</td><td>8%</td><td>979.5</td><td>49%</td></tr><tr><td>Total ESS battery Sales</td><td>62.6</td><td>67%</td><td>13%</td><td>318.1</td><td>83%</td></tr><tr><td>Total xEX battery Sales</td><td>133.4</td><td>42%</td><td>5%</td><td>661.2</td><td>36%</td></tr><tr><td>xEX battery (LFP)</td><td>99.8</td><td>46%</td><td>4%</td><td>488.1</td><td>38%</td></tr><tr><td>xEX battery (NCM)</td><td>33.4</td><td>31%</td><td>7%</td><td>172.3</td><td>33%</td></tr><tr><td>xEX battery (Others)</td><td>0.2</td><td>0%</td><td>100%</td><td>0.9</td><td>-10%</td></tr><tr><td colspan="6">Export (GwH)</td></tr><tr><td>Total xEX &amp; ESS battery export</td><td>36.2</td><td>48%</td><td>24%</td><td>181.3</td><td>42%</td></tr><tr><td>Total ESS battery export</td><td>10.7</td><td>26%</td><td>16%</td><td>58.5</td><td>28%</td></tr><tr><td>Total xEX battery export</td><td>25.5</td><td>61%</td><td>27%</td><td>122.7</td><td>50%</td></tr><tr><td>xEX battery (LFP)</td><td>13.9</td><td>104%</td><td>22%</td><td>62.4</td><td>88%</td></tr><tr><td>xEX battery (NCM)</td><td>11.5</td><td>28%</td><td>34%</td><td>59.7</td><td>24%</td></tr><tr><td>xEX battery (Others)</td><td>0.1</td><td>9900%</td><td>0%</td><td>0.5</td><td>0%</td></tr><tr><td colspan="6">Installment (GwH)</td></tr><tr><td>Total xEX battery</td><td>76.5</td><td>31%</td><td>6%</td><td>335.6</td><td>12%</td></tr><tr><td>xEX battery (LFP)</td><td>63.7</td><td>34%</td><td>9%</td><td>272.0</td><td>12%</td></tr><tr><td>xEX battery (NCM)</td><td>12.7</td><td>19%</td><td>-5%</td><td>63.4</td><td>14%</td></tr><tr><td colspan="6">By battery maker</td></tr><tr><td>CATL</td><td>32.6</td><td>28%</td><td>-1%</td><td>154.3</td><td>20%</td></tr><tr><td>BYD</td><td>14.1</td><td>13%</td><td>19%</td><td>57.4</td><td>-18%</td></tr><tr><td>CALB</td><td>5.2</td><td>18%</td><td>21%</td><td>20.7</td><td>6%</td></tr><tr><td>EVE</td><td>4.5</td><td>76%</td><td>38%</td><td>16.8</td><td>38%</td></tr><tr><td>Gotion</td><td>5.0</td><td>70%</td><td>12%</td><td>20.8</td><td>34%</td></tr><tr><td>Zenergy</td><td>2.1</td><td>62%</td><td>-10%</td><td>9.1</td><td>52%</td></tr></table>

Figure 2: China battery and battery material price summary

<table><tr><td>Price</td><td></td><td>Jun-26</td><td>YoY</td><td>MoM</td></tr><tr><td colspan="5">Battery price</td></tr><tr><td>NCM battery cell (xEV)</td><td>Rmb / Wh</td><td>0.60</td><td>54%</td><td>0%</td></tr><tr><td>LFP battery cell (xEV)</td><td>Rmb / Wh</td><td>0.39</td><td>18%</td><td>0%</td></tr><tr><td>Pouch NCM battery cell (xEV)</td><td>Rmb / Wh</td><td>0.61</td><td>45%</td><td>0%</td></tr><tr><td>LFP (Energy Storage)</td><td>Rmb / Wh</td><td>0.37</td><td>19%</td><td>0%</td></tr><tr><td>LCO (Consumer)</td><td>Rmb / Ah</td><td>8.40</td><td>51%</td><td>1%</td></tr><tr><td>NCM battery pack (xEV)</td><td>Rmb / Wh</td><td>0.76</td><td>46%</td><td>0%</td></tr><tr><td>LFP battery pack (xEV)</td><td>Rmb / Wh</td><td>0.51</td><td>19%</td><td>0%</td></tr><tr><td colspan="5">Precursor</td></tr><tr><td>LFP</td><td>Rmb 10K / ton</td><td>1.48</td><td>38%</td><td>8%</td></tr><tr><td>NCM111</td><td>Rmb 10K / ton</td><td>12.90</td><td>64%</td><td>0%</td></tr><tr><td>NCM523</td><td>Rmb 10K / ton</td><td>11.05</td><td>43%</td><td>0%</td></tr><tr><td>NCM622</td><td>Rmb 10K / ton</td><td>11.00</td><td>38%</td><td>0%</td></tr><tr><td>NCM811</td><td>Rmb 10K / ton</td><td>11.85</td><td>35%</td><td>1%</td></tr><tr><td colspan="5">Cathode Material</td></tr><tr><td>NCM622</td><td>Rmb 10K / ton</td><td>19.15</td><td>58%</td><td>-2%</td></tr><tr><td>NCM523</td><td>Rmb 10K / ton</td><td>19.41</td><td>72%</td><td>-1%</td></tr><tr><td>LFP</td><td>Rmb 10K / ton</td><td>6.06</td><td>90%</td><td>-5%</td></tr><tr><td colspan="5">Anode Material</td></tr><tr><td>Graphite (high-end) 300 mm</td><td>Rmb 10K / ton</td><td>1.75</td><td>20%</td><td>1.2%</td></tr><tr><td>Graphite (high-end) 350 mm</td><td>Rmb 10K / ton</td><td>1.78</td><td>22%</td><td>1.2%</td></tr><tr><td>Graphite (high-end) 400 mm</td><td>Rmb 10K / ton</td><td>1.79</td><td>19%</td><td>1.2%</td></tr><tr><td>Graphite (high-end) 450 mm</td><td>Rmb 10K / ton</td><td>1.80</td><td>18%</td><td>1.2%</td></tr><tr><td>Graphite (high-end) 500 mm</td><td>Rmb 10K / ton</td><td>1.80</td><td>16%</td><td>1.2%</td></tr><tr><td>Graphite (high-end) 600 mm</td><td>Rmb 10K / ton</td><td>1.85</td><td>16%</td><td>1.2%</td></tr><tr><td colspan="5">Separator</td></tr><tr><td>Separator (7μm+2μm)</td><td>Rmb / square meter</td><td>1.20</td><td>12%</td><td>2%</td></tr><tr><td>Separator (9μm+3μm)</td><td>Rmb / square meter</td><td>1.18</td><td>11%</td><td>2%</td></tr><tr><td>Separator (12μm+4μm)</td><td>Rmb / square meter</td><td>1.18</td><td>19%</td><td>0%</td></tr><tr><td colspan="5">Electrolyte</td></tr><tr><td>Lithium electrolyte salts (LiPF6)</td><td>Rmb 10K / ton</td><td>11.33</td><td>118%</td><td>2%</td></tr><tr><td>Electrolyte (NCM 2.6 Ah)</td><td>Rmb 10K / ton</td><td>2.72</td><td>40%</td><td>3%</td></tr><tr><td>Electrolyte (NCM 2.2 Ah)</td><td>Rmb 10K / ton</td><td>2.50</td><td>45%</td><td>3%</td></tr><tr><td>Electrolyte (LFP)</td><td>Rmb 10K / ton</td><td>1.53</td><td>0%</td><td>0%</td></tr><tr><td colspan="5">Lithium</td></tr><tr><td>Lithium Carbonate price</td><td>Rmb 10K / ton</td><td>16.45</td><td>172%</td><td>-12%</td></tr><tr><td>Lithium Hydroxide price</td><td>Rmb 10K / ton</td><td>15.05</td><td>151%</td><td>-13%</td></tr></table>

Source : Wind, China Automotive Power Battery Industry Innovation Alliance (CAPBIIA)

Figure 3: China xEV and ESS battery production volume summary

<table><tr><td colspan="6">Battery production</td></tr><tr><td>GwH</td><td>Jun-26</td><td>YoY</td><td>MoM</td><td>6M 2026</td><td>YoY</td></tr><tr><td colspan="6">Battery Production</td></tr><tr><td>Total xEX &amp; ESS battery Production</td><td>206.00</td><td>59%</td><td>7%</td><td>1,068.90</td><td>53%</td></tr><tr><td>xEX &amp; ESS battery (LFP)</td><td>169.20</td><td>70%</td><td>9%</td><td>874.80</td><td>58%</td></tr><tr><td>xEX &amp; ESS battery (NCM)</td><td>36.60</td><td>24%</td><td>3%</td><td>193.30</td><td>34%</td></tr><tr><td>xEX &amp; ESS battery (Others)</td><td>0.20</td><td>0%</td><td>-33%</td><td>0.90</td><td>-10%</td></tr></table>

Source: Wind, CAPBIIA

Figure 4: China xEV and ESS battery production volume trend  
![](images/5021067ee7c56376f11a97290139f11b8ac545956d901dcd6edd7a1a5928001e.jpg)  
Source: Wind, CAPBIIA

Figure 5: China xEV and ESS battery production volume trend by product  
![](images/cfdf0b4ebd12ce88cdbd069685828c923a1c4d6c5988e1e2d770782959f728c9.jpg)  
Source: Wind, CAPBIIA

Figure 6: China xEV and ESS battery sales volume summary

<table><tr><td colspan="6">Battery sales</td></tr><tr><td>GwH</td><td>Jun-26</td><td>YoY</td><td>MoM</td><td>6M 2026</td><td>YoY</td></tr><tr><td colspan="6">Battery Sales</td></tr><tr><td>Total xEX &amp; ESS battery Sales</td><td>196.00</td><td>49%</td><td>8%</td><td>979.50</td><td>49%</td></tr><tr><td>Total ESS battery Sales</td><td>62.60</td><td>67%</td><td>13%</td><td>318.10</td><td>83%</td></tr><tr><td>Total xEX battery Sales</td><td>133.40</td><td>42%</td><td>5%</td><td>661.20</td><td>36%</td></tr><tr><td>xEX battery (LFP)</td><td>99.80</td><td>46%</td><td>4%</td><td>488.10</td><td>38%</td></tr><tr><td>xEX battery (NCM)</td><td>33.40</td><td>31%</td><td>7%</td><td>172.30</td><td>33%</td></tr><tr><td>xEX battery (Others)</td><td>0.20</td><td>0%</td><td>100%</td><td>0.90</td><td>-10%</td></tr></table>

Figure 7: China xEV and ESS battery sales volume trend  
![](images/5b8d8d3597edac25855db0b03b3ecb621e2fdcc95758a1d3fdbf57bf5045387a.jpg)

Source: Wind, CAPBIIA

Figure 8: China xEV and ESS battery sales volume trend by segment  
![](images/50d01728e9126d2ee53c877e0990f342a092accc7e34dfe2901857e82879ba32.jpg)  
Source: Wind, CAPBIIA

Figure 9: China xEV battery sales volume trend by product  
![](images/5dc36c67d4b7da6cf211c4ce23e8813b2219b765018aed45e0e3973b641bc2c2.jpg)

Figure 10: China xEV and ESS battery export volume summary

<table><tr><td colspan="6">Battery Export</td></tr><tr><td>GwH</td><td>Jun-26</td><td>YoY</td><td>MoM</td><td>6M 2026</td><td>YoY</td></tr><tr><td colspan="6">Battery Export</td></tr><tr><td>Total xEX &amp; ESS battery export</td><td>36.20</td><td>48%</td><td>24%</td><td>181.30</td><td>42%</td></tr><tr><td>Total ESS battery export</td><td>10.70</td><td>26%</td><td>16%</td><td>58.50</td><td>28%</td></tr><tr><td>Total xEX battery export</td><td>25.50</td><td>61%</td><td>27%</td><td>122.70</td><td>50%</td></tr><tr><td>xEX battery (LFP)</td><td>13.90</td><td>104%</td><td>22%</td><td>62.40</td><td>88%</td></tr><tr><td>xEX battery (NCM)</td><td>11.50</td><td>28%</td><td>34%</td><td>59.70</td><td>24%</td></tr><tr><td>xEX battery (Others)</td><td>0.10</td><td>9900%</td><td>0%</td><td>0.50</td><td>0%</td></tr></table>

Figure 11: China xEV and ESS battery export volume trend  
![](images/5986348fc7a5b009b90c5d31d5d609978c5a5a128f3bbe2119ed061f4b60077f.jpg)

Source: Wind, CAPBIIA

Figure 12: China xEV and ESS battery export volume trend by segment  
![](images/d662fff00303c249f643c3d14e41d9970a66a9311efbd13c395484f48bc8efb6.jpg)  
Source: Wind, CAPBIIA

Figure 13: China xEV battery export volume trend by product  
![](images/7e89bb9ee0cb41324f524d11943324b6bc30e4f43af9e25975ea75dbe3ba9ccb.jpg)  
Source: Wind, CAPBIIA

Figure 14: China xEV battery installation volume summary

<table><tr><td colspan="6">Battery installment</td></tr><tr><td>GwH</td><td>Jun-26</td><td>YoY</td><td>MoM</td><td>6M 2026</td><td>YoY</td></tr><tr><td colspan="6">Battery Installment</td></tr><tr><td>Total xEX battery</td><td>76.50</td><td>31%</td><td>6%</td><td>335.60</td><td>12%</td></tr><tr><td>xEX battery (LFP)</td><td>63.70</td><td>34%</td><td>9%</td><td>272.00</td><td>12%</td></tr><tr><td>xEX battery (NCM)</td><td>12.70</td><td>19%</td><td>-5%</td><td>63.40</td><td>14%</td></tr><tr><td>xEX battery (Others)</td><td>0.10</td><td>0%</td><td>0%</td><td>0.21</td><td>111%</td></tr><tr><td colspan="6">Source: Wind, CAPBIIA</td></tr></table>

Figure 15: China xEV battery installation volume trend  
![](images/b70ff6bb317093fce2e25f2189baa9d5d1c3ae344abca92c46a71d158e225be1.jpg)

Figure 16: China xEV battery installation volume trend by product  
![](images/70ceaa1a340d7b9dce74f80c59173b4b1fab424a177564cb6759ffa9291639dd.jpg)

![](images/67edee96d280a1ef1d35683bd370b8f2991cc3946150d6cf415f267b75026e23.jpg)  
Source: Wind, CAPBIIA

Figure 18: BYD's domestic battery installation volume  
![](images/88c8f47d281cdb3f35d318824e88c94df679fb067540aa59dfedbc8133de0e4d.jpg)

Figure 19: CALB's domestic battery installation volume  
![](images/03161957eab4c7b94d5bd9c5151f7efe28ec72e15b819f4d91879440a8210837.jpg)  
Source: Wind, CAPBIIA  
Source: Wind, CAPBIIA

Figure 20: Gotion's domestic battery installation volume  
![](images/3320e25249c04c0dc786141a621344a6c98008e1f8f4b10dc5a1b16db5355c65.jpg)  
Source: Wind, CAPBIIA

Source: Wind, CAPBIIA, DB estimates

![](images/690d587e0752c33c6691c452bf73bc05f27b69550492859225bed615acb33e26.jpg)  
Source: Wind, CAPBIIA

![](images/8bab9ac7d5a6fe5a4c86735f396405be5d3bd4f712e1258f9abb8cc853c90542.jpg)  
Source: Wind, CAPBIIA

![](images/c4ac5750f47f24b98dcb3adc91d126637130068f7aa13bfe03f62022c050c106.jpg)  
Source: Wind, CAPBIIA

![](images/7823650f64aee43b783f04a20608ecabeea3e2c1809ade778b8b5a51a7d293a4.jpg)  
Source: Wind, CAPBIIA

![](images/d54017dfee2e87efdcdc0bf11ab046426bf21762af40df5c9233698f0ef6269e.jpg)  
Source: Wind, CAPBIIA

Figure 28: Lithium product price trend  
![](images/d7126040fce8bd7aea9887b5da4d766dcac71535b4ff41975ff9c10bae2e86c5.jpg)  
Source: Wind, CAPBIIA

![](images/9d822f590f53e0a1bb257acc47844af551fc826de368c2e8df08bf8f9be6bc88.jpg)  
Source: Wind, CAPBIIA

![](images/a7acb89d716ef4849354addb389dce64f7cb5ce996ec27f33f0d8d4b9f1ac06c.jpg)  
Source: Wind, CAPBIIA

Figure 31: Precursor price trend by product  
![](images/a06c2bdff4b35ee1025ca7bdfad337c6d0ed14932bbf1f1a6c648d144c87fd48.jpg)  
Source: Wind, CAPBIIA

![](images/a30bf53115be876f7b0fed61525e8220a068aaea87b7a47d2381399f46a662af.jpg)  
Source: Wind, CAPBIIA

![](images/3e5847f1d197070a199fcffab6d5e7cfe7089a36713f47ce18bb6db43178f3bb.jpg)  
Source: Wind, CAPBIIA

![](images/e1a80d014bc86028d406f6560d3d737e0a7d7cfe950bb06ce30ebe66c1a0db54.jpg)  
Source: Wind, CAPBIIA

Figure 35: Anode material normal graphite 300mm price trend  
![](images/c12dba5dc77a6bff243c707b5f47e1cff079df0c4d6f8f3b70ec8ad6cf8ffa4e.jpg)  
Source: Wind, CAPBIIA

Figure 36: Anode material price trend by product  
![](images/2e8e5e1d7a81a36616b6c1d35fbc82dfbbbf1b3da147615e9a127f97d66945b8.jpg)  
Source: Wind, CAPBIIA

Figure 37: Separator (12μm+4μm) price trend  
![](images/c1092849ca15bfceee106074ca1b4242d4c1acdb69ac318e595fbed04b2229af.jpg)  
Source: Wind, CAPBIIA

Figure 38: Separator price trend by product  
![](images/73ab33b03cf52f9e79236032fb6ff38a3864981b09e6b616ac5d870eba56d563.jpg)  
Source: Wind, CAPBIIA

![](images/c81061a0bb9ddb5fd39e2acda2a56ec5f132247dce1d831f17ab80b28afce15e.jpg)  
Source: Wind, CAPBIIA

![](images/aa686416ed83eba8b39a0642c4fca34b554369adf23e0bb8feb49cd5a85b07a9.jpg)

# Appendix 1

Important Disclosures

\*Other information available upon request

\*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst about the subject issuers and the securities of those issuers. In addition, the undersigned lead analyst has not and will not receive any compensation for providing a specific recommendation or view in this report. Wei Huang, Bin Wang.

![](images/7fa14835b2353142a196e4d8e3f168f4650bc7ddeb2a5ee17698902c4195451b.jpg)  
Equity Rating and Dispersion Key  
The Equity Rating Dispersion Chart depicts the following:

The proportion of recommendations that are rated "buy", "sell" and "hold" over the previous 12 months. This is shown for securities issued in the stated region e.

[中间内容因长度限制已省略]

er items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
