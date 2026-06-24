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
June 22, 2026 04:34 AM GMT

Investor Presentation | Japan

# Electronic Chemicals: Tech Monthly June 2026

MS MUFG SECURITIES CO., LTD.+
Ryoichi Watanabe
Equity Analyst
Ryoichi.Watanabe@morganstanleymufg.com +81 3 6836-8929

Takato Watabe
Equity Analyst
Takato.Watabe@morganstanleymufg.com +81 3 6836-5436

Kayoko Shoji
Research Associate
Kayoko.Shoji@morganstanleymufg.com +81 3 6836-5437

Kano Fujita
Research Associate
Kano.Fujita@morganstanleymufg.com +81 3 6836-8932

![](images/cc132900dda2e47b5861f8dde18cf4bc20ddde147b7d1f74d6561f5ee68cd446.jpg)

ELECTRONIC CHEMICALS

Japan
Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Key points for Electronic Chemicals

## Electronic Chemicals: Industry view In-Line

## Resonac > Sumitomo Bakelite > Tokyo Ohka Kogyo

• We think Resonac is likely to embark on capacity adds and further price hikes for CCLs.

\- Sumitomo Bakelite's business is strong at present; sales of granular encapsulants to Intel are increasing, and sample supplies of liquid encapsulants to TSMC and OSACs are starting up.

Tokyo Ohka Kogyo's lower growth rate than JSR may reflect lower MOR capacity.

## Key points regarding materials

• Very strong performance for FC-BGA CCLs.

• Semiconductor sealant materials doing well in Taiwan market.

• The China market is driving photoresists.

## Stock prices and valuations

