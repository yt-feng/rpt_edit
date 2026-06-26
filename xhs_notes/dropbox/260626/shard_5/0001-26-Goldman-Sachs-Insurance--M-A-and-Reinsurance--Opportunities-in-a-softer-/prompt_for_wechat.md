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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Insurance: M&A and Reinsurance; Opportunities in a softer rate environment

As premium rate increases slow/soften across a number of classes, we see 1) incremental reinsurance opportunities for insurers to optimise ROEs/Margins + a broad based increase in M&A across the sector, as historically observed, particularly as valuations pull back on businesses materially exposed to classes seeing material rate pressure. In this context, we note that:

Reinsurance markets and excess capital are proving favourable for direct insurers + supply of alternative third party capital which should help support capacity for large scale reinsurance transactions. We think this presents opportunities for IAG's Intermediated business and also for SUN to consider optimising returns across their business. With margins in excess of targets for the personal lines insurers as a result of the hard premium rate cycle, we think IAG / SUN are buying (or have bought) additional reinsurance protections with profit commission terms to help smooth margins by deferring profits into outer years.

□ Japanese non-life insurers (e.g. Tokio Marine) hold significant excess capital supported by divestments of cross-holdings and have publicly flagged International M&A opportunities to diversify their exposures; with Australia noted as an attractive market for growth and diversification. This may present opportunities for both IAG's Commercial business and both SUN/IAG's personal lines businesses; and we highlight the evidence / key points from their strategic disclosures within this report.

\- Across our insurers, IAG is pursuing its acquisition of RACI with SUN flagging potential opportunities in the Commercial space (organic or otherwise). Inwardly, IAG flagged possible reinsurance structures for its Commercial business to release capital (perhaps ROE neutral/ upside) with M&A flagged as not a strategy. Ex the Quota share, and post bank sale, we note that SUN is a pure play general insurer similar to IAG.

\- See within for details.

Julian Braganza, FIAA
+61(2)9321-8487 |
julian.braganza@gs.com
GS Australia Pty Ltd

Chris Matthews, FIAA
+61(2)9321-8370 |
chris.matthews@gs.com
GS Australia Pty Ltd

## Reinsurance: Favourable rate reduction expected in June

1 Apr-26 Renewal backdrop: Risk-adjusted rates fell significantly across US and Asia, returning to early 2020s levels.

1 Jul-26 in Australia is expected to be down between 10-15%; closer to 15% overall: It is likely that this would still not be the bottom for reinsurance rates with reinsurer ROEs still adequate and over-earning long term averages. This could also be supported further if their perils losses are relatively benign.

\- Rate reductions have been the same globally in markets: And have not reflected the starting position of rate adequacy in each of the individual geographies i.e. Every market seems to have a very similar rate reduction across Australia, Africa, and China so rate adequacy today by market may look a little more chequered.

■ Greater competition emerging from 2nd and 3rd Tier reinsurers.

\- Reinsurance demand up \~10%, driven by retention buy-downs, frequency protection, and higher limits/extended CAT (catastrophe) towers. However, with very strong ROEs we think reinsurers are still generating capital in excess of organic growth consumption.

Global reinsurer capital up \~10% to US\$785bn and third-party capital (CAT bonds/insurance-linked securities) up 18%, driven by investor appetite and strong reinsurer retained earnings (ROEs \~17%).

Benign CAT losses reinforce favourable reinsurance trends; significantly higher losses are needed to result in a material shift in pricing.

Exhibit 1: Natural Catastrophe Reinsurance Pricing Cycle as portrayed by Hannover – remains favourable Despite recent rate reduction, reinsurance rates remain very rate adequate.  
![](images/acde8d6336de8a6593e44442d0bb0de8c5e26e2cb22d6d34fd8c021e2048f7ed.jpg)  
Source: Company data

Exhibit 2: Reinsurance sector ROEs

![](images/6cce8fa2f869286a14e6c1c2e7af43f4c0e6f66cfc0d8c3da841ddd6fc0998c3.jpg)  
Source: AON

Exhibit 3: Reinsurance sector capital  
![](images/b725f83aacbdce57f34f716400881d2bc881fb202ea6635ddffbfefc8a8bbf4f.jpg)  
Source: AON

## IAG's Commercial business strategy

IAG restructured the licensing of its Intermediated business to support a potential reinsurance structure: IAG has transferred its intermediated insurance business (covering the CGU and WFI brands) into a standalone subsidiary which operates under its own separate general insurance license.

