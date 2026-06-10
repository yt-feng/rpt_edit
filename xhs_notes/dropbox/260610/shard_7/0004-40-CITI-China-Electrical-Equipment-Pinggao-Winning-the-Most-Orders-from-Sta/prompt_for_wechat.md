你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Citi`。标题格式建议：`# Citi：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Electrical Equipment

Pinggao Winning the Most Orders from State Grid 2nd Batch of Equipment Purchase for Building UHV Lines in 2026

## CITI'S TAKE

State Grid (link) announced the bidding results of its 2nd batch of equipment procurement for construction of ultra-high voltage ('UHV') lines total Rmb9.4bn today. These bidding results are important since the amount of Rmb9.4bn was more than double of Rmb4bn in the 1st batch in 2026 and equal to 42.6% of total Rmb22.1bn in the five batches of 2025. The biggest winners this time were (i) Pinggao (600312 CH, BUY) winning Rmb2.092bn or 22.3% of the new orders; (ii) China XD Electric (601179 CH, not covered) winning Rmb1.899bn or 20.2%; (iii) TBEA (600089 CH, BUY) winning Rmb473m or 5.0%; (iv) Sieyuan Electric (002028 CH, BUY) winning Rmb196m or 2,1%; and (iv) NARI (600406 CH, BUY) winning Rmb144m or 1.5%. In PRC power grid equipment sector, our top picks are Sieyuan for fast export growth (>80% yoy), Pinggao for getting the most PRC UHV orders and TBEA for inexpensive valuations.

Total 79 entities winning contracts this time – In term of products in this batch total Rmb9.4bn, these comprised (i) Rmb5.4bn or 57.4% for 1,000kV gas insulated switch-gears ('GIS'), (ii) Rmb1.184m or 12.6% for raw materials; and (iii) Rmb655m or 7.0% for 1,000kV reactors. 79 companies won contracts this round, equal to an average Rmb119m per company. The three biggest winners were (i) Henan Pinggao Electric Co Ltd winning Rmb1.94bn or 20.6% total orders; (ii) Xian Xidian Switchgear Electric Co Ltd (unlisted) owned by China XD Electric winning Rmb1.45bn or 15.4% total orders and (iii) Shandong Electric Hitachi High-Voltage Switch-gear Co Ltd (not listed) winning Rmb1.41bn or 15.0% total orders.

Fast growing PRC power grid capex so far this year – PRC power grid capex surged 40% yoy to Rmb167.5bn in 1Q26; the capex comprises three categories; namely, civil works, equipment procurement and others (such as project design works). NARI explained that the biggest part of PRC power grid capex increment in 1Q26 came from civil works as PRC government was keen on having PRC FAI resuming positive numbers. The goal was achieved and PRC FAI improved from -3.9% yoy in 2025 to +1.7% yoy in 1Q26. Spending in civil works could boost the FAI faster than from other aspects as the former is often incurred at earlier stages. NARI expects the fast growth trend to persist in 2Q26E.

Pinggao expecting more UHV line equipment tendering in 2026E — Pinggao's new orders were +12% yoy to Rmb13.9bn in 2025. It expects more equipment tendering for construction of UHV lines in 2026E, comprising 3 AC projects (namely Dalate-Mengxi, Panzhihua-Xichang, and Zhejiang Ring Network) approved in 2025 and pending equipment tendering ahead as well as possibly at least another 2 AC projects to be approved in 2026E, up from only 3 in 2025. Tendering value of the first batch of State Grid's power grid equipment announced on 31 March 2026 were Rmb9,834m,

Pierre Lau, CFA $^{AC}$

+852-2501-2716

pierre.lau@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

comprising Rmb647m won by Pinggao which ranked No. 2 among all companies participating in the biddings. Pinggao guided that the tendering prices might be higher from the second batch ahead to reflect increased copper prices.

