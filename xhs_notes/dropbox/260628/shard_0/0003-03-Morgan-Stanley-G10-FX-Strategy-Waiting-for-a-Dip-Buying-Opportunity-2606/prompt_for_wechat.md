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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Waiting for a Dip-Buying Opportunity

USD/JPY is again approaching the July 2024 high, but the rally has been driven more by broad USD strength rather than broad JPY weakness, suggesting that MoF's intervention may not be imminent. We see USD/JPY as close to fair value. We remain neutral on USD/JPY and await a clearer entry point for dip-buying.

## Key Takeaways

The USD/JPY rally has shifted from yen weakness to broad USD strength. This distinction matters for intervention risk, as authorities are typically more sensitive to speculative yen selling than to generalized USD appreciation.

Intervention risk has increased, but imminent action does not yet appear likely. The MoF has stepped up verbal warnings, but has not yet characterized recent FX moves as clearly “speculative.”

USD/JPY looks close to fair value on our three-factor framework. The key inputs remain US terminal-rate pricing, global risk sentiment, and Japan's terms of trade.

■ Lower oil prices and weak global risk sentiment are supportive for the yen outside USD crosses.

We remain neutral on JPY given the concern for the potential intervention and await a clearer dip-buying opportunity.

Koichi Sugisaki
Strategist
Koichi.Sugisaki@morganstanleymufg.com +81 3 6836-8428

MS & CO. INTERNATIONAL PLC+

David S. Adams, CFA
Strategist
David.S.Adams@morganstanley.com +44 20 7425-3518

MS & CO. LLC

Andrew M Watrous
Strategist
Andrew.Watrous@morganstanley.com +1 212 761-5287

Molly Nickolin
Strategist
Molly.Nickolin@morganstanley.com +1 212 761-3592

MS MUFG SECURITIES CO., LTD.+

Hiromu Uezato
Strategist
Hiromu.Uezato@morganstanleymufg.com +81 3 6836-8431

## Currency & Foreign Exchange

## Japan | Waiting for a dip-buying opportunity

MS MUFG SECURITIES CO., LTD.

Koichi Sugisaki
Koichi.Sugisaki@morganstanleymufg.com +81 3 6836-8428

MS & CO. INTERNATIONAL PLC

David S. Adams, CFA
David.S.Adams@morganstanley.com +44 20 7425-3518

MS & CO. LLC

Andrew.Watrous@morganstanley.com +1 212 761-5287

Molly Nickolin
molly.nickolin@morganstanley.com +1 212 761-3592

MS MUFG SECURITIES CO., LTD.

Hiromu Uezato
hiromu.uezato@morganstanleymufg.com
+81 3 6836-8431

## Still range-bound market

Following the MoF's FX intervention from late April to early May, USD/JPY briefly declined to the 155 area. Since then, however, the pair has gradually retraced the decline and is now approaching the 161.95 high reached on July 3, 2024.

That said, the dynamics behind USD/JPY appear to have shifted. From late February, when Middle East tensions began to intensify, until the MoF intervention, the USD/JPY rally was driven mainly by yen weakness. Post-intervention, the rally has instead been led more by broad USD strength (see Exhibit 1).

As shown in "What could change the weaker JPY trend?", the period into May was largely characterized by what our USD framework defines as a "Carry Regime", in which US real rates and breakevens rise simultaneously (see Exhibit 2).

Even after the temporary ceasefire in early April, inflation concerns remained elevated amid ongoing disruption to the Strait of Hormuz. At the same time, US economic data continued to look resilient despite Middle East tensions, while financial conditions stayed supportive.

Since mid-May, the regime appears to have broadly shifted to a "USD Bullish Regime", where US real rates rise, but breakeven fall. As the Middle East situation moved toward an agreement, oil prices declined and inflation concerns eased. At the same time, a more hawkish FOMC stance and weakness in AI-related equities weighed on risk sentiment.

Exhibit 1: G10 FX spot performance: From Middle East tension to MoF's intervention versus after MoF's intervention to date  
![](images/31a7babc1dc190f863d473494fee446d05a24281c594e0994fbfd19a3c493cc8.jpg)  
Source: MS, Bloomberg

Exhibit 2: US breakeven versus real yield  
![](images/8db900466620415fce6f1a8296e5e9e961660700984dcf07995d67666a0cdce3.jpg)  
Source: MS, Bloomberg

