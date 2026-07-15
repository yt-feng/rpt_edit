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
<table><tr><td colspan="2">MS MUFG SECURITIES CO., LTD.+</td></tr><tr><td colspan="2">Takato Watabe</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Takato.Watabe@morganstanleymufg.com</td><td>+81 3 6836-5436</td></tr><tr><td colspan="2">Ryoichi Watanabe</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Ryoichi.Watanabe@morganstanleymufg.com</td><td>+81 3 6836-8929</td></tr><tr><td colspan="2">Kayoko Shoji</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Kayoko.Shoji@morganstanleymufg.com</td><td>+81 3 6836-5437</td></tr><tr><td colspan="2">Kano Fujita</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Kano.Fujita@morganstanleymufg.com</td><td>+81 3 6836-8932</td></tr></table>

Investor Presentation | Japan

# Chemicals: Industry Reshuffling also Gaining Steam amid an AI-driven Market

Petrochemical majors (Industry View: Attractive): Expecting continued weak petrochemical demand and ethylene utilization rates, but in addition to China's anti-involution policies, there are signs of naphtha cracker downsizing in South Korea; believe the overall mood is improving. Asia petchem prices and spreads unlikely to fall further, but probably lack recovery momentum. Added impetus for industry reorganization. Investment indicators remain low and shares look generally undervalued. Investment appeal in Sumitomo Chemicals, as it focuses resources on accelerating growth in the agrochemicals and IT-related sectors. OW on Sumitomo Chemical (4005), Mitsui Chemicals (4183), Asahi Kasei (3407); EW on Mitsubishi Chemical (4188), Tosoh (4042).

Electronic chemicals (Industry View: In-line): In addition to the expansion of AI semiconductors, demand for legacy semiconductors is also gradually recovering, and a steady growth trend continues. For silicon wafers, although user inventory levels remain high, the recovery trend continues, centered on 300mm wafers. We are OW on Zeon (4205), Shin-Etsu Chemical (4063); EW on Nissan Chemical (4021), Dexerials (4980), Kuraray (3405); UW on SUMCO (3436), Nitto Denko (6988).

Fine chemicals (Industry View: In-line): Carbon fiber composite materials show significant revenue improvement due to full recovery in aircraft applications. Toray is our Top Pick, with the top share in carbon fiber business and strength in textiles and functional chemicals. We are OW on Toray (3402); EW on Gunze (3002); UW on Teijin (3401); ++ on DIC (4631).

[++] indicates the data for this company have been removed from consideration because under MS policy and/or applicable regulations, MS may be precluded from issuing such information with respect to this company at this time.

![](images/3d065f1f48847b17464f55fe671d962b38f5f5c25d785caec39c0e5979a01c4f.jpg)

![](images/13b58344971cdd600f631636633374b9c12acd085046cfbfc98b3a4ece1fc511.jpg)

<table><tr><td colspan="2">PETROCHEMICAL MAJORS</td></tr><tr><td>Japan</td><td></td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td colspan="2">ELECTRONIC CHEMICALS</td></tr><tr><td>Japan</td><td></td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td colspan="2">FINE CHEMICALS</td></tr><tr><td>Japan</td><td></td></tr><tr><td>Industry View</td><td>In-Line</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Asia Research

## A New Landing Page

CLICK HERE FOR ACCESS

Industry reshuffling also gaining steam amid an AI-driven market

