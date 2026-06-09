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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## GLOBAL CREDIT STRATEGY

## Global Credit: What We're Watching

US Investment Grade: The pullback in equities also weighed on credit, with US IG spreads ending the week 1bp wider, resulting in excess returns of -0.1%. Spread curves bear-steepened while better rated bonds underperformed. Telecoms, technology, utilities delivered the weakest excess returns, while basic industry and services held up better. US IG funds saw \$3.6bn of net inflows last week, lifting YTD inflows to +\$69bn. Primary market activity was robust, with \$47bn of bonds pricing last week. YTD supply is tracking at \$1,095bn (+26% YoY).

US Leveraged Credit: HY spreads widened by 7bp, translating into excess returns of -0.1%. Loans delivered positive total returns at 0.05% last week, outperforming HY (-0.4%). The moves were accompanied by decompression across HY and Loans. Within HY, telecom and consumer goods underperformed, while energy and technology held in better. HY funds reported net inflows of \$880mn (-\$6.2bn YTD), while loan funds saw net inflows of \$760mn last week (+\$3.5bn YTD). Both HY and Loans recorded \$13bn of issuance last week. YTD issuance now stands at \$160bn (+42% YoY) in HY and \$188bn (-3% YoY) in loans.

EU Investment Grade: European credit outperformed the US last week with spreads tightening by 3bp, resulting in excess returns of +0.1%. Curves bull-flattened, while BBBs saw slight outperformance across ratings. Media outperformed, while transportation and basic industry lagged. European IG fund inflows rose to \~\$700m (0.1% of AUM) following last week's more muted but positive print (\~\$155m). The inflows were heavily skewed towards ETFs, while mutual funds reported small net outflows. Issuance moderated to €12bn last week, lifting YTD volumes to €378bn (flat YoY).

EU High Yield: EU HY outperformed IG, with spreads tightening by 13bp last week resulting in excess returns of +0.4%. However, the moves were most pronounced in BBs, while performance was more mixed further down the ratings spectrum. Leisure and tech outperformed, while telecoms and real estate lagged. European HY fund net inflows rose to \~\$425mln / 0.4% of AUM, with both mutual funds and ETFs saw net inflows. YTD supply is tracking at €67bn (+11% YoY).

Key Trades: We reiterate our key trade recommendations across sectors in IG that we outlined in our Mid-Year Outlooks. In the US, we are overweight banks, utilities, while technology/hyperscalers remain our key underweights. In Europe, we like banks, energy, and defensives, while we recommend an underweight on cyclical sectors, autos in particular. In Asia, we like Japan Banks TLAC Senior debt and unhedged AUD LC Corp bonds.

Credit Derivatives: Synthetic spreads widened across the US and EU, with CDX IG and iTraxx Main ending the week 2bp and 1bp wider, respectively, while HY/Xover underperformed. While implied volatility ticked up from the YTD lows, credit lagged the rise in equities vol.

Asia Credit: Asia Credit spreads tightened by 2bp over the last week, while APAC Credit spreads remained flat. In Asia credit, Asia HY (-18bp) outperformed Asia IG (-2bp). Similarly, in APAC credit, HY spreads tightened by 3bp while IG spreads were flat.

## List of Recent Publications:

European Credit Mid-Year Outlook: Glass Half Full

US Credit Strategy Mid-Year Outlook: Financing the Future

US Credit Playbook: Focus Back on Supply

Asia Credit Mid-Year Outlook: A "Low-Fire, Low-Hire" Credit Market

## MS Global

## MS & Co. LLC

## Vishwas Patkar

Strategist

Vishwas.Patkar@morganstanley.com

+1 212 761 8041

## MS & Co. International plc+

## Aron Becker

Strategist

Aron.Becker@morganstanley.com

+44 0(207) 677 0754

## MS Asia Limited+

## Kelvin Pang

Strategist

Kelvin.Pang@morganstanley.com

+852 2848 8204

## MS & Co. LLC

## Christina Sigler

Strategist

Christina.Sigler@morganstanley.com

+1 212.761.4116

Note: The EPFR data and charts displayed here must not be extracted and republished (whether internally or externally). Such use will violate the terms of MS's contract with EPFR which only covers named users.

## Table of Contents

Global Credit Snapshot 3

Performance Across Asset Classes 4

Global Credit Percentile Ranges 5

US Credit Long-Term Spreads and Yields 6

Europe and Asia Credit Long-Term Spreads 7