<table><tr><td colspan="25">as of 2026/06/19Electronic ChemicalsIndustry View: In-Line</td><td></td></tr><tr><td rowspan="2"></td><td rowspan="2">Current Price(Y)</td><td rowspan="2">Market Cap (JPY bn)</td><td rowspan="2">Rating</td><td rowspan="2">Price Target(Y)</td><td rowspan="2">Potential return (%)</td><td colspan="4">P/E(x)</td><td colspan="4">P/B(x)</td><td colspan="4">Div. Yield (%)</td><td colspan="4">EV/EBITDA (x)</td><td colspan="4">ROE(%)</td></tr><tr><td>25</td><td>26e</td><td>27e</td><td>28e</td><td>25</td><td>26e</td><td>27e</td><td>28e</td><td>25</td><td>26e</td><td>27e</td><td>28e</td><td>25</td><td>26e</td><td>27e</td><td>28e</td><td>25</td><td>26e</td><td>27e</td><td>28e</td></tr><tr><td rowspan="2">4004 Resonac Holdings (New)(Diluted)</td><td rowspan="2">18,390</td><td rowspan="2">3,400</td><td rowspan="2">OW</td><td rowspan="2">22,400</td><td rowspan="2">21.8</td><td>114.6</td><td>32.6</td><td>24.3</td><td>21.3</td><td>4.8</td><td>4.2</td><td>3.6</td><td>3.2</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.4</td><td>19.4</td><td>14.2</td><td>12.7</td><td>77.2</td><td>4.3</td><td>13.7</td><td>16.1</td><td>15.8</td></tr><tr><td>114.6</td><td>36.5</td><td>27.3</td><td>23.9</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4186 Tokyo Ohka Kogyo (New)</td><td>11,125</td><td>1,422</td><td>EW</td><td>9,400</td><td>-15.5</td><td>40.0</td><td>37.7</td><td>32.8</td><td>32.8</td><td>5.9</td><td>5.3</td><td>4.7</td><td>4.7</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.8</td><td>24.3</td><td>22.1</td><td>17.2</td><td>17.2</td><td>15.6</td><td>14.7</td><td>15.1</td><td>14.3</td></tr><tr><td>4203 Sumitomo Bakelite (New)</td><td>7,710</td><td>680</td><td>OW</td><td>8,000</td><td>3.8</td><td>24.1</td><td>21.0</td><td>17.6</td><td>15.9</td><td>1.9</td><td>1.8</td><td>1.7</td><td>1.6</td><td>1.4</td><td>1.6</td><td>1.9</td><td>2.3</td><td>12.3</td><td>12.1</td><td>10.3</td><td>9.6</td><td>8.8</td><td>9.0</td><td>10.0</td><td>10.4</td></tr><tr><td colspan="25"></td><td></td></tr><tr><td colspan="25">as of 2026/06/19Fine ChemicalsIndustry View: In-Line</td><td></td></tr><tr><td rowspan="2"></td><td rowspan="2">Current Price(Y)</td><td rowspan="2">Market Cap (JPY bn)</td><td rowspan="2">Rating</td><td rowspan="2">Price Target(Y)</td><td rowspan="2">Potential return (%)</td><td colspan="4">P/E(x)</td><td colspan="4">P/B(x)</td><td colspan="4">Div. Yield (%)</td><td colspan="4">EV/EBITDA (x)</td><td>ROE(%)</td><td></td><td></td><td></td></tr><tr><td>25</td><td>26e</td><td>27e</td><td>28e</td><td>25</td><td>26e</td><td>27e</td><td>28e</td><td>25e</td><td>26e</td><td>27e</td><td>28e</td><td>25</td><td>26e</td><td>27e</td><td>28e</td><td>25</td><td>26e</td><td>27e</td><td>28e</td></tr><tr><td>4023 Kureha</td><td>3,870</td><td>193</td><td>EW</td><td>3,800</td><td>-1.8</td><td>-</td><td>13.6</td><td>12.3</td><td>12.3</td><td>0.9</td><td>0.9</td><td>0.9</td><td>0.9</td><td>5.5</td><td>5.7</td><td>4.1</td><td>4.1</td><td>-4.3</td><td>10.2</td><td>9.3</td><td>7.7</td><td>-</td><td>6.7</td><td>7.3</td><td>7.2</td></tr><tr><td>4043 Tokuyama</td><td>5,124</td><td>369</td><td>OW</td><td>6,300</td><td>23.0</td><td>16.6</td><td>7.0</td><td>11.5</td><td>11.0</td><td>1.3</td><td>1.1</td><td>1.1</td><td>1.0</td><td>2.3</td><td>2.5</td><td>3.1</td><td>3.5</td><td>7.3</td><td>7.1</td><td>6.4</td><td>319.4</td><td>8.2</td><td>17.2</td><td>9.5</td><td>9.4</td></tr><tr><td>4061 Denka</td><td>4,439</td><td>393</td><td>EW</td><td>3,500</td><td>-21.2</td><td>24.4</td><td>19.4</td><td>15.6</td><td>15.6</td><td>1.2</td><td>1.2</td><td>1.2</td><td>1.2</td><td>2.3</td><td>2.3</td><td>2.3</td><td>2.3</td><td>10.1</td><td>9.2</td><td>8.7</td><td>7.0</td><td>5.2</td><td>6.3</td><td>7.7</td><td>7.5</td></tr><tr><td>4091 NIPPON SANSO HOLDINGS (New)</td><td>5,564</td><td>2,410</td><td>UW</td><td>5,300</td><td>-4.7</td><td>19.4</td><td>17.6</td><td>17.6</td><td>17.1</td><td>2.0</td><td>1.8</td><td>1.7</td><td>1.6</td><td>1.1</td><td>1.2</td><td>1.2</td><td>1.3</td><td>9.6</td><td>9.4</td><td>8.9</td><td>72.4</td><td>11.3</td><td>10.8</td><td>9.9</td><td>9.5</td></tr><tr><td>4118 Kaneka</td><td>5,730</td><td>361</td><td>EW</td><td>4,600</td><td>-19.7</td><td>11.4</td><td>13.0</td><td>10.3</td><td>10.3</td><td>0.7</td><td>0.7</td><td>0.6</td><td>0.6</td><td>2.8</td><td>2.9</td><td>3.0</td><td>3.0</td><td>6.7</td><td>5.9</td><td>5.5</td><td>4.5</td><td>6.4</td><td>5.3</td><td>6.5</td><td>6.3</td></tr><tr><td>4182 Mitsubishi Gas Chemical (New)</td><td>5,424</td><td>1,148</td><td>OW</td><td>5,900</td><td>8.8</td><td>-</td><td>18.5</td><td>16.3</td><td>14.3</td><td>1.6</td><td>1.6</td><td>1.5</td><td>1.4</td><td>1.8</td><td>2.0</td><td>2.2</td><td>2.2</td><td>14.9</td><td>10.6</td><td>9.7</td><td>159.0</td><td>-</td><td>8.6</td><td>9.3</td><td>10.0</td></tr><tr><td>4202 Daicel</td><td>1,328</td><td>340</td><td>EW</td><td>1,400</td><td>5.5</td><td>34.3</td><td>7.7</td><td>6.6</td><td>6.6</td><td>1.0</td><td>0.9</td><td>0.8</td><td>0.8</td><td>4.5</td><td>4.8</td><td>5.3</td><td>5.3</td><td>6.4</td><td>5.5</td><td>5.0</td><td>3.9</td><td>2.8</td><td>12.0</td><td>13.1</td><td>12.5</td></tr><tr><td>4204 Sekisui Chemical (New)</td><td>2,471</td><td>1,002</td><td>UW</td><td>2,200</td><td>-11.0</td><td>13.5</td><td>11.7</td><td>10.6</td><td>10.6</td><td>1.2</td><td>1.1</td><td>1.1</td><td>1.0</td><td>3.2</td><td>3.5</td><td>3.6</td><td>3.9</td><td>6.0</td><td>6.3</td><td>5.8</td><td>116.7</td><td>9.0</td><td>9.8</td><td>10.2</td><td>9.6</td></tr><tr><td>4403 NOF</td><td>2,710</td><td>641</td><td>OW</td><td>3,600</td><td>32.8</td><td>15.4</td><td>13.7</td><td>12.8</td><td>12.8</td><td>2.1</td><td>2.0</td><td>1.9</td><td>1.9</td><td>2.3</td><td>2.7</td><td>2.8</td><td>2.8</td><td>8.0</td><td>5.3</td><td>5.5</td><td>6.0</td><td>14.1</td><td>15.1</td><td>15.5</td><td>15.1</td></tr></table>

