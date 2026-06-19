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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## China Food Delivery

Not Just a Soft Draft: Disclosure Rules Could Cool the Food Delivery Subsidy War

SAMR's draft food-delivery rules reduce Meituan's downside tail, but they do not yet turn regulatory relief into a positive earnings catalyst, in our view. We reiterate Neutral on Meituan with a Dec-26 PT of HK\$85, making no changes to our estimates considering the draft's scenario framework. The call rests on one load-bearing assumption: SAMR's funding-source language has real behavioral bite and limits capital-funded subsidy attacks on food delivery. If that premise holds, our reading of the draft lowers the probability of our bear case (Table 4), in which prolonged capital-funded competition weakens the delivery profit pool and Meituan's fair value falls to around HK\$51. If the premise does not hold, the rules become disclosure without much strategic value. We do not use the draft alone as the basis to change our estimates, but we see it as a near-term sentiment stabilizer ahead of the final text due after the July 17, 2026 consultation deadline, and considering 3Q26 subsidy evidence.

- The market appears to be pricing the absence of explicit subsidy caps as evidence that the draft lacks bite. In our view, that misreads the mechanism. The draft does not need to cap every campaign to matter; it needs to make the most aggressive campaigns slower, more visible, and easier to challenge. Seven-day pre-disclosure reduces surprise value, while funding-source reporting and competitive-impact self-assessment create an evidentiary trail for regulators, competitors, merchants, riders, and media to scrutinize extreme promotions.  
- The relative stock implication favors Meituan on this specific catalyst, although not enough for us to prefer it outright over Alibaba (9988 HK/BABA US, OW) at the portfolio level. Meituan's advantages lie in order density, routing efficiency, merchant coverage, rider management, and consumer habit formation. If the rules shift competition away from fast capital-funded cash subsidy toward operating execution, the battleground moves back onto Meituan's terrain.  
- We would change our view if the final rules explicitly allow group-level operating profit to satisfy the funding-source requirement, if platforms keep running aggressive disclosed campaigns without regulatory response, or if Alibaba redirects the fight into higher-AOV use cases where Meituan's profit pool is more exposed. The clearest falsification test is 3Q26 subsidy intensity: if reporting and industry checks show subsidies remain near 1H26 levels with no moderation, our interpretation weakens. Conversely, final wording that preserves Provision 3, first disclosures that force campaign economics into view, and evidence of easing subsidy intensity would support a shift of probability weight from the HKD51 bear case toward the HKD92 base and the HKD128 bull case.

Head of China Equity Research and Co-Head of Asia TMT Research

Alex Yao AC

(86 21) 6106 6505

alex.yao@JPM.com

SAC Registration Number: S1730523020001

Nancy Liu

(86 21) 6106 6343

nancy.liu@JPM.com

SAC Registration Number: S1730524090001

JPM Securities (China) Company Limited

## JPM view

The market is likely to read the draft as soft because it lacks hard caps. We think that misses the point. The draft does not try to regulate subsidies mainly by setting a price ceiling, in our view. It regulates them by making aggressive campaigns slower, more visible, and easier to challenge. In food delivery, that is meaningful. The most damaging form of competition

See page 7 for analyst certification and important disclosures, including non-US analyst disclosures.

is not ordinary promotion; it is fast, capital-funded subsidy escalation designed to change consumer and merchant behavior before the incumbent can respond. Seven-day disclosure and funding-source reporting directly target that mechanism.

Our view is therefore simple: disclosure, funding-source scrutiny, and competitive-impact self-assessment are the enforcement mechanism.

Stock implication: The draft is likely to reduce bear case probability of Meituan but this is not a reason to flip Meituan over Alibaba outright. Alibaba remains a broader AI/cloud/platform optionality story. The point is narrower: on this specific food-delivery catalyst, the relative value setup favors Meituan more than the market is likely to price.

## What has changed?

SAMR released the draft Food Delivery Platform Subsidy Conduct Rules for public consultation on June 17, with comments open through July 17, 2026. The draft is framed under China's anti-monopoly, anti-unfair competition, price, e-commerce, and food-safety regimes.

