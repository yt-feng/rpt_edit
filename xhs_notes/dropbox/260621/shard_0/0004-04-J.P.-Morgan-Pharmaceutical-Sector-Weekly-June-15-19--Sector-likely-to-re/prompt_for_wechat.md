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

Figure 3: Japan Pharmaceutical Sector Valuations

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">JPM Rating</td><td rowspan="2">Price 19-Jun-26(¥)</td><td rowspan="2">JPM Price Target(¥)</td><td rowspan="2">Implied Return</td><td rowspan="2">Mcap 19-Jun-26(¥bn)</td><td colspan="2">P/E(x)</td><td colspan="2">P/B(x)</td><td colspan="2">EV/EBITDA(x)</td><td colspan="2">ROE(%)</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td></tr><tr><td>4151</td><td>Kyowa Kirin</td><td>UW</td><td>2,538</td><td>1,800</td><td>-29.1%</td><td>1,334</td><td>17.5</td><td>13.9</td><td>1.4</td><td>1.3</td><td>6.8</td><td>6.8</td><td>8.3</td><td>10.0</td></tr><tr><td>4502</td><td>Takeda Pharmaceutical</td><td>N</td><td>4,934</td><td>4,900</td><td>-0.7%</td><td>7,851</td><td>10.1</td><td>11.1</td><td>1.2</td><td>1.2</td><td>11.8</td><td>11.3</td><td>3.9</td><td>4.7</td></tr><tr><td>4503</td><td>Astellas Pharma</td><td>N</td><td>2,146</td><td>2,500</td><td>16.5%</td><td>3,883</td><td>9.9</td><td>10.2</td><td>2.0</td><td>1.8</td><td>6.2</td><td>6.4</td><td>22.0</td><td>18.8</td></tr><tr><td>4506</td><td>Sumitomo Pharma</td><td>OW</td><td>1,470</td><td>2,300</td><td>56.5%</td><td>660</td><td>6.7</td><td>6.9</td><td>1.4</td><td>1.2</td><td>6.4</td><td>5.3</td><td>25.2</td><td>18.2</td></tr><tr><td>4507</td><td>Shionogi &amp; Co.</td><td>N</td><td>2,780</td><td>3,100</td><td>11.5%</td><td>2,473</td><td>12.0</td><td>10.8</td><td>1.4</td><td>1.3</td><td>5.6</td><td>4.9</td><td>12.5</td><td>12.7</td></tr><tr><td>4516</td><td>Nippon Shinyaku</td><td>N</td><td>3,972</td><td>4,000</td><td>0.7%</td><td>279</td><td>10.4</td><td>28.2</td><td>0.9</td><td>0.9</td><td>5.1</td><td>10.7</td><td>9.4</td><td>3.4</td></tr><tr><td>4519</td><td>Chugai Pharmaceutical</td><td>OW</td><td>7,550</td><td>11,000</td><td>45.7%</td><td>12,677</td><td>24.2</td><td>18.5</td><td>5.4</td><td>4.7</td><td>15.8</td><td>12.2</td><td>23.6</td><td>26.9</td></tr><tr><td>4523</td><td>Eisai</td><td>N</td><td>3,902</td><td>5,100</td><td>30.7%</td><td>1,138</td><td>17.5</td><td>21.3</td><td>1.3</td><td>1.3</td><td>9.6</td><td>10.9</td><td>7.4</td><td>6.0</td></tr><tr><td>4528</td><td>Ono Pharmaceutical</td><td>UW</td><td>2,249</td><td>1,800</td><td>-20.0%</td><td>1,122</td><td>15.2</td><td>17.2</td><td>1.2</td><td>1.2</td><td>7.8</td><td>8.4</td><td>8.3</td><td>7.1</td></tr><tr><td>4536</td><td>Santen Pharmaceutical</td><td>OW</td><td>1,874</td><td>2,600</td><td>38.7%</td><td>604</td><td>15.3</td><td>12.5</td><td>2.0</td><td>1.8</td><td>8.3</td><td>7.3</td><td>12.7</td><td>15.1</td></tr><tr><td>4552</td><td>JCR Pharmaceuticals (*NC)</td><td>NC</td><td>457</td><td>-</td><td>-</td><td>59</td><td>74.8</td><td>65.8</td><td>1.2</td><td>1.2</td><td>26.0</td><td>31.7</td><td>4.6</td><td>1.7</td></tr><tr><td>4568</td><td>Daiichi Sa

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 20 Jun 2026 01:22 AM JST

Disseminated 20 Jun 2026 01:23 AM JST
"""
