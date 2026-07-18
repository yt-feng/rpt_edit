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
# Xiaomi Corp. (1810.HK)

Xiaomi Robotics: Integrating Hardware Ontologies, Data, and Models to Scale up; Buy

## What's new

We continue to see catalysts in EV and AI playing out in 3Q26 as we outlined in prior notes (Setting the scene for a catalyst-rich 3Q on Jun 24 and Sharpening the scene on Jul 10). Xiaomi Robotics on Jul 13-15 announced several achievements:

1) Humanoid deployment: Xiaomi humanoids have improved the task success rate to 98% at self-tapping nut loading stations by Jul, from 90%+ in Mar when they were initially deployed, which is just 1pp behind experienced human workers. From July, humanoids have started taking on new logistics tasks such as sorting flexible center console side covers and folding returnable boxes with a 90% success rate, and achieved long-duration continuous operations with flexible workpieces for the first time. Despite the apparent gap in speed and volume, this places Xiaomi alongside global leaders (e.g. Figure AI) in deploying humanoids to active automotive production lines.

## 2) Embodied data/scene synthesis: Xiaomi-Robotics-U0, a

38B-parameter unified generative model, is designed to synthesize high-fidelity robot trajectories and physical interaction scenarios and mitigate the bottleneck of real-world data scarcity. The model uniquely unifies text-to-image generation, any-to-image editing, multi-view embodied scene generation, embodied transfer, and embodied video generation into a single architecture, allowing autoregressive scaling across modalities while preserving the geometric integrity and perspective consistency. As per Xiaomi, Robotics-U0 outperforms GPT-Image-2 in embodied scene generation and embodied transfer, and ranks No.1 on WorldArena, a unified benchmark for embodied world models evaluation.

## 3) Robot foundation model: Xiaomi-Robotics-1, a

Vision-Language-Action (VLA) foundation model designed for end-to-end physical execution, was released as the cognitive and

## BUY

Timothy Zhao
+852-2978-2673 | timothy.zhao@gs.com
GS (Asia) L.L.C.

Ronald Keung, CFA
+852-2978-0856 | ronald.keung@gs.com
GS (Asia) L.L.C.

Eunice Liu
+852-2978-7472 | eunice.liu@gs.com
GS (Asia) L.L.C.

## Key Data

Market cap: HK\$708.8bn / \$90.4bn
Enterprise value: HK\$510.2bn / \$65.1bn
3m ADTV: HK\$4.7bn / \$596.8mn
China
China Internet Verticals
M&A Rank: 3
Leases incl. in net debt & EV?: No

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (Rmb mn)</td><td>457,286.6</td><td>479,154.1</td><td>566,666.6</td><td>670,393.3</td></tr><tr><td>EBITDA (Rmb mn)</td><td>56,657.7</td><td>36,636.9</td><td>48,745.1</td><td>60,973.7</td></tr><tr><td>EPS (Rmb)</td><td>1.47</td><td>1.02</td><td>1.36</td><td>1.73</td></tr><tr><td>P/E (X)</td><td>30.6</td><td>23.2</td><td>17.4</td><td>13.8</td></tr><tr><td>P/B (X)</td><td>4.5</td><td>2.1</td><td>1.9</td><td>1.6</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>(2.9)</td><td>(4.7)</td><td>(3.9)</td><td>(3.4)</td></tr><tr><td>CROCI (%)</td><td>28.1</td><td>17.0</td><td>19.0</td><td>20.3</td></tr><tr><td>FCF yield (%)</td><td>1.9</td><td>2.0</td><td>3.4</td><td>4.0</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.23</td><td>0.20</td><td>0.27</td><td>0.32</td></tr></table>

GS Factor Profile

