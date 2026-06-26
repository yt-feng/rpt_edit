你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
Rates Strategy

# A global bond glut

A shift from a global savings glut to a bond glut points to structurally higher long-term yields, reflecting persistent fiscal deficits alongside a price-sensitive buyer base. Incremental measures such as shortening issuance may slow the adjustment, but are unlikely to prove sustainably effective.

\- Long-end yields across developed markets have repriced to multi-decade highs, but the driver is not a return to past rate expectations: despite similar outright levels, current yields reflect a much larger role for term premia, rather than the expected path of short rates, pointing to a structural shift in how duration risk is priced (Figure 1).

\- Budget deficits remain elevated across major economies, but the causes differ across regions: in the US through an erosion of convenience yield, in Europe due to vulnerability to fiscal stress re-emerging under weaker macro conditions, in the UK because of heightened sensitivity to fiscal narratives, and in Japan via fiscal expansion feeding into inflation risk premia.

\- A common thread across markets is that the buyer base has become more price sensitive: Reduced central bank and official sector support have weakened inelastic demand for duration, while a growing reliance on private investors and a diminished perception of bonds as reliable diversifiers mean that sovereign curves now need to clear at higher term premia.

\- Supply-side adjustments are helping at the margin, but not changing the direction of travel: Whether through the Treasury's bill skew, lower WAM issuance in Europe, active remit adjustments in the UK, or super-long issuance cuts in Japan, issuance management can slow the pace of cheapening, but has not been enough to generate a durable rally at the long end (Figure 2).

\- Absent a true macro regime shift, long-end rallies are likely to be temporary: A sustained rally would likely require a material growth shock, a decisive return to policy easing or balance-sheet support, or a meaningful restoration of fiscal credibility; otherwise, the bias remains toward structurally higher long-end yields.

SIGNATURE

## Anshul Pradhan

+1 212 412 3681
anshul.pradhan@BARC.com
BCI, US

## Rohan Khanna

+44 (0) 20 7773 0533
rohan.khanna1@BARC.com
BARC, UK

Moyeen Islam
+44 (0) 20 7773 4675
moyeen.islam@BARC.com
BARC, UK

Shinichiro Kadota
+81 3 4530 1374
shinichiro.kadota2@BARC.com
BSJL, Japan

Demi Hu, CFA
+1 212 526 7398
demi.hu@BARC.com
BCI, US

Andres Mok, CFA
+1 212 526 8690
andres.mok@BARC.com
BCI, US

Max Kitson
+44 (0) 20 3134 1456
max.kitson@BARC.com
BARC, UK

Ayao Ehara
+ 81 3 4530 1379
ayao.ehara@BARC.com
BSJL, Japan

FIGURE 1. The weighted average G7 30y yield is approaching 5%, well above the pre-GFC average of about 4%  
![](images/bcfd06086d4a0abe62c3281ad7a15db0f63ad37a07664e4c2e96d1cc44e886cd.jpg)  
Source: Bloomberg, BARC

FIGURE 2. Despite attempts to shorten issuance WAM by DMOs, markets would still have to absorb meaningful duration supply next year

<table><tr><td colspan="5">Gross issuance</td></tr><tr><td>USD bn</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>USTs</td><td>4,311</td><td>4,390</td><td>4,395</td><td>4,564</td></tr><tr><td>EGBs</td><td>1,466</td><td>1,591</td><td>1,754</td><td>1,741</td></tr><tr><td>JGBs</td><td>1,145</td><td>1,151</td><td>1,067</td><td>1,091</td></tr><tr><td>Gilts</td><td>358</td><td>435</td><td>310</td><td>335</td></tr><tr><td>Total</td><td>7,280</td><td>7,567</td><td>7,526</td><td>7,731</td></tr></table>

Source: BARC

<table><tr><td></td><td colspan="4">Gross issuance, 10y WAM equivalent basis</td></tr><tr><td>USD bn</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>USTs</td><td>3,048</td><td>3,091</td><td>3,094</td><td>3,172</td></tr><tr><td>EGBs</td><td>1,525</td><td>1,591</td><td>1,666</td><td>1,654</td></tr><tr><td>JGBs</td><td>973</td><td>932</td><td>747</td><td>763</td></tr><tr><td>Gilts</td><td>437</td><td>422</td><td>263</td><td>275</td></tr><tr><td>Total</td><td>5,982</td><td>6,036</td><td>5,770</td><td>5,865</td></tr></table>

## US: Returning to the old normal