Pinggao's rising delivery of high voltage switchgears in 2026E — Pinggao's gas insulated switchgears (GIS) delivery should rise to 15 knots (+36% yoy) of 1,100kV units (7 knots for Aba, 4 for Yantai-Weihai, 2 knots for Caozhou project, and 2 knots for power plants) and >100 knots (+7.5% yoy) of 750kV units in 2026E, up from 11 and 93, respectively, in 2025. Its orders on hand were Rmb12.6bn by end 2025, comprising Rmb11.3bn for high-voltage projects, Rmb1.2bn for distribution equipment, and Rmb100m for international projects, with the latter figure adjusted after the cancellation of previous high-risk contracts. The orders on hand comprised high-voltage GIS of 34 knots for 1100kV (including Yantai-Weihai, Datong, Aba, Caozhou, Zhumadian, and Liantang projects) and 150 knots for 750kv ones. Its 750kv knots had 45% market share from total 293 bidding in the market in 2025, up 77% yoy.

Figure 1. Equipment procurement of State Grid in 2025-26 so far for construction of ultra-high voltage transmission lines  
![](images/cb312106b6a221397c8080dfef9527825033cfc595c3b25ce045b806f7efd460.jpg)

<details>
<summary>bar-line hybrid</summary>

| Date | Value (Rmbbn) | Cumulative value (Rmbbn) | # of Bid packages |
| :--- | :--- | :--- | :--- |
| 202501 | 2.0 | 2.0 | 55 |
| 202502 | 0.5 | 2.5 | 42 |
| 202503 | 1.3 | 3.8 | 72 |
| 202504 | 16.5 | 20.3 | 114 |
| 202505 | 1.7 | 22.1 | 115 |
| 202601 | 4.0 | 4.0 | 136 |
| 202601-n | 5.0 | 9.0 | 12 |
| 202602 | 9.4 | 18.4 | 119 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, sgcc.com.cn

Figure 2. Listed companies winning the most orders in the 2nd batch of equipment procurement for UHV line construction by State Grid

<table><tr><td>Company</td><td>Ticker</td><td>Rating</td><td>Rank</td><td>Value (Rmbbn)</td><td>% of total value</td><td># Bid packages</td><td>Biggest package</td><td>Winning bidder</td></tr><tr><td>Pingao</td><td>600312.SH</td><td>BUY</td><td>1</td><td>2.09</td><td>22.2%</td><td>9</td><td>0.90</td><td>5</td></tr><tr><td>XD Electric</td><td>601179.SH</td><td>Not covered</td><td>2</td><td>1.90</td><td>20.2%</td><td>10</td><td>0.62</td><td>6</td></tr><tr><td>TBEA</td><td>600089.SH</td><td>BUY</td><td>3</td><td>0.47</td><td>5.0%</td><td>6</td><td>0.14</td><td>3</td></tr><tr><td>HSINO</td><td>601096.SH</td><td>Not covered</td><td>4</td><td>0.20</td><td>2.2%</td><td>5</td><td>0.10</td><td>2</td></tr><tr><td>Sieyuan</td><td>002028.SZ</td><td>BUY</td><td>5</td><td>0.20</td><td>2.1%</td><td>6</td><td>0.06</td><td>4</td></tr><tr><td>SGIT</td><td>600131.SH</td><td>Not covered</td><td>6</td><td>0.15</td><td>1.6%</td><td>6</td><td>0.0</td><td>2</td></tr><tr><td>NARI</td><td>600406.SH</td><td>BUY</td><td>7</td><td>0.14</td><td>1.5%</td><td>4</td><td>0.1</td><td>3</td></tr><tr><td>FenGFan</td><td>601700.SH</td><td>Not covered</td><td>8</td><td>0.14</td><td>1.4%</td><td>4</td><td>0.06</td><td>1</td></tr><tr><td>Shaanxi Constrution</td><td>600248.SH</td><td>Not covered</td><td>9</td><td>0.11</td><td>1.1%</td><td>1</td><td>0.11</td><td>1</td></tr><tr><td>CEEC</td><td>601868.SH</td><td>Not covered</td><td>10</td><td>0.10</td><td>1.1%</td><td>2</td><td>0.05</td><td>1</td></tr><tr><td>Others</td><td></td><td></td><td></td><td>3.92</td><td>41.6%</td><td>66</td><td>n/a</td><td>51</td></tr><tr><td>Total</td><td></td><td></td><td></td><td>9.42</td><td>100.0%</td><td>119</td><td>0.90</td><td>79</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, sgcc.com.cn

Figure 3. Valuation comp table of global, Asian and Chinese power grid equipment makers

