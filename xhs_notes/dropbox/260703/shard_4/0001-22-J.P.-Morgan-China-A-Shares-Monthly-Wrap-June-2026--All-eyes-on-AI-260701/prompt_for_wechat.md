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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China A-Shares Monthly Wrap

June 2026: All eyes on AI

\- Key market drivers: CSI-300/500/1000 recorded +1.8%/8.0%/4.8% in June, outperforming HSI's/HSCEI's -9.1%/-10.3%, respectively. Such a significant contrast reflects investor confidence in China's AI ecosystem, in particular the infrastructure side, while taking a more cautious and selective stance in the China internet space. Abundant liquidity onshore, as evidenced by A-share velocity surging to over 6%, supported such style preference for growth. Offshore investors we spoke with have increasingly been asking about the likelihood of another round of stimulus to be announced around the July politburo meeting, suggesting rising appetite to bottom-fish consumption proxies. That said, feedback from local clients we spoke with suggests expectations on stimulus remain low onshore.

\- Key sector moves: IT, Materials and Financials took the lead over the past month, while Utilities, Energy and Real Estate underperformed (Figure 1).

\- Earnings and valuation: Consensus CSI-300 2026E EPS growth stayed at $24\%$ at end-June. On 30 June, it traded at a 14.6x FTM P/E, or c1.7SD vs median since 2016, and at a 0.7x FTM PEG with FTM EPS y-y of $19.7\%$ . YTD, materials, IT and energy have recorded the strongest FTM EPS integer upward revisions, while communication services, consumer staples and utilities have recorded the biggest FTM EPS integer downward revisions.

\- Key macro data: China's May activity data improved in certain areas, but overall remained soft. IP improved to 0.2% m-m sa, or 4.5% y-y, rebounding from a sharp monthly contraction in April, though the trend pace slowed further to 1% 3m-3m saar. Retail sales softened further, falling 0.6% oya on a 0.1% m/m sa decline. Auto retail sales plunged a further 16.4% oya. FAI contracted sharply by 10.7% oya (vs -8.0% April), dragging ytd FAI further into contraction at -4.1% oya ytd (vs +1.7% in 1Q). By sector, real estate FAI (-24.3% oya) fell the most. May inflation continued the trend with CPI staying soft with PPI continuing to be firm, at a slower pace. AI-related cost pass-through is broadening into upstream semis and downstream electronics, adding a more durable inflation tailwind. Meanwhile, AI-related high-tech also boosted May exports, with a growing price lift (memory chips/modules, AI datacenter equipment, and new energy). FX reserves rose US\$31.7bn to \$3442.2bn. USD/CNY largely stayed flat and ended at c6.79, while the 10-year CGB yield ticked up to 1.72% at end June.

Figure 1: A-share sector returns and top/bottom stock returns (issue market cap >US\$5bn)

