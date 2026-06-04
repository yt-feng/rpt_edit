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
# Electronic Component Sector

Component Data Deposition: Storage production trends in April 2026; nearline HDDs remained strong, with no change in trend line

In this note, we analyze April 2026 HDD and SSD shipment data from TechnoSystems Research (TSR). HDD production volume declined slightly MoM, but remained on a gradual uptrend. Data center-related nearline HDD capacity output rose slightly MoM, but continued to increase strongly YoY, up 31%. Enterprise SSD capacity output continued to increase both YoY and MoM, with the capacity-based growth rate of enterprise SSDs continuing to grow rapidly, at 117% YoY. In nearline HDDs, demand remained solid for models with capacity of 26TB or more in April 2026. In enterprise SSDs, the maximum capacity was 61.44TB for a long time, but TSR stated that 122.88TB and 245.76TB have been introduced and are now in full swing, and the trend toward higher capacity continues.

TDK is our top pick among HDD electronic components makers. Its market share among captive manufacturers could continue to rise since captive manufacturers are suppressing HDD head production capacity increases, and shifting their existing production capacity to heat-assisted magnetic recording (HAMR).

# HDD production volume

- In April 2026, HDD production volume was 11.2 million units (+8% YoY, -2% MoM), of which, nearline HDDs accounted for 6.8 million units (+14%, -1%). HDD capacity output was 168.5EB (+30% YoY, flat MoM), of which, nearline HDDs accounted for 154.8EB (+31%, +1%). HDD production volume declined slightly MoM, but the trend line still shows a gentle rise. Among these, production of high-capacity nearline HDDs such as 26TB, 28TB, and 32TB have gradually increased.   
- By form factor, only nearline HDD production maintained a growth trend. TSR stated that drive manufacturers are actively moving to secure nearline components, and appear to be presenting bullish production plans to component makers. TSR also said that demand for nearline drives is still at a high level on the back of moves to secure storage upfront, and production volume looks set to remain firm going forward. In addition, in nearline HDDs, the average capacity per drive in April was 22.8TB (+15% YoY, +2% MoM), thus continuing to trend higher.

# SSD production volume

- In April 2026, SSD production volume was 29.2 million units (+3% YoY, -1% MoM), of which enterprise/data center SSDs accounted for 5.7 million units (+42%, -4%), and SSD capacity output was 56.2EB (+64%, +1%), of which enterprise/data center SSDs accounted for 37.7EB (+117%, +2%).   
- In enterprise/data center SSDs, April average capacity per drive reached 6.6TB (+53% YoY, +6% MoM), thus continuing to trend higher. Total SSD shipment volume has plateaued, but total shipment capacity is growing rapidly, mainly in enterprise/data center SSDs.

Japan Equity Research

Technology - Electronic Components

Akinori Kanemoto AC

(81-3) 6736 8628

akinori.kanemoto@JPM.com

Ikki Shibata

(81-3) 6736 8641

ikki.shibata@JPM.com

JPM Securities Japan Co., Ltd.

# Trends in data center and server storage:

\- In April 2026, the total production volume of enterprise HDDs, nearline HDDs, and enterprise/datacenter SSDs was 12.7 million units (+24% YoY, -3% MoM), and total capacity output was 192.9EB (+42%, +1%). Since May 2025, the share of SSDs in total capacity has been on an upward trend, rising to 19.5% of the total as of in April 2026 (19.3% in March 2026, 12.8% in April 2025).

Figure 1: Share price performance 

<table><tr><td>Ticker</td><td>Company</td><td>Price(JPY)</td></tr><tr><td>6981</td><td>Murata Mfg.</td><td>10,490</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>16,060</td></tr><tr><td>6762</td><td>TDK</td><td>4,104</td></tr><tr><td>6971</td><td>Kyocera</td><td>3,538</td></tr><tr><td>6963</td><td>Rohm</td><td>5,182</td></tr><tr><td>6996</td><td>Nichicon</td><td>3,970</td></tr><tr><td>6997</td><td>Nippon Chemi-con</td><td>5,620</td></tr><tr><td>6594</td><td>Nidec</td><td>2,899</td></tr><tr><td>6479</td><td>MinebeaMitsumi</td><td>4,721</td></tr><tr><td>4062</td><td>Ibiden</td><td>21,795</td></tr><tr><td>6806</td><td>Hirose Elec</td><td>28,390</td></tr><tr><td>6807</td><td>JAE</td><td>2,506</td></tr><tr><td>6770</td><td>AlpsAlpine</td><td>2,214</td></tr><tr><td>5334</td><td>Niterra</td><td>10,125</td></tr><tr><td>6727</td><td>Wacom</td><td>871</td></tr><tr><td>7915</td><td>NISSHA</td><td>1,606</td></tr><tr><td colspan="3">Simple Average</td></tr><tr><td></td><td>SOX</td><td>12,829</td></tr><tr><td></td><td>NK225</td><td>66,934</td></tr><tr><td></td><td>TOPIX</td><td>3,941</td></tr></table>

