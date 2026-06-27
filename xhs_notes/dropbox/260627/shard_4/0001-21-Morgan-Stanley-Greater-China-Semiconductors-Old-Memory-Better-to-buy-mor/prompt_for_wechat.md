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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
<table><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Daniel Yen, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daniel.Yen@morganstanley.com</td><td>+886 2 2730-2863</td></tr><tr><td colspan="2">Charlie Chan</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Charlie.Chan@morganstanley.com</td><td>+886 2 2730-1725</td></tr><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Daisy Dai, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daisy.Dai@morganstanley.com</td><td>+852 2848-7310</td></tr><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Tiffany Yeh</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Tiffany.Yeh@morganstanley.com</td><td>+886 2 7712-3032</td></tr><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Ethan Jia</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ethan.Jia@morganstanley.com</td><td>+852 3963-2287</td></tr></table>

# Greater China Semiconductors | Asia Pacific

# Old Memory: Better to buy more

Unexpected persistent tightness in legacy memory supply is driving panicked purchasing by multiple enterprise customers. We reiterate our bullish view and raise PTs across our coverage.

## Key Takeaways

DDR4 buyers may build even larger demand buffers amid prolonged supply tightness.

\- MLC NAND shortages are forcing enterprise HDDs to use SLC NAND, indicating stronger demand.

■ NOR supply is increasingly concentrated among Taiwan vendors, given reduced output from the US.

DDR4 stronger orders from enterprise customers: We upgraded both Nanya Tech and Winbond back to OW on May 28 (link), given the ongoing tightness in DDR4. We now see enterprise customers securing supply as early as possible amid fears of shortages. Channel inventory remains low at under two weeks. This points to further DDR4 price increases into 4Q, following the double-digit monthly uptrend.

SLC NAND likely to see stronger demand from HDD: We noted that high-density SLC NAND can support datacenter eSSD (link). In addition, given the MLC NAND shortfall, enterprise HDDs are likely shifting to high-density SLC NAND. Enterprise HDDs previously used MLC NAND for firmware, hot data, and defect mapping. This shift reinforces continued pricing momentum into 4Q, following the 50–60% increase in 3Q.

NOR flash pricing increase led by Macronix, with potential supply–demand widening: We continue to see strong pricing increases from Macronix, driven by a shift toward NAND from NOR. We also see Micron reducing NOR supply into 2H, likely reallocating capacity to DRAM and NAND. At the same time, Vera Rubin rack ramp-up in 2H will require 50%+ higher NOR content versus Grace Blackwell racks. We therefore expect NOR pricing to rise 30–40% in 3Q and continue into 4Q.

Stock implications – we raise our earnings and PTs across the board: Winbond: PT raised to NT\$288; 2026/27/28 EPS raised by 4%/17%/24%. Nanya Tech: PT raised to NT\$550; 2026/27/28 EPS raised by 7%/15%/14%. Macronix: PT raised to NT\$220; 2026/27/28 EPS raised by 34%/20%/21%. GigaDevice: PT raised to Rmb888; 2026/27/28 EPS raised by 30%/46%/53%. PSMC: PT raised to NT\$111; 2026/27/28 EPS raised by 4%/48%/62%.

Asia Summer School 2026

![](images/5bb30979e855040da9495a1e96575dccd355e0a32083e7cb9930910fb530669f.jpg)

<table><tr><td colspan="3">GREATER CHINA TECHNOLOGY SEMICONDUCTORS</td></tr><tr><td>Asia Pacific Industry View</td><td colspan="2">Attractive</td></tr><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)Price Target</td><td>FromRmb585.00</td><td>ToRmb888.00</td></tr><tr><td>Winbond Electronics Corp(2344.TW)Price Target</td><td>FromNT$222.00</td><td>ToNT$288.00</td></tr><tr><td>Nanya Technology Corp.(2408.TW)Price Target</td><td>FromNT$380.00</td><td>ToNT$550.00</td></tr><tr><td>Macronix International Co Ltd(2337.TW)Price Target</td><td>FromNT$202.00</td><td>ToNT$220.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)Price Target</td><td>FromNT$88.00</td><td>ToNT$111.00</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Key Charts and Exhibits

