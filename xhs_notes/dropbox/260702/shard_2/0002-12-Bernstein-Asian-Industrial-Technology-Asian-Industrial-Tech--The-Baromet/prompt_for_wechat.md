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
- 已识别机构名：`Bernstein`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Asian Industrial Technology

# Asian Industrial Tech: The Barometer (May/June 2026)

![](images/d2c7b8f9b95d7acb49991e03bbb0f9adbc39b5423bddda9db66f66c1095b6883.jpg)

Jay Huang, Ph.D.

+852 2123 2631

jay.huang@bernsteinsg.com

![](images/24aa0d51da5ada0234c574829cb6f4680a3f5bc9ce728fc3cc97cd74283d6617.jpg)

Weibin Liang, Ph.D.

+852 2123 2666

weibin.liang@bernsteinsg.com

In May and June, China FA continued to grow at near-peak rate. In the RoW, the recovery continued despite some fluctuations. Readers can download the complete barometer data set here: Global Industrial Barometer.

We highlight three datasets for China: 1) In June, the official manufacturing PMI and the PMI for production remained in expansion levels at 50.3 (was 50.0, Exhibit 2), 51.4 (was 51.2); PMI for new orders returned to expansion level at 51.2 (was 49.9, Exhibit 4). More relevant to factory automation, PMI for high-tech manufacturing and equipment manufacturing further expanded to 53.5 (was 52.9) and 52.5 (was 52.1). 2) In May, Japan's machine tool orders from China continued to grow strongly YoY (+42.7% YoY in May vs. +33.2% YoY in April, excluding FX effects, Exhibit 17), and the strength remains broad-based (Exhibit 18). The “twin peaks” pattern, similar to previous cycles, is forming. 3) In May, industrial profits continue to grow strongly (+21.1% YoY, Exhibit 7). In 5M26, the manufacturing sector (+20.0% YoY) outperformed the overall industrial sector (+18.8% YoY), led by the high-end manufacturing and electronics segments, which grew 44.7% YoY and 103.9% YoY, respectively.

Global: 1) In May, Japan's machine tool orders grew $37.5\%$ YoY and declined slightly by $6.3\%$ MoM (Exhibit 37). Excluding FX effects, growth in North America was $4.2\%$ YoY ( $16.2\%$ YoY in April), partly due to weakness in automotive (Exhibit 41); growth in EU temporarily turned negative, partly due to a high base (-13.2% YoY vs. +35.6% YoY in April); growth in Japan remained strong (+37.3% YoY in May vs. +43.4% YoY in April, Exhibit 38). 2) In June, the manufacturing PMI in all major economies remained in the expansion range (US. 55.7; Eurozone 51.3; Japan 54.8; Exhibit 34 to Exhibit 36). 3) In May, Japan's robot exports volume growth temporarily weakened, growing $9.1\%$ YoY (+40.7% YoY in April, Exhibit 45), likely due to MoM fluctuations, and all major regions remained in positive growth, with the U.S. +5.8% YoY, China +5.7% YoY, and Europe +10.8% YoY (Exhibit 46). In April, the overall Japan robot order maintained strong momentum (+34% YoY and -5% MoM).

## DETAILS

EXHIBIT 1: Momentum Tracker

