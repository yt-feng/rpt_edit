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
EM ASIA FX/RATES VIEWS

# We recommend going long INR 30Y bonds on improving macro backdrop, recent RBI FX measures and likely Global Agg Index inclusion

Improved macro outlook: India's local government bond yields initially rose 50-70bp between January and March, reflecting concerns around the country's exposure to higher energy and fertilizer prices. But the overall macro impact has been less than initially feared, with the outlook now improving further with the interim US-Iran deal. Q1 real GDP growth came in at $7.8\%$ yoy, around 50bp above our forecast, led by strong investment and services activity. With Q2 growth tracking above earlier expectations and oil forecasts now revised lower, we recently raised our CY26 real GDP forecast by 0.3pp to $6.8\%$ and our FY27 forecast by 0.4pp to $6.5\%$ . Lower oil prices have also reduced the risk of further increases in retail fuel prices, even as earlier pump-price hikes will continue to feed into inflation in the coming months. We therefore lowered our core inflation forecasts for CY26 by 0.1pp to $4.2\%$ and for CY27 by 0.2pp to $4.0\%$ . Meanwhile, the sharp correction in global urea prices is likely to limit the increase in the government's fertilizer subsidy bill relative to our earlier expectations, and recent import tenders have cleared at substantially lower prices than those seen at the peak of the Middle East conflict. Put together, a lower inflation trajectory and reduced fiscal pressures are supportive for the macro backdrop.

RBI's FX measures: On June 5, the RBI and the Government of India announced a slew of capital flow measures aimed at boosting foreign inflows. These include full FX hedging support for fresh Foreign Currency Non-Resident 3-5Y deposits, concessional FX swap rates for quasi-sovereign companies to raise USD funding, as well as raising the individual investment limits for domestic equities. In our view, there are two bond-related measures which should help attract inflows, while also improving India's index eligibility for the Bloomberg Global Aggregate Index. First, the authorities removed interest and capital gains tax for FIIs in G-Sec. This reduces an important operational friction, including the need for a local tax consultant, which was a burden for foreign investors previously. Second, the expansion of the Fully Accessible Route (FAR) universe to include all new 15-year, 30-year, and 40-year G-Sec issuances is foreign-investor friendly and should improve investability across the sovereign yield curve. While these changes may take time to be fully reflected in market practice, the direction of policy is supportive.

Bloomberg Global Aggregate Index inclusion: Bloomberg Indices in January deferred the decision on India's inclusion in the Global Aggregate Index until mid-2026, citing the need for further review of operational and market infrastructure issues, according to media reports at the time. In our view, the hurdle for inclusion has always been relatively high given the index is predominantly a DM

Danny Suwanapruti  
+65-6889-1987 |  
danny.suwanapruti@gs.com  
GS (Singapore) Pte

Santanu Sengupta +91(22)6616-9042 | santanu.sengupta@gs.com GS India SPL

Arjun Varma  
+91(22)6616-9043 | arjun.varma@gs.com GS India SPL

Andrew Tilton  
+852-2978-1802 | andrew.tilton@gs.com GS (Asia) L.L.C.

sovereign/credit index, whose investor base typically requires smoother market access, trading, and settlement than is needed for global EM local-currency indices. That said, India's full inclusion in the JPM GBI-EM Global Diversified index in March 2025, where it has reached the $9 \%$ weight cap, suggests market access has improved materially, and investor feedback also points to gradual progress in onboarding, collateral, and settlement processes (such as custodians being able to post margin on behalf of investors). Taken together with the RBI's announced measures on June 5, we think India's eventual inclusion in the Global Aggregate Index is increasingly a question of timing rather than direction, with a mid-year announcement likely, in our view. If included into the Global Aggregate Index, we estimate that India's index weight will be around $0.7 \%$ , based on the current outstanding size of FAR bonds (including the newly added ones), which could prompt around \$15bn of passive inflows over the phase-in period.

Where on the curve? The macro backdrop is also turning more supportive for INR duration as inflation expectations are easing and lower oil prices should reduce fiscal risks. We prefer the ultra long-end segment of the yield curve as more ultra-long bonds enter the FAR universe, and the front-end has already rallied sharply on lower oil prices over the past few weeks and the pricing out of RBI rate hike expectations. Moreover, as outlined in our previous work on India's "savings glut", there is an ongoing trend of financialization of household savings, where allocations are shifting away from banks to retirement savings (including pension funds, Public Provident Funds, and insurance companies), which should gradually increase the structural demand for ultra long-end bonds. Put together, we recommend buying INR 30-year bonds (entry $7.34\%$ , target $6.90\%$ and stop-loss $7.65\%$ ). The key risk to this trade is if there is large global duration sell-off (say on more hawkish Fed), which could drag EM bond yields, including India, higher across the curve, or if domestic inflation / fiscal risks re-emerge.

