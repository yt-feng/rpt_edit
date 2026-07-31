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
# Tokyo Electron (8035.T)

Earnings Review: 1Q in line, but stronger outlook from 2Q brings FY3/27 operating profits of ¥1 tn into view; margin improvement progress appears ahead of expectations; reiterate Buy

8035.T

12m Price Target: ¥86,000

Price: ¥52,250

Upside: 64.6%

## FY3/27 operating profits of ¥1 tn now in sight

1Q3/27 operating profits of ¥211.4 bn, reported after the July 30 close, were in line with our estimate of ¥215.0 bn and the Bloomberg consensus of just over ¥210 bn, but the gross margin came in high at 46.8%, leaving a positive impression from a profitability perspective. 1H3/27 operating profit guidance was revised up to ¥458 bn from ¥431 bn, which is above our previous estimate and the Bloomberg consensus. Although full-year guidance has not been disclosed, management noted that it expects growth in 2H to substantially exceed that in 1H and that full-year operating profits of ¥1 tn are now in sight (the Bloomberg consensus is just under ¥950 bn). We think this outlook should comfortably satisfy the market's high expectations.

## Key takeaways from the results briefing

(1) Business environment: Tokyo Electron (TEL) expects the WFE market to continue growing by over 20% yoy to over \$150 bn in CY26 and over \$190 bn in CY27, adding that it sees ample potential for the growth rate to expand further. With investment in advanced devices expanding, TEL aims to achieve sales growth that outpaces the WFE market (its sales expectations for equipment used in advanced packaging and etching equipment for DRAM wiring processes are higher than they were three months ago). As regards production capacity, the company has established a framework capable of meeting demand based on customer forecasts for the next two years.

BUY

(2) Pricing strategy: As part of its initiatives to improve profitability, management is working on optimizing pricing, and it expects to see marked benefits emerging from 4Q3/27. Regarding the target of a gross margin of 50% or higher over the next two years, the company is taking steps to achieve this level early in FY3/28.

Shuhei Nakamura
+81(3)4587-9932 | shuhei.nakamura@gs.com
GS Japan Co., Ltd.

Kaho Otake
+81(3)4587-7498 | kaho.otake@gs.com
GS Japan Co., Ltd.

Key Data

Market cap: ¥23.9tr / \$146.1bn
Enterprise value: ¥23.5tr / \$143.5bn
3m ADTV: ¥267.6bn / \$1.7bn
Japan
Japan Semiconductor, SPE & Precision
M&A Rank: 3
Leases incl. in net debt & EV?: No

GS Forecast

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Revenue (¥ bn)</td><td>2,443.5</td><td>3,402.6</td><td>4,344.3</td><td>4,917.6</td></tr><tr><td>Op. profit (¥ bn) New</td><td>624.9</td><td>1,022.4</td><td>1,498.1</td><td>1,786.3</td></tr><tr><td>Op. profit (¥ bn) Old</td><td>624.9</td><td>914.0</td><td>1,360.3</td><td>1,629.7</td></tr><tr><td>Op. profit CoE (¥ bn)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EPS (¥) New</td><td>1,263.0</td><td>1,765.1</td><td>2,619.6</td><td>3,173.0</td></tr><tr><td>EPS (¥) Old</td><td>1,263.0</td><td>1,594.9</td><td>2,404.2</td><td>2,926.6</td></tr><tr><td>P/E (X)</td><td>23.4</td><td>29.6</td><td>19.9</td><td>16.5</td></tr><tr><td>P/B (X)</td><td>6.5</td><td>10.2</td><td>8.9</td><td>7.6</td></tr><tr><td>CROCI (%)</td><td>27.6</td><td>41.3</td><td>49.6</td><td>52.0</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS (¥)</td><td>355.0</td><td>444.7</td><td>421.8</td><td>543.6</td></tr></table>

GS Factor Profile

