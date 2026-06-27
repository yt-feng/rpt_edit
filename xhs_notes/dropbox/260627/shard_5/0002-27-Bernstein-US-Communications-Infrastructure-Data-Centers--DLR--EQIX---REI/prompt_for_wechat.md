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
# US Communications Infrastructure

# Data Centers (DLR, EQIX): REIT-urning to basics - contextualizing returns for the non-REIT investor

![](images/503d73800e9e772e3782a5f75b98d34a1568b268a05894d424e054021ba7c3ab.jpg)  
Madison Rezaei  
+1 917 344 8622  
madison.rezaei@bernsteinsg.com

![](images/ee82b160df97fa909dd7c610fd7bfe792ff619b295ed204bce80f318433077c7.jpg)  
Nancy Wu

+1 917 344 8545

nancy.wu@bernsteinsg.com

Investor interest in data center REITs has expanded rapidly in the AI boom, attracting an increasingly broad pool of capital beyond the traditional REIT crew. Non-REIT investors puzzle over the right way to think about these companies—both how to contextualize them against one another and against alternate investment opportunities.

Data center REITs often screen poorly on traditional metrics such as return on assets or earnings-based multiples, largely due to their capital intensity, long development timelines, and accounting treatments. Importantly, these apparent distortions do not reflect weak business fundamentals, but rather the limitations of applying short-duration financial metrics to assets that are designed to operate and generate cash flows over multi-decade horizons.

Like most forms of real estate, data centers are characterized by exceptionally long useful lives (in some cases, 50+ years!) and significant upfront investment. These assets require large-scale development expenditures and years of construction before generating revenue, but once stabilized, they can deliver durable and predictable cash flows for decades. As a result, traditional measures can understate their true economic value. Within the REIT framework, Adjusted Funds From Operations (AFFO) provides the most relevant lens, as it best approximates distributable cash flow. Yet even AFFO does not fully capture the development-driven nature of the business, particularly for companies that continuously reinvest capital into new capacity.

As an additional metric, today we are looking at yield on cost. This approach evaluates stabilized returns relative to the original development investment, offering a clearer view of asset-level economics. Leading data center REITs generate attractive yields on cost—approximately 11% for Digital Realty and 26% for Equinix (wholesale v. retail)—well above those typically achieved by private market developers, which tend to cluster closer to the HSD range. These elevated returns help explain how REITs can sustain growth while still supporting shareholder distributions, even when headline valuation multiples appear demanding.

Additionally, we flag the importance of capital allocation strategies in sustaining these return profiles. Digital Realty has been particularly sophisticated, leveraging JV structures, a closed-end fund, and now an open-end strategy (via its recent acquisition of Columbia Capital) to monetize stabilized assets and reinvest in higher-yield projects. Equinix takes a different approach: its higher-margin interconnection and retail colocation model drives a repeatable value-creation cycle. It has also raised a \$15B JV-backed development fund (with GIC and CPP) to support over 1.5GW of xScale capacity, extending its balance sheet while preserving capital for higher-return retail deployments. In this context, elevated public market multiples appear more justified, as investors are effectively underwriting a long-duration growth model anchored by attractive development economics and reinvestment opportunities. We maintain our Outperform ratings on both EQIX (\$1,222) and DLR (\$232).

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">25 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>DLR (Digital Realty)</td><td>O</td><td>USD</td><td>192.44</td><td>232.00</td><td>(9.0)%</td><td>USD</td><td>3.87</td><td>2.74</td><td>2.37</td><td>49.7</td><td>70.3</td><td>81.1</td></tr><tr><td>EQIX (Equinix)</td><td>O</td><td>USD</td><td>1,087.61</td><td>1,222.00</td><td>11.2%</td><td>USD</td><td>14.96</td><td>17.88</td><td>21.36</td><td>72.7</td><td>60.8</td><td>50.9</td></tr><tr><td>SPX</td><td></td><td></td><td>7,357.49</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We value DLR on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$232 price target is based on 27x our 2027E AFFO per share of \$8.52.

We value EQIX on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$1,222 price target is based on 25x our 2027E AFFO per share of \$48.63.

## DETAILS

## WHAT DO STABILIZED RETURNS LOOK LIKE?

We evaluate stabilized asset returns for Digital Realty (DLR) and Equinix (EQIX) using two approaches: ROA—defined as total stabilized NOI divided by gross PP&E—and yield on cost—defined as estimated stabilized net income divided by average net PP&E. While differences in asset definitions, capitalization policies, and depreciation conventions can introduce some variability in the denominator, these measures together provide a consistent directional view of underlying asset productivity. Across both frameworks, we observe a persistent return premium at EQIX.

We believe differences in pricing model and customer mix represent a primary driver of this divergence. Equinix is more heavily weighted toward retail colocation, which is typically characterized by smaller deployments, higher unit pricing, and structurally higher margins. In contrast, Digital Realty has greater exposure to wholesale colocation, including powered shell offerings, which tend to involve larger-scale deployments at lower unit margins but benefit from longer contract durations and greater revenue stability. This fundamental difference in go-to-market strategy likely contributes meaningfully to the higher stabilized asset returns observed at EQIX.

