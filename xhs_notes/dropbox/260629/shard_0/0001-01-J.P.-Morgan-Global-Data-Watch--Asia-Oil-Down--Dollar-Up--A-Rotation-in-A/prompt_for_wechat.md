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
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# JPM

## Global Data Watch: Asia

## Oil Down, Dollar Up: A Rotation in Asian Central Banks

## EMAX: as energy prices fall, upside risks to 2H growth emerge

Underpinned by surging tech exports and production, EMAX growth has averaged over 6% q/q, saar – almost twice as strong as potential growth – over the last two quarters. While the region’s reliance on Middle Eastern energy made it particularly vulnerable to the conflict, the worst outcomes were avoided, as economies aggressively sourced energy from other sources, ran down reserves and transitioned to substitutes. Despite the energy headwinds, therefore, 2Q growth is still tracking close to trend. Our extant forecast calls for trend-like growth in the second half of the year, but we see growing upside risks from the confluence of two forces:

\- Tech production continues to hum along at a strong pace. While this week's May IP in Taiwan revealed that tech momentum has cooled from its previous scorching pace, it is still running at a very strong $30\%$ q/q, saar annualized in Taiwan. Similarly, 20-day exports from Korea point to continued strong export momentum, though recent tech gains have been more price led.

\- The end of the Middle East conflict and the sharp fall in crude prices significantly tempers the adverse terms of trade shock that the region was confronting. Headline inflation can be expected to soften, boosting household purchasing power, reducing the quantum of monetary tightening expected in certain economies (Philippines) and reinforcing our expectation that others in the region (RBI, BoT, MAS) won't be forced to hike, easing financial conditions in those economies.

To be sure, the sharp forecasted step down in 2H Chinese growth creates growth headwinds for the region. But the region's export exposure to China has reduced in recent years, and only Indonesia and Philippines saw a meaningful uptick in exports to China in the wake of above-trend Chinese growth in recent quarters. The impact of China downshifting is therefore likely to be more limited to a few economies. That said, disappointing Chinese domestic demand would increase the incentives to export excess capacity to the region and, indeed, around the world.

All told, however, upside risks to EMAX growth have emerged for 2H as energy prices correct and tech hums along.

Emerging Markets Asia, Economic and Policy Research

Sajjid Z Chinoy  
(91-22) 6157-3386  
sajjid.z.chinoy@JPM.com  
JPM Chase Bank, N.A., Mumbai Branch

Anusha Mital  
(91-22) 6157-4113  
anusha.mital@jpmchase.com  
JPM India Private Limited

## Research Notes

Korea: Fiscal implications of the tech windfall

## Data Watches

Japan

Australia and New Zealand

Greater China

Korea

ASEAN

India

Figure 1: EMAX tech IP and exports  
%3m/3m, saar, both scales. IP thru Apr, exports incl. May forecast  
![](images/d8060cd7dfa4ddd88eed27a31b355c7f42bb1b1749a84564a36796ac2e7bc9b9.jpg)  
Source: National sources, JPM

## Oil Down, Dollar Up: A Rotation in Asian Central Banks

With energy prices declining but the US Dollar strengthening, pressures on central banks will rotate in the region. Bank Indonesia is most vulnerable to a stronger dollar because of the pressures the rupiah faces and, even as we have another 25 bps of hikes in our forecast, risks of more tightening will increase if dollar strength continues. A stronger dollar and continued tech momentum also increase the risks that the Bank of Korea – which we already expect to hike by 100 bps over the next year – will have to hike more, and that the CBC in Taiwan hikes towards the end of the year.

The remaining central banks in the region are more focused on domestic growth-inflation dynamics and falling energy prices, and headline inflation will come as a relief. Odds have therefore increased that the BSP in the Philippines will have to hike less than the 6% terminal rate currently in our forecast. It also increases our conviction that the RBI, BoT and MAS stay on hold – bucking market pricing of multiple hikes for the RBI – even though a severe El Nino still remains an inflation risk.

## China: Weak May Fiscal Data Leaves Room for 2H Catch-Up

This week's fiscal data reinforces our view that China's 2Q slowdown reflects not only weak domestic demand but also a delayed fiscal impulse. Despite resilient revenue in May, fiscal expenditure contracted for a second month, with infrastructure outlays down $12.0\%$ oya; government-managed fund revenue and spending fell sharply as land sales weakened further. This helps explain the lack of infrastructure support and our forecast for 2Q GDP growth to slow to $3.3\%$ q/q saar. That said, the fiscal undershoot leaves the mid-year outlook less negative: fiscal deposits rose to the second-highest May level in the past decade, and special local government bond issuance has rebounded in June, creating room for faster policy execution in 2H.

