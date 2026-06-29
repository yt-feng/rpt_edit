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
# Global Memory Tech

# Weekly theme: Micron results implications for Asian memory chipmakers

Industry Overview

## Five implications from Micron's results/guidance

We present five implications for Asian memory chipmakers following Micron's upbeat results/guidance: (1) super-cycle or chip shortage likely to continue into 2027 or even 2030; (2) more LTAs (long-term agreements) with big tech companies and OEMs, which could make the industry less cyclical and highly profitable (such as Taiwan's proven foundry); (3) not easy to build new shell fabs (high construction cost, local government regulation, power/water supply issues, etc.); (4) limited wafer capacity expansion even in 2028 (lots of clean rooms needed for old fab upgrades, longer manufacturing cycles, larger sized front-end and even back-end equipment, low yields in producing more advanced chips, high trade ratio for HBM vs conventional DRAM); and (5) significantly increasing FCF despite more-than-doubled capex spend vs normal cycle. Micron also pointed to meaningful HBM4 sales (US\$1bn so far); new fab construction / operations across the globe – the US (Boise; New York; Virginia), Taiwan (Tongluo), Singapore, and Japan; as well as large EUV orders. Our check also suggests that all major Asian memory chipmakers also agree on Micron's bullish memory industry views.

## Fine-tune global memory forecasts

We also reflect Micron's results (upbeat ASP for May'26-end quarter) and guidance (just \~20% revenue growth QoQ in Aug-end quarter vs +75%/+74% in Feb/May-end quarters) in our industry model. We believe ASP will no longer rise strongly if LTA-based sales increase. We also learned of stronger demand/production for HBM4, HBM4e, SOCAMM, LPDDR5, GDDR7, eSSD, etc. This could lead to higher bit growth in 2H26 and 2027 (but still sub-20% YoY, in our view). Overall, we tweak up our 2026-28 global DRAM/NAND sales forecasts by 2-4%, but the revisions are mostly based on upbeat 2Q26 ASP (offsetting muted 3Q or 2H ASP due to LTAs) and slightly higher volume increase for 2H26 and 2027-28. We also note Micron's revenue guidance (US\$50bn for Aug-end quarter; annual run rate US\$200bn; implied memory industry market size US\$1.0tn with Micron's 20%+/- market share) is consistent with our industry view (3Q global DRAM/NAND sales total US\$257bn; annual run rate also US\$1.0tn). Korea's semis exports (mostly memory) remained strong in June (+188% YoY for the first 20-day period). DRAM spot price has also risen for five consecutive weeks (up 20%) vs softened NAND (down 5%).

## Memory chipmakers unlikely to face severe price competition

Micron and other large memory chipmakers are increasingly using LTAs to fix ASPs; their chip production will also be more high-end centric (HBM, SOCAMM, LPDDR5). This could unlock new growth opportunities for memory chipmakers without severe price competition. We note, for example, that Nanya Tech's DRAM sales (mostly old/legacy DRAM) are still mainly based on monthly/quarterly negotiated ASPs (very low exposure to LTAs).

## 26 June 2026

Equity
Global
Technology

Simon Woo, CFA >> Research Analyst
BofA (Seoul)
+82 2 3707 0554
simon.woo@bofa.com

Dai Shen >>
Research Analyst
BofA (Hong Kong)
dai.shen@bofa.com

Vivek Arya
Research Analyst
BofAS
vivek.arya@bofa.com

Mikio Hirakawa >>
Research Analyst
BofAS Japan
mikio.hirakawa@bofa.com

Matt Shin >>
Research Analyst
BofA (Seoul)
matt.shin2@bofa.com

## Exhibit 1: Global memory forecasts – super-cycle should continue into 2027 even after quadrupling in 2026 BofA global memory forecasts