<table><tr><td colspan="3">A-share sector returns</td><td colspan="3">A-share stock returns</td><td colspan="3">HK &amp; US listed CN stock returns</td></tr><tr><td>Sector</td><td>1M (%)</td><td>YTD (%)</td><td>Ticker</td><td>Company</td><td>1M (%)</td><td>Ticker</td><td>Company</td><td>1M (%)</td></tr><tr><td>IT</td><td>19.6</td><td>63.1</td><td>002636.SZ</td><td>GDM</td><td>124.2</td><td>ACMR.O</td><td>ACM RESEARCH INC</td><td>37.3</td></tr><tr><td>Materials</td><td>2.7</td><td>9.8</td><td>002409.SZ</td><td>YOKE TECHNOLOGY</td><td>109.1</td><td>1347.HK</td><td>HUA HONG SEMICONDUCTOR LTD</td><td>33.4</td></tr><tr><td>Financials</td><td>-1.3</td><td>-12.4</td><td>000725.SZ</td><td>BOE</td><td>71.4</td><td>2359.HK</td><td>WUXI APTEC CO LTD</td><td>18.0</td></tr><tr><td>Healthcare</td><td>-3.1</td><td>-10.0</td><td>000811.SZ</td><td>YANTAI MOON</td><td>71.1</td><td>2611.HK</td><td>GTJA SECURITIES CO LTD</td><td>13.7</td></tr><tr><td>Industrials</td><td>-4.7</td><td>-0.2</td><td>000021.SZ</td><td>KAIFA</td><td>62.4</td><td>6869.HK</td><td>YANGTZE OPTICAL FIBRE AND CABLE ,</td><td>12.4</td></tr><tr><td>Cons. Discre.</td><td>-9.2</td><td>-17.7</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Communication services</td><td>-9.5</td><td>-16.9</td><td>002128.SZ</td><td>OPENCUT COAL</td><td>-25.3</td><td>2688.HK</td><td>ENN ENERGY HOLDINGS LTD</td><td>-26.3</td></tr><tr><td>Cons. Staples</td><td>-10.3</td><td>-19.6</td><td>000933.SZ</td><td>SHENHUO</td><td>-27.0</td><td>2382.HK</td><td>SUNNY OPTICAL TECHNOLOGY GROU $\dagger$ </td><td>-27.2</td></tr><tr><td>Real Estate</td><td>-10.6</td><td>-16.4</td><td>001979.SZ</td><td>CMSK</td><td>-27.1</td><td>0285.HK</td><td>BYD ELECTRONIC INTERNATIONAL CO</td><td>-28.3</td></tr><tr><td>Energy</td><td>-12.2</td><td>-0.8</td><td>002532.SZ</td><td>SHIMGE PUMP</td><td>-28.1</td><td>1378.HK</td><td>CHINA HONGQIAO GROUP LTD</td><td>-28.4</td></tr><tr><td>Utilities</td><td>-14.1</td><td>0.9</td><td>002379.SZ</td><td>LOFTEN</td><td>-30.5</td><td>6181.HK</td><td>LAOPU GOLD CO LTD</td><td>-31.3</td></tr></table>

Source: LSEG Workspace (30 Jun 2026), Wind (30 Jun 2026). Data as of 30 Jun 2026 HKT market close.

## Equity Macro Research

Erin Zhang, CFA AC
(86-21) 6106 6328
erin.zhang@JPM.com
SAC Registration Number: S1730521090002
JPM Securities (China) Company Limited

(852) 2800-4323
tim.huang@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

Rajiv Batra
(65) 6882-8151
rajiv.j.batra@JPM.com
JPM Securities Singapore Private Limited

## Greater China Economics

Feng Zhu
(852) 2800 1745
feng.zhu@JPM.com
JPM Chase Bank, N.A., Hong Kong Branch

Tingting Ge
(852) 2800-0143
tingting.ge@JPM.com
JPM Chase Bank, N.A., Hong Kong Branch

## Head of China Research

Alex Yao
(86 21) 6106 6505
alex.yao@JPM.com
SAC Registration Number: S1730523020001
JPM Securities (China) Company Limited

## Equity review and YTD returns

With key China equity return drivers summarized on the front page, we detail below the top- and bottom-ranked Wind A-share Level 1 sector returns.

## Top 3 performing sectors

\- IT (+20%) continued its lead on AI infrastructure proxies in June.

\- Materials (+3%) saw AI-related materials, e.g., fiber glass and MLCC materials, recording strong return, offset by the retreat in gold and aluminum names.

\- Financials (-1%) saw diverging performance between the outperforming non-bank financials, notably brokers as a catch-up beta trade, and the underperforming banks that suffer from penalties due to regulatory tightening

## Bottom 3 performing sectors

\- Utilities (-14%) corrected on overall macro weakness, while yield as a factor is also out of favor for now.

\- Energy (-12%) retreated on lower oil price due to a potential reopening of the Strait of Hormuz.

\- Real Estate (-11%) corrected as industry data fails to sustain strong momentum.

Figure 2: Market performance

