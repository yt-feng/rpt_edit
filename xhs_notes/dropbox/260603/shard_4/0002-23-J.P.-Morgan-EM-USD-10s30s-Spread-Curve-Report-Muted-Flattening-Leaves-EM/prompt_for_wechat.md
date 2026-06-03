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

Muted Flattening Leaves EM Spread Curve Shape Intact

- After a broad EM steepening move last month, curves have flattened slightly. The EM aggregate 10s30s curve bull flattened by 1bp to 68bp over the past month, driven by EM IG flattening by 1bp m/m to 61bp. The EMBIG curve followed the overall muted bull flattening move, tightening by 1bp to 71bp, with EMBIG Asia driving the move by flattening 7bp m/m to 37bp. Over the past month, the UST 10s30s curve bear flattened by 6bp to 54bp, while the US HG 10s30s curve also flattened by 2bp to 16bp.   
- CEMBI also flattened marginally by -1bp m/m to 56bp, led by Latin America (-1bp m/m to 52bp). The magnitude of the bull flattening was more more substantial in the individual pairs within the region, but the average move was mitigated by the exit of the flattest issuer. CEMBI CEEMEA (-2bp m/m to 60bp) flattened as well, whereas CEMBI Asia (+3bp m/m to 61bp) steepened. Overall, the curves have been relatively stable on average despite the meaningful swings in UST yields.   
- TThe largest steepening over the month was led by DOMREP (11bp), CDEL (9bp), BABA (7bp), KSA (7bp), and PARGUY (7bp). Meanwhile, the largest flattening over the month was led by INDON (-26bp), GRUMAB (-13bp), EGYPT (-12bp), SQM (-12bp), and AITOCU (-11bp).   
- Steepest curves are led by EGYPT (141bp), PEMEX (121bp), ELSALV (116bp), SOAF (104bp), and KSA (90bp). Meanwhile, the flattest curves are led by INDON (9bp), SQM (22bp), GRUMAB (39bp), EXIMBK (39bp) and ECOPET (41bp).   
- Composition changes: At the May month-end rebalance, EGYPT and INDON now reference a new 10-year or 30-year pair in the EMBI 10s30s index. In the CEMBI 10s30s index, BIMBOA exits.

See here for rules and methodology and here for the archive of previous reports

