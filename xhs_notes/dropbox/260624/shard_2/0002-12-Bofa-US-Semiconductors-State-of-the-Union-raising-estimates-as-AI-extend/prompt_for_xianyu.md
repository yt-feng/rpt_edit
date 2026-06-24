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
US Semiconductors

# State of the Union: raising estimates as AI extends visibility into 2028

Price Objective Change

## Inflation plus stronger demand = higher industry forecasts

We reiterate our thesis of the AI industry moving to addressing structural and physical (chips, power) constraints, from having to defend return-on-investment before. Memory chip shortages and price inflation remain the critical moving pieces, and we update our semis industry models and price objectives to conform to the updated industry estimates. Specifically, we raise our CY30E total semis industry TAM to \$2.7Tn, or +28% CAGR between CY25-30E, from \$2.3Tn/+23% CAGR prior, led mostly by growth in memory/data center, and also incrementally by recovery in auto/industrial. Our new industry forecasts/ests derive higher price objectives for key semiconductor and semicap equipment companies as summarized in Exhibit 1.

## Top 5 themes driving next \$1Tn in incremental semi sales

The chip industry took \~50 years to generate its first \$1Tn in sales. We expect AI to help add another \$1Tn in just the next five years. Key drivers include: 1) AI data center systems TAM of \~\$1.7Tn by CY30E, growing from just \~\$273bn in CY25, led by Insatiable demand for compute (see our AI 2030 report); 2) Memory strength/durability, led by LTAs providing greater confidence in 2-3-year supply/demand/pricing visibility, as seen in recent MU/Anthropic partnership; 3) Semicap/Reshoring/EDA – clear beneficiaries from extending supply agreements, rising complexity of chips/packaging – see WFE \$250bn by CY28E (more below); 4) Analogs benefiting from rising power reqs (see our AI power semis primer); 5) Agentic CPU demand, totaling \~\$170bn in server opp'ty with benefits across x86/ARM (see our AI CPU TAM report); and 6) Physical AI over time with also some benefits to DCs for handling more complex queries.

## WFE: raising TAM, now see \~\$250-300bn in CY28-30E

We tweak our CY27E WFE higher by +4% to \$190bn (+31% YoY) from \$183bn (+27% YoY) prior while materially raising CY28E by 23% to \$250bn (+32% YoY) from \$203bn (+11% YoY) prior. Our new CY29/30E WFE forecasts are \$268bn (+7% YoY)/\$292bn (+9%). The upward revisions are based on our expectation for greater cleanroom availability by CY28, LT visibility afford by memory LTAs, and critical tech inflections which tend to drive WFE-per-wafer higher during upcycles across memory and logic (see analysis in the back). Customer and capacity progress at INTC and Samsung are also positives for advanced F/L while Terafab potential could also potentially be credited.

## Core semis benefit from AI, consumer remains a headwind

Of the \~\$2.7Tn total semis outlook by CY30E, we see core semis (non-memory) outlook of \~\$1.1Tn, growing at \~14% CAGR from \~\$567bn in CY25. We see growth driven by server silicon (+24% CAGR) and wired comms (+15%) driven by AI-related chip/networking demand, while consumer-facing PCs (+2%) and smartphones (+0%) remain weak on unit headwinds. We see incrementally better outlook in industrial (+11%) and automotive (+8%) on modest unit recovery and continued content gains.

## Key PO changes: MU, semicap/complexity, AI beneficiaries

Based on new industry & WFE forecasts, we raise ests/POs across related beneficiaries.

## 23 June 2026

Equity
United States
Semiconductors

Vivek Arya
Research Analyst
BofAS
vivek.arya@bofa.com

Duksan Jang
Research Analyst
BofAS
duksan.jang@bofa.com

Michael Mani
Research Analyst
BofAS
michael.mani@bofa.com

Liam Pharr
Research Analyst
BofAS
liam.pharr@bofa.com

## Exhibit 1: We raise POs across select AI/compute, memory, and semicap companies PO changes

