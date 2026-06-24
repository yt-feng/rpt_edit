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
# China Brokers Sector Sector catchup on multiple tailwinds

## Rally on likely strong Q226 results and policy tailwinds

China brokerages (H) surged 6.1% on 22 June, against a 0.65% decline in the Hang Seng Index, flipping the sector into YTD outperformance of \~7pp (Figure 1). The rally, in our view, was driven by two catalysts. First, listed brokers are on track for strong Q2 results, underpinned by robust market activity Q2-to-date (see para 2). Second, policy tailwinds are building, including but not limited to last week's Lujiazui Forum (see para 3) and the Action Plan for Stabilizing and Optimizing Foreign Investment Attraction ('the Plan') issued jointly by MOFCOM, NDRC and MOF. The Plan extends derivative market access to foreign institutions, including treasury futures; and grants them fund advisory licenses, moves that could accelerate the industry's pivot toward a buy-side advisory model. Multiple policy tailwinds have emerged YTD. In May, CSRC rolled out the first departmental rules governing derivatives (UBS note), building toward long-term upside. In April, the regulator unveiled a new round of ChiNext reforms (UBS note), introducing a fourth set of listing criteria.

## Listed brokers are on track for strong Q2 results

CN brokers are poised for a strong Q2 (listed brokers recorded 39% YoY growth in Q1 recurring NPAT), with broad-based gains across major business lines. Market momentum has held firm into Q2. In Q2-to-date, A-share stock ADT jumped to Rmb2.8 trn, up 1.2x YoY (vs. Q1: +69% YoY) and 9% QoQ. Margin financing and securities lending balances rose to Rmb3.0 trn, up 62% YoY (vs. Q1: +36% YoY) and 14% QoQ. A-share IPO fundraising surged 65% YoY and 91% QoQ. Retail sentiment remained buoyant: new hybrid fund issuance reached Rmb96 bn, up 1.8x YoY, while new trading account openings hit 5.3mn in April-May, up 51% YoY. The CSI300 index rebounded 13.7% in Q2-to-date, reversing a 3.9% decline in Q1, a tailwind for brokers' investment portfolios. Leading brokers are well-placed to benefit from STAR market exposure, leveraging their integrated IB, research and investment capabilities via follow-on investment commitments and private equity holdings.

## Lujiazui Forum recap: market stability, tech narrative, and further opening-up

Lujiazui Forum struck a market-stabilization tone. Moves to attract long-term capital and broaden financial instruments (incl. active ETFs) should strengthen market structure, underpin trading volume and asset allocation flows, and facilitate a slow-bull market. Brokers would benefit across wealth management, brokerage and institutional businesses. On equity financing, regulators signalled more inclusive listing standards at STAR and ChiNext markets, with a focus on AI (STAR 5th Listing Criterion) and deep-tech sectors. Expanded support for M&A, refinancing, and onshore listings of eligible HK-listed companies should boost deal flow and lift investment banking revenues. On cross-border, regulators are advancing RMB FX futures pilots and backing HK's launch of 5-year RMB treasury futures, while directing flows through Stock Connect, QDII, and Cross-border WM Connect.

## Stock call: CICC (H), CITICS (A/H), HTSC (A/H) and GTHT (A)

We see a re-rating opportunity in the sector, underpinned by likely strong Q2 results and easing selling pressure. Despite the recent rally, YTD China brokerages (H) and (A) were down 0.4% and 6.8% respectively, against the Hang Seng Index down 7.3% with the CSI300 index up 9.3%. We expect medium- to long-term tailwinds to remain intact, with leading brokers set to benefit disproportionately from stronger regulatory support, broader non-brokerage franchises, higher pricing power and accelerating industry consolidation. Our covered brokers are trading at an average of 1.2x/0.8x 2026E PB, which we view as undemanding given the improving earnings outlook and structural growth drivers. We prefer CICC (H), CITICS (A/H), HTSC (A/H) and GTHT (A).

## Equities

China

Financial Services

Dennis Bai

Analyst

dennis.bai@ubs.com

