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
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## China Internet

## Cheap is acknowledged; urgency still needs proof

Based on our one-week long marketing meetings with US-based investors, we believe US investors remain engaged on China Internet, but the trip did not suggest a broad rotation back into the sector. The consistent message from meetings was that valuation is no longer the central debate. Most investors accept that the large-cap platforms are inexpensive. What they do not yet accept is that cheapness alone is enough to compete for capital against AI hardware, memory, semis, and private or newly listed AI assets where near-term earnings revisions or scarcity narratives remain cleaner.

\- That leaves the sector in a selective, proof-driven regime, in our view. Potential marginal buyers are not asking whether China Internet can screen cheap. They are asking where the next observable catalyst is strong enough to change behavior. On this trip, the most actionable debates were Alibaba cloud margin, Tencent AI disclosure, Baidu's Kunlunxin and capital return path, Zhipu relative to MiniMax, and Kuaishou's value capture from Kling.

\- Our takeaway is not to press broad sector beta. We would focus marketing and positioning around names where a dated catalyst or measurable proof point can do the work. Alibaba had the clearest tactical traction among the large platforms because cloud margin is a near-term reported variable. Baidu drew event-driven interest around Kunlunxin, capital return, and potential listing-related catalysts. The Zhipu over MiniMax relative preference resonated well, although the debate has shifted from model quality to commercial durability. Tencent remains highly respected but was rarely treated as urgent; investors want AI monetization KPIs before assigning more value to the option. Meituan was viewed as regulation-positive but not necessarily the cleanest expression of food-delivery rationalization, with JD repeatedly raised as an alternative revision vehicle. Kuaishou interest remained concentrated in Kling, with the main question being how much value ultimately accrues to the listed parent.

\- We believe US investors are not dismissing China Internet. They are asking for proof before reallocating capital. The sector has investable assets, and valuation support is real. But the market's burden has moved from “is it cheap?” to “what changes revisions, AI monetization, or catalyst density soon enough to matter?”

\- In that regime, we would not chase broad beta. We would lean into where proof is the closest: Alibaba cloud margin, Baidu's catalyst path, and the Zhipu over MiniMax relative preference. We would hold Tencent as patient core but not press the entry without AI KPIs. We would keep Meituan and Kuaishou catalyst-dependent, with JD remaining the cleaner food-delivery revision expression if rationalization shows up there first.

Head of China Equity Research and Co-Head of Asia TMT Research

Alex Yao AC
(86 21) 6106 6505
alex.yao@JPM.com
SAC Registration Number: S1730523020001

Daniel Chen
(86-21) 6106 6205
daniel.q.chen@JPM.com
SAC Registration Number: S1730521040001

Olivia Xu
(86-21) 6106 6138
olivia.w.xu@JPM.com
SAC Registration Number: S1730525060001

Nancy Liu
(86 21) 6106 6343
nancy.liu@JPM.com
SAC Registration Number: S1730524090001
JPM Securities (China) Company Limited

## The positioning regime: engaged, but still underweight in behavior

US-based investors are not rejecting China Internet. It is deferring the trade, in our view.

See page 7 for analyst certification and important disclosures, including non-US analyst disclosures.

Across the meetings, the broad pattern was consistent. Investors were familiar with the valuation argument and generally accepted it. The pushback was timing. For US allocators, the opportunity cost remains high: AI hardware, memory, semis, and private AI assets still offer cleaner near-term revision stories or scarcity value. Against this backdrop, China Internet is respected but not yet urgent.

In our view, the biggest challenge to China Internet is capital allocation. Investors can agree that Tencent, Alibaba, Baidu, Meituan, JD, Kuaishou, and select AI model labs have investable assets, while still choosing not to fund them today. The question that came back repeatedly was: what changes the near-term revision path, reported AI return profile, or catalyst density enough to pull money out of the existing AI hardware and scarcity trades?

This is why the trip supports a more selective framework. We would separate the sector into three groups:

1. Names with near-term proof points that investors can underwrite: Alibaba cloud margin, Baidu's Kunlunxin and capital return path, and the Zhipu over MiniMax relative debate.

2. High-quality names that need disclosure before urgency returns: Tencent is the clearest example.

3. Names where the asset is interesting but the equity bridge remains unproven: Meituan, Kuaishou, and to a lesser extent any broad beta expression without a catalyst.

We believe the feedback signal is the strongest at the sector level: cheapness is acknowledged, but opportunity cost is still winning. It is somewhat less precise at the name level, because individual investor preferences varied by mandate, holding period, and exposure to AI hardware. Still, the same proof burden repeated often enough to be useful.

## What investors pressed on

The trip was not about whether China Internet looks cheap on screens. It was about whether reported proof can arrive quickly enough to compete with the current AI trade.

Four debates ran through the week.

## First, what breaks the long hardware / underweight internet regime?

Investors recognize that AI hardware and memory are crowded. But most did not want to fade that trade without a trigger. A valuation gap by itself was not considered enough. A rotation would likely require either disappointment in hardware revisions or positive revision breadth in China Internet across multiple large caps

## Second, can AI investment show up in reported numbers?

