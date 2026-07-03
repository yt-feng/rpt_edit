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
- 已识别机构名：`Citi`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Auto Manufacturers

## Bi-Monthly Duo NEV Pricing Trends (Discount & MSRP): End-Jun-26

## CITI'S TAKE

In this bimonthly pricing trend report, we monitor the NEV-PV pricing of major OEMs based on data from Top 30 cities collected by Thinkercar. Discount is calculated as the difference between 4S shop retail price and the MSRP. In the second half of Jun-26, China NEV-PV sector weighted average retail discount was -0.6ppt MoM to 6.2% (versus end-May). NEV-PV sector weighted average MSRP was +0.4% MoM to Rmb177,653.

## NEV brands

— Tesla: retail discount stands at 0.9% (+0.0ppt MoM); MSRP at Rmb289,540 (flat MoM)

— Nio: retail discount stands at 2.1% (-0.4ppt MoM); MSRP at Rmb320,307 (+2.3% MoM)

— Xpeng: retail discount stands at 3.6% (+0.0ppt MoM); MSRP at Rmb178,334 (flat MoM)

— Li Auto: retail discount stands at 5.9% (-0.3ppt MoM); MSRP at Rmb294,286 (+1.0% MoM)

— AITO: retail discount stands at 1.0%; MSRP at Rmb319,310

— Leapmotor: retail discount stands at 4.7% (-1.6ppt MoM); MSRP at Rmb122,473 (-0.3% MoM)

## Traditional local brands (for NEV models only)

— BYD: retail discount stands at 7.0% (+0.2ppt MoM); MSRP at Rmb131,726 (-0.2% MoM)

— Geely: retail discount stands at 9.9% (-2.6ppt MoM); MSRP at Rmb113,004 (+0.1% MoM)

— Great Wall: retail discount stands at 6.4% (+0.6ppt MoM); MSRP at Rmb267,145 (-0.3% MoM)

## Traditional luxury brands

— Beijing Mercedes: NEV+ICE weighted-average retail price at Rmb294,980 (-1.9% MoM/-0.8% YoY)

— Brilliance BMW: NEV+ICE weighted-average retail price at Rmb286,616 (-1.7% MoM/+0.4% YoY)

— Audi Group: NEV+ICE weighted-average retail price at Rmb241,706 (-1.0% MoM/-5.1% YoY)

## See Figure 6-11 for CPCA discount summary

Jeff Chung $^{AC}$

+852-2501-2787

jeff.m.chung@citi.com

Kyle Wu

+852-2501-8483

kyle.wu@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations.

Figure 1. NEV-PV retail discounts by OEMs

