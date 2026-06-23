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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 21, 2026 10:00 PM GMT

Asia | Asia Pacific

## Three Actionable Ideas

Murata Manufacturing – OW | Sumitomo Mitsui FG – OW | Doosan Enerbility – OW

OW – Murata Manufacturing (6981.T): We expect a 3-year demand CAGR for high value-added MLCCs in AI and data center applications of \~100%. We think Murata Mfg will benefit the most from increased demand and product mix improvement. Our new Top Pick.

OW – Sumitomo Mitsui FG (8316.T): Expectations for bank earnings continue to improve, supported by rising terminal rate expectations and resilient corporate earnings. Potential earnings upgrades and stronger shareholder returns should serve as catalysts.

OW – Doosan Enerbility (034020.KS): The recent pullback looks more like a catalyst vacuum than a thesis break. With a more visible 2H26 watchlist across nuclear and SMR, we think the stock is worth revisiting. Reiterate OW.

## Links to reports:

Electronic Components: Murata Mfg Now Our Top Pick, Lowering Taiyo Yuden to UW (16 Jun 2026)

Banks: Continue to Favor Bank Stocks in Positive Cycle for Earnings and Returns (16 Jun 2026)

Doosan Enerbility: Re-entering the Catalyst Window (16 Jun 2026)

Exhibit 1: Performance summary

<table><tr><td>As of June 16</td><td>Absolute</td><td>Relative*</td></tr><tr><td>No. of ideas</td><td colspan="2">1509</td></tr><tr><td>Cumulative Outperformance (bps)</td><td colspan="2">8,955</td></tr><tr><td>Avg holding period total return</td><td>4.3%</td><td>2.0%</td></tr><tr><td>Avg 12M total return**</td><td>16.5%</td><td>11.5%</td></tr><tr><td>No. of positive returns</td><td>814</td><td>751</td></tr><tr><td>Hit ratio</td><td>54%</td><td>50%</td></tr></table>

Source: MS, DataStream Refinitiv, Bloomberg. Performance data as at Jun 16, 2026. Cumulative outperformance: against local benchmarks. Holding period total return measures performance when idea was effective. \*\*Avg. 12M total return measures performance of all ideas (closed and active) from Jun 16, 2025, to Jun 16, 2026, and does not adjust for buy/sell direction. \* Relative performance = idea outperformance against local benchmarks. Hit ratio = number of ideas with positive returns as percentage of the total number of ideas. Performance calculation does not consider transaction costs or other costs. Figures are not audited. Past performance is not a guarantee of future results.

MS ASIA LIMITED+

Samuel Lee, CFA  
Equity Strategist  
Samuel.Sw.Lee@morganstanley.com

Hozefa Topiwalla  
Equity Strategist  
Hozefa.Topiwalla@morganstanley.com

+852 2239-1862

+852 2848-6595

![](images/f744ff260b884c4b20f2f682eb45e208b058b9af8cb547182a4f668a68c8ab45.jpg)

![](images/ee08ea40d473a487612483404127069951f404437629268cd057a44837ab9531.jpg)

Latest closing prices as of June 19, 2026: Murata Manufacturing (6981.T): ¥11,750; Sumitomo Mitsui FG (8316.T): ¥6,482; Doosan Enerbility (034020.KS): W97,900.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Three Actionable Ideas

Exhibit 2: Cumulative outperformance

![](images/e876fa44b68dfbffee72ffd5674b49019d02914e837e6d9bb3d9ac623048d60d.jpg)  
Source: MS, Datastream, Refinitiv, Bloomberg. The performance calculation does not consider transaction costs or other costs. These figures are not audited. Past performance is not a guarantee of future results.

Exhibit 3: Weekly hit ratio  
![](images/84e7fe516de7aef9408c0ae09fc2d9cfb67f4e185dcdd2777ff8c8de5f018129.jpg)  
Source: MS, Datastream, Refinitiv, Bloomberg. The performance calculation does not consider transaction costs or other costs. These figures are not audited. Past performance is not a guarantee of future results. The hit ratio as of any particular Tuesday does not account for ideas started on the same day for which holding period was 0 days.

