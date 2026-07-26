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
Rating Buy

## Company Meta

North America
United States

Reuters
META.OQ

Bloomberg
META US

TMT
Internet

## Meta Ambitions Need Meta Scale

We expect Meta to deliver another strong quarter, with advertising revenue likely approaching the high end of guidance as improving return on ad spend continues to attract incremental budget share. Our ad checks were overwhelmingly positive, highlighting stronger conversion performance, growing advertiser ROI, and sustained benefits from Meta's AI-driven ranking, retrieval, and campaign automation investments. The macro environment also appears to have improved from the weakness embedded in the original outlook, supporting our expectation for revenue of approximately \$60.5bn, modestly above consensus and close to current buy-side expectations which are approaching the high-\$61bn range. We think Alphabet's 2Q26 results (link), especially the steady q/q growth in Search revenue and accelerating YouTube revenue, are a positive read-through for Meta.

The setup for 3Q is similarly constructive. Our investor conversations suggest the buy-side is looking for the high end of guidance to reach approximately \$64bn. We think that bar is achievable if Meta sustains the recent magnitude of outperformance relative to its initial guidance, supported by improving ad efficiency, continued engagement growth, with growing contributions from business messaging. The broader implication is that the core business is producing sufficient growth to fund Meta's expanding AI ambitions while preserving meaningful earnings power.

Product momentum provides a second catalyst. Meta's release of Muse Spark 1.1, shortly after Muse Spark and (now discontinued) Muse Image, supports our view that Meta Superintelligence Labs has moved beyond rebuilding the company's training and post-training stack and into a faster, more predictable product cycle. The next-generation model is already in training, with Meta targeting a return to the frontier by year-end. We expect a more frequent cadence of model, assistant, creative, and agent releases to create recurring catalysts while improving engagement and advertising performance across the Family of Apps.

Meta is also building more visible paths to monetize AI directly. The rollout of subscriptions across Instagram, Facebook, WhatsApp, Meta AI, and creator/business products creates recurring revenue opportunities tied to premium features, additional AI capacity, and higher-value workflows. Separately, reports that Meta is evaluating third-party compute and hosted-model services introduce a potential direct return on the company's infrastructure investment. Raw compute sales could monetize older-generation or temporarily underutilized capacity, while a Bedrock-like API layer could establish a higher-

Date
24 July 2026

<table><tr><td>Rating</td><td>Buy</td></tr><tr><td>Price target (USD)</td><td>800.00</td></tr><tr><td>Price at 23 Jul 26</td><td>606.10</td></tr><tr><td>52-week range</td><td>789.46 – 525.72</td></tr></table>

Valuation & Risks

Benjamin Black, CFA
Research Analyst
+1-212-250-9218

Kunal Madhukar, CFA
Research Analyst
+1-212-250-9357

Benjamin Hui, Esq.
Research Associate
+1-212-250-2064

Key changes

Price target (USD) 810 800 -1%

Source: DB

quality recurring revenue stream around Meta-hosted models. Both initiatives should make the company's AI return profile easier for investors to underwrite.

Of course, Capex remains a key debate. Prior to Alphabet recently raising FY26 capex guide, we think there were limited expectations for Meta to increase its current 2026 guidance of \$125-\$145bn. However, now, it is likely investors fear an increase in FY26 outlook likely may be coming, although we would point out that Alphabet's raised capex guide includes the impact of both incremental capacity adds as well as price increases, and we do not think Meta may be adding more capacity (beyond what's currently planned) if it has spare capacity in the short term that it can rent to third parties. Looking further ahead, reports that capacity could rise from approximately 7GW in 2026 to 14GW in 2027 have shifted buy-side expectations for 2027 capex into the low-to-mid \$200bn range (we raise our estimate to \~\$210-\$215bn in 2027 and \~\$265bn in 2028). The headline investment is significant, although the directly funded amount could be lower after accounting for partner-funded capacity such as Hyperion and a growing contribution from lower-cost internal silicon. More importantly, a third-party cloud business would add a direct revenue stream against assets that investors currently value largely through indirect benefits to ads and engagement.

We expect Meta to maintain its FY26 total expense outlook. Recent restructuring actions should improve the company's underlying employee-cost trajectory, particularly in 2027, but higher restructuring and settlement charges are likely to offset most of the near-term benefit. The actions therefore improve the forward cost base without creating a meaningful reduction in reported FY26 expenses.

