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
# China Chemical New Materials Sector Price hikes are the potential catalysts for MLCC/electronic gas/wet chemicals in H226

## Higher forecast and valuation primarily reflects potential price hikes

The share prices of MLCC and electronic specialty gas companies have more than doubled YTD, reflecting market expectations for AI server demand growth, along with memory and related product price appreciation, in our view. Following the recent stock price correction, we prefer products with stronger visibility of price hikes. We expect supply-demand for high-capacitance MLCCs to remain tight in H2, as low tungsten powder exports may constrain WF6 supply, while prices for electronic-grade HF, H2SO4 and Mo/In targets may be supported by raw material costs. We rank price hike visibility from high to low as follows: MLCC materials (release film, etc.) > MLCCs > WF6 > semi wet chemicals (electronic-grade HF/H2SO4) > helium.

## MLCC distributors remain upbeat; focus on upstream material price trends

Yageo recently notified customers of MLCC price increases effective on 1 July (see news report for details), covering multiple downstream sectors, including AI servers, consumer electronics, automotive and industrial. Additionally, distributors remain optimistic about MLCC price increases in H2. While we expect tight supply-demand for high-cap MLCCs to persist, consumer electronics demand remains uncertain. MLCC material orders remain robust and capacity utilization rates remain high, suggesting further upside for MLCC prices in H2, in our view.

## Electronic chemical prices may benefit from reduced supply and cost support

YTD, market prices for WF6 (5N grade) have doubled to Rmb1,800/kg, mainly due to a sharp decline in China's tungsten powder (raw material for WF6) exports. We estimate Japan and South Korea currently account for 46% of global capacity. If tungsten powder exports remain low in H2, WF6 prices could climb further. Meanwhile, we expect electronic-grade HF price hikes in H2, driven by cost and demand support (see more in our note). Furthermore, electronic-grade H2SO4/H2O2 prices have trended upward. We suggest monitoring downstream semiconductor demand growth and raw material cost fluctuations.

## We prefer Jiemei, Guanggang Gas, Capchem and Dongyue Group

We raise our PTs and earnings estimates for relevant companies to reflect potential price hikes (Figure 1). Within the MLCC industry chain, we prefer companies with higher price hike visibility and lower valuations; thus, we recommend Jiemei and Three-Circle. In the electronic chemical sector, Guanggang Gas H126's preliminary results beat our expectations, and we believe newly awarded projects may sustain a 40% net profit CAGR in 2027-29. We like Capchem and Dongyue following the stock price correction, with recovery in their main business and upside in electronic material business.

Figure 1: Earnings estimate and PT revisions

<table><tr><td rowspan="2">13-Jul-26</td><td rowspan="2">Rating</td><td colspan="2">Price target (lcy)</td><td rowspan="2">Share price Local cry</td><td rowspan="2">Upside %</td><td colspan="3">EPS change %</td><td colspan="3">PE (x)</td><td rowspan="2">EPS CAGR 26-28E</td><td rowspan="2">PEG (x) 26E</td><td colspan="3">2026E revenue exposure to ...</td></tr><tr><td>Current</td><td>Old</td><td>26E</td><td>27E</td><td>28E</td><td>26E</td><td>27E</td><td>28E</td><td colspan="2">product with price upside</td><td>electronics</td></tr><tr><td>Guanggang Gas</td><td>Buy</td><td>66.00</td><td>42.00</td><td>44.27</td><td>49%</td><td>15%</td><td>6%</td><td>14%</td><td>116</td><td>79</td><td>51</td><td>52%</td><td>2.2</td><td>Helium</td><td>25%</td><td>70%</td></tr><tr><td>Jinhong Gas</td><td>Buy</td><td>53.00</td><td>37.00</td><td>37.48</td><td>41%</td><td>-2%</td><td>10%</td><td>15%</td><td>60</td><td>40</td><td>32</td><td>36%</td><td>1.7</td><td>Helium</td><td>30%</td><td>50%</td></tr><tr><td>Three Circle</td><td>Buy</td><td>160.00</td><td>159.00</td><td>111.80</td><td>43%</td><td>1%</td><td>1%</td><td>1%</td><td>56</td><td>41</td><td>32</td><td>33%</td><td>1.7</td><td>MLCC</td><td>40%</td><td>50%</td></tr><tr><td>Jiemei</td><td>Buy</td><td>104.00</td><td>86.00</td><td>72.58</td><td>43%</td><td>2%</td><td>3%</td><td>3%</td><td>71</td><td>49</td><td>38</td><td>37%</td><td>1.9</td><td>MLCC release film</td><td>25%</td><td>90%</td></tr><tr><td>Sinocera</td><td>Buy</td><td>93.00</td><td>65.00</td><td>64.01</td><td>45%</td><td>8%</td><td>9%</td><td>15%</td><td>80</td><td>57</td><td>45</td><td>33%</td><td>2.4</td><td>Ceramic powder</td><td>25%</td><td>25%</td></tr><tr><td>Longhua</td><td>Buy</td><td>17.00</td><td>14.20</td><td>11.87</td><td>43%</td><td>6%</td><td>17%</td><td>17%</td><td>44</td><td>32</td><td>26</td><td>29%</td><td>1.5</td><td>Mo &amp; ITO target</td><td>30%</td><td>30%</td></tr></table>

