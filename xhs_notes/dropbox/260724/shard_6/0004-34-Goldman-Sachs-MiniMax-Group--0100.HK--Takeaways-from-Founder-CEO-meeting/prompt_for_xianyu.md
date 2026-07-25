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
<table><tr><td>Key Data</td></tr><tr><td>Market cap: HK$62.5bn / $8.0bn</td></tr><tr><td>Enterprise value: HK$56.1bn / $7.2bn</td></tr><tr><td>3m ADTV: HK$1.5bn / $191.5mn</td></tr><tr><td>China</td></tr><tr><td>China Ecommerce &amp; Logistics</td></tr><tr><td>M&amp;A Rank: 3</td></tr><tr><td>Leases incl. in net debt &amp; EV?: Yes</td></tr></table>

# MiniMax Group (0100.HK)

# Takeaways from Founder/CEO meeting: Pursuing ultimate price-to-performance; reiterate Buy

0100.HK 12m Price Target: HK\$860.00 Price: HK\$199.30 Upside: 331.5%

We attended an analyst meeting hosted by MiniMax Founder & CEO Dr. Yan Junjie and the management team at its Shanghai headquarters on July 23. Key topics discussed include the company's top focus in pursuing the best price-to-performance for each of its models, its relative early-mover in building out computing infrastructure amongst independent AI labs, the latest LLM industry landscape and rising importance of ‘price’ alongside ‘performance’ and agentic/industry capabilities, and the company’s multi-modal approach a key differentiation.

## 1) The company's top focus in pursuing the best

price-to-performance for its models, in particular with M3 model currently at trillions of daily tokens at healthy gross margins for its open platform/API revenues (targeting eventual high double-digits GPM driven by inference efficiencies, at current pricing) and the company expectations that its upcoming M3 Pro (at the 3 trillion parameter size class, targeting launch in Sep-Oct 2026) will have significant cost efficiencies vs. comparable models of its class. MiniMax Sparse Attention, activated parameters and KV Cache optimization were mentioned as drivers.

2) Its early-mover in building out computing infrastructure amongst independent AI labs: the company believes its decision to significantly ramp up self-operated computing (via. acquiring/long-term renting domestically and globally) since Sep 2025 as an advantage amongst peers, when GPUs/AI servers were at much lower long-term rental prices vs. today and will be one of the key drivers of its cost competitiveness via. attractive hardware/rental prices and at high utilization/efficiency (e.g. training+inferencing in a same cluster) given its years of experience in self-operating AI infrastructure.

3) LLM industry landscape and rising importance of ‘price’ alongside ‘performance’ and agentic/sector-specific

## BUY

Ronald Keung, CFA
+852-2978-0856 | ronald.keung@gs.com
GS (Asia) L.L.C.

Lincoln Kong, CFA
+852-2978-6603 | lincoln.kong@gs.com
GS (Asia) L.L.C.

Steve Qiu
+852-2978-2672 | steve.qiu@gs.com
GS (Asia) L.L.C.