Macro Sentiment Indicators 8

Credit Sentiment Indicators 9

Key Trades Across Sectors in IG 10

## US and EU Credit

Yields, Dollar Prices, and Index Quality 20

Curve Performance 21

Global Credit Demand 22

Global Credit Supply 24

Debt Outstanding 25

Maturity Walls 26

Defaults and Rating Changes 27

Fundamentals 28

Credit Derivatives/DTCC Positioning 29

IG Best + Worst Performers 31

IG 5-10Y Carry and Roll Down 37

Performance across Capital Structure 39

Sector Performance 41

Credit/Equity Screen 43

## Asia Credit

Asia Credit Demand 48

Asia Credit Supply 49

Asia Maturity Wall and Default Rate 50

Asia Debt Outstanding 51

Global Credit Snapshot

<table><tr><td>Global IG Credit</td><td>Current</td><td>1 Wk Δ</td><td>3 Mth Δ</td><td>12 Mth Δ</td><td>1Y %Tile</td><td>1Y %Tile Range</td><td>5Y Tights</td><td>5Y Wides</td><td>5Y %Tile</td><td>5Y %Tile Range</td></tr><tr><td>US IG</td><td>73</td><td>1</td><td>(7)</td><td>(14)</td><td>38%</td><td>■</td><td>71</td><td>165</td><td>10%</td><td>■</td></tr><tr><td>EUR IG</td><td>77</td><td>(3)</td><td>(6)</td><td>(22)</td><td>48%</td><td>■</td><td>72</td><td>234</td><td>10%</td><td>■</td></tr><tr><td>Asia IG</td><td>53</td><td>(2)</td><td>(14)</td><td>(28)</td><td>0%</td><td>■</td><td>53</td><td>198</td><td>0%</td><td>■</td></tr><tr><td>CDX IG</td><td>52</td><td>2</td><td>(1)</td><td>(3)</td><td>60%</td><td>■</td><td>46</td><td>111</td><td>38%</td><td>■</td></tr><tr><td>iTraxx Main</td><td>54</td><td>1</td><td>(3)</td><td>(3)</td><td>68%</td><td>■</td><td>44</td><td>138</td><td>39%</td><td>■</td></tr><tr><td>EM IG</td><td>80</td><td>(2)</td><td>(13)</td><td>(27)</td><td>0%</td><td>■</td><td>80</td><td>159</td><td>0%</td><td>■</td></tr><tr><td>Agency MBS</td><td>25</td><td>3</td><td>4</td><td>(17)</td><td>46%</td><td>■</td><td>14</td><td>88</td><td>12%</td><td>■</td></tr><tr><td>CLO AAAs</td><td>123</td><td>0</td><td>(5)</td><td>(12)</td><td>0%</td><td>■</td><td>115</td><td>233</td><td>15%</td><td>■</td></tr><tr><td>RMBS AAAs</td><td>125</td><td>0</td><td>(5)</td><td>(20)</td><td>12%</td><td>■</td><td>60</td><td>280</td><td>20%</td><td>■</td></tr><tr><td>US As</td><td>62</td><td>1</td><td>(5)</td><td>(11)</td><td>44%</td><td>■</td><td>58</td><td>145</td><td>11%</td><td>■</td></tr><tr><td>US BBBs</td><td>90</td><td>1</td><td>(10)</td><td>(18)</td><td>31%</td><td>■</td><td>89</td><td>199</td><td>10%</td><td>■</td></tr><tr><td>US 3-5Y</td><td>64</td><td>1</td><td>(6)</td><td>(13)</td><td>31%</td><td>■</td><td>50</td><td>158</td><td>23%</td><td>■</td></tr><tr><td>US 5-7Y</td><td>72</td><td>2</td><td>(5)</td><td>(19)</td><td>17%</td><td>■</td><td>66</td><td>173</td><td>13%</td><td>■</td></tr><tr><td>US 7-10Y</td><td>86</td><td>1</td><td>(7)</td><td>(16)</td><td>35%</td><td>■</td><td>81</td><td>200</td><td>11%</td><td>■</td></tr><tr><td>US 10Y+</td><td>89</td><td>2</td><td>(11)</td><td>(15)</td><td>34%</td><td>■</td><td>87</td><td>203</td><td>7%</td><td>■</td></tr><tr><td>US Financials</td><td>76</td><td>1</td><td>(8)</td><td>(12)</td><td>55%</td><td>■</td><td>71</td><td>188</td><td>24%</td><td>■</td></tr><tr><td>US Industrials</td><td>70</td><td>1</td><td>(7)</td><td>(14)</td><td>29%</td><td>■</td><td>69</td><td>160</td><td>7%</td><td>■</td></tr><tr><td>US Utilities</td><td>78</td><td>1</td><td>(8)</td><td>(18)</td><td>16%</td><td>■</td><td>77</td><td>161</td><td>6%</td><td>■</td></tr><tr><td>EUR As</td><td>69</td><td>(2)</td><td>(6)</td><td>(19)</td><td>49%</td><td>■</td><td>65</td><td>200</td><td>16%</td><td>■</td></tr><tr><td>EUR BBBs</td><td>89</td><td>(3)</td><td>(5)</td><td>(25)</td><td>50%</td><td>■</td><td>83</td><td>273</td><td>10%</td><td>■</td></tr><tr><td>EUR 3-5Y</td><td>77</td><td>(2)</td><td>(5)</td><td>(24)</td><td>47%</td><td>■</td><td>71</td><td>245</td><td>12%</td><td>■</td></tr><tr><td>EUR 5-7Y</td><td>90</td><td>(2)</td><td>(7)</td><td>(22)</td><td>43%</td><td>■</td><td>85</td><td>251</td><td>15%</td><td>■</td></tr><tr><td>EUR 7-10Y</td><td>95</td><td>(2)</td><td>(7)</td><td>(21)</td><td>39%</td><td>■</td><td>91</td><td>247</td><td>8%</td><td>■</td></tr><tr><td>EUR 10Y+</td><td>90</td><td>(3)</td><td>(8)</td><td>(18)</td><td>45%</td><td>■</td><td>88</td><td>234</td><td>9%</td><td>■</td></tr></table>

