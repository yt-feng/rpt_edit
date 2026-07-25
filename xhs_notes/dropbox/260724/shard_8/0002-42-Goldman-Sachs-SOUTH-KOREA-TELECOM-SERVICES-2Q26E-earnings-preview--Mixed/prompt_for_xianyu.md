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
SOUTH KOREA TELECOM SERVICES

# 2Q26E earnings preview; Mixed earnings as AIDC optionality moves into focus

We expect mixed 2Q26E earnings across the Korean telcos, with KT's reported results impacted by a high property-development base, LGU delivering a relatively clean sequential recovery, and SKT posting a sharp YoY OP rebound, largely on the absence of data-breach-related costs. Underlying wireless trends should remain subdued across the sector: subscriber momentum has stabilized following the recent penalty-waiver periods, but the lingering impact of earlier subscriber losses, temporary plan downgrades and subscriber-acquisition cost amortization should limit meaningful earnings expansion. Meanwhile, enterprise and data-center operations should remain the principal incremental growth drivers, supported by KT Cloud's double-digit growth, LGU's $c.30\%$ AIDC growth and higher Pangyo DC utilization at SK Broadband. Beyond the quarter, we see infrastructure-led growth optionality becoming an increasingly important differentiator. We believe KT offers most favorable risk-reward, supported by its demand-backed and relatively capital-light plan to expand AIDC capacity to 1GW by 2031, subsea-cable expansion and continued shareholder returns. For LGU, improving earnings quality and its plan to expand AIDC capacity to 400MW by 2030 are balanced by valuation. For SKT, existing SK Broadband data-center operations provide tangible earnings support, but we believe the consortium-led 5GW-to-15GW roadmap remains too early to capitalize without greater visibility on customers, funding requirements and prospective returns. We raise our 12-month TPs for KT to W74k (previously W72k) and LGU to W17k (previously W16k), while maintaining our W58k TP for SKT. We remain Buy-rated on KT, Neutral-rated on LGU and Sell-rated on SKT.

Eric Cha
+82(2)3788-1799 | eric.cha@gs.com
GS (Asia) L.L.C., Seoul Branch

Vona Lee  
+82(2)3788-1201 | vona.lee@gs.com  
GS (Asia) L.L.C., Seoul Branch

KT (W74,000, Buy): In 2Q, we expect KT to report consolidated revenue of W6.8trn (-8% YoY and +1% QoQ) and OP of W558bn (-45% YoY and +16 QoQ), down YoY due to the high base of c.W380bn Gwangjin-gu property-development gain recognized in 2Q25. While the wireless subscribers returned to net additions following the penalty-waiver period, we think wireless service revenue should remain under pressure from subscriber losses at the beginning of the year, as well as the temporary plan downgrades associated with the free 100GB customer-appreciation package. On costs, marketing expenses should remain elevated YoY due to amortization of subscriber-acquisition costs incurred last year, although easing competition and better cost control should support a QoQ improvement. Among subsidiaries, KT Cloud revenue should grow at a double-digit rate on DBO, co-location and private-cloud demand, while KT

Estate should benefit from hotel operations and property-development contributions. However, KT Cloud margins may remain temporarily compressed due to still-low utilization rate of Gasan AIDC (despite capacity being fully contracted), while lease and depreciation expenses are already being recognized. In our view, the conclusion of the customer-appreciation package in July will support a more visible wireless and earnings recovery from 3Q. Beyond the quarter, the company's plan to expand AIDC capacity to 1GW by 2031 and subsea-cable capacity from 31Tbps to 90Tbps provides credible infrastructure-led growth optionality, supported by presales and a capital-light model. We maintain Buy, underpinned by the ongoing W250bn share buyback, shareholder-return visibility and improving medium-term infrastructure growth. We remain Buy-rated with a SOTP-based 12m TP of 74,000 (previously W72,000), with $40\%$ implied upside. For legacy businesses mainly consisting of telecom services, we apply a 11x P/E on NTM EPS, and roll forward our valuation to 3Q26-2Q27 (previously 2Q26-1Q27). For KT Cloud, we apply a 9.1x EV/EBITDA (domestic data center peer comp) and a $50\%$ holdco discount. For other key subsidiaries/affiliates, we also apply a $50\%$ holdco discount.