<table><tr><td colspan="6">Performance</td></tr><tr><td>-1W</td><td>-1M</td><td>-3M</td><td>-6M</td><td>-9M</td><td>-12M</td></tr><tr><td>47.1%</td><td>116.7%</td><td>155.4%</td><td>226.5%</td><td>331.3%</td><td>385.3%</td></tr><tr><td>76.4%</td><td>143.9%</td><td>234.9%</td><td>392.8%</td><td>429.0%</td><td>555.4%</td></tr><tr><td>21.8%</td><td>53.3%</td><td>69.3%</td><td>60.3%</td><td>112.0%</td><td>156.2%</td></tr><tr><td>18.1%</td><td>31.6%</td><td>28.0%</td><td>65.6%</td><td>79.0%</td><td>100.1%</td></tr><tr><td>12.8%</td><td>51.0%</td><td>80.2%</td><td>147.4%</td><td>137.5%</td><td>225.1%</td></tr><tr><td>18.3%</td><td>70.9%</td><td>84.1%</td><td>140.8%</td><td>187.7%</td><td>235.6%</td></tr><tr><td>67.0%</td><td>128.3%</td><td>197.7%</td><td>282.1%</td><td>299.1%</td><td>423.8%</td></tr><tr><td>6.8%</td><td>22.2%</td><td>17.7%</td><td>47.2%</td><td>-9.7%</td><td>1.8%</td></tr><tr><td>18.3%</td><td>54.3%</td><td>40.3%</td><td>48.9%</td><td>85.3%</td><td>129.3%</td></tr><tr><td>13.2%</td><td>73.5%</td><td>128.5%</td><td>266.9%</td><td>501.9%</td><td>632.7%</td></tr><tr><td>19.5%</td><td>30.5%</td><td>21.7%</td><td>61.1%</td><td>47.8%</td><td>65.7%</td></tr><tr><td>-2.5%</td><td>2.0%</td><td>-7.3%</td><td>1.4%</td><td>-1.1%</td><td>-0.4%</td></tr><tr><td>2.7%</td><td>-4.9%</td><td>-5.6%</td><td>9.2%</td><td>22.2%</td><td>58.0%</td></tr><tr><td>4.9%</td><td>18.5%</td><td>28.1%</td><td>50.0%</td><td>90.8%</td><td>115.0%</td></tr><tr><td>1.3%</td><td>20.5%</td><td>-0.7%</td><td>3.7%</td><td>19.2%</td><td>36.9%</td></tr><tr><td>-1.9%</td><td>24.4%</td><td>17.9%</td><td>34.2%</td><td>17.8%</td><td>21.9%</td></tr><tr><td>20.2%</td><td>52.3%</td><td>68.1%</td><td>114.9%</td><td>146.9%</td><td>196.4%</td></tr><tr><td>5.1%</td><td>24.9%</td><td>58.4%</td><td>82.6%</td><td>126.3%</td><td>164.0%</td></tr><tr><td>5.7%</td><td>11.7%</td><td>13.7%</td><td>33.2%</td><td>56.7%</td><td>74.2%</td></tr><tr><td>1.2%</td><td>4.5%</td><td>0.1%</td><td>16.6%</td><td>28.1%</td><td>40.1%</td></tr></table>