<table><tr><td>Global HY Credit</td><td>Current</td><td>1 Wk Δ</td><td>3 Mth Δ</td><td>12 Mth Δ</td><td>1Y %Tile</td><td>1Y %Tile Range</td><td>5Y Tights</td><td>5Y Wides</td><td>5Y %Tile</td><td>5Y %Tile Range</td></tr><tr><td>US HY</td><td>265</td><td>7</td><td>(16)</td><td>(47)</td><td>16%</td><td>■</td><td>250</td><td>583</td><td>7%</td><td>■</td></tr><tr><td>EUR HY</td><td>250</td><td>(13)</td><td>(40)</td><td>(59)</td><td>39%</td><td>■</td><td>247</td><td>668</td><td>8%</td><td>■</td></tr><tr><td>CDX HY</td><td>312</td><td>12</td><td>(14)</td><td>(33)</td><td>53%</td><td>■</td><td>269</td><td>627</td><td>31%</td><td>■</td></tr><tr><td>Xover</td><td>263</td><td>4</td><td>(2)</td><td>(31)</td><td>63%</td><td>■</td><td>225</td><td>662</td><td>23%</td><td>■</td></tr><tr><td>US BBs</td><td>157</td><td>4</td><td>(10)</td><td>(27)</td><td>20%</td><td>■</td><td>149</td><td>413</td><td>8%</td><td>■</td></tr><tr><td>US Bs</td><td>282</td><td>9</td><td>(25)</td><td>(17)</td><td>51%</td><td>■</td><td>236</td><td>653</td><td>27%</td><td>■</td></tr><tr><td>US CCCs</td><td>724</td><td>18</td><td>96</td><td>13</td><td>82%</td><td>■</td><td>444</td><td>1,133</td><td>45%</td><td>■</td></tr><tr><td>EUR HY BBs</td><td>149</td><td>(13)</td><td>(27)</td><td>(57)</td><td>26%</td><td>■</td><td>149</td><td>526</td><td>6%</td><td>■</td></tr><tr><td>EUR HY Bs</td><td>321</td><td>(19)</td><td>(71)</td><td>(9)</td><td>71%</td><td>■</td><td>279</td><td>837</td><td>21%</td><td>■</td></tr><tr><td>EUR HY CCCs</td><td>1,099</td><td>14</td><td>72</td><td>(4)</td><td>40%</td><td>■</td><td>556</td><td>1,549</td><td>43%</td><td>■</td></tr></table>

