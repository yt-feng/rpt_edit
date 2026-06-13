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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Asia Power Equipment

Addressing investors' key questions - What to do post the 20-30% decline during 2Q?

Chinese and Korean power equipment companies have pulled back by more than 20-30% from their April peaks, and in this note we address key investor questions. We believe the pullback reflects concerns over data center connection delays, geopolitical tensions, and a lack of immediate catalysts following record-high 1Q new orders. While we cautioned against elevated valuations in our previous note, we are more comfortable with current valuations after the 20-30% decline from the peak (Figure 2). We see good value in Hyosung Heavy, as the stock trades at \~20x 2028E P/E — the cheapest among Korean electricals (Figure 1) — and should be least impacted by any data center connection issues, if they materialize, as it derives more than 90% of new orders from utilities and grids in the U.S., where capex growth remains structural. For the Chinese names, fund flows into the AI sector and rising concerns over geopolitical tensions have also weighed on share performance. Our base case is that the E.U. is unlikely to impose trade tariffs on Chinese power equipment, as Chinese players' market share in the EU remains small at less than 10%, making it unlikely to threaten the market share of domestic players such as Siemens Energy. The pullback presents an attractive entry point for quality players such as Wasion Holdings (3393 HK), which trades at \~10x 1-year forward P/E with more than 20% earnings growth p.a.

- Concerns about data center capacity growth have dragged down share performance in 2Q: A number of power equipment companies have pulled back recently (Figure 3) following the release of 1Q results. While we are not aware of any fundamental changes, we believe investors are increasingly concerned about slower-than-expected data center capacity growth next year, driven by potential delays in permitting, power constraints and other issues. This may lead to slower-than-expected new order growth, especially for behind-the-meter generation equipment.  
- Why did the Korean names pull back by \~25% in a month despite a strong beat in 1Q new orders? This compares with a flat KOSPI over the same period. We believe the pullback reflects several factors: (1) Valuation: Hyundai Electric and Hyosung Heavy traded at \~35x 1-year forward P/E at their valuation peaks, representing a premium to some global peers. (2) Short interest and funding dynamics: We have seen rising short interest in the sector locally, especially in Hyundai Electric and LS Electric. We sense that some hedge fund investors may have positioned power equipment companies as a short to fund long positions in memory names, as the two sectors have somewhat traded in tandem with U.S. tech stocks. (3) Lack of high-frequency catalysts: There is limited forward-looking and high-frequency data between quarterly results for power equipment companies. Some investors are concerned that order growth may slow from 2Q, given the high sequential base in 1Q, when new orders doubled for some names.  
- Rising concerns about geopolitical tensions have also weighed on sentiment for Chinese names: We have seen rising concerns from local investors regarding new order growth in the E.U. for Chinese power equipment players. This follows the European Commission's measures on the auto sector

## Power Equipment and Utilities

## Stephen Tsui, CFA AC

(852) 2800-8592

stephen.tsui@JPM.com

## Vento Suen

(852) 2800-8546

vento.suen@JPM.com

## Alan Hon

(852) 2800-8573

alan.hon@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

and inverters (note). Overall, we believe the risk of the EU imposing trade tariffs on Chinese electrical equipment is low. This is because the market share of Chinese products remains below 10% in our estimates, and China mainly exports primary electrical equipment to the EU, with less exposure to software and systems. As a result, we believe the impact of rising Chinese product sales on EU electrical equipment companies is muted. As demand for electrical equipment rises amid the region’s energy transition commitments, we believe EU countries will continue to procure Chinese products given limited domestic capacity.

\- How would delays in data center connections affect new order wins? Among our coverage, we believe Korean power equipment companies focused on heavy electricals, such as Hyundai Electric and Hyosung Heavy, would be least impacted by data center connection issues. This is because data centers account for less than 10% of new orders, while the bulk of orders come from utilities and grid customers, which are independent of data center connection issues. We believe order growth for both companies should remain intact, as transmission capex in the U.S. should continue to see structural growth.

Table 1: Asia Power Equipment Valuation Comps