LGU (W17,000, Neutral): In 2Q, we expect LGU to report consolidated revenue of W3.9trn (+1% YoY and +2% QoQ) and OP W316bn (+4% YoY and +16% QoQ), generally in-line with Street. In 2Q, service revenue growth should remain at low-single digits (+2.4% YoY), with mobile growth moderating on a tougher base following subscriber inflows from SKT beginning in 2Q25. Enterprise should see accelerating growth on strong AIDC growth (c.30%+), supported by higher existing-center utilization and DBO contribution. On costs, marketing-expense growth should moderate to high-single digits YoY (+9.8% YoY) from +11.7% in 1Q, reflecting easing number-portability competition and improving handset margins, while restructuring-led labor-cost savings provide an additional offset. Beyond the quarter, we look forward to upcoming shareholder-return announcement, as well as the company's plan to expand AIDC capacity from 165MW currently to 400MW by 2030. We maintain our Neutral rating with a P/E-based 12m TP of W17,000 (previously W16,000) with a 15% implied upside, balancing improving earnings quality and AIDC optionality against valuation. We apply an unchanged P/E multiple of 9x to NTM EPS, and roll forward our valuation to 3Q26-2Q27 (previously 2Q26-1Q27).

SKT (W58,000, Sell): We expect SKT's consolidated revenue at W4.4trn (+1% YoY and flat QoQ) and OP at W545bn (+61% YoY and +1% QoQ), in-line with BBG consensus. The sharp YoY recovery largely reflects the absence of c.W200-250bn in USIM replacement and dealer-compensation costs booked following the data breach in 2Q25. Meanwhile, underlying wireless trends appear steady with continued subscriber recovery following KT's termination-fee waiver in Jan. On costs, we expect marketing expenses to stay relatively modest, rising only low-single digits YoY (+2% YoY). In our view, SKB should remain the cleaner incremental earnings driver, with a revenue up +3% YoY, supported by higher Pangyo DC utilization, contract-price renewals and continued broadband subscriber growth. We expect quarterly DPS of W830 and retain our FY26 DPS forecast of W3,540. In our view, the 2Q earnings rebound is predominantly a normalization from an

exceptionally weak base, while underlying telecom revenue growth remains limited. Existing SK Broadband data-center operations provide tangible earnings support, but the consortium-led 5GW-to-15GW AIDC roadmap remains too early to capitalize without greater visibility on customers, SKT's ownership and funding commitment, capex intensity and prospective returns. Hence, we maintain Sell with an unchanged P/E-based 12m TP of W58,000 and $42\%$ implied downside. We apply an unchanged target P/E multiple of 9x to our NTM EPS, and roll forward our valuation to 3Q26-2Q27 (previously 2Q26-1Q27).

Exhibit 1: KT 2Q26E earnings preview summary

<table><tr><td colspan="3"></td><td colspan="3">GS est</td><td colspan="2">BBG</td></tr><tr><td>(W bn)</td><td>2Q25</td><td>1Q26</td><td>2Q26E</td><td>% yoy</td><td>% qoq</td><td>2Q26E</td><td>% Diff</td></tr><tr><td>Total revenue</td><td>7,427</td><td>6,778</td><td>6,833</td><td>-8%</td><td>1%</td><td>6,828</td><td>0%</td></tr><tr><td>OPEX</td><td>6,413</td><td>6,296</td><td>6,275</td><td>-2%</td><td>0%</td><td>6,253</td><td>0%</td></tr><tr><td>Operating profit</td><td>1,015</td><td>483</td><td>558</td><td>-45%</td><td>16%</td><td>575</td><td>-3%</td></tr><tr><td>OP margin (%)</td><td>13.7%</td><td>7.1%</td><td>8.2%</td><td>-5.5%p</td><td>1.1%p</td><td>8.4%</td><td>-0.2%p</td></tr><tr><td>Net profit</td><td>733</td><td>388</td><td>391</td><td>-47%</td><td>1%</td><td>412</td><td>-5%</td></tr><tr><td>NP margin (%)</td><td>9.9%</td><td>5.7%</td><td>5.7%</td><td>-4.2%p</td><td>0.0%p</td><td>6.0%</td><td>-0.3%p</td></tr></table>

