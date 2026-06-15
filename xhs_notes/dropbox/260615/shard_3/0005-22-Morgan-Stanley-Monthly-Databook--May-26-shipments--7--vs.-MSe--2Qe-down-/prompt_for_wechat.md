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

# Monthly Databook: May-26 shipments -7% vs. MSe; 2Qe down 3%; introduce 3Qe at -1% q/q

## Key Takeaways

Top five ODMs' May 2026 NB shipments were 9.3m units (+2% m/m, -12% y/y), 7% below our estimate.  
We estimate June 2026 NB builds at 10.9m units (+17% m/m, -16% y/y).  
We cut our 2Q26 NB build estimate by 3% to 29.3m units (flat q/q, -12% y/y).  
We also introduce our 3Q26 NB build estimate at 29m units (-1% q/q, -15% y/y).

## Overall May ODM notebook shipments came in 7% below our estimate:

Component constraints remain the key bottlenecks, forcing ODMs to prioritize higher-end, more profitable models. We forecast June NB builds at 10.9m (+17% q/q, -16% y/y) due to quarter-end pull-ins.

We lower our 2Q notebook build estimate by 3% to 29.3m units (flat q/q, -12% y/y): The flat q/q growth is 12ppts below the 15Y avg seasonality of +12% q/q in 2Q, which is based on ODMs' latest guidance. We believe any deviation from the guidance will mainly stem from component availability.

We stay cautious on demand downside in 2H, although it is difficult to predict the exact timing. PC OEMs' mix will continue to shift toward more high-end segments, as they prioritize putting limited components into premium models to drive higher profits. We introduce our 3Q notebook build estimate at 29m units (-1% q/q, -15% y/y), which is sub-seasonal vs. the 15Y avg seasonality of +5% q/q in 3Q. Actual shipments will continue to depend on component availability.

Exhibit 1: Monthly NB shipments for top five NB ODMs