![](images/fc4439cda2d5c2a8ed9b88bbe789dc297808f610d31819e675ccf3d5b3f8a09b.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Xiaomi Corp. (1810.HK) Rating since Oct 19, 2023

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>30.6</td><td>23.2</td><td>17.4</td><td>13.8</td></tr><tr><td>P/B (X)</td><td>4.5</td><td>2.1</td><td>1.9</td><td>1.6</td></tr><tr><td>FCF yield (%)</td><td>1.9</td><td>2.0</td><td>3.4</td><td>4.0</td></tr><tr><td>EV/EBITDAR (X)</td><td>17.5</td><td>12.0</td><td>8.8</td><td>6.7</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>17.5</td><td>12.0</td><td>8.8</td><td>6.7</td></tr><tr><td>CROCI (%)</td><td>28.1</td><td>17.0</td><td>19.0</td><td>20.3</td></tr><tr><td>ROE (%)</td><td>18.3</td><td>8.6</td><td>10.4</td><td>11.7</td></tr><tr><td>Net debt/equity (%)</td><td>(61.4)</td><td>(57.9)</td><td>(55.9)</td><td>(54.0)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(61.4)</td><td>(57.9)</td><td>(55.9)</td><td>(54.0)</td></tr><tr><td>Interest cover (X)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Days inventory outst, sales</td><td>57.3</td><td>64.4</td><td>60.8</td><td>59.7</td></tr><tr><td>Receivable days</td><td>46.9</td><td>47.7</td><td>43.6</td><td>42.2</td></tr><tr><td>Days payable outstanding</td><td>144.1</td><td>142.3</td><td>127.3</td><td>117.3</td></tr><tr><td>DuPont ROE (%)</td><td>15.6</td><td>8.1</td><td>9.8</td><td>11.0</td></tr><tr><td>Turnover (X)</td><td>0.9</td><td>0.9</td><td>1.0</td><td>1.0</td></tr><tr><td>Leverage (X)</td><td>1.9</td><td>1.8</td><td>1.8</td><td>1.7</td></tr><tr><td>Gross cash invested (ex cash) (Rmb)</td><td>193,679.1</td><td>226,261.1</td><td>261,292.4</td><td>303,166.7</td></tr><tr><td>Average capital employed (Rmb)</td><td>230,839.6</td><td>286,628.9</td><td>309,387.5</td><td>335,633.3</td></tr><tr><td>BVPS (Rmb)</td><td>9.97</td><td>11.20</td><td>12.60</td><td>14.40</td></tr></table>

Income Statement (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>457,286.6</td><td>479,154.1</td><td>566,666.6</td><td>670,393.3</td></tr><tr><td>Cost of goods sold</td><td>(355,480.8)</td><td>(378,237.8)</td><td>(442,877.5)</td><td>(521,559.7)</td></tr><tr><td>SG&amp;A</td><td>(39,867.4)</td><td>(42,521.3)</td><td>(46,836.4)</td><td>(51,873.4)</td></tr><tr><td>R&amp;D</td><td>(33,132.2)</td><td>(39,991.0)</td><td>(47,748.6)</td><td>(56,518.7)</td></tr><tr><td>Other operating inc./(exp.)</td><td>19,094.7</td><td>8,026.1</td><td>8,026.1</td><td>8,026.1</td></tr><tr><td>EBITDA</td><td>56,657.7</td><td>36,636.9</td><td>48,745.1</td><td>60,973.7</td></tr><tr><td>Depreciation &amp; amortization</td><td>(8,756.7)</td><td>(10,206.8)</td><td>(11,514.9)</td><td>(12,506.0)</td></tr><tr><td>EBIT</td><td>47,900.9</td><td>26,430.1</td><td>37,230.2</td><td>48,467.7</td></tr><tr><td>Net interest inc./(exp.)</td><td>1,745.9</td><td>2,513.0</td><td>2,689.9</td><td>2,568.2</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>49,646.9</td><td>28,943.2</td><td>39,920.1</td><td>51,035.9</td></tr><tr><td>Provision for taxes</td><td>(8,080.4)</td><td>(4,905.0)</td><td>(7,007.9)</td><td>(8,766.7)</td></tr><tr><td>Minority interest</td><td>77.0</td><td>51.3</td><td>51.3</td><td>25.7</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>41,643.4</td><td>24,089.5</td><td>32,963.6</td><td>42,294.9</td></tr><tr><td>Post-tax exceptionals</td><td>(2,400.1)</td><td>2,950.2</td><td>3,342.9</td><td>3,952.6</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>39,243.2</td><td>27,039.8</td><td>36,306.5</td><td>46,247.4</td></tr><tr><td>EPS (basic, pre-except) (Rmb)</td><td>1.62</td><td>0.93</td><td>1.27</td><td>1.62</td></tr><tr><td>EPS (diluted, pre-except) (Rmb)</td><td>1.56</td><td>0.91</td><td>1.24</td><td>1.58</td></tr><tr><td>EPS (basic, post-except) (Rmb)</td><td>1.53</td><td>1.05</td><td>1.40</td><td>1.77</td></tr><tr><td>EPS (diluted, post-except) (Rmb)</td><td>1.47</td><td>1.02</td><td>1.36</td><td>1.73</td></tr><tr><td>DPS (Rmb)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Growth & Margins (%)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>25.0</td><td>4.8</td><td>18.3</td><td>18.3</td></tr><tr><td>EBITDA growth</td><td>83.8</td><td>(35.3)</td><td>33.0</td><td>25.1</td></tr><tr><td>EPS growth</td><td>37.2</td><td>(30.5)</td><td>33.2</td><td>26.7</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EBIT margin</td><td>10.5</td><td>5.5</td><td>6.6</td><td>7.2</td></tr><tr><td>EBITDA margin</td><td>12.4</td><td>7.6</td><td>8.6</td><td>9.1</td></tr><tr><td>Net income margin</td><td>9.1</td><td>5.0</td><td>5.8</td><td>6.3</td></tr></table>

Price Performance  
![](images/43718a7f8aa9aaad734738205a46805608258661ba3d555ff928250701c350de.jpg)  
Source: FactSet. Price as of 16 Jul 2026 close.

Balance Sheet (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>26,914.4</td><td>34,852.2</td><td>51,238.7</td><td>71,749.5</td></tr><tr><td>Accounts receivable</td><td>61,546.1</td><td>63,567.3</td><td>71,669.0</td><td>83,210.5</td></tr><tr><td>Inventory</td><td>80,989.5</td><td>88,082.8</td><td>100,709.1</td><td>118,601.2</td></tr><tr><td>Other current assets</td><td>85,360.8</td><td>85,360.8</td><td>85,360.8</td><td>85,360.8</td></tr><tr><td>Total current assets</td><td>254,810.8</td><td>271,863.1</td><td>308,977.8</td><td>358,922.1</td></tr><tr><td>Net PP&amp;E</td><td>27,950.3</td><td>36,504.1</td><td>45,549.0</td><td>55,533.9</td></tr><tr><td>Net intangibles</td><td>8,319.4</td><td>8,732.5</td><td>9,263.9</td><td>9,973.3</td></tr><tr><td>Total investments</td><td>87,149.5</td><td>94,149.5</td><td>101,149.5</td><td>108,149.5</td></tr><tr><td>Other long-term assets</td><td>129,866.0</td><td>129,866.0</td><td>129,866.0</td><td>129,866.0</td></tr><tr><td>Total assets</td><td>508,096.0</td><td>541,115.2</td><td>594,806.2</td><td>662,444.8</td></tr><tr><td>Accounts payable</td><td>146,051.4</td><td>148,794.3</td><td>160,202.4</td><td>175,010.7</td></tr><tr><td>Short-term debt</td><td>13,202.2</td><td>13,202.2</td><td>13,202.2</td><td>13,202.2</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>33,151.9</td><td>33,115.2</td><td>35,495.1</td><td>38,446.3</td></tr><tr><td>Total current liabilities</td><td>192,405.5</td><td>195,111.7</td><td>208,899.7</td><td>226,659.2</td></tr><tr><td>Long-term debt</td><td>22,921.4</td><td>22,921.4</td><td>22,921.4</td><td>22,921.4</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>26,445.8</td><td>26,628.4</td><td>26,820.1</td><td>27,021.5</td></tr><tr><td>Total long-term liabilities</td><td>49,367.2</td><td>49,549.8</td><td>49,741.6</td><td>49,942.9</td></tr><tr><td>Total liabilities</td><td>241,772.7</td><td>244,661.5</td><td>258,641.3</td><td>276,602.1</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>266,218.7</td><td>296,349.1</td><td>336,060.3</td><td>385,738.1</td></tr><tr><td>Minority interest</td><td>104.6</td><td>104.6</td><td>104.6</td><td>104.6</td></tr><tr><td>Total liabilities &amp; equity</td><td>508,096.0</td><td>541,115.2</td><td>594,806.2</td><td>662,444.8</td></tr><tr><td>Net debt, adjusted</td><td>(71,572.9)</td><td>(79,510.7)</td><td>(95,897.3)</td><td>(116,408.0)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (Rmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>41,643.4</td><td>24,089.5</td><td>32,963.6</td><td>42,294.9</td></tr><tr><td>D&amp;A add-back</td><td>8,756.7</td><td>10,206.8</td><td>11,514.9</td><td>12,506.0</td></tr><tr><td>Minority interest add-back</td><td>(77.0)</td><td>(51.3)</td><td>(51.3)</td><td>(25.7)</td></tr><tr><td>Net (inc)/dec working capital</td><td>(14,220.5)</td><td>(6,225.7)</td><td>(6,748.3)</td><td>(11,472.8)</td></tr><tr><td>Other operating cash flow</td><td>(1,960.3)</td><td>3,579.2</td><td>4,109.0</td><td>4,840.4</td></tr><tr><td>Cash flow from operations</td><td>34,142.4</td><td>31,598.5</td><td>41,787.8</td><td>48,142.8</td></tr><tr><td>Capital expenditures</td><td>(12,769.2)</td><td>(19,173.8)</td><td>(21,091.2)</td><td>(23,200.3)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(58,909.6)</td><td>(4,487.0)</td><td>(4,310.1)</td><td>(4,431.8)</td></tr><tr><td>Cash flow from investing</td><td>(71,678.7)</td><td>(23,660.7)</td><td>(25,401.3)</td><td>(27,632.1)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Inc/(dec) in debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>30,789.3</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Total cash flow</td><td>(6,747.1)</td><td>7,937.8</td><td>16,386.6</td><td>20,510.8</td></tr><tr><td>Free cash flow</td><td>21,373.2</td><td>12,424.8</td><td>20,696.7</td><td>24,942.5</td></tr></table>

Source: Company data, GS estimates.

physical control layer. The model features large-scale pre-training involving 100k hours of real-world robot operation trajectories and 10k hours of cross-ontology post-training, which demonstrates a clean scaling behavior in VLM, and enables cross-ontology adaptation i.e. bipedal, quad, dual-arm, or wheeled systems. The model achieves state-of-the-art (SOTA) across multiple benchmarks (Exhibit 4), outperforming baseline open-source models such as Pi-0.5.

## Implications

Robotics: We see Xiaomi has completed the initial integration of its robotics framework across ontology/body, data and models, which may lead to a self-reinforcing loop (Exhibit 1) toward general-purpose industrial and domestic automation. We believe Xiaomi has clear advantages in deployment scenarios including its own manufacturing factories and a vast home AIoT ecosystem. Real-world deployment failures are analyzed and fed back into the scene generative model to synthesize similar edge-case scenarios; this synthetic data retrains the core foundation model, which is then redeployed to the physical hardware.

That said, we believe there remains a gap between Xiaomi and global leaders in real-world execution (e.g. Figure03 models deployed at BMW Group Plant Spartanburg demonstrated fast speed for similar tasks) and model capabilities (e.g. with closed-source models such as Physical Intelligence's Pi-0.7, Figure's Helix 02, Optimus, and Gemini Robotics 1.5). Meanwhile, Xiaomi has not disclosed detailed architecture, such as cost structure, performance parameters, etc.

AI monetization: As mentioned in our prior note, physical intelligence including embodied AI as one of the three monetization paths within Xiaomi's AI strategy. We expect Xiaomi Robotics to focus on more structured to-B commercial scenarios over the next 3-5 years, e.g. massive humanoid deployment at Xiaomi's factories (smart EV, smartphone and home appliance) and its partner factories, which resembles Tesla's strategy for Optimus in our view.

Valuation: Post +24% share price performance QTD (vs. +3% for HSTECH) partially thanks to favorable flow, the current market cap implies 1) 15x 2026E P/E or 14x 12m-fwd P/E on Xiaomi core ex. smart EV, AI and other new initiatives; 2) 1.3x 2026E P/S on smart EV (vs. 0.75x as of Jun-end) driven by stronger sentiment on the upcoming SkyNomad launch, compared to 0.8x average P/S multiple of its domestic peers (BYD, Li Auto, XPeng and NIO); 

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
