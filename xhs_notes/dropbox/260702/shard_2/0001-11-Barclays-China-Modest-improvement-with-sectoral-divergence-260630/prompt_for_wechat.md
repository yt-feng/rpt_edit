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
- 已识别机构名：`BARC`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份BARC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
China

# Modest improvement with sectoral divergence

June PMI details and recent high-frequency indicators continue to point to a bifurcated growth pattern, with resilience in high-tech and export-oriented sectors contrasting with weakness in traditional industries and domestic demand. Construction activity stayed weak despite faster LGSB issuance.

• May NBS manufacturing PMI: 50.3

• Bloomberg consensus forecast (BARC): 50.1 (50.1)

• May NBS manufacturing PMI: 50.0

China's NBS manufacturing PMI rose to 50.3 in June from 50.0 in May, above both our forecast and consensus of 50.1. The production sub-index edged higher, while both new orders and new export orders improved and moved back into expansion territory. The pickup suggests a modest improvement in manufacturing activity in June, supported by resilient demand for high-tech products, lower energy prices, and a normalization in production following holiday-related disruptions in May. That said, the headline PMI remained only slightly above the 50 threshold, while underlying sector performance continued to diverge.

Sector performance remained uneven. The June PMI details continued to point to a bifurcated trend, with high-tech industries outperforming traditional sectors. High-tech manufacturing PMI rose to 53.5 from 52.9 in May, reaching its highest level in more than two years and remaining in expansion for a 17th consecutive month. Equipment manufacturing also strengthened to a three-year high of 52.5. Notably, both the production and new orders indices for sectors such as special equipment and computers, communications and electronic equipment remained above 54. In contrast, traditional industries remained weak. Oil-related sectors, including chemical fibers, and rubber and plastic products, stayed in contraction, while ferrous metals processing is facing headwinds from the prolonged property sector weakness. Consumer goods manufacturing improved but continued to lag the headline PMI, underscoring still-soft domestic demand.

Recent high-frequency indicators reinforce this picture of a two-speed economy, with resilience in high-tech and export-oriented sectors, but weakness in traditional industries and domestic demand (China: Domestic demand searches for a bottom, 24 June 2026). On the domestic demand side, major e-commerce platforms reported slower sales growth during the midyear shopping festival, while auto sales remained in a double-digit decline. Property market indicators also softened, with new home sales growth slowing further from May and secondary-market transactions easing slightly, albeit still recording low double-digit growth. In contrast,

Ying Zhang
+852 2903 2652
ying.zhang3@BARC.com
BARC Bank, Hong Kong

Yingke Zhou
+852 2903 2653
yingke.zhou@BARC.com
BARC Bank, Hong Kong

Jian Chang
+852 2903 2654
jian.chang@BARC.com
BARC Bank, Hong Kong

external demand remained resilient, with port cargo throughput expanding by an average of 5.2% y/y in June, up from 4.6% in May, suggesting continued strength in exports.

## Highlights of NBS manufacturing PMI breakdown

\- On prices, manufacturing prices weakened, with the input price index falling to 54.2 and the output price index slipping back into contractionary territory at 48.2 (from 60.5 and 51.9, respectively), both below their February survey readings which were collected before the Middle East conflict broke out on 27 February. The gap between the input and output price PMIs narrowed to 6.0pp in June after reaching a four-year high of 8.6pp in April-May, reflecting some relief from lower input costs. That said, the gap remained wider than the roughly 5pp average seen in January-February before the conflict, indicating that margin pressures have eased but have not fully returned to pre-conflicts levels.

\- Both supply and demand indicators improved in June relative to May. The production PMI edged up 0.2pp, to 51.4, while the new orders PMI returned to expansion territory at 51.2 from 49.9 in May. The improvement was accompanied by a rebound in the new export orders PMI, which rose to 50.1 in June after falling to 48.6 in May.

\- High-tech manufacturing remained the strongest-performing segment, with its PMI rising to 53.5 in June from 52.9 in May, the highest in more than two years and above 50 for a 17th straight month. Equipment manufacturing also strengthened, reaching a three-year high of 52.5. Consumer goods manufacturing returned to expansion territory, at 50.2 (May: 49.7), though it continued to lag the headline PMI, while manufacturing in energy-intensive sectors remained weak at 47.1.