Exhibit 1: Order of preference: GC memory

<table><tr><td></td><td>Macronix2337.TW</td><td>Winbond2344.TW</td><td>AP Memory6531.TW</td><td>PSMC6770.TW</td><td>GigaDevice603986.SS</td><td>Nanya Tech2408.TW</td></tr><tr><td>Rating</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td></tr><tr><td>Trading Currency</td><td>TWD</td><td>TWD</td><td>TWD</td><td>TWD</td><td>CNY</td><td>TWD</td></tr><tr><td>Price Target</td><td>220.0</td><td>288.0</td><td>1,555.0</td><td>111.0</td><td>888.0</td><td>550.0</td></tr><tr><td>Current Price (as of 2026/6/24)</td><td>172.0</td><td>205.0</td><td>1,115.0</td><td>85.7</td><td>705.1</td><td>443.5</td></tr><tr><td>Upside/(Downside) (%)</td><td>28%</td><td>40%</td><td>39%</td><td>30%</td><td>26%</td><td>24%</td></tr><tr><td>Market Cap (in USD mm)</td><td>9,780.7</td><td>26,999.2</td><td>5,685.1</td><td>11,308.3</td><td>69,101.7</td><td>43,068.6</td></tr><tr><td>Avg Daily Traded Vol (in USD mm)</td><td>264.9</td><td>478.6</td><td>79.2</td><td>256.3</td><td>1,346.6</td><td>647.1</td></tr><tr><td colspan="7">Street View: Ratings</td></tr><tr><td>Buy/Overweight</td><td>90%</td><td>100%</td><td>75%</td><td>67%</td><td>94%</td><td>86%</td></tr><tr><td>Hold/Equal-weight</td><td>0%</td><td>0%</td><td>25%</td><td>33%</td><td>6%</td><td>14%</td></tr><tr><td>Sell/Underweight</td><td>10%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Bull Case Value</td><td>355.0</td><td>342.0</td><td>1,830.0</td><td>177.0</td><td>1,542.0</td><td>1,160.0</td></tr><tr><td>Upside (%)</td><td>106%</td><td>67%</td><td>64%</td><td>107%</td><td>119%</td><td>162%</td></tr><tr><td>Bear Case Value</td><td>130.0</td><td>118.0</td><td>620.0</td><td>55.0</td><td>648.0</td><td>305.0</td></tr><tr><td>Downside (%)</td><td>-24%</td><td>-42%</td><td>-44%</td><td>-36%</td><td>-8%</td><td>-31%</td></tr><tr><td>Risk/Reward Skew</td><td>4.4</td><td>1.6</td><td>1.4</td><td>3.0</td><td>14.7</td><td>5.2</td></tr><tr><td colspan="7">MS Estimates</td></tr><tr><td>FY26e</td><td>TWD</td><td>TWD</td><td>TWD</td><td>TWD</td><td>CNY</td><td>TWD</td></tr><tr><td>Sales</td><td>77,854</td><td>269,908</td><td>9,601</td><td>75,820</td><td>28,399</td><td>349,737</td></tr><tr><td>EBITDA</td><td>30,271</td><td>134,605</td><td>3,037</td><td>13,926</td><td>13,300</td><td>270,152</td></tr><tr><td>EBIT</td><td>22,733</td><td>118,994</td><td>2,976</td><td>6,362</td><td>13,050</td><td>257,966</td></tr><tr><td>EPS</td><td>9.84</td><td>21.27</td><td>17.65</td><td>4.80</td><td>16.68</td><td>65.56</td></tr><tr><td colspan="7">FY27e</td></tr><tr><td>Sales</td><td>143,216</td><td>432,740</td><td>17,829</td><td>102,954</td><td>46,298</td><td>524,965</td></tr><tr><td>EBITDA</td><td>64,657</td><td>234,811</td><td>6,491</td><td>38,229</td><td>23,646</td><td>391,551</td></tr><tr><td>EBIT</td><td>58,187</td><td>214,635</td><td>6,429</td><td>30,764</td><td>23,396</td><td>368,367</td></tr><tr><td>EPS</td><td>25.02</td><td>38.29</td><td>34.34</td><td>5.61</td><td>30.27</td><td>93.08</td></tr><tr><td colspan="7">FY26 MSe vs. Consensus Mean</td></tr><tr><td>Sales</td><td>-2.5%</td><td>9.2%</td><td>-3.0%</td><td>10.7%</td><td>56.8%</td><td>16.4%</td></tr><tr><td>EBITDA</td><td>-4.5%</td><td>-2.1%</td><td>-0.9%</td><td>-52.9%</td><td>77.7%</td><td>18.4%</td></tr><tr><td>EBIT</td><td>-20.7%</td><td>7.4%</td><td>3.8%</td><td>-74.4%</td><td>82.1%</td><td>19.8%</td></tr><tr><td>EPS</td><td>-26.0%</td><td>-0.1%</td><td>1.1%</td><td>-10.3%</td><td>88.0%</td><td>24.1%</td></tr><tr><td colspan="7">FY27 MSe vs. Consensus Mean</td></tr><tr><td>Sales</td><td>21.4%</td><td>25.7%</td><td>19.6%</td><td>20.7%</td><td>95.4%</td><td>26.7%</td></tr><tr><td>EBITDA</td><td>-4.5%</td><td>8.8%</td><td>26.0%</td><td>16.2%</td><td>148.3%</td><td>26.7%</td></tr><tr><td>EBIT</td><td>4.2%</td><td>34.2%</td><td>33.0%</td><td>30.6%</td><td>147.0%</td><td>25.8%</td></tr><tr><td>EPS</td><td>-9.7%</td><td>20.3%</td><td>27.0%</td><td>23.0%</td><td>167.2%</td><td>32.0%</td></tr><tr><td colspan="7">Valuation Multiples at Last Close</td></tr><tr><td colspan="7">FY26e</td></tr><tr><td>P/E</td><td>17.5x</td><td>9.6x</td><td>63.2x</td><td>17.8x</td><td>42.3x</td><td>6.8x</td></tr><tr><td>EV/EBIT</td><td>19.6x</td><td>10.3x</td><td>80.6x</td><td>44.1x</td><td>44.0x</td><td>7.4x</td></tr><tr><td>EV/EBITDA</td><td>11.9x</td><td>6.5x</td><td>53.5x</td><td>16.1x</td><td>34.0x</td><td>5.8x</td></tr><tr><td>EV/Sales</td><td>4.6x</td><td>3.2x</td><td>16.9x</td><td>3.0x</td><td>15.9x</td><td>4.5x</td></tr><tr><td>FCF Yield</td><td>-11.9%</td><td>2.9%</td><td>1.2%</td><td>28.6%</td><td>2.0%</td><td>-18.1%</td></tr><tr><td colspan="7">FY27e</td></tr><tr><td>P/E</td><td>6.9x</td><td>5.4x</td><td>32.5x</td><td>15.3x</td><td>23.3x</td><td>4.8x</td></tr><tr><td>EV/EBIT</td><td>5.3x</td><td>3.3x</td><td>24.9x</td><td>5.6x</td><td>18.7x</td><td>3.6x</td></tr><tr><td>EV/EBITDA</td><td>4.8x</td><td>3.0x</td><td>24.7x</td><td>4.5x</td><td>18.5x</td><td>3.3x</td></tr><tr><td>EV/Sales</td><td>2.2x</td><td>1.6x</td><td>9.0x</td><td>1.7x</td><td>9.5x</td><td>2.5x</td></tr><tr><td>FCF Yield</td><td>17.5%</td><td>18.9%</td><td>2.2%</td><td>16.2%</td><td>3.9%</td><td>19.3%</td></tr><tr><td colspan="7">Implied Multiples on MS Price Target</td></tr><tr><td colspan="7">FY26e</td></tr><tr><td>P/E</td><td>22.4x</td><td>13.5x</td><td>88.1x</td><td>23.1x</td><td>53.2x</td><td>8.4x</td></tr><tr><td>EV/EBIT</td><td>19.6x</td><td>10.3x</td><td>80.6x</td><td>44.1x</td><td>44.0x</td><td>7.4x</td></tr><tr><td>EV/EBITDA</td><td>14.8x</td><td>9.1x</td><td>79.0x</td><td>20.1x</td><td>43.2x</td><td>7.0x</td></tr><tr><td>EV/Sales</td><td>5.7x</td><td>4.5x</td><td>25.0x</td><td>3.7x</td><td>20.2x</td><td>5.4x</td></tr><tr><td colspan="7">FY27e</td></tr><tr><td>P/E</td><td>8.8x</td><td>7.5x</td><td>45.3x</td><td>19.8x</td><td>29.3x</td><td>5.9x</td></tr><tr><td>EV/EBIT</td><td>7.0x</td><td>5.7x</td><td>40.0x</td><td>15.5x</td><td>28.3x</td><td>4.7x</td></tr><tr><td>EV/EBITDA</td><td>6.3x</td><td>5.2x</td><td>39.7x</td><td>12.5x</td><td>28.0x</td><td>4.4x</td></tr><tr><td>EV/Sales</td><td>2.8x</td><td>2.8x</td><td>14.4x</td><td>4.6x</td><td>14.3x</td><td>3.3x</td></tr></table>

