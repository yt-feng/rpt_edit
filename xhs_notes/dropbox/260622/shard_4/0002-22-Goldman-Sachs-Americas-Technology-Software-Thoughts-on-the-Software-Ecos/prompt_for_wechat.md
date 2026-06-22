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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
AMERICAS TECHNOLOGY: SOFTWARE

# Thoughts on the Software Ecosystem post Databricks DAIS (SNOW, PLTR, MSFT, Apps)

We met with several industry experts at and around the Databricks' Data & AI Summit in San Francisco, 6/15-6/19. Databricks presented several architectural ideas that we believe are key to where the Software industry is going, including: a) the importance of open standards and easy data ingestion such that customers can maintain good data hygiene and a single source of truth, and drive better quality AI outcomes; b) an emerging TAM in custom agentic apps tailored to enterprise-specific use cases that sit in the white space between classic SaaS systems, in turn supported by a unified operation system/ontology layer with governance and model controls. Our conversations suggest that the value in the software stack will increasingly accrue to vendors that can enable these two architectures: today, SNOW, PLTR & Databricks; and over the medium term, potentially MSFT, NOW and app vendors that figure out how to monetize headless.

Gabriela Borges, CFA
+1(212)902-7839 |
gabriela.borges@gs.com
GS & Co. LLC

Maura Hager  
+1(212)9028724 | maura.hager@gs.com  
GS & Co. LLC

Selina Zhang  
+1(212)357-9979 |  
selina.zhang@gs.com  
GS & Co. LLC

## Key takeaways:

1. Good sticky vs. bad sticky: We have been using a simple litmus test to assess the durability of Software moats: “good sticky” companies are innovating at an accelerating pace on core differentiators and have products that their customers love. “Bad sticky” companies may have innovated less over the last several years, but are sticky because of the costs associated with migration, and generally have high levels of customer complaints or low levels of customer engagement and usage. We expect bad sticky moats to be eroded, in part because it is now much easier to use AI to streamline migrations. In our view, Databricks’ pace of innovation coupled with their push towards open ecosystems raises the bar on what it means to be a “good sticky” company:

While pace of innovation cannot be measured by the number of product releases alone, several industry experts highlighted that Databricks announced several product releases that are significant in the pain points they address, such as LTAP (which allows analytical and transactional engines to operate from a single open-format source of truth) and opensharing (an open protocol for sharing data, models, agents and skills across any cloud/vendor).

Today, it is clearly in Databricks' interest to lower barriers to switching to Databricks from legacy data management platforms; however, the company also acknowledges customer freedom such that if a more innovative non-Databricks solution arrives, it will also be easy to run a multi-vendor ecosystem or switch off Databricks. This likely creates an upward bias to Databricks' R&D and M&A intensity (Databricks plans to manage to FCF breakeven), but it also drives the company's strategy to be aggressive in how it disrupts adjacent TAMs (like SIEM and CDP) and leverages moats like Unity Catalog into new markets (such as governance for agents). This in turn limits the potential for new entrants in the future. In the investor session, Databricks noted that it could choose to price 2x higher, but that short-term pricing optimization decisions often come at the expense of long-term competitiveness and LTV.

☐ We look for similar characteristics to identify “good sticky” companies in our publicly-traded coverage: assets like Shopify and Cloudflare stand out to us: their pace of innovation is high and their pricing is oftentimes disruptive with the goal of long-term market share momentum (consider Shopify’s comments that Shopify Plus is the best deal in enterprise software, and Cloudflare’s ability to price aggressively in SASE because of the low margin cost to serve, as SASE works via forward proxy and uses the same rails as CDN does for reverse proxy).

## 2. Custom vs. packaged apps and the blurring lines between infra and app

software: Databricks' Day 1 keynote introduced tools to build a new agentic app layer: while SaaS apps have historically existed in silos, the most interesting agentic applications are likely to exist in the white space between the silos. This lends itself to custom apps for business-specific use cases that capture a greater share of the agentic software TAM, and thus the entire Software TAM, than they have in the past (recall we have previously quantified a Software TAM uplift of 20% by 2030, implying a 2pt tailwind to industry growth, from 7% to 9%). In order to enable this new agentic app layer, customers need to build an intelligent operating system layer that pulls data from systems of record (in a headless architecture) and other enterprise data stores.

