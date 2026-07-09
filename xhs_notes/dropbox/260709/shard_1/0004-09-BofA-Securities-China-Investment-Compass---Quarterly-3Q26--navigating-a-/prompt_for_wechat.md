你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`BofA`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份BofA研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Investment Compass - Quarterly

# 3Q26: navigating a K-shaped market

Equity Strategy

## A stock pickers' market with diverging performance

China equities posted divergent performance in 2Q: MSCI China/HSCEI fell 7.6%/9.8%, while ChiNext/STAR 50 surged 38.6%/78.6%, highlighting the gap between internet-heavy HK benchmarks and A-share growth indices. Globally, macro events (eg Iran conflict, the Trump-Xi meeting) had limited market impact, while AI capex drove earnings upgrades across tech supply chains. Positioning became more concentrated and crowded, volatility is elevated, and retail leverage (incl leveraged ETFs) amplified market swings. Sentiment became more fragile amid inflation and liquidity concerns. We continue to view China as a stock pickers' market, with A-shares likely to outperform H-shares until the global AI rally unwinds. We maintain our barbell strategy, favoring both value/yield and sectors with strong earnings support and R.E.A.L. moats.

## Market: inexpensive, but not yet compelling

MSCI China fell 7.6% in 2Q26 in USD terms, underperforming global markets (vs MSCI World: +14.5%, MSCI EM: +23.3%). Within MSCI China, IT was the only sector with positive return in 2Q (+36.7%), while Consumer Discretionary (-20.7%), Consumer Staples (-18.6%) and Materials (-18.3%) were the worst performers. The index currently trades at 10.3x forward P/E, a 12% discount to its long-term average, but still above the historical trough of 8-9x. Earnings remain challenged, with consensus 2026E EPS growth revised down from 11-12% in Jan to 2-3% now. Flow-wise, liquidity pressures are building in 3Q, with nearly HKD540bn of lock-up expiries and a strong IPO pipeline.

## Macro: uneven growth with continued domestic softness

China Investment Compass (CIM) should mostly be in the C4/stimulating phase in 2026. Credit growth slowed from 8.2% in 2025 to 7.7% in 1Q26 and 7.4% in May, alongside weak domestic demand. FAI declined 4.1% YoY, while retail sales rose just 1.4% in 5M26. Exports remained a bright spot (+15.5% YoY in 5M26), but the uneven growth caps investor conviction on China equities. PPI turned positive in Mar-26, after 41 consecutive months of deflation, and rose to 3.9% by May, driving a strong industrial profit growth of 18.8% YoY in 5M26. However, sustainability is questionable given the lower energy prices. Expectations for near-term policy stimulus remain muted.

## Model portfolio: industrials/tech over utilities/consumers

For 3Q26, our quant-driven portfolio upgrades industrials (incl. heavy machinery and electrical equipment) and tech hardware to the Top-10 OW list. We stay positive on communications equipment, which was up 92% in 2Q. We also upgrade diversified financials for strong 2Q earnings, and remain constructive on metals & mining (ex-gold), chemicals, and life sciences sectors. On the other hand, our model downgrades IPPs & renewables and liquors to the Bottom-10 UW list, while remains cautious on the autos, gas & water utilities, real estate, biotech, and household durables sectors.

## 07 July 2026

Equity Strategy
China

BofA
Data Analytics

![](images/77e83dcfcec08cd0f40833320def2cace9e319be41b48ebb3541a230f127cd66.jpg)

## Table of Contents

<table><tr><td>Executive summary: the 3Ms</td><td>2</td></tr><tr><td>Market: inexpensive, but not compelling</td><td>3</td></tr><tr><td>China flow lens</td><td>7</td></tr><tr><td>Macro: export-led, uneven growth</td><td>10</td></tr><tr><td>Other key things investors are watching</td><td>13</td></tr><tr><td>Sector model portfolio</td><td>16</td></tr><tr><td>Appendix</td><td>18</td></tr><tr><td>China Investment Compass (中国投资罗盘)</td><td>18</td></tr><tr><td>Sector classification</td><td>20</td></tr><tr><td>Valuation comp table</td><td>24</td></tr></table>

## Winnie Wu >>

Research Analyst
BofA (Hong Kong)
+852 3508 3058
winnie.wu@bofa.com

Patrick Pan, CFA >>
Research Analyst
BofA (Hong Kong)
+852 3508 4601
patrick.pan2@bofa.com

