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
GLOBAL FX TRADER

# Deferential to the Differential

Our thoughts on USD, EM FX, GBP, JPY, MYR, and AI and the Dollar - USD: Back to basics. The Dollar has moved stronger in tandem with rate differentials following the hawkish reaction to last week's FOMC decision. There has been some surprise that the currency has strengthened despite the move lower in oil. But as we discussed last week, rate differentials have a more consistent and significant relationship with exchange rates, which we think accounts for the range break. We see risks for the Dollar as still skewed to the upside in the near term because we think the probability of rate hikes could move up quickly, but come out only slowly. Over the medium term, however risks remain more balanced. We see three primary routes for the Dollar to weaken over time. First, the shift in relative policy pricing has now been sufficiently large that pricing out rate hikes in the future, in line with our economists' view, would weigh on the currency enough to put us back in the previous multi-month range. Second, if institutional credibility concerns were to return—particularly through a perceived overly dovish reaction function—that would again weigh on the Dollar. And finally, our economists expect growth to slow somewhat in the second half of the year as positive economic impulses fade, so we still see a route to a weaker Dollar in response to less exceptional performance than before. But on the other hand, we increasingly see an upside case for the Dollar if Fed officials determine that policy is not sufficiently restrictive, particularly in light of strong AI-related capital expenditures. This would be especially positive for the currency if that level of restriction proves more challenging for countries in Europe and elsewhere that would import tighter financial conditions from the Fed without the commensurate demand for AI-related investment. We believe that economic developments over the last few months, and policymaker communications over the last few weeks, make this outcome increasingly likely, but not our baseline.

■ EM FX: Low-yielder lowdown. The Thai Baht (THB), Israeli Shekel (ILS) and the Chilean Peso (CLP) were the worst performing EM currencies versus the Dollar over the past week across the major regions (Exhibit 1). The common theme here is that these are among the lowest yielding currencies in Asia, EMEA and Latam, and so the underperformance here is consistent with our view that a bear-flattening in US rates, induced by a hawkish Fed meeting in June, should put most pressure on low-yielding currencies across G10 and EM. As we discussed

Kamakshya Trivedi +44(20)7051-4005 | kamakshya.trivedi@gs.com GS International

Michael Cahill  
+44(20)7552-8314 |  
michael.e.cahill@gs.com  
GS International

Danny Suwanapruti  
+65-6889-1987 |  
danny.suwanapruti@gs.com  
GS (Singapore) Pte

Teresa Alves  
+44(20)7051-7566 |  
teresa.alves@gs.com  
GS International

Karen Reichgott Fishman  
+1(212)855-6006 |  
karen.fishman@gs.com  
GS & Co. LLC

Stuart Jenkins  
+44(20)7051-4700 |  
stuart.jenkins@gs.com  
GS International

Victor Engel  
+44(20)7051-3862 | victor.engel@gs.com GS International

Lexi Kanter  
+1(212)855-9701 | alexandra.kanter@gs.com GS & Co. LLC

last week, funding high carry EM FX strategies by such low-yielders in EM or G10 can help neutralise the risk exposure and USD beta of carry currencies, and augment the overall carry proposition. But apart from the common low-yielding feature of these currencies, each of these funders comes with slightly different characteristics. From a valuation perspective, using our 60:40 ratio of GSDEER and GSFEER metrics, the Shekel is about $10\%$ overvalued, the Peso is about $15\%$ undervalued, and the Baht is about fair. The risk exposures that they neutralize are also subtly different. The ILS has one of the highest sensitivities to tech stocks, so is likely to be particularly suitable as a funder given recent volatility in tech sector equities. CLP is by far the most exposed currency to copper prices, and the broader cyclical risk betas that those mirror, so is a better hedge when broader growth concerns are more in focus. THB has a lower beta to equity risk than ILS and CLP, but is likely to be a clearer underperformer in the event that gold prices continue to slip further. Domestic considerations also point more clearly to THB and ILS weakness: in the former, structural economic challenges warrant lower rates and policymakers have welcomed currency weakness, and in the latter as well there has been a shift in policy with the Bol's decision to cut rates in May and to intervene in FX markets by buying Dollars for the first time since 2022. Taken together, within EM, THB and ILS screen as more attractive funders for carry baskets, and we continue to recommend short THB/INR as one variation of that theme.

