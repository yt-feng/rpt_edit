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
# Digital Banking

## AI Defensibility Underappreciated; QTWO Top-Pick, ALKT High-Conviction Take-Out Candidate, More Constructive on NCNO

![](images/aac8bfeac4d8d3eb228a7a232701b96d96842672c475b625627174781ad422a6.jpg)

We are rolling forward our valuation framework to Dec-27 across our banking technology/digital banking coverage and come away with a constructive view on the group, whereby AI-defensibility concerns appear overstated relative to the entrenched workflow, data, and compliance moats these vendors have built. Our highest-conviction ideas remain Q2 (QTWO) and Alkami (ALKT), both Overweight, which operate in a consolidated, duopolistic digital banking market with long contract durations, strong gross retention, and clear pathways to meaningful margin and FCF expansion—characteristics we believe should command premium multiples in a fundamentals-driven tape. ALKT screens as our high-conviction takeout candidate amid renewed activist pressure and supportive ownership dynamics, while QTWO offers the cleaner organic compounding story with a large underpenetrated TAM and conservative capital allocation. On nCino (NCNO), we maintain our Neutral rating given a less consolidated end market and a comparatively less crystallized AI narrative, but following this week's headquarters visit (see detailed notes here) we are incrementally more positive on the company's AI defensibility, and the valuation looks compelling.

\- In a fundamentals-driven tape, we think Q2 (QTWO) would be an outperformer. The company operates in a duopolistic competitive landscape, and has a large, underpenetrated TAM of \~250M digital banking accounts at regional/community banks and credit unions. Only \~20% are on modern platforms. The company benefits from long 5-7 year contracts and only \~400-500 annual renewals reinforcing strong revenue visibility. Management currently guides 12.5-13.0% subscription growth for FY27: we view management's guidance as the floor for growth in FY27 and the medium term. Management's soft guidance implies about over 1,000 bps of EBITDA margin expansion over the next five years (24% in FY25 to \~35% in FY30). The company has no debt, and is already achieving >90% FCF conversion. We expect capital to primarily be deployed towards share repurchases; transformational M&A is not off the table, but management maintains a conservative, value-orientated stature toward M&A. We view 15x EV/EBITDA for FY27 as an extremely fair price for a company with these characteristics. We establish our Dec-27 PT of \$60/sh (nearly 40% upside), versus \$80/sh for Dec-26E previously.

\- Alkami (ALKT) as a high-conviction takeout candidate. Alkami (ALKT) is our high-conviction takeout candidate, with activist investor Jana Partners reportedly pushing the company to restart a sale process (link here). Alkami stands out within software coverage due to its mission-critical positioning,

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price ($)</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>Q2 Holdings</td><td>QTWO US</td><td>2,630.80</td><td>43.77</td><td>OW</td><td>n/c</td><td>60.00</td><td>Dec-27</td><td>80.00</td><td>Dec-26</td></tr><tr><td>Alkami</td><td>ALKT US</td><td>1,672.79</td><td>15.09</td><td>OW</td><td>n/c</td><td>19.00</td><td>Dec-27</td><td>20.00</td><td>Dec-26</td></tr><tr><td>nCino</td><td>NCNO US</td><td>1,780.06</td><td>15.49</td><td>N</td><td>n/c</td><td>17.00</td><td>Dec-27</td><td>16.00</td><td>Dec-26</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 17 Jun 26.

See page 9 for analyst certification and important disclosures.

## Vertical SaaS & HealthTech

Ella Smith AC
(1-212) 622-2451
ella.smith@jpmchase.com

Alexei Gogolev

(1-212) 622-9391

alexei.gogolev@JPM.com

Destiny Jackson

(1-212) 622-4360

destiny.jackson@JPM.com

Isabella A Camaj
(1-212) 834-2379
bella.camaj@JPM.com
JPM Securities LLC

durable growth runway, and clear margin/FCF expansion pathway. We view Q2 as Alkami's one, formidable competitor. Alkami is more AI-defensible than the market assumes, as digital banking requires complex integrations, compliance readiness, and careful implementation that AI-native entrants cannot shortcut, reflected in gross retention consistently above 98% with churn primarily driven by customer M&A rather than competition. Private equity is viewed as the most likely acquirer since strategies like FIS, Fiserv, and Jack Henry have more legacy offerings and face ecosystem conflicts, while a sponsor could preserve processor neutrality and underwrite meaningful operating leverage (modeled at \~18% EBITDA margin and low-60s% FCF/EBITDA conversion in 2026E). Ownership dynamics further support a strategic path, with General Atlantic nearly doubling its stake to close to one-fifth of shares outstanding since July 2025. We view 17x 2027E EV/EBITDA as a reasonable multiple, given the company's growth profile and stickiness. We assign a +2x multiple premium to Alkami versus Q2, due to the company's higher takeout potential. We establish our Dec-27 PT of \$19/sh (about 30% upside), versus \$20/sh for Dec-26E previously.

