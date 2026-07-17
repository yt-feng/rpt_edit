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
## China Oil, Gas and Chemical Sector Weekly tracker: Chemical stock index down 9% since June; PP/PVC/PFY inventory down WoW

## Refining: teapot refinery utilisation improved; crude inventory built

SOE refineries' average utilisation declined 0.12ppt WoW to 67.8% last week. Utilisation at teapot refineries recovered by 3.6ppt WoW to 46.58% as some refineries increased their utilisation on improving refining margins. China's total crude throughput declined 236kb/d WoW to 11,833kb/d last week. As per Kpler data, China crude inventory turned from a draw to a build last week (overall level at \~1,288mmbbl by this Monday).

## Chemicals: utilisation of PX declined sharply WoW

Ethylene: naphtha-based ethylene utilisation declined 2ppt WoW to 73% (down 7ppt YoY), while MTO route utilisation increased 2ppt WoW; it was down 4ppt YoY to 82%. Polyolefins: PE utilisation decreased 1/1ppt WoW/YoY to 79%, while PP utilisation increased 2ppt WoW to 66% (down 9ppt YoY). PDH utilisation was broadly flat WoW at 64%. PVC utilisation decreased 3ppt WoW from 68% to 65%. Aromatics chain: PX utilisation declined 7ppt WoW to 61% (down 19ppt YoY), while PTA utilisation decreased 4ppt WoW to 58% (down 23ppt YoY). Polyester filament utilisation was broadly flat WoW at 74% (down 15ppt YoY). TDI utilisation declined 3ppt WoW to 64%, while MDI/TiO2 utilisation was broadly flat WoW at 72%/78%.

## PP/PVC/Polyester filament inventory declined WoW

According to sample inventory data, PP inventory decreased 4% WoW and 30% YoY to 406kt. PE inventory increased 24% WoW but declined 11% YoY to 438kt. PVC inventory decreased 1% WoW and 19% YoY to 431kt. TiO2 inventory was up 4% WoW but down 35% YoY to 213kt. Polyester filament Yarn (PFY) inventory decreased 14% WoW but increased 37% YoY, while silicone DMC inventory rose 3% WoW but declined 9% YoY to 45kt.

## CCPI down 6% MoM in June; Chemical stock index down 9% since June

The China Chemicals Price Index (CCPI) fell 6% MoM in June, alongside the decline in crude oil prices. Chemical stock index has fallen 9% since June. Highlights: 1) The R22/R134a refrigerant average prices rose 30%/3% MoM, as high temperatures supported the continued release of maintenance demand. 2) In the aromatics chain, the PTA spread expanded sharply, up 302% MoM, while the polyester POY spread rose 4% MoM, mainly because intensive maintenance and continued destocking among PTA producers led to tighter PTA supply, while PX and polyester filament supply contracted to a lesser extent.

## Stock picks

We still prefer oil companies (PetroChina, Sinopec and CNOOC) with attractive dividend yields (see note). We also view selected chemical stocks' valuation as appealing after recent correction, including Wanhua, Baofeng, Asia-Potash and Dongyue. We will host our H226E chemical outlook expert call series this week and next week (Register here).

## Equities

China
Chemicals

Amily Guo
Analyst
amily.guo@ubs.com
+86-105-832 8845

Cheryl Wen
Analyst
S1460525030002
cheryl.wen@ubs.com
+86-21-3866 8916

Richard Li
Analyst
S1460121090003
richard-ze.li@ubs.com
+86-21-3866 8802

Nayoung Kim
Analyst
nayoung.kim@ubs.com
+44-20-7568 4010

Jay LIN

Analyst

S1460525070001

jay.lin@ubs.com

+86-105-832 8044

Crude inventory and refinery utilisation
Figure 1: China crude oil inventory  
![](images/8509b649840d43461923134b53ffdc32fc2616e123e3dfcb330f6b792e603d71.jpg)  
Source: Kpler, UBS

Figure 2: Utilisation of China SOE/teapot refiners  
![](images/d8a6fb6be21a29efa7edfe53773cb51cddce720d88ca29d9a19697cd1d8b33a1.jpg)  
Source: SCI99, Wind

Chemical utilisation  
Figure 3: China ethylene (naphtha cracking) capacity utilisation  
![](images/4bfd91ab4fb67b952b80d31916f72c5df17f172615357df0a850e90ae2d3d8e8.jpg)  
Source: Wind, Oilchem

