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
## Global Credit Strategy & Securitized Products Research

# AI Debt Financing Tracker: Warming Up for a Hot Summer

The majority of issuance QTD was to fund construction of data center shells. April was the busiest month YTD with a notable deceleration in May. Hyperscalers have been broadening their investor base through non-USD issuance. We're starting to see more chip financing structures across markets, and expect AI-related supply to accelerate going into 2H26.

## Key Takeaways

April Ran Hot: April saw the highest supply YTD with >\$74bn of AI-related issuance. Project finance structures to fund construction of data center shells accounted for 85% of the AI-related HY supply and 40% of the IG.  
“May” Be Catching Its Breath: We saw limited new issuance in the US markets in May, but hyperscalers collectively issued \~\$24bn of debt in other currencies (EUR, CAD, CHF, and JPY). These issuers’ relatively smaller representation in EUR/GBP benchmarks (vs. USD) leaves room for more non-USD supply, as hyperscalers expand and diversify their investor base.  
■ Technicals Over Fundamentals: Fundamental backdrop remains strong, but for now we think price action is being mostly driven by supply expectations. The market has broadly tightened across asset classes since end of 1Q despite elevated supply.  
We Forecast \~\$570bn of AI-Related Global Supply in 2026: We're at \~\$236bn YTD (until 5/31), >4x more than global AI-related issuance during same period in 2025. We expect issuance to accelerate in 2H26 as our equity colleagues estimate hyperscaler cash capex to surpass \$1tn in 2027.  
Chip Financing in Focus: We are starting to see more chip financing activity in public and private markets. Deals so far have come with shorter maturities vs. some data center construction transactions, and full amortization. We expect to see increasing investor demand for these structures.

This deck tracks the accelerating AI-related financing cycle, highlighting surging hyperscaler capex, expanding debt issuance across different asset classes (IG/HY/Securitized Credit) and currencies. If you'd like underlying data for this report, please reach out here.

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Fernanda Lima</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Fernanda.Lima@morganstanley.com</td><td>+1 212 761-3021</td></tr><tr><td colspan="2">Carolyn L Campbell</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Carolyn.Campbell@morganstanley.com</td><td>+1 212 761-3748</td></tr><tr><td colspan="2">Vishwanath Tirupattur</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Vishwanath.Tirupattur@morganstanley.com</td><td>+1 212 761-1043</td></tr><tr><td colspan="2">Vishwas Patkar</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Vishwas.Patkar@morganstanley.com</td><td>+1 212 761-8041</td></tr><tr><td colspan="2">James Egan</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>James.F.Egan@MorganStanley.com</td><td>+1 212 761-4715</td></tr><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="2">Aron Becker</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Aron.Becker@morganstanley.com</td><td>+44 20 7677-0754</td></tr><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Kelvin Pang</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Kelvin.Pang@morganstanley.com</td><td>+852 2848-8204</td></tr><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Catherine Liu</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Catherine.Liu2@morganstanley.com</td><td>+1 212 761-0222</td></tr><tr><td colspan="2">Eva C Baurmeister</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Eva.Baurmeister@morganstanley.com</td><td>+1 212 761-4588</td></tr><tr><td colspan="2">Christina C Sigler</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Christina.Sigler@morganstanley.com</td><td>+1 212 761-4116</td></tr><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="2">Jonathan Loke</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Jonathan.Loke1@morganstanley.com</td><td>+44 20 7677-3136</td></tr><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Raquel Kanner</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Raquel.Kanner@morganstanley.com</td><td>+1 212 761-1103</td></tr><tr><td colspan="2">MS INDIA COMPANY PRIVATE LIMITED+</td></tr><tr><td colspan="2">Yagyesh Modi</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Yagyesh.Modi@morganstanley.com</td><td>+91 22 6995-2808</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

MS & CO. INTERNATIONAL PLC+

## Ellie Dann

Strategist

Ellie.Dann@morganstanley.com

+44 20 7425-2599

## See our other recent reports:

- Securitized & Corporate Credit: Data Center Financing: Faster, Broader, Deeper (26 May 2026)  
- Deep Thoughts on Securitized Markets: Data Center Financing and Value Across Securitized and Corporate Credit | Ep. 360 (29 May 2026)  
- US Credit Strategy & Securitized Products Research: AI Debt Financing Tracker (10 Apr 2026)

## MS

## AI Debt Financing Tracker – Warming Up For a Hot Summer

- April Ran Hot: April saw the highest supply YTD with >\$74bn of AI-related issuance. Project finance structures to fund construction of data center shells accounted for 85% of the AI-related HY supply and 40% of the IG.  
- “May” Be Catching Its Breath: We saw limited new issuance in the US markets in May, but hyperscalers collectively issued \~\$24bn of debt in other currencies (EUR, CAD, CHF, and JPY). These issuers’ relatively smaller representation in EUR/GBP benchmarks (vs. USD) leaves room for more non-USD supply, as hyperscalers expand and diversify their investor base.  
- Technicals Over Fundamentals: Fundamental backdrop remains strong, but for now we think price action is being mostly driven by supply expectations. The market has broadly tightened across asset classes since end of 1Q despite elevated supply.  
- We Forecast \~\$570bn of AI-Related Global Supply in 2026: We're at \~\$236bn YTD (until 5/31), >4x more than global AI-related issuance during same period in 2025. We expect issuance to accelerate in 2H26 as our equity colleagues estimate hyperscaler cash capex to surpass \$1tn in 2027.  
- Chip Financing in Focus: We are starting to see more chip financing activity in public and private markets. Deals so far have come with shorter maturities vs. some data center construction transactions, and full amortization. We expect to see increasing investor demand for these structures.

Data as of May 31, 2026, unless otherwise indicated. This deck covers public, tradeable debt in USD, EUR, GBP, CHF, CAD, JPY.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Authors

## North America

MS & Co. LLC

Fernanda Lima

Credit Strategist

Fernanda.Lima@morganstanley.com

+1 212.761.3021

## Vishwas Patkar

Head of U.S. Corporate Credit Research

Vishwas.Patkar@morganstanley.com

+1 212.761.8041

## Christina Sigler

Credit Strategist

Christina.Sigler@morganstanley.com

+1 212.761.4116

## Europe

MS & Co. International PLC+

Aron Becker

Credit Strategist

Aron.Becker@morganstanley.com

+44 20 7677.0693

## Ellie Dann

Credit Strategist

Ellie.Dann@morganstanley.com

+44 20 7425.2599

## Jonathan Loke

Credit Strategist

Jonathan.Loke1@morganstanley.com

+44 20 7677.3136

## Carolyn Campbell

ABS Strategist

Carolyn.Campbell@morganstanley.com

+1 212.761.3748

## James Egan

Co-Head of Securitized Products Research

James.F.Egan@morganstanley.com

+1 212.761.4715

## Catherine Liu

CMBS Strategist

Catherine.Liu@morganstanley.com

+1 212.761.0022

## MS India Company Private Limited+

Yagyesh Modi

Credit Strategist

Yagyesh.Modi@morganstanley.com

+91 22 6995-2808

## Vishwanath Tirupattur

Chief Fixed Income Strategist

Vishwanath.Tirupattur@morganstanley.com

+1 212.761.1043

## Eva Baurmeister

Credit Strategist

Eva.Baurmeister@morganstanley.com

+1 212.761.4588

## Raquel Kanner

ABS Strategist

Raquel.Kanner@morganstanley.com

+1 212.761.1103

## Asia Pacific

MS Asia Limited+

Kelvin Pang

Credit Strategist

Kelvin.Pang@morganstanley.com

+852 2848.8204

## MS

AI Debt Financing Tracker | Issuance Summary & Estimates