<table><tr><td rowspan="3">as of Electronic Chemicals Industry View: In-Line</td><td rowspan="3">2026/06/19</td><td colspan="6">3M ave</td><td colspan="8">3M ave</td><td></td></tr><tr><td rowspan="2">(JPY)Last</td><td rowspan="2">(JPY bn)Market cap</td><td rowspan="2">(JPY bn)Daily vol</td><td colspan="4">Performance (%)</td><td rowspan="2">(mil)Daily vol</td><td rowspan="2">(mil)Mgn buy</td><td rowspan="2">(mil)Mgn sell</td><td rowspan="2">(mil)Short</td><td rowspan="2">(mil)Net</td><td rowspan="2">(days)Net</td><td rowspan="2">(k) Holders</td><td rowspan="2">(%) Foreign</td></tr><tr><td>WTD</td><td>MTD</td><td>QTD</td><td>YTD</td></tr><tr><td>4004 RESONAC HOLDINGS CORP</td><td>18,390</td><td>3,400.3</td><td>53.0</td><td>8.5</td><td>-1.8</td><td>87.6</td><td>181.8</td><td>3.4</td><td>1.5</td><td>-0.3</td><td>-10.0</td><td>-8.8</td><td>-2.6</td><td>59.5</td><td>38.5</td><td></td></tr><tr><td>4186 TOKYO OHKA KOGYO CO LTD</td><td>11,125</td><td>1,421.8</td><td>10.6</td><td>12.3</td><td>1.0</td><td>50.9</td><td>91.7</td><td>1.1</td><td>0.6</td><td>-0.1</td><td>0.0</td><td>0.5</td><td>0.5</td><td>18.8</td><td>27.3</td><td></td></tr><tr><td>4203 SUMITOMO BAKELITE CO LTD</td><td>7,710</td><td>680.4</td><td>3.7</td><td>19.0</td><td>11.7</td><td>59.7</td><td>49.3</td><td>0.6</td><td>0.1</td><td>-0.0</td><td>0.0</td><td>0.1</td><td>0.2</td><td>8.6</td><td>35.8</td><td></td></tr><tr><td colspan="17"></td></tr><tr><td rowspan="2">as of Fine Chemiclas Industry View: In-Line</td><td rowspan="2">2026/06/19</td><td colspan="6">3M ave</td><td colspan="9">3M ave</td></tr><tr><td>(JPY)Last</td><td>(JPY bn)Market cap</td><td>(JPY bn)Daily vol</td><td colspan="4">Performance (%)</td><td>(mil)Daily vol</td><td>(mil)Mgn buy</td><td>(mil)Mgn sell</td><td>(mil)Short</td><td>(mil)Net</td><td>(days)Net</td><td>(k) Holders</td><td>(%) Foreign</td></tr><tr><td>4023 KUREHA CORP</td><td>3,870</td><td>193.3</td><td>1.7</td><td>2.8</td><td>-0.9</td><td>-1.9</td><td>-5.3</td><td>0.4</td><td>0.6</td><td>-0.1</td><td>-2.8</td><td>-2.2</td><td>-5.1</td><td>9.2</td><td>18.3</td><td></td></tr><tr><td>4043 TOKUYAMA CORP</td><td>5,124</td><td>369.4</td><td>3.8</td><td>9.0</td><td>0.3</td><td>37.1</td><td>24.3</td><td>0.9</td><td>1.4</td><td>-0.0</td><td>-0.4</td><td>1.0</td><td>1.1</td><td>30.6</td><td>28.6</td><td></td></tr><tr><td>4061 DENKA CO LTD</td><td>4,439</td><td>393.1</td><td>3.8</td><td>10.2</td><td>-0.8</td><td>25.7</td><td>61.8</td><td>1.0</td><td>0.2</td><td>-0.1</td><td>-3.9</td><td>-3.8</td><td>-3.9</td><td>41.6</td><td>20.9</td><td></td></tr><tr><td>4091 NIPPON SANSO HOLDINGS CORP</td><td>5,564</td><td>2,409.7</td><td>4.4</td><td>3.0</td><td>-10.0</td><td>0.6</td><td>19.2</td><td>0.7</td><td>0.2</td><td>-0.0</td><td>0.0</td><td>0.2</td><td>0.2</td><td>12.5</td><td>22.1</td><td></td></tr><tr><td>4118 KANEKA CORP</td><td>5,730</td><td>361.0</td><td>1.2</td><td>2.9</td><td>3.8</td><td>19.5</td><td>30.4</td><td>0.2</td><td>0.2</td><td>-0.0</td><td>0.0</td><td>0.2</td><td>0.6</td><td>22.1</td><td>24.3</td><td></td></tr><tr><td>4182 MITSUBISHI GAS CHEMICAL CO</td><td>5,424</td><td>1,148.2</td><td>6.7</td><td>10.6</td><td>-2.2</td><td>50.9</td><td>91.0</td><td>1.5</td><td>0.2</td><td>-0.1</td><td>0.0</td><td>0.1</td><td>0.1</td><td>33.3</td><td>21.7</td><td></td></tr><tr><td>4202 DAICEL CORP</td><td>1,328</td><td>340.0</td><td>2.0</td><td>2.2</td><td>-0.5</td><td>8.3</td><td>-5.1</td><td>1.6</td><td>0.9</td><td>-0.0</td><td>0.0</td><td>0.8</td><td>0.5</td><td>37.7</td><td>32.6</td><td></td></tr><tr><td>4204 SEKISUI CHEMICAL CO LTD</td><td>2,471</td><td>1,002.0</td><td>7.8</td><td>3.8</td><td>7.9</td><td>-5.2</td><td>-6.2</td><td>3.2</td><td>2.8</td><td>-0.3</td><td>0.0</td><td>2.4</td><td>0.8</td><td>155.9</td><td>34.6</td><td></td></tr><tr><td>4208 UBE CORP</td><td>3,205</td><td>340.4</td><td>3.1</td><td>4.5</td><td>8.6</td><td>31.8</td><td>24.7</td><td>1.1</td><td>0.8</td><td>-0.1</td><td>-3.3</td><td>-2.5</td><td>-2.2</td><td>77.6</td><td>16.7</td><td></td></tr><tr><td>4403 NOF CORP</td><td>2,710</td><td>641.0</td><td>2.5</td><td>0.9</td><td>-3.0</td><td>-12.6</td><td>-10.0</td><td>0.8</td><td>0.2</td><td>-0.0</td><td>0.0</td><td>0.2</td><td>0.2</td><td>12.0</td><td>36.9</td><td></td></tr></table>

