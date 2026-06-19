你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

This is the most important risk. If the final rule explicitly allows platforms to fund subsidies from group-level operating profit, the asym

[中间内容因长度限制已省略]

ies discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