Three Actionable Ideas are not and should not be considered a portfolio: Each investment idea is chosen based on its own merit and without any consideration of the other investment ideas chosen. Specifically, there has been no effort to mitigate the risks of investing in any collective group of "Three Actionable Ideas". Concepts important to a balanced portfolio, such as negative correlation and diversification, have not been considered. Treating "Three Actionable Ideas" ideas as a portfolio will subject you to the risk of losing all or a substantial portion of your investments.

The information contained herein has been prepared solely for informational purposes and is not a solicitation of any offer to buy or sell any security or other financial instrument or to participate in any trading strategy. Products and trades of this type may not be appropriate for every investor. Please consult with your legal and tax advisors before making any investment decision. Please contact your MS sales representative for more details.

Exhibit 4: Three Actionable Ideas – Still in effect

<table><tr><td>No.</td><td>Ticker</td><td>Direction</td><td>Stock Rating*</td><td>Start</td><td>End</td><td>Idea</td><td>Last px**</td><td>Benchmark Index</td><td>Abs perf</td><td>Rel perf</td></tr><tr><td>1</td><td>4958.TW</td><td>Buy</td><td>OW</td><td>16-Jun-26</td><td>15-Sep-26</td><td>Zhen Ding</td><td>624</td><td>Taiwan Se Weighed Taiex</td><td>0.0%</td><td>0.0%</td></tr><tr><td>2</td><td>2344.TW</td><td>Buy</td><td>OW</td><td>16-Jun-26</td><td>15-Sep-26</td><td>Winbond Electronics Corp</td><td>197</td><td>Taiwan Se Weighed Taiex</td><td>0.0%</td><td>0.0%</td></tr><tr><td>3</td><td>ONGC.NS</td><td>Buy</td><td>OW</td><td>16-Jun-26</td><td>15-Sep-26</td><td>Oil &amp; Natural Gas Corp.</td><td>248.2</td><td>Bse Sensex</td><td>0.0%</td><td>0.0%</td></tr><tr><td>4</td><td>5801.T</td><td>Buy</td><td>OW</td><td>9-Jun-26</td><td>8-Sep-26</td><td>Furukawa Electric</td><td>46130</td><td>Topix</td><td>-0.8%</td><td>-3.2%</td></tr><tr><td>5</td><td>WBC.AX</td><td>Sell</td><td>UW</td><td>9-Jun-26</td><td>8-Sep-26</td><td>Westpac Banking</td><td>35.75</td><td>S&amp;P/Asx All Australian 200</td><td>-3.1%</td><td>0.6%</td></tr><tr><td>6</td><td>HPCL.NS</td><td>Buy</td><td>OW</td><td>9-Jun-26</td><td>8-Sep-26</td><td>Hindustan Petroleum</td><td>401.8</td><td>Bse Sensex</td><td>5.2%</td><td>1.3%</td></tr><tr><td>7</td><td>3563.T</td><td>Buy</td><td>OW</td><td>2-Jun-26</td><td>1-Sep-26</td><td>FOOD &amp; LIFE COMPANIES</td><td>10150</td><td>Topix</td><td>-3.1%</td><td>-4.8%</td></tr><tr><td>8</td><td>002371.SZ</td><td>Buy</td><td>OW</td><td>2-Jun-26</td><td>1-Sep-26</td><td>NAURA Technology Group Co Ltd</td><td>672.19</td><td>Shanghai Se Composite</td><td>11.5%</td><td>10.9%</td></tr><tr><td>9</td><td>5274.TWO</td><td>Buy</td><td>OW</td><td>2-Jun-26</td><td>1-Sep-26</td><td>Aspeed Technology</td><td>18155</td><td>Taiwan Se Weighed Taiex</td><td>0.3%</td><td>-0.4%</td></tr><tr><td>10</td><td>TITN.NS</td><td>Buy</td><td>OW</td><td>26-May-26</td><td>25-Aug-26</td><td>Titan Company Ltd</td><td>4338</td><td>Bse Sensex</td><td>5.7%</td><td>4.5%</td></tr><tr><td>11</td><td>285A.T</td><td>Buy</td><td>OW</td><td>26-May-26</td><td>25-Aug-26</td><td>KIOXIA Holdings</td><td>94720</td><td>Topix</td><td>51.6%</td><td>50.2%</td></tr><tr><td>12</td><td>3908.HK</td><td>Buy</td><td>OW</td><td>26-May-26</td><td>25-Aug-26</td><td>China International Capital Corp. Ltd.</td><td>21.12</td><td>Hang Seng China Enterprises</td><td>2.3%</td><td>5.7%</td></tr><tr><td>13</td><td>BHP.AX</td><td>Buy</td><td>OW</td><td>19-May-26</td><td>18-Aug-26</td><td>BHP Group Ltd</td><td>65.19</td><td>S&amp;P/Asx All Australian 200</td><td>11.2%</td><td>7.6%</td></tr><tr><td>14</td><td>JARD.SI</td><td>Buy</td><td>OW</td><td>19-May-26</td><td>18-Aug-26</td><td>Jardine Matheson Holdings Limited</td><td>63.55</td><td>Hang Seng</td><td>-11.4%</td><td>-7.1%</td></tr><tr><td>15</td><td>3017.TW</td><td>Buy</td><td>OW</td><td>19-May-26</td><td>18-Aug-26</td><td>Asia Vital Components Co. Ltd.</td><td>2370</td><td>Taiwan Se Weighed Taiex</td><td>-0.8%</td><td>-15.1%</td></tr><tr><td>16</td><td>7011.T</td><td>Buy</td><td>OW</td><td>12-May-26</td><td>11-Aug-26</td><td>Mitsubishi Heavy Industries</td><td>3810</td><td>Topix</td><td>-11.4%</td><td>-14.5%</td></tr><tr><td>17</td><td>402340.KS</td><td>Buy</td><td>OW</td><td>12-May-26</td><td>11-Aug-26</td><td>SK Square Co Ltd.</td><td>1501000</td><td>Korea Se Composite (Kospi)</td><td>33.5%</td><td>19.3%</td></tr><tr><td>18</td><td>6669.TW</td><td>Buy</td><td>OW</td><td>12-May-26</td><td>11-Aug-26</td><td>Wiwynn Corp</td><td>4880</td><td>Taiwan Se Weighed Taiex</td><td>-15.7%</td><td>-25.3%</td></tr><tr><td>19</td><td>688008.SS</td><td>Buy</td><td>OW</td><td>5-May-26</td><td>4-Aug-26</td><td>Montage Technology Co Ltd</td><td>244.17</td><td>Shanghai Se Composite</td><td>40.9%</td><td>40.9%</td></tr><tr><td>20</td><td>AXBK.NS</td><td>Buy</td><td>OW</td><td>5-May-26</td><td>4-Aug-26</td><td>Axis Bank</td><td>1365.7</td><td>Bse Sensex</td><td>8.4%</td><td>8.5%</td></tr><tr><td>21</td><td>006400.KS</td><td>Buy</td><td>OW</td><td>5-May-26</td><td>4-Aug-26</td><td>Samsung SDI</td><td>549000</td><td>Korea Se Composite (Kospi)</td><td>-22.1%</td><td>-48.0%</td></tr><tr><td>22</td><td>6674.T</td><td>Buy</td><td>OW</td><td>28-Apr-26</td><td>28-Jul-26</td><td>GS Yuasa Corporation</td><td>6568</td><td>Topix</td><td>6.6%</td><td>0.7%</td></tr><tr><td>23</td><td>0100.HK</td><td>Buy</td><td>OW</td><td>28-Apr-26</td><td>28-Jul-26</td><td>MiniMax</td><td>416.6</td><td>Hang Seng China Enterprises</td><td>-42.4%</td><td>-38.7%</td></tr><tr><td>24</td><td>603986.SS</td><td>Buy</td><td>OW</td><td>28-Apr-26</td><td>28-Jul-26</td><td>GigaDevice Semiconductor Beijing Inc</td><td>532.76</td><td>Shanghai Se Composite</td><td>73.5%</td><td>72.7%</td></tr><tr><td>25</td><td>2318.HK</td><td>Buy</td><td>OW</td><td>21-Apr-26</td><td>21-Jul-26</td><td>Ping An Insurance Group Co of China Ltd</td><td>56.35</td><td>Hang Seng China Enterprises</td><td>-5.1%</td><td>1.8%</td></tr><tr><td>26</td><td>4901.T</td><td>Buy</td><td>OW</td><td>21-Apr-26</td><td>21-Jul-26</td><td>FUJIFILM Holdings</td><td>3379</td><td>Topix</td><td>8.9%</td><td>3.0%</td></tr><tr><td>27</td><td>BILI.O</td><td>Buy</td><td>OW</td><td>21-Apr-26</td><td>21-Jul-26</td><td>Bilibili Inc</td><td>17.3</td><td>Hang Seng China Enterprises</td><td>-26.0%</td><td>-19.0%</td></tr><tr><td>28</td><td>1211.HK</td><td>Buy</td><td>OW</td><td>14-Apr-26</td><td>14-Jul-26</td><td>BYD Company Limited</td><td>84.05</td><td>Hang Seng China Enterprises</td><td>-22.8%</td><td>-18.7%</td></tr><tr><td>29</td><td>3690.HK</td><td>Buy</td><td>OW</td><td>14-Apr-26</td><td>14-Jul-26</td><td>Meituan</td><td>75.3</td><td>Hang Seng China Enterprises</td><td>-11.5%</td><td>-7.5%</td></tr><tr><td>30</td><td>2338.HK</td><td>Buy</td><td>OW</td><td>7-Apr-26</td><td>7-Jul-26</td><td>WeiChai Power</td><td>36.84</td><td>Hang Seng China Enterprises</td><td>26.6%</td><td>28.2%</td></tr><tr><td>31</td><td>009150.KS</td><td>Buy</td><td>OW</td><td>7-Apr-26</td><td>7-Jul-26</td><td>Samsung Electro-Mechanics</td><td>2048000</td><td>Korea Se Composite (Kospi)</td><td>348.1%</td><td>289.2%</td></tr><tr><td>32</td><td>8593.T</td><td>Buy</td><td>OW</td><td>7-Apr-26</td><td>7-Jul-26</td><td>Mitsubishi HC Capital</td><td>1314.5</td><td>Topix</td><td>-11.3%</td><td>-20.6%</td></tr><tr><td>33</td><td>GMG.AX</td><td>Buy</td><td>OW</td><td>31-Mar-26</td><td>30-Jun-26</td><td>Goodman Group</td><td>32.26</td><td>S&amp;P/Asx All Australian 200</td><td>26.6%</td><td>21.0%</td></tr><tr><td>34</td><td>PTTGC.BK</td><td>Buy</td><td>OW</td><td>31-Mar-26</td><td>30-Jun-26</td><td>PTT Global Chemicals</td><td>32.5</td><td>Bangkok S.E.T.</td><td>-11.0%</td><td>-22.2%</td></tr><tr><td>35</td><td>300750.SZ</td><td>Buy</td><td>OW</td><td>24-Mar-26</td><td>23-Jun-26</td><td>Contemporary Amperex Technology Co. Ltd.</td><td>403.53</td><td>Shanghai Se Composite</td><td>3.3%</td><td>-2.7%</td></tr><tr><td>36</td><td>6762.T</td><td>Buy</td><td>OW</td><td>24-Mar-26</td><td>23-Jun-26</td><td>TDK</td><td>3802</td><td>Topix</td><td>88.5%</td><td>75.2%</td></tr><tr><td>37</td><td>028260.KS</td><td>Buy</td><td>OW</td><td>24-Mar-26</td><td>23-Jun-26</td><td>Samsung C&amp;T</td><td>497000</td><td>Korea Se Composite (Kospi)</td><td>76.6%</td><td>18.8%</td></tr></table>