Exhibit 1: THB, ILS, and CLP were the worst performing EM currencies versus the Dollar over the past week across the major regions  
![](images/dade5423e4bc2795b8ea99720619de92ac3e9a4c4784028af41afad3cf7fa5c3.jpg)  
Source: Bloomberg, GS Global Investment Research

GBP: Transitions and positions. We see three reasons for Sterling's steady performance following Andy Burnham's Makerfield by-election win. First and foremost, PM Starmer's resignation and Wes Streeting's announced endorsement of Burnham have meaningfully narrowed the perceived range of leadership outcomes, reducing uncertainty around the leadership transition. Second, the relationship between pricing of a Starmer government and premium in Sterling has held less

tightly after Burnham's announced commitment to the fiscal rules in mid-May. And third, a Burnham-led government was already heavily priced in prediction markets ahead of the by-election (at around 80% on Polymarket). We think all three of these factors have helped form the case for Sterling relief on a compression in premium and a reduction in short-GBP positioning. But from a fundamental perspective, we see good reason to expect this relief to be fairly tactical and narrow, with fiscal and political premium in the currency already having been fully removed under our cyclical models—after recently peaking at \~2.5% in May (Exhibit 2). Underpinning that has been a widening in EU-UK rate differentials and a risk-off dynamic so far this month, both of which have pushed in a positive direction for EUR/GBP under the surface, balancing out the compression in premium (Exhibit 3). The risks of a sustained premium-driven Sterling sell-off continue to look low to us after recent events, but there are still important challenges on the fiscal front. Our economists note risks of a slower fiscal consolidation under a Burnham government on further spending pressures and limited available tax room. And even though Burnham has announced his commitment to the fiscal rules, this does not necessarily preclude a front-loaded borrowing approach that tests the limits of the Gilt market's tolerance—which will likely move into focus again ahead of this year's Autumn budget. Meanwhile, a more positive Sterling tail that could come out of recent developments is a potential reset to closer trade ties with the EU that Burnham has advocated, which could partially reverse Brexit's long-term impact on the currency, and help offset the challenging structural valuation picture.

Exhibit 2: Under our GSBEER-based proxy, premium in Sterling has now be reduced to around zero after the recent compression  
![](images/37af9ccc8f4d00c47b02617acb15cf0f4955d9e699fbfda09bdf4293bf2deb8d.jpg)  
Source: GS Global Investment Research

Exhibit 3: Steady EUR/GBP performance reflects a balance between premium compression and a Sterling-negative shift in rate differentials  
![](images/ca09e3108d196090a60fb71582c62b82b8b26a513b40a1fbb276dcf0517a9634.jpg)  
Source: GS Global Investment Research

JPY: An even better funder. This past week saw USD/JPY trade up close to 162, its highest level since July 2024, when the MoF subsequently intervened. Many view the short-lived impact of the last intervention and the lack of official operations since then as lowering the odds of an additional round. We find that argument less compelling, since the likelihood of sustained effectiveness was already low prior to the April decision. But it does seem more likely that any operations would follow any weak US data release (e.g. payrolls, CPI) or another event that weighs notably on USD/JPY to maximize its impact. That said, even with the risk of additional intervention still elevated, the risk that markets continue to press a more hawkish

