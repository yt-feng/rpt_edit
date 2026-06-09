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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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
## Asia | Asia Pacific

# Three Actionable Ideas

Furukawa Electric – OW | Westpac Banking – UW | Hindustan Petroleum – OW

OW – Furukawa Electric (5801.T): New record profit with sharp growth is in scope, thanks to higher optical and water-cooling module sales; we raise our price target to ¥66,000 and reiterate our OW rating.

UW – Westpac Banking (WBC.AX): We have lowered our estimates and price targets to reflect a shift in the outlook for the Australian housing and mortgage market. We retain our Cautious industry view.

OW – Hindustan Petroleum (HPCL.NS): Energy security is paramount and policymakers are acting in ways that surprised consensus. Indian fuel retailers are most levered plays to improving energy supplies beyond the oil shock. HPCL key pick.

## Links to reports:

Furukawa Electric: Accelerating Growth in Optical and Water-cooling Businesses; Reiterate OW Rating (3 Jun 2026)

Australia Banks: Air Pocket (4 Jun 2026)

India Fuel Retailers: Energy Security in Play (3 Jun 2026)

Exhibit 1: Performance summary

<table><tr><td>As of June 2</td><td>Absolute</td><td>Relative*</td></tr><tr><td>No. of ideas</td><td colspan="2">1503</td></tr><tr><td>Cumulative Outperformance (bps)</td><td colspan="2">9,363</td></tr><tr><td>Avg holding period total return</td><td>4.3%</td><td>2.0%</td></tr><tr><td>Avg 12M total return**</td><td>16.0%</td><td>10.6%</td></tr><tr><td>No. of positive returns</td><td>810</td><td>748</td></tr><tr><td>Hit ratio</td><td>54%</td><td>50%</td></tr></table>

Source: MS, DataStream Refinitiv, Bloomberg. Performance data as at Jun 2, 2026. Cumulative outperformance: against local benchmarks. Holding period total return measures performance when idea was effective. \*\*Avg. 12M total return measures performance of all ideas (closed and active) from Jun 2, 2025, to Jun 2, 2026, and does not adjust for buy/sell direction. \* Relative performance = idea outperformance against local benchmarks. Hit ratio = number of ideas with positive returns as percentage of the total number of ideas. Performance calculation does not consider transaction costs or other costs. Figures are not audited. Past performance is not a guarantee of future results.

MS ASIA LIMITED+

## Samuel Lee, CFA

Equity Strategist

Samuel.Sw.Lee@morganstanley.com +852 2239-1862

## Hozefa Topiwalla

Equity Strategist

Hozefa.Topiwalla@morganstanley.com +852 2848-6595