Investors were less interested in broad AI narratives than in reported evidence. For Tencent, the focus was Hunyuan, WeChat agents, WorkBuddy, cloud APIs, advertising monetization, and whether any of those surfaces can become visible in revenue or margin. For Alibaba, the debate was more concrete: whether cloud margin can expand as AI demand scales, and whether losses in consumer AI or local services offset the cloud benefit.

## Third, does China's lower-cost AI path create durable economics?

Investors accepted that Chinese models may operate on a different cost curve. The question was whether that translates into commercial advantage, pricing power, and retention, or whether the model layer remains structurally competitive with limited rent capture. This was especially relevant to Zhipu and MiniMax.

## Fourth, does food-delivery regulation reset economics or simply create a tradeable window?

Investors were broadly willing to treat the SAMR rules as regulation-positive for the sector. But they were more divided on equity expression. Meituan was not rejected, but several investors framed JD as the cleaner revision surprise if rationalization holds.

The common thread is that investors wanted proof with dates, not just frameworks. Cloud margin, AI KPIs, unit economics, listing events, lock-up clearance, capital return, and revenue disclosure all mattered more than broad sector valuation.

## US versus Asia: same regime, different lens

Our Asia marketing ran from early April through late June, while the US feedback reflects one week of meetings from June 15–22. The two periods are not perfectly comparable. The tape, hardware trade, and several company-specific catalysts moved during the Asia window. We therefore read the comparison as directional rather than precise.

With that caveat, both cohorts broadly agreed on the central regime: China Internet is inexpensive, but opportunity cost against AI hardware, memory, domestic chips, and model labs remains high.

The difference was in how the debate was framed. Asia investors tended to spend more time inside the operating mechanics: Alibaba cloud margin, Tencent Hunyuan and agents, Baidu Kunlunxin, food-delivery anti-involution, and AI cloud returns. US investors were more direct about the allocation problem: why own China Internet now when the AI hardware and scarcity trades still have cleaner revisions?

That distinction matters. Asia could become the earlier marginal bid if reported proof lands first in Alibaba cloud, Tencent AI disclosure, Baidu's event path, or Kuaishou/Kling value discovery. But Asia may also simply be expressing the same caution with more name-level detail. We would not overstate a regional divergence. The real divide is not US versus Asia. It is proof versus narrative.

## Feedback by name

## Tencent: respected, but still waiting for AI disclosure

Tencent remains the highest-quality large-cap platform in the group, but respect did not convert into urgency on this trip.

We carry Overweight on Tencent based on compounding earnings, bounded AI investment risk, and a trough multiple. Investors generally accepted the quality argument. The pushback was not that Tencent lacks assets. It was that the AI revenue path still feels too long-dated relative to what investors can own elsewhere today. For many investors, Tencent is not being rejected; it is being deferred.

The key debate is whether Tencent is a long-duration AI winner or simply a high-quality funding source for more immediate AI hardware exposure. The Hy3 release helped narrow the execution discount, but the market still wants disclosure rather than narrative. Investors asked for evidence around Hunyuan at scale, WeChat agents, WorkBuddy, cloud APIs, and advertising monetization.

The implication for our call is clear. Tencent remains a patient core position, not a name we would press purely on valuation. To shift from respected compounder to urgent buy, Tencent needs AI KPIs that can be connected to reported revenue, margin, or engagement over the next few quarters. Without that, the AI option remains outside base earnings in investors' minds.

## Alibaba: the strongest large-cap tactical set-up

Alibaba had the most tactical traction among the large platforms because the debate is tied to a dated and measurable proof point: cloud margin.

Investors were no longer debating whether Alibaba has an AI narrative. They were debating whether the cloud margin path is real, how quickly it can scale, and how much of the benefit leaks into consumer AI or local services losses. Our most recent review raised our 12-month conviction after external cloud growth near 40% year on year, the first MaaS ARR disclosure, and a more visible path for margin expansion.

The important nuance is that the cloud-margin thesis is no longer undiscovered. Many investors already understand the bull case: external cloud margin rising from the high-single-digit to low-double-digit range toward a higher long-term level. The investable edge is not in repeating that AI cloud is important. It is in assessing the slope of margin expansion and the degree of reinvestment leakage elsewhere.

That makes Alibaba the cleanest tactical large-cap expression of the current regime, in our view. The catalyst is measurable, near-term, and tied to reported numbers. If cloud margin expands sequentially while losses in local services and consumer AI remain controlled, Alibaba can shift from tactical AI beneficiary to a more durable compounder. If the margin path stalls or is offset by losses elsewhere, the current traction likely fades.

## Baidu: catalyst-dense, but still more event path than platform call

Baidu drew event-driven interest because Kunlunxin and capital return provide a denser catalyst path than broad sector beta.

Our most recent published view frames cloud inference momentum and Kunlunxin demand as the swing variable. Investors were interested in several potential catalysts: Kunlunxin IPO progress, a Hong Kong primary listing, Stock Connect inclusion, the first dividend, and a possible special distribution. Those are concrete events, and they help Baidu stand out in a sector where many investors still ask what the near-term trigger is.

