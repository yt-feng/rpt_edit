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
# EM USD 10s30s Spread Curve Report

- This is the weekly analytics version of the EM USD 10s30s Spread Curve Report. This will be updated on a weekly basis, posted on JPMmarkets, and included in our EM Daily Analytics Package email. The monthly version will continue to be produced and emailed out separately, including our commentary.  
- The EM aggregate 10s30s data is also available on Bloomberg and will be updated weekly. It can be accessed using the below tickers:

<table><tr><td>Aggregate</td><td>Bloomberg Tickers</td></tr><tr><td>EM Aggregate 10s30s</td><td>JPCUEMAG Index</td></tr><tr><td>EM IG 10s30s</td><td>JPCUEMAI Index</td></tr><tr><td>EM HY 10s30s</td><td>JPCUEMAH Index</td></tr><tr><td>EMBIG 10s30s</td><td>JPCUEMBG Index</td></tr><tr><td>EMBIG IG 10s30s</td><td>JPCUEMBI Index</td></tr><tr><td>EMBIG HY 10s30s</td><td>JPCUEMBH Index</td></tr><tr><td>CEMBI 10s30s</td><td>JPCUCEMB Index</td></tr><tr><td>CEMBI IG 10s30s</td><td>JPCUCEMI Index</td></tr><tr><td>CEMBI HY 10s30s</td><td>JPCUCEMH Index</td></tr></table>

• See here for rules and methodology and here for an archive of previous reports.

Figure 1: EM USD Aggregate 10s30s  
![](images/53ddd43813608ccc90b4defff48e013b5ec30e5fbd7d463f339b5d0a503906e6.jpg)

<details>
<summary>line chart</summary>

| Year | EM USD Aggregate 10s30s Spread Index |
| ---- | ------------------------------------- |
| 2025 | 67                                    |
</details>

Figure 2: UST 10s30s yield curve slope  
![](images/d638962e7e97dd8dd12fc464a6dbeb7929ce98ffc3052f7b153dfb7bfbe78a98.jpg)

<details>
<summary>line chart</summary>

| Date   | UST 10s30s |
|--------|------------|
| Jun-21 | 60         |
| Jun-22 | 0          |
| Jun-23 | 20         |
| Jun-24 | 40         |
| Jun-25 | 60         |
| Jun-26 | 50         |
</details>

Figure 3: Steepest and flattest 10s30s curves  
![](images/25450fd5dc334cfaa54f821cbf99e1d88571cfac89765c9b33390c201fb39517.jpg)

<details>
<summary>bar chart</summary>

| Category | Value |
|---|---|
| EGYPT | 134 |
| PEMEX | 112 |
| ELSALV | 109 |
| SOAF | 107 |
| KSA | 88 |
| CHILE | 38 |
| BIMBOA | 37 |
| EXIMBK | 28 |
| SQM | 25 |
| INDON | 8 |
The chart is divided into two sections: 'Steepest' and 'Flattest'. The values for each section are explicitly labeled on the bars.
</details>

Source: (all charts and data in this report) JPM. Levels as of 12th June 2026 EOD.

Figure 4: Largest 1w changes in 10s30s  
![](images/e46394efbdff6627f35aeda3150afc54ace827e99a6f246986e89bb27f0e5829.jpg)

<details>
<summary>bar chart</summary>

| Category | Value |
|---|---|
| AALLN | +7 |
| INDON | +7 |
| BABA | +5 |
| REPHUN | +4 |
| JBS | +4 |
| BGOSK | -9 |
| PARGUY | -10 |
| AITOCU | -10 |
| EXIMBK | -12 |
| EGYPT | -18 |
</details>

## Emerging Markets Strategy

## Ankit Chawla AC

(91-22) 6157-3281

ankit.chawla@jpmchase.com

JPM India Private Limited

## Nishant M Poojary, CFA

(44 20) 3493-3859

nishant.m.poojary@JPM.com

JPM Securities plc

## Emerging Markets Corporate Strategy

## Yang-Myung Hong

(1-212) 834-4274

ym.hong@JPM.com

JPM Securities LLC

## Global Index Research

## Pallav Poddar

(44 20) 3493-5201

pallav.poddar@JPM.com

JPM Securities plc

Contents