Gina Wu >>
Strategist
BofA (Hong Kong)
+852 3508 8008
gina.wu@bofa.com

## Glossary

OW: overweight

UW: underweight

R.E.A.L.: Regulatory Critical – Enduring Cycles – Asset Heavy – Local Services

## Executive summary: the 3Ms

Market: MSCI China and H-share significantly underperformed A-share and global markets in 2Q. MSCI China's forward P/E at 10.3x currently is $12\%$ below the long-term average. EPS growth expectations have been reduced to $2 - 3\%$ YoY for 2026E.

Exhibit 1: MSCI China's P/E at 10.3x is $12\%$ below long-term average Forward P/E valuation of MSCI China Index  
![](images/60a2567cdc5d47b49a455c287585e25718f48906ba80d98cff6460792babfaba.jpg)  
Source: Bloomberg, MSCI  
BofA GLOBAL RESEARCH

Exhibit 2: Consensus EPS forecast was cut from >11% in Jan to <3%
Consensus forecast for MSCI China earnings growth  
![](images/c472fe75502ace95e7af485b4b9dfe2447d2e0388f1b7d6b797c78bfb81bf55c.jpg)  
Source: MSCI, FactSet  
BofA GLOBAL RESEARCH

Macro: Credit and nominal GDP growth softened in 5M26, along with weak FAI and consumption, although higher energy prices drove up PPI and industrial profits.

Exhibit 3: China's consumer confidence retreated in Mar-Apr 2026
China consumer confidence index (CCI)  
![](images/38cce390ac944d86435c4b4af9c39d4aacfbde1bed5cac7562d48bb3862abe68.jpg)  
Source: NBS

Exhibit 4: Industrial profit growth accelerated to 18.8% YoY in 5M26
Industrial profit growth (YTD) vs PPI inflation  
![](images/8a7b8ab88934f61ec11062c25a22d0f109bae00ddb32ea0257b8f3bd16dafc73.jpg)  
Source: NBS, CEIC  
BofA GLOBAL RESEARCH

BofA GLOBAL RESEARCH

Model portfolio: For 3Q26, we prefer industrials (heavy machinery, electrical equipment), tech (communications equipment, hardware), and materials. Underweight utilities (IPPs, gas & water), consumers (liquors, auto, durables) and biotech sectors.

Exhibit 5: We prefer brokers/industrials/tech sectors over consumer/utilities in 3Q26
China Investment Compass based model portfolio recommendation: 3Q26

<table><tr><td>#</td><td>Overweight Sectors</td><td>vs 2Q26</td><td>Underweight Sectors</td><td>vs 2Q26</td></tr><tr><td>1</td><td>FI- Diversified Financials</td><td>↑</td><td>UTL- Independent Power &amp; Renewable</td><td>↓</td></tr><tr><td>2</td><td>MAT- Metals &amp; Mining (ex. gold)</td><td>√</td><td>CS- Liquors</td><td>↓</td></tr><tr><td>3</td><td>MAT- Chemicals</td><td>√</td><td>CD- Auto</td><td>√</td></tr><tr><td>4</td><td>IND- Heavy Machinery</td><td>↑</td><td>COM- Telecom</td><td>√</td></tr><tr><td>5</td><td>IND- Electrical Equipment</td><td>↑</td><td>CD- Household Durables</td><td>√</td></tr><tr><td>6</td><td>IT- Communications Equipment</td><td>√</td><td>IND- Construction &amp; Engineering</td><td>↓</td></tr><tr><td>7</td><td>IND- Airline, Logistics &amp; Shipping</td><td>√</td><td>RE- Real Estate</td><td>√</td></tr><tr><td>8</td><td>IT- Technology Hardware</td><td>↑</td><td>HC- Biotechnology</td><td>√</td></tr><tr><td>9</td><td>COM- Interactive Entertainment</td><td>↑</td><td>UTL- Gas &amp; Water Utilities</td><td>√</td></tr><tr><td>10</td><td>HC- Life Sciences Tools &amp; Services</td><td>√</td><td>MAT- Construction Materials &amp; Paper</td><td>↓</td></tr></table>

Source: BofA Global Research \*V shows sectors on our OW/UW list last quarter; ↑ shows new upgrades, ↓ shows new downgrades  
BofA GLOBAL RESEARCH

## Market: inexpensive, but not compelling

## Market performance review