We also observe a material difference in exposure to higher-margin revenue streams. Approximately 24% of Equinix's FY2025 revenue is derived from interconnection and managed infrastructure services, both of which exhibit more “software-like” margins. In comparison, interconnection represents only approximately 8% of Digital Realty’s revenue (typically more driven by enterprise colocation, where they are smaller today). Additionally, Digital Realty frequently relies on third-party partnerships, such as with providers like Megaport and Lumen, to deliver certain managed services. This approach may limit its ability to capture the full margin associated with these offerings relative to Equinix’s more vertically integrated model, further contributing to the return gap.

Differences in depreciation policies can also meaningfully distort return metrics. For example, DLR depreciates buildings and improvements over 5–39 years, while EQIX uses 12–60 years for buildings and 12–40 years for leasehold improvements, which can drive very different annual D&A charges for assets with similar economic lives. Shorter useful lives front-load depreciation, depressing GAAP net income and any return measure that uses a below-the-line numerator (such as our accounting ROA on net PP&E), whereas longer lives smooth that expense and mechanically boost ROA, even if underlying cash returns on cost are identical. This is another reason we emphasize stabilized yield on cost (based on NOI or cash earnings over gross PP&E) as our primary gauge of project economics, and treat accounting ROA as a secondary, more methodology-sensitive indicator.

Finally, we believe differences in how each company defines and classifies stabilized assets also influence returns, both on an ROA and yield on cost basis. Digital Realty defines stabilization as assets where less than 5% of rentable square footage remains under development, whereas Equinix considers an asset stabilized once the final phase of expansion or redevelopment has begun operating. These definitional differences are reflected in portfolio composition metrics. At Digital Realty, stabilized PP&E represents 81% of the asset base but generates only 72% of revenue. At Equinix, stabilized PP&E accounts for 68% of the asset base while contributing >80% of revenue. While part of this discrepancy likely reflects differences in pricing model and service mix, we believe definitional variation may also play a role in shaping reported stabilized returns, as Digital Realty has a tighter definition and may associate more like-for-like revenue with development assets.

Overall, we attribute Equinix's higher stabilized asset returns to a combination of greater exposure to retail colocation, a higher mix of margin-accretive interconnection and managed infrastructure services, and differences in asset classification methodologies. Although certain reporting nuances remain, the directional conclusions are consistent across multiple analytical approaches and suggest structurally higher asset productivity within Equinix's portfolio relative to Digital Realty.

EXHIBIT 1: ROA of Stabilized Assets  
![](images/d9b9c2a62a1a75ec3e48ec925c7d4f918440dbe9c9e4f0e32138328b45a9aeef.jpg)  
Calculated as total stabilized NOI / gross PP&E
Source: Bloomberg, Company disclosures, Bernstein analysis and estimates

EXHIBIT 2: Yield on Cost of Stabilized Assets  
![](images/e83869a623e30d201fe389cb225d7f5c88b9db312c1b7774bd06e834b86e4490.jpg)  
Calculated as est. stabilized net income / average net PP&E
Source: Bloomberg, Company disclosures, Bernstein analysis and estimates

EXHIBIT 3: We believe that ROA may obscure the economic returns of data center assets, as depreciated book values are more sensitive to depreciation schedules and capital structure than project economics  
ROA of Stabilized Assets (Net PP&E), 2015-2025  
![](images/1058a59df1e0537fc1092216062931e8f4b7aaa2457e7d6b450cf0bbc21ed691.jpg)  
Calculated as total stabilized NOI / gross PP&E  
Source: Bloomberg, Company disclosures, Bernstein analysis and estimates

EXHIBIT 4: Our preferred measure is yield on cost when looking at unlevered project-level returns, as colo REITs are extremely CapEx-heavy and depreciation is large and can be arbitrary

Yield on Cost of Stabilized Assets (Gross PP&E), 2015-2025

![](images/326b512511d36fba9d1cbabc5f4c057de1234a00e8f6141cd0c1629c61f613f2.jpg)  
Calculated as est. stabilized net income / average net PP&E  
Source: Bloomberg, Company disclosures, Bernstein analysis and estimates

## ARE PUBLIC MARKET MULTIPLES JUSTIFIED?