<table><tr><td>10s30s Spread Curve Overview</td><td>2</td></tr><tr><td>Slope versus Spread Level Relationship by Region</td><td>5</td></tr><tr><td>Slope versus Spread Level Relationship by Index</td><td>6</td></tr><tr><td>Slope versus Credit Rating Relationship</td><td>7</td></tr><tr><td>Steepest and Flattest 10s30s Spread Curves in EM Credit</td><td>8</td></tr><tr><td>Largest 1-Week Steepening and Flattening</td><td>9</td></tr><tr><td>Asia 10s30s Spread Curves</td><td>10</td></tr><tr><td>CEEMEA 10s30s Spread Curves</td><td>11</td></tr><tr><td>Latin America 10s30s Spread Curves</td><td>13</td></tr></table>

## 10s30s Spread Curve Overview

Figure 5: Summary of 10s30s curves across EM sovereigns, EM corporates, US HG and US Treasuries

<table><tr><td>Aggregate</td><td>Current</td><td>1w</td><td>1y</td><td>10y Spd</td><td>30y Spd</td><td>1y Avg</td><td>1y Low</td><td></td><td>1y High</td><td>Index</td><td>Region</td><td>Count</td></tr><tr><td>EM Aggregate</td><td>67</td><td>-2</td><td>-10</td><td>171</td><td>237</td><td>67</td><td>58</td><td>●</td><td>◆○</td><td>77</td><td>Agg</td><td>Global</td></tr><tr><td>EM IG</td><td>61</td><td>-1</td><td>-14</td><td>130</td><td>191</td><td>62</td><td>52</td><td>●</td><td>◆○</td><td>75</td><td>Agg</td><td>Global</td></tr><tr><td>EM HY</td><td>79</td><td>-3</td><td>-3</td><td>258</td><td>337</td><td>80</td><td>70</td><td>●</td><td>◆○</td><td>86</td><td>Agg</td><td>Global</td></tr><tr><td>EMBIG</td><td>69</td><td>-2</td><td>-8</td><td>172</td><td>241</td><td>71</td><td>61</td><td>●</td><td>◆○</td><td>79</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG Sov</td><td>68</td><td>-2</td><td>-8</td><td>183</td><td>251</td><td>71</td><td>61</td><td>●</td><td>◆○</td><td>79</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG Quasi</td><td>61</td><td>-4</td><td>-9</td><td>137</td><td>198</td><td>61</td><td>53</td><td>●</td><td>◆○</td><td>70</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG Asia</td><td>36</td><td>-2</td><td>-20</td><td>103</td><td>139</td><td>41</td><td>30</td><td>●</td><td>◆○</td><td>56</td><td>EMBIG</td><td>Asia</td></tr><tr><td>EMBIG CEEMEA</td><td>76</td><td>-3</td><td>+1</td><td>182</td><td>258</td><td>72</td><td>57</td><td>●</td><td>◆○</td><td>84</td><td>EMBIG</td><td>CEEMEA</td></tr><tr><td>EMBIG LatAm</td><td>65</td><td>-3</td><td>-14</td><td>180</td><td>245</td><td>70</td><td>61</td><td>●</td><td>◆○</td><td>81</td><td>EMBIG</td><td>Latin America</td></tr><tr><td>EMBIG IG</td><td>61</td><td>-2</td><td>-12</td><td>131</td><td>192</td><td>63</td><td>52</td><td>●</td><td>◆○</td><td>74</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG HY</td><td>84</td><td>-3</td><td>-1</td><td>253</td><td>337</td><td>86</td><td>76</td><td>●</td><td>◆○</td><td>94</td><td>EMBIG</td><td>Global</td></tr><tr><td>CEMBI</td><td>58</td><td>-0</td><td>-17</td><td>166</td><td>224</td><td>55</td><td>39</td><td>●</td><td>◆○</td><td>75</td><td>CEMBI</td><td>Global</td></tr><tr><td>CEMBI Asia</td><td>60</td><td>+3</td><td>+6</td><td>65</td><td>125</td><td>53</td><td>40</td><td>●</td><td>◆○</td><td>65</td><td>CEMBI</td><td>Asia</td></tr><tr><td>CEMBI CEEMEA</td><td>63</td><td>-0</td><td>-28</td><td>152</td><td>215</td><td>66</td><td>55</td><td>●</td><td>◆○</td><td>93</td><td>CEMBI</td><td>CEEMEA</td></tr><tr><td>CEMBI LatAm</td><td>54</td><td>-1</td><td>-14</td><td>206</td><td>260</td><td>49</td><td>24</td><td>●</td><td>◆○</td><td>68</td><td>CEMBI</td><td>Latin America</td></tr><tr><td>CEMBI IG</td><td>59</td><td>+1</td><td>-17</td><td>129</td><td>188</td><td>57</td><td>38</td><td>●</td><td>◆○</td><td>77</td><td>CEMBI</td><td>Global</td></tr><tr><td>CEMBI HY</td><td>52</td><td>-2</td><td>-15</td><td>285</td><td>338</td><td>47</td><td>20</td><td>●</td><td>◆○</td><td>68</td><td>CEMBI</td><td>Global</td></tr><tr><td>US High Grade</td><td>15</td><td>-0</td><td>-1</td><td>83</td><td>93</td><td>16</td><td>10</td><td>●</td><td>◆○</td><td>22</td><td>JULI</td><td>US</td></tr><tr><td>US Treasuries</td><td>49</td><td>+3</td><td>+0</td><td>448</td><td>497</td><td>60</td><td>46</td><td>●</td><td>◆○</td><td>70</td><td>GBI-US</td><td>US</td></tr></table>