<table><tr><td>Shipment (unit: k)</td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25E</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>May-26E</td><td>Diff.</td><td>Jun-26E</td></tr><tr><td>Quanta</td><td>2,800</td><td>3,100</td><td>4,900</td><td>3,300</td><td>3,800</td><td>5,000</td><td>4,000</td><td>4,100</td><td>4,600</td><td>3,500</td><td>3,500</td><td>3,900</td><td>2,700</td><td>2,000</td><td>5,300</td><td>3,500</td><td>3,500</td><td>3,500</td><td>0%</td><td>3,500</td></tr><tr><td>Wistron</td><td>1,500</td><td>1,500</td><td>1,900</td><td>1,700</td><td>1,800</td><td>2,400</td><td>2,000</td><td>2,200</td><td>2,200</td><td>2,100</td><td>2,200</td><td>2,600</td><td>1,700</td><td>1,600</td><td>2,800</td><td>1,800</td><td>1,700</td><td>2,000</td><td>-15%</td><td>2,200</td></tr><tr><td>Others</td><td>1,500</td><td>1,600</td><td>1,900</td><td>1,700</td><td>1,800</td><td>2,100</td><td>1,700</td><td>1,800</td><td>1,900</td><td>1,600</td><td>1,700</td><td>2,000</td><td>1,700</td><td>1,500</td><td>2,200</td><td>1,500</td><td>1,500</td><td>1,800</td><td>-17%</td><td>2,200</td></tr><tr><td>Compal</td><td>2,000</td><td>2,100</td><td>2,900</td><td>2,200</td><td>2,400</td><td>2,500</td><td>2,300</td><td>2,300</td><td>2,500</td><td>2,100</td><td>2,300</td><td>2,400</td><td>1,600</td><td>1,500</td><td>2,800</td><td>1,800</td><td>2,000</td><td>2,100</td><td>-5%</td><td>2,200</td></tr><tr><td>Pegatron</td><td>610</td><td>575</td><td>700</td><td>610</td><td>775</td><td>990</td><td>750</td><td>825</td><td>825</td><td>775</td><td>710</td><td>925</td><td>700</td><td>425</td><td>675</td><td>525</td><td>575</td><td>625</td><td>-5%</td><td>750</td></tr><tr><td>Total</td><td>8,410</td><td>8,875</td><td>12,300</td><td>9,510</td><td>10,575</td><td>12,990</td><td>10,750</td><td>11,225</td><td>12,025</td><td>10,075</td><td>10,410</td><td>11,825</td><td>8,400</td><td>7,025</td><td>13,775</td><td>9,125</td><td>9,275</td><td>10,025</td><td>-7%</td><td>10,850</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quanta</td><td>-35%</td><td>11%</td><td>58%</td><td>-33%</td><td>15%</td><td>32%</td><td>-20%</td><td>2%</td><td>12%</td><td>-24%</td><td>0%</td><td>11%</td><td>-31%</td><td>-26%</td><td>165%</td><td>-34%</td><td>0%</td><td>0%</td><td></td><td>0%</td></tr><tr><td>Wistron</td><td>-17%</td><td>0%</td><td>27%</td><td>-11%</td><td>6%</td><td>33%</td><td>-17%</td><td>10%</td><td>0%</td><td>-5%</td><td>5%</td><td>18%</td><td>-35%</td><td>-6%</td><td>75%</td><td>-36%</td><td>-6%</td><td>11%</td><td></td><td>29%</td></tr><tr><td>Others</td><td>-25%</td><td>7%</td><td>19%</td><td>-11%</td><td>6%</td><td>17%</td><td>-19%</td><td>6%</td><td>6%</td><td>-16%</td><td>6%</td><td>18%</td><td>-15%</td><td>-12%</td><td>47%</td><td>-32%</td><td>0%</td><td>20%</td><td></td><td>47%</td></tr><tr><td>Compal</td><td>-13%</td><td>5%</td><td>38%</td><td>-24%</td><td>9%</td><td>4%</td><td>-8%</td><td>0%</td><td>9%</td><td>-16%</td><td>10%</td><td>4%</td><td>-33%</td><td>-6%</td><td>87%</td><td>-36%</td><td>11%</td><td>17%</td><td></td><td>10%</td></tr><tr><td>Pegatron</td><td>-19%</td><td>-6%</td><td>22%</td><td>-13%</td><td>27%</td><td>28%</td><td>-24%</td><td>10%</td><td>0%</td><td>-6%</td><td>-8%</td><td>30%</td><td>-24%</td><td>-39%</td><td>59%</td><td>-22%</td><td>10%</td><td>19%</td><td></td><td>30%</td></tr><tr><td>Total</td><td>-25%</td><td>6%</td><td>39%</td><td>-23%</td><td>11%</td><td>23%</td><td>-17%</td><td>4%</td><td>7%</td><td>-16%</td><td>3%</td><td>14%</td><td>-29%</td><td>-16%</td><td>96%</td><td>-34%</td><td>2%</td><td>10%</td><td></td><td>17%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quanta</td><td>-3%</td><td>7%</td><td>4%</td><td>3%</td><td>-5%</td><td>11%</td><td>18%</td><td>-5%</td><td>-6%</td><td>9%</td><td>-3%</td><td>-9%</td><td>-4%</td><td>-35%</td><td>8%</td><td>6%</td><td>-8%</td><td>-8%</td><td></td><td>-30%</td></tr><tr><td>Wistron</td><td>15%</td><td>7%</td><td>0%</td><td>6%</td><td>6%</td><td>33%</td><td>25%</td><td>29%</td><td>16%</td><td>17%</td><td>29%</td><td>44%</td><td>13%</td><td>7%</td><td>47%</td><td>6%</td><td>-6%</td><td>11%</td><td></td><td>-8%</td></tr><tr><td>Others</td><td>0%</td><td>23%</td><td>12%</td><td>13%</td><td>6%</td><td>24%</td><td>0%</td><td>6%</td><td>6%</td><td>-6%</td><td>0%</td><td>0%</td><td>13%</td><td>-6%</td><td>16%</td><td>-12%</td><td>-17%</td><td>0%</td><td></td><td>5%</td></tr><tr><td>Compal</td><td>-9%</td><td>-9%</td><td>-3%</td><td>-21%</td><td>-17%</td><td>-17%</td><td>-8%</td><td>-21%</td><td>-14%</td><td>-25%</td><td>-15%</td><td>4%</td><td>-20%</td><td>-29%</td><td>-3%</td><td>-18%</td><td>-17%</td><td>-13%</td><td></td><td>-12%</td></tr><tr><td>Pegatron</td><td>16%</td><td>53%</td><td>8%</td><td>16%</td><td>6%</td><td>28%</td><td>-3%</td><td>-6%</td><td>0%</td><td>35%</td><td>14%</td><td>23%</td><td>15%</td><td>-26%</td><td>-4%</td><td>-14%</td><td>-26%</td><td>-19%</td><td></td><td>-24%</td></tr><tr><td>Total</td><td>0%</td><td>7%</td><td>3%</td><td>-1%</td><td>-4%</td><td>10%</td><td>8%</td><td>-2%</td><td>-2%</td><td>0%</td><td>1%</td><td>6%</td><td>0%</td><td>-21%</td><td>12%</td><td>-4%</td><td>-12%</td><td>-5%</td><td></td><td>-16%</td></tr></table>