<table><tr><td rowspan="2"></td><td rowspan="2">Stock code</td><td rowspan="2">Citi rating</td><td rowspan="2">Price 8-Jun-26</td><td rowspan="2">Target price</td><td rowspan="2">Potential upside</td><td colspan="2">PER</td><td colspan="2">PB</td><td colspan="2">ROE</td><td colspan="2">Yield</td><td colspan="2">Net D/E</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td colspan="16">PRC private companies:</td></tr><tr><td>Sieyuan</td><td>002028.SZ</td><td>Buy</td><td>177.6</td><td>270.0</td><td>52.0%</td><td>29.6</td><td>21.3</td><td>7.2</td><td>5.6</td><td>26.9%</td><td>29.6%</td><td>0.6%</td><td>0.8%</td><td>net cash</td><td>net cash</td></tr><tr><td>Huaming Electric</td><td>002270.SZ</td><td>Buy</td><td>19.6</td><td>32.5</td><td>66.0%</td><td>22.2</td><td>19.7</td><td>5.1</td><td>4.7</td><td>23.9%</td><td>25.1%</td><td>3.2%</td><td>3.5%</td><td>net cash</td><td>net cash</td></tr><tr><td>Wasion Holdings</td><td>3393.HK</td><td>Buy</td><td>20.8</td><td>34.0</td><td>63.6%</td><td>13.6</td><td>10.9</td><td>2.7</td><td>2.3</td><td>20.3%</td><td>22.8%</td><td>2.9%</td><td>3.7%</td><td>net cash</td><td>net cash</td></tr><tr><td>Sanxing Medical Electric</td><td>601567.SS</td><td>n/a</td><td>14.8</td><td>n/a</td><td>n/a</td><td>9.2</td><td>7.3</td><td>1.5</td><td>1.4</td><td>16.9%</td><td>19.3%</td><td>5.5%</td><td>6.8%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Sub-sector average</td><td></td><td></td><td></td><td></td><td></td><td>17.5</td><td>13.9</td><td>3.6</td><td>3.1</td><td>19.9%</td><td>22.0%</td><td>3.4%</td><td>4.2%</td><td>n.a.</td><td>n.a.</td></tr><tr><td colspan="16">PRC SOEs:</td></tr><tr><td>Pinggao</td><td>600312.SS</td><td>Buy</td><td>18.5</td><td>24.0</td><td>29.9%</td><td>19.8</td><td>17.1</td><td>2.1</td><td>1.9</td><td>10.8%</td><td>11.6%</td><td>2.1%</td><td>2.6%</td><td>net cash</td><td>net cash</td></tr><tr><td>NARI</td><td>600406.SS</td><td>Buy</td><td>22.9</td><td>31.0</td><td>35.6%</td><td>19.9</td><td>18.4</td><td>3.3</td><td>3.0</td><td>16.9%</td><td>17.2%</td><td>3.0%</td><td>3.3%</td><td>net cash</td><td>net cash</td></tr><tr><td>XJ Electric</td><td>000400.SZ</td><td>Buy</td><td>22.1</td><td>33.0</td><td>49.5%</td><td>17.4</td><td>16.3</td><td>1.7</td><td>1.6</td><td>10.2%</td><td>10.1%</td><td>2.3%</td><td>2.5%</td><td>net cash</td><td>net cash</td></tr><tr><td>TBEA</td><td>600089.SS</td><td>Buy</td><td>23.9</td><td>36.0</td><td>50.4%</td><td>13.3</td><td>11.7</td><td>1.6</td><td>1.5</td><td>12.7%</td><td>13.2%</td><td>2.4%</td><td>2.7%</td><td>24.3%</td><td>25.1%</td></tr><tr><td>XD Electric</td><td>601179.SS</td><td>n/a</td><td>14.0</td><td>n/a</td><td>n/a</td><td>46.1</td><td>38.1</td><td>3.0</td><td>2.8</td><td>6.5%</td><td>7.4%</td><td>0.9%</td><td>1.1%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Jinpan Smart Technology</td><td>688676.SS</td><td>n/a</td><td>83.6</td><td>n/a</td><td>n/a</td><td>42.9</td><td>31.2</td><td>6.3</td><td>5.5</td><td>15.2%</td><td>17.9%</td><td>0.9%</td><td>1.2%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Sub-sector average</td><td></td><td></td><td></td><td></td><td></td><td>26.6</td><td>22.1</td><td>3.0</td><td>2.7</td><td>12.1%</td><td>12.9%</td><td>1.9%</td><td>2.2%</td><td>n.a.</td><td>n.a.</td></tr><tr><td colspan="16">Asia (ex-China) companies:</td></tr><tr><td>Hyundai Electric</td><td>267260.KS</td><td>Buy</td><td>889,000.0</td><td>1,440,000.0</td><td>62.0%</td><td>31.5</td><td>24.5</td><td>11.5</td><td>8.5</td><td>42.0%</td><td>39.8%</td><td>0.8%</td><td>1.0%</td><td>net cash</td><td>net cash</td></tr><tr><td>LS Electric</td><td>010120.KS</td><td>Buy</td><td>208,000.0</td><td>320,000.0</td><td>53.8%</td><td>66.0</td><td>45.7</td><td>13.1</td><td>11.0</td><td>21.3%</td><td>26.2%</td><td>0.5%</td><td>0.7%</td><td>33.4%</td><td>34.5%</td></tr><tr><td>Hyosung Heavy</td><td>298040.KS</td><td>Buy</td><td>3,196,000.0</td><td>4,500,000.0</td><td>40.8%</td><td>35.2</td><td>25.4</td><td>10.0</td><td>7.6</td><td>32.0%</td><td>34.1%</td><td>0.6%</td><td>0.8%</td><td>net cash</td><td>net cash</td></tr><tr><td>Chung Hsin Electric</td><td>1513.TW</td><td>Buy</td><td>169.5</td><td>180.0</td><td>6.2%</td><td>18.6</td><td>16.5</td><td>3.8</td><td>3.6</td><td>21.0%</td><td>22.4%</td><td>4.0%</td><td>4.5%</td><td>-9.5%</td><td>-30.0%</td></tr><tr><td>Fortune Electric</td><td>1519.TW</td><td>Buy</td><td>815.0</td><td>1,150.0</td><td>41.1%</td><td>42.0</td><td>32.3</td><td>21.4</td><td>18.9</td><td>53.6%</td><td>62.0%</td><td>1.9%</td><td>2.5%</td><td>net cash</td><td>net cash</td></tr><tr><td>Shihlin Electric &amp; Engineering</td><td>1503.TW</td><td>n/a</td><td>230.0</td><td>n/a</td><td>n/a</td><td>25.3</td><td>16.8</td><td>3.1</td><td>N/A</td><td>12.9%</td><td>16.7%</td><td>N/A</td><td>N/A</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Sub-sector average</td><td></td><td></td><td></td><td></td><td></td><td>38.7</td><td>28.9</td><td>12.0</td><td>9.9</td><td>34.0%</td><td>36.9%</td><td>1.6%</td><td>1.9%</td><td>n.a.</td><td>n.a.</td></tr><tr><td colspan="16">Global companies:</td></tr><tr><td>ABB</td><td>ABBN.S</td><td>Neutral</td><td>81.9</td><td>78.0</td><td>-4.7%</td><td>31.7</td><td>29.3</td><td>9.4</td><td>8.1</td><td>43.7%</td><td>28.7%</td><td>1.2%</td><td>1.2%</td><td>net cash</td><td>net cash</td></tr><tr><td>Siemens Energy</td><td>ENR1n.DE</td><td>Neutral</td><td>157.5</td><td>185.0</td><td>17.5%</td><td>35.3</td><td>24.1</td><td>13.1</td><td>11.4</td><td>34.6%</td><td>49.4%</td><td>1.3%</td><td>1.8%</td><td>net cash</td><td>net cash</td></tr><tr><td>Alstom</td><td>ALSO.PA</td><td>Buy</td><td>16.7</td><td>28.0</td><td>67.9%</td><td>11.8</td><td>9.6</td><td>0.7</td><td>0.7</td><td>3.1%</td><td>5.4%</td><td>N/A</td><td>1.5%</td><td>11.4%</td><td>11.8%</td></tr><tr><td>Schneider Electric</td><td>SCHN.PA</td><td>Buy</td><td>266.8</td><td>340.0</td><td>27.4%</td><td>25.7</td><td>22.5</td><td>5.6</td><td>5.0</td><td>20.8%</td><td>21.7%</td><td>1.6%</td><td>1.7%</td><td>41.8%</td><td>28.8%</td></tr><tr><td>Sub-sector average</td><td></td><td></td><td></td><td></td><td></td><td>26.1</td><td>21.4</td><td>7.2</td><td>6.3</td><td>25.5%</td><td>26.3%</td><td>1.4%</td><td>1.6%</td><td>26.6%</td><td>20.3%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, IEBS