FIGURE 1. NBS manufacturing PMI improved...  
![](images/3f21c8075d7eb1786e9e8be5bcf80d3ce298ec8618ac2735c9c74f55a5d81ffc.jpg)  
Source: Wind, BARC

FIGURE 2. ... with new (export) orders PMIs jumping back to expansionary territory  
![](images/ecec05ab1e4708d1a4324cbaf4fb100736f7a154988e61f59438d8bd2e38de68.jpg)  
Source: Wind, BARC

FIGURE 3. Manufacturing prices normalise gradually  
![](images/da5973aaa9fdad9d2fe85c99ad5eac192f6872ce1fc1197f8bf8c81827c620f1.jpg)  
Source: Wind, BARC

FIGURE 4. High-tech sectors continued to take the lead  
![](images/6d8dbcc4d63a12bcc7467c641fc38fd79754a6e157ac2530378d6c1ac79ef295.jpg)  
Source: Wind, BARC

FIGURE 5. Strong shipments of AI and green-tech product  
![](images/ad1f9e9045f7f058fb8490cf955a1f28bdf537216a1c46d2838b2e45cf4192e0.jpg)  
Data as of May
Source: Wind, BARC

FIGURE 6. Port cargo throughput stayed resilient in June  
![](images/f1864ae6043055bf3b261504e600dd58286933a6c7aaedc501b193dd914d5450.jpg)  
Source: Wind, BARC

## Non-manufacturing PMI edged up

The non-manufacturing PMI improved marginally to 50.2 in June from 50.1 in May, supported by modest gains in both services and construction activity. Within services, the PMI edged up to 50.4 from 50.3. Growth remained concentrated in technology- and finance-related sectors, including telecommunications, broadcasting, satellite transmission, software and IT services, monetary and financial services, and insurance, where activity indices stood above 55. By contrast, air transport and real estate services lag, with PMIs below the breakeven threshold, pointing to weaker demand in these sectors.

The construction PMI edged higher for a second month, rising to 49 in June from the post-COVID low in April. However, the new orders index remained weak although improving to 46.3 from 43.5, underscoring still-weak demand conditions. We note that the pace of local-government special bond issuance accelerated in June after March-May slowdown, with the single-month issuance amounting to 13% of the annual quota, versus a monthly average of 4% in April-May and 9% on average in Q1, although cumulative YTD issuance is still fell 2.1% than in H1 25.

The property sector is likely to remain a drag on construction activity. High-frequency data showed June new property sales growth weakened further from May and secondary transactions slowed slightly while maintaining low double-digit growth. Home prices in both the new and secondary markets continued to fall, while most housing indicators, notably property investment and new starts stayed deep in contraction.

FIGURE 7. Services PMI showed signs of recovery  
![](images/7db78d6f10a62df39f2028bb72f8e59d9ee01eac8b6837d1d34872ee66074120.jpg)  
Source: Wind, BARC

FIGURE 8. Construction PMI stayed in contraction despite faster LGSB issuance  
![](images/b0d0da5fcf04dbde5483b7d728297734a655becf790d6950009fad913fcc3e88.jpg)  
Source: Wind, BARC

FIGURE 9. NBS manufacturing and non-manufacturing PMIs

