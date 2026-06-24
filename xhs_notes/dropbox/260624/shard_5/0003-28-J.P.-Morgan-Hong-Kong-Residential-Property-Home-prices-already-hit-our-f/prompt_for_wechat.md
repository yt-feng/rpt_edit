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
## Hong Kong Residential Property

## Home prices already hit our full-year target; momentum may slow in 2H

Year-to-date, the secondary home price index has rebounded 10.4% (or +17.9% from the trough), which is stronger than expected and has already reached our full-year forecast of 10-15% for 2026. While we maintain this forecast, this implies home price growth may slow to <5% in 2H26. While the two key overhangs (capital outflow control & rate hike concerns) have been well discussed, we believe the biggest downside risk is actually a prolonged weakness of the HK stock market, which has historically shown a strong correlation to HK home prices (typically with a 3-6 month lag). Fortunately, other sector fundamentals (e.g. inventory, rental growth, population) are still intact, and thus for now we forecast slower home price growth but the upcycle will still continue. However, if the Hang Seng Index stays weak for an extended period, home prices could come under pressure. In the near term, we stay defensive on our stock picks and prefer CKA & Sino, while NWD/Henderson may underperform. For SHKP, on dips we'd accumulate the stock, although its year-to-date outperformance (+21% vs. HSI -7%) leaves it vulnerable to near-term profit-taking.

\- High-frequency data is turning more mixed: While the weekly secondary home price index has remained solid (up another 1.0% over the past 4 weeks) (Figure 1), the index has a 3-week lag, and thus the impact of the recent stock market weakness & rate hike concerns has not yet been factored in. For sales volume (primary & secondary combined), May is also tracking a strong 40% Y/Y 12-month rolling growth (Figure 2). However, over the past month, some high-frequency data has shown signs of cooling down (except for weekend viewing appointments): (1) primary sell-through rates (Table 1): slowing down to 64% (from >70%), although this is partially because of developers' aggressive pricing (average 23% premium to secondary) as many now prioritize margin over velocity; (2) 35-estate secondary sales volume (Figure 3): down to <60 units for two consecutive weeks (although partially affected by adverse weather); (3) 15-estate weekend viewing appointments (Figure 4): interestingly, this leading indicator has turned even stronger in the past 3 weeks (>570, the strongest year-to-date). This shows that homebuyers' interest is still intact, but with the weaker stock market & rate hike narrative, many have shifted into a wait-and-see mode.

\- A recap of the two existing overhangs: Over the past month, the two most well-discussed overhangs have been (1) potential tightening of capital outflow controls and (2) rising expectations of a rate hike. In our view, while these two headwinds are directionally negative, they alone may not derail the upcycle if other factors remain intact. For capital outflow control from Mainland China, first of all, real estate is not explicitly mentioned in Document 837, and FX

Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC
(852) 2800-8513
karl.chan@JPM.com

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

Jocelyn Gao
(852) 2800-8529
jocelyn.gao@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev End Date</td><td></td></tr><tr><td>Sun Hung Kai Properties (0016)</td><td>16 HK</td><td>42,004</td><td>HKD</td><td>113.60</td><td>OW</td><td>n/c</td><td>140.00</td><td>Dec-26</td><td>162.00</td><td>n/c</td></tr><tr><td>CK Asset Holdings Ltd (1113)</td><td>1113 HK</td><td>19,971</td><td>HKD</td><td>44.72</td><td>OW</td><td>n/c</td><td>52.00</td><td>Dec-26</td><td>n/c</td><td>n/c</td></tr><tr><td>Henderson Land Development (0012)</td><td>12 HK</td><td>15,839</td><td>HKD</td><td>25.64</td><td>N</td><td>n/c</td><td>27.00</td><td>Dec-26</td><td>30.00</td><td>n/c</td></tr><tr><td>Sino Land (0083)</td><td>83 HK</td><td>12,978</td><td>HKD</td><td>10.61</td><td>OW</td><td>n/c</td><td>12.50</td><td>Dec-26</td><td>14.50</td><td>n/c</td></tr><tr><td>New World Development (0017)</td><td>17 HK</td><td>2,280</td><td>HKD</td><td>7.10</td><td>N</td><td>n/c</td><td>6.80</td><td>Dec-26</td><td>8.00</td><td>n/c</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 22 Jun 26.

See page 41 for analyst certification and important disclosures, including non-US analyst disclosures.

