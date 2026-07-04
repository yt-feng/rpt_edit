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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化。汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
July 1, 2026 04:14 AM GMT

Semiconductors | North America

# Semiconductor Inventory Tracker: Not Restocking Yet

Supply chain inventory rose q/q but outperformed seasonality, with below-seasonal producer builds and distributor declines. Supply is tightening, but meaningful restocking has yet to emerge.

## Key Takeaways

\- Overall supply chain outperformed seasonality, increasing by less than the typical 1Q increase.

\- Producer and disti DOIs outperformed seasonality; customers were \~in-line.

■ Auto OEM DOI moved above historical median, while Auto Supplier DOI declined to in-line with historical levels.

Overall supply chain inventory increased q/q in 1Q, but the build was below typical 1Q seasonality. We remain above historical median levels, as distributors declined and producers built less than seasonal levels, while customers were \~inline. While this is a step in the right direction, we still remain 33 days above historical median for the supply chain, and have not yet seen a broader restocking cycle.

The quarter reflected a mix of normal 1Q inventory build and continued discipline across the supply chain rather than broad restocking. Distributors continue to lean out, producer builds remain relatively steady, and customer trends were mixed. For stocks, we prefer areas where supply/demand is tightening or inventory risk is more defensible, including premium-end analog exposure in ADI and NXP, compute/networking names NVDA, AVGO, and CBRS, memory names MU and SNDK, and semicap names MKSI, KLAC, LRCX and ONTO.

Exhibit 1: Stacked DOI increased 9 days vs. a seasonal 19-day increase and is 33 days above the historical median. Trailing decreased \~2 days.

![](images/743526fa6b2c85d27e2630a81e92c2248082064e2ff319de50ff129cb5d71fca.jpg)  
Source: FactSet, MS

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Joseph Moore</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joseph.Moore@morganstanley.com</td><td>+1 212 761-7516</td></tr><tr><td colspan="2">Nicole Kozhukhov</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Nicole.Kozhukhov@morganstanley.com</td><td>+1 212 761-1636</td></tr><tr><td colspan="2">Ella Tulchinsky</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ella.Tulchinsky@morganstanley.com</td><td>+1 212 761-2222</td></tr><tr><td colspan="2">Shane Brett</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Shane.Brett@morganstanley.com</td><td>+1 212 761-1022</td></tr><tr><td colspan="2">Mason Wayne</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Mason.Wayne@morganstanley.com</td><td>+1 212 761-6012</td></tr></table>

<table><tr><td colspan="2">SEMICONDUCTORS</td></tr><tr><td>North America</td><td></td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td colspan="2">SEMICONDUCTOR CAPITAL EQUIPMENT</td></tr><tr><td>North America</td><td></td></tr><tr><td>Industry View</td><td>In-Line</td></tr></table>

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

## Supply Chain Inventory Overview

Supply chain inventory increased q/q in 1Q, but by less than typical seasonality, with customer inventory \~in-line, distributors declining, and producers building less than seasonal levels. Total supply chain DOI increased 9 days q/q vs. a seasonal increase of 19 days, leaving DOI 33 days above the historical median. The improvement was led by distributor lean-out and muted producer builds, while customers were mixed by end market.

Semiconductor customer inventory increased by 9 days, \~in-line with the seasonal increase of 8 days, and now sits above the historical median by 6 days. The only semi customer where DOI decreased was Auto Suppliers (-1 day). Communications (+17 days) and ODMs (+16 days) saw the largest increases q/q. Storage remains slightly below its historical median, while other customers are now in-line (Auto suppliers, Auto OEMs, Consumer) or above (Industrials, Machinery, Computing/Mobile, Contract Manufacturers, and ODMs). Trailing four-quarter inventory increased from last quarter.

Exhibit 2: Semi Customer DOI increased 9 days sequentially to 60 days vs a seasonal increase of 8 days. DOI is above the historical median and trailing 4 quarters increased from last quarter.

![](images/2ce4f8d5b0e71eae65d038287f4beaedb2ab4220a184d4d340f556e42c0e7f42.jpg)  
Source: FactSet, MS

