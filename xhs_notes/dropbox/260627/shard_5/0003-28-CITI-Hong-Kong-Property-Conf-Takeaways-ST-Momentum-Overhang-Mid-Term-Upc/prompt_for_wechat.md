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
- 已识别机构名：`Citi`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Hong Kong Property

## Conf Takeaways: ST Momentum Overhang; Mid-Term Upcycle on Track

## CITI'S TAKE

14 property corporates and global investors (25% based outside HK, vs. 5% last year) attended Citi's Property & Financials Conference. The dominant question was impact of China's ODI regulation on residential as well as office markets – for which listed firms identified no visible impact to date, though some flagged possible short-term volume softening with moderation in home price momentum. Most-attended meetings were SHKP, Hongkong Land and CKA. Many investors have trimmed exposure due to concern on policy execution, higher interest rate expectations, and rotation to other sectors or regions. Investors showed greater focus on company-specific features (DPS, buyback, capital recycling, low-gearing, new IP, new land, etc.) against unfavorable macro beta. We believe sector share prices could remain volatile in Jun-Jul, before the likely strong 1H26 results serve as the next potential catalyst in Aug. Our sector picks are Swire Properties, SHKP, CKA and Link REIT.

Sentiment overhang but no material impact from China's ODI regulation; $< 10\%$ non-HKID buyer; property sits outside of CRS — Despite sentiment overhang, none of the property firms we met observed any measurable impact from China's capital control. Over the past month, there were 1-2 cases of cancellation or extended completion period (by 1 week); yet such are considered normal and consistent with prior experience rather than being linked to the policy. Non-HKID buyers are within $10\%$ per developers (this is in-line with our own analysis through data from Inland Revenue Department). Per our observation, even for projects in Kai Tak (an area popular among mainland buyers), the share of non-HKID holders is $c.15\%$ despite $77\%$ carrying mainland surnames (at Victoria Voyage). We see HK property remains an attractive asset allocation, not only to meet living needs or earn rental yield, but also because it falls outside the scope of China's CRS tax enforcement. According to developers, KYC responsibilities rest with financial institutions or agents, while themselves neither hold direct access to nor maintain confidential personal data.

Moderate home price increase is favorable; temporary volume dip on wait-and-see mood & HSI — 1H26E primary registration of c.12.5k units could become a 21-year high, and secondary volume +35%yoy. In Jun-alone, transaction activities had been quieter, reflecting (1) recent correction in HK equities, (2) buyer hesitation as sentiment is clouded by volatile news flow & may take 1-2 months to stabilize, (3) bad weather conditions, (4) slower launches, (5) narrower room for price negotiation in the secondary market after price recovery. We view such cyclical headwinds as unlikely to alter the mid-term home price upcycle given its anchoring to temporary structural under-supply in 2026-28E (completion 15-18k/year).

Margin recovery visible from 1H results; active for new lands — Clear bottoming-out of development margins should crystallize from 1H results, backed by higher-margin inventory sales (e.g., even Kai Tak can achieve mid-teens OPM after 10-15% price hikes YTD). Sales strategy has been adjusted to seek profit through premium units, while balancing with sell-through for mass projects. Strong property sales drives cashflow & lower gearing – for example, on our estimates, HK sales for SHKP at HK\$37bn in FY26E (vs. target HK\$30bn), Henderson at HK\$17bn in 1H26E (vs. FY25 HK\$19bn). Developers are active in land replenishment (SHKP, Kerry Prop, etc). (Continued)

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations.

Griffin Chan AC

+852-2501-2438

griffin.chan@citi.com

Cindy Li $^{AC}$

+852-2501-2710

cindy.li@citi.com

Upside to Central office rent; smooth leasing at IGC — Spot rent for Central super Grade-A offices have been picking up progressively, underpinned by no new supply and rising enquiries amid re-centralization trend, which clearly favors the bargaining power of landlords. Other districts are generally still digesting supplies with high competition, except Admiralty (benefiting from spill-over demand from Central) and West Kowloon (market share gain on high-quality new supplies). Reversion remains negative but narrowing (e.g., HKLD: est. -5% in '26E and flat in '27E). Project highlights: The Henderson is 95%-let; Central Yards gained privilege to select tenants at its own pace without rush after receiving strong interests, and we think it is on track to be fully committed by 1Q27E; IGC showing decent leasing progress riding on its strong transportation connectivity and a largest floor plate in HK (of 78k sqft), and we believe a reasonably high committed occupancy by 2027E appears achievable; CKC II is approaching 50% commitment.

Retail: tenant sales improving across luxury & non-discretionary; reversion mixed — Tenant sales growth, ranked from high to low, is Mainland China luxury > HK luxury > 10%yoy > HK non-discretionary > 0%. While luxury retail faces a fade-out of favorable base effect in 2H, we suggest that leasing alpha by key landlords should continue to drive outperformance relative to the broader market (e.g., upside post asset reconfiguration at Swire Properties' BJ Sanlitun & SH HKRI Taikoo Hui; brand (re)openings at Hongkong Land's Central Landmark). For reversion, some luxury landlords are expecting negatives in '26E despite good tenant sales due to the high expiring rents (e.g., Harbour City), before turning to positive reversion in '27E. Typical non-luxury malls are seeing less negative retail reversion. Neighborhood malls have spot rent stabilizing, but reversion likely stays at negative high-single-digit magnitude throughout '26E.

