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
Asia-Pacific Nuclear Power

# Asia-Pacific Nuclear Power: The next wave of nuclear builds. What does a \$250bn nuclear pipeline mean for Doosan?

![](images/3bc5820285da1537b69662969d3ef7996091f475db893010c3d061d2fa3a9402.jpg)  
Brian Ho, CFA  
+852 2123 2615  
brian.ho@bernsteinsg.com

![](images/7a553c03229cfda2cc7850894e87d9631433a5493d1699d1ac3651010372dd4f.jpg)

Neil Beveridge, Ph.D.

+852 2123 2648

neil.beveridge@bernsteinsg.com

![](images/150fd3804d11e73662b70b848a0b8e293ecb3d092e9ba5edce16ceb3410f09e5.jpg)

Kelvin Yuan, Ph.D., CFA

+852 2123 2612

kelvin.yuan@bernsteinsg.com

We identify \~35GW or \~USD250bn of nuclear projects nearing procurement for Doosan Enerbility. This pipeline is primarily driven by large-scale reactors (APR/AP1000) with a smaller contribution from SMRs. Regionally, the near-term pipeline is dominated by projects in Europe, with U.S. projects emerging toward the end of the decade as financing and supply chain support improves.

This pipeline translates into \~USD44bn (KRW67tn) of potential nuclear equipment contracts. Near-term visibility is strongest in Europe, where Poland is moving toward equipment and EPC contracting this year, followed by Bulgaria targeting EPC contracting in 2027. Longer term, the key source of upside is U.S. nuclear project progression, supported by policy initiatives such as DOE financing programs. In our view, Doosan's established role in AP1000 and large reactor supply chains positions it well to capture a meaningful share of this opportunity.

Despite capacity expansion for gas turbines, we believe fundamentals remain structurally supportive underpinning pricing and margin strength. We expect Doosan's gas orders to increase from KRW4.7tn in 2025 to \~KRW7tn by 2030, supported by capacity expansion. As the installed base scales, we estimate gas services revenue could reach \~KRW0.4tn by 2030 and \~KRW1tn by 2035, providing a growing and higher-margin recurring revenue stream over time.

Taken together, we expect Doosan's annual orders to increase from \~KRW15tn in 2025 to \~KRW24tn by the end of the decade. This is above the company's target of \~KRW16.5tn by 2030. While execution risks and project delays remain, our forecasts incorporate risk-adjusted assumptions based on the progression of nuclear projects through key development milestones.

We expect Doosan's margin profile to improve meaningfully, reaching low-teens OPM by 2028, as business mix shifts toward high value nuclear and gas equipment. These segments are expected to account for more than $75\%$ of revenue by 2027, driven by both volume growth and higher-margin equipment exposure. Globally, gas turbine OEMs are moving toward $20\%+$ margins over the next few years, while nuclear equipment suppliers operate at mid-teens EBITDA margins, providing a strong benchmark for Doosan's earnings potential as sales shift towards overseas market.

We update our valuation to reflect higher nuclear and gas order assumptions. Our SOTP-based price target is KRW100,000 per share, underpinned by a standalone DCF valuation of KRW63tn (unchanged 8% WACC). We believe valuation should increasingly reflect not just current backlog, but also forward order pipeline and mix shift toward higher-quality businesses, with nuclear and gas offering structural growth, margin expansion, and scarcity value given Doosan's limited global competition.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">26 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Ticker</td><td>O</td><td>KRW</td><td>81,400</td><td>100,000</td><td>(11.0)%</td><td>KRW</td><td>132.34</td><td>691.11</td><td>1,249.76</td><td>615.1</td><td>117.8</td><td>65.1</td></tr><tr><td>034020.KS (Doosan Enerbility)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>95,000</td><td></td><td></td><td></td><td>687.53</td><td>1,484.30</td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,963.59</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Our overall conclusion is that Doosan is positioned for sustained order growth alongside a structurally improving earnings profile. First, the company's growth is increasingly underpinned by long-cycle, technically differentiated nuclear equipment, replacing lower-quality legacy exposure and supporting a more long-term investment case. Second, gas markets remain structurally supportive over the medium term, sustaining both volume growth and margin expansion. This is in light of current planned expansion to raise gas turbine capacity. Third, the mix shift toward nuclear and gas equipment should drive not just revenue growth, but also a meaningful improvement in profitability. By 2028, we expect more than $75\%$ of standalone revenue to come from nuclear and gas, and margins to reach the low-teens, aligning more closely with the profitability seen across global energy equipment peers. Reflecting stronger order visibility from nuclear and gas, we raise our SOTP-based price target to KRW100,000, as valuation increasingly incorporates forward pipeline upside and improving earnings quality.