Our 2H view rests on a better, though still uneven, growth mix. We forecast GDP growth at $3.5\%$ q/q saar in 3Q and $3.7\%$ in 4Q, leaving full-year 2026 growth at $4.7\%$ y/y. Fiscal execution should improve, and global IP strength and the AI capex cycle should continue to support Chinese exports and high-tech/equipment manufacturing, partly offsetting weak consumption. The reopening of the Strait of Hormuz and lower oil prices should ease energy and supply-chain pressures, helping producer sentiment.

For next week's PMIs, we expect the NBS manufacturing PMI to edge up to 50.2 and the RatingDog PMI to 52.1, with production still modestly expansionary but new orders remaining soft. Downside risks are concentrated in weak private investment, soft consumption, and the ongoing housing slump. If the June activity data released in July are very weak, policy response is likely to become more visible after the late-July Politburo meeting: faster project approvals, quicker deployment of special local government bond proceeds, a more aggressive drawdown of fiscal deposits, expanded policy-bank financing, and targeted support for infrastructure and housing stabilization. Monetary policy should remain supportive, but fiscal policy is likely to do the heavier lifting in 2H.

Table 1: EM Asia data release

<table><tr><td>Date</td><td colspan="2">Market</td><td>Data</td><td>Period</td><td>Unit</td><td>JPM</td><td>Consensus</td><td>Previous</td></tr><tr><td>Mon, 29-Jun</td><td>IN</td><td>IP</td><td></td><td>May</td><td>%oya</td><td>3.7</td><td>3.9</td><td>4.9</td></tr><tr><td rowspan="6">Tue, 30-Jun</td><td>KR</td><td>IP</td><td></td><td>May</td><td>%oya</td><td>1.5</td><td>4.0</td><td>1.5</td></tr><tr><td>PH</td><td>Trade balance</td><td></td><td>May</td><td>US$bn</td><td>-5.2</td><td>-5.2</td><td>-6.0</td></tr><tr><td>PH</td><td>Exports</td><td></td><td>May</td><td>%oya</td><td>2.5</td><td>5.1</td><td>6.3</td></tr><tr><td>PH</td><td>Imports</td><td></td><td>May</td><td>%oya</td><td>15.4</td><td>19.6</td><td>22.4</td></tr><tr><td>CN</td><td>PMI mfg. (NBS)</td><td></td><td>Jun</td><td>Index</td><td>50.2</td><td>50.1</td><td>50.0</td></tr><tr><td>TH</td><td>Mfg. production</td><td></td><td>May</td><td>%oya</td><td>-0.9</td><td>-</td><td>-0.4</td></tr><tr><td rowspan="11">Wed, 01-Jul</td><td>TW</td><td>PMI mfg.</td><td></td><td>Jun</td><td>Index</td><td>56.5</td><td>-</td><td>56.1</td></tr><tr><td>KR</td><td>Trade balance</td><td></td><td>Jun</td><td>US$bn</td><td>33.3</td><td>33.1</td><td>26.9</td></tr><tr><td>KR</td><td>Exports</td><td></td><td>Jun</td><td>%oya</td><td>60.4</td><td>60.6</td><td>53.2</td></tr><tr><td>KR</td><td>Imports</td><td></td><td>Jun</td><td>%oya</td><td>23.2</td><td>23.9</td><td>20.8</td></tr><tr><td>KR</td><td>PMI mfg.</td><td></td><td>Jun</td><td>Index</td><td>55.0</td><td>-</td><td>54.8</td></tr><tr><td>CN</td><td>PMI mfg.(RatingDog)</td><td></td><td>Jun</td><td>Index</td><td>52.1</td><td>52.0</td><td>51.8</td></tr><tr><td>IN</td><td>PMI mfg.</td><td></td><td>Jun</td><td>Index</td><td>-</td><td>-</td><td>54.5</td></tr><tr><td>ID</td><td>Trade balance</td><td></td><td>May</td><td>US$bn</td><td>2.5</td><td>1.1</td><td>0.1</td></tr><tr><td>ID</td><td>Exports</td><td></td><td>May</td><td>%oya</td><td>0.2</td><td>6.4</td><td>22.0</td></tr><tr><td>ID</td><td>Imports</td><td></td><td>May</td><td>%oya</td><td>9.3</td><td>23.5</td><td>22.5</td></tr><tr><td>ID</td><td>CPI</td><td></td><td>Jun</td><td>%oya</td><td>3.1</td><td>3.2</td><td>3.1</td></tr><tr><td rowspan="3">Thu, 02-Jul</td><td>KR</td><td>CPI</td><td></td><td>Jun</td><td>%oya</td><td>3.2</td><td>3.2</td><td>3.1</td></tr><tr><td>HK</td><td>Retail sales</td><td></td><td>May</td><td>%oya</td><td>4.8</td><td>-</td><td>6.4</td></tr><tr><td>SG</td><td>PMI</td><td></td><td>Jun</td><td>Index</td><td>51.2</td><td>-</td><td>51.0</td></tr><tr><td colspan="9">Fri, 03-Jul</td></tr></table>