<table><tr><td>YoY</td><td>24</td><td>25</td><td>26E</td><td>27E</td></tr><tr><td>DRAM sales</td><td>86%</td><td>52%</td><td>316%</td><td>43%</td></tr><tr><td>NAND sales</td><td>84%</td><td>4%</td><td>295%</td><td>29%</td></tr><tr><td>DRAM ASP</td><td>62%</td><td>29%</td><td>242%</td><td>23%</td></tr><tr><td>NAND ASP</td><td>65%</td><td>-8%</td><td>234%</td><td>8%</td></tr><tr><td>DRAM bit</td><td>15%</td><td>18%</td><td>22%</td><td>17%</td></tr><tr><td>NAND bit</td><td>11%</td><td>13%</td><td>18%</td><td>20%</td></tr><tr><td>DRAM capex</td><td>49%</td><td>43%</td><td>65%</td><td>21%</td></tr><tr><td>NAND capex</td><td>4%</td><td>-5%</td><td>56%</td><td>16%</td></tr><tr><td>DRAM capa</td><td>7%</td><td>8%</td><td>11%</td><td>9%</td></tr><tr><td>NAND capa</td><td>-2%</td><td>-7%</td><td>5%</td><td>4%</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 2: DDR5 and DDR4 price up in June, while NAND prices softened
Spot-market prices among DRAM and NAND

<table><tr><td>US$</td><td>Current</td><td>WoW</td><td>QoQ</td><td>YoY</td></tr><tr><td colspan="5">DRAM spot</td></tr><tr><td>16Gb DDR5</td><td>46.7</td><td>2%</td><td>25%</td><td>672%</td></tr><tr><td>16Gb DDR4</td><td>71.6</td><td>4%</td><td>-4%</td><td>737%</td></tr><tr><td>8Gb DDR4</td><td>67.8</td><td>1%</td><td>-4%</td><td>721%</td></tr><tr><td colspan="5">NAND spot</td></tr><tr><td>1Tb wafer</td><td>24.5</td><td>-2%</td><td>-12%</td><td>383%</td></tr><tr><td>512Gb wafer</td><td>20.1</td><td>-2%</td><td>-12%</td><td>648%</td></tr><tr><td>256Gb wafer</td><td>10.2</td><td>-2%</td><td>-9%</td><td>581%</td></tr></table>

Source: DRAMeXchange

BofA GLOBAL RESEARCH

Korea semis exports – YoY in first 20 days of month

## Korea's exports and Micron's results

Exhibit 3: Strong MoM growth in Jun (US\$25.5bn; +16% MoM); more than 3x higher than 2025 year-average level
Korea semis exports (mostly memory) – first 20 days of month (US\$bn)  
![](images/a2ecb66cad4481f030e9addf5c016f35ceaeecfd255bd3717b79ccd4fc04cdd8.jpg)  
Source: MoTIR  
BofA GLOBAL RESEARCH  
Exhibit 5: Record-high sales in May-Q (US\$41bn; +346% YoY); mgmt also provided solid guidance for Aug-Q (US\$50bn), which implies +21% QoQ growth  
Micron – Sales and YoY growth trend

![](images/c419738f3e2fe0ac0a351f9bf0643c6a903953154c93affb887101cbb51f73ee.jpg)  
Source: Company, BofA Global Research estimates  
BofA GLOBAL RESEARCH  
Source: MoTIR  
BofA GLOBAL RESEARCH

Exhibit 4: Up 188% YoY in Jun; already five consecutive months of triple-digit growth  
![](images/824817b104a14adf07e70db1ebf66c750a35cf53c7285628cb634b1b3ade2682.jpg)

Exhibit 6: Significant margin enhancement in May-Q (GM 85%, OPM 81%); mgmt. expects high-margin profile to continue
Micron – Gross/OP margin trend  
![](images/d05dc3cf56377369227c846486d52c4501f4e3966ee89c8e7ef77f4af361022b.jpg)  
Source: Company, BofA Global Research estimates  
BofA GLOBAL RESEARCH  
Micron – DRAM and NAND ASP trend (QoQ basis)

