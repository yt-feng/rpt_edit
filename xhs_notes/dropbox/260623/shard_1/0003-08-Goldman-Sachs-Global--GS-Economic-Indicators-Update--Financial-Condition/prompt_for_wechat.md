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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global: GS Economic Indicators Update: Financial Conditions Continue to Ease in South Korea

Please find an update of our proprietary global economic indicators below. The data behind these exhibits can be downloaded here. Interactive charts can be found on our living page here.

## Chart of the Week

Exhibit 1: The South Korea FCI Eased by 29bp Last Week as Tech Continued to Lead an Equity Rally

![](images/9645f958c78d073d585d622875f619d084ff72ab1a097c5db27757c1cc9f063d.jpg)  
Source: GS Global Investment Research

Jan Hatzius
+1(212)902-0394 | jan.hatzius@gs.com
GS & Co. LLC

Joseph Briggs
+1(212)902-2163 |
joseph.briggs@gs.com
GS & Co. LLC

Sarah Dong
+1(212)357-9741 | sarah.dong@gs.com
GS & Co. LLC

Megan Peters
+44(20)7051-2058 |
megan.l.peters@gs.com
GS International

## Key FCI and Growth Charts

Exhibit 2: The Global ex Russia FCI Eased by -0.8bps Last Week Primarily on Equities  
![](images/bc0de9f62121f7f6c18d22bd45d5bd2aa8f3cf7ab58cc0e9705e03a91195de2a.jpg)

![](images/23dcf052b2a26c296866eb8feb334e988f6f7c27d095aab34ff09ef99a69abad.jpg)  
Source: GS Global Investment Research

Exhibit 3: Higher 2026 Growth in South Korea  
![](images/035d44a12e8f66b27bc608eb5940d4e1da3025b8a65d5367da0246df310fde3f.jpg)  
Source: GS Global Investment Research

Exhibit 4: Our Preliminary May CAI Fell by -0.8pp in China and Rose by +0.7pp in Japan

<table><tr><td rowspan="2">Country(% of Data Released)</td><td rowspan="2">Month</td><td colspan="2">Spot CAI(% mom annualized)</td><td rowspan="2">3 Month AverageCAI (% momannualized)</td></tr><tr><td>Value</td><td>Weekly Change</td></tr><tr><td>Global</td><td>May</td><td>+2.9</td><td>-0.1</td><td>+3.0</td></tr><tr><td>Developed Markets</td><td>May</td><td>+2.2</td><td>+0.1</td><td>+2.3</td></tr><tr><td>US (17%)</td><td>June</td><td>+2.6</td><td>+0.2</td><td>+2.7</td></tr><tr><td>Euro Area (40%)</td><td>May</td><td>+1.1</td><td>+0.1</td><td>+1.6</td></tr><tr><td>Germany (50%)</td><td>May</td><td>-0.9</td><td>0.0</td><td>-0.1</td></tr><tr><td>France (38%)</td><td>May</td><td>+0.8</td><td>0.0</td><td>+1.2</td></tr><tr><td>Italy (34%)</td><td>May</td><td>+1.3</td><td>+0.1</td><td>+1.9</td></tr><tr><td>Spain (43%)</td><td>May</td><td>+2.8</td><td>+0.1</td><td>+3.7</td></tr><tr><td>Japan (51%)</td><td>May</td><td>+1.3</td><td>+0.7</td><td>+1.3</td></tr><tr><td>UK (62%)</td><td>May</td><td>0.0</td><td>+0.2</td><td>+0.4</td></tr><tr><td>Canada (33%)</td><td>May</td><td>+2.1</td><td>+0.1</td><td>+2.1</td></tr><tr><td>Australia (58%)</td><td>May</td><td>+1.3</td><td>0.0</td><td>+1.4</td></tr><tr><td>New Zealand (80%)</td><td>May</td><td>+2.0</td><td>-0.1</td><td>+2.3</td></tr><tr><td>Norway (58%)</td><td>May</td><td>+2.1</td><td>0.0</td><td>+2.6</td></tr><tr><td>Sweden (80%)</td><td>May</td><td>+2.4</td><td>0.0</td><td>+2.4</td></tr><tr><td>Emerging Markets</td><td>May</td><td>+4.0</td><td>-0.4</td><td>+4.2</td></tr><tr><td>China (80%)</td><td>May</td><td>+4.6</td><td>-0.8</td><td>+4.4</td></tr><tr><td>India (53%)</td><td>May</td><td>+7.5</td><td>+0.1</td><td>+7.3</td></tr><tr><td>Brazil (63%)</td><td>May</td><td>+2.1</td><td>0.0</td><td>+3.6</td></tr><tr><td>Russia (37%)</td><td>May</td><td>+0.1</td><td>0.0</td><td>+2.0</td></tr></table>

