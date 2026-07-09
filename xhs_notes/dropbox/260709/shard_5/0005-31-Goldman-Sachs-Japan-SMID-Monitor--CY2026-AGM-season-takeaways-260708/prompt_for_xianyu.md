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
# Japan SMID Monitor: CY2026 AGM season takeaways

In this month's edition of the Japan SMID Monitor, we focus on the 2026 AGM season trends within Japan SMID universe versus the larger cap space. One conclusion is that Japan SMID stocks currently appear to be under slightly more shareholder pressure versus their larger cap peers. Just over $15\%$ of Japan SMIDs have CEO approval ratings below $80\%$ (Exhibit 7), compared with less than $10\%$ for companies with 6M ADTV over US\$20mn. However, in terms of overall average approval rating changes over time (Exhibit 5) and inter-quartile ranges (Exhibit 6), there appears to be very little difference between the two data-sets. Historically, CEO approval IQRs were significantly higher with Japan SMID stocks (Exhibit 6), but this difference largely disappeared in CY2026. After peaking in CY2024 at over $11\%$ (versus just $7\%$ for the more liquid universe), the SMID CEO approval IQR fell 2ppts to $9\%$ by CY2026, while the more liquid universe's CEO Approval IQR has risen 2ppts to the same $9\%$ level.

Tech Hardware, Industrials and Inbound Tourism out-performed IT Services in GS Japan coverage universe: The best-performing SMID names in June covered by GS Japan analysts included Taiyo Yuden (+37% mom), Japan Material (+25% mom), Kyoritsu Maintenance (+21% mom) and Kotobuki Spirits (+19% mom). The two worst-performers were ANYCOLOR (-22% mom), and Cover Corp (-14%).

Japan SMID thematic and sub-sector index data showed that Financials led in June while Software lagged: The best-preforming indices last month were Regional Banks (+17% mom) and Banks (+11% mom), while the worst-performers included SAAS (-13% mom) and Software (-9% mom).

GS Japan SMID team remain bullish on the Japan Shipbuilding sector: GS Japan SMID analyst Norihiro Miyazaki published a sector update on the Japan Shipbuilding sector (LINK). Japan's May 2026 order backlog was a very healthy 29.3mn GT (vessel demand for the next 3-4 years), and media reports also suggest that the US Navy may start to procure ships from US and South Korean shipyards. If confirmed, this would be a very positive catalyst for this sector in Japan.

■ Individuals net bought TSE Growth and TSE Standard, whilst foreigners net sold both: As can be seen in Exhibit 1 and Exhibit 2 below, for the month of June, individuals net bought ¥11.4bn and ¥84.3bn of Standard cash equities and Growth cash, whilst foreigners net sold -¥13.9bn and -¥63.4bn, respectively.

Bruce Kirk, CFA
+81(3)4587-9950 | bruce.kirk@gs.com
GS Japan Co., Ltd.

Julius Chan
+81(3)4587-1789 | julius.chan@gs.com
GS Japan Co., Ltd.

Exhibit 1: TSE Standard net buying 2-year chart as of Jun 26 2026, JPY bn  
![](images/a9060d64199e28ff0e77ac17592192d2214d2871ab89ff8c22269c24bbf8bf2a.jpg)  
Source: Bloomberg, Tokyo Stock Exchange

Exhibit 2: TSE Growth net buying
2-year chart as of Jun 26 2026, JPY bn  
![](images/6c08717a895b45bc7ca8ea75960646961d747a6bc10067506ee6f626dbeb8af4.jpg)  
Source: Bloomberg, Tokyo Stock Exchange

## GS Covered Japan SMID Stocks

Exhibit 3: GS covered SMID stocks ranked by monthly performance
Data as of Jun 30 2026