Source: Bloomberg Finance L.P. and JPM forecasts

## Regional Economic Outlook in Summary

<table><tr><td rowspan="3"></td><td colspan="3">2024 Nominal GDP, US$</td><td colspan="3">Real GDP</td><td colspan="3">Consumer prices</td></tr><tr><td rowspan="2">Total billion</td><td rowspan="2">% of region</td><td rowspan="2">per capita</td><td colspan="3">% year-on-year</td><td colspan="3">% year-on-year</td></tr><tr><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>Japan</td><td>4,019</td><td>n.a.</td><td>33,820</td><td>-0.2</td><td>1.1</td><td>0.6</td><td>2.7</td><td>3.2</td><td>2.1</td></tr><tr><td>Australia</td><td>1,794</td><td>n.a.</td><td>65,701</td><td>1.0</td><td>2.0</td><td>2.0</td><td>3.2</td><td>2.8</td><td>4.2</td></tr><tr><td>New Zealand</td><td>258</td><td>n.a.</td><td>48,929</td><td>-0.3</td><td>0.2</td><td>2.1</td><td>2.9</td><td>2.8</td><td>3.5</td></tr><tr><td>Emerging Asia</td><td>29,492</td><td>100.0</td><td>8,507</td><td>5.0</td><td>5.2</td><td>4.9</td><td>1.3</td><td>0.7</td><td>2.0</td></tr><tr><td>ex China and India</td><td>6,891</td><td>23.4</td><td>11,722</td><td>4.0</td><td>4.0</td><td>4.7</td><td>2.1</td><td>1.6</td><td>2.9</td></tr><tr><td>China</td><td>18,752</td><td>63.6</td><td>13,453</td><td>4.9</td><td>5.0</td><td>4.7</td><td>0.2</td><td>0.0</td><td>1.0</td></tr><tr><td>Hong Kong SAR, China</td><td>407</td><td>1.4</td><td>54,445</td><td>2.6</td><td>3.6</td><td>3.4</td><td>1.7</td><td>1.4</td><td>1.6</td></tr><tr><td>Taiwan, China</td><td>797</td><td>2.7</td><td>34,252</td><td>5.3</td><td>8.8</td><td>9.9</td><td>2.2</td><td>1.7</td><td>2.0</td></tr><tr><td>Korea</td><td>1,875</td><td>6.4</td><td>36,239</td><td>2.2</td><td>1.1</td><td>3.7</td><td>2.3</td><td>2.1</td><td>3.0</td></tr><tr><td>India</td><td>3,849</td><td>13.1</td><td>2,592</td><td>7.1</td><td>7.7</td><td>6.5</td><td>4.9</td><td>2.1</td><td>5.0</td></tr><tr><td>Indonesia</td><td>1,398</td><td>4.7</td><td>4,958</td><td>5.0</td><td>5.1</td><td>4.7</td><td>2.3</td><td>1.9</td><td>3.4</td></tr><tr><td>Malaysia</td><td>422</td><td>1.4</td><td>12,619</td><td>5.1</td><td>5.2</td><td>5.0</td><td>1.8</td><td>1.4</td><td>1.9</td></tr><tr><td>Philippines</td><td>462</td><td>1.6</td><td>4,089</td><td>5.7</td><td>4.4</td><td>4.0</td><td>3.2</td><td>1.6</td><td>6.3</td></tr><tr><td>Singapore</td><td>547</td><td>1.9</td><td>94,897</td><td>5.3</td><td>5.0</td><td>4.6</td><td>2.4</td><td>0.9</td><td>2.1</td></tr><tr><td>Thailand</td><td>527</td><td>1.8</td><td>7,387</td><td>2.9</td><td>2.4</td><td>2.1</td><td>0.4</td><td>-0.1</td><td>2.4</td></tr><tr><td>Vietnam</td><td>456</td><td>1.5</td><td>4,536</td><td>7.1</td><td>7.9</td><td>7.3</td><td>3.6</td><td>3.3</td><td>4.6</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="3">Current account balance US$ billion</td><td colspan="3">Current account % of GDP</td><td colspan="3">Foreign reserves US$ billion</td></tr><tr><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>Japan</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>4.6</td><td>4.8</td><td>3.6</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Australia</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-2.2</td><td>-2.7</td><td>-2.7</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>New Zealand</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-4.8</td><td>-3.7</td><td>-4.3</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Emerging Asia</td><td>787.8</td><td>1186.0</td><td>1299.9</td><td>2.6</td><td>3.8</td><td>3.9</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>ex China and India</td><td>386.9</td><td>463.1</td><td>600.8</td><td>5.5</td><td>6.1</td><td>8.0</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>China</td><td>423.9</td><td>747.9</td><td>754.1</td><td>2.3</td><td>3.8</td><td>3.6</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Hong Kong SAR, China</td><td>52.5</td><td>54.7</td><td>47.3</td><td>12.9</td><td>12.8</td><td>10.5</td><td>421</td><td>426</td><td>428</td></tr><tr><td>Taiwan, China</td><td>112.7</td><td>139.3</td><td>135.2</td><td>14.1</td><td>15.1</td><td>13.6</td><td>578</td><td>585</td><td>592</td></tr><tr><td>Korea</td><td>100.0</td><td>129.0</td><td>300.8</td><td>5.3</td><td>6.9</td><td>14.8</td><td>409</td><td>422</td><td>426</td></tr><tr><td>India</td><td>-23.0</td><td>-25.0</td><td>-55.0</td><td>-0.6</td><td>-0.6</td><td>-1.4</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Indonesia</td><td>-8.7</td><td>-10.2</td><td>-14.8</td><td>-0.6</td><td>-0.8</td><td>-1.0</td><td>149</td><td>145</td><td>140</td></tr><tr><td>Malaysia</td><td>7.2</td><td>9.7</td><td>14.9</td><td>1.7</td><td>2.1</td><td>2.8</td><td>124</td><td>127</td><td>130</td></tr><tr><td>Philippines</td><td>-17.5</td><td>-16.3</td><td>-21.9</td><td>-3.8</td><td>-3.3</td><td>-4.4</td><td>95</td><td>91</td><td>74</td></tr><tr><td>Singapore</td><td>98.5</td><td>100.9</td><td>128.0</td><td>17.2</td><td>16.7</td><td>19.8</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Thailand</td><td>11.6</td><td>22.8</td><td>2.3</td><td>2.2</td><td>3.9</td><td>0.4</td><td>217</td><td>249</td><td>270</td></tr><tr><td>Vietnam</td><td>30.5</td><td>33.1</td><td>9.1</td><td>6.8</td><td>6.6</td><td>1.7</td><td>83</td><td>87</td><td>82</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="3">External debt % of GDP, end of period</td><td colspan="3">Short-term foreign debt US$ billion, end of period</td><td colspan="3">Government balance % of GDP, end of period</td></tr><tr><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>Japan</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-6.1</td><td>-6.7</td><td>-6.9</td></tr><tr><td>Australia</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>0.0</td><td>-0.4</td><td>-0.6</td></tr><tr><td>New Zealand</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-2.6</td><td>-2.4</td><td>-2.7</td></tr><tr><td>China</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-3.0</td><td>-4.0</td><td>-4.0</td></tr><tr><td>Hong Kong SAR, China</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-1.8</td><td>0.1</td><td>0.6</td></tr><tr><td>Taiwan, China</td><td>26.2</td><td>23.5</td><td>22.5</td><td>207</td><td>213</td><td>221</td><td>-0.6</td><td>-1.0</td><td>-1.6</td></tr><tr><td>Korea</td><td>35.9</td><td>38.2</td><td>39.8</td><td>147</td><td>179</td><td>179</td><td>-1.7</td><td>-1.8</td><td>1.2</td></tr><tr><td>India</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-8.3</td><td>-7.9</td><td>-7.7</td></tr><tr><td>Indonesia</td><td>27.4</td><td>25.3</td><td>23.6</td><td>43</td><td>43</td><td>43</td><td>-2.7</td><td>-2.9</td><td>-3.0</td></tr><tr><td>Malaysia</td><td>50.6</td><td>47.3</td><td>43.8</td><td>119</td><td>129</td><td>139</td><td>-4.3</td><td>-3.8</td><td>-3.5</td></tr><tr><td>Philippines</td><td>28.5</td><td>30.6</td><td>33.6</td><td>21</td><td>22</td><td>27</td><td>-5.7</td><td>-5.6</td><td>-6.0</td></tr><tr><td>Singapore</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>0.4</td><td>0.4</td><td>0.2</td></tr><tr><td>Thailand</td><td>37.0</td><td>34.1</td><td>32.1</td><td>86</td><td>75</td><td>75</td><td>-4.0</td><td>-4.7</td><td>-4.5</td></tr><tr><td>Vietnam</td><td>46.1</td><td>47.1</td><td>48.1</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-3.6</td><td>-3.8</td><td>-4.2</td></tr></table>