CAI in countries with 0% of data released is forecasted. CAI aggregates for Global, Developed Markets, and Emerging Markets are GDP-weighted using market FX country weights.  
Source: GS Global Investment Research

Exhibit 5: Our Global CAI Remains Above Potential  
![](images/f5f7e5baebcdd8e0cff9ab7d394ea3f2154d1d4d018ae1a885c4eb6da395e70f.jpg)  
Source: GS Global Investment Research  
GS DM CAI is a market FX-weighted average of the US, Germany, France, Italy, Spain, Japan, the UK, and Canada and EM is of Brazil, Russia, India, and China. Global GS CAI is an average of all aforementioned countries.

## Key Wage and Price Inflation Charts

Exhibit 6: GS Wage Trackers and Inflation Measures  
![](images/b9e973950b7e9ade60eb6cd9bf3dd23265cad3563aea0d4a1cd9334b84855418.jpg)  
US wage tracker is composition-adjusted in 2020 and 2021.  
Source: GS Global Investment Research

Exhibit 7: GS Jobs-Workers Gaps  
![](images/b8d092ae6da7d414f1af8d32e1d3bfe8324c180a586c0a15983f9cc8a37e1cbb.jpg)  
Source: GS Global Investment Research

![](images/0d7044b4702fedb5ab7e9eca2188d2c41d5234c7039ddb65e0fb103d66b41dff.jpg)

## Detailed Indicators Update

## Financial Conditions Index (FCI)

Exhibit 8: GS Global ex Russia FCI Level (Left) and Weekly Change With Contributions (Right)  
![](images/e8415475ec6dfef008c5e3a4d9c716929f92ae542edbc5930c10980edb3342bc.jpg)  
Source: GS Global Investment Research

![](images/d1201f815fe4937059893e8ea5756c63982bf2455a5472d569c0ae9cb3433a3d.jpg)

Exhibit 9: GS Global FCI Level (Left) and Weekly Change With Contributions (Right)  
![](images/db845992c6e768e420ef64c871b46cd695850845ed1cb5914f56c46d8a89115a.jpg)  
Source: GS Global Investment Research

![](images/fbcbeea8f3ea2a0aa5f31ca97c6420ad83d2eb8a3c359a36b4af1f1eecb85365.jpg)

Exhibit 10: GS US FCI Level (Left) and Weekly Change With Contributions (Right)  
![](images/9a83add430c714fe744df442bb094918a5ad017831737a0e8c00380b1750561c.jpg)  
Source: GS Global Investment Research

![](images/8b7038c604604fdd5e1b7ce0019cdec57d4887c55e2aa3eb5b11b6bb213341cd.jpg)

Exhibit 11: GS Euro Area FCI Level (Left) and Weekly Change With Contributions (Right)  
![](images/18be927e28299a1ad963a2c9dbc77a12c2a911ae15d38ecc7a72b19b48b41dc8.jpg)  
Source: GS Global Investment Research

![](images/6a2d81d3665fc3ce0a9390c9542bafa91ea93d860c73e4771ff9a8839ca05c2f.jpg)

Exhibit 12: Weekly Change in FCI Across Countries  
![](images/b1ade29adf48bb65f513e402af7db8e4669ce15e9e533eafd9b09ea7c1b518c8.jpg)  
Source: GS Global Investment Research

Exhibit 13: Year-Over-Year Change in FCI Across Countries  
![](images/eaf2fde19055a84a2f91388bb9fa2b34af857aa05de47125c8eb6f6ba17eb7b8.jpg)  
Source: GS Global Investment Research

FCI Impulses  
Exhibit 14: FCI Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right)  
![](images/48a46232ad7ecef9af27a453dff974b18bb34022a4e6908b5d9d20c7dc650426.jpg)  
Source: GS Global Investment Research

Exhibit 15: FCI Impulses in the US, Euro Area, Japan, and UK  
![](images/19a40d88f2abb9d55f016f358eb065d02ecb42260b5563390b1626d9a04fa5c4.jpg)  
Source: GS Global Investment Research

Current Activity Indicator (CAI)  
Exhibit 16: CAI Aggregates  
![](images/5c6aff77a609d953ba6ad2c15311196f826d3dcd33899374769c75fee5611c6e.jpg)

