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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# US TMC Conference

Feedback on US wireless, the satellite debate, and AI related upside

Over the last two days, JPM has hosted its (ongoing) 54 $^{th}$ TMC conference in Boston. Key feedback, as it pertains to our EMEA coverage universe, includes: (1) US wireless: Investors remain a little nervous on near-term competitive unknowns given Verizon’s planned Q2 tariff refresh, and CEO Schulman’s insistence that his FY net adds guide is conservative. That said, the bigger picture (for us) was that the BIG3 seem collectively confident in their growth outlooks, which are more centered around driving share gains across new TAMs (FWA, fibre, convergence), and leveraging AI to accelerate cost efficiencies as well as reduce churn, (2) Satellites: Reassuring messages, with the BIG3 stressing they have no appetite to offer satellite operators an MVNO, that D2D volumes are extremely low (just 0.0002% of TMUS’ total network traffic), and that satellite is in their minds complementary, rather than a threat (a view reinforced by the BIG3 D2D JV), (3) AI: The most confident AI messages came from Twilio (its AI product stack is far superior to that of Sinch, but offers insights into what is possible should Sinch close the gap), and AMT (led by its datacentre unit CoreSite, but includes hopes of mid-term benefits to the tower ecosystem), (4) DT: On Monday (here) we argued DT’s shares screened oversold, and we believe this supportive US conference feedback should see the recent rebound run further. That said, several unknowns remain, and furthermore we continue to see European consolidation plays as offering the most compelling risk-reward ahead. US Telcos are covered by Sebastiano Petti and US Towers by Richard Choe.

# T-Mobile – Srini Gopalan (CEO)

Takeaways: (1) Network perception: The CEO believes this can drive years of ongoing share gains given an identified 20m+ addressable “network seeker”; (2) ARPA growth: Expect this to be supported by the fact that port-in ARPA is 20% higher than port-out ARPA (hence volume growth is accretive), expanding customer relationships, and thoughtful more-for-more pricing; (3) SMRA: Momentum to continue. Q1 share of 24% marked the 12th consecutive quarter of win-share leadership; (4) FWA: Reiterated guidance for 15m FWA customers by FY30E (underpinned by fallow capacity, without considering upside from new spectrum wins or technology driven improvements in spectral efficiency); (5) Fibre: TMUS remains disciplined, targeting double-digit IRRs and first-to-fiber areas. The CEO noted first year fibre penetration rates of \~20%, a preference for fibre ownership over wholesale deals, and that cable M&A is “structurally off the table” given cable’s overpriced back book; (6) DT-TMUS merger: TMUS would not comment on “market speculation”, reiterating that under Delaware law, any such hypothetical transaction would require majority approval of disinterested shareholders; (7) Satellite: The recent D2D JV with Verizon and AT&T includes implementing satellite as a standard feature on premium rate plans, driving a uniform device ecosystem, and standardizing spectrum. TMUS reiterated that D2D is complementary to terrestrial wireless. The company sees no incremental TAM opportunity from offering satellite an MVNO arrangement, and noted satellite usage today is extremely limited (0.0002% of total network traffic).

# European Telecommunication Services

Akhil Dattani AC

(44-20) 7134-4725

akhil.dattani@JPM.com

JPM Securities plc

Ankur Baheti, CFA

(91-86) 5796-8820

ankur.baheti@jpmchase.com

JPM India Private Limited

# Specialist Sales contact details:

# Scott Silver - Specialist Sales - European TMT

(44-20) 7134-0412

scott.silver@JPM.com

# Verizon – Dan Schulman (CEO)

