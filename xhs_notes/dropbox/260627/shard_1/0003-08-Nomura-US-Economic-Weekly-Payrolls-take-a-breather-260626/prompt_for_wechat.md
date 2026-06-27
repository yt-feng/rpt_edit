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
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Economics - North America

## Payrolls take a breather

\- We expect job gains decelerated to 70k in June, primarily due to the waning impact of some temporary factors that boosted May's payrolls. Overall, we still believe that the labor market remains resilient, which is likely to keep the Fed focused on inflation.

\- We expect Chair Warsh will repeat his June FOMC comments at the ECB's Sintra forum and is unlikely to break any new ground, but one key aspect to watch is how he describes recent developments in the Middle East and energy prices.

\- Data released this week suggests growth remains resilient. Real personal spending growth accelerated in May, despite Iran war-related uncertainty, while the durable goods report points to broad based business investment.

## Research Analysts

North America Economics

Aichi Amemiya - NSI  
aichi.amemiya@NOM.com  
+1 212 667 9347

Jeremy Schwartz - NSI
jeremy.schwartz@NOM.com
+1 212 667 9637

Ruchir Sharma - NSI  
ruchir.sharma@NOM.com  
+1 212 667 9186

## Job gains likely slowed in June

We expect headline NFP growth slowed to 70k in June, slightly below the year-to-date average. Some reversal in the noisy factors that boosted the May print points to a deceleration in June, but overall we believe that the labor market remains resilient.

Jacklyn Goloborodsky - NSI
jacklyn.goloborodsky@NOM.com
+1 212 298 4739

## Global Economics

David Seif - NSI
david.seif@NOM.com
+1 212 667 9180

Lead indicators have remained modestly positive, with few signs of stress in the labor market. Weekly ADP data have slowed from its peak, but continue to point to solid employment growth in the private sector and continuing claims rose through the June NFP survey reference week (Fig. 1). Survey data have been mixed, with flash PMIs pointing to some softening, while regional surveys suggest modest improvement.

Fig. 1: Continuing jobless rose through the June NFP survey reference week  
![](images/9bd85ea3c70d3797b6b6bbc1deffe88a512c9751c3c45b694e5ebd840cb45f2b.jpg)  
Note: Markers refer to NFP survey reference week  
Source: DOL, BLS, Haver, NOM

Fig. 2: Outsized employment gains in some sectors boosted the May print, and is likely to reverse in June Employment indices of national and regional service surveys  
![](images/c09c918b8f8bbd1d2235f16cdea993051d40487b2a936e340c7cf4c5f76a66f0.jpg)  
Source: BLS, Haver, NOM

Despite these relatively constructive signals, we expect payroll gains slowed in June. NFP has been a positive outlier in recent months, supported in part by temporary factors (Fig. 2). The pace of job gains in leisure and hospitality, likely reflecting FIFA World Cup-related hiring and noisy seasonals, appears unsustainable and likely unwounded in the

Production Complete: 2026-06-26 18:08 UTC

month. In addition, the outsized increase in local government employment in May, which pushed government job gains to their strongest monthly pace since July 2024, is likely to fade.

We expect the unemployment rate ticked up slightly, but remained unchanged on a rounded basis at $4.3\%$ in June. Measures of layoffs have remained subdued lately (Fig. 3), while labor demand seems to be stabilizing following a downtrend in 2025.

We expect average hourly earnings (AHE) growth slowed to $0.2\%$ m-o-m in June. Alternative wage measures, including the Atlanta Fed Wage Growth Tracker and ADP Pay Insights, have continued to trend lower, albeit gradually (Fig. 4). This should help prevent a pickup in wage-sensitive supercore services inflation.

Fig. 3: Layoffs have remained subdued Job loss rates  
![](images/979715e45f6c3157a4ccd010aba0f3e354e36ba053c8e10c486d65991d5b4059.jpg)  
Source: BLS, Haver, NOM

Fig. 4: Wage measures have continued to trend lower, albeit gradually  
![](images/1f3f040c43fa24e68cf15816f81f82a36b1f44ea98679b91f6c0a9c52af69008.jpg)  
Source: BEA, BLS, Atlanta Fed, ADP, Indeed, Haver, NOM

## Warsh likely to echo his June FOMC comments at Sintra

