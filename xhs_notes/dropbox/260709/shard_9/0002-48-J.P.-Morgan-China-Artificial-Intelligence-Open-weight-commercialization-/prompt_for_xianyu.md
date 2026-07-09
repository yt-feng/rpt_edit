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
## China Artificial Intelligence

Open-weight commercialization playbook: winner takes more; Raise Zhipu to HK\$2,000 (OW), cut MiniMax to HK\$300 (Neutral)

Investors typically read open-weight releases as monetization leakage, since public weights allow third parties to deploy models outside the first-party API route. We agree, but we believe the more crucial question is whether LLM providers can turn reduced access control into wider distribution and paid conversion. In our view, the answer depends heavily on model capability – for competitive models, open weights can scale adoption on external GPU capacity across CSP, inference platforms and private deployments, rather than only on the provider's own compute stack. The LLM provider can still participate and monetize through official-backed routes, licensing, marketplace SaaS, revenue share, deployment support or enterprise co-selling, especially when customers care about model freshness, endpoint quality and reliability. For weaker models, reduced access control can lead to faster price comparison and traffic rerouting. This is positive for Zhipu, given GLM-5.2's globally competitive positioning, while more challenging for MiniMax, as M3 has not yet shown enough differentiation and pricing power. Open-weight commercialization is therefore becoming a 'winner-takes-more' framework.

\- Partner channels such as CSPs and inference platforms still have incentives to work with open-weight LLM providers because commercial customers are buying a production-grade model service, rather than just access to weights. A public release is closer to a starting checkpoint, while the official route can keep improving through post-launch model updates and serving optimization. If third-party deployments lag the official route, the same model name can deliver sizably different user experiences across endpoints. For stronger models, customer demand gives partner channels more reasons to support official-backed access, even when self-deployment offers better gross margins. This allows the model provider to keep a role in the economics of external compute capacity.

\- Recent launches fit this framework. Zhipu's GLM-5.2 release looks like a more confident open-weight strategy: widen adoption through permissive access, while keeping official route and higher-service variants (e.g. GLM-Turbo series) positioned for quality-sensitive demand. MiniMax adopts a similar strategy by keeping model open-sourced with additional commercialization restrictions, however, the key issue is model competitiveness, in our view. If users view the model as replaceable, open access makes it easier to compare, route and substitute; if the model is strong, open access expands reach and creates more routes back into paid usage. From enterprise users' perspective, open weights can also reduce adoption and accessibility risk, as users have a fallback route if hosted API pricing, access policy or availability changes.

\- We believe this framework provides sizeable optionality for Zhipu, while the revenue path still depends on sustained model leadership. At the current valuation, we think the market has largely moved beyond the company's US\$1bn year-end ARR guidance, while the broader open-weight monetization path remains less reflected. The key tests are whether GLM-5.2 represents a company-specific capability step-up, how Kimi K3 and DeepSeek V4.1 compare, and whether GLM-5.5/6 can extend the gap. We raise our Dec-26 PT for Zhipu AI to HK\$2,000 and reiterate OW. For MiniMax, the recent launch provides weaker evidence of model-led pricing power and paid conversion under this framework – we lower our Dec-26 PT to HK\$300 and maintain Neutral.

See page 21 for analyst certification and important disclosures, including non-US analyst disclosures.

Hong Kong

Olivia Xu AC
(86-21) 6106 6138
olivia.w.xu@JPM.com
SAC Registration Number: S1730525060001

Alex Yao
(86 21) 6106 6505
alex.yao@JPM.com
SAC Registration Number: S1730523020001

Daniel Chen
(86-21) 6106 6205
daniel.q.chen@JPM.com
SAC Registration Number: S1730521040001
JPM Securities (China) Company Limited

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>Zhipu AI</td><td>2513 HK</td><td>45,431</td><td>HKD</td><td>1,610.00</td><td>OW</td><td>n/c</td><td>2,000.00</td><td>Dec-26</td><td>1,800.00</td><td>n/c</td></tr><tr><td>MiniMax Group Inc - H</td><td>100 HK</td><td>9,419</td><td>HKD</td><td>323.80</td><td>N</td><td>n/c</td><td>300.00</td><td>Dec-26</td><td>400.00</td><td>n/c</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 07 Jul 26.

## Open-weight strategy: distribution upside, model-access pressure and a more flexible monetization playbook