Source: Bloomberg, Company data, GS Global Investment Research

Exhibit 2: LGU 2Q26E earnings preview summary

<table><tr><td colspan="3"></td><td colspan="3">GS est</td><td colspan="2">BBG</td></tr><tr><td>(W bn)</td><td>2Q25</td><td>1Q26</td><td>2Q26E</td><td>% yoy</td><td>% qoq</td><td>2Q26E</td><td>% Diff</td></tr><tr><td>Revenue</td><td>3,844</td><td>3,804</td><td>3,880</td><td>1%</td><td>2%</td><td>3,900</td><td>-1%</td></tr><tr><td>OPEX</td><td>3,540</td><td>3,531</td><td>3,564</td><td>1%</td><td>1%</td><td>3,590</td><td>-1%</td></tr><tr><td>OP</td><td>305</td><td>272</td><td>316</td><td>4%</td><td>16%</td><td>310</td><td>2%</td></tr><tr><td>OP margin (%)</td><td>7.9%</td><td>7.2%</td><td>8.1%</td><td>0.2%p</td><td>1.0%p</td><td>7.9%</td><td>0.2%p</td></tr><tr><td>NP</td><td>217</td><td>176</td><td>214</td><td>-2%</td><td>21%</td><td>209</td><td>2%</td></tr><tr><td>NP margin (%)</td><td>5.6%</td><td>4.6%</td><td>5.5%</td><td>-0.1%p</td><td>0.9%p</td><td>5.4%</td><td>0.1%p</td></tr></table>

Source: Bloomberg, Company data, GS Global Investment Research

Exhibit 3: SKT 2Q26E earnings preview summary

<table><tr><td colspan="3"></td><td colspan="3">GS est</td><td colspan="2">BBG</td></tr><tr><td>(W bn)</td><td>2Q25</td><td>1Q26</td><td>2Q26E</td><td>% yoy</td><td>% qoq</td><td>2Q26E</td><td>% Diff</td></tr><tr><td>Revenue</td><td>4,339</td><td>4,392</td><td>4,399</td><td>1%</td><td>0%</td><td>4,399</td><td>0%</td></tr><tr><td>OPEX</td><td>4,001</td><td>3,855</td><td>3,854</td><td>-4%</td><td>0%</td><td>3,856</td><td>0%</td></tr><tr><td>OP</td><td>338</td><td>538</td><td>545</td><td>61%</td><td>1%</td><td>543</td><td>0%</td></tr><tr><td>OP margin (%)</td><td>7.8%</td><td>12.2%</td><td>12.4%</td><td>4.6%p</td><td>0.2%p</td><td>12.3%</td><td>0.0%p</td></tr><tr><td>NP</td><td>83</td><td>316</td><td>371</td><td>346%</td><td>17%</td><td>375</td><td>-1%</td></tr><tr><td>NP margin (%)</td><td>1.9%</td><td>7.2%</td><td>8.4%</td><td>6.5%p</td><td>1.2%p</td><td>8.5%</td><td>-0.1%p</td></tr></table>

Source: Bloomberg, Company data, GS Global Investment Research

Exhibit 4: KT earnings revision summary

