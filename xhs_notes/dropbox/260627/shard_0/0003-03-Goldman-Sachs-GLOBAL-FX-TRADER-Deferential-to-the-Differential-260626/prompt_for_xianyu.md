你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

<table><tr><td rowspan="2"></td><td rowspan="2">Current Spot</td><td colspan="2">3-Month Horizon</td><td colspan="2">6-Month Horizon</td><td colspan="2">12-Month Horizon</td></tr><tr><td>Forward</td><td>Forecast</td><td>Forward</td><td>Forecast</td><td>Forward</td><td>Forecast</td></tr><tr><td colspan="8">G10</td></tr><tr><td>EUR/$</td><td>1.14</td><td>1.14</td><td>1.14</td><td>1.15</td><td>1.18</td><td>1.16</td><td>1.20</td></tr><tr><td>£/$</td><td>1.32</td><td>1.32</td><td>1.33</td><td>1.32</td><td>1.34</td><td>1.32</td><td>1.33</td></tr><tr><td>AUD/$</td><td>0.69</td><td>0.69</td><td>0.72</td><td>0.69</td><td>0.73</td><td>0.69</td><td>0.74</td></tr><tr><td>NZD/$</td><td>0.56</td><td>0.57</td><td>0.60</td><td>0.57</td><td>0.61</td><td>0.57</td><td>0.62</td></tr><tr><td>$/CAD</td><td>1.42</td><td>1.41</td><td>1.40</td><td>1.41</td><td>1.38</td><td>1.40</td><td>1.38</td></tr><tr><td>$/CHF</td><td>0.81</td><td>0.80</td><td>0.80</td><td>0.79</td><td>0.76</td><td>0.78</td><td>0.73</td></tr><tr><td>$/NOK</td><td>9.86</td><td>9.88</td><td>9.30</td><td>9.89</td><td>8.98</td><td>9.91</td><td>8.75</td></tr><tr><td>$/SEK</td><td>9.73</td><td>9.68</td><td>9.65</td><td>9.63</td><td>9.15</td><td>9.53</td><td>8.75</td></tr><tr><td>$/JPY</td><td>162</td><td>161</td><td>160</td><td>159</td><td>158</td><td>157</td><td>155</td></tr><tr><td colspan="8">EMEA</td></tr><tr><td>$/CZK</td><td>21.3</td><td>21.3</td><td>21.5</td><td>21.3</td><td>20.7</td><td>21.2</td><td>20.2</td></tr><tr><td>$/HUF</td><td>312</td><td>313</td><td>311</td><td>313</td><td>297</td><td>314</td><td>288</td></tr><tr><td>$/PLN</td><td>3.77</td><td>3.77</td><td>3.77</td><td>3.77</td><td>3.60</td><td>3.76</td><td>3.54</td></tr><tr><td>$/RON</td><td>4.60</td><td>4.63</td><td>4.52</td><td>4.65</td><td>4.39</td><td>4.68</td><td>4.38</td></tr><tr><td>$/RUB</td><td>78.10</td><td>78.10</td><td>80.0</td><td>80.31</td><td>85.0</td><td>84.33</td><td>90.0</td></tr><tr><td>$/UAH</td><td>44.9</td><td>46.2</td><td>44.0</td><td>47.5</td><td>46.0</td><td>50.2</td><td>48.0</td></tr><tr><td>$/TRY</td><td>46.56</td><td>50.21</td><td>48.0</td><td>54.21</td><td>50.0</td><td>63.43</td><td>54.0</td></tr><tr><td>$/ILS</td><td>2.98</td><td>2.98</td><td>3.00</td><td>2.97</td><td>3.05</td><td>2.94</td><td>3.10</td></tr><tr><td>$/EGP</td><td>49.5</td><td>51.4</td><td>49.0</td><td>53.2</td><td>48.0</td>

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
