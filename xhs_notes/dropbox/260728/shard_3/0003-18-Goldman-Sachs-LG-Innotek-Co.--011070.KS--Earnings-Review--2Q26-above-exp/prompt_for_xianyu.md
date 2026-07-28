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
# LG Innotek Co. (011070.KS)

Earnings Review: 2Q26 above expectations, however expect limited margin expansion in 2H26; Neutral

011070.KS 12m Price Target: W860,000 Price: W614,000 Upside: $40.1\%$

2Q26 revenue/OP beat mainly from strength in camera modules LG Innotek (LGI) reported 2Q26 revenue of W5.5tn and OP of W246bn, where revenue was higher than both GSe and Bloomberg consensus of W5.1tn, and OP was also higher compared to GSe of W200bn and consensus estimate of W196bn. We believe the revenue beat came from the strength in both camera module and package substrates, especially with the favorable product mix for the former in addition to the F/X tailwinds. We believe the OP beat likely came from the stronger revenue and higher-than-expected camera module margin. Despite the strong results, we lower our 2H26 earnings expectations as we expect limited margin expansion from the camera module business, and lower TP to W860K while maintaining our Neutral rating.

## Key takeaways

\- Optics Solution (camera module and 3D sensor): After a solid beat the business saw in 1Q26, optics revenue/margin in 2Q26 was again better-than-expected likely due to solid iPhone demand, improved product mix, and F/X tailwinds. From the low base in 2Q25, revenue grew by $48\%$ yoy for the business, and we believe margin recovered by more than $4\%$ pt yoy with the significant revenue growth and favorable F/X. We expect the factors that led to the 2Q26 beat to continue to push for a strong yoy revenue growth in 3Q26E, however, we do not expect a material margin improvement both on a qoq and yoy basis as the higher memory cost could start to act as a more material headwind in 2H26E and increasingly offset the positive impact from the higher revenue. Our updated 3Q26E optics revenue is W5.3tn (+18% qoq and +19% yoy), with $3.2\%$ operating margin (vs. $3.6\%$ OPM in 3Q25).

## ■ Package Solution (package substrates and display solutions):

## NEUTRAL

Giuni Lee
+82(2)3788-1177 | giuni.lee@gs.com
GS (Asia) L.L.C., Seoul Branch

Taeyong Lee
+82(2)3788-0981 | taeyong.lee@gs.com
GS (Asia) L.L.C., Seoul Branch

Daiki Takayama
+81(3)4587-9870 | daiki.takayama@gs.com
GS Japan Co., Ltd.

## Key Data

Market cap: W14.5tr / \$9.9bn  
Enterprise value: W15.6tr / \$10.7bn  
3m ADTV: W440.2bn / \$291.1mn  
South Korea  
Korea Technology  
M&A Rank: 3  
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (W bn) New</td><td>21,896.6</td><td>24,515.6</td><td>25,145.8</td><td>28,178.8</td></tr><tr><td>Revenue (W bn) Old</td><td>21,896.6</td><td>24,713.3</td><td>26,045.9</td><td>28,378.5</td></tr><tr><td>EBITDA (W bn)</td><td>1,815.3</td><td>2,173.7</td><td>2,396.4</td><td>2,933.2</td></tr><tr><td>EPS (W) New</td><td>14,421</td><td>35,619</td><td>39,249</td><td>53,237</td></tr><tr><td>EPS (W) Old</td><td>14,421</td><td>36,916</td><td>42,732</td><td>54,481</td></tr><tr><td>P/E (X)</td><td>12.4</td><td>17.2</td><td>15.6</td><td>11.5</td></tr><tr><td>P/B (X)</td><td>0.7</td><td>2.1</td><td>1.9</td><td>1.6</td></tr><tr><td>Dividend yield (%)</td><td>1.1</td><td>0.7</td><td>1.0</td><td>1.2</td></tr><tr><td>CROCI (%)</td><td>13.2</td><td>7.9</td><td>11.1</td><td>12.0</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS (W)</td><td>7,170</td><td>7,326</td><td>11,440</td><td>7,285</td></tr></table>

GS Factor Profile