remittance to HK (including the US\$50K annual quota) for the purpose of homebuying has never been (and is unlikely to be) allowed. However, if the source of funding is offshore, Mainland Chinese are not banned from buying properties in HK. However, another concern is the potential for more stringent checks on Mainland Chinese tax residents' offshore assets (e.g. HK Property), which are taxable (20% for rental income/capital gains). We estimate 5-10% of transactions (or 10-15% by value) are from non-HK-based Mainland Chinese (more discussion in our earlier reports Takeaways from call with legal expert & Implications of Regulations on Outbound Investment). For rate hikes, first of all, JPM maintains the view of "no rate hike" in 2026, but if the US Fed Funds Rate is raised, the HK prime rate will likely follow (Figure 8), and thus mortgage rates will be higher (current mortgage rate 3.25% vs. net rental yield 2.9%, although some banks offer fixed rate of 2.73%, while banks also typically offer 0.5-1.5% cash rebates on top). However, historically a rate hike has not necessarily translated into housing market weakness (e.g. 2004-06, 16-18) if other factors are intact (more in our report What if there is a rate hike?). That said, higher rates may still weigh on developers' financing costs, and we expect NWD & Henderson to see higher earnings sensitivity (Figure 10). For more, please see our report After one overhang, here comes another one.

\- Our bigger concern is a prolonged weakness in the stock market: Instead of the above two overhangs, we are actually more concerned about a prolonged weakness in the Hang Seng Index, which has traditionally been a key leading indicator to HK home prices by a 3-6 month lag (Figure 6). From the peak in January, the HSI has dropped $15\%$ so far, and although we are not yet in a financial crisis, if the weakness continues for another 3-6 months, we believe this will still weigh on the housing market sentiment.

\- What drives home prices? Out of all key home price drivers (Figure 5), inventory has seen the strongest correlation (Figure 18), followed by the Hang Seng Index. Fortunately, inventory is currently at an optimal level, and thus is not a huge near-term concern. In the primary market, as of 1Q26 unsold inventory amounted to 16.7K units, implying 9 months of inventory (Figure 16). Meanwhile, the past 12 months saw total primary sales of 23.9K units. Even if we assume annual sales will drop 20%, the implied inventory months would be \~10.5 months (which is manageable). In the secondary market, based on for-sale listings (29.2K units) on Centraline (Figure 17), the implied inventory is only 7 months (based on 12-month rolling sales of 49K units). Even if we assume annual transactions will drop 20%, the implied inventory would still be <9 months. Other supportive factors, including population growth (Figure 18), rental growth (Figure 19) & a low vacancy rate (<5%), are also intact, at least for now.

\- How is the sector trading now? HK Property has corrected 18% from the peak in May (HSI: -9%), and is now trading at 50% NAV discount (1 s.d. below historical average - Figure 22) or 4.7% dividend yield (1 s.d. above historical average - Figure 28). Therefore, we believe the current valuations have mostly priced in the first two overhangs. However, to factor in the uncertainties, we have cut our price targets by 10% on average (Table 3). Our stock picking also has a defensive bias, and we prefer developers with net cash (or soon-to-be net cash) including CKA & Sino. We also like SHKP but the stock remains an obvious outperformer year-to-date (+21%) and might be vulnerable to near-term profit-taking. For now, we expect the potential downside for SHKP could be \~HK\$105 if NAV discount derates to 1 s.d. below mean, but we'd accumulate on dips. Names with higher leverage (NWD, Henderson) may underperform in the near term, although for NWD a near-term upside risk is the potential resolution for 11 SKIES (or more liquidity support from the parent company).

\- What might drive outperformance again? (1) Sustainable rebound of the Hang Seng Index; (2) lower expectations of a rate hike (rate pause is tolerable); (3) lower HIBOR; (4) proof of solid sales/home price momentum despite potentially fewer buyers from Mainland China; (5) stronger guidance of DP margin/rental growth in the results season (August/September).

## High-frequency data is turning more mixed

\- Secondary home price index: rebounded 17.9% from the trough, or 10.4% year-to-date (almost like a straight-line growth).

Figure 1: Hong Kong secondary home price index (and major events)  
![](images/6c219a52bcc1dc44d690989eb22222432fa3a1b3c48f891340da3699e0851624.jpg)  
Source: Centraline. Note: the index has a 3-week lag.

\- Transaction volume: Remained strong year-to-date; the latest 12-month rolling Y/Y growth is tracking 40%.

Figure 2: HK monthly private residential transactions (primary & secondary)  
![](images/6a993ab4e33ab08c0402c14cbf2994cdf3b0f544137fdbc842ced8365f7d84e2.jpg)  
Source: HK Land Registry, CEIC

\- First-day sell-through rates: Slowed down to 64% over the past month (prior: >70%), although this is partially due to developers' aggressive pricing (23% premium to secondary on average), as developers have prioritized margin over velocity.

Table 1: First-day sell-through rates of primary launches over the past month