Figure 4: China ethylene (MTO) capacity utilisation  
![](images/f21317cf546800c0a1e6c22aa9cc849874dce13fd4b881bd4364d5183cd62f3d.jpg)  
Source: Wind, Oilchem

Figure 5: China PE capacity utilisation  
![](images/83e72bf67329f87123595de32b790e5ec7672ef441a49df2388f2233d335a6b2.jpg)  
Source: Baiinfo

Figure 6: China PP capacity utilisation  
![](images/029e1255fabb3842abbb3660590d2d21d6a80debdefb5cf257b9447ea3797df4.jpg)  
Source: Baiinfo

Figure 7: China PVC capacity utilisation  
![](images/6d625ac6470fca4d17f9c971f7aac48933262d2f71f789cf9b9352a237ca96c8.jpg)  
Source: Baiinfo

Figure 8: China PDH capacity utilisation  
![](images/aa38fe21ef195651b32b18bf965a2670e269c5fddf93c2868b5336ceef74ceba.jpg)  
Source: Baiinfo

Figure 9: China PX capacity utilisation  
![](images/313bc3ea327bbeb9495fa23e5ead8b66b79b2bb43b3898e492a897fd7a9803f2.jpg)  
Source: Baiinfo

Figure 10: China PTA capacity utilisation  
![](images/8c12948525d81a9f45e473bd5619af6116bd82e859389f4d41dcd2fc9e501db7.jpg)  
Source: Baiinfo

Figure 11: China Polyester filament capacity utilisation  
![](images/0c128e0a93c3dbdc305073b505e52a09d0a3b23aea2deb32d4dcb9aa8b71968e.jpg)  
Source: Baiinfo

Figure 12: China MDI capacity utilisation  
![](images/77427b2195ecd69b7c6e50e7e99dc8b75cae8e7c1f3f59aa8286f8ce470ee3f1.jpg)  
Source: Baiinfo

Figure 13: China TDI capacity utilisation  
![](images/e82c42c73953395646f024a71f4dbee27fd4e84b665ed276d560e39b3217bd68.jpg)  
Source: Baiinfo

Figure 14: China TiO2 capacity utilisation  
![](images/f1e87b7b93ab89ce82728d93a372b75666785dbd696851d520129642827cc876.jpg)  
Source: Baiinfo

## Inventory

Figure 15: Sample factories' inventory of PP  
![](images/0e621deba75f18984c4ff5e172ce8b46087339f4cb1f82466ec3a09c99971ebb.jpg)  
Source: Baiinfo

Figure 16: Sample factories' inventory of PE  
![](images/d7fbfbdd3fceae6cbf8331ab19c34acd445a1cccea4ac101b944c3eda7d3382a.jpg)  
Source: Baiinfo

Figure 17: Sample factories' inventory of PVC  
![](images/dec8e92fb69877b7edebf38ebfc4251139494ac0a8239e758247c60862900221.jpg)  
Source: Baiinfo

Figure 18: Sample factories' inventory of TiO2  
![](images/842be37f37571d23785d5e91aa933102cea1808ae227746d8afefd8fa01ff781.jpg)  
Source: Baiinfo

Figure 19: Sample factories' inventory of polyester filament  
![](images/f2195ec2ab6c562dc45a20ed9f90905f64eadd3ee88d15418a45b2525c32077f.jpg)  
Source: Baiinfo

Figure 20: Sample factories' inventory of silicone DMC  
![](images/ebe411fc2216782670ff70df01682440164ff13636477bf7299e2e66e71321f5.jpg)  
Source: Baiinfo

Figure 21: Chemical product spreads in June 2026 (Rmb/t)