<table><tr><td rowspan="2">(W bn)</td><td colspan="4">2026E</td><td colspan="4">2027E</td><td colspan="4">2028E</td></tr><tr><td>Old</td><td>New</td><td>Chg</td><td>% Chg</td><td>Old</td><td>New</td><td>Chg</td><td>% Chg</td><td>Old</td><td>New</td><td>Chg</td><td>% Chg</td></tr><tr><td>Revenue</td><td>27,876</td><td>27,646</td><td>-230</td><td>-0.8%</td><td>28,282</td><td>28,023</td><td>-260</td><td>-0.9%</td><td>28,562</td><td>28,335</td><td>-227</td><td>-0.8%</td></tr><tr><td>% yoy</td><td>-1%</td><td>-2%</td><td></td><td>-0.8%p</td><td>1%</td><td>1%</td><td></td><td>-0.1%p</td><td>1%</td><td>1%</td><td></td><td>0.1%p</td></tr><tr><td>KT</td><td>19,536</td><td>19,425</td><td>-111</td><td>-1%</td><td>19,786</td><td>19,668</td><td>-119</td><td>-1%</td><td>19,997</td><td>19,907</td><td>-90</td><td>0%</td></tr><tr><td>% yoy</td><td>1.1%</td><td>0.5%</td><td></td><td>-0.6%p</td><td>1.3%</td><td>1.2%</td><td></td><td>0.0%p</td><td>1.1%</td><td>1.2%</td><td></td><td>0.2%p</td></tr><tr><td>% of revenue</td><td>70%</td><td>70%</td><td></td><td>0.2%p</td><td>70%</td><td>70%</td><td></td><td>0.2%p</td><td>70%</td><td>70%</td><td></td><td>0.2%p</td></tr><tr><td>Subsidiaries</td><td>14,298</td><td>14,178</td><td>-120</td><td>-1%</td><td>14,592</td><td>14,451</td><td>-141</td><td>-1%</td><td>14,803</td><td>14,666</td><td>-137</td><td>-1%</td></tr><tr><td>% yoy</td><td>-6%</td><td>-7%</td><td></td><td>-0.8%p</td><td>2%</td><td>2%</td><td></td><td>-0.1%p</td><td>1%</td><td>1%</td><td></td><td>0.0%p</td></tr><tr><td>% of revenue</td><td>51%</td><td>51%</td><td></td><td>0.0%p</td><td>52%</td><td>52%</td><td></td><td>0.0%p</td><td>52%</td><td>52%</td><td></td><td>-0.1%p</td></tr><tr><td>Adjustments</td><td>-5,958</td><td>-5,958</td><td>0</td><td>na</td><td>-6,096</td><td>-6,096</td><td>0</td><td>na</td><td>-6,238</td><td>-6,238</td><td>0</td><td>na</td></tr><tr><td>% yoy</td><td>na</td><td>na</td><td></td><td>na</td><td>na</td><td>na</td><td></td><td>na</td><td>na</td><td>na</td><td></td><td>na</td></tr><tr><td>OPEX</td><td>25,717</td><td>25,582</td><td>-135</td><td>-0.5%</td><td>25,996</td><td>25,856</td><td>-140</td><td>-0.5%</td><td>26,344</td><td>26,212</td><td>-132</td><td>-0.5%</td></tr><tr><td>% yoy</td><td>0%</td><td>-1%</td><td></td><td>-0.5%p</td><td>1%</td><td>1%</td><td></td><td>0.0%p</td><td>1%</td><td>1%</td><td></td><td>0.0%p</td></tr><tr><td>Operating profit</td><td>2,159</td><td>2,063</td><td>-95</td><td>-4.4%</td><td>2,287</td><td>2,167</td><td>-120</td><td>-5.2%</td><td>2,218</td><td>2,123</td><td>-95</td><td>-4.3%</td></tr><tr><td>% yoy</td><td>-13%</td><td>-16%</td><td></td><td>-3.9%p</td><td>6%</td><td>5%</td><td></td><td>-0.9%p</td><td>-3%</td><td>-2%</td><td></td><td>1.0%p</td></tr><tr><td>OP margin (%)</td><td>7.7%</td><td>7.5%</td><td></td><td>-0.3%p</td><td>8.1%</td><td>7.7%</td><td></td><td>-0.4%p</td><td>7.8%</td><td>7.5%</td><td></td><td>-0.3%p</td></tr><tr><td>EBITDA</td><td>6,012</td><td>5,917</td><td>-95</td><td>-1.6%</td><td>6,130</td><td>6,011</td><td>-120</td><td>-2.0%</td><td>6,053</td><td>5,957</td><td>-95</td><td>-1.6%</td></tr><tr><td>% yoy</td><td>-5%</td><td>-7%</td><td></td><td>-1.5%p</td><td>2%</td><td>2%</td><td></td><td>-0.4%p</td><td>-1%</td><td>-1%</td><td></td><td>0.4%p</td></tr><tr><td>EBITDA margin (%)</td><td>21.6%</td><td>21.4%</td><td></td><td>-0.2%p</td><td>21.7%</td><td>21.4%</td><td></td><td>-0.2%p</td><td>21.2%</td><td>21.0%</td><td></td><td>-0.2%p</td></tr><tr><td>Net profit</td><td>1,348</td><td>1,315</td><td>-32</td><td>-2.4%</td><td>1,439</td><td>1,425</td><td>-14</td><td>-1.0%</td><td>1,390</td><td>1,393</td><td>3</td><td>0.2%</td></tr><tr><td>% yoy</td><td>-21%</td><td>-23%</td><td></td><td>-1.9%p</td><td>7%</td><td>8%</td><td></td><td>1.6%p</td><td>-3%</td><td>-2%</td><td></td><td>1.2%p</td></tr><tr><td>NP margin (%)</td><td>4.8%</td><td>4.8%</td><td></td><td>-0.1%p</td><td>5.1%</td><td>5.1%</td><td></td><td>0.0%p</td><td>4.9%</td><td>4.9%</td><td></td><td>0.1%p</td></tr></table>