As best we understand, there are four key ways to build this OS layer: a) Databricks' new Ontology product, that includes functionality like OntoRank to prioritize data sources based on context; b) Palantir, which in turn leverages Databricks and Snowflake as building blocks, and moves the burden of engineering entirely from the customer to Palantir's FDE team; c) hyperscalers; recall Satya Nadella's June 14 post on frontier ecosystems, that emphasizes that every enterprise should have its own version of frontier intelligence that marries frontier models with their specific enterprise data; d) select AI point products, such as ServiceNow's agent control tower or privately-held Dataiku. We suspect the line of demarcation between custom and packaged will likely hinge on organizational complexity: more complex orgs and apps will likely be custom built; less complex including SMBs will likely leverage SaaS off the shelf offerings like Salesforce Agentforce or ServiceNow Control Tower. Given how early the agentic Software TAM is, we expect a rising tide to lift many boats; however, our conversations over the last 3 weeks (including at the SNOW conference) make us incrementally positive on custom apps as a driver of underlying consumption for Databricks, Snowflake and Palantir.

☐ Databricks is also directly addressing the cost of maintaining a custom app, in the context of the cost of building already having collapsed with coding tools. Recall that the cost of building an app is only one part of the equation; an organization also has to maintain their custom app in production, which ServiceNow has previously quantified as having a 5-10x TCO vs. SaaS. Many of the innovations that Databricks announced directly lower this maintenance TCO. For example, Unity Catalog acts as a universal governance layer embedded in ontology; ontology leverages a single source of truth; and LTAP collapses the need for otherwise brittle pipelines and ETL (extract, transform, load) processes between different data sources.

On competition vs. Palantir, Databricks noted a generally complementary relationship, in part because of Palantir's strong FDE motion and Palantir pulling through usage of Databricks. Based on our customer conversations, the biggest question is whether you are willing to trade off outsourcing the heavy lift on building the ontology for the risk of longer term lock in with Palantir, as Palantir's pricing model is recurring, but the value provided is weighted up front to its original ontology build. To this end, Databricks noted it will sometimes engage with Palantir customers upon their renewals who look to rebuild agentic workflows with Databricks.

3. New CDP and SIEM apps: Databricks described its evolution to date in four chapters: 1) Lakehouse; 2) next-gen Database products; 3) Agentic AI; and 4) agentic apps. Databricks has announced two Chapter 4 apps to date: SIEM (at RSA in March)

and CDP (customer data platform at DAIS last week), and sees natural expansion opportunities around these two vectors of security and marketing. Our conversations suggest that customers were already using Databricks as the cornerstone of their custom SIEM and CDP strategies; these announcements commercialize what more sophisticated customers were already doing. We believe these product offerings are likely to be compelling because they directly solve problems around data ingestion and aggregation; however, our customer conversations suggest it will likely take time for Databricks to build out its domain specific experience.

☐ For example, in Security, in addition to solving the key cost problem around data ingestion, Databricks may also need to introduce more sophisticated event streaming and correlation functionality, and build out its go to market. Recall that Cloudflare took several years to evolve its Security go to market before seeing more success in the 2025 time frame; and that Datadog is still in the process of crystallizing its security strategy after mixed traction in cloud security (per our customer conversations).

☐ We think milestones in CDP may come faster, as switching costs in marketing are generally lower than in Security, and customers can map good CDP functionality directly to more effective revenue generation.

4. When describing its product innovation, Databricks noted that while the rest of the industry is focused on agentic, it sees an opportunity to further advance the database technologies that in turn will support agentic. All of the new software being written today needs a database, and Databricks can provide database technology that takes outsized share in this greenfield TAM. Examples include LTAP, which solves a 40-year problem in database engineering with a unified data stack that spans both OLTP and OLAP databases; and Reyden, a new compute engine that powers real-time lakehouse queries. Databricks' product expansion aims to collapse a fragmented database and data infrastructure market, where enterprises have used separate tools for transactional databases, ETL, warehouses, BI, governance, and AI; into an integrated platform built on open formats, shared governance, and a common data layer. With the combination of product-market-fit and new innovation, Databricks' core revenue growth (excluding token pass through) has accelerated for the last 5 quarters. Key product announcements:

OLTP/LTAP via Lakebase: LTAP (Lake Transactional/Analytical Processing) represents a strategic move beyond Databricks' historical OLAP core into OLTP. With LTAP, Databricks now positions its platform as a single governed foundation spanning transactional, analytical, streaming, and operational data, structurally reducing reliance on ETL, replicas, and CDC pipelines that have long separated application databases from analytics systems. Lakebase is the architectural unlock: a serverless Postgres layer on open object storage that enables low latency operational workloads while maintaining shared, open data formats with Lakehouse. This expands Databricks' TAM while improving its competitive positioning to capture operational workloads that have historically sat outside its core competencies.

☐ Postgres for agents: Databricks framed Postgres as increasingly central in an agent-driven world, where workloads operate at machine speed and require cost efficient, deterministic, and inherently branchable environments. Lakebase introduces primitives such as near-instant database branching, enabling agents to safely fork datasets, experiment, write changes, and revert to prior states as needed. In our view, the emphasis on Postgres is critical, as agentic applications require not just read access to enterprise context, but governed, low latency transactional systems where agents can act safely, at scale, and with repeatability.

□ Data engineering: Lakeflow: New innovations in Lakeflow focus on minimizing upstream complexity through a unified, declarative framework for ingestion, transformation, and orchestration built natively on Spark. Lakeflow abstracts pipeline creation via no code and declarative constructs, while maintaining open, non proprietary execution under the hood. The innovation shifts toward operationalizing data engineering at scale: automated orchestration across >50 integrations, and tight integration with agents via Genie Code and Genie Ops. These innovations are important in alleviating data engineers' ongoing maintenance burden, which has historically consumed a disproportionate share of data engineering resources.

Data science/AI: Databrick's core lakehouse and data science positioning remains central as it provides the enterprise context layer for AI. The introduction of Genie Ontology and OntoRank create a structured graph across enterprise data, documents, and usage patterns, improving agent accuracy by $30\%$ and reducing runtime by $50\%$ . The broader implication is that Databricks is capturing incremental spend in AI infrastructure, semantic layers, and enterprise knowledge systems, beyond traditional ML workloads.

☐ Data warehousing: Databricks continues to expand beyond its roots in engineering and ML into a more comprehensive lakehouse architecture, anchored by its next generation compute engine, Reyden, which is designed to support both complex analytical queries and highly interactive workloads. The launch of Genie One, an agentic coworker, provides conversational analytics on data stored in Databricks, embedding analytics into natural language and automated decision flows.

Real-time analytics: Databricks launched Lakehouse//RT, a real-time Lakehouse powered by a new compute engine built for concurrency and latency demands of modern agentic enterprises (Reyden, discussed above). Historically, enterprises needed a distinct real-time serving layer, which introduced duplication, latency, governance tax, and higher costs; Lakehouse//RT eliminates this layer by querying live data in place under a single governance model. On standard analytical benchmarks, Databricks found sub-100ms latency at 12,000 queries per second, and noted customers have seen up to 16x better performance than existing specialized real-time serving stacks.

Exhibit 1: Databricks core growth has accelerated over the last 5 quarters as a function of its product market fit with AI; Snowflake is also starting to show acceleration, albeit to a lesser extent

\*Databricks expects ARR to grow 80% in 1H27, or \~65% when excluding token pass through

![](images/e5bdfa38d44b16fc8a473535c64caf10b4186188ed7faff83986e467ce13fa85.jpg)  
Source: Company data, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Gabriela Borges, CFA, Maura Hager and Selina Zhang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Gabriela Borges, CFA GS & Co. LLC, Maura Hager GS & Co. LLC, Selina Zhang GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS h

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