In the former regime, JPY tends to underperform the most, given its role as a funding currency. In the latter regime, JPY tends to underperform USD but is more likely to outperform risk-sensitive currencies (see Prepare for the Defense Regime). Recent JPY performance has broadly been consistent with this regime framework.

As discussed in "What could change the weaker JPY trend?", recent USD/JPY moves can be largely explained by three factors: 1) market pricing of the US terminal rate; 2) global risk sentiment, as proxied by the relative performance of equities and bonds; and 3) Japan's terms of trade.

At the current juncture, the US and Iran have agreed on a memorandum of understanding toward a long-term ceasefire, and the Strait of Hormuz appears to be moving toward reopening, albeit potentially on a time-limited basis. The resulting decline in oil prices has supported an improvement in Japan's terms of trade (see Exhibit 3).

As our economists have also noted, moreover, compared with 2022, the pass-through of AI-related component export prices has been smoother. As a result, Japan's terms of trade have not deteriorated as much as they did during the previous commodity shock.

We think these factors help explain why the JPY has recently shown relatively resilient performance against currencies other than the USD.

That said, following the hawkish FOMC outcome, markets have started to price not only a Fed hold but even the possibility of renewed rate hikes. Against this backdrop, the current level of USD/JPY looks close to the fair value implied by these three factors (see Exhibit 4).

Exhibit 3: Japan's terms of trade versus energy prices  
![](images/0e8b13389bae2ff2496c9a156a54f82e51ba0ac726a69d6c439be90ff9f6d2ff.jpg)  
Source: MS, Bloomberg, CITI

Exhibit 4: USD/JPY versus its fair value (US terminal rate pricing, global risk sentiment, and Japan's terms of trade)  
![](images/9344389494f2094c1b118ccde45fe86945718931e2fbc598fffa043e0391c368.jpg)  
Source: MS, Bloomberg Note: \*Global Risk Demand Index is a proprietary index of risk appetite. US Pat. No. 7,617,143.

As discussed below, the MoF has strengthened its verbal warnings in response to the recent USD/JPY rally. In particular, as Japan's MoF emphasizes policy coordination with the US, the risk of coordinated intervention is likely to remain in investors' minds. This may limit the extent to which USD/JPY can move materially above fair value, in our view.

At the same time, we do not expect a large downward revision to USD/JPY fair value either. For fair value to move materially lower, two conditions would likely need to occur simultaneously: 1) markets would need to price aggressive Fed cuts; and 2) global risk sentiment would need to deteriorate significantly, with bonds sharply outperforming equities.

Such a combination would be consistent with the "Defense Regime" in our USD framework, characterized by simultaneous declines in US real rates and breakevens. More generally, it is a regime in which a sharp slowdown in US demand brings disinflation into focus and leads markets to price substantial Fed easing.

At present, US growth and labor-market data remain resilient. Middle East tensions are also easing following the US-Iran MOU aimed at a long-term ceasefire. Our US economists expect the decline in oil-price risk and the lower probability of a near-term energy-driven inflation shock to limit second-round effects and support real income.

In this environment, a near-term US recession appears unlikely. A more plausible downside scenario would involve emerging profitability concerns around the AI sector, leading to a sharp slowdown in AI-related capex – an important driver of growth – and exerting downward pressure on risk markets.

For these reasons, we maintain a neutral stance on USD/JPY and await a clearer dip-buying opportunity, particularly in the event of a potential MoF intervention.

## Possibility of FX intervention

As noted above, USD/JPY has moved closer to the 161.95 high reached in 2024, and investor questions about another round of FX intervention have started to increase again.

From the perspective of the FX level alone, intervention at any time would not be surprising. However, based on recent comments from senior MoF officials, actual intervention still appears some distance away.

Finance Minister Katayama has stated that the authorities stand ready to take decisive action at any time if necessary. However, recent remarks have not included language that clearly defines current FX moves as “speculative.”

Historically, FX intervention has tended to be implemented after authorities confirm that positions are significantly skewed in one direction and deemed speculative, in order to maximize the effect of intervention (see Exhibit 5 and Exhibit 6).

Exhibit 5: History of recent FX intervention