## DETAILS

The orderbook outlook is a key driver of company value, as it underpins revenue visibility, earnings growth, and long-term valuation. Our annual orders outlook reflects the increasing visibility from both the global nuclear pipeline and structurally tight gas turbine market. Based on our bottom-up analysis, we see meaningful order contribution from a set of identifiable nuclear projects, alongside accelerating gas turbine demand driven by power generation needs. Within nuclear, order timing is inherently linked to project progression, with equipment contracts typically awarded after licensing, engineering, and financing milestones are completed. This gives us confidence that much of the pipeline we track is potentially actionable over the next few years. At the same time, gas turbine orders are benefiting from strong end-market demand and constrained supply, reinforcing a multi-year growth cycle. Taken together, we believe the combined nuclear and gas pipeline provides a strong foundation for sustained order growth beyond current company target. As a result, we expect annual orders to increase from \~KRW15tn in 2025 to \~KRW21tn by the end of the decade, on a risk-adjusted basis reflecting the probability of nuclear project progression.

EXHIBIT 1: Order outlook is a key driver of company value. We expect annual orders to grow from c.KRW15tn in 2025 to \~KRW21tn by 2030  
Doosan Enerbility: Annual orders (KRW bn)  
![](images/8b922e6bca4692629695aaaeec8df4ce317127bab02ac29f3ee13dbf944955d2.jpg)  
Source: Company data, Bernstein estimates (2026+) and analysis

Historically, Doosan Enerbility's market capitalization has shown a strong correlation with annual order intake, reflecting the importance of order visibility and backlog growth in driving future revenue and earnings. More recently, however, market cap has expanded faster than reported orders. We believe this reflects a shift in the business mix—from lower-margin segments (coal and desalination) toward higher-quality nuclear and gas equipment, which offer stronger growth prospects and improved margin profiles. In our view, continued growth in nuclear and gas equipment orders should support the company's current valuation.

EXHIBIT 2: Continued growth in nuclear and gas equipment orders are expected to support company's valuation  
![](images/d13c419b2a8da028ddadb4ee9d60f49d47bc765006a68ba6fca410ca0ee668cf.jpg)  
Source: Company data, Bloomberg, Bernstein estimates (2026+) and analysis

## A \$250BN NUCLEAR TAM FOR DOOSAN ENERBILITY

Nuclear projects follow a structured development process, where major equipment contracting generally occurs only after key milestones have been met—namely regulatory licensing approval, completion of front-end engineering and design (FEED), and finalisation of project financing and ownership structure. Prior to these stages, projects remain in feasibility or early engineering phases with limited certainty on scope, timing, and capital allocation. As such, we focus on projects that have progressed sufficiently through these phases and are entering the pre-procurement or early procurement stage, where long-lead items such as reactor vessels, steam generators, and other heavy components begin to be ordered. Heavy nuclear equipment is a major and technically critical part of the overall cost stack, especially for reactor vessels, steam generators, and other long-lead forged and fabricated components.

EXHIBIT 3: Our nuclear TAM is based on identifiable projects nearing equipment procurement stage  
Nuclear new build framework  
![](images/ea6b5bc3bd249adbe043eb7c05fbb3a3f7885d69dfc2c225cb93a6b18a5d1371.jpg)  
Source: Westinghouse, Bernstein analysis

