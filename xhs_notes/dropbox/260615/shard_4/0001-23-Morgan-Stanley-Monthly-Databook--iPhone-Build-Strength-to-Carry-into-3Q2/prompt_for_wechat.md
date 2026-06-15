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
## Greater China Technology Hardware | Asia Pacific

# Monthly Databook: iPhone Build Strength to Carry into 3Q26 for New Premium Models Debut

## Key Takeaways

2Q26e iPhone builds estimate stays at 52mn units (down 7% QoQ, up 12% YoY).  
3Q26e iPhone builds introduced at 54mn units (up 4% QoQ, down 2% YoY).  
We keep 2Q26e iPad builds at 13mn units (up 8% QoQ, down 10% YoY).  
3Q26 iPad builds introduced at 13mn units (flat QoQ, down 7% YoY).

We keep our 2Q26 iPhone build estimate at 52mn units, down 7% QoQ (+12% YoY), vs. the historical 15-25% QoQ declines previously seen for 2Q. Our checks suggest better-than-seasonal builds this quarter from major assembly partners including Hon Hai, with iPhone shipments in May up MoM. This indicates to us that iPhone sell-through continues to trend well amid memory cost hikes.

We introduce our preliminary 3Q26 iPhone build estimate at 54mn units, up 4% QoQ (-2% YoY). The slower run rate mainly reflects new model SKUs shifting to the premium segment (18 Pro/Pro Max and iPhone Fold), while the iPhone 18 model is scheduled for introduction in 1H27. We currently expect 7-8mn iPhone Fold builds in 2H26 and will closely monitor the ramp-up progress.

We keep our 2Q26 iPad build forecast at 13mn units, up 8% QoQ (-10% YoY). The YoY decline reflects a higher base in 2Q25 given product launches. We introduce our preliminary 3Q26 iPad build forecast at 13mn units, flat QoQ (-7% YoY), as we expect stocking to remain normal, although memory and material price hikes could have an impact.

Exhibit 1: iPhone Sell-in Data, by Quarter