We expect Chair Warsh will keep his cards close at the Sintra meeting, similar to the post-FOMC press conference, deflecting pointed questions by deferring to the five task forces currently being assembled. The more important signal will be how he frames recent developments in the Middle East and the decline in crude oil prices. Hawks on the Committee view elevated inflation as at risk of becoming entrenched, while doves attribute it to transitory factors such as energy prices and tariffs. If Warsh characterizes falling oil prices as an encouraging sign for the inflation outlook, that would signal a dovish lean. Moreover, it would be key if he mentions something about the labor markets since he did not elucidate his views much in the June press conference.

## Post-FOMC Fedspeak reduces the likelihood of a July rate hike

NY Fed President Williams remained dovish in his prepared remarks, suggesting he remains comfortable with the current stance of monetary policy with which the Fed can bring inflation down to 2% on a sustained basis despite hawkish revisions to his economic outlook. Williams acknowledged that inflation remains “unquestionably elevated” and well above the FOMC’s target. However, he still expects inflation to decline as tariff effects fade, energy and related goods prices stabilize, and shelter inflation eases. Chicago Fed President Goolsbee, a hawk, continued to express concerns over resilience of services inflation. Minneapolis Fed President Kashkari echoed concerns over sticky services inflation and revealed that he penciled in one rate hike for 2026 in his June dot plot (Fig. 5). Hawkish policymakers have emphasized the importance of composition of inflation, suggesting their recent hawkish pivot was not driven simply by temporary factors such as tariffs or higher energy prices. That said, Goolsbee said that one month data of inflation would be "no month," which suggests that the June inflation data are unlikely to lead to a rate hike at the July FOMC meeting. Despite his hawkish bias, Goolsbee seemed to support the Fed's wait-and-see mode for now.

Separately, in his public appearances earlier this week, Treasury Secretary Bessent indicated further reduction in political pressures on easing monetary policy. He was fully confident in Warsh's leadership as Fed Chair and acknowledged that Warsh "came out tough talking about inflation." Moreover, he mentioned favorably of mid-cycle adjustments to the policy rate in early 1997 when former Fed Chair Greenspan engineered "one tap-on-the-brakes rate hike" that did not weigh on economic activities substantially. In the meantime, President Trump argued that lower interest rates would be needed to support housing markets. Overall, Bessent's relatively hawkish comment suggests that the White House is becoming neutral on the near-term monetary policy outlook.

We maintain our Fed call of no changes to the federal funds rate through the end of 2027.

Fig. 5: A majority of hawkish dots were likely submitted by non-voting regional Fed presidents  
NOM's guess: individual 2026 dots at the June FOMC meeting

<table><tr><td>%</td><td colspan="2">2026 dots as of June</td><td></td><td>Voter &#x27;26</td></tr><tr><td>4.375</td><td>Logan</td><td>Three rate hikes</td><td>1</td><td>Y</td></tr><tr><td>4.125</td><td>Schmid</td><td>Two rate hikes</td><td>2</td><td></td></tr><tr><td>4.125</td><td>Hammack</td><td>Two rate hikes</td><td>3</td><td>Y</td></tr><tr><td>4.125</td><td>Musalem</td><td>Two rate hikes</td><td>4</td><td></td></tr><tr><td>4.125</td><td>Goolsbee</td><td>Two rate hikes</td><td>5</td><td></td></tr><tr><td>4.125</td><td>Collins</td><td>Two rate hikes</td><td>6</td><td></td></tr><tr><td>3.875</td><td>Barkin</td><td>One rate hike</td><td>7</td><td></td></tr><tr><td>3.875</td><td>Kashkari</td><td>One rate hike</td><td>8</td><td>Y</td></tr><tr><td>3.875</td><td>Barr</td><td>One rate hike</td><td>9</td><td>Y</td></tr><tr><td>3.625</td><td>Venable</td><td>Unchanged</td><td>10</td><td></td></tr><tr><td>3.625</td><td>Cook</td><td>Unchanged</td><td>11</td><td>Y</td></tr><tr><td>3.625</td><td>Waller</td><td>Unchanged</td><td>12</td><td>Y</td></tr><tr><td>3.625</td><td>Jefferson</td><td>Unchanged</td><td>13</td><td>Y</td></tr><tr><td>3.625</td><td>Powell</td><td>Unchanged</td><td>14</td><td>Y</td></tr><tr><td>3.625</td><td>Daly</td><td>Unchanged</td><td>15</td><td></td></tr><tr><td>3.625</td><td>Paulson</td><td>Unchanged</td><td>16</td><td>Y</td></tr><tr><td>3.625</td><td>Williams</td><td>Unchanged</td><td>17</td><td>Y</td></tr><tr><td>3.375</td><td>Bowman</td><td>One more rate cut</td><td>18</td><td>Y</td></tr></table>