![](images/78cc733320cafa61a01d5436872106eba3b22fa14d78be2e391deae5961d5d03.jpg)  
GS DM CAI is a market FX-weighted average of the US, Germany, France, Italy, Spain, Japan, the UK, and Canada and EM is of Brazil, Russia, India, and China. Global GS CAI is an average of all aforementioned countries.  
Source: GS Global Investment Research

Exhibit 17: CAI Heatmap

<table><tr><td rowspan="2">Country(% of Data Released)</td><td rowspan="2">Month</td><td colspan="2">Spot CAI(% mom annualized)</td><td rowspan="2">3 Month AverageCAI (% momannualized)</td></tr><tr><td>Value</td><td>Weekly Change</td></tr><tr><td>Global</td><td>May</td><td>+2.9</td><td>-0.1</td><td>+3.0</td></tr><tr><td>Developed Markets</td><td>May</td><td>+2.2</td><td>+0.1</td><td>+2.3</td></tr><tr><td>US (17%)</td><td>June</td><td>+2.6</td><td>+0.2</td><td>+2.7</td></tr><tr><td>Euro Area (40%)</td><td>May</td><td>+1.1</td><td>+0.1</td><td>+1.6</td></tr><tr><td>Germany (50%)</td><td>May</td><td>-0.9</td><td>0.0</td><td>-0.1</td></tr><tr><td>France (38%)</td><td>May</td><td>+0.8</td><td>0.0</td><td>+1.2</td></tr><tr><td>Italy (34%)</td><td>May</td><td>+1.3</td><td>+0.1</td><td>+1.9</td></tr><tr><td>Spain (43%)</td><td>May</td><td>+2.8</td><td>+0.1</td><td>+3.7</td></tr><tr><td>Japan (51%)</td><td>May</td><td>+1.3</td><td>+0.7</td><td>+1.3</td></tr><tr><td>UK (62%)</td><td>May</td><td>0.0</td><td>+0.2</td><td>+0.4</td></tr><tr><td>Canada (33%)</td><td>May</td><td>+2.1</td><td>+0.1</td><td>+2.1</td></tr><tr><td>Australia (58%)</td><td>May</td><td>+1.3</td><td>0.0</td><td>+1.4</td></tr><tr><td>New Zealand (80%)</td><td>May</td><td>+2.0</td><td>-0.1</td><td>+2.3</td></tr><tr><td>Norway (58%)</td><td>May</td><td>+2.1</td><td>0.0</td><td>+2.6</td></tr><tr><td>Sweden (80%)</td><td>May</td><td>+2.4</td><td>0.0</td><td>+2.4</td></tr><tr><td>Emerging Markets</td><td>May</td><td>+4.0</td><td>-0.4</td><td>+4.2</td></tr><tr><td>China (80%)</td><td>May</td><td>+4.6</td><td>-0.8</td><td>+4.4</td></tr><tr><td>India (53%)</td><td>May</td><td>+7.5</td><td>+0.1</td><td>+7.3</td></tr><tr><td>Brazil (63%)</td><td>May</td><td>+2.1</td><td>0.0</td><td>+3.6</td></tr><tr><td>Russia (37%)</td><td>May</td><td>+0.1</td><td>0.0</td><td>+2.0</td></tr></table>

CAI in countries with 0% of data released is forecasted. CAI aggregates for Global, Developed Markets, and Emerging Markets are GDP-weighted using market FX country weights.  
Source: GS Global Investment Research

Exhibit 18: CAIs for Large DMs and EMs  
![](images/04f0caa84f5735f1f970a1c06867c8592b48b2a0995e18d34f63bfbf43676023.jpg)  
Source: GS Global Investment Research

![](images/c5bc23331413f89d59d02c9956677c13d9d87c2dd28870cedc01cacf7ecd8305.jpg)

MAP  
Exhibit 19: GS MAP Surprise Index  
![](images/f06099127306e567faa9972f4f273ebe8e9c9b96d2c24c5cd8574b94395be472.jpg)  
We present the 21-day moving average of daily MAP scores.

![](images/0da6f3e7e369929c869b8a6225940190c6d37d8c46020690383487aee63dedae.jpg)  
Source: GS Global Investment Research

![](images/4f199dfbfb7b088d0ff0084f16f04ff63dff650a0a4a4662dfdb33842619961f.jpg)  
We present the 21 day moving average of daily MAP scores.  
Source: GS Global Investment Research

## Trimmed Core Inflation

Exhibit 21: GS Trimmed Core Inflation  
![](images/4938e35ad1a79610f25c535c1cc9042b7a68cd0c4fd581900452e1eb46f50cc3.jpg)  
Source: GS Global Investment Research