\- Incrementally positive on AI defensibility on nCino (NCNO). Following the nCino headquarters visit in Wilmington, NC—where investors engaged directly with nCino's CEO, CFO, CTO, and co-founder—we come away more positive on nCino's AI defensibility, grounded in how deeply embedded the platform is within commercial banking workflows and reinforced by tangible AI traction in products like Banking Advisor, Digital Partners, and continuous credit monitoring. Co-founder Pullen Daniel's field perspective was particularly compelling: customers are largely indifferent to the underlying model so long as nCino owns the governance and regulatory burden, and the build-vs-buy calculus still favors nCino given that coding is only a fraction of the effort relative to design, testing, governance, and ongoing support. We maintain our Neutral rating—versus Overweight on QTWO and ALKT, which benefit from more consolidated end markets and clearer AI defensibility narratives—but nCino's valuation looks compelling at current levels, and the bundled intelligence-unit monetization model insulates customers from token-cost volatility while keeping conversations anchored on outcomes. Net-net, we are incrementally less concerned about AI-native disruption near term, as banks continue to find AI-native entrants short of enterprise readiness on historical data access and third-party risk management, leaving nCino's contextual data and embedded workflow moat intact. We establish our Dec-27 PT of \$17/sh, versus \$16/sh for Dec-26E previously.

# Investment Thesis, Valuation and Risks

Q2 Holdings (Overweight; Price Target: \$60.00)

## Investment Thesis

Of the innovators in the digital banking space, QTWO leads amongst large financial institutions. QTWO provides an end-to-end digital banking platform, supporting delivery of retail, SMB, and commercial functionalities. The platform is highly customizable, allowing customers to develop their own unique extensions of and integrations to their digital platform. QTWO has more than 1,200 financial institution customers, including more than 40% of the top 100 U.S. Banks and more than 40% of the top 100 U.S. Credit Unions, based on total assets.

## Valuation

YE27 \$60/sh PT implies a 15x EV/EBITDA multiple for 2027E. Our price target multiple is in line with where high-quality Vertical Software companies currently trade. We believe this is justified due to QTWO's large market opportunity, market leading position, strong and improving cash generation profile, as well as AI defensibility.

## Risks to Rating and Price Target

## Risks to Downside

Elongated sales cycles could lead to earnings risk. Consistent with vertical software, Q2 has long sales cycles that can span three to 24 months. Any further elongation from macro or industry pressure could lead to lower-than-expected revenue growth, which could impair stock performance.

Weakness in regional bank and credit union industry could lead to poorer sentiment. Q2's target customer base is the largest \~2,000 financial institutions in United States, excluding the ultra-large money centers (e.g., JPM Chase). Weakness in this space—or banking failures—could lead to negative sentiment or earnings risk for Q2.

# Investment Thesis, Valuation and Risks

Alkami (Overweight; Price Target: \$19.00)

Investment Thesis

Of the innovators in the digital banking space, Alkami leads amongst the credit unions, whereas QTWO's forte is the banking space. Like QTWO, Alkami provides an end-to-end digital banking platform, supporting delivery of retail, SMB, and commercial functionalities. There is an imperative for U.S. credit unions and regional banks to modernize. We think this is likely to continue for at least another decade, supporting the durability of Alkami's growth. The financial institutions are looking for an outsourcing partner that could help them enable onboarding and better engagement of new users and improve operational efficiency. Alkami is unique in that it is built on a cloud-native, multi-tenant architecture. Alkami built its platform on a single code base, and ensures a continuous delivery platform to provide significant speed to market and implementation for clients.

## Valuation

YE27 \$19/sh PT implies a 17x EV/EBITDA multiple for 2027E. Our price target multiple is at the higher-end of the range versus where Vertical Software companies currently trade. We believe this is justified due to ALKT's large market opportunity, solid organic growth profile, as well as AI defensibility. We assign a slight premium to ALKT versus QTWO due to higher take-out risk probability.

## Risks to Rating and Price Target

## Risks to Downside