<table><tr><td>Sector</td><td>Jun 26 return</td><td>YTD return</td></tr><tr><td>CSI300</td><td>1.8%</td><td>7.5%</td></tr><tr><td>CSI500</td><td>8.0%</td><td>21.0%</td></tr><tr><td>CSI1000</td><td>4.8%</td><td>16.0%</td></tr><tr><td>Wind All A-shares</td><td>3.2%</td><td>11.5%</td></tr><tr><td>HSCEI</td><td>-10.3%</td><td>-15.2%</td></tr><tr><td>HSI</td><td>-9.1%</td><td>-10.7%</td></tr><tr><td>CSI300 Relative Growth</td><td>9.4%</td><td>26.9%</td></tr><tr><td>CSI300 Relative Value</td><td>-5.6%</td><td>-9.9%</td></tr><tr><td>Wind Dividend</td><td>-8.2%</td><td>-10.1%</td></tr></table>

Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 3: Wind A-share Level 2 sector indices' MTD/YTD returns  
![](images/9f0e9e558f336484593c6293858e8ae58aff0097accf912652cab891412b2b2a.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

## Fund flow, margin financing, issuance

EPFR data recorded -US\$0.4bn in net outflow from A-shares over 1-26 June 2026, led by outflows from Industrials, Financials, and Consumer Discretionary, with IT the only sector recording mild net inflow.

Figure 4: EPFR tracked net A-share flows  
![](images/99d129e68cd77d5b72109322dbc469b99a24cd2d6a95e49649baed7b512322b0.jpg)  
Source: EPFR (26 June 2026), JPM (26 June 2026).

Figure 5: Active global equity funds' China weights vs MSCI benchmarks  
![](images/f8dc6072121e42d1795808c003975771f829ae3cc8d378aee0b496311232c2e5.jpg)  
Source: EPFR, MSCI. Data as of end-May 2026.

Figure 6: Active AeJ/EM equity funds' China weights vs MSCI benchmarks  
![](images/8f42d27015fcc414e6c9246c941ffe6b352b029c62b537e9ff0efe0db34db361.jpg)  
Source: EPFR, MSCI. Data as of end-May 2026.

The A-share margin financing balance as a percentage of A-share market cap edged up to 2.85% at end-June (range of 1.8-3% since 2016), while gross margin buying as a percentage of total A-share turnover stayed around 10% (range of 5.3-12.8% since 2016).

Figure 7: A-share margin financing  
![](images/42be51334cc4f1ccce3ceed14c5fe179c3517765c8e3434b66c5a8f39b7e59cc.jpg)  
Source: Wind (29 June 2026), JPM (29 June 2026).

A-share equity mutual fund issuance remained stable Preliminary data recorded Rmb19bn/Rmb12bn equity/balanced fund issuance in June, while May's final numbers improved to Rmb26bn/Rmb56bn from the preliminary reading of Rm22bn/Rmb31bn.

Annual fundraising proceeds since 2016 have ranged Rmb40bn-419bn for equity funds (median Rmb143bn) and Rmb65bn-1,625bn for balanced funds (median Rmb234bn).

We estimate retail/controlling & strategic shareholders/domestic financial institutions/foreign investors held 43%/42%/12%/3% of A-shares' total market cap at end-2025, based on company shareholding data and the PBOC's statistics of foreign investors' holdings of A-shares, respectively.

## Figure 8: Onshore mutual fund issuance

Onshore mutual fund issuance (Rmb bn)  
![](images/0f52d90126af908c09ec5e16663a328be84f02f78d6556f9f4ee1cb3abead687.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026). Data as of 30 Jun 2026.

## CSI-300 EPS revisions and valuation

Consensus CSI-300 2026E EPS growth was 24% at end-June. On 30 June, it traded at a 14.6x FTM P/E, or c1.7SD vs median since 2016, and at a 0.7x FTM PEG with FTM EPS y-y of 19.7%.

Figure 9: CSI-300 FTM EPS revisions

<table><tr><td rowspan="2"></td><td rowspan="2">FTM EPS growth</td><td colspan="2">FTM EPS growth revision</td><td colspan="2">FTM EPS integer revision</td></tr><tr><td>Since end-Dec 2025</td><td>Since 20 Sep 2024</td><td>Since end-Dec 2025</td><td>Since 20 Sep 2024</td></tr><tr><td>Communication Services</td><td>11%</td><td>5%</td><td>9%</td><td>-13.4%</td><td>0.1%</td></tr><tr><td>Consumer Discretionary</td><td>13%</td><td>-2%</td><td>23%</td><td>-4.6%</td><td>55.4%</td></tr><tr><td>Consumer Staples</td><td>15%</td><td>5%</td><td>25%</td><td>-13.3%</td><td>8.3%</td></tr><tr><td>Energy</td><td>15%</td><td>8%</td><td>8%</td><td>14.6%</td><td>-17.8%</td></tr><tr><td>Financials</td><td>6%</td><td>1%</td><td>1%</td><td>1.9%</td><td>24.6%</td></tr><tr><td>Health Care</td><td>23%</td><td>13%</td><td>20%</td><td>2.0%</td><td>13.5%</td></tr><tr><td>Industrials</td><td>25%</td><td>1%</td><td>15%</td><td>2.9%</td><td>31.2%</td></tr><tr><td>IT</td><td>53%</td><td>10%</td><td>49%</td><td>25.5%</td><td>202.9%</td></tr><tr><td>Materials</td><td>38%</td><td>14%</td><td>18%</td><td>43.4%</td><td>69.0%</td></tr><tr><td>Utilities</td><td>3%</td><td>-3%</td><td>35%</td><td>-6.7%</td><td>44.2%</td></tr><tr><td>Real Estate</td><td>63%</td><td>-24%</td><td>-14.5%</td><td>-835.8%</td><td>-176.7%</td></tr><tr><td>CSI300</td><td>20%</td><td>5%</td><td>17%</td><td>5.7%</td><td>35.2%</td></tr></table>

Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 10: CSI-300 FTM P/E  
![](images/6996dda94f277e92f414d3d6c95a2b15bda9ba7a6e2ee463e07661f06450fed3.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 11: CSI-300 FTM P/E and EPS by sector  
![](images/d04f513dcc51a805fa9a47a17a812ebcb155378b30fb4012b83b02c07a1fcee3.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 12: CSI-300 consensus P/E-EPS metrics vs. other markets  
![](images/87768aa9016e06ccc11fc058d2e51b25c23a20653427cc72f7068c724b3255ac.jpg)  
Source: LSEG Workspace (30 Jun 2026), Wind (30 Jun 2026), JPM (30 Jun 2026). Note: All markets except for CSI-300 are based on MSCI market indices.

## Economic and political review

Average one-year CGB YTM ticked down by 1bp, and 10-year CGB YTM edged down 2bps. New loan creation returned to positive Rmb520bn, but quality was weak with most of the lift from corporate short-term loans and bill financing. Household loans and corporate medium- to long-term loans stayed in contraction, signaling genuine demand weakness. Loan growth slipped to 5.5% oya, a fresh record low; TSF softened to 7.7%..

## May activity recorded another month of broad weakness, though improved from April numbers.

Retail sales softened further, falling 0.6% oya on a 0.1% m/m sa decline. Auto retail sales plunged a further 16.4% oya (-1.1% m/m sa). Several categories recorded sharp declines: spending on household electronics fell 15.6% oya (vs -15.1% April), construction and decoration materials sales fell 13.6%, gold and silver jewelry fell 8.9%, and consumption of oil and related products fell 3.2%. Services spending continued to outperform: services retail sales grew 5.4% oya ytd in May, led by communications, software & information, leasing and business, financial, and transport and storage services. Online sales expanded further, with services outpacing goods.

FAI contracted sharply by 10.7% oya (vs -8.0% April), dragging ytd FAI further into contraction at -4.1% oya ytd (vs +1.7% in 1Q). By sector, real estate FAI (-24.3% oya) fell most and drove the decline, indicating a contraction stronger than seen in 1Q. Manufacturing (-4.2% oya) and infrastructure (-9.4%) also contracted. Within manufacturing, investment broadly cooled or contracted – led by special purpose equipment, chemicals, and pharmaceuticals – while high-tech manufacturing FAI held up better (electrical machinery and equipment, and computers, communications and other electronic equipment).

Industrial production improved to 4.5% oya. On a seasonally adjusted basis, IP rose 0.2%m/m sa but remained soft, rebounding from a sharp monthly contraction in April. The trend pace slowed further to 1.0%3m/3m saar. Industrial restructuring towards high-end manufacturing continued apace, with high-tech and equipment manufacturing outperforming, riding on the tech cycle upswing and policy support: growth accelerated to 15.1% oya and 9.5%, up from 12.8% and 7.2%, respectively. Production of 3D printing equipment, lithium-ion batteries, industrial robots and integrated circuits increased by 54.4%, 40.0%, 27.9%, and 22.9%, respectively. The pace of production of computers, communication and other electronic equipment accelerated to 17.0% oya, up from 15.6% in April.

On inflation, CPI inched up 0.1%m/m sa, or 1.2% y-y, as firmer communications/entertainment prices were offset by ongoing food-price deflation. PPI extended its upturn, rising 0.8%m/m sa or 3.9%oya. Relative to last month, the lift came from industrial upgrading and AI-driven compute demand, pushing up metals, electrical machinery and electronics prices.

Figure 13: Chinese consumer confidence and SME development  
![](images/4e5a3e67d10f0e21e94b94274e5bf78502a679491fdfdaa0cb0c42d19bbaf484.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 14: Chinese government bond yield to maturity (CGB YTM)  
![](images/e03969c9ac4f0027446191d67f3e66fd4d439eb1d60273481c1d2402a3957067.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 15: Key macro indicators

<table><tr><td>Macro indicators</td><td>2026-06F</td><td>2026-05F</td><td>2026-05</td><td>2026-04</td></tr><tr><td>CPI (%)</td><td>1.2</td><td>1.4</td><td>1.2</td><td>1.2</td></tr><tr><td>PPI (%)</td><td>4.2</td><td>3.5</td><td>3.9</td><td>2.8</td></tr><tr><td>Industrial production (%)</td><td>5.6</td><td>--</td><td>5.4</td><td>5.6</td></tr><tr><td>FAI YTD y-y (%)</td><td>-3.7</td><td>-1.7</td><td>-4.1</td><td>-1.6</td></tr><tr><td>Manufacturing FAI YTD y-y (%)</td><td>0.3</td><td>0.1</td><td>-0.4</td><td>1.2</td></tr><tr><td>Infrastructure FAI YTD y-y (%)</td><td>3.7</td><td>2.1</td><td>0.8</td><td>4.9</td></tr><tr><td>Real estate FAI YTD y-y (%)</td><td>-15.0</td><td>-14.6</td><td>-16.2</td><td>-13.7</td></tr><tr><td>Social retail sales y-y (%)</td><td>0.3</td><td>0.1</td><td>-0.6</td><td>0.2</td></tr><tr><td>Imports y-y (%)</td><td>26.7</td><td>20.2</td><td>27.4</td><td>25.2</td></tr><tr><td>Exports y-y (%)</td><td>16.7</td><td>12.3</td><td>19.4</td><td>14.0</td></tr><tr><td>M2 y-y (%)</td><td>8.3</td><td>8.6</td><td>8.6</td><td>8.6</td></tr><tr><td>Rmb loans y-y (%)</td><td>5.7</td><td>5.5</td><td>5.5</td><td>5.6</td></tr><tr><td>TSF y-y (%)</td><td>7.8</td><td>7.6</td><td>7.7</td><td>7.8</td></tr><tr><td>Official manufacturing PMI</td><td>50.0</td><td>50.3</td><td>50.0</td><td>50.3</td></tr><tr><td>Urban survey-based unemployment rate (%)</td><td>--</td><td>5.2</td><td>5.1</td><td>5.2</td></tr></table>

Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if app

[中间内容因长度限制已省略]

re subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND

DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