+852-3712 2473

Wen Chen, CPA

Associate

S1460524120002

wen.chen@ubs.com

+86-21-3866 8259

Figure 1: Broker sector stock performance

<table><tr><td>Ticker</td><td>Name</td><td>Date</td><td>Price</td><td>2026-06-22</td><td>WTD</td><td>MTD</td><td>QTD</td><td>YTD</td><td>FY25</td></tr><tr><td>HSI.HI</td><td>HSI</td><td>2026-06-22</td><td>23,768.52</td><td>-0.7%</td><td>-0.7%</td><td>-5.6%</td><td>-4.1%</td><td>-7.3%</td><td>27.8%</td></tr><tr><td>887640.WI</td><td>CN Broker Index</td><td>2026-06-22</td><td>1,429.22</td><td>6.1%</td><td>6.1%</td><td>11.5%</td><td>18.6%</td><td>-0.4%</td><td>36.7%</td></tr><tr><td>6030.HK</td><td>CITICS</td><td>2026-06-22</td><td>28.36</td><td>6.1%</td><td>6.1%</td><td>8.9%</td><td>21.4%</td><td>5.4%</td><td>31.5%</td></tr><tr><td>3908.HK</td><td>CICC</td><td>2026-06-22</td><td>21.72</td><td>7.8%</td><td>7.8%</td><td>10.7%</td><td>26.5%</td><td>11.0%</td><td>54.2%</td></tr><tr><td>6886.HK</td><td>HTSC</td><td>2026-06-22</td><td>17.73</td><td>4.7%</td><td>4.7%</td><td>11.9%</td><td>19.7%</td><td>-5.8%</td><td>48.4%</td></tr><tr><td>2611.HK</td><td>GTHT</td><td>2026-06-22</td><td>15.45</td><td>5.2%</td><td>5.2%</td><td>18.3%</td><td>18.9%</td><td>-4.4%</td><td>54.6%</td></tr><tr><td>6881.HK</td><td>CGS</td><td>2026-06-22</td><td>7.98</td><td>5.3%</td><td>5.3%</td><td>2.8%</td><td>1.0%</td><td>-20.4%</td><td>46.7%</td></tr><tr><td>6178.HK</td><td>EBS</td><td>2026-06-22</td><td>8.02</td><td>3.6%</td><td>3.6%</td><td>7.5%</td><td>5.8%</td><td>-9.8%</td><td>13.9%</td></tr><tr><td>6066.HK</td><td>CSC</td><td>2026-06-22</td><td>12.86</td><td>8.6%</td><td>8.6%</td><td>13.3%</td><td>24.1%</td><td>0.2%</td><td>35.1%</td></tr><tr><td>6099.HK</td><td>CMS</td><td>2026-06-22</td><td>17.41</td><td>4.3%</td><td>4.3%</td><td>18.9%</td><td>32.7%</td><td>24.9%</td><td>-9.6%</td></tr><tr><td>3958.HK</td><td>Orient</td><td>2026-06-22</td><td>6.10</td><td>6.6%</td><td>6.6%</td><td>7.2%</td><td>13.0%</td><td>-10.8%</td><td>40.8%</td></tr><tr><td>1776.HK</td><td>GFS</td><td>2026-06-22</td><td>18.60</td><td>9.7%</td><td>9.7%</td><td>15.2%</td><td>29.2%</td><td>5.6%</td><td>74.7%</td></tr><tr><td>6806.HK</td><td>SWHY</td><td>2026-06-22</td><td>2.69</td><td>5.5%</td><td>5.5%</td><td>3.9%</td><td>-0.7%</td><td>-11.5%</td><td>35.6%</td></tr><tr><td>000300.SH</td><td>CSI 300</td><td>2026-06-22</td><td>5,059.66</td><td>2.4%</td><td>2.4%</td><td>3.4%</td><td>13.7%</td><td>9.3%</td><td>17.7%</td></tr><tr><td>886054.WI</td><td>Broker Index</td><td>2026-06-22</td><td>10,597.72</td><td>7.5%</td><td>7.5%</td><td>9.4%</td><td>9.8%</td><td>-6.8%</td><td>4.1%</td></tr><tr><td>600030.SH</td><td>CITICS</td><td>2026-06-22</td><td>28.64</td><td>7.8%</td><td>7.8%</td><td>11.7%</td><td>21.1%</td><td>2.4%</td><td>-0.7%</td></tr><tr><td>601995.SH</td><td>CICC</td><td>2026-06-22</td><td>35.44</td><td>6.1%</td><td>6.1%</td><td>4.9%</td><td>9.4%</td><td>1.3%</td><td>4.4%</td></tr><tr><td>601688.SH</td><td>HTSC</td><td>2026-06-22</td><td>21.29</td><td>8.9%</td><td>8.9%</td><td>17.1%</td><td>19.6%</td><td>-9.7%</td><td>37.4%</td></tr><tr><td>601211.SH</td><td>GTHT</td><td>2026-06-22</td><td>18.15</td><td>5.0%</td><td>5.0%</td><td>18.0%</td><td>9.4%</td><td>-11.7%</td><td>12.6%</td></tr><tr><td>601881.SH</td><td>CGS</td><td>2026-06-22</td><td>13.04</td><td>7.9%</td><td>7.9%</td><td>6.2%</td><td>2.4%</td><td>-17.0%</td><td>5.2%</td></tr><tr><td>601788.SH</td><td>EBS</td><td>2026-06-22</td><td>15.05</td><td>6.1%</td><td>6.1%</td><td>5.5%</td><td>-1.2%</td><td>-14.2%</td><td>-1.9%</td></tr><tr><td>601066.SH</td><td>CSC</td><td>2026-06-22</td><td>27.39</td><td>10.0%</td><td>10.0%</td><td>12.3%</td><td>27.7%</td><td>2.9%</td><td>4.6%</td></tr><tr><td>600999.SH</td><td>CMS</td><td>2026-06-22</td><td>19.65</td><td>5.8%</td><td>5.8%</td><td>15.7%</td><td>27.3%</td><td>18.1%</td><td>-10.6%</td></tr><tr><td>600958.SH</td><td>Orient</td><td>2026-06-22</td><td>9.76</td><td>6.0%</td><td>6.0%</td><td>4.8%</td><td>8.0%</td><td>-10.5%</td><td>5.4%</td></tr><tr><td>000776.SZ</td><td>GFS</td><td>2026-06-22</td><td>22.70</td><td>10.0%</td><td>10.0%</td><td>20.2%</td><td>26.4%</td><td>3.1%</td><td>39.6%</td></tr><tr><td>000166.SZ</td><td>SWHY</td><td>2026-06-22</td><td>4.63</td><td>5.0%</td><td>5.0%</td><td>5.0%</td><td>-1.1%</td><td>-12.1%</td><td>0.0%</td></tr><tr><td>601377.SH</td><td>Industrial</td><td>2026-06-22</td><td>6.24</td><td>7.2%</td><td>7.2%</td><td>8.5%</td><td>6.3%</td><td>-15.9%</td><td>21.1%</td></tr><tr><td>002736.SZ</td><td>Guosen</td><td>2026-06-22</td><td>10.37</td><td>5.3%</td><td>5.3%</td><td>6.1%</td><td>-4.2%</td><td>-17.5%</td><td>20.9%</td></tr><tr><td>601555.SH</td><td>Soochow</td><td>2026-06-22</td><td>8.06</td><td>6.3%</td><td>6.3%</td><td>2.8%</td><td>2.8%</td><td>-11.0%</td><td>21.3%</td></tr><tr><td>600109.SH</td><td>Sinolink</td><td>2026-06-22</td><td>8.99</td><td>6.5%</td><td>6.5%</td><td>3.7%</td><td>7.3%</td><td>-3.3%</td><td>7.9%</td></tr><tr><td>000783.SZ</td><td>Changjiang</td><td>2026-06-22</td><td>8.60</td><td>10.0%</td><td>10.0%</td><td>10.1%</td><td>30.4%</td><td>9.8%</td><td>22.2%</td></tr></table>

