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
NAVIGATING CHINA AI MODELS

# New frontier from Kimi K3; from cost efficiency, intelligence to pricing power of Chinese models

![](images/97ed7ad13f452c03dd397beae6233b51a35568484f31139e63415973eca5c9a6.jpg)

From cost efficiency (DeepSeek), rise in model intelligence (GLM) to new frontier/pricing power at Kimi K3

On July 17, the Kimi K3 open-weight model was released with 2.8 trillion parameters, and has set a new frontier in coding and certain agentic capabilities globally, as per Arena.ai coding rank and Artificial Analysis Intelligence score (Exhibit 1). Accordingly, we note K3's pricing was set at a new high amongst Chinese models, US\$2.3 per 1M tokens (blended) vs. Qwen3.7 Max of US\$1.4/Zhipu's GLM5.2 of US\$0.9/MiniMax's M3 of US\$0.22/DeepSeek's V4 Pro of US\$0.18, being still below global SOTA models, Exhibit 3.

As highlighted in our recent China LLM primer, we believe China's AI open-source/open-weight models are reaching a critical point of intelligence performance for global proliferation. Amongst signposts into 2H 2026, we have anticipated that competition could intensify in the high-end coding segment via coding data flywheel and scaling (to larger models, up to 2-5 trillions parameter sizes). We believe the share price reaction of Knowledge Atlas/Zhipu (where we recently initiated at Neutral, -28% on July 17) and MiniMax (Buy-rated, -16% on July 17) have been due to concerns around Chinese AI model competition and who the potential long-term winners will be, given the competitive landscape/sustainability of model company leadership remains highly dynamic.

We continue to note that independent AI model companies stand out in our Competitive Positioning framework. We also note positive read from Chinese President Xi's comments at the opening ceremony of World Artificial Intelligence Conference (WAIC) in Shanghai held today, drawing parallels of AI's societal impact to the invention of electricity and steam engines, and in offering China's technology infrastructure to developing nations with its continued open approach, yet cautioned on the need for human oversight/controls and risk mitigation.

What to watch out for from here? As highlighted in our LLM primer:

Ronald Keung, CFA
+852-2978-0856 |
ronald.keung@gs.com
GS (Asia) L.L.C.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Lincoln Kong, CFA
+852-2978-6603 | lincoln.kong@gs.com
GS (Asia) L.L.C.

Timothy Zhao  
+852-2978-2673 |  
timothy.zhao@gs.com  
GS (Asia) L.L.C.

## Damian Xie

+852-2978-1398 | damian.xie@gs.com
GS (Asia) L.L.C.

## Iris Xiao

+852-2978-0202 | iris.xiao@gs.com
GS (Asia) L.L.C.

## Steve Qiu

+852-2978-2672 | steve.qiu@gs.com
GS (Asia) L.L.C.

## Eunice Liu

+852-2978-7472 | eunice.liu@gs.com
GS (Asia) L.L.C.

Luqing Zhou
+852-3465-4207 | luqing.zhou@gs.com
GS (Asia) L.L.C.

