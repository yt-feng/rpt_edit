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
# Multi-Industry: 3rd Industrials trip to HVAC InstallerSHOW: Key takeaways

We hosted meetings with five HVAC equipment suppliers and the Director General of the European Heat Pump Association (EHPA) on our field trip to the InstallerSHOW in Birmingham on 24th June 2026. Our key takeaways are:

Christian Hinderaker, CFA +44(20)7774-7366 | christian.hinderaker@gs.com GS International

1. Global warming is likely, in our view, to drive further adoption of air-to-air (ATA) heat pumps in the UK and Europe. This reflects their capability as both a heating and cooling technology, as well as the ambitions of a number of HVAC OEMs that are seeking to broaden their product ranges in response to installers' feedback and their need to achieve economies of scale. We expect innovations in the ATA segment to be a particular focus for the market over the next year, including from NIBE which recently announced its entry into this segment (where it had never had a presence) and Viessmann, which announced the UK launch of its Vitocal 200-A today at the InstallerSHOW.

2. The UK heat pump market has significant long-term growth potential, with recent policy changes likely to provide a near-term boost in demand. Though heat pump (HP) adoption remains low compared to the >1.8m gas boilers sold each year, UK HP sales grew +27% YoY to c.125k units in 2025. With penetration at ≤1% of all households there is substantial room for long-term growth, supported by policy measures and consumers' desire to reduce their energy costs. The Government's Warm Homes Plan is targeting c.450,000 annual installations by 2030, with support from subsidy measures such as the Boiler Upgrade Scheme (BUS), which provides grants to consumers replacing existing fossil fuel heating with low-carbon heating systems. The BUS scheme provides £7,500 towards the cost of an air-source heat pump (ASHP) or ground source heat pump (GSHP) installation. Additionally, the scheme recently saw an expansion in scope to include exhaust air heat pumps (a positive for NIBE), while grants of £2,500 will also become available for ATA HPs later this year. From 21 $^{st}$ July, homeowners with off-gas grid properties currently heated by oil or LPG will be eligible for a £1,500 uplift for the installation of ASHPs/GSHPs.

3. Competition, particularly from Chinese suppliers, remains fierce: The UK market continues to be dominated by SME installers which largely procure through the trade merchants. This is seen as one of the key competitive moats for the European OEMs. We note, however, that there has been an incremental move towards D2C models in recent years, including via partnerships with utility

Hollie Cooper  
+44(20)7051-0956 |  
hollie.cooper@gs.com  
GS International

suppliers, such as that between British Gas and NIBE. Broader competitive pressures from Asian manufacturers and other players (such as Octopus Energy and PE-backed OEMs) persist. In the case of the Chinese HVAC OEMs and other new entrants, these players typically seek to differentiate through lower-cost models or direct-to-consumer sales, potentially putting pressure on margins over the long term, in our view. At the same time, OEMs from other parts of Asia (such as Daikin, Mitsubishi, or Samsung) are looking to compete through technology-leadership.

More details and key takeaways by companies below.

## European Heat Pump Association

We met with the Director General of the European Heat Pump Association (EHPA), Mr Paul Kenny. Our key takeaways are:

The EHPA expects to see further market consolidation over the coming years. Mr Kenny highlighted that: (1) heat pump OEMs significantly outnumber the companies manufacturing key components. As an example, Mr Kenny noted that there are four main global suppliers for compressors, which comprise some 20-25% of the overall value in a HP, (2) Expanding access to European heating markets remains an ambition of a number of OEMs in Asia and North America, and (3) Economies of scale require annual production volumes of >500k for companies to remain competitive.

Chinese competition remains a growing threat to European producers: In line with point 1 and with trends seen across other industrial end-markets, Asian OEMs continue to seek market share gains across Europe, where the EHPA expect HP volumes to show another year of LDD growth in 2026.

HVAC OEMs are broadening their product ranges in response to installers' feedback and the need to scale. Companies that have historical strengths in a specific product are increasingly looking at expansion into new categories to ensure they can supply their installer customers with options for different consumer needs. Consistent with the market consolidation trend, there is also a drive to increase economies of scale through expansion into ancillary product areas. As an example, NIBE recently announced its entry into the air-to-air HP market, which it had historically shunned. Amidst a week of extraordinarily high temperatures across the UK and Europe, the dual function of air-to-air HPs as a technology for both heating and cooling was a particular focus of discussions at the InstallerSHOW. The UK central heating has traditionally been designed around “wet” circuits and air-to-air heat pumps therefore represented <10% of the systems sold in the UK in 2025. However, Mr. Kenny believes that this could change over time, highlighting that the European air-to-air market is c.6x larger than the air-to-water market. A number of new air-to-air systems were being showcased at the event.