Source: Wind, UBS

Figure 2: A-share equity-linked ADT rose 95% YoY to Rmb3.2 trn in 5M26  
![](images/1d208b096dea02e09f09347055b29cef672fb7c5613bc4ce8c8dcdb5002a7ed0.jpg)  
Source: Wind, UBS estimates

Figure 3: Margin financing and securities lending balances rose to Rmb3.0 trn, up 62%/14% YoY/QoQ  
![](images/d2e56f747880e175fedd3d8f916215ff70d752a65bb3e3de4e318dbce16bbc56.jpg)  
Source: Wind, UBS estimates

Figure 4: YTD A share IPO underwriting value +62% YoY  
![](images/7a03c24252ded15807e47b40dfa9e3f9ba686b03dd7acc9ba218e5652ee7f5c4.jpg)  
Source: Wind, UBS estimates

Figure 5: YTD A share refinancing underwriting value down 45% YoY  
![](images/a85cf8a1cf43dca9be202c85ece253cb0e12cf59959d1444ba671ea312dd2ff4.jpg)  
Source: Wind, UBS estimates. Note: the 2025 comparable base was boosted by private placement fund-raisings of several state-owned banks.

## Valuation Method and Risk Statement

We believe main risks to China's securities sector include: 1) a market downturn and greater access to licenses, leading to increased industry competition; 2) risk of sustained commission decreases; 3) the scale of margin financing, share pledges and other capital intermediary services is lower than expected and thus contributes less to earnings than expected; 4) regulatory penalties; 5) innovation-related failures that could lead to reputational loss, the loss of customers, lawsuits or other risks; and 6) lower-than-expected earnings or other risks due to fluctuations in investment income.