<table><tr><td rowspan="2" colspan="2">Markets</td><td rowspan="2">Issuers$bn, unless otherwise noted</td><td colspan="8">Year-to-Date Issuance Tracker</td><td colspan="3">Full Year Tracker</td></tr><tr><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>2026 YTD</td><td>2025 YTD</td><td>Δ %</td><td>2026E</td><td>2025A</td><td>Δ %</td></tr><tr><td rowspan="12">Corporate Credit (U.S.)</td><td rowspan="7">U.S. Investment Grade</td><td>Hyperscalers</td><td>0.0</td><td>20.0</td><td>37.0</td><td>25.0</td><td>0.0</td><td>82.0</td><td>5.0</td><td>1540%</td><td rowspan="2">300.0</td><td rowspan="2">93.3</td><td rowspan="2">222%</td></tr><tr><td>Oracle</td><td>0.0</td><td>25.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>25.0</td><td>7.8</td><td>223%</td></tr><tr><td>Semiconductors</td><td>4.5</td><td>0.0</td><td>0.0</td><td>7.5</td><td>0.0</td><td>12.0</td><td>16.6</td><td>-28%</td><td rowspan="4">100.0</td><td rowspan="4">64.1</td><td rowspan="4">56%</td></tr><tr><td>Data Center REITS</td><td>0.0</td><td>1.5</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.5</td><td>0.0</td><td>-</td></tr><tr><td>Data Center Construction</td><td>0.0</td><td>0.0</td><td>0.0</td><td>7.9</td><td>0.0</td><td>7.9</td><td>0.0</td><td>-</td></tr><tr><td>Anchored/Structured DC Construction</td><td>0.0</td><td>0.0</td><td>0.0</td><td>14.0</td><td>0.0</td><td>14.0</td><td>0.0</td><td>-</td></tr><tr><td>Total IG</td><td>4.5</td><td>46.5</td><td>37.0</td><td>54.4</td><td>0.0</td><td>142.4</td><td>29.4</td><td>385%</td><td>400.0</td><td>157.4</td><td>154%</td></tr><tr><td rowspan="4">U.S. Leverage Finance</td><td>Data Center Construction</td><td>0.0</td><td>5.8</td><td>2.2</td><td>15.9</td><td>0.0</td><td>23.8</td><td>0.0</td><td>-</td><td rowspan="2">50.0</td><td rowspan="2">15.3</td><td rowspan="2">226%</td></tr><tr><td>Regular Corporate Issuance</td><td>0.0</td><td>0.0</td><td>0.0</td><td>2.8</td><td>0.0</td><td>2.8</td><td>2.0</td><td>38%</td></tr><tr><td>Loans</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>3.1</td><td>3.1</td><td>0.0</td><td>-</td><td>15.0</td><td>2.0</td><td>650%</td></tr><tr><td>Total LevFin</td><td>0.0</td><td>5.8</td><td>2.2</td><td>18.6</td><td>3.1</td><td>29.7</td><td>2.0</td><td>1384%</td><td>65.0</td><td>17.3</td><td>275%</td></tr><tr><td colspan="2">Total Corporate Credit</td><td>4.5</td><td>52.3</td><td>39.2</td><td>73.0</td><td>3.1</td><td>172.0</td><td>31.4</td><td>449%</td><td>465.0</td><td>174.7</td><td>166%</td></tr><tr><td rowspan="3">Securitized Credit (U.S.)</td><td rowspan="2">Securitized Credit</td><td>ABS</td><td>1.9</td><td>2.9</td><td>2.7</td><td>1.4</td><td>0.0</td><td>8.9</td><td>6.9</td><td>28%</td><td>21.2</td><td>15.9</td><td>33%</td></tr><tr><td>CMBS</td><td>0.0</td><td>2.1</td><td>0.0</td><td>0.0</td><td>1.1</td><td>3.1</td><td>5.7</td><td>-45%</td><td>9.0</td><td>11.5</td><td>-22%</td></tr><tr><td colspan="2">Total Securitized Credit</td><td>1.9</td><td>4.9</td><td>2.7</td><td>1.4</td><td>1.1</td><td>12.0</td><td>12.6</td><td>-5%</td><td>30.2</td><td>27.4</td><td>10%</td></tr><tr><td colspan="3">Total U.S. Credit Markets</td><td>6.4</td><td>57.2</td><td>41.8</td><td>74.4</td><td>4.2</td><td>184.0</td><td>44.0</td><td>319%</td><td>495.2</td><td>202.2</td><td>145%</td></tr><tr><td rowspan="6">Corporate Credit (non-U.S.)</td><td rowspan="5">IG Hyperscalers</td><td>EUR</td><td>0.0</td><td>0.0</td><td>16.8</td><td>0.0</td><td>10.5</td><td>27.3</td><td>7.7</td><td>255%</td><td>50.0</td><td>15.2</td><td>230%</td></tr><tr><td>GBP $^{1}$ </td><td>0.0</td><td>7.5</td><td>0.0</td><td>0.0</td><td>0.0</td><td>7.5</td><td>0.0</td><td>-</td><td>7.5</td><td>0.0</td><td>-</td></tr><tr><td>CAD $^{1}$ </td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>6.2</td><td>6.2</td><td>0.0</td><td>-</td><td>6.2</td><td>0.0</td><td>-</td></tr><tr><td>CHF $^{1}$ </td><td>0.0</td><td>4.0</td><td>0.0</td><td>0.0</td><td>3.6</td><td>7.6</td><td>0.0</td><td>-</td><td>7.6</td><td>0.0</td><td>-</td></tr><tr><td>JPY $^{1}$ </td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>3.6</td><td>3.6</td><td>0.0</td><td>-</td><td>3.6</td><td>0.0</td><td>-</td></tr><tr><td colspan="2">Total IG Other Currencies</td><td>0.0</td><td>11.5</td><td>16.8</td><td>0.0</td><td>24.0</td><td>52.3</td><td>7.7</td><td>580%</td><td>75.0</td><td>15.2</td><td>394%</td></tr><tr><td colspan="3">Total Global Credit Markets</td><td>6.4</td><td>68.7</td><td>58.6</td><td>74.4</td><td>28.2</td><td>236.3</td><td>51.6</td><td>357%</td><td>570.2</td><td>217.3</td><td>162%</td></tr></table>

