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
# US Communications Infrastructure & Global Digital Assets

# Data Centers & Neoclouds: How much is a megawatt worth?

![](images/872499a7f732bd8eef80defb821f8228359b40ab8b9f0bb64b007ace71a11e28.jpg)

![](images/720202c2af392324745d05ceb4723ce171458ad911423d7de273c0d9c77eb96e.jpg)

![](images/6697666c64e9fbb6bf537ebd31885eb3f79e1fd0f36ee4ac342ad63a70bec75c.jpg)

![](images/b929bc2181e588962d7bc64dc8634d0e0b5370df606fe9b4a866b96be0441dc5.jpg)

![](images/50a87d15c2fcd92ffee2ef9fe7c903fda6b9bc99c3f50388cc61dc2a6eb2bc30.jpg)

![](images/c95c0df10f49720214c5075e1f165841cc1efa98e798a3cba944a8a92177ed22.jpg)

Madison Rezaei
+1 917 344 8622
madison.rezaei@bernsteinsg.com

Gautam Chhugani
+91 226 842 1416
gautam.chhugani@bernsteinsg.com

Nancy Wu
+1 917 344 8545
nancy.wu@bernsteinsg.com

Mahika Sapra
+91 226 842 1408
mahika.sapra@bernsteinsg.com

Sanskar Chindalia
+91 226 842 1445
sanskar.chindalia@bernsteinsg.com

Harsh Misra
+91 226 842 1457
harsh.misra@bernsteinsg.com

Almost every time a splashy GPU cloud or colocation contract hits, we get questions on whether that is a “good deal”. Today, we look at the \$/MW of the public data center and neocloud companies, in addition to benchmarking the publicly announced deals with other private providers. We continue to prefer the colo model to the neocloud model, but can appreciate that some neocloud contracts are quite attractive, particularly when the neocloud owns its own real estate.

Revenue/MW is a frequently assessed metric for both colo and cloud deals (not always rightly so). It can vary dramatically by business model, location of capacity, time to service, contract duration, and size of deal. We've seen ranges from <\$1M to \$55M/MW. Generally, neocloud models look attractive on a revenue basis with very high \$/MW, but when you layer in opex, actual performance varies.

Colocation model: landlord-style REITs sell powered capacity on long-term leases - either on more of a retail or wholesale basis. They serve a broad base: enterprise, hyperscaler, and sometimes neocloud customers, anchoring pricing and utilization. Increasingly, we see emerging AI infra providers (WULF, CIFR) playing with this model. The highest revenue per MW in this space unsurprisingly belongs to EQIX (\$5M/MW), who has a retail-focused model, layering services and interconnection revenue on top of a valuable major metro footprint. More wholesale-type models end up in the \$3-\$4M range, with the emerging entrants lower on a per-MW basis than the established REITs. This likely has to do with available capacity and location—DLR, EQIX, and CoreSite all have strong footprints in top markets and can sell capacity immediately, whereas the emerging players are in more rural areas and mostly preselling for yet-to-be-completed builds.

GPU cloud model: The main players in this space are CRWV, NBIS, and IREN, though we are seeing other non-neocloud players announce competitive large-scale deals. Since the neoclouds are offering a vertically integrated solution, monetizing the same MWs with hardware and services on top of the real estate, the \$/MW levels are higher. Scarce/near-term capacity, fungible terms, and shorter contract durations or flexible contract-outs (for example, 90-day terms instead of traditional 5-year leases) increase the value per MW.

Return differences: Colocation providers are relatively asset-heavy but OpEx-light; while they incur the upfront cost of developing and building facilities, once a data center is stabilized, ongoing operating costs are comparatively low. A significant portion of power and facility-related OpEx is either passed through to customers or embedded within lease structures. By contrast, neocloud providers are RE-light (generally, some are building themselves) but remain capital-intensive as they bear the cost of GPU purchases and see correspondingly high CapEx levels.