Key takeaways: (1) Costs: Want to be the most efficient Telco in the world. Already well on the way to cutting \$5bn in opex (with risk potentially to the upside), as well as \$4bn in capex (it seems there could even be room to cut further mid-term, depending somewhat on how much spectrum Verizon secures in upcoming auctions). But Schulman was clear that costs were an output, rather than an input, with the core objective being to “delight customers”; (2) Driving change: Schulman believes Verizon was historically too slow, too process orientated, and too risk averse. Today they are one of the 1 $^{st}$ 30 companies to have worked with Anthropic, they are becoming AI-native, and they are working to drive major improvements to every layer of the customer experience. Churn in Q4 was 95bp. This fell to 90bp in Q1, and 85bp by the end of Q1. This is helping lower both the cost per gross add and retention costs. Over 50% of the FY net adds improvement will come from churn reductions; (3) Q2 tariff refresh: The CEO noted their targeted Q2 “valuation proposition refresh” has been worked on for some time. Whilst he did not provide any clear colour, he suggested it would be about changing “lots of small things” and being “fiscally responsible”. He noted a desire to move away from clumsy “free handset” offers to tools that create tangible, and durable, improvements in customer experience and satisfaction; (4) Shareholder value: The CEO noted Verizon in the past was a substitute for a bond yield given 20 years of ongoing dividend growth. But he now wants to pivot to driving a step function change in revenue and bottom-line growth, which in turn should deliver greater shareholder value; (5) D2D partnership: Seen as a pragmatic agreement that will eliminate deadzones, create standards for all satellite operators, and simplify the ecosystem. Like TMUS, Verizon also indicated no appetite for offering satellite operators an MVNO. Finally, Schulman argued he could not see satellites being anything but complimentary to wireless over the next 10 years given the vast differences in urban capacity.

# AT&T – John Stankey (Chairman & CEO)

Takeaways: (1) Fibre: Lumen integration is progressing well. On further fibre M&A, AT&T reiterated no interest in fragmented “postage stamp” fiber assets, noting a preference for scaled, metro-dense fiber at fair value. That said, the CEO is also open to aggregating mismanaged assets cleansed through bankruptcy if any such opportunity arises. But for now, an organic strategy is the company’s focus; (2) Churn: AT&T believes the recent deterioration (attributed to competitor buy-out offers) should plateau as they have now worked through the base. Longer term, AT&T believes convergence can deliver “dramatic improvement[s] in churn and longevity”. On the value segment push, Stankey framed it as a network utilization decision (which he considers accretive to returns); (3) Cable: AT&T stressed that their fibre growth was coming from competitive wins, not base transition, given the absence of any remaining DSL base to harvest. The company also suggested cable-wireless bases may become increasingly vulnerable to fibre share gains; (4) AI: AT&T sees the company’s role across three layers: (i) Preferred access: Fiber has the lowest marginal cost, and is the most future-proofed technology for heavy workloads, which paired with EchoStar spectrum enables more symmetrical low-band upstream on wireless; (ii) Metro aggregation and backbone: Actively building shared dark and lit fiber infrastructure into hyperscaler access points; and (iii) Edge compute: A potential opportunity “if we think it makes sense” but conviction seemed low; (5) D2D: AT&T see satellite as a “great complement” with a seamless D2D product expected in 2H26. AT&T notes it would make no sense for the BIG3 to each separately lobby for spectrum harmonisation and shared network standards, nor for each to build out duplicate ground-station infrastructure. A detailed term sheet should materialise shortly, with the regulatory timeline a little more difficult to call.

# Twilio – Aidan Viggiano (CFO)

Takeaways: (1) AI-first: Twilio has recently embedded several new AI capabilities to its offering which can now maintain one continuous customer conversation across all channels, remembers conversations/context, and leverages AI to turn conversations into actionable, real-time intelligence that enhances human agents and triggers immediate actions like automated workflows across voice and messaging channels; (2) Q1 acceleration usage-led: The company's organic growth in Q1 was broad-based across products and the recent acceleration was attributed to AI native offerings. On the 5% beat last quarter, management commented that they wouldn't see it as “kind of the new norm”, however attributed it to their usage-based model; (3) Q2 guide prudent: On the debate regarding Q2 guide screening conservative, given it implies a deceleration in organic growth, management commented that “it's pretty consistent with how we've guided... we're usage-based... we plan a bit more prudently”. They also added that they “feel really good about the opportunity ahead.. and about the setup for Q2 and the balance of the year”.