All in, Meta enters the print with improving advertising returns, a stronger product cadence, and increasingly credible paths to monetize AI directly. Capex would remain elevated, but the core business is generating tangible returns from those investments today, while subscriptions and third-party infrastructure sales expand the potential revenue opportunity. We maintain our Buy rating though lower our target to \$800 (from \$810), based on 24x FY27E GAAP EPS. In our view, Meta's shares modest discount to the broader market does not adequately reflect the durability of the advertising business or the growing monetization optionality across AI, subscriptions, business agents, and cloud infrastructure.

## Advertising checks point to upside

Our checks were broadly positive and suggest Meta's advertising business is outperforming our initial expectations. Advertisers consistently highlighted improved return on ad spend, better conversion performance, and growing willingness to allocate incremental budget to Meta. In our view, these improving outcomes are likely tied back to the cumulative impact of Meta's backend investments across Gem, Andromeda, adaptive ranking, creative automation, and Advantage+. Scaling these models across larger infrastructure clusters and training them on more data continues to improve conversion performance, creating a self-reinforcing cycle of stronger ROI and higher advertiser spend.

Engagement remains an important contributor. Instagram daily users continue to grow at a low-single-digit rate globally, while time spent is growing at a low-double-digit rate. One channel check indicated that client spend accelerated modestly sequentially during 2Q, supported by strong engagement and better pricing as advertiser ROAS improved. Meta's ability to grow engagement faster than users, and ad impressions faster than engagement, gives the company multiple levers to sustain advertising growth even as comparisons become more demanding.

United States  
United States  
Figure 1: Instagram daily users and time spent worldwide continue to grow Worldwide  
![](images/10a4aa1095d4e04b8f58017b90a0212b3ff6a2558aef72befb2a1e072c30ae5e.jpg)

![](images/7e08050fd20d8ddce7fc011422d77c2860c7c6cc88049894b624955933d03c5a.jpg)

![](images/d9893b6d65b13e935519d5b861322ec7fa40bd3a983ba3495cf9e7ad96494533.jpg)

![](images/d608d138b47cfdb5e98c39b040e9e9dc64f6c71d1a57903c3dc92bf44e57d61a.jpg)

The macro backdrop also appears better than expected. Meta's 2Q outlook contemplated demand weakness associated with the conflict in Iran, initially concentrated in the Middle East before extending to other regions and verticals. Conditions began improving during April, and the guidance assumed that improvement would continue. Our checks indicate that the recovery has held, with strength across newer verticals including GLP-1 and peptide-related advertising and no material deterioration associated with energy prices.

All in all, we raise our 2Q revenue estimate to \$60.5bn from \$60.3bn, reflecting stronger advertising checks and a better macro outcome than we originally contemplated. This represents roughly 27% y/y growth and places Meta near the top of its \$58-\$61bn guidance range. We think buy-side expectations are approaching the high-\$61bn range. Looking to 3Q, investors appear to expect guidance with a high end near \$64bn (up 25-26% y/y). We think Meta can meet that bar if the advertising platform maintains its current momentum.

## A rebuilt AI stack should drive a faster product cadence

Muse Spark 1.1 represents more than an incremental model update. Meta Superintelligence Labs spent its first nine to ten months rebuilding the company's AI organization, training infrastructure, and post-training stack while simultaneously developing Muse Spark. With that foundation now in place, the company should be able to scale models more efficiently and release products more predictably. The next-generation model is already in training, and Meta continues to target a return to frontier performance by year-end.

The release sequence is encouraging. Muse Spark established the new model foundation, Muse Image expanded Meta's image-generation capabilities (though this has been withdrawn), and Muse Spark 1.1 added agentic coding functionality. This faster iteration supports our view that product releases should become recurring share catalysts rather than isolated events. It also expands the range of use cases across advertising creative, Meta AI, coding, business agents, wearables, and consumer content generation.

The models are already clearly benefiting Meta's core business. Meta uses LLMs to understand and label new content across topics and tone, improving the signals sent into recommendation systems. Over time, we think Meta intends to transition toward an LLM-native recommendation architecture that can generate tokens and match them against both organic content and advertising inventory. The same scaling dynamic applies to Gem, Andromeda, and Meta's adaptive adranking models, where larger systems and more training data continue to drive conversion gains.

This positions AI releases as both strategic and financially relevant. Better models can improve content relevance, increase engagement, automate advertiser creative, strengthen campaign conversion, and deepen usage of Meta AI. The investment return therefore begins inside the existing advertising franchise before expanding into new revenue streams.

## Subscriptions create an explicit AI monetization layer

