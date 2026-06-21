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
## Pharmaceutical Sector Weekly

June 15-19: Sector likely to remain weak, but look for share prices to rise in 2H 2026

The pharmaceutical sector rose 0.8% WoW in the week of June 15-19, underperforming TOPIX (+4.2%). Monetary policy events happened in both Japan and the US during the week, but the Nikkei Stock Average closed at an all-time high on June 19 after the market shifted to a risk-on attitude as the Middle East outlook improved. However, buying was still concentrated in AI and semiconductor stocks, with the pharmaceutical sector lagging notably. Within the sector, Sumitomo Pharma and Kyowa Kirin outperformed TOPIX. In particular, Kyowa Kirin was the sector's best performer over the past month. Despite the uncertain medium- to long-term outlook after rocatinlimab development was halted, we believe the bad news has run its course in the near term, and this might be having a positive impact. For Kyowa Kirin, our focus is on Phase 2 study results for KHK4951 (wet age-related macular degeneration, diabetic macular edema). We think data might be presented at an academic conference in October, and thus will look to confirm this at 2Q (April-June) results. We expect the overall pharmaceutical sector to remain weak for some time, but will look for April-June results and the catalysts and events expected in 2H 2026 (Figures 7-10) to cause share prices to rise.

- Nippon Shinyaku: There was an update on June 17 regarding the lawsuit filed by Capricor Therapeutics against Nippon Shinyaku concerning deramiocel. See our report here.  
- Chugai Pharmaceutical: Chugai hosted a briefing on Elevidys, Japan's first gene therapy for Duchenne muscular dystrophy (DMD), on June 17 at 13:00. See our report here.  
- FUJIFILM Holdings: CEO Goto hosted a dinner meeting with sell-side analysts on June 18. See our report here.  
- Sumitomo Pharma: The company presented the latest data on nuvisertib and enzomenib on June 16 at the European Hematology Association (EHA) 2026 Congress. See its press release here.  
- Chugai Pharmaceutical: Chugai announced on June 19 that it had filed for domestic manufacturing and marketing approval for sparsentan (IgA nephropathy). See its press release here.  
- Santen Pharmaceutical: Santen announced on June 19 that it had obtained manufacturing and marketing approval in Japan for Rhopressa ophthalmic solution $0.02\%$ for glaucoma and ocular hypertension. See its press release here.  
- Sumitomo Pharma: The company announced on June 19 that co-promotor Novo Nordisk Pharma had received approval for Wegovy subcutaneous injection for metabolic dysfunction-associated steatohepatitis (MASH). See its press release here.

Japan Equity Research

Biotechnology & Pharmaceuticals/Medical Technologies & Services

Seiji Wakao, Ph.D. AC

(81-3) 6736-8612

seiji.wakao@JPM.com

Yugo R. Kamimura, Ph.D.

(81-3) 6736-8635

yugo.kamimura@JPM.com

Naoko Saito

(81-3) 6736-8693

naoko.saito@JPM.com

JPM Securities Japan Co., Ltd.

Figure 1: Domestic Pharmaceutical Sector Share Price Performance

<table><tr><td colspan="2">1 week</td></tr><tr><td>Sumitomo Pharma</td><td>6.9%</td></tr><tr><td>Kyowa Kirin</td><td>5.7%</td></tr><tr><td>TOPIX</td><td>4.2%</td></tr><tr><td>Eisai</td><td>3.2%</td></tr><tr><td>Otsuka Holdings</td><td>3.1%</td></tr><tr><td>JCR Pharmaceuticals</td><td>1.8%</td></tr><tr><td>Ono Pharmaceutical</td><td>1.6%</td></tr><tr><td>Daiichi Sankyo</td><td>1.6%</td></tr><tr><td>Chugai Pharmaceutical</td><td>1.3%</td></tr><tr><td>Pharmaceutical Sector</td><td>0.8%</td></tr><tr><td>Nippon Shinyaku</td><td>0.7%</td></tr><tr><td>Astellas Pharma</td><td>0.3%</td></tr><tr><td>Shionogi &amp; Co.</td><td>0.2%</td></tr><tr><td>Santen Pharmaceutical</td><td>-2.6%</td></tr><tr><td>Takeda Pharmaceutical</td><td>-2.9%</td></tr></table>

