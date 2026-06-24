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
June 22, 2026 06:29 AM GMT

Investor Presentation | Japan

Semiconductor Production Equipment:

Tech Monthly Jun 2026

MS MUFG SECURITIES CO., LTD.+
Suzune Tamura, CFA
Equity Analyst
Suzune.Tamura@morganstanleymufg.com +81 3 6836-8891

Kazuo Yoshikawa, CFA  
Equity Analyst  
Kazuo.Yoshikawa@morganstanleymufg.com +81 3 6836-8408

![](images/3ab4ef10d66e790a71f6550edb00d699a81725259c10b654358a32785d0c9551.jpg)

SEMICONDUCTOR PRODUCTION EQUIPMENT

Japan Industry View Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Stock Price Performance

![](images/e4636372929ea70f2bb83131b1408a5a395c8a6dc69a8ace702b1b857e5efbf4.jpg)  
2025/06/20 2025/08/01 2025/09/12 2025/10/24 2025/12/05 2026/01/16 2026/02/27 2026/04/10 2026/05/22

![](images/2ea443efeded348a602fdea9f2d03a693527109fc0e596f5c7497e56d692a0bd.jpg)

Source: FactSet data, MS

## Stock performance and valuation

<table><tr><td rowspan="3" colspan="3"></td><td rowspan="2" colspan="6">Rating Share price (LC) (LC) Performance</td><td colspan="12">Valuation</td><td></td></tr><tr><td colspan="3">Cons PE (x)</td><td colspan="3">Cons EV/EBITDA (x)</td><td colspan="3">Cons PBR (x)</td><td colspan="3">Cons Div. yield</td><td></td></tr><tr><td>MS</td><td>Last close</td><td>MS PT</td><td>YTD</td><td>3m</td><td>1m</td><td>11/20 ~</td><td>F1</td><td>F2</td><td>F3</td><td>F1</td><td>F2</td><td>F3</td><td>F1</td><td>F2</td><td>F3</td><td>F1</td><td>F2</td><td>F3</td></tr><tr><td>6146 JP</td><td>DISCO</td><td></td><td>OW</td><td>84,900</td><td>78,000</td><td>76.3%</td><td>22.0%</td><td>37.8%</td><td>79.6%</td><td>51.2</td><td>42.8</td><td>37.4</td><td>34.5</td><td>28.9</td><td>26.0</td><td>13.2</td><td>11.0</td><td>9.5</td><td>0.8%</td><td>1.0%</td><td>1.2%</td></tr><tr><td>7729 JP</td><td>Tokyo Seimitsu</td><td></td><td>OW</td><td>20,075</td><td>22,000</td><td>80.8%</td><td>40.6%</td><td>26.1%</td><td>85.3%</td><td>28.1</td><td>23.9</td><td>20.8</td><td>16.8</td><td>14.4</td><td>12.5</td><td>3.9</td><td>3.5</td><td>3.2</td><td>1.4%</td><td>1.7%</td><td>1.9%</td></tr><tr><td>6315 JP</td><td>Towa</td><td></td><td>EW</td><td>3,325</td><td>3,200</td><td>54.7%</td><td>31.2%</td><td>26.5%</td><td>32.0%</td><td>29.7</td><td>23.6</td><td>20.6</td><td>16.6</td><td>13.2</td><td>12.2</td><td>3.2</td><td>2.9</td><td>2.6</td><td>0.7%</td><td>0.8%</td><td>0.8%</td></tr><tr><td>6857 JP</td><td>Advantest</td><td></td><td>OW</td><td>31,740</td><td>36,000</td><td>61.7%</td><td>32.4%</td><td>25.5%</td><td>52.3%</td><td>45.6</td><td>36.3</td><td>31.8</td><td>31.4</td><td>25.2</td><td>23.0</td><td>20.1</td><td>14.2</td><td>10.9</td><td>0.3%</td><td>0.4%</td><td>0.5%</td></tr><tr><td>TER US</td><td>Teradyne</td><td></td><td>EW</td><td>438</td><td>387</td><td>126.2%</td><td>45.9%</td><td>36.4%</td><td>180.9%</td><td>59.4</td><td>44.0</td><td>32.2</td><td>44.6</td><td>34.1</td><td>26.3</td><td>19.4</td><td>15.3</td><td>11.5</td><td>0.1%</td><td>0.1%</td><td>0.1%</td></tr><tr><td>8035 JP</td><td>Tokyo Electron</td><td></td><td>OW</td><td>75,360</td><td>65,000</td><td>119.6%</td><td>91.6%</td><td>59.8%</td><td>131.9%</td><td>48.0</td><td>37.8</td><td>31.7</td><td>33.4</td><td>26.6</td><td>23.3</td><td>14.0</td><td>11.8</td><td>10.0</td><td>1.0%</td><td>1.3%</td><td>1.6%</td></tr><tr><td>7735 JP</td><td>SCREEN Holdings</td><td></td><td>OW</td><td>16,745</td><td>17,000</td><td>119.8%</td><td>68.3%</td><td>59.2%</td><td>158.4%</td><td>27.5</td><td>23.0</td><td>20.2</td><td>17.0</td><td>14.4</td><td>13.0</td><td>5.8</td><td>5.0</td><td>4.2</td><td>1.1%</td><td>1.3%</td><td>1.5%</td></tr><tr><td>6525 JP</td><td>Kokusai Electric</td><td></td><td>OW</td><td>10,165</td><td>8,300</td><td>85.0%</td><td>88.1%</td><td>54.0%</td><td>140.8%</td><td>49.3</td><td>37.2</td><td>31.8</td><td>29.3</td><td>23.4</td><td>19.8</td><td>9.5</td><td>8.2</td><td>7.0</td><td>0.5%</td><td>0.7%</td><td>0.9%</td></tr><tr><td>6361 JP</td><td>Ebara</td><td></td><td>OW</td><td>6,560</td><td>5,800</td><td>78.1%</td><td>38.0%</td><td>27.3%</td><td>69.9%</td><td>29.2</td><td>26.0</td><td>21.8</td><td>17.8</td><td>15.0</td><td>13.0</td><td>5.2</td><td>4.6</td><td>4.1</td><td>1.1%</td><td>1.3%</td><td>1.6%</td></tr><tr><td>6920 JP</td><td>Lasertec</td><td></td><td>UW</td><td>55,100</td><td>15,600</td><td>85.9%</td><td>57.0%</td><td>52.8%</td><td>97.1%</td><td>64.8</td><td>51.7</td><td>40.8</td><td>44.1</td><td>35.1</td><td>28.3</td><td>20.1</td><td>16.2</td><td>12.8</td><td>0.6%</td><td>0.7%</td><td>0.9%</td></tr><tr><td>6951 JP</td><td>JEOL</td><td></td><td>EW</td><td>7,066</td><td>5,200</td><td>40.4%</td><td>18.9%</td><td>7.4%</td><td>52.2%</td><td>16.5</td><td>13.9</td><td>12.5</td><td>10.8</td><td>8.9</td><td>8.2</td><td>NA</td><td>NA</td><td>NA</td><td>1.9%</td><td>2.4%</td><td>2.3%</td></tr><tr><td>6925 JP</td><td>Ushio</td><td></td><td>OW</td><td>4,631</td><td>3,100</td><td>84.9%</td><td>61.9%</td><td>17.9%</td><td>99.3%</td><td>36.2</td><td>26.4</td><td>23.6</td><td>16.4</td><td>13.5</td><td>NA</td><td>1.9</td><td>1.9</td><td>NA</td><td>1.5%</td><td>1.7%</td><td>2.2%</td></tr><tr><td>6728 JP</td><td>ULVAC</td><td></td><td>EW</td><td>10,255</td><td>8,100</td><td>44.8%</td><td>11.8%</td><td>11.1%</td><td>53.5%</td><td>27.9</td><td>21.3</td><td>18.4</td><td>13.5</td><td>9.9</td><td>8.7</td><td>2.2</td><td>2.0</td><td>1.9</td><td>1.5%</td><td>1.7%</td><td>2.0%</td></tr><tr><td>7731 JP</td><td>Nikon</td><td></td><td>UW</td><td>2,153</td><td>1,100</td><td>23.5%</td><td>11.3%</td><td>6.6%</td><td>24.0%</td><td>65.2</td><td>33.2</td><td>25.3</td><td>14.3</td><td>11.4</td><td>10.2</td><td>1.2</td><td>1.2</td><td>1.2</td><td>1.2%</td><td>1.5%</td><td>1.4%</td></tr><tr><td>AMAT US</td><td>Applied Materials</td><td></td><td>EW</td><td>617</td><td>502</td><td>140.1%</td><td>76.6%</td><td>49.2%</td><td>180.2%</td><td>50.4</td><td>37.5</td><td>30.6</td><td>43.2</td><td>31.8</td><td>25.9</td><td>18.5</td><td>14.9</td><td>11.9</td><td>0.3%</td><td>0.3%</td><td>0.4%</td></tr><tr><td>LRCX US</td><td>Lam Research</td><td></td><td>OW</td><td>389</td><td>331</td><td>127.3%</td><td>73.1%</td><td>40.0%</td><td>178.7%</td><td>68.4</td><td>48.3</td><td>39.6</td><td>56.7</td><td>40.0</td><td>33.4</td><td>42.5</td><td>28.7</td><td>20.1</td><td>0.3%</td><td>0.3%</td><td>0.3%</td></tr><tr><td>KLAC US</td><td>KLA</td><td></td><td>OW</td><td>260</td><td>190</td><td>113.6%</td><td>75.1%</td><td>47.8%</td><td>135.4%</td><td>70.0</td><td>50.8</td><td>42.7</td><td>55.9</td><td>42.0</td><td>35.5</td><td>58.4</td><td>46.4</td><td>35.7</td><td>0.3%</td><td>0.4%</td><td>0.4%</td></tr><tr><td>NVDA US</td><td>NVIDIA Corp</td><td></td><td>OW</td><td>211</td><td>288</td><td>13.0%</td><td>16.8%</td><td>-5.2%</td><td>16.6%</td><td>23.6</td><td>16.8</td><td>14.3</td><td>19.2</td><td>13.5</td><td>11.2</td><td>17.0</td><td>10.1</td><td>6.8</td><td>0.3%</td><td>0.4%</td><td>0.4%</td></tr><tr><td>285A JP</td><td>Kioxia Holdings</td><td></td><td>OW</td><td>108,600</td><td>110,000</td><td>940.7%</td><td>385.7%</td><td>118.2%</td><td>858.1%</td><td>11.5</td><td>8.9</td><td>7.5</td><td>7.9</td><td>6.1</td><td>5.5</td><td>9.4</td><td>5.1</td><td>3.3</td><td>0.3%</td><td>0.4%</td><td>0.5%</td></tr><tr><td>429A JP</td><td>Tekscend</td><td></td><td>EW</td><td>4,305</td><td>4,600</td><td>42.1%</td><td>41.8%</td><td>4.2%</td><td>37.5%</td><td>16.2</td><td>14.5</td><td>12.4</td><td>7.1</td><td>6.0</td><td>5.1</td><td>2.2</td><td>2.0</td><td>1.8</td><td>1.8%</td><td>1.8%</td><td>2.2%</td></tr><tr><td>PLAB US</td><td>Photronics</td><td></td><td>NA</td><td>34</td><td>NA</td><td>5.1%</td><td>-5.0%</td><td>-29.2%</td><td>65.8%</td><td>18.2</td><td>16.6</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr></table>