<table><tr><td colspan="6">Performance Ranking</td></tr><tr><td>-1W</td><td>-1M</td><td>-3M</td><td>-6M</td><td>-9M</td><td>-12M</td></tr><tr><td>3</td><td>3</td><td>3</td><td>4</td><td>3</td><td>4</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td></tr><tr><td>4</td><td>7</td><td>7</td><td>9</td><td>7</td><td>7</td></tr><tr><td>8</td><td>9</td><td>10</td><td>7</td><td>10</td><td>10</td></tr><tr><td>10</td><td>8</td><td>6</td><td>5</td><td>6</td><td>6</td></tr><tr><td>6</td><td>5</td><td>5</td><td>6</td><td>5</td><td>5</td></tr><tr><td>2</td><td>2</td><td>2</td><td>2</td><td>4</td><td>3</td></tr><tr><td>11</td><td>12</td><td>13</td><td>12</td><td>16</td><td>15</td></tr><tr><td>7</td><td>6</td><td>8</td><td>11</td><td>9</td><td>8</td></tr><tr><td>9</td><td>4</td><td>4</td><td>3</td><td>1</td><td>1</td></tr><tr><td>5</td><td>10</td><td>11</td><td>8</td><td>11</td><td>11</td></tr><tr><td>16</td><td>15</td><td>16</td><td>16</td><td>15</td><td>16</td></tr><tr><td>13</td><td>16</td><td>15</td><td>14</td><td>12</td><td>12</td></tr><tr><td>12</td><td>14</td><td>9</td><td>10</td><td>8</td><td>9</td></tr><tr><td>14</td><td>13</td><td>14</td><td>15</td><td>13</td><td>13</td></tr><tr><td>15</td><td>11</td><td>12</td><td>13</td><td>14</td><td>14</td></tr></table>

Source: Bloomberg Finance L.P., JPM.   
Note: Share prices as of June 1, 2026. The darker the red, the higher the stock price performance ranking (the darker the blue, the lower the ranking).