Harness/agentic applications: We expect China AI model companies to increasingly focus on positioning their harness/agentic applications as key entry points, especially in coding (e.g. Zhipu's ZCode, Tencent's Workbuddy, and Alibaba's Qoder which are aggregate platforms that support the full suite of AI models) as model companies attempt to close the loop in capturing more real-life coding and agentic data for scaling. Co-work and industry expert agentic products could be the next priorities.

■ Multiple large parameter high-end coding model launches and potentially stricter access to the most advanced Chinese AI models outside of China: After Kimi K3 launch, we anticipate for further new Chinese AI model launches over 2H26 (Zhipu GLM, Alibaba Qwen, MiniMax M3 Pro and more) with significantly larger total parameter sizes of 2-5 trillion across Chinese AI model players.

Coding/programming segment competition will remain intense. The addition of multi-modal/visual understanding will also be the next upgrades amongst Chinese AI foundation models.

Continued suppressed API pricing for the lower end agentic-focused segment: We expect API pricing and therefore gross margins to remain under pressure at the lower-end pricing segment (around US\$0.1-0.2 per 1M tokens) into the second half, as China's AI model players have significant cash buffers post-fund raising to subsidize competitive pricing. As a result, we see financial strength as one of the three most important metrics (alongside pricing power and cost efficiencies) in assessing a Chinese AI model company.

Multi-modal/video-generation models to see further ARR ramp-up from global adoption: We expect continued healthy industry pricing and gross margins within video generation (unlike foundation text) where key players ByteDance's SeeDance (at reportedly 70% gross margins, latest US\$2bn ARR run-rate), Kuaishou's (Buy) Kling and MiniMax's (Buy) Hailuo/upcoming H3 models to enjoy healthy growth over 2H 2026 amid new functionality breakthroughs (combination of video-generation with LLM) and tight computing resources where demand significantly outpaces capacity.

We also expect increasing domestic ASICs supply, any stricter access to China's future most frontier models for overseas markets, Western markets' policies on China models, and access to high-end computing in model training as key swing factors/risks to our China AI model token/revenue growth trajectory.

## Our key ideas/stock picks

■ Within Cloud & Data Centers (our top preferred sub-sector within China Internet), we continue to highlight key ideas (Alibaba, GDS, VNET, and Kingsoft Cloud) on the back of higher AI hyperscaler capex spending into 2H 2026.

■ Within AI models, we highlight MiniMax on upside skewed risk-reward. Key swing factors for MiniMax to improve its overall competitive positioning will hinge on its pricing power following its recent completed fund-raising that has strengthened financial strength. We expect its H3 video generation model performance (imminent launch in a more favorable industry landscape vs. text models) and time-to-market for its next M3 updates (focusing on further coding intelligence level uplift from post-training/reinforcement learning, we estimate M3 update over July-Aug, and a larger parameter size M3 Pro model later in 2H 2026) will be the next key drivers.

## See also from our recent reports

■ Navigating China AI models: LLM primer: Critical point of intelligence for global proliferation, July 10, 2026

Knowledge Atlas Technology (2513.HK): Initiate with Neutral at US\$110bn valuation; China's top enterprise/coding AI model, July 10, 2026

MiniMax Group (0100.HK): Key focuses post-share unlock; upside skew to risk-reward; Buy, July 10, 2026

Exhibit 1: Code Arena have updated their global ranking...
Latest score and model ranking as of July 16, 2026  
![](images/e6e0b6381cd8105bf6aff2048715cf1cdb7564822d2aa48886142b6fd1180167.jpg)  
Source: LMArena, Data compiled by GS Global Investment Research

Exhibit 2: ...with Artificial Analysis Intelligence Index also reaching at/near global SOTA level Artificial Analysis Intelligence Index  
![](images/86042ab29dfe56d94b19464b91db3ed7f2db38644c593a46820b844bcac1cb8a.jpg)  
Source: Artificial Analysis, Data compiled by GS Global Investment Research

Exhibit 3: Kimi K3 raised blended API pricing on rising model intelligence and parameter size  
![](images/a46bf088dd38bf0d7f32c8b7d62afaa229de3bbcc2a875c586606cb66bc40721.jpg)  
Source: Artificial Analysis, Data compiled by GS Global Investment Research

Exhibit 4: Total cost to complete AA Intelligence benchmark test rises 3X, same scale with API pricing hike Cost per task (US\$)  
![](images/e5893d4287d711cb507509da50db6fadb0ca11e3eab79b199469bf99fabbb579.jpg)  
Source: Artificial Analysis, Data compiled by GS Global Investment Research

## Exhibit 5: Our competitive positioning analysis for key LLM labs/models

![](images/3c2d46c57db0e0cb5fc35cef616541b2bb44fbf6093d9292cd270c9217a4182d.jpg)

![](images/ccf2ed8be87a21365a4955ddf2424368a5174ee164960140046625cde65c8e46.jpg)  
MiniMax M-series: Unique full-modal capabilities among independent players; cost-efficient computing architectures

![](images/42a06729ef2c3efe9686cb23ccf74ad0360837172c3c48eb6bd4fc3ae793d49d.jpg)

![](images/b6d602490c9d2a4c4d84a7736b8dd728014593bd79b44a24503c61b91642e62a.jpg)  
DeepSeek: Extreme cost efficiency to sustain scalable token usage on competitive pricing

![](images/2dfe194c6ebf26ed8efc4acd622c23be57962ebcfe52479c8dea1418bece8091.jpg)

## Kimi K-series

![](images/4734bd0472296a21889ad370e2af4e12d6d0648431fe0f3d7929411366007e81.jpg)  
N/A for private companies valuation multiple

Source: GS Global Investment Research

## Exhibit 6: Competitive positioning framework for AI model players

![](images/6e52b5a0e8f6c93f6c0078351a1af2bdcdae1caaef06372a9e5b3d53afad565e.jpg)  
Source: GS Global Investment Research

## Price Target Risks and Methodology - MiniMax Group

We are Buy rated on MiniMax with a 12-month target price of HK\$860. Our valuation is based on DCF valuation, with 12% WACC and 2% terminal growth rate.

Key risks: Weaker-than-expected model performance amid the competition in the global foundation model industry; Slower-than-expected path to profit visibility; Weaker-than-expected commercialization capability; risks around IP/content generation; cash burn/self-funding capability; risks around geopolitics under an intensified tech race between the US and China.

## Price Target Risks and Methodology - Knowledge Atlas Technology

We are Neutral rated on Knowledge Atlas with a 12-month target price of HK\$1,880. Our valuation is based on DCF valuation, with 12% WACC and 2% terminal growth rate (consistent with our coverage).

Key risks: (+) Stronger-than-expected model intelligence, (+) Faster-than-expected path to profit visibility, (+) Additional non-inference take rate revenue streams, (+) Stronger-than-expected commercialization capability, (-) Competition in global foundation model industry, (-) Limited near-term profit visibility due to high R&D expenses, (-) Cash burn/self-funding capability, (-) Risk around geopolitics under an intensified tech race between the US and China.

## Price Target Risks and Methodology - Tencent Holdings

Valuation methodology: We are Buy rated on Tencent (0700.HK), with a 12-m SOTP-based TP of HK\$700.

Key risks: More intense industry competition in performance-based advertising, unexpected delays in game launches/Banhao approvals, moderated growth in FinTech and Cloud businesses, slower-than-expected AI development progress, reinvestment risk.

## Price Target Risks and Methodology - Alibaba Group

Valuation methodology: We are Buy rated on BABA/9988.HK, with SOTP-based 12-month target prices of US\$186/HK\$180 per ADS/share (FY27E-based).

Key risks: (1) Lower-than-expected GMV growth due to macro/competition; (2) Slower-than-expected monetization in China retail; (3) Weaker-than-expected execution in key strategic investments; and (4) Cloud revenue growth deceleration.

## Disclosure Appendix

## Reg AC

We, Ronald Keung, CFA, Allen Chang, Lincoln Kong, CFA, Timothy Zhao, Damian Xie, Iris Xiao, Steve Qiu, Eunice Liu and Luqing Zhou, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Ronald Keung, CFA GS (Asia) L.L.C., Allen Chang GS (Asia) L.L.C., Lincoln Kong, CFA GS (Asia) L.L.C., Timothy Zhao GS (Asia) L.L.C., Damian Xie GS (Asia) L.L.C., Iris Xiao GS (Asia) L.L.C., Steve Qiu GS (Asia) L.L.C., Eunice Liu GS (Asia) L.L.C., Luqing Zhou GS (Asia) L.L.C..

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

## Rating and pricing information

GDS Holdings (ADR) (Buy, \$32.75), GDS Holdings (H) (Buy, HK\$30.66), Kingsoft Cloud (Buy, \$10.06), Kuaishou Technology (Buy, HK\$43.28) and VNET Group (Buy, \$7.72)

The rating(s) for Alibaba Group (ADR), Alibaba Group (H), Knowledge Atlas Technology, MiniMax Group and Tencent Holdings is/are relative to the other companies in its/their coverage universe: Alibaba Group (ADR), Alibaba Group (H), DiDi Global Inc., Full Truck Alliance Co., J&T Global Express Ltd., JD Logistics, JD.com Inc. (ADR), JD.com Inc. (H), Jingdong Industrials Inc., KLN Logistics Group, Knowledge Atlas Technology, Meituan, MiniMax Group, PDD Holdings, S.F. Holding (A), S.F. Holding (H), STO Express, Sinotrans Ltd. (A), Sinotrans Ltd. (H), Tencent Holdings, Vipshop Holdings,

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