Exhibit 7: Robust price hike observed in May-Q (DRAM up low-60% QoQ and NAND up mid-80%)

![](images/7cf677fc7271cc18f4d324a7d4035f3f14ae1e3588506eb05982d2dc7412b024.jpg)

Exhibit 8: Record-high margins in May-Q (DRAM 81%, NAND 78%) Micron – DRAM and NAND OP margin trend  
![](images/714d1461c3b463d9d9015990e494b204d44b10d3de5220bf9b2dda25585584dd.jpg)  
Source: Company, BofA Global Research estimates

## Global memory forecasts

Exhibit 9: We expect global DRAM revenue to nearly quadruple (+316% YoY) in 2026E, building on the strong growth trajectory of 86%/52% in 2024/25, primarily driven by a sharp \~3x rebound in ASPs (+242% YoY). NAND revenue is similarly forecast to increase nearly fourfold (+295% YoY) in 2026E, following modest low-single-digit growth in 2025, supported by a robust \~2.3x expansion in ASPs (+234% YoY).

Global memory forecast summary – top-down approach

<table><tr><td></td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="17">Revenue US$bn</td></tr><tr><td>DRAM</td><td>83.9</td><td>134.6</td><td>162.1</td><td>176.6</td><td>185.5</td><td>193.5</td><td>206.3</td><td>213.9</td><td>92.1</td><td>77.7</td><td>47.3</td><td>87.9</td><td>133.8</td><td>557.2</td><td>799.1</td><td>870.9</td></tr><tr><td>NAND</td><td>45.3</td><td>78.9</td><td>94.7</td><td>100.6</td><td>99.9</td><td>101.3</td><td>104.9</td><td>106.9</td><td>73.3</td><td>67.3</td><td>42.4</td><td>78.1</td><td>81.0</td><td>319.6</td><td>413.0</td><td>414.1</td></tr><tr><td>DRAM+NAND total</td><td>129.2</td><td>213.6</td><td>256.8</td><td>277.2</td><td>285.4</td><td>294.8</td><td>311.2</td><td>320.7</td><td>165.4</td><td>144.9</td><td>89.7</td><td>166.0</td><td>214.8</td><td>876.8</td><td>1,212.2</td><td>1,285.1</td></tr><tr><td colspan="17">% QoQ</td></tr><tr><td>DRAM</td><td>78%</td><td>60%</td><td>20%</td><td>9%</td><td>5%</td><td>4%</td><td>7%</td><td>4%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>NAND</td><td>71%</td><td>74%</td><td>20%</td><td>6%</td><td>-1%</td><td>1%</td><td>4%</td><td>2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DRAM/NAND total</td><td>75%</td><td>65%</td><td>20%</td><td>8%</td><td>3%</td><td>3%</td><td>6%</td><td>3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="17">% YoY</td></tr><tr><td>DRAM</td><td>258%</td><td>378%</td><td>362%</td><td>275%</td><td>121%</td><td>44%</td><td>27%</td><td>21%</td><td>41%</td><td>-16%</td><td>-39%</td><td>86%</td><td>52%</td><td>316%</td><td>43%</td><td>9%</td></tr><tr><td>NAND</td><td>196%</td><td>332%</td><td>352%</td><td>280%</td><td>121%</td><td>28%</td><td>11%</td><td>6%</td><td>25%</td><td>-8%</td><td>-37%</td><td>84%</td><td>4%</td><td>295%</td><td>29%</td><td>0%</td></tr><tr><td>DRAM/NAND total</td><td>234%</td><td>360%</td><td>359%</td><td>276%</td><td>121%</td><td>38%</td><td>21%</td><td>16%</td><td>34%</td><td>-12%</td><td>-38%</td><td>85%</td><td>29%</td><td>308%</td><td>38%</td><td>6%</td></tr><tr><td colspan="17">Blended ASP US$/unit</td></tr><tr><td>DRAM 8Gb equiv</td><td>8.1</td><td>12.4</td><td>14.4</td><td>15.5</td><td>15.8</td><td>15.8</td><td>15.6</td><td>15.3</td><td>3.8</td><td>3.2</td><td>1.8</td><td>2.9</td><td>3.7</td><td>12.7</td><td>15.6</td><td>14.4</td></tr><tr><td>NAND 256Gb equiv</td><td>5.0</td><td>8.3</td><td>9.4</td><td>9.5</td><td>9.3</td><td>9.0</td><td>8.6</td><td>8.3</td><td>3.4</td><td>3.0</td><td>1.6</td><td>2.6</td><td>2.4</td><td>8.1</td><td>8.8</td><td>7.6</td></tr><tr><td colspan="17">% QoQ</td></tr><tr><td>DRAM ASP</td><td>73%</td><td>53%</td><td>17%</td><td>7%</td><td>2%</td><td>0%</td><td>-2%</td><td>-2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>NAND ASP</td><td>75%</td><td>65%</td><td>13%</td><td>1%</td><td>-2%</td><td>-3%</td><td>-5%</td><td>-3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="17">% YoY</td></tr><tr><td>DRAM ASP</td><td>155%</td><td>283%</td><td>304%</td><td>231%</td><td>95%</td><td>28%</td><td>8%</td><td>-1%</td><td>14%</td><td>-16%</td><td>-45%</td><td>62%</td><td>29%</td><td>242%</td><td>23%</td><td>-8%</td></tr><tr><td>NAND ASP</td><td>115%</td><td>281%</td><td>306%</td><td>230%</td><td>86%</td><td>9%</td><td>-9%</td><td>-12%</td><td>-9%</td><td>-13%</td><td>-46%</td><td>65%</td><td>-8%</td><td>234%</td><td>8%</td><td>-13%</td></tr><tr><td colspan="17">Shipments bn units</td></tr><tr><td>DRAM 8Gb equiv</td><td>10.4</td><td>10.9</td><td>11.2</td><td>11.4</td><td>11.8</td><td>12.2</td><td>13.3</td><td>14.0</td><td>24.1</td><td>24.2</td><td>26.7</td><td>30.6</td><td>36.0</td><td>43.9</td><td>51.2</td><td>60.5</td></tr><tr><td>NAND 256Gb equiv</td><td>9.0</td><td>9.5</td><td>10.1</td><td>10.6</td><td>10.7</td><td>11.2</td><td>12.2</td><td>12.8</td><td>21.3</td><td>22.6</td><td>26.6</td><td>29.5</td><td>33.2</td><td>39.3</td><td>47.0</td><td>54.3</td></tr><tr><td colspan="17">% QoQ</td></tr><tr><td>DRAM bit growth</td><td>3%</td><td>5%</td><td>3%</td><td>2%</td><td>3%</td><td>4%</td><td>8%</td><td>5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>NAND bit growth</td><td>-2%</td><td>5%</td><td>6%</td><td>5%</td><td>1%</td><td>5%</td><td>9%</td><td>5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="17">% YoY</td></tr><tr><td>DRAM bit growth</td><td>41%</td><td>25%</td><td>14%</td><td>13%</td><td>13%</td><td>12%</td><td>18%</td><td>22%</td><td>23%</td><td>0%</td><td>10%</td><td>15%</td><td>18%</td><td>22%</td><td>17%</td><td>18%</td></tr><tr><td>NAND bit growth</td><td>38%</td><td>13%</td><td>11%</td><td>15%</td><td>19%</td><td>18%</td><td>21%</td><td>21%</td><td>38%</td><td>6%</td><td>18%</td><td>11%</td><td>13%</td><td>18%</td><td>20%</td><td>16%</td></tr><tr><td colspan="17">Capacity 300mm k wpm</td></tr><tr><td>DRAM wafer capacity</td><td>1,988</td><td>2,036</td><td>2,091</td><td>2,150</td><td>2,182</td><td>2,224</td><td>2,264</td><td>2,299</td><td>1,481</td><td>1,561</td><td>1,628</td><td>1,734</td><td>1,867</td><td>2,066</td><td>2,242</td><td>2,379</td></tr><tr><td>NAND wafer capacity</td><td>1,695</td><td>1,722</td><td>1,736</td><td>1,750</td><td>1,767</td><td>1,784</td><td>1,801</td><td>1,834</td><td>1,681</td><td>1,783</td><td>1,820</td><td>1,781</td><td>1,651</td><td>1,726</td><td>1,797</td><td>1,878</td></tr><tr><td>DRAM+NAND total</td><td>3,683</td><td>3,758</td><td>3,827</td><td>3,900</td><td>3,949</td><td>4,008</td><td>4,065</td><td>4,133</td><td>3,162</td><td>3,344</td><td>3,447</td><td>3,515</td><td>3,517</td><td>3,792</td><td>4,039</td><td>4,256</td></tr><tr><td colspan="17">% QoQ</td></tr><tr><td>DRAM capacity total</td><td>3%</td><td>2%</td><td>3%</td><td>3%</td><td>1%</td><td>2%</td><td>2%</td><td>2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>NAND capacity total</td><td>1%</td><td>2%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DRAM/NAND total</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td><td>1%</td><td>1%</td><td>1%</td><td>2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="17">% YoY</td></tr><tr><td>DRAM capacity</td><td>9%</td><td>11%</td><td>12%</td><td>11%</td><td>10%</td><td>9%</td><td>8%</td><td>7%</td><td>8%</td><td>5%</td><td>4%</td><td>7%</td><td>8%</td><td>11%</td><td>9%</td><td>6%</td></tr><tr><td>NAND capacity</td><td>2%</td><td>6%</td><td>6%</td><td>4%</td><td>4%</td><td>4%</td><td>4%</td><td>5%</td><td>1%</td><td>6%</td><td>2%</td><td>-2%</td><td>-7%</td><td>5%</td><td>4%</td><td>5%</td></tr><tr><td>DRAM+NAND total</td><td>5%</td><td>9%</td><td>9%</td><td>8%</td><td>7%</td><td>7%</td><td>6%</td><td>6%</td><td>4%</td><td>6%</td><td>3%</td><td>2%</td><td>0%</td><td>8%</td><td>7%</td><td>5%</td></tr><tr><td colspan="17">Capex spending</td></tr><tr><td>DRAM</td><td>23.2</td><td>22.3</td><td>21.4</td><td>22.3</td><td>24.8</td><td>25.9</td><td>28.0</td><td>29.1</td><td>27.1</td><td>31.0</td><td>25.2</td><td>37.7</td><td>53.9</td><td>89.1</td><td>107.9</td><td>112.3</td></tr><tr><td>NAND</td><td>6.9</td><td>7.2</td><td>7.5</td><td>8.4</td><td>9.1</td><td>8.7</td><td>8.4</td><td>8.7</td><td>27.9</td><td>29.0</td><td>19.7</td><td>20.4</td><td>19.3</td><td>30.1</td><td>34.8</td><td>36.3</td></tr><tr><td>Total (DRAM+NAND)</td><td>30.1</td><td>29.5</td><td>28.9</td><td>30.7</td><td>33.9</td><td>34.6</td><td>36.4</td><td>37.8</td><td>55.0</td><td>60.0</td><td>45.0</td><td>58.2</td><td>73.2</td><td>119.2</td><td>142.7</td><td>148.6</td></tr><tr><td colspan="17">QoQ/YoY in capex</td></tr><tr><td>DRAM</td><td>59%</td><td>-4%</td><td>-4%</td><td>4%</td><td>11%</td><td>4%</td><td>8%</td><td>4%</td><td>27%</td><td>14%</td><td>-19%</td><td>49%</td><td>43%</td><td>65%</td><td>21%</td><td>4%</td></tr><tr><td>NAND</td><td>28%</td><td>4%</td><td>4%</td><td>12%</td><td>7%</td><td>-4%</td><td>-4%</td><td>4%</td><td>24%</td><td>4%</td><td>-32%</td><td>4%</td><td>-5%</td><td>56%</td><td>16%</td><td>4%</td></tr><tr><td>Total (DRAM+NAND)</td><td>51%</td><td>-2%</td><td>-2%</td><td>6%</td><td>10%</td><td>2%</td><td>5%</td><td>4%</td><td>25%</td><td>9%</td><td>-25%</td><td>29%</td><td>26%</td><td>63%</td><td>20%</td><td>4%</td></tr></table>