<table><tr><td colspan="2">1 month</td></tr><tr><td>Kyowa Kirin</td><td>6.5%</td></tr><tr><td>TOPIX</td><td>5.0%</td></tr><tr><td>Santen Pharmaceutical</td><td>-1.0%</td></tr><tr><td>Daiichi Sankyo</td><td>-3.6%</td></tr><tr><td>Chugai Pharmaceutical</td><td>-4.9%</td></tr><tr><td>Otsuka Holdings</td><td>-5.5%</td></tr><tr><td>Pharmaceutical Sector</td><td>-5.6%</td></tr><tr><td>Sumitomo Pharma</td><td>-5.6%</td></tr><tr><td>Takeda Pharmaceutical</td><td>-6.1%</td></tr><tr><td>Nippon Shinyaku</td><td>-6.3%</td></tr><tr><td>Ono Pharmaceutical</td><td>-7.3%</td></tr><tr><td>Astellas Pharma</td><td>-7.4%</td></tr><tr><td>Shionogi &amp; Co.</td><td>-8.2%</td></tr><tr><td>JCR Pharmaceuticals</td><td>-8.8%</td></tr><tr><td>Eisai</td><td>-12.6%</td></tr></table>

<table><tr><td colspan="2">3 months</td></tr><tr><td>TOPIX</td><td>12.1%</td></tr><tr><td>Santen Pharmaceutical</td><td>11.1%</td></tr><tr><td>Kyowa Kirin</td><td>8.1%</td></tr><tr><td>Otsuka Holdings</td><td>-1.9%</td></tr><tr><td>Ono Pharmaceutical</td><td>-4.3%</td></tr><tr><td>Astellas Pharma</td><td>-9.9%</td></tr><tr><td>Pharmaceutical Sector</td><td>-11.1%</td></tr><tr><td>Daiichi Sankyo</td><td>-12.5%</td></tr><tr><td>Chugai Pharmaceutical</td><td>-12.7%</td></tr><tr><td>Takeda Pharmaceutical</td><td>-14.5%</td></tr><tr><td>Shionogi &amp; Co.</td><td>-17.4%</td></tr><tr><td>Eisai</td><td>-18.1%</td></tr><tr><td>Sumitomo Pharma</td><td>-20.8%</td></tr><tr><td>Nippon Shinyaku</td><td>-20.8%</td></tr><tr><td>JCR Pharmaceuticals</td><td>-23.5%</td></tr></table>

<table><tr><td colspan="2">6 months</td></tr><tr><td>TOPIX</td><td>19.5%</td></tr><tr><td>Santen Pharmaceutical</td><td>14.4%</td></tr><tr><td>Otsuka Holdings</td><td>14.0%</td></tr><tr><td>Takeda Pharmaceutical</td><td>7.2%</td></tr><tr><td>Ono Pharmaceutical</td><td>3.6%</td></tr><tr><td>Shionogi &amp; Co.</td><td>2.4%</td></tr><tr><td>Astellas Pharma</td><td>2.2%</td></tr><tr><td>Kyowa Kirin</td><td>0.1%</td></tr><tr><td>Pharmaceutical Sector</td><td>-4.2%</td></tr><tr><td>Chugai Pharmaceutical</td><td>-8.9%</td></tr><tr><td>Eisai</td><td>-13.4%</td></tr><tr><td>Daiichi Sankyo</td><td>-23.0%</td></tr><tr><td>Nippon Shinyaku</td><td>-33.7%</td></tr><tr><td>Sumitomo Pharma</td><td>-35.9%</td></tr><tr><td>JCR Pharmaceuticals</td><td>-36.6%</td></tr></table>

<table><tr><td colspan="2">YTD</td></tr><tr><td>TOPIX</td><td>18.7%</td></tr><tr><td>Otsuka Holdings</td><td>18.5%</td></tr><tr><td>Santen Pharmaceutical</td><td>15.3%</td></tr><tr><td>Ono Pharmaceutical</td><td>3.5%</td></tr><tr><td>Astellas Pharma</td><td>2.5%</td></tr><tr><td>Takeda Pharmaceutical</td><td>2.0%</td></tr><tr><td>Kyowa Kirin</td><td>0.4%</td></tr><tr><td>Shionogi &amp; Co.</td><td>-2.1%</td></tr><tr><td>Pharmaceutical Sector</td><td>-4.9%</td></tr><tr><td>Chugai Pharmaceutical</td><td>-8.4%</td></tr><tr><td>Eisai</td><td>-16.3%</td></tr><tr><td>Daiichi Sankyo</td><td>-24.1%</td></tr><tr><td>Nippon Shinyaku</td><td>-29.7%</td></tr><tr><td>JCR Pharmaceuticals</td><td>-35.8%</td></tr><tr><td>Sumitomo Pharma</td><td>-36.6%</td></tr></table>

