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
# Kakao Corp. (035720.KS)

# 2Q26E preview; Core Platform resilient; AI launch catalyst remains intact; Buy

035720.KS 12m Price Target: W49,000 Price: W34,650 Upside: $41.4\%$

We preview Kakao's 2Q26 results and expect a broadly solid quarter, supported by Platform revenue momentum. Talk Biz ads appear to have sustained YoY growth into 2Q, and Commerce should benefit from deferred revenue from the March Shopping Festa and Family Month promotions in May. That said, we would avoid being overly aggressive on margin despite positive Platform seasonality, given higher Piccoma marketing spend and the mechanical Portal Biz impact from AXZ deconsolidation.

The key near-term debate remains AI. Kakao's agentic AI service connection with vertical partners is still expected to launch before 2Q earnings, consistent with the official timeline. The important question is not whether Kakao has an AI roadmap, but whether the launch can demonstrate a tangible value proposition: connecting KakaoTalk conversation intent to high-frequency actions, partner services, and eventually transactions.

We maintain Buy with an unchanged 12m TP of W49k. The core earnings base is supported by Talk Biz, Commerce, Pay, Mobility, and restructuring, while AI expectations have already been reset. We think the upcoming agentic AI launch could be an important sentiment catalyst if it shows that Kakao can move beyond AI discovery and begin proving the connection-to-action thesis inside KakaoTalk.

Action: We revise our earnings estimates, reflecting: 1) the deconsolidation of Kakao's portal business with the completion of AXZ transaction in May, 2) solid growth momentum of core Talk Biz revenue, and 3) recent trends of Platform/Contents segment. As a result, our 2026E/27E/28E top line is revised down by -1%/-2%/-1% and our OP -5%/-6%/-3%. Our NP is revised down by -6%/-6%/-3%.

Catalyst: We expect Kakao's agentic AI service connection with vertical partners to launch before 2Q earnings (as guided by the management during 1Q earnings call) to be a key near-term catalyst.

## BUY

Eric Cha  
+82(2)3788-1799 | eric.cha@gs.com  
GS (Asia) L.L.C., Seoul Branch

Vona Lee  
+82(2)3788-1201 | vona.lee@gs.com  
GS (Asia) L.L.C., Seoul Branch

Market cap: W15.2tr / \$10.0bn  
Enterprise value: W10.3tr / \$6.8bn  
3m ADTV: W87.6bn / \$58.2mn  
South Korea  
Korea TMT & Consumer  
M&A Rank: 3  
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td colspan="5">GS Forecast</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (W bn) New</td><td>7,669.5</td><td>8,208.5</td><td>8,825.2</td><td>9,347.8</td></tr><tr><td>Revenue (W bn) Old</td><td>7,669.5</td><td>8,308.4</td><td>8,963.9</td><td>9,453.6</td></tr><tr><td>EBITDA (W bn)</td><td>1,560.9</td><td>1,721.0</td><td>1,944.4</td><td>2,162.8</td></tr><tr><td>EPS (W) New</td><td>1,655</td><td>1,582</td><td>1,730</td><td>2,024</td></tr><tr><td>EPS (W) Old</td><td>1,655</td><td>1,681</td><td>1,848</td><td>2,084</td></tr><tr><td>P/E (X)</td><td>31.3</td><td>21.9</td><td>20.0</td><td>17.1</td></tr><tr><td>P/B (X)</td><td>1.5</td><td>1.3</td><td>1.2</td><td>1.1</td></tr><tr><td>Dividend yield (%)</td><td>0.2</td><td>0.5</td><td>0.5</td><td>0.6</td></tr><tr><td>CROCI (%)</td><td>12.3</td><td>13.2</td><td>14.0</td><td>14.4</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (W)</td><td>374</td><td>415</td><td>441</td><td>353</td></tr></table>

GS Factor Profile