2Q26 was marked by AI-led market leadership, resulting in sharper divergence between tech and non-tech sectors and between A- and H-shares. While investors increasingly looked through geopolitical headlines, concerns over weak domestic demand and an export-reliant economy continued to cap conviction on China equities. In USD terms, KOSPI (+64.2%), ChiNext (+38.6%), and Nikkei 225 (+34.1%) outperformed in 2Q26, while HSCEI (-9.8%), HSI (-7.7%), and MSCI China (-7.6%) lagged. Within MSCI China, IT was the only sector with positive return in 2Q (+36.7%), while Consumer Discretionary (-20.7%), Consumer Staples (-18.6%) and Materials (-18.3%) were the worst performers. A/H-share divergence widened notably: CSI 300 +13.7% in 2Q, while HSCEI -9.8%. P/E valuation of MSCI China fell back to 10.3x, which is a 12% discount to its long-term average, but still above the historical trough of 8-9x.

Exhibit 6: KOSPI, ChiNext, and Nikkei 225 outperformed in 2Q26 while HSCEI, HSI and MSCI China lagged
Comparison of key global market performance  
![](images/4ced1b68520e78aaaad1a7f35dabcc63b3046aa2fc1724c5bb6d683de723a621.jpg)  
Source: Bloomberg, MSCI \*Net return excluding dividend  
BofA GLOBAL RESEARCH

Exhibit 7: IT significantly outperformed in 2Q26, while consumer discretionary, consumer staples and materials lagged
Comparison of MSCI China sector performance  
![](images/cb8c7065cdff7f0bc24d05e2983a8c85393be768b0a6bd6661262e034082654d.jpg)  
Source: Bloomberg, MSCI \*Net return excluding dividend  
BofA GLOBAL RESEARCH

All of the top 10 market cap gainers in 2Q26 came from the tech hardware and semis sectors, whereas the largest market cap losers spread across the energy, internet, consumer and materials sectors.

Exhibit 8: AI hardware and semis stocks were among the top market cap gainers
Top 10 market cap gainers in MSCI China (2Q26)  
![](images/c92a5bf7c3ec38c6fbc03b4aa7e0b7541d1aae9af372295bba6e27584e90bc3d.jpg)  
Source: Bloomberg, MSCI  
BofA GLOBAL RESEARCH

Exhibit 9: Energy, internet and consumer stocks were among the top market cap losers
Top 10 market cap losers in MSCI China (2Q26)  
![](images/53a82982055320d75e604771114b64674f5c8f13629595b99feef40674c98adb.jpg)  
Source: Bloomberg, MSCI  
BofA GLOBAL RESEARCH

AI investing became increasingly nuanced in 2Q26, as markets grappled with shifting narratives around memory supercycles, CPO deployment delays, domestic GPU substitution, and internet platforms' AI monetization. However, a series of brief but sharp sentiment resets from late May highlighted growing investor discomfort. Concentrated holdings, elevated volatility, retail leverage (including leveraged ETFs), and rising inflation and liquidity concerns contributed to increasingly jittery market sentiment. Global yield breakouts, a muted Trump-Xi summit, China's cross-border capital flow tightening, and renewed geopolitical uncertainty further triggered periodic de-risking. The narrow rally also widened the divergence between A-shares and H-shares. China's AI localization theme remained a key source of support for onshore equities, while the offshore Hong Kong market, with lower exposure to domestic semiconductor champions and higher weights in internet and financial stocks, was more vulnerable to earnings risks, macro headwinds, and domestic policy actions.

Policy actions in 2Q26 appeared more targeted, in contrast to the broad-based margin requirement tightening in January. In late May, regulators launched a two-year crackdown on illegal cross-border investment by mainland investors and penalized three online brokers. In addition, the State Council issued Order No. 837 on Outbound Investment, expanding oversight to resident individuals and embeds national security, export control, and cross-border compliance considerations into overseas investment activities. Meanwhile, Chinese tax authorities have stepped up scrutiny of overseas income and assets reported through CRS (Common Reporting Standard) information-sharing mechanisms, prompting investor concerns on outbound wealth flows and offshore asset holdings. These developments raised worries over Hong Kong's liquidity and its insurance, wealth management, and property sectors. Separately, regulatory overhang on large internet platforms resurfaced, as evidenced by SAMR-led actions targeting platform marketing practices during the "618" shopping festival, food delivery competition and safety standards, and online train-ticketing services.

