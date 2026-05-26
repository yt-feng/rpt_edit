你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# EM USD 10s30s Spread Curve Report

- This is the weekly analytics version of the EM USD 10s30s Spread Curve Report. This will be updated on a weekly basis, posted on JPMmarkets, and included in our EM Daily Analytics Package email. The monthly version will continue to be produced and emailed out separately, including our commentary.   
- The EM aggregate 10s30s data is also available on Bloomberg and will be updated weekly. It can be accessed using the below tickers:

<table><tr><td>Aggregate</td><td>Bloomberg Tickers</td></tr><tr><td>EM Aggregate 10s30s</td><td>JPCUEMAG Index</td></tr><tr><td>EM IG 10s30s</td><td>JPCUEMAI Index</td></tr><tr><td>EM HY 10s30s</td><td>JPCUEMAH Index</td></tr><tr><td>EMBIG 10s30s</td><td>JPCUEMBG Index</td></tr><tr><td>EMBIG IG 10s30s</td><td>JPCUEMBI Index</td></tr><tr><td>EMBIG HY 10s30s</td><td>JPCUEMBH Index</td></tr><tr><td>CEMBI 10s30s</td><td>JPCUCEMB Index</td></tr><tr><td>CEMBI IG 10s30s</td><td>JPCUCEMI Index</td></tr><tr><td>CEMBI HY 10s30s</td><td>JPCUCEMH Index</td></tr></table>

• See here for rules and methodology and here for an archive of previous reports.

Figure 1: EM USD Aggregate 10s30s   
![](images/720ba8967c62bfc191b1f11c883c002b9a44df83f47e4160e8a9cbbe7848c684.jpg)

<details>
<summary>line</summary>

| Year | EM USD Aggregate 10s30s Spread Index |
| ---- | ------------------------------------- |
| 2025 | 68                                    |
</details>

Figure 2: UST 10s30s yield curve slope   
![](images/12fc6a0afb78bc11900f27271a2cdca0f2e45e59fc86079c9787c5b93c647fea.jpg)

<details>
<summary>line</summary>

| Date   | UST 10s30s |
|--------|------------|
| Mar-21 | 70         |
| May-22 | 0          |
| May-23 | 10         |
| May-24 | 20         |
| May-25 | 40         |
| May-26 | 60         |
</details>