Across our coverage, we continue to prefer the colo model over the cloud model for subscale providers. The emerging AI infra providers represent an interesting counterpoint to traditional REITs as they look to pursue the same model on a higher-risk, potentially higher-reward basis. Without a ton of history, it's hard to assess them on the same basis today.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">22 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">EBITDA (M)</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>DLR (Digital Realty)</td><td>O</td><td>USD</td><td>195.54</td><td>232.00</td><td>(13.7)%</td><td>USD</td><td>3.87</td><td>2.74</td><td>2.37</td><td>50.5</td><td>71.5</td><td>82.4</td></tr><tr><td>EQIX (Equinix)</td><td>O</td><td>USD</td><td>1,115.94</td><td>1,222.00</td><td>1.2%</td><td>USD</td><td>14.96</td><td>17.88</td><td>21.36</td><td>74.6</td><td>62.4</td><td>52.2</td></tr><tr><td>AMT (American Tower)</td><td>O</td><td>USD</td><td>176.43</td><td>207.00</td><td>(44.1)%</td><td>USD</td><td>5.40</td><td>6.60</td><td>7.08</td><td>32.7</td><td>26.7</td><td>24.9</td></tr><tr><td>CRWV (CoreWeave)</td><td>U</td><td>USD</td><td>111.29</td><td>67.00</td><td>(64.6)%</td><td>USD</td><td>(1.20)</td><td>(4.20)</td><td>(2.41)</td><td>38.4</td><td>15.1</td><td>8.0</td></tr><tr><td>IREN (IREN)</td><td>O</td><td>USD</td><td>56.87</td><td>100.00</td><td>418.0%</td><td>USD</td><td>269.67</td><td>233.06</td><td>1,296</td><td>81.9</td><td>94.7</td><td>17.0</td></tr><tr><td>CIFR (Cipher)</td><td>O</td><td>USD</td><td>28.14</td><td>32.00</td><td>617.3%</td><td>USD</td><td>22.24</td><td>50.72</td><td>636.93</td><td>700.1</td><td>306.9</td><td>24.4</td></tr><tr><td>WULF (TeraWulf)</td><td>O</td><td>USD</td><td>28.31</td><td>36.00</td><td>631.7%</td><td>USD</td><td>(23.11)</td><td>115.77</td><td>768.30</td><td>(17.0)</td><td>(16.3)</td><td>(49.1)</td></tr><tr><td>CORZ (Core Scientific)</td><td>O</td><td>USD</td><td>29.08</td><td>32.00</td><td>120.0%</td><td>USD</td><td>(29.66)</td><td>276.21</td><td>630.77</td><td>(33.0)</td><td>(31.5)</td><td>111.8</td></tr><tr><td>RIOT (Riot)</td><td>O</td><td>USD</td><td>28.63</td><td>30.00</td><td>174.3%</td><td>USD</td><td>164.30</td><td>281.69</td><td>405.58</td><td>(14.7)</td><td>21.0</td><td>(37.0)</td></tr><tr><td>SPX</td><td></td><td></td><td>7,472.79</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

DLR, EQIX, AMT, CRWV estimate is Adjusted EPS; CRWV, IREN, CIFR valuation is EV/EBITDA (x); WULF, CORZ, RIOT valuation is Reported P/E (x); Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

U.S. Communications Infrastructure: We value DLR on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$232 price target is based on 27x our 2027E AFFO per share of \$8.52.

We value EQIX on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$1,222 price target is based on 25x our 2027E AFFO per share of \$48.63.

We value AMT on a Price to NTM Adjusted Funds From Operations (AFFO) per share multiple. Our \$207 price target is based on 18x our 2027E AFFO per share of \$11.49.

We value CRWV on an EV/Adjusted EBIT multiple. Our \$67 price target is based on an Enterprise Value calculated as 28.4x our 2027E Adj. EBIT per share of \$5.81.

Bitcoin Miners/Emerging AI Infra: Crypto miners remain well positioned to solve ‘time to compute’ given their planned 30GW power portfolio and operating ability to deliver ‘warm powered shells’ in time. Over the past two years, miners have contracted 6 GW of power capacity to hyperscalers, neoclouds and AI-chip manufacturers across 17 deals worth over \$110Bn. The contracted 6 GW represents \~20% of the 30 GW pipeline of crypto miners, allowing runway for new contracts. We rate WULF Outperform (PT\$36), CIFR Outperform (PT\$32), IREN Outperform (PT\$100), CORZ Outperform (PT\$32), RIOT Outperform (PT\$30), CLSK Outperform (PT\$24), and MARA Market-Perform (PT\$17)

Emerging AI & IREN figures are calculated based on a per contract basis.

## DETAILS

A number of factors could impact the unit economics of how much value can be extracted from a megawatt of active power, depending on the operating model, customer mix, and service stack of the business. While landlord-style colocation REITs sell primarily powered capacity via long-term leases, neoclouds like CoreWeave are vertically integrated GPU cloud providers that monetize the same one MW with more IT and software services on top. Specifically, Digital Realty, Equinix, and CoreSite focus on 2-15 year leases for blocks of capacity, trading away usage volatility for stable, lower-margin lease revenue per MW. On the other hand, CoreWeave buys or leases the same physical capacity (from other colo providers), fills it with GPUs and resells compute with platform tooling, enabling higher revenue density per MW. They are capturing value from both the infrastructure and application layer. Lastly, emerging AI infra players (former crypto miners) span both ends of the spectrum, with IREN operating a vertically integrated neocloud model while other players (CIFR, WULF, CORZ etc.) follow a colocation-based, power-landlord style model which drives divergence in revenue intensity per MW despite access to similar underlying power assets.