The draft has three elements that matter most for investors:

Table 1: Key details in Food Delivery Platform Subsidy Conduct Rules

<table><tr><td>Rule element</td><td>What it requires</td><td>Why it matters</td></tr><tr><td>Funding-source discipline</td><td>Subsidies should be funded from own operating profit, not capital advantage</td><td>Limits the ability of challengers to fund food-delivery losses with group-level capital</td></tr><tr><td>Seven-day pre-disclosure</td><td>Platforms must disclose campaigns before launch</td><td>Reduces speed and surprise in subsidy wars</td></tr><tr><td>Competitive-impact reporting</td><td>Platforms must disclose campaign design, funding source, and competitive impact</td><td>Creates a written record that can later support enforcement</td></tr></table>

Source: SAMR (link), JPM.

The timing also matters. The draft lands during the 618 promotional window, exactly when renewed subsidy escalation would have tested the bear case for Meituan.

## Why disclosure is enforcement

The first instinct is that “no caps” means “no bite.” We disagree.

The disclosure regime changes the economics of subsidy competition in three ways.

First, it slows the game down. Food-delivery subsidy wars are reactive. A challenger launches a promotion, the incumbent responds, and the market tests how far each side is willing to go. A seven-day public notice window reduces the value of surprise and weakens the tit-for-tat dynamic.

Second, it creates evidence. Funding-source disclosure and competitive-impact self-assessment force platforms to write down the facts that regulators would later need to evaluate whether a campaign relied on capital advantage or unfair competition.

Third, it raises the cost of aggression before penalties arrive. A campaign that must be disclosed in advance is easier for competitors, merchants, riders, media, and regulators to monitor. That reputational and enforcement risk should reduce the willingness to run extreme campaigns.

This is why we view the draft as more binding than it appears. It does not need to ban every subsidy to change platform behavior. It only needs to make the most aggressive campaigns harder to launch, justify, and repeat.

## The key interpretive issue: segment profit or group profit?

Provision 3 is the load-bearing clause, in our view. It requires subsidies to come from own operating profit rather than capital advantage.

The investment conclusion depends on how “own operating profit” is interpreted.

Table 2: Possible interpretations for 'own operating profit' term

<table><tr><td>Interpretation</td><td>Implication</td></tr><tr><td>Segment-level or near-segment-level profit</td><td>Strongly favors Meituan; challengers cannot easily fund delivery losses with group capital</td></tr><tr><td>Group-level profit</td><td>Weakens the asymmetry; Alibaba could argue that group profitability supports continued investment</td></tr><tr><td>Vague final wording</td><td>Keeps the issue alive; enforcement behavior becomes more important than the text itself</td></tr></table>

Source: JPM.

Our base interpretation is that the “capital advantage” language is intended to limit cross-subsidy and balance-sheet-funded share attacks. That is why the rule matters for Meituan. But this is also the biggest risk to our view. If the final text explicitly allows group-level profit to satisfy the requirement, the strategic benefit to Meituan would be materially smaller.

## How the rule changes competition

The draft shifts the battleground from cash subsidy toward operating quality.

Table 3: Changes in key dimensions post the SAMR draft

<table><tr><td>Dimension</td><td>Before the draft</td><td>After the draft</td><td>Relative beneficiary</td></tr><tr><td>Campaign speed</td><td>Flash promotions and rapid response</td><td>Seven-day pre-disclosure</td><td>Incumbent with scale and density</td></tr><tr><td>Funding source</td><td>Group capital can support delivery losses</td><td>Own operating profit becomes more important</td><td>Meituan</td></tr><tr><td>Competitive lever</td><td>Cash subsidy and user incentives</td><td>Fulfillment, routing, merchant depth, reliability</td><td>Meituan</td></tr><tr><td>Merchant/rider economics</td><td>More room for cost shifting</td><td>Cost-shifting restrictions</td><td>Sector-wide cost floor rises</td></tr><tr><td>Profit pool</td><td>Higher risk of multi-quarter loss-funded war</td><td>Lower probability of negative-profit tail</td><td>Meituan structurally</td></tr></table>