Vibrant IPO market is bright spot amid tech boom, with A-share IPO fundraising +89% YoY to USD10bn in 1H26 and HK proceeds +91% YoY to USD27bn, the strongest first-half on record. Concerns of capital rotation away from existing holdings to fund new offerings, as well as selling pressure from upcoming lock-up expirations of recently listed names, increasingly weighed on near-term sentiment.

Macro activity data in Apr-May pointed to further weakness in domestic demand and investment, and economic growth became increasingly reliant on exports. Policy direction remained broadly consistent. The new overnight rate framework signals higher tolerance for lower rates, while fiscal spending YTD appeared more delayed and conditional. Apr Politburo meeting readout indicated no rush on stimulus and highlighted economic resilience, as market expected. The Lujiazui forum in Jun unveiled a narrower short-term rate corridor (50bp vs. 70bp previously) to improve short-term liquidity guidance, introduced a new “FIMA RMB Repo” to supply offshore yuan liquidity, and relaxed STAR listing criteria to accommodate pre-profit AI model companies.

Geopolitics remained an overhang across Asian markets, but its marginal influence diminished during 2Q26, particularly for A-shares. Investors looked through geopolitical shocks and focused on regions and sectors with stronger AI fundamentals, notably Korea and Taiwan, while China relatively underperformed.

On US-China relations, the Trump-Xi summit in May delivered modest economic agreements, although progress on core disputes remained limited. A positive takeaway was Trump's invitation for Xi to visit the White House in Sep-2026, providing a degree of near-term policy stability. China was also not singled out in the Section 301 findings released in early June; the 12.5% tariff was imposed alongside measures targeting multiple major trading partners over forced-labor concerns. That said, geopolitical and reputational risks continue to rise as new restrictions emerge. In June, the Pentagon updated its Section 1260H list of entities with alleged military ties, adding several major Chinese companies, including Alibaba, Baidu, BYD, CXMT, and Unitree.

Exhibit 10: 2Q26 was shaped by a narrow tech rally. Within China, Star 50, ChiNext, CSI500, and CSI 1000 outperformed NASDAQ Golden Dragon, HSCEI and HSI  
Performance comparison (net return in USD terms, as of Jun 30 $^{th}$ )