\- Long-end yields have reverted to pre-GFC levels, but their composition has fundamentally shifted: Expected real returns on cash are significantly lower, with term premia – both rate and fiscal – playing a larger role, particularly the latter. The inflation risk premium is very well contained for now, but eroding insurance value is increasing the compensation private investors are demanding to absorb duration.

\- Scope remains for further repricing through neutral rates and fiscal premia: Investment-driven demand is likely to push estimates of r\* higher versus the consensus, which remains too anchored to the post GFC–pre COVID era. There is room for the deficit outlook to worsen, rate volatility to rise and a shortening of the Fed's balance sheet to add to the term premium.

## 30y yields back near 5%: Same level, different story

30y yields have moved back near 5%, briefly revisiting levels last reached in 2007 and drawing renewed market attention. The 5% threshold remains much watched, with evidence of demand from investors seeking to lock in long-duration yields at attractive levels. Here, we place current levels in a historical context and decompose 30y yields into their key drivers to assess the path.

Long-end yields can be decomposed into the expected path of short rates (ie, the expected return from holding T-bills) and the term premium required to bear duration risk. Both components can further be split into real and inflation elements. An alternative lens is to decompose term premia into rate-driven factors, capturing compensation embedded in swap rates relative to expected short rates, and fiscal-specific factors, reflected in the asset swap spread between Treasury yields and swap rates.

Figures 3 to 5 present this decomposition over time and across key snapshots. Several points stand out:

A significantly lower expectations component: While 30y yields are back near 2007 levels, the expectations component (based on surveys) is materially lower. Current estimates point to \~3.1% nominal, versus \~4.4% in 2007, 130-140bp lower. While surveys may be lagging and understating true market expectations, the magnitude of the gap suggests this is not purely a measurement issue.

The rate term premium has normalized higher: The rate-driven term premium (30y swap rate minus the above expected rate) is now well above pre-COVID levels and also somewhat above pre-GFC norms, indicating investors are being compensated for taking duration risk. 30y swap rates currently trade at \~110bp over the survey based expectations component, in between the \~90bp average in the 2000s and the mid-1990s levels of 120bp.

Inflation compensation is well anchored: Long-term inflation expectations and risk premium have been well anchored and are not the reason 30y yields have risen from the lows. Most forecasters continue to have faith in the Fed's inflation-fighting credibility and expect core PCE inflation to be near 2%. In addition, 5y5y CPI swaps have been trading in a tight range near 2.4%, also pointing to very little inflation risk premium, recently reflecting the Fed's singular focus on price stability.

Fiscal premium is clearly visible in asset swap spreads: Perhaps the most striking shift is in asset swap spreads. 30y Treasuries trade at +70bp to swaps, markedly cheaper than the -70bp in 2000 and -20bp in the mid 1990s (both converted into SOFR equivalents). This suggests that investors are already demanding meaningful compensation for the deteriorating fiscal profile.

Bottom line: 30y yields of about 4.9% embed an expected short rate of 3.1%, a rate term premium of 1.1% and a fiscal risk premium of 0.7%. Although 30y yields are back near 2007 levels, the underlying composition is fundamentally different. Expected real returns on cash are significantly lower and term premia are playing a larger role.

FIGURE 3. Although 30y yields are back near 2007 levels, the underlying composition is fundamentally different; expected real returns on cash are significantly lower and term premia are playing a larger role

<table><tr><td></td><td colspan="4">30y Expectations component</td><td colspan="2">Rate Term premium</td><td>Fiscal Risk Premium</td></tr><tr><td>%</td><td>30y UST</td><td>Real Short Rate</td><td>Expected Inflation</td><td>Nominal Short Rate</td><td>30y swap rate</td><td>30y Swap Rate minus Expected Rate</td><td>30y USTs minus Swap Rate</td></tr><tr><td>Dec-95</td><td>5.95</td><td>2.30</td><td>2.70</td><td>5.00</td><td>6.16</td><td>1.16</td><td>-0.21</td></tr><tr><td>Dec-00</td><td>5.46</td><td>3.00</td><td>2.20</td><td>5.20</td><td>6.17</td><td>0.96</td><td>-0.71</td></tr><tr><td>Jun-07</td><td>5.02</td><td>2.52</td><td>2.03</td><td>4.55</td><td>5.49</td><td>0.93</td><td>-0.46</td></tr><tr><td>Dec-19</td><td>2.39</td><td>0.46</td><td>1.79</td><td>2.25</td><td>1.79</td><td>-0.46</td><td>0.60</td></tr><tr><td>Jun-26</td><td>4.93</td><td>1.10</td><td>2.03</td><td>3.13</td><td>4.21</td><td>1.08</td><td>0.71</td></tr></table>