Source: Company data, MS. E = MS estimates. "Others" are other leaders.

MS TAIWAN LIMITED+

## Howard Kao

Equity Analyst

Howard.Kao@morganstanley.com +886 2 2730-2989

## Sharon Shih

Equity Analyst

Sharon.Shih@morganstanley.com +886 2 2730-2865

## Irene Yen

Research Associate

Irene.Yen@morganstanley.com +886 2 2730-2869

## Asia Summer School 2026

![](images/c384b6f3793f2f1ddd84f938d23ad9cb6a7912780a082c579af0578a59ff257f.jpg)

## GREATER CHINA TECHNOLOGY HARDWARE

## Asia Pacific

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Exhibit 2: Quarterly NB shipments for top five NB ODMs

<table><tr><td>Shipment (unit: k)</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>1Q26E</td><td>Diff.</td><td>2Q26E</td><td>2Q26E</td><td>Diff.</td><td>3Q26E</td></tr><tr><td>Quanta</td><td>10,500</td><td>11,700</td><td>12,600</td><td>11,100</td><td>10,800</td><td>12,100</td><td>12,700</td><td>10,900</td><td>10,000</td><td>9,000</td><td>11%</td><td>10,500</td><td>10,500</td><td>0%</td><td>10,800</td></tr><tr><td>Wistron</td><td>4,600</td><td>5,100</td><td>5,200</td><td>5,300</td><td>4,900</td><td>5,900</td><td>6,400</td><td>6,900</td><td>6,100</td><td>5,400</td><td>13%</td><td>5,700</td><td>5,800</td><td>-2%</td><td>5,500</td></tr><tr><td>Others</td><td>4,500</td><td>4,900</td><td>5,200</td><td>5,400</td><td>5,000</td><td>5,600</td><td>5,400</td><td>5,300</td><td>5,400</td><td>4,400</td><td>23%</td><td>5,200</td><td>5,500</td><td>-5%</td><td>4,500</td></tr><tr><td>Compal</td><td>7,500</td><td>8,700</td><td>8,300</td><td>7,800</td><td>7,000</td><td>7,100</td><td>7,100</td><td>6,800</td><td>5,900</td><td>5,500</td><td>7%</td><td>6,000</td><td>6,500</td><td>-8%</td><td>6,400</td></tr><tr><td>Pegatron</td><td>1,550</td><td>2,030</td><td>2,475</td><td>1,950</td><td>1,885</td><td>2,375</td><td>2,400</td><td>2,410</td><td>1,800</td><td>2,050</td><td>-12%</td><td>1,850</td><td>2,000</td><td>-8%</td><td>1,800</td></tr><tr><td>Total</td><td>28,650</td><td>32,430</td><td>33,775</td><td>31,550</td><td>29,585</td><td>33,075</td><td>34,000</td><td>32,310</td><td>29,200</td><td>26,350</td><td>11%</td><td>29,250</td><td>30,300</td><td>-3%</td><td>29,000</td></tr><tr><td>QoQ %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quanta</td><td>1%</td><td>11%</td><td>8%</td><td>-12%</td><td>-3%</td><td>12%</td><td>5%</td><td>-14%</td><td>-8%</td><td>-17%</td><td></td><td>5%</td><td>5%</td><td></td><td>3%</td></tr><tr><td>Wistron</td><td>-13%</td><td>11%</td><td>2%</td><td>2%</td><td>-8%</td><td>20%</td><td>8%</td><td>8%</td><td>-12%</td><td>-22%</td><td></td><td>-7%</td><td>-5%</td><td></td><td>-4%</td></tr><tr><td>Others</td><td>0%</td><td>9%</td><td>6%</td><td>4%</td><td>-7%</td><td>12%</td><td>-4%</td><td>-2%</td><td>2%</td><td>-17%</td><td></td><td>-4%</td><td>2%</td><td></td><td>-13%</td></tr><tr><td>Compal</td><td>-10%</td><td>16%</td><td>-5%</td><td>-6%</td><td>-10%</td><td>1%</td><td>0%</td><td>-4%</td><td>-13%</td><td>-19%</td><td></td><td>2%</td><td>10%</td><td></td><td>7%</td></tr><tr><td>Pegatron</td><td>-6%</td><td>31%</td><td>22%</td><td>-21%</td><td>-3%</td><td>26%</td><td>1%</td><td>0%</td><td>-25%</td><td>-15%</td><td></td><td>3%</td><td>11%</td><td></td><td>-3%</td></tr><tr><td>Total</td><td>-5%</td><td>13%</td><td>4%</td><td>-7%</td><td>-6%</td><td>12%</td><td>3%</td><td>-5%</td><td>-10%</td><td>-18%</td><td></td><td>0%</td><td>4%</td><td></td><td>-1%</td></tr><tr><td>YoY%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quanta</td><td>-3%</td><td>-7%</td><td>-4%</td><td>7%</td><td>3%</td><td>3%</td><td>1%</td><td>-2%</td><td>-7%</td><td>-17%</td><td></td><td>-13%</td><td>-13%</td><td></td><td>-15%</td></tr><tr><td>Wistron</td><td>18%</td><td>11%</td><td>0%</td><td>0%</td><td>7%</td><td>16%</td><td>23%</td><td>30%</td><td>24%</td><td>10%</td><td></td><td>-3%</td><td>-2%</td><td></td><td>-14%</td></tr><tr><td>Others</td><td>2%</td><td>0%</td><td>6%</td><td>20%</td><td>11%</td><td>14%</td><td>4%</td><td>-2%</td><td>8%</td><td>-12%</td><td></td><td>-7%</td><td>-2%</td><td></td><td>-17%</td></tr><tr><td>Compal</td><td>-1%</td><td>0%</td><td>-11%</td><td>-6%</td><td>-7%</td><td>-18%</td><td>-14%</td><td>-13%</td><td>-16%</td><td>-21%</td><td></td><td>-15%</td><td>-8%</td><td></td><td>-10%</td></tr><tr><td>Pegatron</td><td>-9%</td><td>-2%</td><td>-1%</td><td>18%</td><td>22%</td><td>17%</td><td>-3%</td><td>24%</td><td>-5%</td><td>9%</td><td></td><td>-22%</td><td>-16%</td><td></td><td>-25%</td></tr><tr><td>Total</td><td>1%</td><td>-1%</td><td>-4%</td><td>5%</td><td>3%</td><td>2%</td><td>1%</td><td>2%</td><td>-1%</td><td>-11%</td><td></td><td>-12%</td><td>-8%</td><td></td><td>-15%</td></tr></table>

