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
# JCET (600584.SS): New advanced packaging capacity announced; 2Q26 NI guidance beat

JCET's 2Q26 net income mid-point guidance was at Rmb570m (+113% YoY, +96% QoQ) (link), which management attributes to (1) strong AI infrastructure spending driving JCET's revenue growth and utilization rate, (2) product mix upgrade towards high-end OSAT service, driving the profitability, and (3) disciplined cost control. JCET's GM improved from 12.6% in 1Q25 to 14.5% in 1Q26. We expect the company's net income to grow at +34% CAGR in 2026-28E, driven by AI infrastructure upcycle, product mix upgrade, and the company's capacity expansion to capture the rising demand.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Yifan Hu  
+852-2978-0996 | yifan.hu@gs.com  
GS (Asia) L.L.C.

New capacity for advanced packaging: JCET announced its new capacity for advanced packaging in Jun 2026 (link), with a total investment at Rmb7.8bn, aiming to complete the phase 1 investment (plant construction, equipment investment) in 2H28E. We expect the capacity expansion plan to further drive JCET shipments growth and product mix upgrade in the long run, enabling it to capture the rising advanced packaging end demand in the local market, such as AI computing chips, high-end consumer electronics, automotive electronics, etc.

Earnings revision: We factor in JCET's 2Q26 net income guidance and raise our 2026E net income by $5\%$ , mainly on higher revenues and GM. We raise our 2026E revenue to reflect JCET benefiting from the rising AI related end demand. Our 2026E net income is revised up to reflect the company's product mix upgrade towards high-end OSAT service and utilization rate improvement.

Exhibit 1: Earnings revision

<table><tr><td rowspan="2">(Rmb mn)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td></tr><tr><td>Revenue</td><td>46,802</td><td>46,398</td><td>1%</td><td>53,869</td><td>53,869</td><td>0%</td><td>61,773</td><td>61,773</td><td>0%</td></tr><tr><td>Gross profit</td><td>6,878</td><td>6,769</td><td>2%</td><td>7,873</td><td>7,873</td><td>0%</td><td>9,599</td><td>9,599</td><td>0%</td></tr><tr><td>Operating income</td><td>2,834</td><td>2,746</td><td>3%</td><td>3,552</td><td>3,552</td><td>0%</td><td>4,892</td><td>4,892</td><td>0%</td></tr><tr><td>Net income</td><td>2,596</td><td>2,464</td><td>5%</td><td>3,349</td><td>3,349</td><td>0%</td><td>4,648</td><td>4,646</td><td>0%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>Gross margin</td><td>14.7%</td><td>14.6%</td><td>0.1ppts</td><td>14.6%</td><td>14.6%</td><td>0ppts</td><td>15.5%</td><td>15.5%</td><td>0ppts</td></tr><tr><td>Operating margin</td><td>6.1%</td><td>5.9%</td><td>0.1ppts</td><td>6.6%</td><td>6.6%</td><td>0ppts</td><td>7.9%</td><td>7.9%</td><td>0ppts</td></tr><tr><td>Net margin</td><td>5.5%</td><td>5.3%</td><td>0.2ppts</td><td>6.2%</td><td>6.2%</td><td>0ppts</td><td>7.5%</td><td>7.5%</td><td>0ppts</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We continue to derive our 12M TP based on 2030E discounted P/E to capture JCET's long-term growth opportunities, and our 12-month target price is unchanged at Rmb125. Our target multiple is based on the correlation between peers' P/E vs. the sum of forward year NI growth and OPM, which is 46x 2030E discounted P/E target multiple, based on the company's NI YoY at $18\%$ and OPM at $10\%$ in 2031E. We apply the 46x target P/E and discount it back to 2027E with a COE of 11%. Our new TP implied 2027E P/E at 67x is in line with the company's recent forward trading P/E range at \~60x. Maintain Neutral.

Exhibit 2: Target multiple is derived from the correlation between peers P/E and the sum of forward year earnings and OPM

<table><tr><td></td><td>2030E P/E</td><td>2031E OPM</td><td>2031E NI YoY</td><td>Ratio</td></tr><tr><td>JCET</td><td>46</td><td>10%</td><td>18%</td><td>1.6</td></tr><tr><td></td><td>2027E P/E</td><td>2028E OPM</td><td>2028E NI YoY</td><td>Ratio</td></tr><tr><td>Huatian</td><td>68</td><td>5%</td><td>23%</td><td>2.5</td></tr><tr><td>TSMC</td><td>20</td><td>58%</td><td>35%</td><td>0.2</td></tr><tr><td>Forehope</td><td>92</td><td>8%</td><td>38%</td><td>2.0</td></tr><tr><td>Amkor</td><td>35</td><td>10%</td><td>6%</td><td>2.3</td></tr><tr><td>ASE</td><td>29</td><td>26%</td><td>29%</td><td>0.5</td></tr><tr><td>Tongfu</td><td>58</td><td>7%</td><td>21%</td><td>2.1</td></tr><tr><td>Avg.</td><td></td><td></td><td></td><td>1.6</td></tr></table>