Source: FRB, NOM  
Fig. 6: The wedge between core PCE inflation and core CPI inflation could narrow after the BEA's methodological changes are implemented  
Decomposition of the wedge in y-o-y core PCE inflation between the PCE price index and CPI

![](images/2d96a5d62bb531e9c9c6f5dfa04005636dc06c46e2f0be05b16885115db0a363.jpg)  
Source: BEA, BLS, Haver, NOM

## Core PCE inflation accelerated in May, driven by service components

Core PCE inflation rose $0.320\%$ m-o-m in May from $0.250\%$ m-o-m in April, boosted by service components derived from PPI data (e.g., healthcare services, financial services and airline fares). By contrast, as we had expected, core goods PCE inflation turned negative on a m-o-m basis for the first time since November 2025. This translates to y-o-y core PCE inflation on $3.412\%$ in May, up from $3.319\%$ in April.

PCE trimmed mean inflation picked up only modestly to 0.23% m-o-m in May from 0.20% in April. Its 12-month change ticked up to 2.41% in May from 2.34% in April. Given the strength in May core PCE inflation, the wedge in y-o-y inflation between the core PCE price index and trimmed-mean index remained large (100bp). We do not know whether Chair Warsh or the task force on the inflation framework will put a heavy weight on PCE trimmed-mean inflation. However, we think the wide divergence between core inflation and trimmed-mean inflation highlights the importance of how to gauge the underlying inflation trend. From the trimmed-mean inflation perspective, inflation has not accelerated much. Considering lower crude oil prices, waning impact from tariffs, and moderating wage growth, it seems reasonable for the Fed to remain patient on rate hikes and assess how inflation will evolve for some time.

Upcoming methodological changes to the PCE price index seems disinflationary

The BEA announced future changes to its methodology to estimate certain key PCE price components, including portfolio management and investment advice services, legal services, and computer software and accessories. The net impact from those changes has the potential to lower y-o-y core PCE inflation by 20-30bp, which has not been incorporated into our official inflation forecast yet. Those changes will take effect on 30 September 2026, along with annual revisions to the national account data. As a result, the degree of core PCE inflation's outperformance over core CPI inflation might become narrower (Fig. 6).

## Growth momentum continues

Data released this week were overall positive, pointing to continued resilience in growth. Personal spending growth rose to 0.7% m-o-m in May following a 0.4% advance in April. Spending was robust across goods and services. Based on the PCE deflator, real personal spending grew 0.3% m-o-m in May, suggesting that consumption has remained resilient despite higher gasoline prices and Iran war-related uncertainty. Looking ahead, we expect lower gasoline prices to weigh on headline inflation, while relatively stable income growth should help keep consumption steady in the coming months.

Durable goods orders report also suggested continued and broad based strength in business investment. Excluding transportation, durable goods orders rose 1.3% m-o-m (NOM and Consensus: 0.6%). Core capital goods orders (nondefense capital goods ex aircraft), a leading indicator for equipment investment, also remained strong.

## Q2 GDP tracking

We have lowered our Q2 GDP tracking estimate to 2.4% q-o-q ar from 2.6% last week. Our estimate for real final sales to private domestic purchasers remained unchanged at 2.8%. Data released were generally positive for domestic demand; however, Q1 GDP revisions and a sharp pick up in goods trade deficit in May, lowered our Q2 GDP tracking.

Fig. 7: NOM's inflation forecasts