Open-weight strategy has been an important part of the China large language model (LLM) market, and we believe the debate for investors is more focused on how these LLM providers use open distribution to build monetizable channels. We believe the commercial logic is to use open access to reach developers, cloud platforms, application programming interface (API) aggregators and overseas users faster, then monetize through official API, cloud partnerships, enterprise deployments and workflow products.

The cost of such open-source strategy is also visible: once a model is open-weight, cloud service providers (CSP), API aggregators and technically capable enterprises can deploy it on their own infrastructure. This creates competition for part of the traffic that may otherwise have gone to the LLM provider's first-party API. The pressure is most visible in simple workloads such as chat, summarization, translation, basic Q&A and other low service-level agreement (SLA) text tasks, where users mainly compare price and basic functionality. These tasks have lower requirements on model freshness, long-context stability, tool calling, prompt caching and enterprise support.

That said, open weights do not make all API endpoints equal. Running an open model is different from operating a high-quality production inference service. Third-party deployments can be cheaper or more widely available, while first-party APIs usually have better access to the latest model version, model-specific serving parameters, prompt caching, long-context execution, rate-limit management, toolchain support and enterprise SLA. For more demanding workloads, proprietary API pricing is tied to stable access to a higher-quality endpoint.

The quality gap can widen after the initial model launch. An open-weight release is usually a released checkpoint, while the official API remains a live product. After launch, the model provider continues to observe real-world traffic and optimize the model, the system layer and the serving stack. These follow-on improvements can include post-training updates, instruction-following refinements, coding and tool-use tuning, refusal-policy changes, routing logic, cache policy, context-window handling, decoding parameters and inference-kernel optimization. Most of these changes are not re-open-sourced in real time. As a result, third-party deployment of the same open-weight model may gradually fall behind the official API in both perceived intelligence and production reliability, even if the original base weights are identical.

This is especially relevant for coding, agentic and long-context workloads. In these tasks, users usually care about task completion, repo-level understanding, debugging quality, multi-step planning, tool reliability and latency consistency. Small differences in the serving stack can create visible differences in user experience. The same model name, therefore, does not guarantee the same product quality.

We therefore think open-weight strategy should be analyzed as a shift in revenue mix. LLM providers may lose part of the revenue tied to model access alone, while gaining a wider funnel for paid inference, cloud distribution and workflow monetization. The balance should vary by model quality: stronger models are more likely to attract developers, receive cloud platform priority and convert open-weight adoption into paid usage.

Table 1: Open-weight strategy reshapes the monetization mix

<table><tr><td>Area</td><td>Positive impact</td><td>Commercial pressure</td><td>What remains monetizable</td></tr><tr><td>Model access</td><td>Lower barrier for developers, CSPs, aggregators and overseas users</td><td>Third parties can deploy and resell the model</td><td>Latest versions, premium versions, commercial licenses</td></tr><tr><td>API usage</td><td>Wider user funnel and more trial demand</td><td>Simple workloads face more price comparison from non-proprietary APIs</td><td>API quality: latency, throughput, caching, uptime, SLA, model freshness</td></tr><tr><td>Cloud distribution</td><td>Faster global reach through existing cloud platforms</td><td>CSPs may self-deploy and earn 100% of API profit</td><td>Revenue share, official endpoints, enterprise co-selling</td></tr><tr><td>Workflows</td><td>Easier entry into coding, agent and enterprise ecosystems</td><td>Generic token pricing remains competitive</td><td>Task completion, reliability, integration, support</td></tr><tr><td>Enterprise deployment</td><td>More awareness and technical validation</td><td>Some enterprises can self-host</td><td>Private deployment, security, support, customization</td></tr></table>

Source: JPM estimates. (As of Jul 6, 2026)

## Open-weight is a dynamic commercial choice for LLM providers

Open-source should be analyzed by model version, license and channel. LLM providers can decide by model generation, capability tier, customer type and commercialization stage which models to open, how permissive the license should be, and which premium versions to keep in paid channels.

The 2025-26 release cycle shows three broad patterns among the major independent China LLM providers: DeepSeek sits closest to the permissive open-weight end of the spectrum; Zhipu uses permissive open-weight base flagships to drive adoption, while keeping selected Turbo / multimodal Turbo variants in managed API channels; Kimi and MiniMax show how modified or community licenses can preserve different degrees of commercial control.

