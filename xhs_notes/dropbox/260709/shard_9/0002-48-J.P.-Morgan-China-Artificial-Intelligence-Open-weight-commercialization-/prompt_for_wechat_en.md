You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
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

The same logic applies beyond price. If DeepSeek keeps optimizing the official endpoint after the open-weight release, the official API can retain a quality advantage that is not fully visible from the model name alone. Third-party providers may advertise the same model family, but users may still see differences in answer quality, tool reliability, cache behavior, latency consistency and long-context completion as the official route incorporates more post-launch tuning.

Table 3: Different providers on the same model of DeepSeek V4 Pro offer different API economics

<table><tr><td>DeepSeek V4 Pro provider</td><td>Nominal input / M</td><td>Cache-read / M</td><td>Nominal output / M</td><td>Effective input / M</td><td>Cache hit rate</td><td>Estimated monthly cost*</td><td>Latency</td><td>Throughput</td></tr><tr><td>DeepSeek official route</td><td>US$0.435/0.870</td><td>US$0.004/0.008</td><td>US$0.870/1.740</td><td>US$0.061</td><td>93.5%</td><td>US$23.5-40.9</td><td>1.42s</td><td>45tps</td></tr><tr><td>Bailian Qianfan</td><td>US$0.761</td><td>US$0.063</td><td>US$1.521</td><td>US$0.549</td><td>30.2%</td><td>US$85.3</td><td>0.72s</td><td>24tps</td></tr><tr><td>Alibaba Cloud</td><td>US$1.608</td><td>US$0.134</td><td>US$3.216</td><td>US$0.830</td><td>53.8%</td><td>US$147.3</td><td>1.19s</td><td>19tps</td></tr><tr><td>GMICloud</td><td>US$1.131</td><td>US$0.094</td><td>US$2.262</td><td>US$0.458</td><td>64.9%</td><td>US$91.0</td><td>1.88s</td><td>40tps</td></tr><tr><td>SiliconFlow</td><td>US$1.600</td><td>US$0.135</td><td>US$3.135</td><td>US$1.330</td><td>18.2%</td><td>US$195.7</td><td>2.02s</td><td>22tps</td></tr><tr><td>NovitaAI</td><td>US$1.600</td><td>US$0.135</td><td>US$3.200</td><td>US$0.277</td><td>90.1%</td><td>US$91.7</td><td>1.77s</td><td>39tps</td></tr><tr><td>Together</td><td>US$1.740</td><td>US$0.200</td><td>US$3.480</td><td>US$1.150</td><td>38.3%</td><td>US$184.6</td><td>0.66s</td><td>39tps</td></tr><tr><td>Fireworks</td><td>US$1.740</td><td>US$0.145</td><td>US$3.480</td><td>US$0.773</td><td>60.6%</td><td>US$146.9</td><td>1.59s</td><td>32tps</td></tr></table>

Source: OpenRouter (data as of Jul 6, 2026); \* Estimated monthly cost is calculated under the assumption of 100M effective input tokens and 20M output tokens per month

Case Study #2: MiniMax M3 – similar headline price, better official-route quality
MiniMax M3 supports the same thesis from a different angle. The official route does not win mainly by charging a lower output price, as several providers show similar headline output pricing. The advantage comes from cache efficiency, realized input cost, usage concentration and speed. OpenRouter shows the MiniMax route with a higher cache hit rate and lower effective input price than selected third-party routes. Artificial Analysis adds the performance angle: MiniMax is among the fastest M3 providers, while lower-cost or quantized third-party routes can be materially slower. For agent and coding workloads, these factors matter because the user pays for task completion, not just raw tokens.

This is also where post-launch optimization matters. If MiniMax continues to

[中间内容因长度限制已省略]

e subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into

which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