<table><tr><td colspan="2"></td><td>Lastest period</td><td>Data type / unit</td><td>(a) Latest</td><td>(b) Previous</td><td>(c) YTD</td><td>(d) Previous FY</td><td>Momentum (a) vs. (b)</td><td>Momentum (c) vs. (d)</td></tr><tr><td rowspan="22">China</td><td colspan="9">Macro Indicator</td></tr><tr><td>M1</td><td>May-26</td><td>YoY Growth</td><td>5.5%</td><td>5.0%</td><td>5.3%</td><td>3.7%</td><td>↑</td><td>↑</td></tr><tr><td>PMI in Manufacturing</td><td>Jun-26</td><td>Index</td><td>50.3</td><td>50.0</td><td>49.9</td><td>49.6</td><td>↑</td><td>↑</td></tr><tr><td>RatingDog Manufacturing PMI</td><td>Jun-26</td><td>Index</td><td>51.7</td><td>51.8</td><td>51.5</td><td>50.3</td><td>↓</td><td>↑</td></tr><tr><td>Emerging Industries PMI</td><td>Jun-26</td><td>Index</td><td>50.4</td><td>52.9</td><td>52.2</td><td>50.9</td><td>↓</td><td>↑</td></tr><tr><td>FAI - Overall</td><td>May-26</td><td>YTD Growth</td><td>-4.1%</td><td>-1.6%</td><td>-0.1%</td><td>1.4%</td><td>↓</td><td>↓</td></tr><tr><td>FAI in Manufacturing</td><td>May-26</td><td>YTD Growth</td><td>-0.4%</td><td>1.2%</td><td>2.0%</td><td>5.8%</td><td>↓</td><td>↓</td></tr><tr><td>FAI in Equipment Purchase</td><td>May-26</td><td>YTD Growth</td><td>9.3%</td><td>11.5%</td><td>11.6%</td><td>15.5%</td><td>↓</td><td>↓</td></tr><tr><td>Manufacturing Capacity Utilization</td><td>1Q26</td><td>Value (%)</td><td>73.6</td><td>74.9</td><td>73.6</td><td>74.4</td><td>↓</td><td>↓</td></tr><tr><td>Industrial Profit Growth</td><td>May-26</td><td>YoY Growth</td><td>21.1%</td><td>24.7%</td><td>18.8%</td><td>0.6%</td><td>↓</td><td>↑</td></tr><tr><td>Manufacturing Value-Add</td><td>May-26</td><td>YoY Growth</td><td>4.4%</td><td>4.0%</td><td>5.3%</td><td>6.3%</td><td>↑</td><td>↓</td></tr><tr><td>PPI: All Industries</td><td>May-26</td><td>Index</td><td>101.8</td><td>101.3</td><td>99.9</td><td>98.1</td><td>↑</td><td>↑</td></tr><tr><td>Floor Space: Started</td><td>May-26</td><td>YTD Growth</td><td>-22.7%</td><td>-22.1%</td><td>-22.2%</td><td>-22.6%</td><td>↓</td><td>↑</td></tr><tr><td colspan="9">Equipment Production</td></tr><tr><td>Excavator (Sales Volume)</td><td>May-26</td><td>YoY Growth</td><td>36.2%</td><td>29.8%</td><td>24.7%</td><td>17.0%</td><td>↑</td><td>↑</td></tr><tr><td>Electric Motors</td><td>May-26</td><td>YoY Growth</td><td>6.3%</td><td>0.1%</td><td>-0.5%</td><td>-0.5%</td><td>↑</td><td>—</td></tr><tr><td>Metal-cutting Machine Tool</td><td>May-26</td><td>YoY Growth</td><td>10.7%</td><td>7.5%</td><td>5.9%</td><td>9.7%</td><td>↑</td><td>↓</td></tr><tr><td>Packaging Machinery</td><td>May-26</td><td>YoY Growth</td><td>-7.5%</td><td>21.2%</td><td>-3.8%</td><td>18.2%</td><td>↓</td><td>↓</td></tr><tr><td>Metal-shaping Machine Tool</td><td>May-26</td><td>YoY Growth</td><td>6.3%</td><td>6.3%</td><td>4.1%</td><td>7.2%</td><td>—</td><td>↓</td></tr><tr><td>Multiple Units</td><td>May-26</td><td>YoY Growth</td><td>-76.0%</td><td>-50.6%</td><td>3.0%</td><td>6.7%</td><td>↓</td><td>↓</td></tr><tr><td>Locomotives</td><td>May-26</td><td>YoY Growth</td><td>13.1%</td><td>30.6%</td><td>40.7%</td><td>16.7%</td><td>↓</td><td>↑</td></tr><tr><td>Industrial Robots</td><td>May-26</td><td>YoY Growth</td><td>27.9%</td><td>15.1%</td><td>28.1%</td><td>28.0%</td><td>↑</td><td>↑</td></tr><tr><td rowspan="31">World</td><td colspan="9">Purchasing Managers&#x27; Index (PMI)</td></tr><tr><td>World</td><td>May-26</td><td>Index</td><td>52.6</td><td>52.6</td><td>51.8</td><td>50.3</td><td>—</td><td>↑</td></tr><tr><td>United States</td><td>Jun-26</td><td>Index</td><td>55.7</td><td>55.1</td><td>53.6</td><td>51.7</td><td>↑</td><td>↑</td></tr><tr><td>Eurozone</td><td>Jun-26</td><td>Index</td><td>51.3</td><td>51.6</td><td>51.2</td><td>49.1</td><td>↓</td><td>↑</td></tr><tr><td>Japan</td><td>Jun-26</td><td>Index</td><td>54.8</td><td>54.5</td><td>53.4</td><td>49.0</td><td>↑</td><td>↑</td></tr><tr><td>Emerging Markets</td><td>May-26</td><td>Index</td><td>51.6</td><td>51.6</td><td>51.3</td><td>50.6</td><td>—</td><td>↑</td></tr><tr><td colspan="9">Manufacturing Utilization and Investment</td></tr><tr><td>Japan Manufacturing Utilization</td><td>Apr-26</td><td>Index</td><td>102.9</td><td>103.7</td><td>104.2</td><td>102.5</td><td>↓</td><td>↑</td></tr><tr><td>US Manufacturing Utilization</td><td>May-26</td><td>Value (%)</td><td>75.6</td><td>75.6</td><td>75.2</td><td>75.3</td><td>—</td><td>↓</td></tr><tr><td>US Industrial Equipment Investment</td><td>1Q26</td><td>YoY Growth</td><td>7.4%</td><td>8.1%</td><td>7.4%</td><td>6.8%</td><td>↓</td><td>↑</td></tr><tr><td>EU Manufacturing Utilization</td><td>1Q26</td><td>Value (%)</td><td>77.9</td><td>77.9</td><td>77.9</td><td>77.8</td><td>—</td><td>↑</td></tr><tr><td colspan="9">Japan Machine Tool Orders</td></tr><tr><td>Total Japan Machine Tool Orders</td><td>May-26</td><td>YoY Growth</td><td>37.5%</td><td>45.1%</td><td>32.2%</td><td>8.0%</td><td>↓</td><td>↑</td></tr><tr><td>from Japan</td><td>May-26</td><td>YoY Growth</td><td>37.3%</td><td>43.4%</td><td>17.8%</td><td>-0.2%</td><td>↓</td><td>↑</td></tr><tr><td>from China</td><td>May-26</td><td>YoY Growth</td><td>42.7%</td><td>33.2%</td><td>35.9%</td><td>17.1%</td><td>↑</td><td>↑</td></tr><tr><td>from Asia ex-China</td><td>May-26</td><td>YoY Growth</td><td>67.4%</td><td>60.9%</td><td>34.3%</td><td>5.6%</td><td>↑</td><td>↑</td></tr><tr><td>from EU</td><td>May-26</td><td>YoY Growth</td><td>-13.2%</td><td>35.6%</td><td>9.7%</td><td>1.3%</td><td>↓</td><td>↑</td></tr><tr><td>from North America</td><td>May-26</td><td>YoY Growth</td><td>4.2%</td><td>16.2%</td><td>27.3%</td><td>19.0%</td><td>↓</td><td>↑</td></tr><tr><td colspan="9">Japan Industrial Robot Export Volume</td></tr><tr><td>Total Industrial Robot Export</td><td>May-26</td><td>YoY Growth</td><td>9.1%</td><td>40.7%</td><td>27.9%</td><td>26.8%</td><td>↓</td><td>↑</td></tr><tr><td>to China</td><td>May-26</td><td>YoY Growth</td><td>5.7%</td><td>32.8%</td><td>26.1%</td><td>37.6%</td><td>↓</td><td>↓</td></tr><tr><td>to Asia ex-China</td><td>May-26</td><td>YoY Growth</td><td>22.4%</td><td>88.6%</td><td>33.0%</td><td>5.3%</td><td>↓</td><td>↑</td></tr><tr><td>to US</td><td>May-26</td><td>YoY Growth</td><td>5.8%</td><td>-5.8%</td><td>17.2%</td><td>92.4%</td><td>↑</td><td>↓</td></tr><tr><td>to EU</td><td>May-26</td><td>YoY Growth</td><td>10.8%</td><td>68.3%</td><td>37.4%</td><td>-8.8%</td><td>↓</td><td>↑</td></tr><tr><td colspan="9">Japan Automation Production and Order</td></tr><tr><td>Servo Motor Production</td><td>Apr-26</td><td>YoY Growth</td><td>11.0%</td><td>25.0%</td><td>18.5%</td><td>0.3%</td><td>↓</td><td>↑</td></tr><tr><td>PLC Production</td><td>Apr-26</td><td>YoY Growth</td><td>-35.1%</td><td>-6.6%</td><td>-20.6%</td><td>41.2%</td><td>↓</td><td>↓</td></tr><tr><td>Reducer Production</td><td>Apr-26</td><td>YoY Growth</td><td>10.3%</td><td>35.9%</td><td>19.6%</td><td>-8.7%</td><td>↓</td><td>↑</td></tr><tr><td>Robot Production</td><td>Apr-26</td><td>YoY Growth</td><td>17.3%</td><td>21.1%</td><td>18.8%</td><td>19.6%</td><td>↓</td><td>↓</td></tr><tr><td>Pneumatic Components Production</td><td>Apr-26</td><td>YoY Growth</td><td>31.1%</td><td>27.2%</td><td>24.0%</td><td>5.6%</td><td>↑</td><td>↑</td></tr><tr><td>Robot Order</td><td>Apr-26</td><td>YoY Growth</td><td>33.5%</td><td>23.1%</td><td>39.7%</td><td>41.1%</td><td>↑</td><td>↓</td></tr></table>

