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
# Montage (688008.SS): Rising memory interface IC with Gen-3/ Gen-4 ramp up; 2Q26 NI guidance beat; Buy

Montage announced 2Q26 revenues at Rmb1.9bn (34% YoY), or 5% higher than our estimates, driven by interconnect chip growth at 28% YoY in 2Q26 and strong growth of new products (PCIe retimer). The company guided 2Q26 NI at Rmb1.0bn\~Rmb1.2bn (+61%\~77% YoY), with the midpoint NI beating our estimates by 48%, which we attribute to the product mix upgrade toward new generation of products and better-than-expected non-OP. With the increasing adoption of agentic AI and heavier workload of CPUs and memory management, we are positive on the rising demand for the company's memory interface IC's and its expansion to new products across MRCD/ MDB, CXL, PCIe, and Optical interconnect ICs in the long-term. Maintain Buy.

Ramp up of DDR5 Gen-3/ Gen-4 interface IC: Management notes the contribution from DDR5 Gen-3 and Gen-4 interface IC continues to increase in 2Q26, driving better product mix and interconnect chips up 28% YoY/ 20% QoQ. Montage has also started the shipment of Gen-5 interface IC to clients. Mgmt. notes the company is developing the new generation of product DDR6 Gen-1 interface IC, and benefits from the strong momentum from clients. On MRCD/ MDB, the company is now undertaking verification of Gen-2 products with clients, and we expect the accelerated adoption to start from 2027E.

Earnings revision: We factor in Montage 2Q26 guidance, revise up 2026E earnings by \~8% on higher than expected revenues, GM an non-OP, supported by new generation of interface IC ramp up. Our 2027E-32E earnings are essentially unchanged.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Ting Song
+852-2978-6466 | ting.song@gs.com
GS (Asia) L.L.C.

Exhibit 1: Earnings revision

<table><tr><td rowspan="2">(Rmb bn)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td><td colspan="3">2029E</td><td colspan="3">2030E</td><td colspan="3">2031E</td><td colspan="3">2032E</td></tr><tr><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td></tr><tr><td>Revenue</td><td>8,212</td><td>8,122</td><td>1%</td><td>11,185</td><td>11,185</td><td>0%</td><td>15,737</td><td>15,737</td><td>0%</td><td>21,366</td><td>21,366</td><td>0%</td><td>29,478</td><td>29,478</td><td>0%</td><td>37,566</td><td>37,566</td><td>0%</td><td>45,555</td><td>45,555</td><td>0%</td></tr><tr><td>Gross profit</td><td>5,553</td><td>5,464</td><td>2%</td><td>7,298</td><td>7,298</td><td>0%</td><td>9,943</td><td>9,943</td><td>0%</td><td>13,350</td><td>13,350</td><td>0%</td><td>18,418</td><td>18,418</td><td>0%</td><td>23,506</td><td>23,506</td><td>0%</td><td>28,606</td><td>28,606</td><td>0%</td></tr><tr><td>Operating income</td><td>3,805</td><td>3,750</td><td>1%</td><td>5,336</td><td>5,358</td><td>0%</td><td>7,465</td><td>7,495</td><td>0%</td><td>10,246</td><td>10,284</td><td>0%</td><td>14,460</td><td>14,484</td><td>0%</td><td>18,691</td><td>18,721</td><td>0%</td><td>23,055</td><td>23,090</td><td>0%</td></tr><tr><td>Pre tax profit</td><td>4,445</td><td>4,119</td><td>8%</td><td>5,819</td><td>5,839</td><td>0%</td><td>7,992</td><td>8,018</td><td>0%</td><td>10,836</td><td>10,872</td><td>0%</td><td>15,134</td><td>15,156</td><td>0%</td><td>19,482</td><td>19,510</td><td>0%</td><td>24,004</td><td>24,037</td><td>0%</td></tr><tr><td>Net income</td><td>4,104</td><td>3,811</td><td>8%</td><td>5,338</td><td>5,356</td><td>0%</td><td>7,281</td><td>7,305</td><td>0%</td><td>9,823</td><td>9,855</td><td>0%</td><td>13,655</td><td>13,675</td><td>0%</td><td>17,530</td><td>17,555</td><td>0%</td><td>21,552</td><td>21,582</td><td>0%</td></tr><tr><td>EPS (Diluted)</td><td>3.36</td><td>3.12</td><td>8%</td><td>4.37</td><td>4.38</td><td>0%</td><td>5.96</td><td>5.98</td><td>0%</td><td>8.04</td><td>8.06</td><td>0%</td><td>11.17</td><td>11.19</td><td>0%</td><td>14.34</td><td>14.36</td><td>0%</td><td>17.63</td><td>17.66</td><td>0%</td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross margin</td><td>67.6%</td><td>67.3%</td><td></td><td>65.2%</td><td>65.2%</td><td></td><td>63.2%</td><td>63.2%</td><td></td><td>62.5%</td><td>62.5%</td><td></td><td>62.5%</td><td>62.5%</td><td></td><td>62.6%</td><td>62.6%</td><td></td><td>62.8%</td><td>62.8%</td><td></td></tr><tr><td>Operating margin</td><td>46.3%</td><td>46.2%</td><td></td><td>47.7%</td><td>47.9%</td><td></td><td>47.4%</td><td>47.6%</td><td></td><td>48.0%</td><td>48.1%</td><td></td><td>49.1%</td><td>49.1%</td><td></td><td>49.8%</td><td>49.8%</td><td></td><td>50.6%</td><td>50.7%</td><td></td></tr><tr><td>Net margin</td><td>50.0%</td><td>46.9%</td><td></td><td>47.7%</td><td>47.9%</td><td></td><td>46.3%</td><td>46.4%</td><td></td><td>46.0%</td><td>46.1%</td><td></td><td>46.3%</td><td>46.4%</td><td></td><td>46.7%</td><td>46.7%</td><td></td><td>47.3%</td><td>47.4%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: With 2027E-2032E earning estimates and target P/E essentially unchanged, we maintain our A-share TP at Rmb387 while tweaking H-share TP to HK\$583 (vs. HK\$582 previously).