<table><tr><td>Period</td><td>Actual Intervention</td><td>Messages from officials immediately before the intervention</td></tr><tr><td>March 17–18, 2011</td><td>Yen-selling intervention through G7 coordination in response to the yen&#x27;s sharp appreciation after the Great East Japan Earthquake.</td><td rowspan="3">The G7 statement explicitly stated that, in response to movements in the yen exchange rate associated with the events in Japan, coordinated intervention would be conducted on March 18 at Japan&#x27;s request. It also stated that &quot;excess volatility and disorderly movements in exchange rates have adverse implications for economic and financial stability.&quot;After the yen hit a record high against the dollar, Finance Minister Azumi said he would take &quot;decisive action&quot; againstspeculative moves. On October 24, he also said that the authorities would respond decisively to excessive and speculative FX moves, and that the yen&#x27;s strength did not reflect fundamentals.On September 14, it was reported that the authorities conducted a rate check in response to the yen&#x27;s depreciation. Finance Minister Suzuki described recent moves as &quot;rapid and one-sided,&quot;including speculative activity, and stated that authorities would respond &quot;without ruling out any options&quot; if such moves continued.</td></tr><tr><td>31 October 2011</td><td>Yen-selling intervention</td></tr><tr><td>September 14–22, 2022</td><td>Yen-buying intervention (JPY 2.8382 trillion)</td></tr><tr><td>October 20–24, 2022</td><td>Yen-buying intervention JPY 5.6202 trillion on October 21, and JPY 729.6 billion on October 24.</td><td>On October 20, after the yen broke through 150 against the dollar, Vice Finance Minister for International Affairs Kanda stated that excessive volatility was becoming increasingly unacceptable and that authorities stood ready to act. Finance Minister Suzuki also describedspeculative-drivenmovesas &quot;unacceptable&quot; and reiterated that authorities would take &quot;decisive action&quot; if necessary.</td></tr></table>

Source: Japan MoF, Various Media article, MS

Exhibit 6: History of recent FX intervention

<table><tr><td>Period</td><td>Actual Intervention</td><td>Messages from officials immediately before the intervention</td></tr><tr><td>March 27-April 29, 2024</td><td>Yen-buying intervention JPY 5.9185 trillion on April 29, and JPY 3.87 trillion on May 1st.</td><td>Immediately before the April 29, 2024 intervention, Kanda described market moves as “speculative, rapid, and abnormal,” and stated that they could not be overlooked.</td></tr><tr><td>Late June-July 12, 2024</td><td>Yen-buying intervention JPY 3.1678 trillion on July 11, and JPY 2.367 trillion on July 12.</td><td>On June 26, Vice Finance Minister Kanda said that he was “seriously concerned” about the yen’s sharp decline and was monitoring developments with a “high sense of urgency.” On July 12, he reiterated that the authorities would act in the FX market as needed, while Chief Cabinet Secretary Hayashi also stated that the government was prepared to take “all possible measures” on FX.</td></tr><tr><td>Around April 30, 2026</td><td>Total intervention amounted to JPY 11.7349 trillion between April 28 and May 27</td><td>On April 30, Finance Minister Katayama said that the time for “decisive action” was approaching. Vice Finance Minister for International Affairs Mimura reportedly described the message to speculators as a “final warning to get out.”</td></tr></table>

Source: Japan MoF, Various Media article, MS

CFTC data suggest that speculative JPY short positions have continued to build after the previous intervention (see Exhibit 7). In the spot market, overseas non-residents also appear to maintain strong demand for yen funding through FX swaps and related channels (see Exhibit 8).

Even so, since the late-April intervention, the rise in USD/JPY has been driven mainly by broad USD strength (see Exhibit 1). The JPY has, in fact, outperformed other G10 currencies excluding the USD. This price action may indicate that the authorities are not yet fully convinced that speculative JPY shorts have become excessive.

If USD/JPY were to rise sharply from here on the back of renewed JPY weakness, we think the MoF may be more likely to characterize the move as “speculative.” In that case, the likelihood of FX intervention could rise.

![](images/34693736eb50daf0c8074c9e1bbe8229a2f106f254f1339b7404554c05088ddd.jpg)  
Source: CFTC, MS

Exhibit 8: Funding needs for JPY via offshore non-bank financial sectors  
![](images/ceb525467e30cb423282285a9cc6ae177fb5851b9a9ed5f7f32a3552a932c3a0.jpg)  
- Fx swap/forward notional amount (JPY, with non-Bank sector)
- JPY loan to overseas non-Bank sector,RHS  
Source: BIS, MS