## Company-specific takeaways

## Developers:

■ SHKP: DPS growth on earnings; FY26E HK sales at HK\$37bn; DP margin back to mid-teens in FY26E (1H: 8%) & further recovery in FY27E.

■ CKA: possibility for a “small candy” special dividend at interim; DPS growth via earnings and favor dividend more than buyback; 30% threshold margin for new lands; Victoria Blossom will launch in 2H26E.

■ Henderson: govt land resumption likely resumes from mid-27E; stable interim DPS after FY25 result; DP margin recovering to high-teens (incl. the Legacy; excl: mid-teens) in 1H26E (FY25: 8%).

■ Sino Land: La Mirabelle strong sales; new investment targeting land, student accommodation and Fullerton-brand hotel; continue to assess & explore buyback option.

■ Kerry Properties: YTD HK sales HK\$4.5bn+ (1H25: HK\$5.5bn); YTD acquire 3 land sites (20%+ EBITDA margin); look for <30% gearing by end-26E.

## Landlords:

■ Swire Properties: mainland China mall SSSG sustaining 10%+ into Apr-May; PP office spot rent stabilizing and room for less negative reversion.

■ Hongkong Land: HK office reversion -5% in '26E & flat in '27E, see spot rent upside; exploring SG office investment opportunity; portfolio-centric internal optimization for est. US\$40-50m annual cost savings from '27E.

■ Hang Lung Prop: mainland China mall SSSG at teens in Apr & May (vs. 1Q: +24%); HK retail SSSG +ve; CN office keeping occupancy despite -ve reversion.

■ Wharf REIC: expect good May SSSG data; retail recovery could bring reversion back to positive from early 2027E; decision on Marco Polo hotel to be made by end-26E with potential to double GFA if redeveloped.

■ Hysan: 5M25 tenant sales up high-teens yoy; office occupancy stable & mid-teens negative reversion; LG8 OP in early 4Q26E.

## REITs:

\- Link REIT: look for flattish DPU via cost savings and buybacks despite -ve reversion; tenant sales recovering; potential divestment of 100 Market Street and UK office ongoing; ST priority on disposal, HK biz & buyback.

■ Fortune REIT: narrowing negative reversion; supermarket sales at mild growth in 1Q26; refinancing with HK\$3.8bn sustainability-lined loans.

■ Champion REIT: spot rent c.HK\$70s vs. passing rent HK\$73 vs. expiring rent HK\$80s; yoy stable occupancy; Langham mall retail sales at LSD growth.

Figure 1. HK Property Sector — Valuations (25-Jun-2026 close) Citi Rating: 1 – Buy; 2 – Neutral; 3 – Sell; H – High Risk