Source: FactSet (consensus mean), MS (e) estimates.

Exhibit 2: NOR flash demand and supply growth rates  
![](images/36816b8a68b7dc027ae480e837448ad4f9afc8b1269aaa9bb68b3e3869f94a5c.jpg)  
Source: Company data, MS

Exhibit 3: NOR flash demand growth and supply growth by  
![](images/f37b20bc0b0d1cdc2e7657703661d401761e155833ce6ae1c5765e69b2a3e3e2.jpg)  
Source: Company data, MS

Exhibit 4: DDR4 quarterly supply and demand summary  
![](images/7dee2e67aa9700c4de4cfe1bf3f5aef198927558ee5f5da7f926a26be6418fd4.jpg)  
Source: Company data, IDC, MS (e) estimates

Exhibit 5: Quarterly oversupply/undersupply ratio vs. Nanya and Winbond pricing Q/Q change  
![](images/4c2bee4af3aaa82ece808fd444ebea07523d6b700f18563bc0af16a5f937d5c6.jpg)  
Source: Company data, IDC, MS (e) estimates

Exhibit 6: Quarterly supply breakdown (mn Gb)  
![](images/c240f2a5fec2f22a217485b0546feb46f8e3fef8e47939ead12fb8f55ffca0c0.jpg)  
Source: Company data, MS (e) estimates