Meta is rolling out subscriptions across its consumer apps, AI products, and creator/business ecosystem. The current framework includes app-specific plans for Instagram, Facebook, and WhatsApp, AI subscriptions at \$7.99 and \$19.99 per month, and creator/business products at \$14.99 and \$49.99 per month. Consumer features include personalization, enhanced reactions, and insights, while AI plans provide greater capacity for compute-intensive activities such as reasoning and image or video generation.

The near-term revenue impact should remain modest relative to advertising, but we contend that the strategic implications are meaningful. Subscriptions establish direct revenue against AI usage and create a capacity-management mechanism ahead of more capable models. They also demonstrate that Meta can monetize AI through recurring revenue in addition to the embedded benefits flowing through ad targeting, creative automation, and engagement.

Meta AI usage accelerated following the Muse Spark release, and the company is now laying the commercial rails for users who want deeper functionality or consume more tokens. The company is also bundling advanced AI tools, analytics, discoverability, and support into higher-value creator and business plans. Our prior scenario work (see here for more) suggests the combined subscription portfolio could generate \$4.5-\$15.6bn of FY27 revenue and approximately \$1.30-\$4.60 of incremental GAAP EPS under modest penetration assumptions. These remain scenario estimates rather than forecast changes, but we contend they illustrate how small conversion rates across Meta's distribution base can create a material revenue stream.

Business agents add another medium-term opportunity. Meta is facilitating approximately 10mn weekly conversations between users and business AIs across its messaging platforms, up tenfold since the start of the year. The products currently remain free to use, but we think the company will likely establish a longer-term monetization framework that could combine subscriptions with volume-based pricing. We view this primarily as a 2027 opportunity, with the potential to extend paid business messaging into markets where labor costs previously limited adoption.

## Cloud sales could improve the capex return framework

Reports indicate that Meta is considering a cloud infrastructure business that could sell raw compute capacity and hosted access to AI models. A Bedrock-like offering would allow developers to use Meta-hosted models through an API, while a neocloud-style product could monetize excess computing capacity directly. While a formal announcement of cloud sales has not yet occurred (Anthropic is reported to be in early discussions to lease compute from Meta, with a potential value of roughly \$10bn), the strategic logic is increasingly clear.

We believe Meta can preserve its frontier-model ambitions while monetizing less strategic capacity. The company could reserve its newest Rubin-era infrastructure for internal training while selling access to older Nvidia systems, inference clusters, or temporarily underutilized capacity. The third-party market remains supply constrained, giving Meta a potential utilization backstop at attractive pricing, best evidenced by Alphabet's announcement to continue to leverage third party bridge capacity.

Raw capacity sales would reduce stranded-asset risk and provide high incremental flow-through because much of the associated capex, depreciation, leases, power, and infrastructure expense already sits in investor forecasts. A hosted-model API layer would be more strategically valuable, creating usage-based recurring revenue and increasing the value of Meta's proprietary models. Meta would need to build enterprise sales, support, billing, security, and developer tooling, suggesting an initial focus on bilateral compute contracts before expanding into a broader platform.

Our previous capacity analysis work highlighted a potential medium-term opportunity of \$15-\$36bn, with a base case of approximately \$24bn in annualized third-party revenue after incorporating the reported 14GW of 2027 capacity (see here for more). These scenarios depend on available capacity, utilization, pricing, and customer demand and are not included in our current estimates. However, they demonstrate why a larger infrastructure footprint could increase revenue optionality alongside the capital requirement.

## 2027 capex expectations have moved higher, but the net burden may be more manageable

Reports suggesting that Meta could expand from approximately 7GW of capacity in 2026 to 14GW in 2027 have moved buy-side capex expectations into the low-to-mid \$200bn range. Applying a simple \$35bn-per-GW assumption to 7GW of incremental capacity produces approximately \$245bn of investment, although that figure likely overstates the amount Meta will directly fund.

Hyperion could contribute approximately 1.0-1.5GW through a partner-funded structure, reducing directly funded incremental capacity to approximately 5.5GW. Meta's internal Iris/MTIA roadmap could also lower the blended cost per unit of compute. Servers represent a majority of data-center cost, a

[中间内容因长度限制已省略]

ble upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau
Group Chief Economist and Global Head of Research

<table><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Japan</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td>Tel: (852) 2203 8888</td><td>Tel: (81) 3 6730 1000</td></tr></table>

DB AG
21 Moorfields
London EC2Y 9DB
United Kingdom
Tel: (44) 20 7545 8000

DB Securities Inc.

The DB Center
1 Columbus Circle
New York, NY 10019
Tel: (1) 212 250 2500

DB AG
Filiale Singapur
One Raffles Quay, South Tower
Singapore 048583
Tel: (65) 6423 8001
"""