Exhibit 3: Sequential and y/y change in semi customer inventory levels

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Q/Q</td><td colspan="2">Y/Y</td></tr><tr><td>Change in DOI</td><td>Change in $ Inventory</td><td>Change in DOI</td><td>Change in $ Inventory</td></tr><tr><td rowspan="11">Customers</td><td>AUTO OEMS</td><td>7</td><td>7%</td><td>-1</td><td>3%</td></tr><tr><td>AUTO SUPPLIERS</td><td>-1</td><td>1%</td><td>-2</td><td>2%</td></tr><tr><td>US INDUSTRIALS</td><td>8</td><td>4%</td><td>-4</td><td>7%</td></tr><tr><td>MACHINERY</td><td>5</td><td>7%</td><td>-10</td><td>9%</td></tr><tr><td>COMMUNICATIONS</td><td>17</td><td>11%</td><td>6</td><td>21%</td></tr><tr><td>COMPUTING/MOBILE</td><td>11</td><td>27%</td><td>3</td><td>42%</td></tr><tr><td>STORAGE</td><td>0</td><td>1%</td><td>-12</td><td>4%</td></tr><tr><td>CONSUMER</td><td>4</td><td>-5%</td><td>-6</td><td>-7%</td></tr><tr><td>CONTRACT MANUFACTURERS</td><td>13</td><td>8%</td><td>-5</td><td>24%</td></tr><tr><td>ODM&#x27;S</td><td>16</td><td>45%</td><td>13</td><td>108%</td></tr><tr><td>TOTAL</td><td>9</td><td>11%</td><td>-1</td><td>15%</td></tr></table>

Source: FactSet, MS

Distributor inventory decreased by 2 days q/q, below a seasonal increase of 4 days, but still sits 7 days above the historical median of 54 days. DOI declined q/q at WPG and Avnet, driven by COGS growth outpacing inventory growth (WPG: inventory +18% vs. COGS +21%; Avnet: inventory +3% vs. COGS +13%), while Arrow's DOI increased by 2 days. Absolute \$ of inventory increased for each distributor. Trailing 4-quarter decreased in the first quarter. (Arrow and Avnet are not covered by MS. WPG is covered by Daniel Yen.)

Exhibit 4: Distributor inventory is at 61 days, down 2 days q/q, below the seasonal increase of 4 days. DOI is 7 days above the historical median while trailing 4-quarters decreased sequentially.

![](images/a6a2858d28102801e8f3971965d36f500ab6b2d0d99200e5987bcabbd009d7c2.jpg)  
Source: FactSet, MS

Exhibit 5: Sequential and y/y change in distributor inventory levels

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Q/Q</td><td colspan="2">Y/Y</td></tr><tr><td>Change in DOI</td><td>Change in $ Inventory</td><td>Change in DOI</td><td>Change in $ Inventory</td></tr><tr><td>Distributors</td><td>Distributors</td><td>-2</td><td>11%</td><td>-13</td><td>11%</td></tr></table>

Source: FactSet, MS

Semiconductor company inventory days went up by 2 days q/q, below the seasonal increase of 5 days, and is now 23 days above the historical median. The DOI increase was driven by Smartphones (20.8%) and Foundries (10.8%), while other sectors showed marginal changes in the range of -3.5% (Semi Cap Equipment) to +1.9% (Computing). Change in absolute \$ inventory was broadly up across the board both q/q and y/y, with the exception of Memory holding \~flat y/y. Trailing 4-quarters DOI across semi companies slightly increased in 1Q.

Exhibit 6: Semiconductor Company inventory is at 114 days, up 2 days q/q, below the seasonal increase of 5 days. DOI is 23 days above the historical median and trailing 4-quarters increased.

Semiconductor Company (DOI)  
![](images/510fcf57805b2f576c8bad053e434a8c3e24c05c8c13f1460e858a1ddeffbe6c.jpg)  
Source: FactSet, MS