## Stock price performance (as of Jun 19)

Source: Bloomberg, MS
Note: Share prices are as of 19 June 2026.

## OP, core OP, BP (quarterly)

<table><tr><td colspan="7">(JPY bn)</td></tr><tr><td></td><td>25/3</td><td>25/6</td><td>25/9</td><td>25/12</td><td>26/3e</td><td>26/3A</td></tr><tr><td>Electronic Materials</td><td>31.6</td><td>38.8</td><td>58.4</td><td>60.6</td><td>48.1</td><td>57.3</td></tr><tr><td>* 4004 Resonac Holdings (IFRS)**</td><td>14.8</td><td>19.8</td><td>38.2</td><td>36.3</td><td>27.5</td><td>33.6</td></tr><tr><td>* 4186 Tokyo Ohka Kogyo</td><td>9.8</td><td>10.0</td><td>12.0</td><td>15.5</td><td>12.5</td><td>15.1</td></tr><tr><td>4203 Sumitomo Bakelite***</td><td>6.9</td><td>9.0</td><td>8.1</td><td>8.7</td><td>8.1</td><td>8.6</td></tr><tr><td>Fine Chemicals</td><td>134.2</td><td>123.4</td><td>134.2</td><td>144.1</td><td>122.8</td><td>120.2</td></tr><tr><td>4023 Kureha</td><td>-1.0</td><td>2.3</td><td>5.8</td><td>5.2</td><td>-23.3</td><td>-31.9</td></tr><tr><td>4043 Tokuyama</td><td>8.9</td><td>7.9</td><td>11.3</td><td>7.6</td><td>12.8</td><td>10.3</td></tr><tr><td>4061 Denka</td><td>2.6</td><td>2.3</td><td>7.4</td><td>8.5</td><td>7.3</td><td>8.0</td></tr><tr><td>4091 NIPPON SANSO HOLDINGS**</td><td>49.4</td><td>45.6</td><td>48.6</td><td>52.0</td><td>49.8</td><td>56.8</td></tr><tr><td>4118 Kaneka</td><td>10.9</td><td>8.2</td><td>6.8</td><td>7.2</td><td>11.8</td><td>10.7</td></tr><tr><td>4182 Mitsubishi Gas Chemical</td><td>5.6</td><td>11.0</td><td>14.2</td><td>12.7</td><td>10.2</td><td>7.5</td></tr><tr><td>4202 Daicel</td><td>17.8</td><td>13.0</td><td>7.1</td><td>12.3</td><td>8.6</td><td>9.6</td></tr><tr><td>4204 Sekisui Chemical</td><td>30.6</td><td>21.2</td><td>24.2</td><td>27.5</td><td>32.1</td><td>33.6</td></tr><tr><td>4403 NOF</td><td>9.5</td><td>11.8</td><td>8.8</td><td>11.2</td><td>13.7</td><td>15.6</td></tr><tr><td>Total</td><td>165.8</td><td>162.2</td><td>192.6</td><td>204.7</td><td>170.9</td><td>177.5</td></tr></table>