The problem IAG is trying to address is that the intermediated business has been earning ROEs that are well below Group ROEs of \~15%: IAG's intermediated business has consistently earned returns that is below Group margins / ROE i.e. 11.7% currently v Group of 15%+. With material expense savings, the Intermediated business is expected to get to \~13% insurance margin / ROE which is still below Group with further capital optimisation initiatives needed to support returns.

While we think reinsurance is a potential catalyst for IAG's Intermediated business, IAG could well be exploring a number of options: IAG is targeting a $13\%$ margin on this business v $11.7\%$ at 1H26 currently; largely through expense ratio reductions. We think there is further upside to margin / ROE for this business through a possible reinsurance transaction with M&A not specifically flagged as a strategy by IAG.

Tokio Marine (Not Covered) 2035 Strategy /Plan: M&A a feature

The company's plan targets $7 \%+$ Profit growth CAGR into FY35

\- Geographic diversification targeted through a combination of a) Organic growth b) Business build out c) Small and medium-sized bolt on M&A d) Large M&A.

■ Building out growth opportunities with low correlation to existing business: both across geography and product set to minimise the impact on capital requirement strain resulting in better ROE trends.

\- Targeting a significant improvement in group ROE to 17%+ from \~13% currently. This will also be driven by a combination of reallocating capital from equity stake to higher returning investments offshore, per the company.

■ Stronger presence in Australia targeted.

Exhibit 4: Tokio Marine 2035 ambitions  
![](images/72be0615c3b627a7d8dd578804824094488fc9cd20e9ee1ae93516ca648e9100.jpg)  
Source: Company data

## Tokio Marine /Berkshire Partnership: Collaborating on M&A

Tokio Marine entered into a strategic partnership with Berkshire Hathaway insurance in March this year. The partnership mirrors IAG's own partnership with Berkshire however it also opens up Tokio Marine to large scale M&A in collaboration with Berkshire.

☐ As the foundation of the partnership, Berkshire has taken a stake of 2.5% in Tokio Marine (capped at a maximum of \~10%).

Tokio Marine is also reinsuring a portion of the group insurance portfolio through a Whole of Account Quota Share over a 10 year term. The portion of the reinsurance is undisclosed. This will achieve a reduction in earnings volatility in the insurance portfolio supporting earnigns generation for growth.

Tokio Marine and Berkshire will also look to collaborate on global strategic investment opportunities to drive sustainable growth for both companies. Berkshire is leveraging Tokio Marine's M&A execution capability and Tokio Marine is leveraging Berkshire's capital strength which will significantly broaden M&A options and opportunities.

## Exhibit 5: Tokio Marine Partnership with Berkshire

![](images/37e638222ab90e128cf89624ac0551003f9712a22fd0936c2585c0343ce33c00.jpg)

## Reduction of earnings volatility in the insurance underwriting portfolio (including natural disaster risks) The long-term and stable capacity generated to be deployed toward growth areas Significantly broaden M&A options and opportunities

\*Whole of Account Quota Share arrangement

Source: Company data

## Tokio Marine's M&A strategy

Until recently Tokio Marine's focus was on smaller /unlisted targets with lower multiples. The partnership with Berkshire should provide access to a larger pool of capital.

Tokio Marine will have capital capacity / M&A firepower of up to US\$20bn standalone: Driven by 1) Re-deployment of excess capital post sale of equity investments 2) Optimising balance sheet through use of subordinated debt.

☐ Pipeline extends beyond US\$1bn type acquisitions / bolt-ons to large scale M&A in collaboration with Berkshire.

☐ Preference for unlisted targets noting better multiples and ability to negotiate on price v listed players.

☐ M&A preference for lines that are showing more material softening on rate which has better valuations e.g. Financial lines.

☐ FX /weaker Yen is not an issue noting Tokio Marine earns a good proportion of profits in USD that can be deployed.

Source: Company data, GS Global Investment Research

Exhibit 6: M&A framework and track record  
![](images/3cd5f5cc612e040e736b3c8c890d01729e9ac9fedb6efd68ada672dcdf416d85.jpg)

## Exhibit 7: M&A scotp in Commerical

## Rate Cycle and M&A Opportunities

The current rate cycle has entered the early stage of a softening phase, leading to an increase in M&A activity.  
![](images/eee2f039eb1fb0276421625f774bce340553af7c326dc8c8b16d03a4a687ffe6.jpg)  
\*1: U.S. Commercial market (Source) WTW, Commercial Lines Insurance Pricing Survey  
\*2: Global M&A transactions announced between 2003 and 2025, involving \$100M or more, targeting P&C insurance companies (Source) Dealogic. \*3: Date is the announced date. \*4: FX rate at the time of announcement

