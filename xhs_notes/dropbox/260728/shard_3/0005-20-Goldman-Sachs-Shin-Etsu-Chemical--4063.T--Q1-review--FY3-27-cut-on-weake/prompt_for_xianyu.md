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
# Shin-Etsu Chemical (4063.T)

# Q1 review: FY3/27 cut on weaker PVC outlook, but strong semiconductor and AI materials support FY3/28 onwards

4063.T

12m Price Target: ¥9,510

Price: ¥6,159

Upside: $54.4\%$

We have revised our earnings forecasts for Shin-Etsu Chemical following its Q1 results and our subsequent review of business trends. We cut our FY3/27 operating profit forecast by 5%, primarily reflecting a lower PVC pricing assumption in the Infrastructure segment. While the weaker PVC outlook also weighs on our FY3/28–29 forecasts, the impact is expected to be partially offset by strong growth in the Electronics Materials business—driven by silicon wafers, photoresists, and magnetic materials—as well as solid performance in Functional Materials, supported by silicones and new products. As a result, our FY3/28 and FY3/29 operating profit forecasts are reduced by only 2% and less than 1%, respectively.

The business environment for PVC from Q2 onward is clearly more challenging than we previously expected. The stock has corrected sharply, falling 8.3% between the Q1 earnings announcement and July 27 vs a 1.4% gain for TOPIX. However, we believe the market has largely priced in the anticipated downward consensus revisions. Shin-Etsu now trades at a relatively attractive valuation, while the contribution of the cyclical Infrastructure segment to company-wide operating profit is expected to decline to an average of 18% over FY3/27–29, down from a 42% average over the past five years.

In contrast, expanding demand for semiconductor materials and AI-related products—particularly in front-end semiconductor applications—should drive a CAGR of 19% in operating profit between FY3/26 and FY3/29. Against this backdrop, the stock is trading at 17x FY3/28 P/E, within its 10-year historical range of 14–21x and increasingly attractive in our view. We lower our target price slightly to ¥9,510 from ¥9,610 to reflect our revised earnings forecasts, but reiterate our Buy rating.

## BUY

Atsushi Ikeda
+81(3)4587-9940 | atsushi.ikeda@gs.com
GS Japan Co., Ltd.

Yuri Izumikawa
+81(3)4587-3643 | yuri.x.izumikawa@gs.com
GS Japan Co., Ltd.

Key Data

Market cap: ¥11.4tr / \$69.8bn  
Enterprise value: ¥10.5tr / \$64.0bn  
3m ADTV: ¥57.0bn / \$355.5mn  
Japan  
Japan Chemicals & Advanced Materials  
M&A Rank: 3  
Leases incl. in net debt & EV?: No

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Revenue (¥ bn)</td><td>2,574.0</td><td>2,863.7</td><td>3,155.5</td><td>3,496.5</td></tr><tr><td>Op. profit (¥ bn) New</td><td>635.2</td><td>738.4</td><td>873.3</td><td>1,065.1</td></tr><tr><td>Op. profit (¥ bn) Old</td><td>635.2</td><td>780.5</td><td>887.9</td><td>1,069.7</td></tr><tr><td>Op. profit CoE (¥ bn)</td><td>-</td><td>700.0</td><td>-</td><td>-</td></tr><tr><td>EPS (¥) New</td><td>255.5</td><td>307.9</td><td>370.2</td><td>445.5</td></tr><tr><td>EPS (¥) Old</td><td>255.5</td><td>322.8</td><td>374.6</td><td>445.7</td></tr><tr><td>P/E (X)</td><td>19.0</td><td>20.0</td><td>16.6</td><td>13.8</td></tr><tr><td>P/B (X)</td><td>2.0</td><td>2.6</td><td>2.5</td><td>2.5</td></tr><tr><td>CROCI (%)</td><td>10.3</td><td>11.0</td><td>12.1</td><td>13.4</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS (¥)</td><td>70.3</td><td>-</td><td>-</td><td>-</td></tr></table>