Source: Company data, GS Global Investment Research, Refinitiv Eikon

Exhibit 3: JCET discounted P/E

<table><tr><td>Rmb mn</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td></tr><tr><td>Revenue</td><td>29,661</td><td>35,962</td><td>38,871</td><td>46,802</td><td>53,869</td><td>61,773</td><td>69,700</td><td>75,489</td><td>81,760</td></tr><tr><td>Rev YoY %</td><td>-12%</td><td>21%</td><td>8%</td><td>20%</td><td>15%</td><td>15%</td><td>13%</td><td>8%</td><td>8%</td></tr><tr><td>Gross margin</td><td>13.7%</td><td>13.1%</td><td>14.1%</td><td>14.7%</td><td>14.6%</td><td>15.5%</td><td>16.1%</td><td>16.6%</td><td>17.0%</td></tr><tr><td>Gross profit</td><td>4,049</td><td>4,696</td><td>5,499</td><td>6,878</td><td>7,873</td><td>9,599</td><td>11,235</td><td>12,511</td><td>13,899</td></tr><tr><td>Opex</td><td>2,503</td><td>2,975</td><td>3,593</td><td>4,044</td><td>4,321</td><td>4,707</td><td>5,171</td><td>5,375</td><td>5,396</td></tr><tr><td>Opex ratio</td><td>8%</td><td>8%</td><td>9%</td><td>9%</td><td>8%</td><td>8%</td><td>7%</td><td>7%</td><td>7%</td></tr><tr><td>OP income</td><td>1,547</td><td>1,721</td><td>1,906</td><td>2,834</td><td>3,552</td><td>4,892</td><td>6,064</td><td>7,136</td><td>8,503</td></tr><tr><td>OPM</td><td>5%</td><td>5%</td><td>5%</td><td>6%</td><td>7%</td><td>8%</td><td>9%</td><td>9%</td><td>10%</td></tr><tr><td>Non-op gains</td><td>(25)</td><td>(72)</td><td>(168)</td><td>34</td><td>169</td><td>272</td><td>262</td><td>297</td><td>297</td></tr><tr><td>Pre-tax profit</td><td>1,522</td><td>1,649</td><td>1,738</td><td>2,868</td><td>3,721</td><td>5,164</td><td>6,325</td><td>7,433</td><td>8,800</td></tr><tr><td>Net profit</td><td>1,471</td><td>1,610</td><td>1,565</td><td>2,596</td><td>3,349</td><td>4,648</td><td>5,693</td><td>6,690</td><td>7,920</td></tr><tr><td>YoY</td><td>-54%</td><td>9%</td><td>-3%</td><td>66%</td><td>29%</td><td>39%</td><td>22%</td><td>18%</td><td>18%</td></tr><tr><td>EPS</td><td>0.82</td><td>0.90</td><td>0.87</td><td>1.45</td><td>1.87</td><td>2.60</td><td>3.18</td><td>3.74</td><td>4.43</td></tr><tr><td>2030 Target P/E</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>46.0x</td><td></td></tr><tr><td>12M target price (Rmb)</td><td></td><td></td><td></td><td></td><td>125</td><td></td><td></td><td></td><td></td></tr><tr><td>TP implied P/E</td><td></td><td></td><td></td><td></td><td>67</td><td>48</td><td>39</td><td></td><td></td></tr><tr><td colspan="10">COE assumption</td></tr><tr><td>Beta</td><td>1.20</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Risk free</td><td>3.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Market risk premium</td><td>6.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COE</td><td>11%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, GS Global Investment Research