For the A-share, our 12M target price of Rmb387 is based on a 48.0x (vs. 47.9x previously) 2030E discounted P/E, against 34% average EPS growth in 2030E-2031E (vs. 34% previously). Our target P/E multiple of 48.0x is derived from peers' P/E and NI growth correlation.

For the H-share, our 12M target price of HK\$583 is based on a 66.2x 2030E P/E (38% valuation premium over the A-share and using a 1.09 CNY/HKD). The H-A premium is based on the last 30-trading-day average H-A premium of the company.

Exhibit 2: Montage: 2030E discounted P/E

<table><tr><td>Rmb m</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td><td>2032E</td></tr><tr><td>Key assumptions</td><td colspan="4">RCD DDR5 penetration</td><td colspan="4">MRDIMM, CKD, PCIe Retimer/ Switch</td><td colspan="3">PCIe Switch/ CXL</td></tr><tr><td>Revenues %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RDIMM interconnect</td><td>73%</td><td>93%</td><td>79%</td><td>77%</td><td>57%</td><td>45%</td><td>37%</td><td>30%</td><td>23%</td><td>18%</td><td>15%</td></tr><tr><td>MRDIMM interconnect</td><td>0%</td><td>0%</td><td>1%</td><td>2%</td><td>6%</td><td>10%</td><td>14%</td><td>15%</td><td>20%</td><td>26%</td><td>27%</td></tr><tr><td>CKD</td><td>0%</td><td>0%</td><td>2%</td><td>4%</td><td>14%</td><td>14%</td><td>12%</td><td>10%</td><td>8%</td><td>7%</td><td>6%</td></tr><tr><td>PCIe Retimer</td><td>2%</td><td>3%</td><td>9%</td><td>11%</td><td>17%</td><td>21%</td><td>22%</td><td>21%</td><td>20%</td><td>18%</td><td>17%</td></tr><tr><td>PCIe Switch</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>2%</td><td>6%</td><td>14%</td><td>20%</td><td>22%</td><td>24%</td></tr><tr><td>CXL</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>2%</td><td>4%</td><td>4%</td><td>5%</td><td>5%</td></tr><tr><td>Revenues</td><td>3,672</td><td>2,286</td><td>3,639</td><td>5,456</td><td>8,212</td><td>11,185</td><td>15,737</td><td>21,366</td><td>29,478</td><td>37,566</td><td>45,555</td></tr><tr><td>Rev YoY growth</td><td></td><td>-38%</td><td>59%</td><td>50%</td><td>51%</td><td>36%</td><td>41%</td><td>36%</td><td>38%</td><td>27%</td><td>21%</td></tr><tr><td>Gross Profit</td><td>1,706</td><td>1,347</td><td>2,115</td><td>3,395</td><td>5,553</td><td>7,298</td><td>9,943</td><td>13,350</td><td>18,418</td><td>23,506</td><td>28,606</td></tr><tr><td>GM</td><td>46.4%</td><td>58.9%</td><td>58.1%</td><td>62.2%</td><td>67.6%</td><td>65.2%</td><td>63.2%</td><td>62.5%</td><td>62.5%</td><td>62.6%</td><td>62.8%</td></tr><tr><td>Opex</td><td>(858)</td><td>(950)</td><td>(1,062)</td><td>(1,568)</td><td>(1,748)</td><td>(1,962)</td><td>(2,478)</td><td>(3,104)</td><td>(3,958)</td><td>(4,815)</td><td>(5,551)</td></tr><tr><td>Opex ratio</td><td>-23.4%</td><td>-41.6%</td><td>-29.2%</td><td>-28.7%</td><td>-21.3%</td><td>-17.5%</td><td>-15.7%</td><td>-14.5%</td><td>-13.4%</td><td>-12.8%</td><td>-12.2%</td></tr><tr><td>EBIT</td><td>848</td><td>396</td><td>1,053</td><td>1,827</td><td>3,805</td><td>5,336</td><td>7,465</td><td>10,246</td><td>14,460</td><td>18,691</td><td>23,055</td></tr><tr><td>OP margin</td><td>23.1%</td><td>17.3%</td><td>28.9%</td><td>33.5%</td><td>46.3%</td><td>47.7%</td><td>47.4%</td><td>48.0%</td><td>49.1%</td><td>49.8%</td><td>50.6%</td></tr><tr><td>Non-OP</td><td>566</td><td>76</td><td>359</td><td>493</td><td>640</td><td>483</td><td>526</td><td>590</td><td>674</td><td>790</td><td>949</td></tr><tr><td>Pre tax income</td><td>1,414</td><td>472</td><td>1,413</td><td>2,321</td><td>4,445</td><td>5,819</td><td>7,992</td><td>10,836</td><td>15,134</td><td>19,482</td><td>24,004</td></tr><tr><td>Tax</td><td>114</td><td>21</td><td>72</td><td>191</td><td>404</td><td>598</td><td>839</td><td>1,155</td><td>1,634</td><td>2,124</td><td>2,640</td></tr><tr><td>Net income (Attributed to owners)</td><td>1,299</td><td>451</td><td>1,412</td><td>2,236</td><td>4,104</td><td>5,338</td><td>7,281</td><td>9,823</td><td>13,655</td><td>17,530</td><td>21,552</td></tr><tr><td>Net income YoY growth</td><td></td><td>-65%</td><td>213%</td><td>58%</td><td>84%</td><td>30%</td><td>36%</td><td>35%</td><td>39%</td><td>28%</td><td>23%</td></tr><tr><td>EPS (Rmb)</td><td>1.15</td><td>0.40</td><td>1.24</td><td>1.95</td><td>3.36</td><td>4.37</td><td>5.96</td><td>8.04</td><td>11.17</td><td>14.34</td><td>17.63</td></tr><tr><td>EPS YoY growth</td><td></td><td>-66%</td><td>212%</td><td>58%</td><td>72%</td><td>30%</td><td>36%</td><td>35%</td><td>39%</td><td>28%</td><td>23%</td></tr><tr><td colspan="12">A shares</td></tr><tr><td>2030E Target P/E</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>48.0x</td><td></td><td></td></tr><tr><td>Target multiple x EPS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>536</td><td></td><td></td></tr><tr><td>TP (Rmb, 2027E)</td><td></td><td></td><td></td><td></td><td></td><td>387.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Implied P/E</td><td></td><td></td><td></td><td></td><td></td><td>89x</td><td>65x</td><td>48x</td><td>35x</td><td>27x</td><td>22x</td></tr><tr><td>Implied P/B</td><td></td><td></td><td></td><td></td><td></td><td>20x</td><td>17x</td><td>15x</td><td>12x</td><td>10x</td><td>8x</td></tr><tr><td colspan="12">H shares</td></tr><tr><td>H-A premium</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>38%</td><td></td><td></td></tr><tr><td>2030E Target P/E</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>66.2x</td><td></td><td></td></tr><tr><td>Target multiple x EPS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>740</td><td></td><td></td></tr><tr><td>CNYHKD</td><td></td><td></td><td></td><td></td><td></td><td>1.09</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TP (HK$, 2027E)</td><td></td><td></td><td></td><td></td><td></td><td>583.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Implied P/E</td><td></td><td></td><td></td><td></td><td></td><td>122x</td><td>90x</td><td>67x</td><td>48x</td><td>37x</td><td>30x</td></tr><tr><td>Implied P/B</td><td></td><td></td><td></td><td></td><td></td><td>28x</td><td>24x</td><td>20x</td><td>17x</td><td>14x</td><td>11x</td></tr></table>