Weakness in regional bank and credit union industries could lead to poorer stock sentiment. Alkami's target customer base is the largest \~2,000 financial institutions in United States, excluding the ultra-large money centers (e.g., JPM Chase). Weakness in this space—or banking failures—could lead to negative sentiment or earnings risk for Alkami.

Alkami is semi-acquisitive—failure to monetize and integrate these acquisitions could lead to share underperformance. Alkami recently acquired MANTL (2025), Segmint (2022), MK Decisioning Systems (2021), and ACH Alert (2020). Failure to invest in these businesses and drive cross-sell could lead to less-than-expected earnings potential for the company, causing shares to underperform.

Alkami's share price is sensitive to its forecast growth rates. Slower-than-expected growth is likely to have a negative impact on share performance.

# Investment Thesis, Valuation and Risks

nCino (Neutral; Price Target: \$17.00)

Investment Thesis

nCino uniquely benefits from industry experience in both banking and technology, having been spun out as a separate company from a bank in late 2011. Its aim was to help other financial institutions with the challenges plaguing the industry. These challenges include cumbersome legacy technology, fragmented data, disconnected business functions, and a disengaged workforce that makes it difficult to maintain relevancy to clients. The company is also built on a single-code base. We also note nCino has a high-quality roster of customers. The company touts 15 out of the top 30 banks in the US, five of the top seven in the U.K. and Ireland, and three of the top five in APAC.

## Valuation

YE27 \$17/sh PT implies a 9x EV/EBITDA multiple for CY 2027E (ending Dec-2027). Our price target multiple is at the lower-end of the range versus where Vertical Software companies currently trade, but ahead of companies we expect to be meaningfully disrupted by AI proliferation. We believe this is justified due to NCNO's less-attractive competitive positioning versus companies in the FinTech spaces, such as QTWO and ALKT. We also believe there are more clear beneficiaries of AI proliferation.

## Risks to Rating and Price Target

Risk to Upside: nCino is in the midst of a transformational change, which could be positive for earnings momentum and be supportive of share performance. The company is changing its pricing model, cutting R&D costs, reinvesting in S&M, and expecting subscription revenue to begin accelerating in a few quarters. Should it be successful implementing these strategies, the market could reward the shares, trading them higher.

Risk to Upside: nCino could rely more on third-party system integrations, versus performing these functions internally, which could lead to higher-than-expected earnings. nCino has reported negative services margins multiple times in the past 12 months. The company already has partnerships with best-in-class system integrators, such as Accenture, Deloitte, PwC, and West Monroe Partners. They are usually enlisted to implement and configure the nCino Platform for larger FI customers, whereas nCino has historically performed professional services for smaller FIs itself. Higher use of SIs across its customer base could lead to higher margins for nCino.

Risk to Downside: Certain nCino products are built on Salesforce – nCino's share price can be negatively affected by any compromise to its Salesforce partnership. Fundamental elements of the nCino Platform are built on the Salesforce platform, including nCino's client onboarding, loan origination, and deposit account opening solutions. The agreement runs through January 2031. Any termination of the relationship with Salesforce would result in a materially adverse impact on nCino's business.

Risk to Downside: nCino recently transitioned to a new CEO – internal and external leadership failures could lead to share underperformance. nCino’s founding CEO, Pierre Naude, recently resigned. Naude has been the CEO since the company’s founding and is moving to the Executive Chairman role. Sean Desmond succeeded the former CEO. It will be important to maintain the innovation and elements essential to the continued growth of the business under new leadership. Any failure to do so may have an adverse impact on the results of operations and financial condition.

Q2 Holdings: Summary of Financials