<table><tr><td>Project</td><td></td><td>Location</td><td>Lead Developer</td><td>Launch Date</td><td>ASP (HK$ psf)</td><td>Units launched</td><td>Units sold</td><td>Sell-through</td><td>vs. previous phase</td><td>vs. secondary prices</td></tr><tr><td>Lime SPARK</td><td>形瑁</td><td>Tsuen Wan</td><td>SHKP</td><td>23-May-26</td><td>18 - 20K</td><td>87</td><td>87</td><td>100%</td><td>3%</td><td>22%</td></tr><tr><td>Highwood Ph5</td><td>壹沐2期</td><td>To Kwa Wan</td><td>Henderson</td><td>23-May-26</td><td>20 - 27K</td><td>35</td><td>29</td><td>83%</td><td>1%</td><td>26%</td></tr><tr><td>Lime SPARK</td><td>形瑁</td><td>Tsuen Wan</td><td>SHKP</td><td>30-May-26</td><td>18 - 20K</td><td>52</td><td>52</td><td>100%</td><td>3%</td><td>26%</td></tr><tr><td>Highwood Ph6</td><td>壹沐2期</td><td>To Kwa Wan</td><td>Henderson</td><td>31-May-26</td><td>22 - 27K</td><td>23</td><td>5</td><td>22%</td><td>13%</td><td>35%</td></tr><tr><td>Pavilia Rosa</td><td>激蘊</td><td>Kowloon Tong</td><td>NWD</td><td>4-Jun-26</td><td>30 - 36K</td><td>65</td><td>40</td><td>62%</td><td>-</td><td>29%</td></tr><tr><td>The Headland Residences</td><td>海德園</td><td>Chai Wan</td><td>Swire Prop</td><td>9-Jun-26</td><td>16 - 19K</td><td>78</td><td>41</td><td>53%</td><td>-1%</td><td>15%</td></tr><tr><td>Pavilia Rosa</td><td>激蘊</td><td>Kowloon Tong</td><td>NWD</td><td>12-Jun-26</td><td>30 - 36K</td><td>28</td><td>16</td><td>57%</td><td>-</td><td>29%</td></tr><tr><td>One Victoria Cove Ph4</td><td>首岸4期</td><td>Hung Hom</td><td>Henderson</td><td>14-Jun-26</td><td>20 - 23K</td><td>80</td><td>59</td><td>74%</td><td>-2%</td><td>18%</td></tr><tr><td>One Victoria Cove Ph4</td><td>首岸4期</td><td>Hung Hom</td><td>Henderson</td><td>18-Jun-26</td><td>20 - 23K</td><td>53</td><td>5</td><td>9%</td><td>-2%</td><td>18%</td></tr><tr><td>La Montagne Ph4B</td><td>海盈山4B期</td><td>Wong Chuk Hang</td><td>Kerry</td><td>18-Jun-26</td><td>28 - 32K</td><td>75</td><td>34</td><td>45%</td><td>5%</td><td>13%</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td>576</td><td>368</td><td>64%</td><td>3%</td><td>23%</td></tr></table>

Source: HKET, HKEJ, Centraline, Midland  
Note: 18 June 2026 may be partially affected by adverse weather (black rainstorm warning signal) in Hong Kong.

\- Secondary sales volume: Among 35 major estates, the weekly volume has dropped to <60 weeks over the past 2 weeks (previously 60-100 units earlier this year), partially due to adverse weather.

Figure 3: Weekly secondary transactions in 35 major estates  
![](images/856d184137efc6540acb00c6aa6f4632beec9eee8349545aa6b6da250b8d3954.jpg)  
Source: Midland

\- Weekend viewing appointments: Interestingly, this leading indicator has become mildly stronger over the past few weeks (>570 groups in 15 housing estates). This shows homebuyers' interest is intact, but more may have turned into a “wait-and-see” mode.

Figure 4: Midland weekend appointment volume (15 housing estates)  
![](images/4a904b8cdb1e9ffff489e659436b7ce76d5fbe408788836ad716b1be3b29e224.jpg)  
Source: Midland

## Home price drivers

Inventory is the strongest home price driver, followed by the Hang Seng Index. The least correlated factor is affordability.

Figure 5: Correlation with HK home prices Y/Y  
![](images/2e10aba7125fdd6929fca18e4d0560a734bff8add9e515c4d15668d0d650e74e.jpg)  
Source: Bloomberg Finance L.P., JPM, Centraline, CEIC, HKET, Mingpao, HKMA.

## Stock market

\- Hang Seng Index has shown a decent correlation to HK home prices.

Figure 6: HK Secondary Home Price Index vs. Hang Seng Index (Y/Y change)  
![](images/11abf68949d5122483a2cb75ba2b26367ec5d48cfe61f2069d47116fb8bca540.jpg)  
Source: Centraline, Bloomberg Finance L.P.

