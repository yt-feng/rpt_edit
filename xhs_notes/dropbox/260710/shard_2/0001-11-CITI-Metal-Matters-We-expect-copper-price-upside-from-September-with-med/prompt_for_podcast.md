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
# Metal Matters

# We expect copper price upside from September with medium-term bullish view intact.

## CITI'S TAKE

We publish April and May data for our global copper end-use consumption tracker. Negative headline implied y/y copper end-use growth reflects the distortive base effect of the policy-led spike in reported China renewable additions in 2Q'25. Implied growth in global copper end-use elsewhere has been tepid, but headline manufacturing sentiment remains robust. We expect renewed price upside from September and see copper touching \$15k/t within a year even as copper tariff dynamics and gold market headwinds threaten to limit gains through the summer (July and August).

Our conviction in near-term copper price direction is limited. We think copper will struggle to rally through the summer in our base case that US copper tariff fears fade and if bearish gold-price momentum is sustained — Our call for copper upside through June failed to materialise as a hawkish Fed surprised us, despite reliance versus June's broader commodity price pullback (e.g. gold, oil, aluminium). However, fading fears of potential Section 232 US tariffs on copper cathode risk weighing on sentiment in the coming weeks (given President Trump's end-June review deadline has passed and assuming our base case of no tariff announcement holds).

That said, we see positive price catalysts re-emerging from September including a more dovish Fed, greater focus on tighter copper physical market dynamics in 2027, and the structural medium-term bullish backdrop (please see our 114-slide Copper Book 2026 published late-June). We see copper averaging \$14,500/t through 4Q'26 as risks skew in our view towards a more dovish Fed on easing inflation and a softer US labour market, the potential for an eventual US-Iran deal, lower real interest rates, and a generally more supportive backdrop for demand and growth expectations.

Global manufacturing PMIs implied further expansion in activity in June, supported by AI-related investment and defence spending, despite softer sequential readings in the US and Europe. Resilience in manufacturing activity and these metal-intensive demand segments likely continue to support copper demand, a tailwind that our global end-use consumption tracker may be understating given it does not currently track these segments directly. Productivity gains from AI investment also have the potential to support copper pricing by supporting growth and quelling above-target inflation.

Headline implied global copper end-use declined by \~10% y/y in May'26, an anomaly due to the reporting spike in China renewable installations in May'25 (when GCET rose 13.5% y/y). Stripping out these distortions, underlying end-use appears tepid but resilient, with implied end-use growing \~1% y/y. Policy driven front-loading of China solar and wind installation reporting peaked in May'25 heavily distorting growth on a y/y comparison this year. Relying solely on headline copper-end use thus overstates the weakness in copper demand. Adjusting for solar/wind distortions, implied global copper end-use has risen 1.4% YTD vs a decline of 2.1% YTD on an unadjusted basis.

Tom Mulqueen $^{AC}$ +44-20-7986-4559
tom.mulqueen@citi.com

Shreyas Madabushi $^{AC}$ +91-22-4277-5048
shreyas.madabushi@citi.com

Maximilian J Layton $^{AC}$ +44-20-7986-4556
max.layton@citi.com

Wenyu Yao $^{AC}$ +44-20-7986-4551
wenyu.yao@citi.com

Kenny Hu, CFA $^{AC}$ +65-6657-3873
kenny.x.hu@citi.com

Ephrem Ravi $^{AC}$ +44-20-7986-2462
ephrem.ravi@citi.com

Jack Shang, CFA $^{AC}$ +852-2501-2441
jack.shang@citi.com

Alexander Hacking, CFA $^{AC}$ +1-212-816-6232
alex.hacking@citi.com

# Copper upside from September, medium-term bullish view intact

We expect renewed upside for copper prices after the summer as we look for prices to average \$14,500/t in 4Q'26 and to touch \$15k/t within a year. We think copper will struggle to rally sustainably through July and August given our expectation that the market will fade the tail risk of US import tariffs on cathodes over the coming months and given the potential for further bearish gold (and broader precious) price momentum near-term. By September, we see bullish catalysts re-emerging, including a more dovish Fed in response to softening US labour market conditions, a renewed focus on projected tighter physical copper market dynamics in 2027 and the structural copper bull case (see our 114-slide note published mid-June: Copper Book 2026 – Structural tailwinds and cyclical sensitivity pave path to \$15 k/t copper). We think lower real interest rates, an eventual and more sustainable US-Iran deal and a more supportive backdrop for demand and growth expectations should further improve sentiment towards copper later in the year.