The pushback was durability. Investors questioned whether Baidu is an asset-monetization trade or a sustainable AI platform. Legacy search remains under pressure, capex is below the largest platforms, and communication has not always helped investors underwrite the transition.

In our view, Baidu's event path can work, but long-only sizing likely requires a clearer capital return framework, more confidence in parent earnings quality, and better evidence that AI cloud revenue is durable rather than episodic.

## Meituan: regulation-positive, but not the cleanest expression

Meituan was viewed as a beneficiary of food-delivery rationalization, but the feedback did not support upgrading on regulation alone.

We are Neutral on Meituan with a fair value of HKD88. Investors generally accepted that SAMR subsidy rules are directionally positive for industry economics. The harder question was whether Meituan is the best way to express that view. Several investors asked whether the revision surprise is cleaner in JD.

For Meituan, the core debate remains normalized unit economics. Investors focused on the gap between management's roughly CNY1 per order ambition and bear cases closer to CNY0.20–0.30. The question is whether regulation protects Meituan's profit pool or exposes lower normalized economics once rational competitors regain share.

Our thesis continues to rest on durable unit economics and high-value order share. The trip reinforced our reluctance to upgrade on regulation alone. We need 2Q26 and 3Q26 to show that the improvement is owned rather than rented. If the sector rationalizes but JD captures the cleaner revision surprise, then JD may remain the better expression of the same theme.

## JD: the unprompted alternative in food-delivery rationalization

JD was not a lead marketed name on this trip, but it repeatedly surfaced as the preferred alternative expression of the food-delivery rationalization trade.

That is important feedback. Where investors were cautious on upgrading Meituan, several framed JD as the cleaner revision vehicle. If the thesis is rationalization plus positive earnings surprise, JD may be perceived as having more upside to consensus and a more straightforward path to earnings revision.

We carry Overweight on JD with estimates above consensus, so this feedback aligns with our existing positioning. Because JD was not systematically tested across all meetings, we would treat the signal as medium confidence rather than definitive. But the fact that investors volunteered the comparison is meaningful. It raises the bar for Meituan: Meituan needs to win on its own unit economics, not simply benefit from the same regulatory tailwind that investors may prefer to express through JD.

## Zhipu: preferred listed model-lab exposure, but the burden has moved to commercial proof

Zhipu was one of the most positively received relative calls on the trip. Investors generally preferred Zhipu to MiniMax as listed model-lab exposure, citing model quality, pricing power, capital access, and the fundraising flywheel.

Our long case on ship should not rest only on generic base-model leadership. It needs to rest on coding as a defended workflow vertical where Zhipu can show paid demand, pricing power, retention, and enterprise value capture.

That distinction matters because the model-lab scarcity premium may compress as more assets list or become available to public-market investors. Kimi, DeepSeek, and others may all affect how investors price scarcity. In that environment, benchmark progress is necessary but not sufficient. The commercial test is more important: can Zhipu defend economics inside the coding workflow, retain users, and capture enterprise value despite low switching costs?

The feedback supports the relative preference for Zhipu over MiniMax. It does not remove the need for commercial proof.

## MiniMax: least well received; scarcity alone is not enough

MiniMax drew the most negative relative feedback among the names discussed.

Investors focused on the failed price increase, the pricing floor set by DeepSeek, Zhipu's capital advantage, and the lock-up that clears around July 8. The recurring question was whether scarcity can continue to support the stock if relative fundamentals remain weak.

We are cautious on names whose thesis depends mainly on base-model differentiation. MiniMax is the clearest case. The next model cycle, pricing power, customer retention, and technical selling pressure around the lock-up matter more than headline parameter counts. A clean lock-up clearance could support the stock tactically. But without evidence of pricing power and retention, scarcity is a fragile foundation.

## Kuaishou: Kling is interesting; parent value capture is the debate

Kuaishou interest was concentrated almost entirely in Kling rather than the core business.

Investors cited a private valuation around US\$16-18bn and a possible IPO valuation of US\$25bn–30bn within six to twelve months. We treat those figures as investor-stated and unverified, not as our valuation target. The point is not the exact number. The point is that investors see Kling as a potential hidden asset, while remaining unsure how much value reaches Kuaishou shareholders.

The equity bridge is the entire debate, in our view. Investors need clarity on ownership, dilution, listing structure, holdco discount, revenue trajectory, model quality, and the degree to which any Kling value can offset pressure in the core short-video business. Without that bridge, Kling remains an interesting asset rather than a clean equity thesis.

## Where the trip sharpened our thesis

The trip did not change the sector call. It sharpened where we should demand proof.

For the sector, broad cheapness is not enough. China Internet needs catalyst density, revision stabilization, and observable AI payback to compete for capital. The feedback argues against chasing broad beta without proof.

For Tencent, the call stands, but the burden shifts further toward AI KPIs and disclosure. Tencent remains a patient core Overweight rather than a valuation-led urgency call.

For Alibaba, the feedback strengthens the tactical case. Cloud margin is the cleanest large-cap proof point, and this is where reported traction can most directly change positioning.

For Baidu, the event path is more compelling than the platform narr

[中间内容因长度限制已省略]

re subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