# AST – Scott Wisniewski (President & CSO)

Takeaways: (1) Commercialisation: 45+ satellites in orbit is the threshold needed to achieve full commercial service in priority markets like the US. D2D broad integration is expected from 2027 onward; (2) Spectrum: S-Band spectrum is being pursued opportunistically around the world, notably in Europe where licenses are underutilized. Since the company's satellites were being built regardless, the incremental cost of adding new spectrum bands is relatively low, enabling fast and strategic spectrum acquisition; (3) Revenues: Revenues are expected to grow sequentially each quarter toward \$150-200m in 2026, all from pre-commercial service activity. A roughly 50/50 split between government and commercial revenue is anticipated, with upside potential in both. More than half of the remaining 2026 guidance is already contracted, with the rest covered several times over by the pipeline; (4) Backlog: Minimum revenue commitments secured from operators, contributing \$100m+ per year across multi-year agreements (ranging from 2 to 10 years), spread pro-rata i.e. not back-end loaded; (5) Outlook: The company thinks it can reach positive operating FCF well before hitting \$1bn in revenue. Active in-orbit testing is underway for multiple US government revenue-producing opportunities.

# AMT – Rodney Smith (EVP & CFO)

Takeaways: (1) Outlook: Mid-single-digit revenue growth in the US is expected to underpin industry-leading AFFO per share growth, complemented by faster growth in emerging markets and double-digit growth in the data center platform, collectively targeting mid to upper single-digit AFFO per share growth reliably; (2) Europe: The region is outperforming its original business case, with mid single-digit or better revenue growth expected. The portfolio is insulated from material one-time churn events, as the majority of revenue is tied to long-term contracts with Telefonica; (3) LatAm: The region is going through a consolidation. Hence 2026 marks peak churn, particularly in Brazil, which is transitioning to a three-carrier market. Starting next year, churn is expected to decrease rapidly with new business activity likely accelerating; (4) Africa: Upper single-digit organic tenant billings growth, even after absorbing a few hundred basis points of churn, which management views as a normal operating environment for the region; (5) CoreSite: Datacenter investments have been scaled up from \$200m to \$800m now. The long-term vision is to connect CoreSite facilities directly into tower assets, positioning the company to benefit from the convergence of mobile network densification and AI-driven edge compute demand. Capital reallocation in datacenters has been deliberate with investment appetite shifted away from emerging markets and toward the US and CoreSite; (6) AI workloads: These are increasingly tipping out of large language models, and hyperscale facilities, into edge facilities like CoreSite, which management views as a meaningful and growing source of upside. Future wireless network evolution will require uplink and downlink symmetry, improved latency, more antennas, and compute power paired directly at tower sites, potentially including cloud on-ramps and interconnection capabilities.

# SBA – Marc Montagner (EVP & CFO)

Takeaways: (1) US: Long-term US growth is framed as 3% escalators + 2.5-3% new lease activity from the big three MNOs - 1% churn, arriving 4.5-5% baseline growth rate, assuming a three-carrier market. Upside scenarios beyond the baseline include new use cases such as drone delivery, self-driving cars, and edge computing for AI inference, as well as potential satellite spectrum deployment, which management believes would be a net positive for tower demand. 6G expected in late 2028-2029, combined with new use cases and edge computing demand, could meaningfully exceed the current 3+3-1 growth framework over the long term; (2) AI: AI-driven latency requirements are expected to push compute closer to the network edge, creating potential incremental demand at tower sites; (3) BTS: New BTS rates offered by the big three carriers in the US were previously unattractive, leading SBA to largely sit out. However, the dialogue is shifting and conversations are resuming, with management willing to participate at the right returns; (4) Brazil: SBA could see peak churn this year due to Oi Mobile's consolidation, however churn is expected to persist for another \~2 years. The long-term outlook remains high single-digit growth, assuming \~5-6% CPI and \~4% lease-up; (5) Shareholder returns: Buybacks remain a priority. \$500m was spent on repurchases last year and management expect to lean toward buybacks again this year. The dividend was increased 13% last year with a \~41% payout ratio, and low-teens dividend growth is expected to be maintained for the next three years.