Exhibit 7: Sequential and y/y change in semi company inventory levels

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Q/Q</td><td colspan="2">Y/Y</td></tr><tr><td>Change in DOI</td><td>Change in $ Inventory</td><td>Change in DOI</td><td>Change in $ Inventory</td></tr><tr><td rowspan="9">Semi Companies</td><td>Computing</td><td>2</td><td>13%</td><td>31</td><td>54%</td></tr><tr><td>Analog/MCU</td><td>-2</td><td>0%</td><td>-9</td><td>5%</td></tr><tr><td>Smartphones/Networking/PLD&#x27;s/I</td><td>21</td><td>10%</td><td>28</td><td>31%</td></tr><tr><td>Memory</td><td>0</td><td>3%</td><td>-40</td><td>-1%</td></tr><tr><td>Foundries</td><td>8</td><td>6%</td><td>1</td><td>15%</td></tr><tr><td>Semi Cap Equipment</td><td>-6</td><td>0%</td><td>-24</td><td>5%</td></tr><tr><td>Components</td><td>0</td><td>10%</td><td>-2</td><td>25%</td></tr><tr><td>Others</td><td>1</td><td>3%</td><td>3</td><td>5%</td></tr><tr><td>TOTAL</td><td>2</td><td>5%</td><td>5</td><td>16%</td></tr></table>

Source: FactSet, MS

Total supply chain DOI across producers, distributors, and consumers increased 9 days q/q, increasing 10 days less than seasonality, and is now tracking 33 days above the historical median. Distributor and Company DOI both outperformed seasonality, with Distributors showing the greatest seasonal difference, decreasing by 2 days compared to a seasonal increase of 4. Customers DOI was \~in-line with seasonality, increasing by 1 day more than seasonal levels. Distributors in particular appear to be leaning out, driven by high COGS and revenue growth. Trailing 4-quarter DOI average was \~flat for the supply chain overall.

Exhibit 8: Total supply chain inventory increased 9 days q/q, less than the seasonal increase of 19 days. DOI is 33 days above the historical median, and trailing 4-quarters was flat.

![](images/e83deb534703e0c231c0062972efbf8bb5c27fe5ba6d585e2b1f32f40785f4e9.jpg)  
Source: FactSet, MS

# Semi Inventory Analysis: DOI \~flat at Customers, lower at Producers and Distributors.

## Customer Inventory

Semi customer inventory DOI increased more than seasonality. Absolute inventory levels increased q/q for all end markets except for Consumer. COGS decreased in Auto OEMs, US Industrials, Communications, Computing/Mobile, Consumer, and Contract Manufacturers, and increased in Auto Suppliers, Machinery, Storage, and ODM's.

Exhibit 9: Semi Customer Inventory Index increased 10.8% and trailing 4-quarters increased 3.7%.

Semi Customers (DOI)  
![](images/96c7dee05a8ba436cbc475a676abf4b0f90d69794a69e7593eb70d8114c51e8c.jpg)  
Source: FactSet, MS  
Exhibit 10: Semi Customer DOI increased 9 days sequentially to 60 days vs a seasonal increase of 8 days. DOI is above the historical median and trailing 4 quarters increased from last quarter.

![](images/95f52046d679744891b000822b53ce8e5ef54e471f9d6d55b7f8cb60a1e58da7.jpg)  
Source: FactSet, MS

Exhibit 11: Auto OEM DOI increased 7 days q/q and is above the historical median (56). Trailing 4-quarters decreased from last quarter.  
![](images/c1ec30ecb05c287e08ba37460a0ad88fdb6256ee508c324eba9d7992460f1158.jpg)  
Source: FactSet, MS

Exhibit 12: Auto suppliers DOI decreased 1 day q/q and is in-line with the historical median. Trailing 4-quarters increased q/q.  
![](images/d51e4b35d89e1efe0c9bfd728d00c2884c7c59175ebfbf3bbdd77bf22aa5be45.jpg)  
Source: FactSet, MS