Exhibit 7: Quarterly demand breakdown by product (mn Gb)  
![](images/01841940c59d45e7d7360fdef1f61c2bf10054194b1d2dca36ba7ad5f327fdff.jpg)  
Source: IDC, MS (e) estimates

Exhibit 8: DDR4 8Gb (1Gx8) pricing chart  
![](images/203cdb1ac2f6d7513df34ae4f7deb596145cacb494edfcd6d2b98ca605add582.jpg)  
Source: DRAMeXchange, MS. Data as of Jun 2026.

Exhibit 9: DDR5 16Gb (2Gx8) pricing chart  
![](images/767083085d554ca5c013c01be5c10354cce69b3df150def79589659bc7fb06f6.jpg)  
Source: DRAMeXchange, MS. Data as of Jun 2026.

# Winbond: Estimate Revisions and Quarterly Financials

We raise our 2026/27/28 EPS estimates by 4%/17%/24% respectively. This reflects stronger than previously expected memory pricing strength across DDR4, NOR flash, and SLC NAND. We now expect DDR4 pricing to rise further into 4Q, post the double digit monthly pricing uptrend. SLC NAND pricing uptrend is highly likely to continue into 4Q, post 50-60% hike in 3Q. NOR pricing could be hiked by 30-40% in 3Q and even into 4Q.

Exhibit 10: Winbond: Estimate revisions