<table><tr><td rowspan="2">Stock</td><td rowspan="2">RIC</td><td rowspan="2">25-Jun-26 Price</td><td rowspan="2">Mkt Cap (USDm)</td><td rowspan="2">Citi Rating</td><td rowspan="2">Est. NAV</td><td rowspan="2">NAV Disc</td><td rowspan="2">Target Price</td><td colspan="3">P/E</td><td colspan="3">P/B</td><td colspan="3">Yield</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Wharf</td><td>0004.HK</td><td>18.46</td><td>7,195</td><td>3</td><td>47.00</td><td>-61%</td><td>21.15</td><td>13.5</td><td>13.3</td><td>12.6</td><td>0.4</td><td>0.4</td><td>0.4</td><td>2.2%</td><td>2.2%</td><td>2.2%</td></tr><tr><td>Henderson Land</td><td>0012.HK</td><td>25.82</td><td>15,943</td><td>1</td><td>57.00</td><td>-55%</td><td>34.20</td><td>17.3</td><td>15.5</td><td>14.2</td><td>0.4</td><td>0.4</td><td>0.4</td><td>4.9%</td><td>4.9%</td><td>4.9%</td></tr><tr><td>Hysan</td><td>0014.HK</td><td>17.02</td><td>2,229</td><td>1</td><td>45.74</td><td>-63%</td><td>24.30</td><td>12.4</td><td>11.8</td><td>11.4</td><td>0.3</td><td>0.3</td><td>0.3</td><td>6.3%</td><td>6.3%</td><td>6.3%</td></tr><tr><td>SHK Properties</td><td>0016.HK</td><td>116.90</td><td>43,204</td><td>1</td><td>210.00</td><td>-44%</td><td>168.00</td><td>15.0</td><td>14.0</td><td>12.8</td><td>0.5</td><td>0.5</td><td>0.5</td><td>3.3%</td><td>3.6%</td><td>3.8%</td></tr><tr><td>New World Dev</td><td>0017.HK</td><td>6.88</td><td>2,208</td><td>2</td><td>22.65</td><td>-70%</td><td>11.32</td><td>NM</td><td>NM</td><td>22.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Sino Land</td><td>0083.HK</td><td>10.55</td><td>12,899</td><td>1</td><td>18.93</td><td>-44%</td><td>14.20</td><td>19.5</td><td>19.2</td><td>18.3</td><td>0.6</td><td>0.6</td><td>0.6</td><td>5.5%</td><td>5.5%</td><td>5.5%</td></tr><tr><td>Hang Lung Ppt</td><td>0101.HK</td><td>7.24</td><td>4,804</td><td>1</td><td>27.99</td><td>-74%</td><td>11.20</td><td>11.6</td><td>10.9</td><td>10.4</td><td>0.3</td><td>0.3</td><td>0.3</td><td>7.2%</td><td>7.2%</td><td>7.2%</td></tr><tr><td>Kerry Prop</td><td>0683.HK</td><td>18.56</td><td>3,435</td><td>1</td><td>63.87</td><td>-71%</td><td>25.55</td><td>11.0</td><td>7.1</td><td>4.5</td><td>0.3</td><td>0.3</td><td>0.2</td><td>7.3%</td><td>7.3%</td><td>7.3%</td></tr><tr><td>Fortune REIT</td><td>0778.HK</td><td>4.52</td><td>1,189</td><td>1</td><td>10.37</td><td>-56%</td><td>6.00</td><td>15.6</td><td>16.4</td><td>16.5</td><td>0.4</td><td>0.4</td><td>0.4</td><td>7.4%</td><td>7.1%</td><td>7.1%</td></tr><tr><td>Link REIT</td><td>0823.HK</td><td>36.18</td><td>11,993</td><td>1</td><td>55.96</td><td>-35%</td><td>44.80</td><td>14.2</td><td>14.6</td><td>14.6</td><td>0.6</td><td>0.6</td><td>0.6</td><td>7.0%</td><td>6.9%</td><td>6.8%</td></tr><tr><td>CK Asset</td><td>1113.HK</td><td>44.62</td><td>19,917</td><td>1</td><td>99.18</td><td>-55%</td><td>54.80</td><td>12.7</td><td>12.5</td><td>11.7</td><td>0.4</td><td>0.4</td><td>0.4</td><td>4.1%</td><td>4.2%</td><td>4.4%</td></tr><tr><td>Sw ire Properties</td><td>1972.HK</td><td>21.00</td><td>15,420</td><td>1</td><td>51.59</td><td>-60%</td><td>28.80</td><td>16.1</td><td>12.6</td><td>12.4</td><td>0.4</td><td>0.4</td><td>0.4</td><td>5.8%</td><td>6.0%</td><td>6.3%</td></tr><tr><td>Wharf REIC</td><td>1997.HK</td><td>22.56</td><td>8,736</td><td>1</td><td>57.45</td><td>-61%</td><td>31.60</td><td>11.0</td><td>10.8</td><td>10.5</td><td>0.4</td><td>0.4</td><td>0.4</td><td>5.9%</td><td>6.0%</td><td>6.2%</td></tr><tr><td>Champion REIT</td><td>2778.HK</td><td>2.12</td><td>1,664</td><td>3</td><td>5.09</td><td>-60%</td><td>2.03</td><td>15.8</td><td>16.1</td><td>16.0</td><td>0.3</td><td>0.3</td><td>0.3</td><td>5.7%</td><td>5.6%</td><td>5.6%</td></tr><tr><td>Hongkong Land</td><td>HKLD.SI</td><td>7.28</td><td>15,589</td><td>1</td><td>14.86</td><td>-51%</td><td>9.88</td><td>33.9</td><td>29.8</td><td>24.6</td><td>0.5</td><td>0.5</td><td>0.5</td><td>3.6%</td><td>3.8%</td><td>4.1%</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td>-48%</td><td></td><td>15.9</td><td>16.2</td><td>17.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>4.5%</td><td>4.6%</td><td>4.8%</td></tr></table>

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>The Firm has made a market in the publicly traded equity securities of New World Development Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of CK Asset Holdings Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Henderson Land Development Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Sun Hung Kai Properties Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Link Real Estate Investment Trust on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from New World Development,SHK Properties.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from CK Asset,Champion REIT,Hang Lung Props,Henderson Land,Hongkong Land,Kerry Props,Link REIT,New World Development,SHK Properties,Swire Properties,Wharf (Holdings),Wharf REIC in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): New World Development,SHK Properties.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: CK Asset,Champion REIT,Hongkong Land,Link REIT,New World Development,SHK Properties,Swire Properties.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: CK Asset,Champion REIT,Hang Lung Props,Henderson Land,Hongkong Land,Kerry Props,Link REIT,New World Development,SHK Properties,Swire Properties,Wharf (Holdings),Wharf REIC.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to SHK Properties. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr></table>

The Firm is a market maker in the publicly traded equity securities of CK Asset, Henderson Land, Link REIT, New World Development, SHK Properties.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.
For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013,

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective

investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