For users, the open-weight route creates a fallback option. Once the weights are public, developers and enterprises can self-deploy, use a third-party inference provider or migrate across cloud routes if hosted access changes. This access certainty can support experimentation and ecosystem build-out. It also reduces fear that a model family could disappear from the user's stack after a policy change, access restriction or commercial dispute.

Table 2: China LLM providers are increasingly tiering open weights and monetization control

<table><tr><td></td><td>License</td><td>Conditional / restricted tier</td><td>API-led or managed tier</td></tr><tr><td>DeepSeek</td><td>MIT</td><td>Limited commercial restrictions in the MIT release</td><td>First-party API with aggressive pricing and cache-based economics</td></tr><tr><td>Zhipu / Z.AI</td><td>GLM-5 / GLM-5.1 / GLM-5.2 under MIT; GLM-5-Turbo / GLM-5V-Turbo are proprietary</td><td>No broad commercial restriction on GLM-5 / GLM-5.1 / GLM-5.2 weights</td><td>GLM-5-Turbo, GLM-5V-Turbo and other speed-optimized or multimodal-agent variants are primarily accessed through Z.ai API / managed channels</td></tr><tr><td>Moonshot / Kimi</td><td>Modified MIT</td><td>Modified MIT; attribution required above large-scale thresholds such as 100mn MAU or US$20mn monthly revenue</td><td>Additional restrictions on third-party commercialization</td></tr><tr><td>MiniMax</td><td>MiniMax community license</td><td>M3 uses a community license with commercial-use conditions</td><td>Additional restrictions on third-party commercialization</td></tr></table>

Source: JPM estimates. (As of Jul 6, 2026); Note: an open weight Massachusetts Institute of Technology (MIT) license means anyone can download, modify, fine-tune, and commercially deploy the model's neural network weights without paying royalties or facing restrictive terms, provided they include the original copyright notice

## API quality: proprietary APIs sell stable access to fresher and higher-quality models

Open-weight release increases model availability, but it does not make API products interchangeable. In production, users are buying a serving route rather than model weights alone. That route includes model freshness, cache policy, throughput, latency, feature support, reliability and provider-level optimization. We think proprietary APIs remain the most optimal choice to most of users because they offer the most stable route to the newest and highest-quality model variants, while third-party deployment can widen access with more variable economics and service quality.

Model freshness is increasingly important. An open-weight model should be viewed as a released checkpoint, while the official API remains a continuously optimized product. After launch, the model provider can keep improving instruction following, coding behavior, long-context stability, tool calling, refusal policy, caching strategy and inference efficiency based on live traffic. These optimizations are often absorbed into the official endpoint without a full public re-release of the weights. For users, the official API may behave like a fresher and more capable version of the same model, while third-party endpoints may still run the earlier open-weight snapshot or a less optimized serving stack.

The data points to two forms of first-party API advantage. DeepSeek V4 Pro is the price-led case: the official route is roughly 6-12x cheaper than selected third-party routes in a repeated-context workload, helped by lower list pricing and stronger cache economics. MiniMax M3 demonstrates the quality-led case: headline output pricing is broadly similar across providers, while the official route has better cache hit rate, lower realized input cost, higher usage concentration and stronger speed. These cases suggest open-weight distribution can broaden reach without fully commoditizing first-party API revenue.

Case Study #1: DeepSeek V4 Pro – official route wins through list price and cache economics

DeepSeek V4 Pro is the cleanest example of a first-party API using price as a moat. OpenRouter's provider-level data shows the DeepSeek official route has much lower effective input pricing and higher cache hit rate than selected third-party routes, while the model-level price also compares favorably before caching. In a simplified monthly workload with 100M effective input tokens and 20M output tokens, the official route costs roughly US\$24-41, vs US\$85-196 across selected third-party routes. The gap is especially relevant for coding agents, retrieval-augmented generation (RAG) and long-context automation, where repeated system prompts, repo context, tool schemas and intermediate state make cache efficiency a major driver of realized cost. We believe such effective pricing is more meaningful than list price, as it reflects what customers actually pay after prompt caching, and repeated context can make actual cost meaningfully lower than headline list price.

The same logic applies beyond price. If DeepSeek keeps optimizing the official endpoint after the open-weight release, the official API can retain a quality advantage that is not fully visible from the model name alone. Third-party providers may advertise the same model family, but users may stil

[中间内容因长度限制已省略]

es discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into

which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