<table><tr><td rowspan="2">Company</td><td rowspan="2">Code</td><td rowspan="2">Rating</td><td rowspan="2">C. Price13-Jul</td><td rowspan="2">PriceTarget</td><td colspan="5">% Difference from Current Price</td></tr><tr><td>-60%</td><td>-40%</td><td>-20%</td><td>0%</td><td>20%</td></tr><tr><td>Petrochemical Majors</td><td colspan="9">Attractive</td></tr><tr><td>Sumitomo Chemical</td><td>4005</td><td>OW</td><td>¥519</td><td>¥850</td><td></td><td>-13%</td><td></td><td>64%</td><td>122%</td></tr><tr><td>Mitsui Chemicals</td><td>4183</td><td>OW</td><td>¥2,070</td><td>¥2,900</td><td></td><td>-8%</td><td></td><td>40%</td><td>93%</td></tr><tr><td>Asahi Kasei</td><td>3407</td><td>OW</td><td>¥1,816</td><td>¥2,200</td><td></td><td>-6%</td><td></td><td>21%</td><td>49%</td></tr><tr><td>Mitsubishi Chemical Group</td><td>4188</td><td>EW</td><td>¥1,162</td><td>¥1,250</td><td></td><td>-18%</td><td></td><td>8%</td><td>29%</td></tr><tr><td>Tosoh</td><td>4042</td><td>EW</td><td>¥2,691</td><td>¥2,900</td><td></td><td>-22%</td><td></td><td>8%</td><td>34%</td></tr><tr><td>Electronic Chemicals</td><td colspan="9">In-Line</td></tr><tr><td>Zeon</td><td>4205</td><td>OW</td><td>¥2,225</td><td>¥3,000</td><td></td><td>-6%</td><td></td><td>35%</td><td>73%</td></tr><tr><td>Shin-Etsu Chemical</td><td>4063</td><td>OW</td><td>¥7,340</td><td>¥8,200</td><td></td><td>-14%</td><td></td><td>12%</td><td>29%</td></tr><tr><td>Nissan Chemical</td><td>4021</td><td>EW</td><td>¥7,906</td><td>¥9,000</td><td></td><td>-24%</td><td></td><td>14%</td><td>39%</td></tr><tr><td>Dexerials</td><td>4980</td><td>EW</td><td>¥3,922</td><td>¥4,400</td><td>-46%</td><td></td><td></td><td>12%</td><td>53%</td></tr><tr><td>Kuraray</td><td>3405</td><td>EW</td><td>¥1,696</td><td>¥1,750</td><td></td><td>-26%</td><td></td><td>3%</td><td>30%</td></tr><tr><td>SUMCO</td><td>3436</td><td>UW</td><td>¥5,133</td><td>¥3,000</td><td>-42%</td><td></td><td></td><td>13%</td><td></td></tr><tr><td>Nitto Denko</td><td>6988</td><td>UW</td><td>¥3,221</td><td>¥3,000</td><td>-32%</td><td>-7%</td><td></td><td>21%</td><td></td></tr><tr><td>Fine Chemicals</td><td colspan="9">In-Line</td></tr><tr><td>Toray</td><td>3402</td><td>OW</td><td>¥1,138</td><td>¥1,600</td><td></td><td>-3%</td><td></td><td>41%</td><td>76%</td></tr><tr><td>Gunze</td><td>3002</td><td>EW</td><td>¥3,970</td><td>¥4,200</td><td></td><td>-29%</td><td></td><td>6%</td><td>28%</td></tr><tr><td>Teijin</td><td>3401</td><td>UW</td><td>¥1,655</td><td>¥1,450</td><td>-46%</td><td>-12%</td><td></td><td>27%</td><td></td></tr><tr><td>DIC</td><td>4631</td><td>++</td><td>¥4,520</td><td>++</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10">Source: FactSet, MS</td></tr></table>

[++] indicates the data for this company have been removed from consideration because under MS policy and/or applicable regulations, MS may be precluded from issuing such information with respect to this company at this time.

## Overall Summary: Chemicals industry coverage list & key investment metrics

Recommended stocks:
Zeon (4205), Sumitomo Chemical (4005), Toray (3402), Asahi Kasei (3407), Shin-Etsu Chemical (4063)