Figure 2: Valuations of electronic component and HDD-related stocks 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company</td><td rowspan="2">Share Price(JPY)</td><td rowspan="2">Price Target(JPY)</td><td rowspan="2">Return</td><td rowspan="2">Rating</td><td rowspan="2">Market Capitalization(JPY mn)</td><td colspan="3">P/E</td><td colspan="3">EPS</td><td colspan="3">EV/EBITDA</td><td colspan="3">P/B</td></tr><tr><td>FY25E(x)</td><td>FY26E(x)</td><td>FY27E(x)</td><td>FY25E(x)</td><td>FY26E(x)</td><td>FY27E(x)</td><td>FY25E(x)</td><td>FY26E(x)</td><td>FY27E(x)</td><td>FY25E(x)</td><td>FY26E(x)</td><td>FY27E(x)</td></tr><tr><td>6981</td><td>Murata Mfg.</td><td>10,490</td><td>7,000</td><td>-33.3%</td><td>OW</td><td>20,591,889</td><td>89.31</td><td>64.47</td><td>43.97</td><td>117</td><td>163</td><td>239</td><td>20.42</td><td>16.20</td><td>11.77</td><td>7.38</td><td>6.89</td><td>6.19</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>16,060</td><td>9,500</td><td>-40.8%</td><td>OW</td><td>2,091,309</td><td>136.78</td><td>91.46</td><td>44.57</td><td>117</td><td>176</td><td>360</td><td>12.92</td><td>10.54</td><td>7.07</td><td>6.18</td><td>5.95</td><td>5.35</td></tr><tr><td>6762</td><td>TDK</td><td>4,104</td><td>3,200</td><td>-22.0%</td><td>OW</td><td>7,977,601</td><td>39.63</td><td>31.56</td><td>26.50</td><td>104</td><td>130</td><td>155</td><td>7.85</td><td>6.63</td><td>5.71</td><td>4.03</td><td>3.72</td><td>3.40</td></tr><tr><td>6971</td><td>Kyocera</td><td>3,538</td><td>2,400</td><td>-32.2%</td><td>N</td><td>5,020,779</td><td>39.20</td><td>38.81</td><td>36.04</td><td>90</td><td>91</td><td>98</td><td>16.04</td><td>14.20</td><td>13.08</td><td>1.52</td><td>1.62</td><td>1.73</td></tr><tr><td>6963</td><td>Rohm</td><td>5,182</td><td>3,900</td><td>-24.7%</td><td>OW</td><td>2,092,284</td><td>161.49</td><td>59.52</td><td>38.63</td><td>32</td><td>87</td><td>134</td><td>20.26</td><td>12.32</td><td>9.91</td><td>2.26</td><td>2.24</td><td>2.17</td></tr><tr><td>6996</td><td>Nichicon</td><td>3,970</td><td>2,400</td><td>-39.5%</td><td>OW</td><td>277,900</td><td>46.39</td><td>35.56</td><td>26.83</td><td>86</td><td>112</td><td>148</td><td>6.21</td><td>4.90</td><td>3.99</td><td>2.34</td><td>2.24</td><td>2.11</td></tr><tr><td>6997</td><td>Nippon Chemi-con</td><td>5,620</td><td>1,260</td><td>-77.6%</td><td>UW</td><td>138,805</td><td>69.39</td><td>34.16</td><td>23.28</td><td>81</td><td>165</td><td>241</td><td>8.45</td><td>6.56</td><td>5.24</td><td>3.25</td><td>2.94</td><td>2.59</td></tr><tr><td>6594</td><td>Nidec</td><td>2,899</td><td>1,800</td><td>-37.9%</td><td>UW</td><td>3,457,257</td><td>26.66</td><td>16.56</td><td>14.50</td><td>109</td><td>175</td><td>200</td><td>10.02</td><td>6.45</td><td>5.45</td><td>1.80</td><td>1.63</td><td>1.46</td></tr><tr><td>6479</td><td>MinebeaMitsumi</td><td>4,721</td><td>3,700</td><td>-21.6%</td><td>OW</td><td>2,016,248</td><td>27.54</td><td>21.64</td><td>18.88</td><td>171</td><td>218</td><td>250</td><td>8.20</td><td>7.09</td><td>6.19</td><td>2.40</td><td>2.22</td><td>2.05</td></tr><tr><td>4062</td><td>Ibiden</td><td>21,795</td><td>18,400</td><td>-15.6%</td><td>OW</td><td>6,140,112</td><td>84.74</td><td>114.71</td><td>95.14</td><td>257</td><td>190</td><td>229</td><td>36.02</td><td>27.72</td><td>20.31</td><td>10.53</td><td>9.68</td><td>8.82</td></tr><tr><td>6806</td><td>Hirose Elec</td><td>28,390</td><td>32,100</td><td>13.1%</td><td>OW</td><td>1,013,352</td><td>30.78</td><td>30.31</td><td>26.23</td><td>922</td><td>937</td><td>1,082</td><td>11.74</td><td>10.72</td><td>9.79</td><td>2.55</td><td>2.50</td><td>2.44</td></tr><tr><td>6807</td><td>JAE</td><td>2,506</td><td>2,395</td><td>-4.4%</td><td>N</td><td>176,178</td><td>23.00</td><td>19.32</td><td>14.39</td><td>109</td><td>130</td><td>174</td><td>4.91</td><td>4.29</td><td>3.62</td><td>1.23</td><td>1.19</td><td>1.13</td></tr><tr><td>6770</td><td>AlpsAlpine</td><td>2,214</td><td>2,440</td><td>10.2%</td><td>N</td><td>460,742</td><td>16.71</td><td>14.24</td><td>12.34</td><td>133</td><td>156</td><td>179</td><td>5.39</td><td>4.62</td><td>4.15</td><td>0.95</td><td>0.91</td><td>0.86</td></tr><tr><td>5334</td><td>Niterra</td><td>10,125</td><td>9,100</td><td>-10.1%</td><td>OW</td><td>2,017,383</td><td>19.31</td><td>17.85</td><td>16.13</td><td>524</td><td>567</td><td>628</td><td>8.63</td><td>7.49</td><td>6.62</td><td>2.57</td><td>2.37</td><td>2.17</td></tr><tr><td>6727</td><td>Wacom</td><td>871</td><td>1,300</td><td>49.3%</td><td>OW</td><td>117,585</td><td>11.77</td><td>12.04</td><td>11.47</td><td>74</td><td>72</td><td>76</td><td>5.23</td><td>4.36</td><td>3.36</td><td>2.64</td><td>2.06</td><td>1.67</td></tr><tr><td>7915</td><td>NISSHA</td><td>1,606</td><td>1,340</td><td>-16.6%</td><td>N</td><td>77,114</td><td>76.03</td><td>18.50</td><td>14.10</td><td>21</td><td>87</td><td>114</td><td>6.26</td><td>4.95</td><td>4.39</td><td>0.66</td><td>0.65</td><td>0.63</td></tr><tr><td colspan="2">Simple Average</td><td></td><td></td><td>-19.0%</td><td></td><td>3,354,159</td><td>56.17</td><td>38.79</td><td>28.94</td><td>184</td><td>216</td><td>269</td><td>11.78</td><td>9.32</td><td>7.54</td><td>3.27</td><td>3.05</td><td>2.80</td></tr></table>