Source: Company data, MS. E = MS estimates. "Others" are other leaders.

## Valuation Methodology and Risks

## Compal Electronics (2324.TW)

Base case, residual income model. Our key assumptions include a cost of equity of 9.1% (beta 1.3, equity risk premium 6.0%, and risk-free rate 1.5%), a medium-term growth rate of 5.0%, and a long-term earnings growth rate of 3.0%.

## Risks to Upside

■ Stronger-than-expected NB and smartphone demand  
■ Further share gains in iPad  
■ Margin expansion thanks to better scale

## Risks to Downside

■ Weaker-than-expected NB demand  
■ Margin contraction from sales shortfall and fierce price competition  
■ Weaker-than-expected iPad shipments

## Quanta Computer Inc. (2382.TW)

Base case, residual income model. Key assumptions include a cost of equity of 9.0% (beta of 1.2, equity premium of 6.0% and risk-free rate of 1.5%), an 8.5% medium-term growth rate, and a 3% terminal growth rate.

## Risks to Upside

■ Stronger-than-expected NB demand  
■ Stronger-than-expected Apple Watch demand  
■ Stronger-than-expected server demand  
■ Faster-than-expected AI server penetration

## Risks to Downside

■ Weaker-than-expected NB demand  
■ Softer-than-expected Apple Watch demand  
■ Weak margin performance owing to rising labor costs and sales shortfalls  
■ Fierce price competition in the mega data center segment  
■ Slower-than-expected AI server penetration

## Wistron Corporation (3231.TW)

Base case, residual income valuation. Key assumptions: 8.7% cost of equity, 7.0% medium-term growth rate and 3% terminal growth rate.