![](images/39b03fb0988019a5ae3ec355d72b0ca5a8bde116579c1706ba1ca076883a2dce.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Kakao Corp. (035720.KS)

Rating since Jul 16, 2025

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>31.3</td><td>21.9</td><td>20.0</td><td>17.1</td></tr><tr><td>P/B (X)</td><td>1.5</td><td>1.3</td><td>1.2</td><td>1.1</td></tr><tr><td>FCF yield (%)</td><td>3.5</td><td>6.1</td><td>5.7</td><td>5.5</td></tr><tr><td>EV/EBITDAR (X)</td><td>14.4</td><td>6.0</td><td>5.0</td><td>4.2</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>14.4</td><td>6.0</td><td>5.0</td><td>4.2</td></tr><tr><td>CROCI (%)</td><td>12.3</td><td>13.2</td><td>14.0</td><td>14.4</td></tr><tr><td>ROE (%)</td><td>6.8</td><td>6.0</td><td>6.2</td><td>6.9</td></tr><tr><td>Net debt/equity (%)</td><td>(27.8)</td><td>(41.4)</td><td>(44.5)</td><td>(46.6)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(27.8)</td><td>(41.4)</td><td>(44.5)</td><td>(46.6)</td></tr><tr><td>Interest cover (X)</td><td>2.2</td><td>4.1</td><td>5.2</td><td>5.8</td></tr><tr><td>Days inventory outst, sales</td><td>3.8</td><td>3.6</td><td>3.6</td><td>3.6</td></tr><tr><td>Receivable days</td><td>26.6</td><td>26.0</td><td>25.7</td><td>25.9</td></tr><tr><td>Days payable outstanding</td><td>164.1</td><td>166.2</td><td>164.8</td><td>168.1</td></tr><tr><td>DuPont ROE (%)</td><td>4.8</td><td>5.8</td><td>6.0</td><td>6.7</td></tr><tr><td>Turnover (X)</td><td>0.3</td><td>0.4</td><td>0.4</td><td>0.4</td></tr><tr><td>Leverage (X)</td><td>1.8</td><td>1.9</td><td>1.8</td><td>1.8</td></tr><tr><td>Gross cash invested (ex cash) (W)</td><td>11,769.6</td><td>11,230.6</td><td>12,069.7</td><td>13,153.2</td></tr><tr><td>Average capital employed (W)</td><td>10,487.1</td><td>8,995.7</td><td>7,001.2</td><td>7,060.2</td></tr><tr><td>BVPS (W)</td><td>34,639</td><td>27,180</td><td>28,657</td><td>30,336</td></tr></table>

Growth & Margins (%)

Income Statement (W bn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>7,669.5</td><td>8,208.5</td><td>8,825.2</td><td>9,347.8</td></tr><tr><td>Cost of goods sold</td><td>(4,523.1)</td><td>(4,767.5)</td><td>(5,003.3)</td><td>(5,232.7)</td></tr><tr><td>SG&amp;A</td><td>(1,245.5)</td><td>(1,332.9)</td><td>(1,477.5)</td><td>(1,552.3)</td></tr><tr><td>R&amp;D</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other operating inc./(exp.)</td><td>(1,129.8)</td><td>(1,204.1)</td><td>(1,308.4)</td><td>(1,397.2)</td></tr><tr><td>EBITDA</td><td>1,560.9</td><td>1,721.0</td><td>1,944.4</td><td>2,162.8</td></tr><tr><td>Depreciation &amp; amortization</td><td>(789.8)</td><td>(817.0)</td><td>(908.4)</td><td>(997.2)</td></tr><tr><td>EBIT</td><td>771.1</td><td>904.0</td><td>1,036.0</td><td>1,165.6</td></tr><tr><td>Net interest inc./(exp.)</td><td>85.3</td><td>40.3</td><td>50.0</td><td>50.0</td></tr><tr><td>Income/(loss) from associates</td><td>92.7</td><td>102.0</td><td>80.0</td><td>80.0</td></tr><tr><td>Pre-tax profit</td><td>892.7</td><td>916.3</td><td>996.0</td><td>1,125.6</td></tr><tr><td>Provision for taxes</td><td>(139.0)</td><td>(193.1)</td><td>(239.0)</td><td>(270.1)</td></tr><tr><td>Minority interest</td><td>(26.5)</td><td>(27.0)</td><td>4.3</td><td>35.3</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>727.3</td><td>696.3</td><td>761.3</td><td>890.8</td></tr><tr><td>Post-tax exceptionals</td><td>(90.0)</td><td>7.0</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>637.3</td><td>703.3</td><td>761.3</td><td>890.8</td></tr><tr><td>EPS (basic, pre-except) (W)</td><td>1,655</td><td>1,582</td><td>1,730</td><td>2,024</td></tr><tr><td>EPS (diluted, pre-except) (W)</td><td>1,655</td><td>1,582</td><td>1,730</td><td>2,024</td></tr><tr><td>EPS (basic, post-except) (W)</td><td>1,450</td><td>1,598</td><td>1,730</td><td>2,024</td></tr><tr><td>EPS (diluted, post-except) (W)</td><td>1,450</td><td>1,598</td><td>1,730</td><td>2,024</td></tr><tr><td>DPS (W)</td><td>89</td><td>166</td><td>172</td><td>194</td></tr><tr><td>Div. payout ratio (%)</td><td>5.3</td><td>10.5</td><td>9.9</td><td>9.6</td></tr></table>

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(2.5)</td><td>7.0</td><td>7.5</td><td>5.9</td></tr><tr><td>EBITDA growth</td><td>15.2</td><td>10.3</td><td>13.0</td><td>11.2</td></tr><tr><td>EPS growth</td><td>578.6</td><td>(4.4)</td><td>9.3</td><td>17.0</td></tr><tr><td>DPS growth</td><td>(10.6)</td><td>87.5</td><td>3.7</td><td>13.0</td></tr><tr><td>EBIT margin</td><td>10.1</td><td>11.0</td><td>11.7</td><td>12.5</td></tr><tr><td>EBITDA margin</td><td>20.4</td><td>21.0</td><td>22.0</td><td>23.1</td></tr><tr><td>Net income margin</td><td>9.5</td><td>8.5</td><td>8.6</td><td>9.5</td></tr></table>

Price Performance  
![](images/19facb380095728555fbea41f79fb76b48077872ba312e0ade42619a320d4164.jpg)  
Source: FactSet. Price as of 8 Jul 2026 close.

Balance Sheet (W bn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>6,373.8</td><td>6,893.7</td><td>7,393.7</td><td>7,877.2</td></tr><tr><td>Accounts receivable</td><td>569.5</td><td>598.4</td><td>643.3</td><td>681.4</td></tr><tr><td>Inventory</td><td>76.5</td><td>84.3</td><td>90.7</td><td>96.0</td></tr><tr><td>Other current assets</td><td>5,354.4</td><td>5,397.0</td><td>5,493.6</td><td>5,566.2</td></tr><tr><td>Total current assets</td><td>12,374.2</td><td>12,973.4</td><td>13,621.3</td><td>14,220.8</td></tr><tr><td>Net PP&amp;E</td><td>1,556.7</td><td>1,572.3</td><td>1,588.0</td><td>1,603.9</td></tr><tr><td>Net intangibles</td><td>5,227.8</td><td>4,182.2</td><td>3,345.8</td><td>2,676.6</td></tr><tr><td>Total investments</td><td>2,516.9</td><td>2,218.4</td><td>3,082.7</td><td>3,944.6</td></tr><tr><td>Other long-term assets</td><td>6,108.0</td><td>1,270.0</td><td>1,373.5</td><td>1,450.8</td></tr><tr><td>Total assets</td><td>27,783.5</td><td>22,216.3</td><td>23,011.2</td><td>23,896.7</td></tr><tr><td>Accounts payable</td><td>2,164.7</td><td>2,177.0</td><td>2,340.5</td><td>2,479.1</td></tr><tr><td>Short-term debt</td><td>1,144.2</td><td>938.3</td><td>769.4</td><td>630.9</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>5,470.8</td><td>5,565.4</td><td>5,662.5</td><td>5,762.4</td></tr><tr><td>Total current liabilities</td><td>8,779.7</td><td>8,680.6</td><td>8,772.5</td><td>8,872.4</td></tr><tr><td>Long-term debt</td><td>990.5</td><td>1,000.5</td><td>1,010.5</td><td>1,020.5</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>2,788.3</td><td>574.6</td><td>617.8</td><td>654.3</td></tr><tr><td>Total long-term liabilities</td><td>3,778.9</td><td>1,575.1</td><td>1,628.3</td><td>1,674.9</td></tr><tr><td>Total liabilities</td><td>12,558.6</td><td>10,255.8</td><td>10,400.8</td><td>10,547.3</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>11,276.2</td><td>11,933.5</td><td>12,614.8</td><td>13,384.7</td></tr><tr><td>Minority interest</td><td>3,948.7</td><td>27.0</td><td>(4.3)</td><td>(35.3)</td></tr><tr><td>Total liabilities &amp; equity</td><td>27,783.5</td><td>22,216.3</td><td>23,011.2</td><td>23,896.7</td></tr><tr><td>Net debt, adjusted</td><td>(4,239.0)</td><td>(4,954.9)</td><td>(5,613.7)</td><td>(6,225.8)</td></tr></table>

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>663.8</td><td>730.3</td><td>757.0</td><td>855.5</td></tr><tr><td>D&amp;A add-back</td><td>789.8</td><td>817.0</td><td>908.4</td><td>997.2</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(48.1)</td><td>(48.1)</td><td>(48.1)</td><td>(48.1)</td></tr><tr><td>Other operating cash flow</td><td>(0.6)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from operations</td><td>1,404.8</td><td>1,499.2</td><td>1,617.2</td><td>1,804.5</td></tr><tr><td>Capital expenditures</td><td>(479.2)</td><td>(575.0)</td><td>(747.5)</td><td>(971.8)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>1.0</td><td>(135.2)</td><td>(135.2)</td><td>(135.2)</td></tr><tr><td>Cash flow from investing</td><td>(478.2)</td><td>(710.2)</td><td>(882.7)</td><td>(1,107.0)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(38.9)</td><td>(73.0)</td><td>(75.7)</td><td>(85.5)</td></tr><tr><td>Inc/(dec) in debt</td><td>(80.3)</td><td>(196.0)</td><td>(158.9)</td><td>(128.5)</td></tr><tr><td>Other financing cash flows</td><td>(603.3)</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>(722.5)</td><td>(269.0)</td><td>(234.6)</td><td>(214.0)</td></tr><tr><td>Total cash flow</td><td>204.0</td><td>520.0</td><td>499.9</td><td>483.5</td></tr><tr><td>Free cash flow</td><td>925.6</td><td>924.2</td><td>869.7</td><td>832.8</td></tr></table>

Source: Company data, GS estimates.

That said, we believe investor focus should be less on the launch itself, and more on evidence of repeat usage, partner expansion, transaction completion and user engagement that could gradually validate Kakao's AI monetization framework.

## Key numbers

We expect 2Q consolidated top line to come in at W2trn (+6% YoY and +5% QoQ) and OP W214bn (+5% YoY and +1% QoQ), broadly in-line with BBG consensus: While top line growth momentum should be supported by Talk Biz ads (+20% YoY), Commerce (+16%), Mobility (+10%), and Pay (+26% YoY), we expect Portal Biz impact from AXZ deconsolidation from May to slightly offset revenue growth (expect Portal Biz revenue to decline -40% YoY). Meanwhile, on OP, we expect relatively high marketing spend on Piccoma to slightly pressure margins.

## ■ Key numbers to track (thesis pillars):

Core Platform recovery: We continue to monitor Talk Biz growth, Biz Message expansion, advertising inventory improvement following the KakaoTalk revamp, and operating leverage. We believe these remain the primary near-term earnings drivers and now carry greater weight within our investment thesis.

☐ Portfolio restructuring and earnings quality improvement: We will look for continued reduction in non-core subsidiary losses and improvements in consolidated earnings visibility. Successful execution should help to improve earnings quality and allow management to focus more clearly on core operations.

☐ AI ecosystem development: Rather than headline product launches, we focus on measurable ecosystem progress including external partner onboarding, breadth of vertical integrations, and management commentary regarding commercial deployment. Broader ecosystem participation would increase our confidence in Kakao's LT AI monetization framework.

☐ User engagement and transaction conversion: We believe the key proof point is whether users increasingly complete tasks directly within KakaoTalk, including search, reservations, commerce and payment-linked actions. Repeat user behavior is likely to matter more than initial download metrics.

□ Early monetization evidence: We will monitor disclosure around AI-assisted search advertising, CPS economics and transaction-linked revenue contribution. We believe meaningful valuation expansion requires evidence that AI usage can translate into sustainable economic value.

## 2Q26E earnings preview

We expect 2Q consolidated top line to come in at W2trn (+6% YoY and +5% QoQ) and OP W214bn (+5% YoY and +1% QoQ), broadly in-line with BBG consensus. While top line growth momentum should be supported by Talk Biz ads, Commerce, Mobility, and Pay, we expect Portal Biz impact from AXZ deconsolidation from May to slightly offset revenue growth. Meanwhile, on OP, we expec

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