\*CY, \*\*Core OP, \*\*\*Business profit

<table><tr><td colspan="6">(YoY)</td></tr><tr><td>25/3</td><td>25/6</td><td>25/9</td><td>25/12</td><td>26/3e</td><td>26/3A</td></tr><tr><td>43%</td><td>-1%</td><td>9%</td><td>47%</td><td>52%</td><td>82%</td></tr><tr><td>55%</td><td>-16%</td><td>7%</td><td>56%</td><td>85%</td><td>126%</td></tr><tr><td>69%</td><td>31%</td><td>23%</td><td>57%</td><td>28%</td><td>54%</td></tr><tr><td>2%</td><td>14%</td><td>2%</td><td>8%</td><td>17%</td><td>25%</td></tr><tr><td>9%</td><td>-12%</td><td>-4%</td><td>8%</td><td>-8%</td><td>-10%</td></tr><tr><td>-</td><td>-27%</td><td>54%</td><td>50%</td><td>-</td><td>-</td></tr><tr><td>2%</td><td>5%</td><td>75%</td><td>7%</td><td>44%</td><td>16%</td></tr><tr><td>216%</td><td>-51%</td><td>59%</td><td>248%</td><td>181%</td><td>209%</td></tr><tr><td>20%</td><td>-6%</td><td>8%</td><td>12%</td><td>1%</td><td>15%</td></tr><tr><td>0%</td><td>-21%</td><td>-23%</td><td>-28%</td><td>8%</td><td>-2%</td></tr><tr><td>-36%</td><td>-30%</td><td>-21%</td><td>10%</td><td>83%</td><td>35%</td></tr><tr><td>-1%</td><td>-25%</td><td>-50%</td><td>6%</td><td>-52%</td><td>-46%</td></tr><tr><td>7%</td><td>5%</td><td>-15%</td><td>-4%</td><td>5%</td><td>10%</td></tr><tr><td>8%</td><td>-12%</td><td>-10%</td><td>-10%</td><td>43%</td><td>63%</td></tr><tr><td>14%</td><td>-10%</td><td>0%</td><td>17%</td><td>3%</td><td>7%</td></tr></table>