## Risks to Upside

■ Faster-than-expected divestiture of consumer electronics business  
■ Stronger-than-expected NB demand  
■ Margin expansion from better product mix  
■ Faster-than-expected AI server penetration

## Risks to Downside

■ Slower-than-expected divestiture of consumer electronics business  
■ Weaker-than-expected NB demand  
■ Margin contraction from sales shortfall and fierce competition  
■ Slower-than-expected AI server penetration

## Pegatron Corporation (4938.TW)

Base case, sum-of-the-parts. Recurring core business earnings: 9x 2027e P/E, within ODMs' historical trading range of 8x to 12x since 2011, and below Pegatron's five-year average of 11.8x. We view our target P/E multiple as fair, reflecting a weaker end demand outlook for Pegatron's smartphone and PC business. We value its stakes in AsRock, Kinsus and Azure based on their market values in proportion to Pegatron's holdings.

## Risks to Upside

■ Better-than-expected iPhone volumes.  
■ Stronger PC shipments as a result of better component supply.  
■ Better-than-expected demand from EVs.

## Risks to Downside

■ Weaker iPhone demand.  
■ Margin erosion from poor resource planning.  
■ Lower contribution from non-PC products.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please con

[中间内容因长度限制已省略]

 JSC Ltd (601869.SS)</td><td>U (10/13/2021)</td><td>Rmb436.50</td></tr><tr><td>Yangtze Optical Fibre and Cable JSC Ltd (6869.HK)</td><td>E (04/20/2023)</td><td>HK$226.60</td></tr><tr><td>Yongxin Optics Co Ltd (603297.SS)</td><td>E (11/15/2022)</td><td>Rmb117.30</td></tr><tr><td>Zhejiang Crystal-Optech Co Ltd (002273.SZ)</td><td>O (11/15/2022)</td><td>Rmb32.39</td></tr><tr><td>Zhongji Innolight Co Ltd (300308.SZ)</td><td>++</td><td>Rmb1,149.00</td></tr><tr><td>ZTE Corporation (0763.HK)</td><td>O (06/04/2026)</td><td>HK$26.00</td></tr><tr><td>ZTE Corporation (000063.SZ)</td><td>E (06/04/2026)</td><td>Rmb36.35</td></tr><tr><td colspan="3">Derrick Yang</td></tr><tr><td>Accton Technology Corporation (2345.TW)</td><td>O (06/06/2024)</td><td>NT$2,335.00</td></tr><tr><td>Advantech (2395.TW)</td><td>O (01/20/2021)</td><td>NT$473.00</td></tr><tr><td>AirTAC International (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,290.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$23.50</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$2,310.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb5.57</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,475.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$2,295.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$196.00</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$64.40</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$323.50</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$48.55</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$6,910.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb41.14</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$91.30</td></tr><tr><td>Sanan Optoelectronics (600703.SS)</td><td>U (08/21/2023)</td><td>Rmb13.92</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb4.55</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb7.51</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb196.30</td></tr><tr><td colspan="3">Howard Kao</td></tr><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$36.70</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$785.00</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$36.35</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$7.36</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$342.00</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$1,320.00</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb57.86</td></tr><tr><td>Lenovo (0992.HK)</td><td>E (11/16/2025)</td><td>HK$22.34</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$2,240.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$819.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$93.10</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$372.00</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb151.28</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb379.50</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$902.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$156.00</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$4,850.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$855.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$552.00</td></tr><tr><td colspan="3">Sharon Shih</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,405.00</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$1,055.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$205.50</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$2,215.00</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,825.00</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb70.13</td></tr><tr><td>Foxconn Technology (2354.TW)</td><td>U (04/23/2025)</td><td>NT$57.00</td></tr><tr><td>GoerTek Inc (002241.SZ)</td><td>U (04/23/2025)</td><td>Rmb23.01</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$260.50</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$2,195.00</td></tr><tr><td>Lingyi Itech Guangdong Co (002600.SZ)</td><td>U (04/23/2025)</td><td>Rmb14.01</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$217.00</td></tr><tr><td>Luxshare Precision Industry Co., Ltd. (002475.SZ)</td><td>O (10/24/2016)</td><td>Rmb63.76</td></tr><tr><td>Sunonwealth Electric Machine Industry Co (2421.TW)</td><td>E (02/23/2024)</td><td>NT$144.00</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$238.50</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$352.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
