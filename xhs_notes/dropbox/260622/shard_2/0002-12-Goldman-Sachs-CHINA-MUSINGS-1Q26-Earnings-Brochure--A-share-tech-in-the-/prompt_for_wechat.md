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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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
CHINA MUSINGS

# 1Q26 Earnings Brochure: A-share tech in the driver's seat

Following the conclusion of the 1Q26 results season, we highlight the key trends and themes emerging from the financial statements of \~7,000 listed Chinese companies, as well as 4,500+ conference call transcripts:

1. A-share tech leading the growth: A stark earnings growth gap emerged as onshore indices (CSI300 +9%, ChiNext +22%, STAR +198% yoy) outpaced their offshore counterparts (MSCI China -8%), driven by the “Hard vs. Soft” tech divide. We project 2Q26 and 2026E earnings growth of +11%/+20% yoy for CSI300 vs. 0%/+8% yoy for MSCI China, validating our preference for A over H-shares.

2. AI profits shifting towards hardware, both globally and domestically. Within China's AI supply chain, the hardware profit share rebounded to $54\%$ in 1Q26 (from $41\%$ in 2024), while downstream software applications faced margin compression.

3. Recovering aggregate revenues but bifurcated margins in “involuted” sectors: Margins compressed for consumer-facing New Economy/POEs and Banks, whereas Old Economy/SOEs experienced a margin recovery.

4. “Going global” is still ongoing: Despite tariff uncertainties, Chinese corporates expanded their overseas revenue exposure to 18% in 2025 (from 16% in 2024), led by Autos, Semis, Cap Goods, Pharma, and Transportation.

5. Total corporate cash returns are projected to reach a record Rmb3.8tn in 2026 (from Rmb3.4tn in 2025), representing a total shareholder yield of 2.9%. Payouts are driven by robust dividends, while remaining cash is increasingly allocated to R&D and acquisitions.

6. Textual analysis of earnings calls reveals that market participants' AI focus has shifted from downstream software toward upstream hardware, while “Going Global” initiatives remain a common theme across manufacturing and hard-tech sectors.

Earnings Strategy: Combining our top-down earnings themes with recent corporate disclosures, we screen 25 names for our refreshed GS China Growth Portfolio to help investors capture growth opportunities with compelling risk/reward profiles.

## Kevin Wang, CFA

Kevin Wang, CFA
+852-2978-2446 | kevin.wang@gs.com
GS (Asia) L.L.C.

Kinger Lau, CFA
+852-2978-1224 | kinger.lau@gs.com
GS (Asia) L.L.C.

Timothy Moe, CFA
+65-6889-1199 | timothy.moe@gs.com
GS (Singapore) Pte

Si Fu, Ph.D.
+852-2978-0200 | si.fu@gs.com
GS (Asia) L.L.C.

## 1) A-share tech leading the growth

A outpacing H: Aggregate net profits for all listed Chinese companies (\~7,000 names across A, H, and ADRs) delivered a resilient 6% yoy growth in 1Q26 (vs +7% in 2025 and -4% in 4Q25). However, a substantial divergence has emerged among major indices: CSI300 (+9% yoy) significantly outpaced MSCI China (-8% yoy) in 1Q26. The outperformance of A-shares was driven by indices with higher AI hardware exposure, such as ChiNext (+22% yoy) and STAR (+198% yoy). Conversely, the offshore index continues to be weighed down by quick commerce subsidies and rising AI Capex.

■ Sector divergence: SOE profit growth picked up to +7% yoy in 1Q26 (vs. +1% in 2025), while POE growth slowed down to +4% yoy in 1Q26 (from +11% in 2025). At the sector level, upstream and technology sectors maintained robust momentum, led by Materials (+73% yoy), Tech Hardware (+25%), and Energy (+48%). In contrast, growth in consumer and property-related sectors remained subdued, with Retailing (-50%) and Autos (-27%) both contracting sharply.