![](images/e9e7fc836baf90f63fd5adb894f0a3197d7c43c8b9c8648fa96b5edf7efb2c9d.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 5: JCET P&L summary

<table><tr><td>(Rmb m)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="16">Income statement</td></tr><tr><td>Revenue</td><td>9,335</td><td>9,270</td><td>10,064</td><td>10,202</td><td>9,171</td><td>11,282</td><td>12,727</td><td>13,623</td><td>33,762</td><td>29,661</td><td>35,962</td><td>38,871</td><td>46,802</td><td>53,869</td><td>61,773</td></tr><tr><td>Gross profit</td><td>1,179</td><td>1,327</td><td>1,434</td><td>1,559</td><td>1,334</td><td>1,696</td><td>1,854</td><td>1,992</td><td>5,752</td><td>4,049</td><td>4,696</td><td>5,499</td><td>6,878</td><td>7,873</td><td>9,599</td></tr><tr><td>OP</td><td>354</td><td>427</td><td>508</td><td>617</td><td>413</td><td>655</td><td>835</td><td>930</td><td>3,265</td><td>1,547</td><td>1,721</td><td>1,906</td><td>2,834</td><td>3,552</td><td>4,892</td></tr><tr><td>EBITDA</td><td>1,363</td><td>1,437</td><td>1,518</td><td>1,627</td><td>1,423</td><td>1,860</td><td>2,040</td><td>2,331</td><td>6,929</td><td>4,992</td><td>5,261</td><td>5,944</td><td>7,654</td><td>8,504</td><td>9,986</td></tr><tr><td>Net income</td><td>203</td><td>267</td><td>483</td><td>611</td><td>290</td><td>578</td><td>821</td><td>907</td><td>3,231</td><td>1,471</td><td>1,610</td><td>1,565</td><td>2,596</td><td>3,349</td><td>4,648</td></tr><tr><td>EPS (Rmb)</td><td>0.11</td><td>0.15</td><td>0.27</td><td>0.34</td><td>0.16</td><td>0.32</td><td>0.46</td><td>0.51</td><td>1.82</td><td>0.82</td><td>0.90</td><td>0.87</td><td>1.45</td><td>1.87</td><td>2.60</td></tr><tr><td colspan="16">Margins</td></tr><tr><td>Gross margin</td><td>12.6%</td><td>14.3%</td><td>14.3%</td><td>15.3%</td><td>14.5%</td><td>15.0%</td><td>14.6%</td><td>14.6%</td><td>17.0%</td><td>13.7%</td><td>13.1%</td><td>14.1%</td><td>14.7%</td><td>14.6%</td><td>15.5%</td></tr><tr><td>OPM</td><td>3.8%</td><td>4.6%</td><td>5.0%</td><td>6.1%</td><td>4.5%</td><td>5.8%</td><td>6.6%</td><td>6.8%</td><td>9.7%</td><td>5.2%</td><td>4.8%</td><td>4.9%</td><td>6.1%</td><td>6.6%</td><td>7.9%</td></tr><tr><td>EBITDA margin</td><td>14.6%</td><td>15.5%</td><td>15.1%</td><td>15.9%</td><td>15.5%</td><td>16.5%</td><td>16.0%</td><td>17.1%</td><td>20.5%</td><td>16.8%</td><td>14.6%</td><td>15.3%</td><td>16.4%</td><td>15.8%</td><td>16.2%</td></tr><tr><td>Net margin</td><td>2.2%</td><td>2.9%</td><td>4.8%</td><td>6.0%</td><td>3.2%</td><td>5.1%</td><td>6.4%</td><td>6.7%</td><td>9.6%</td><td>5.0%</td><td>4.5%</td><td>4.0%</td><td>5.5%</td><td>6.2%</td><td>7.5%</td></tr><tr><td colspan="16">Ratios</td></tr><tr><td>Opex ratio</td><td>8.8%</td><td>9.7%</td><td>9.2%</td><td>9.2%</td><td>10.0%</td><td>9.2%</td><td>8.0%</td><td>7.8%</td><td>7.4%</td><td>8.4%</td><td>8.3%</td><td>9.2%</td><td>8.6%</td><td>8.0%</td><td>7.6%</td></tr><tr><td>Tax rate</td><td>24.6%</td><td>12.4%</td><td>20.7%</td><td>-11.1%</td><td>8.7%</td><td>10.0%</td><td>10.0%</td><td>10.0%</td><td>1.8%</td><td>3.4%</td><td>2.2%</td><td>9.7%</td><td>9.9%</td><td>10.0%</td><td>10.0%</td></tr><tr><td colspan="16">QoQ</td></tr><tr><td>Revenue</td><td>-15%</td><td>-1%</td><td>9%</td><td>1%</td><td>-10%</td><td>23%</td><td>13%</td><td>7%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross profit</td><td>-20%</td><td>12%</td><td>8%</td><td>9%</td><td>-14%</td><td>27%</td><td>9%</td><td>7%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating income</td><td>-29%</td><td>21%</td><td>19%</td><td>21%</td><td>-33%</td><td>59%</td><td>27%</td><td>11%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net income</td><td>-62%</td><td>31%</td><td>81%</td><td>27%</td><td>-53%</td><td>99%</td><td>42%</td><td>11%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBITDA</td><td>-11%</td><td>5%</td><td>6%</td><td>7%</td><td>-13%</td><td>31%</td><td>10%</td><td>14%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="16">YoY</td></tr><tr><td>Revenue</td><td>36%</td><td>7%</td><td>6%</td><td>-7%</td><td>-2%</td><td>22%</td><td>26%</td><td>34%</td><td>11%</td><td>-12%</td><td>21%</td><td>8%</td><td>20%</td><td>15%</td><td>15%</td></tr><tr><td>Gross profit</td><td>41%</td><td>7%</td><td>24%</td><td>6%</td><td>13%</td><td>28%</td><td>29%</td><td>28%</td><td>2%</td><td>-30%</td><td>16%</td><td>17%</td><td>25%</td><td>14%</td><td>22%</td></tr><tr><td>Operating income</td><td>118%</td><td>-15%</td><td>-9%</td><td>24%</td><td>17%</td><td>53%</td><td>64%</td><td>51%</td><td>5%</td><td>-53%</td><td>11%</td><td>11%</td><td>49%</td><td>25%</td><td>38%</td></tr><tr><td>Net income</td><td>50%</td><td>-45%</td><td>6%</td><td>15%</td><td>43%</td><td>116%</td><td>70%</td><td>48%</td><td>9%</td><td>-54%</td><td>9%</td><td>-3%</td><td>66%</td><td>29%</td><td>39%</td></tr><tr><td>EBITDA</td><td>30%</td><td>3%</td><td>5%</td><td>18%</td><td>4%</td><td>30%</td><td>34%</td><td>43%</td><td>4%</td><td>-28%</td><td>5%</td><td>13%</td><td>29%</td><td>11%</td><td>17%</td></tr></table>

Source: Company data, GS Global Investment Research

## Price Target Risks and Methodology - JCET

Valuation: We are Neutral-rated on JCET with a 12-month target price of Rmb125, which is based on 46x 2030E discounted P/E (discounted back to 2027E). Our target P/E is derived from correlation between peers P/E to the sum of NI YoY and OPM.

Key upside risks: Faster-/slower-than-expected semis capex expansion in China; Faster-/slower-than-expected technology development; Faster-/slower-than-expected shipments ramp up of advanced packaging.

<table><tr><td>600584.SS</td><td colspan="2">12m Price Target: Rmb125.00</td><td colspan="2">Price: Rmb85.49</td><td colspan="2">Upside: 46.2%</td></tr><tr><td colspan="2">Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td colspan="2">Market cap:</td><td>Revenue (Rmb mn) New</td><td>38,871.3</td><td>46,802.4</td><td>53,868.6</td><td>61,772.8</td></tr><tr><td colspan="2">Rmb153.0bn / $22.6bn</td><td>Revenue (Rmb mn) Old</td><td>38,871.3</td><td>46,398.1</td><td>53,868.6</td><td>61,772.8</td></tr><tr><td colspan="2">Enterprise value:</td><td>EBITDA (Rmb mn)</td><td>5,944.3</td><td>7,654.0</td><td>8,503.6</td><td>9,986.5</td></tr><tr><td colspan="2">Rmb162.8bn / $24.1bn</td><td>EPS (Rmb) New</td><td>0.87</td><td>1.45</td><td>1.87</td><td>2.60</td></tr><tr><td colspan="2">3m ADTV: Rmb16.6bn / $2.4bn</td><td>EPS (Rmb) Old</td><td>0.87</td><td>1.38</td><td>1.87</td><td>2.60</td></tr><tr><td colspan="2">China</td><td>P/E (X)</td><td>41.8</td><td>58.9</td><td>45.7</td><td>32.9</td></tr><tr><td colspan="2">Greater China Technology</td><td>P/B (X)</td><td>2.1</td><td>4.6</td><td>4.2</td><td>3.8</td></tr><tr><td colspan="2">M&amp;A Rank: 3</td><td>Dividend yield (%)</td><td>0.4</td><td>0.3</td><td>0.3</td><td>0.5</td></tr><tr><td colspan="2">Leases incl. in net debt &amp; EV?: Yes</td><td>CROCI (%)</td><td>8.2</td><td>15.0</td><td>12.5</td><td>12.7</td></tr><tr><td colspan="2"></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td colspan="2"></td><td>EPS (Rmb)</td><td>0.16</td><td>0.32</td><td>0.46</td><td>0.51</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 17 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Yifan Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise s

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