Our base case remains that copper cathode will not be subject to a Section 232 US import tariff. We think the market will be inclined to fade the tail-risk of tariffs through the summer since more than a week has passed since the June $30^{\text{th}}$ review deadline without an announcement. The June 30th deadline set by President Trump last July for the review of Section 232 tariffs on copper cathode was over a week ago without any acknowledgement from the administration. Tariffs could still be announced in the coming weeks, but we don't think this is likely and we believe it is in the US administration's interest to maintain strategic ambiguity by neither implementing tariffs nor ruling them out. This can act as a headwind for copper pricing through July/August (more so for US copper prices given the current premium, Fig 1) if market participants opt to fade tariff tail risks although needs to be balanced against more bullish longer-term structural market themes and volatility in rates expectations around Fed comments and Strait of Hormuz developments.

Figure 1. We expect the COMEX premium over LME to ease further through July and August as tariff risk is faded (assuming our base case that no tariff is announced)  
![](images/594c1163be2e5bd5162888305fe7a11c4ec74ad7be767cc7e0ed42765d954803.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Bloomberg, CME Group, LME

Figure 2. China's copper-in-scrap imports close to flat y/y through to end-May suggested a muted global scrap response to much-higher copper prices.  
![](images/5526e2243fa37127b4bc7dea531d8131a97e92a6fa4a0750362334a515ce4248.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, TDM, China Customs, LME, Bloomberg

Broadly flat y/y China copper-in-scrap imports through May (Fig 2) despite much higher copper prices y/y imply a relatively price-inelastic scrap market.

Combined with flat mine supply anticipated in 2026, it suggests a very constrained supply-picture that can offset implied weakening of China demand growth this year. China's copper scrap imports were close to flat year-on-year through May, with April and May broadly in line with 2025 levels. Given the significantly higher copper price environment, the lack of a stronger import response suggests continued tightness in global scrap supply and a muted scrap availability response to price incentives. We see a balanced copper market in 2026 (Fig 3) swinging to a \~400kt deficit in 2027 basis current prices assuming a modest cyclical demand recovery, sustained energy transition and AI demand growth, versus around half-trend supply growth next year.

Figure 3. Citi copper supply and demand balance 2020-2030

<table><tr><td>kt Cu</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026f</td><td>2027f</td><td>2028f</td><td>2029f</td><td>2030f</td></tr><tr><td>Mine Production</td><td>20,752</td><td>21,179</td><td>21,808</td><td>22,395</td><td>23,128</td><td>23,398</td><td>23,334</td><td>23,739</td><td>24,509</td><td>25,272</td><td>25,880</td></tr><tr><td>% Change</td><td>0.7%</td><td>2.1%</td><td>3.0%</td><td>2.7%</td><td>3.3%</td><td>1.2%</td><td>-0.3%</td><td>1.7%</td><td>3.2%</td><td>3.1%</td><td>2.4%</td></tr><tr><td>Of Which Disr. Allowance (t)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>973</td><td>1,805</td><td>1,926</td><td>1,964</td><td>2,023</td></tr><tr><td>Of Which Disr. Allowance (%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>4.0%</td><td>7.1%</td><td>7.3%</td><td>7.2%</td><td>7.2%</td></tr><tr><td>Refined Production</td><td>23,591</td><td>24,374</td><td>25,067</td><td>25,561</td><td>26,450</td><td>27,300</td><td>27,505</td><td>27,866</td><td>28,716</td><td>29,557</td><td>30,248</td></tr><tr><td>% Change</td><td>-0.3%</td><td>3.3%</td><td>2.8%</td><td>2.0%</td><td>3.5%</td><td>3.2%</td><td>0.8%</td><td>1.3%</td><td>3.0%</td><td>2.9%</td><td>2.3%</td></tr><tr><td>Refined Consumption</td><td>23,103</td><td>24,769</td><td>24,841</td><td>25,704</td><td>26,311</td><td>26,943</td><td>27,522</td><td>28,267</td><td>28,820</td><td>29,446</td><td>29,928</td></tr><tr><td>% Change</td><td>-3.4%</td><td>7.2%</td><td>0.3%</td><td>3.5%</td><td>2.4%</td><td>2.4%</td><td>2.2%</td><td>2.7%</td><td>2.0%</td><td>2.2%</td><td>1.6%</td></tr><tr><td>End-Use Consumption</td><td>24,165</td><td>25,908</td><td>25,984</td><td>26,886</td><td>27,521</td><td>28,182</td><td>28,788</td><td>29,567</td><td>30,146</td><td>30,800</td><td>31,305</td></tr><tr><td>Surplus/Deficit</td><td>489</td><td>-395</td><td>226</td><td>-143</td><td>139</td><td>357</td><td>-18</td><td>-401</td><td>-104</td><td>111</td><td>320</td></tr><tr><td>Av. Price (US$/t ex-US)</td><td>6,183</td><td>9,318</td><td>8,830</td><td>8,485</td><td>9,145</td><td>9,950</td><td>13,700</td><td>14,250</td><td>14,000</td><td>14,000</td><td>14,000</td></tr></table>

\*Updated 12-Jun-26, forecast production and consumption basis current \~\$13.5k/t spot price

© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: Citi, Bloomberg, Wood Mackenzie, BGRIMM, IWCC, ICSG, Company Reports

## Global factory output expanding even as near-term outlook clouded by more hawkish Fed and geopolitical uncertainty

Global June PMI prints suggest expanding manufacturing activity (see Figure 4 and 5) across all major economies including China, US and Europe. This is generally a supportive signal for cyclical copper consumption even as investor's increased pricing-in of Fed rate hikes has weighed on sentiment in recent weeks. China's manufacturing PMI has nudged back into expansion with the latest prints coming at 50.3. Export orders continued to lead the recovery, with high-tech manufacturing outperforming old-economy sectors. Our China economists expect further imminent targeted easing but not a policy pivot. The July Politburo meeting is the next catalyst to watch from a China policy perspective.

European PMI implied manufacturing expansion for a fifth consecutive month while US prints suggest modest growth in activity. Although June prints edged down slightly versus May for both Europe and the US, activity was supported by supply-chain disruptions linked to the Middle East conflict as consumers accumulated inventory ahead of feared price rises. The US manufacturing sector continues to show momentum as the buildout of AI infrastructure remains a tailwind. In addition, defence spending is emerging as a likely contributor to activity. Our US economists expect manufacturing PMIs to remain in expansion this year as these tailwinds persist.

Figure 4. Copper fund positioning remains net bullish amid structural demand drivers, supply constraint, and improving PMIs now also imply support.  
![](images/8eefc2ba33a79c029879e406bf58dcccf1819971c96b0970aeb11b4cfbb02d38.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Bloomberg, LME, CME Group

Figure 5. Global PMIs in expansion in recent months amid supply-chain stockpiling on Middle East tensions and AI/Datacentre buildout  
![](images/8de0baa381cb1fd7cc7a4a90b945b9cdbcba2fedaeebc78fa154962b80f911d5.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, Rating Dog, Platts, Bloomberg, NBS, SMM

## China's renewables base effect negatively distorting tracked global copper end-use, otherwise growing but sluggish

Implied global copper end-use from our proprietary GCET tracker declined by \~10% y/y in May 2026. This largely reflects a statistical base effect stemming from comparison against a record reporting spike in China's renewables installations in May 2026. Aggregate demand across all other segments rose +1% y/y. The weak headline print is not surprising and is consistent with our expectations in prior publications, where we highlighted the outsized impact of policy- and trade-driven shifts in China's renewable installations last year. Notably, May 2025 saw implied copper end-use growth of \~13% y/y, driven by exceptionally strong reported China solar installations, with energy transition-related demand surging \~120% y/y. More normalised reported installations through 2Q'26 look far weaker by comparison. China's renewables installation reporting is an imperfect proxy for underlying copper consumption given the policy-sensitive volatility which must be acknowledged when interpreting implied y/y growth rates from our tracker. The base effect is likely to reverse and drive more positive implied growth in 2H'26.

Figure 6. China renewable power installations weigh on tracked copper end use growth y/y amid strong base effect  
![](images/f937fa8c8a017c1cd9a078a5de6b275f91b688f2a965eae05a2b151f1be37c83.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, ICA, Wood Mackenzie, Bloomberg

Figure 7. Global implied copper end-use grew \~1% y/y in May'26 after excluding consumption implied by China solar and wind reported capacity additions.  
![](images/09b0dd73e6c5ec5fcc32b0cd0b6c4a264df05c450e799f087ddf02de540404b4.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, ICA, Wood Mackenzie, Bloomberg

Figure 8. Total implied copper end-use (based on our tracker) annualizing at 27Mt  
![](images/53764580245a7949bb73d3940374600d54448b4e57139bf2331c230016b3de0c.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

Figure 9. Weaker China implied copper end-use due to statistical effects weighs on global implied copper end-use  
![](images/95b7233d17fdb5478fe807f4e8e89e498abd7c3402999da391cfee40556d8b00.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

China's weak headline copper end-use (as implied by our tracker) has been the primary drag on global consumption. China's copper end-use declined by \~17% y/y in May 2026. However, adjusting for distortions from the renewable sector, the underlying picture (see Figure 8) is more stable. Excluding solar and wind installations, China's copper end-use grew by \~0.6% y/y, indicating modest resilience in broader industrial demand. The key drag remains the sharp slowdown in renewable installations. China installed \~8.7GW of solar capacity in May—the lowest monthly run-rate this year—compared to an outsized \~93GW in May 2025. Similarly, wind installations came in at \~3.8GW versus \~26GW in the same period last year. This normalization following last year's front-loaded build-out has significantly reduced copper demand from the energy transition segment.

In addition, softer domestic EV demand has weighed on energy-transition-related copper consumption. EV wholesales are up just \~2% YTD, while retail sales have contracted \~15% y/y, pointing to weak domestic uptake. That said, this has

been partially offset by robust export demand, with EV exports surging \~115% y/y. Despite the sluggish start to EV sales in 2026, implied copper consumption from EVs still grew a solid \~17% y/y in May, supported by the export channel and ongoing electrification trends. Looking ahead, seasonality and policy support should provide a tailwind. We expect a stronger pickup in EV sales into 2H'26, underpinned by recently announced policy measures aimed at boosting EV consumption, particularly in rural areas.

Figure 10. Excluding the impacts from solar and wind, China implied end-use grew \~0.6% y/y in May  
![](images/37766bdeb9f7d9a3ec4d56ae995dd9c42e5ff543f8857905e27d7245df4ede5a.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, ICA, Wood Mackenzie, Bloomberg

Figure 11. China reported solar installations down 70% YTD after spike in Q2'25  
![](images/9acb87166e16f4d7ed01ec69b61264d6ed91fc7db09eed89c87074b00d550a1f.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, NEA

Figure 12. China reported wind installations down \~50% YTD against policy-led spike in May-25  
![](images/4af3fc82e44961e3b8eacfe2edcd1759a5f7835f3592919a19989c5bbd3489ac.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, NEA

Figure 13. China EV wholesales +2% YTD  
![](images/156dccad9f7f41621eb6f8e6e4d277a866fec896a5ac33905fef50b400fd7d39.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, CPCA, Bloomberg

Figure 14. EV exports the main driver of China wholesale autos growth  
![](images/dbf3b06d8980233c2837102d81d3bb0124f2a005b502411228b74ca8fda6d503.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, CPCA, Bloomberg

Figure 15. Electrification of commercial vehicles building momentum in China  
![](images/7177154e10a0ffda528b3f9432eeb0e77edac2b70161f57399e4d03f5cecd0da.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, CATARAC, Bloomberg

Implied ex-China copper end-use grew 1% y/y in May 2026 underpinned by a mix of energy transition and cyclical-related consumption. The outlook for ex-China remains a mixed bag near term. Demand-related concerns have emerged on a hawkish US Fed stance with investors pricing in rate hikes this year. Our house view in contrast expects rate cuts from October. Rising AI-related capex is helping drive demand for power infrastructure equipment, including switchgears and transformers, thereby supporting copper consumption. In addition, continued growth in solar, wind and BESS installations outside of China is contributing to incremental demand. Manufactu

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
