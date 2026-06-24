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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`美国银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份美国银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

<table><tr><td>Revenue ($mn)</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>CAGR&#x27;15-25</td><td>CAGR&#x27;19-25</td><td>CAGR&#x27;25-30</td></tr><tr><td>Total Semis</td><td>$451</td><td>$572</td><td>$594</td><td>$528</td><td>$633</td><td>$787</td><td>$1,593</td><td>$2,033</td><td>$2,194</td><td>$2,498</td><td>$2,734</td><td>8.9%</td><td>11.1%</td><td>28.3%</td></tr><tr><td>YoY%</td><td>7.7%</td><td>27.0%</td><td>3.8%</td><td>(11.0%)</td><td>19.7%</td><td>24.3%</td><td>102.6%</td><td>27.6%</td><td>7.9%</td><td>13.8%</td><td>9.5%</td><td></td><td></td><td></td></tr><tr><td>Memory</td><td>$128</td><td>$170</td><td>$150</td><td>$94</td><td>$170</td><td>$220</td><td>$874</td><td>$1,184</td><td>$1,243</td><td>$1,469</td><td>$1,646</td><td>11.0%</td><td>11.8%</td><td>49.6%</td></tr><tr><td>YoY%</td><td>13.5%</td><td>33.4%</td><td>(11.9%)</td><td>(37.4%)</td><td>81.3%</td><td>28.9%</td><td>297.8%</td><td>35.5%</td><td>5.0%</td><td>18.2%</td><td>12.0%</td><td></td><td></td><td></td></tr><tr><td>Core Semis (ex-memory)</td><td>$323</td><td>$402</td><td>$444</td><td>$435</td><td>$463</td><td>$567</td><td>$720</td><td>$849</td><td>$951</td><td>$1,028</td><td>$1,089</td><td>8.2%</td><td>10.8%</td><td>13.9%</td></tr><tr><td>YoY%</td><td>5.6%</td><td>24.4%</td><td>10.5%</td><td>(2.1%)</td><td>6.4%</td><td>22.6%</td><td>27.0%</td><td>18.0%</td><td>11.9%</td><td>8.2%</td><td>5.9%</td><td></td><td></td><td></td></tr><tr><td>Compute and Storage</td><td>$108</td><td>$128</td><td>$154</td><td>$167</td><td>$205</td><td>$299</td><td>$441</td><td>$547</td><td>$621</td><td>$674</td><td>$715</td><td>13.7%</td><td>20.7%</td><td>19.1%</td></tr><tr><td>YoY%</td><td>11.2%</td><td>19.1%</td><td>20.3%</td><td>8.4%</td><td>22.5%</td><td>46.2%</td><td>47.5%</td><td>24.0%</td><td>13.4%</td><td>8.7%</td><td>6.1%</td><td></td><td></td><td></td></tr><tr><td>PCs</td><td>$56</td><td>$68</td><td>$59</td><td>$52</td><td>$57</td><td>$61</td><td>$56</td><td>$58</td><td>$62</td><td>$66</td><td>$68</td><td>4.3%</td><td>4.3%</td><td>2.1%</td></tr><tr><td>YoY%</td><td>16.5%</td><td>22.3%</td><td>(12.4%)</td><td>(11.8%)</td><td>9.3%</td><td>7.2%</td><td>(9.3%)</td><td>4.5%</td><td>5.8%</td><td>7.2%</td><td>3.1%</td><td></td><td></td><td></td></tr><tr><td>Servers (silicon only)</td><td>$27</td><td>$32</td><td>$63</td><td>$80</td><td>$119</td><td>$209</td><td>$356</td><td>$459</td><td>$528</td><td>$577</td><td>$615</td><td>28.2%</td><td>41.0%</td><td>24.1%</td></tr><tr><td>YoY%</td><td>2.2%</td><td>16.9%</td><td>97.3%</td><td>27.5%</td><td>48.7%</td><td>75.5%</td><td>70.6%</td><td>28.8%</td><td>15.1%</td><td>9.2%</td><td>6.6%</td><td></td><td></td><td></td></tr><tr><td>Wireless Communications</td><td>$85</td><td>$104</td><td>$111</td><td>$94</td><td>$93</td><td>$91</td><td>$80</td><td>$80</td><td>$86</td><td>$90</td><td>$93</td><td>3.3%</td><td>2.9%</td><td>0.4%</td></tr><tr><td>YoY%</td><td>11.1%</td><td>22.3%</td><td>6.8%</td><td>(15.8%)</td><td>(0.5%)</td><td>(2.4%)</td><td>(11.6%)</td><td>(0.2%)</td><td>7.1%</td><td>4.6%</td><td>3.3%</td><td></td><td></td><td></td></tr><tr><td>Smartphone</td><td>$71</td><td>$88</td><td>$91</td><td>$77</td><td>$80</td><td>$78</td><td>$68</td><td>$67</td><td>$72</td><td>$76</td><td>$78</td><td>3.9%</td><td>3.5%</td><td>0.0%</td></tr><tr><td>YoY%</td><td>12.3%</td><td>23.7%</td><td>3.2%</td><td>(15.4%)</td><td>3.6%</td><td>(2.0%)</td><td>(13.0%)</td><td>(1.0%)</td><td>7.5%</td><td>4.7%</td><td>3.2%</td><td></td><td></td><td></td></tr><tr><td>Wireless Infrastructure</td><td>$14</td><td>$16</td><td>$20</td><td>$16</td><td>$13</td><td>$13</td><td>$12</td><td>$13</td><td>$13</td><td>$14</td><td>$14</td><td>2.9%</td><td>(0.7%)</td><td>2.8%</td></tr><tr><td>YoY%</td><td>5.0%</td><td>14.7%</td><td>27.1%</td><td>(17.5%)</td><td>(20.0%)</td><td>(5.0%)</td><td>(3.0%)</td><td>4.0%</td><td>5.0%</td><td>4.0%</td><td>4.0%</td><td></td><td></td><td></td></tr><tr><td>Automotive</td><td>$34</td><td>$46</td><td>$49</td><td>$59</td><td>$56</td><td>$52</td><td>$54</td><td>$60</td><td>$67</td><td>$73</td><td>$78</td><td>5.7%</td><td>5.6%</td><td>8.3%</td></tr><tr><td>YoY%</td><td>(9.1%)</td><td>34.6%</td><td>5.4%</td><td>22.3%</td><td>(6.4%)</td><td>(6.0%)</td><td>4.1%</td><td>10.6%</td><td>11.2%</td><td>9.0%</td><td>6.7%</td><td></td><td></td><td></td></tr><tr><td>Global Automotive Units (mn)</td><td>74.6</td><td>77.2</td><td>82.3</td><td>90.5</td><td>92.5</td><td>94.0</td><td>91.9</td><td>92.4</td><td>94.8</td><td>96.6</td><td>97.7</td><td>0.6%</td><td>0.9%</td><td>0.8%</td></tr><tr><td>YoY%</td><td>(16.1%)</td><td>3.5%</td><td>6.7%</td><td>9.9%</td><td>2.2%</td><td>1.6%</td><td>(2.2%)</td><td>0.5%</td><td>2.6%</td><td>1.9%</td><td>1.1%</td><td></td><td></td><td></td></tr><tr><td>Auto semi content ($/LV) / Inv. Adj.</td><td>$459</td><td>$597</td><td>$590</td><td>$657</td><td>$602</td><td>$556</td><td>$593</td><td>$652</td><td>$707</td><td>$756</td><td>$798</td><td>5.1%</td><td>4.6%</td><td>7.5%</td></tr><tr><td>YoY%</td><td>8.4%</td><td>30.0%</td><td>(1.1%)</td><td>11.3%</td><td>(8.5%)</td><td>(7.5%)</td><td>6.5%</td><td>10.0%</td><td>8.4%</td><td>7.0%</td><td>5.5%</td><td></td><td></td><td></td></tr><tr><td>Industrial &amp; Other</td><td>$43</td><td>$54</td><td>$62</td><td>$59</td><td>$45</td><td>$50</td><td>$59</td><td>$66</td><td>$73</td><td>$78</td><td>$82</td><td>4.1%</td><td>2.1%</td><td>10.6%</td></tr><tr><td>YoY%</td><td>(2.6%)</td><td>26.5%</td><td>15.3%</td><td>(4.8%)</td><td>(24.3%)</td><td>10.8%</td><td>18.2%</td><td>12.5%</td><td>9.8%</td><td>7.2%</td><td>5.6%</td><td></td><td></td><td></td></tr><tr><td>Automation</td><td>$10</td><td>$13</td><td>$15</td><td>$15</td><td>$12</td><td>$13</td><td>$16</td><td>$18</td><td>$21</td><td>$23</td><td>$25</td><td>6.4%</td><td>4.6%</td><td>13.6%</td></tr><tr><td>YoY%</td><td>(3.0%)</td><td>29.5%</td><td>17.0%</td><td>(1.0%)</td><td>(15.0%)</td><td>5.6%</td><td>20.1%</td><td>16.6%</td><td>13.2%</td><td>10.1%</td><td>8.5%</td><td></td><td></td><td></td></tr><tr><td>Power/Energy</td><td>$6</td><td>$7</td><td>$9</td><td>$9</td><td>$8</td><td>$8</td><td>$9</td><td>$10</td><td>$11</td><td>$11</td><td>$12</td><td>6.8%</td><td>5.3%</td><td>7.8%</td></tr><tr><td>YoY%</td><td>(0.5%)</td><td>25.4%</td><td>22.0%</td><td>5.0%</td><td>(18.0%)</td><td>4.1%</td><td>13.5%</td><td>10.2%</td><td>6.2%</td><td>5.3%</td><td>4.1%</td><td></td><td></td><td></td></tr><tr><td>Consumer</td><td>$35</td><td>$48</td><td>$48</td><td>$30</td><td>$31</td><td>$33</td><td>$31</td><td>$31</td><td>$32</td><td>$33</td><td>$35</td><td>1.1%</td><td>(0.0%)</td><td>1.3%</td></tr><tr><td>YoY%</td><td>6.5%</td><td>37.5%</td><td>0.1%</td><td>(37.1%)</td><td>3.4%</td><td>4.7%</td><td>(6.9%)</td><td>(0.1%)</td><td>3.1%</td><td>6.3%</td><td>4.8%</td><td></td><td></td><td></td></tr><tr><td>TVs</td><td>$10</td><td>$14</td><td>$14</td><td>$11</td><td>$11</td><td>$11</td><td>$11</td><td>$12</td><td>$12</td><td>$12</td><td>$13</td><td>0.3%</td><td>2.8%</td><td>2.8%</td></tr><tr><td>YoY%</td><td>10.5%</td><td>37.1%</td><td>1.8%</td><td>(21.7%)</td><td>(4.0%)</td><td>2.1%</td><td>2.3%</td><td>2.8%</td><td>2.8%</td><td>3.0%</td><td>3.0%</td><td></td><td></td><td></td></tr><tr><td>Video console SoCs (Gaming)</td><td>$3</td><td>$6</td><td>$7</td><td>$7</td><td>$3</td><td>$3</td><td>$3</td><td>$3</td><td>$3</td><td>$4</td><td>$5</td><td>6.5%</td><td>14.5%</td><td>7.6%</td></tr><tr><td>YoY%</td><td>102.2%</td><td>89.9%</td><td>26.2%</td><td>(4.3%)</td><td>(57.1%)</td><td>13.0%</td><td>(20.2%)</td><td>(0.7%)</td><td>11.0%</td><td>39.2%</td><td>17.9%</td><td></td><td></td><td></td></tr><tr><td>Wired Communications</td><td>$18</td><td>$21</td><td>$20</td><td>$25</td><td>$33</td><td>$42</td><td>$54</td><td>$65</td><td>$73</td><td>$80</td><td>$85</td><td>9.8%</td><td>15.2%</td><td>15.2%</td></tr><tr><td>YoY%</td><td>1.0%</td><td>17.0%</td><td>(8.3%)</td><td>26.9%</td><td>32.8%</td><td>28.1%</td><td>29.3%</td><td>19.6%</td><td>12.2%</td><td>9.2%</td><td>6.9%</td><td></td><td></td><td></td></tr><tr><td>Ethernet/Network switch</td><td>$5</td><td>$5</td><td>$6</td><td>$9</td><td>$13</td><td>$17</td><td>$25</td><td>$31</td><td>$36</td><td>$40</td><td>$43</td><td>12.3%</td><td>22.6%</td><td>20.2%</td></tr><tr><td>YoY%</td><td>(3.8%)</td><td>11.9%</td><td>15.0%</td><td>45.0%</td><td>40.0%</td><td>35.0%</td><td>42.0%</td><td>28.0%</td><td>15.0%</td><td>11.0%</td><td>8.0%</td><td></td><td></td><td></td></tr><tr><td>Optical Equipment</td><td>$4</td><td>$5</td><td>$5</td><td>$6</td><td>$9</td><td>$12</td><td>$15</td><td>$19</td><td>$21</td><td>$24</td><td>$26</td><td>18.4%</td><td>20.5%</td><td>16.9%</td></tr><tr><td>YoY%</td><td>9.8%</td><td>11.8%</td><td>5.0%</td><td>30.0%</td><td>35.0%</td><td>35.0%</td><td>32.0%</td><td>20.0%</td><td>15.0%</td><td>11.0%</td><td>8.0%</td><td></td><td></td><td></td></tr></table>

Source: BofA Global Research, Mercury Research, Gartner, Omdia, SIA  
BofA GLOBAL RESEARCH

In 2026, we expect semis/core semis sales to grow +103%/+27% YoY. Memory is expected to be even stronger, now up nearly +298% YoY (after +81%/+29% YoY growth in CY24/25).

By device type, we see CY26 memory sales driven by both DRAM (+309% YoY) and NAND (+295% YoY).

Ex-memory, microprocessors (MPUs) strong (+33% YoY) on hyperscaler consumption modestly offset by weak PC units, and logic particularly strong (+39% YoY) on AI accelerator-related demand. We also model industrial-centric markets (MCUs, Analog) seeing recovery following inventory digestion throughout 2024 and 1H25. In CY26, we model other markets (discretes, optos, sensors) to generally return to healthy growths (+6% YoY) as well, particularly driven by data center-related optoelectronic demands.

Exhibit 4: We model memory, logic, microcomponents driving semiconductor growth
Summary of BofA Semis Forecast by device type

<table><tr><td>Revenue ($bn)</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>CAGR&#x27;15-25</td><td>CAGR&#x27;19-25</td><td>CAGR&#x27;25-30</td></tr><tr><td>Total Semis

[中间内容因长度限制已省略]

ns, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and

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
