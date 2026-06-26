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
CHINA BANKS

# Questions Arising from Strengthened Tax Supervision on BOC: Effective Tax Rate and Liquidity

According to news reports (link), China's National Audit Office reported that BOC evaded Rmb 2.367bn in taxes, representing approximately $1\%$ of its net profit. BOC's H-share price declined by more than $5\%$ at the last close, contributing to a $3\%$ decline in Chinese banks' H-shares. The news reports indicate that BOC achieved tax reductions by packaging private fund products as public funds. In light of this news, we see investors will likely focus on two key questions: 1) whether this reported incident could create upward pressure on banks' effective tax rates, potentially weighing on net profit; 2) whether interbank liquidity could tighten as a result.

Shuo Yang, Ph.D.
+852-2978-0701 | shuo.yang@gs.com
GS (Asia) L.L.C.

Claire Ouyang
+852-2978-6686 |
claire.x.ouyang@gs.com
GS (Asia) L.L.C.

Our view is as follows:

## 1. The effective tax rate for Chinese banks is unlikely to rise materially as a result of the news report.

This is mainly because the decline in effective tax rates in recent years has primarily been driven by banks' purchases of government bonds, which are tax-exempt. While income generated from banks' holdings of mutual funds may also qualify for tax exemptions, the volume of newly acquired government bonds far exceeds that of newly acquired public funds.

Based on available data, using the four large banks as an example, the aggregate increase in government bond holdings reached Rmb 16tn over the past three years, while the total increase in fund investments amounted to Rmb 0.3tn (Exhibit 1, Exhibit 2). Therefore, government bonds predominantly contribute to the growth of low-tax assets.

We also expect that large banks will continue to increase their holdings of government bonds, due to 1) credit deployment needs, and 2) enhanced comprehensive returns derived from tax exemptions and capital relief associated with government bonds. Therefore, even if regulatory oversight tightens or rules change, leading to reduction in tax incentives for mutual funds, it is unlikely this will alter the broader trend of large banks maintaining persistently low effective tax rates.

Our model indicates that the average effective tax rate of the four large banks was 13% over the past three years, with a projected average of 12% for the next three years (Exhibit 3), mainly reflecting the tax-exempt effect and continued increases in

government bond holdings.

## 2. Stricter taxation on banks' mutual fund holdings is unlikely to materially affect interbank market liquidity.

This is largely because banks utilize mutual funds (such as money market funds) to support their interbank deposits, effectively providing liquidity for interbank liabilities, in addition to the aforementioned tax-exempt benefits of mutual funds. Therefore, for banks, holding mutual funds allows them to access interbank liabilities while also generating tax-exempt income.

Firstly, we believe tax exemption rules for specific mutual funds (particularly money market funds) are unlikely to change in the short term, as tax exemption is an important measure to support the development of the mutual fund industry. Second, based on the recent Lujiazui Forum (see here), we think a downward shift in the center of the interest rate corridor (Exhibit 4) and new liquidity support for non-bank financial institutions should help maintain ample interbank liquidity.

Therefore, we do not expect strengthened tax supervision of mutual funds to cause meaningful tightness in interbank market liquidity. However, our recent discussions with banks indicate a less optimistic outlook on NIM guidance than before. This is primarily because, while deposit costs continue their downward trend, the pace of reduction is expected by the banks to gradually narrow, thereby progressively weakening support for NIM. Our stock selection framework for the banking sector remains unchanged; amid a slowdown in industry loan growth, we continue to prefer banks that can maintain their NIM and asset quality, strengthen their balance sheets, and stabilize their ROE. We still prefer large banks (such as BOC, CCB) and BONB.

The authors would like to thank Zihan Wang for her contribution to this report.

Exhibit 1: Taking the four large banks as an example, the aggregate increase in government bond holdings reached Rmb 16tn over the past three years ...  
![](images/ea5237cde586cdffbba98f38252613e55b3f1d93cdb1f4901e49d5b7dc398aad.jpg)  
Note: the large four banks are ICBC, CCB, ABC, BOC  
Source: Company data

Exhibit 2: ...whereas the total increase in fund investments amounted to Rmb 0.3tn. Therefore, government bonds predominantly contribute to the growth of low-tax assets  
![](images/32c0a46898c23cd97538f3f3a028957798b3f3ea593416faa33aa5af1be9f46d.jpg)  
Due to data availability, mutual fund investments are proxied by “Fund Investments and Others” under the FVTPL category, potentially higher than the actual asset balance.

Exhibit 3: Our model indicates that the average effective tax rate of the four large banks was 13% over the past three years, with a projected average of 12% for the next three years, mainly reflecting the tax-exempt effect and the continued increase in holdings of government bonds.