## OP, core OP, BP (yearly)

<table><tr><td colspan="17">(JPY bn)</td></tr><tr><td rowspan="2"></td><td rowspan="2">F23A</td><td rowspan="2">F24A</td><td colspan="4">F25</td><td colspan="3">F26</td><td colspan="3">(YoY)</td><td colspan="3">(F26)</td><td>F26</td></tr><tr><td>Ce</td><td>Con</td><td>e</td><td>A</td><td>Con</td><td>e</td><td>Ce</td><td>Con</td><td>e</td><td>A</td><td>Con</td><td>e</td><td>Ce</td><td>Ce vs Con</td></tr><tr><td>Electronic Materials</td><td>60.1</td><td>156.1</td><td>172.0</td><td>189.9</td><td>190.5</td><td>191.0</td><td>222.3</td><td>284.0</td><td>230.2</td><td>22%</td><td>22%</td><td>22%</td><td>16%</td><td>49%</td><td>21%</td><td>4%</td></tr><tr><td>* 4004 Resonac Holdings (New)**</td><td>9.9</td><td>92.1</td><td>98.0</td><td>109.1</td><td>109.1</td><td>109.1</td><td>131.4</td><td>183.0</td><td>140.0</td><td>18%</td><td>18%</td><td>18%</td><td>20%</td><td>68%</td><td>28%</td><td>7%</td></tr><tr><td>* 4186 Tokyo Ohka Kogyo (New)</td><td>22.7</td><td>33.1</td><td>40.0</td><td>47.4</td><td>47.4</td><td>47.4</td><td>53.8</td><td>60.0</td><td>52.2</td><td>43%</td><td>43%</td><td>43%</td><td>14%</td><td>27%</td><td>10%</td><td>-3%</td></tr><tr><td>4203 Sumitomo Bakelite (New)***</td><td>27.5</td><td>30.8</td><td>34.0</td><td>33.4</td><td>34.0</td><td>34.5</td><td>37.1</td><td>41.0</td><td>38.0</td><td>8%</td><td>10%</td><td>12%</td><td>8%</td><td>19%</td><td>10%</td><td>2%</td></tr><tr><td>Fine Chemicals</td><td>496.7</td><td>548.1</td><td>520.1</td><td>555.9</td><td>524.5</td><td>521.9</td><td>633.1</td><td>639.0</td><td>-</td><td>1%</td><td>-4%</td><td>-5%</td><td>21%</td><td>22%</td><td>-</td><td>-</td></tr><tr><td>4023 Kureha</td><td>12.8</td><td>9.4</td><td>-17.9</td><td>14.0</td><td>-10.0</td><td>-18.6</td><td>15.5</td><td>16.0</td><td>10.0</td><td>48%</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-35%</td></tr><tr><td>4043 Tokuyama (New)</td><td>25.6</td><td>30.0</td><td>39.0</td><td>39.8</td><td>39.5</td><td>37.0</td><td>43.1</td><td>40.0</td><td>-</td><td>33%</td><td>32%</td><td>24%</td><td>16%</td><td>8%</td><td>-</td><td>-</td></tr><tr><td>4061 Denka</td><td>13.4</td><td>14.4</td><td>25.0</td><td>25.5</td><td>25.5</td><td>26.2</td><td>36.3</td><td>34.5</td><td>30.0</td><td>77%</td><td>77%</td><td>82%</td><td>38%</td><td>32%</td><td>14%</td><td>-17%</td></tr><tr><td>4091 NIPPON SANSO HOLDINGS (New)**</td><td>166.0</td><td>189.1</td><td>196.0</td><td>197.8</td><td>196.0</td><td>203.1</td><td>213.3</td><td>210.0</td><td>208.0</td><td>5%</td><td>4%</td><td>7%</td><td>5%</td><td>3%</td><td>2%</td><td>-2%</td></tr><tr><td>4118 Kaneka</td><td>32.6</td><td>40.1</td><td>34.0</td><td>33.7</td><td>34.0</td><td>32.9</td><td>40.8</td><td>44.0</td><td>36.0</td><td>-16%</td><td>-15%</td><td>-18%</td><td>24%</td><td>34%</td><td>9%</td><td>-12%</td></tr><tr><td>4182 Mitsubishi Gas Chemical (New)</td><td>47.3</td><td>50.9</td><td>47.0</td><td>47.5</td><td>48.0</td><td>45.3</td><td>60.2</td><td>68.0</td><td>59.0</td><td>-7%</