<table><tr><td rowspan="2"></td><td rowspan="2">Ticker</td><td rowspan="2">JPM rating</td><td rowspan="2">Share price (LC)</td><td rowspan="2">Mkt Cap (USDm)</td><td rowspan="2">Daily liquidity (USDm)</td><td colspan="2">PE (x)</td><td colspan="2">P/BV (x)</td><td colspan="2">Dividend yield (%)</td><td colspan="2">ROE (%)</td><td colspan="2">EV/EBITDA (x)</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td>Hitachi</td><td>6501 JP</td><td>OW</td><td>4,655.0</td><td>131,529</td><td>433.1</td><td>22.6</td><td>19.9</td><td>3.3</td><td>3.0</td><td>1.0</td><td>1.0</td><td>14.5</td><td>15.2</td><td>11.4</td><td>10.5</td></tr><tr><td colspan="16">Mainland China</td></tr><tr><td>Nari Technology</td><td>600406 CH</td><td>OW</td><td>22.9</td><td>27,076</td><td>380.3</td><td>19.0</td><td>16.7</td><td>3.3</td><td>3.0</td><td>3.2</td><td>3.6</td><td>13.9</td><td>13.8</td><td>14.4</td><td>12.9</td></tr><tr><td>Qingdao TGood</td><td>300001 CH</td><td>OW</td><td>36.3</td><td>5,654</td><td>183.4</td><td>24.7</td><td>20.9</td><td>3.9</td><td>3.4</td><td>0.7</td><td>0.8</td><td>16.8</td><td>17.4</td><td>16.6</td><td>14.6</td></tr><tr><td>Xuji Electric</td><td>000400 CH</td><td>OW</td><td>21.6</td><td>3,248</td><td>124.3</td><td>13.8</td><td>12.0</td><td>1.5</td><td>1.4</td><td>2.8</td><td>3.1</td><td>12.8</td><td>13.4</td><td>8.3</td><td>7.4</td></tr><tr><td>Wasion Holdings</td><td>3393 HK</td><td>OW</td><td>19.9</td><td>2,653</td><td>27.8</td><td>13.6</td><td>11.3</td><td>2.6</td><td>2.3</td><td>3.3</td><td>4.0</td><td>19.8</td><td>21.3</td><td>8.7</td><td>7.3</td></tr><tr><td>Gold Cup Electric</td><td>002533 CH</td><td>NC</td><td>10.8</td><td>1,174</td><td>33.5</td><td>11.1</td><td>9.8</td><td>1.7</td><td>1.5</td><td>4.9</td><td>5.6</td><td>15.0</td><td>15.8</td><td>12.4</td><td>11.0</td></tr><tr><td>Hexing Electrical</td><td>603556 CH</td><td>NC</td><td>23.6</td><td>1,690</td><td>25.0</td><td>10.3</td><td>8.8</td><td>1.4</td><td>1.3</td><td>4.3</td><td>5.6</td><td>12.8</td><td>14.1</td><td>8.0</td><td>6.4</td></tr><tr><td>Liangxin Electric</td><td>002706 CH</td><td>NC</td><td>11.5</td><td>1,904</td><td>119.6</td><td>36.7</td><td>27.6</td><td>2.9</td><td>2.8</td><td>1.8</td><td>2.3</td><td>7.6</td><td>10.1</td><td>18.9</td><td>15.8</td></tr><tr><td>Eaglerise Electric</td><td>002922 CH</td><td>NC</td><td>34.1</td><td>2,126</td><td>147.4</td><td>28.3</td><td>19.7</td><td>3.5</td><td>3.2</td><td>1.8</td><td>2.6</td><td>12.1</td><td>16.4</td><td>18.5</td><td>13.8</td></tr><tr><td>Pinggao Electric</td><td>600312 CH</td><td>NC</td><td>18.2</td><td>3,633</td><td>91.4</td><td>17.4</td><td>14.5</td><td>2.0</td><td>1.8</td><td>1.8</td><td>2.0</td><td>11.6</td><td>12.7</td><td>10.5</td><td>8.9</td></tr><tr><td>Sifang Automation</td><td>601126 CH</td><td>NC</td><td>67.1</td><td>8,244</td><td>271.1</td><td>56.8</td><td>48.6</td><td>10.3</td><td>9.5</td><td>1.2</td><td>1.3</td><td>18.7</td><td>20.0</td><td>44.9</td><td>38.0</td></tr><tr><td>China XD</td><td>601179 CH</td><td>NC</td><td>13.5</td><td>10,179</td><td>551.8</td><td>42.9</td><td>35.0</td><td>2.8</td><td>2.7</td><td>0.7</td><td>0.8</td><td>6.5</td><td>7.5</td><td>23.5</td><td>20.3</td></tr><tr><td>Shemar Electric</td><td>603530 CH</td><td>NC</td><td>51.1</td><td>3,254</td><td>50.0</td><td>36.4</td><td>27.3</td><td>9.9</td><td>7.9</td><td>1.0</td><td>1.3</td><td>28.8</td><td>30.7</td><td>24.5</td><td>19.4</td></tr><tr><td>Sanxing</td><td>601567 CH</td><td>NC</td><td>14.0</td><td>2,894</td><td>89.7</td><td>8.7</td><td>7.3</td><td>1.5</td><td>1.3</td><td>6.2</td><td>7.8</td><td>15.9</td><td>18.2</td><td>6.7</td><td>5.4</td></tr><tr><td colspan="16">India</td></tr><tr><td>ABB India</td><td>ABB IN</td><td>N</td><td>6,719.0</td><td>14,868</td><td>34.6</td><td>80.1</td><td>63.6</td><td>16.4</td><td>14.3</td><td>0.6</td><td>0.7</td><td>21.5</td><td>24.0</td><td>66.2</td><td>51.0</td></tr><tr><td>Bharat Heavy</td><td>BHEL IN</td><td>UW</td><td>370.7</td><td>13,478</td><td>64.7</td><td>37.3</td><td>24.4</td><td>4.5</td><td>3.9</td><td>0.8</td><td>1.0</td><td>12.5</td><td>17.1</td><td>26.2</td><td>16.9</td></tr><tr><td>CG Power</td><td>CGPOWER IN</td><td>OW</td><td>901.4</td><td>14,824</td><td>35.2</td><td>87.1</td><td>67.5</td><td>15.2</td><td>12.6</td><td>0.2</td><td>0.2</td><td>18.3</td><td>20.0</td><td>64.9</td><td>49.5</td></tr><tr><td>Hitachi Energy India</td><td>POWERIND IN</td><td>OW</td><td>33,250.0</td><td>15,476</td><td>58.7</td><td>100.5</td><td>70.1</td><td>22.5</td><td>17.2</td><td>0.0</td><td>0.1</td><td>25.1</td><td>27.8</td><td>76.2</td><td>51.4</td></tr><tr><td>Power Grid</td><td>PWGR IN</td><td>OW</td><td>286.7</td><td>27,840</td><td>46.3</td><td>15.9</td><td>14.5</td><td>2.5</td><td>2.3</td><td>3.3</td><td>3.6</td><td>15.4</td><td>15.4</td><td>10.7</td><td>10.2</td></tr><tr><td>Siemens India</td><td>SIEM IN</td><td>UW</td><td>3,522.0</td><td>13,098</td><td>20.7</td><td>45.6</td><td>60.9</td><td>9.1</td><td>8.1</td><td>0.3</td><td>0.3</td><td>17.4</td><td>14.0</td><td>42.5</td><td>46.5</td></tr><tr><td>Transformers &amp; Rectifiers India</td><td>TARIL IN</td><td>NC</td><td>300.5</td><td>942</td><td>14.8</td><td>28.4</td><td>22.3</td><td>4.9</td><td>4.0</td><td>0.1</td><td>0.2</td><td>17.4</td><td>18.3</td><td>18.2</td><td>14.3</td></tr><tr><td>Voltamp Transformers</td><td>VAMP IN</td><td>NC</td><td>9,531.5</td><td>1,007</td><td>7.9</td><td>28.6</td><td>24.5</td><td>4.8</td><td>4.2</td><td>1.1</td><td>1.3</td><td>17.7</td><td>18.2</td><td>24.3</td><td>20.7</td></tr><tr><td>GEV T&amp;D</td><td>GVTD IN</td><td>OW</td><td>4,735.0</td><td>12,661</td><td>40.1</td><td>77.9</td><td>58.9</td><td>31.0</td><td>22.0</td><td>0.3</td><td>0.4</td><td>47.1</td><td>43.7</td><td>58.0</td><td>43.6</td></tr><tr><td>Siemens Energy India</td><td>ENRIN IN</td><td>N</td><td>3,412.5</td><td>12,691</td><td>20.8</td><td>63.4</td><td>52.5</td><td>16.2</td><td>12.7</td><td>0.1</td><td>0.2</td><td>29.0</td><td>27.1</td><td>46.1</td><td>37.6</td></tr><tr><td colspan="16">Japan</td></tr><tr><td>Mitsubishi Heavy</td><td>7011 JP</td><td>NC</td><td>3,494.0</td><td>73,429</td><td>673.7</td><td>28.7</td><td>24.1</td><td>3.6</td><td>3.2</td><td>0.9</td><td>1.0</td><td>13.0</td><td>14.1</td><td>15.4</td><td>13.4</td></tr><tr><td>Mitsubishi Electric</td><td>6503 JP</td><td>OW</td><td>5,446.0</td><td>71,695</td><td>248.0</td><td>23.2</td><td>20.6</td><td>2.6</td><td>2.5</td><td>1.1</td><td>1.2</td><td>11.3</td><td>11.9</td><td>13.4</td><td>12.3</td></tr><tr><td>Fuji Electric</td><td>6504 JP</td><td>NC</td><td>13,305.0</td><td>12,374</td><td>89.7</td><td>18.9</td><td>17.4</td><td>2.3</td><td>2.1</td><td>1.6</td><td>1.8</td><td>12.6</td><td>12.7</td><td>10.0</td><td>9.3</td></tr><tr><td colspan="16">Korea</td></tr><tr><td>LS Electric</td><td>010120 KS</td><td>N</td><td>232,500</td><td>22,788</td><td>352.7</td><td>71.6</td><td>53.6</td><td>14.1</td><td>11.7</td><td>0.4</td><td>0.6</td><td>21.4</td><td>23.9</td><td>42.1</td><td>32.2</td></tr><tr><td>HD Hyundai Electric</td><td>267260 KS</td><td>OW</td><td>1,033,000</td><td>24,332</td><td>169.7</td><td>37.2</td><td>28.9</td><td>13.9</td><td>10.6</td><td>0.9</td><td>1.2</td><td>42.4</td><td>41.5</td><td>26.7</td><td>20.6</td></tr><tr><td>Hyosung Heavy Industries</td><td>298040 KS</td><td>OW</td><td>3,307,000</td><td>20,149</td><td>182.5</td><td>39.2</td><td>27.9</td><td>10.0</td><td>7.6</td><td>0.3</td><td>0.5</td><td>29.0</td><td>30.9</td><td>27.5</td><td>20.1</td></tr><tr><td>Sanil Electric</td><td>062040 KS</td><td>NC</td><td>218,500</td><td>4,371</td><td>148.1</td><td>31.8</td><td>25.5</td><td>8.8</td><td>6.8</td><td>0.6</td><td>0.8</td><td>31.9</td><td>31.4</td><td>24.8</td><td>19.9</td></tr><tr><td>Iljin Electric</td><td>103590 KS</td><td>NC</td><td>79,900</td><td>2,490</td><td>74.8</td><td>24.3</td><td>20.4</td><td>5.3</td><td>4.4</td><td>0.8</td><td>0.9</td><td>23.9</td><td>23.4</td><td>16.3</td><td>14.1</td></tr><tr><td colspan="16">Taiwan</td></tr><tr><td>Shilin Electric</td><td>1503 TT</td><td>NC</td><td>215.0</td><td>3,542</td><td>27.5</td><td>24.6</td><td>15.7</td><td>2.9</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>12.9</td><td>16.7</td><td>18.1</td><td>11.7</td></tr><tr><td>Chung-Hsin Electric</td><td>1513 TT</td><td>NC</td><td>164.0</td><td>2,609</td><td>48.9</td><td>18.5</td><td>15.6</td><td>3.7</td><td>4.3</td><td>3.9</td><td>4.5</td><td>20.4</td><td>22.6</td><td>9.1</td><td>8.1</td></tr><tr><td>Allis Electric</td><td>1514 TT</td><td>NC</td><td>118.0</td><td>1,019</td><td>20.1</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Fortune Electric</td><td>1519 TT</td><td>NC</td><td>773.0</td><td>7,721</td><td>101.5</td><td>37.4</td><td>28.1</td><td>16.7</td><td>12.4</td><td>1.9</td><td>2.5</td><td>53.3</td><td>53.4</td><td>28.7</td><td>21.4</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates (consensus estimates for non-covered companies). Priced as of 11 Jun 2026.