Exhibit 1: We think there is scope for long-end yields to move structurally lower  
![](images/ba38c8c961a443f53adf7bbe10e0e308aebf467090f0d50cacb844c852ce5c67.jpg)  
Source: Bloomberg

Exhibit 2: Long-term investors like insurance companies, pension and provident funds have increased their ownership of IGBs in recent years  
![](images/9d83b46fe2ea3611369520b3d181e09ab65a0ec39b20db0728cef7ff84f2187a.jpg)  
Note: i) Others include RBI, foreign institutions, corporates and financial institutions, ii) Others included pension funds as well prior to 2022, iii) Years are in fiscal years

Exhibit 3: The RBI recently expanded the universe of Fully Accessible Bonds (FAR) bonds to include the ultra-long end

<table><tr><td>ISIN</td><td>Coupon</td><td>Maturity at issuance</td><td>Issue date</td><td>Maturity</td><td>Amount Outstanding (INR bn)</td><td>Amount Outstanding (USD bn)</td></tr><tr><td>IN0020220037</td><td>7.38</td><td>5</td><td>6/20/2022</td><td>6/20/2027</td><td>1,099</td><td>11.64</td></tr><tr><td>IN0020230010</td><td>7.06</td><td>5</td><td>4/10/2023</td><td>4/10/2028</td><td>922</td><td>9.76</td></tr><tr><td>IN0020210186</td><td>5.74</td><td>5</td><td>11/15/2021</td><td>11/15/2026</td><td>467</td><td>4.94</td></tr><tr><td>IN0020250141</td><td>6.36</td><td>5</td><td>2/16/2026</td><td>2/16/2031</td><td>810</td><td>8.58</td></tr><tr><td>IN0020230101</td><td>7.37</td><td>5</td><td>10/23/2023</td><td>10/23/2028</td><td>556</td><td>5.89</td></tr><tr><td>IN0020240159</td><td>6.79</td><td>10</td><td>12/2/2024</td><td>12/2/2034</td><td>100</td><td>1.06</td></tr><tr><td>IN0020240076</td><td>7.02</td><td>7</td><td>6/18/2024</td><td>6/18/2031</td><td>640</td><td>6.78</td></tr><tr><td>IN0020230085</td><td>7.18</td><td>10</td><td>8/14/2023</td><td>8/14/2033</td><td>2,010</td><td>21.28</td></tr><tr><td>IN0020230051</td><td>7.3</td><td>30</td><td>6/19/2023</td><td>6/19/2053</td><td>1,950</td><td>20.65</td></tr><tr><td>IN0020250059</td><td>6.28</td><td>7</td><td>7/14/2025</td><td>7/14/2032</td><td>550</td><td>5.82</td></tr><tr><td>IN0020240019</td><td>7.1</td><td>10</td><td>4/8/2024</td><td>4/8/2034</td><td>1,800</td><td>19.06</td></tr><tr><td>IN0020230077</td><td>7.18</td><td>14</td><td>7/24/2023</td><td>7/24/2037</td><td>1,720</td><td>18.21</td></tr><tr><td>IN0020180454</td><td>7.26</td><td>10</td><td>1/14/2019</td><td>1/14/2029</td><td>1,197</td><td>12.67</td></tr><tr><td>IN0020210244</td><td>6.54</td><td>10</td><td>1/17/2022</td><td>1/17/2032</td><td>1,560</td><td>16.52</td></tr><tr><td>IN0020220011</td><td>7.1</td><td>7</td><td>4/18/2022</td><td>4/18/2029</td><td>1,519</td><td>16.08</td></tr><tr><td>IN0020220060</td><td>7.26</td><td>10</td><td>8/22/2022</td><td>8/22/2032</td><td>1,480</td><td>15.67</td></tr><tr><td>IN0020230135</td><td>7.32</td><td>7</td><td>11/13/2023</td><td>11/13/2030</td><td>700</td><td>7.41</td></tr><tr><td>IN0020250075</td><td>7.24</td><td>30</td><td>8/18/2025</td><td>8/18/2055</td><td>980</td><td>10.38</td></tr><tr><td>IN0020250091</td><td>6.48</td><td>10</td><td>10/6/2025</td><td>10/6/2035</td><td>2,260</td><td>23.93</td></tr><tr><td>IN0020250133</td><td>6.68</td><td>7</td><td>1/27/2026</td><td>1/27/2033</td><td>550</td><td>5.82</td></tr><tr><td>IN0020240191</td><td>6.79</td><td>7</td><td>12/30/2024</td><td>12/30/2031</td><td>630</td><td>6.67</td></tr><tr><td>IN0020240126</td><td>6.79</td><td>10</td><td>10/7/2024</td><td>10/7/2034</td><td>1,840</td><td>19.48</td></tr><tr><td>IN0020230036</td><td>7.17</td><td>7</td><td>4/17/2023</td><td>4/17/2030</td><td>1,030</td><td>10.91</td></tr><tr><td>IN0020250067</td><td>6.01</td><td>5</td><td>7/21/2025</td><td>7/21/2030</td><td>1,170</td><td>12.39</td></tr><tr><td>IN0020220151</td><td>7.26</td><td>10</td><td>2/6/2023</td><td>2/6/2033</td><td>1,500</td><td>15.88</td></tr><tr><td>IN0020210095</td><td>6.1</td><td>10</td><td>7/12/2021</td><td>7/12/2031</td><td>1,524</td><td>16.13</td></tr><tr><td>IN0020240050</td><td>7.04</td><td>5</td><td>6/3/2024</td><td>6/3/2029</td><td>871</td><td>9.22</td></tr><tr><td>IN0020220086</td><td>7.36</td><td>30</td><td>9/12/2022</td><td>9/12/2052</td><td>1,620</td><td>17.15</td></tr><tr><td>IN0020200153</td><td>5.77</td><td>10</td><td>8/3/2020</td><td>8/3/2030</td><td>1,230</td><td>13.02</td></tr><tr><td>IN0020240183</td><td>6.75</td><td>5</td><td>12/23/2024</td><td>12/23/2029</td><td>870</td><td>9.21</td></tr><tr><td>IN0020250026</td><td>6.33</td><td>10</td><td>5/5/2025</td><td>5/5/2035</td><td>1,834</td><td>19.42</td></tr><tr><td>IN0020250042</td><td>6.68</td><td>15</td><td>7/7/2025</td><td>7/7/2040</td><td>2,110</td><td>22.34</td></tr><tr><td>IN0020260025</td><td>6.94</td><td>10</td><td>5/11/2026</td><td>5/11/2036</td><td>680</td><td>7.20</td></tr><tr><td>IN0020190362</td><td>6.45</td><td>10</td><td>10/7/2019</td><td>10/7/2029</td><td>1,148</td><td>12.16</td></tr><tr><td>IN0020200252</td><td>6.67</td><td>30</td><td>11/2/2020</td><td>12/17/2050</td><td>1,492</td><td>15.79</td></tr><tr><td>IN0020220029</td><td>7.54</td><td>14</td><td>5/23/2022</td><td>5/23/2036</td><td>1,539</td><td>16.30</td></tr><tr><td>IN0020200070</td><td>5.79</td><td>10</td><td>5/11/2020</td><td>5/11/2030</td><td>1,116</td><td>11.82</td></tr><tr><td>IN0020220102</td><td>7.41</td><td>14</td><td>12/19/2022</td><td>12/19/2036</td><td>1,650</td><td>17.47</td></tr><tr><td>IN0020200294</td><td>5.85</td><td>10</td><td>12/1/2020</td><td>12/1/2030</td><td>1,208</td><td>12.79</td></tr><tr><td>IN0020210194</td><td>6.99</td><td>30</td><td>11/15/2021</td><td>12/15/2051</td><td>1,484</td><td>15.71</td></tr><tr><td>IN0020230176</td><td>7.37</td><td>30</td><td>1/23/2024</td><td>1/23/2054</td><td>100</td><td>1.06</td></tr><tr><td>IN0020220136</td><td>7.1</td><td>5</td><td>1/27/2023</td><td>1/27/2028</td><td>80</td><td>0.85</td></tr><tr><td>IN0020200054</td><td>7.16</td><td>30</td><td>4/20/2020</td><td>9/20/2050</td><td>1,027</td><td>10.87</td></tr><tr><td>IN0020220144</td><td>7.29</td><td>10</td><td>1/27/2023</td><td>1/27/2033</td><td>80</td><td>0.85</td></tr><tr><td>IN0020190032</td><td>7.72</td><td>30</td><td>4/15/2019</td><td>6/15/2049</td><td>845</td><td>8.95</td></tr><tr><td>IN0020230150</td><td>7.24</td><td>10</td><td>12/11/2023</td><td>12/11/2033</td><td>50</td><td>0.53</td></tr><tr><td>IN0020230143</td><td>7.25</td><td>5</td><td>11/13/2023</td><td>11/13/2028</td><td>50</td><td>0.53</td></tr><tr><td>IN0020260033</td><td>7.71</td><td>40</td><td>5/18/2026</td><td>5/18/2066</td><td>220</td><td>2.33</td></tr><tr><td colspan="4"></td><td>Total</td><td>51,867</td><td>549</td></tr></table>