## Wage Trackers

Exhibit 22: GS Wage Trackers  
![](images/3e1fe99f8789bb4aaf546d99d33d4003323b2ebdaa77ab0f4268a88498e5db5d.jpg)  
Source: GS Global Investment Research

Exhibit 23: GS Sequential Wage Trackers  
![](images/9fe84538751267f9816f9117509c5b69acb6c1c6ded882ed25c292c54be48c6b.jpg)

![](images/d2987a948443abfd0cd8b449a4056991e41e267d6a51bdb1857f90485edd6a1d.jpg)

![](images/05b29f1d96a54bae73f3eb3ec9c329dce87b9a87553680b1849754be23d4dfc0.jpg)

![](images/47fcd5a344bee27c4d5135f910cbfe7350b015b79a9d27f00738e0bd9f42fee3.jpg)

![](images/a58b9c040c30a1daaad72a42b54ccdc47f40bf1d9a4a046c7145084a629184d4.jpg)  
Source: GS Global Investment Research

![](images/e73fc166e79a3b5c4a64a23bfe78c70c90871c816cc330bfb2a1fee257095194.jpg)

Exhibit 24: GS Jobs-Workers Gaps  
![](images/113504d880384e4228f88c10ede1484f9efcacb9d1b3e61deeaa82f0aa97c4df.jpg)

![](images/5cd7e3dfde384702b652cdb435c95ad13d7a5f03782782af7bd89c53aaa32237.jpg)

Source: GS Global Investment Research  
Exhibit 25: Wage Survey Leading Indicators  
![](images/8c7cd06c29e9d8a1a15f4fe6f80b7ada6aa5efc55e250445178a8baef66197b6.jpg)  
Source: GS Global Investment Research

![](images/bb59ef6a29618f0b3a969e4353f0495bf0b3b8595c34dffedeb3af823393f03c.jpg)

## Top-Down Fiscal Impulses

Exhibit 26: Top-Down Fiscal Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right)  
![](images/11fae9f258e6a536d4a7cea5d1d1990c8c010bb6dd5669fc080ee3002c28597e.jpg)  
We compute the 4-quarter measure using average fiscal growth impulses from 2026Q1 to 2026Q4. The US impulse captures both expansionary fiscal discretionary policy and the tax-like effects of tariffs.  
Source: GS Global Investment Research

## Exhibit 27: Top-Down Fiscal Impulses in the US, Euro Area, China, and UK

![](images/99e3318742d0568109a951d7b0e7e0065ccf5d6dca62345fc34c67ae90b7f038.jpg)  
Source: GS Global Investment Research  
The US impulse captures both expansionary fiscal discretionary policy and the tax-like effects of tariffs.

Output Gaps  
Exhibit 28: Latest Short-Run Utilization Scores

<table><tr><td rowspan="2">Country</td><td rowspan="2">Month</td><td colspan="2">Spot Short-Run Utilization Scores (% of Potential)</td><td rowspan="2">3 Month Average (% of Potential)</td></tr><tr><td>Value</td><td>Weekly Change</td></tr><tr><td>US</td><td>June</td><td>-1.8</td><td>+0.1</td><td>-1.9</td></tr><tr><td>Germany</td><td>June</td><td>+0.5</td><td>0.0</td><td>+0.5</td></tr><tr><td>France</td><td>June</td><td>+0.9</td><td>+0.1</td><td>+0.9</td></tr><tr><td>Italy</td><td>June</td><td>+6.5</td><td>0.0</td><td>+6.5</td></tr><tr><td>Spain</td><td>June</td><td>+5.6</td><td>+0.4</td><td>+5.1</td></tr><tr><td>Japan</td><td>April</td><td>-0.2</td><td>0.0</td><td>-0.5</td></tr><tr><td>UK</td><td>June</td><td>-1.4</td><td>+0.1</td><td>-1.2</td></tr><tr><td>Canada</td><td>May</td><td>-0.8</td><td>0.0</td><td>-1.0</td></tr><tr><td>Australia</td><td>May</td><td>+0.1</td><td>-0.1</td><td>+0.2</td></tr><tr><td>China</td><td>May</td><td>-0.1</td><td>+0.1</td><td>-0.1</td></tr><tr><td>India</td><td>May</td><td>+0.3</td><td>0.0</td><td>+0.2</td></tr><tr><td>Brazil</td><td>April</td><td>+0.7</td><td>0.0</td><td>+0.6</td></tr><tr><td>Russia</td><td>May</td><td>+1.3</td><td>0.0</td><td>+1.3</td></tr></table>