<table><tr><td></td><td>Weight</td><td>Jun-26</td><td>May-26</td><td>Apr-26</td><td>Mar-26</td><td>Feb-26</td><td>Jan-26</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>Sep-25</td><td>Aug-25</td><td>Jul-25</td><td>Jun-25</td></tr><tr><td>NBS manufacturing PMI</td><td></td><td>50.3</td><td>50.0</td><td>50.3</td><td>50.4</td><td>49.0</td><td>49.3</td><td>50.1</td><td>49.2</td><td>49.0</td><td>49.8</td><td>49.4</td><td>49.3</td><td>49.7</td></tr><tr><td>New Orders</td><td>30%</td><td>51.2</td><td>49.9</td><td>50.6</td><td>51.6</td><td>48.6</td><td>49.2</td><td>50.8</td><td>49.2</td><td>48.8</td><td>49.7</td><td>49.5</td><td>49.4</td><td>50.2</td></tr><tr><td>Production</td><td>25%</td><td>51.4</td><td>51.2</td><td>51.5</td><td>51.4</td><td>49.6</td><td>50.6</td><td>51.7</td><td>50.0</td><td>49.7</td><td>51.9</td><td>50.8</td><td>50.5</td><td>51.0</td></tr><tr><td>Employment</td><td>20%</td><td>48.5</td><td>48.6</td><td>48.8</td><td>48.6</td><td>48.0</td><td>48.1</td><td>48.2</td><td>48.4</td><td>48.3</td><td>48.5</td><td>47.9</td><td>48.0</td><td>47.9</td></tr><tr><td>Supplier Deliveries</td><td>15%</td><td>49.9</td><td>49.2</td><td>49.5</td><td>49.5</td><td>49.1</td><td>50.1</td><td>50.2</td><td>50.1</td><td>50.0</td><td>50.8</td><td>50.5</td><td>50.3</td><td>50.2</td></tr><tr><td>Raw Material Inventory</td><td>10%</td><td>48.4</td><td>48.6</td><td>49.3</td><td>47.7</td><td>47.5</td><td>47.4</td><td>47.8</td><td>47.3</td><td>47.3</td><td>48.5</td><td>48.0</td><td>47.7</td><td>48.0</td></tr><tr><td>New Export Orders</td><td></td><td>50.1</td><td>48.6</td><td>50.3</td><td>49.1</td><td>45.0</td><td>47.8</td><td>49.0</td><td>47.6</td><td>45.9</td><td>47.8</td><td>47.2</td><td>47.1</td><td>47.7</td></tr><tr><td>Imports</td><td></td><td>49.6</td><td>48.8</td><td>50.1</td><td>49.8</td><td>45.6</td><td>47.3</td><td>47.0</td><td>47.0</td><td>46.8</td><td>48.1</td><td>48.0</td><td>47.8</td><td>47.8</td></tr><tr><td>Input Prices</td><td></td><td>54.2</td><td>60.5</td><td>63.7</td><td>63.9</td><td>54.8</td><td>56.1</td><td>53.1</td><td>53.6</td><td>52.5</td><td>53.2</td><td>53.3</td><td>51.5</td><td>48.4</td></tr><tr><td>Output Prices</td><td></td><td>48.2</td><td>51.9</td><td>55.1</td><td>55.4</td><td>50.6</td><td>50.6</td><td>48.9</td><td>48.2</td><td>47.5</td><td>48.2</td><td>49.1</td><td>48.3</td><td>46.2</td></tr><tr><td>Finished Goods Inventory</td><td></td><td>47.7</td><td>49.3</td><td>47.5</td><td>46.7</td><td>45.8</td><td>48.6</td><td>48.2</td><td>47.3</td><td>48.1</td><td>48.2</td><td>46.8</td><td>47.4</td><td>48.1</td></tr><tr><td>Large Enterprises</td><td></td><td>50.7</td><td>51.1</td><td>50.2</td><td>51.6</td><td>51.5</td><td>50.3</td><td>50.8</td><td>49.3</td><td>49.9</td><td>51.0</td><td>50.8</td><td>50.3</td><td>51.2</td></tr><tr><td>Medium Enterprises</td><td></td><td>50.5</td><td>48.6</td><td>50.5</td><td>49.0</td><td>47.5</td><td>48.7</td><td>49.8</td><td>48.9</td><td>48.7</td><td>48.8</td><td>48.9</td><td>49.5</td><td>48.6</td></tr><tr><td>Small Enterprises</td><td></td><td>48.2</td><td>48.5</td><td>50.1</td><td>49.3</td><td>44.8</td><td>47.4</td><td>48.6</td><td>49.1</td><td>47.1</td><td>48.2</td><td>46.6</td><td>46.4</td><td>47.3</td></tr><tr><td>RatingDog China manufacturing PMI</td><td></td><td></td><td>51.8</td><td>52.2</td><td>50.8</td><td>52.1</td><td>50.3</td><td>50.1</td><td>49.9</td><td>50.6</td><td>51.2</td><td>50.5</td><td>49.5</td><td>50.4</td></tr><tr><td>NBS services PMI</td><td></td><td>50.4</td><td>50.3</td><td>49.6</td><td>50.2</td><td>49.7</td><td>49.5</td><td>49.7</td><td>49.5</td><td>50.2</td><td>50.1</td><td>50.5</td><td>50.0</td><td>50.1</td></tr><tr><td>NBS construction PMI</td><td></td><td>49.0</td><td>48.8</td><td>48.0</td><td>49.3</td><td>48.2</td><td>48.8</td><td>52.8</td><td>49.6</td><td>49.1</td><td>49.3</td><td>49.1</td><td>50.6</td><td>52.8</td></tr><tr><td>NBS composite PMI</td><td></td><td>50.6</td><td>50.5</td><td>50.1</td><td>50.5</td><td>49.5</td><td>49.8</td><td>50.7</td><td>49.7</td><td>50.0</td><td>50.6</td><td>50.5</td><td>50.2</td><td>50.7</td></tr></table>