<table><tr><td>Unit units</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>2022</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>2023</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td><td>2Q26e</td><td>3Q26e</td></tr><tr><td colspan="24">iPhone Sell in</td></tr><tr><td>iPhone SE1 (SE 5G/16e/17e)</td><td>3.0</td><td>13.0</td><td>6.0</td><td>2.0</td><td>24.0</td><td>1.0</td><td>2.5</td><td>5.0</td><td>3.0</td><td>11.5</td><td>1.0</td><td>2.0</td><td>5.0</td><td>3.0</td><td>11.0</td><td>4.0</td><td>9.0</td><td>4.0</td><td>1.0</td><td>18.0</td><td>2.0</td><td>10.0</td><td>8.0</td></tr><tr><td>iPhone XR</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 11</td><td>1.0</td><td>1.0</td><td>0.5</td><td>0.5</td><td>3.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 12 mini (5.4&quot;)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 12 (5.1&quot;)</td><td>2.0</td><td>1.0</td><td>1.0</td><td>0.5</td><td>4.5</td><td>0.5</td><td>-</td><td>0.5</td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 12 Pro (5.1&quot;)</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>2.5</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 12 Pro Mat (6.7&quot;)</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>2.5</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 13 mini (5.4&quot;)</td><td>5.0</td><td>2.0</td><td>2.0</td><td>1.0</td><td>10.0</td><td>1.0</td><td>0.5</td><td>-</td><td>-</td><td>1.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 13 (5.1&quot;)</td><td>10.0</td><td>11.5</td><td>8.0</td><td>3.0</td><td>38.5</td><td>1.0</td><td>0.5</td><td>-</td><td>-</td><td>1.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 13 Pro (5.1&quot;)</td><td>13.0</td><td>8.0</td><td>6.0</td><td>3.5</td><td>30.5</td><td>1.0</td><td>2.0</td><td>1.0</td><td>-</td><td>4.0</td><td>0.5</td><td>0.5</td><td>-</td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 13 Pro Mat (5.7&quot;)</td><td>12.0</td><td>7.5</td><td>5.0</td><td>4.0</td><td>28.5</td><td>2.0</td><td>2.0</td><td>1.0</td><td>-</td><td>5.0</td><td>0.5</td><td>0.5</td><td>-</td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 14 (6.1&quot;)</td><td></td><td></td><td>6.5</td><td>13.0</td><td>19.5</td><td>7.0</td><td>4.0</td><td>5.0</td><td>2.0</td><td>18.0</td><td>1.0</td><td>0.5</td><td>-</td><td>-</td><td>1.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 14 Plus (5.7&quot;)</td><td></td><td></td><td>2.0</td><td>13.5</td><td>15.5</td><td>5.0</td><td>3.0</td><td>1.0</td><td>1.0</td><td>10.0</td><td>1.0</td><td>0.5</td><td>-</td><td>-</td><td>1.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 14 Pro (5.1&quot;)</td><td></td><td></td><td>6.0</td><td>16.5</td><td>22.0</td><td>10.5</td><td>12.0</td><td>7.0</td><td>3.0</td><td>37.0</td><td>2.0</td><td>2.0</td><td>1.5</td><td>1.0</td><td>6.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>-</td><td>3.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 14 Pro Mat (6.7&quot;)</td><td></td><td></td><td>6.0</td><td>19.0</td><td>25.0</td><td>19.5</td><td>14.0</td><td>9.0</td><td>4.0</td><td>46.5</td><td>2.0</td><td>2.0</td><td>1.0</td><td>1.0</td><td>6.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>-</td><td>3.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 15 (6.1&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6.0</td><td>12.0</td><td>18.0</td><td>6.0</td><td>5.0</td><td>4.0</td><td>1.0</td><td>16.0</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>2.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 15 Plus (6.7&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5.0</td><td>10.0</td><td>15.0</td><td>4.0</td><td>3.0</td><td>1.0</td><td>1.0</td><td>9.0</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>2.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPhone 15 Pro (5.1&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td><td>16.0</td><td>24.0</td><td>12.0</td><td>10.0</td><td>8.5</td><td>2.0</td><td>32.5</td><td>2.0</td><td>2.0</td><td>2.0</td><td>1.0</td><td>7.0</td><td>1.0</td><td>1.0</td><td>-</td><td>-</td></tr><tr><td>iPhone 15 Pro Mat (6.7&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>2.0</td><td>24.0</td><td>26.0</td><td>18.0</td><td>13.0</td><td>10.5</td><td>3.0</td><td>44.5</td><td>3.0</td><td>3.0</td><td>2.0</td><td>1.0</td><td>9.0</td><td>1.0</td><td>1.0</td><td>-</td><td>-</td></tr><tr><td>iPhone 16 (5.1&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6.0</td><td>12.0</td><td>18.0</td><td>5.0</td><td>4.0</td><td>4.0</td><td>1.0</td><td>14.0</td><td>2.0</td><td>2.0</td><td>1.0</td><td></td></tr><tr><td>iPhone 16 Plus (6.7&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5.0</td><td>6.0</td><td>11.0</td><td>4.0</td><td>3.0</td><td>1.0</td><td>1.0</td><td>8.0</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>iPhone 16 Pro (5.2&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td><td>17.0</td><td>25.0</td><td>11.5</td><td>9.5</td><td>4.0</td><td>2.0</td><td>27.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td></td></tr><tr><td>iPhone 16 Pro Mat (5.9&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4.0</td><td>26.0</td><td>30.0</td><td>16.5</td><td>13.0</td><td>10.0</td><td>4.0</td><td>43.5</td><td>5.0</td><td>3.0</td><td>2.0</td></tr><tr><td>iPhone 17 (5.1&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6.0</td><td>16.0</td><td>22.0</td><td>10.0</td><td>8.0</td></tr><tr><td>iPhone Air (5.7&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4.0</td><td>4.0</td><td>8.0</td><td></td><td></td></tr><tr><td>iPhone 17 Pro (5.3&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td><td>22.0</td><td>30.0</td><td>18.0</td><td>13.0</td></tr><tr><td>iPhone 17 Pro Mat (6.9&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>7.0</td><td>23.0</td><td>30.0</td><td>15.0</td><td>12.0</td></tr><tr><td>iPhone 18 Pro (5.3&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td></tr><tr><td>iPhone 18 Pro Mat (6.9&quot;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>8.0</td></tr><tr><td>iPhone Fold</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.0</td></tr><tr><td>Total</td><td>54.0</td><td>45.0</td><td>50.0</td><td>17.0</td><td>226.0</td><td>54.0</td><td>41.0</td><td>50.0</td><td>75.0</td><td>220.0</td><td>48.0</td><td>39.0</td><td>54.0</td><td>73.0</td><td>214.0</td><td>50.0</td><td>46.5</td><td>55.0</td><td>76.0</td><td>227.5</td><td>56.0</td><td>52.0</td><td>54.0</td></tr><tr><td>YoY</td><td>7%</td><td>1%</td><td>0%</td><td>-9%</td><td>-2%</td><td>0%</td><td>-9%</td><td>0%</td><td>-3%</td><td>-3%</td><td>-11%</td><td>-5%</td><td>8%</td><td>-3%</td><td>-3%</td><td>-4%</td><td>-15%</td><td>2%</td><td>4%</td><td>6%</td><td>-12%</td><td>12%</td><td>-2%</td></tr><tr><td>QoQ</td><td>-36%</td><td>-17%</td><td>11%</td><td>54%</td><td></td><td>-30%</td><td>-24%</td><td>22%</td><td>50%</td><td></td><td>-36%</td><td>-19%</td><td>38%</td><td>35%</td><td></td><td>-32%</td><td>-7%</td><td>18%</td><td>38%</td><td></td><td>-26%</td><td>-7%</td><td>4%</td></tr></table>

Source: Company data, MS. e = MS Asia Research estimates based on company announcements and supply chain checks.

MS TAIWAN LIMITED+

## Sharon Shih

Equity Analyst

Sharon.Shih@morganstanley.com +886 2 2730-2865

## Derrick Yang

Equity Analyst

Derrick.Yang@morganstanley.com +886 2 2730-2862

## Howard Kao

Equity Analyst

Howard.Kao@morganstanley.com +886 2 2730-2989

MS ASIA LIMITED+

## Andy Meng, CFA

Equity Analyst

Andy.Meng@morganstanley.com +852 2239-7689

MS TAIWAN LIMITED+

## Vivi Huang

Research Associate

Vivi.Huang@morganstanley.com +886 2 2730-2860

## Irene Yen

Research Associate

Irene.Yen@morganstanley.com +886 2 2730-2869

MS ASIA LIMITED+

## Betty Chen

Research Associate

Betty.H.Chen@morganstanley.com +852 2239-7213

## Asia Summer School 2026

![](images/0455946f612eac8945b8320bf986adc4edfee6b236d984e8276ddb1471a3e3b6.jpg)

## GREATER CHINA TECHNOLOGY HARDWARE

Asia Pacific

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Exhibit 2: iPad Sell-in Data, by Quarter

<table><tr><td>Unit units</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>2022</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>2023</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td><td>2Q26e</td><td>3Q26e</td></tr><tr><td>iPad Sell-in</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad mini</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad mini</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad miniS</td><td>1.5</td><td>1.5</td><td>1.0</td><td>1.0</td><td>5.0</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad miniS</td><td></td><td></td><td></td><td></td><td></td><td>1.0</td><td>2.5</td><td>3.0</td><td>2.0</td><td>8.5</td><td>1.0</td><td>1.0</td><td>2.0</td><td>3.0</td><td>7.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad miniY</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td>1.0</td><td>1.5</td><td>2.5</td><td>2.0</td><td>2.0</td><td>1.5</td><td>0.5</td><td>6.0</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>The iPad (8&#x27;7&#x27;)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>The iPad 10&#x27;12&quot;</td><td>4.5</td><td>3.3</td><td>3.5</td><td>-</td><td>11.3</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>The iPad (10&#x27;9&#x27;)</td><td>-</td><td>-</td><td>3.0</td><td>7.0</td><td>10.0</td><td>4.0</td><td>4.5</td><td>4.5</td><td>6.0</td><td>19.0</td><td>3.5</td><td>2.5</td><td>5.5</td><td>5.5</td><td>17.0</td><td>5.5</td><td>6.0</td><td>6.0</td><td>6.0</td><td>23.5</td><td>5.5</td><td>6.0</td><td>6.0</td></tr><tr><td>iPad Air (10 S10/9&#x27;11&quot;)</td><td>3.5</td><td>5.0</td><td>4.0</td><td>3.0</td><td>15.5</td><td>3.0</td><td>2.0</td><td>3.0</td><td>4.0</td><td>12.0</td><td>2.0</td><td>2.0</td><td>3.0</td><td>2.5</td><td>9.5</td><td>2.5</td><td>3.0</td><td>3.0</td><td>3.5</td><td>12.0</td><td>3.0</td><td>3.5</td><td>3.5</td></tr><tr><td>iPad Air (12 9&#x27;13&#x27;F)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.0</td><td>2.0</td><td>2.0</td><td>1.5</td><td>6.5</td><td>1.0</td><td>1.5</td><td>1.5</td><td>2.0</td><td>6.0</td><td>2.0</td><td>2.0</td><td>2.0</td></tr><tr><td>iPad Pro 12&#x27;3&quot;</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 10&#x27;5&quot;</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 12&#x27;5&#x27; Face ID (2018)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 11&#x27; Face ID (2018)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 12&#x27;5&#x27; Face ID (2020)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 11&#x27; Face ID (2020)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iPad Pro 12&#x27;5&#x27; Face ID (2021)</td><td>1.5</td><td>1.0</td><td>0.5</td><td>-</td><td>3.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>iPad Pro 11&#x27; Face ID (2021)</td><td>1.0</td><td>1.0</td><td>0.5</td><td>-</td><td>2.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</t

[中间内容因长度限制已省略]

ptical Fibre and Cable JSC Ltd (601869.SS)</td><td>U (10/13/2021)</td><td>Rmb436.50</td></tr><tr><td>Yangtze Optical Fibre and Cable JSC Ltd (6869.HK)</td><td>E (04/20/2023)</td><td>HK$226.60</td></tr><tr><td>Yongxin Optics Co Ltd (603297.SS)</td><td>E (11/15/2022)</td><td>Rmb117.30</td></tr><tr><td>Zhejiang Crystal-Optech Co Ltd (002273.SZ)</td><td>O (11/15/2022)</td><td>Rmb32.39</td></tr><tr><td>Zhongji Innolight Co Ltd (300308.SZ)</td><td>++</td><td>Rmb1,149.00</td></tr><tr><td>ZTE Corporation (0763.HK)</td><td>O (06/04/2026)</td><td>HK$26.00</td></tr><tr><td>ZTE Corporation (000063.SZ)</td><td>E (06/04/2026)</td><td>Rmb36.35</td></tr></table>

Derrick Yang

<table><tr><td>Accton Technology Corporation (2345.TW)</td><td>O (06/06/2024)</td><td>NT$2,335.00</td></tr><tr><td>Advantech (2395.TW)</td><td>O (01/20/2021)</td><td>NT$473.00</td></tr><tr><td>AirTAC International (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,290.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$23.50</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$2,310.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb5.57</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,475.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$2,295.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$196.00</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$64.40</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$323.50</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$48.55</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$6,910.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb41.14</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$91.30</td></tr><tr><td>Sanan Optoelectronics (600703.SS)</td><td>U (08/21/2023)</td><td>Rmb13.92</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb4.55</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb7.51</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb196.30</td></tr></table>

Howard Kao

<table><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$36.70</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$785.00</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$36.35</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$7.36</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$342.00</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$1,320.00</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb57.86</td></tr><tr><td>Lenovo (0992.HK)</td><td>E (11/16/2025)</td><td>HK$22.34</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$2,240.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$819.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$93.10</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$372.00</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb151.28</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb379.50</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$902.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$156.00</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$4,850.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$855.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$552.00</td></tr><tr><td colspan="3">Sharon Shih</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,405.00</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$1,055.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$205.50</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$2,215.00</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,825.00</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb70.13</td></tr><tr><td>Foxconn Technology (2354.TW)</td><td>U (04/23/2025)</td><td>NT$57.00</td></tr><tr><td>GoerTek Inc (002241.SZ)</td><td>U (04/23/2025)</td><td>Rmb23.01</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$260.50</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$2,195.00</td></tr><tr><td>Lingyi Itech Guangdong Co (002600.SZ)</td><td>U (04/23/2025)</td><td>Rmb14.01</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$217.00</td></tr><tr><td>Luxshare Precision Industry Co., Ltd. (002475.SZ)</td><td>O (10/24/2016)</td><td>Rmb63.76</td></tr><tr><td>Sunonwealth Electric Machine Industry Co (2421.TW)</td><td>E (02/23/2024)</td><td>NT$144.00</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$238.50</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$352.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
