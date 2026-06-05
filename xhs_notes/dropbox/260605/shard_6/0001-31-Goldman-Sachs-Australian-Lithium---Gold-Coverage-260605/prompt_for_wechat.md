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
# Australian Lithium & Gold Coverage

Coverage Summary, Forecasts and Spot Pricing Scenarios

June 2026

Priced as of 5 June 2026

Hugo Nicolaci

Paul Young

Marcus Dosanjh

Kavya Balaji

GS Australia Pty Ltd

GS Australia Pty Ltd

GS Australia Pty Ltd

GS Australia Pty Ltd

+61 2 9321 8323

+61 2 9321 8302

+61 2 9321 8780

+61 3 9679 1126

hugo.nicolaci@gs.com

paul.young1@gs.com

marcus.dosanjh@gs.com

kavya.balaji@gs.com

# Coverage Summary

Buy: NEM, NST, BGL, RMS, WGX, PNR, & WA1

Sell: PLS, MIN, & GGP

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">GS Rating</td><td rowspan="2">Key Commodities</td><td colspan="2">Priced: 5-Jun-26</td><td colspan="2">12mth Price Target</td><td colspan="2">NAV Valuation</td><td colspan="3">NTM EV/ EBITDA Valuation</td><td rowspan="2">M&amp;A GSe A$/sh</td><td rowspan="2">NTM Div Yield</td><td rowspan="2">TSR</td><td rowspan="2">NTM FCF Yield</td></tr><tr><td>Market cap US$bn</td><td>Last Price A$/sh</td><td>A$/sh</td><td>Upside/Downside %</td><td>NAV A$/sh</td><td>P/NAV (x)</td><td>A$/sh</td><td>Current Multiple (GSe)</td><td>Applied Target Multiple</td></tr><tr><td>IGO</td><td>Neutral</td><td>Nickel / Lithium</td><td>4.8</td><td>8.89</td><td>7.70</td><td>(13%)</td><td>5.95</td><td>1.49</td><td>9.40</td><td>13.7x</td><td>14.1x</td><td>-</td><td>1%</td><td>(12%)</td><td>4%</td></tr><tr><td>PLS</td><td>Sell</td><td>Spodumene</td><td>13.6</td><td>5.93</td><td>4.20</td><td>(29%)</td><td>3.70</td><td>1.60</td><td>4.62</td><td>18.8x</td><td>14.0x</td><td>-</td><td>1%</td><td>(28%)</td><td>(0%)</td></tr><tr><td>LTR</td><td>Neutral</td><td>Spodumene</td><td>4.9</td><td>2.17</td><td>1.75</td><td>(19%)</td><td>1.44</td><td>1.51</td><td>2.07</td><td>16.8x</td><td>16.0x</td><td>-</td><td>0%</td><td>(19%)</td><td>3%</td></tr><tr><td>CXO</td><td>Neutral</td><td>Spodumene</td><td>0.6</td><td>0.27</td><td>0.22</td><td>(20%)</td><td>0.22</td><td>1.25</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0%</td><td>(20%)</td><td>(12%)</td></tr><tr><td>MIN</td><td>Sell</td><td>Fe / Li / Crushing</td><td>9.7</td><td>68.46</td><td>53.00</td><td>(23%)</td><td>45.20</td><td>1.51</td><td>60.41</td><td>9.2x</td><td>8.5x</td><td>-</td><td>1%</td><td>(21%)</td><td>6%</td></tr><tr><td>NST</td><td>Buy</td><td>Gold</td><td>20.7</td><td>20.27</td><td>25.20</td><td>24%</td><td>24.81</td><td>0.82</td><td>25.60</td><td>7.1x</td><td>9.0x</td><td>-</td><td>2%</td><td>26%</td><td>2%</td></tr><tr><td>EVN</td><td>Neutral</td><td>Gold / Copper</td><td>17.2</td><td>11.85</td><td>12.70</td><td>7%</td><td>12.97</td><td>0.91</td><td>12.48</td><td>6.6x</td><td>7.0x</td><td>-</td><td>4%</td><td>11%</td><td>6%</td></tr><tr><td>NEM</td><td>Buy</td><td>Gold</td><td>115.6</td><td>150.52</td><td>172.30</td><td>14%</td><td>164.53</td><td>0.91</td><td>180.14</td><td>5.9x</td><td>7.0x</td><td>-</td><td>1%</td><td>16%</td><td>9%</td></tr><tr><td>RRL</td><td>Not Rated</td><td>Gold</td><td>3.2</td><td>5.95</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2.1x</td><td>-</td><td>-</td><td>7%</td><td>-</td><td>19%</td></tr><tr><td>CMM</td><td>Neutral</td><td>Gold</td><td>4.3</td><td>13.10</td><td>16.90</td><td>29%</td><td>16.34</td><td>0.80</td><td>15.97</td><td>10.1x</td><td>12.5x</td><td>21.24</td><td>1%</td><td>30%</td><td>(0%)</td></tr><tr><td>BGL</td><td>Buy</td><td>Gold</td><td>1.6</td><td>1.43</td><td>1.90</td><td>33%</td><td>1.99</td><td>0.72</td><td>1.57</td><td>4.5x</td><td>5.0x</td><td>2.59</td><td>1%</td><td>34%</td><td>10%</td></tr><tr><td>VAU</td><td>Not Rated</td><td>Gold</td><td>3.1</td><td>4.11</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2.9x</td><td>-</td><td>-</td><td>5%</td><td>-</td><td>16%</td></tr><tr><td>RMS</td><td>Buy</td><td>Gold</td><td>4.3</td><td>3.09</td><td>5.40</td><td>75%</td><td>5.34</td><td>0.58</td><td>4.55</td><td>6.6x</td><td>10.0x</td><td>6.94</td><td>1%</td><td>76%</td><td>3%</td></tr><tr><td>GMD</td><td>Neutral</td><td>Gold</td><td>4.6</td><td>5.43</td><td>8.00</td><td>47%</td><td>8.03</td><td>0.68</td><td>7.14</td><td>5.3x</td><td>7.0x</td><td>10.44</td><td>2%</td><td>50%</td><td>3%</td></tr><tr><td>WGX</td><td>Buy</td><td>Gold</td><td>3.4</td><td>4.92</td><td>7.85</td><td>60%</td><td>7.91</td><td>0.62</td><td>6.94</td><td>3.1x</td><td>4.5x</td><td>10.29</td><td>3%</td><td>62%</td><td>11%</td></tr><tr><td>GGP</td><td>Sell</td><td>Gold / Copper</td><td>6.5</td><td>12.99</td><td>12.60</td><td>(3%)</td><td>13.25</td><td>0.98</td><td>11.97</td><td>6.9x</td><td>6.0x</td><td>-</td><td>0%</td><td>(3%)</td><td>1%</td></tr><tr><td>PNR</td><td>Buy</td><td>Gold</td><td>0.8</td><td>2.71</td><td>4.95</td><td>83%</td><td>4.44</td><td>0.61</td><td>5.17</td><td>1.9x</td><td>4.0x</td><td>5.77</td><td>1%</td><td>84%</td><td>19%</td></tr><tr><td>WA1</td><td>Buy</td><td>Niobium</td><td>0.7</td><td>13.27</td><td>27.30</td><td>106%</td><td>31.24</td><td>0.42</td><td>-</td><td>-</td><td>-</td><td>40.61</td><td>0%</td><td>106%</td><td>(5%)</td></tr></table>