In this note, we examine per-MW revenue, OpEx, and CapEx across our coverage and the two different business models—colocation providers and neoclouds—to highlight how customer mix, stack position, scale, and capital intensity drive wide dispersion in unit economics.

EXHIBIT 1: Resume Annualized Revenue per Active MW (\$M) per Segments  
Annualized Revenue per Active MW (\$M)  
![](images/c8af00efd02c2b4a26a467ee4129274ab45f395fcc6176e04f59293e0fbca82b.jpg)  
Source: Company filings, Bernstein Analysis and Estimates

EXHIBIT 2: Annualized Revenue per Active MW (\$M) by Other AI Contracts  
![](images/ca54bbd5234e408f5d6226f7b6b00198ebfcbfd5818b852374d611528f8d62b4.jpg)  
Source: Company filings and public disclosures, Bernstein Analysis and Estimates

## CUSTOMER MIX AND PRICING POWER

\- Colocation model: Digital Realty, Equinix, and CoreSite serve a broad mix of enterprise, network, and hyperscaler customers, while CoreWeave is concentrated in AI-heavy workloads needing dense GPUs. This customer composition changes average utilization, term, and pricing structures per MW. Equinix and CoreSite have historically skewed towards retail colo and interconnection, with many smaller customers at lower power densities but high cross-connect and networking revenue; this is evident in their revenue per MW figures of \$4.7M and \$3.8M (3-yr average basis), compared with Digital Realty's heavier weight towards wholesale and hyperscaler deals with large tenants, resulting in lower effective pricing per MW of \$3.4M.

\- GPU cloud model: In comparison, neoclouds like CoreWeave and Nebius have higher revenue-per-MW figures of \$20.8M and \$8.4M respectively (on average from FY24-25), due to their customer base of mostly AI labs, startups, and enterprises that need large pools of GPUs for training and inference. They can sustain higher, near 24/7 utilization and maximize monetizable compute hours, allowing them to sign large multi-year deals at premium rates and ultimately driving relatively higher revenue per deployed MW. IREN's customer mix, on the other hand, is anchored by long-term hyperscaler contracts (Microsoft, NVIDIA) along with enterprise clients at their Canada sites, with revenue-per-MW \$10.4 Mn/IT-MW basis contracted capacity, positioning it close to neocloud peers CRWV and NBIS. IREN's position is contingent on timely delivery to hyperscale clients and further buildout of their 5.8 GW owned global power portfolio.

\- AI infrastructure players (CIFR, WULF, CORZ etc.) serve both hyperscalers and neoclouds under long duration (10-15 year) colocation agreements that result in stable, but comparatively lower revenue, at \$1.75 Mn/IT-MW reflecting landlord style monetization of power capacity. WULF and CORZ currently have contracts with neoclouds such as CoreWeave, Core 42 and Fluidstack (backed by Google) while CIFR fares better with 2/3 long term contracts with AWS and the remaining with Google backed Fluidstack. In the colocation business, obtaining hyperscaler rent guarantees and/or stake through warrants acts as a major catalyst for contracts and proof of pedigree, with focus shifting to timely design, procurement and execution.

EXHIBIT 3: Colocation Prov - Annualized Q Rental Revenue per Active MW (\$M, 1Q23-1Q26)  
![](images/a469afe55ae48c06e1738b4689e4a8e55cb292dc4ad593b633eeb3407cc8969c.jpg)  
Source: Company filings, Bernstein Analysis and Estimates  
Neoclouds - Annualized Revenue per Active MW (\$M, 1Q24-1Q26)

EXHIBIT 4: Neoclouds - Annualized Q Revenue per Active MW (\$M, 1Q24-1Q26)

![](images/e012b035c67f685ab9add19b8da3abe785f54c4cfb7694f49afb4715e6e1f337.jpg)  
Source: Company filings, Bernstein Analysis and Estimates

EXHIBIT 5: Emerging AI Infra. - Annualized Rental Revenue per Active MW (\$M)  
Emerging AI Infra. - Annualized Rental Revenue per Active MW (\$M)  
![](images/96a79b775725a8fce0b5d2dc2dc1ec86e78f7f748366b46615cfda01935ff73f.jpg)  
Emerging AI figures are calculated based on a per contract basis.  
Source: Company filings and public announcements, Bernstein Analysis and Estimates

## WHO BEARS THE OPEX?

