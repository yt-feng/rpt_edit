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
June 30, 2026 09:51 AM GMT

Electronic Components | Japan

# May HDD/SSD Data: DC Volumes Remain High

## Key Takeaways

\- DC storage likely to stay segmented between SSDs, HDDs, and tape drives.

TSR forecasts 2026 DC-use enterprise SSD shipment capacity at 509.33EB, up 94.0% YoY.

TSR forecast 2026 DC-use NL HDD shipment capacity at 1,841EB, up $30.1\%$ YoY.

No change to view for continued growth in total shipment capacity of both NL HDDs and enterprise SSDs for data center use: We continue to expect sustained growth in total shipment capacity for both NL HDDs and enterprise SSDs, driven by ongoing high production levels and rising capacity per unit. TSR slightly lowered its 2026 HDD shipment capacity forecast to 2,055.5EB (+26.3% YoY) from 2,058.2EB (+26.4%) last month, but still expects continued growth from 1,627.9EB in 2025 (+29.5%). Meanwhile, TSR raised its 2026 total SSD shipment capacity forecast to 759.36EB (+52.5% YoY) from 675.30EB (+35.6%) last month, compared with 498.0EB in 2025 (+38.0%). With higher-capacity products accounting for an increasing share of shipments for both NL HDDs and enterprise SSDs, we expect shipment capacity growth to continue outpacing unit shipment growth.

May DC NL HDD output +14.8% YoY, +4.0% MoM: May NL HDD production was 7.07mn units (6.16mn a year ago, 6.80mn a month ago). NL output declined from 81.45mn units in 2021 (+18.0% YoY) to 71.30mn in 2022 (-12.5%) and 44.51mn in 2023 (-37.6%), before recovering to 63.12mn in 2024 (+41.8%) and 74.77mn in 2025 (+18.5%). TSR forecasts 84.37mn units for 2026 (+12.8% YoY), up from last month's forecast of 83.97mn (+12.3% YoY). It estimates Jan–Mar production of 20.77mn units (+19.9% YoY, +5.0% QoQ) and Apr–Jun production of 20.97mn units (+14.2% YoY, +1.0% QoQ).

May DC-use enterprise SSD shipments (capacity) +138.8% YoY, +9.7% MoM: May enterprise SSD shipment capacity totaled 41.35EB (17.32EB a year ago, 37.70EB a month ago). Full-year shipment capacity was 77.47EB in 2021, 109.83EB (+41.8% YoY) in 2022, 102.66EB (-6.5%) in 2023, 165.95EB (+61.6%) in 2024, and 262.5EB (+58.2% YoY) in 2025. TSR forecasts 2026 enterprise SSD shipment capacity at 509.33EB (+94.0% YoY), up from last month's forecast of 476.1EB (+62.0% YoY).

MS MUFG SECURITIES CO., LTD.+

Shoji Sato  
Equity Analyst  
Shoji.Sato@morganstanleymufg.com

Sota Harashima  
Equity Analyst  
Sota.Harashima@morganstanleymufg.com

+81 3 6836-8404

+81 3 6836-8897

![](images/4021bd426adf012bae60496938a7b74a664398239af6a00a150c4215179b7552.jpg)

ELECTRONIC COMPONENTS

Japan Industry View In-Line

Exhibit 1: HDD Production Volume YoY and Share Prices of TDK & Nidec

![](images/dcbfa8cae2dc2300d1181ed452b2abb34653302ce8df98ef398e5c4a87ccb2d1.jpg)  
Source: TSR, MS

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

\+ = Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

May HDD output +6.9% YoY, +0.7% MoM: May HDD production was 11.26mn units (10.54mn a year ago, 11.18mn a month ago). HDD output declined from 261.70mn units in 2021 (-0.1% YoY) to 168.70mn in 2022 (-35.5%), then to 120.51mn in 2023 (-28.6%), but rose to 124.77mn in 2024 (+3.5%) and to 129.54mn in 2025 (+3.8%). TSR forecasts 134.85mn units for 2026 (+4.1% YoY), slightly below last month's forecast of 135.04mn (+4.2% YoY). It estimates Jan–Mar production at 33.89mn units (+12.9% YoY, +0.1% QoQ) and Apr–Jun production at 33.76mn units (+6.6% YoY, -0.4% QoQ), versus last month's forecast of 33.81mn (+6.7% YoY, -0.2% QoQ). Our forecasts shown in Exhibit 4 onward reflect shipments and therefore differ from TSR's production estimates.