Exhibit 13: Industrial DOI increased 8 days q/q, tracking 19 days above the historical median. Trailing 4-quarters declined q/q.  
![](images/6a8ac564f3e3920087e979e44b203d94ad879fa3478812a9cbcfdf693a8ced73.jpg)  
Source: FactSet, MS

Exhibit 14: Machinery DOI increased by 5 days q/q, tracking 13 days above the historical median. Trailing 4-quarters increased q/q.  
![](images/74aee4f3f78f9fbdef4662b33f72c65a3b5225fca0aef7715f8ff251944eba94.jpg)  
Source: FactSet, MS

Exhibit 15: Communications DOI increased 17 days q/q, tracking 23 days above the historical median. Trailing 4-quarters increased q/q.  
![](images/5950e143fa7333b22cf263b429237c6303b2c26bc32e541d18b4edaf328522f6.jpg)  
Source: FactSet, MS

Exhibit 16: Computing/Mobile company DOI increased by 11 days q/q, tracking 12 days above the historical median. Trailing 4-quarters increased sequentially.  
![](images/9937f9ea33b480d59ba14990ac7a378047a4e80df3f7167e45ee3bf361780aef.jpg)  
Source: FactSet, MS

Exhibit 17: Storage DOI remained flat q/q, now tracking 2 days below the historical median. Trailing 4-quarters increased from last quarter.  
![](images/fcb85995c1c679f111ca6e754c702d57f2b490f90d7a26a474ecdaeecf0e366b.jpg)  
Source: FactSet, MS

Exhibit 18: Consumer company DOI increased 4 days q/q, now tracking 2 days above the historical median. Trailing 4-quarters decreased.  
![](images/cf79fc6c236de70561ec658b964e76c79acc3615a6c114ecdabe05df86f7e429.jpg)  
Source: FactSet, MS

Exhibit 19: Contract manufacturers DOI increased 13 days q/q, tracking 7 days above the historical median. Trailing 4-quarters decreased from last quarter.  
![](images/859ebfc1560a11eb5b66d239ddd13b81f14445102305639af16410ac68189da7.jpg)  
Source: FactSet, MS

Exhibit 20: ODM DOI increased 16 days q/q, tracking 21 days above historical median. Trailing 4-quarter increased from last quarter.  
![](images/72c16b178cfafd503fde7d52b9c62e2fa82277be808f1ab5246c085bda165238.jpg)  
Source: FactSet, MS

## Distributor Inventory

Distributor DOI decreased 2 days q/q, outperforming a seasonal increase of 4 days. DOI is tracking 7 days above the historical median.

Exhibit 21: Distributor Inventory index increased 10.8% sequentially, and trailing 4-quarters increased from last quarter.

![](images/67b4c0386ec284dac784547b64db360bde07d38743bf5790130b1ecf28a6ad24.jpg)  
Source: FactSet, MS

Exhibit 22: Distributor inventory is at 61 days, down 2 days q/q, below the seasonal increase of 4 days. DOI is 7 days above the historical median while trailing 4-quarters decreased sequentially.

![](images/5d012f0a16eaedab23d4c13beecfadbb57a176fe541e6746ce95a330ced88739.jpg)  
Source: FactSet, MS

## Producer Inventory

Semiconductor company DOI increased less than seasonality. DOI decreased the most for Semi Cap Equipment and Analog/MCU while Memory was \~flat. Overall DOI momentum increased again consecutively.

Exhibit 23: Semi Company inventory index increased 5.2% q/q, with trailing 4-quarters increasing.

Semiconductor Company Inventory Index  
![](images/a6605d298b042b0c807d6d6117a63306e8d6fc247e4f8836bc6181cfe484b931.jpg)  
Source: FactSet, MS

Exhibit 24: Semiconductor Company inventory is at 114 days, up 2 days q/q, below the seasonal increase of 5 days. DOI is 23 days above the historical median and trailing 4-quarters slightly increased.

![](images/9721343bbddb1b12e947e3e79a14eb20c03892747c567fd6cefaae8c3da7a519.jpg)  
Source: FactSet, MS