\- Colocation model: For Digital Realty, Equinix, and CoreSite, a significant portion of power and operating costs is either passed through to customers or structured in lease economics, whereas neoclouds incur most of the OpEx directly on their P&L. Interestingly, operating margin per MW nets out to 8.2% for Digital Realty but 66.2% for Equinix, likely due to the higher mix of retail and higher-margin interconnection business, increased pricing power, and a less development-heavy P&L.

\- GPU cloud model: On the other hand, neoclouds buy power, operate the IT stack, and bundle these services into the compute price. They also bear the cost of GPU depreciation, orchestration software, and support engineering, which also sit as a layer on top of the physical infrastructure cost, leading to a comparatively higher OpEx per MW figure. Notably, while the three colocation REITs incur an average of \$2.2M of OpEx per MW, CoreWeave and Nebius post a whopping \$18.6M and \$33.3M respectively, on average annually from FY24-25. CoreWeave's operating margin per MW, at 10.8%, is within range of Digital Realty, while Nebius is still earlier stage and not yet breaking even on a per-MW basis. IREN bears the full OpEx including power procurement, GPU depreciation, and cloud operations, driving higher absolute OpEx per MW but also higher revenue capture.

\- Emerging AI infra: The distinction is evident here as well: Companies like CIFR, WULF, CORZ enter into long-term contracts in the form of gross net deals (typically \~70-90% NOI margins) or triple net (NNN) deals (\~100% NOI margin), and pass through either most or all power and operating costs to tenants resulting in structurally lower OpEx per MW and higher EBITDA margins at the asset level. The average margin across bitcoin miners pivoting to AI colocation deals is \~85%, expected to improve as the companies land better contracts (progressing towards triple net) with proven execution.

## SCALE, UTILIZATION, AND MARGINS

\- Colocation model: Digital Realty and Equinix both have large global footprints with relatively mature utilization patterns, while neoclouds are still in rapid growth and scaling into high-demand AI workloads. Both dynamics affect revenue intensity and the efficiency of OpEx per MW. Large REITs aim for high occupancy but still carry some underutilized capacity and development pipeline, so some MW of "active" power may not yet be fully revenue-generating, diluting revenue per MW but supporting long-term growth. Their OpEx is spread across a mix of stabilized and ramping facilities—which explains Digital Realty's relatively lower per-MW margin when compared with Equinix.

\- GPU cloud model: Neoclouds have achieved strong top-line growth on the back of building concentrated GPU footprints as AI demand surged, but the high revenue per MW also requires intensive spend on infrastructure and networking. In effect, the colocation REITs in our coverage optimize for steady, lower-risk returns on capital per MW, while neoclouds optimize for high-growth, higher-risk, and the unit economics reflect those different objectives and risk profiles. Specifically, IREN has expanded from a pure North American play into a global firm with a total of 5.8 GW owned power capacity as its USP with site acquisitions in Europe (Nostrum acquisition) and Australia. IREN's revenue is expected to improve with time and scale as utilization ramps, remaining contingent on execution of cloud deployment cycle and customer demand for enterprise scale compute. We see improvement in deal terms in the NVIDIA contract, (vs MSFT contract, assuming PUE for air cooled capacity to be 1.2) as revenue per IT-MW increased from \$9.5 Mn/IT-MW to \$14 Mn/IT-MW.

\- As for emerging AI infra firms, WULF has a multi-state footprint in the US and now has contracts with neoclouds Core42 and Fluidstack (Google-backed) and has begun delivering data rooms. CIFR's sites are concentrated in Texas with nascent diversification with long term contracts with Fluidstack (Google) and AWS (2 separate contracts) - AWS returning as tenant for a deal is evidence of trust placed in CIFR's execution capability, with delivery slated to start in Q4CY26. Both CIFR and WULF demonstrate REIT-like characteristics with high visibility, contract-backed utilization and triple net (NNN) EBITDA margins (\~80-95%) as assets stabilize, and future upside contingent on converting owned power sites into revenue-generating colocation contracts.

EXHIBIT 6: Colocation Prov - Annualized Q OPEX per Active MW (\$M, 1Q23-1Q26)  
Colocation Providers - Annualized OPEX per Active MW (\$M, 1Q23-1Q26)  
![](images/ce48d36670cff74d64f118ef6c8d5e80927cd3c7acd5a7eb25dd56982f88254e.jpg)  
Source: Company filings, Bernstein Analysis and Estimates

EXHIBIT 7: Colocation Prov - Operating Margin per Active MW (%, 1Q23-1Q26)  
Colocation Providers - Operating Margin per Active MW (% , 1Q23-1Q26)  
![](images/cfc1782dd9bbee3a9233e6910fab28cae9b5869a34bc509c1ff84125a296248c.jpg)  
Source: Company fil

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