GS Forecast

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue ($ mn)</td><td>79.0</td><td>300.0</td><td>880.1</td><td>2,469.6</td></tr><tr><td>EBITDA ($ mn)</td><td>(294.7)</td><td>(452.5)</td><td>(518.8)</td><td>(396.7)</td></tr><tr><td>EPS ($)</td><td>(2.31)</td><td>(1.35)</td><td>(1.48)</td><td>(1.08)</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>P/B (X)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Dividend yield (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>CROCI (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>FCF yield (%)</td><td>-</td><td>(3.6)</td><td>(6.3)</td><td>(3.4)</td></tr><tr><td></td><td>6/25</td><td>12/25</td><td>6/26E</td><td>12/26E</td></tr><tr><td>EPS ($)</td><td>(1.38)</td><td>(0.93)</td><td>(1.69)</td><td>(2.14)</td></tr></table>

GS Factor Profile

![](images/a4f50e3a3fcfcbd187da6d8e831df75b367d688c3e1b149db8ba429f2e3eb8aa.jpg)  
Source: Company data, GS estimates. See disclosures for details.

Rating since May 4, 2026

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>P/B (X)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>FCF yield (%)</td><td>-</td><td>(3.6)</td><td>(6.3)</td><td>(3.4)</td></tr><tr><td>EV/EBITDAR (X)</td><td>-</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>-</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>CROCI (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROE (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/equity (%)</td><td>18.3</td><td>33.3</td><td>10.3</td><td>0.4</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>18.4</td><td>33.4</td><td>10.5</td><td>0.7</td></tr><tr><td>Interest cover (X)</td><td>(442.5)</td><td>(1,713.9)</td><td>(794.3)</td><td>(421.5)</td></tr><tr><td>Days inventory outst, sales</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Receivable days</td><td>40.9</td><td>40.9</td><td>40.9</td><td>40.9</td></tr><tr><td>Days payable outstanding</td><td>337.1</td><td>206.3</td><td>118.7</td><td>94.1</td></tr><tr><td>DuPont ROE (%)</td><td>9.5</td><td>17.3</td><td>16.2</td><td>10.7</td></tr><tr><td>Turnover (X)</td><td>0.1</td><td>0.2</td><td>0.6</td><td>1.4</td></tr><tr><td>Leverage (X)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Gross cash invested (ex cash) ($)</td><td>(3,187.6)</td><td>(3,323.0)</td><td>(3,282.8)</td><td>(3,359.6)</td></tr><tr><td>Average capital employed ($)</td><td>(2,094.6)</td><td>(3,189.4)</td><td>(3,238.4)</td><td>(3,252.4)</td></tr><tr><td>BVPS ($)</td><td>(24.37)</td><td>(7.82)</td><td>(9.15)</td><td>(10.05)</td></tr></table>

Income Statement (\$ mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>79.0</td><td>300.0</td><td>880.1</td><td>2,469.6</td></tr><tr><td>Cost of goods sold</td><td>(59.0)</td><td>(221.9)</td><td>(666.3)</td><td>(1,624.7)</td></tr><tr><td>SG&amp;A</td><td>(88.7)</td><td>(134.8)</td><td>(259.4)</td><td>(530.5)</td></tr><tr><td>R&amp;D</td><td>(252.8)</td><td>(467.6)</td><td>(549.5)</td><td>(791.8)</td></tr><tr><td>Other operating inc./(exp.)</td><td>24.0</td><td>68.9</td><td>72.3</td><td>75.9</td></tr><tr><td>EBITDA</td><td>(294.7)</td><td>(452.5)</td><td>(518.8)</td><td>(396.7)</td></tr><tr><td>Depreciation &amp; amortization</td><td>(2.7)</td><td>(2.9)</td><td>(3.9)</td><td>(4.8)</td></tr><tr><td>EBIT</td><td>(297.4)</td><td>(455.4)</td><td>(522.8)</td><td>(401.5)</td></tr><tr><td>Net interest inc./(exp.)</td><td>(0.7)</td><td>(0.3)</td><td>(0.7)</td><td>(1.0)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>(257.7)</td><td>(424.5)</td><td>(473.5)</td><td>(351.9)</td></tr><tr><td>Provision for taxes</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>(250.9)</td><td>(424.5)</td><td>(473.5)</td><td>(351.9)</td></tr><tr><td>Post-tax exceptionals</td><td>(1,620.8)</td><td>(68.9)</td><td>(72.3)</td><td>(75.9)</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>(1,871.6)</td><td>(493.4)</td><td>(545.8)</td><td>(427.8)</td></tr><tr><td>EPS (basic, pre-except) ($)</td><td>(2.31)</td><td>(1.35)</td><td>(1.48)</td><td>(1.08)</td></tr><tr><td>EPS (diluted, pre-except) ($)</td><td>(2.31)</td><td>(1.35)</td><td>(1.48)</td><td>(1.08)</td></tr><tr><td>EPS (basic, post-except) ($)</td><td>(17.23)</td><td>(1.57)</td><td>(1.71)</td><td>(1.31)</td></tr><tr><td>EPS (diluted, post-except) ($)</td><td>(17.23)</td><td>(1.57)</td><td>(1.71)</td><td>(1.31)</td></tr><tr><td>DPS ($)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Growth & Margins (%)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>158.9</td><td>279.6</td><td>193.3</td><td>180.6</td></tr><tr><td>EBITDA growth</td><td>(6.0)</td><td>(53.6)</td><td>(14.7)</td><td>23.5</td></tr><tr><td>EPS growth</td><td>(2.7)</td><td>41.4</td><td>(9.3)</td><td>27.1</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EBIT margin</td><td>(376.2)</td><td>(151.8)</td><td>(59.4)</td><td>(16.3)</td></tr><tr><td>EBITDA margin</td><td>(372.8)</td><td>(150.8)</td><td>(59.0)</td><td>(16.1)</td></tr><tr><td>Net income margin</td><td>(317.4)</td><td>(141.5)</td><td>(53.8)</td><td>(14.2)</td></tr></table>

Price Performance  
![](images/7c0c9325cbc1211bd5ec7d14006489055c96617ab0e5d0b28d825a3831a93a13.jpg)  
Source: FactSet. Price as of 23 Jul 2026 close.

<table><tr><td colspan="5">Balance Sheet ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>507.6</td><td>1,041.1</td><td>727.6</td><td>543.8</td></tr><tr><td>Accounts receivable</td><td>10.7</td><td>56.5</td><td>140.7</td><td>412.7</td></tr><tr><td>Inventory</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current assets</td><td>489.0</td><td>502.7</td><td>560.7</td><td>719.7</td></tr><tr><td>Total current assets</td><td>1,007.4</td><td>1,600.3</td><td>1,429.0</td><td>1,676.2</td></tr><tr><td>Net PP&amp;E</td><td>3.9</td><td>5.3</td><td>6.5</td><td>7.4</td></tr><tr><td>Net intangibles</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total investments</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Other long-term assets</td><td>77.1</td><td>79.2</td><td>85.0</td><td>100.9</td></tr><tr><td>Total assets</td><td>1,088.4</td><td>1,684.8</td><td>1,520.5</td><td>1,784.5</td></tr><tr><td>Accounts payable</td><td>57.7</td><td>193.1</td><td>240.2</td><td>597.2</td></tr><tr><td>Short-term debt</td><td>35.5</td><td>235.5</td><td>435.5</td><td>535.5</td></tr><tr><td>Short-term lease liabilities</td><td>1.3</td><td>1.5</td><td>2.4</td><td>3.3</td></tr><tr><td>Other current liabilities</td><td>3,639.2</td><td>3,702.9</td><td>3,762.9</td><td>3,919.4</td></tr><tr><td>Total current liabilities</td><td>3,733.6</td><td>4,133.1</td><td>4,441.0</td><td>5,055.4</td></tr><tr><td>Long-term debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Long-term lease liabilities</td><td>0.6</td><td>2.3</td><td>3.6</td><td>5.0</td></tr><tr><td>Other long-term liabilities</td><td>2.3</td><td>2.3</td><td>2.3</td><td>2.3</td></tr><tr><td>Total long-term liabilities</td><td>3.0</td><td>4.6</td><td>5.9</td><td>7.3</td></tr><tr><td>Total liabilities</td><td>3,736.6</td><td>4,137.7</td><td>4,446.9</td><td>5,062.7</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>(2,648.2)</td><td>(2,452.7)</td><td>(2,926.2)</td><td>(3,278.0)</td></tr><tr><td>Minority interest</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total liabilities &amp; equity</td><td>1,088.4</td><td>1,684.8</td><td>1,520.5</td><td>1,784.5</td></tr><tr><td>Net debt, adjusted</td><td>(486.0)</td><td>(819.4)</td><td>(306.0)</td><td>(22.1)</td></tr></table>

<table><tr><td colspan="5">Cash flow ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>(1,871.6)</td><td>(493.4)</td><td>(545.8)</td><td>(427.8)</td></tr><tr><td>D&amp;A add-back</td><td>2.7</td><td>2.9</td><td>3.9</td><td>4.8</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>6.3</td><td>137.6</td><td>(41.0)</td><td>66.7</td></tr><tr><td>Other operating cash flow</td><td>1,583.0</td><td>69.1</td><td>73.0</td><td>76.9</td></tr><tr><td>Cash flow from operations</td><td>(279.6)</td><td>(283.7)</td><td>(509.8)</td><td>(279.5)</td></tr><tr><td>Capital expenditures</td><td>(0.9)</td><td>(1.5)</td><td>(1.8)</td><td>(2.1)</td></tr><tr><td>Acquisitions</td><td>(2,207.1)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>4,865.2</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(13.7)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>72.3</td><td>(1.5)</td><td>(1.8)</td><td>(2.1)</td></tr><tr><td>Repayment of lease liabilities</td><td>(2.2)</td><td>(1.1)</td><td>(1.2)</td><td>(1.3)</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Inc/(dec) in debt</td><td>15.5</td><td>199.7</td><td>199.3</td><td>99.0</td></tr><tr><td>Other financing cash flows</td><td>427.5</td><td>620.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>426.1</td><td>818.6</td><td>198.2</td><td>97.8</td></tr><tr><td>Total cash flow</td><td>218.7</td><td>533.5</td><td>(313.5)</td><td>(183.8)</td></tr><tr><td>Free cash flow</td><td>(282.8)</td><td>(286.3)</td><td>(512.8)</td><td>(282.9)</td></tr></table>

Source: Company data, GS estimates.

capabilities: the company commented that their M2 model series outperformed peers in time-to-market and on price-to-performance earlier this year, but acknowledged its upcoming M3 Pro has lagged slightly as the company pursued a two-model within the M3 family and as the company was ramping up its self-operated computing clusters over 1Q26. With Chinese players' focused on post training data and reinforcement learning that is bringing coding performance uplift across the board (where MiniMax is focusing on as well), the company believes user switching between models can be fast and sees pricing/cost efficiencies/speed to become other drivers to user adoption amongst the handful of 3 trillions parameter sizes models to be launched from Chinese players over the next few months.

4) Multi-modal approach as a key differentiation, where the company continues to iterate/refine M3 multi-modal capabilities that will be applied to M3 Pro. Meanwhile, its upcoming H3 model will be more than a video-generation model (Hailuo) but a new architecture as an Omni-model, that understands all modals (text, image, video, audio, music) with stable output across video, image, audio based on user needs/prompts. The company expects imminent launch of its H3 model (that is in its final stages of launch preparations) with implications to the multi-modal industry landscape (offering alternatives to existing video generation products).

## Implications: We view multiple positive share price drivers from here; positive skewed risk-reward

With MiniMax eligible for Southbound Connect from Aug 2026 and given the steep market cap discount (US\$8.5bn) vs. China video-generation model peer Kling post-money valuation of US\$18bn (see our report) and Z.ai/Zhipu last close at US\$71bn, we view the company's articulated strategy in addressing M3 model competitiveness and imminent H3 multi-modal launch as positive drivers for ARR ramp up that could drive significant room for valuation repair over 2H 2026 (vs. ARR of US\$400mn+ in early June 2026 before M3 launch, at a run-rate likely at half of Zhipu at the mid-year mark 2026). We see a clear positive skew to risk-reward and reiterate Buy.

We continue to see MiniMax as well positioned amongst Chinese AI model companies to capture the significant global TAM growth potential across text/coding, multi-modal, agentic/co-worker (digital labor) and multi-modal generation on the back of its comprehensive multi-modal offerings, strong commercialization capability, AI model per token cost advantages and high organizational efficiency.

Key risks: Weaker-than-expected model performance amid competition in the global foundation model industry; Slower-than-expected path to profit visibility; Weaker-than-expected commercialization capabil

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
