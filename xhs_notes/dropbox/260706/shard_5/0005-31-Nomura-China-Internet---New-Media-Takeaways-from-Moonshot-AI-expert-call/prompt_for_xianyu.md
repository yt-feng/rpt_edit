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
# China Internet & New Media

6 July 2026

EQUITY: INTERNET & NEW MEDIA

# Takeaways from Moonshot AI expert call

Commercial acceleration and strategic pivot

Key highlights

The NOM China internet team recently hosted a group call with an expert from Moonshot AI (unlisted), a leading Chinese generative AI startup. Its annualized recurring revenue (ARR) is projected by management to surpass USD1bn by year-end, driven primarily by overseas API usage and robust AI coding capabilities. Beyond AI coding, the expert believes that the next growth frontiers will be AI solutions for healthcare, education, and finance industries, where high-quality proprietary data will be a critical differentiator aside from specialised AI capabilities. To protect margins and improve monetization, Moonshot is shifting toward a closed-source strategy for its flagship models, while utilizing domestic chips to lower inference costs. While experts suggest pure-play AI labs like Moonshot could outcompete large internet platforms by maintaining pure focus, we continue to believe that major internet platforms such as Alibaba (BABA US, Buy) and ByteDance (unlisted) remain formidable competitors due to their vast capital, data ecosystems, and strategic need to own state-of-the-art (SOTA) LLMs (large language models).

## Who is Moonshot AI

Moonshot AI (Moonshot) is a Beijing-based AI startup focused on LLMs and AI assistant products. Founded in early 2023 by Dr. Yang Zhilin—a former Google Brain and Meta/FAIR engineer – alongside a group of his Tsinghua University alumni, the company has rapidly established a prominent position in China's generative AI landscape.

Moonshot's product and model ecosystem is built around the Kimi assistant and K-series foundation models. Its flagship foundation model, Kimi K2, is a trillion-parameter model featuring advanced coding and agentic capabilities. Subsequent iterations include Kimi K2 Thinking, Kimi K2.5, Kimi K2.6, and Kimi K2.7 Code. Moonshot has also expanded into specialized AI agent products, notably Kimi Code, Kimi Agent/Agent Swarm, and Kimi Work, with the latter positioned as a dedicated desktop AI agent for office workers.

The company is backed by a premier group of Chinese technology corporations and venture capital investors, including Alibaba, Tencent, HongShan, ZhenFund, and IDG Capital. Chinese media reported that Moonshot completed its latest funding round in May 2026, raising USD2bn at a post-money valuation of USD20bn. This round was led by Meituan, with participation from China Mobile, Tsinghua Capital, and other venture capital investors.

## ARR likely to surpass USD1bn by the year-end

According to the expert, Moonshot's annualized ARR reached USD400-500mn by mid-2026, with monthly ARR rising $10 - 20\%$ sequentially. Growth was particularly robust early in the year, expanding 2-2.5x y-y, supported by new product launches and accelerating model adoption driven by the hype around the desktop agent, OpenClaw. The expert projects that Moonshot's ARR could exceed USD1bn by the year-end.

Revenue composition is shifting materially toward API calls. According to the expert, API usage has become the primary revenue driver, followed by consumer-oriented subscriptions. Private deployment, including licensing and maintenance fees, contributes a relatively small share and has been declining as a proportion of revenue.

The expert attributed API growth primarily to continuous model iteration, increased usage by overseas developers, and the release of useful vertical capabilities such as coding. Subscription revenue is also growing, but at a slower pace than API revenue.

## Research Analysts

China Internet & New Media

Jialong Shi - NIHK
Jialong.shi@NOM.com
+852 2252 1409

Rachel Guo - NIHK

rachel.guo@NOM.com

+852 2252 1400

Geographically, the revenue mix has increasingly pivoted toward international markets. Overseas revenue contribution has risen steadily since the beginning of the year and now represents a larger share of total revenue than domestic operations. Sustained future growth remains heavily dependent on the continued expansion of overseas API calls, international subscriptions, model upgrades, and the deployment of specialized vertical capabilities, according to the expert.

The next major product catalyst is expected to be K3, which the expert suggests could be released around September 2026. However, the launch window remains flexible and may be adjusted depending on the release schedules of competitors such as MiniMax, Zhipu, DeepSeek, and Alibaba's Qwen.

K3's key areas of improvement are expected to include multimodal capability, enhanced coding performance, agent task orchestration, and enriched vertical capabilities, according to the expert.

In coding, the expert views GLM and Kimi as among the leading domestic models. DeepSeek and Qwen are also viewed by the expert as strong competitors.

Healthcare, education and finance likely to become the next battlefields for AI agents, after coding