Figure 6: 10s30s curves vs. the 10y level relationship  
![](images/954064955d9dfbe5a5ec44787242031aa56e9b3c130c874479f548350d9e1292.jpg)

<details>
<summary>scatterplot</summary>

| Entity | 10y spread | 10s30s curve |
| --- | --- | --- |
| EM AGgregates | 250 | 80 |
| EMHY | 250 | 85 |
| EMBIG | 180 | 75 |
| EMBIG Asia | 100 | 35 |
| CEMBI Asia | 60 | 60 |
| EM Bigl AGg | 130 | 65 |
| EM Bigl Coasi | 130 | 60 |
| EM Bigl LatAm | 150 | 65 |
| EM Bigl CG | 130 | 60 |
| EM Bigl Cyemea | 170 | 70 |
| EM Bigl Syb | 170 | 65 |
| EM Bigl AGg | 170 | 65 |
| EM Bigl Cyemea | 180 | 70 |
| EM Bigl Syb | 180 | 65 |
| EM Bigl Cyemea | 180 | 65 |
| EM Bigl Syb | 180 | 65 |
| EM Bigl Cyemea | 180 | 65 |
| EM Bigl Syb | 180 | 65 |
| EM Bigl Cyemea | 180 | 65 |
| EM Bigl Syb | 180 | 65 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
| CEMBI | 130 | 60 |
</details>

Figure 7: 1w change in aggregate 10s30s vs. 1w change in aggregate 10 spreads  
![](images/9bfa3507da89cebbbcc0fd706eb2b1e5c2ef6facff984a92c5cfdc791d7978d5.jpg)

<details>
<summary>scatterplot</summary>

| Entity           | 1w change in 10y spread | 1w change in 10s30s curve |
| ---------------- | ------------------------ | -------------------------- |
| US Treasuries     | -5.0                     | +2.5                       |
| CEMBI HY         | -6.0                     | -2.0                       |
| EM HY            | -2.5                     | -3.0                       |
| EMBIG HY         | -2.0                     | -3.0                       |
| CEMBI LatAm      | -1.5                     | -1.0                       |
| EM Aggregate     | -0.5                     | -2.0                       |
| CEMBI CGM        | -0.5                     | -2.0                       |
| EMBIG CGM        | -0.5                     | -2.0                       |
| CEMBI IG         | 2.0                      | -0.5                       |
| CEMBI CEEMEA     | 2.5                      | -0.5                       |
| EM IG            | 1.0                      | -1.5                       |
| EMBIG Asia       | 1.5                      | -2.0                       |
| EMBIG LatAm      | 0.5                      | -2.5                       |
| EMBIG Quasi      | 2.5                      | -4.5                       |
| CEMBI Asia       | 2.5                      | 3.0                        |
| CEMBI IG         | 2.0                      | -0.5                       |
| CEMBI CEEMEA     | 1.5                      | -0.5                       |
| EM Big            | 1.0                      | -1.5                       |
| EMBIG Secu        | 0.5                      | -2.0                       |
| EMBIG Hy         | -1.5                     | -2.5                       |
| EM Big            | -1.0                     | -2.5                       |
| EMBIG Secu        | -1.0                     | -2.5                       |
| EMBIG LatAm      | 0.5                      | -2.5                       |
| EMBIG Quasi      | 2.5                      | -4.5                       |
| Bear Steepening   | 2.5                      | -3.0                       |
| Bear Flattening   | 2.5                      | -4.5                       |
</details>

