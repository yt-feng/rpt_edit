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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# Flows & Liquidity

The need for AI rotation

\- The strong and almost steady outperformance since last September of semiconductor stocks (i.e. AI chip and memory makers) vs. hyperscalers (i.e. AI cloud providers) appears somewhat unsustainable in the long run.

\- One way this gap in performance could close is that as hyperscalers and AI model providers as well as users see improvements in monetization, revenues and earnings and they start to catch up, capturing a bigger share of the overall AI value added pie (the positive scenario).

\- Another way it could close is that if semiconductor outperformance comes at the expense of customers like hyperscalers, AI model providers or end-users, this could start to depress capex intentions of hyperscalers and model providers and eventually act as a headwind to demand for the semiconductor companies' products (the negative scenario).

\- Our house view is for a more positive scenario, while the consensus of bottom-up analysts points to a sharp deceleration in hyperscalers' capex growth from next year onwards which taken at face value would tilt towards the negative scenario.

\- US money creation on track to step up from \$1.6tr in 2025 to \$1.8tr in 2026.

\- MicroStrategy introduced avoidable two-way risk into crypto markets inducing more uncertainty and volatility.

## Cross Asset Fund Flow Monitor

Current level shows the latest percentile of weekly flows; Min is denoted by 0 and Max by 1. As of 24 $^{th}$ June 26.

<table><tr><td>MF &amp; ETF Flows</td><td>Min</td><td>Max</td><td>4 wk avg ($bn)</td><td>2025 avg ($bn)</td></tr><tr><td>All Equities</td><td></td><td></td><td>34.0</td><td>8.1</td></tr><tr><td>All Bonds</td><td></td><td></td><td>14.9</td><td>11.3</td></tr><tr><td>US Equities</td><td></td><td></td><td>29.4</td><td>3.5</td></tr><tr><td>US Bonds</td><td></td><td></td><td>8.2</td><td>4.3</td></tr><tr><td>Non-US Equities</td><td></td><td></td><td>4.6</td><td>4.6</td></tr><tr><td>Non-US Bonds</td><td></td><td></td><td>6.7</td><td>7.0</td></tr><tr><td>US HG Bonds</td><td></td><td></td><td>2.5</td><td>3.4</td></tr><tr><td>US HY Bonds</td><td></td><td></td><td>0.8</td><td>0.4</td></tr><tr><td>US Lev. Loans *</td><td></td><td></td><td>0.6</td><td>0.0</td></tr><tr><td>US MMFs</td><td></td><td></td><td>0.1</td><td>4.0</td></tr><tr><td>EM Equities</td><td></td><td></td><td>-1.9</td><td>0.9</td></tr><tr><td>EM Bonds</td><td></td><td></td><td>0.60</td><td>0.50</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>-0.1</td><td>-0.1</td></tr><tr><td>China Equities</td><td></td><td></td><td>-1.08</td><td>-0.15</td></tr><tr><td colspan="5">Europe</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>-1.7</td><td>0.9</td></tr><tr><td>Europe Bonds</td><td></td><td></td><td>4.6</td><td>4.3</td></tr><tr><td>Europe HG Bonds</td><td></td><td></td><td>0.3</td><td>0.9</td></tr><tr><td>Europe HY Bonds</td><td></td><td></td><td>0.28</td><td>0.17</td></tr><tr><td>Europe MMFs</td><td></td><td></td><td>5.0</td><td>3.8</td></tr><tr><td>Other Equities</td><td></td><td></td><td>8.55</td><td>3.00</td></tr></table>

Source: Lipper, ICI, Bloomberg Finance L.P. and JPM Flows & Liquidity.  
\* US LL historical flows are monthly averages converted to weekly for comparison. China onshore A-share ETFs have been excluded.

## See page 27 for analyst certification and important disclosures.

## Global Markets Strategy

Nikolaos Panigirtzoglou AC (44-20) 7134-7815 nikolaos.panigirtzoglou@JPM.com JPM Securities plc

Mika Inkinen
(44-20) 7742 6565
mika.j.inkinen@JPM.com
JPM Securities plc

Mayur Yeole
(91 22) 6157 3872
mayur.yeole@jpmchase.com
JPM India Private Limited

(91-22) 6157-5016
krutik.mehta@jpmchase.com
JPM India Private Limited

Cross Asset Positioning Monitor Current level shows the latest percentile, Min is denoted by 0 and Max by 1.