Note: Share price as of 2026/06/19  
Source: Bloomberg Finance L.P., JPM

Figure 2: Domestic Share Price Performance by Sector

<table><tr><td colspan="2">1 week</td></tr><tr><td>Nonferrous Metals</td><td>19.1%</td></tr><tr><td>Electric Appliances</td><td>11.0%</td></tr><tr><td>Glass &amp; Ceramics Products</td><td>9.0%</td></tr><tr><td>Machinery</td><td>7.8%</td></tr><tr><td>Metal Products</td><td>7.2%</td></tr><tr><td>Construction</td><td>5.9%</td></tr><tr><td>Air Transportation</td><td>5.0%</td></tr><tr><td>TOPIX</td><td>4.2%</td></tr><tr><td>Chemicals</td><td>3.4%</td></tr><tr><td>Rubber Products</td><td>3.3%</td></tr><tr><td>Precision Instruments</td><td>2.8%</td></tr><tr><td>Information &amp; Communication</td><td>2.4%</td></tr><tr><td>Other Financing Business</td><td>2.1%</td></tr><tr><td>Banks</td><td>2.1%</td></tr><tr><td>Securities &amp; Commodity</td><td>2.0%</td></tr><tr><td>Iron &amp; Steel</td><td>2.0%</td></tr><tr><td>Foods</td><td>1.5%</td></tr><tr><td>Pulp &amp; Paper</td><td>1.3%</td></tr><tr><td>Transportation Equipment</td><td>1.1%</td></tr><tr><td>Oil &amp; Coal Products</td><td>1.1%</td></tr><tr><td>Textiles &amp; Apparels</td><td>0.9%</td></tr><tr><td>Pharmaceutical</td><td>0.8%</td></tr><tr><td>Insurance</td><td>0.4%</td></tr><tr><td>Services</td><td>-0.1%</td></tr><tr><td>Warehouse &amp; Harbor Transp.</td><td>-0.3%</td></tr><tr><td>Other Products</td><td>-0.3%</td></tr><tr><td>Retail Trade</td><td>-0.9%</td></tr><tr><td>Electric Power &amp; Gas</td><td>-1.0%</td></tr><tr><td>Wholesale Trade</td><td>-1.1%</td></tr><tr><td>Land Transportation</td><td>-1.2%</td></tr><tr><td>Mining</td><td>-1.3%</td></tr><tr><td>Real Estate</td><td>-1.5%</td></tr><tr><td>Fishery Agric. &amp; Forestry</td><td>-1.6%</td></tr><tr><td>MedTech</td><td>-1.7%</td></tr><tr><td>Marine Transportation</td><td>-7.8%</td></tr></table>

<table><tr><td colspan="2">1 month</td></tr><tr><td>Electric Appliances</td><td>20.8%</td></tr><tr><td>Glass &amp; Ceramics Products</td><td>16.3%</td></tr><tr><td>Metal Products</td><td>15.4%</td></tr><tr><td>Nonferrous Metals</td><td>11.6%</td></tr><tr><td>Air Transportation</td><td>8.1%</td></tr><tr><td>Banks</td><td>6.9%</td></tr><tr><td>Machinery</td><td>6.3%</td></tr><tr><td>Rubber Products</td><td>6.1%</td></tr><tr><td>Chemicals</td><td>5.5%</td></tr><tr><td>Other Financing Business</td><td>5.4%</td></tr><tr><td>TOPIX</td><td>5.0%</td></tr><tr><td>Information &amp; Communication</td><td>5.0%</td></tr><tr><td>Services</td><td>4.5%</td></tr><tr><td>Securities &amp; Commodity</td><td>4.3%</td></tr><tr><td>Iron &amp; Steel</td><td>2.2%</td></tr><tr><td>Textiles &amp; Apparels</td><td>1.8%</td></tr><tr><td>Retail Trade</td><td>1.5%</td></tr><tr><td>Precision Instruments</td><td>1.5%</td></tr><tr><td>Construction</td><td>0.6%</td></tr><tr><td>Foods</td><td>-0.2%</td></tr><tr><td>Pulp &amp; Paper</td><td>-1.4%</td></tr><tr><td>Insurance</td><td>-1.8%</td></tr><tr><td>Real Estate</td><td>-2.3%</td></tr><tr><td>Transportation Equipment</td><td>-2.3%</td></tr><tr><td>Warehouse &amp; Harbor Transp.</td><td>-2.8%</td></tr><tr><td>Other Products</td><td>-3.5%</td></tr><tr><td>Electric Power &amp; Gas</td><td>-4.5%</td></tr><tr><td>MedTech</td><td>-4.8%</td></tr><tr><td>Fishery Agric. &amp; Forestry</td><td>-5.0%</td></tr><tr><td>Pharmaceutical</td><td>-5.6%</td></tr><tr><td>Land Transportation</td><td>-5.7%</td></tr><tr><td>Oil &amp; Coal Products</td><td>-6.7%</td></tr><tr><td>Marine Transportation</td><td>-8.0%</td></tr><tr><td>Mining</td><td>-11.9%</td></tr><tr><td>Wholesale Trade</td><td>-12.3%</td></tr></table>