<table><tr><td></td><td colspan="3">PO Changes</td></tr><tr><td></td><td>OLD</td><td>NEW</td><td>Rating</td></tr><tr><td>ACLS</td><td>$130</td><td>$156</td><td>U/P</td></tr><tr><td>AEIS</td><td>$430</td><td>$450</td><td>BUY</td></tr><tr><td>ALAB</td><td>$240</td><td>$450</td><td>NEUTRAL</td></tr><tr><td>AMAT</td><td>$540</td><td>$720</td><td>BUY</td></tr><tr><td>ARM</td><td>$335</td><td>$460</td><td>NEUTRAL</td></tr><tr><td>CRDO</td><td>$252</td><td>$340</td><td>BUY</td></tr><tr><td>INTC</td><td>$135</td><td>$160</td><td>BUY</td></tr><tr><td>KLAC</td><td>$210</td><td>$317</td><td>BUY</td></tr><tr><td>LRCX</td><td>$330</td><td>$480</td><td>BUY</td></tr><tr><td>MKSI</td><td>$380</td><td>$500</td><td>BUY</td></tr><tr><td>MRVL</td><td>$240</td><td>$365</td><td>BUY</td></tr><tr><td>MU</td><td>$950</td><td>$1,500</td><td>BUY</td></tr><tr><td>TER</td><td>$365</td><td>$525</td><td>BUY</td></tr></table>

U/P = Underperform

Source: BofA Global Research

BofA GLOBAL RESEARCH

Glossary at end of report

## Contents

Summary of PO changes 3
Global Semis Forecast Update 4
Wafer Fab Equipment (WFE) Forecast 6
The case for \$250bn WFE by CY28E 8
MU: Raise PO to \$1,500, Buy 14
    Memory content per AI system scales faster than compute 14
    Structurally lower supply elasticity 15
    DRAM/NAND Pricing Trends 18
    MU Estimate Changes 18
    MU Valuation Analysis, \$1,500 PO 19
INTC: Raise PO to \$160, Buy 20
    Fully established IDM by CY30, EPS power \$6+ 20
ARM: Raise PO to \$460, Neutral 21
    Sum-of-Parts Valuation: IP & Chip Businesses 21
CRDO: Raise PO to \$340, Buy 22
MRVL: Raise PO to \$365, Buy 23
    EPS Power \$15+ by CY30E, see \$365 PO 23
ALAB: Raise PO to \$450, Neutral 24
    EPS Power \$9+ by CY30E, see \$450 PO 24
TER: Raise PO to \$525, Buy 26
ACLS: Raise PO to \$156, Underperform 27
    VECO already generally priced in at EPS power \$9+ 27
Semicap PO changes and LT EPS power 28

## Summary of PO changes

Exhibit 2: We raise POs for ACLS, AEIS, ALAB, AMAT, ARM, CRDO, INTC, KLAC, LRCX, MKSI, MRVL, MU and TER. We move to a CY28E valuation basis for multiple companies (from CY27E prior).

Summary of PO changes

<table><tr><td colspan="4">PO Changes</td><td colspan="2">POBR Changes</td></tr><tr><td></td><td>OLD</td><td>NEW</td><td>Rating</td><td>Old POBR</td><td>New POBR</td></tr><tr><td>ACLS</td><td>$130</td><td>$156</td><td>U/P</td><td>27x CY27E PE</td><td>26x CY28E PE</td></tr><tr><td>AEIS</td><td>$430</td><td>$450</td><td>BUY</td><td>36x CY27E PE</td><td>32x CY28E PE</td></tr><tr><td>ALAB</td><td>$240</td><td>$450</td><td>NEUTRAL</td><td>66x CY27E PE</td><td>77x CY28E PE (~2.0x PEG)</td></tr><tr><td>AMAT</td><td>$540</td><td>$720</td><td>BUY</td><td>32x CY27E PE</td><td>36x CY28E PE</td></tr><tr><td>ARM</td><td>$335</td><td>$460</td><td>NEUTRAL</td><td>SOTP CY30E discounted back 2 years (2.0x PEG for IP + 35x PE for Chip)</td><td>SOTP CY30E discounted back 2 years (2.5x PEG for IP + 31x PE for Chip)</td></tr><tr><td>CRDO</td><td>$252</td><td>$340</td><td>BUY</td><td>33x CY27E PE</td><td>34x CY28E PE</td></tr><tr><td>INTC</td><td>$135</td><td>$160</td><td>BUY</td><td>25x CY30E EPS Power, discounted back 2 years</td><td>31x CY30E EPS Power, discounted back 2 years</td></tr><tr><td>KLAC</td><td>$210</td><td>$317</td><td>BUY</td><td>40x CY27E PE</td><td>53x CY28E PE</td></tr><tr><td>LRCX</td><td>$330</td><td>$480</td><td>BUY</td><td>36x CY27E PE</td><td>47x CY28E PE</td></tr><tr><td>MKSI</td><td>$380</td><td>$500</td><td>BUY</td><td>18x CY27E EV/EBIDA</td><td>22x CY28E EV/EBITDA</td></tr><tr><td>MRVL</td><td>$240</td><td>$365</td><td>BUY</td><td>30x CY28E PE</td><td>31x CY30E EPS Power, discounted back 2 years</td></tr><tr><td>MU</td><td>$950</td><td>$1,500</td><td>BUY</td><td>SOTP CY27E (3.1x P/B for trad memory + 27x PE for HBM)</td><td>SOTP CY28E (2.5x P/B for trad memory + 31x PE for HBM)</td></tr><tr><td>TER</td><td>$365</td><td>$525</td><td>BUY</td><td>41x CY27E PE</td><td>41x CY28E PE</td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH

## Global Semis Forecast Update

We model CY26 semis/core semis (ex-memory) growth of +103%/+27% YoY, led by growth in memory, data center, and modestly improved outlook in industrial and automotive, offset by continued unit headwinds in PCs/smartphones/consumer.

By end market, we now model (1) compute and storage up +48% YoY (continued server strength); (2) wireless comms down -12% YoY (smartphone unit headwind); (3) auto sales up +4% on sluggish units but improving content; (4) Industrial up +18% YoY on improved end demand and inventory dynamics since 2H25; (5) consumer down -7% YoY; and (6) wired comms up +29% YoY on data center related infra buildout.

Exhibit 3: We model semis/core semis sales up +103%/+27% YoY in CY26E Summary of BofA Semiconductor forecasts by end market

<table><tr><td>Revenue ($mn)</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>CAGR&#x27;15-25</td><td>CAGR&#x27;19-25</td><td>CAGR&#x27;25-30</td></tr><tr><td>Total Semis</td><td>$451</td><td>$572</td><td>$594</td><td>$528</td><td>$633</td><td>$787</td><td>$1,593</td><td>$2,033</td><td>$2,194</td><td>$2,498</td><td>$2,734</td><td>8.9%</td><td>11.1%</td><td>28.3%</td></tr><tr><td>YoY%</td><td>7.7%</td><td>27.0%</td><td>3.8%</td><td>(11.0%)</td><td>19.7%</td><td>24.3%</td><td>102.6%</td><td>27.6%</td><td>7.9%</td><td>13.8%</td><td>9.5%</td><td></td><td></td><td></td></tr><tr><td>Memory</td><td>$128</td><td>$170</td><td>$150</td><td>$94</td><td>$170</td><td>$220</td><td>$874</td><td>$1,184</td><td>$1,243</td><td>$1,469</td><td>$1,646</td><td>11.0%</td><td>11.8%</td><td>49.6%</td></tr><tr><td>YoY%</td><td>13.5%</td><td>33.4%</td><td>(11.9%)</td><td>(37.4%)</td><td>81.3%</td><td>28.9%</td><td>297.8%</td><td>35.5%</td><td>5.0%</td><td>18.2%</td><td>12.0%</td><td></td><td></td><td></td></tr><tr><td>Core Semis (ex-memory)</td><td>$323</td><td>$402</td><td>$444</td><td>$435</td><td>$463</td><td>$567</td><td>$720</td><td>$849</td><td>$951</td><td>$1,028</td><td>$1,089</td><td>8.2%</td><td>10.8%</td><td>13.9%</td></tr><tr><td>YoY%</td><td>5.6%</td><td>24.4%</td><td>10.5%</td><td>(2.1%)</td><td>6.4%</td><td>22.6%</td><td>27.0%</td><td>18.0%</td><td>11.9%</td><td>8.2%</td><td>5.9%</td><td></td><td></td><td></td></tr><tr><td>Compute and Storage</td><td>$108</td><td>$128</td><td>$154</td><td>$167</td><td>$205</td><td>$299</td><td>$441</td><td>$547</td><td>$621</td><td>$674</td><td>$715</td><td>13.7%</td><td>20.7%</td><td>19.1%</td></tr><tr><td>YoY%</td><td>11.2%</td><td>19.1%</td><td>20.3%</td><td>8.4%</td><td>22.5%</td><td>46.2%</td><td>47.5%</td><td>24.0%</td><td>13.4%</td><td>8.7%</td><td>6.1%</td><td></td><td></td><td></td></tr><tr><td>PCs</td><td>$56</td><td>$68</td><td>$59</td><td>$52</td><td>$57</td><td>$61</td><td>$56</td><td>$58</td><td>$62</td><td>$66</td><td>$68</td><td>4.3%</td><td>4.3%</td><td>2.1%</td></tr><tr><td>YoY%</td><td>16.5%</td><td>22.3%</td><td>(12.4%)</td><td>(11.8%)</td><td>9.3%</td><td>7.2%</td><td>(9.3%)</td><td>4.5%</td><td>5.8%</td><td>7.2%</td><td>3.1%</td><td></td><td></td><td></td></tr><tr><td>Servers (silicon only)</td><td>$27</td><td>$32</td><td>$63</td><td>$80</td><td>$119</td><td>$209</td><td>$356</td><td>$459</td><td>$528</td><td>$577</td><td>$615</td><td>28.2%</td><td>41.0%</td><td>24.1%</td></tr><tr><td>YoY%</td><td>2.2%</td><td>16.9%</td><td>97.3%</td><td>27.5%</td><td>48.7%</td><td>75.5%</td><td>70.6%</td><td>28.8%</td><td>15.1%</td><td>9.2%</td><td>6.6%</td><td></td><td></td><td></td></tr><tr><td>Wireless Communications</td><td>$85</td><td>$104</td><td>$111</td><td>$94</td><td>$93</td><td>$91</td><td>$80</td><td>$80</td><td>$86</td><td>$90</td><td>$93</td><td>3.3%</td><td>2.9%</td><td>0.4%</td></tr><tr><td>YoY%</td><td>11.1%</td><td>22.3%</td><td>6.8%</td><td>(15.8%)</td><td>(0.5%)</td><td>(2.4%)</td><td>(11.6%)</td><td>(0.2%)</td><td>7.1%</td><td>4.6%</td><td>3.3%</td><td></td><td></td><td></td></tr><tr><td>Smartphone</td><td>$71</td><td>$88</td><td>$91</td><td>$77</td><td>$80</td><td>$78</td><td>$68</td><td>$67</td><td>$72</td><td>$76</td><td>$78</td><td>3.9%</td><td>3.5%</td><td>0.0%</td></tr><tr><td>YoY%</td><td>12.3%</td><td>23.7%</td><td>3.2%</td><td>(15.4%)</td><td>3.6%</td><td>(2.0%)</td><td>(13.0%)</td><td>(1.0%)</td><td>7.5%</td><td>4.7%</td><td>3.2%</td><td></td><td></td><td></td></tr><tr><td>Wireless Infrastructure</td><td>$14</td><td>$16</td><td>$20</td><td>$16</td><td>$13</td><td>$13</td><td>$12</td><td>$13</td><td>$13</td><td>$14</td><td>$14</td><td>2.9%</td><td>(0.7%)</td><td>2.8%</td></tr><tr><td>YoY%</td><td>5.0%</td><td>14.7%</td><td>27.1%</td><td>(17.5%)</td><td>(20.0%)</td><td>(5.0%)</td><td>(3.0%)</td><td>4.0%</td><td>5.0%</td><td>4.0%</td><td>4.0%</td><td></td><td></td><td></td></tr><tr><td>Automotive</td><td>$34</td><td>$46</td><td>$49</td><td>$59</td><td>$56</td><td>$52</td><td>$54</td><td>$60</td><td>$67</td><td>$73</td><td>$78</td><td>5.7%</td><td>5.6%</td><td>8.3%</td></tr><tr><td>YoY%</td><td>(9.1%)</td><td>34.6%</td><td>5.4%</td><td>22.3%</td><td>(6.4%)</td><td>(6.0%)</td><td>4.1%</td><td>10.6%</td><td>11.2%</td><td>9.0%</td><td>6.7%</td><td></td><td></td><td></td></tr><tr><td>Global Automotive Units (mn)</td><td>74.6</td><td>77.2</td><td>82.3</td><td>90.5</td><td>92.5</td><td>94.0</td><td>91.9</td><td>92.4</td><td>94.8</td><td>96.6</td><td>97.7</td><td>0.6%</td><td>0.9%</td><td>0.8%</td></tr><tr><td>YoY%</td><td>(16.1%)</td><td>3.5%</td><td>6.7%</td><td>9.9%</td><td>2.2%</td><td>1.6%</td><td>(2.2%)</td><td>0.5%</td><td>2.6%</td><td>1.9%</td><td>1.1%</td><td></td><td></td><td></td></tr><tr><td>Auto semi content ($/LV) / Inv. Adj.</td><td>$459</td><td>$597</td><td>$590</td><td>$657</td><td>$602</td><td>$556</td><td>$593</td><td>$652</td><td>$707</td><td>$756</td><td>$798</td><td>5.1%</td><td>4.6%</td><td>7.5%</td></tr><tr><td>YoY%</td><td>8.4%</td><td>30.0%</td><td>(1.1%)</td><td>11.3%</td><td>(8.5%)</td><td>(7.5%)</td><td>6.5%</td><td>10.0%</td><td>8.4%</td><td>7.0%</td><td>5.5%</td><td></td><td></td><td></td></tr><tr><td>Industrial &amp; Other</td><td>$43</td><td>$54</td><td>$62</td><td>$59</td><td>$45</td><td>$50</td><td>$59</td><td>$66</td><td>$73</td><td>$78</td><td>$82</td><td>4.1%</td><td>2.1%</td><td>10.6%</td></tr><tr><td>YoY%</td><td>(2.6%)</td><td>26.5%</td><td>15.3%</td><td>(4.8%)</td><td>(24.3%)</td><td>10.8%</td><td>18.2%</td><td>12.5%</td><td>9.8%</td><td>7.2%</td><td>5.6%</td><td></td><td></td><td></td></tr><tr><td>Automation</td><td>$10</td><td>$13</td><td>$15</td><td>$15</td><td>$12</td><td>$13</td><td>$16</td><td>$18</td><td>$21</td><td>$23</td><td>$25</td><td>6.4%</td><td>4.6%</td><td>13.6%</td></tr><tr><td>YoY%</td><td>(3.0%)</td><td>29.5%</td><td>17.0%</td><td>(1.0%)</td><td>(15.0%)</td><td>5.6%</td><td>20.1%</td><td>16.6%</td><td>13.2%</td><td>10.1%</td><td>8.5%</td><td></td><td></td><td></td></tr><tr><td>Power/Energy</td><td>$6</td><td>$7</td><td>$9</td><td>$9</td><td>$8</td><td>$8</td><td>$9</td><td>$10</td><td>$11</td><td>$11</td><td>$12</td><td>6.8%</td><td>5.3%</td><td>7.8%</td></tr><tr><td>YoY%</td><td>(0.5%)</td><td>25.4%</td><td>22.0%</td><td>5.0%</td><td>(18.0%)</td><td>4.1%</td><td>13.5%</td><td>10.2%</td><td>6.2%</td><td>5.3%</td><td>4.1%</td><td></td><td></td><td></td></tr><tr><td>Consumer</td><td>$35</td><td>$48</td><td>$48</td><td>$30</td><td>$31</td><td>$33</td><td>$31</td><td>$31</td><td>$32</td><td>$33</td><td>$35</td><td>1.1%</td><td>(0.0%)</td><td>1.3%</td></tr><tr><td>YoY%</td><td>6.5%</td><td>37.5%</td><td>0.1%</td><td>(37.1%)</td><td>3.4%</td><td>4.7%</td><td>(6.9%)</td><td>(0.1%)</td><td>3.1%</td><td>6.3%</td><td>4.8%</td><td></td><td></td><td></td></tr><tr><td>TVs</td><td>$10</td><td>$14</td><td>$14</td><td>$11</td><td>$11</td><td>$11</td><td>$11</td><td>$12</td><td>$12</td><td>$12</td><td>$13</td><td>0.3%</td><td>2.8%</td><td>2.8%</td></tr><tr><td>YoY%</td><td>10.5%</td><td>37.1%</td><td>1.8%</td><td>(21.7%)</td><td>(4.0%)</td><td>2.1%</td><td>2.3%</td><td>2.8%</td><td>2.8%</td><td>3.0%</td><td>3.0%</td><td></td><td></td><td></td></tr><tr><td>Video console SoCs (Gaming)</td><t

[中间内容因长度限制已省略]

he extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and

employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