<table><tr><td>Ticker</td><td>Name</td><td>Analyst</td><td>1W</td><td>2W</td><td>1M</td><td>3M</td><td>6M</td><td>YTD</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>Daiki Takayama</td><td>19%</td><td>0%</td><td>36%</td><td>398%</td><td>469%</td><td>469%</td></tr><tr><td>6055</td><td>Japan Material</td><td>Takeru Adachi</td><td>1%</td><td>7%</td><td>25%</td><td>55%</td><td>66%</td><td>66%</td></tr><tr><td>9616</td><td>Kyoritsu Maintenance</td><td>Norihiro Miyazaki</td><td>5%</td><td>11%</td><td>21%</td><td>21%</td><td>8%</td><td>8%</td></tr><tr><td>2222</td><td>Kotobuki Spirits Co.</td><td>Norihiro Miyazaki</td><td>7%</td><td>9%</td><td>19%</td><td>32%</td><td>36%</td><td>36%</td></tr><tr><td>6622</td><td>Daihen</td><td>Ryo Harada</td><td>-3%</td><td>11%</td><td>14%</td><td>46%</td><td>81%</td><td>81%</td></tr><tr><td>6407</td><td>CKD</td><td>Yuichiro Isayama</td><td>-2%</td><td>0%</td><td>14%</td><td>58%</td><td>144%</td><td>144%</td></tr><tr><td>6103</td><td>Okuma</td><td>Yuichiro Isayama</td><td>4%</td><td>4%</td><td>13%</td><td>24%</td><td>27%</td><td>27%</td></tr><tr><td>6728</td><td>Ulvac</td><td>Shuhei Nakamura</td><td>4%</td><td>15%</td><td>9%</td><td>18%</td><td>46%</td><td>46%</td></tr><tr><td>4205</td><td>Zeon</td><td>Atsushi Ikeda</td><td>2%</td><td>1%</td><td>8%</td><td>31%</td><td>32%</td><td>32%</td></tr><tr><td>6254</td><td>NOM Micro Science</td><td>Takeru Adachi</td><td>-2%</td><td>7%</td><td>7%</td><td>49%</td><td>65%</td><td>65%</td></tr><tr><td>7988</td><td>Nifco Inc.</td><td>Kota Yuzawa</td><td>4%</td><td>8%</td><td>7%</td><td>7%</td><td>0%</td><td>0%</td></tr><tr><td>4912</td><td>Lion</td><td>Takashi Miyazaki</td><td>4%</td><td>2%</td><td>6%</td><td>0%</td><td>4%</td><td>4%</td></tr><tr><td>7721</td><td>Tokyo Keiki</td><td>Norihiro Miyazaki</td><td>0%</td><td>18%</td><td>5%</td><td>-5%</td><td>16%</td><td>16%</td></tr><tr><td>6951</td><td>JEOL</td><td>Shuhei Nakamura</td><td>7%</td><td>12%</td><td>5%</td><td>22%</td><td>48%</td><td>48%</td></tr><tr><td>9706</td><td>Japan Airport Terminal</td><td>Norihiro Miyazaki</td><td>7%</td><td>5%</td><td>4%</td><td>-7%</td><td>15%</td><td>15%</td></tr><tr><td>6432</td><td>Takeuchi MFG</td><td>Takeru Adachi</td><td>-4%</td><td>-4%</td><td>4%</td><td>9%</td><td>5%</td><td>5%</td></tr><tr><td>3774</td><td>Internet Initiative Japan</td><td>Chikai Tanaka, CFA</td><td>5%</td><td>8%</td><td>3%</td><td>28%</td><td>16%</td><td>16%</td></tr><tr><td>4202</td><td>Daicel</td><td>Atsushi Ikeda</td><td>6%</td><td>3%</td><td>3%</td><td>9%</td><td>-2%</td><td>-2%</td></tr><tr><td>2229</td><td>Calbee Inc</td><td>Takashi Miyazaki</td><td>5%</td><td>5%</td><td>2%</td><td>-5%</td><td>-1%</td><td>-1%</td></tr><tr><td>8304</td><td>Aozora Bank</td><td>Makoto Kuroda</td><td>-1%</td><td>-1%</td><td>2%</td><td>3%</td><td>8%</td><td>8%</td></tr><tr><td>7581</td><td>Saizeriya</td><td>Sho Kawano</td><td>4%</td><td>3%</td><td>1%</td><td>-18%</td><td>-1%</td><td>-1%</td></tr><tr><td>4483</td><td>JMDC</td><td>Akinori Ueda, Ph.D.</td><td>6%</td><td>4%</td><td>1%</td><td>-16%</td><td>-28%</td><td>-28%</td></tr><tr><td>6592</td><td>Mabuchi Motor</td><td>Daiki Takayama</td><td>-1%</td><td>-1%</td><td>1%</td><td>-3%</td><td>9%</td><td>9%</td></tr><tr><td>3994</td><td>Money Forward</td><td>Chikai Tanaka, CFA</td><td>8%</td><td>13%</td><td>1%</td><td>21%</td><td>-6%</td><td>-6%</td></tr><tr><td>6324</td><td>Harmonic Drive Systems</td><td>Yuichiro Isayama</td><td>1%</td><td>11%</td><td>0%</td><td>113%</td><td>106%</td><td>106%</td></tr><tr><td>4194</td><td>Visional</td><td>Norihiro Miyazaki</td><td>9%</td><td>8%</td><td>-1%</td><td>6%</td><td>-22%</td><td>-22%</td></tr><tr><td>6674</td><td>GS Yuasa Corp.</td><td>Kota Yuzawa</td><td>-9%</td><td>-2%</td><td>-1%</td><td>14%</td><td>72%</td><td>72%</td></tr><tr><td>8570</td><td>Aeon Financial Service Co.</td><td>Makoto Kuroda</td><td>2%</td><td>-2%</td><td>-3%</td><td>-8%</td><td>-16%</td><td>-16%</td></tr><tr><td>6508</td><td>Meidensha</td><td>Ryo Harada</td><td>-6%</td><td>4%</td><td>-3%</td><td>20%</td><td>75%</td><td>75%</td></tr><tr><td>4061</td><td>Denka</td><td>Atsushi Ikeda</td><td>-1%</td><td>3%</td><td>-3%</td><td>15%</td><td>58%</td><td>58%</td></tr><tr><td>6754</td><td>Anritsu</td><td>Ryo Harada</td><td>-2%</td><td>7%</td><td>-3%</td><td>47%</td><td>96%</td><td>96%</td></tr><tr><td>4587</td><td>PeptiDream</td><td>Akinori Ueda, Ph.D.</td><td>9%</td><td>13%</td><td>-4%</td><td>-15%</td><td>-36%</td><td>-36%</td></tr><tr><td>3697</td><td>SHIFT</td><td>Chikai Tanaka, CFA</td><td>10%</td><td>6%</td><td>-4%</td><td>-1%</td><td>-31%</td><td>-31%</td></tr><tr><td>7383</td><td>Net Protections Holdings</td><td>Makoto Kuroda</td><td>-1%</td><td>-1%</td><td>-4%</td><td>-12%</td><td>-35%</td><td>-35%</td></tr><tr><td>7014</td><td>Namura Shipbuilding Co.</td><td>Norihiro Miyazaki</td><td>-4%</td><td>-6%</td><td>-5%</td><td>-20%</td><td>0%</td><td>0%</td></tr><tr><td>4478</td><td>freee K.K.</td><td>Chikai Tanaka, CFA</td><td>7%</td><td>5%</td><td>-5%</td><td>-4%</td><td>-34%</td><td>-34%</td></tr><tr><td>6770</td><td>Alps Alpine</td><td>Daiki Takayama</td><td>-4%</td><td>-3%</td><td>-6%</td><td>-8%</td><td>3%</td><td>3%</td></tr><tr><td>3923</td><td>Rakus Co.</td><td>Norihiro Miyazaki</td><td>7%</td><td>6%</td><td>-6%</td><td>21%</td><td>-9%</td><td>-9%</td></tr><tr><td>6966</td><td>Mitsui High-tec Inc.</td><td>Kota Yuzawa</td><td>-12%</td><td>-14%</td><td>-7%</td><td>57%</td><td>25%</td><td>25%</td></tr><tr><td>3116</td><td>Toyota Boshoku</td><td>Kota Yuzawa</td><td>0%</td><td>-5%</td><td>-7%</td><td>-14%</td><td>-15%</td><td>-15%</td></tr><tr><td>4443</td><td>Sansan Inc.</td><td>Norihiro Miyazaki</td><td>8%</td><td>6%</td><td>-8%</td><td>30%</td><td>-10%</td><td>-10%</td></tr><tr><td>4369</td><td>Tri Chemical Laboratories Inc</td><td>Atsushi Ikeda</td><td>-5%</td><td>-7%</td><td>-8%</td><td>25%</td><td>29%</td><td>29%</td></tr><tr><td>5805</td><td>SWCC</td><td>Ryo Harada</td><td>-6%</td><td>-2%</td><td>-9%</td><td>5%</td><td>30%</td><td>30%</td></tr><tr><td>4922</td><td>Kose Holdings</td><td>Takashi Miyazaki</td><td>0%</td><td>-3%</td><td>-10%</td><td>-17%</td><td>-4%</td><td>-4%</td></tr><tr><td>5253</td><td>Cover Corp.</td><td>Norihiro Miyazaki</td><td>14%</td><td>-3%</td><td>-14%</td><td>-1%</td><td>-9%</td><td>-9%</td></tr><tr><td>5032</td><td>ANYCOLOR</td><td>Norihiro Miyazaki</td><td>10%</td><td>-3%</td><td>-22%</td><td>-25%</td><td>-54%</td><td>-54%</td></tr></table>