<table><tr><td>NT$ mn</td><td>New &#x27;26E</td><td>Old &#x27;26E</td><td>Diff.</td><td>New &#x27;27E</td><td>Old &#x27;27E</td><td>Diff.</td><td>New &#x27;28E</td><td>Old &#x27;28E</td><td>Diff.</td></tr><tr><td>Net sales</td><td>269,908</td><td>258,581</td><td>4%</td><td>432,740</td><td>377,335</td><td>15%</td><td>493,598</td><td>410,515</td><td>20%</td></tr><tr><td>COGS</td><td>(117,684)</td><td>(111,702)</td><td></td><td>(182,017)</td><td>(158,768)</td><td></td><td>(211,407)</td><td>(178,012)</td><td></td></tr><tr><td>Gross profit</td><td>152,224</td><td>146,879</td><td>4%</td><td>250,723</td><td>218,567</td><td>15%</td><td>282,192</td><td>232,503</td><td>21%</td></tr><tr><td>Operating expenses</td><td>(33,230)</td><td>(33,028)</td><td></td><td>(36,088)</td><td>(35,211)</td><td></td><td>(37,465)</td><td>(36,149)</td><td></td></tr><tr><td>Operating profit</td><td>118,994</td><td>113,852</td><td>5%</td><td>214,635</td><td>183,356</td><td>17%</td><td>244,727</td><td>196,354</td><td>25%</td></tr><tr><td>Non-op. income (exp)</td><td>715</td><td>715</td><td></td><td>776</td><td>776</td><td></td><td>756</td><td>756</td><td></td></tr><tr><td>Pretax Income</td><td>119,709</td><td>114,567</td><td>4%</td><td>215,411</td><td>184,133</td><td>17%</td><td>245,483</td><td>197,111</td><td>25%</td></tr><tr><td>Taxes</td><td>(23,975)</td><td>(22,946)</td><td></td><td>(43,082)</td><td>(36,827)</td><td></td><td>(50,284)</td><td>(40,609)</td><td></td></tr><tr><td>Net income</td><td>95,721</td><td>91,607</td><td>4%</td><td>172,315</td><td>147,293</td><td>17%</td><td>195,186</td><td>156,488</td><td>25%</td></tr><tr><td>Reported EPS</td><td>21.27</td><td>20.36</td><td>4%</td><td>38.29</td><td>32.73</td><td>17%</td><td>44.69</td><td>36.09</td><td>24%</td></tr><tr><td colspan="10">Margins</td></tr><tr><td>Gross margin</td><td>56.4%</td><td>56.8%</td><td>-0.4 ppt</td><td>57.9%</td><td>57.9%</td><td>0.0 ppt</td><td>57.2%</td><td>56.6%</td><td>0.5 ppt</td></tr><tr><td>Operating margin</td><td>44.1%</td><td>44.0%</td><td>0.1 ppt</td><td>49.6%</td><td>48.6%</td><td>1.0 ppt</td><td>49.6%</td><td>47.8%</td><td>1.7 ppt</td></tr><tr><td>Pretax margin</td><td>44.4%</td><td>44.3%</td><td>0.0 ppt</td><td>49.8%</td><td>48.8%</td><td>1.0 ppt</td><td>49.7%</td><td>48.0%</td><td>1.7 ppt</td></tr><tr><td>Net margin</td><td>35.5%</td><td>35.4%</td><td>0.0 ppt</td><td>39.8%</td><td>39.0%</td><td>0.8 ppt</td><td>39.5%</td><td>38.1%</td><td>1.4 ppt</td></tr><tr><td>Opex %</td><td>12.3%</td><td>12.8%</td><td>-0.5 ppt</td><td>8.3%</td><td>9.3%</td><td>-1.0 ppt</td><td>7.6%</td><td>8.8%</td><td>-1.2 ppt</td></tr></table>

<table><tr><td>NT$</td><td>New &#x27;26E</td><td>Old &#x27;26E</td><td>Diff.</td><td>New &#x27;27E</td><td>Old &#x27;27E</td><td>Diff.</td><td>New &#x27;28E</td><td>Old &#x27;28E</td><td>Diff.</td></tr><tr><td>BVPS</td><td>46.68</td><td>40.54</td><td>15%</td><td>85.02</td><td>73.32</td><td>16%</td><td>129.77</td><td>82.20</td><td>58%</td></tr></table>