<table><tr><td>Asia Credit</td><td>Current</td><td>1 Wk Δ</td><td>3 Mth Δ</td><td>12 Mth Δ</td><td>1Y %Tile</td><td>1Y %Tile Range</td><td>5Y Tights</td><td>5Y Wides</td><td>5Y %Tile</td><td>5Y %Tile Range</td></tr><tr><td>iTraxx Japan</td><td>60</td><td>(1)</td><td>(2)</td><td>(2)</td><td>69%</td><td>■</td><td>42</td><td>117</td><td>55%</td><td>■</td></tr><tr><td>iTraxx Australia</td><td>72</td><td>(0)</td><td>(2)</td><td>(3)</td><td>70%</td><td>■</td><td>56</td><td>152</td><td>47%</td><td>■</td></tr><tr><td>Asia Credit</td><td>93</td><td>(3)</td><td>(14)</td><td>(41)</td><td>13%</td><td>■</td><td>93</td><td>407</td><td>3%</td><td>■</td></tr><tr><td>Asia IG</td><td>53</td><td>(2)</td><td>(14)</td><td>(28)</td><td>0%</td><td>■</td><td>53</td><td>198</td><td>0%</td><td>■</td></tr><tr><td>Asia HY</td><td>326</td><td>(16)</td><td>(23)</td><td>(124)</td><td>55%</td><td>■</td><td>309</td><td>1,536</td><td>11%</td><td>■</td></tr><tr><td>China IG</td><td>39</td><td>(3)</td><td>(17)</td><td>(35)</td><td>0%</td><td>■</td><td>39</td><td>226</td><td>0%</td><td>■</td></tr><tr><td>China HY</td><td>498</td><td>(18)</td><td>7</td><td>(64)</td><td>86%</td><td>■</td><td>345</td><td>2,570</td><td>33%</td><td>■</td></tr></table>

![](images/91770c2e3e6fddd8a00ba879083952e582f1e98ad420c4ac8ff33f2186575b0c.jpg)

<details>
<summary>bar chart</summary>

YTD Global Credit Returns
| Category | Total Return (%) | Excess Return (%) |
| :--- | :--- | :--- |
| US IG | 0.1 | 0.8 |
| US AAs | -0.3 | 0.4 |
| US As | -0.1 | 0.6 |
| US BBBs | 0.3 | 1.0 |
| EU IG | 0.5 | 0.6 |
| EU AAs | 0.3 | 0.5 |
| EU As | 0.4 | 0.6 |
| EU BBBs | 0.5 | 0.7 |
| Asia IG | 0.2 | 0.6 |
| US HY | 1.3 | 1.2 |
| US BBs | 1.3 | 1.3 |
| US Bs | 1.5 | 1.3 |
| US CCCs | 1.3 | 1.1 |
| EU HY | 1.3 | 1.3 |
| EU BBs | 1.3 | 1.3 |
| EU Bs | 1.2 | 1.1 |
| EU CCCs | 2.1 | 2.2 |
| US Loans | 1.3 | |
| EU Loans | 1.6 | |
The chart displays a single bar for each category, with the total return percentage labeled above the bars and excess return percentage below it.
</details>

![](images/18ae72366546b278dc5c8773b2bdae20a8b08366d88e9798d35036de34ef2f50.jpg)

<details>
<summary>bar chart</summary>

YTD Asset Class Returns
| Asset Class | Total Return (%) | Excess Return (%) |
| :--- | :--- | :--- |
| Treasuries | -0.5 | -1.0 |
| Aggregate | -0.2 | 0.3 |
| Agency | 0.1 | 0.6 |
| MBS | 0.1 | 0.3 |
| US IG | 0.8 | 0.1 |
| Asia IG | 0.2 | 0.6 |
| EUR IG | 0.5 | 0.6 |
| ABS | 0.6 | 0.4 |
| US HY | 1.3 | 1.2 |
| EUR HY | 1.3 | 1.3 |
| US Loans | 1.3 | 0 |
| EU Loans | 1.6 | 0 |
| S&P 500 | 8.4 | 0 |
</details>

Performance Across Asset Classes