Source: Wind, UBS-S estimates. Note: Share price data as of 13 July 2026.

China
Chemicals

Amily Guo
Analyst
amily.guo@ubs.com
+86-105-832 8845

Richard Li
Analyst
S1460121090003
richard-ze.li@ubs.com
+86-21-3866 8802

Jay LIN
Analyst
S1460525070001
jay.lin@ubs.com
+86-105-832 8044

Cheryl Wen
Analyst
S1460525030002
cheryl.wen@ubs.com
+86-21-3866 8916

Eason Tang
Analyst
eason.tang@ubs.com
+852-3712 3883

## MLCCs: Distributors remain optimistic; high-cap MLCC supply-demand to stay tight in H2

Distributors remain optimistic; Yageo recently announced price hikes. According to Trendforce, Yageo recently notified customers of price increases for its capacitor products effective 1 July, covering MLCCs, aluminum electrolytic capacitors, tantalum capacitors, etc. This round of price hikes is mainly driven by rising manufacturing costs due to geopolitics, energy and raw material price appreciation. The price hikes span a broad range of products, with downstream segments including AI servers, consumer electronics, automotive and industrial.

On 22 May 2026, we hosted an online MLCC discussion (more in note) and invited a Southern China distributor to attend. The distributor is also optimistic about MLCC price increases in H2, given that: 1) AI server demand for high-cap MLCCs is crowding out substantial MLCC capacity, leading to overall MLCC capacity tightness; 2) distributor and end-user inventory remains low, at about one month, with major domestic MLCC manufacturers near full capacity; and 3) manufacturers are tightening low-priced MLCC supply and scaling back preferential pricing policies.

Figure 2: Japan MLCC production and export price trends  
![](images/088faa65692134c22ed79efc4a8638cb92d45bb7befcc166ea2c4588040f8ddc.jpg)  
Source: METI, UBS-S

We expect high-cap MLCC supply-demand to remain tight in H226 and suggest monitoring price hike realization for upstream materials. According to Crypto Briefing, Samsung Electro-Mechanics recently secured a KRW454bn MLCC order, which the market expects may come from a leading supplier for a cloud service provider. Meanwhile, as per UBS Evidence Lab (>Access Dataset), MLCC distributors' unit inventory fell 3% as of 13 June vs. 8 May, while inventory value rose 1%; thus, we foresee MLCC supply-demand remaining tight in H226. Our recent industry check showed MLCC material suppliers are running at high utilisation rates; if MLCC demand continues to improve in H2, we would see significant upside potential for upstream material prices.

Figure 3: MLCC distributor inventory value index  
![](images/0b8d09f9d5a588c3225c743c85430e9105af6bbb61e5cefad00892fac7c98202.jpg)  
Source: UBS Evidence Lab (> Access Dataset); Note: Standardized USD inventory.

Figure 4: MLCC distributor inventory value index (by manufacturer)  
![](images/5fe5dc93c5c1dc347c0463e4ee9176c2296e22cba0ac779ccf26d3871c9dd701.jpg)  
Source: UBS Evidence Lab (> Access Dataset); Note: Standardized USD inventory.

## Electronic specialty gases: Monitoring WF6 raw material exports; helium prices rebounded modestly

