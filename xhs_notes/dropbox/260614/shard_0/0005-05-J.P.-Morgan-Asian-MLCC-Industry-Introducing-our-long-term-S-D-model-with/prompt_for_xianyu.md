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
## Asian MLCC Industry

Introducing our long-term S&D model with a multi-year bullish view; prefer JP/TW names over KR

- We introduce our MLCC S-D model which predicts a supply shortage view through 2028E. Our Global MLCC S-D model includes historical updates and a forward three-year outlook. We forecast S-D shortage mainly propelled by server compute demand growth and unique capacity constraint factors. We expect the degree of tightness in the 26-28E cycle (from $10\%$ over-supply in 25 to $6\%$ shortage by 28E) to be slightly worse than that of the 2017-18 cycle (leading supplier's end-of-life program led a procurement demand spike amid first cloud capex and then first-gen EV demand take-off cycle) and estimate high- $50\%$ ASP growth during the same period (similar range of growth to that of the 2016-18 cycle).  
- Server compute drivers' TAM expansion. Server is the single most important application in the MLCC industry which has seen a sharp surge in customer capacity allocation requests (both AI and GP server demand) and we have also seen relatively resilient automotive MLCC demand. While consumer electronics' end demand remains challenging, procurement activities are slightly different as customers (incl. distributor channels) will start to notice a tightening of supply. We forecast the MLCC industry TAM to be above US \$30bn (2025-28E CAGR of 24% vs. '2016-19 CAGR of +16%) with a larger impact from the ASP uptick. As a result, we estimate a higher margin profile in coming years (industry OPM at 38% in 2028E vs. 36% in '18), consistent with other commodity tech sectors (e.g. memory, substrate and others).  
- Higher capacity trade loss ratio from server/auto mix increase and yield challenge is an underappreciated point. MLCC industry nameplate capacity has historically grown \~10% in the past ten years; however, effective capacity (after production penalty and yield adjustment) indicates considerably limited supply output versus growing procurement demand. Auto and Server MLCC are mainly designed based on larger form-factor vs. IT applications, and higher system power voltage requirements lead to the use of advanced specs. Furthermore, we have seen a sharp rise in new MLCC specs with ultra-high capacitance (e.g. 1005-47uf) for AI server applications (on the back of rising interest from both leading GPU and ASIC camp customers) resulting in a declining assembly yield in the leading supplier's capacity. Such capacity penalties (or trade losses) are accelerating this year (DD% negative impact on headline capacity growth in the next three years vs. low-to-mid single-digit % impact in the past five years), and is not fully understood by investors, in our view.  
- Investment recommendations – JP/TW over KR on valuation merit. MLCC suppliers have collectively delivered a 268% 2026 YTD return (vs. MXAP +16%) well outperforming the rest of the technology hardware sub-sector, and its aggregate market cap stands at US\$354bn trading at 61x/40x/30x FY26-28E on consensus EPS. Given the early stage of the industry transition towards the AI ecosystem, we believe consensus earnings revisions tend to lag and expect investors to focus on the growth momentum. That said, share price momentum may remain strong in 2H26E and we stay

## Technology - Semiconductors

Jay Kwon AC

(82-2) 758-5725

jay.h.kwon@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

Akinori Kanemoto AC

(81-3) 6736 8628

akinori.kanemoto@JPM.com

JPM Securities Japan Co., Ltd.

Jerry Tsai AC

(886-2) 2725-9867

jerry.tsai@JPM.com

JPM Securities (Taiwan) Limited

Sangsik Lee

(82-2) 758 5146

sangsik.lee@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

Neelay Y Kamath

(91-22) 6157 3764

neelay.kamath@jpmchase.com

JPM India Private Limited

constructive on the sector's growth prospects. We have an OW view on all major MLCC players in Asia and believe Japan (Murata > Taiyo Yuden > TDK) and Taiwan (Yageo) peers present greater upside over their Korean peers (SEMCO) due to attractive valuation.

\- Key risks and catalysts. AI server-grade MLCC (using side-gap construction method) is a relatively new SKU in the industry and we are seeing meaningful R&D activity pick up to accommodate higher power requirements for next-generation server systems. As discussed earlier, assembly yield tends to be 3-6x lower than that of normal MLCC and there are only a few selective suppliers who can scale up to meaningful volumes. This is likely to limit the production output for a considerable period and end customers' procurement appetite could be substantially higher regardless of price point. This remains a key upside risk point to the pricing and margin profile for AI MLCC and the spillover effect to IT and commodity segment will be a key monitoring point. We will closely follow suppliers' production and capacity-related commentary to assess the realistic supply increase and consequent S-D situation. Secondary market pricing has traditionally been a leading indicator of contract pricing sentiment and we will closely follow the trends.

# Key charts and tables

Figure 1: MLCC industry revenue and y-y  
![](images/b94aba56c86fb0cb47456ca3fc1966a7929221895a94d6ae2e46681af0be5e25.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | MLCC industry revenue (top-down) (US$mn) | y-y changes, % [RHS] (%) |
| :--- | :--- | :--- |
| 2016 | 8000 | - |
| 2017 | 9500 | 17 |
| 2018 | 13000 | 36 |
| 2019 | 12500 | -4 |
| 2020 | 13000 | 5 |
| 2021 | 16000 | 24 |
| 2022 | 14000 | -14 |
| 2023 | 12500 | -9 |
| 2024 | 13500 | 5 |
| 2025E | 17500 | 14 |
| 2027E | 24000 | 15 |
| 2028E | 31000 | 35 |
| 2018E | 33000 | 17 |
| 2028E | 31000 | 27 |
</details>

Source: JPM estimates, Company data.

Figure 3: MLCC industry pricing and y-y  
![](images/06b297fabac02fa68cc82cd963640bf58573cc39c3e28b9f16b0c641eee17482.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | MLCC industry pricing (US$) / k unit | y-y changes, % [RHS] |
| :--- | :--- | :--- |
| 2016 | 2.8 | - |
| 2017 | 3.0 | 5% |
| 2018 | 3.8 | 28% |
| 2019 | 3.4 | -10% |
| 2020 | 3.5 | 3% |
| 2021 | 3.6 | 13% |
| 2022 | 3.5 | -10% |
| 2023 | 3.2 | -10% |
| 2024 | 3.1 | -2% |
| 2025E | 3.3 | 5% |
| 2027E | 4.5 | 10% |
| 2028E | 5.1 | 17% |
</details>

Source: JPM estimates, Company data.

Figure 5: MLCC industry revenue vs volume CAGR comparison  
![](images/41fafd876138a9768115cea4d4fa1b7e9f6b910212cee3dca752ed7800d0fd39.jpg)

<details>
<summary>bar chart</summary>

ASP start to move up upon mix improvement and tightening S-D
| Period | Revenue (%) |
| :--- | :--- |
| 16-19 | 16 |
| 19-22 | 5 |
| 22-25 | 3 |
| 25A-28E | 24 |
</details>

Source: JPM estimates, Company data.

Figure 2: MLCC industry volume and y-y  
![](images/755e26c6a47cb520c0566cea69f62f7332b94ae4a15509973021645caea13787.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | MLCC industry volume (top-down) (US$mn) | y-y changes, % [RHS] (%) |
| :--- | :--- | :--- |
| 2016 | 2900 | |
| 2017 | 3200 | 11 |
| 2018 | 3400 | 7 |
| 2019 | 3600 | 7 |
| 2020 | 3800 | 1 |
| 2021 | 4000 | 9 |
| 2022 | 3900 | -4 |
| 2023 | 3950 | 1 |
| 2024 | 4200 | 7 |
| 2025 | 4500 | 9 |
| 2026E | 4800 | 4 |
| 2027E | 5200 | 9 |
| 2028E | 5700 | 9 |
</details>

Source: JPM estimates, Company data.

Figure 4: MLCC Revenue and OPM trend for the top 5 players  
![](images/8d90a069214e0653cc7a023abcf8bbae5fcaf849f19acb046360be3f8527abcd.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | Top 5 (US$bn, %) | Industry (%) |
| :--- | :--- | :--- |
| 2020 | 11.5 | 26 |
| 2021 | 14.5 | 30 |
| 2022 | 12.0 | 24 |
| 2023 | 11.0 | 15 |
| 2024 | 11.5 | 15 |
| 2025 | 13.0 | 17 |
| 2026E | 14.5 | 21 |
| 2027E | 20.0 | 30 |
| 2028E | 25.0 | 38 |
</details>

Source: JPM estimates, Company data.

Figure 6: MLCC content comparison by application  
![](images/6761c42229f2ad0b7b407940ead5a11ee7ae2b753602ed8e8b82e847b823741a.jpg)

<details>
<summary>bar chart</summary>

| Year   | Smartphone | Server | Auto  |
| ------ | ---------- | ------ | ----- |
| 2016   | ~1,000     | ~2,500 | ~3,000 |
| 2019   | ~1,500     | ~4,000 | ~4,500 |
| 2022   | ~1,500     | ~5,000 | ~6,000 |
| 2025   | ~1,500     | ~12,000 | ~8,000 |
| 2028E  | ~1,500     | ~30,000 | ~11,000 |
| 2030E  | ~1,500     | ~45,000 | ~14,000 |
</details>

Source: JPM estimates, Company data.

Figure 7: MLCC content comparison by application for 2025E  
![](images/a63cb3fa5dcb6d6d5bbc22d1bfc7810029b71e619e89c0ad13107cf6f8e64243.jpg)

<details>
<summary>bar chart</summary>

| Category | 2025 (units) | 2030E (units) |
| :--- | :--- | :--- |
| GP server | 8000 | 12000 |
| AI server | 50000 | 148000 |
| ICE | 6000 | 11000 |
| BEV | 15000 | 22000 |
| Humanoid | 12000 | 23000 |
</details>

Source: JPM estimates, Company data.

Figure 9: MLCC player's UTR trend  
![](images/9cac9ea56383cf698414a4926fd0d83cffed377974964feb8aa31c7667ffa288.jpg)

<details>
<summary>line chart</summary>

| Quarter | Value |
| ------- | ----- |
| 1Q19    | 70    |
| 3Q19    | 62    |
| 1Q20    | 63    |
| 3Q20    | 75    |
| 1Q21    | 55    |
| 3Q21    | 54    |
| 1Q22    | 68    |
| 3Q22    | 77    |
| 1Q23    | 82    |
| 3Q23    | 71    |
| 1Q24    | 78    |
| 3Q24    | 74    |
| 1Q25    | 79    |
| 3Q25    | 76    |
| 1Q26    | 75    |
</details>

Source: JPM estimates, Company data.

Figure 8: MLCC industry bottoms-up OPM trend  
![](images/96930705c5f7496e48f4fd7b7cbc948b370ab1788cb25818e578c18f2327c338.jpg)

<details>
<summary>bar chart</summary>

| Year | Value (%) |
| :--- | :--- |
| 2016 | 16 |
| 2017 | 19 |
| 2018 | 36 |
| 2019 | 23 |
| 2020 | 25 |
| 2021 | 29 |
| 2022 | 22 |
| 2023 | 15 |
| 2024 | 16 |
| 2025 | 17 |
| 2026E | 22 |
| 2027E | 31 |
| 2028E | 38 |
</details>

Source: JPM estimates, Company data.

Figure 10: MLCC players' inventory days outstanding  
![](images/8e3c9953275cf6039b592a5d5c418672eb81ebfea34d62eb35a0527c21f60f7b.jpg)

<details>
<summary>line chart</summary>

| Quarter | Value |
| ------- | ----- |
| 1Q19    | 91%   |
| 3Q19    | 87%   |
| 1Q20    | 85%   |
| 3Q20    | 94%   |
| 1Q21    | 95%   |
| 3Q21    | 96%   |
| 1Q22    | 92%   |
| 3Q22    | 80%   |
| 1Q23    | 72%   |
| 3Q23    | 78%   |
| 1Q24    | 80%   |
| 3Q24    | 83%   |
| 1Q25    | 85%   |
| 3Q25    | 87%   |
| 1Q26    | 90%   |
| 3Q26E   | 94%   |
</details>

Source: JPM estimates, Company data.  
US\$mn, % - RHS

Figure 11: Long Term MLCC Supply-Procurement Gap trend

![](images/d70cb00ccca3de786571e54afc54c4a93f92858f89c899441594dd95cba4e89a.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year   | Procurement | Supply | Gap (%) - RHS |
|--------|-------------|--------|---------------|
| 2016   | 3000        | 3200   | 7%            |
| 2017   | 3200        | 3400   | 3%            |
| 2018   | 3800        | 3600   | -4%           |
| 2019   | 3400        | 3800   | 4%            |
| 2020   | 3800        | 4000   | 2%            |
| 2021   | 4600        | 4800   | 6%            |
| 2022   | 4000        | 4600   | 15%           |
| 2023   | 3800        | 4400   | 13%           |
| 2024   | 4400        | 4800   | 12%           |
| 2025   | 4800        | 5200   | 10%           |
| 2026E  | 5200        | 5400   | 5%            |
| 2027E  | 5800        | 5600   | -5%           |
| 2028E  | 6400        | 6000   | -6%           |
</details>

Source: JPM estimates, Company data.

Table 1: MLCC industry demand forecast  
Units in billions

<table><tr><td>Unit in billions</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>MLCC demand</td><td>2,875</td><td>3,205</td><td>3,415</td><td>3,658</td><td>3,710</td><td>4,053</td><td>3,902</td><td>3,937</td><td>4,224</td><td>4,593</td><td>4,789</td><td>5,222</td><td>5,688</td><td>6,283</td><td>6,898</td></tr><tr><td>y/y changes, %</td><td></td><td>11%</td><td>7%</td><td>7%</td><td>1%</td><td>9%</td><td>-4%</td><td>1%</td><td>7%</td><td>9%</td><td>4%</td><td>9%</td><td>9%</td><td>10%</td><td>10%</td></tr><tr><td>Mobile</td><td>1,132</td><td>1,288</td><td>1,329</td><td>1,390</td><td>1,341</td><td>1,483</td><td>1,406</td><td>1,374</td><td>1,465</td><td>1,568</td><td>1,485</td><td>1,478</td><td>1,503</td><td>1,557</td><td>1,600</td></tr><tr><td>Smartphone</td><td>897</td><td>1,060</td><td>1,105</td><td>1,136</td><td>1,058</td><td>1,178</td><td>1,111</td><td>1,094</td><td>1,167</td><td>1,254</td><td>1,179</td><td>1,177</td><td>1,194</td><td>1,233</td><td>1,265</td></tr><tr><td>Low-end</td><td>252</td><td>288</td><td>316</td><td>317</td><td>297</td><td>281</td><td>246</td><td>281</td><td>333</td><td>334</td><td>280</td><td>273</td><td>279</td><td>290</td><td>298</td></tr><tr><td>Mid-end</td><td>305</td><td>396</td><td>393</td><td>436</td><td>372</td><td>441</td><td>410</td><td>357</td><td>358</td><td>394</td><td>384</td><td>384</td><td>389</td><td>400</td><td>412</td></tr><tr><td>High-end</td><td>339</td><td>376</td><td>397</td><td>382</td><td>389</td><td>457</td><td>455</td><td>456</td><td>475</td><td>526</td><td>515</td><td>519</td><td>526</td><td>542</td><td>556</td></tr><tr><td>Tablets</td><td>127</td><td>125</td><td>109</td><td>117</td><td>141</td><td>140</td><td>124</td><td>114</td><td>126</td><td>129</td><td>122</td><td>117</td><td>117</td><td>122</td><td>127</td></tr><tr><td>Featurephone</td><td>94</td><td>81</td><td>80</td><td>74</td><td>65</td><td>67</td><td>64</td><td>57</td><td>54</td><td>57</td><td>54</td><td>55</td><td>57</td><td>60</td><td>61</td></tr><tr><td>Others</td><td>15</td><td>24</td><td>34</td><td>64</td><td>77</td><td>98</td><td>107</td><td>109</td><td>119</td><td>128</td><td>130</td><td>130</td><td>135</td><td>142</td><td>146</td></tr><tr><td>PC/Server</td><td>296</td><td>336</td><td>376</td><td>401</td><td>442</td><td>520</td><td>484</td><td>430</td><td>474</td><td>592</td><td>711</td><td>957</td><td>1,199</td><td>1,453</td><td>1,717</td></tr><tr><td>Desktop</td><td>130</td><td>143</td><td>155</td><td>165</td><td>140</td><td>158</td><td>148</td><td>126</td><td>128</td><td>148</td><td>147</td><td>157</td><td>176</td><td>188</td><td>198</td></tr><tr><td>NBPC</td><td>130</td><td>144</td><td>160</td><td>170</td><td>215</td><td>265</td><td>245</td><td>220</td><td>236</td><td>273</td><td>277</td><td>310</td><td>363</td><td>384</td><td>405</td></tr><tr><td>Chromebook</td><td>7</td><td>11</td><td>14</td><td>16</td><td>33</td><td>38</td><td>22</td><td>20</td><td>22</td><td>23</td><td>23</td><td>25</td><td>30</td><td>33</td><td>37</td></tr><tr><td>Server</td><td>27</td><td>35</td><td>45</td><td>48</td><td>52</td><td>57</td><td>67</td><td>63</td><td>87</td><td>148</td><td>264</td><td>463</td><td>629</td><td>847</td><td>1,077</td></tr><tr><td>GP server</td><td>27</td><td>35</td><td>45</td><td>48</td><td>52</td><td>57</td><td>65</td><td>54</td><td>60</td><td>64</td><td>90</td><td>119</td><td>142</td><td>167</td><td>189</td></tr><tr><td>AI server</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2</td><td>8</td><td>27</td><td>84</td><td>174</td><td>345</td><td>487</td><td>680</td><td>888</td></tr><tr><td>Others</td><td>3</td><td>3</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Consumer</td><td>811</td><td>848</td><td>900</td><td>955</td><td>985</td><td>993</td><td>991</td><td>1,000</td><td>1,043</td><td>1,077</td><td>1,099</td><td>1,122</td><td>1,153</td><td>1,184</td><td>1,230</td></tr><tr><td>TV</td><td>444</td><td>452</td><td>476</td><td>490</td><td>503</td><td>491</td><td>478</td><td>484</td><td>502</td><td>511</td><td>517</td><td>533</td><td>543</td><td>554</td><td>564</td></tr><tr><td>Appliance</td><td>344</td><td>375

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 12 Jun 2026 07:29 PM HKT

Disseminated 12 Jun 2026 10:21 PM HKT
"""