Figure 8: 1w change in 10s30s vs. 1w change in 10y spreads by issuer  
![](images/ba2278c25d38462a1b1375324dcd1c6d54cb52c04c471e730c11b4e5ac582030.jpg)

<details>
<summary>scatterplot</summary>

| 1w change in 10y spread | 1w change in 10s30s | Category |
| --- | --- | --- |
| -12.5 | -1.2 | EMBIG SOV |
| -11.8 | -1.0 | EMBIG SOV |
| -10.5 | -0.8 | EMBIG SOV |
| -9.2 | -0.6 | EMBIG SOV |
| -8.5 | -0.4 | EMBIG SOV |
| -7.8 | -0.2 | EMBIG SOV |
| -6.5 | 0.0 | EMBIG SOV |
| -5.2 | 0.2 | EMBIG SOV |
| -4.8 | 0.4 | EMBIG SOV |
| -3.5 | 0.6 | EMBIG SOV |
| -2.8 | 0.8 | EMBIG SOV |
| -1.5 | 1.0 | EMBIG SOV |
| -0.8 | 1.2 | EMBIG SOV |
| 0.5 | 1.4 | EMBIG SOV |
| 1.2 | 1.6 | EMBIG SOV |
| 2.0 | 1.8 | EMBIG SOV |
| 3.5 | 2.0 | EMBIG SOV |
| 4.2 | 2.2 | EMBIG SOV |
| 5.8 | 2.4 | EMBIG SOV |
| 7.5 | 2.6 | EMBIG SOV |
| 9.0 | 2.8 | EMBIG SOV |
| 10.5 | 3.0 | EMBIG SOV |
| 12.0 | 3.2 | EMBIG SOV |
| 13.5 | 3.4 | EMBIG SOV |
| 15.0 | 3.6 | EMBIG SOV |
| 16.5 | 3.8 | EMBIG SOV |
| -12.0 | -1.5 | EMBIG QUASI |
| -10.8 | -1.3 | EMBIG QUASI |
| -9.5 | -1.1 | EMBIG QUASI |
| -8.2 | -0.9 | EMBIG QUASI |
| -7.0 | -0.7 | EMBIG QUASI |
| -5.8 | -0.5 | EMBIG QUASI |
| -4.5 | -0.3 | EMBIG QUASI |
| -3.2 | -0.1 | EMBIG QUASI |
| -2.0 | 0.1 | EMBIG QUASI |
| -0.8 | 0.3 | EMBIG QUASI |
| 0.5 | 0.5 | EMBIG QUASI |
| 1.8 | 0.7 | EMBIG QUASI |
| 3.2 | 0.9 | EMBIG QUASI |
| 4.5 | 1.1 | EMBIG QUASI |
| 6.0 | 1.3 | EMBIG QUASI |
| 7.5 | 1.5 | EMBIG QUASI |
| 9.0 | 1.7 | EMBIG QUASI |
| 10.5 | 1.9 | EMBIG QUASI |
| 12.0 | 2.1 | EMBIG QUASI |
| 13.5 | 2.3 | EMBIG QUASI |
| 15.0 | 2.5 | EMBIG QUASI |
| 16.5 | 2.7 | EMBIG QUASI |
| -12.5 | -1.8 | CEMBI |
| -11.5 | -1.6 | CEMBI |
| -9.8 | -1.4 | CEMBI |
| -8.5 | -1.2 | CEMBI |
| -7.2 | -1.0 | CEMBI |
| -6.0 | -0.8 | CEMBI |
| -4.8 | -0.6 | CEMBI |
| -3.5 | -0.4 | CEMBI |
| -2.2 | -0.2 | CEMBI |
| -1.0 | 0.0 | CEMBI |
| 0.2 | 0.2 | CEMBI |
| 1.5 | 0.4 | CEMBI |
| 2.8 | 0.6 | CEMBI |
| 4.2 | 0.8 | CEMBI |
| 5.5 | 1.0 | CEMBI |
| 7.0 | 1.2 | CEMBI |
| 8.5 | 1.4 | CEMBI |
| 10.0 | 1.6 | CEMBI |
| 11.5 | 1.8 | CEMBI |
| 13.0 | 2.0 | CEMBI |
| 14.5 | 2.2 | CEMBI |
| 16.0 | 2.4 | CEMBI |
| -13.0 | -2.0 | Bull flattening |
| -11.5 | -1.8 | Bull flattening |
| -9.8 | -1.6 | Bull flattening |
| -8.5 | -1.4 | Bull flattening |
| -7.2 | -1.2 | Bull flattening |
| -6.0 | -1.0 | Bull flattening |
| -4.8 | -0.8 | Bull flattening |
| -3.5 | -0.6 | Bull flattening |
| -2.2 | -0.4 | Bull flattening |
| -1.0 | -0.2 | Bull flattening |
| 0.2 | 0.0 | Bull flattening |
| 1.5 | 0.2 | Bull flattening |
| 2.8 | 0.4 | Bull flattening |
| 4.2 | 0.6 | Bull flattening |
| 5.5 | 0.8 | Bull flattening |
| 7.0 | 1.0 | Bull flattening |
| 8.5 | 1.2 | Bull flattening |
| 10.0 | 1.4 | Bull flattening |
| 11.5 | 1.6 | Bull flattening |
| 13.0 | 1.8 | Bull flattening |
| 14.5 | 2.0 | Bull flattening |
| -13.5 | -2.2 | Bear steepening |
| -12.5 | -2.0 | Bear steepening |
| -9.8 | -1.8 | Bear steepening |
| -8.5 | -1.6 | Bear steepening |
| -7.2 | -1.4 | Bear steepening |
| -6.0 | -1.2 | Bear steepening |
| -4.8 | -1.0 | Bear steepening |
| -3.5 | -0.8 | Bear steepening |
| -2.2 | -0.6 | Bear steepening |
| -1.0 | -0.4 | Bear steepening |
| 0.2 | -0.2 | Bear steepening |
| 1.5 | 0.0 | Bear steepening |
| 2.8 | 0.2 | Bear steepening |
| 4.2 | 0.4 | Bear steepening |
| 5.5 | 0.6 | Bear steepening |
| 7.0 | 0.8 | Bear steepening |
| 8.5 | 1.0 | Bear steepening |
| 10.0 | 1.2 | Bear steepening |
| 11.5 | 1.4 | Bear steepening |
| 13.0 | 1.6 | Bear steepening |
| 14.5 | 1.8 | Bear steepening |
| -14.5 | -2.4 | Bull flattening |
| -13.5 | -2.2 | Bull flattening |
| -12.5 | -2.0 | Bull flattening |
| -9.8 | -1.8 | Bull flattening |
| -8.5 | -1.6 | Bull flattening |
| -7.2 | -1.4 | Bull flattening |
| -6.0 | -1.2 | Bull flattening |
| -4.8 | -1.0 | Bull flattening |
| -3.5 | -0.8 | Bull flattening |
| -2 .2 | -0.6 | Bull flattening |
| -1 .0 | -0.4 | Bull flattening |
| 0 .2 | -0.2 | Bull flattening |
| 1 .5 | 0 .0 | Bull flattening |
| 2 .8 | 0 .2 | Bull flattening |
| 4 .2 | 0 .4 | Bull flattening |
| 6 .5 | 0 .6 | Bull flattening |
| 8 .8 | 0 .8 | Bull flattening |
| 11 .2 | 1 .0 | Bull flattening |
| 13 .5 | 1 .2 | Bull flattening |
</details>

Figure 9: Historical EM aggregate 10s30s spread curve slope  
![](images/2dced8dca0dcfb51675b7fdcba9a83e5cfecb5df7cfbaeec0631aa868d7df142.jpg)

<details>
<summary>line chart</summary>

| Date    | EM Aggregate 10s30s |
|---------|---------------------|
| Jun-21  | 100                 |
| Jun-22  | -80                 |
| Jun-23  | 80                  |
| Jun-24  | 70                  |
| Jun-25  | 60                  |
| Jun-26  | 70                  |
</details>

Figure 11: Historical EMBIG vs. CEMBI spread curve slope  
![](images/a709be78310e7188a769ac66bd0937f9e4fdcf3d8e838e1c260d9b56c47fc0cd.jpg)

<details>
<summary>line chart</summary>

| Date   | EMBIG 10s30s | CEMBI Broad 10s30s |
|--------|--------------|--------------------|
| Jun-21 | ~90     

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 16 Jun 2026 03:19 AM HKT

Disseminated 16 Jun 2026 03:19 AM HKT
"""
