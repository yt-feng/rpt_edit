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
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Economics - Asia ex-Japan

## Korea: Inflation rises again on higher oil prices while core inflation remains sticky

Research Analysts

As earlier oil price shocks are fading, we expect inflation to gradually ease in Q4 and beyond.

Asia Economics

Jeong Woo Park - NSL

jeongwoo.park@NOM.com

+65 6433 6197

\- Headline CPI rose by $3.2\%$ y-o-y (0.1% m-o-m) in June, up slightly from the $3.1\%$ y-o-y (0.5%) gain in May. The sequential pace slowed sharply from the previous two months, suggesting the June increase was still driven more by earlier cost shocks and base effects than by a broad-based monthly acceleration

\- Core inflation remained sticky rather than accelerating further. CPI excluding food and energy rose by 2.5% y-o-y, unchanged from May. However, its sequential pace also slowed markedly to 0% m-o-m in June from 0.5% in May, which suggests the headline pickup was still concentrated in volatile items, while underlying inflation stayed in the mid-2% range.

\- We reiterate our view that the headline CPI will resume a gradual disinflationary trend after it peaks in August. While falling oil prices are increasing the downside risks to the inflation outlook, we believe a weaker currency and the flexible oil price cap are likely to limit the transmission of lower oil prices. We maintain our 2026 and 2027 inflation forecasts of $2.7\%$ (core inflation: $2.5\%$ ) and $2.1\%$ (core: $2.1\%$ ), respectively.

\- As financial stability concerns are outweighing inflation concerns, we expect the BOK to maintain its hawkish narrative. We maintain our forecast for three 25bp rate hikes (July/October/January; terminal rate: $3.25\%$ ).

## Earlier oil price shocks lifted headline inflation while underlying price trends remained stable

Headline CPI inflation rose to 3.2% y-o-y (0.1% m-o-m) in June from 3.1% (0.5%) in May (Consensus and NOM: 3.2%), the fastest year-on-year pace since late 2023. However, the monthly increase slowed sharply, and core inflation was also stable with CPI excluding food and energy at 2.5% y-o-y (0.0% m-o-m) in June, which suggests the latest pickup was still led mainly by volatile and energy-related items rather than a broad-based acceleration in underlying prices. Indeed, personal service price inflation excluding dining out slowed markedly to 3.9% y-o-y in June from 4.4% in May, with tourism-related item prices reversing its one-off increase in prior months.

That said, headline inflation remained above $3\%$ reflecting higher oil price shock.

By product category (Figure 1):

\- Goods prices rose by $3.8\%$ y-o-y (0.3% m-o-m) in June, led by industrial products at $4.4\%$ y-o-y (0.3% m-o-m). Petroleum product prices were the standout driver, rising by $24.7\%$ y-o-y (0.0% m-o-m) and contributing 0.93ppt to headline inflation (gasoline: $23.1\%$ y-o-y; diesel $33.7\%$ y-o-y; kerosene $23.1\%$ y-o-y).

\- Agricultural, livestock (meat and poultry) and fishery product inflation jumped to $3.2\%$ y-o-y $(0.4\% \mathrm{m - o - m})$ in June from $2.2\%$ $(0\%)$ in May. The pressure was stronger in livestock and fishery products than in crops. Livestock prices increased by $6.2\%$ y-o-y $(1.6\% \mathrm{m - o - m})$ in June, while fishery products rose by $3.7\%$ y-o-y $(0.2\% \mathrm{m - o - m})$ . Agricultural products rose by only $1.1\%$ y-o-y $(-0.4\% \mathrm{m - o - m})$ , with vegetable prices broadly soft on the month.

• Services inflation eased to 2.6% y-o-y (-0.1% m-o-m) in June from 2.8% y-o-y (0.5%) in May. In June, rents rose by 1.0% y-o-y (0.1% m-o-m), public services rose by 1.6% y-o-y (-0.1% m-o-m) and personal services rose by 3.4% y-o-y (-0.2% m-o-m)

. Within personal services, dining-out prices rose by $2.6\%$ y-o-y (0.2% m-o-m), while personal services excluding dining-out rose by $3.9\%$ y-o-y (-0.4% m-o-m).

NOM's view: We maintain our 2026 inflation forecast of $2.7\%$ (core inflation: $2.5\%$ ). Amid falling oil prices, we see growing downside risks to the inflation outlook. However, there are also some offsetting factors to limit the transmission of lower oil prices. Indeed, the flexible fuel price cap has contained the oil price shock, and a weaker currency is likely to partly offset the disinflationary impact from lower oil prices on domestic prices.

Thus, we believe lower oil prices will gradually ease supply-side pressures, and we expect the CPI to peak in August before it resumes a gradual disinflationary trend in Q4, which will likely anchor inflation to the BOK's 2% target in Q2 2027. We maintain our 2026 and 2027 inflation forecasts of 2.7% y-o-y (core inflation: 2.5%) and 2.1% (core inflation: 2.1%), respectively.