Source: Wind, BARC

## Analyst(s) Certification(s):

We, Yingke Zhou, Jian Chang and Ying Zhang, hereby certify (1) that the views expressed in this research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC").

All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

For current important disclosures regarding any issuers which are the subject of this research report please refer to https://

publicresearch.BARC.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that BARC may have a conflict of interest that could affect the objectivity of this report. BARC Capital Inc. and/or one of its affiliates regularly trades, generally deals as principal and generally provides liquidity (as market maker or otherwise) in the debt securities that are the subject of this research report (and related derivatives thereof). BARC trading desks may have either a long and / or short position in such securities, other financial instruments and / or derivatives, which may pose a conflict with the interests of investing customers. Where permitted and subject to appropriate information barrier restrictions, BARC fixed income research analysts regularly interact with its trading desk personnel regarding current market conditions and prices. BARC fixed income research analysts receive compensation based on various factors including, but not limited to, the quality of their work, the overall performance of the firm (including the profitability of the Investment Banking Department), the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst. To the extent that any historical pricing information was obtained from BARC trading desks, the firm makes no representation that it is accurate or complete. All levels, prices and spreads are historical and do not necessarily represent current market levels, prices or spreads, some or all of which may have changed since the publication of this document. BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations and trade ideas contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://

publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

## Disclosure(s) regarding Information Sources

Bloomberg $^{\textregistered}$ is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”) and the Bloomberg Indices are trademarks of Bloomberg. Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Bloomberg does not approve or endorse this material, or guarantee the accuracy or completeness of any information herein, or make any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, Bloomberg shall have no liability or responsibility for injury or damages arising in connection therewith.

All pricing information is indicative only. Unless otherwise indicated, prices are sourced from LSEG Data & Analytics and reflect the closing price in the relevant trading market, which may not be the last available price at the time of publication.

## Types of investment recommendations produced by BARC FICC Research:

In addition to any ratings assigned under BARC' formal rating systems, this publication may contain investment recommendations in the form of trade ideas, thematic screens, scorecards or portfolio recommendations that have been produced by analysts in FICC Research. Any such investment recommendations produced by non-Credit Research teams shall remain open until they are subsequently amended, rebalanced or closed in a future research report. Any such investment recommendations produced by the Credit Research teams are valid at current market conditions and may not be otherwise relied upon.

## Disclosure of other investment recommendations produced by BARC FICC Research:

BARC FICC Research may have published other investment recommendations in respect of the same securities/instruments recommended in this research report during the preceding 12 months. To view all investment recommendations published by BARC FICC Research in the preceding 12 months please refer to https://live.barcap.com/go/research/Recommendations.

BARC does not assign ratings to asset backed securities. BARC Capital Inc. and/or one of its affiliates may have acted as an underwriter for public offerings of any asset backed securities that are otherwise recommended in trade ideas contained within its securitised research reports.

## Legal entities involved in producing BARC:

BARC Bank PLC (BARC, UK)

BARC Capital Inc. (BCI, US)

BARC Bank Ireland PLC, Frankfurt Branch (BBI, Frankfurt)

BARC Bank Ireland PLC, Paris Branch (BBI, Paris)

BARC Bank Ireland PLC, Milan Branch (BBI, Milan)

BARC Securities Japan Limited (BSJL, Japan)

BARC Bank PLC, Hong Kong Branch (BARC Bank, Hong Kong)

BARC | China

BARC Bank Mexico, S.A. (BBMX, Mexico)

BARC Capital Casa de Bolsa, S.A. de C.V. (BCCB, Mexico)

BARC Securities (India) Private Limited (BSIPL, India)

BARC Bank PLC, Singapore Branch (BARC Bank, Singapore)

BARC Bank PLC, DIFC Branch (BARC Bank, DIFC)

## Disclaimer:

This publication has been produced by BARC Department in the Investment Bank of BARC Bank PLC and/or one or more of its affiliate

[中间内容因长度限制已省略]

 scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