## Companies Mentioned:

ABB (ABBN.S; SFr83.1; 2; 05 Jun 26; 17:30) | Alstom (ALSO.PA; €17.15; 1; 05 Jun 26; 17:30) | Changshu Fengfan Power Equipment Co Ltd (601700.SS; Rmb4.95; Not Rated; 08 Jun 26; 15:00) | China Energy Engineering Corp Ltd (601868.SS; Rmb2.8; Not Rated; 08 Jun 26; 15:00) | China XD Electric (601179.SS; Rmb14.01; Not Rated; 08 Jun 26; 15:00) | Chung Hsin Electric (1513.TW; NT\$169.5; 1; 08 Jun 26; 13:30) | Fortune Electric (1519.TW; NT\$815.0; 1; 08 Jun 26; 13:30) | Hainan Jinpan Smart Technology Co Ltd (688676.SS; Rmb83.6; Not Rated; 08 Jun 26; 15:00) | HD Hyundai Electric (267260.KS; W889000.0; 1; 08 Jun 26; 15:45) | Henan Pinggao Electric Co (600312.SS; Rmb18.48; 1; 08 Jun 26; 15:00) | Hsino Tower Group Co Ltd (601096.SS; Rmb4.69; Not Rated; 08 Jun 26; 15:00) | Huaming Power Equipment (002270.SZ; Rmb19.58; 1; 08 Jun 26; 15:00) | Hyosung Heavy Industries (298040.KS; W3196000.0; 1; 08 Jun 26; 15:45) | LS Electric (010120.KS; W208000.0; 1; 08 Jun 26; 15:45) | NARI Technology Co (600406.SS; Rmb22.86; 1; 08 Jun 26; 15:00) | Schneider Electric (SCHN.PA; €269.05; 1; 05 Jun 26; 17:30) | Shaanxi Construction Engineering Group Corp Ltd (600248.SS; Rmb3.07; Not Rated; 08 Jun 26; 15:00) | Shihlin Electric & Engineering Corp (1503.TW; NT\$230.0; Not Rated; 08 Jun 26; 13:30) | Siemens Energy AG (ENRIn.DE; €158.02; 2;

05 Jun 26; 17:30) | Sieyuan Electric (002028.SZ; Rmb177.59; 1; 08 Jun 26; 15:00) | State Grid Information & Communication Co Ltd (600131.SS; Rmb15.4; Not Rated; 08 Jun 26; 15:00) | TBEA Co (600089.SS; Rmb23.94; 1; 08 Jun 26; 15:00) | Wasion Holdings (3393.HK; HK\$20.78; 1; 08 Jun 26; 16:10) | XJ Electric (000400.SZ; Rmb22.07; 1; 08 Jun 26; 15:00)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>The Firm has made a market in the publicly traded equity securities of Wasion Holdings Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of Schneider Electric,Wasion Holdings.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from ABB,NARI Technology Co,Schneider Electric,Siemens Energy AG,Wasion Holdings.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from NARI Technology Co,Schneider Electric.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from ABB,Alstom,HD Hyundai Electric,Hainan Jinpan Smart Technology Co Ltd,Hyosung Heavy Industries,LS Electric,NARI Technology Co,Schneider Electric,Shihlin Electric &amp; Engineering Corp,Siemens Energy AG,Sieyuan Electric in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): ABB,NARI Technology Co,Schneider Electric,Siemens Energy AG,Wasion Holdings.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: ABB,Alstom,HD Hyundai Electric,Hainan Jinpan Smart Technology Co Ltd,LS Electric,NARI Technology Co,Schneider Electric,Siemens Energy AG,Sieyuan Electric.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has,

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