The EHPA continues to champion increased heat pump adoption across Europe, advocating for policies that help to improve the affordability of heat pumps. The association focuses on four key drivers when assessing country-level policies that aim to increase market adoption of the technology: (1) Electricity-to-gas price ratios – an EC policy focus area, where recent changes to energy taxes in Belgium have shown early success in driving behavioural change, (2) Subsidies – while these remain available across Europe, a number of countries' policies have been unclear and/or inconsistent, and have therefore been less effective, (3) Supporting new build construction growth, and (4) Enhancing the competence and competitiveness of the installer market. On this fourth point, and in a follow up to our past discussion that installation costs in Germany remain high compared to other European countries, Mr. Kenny believed this results from: (a) Higher overall installer margins, (b) Stricter planning rules that require higher technology content, (c) Strict installer qualification requirements for subsidy eligibility, and (d) Subsidies being structured as a percentage of the installed cost, rather than at a fixed value.

## NIBE Industrier AB (Sell, 12m TP SEK34)

We met with the Managing Director of NIBE Energy Systems Ltd (NIBE's UK business). Our key takeaways are:

NIBE views the recent extension of the Boiler Upgrade Scheme (BUS) scheme to include Exhaust Air heat pumps as a key positive for its UK business. As one of just three OEM's supplying Exhaust Air HP technology to the UK market, compared to a more competitive air-to-water market, the group believes it is well positioned to benefit from the expansion of funding here. Additionally, the announced step up to £9k from July-26 for those converting from an O&G system is expected to further support demand growth in the UK.

NIBE believes that the BUS is the primary driver of growth in the UK heat pump market today. There were c.125k heat pumps sold in the UK last year. Of the combined £2.7bn in funding for the Boiler Upgrade Scheme, £295m was earmarked for the 2025/26 year. At the standard £7,500 grant for ASHPs/GSHPs, that implies potential support for up to 39,333 heat pump installations. Though the HP market was weak in 1Q following the transition of the low income funding scheme, NIBE expects to see flat volumes in the UK overall for 2026. Some UK demand within ground source HPs is driven by replacement demand, and NIBE notes success in outpacing the market in this product area. Air-to-air has not traditionally been a key market in the UK and NIBE does not currently compete here, estimating that only c.2.5k units are sold annually. While the group recently announced that it would add an air-to-air solution to its offering, we expect its initial focus to be on the French market and do not expect it to see meaningful sales in the UK in the near-term.

Training programs with installers are key for improving customer awareness. NIBE is celebrating its 20th year in the UK market, and has an established installer base, which means that the group has not seen labour shortages impacting its business. Last year the group announced its partnership with GTEC to train installers in the UK. The group believes that the program is going well, with 5k installers now trained to install HPs. Through this arrangement, the group sees scope for further growth in the brand for the years ahead, without the need to directly hire a large cohort of its own field service engineers.

In the last five weeks, NIBE UK has launched a direct-to-customer offering. The group believes that homeowners require access to fast online quoting, and so by launching this offering, it looks to capture more of the D2C market. NIBE UK is also considering setting up a financing option for its customers, similar to those already offered by Energy providers. We believe that this will likely be received well by customers as it breaks down the initial cost barrier to entry that many consumers face, likely broadening its TAM.

## Valuation & Key risks

We are Sell rated. Our 12-month price target of SEK34 is based on our sector-relative EV/IC vs. ROIC/WACC methodology on 9m27/3m28E.

Key risks to our Sell thesis: (1) The introduction of more supportive subsidy measures for energy efficient heating systems; (2) Changes to US export regulations/tariffs related to semiconductor markets; (3) An improvement in European construction markets resulting in better-than-expected sales growth; (4) A reduction in inflation and interest rates; (5) Better-than-expected cost improvements / M&A synergies; (6) Improving supply chains; (7) Cost inflation/pricing; (8) Margin or market share impact from changing trade tariffs (e.g. on imports into the US); and (9) Gas price increases or favourable FX.

## Viessmann (subsidiary of Carrier Global, covered by Joe Ritchie)

We met with the sales and product management representatives at Viessmann, a subsidiary of Carrier Global. Our key takeaways are:

Focusing on growth following its multi-year transformation. After a period of portfolio change, the group now has a strong portfolio of intelligent climate and energy solutions for the European HVAC market. Having combined its R&D expertise across the three organisations (Carrier, Toshiba, and Viessmann) the group now aims to bring a high quality, competitively priced offering that is underpinned by compelling warranties and its strong brand heritage across both resi and non-resi markets.

Within the UK market, the group sees a number of opportunities across its three growth vectors: (1) Product – Carrier’s European Datacentre business sees attractive opportunities for growth in the UK, which stands to benefit as the Irish grid has approached capacity constraints. In the resi market, Viessmann targets an expansion into the UK air-to-air HP segment next year, while Toshiba sees opportunities to expand the penetration of its cooling technologies in the UK, (2) Aftermarket – Carrier expects a multi-year aftermarket opportunity to follow the substantial growth in its product sales to the datacentre market, and (3) Systems – In March, Carrier made a strategic investment in Heat Geek, a UK-based startup digital sales platform that connects homeowners with Heat Geek-certified, trained local installers who use AI-powered tools to design and install the most efficient heat pump system for each customer’s home. This investment not only illustrates its commitment to the UK market, but highlights the group’s aims to deepen relationships with its installer customers.

Carrier's UK distribution model provides an edge over Asian peers targeting market entry via D2C. Chinese competition is intensifying in the UK with players looking to buy their way into the heat pump market, which resulted in the recent period of overstocking. However, Viessmann believes most installers buy through trade merchants, who provide their customers with access to credit lines and aftersales support, as well as the ease of a one-stop-shop for all installation requirements including piping and accessories. Viessman's UK distribution partners include large wholesalers, three national trade merchants (City Plumbing, UKPS, and Wolseley), and a number of smaller buying groups. Amidst this influx of competition, the group see its distribution model as an advantage vs. Asian suppliers that are predominantly looking to sell D2C.

Viessmann have passed through two $+3\%$ price increases this year, in January and in June/July. Because of rising costs, Viessmann's growth in the UK is expected to reach $+6\%$ from pricing alone this year. The group noted that this was slightly less than some other players but broadly in line with the industry.

## IMI (Neutral, 12m TP 2,560p)

We met with Marc Robertson, Head of Residential Buildings at IMI's Climate Control business. Our key takeaways are:

residential HVAC system. The group now has a full suite of technologies for both heating and cooling, providing full climate control in the home. Its technologies include pressurisation vessels, valves for system balancing, and thermostatic sensors, as well as the system's control interface. This provides scope for a potential two-fold increase in the c.£1,000 average wallet share currently captured by Heatmiser in a typical UK home (where the average residential HVAC system is comprised of c.6-7 radiators upstairs and an underfloor system at ground level). Its latest R&D initiatives have placed an emphasis on connectivity and the smart home.

## IMI's product quality and brand strength drive pull-through demand in an

installer-led market. The Heatmiser brand has strong resonance with installers, who drive $>90\%$ of the purchase decisions in the residential market. It also has a strong reputation among integrators and specifiers in the newer renewables market, where they are seeing strong pull-through demand for their products. However, IMI's residential climate control offering is now generating c.4-5% of its sales D2C via its website. Where the business is selling via merchants it seeks to incentivise project sales through adaptive pricing.

IMI's >1.5m connected devices and in-house software stack provide direct customer intimacy in an installer-led market, enabling its R&D teams to enhance the user experience and deepen IMI's pull-through demand. The company uses its connected offering to understand end-user behaviour, generated from the c.600,000 users of its app (Heatmiser Neo) which recently underwent a significant upgrade. While the convenience and energy saving advantages of smart controls are clear, having a reliable and easy-to-navigate user interface is key to the user experience. IMI therefore believes having an in-house software team is a key differentiator vs. peers in the segment using third party providers. It believes this provides an advantage in the sale of its smart valves, which generate between 4-6x the value of a manual valve.

## Valuation & Key risks

We are Neutral rated: Our 12-month price target of 2,560p is based on an 85% weighting to sector-relative EV/IC to ROIC/WACC, with a 15% weighting to an M&A component (16x EV/EBIT based on precedent transactions), using 12m27E.

Key risks: (1) Better/worse-than-expected IP growth that could positively/negatively impact IA, (2) Potential acceleration/curtailments of customers' capex projects and/or valve maintenance schedules as a result of improving/deteriorating oil prices and/or industrial activity, (3) A positive/negative adjustment in Truck OEMs' production rates, which could drive higher/lower demand for IMI's fluid control products in Transport, (4) The potential sale of the Transport segment, following the Board's strategic review of the business, (5) Better/worse-than-expected residential or commercial construction activity weighing on Climate Control, (6) Cost inflation/disinflation, particularly within the labour component, (7) Risk of margin pressure, share loss, or supply-chain challenges stemming from rising trade tariffs (e.g. on imports into the US), (8) M&A

execution, and, (9) Unfavourable FX.

## Stelrad Group plc (not covered)

We met with the Head of Marketing and the broader sales team from Stelrad Group plc. Stelrad is a European manufacturer of central heating radiators, with a product range that spans standard steel panel radiators, through low-temperature solutions for heat pump systems, as well as electric and designer radiators. Our key takeaways are:

The European market leader in radiators: Stelrad manufactures close to fifteen thousand radiators per day and generated c.£280m of revenue last year, supplying customers in over 40 countries. The group has a >50% share of the UK radiator market and a strong presence across Europe as a whole. The company primarily sells steel panel hydronic radiators that are produced in the UK and Turkey. It also supplies electric products under the De’Longhi brand that it acquired in 2022. The group sells 70% of its products through trade merchants, with the remaining 30% sold through other channels, including direct partnerships with installers where they offer a points-based incentive scheme to reward brand loyalty and encourage the up-selling of its products (e.g. to coloured radiators, which are now available in >200 different RAL colours).

(1) There is a need for new piping and radiator circuits when a conventional boiler system is converted to a heat pump. This can prove costly for customers and, without financial support, customers can be disincentivised from making the transition. (2) ECO funding in the UK was stopped for 6 months following the announcement of the Warm Homes Plan. Without this disruption, Stelrad believe that the market would have performed better. (3) Education and training remain lacking amongst installers. The group believes that installer knowledge of the broader HP installation requirements (such as wider pipes and larger surface area radiators) remains limited, with further training required to support the installe

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS.

This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