<table><tr><td rowspan="2"></td><td rowspan="2">Rating</td><td rowspan="2">Share price (¥) (13-Jul)</td><td rowspan="2">Price target (¥)</td><td colspan="3">P/E (x)</td><td colspan="3">P/CF (x)</td><td colspan="3">EV/EBITDA (x)</td><td colspan="3">P/B (x)</td><td colspan="3">Dividend yield (%)</td><td rowspan="2">Mkt cap (¥bn)</td><td colspan="2">FX Sensitivity for OP (¥bn)</td><td colspan="2">FX Sensitivity vs F26 MS (core) OP</td><td colspan="2">Company FX assumptions (F26)</td></tr><tr><td>F26e</td><td>F27e</td><td>F28e</td><td>F26e</td><td>F27e</td><td>F28e</td><td>F26e</td><td>F27e</td><td>F28e</td><td>F26e</td><td>F27e</td><td>F28e</td><td>F26e</td><td>F27e</td><td>F28e</td><td>vs. USD</td><td>vs. EUR</td><td>vs. USD</td><td>vs. EUR</td><td>(¥/USD)</td><td>(¥/EUR)</td></tr><tr><td colspan="26">Petrochemical Majors</td></tr><tr><td>3407 Asahi Kasei</td><td>OW</td><td>1,816</td><td>2,200</td><td>14.3</td><td>12.1</td><td>10.7</td><td>6.3</td><td>5.8</td><td>5.4</td><td>6.7</td><td>6.2</td><td>5.8</td><td>1.1</td><td>1.1</td><td>1.0</td><td>2.4</td><td>2.9</td><td>3.2</td><td>2,462.6</td><td>1.6</td><td>0.1</td><td>0.6%</td><td>0.0%</td><td>150.0</td><td>175.0</td></tr><tr><td>4005 Sumitomo Chemical</td><td>OW</td><td>519</td><td>850</td><td>8.7</td><td>6.5</td><td>5.6</td><td>3.9</td><td>3.4</td><td>3.1</td><td>6.3</td><td>5.5</td><td>5.4</td><td>0.8</td><td>0.7</td><td>0.7</td><td>4.6</td><td>4.8</td><td>5.4</td><td>857.1</td><td>2.0</td><td>-</td><td>0.8%</td><td>-</td><td>155.0</td><td>-</td></tr><tr><td>4042 Tosoh</td><td>EW</td><td>2,691</td><td>2,900</td><td>13.7</td><td>12.8</td><td>11.2</td><td>7.4</td><td>7.0</td><td>6.5</td><td>6.6</td><td>6.5</td><td>6.3</td><td>1.0</td><td>0.9</td><td>0.9</td><td>3.7</td><td>3.7</td><td>3.7</td><td>828.4</td><td>0.5</td><td>0.2</td><td>0.5%</td><td>0.2%</td><td>-</td><td>-</td></tr><tr><td>4183 Mitsui Chemicals</td><td>OW</td><td>2,070</td><td>2,900</td><td>12.8</td><td>8.3</td><td>6.8</td><td>4.0</td><td>3.3</td><td>3.1</td><td>7.7</td><td>6.4</td><td>5.8</td><td>0.8</td><td>0.8</td><td>0.7</td><td>3.6</td><td>4.1</td><td>4.8</td><td>762.0</td><td>0.8-0.9</td><td>-</td><td>0.7%</td><td>-</td><td>155.0</td><td>-</td></tr><tr><td>4188 Mitsubishi Chemical Group</td><td>EW</td><td>1,162</td><td>1,250</td><td>13.1</td><td>11.7</td><td>10.1</td><td>3.9</td><td>3.8</td><td>3.6</td><td>6.2</td><td>6.0</td><td>5.7</td><td>0.9</td><td>0.8</td><td>0.8</td><td>2.8</td><td>3.0</td><td>3.4</td><td>1,578.0</td><td>1.1</td><td>-</td><td>0.4%</td><td>-</td><td>150.0</td><td>-</td></tr><tr><td>Petrochemical Majors average</td><td colspan="3">Attractive</td><td>12.9</td><td>10.7</td><td>9.5</td><td>5.0</td><td>4.7</td><td>4.5</td><td>6.6</td><td>6.1</td><td>5.7</td><td>1.0</td><td>0.9</td><td>0.9</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="26">Electronic Chemicals</td></tr><tr><td>3405 Kuraray</td><td>EW</td><td>1,696</td><td>1,750</td><td>15.7</td><td>12.6</td><td>10.8</td><td>4.3</td><td>3.9</td><td>3.6</td><td>5.2</td><td>4.9</td><td>4.7</td><td>0.7</td><td>0.6</td><td>0.6</td><td>3.8</td><td>3.8</td><td>3.8</td><td>511.0</td><td>0.1</td><td>0.2</td><td>0.2%</td><td>0.3%</td><td>150.0</td><td>175.0</td></tr><tr><td>3436 SUMCO</td><td>UW</td><td>5,133</td><td>3,000</td><td>-</td><td>138.1</td><td>59.8</td><td>15.6</td><td>14.0</td><td>13.1</td><td>16.8</td><td>15.2</td><td>13.4</td><td>3.3</td><td>3.3</td><td>3.1</td><td>0.4</td><td>0.4</td><td>0.6</td><td>1,795.1</td><td>1.1</td><td>-</td><td>-</td><td>-</td><td>160.0</td><td>-</td></tr><tr><td>4021 Nissan Chemical</td><td>EW</td><td>7,906</td><td>9,000</td><td>20.3</td><td>19.5</td><td>18.9</td><td>14.9</td><td>14.2</td><td>13.7</td><td>12.4</td><td>11.8</td><td>11.5</td><td>3.9</td><td>3.7</td><td>3.5</td><td>2.7</td><td>2.8</td><td>2.9</td><td>1,060.3</td><td>0.3</td><td>-</td><td>0.4%</td><td>-</td><td>150.0</td><td>-</td></tr><tr><td>4063 Shin-Etsu Chemical</td><td>OW</td><td>7,340</td><td>8,200</td><td>22.2</td><td>20.0</td><td>18.1</td><td>15.8</td><td>14.4</td><td>13.1</td><td>12.3</td><td>11.6</td><td>10.8</td><td>3.0</td><td>2.9</td><td>2.8</td><td>1.8</td><td>2.0</td><td>2.2</td><td>13,628.3</td><td>3.9</td><td>0.2</td><td>0.5%</td><td>0.03%</td><td>150.0</td><td>180.0</td></tr><tr><td>4205 Zeon</td><td>OW</td><td>2,225</td><td>3,000</td><td>11.2</td><td>10.7</td><td>9.7</td><td>7.2</td><td>7.0</td><td>6.6</td><td>7.2</td><td>6.9</td><td>6.8</td><td>1.1</td><td>1.0</td><td>1.0</td><td>3.6</td><td>3.7</td><td>4.1</td><td>425.6</td><td>0.3</td><td>0.1</td><td>0.7%</td><td>-</td><td>150.0</td><td>175.0</td></tr><tr><td>4980 Dexerials</td><td>EW</td><td>3,922</td><td>4,400</td><td>23.8</td><td>20.6</td><td>18.1</td><td>18.1</td><td>15.3</td><td>13.1</td><td>14.8</td><td>12.6</td><td>10.9</td><td>5.4</td><td>4.9</td><td>4.4</td><td>1.6</td><td>1.8</td><td>2.0</td><td>657.0</td><td>0.5</td><td>-</td><td>1.2%</td><td>-</td><td>150.0</td><td>-</td></tr><tr><td>6988 Nitto Denko</td><td>UW</td><td>3,221</td><td>3,000</td><td>15.8</td><td>14.5</td><td>13.0</td><td>9.8</td><td>9.1</td><td>8.5</td><td>7.1</td><td>6.8</td><td>6.5</td><td>1.8</td><td>1.7</td><td>1.6</td><td>2.0</td><td>2.0</td><td>2.2</td><td>2,169.9</td><td>2.7</td><td>-</td><td>1.5%</td><td>-</td><td>153.0</td><td>-</td></tr><tr><td>Electronic Chemicals average</td><td colspan="3">In-Line</td><td>23.7</td><td>21.0</td><td>19.2</td><td>14.0</td><td>13.1</td><td>12.3</td><td>11.1</td><td>10.5</td><td>9.8</td><td>2.6</td><td>2.6</td><td>2.6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="26">Fine Chemicals (In-Line)</td></tr><tr><td>3002 Gunze</td><td>EW</td><td>3,970</td><td>4,200</td><td>25.3</td><td>19.3</td><td>16.0</td><td>10.1</td><td>9.1</td><td>33.1</td><td>8.0</td><td>7.0</td><td>6.5</td><td>1.1</td><td>1.1</td><td>1.1</td><td>5.4</td><td>5.5</td><td>5.5</td><td>126.7</td><td>0.10</td><td>-</td><td>1.2%</td><td>-</td><td>155.0</td><td>-</td></tr><tr><td>3401 Teijin</td><td>UW</td><td>1,655</td><td>1,450</td><td>7.6</td><td>19.4</td><td>15.6</td><td>3.4</td><td>4.5</td><td>4.2</td><td>7.0</td><td>6.4</td><td>5.9</td><td>0.8</td><td>0.8</td><td>0.8</td><td>3.0</td><td>3.0</td><td>3.0</td><td>319.3</td><td>0.25</td><td>-</td><td>0.9%</td><td>-</td><td>150.0</td><td>176.0</td></tr><tr><td>3402 Toray</td><td>OW</td><td>1,138</td><td>1,600</td><td>14.3</td><td>11.0</td><td>9.1</td><td>6.4</td><td>5.5</td><td>5.0</td><td>8.3</td><td>7.4</td><td>6.8</td><td>0.9</td><td>0.8</td><td>0.8</td><td>2.3</td><td>2.6</td><td>3.2</td><td>1,657.1</td><td>1.0</td><td>-</td><td>0.6%</td><td>-</td><td>150.0</td><td>-</td></tr><tr><td>4631 DIC</td><td>++</td><td>4,520</td><td>++</td><td>12.4</td><td>13.2</td><td>12.2</td><td>4.8</td><td>4.7</td><td>4.6</td><td>7.4</td><td>7.3</td><td>7.0</td><td>0.9</td><td>0.8</td><td>0.8</td><td>3.1</td><td>3.3</td><td>3.5</td><td>428.0</td><td>0.2</td><td>-</td><td>0.3%</td><td>-</td><td>150.0</td><td>168.0</td></tr></table>