<table><tr><td colspan="2">3 months</td></tr><tr><td>Electric Appliances</td><td>44.0%</td></tr><tr><td>Glass &amp; Ceramics Products</td><td>38.7%</td></tr><tr><td>Metal Products</td><td>31.7%</td></tr><tr><td>Nonferrous Metals</td><td>28.0%</td></tr><tr><td>Services</td><td>24.4%</td></tr><tr><td>Banks</td><td>22.2%</td></tr><tr><td>Information &amp; Communication</td><td>18.9%</td></tr><tr><td>Other Financing Business</td><td>17.3%</td></tr><tr><td>Insurance</td><td>17.0%</td></tr><tr><td>Chemicals</td><td>14.5%</td></tr><tr><td>TOPIX</td><td>12.1%</td></tr><tr><td>Rubber Products</td><td>8.8%</td></tr><tr><td>MedTech</td><td>8.6%</td></tr><tr><td>Securities &amp; Commodity</td><td>6.4%</td></tr><tr><td>Precision Instruments</td><td>6.0%</td></tr><tr><td>Foods</td><td>5.8%</td></tr><tr><td>Machinery</td><td>4.6%</td></tr><tr><td>Air Transportation</td><td>4.2%</td></tr><tr><td>Textiles &amp; Apparels</td><td>2.9%</td></tr><tr><td>Retail Trade</td><td>0.7%</td></tr><tr><td>Pulp &amp; Paper</td><td>-1.8%</td></tr><tr><td>Iron &amp; Steel</td><td>-4.0%</td></tr><tr><td>Construction</td><td>-5.0%</td></tr><tr><td>Warehouse &amp; Harbor Transp.</td><td>-5.4%</td></tr><tr><td>Land Transportation</td><td>-6.6%</td></tr><tr><td>Transportation Equipment</td><td>-8.9%</td></tr><tr><td>Fishery Agric. &amp; Forestry</td><td>-9.5%</td></tr><tr><td>Electric Power &amp; Gas</td><td>-9.9%</td></tr><tr><td>Oil &amp; Coal Products</td><td>-10.0%</td></tr><tr><td>Wholesale Trade</td><td>-10.7%</td></tr><tr><td>Pharmaceutical</td><td>-11.1%</td></tr><tr><td>Real Estate</td><td>-13.6%</td></tr><tr><td>Other Products</td><td>-15.1%</td></tr><tr><td>Marine Transportation</td><td>-18.5%</td></tr><tr><td>Mining</td><td>-26.0%</td></tr></table>