![](images/b8899b86f1ba2a568d1ea8bd238a0a2b2995e730a9ed613b84922d6f50759264.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: Based on the recent Lujiazui Forum, our conclusion is that a downward shift in the center of the interest rate corridor and new liquidity support for non-bank financial institutions should help maintain ample interbank liquidity

![](images/894e16e1523e21486a80b9a14a6878556b75db423f9f2bc649fa81a280dbd130.jpg)  
From GS macro team. The grey dashed lines represent the corridor defined by the temporary overnight OMOs.

Source: Wind, GS Global Investment Research

Exhibit 5: Covered banks NIM comparison

<table><tr><td colspan="7">NIM (GS calculated)</td></tr><tr><td></td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>ICBC</td><td>1.57</td><td>1.38</td><td>1.26</td><td>1.22</td><td>1.20</td><td>1.20</td></tr><tr><td>BOC</td><td>1.56</td><td>1.36</td><td>1.23</td><td>1.20</td><td>1.18</td><td>1.18</td></tr><tr><td>CCB</td><td>1.70</td><td>1.50</td><td>1.33</td><td>1.28</td><td>1.25</td><td>1.25</td></tr><tr><td>ABC</td><td>1.54</td><td>1.39</td><td>1.24</td><td>1.18</td><td>1.16</td><td>1.15</td></tr><tr><td>BoCom</td><td>1.24</td><td>1.20</td><td>1.16</td><td>1.16</td><td>1.13</td><td>1.13</td></tr><tr><td>PSBC</td><td>1.89</td><td>1.75</td><td>1.58</td><td>1.54</td><td>1.51</td><td>1.50</td></tr><tr><td>CMB</td><td>2.05</td><td>1.84</td><td>1.73</td><td>1.69</td><td>1.67</td><td>1.67</td></tr><tr><td>Industrial</td><td>1.54</td><td>1.47</td><td>1.41</td><td>1.34</td><td>1.34</td><td>1.34</td></tr><tr><td>PAB</td><td>2.20</td><td>1.67</td><td>1.53</td><td>1.48</td><td>1.46</td><td>1.45</td></tr><tr><td>HuaXia</td><td>1.74</td><td>1.46</td><td>1.40</td><td>1.47</td><td>1.47</td><td>1.48</td></tr><tr><td>BONB</td><td>1.62</td><td>1.66</td><td>1.59</td><td>1.56</td><td>1.56</td><td>1.55</td></tr><tr><td>BONJ</td><td>1.18</td><td>1.10</td><td>1.25</td><td>1.25</td><td>1.20</td><td>1.20</td></tr><tr><td colspan="7">Average</td></tr><tr><td>Total</td><td>1.65</td><td>1.48</td><td>1.39</td><td>1.36</td><td>1.34</td><td>1.34</td></tr><tr><td>Large</td><td>1.58</td><td>1.43</td><td>1.30</td><td>1.26</td><td>1.24</td><td>1.24</td></tr><tr><td>Joint-stock</td><td>1.88</td><td>1.61</td><td>1.52</td><td>1.49</td><td>1.48</td><td>1.49</td></tr><tr><td>Regional</td><td>1.40</td><td>1.38</td><td>1.42</td><td>1.41</td><td>1.38</td><td>1.38</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 6: Covered banks LDR comparison

<table><tr><td colspan="7">LDR</td></tr><tr><td></td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>ICBC</td><td>87%</td><td>85%</td><td>88%</td><td>88%</td><td>88%</td><td>88%</td></tr><tr><td>BOC</td><td>87%</td><td>89%</td><td>89%</td><td>89%</td><td>89%</td><td>88%</td></tr><tr><td>CCB</td><td>86%</td><td>90%</td><td>90%</td><td>89%</td><td>89%</td><td>89%</td></tr><tr><td>ABC</td><td>78%</td><td>82%</td><td>83%</td><td>83%</td><td>84%</td><td>84%</td></tr><tr><td>BoCom</td><td>93%</td><td>97%</td><td>98%</td><td>98%</td><td>99%</td><td>99%</td></tr><tr><td>PSBC</td><td>58%</td><td>58%</td><td>58%</td><td>58%</td><td>58%</td><td>58%</td></tr><tr><td>CMB</td><td>79%</td><td>75%</td><td>73%</td><td>72%</td><td>72%</td><td>71%</td></tr><tr><td>Industrial</td><td>105%</td><td>102%</td><td>99%</td><td>98%</td><td>97%</td><td>96%</td></tr><tr><td>PAB</td><td>99%</td><td>94%</td><td>93%</td><td>93%</td><td>92%</td><td>91%</td></tr><tr><td>HuaXia</td><td>107%</td><td>108%</td><td>107%</td><td>105%</td><td>104%</td><td>104%</td></tr><tr><td>BONB</td><td>79%</td><td>79%</td><td>84%</td><td>88%</td><td>92%</td><td>96%</td></tr><tr><td>BONJ</td><td>79%</td><td>82%</td><td>83%</td><td>84%</td><td>85%</td><td>86%</td></tr><tr><td colspan="7">Average</td></tr><tr><td>Total</td><td>86%</td><td>87%</td><td>87%</td><td>87%</td><td>87%</td><td>88%</td></tr><tr><td>Large</td><td>82%</td><td>84%</td><td>84%</td><td>84%</td><td>84%</td><td>84%</td></tr><tr><td>Joint-stock</td><td>97%</td><td>95%</td><td>93%</td><td>92%</td><td>91%</td><td>91%</td></tr><tr><td>Regional</td><td>79%</td><td>81%</td><td>84%</td><td>86%</td><td>89%</td><td>91%</td></tr></table>

Source: Company data, GS Global Investment Research

## Price Target Risks and Methodology - Bank of China

Valuation: We are Buy rated on BOC A/H with 12-month target prices of Rmb6.72/HK\$5.95. Our 2027E-based target P/PPOP multiples are 4.375x/3.875x for A/H shares.

Downside risks: 1) significantly higher-than-expected asset growth, impacting capital accumulation, 2) dividend payout ratio cut, 3) continued deterioration in asset quality.