![](images/1b23b4d7ce551d1ee2a7f70a7719b729c95c0eef37cc3b38fac8faef83db7959.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

![](images/b101c193bd13f356ee8c2aea0b40002d093bbd6b37d7f048f2c893a827c2f88d.jpg)

<details>
<summary>text_image</summary>

Three in Three - Asia
Click Here For Collection >
</details>

Latest closing prices as of June 5, 2026:

Furukawa Electric (5801.T): ¥49,050.00;

Westpac Banking (WBC.AX): A\$34.81; Hindustan

Petroleum (HPCL.NS): Rs385.05.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Three Actionable Ideas

Exhibit 2: Cumulative outperformance  
![](images/4e377d9f5ea0d5678167cf39ac07ed64e8dce10375b4b2fb1135194606583ad4.jpg)

<details>
<summary>line chart</summary>

| Date     | Value |
| -------- | ----- |
| A-16A    | 95.0  |
| A-16D    | 115.0 |
| A-16E    | 117.0 |
| A-17A    | 118.0 |
| A-17D    | 120.0 |
| A-17E    | 122.0 |
| A-18A    | 125.0 |
| A-18D    | 128.0 |
| A-18E    | 130.0 |
| A-19A    | 132.0 |
| A-19D    | 135.0 |
| A-19E    | 138.0 |
| A-20A    | 145.0 |
| A-20D    | 155.0 |
| A-20E    | 165.0 |
| A-21A    | 170.0 |
| A-21D    | 172.0 |
| A-21E    | 175.0 |
| A-22A    | 173.0 |
| A-22D    | 170.0 |
| A-22E    | 168.0 |
| A-23A    | 170.0 |
| A-23D    | 175.0 |
| A-23E    | 180.0 |
| A-24A    | 185.0 |
| A-24D    | 180.0 |
| A-24E    | 175.0 |
| A-25A    | 178.0 |
| A-25D    | 185.0 |
| A-25E    | 190.0 |
| A-26A    | 195.0 |
| A-26B    | 200.0 |
</details>

Source: MS, Datastream, Refinitiv, Bloomberg. The performance calculation does not consider transaction costs or other costs. These figures are not audited. Past performance is not a guarantee of future results.

Exhibit 3: Weekly hit ratio  
![](images/ce1d617de2ae332ab9ab2a64d7f525d02703a7c01d69144b53fecdeae91564be.jpg)

<details>
<summary>line chart</summary>

| Date     | Weekly Hit Ratio |
| -------- | ---------------- |
| M-16     | 80%              |
| S-16     | 70%              |
| J-17     | 60%              |
| M-17     | 55%              |
| S-17     | 55%              |
| J-18     | 55%              |
| M-18     | 55%              |
| S-18     | 55%              |
| J-19     | 55%              |
| M-19     | 55%              |
| S-19     | 55%              |
| J-20     | 55%              |
| M-20     | 55%              |
| S-20     | 55%              |
| J-21     | 55%              |
| M-21     | 55%              |
| S-21     | 55%              |
| J-22     | 55%              |
| M-22     | 55%              |
| S-22     | 55%              |
| J-23     | 55%              |
| M-23     | 55%              |
| S-23     | 55%              |
| J-24     | 55%              |
| M-24     | 55%              |
| S-24     | 55%              |
| J-25     | 55%              |
| M-25     | 55%              |
| S-25     | 55%              |
| J-26     | 55%              |
| M-26     | 50%              |
</details>

Source: MS, Datastream, Refinitiv, Bloomberg. The performance calculation does not consider transaction costs or other costs. These figures are not audited. Past performance is not a guarantee of future results. The hit ratio as of any particular Tuesday does not account for ideas started on the same day for which holding period was 0 days.

Three Actionable Ideas are not and should not be considered a portfolio: Each investment idea is chosen based on its own merit and without any consideration of the other investment ideas chosen. Specifically, there has been no effort to mitigate the risks of investing in any collective group of "Three Actionable Ideas". Concepts important to a balanced portfolio, such as negative correlation and diversification, have not been considered. Treating "Three Actionable Ideas" ideas as a portfolio will subject you to the risk of losing all or a substantial portion of your investments.

The information contained herein has been prepared solely for informational purposes and is not a solicitation of any offer to buy or sell any security or other financial instrument or to participate in any trading strategy. Products and trades of this type may not be appropriate for every investor. Please consult with your legal and tax advisors before making any investment decision. Please contact your MS sales representative for more details.

Exhibit 4: Three Actionable Ideas – Still in effect

<table><tr><td>No.</td><td>Ticker</td><td>Direction</td><td>Stock Rating*</td><td>Start</td><td>End</td><td>Idea</td><td>Last px**</td><td>Benchmark Index</td><td>Abs perf</td><td>Rel perf</td></tr><tr><td>1</td><td>3563.T</td><td>Buy</td><td>OW</td><td>2-Jun-26</td><td>1-Sep-26</td><td>FOOD &amp; LIFE COMPANIES</td><td>10475</td><td>Topix</td><td>0.0%</td><td>0.0%</td></tr><tr><td>2</td><td>002371.SZ</td><td>Buy</td><td>OW</td><td>2-Jun-26</td><td>1-Sep-26</td><td>NAURA Technology Group Co Ltd</td><td>602.8</td><td>Shanghai Se Composite</td><td>0.0%</td><td>0.0%</td></tr><tr><td>3</td><td>5274.TWO</td><td>Buy</td><td>OW</td><td>2-Jun-26</td><td>1-Sep-26</td><td>Aspeed Technology</td><td>18095</td><td>Taiwan Se Weighed Taiex</td><td>0.0%</td><td>0.0%</td></tr><tr><td>4</td><td>TITN.NS</td><td>Buy</td><td>OW</td><td>26-May-26</td><td>25-Aug-26</td><td>Titan Company Ltd</td><td>4078.1</td><td>Bse Sensex</td><td>-0.7%</td><td>1.1%</td></tr><tr><td>5</td><td>285A.T</td><td>Buy</td><td>OW</td><td>26-May-26</td><td>25-Aug-26</td><td>KIOXIA Holdings</td><td>77540</td><td>Topix</td><td>24.1%</td><td>24.4%</td></tr><tr><td>6</td><td>3908.HK</td><td>Buy</td><td>OW</td><td>26-May-26</td><td>25-Aug-26</td><td>China International Capital Corp. Ltd.</td><td>19.74</td><td>Hang Seng China Enterprises</td><td>-4.4%</td><td>-6.7%</td></tr><tr><td>7</td><td>BHP.AX</td><td>Buy</td><td>OW</td><td>19-May-26</td><td>18-Aug-26</td><td>BHP Group Ltd</td><td>63.37</td><td>S&amp;P/Asx All Australian 200</td><td>8.0%</td><td>6.7%</td></tr><tr><td>8</td><td>JARD.SI</td><td>Buy</td><td>OW</td><td>19-May-26</td><td>18-Aug-26</td><td>Jardine Matheson Holdings Limited</td><td>64.22</td><td>Hang Seng</td><td>-10.5%</td><td>-11.8%</td></tr><tr><td>9</td><td>3017.TW</td><td>Buy</td><td>OW</td><td>19-May-26</td><td>18-Aug-26</td><td>Asia Vital Components Co. Ltd.</td><td>2700</td><td>Taiwan Se Weighed Taiex</td><td>13.0%</td><td>-0.4%</td></tr><tr><td>10</td><td>7011.T</td><td>Buy</td><td>OW</td><td>12-May-26</td><td>11-Aug-26</td><td>Mitsubishi Heavy Industries</td><td>3516</td><td>Topix</td><td>-18.2%</td><td>-19.6%</td></tr><tr><td>11</td><td>402340.KS</td><td>Buy</td><td>OW</td><td>12-May-26</td><td>11-Aug-26</td><td>SK Square Co Ltd.</td><td>1346000</td><td>Korea Se Composite (Kospi)</td><td>19.7%</td><td>4.5%</td></tr><tr><td>12</td><td>6669.TW</td><td>Buy</td><td>OW</td><td>12-May-26</td><td>11-Aug-26</td><td>Wiwynn Corp</td><td>5475</td><td>Taiwan Se Weighed Taiex</td><td>-5.4%</td><td>-14.2%</td></tr><tr><td>13</td><td>688008.SS</td><td>Buy</td><td>OW</td><td>5-May-26</td><td>4-Aug-26</td><td>Montage Technology Co Ltd</td><td>237</td><td>Shanghai Se Composite</td><td>36.8%</td><td>37.4%</td></tr><tr><td>14</td><td>AXBK.NS</td><td>Buy</td><td>OW</td><td>5-May-26</td><td>4-Aug-26</td><td>Axis Bank</td><td>1251.1</td><td>Bse Sensex</td><td>-0.7%</td><td>2.2%</td></tr><tr><td>15</td><td>006400.KS</td><td>Buy</td><td>OW</td><td>5-May-26</td><td>4-Aug-26</td><td>Samsung SDI</td><td>602000</td><td>Korea Se Composite (Kospi)</td><td>-14.6%</td><td>-41.5%</td></tr><tr><td>16</td><td>6674.T</td><td>Buy</td><td>OW</td><td>28-Apr-26</td><td>28-Jul-26</td><td>GS Yuasa Corporation</td><td>6861</td><td>Topix</td><td>11.3%</td><td>7.2%</td></tr><tr><td>17</td><td>0100.HK</td><td>Buy</td><td>OW</td><td>28-Apr-26</td><td>28-Jul-26</td><td>MiniMax</td><td>667.5</td><td>Hang Seng China Enterprises</td><td>-7.7%</td><td>-9.6%</td></tr><tr><td>18</td><td>603986.SS</td><td>Buy</td><td>OW</td><td>28-Apr-26</td><td>28-Jul-26</td><td>GigaDevice Semiconductor Beijing Inc</td><td>474.69</td><td>Shanghai Se Composite</td><td>54.6%</td><td>54.4%</td></tr><tr><td>19</td><td>2318.HK</td><td>Buy</td><td>OW</td><td>21-Apr-26</td><td>21-Jul-26</td><td>Ping An Insurance Group Co of China Ltd</td><td>58.6</td><td>Hang Seng China Enterprises</td><td>-1.3%</td><td>0.2%</td></tr><tr><td>20</td><td>4901.T</td><td>Buy</td><td>OW</td><td>21-Apr-26</td><td>21-Jul-26</td><td>FUJIFILM Holdings</td><td>3346</td><td>Topix</td><td>7.8%</td><td>3.7%</td></tr><tr><td>21</td><td>BILI.O</td><td>Buy</td><td>OW</td><td>21-Apr-26</td><td>21-Jul-26</td><td>Bilibili Inc</td><td>18.65</td><td>Hang Seng China Enterprises</td><td>-20.2%</td><td>-18.7%</td></tr><tr><td>22</td><td>1211.HK</td><td>Buy</td><td>OW</td><td>14-Apr-26</td><td>14-Jul-26</td><td>BYD Company Limited</td><td>96.75</td><td>Hang Seng China Enterprises</td><td>-11.6%</td><td>-13.1%</td></tr><tr><td>23</td><td>3690.HK</td><td>Buy</td><td>OW</td><td>14-Apr-26</td><td>14-Jul-26</td><td>Meituan</td><td>85.5</td><td>Hang Seng China Enterprises</td><td>0.5%</td><td>-1.1%</td></tr><tr><td>24</td><td>2338.HK</td><td>Buy</td><td>OW</td><td>7-Apr-26</td><td>7-Jul-26</td><td>WeiChai Power</td><td>39.22</td><td>Hang Seng China Enterprises</td><td>34.8%</td><td>30.6%</td></tr><tr><td>25</td><td>009150.KS</td><td>Buy</td><td>OW</td><td>7-Apr-26</td><td>7-Jul-26</td><td>Samsung Electro-Mechanics</td><td>1813000</td><td>Korea Se Composite (Kospi)</td><td>296.7%</td><td>236.4%</td></tr><tr><td>26</td><td>8593.T</td><td>Buy</td><td>OW</td><td>7-Apr-26</td><td>7-Jul-26</td><td>Mitsubishi HC Capital</td><td>1265</td><td>Topix</td><td>-14.7%</td><td>-22.1%</td></tr><tr><td>27</td><td>GMG.AX</td><td>Buy</td><td>OW</td><td>31-Mar-26</td><td>30-Jun-26</td><td>Goodman Group</td><td>31.6</td><td>S&amp;P/Asx All Australian 200</td><td>23.9%</td><td>20.6%</td></tr><tr><td>28</td><td>PTTGC.BK</td><td>Buy</td><td>OW</td><td>31-Mar-26</td><td>30-Jun-26</td><td>PTT Global Chemicals</td><td>34.5</td><td>Bangkok S.E.T.</td><td>-5.5%</td><td>-16.7%</td></tr><tr><td>29</td><td>300750.SZ</td><td>Buy</td><td>OW</td><td>24-Mar-26</td><td>23-Jun-26</td><td>Contemporary Amperex Technology Co. Ltd.</td><td>433.89</td><td>Shanghai Se Composite</td><td>11.0%</td><td>5.8%</td></tr><tr><td>30</td><td>6762.T</td><td>Buy</td><td>OW</td><td>24-Mar-26</td><td>23-Jun-26</td><td>TDK</td><td>3849</td><td>Topix</td><td>90.8%</td><td>79.4%</td></tr><tr><td>31</td><td>028260.KS</td><td>Buy</td><td>OW</td><td>24-Mar-26</td><td>23-Jun-26</td><td>Samsung C&amp;T</td><td>485500</td><td>Korea Se Composite (Kospi)</td><td>72.5%</td><td>13.4%</td></tr><tr><td>32</td><td>BABA.N</td><td>Buy</td><td>OW</td><td>17-Mar-26</td><td>16-Jun-26</td><td>Alibaba Group Holding</td><td>130.82</td><td>Hang Seng China Enterprises</td><td>-4.2%</td><td>-4.1%</td></tr><tr><td>33</td><td>4005.T</td><td>Buy</td><td>OW</td><td>17-Mar-26</td><td>16-Jun-26</td><td>Sumitomo Chemical</td><td>583.4</td><td>Topix</td><td>22.2%</td><td>12.8%</td></tr><tr><td>34</td><td>2345.TW</td><td>Buy</td><td>OW</td><td>17-Mar-26</td><td>16-Jun-26</td><td>Accton Technology Corporation</td><td>2425</td><td>Taiwan Se Weighed Taiex</td><td>66.7%</td><td>31.9%</td></tr><tr><td>35</td><td>4004.T</td><td>Buy</td><td>OW</td><td>10-Mar-26</td><td>9-Jun-26</td><td>Resonac Holdings</td><td>17825</td><td>Topix</td><td>65.0%</td><td>56.8%</td></tr><tr><td>36</td><td>055550.KS</td><td>Buy</td><td>OW</td><td>10-Mar-26</td><td>9-Jun-26</td><td>Shinhan Financial Group</td><td>96400</td><td>Korea Se Composite (Kospi)</td><td>8.9%</td><td>-51.0%</td></tr><tr><td>37</td><td>6981.T</td><td>Buy</td><td>OW</td><td>10-Mar-26</td><td>9-Jun-26</td><td>Murata Manufacturing</td><td>10230</td><td>Topix</td><td>181.4%</td><td>173.1%</td></tr></table>

Source: MS, Datastream, Refinitiv, Bloomberg.  
Note: Performance data as at last price date Jun 2, 2026. \*Stock ratings refer to that when the idea was introduced unless the coverage is dropped or rating is removed from consideration because under MS policy and/or applicable regulations. NC - Currently not covered by MS. 12M performance refers to average total return of the ideas from Jun 2, 2025 to Jun 2, 2026, and does not adjust for buy/sell direction. These figures are not audited. Past performance is no guarantee of future results. Results shown exclude brokerage commissions and transaction costs. Certain historical Three Actionable Ideas have been removed because under MS policy and/or applicable regulations, MS may be precluded from issuing such information with respect to this company at this time. ++ = Stock Rating, Price Target or Estimates are not available or have been removed due to applicable law and/or MS policy. Please note that all important disclosures including personal holding disclosures and MS disclosures for stocks under coverage appear on the MS public website at www.morganstanley.com/researchdisclosures. For non-covered (NC) stocks please refer to Important US Regulatory Disclosures on Subject Companies and Other Important Disclosures located at the back of this report. Please refer to this section for more details.

Exhibit 5: Three Actionable Ideas – Closed in last 13 weeks

<table><tr><td>No.</td><td>Ticker</td><td>Direction</td><td>Stock Rating*</td><td>Start</td><td>End</td><td>Idea</td><td>Last px**</td><td>Benchmark Index</td><td>Abs perf</td><td>Rel perf</td></tr><tr><td>38</td><td>300502.SZ</td><td>Buy</td><td>OW</td><td>3-Mar-26</td><td>2-Jun-26</td><td>Eoptolink Technology Inc Ltd</td><td>747</td><td>Shanghai Se Composite</td><td>95.4%</td><td>96.3%</td></tr><tr><td>39</td><td>6758.T</td><td>Buy</td><td>OW</td><td>3-Mar-26</td><td>2-Jun-26</td><td>Sony Group</td><td>3669</td><td>Topix</td><td>9.4%</td><td>4.2%</td></tr><tr><td>40</td><td>2360.TW</td><td>Buy</td><td>OW</td><td>3-Mar-26</td><td>2-Jun-26</td><td>Chroma Ate Inc.</td><td>2420</td><td>Taiwan Se Weighed Taiex</td><td>73.5%</td><td>40.5%</td></tr><tr><td>41</td><td>TLS.AX</td><td>Buy</td><td>OW</td><td>24-Feb-26</td><td>26-May-26</td><td>Telstra Corporation</td><td>5.16</td><td>S&amp;P/Asx All Australian 200</td><td>1.5%</td><td>4.1%</td></tr><tr><td>42</td><td>7550.T</td><td>Buy</td><td>OW</td><td>24-Feb-26</td><td>26-May-26</td><td>Zensho Holdings</td><td>7957</td><td>Topix</td><td>-23.7%</td><td>-27.9%</td></tr><tr><td>43</td><td>QBE.AX</td><td>Buy</td><td>NC</td><td>31-Mar-26</td><td>26-May-26</td><td>QBE Insurance Group</td><td>22.1</td><td>S&amp;P/Asx All Australian 200</td><td>9.3%</td><td>6.7%</td></tr><tr><td>44</td><td>090430.KS</td><td>Buy</td><td>OW</td><td>17-Feb-26</td><td>19-May-26</td><td>Amorepacific</td><td>109300</td><td>Korea Se Composite (Kospi)</td><td>-24.9%</td><td>-57.8%</td></tr><tr><td>45</td><td>0753.HK</td><td>Buy</td><td>OW</td><td>17-Feb-26</td><td>19-May-26</td><td>Air China Limited</td><td>4.78</td><td>Hang Seng China Enterprises</td><td>-35.3%</td><td>-31.0%</td></tr><tr><td>46</td><td>KPLM.SI</td><td>Buy</td><td>OW</td><td>17-Feb-26</td><td>19-May-26</td><td>Keppel Ltd</td><td>10.95</td><td>Straits Times Index L</td><td>-18.2%</td><td>-23.0%</td></tr><tr><td>47</td><td>3659.T</td><td>Buy</td><td>OW</td><td>14-Apr-26</td><td>19-May-26</td><td>Nexon</td><td>2315.5</td><td>Topix</td><td>-13.7%</td><td>-16.3%</td></tr><tr><td>48</td><td>STEG.SI</td><td>Buy</td><td>OW</td><td>10-Feb-26</td><td>12-May-26</td><td>ST Engineering</td><td>11.16</td><td>Straits Times Index L</td><td>6.1%</td><td>4.4%</td></tr><tr><td>49</td><td>FUTU

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