Fed leaves JPY funding relatively more attractive than before. Because as long as Fed expectations are shifting, JPY should be a lower vol funder than the other low-yielders; it tends to have a more muted response when equities and yields are moving in opposite directions. But we continue to see room for further EUR downside, and we think CAD and CHF remain attractive funders as well. Overall, a backdrop of higher US yields, low recession odds, as well as lingering domestic fiscal risks alongside only gradual BoJ hikes (which reportedly will come with even greater resistance from the administration than before, given its plan to call for the BoJ to help bolster demand) means that the upward pressure on USD/JPY should persist—as long as policymakers allow it.

MYR: Political potholes. MYR underperformed regional NJA FX peers early in June but rebounded over the past week. The initial weakness was, in our view, driven less by macro fundamentals but more by a rise in the domestic political risk premium, following the dissolution of the Johor and Negeri Sembilan state assemblies and prior remarks by Prime Minister Anwar Ibrahim that a snap election this year could be possible if the unity government fractures. Johor will go to polls on 11 July and Negeri Sembilan will vote on 1 August. State elections are distinct from federal elections and do not directly change the federal government but can have political repercussions on coalition unity depending on the results. Although oil prices have declined, unless a snap election is called (which would bring about greater uncertainty), we think MYR will continue its rebound as the underlying macro fundamentals remain positive. We expect real GDP to print a still solid $4.2\%$ yoy in 2026 (from a strong $5.2\%$ in 2025). The current account recorded a surplus of $3.0\%$ of GDP in Q1 (well above the 5-year average of $2.3\%$ ), supported by a firm goods balance and improving services balance. In Q2, high-frequency export data so far looks favorable, and Malaysia is also now benefiting from the rollout of data center-related services. Before 2025, information, communication and technology (ICT) services were a structural drag at around $-0.2\%$ of GDP; since H2 2025, they have turned positive, contributing about $0.2\%$ of GDP. As more data centers come online, services exports should become a growing pillar of current account support. We continue to like being long the Ringgit versus SGD, which is trading $1.4\%$ above the mid-point of the SGD NEER and we expect the MAS to keep policy parameters unchanged in July.

AI and the Dollar: Tech Support. Coming into the year, we argued that less exceptional US performance should lead to a weaker Dollar over time. Not only has the conflict in the Middle East disrupted expectations for more notable relative underperformance, but a surge in AI momentum has also challenged that narrative. The strength of the AI trade has driven another leg of US equity outperformance; if anything, the Dollar has appeared slightly weaker than expected from this perspective alone. We see three reasons that help explain the flatter Dollar relative to clear US equity outperformance. First, US equity outperformance is less pronounced versus EMs than DMs, and flows tend to matter more for EM FX. Second, we find evidence that durability matters: sharp upgrades to near-term US earnings expectations do not generate as much Dollar demand as more sustained earnings power would (Exhibit 4). Third, narrow equity market breadth appears to limit FX

spillovers. Together, these factors reinforce that relative equity returns can proxy broader balance-of-payments pressures that influence exchange rates. While they suggest that this year's tech sector strength may overstate the extent of US outperformance and demand for Dollar assets, the broader equity impulse has clearly shifted from an expected drag to a source of support for the Dollar (Exhibit 5).

Exhibit 4: Recent sharp upgrades to near-term US earnings expectations have not generated as much Dollar demand as more sustained earnings power would  
![](images/dfd5ce9df052f9063114baeff3c383377473f66abdd2d80f8429f44f7e6191e4.jpg)  
Levels regression of USDTWI on log (S&P 500 / MSCI World ex-US). Sample: weekly since 2000. Expected earnings growth acceleration measures the slope of consensus forward earnings growth expectations, calculated as two-year-ahead minus one-year-ahead earnings growth estimates.  
Source: Bloomberg, FactSet, GS Global Investment Research

Exhibit 5: The broader equity impulse has clearly shifted from an expected drag to a support for the Dollar  
![](images/dd57e8c7366d37ecfac32630f729708542dc597c598c92282435f7e74b60ee31.jpg)  
Source: Bloomberg, GS Global Investment Research