## Memory price trends

![](images/108d4a9a346b73c1c576647610aba3c21efa90b71faa6e1e00edf1c64bbe1402.jpg)

![](images/4339e8018e298137dd599071ee8456c02e59024dc7be4cfa944596ec1b827a4b.jpg)

## DRAM YoY growth

DRAM Sales YoY contribution breakdown  
![](images/1f00d69c627da6c6b65b308c7a30c3a8ba2df064e375cb8fa02008e5bf256723.jpg)  
Source: WSTS, MS

## DRAM bit shipment and ASP YoY growth

Bit volume YoY and ASP YoY  
![](images/85081574474d78a1ce8f15a9e52869e6bb80c32d006d93970c32710191fd3f88.jpg)  
Source: WSTS, MS

## Agentic AI: Sizable memory demand

## Vera CPU could boost total DRAM bit demand by $\sim 16\%$ vs 2025

![](images/cd607437508d43093d8bd560c59aa023bd30cbae4193c98093dc19ef1c8ad2cd.jpg)  
Source: Nvidia, MS

![](images/b6fba2d892a41bc32b4be54c95a7394036e90d9e7cbb6da6ee37be5afb2b4a71.jpg)  
Source: TrendForce, MS estimates

## Huge amount of DRAM needed in Agentic era