P/NAV   
![](images/bd5c28315efe2f250698fb8ed140962ebec1cfd4b11f751bf73433f1ef0e1360.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| IGO | 1.49 |
| PLS | 1.60 |
| LTR | 1.51 |
| CXO | 1.25 |
| MIN | 1.51 |
| NST | 0.82 |
| EVN | 0.91 |
| NEM | 0.91 |
| CMM | 0.80 |
| BGL | 0.72 |
| RMS | 0.58 |
| GMD | 0.68 |
| WGX | 0.62 |
| GGP | 0.98 |
| PNR | 0.61 |
| WA1 | 0.42 |
</details>

EV/EBITDA

![](images/d8231d73fd054fe3c928ce1ff545474ad220f26aaf137e0645713ac7cb5f880d.jpg)

<details>
<summary>bar</summary>

| Category | Lithium Sector Ave: 11.0x | Gold Large Cap Ave: 6.5x | Gold Mid Cap Ave: 5.0x |
|---|---|---|---|
| Bar 1 | 13.7x | | |
| Bar 2 | 18.8x | | |
| Bar 3 | 16.8x | | |
| Bar 4 | 9.2x | | |
| Bar 5 | 7.1x | 6.6x | |
| Bar 6 | 5.9x | | 2.1x |
| Bar 7 | | 10.1x | |
| Bar 8 | | 4.5x | |
| Bar 9 | | 2.9x | |
| Bar 10 | 6.6x | | |
| Bar 11 | 5.3x | | |
| Bar 12 | 3.1x | | |
| Bar 13 | 6.9x | | |
| Bar 14 | | 1.9x | |
</details>

IGO PLS LTR MIN NST EVN NEM RRL CMM BGL VAU RMSGMDWGXGGP PNR

![](images/728799f78480fc7450124b83fc09f14f561d5750cf14f9632e57fad42af23711.jpg)

<details>
<summary>bar</summary>

| Category | Implied upside / downside to PT (%) | Buy (%) | Sell (%) |
| :--- | :--- | :--- | :--- |
| 1 | -13 | 24 | 7 |
| 2 | -29 | 14 | 29 |
| 3 | -19 | 33 | 47 |
| 4 | -20 | 75 | 60 |
| 5 | -23 | 83 | 106 |
</details>

IGO PLS LTR CXO MIN NST EVN NEM CMM BGL RMS GMD WGX GGP PNR WA1

Commodity & FX Forecasts 

<table><tr><td>Calendar year</td><td>Unit</td><td>Spot</td><td>2024</td><td>2025</td><td>Q1&#x27;26</td><td>Q2&#x27;26</td><td>Q3&#x27;26</td><td>Q4&#x27;26</td><td>2026</td><td>2027</td><td>2028</td><td>2029</td><td>LT (real)</td><td>LT (nom)</td><td>LT (real)</td><td>Q2&#x27;26</td></tr><tr><td>Non-Ferrous Metals</td><td></td><td></td><td>Act</td><td>Act</td><td>Act</td><td>Est</td><td>Est</td><td>Est</td><td>Est</td><td>Est</td><td>Est</td><td>Est</td><td>Est</td><td>Est</td><td>vs. Spot</td><td>vs. Spot</td></tr><tr><td>Aluminium</td><td>US$/lb.</td><td>1.71</td><td>1.10</td><td>1.19</td><td>1.45</td><td>1.50</td><td>1.45</td><td>1.41</td><td>1.45</td><td>1.36</td><td>1.36</td><td>1.39</td><td>1.22</td><td>1.42</td><td>-28%</td><td>-13%</td></tr><tr><td>Copper</td><td>US$/lb.</td><td>6.26</td><td>4.15</td><td>4.51</td><td>5.82</td><td>6.08</td><td>6.17</td><td>6.21</td><td>6.07</td><td>6.26</td><td>6.21</td><td>6.12</td><td>5.22</td><td>6.05</td><td>-17%</td><td>-3%</td></tr><tr><td>Cobalt</td><td>US$/lb.</td><td>25.3</td><td>11.9</td><td>15.8</td><td>25.3</td><td>21.0</td><td>21.2</td><td>21.3</td><td>22.2</td><td>19.3</td><td>19.2</td><td>19.2</td><td>16.50</td><td>19.13</td><td>-35%</td><td>-17%</td></tr><tr><td>Nickel</td><td>US$/lb.</td><td>8.46</td><td>7.63</td><td>6.88</td><td>7.86</td><td>8.16</td><td>8.16</td><td>8.16</td><td>8.09</td><td>7.71</td><td>8.23</td><td>8.76</td><td>8.01</td><td>9.28</td><td>-5%</td><td>-3%</td></tr><tr><td>Zinc</td><td>US$/lb.</td><td>1.63</td><td>1.26</td><td>1.30</td><td>1.47</td><td>1.47</td><td>1.45</td><td>1.41</td><td>1.45</td><td>1.45</td><td>1.55</td><td>1.64</td><td>1.50</td><td>1.74</td><td>-8%</td><td>-9%</td></tr><tr><td colspan="17">Precious Metals</td></tr><tr><td>Gold</td><td>US$/oz</td><td>4,480</td><td>2,387</td><td>3,440</td><td>4,873</td><td>4,590</td><td>4,565</td><td>4,626</td><td>4,664</td><td>4,820</td><td>4,888</td><td>4,638</td><td>3,800</td><td>4,405</td><td>-15%</td><td>2%</td></tr><tr><td>Silver</td><td>US$/oz</td><td>74</td><td>28.2</td><td>40.1</td><td>83.7</td><td>76.0</td><td>75.1</td><td>76.6</td><td>77.9</td><td>78.9</td><td>80.4</td><td>69.3</td><td>52.0</td><td>60.3</td><td>-30%</td><td>3%</td></tr><tr><td colspan="17">Bulks</td></tr><tr><td>Iron ore (61% Fe)</td><td>US$/t</td><td>101</td><td>110</td><td>102</td><td>104</td><td>100</td><td>97</td><td>95</td><td>99</td><td>95</td><td>96</td><td>97</td><td>85</td><td>99</td><td>-16%</td><td>-1%</td></tr><tr><td>Freight - Aus/China</td><td>US$/t</td><td>14.6</td><td>10.1</td><td>9.0</td><td>9.6</td><td>13.0</td><td>15.0</td><td>13.0</td><td>12.7</td><td>12.0</td><td>11.9</td><td>11.7</td><td>10.0</td><td>11.6</td><td>-31%</td><td>-11%</td></tr><tr><td>Aus Hard Coking Coal (Qld)</td><td>US$/t</td><td>242</td><td>241</td><td>188</td><td>235</td><td>220</td><td>210</td><td>200</td><td>216</td><td>205</td><td>216</td><td>227</td><td>205</td><td>238</td><td>-15%</td><td>-9%</td></tr><tr><td>PCI</td><td>US$/t</td><td>174</td><td>165</td><td>141</td><td>161</td><td>150</td><td>150</td><td>150</td><td>153</td><td>160</td><td>165</td><td>169</td><td>150</td><td>174</td><td>-14%</td><td>-14%</td></tr><tr><td>Semi-soft (SSCC)</td><td>US$/t</td><td>145</td><td>144</td><td>116</td><td>146</td><td>140</td><td>140</td><td>135</td><td>140</td><td>130</td><td>135</td><td>140</td><td>125</td><td>145</td><td>-14%</td><td>-3%</td></tr><tr><td>Thermal (6000 kcal)</td><td>US$/t</td><td>148</td><td>136</td><td>108</td><td>122</td><td>130</td><td>125</td><td>120</td><td>124</td><td>115</td><td>115</td><td>116</td><td>100</td><td>116</td><td>-32%</td><td>-12%</td></tr><tr><td>Manganese ore (44%)</td><td>US$/mnu</td><td>5.10</td><td>5.39</td><td>4.58</td><td>5.18</td><td>5.20</td><td>5.20</td><td>5.20</td><td>5.20</td><td>5.20</td><td>5.48</td><td>5.75</td><td>5.20</td><td>6.03</td><td>2%</td><td>2%</td></tr><tr><td>Bauxite</td><td>US$/t</td><td>67</td><td>64</td><td>79</td><td>64</td><td>70</td><td>70</td><td>70</td><td>69</td><td>70</td><td>70</td><td>70</td><td>60</td><td>70</td><td>-10%</td><td>4%</td></tr><tr><td>Alumina</td><td>US$/t</td><td>305</td><td>502</td><td>386</td><td>307</td><td>310</td><td>310</td><td>340</td><td>317</td><td>355</td><td>370</td><td>380</td><td>350</td><td>406</td><td>15%</td><td>2%</td></tr><tr><td>Potash</td><td>US$/t</td><td>405</td><td>295</td><td>348</td><td>369</td><td>360</td><td>360</td><td>360</td><td>362</td><td>370</td><td>395</td><td>421</td><td>385</td><td>446</td><td>-5%</td><td>-11%</td></tr><tr><td>Uranium</td><td>US$/lb</td><td>86</td><td>87</td><td>73</td><td>87</td><td>75</td><td>75</td><td>75</td><td>78</td><td>78</td><td>81</td><td>84</td><td>75</td><td>87</td><td>-13%</td><td>-13%</td></tr><tr><td colspan="17">Battery Materials</td></tr><tr><td>Lithium carbonate - China</td><td>US$/t</td><td>21,978</td><td>11,167</td><td>9,319</td><td>19,732</td><td>18,650</td><td>15,500</td><td>13,000</td><td>16,720</td><td>13,500</td><td>13,882</td><td>16,222</td><td>15,000</td><td>17,389</td><td>-32%</td><td>-15%</td></tr><tr><td>Lithium hydroxide - China</td><td>US$/t</td><td>20,051</td><td>10,083</td><td>8,769</td><td>18,804</td><td>17,850</td><td>14,700</td><td>12,225</td><td>15,895</td><td>12,825</td><td>13,351</td><td>15,525</td><td>14,250</td><td>16,520</td><td>-29%</td><td>-11%</td></tr><tr><td>Spodumene 6%</td><td>US$/t</td><td>2,550</td><td>974</td><td>842</td><td>2,015</td><td>1,950</td><td>1,575</td><td>1,260</td><td>1,700</td><td>1,308</td><td>1,275</td><td>1,373</td><td>1,225</td><td>1,420</td><td>-52%</td><td>-24%</td></tr><tr><td>NdPr (China)</td><td>US$/kg</td><td>103</td><td>54</td><td>68</td><td>108</td><td>120</td><td>120</td><td>120</td><td>117</td><td>120</td><td>123</td><td>125</td><td>110</td><td>128</td><td>7%</td><td>16%</td></tr><tr><td>Niobium Pentoxide (China)</td><td>US$/t</td><td>56,461</td><td>51,763</td><td>51,970</td><td>53,560</td><td>53,303</td><td>53,303</td><td>53,303</td><td>53,367</td><td>54,902</td><td>57,500</td><td>59,992</td><td>53,303</td><td>61,792</td><td>-6%</td><td>-6%</td></tr><tr><td>Ferro-Niobium (China)</td><td>US$/t</td><td>48,933</td><td>37,526</td><td>43,188</td><td>46,880</td><td>46,350</td><td>46,350</td><td>46,350</td><td>46,483</td><td>47,741</td><td>50,000</td><td>52,167</td><td>46,350</td><td>53,732</td><td>-5%</td><td>-5%</td></tr><tr><td colspan="17">Currencies</td></tr><tr><td>AUD:USD</td><td></td><td>0.71</td><td>0.66</td><td>0.64</td><td>0.70</td><td>0.72</td><td>0.72</td><td>0.72</td><td>0.71</td><td>0.71</td><td>0.71</td><td>0.70</td><td>0.70</td><td>0.70</td><td>-2%</td><td>1%</td></tr><tr><td>CAD:USD</td><td></td><td>0.72</td><td>0.73</td><td>0.72</td><td>0.73</td><td>0.73</td><td>0.73</td><td>0.73</td><td>0.73</td><td>0.74</td><td>0.75</td><td>0.75</td><td>0.76</td><td>0.76</td><td>6%</td><td>1%</td></tr><tr><td>USD:ZAR</td><td></td><td>16.3</td><td>18.3</td><td>17.9</td><td>16.4</td><td>16.9</td><td>17.1</td><td>17.2</td><td>16.9</td><td>17.8</td><td>17.5</td><td>17.3</td><td>17.00</td><td>17.0</td><td>4%</td><td>4%</td></tr><tr><td>BRL:USD</td><td></td><td>0.20</td><td>0.19</td><td>0.18</td><td>0.19</td><td>0.19</td><td>0.19</td><td>0.18</td><td>0.19</td><td>0.17</td><td>0.18</td><td>0.18</td><td>0.19</td><td>0.19</td><td>-4%</td><td>-4%</td></tr><tr><td>USD:CLP</td><td></td><td>896</td><td>944</td><td>951</td><td>886</td><td>915</td><td>916</td><td>916</td><td>908</td><td>924</td><td>900</td><td>875</td><td>850</td><td>850</td><td>-5%</td><td>2%</td></tr><tr><td>USD:ARS</td><td></td><td>1,437</td><td>915</td><td>1,244</td><td>1,419</td><td>1,475</td><td>1,574</td><td>1,676</td><td>1,536</td><td>1,770</td><td>1,580</td><td>1,390</td><td>1,200</td><td>1,200</td><td>-16%</td><td>3%</td></tr></table>

1. Source: Company data, Bloomberg, Platts, SMM, Asian Metals, FactSet, GS Global Investment Research.

2. Spot rutile and zircon are CIF. ILU average achieved price is FOB. FMG spot scenario uses GSe Fe price realisations. CIA realised price includes high grades 66% fines and 69% DRI feed

3. Spot steel spreads not lagged. Prices above reflect latest commodity team updates but may not be captured in company models. Forecast lithium prices for China (chemicals excl. VAT).

# GSe Base Case vs Spot Prices and FX

FY27 FCF Yield   
![](images/348df348b03365995f11dc394017cf5015d71f8fd2ed576f1775218bde94dbcd.jpg)  
IGO PLS LTR CXO MIN NST EVN NEM RRL CMM BGL VAU RMS GMDWGX GGP PNR WA1   
GSe Spot

FY27 EV/EBITDA   
![](images/3042f9903dc6e1e7c92cc6b9b4748b5b72573e7b3039e3ae647547a768aad55a.jpg)

<details>
<summary>bar</summary>

EV/EBITDA
| Company | GSe (x) | Spot (x) |
| :--- | :--- | :--- |
| IGO | 31.4 | 9.1 |
| PLS | 18.8 | 6.7 |
| LTR | 16.8 | 6.7 |
| MIN | 9.2 | 5.9 |
| NST | 7.1 | 7.4 |
| EVN | 6.6 | 6.8 |
| NEM | 6.3 | 6.4 |
| RRL | 2.1 | 2.2 |
| CMM | 10.1 | 10.5 |
| BGL | 4.5 | 4.7 |
| VAU | 2.9 | 3.1 |
| RMS | 6.6 | 6.9 |
| GMD | 5.3 | 5.5 |
| WGX | 3.1 | 3.2 |
| GGP | 6.9 | 7.2 |
| PNR | 1.9 | 2.0 |
</details>

FY27 Dividend Yield   
![](images/813d13753cd3e1a6b84942f0d68d2b6caa824e605028397f73980fc039f9d99f.jpg)

<details>
<summary>bar</summary>

Dividend yield
| Company | GSe (%) | Spot (%) |
| :--- | :--- | :--- |
| IGO | 1 | 3 |
| PLS | 1 | 3 |
| LTR | 0 | 0 |
| CXO | 0 | 0 |
| MIN | 1 | 4 |
| NST | 2 | 2 |
| EVN | 4 | 4 |
| NEM | 1 | 1 |
| RRL | 7 | 6 |
| CMM | 1 | 1 |
| BGL | 0.6 | 0.5 |
| VAU | 5 | 5 |
| RMS | 1 | 1 |
| GMD | 2 | 2 |
| WGX | 3 | 3 |
| GGP | 0 | 0 |
| PNR | 1 | 1 |
| WA1 | 0 | 0 |
</details>

% Difference in FY27 Underlying EBITDA   
![](images/7dfa645076c12385ee0ce48a929a0b90e38d61e6a37ea3860d4456ab7fdf4d79.jpg)

<details>
<summary>bar</summary>

% diff in Underlying EBITDA
| Company | Spot vs. GSe (%) | Cons vs. GSe (%) |
| :--- | :--- | :--- |
| IGO | 260 | 172 |
| PLS | 182 | 66 |
| LTR | 154 | 91 |
| CXO | 303 | 258 |
| MIN | 58 | 14 |
| NST | (5) | 31 |
| EVN | (2) | 10 |
| NEM | (3) | 12 |
| RRL | (4) | 1 |
| CMM | (4) | 28 |
| BGL | (3) | 32 |
| VAU | (5) | 21 |
| RMS | (4) | 30 |
| GMD | (4) | 16 |
| WGX | (5) | 16 |
| GGP | (4) | 2 |
| PNR | (4) | 3 |
</details>

GSe Base Case vs Spot Prices and FX 

<table><tr><td rowspan="2"></td><td rowspan="2">YE</td><td rowspan="2">Crncy</td><td rowspan="2"></td><td colspan="3">Under. EBITDA ($bn)</td><td colspan="3">Under. NPAT ($bn)</td><td colspan="3">Free Cash Flow ($bn)</td><td colspan="3">Net Debt/(Cash) ($bn)</td><td colspan="3">EPS (cps)</td><td colspan="3">DPS (cps)</td><td colspan="3">EV/EBITDA</td><td colspan="3">P/E</td></tr><tr><td>2026</td><td>2027</td><td>2028</td><td>2026</td><td>2027</td><td>2028</td><td>2026</td><td>2027</td><td>2028</td><td>2026</td><td>2027</td><td>2028</td><td>2026</td><td>2027</td><td>2028</td><td>2026</td><td>2027</td><td>2028</td><td>2026</td><td>2027</td><td>2028</td><td>2026</td><td>2026</td><td>2028</td></tr><tr><td colspan="28">Lithium</td></tr><tr><td>IGO</td><td>June</td><td>AUD</td><td>GSe</td><td>0.3</td><td>0.2</td><td>0.3</td><td>0.2</td><td>0.2</td><td>0.3</td><td>0.2</td><td>0.3</td><td>0.2</td><td>(0.4)</td><td>(0.6)</td><td>(0.8)</td><td>20.4</td><td>28.2</td><td>43.3</td><td>4.0</td><td>11.0</td><td>11.9</td><td>20.3</td><td>-</td><td>20.6</td><td>43.5</td><td>31.5</td><td>20.5</td></tr><tr><td></td><td></td><td></td><td>Spot</td><td>0.4</td><td>0.7</td><td>0.8</td><td>0.2</td><td>0.7</td><td>0.9</td><td>0.2</td><td>0.8</td><td>0.8</td><td>(0.4)</td><td>(1.1)</td><td>(1.5)</td><td>25.9</td><td>94.9</td><td>115.8</td><td>4.0</td><td>29.0</td><td>54.3</td><td>17.9</td><td>8.1</td><td>6.3</td><td>34.3</td><td>9.4</td><td>7.7</td></tr><tr><td></td><td></td><td></td><td>Diff</td><td>13%</td><td>260%</td><td>185%</td><td>27%</td><td>237%</td><td>167%</td><td>(0%)</td><td>138%</td><td>250%</td><td>0%</td><td>(64%)</td><td>(89%)</td><td>27%</td><td>237%</td><td>167%</td><td>0%</td><td>164%</td><td>357%</td><td>(12%)</td><td>-</td><td>(69%)</td><td>(21%)</td><td>(70%)</td><td>(63%)</td></tr><tr><td>PLS</td><td>June</td><td>AUD</td><td>GSe</td><td>1.0</td><td>1.0</td><td>1.1</td><td>0.5</td><td>0.4</td><td>0.5</td><td>0.5</td><td>(0.0)</td><td>(0.5)</td><td>(1.1)</td><td>(0.7)</td><td>0.1</td><td>16.5</td><td>13.2</td><td>16.2</td><td>3.5</td><td>4.5</td><td>5.2</t

[中间内容因长度限制已省略]

ionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.fiadocumentation.org/fia/regulatory-disclosures\_1/fia-uniform-futures-and-options-on-futures-risk-disclosures-booklet-pdf-version-2018. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

# Disclosure Appendix

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