NBS, JMTBA, METI, Japan Ministry of Finance, US BEA, PMIII, Haver, Bloomberg, Wind, Bernstein analysis. Source: Momentum Tracker

CHINA  
EXHIBIT 2: China manufacturing PMI trend  
![](images/5c1fe0430689923f1bad2b407e54598f36afef9622cc380a6d4ae069a7309bf4.jpg)  
Source: Haver, Bloomberg, Bernstein analysis

EXHIBIT 3: Liquidity tracker: M1, TSF and entrusted & trust loan trends  
![](images/7084a8e77b8d7d005edc1fec635a975c5b9c9314ea39656836994dd3a995f3eb.jpg)  
Source: Haver, Bernstein analysis

EXHIBIT 4: China new order, new order/inventory, production and business expectation PMIs  
![](images/c48fc8f4caeaf4517f06b86725e3a157c48017a2cf4061a942a2747a5b96ef7c.jpg)  
Source: Haver, China National Bureau of Statistics, Bernstein analysis.

EXHIBIT 5: China emerging industries PMI (6-month moving average)  
China Emerging Industries PMI (6-month moving average)  
![](images/a85819444c0d82cec19ec286f94c679ed03644482057232bec77a39a8d0199b4.jpg)

Note: The EPMI includes 280 sample companies in seven industries including energy conservation and environmental protection, new generation information technology, biotechnology, high-end equipment manufacturing, new energy, new materials, and new energy automobile industry. The EPMI survey is a monthly survey, which is greatly affected by seasonal factors and has large data fluctuations. The comprehensive index and sub-indices of EPMI currently released are seasonally adjusted data.