![](images/bb4e1ee4b846e5f3d6c8d7fb92c2db64c7fa9bdd5896ad8c2d0ebc0d2eda4607.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Shin-Etsu Chemical (4063.T)

Rating since Aug 15, 2019

Ratios & Valuation

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>P/E (X)</td><td>19.0</td><td>20.0</td><td>16.6</td><td>13.8</td></tr><tr><td>P/B (X)</td><td>2.0</td><td>2.6</td><td>2.5</td><td>2.5</td></tr><tr><td>FCF yield (%)</td><td>4.1</td><td>3.3</td><td>4.1</td><td>5.3</td></tr><tr><td>EV/EBITDAR (X)</td><td>8.8</td><td>10.2</td><td>8.8</td><td>7.5</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>8.8</td><td>10.2</td><td>8.8</td><td>7.5</td></tr><tr><td>CROCI (%)</td><td>10.3</td><td>11.0</td><td>12.1</td><td>13.4</td></tr><tr><td>ROE (%)</td><td>10.4</td><td>12.6</td><td>14.9</td><td>17.9</td></tr><tr><td>Net debt/equity (%)</td><td>(30.5)</td><td>(25.8)</td><td>(21.0)</td><td>(17.9)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(30.5)</td><td>(25.8)</td><td>(21.0)</td><td>(17.9)</td></tr><tr><td>Interest cover (X)</td><td>234.7</td><td>144.8</td><td>171.2</td><td>208.8</td></tr><tr><td>Days inventory outst, sales</td><td>110.7</td><td>105.5</td><td>103.6</td><td>99.4</td></tr><tr><td>Receivable days</td><td>74.5</td><td>72.1</td><td>72.4</td><td>72.2</td></tr><tr><td>Days payable outstanding</td><td>38.9</td><td>36.8</td><td>37.9</td><td>38.9</td></tr><tr><td>DuPont ROE (%)</td><td>10.2</td><td>12.2</td><td>14.1</td><td>16.6</td></tr><tr><td>Turnover (X)</td><td>0.5</td><td>0.5</td><td>0.6</td><td>0.6</td></tr><tr><td>Leverage (X)</td><td>1.2</td><td>1.2</td><td>1.2</td><td>1.2</td></tr><tr><td>Gross cash invested (ex cash) (¥)</td><td>6,992.9</td><td>7,346.8</td><td>7,774.2</td><td>8,215.7</td></tr><tr><td>Average capital employed (¥)</td><td>3,186.3</td><td>3,301.8</td><td>3,495.4</td><td>3,733.4</td></tr><tr><td>BVPS (¥)</td><td>2,404.5</td><td>2,409.1</td><td>2,472.4</td><td>2,509.5</td></tr></table>

Income Statement (¥ bn)

<table><tr><td colspan="5">Income Statement (EUR)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue</td><td>2,574.0</td><td>2,863.7</td><td>3,155.5</td><td>3,496.5</td></tr><tr><td>Cost of goods sold</td><td>(1,693.2)</td><td>(1,852.1)</td><td>(1,981.1)</td><td>(2,097.8)</td></tr><tr><td>SG&amp;A</td><td>(245.6)</td><td>(273.2)</td><td>(301.1)</td><td>(333.6)</td></tr><tr><td>R&amp;D</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>878.2</td><td>988.7</td><td>1,148.5</td><td>1,355.7</td></tr><tr><td>Depreciation &amp; amortization</td><td>(243.0)</td><td>(250.3)</td><td>(275.2)</td><td>(290.6)</td></tr><tr><td>EBIT</td><td>635.2</td><td>738.4</td><td>873.3</td><td>1,065.1</td></tr><tr><td>Net interest inc./(exp.)</td><td>60.2</td><td>64.9</td><td>66.9</td><td>67.9</td></tr><tr><td>Income/(loss) from associates</td><td>0.0</td><td>0.0</td><td>0.0</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>708.5</td><td>807.2</td><td>943.1</td><td>1,135.9</td></tr><tr><td>Provision for taxes</td><td>(202.2)</td><td>(217.9)</td><td>(254.6)</td><td>(306.7)</td></tr><tr><td>Minority interest</td><td>(31.8)</td><td>(35.2)</td><td>(41.6)</td><td>(50.7)</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>474.5</td><td>554.1</td><td>646.9</td><td>778.5</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>474.5</td><td>554.1</td><td>646.9</td><td>778.5</td></tr><tr><td>EPS (basic, pre-except) (¥)</td><td>255.5</td><td>307.9</td><td>370.2</td><td>445.5</td></tr><tr><td>EPS (diluted, pre-except) (¥)</td><td>255.5</td><td>307.9</td><td>370.2</td><td>445.5</td></tr><tr><td>EPS (basic, post-except) (¥)</td><td>255.5</td><td>307.9</td><td>370.2</td><td>445.5</td></tr><tr><td>EPS (diluted, post-except) (¥)</td><td>255.5</td><td>307.9</td><td>370.2</td><td>445.5</td></tr><tr><td>DPS (¥)</td><td>106.0</td><td>120.0</td><td>150.0</td><td>180.0</td></tr><tr><td>Div. payout ratio (%)</td><td>41.5</td><td>39.0</td><td>40.5</td><td>40.4</td></tr></table>

Growth & Margins (%)

<table><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Total revenue growth</td><td>0.5</td><td>11.3</td><td>10.2</td><td>10.8</td></tr><tr><td>EBITDA growth</td><td>(10.4)</td><td>12.6</td><td>16.2</td><td>18.0</td></tr><tr><td>EPS growth</td><td>(6.2)</td><td>20.5</td><td>20.2</td><td>20.3</td></tr><tr><td>DPS growth</td><td>0.0</td><td>13.2</td><td>25.0</td><td>20.0</td></tr><tr><td>EBIT margin</td><td>24.7</td><td>25.8</td><td>27.7</td><td>30.5</td></tr><tr><td>EBITDA margin</td><td>34.1</td><td>34.5</td><td>36.4</td><td>38.8</td></tr><tr><td>Net income margin</td><td>18.4</td><td>19.3</td><td>20.5</td><td>22.3</td></tr></table>

Price Performance  
![](images/318d822aacfd424eea0566d4bc1e011cea90f5e62eab47cdeda7a0ed58312a11.jpg)  
Source: FactSet. Price as of 27 Jul 2026 close.

Balance Sheet (¥ bn)

<table><tr><td colspan="5">Balance Sheet (+ bn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>1,660.1</td><td>1,415.6</td><td>1,206.1</td><td>1,082.1</td></tr><tr><td>Accounts receivable</td><td>535.4</td><td>595.6</td><td>656.3</td><td>727.3</td></tr><tr><td>Inventory</td><td>790.9</td><td>865.1</td><td>925.4</td><td>979.9</td></tr><tr><td>Other current assets</td><td>113.3</td><td>113.3</td><td>113.3</td><td>113.3</td></tr><tr><td>Total current assets</td><td>3,106.7</td><td>2,997.5</td><td>2,909.7</td><td>2,912.0</td></tr><tr><td>Net PP&amp;E</td><td>2,153.3</td><td>2,222.4</td><td>2,355.2</td><td>2,485.6</td></tr><tr><td>Net intangibles</td><td>34.7</td><td>34.7</td><td>34.7</td><td>34.7</td></tr><tr><td>Total investments</td><td>151.8</td><td>151.8</td><td>151.8</td><td>151.8</td></tr><tr><td>Other long-term assets</td><td>198.3</td><td>198.3</td><td>198.3</td><td>198.3</td></tr><tr><td>Total assets</td><td>5,644.8</td><td>5,604.7</td><td>5,649.8</td><td>5,782.4</td></tr><tr><td>Accounts payable</td><td>176.4</td><td>196.8</td><td>214.7</td><td>231.9</td></tr><tr><td>Short-term debt</td><td>6.9</td><td>6.9</td><td>6.9</td><td>6.9</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>343.3</td><td>343.3</td><td>343.3</td><td>343.3</td></tr><tr><td>Total current liabilities</td><td>526.7</td><td>547.1</td><td>565.0</td><td>582.2</td></tr><tr><td>Long-term debt</td><td>236.4</td><td>236.4</td><td>236.4</td><td>236.4</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>271.9</td><td>271.9</td><td>271.9</td><td>271.9</td></tr><tr><td>Total long-term liabilities</td><td>508.2</td><td>508.2</td><td>508.2</td><td>508.2</td></tr><tr><td>Total liabilities</td><td>1,034.9</td><td>1,055.3</td><td>1,073.2</td><td>1,090.4</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>4,464.4</td><td>4,335.3</td><td>4,320.9</td><td>4,385.6</td></tr><tr><td>Minority interest</td><td>178.9</td><td>214.1</td><td>255.7</td><td>306.4</td></tr><tr><td>Total liabilities &amp; equity</td><td>5,678.2</td><td>5,604.7</td><td>5,649.8</td><td>5,782.4</td></tr><tr><td>Net debt, adjusted</td><td>(1,416.8)</td><td>(1,172.3)</td><td>(962.8)</td><td>(838.8)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (¥ bn)</td></tr><tr><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Net income</td><td>474.5</td><td>554.1</td><td>646.9</td><td>778.5</td></tr><tr><td>D&amp;A add-back</td><td>243.0</td><td>250.3</td><td>275.2</td><td>290.6</td></tr><tr><td>Minority interest add-back</td><td>31.8</td><td>35.2</td><td>41.6</td><td>50.7</td></tr><tr><td>Net (inc)/dec working capital</td><td>(39.8)</td><td>(114.1)</td><td>(103.1)</td><td>(108.2)</td></tr><tr><td>Other operating cash flow</td><td>3.2</td><td>0.0</td><td>0.0</td><td>-</td></tr><tr><td>Cash flow from operations</td><td>712.7</td><td>725.5</td><td>860.6</td><td>1,011.6</td></tr><tr><td>Capital expenditures</td><td>(339.7)</td><td>(354.0)</td><td>(408.0)</td><td>(421.0)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(205.1)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(544.8)</td><td>(354.0)</td><td>(408.0)</td><td>(421.0)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(196.8)</td><td>(215.9)</td><td>(262.1)</td><td>(314.6)</td></tr><tr><td>Inc/(dec) in debt</td><td>(3.4)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>(272.0)</td><td>(400.0)</td><td>(400.0)</td><td>(400.0)</td></tr><tr><td>Cash flow from financing</td><td>(472.1)</td><td>(615.9)</td><td>(662.1)</td><td>(714.6)</td></tr><tr><td>Total cash flow</td><td>(304.3)</td><td>(244.4)</td><td>(209.5)</td><td>(124.0)</td></tr><tr><td>Free cash flow</td><td>373.0</td><td>371.5</td><td>452.6</td><td>590.6</td></tr></table>

Source: Company data, GS estimates.

## Electronics Materials

The Electronics Materials segment delivered a strong start to FY3/27, with Q1 operating profit rising 23% YoY and 19% QoQ. Among the segment's businesses, optical fiber preforms and rare-earth magnets recorded particularly strong profit growth, while photoresists, encapsulation materials, quartz substrates, and other products also achieved double-digit earnings growth. Semiconductor wafers posted more modest profit growth of around 5% YoY due to a high comparison base in the prior year. On a QoQ basis, encapsulation materials saw especially strong growth, while rare-earth magnets, semiconductor wafers, photomask blanks, and quartz substrates delivered profit growth broadly in line with the segment average. We estimate that photoresists achieved nearly 10% profit growth despite absorbing depreciation costs associated with the new Isesaki plant.

## Semiconductor Wafers

Management estimates that AI-related applications now account for nearly $30\%$ of 300mm wafer demand. Beyond GPUs, ASICs, and HBM, AI-driven demand is increasingly spreading to memory, power management ICs, and other supporting logic semiconductors, suggesting stronger-than-expected AI-related wafer consumption. This is important when assessing the future trajectory of 300mm wafer demand.

In addition, management indicated that bonded wafers used in applications such as CMOS Bonded on Array (CBA) for 3D NAND now account for nearly $10\%$ of total 300mm wafer demand. As advanced semiconductor applications increasingly require multiple wafers per device, this trend could provide a larger-than-expected boost to future 300mm wafer demand.

The company also highlighted rapidly increasing demand for process wafers, including dummy monitor wafers and test wafers required for new product and production-line ramp-ups. These developments represent further signs of near-term expansion in 300mm wafer demand and support our constructive outlook.

While we believe Shin-Etsu retains some brownfield expansion capacity, management reiterated that capacity additions will remain disciplined and primarily tied to customer commitments under long-term agreements. Based on ongoing contract negotiations, we expect greenfield investments will eventually become necessary. However, given the extremely high quality and cost requirements for leading-edge AI-related wafers, the company continues to take a cautious stance toward further capacity expansion.

This cautious approach is consistent with comments made by SUMCO President Jiro Tatsuta in a July 27 Nikkei XTECH interview, where he stated that while AI demand could persist for three to five years, wafer manufacturers should not rush capacity expansion at the expense of quality. With Japan's two dominant suppliers of advanced wafers demonstrating disciplined investment behavior, we expect investors to increasingly anticipate sustaine

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY

10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