Doosan Enerbility is widely regarded as a preferred global nuclear equipment supplier, underpinned by its deep manufacturing expertise, proven track record on large-scale projects, and ability to deliver critical components at scale. The company's core strength lies in the production of heavy nuclear equipment, including reactor pressure vessels, steam generators, pressurizers, turbine systems, and other long-lead forged and fabricated components for both large reactors (APR1400/AP1000) and emerging SMR designs. These components are technologically complex, capital intensive, and form a critical bottleneck in nuclear project execution, which limits the number of qualified suppliers globally and strengthens Doosan's competitive position. Importantly, Doosan's vertically integrated manufacturing base and accumulated experience from projects such as Korea's domestic fleet and Barakah in the UAE allow it to deliver high-quality components with relatively faster lead times and more predictable execution, supporting shorter construction timelines and lower overall project costs compared to most non-China suppliers. This combination of engineering capability, scale manufacturing, cost competitiveness, and execution reliability has made Doosan a key partner in international nuclear projects and positions it well to capture a disproportionate share of future equipment orders as global nuclear deployment accelerates.

EXHIBIT 4: Doosan's vertical integration and experience from projects such as Korea's domestic fleet and Barakah in the UAE allow it to deliver high-quality components with relatively faster lead times and reliable execution  
Capital cost and construction time for recent nuclear projects  
![](images/0cee931a1ccc95ce98c85a1e1f4472ae824daa7d756286f18e781277230fcc69.jpg)  
Source: Bloomberg, Company data, Bernstein analysis

Doosan Enerbility's Changwon facility in Korea is strategically organized as a vertically integrated "one-stop shop" for nuclear components. This means the company handles virtually every stage of production in-house, significantly reducing reliance on outside suppliers. The facility manages the entire supply chain, starting from the production of the raw material steel all the way to the final assembly of the complex nuclear components. Based on many years of experience in manufacturing large nuclear power plant main reactors, Doosan is also promoting the SMR foundry business, as consignment manufacturer for key SMR companies. As the SMR market is expected to expand in the future, Doosan will establish dedicated production line that can shorten the production period and mass-produce high-quality SMRs. Doosan's depth of experience creates a knowledge base that few competitors can match. The company has spent over 40 years as a major global supplier of nuclear components, developing unrivalled expertise in the design and manufacturing of these systems. Outside of China and Russia, Doosan is the most experienced supplier of nuclear power systems globally.

EXHIBIT 5: Doosan is the most experienced nuclear power system supplier outside of China and Russia
Number of reactors built by supplier in the last 20 years  
![](images/494881347f7d4c1b6829fdf4ca1f37ccef7ab2673465aa5971f40f98338416f8.jpg)  
■ Chinese or Russian suppliers

## Source: IAEA, Company data, Bernstein analysis

Globally, Doosan has manufactured and supplied a significant number of core components, including 34 reactor vessels and 124 steam generators. For AP1000 designs, Doosan has delivered 6 reactor vessel and 12 steam generators. Any new competitor attempting to enter this highly regulated market would need to dedicate the same kind of time and investment to reach the same level of capability and trust. Doosan also began investing heavily in SMR manufacturing more than five years ago, building new experience ahead of the market.

EXHIBIT 6: Doosan's booked nuclear equipment contracts. The company has spent over 40 years as a major global supplier of nuclear components, developing unrivaled expertise in the design and manufacturing of these systems