Source: RBI, Bloomberg, GS Global Investment Research

## Summary tables

Exhibit 4: Our views on relative performance of NJA FX and rates (3 month outlook)

<table><tr><td></td><td>FX outlook*</td><td>Rates outlook**</td><td>Comments</td></tr><tr><td>China</td><td>Bullish</td><td>Neutral</td><td>Export strength, FX undervaluation and PBoC&#x27;s broader tolerance for CNY strength underpins our bullish CNY view. Recent PBoC actions signal pace management of CNY appreciation.</td></tr><tr><td>Korea</td><td>Neutral</td><td>Neutral</td><td>Improving terms of trade outlook (on tech-exports and lower oil) offset by foreign equity outflows. We expect the BoK to hike 3 times versus market pricing of 4 in the next 12-months.</td></tr><tr><td>Taiwan</td><td>Bullish</td><td>Neutral</td><td>Robust trade surplus from tech exports and large accumulation of USD deposits presents asymmetric risk for TWD strength. Neutral on TWD rates, as we expect CBC to remain on hold.</td></tr><tr><td>Hong Kong</td><td>Neutral</td><td>Neutral</td><td>Broad USD strength has pushed USD/HKD towards the upper end of the convertibility band; we expect spot to stay rangebound from here.</td></tr><tr><td>India</td><td>Bullish</td><td>Bullish</td><td>RBI&#x27;s FX measures to attract inflows were meaningful. Lower oil prices should help temper inflation and fiscal concerns. We also like INR duration and recommend 30Y bonds.</td></tr><tr><td>Singapore</td><td>Neutral</td><td>Neutral</td><td>Growth had held up in Q1, while rise in inflation has been moderate. MAS already pre-emptively tightened policy in April and we do not expect further tightening this year.</td></tr><tr><td>Thailand</td><td>Bearish</td><td>Neutral</td><td>BoT remains neutral and likely to look through transitory inflation pressures. Lower gold prices and structural headwinds to the economy should exert weakening pressures on the THB.</td></tr><tr><td>Malaysia</td><td>Bullish</td><td>Neutral</td><td>MYR has been under pressure on increased political risk premium ahead of state elections. However, growth, export and FDI outlook remains solid and we remain constructive the MYR.</td></tr><tr><td>Indonesia</td><td>Bearish</td><td>Bearish</td><td>BI rate hikes and FX measures provided short-term relief for IDR. However, concerns on natural resource export rules, governance and fiscal discipline to keep the IDR under pressure.</td></tr><tr><td>Philippines</td><td>Neutral</td><td>Neutral</td><td>BSP is vigilant on second-round inflation and remains hawkish. However, if oil prices stay low, then an improved terms of trade outlook will be supportive of the PHP.</td></tr></table>

