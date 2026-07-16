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
July 14, 2026 09:00 PM GMT

Greater China Technology Hardware | Asia Pacific

# Monthly Databook: Jun-26 shipments +10% vs. MSe; 2Q 8% y/y; 3Qe at -15% y/y

## Key Takeaways

Top five ODMs' June 2026 NB shipments were 12.0M units (+29% m/m, -8% y/y), 10% above our estimate.

We estimate July 2026 NB builds at 8.6M units (-28% m/m, -20% y/y).

We keep our 3Q26 NB build estimate largely unchanged at 28.9M units (-5% q/q, -15% y/y).

Overall June ODM notebook shipments came in 10% above our estimate: Component constraints remain the key bottlenecks, forcing ODMs to prioritize higher-end, more profitable models. We forecast July NB builds at 8.6M (-28% q/q, -20% y/y), after strong quarter-end pull-ins. Overall 2Q notebook builds came in at 30.4M units (+4% q/q, -8% y/y), 4% above our estimate.

We keep our 3Q notebook build estimate largely unchanged at 28.9M units (-5% q/q, -15% y/y): After the stronger 2Q, despite us keeping 3Q builds largely unchanged, the builds imply a \~5% sequential decline, which is sub-seasonal vs the 15Y avg seasonality of +5% q/q in 3Q. Actual shipments will continue to depend on component availability, but we continue to hear about constraints and expect this to continue to cap low-end notebook model builds. We expect ODMs to provide quantitative guidance on 3Q notebook builds when they report 2Q earnings in early August.

Exhibit 1: Monthly NB shipments for top five NB ODMs