<table><tr><td>Income Statement - Annual</td><td>FY24A</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Revenue</td><td>696</td><td>795</td><td>882</td><td>973</td><td>-</td></tr><tr><td>COGS</td><td>(306)</td><td>(334)</td><td>(333)</td><td>(358)</td><td>-</td></tr><tr><td>Gross profit</td><td>354</td><td>430</td><td>523</td><td>615</td><td>-</td></tr><tr><td>SG&amp;A</td><td>(168)</td><td>(169)</td><td>(179)</td><td>(188)</td><td>-</td></tr><tr><td>Adj. EBITDA</td><td>142</td><td>187</td><td>242</td><td>287</td><td>-</td></tr><tr><td>D&amp;A</td><td>(69)</td><td>(53)</td><td>(45)</td><td>(49)</td><td>-</td></tr><tr><td>Adj. EBIT</td><td>95</td><td>154</td><td>214</td><td>257</td><td>-</td></tr><tr><td>Net Interest</td><td>11</td><td>15</td><td>10</td><td>10</td><td>-</td></tr><tr><td>Adj. PBT</td><td>107</td><td>170</td><td>224</td><td>267</td><td>-</td></tr><tr><td>Tax</td><td>(8)</td><td>(3)</td><td>5</td><td>13</td><td>-</td></tr><tr><td>Minority Interest</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Adj. Net Income</td><td>99</td><td>167</td><td>229</td><td>280</td><td>-</td></tr><tr><td>Reported EPS</td><td>1.65</td><td>2.45</td><td>3.44</td><td>4.39</td><td>-</td></tr><tr><td>Adj. EPS</td><td>1.65</td><td>2.45</td><td>3.44</td><td>4.39</td><td>-</td></tr><tr><td>DPS</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Payout ratio</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Shares outstanding</td><td>60</td><td>68</td><td>67</td><td>64</td><td>-</td></tr><tr><td>Balance Sheet &amp; Cash Flow Statement</td><td>FY24A</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Cash and cash equivalents</td><td>359</td><td>368</td><td>222</td><td>486</td><td>-</td></tr><tr><td>Accounts receivable</td><td>42</td><td>52</td><td>63</td><td>69</td><td>-</td></tr><tr><td>Inventories</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current assets</td><td>110</td><td>122</td><td>145</td><td>152</td><td>-</td></tr><tr><td>Current assets</td><td>559</td><td>556</td><td>406</td><td>677</td><td>-</td></tr><tr><td>PP&amp;E</td><td>30</td><td>27</td><td>26</td><td>26</td><td>-</td></tr><tr><td>LT investments</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other non current assets</td><td>657</td><td>658</td><td>533</td><td>834</td><td>-</td></tr><tr><td>Total assets</td><td>1,853</td><td>1,832</td><td>1,570</td><td>2,167</td><td>-</td></tr><tr><td>Short term borrowings</td><td>190</td><td>303</td><td>4</td><td>4</td><td>-</td></tr><tr><td>Payables</td><td>9</td><td>77</td><td>76</td><td>65</td><td>-</td></tr><tr><td>Other short term liabilities</td><td>199</td><td>164</td><td>225</td><td>289</td><td>-</td></tr><tr><td>Current liabilities</td><td>399</td><td>544</td><td>305</td><td>357</td><td>-</td></tr><tr><td>Long-term debt</td><td>302</td><td>0</td><td>0</td><td>0</td><td>-</td></tr><tr><td>Other long term liabilities</td><td>475</td><td>614</td><td>377</td><td>429</td><td>-</td></tr><tr><td>Total liabilities</td><td>1,176</td><td>1,159</td><td>681</td><td>786</td><td>-</td></tr><tr><td>Shareholders&#x27; equity</td><td>678</td><td>674</td><td>889</td><td>1,380</td><td>-</td></tr><tr><td>Minority interests</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total liabilities &amp; equity</td><td>1,853</td><td>1,832</td><td>1,570</td><td>2,167</td><td>-</td></tr><tr><td>BVPS</td><td>11.27</td><td>10.84</td><td>14.31</td><td>22.49</td><td>-</td></tr><tr><td>y/y Growth</td><td>(4.0%)</td><td>(3.8%)</td><td>32.0%</td><td>57.1%</td><td>-</td></tr><tr><td>Net debt/(cash)</td><td>134</td><td>(64)</td><td>(218)</td><td>(482)</td><td>-</td></tr><tr><td>Cash flow from operating activities</td><td>136</td><td>201</td><td>272</td><td>319</td><td>-</td></tr><tr><td>o/w Depreciation &amp; amortization</td><td>69</td><td>53</td><td>45</td><td>49</td><td>-</td></tr><tr><td>o/w Changes in working capital</td><td>16</td><td>(24)</td><td>29</td><td>46</td><td>-</td></tr><tr><td>Cash flow from investing activities</td><td>(21)</td><td>(4)</td><td>(21)</td><td>(54)</td><td>-</td></tr><tr><td>o/

[中间内容因长度限制已省略]

 information in this material has been obtained from sources believed to be reliable. While all reasonable care has been taken to ensure that the facts stated in this material are accurate and that the forecasts, opinions and expectations contained herein are fair and reasonable, JPM Chase & Co. or its affiliates and/or subsidiaries (collectively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is
"""