\- Typically, HK home prices show a 3-6 month lag to the HK stock market. That said, there are still exceptions where the two may not closely correlate with each other. For example, in 1999-2000, despite a big jump in the Hang Seng Index, home prices did not see a big rebound due to high inventory. In 2011, despite the stock market weakness, HK home prices only dropped very mildly.

Figure 7: HK Secondary Home Price Index vs. Hang Seng Index (absolute)  
![](images/5d0bb0df0788a83c3973623d95325a77163816c6bf164c175fd3279efd87c797.jpg)  
Source: Centraline, Bloomberg Finance L.P.

## Inventory

\- Unsold inventory amounted to 16-17K units, with an implied inventory month of 9. Typically, home prices grow when inventory is <10 months.

Figure 8: Hong Kong unsold primary private residential properties  
![](images/8241a3543b1638a0287d03794e8fff1a32e36b2d4708a77d7865392babf86edd.jpg)  
Source: HKSAR government, Centaline

\- In the secondary market, the implied inventory is 7, based on Centraline's secondary for-sale listings.

Figure 9: Centraline – No. of secondary listings (for sale)  
![](images/33f1ae44a1ec5a656a08c4429e8ffdb8aacb17b79f9be058d3e324c62cb207f2.jpg)  
Source: Similarweb, Centraline, JPM.

\- Inventory month & home prices have seen a strong correlation.

Figure 10: Secondary home price Y/Y vs inventory month  
![](images/ebdeb6624b8e5b04cac8c0d156b4dcfc460b108703b8b60ccade2f60a5dae6c8.jpg)

## Mortgage rates

## Mortgage rate vs. rental yield

\- Carry is broadly neutral (for now): The latest mortgage rate in HK is 3.25% (prime rate of 5% minus 1.75%), compared to net rental yield of 2.9% (3.2% on gross). However, if we take into account the cash rebates offered by banks (0.5-1.5%), effective mortgage rate is 2.9-3.0% for the 2-year penalty period. In addition, some banks still offer a fixed-rate plan of 2.73%.

Figure 11: HK rental yield over mortgage rate vs. secondary home price  
![](images/7b66d5a5106bc8a85e493edc458aa58a352e14dae620ee4cfed6557d7f601295.jpg)  
Source: Centraline, HSBC, HKET, JPM

# Mainland Chinese buyers in HK residential market

\- The % of non-local buyers can be gauged by the % of homebuyers who do not hold a HKID. However, the latest data is only available till FY24/25 (i.e. 2Q24 to 1Q25).

Table 2: HK private residential market – % of buyers who are not holders of a Hong Kong Identity Card (HKID)

<table><tr><td rowspan="2"></td><td colspan="4">Individual buyers who are not HKID holders</td></tr><tr><td colspan="2">Volume(units) as % of total</td><td colspan="2">Value(HK$ bn) as % of total</td></tr><tr><td>FY20/21</td><td>110</td><td>0.1%</td><td>1.1</td><td>0.2%</td></tr><tr><td>FY21/22</td><td>153</td><td>0.2%</td><td>1.6</td><td>0.2%</td></tr><tr><td>FY22/23</td><td>168</td><td>0.3%</td><td>1.6</td><td>0.4%</td></tr><tr><td>FY23/24</td><td>700</td><td>1.6%</td><td>6.8</td><td>2.0%</td></tr><tr><td>FY24/25</td><td>2,997</td><td>5.5%</td><td>31.3</td><td>7.2%</td></tr></table>

Source: HK Inland Revenue Department  
Note: FY denotes HK government's fiscal year (year ending 31 March). For example, FY24/25 refers to the period from 2Q24 to 1Q25.

\- The % of “Mainland Chinese buyers” widely quoted by property agents is based on homebuyers’ last name with Mandarin pinyin. However, this includes many who currently reside in Hong Kong, as well as a small number of Hong Kong locals who keep a Mandarin last name.

Figure 12: HK private residential market – % of “Mainland Chinese” buyers with a last name in Mandarin pinyin (by volume)  
![](images/02607677656113400342c4c5bf4272aee88c3d97ba2e394e23c0b6b902b264d3.jpg)  
Source: Centraline.  
Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

Figure 13: HK private residential market – % of “Mainland Chinese” buyers with a last name in Mandarin pinyin (by value)  
![](images/1ef1fd297505d30b842062912bfeef0a8468463c099e8f9cce7abf2b6539d1e9.jpg)  
Source: Centraline.  
Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

## Interest rate

\- If a US Fed rate hike leads to higher HIBOR, NWD & Henderson will likely be more impacted in terms of earnings sensitivity.

\- Meanwhile, Sino & CKA will likely be least impacted.

## Interest rate sensitivity

Figure 14: Earnings impact of every 1

[中间内容因长度限制已省略]

aterial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