Looking ahead: We have recently revised down our MSCI China EPS growth forecasts to 8%/12% for 2026/27E, while maintaining our CSI300 EPS growth forecasts at 20%/12%, supported by the ongoing “Soft vs. Hard” tech divide. Consensus estimates for ChiNext and STAR50 also point to robust growth of +34%/+25% and +83%/+60% yoy for 2026/27E, respectively. On a quarterly basis, our top-down model and analysts’ estimates collectively project 0%/+11% earnings growth yoy for MSCI China/CSI300 in the upcoming 2Q26 results season starting in August, reflecting a delayed earnings recovery for offshore mega-caps under the headwinds mentioned above.

Exhibit 1: A-share tech/small-mid caps led year-on-year earnings growth in 1Q26

![](images/eb95270f90d2ba30afa6046e7985529d5848a45bfe878e578f4f3526da2611ec.jpg)  
Source: FactSet, Wind, MSCI, GS Global Investment Research  
Exhibit 2: Better earnings revision trend in A-shares/IT compared to MSCI China/Internet

![](images/747044fc9df9f160b70dd28bc0688f66245209d9a6870b58838b72f9eb476836.jpg)  
Source: FactSet, MSCI, GS Global Investment Research

Exhibit 3: We now expect 8%/12% earnings growth for MSCI China in 2026/27E, below consensus estimates  
![](images/46d32601efe5fcd4059ff9d97426a34ed588d052771b750d2672ba95583cb729.jpg)  
Source: MSCI, FactSet, GS Global Investment Research

Exhibit 4: Profit growth momentum for offshore tech could improve in 2H26 per GS and consensus expectations  
![](images/27d00972a4017ce048edeaa200e1122a33e0c01585f9c93891dd46cb70b2e42b.jpg)  
Source: MSCI, FactSet, GS Global Investment Research  
Exhibit 5: The 1H/2Q26 earnings season will kick off in August