[中间内容因长度限制已省略]

ntial Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Electronic Chemicals

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/19/2026)</td></tr><tr><td colspan="3">Ryoichi Watanabe</td></tr><tr><td>Resonac Holdings (4004.T)</td><td>O (03/04/2024)</td><td>¥18,390</td></tr><tr><td>Sumitomo Bakelite (4203.T)</td><td>O (05/26/2025)</td><td>¥7,710</td></tr><tr><td>Tokyo Ohka Kogyo (4186.T)</td><td>E (06/10/2025)</td><td>¥11,125</td></tr><tr><td colspan="3">Takato Watabe</td></tr><tr><td>Dexerials (4980.T)</td><td>E (08/27/2024)</td><td>¥4,859</td></tr><tr><td>Kuraray (3405.T)</td><td>E (04/03/2023)</td><td>¥1,723</td></tr><tr><td>Nissan Chemical (4021.T)</td><td>E (06/11/2018)</td><td>¥8,106</td></tr><tr><td>Nitto Denko (6988.T)</td><td>U (06/24/2022)</td><td>¥3,135</td></tr><tr><td>Shin-Etsu Chemical (4063.T)</td><td>O (07/27/2016)</td><td>¥7,310</td></tr><tr><td>SUMCO (3436.T)</td><td>U (06/09/2026)</td><td>¥4,254</td></tr><tr><td>ZEON (4205.T)</td><td>O (10/23/2014)</td><td>¥2,334</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS MUFG
"""