Exhibit 8: Tokio Marine historical M&A since 2008 TM has been buying global insurers for two decades

<table><tr><td>Target</td><td>Description</td><td>Year</td><td>Value</td></tr><tr><td>Kiln</td><td>Lloyd&#x27;s of London specialist</td><td>2008</td><td>£442m</td></tr><tr><td>Philadelphia Consolidated</td><td>US property &amp; casualty</td><td>2008</td><td>$4.7bn</td></tr><tr><td>Delphi Financial</td><td>US life, property &amp; casualty</td><td>2012</td><td>$2.7bn</td></tr><tr><td>HCC Insurance</td><td>Global property &amp; casualty</td><td>2015</td><td>$7.5bn</td></tr><tr><td>Privilege Underwriters</td><td>US property &amp; casualty</td><td>2019</td><td>$3.1bn</td></tr></table>

Source: Financial Times, Data compiled by GS Global Investment Research

## M&A Strategy - Sompo (Not Covered)

Remains committed to M&A in P&C: post US\$3.5bn acquisition of global insurance and reinsurance company Aspen in Feb-26.

\- Holds >JPY\$1trn (\~A\$8.9bn) of excess capital for growth: with \~60-70% of this committed for overseas M&A.

■ Sompo is targeting large-scale M&A in P&C, with bolt-on M&A also in view:

☐ Looking for targets with alignment in underwriting philosophies, expansion of scale and diversification and ROI exceeding the cost of capital.

☐ North America and Europe are targeted regions for M&A within Commercial markets.

□ Criteria for overseas P&C M&A: 1) Increasing ROE, 2) Growth potential, profitability, and diversification of existing business, 3) Prioritise Aspen's PMI.

☐ Criteria for domestic P&C M&A: Expanding services from pre-disaster to post-disaster.

Sompo strengthened its presence in the Australian market through the recruitment of 9 specialist underwriters in Apr-26: Underwriters have established expertise across property, casualty, financial lines, energy and construction.

\- Even after the completion of the Aspen acquisition, sufficient capacity for growth investments remains, thanks to the accelerated sale of strategic equity holdings and higher-than-expected earnings
- We will implement growth investments that contribute to early profit generation and sustainable profit growth, thereby enhancing capital efficiency through profit growth

![](images/40a77a9513a3a9f4ce0b1ce54cad662d1676e3a74d73d7158b50255a61ca06b5.jpg)  
Source: Company data

## Exhibit 10: Sompo investments in Future growth plan

## Investments in Future Growth

![](images/98c6c1842af6102b94b4f0dd44c8ade899a4a505a73edda7338997891788eedf.jpg)

Capital Generation and Allocation  
![](images/8c178836f0ef02f2c7489b5798916e01e6486f7276fc315b2a6143976f77f472.jpg)

## M&A Strategy - MS&AD (Not Covered)

MS&AD has said it intends to deploy a portion of the remaining proceeds from its divestment of strategic equity holdings to new business investment & additional M&A - see Exhibit 11: A portion of JPY\$0.7trn (\~A\$6.3bn) will be considered for small to medium-sized bolt-on investments to deepen presence in Asian markets and/ or international life insurance companies.

W.R. Berkley 15% acquisition was completed in Mar-26: JPY\$0.6trn (\~A\$5.4bn) allocated to business investment in WRB.

Appears more tentative on large-scale M&A: On its May-26 guidance call, MS&AD noted that there were no immediate plans to deploy ongoing strategic equity holdings divestments into large-scale business investments, although investments in high growth areas and overseas life will continue to be considered.

Exhibit 11: MS&AD use of strategic equity holdings divestment proceeds
Part of JPY\$0.7trn (\~A\$5.4bn) to be allocated to new business investment and additional acquisitions

## 01 Status of Strategic Equity Holdings Sales and Use of Proceeds

Generally obtained approval from issuers for the sale of strategic shareholdings, and will proceed with the sales ahead of schedule\*1.

The proceeds from these sales will be invested in growth areas with sufficient investment efficiency to achieve 1 trillion yen in adjusted profit at an early stage.

For our own shares that are sold as a result of dissolving cross-shareholdings, we will take measures to address supply and demand, such as off-market transactions.

![](images/6e8b218206b0ac9f87ff993c0525b735a8ddf5db50846993f6a8bcfc3c789493.jpg)

## ■ New business investment & additional acquisitions

– Capital enhancement for growth strategy in the Americas

\- Small- to medium-sized bolt-on investments to deepen presence in Asian markets

