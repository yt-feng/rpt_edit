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
- 已识别机构名：`DB`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份DB研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Commodities Precious Special Report

## Hawks drive out bulls

\- Fed repricing together with resilient US macro data has played the primary role in pushing gold lower. This new 'problem' became evident once gold began diverging from oil last month. Our revised base case is for gold to reach USD 4,800/oz in Q4, consistent with an indefinite Fed hold, while a risk case of pricing 3-4 Fed hikes may bring gold to USD 3,800/oz.

\- The first FOMC meeting with Chair Warsh revealed no resistance to market pricing for hikes. The FOMC press conference underlined potential for a further hawkish shift, supported by a Taylor rule prescription some 80 bps higher. On the dovish side, our house call remains for an indefinite hold near neutral, market-based measures of inflation expectations are declining with oil, and the SEP dot plot median showed only one hike followed by a reversal next year compared with 48 bps priced by the market through Mar'27.

\- The usual suspects which might provide support via investment demand are notably absent, for now. The dip in gold after the May NFP report was met by continued ETF selling, while futures open interest sits at a 17-year low, and futures net long positioning nearer the year's low than high.

\- The China premium over Comex has reversed to a small discount, suggesting that China gold imports will not be a support for the market. The rationale could be that Chinese investors have less reason to diversify into gold as CNY remains on a strengthening trend, while evidence also points to a possible property market bottoming. For India, the recent hike of gold import VAT is likely to suppress demand.

\- The one pillar which remains strong is central bank demand, and we expect this to be the case for some time to come as EM central banks catch up to DM central banks in gold holdings. However, official demand also has not accelerated as of Q1, so it will not compensate for otherwise slower investment demand on its own.

\- All of the above suggests a neutral outlook for gold into H2, with Fed data dependency implying gold data dependency. We think structural positives remain in the form of central bank demand sustaining its higher post-2022 pace, and expansion of US federal debt outstanding at an 8% pace, above the CBO's long-term expectation of 6% growth.

## Recalibrating precious forecasts

We recognise a lower forecast profile for the precious metals around which we think are risks are balanced. The challenge to gold (Link) was first most clearly linked to the energy price shock of the US-Iran war, but this relationship broke down around mid-May (Figure 2). Subsequently, gold's link to Fed pricing was more persistent and gained the upper hand over lower oil prices (Figure 3), embedding in gold the risk that inflation remaining above target would necessitate tighter monetary policy (Link).

Figure 1: Precious metal forecasts

<table><tr><td>USD/oz</td><td>2024</td><td>2025</td><td>Q1 26</td><td>Q2 26</td><td>Q3 26</td><td>Q4 26</td><td>2026</td><td>2027</td></tr><tr><td>Gold</td><td>2,387</td><td>3,440</td><td>4,873</td><td>4,550</td><td>4,300</td><td>4,800</td><td>4,631</td><td>5,300</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td>-10.8%</td><td>-21.8%</td><td>-17.2%</td><td>-12.9%</td><td>-11.7%</td></tr><tr><td>Silver</td><td>28.2</td><td>40.1</td><td>83.9</td><td>74.5</td><td>65.0</td><td>73.0</td><td>74.1</td><td>80.5</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td>-8.0%</td><td>-21.7%</td><td>-17.0%</td><td>-11.8%</td><td>-10.6%</td></tr><tr><td>Platinum</td><td>956</td><td>1,283</td><td>2,204</td><td>1,950</td><td>1,720</td><td>1,920</td><td>1,949</td><td>2,120</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td>-8.5%</td><td>-25.2%</td><td>-16.5%</td><td>-12.8%</td><td>-11.7%</td></tr><tr><td>Palladium</td><td>983</td><td>1,151</td><td>1,706</td><td>1,400</td><td>1,300</td><td>1,450</td><td>1,464</td><td>1,535</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td>-12.5%</td><td>-18.8%</td><td>-9.4%</td><td>-10.0%</td><td>-9.7%</td></tr></table>

Source: DB; Figures are period averages

Figure 2: Gold negatively linked to oil in March & April  
![](images/64da19954872de7eb74865ae67117c52e80cc9c65848e393aa1c094d8cfd2721.jpg)

Figure 3: Gold linkage to Fed pricing more influential after May  
![](images/e540f71061e0e9d283c2551ca51720ab4309bb32a12291020fbb11bfa2574e40.jpg)