# Uniti – Kenny Gunderman (CEO)

In April 2026, press reports speculated T-Mobile's interest in Uniti's Consumer fibre assets (here). The presentation covered (in great detail) Uniti's build strategy, competitive dynamics, business moats, and hyperscaler opportunity. Takeaways: (1) Fibre: Uniti's core strategy is to build fiber first, where no fiber exists, focusing on clustered strategic markets rather than a patchwork of builds across the country, in order to capture go-to-market, construction, and operational synergies; (2) Q1 phasing: Winter storms were cited as a partial reason for the Q1 slowdown, but March and April each saw \~45k homes built, which annualizes to 500k+ homes and is directionally where the company wants to be; (3) Churn: Fiber churn is tracking “better than expected” and is now a bonus metric; (4) Overbuilders: Altnets have largely stayed away from Uniti's footprint, as rural markets are harder to enter due to smaller addressable populations, limited backhaul options (Uniti is often the only provider and does not sell to overbuilders), and the company's strategy of building as fast as possible to raise barriers to entry; (5) Cable: Overlap exists in roughly 50% of the footprint, which is well below the industry average; (6) Penetration: The 40% long-term penetration guidance is viewed as increasingly conservative, with management noting that virtually all original model assumptions are proving prudent; (7) Backbone: Uniti's rural backbone infrastructure, built across Tier 2 and Tier 3 long-haul corridors, has proven to be strategically valuable to hyperscalers who are targeting those locations for land and power accessibility. This gives Uniti a deployment speed and cost advantage, as 80% of hyperscaler deals involve selling existing infrastructure or infrastructure attached to existing routes. (8) Outlook: The company is targeting \~\$1.5bn of revenue from anchor hyperscaler builds over the next several years, expected to generate \~\$500m of recurring revenue, representing a meaningful share of what management estimates to be a \$75bn TAM for fiber companies. Management noted these numbers could be larger when revisited next year; (9) IRRs: Blended IRR on anchor plus lease-up hyperscaler economics is tracking at 30%.

Companies Discussed in This Report (all prices in this report as of market close on 19 May 2026, unless otherwise indicated) AT&T(T/\$24.98/OW), American Tower(AMT/\$183.00/OW), Cellnex(CLNX.MC/€29.16/N), Deutsche Telekom(DTEGn.DE/€29.25/OW), Elisa(ELISA.HE/€41.72/UW), Inwit(INWT.MI/€6.76/N), KPN(KPN.AS/€4.67/N), Liberty Global(LBTYA/\$12.15/NR), NOS(NOS.LS/€5.42/UW), OTE(OTEr.AT/€18.70/N), Orange SA(ORAN.PA/€18.74/OW), SBA Communications(SBAC/\$207.51/N), Swisscom(SCMN.S/CHF684.50/UW), T-Mobile US Inc.(TMUS/\$193.42/OW), Tele2(TEL2b.ST/Skr185.15/OW), Telecom Italia(TLIT.MI/€0.72/NR), Telecom Italia (Savings)(TLITn.MI/€0.76/NR), Twilio(TWLO/\$195.95/OW), Uniti Group Inc(UNIT/\$10.67/N), Verizon Communications(VZ/\$47.74/N), Vodafone(VOD.L/113p/UW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

# Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including pr

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 19 May 2026 11:41 PM BST

Disseminated 20 May 2026 12:15 AM BST
"""