Source: Companies' reports, BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 10: We slightly raise our 2026–28 DRAM revenue forecasts by 2–4%, primarily reflecting higher ASP assumptions (at \~\$13/\$16/\$14 per 8Gb equivalent in 2026/27/28). NAND revenue estimates are also increased by 4% for 2027–28, driven by stronger ASP expectations (\~\$8–9 per 256Gb equivalent) amid the recent pricing upcycle.
Global memory forecast revisions – top-down analysis

<table><tr><td></td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="17">DRAM (8Gb equiv)</td></tr><tr><td colspan="17">Sales (US$bn)</td></tr><tr><td>New</td><td>83.9</td><td>134.6</td><td>162.1</td><td>176.6</td><td>185.5</td><td>193.5</td><td>206.3</td><td>213.9</td><td>92.1</td><td>77.7</td><td>47.3</td><td>87.9</td><td>133.8</td><td>557.2</td><td>799.1</td><td>870.9</td></tr><tr><td>Old</td><td>83.9</td><td>128.9</td><td>159.2</td><td>175.0</td><td>180.3</td><td>188.1</td><td>201.7</td><td>209.1</td><td>92.1</td><td>77.7</td><td>47.3</td><td>87.9</td><td>133.8</td><td>547.0</td><td>779.1</td><td>838.0</td></tr><tr><td>Diff</td><td>nm</td><td>4.4%</td><td>1.8%</td><td>0.9%</td><td>2.9%</td><td>2.9%</td><td>2.3%</td><td>2.3%</td><td>nm</td><td>nm</td><td>nm</td><td>nm</td><td>nm</td><td>1.9%</td><td>2.6%</td><td>3.9%</td></tr><tr><td colspan="17">Shipments (bn units)</td></tr><tr><td>New</td><td>10.4</td><td>10.9</td><td>11.2</td><td>11.4</td><td>11.8</td><td>12.2</td><td>13.3</td><td>14.0</td><td>24.1</td><td>24.2</td><td>26.7</td><td>30.6</td><td>36.0</td><td>43.9</td><td>51.2</td><td>60.5</td></tr><tr><td>Old</td><td>10.4</td><td>11.0</td><td>11.3</td><td>11.5</td><td>11.7</td><td>12.1</td><td>13.1</td><td>13.8</td><td>24.1</td><td>24.2</td><td>26.7</td><td>30.6</td><td>36.0</td><td>44.3</td><td>50.8</td><td>58.8</td></tr><tr><td>Diff</td><td>nm</td><td>-1.0%</td><td>-1.0%</td><td>-1.0%</td><td>0.9%</td><td>0.9%</td><td>0.9%</td><td>0.9%</td><td>nm</td><td>nm</td><td>nm</td><td>nm</td><td>nm</td><td>-0.8%</td><td>0.9%</td><td>2.9%</td></tr><tr><td colspan="17">Bit growth - sequential</td></tr><tr><td>New</td><td>2.8%</td><td>5.0%</td><td>3.0%</td><td>1.8%</td><td>3.0%</td><td>4.1%</td><td>8.3%</td><td>5.3%</td><td>23.3%</td><td>0.3%</td><td>10.3%</td><td>14.8%</td><td>17.6%</td><td>21.9%</td><td>16.7%</

[中间内容因长度限制已省略]

h information is distributed simultaneously to internal and client websites and other portals by BofA and is not publicly-available material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