![](images/32ba04667d22b02775eb43f48253d8ebceb901e4e99a852cf984661ad2cb6d65.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## LG Innotek Co. (011070.KS)

Rating since Jan 10, 2019

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>12.4</td><td>17.2</td><td>15.6</td><td>11.5</td></tr><tr><td>P/B (X)</td><td>0.7</td><td>2.1</td><td>1.9</td><td>1.6</td></tr><tr><td>FCF yield (%)</td><td>16.7</td><td>(2.3)</td><td>(1.9)</td><td>4.2</td></tr><tr><td>EV/EBITDAR (X)</td><td>2.8</td><td>7.2</td><td>6.7</td><td>5.3</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>2.8</td><td>7.3</td><td>6.8</td><td>5.4</td></tr><tr><td>CROCI (%)</td><td>13.2</td><td>7.9</td><td>11.1</td><td>12.0</td></tr><tr><td>ROE (%)</td><td>6.1</td><td>13.2</td><td>12.6</td><td>15.1</td></tr><tr><td>Net debt/equity (%)</td><td>15.2</td><td>15.9</td><td>19.4</td><td>12.0</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>14.8</td><td>15.6</td><td>19.2</td><td>11.8</td></tr><tr><td>Interest cover (X)</td><td>7.6</td><td>13.3</td><td>14.8</td><td>20.0</td></tr><tr><td>Days inventory outst, sales</td><td>28.0</td><td>32.1</td><td>40.8</td><td>40.7</td></tr><tr><td>Receivable days</td><td>51.5</td><td>48.5</td><td>48.1</td><td>46.4</td></tr><tr><td>Days payable outstanding</td><td>44.2</td><td>44.0</td><td>45.6</td><td>44.2</td></tr><tr><td>DuPont ROE (%)</td><td>5.9</td><td>12.1</td><td>11.9</td><td>14.1</td></tr><tr><td>Turnover (X)</td><td>1.8</td><td>1.9</td><td>1.8</td><td>1.9</td></tr><tr><td>Leverage (X)</td><td>2.1</td><td>1.8</td><td>1.8</td><td>1.7</td></tr><tr><td>Gross cash invested (ex cash) (W)</td><td>14,052.4</td><td>16,249.7</td><td>18,484.0</td><td>20,243.1</td></tr><tr><td>Average capital employed (W)</td><td>6,647.1</td><td>7,343.5</td><td>8,683.2</td><td>9,633.2</td></tr><tr><td>BVPS (W)</td><td>243,532</td><td>294,895</td><td>329,644</td><td>376,880</td></tr></table>

Income Statement (W bn)

Growth & Margins (%)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>3.3</td><td>12.0</td><td>2.6</td><td>12.1</td></tr><tr><td>EBITDA growth</td><td>(8.6)</td><td>19.7</td><td>10.2</td><td>22.4</td></tr><tr><td>EPS growth</td><td>(24.0)</td><td>147.0</td><td>10.2</td><td>35.6</td></tr><tr><td>DPS growth</td><td>(10.0)</td><td>139.4</td><td>33.3</td><td>25.0</td></tr><tr><td>EBIT margin</td><td>3.0</td><td>4.7</td><td>5.1</td><td>6.1</td></tr><tr><td>EBITDA margin</td><td>8.3</td><td>8.9</td><td>9.5</td><td>10.4</td></tr><tr><td>Net income margin</td><td>1.6</td><td>3.4</td><td>3.7</td><td>4.5</td></tr></table>

![](images/e87bdabebd4bc36b247294aa0a2ae57dd75379f977e227c956ac1d88d2521fcc.jpg)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>21,896.6</td><td>24,515.6</td><td>25,145.8</td><td>28,178.8</td></tr><tr><td>Cost of goods sold</td><td>(20,147.0)</td><td>(21,952.2)</td><td>(22,401.9)</td><td>(24,815.7)</td></tr><tr><td>SG&amp;A</td><td>(507.2)</td><td>(838.9)</td><td>(850.2)</td><td>(972.0)</td></tr><tr><td>R&amp;D</td><td>(577.4)</td><td>(562.0)</td><td>(608.4)</td><td>(658.5)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>1,815.3</td><td>2,173.7</td><td>2,396.4</td><td>2,933.2</td></tr><tr><td>Depreciation &amp; amortization</td><td>(1,150.3)</td><td>(1,011.2)</td><td>(1,111.0)</td><td>(1,200.6)</td></tr><tr><td>EBIT</td><td>665.0</td><td>1,162.5</td><td>1,285.3</td><td>1,732.7</td></tr><tr><td>Net interest inc./(exp.)</td><td>(46.4)</td><td>(53.6)</td><td>(48.6)</td><td>(51.6)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>408.6</td><td>1,074.4</td><td>1,190.8</td><td>1,615.2</td></tr><tr><td>Provision for taxes</td><td>(67.4)</td><td>(231.5)</td><td>(262.0)</td><td>(355.3)</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>341.3</td><td>842.9</td><td>928.8</td><td>1,259.8</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>341.3</td><td>842.9</td><td>928.8</td><td>1,259.8</td></tr><tr><td>EPS (basic, pre-except) (W)</td><td>14,421</td><td>35,619</td><td>39,249</td><td>53,237</td></tr><tr><td>EPS (diluted, pre-except) (W)</td><td>14,421</td><td>35,619</td><td>39,249</td><td>53,237</td></tr><tr><td>EPS (basic, post-except) (W)</td><td>14,421</td><td>35,619</td><td>39,249</td><td>53,237</td></tr><tr><td>EPS (diluted, post-except) (W)</td><td>14,421</td><td>35,619</td><td>39,249</td><td>53,237</td></tr><tr><td>DPS (W)</td><td>1,880</td><td>4,500</td><td>6,000</td><td>7,500</td></tr><tr><td>Div. payout ratio (%)</td><td>13.0</td><td>12.6</td><td>15.3</td><td>14.1</td></tr></table>

Price Performance  
Source: FactSet. Price as of 27 Jul 2026 close.

Balance Sheet (W bn)

<table><tr><td colspan="5">Balance Sheet (W bn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>1,407.7</td><td>1,076.1</td><td>670.5</td><td>1,116.3</td></tr><tr><td>Accounts receivable</td><td>3,398.4</td><td>3,123.4</td><td>3,501.7</td><td>3,661.6</td></tr><tr><td>Inventory</td><td>1,788.8</td><td>2,519.3</td><td>3,096.9</td><td>3,193.6</td></tr><tr><td>Other current assets</td><td>183.5</td><td>614.8</td><td>665.4</td><td>720.3</td></tr><tr><td>Total current assets</td><td>6,778.4</td><td>7,333.6</td><td>7,934.6</td><td>8,691.8</td></tr><tr><td>Net PP&amp;E</td><td>4,108.2</td><td>3,786.1</td><td>4,224.6</td><td>4,575.6</td></tr><tr><td>Net intangibles</td><td>609.9</td><td>301.2</td><td>290.8</td><td>280.0</td></tr><tr><td>Total investments</td><td>124.1</td><td>127.7</td><td>127.7</td><td>127.7</td></tr><tr><td>Other long-term assets</td><td>310.3</td><td>1,263.2</td><td>1,367.3</td><td>1,480.0</td></tr><tr><td>Total assets</td><td>11,930.9</td><td>12,811.8</td><td>13,945.0</td><td>15,155.1</td></tr><tr><td>Accounts payable</td><td>2,642.1</td><td>2,645.3</td><td>2,956.1</td><td>3,048.4</td></tr><tr><td>Short-term debt</td><td>722.3</td><td>811.5</td><td>811.5</td><td>811.5</td></tr><tr><td>Short-term lease liabilities</td><td>7.2</td><td>7.9</td><td>7.3</td><td>6.5</td></tr><tr><td>Other current liabilities</td><td>1,135.6</td><td>903.5</td><td>904.0</td><td>904.9</td></tr><tr><td>Total current liabilities</td><td>4,507.2</td><td>4,368.2</td><td>4,679.0</td><td>4,771.3</td></tr><tr><td>Long-term debt</td><td>1,540.2</td><td>1,355.3</td><td>1,355.3</td><td>1,355.3</td></tr><tr><td>Long-term lease liabilities</td><td>15.2</td><td>14.2</td><td>13.4</td><td>12.5</td></tr><tr><td>Other long-term liabilities</td><td>105.2</td><td>95.5</td><td>96.4</td><td>97.2</td></tr><tr><td>Total long-term liabilities</td><td>1,660.6</td><td>1,465.1</td><td>1,465.1</td><td>1,465.1</td></tr><tr><td>Total liabilities</td><td>6,167.8</td><td>5,833.2</td><td>6,144.1</td><td>6,236.4</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>5,763.1</td><td>6,978.5</td><td>7,800.9</td><td>8,918.7</td></tr><tr><td>Minority interest</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total liabilities &amp; equity</td><td>11,930.9</td><td>12,811.8</td><td>13,945.0</td><td>15,155.1</td></tr><tr><td>Net debt, adjusted</td><td>854.7</td><td>1,090.7</td><td>1,496.3</td><td>1,050.5</td></tr></table>

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>341.3</td><td>842.9</td><td>928.8</td><td>1,259.8</td></tr><tr><td>D&amp;A add-back</td><td>1,150.3</td><td>1,011.2</td><td>1,111.0</td><td>1,200.6</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(427.0)</td><td>(452.4)</td><td>(645.0)</td><td>(164.3)</td></tr><tr><td>Other operating cash flow</td><td>266.8</td><td>(696.4)</td><td>(154.8)</td><td>(167.6)</td></tr><tr><td>Cash flow from operations</td><td>1,331.4</td><td>705.3</td><td>1,240.0</td><td>2,128.5</td></tr><tr><td>Capital expenditures</td><td>(611.0)</td><td>(1,024.3)</td><td>(1,500.0)</td><td>(1,500.0)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(185.4)</td><td>(56.2)</td><td>(39.1)</td><td>(40.7)</td></tr><tr><td>Cash flow from investing</td><td>(796.3)</td><td>(1,080.5)</td><td>(1,539.1)</td><td>(1,540.7)</td></tr><tr><td>Repayment of lease liabilities</td><td>(15.3)</td><td>(14.0)</td><td>(15.5)</td><td>(17.0)</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(49.5)</td><td>(44.5)</td><td>(106.5)</td><td>(142.0)</td></tr><tr><td>Inc/(dec) in debt</td><td>(389.6)</td><td>(95.6)</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>(2.4)</td><td>197.6</td><td>15.5</td><td>17.0</td></tr><tr><td>Cash flow from financing</td><td>(456.7)</td><td>43.6</td><td>(106.5)</td><td>(142.0)</td></tr><tr><td>Total cash flow</td><td>78.3</td><td>(331.6)</td><td>(405.6)</td><td>445.8</td></tr><tr><td>Free cash flow</td><td>705.1</td><td>(333.0)</td><td>(275.5)</td><td>611.6</td></tr></table>

Source: Company data, GS estimates.

LGI's package solution continued to see solid revenue growth on the back of rising demand for high-end substrates and favorable pricing trends. With operating margin improving to low-teens% level which was inline with our expectations, both revenue and profit for the business exceeded our expectations. While we expect the strength in high-value substrates to continue in the coming quarters, revenue growth for the overall business may see some limited upside in the near-term given the already high utilization rate for the business. As such, we also note that the company may see increasing fixed cost burden especially from FC-BGA as it plans to invest a significant amount of capex over the next few years. Our updated 3Q26E package solution revenue is W509bn (+2% qoq and +16% yoy), with 13% operating margin (vs. 7% OPM in 3Q25).

■ Lower 3Q26E OP to W247bn: We lower 3Q26E OP estimate to W247bn (from W306bn previously), where most of the delta comes from lower camera module revenue and margin estimates.

## Lower earnings estimates and TP to W860K; remain Neutral-rated

We lower our 2026E/2027E/2028E EPS estimates by 4%/8%/2% mainly reflecting lower camera module ASP and lower mobility solution revenue/margin estimates. As we refresh our target multiples (from 10.2x to 8.1x for Optics Solution, and from 15.1x to 16.0x for Package Solution) to reflect changes in peer valuation, our 2027E-2028E SOTP based 12m TP is lowered to W860,000 (from W1,000,000 prior). While we appreciate the increasing contribution from the substrate business, camera module continues to drive overall revenue/profit, for which we expect to see limited margin expansion. As such, our earnings estimates during our forecast period are below consensus, and we remain Neutral-rated on the stock. Key risks include higher-/lower-than-expected camera module market share of LGI in Apple.

Exhibit 1: LGI shares are currently trading at 1.9x 12m FWD P/B with 2026E/2027E ROE of 13%/13% LGI 12m FWD P/B vs. ROE  
![](images/5061f1291256084c66c619f39848734e637d8955ef36709724570db02b079a97.jpg)  
Source: Bloomberg, Company data, GS Global Investment Research

Exhibit 2: LGI currently trades at 16.2x 12m FWD P/E
LGI 12m FWD P/E  
![](images/8650d0b8d0103ad34f14a8c774c42ff5ecb1e644ce426938d72cb2d19395bddd.jpg)  
Source: Bloomberg, Company data, GS Global Investment Research

Exhibit 3: LGI earnings revisions

<table><tr><td rowspan="2">(W bn)</td><td colspan="4">Revised</td><td colspan="4">Previous</td><td colspan="4">%-change</td></tr><tr><td>2Q26</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>2Q26E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>2Q26E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Sa

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or

finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