<table><tr><td>As of 30-Jun-26</td><td>MIN</td><td>MAX</td><td>Current percentile</td></tr><tr><td>Equities</td><td></td><td></td><td>0.72</td></tr><tr><td>Govt Bonds</td><td></td><td></td><td>0.73</td></tr><tr><td>Credit</td><td></td><td></td><td>0.29</td></tr><tr><td>Dollar</td><td></td><td></td><td>0.81</td></tr><tr><td>Commodities ex Gold</td><td></td><td></td><td>0.32</td></tr><tr><td>Gold</td><td></td><td></td><td>0.40</td></tr><tr><td>Bitcoin</td><td></td><td></td><td>0.51</td></tr><tr><td>EM Equities</td><td></td><td></td><td>0.66</td></tr><tr><td>EM Bonds/FX</td><td></td><td></td><td>0.20</td></tr><tr><td>Japan Equities</td><td></td><td></td><td>0.81</td></tr><tr><td>Europe Equities</td><td></td><td></td><td>0.90</td></tr><tr><td colspan="4">US Equity Sectors:</td></tr><tr><td>Energy</td><td></td><td></td><td>0.61</td></tr><tr><td>Materials</td><td></td><td></td><td>0.54</td></tr><tr><td>Industrials</td><td></td><td></td><td>0.65</td></tr><tr><td>Discretionary</td><td></td><td></td><td>0.54</td></tr><tr><td>Staples</td><td></td><td></td><td>0.15</td></tr><tr><td>Health Care</td><td></td><td></td><td>0.51</td></tr><tr><td>Financials</td><td></td><td></td><td>0.15</td></tr><tr><td>Technology</td><td></td><td></td><td>0.69</td></tr><tr><td>Communication Services</td><td></td><td></td><td>0.28</td></tr><tr><td>Utilities</td><td></td><td></td><td>0.44</td></tr></table>

Cross Asset Positioning Monitor aggregates across the various position indicators of Appendix ranging from positioning proxies across various futures contracts, momentum signals as proxies of how trend-following funds/CTAs are positioned, mutual fund betas as proxies of how mutual fund managers are positioned, risk parity fund positioning and leverage proxies, hedge fund betas as proxies of how hedge fund managers are positioned, client surveys, asset allocation estimates of private non-bank investors at global level, short interest indicators, etc.

\- The strong and almost steady outperformance since last September of semiconductor stocks (AI chip and memory makers) vs. hyperscalers (i.e. AI cloud providers) has been striking, raising concerns about the sustainability of this performance gap. A major trigger for this outperformance has been the spectacular revision in the 2026 capex plans by hyperscalers which as shown in Figure 2 and Figure 3 are tracking a record 100% yoy pace this year. Given the semiconductor trade is effectively part of the broader AI trade, this divergence appears somewhat unsustainable in the long run.