<table><tr><td>Shipment (unit: k)</td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25E</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>Jun-26E</td><td>Diff</td><td>Jul-26E</td></tr><tr><td>Quanta</td><td>2,800</td><td>3,100</td><td>4,900</td><td>3,300</td><td>3,800</td><td>5,000</td><td>4,000</td><td>4,100</td><td>4,600</td><td>3,500</td><td>3,500</td><td>3,900</td><td>2,760</td><td>2,000</td><td>5,300</td><td>3,500</td><td>3,500</td><td>4,500</td><td>3,500</td><td>29%</td><td>3,200</td></tr><tr><td>Wiston</td><td>1,500</td><td>1,500</td><td>1,900</td><td>1,700</td><td>1,800</td><td>2,400</td><td>2,000</td><td>2,200</td><td>2,200</td><td>2,100</td><td>2,200</td><td>2,600</td><td>1,700</td><td>1,600</td><td>2,800</td><td>1,800</td><td>1,700</td><td>2,000</td><td>2,200</td><td>-9%</td><td>1,500</td></tr><tr><td>Others</td><td>1,500</td><td>1,600</td><td>1,900</td><td>1,700</td><td>1,800</td><td>2,100</td><td>1,700</td><td>1,800</td><td>1,900</td><td>1,600</td><td>1,700</td><td>2,000</td><td>1,700</td><td>1,500</td><td>2,200</td><td>1,500</td><td>1,500</td><td>2,400</td><td>2,200</td><td>9%</td><td>1,500</td></tr><tr><td>Compal</td><td>2,000</td><td>2,100</td><td>2,900</td><td>2,200</td><td>2,400</td><td>2,500</td><td>2,300</td><td>2,300</td><td>2,500</td><td>2,100</td><td>2,300</td><td>2,400</td><td>1,600</td><td>1,500</td><td>2,800</td><td>1,800</td><td>2,000</td><td>2,400</td><td>2,200</td><td>9%</td><td>1,800</td></tr><tr><td>Pegatron</td><td>610</td><td>675</td><td>610</td><td>610</td><td>75</td><td>75</td><td>75</td><td>825</td><td>825</td><td>825</td><td>75</td><td>625</td><td>700</td><td>435</td><td>675</td><td>525</td><td>575</td><td>650</td><td>750</td><td>-13%</td><td>550</td></tr><tr><td>Total</td><td>8,410</td><td>8,875</td><td>12,300</td><td>9,510</td><td>10,575</td><td>12,990</td><td>10,750</td><td>11,225</td><td>12,025</td><td>10,075</td><td>10,410</td><td>11,825</td><td>8,400</td><td>7,025</td><td>13,775</td><td>9,125</td><td>9,275</td><td>11,950</td><td>10,850</td><td>10%</td><td>8,550</td></tr><tr><td>MoM %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quanta</td><td>-35%</td><td>11%</td><td>58%</td><td>-33%</td><td>15%</td><td>32%</td><td>-20%</td><td>2%</td><td>12%</td><td>-24%</td><td>0%</td><td>11%</td><td>-31%</td><td>-26%</td><td>165%</td><td>-34%</td><td>0%</td><td>29%</td><td>0%</td><td>-29%</td><td></td></tr><tr><td>Wiston</td><td>-17%</td><td>0%</td><td>27%</td><td>-11%</td><td>6%</td><td>33%</td><td>-17%</td><td>10%</td><td>0%</td><td>-5%</td><td>5%</td><td>18%</td><td>-35%</td><td>-6%</td><td>75%</td><td>-36%</td><td>-6%</td><td>18%</td><td>29%</td><td>-25%</td><td></td></tr><tr><td>Others</td><td>-25%</td><td>7%</td><td>19%</td><td>-11%</td><td>6%</td><td>17%</td><td>-19%</td><td>6%</td><td>6%</td><td>-16%</td><td>6%</td><td>18%</td><td>-15%</td><td>-12%</td><td>47%</td><td>-32%</td><td>0%</td><td>87%</td><td>47%</td><td>-38%</td><td></td></tr><tr><td>Compal</td><td>-13%</td><td>5%</td><td>38%</td><td>-24%</td><td>9%</td><td>4%</td><td>-8%</td><td>0%</td><td>9%</td><td>-16%</td><td>10%</td><td>4%</td><td>-33%</td><td>-6%</td><td>87%</td><td>-36%</td><td>11%</td><td>20%</td><td>10%</td><td>-25%</td><td></td></tr><tr><td>Pegatron</td><td>-19%</td><td>-6%</td><td>22%</td><td>-13%</td><td>27%</td><td>28%</td><td>-24%</td><td>10%</td><td>0%</td><td>-6%</td><td>-8%</td><td>30%</td><td>-24%</td><td>-39%</td><td>59%</td><td>-22%</td><td>10%</td><td>13%</td><td>30%</td><td>-15%</td><td></td></tr><tr><td>Total</td><td>-25%</td><td>6%</td><td>39%</td><td>-23%</td><td>11%</td><td>23%</td><td>-17%</td><td>4%</td><td>7%</td><td>-16%</td><td>3%</td><td>14%</td><td>-29%</td><td>-16%</td><td>96%</td><td>-34%</td><td>2%</td><td>29%</td><td>17%</td><td>-28%</td><td></td></tr><tr><td>YoY%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quanta</td><td>-3%</td><td>7%</td><td>4%</td><td>3%</td><td>-5%</td><td>11%</td><td>18%</td><td>-5%</td><td>-6%</td><td>9%</td><td>-3%</td><td>-9%</td><td>-4%</td><td>-35%</td><td>8%</td><td>6%</td><td>-8%</td><td>-10%</td><td>-30%</td><td>-20%</td><td></td></tr><tr><td>Wiston</td><td>15%</td><td>7%</td><td>0%</td><td>6%</td><td>6%</td><td>33%</td><td>25%</td><td>29%</td><td>16%</td><td>17%</td><td>29%</td><td>44%</td><td>13%</td><td>7%</td><td>47%</td><td>47%</td><td>6%</td><td>-17%</td><td>-8%</td><td>-25%</td><td></td></tr><tr><td>Others</td><td>0%</td><td>23%</td><td>12%</td><td>13%</td><td>6%</td><td>24%</td><td>0%</td><td>6%</td><td>6%</td><td>-6%</td><td>0%</td><td>0%</td><td>13%</td><td>-6%</td><td>16%</td><td>-12%</td><td>-17%</td><td>14%</td><td>5%</td><td>-12%</td><td></td></tr><tr><td>Compal</td><td>-9%</td><td>-9%</td><td>-3%</td><td>-21%</td><td>-17%</td><td>-17%</td><td>-8%</td><td>-21%</td><td>-14%</td><td>-25%</td><td>-15%</td><td>4%</td><td>-20%</td><td>-29%</td><td>-3%</td><td>-18%</td><td>-17%</td><td>-4%</td><td>-12%</td><td>-22%</td><td></td></tr><tr><td>Pegatron</td><td>16%</td><td>53%</td><td>8%</td><td>16%</td><td>6%</td><td>28%</td><td>-3%</td><td>-6%</td><td>-2%</td><td>35%</td><td>14%</td><td>23%</td><td>15%</td><td>-26%</td><td>-4%</td><td>-14%</td><td>-26%</td><td>-34%</td><td>-24%</td><td>-27%</td><td></td></tr><tr><td>Total</td><td>0%</td><td>7%</td><td>3%</td><td>-1%</td><td>-4%</td><td>10%</td><td>8%</td><td>-2%</td><td>-2%</td><td>0%</td><td>1%</td><td>6%</td><td>0%</td><td>-21%</td><td>12%</td><td>-4%</td><td>-12%</td><td>-8%</td><td>-16%</td><td>-20%</td><td></td></tr></table>

