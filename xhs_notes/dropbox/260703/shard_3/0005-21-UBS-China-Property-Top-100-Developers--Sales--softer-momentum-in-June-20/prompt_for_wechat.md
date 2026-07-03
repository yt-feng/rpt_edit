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
- 已识别机构名：`UBS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份UBS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
First Read

# China Property

# Top 100 Developers' Sales: softer momentum in June 2026

## Top 100 developers' contract sales declined by 12% YoY

Top 100 developers' contract sales declined 12% YoY in June 2026, widening from -2% in May 2026 (Figure 1). On MoM basis, June 2026 sales improved 5% from May, vs 2021-2025 average of 26%. In the first half of this year, top 100 contract sales declined by 16% YoY, vs -17% in 5M2026. Despite a softer momentum in property sales in June 2026, land market remained heated in June. In June, Shenzhen sold three land parcels for a total consideration of Rmb20bn, at 99-151% premium above base price (see note). In Shanghai, on 30 June 2026, C&D International acquired a land parcel for Rmb7bn, at 30% premium, and Greentown China won two parcels for a total of Rmb3bn, at c.20% premium. The strong land premiums show developers' confidence in tier 1 cities' prime location, which reflects the recent strong sell-through rate in tier 1 cities' high end property. This is in line with our expectation of improved sentiment in physical market (see our upgrade note).

## Secondary transactions remained strong in June 2026

As of the week of June 28th, secondary transaction volume (in units) for 12 cities remained strong at +11% YoY month-to-date. In addition, as of 24 June 2026, growth of secondary listings across 50 cities slowed to 2.3% YoY, while tier 1 cities' secondary listings decreased at -9.7% YoY, a positive signal suggesting less secondary supply. We attribute the accelerated decline of secondary listings in tier 1 cities to policy relaxation, improved housing sentiment and rental yield improvement. Meanwhile, rental price in four tier 1 cities still declined by 2.0% YoY in May 2026, narrowing from -2.7% in April 2026 (Figure 11).

## COLI monthly contract sales moved to the first place

In June 2026, SOE developers continued to gain market share from POE developers, and SOE developers' contract sales outperformed at -8% YoY (Figure 7). As of 1H26, among developers under our coverage, COLI, CMSK, Jinmao and CRL outperformed with contract sales growth of +12%/8%/8%/6% YoY respectively, while Vanke/Longfor underperformed with contract sales declining by 49%/53% YoY. COLI' monthly contract sales moved to the first place at Rmb31.4bn, +5% YoY, due to two new launches in Shenzhen - Antiyayuan (100% sell-through) and Yunsongjiuzhang (83% sell-through, see our field trip video). Our top pick remains COLI, and we are Buy rated on CMSK, Jinmao and CRL.

Equities

China
Real Estate

John Lam, CFA

Analyst

john-za.lam@ubs.com

+852-2971 6358

Vera Gong, CFA

Analyst

vera.gong@ubs.com

+852-2971 8950

Mark Leung

Analyst

mark.leung@ubs.com

+852-2971 8636

Ben Ho
Associate Analyst
ben.ho@ubs.com
+852-3712 2819

Figure 1: Top 100 developers' contract sales in June 2026 improved sequentially, +5% MoM, and YoY declined 12%

<table><tr><td rowspan="2">Company</td><td colspan="3">June2026 (CRIC)</td><td colspan="2">1H26</td></tr><tr><td>Rmb bn</td><td>YoY%</td><td>MoM%</td><td>Rmb bn</td><td>YoY%</td></tr><tr><td>COLI</td><td>31.4</td><td>5%</td><td>15%</td><td>134.4</td><td>12%</td></tr><tr><td>Poly Developments</td><td>29.8</td><td>2%</td><td>8%</td><td>135.1</td><td>-7%</td></tr><tr><td>CR Land</td><td>23.0</td><td>-2%</td><td>-2%</td><td>116.5</td><td>5%</td></tr><tr><td>CMSK</td><td>20.2</td><td>-7%</td><td>-3%</td><td>96.2</td><td>8%</td></tr><tr><td>Jinmao</td><td>15.8</td><td>1%</td><td>50%</td><td>57.5</td><td>8%</td></tr><tr><td>Yuexiu</td><td>13.5</td><td>25%</td><td>19%</td><td>50.5</td><td>-18%</td></tr><tr><td>Greenland (A)</td><td>12.2</td><td>44%</td><td>126%</td><td>35.9</td><td>7%</td></tr><tr><td>C&amp;D International</td><td>12.0</td><td>-18%</td><td>-13%</td><td>63.8</td><td>-10%</td></tr><tr><td>Greentown China</td><td>11.7</td><td>-22%</td><td>-6%</td><td>60.2</td><td>-25%</td></tr><tr><td>Binjiang</td><td>9.6</td><td>2%</td><td>3%</td><td>43.2</td><td>-18%</td></tr><tr><td>Vanke</td><td>7.4</td><td>-37%</td><td>18%</td><td>35.0</td><td>-49%</td></tr><tr><td>CRCC</td><td>4.9</td><td>-41%</td><td>1%</td><td>26.3</td><td>-27%</td></tr><tr><td>Huafa</td><td>4.0</td><td>-43%</td><td>-9%</td><td>22.1</td><td>-55%</td></tr><tr><td>Poly Property</td><td>3.3</td><td>-31%</td><td>-25%</td><td>23.1</td><td>-14%</td></tr><tr><td>Country Garden</td><td>3.0</td><td>-16%</td><td>-4%</td><td>17.0</td><td>-17%</td></tr><tr><td>OCT</td><td>2.9</td><td>43%</td><td>175%</td><td>7.4</td><td>-30%</td></tr><tr><td>Longfor</td><td>2.8</td><td>-57%</td><td>-18%</td><td>16.5</td><td>-53%</td></tr><tr><td>BCDC</td><td>2.3</td><td>-16%</td><td>109%</td><td>6.8</td><td>-38%</td></tr><tr><td>CCCG Real Estate</td><td>2.2</td><td>-29%</td><td>11%</td><td>12.8</td><td>-18%</td></tr><tr><td>Evergrande</td><td>1.8</td><td>21%</td><td>87%</td><td>5.5</td><td>-50%</td></tr><tr><td>Gemdale</td><td>1.7</td><td>-45%</td><td>-15%</td><td>9.5</td><td>-44%</td></tr><tr><td>Yango</td><td>1.5</td><td>-16%</td><td>9%</td><td>6.3</td><td>-27%</td></tr><tr><td>Seazen Holdings</td><td>1.3</td><td>-17%</td><td>32%</td><td>6.4</td><td>-39%</td></tr><tr><td>Midea Real Estate</td><td>1.3</td><td>-48%</td><td>-7%</td><td>7.5</td><td>-52%</td></tr><tr><td>Sino-ocean</td><td>1.3</td><td>-55%</td><td>-42%</td><td>8.1</td><td>-39%</td></tr><tr><td>Shimao</td><td>1.3</td><td>-45%</td><td>3%</td><td>8.2</td><td>-39%</td></tr><tr><td>Xiamen Xiangyu</td><td>1.1</td><td>-62%</td><td>-69%</td><td>11.5</td><td>-21%</td></tr><tr><td>Hopson</td><td>1.1</td><td>-24%</td><td>-1%</td><td>4.5</td><td>-18%</td></tr><tr><td>CIFI</td><td>1.1</td><td>-12%</td><td>27%</td><td>5.0</td><td>-51%</td></tr><tr><td>Sunac</td><td>0.9</td><td>-88%</td><td>-20%</td><td>9.0</td><td>-62%</td></tr><tr><td>Yanlord</td><td>0.7</td><td>-11%</td><td>-50%</td><td>5.2</td><td>-42%</td></tr><tr><td>Grandjoy</td><td>0.7</td><td>-71%</td><td>-11%</td><td>4.4</td><td>-54%</td></tr><tr><td>CCRE</td><td>0.7</td><td>-35%</td><td>-9%</td><td>3.7</td><td>-18%</td></tr><tr><td>Powerlong</td><td>0.6</td><td>-15%</td><td>5%</td><td>3.4</td><td>-8%</td></tr><tr><td>SCE</td><td>0.6</td><td>-15%</td><td>-23%</td><td>3.9</td><td>-14%</td></tr><tr><td>Logan</td><td>0.6</td><td>45%</td><td>0%</td><td>2.8</td><td>-20%</td></tr><tr><td>Top1-10 total</td><td>175</td><td>0%</td><td>8%</td><td>714</td><td>-16%</td></tr><tr><td>Top1-50 total</td><td>285</td><td>-11%</td><td>6%</td><td>1,302</td><td>-15%</td></tr><tr><td>Top1-100 total</td><td>324</td><td>-12%</td><td>5%</td><td>1,495</td><td>-16%</td></tr></table>

Source: CRIC. Note: Ranked by contract sales in June-2026, Contract sales for Greentown China and CCRE exclude project management amount.

Figure 2: Top 100 developers' contract sales up 5% MoM in June 2026, lower than 2021-2025 average of 26%

<table><tr><td>Month</td><td>Contract sales (Rmb bn)</td><td>MoM</td><td>YoY</td></tr><tr><td>Jun-21</td><td>1,458</td><td>13%</td><td>0%</td></tr><tr><td>Jun-22</td><td>831</td><td>60%</td><td>-43%</td></tr><tr><td>Jun-23</td><td>601</td><td>10%</td><td>-28%</td></tr><tr><td>Jun-24</td><td>470</td><td>33%</td><td>-22%</td></tr><tr><td>Jun-25</td><td>369</td><td>16%</td><td>-22%</td></tr><tr><td>Jun-26</td><td>324</td><td>5%</td><td>-12%</td></tr><tr><td colspan="2">Average (2021-25)</td><td>26%</td><td>-23%</td></tr></table>

Source: CRIC

Figure 3: Top 100 developers' combined attri. contract sales value dropped by 10% YoY in June 2026  
![](images/e565650959b94bb218c87ad755f2cea7087337b6ff7c5b228e0b91c42bfb3833.jpg)  
Source: CRIC, UBS

Figure 4: Top 100 developers' combined gross contract sales value dropped by 12% YoY in June 2026  
![](images/0404040521ed1f71e22ff97ceeeb77ed267c60d9bc61190ad572b2e6a793b8e5.jpg)  
Source: CRIC, UBS

Figure 5: Top 100 developers' combined attr. contract sales GFA dropped by 7% YoY in June 2026  
![](images/fa53c044d8ba235dd200bb3f55104f9fa3b20bd1e67801e7b48564af76e060c8.jpg)  
Source: CRIC, UBS

Figure 6: Top 100 developers' combined gross contract sales GFA dropped by 9% YoY in June 2026  
![](images/f81a8d24b45eb8474cf9701a1bc8daf4ff5557c66d8bd3661a4b9f15d04a7652.jpg)  
Source: CRIC, UBS

Figure 7: SOE monthly contract sales values decreased by 8% YoY in June 2026, outperformed top 100 peers  
![](images/a56d6b4b757fb221f486ebb670df6aea3a87587a65eb7f0b6efd030089b47d39.jpg)  
Source: CRIC, UBS

Figure 8: Real-time weekly secondary transactions for 12 major cities increased 13% YoY  
![](images/274e9e415ed743fcf389ee8a082d0c0f6b477a9c81ced596889cd207b6cf7359.jpg)  
Source: Bingshan index, UBS. Date as of June 28th 2026.

Figure 9: Real-time weekly secondary transactions for 12 major cities increased 13% YoY  
![](images/383dd96ff5c880fbbaaef9e40575e95abf9427b1f499365dc36b48d72f5b3fa1.jpg)  
Source: Bingshan index, UBS. Date as of June 28th 2026.

Figure 10: Secondary property price index in tier 1 cities increased by 0.2% MoM in May 2026  
Tier 1 cities secondary property price index  
![](images/8495896e3befdaf7e8d7ffa757ccc26eda0020246680e9beed2baf8d59a491c3.jpg)  
Source: Centraline, Wind

Figure 11: Rental price index in tier 1 cities declined by 2.0% as of May 2026  
![](images/a39806450dd530fbc3d650e3f42ff3c6c9e85f8856633af904f6e9b8f20d6bde.jpg)  
Source: Centraline, UBS.

Figure 12: 50-city secondary listing growth slowed to 2.3% YoY  
50-city secondary units of listing on Beike  
![](images/0cc8a74a1c6c63a97915fd78c5f2202d9fdf5f42a841f10b578656dc8063a979.jpg)  
Source: BEKE. Data is as of 24 June 2026.

Figure 13: Tier-1 cites secondary listing declined by 9.7% YoY  
Tier 1 cities units of listing on Beike  
![](images/8dd87be6541ef2b4f09013779d609637bf5c372811bfb186ef7a2ef66b1c0ba1.jpg)  
Source: BEKE. Data is as of 24 June 2026.

## Valuation Method and Risk Statement

We base our valuations of China's property developers on PE or P/BV multiples. We believe key downside risks related to the Chinese property market include: 1) government administrative policies that restrict demand and mortgage lending; 2) tight financing for China's developers; 3) lower-than-expected residential growth in China's economy. We believe key upside risks include: 1) material policy loosening that effectively boosts residential property sales, investments and prices to positive YoY growth; 2) large-scale asset disposals at fair prices by some developers to ease liquidity pressures.

COLI: Our price target of COLI is based on P/BV. Key risks related to COLI are: 1) government administrative policies to restrict demand and mortgage lending; 2) tight financing for China developers; and 3) lower-than-expected growth of China's economy. Key upside risks: 1) rise in sales volume and prices on property policy loosening; 2) large-scale policy stimulus on property market.

CMSK: We value China Merchants Shekou using a P/BV multiple. Key downside risks to the company include: 1) lower-than-expected sales at the Qianhai project; and 2) weaker-than-expected property sales in tier 1 and 2 cities. Key upside risks: 1) rise in sales volume and prices on property policy loosening; 2) large-scale policy stimulus on property market.

Jinmao: Our price target of Jinmao is based on PE. We believe the key downside risks for Jinmao include: 1) a tightening of property policies resulting in restrictions on the primary market and pre-sales, and squeezed margins; 2) an unsuccessful roll-out of city operation business; and 3) lower-than-expected growth of China's economy. Key upside risks: 1) rise in sales volume and prices on property policy loosening; 2) large-scale policy stimulus on property market.

CRL: Our price target of CRL is based on PE. We believe the key risks to CR Land include: 1) a slowdown in China's property market; 2) increasing competition in land market leading to higher land costs and lower margins; and 3) lower-than-expected growth of China's retail sales market. Key upside risks: 1) rise in sales volume and prices on property policy loosening; 2) large-scale policy stimulus on property market; 3) accelerated spin-off of its investment properties at higher-than-expected valuation.

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 01 July 2026 07:13 AM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>54%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 31 March 2026.  
1: Percentage of companies under coverage globally within the 12-month rating category.

2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE): Exceptions to the standard +/-6% bands may be granted by the Investment Review Consultation (IRC). Factors considered by the IRC include the stock's volatility and the credit spread of the respective company's debt. As a result, stocks deemed to be very high or low risk may be subject to higher or lower bands as they relate to the rating. When such exceptions apply, they will be identified in the Company Disclosures table in the relevant research piece.

Research analysts contributing to this report who are employed by any non-US affiliate of UBS LLC are not registered/qualified as research analysts with FINRA. Such analysts may not be associated persons of UBS LLC and therefore are not subject to the FINRA restrictions on communications with a subject company, public appearances, and trading securities held by a research analyst account. The name of each affiliate and analyst employed by that affiliate contributing to this report, if any, follows.

UBS AG Hong Kong Branch: Ben Ho, John Lam, CFA, Mark Leung, Vera Gong

[中间内容因长度限制已省略]

lated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