<table><tr><td></td><td>15-Feb-26</td><td>28-Feb-26</td><td>15-Mar-26</td><td>31-Mar-26</td><td>15-Apr-26</td><td>30-Apr-26</td><td>15-May-26</td><td>31-May-26</td><td>15-Jun-26</td><td>30-Jun-26</td></tr><tr><td colspan="11">Weighted average retail discount</td></tr><tr><td>Tesla</td><td>0.8%</td><td>0.8%</td><td>0.7%</td><td>0.7%</td><td>0.3%</td><td>0.3%</td><td>0.9%</td><td>0.9%</td><td>0.9%</td><td>0.9%</td></tr><tr><td>Nio</td><td>1.9%</td><td>1.9%</td><td>3.3%</td><td>3.3%</td><td>2.8%</td><td>2.8%</td><td>2.5%</td><td>2.5%</td><td>2.5%</td><td>2.1%</td></tr><tr><td>Xpeng</td><td>6.4%</td><td>6.4%</td><td>6.8%</td><td>6.7%</td><td>3.9%</td><td>4.4%</td><td>4.4%</td><td>3.6%</td><td>3.6%</td><td>3.6%</td></tr><tr><td>Li Auto</td><td>5.3%</td><td>5.3%</td><td>6.6%</td><td>6.6%</td><td>6.4%</td><td>6.4%</td><td>6.5%</td><td>6.1%</td><td>5.8%</td><td>5.9%</td></tr><tr><td>AITO</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.0%</td><td>1.0%</td></tr><tr><td>Leapmotor</td><td>7.9%</td><td>9.2%</td><td>9.2%</td><td>9.2%</td><td>7.9%</td><td>7.9%</td><td>6.0%</td><td>6.3%</td><td>6.5%</td><td>4.7%</td></tr><tr><td>BYD</td><td>7.3%</td><td>7.5%</td><td>8.3%</td><td>8.6%</td><td>8.2%</td><td>7.8%</td><td>6.8%</td><td>6.9%</td><td>6.9%</td><td>7.0%</td></tr><tr><td>Geely</td><td>10.0%</td><td>10.2%</td><td>11.3%</td><td>11.7%</td><td>12.4%</td><td>12.6%</td><td>12.3%</td><td>12.5%</td><td>9.8%</td><td>9.9%</td></tr><tr><td>Great Wall</td><td>4.4%</td><td>4.4%</td><td>4.4%</td><td>4.5%</td><td>7.3%</td><td>7.2%</td><td>5.8%</td><td>5.9%</td><td>6.4%</td><td>6.4%</td></tr><tr><td>Beijing Mercedes</td><td>31.1%</td><td>31.2%</td><td>31.1%</td><td>31.2%</td><td>35.3%</td><td>35.7%</td><td>28.0%</td><td>28.1%</td><td>28.1%</td><td>28.1%</td></tr><tr><td>Brilliance BMW</td><td>38.2%</td><td>38.3%</td><td>37.5%</td><td>37.6%</td><td>33.2%</td><td>33.5%</td><td>33.1%</td><td>33.2%</td><td>32.8%</td><td>33.1%</td></tr><tr><td>Audi Group</td><td>13.9%</td><td>19.2%</td><td>14.9%</td><td>14.9%</td><td>19.4%</td><td>16.5%</td><td>13.4%</td><td>13.5%</td><td>13.5%</td><td>16.4%</td></tr><tr><td>NEV-PV sector weighted average discount</td><td>6.1%</td><td>6.3%</td><td>7.4%</td><td>7.6%</td><td>7.8%</td><td>7.7%</td><td>6.7%</td><td>6.8%</td><td>6.3%</td><td>6.2%</td></tr><tr><td colspan="11">Weighted average retail discount MoM change</td></tr><tr><td>Tesla</td><td>0.5ppt</td><td>0.5ppt</td><td>-0.1ppt</td><td>-0.1ppt</td><td>-0.4ppt</td><td>-0.4ppt</td><td>0.6ppt</td><td>0.6ppt</td><td>0.0ppt</td><td>0.0ppt</td></tr><tr><td>Nio</td><td>0.4ppt</td><td>0.4ppt</td><td>1.4ppt</td><td>1.4ppt</td><td>-0.5ppt</td><td>-0.5ppt</td><td>-0.3ppt</td><td>-0.3ppt</td><td>0.0ppt</td><td>-0.4ppt</td></tr><tr><td>Xpeng</td><td>3.1ppt</td><td>3.1ppt</td><td>0.3ppt</td><td>0.3ppt</td><td>-2.8ppt</td><td>-2.4ppt</td><td>0.0ppt</td><td>-0.8ppt</td><td>0.1ppt</td><td>0.0ppt</td></tr><tr><td>Li Auto</td><td>-0.1ppt</td><td>-0.1ppt</td><td>1.3ppt</td><td>1.3ppt</td><td>-0.1ppt</td><td>-0.1ppt</td><td>0.1ppt</td><td>-0.3ppt</td><td>-0.4ppt</td><td>-0.3ppt</td></tr><tr><td>AITO</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Leapmotor</td><td>0.5ppt</td><td>1.8ppt</td><td>0.0ppt</td><td>0.0ppt</td><td>-1.4ppt</td><td>-1.3ppt</td><td>-2.0ppt</td><td>-1.7ppt</td><td>0.2ppt</td><td>-1.6ppt</td></tr><tr><td>BYD</td><td>0.7ppt</td><td>0.9ppt</td><td>0.8ppt</td><td>1.1ppt</td><td>-0.4ppt</td><td>-0.9ppt</td><td>-1.0ppt</td><td>-0.9ppt</td><td>0.0ppt</td><td>0.2ppt</td></tr><tr><td>Geely</td><td>0.3ppt</td><td>0.5ppt</td><td>1.1ppt</td><td>1.5ppt</td><td>0.7ppt</td><td>0.9ppt</td><td>-0.3ppt</td><td>-0.1ppt</td><td>-2.7ppt</td><td>-2.6ppt</td></tr><tr><td>Great Wall</td><td>0.2ppt</td><td>0.3ppt</td><td>0.0ppt</td><td>0.1ppt</td><td>2.8ppt</td><td>2.7ppt</td><td>-1.4ppt</td><td>-1.3ppt</td><td>0.5ppt</td><td>0.6ppt</td></tr><tr><td>Beijing Mercedes</td><td>1.6ppt</td><td>1.7ppt</td><td>-0.1ppt</td><td>0.0ppt</td><td>4.1ppt</td><td>4.5ppt</td><td>-7.7ppt</td><td>-7.6ppt</td><td>0.0ppt</td><td>0.0ppt</td></tr><tr><td>Brilliance BMW</td><td>-1.0ppt</td><td>-1.0ppt</td><td>-0.8ppt</td><td>-0.7ppt</td><td>-4.4ppt</td><td>-4.1ppt</td><td>-0.3ppt</td><td>-0.3ppt</td><td>-0.4ppt</td><td>-0.1ppt</td></tr><tr><td>Audi Group</td><td>-1.8ppt</td><td>3.5ppt</td><td>-4.3ppt</td><td>-4.2ppt</td><td>4.5ppt</td><td>1.6ppt</td><td>-3.1ppt</td><td>-3.0ppt</td><td>0.0ppt</td><td>2.9ppt</td></tr><tr><td>Changes in sector weighted average discount</td><td>0.1ppt</td><td>0.3ppt</td><td>1.1ppt</td><td>1.3ppt</td><td>0.2ppt</td><td>0.1ppt</td><td>-0.9ppt</td><td>-0.9ppt</td><td>-0.4ppt</td><td>-0.6ppt</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 2. Sector weighted average NEV-PV discount vs MSRP  
![](images/91d0e7c9d76e88a047124b8857fd721de970e7b8a3a010e086af8f272a177cf2.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 3. NEV-PV retail MSRP by OEMs

<table><tr><td></td><td>15-Feb-26</td><td>28-Feb-26</td><td>15-Mar-26</td><td>31-Mar-26</td><td>15-Apr-26</td><td>30-Apr-26</td><td>15-May-26</td><td>31-May-26</td><td>15-Jun-26</td><td>30-Jun-26</td></tr><tr><td colspan="11">Weighted average MSRP</td></tr><tr><td>Tesla</td><td>295,288</td><td>295,288</td><td>293,475</td><td>293,475</td><td>294,716</td><td>294,716</td><td>289,540</td><td>289,540</td><td>289,540</td><td>289,540</td></tr><tr><td>Nio</td><td>345,919</td><td>345,919</td><td>330,031</td><td>330,031</td><td>317,320</td><td>320,799</td><td>313,047</td><td>313,047</td><td>320,589</td><td>320,307</td></tr><tr><td>Xpeng</td><td>191,933</td><td>191,933</td><td>187,516</td><td>186,612</td><td>178,019</td><td>178,019</td><td>164,596</td><td>178,334</td><td>178,334</td><td>178,334</td></tr><tr><td>Li Auto</td><td>282,728</td><td>282,728</td><td>282,677</td><td>282,677</td><td>282,865</td><td>282,865</td><td>288,739</td><td>291,513</td><td>294,286</td><td>294,286</td></tr><tr><td>AITO</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>326,698</td><td>319,310</td></tr><tr><td>Leapmotor</td><td>130,589</td><td>130,589</td><td>129,277</td><td>129,277</td><td>118,784</td><td>123,975</td><td>122,852</td><td>122,852</td><td>122,852</td><td>122,473</td></tr><tr><td>BYD</td><td>137,757</td><td>137,757</td><td>128,236</td><td>128,083</td><td>131,935</td><td>132,570</td><td>131,481</td><td>131,975</td><td>131,720</td><td>131,726</td></tr><tr><td>Geely</td><td>125,921</td><td>125,921</td><td>110,174</td><td>110,240</td><td>106,513</td><td>107,090</td><td>111,118</td><td>112,890</td><td>112,563</td><td>113,004</td></tr><tr><td>Great Wall</td><td>267,758</td><td>267,758</td><td>258,235</td><td>258,235</td><td>231,473</td><td>255,107</td><td>225,924</td><td>267,995</td><td>267,995</td><td>267,145</td></tr><tr><td>Beijing Mercedes</td><td>454,328</td><td>454,328</td><td>422,375</td><td>422,375</td><td>420,636</td><td>418,376</td><td>375,874</td><td>375,874</td><td>375,874</td><td>375,874</td></tr><tr><td>Brilliance BMW</td><td>320,878</td><td>320,878</td><td>321,588</td><td>321,588</td><td>301,729</td><td>301,729</td><td>297,410</td><td>297,410</td><td>297,410</td><td>297,410</td></tr><tr><td>Audi Group</td><td>290,536</td><td>290,536</td><td>286,218</td><td>286,218</td><td>324,674</td><td>317,034</td><td>327,624</td><td>327,624</td><td>327,944</td><td>327,944</td></tr><tr><td>NEV-PV sector weighted average MSRP</td><td>205,131</td><td>205,131</td><td>185,580</td><td>185,490</td><td>171,642</td><td>173,654</td><td>173,515</td><td>176,911</td><td>177,686</td><td>177,653</td></tr></table>

<table><tr><td colspan="11">Weighted average MSRP MoM change</td></tr><tr><td>Tesla</td><td>1.8%</td><td>1.8%</td><td>-0.6%</td><td>-0.6%</td><td>0.4%</td><td>0.4%</td><td>-1.8%</td><td>-1.8%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Nio</td><td>-2.3%</td><td>-2.3%</td><td>-4.6%</td><td>-4.6%</td><td>-3.9%</td><td>-2.8%</td><td>-2.4%</td><td>-2.4%</td><td>2.4%</td><td>2.3%</td></tr><tr><td>Xpeng</td><td>-7.9%</td><td>-7.9%</td><td>-2.3%</td><td>-2.8%</td><td>-4.6%</td><td>-4.6%</td><td>-7.5%</td><td>0.2%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Li Auto</td><td>-0.1%</td><td>-0.1%</td><td>0.0%</td><td>0.0%</td><td>0.1%</td><td>0.1%</td><td>2.1%</td><td>3.1%</td><td>1.0%</td><td>1.0%</td></tr><tr><td colspan="11">AITO</td></tr><tr><td>Leapmotor</td><td>1.3%</td><td>1.3%</td><td>-1.0%</td><td>-1.0%</td><td>-8.1%</td><td>-4.1%</td><td>-0.9%</td><td>-0.9%</td><td>0.0%</td><td>-0.3%</td></tr><tr><td>BYD</td><td>-3.9%</td><td>-3.9%</td><td>-6.9%</td><td>-7.0%</td><td>3.0%</td><td>3.5%</td><td>-0.8%</td><td>-0.4%</td><td>-0.2%</td><td>-0.2%</td></tr><tr><td>Geely</td><td>1.1%</td><td>1.1%</td><td>-12.5%</td><td>-12.5%</td><td>-3.4%</td><td>-2.9%</td><td>3.8%</td><td>5.4%</td><td>-0.3%</td><td>0.1%</td></tr><tr><td>Great Wall</td><td>0.9%</td><td>0.9%</td><td>-3.6%</td><td>-3.6%</td><td>-10.4%</td><td>-1.2%</td><td>-11.4%</td><td>5.1%</td><td>0.0%</td><td>-0.3%</td></tr><tr><td>Beijing Mercedes</td><td>-0.3%</td><td>-0.3%</td><td>-7.0%</td><td>-7.0%</td><td>-0.4%</td><td>-0.9%</td><td>-10.2%</td><td>-10.2%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Brilliance BMW</td><td>-6.7%</td><td>-6.7%</td><td>0.2%</td><td>0.2%</td><td>-6.2%</td><td>-6.2%</td><td>-1.4%</td><td>-1.4%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Audi Group</td><td>-13.6%</td><td>-13.6%</td><td>-1.5%</td><td>-1.5%</td><td>13.4%</td><td>10.8%</td><td>3.3%</td><td>3.3%</td><td>0.1%</td><td>0.1%</td></tr><tr><td>Changes in sector weighted average MSRP</td><td>1.9%</td><td>1.9%</td><td>-9.5%</td><td>-9.6%</td><td>-7.5%</td><td>-6.4%</td><td>-0.1%</td><td>1.9%</td><td>0.4%</td><td>0.4%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Figure 4. German luxury ICE discount summary

<table><tr><td></td><td>30-Jun-26</td><td>31-May-26</td><td>Jun-26 MoM</td><td>30-Jun-25</td><td>Jun-26 YoY</td><td>31-May-25</td><td>Jun-25 MoM</td></tr><tr><td>German Luxury ICE (weighted avg)</td><td>27.2%</td><td>26.1%</td><td>1.2ppt</td><td>34.0%</td><td>-6.8ppt</td><td>33.0%</td><td>1.0ppt</td></tr><tr><td colspan="8">By brand</td></tr><tr><td>Brilliance BMW</td><td>23.3%</td><td>21.9%</td><td>1.4ppt</td><td>34.6%</td><td>-11.3ppt</td><td>32.8%</td><td>1.8ppt</td></tr><tr><td>Beijing Mercedes</td><td>25.0%</td><td>23.5%</td><td>1.5ppt</td><td>31.6%</td><td>-6.7ppt</td><td>31.1%</td><td>0.5ppt</td></tr><tr><td>Audi Group</td><td>32.8%</td><td>32.2%</td><td>0.6ppt</td><td>35.5%</td><td>-2.7ppt</td><td>34.9%</td><td>0.6ppt</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Thinkercar

Source: Citi, Thinkercar

Figure 5. German luxury ICE discount summary  
![](images/f3f8bca0178b43b4e6dbf1c6f5b5199efab38250ef640e6b338aa322dc3a759c.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 6. CPCA: Monthly Number of Car Model Adopted Price Cut  
Monthly Number of Car Model Adopted Price Cut  
![](images/c422eccb3a9deaeaef2d9b57d8377f5ec70702d19463fe0d32289b6cc093ad45.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, CPCA

Figure 7. CPCA: ICE Discount Trend ICE Discount Trend

![](images/7a47445494bbfaf38a789a92066f08ab65ca21aeabfc68bc1e259848a95d9fb5.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, CPCA

Figure 8. CPCA: NEV Discount Trend  
![](images/850eecf228d250e8e067f3f3008c62e824b6160c815243fcb2461283717bd76e.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, CPCA

Figure 9. CPCA: Luxury ICE Discount  
![](images/5adb557bfc6c0abc271c1fd289b0752c69d6eb4ff47efbb678dab84609aea638.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, CPCA

Figure 10. CPCA: JV ICE Discount  
![](images/22a0b88924860cea5070c3f3c8941bac9fa65a5d1957ee6c454dcec973ab213e.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, CPCA

Figure 11. CPCA: Local ICE Discount  
![](images/996f3908fe0ed8e52529b3edfebbb01c6092519f6d89eeffc2c54bcaff7818e5.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, CPCA

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at

https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for 

[中间内容因长度限制已省略]

ives, financial situation or needs of any particular investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a

subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.
"""