[++] indicates the data for this company have been removed from consideration because under MS policy and/or applicable regulations, MS may be precluded from issuing such information with respect to this company at this time.  
Fiscal years for Kuraray, SUMCO, and DIC end in December
FX Assumption: Shin-Etsu F3/27 1Q, SUMCO F12/26 2Q
e = MS estimates
Source: Company data, FactSet, MS

Chemicals industry earnings estimates (1)

<table><tr><td rowspan="2"></td><td colspan="2">Sales</td><td colspan="2">Core Operating profit</td><td colspan="2">Operating profit</td><td colspan="2">Recurring/ Pretax profit</td><td colspan="2">Net profit</td><td>EPS</td></tr><tr><td>(¥m)</td><td>(% YoY)</td><td>(¥m)</td><td>(% YoY)</td><td>(¥m)</td><td>(% YoY)</td><td>(¥m)</td><td>(% YoY)</td><td>(¥m)</td><td>(% YoY)</td><td>(¥)</td></tr><tr><td colspan="12">- Petrochemical Majors</td></tr><tr><td colspan="12">(3407) Asahi Kasei</td></tr><tr><td>3/25</td><td>3,037,312</td><td>9.1</td><td>-</td><td>-</td><td>211,921</td><td>50.6</td><td>193,459</td><td>114.7</td><td>134,996</td><td>208.2</td><td>97.9</td></tr><tr><td>3/26</td><td>3,074,505</td><td>1.2</td><td>-</td><td>-</td><td>231,200</td><td>9.1</td><td>230,419</td><td>19.1</td><td>158,793</td><td>17.6</td><td>117.0</td></tr><tr><td>3/27Ce</td><td>3,254,000</td><td>5.8</td><td>-</td><td>-</td><td>248,000</td><td>7.3</td><td>247,500</td><td>7.4</td><td>160,000</td><td>0.8</td><td>119.7</td></tr><tr><td>3/27e</td><td>3,301,000</td><td>7.4</td><td>-</td><td>-</td><td>267,000</td><td>15.5</td><td>266,500</td><td>1