Notes: Presented figures exclude current and estimated EUR/non-USD issuance across securitized credit. 1. We don't have FY26 estimates for hyperscaler issuance in GBP, CAD, CHF, and JPY, and therefore in the 2026E column we reflect current YTD values for these currencies.  
Source: Bloomberg, Pitchbook | LCD, CreditFlow, TREPP, MS Estimates.

## MS

## AI Debt Financing | QTD 2Q26 Issuance Pricing At a Glance

Corporate Credit

<table><tr><td>Ticker</td><td>Issue Date</td><td>Maturity Date</td><td>Size ($bn)</td><td>Composite Rating</td><td>Coupon</td><td>Issue Spread to Benchmark (bps)</td><td>Current Spread to Benchmark (bps)</td><td>Spread Δ Since Issuance (bps)</td></tr><tr><td colspan="9">Investment Grade</td></tr><tr><td>QTSQST</td><td>4/6/2026</td><td>4/15/2036</td><td>4.60</td><td>NR</td><td>5.700%</td><td>138</td><td>166</td><td>+29</td></tr><tr><td>RDMICH</td><td>4/24/2026</td><td>3/30/2045</td><td>14.00</td><td>BBB-</td><td>7.500%</td><td>329</td><td>340</td><td>+11</td></tr><tr><td>HUTRBA</td><td>4/27/2026</td><td>11/15/2042</td><td>3.25</td><td>NR</td><td>6.192%</td><td>185</td><td>160</td><td>-25</td></tr><tr><td>INTC</td><td>4/27/2026</td><td>6/1/2031</td><td>1.00</td><td>BBB</td><td>4.650%</td><td>75</td><td>66</td><td>-9</td></tr><tr><td>INTC</td><td>4/27/2026</td><td>5/15/2036</td><td>2.25</td><td>BBB</td><td>5.300%</td><td>100</td><td>94</td><td>-7</td></tr><tr><td>INTC</td><td>4/27/2026</td><td>5/15/2056</td><td>1.75</td><td>BBB</td><td>6.125%</td><td>120</td><td>115</td><td>-6</td></tr><tr><td>META</td><td>4/30/2026</td><td>5/15/2031</td><td>3.00</td><td>AA-</td><td>4.550%</td><td>53</td><td>43</td><td>-10</td></tr><tr><td>META</td><td>4/30/2026</td><td>5/15/2036</td><td>6.00</td><td>AA-</td><td>5.250%</td><td>90</td><td>82</td><td>-8</td></tr><tr><td>META</td><td>4/30/2026</td><td>5/15/2056</td><td>6.00</td><td>AA-</td><td>6.300%</td><td>132</td><td>125</td><td>-7</td></tr><tr><td colspan="9">High Yield</td></tr><tr><td>CRWV</td><td>4/9/2026</td><td>10/1/2031</td><td>2.75</td><td>B+</td><td>9.750%</td><td>586</td><td>496</td><td>-90</td></tr><tr><td>MERIDI</td><td>4/16/2026</td><td>4/30/2031</td><td>5.70</td><td>BB</td><td>6.250%</td><td>233</td><td>200</td><td>-33</td></tr><tr><td>EDGCOM</td><td>4/21/2026</td><td>4/30/2031</td><td>1.30</td><td>BB</td><td>7.500%</td><td>358</td><td>346</td><td>-12</td></tr><tr><td>TRACTD</td><td>4/28/2026</td><td>5/1/2031</td><td>4.59</td><td>BB</td><td>6.500%</td><td>288</td><td>229</td><td>-59</td></tr><tr><td>CORZ</td><td>4/22/2026</td><td>5/15/2031</td><td>3.30</td><td>BB-</td><td>7.750%</td><td>399</td><td>299</td><td>-100</td></tr><tr><td>SECMOS</td><td>4/30/2026</td><td>5/1/2031</td><td>1.00</td><td>NR</td><td>8.875%</td><td>499</td><td>368</td><td>-131</td></tr><tr><td>ELKGVP</td><td>6/2/2026</td><td>6/15/2031</td><td>0.90</td><td>BB-</td><td>7.500%</td><td>333</td><td>298</td><td>-34</td></tr><tr><td colspan="9">Lev Loans</td></tr><tr><td>CRWC</td><td>5/15/2026</td><td>11/17/2031</td><td>3.10</td><td>BB</td><td>S+450</td><td>472</td><td>399</td><td>-73</td></tr></table>