Source: GS Global Investment Research

Exhibit 5: LGU earnings revision summary

<table><tr><td rowspan="2">(W bn)</td><td colspan="4">2026E</td><td colspan="4">2027E</td><td colspan="4">2028</td></tr><tr><td>Old</td><td>New</td><td>Chg</td><td>% Chg</td><td>Old</td><td>New</td><td>Chg</td><td>% Chg</td><td>Old</td><td>New</td><td>Chg</td><td>% Chg</td></tr><tr><td>Revenue</td><td>15,690</td><td>15,698</td><td>8</td><td>0.1%</td><td>15,877</td><td>15,886</td><td>9</td><td>0.1%</td><td>15,971</td><td>15,981</td><td>10</td><td>0.1%</td></tr><tr><td>% yoy</td><td>2%</td><td>2%</td><td></td><td>0.1%p</td><td>1%</td><td>1%</td><td></td><td>0.0%p</td><td>1%</td><td>1%</td><td></td><td>0.0%p</td></tr><tr><td>Service revenue</td><td>12,494</td><td>12,503</td><td>8</td><td>0.1%</td><td>12,611</td><td>12,621</td><td>9</td><td>0.1%</td><td>12,675</td><td>12,685</td><td>10</td><td>0.1%</td></tr><tr><td>% yoy</td><td>2%</td><td>2%</td><td></td><td>0.1%p</td><td>1%</td><td>1%</td><td></td><td>0.0%p</td><td>0%</td><td>1%</td><td></td><td>0.0%p</td></tr><tr><td>% of revenue</td><td>80%</td><td>80%</td><td></td><td>0.0%p</td><td>79%</td><td>79%</td><td></td><td>0.0%p</td><td>79%</td><td>79%</td><td></td><td>0.0%p</td></tr><tr><td>Wireless revenue</td><td>6,722</td><td>6,722</td><td>0</td><td>0%</td><td>6,723</td><td>6,723</td><td>0</td><td>0%</td><td>6,662</td><td>6,662</td><td>0</td><td>0%</td></tr><tr><td>% yoy</td><td>1%</td><td>1%</td><td></td><td>0.0%p</td><td>0%</td><td>0%</td><td></td><td>0.0%p</td><td>-1%</td><td>-1%</td><td></td><td>0.0%p</td></tr><tr><td>Fixed-line revenue</td><td>4,907</td><td>4,915</td><td>8</td><td>0.2%</td><td>5,022</td><td>5,031</td><td>9</td><td>0.2%</td><td>5,146</td><td>5,156</td><td>10</td><td>0.2%</td></tr><tr><td>% yoy</td

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