<table><tr><td rowspan="2"></td><td rowspan="2">Current level</td><td colspan="8">Performance (%)</td><td colspan="8">Ranking</td></tr><tr><td>1M</td><td>3M</td><td>6M</td><td>12M</td><td>YTD</td><td>3yr</td><td>5yr</td><td>10yr</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td><td>YTD</td><td>3yr</td><td>5yr</td><td>10yr</td></tr><tr><td colspan="18">Major indices</td></tr><tr><td>S&amp;P 500</td><td>7,499</td><td>-1.1</td><td>14.9</td><td>9.6</td><td>20.9</td><td>9.6</td><td>68.5</td><td>74.5</td><td>257.3</td><td>12</td><td>9</td><td>10</td><td>11</td><td>10</td><td>6</td><td>3</td><td>2</td></tr><tr><td>Dow Jones</td><td>52,319</td><td>2.5</td><td>12.9</td><td>8.9</td><td>18.7</td><td>8.9</td><td>52.1</td><td>51.6</td><td>191.8</td><td>7</td><td>11</td><td>11</td><td>12</td><td>11</td><td>9</td><td>5</td><td>4</td></tr><tr><td>NASDAQ</td><td>26,214</td><td>-2.8</td><td>21.4</td><td>12.8</td><td>28.7</td><td>12.8</td><td>90.1</td><td>80.7</td><td>441.3</td><td>13</td><td>5</td><td>8</td><td>9</td><td>8</td><td>4</td><td>2</td><td>1</td></tr><tr><td>Euro Stoxx 50</td><td>6,328</td><td>2.3</td><td>12.4</td><td>6.3</td><td>15.8</td><td>6.3</td><td>50.4</td><td>50.0</td><td>127.7</td><td>8</td><td>12</td><td>12</td><td>13</td><td>12</td><td>10</td><td>6</td><td>7</td></tr><tr><td>FTSE 100</td><td>10,497</td><td>-0.8</td><td>3.4</td><td>4.1</td><td>15.8</td><td>4.1</td><td>45.2</td><td>43.2</td><td>61.2</td><td>11</td><td>14</td><td>14</td><td>14</td><td>14</td><td>11</td><td>7</td><td>9</td></tr><tr><td>Nikkei 225</td><td>70,062</td><td>3.4</td><td>34.1</td><td>33.8</td><td>53.4</td><td>33.8</td><td>87.3</td><td>66.2</td><td>185.4</td><td>6</td><td>4</td><td>4</td><td>5</td><td>4</td><td>5</td><td>4</td><td>5</td></tr><tr><td>KOSPI</td><td>8,476</td><td>-2.9</td><td>64.2</td><td>87.1</td><td>141.2</td><td>87.1</td><td>181.3</td><td>87.8</td><td>220.0</td><td>14</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>3</td></tr><tr><td>Russell 2000</td><td>3,024</td><td>3.6</td><td>21.2</td><td>21.9</td><td>39.0</td><td>21.9</td><td>60.1</td><td>30.9</td><td>162.5</td><td>5</td><td>6</td><td>6</td><td>7</td><td>6</td><td>8</td><td>9</td><td>6</td></tr><tr><td>MSCI China</td><td>70</td><td>-7.6</td><td>-7.6</td><td>-15.9</td><td>-6.8</td><td>-15.9</td><td>16.1</td><td>-36.6</td><td>25.0</td><td>15</td><td>15</td><td>17</td><td>16</td><td>17</td><td>17</td><td>17</td><td>14</td></tr><tr><td>NASDAQ Golden Dragon</td><td>5,848</td><td>-11.2</td><td>-13.4</td><td>-22.3</td><td>-20.3</td><td>-22.3</td><td>-10.8</td><td>-60.7</td><td>-11.2</td><td>18</td><td>18</td><td>18</td><td>18</td><td>18</td><td>18</td><td>18</td><td>17</td></tr><tr><td>HSI</td><td>22,881</td><td>-9.2</td><td>-7.7</td><td>-11.4</td><td>-4.9</td><td>-11.4</td><td>20.9</td><td>-21.4</td><td>8.9</td><td>16</td><td>16</td><td>15</td><td>15</td><td>15</td><td>15</td><td>15</td><td>15</td></tr><tr><td>HSCEI</td><td>7,558</td><td>-10.4</td><td>-9.8</td><td>-15.8</td><td>-12.8</td><td>-15.8</td><td>17.5</td><td>-29.8</td><td>-14.2</td><td>17</td><td>17</td><td>16</td><td>17</td><td>16</td><td>16</td><td>16</td><td>18</td></tr><tr><td>SHCOMP</td><td>4,094</td><td>0.3</td><td>6.9</td><td>6.2</td><td>25.5</td><td>6.2</td><td>36.7</td><td>8.5</td><td>37.0</td><td>10</td><td>13</td><td>13</td><td>10</td><td>13</td><td>14</td><td>13</td><td>13</td></tr><tr><td>CSI300</td><td>4,979</td><td>1.5</td><td>13.7</td><td>10.7</td><td>33.5</td><td>10.7</td><td>38.5</td><td>-9.3</td><td>54.8</td><td>9</td><td>10</td><td>9</td><td>8</td><td>9</td><td>13</td><td>14</td><td>10</td></tr><tr><td>CSI500</td><td>9,031</td><td>7.7</td><td>20.5</td><td>24.6</td><td>61.1</td><td>24.6</td><td>60.9</td><td>26.2</td><td>44.6</td><td>2</td><td>7</td><td>5</td><td>4</td><td>5</td><td>7</td><td>10</td><td>12</td></tr><tr><td>CSI1000</td><td>8,810</td><td>4.4</td><td>17.5</td><td>19.4</td><td>46.3</td><td>19.4</td><td>42.6</td><td>18.3</td><td>-1.2</td><td>4</td><td>8</td><td>7</td><td>6</td><td>7</td><td>12</td><td>12</td><td>16</td></tr><tr><td>ChiNext</td><td>4,343</td><td>7.2</td><td>38.6</td><td>39.6</td><td>112.9</td><td>39.6</td><td>109.5</td><td>18.8</td><td>91.1</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>11</td><td>8</td></tr><tr><td>Star 50</td><td>2,208</td><td>25.7</td><td>78.6</td><td>69.1</td><td>132.2</td><td>69.1</td><td>13

[中间内容因长度限制已省略]

h information is distributed simultaneously to internal and client websites and other portals by BofA and is not publicly-available material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