Securitized Credit

<table><tr><td>Bond</td><td>Issue Date</td><td>Anticipated Repayment Date</td><td>Size ($bn)</td><td>Composite Rating</td><td>Coupon</td><td>Issue Spread to Benchmark (bps)</td><td>Current Spread to Benchmark (bps)</td><td>Spread Δ Since Issuance (bps)</td></tr><tr><td colspan="9">ABS</td></tr><tr><td>CLDHQ 2026-1 A2I</td><td>4/20/2026</td><td>4/15/2031</td><td>0.725</td><td>AAA</td><td>5.05%</td><td>125</td><td>108</td><td>-17</td></tr><tr><td>CLDHQ 2026-1 A2II</td><td>4/20/2026</td><td>4/15/2031</td><td>0.225</td><td>AA-</td><td>5.34%</td><td>155</td><td>128</td><td>-27</td></tr><tr><td>CLDHQ 2026-1 A2III</td><td>4/20/2026</td><td>4/15/2031</td><td>0.250</td><td>A</td><td>5.54%</td><td>175</td><td>156</td><td>-19</td></tr><tr><td>CLDHQ 2026-1 B1</td><td>4/20/2026</td><td>4/15/2031</td><td>0.100</td><td>A-</td><td>5.88%</td><td></td><td></td><td></td></tr><tr><td>CLDHQ 2026-1 B2</td><td>4/20/2026</td><td>4/15/2031</td><td>0.100</td><td>BBB</td><td>6.36%</td><td></td><td></td><td></td></tr><tr><td colspan="9">CMBS</td></tr><tr><td>CONE 2026-DFW3 A</td><td>5/1/2026</td><td>5/1/2031</td><td>0.522</

[中间内容因长度限制已省略]

Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i)

are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Aron Becker; Eva C Baurmeister; Vishwanath Tirupattur; James Egan; Kelvin Pang; Carolyn L Campbell; Raquel Kanner; Yagyesh Modi; Ellie Dann; Vishwas Patkar; Fernanda Lima; Christina C Sigler.

© 2026 MS
"""