<table><tr><td colspan="2">COE assumption</td></tr><tr><td>Beta</td><td>1.3</td></tr><tr><td>Risk free</td><td>3.0%</td></tr><tr><td>Market risk premium</td><td>6.5%</td></tr><tr><td>COE</td><td>11.5%</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 3: Montage (A): 12M forward P/E  
![](images/e0bb801314ec1632e8312eb943a20eb2909ba5960d771f4a84554f3b630bcc66.jpg)  
Source: Company data, GS Global Investment Research, LSEG Data & Analytics

Exhibit 4: Montage(H): 12m forward P/E  
![](images/e22f32c4ee0300ac95ffc3c20d69abf2ed22b90cea1b67195a27ac9f0371249e.jpg)  
Source: Company data, GS Global Investment Research, LSEG Data & Analytics

Exhibit 5: Montage P&L Summary

<table><tr><td>(Rmb mn)</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td><td>2032E</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td>Revenue</td><td>3,672</td><td>2,286</td><td>3,639</td><td>5,456</td><td>8,212</td><td>11,185</td><td>15,737</td><td>21,366</td><td>29,478</td><td>37,566</td><td>45,555</td><td>1,222</td><td>1,411</td><td>1,424</td><td>1,399</td><td>1,461</td><td>1,875</td><td>2,355</td><td>2,522</td></tr><tr><td>COGS</td><td>1,967</td><td>939</td><td>1,524</td><td>2,061</td><td>2,659</td><td>3,887</td><td>5,795</td><td>8,016</td><td>11,060</td><td>14,060</td><td>16,949</td><td>483</td><td>558</td><td>522</td><td>497</td><td>441</td><td>618</td><td>778</td><td>822</td></tr><tr><td>Gross profit</td><td>1,706</td><td>1,347</td><td>2,115</td><td>3,395</td><td>5,553</td><td>7,298</td><td>9,943</td><td>13,350</td><td>18,418</td><td>23,506</td><td>28,606</td><td>739</td><td>853</td><td>902</td><td>902</td><td>1,019</td><td>1,257</td><td>1,578</td><td>1,699</td></tr><tr><td>Selling expenses</td><td>86</td><td>90</td><td>96</td><td>120</td><td>130</td><td>147</td><td>165</td><td>181</td><td>208</td><td>239</td><td>263</td><td>24</td><td>27</td><td>31</td><td>38</td><td>29</td><td>29</td><td>32</td><td>40</td></tr><tr><td>G&amp;A expenses</td><td>202</td><td>173</td><td>196</td><td>526</td><td>477</td><td>512</td><td>604</td><td>701</td><td>841</td><td>967</td><td>1,063</td><td>102</td><td>120</td><td>370</td><td>(65)</td><td>127</td><td>121</td><td>111</td><td>117</td></tr><tr><td>R&amp;D expenses</td><td>563</td><td>682</td><td>763</td><td>915</td><td>1,132</td><td>1,290</td><td>1,690</td><td>2,197</td><td>2,874</td><td>3,564</td><td>4,170</td><td>153</td><td>204</td><td>176</td><td>382</td><td>188</td><td>245</td><td>317</td><td>382</td></tr><tr><td>Operating expense</td><td>858</td><td>950</td><td>1,062</td><td>1,568</td><td>1,748</td><td>1,962</td><td>2,478</td><td>3,104</td><td>3,958</td><td>4,815</td><td>5,551</td><td>280</td><td>353</td><td>578</td><td>357</td><td>346</td><td>397</td><td>463</td><td>542</td></tr><tr><td>Operating income</td><td>848</td><td>396</td><td>1,053</td><td>1,827</td><td>3,805</td><td>5,336</td><td>7,465</td><td>10,246</td><td>14,460</td><td>18,691</td><td>23,055</td><td>458</td><td>500</td><td>324</td><td>545</td><td>673</td><td>860</td><td>1,115</td><td>1,157</td></tr><tr><td>Non-op</td><td>566</td><td>76</td><td>359</td><td>493</td><td>640</td><td>483</td><td>526</td><td>590</td><td>674</td><td>790</td><td>949</td><td>72</td><td>155</td><td>183</td><td>83</td><td>204</td><td>328</td><td>58</td><td>49</td></tr><tr><td>Pre tax profit</td><td>1,414</td><td>472</td><td>1,413</td><td>2,321</td><td>4,445</td><td>5,819</td><td>7,992</td><td>10,836</td><td>15,134</td><td>19,482</td><td>24,004</td><td>531</td><td>655</td><td>507</td><td>628</td><td>877</td><td>1,189</td><td>1,173</td><td>1,206</td></tr><tr><td>Tax</td><td>114</td><td>21</td><td>72</td><td>191</td><td>404</td><td>598</td><td>839</td><td>1,155</td><td>1,634</td><td>2,124</td><td>2,6

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