Figure 1: Steepest and flattest 10s30s curves   
![](images/0f747467f25eaec994a5f4375448e271749f6d6305339aadc02b80849d547a3a.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| EGYPT | 141 |
| PEMEX | 121 |
| ELSALV | 116 |
| SOAF | 104 |
| KSA | 90 |
| ECOPET | 41 |
| EXIMBK | 39 |
| GRUMAB | 39 |
| SQM | 22 |
| INDON | 9 |
</details>

Source: All charts and data in this report: JPM. Levels as of 29th May 2026, COB.

Figure 2: Largest 1m changes in 10s30s   
![](images/390594e5c878f4b82a84fe4a8fe0c27dc60fa04e022e1e1c9932de264b771772.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| DOMREP | +11 |
| CDEL | +9 |
| BABA | +7 |
| KSA | +7 |
| PARGUY | +7 |
| AITOCU | -11 |
| SQM | -12 |
| EGYPT | -12 |
| GRUMAB | -13 |
| INDON | -26 |
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

# 10s30s Spread Curve Overview

Figure 3: Summary of 10s30s curves across EM sovereigns, EM corporates, US HG and US Treasuries 

<table><tr><td>Aggregate</td><td>Current</td><td>1m</td><td>1y</td><td>10y Spd</td><td>30y Spd</td><td>1y Avg</td><td>1y Low</td><td>1y Low○ 1m ago</td><td>1y High● Current</td><td>1y High</td><td>Index</td><td>Region</td><td>Count</td></tr><tr><td>EM Aggregate</td><td>68</td><td>-1</td><td>-10</td><td>177</td><td>245</td><td>67</td><td>58</td><td>●</td><td>◆</td><td>●</td><td>79</td><td>Agg</td><td>Global</td></tr><tr><td>EM IG</td><td>61</td><td>-1</td><td>-14</td><td>132</td><td>193</td><td>62</td><td>52</td><td>●</td><td>◆</td><td>○</td><td>76</td><td>Agg</td><td>Global</td></tr><tr><td>EM HY</td><td>82</td><td>+0</td><td>-2</td><td>275</td><td>357</td><td>80</td><td>70</td><td>●</td><td></td><td>◆</td><td>86</td><td>Agg</td><td>Global</td></tr><tr><td>EMBIG</td><td>71</td><td>-1</td><td>-8</td><td>178</td><td>249</td><td>71</td><td>61</td><td>●</td><td></td><td>◆</td><td>79</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG Sov</td><td>70</td><td>-1</td><td>-7</td><td>190</td><td>260</td><td>71</td><td>61</td><td>●</td><td></td><td>◆</td><td>79</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG Quasi</td><td>63</td><td>-2</td><td>-8</td><td>138</td><td>201</td><td>61</td><td>53</td><td>●</td><td></td><td>◆</td><td>71</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG Asia</td><td>37</td><td>-7</td><td>-23</td><td>99</td><td>136</td><td>41</td><td>30</td><td>●</td><td>◆</td><td>○</td><td>61</td><td>EMBIG</td><td>Asia</td></tr><tr><td>EMBIG CEEMEA</td><td>77</td><td>-1</td><td>+4</td><td>186</td><td>263</td><td>72</td><td>57</td><td>●</td><td></td><td></td><td>84</td><td>EMBIG</td><td>CEEMEA</td></tr><tr><td>EMBIG LatAm</td><td>67</td><td>+1</td><td>-15</td><td>189</td><td>257</td><td>70</td><td>61</td><td>●</td><td>◆</td><td>○</td><td>82</td><td>EMBIG</td><td>Latin America</td></tr><tr><td>EMBIG IG</td><td>62</td><td>-2</td><td>-12</td><td>133</td><td>196</td><td>64</td><td>52</td><td>●</td><td></td><td>◆</td><td>75</td><td>EMBIG</td><td>Global</td></tr><tr><td>EMBIG HY</td><td>88</td><td>+1</td><td>-0</td><td>264</td><td>352</td><td>86</td><td>76</td><td>●</td><td></td><td></td><td>94</td><td>EMBIG</td><td>Global</td></tr><tr><td>CEMBI</td><td>56</td><td>-1</td><td>-18</td><td>176</td><td>232</td><td>55</td><td>39</td><td>●</td><td></td><td>◆</td><td>76</td><td>CEMBI</td><td>Global</td></tr><tr><td>CEMBI Asia</td><td>61</td><td>+3</td><td>+13</td><td>57</td><td>118</td><td>53</td><td>40</td><td>●</td><td></td><td></td><td>65</td><td>CEMBI</td><td>Asia</td></tr><tr><td>CEMBI CEEMEA</td><td>60</td><td>-2</td><td>-32</td><td>152</td><td>212</td><td>67</td><td>55</td><td>●</td><td>◆</td><td>○</td><td>95</td><td>CEMBI</td><td>CEEMEA</td></tr><tr><td>CEMBI LatAm</td><td>52</td><td>-1</td><td>-14</td><td>227</td><td>279</td><td>50</td><td>24</td><td>●</td><td></td><td></td><td>68</td><td>CEMBI</td><td>Latin America</td></tr><tr><td>CEMBI IG</td><td>58</td><td>-0</td><td>-19</td><td>127</td><td>185</td><td>57</td><td>38</td><td>●</td><td></td><td>◆</td><td>79</td><td>CEMBI</td><td>Global</td></tr><tr><td>CEMBI HY</td><td>48</td><td>-0</td><td>-14</td><td>334</td><td>382</td><td>47</td><td>20</td><td>●</td><td></td><td></td><td>68</td><td>CEMBI</td><td>Global</td></tr><tr><td>US High Grade</td><td>16</td><td>-2</td><td>-1</td><td>83</td><td>93</td><td>16</td><td>10</td><td>●</td><td></td><td>◆</td><td>22</td><td>JULI</td><td>US</td></tr><tr><td>US Treasuries</td><td>54</td><td>-6</td><td>+4</td><td>445</td><td>499</td><td>60</td><td>45</td><td>●</td><td></td><td>◆</td><td>70</td><td>GBI-US</td><td>US</td></tr></table>

Figure 4: 10s30s curves versus the 10y level relationship   
![](images/fe37e6b02a3198f9ae9b075fc825ad305e83553e69c22c2ce15f3fc172fca8f6.jpg)

<details>
<summary>scatter</summary>

| Category         | 10y spread | 10s30s curve |
| ---------------- | ---------- | ------------ |
| EM AGgregates    | 270        | 82           |
| EMBIG HY         | 265        | 88           |
| CEMBI HY         | 335        | 48           |
| US Treasuries     | 445        | 55           |
| CEMBI LatAm      | 225        | 52           |
| CEMBI          | 175        | 56           |
| CEMBI Quasi      | 125        | 58           |
| EMBIG Asia       | 100        | 37           |
| EM Big            | 130        | 62           |
| EMBIG AGG         | 180        | 68           |
| EMBIG CEEMEA     | 185        | 77           |
| EMBIG LatAm      | 190        | 67           |
| EMBIG Avg         | 195        | 69           |
| EMBIG CyEMEA     | 185        | 76           |
| EMBIG IG          | 130        | 61           |
| US High Grade    | 85         | 17           |
</details>

Figure 5: 1m change in aggregate 10s30s versus 1m change in aggregate 10y spreads   
![](images/b6c2ac917f4103fd5f28fd5c57cbd68b4d7286b889850bc98fa25b84d32e0cef.jpg)

<details>
<summary>scatter</summary>

| Entity           | 1m change in 10y spread | 1m change in 10s30s curve |
| ---------------- | ------------------------ | -------------------------- |
| CEMBI Asia       | -18                      | +2                         |
| EM HY            | -14                      | -0.5                       |
| EMBIG HY         | -16                      | -0.8                       |
| EM Big Avgregates| -7                       | -0.8                       |
| CEMBI IG         | -9                       | -0.5                       |
| EMBIG Latvia      | -5                       | 0.5                        |
| CEMBI CyEMEA     | -15                      | -1                         |
| EMBIG Sov        | -11                      | -0.8                       |
| CEMBI CEEMEA     | -9                       | -1.5                       |
| EMBIG Quasi      | -7                       | -1.8                       |
| EM AGgregate     | -6                       | -0.5                       |
| CEMBI            | -4                       | -0.5                       |
| EMBIG IG         | -6                       | -1.5                       |
| CEMBI Hy         | 2                        | -0.5                       |
| CEMBI LatAm      | 8                        | -1                         |
| US Treasuries    | 7                        | -6                         |
| Bear Steepening   | 2                        | 3                          |
| Bear Flattening   | 8                        | -1                         |
</details>

Figure 6: 1m change in aggregate 10s30s versus 1m change in 10y spreads by issuer

![](images/5d92dc5017aa865ebd1da3891f258fce758b06599cf5187f19d5afd8ba796fbf.jpg)

<details>
<summary>scatter</summary>

| Index       | 1m change in 10y spread | 1m change in 10s30s |
|-------------|--------------------------|----------------------|
| EMBIG SOV   | -35                      | -10                  |
| EMBIG SOV   | -25                      | 10                   |
| EMBIG SOV   | -20                      | 7                    |
| EMBIG SOV   | -15                      | 7                    |
| EMBIG SOV   | -10                      | 4                    |
| EMBIG SOV   | -8                       | 0                    |
| EMBIG SOV   | -6                       | -2                   |
| EMBIG SOV   | -4                       | -1                   |
| EMBIG SOV   | -2                       | -4                   |
| EMBIG SOV   | 0                        | -5                   |
| EMBIG SOV   | 2                        | -6                   |
| EMBIG SOV   | 4                        | -7                   |
| EMBIG SOV   | 6                        | -8                   |
| EMBIG QUASI  | -25                      | 7                    |
| EMBIG QUASI  | -20                      | 3                    |
| EMBIG QUASI  | -15                      | 1                    |
| EMBIG QUASI  | -10                      | 1                    |
| EMBIG QUASI  | -8                       | -3                   |
| EMBIG QUASI  | -6                       | -2                   |
| EMBIG QUASI  | -4                       | -1                   |
| EMBIG QUASI  | -2                       | -1                   |
| EMBIG QUASI  | 0                        | -1                   |
| EMBIG QUASI  | 2                        | -1                   |
| CEMBI       | -25                      | 7                    |
| CEMBI       | -20                      | -6                   |
| CEMBI       | -15                      | 6                    |
| CEMBI       | -10                      | -3                   |
| CEMBI       | -8                       | -2                   |
| CEMBI       | -6                       | -1                   |
| CEMBI       | -4                       | 1                    |
| CEMBI       | -2                       | -2                   |
| CEMBI       | 0                        | -2                   |
| CEMBI       | 2                        | -2                   |
| CEMBI       | 4                        | -2                   |
| CEMBI       | 6                        | -2                   |
| CEMBI       | 8                        | -2                   |
| CEMBI       | 10                       | -2                   |
| CEMBI       | 12                       | -2                   |
| CEMBI       | 14                       | -2                   |
| CEMBI       | 16                       | -2                   |
| CEMBI       | 18                       | -2                   |
| CEMBI       | 20                       | -2                   |
| CEMBI       | 22                       | -2                   |
| CEMBI       | 24                       | -2                   |
| CEMBI       | 26                       | -2                   |
| CEMBI       | 28                       | -2                   |
| CEMBI       | 30                       | -2                   |
| CEMBI       | 32                       | -2                   |
| CEMBI       | 34                       | -2                   |
| CEMBI       | 36                       | -2                   |
| CEMBI       | 38                       | -2                   |
| CEMBI       | 40                       | -2                   |
| CEMBI       | 42                       | -2                   |
| CEMBI       | 44                       | -2                   |
| CEMBI       | 46                       | -2                   |
| CEMBI       | 48                       | -2                   |
| CEMBI       | 50                       | -2                   |
| CEMBI       | 52                       | -2                   |
| CEMBI       | 54                       | -2                   |
| CEMBI       | 56                       | -2                   |
| CEMBI       | 58                       | -2                   |
| CEMBI       | 60                       | -2                   |
| CEMBI       | 62                       | -2                   |
| CEMBI       | 64                       | -2                   |
| CEMBI       | 66                       | -2                   |
| CEMBI       | 68                       | -2                   |
| CEMBI       | 70                       | -2                   |
| CEMBI       | 72                       | -2                   |
| CEMBI       | 74                       | -2                   |
| CEMBI       | 76                       | -2                   |
| CEMBI       | 78                       | -2                   |
| CEMBI       | 80                       | -2                   |
| CEMBI       | 82                       | -2                   |
| CEMBI       | 84                       | -2                   |
| CEMBI       | 86                       | -2                   |
| CEMBI       | 88                       | -2                   |
| CEMBI       | 90                       | -2                   |
| CEMBI       | 92                       | -2                   |
| CEMBI       | 94                       | -2                   |
| CEMBI       | 96                       | -2                   |
| CEMBI       | 98                       | -2                   |
| CEMBI       | 100                      | -2                   |
| BULL flattening     | -35                     | -15                  |
| BULL flattening     | -30                     | -15                  |
| BULL flattening     | -25                     | -15                  |
| BULL flattening     | -20                     | -15                  |
| BULL flattening     | -15                     | -15                  |
| BULL flattening     | -10                     | -15                  |
| BULL flattening     | -8                      | -15                  |
| BULL flattening     | -6                      | -15                  |
| BULL flattening     | -4                      | -15                  |
| BULL flattening     | -2                      | -15                  |
| BULL flattening     | 0                        | -15                  |
| BULL flattening     | 2                        | -15                  |
| BULL flattening     | 4                        | -15                  |
| BULL flattening     | 6                        | -15                  |
| BULL flattening     | 8                        | -15                  |
| BULL flattening     | 10                       | -15                  |
| BULL flattening     | 12                       | -15                  |
| BULL flattening     | 14                       | -15                  |
| BULL flattening     | 16                       | -15                  |
| BULL flattening     | 18                       | -15                  |
| BULL flattening     | 20                       | -15                  |
| BULL flattening     | 22                       | -15                  |
| BULL flattening     | 24                       | -15                  |
| BULL flattening     | 26                       | -15                  |
| BULL flattening     | 28                       | -15                  |
| BULL flattening     | 30                       | -15                  |
| BULL flattening     | 32                       | -15                  |
| BULL flattening     | 34                       | -15                  |
| BULL flattening     | 36                       | -15                  |
| BULL flattening     | 38                       | -15                  |
| BULL flattening     | 40                       | -15                  |
| BULL flattening     | 42                       | -15                  |
| BULL flattening     | 44                       | -15                  |
| BULL flattening     | 46                       | -15                  |
| BULL flattening     | 48                       | -15                  |
| BULL flattening     | 50                       | -15                  |
| BULL flattening     | 52                       | -15                  |
| BULL flattening     | 54                       | -15                  |
| BULL flattening     | 56                       | -15                  |
| BULL flattening     | 58                       | -15                  |
| BULL flattening     | 60                       | -15                  |
| BULL flattening     | 62                       | -15                  |
| BULL flattening     | 64                       | -15                  |
| BULL flattening     | 66                       | -15                  |
| BULL flattening     | 68                       | -15             

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 02 Jun 2026 02:49 PM HKT

Disseminated 02 Jun 2026 02:49 PM HKT
"""