Using surveys to estimate the expected path of nominal and real short rates and inflation. Libor-based swap rates have been adjusted lower in the historical data. Source: Federal Reserve, Haver Analytics, BARC

FIGURE 4. The expectations components in 30y yields  
![](images/ad9c5064cb64d362e09f0ccf608f8bb6b6ae8102c4c2bbaf0736898cd9f1435a.jpg)  
Source: Federal Reserve, Haver Analytics, BARC

FIGURE 5. 30y term premium, broken into rates and fiscal  
![](images/dbb761a28baa3cebcf4d706369a2994068489dd89e72ee3795f7858371107aff.jpg)  
Source: Federal Reserve, Haver Analytics, BARC

## Where to from here?

We see two potential drivers of higher 30y yields: a reassessment of the nominal neutral rate and somewhat greater fiscal risk premium. Whether the rate term premium moves higher depends on the Fed's communication and its balance sheet policy.

## Room for neutral rate estimates to move higher

Recent economic data point to a robust growth backdrop, resilience in the labor market and a further pickup in core inflation. US economy has likely grown about 2.5% in the first half of the year. Job gains have picked up, averaging 114k/month YTD, versus 30k during the same time last year, and the unemployment rate has moved lower. Core PCE inflation has risen to 3.4% y/y in May from 3% at the beginning of the year (Figure 6). All of this calls into question whether the nominal neutral rate is below the overnight rate, let alone around the consensus forecast of 3.1%.

From a first principal perspective, the saving-investment imbalance is shifting to excess investment, which points to a higher neutral rate for a given estimate of trend growth. Figure 7 shows that hyperscaler investments have risen to about 2.2% of GDP in 2026, with an expectation of \$1trn, or 3% of GDP, by 2028. Meanwhile, the personal savings rate has fallen dramatically, to about 2.5%, due to growing household net worth (Figure 8). These trends also point to a rising neutral rate.

In Figure 9, we tabulate estimates of the nominal neutral rate across major models. The average is about 3.5%, with the higher end nearing 4%. The lower end, which includes the Fed's long-run dot, is likely lagging the economic performance, and we expect model estimates to drift higher.

All of the above suggests that the market should be discounting a nominal neutral rate near 3.5%, with the risk of skewing towards 4%, rather than 3%. All else equal, this should push long-term yields even higher.

FIGURE 6. The unemployment rate has fallen and core inflation has risen in recent months  
![](images/acfdd7bed37c5377cd06996a88acd322a1e036cc9ba39dedfc362df149b7f4fc.jpg)  
Source: Haver Analytics, BARC

FIGURE 7. Hyperscaler investments are expected to rise to about 3% GDP  
![](images/885e7811fd042c759de3da6a5a4c464333715f4736f0f6019dc69eafec3c28df.jpg)  
Source: BARC

FIGURE 8. The household saving rate has moved sharply lower  
![](images/34c5da8b5eada65d28625dff442a9367765a227522d30737327aa8ca79f55466.jpg)  
Source: Haver Analytics, BARC

FIGURE 9. Model-based estimates of the nominal neutral rate are above the consensus  
![](images/d300af2eb4c4927200738d73ad4f9b00004c53cbd85689fe733299a5bb307b52.jpg)  
Source: Haver Analytics, BARC

## Room for fiscal risk premium to move somewhat higher

Figure 10 shows that 30y swap spreads are quite sensitive to the budget deficit outlook. In the mid-1990s, the government was expected to run a large budget surplus; as a result, swap spreads were quite wide. However, as the outlook moved towards persistent deficit, they have turned negative. A 1pp increase in average deficit pushes up 30y Treasury yields relative to swap rates about 15bp, in our view (Figure 11).

We estimate that the markets are discounting an average 10y budget deficit of 6-6.5% GDP. This looks broadly in line with the CBO's latest forecast of 6.1% GDP and a debt/GDP ratio of 120% by 2036. However, the CBO's assumptions now seem somewhat benign, given the slippage in tariff revenues and higher interest costs.

Figure 12 shows that the effective tariff rate has fallen to 7-8%, from a peak of 12% and the CBO's assumptions of 15%. The CBO assumed that the custom duties would total about \$4trn in revenues in 2027-36. At a 10% effective rate, they would be about \$2.7trn, or \$1.3trn lower. Higher interest rates also add to budget deficits. Figure 13 shows that every 10bp adds about \$380bn to 10-year cumulative deficits. For instance, 5-year yields have risen about 50bp year-to-date, which, if sustained, implies about another 1.9trn in 10-year deficits. One potential offset is strong productivity gains. The CBO estimates that a 0.5pp improvement in annual productivity growth would reduce 10y average deficits by 1.6trn. $^{1}$