May SSD shipments -0.5% YoY, +1.5% MoM: May SSD shipments were 29.64mn units (29.80mn a year ago, 29.23mn a month ago). SSD shipments declined from 383.02mn units in 2021 (+21.4% YoY) to 348.30mn in 2022 (-9.1%), then to 319.80mn in 2023 (-8.2%), but recovered to 348.20mn in 2024 (+8.0%) and to 375.01mn in 2025 (+7.7%). TSR forecasts shipments of 380.46mn units for 2026 (+1.5% YoY), compared with last month's forecast of 363.90mn (-3.0% YoY). It estimates Jan-Mar shipments at 89.20mn units (+2.6% YoY, -11.4% QoQ) and Apr-Jun shipments at 89.77mn units (flat YoY, +0.6% QoQ), versus last month's forecast of 90.38mn (+0.6% YoY, +1.3% QoQ).

May DC-use enterprise SSD shipments +45.8% YoY, +2.6% MoM: May enterprise SSD shipments were 5.83mn units (4.00mn a year ago, 5.68mn a month ago). Enterprise SSD shipments rose from 36.10mn units in 2021 (+6.8% YoY) to 47.30mn in 2022 (+31.0%), then fell to 40.10mn in 2023 (-15.2%), before recovering to 50.00mn in 2024 (+24.7%) and to 56.51mn in 2025 (+13.1%). TSR forecasts 72.31mn units for 2026 (+28.0% YoY), up from last month's forecast of 71.53mn (+26.6% YoY). It estimates Jan–Mar shipments at 17.20mn units (+41.0% YoY, +2.9% QoQ) and Apr–Jun shipments at 17.66mn units (+41.3% YoY, +2.7% QoQ), compared with last month's forecast of 17.63mn units.

Exhibit 2: HDD Production Volume by Company and Size