Tungsten hexafluoride (WF6) is a precursor material used in chemical vapor deposition (CVD) processes of semiconductor manufacturing, primarily to deposit metal tungsten thin film on wafer surfaces, with extensive applications in memory and logic chip fabrication. YTD, the market price for WF6 (5N grade) has surged from Rmb945/kg to Rmb1,800/kg, mainly due to a sharp drop in monthly tungsten powder (raw material for WF6) exports from China since January. According to USGS, China accounted for nearly 80% of global tungsten ore output in 2025, and is also a major producer of electronic-grade tungsten powder. Therefore, reduced exports have left Japan and South Korea WF6 capacity facing a raw material shortage.

Figure 5: China monthly tungsten powder exports (tonnes)  
![](images/c4229b57416a1ea54fa6609b3b43afbe9166f3c439e1aa8a854db71f162aa063.jpg)  
Source: GAC

Figure 6: WF6 (5N) and tungsten powder price trends (Rmb/kg)  
![](images/59b41999c5741b5b1a065fa8acb260ce5cbcf0f524e1f63ecc3701910f629107.jpg)  
Source: Wind, Oilchem

According to Peric Special Gases' prospectus, Japan accounted for c22% of global WF6 capacity in 2025, while South Korea accounted for c24%. Among domestic producers, Peric Special Gases is the largest by capacity, while Borui Zhongxiao, Haohua Chemical Science and Technology, and Nata Opto-Electronic Material each have 600-700 tonnes of WF6 capacity.

Figure 7: Major WF6 capacity summary (2025)

<table><tr><td>Overseas</td><td>Capacity t</td><td>Country</td><td>Comments</td></tr><tr><td>SK Material</td><td>1,800</td><td>Korea</td><td></td></tr><tr><td>Kanto Denka</td><td>1,400</td><td>Japan</td><td></td></tr><tr><td>Foosung</td><td>900</td><td>Korea</td><td>400t in Nantong</td></tr><tr><td>Central Glass</td><td>700</td><td>Japan</td><td></td></tr><tr><td>Merck</td><td>600</td><td>German</td><td></td></tr><tr><td>Peric gas</td><td>2,230</td><td>China</td><td>1,000t new capacity to start in H127</td></tr><tr><td>Borui-Central Glass</td><td>600</td><td>China</td><td>JV with Central glass</td></tr><tr><td>Haohua</td><td>700</td><td>China</td><td></td></tr><tr><td>Nata Optic</td><td>600</td><td>China</td><td></td></tr></table>

Source: Company data, UBS-S

We believe upside to WF6 prices hinges on tungsten powder exports. The domestic market ASP of tungsten powder rose from Rmb1,065/kg to Rmb2,000+/kg in 4M26, although it has retreated sharply below Rmb1,200/kg since May. The WF6 (5N) price uptrend has also moderated significantly since May. Thus, we consider cost support and tungsten powder supply to be the main drivers of WF6 price fluctuations. If China's tungsten powder exports remain low, there would still be upside to WF6 prices.

Figure 8: Global Tungsten Production by Country – 2025  
![](images/1b3313724b63c1c3197577e21d254a15eb4a3545633d5ce4f27bcc7d9dcf91c5.jpg)  
Source: USGS  
Figure 9: China Tungsten Consumption by End-Use Sector – 2023

![](images/00230c8a40a011289669e5651b59662173523916cdc2de1a6b4b57f24a046803.jpg)  
Source: Antaike

Helium prices have rebounded slightly recently, and we expect overall stability in H226. The production halt of Qatar's helium facilities in March and Russia's helium export control in April caused China's helium retail price to rise sharply to cRmb500/cubic meter in April, although the price declined to cRmb250/cubic meter in May-June, mainly due to market expectations for Russia's supply restriction to ease. Helium prices picked up mildly amid heightening geopolitical risks recently. We foresee limited upside and downside risks for helium prices in H226, and we expect domestic market prices to stay around Rmb200-300/cubic meter (see note for details).

Figure 10: Helium price trend in China (Rmb/cylinder)  
![](images/67d2b524ed0b8c0aa4a1b251af4c7a343bba2cb6066c767cdc0fcdc68af5f2f8.jpg)  
Source: Wind. Note: One cylinder holds about 6 cubic meters of helium.

## Electronic wet chemicals: Raw material cost inflation and growing demand set to drive price hikes