Source: Company data, MS. E = MS estimates. "Others" are other leaders.

Exhibit 2: Quarterly NB shipments for top five NB ODMs

<table><tr><td>Shipment (unit: k)</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>2Q26E</td><td>Diff.</td><td>3Q26E</td><td>3Q26E</td><td>Diff.</td></tr><tr><td>Quanta</td><td>10,500</td><td>11,700</td><td>12,600</td><td>11,100</td><td>10,800</td><td>12,100</td><td>12,700</td><td>10,900</td><td>10,000</td><td>11,500</td><td>10,500</td><td>10%</td><td>11,000</td><td>10,800</td><td>2%</td></tr><tr><td>Wistron</td><td>4,600</td><td>5,100</td><td>5,200</td><td>5,300</td><td>4,900</td><td>5,900</td><td>6,400</td><td>6,900</td><td>6,100</td><td>5,500</td><td>5,700</td><td>-4%</td><td>4,700</td><td>5,500</td><td>-15%</td></tr><tr><td>Others</td><td>4,500</td><td>4,900</td><td>5,200</td><td>5,400</td><td>5,000</td><td>5,600</td><td>5,400</td><td>5,300</td><td>5,400</td><td>5,400</td><td>5,200</td><td>4%</td><td>5,000</td><td>4,500</td><td>11%</td></tr><tr><td>Compal</td><td>7,500</td><td>8,700</td><td>8,300</td><td>7,800</td><td>7,000</td><td>7,100</td><td>7,100</td><td>6,800</td><td>5,900</td><td>6,200</td><td>6,000</td><td>3%</td><td>6,400</td><td>6,400</td><td>0%</td></tr><tr><td>Pegatron</td><td>1,550</td><td>2,030</td><td>2,475</td><td>1,950</td><td>1,885</td><td>2,375</td><td>2,400</td><td>2,410</td><td>1,800</td><td>1,750</td><td>1,850</td><td>-5%</td><td>1,800</td><td>1,800</td><td>0%</td></tr><tr><td>Total</td><td>28,650</td><td>32,430</td><td>33,775</td><td>31,550</td><td>29,585</td><td>33,075</td><td>34,000</td><td>32,310</td><td>29,200</td><td>30,350</td><td>29,250</td><td>4%</td><td>28,900</td><td>29,000</td><td>0%</td></tr><tr><td>QoQ %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quanta</td><td>1%</td><td>11%</td><td>8%</td><td>-12%</td><td>-3%</td><td>12%</td><td>5%</td><td>-14%</td><td>-8%</td><td>15%</td><td>5%</td><td></td><td>-4%</td><td>3%</td><td></td></tr><tr><td>Wistron</td><td>-13%</td><td>11%</td><td>2%</td><td>2%</td><td>-8%</td><td>20%</td><td>8%</td><td>8%</td><td>-12%</td><td>-10%</td><td>-7%</td><td></td><td>-15%</td><td>-4%</td><td></td></tr><tr><td>Others</td><td>0%</td><td>9%</td><td>6%</td><td>4%</td><td>-7%</td><td>12%</td><td>-4%</td><td>-2%</td><td>2%</td><td>0%</td><td>-4%</td><td></td><td>-7%</td><td>-13%</td><td></td></tr><tr><td>Compal</td><td>-10%</td><td>16%</td><td>-5%</td><td>-6%</td><td>-10%</td><td>1%</td><td>0%</td><td>-4%</td><td>-13%</td><td>5%</td><td>2%</td><td></td><td>3%</td><td>7%</td><td></td></tr><tr><td>Pegatron</td><td>-6%</td><td>31%</td><td>22%</td><td>-21%</td><td>-3%</td><td>26%</td><td>1%</td><td>0%</td><td>-25%</td><td>-3%</td><td>3%</td><td></td><td>3%</td><td>-3%</td><td></td></tr><tr><td>Total</td><td>-5%</td><td>13%</td><td>4%</td><td>-7%</td><td>-6%</td><td>12%</td><td>3%</td><td>-5%</td><td>-10%</td><td>4%</td><td>0%</td><td></td><td>-5%</td><td>-1%</td><td></td></tr><tr><td>YoY%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quanta</td><td>-3%</td><td>-7%</td><td>-4%</td><td>7%</td><td>3%</td><td>3%</td><td>1%</td><td>-2%</td><td>-7%</td><td>-5%</td><td>-13%</td><td></td><td>-13%</td><td>-15%</td><td></td></tr><tr><td>Wistron</td><td>18%</td><td>11%</td><td>0%</td><td>0%</td><td>7%</td><td>16%</td><td>23%</td><td>30%</td><td>24%</td><td>-7%</td><td>-3%</td><td></td><td>-27%</td><td>-14%</td><td></td></tr><tr><td>Others</td><td>2%</td><td>0%</td><td>6%</td><td>20%</td><td>11%</td><td>14%</td><td>4%</td><td>-2%</td><td>8%</td><td>-4%</td><td>-7%</td><td></td><td>-7%</td><td>-17%</td><td></td></tr><tr><td>Compal</td><td>-1%</td><td>0%</td><td>-11%</td><td>-6%</td><td>-7%</td><td>-18%</td><td>-14%</td><td>-13%</td><td>-16%</td><td>-13%</td><td>-15%</td><td></td><td>-10%</td><td>-10%</td><td></td></tr><tr><td>Pegatron</td><td>-9%</td><td>-2%</td><td>-1%</td><td>18%</td><td>22%</td><td>17%</td><td>-3%</td><td>24%</td><td>-5%</td><td>-26%</td><td>-22%</td><td></td><td>-25%</td><td>-25%</td><td></td></tr><tr><td>Total</td><td>1%</td><td>-1%</td><td>-4%</td><td>5%</td><td>3%</td><td>2%</td><td>1%</td><td>2%</td><td>-1%</td><td>-8%</td><td>-12%</td><td></td><td>-15%</td><td>-15%</td><td></td></tr></table>