Figure 1: US listed Hyperscalers vs Semiconductors relative performance  
![](images/f6e4338bc06126fb8021e955413e2077722093f941b81264c29d718858ce4468.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 2: US hyperscalers capex projections by the consensus of bottom-up analysts as reported by Bloomberg

<table><tr><td>In $bn</td><td>23</td><td>24</td><td>25</td><td>26E</td><td>27E</td><td>28E</td><td>29E</td><td>30E</td></tr><tr><td>Google</td><td>32.3</td><td>52.5</td><td>91.4</td><td>186.5</td><td>242.4</td><td>256.6</td><td>260.5</td><td>264.5</td></tr><tr><td>Amazon</td><td>52.7</td><td>83.0</td><td>131.8</td><td>199.3</td><td>230.0</td><td>235.1</td><td>233.0</td><td>236.1</td></tr><tr><td>Meta</td><td>27.3</td><td>37.3</td><td>69.7</td><td>134.5</td><td>161.7</td><td>177.9</td><td>180.9</td><td>188.2</td></tr><tr><td>Microsoft</td><td>28.1</td><td>44.5</td><td>64.6</td><td>159.5</td><td>190.7</td><td>215.5</td><td>246.0</td><td>253.8</td></tr><tr><td>Oracle</td><td>8.7</td><td>6.9</td><td>21.2</td><td>78.3</td><td>100.3</td><td>101.1</td><td>88.2</td><td>72.6</td></tr><tr><td>Total</td><td>149.0</td><td>224.1</td><td>378.7</td><td>758.1</td><td>925.0</td><td>986.3</td><td>1,008.6</td><td>1,015.3</td></tr><tr><td>Y/Y growth</td><td>-4%</td><td>50%</td><td>69%</td><td>100%</td><td>22%</td><td>7%</td><td>2%</td><td>1%</td></tr></table>

Source: Bloomberg Finance L.P., JPM Flows & Liquidity.  
Figure 3: US hyperscalers capex yoy growth implied by consensus forecasts  
Based on projections by the consensus of bottom-up analysts, as reported by Bloomberg.

![](images/9e8bf3dc3a2296b3719794ad41474b015a8edb858f5e723fedbe0b24d6225c46.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- One way this gap in performance could close is that as hyperscalers and AI model providers as well as users see improvements in monetization, revenues and earnings and they start to catch up, capturing a bigger share of the overall AI value added pie (the positive scenario).

\- Another way it could close is that if semiconductor outperformance comes at the expense of customers like hyperscalers, AI model providers or end-users, this could start to depress capex intentions of hyperscalers and model providers and eventually act as a headwind to demand for the semiconductor companies' products (the negative scenario).

\- In our mid-year outlook (Global Equity Strategy 2026 Mid-Year Outlook, Jun 24th), we have outlined our house view, which is tilted towards the more positive scenario. At the same time, in our recent client conversations concerns over the negative scenario have been featuring prominently given that the rally has given investors overall higher exposure to the semiconductor trade (Figure 4). The concern is that the market pressure that hyperscalers are currently facing on both their equity and debt, could induce them to trim their capex plans from 2027 onwards. Indeed, despite strong earnings growth hyperscalers stock prices have been flattish over the past year, implying derating and an increase in their cost of equity (Figure 5). And their credit spreads have opened a gap vs those of semiconductor companies, again implying a higher cost of debt (Figure 6). Moreover, clients are noticing the sharp deceleration in hyperscalers capex trajectory from 2027 onwards as implied by the consensus of analysts' projections (Figure 2 and Figure 3). Although JPM analysts are projecting stronger capex growth for 2027 (\$1,150bn, see “AI Capex 2.0, Jun 17th”) than the consensus (\$925bn), the fear is that if the sharp deceleration

Figure 6: US JULI HG index, overall tech sector vs. computer hardware subsector
Credit spreads in bps over USTs.

in hyperscalers' capex trajectory from 2027 onwards implied by the consensus of analysts' projections proves right, the semiconductor trade could come under severe pressure inducing a more significant and sustained correction in the AI trade in both equity and debt markets.

Figure 4: Ratio of market capitalization to sales shares of the MSCI ACWI Semiconductor sector in the MSCI ACWI  
![](images/209236582d9e01034c8a9606d672e324705e7da009680264c2902c5d5718e657.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 5: Hyperscalers stock price  
UBS equally weighted US listed Hyperscalers stock index.  
![](images/f0c0a8558ac942c1bc21a9bc7360e700d0d5caa3e50b2fbee72b7932aa45696d.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

![](images/1fba70fee513d7f5d69476449d3622ed15729ee534376c9986d2a11b0f78bdc6.jpg)  
Source: Bloomberg Finance L.P., JPM Flows & Liquidity.

\- What evidence can we find from market metrics such as short interest ratios of hyperscalers, tech ex semiconductors, AI adoption beneficiaries or AI vulnerable companies?

\- The short interest ratios for these groups are shown in Figure 7 to Figure 10 below. For hyperscalers (Figure 7), there has been a rising trend since last October with a further steep increase in May/June, consistent with rising investor concern. For semiconductors ex. memory (Figure 8), short interest ratios have been rising more recently during May/June, but they are not higher to levels a year ago. For AI adoption beneficiaries, Figure 9 shows the short interest ratio of the JPM AI adoption beneficiaries basket (JPAIADPT Index), which remains rather contained since early April and stands at below its level at the start of the year. And Figure 10 shows the short interest ratios of companies in the JPM AI vulnerable basket (JPAIVUL Index), which has been rising steadily since the start of 2025 and in terms of levels stands significantly above the levels of the other three groups. In other words, while there are some signs that the semiconductor trade, in particular among memory makers, has resulted in added concerns among hyperscalers and other semiconductor stocks expressed via the rise in their short interest ratios over the past two months, AI adoption beneficiaries show little evidence of a similar rise while markets have continued to express concerns over AI vulnerable companies.

Figure 7: Hyperscalers short interest  
Short Interest as a \% share of shares outstanding.  
![](images/75ae28d0211e2eacf0b52028d9d10f434d56bfc5bbf67999af6a34b3da33321e.jpg)  
Source: S3, JPM Flows & Liquidity.

Figure 8: Semiconductors ex Memory short interest
Short Interest as a % share of shares outstanding.  
![](images/ee3ead7cb003f5c7d095722fca646029803a7f4a25d776ab9663e559fbb21082.jpg)  
Source: S3, JPM Flows & Liquidity.

Figure 9: JPM AI beneficiaries basket (JPAIADPT Index) short interest
Short Interest as a % share of shares outstanding.  
![](images/689d8e547cc955089fd679ed89d38241db4ebe8a8da784c123fc5df8cee48838.jpg)  
Source: S3, JPM Flows & Liquidity.

Figure 10: JPM AI vulnerable basket (JPAIVUL Index) short interest
Short Interest as a % share of shares outstanding.  
![](images/19a874799b65ad2aa5ec1bdd3eabca3d3a03f192a4c84b853b07de38f6f272e1.jpg)  
Source: S3, JPM Flows & Liquidity.

\- Going forward, the price for AI compute would be key for the ability of hyperscalers to monetize their AI capital spending. The higher the price for compute, the higher the ability of the hyperscalers to maintain or increase their profit margins. After some persistent downward pressure on compute pricing into end-2025, there have been some signs of improvement in April/May which was encouraging (Figure 11), though it appears to have subsided somewhat in June. And for AI model providers, LLM token prices had been rising from late Feb to end-May before subsiding somewhat in June (Figure 12). Monitoring these AI compute prices would be key going forward.

\- Finally, our colleague Jason Hunter also noted this growing divergence between hyperscalers and semiconductors, and that if the wedge does not start to close it could create a sentiment issue for the market from a technical perspective (Equity Technical Update, July 1st).

Figure 11: Compute Desk's Hopper US Index  
Aggregates listed on-demand and reserved prices for renting NVIDIA Hopper (H100 and H200) GPUs from US neocloud providers. The Index is priced in US dollars per GPU per hour.  
![](images/bffa7f7c3aec9641d6a3887fdf528a436d01f7ddae37edae71832c4dac699676.jpg)  
Source: Bloomberg Finance L.P., Compute Desk.

Figure 12: LLM Token Expenditure index \$ per million tokens.  
![](images/ccdeea6fe0f013a6c83d3d4d70e9b41815e1be24d406bc24429a195c4f8a4d76.jpg)  
Source: Bloomberg Finance L.P., Silicon Data.

## US money creation on track to step up from \$1.6tr in 2025 to \$1.8tr in 2026

\- We mentioned previously that US liquidity or the stock of US M2 money supply, which we proxy by the sum of US commercial bank deposits and the AUM of US Money Market Funds, increased at a strong pace of \$1.2tr in 2024 after expanding by \$1tr from May 2023 to end-2023. This had brought the cumulative increase in US money supply from May 2023 to end-2024 to \$2.2tr or 9.6%.

\- This pace of US money creation has increased further since 2025 with \$1.6tr expansion during 2025 and an even stronger \$1.8tr annualized pace YTD (Figure 13 and Figure 14). The stronger pace of US money creation since 2025 has been mostly a reflection of US banks willingness to expand their balance sheets (by making more loans and by accumulating more bonds) at a faster pace than in previous years, perhaps due to deregulation (Figure 15). US money creation has been further supported this year by the Fed's decision to stop contracting and instead to modestly expand its balance sheet (Figure 16).

Figure 13: Stock of US M2 money supply proxied by the sum of the stock of US commercial bank deposits and the AUM of US MMFs In \$tr.  
![](images/e924a4f2ab5aa7cff4423b51b5070218f76c1337a08f23fb3993346723f3122a.jpg)  
Source: Crane Data, Bloomberg Finance L.P., JPM Flows & Liquidity.

Figure 15: US commercial banks total assets In \$bn.  
Figure 14: US money creation by year annual change in the stock of US M2 money supply proxied by the sum of the stock of US commercial bank deposits and the AUM of US MMFs  
![](images/34d73702b7374184b8d224651c63ace67142b52ad50b0186c24e9e5a5faa2a0a.jpg)  
Source: Crane Data, Bloomberg Finance L.P., JPM Flows & Liquidity.

![](images/19ea89b6b7022bd428fddb3de16f91535ffe7ea95be4b138e7d030ce037c67e9.jpg)  
Source: Federal Reserve, JPM Flows & Liquidity.

Figure 16: Federal Reserve total assets  
![](images/9de2e5df03dc879418d9f01e88a2169d112a597319b2e4a55db7272c3987430d.jpg)  
Source: Federal Reserve, JPM Flows & Liquidity.

\- And similar to previous years, this stronger than nominal GDP money creation should provide a source of support to US financial assets, especially US equities, even as cash allocations overall look rather low (Figure 17), As we explained previously in our publication, these low

cash allocations would not necessarily prevent US liquidity creation from propagating US financial assets further from here, but they rather pose a vulnerability for financial assets if a significant negative shock in the future induces economic agents to start rebuilding their low cash allocations as they did in March 2020 with the pandemic or in 2022 with the Ukraine war/ global inflation shock or in March 2025 with tariffs/Liberation Day or in March 2026 with the Iran conflict.

Figure 17: Implied cash allocation by non-bank investors globally
Global cash held by non-bank investors as % total holdings of equities/bonds/M2 by non-bank investors/Commodities including gold held by private investors. Dotted lines are averages.  
![](images/a9210ec117a6e10f9ceb7061b30cd6a682aa31a46c9df621b380358d5317d86b.jpg)  
Source: Bloomberg Finance L.P., LSEG DataStream, JPM Flows & Liquidity.

## MicroStrategy introduced avoidable two-way risk into crypto markets inducing more uncertainty and volatility

\- This week

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 01 Jul 2026 08:35 PM BST

Disseminated 01 Jul 2026 08:35 PM BST
"""