Source: JPM.

This does not mean food-delivery competition goes away. It means the easiest way to attack the incumbent, using capital to subsidize losses, becomes more expensive and more visible. Competition can still move into fulfillment quality, merchant selection, membership benefits, logistics, and high-AOV use cases. But those are precisely the areas where scale, density, and operating capability matter more than headline cash burn.

## Industry implications

## Competition: less cash burn, more operating execution

The rule reduces the value of capital-funded subsidy as a competitive shortcut. A challenger can still invest, but it becomes harder to disguise a share-buying campaign as ordinary promotion if the campaign must be disclosed in advance, justified publicly, and linked to a compliant funding source.

That matters because Meituan's moat is operational rather than financial. Its advantage sits in order density, routing efficiency, merchant coverage, rider network management, and consumer habit formation. If the competitive game moves back toward these variables, Meituan's relative position improves.

## Operations: subsidy relief, but a higher cost floor

The draft should reduce the probability of extreme promotional escalation. At the same time, it reinforces a higher sector cost floor. Rules against forcing merchants or riders to bear subsidy costs, combined with rider social-insurance pressure, make it harder for platforms to offset promotion through cost shifting.

For Meituan, this is a mixed but net constructive outcome. The subsidy line should face less tail risk, but delivery costs are unlikely to return cleanly to pre-2025 levels. Our model already assumes rider cost per order moving from around RMB5.0 toward RMB5.2–5.3. The draft reinforces that direction.

## Profit pool: the floor improves more than the ceiling

We retain our published industry profit-pool framework. In our base case, Meituan captures all or almost all positive food-delivery industry profit. In the fragmented bear case, the profit pool can turn negative.

The draft could reduce the probability of that negative-pool scenario. It does not restore the industry to a 2024-style profit ceiling. Redirected competition into service quality, logistics, and merchant support will still cost money. The more important change is that sustained loss-funded subsidy competition becomes harder to justify.

## Stock implications

## Meituan: the strategic beneficiary

Meituan is the stock most helped by the strategic logic of the draft. The rule reduces the probability of a prolonged capital-funded attack on its core delivery profit pool. It also arrives at the moment when subsidy reacceleration would have been the clearest bear-case trigger.

The caveat is that Meituan's own promotional toolkit is also constrained. It cannot rely on forced participation, below-cost pricing, discriminatory treatment, or surprise campaigns. The draft also does not directly stop Alibaba from attacking high-AOV delivery use cases, which remains our live falsification risk.

Still, the balance is favorable. The rule shifts the fight from capital subsidy back toward operating efficiency. That is Meituan's terrain.

We maintain Neutral. The draft does not yet justify an estimate change, but it modestly improves near term investor sentiment.

## Alibaba: near-term relief, but less instant-commerce optionality

For Alibaba, the P&L effect is positive. Less food-delivery subsidy intensity should reduce losses in Taobao Instant Commerce / Ele.me.

But the strategic effect is more complicated. Part of the Alibaba bull case assumes instant commerce can become a traffic-acquisition and user-frequency engine for Taobao. If the rule limits capital-funded delivery subsidies, that option becomes less valuable. Alibaba can still pursue the opportunity, but it may need to rely more on operating execution and less on balance-sheet-funded user acquisition. This is why the rule taxes the optionality leg, even if it helps near-term losses.

The key ambiguity is again Provision 3. If group-level profit is enough to satisfy the rule, Alibaba's flexibility remains much greater. If segment-level economics matter, the instant-commerce push becomes more constrained.

## JD: cleanest P&L relief, weaker strategic durability

JD has the cleanest near-term earnings read-through. Its food-delivery entry has been subsidy-intensive, and the draft gives management both regulatory cover and economic reason to rationalize spend.

That explains why the consensus trade favored JD. But the strategic read is less favorable. JD's delivery push is the most dependent on capital-funded subsidy among the three platforms. If Provision 3 is enforced with real bite, the durability of JD's food-delivery position becomes harder to underwrite.