Figure 1: Korea Power Equipment Companies' Valuation  
![](images/aabf8787f735cd49f407fe590dffadccc3003ad72effacf5af404832ec83cd2c.jpg)

<details>
<summary>bar chart</summary>

| Company | FY27E P/E (x) | FY28E P/E (x) |
| :--- | :--- | :--- |
| Hyosung Heavy | 28 | 22 |
| HD Hyundai Electric | 29 | 25 |
| LS Electric | 53 | 45 |
</details>

Source: Bloomberg Finance L.P., JPM estimates. Priced as of 11 Jun 2026.

Figure 2: Fund Rotations from China Power Equipment into China AI-Themed Stocks  
![](images/0b3482c35fd0b19f2017b082973ac6ba3b281963d0cdf8d9b6b23daed1691cfb.jpg)

<details>
<summary>bar chart</summary>

| Quarter | China Power Equipment (%) | China AI (%) |
| :--- | :--- | :--- |
| 1Q26 | 20 | 0 |
| 2Q26 | -11 | 56 |
</details>

Source: Bloomberg Finance L.P., JPM. Priced as of 11 Jun 2026.

Figure 3: Share Price Weaknesses Across Global Power Equipment Companies Since May  
![](images/fbd56ef69fbe4ab9f259d797320f2d1c5f8db31a1bcf299898473496bfa53b32.jpg)