<table><tr><td colspan="2">6 months</td></tr><tr><td>Nonferrous Metals</td><td>110.3%</td></tr><tr><td>Glass &amp; Ceramics Products</td><td>60.5%</td></tr><tr><td>Electric Appliances</td><td>52.0%</td></tr><tr><td>Banks</td><td>34.4%</td></tr><tr><td>Metal Products</td><td>32.8%</td></tr><tr><td>Machinery</td><td>27.2%</td></tr><tr><td>Chemicals</td><td>26.8%</td></tr><tr><td>Other Financing Business</td><td>23.4%</td></tr><tr><td>Insurance</td><td>22.4%</td></tr><tr><td>TOPIX</td><td>19.5%</td></tr><tr><td>Oil &amp; Coal Products</td><td>12.0%</td></tr><tr><td>Precision Instruments</td><td>11.8%</td></tr><tr><td>Marine Transportation</td><td>11.7%</td></tr><tr><td>Foods</td><td>11.1%</td></tr><tr><td>Mining</td><td>11.1%</td></tr><tr><td>Wholesale Trade</td><td>10.4%</td></tr><tr><td>Textiles &amp; Apparels</td><td>8.9%</td></tr><tr><td>Services</td><td>7.1%</td></tr><tr><td>Information &amp; Communication</td><td>6.6%</td></tr><tr><td>Securities &amp; Commodity</td><td>5.9%</td></tr><tr><td>Warehouse &amp; Harbor Transp.</td><td>4.1%</td></tr><tr><td>Pulp &amp; Paper</td><td>3.5%</td></tr><tr><td>Construction</td><td>2.0%</td></tr><tr><td>Fishery Agric. &amp; Forestry</td><td>0.5%</td></tr><tr><td>Rubber Products</td><td>-1.1%</td></tr><tr><td>Electric Power &amp; Gas</td><td>-1.3%</td></tr><tr><td>Retail Trade</td><td>-1.5%</td></tr><tr><td>Iron &amp; Steel</td><td>-3.4%</td></tr><tr><td>MedTech</td><td>-4.2%</td></tr><tr><td>Air Transportation</td><td>-4.2%</td></tr><tr><td>Pharmaceutical</td><td>-4.2%</td></tr><tr><td>Real Estate</td><td>-4.8%</td></tr><tr><td>Land Transportation</td><td>-9.3%</td></tr><tr><td>Transportation Equipment</td><td>-13.1%</td></tr><tr><td>Other Products</td><td>-16.9%</td></tr></table>

<table><tr><td colspan="2">YTD</td></tr><tr><td>Nonferrous Metals</td><td>101.0%</td></tr><tr><td>Glass &amp; Ceramics Products</td><td>58.6%</td></tr><tr><td>Electric Appliances</td><td>48.5%</td></tr><tr><td>Banks</td><td>33.0%</td></tr><tr><td>Metal Products</td><td>30.8%</td></tr><tr><td>Chemicals</td><td>25.9%</td></tr><tr><td>Machinery</td><td>25.8%</td></tr><tr><td>Insurance</td><td>23.4%</td></tr><tr><td>Other Financing Business</td><td>22.0%</td></tr><tr><td>TOPIX</td><td>18.7%</td></tr><tr><td>Precision Instruments</td><td>12.6%</td></tr><tr><td>Foods</td><td>12.4%</td></tr><tr><td>Mining</td><td>11.2%</td></tr><tr><td>Oil &amp; Coal Products</td><td>9.8%</td></tr><tr><td>Textiles &amp; Apparels</td><td>9.5%</td></tr><tr><td>Wholesale Trade</td><td>9.0%</td></tr><tr><td>Marine Transportation</td><td>7.5%</td></tr><tr><td>Services</td><td>6.7%</td></tr><tr><td>Information &amp; Communication</td><td>6.3%</td></tr><tr><td>Warehouse &amp; Harbor Transp.</td><td>4.5%</td></tr><tr><td>Securities &amp; Commodity</td><td>3.5%</td></tr><tr><td>Construction</td><td>1.9%</td></tr><tr><td>Pulp &amp; Paper</td><td>1.6%</td></tr><tr><td>Rubber Products</td><td>1.3%</td></tr><tr><td>Fishery Agric. &amp; Forestry</td><td>1.3%</td></tr><tr><td>Retail Trade</td><td>-1.0%</td></tr><tr><td>Electric Power &amp; Gas</td><td>-1.3%</td></tr><tr><td>Air Transportation</td><td>-2.3%</td></tr><tr><td>MedTech</td><td>-2.8%</td></tr><tr><td>Real Estate</td><td>-4.8%</td></tr><tr><td>Pharmaceutical</td><td>-4.9%</td></tr><tr><td>Iron &amp; Steel</td><td>-6.9%</td></tr><tr><td>Land Transportation</td><td>-8.9%</td></tr><tr><td>Transportation Equipment</td><td>-11.9%</td></tr><tr><td>Other Products</td><td>-16.5%</td></tr></table>

Note: Share price as of 2026/06/19  
Source: Bloomberg Finance L.P., JPM

Figure 3: Japan Pharmaceutical Sector Valu

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 20 Jun 2026 01:22 AM JST

Disseminated 20 Jun 2026 01:23 AM JST
"""