Although the sources of inflation are quite broad-based (Link) and there are numerous reasons to doubt the disinflation narrative (Link), it is also true that market-based measures of inflation expectations are declining after the US-Iran memorandum of understanding and the beginning of higher rates of Gulf oil exports.

## Policy risk scenarios

The two-sided risks from a lower Q2 starting point of precious metal prices are framed by monetary policy, which has dominated gold's move lower towards USD 4,000/oz. The Fed Chair's emphasis on data dependence and elimination of forward guidance means gold is also likely to be data dependent.

The hawkish risk is contained in the June FOMC meeting's confirmation of the tightening bias. Fed Chair Warsh stated that "we have missed [our inflation target] for five years, and we are going to fix that." Our US Econ team explains the hawkish risk is best illustrated by the fact that around mid-2025, Fed policy was near standard policy rules, so that late 2025 Fed cuts (characterized as "insurance or risk management cuts") moved policy below those rules, just as Core PCE began to move higher (Link). The Taylor rule prescription using Bloomberg consensus year-end forecasts for Core PCE (3.1%) and unemployment (4.4%), and the Fed's SEP median estimates of the neutral real rate (1.1%) and NAIRU (4.2%) would imply a policy setting 80 bps above the Fed's current upper bound (4.55%). Across three standard policy rules, our US Econ team quantified the policy upside risk between 30-75 bps, before accounting for any change in the neutral rate estimate (Link).

On the dovish risk, with the Fed's elimination of forward guidance and heightened data dependency, the appearance of disinflationary data could well reduce the market's Fed pricing from the current peak of +44 bps for March 2027. Our house view remains of a Fed on indefinite hold near neutral (Link), although June FOMC "crystallised risks for rate hikes" (Link). The US-Iran memorandum of understanding, increase in shipping flows through the Strait of Hormuz, steep drop in oil prices, inflation swaps and TIPS breakevens all point to reasons why the Fed should be marginally less inclined to hike (Figure 4). If extended, this may form an important part of the data landscape that the FOMC consider at the July meeting. Supporting that line of thought, our team published an optimistic dbDataInsights survey indicating that the inflation shock may have peaked (Link), and year-end Bloomberg consensus forecasts for Core PCE are at 3.1% versus the most recent 3.3%.

![](images/7517a2d439037998a5e4ac4c03b60b78111aa6c3c59c841908a3d6c269b9d791.jpg)  
Source: Bloomberg Finance LP, DB

Figure 5: US FCI index eased since March  
![](images/25109aa8d6fa0953c58529acc51260dcd66ac319505eb1d972ae671a9b4aa0a5.jpg)  
Source: Bloomberg Finance LP, DB

Last but not least, Fed Chair Warsh was equivocal on the nature of the current policy setting. Chair Warsh indicated that "Broadly I would say there Fed policy appears to be somewhat restrictive" $^{2}$ in the context of the housing market, but less so when viewed in the context of financial markets ("And the best way I can describe is it's uneven") $^{3}$ . For what it's worth, Bloomberg's FCI index shows a marked loosening since March (Figure 5). We think the conclusion is that Chair Warsh does not express an obvious inclination to adopt a higher estimate of real neutral as estimated by our US Econ at 1.6% versus 1.1% according to the Fed's SEP longer-run median.

![](images/f919d2cb0f7c2e4a0b890909c4090fc687f6b05608fb085c859b41fddc2ad0f0.jpg)

<table><tr><td colspan="3">Figure 6: Fed Jun&#x27;27 pricing to gold regression tighter since March (R2=0.80) than since December (R2=0.28)</td></tr><tr><td></td><td>Gold Dec&#x27;26 futures</td><td>Gold Jun&#x27;27 futures</td></tr><tr><td colspan="3">Current Price Targeted at Current FCF is 4,350 and Current FCF is 4,450; Current FCF is 3.63% and Current FCF is 4,900; Prices as of 22-Jun are 4,274 and 4,374.</td></tr></table>

Source: Bloomberg Finance LP, DB

## Recent tightening examples

If market pricing of Fed policy remains the only variable, then our revised year-end forecast of USD 4,800/oz lies toward the dovish end of the spectrum (Figure 7). However, the history of the gold market is one that reflects a constant shifting of drivers, and the 2022-23 example is worth recalling. Well before the last hike of the cycle was realized in July 2023, gold had diverged from a formerly tight relationship with Fed rates pricing around November 2022 (Figure 8). As a counterexample, gold did not meaningfully diverge from 10y TIPS after the Fed QE tapering shock of 2013, Figure 9.