<table><tr><td colspan="2">Market</td><td>Ccy</td><td>Latest</td><td>1Y</td><td>1 Mth Δ</td><td>3 Mth Δ</td><td>2026 Δ</td></tr><tr><td colspan="2">EQUITIES</td><td colspan="3">Level</td><td colspan="3">Total Returns (%)</td></tr><tr><td rowspan="5">US</td><td>S&amp;P 500</td><td>USD</td><td>7,384</td><td></td><td>1.9</td><td>8.4</td><td>8.4</td></tr><tr><td>Russell 2000</td><td>USD</td><td>2,834</td><td></td><td>(0.3)</td><td>10.0</td><td>14.8</td></tr><tr><td>DJIA</td><td>USD</td><td>50,867</td><td></td><td>3.5</td><td>6.5</td><td>6.6</td></tr><tr><td>NASDAQ</td><td>USD</td><td>25,709</td><td></td><td>1.6</td><td>13.2</td><td>10.9</td></tr><tr><td>MSCI EAFE</td><td>USD</td><td>3,074</td><td></td><td>2.1</td><td>4.7</td><td>8.3</td></tr><tr><td>Europe</td><td>MSCI EUROPE</td><td>EUR</td><td>208</td><td></td><td>3.1</td><td>5.0</td><td>7.6</td></tr><tr><td rowspan="5">Asia</td><td>TOPIX</td><td>JPY</td><td>3,952</td><td></td><td>5.9</td><td>7.8</td><td>17.1</td></tr><tr><td>HSI</td><td>HKD</td><td>24,962</td><td></td><td>(2.9)</td><td>(0.2)</td><td>(1.4)</td></tr><tr><td>CSI 300</td><td>CNY</td><td>4,817</td><td></td><td>0.4</td><td>4.0</td><td>4.6</td></tr><tr><td>KOSPI</td><td>KRW</td><td>8,161</td><td></td><td>17.7</td><td>46.8</td><td>94.8</td></tr><tr><td>Nifty</td><td>INR</td><td>23,367</td><td></td><td>(2.5)</td><td>(5.4)</td><td>(10.1)</td></tr><tr><td>EM</td><td>MSCI EM</td><td>USD</td><td>1,717</td><td></td><td>4.4</td><td>15.0</td><td>23.3</td></tr></table>

<table><tr><td colspan="2">RATES</td><td colspan="3">Yield (%)</td><td colspan="3">Yield Change (bp)</td></tr><tr><td>US</td><td>US 2 Year</td><td>USD</td><td>4.15</td><td>■</td><td>14</td><td>35</td><td>67</td></tr><tr><td></td><td>US 5 Year</td><td>USD</td><td>4.27</td><td>■</td><td>13</td><td>32</td><td>54</td></tr><tr><td></td><td>US 10 Year</td><td>USD</td><td>4.53</td><td>■</td><td>9</td><td>21</td><td>36</td></tr><tr><td></td><td>US 30 Year</td><td>USD</td><td>5.00</td><td>■</td><td>2</td><td>9</td><td>15</td></tr><tr><td>Europe</td><td>Bund 2Y</td><td>EUR</td><td>2.69</td><td>■</td><td>16</td><td>8</td><td>57</td></tr><tr><td></td><td>Bund 5Y</td><td>EUR</td><td>2.77</td><td>■</td><td>13</td><td>4</td><td>32</td></tr><tr><td></td><td>Bund 10Y</td><td>EUR</td><td>3.04</td><td>■</td><td>10</td><td>3</td><td>18</td></tr><tr><td></td><td>Bund 30Y</td><td>EUR</td><td>3.57</td><td>■</td><td>7</td><td>11</td><td>9</td></tr><tr><td>Japan</td><td>Japan 5Y</td><td>JPY</td><td>1.93</td><td>■</td><td>2</td><td>14</td><td>37</td></tr><tr><td></td><td>Japan 10Y</td><td>JPY</td><td>2.67</td><td>■</td><td>1</td><td>32</td><td>61</td></tr><tr><td>China</td><td>China 5Y</td><td>CNY</td><td>1.41</td><td>■</td><td>0</td><td>(11)</td><td>(20)</td></tr><tr><td></td><td>China 10Y</td><td>CNY</td><td>1.72</td><td>■</td><td>1</td><td>(10)</td><td>(13)</td></tr><tr><td>India</td><td>India 5Y</td><td>INR</td><td>6.65</td><td>■</td><td>(18)</td><td>(10)</td><td>34</td></tr><tr><td></td><td>India 10Y</td><td>INR</td><td>6.98</td><td>■</td><td>(3)</td><td>(5)</td><td>39</td></tr><tr><td>South Korea</td><td>South Korea 5Y</td><td>KRW</td><td>4.12</td><td>■</td><td>19</td><td>34</td><td>88</td></tr><tr><td></td><td>South Korea 10Y</td><td>KRW</td><td>4.25</td><td>■</td><td>18</td><td>37</td><td>87</td></tr></table>