Source: GS Global Investment Research

Exhibit 29: Short-Run Utilization Scores  
![](images/eeeeb1997a7888dd2d7913a1caac205d798b4e7e975b98d70d55351165a466d2.jpg)  
Source: GS Global Investment Research

## GS Forecasts vs. Consensus

Exhibit 30: Change in GS 2026 Inflation Forecasts  
![](images/db05c6b75b109696fd5ebc9db09cfa119378ae92c85370029671d3a97af8ad0e.jpg)  
Source: GS Global Investment Research

## Exhibit 31: Change in GS 2027 Inflation Forecasts

![](images/afb9dd8575e2f5233e06ee5ebcee8c5f3e8bd6b3a257975560fdd73b0946c41b.jpg)  
Source: GS Global Investment Research

Exhibit 32: Change in GS 2026 GDP Forecasts  
![](images/6d286f9d7d4f9b1a18c11a9ecb7f13e07a3b2ec277b0dd3dc786cb166f87a5e3.jpg)  
Source: GS Global Investment Research

## Exhibit 33: Change in GS 2027 GDP Forecasts

![](images/ec0a5eeba7ebfb2f9cad72e401cf52937426508199d405bd05d64c5ee2faf8ca.jpg)  
Source: GS Global Investment Research

## Exhibit 34: GS 2026 Global GDP Forecasts vs. Other Forecasters

![](images/4a1ab462532bb16e10404a10ca4026c05d5a4e1acddc6166ff78c7c5ad95867d.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 35: GS 2027 Global GDP Forecasts vs. Other Forecasters  
![](images/080377932f613932d4c6d761808795fa9fbb946cbbd212113a9399411deb2958.jpg)  
Source: Bloomberg, GS Global Investment Research

Thank you to Jamal Lawal, intern on the Global Economics team, for his contributions to this report.

## Methodology Notes for GS Proprietary Economic Indicators

1. Financial Conditions: Our Financial Conditions Indexes are designed to gauge the overall looseness or tightness of financial conditions across the world's major economies. The GSFCIs can provide valuable information about the GDP growth outlook, the transmission of monetary policy to the real economy, and the importance of financial shocks hitting the economy. (Latest methodology notes here and here.)

2. FCI Impulses: Our FCI impulses measure the effect of financial conditions on real GDP growth. For details on the methodology please see here.

3. Current Activity Indicator: In statistical jargon, the CAIs are the “first principal component” of several real activity indicators, expressed in GDP-equivalent units. The CAIs can be interpreted as the growth signal in the main high-frequency indicators for each economy. At any given point, data for certain indicators may not be available. The CAIs therefore incorporate forecasted values for missing indicators, which are then replaced with actual values when they are released. (Latest methodology note here.)

4. MAP Surprise Index: Our daily MAP surprise indices summarize the importance and strength (relative to consensus expectations) of economic indicators worldwide. Across numerous countries, our surprise index's methodology standardizes the criteria for indicator selection and importance, thresholds for “surprise” scores, and schemes for aggregation, while allowing for occasional judgmental input from local economists. (Latest methodology here.)

5. Trimmed Core Inflation. Our trimmed core inflation measure trims the one third most extreme price changes from the individual core inflation components. (Latest methodology note here.)

6. Jobs-Workers Gaps: Our jobs-workers gaps capture the difference between total labor demand (i.e. job openings plus employment) and labor supply (i.e. the labor force). We forecast the jobs-workers gap by forecasting official job openings with country-specific models reliant on high-frequency job posting data, and by forecasting the unemployment rate using jobless claims and other leading unemployment indicators. Our latest note can be found here.

7. Wage Survey Leading Indicator: Our wage survey leading indicators summarize survey questions about current and expected wage growth from business and consumer surveys. Our latest note can be found here.

8. Wage Trackers: Our wage trackers measure the underlying pace of wage growth across the G10 economies. Our latest notes can be found here and here.

9. Fiscal Impulses: Our fiscal impulses measure the effect of fiscal policy on real GDP growth. For details on the methodology please see here.

10. Short-Run Utilization Scores: Our short-run utilization scores are based on scores for both the labor market and the industrial sector, each based on a number of hard indicators and surveys, such as, for instance, the unemployment rate or supplier delivery times. We then define the short-run utilization score as a weighted average of these scores, converted into GDP-equivalent units. Our latest note can be found here. (We previously called our short-run utilization scores short-run output gaps.)

## Disclosure Appendix

## Reg AC

We, Jan Hatzius, Joseph Briggs, Sarah Dong and Megan Peters, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Author

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