Important note regarding economic sanctions. This report references jurisdictions which may be the subject of economic sanctions. Readers are solely responsible for ensuring that their investment activities are carried out in compliance with applicable laws.

## Global Macro Strategy Team

<table><tr><td>MS &amp; CO. LLC</td><td>Matthew Hornbach, CMT Matthew.Hornbach@morganstanley.com</td><td>Global Head of Macro Strategy</td><td>+1 212 761-1837</td></tr><tr><td></td><td>Martin Tobias, CFA, CMT</td><td>US Rates Strategist</td><td>+1 212 761-6076</td></tr><tr><td></td><td>Shaun Zhou</td><td>US Rates Strategist</td><td>+1 212 761-3348</td></tr><tr><td></td><td>Aryaman Singh</td><td>US Rates Strategist</td><td>+1 212 761-1993</td></tr><tr><td></td><td>Eli Carter</td><td>US Rates Strategist</td><td>+1 212 761-4703</td></tr><tr><td>MS &amp; CO. LLC</td><td>Andrew Watrous</td><td>G10 FX Strategist</td><td>+1 212 761-5287</td></tr><tr><td></td><td>Molly Nickolin</td><td>G10 FX Strategist</td><td>+1 212 761-3592</td></tr><tr><td></td><td>Simon Waever Simon.Waever@morganstanley.com</td><td>Head of EM Sovereign Credit and Latin America Fixed Income Strategy</td><td>+1 212 296-8101</td></tr><tr><td></td><td>Ioana Zamfir</td><td>Latin America Macro Strategist</td><td>+1 212 761-4012</td></tr><tr><td></td><td>Emma Cerda</td><td>Latin America Sovereign Credit</td><td>+1 212 761-2344</td></tr><tr><td></td><td>Sofia Palacios</td><td>Latin America Sovereign Credit</td><td>+1 212 761-0428</td></tr><tr><td>MS &amp; CO. INTERNATIONAL PLC</td><td>James K. Lord James.Lord@morganstanley.com</td><td>Global Head of FXEM Strategy</td><td>+44 20 7677-3254</td></tr><tr><td></td><td>Gianluca Salford Luca.Salford@morganstanley.com</td><td>Head of European Rates Strategy</td><td>+44 20 7677-1337</td></tr><tr><td></td><td>Fabio Bassanin, CFA</td><td>UK Rates Strategist</td><td>+44 20 7425-1869</td></tr><tr><td></td><td>Maria Chiara Russo</td><td>Euro Area Rates Strategist</td><td>+44 20 7677-3499</td></tr><tr><td></td><td>David S. Adams, CFA David.S.Adams@morganstanley.com</td><td>Head of G10 FX Strategy</td><td>+44 20 7425-3518</td></tr><tr><td></td><td>Neville Mandimika</td><td>CEEMEA Sovereign Credit Strategist</td><td>+44 20 7425-2509</td></tr><tr><td></td><td>Arnav Gupta</td><td>CEEMEA Rates Strategist</td><td>+44 20 7677-0382</td></tr><tr><td>MS ASIA LIMITED+</td><td>Gek Teng Khoo</td><td>AXJ Macro Strategist</td><td>+852 3963-0303</td></tr><tr><td>MS INDIA COMPANY PRIVATE LIMITED</td><td>Nimish Prabhune</td><td>AXJ Macro Strategist</td><td>+91 22 6996-1862</td></tr><tr><td>MS MUFG SECURITIES CO., LTD.</td><td>Koichi Sugisaki Koichi.Sugisaki@morganstanleymufg.com</td><td>Head of Japan Macro Strategy</td><td>+81 3 6836-8428</td></tr><tr><td></td><td>Hiromu Uezato</td><td>Japan Macro Strategist</td><td>+81 3 6836-8431</td></tr></table>

## Disclosure Section

The information and opinions in MS were prepared by MS MUFG Securities Co., Ltd. and its affiliates (collectively, "MS").

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: David S. Adams, CFA; Molly Nickolin; Koichi Sugisaki; Hiromu Uezato; Andrew M Watrous.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

The e

[中间内容因长度限制已省略]

ficer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.
The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Molly Nickolin; David S. Adams, CFA; Andrew M Watrous; Koichi Sugisaki; Hiromu Uezato.

© 2026 MS
"""