Source: Company data, MS. E = MS estimates. "Others" are other leaders.

MS TAIWAN LIMITED+

Howard Kao
Equity Analyst
Howard.Kao@morganstanley.com

Irene Yen
Research Associate
Irene.Yen@morganstanley.com +886 2 2730-2989

+886 2 2730-2869

MS ASIA LIMITED+

Andy Meng, CFA
Equity Analyst
Andy.Meng@morganstanley.com

+852 2239-7689

![](images/dd56315fc82286cfdf92eb6963f554d012b4331795746556aa64abc1ac51d6c3.jpg)

Asia Summer School 2026

GREATER CHINA TECHNOLOGY HARDWARE

Asia Pacific
Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-74

[中间内容因长度限制已省略]

><td>Yongxin Optics Co Ltd (603297.SS)</td><td>E (11/15/2022)</td><td>Rmb111.22</td></tr><tr><td>Zhejiang Crystal-Optech Co Ltd (002273.SZ)</td><td>O (11/15/2022)</td><td>Rmb29.66</td></tr><tr><td>Zhongji Innolight Co Ltd (300308.SZ)</td><td>++</td><td>Rmb1,108.00</td></tr><tr><td>ZTE Corporation (0763.HK)</td><td>O (06/04/2026)</td><td>HK$24.92</td></tr><tr><td>ZTE Corporation (000063.SZ)</td><td>E (06/04/2026)</td><td>Rmb40.04</td></tr><tr><td colspan="3">Derrick Yang</td></tr><tr><td>Accton Technology Corporation (2345.TW)</td><td>O (06/06/2024)</td><td>NT$2,405.00</td></tr><tr><td>Advantech (2395.TW)</td><td>O (01/20/2021)</td><td>NT$536.00</td></tr><tr><td>AirTAC International (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,320.00</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,225.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$29.25</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$905.00</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$1,865.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb6.83</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,135.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$1,850.00</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$1,890.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$196.00</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$60.90</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,410.00</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$332.00</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$61.00</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$8,080.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb39.53</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$222.00</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$90.00</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb4.81</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb7.16</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb297.10</td></tr><tr><td colspan="3">Howard Kao</td></tr><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$31.95</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$704.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$192.50</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$36.65</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$5.99</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb63.08</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$335.50</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$1,045.00</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$236.50</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb85.49</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$1,990.00</td></tr><tr><td>Lenovo (0992.HK)</td><td>O (07/10/2026)</td><td>HK$23.30</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$1,980.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$1,270.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$82.60</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$378.00</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb134.45</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb393.59</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$903.00</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$329.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$143.50</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$4,960.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$816.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$646.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