Figure 8: Gold and Fed hiking cycle over 2022-23  
![](images/50a8b772d4dd42f49d5561a247231640106f8c31d3d9f59a18abf7491c44bd61.jpg)

![](images/27e3d91de3d202366dcf235d1cc586297ace1be2b7202964c5f2026d389ec7e7.jpg)

## Short-term flow factors appear weak

We look at three components of short-term flow which are not encouraging at this moment in time. First, ETF assets across US, Europe, China, Japan and India have reached a new low for the year. Since 11-Jun, ETF investors have been sellers into the rise in gold prices, Figure 10, with the exception of last Friday 19-Jun which marked the strongest day of gold ETF accumulation since 17-Apr. This is certainly worth watching as a possible turning point. At the same time, futures open interest for gold stands at a 17-year low, and futures net long positioning is closer to the low of the year than the high. For the time being, it does not appear that either ETF flows or futures investment (measured in contracts) are poised to return to Q1 highs.

As an aside, we observe that gold price changes are associated with ever-smaller volumes of ETF investment or redemption, Figure 11. This is a further progression from the stable sensitivity viewed over the 2003-2022 period, when it could be estimated that 1 mm troy oz of investment or disinvestment could drive a gold price change of 1%. Over the Jan-Sep'25 period, that sensitivity appears to have risen to 1.8% (using the midpoint of the gold price range), and to as much as 2.9% in the Oct'25-current period. The roughly unchanged size of the gold market in annual ounces would suggest that this may be the result of similarly timed but unobserved investment flows in less transparent venues like the OTC market. The recent sensitivity would also imply that to attain a gold price of USD 4,800/oz,

Source: Bloomberg Finance LP, DB

ETF year-to-date inflow would have to rise to 5 mm troy oz, just above the year-to-date high.

Figure 10: ETF investment nearly zero year to date; would need to rise to 5 mm troy oz to imply gold at USD 4,800/oz

![](images/3da7df6b1e68376aba59625c23a76c1ba81715ce823ce74f15375d35fd0dd764.jpg)

Figure 11: Gold progressively responding more steeply to any given ETF volume change  
![](images/9d01010acc4c250727039094ebce2535ac8bcc87576f6f3275c288841b42b6ed.jpg)  
Source: Bloomberg Finance LP, DB

Second, China and India gold import demand has been holding up well and even rising since January, but forward signals are negative. The China SGE differential to Comex has just recently turned to a discount after a long period of premiums (Figure 13). Since there is a positive relationship between SGE differential and China import demand (Figure 14), the latter can no longer be considered as a support for the market. Today's climate of CNY strength means there is no reason for authorities to withhold gold import quotas. But this also means that onshore investors have less reason to protect assets by diversification into gold. By the same token, our China economist sees the possibility of a China property bottom (Link) which works against the need for gold as an investment alternative. We also note the China central government has "moved to close informal channels between Chinese households and global capital markets". For now there is no indication of any official stance on gold being regarded as either 'patriotic' or 'unpatriotic', but we should be watchful for any potential signals should they be forthcoming.

Third, the India rise in VAT on gold imports means that Indian demand may also be hampered for now, as the government has sought to limit demand for foreign currency. The initial signal was contained in Prime Minister Modi's 10-May speech urging citizens to stop buying gold for a year. $^{5}$ The policy moves followed with the rise in VAT announced on 13-May, and then on 14-May, a tightening of the rules for gold imported under tax-exempt status. Though Indian import demand was already on the lower end of the range in April at 1.2 mm troy oz, there is still room to fall and that may come alongside weaker China import demand.

A possible silver lining for demand is that India has reported grey market discounts of as much as USD 200/oz. This suggests illegal imports may rise as a result. $^{6}$ The discount is nearly 5% of the gold price on 9-Jun when the news was reported, making for a significant share of the import duty that has risen from 6% to 15%. The relationship between duties and illegal imports is underlined by the fact that the July 2024 reduction in gold VAT was intended partly as an effort to constrain smuggling activity. $^{7}$

![](images/0696ec2672981299b83ac008f62ee383898b05f5d670f958c861213ab6c05150.jpg)  
Source: Bloomberg Finance LP, DB

![](images/a3ed927b38221036a9ed1f257265eca719f3328f84b8bcf5b9f046ddae162bf6.jpg)  
Source: Bloomberg Finance LP, DB

Figure 14: China discount or smaller premium is associated with lower gold imports  
![](images/dbc00ae416bbd8f20fa9c0a20879e42013328fc2842fd44588012d48067c374c.jpg)  
Source: Bloomberg Finance LP, DB

