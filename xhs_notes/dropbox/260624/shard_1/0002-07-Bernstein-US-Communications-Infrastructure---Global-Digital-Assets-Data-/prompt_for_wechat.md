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
- 已识别机构名：`Bernstein`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