<table><tr><td>(k units)</td><td></td><td>25/5</td><td>25/6</td><td>25/7</td><td>25/8</td><td>25/9</td><td>25/10</td><td>25/11</td><td>25/12</td><td>26/1</td><td>26/2</td><td>26/3</td><td>26/4</td><td>26/5</td><td>YoY</td><td>MoM</td></tr><tr><td rowspan="5">Seagate</td><td>Enterprise</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>100</td><td>160</td><td>110</td><td>110</td><td>160</td><td>140</td><td>130</td><td>-13.3%</td><td>-7.1%</td></tr><tr><td>NL</td><td>2,500</td><td>2,600</td><td>2,600</td><td>2,650</td><td>2,650</td><td>2,700</td><td>2,800</td><td>2,900</td><td>2,850</td><td>2,870</td><td>2,700</td><td>2,800</td><td>2,850</td><td>14.0%</td><td>1.8%</td></tr><tr><td>3.5&quot;ATA</td><td>1,050</td><td>900</td><td>1,000</td><td>1,000</td><td>1,000</td><td>1,000</td><td>900</td><td>1,100</td><td>1,000</td><td>950</td><td>900</td><td>950</td><td>950</td><td>-9.5%</td><td>0.0%</td></tr><tr><td>2.5&quot;Mobile</td><td>600</td><td>700</td><td>700</td><td>650</td><td>650</td><td>650</td><td>650</td><td>650</td><td>600</td><td>550</td><td>600</td><td>550</td><td>500</td><td>-16.7%</td><td>-9.1%</td></tr><tr><td>Total</td><td>4,300</td><td>4,350</td><td>4,450</td><td>4,450</td><td>4,450</td><td>4,500</td><td>4,450</td><td>4,810</td><td>4,560</td><td>4,480</td><td>4,360</td><td>4,440</td><td>4,430</td><td>3.0%</td><td>-0.2%</td></tr><tr><td rowspan="5">WDC</td><td>Enterprise</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>NL</td><td>2,900</td><td>2,900</td><td>2,900</td><td>2,950</td><td>2,950</td><td>2,960</td><td>3,160</td><td>3,080</td><td>3,150</td><td>3,200</td><td>3,100</td><td>3,200</td><td>3,350</td><td>15.5%</td><td>4.7%</td></tr><tr><td>3.5&quot;ATA</td><td>1,000</td><td>1,100</td><td>1,200</td><td>1,150</td><td>1,150</td><td>1,100</td><td>1,050</td><td>1,100</td><td>1,150</td><td>1,100</td><td>1,100</td><td>1,050</td><td>1,000</td><td>0.0%</td><td>-4.8%</td></tr><tr><td>2.5&quot;Mobile</td><td>600</td><td>650</td><td>650</td><td>700</td><td>650</td><td>600</td><td>600</td><td>600</td><td>580</td><td>580</td><td>650</td><td>600</td><td>550</td><td>-8.3%</td><td>-8.3%</td></tr><tr><td>Total</td><td>4,500</td><td>4,650</td><td>4,750</td><td>4,800</td><td>4,750</td><td>4,660</td><td>4,810</td><td>4,780</td><td>4,880</td><td>4,880</td><td>4,850</td><td>4,850</td><td>4,900</td><td>8.9%</td><td>1.0%</td></tr><tr><td rowspan="5">Toshiba</td><td>Enterprise</td><td>140</td><td>130</td><td>130</td><td>110</td><td>100</td><td>140</td><td>160</td><td>140</td><td>120</td><td>90</td><td>100</td><td>60</td><td>70</td><td>-50.0%</td><td>16.7%</td></tr><tr><td>NL</td><td>760</td><td>760</td><td>720</td><td>770</td><td>770</td><td>920</td><td>870</td><td>730</td><td>880</td><td>980</td><td>1,040</td><td>800</td><td>870</td><td>14.5%</td><td>8.7%</td></tr><tr><td>3.5&quot;ATA</td><td>220</td><td>300</td><td>240</td><td>210</td><td>350</td><td>240</td><td>415</td><td>330</td><td>320</td><td>270</td><td>500</td><td>330</td><td>310</td><td>40.9%</td><td>-6.1%</td></tr><tr><td>2.5&quot;Mobile</td><td>620</td><td>630</td><td>660</td><td>660</td><td>640</td><td>680</td><td>660</td><td>540</td><td>500</td><td>480</td><td>600</td><td>700</td><td>680</td><td>9.7%</td><td>-2.9%</td></tr><tr><td>Total</td><td>1,740</td><td>1,820</td><td>1,750</td><td>1,750</td><td>1,860</td><td>1,980</td><td>2,105</td><td>1,740</td><td>1,820</td><td>1,820</td><td>2,240</td><td>1,890</td><td>1,930</td><td>10.9%</td><td>2.1%</td></tr><tr><td rowspan="7">Total</td><td>Enterprise</td><td>290</td><td>280</td><td>280</td><td>260</td><td>250</td><td>290</td><td>260</td><td>300</td><td>230</td><td>200</td><td>260</td><td>200</td><td>200</td><td>-31.0%</td><td>0.0%</td></tr><tr><td>NL</td><td>6,160</td><td>6,260</td><td>6,220</td><td>6,370</td><td>6,370</td><td>6,580</td><td>6,830</td><td>6,710</td><td>6,880</td><td>7,050</td><td>6,840</td><td>6,800</td><td>7,070</td><td>14.8%</td><td>4.0%</td></tr><tr><td>(Air)</td><td>1,310</td><td>1,190</td><td>1,170</td><td>1,245</td><td>1,295</td><td>1,270</td><td>1,280</td><td>1,280</td><td>1,220</td><td>1,210</td><td>1,120</td><td>1,070</td><td>1,130</td><td>-13.7%</td><td>5.6%</td></tr><tr><td>(He)</td><td>4,850</td><td>5,070</td><td>5,050</td><td>5,125</td><td>5,075</td><td>5,310</td><td>5,550</td><td>5,430</td><td>5,660</td><td>5,840</td><td>5,720</td><td>5,730</td><td>5,940</td><td>22.5%</td><td>3.7%</td></tr><tr><td>3.5&quot;ATA</td><td>2,270</td><td>2,300</td><td>2,440</td><td>2,360</td><td>2,500</td><td>2,340</td><td>2,365</td><td>2,530</td><td>2,470</td><td>2,320</td><td>2,500</td><td>2,330</td><td>2,260</td><td>-0.4%</td><td>-3.0%</td></tr><tr><td>2.5&quot;Mobile</td><td>1,820</td><td>1,980</td><td>2,010</td><td>2,010</td><td>1,940</td><td>1,930</td><td>1,910</td><td>1,790</td><td>1,680</td><td>1,610</td><td>1,850</td><td>1,850</td><td>1,730</td><td>-4.9%</td><td>-6.5%</td></tr><tr><td>Total</td><td>10,540</td><td>10,820</td><td>10,950</td><td>11,000</td><td>11,060</td><td>11,140</td><td>11,365</td><td>11,330</td><td>11,260</td><td>11,180</td><td>11,450</td><td>11,180</td><td>11,260</td><td>6.8%</td><td>0.7%</td></tr><tr><td rowspan="7">YoY % Change</td><td>Enterprise</td><td>-9.4%</td><td>-12.5%</td><td>-15.2%</td><td>-27.8%</td><td>-21.9%</td><td>-17.1%</td><td>-27.8%</td><td>-9.1%</td><td>-23.3%</td><td>-42.9%</td><td>-13.3%</td><td>-28.6%</td><td>-31.0%</td><td></td><td></td></tr><tr><td>NL</td><td>17.3%</td><td>19.7%</td><td>13.7%</td><td>11.8%</td><td>11.2%</td><td>15.4%</td><td>20.2%</td><td>14.5%</td><td>22.0%</td><td>20.5%</td><td>17.3%</td><td>14.3%</td><td>14.8%</td><td></td><td></td></tr><tr><td>(Air)</td><td>-5.8%</td><td>-11.2%</td><td>-24.5%</td><td>-14.1%</td><td>-15.6%</td><td>-17.8%</td><td>-16.1%</td><td>-15.0%</td><td>-19.2%</td><td>-18.2%</td><td>-11.1%</td><td>-21.3%</td><td>-13.7%</td><td></td><td></td></tr><tr><td>(He)</td><td>25.6%</td><td>30.3%</td><td>28.8%</td><td>20.6%</td><td>21.0%</td><td>27.8%</td><td>33.6%</td><td>24.7%</td><td>37.0%</td><td>33.6%</td><td>25.2%</td><td>24.8%</td><td>22.5%</td><td></td><td></td></tr><tr><td>3.5&quot;ATA</td><td>-17.5%</td><td>-14.2%</td><td>-11.9%</td><td>-9.9%</td><td>-9.1%</td><td>-4.9%</td><td>-8.0%</td><td>15.5%</td><td>5.1%</td><td>0.9%</td><td>1.2%</td><td>2.2%</td><td>-0.4%</td><td></td><td></td></tr><tr><td>2.5&quot;</td><td>-15.7%</td><td>-6.6%</td><td>-7.8%</td><td>-6.5%</td><td>-4.0%</td><td>-8.1%</td><td>-8.2%</td><td>-2.2%</td><td>-10.2%</td><td>-13.4%</td><td>-2.1%</td><td>2.2%</td><td>-4.9%</td><td></td><td></td></tr><tr><td>Total</td><td>0.6%</td><td>4.5%</td><td>2.8%</td><td>1.6%</td><td>2.2%</td><td>5.0%</td><td>6.3%</td><td>11.0%</td><td>10.8%</td><td>7.9%</td><td>9.2%</td><td>8.3%</td><td>6.8%</td><td></td><td></td></tr><tr><td rowspan="7">MoM % Change</td><td>Enterprise</td><td>3.6%</td><td>-3.4%</td><td>0.0%</td><td>-7.1%</td><td>-3.8%</td><td>16.0%</td><td>-10.3%</td><td>15.4%</td><td>-23.3%</td><td>-13.0%</td><td>30.0%</td><td>-23.1%</td><td>0.0%</td><td></td><td></td></tr><tr><td>NL</td><td>3.5%</td><td>1.6%</td><td>-0.6%</td><td>2.4%</td><td>0.0%</td><td>3.3%</td><td>3.8%</td><td>-1.8%</td><td>2.5%</td><td>2.5%</td><td>-3.0%</td><td>-0.6%</td><td>4.0%</td><td></td><td></td></tr><tr><td>(Air)</td><td>-3.7%</td><td>-9.2%</td><td>-1.7%</td><td>6.4%</td><td>4.0%</td><td>-1.9%</td><td>0.8%</td><td>0.0%</td><td>-4.7%</td><td>-0.8%</td><td>-7.4%</td><td>-4.5%</td><td>5.6%</td><td></td><td></td></tr><tr><td>(He)</td><td>5.7%</td><td>4.5%</td><td>-0.4%</td><td>1.5%</td><td>-1.0%</td><td>4.6%</td><td>4.5%</td><td>-2.2%</td><td>4.2%</td><td>3.2%</td><td>-2.1%</td><td>0.2%</td><td>3.7%</td><td></td><td></td></tr><tr><td>3.5&quot;ATA</td><td>-0.4%</td><td>1.3%</td><td>6.1%</td><td>-3.3%</td><td>5.9%</td><td>-6.4%</td><td>1.1%</td><td>7.0%</td><td>-2.4%</td><td>-6.1%</td><td>7.8%</td><td>-6.8%</td><td>-3.0%</td><td></td><td></td></tr><tr><td>2.5&quot;</td><td>0.6%</td><td>8.8%</td><td>1.5%</td><td>0.0%</td><td>-3.5%</td><td>-0.5%</td><td>-1.0%</td><td>-6.3%</td><td>-6.1%</td><td>-4.2%</td><td>14.9%</td><td>0.0%</td><td>-6.5%</td><td></td><td></td></tr><tr><td>Total</td><td>2.1%</td><td>2.7%</td><td>1.2%</td><td>0.5%</td><td>0.5%</td><td>0.7%</td><td>2.0%</td><td>-0.3%</td><td>-0.6%</td><td>-0.7%</td><td>2.4%</td><td>-2.4%</td><td>0.7%</td><td></td><td></td></tr></table>