Overall, it appears that the fiscal outlook is likely worse than what the CBO assumed earlier in the year. Were the budget deficit to average 7% GDP instead, 30y swap spreads would be about -85bp.

We believe the Treasury's issuance strategy is likely helping keep the fiscal risk premium in check for now. It has been skewing issuance to the front end. For instance, of the \$2.1trn in net borrowing needs it faces in 2026, we expect only \$1.2trn in notes/bonds and the rest (about \$900bn, or 43%) in T-bills. This is well above the share of T-bills in outstanding debt of about 22%. We believe that the Treasury is likely later this year to signal that it is looking to increase auction sizes sometime in 2027. As that comes closer, swap spreads should tighten towards fair levels and long-term yields should rise somewhat.

FIGURE 10. As the fiscal outlook has worsened, Treasuries have cheapened versus swaps  
![](images/9f1a7d5b41f96d2f7fd24e77442561cde1cc6e5fe12ec1b2a74985e05f00621e.jpg)  
Source: CBO, BARC

FIGURE 11. A 1pp increase in deficit/GDP ratio tightens 30y swap spreads about 15bp  
![](images/b11f1551ebdc150ed7be513c1b5d063eda4f9a34f99ba2ae62c6774745054abb.jpg)  
Source: CBO, BARC

FIGURE 12. The effective tariff rate has slipped well below the CBO's assumption of 15%  
![](images/008795ad1e17bbfbea5a4a80dba665a70ec77086784bf55387b14e75622f8072.jpg)  
Source: Bloomberg, BARC

FIGURE 13. Higher interest rates would also add to budget deficits  
![](images/c46e861ccef663d2e38bad65c48a55532e87e41f0db8352345131546ff4ccf62.jpg)  
Source: CBO, BARC

## The rate term premium is well priced, but risks remain

The rate term premium (the swap rate minus the expected rate) has already risen well above pre-COVID levels and likely beyond those pre-GFC as well; the latter conclusion is sensitive to whether survey-based estimates of expected rate are lagging and biased lower. We think a return to pre-GFC norms is largely justified by a few factors:

The buyer base has become more price sensitive, needing a higher term premium. Figure 14 shows the ownership of US Treasuries broken down into foreign official, foreign private, Fed and domestic private. Foreign official holdings have steadily fallen over the past decade, and Fed holdings have also unwound the increase during COVID. As a result, foreign and domestic private investors own a larger share of the universe.

The diversification benefits of USTs have come into question with elevated inflation: Figure 15 shows the return correlation between stocks and the long end. The negative values over post-GFC to the pre-COVID era suggest that bonds were diversifying risk-off scenarios, and this insurance value manifested itself as depressed term premia. The correlation has now reverted to positive territory as inflation has become the primary concern. Were growth to dominate again, the term premium might fall.

Rate volatility is below pre-GFC levels and has room to rise: Warsh's June FOMC press conference signals a shift away from forward guidance toward a more data-reactive policy framework, with markets encouraged to respond directly to incoming data, rather than attempting to infer the Fed's reaction function. Figure 16 shows that implied rate vol on 2y and 10y tails on average traded higher pre-GFC, when the Fed was communicating less. 1y2y rate vol averaged 116bp/y from 1995 to 2005, versus the current 95bp/y. 1y10y rate vol averaged 109bp/y, vs. 78bp/y currently.

## Warsh's disdain for a bloated Fed balance sheet poses upside risk to the term

premium: While the Fed's Treasury holdings as a share of outstanding debt are below pre-GFC levels, the portfolio is much longer. About 40% of Fed's holdings are greater than 10y, versus 10% in 2006; that in T-bills is 10%, vs. 35% in 2006. As a result, the portfolio WAM is about 8.5 years, versus 3 years pre-GFC (Figure 17). We estimate that under passive shortening (via reinvestments but no sales), the Fed's portfolio in 10y equivalents would fall 1pp GDP every year, which could push up the term premium 10bp/yr.

Bottom line: 30y yields around 4.9% do not look particularly high in a historical context, and scope remains for further repricing through neutral rates and fiscal premia: R\* estimates are too anchored to the post GFC–pre COVID era and have room to rise. The deficit outlook is likely worse than is discounted. Rate volatility has room to rise and a shortening of the Fed's balance sheet would further add pressure to the term premium.

FIGURE 14. The buyer base has become more price sensitive needing a higher term premium  
![]

[中间内容因长度限制已省略]

 existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.

## BRCF2242
"""