## The BOK's hawkish stance remains intact

For the BOK, the June CPI print keeps the case for a hawkish policy stance intact, but it does not by itself prove a broad inflationary reacceleration. The key issue for the July MPC will be whether higher energy and transport costs begin to feed into services prices, wages and inflation expectations.

A headline rate above 3% strengthens the case for caution, but stable core inflation means the policy debate should focus on second-round effects rather than the headline number alone.

While we do not see strong evidence of wage-led/demand-side inflation pressures, we believe it is too early to expect the BOK to alter its policy narrative, as financial stability concerns are outweighing inflation concerns. Thus, we expect the BOK to maintain its hawkish narrative and start rate hikes in July. We maintain our forecast for three 25bp hikes (July/October/January; terminal rate: 3.25%).

Fig. 1: Inflation heatmap

<table><tr><td>% y-o-y</td><td>Weight (%)</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td>CPI</td><td>100.0</td><td>2.0</td><td>2.0</td><td>2.2</td><td>2.6</td><td>3.1</td><td>3.2</td></tr><tr><td>Core CPI (CPI ex food &amp; energy)</td><td>78.2</td><td>2.0</td><td>2.3</td><td>2.2</td><td>2.2</td><td>2.5</td><td>2.5</td></tr><tr><td>Food &amp; Energy</td><td>21.8</td><td>1.9</td><td>1.0</td><td>2.1</td><td>3.9</td><td>5.3</td><td>5.6</td></tr><tr><td>Goods</td><td>44.8</td><td>1.7</td><td>1.2</td><td>1.9</td><td>2.7</td><td>3.5</td><td>3.8</td></tr><tr><td>Agricultural products</td><td>3.8</td><td>0.9</td><td>-1.4</td><td>-5.6</td><td>-5.2</td><td>-0.8</td><td>1.1</td></tr><tr><td>Meat and poultry</td><td>1.4</td><td>4.1</td><td>6.0</td><td>6.2</td><td>5.5</td><td>5.8</td><td>6.2</td></tr><tr><td>Fish and Seafood</td><td>1.1</td><td>5.9</td><td>4.4</td><td>4.4</td><td>4.0</td><td>5.0</td><td>3.7</td></tr><tr><td>Processed food</td><td>8.3</td><td>2.8</td><td>2.1</td><td>1.6</td><td>1.0</td><td>0.8</td><td>0.9</td></tr><tr><td>Durable goods</td><td>8.5</td><td>1.6</td><td>1.5</td><td>2.0</td><td>2.2</td><td>2.4</td><td>3.1</td></tr><tr><td>Clothing</td><td>4.4</td><td>2.2</td><td>2.2</td><td>2.2</td><td>2.2</td><td>2.5</td><td>2.3</td></tr><tr><td>Fuels</td><td>3.9</td><td>0.0</td><td>-2.4</td><td>9.9</td><td>21.9</td><td>24.2</td><td>24.7</td></tr><tr><td>Medicines</td><td>1.6</td><td>-0.2</td><td>-0.4</td><td>-0.4</td><td>-0.4</td><td>-0.5</td><td>-0.5</td></tr><tr><td>Cosmetics</td><td>1.1</td><td>2.4</td><td>3.7</td><td>2.9</td><td>0.7</td><td>0.7</td><td>0.9</td></tr><tr><td>Others</td><td>6.2</td><td>1.3</td><td>1.2</td><td>1.5</td><td>1.0</td><td>1.9</td><td>1.9</td></tr><tr><td>Electricity, Water &amp; Gas</td><td>3.6</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.1</td><td>0.1</td></tr><tr><td>Electricity</td><td>1.6</td><td>-0.4</td><td>-0.4</td><td>-0.4</td><td>-0.4</td><td>-0.4</td><td>-0.4</td></tr><tr><td>Gas</td><td>1.3</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.3</td></tr><tr><td>Services</td><td>55.2</td><td>2.2</td><td>2.6</td><td>2.4</td><td>2.4</td><td>2.8</td><td>2.6</td></tr><tr><td>Housing Rentals</td><td>9.9</td><td>0.9</td><td>0.9</td><td>0.9</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td>Public Services</td><td>12.0</td><td>1.6</td><td>1.6</td><td>1.0</td><td>1.4</td><td>1.8</td><td>1.6</td></tr><tr><td>Personal Services</td><td>33.3</td><td>2.8</td><td>3.5</td><td>3.2</td><td>3.2</td><td>3.7</td><td>3.4</td></tr><tr><td>Dining out</td><td>13.8</td><td>2.9</td><td>2.9</td><td>2.8</td><td>2.6</td><td>2.6</td><td>2.6</td></tr><tr><td>Personal service ex-dining out</td><td>19.5</td><td>2.8</td><td>3.9</td><td>3.5</td><td>3.5</td><td>4.4</td><td>3.9</td></tr></table>