Source: TSR, MS

Exhibit 3: SSD Shipments/Capacity by Application

<table><tr><td>(k units)</td><td></td><td>25/5</td><td>25/6</td><td>25/7</td><td>25/8</td><td>25/9</td><td>25/10</td><td>25/11</td><td>25/12</td><td>26/1</td><td>26/2</td><td>26/3</td><td>26/4</td><td>26/5</td><td>YoY</td><td>MoM</td></tr><tr><td rowspan="6">SSD shipment</td><td>Enterprise</td><td>4,000</td><td>4,500</td><td>4,870</td><td>5,010</td><td>5,220</td><td>5,500</td><td>5,610</td><td>5,600</td><td>5,630</td><td>5,670</td><td>5,900</td><td>5,680</td><td>5,830</td><td>45.8%</td><td>2.6%</td></tr><tr><td>PC</td><td>18,500</td><td>19,500</td><td>19,000</td><td>20,000</td><td>20,500</td><td>21,000</td><td>21,500</td><td>19,000</td><td>18,000</td><td>17,000</td><td>17,500</td><td>17,430</td><td>17,500</td><td>-5.4%</td><td>0.4%</td></tr><tr><td>Add-on</td><td>4,100</td><td>4,200</td><td>4,200</td><td>4,300</td><td>4,500</td><td>4,500</td><td>4,600</td><td>4,400</td><td>4,000</td><td>3,700</td><td>3,500</td><td>3,560</td><td>3,630</td><td>-11.5%</td><td>2.0%</td></tr><tr><td>Game</td><td>2,400</td><td>2,600</td><td>2,000</td><td>2,500</td><td>3,000</td><td>2,500</td><td>2,000</td><td>2,000</td><td>1,800</td><td>1,800</td><td>1,800</td><td>1,600</td><td>1,700</td><td>-29.2%</td><td>6.3%</td></tr><tr><td>Others</td><td>800</td><td>900</td><td>800</td><td>800</td><td>900</td><td>800</td><td>800</td><td>900</td><td>950</td><td>980</td><td>970</td><td>960</td><td>980</td><td>22.5%</td><td>2.1%</td></tr><tr><td>Total</td><td>29,800</td><td>31,700</td><td>30,870</td><td>32,610</td><td>34,120</td><td>34,300</td><td>34,510</td><td>31,900</td><td>30,380</td><td>29,150</td><td>29,670</td><td>29,230</td><td>29,640</td><td>-0.5%</td><td>1.4%</td></tr><tr><td rowspan="6">YoY % Change</td><td>Enterprise</td><td>-4.8%</td><td>-6.3%</td><td>13.3%</td><td>11.3%</