[中间内容因长度限制已省略]

relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Petrochemical Majors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/13/2026)</td></tr><tr><td colspan="3">Takato Watabe</td></tr><tr><td>Asahi Kasei (3407.T)</td><td>O (06/23/2025)</td><td>¥1,816</td></tr><tr><td>Mitsubishi Chemical Group (4188.T)</td><td>E (06/26/2025)</td><td>¥1,162</td></tr><tr><td>Mitsui Chemicals (4183.T)</td><td>O (08/31/2015)</td><td>¥2,070</td></tr><tr><td>Sumitomo Chemical (4005.T)</td><td>O (04/21/2014)</td><td>¥519</td></tr><tr><td>Tosoh (4042.T)</td><td>E (04/10/2023)</td><td>¥2,691</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: Electronic Chemicals

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/13/2026)</td></tr><tr><td colspan="3">Ryoichi Watanabe</td></tr><tr><td>Resonac Holdings (4004.T)</td><td>O (03/04/2024)</td><td>¥15,330</td></tr><tr><td>Sumitomo Bakelite (4203.T)</td><td>O (05/26/2025)</td><td>¥7,035</td></tr><tr><td>Tokyo Ohka Kogyo (4186.T)</td><td>E (06/10/2025)</td><td>¥10,350</td></tr><tr><td colspan="3">Takato Watabe</td></tr><tr><td>Dexerials (4980.T)</td><td>E (08/27/2024)</td><td>¥3,922</td></tr><tr><td>Kuraray (3405.T)</td><td>E (04/03/2023)</td><td>¥1,696</td></tr><tr><td>Nissan Chemical (4021.T)</td><td>E (06/11/2018)</td><td>¥7,906</td></tr><tr><td>Nitto Denko (6988.T)</td><td>U (06/24/2022)</td><td>¥3,221</td></tr><tr><td>Shin-Etsu Chemical (4063.T)</td><td>O (07/27/2016)</td><td>¥7,340</td></tr><tr><td>SUMCO (3436.T)</td><td>U (06/09/2026)</td><td>¥5,133</td></tr><tr><td>ZEON (4205.T)</td><td>O (10/23/2014)</td><td>¥2,225</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: Fine Chemicals

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/13/2026)</td></tr><tr><td colspan="3">Ryoichi Watanabe</td></tr><tr><td>Air Water (4088.T)</td><td>E (03/04/2024)</td><td>¥2,522</td></tr><tr><td>Daicel (4202.T)</td><td>E (06/20/2025)</td><td>¥1,404</td></tr><tr><td>Denka (4061.T)</td><td>E (03/04/2024)</td><td>¥3,838</td></tr><tr><td>Kaneka (4118.T)</td><td>E (03/04/2024)</td><td>¥5,568</td></tr><tr><td>Kureha (4023.T)</td><td>E (06/12/2025)</td><td>¥4,090</td></tr><tr><td>Mitsubishi Gas Chemical (4182.T)</td><td>O (03/04/2024)</td><td>¥4,564</td></tr><tr><td>Nippon Sanso Holdings (4091.T)</td><td>U (06/20/2025)</td><td>¥6,052</td></tr><tr><td>NOF (4403.T)</td><td>O (03/19/2026)</td><td>¥2,720</td></tr><tr><td>Sekisui Chemical (4204.T)</td><td>U (05/07/2025)</td><td>¥2,611</td></tr><tr><td>Tokuyama (4043.T)</td><td>O (03/04/2024)</td><td>¥4,507</td></tr><tr><td>UBE (4208.T)</td><td>++</td><td>¥3,100</td></tr><tr><td colspan="3">Takato Watabe</td></tr><tr><td>DIC (4631.T)</td><td>++</td><td>¥4,520</td></tr><tr><td>Gunze (3002.T)</td><td>E (06/25/2025)</td><td>¥3,970</td></tr><tr><td>Teijin (3401.T)</td><td>U (10/03/2022)</td><td>¥1,655</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.
\* Historical prices are not split adjusted.

© 2026 MS MUFG
"""