<table><tr><td rowspan="2">Tiker</td><td rowspan="2">Company</td><td rowspan="2">Share Price(JPY)</td><td rowspan="2">Price Target(JPY)</td><td rowspan="2">Return</td><td rowspan="2">Rating</td><td rowspan="2">Market Capitalization(JPY mn)</td><td colspan="3">ROE</td><td colspan="3">DPS</td><td colspan="3">Dividend Yield</td><td colspan="3">Dividend Payout Ratio</td></tr><tr><td>FY25E</td><td>FY26E</td><td>FY27E</td><td>FY25E(JPY)</td><td>FY26E(JPY)</td><td>FY27E(JPY)</td><td>FY25E</td><td>FY26E</td><td>FY27E</td><td>FY25E</td><td>FY26E</td><td>FY27E</td></tr><tr><td>6981</td><td>Murata Mfg.</td><td>10,490</td><td>7,000</td><td>-33.3%</td><td>OW</td><td>20,591,889</td><td>8.3%</td><td>11.1%</td><td>14.8%</td><td>60.0</td><td>62.0</td><td>66.0</td><td>0.6%</td><td>0.6%</td><td>0.6%</td><td>51.1%</td><td>38.1%</td><td>27.7%</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>16,060</td><td>9,500</td><td>-40.8%</td><td>OW</td><td>2,091,309</td><td>5.0%</td><td>7.3%</td><td>13.8%</td><td>90.0</td><td>90.0</td><td>90.0</td><td>0.6%</td><td>0.6%</td><td>0.6%</td><td>76.7%</td><td>51.3%</td><td>25.0%</td></tr><tr><td>6762</td><td>TDK</td><td>4,104</td><td>3,200</td><td>-22.0%</td><td>OW</td><td>7,977,601</td><td>10.5%</td><td>12.3%</td><td>13.4%</td><td>34.0</td><td>42.0</td><td>50.0</td><td>0.8%</td><td>1.0%</td><td>1.2%</td><td>32.8%</td><td>32.3%</td><td>32.3%</td></tr><tr><td>6971</td><td>Kyocera</td><td>3,538</td><td>2,400</td><td>-32.2%</td><td>N</td><td>5,020,779</td><td>3.8%</td><td>4.0%</td><td>4.6%</td><td>50.0</td><td>50.0</td><td>50.0</td><td>1.4%</td><td>1.4%</td><td>1.4%</td><td>55.4%</td><td>54.8%</td><td>50.9%</td></tr><tr><td>6963</td><td>Rohm</td><td>5,182</td><td>3,900</td><td>-24.7%</td><td>OW</td><td>2,092,284</td><td>1.6%</td><td>4.4%</td><td>6.6%</td><td>50.0</td><td>50.0</td><td>50.0</td><td>1.0%</td><td>1.0%</td><td>1.0%</td><td>155.8%</td><td>57.4%</td><td>37.3%</td></tr><tr><td>6996</td><td>Nichicon</td><td>3,970</td><td>2,400</td><td>-39.5%</td><td>OW</td><td>277,900</td><td>5.1%</td><td>6.4%</td><td>8.1%</td><td>36.0</td><td>37.0</td><td>38.0</td><td>0.9%</td><td>0.9%</td><td>1.0%</td><td>42.1%</td><td>33.1%</td><td>25.7%</td></tr><tr><td>6997</td><td>Nippon Chemi-con</td><td>5,620</td><td>1,260</td><td>-77.6%</td><td>UW</td><td>138,805</td><td>4.0%</td><td>7.6%</td><td>10.1%</td><td>20.0</td><td>20.0</td><td>20.0</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>24.7%</td><td>12.2%</td><td>8.3%</td></tr><tr><td>6594</td><td>Nidec</td><td>2,899</td><td>1,800</td><td>-37.9%</td><td>UW</td><td>3,457,257</td><td>7.0%</td><td>10.3%</td><td>10.6%</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>6479</td><td>MinebeaMitsumi</td><td>4,721</td><td>3,700</td><td>-21.6%</td><td>OW</td><td>2,016,248</td><td>9.0%</td><td>10.7%</td><td>11.3%</td><td>55.0</td><td>60.0</td><td>70.0</td><td>1.2%</td><td>1.3%</td><td>1.5%</td><td>32.1%</td><td>27.5%</td><td>28.0%</td></tr><tr><td>4062</td><td>Ibiden</td><td>21,795</td><td>18,400</td><td>-15.6%</td><td>OW</td><td>6,140,112</td><td>14.2%</td><td>9.3%</td><td>10.3%</td><td>25.0</td><td>21.0</td><td>22.0</td><td>0.1%</td><td>0.1%</td><td>0.1%</td><td>9.7%</td><td>11.1%</td><td>9.6%</td></tr><tr><td>6806</td><td>Hirose Elec</td><td>28,390</td><td>32,100</td><td>13.1%</td><td>OW</td><td>1,013,352</td><td>8.6%</td><td>10.0%</td><td>11.3%</td><td>540.0</td><td>560.0</td><td>580.0</td><td>1.9%</td><td>2.0%</td><td>2.0%</td><td>58.5%</td><td>59.8%</td><td>53.6%</td></tr><tr><td>6807</td><td>JAE</td><td>2,506</td><td>2,395</td><td>-4.4%</td><td>N</td><td>176,178</td><td>5.4%</td><td>6.3%</td><td>8.1%</td><td>60.0</td><td>60.0</td><td>60.0</td><td>2.4%</td><td>2.4%</td><td>2.4%</td><td>55.1%</td><td>46.3%</td><td>34.4%</td></tr><tr><td>6770</td><td>AlpsAlpine</td><td>2,214</td><td>2,440</td><td>10.2%</td><td>N</td><td>460,742</td><td>6.3%</td><td>6.9%</td><td>7.6%</td><td>60.0</td><td>65.0</td><td>70.0</td><td>2.7%</td><td>2.9%</td><td>3.2%</td><td>45.3%</td><td>41.8%</td><td>39.0%</td></tr><tr><td>5334</td><td>Niterra</td><td>10,125</td><td>9,100</td><td>-10.1%</td><td>OW</td><td>2,017,383</td><td>14.2%</td><td>13.8%</td><td>14.0%</td><td>204.4</td><td>220.0</td><td>240.0</td><td>2.0%</td><td>2.2%</td><td>2.4%</td><td>39.0%</td><td>38.8%</td><td>38.2%</td></tr><tr><td>6727</td><td>Wacom</td><td>871</td><td>1,300</td><td>49.3%</td><td>OW</td><td>117,585</td><td>26.5%</td><td>19.2%</td><td>16.1%</td><td>26.0</td><td>22.0</td><td>22.0</td><td>3.0%</td><td>2.5%</td><td>2.5%</td><td>35.1%</td><td>30.4%</td><td>29.0%</td></tr><tr><td>7915</td><td>NISSHA</td><td>1,606</td><td>1,340</td><td>-16.6%</td><td>N</td><td>77,114</td><td>0.9%</td><td>3.5%</td><td>4.6%</td><td>50.0</td><td>50.0</td><td>50.0</td><td>3.1%</td><td>3.1%</td><td>3.1%</td><td>236.7%</td><td>57.6%</td><td>43.9%</td></tr><tr><td colspan="2">Simple Average</td><td></td><td></td><td>-19.0%</td><td></td><td>3,354,159</td><td>8.1%</td><td>8.9%</td><td>10.3%</td><td></td><td></td><td></td><td>1.4%</td><td>1.4%</td><td>1.5%</td><td>59.4%</td><td>37.0%</td><td>30.2%</td></tr></table>

<table><tr><td rowspan="2">Ticker Company</td><td rowspan="2">Share Price(LC)</td><td colspan="3">P/E Consensus(BBG)</td><td colspan="3">P/B Consensus(BBG)</td></tr><tr><td>FY25(x)</td><td>FY26E(x)</td><td>FY27E(x)</td><td>FY25(x)</

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 02 Jun 2026 04:37 PM JST

Disseminated 02 Jun 2026 04:37 PM JST
"""