Figure 3: Steepest and flattest 10s30s curves   
![](images/a13ead584c14588012f41169ce91f9e4c591fec74c30cb59636244b731e3dd9b.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| EGYPT | 159 |
| ELSALV | 117 |
| SOAF | 112 |
| PEMEX | 110 |
| UAE | 91 |
| PETMK | 38 |
| GRUMAB | 37 |
| EXIMBK | 34 |
| SQM | 31 |
| INDON | 20 |
</details>

Source: (all charts and data in this report) JPM. Levels as of 22nd May 2026 EOD.

Figure 4: Largest 1w changes in 10s30s   
![](images/0843a7fcb1d0517fe7888985c7e01a3968ffdf06cb07a1f199f98475eb1b8223.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| ELSALV | +6 |
| ROMANI | +5 |
| PIFKSA | +4 |
| MUBAUH | +3 |
| UAE | +3 |
| PEMEX | -8 |
| SOAF | -9 |
| ARAMCO | -9 |
| GRUMAB | -9 |
| INDON | -14 |
</details>

# Emerging Markets Strategy

# Ankit Chawla AC

(91-22) 6157-3281

ankit.chawla@jpmchase.com

JPM India Private Limited

# Nishant M Poojary, CFA

(44 20) 3493-3859

nishant.m.poojary@JPM.com

JPM Securities plc

# Emerging Markets Corporate Strategy

# Yang-Myung Hong

(1-212) 834-4274

ym.hong@JPM.com

JPM Securities LLC

# Global Index Research

# Pallav Poddar

(44 20) 3493-5201

pallav.poddar@JPM.com

JPM Securities plc

Contents 

<table><tr><td>10s30s Spread Curve Overview</td><td>2</td></tr><tr><td>Slope versus Spread Level Relationship by Region</td><td>5</td></tr><tr><td>Slope versus Spread Level Relationship by Index</td><td>6</td></tr><tr><td>Slope versus Credit Rating Relationship</td><td>7</td></tr><tr><td>Steepest and Flattest 10s30s Spread Curves in EM Credit</td><td>8</td></tr><tr><td>Largest 1-Week Steepening and Flattening</td><td>9</td></tr><tr><td>Asia 10s30s Spread Curves</td><td>10</td></tr><tr><td>CEEMEA 10s30s Spread Curves</td><td>11</td></tr><tr><td>Latin America 10s30s Spread Curves</td><td>13</td></tr></table>

# 10s30s Spread Curve Overview

Figure 5: Summary of 10s30s curves across EM sovereigns, EM corporates, US HG and US Treasuries 

<table><tr><td>Aggregate</td><td>Current</td><td>1w</td><td>1y</td><td>10y Spd</td><td>30y Spd</td><td>1y Avg</td><td>1y Low</td><td></td><td>1y High</td><td>1y High</td><td>Index</td><td>Region</td><td>Count</td></tr><tr><td>EM Aggregate</td><td>68</td><td>-2</td><td>-7</td><td>178</td><td>246</td><td>68</td><td>58</td><td>●</td><td>○</td><td>●</td><td>79</td><td>Agg</td><td>Global</td></tr><tr><td>EM IG</td><td>61</td><td>-2</td><td>-11</td><td>132</td><td>194</td><td>62</td><td>52</td><td>●</td><td>○</td><td>●</td><td>76</td><td>Agg</td><td>Global</td></tr><tr><td>EM HY</td><td>83</td><td>-3</td><td>+2</td><td>283</td><td>366</td><td>80</td><td>70</td><td>●</td><td></td><td>○</td><td>86</td><td>Agg</td><td>Global</td></tr><tr><td>EMBIG</td><td>71</td><td>-2</td><td>-6</td><td>179</td><td>251</td><td>71</td><td>61</td><td>●</td><td></td><td>○</td><td>79</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG Sov</td><td>72</td><td>-1</td><td>-3</td><td>193</td><td>265</td><td>71</td><td>61</td><td>●</td><td></td><td>○</td><td>79</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG Quasi</td><td>60</td><td>-3</td><td>-10</td><td>140</td><td>200</td><td>62</td><td>53</td><td>●</td><td></td><td>○</td><td>71</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG Asia</td><td>35</td><td>-6</td><td>-24</td><td>99</td><td>133</td><td>42</td><td>30</td><td>●</td><td>○</td><td>●</td><td>61</td><td>EMBIG</td><td>Asia</td></tr><tr><td>EMBIG CEEMEA</td><td>81</td><td>-0</td><td>+10</td><td>188</td><td>268</td><td>72</td><td>57</td><td>●</td><td></td><td></td><td>84</td><td>EMBIG</td><td>CEEMEA</td></tr><tr><td>EMBIG LatAm</td><td>66</td><td>-1</td><td>-16</td><td>193</td><td>259</td><td>71</td><td>61</td><td>●</td><td>○</td><td></td><td>82</td><td>EMBIG</td><td>Latin America</td></tr><tr><td>EMBIG IG</td><td>63</td><td>-1</td><td>-10</td><td>133</td><td>197</td><td>64</td><td>52</td><td>●</td><td></td><td>○</td><td>75</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG HY</td><td>88</td><td>-3</td><td>+2</td><td>273</td><td>362</td><td>86</td><td>76</td><td>●</td><td></td><td></td><td>94</td><td>EMBIG</td><td>Global</td></tr><tr><td>CEMBI</td><td>55</td><td>-4</td><td>-14</td><td>174</td><td>229</td><td>56</td><td>39</td><td>●</td><td></td><td>○</td><td>76</td><td>CEMBI</td><td>Global</td></tr><tr><td>CEMBI Asia</td><td>57</td><td>-5</td><td>+10</td><td>59</td><td>116</td><td>53</td><td>40</td><td>●</td><td></td><td>○</td><td>65</td><td>CEMBI</td><td>Asia</td></tr><tr><td>CEMBI CEEMEA</td><td>61</td><td>-5</td><td>-29</td><td>153</td><td>214</td><td>67</td><td>55</td><td>●</td><td>○</td><td></td><td>95</td><td>CEMBI</td><td>CEEMEA</td></tr><tr><td>CEMBI LatAm</td><td>52</td><td>-4</td><td>-5</td><td>216</td><td>268</td><td>50</td><td>24</td><td>●</td><td></td><td>○</td><td>68</td><td>CEMBI</td><td>Latin America</td></tr><tr><td>CEMBI IG</td><td>56</td><td>-5</td><td>-16</td><td>128</td><td>183</td><td>58</td><td>38</td><td>●</td><td></td><td>○</td><td>79</td><td>CEMBI</td><td>Global</td></tr><tr><td>CEMBI HY</td><td>52</td><td>-2</td><td>-5</td><td>335</td><td>387</td><td>47</td><td>20</td><td>●</td><td></td><td></td><td>68</td><td>CEMBI</td><td>Global</td></tr><tr><td>US High Grade</td><td>15</td><td>-2</td><td>-4</td><td>82</td><td>92</td><td>16</td><td>10</td><td>●</td><td></td><td>○</td><td>22</td><td>JULI</td><td>US</td></tr><tr><td>US Treasuries</td><td>51</td><td>-2</td><td>-0</td><td>457</td><td>508</td><td>60</td><td>45</td><td>●</td><td>○</td><td></td><td>70</td><td>GBI-US</td><td>US</td></tr></table>

Figure 6: 10s30s curves vs. the 10y level relationship   
![](images/37dead1ff59dcd971608ead8a5d0b28d4a5dc643b9476238f43979d76564e946.jpg)

<details>
<summary>scatter</summary>

| Currency         | 10y spread | 10s30s curve |
| ---------------- | ---------- | ------------ |
| EM AGgregates    | ~280       | ~82          |
| EMBIG CY         | ~280       | ~82          |
| EMBIG CEEMEA     | ~190       | ~80          |
| EMBIG AGGAGE     | ~180       | ~70          |
| EMBIG IG         | ~140       | ~65          |
| EMBIG SOV        | ~190       | ~70          |
| EMBIG LatAm      | ~150       | ~60          |
| CEMBI LatAm      | ~170       | ~55          |
| CEMBI QUasi      | ~130       | ~55          |
| CEMBI IG         | ~130       | ~60          |
| CEMBI Asia       | ~60        | ~55          |
| EMBIG Asia       | ~100       | ~35          |
| US High Grade    | ~80        | ~15          |
| CEMBI HY         | ~340       | ~50          |
| US Treasuries    | ~460       | ~50          |
</details>

Figure 7: 1w change in aggregate 10s30s vs. 1w change in aggregate 10 spreads   
![](images/7db12968867e6d592c5dcc6d054b7fe5500f1ccdd8cf755bf31e1ff9d0e4331d.jpg)

<details>
<summary>scatter</summary>

| Entity           | 1w change in 10y spread | 1w change in 10s30s curve |
| ---------------- | ---------------------- | ------------------------- |
| EM Aggregates    | ~3.5                   | ~-2.0                     |
| EM Big AGgregates| ~3.5                   | ~-2.0                     |
| EM Big SOV       | ~4.0                   | ~-1.0                     |
| EMBIG LatAm      | ~5.5                   | ~-1.0                     |
| EMBIG HY         | ~4.5                   | ~-2.5                     |
| EMBIG CeEMEA     | ~2.0                   | ~-0.5                     |
| EMBIG IG         | ~3.5                   | ~-1.0                     |
| EM IG            | ~3.5                   | ~-2.0                     |
| EM Aggregate     | ~3.5                   | ~-2.0                     |
| CEMBI HY         | ~1.5                   | ~-2.0                     |
| CEMBI LatAm      | ~3.5                   | ~-3.5                     |
| CEMBI            | ~2.5                   | ~-4.0                     |
| CEMBI IG         | ~3.0                   | ~-4.5                     |
| CEMBI Asia       | ~-3.5                  | ~-4.5                     |
| CEMBI Asia       | ~0.5                   | ~-6.0                     |
| CEMBI IG         | ~3.0                   | ~-4.5                     |
| CEMBI CEEMEA     | ~4.5                   | ~-4.5                     |
| US Treasuries    | ~-2.5                  | ~-2.5                     |
</details>

Figure 8: 1w change in 10s30s vs. 1w change in 10y spreads by issuer   
![](images/cea941e295e88e711a00b66f80d1377ded5b54e9b9d6a2c5b968702581709e34.jpg)

Figure 9: Historical EM aggregate 10s30s spread curve slope   
![](images/7fcb45dfc0ac36231d9836a7c871001f6320ae72937238967ff4c2654964495c.jpg)

<details>
<summary>line</summary>

| Date    | EM Aggregate 10s30s |
|---------|---------------------|
| May-21  | 100                 |
| May-22  | -80                 |
| May-23  | 80                  |
| May-24  | 70                  |
| May-25  | 60                  |
| May-26  | 70                  |
</details>

Figure 11: Historical EMBIG vs. CEMBI spread curve slope   
![](images/e6941032793ccf963d18115260cf0c89d471b887fb8faf5723a5111f857b7d6a.jpg)

<details>
<summary>line</summary>

| Date   | EMBIG 10s30s | CEMBI Broad 10s30s |
|--------|--------------|--------------------|
| May-21 | ~90          | ~90                |
| May-22 | ~-150        | ~90                |
| May-23 | ~80          | ~70                |
| May-24 | ~70          | ~60                |
| May-25 | ~60          | ~50                |
| May-26 | ~50          | ~40                |
</details>

Figure 13: Historical sovereign vs. quasi-sovereign curve slope   
![](images/74358a714661c57478cadb031cb2114f1aeaabf81c3e32fc17171bf5b00b0ae6.jpg)

<details>
<summary>line</summary>

| Date   | EMBIG Div Sovereign 10s30s | EMBIG Div Quasi 10s30s |
|--------|----------------------------|------------------------|
| May-21 | ~85                        | ~85                    |
| May-22 | ~-180                      | ~80                    |
| May-23 | ~80                        | ~75                    |
| May-24 | ~75                        | ~75                    |
| May-25 | ~75                        | ~75                    |
| May-26 | ~75                        | ~75                    |
</details>

Figure 15: Historical EMBIGD curve slope by region   
![](images/d8a1b92520e669105f868af6a29a626eb202c57d7070e853a55e625c22e5bfaf.jpg)

<details>
<summary>line</summary>

| Date   | EMBIG Div Asia 10s30s | EMBIG Div CEEMEA 10s30s | EMBIG Div LatAm 10s30s |
|--------|----------------------|-------------------------|------------------------|
| May-21 | ~50                  | ~50                     | ~50                    |
| May-22 | ~-350                | ~-350                   | ~-350                  |
| May-23 | ~50                  | ~50                     | ~50                    |
| May-24 | ~50                  | ~50                     | ~50                    |
| May-25 | ~50                  | ~50                     | ~50                    |
| May-26 | ~50                  | ~50                     | ~50                    |
</details>

Figure 10: Historical US Treasury 10s30s yield curve slope   
![](images/91d1306115d92ebff5903f686ce45839f941496364e7c14516cc290ffeccf4f1.jpg)

<details>
<summary>line</summary>

| Date   | UST 10s30s |
|--------|------------|
| May-21 | 70         |
| May-22 | 0          |
| May-23 | 40         |
| May-24 | 30         |
| May-25 | 60         |
| May-26 | 50         |
</details>

Figure 12: Historical EM IG vs. HY spread curve slope

![](images/b9448ecf155c80128fbe27218248cc614e6f6bca80eafe42c953d507a3d6e187.jpg)

<details>
<summary>line</summary>

| Date   | EM IG 10s30s | EM HY 10s30s |
|--------|--------------|--------------|
| May-21 | ~100         | ~100         |
| May-22 | ~-200        | ~-200        |
| May-23 | ~75          | ~75          |
| May-24 | ~75          | ~75          |
| May-25 | ~75          | ~75          |
| May-26 | ~75          | ~75          |
</details>

Figure 14: EM corporate vs. US HG corporate spread curve slope   
![](images/9eb8c7392358b750b19bbec77a361da0a6f8ca8c5c260f1f117e8b47a6916937.jpg)

<details>
<summary>line</summary>

| Date   | CEMBI Broad 10s30s | US HG 10s30s |
|--------|--------------------|--------------|
| May-21 | ~90                | ~35          |
| May-22 | ~100               | ~40          |
| May-23 | ~85                | ~25          |
| May-24 | ~70                | ~20          |
| May-25 | ~60                | ~15          |
| May-26 | ~50                | ~15          |
</details>

Figure 16: Historical CEMBI curve slope by region   
![](images/9ff67d79f04d06281f6a4d40c2b4c240ed8319740af60dbc58721c6ac9be046c.jpg)

<details>
<summary>line</summary>

| Date   | CEMBI Broad Asia 10s30s | CEMBI Broad CEEMEA 10s30s | CEMBI Broad LatAm 10s30s |
|--------|--------------------------|----------------------------|---------------------------|
| May-21 | ~60                      | ~60                        | ~120                      |
| May-22 | ~80                      | ~80                        | ~100                      |
| May-23 | ~70                      | ~70                        | ~90                       |
| May-24 | ~60                      | ~60                        | ~80                       |
| May-25 | ~50                      | ~50                        | ~70                       |
| May-26 | ~40                      | ~40                        | ~60                       |
</details>

# Slope versus Spread Level Relationship by Region

Figure 17: 10s30s spread curve slopes vs. 10y spread   
![](images/a90934d23c0f38b7c03bdb3f819d2fd0c7b4ef0cf6877f83b957dee4b84009b7.jpg)

<details>
<summary>scatter</summary>

| Region       | 10y spread | 10s30s spread curve |
| ------------ | ---------- | ------------------- |
| Asia         | 50         | 52                  |
| Asia         | 75         | 60                  |
| Asia         | 100        | 40                  |
| Asia         | 125        | 35                  |
| Asia         | 150        | 20                  |
| Asia         | 175        | 30                  |
| Asia         | 200        | 45                  |
| Asia         | 225        | 50                  |
| Asia         | 250        | 60                  |
| Asia         | 275        | 70                  |
| Asia         | 300        | 80                  |
| Asia         | 325        | 90                  |
| Asia         | 350        | 100                 |
| Asia         | 375        | 110                 |
| Asia         | 400        | 120                 |
| CEEMEA       | 60         | 80                  |
| CEEMEA       | 90         | 70                  |
| CEEMEA       | 120        | 65                  |
| CEEMEA       | 140        | 60                  |
| CEEMEA       | 160        | 55                  |
| CEEMEA       | 180        | 50                  |
| CEEMEA       | 200        | 45                  |
| CEEMEA       | 225        | 40                  |
| CEEMEA       | 250        | 35                  |
| CEEMEA       | 275        | 30                  |
| CEEMEA       | 300        | 25                  |
| CEEMEA       | 325        | 20                  |
| CEEMEA       | 350        | 15                  |
| CEEMEA       | 375        | 10                  |
| CEEMEA       | 400        | 5                   |
| Latin America| 125        | 75                  |
| Latin America| 150        | 70                  |
| Latin America| 175        | 65                  |
| Latin America| 200        | 60                  |
| Latin America| 225        | 55                  |
| Latin America| 250        | 50                  |
| Latin America| 275        | 45                  |
| Latin America| 300        | 40                  |
| Latin America| 325        | 35                  |
| Latin America| 350        | 30                  |
| Latin America| 375        | 25                  |
| Latin America| 400        | 20                  |
</details>

Figure 18: Asia issuers   
![](images/6dceda765787401a9152a3a86b82b1f591351652fb3c474414faadbf5ad52b19.jpg)

<details>
<summary>scatter</summary>

10s30s spread curve
| Label | 10y spread | 10s30s spread curve |
| :--- | :--- | :--- |
| EMBIG | 90 | 38 |
| CEMBI | 45 | 52 |
| MTRC | 55 | 60 |
| BABA | 70 | 60 |
| PETMK | 90 | 38 |
| EXIMBK | 110 | 34 |
| INDON | 130 | 20 |
</details>

Figure 19: CEEMEA issuers   
![](images/2c4a0050ba0b40e234e2457b4cd2b2b740aaf34d532c9e207b9ea7e68256f526.jpg)

<details>
<summary>scatter</summary>

| Country   | 10y spread | 10s30s spread curve |
| --------- | ---------- | ------------------- |
| EMBIG     | ~230       | ~165                |
| CEMBI     | ~140       | ~40                 |
| SOAF      | ~230       | ~110                |
| NGERIA    | ~310       | ~75                 |
| AALLN     | ~130       | ~40                 |
| ADQABU    | ~120      

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 26 May 2026 05:21 AM HKT

Disseminated 26 May 2026 06:41 AM HKT
"""