– International life insurance with stable and high cash flow, such as corporate pension business

## ■ Investment in organic growth

\- Investment in productivity/innovation (AI, next-gen systems) and top specialists

\- Investment in transforming the business model and structure of domestic life insurance

\- Careful expansion of investments in higher return assets $^{*3}$

## ■ Additional return

\- Share buybacks, considering balance and timing with growth investments

## End of March 2026

\*1 Over 70% of the fair value balance, excluding planned transfers to pure domestic equity investments, is expected to be sold in FY2026 and FY2027.

\*2 Carefully selecting and investing in stocks that are expected to achieve sustainable corporate value growth through profit growth, based on a long-term investment approach.

\*3 Assets held with the expectation of relatively high returns. Refers to pure investments other than ALM-related assets (yen interest rate assets held to match long-term insurance liabilities).

## Commercial vs personal lines ROE and GWP growth

Exhibit 12: Commercial lines insurers - ROE (12m rolling)  
![](images/1694a05d54aae4c72a54d6441d7fd46d0f87cfba0584272c72ace30ea410dd82.jpg)  
(1) Due to accounting standard changes and data collection limitations, Sep-23 data is unavailable. (2) We note that APRA defines commercial line insurers as direct insurers that primarily sell commercial lines business.  
Source: APRA, Data compiled by GS Global Investment Research

Exhibit 13: Personal lines insurers - ROE (12m rolling)  
![](images/b433c936ba7b822aa6ac6f3c9e01a3e938ca0c3fae0fa204b113877941e96838.jpg)  
(1) Due to accounting standard changes and data collection limitations, Sep-23 data is unavailable. (2) APRA defines personal line insurers as direct insurers that primarily sell personal lines business.  
Source: APRA, Data compiled by GS Global Investment Research

Exhibit 14: Direct insurers from large groups - ROE (12m rolling)  
![](images/5943648c660e6b3870a913076422c94041c2e6687577d9bc36f66ad64aad750d.jpg)  
(1) Due to accounting standard changes and data collection limitations, Sep-23 data is unavailable. (2) We note that APRA defines “Direct insurers from large groups” as insurers in a group that makes up at least 10% of industry gross earned premium.

Exhibit 15: Commercial Lines GWP growth (12m rolling) and average  
![](images/e6a1bb7da373a2aff09f17bb2911e3c210de39cbca7a7e7e96865bdbfd83b4c5.jpg)  
(1) Due to accounting standard changes and data collection limitations, Sep-23 data is unavailable and has been estimated. (2) We have built up commercial lines GWP to include Commercial motor, Fire and ISR, Directors and officers, Employers liability, Professional indemnity, Public and product liability, Cyber and Other direct classes

Exhibit 16: Personal Lines GWP growth (12m rolling) and average  
![](images/a9ac778176d890c6e1193457dbd1a1ac47c4db0a2318e76059145a473b29d4cd.jpg)  
(1) Due to accounting standard changes and data collection limitations, Sep-23 data is unavailable and has been estimated. (2) We have built up personal lines GWP to include Home, Motor and CTP classes.  
Source: APRA, Data compiled by GS Global Investment Research

## Price Target, Risks and Methodology - IAG

We are Buy-rated. Our 12-month PT of A\$8.60 is 50% based on our DCF valuation and 50% on a multiple of NTA derived from a regression of P/NTA to sustainable ROTE across our financials coverage universe. Our DCF valuation uses a WACC of 9.5% and a TGR of 2.5%.

Key downside risks include: 1) Rate momentum weakens materially and below loss cost inflation; 2) Volume loss; 3) Persistent claims inflation / perils. 4) Lower investment yields.

## Investment Thesis - IAG

IAG is one of Australia's largest Personal and Commercial insurance companies. We have a Buy rating on IAG relative to the rest of our sector coverage. We like IAG because 1) Margins is in a strong position, 2) IAG is targeting ongoing earnings improvement in its Intermediated Insurance business driven by expense ratios, 3) Catastrophe volatility and reserve protection covers, 4) Greensill de-risked.

## Price Target, Risks and Methodology - Suncorp

We are Neutral-rated. Our 12-month PT of A\$20.00 is based equally on our DCF valuation and a multiple of NTA derived from a regression of P/NTA to sustainable ROTE across our financials coverage universe. Our DCF valuation uses a WACC of 9.5% and a TGR of 2.5%.

Key downside risks: 1) Commercial/Personal Rate increases faster than expected and below loss cost inflation; 2) Significant volume loss to competitors as a result of price increases / ROEs

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