<table><tr><td colspan="2">Operator</td><td>NSSS Supplier</td><td>Size / Type</td><td>80-90</td><td>90-00</td><td>00-10</td><td>10-20</td><td>20-30</td></tr><tr><td rowspan="14">Domestic</td><td>KHNP/KEPCO</td><td>Westinghouse</td><td>900 MW</td><td>Hanbit 1&amp;2</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Framatome</td><td>900 MW</td><td>Hanul 1&amp;2</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1000 MW (OPR1000)</td><td>Hanbit 3&amp;4</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>700 MW (PHWR)</td><td>Wolsung 2</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1000 MW (OPR1000)</td><td>Hanul 3&amp;4</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>700 MW (PHWR)</td><td>Wolsung 3&amp;4</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1000 MW (OPR1000)</td><td>Hanbit 3&amp;4</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1000 MW (OPR1000)</td><td>Hanul 5&amp;6</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1000 MW (OPR1000)</td><td>KEDO 1&amp;2</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1000 MW (OPR1000)</td><td>Shin-Kori 1&amp;2</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1000 MW (OPR1000)</td><td>Shin-Wolsung 1&amp;2</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1400 MW (APR1400)</td><td>Saeul 1&amp;2</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1400 MW (APR1400)</td><td>Saeul 3&amp;4</td><td></td><td></td><td></td><td></td></tr><tr><td>KHNP/KEPCO</td><td>Doosan</td><td>1400 MW (APR1400)</td><td>Shin-Hanul 3&amp;4</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="8">Overseas</td><td>CNNC</td><td>CNNC</td><td>700 MW (PHWR)</td><td colspan="3">China Qinshan III</td><td></td><td></td></tr><tr><td>CNNC</td><td>CNNC</td><td>600 MW</td><td colspan="3">China Qinshan</td><td></td><td></td></tr><tr><td>SMNPC</td><td>Westinghouse</td><td>1000 MW (AP1000)</td><td colspan="3">China Sanmen 1 / Haiyang 1</td><td></td><td></td></tr><tr><td>SCE&amp;G</td><td>Westinghouse</td><td>1000 MW (AP1000)</td><td colspan="3">US VC Summer 2&amp;3</td><td></td><td></td></tr><tr><td>Southern</td><td>Westinghouse</td><td>1000 MW (AP1000)</td><td colspan="3">US Vogtle 3&amp;4</td><td></td><td></td></tr><tr><td>Progress Energy</td><td>Westinghouse</td><td>1000 MW (AP1000)</td><td colspan="3">US Levy Country 1&amp;2</td><td></td><td></td></tr><tr><td>ENEC</td><td>KHNP/KEPCO</td><td>1400 MW (APR1400)</td><td colspan="3">UAE BNPP 1&amp;2, 3&amp;4</td><td></td><td></td></tr><tr><td>CEZ</td><td>KHNP/KEPCO</td><td>1000MW (APR1000)</td><td colspan="3">Dukovany</td><td></td><td></td></tr></table>

Source: Company data, Bernstein analysis

Our bottom-up analysis of nuclear projects globally shows a substantial and trackable order pipeline for Doosan. We estimate around 35GW of nuclear project with USD250bn of TAM where Doosan could realistically participate, translating into roughly USD44bn or KRW67tn, of potential equipment contracts for the company.

EXHIBIT 7: We estimate USD44bn or KRW67tn of potential nuclear equipment contracts for Doosan Enerbility over the medium term

Doosan Enerbility: Potential nuclear order backlog (KRW tn)  
![](images/4682e8108a15f0480abd752e7109bd04bc76b8147f38aa9a1033d9018524a6ff.jpg)  
Source: Company data, Bernstein estimates and analysis

Importantly, this TAM includes projects that are sufficiently advanced to be approaching equipment contracting or pre-procurement stages, and therefore excludes a wider set of earlier-stage opportunities that could mature over time. In that sense, we view this as an actionable near-to-medium-term addressable market rather than an all-inclusive industry total.

EXHIBIT 8: We estimate around 35GW of nuclear project with USD250bn of TAM where Doosan could realistically participate

<table><tr><td>Country</td><td>Project</td><td>Capacity (GW)</td><td>Construction start</td><td>Expected completion</td><td>Developer</td><td>Status</td><td>Total project cost (USD bn)</td><td>Doosan contract value (USD bn)</td><td>Doosan contract value (KRW tn)</td></tr><tr><td>South Korea</td><td>Shin Hanul 3 &amp; 4</td><td>2.8</td><td>2025</td><td>2032</td><td>KHNP</td><td>Booked</td><td>8.8</td><td>1.9</td><td>2.9</td></tr><tr><td>Czech Republic</td><td>Dukovany 5 &amp; 6</td><td>2.1</td><td>2029</td><td>2036</td><td>EDU II / KHNP</td><td>Booked</td><td>18.6</td><td>3.7</td><td>5.6</td></tr><tr><td>Bulgaria</td><td>Kozloduy 7 &amp; 8</td><td>2.0</td><td>2027</td><td>2035</td><td>Westinghouse</td><td>Not Booked</td><td>14.0</td><td>2.5</td><td>3.8</td></tr><tr><td>Poland</td><td>Lubiatowo-Kopalino 1-3</td><td>3.0</td><td>2028</td><td>2036</td><td>PEJ / Westinghouse</td><td>Not Booked</td><td>20.0</td><td>3.6</td><td>5.5</td></tr><tr><td>Vietnam</td><td>Ninh Thuan 2</

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