Source: Wind, Chinese Academy of Science and Technology for Development, PMIII, Bernstein analysis

EXHIBIT 6: Value-add growth of high technology manufacturing and general manufacturing  
Value-add Growth of High Tech Mfg and General Mfg  
![](images/8201736a0ff2ee3f7efe317c13c05bca6c9513f5e011e21e922ae13ddd226fa3.jpg)  
Note: Pricing effect has been removed from the value-add growth rate. Source: NBS, Bernstein analysis.

EXHIBIT 7: Growth of industrial profit and inventory of finished goods in China (yoy)  
Growth of industrial profit and inventory of finished goods in China  
![](images/191d60d7f5d3ee509dcf70eb362ac39a4d371f957d6f3b0eb584d662660426bf.jpg)  
Source: Wind, National Bureau of Statistics of China, Bernstein analysis

EXHIBIT 8: Industrial profit trend  
Industrial Profit Growth (YTD, yoy) by Manufacturing Subsector in China  
![](images/0e36ca3d976b5789038c47ce49bb844a98417ae3faeef9796b69702931cd7401.jpg)  
Source: NBS, Haver, Bernstein analysis

EXHIBIT 9: Total Fixed Asset Investment (FAI), FAI in manufacturing, and FAI in purchase of equipment.  
Total FAI and Fixed Investment for Manufacturing and Purchase of Equipment (YTD Y/Y Growth)  
![](images/b2e6f80161bcc690e905c1addb7387f1ed7570ee889b42c25c39c3eea2486445.jpg)  
Total Investment in Fixed Assets (YTD Y/Y Growth)
Fixed Investment: Purchase of Equipment (YTD Y/Y Growth)  
Source: National Bureau of Statistics (NBS), Haver, Bernstein analysis