## Price Target Risks and Methodology - China Construction Bank

Valuation: We are Buy rated on CCB A/H with 12m TPs of Rmb11.47/HK\$ 9.96. Our 2027E-based target P/PPOP multiples are 4.75x/4.125x for A/H shares.

Downside risks: 1) dividend payout ratio miss, 2) worse NIM and asset quality, 3) more capital requirement.

Price Target Risks and Methodology - Bank of Ningbo

Valuation: We are Buy rated on BONB with a 12-month target price of Rmb 41.29 based on 2027E P/PPOP multiple of 4.25x.

Key risks: Worse-than-expected NIM, asset quality and more-than-expected investment loss. Deposit outflow.

## Disclosure Appendix

## Reg AC

We, Shuo Yang, Ph.D. and Claire Ouyang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Shuo Yang, Ph.D. GS (Asia) L.L.C., Claire Ouyang GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Bank of China (A), Bank of China (H), Bank of Ningbo, China Construction Bank (A) and China Construction Bank (H) is/are relative to the other companies in its/their coverage universe: Agricultural Bank of China (A), Agricultural Bank of China (H), Bank of China (A), Bank of China (H), Bank of Communications (A), Bank of Communications (H), Bank of Nanjing, Bank of Ningbo, China Construction Bank (A), China Construction Bank (H), China Merchants Bank (A), China Merchants Bank (H), Hua Xia Bank, ICBC (A), ICBC (H), Industrial Bank, Ping An Bank Co., Postal Savings Bank of China Co. (A), Postal Savings Bank of China Co. (H)

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Bank of Ningbo (Rmb30.79)

GS has received compensation for investment banking services in the past 12 months: Bank of China (A) (Rmb5.79), Bank of China (H) (HK\$4.99), China Construction Bank (A) (Rmb9.81) and China Construction Bank (H) (HK\$8.30)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Bank of China (A) (Rmb5.79), Bank of China (H) (HK\$4.99), China Construction Bank (A) (Rmb9.81) and China Construction Bank (H) (HK\$8.30)

GS has received compensation for non-investment banking services during the past 12 months: Bank of China (A) (Rmb5.79), Bank of China (H) (HK\$4.99), Bank of Ningbo (Rmb30.79), China Construction Bank (A) (Rmb9.81) and China Construction Bank (H) (HK\$8.30)

GS had an investment banking services client relationship during the past 12 months with: Bank of China (A) (Rmb5.79), Bank of China (H) (HK\$4.99), China Construction Bank (A) (Rmb9.81) and China Construction Bank (H) (HK\$8.30)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Bank of China (A) (Rmb5.79), Bank of China (H) (HK\$4.99), Bank of Ningbo (Rmb30.79), China Construction Bank (A) (Rmb9.81) and China Construction Bank (H) (HK\$8.30)

GS had a non-securities services client relationship during the past 12 months with: Bank of China (A) (Rmb5.79), Bank of China (H) (HK\$4.99), Bank of Ningbo (Rmb30.79), China Construction Bank (A) (Rmb9.81) and China Construction Bank (H) (HK\$8.30)

GS makes a market in the securities or derivatives thereof: Bank of China (A) (Rmb5.79), Bank of China (H) (HK\$4.99), China Construction Bank (A) (Rmb9.81) and China Construction Bank (H) (HK\$8.30)

## Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td></tr></table>

<table><tr><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price targe

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