Source: National statistics authorities and JPM

Key economic statistics

<table><tr><td></td><td></td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td></tr><tr><td colspan="10">Real GDP, %-ch over 1 quarter, saar</td></tr><tr><td>Japan</td><td></td><td>2.0</td><td>1.1</td><td>-2.3</td><td>0.7</td><td>1.8</td><td>0.2</td><td>1.0</td><td>0.8</td></tr><tr><td>Australia</td><td></td><td>1.0</td><td>3.9</td><td>1.5</td><td>3.5</td><td>1.1</td><td>1.6</td><td>1.5</td><td>1.9</td></tr><tr><td>New Zealand</td><td></td><td>3.5</td><td>-2.6</td><td>3.5</td><td>1.8</td><td>3.2</td><td>1.2</td><td>3.4</td><td>1.2</td></tr><tr><td>Emerging Asia</td><td></td><td>4.7</td><td>5.1</td><td>4.5</td><td>5.8</td><td>6.7</td><td>3.5</td><td>3.7</td><td>3.9</td></tr><tr><td>ex China and India</td><td></td><td>2.6</td><td>5.7</td><td>5.0</td><td>6.6</td><td>6.0</td><td>3.3</td><td>3.4</td><td>3.2</td></tr><tr><td>China</td><td></td><td>4.9</td><td>4.2</td><td>3.7</td><td>5.2</td><td>6.7</td><td>3.3</td><td>3.5</td><td>3.7</td></tr><tr><td>Hong Kong SAR, China</td><td></td><td>4.6</td><td>3.3</td><td>3.8</td><td>4.3</td><td>12.2</td><td>3.0</td><td>2.8</td><td>2.8</td></tr><tr><td>Taiwan, China</td><td></td><td>3.7</td><td>16.3</td><td>6.7</td><td>28.7</td><td>6.9</td><td>4.5</td><td>3.2</td><td>3.2</td></tr><tr><td>Korea</td><td></td><td>-0.7</td><td>2.6</td><td>5.6</td><td>-0.4</td><td>7.5</td><td>2.0</td><td>4.0</td><td>3.0</td></tr><tr><td>India</td><td></td><td>7.2</td><td>8.5</td><td>7.5</td><td>7.5</td><td>8.0</td><td>5.1</td><td>5.0</td><td>6.2</td></tr><tr><td>Indonesia</td><td></td><td>4.9</td><td>5.5</td><td>5.3</td><td>5.7</td><td>5.7</td><td>3.6</td><td>3.0</td><td>2.6</td></tr><tr><td>Malaysia</td><td></td><td>4.3</td><td>7.3</td><td>7.0</td><td>5.9</td><td>1.7</td><td>7.0</td><td>5.0</td><td>4.5</td></tr><tr><td>Philippines</td><td></td><td>4.9</td><td>3.7</td><td>1.4</td><td>2.4</td><td>3.8</td><td>4.9</td><td>5.7</td><td>8.2</td></tr><tr><td>Singapore</td><td></td><td>2.5</td><td>7.3</td><td>7.8</td><td>5.2</td><td>3.9</td><td>5.0</td><td>2.0</td><td>

[中间内容因长度限制已省略]

aterial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