![](images/1f2f72401813036da06e2f7d4d6adb1c6990217acc330833c8f80fb86f3322d8.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 6: Based on our top-down model and analysts estimates, we expect 0%/+11%/+9% earnings growth yoy for MSCI China/CSI300/All China in 2Q26  
![](images/cd72414bbedf0d207c327e881d8be14e307fc26011bd4d947e53830c168b8926.jpg)  
Source: Wind, FactSet, NBS, GS Global Investment Research

## 2) AI profits shifting towards hardware, both globally and domestically

Global AI profit pool: We laid out our global AI equity universe maps in March, covering over 3,700 companies across 29 industries and 5 thematic layers, representing a total market cap of \$42tn. While the US dominates high-margin IP layers, such as IC Design, capturing 66% of global AI earnings, China's share is shrinking from 10% in 2024 to 9% in 2025 and 8% in 1Q26. Other regions (primarily North Asia) have capitalized on advanced foundry and memory demand, growing their global earnings share from 24% in 2024 to 27% in 1Q26. The Chinese AI universe's earnings grew by 10%/35% yoy in 2025/1Q26 (led by upstream hardware, with Chinese Power, Semis, and Infrastructure layers growing 18%/12%/46% in 2025 and 32%/141%/70% in 1Q26, respectively), while the US AI universe's earnings grew by 30%/67% yoy.

Within China's AI supply chain, the profit pool has undergone a pronounced rebound toward hardware (to $54\%$ in 1Q26 vs $41\%$ in 2024). This was particularly evident in semiconductors, with Memory, IC Design, and Materials gaining the most earnings share, while Foundry slightly lost share. Among the power and infrastructure layers, the profit pool shifted toward Data Center, Power Generation, and PCB/CCL. Consequently, AI applications lost share, falling from $59\%$ in 2024 to $46\%$ in 1Q26.

\- Capex drivers: This rebound toward hardware is heavily supported by the massive Capex commitments of major CSPs. As shown in Exhibit 9, US hyperscalers continue to aggressively scale up AI Capex, while Chinese CSPs are also accelerating their spending, providing a visible demand runway for upstream hardware players.

Exhibit 7: China's share in global AI profit pool declined as other regions gained  
![](images/a39bbc710a5c7e9030ebb25d7c81ffbdb821a0d5df325170afd72e2c08977117.jpg)  
Source: FactSet, MSCI, GS Global Investment Research

Exhibit 8: The margin profile for Chinese AI companies still lags global peers  
![](images/d8d19f974b15b13b48ad0e50957929771a75f5a6a3873d9decd436155dc13f3a.jpg)  
Source: FactSet, MSCI, GS Global Investment Research

Exhibit 9: Both US and Chinese hyperscalers keep scaling up AI Capex estimates by GS Internet team (US\$bn)

![](images/aa3c33579023b27ebba60affc6b87f865f28409389a63c374094debf091b0840.jpg)  
Our Internet analysts calculate Bytedance's (Not Covered) relevant operating metrics by analyzing the industry and companies that they cover, and then extrapolating them to Bytedance.

Exhibit 10: The semiconductors layer grew the fastest in the Chinese AI universe in 1Q26  
![](images/7966b72da47d75656ec04cad152afe1c86977d95e17b473b12ae30b3a3cf56e9.jpg)  
Source: FactSet, MSCI, GS Global Investment Research  
Source: Company data, GS Global Investment Research  
Exhibit 11: Within China's AI supply chain, the internal profit pool has undergone a rebound toward hardware

![](images/7254c144285b3b1dd15a127ffa1fcdff1b785b35e3d42b16b06d1f19f31a0644.jpg)  
For definition and weighting methods of the AI universe, please refer to China Strategy | AI changes the game (Part 2): A top-down guide to the Chinese AI universe  
Source: FactSet, MSCI, GS Global Investment Research

## 3) Recovering aggregate revenues but bifurcated margins in “involuted” sectors

■ Revenue acceleration: In 1Q26, the aggregate revenue growth for the listed universe picked up to +4% yoy, up from +1% in 2025 and -1% in 2024. This overall improvement masks a bifurcated sector landscape, characterized by sharp rebounds in cyclicals and tech-heavy sectors (Brokers/IT/Industrial all +15% yoy in 1Q26), a stabilization in consumer staples, and substantial declines in Real Estate.

Margin divergence: The net margin for the listed universe remained stable, ticking up slightly to 9.0% in 1Q26 (from 8.9% in 1Q25). Consumer-facing New Economy/POE and Banks (pressured by narrowing NIM) generally underperformed their Old Economy/SOE counterparts. Among our defined “involuted” sectors, Semiconductors, Industrial Metals, and Airlines (aided by an 8% yoy decline in domestic jet fuel prices in 1Q26) were the primary margin gainers. Conversely, the margin erosion was exacerbated in select consumer sectors (Autos, Agriculture, and E-commerce), Construction Materials (such as Cement and Steel) and Solar Equipment, highlighting a stark divergence between a hard-tech recovery and a consumer/property-linked slowdown. See Exhibit 33 in Appendix for more details.

Exhibit 12: Aggregate revenue growth for the All China universe accelerated to 4% in 1Q26 vs. +1% in 2025  
![](images/4e9e167c7dd4d23f31c6a7f1005ae38a61d01022c52ed394343917bdb95f0e7c.jpg)  
Source: Wind, FactSet, Bloomberg, GS Global Investment Research

Exhibit 13: Mixed margin profile across the “involuted” sectors in 1Q26  
![](images/abbe469d0b9024e9b6f4395a0f9761b76d26931e02bd12132fe976fc4d9b6941.jpg)  
Source: Wind, FactSet, GS Global Investment Research

## 4) "Going Global" is still ongoing

Sustained momentum: Chinese corporate overseas revenue exposure continued its upward trajectory to 18% in 2025 from 16% in 2024. The Auto sector has been the leader of this globalization trend, surging to 29% in 2025 (+8pp vs. 2024 due to rapid EV overseas expansion), and the 1Q26 results for the sector leader confirmed the trend. This globalization trend is increasingly broad-based, with Semiconductors, Transportation, Capital Goods, Durables, and Pharma & Biotech also making inroads. Conversely, Tech Hardware (driven by smartphones) and Energy both declined.

Profitability premium: Most sectors still enjoy better profit margins in overseas markets compared to their domestic operations (as shown in Exhibit 16), providing a strong structural incentive for continued international expansion. In fact, Chinese exporters (>50% overseas exposure) delivered robust growth across both revenue and earnings in 1Q26 (see Exhibit 28 in Appendix), significantly higher than the aggregate listed universe.

FX impact: The FX impact reversed to a net loss of Rmb5.8bn in 2025 from a net gain of Rmb3.3bn in 2024, driven by a slight appreciation of the CNY against the USD (on a full-year average basis). Export-heavy and commodity-related segments (including Industrials, Materials, Energy, and IT) experienced a squeeze, while USD-debt-heavy sectors (such as Airlines) and Consumer Discretionary capitalized on this currency strength.

Exhibit 14: Foreign sales exposure of Chinese listed universe rose further to 18% despite tariff headwinds

![](images/af017972de98db668acd78ca884814c40cc536734272667e0eacaa21534aa3e5.jpg)  
Source: Wind, FactSet, GS Global Investment Research  
Exhibit 15: Autos and Pharma are the leaders in the globalization trend

![](images/fca10f5c836fad49a12c32a201316bdf256f581971bdd718ddc0fce06cef5c92.jpg)  
Source: Wind, FactSet, GS Global Investment Research

Exhibit 16: Most sectors enjoy better profitability in the overseas markets  
![](images/15e01af0b6df633be7087273fd02dc11a1d69e1afc59f9e50619e08071072ff6.jpg)  
Source: Wind, FactSet, GS Global Investment Research

Exhibit 17: A slight FX loss was recorded in 2025 due to CNY appreciation  
![](images/163f5eabecf36b7873d44f0426282742656aad7817bc8e3a78132a4e5ed75b67.jpg)  
Source: FactSet, MSCI, GS Global Investment Research

## 5) Record cash returns along with more R&D and acquisitions

Record-high cash returns driven by dividends: Aggregate dividends distributed by the All-China listed universe aligned with our prior expectations at Rmb3.0tn in 2025. Traditional and SOE-dominated sectors, such as Consumer Staples, Utilities, Financials, and Energy raised their dividend payouts, supported by regulatory directives that encourage higher payout ratios and interim and quarterly dividend distributions.

■ Conversely, share buybacks fell short, totaling Rmb0.4tn (-11% yoy). This decline in buybacks was heavily concentrated in Internet (Retailing and Media), where buyback volume fell 28% in 2025 as companies prioritized AI spending and quick commerce subsidies. Despite lower volumes, net buybacks remain accretive to EPS for existing MSCI China universe (ex-Financials).

Shifts in corporate cash allocation: Beyond shareholder returns, growth investments grew by 3% yoy (vs. -5% in 2024). Sector-level spending varied dramatically underneath a flat Capex (remaining at Rmb6.4tn): Retailing, Tech Hardware, and Media grew by 94%, 22%, and 16% yoy, respectively, whereas Real Estate, Solar Equipment, and Materials declined by 33%, 48%, and 8% yoy, reflecting a disciplined approach to capacity expansion in oversupplied industries. Conversely, cash allocated to acquisitions surged by 46% yoy to Rmb0.7tn, as relaxed regulatory frameworks prompted leading Chinese firms to increasingly prioritize inorganic growth, industry consolidation, and overseas expansion. Meanwhile, R&D spending rose 3% yoy to Rmb2.1tn, driven by sustained corporate commitments to localized technology and AI hardware.

For 2026, we project total shareholder returns to reach Rmb3.8tn, led by a 15% yoy increase in dividends to Rmb3.4tn, which represents a total shareholder yield of 2.9% (vs. 2.7% in 2025). The surge is supported by robust A-share and upstream earnings growth and favorable regulatory tailwinds. Growth investments are also expected to remain flat, with modestly lower Capex (primarily in “involuted” sectors, while remaining strong in Tech Hardware) offset by higher spending on R&D and acquisitions.

All China - Dividend Payout Ratio  
Exhibit 18: Chinese corporates spent more cash on dividends, acquisitions, and R&D in 2025 (Rmb tn/%) All China listed universe - Use of Cash  
![](images/3b5708094a77ab2f04becb7a008d68126a7172ea83303f73912cceed062232e1.jpg)  
Source: FactSet, Wind, GS Global Investment

Exhibit 19: Dividend payout ratio edged up to 39% in 2025  
![](images/cead0c0ffadeddbc06ad04864b6b88fe676654804a71e5964a0b8cc8aff37b49.jpg)  
Source: FactSet, Wind, GS Global Investment

Exhibit 20: Net buybacks remain accretive to EPS despite lower absolute volumes  
![](images/ee59899f6b26a55091dc11cea7df90dad130ab293ecc563c1948041dd6b644ed.jpg)  
Represents the net change in the carrying value of common and preferred stock  
Source: FactSet, MSCI, GS Global Investment Research

6) Key themes from earnings calls: AI and “Going Global”