![](images/ad6990d86566e52984c437fc71ea5aab266babf5f67a2b52711f8a280b480dd1.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Tokyo Electron (8035.T)

Rating since Jul 24, 2020

Price Performance  
Ratios & Valuation

<table><tr><td colspan="5">Ratios &amp; Valuation</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>P/E (X)</td><td>23.4</td><td>29.6</td><td>19.9</td><td>16.5</td></tr><tr><td>P/B (X)</td><td>6.5</td><td>10.2</td><td>8.9</td><td>7.6</td></tr><tr><td>FCF yield (%)</td><td>2.4</td><td>2.0</td><td>3.6</td><td>5.4</td></tr><tr><td>EV/EBITDAR (X)</td><td>18.4</td><td>20.7</td><td>14.2</td><td>11.6</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>18.4</td><td>20.7</td><td>14.2</td><td>11.6</td></tr><tr><td>CROCI (%)</td><td>27.6</td><td>41.3</td><td>49.6</td><td>52.0</td></tr><tr><td>ROE (%)</td><td>29.3</td><td>36.4</td><td>47.3</td><td>49.6</td></tr><tr><td>Net debt/equity (%)</td><td>(24.5)</td><td>(18.3)</td><td>(14.6)</td><td>(20.4)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(24.5)</td><td>(18.3)</td><td>(14.6)</td><td>(20.4)</td></tr><tr><td>Interest cover (X)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Days inventory outst, sales</td><td>109.2</td><td>84.5</td><td>78.1</td><td>75.7</td></tr><tr><td>Receivable days</td><td>75.5</td><td>63.6</td><td>61.3</td><td>61.6</td></tr><tr><td>Days payable outstanding</td><td>32.2</td><td>30.5</td><td>31.8</td><td>33.3</td></tr><tr><td>DuPont ROE (%)</td><td>27.8</td><td>34.4</td><td>44.8</td><td>46.3</td></tr><tr><td>Turnover (X)</td><td>0.9</td><td>1.1</td><td>1.3</td><td>1.3</td></tr><tr><td>Leverage (X)</td><td>1.4</td><td>1.4</td><td>1.3</td><td>1.3</td></tr><tr><td>Gross cash invested (ex cash) (¥)</td><td>1,962.6</td><td>2,364.7</td><td>2,770.5</td><td>3,021.6</td></tr><tr><td>Average capital employed (¥)</td><td>1,461.4</td><td>1,729.0</td><td>2,057.2</td><td>2,302.3</td></tr><tr><td>BVPS (¥)</td><td>4,550.9</td><td>5,128.5</td><td>5,849.9</td><td>6,850.0</td></tr></table>

Income Statement (¥ bn)

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue</td><td>2,443.5</td><td>3,402.6</td><td>4,344.3</td><td>4,917.6</td></tr><tr><td>Cost of goods sold</td><td>(1,335.7)</td><td>(1,794.7)</td><td>(2,181.2)</td><td>(2,406.0)</td></tr><tr><td>SG&amp;A</td><td>(232.9)</td><td>(307.6)</td><td>(335.0)</td><td>(355.3)</td></tr><tr><td>R&amp;D</td><td>(250.0)</td><td>(277.9)</td><td>(330.0)</td><td>(370.0)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>705.9</td><td>1,122.4</td><td>1,610.9</td><td>1,910.3</td></tr><tr><td>Depreciation &amp; amortization</td><td>(81.0)</td><td>(100.0)</td><td>(112.8)</td><td>(124.0)</td></tr><tr><td>EBIT</td><td>624.9</td><td>1,022.4</td><td>1,498.1</td><td>1,786.3</td></tr><tr><td>Net interest inc./(exp.)</td><td>2.0</td><td>4.0</td><td>4.5</td><td>5.0</td></tr><tr><td>Income/(loss) from associates</td><td>2.7</td><td>2.0</td><td>2.0</td><td>2.0</td></tr><tr><td>Pre-tax profit</td><td>748.2</td><td>1,035.9</td><td>1,512.1</td><td>1,800.8</td></tr><tr><td>Provision for taxes</td><td>(173.7)</td><td>(237.8)</td><td>(347.3)</td><td>(413.7)</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>574.5</td><td>798.1</td><td>1,164.8</td><td>1,387.1</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>574.5</td><td>798.1</td><td>1,164.8</td><td>1,387.1</td></tr><tr><td>EPS (basic, pre-except) (¥)</td><td>1,263.0</td><td>1,765.1</td><td>2,619.6</td><td>3,173.0</td></tr><tr><td>EPS (diluted, pre-except) (¥)</td><td>1,263.0</td><td>1,765.1</td><td>2,619.6</td><td>3,173.0</td></tr><tr><td>EPS (basic, post-except) (¥)</td><td>1,263.0</td><td>1,765.1</td><td>2,619.6</td><td>3,173.0</td></tr><tr><td>EPS (diluted, post-except) (¥)</td><td>1,263.0</td><td>1,765.1</td><td>2,619.6</td><td>3,173.0</td></tr><tr><td>DPS (¥)</td><td>628.0</td><td>883.0</td><td>1,310.0</td><td>1,587.0</td></tr><tr><td>Div. payout ratio (%)</td><td>49.7</td><td>50.0</td><td>50.0</td><td>50.0</td></tr></table>

Growth & Margins (%)

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue growth</td><td>0.5</td><td>39.2</td><td>27.7</td><td>13.2</td></tr><tr><td>EBITDA growth</td><td>(7.1)</td><td>59.0</td><td>43.5</td><td>18.6</td></tr><tr><td>EPS growth</td><td>6.3</td><td>39.8</td><td>48.4</td><td>21.1</td></tr><tr><td>DPS growth</td><td>6.1</td><td>40.6</td><td>48.4</td><td>21.1</td></tr><tr><td>EBIT margin</td><td>25.6</td><td>30.0</td><td>34.5</td><td>36.3</td></tr><tr><td>EBITDA margin</td><td>28.9</td><td>33.0</td><td>37.1</td><td>38.8</td></tr><tr><td>Net income margin</td><td>23.5</td><td>23.5</td><td>26.8</td><td>28.2</td></tr></table>

![](images/fc4ce5411a6e04dbd7a7289333aed7d4383523857d48e356849c309adfe0e133.jpg)  
Source: FactSet. Price as of 30 Jul 2026 close.

<table><tr><td colspan="5">Balance Sheet (¥ bn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>506.3</td><td>424.6</td><td>381.0</td><td>610.0</td></tr><tr><td>Accounts receivable</td><td>525.9</td><td>659.1</td><td>799.4</td><td>859.7</td></tr><tr><td>Inventory</td><td>713.1</td><td>862.4</td><td>995.7</td><td>1,043.4</td></tr><tr><td>Other current assets</td><td>90.2</td><td>90.2</td><td>90.2</td><td>90.2</td></tr><tr><td>Total current assets</td><td>1,835.5</td><td>2,036.3</td><td>2,266.4</td><td>2,603.2</td></tr><tr><td>Net PP&amp;E</td><td>589.3</td><td>679.3</td><td>766.5</td><td>842.5</td></tr><tr><td>Net intangibles</td><td>37.5</td><td>37.5</td><td>37.5</td><td>37.5</td></tr><tr><td>Total investments</td><td>225.5</td><td>227.5</td><td>229.5</td><td>231.5</td></tr><tr><td>Other long-term assets</td><td>173.2</td><td>173.2</td><td>173.2</td><td>173.2</td></tr><tr><td>Total assets</td><td>2,861.0</td><td>3,153.8</td><td>3,473.1</td><td>3,887.9</td></tr><tr><td>Accounts payable</td><td>127.8</td><td>171.8</td><td>208.8</td><td>230.3</td></tr><tr><td>Short-term debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>551.4</td><td>551.4</td><td>551.4</td><td>551.4</td></tr><tr><td>Total current liabilities</td><td>679.2</td><td>723.2</td><td>760.2</td><td>781.7</td></tr><tr><td>Long-term debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>111.8</td><td>111.8</td><td>111.8</td><td>111.8</td></tr><tr><td>Total long-term liabilities</td><td>111.8</td><td>111.8</td><td>111.8</td><td>111.8</td></tr><tr><td>Total liabilities</td><td>791.0</td><td>834.9</td><td>871.9</td><td>893.5</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>2,070.0</td><td>2,318.8</td><td>2,601.2</td><td>2,994.5</td></tr><tr><td>Minority interest</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total liabilities &amp; equity</td><td>2,861.0</td><td>3,153.8</td><td>3,473.1</td><td>3,887.9</td></tr><tr><td>Net debt, adjusted</td><td>(506.3)</td><td>(424.6)</td><td>(381.0)</td><td>(610.0)</td></tr></table>

<table><tr><td colspan="5">Cash flow (€ bn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Net income</td><td>574.5</td><td>798.1</td><td>1,164.8</td><td>1,387.1</td></tr><tr><td>D&amp;A add-back</td><td>81.0</td><td>100.0</td><td>112.8</td><td>124.0</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>32.4</td><td>(238.5)</td><td>(236.7)</td><td>(86.4)</td></tr><tr><td>Other operating cash flow</td><td>(148.1)</td><td>(2.0)</td><td>(2.0)</td><td>(2.0)</td></tr><tr><td>Cash flow from operations</td><td>539.7</td><td>657.6</td><td>1,038.9</td><td>1,422.7</td></tr><tr><td>Capital expenditures</td><td>(216.0)</td><td>(190.0)</td><td>(200.0)</td><td>(200.0)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>119.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(96.5)</td><td>(190.0)</td><td>(200.0)</td><td>(200.0)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(285.6)</td><td>(399.2)</td><td>(582.5)</td><td>(693.8)</td></tr><tr><td>Inc/(dec) in debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>(147.6)</td><td>(150.0)</td><td>(300.0)</td><td>(300.0)</td></tr><tr><td>Cash flow from financing</td><td>(433.2)</td><td>(549.2)</td><td>(882.5)</td><td>(993.8)</td></tr><tr><td>Total cash flow</td><td>10.0</td><td>(81.7)</td><td>(43.5)</td><td>228.9</td></tr><tr><td>Free cash flow</td><td>323.7</td><td>467.6</td><td>838.9</td><td>1,222.7</td></tr></table>

Source: Company data, GS estimates.

<table><tr><td colspan="19">Tokyo Electron (8035.T)</td></tr><tr><td>(JPY mn)</td><td></td><td>GSE</td><td>GSE</td><td>GSE</td><td>CoE</td><td></td><td></td><td>Old: CoE</td><td>New: CoE</td><td></td><td></td><td></td><td></td><td>GSE</td><td>GSE</td><td>GSE</td><td>CoE</td><td></td></tr><tr><td>Consolidated income statement</td><td>3/2026</td><td>3/2027</td><td>3/2028</td><td>3/2029</td><td>3/2027</td><td>3/2026 1H</td><td>3/2026 2H</td><td>3/2027 1H</td><td>3/2027 1H</td><td>3/2026 1Q</td><td>3/2026 2Q</td><td>3/2026 3Q</td><td>3/2026 4Q</td><td>3/2027 1Q</td><td>3/2027 2Q</td><td>3/2027 3Q</td><td>3/2027 4Q</td><td>3/2027 2Q</td></tr><tr><td>Sales</td><td>2,443,533</td><td>3,402,600</td><td>4,344,300</td><td>4,917,600</td><td></td><td>1,179,668</td><td>1,263,865</td><td>1,570,000</td><td>1,620,000</td><td>549,586</td><td>630,082</td><td>552,047</td><td>711,818</td><td>732,388</td><td>902,000</td><td>842,000</td><td>926,212</td><td>887,612</td></tr><tr><td>Operating profits</td><td>624,936</td><td>1,022,400</td><td>1,498,100</td><td>1,786,300</td><td></td><td>303,153</td><td>321,783</td><td>431,000</td><td>458,000</td><td>144,694</td><td>158,459</td><td>116,140</td><td>205,643</td><td>211,407</td><td>264,400</td><td>250,700</td><td>295,893</td><td>246,593</td></tr><tr><td>Recurring profits</td><td>630,338</td><td>1,035,900</td><td>1,512,100</td><td>1,800,800</td><td></td><td>306,896</td><td>323,442</td><td>437,000</td><td>464,000</td><td>147,347</td><td>159,549</td><td>116,900</td><td>206,542</td><td>215,626</td><td>267,400</td><td>253,700</td><td>299,174</td><td>248,374</td></tr><tr><td>Net income</td><td>574,454</td><td>798,100</td><td>1,164,800</td><td>1,387,100</td><td></td><td>241,626</td><td>332,828</td><td>328,000</td><td>349,000</td><td>117,801</td><td>123,825</td><td>118,538</td><td>214,290</td><td>164,341</td><td>205,900</td><td>195,300</td><td>232,559</td><td>184,659</td></tr><tr><td>EBITDA</td><td>705,918</td><td>1,122,400</td><td>1,610,900</td><td>1,910,300</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross profits</td><td>45.3%</td><td>47.3%</td><td>49.8%</td><td>51.1%</td><td></td><td>45.7%</td><td>45.0%</td><td>45.5%</td><td>46.2%</td><td>46.2%</td><td>45.2%</td><td>42.7%</td><td>46.8%</td><td>46.8%</td><td>46.5%</td><td>47.0%</td><td>48.6%</td><td>45.7%</td></tr><tr><td>Operating profits</td><td>25.6%</td><td>30.0%</td><td>34.5%</td><td>36.3%</td><td></td><td>25.7%</td><td>25.5%</td><td>27.5%</td><td>28.3%</td><td>26.3%</td><td>25.1%</td><td>21.0%</td><td>28.9%</td><td>28.9%</td><t

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