Exhibit 4: GS covered SMID stocks by analyst, 1M performance and consensus valuations
Data as of Jun 30 2026

<table><tr><td>Ticker</td><td>Name</td><td>Analyst</td><td>1M price return</td><td>P/B</td><td>P/E NTM</td><td>ROE FY26E</td><td>DY FY26E</td></tr><tr><td>4483</td><td>JMDC</td><td>Akinori Ueda, Ph.D.</td><td>1%</td><td>2.3</td><td>21.9</td><td>8.6</td><td>0.7</td></tr><tr><td>4587</td><td>PeptiDream</td><td>Akinori Ueda, Ph.D.</td><td>-4%</td><td>2.7</td><td>9.0</td><td>30.4</td><td>0.0</td></tr><tr><td>4205</td><td>Zeon</td><td>Atsushi Ikeda</td><td>8%</td><td>1.2</td><td>13.3</td><td>9.5</td><td>3.3</td></tr><tr><td>4202</td><td>Daicel</td><td>Atsushi Ikeda</td><td>3%</td><td>1.0</td><td>9.9</td><td>8.7</td><td>4.9</td></tr><tr><td>4061</td><td>Denka</td><td>Atsushi Ikeda</td><td>-3%</td><td>1.2</td><td>19.6</td><td>6.9</td><td>2.3</td></tr><tr><td>4369</td><td>Tri Chemical Laboratories Inc.</td><td>Atsushi Ikeda</td><td>-8%</td><td>3.1</td><td>20.0</td><td>14.4</td><td>1.1</td></tr><tr><td>3774</td><td>Internet Initiative Japan</td><td>Chikai Tanaka, CFA</td><td>3%</td><td>3.6</td><td>20.5</td><td>16.3</td><td>1.4</td></tr><tr><td>3994</td><td>Money Forward</td><td>Chikai Tanaka, CFA</td><td>1%</td><td>5.8</td><td>102.2</td><td>2.7</td><td>0.0</td></tr><tr><td>3697</td><td>SHIFT</td><td>Chikai Tanaka, CFA</td><td>-4%</td><td>4.5</td><td>12.6</td><td>21.7</td><td>0.0</td></tr><tr><td>4478</td><td>freee K.K.</td><td>Chikai Tanaka, CFA</td><td>-5%</td><td>5.8</td><td>34.9</td><td>4.0</td><td>0.0</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>Daiki Takayama</td><td>36%</td><td>7.3</td><td>80.7</td><td>7.7</td><td>0.5</td></tr><tr><td>6592</td><td>Mabuchi Motor</td><td>Daiki Takayama</td><td>1%</td><td>1.1</td><td>17.9</td><td>6.2</td><td>3.2</td></tr><tr><td>6770</td><td>Alps Alpine</td><td>Daiki Takayama</td><td>-6%</td><td>0.9</td><td>13.5</td><td>6.3</td><td>3.2</td></tr><tr><td>7988</td><td>Nifco Inc.</td><td>Kota Yuzawa</td><td>7%</td><td>1.5</td><td>11.7</td><td>12.1</td><td>2.5</td></tr><tr><td>6674</td><td>GS Yuasa Corp.</td><td>Kota Yuzawa</td><td>-1%</td><td>1.6</td><td>15.6</td><td>10.0</td><td>1.6</td></tr><tr><td>6966</td><td>Mitsui High-tec Inc.</td><td>Kota Yuzawa</td><td>-7%</td><td>1.5</td><td>16.2</td><td>10.0</td><td>2.0</td></tr><tr><td>3116</td><td>Toyota Boshoku</td><td>Kota Yuzawa</td><td>-7%</td><td>0.8</td><td>7.8</td><td>9.6</td><td>4.1</td></tr><tr><td>8304</td><td>Aozora Bank</td><td>Makoto Kuroda</td><td>2%</td><td>0.8</td><td>13.1</td><td>5.7</td><td>3.7</td></tr><tr><td>8570</td><td>Aeon Financial Service Co.</td><td>Makoto Kuroda</td><td>-3%</td><td>0.7</td><td>14.1</td><td>4.3</td><td>3.6</td></tr><tr><td>7383</td><td>Net Protections Holdings</td><td>Makoto Kuroda</td><td>-4%</td><td>1.6</td><td>14.8</td><td>9.9</td><td>0.0</td></tr><tr><td>9616</td><td>Kyoritsu Maintenance</td><td>Norihiro Miyazaki</td><td>21%</td><td>1.9</td><td>14.5</td><td>13.2</td><td>1.5</td></tr><tr><td>2222</td><td>Kotobuki Spirits Co.</td><td>Norihiro Miyazaki</td><td>19%</td><td>8.0</td><td>25.8</td><td>27.1</td><td>1.5</td></tr><tr><td>7721</td><td>Tokyo Keiki</td><td>Norihiro Miyazaki</td><td>5%</td><td>2.2</td><td>20.0</td><td>10.7</td><td>0.8</td></tr><tr><td>9706</td><td>Japan Airport Terminal</td><td>Norihiro Miyazaki</td><td>4%</td><td>2.2</td><td>18.1</td><td>11.9</td><td>1.9</td></tr><tr><td>4194</td><td>Visional</td><td>Norihiro Miyazaki</td><td>-1%</td><td>3.8</td><td>16.0</td><td>22.9</td><td>0.0</td></tr><tr><td>7014</td><td>Namura Shipbuilding Co.</td><td>Norihiro Miyazaki</td><td>-5%</td><td>1.8</td><td>10.3</td><td>16.2</td><td>1.7</td></tr><tr><td>3923</td><td>Rakus Co.</td><td>Norihiro Miyazaki</td><td>-6%</td><td>12.9</td><td>16.7</td><td>72.4</td><td>0.7</td></tr><tr><td>4443</td><td>Sansan Inc.</td><td>Norihiro Miyazaki</td><td>-8%</td><td>10.9</td><td>21.2</td><td>37.1</td><td>0.1</td></tr><tr><td>5253</td><td>Cover Corp.</td><td>Norihiro Miyazaki</td><td>-14%</td><td>4.5</td><td>12.7</td><td>31.2</td><td>0.0</td></tr><tr><td>5032</td><td>ANYCOLOR</td><td>Norihiro Miyazaki</td><td>-22%</td><td>5.0</td><td>8.2</td><td>51.1</td><td>3.7</td></tr><tr><td>6622</td><td>Daihen</td><td>Ryo Harada</td><td>14%</td><td>2.8</td><td>23.3</td><td>10.9</td><td>1.3</td></tr><tr><td>6508</td><td>Meidensha</td><td>Ryo Harada</td><td>-3%</td><td>2.5</td><td>20.1</td><td>12.1</td><td>1.6</td></tr><tr><td>6754</td><td>Anritsu</td><td>Ryo Harada</td><td>-3%</td><td>4.2</td><td>36.0</td><td>10.9</td><td>1.2</td></tr><tr><td>5805</td><td>SWCC</td><td>Ryo Harada</td><td>-9%</td><td>4.1</td><td>18.8</td><td>19.4</td><td>2.0</td></tr><tr><td>7581</td><td>Saizeriya</td><td>Sho Kawano</td><td>1%</td><td>2.1</td><td>18.8</td><td>10.3</td><td>0.6</td></tr><tr><td>6728</td><td>Ulvac</td><td>Shuhei Nakamura</td><td>9%</td><td>2.2</td><td>21.1</td><td>8.7</td><td>1.6</td></tr><tr><td>6951</td><td>JEOL</td><td>Shuhei Nakamura</td><td>5%</td><td>2.5</td><td>16.4</td><td>14.6</td><td>1.7</td></tr><tr><td>4912</td><td>Lion</td><td>Takashi Miyazaki</td><td>6%</td><td>1.5</td><td>18.3</td><td>7.8</td><td>2.0</td></tr><tr><td>2229</td><td>Calbee Inc</td><td>Takashi Miyazaki</td><td>2%</td><td>1.7</td><td>19.6</td><td>8.9</td><td>2.3</td></tr><tr><td>4922</td><td>Kose Holdings</td><td>Takashi Miyazaki</td><td>-10%</td><td>1.0</td><td>22.8</td><td>4.0</td><td>3.0</td></tr><tr><td>6055</td><td>Japan Material</td><td>Takeru Adachi</td><td>25%</td><td>4.2</td><td>22.8</td><td>17.3</td><td>1.2</td></tr><tr><td>6254</td><td>NOM Micro Science</td><td>Takeru Adachi</td><td>7%</td><td>4.8</td><td>19.7</td><td>25.2</td><td>1.6</td></tr><tr><td>6432</td><td>Takeuchi MFG</td><td>Takeru Adachi</td><td>4%</td><td>1.7</td><td>12.2</td><td>12.9</td><td>3.1</td></tr><tr><td>6407</td><td>CKD</td><td>Yuichiro Isayama</td><td>14%</td><td>3.3</td><td>26.0</td><td>11.5</td><td>1.4</td></tr><tr><td>6103</td><td>Okuma</td><td>Yuichiro Isayama</td><td>13%</td><td>1.1</td><td>17.2</td><td>6.3</td><td>2.2</td></tr><tr><td>6324</td><td>Harmonic Drive Systems</td><td>Yuichiro Isayama</td><td>0%</td><td>9.2</td><td>114.3</td><td>6.6</td><td>0.3</td></tr></table>

## CY2026 AGM CEO approval ratings in SMID space

Exhibit 5: Median / mean CEO a

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