## Longer-term gold drivers

The inflation and monetary policy frame of reference lowers the starting point for our forecasts, but the longer-term trajectory is likely to remain positive. First, we see the structural gold-positive factor of both US and global debt growth unchanged, and this remains a reason to expect gold to rise in real terms. The current annual pace of US public debt growth of 8% is running above CBO long term projections of 6%. Given that our model assumes a roughly one-to-one impact on gold prices (Link), we think these figures are likely to support gold appreciation over 2026 and 2027 that is steeper than the 4.6% slope in the gold futures curve (Aug'27 vs Aug'26).

Figure 15: Long-term gold model sees debt growth as structurally positive driver  
![](images/22fa50c4c3cbeab7b25feac599df2d6316c187522f4bd4acbb2b9b8c91158cfc.jpg)  
Source: Bloomberg Finance LP, DB  
Figure 16: US public debt growth faster than CBO projection

![](images/69cf0f7f6d4be6982d3d38102ec877920001d53cef3eab760c6698794be3b529.jpg)  
Source: Bloomberg Finance LP, DB

Second, the higher pace of central bank demand since 2022 may also be structural in nature; it is a form of demand that we see as elastic and driving the price of gold, Figure 21. We think that central bank accumulation has been a key factor explaining recent gold outperformance versus model (Link). Plus, EM central banks likely have further room to go in building up gold reserves, as they still hold only half the gold held by DM central banks (Link). Short-term data suggest this trend is continuing. In fact, in recent quarters the unreported component of official demand has been higher than we expected from measuring China “other investment demand”, calculated as China gold supply (production and imports) from which we subtract known categories of demand (Link), Figure 17. The longer-term relationship remains reasonable, Figure 18.

According to both Q1 estimated data and the World Gold Council's 2026 survey, reserve managers have a similarly strong inclination to add to gold reserves as they did last year. In USD real terms, gold purchases rose to a new record high of USD 38.9bn in the first quarter (Figure 19). The OMFIF reserve manager survey will be released at the end of June which we expect to broadly confirm the WGC results. The fact that jewellery demand also shrank in the first quarter, is consistent with the narrative of inelastic demand outcompeting elastic demand for the roughly fixed volume of gold supply (Link). In fact, gold jewellery demand in Q1 was at the lowest since the pandemic (Q2'20), Figure 20. On a notional $10\%$ move in gold, we would expect jewellery demand and increased recycled supply to compensate for an increase in ETF and official demand, Figure 21. The moderate ETF selling in Q2 along with a lower gold price suggests jewellery demand may now have room to re-expand slightly from the very low point in Q1.

## Outlining the picture for H2

All in all, we think gold's repricing is a function of expectations of tighter monetary policy. While there are two-sided risks to this, a Fed tightening cycle would seem to have limited room to run, certainly in comparison with the 2022-23 tightening cycle. The hawkish risk case is that data pointing to 80 bps of tightening may result in gold pricing around USD 3,800/oz. On the dovish side, a continuation of weaker oil prices and lower breakevens may help to support the argument for a hold at the July FOMC, and reduce some of the tightening currently priced. Should Core PCE disinflation follow DB and consensus forecasts, this would also be more supportive of gold towards USD 4,800/oz. In the short term, investment flows appear discouraging while central bank demand remains the most supportive pillar.

Figure 17: Unreported official demand higher than expected in Q1

![](images/88324022736b38b33b20f72851d213a3d651d566ecb9cad101bbc66abc2cdb85.jpg)  
Source: World Gold Council, Bloomberg Finance LP, DB

Figure 18: Relationship between unreported official demand and China still reasonably strong  
![](images/8c249a4204d7d7feda2419f394b20e58f72f689fc9c1eed0b5e253ef346c613c.jpg)  
Source: World Gold Council, Bloomberg Finance LP, DB

Figure 19: Q1

[中间内容因长度限制已省略]

r confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau
Group Chief Economist and Global Head of Research

<table><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Japan</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td>Tel: (852) 2203 8888</td><td>Tel: (81) 3 6730 1000</td></tr></table>

DB AG
21 Moorfields
London EC2Y 9DB
United Kingdom
Tel: (44) 20 7545 8000

DB Securities Inc.

The DB Center
1 Columbus Circle
New York, NY 10019
Tel: (1) 212 250 2500

DB AG
Filiale Singapur
One Raffles Quay, South Tower
Singapore 048583
Tel: (65) 6423 8001
"""