CITIC-A/H: Our price target is based on P/BV-ROE methodology for CITIC-A and DDM for CITIC-H. We think the main upside risks for the stock include: 1) higher-than-expected activity in the A-share market; 2) decreasing regulatory risk; and 3) faster-than-expected business development driving earnings to overshoot estimates. The main downside risks include: 1) brokers experiencing lower earnings and de-rating amid a protracted A-share slump; 2) slower-than-expected progress in innovative segments; and 3) large-scale employee turnover leading to sharp declines in market share and earnings.

Huatai-A/H: Our price target is based on P/BV-ROE for Huatai-A and DDM for Huatai-H. We believe key downside risks facing the company include: the opening-up of off-site account opening, internet applications and increasing lite outlets (engaged in trading and margin financing only) could intensify brokerage competition, causing commission rates to decline in the medium-to-long-term; if debt financing increases and interest expenses rise, margin financing, share pledges and other capital intermediary services may make less-than-expected earnings contribution; failure in innovation may lead to reputational damage, customer losses, litigation, regulatory penalties, etc; volatile securities market investment return, persistently sluggish trading, etc.

CICC-H: Our price target is based on DDM for CICC-H. We think the main downside risks include: 1) brokers experiencing lower earnings and downward re-ratings amid a protracted A-share slump; 2) slower-than-expected progress in innovative segments; and 3) fiercer competition in the brokerage business and declining commission rates in the medium to long term.

GTHT-A: Our price target is based on a P/BV–ROE methodology. Downside risks include: 1) disappointing outcomes from the merger; 2) weaker-than-expected profit contributions from capital intermediary services such as margin financing and equity pledge loans amid higher debt financing and interest expenses; 3) continued volatility in investment returns, subdued market trading activity; and 4) the risk of Haitong International remaining loss-making in its investment operations.

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 22 June 2026 04:02 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>54%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 31 March 2026.  
1: Percentage of companies under coverage globally within the 12-month rating category.

2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE): Exceptions to the standard +/-6% bands may be granted by the Investment Review Consultation (IRC). Factors considered by the IRC include the stock's volatility and the credit spread of the respective company's debt. As a result, stocks deemed to be very high or low risk may be subject to higher or lower bands as they relate to the 

[中间内容因长度限制已省略]

lated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