Note: Red colors mean rising inflation; green colors indicate easing inflation. Source: MODS, NOM Global Economics

## Appendix A-1

This report has been produced by NOM Singapore Ltd. (NSL), Singapore.

See Disclaimers for NOM Group entity details.

## Analyst Certification

I, Jeong Woo Park, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms and conditions for availing research services is disclosed on NFASL webpage.

(I) NOM Fiduciary Research & Consulting Co., Ltd. ('NFRC') Tokyo, Japan. (m) NOM Orient International Securities Co., Ltd ("NOI"), is a majority owned joint venture amongst NOM Group, Orient International (Holding) Co., Ltd, and Shanghai Huangpu Investment Holding (Group) Co., Ltd. In accordance with the laws of the People's Republic of China ("PRC", excluding Hong Kong, Macau and Taiwan, for the purpose of this document), NOI is licensed in the PRC to provide securities research and investment recommendations and it operates independently from the other members of the NOM Group; in particular, NOI's interests in PRC securities are not disclosed to, or aggregated with the holdings of, any other NOM Group entities and the interests in PRC securities of other NOM Group entities are not disclosed to, or aggregated with the holdings of, NOI. An individual name printed next to NOI on the front page of a research report indicates that individual is employed by NOI to provide research assistance to NIHK under a research partnership agreement. 'NSFSPL' next to an employee's name on the front page of a research report indicates that the individual is employed by NOM Structured Finance Services Private Limited to provide assistance to certain NOM entities under inter-company agreements. 'Verdhana' next to an individual's name on the front page of a research report indicates that the individual is employed by PT Verdhana Sekuritas Indonesia ('Verdhana') to provide research assistance to NIHK under a research partnership agreement and neither Verdhana nor such individual is licensed outside of Indonesia.

THIS MATERIAL IS: (I) FOR YOUR PRIVATE INFORMATION, AND WE ARE NOT SOLICITING ANY ACTION BASED UPON IT; (II) NOT TO BE CONSTRUED AS AN OFFER TO SELL OR A SOLICITATION OF AN OFFER TO BUY ANY SECURITIES IN ANY JURISDICTION WHERE SUCH OFFER OR SOLICITATION WOULD BE ILLEGAL; AND (III) OTHER THAN DISCLOSURES RELATING TO THE NOM GROUP, BASED UPON INFORMATION FROM SOURCES THAT WE CONSIDER RELIABLE, BUT HAS NOT BEEN INDEPENDENTLY VERIFIED BY NOM GROUP.

Other than disclosures relating to the NOM Group, the NOM Group does not warrant, represent or undertake, express or implied, that the document is fair, accurate, complete, correct, reliable or fit for any particular purpose or merchantable, and to the maximum extent permissible by law and/or regulation, does not accept liability (in negligence or otherwise, and in whole or in part) for any act (or decision not to act) resulting from use of this document and related data. To the maximum extent permissible by law and/or regulation, all warranties and other assurances by the NOM Group are hereby excluded and the NOM Group shall have no liability (in negligence or otherwise, and in whole or in part) for any loss howsoever arising from the use, misuse, or distribution of this material or the information contained in this material or otherwise arising in connection therewith.

Opinions or estimates expressed are current opinions as of the original publication date appearing on this material and the information, including the opinions and estimates contained herein, are subject to change without notice. The NOM Group, however, expressly disclaims any obligation, and therefore is under no duty, to update or revise this document. Any comments or statements made herein are those of the author(s) and may differ from views held by other parties within NOM Group. Clients should consider whether any advice or recommendation in this report is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The NOM Group does not provide tax advice.

The NOM Group, and/or its officers, directors, employees and affiliates, may, to the extent permitted by applicable law and/or regulation, deal as principal, agent, or otherwise, or have long or short positions in, or buy or sell, the securities, commodities or instruments, or options or other derivative instruments based thereon, of issuers or securities mentioned herein. The NOM Group companies may also act as market maker or liquidity provider (within the meaning of applicable regulations in the UK) in the financial instruments of the issuer. Where the activity of market maker is carried out in accordance with the definition given to it by specific laws and regulations of the US or other jurisdictions, this will be separately disclosed within the specific issuer disclosures.

This document may contain information obtained from third parties, including, but not limited to, ratings from credit ratings agencies such as Standard & Poor's. The NOM Group hereby expressly disclaims all representations, warranties or undertakings of originality, fairness,

accuracy, completeness, correctness, merchantability or fitness for a particular purpose with respect to any of the information obtained from third parties contained in this material or otherwise arising in connection therewith, and shall not be liable (in negligence or otherwise, and in whole or in part) for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses,

legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use or misuse of any of the information obtained from third parties contained in this material or otherwise arising in connection therewith. Reproduction and distr

[中间内容因长度限制已省略]

change Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved.
"""