<table><tr><td>Category</td><td>Product</td><td>Jun avg</td><td>May avg</td><td>Year beginning</td><td>End-Jun</td><td>YoY</td><td>MoM</td><td>YTD</td></tr><tr><td rowspan="16">Olefins and plastics</td><td>Ethylene-crude</td><td>2,139</td><td>3,073</td><td>1,912</td><td>1,740</td><td>-12.3%</td><td>-30.4%</td><td>-9.0%</td></tr><tr><td>Propylene-crude</td><td>2,787</td><td>3,249</td><td>1,807</td><td>2,421</td><td>80.2%</td><td>-14.2%</td><td>34.0%</td></tr><tr><td>Ethylene-Naphtha</td><td>1,761</td><td>1,982</td><td>1,585</td><td>1,169</td><td>-10.5%</td><td>-11.2%</td><td>-26.2%</td></tr><tr><td>Propylene-Naphtha</td><td>2,334</td><td>2,139</td><td>1,491</td><td>1,771</td><td>98.4%</td><td>9.1%</td><td>18.8%</td></tr><tr><td>PE-crude</td><td>3,840</td><td>3,617</td><td>3,296</td><td>3,970</td><td>4.2%</td><td>6.2%</td><td>20.5%</td></tr><tr><td>PP-crude</td><td>4,886</td><td>4,388</td><td>2,865</td><td>4,590</td><td>63.6%</td><td>11.3%</td><td>60.2%</td></tr><tr><td>PE-ethylene</td><td>1,701</td><td>544</td><td>1,383</td><td>2,230</td><td>36.4%</td><td>212.8%</td><td>61.2%</td></tr><tr><td>PP-propylene</td><td>2,100</td><td>1,139</td><td>1,058</td><td>2,168</td><td>45.7%</td><td>84.3%</td><td>105.0%</td></tr><tr><td>PVC-ethylene</td><td>-715</td><td>-1,760</td><td>-23</td><td>-108</td><td>N.M.</td><td>N.M.</td><td>N.M.</td></tr><tr><td>PVC-calcium carbide</td><td>427</td><td>614</td><td>238</td><td>288</td><td>24.7%</td><td>-30.5%</td><td>20.8%</td></tr><tr><td>ABS-styrene-butadiene-acrylonitrile</td><td>1,461</td><td>1,713</td><td>2,176</td><td>1,984</td><td>-50.9%</td><td>-14.7%</td><td>-8.8%</td></tr><tr><td>PS-styrene</td><td>1,506</td><td>1,355</td><td>815</td><td>1,378</td><td>89.1%</td><td>11.1%</td><td>69.0%</td></tr><tr><td>Styrene-benzene-ethylene</td><td>331</td><td>299</td><td>884</td><td>152</td><td>-62.0%</td><td>10.6%</td><td>-82.8%</td></tr><tr><td>Acrylic acid-propylene</td><td>1,941</td><td>1,706</td><td>1,606</td><td>1,977</td><td>-22.2%</td><td>13.8%</td><td>23.1%</td></tr><tr><td>Butyl acrylate-acrylic acid-butanol</td><td>132</td><td>-239</td><td>18</td><td>159</td><td>-24.7%</td><td>N.M.</td><td>800.0%</td></tr><tr><td>Propylene - Propane</td><td>1,662</td><td>2,047</td><td>1,562</td><td>3,186</td><td>33.7%</td><td>-18.8%</td><td>103.9%</td></tr><tr><td rowspan="10">Chemical fibres</td><td>PX-naptha</td><td>3,422</td><td>2,620</td><td>3,336</td><td>2,931</td><td>45.3%</td><td>30.6%</td><td>-12.1%</td></tr><tr><td>PTA-PX</td><td>378</td><td>94</td><td>104</td><td>580</td><td>16.4%</td><td>301.9%</td><td>457.9%</td></tr><tr><td>MEG-ethylene</td><td>159</td><td>-677</td><td>165</td><td>537</td><td>-34.1%</td><td>N.M.</td><td>226.0%</td></tr><tr><td>Polyester FDY spread</td><td>1,554</td><td>1,543</td><td>1,042</td><td>1,530</td><td>16.5%</td><td>0.7%</td><td>46.9%</td></tr><tr><td>Polyester POY spread</td><td>1,292</td><td>1,238</td><td>865</td><td>1,353</td><td>20.3%</td><td>4.4%</td><td>56.5%</td></tr><tr><td>Nylon POY spread</td><td>1,682</td><td>2,202</td><td>1,475</td><td>1,835</td><td>-30.6%</td><td>-23.6%</td><td>24.4%</td></tr><tr><td>Spandex-MDI-MEG</td><td>12,748</td><td>12,038</td><td>8,938</td><td>13,027</td><td>41.0%</td><td>5.9%</td><td>45.7%</td></tr><tr><td>Caprolactam-benzene</td><td>3,995</td><td>3,949</td><td>4,099</td><td>4,065</td><td>22.3%</td><td>1.2%</td><td>-0.8%</td></tr><tr><td>Acrylonitrile-propylene</td><td>2,251</td><td>1,188</td><td>1,562</td><td>3,186</td><td>9.9%</td><td>89.5%</td><td>103.9%</td></tr><tr><td>PET-PTA-MEG</td><td>287</td><td>348</td><td>201</td><td>256</td><td>120.6%</td><td>-17.6%</td><td>27.2%</td></tr><tr><td>Organic materials</td><td>Methanol-coal</td><td>1,107</td><td>1,190</td><td>332</td><td>819</td><td>33.0%</td><td>-7.0%</td><td>146.7%</td></tr><tr><td rowspan="4">Chemical fertilizers and pesticides</td><td>Urea-coal</td><td>355</td><td>360</td><td>262</td><td>345</td><td>-30.5%</td><td>-1.4%</td><td>31.4%</td></tr><tr><td>Monoammonium phosphate-phosphorus ore</td><td>2,319</td><td>2,067</td><td>1,863</td><td>2,399</td><td>47.2%</td><td>12.2%</td><td>28.8%</td></tr><tr><td>Diammonium phosphate-phosphorus ore-sulfur-synthetic ammonia</td><td>-2,040</td><td>-1,468</td><td>-227</td><td>-1,687</td><td>N.M.</td><td>N.M.</td><td>N.M.</td></tr><tr><td>Glyphosphate spread</td><td>13,385</td><td>16,369</td><td>11,520</td><td>12,201</td><td>13.6%</td><td>-18.2%</td><td>5.9%</td></tr><tr><td rowspan="3">Polyurethanes</td><td>MDI-benzene</td><td>13,193</td><td>15,708</td><td>12,738</td><td>12,521</td><td>13.8%</td><td>-16.0%</td><td>-1.7%</td></tr><tr><td>pMDI-benzene</td><td>9,826</td><td>11,298</td><td>9,508</td><td>9,955</td><td>-7.6%</td><td>-13.0%</td><td>4.7%</td></tr><tr><td>Propylene oxide-propylene</td><td>1,772</td><td>1,525</td><td>2,766</td><td>1,750</td><td>-19.9%</td><td>16.2%</td><td>-36.7%</td></tr><tr><td rowspan="3">Others</td><td>Soda ash spread</td><td>35</td><td>38</td><td>64</td><td>6</td><td>-75.1%</td><td>-7.5%</td><td>-90.7%</td></tr><tr><td>Titanium dioxide-titanium concentrate-sulfuric acid</td><td>3,311</td><td>3,047</td><td>2,637</td><td>2,752</td><td>-16.3%</td><td>8.6%</td><td>4.4%</td></tr><tr><td>Ethylene oxide-ethylene</td><td>646</td><td>55</td><td>672</td><td>1,444</td><td>-10.7%</td><td>1077.4%</td><td>114.9%</td></tr><tr><td rowspan="3">Refined oil products</td><td>Gasoline-crude</td><td>1,027</td><td>1,153</td><td>1,319</td><td>864</td><td>-37.3%</td><td>-10.9%</td><td>-34.5%</td></tr><tr><td>Diesel-crude</td><td>446</td><td>747</td><td>1,012</td><td>292</td><td>-54.4%</td><td>-40.3%</td><td>-71.1%</td></tr><tr><td>Fuel oil-crude</td><td>836</td><td>984</td><td>1,139</td><td>773</td><td>8.7%</td><td>-15.1%</td><td>-32.1%</td></tr></table>