<details>
<summary>bar chart</summary>

| Company | Share performance since May (%) |
| :--- | :--- |
| Hitachi | -3 |
| Eaton | -12 |
| Nari Tech | -12 |
| Vertiv | -14 |
| LS Electric | -16 |
| Hyosung Heavy | -16 |
| Hyundai Electric | -18 |
| GEV | -18 |
| Siemens Energy | -21 |
| Wasion | -27 |
</details>

Source: Bloomberg Finance L.P., JPM. Priced as of 11 Jun 2026.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

• Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to HD Hyundai Electric, Hyosung Heavy Industries or related entities.  
- Market Maker/ Liquidity Provider (Hong Kong): JPM Securities (Asia Pacific) Limited and/or JPM Broking (Hong Kong) Limited and/or an affiliate is a market maker and/or liquidity provider in the securities of Wasion Holdings Ltd - H or related entities and/or warrants or options thereon, which are listed or traded on The Stock Exchange of Hong Kong Limited.  
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: HD Hyundai Electric, Hyosung Heavy Industries, Wasion Holdings Ltd - H or related entities.  
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: HD Hyundai Electric, Hyosung Heavy Industries, Wasion Holdings Ltd - H or related entities.  
- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Hyosung Heavy Industries or related entities.  
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Wasion Holdings Ltd - H or related entities.  
• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from HD Hyundai Electric, Hyosung Heavy Industries, Wasion Holdings Ltd - H or related entities.  
- Debt Position: JPM may hold a position in the debt securities of HD Hyundai 

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 11 Jun 2026 08:44 PM HKT

Disseminated 11 Jun 2026 08:44 PM HKT
"""