FAI in Manufacturing, Auto, and Electronics (YTD Y/Y Growth)  
![](images/c0f13e772cd88992a3e4f7d6fd3927c5c5a9bafb47d4a8cc2046d69676a31ada.jpg)  
Source: NBS, Haver, Bernstein analysis

EXHIBIT 11: Infrastructure investment in China is still growing, especially Railway-related investments  
FAI in Infrastructure, Railway and Road (YTD Y/Y Growth)  
![](images/c45df29e31d2fc6e6217ebf60183516f50fae79e8e0c6f86817cbbdfb49a3aec.jpg)  
Source: Haver, Bernstein analysis

EXHIBIT 12: Real estate development trend  
![](images/2f465d2e161700b0626f7f48c0ab41b4597c819ab4eba80ad2b75ead68995617.jpg)  
Source: NBS, Haver, Bernstein analysis

EXHIBIT 13: China industrial capacity utilization by quarter  
![](images/6731e3eff7d0b1294e24e8fafd7be07780914d3ca31ad8973660e24dc300a153.jpg)  
Source: Haver, Bernstein analysis

EXHIBIT 14: Power consumption growth.  
![](images/d048047dd8c308cf891cf2ac6ef6fd19e6c247fef79519fafa32f4d141bc2063.jpg)  
Note: No data in December and January
Source: Haver, Bernstein analysis.

## EXHIBIT 15: PPI and steel price trends

![](images/e02533fdd2a3510220e3016ee95c470d7c8f8d3f6618a016e714dadd945293a4.jpg)  
Note: Manufactured goods exclude mining, quarrying and raw materials.
Source: Haver, Bernstein analysis.

## Equipment sales and production

EXHIBIT 16: China factory automation shipment value growth trend by product (YoY)  
![](images/e3f1bd688f8892c347e2fff17204f55bfc1a4a34c167b5214618b2f2732c36df.jpg)  
Source: MIR Databank, Bernstein analysis

Japan machine tool orders from China

EXHIBIT 17: Japan machine tool orders from China and Y/Y growth.  
![](images/e286027e3e8a743c67da43c420e7d966d51f8511dbc20af7339c8f929bfae076.jpg)  
Note: We adjusted the value to local currency to reflect the true demand.
Source: Bloomberg, JMTBA, Bernstein analysis