Source: MS (E) estimates

Exhibit 11: Winbond: Quarterly financials

<table><tr><td>NT$ in million</td><td>4Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>1Q28E</td><td>2Q28E</td><td>3Q28E</td><td>4Q28E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Total Revenues</td><td>19,993</td><td>21,018</td><td>21,771</td><td>26,625</td><td>38,253</td><td>57,075</td><td>77,583</td><td>96,997</td><td>#######</td><td>#######</td><td>#######</td><td>#######</td><td>#######</td><td>#######</td><td>#######</td><td>#######</td><td>89,406</td><td>269,908</td><td>432,740</td><td>493,598</td></tr><tr><td>Sequential Change</td><td>7.0%</td><td>5.1%</td><td>3.6%</td><td>2.3%</td><td>25.9%</td><td>49.2%</td><td>43.7%</td><td>49.2%</td><td>5.6%</td><td>5.0%</td><td>2.4%</td><td>2.5%</td><td>5.5%</td><td>5.5%</td><td>5.5%</td><td>5.5%</td><td></td><td></td><td></td><td></td></tr><tr><td>Change vs Year Ago</td><td>-0.6%</td><td>-2.2%</td><td>2.1%</td><td>42.4%</td><td>91.3%</td><td>171.6%</td><td>256.4%</td><td>264.3%</td><td>164.0%</td><td>84.3%</td><td>42.0%</td><td>20.0%</td><td>18.7%</td><td>16.7%</td><td>13.1%</td><td>8.6%</td><td>9.6%</td><td>201.9%</td><td>60.3%</td><td>14.1%</td></tr><tr><td>Cost of Sales</td><td>(14,871)</td><td>(16,255)</td><td>(11,605)</td><td>(15,479)</td><td>(17,838)</td><td>(25,385)</td><td>(33,251)</td><td>(41,211)</td><td>(42,310)</td><td>(44,062)</td><td>(46,471)</td><td>(49,174)</td><td>(49,360)</td><td>(50,707)</td><td>(52,108)</td><td>(53,297)</td><td>(58,210)</td><td>(117,664)</td><td>(182,017)</td><td>(211,407)</td></tr><tr><td>Percent of Revenues</td><td>74.4%</td><td>77.3%</td><td>53.3%</td><td>58.1%</td><td>46.6%</td><td>44.5%</td><td>42.9%</td><td>42.5%</td><td>41.9%</td><td>41.9%</td><td>42.2%</td><td>42.3%</td><td>41.2%</td><td>41.3%</td><td>41.8%</td><td>42.2%</td><td>65.1%</td><td>43.6%</td><td>42.1%</td><td>42.8%</td></tr><tr><td>Gross Margin</td><td>5,122</td><td>4,763</td><td>10,166</td><td>11,146</td><td>20,415</td><td>31,690</td><td>44,332</td><td>55,787</td><td>58,685</td><td>61,132</td><td>63,694</td><td>67,212</td><td>70,526</td><td>72,011</td><td>72,454</td><td>73,142</td><td>31,196</td><td>152,224</td><td>250,7

[中间内容因长度限制已省略]

deng Precision (3680.TWO)</td><td>O (11/25/2025)</td><td>NT$505.00</td></tr><tr><td>Hua Hong Semiconductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$192.80</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$793.00</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$334.50</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb111.32</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$4,310.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb770.52</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$477.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb798.00</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb89.71</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,475.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb138.28</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$615.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$86.00</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,390.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$178.50</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$220.00</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$463.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$204.80</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb84.72</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$180.00</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb110.10</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb49.86</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$67.20</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb104.17</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$28.24</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb172.28</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb138.22</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb87.50</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb36.19</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb137.45</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$1,100.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,435.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$17,425.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$124.50</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb124.23</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb775.21</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$161.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$459.00</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb279.16</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$561.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$177.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$658.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$83.20</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$814.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb59.81</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$219.50</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$107.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$217.50</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb179.45</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb677.30</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,105.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$629.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$15.73</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,920.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,905.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$321.66</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,100.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