Electronic-grade hydrofluoric acid (EG-HF) is a key wet electronic chemical. It is an aqueous solution prepared by purifying anhydrous hydrogen fluoride and absorbing it into ultrapure water. With a 2025 market size of around Rmb4.25bn in China, EG-HF's TAM has been driven by downstream capacity expansion (eg, semis and display panels), as well as domestic substitution (see our note: Fluorochemicals: Beneficiary of AI-driven new opportunities).

We foresee a continuing price uptrend for EG-HF amid rising raw material prices and growing demand. Regarding raw materials, the price of anhydrous hydrogen fluoride in China has risen 19% YTD, mainly driven by sulfur price hikes amid the Middle East conflict. Except UPSSS-grade EG-HF, domestic market prices of other grades have gained 2-22% YTD. We think the domestic price of UPSSS-grade EG-HF is mainly subject to order cycles, and there could be pass-through of cost inflation pressure. As per Do-

Fluoride, the market prices of semi-grade hydrofluoric acid have increased around 20-30%.

Figure 11: Price of anhydrous hydrogen fluoride in China  
![](images/7028c1d0a0819edf6744f5719c83aaed9ad922a1584f276d3f58b241179c648c.jpg)  
Source: Wind

Figure 12: Sulfur price in China  
![](images/b0985e3715ed6f14438a91d1294aa79ea435e1af141feca5174148b89f727720.jpg)  
Source: Wind

Figure 13: China's EG-HF (ex. UPSSS-grade) prices have risen YTD  
![](images/67c3358db473f0b48743e30083b2514f14edee04fc4e0214038d22f00ba33bc8.jpg)  
Source: Wind

Reportedly, overseas wafer fabs are proactively purchasing EG-HF. In terms of exports, China's EG-HF exports expanded 33% YoY in 5M26, with ASP up 19% MoM in May, demonstrating robust overseas demand. In terms of earnings of the product, as per DoFluoride, downstream clients value supply stability and quality consistency more, as EG-HF takes up a limited proportion of the total chip cost. As such, corporate profitability has been well underpinned amid cost-driven price hikes. In H226, we suggest watching: 1) sulfur price trends and their impact on anhydrous hydrogen fluoride prices; and 2) the progress of Chinese EG-HF producers in supplying to/certification by overseas semi clients.

Figure 14: China's EG-HF exports grew 33% YoY in 5M26  
![](images/e90f0dc61fdd5c307ead7f732f45753ffc502ac2445cffcdfda5c1a02f90a078.jpg)  
Source: Wind, customs data

Figure 15: China's EG-HF export ASP rose 19% MoM in May 2026  
![](images/4b4edca07ccb2f215abed9ebcf58b412a6f549412563d5c3063dbd3606ece42d.jpg)  
Source: Wind, customs data

The prices of high-purity sulfuric acid/indium tin oxide (ITO) targets may have been bolstered by raw material costs. Sulfur prices have more than doubled YTD, while metals such as indium/molybdenum have had 70%/30% price gains, respectively, likely providing cost support for select electronic chemical materials. Meanwhile, sector fundamentals could bottom out amid downstream memory demand. We note continued price increases of high-purity sulfuric acid/hydrogen peroxide since March, and we expect price hikes for molybdenum/ITO targets for pass-through of raw material costs.

Figure 16: Price trends of high-purity hydrogen peroxide in China  
![](images/8ee02a5ddf48042ebfcf680da2de69a89d88d41cc556fc4180785753461aa46c.jpg)  
Source: Wind

Figure 17: Price trends of high-purity sulfuric acid in China  
![](images/93a6c7595aba9ad5a6e1a1b0a8af8b36c3c47d53eb4925ca092989eaac1bca22.jpg)  
Source: Wind

Figure 18: Price trend of indium in China  
![](images/d7f18b2d2193e9033ffc1b9aaa49b2cd740e85eebeb36b15f63455d3d53bc65f.jpg)  
Source: Wind

Figure 19: Price trend of molybdenum powder in China  
![](images/5c016430b278a94d62d5b18ffd1ecd0304a352844f7ff69da99d52c3ba5a58ff.jpg)  
Source: Antaike

## Stock picks and price target revisions

ESG/MLCC value chain peers have re-rated to 3.3/2.3x 2026E PEG, on average. The share prices of ESG/MLCC value chain names overall ha

[中间内容因长度限制已省略]

and/or Market Counterparties only as classified under the DFSA rulebook. It should not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