AI discussion trends: We compiled over 4,500 earnings call transcripts released by Chinese companies and extracted the key themes discussed by management and investors. Overall, approximately 1/4 of companies directly referenced “artificial intelligence” or closely related keywords (such as semiconductors, memory chips, and humanoid robots) on earnings calls. The surge in AI-related discussions has been notable in physical and hardware-heavy sectors, such as Capital Goods, Tech Hardware, and Materials, compared to previous quarters. Conversely, downstream segments experienced a relative moderation.

Sustained focus on globalization: Concurrently, “Going Global” initiatives remained a dominant strategic focus across nearly all manufacturing and hard-tech sectors in 1Q26. Sectors such as Capital Goods, Materials, Tech Hardware, and Biotechnology saw a notable rise in overseas expansion discussions. Direct mentions of tariff headwinds generally moderated or stabilized at lower levels compared to the peaks of 1Q25.

Exhibit 21: AI/Technology and shareholder (returns) were frequently mentioned in listed companies' earnings transcripts.

Exhibit 22: Our textual analysis reveals a notable surge in AI-related discussions within physical and hardware-heavy sectors in A-shares

<table><tr><td rowspan="2">Industry Group</td><td colspan="3">AI</td><td colspan="3">Tariff</td><td colspan="2">Shareholder Returns</td><td colspan="2">Anti-Involution</td><td colspan="2">Going global</td><td rowspan="2" colspan="2">*Ytd Perf</td></tr><tr><td>1Q26</td><td>1H/2Q25</td><td>CY24/1Q25</td><td>1Q26</td><td>1H/2Q25</td><td>CY24/1Q25</td><td>1Q26</td><td>1H/2Q25</td><td>1Q26</td><td>1H/2Q25</td><td>1Q26</td><td>1H/2Q25</td></tr><tr><td>Semis</td><td>3.1</td><td>2.9</td><td>1.4</td><td>0.3</td><td>0.5</td><td>1.3</td><td>0.9</td><td>0.1</td><td>0.7</td><td>0.1</td><td>1.8</td><td>0.4</td><td>28%</td><td></td></tr><tr><td>Tech Hardware</td><td>3.8</td><td>3.2</td><td>2.4</td><td>0.4</td><td>0.6</td><td>2.0</td><td>1.4</td><td>0.1</td><td>0.9</td><td>0.1</td><td>2.7</td><td>0.4</td><td>18%</td><td></td></tr><tr><td>Energy</td><td>0.1</td><td>1.6</td><td>0.2</td><td>0.0</td><td>0.2</td><td>1.1</td><td>0.2</td><td>0.8</td><td>0.1</td><td>0.4</td><td>0.3</td><td>0.2</td><td>12%</td><td></td></tr><tr><td>Utilities</td><td>0.2</td><td>0.6</td><td>0.3</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.6</td><td>0.9</td><td>0.1</td><td>0.1</td><td>0.3</td><td>0.2</td><td>5%</td><td></td></tr><tr><td>Capital Goods</td><td>5.1</td><td>2.6</td><td>0.5</td><td>0.9</td><td>0.8</td><td>1.2</

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