Exhibit 25: Computing group DOI increased 2 days q/q, now tracking 28 days above the historical median. Trailing 4-quarters increased.  
![](images/d2b39147fd8254fbb3a549ba127bf6cb60d02418151deb1f89fba1255d3dd6cf.jpg)  
Source: FactSet, MS

Exhibit 27: Smartphone DOI increased 21 days q/q, now tracking 37 days above the historical median. Trailing 4-quarters increased q/q.  
Exhibit 26: Analog/MCU group DOI decreased 2 days q/q, now tracking 45 days above the historical median. Trailing 4-quarters fell q/q.  
![](images/b4dd242aa0e1be6feefc399f60304f02cb281efe6976b9104506c6a5365252b3.jpg)  
Source: FactSet, MS

![](images/2f5cbcdf354f5e2d413f462ecd10ca28bfde2432bc72ecb448edb12cfb2676e1.jpg)  
Exhibit 28: Memory group DOI remained flat q/q, now tracking 8 days above the historical median. Trailing 4-quarters decreased.  
Source: FactSet, MS

![](images/26b9f78b33a705cb8a24529b834f1ed4032b4c5c70ed06742a270e22d069605c.jpg)  
Source: FactSet, MS

Exhibit 29: Foundry group DOI increased by 8 days q/q, now tracking 8 days above the historical median. Trailing 4-quarters increased.  
![](images/9a9469a7997a773170358703499dff5089ca182f2bc2bfe76c6cd6e0488db0a7.jpg)  
Source: FactSet, MS

Exhibit 30: Semi Cap Equipment group DOI decreased 6 days q/q, now tracking 11 days above the historical median. Trailing 4-quarters decreased from last quarter.  
![](images/91308b1b69e7201311a03efd75c98d9fbdec0fb085bae5b49f4a39df69ea0568.jpg)  
Source: FactSet, MS

Exhibit 31: Components group DOI was \~flat q/q, now tracking 1 day above the historical median. Trailing 4-quarters increased from last quarter.  
![](images/4babd8cf070ffdc5a38508978f94ebfab45a3c8974a7a30147afc8b2c4575360.jpg)  
Source: FactSet, MS

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Shane Brett; Joseph Moore; Ella Tulchinsky; Ma

[中间内容因长度限制已省略]

 to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/30/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$580.91</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$28.72</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$69.62</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$85.80</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$86.23</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$397.17</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$483.02</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$377.75</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$221.00</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$82.41</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$139.63</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$53.26</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$297.89</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$91.20</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$1,154.29</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$17.92</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$200.09</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$281.03</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>++</td><td>$94.54</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$93.27</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>E (06/24/2026)</td><td>$184.79</td></tr><tr><td>Quantinuum (QNT.O)</td><td>E (06/29/2026)</td><td>$81.74</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$2,273.73</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$161.85</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$218.56</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$67.80</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$298.07</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$48.25</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$354.57</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$375.32</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$446.07</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: Semiconductor Capital Equipment

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/30/2026)</td></tr><tr><td colspan="3">Shane Brett</td></tr><tr><td>Applied Materials Inc. (AMAT.O)</td><td>E (05/18/2026)</td><td>$723.00</td></tr><tr><td>Camtek (CAMT.O)</td><td>E (12/01/2025)</td><td>$163.12</td></tr><tr><td>KLA Corp (KLAC.O)</td><td>O (01/15/2026)</td><td>$301.71</td></tr><tr><td>Lam Research Corp (LRCX.O)</td><td>O (05/18/2026)</td><td>$433.33</td></tr><tr><td>MKS Inc. (MKSI.O)</td><td>O (08/04/2024)</td><td>$444.80</td></tr><tr><td>Nova Ltd (NVMI.O)</td><td>E (12/01/2025)</td><td>$542.94</td></tr><tr><td>ONTO Innovation Inc (ONTO.N)</td><td>O (06/14/2026)</td><td>$378.45</td></tr><tr><td>Teradyne Inc (TER.O)</td><td>E (07/30/2025)</td><td>$483.84</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