AI coding currently represents one of the clearest commercialization paths for LLM developers, a trend heavily validated by the rapid monetization of overseas peers like Anthropic's Claude Code. However, the expert thinks that the long-term total addressable market (TAM) for AI coding may face constraints. The core addressable user base requiring sophisticated, high-frequency coding assistance is relatively price-insensitive but modest in absolute size. Further, international players like Anthropic and OpenAI have already captured a meaningful portion of high-value global demand, according to the expert.

Consequently, the expert believes that the next phase of enterprise competition is expected to shift toward larger vertical markets, specifically healthcare, education, and finance. Healthcare represents the most immediate opportunity due to the acute demand for AI capabilities in medical consultations, diagnostic assistance, imaging interpretation, automated report generation, complex case discussions, and pharmaceutical R&D. Both education and finance sectors present abundant use cases, though AI penetration in finance will likely lag education due to stringent regulatory and compliance constraints, according to the expert.

Value of high-quality data elevates for vertical AI agents

According to the expert, securing high-quality vertical data remains a key prerequisite for sharpening vertical model capabilities. Because this data is rarely accessible in the public domain due to commercial sensitivity and privacy regulations, internet platforms with proprietary transaction, operational, or user-behavior data hold a structural advantage.

The expert believes this data dynamic explains why large vertical platforms are opting to build proprietary models rather than relying on external foundation model providers. The expert cited Meituan as an example that has developed its own LLM, LongCat, specifically to prevent proprietary operational data leakage.

While the general-purpose foundation model market is expected to consolidate over time, the expert anticipates that highly viable, industry-specific solution providers will continue to emerge across the healthcare, education, travel, and finance sectors.

Unit inference costs on the decline due to increased adoption of domestic chips and improved infrastructure efficiency

On the infrastructure side, the expert said Moonshot has increased the proportion of domestic inference chips in its infrastructure, while still using NVIDIA H20 and other NVIDIA GPUs for part of its inference workload. Under the current compute mix, the expert indicated that the gross margin for K2.7-related inference workloads is approaching the $\sim 30\%$ level.

API price reductions are likely to remain an industry trend, driven by competition and declining inference costs. However, the expert does not believe price cuts necessarily imply significant margin compression. As domestic chip usage rises, inference concurrency improves, and resource utilization increases, unit inference costs should continue to decline which could offset the pressure from price cutting.

Pivoting towards a closed-source strategy for easier monetisation Moonshot's open-source framework serves as a balanced mechanism for developer outreach, public relations, and commercial monetization. Open-source models are highly effective for building brand equity and developer mindshare – particularly in overseas markets – by lowering the entry barriers for initial testing and showcasing technical capability under resource-constrained environments, according to the expert.

Conversely, unrestricted open-source distribution can dilute direct commercialization, as enterprise users may favor free local deployment over paid API integrations, dampening conversion rates. To mitigate this, the expert stated that AI labs like Moonshot are inclined to adopt a tiered model strategy over time. Under such a strategy, mid-tier and lower-tier models may be open-sourced to support developer ecosystems and market awareness, while flagship models are likely to remain closed-source and priced at a premium to protect monetization and gross margin, according to the expert. We note that Alibaba's Qwen initially favored broad open-source deployment but chose a closed-source, premium API delivery model for its latest flagship model, Qwen 3.7 Max.

## AI labs likely triumph over big internet platforms

The expert believes the general-purpose LLM market would undergo structural consolidation, ultimately leaving only a select group of players. The expert thinks that pure-play LLM developers like Moonshot and DeepSeek are well-positioned to compete effectively against large internet conglomerates like Alibaba and ByteDance, arguing that big internet platforms may risk diluting their focus by expanding across the entire AI value chain. In the expert's view, big platforms should and eventually will, focus primarily on cloud and AI infrastructure services, which are lucrative and easier to commercialise.

We do not fully agree with the expert's view regarding the ultimate landscape of the Chinese LLM industry. While independent AI labs currently hold a tactical lead in specific verticals like AI coding – owing to their first-mover focus – we believe large internet platforms remain formidable competitors in the broader LLM market. They possess deep technical know-how, unmatched capital reserves, and significant data ecosystems generated by their core internet operations.

We view it as highly unlikely that major tech platforms will de-emphasize their proprietary LLM initiatives simply because they are happy with the abundant revenue being generated from underlying infrastructure services. The strategic significance of owning a proprietary LLM extends far beyond standalone commercial monetization; it serves as the foundational core framework ("the brain") powering all existing and future consumer and enterprise AI applications. This strategic necessity will continue to drive large internet platforms to invest heavily to maintain SOTA model performance, in our view.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Rachel Guo and Jialong Shi, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

58% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 33% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

39% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

3% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 15% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

## Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with appl

[中间内容因长度限制已省略]

kets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page: http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