<table><tr><td rowspan="2"></td><td colspan="2">Headline PCE</td><td colspan="3">Core PCE</td><td colspan="2">Headline CPI</td><td colspan="3">Core CPI</td><td>CPI NSA</td></tr><tr><td>m/m %</td><td>y/y %</td><td>m/m %</td><td>y/y %</td><td>qtrly, y/y %</td><td>m/m %</td><td>y/y %</td><td>m/m %</td><td>y/y %</td><td>qtrly, y/y %</td><td>Index</td></tr><tr><td>Jan-25</td><td>0.35</td><td>2.61</td><td>0.31</td><td>2.78</td><td></td><td>0.43</td><td>3.00</td><td>0.43</td><td>3.26</td><td></td><td>317.671</td></tr><tr><td>Feb-25</td><td>0.40</td><td>2.71</td><td>0.45</td><td>2.97</td><td></td><td>0.23</td><td>2.82</td><td>0.25</td><td>3.12</td><td></td><td>319.082</td></tr><tr><td>Mar-25</td><td>0.02</td><td>2.36</td><td>0.10</td><td>2.67</td><td>2.81</td><td>0.03</td><td>2.39</td><td>0.07</td><td>2.79</td><td>3.08</td><td>319.799</td></tr><tr><td>Apr-25</td><td>0.17</td><td>2.28</td><td>0.19</td><td>2.61</td><td></td><td>0.16</td><td>2.31</td><td>0.24</td><td>2.78</td><td></td><td>320.795</td></tr><tr><td>May-25</td><td>0.18</td><td>2.46</td><td>0.23</td><td>2.78</td><td></td><td>0.10</td><td>2.35</td><td>0.13</td><td>2.79</td><td></td><td>321.465</td></tr><tr><td>Jun-25</td><td>0.29</td><td>2.59</td><td>0.26</td><td>2.81</td><td>2.74</td><td>0.25</td><td>2.67</td><td>0.23</td><td>2.93</td><td>2.82</td><td>322.561</td></tr><tr><td>Jul-25</td><td>0.17</td><td>2.61</td><td>0.25</td><td>2.86</td><td></td><td>0.23</td><td>2.70</td><td>0.31</td><td>3.06</td><td></td><td>323.048</td></tr><tr><td>Aug-25</td><td>0.26</td><td>2.75</td><td>0.22</td><td>2.91</td><td></td><td>0.35</td><td>2.92</td><td>0.31</td><td>3.11</td><td></td><td>323.976</td></tr><tr><td>Sep-25</td><td>0.26</td><td>2.79</td><td>0.19</td><td>2.83</td><td>2.87</td><td>0.30</td><td>3.01</td><td>0.22</td><td>3.02</td><td>3.06</td><td>324.800</td></tr><tr><td>Oct-25</td><td>0.19</td><td>2.71</td><td>0.23</td><td>2.75</td><td></td><td>0.03</td><td>2.76</td><td>0.11</td><td>2.81</td><td></td><td>324.372</td></tr><tr><td>Nov-25</td><td>0.22</td><td>2.82</td><td>0.18</td><td>2.83</td><td></td><td>0.22</td><td>2.74</td><td>0.08</td><td>2.63</td><td></td><td>324.122</td></tr><tr><td>Dec-25</td><td>0.33</td><td>2.88</td><td>0.33</td><td>2.97</td><td>2.85</td><td>0.30</td><td>2.68</td><td>0.23</td><td>2.64</td><td>2.69</td><td>324.054</td></tr><tr><td>Jan-26</td><td>0.35</td><td>2.88</td><td>0.44</td><td>3.10</td><td></td><td>0.17</td><td>2.39</td><td>0.30</td><td>2.50</td><td></td><td>325.252</td></tr><tr><td>Feb-26</td><td>0.40</td><td>2.87</td><td>0.39</td><td>3.05</td><td></td><td>0.27</td><td>2.41</td><td>0.22</td><td>2.46</td><td></td><td>326.785</td></tr><tr><td>Mar-26</td><td>0.67</td><td>3.54</td><td>0.30</td><td>3.25</td><td>3.14</td><td>0.87</td><td>3.26</td><td>0.20</td><td>2.60</td><td>2.53</td><td>330.213</td></tr><tr><td>Apr-26</td><td>0.41</td><td>3.80</td><td>0.25</td><td>3.32</td><td></td><td>0.64</td><td>3.81</td><td>0.38</td><td>2.75</td><td></td><td>333.020</td></tr><tr><td>May-26</td><td>0.45</td><td>4.07</td><td>0.32</td><td>3.41</td><td></td><td>0.47</td><td>4.25</td><td>0.21</td><td>2.85</td><td></td><td>335.123</td></tr><tr><td>Jun-26</td><td>0.02</td><td>3.80</td><td>0.25</td><td>3.40</td><td>3.38</td><td>-0.08</td><td>3.88</td><td>0.26</td><td>2.85</td><td>2.81</td><td>335.065</td></tr><tr><td>Jul-26</td><td>0.12</td><td>3.75</td><td>0.21</td><td>3.36</td><td></td><td>0.05</td><td>3.70</td><td>0.22</td><td>2.75</td><td></td><td>335.015</td></tr><tr><td>Aug-26</td><td>0.18</td><td>3.67</td><td>0.20</td><td>3.34</td><td></td><td>0.20</td><td>3.54</td><td>0.22</td><td>2.66</td><td></td><td>335.439</td></tr><tr><td>Sep-26</td><td>0.20</td><td>3.60</td><td>0.20</td><td>3.35</td><td>3.35</td><td>0.24</td><td>3.46</td><td>0.22</td><td>2.66</td><td>2.69</td><td>336.041</td></tr><tr><td>Oct-26</td><td>0.14</td><td>3.55</td><td>0.22</td><td>3.34</td><td></td><td>0.12</td><td>3.54</td><td>0.22</td><td>2.77</td><td></td><td>335.861</td></tr><tr><td>Nov-26</td><td>0.21</td><td>3.54</td><td>0.21</td><td>3.37</td><td></td><td>0.24</td><td>3.54</td><td>0.22</td><td>2.91</td><td></td><td>335.600</td></tr><tr><td>Dec-26</td><td>0.25</td><td>3.45</td><td>0.21</td><td>3.25</td><td>3.32</td><td>0.30</td><td>3.51</td><td>0.22</td><td>2.90</td><td>2.86</td><td>335.430</td></tr><tr><td>Jan-27</td><td>0.20</td><td>3.30</td><td>0.25</td><td>3.05</td><td></td><td>0.19</td><td>3.54</td><td>0.27</td><td>2.87</td><td></td><td>336.765</td></tr><tr><td>Feb-27</td><td>0.12</td><td>3.01</td><td>0.20</td><td>2.86</td><td></td><td>0.06</td><td>3.34</td><td>0.20</td><td>2.85</td><td></td><td>337.696</td></tr><tr><td>Mar-27</td><td>0.21</td><td>2.55</td><td>0.20</td><td>2.76</td><td>2.89</td><td>0.21</td><td>2.70</td><td>0.20</td><td>2.85</td><td>2.86</td><td>339.123</td></tr><tr><td>Apr-27</td><td>0.17</td><td>2.30</td><td>0.20</td><td>2.71</td><td></td><td>0.14</td><td>2.17</td><td>0.19</td><td>2.66</td><td></td><td>340.258</td></tr><tr><td>May-27</td><td>0.17</td><td>2.01</td><td>0.20</td><td>2.59</td><td></td><td>0.14</td><td>1.82</td><td>0.19</td><td>2.65</td><td></td><td>341.230</td></tr><tr><td>Jun-27</td><td>0.16</td><td>2.15</td><td>0.20</td><td>2.53</td><td>2.61</td><td>0.13</td><td>2.05</td><td>0.19</td><td>2.57</td><td>2.63</td><td>341.918</td></tr><tr><td>Jul-27</td><td>0.18</td><td>2.21</td><td>0.19</td><td>2.52</td><td></td><td>0.19</td><td>2.18</td><td>0.19</td><td>2.54</td><td></td><td>342.316</td></tr><tr><td>Aug-27</td><td>0.20</td><td>2.23</td><td>0.19</td><td>2.50</td><td></td><td>0.20</td><td>2.19</td><td>0.18</td><td>2.50</td><td></td><td>342.779</td></tr><tr><td>Sep-27</td><td>0.22</td><td>2.25</td><td>0.19</td><td>2.48</td><td>2.50</td><td>0.23</td><td>2.19</td><td>0.18</td><td>2.47</td><td>2.50</td><td>343.388</td></tr><tr><td>Oct-27</td><td>0.14</td><td>2.25</td><td>0.19</td><td>2.45</td><td></td><td>0.12</td><td>2.19</td><td>0.18</td><td>2.43</td><td></td><td>343.211</td></tr><tr><td>Nov-27</td><td>0.21</td><td>2.25</td><td>0.18</td><td>2.43</td><td></td><td>0.23</td><td>2.18</td><td>0.18</td><td>2.38</td><td></td><td>342.932</td></tr><tr><td>Dec-27</td><td>0.24</td><td>2.25</td><td>0.18</td><td>2.40</td><td>2.43</td><td>0.29</td><td>2.18</td><td>0.18</td><td>2.34</td><td>2.38</td

[中间内容因长度限制已省略]

t of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Securities International, Inc., US. All rights reserved.
"""