Source: Wind; Note: Data as of 30 June 2026

Figure 22: Chemical product prices in June 2026 (Rmb/t)

<table><tr><td>Category</td><td>Product</td><td>Jun avg</td><td>May avg</td><td>Year beginning</td><td>End-Jun</td><td>YoY</td><td>MoM</td><td>YTD</td></tr><tr><td rowspan="2">Chemical feedstock</td><td>Naphtha</td><td>4,370</td><td>5,972</td><td>3,301</td><td>4,060</td><td>12.0%</td><td>-26.8%</td><td>23.0%</td></tr><tr><td>LPG</td><td>5,839</td><td>6,668</td><td>4,900</td><td>5,270</td><td>19.1%</td><td>-12.4%</td><td>7.6%</td></tr><tr><td rowspan="11">Olefins and plastics</td><td>Ethylene</td><td>6,359</td><td>8,212</td><td>5,092</td><td>5,381</td><td>3.8%</td><td>-22.6%</td><td>5.7%</td></tr><tr><td>Propylene</td><td>7,007</td><td>8,389</td><td>4,986</td><td>6,062</td><td>33.9%</td><td>-16.5%</td><td>21.6%</td></tr><tr><td>PE</td><td>9,109</td><td>9,895</td><td>7,317</td><td>8,600</td><td>9.4%</td><td>-7.9%</td><td>17.5%</td></tr><tr><td>PP</td><td>10,290</td><td>10,767</td><td>6,830</td><td>9,300</td><td>36.5%</td><td>-4.4%</td><td>36.2%</td></tr><tr><td>PS</td><td>9,536</td><td>10,556</td><td>7,429</td><td>8,597</td><td>14.5%</td><td>-9.7%</td><td>15.7%</td></tr><tr><td>PVC-ethylene</td><td>5,181</td><td>5,744</td><td>4,769</td><td>4,945</td><td>1.4%</td><td>-9.8%</td><td>3.7%</td></tr><tr><td>PVC-calcium carbide</td><td>4,550</td><td>4,855</td><td>4,430</td><td>4,390</td><td>-1.9%</td><td>-6.3%</td><td>-0.9%</td></tr><tr><td>Styrene</td><td>8,247</td><td>9,499</td><td>6,850</td><td>7,410</td><td>5.5%</td><td>-13.2%</td><td>8.2%</td></tr><tr><td>ABS</td><td>9,896</td><td>11,669</td><td>8,800</td><td>9,425</td><td>-5.7%</td><td>-15.2%</td><td>7.1%</td></tr><tr><td>Acrylic acid</td><td>7,933</td><td>8,800</td><td>5,900</td><td>7,200</td><td>11.7%</td><td>-9.8%</td><td>22.0%</td></tr><tr><td>Butyl acrylate</td><td>8,910</td><td>9,417</td><td>7,100</td><td>8,100</td><td>6.6%</td><td>-5.4%</td><td>14.1%</td></tr><tr><td rowspan="11">Chemical fibres</td><td>PX</td><td>8,804</td><td>9,709</td><td>7,500</td><td>7,900</td><td>24.5%</td><td>-9.3%</td><td>5.3%</td></tr><tr><td>PTA</td><td>6,194</td><td>6,466</td><td>5,030</td><td>5,830</td><td>23.9%</td><td>-4.2%</td><td>15.9%</td></tr><tr><td>MEG</td><td>4,527</td><td>4,849</td><td>3,667</td><td>4,285</td><td>1.5%</td><td>-6.6%</td><td>16.9%</td></tr><tr><td>Polyester FDY</td><td>8,621</td><td>8,953</td><td>6,750</td><td>8,200</td><td>17.8%</td><td>-3.7%</td><td>21.5%</td></tr><tr><td>Polyester POY</td><td>8,326</td><td>8,608</td><td>6,550</td><td>8,000</td><td>18.5%</td><td>-3.3%</td><td>22.1%</td></tr><tr><td>Nylon POY</td><td>13,419</td><td>14,761</td><td>11,400</td><td>13,300</td><td>9.4%</td><td>-9.1%</td><td>16.7%</td></tr><tr><td>Spandex</td><td>28,290</td><td>28,300</td><td>23,000</td><td>28,200</td><td>20.8%</td><td>0.0%</td><td>22.6%</td></tr><tr><td>Caprolactam</td><td>11,183</td><td>11,915</td><td>9,450</td><td>10,900</td><td>20.9%</td><td>-6.1%</td><td>15.3%</td></tr><tr><td>Acrylonitrile</td><td>10,462</td><td>10,822</td><td>7,400</td><td>10,450</td><td>27.2%</td><td>-3.3%</td><td>41.2%</td></tr><tr><td>PET chips</td><td>7,190</td><td>7,602</td><td>5,800</td><td>6,760</td><td>20.6%</td><td>-5.4%</td><td>16.6%</td></tr><tr><td>Viscose staple fibre</td><td>14,138</td><td>14,047</td><td>12,800</td><td>14,200</td><td>10.0%</td><td>0.6%</td><td>10.9%</td></tr><tr><td rowspan="3">Chlor-alkali</td><td>Light soda ash</td><td>1,176</td><td>1,208</td><td>1,185</td><td>1,155</td><td>-10.1%</td><td>-2.7%</td><td>-2.5%</td></tr><tr><td>Caustic soda</td><td>749</td><td>779</td><td>871</td><td>735</td><td>-25.7%</td><td>-3.8%</td><td>-15.6%</td></tr><tr><td>Calcium carbide</td><td>2,712</td><td>2,774</td><td>2,

[中间内容因长度限制已省略]

 not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

![](images/aecacd117135471d3a495cc94c0c37debbe637d647db8fe09ce18cc3b39deb9a.jpg)

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