Public market valuations for the data center REITs appear rich on headline EV/EBITDA, with our targets implying investors are effectively paying only a \~4-5% pre-CapEx EBITDA yield for stabilized portfolios (given DLR and EQIX's current EV/NTM EBITDA of 22.3x and 23.1x, respectively). We think this is broadly justified by asset-level economics: stabilized data centers are generating meaningfully higher returns on cost, such that ROIC/ROA sits above the cost of capital, and management teams can repeatedly recycle capital into additional projects at attractive development returns. If investors believe these companies can continue to deploy capital at returns closer to the asset-level yields we observe today (roughly 11% for DLR and 26% for EQIX in 2025), then a mid-single-digit starting yield can still support a low-teens equity IRR, conceptually combining a 4-5% initial EBITDA/AFFO yield with HSD to low-teens sustainable earnings growth to arrive at roughly 11-13%+ total return. Recent fundamentals are consistent with this framework: in 2025, Digital Realty grew AFFO per share by 7.1% and Equinix by 9.3%, which sits within the growth range implied by our return math and helps to reconcile high EV/EBITDA multiples with a reasonable long-term return profile for equity holders. Our forecasts also put future growth higher for both companies, at 11.3% FY26-28 CAGR for DLR and 12.1% for EQIX.

Thus, though our target prices underwrite EV/NTM EBITDA multiples of 23.9x for DLR and 29.2x for EQIX (implied from 27x and 25x NTM AFFO, respectively)—which correspond to forward EBITDA yields in the low- to mid-4% range—we view them as consistent with the combination of strong stabilized economics and the ability to convert those returns into AFFO per share growth, which together can still support a low-teens equity IRR off an MSD starting cash yield. We view the higher multiple for EQIX as reflecting its superior asset-level returns, scale, and growth profile: EQIX's substantially higher yield on cost implies a wider spread over its cost of capital likely due to the factors above (pricing model and higher margins, albeit possibly somewhat offset by a less punitive depreciation accounting policy and definition of “stabilized”), which, in our view, warrants a meaningfully higher EV/EBITDA than DLR. In both cases, we believe the implied 3-4% forward EBITDA yield at our target prices represents the premium the market is placing on the platforms' ability to earn attractive unlevered returns on invested capital and to reinvest incremental dollars into their development portfolios.

EXHIBIT 5: DLR Historical Forward EV/EBITDA (NTM)  
![](images/0921c1d36bb8a5d9a32661ba48b728133a188939e173774e6d793cbf7b3f612d.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 6: EQIX Historical Forward EV/EBITDA (NTM)  
![](images/42543fab4fa54c5f3ae89468b6a0c80c863a23ec1153cbfb2873f8eb0de7f828.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 7: DLR Price to NTM AFFO per Share (2021-2026, DLR and EQIX)  
![](images/abe40550f9c0e9c672c4bc3fde5cc269423901fca111c048843df97e7cc99a93.jpg)  
DLR Price to NTM AFFO per Share (as of June 25, 2026) - Max: 30.9x, Median: 23.2x, Avg: 22.7x, Min: 14.9x, Bernstein 27x. Source: Bloomberg, Bernstein estimates and analysis

EXHIBIT 8: EQIX Price to NTM AFFO per Share (2021-2026, EQIX and DLR)  
![](images/455843ded1a3aa840fff44f4ea831d8b416736978051fd146cb1beab10683f87.jpg)  
EQIX Price to NTM AFFO per Share (as of June 25, 2026) - Max: 31.6x, Median: 23.1x, Avg: 23.1x, Min: 16.4x, Bernstein 25x. Source: Bloomberg, Bernstein estimates and analysis

## EXAMPLE: 350 E CERMAK, A 27YO, STILL-PRODUCING, HIGHLY VALUABLE DATA CENTER

While we do not have infinite examples of data centers with very long lifespans, there are enough. Our personal favorite is 350 Cermak in Chicago, an enormous 1.1M sqft facility owned by DLR and partially leased by EQIX. 350 Cermark was originally built as a printing plant in 1912, and in 1999, it was reconceived to be the first and largest carrier hotel in the U.S. The building's original industrial construction—designed to support heavy printing presses—translated well to data center use, providing the kind of reinforced floor loading and structural depth (column spacing of 24' x 24') needed for dense server deployments.

DLR acquired the facility in 2005 for \$140M. Today, it is recognized as one of the most interconnected and valuable multi-tenant data centers in the Midwest, with 330+ network providers per our Interconnection analysis. While we haven't attempted to estimate the financials on it as a standalone facility, estimates put its value over \$2B... we are highly confident it is still producing lucrative returns, 27 years after its original conversion.

## EXHIBIT 9: Digital Realty's facility at 350 Cermak, originally built in 1912

EXHIBIT 10: The facility was retrofitted into a telecom and data center hub in 1999 and acquired by DLR in 2005  
![](images/05b63664a132ff44047f692825f2cd30843f6f9c21d143f82bb8f70a6eb0e1f5.jpg)  
Source: Data Center Knowledge

![](images/aa863cb32125b2e1b53041001f9f1ac93ed08e735ffe17d279f5a25f88ba7ded.jpg)  
Source: Forbes

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Digital Realty Trust, Inc.

We value DLR on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$232 price target is based on 27x our 2027E AFFO per share of \$8.52.

## Equinix, Inc.

We value EQIX on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$1,222 price target is based on 25x our 2027E AFFO per share of \$48.63.

## RISKS

## Digital Realty Trust, Inc.

The main downside risks to our price target/Outperform rating on DLR are 1) Lower than expected growth in the <1MW segment, 2) Slowdown in enterprise demand for data center capacity, and 3) Continuing decline in market share of data center supply may elevate pricing pressures

## Equinix, Inc.

The main downside risks to our price target/Outperform rating on EQIX are 1) Slowdown in enterprise demand for data center capacity, 2) Increased competition in the interconnection space, and 3) Continuing decline in market share of data center supply may elevate pricing pressures

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exc

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