Chatbot

Agents

Request

Request

GPU

GPU

10s\~100s loops

CPU

Requires huge working memory throughout the loops

Source: MS

# NAND also seeing exponential demand

AI storage architecture

Memory Model Weights & GPU Overflow

Flash KV Cache

Flash Vectors, Embeddings & RAG

HDD Bulk Storage

Agentic AI leads to longer context, compounding data retention requirements, etc.

Source: Western Digital, MS

Distance that signals can travel over Cu cable

## Connectivity to be the next bottle neck

![](images/4b9a686f5b84cacf3566eb7fbf15fbfe21e1f0f825e25a3c373d9fe0408aceb1.jpg)

![](images/19d43069661349c774f9ed7f17790f92183baf6a012a2dfa1fb8d041b1be3daf.jpg)  
Source: Marvell Technology, MS

## Our earnings forecasts

## Semiconductor Production Equipment: Jan-Mar Results Overview (26 May 2026)

<table><tr><td>New Forecasts</td><td>Actual</td><td>MSe</td><td></td><td>MSe</td><td></td><td>MSe</td><td></td></tr><tr><td></td><td>26/3</td><td>27/3</td><td>YoY</td><td>28/3</td><td>YoY</td><td>29/3</td><td>YoY</td></tr><tr><td>Sales (¥bn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tokyo Electron</td><td>2,443.5</td><td>3,396.0</td><td>39%</td><td>4,087.0</td><td>20%</td><td>4,546.0</td><td>11%</td></tr><tr><td>SCREEN Holdings</td><td>605.7</td><td>739.7</td><td>22%</td><td>861.2</td><td>16%</td><td>973.2</td><td>13%</td></tr><tr><td>KOKUSAI ELECTRIC</td><td>235.1</td><td>321.2</td><td>37%</td><td>377.8</td><td>18%</td><td>399.9</td><td>6%</td></tr><tr><td>Advantest</td><td>1,128.6</td><td>1,563.5</td><td>39%</td><td>2,182.9</td><td>40%</td><td>2,641.8</td><td>21%</td></tr><tr><td>Disco</td><td>436.9</td><td>579.8</td><td>33%</td><td>679.0</td><td>17%</td><td>780.0</td><td>15%</td></tr><tr><td>Operating Income (¥bn)</td><td></td><td></td><td>OPM</td><td></td><td>OPM</td><td></td><td>OPM</td></tr><tr><td>Tokyo Electron</td><td>624.9</td><td>988.0</td><td>29%</td><td>1,358.0</td><td>33%</td><td>1,607.0</td><td>35%</td></tr><tr><td>SCREEN Holdings</td><td>122.5</td><td>164.9</td><td>22%</td><td>199.8</td><td>23%</td><td>236.4</td><td>24%</td></tr><tr><td>KOKUSAI ELECTRIC</td><td>41.8</td><td>73.6</td><td>23%</td><td>94.0</td><td>25%</td><td>98.3</td><td>25%</td></tr><tr><td>Advantest</td><td>499.1</td><td>736.7</td><td>47%</td><td>1,097.9</td><td>50%</td><td>1,348.2</td><td>51%</td></tr><tr><td>Disco</td><td>185.0</td><td>263.8</td><td>45%</td><td>321.0</td><td>47%</td><td>379.8</td><td>49%</td></tr><tr><td>EPS (¥)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tokyo Electron</td><td>1,255</td><td>1,644</td><td>31%</td><td>2,256</td><td>37%</td><td>2,667</td><td>18%</td></tr><tr><td>SCREEN Holdings</td><td>487</td><td>636</td><td>31%</td><td>765</td><td>20%</td><td>903</td><td>18%</td></tr><tr><td>KOKUSAI ELECTRIC</td><td>129</td><td>233</td><td>81%</td><td>298</td><td>28%</td><td>312</td><td>5%</td></tr><tr><td>Advantest</td><td>515</td><td>751</td><td>46%</td><td>1,120</td><td>49%</td><td>1,375</td><td>23%</td></tr><tr><td>Disco</td><td>1,250</td><td>1,802</td><td>44%</td><td>2,192</td><td>22%</td><td>2,592</td><td>18%</td></tr></table>

<table><tr><td colspan="4">Mse based PER (as of Jun 19)</td></tr><tr><td>Close price(¥)</td><td>27/3</td><td>28/3</td><td>29/3</td></tr><tr><td>75,360</td><td>45.8</td><td>33.4</td><td>28.3</td></tr><tr><td>16,745</td><td>26.3</td><td>21.9</td><td>18.5</td></tr><tr><td>10,165</td><td>43.7</td><td>34.1</td><td>32.5</td></tr><tr><td>31,740</td><td>42.2</td><td>28.3</td><td>23.1</td></tr><tr><td>84,900</td><td>47.1</td><td>38.7</td><td>32.8</td></tr></table>

## We upgraded Advantest to Top Pick (May 26, 2026)

## Computing/Communication Tester forecasts

<table><tr><td>(JPY mn) Computing/Communication</td><td>19/3</td><td>20/3</td><td>21/3</td><td>22/3</td><td>23/3</td><td>24/3</td><td>25/3</td><td>26/3</td><td>27/3 MSe</td><td>28/3 MSe</td><td>29/3 MSe</td></tr><tr><td>Computing/Communication</td><td>89,160</td><td>108,500</td><td>77,798</td><td>135,360</td><td>211,575</td><td>147,360</td><td>396,360</td><td>729,030</td><td>1,070,000</td><td>1,555,000</td><td>1,875,000</td></tr><tr><td>y-y</td><td>NA</td><td>22%</td><td>-28%</td><td>74%</td><td>56%</td><td>-30%</td><td>169%</td><td>84%</td><td>47%</td><td>45%</td><td>21%</td></tr><tr><td>V93000 EXA Scale price (¥mn) (asmp.)</td><td>191</td><td>202</td><td>191</td><td>202</td><td>241</td><td>257</td><td>275</td><td>270</td><td>279</td><td>287</td><td>296</td></tr><tr><td>$mn</td><td>1.8</td><td>1.8</td><td>1.8</td><td>1.8</td><td>1.8</td><td>1.8</td><td>1.8</td><td>1.8</td><td>1.8</td><td>1.9</td><td>1.9</td></tr><tr><td>y-y</td><td>NA</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>3%</td><td>3%</td></tr><tr><td>Implied units (unit)</td><td>467</td><td>538</td><td>408</td><td>671</td><td>877</td><td>572</td><td>1,439</td><td>2,700</td><td>3,835</td><td>5,411</td><td>6,335</td></tr><tr><td>y-y</td><td>NA</td><td>15%</td><td>-24%</td><td>64%</td><td>31%</td><td>-35%</td><td>152%</td><td>88%</td><td>42%</td><td>41%</td><td>17%</td></tr><tr><td>TSMC</td><td></td><td></td><td></td><td></td><td></td><td></td><td>96,158</td><td></td><td></td><td></td><td></td></tr><tr><td>% of sales</td><td></td><td></td><td></td><td></td><td></td><td></td><td>12.3%</td><td></td><td></td><td></td><td></td></tr></table>

Our P&L forecasts

<table><tr><td>(JPY mn) IFRS</td><td>19/3</td><td>20/3</td><td>21/3</td><td>22/3</td><td>23/3</td><td>24/3</td><td>25/3</td><td>26/3</td><td>27/3 MSe</td><td>28/3 MSe</td><td>29/3 MSe</td></tr><tr><td>Net sales</td><td>282,456</td><td>275,894</td><td>312,789</td><td>416,901</td><td>560,191</td><td>486,507</td><td>779,707</td><td>1,128,610</td><td>1,563,500</td><td>2,182,900</td><td>2,641,800</td></tr><tr><td>y-y</td><td>NA</td><td>-2%</td><td>13%</td><td>33%</td><td>34%</td><td>-13%</td><td>60%</td><td>45%</td><td>39%</td><td>40%</td><td>21%</td></tr><tr><td>q-q</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cost of sales</td><td>128,417</td><td>119,397</td><td>144,498</td><td>180,994</td><td>241,130</td><td>240,477</td><td>334,622</td><td>402,503</td><td>555,600</td><td>769,100</td><td>925,000</td></tr><tr><td>Gross profit</td><td>154,039</td><td>156,497</td><td>168,291</td><td>235,907</td><td>319,061</td><td>246,030</td><td>445,085</td><td>726,107</td><td>1,007,900</td><td>1,413,800</td><td>1,716,800</td></tr><tr><td>y-y</td><td>NA</td><td>2%</td><td>8%</td><td>40%</td><td>35%</td><td>-23%</td><td>81%</td><td>63%</td><td>39%</td><td>40%</td><td>21%</td></tr><tr><td>q-q</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>margin</td><td>54.5%</td><td>56.7%</td><td>53.8%</td><td>56.6%</td><td>57.0%</td><td>50.6%</td><td>57.1%</td><td>64.3%</td><td>64.5%</td><td>64.8%</td><td>65.0%</td></tr><tr><td>Operating profit</td><td>64,662</td><td>58,708</td><td>70,726</td><td>114,734</td><td>167,687</td><td>81,628</td><td>228,161</td><td>499,120</td><td>736,700</td><td>1,097,900</td><td>1,348,200</td></tr><tr><td>y-y</td><td>NA</td><td>-9%</td><td>20%</td><td>62%</td><td>46%</td><td>-51%</td><td>180%</td><td>119%</td><td>48%</td><td>49%</td><td>23%</td></tr><tr><td>q-q</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>margin</td><td>22.9%</td><td>21.3%</td><td>22.6%</td><td>27.5%</td><td>29.9%</td><td>16.8%</td><td>29.3%</td><td>44.2%</td><td>47.1%</td><td>50.3%</td><td>51.0%</td></tr><tr><td>EPS (JPY)</td><td>75.59</td><td>67.53</td><td>88.47</td><td>112.39</td><td>174.35</td><td>84.45</td><td>218.67</td><td>515.15</td><td>751.47</td><td>1,119.76</td><td>1,375.16</td></tr><tr><td>y-y</td><td>NA</td><td>-11%</td><td>31%</td><td>27%</td><td>55%</td><td>-52%</td><td>159%</td><td>136%</td><td>46%</td><td>49%</td><td>23%</td></tr></table>

Source: MS; MSe= MS estimates

## Tekscend Photomask: Earning Update (15 Jun 2026)

## Raising Forecasts on Expanding Outsourcing Demand

The three major investment projects currently planned are scheduled to begin production sequentially over 2027-28

<table><tr><td></td><td>Investment amount (@¥155/$)</td><td>Production starting in</td><td>Type of investment</td><td>Investment details</td></tr><tr><td>Singapore</td><td>¥35bn</td><td>H1 2027</td><td>New fab</td><td>up to 28nm</td></tr><tr><td>Round Rock (US)</td><td>&gt;=¥35bn</td><td>H2 2027</td><td>Line expansion</td><td>up to 12nm, &gt;= 40% capacity expansion</td></tr><tr><td>Icheon (South Korea)</td><td>¥26bn</td><td>H2 2028</td><td>New building (3rd plant)</td><td>14nm and below</td></tr><tr><td>Total</td><td>¥96bn</td><td></td><td></td><td></td></tr></table>

Source: Company materials, government publications and MS  
Summary of our forecasts

<table><tr><td rowspan="2">IFRS (¥mn)</td><td></td><td></td><td>MSe</td><td>MSe</td><td>MSe</td><td>Ce</td></tr><tr><td>Mar-25</td><td>Mar-26</td><td>Mar-27</td><td>Mar-28</td><td>Mar-29</td><td>Mar-27</td></tr><tr><td>Revenue</t

[中间内容因长度限制已省略]

n prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Semiconductor Production Equipment

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/19/2026)</td></tr><tr><td>Suzune Tamura, CFA</td><td></td><td></td></tr><tr><td>Advantest (6857.T)</td><td>O (01/17/2024)</td><td>¥31,740</td></tr><tr><td>DISCO (6146.T)</td><td>O (07/07/2023)</td><td>¥84,900</td></tr><tr><td>Ebara (6361.T)</td><td>O (12/04/2024)</td><td>¥6,560</td></tr><tr><td>JEOL (6951.T)</td><td>E (07/08/2025)</td><td>¥7,066</td></tr><tr><td>KOKUSAI ELECTRIC (6525.T)</td><td>O (12/19/2025)</td><td>¥10,165</td></tr><tr><td>Lasertec (6920.T)</td><td>U (07/28/2025)</td><td>¥55,100</td></tr><tr><td>Nikon (7731.T)</td><td>U (08/08/2023)</td><td>¥2,153</td></tr><tr><td>SCREEN Holdings (7735.T)</td><td>O (11/13/2025)</td><td>¥16,745</td></tr><tr><td>Tekscend Photomask (429A.T)</td><td>E (11/18/2025)</td><td>¥4,305</td></tr><tr><td>Tokyo Electron (8035.T)</td><td>O (12/19/2025)</td><td>¥75,360</td></tr><tr><td>Ulvac (6728.T)</td><td>E (01/17/2024)</td><td>¥10,255</td></tr><tr><td>Ushio (6925.T)</td><td>O (01/05/2026)</td><td>¥4,631</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS MUFG
"""