<table><tr><td colspan="2">Market</td><td>Ccy</td><td>Latest</td><td>1Y</td><td>1 Mth Δ</td><td>3 Mth Δ</td><td>2026 Δ</td></tr><tr><td>FX</td><td></td><td></td><td colspan="2">Spot</td><td colspan="3">% Change (vs. USD)</td></tr><tr><td rowspan="4">G10</td><td>EURUSD</td><td>-</td><td>1.15</td><td>■</td><td>(1.2)</td><td>(0.3)</td><td>(1.9)</td></tr><tr><td>GBPUSD</td><td>-</td><td>1.33</td><td>■</td><td>(0.8)</td><td>0.9</td><td>(1.0)</td></tr><tr><td>USDCAD</td><td>-</td><td>1.39</td><td>■</td><td>(1.0)</td><td>(0.2)</td><td>(1.6)</td></tr><tr><td>USDJPY</td><td>-</td><td>160</td><td>■</td><td>(0.6)</td><td>(1.0)</td><td>(2.3)</td></tr><tr><td rowspan="5">APAC / EM</td><td>USDBRL</td><td>-</td><td>5.2</td><td>■</td><td>(2.6)</td><td>0.2</td><td>5.6</td></tr><tr><td>USDINR</td><td>-</td><td>94.9</td><td>■</td><td>0.1</td><td>(0.1)</td><td>(5.6)</td></tr><tr><td>USDCNY</td><td>-</td><td>7</td><td>■</td><td>(0.3)</td><td>1.5</td><td>2.9</td></tr><tr><td>USDCNH</td><td>-</td><td>7</td><td>■</td><td>(0.4)</td><td>1.4</td><td>2.7</td></tr><tr><td>USDKRW</td><td>-</td><td>1558</td><td>■</td><td>(3.6)</td><td>(2.8)</td><td>(7.9)</td></tr></table>

<table><tr><td colspan="4">COMMODITIES</td><td colspan="3">% Change</td></tr><tr><td>S&amp;P GSCI</td><td>USD</td><td>693.8</td><td></td><td>(0)</td><td>(7)</td><td>26</td></tr><tr><td>Oil (WTIC, $/bbl)</td><td>USD</td><td>94.3</td><td></td><td>4</td><td>(11)</td><td>58</td></tr><tr><td>Brent Crude</td><td>USD</td><td>97.2</td><td></td><td>1</td><td>(21)</td><td>53</td></tr><tr><td>Natural Gas ($/MMBtu)</td><td>USD</td><td>3.2</td><td></td><td>(2)</td><td>12</td><td>(12)</td></tr><tr><td>Copper ($/lb)</td><td>USD</td><td>628</td><td></td><td>(2)</td><td>12</td><td>11</td></tr><tr><td>Gold ($/oz)</td><td>USD</td><td>4,299</td><td></td><td>(5)</td><td>(7)</td><td>(0)</td></tr></table>

<table><tr><td colspan="2">CREDIT</td><td colspan="3">Spread (bp)</td><td colspan="3">Spread Change (bp)</td></tr><tr><td rowspan="2">US</td><td>IG Corporates</td><td>USD</td><td>73</td><td></td><td>1</td><td>(16)</td><td>(5)</td></tr><tr><td>HY Corporates</td><td>USD</td><td>265</td><td></td><td>8</td><td>(52)</td><td>(1)</td></tr><tr><td rowspan="2">EUR</td><td>IG Corporates</td><td>EUR</td><td>77</td><td></td><td>(3)</td><td>(21)</td><td>(2)</td></tr><tr><td>HY Corporates</td><td>EUR</td><td>250</td><td></td><td>(13)</td><td>(82)</td><td>(15)</td></tr><tr><td>EM</td><td>EM Sovereign</td><td>USD</td><td>163</td><td></td><td>(4)</td><td>(5

[中间内容因长度限制已省略]

 details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India

## Disclosure Section (Cont.)

Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. dr0806

## The Americas

1585 Broadway

New York, NY 10036-8293

United States

+1 212 761 4000

## Europe

20 Bank Street, Canary Wharf

London E14 4AD

United Kingdom

+44 (0)20 7425 8000

## Japan

1-9-7 Otemachi, Chiyoda-ku

Tokyo 100-8104

Japan

+81 (0) 3 6836 5000

## Asia/Pacific

1 Austin Road West

Kowloon

Hong Kong

+852 2848 5200
"""