EXHIBIT 18: Japan machine tool order growth contribution breakdown by industry (China)  
![](images/b6cfbb97e2171abc8a726cb3bc9d28b75bf85e629c68b0d8827e792832c319fc.jpg)  
Source: JMTBA, Bernstein analysis

EXHIBIT 19: China metal-cutting machine tool production and Y/Y growth  
![](images/8037751f5939797471ad412f65afbb4376bf6ea40e5e1d83466c17f398cf5113.jpg)  
Note: The year-over-year percent changes of the monthly volume data do not always match the published year-over-year percent changes because the monthly volume data come from enterprises that are not the same from year to year whereas the published growth rates are calculated from enterprises that are the same from year to year.  
Source: Haver, Bernstein analysis.  
Electric Motor - Industrial Output YTD Growth  
Industrial Robot - Industrial Output YTD Growth

EXHIBIT 20: Electric Motor: Industrial output YTD growth

![](images/17ade0eb02880d98c3f6df0841134435b93befed92e7c24c1662f28e2691da11.jpg)  
EXHIBIT 21: Industrial Robot: Industrial output YTD growth

Note: The published year-to-year percent changes of the monthly YTD volume series are not always the same as the calculated year-to-year percent changes because the monthly YTD volume data come from enterprises that are not the same from year to year whereas the published growth rates are calculated from enterprises that are the same from year to year.

Source: Haver, Bernstein analysis.

![](images/458967f52b2a344402d0cdb065aaca8374054bfdfdac1eee9559c9eee9d31fee.jpg)  
Note: The published year-to-year percent changes of the monthly YTD volume series are not always the same as the calculated year-to-year percent changes because the monthly YTD volume data come from enterprises that are not the same from year to year whereas the published growth rates are calculated from enterprises that are the same from year to year.
Source: Haver, Bernstein analysis

EXHIBIT 22: Metal-cutting Machine Tool: Industrial output YTD growth  
Metal-Cutting Machine Tool - Industrial Output YTD Growth  
![](images/2704be5906dc4861b22da8ee26a31a8063623577ff16e684807479b3550722eb.jpg)  
Note: The published year-to-year percent changes of the monthly YTD volume series are not always the same as the calculated year-to-year percent changes because the monthly YTD volume data come from enterprises that are not the same from year to year whereas the published growth rates are calculated from enterprises that are the same from year to year.
Source: Haver, Bernstein analysis.

EXHIBIT 24: Metal-shaping Machine Tool: Industrial output YTD growth  
Packaging Machinery - Industrial Output
YTD Growth  
EXHIBIT 23: Packaging Machinery: Industrial output YTD growth  
![](images/3b909cc58b978c00c16a5c51804c71f6077d0033474b297f53f4da469889ab4a.jpg)  
Note: The published year-to-year percent changes of the monthly YTD volume series are not always the same as the calculated year-to-year percent changes because the monthly YTD volume data come from enterprises that are not the same from year to year whereas the published growth rates are calculated from enterprises that are the same from year to year.
Source: Haver, Bernstein analysis.

![](images/eea1e5db01e9c7f95d66c64c01094ad386871b354f3bf501876e94edc3284bbd.jpg)  
EXHIBIT 25: Cement Producing Equipment: Industrial output YTD growth  
Metal-Shaping Machine Tool - Industrial Output YTD Growth  
Note: The published year-to-year percent changes of the monthly YTD volume series are not always the same as the calculated year-to-year percent changes because the monthly YTD volume data come from enterprises that are not the same from year to year whereas the published growth rates are calculated from enterprises that are the same from year to year.
Source: Haver; Bernstein analysis.

Cement Producing Equipment - Industrial Output YTD Growth  
![](images/ba72c250d76d6e2be32e4ea5d9df2ffd12825c74e0c6672e5ef1bcfd8091509b.jpg)  
Note: The published year-to-year percent changes of the monthly YTD volume series are not always the same as the calculated year-to-year percent changes because the monthly YTD volume data come from enterprises that ar

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