Source: MS, Datastream, Refinitiv, Bloomberg.

Exhibit 5: Three Actionable Ideas – Closed in last 13 weeks

<table><tr><td>No.</td><td>Ticker</td><td>Direction</td><td>Stock Rating*</td><td>Start</td><td>End</td><td>Idea</td><td>Last px**</td><td>Benchmark Index</td><td>Abs perf</td><td>Rel perf</td></tr><tr><td>38</td><td>BABA.N</td><td>Buy</td><td>OW</td><td>17-Mar-26</td><td>16-Jun-26</td><td>Alibaba Group Holding</td><td>110.97</td><td>Hang Seng China Enterprises</td><td>-18.0%</td><td>-12.3%</td></tr><tr><td>39</td><td>4005.T</td><td>Buy</td><td>OW</td><td>17-Mar-26</td><td>16-Jun-26</td><td>Sumitomo Chemical</td><td>576.5</td><td>Topix</td><td>20.7%</td><td>9.5%</td></tr><tr><td>40</td><td>2345.TW</td><td>Buy</td><td>OW</td><td>17-Mar-26</td><td>16-Jun-26</td><td>Accton Technology Corporation</td><td>2520</td><td>Taiwan Se Weighed Taiex</td><td>73.2%</td><td>37.5%</td></tr><tr><td>41</td><td>4004.T</td><td>Buy</td><td>OW</td><td>10-Mar-26</td><td>9-Jun-26</td><td>Resonac Holdings</td><td>18290</td><td>Topix</td><td>53.3%</td><td>45.9%</td></tr><tr><td>42</td><td>055550.KS</td><td>Buy</td><td>OW</td><td>10-Mar-26</td><td>9-Jun-26</td><td>Shinhan Financial Group</td><td>106700</td><td>Korea Se Composite (Kospi)</td><td>14.3%</td><td>-32.8%</td></tr><tr><td>43</td><td>6981.T</td><td>Buy</td><td>OW</td><td>10-Mar-26</td><td>9-Jun-26</td><td>Murata Manufacturing</td><td>10530</td><td>Topix</td><td>166.6%</td><td>159.1%</td></tr><tr><td>44</td><td>300502.SZ</td><td>Buy</td><td>OW</td><td>3-Mar-26</td><td>2-Jun-26</td><td>Eoptolink Technology Inc Ltd</td><td>549</td><td>Shanghai Se Composite</td><td>95.4%</td><td>96.3%</td></tr><tr><td>45</td><td>6758.T</td><td>Buy</td><td>OW</td><td>3-Mar-26</td><td>2-Jun-26</td><td>Sony Group</td><td>3275</td><td>Topix</td><td>9.4%</td><td>4.2%</td></tr><tr><td>46</td><td>2360.TW</td><td>Buy</td><td>OW</td><td>3-Mar-26</td><td>2-Jun-26</td><td>Chroma Ate Inc.</td><td>2325</td><td>Taiwan Se Weighed Taiex</td><td>73.5%</td><td>40.5%</td></tr><tr><td>47</td><td>TLS.AX</td><td>Buy</td><td>OW</td><td>24-Feb-26</td><td>26-May-26</td><td>Telstra Corporation</td><td>5.12</td><td>S&amp;P/Asx All Australian 200</td><td>1.5%</td><td>4.1%</td></tr><tr><td>48</td><td>7550.T</td><td>Buy</td><td>OW</td><td>24-Feb-26</td><td>26-May-26</td><td>Zensho Holdings</td><td>8021</td><td>Topix</td><td>-23.7%</td><td>-27.9%</td></tr><tr><td>49</td><td>QBE.AX</td><td>Buy</td><td>NC</td><td>31-Mar-26</td><td>26-May-26</td><td>QBE Insurance Group</td><td>23.47</td><td>S&amp;P/Asx All Australian 200</td><td>9.3%</td><td>6.7%</td></tr><tr><td>50</td><td>090430.KS</td><td>Buy</td><td>OW</td><td>17-Feb-26</td><td>19-May-26</td><td>Amorepacific</td><td>110400</td><td>Korea Se Composite (Kospi)</td><td>-24.9%</td><td>-57.8%</td></tr><tr><td>51</td><td>0753.HK</td><td>Buy</td><td>OW</td><td>17-Feb-26</td><td>19-May-26</td><td>Air China Limited</td><td>4.7</td><td>Hang Seng China Enterprises</td><td>-35.3%</td><td>-31.0%</td></tr><tr><td>52</td><td>KPLM.SI</td><td>Buy</td><td>OW</td><td>17-Feb-26</td><td>19-May-26</td><td>Keppel Ltd</td><td>11.21</td><td>Straits Times Index L</td><td>-18.2%</td><td>-23.0%</td></tr><tr><td>53</td><td>3659.T</td><td>Buy</td><td>OW</td><td>14-Apr-26</td><td>19-May-26</td><td>Nexon</td><td>2200</td><td>Topix</td><td>-13.7%</td><td>-16.3%</td></tr><tr><td>54</td><td>STEG.SI</td><td>Buy</td><td>OW</td><td>10-Feb-26</td><td>12-May-26</td><td>ST Engineering</td><td>10.79</td><td>Straits Times Index L</td><td>6.1%</td><td>4.4%</td></tr><tr><td>55</td><td>FUTU.O</td><td>Buy</td><td>OW</td><td>10-Feb-26</td><td>12-May-26</td><td>Futu Holdings Ltd</td><td>96.01</td><td>Hang Seng China Enterprises</td><td>-12.1%</td><td>-8.5%</td></tr><tr><td>56</td><td>PREG.NS</td><td>Buy</td><td>OW</td><td>10-Feb-26</td><td>12-May-26</td><td>Prestige Estates Projects Ltd</td><td>1521.1</td><td>Bse Sensex</td><td>-13.3%</td><td>-1.8%</td></tr><tr><td>57</td><td>7182.T</td><td>Buy</td><td>OW</td><td>3-Feb-26</td><td>5-May-26</td><td>Japan Post Bank</td><td>3170</td><td>Topix</td><td>-2.2%</td><td>-5.6%</td></tr><tr><td>58</td><td>2449.TW</td><td>Buy</td><td>OW</td><td>3-Feb-26</td><td>5-May-26</td><td>King Yuan Electronics Co Ltd</td><td>278</td><td>Taiwan Se Weighed Taiex</td><td>20.6%</td><td>-6.3%</td></tr><tr><td>59</td><td>6361.T</td><td>Buy</td><td>OW</td><td>27-Jan-26</td><td>28-Apr-26</td><td>Ebara</td><td>6232</td><td>Topix</td><td>10.0%</td><td>3.1%</td></tr><tr><td>60</td><td>7936.T</td><td>Buy</td><td>OW</td><td>27-Jan-26</td><td>28-Apr-26</td><td>Asics</td><td>4431</td><td>Topix</td><td>18.0%</td><td>11.1%</td></tr><tr><td>61</td><td>2308.TW</td><td>Buy</td><td>OW</td><td>27-Jan-26</td><td>28-Apr-26</td><td>Delta Electronics Inc.</td><td>2230</td><td>Taiwan Se Weighed Taiex</td><td>70.0%</td><td>47.5%</td></tr><tr><td>62</td><td>SHMF.NS</td><td>Buy</td><td>OW</td><td>20-Jan-26</td><td>21-Apr-26</td><td>Shriram Finance Ltd.</td><td>1005.75</td><td>Bse Sensex</td><td>5.9%</td><td>9.3%</td></tr><tr><td>63</td><td>4502.T</td><td>Buy</td><td>OW</td><td>20-Jan-26</td><td>21-Apr-26</td><td>Takeda Pharmaceutical</td><td>5020</td><td>Topix</td><td>10.3%</td><td>5.3%</td></tr><tr><td>64</td><td>068270.KS</td><td>Buy</td><td>OW</td><td>20-Jan-26</td><td>21-Apr-26</td><td>Celltrion Inc</td><td>174500</td><td>Korea Se Composite (Kospi)</td><td>-1.9%</td><td>-33.5%</td></tr><tr><td>65</td><td>0016.HK</td><td>Buy</td><td>OW</td><td>13-Jan-26</td><td>14-Apr-26</td><td>Sun Hung Kai Properties</td><td>116.9</td><td>Hang Seng</td><td>28.1%</td><td>31.3%</td></tr><tr><td>66</td><td>005930.KS</td><td>Buy</td><td>OW</td><td>13-Jan-26</td><td>14-Apr-26</td><td>Samsung Electronics</td><td>343000</td><td>Korea Se Composite 

[中间内容因长度限制已省略]

tional Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