The lasting impact of JD's entry may therefore be less about permanent share gain and more about a higher sector cost floor, especially on rider wages and fulfillment standards.

## Valuation: scenario skew improves, estimates unchanged

We keep ratings and estimates unchanged. The draft is still open for comment, and the final wording will matter.

Our Meituan scenario set remains:

Table 4: Meituan scenario analysis

<table><tr><td>Scenario</td><td>PT</td><td>Description</td></tr><tr><td>Bull</td><td>Around HKD128</td><td>Rationalized competition, stronger profit-pool recovery</td></tr><tr><td>Base</td><td>Around HKD92</td><td>Subsidy pressure eases, but cost floor remains higher</td></tr><tr><td>Bear</td><td>Around HKD51</td><td>Prolonged capital-funded competition and weaker delivery profit pool</td></tr></table>

Source: JPM.

The draft does not change the model mechanically today. It changes the probability distribution. A credible shift in the “binding vs cosmetic” debate would justify moving some weight out of the bear case and into the base and bull cases. Illustratively, moving around ten points of probability weight away from the bear case would lift our blended PT into the low-to-mid HKD90s.

That is a continuation of our prior framework, not a new valuation thesis. Bear-case probability had already declined from our April deep dive to the 1Q26 results update. The SAMR draft reinforces that direction but does not complete the argument. We would wait for final text and 3Q26 subsidy evidence before making formal estimate changes.

## What could make us wrong?

## Final wording allows group-level profit

This is the most important risk. If the final rule explicitly allows platforms to fund subsidies from group-level operating profit, the asymmetry weakens. Alibaba would retain greater flexibility to support food-delivery investment, and Meituan's strategic benefit would be smaller.

## Enforcement is soft

The draft could become a disclosure exercise without meaningful behavioral impact. If platforms continue aggressive subsidy campaigns after making formal disclosures, and regulators do not respond, the rule would be less binding than we expect.

## Alibaba shifts into high-AOV core attack

The rule targets subsidies, below-cost pricing, and cost shifting. It does not directly prevent competition through fulfillment quality, selection, membership, or logistics. Alibaba could still attack higher-AOV use cases where Meituan's profit pool is more exposed.

## 3Q26 data show no easing

The clearest falsification test is actual subsidy intensity. If 3Q26 reporting and industry checks show per-order subsidies continuing near 1H26 levels with no evidence of moderation, our interpretation would need to be revisited.

## What to watch next

The next catalysts include:

Table 5: Key catalysts to watch

<table><tr><td>Date / evidence</td><td>Why it matters</td></tr><tr><td>Final SAMR text after July 17, 2026</td><td>Determines whether Provision 3 keeps real bite</td></tr><tr><td>First seven-day campaign disclosures</td><td>Shows whether platforms must reveal funding source and campaign mechanics</td></tr><tr><td>3Q26 results and management commentary</td><td>Tests whether subsidy intensity is actually easing</td></tr><tr><td>Alibaba instant-commerce strategy</td><td>Determines whether competition shifts from broad subsidy to high-AOV core attack</td></tr><tr><td>JD reinvestment behavior</td><td>Tests whether subsidy savings flow to earnings or are redirected into new spending</td></tr></table>

Source: JPM.

The draft is not the end of the debate. It is the start of a more observable phase. If the final rules preserve the funding-source language and the first disclosures force platforms to explain campaign economics, the market may need to revisit the relative value setup across Meituan, Alibaba, and JD.

Companies Discussed in This Report (all prices in this report as of market close on 17 June 2026, unless otherwise indicated)

Alibaba Group Holding Limited(9988.HK/HK\$106.90/OW), Alibaba Group Holding Limited (BABA)(BABA/\$107.44/OW), JD.Com, Inc. (9618)(9618.HK/HK\$111.10/OW), JD.com, Inc.(JD/\$27.91/OW), Meituan (3690)(3690.HK/HK\$74.40/N)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that

[中间内容因长度限制已省略]

re subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