[中间内容因长度限制已省略]

or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Electronic Components

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/30/2026)</td></tr><tr><td colspan="3">Shoji Sato</td></tr><tr><td>ALPS ALPINE (6770.T)</td><td>O (03/17/2026)</td><td>¥2,045</td></tr><tr><td>Hamamatsu Photonics (6965.T)</td><td>E (06/17/2026)</td><td>¥2,671</td></tr><tr><td>Ibiden (4062.T)</td><td>U (02/04/2026)</td><td>¥23,815</td></tr><tr><td>Kyocera (6971.T)</td><td>E (06/25/2020)</td><td>¥3,561</td></tr><tr><td>Mabuchi Motor (6592.T)</td><td>E (11/03/2022)</td><td>¥1,570</td></tr><tr><td>Minebea Mitsumi (6479.T)</td><td>E (10/23/2025)</td><td>¥4,756</td></tr><tr><td>Murata Manufacturing (6981.T)</td><td>O (11/26/2025)</td><td>¥11,395</td></tr><tr><td>Nidec (6594.T)</td><td>NR (09/05/2025)</td><td>¥2,645</td></tr><tr><td>Niterra (5334.T)</td><td>O (01/17/2024)</td><td>¥10,705</td></tr><tr><td>Taiyo Yuden (6976.T)</td><td>U (06/17/2026)</td><td>¥20,150</td></tr><tr><td>TDK (6762.T)</td><td>O (08/02/2022)</td><td>¥3,570</td></tr><tr><td colspan="3">Sota Harashima</td></tr><tr><td>CMK (6958.T)</td><td>E (02/28/2025)</td><td>¥653</td></tr><tr><td>Daishinku (6962.T)</td><td>U (06/17/2026)</td><td>¥880</td></tr><tr><td>Hirose Electric (6806.T)</td><td>O (07/10/2024)</td><td>¥28,835</td></tr><tr><td>IRISO Electronics (6908.T)</td><td>E (08/02/2022)</td><td>¥2,914</td></tr><tr><td>Japan Aviation Electronics Industry (6807.T)</td><td>E (01/17/2024)</td><td>¥2,311</td></tr><tr><td>KOA (6999.T)</td><td>E (06/17/2026)</td><td>¥2,898</td></tr><tr><td>Meiko Electronics (6787.T)</td><td>E (04/03/2026)</td><td>¥31,000</td></tr><tr><td>Nichicon (6996.T)</td><td>E (11/10/2021)</td><td>¥4,150</td></tr><tr><td>Nihon Dempa Kogyo (6779.T)</td><td>E (03/07/2024)</td><td>¥3,425</td></tr><tr><td>Nippon Chemi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥5,490</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS MUFG
"""