## Global FX Forecasts

<table><tr><td rowspan="2"></td><td rowspan="2">Current Spot</td><td colspan="2">3-Month Horizon</td><td colspan="2">6-Month Horizon</td><td colspan="2">12-Month Horizon</td></tr><tr><td>Forward</td><td>Forecast</td><td>Forward</td><td>Forecast</td><td>Forward</td><td>Forecast</td></tr><tr><td colspan="8">G10</td></tr><tr><td>EUR/$</td><td>1.14</td><td>1.14</td><td>1.14</td><td>1.15</td><td>1.18</td><td>1.16</td><td>1.20</td></tr><tr><td>£/$</td><td>1.32</td><td>1.32</td><td>1.33</td><td>1.32</td><td>1.34</td><td>1.32</td><td>1.33</td></tr><tr><td>AUD/$</td><td>0.69</td><td>0.69</td><td>0.72</td><td>0.69</td><td>0.73</td><td>0.69</td><td>0.74</td></tr><tr><td>NZD/$</td><td>0.56</td><td>0.57</td><td>0.60</td><td>0.57</td><td>0.61</td><td>0.57</td><td>0.62</td></tr><tr><td>$/CAD</td><td>1.42</td><td>1.41</td><td>1.40</td><td>1.41</td><td>1.38</td><td>1.40</td><td>1.38</td></tr><tr><td>$/CHF</td><td>0.81</td><td>0.80</td><td>0.80</td><td>0.79</td><td>0.76</td><td>0.78</td><td>0.73</td></tr><tr><td>$/NOK</td><td>9.86</td><td>9.88</td><td>9.30</td><td>9.89</td><td>8.98</td><td>9.91</td><td>8.75</td></tr><tr><td>$/SEK</td><td>9.73</td><td>9.68</td><td>9.65</td><td>9.63</td><td>9.15</td><td>9.53</td><td>8.75</td></tr><tr><td>$/JPY</td><td>162</td><td>161</td><td>160</td><td>159</td><td>158</td><td>157</td><td>155</td></tr><tr><td colspan="8">EMEA</td></tr><tr><td>$/CZK</td><td>21.3</td><td>21.3</td><td>21.5</td><td>21.3</td><td>20.7</td><td>21.2</td><td>20.2</td></tr><tr><td>$/HUF</td><td>312</td><td>313</td><td>311</td><td>313</td><td>297</td><td>314</td><td>288</td></tr><tr><td>$/PLN</td><td>3.77</td><td>3.77</td><td>3.77</td><td>3.77</td><td>3.60</td><td>3.76</td><td>3.54</td></tr><tr><td>$/RON</td><td>4.60</td><td>4.63</td><td>4.52</td><td>4.65</td><td>4.39</td><td>4.68</td><td>4.38</td></tr><tr><td>$/RUB</td><td>78.10</td><td>78.10</td><td>80.0</td><td>80.31</td><td>85.0</td><td>84.33</td><td>90.0</td></tr><tr><td>$/UAH</td><td>44.9</td><td>46.2</td><td>44.0</td><td>47.5</td><td>46.0</td><td>50.2</td><td>48.0</td></tr><tr><td>$/TRY</td><td>46.56</td><td>50.21</td><td>48.0</td><td>54.21</td><td>50.0</td><td>63.43</td><td>54.0</td></tr><tr><td>$/ILS</td><td>2.98</td><td>2.98</td><td>3.00</td><td>2.97</td><td>3.05</td><td>2.94</td><td>3.10</td></tr><tr><td>$/EGP</td><td>49.5</td><td>51.4</td><td>49.0</td><td>53.2</td><td>48.0</td><td>56.6</td><td>46.0</td></tr><tr><td>$/ZAR</td><td>16.49</td><td>16.61</td><td>16.50</td><td>16.72</td><td>16.00</td><td>16.95</td><td>15.75</td></tr><tr><td>$/NGN</td><td>1381</td><td>1431</td><td>1325</td><td>1474</td><td>1300</td><td>1555</td><td>1250</td></tr><tr><td colspan="8">Americas</td></tr><tr><td>$/ARS</td><td>1477</td><td>1558</td><td>1500</td><td>1647</td><td>1600</td><td>1847</td><td>1800</td></tr><tr><td>$/BRL</td><td>5.18</td><td>5.29</td><td>4.90</td><td>5.39</td><td>5.00</td><td>5.61</td><td>5.00</td></tr><tr><td>$/MXN</td><td>17.50</td><td>17.64</td><td>17.75</td><td>17.77</td><td>18.00</td><td>18.03</td><td>18.00</td></tr><tr><td>$/CLP</td><td>922</td><td>921</td><td>920</td><td>920</td><td>900</td><td>919</td><td>860</td></tr><tr><td>$/PEN</td><td>3.41</td><td>3.42</td><td>3.40</td><td>3.43</td><td>3.35</td><td>3.46</td><td>3.30</td></tr><tr><td>$/COP</td><td>3435</td><td>3511</td><td>3600</td><td>3589</td><td>3700</td><td>3742</td><td>3750</td></tr><tr><td colspan="8">Asia</td></tr><tr><td>$/CNY</td><td>6.80</td><td>6.76</td><td>6.80</td><td>6.71</td><td>6.70</td><td>6.62</td><td>6.50</td></tr><tr><td>$/HKD</td><td>7.84</td><td>7.82</td><td>7.80</td><td>7.80</td><td>7.80</td><td>7.77</td><td>7.80</td></tr><tr><td>$/INR</td><td>94.40</td><td>95.35</td><td>96.00</td><td>96.04</td><td>96.00</td><td>97.40</td><td>97.00</td></tr><tr><td>$/KRW</td><td>1543</td><td>1540</td><td>1460</td><td>1536</td><td>1440</td><td>1528</td><td>1420</td></tr><tr><td>$/MYR</td><td>4.12</td><td>4.11</td><td>3.90</td><td>4.09</td><td>3.80</td><td>4.07</td><td>3.70</td></tr><tr><td>$/SGD</td><td>1.30</td><td>1.29</td><td>1.28</td><td>1.28</td><td>1.25</td><td>1.26</td><td>1.24</td></tr><tr><td>$/TWD</td><td>31.8</td><td>32.0</td><td>31.5</td><td>32.1</td><td>31.0</td><td>32.2</td><td>30.5</td></tr><tr><td>$/THB</td><td>33.35</td><td>33.24</td><td>34.00</td><td>33.08</td><td>33.50</td><td>32.75</td><td>33.00</td></tr><tr><td>$/IDR</td><td>17925</td><td>18085</td><td>17000</td><td>18204</td><td>17100</td><td>18445</td><td>17200</td></tr><tr><td>$/PHP</td><td>61.31</td><td>61.43</td><td>62.00</td><td>61.60</td><td>61.00</td><td>61.92</td><td>61.00</td></tr><tr><td colspan="8">Euro Crosses</td></tr><tr><td>EUR/GBP</td><td>0.86</td><td>0.87</td><td>0.86</td><td>0.87</td><td>0.88</td><td>0.88</td><td>0.90</td></tr><tr><td>EUR/CHF</td><td>0.92</td><td>0.92</td><td>0.91</td><td>0.91</td><td>0.90</td><td>0.90</td><td>0.88</td></tr><tr><td>EUR/NOK</td><td>11.22</td><td>11.27</td><td>10.60</td><td>11.33</td><td>10.60</td><td>11.45</td><td>10.50</td></tr><tr><td>EUR/SEK</td><td>11.06</td><td>11.05</td><td>11.00</td><td>11.03</td><td>10.80</td><td>11.01</td><td>10.50</td></tr><tr><td>EUR/CZK</td><td>24.

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global

Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