Italics denote a change from our previous stance.

Source: GS Global Investment Research

## Exhibit 5: Trade Ideas in EM Asia rates and FX

Trade Ideas in EM Asia rates and FX

<table><tr><td>Open trades</td><td>Initiated</td><td>Current</td><td>Entry</td><td>Target</td><td>Stop</td><td>Total PnL (capital and carry)</td></tr><tr><td>Long INR 30-year bonds</td><td>26-Jun-26</td><td>7.34%</td><td>7.34%</td><td>6.90%</td><td>7.65%</td><td>+ 0bps</td></tr><tr><td>Short THB/INR</td><td>12-Jun-26</td><td>2.91</td><td>2.91</td><td>2.70</td><td>3.05</td><td>+ 3%</td></tr><tr><td>Short SGD/MYR</td><td>23-Jan-26</td><td>3.19</td><td>3.13</td><td>2.90</td><td>3.30</td><td>- 1.9%</td></tr></table>

\*Target / Spot-loss levels are expressed in index terms to incorporate the total returns from; i) duration, ii) carry and iii) spot FX where appropriate.

<table><tr><td>Closed trades</td><td>Initiated</td><td>Closed</td><td>Entry</td><td>Closed</td><td>Total PnL (capital and carry)</td></tr><tr><td>Receive THB THOR 2Y OIS</td><td>23-Jan-26</td><td>9-Mar-26</td><td>1.20%</td><td>1.13%</td><td>+15bps</td></tr><tr><td>Long PHP 5Y bond FX-hedged</td><td>5-Aug-25</td><td>5-Mar-26</td><td>5.93%</td><td>5.77%</td><td>+32bps</td></tr><tr><td>Long INR 30Y bonds FX-hedged</td><td>5-Sep-25</td><td>11-Feb-26</td><td>7.22%</td><td>7.47%</td><td>+20bps</td></tr><tr><td>KRW 2Y IRS</td><td>18-Nov-25</td><td>4-Feb-26</td><td>2.80%</td><td>3.16%</td><td>-35bps</td></tr><tr><td>Short SGD/TWD</td><td>3-Oct-25</td><td>7-Jan-26</td><td>23.57</td><td>24.6</td><td>-3.80%</td></tr><tr><td>Short THB/KRW</td><td>10-Jan-25</td><td>9-Sep-25</td><td>42.3</td><td>43.74</td><td>-3.30%</td></tr><tr><td>Long 1Y SRBIs fully FX hedged</td><td>3-Oct-24</td><td>21-Jul-25</td><td>6.82%</td><td>6.58%</td><td>+112bp</td></tr><tr><td>Long 2Y CGBs</td><td>6-Apr-25</td><td>16-May-25</td><td>1.47%</td><td>1.47%</td><td>0bp</td></tr><tr><td>Receive INR 2Y NDOIS</td><td>28-Jan-25</td><td>16-May-25</td><td>6.08%</td><td>5.48%</td><td>+44bp</td></tr><tr><td>Long KRW 2s10s IRS Steepener</td><td>4-Sep-24</td><td>16-May-25</td><td>-12bp</td><td>20bp</td><td>+9bp</td></tr><tr><td>Long INR vs. Asian FX basket (CNH, TWD, THB, MYR, and SGD with equal weights)</td><td>6-Jan-25</td><td>3-Apr-25</td><td>100</td><td>100.33</td><td>+33bp</td></tr><tr><td>Long 5Y CGB on a FX-hedged basis</td><td>17-Nov-24</td><td>21-Feb-25</td><td>1.69%</td><td>1.55%</td><td>+14bp</td></tr><tr><td>Long INR vs. Asian FX basket (CNY, KRW, TWD, THB, MYR, SGD and JPY with equal weights)</td><td>17-Nov-24</td><td>6-Jan-24</td><td>100</td><td>100.48</td><td>+114bp</td></tr><tr><td>Long 2Y IGBs FX-unhedged</td><td>29-Feb-24</td><td>6-Nov-24</td><td>7.02%</td><td>6.50%</td><td>+3.8%</td></tr><tr><td>Pay THB 2Y THOR OIS</td><td>7-Aug-24</td><td>1-Oct-24</td><td>2.02%</td><td>2.04%</td><td>+8bp</td></tr><tr><td>Short CNY vs. CFETS basket</td><td>9-Aug-24</td><td>30-Sep-24</td><td>100</td><td>103</td><td>-0.7%</td></tr><tr><td>Short EUR/INR</td><td>12-Jan-24</td><td>21-Aug-24</td><td>90.91</td><td>93</td><td>-0.3%</td></tr><tr><td>Rec SGD 2Y SORA OIS vs. basket of global 2Y rates</td><td>14-Apr-23</td><td>6-Aug-24</td><td>-8bp</td><td>-28bp</td><td>+42bp</td></tr><tr><td>Short THB/KRW</td><td>15-Mar-24</td><td>26-Jul-24</td><td>37.17</td><td>38.31</td><td>-2.7%</td></tr><tr><td>Long THB 3Y bonds vs. paying 3Y THOR swaps</td><td>10-Jan-24</td><td>10-Jul-24</td><td>-20</td><td>-10</td><td>+10bp</td></tr><tr><td>Long 1Y CGB (FX hedged)</td><td>10-Nov-23</td><td>27-Apr-24</td><td>2.25%</td><td>1.65%</td><td>+60bp</td></tr><tr><td>Long 10Y INDOGBs FX-unhedged</td><td>14-Dec-23</td><td>17-Apr-24</td><td>6.60%</td><td>6.75%</td><td>-15bp</td></tr><tr><td>Short TWD/KRW</td><td>13-Jun-23</td><td>15-Mar-24</td><td>41.42</td><td>41.83</td><td>+0.3%</td></tr><tr><td>Short MYRTHB</td><td>10-Nov-23</td><td>7-Feb-24</td><td>7.63</td><td>7.48</td><td>+2.0%</td></tr></table>

Source: GS Glob

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
