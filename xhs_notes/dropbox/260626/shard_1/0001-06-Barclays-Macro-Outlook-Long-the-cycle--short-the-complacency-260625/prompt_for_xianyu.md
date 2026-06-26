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
Macro Outlook

# Long the cycle, short the complacency

The Q3 outlook hinges on a strong, broadening US earnings cycle offset by already-optimistic market pricing. While global growth – led by US profits, AI-driven capex, and a firm jobs market – remains intact, higher bond yields and richer valuations leave less room for error.

\- The US profit cycle remains the dominant force in global macro. Earnings are broadening beyond mega-cap tech, supporting hiring, capex and consumption. But markets are already pricing in much of the upside, leaving little room for error.

\- Central banks such as the ECB and BoJ will likely tighten policy at the margin, but we expect the Fed to stay on hold for the rest of the year. Bonds remain the most challenged asset class, as fiscal and inflation profiles are worsening globally. For yet another quarter, we prefer equities over fixed income from an asset allocation standpoint.

\- The semiconductor complex now represents a concentrated macro risk if sentiment turns. But order books are full well into 2027, vendor-financing concerns are exaggerated, and forward multiples reasonable. There may come a point at which the AI infrastructure build-out overshoots demand, à la 2000. But that reckoning, even if it comes, is likely a 2028 problem, not a 2026 concern.

\- Macro conditions are supportive but not overheating: the US labor market is firming without wage-driven inflation, and consumption shouldn't collapse despite a low savings rate. Europe and China are weaker, but neither is collapsing. Our economists forecast the global economy to grow $3.1\%$ in 2026. The global expansion should persist.

The market outlook for the third quarter rests on a tension: a (mainly US) profit cycle that continues to deliver against a market that has absorbed much of the good news. How that tension is resolved will determine financial markets in the coming months. We think the weight of evidence suggests the global expansion is still intact.

Exhibit A is corporate earnings, the single most important variable in markets today. An economy where profits are expanding 22% y/y (consensus for FY26), such as the US, does not roll over quietly. It pulls the labor market forward, sustains capex, and underwrites consumer spending even when other indicators flash caution. The question is not whether earnings are strong – they plainly are – but whether their breadth and durability can withstand headwinds: a

SIGNATURE

Ajay Rajadhyaksha $^{(i)}$ +1 212 412 7669
ajay.rajadhyaksha@BARC.com
BCI, US

Amrut Nashikkar $^{(i)}$ +1 212 412 1848
amrut.nashikkar@BARC.com
BCI, US

low US savings rate, central banks that are no longer easing, and a bond market demanding higher yields from sovereigns and corporates alike.

## Earnings: No longer a tech story

S&P 500 earnings growth was 19% y/y in the second quarter. That alone would be noteworthy. But the composition is as significant. The mega-cap tech names delivered 30% growth – impressive, but by now largely expected. The surprise was the rest of the technology sector, where EPS surged 50% y/y, a pace that suggests the monetization of AI is now well past the handful of names that have dominated for years. If consensus estimates of 22% EPS growth for 2026 are realized, it would, almost by definition, imply a robust economy.

Margins are expanding in materials, helped by the AI infrastructure build-out. Financials are benefiting from a rising equity market and robust deal activity. After a prolonged stretch of post-pandemic margin compression, healthcare is beginning to see operating leverage return. When the earnings cycle broadens thus, it becomes self-reinforcing: sector-level profit growth drives sector-level hiring, which supports households, which in turn sustains the demand that feeds next quarter's revenue.

The risk is that the world is already priced for it. At current index levels, markets are already expecting healthy, double-digit EPS growth in 2027. If margins compress – whether from higher input costs, rising borrowing costs, or a deceleration in AI spending – investors will start to get nervous. We do not think that is likely in Q3, or for the rest of 2026. Order books in key sectors (especially the all-important semiconductor vertical) remain full, corporate guidance has been broadly constructive, and capex commitments are contractual, rather than discretionary. But the market rally since March does mean we are more measured in our risk-friendly stance than three months ago.

## The US labor market: Firming, not overheating

If earnings are the engine of this cycle, the US labor market is the transmission mechanism – and it seems to be working. May payrolls surprised to the upside for the third straight month. The three-month moving average of nonfarm payrolls is now up nearly 200k from the three months ending in February. Job gains are more broad-based across sectors, including government, leisure and healthcare. After rising ominously in H2 25, the under-employment rate has dropped this year. Continuing claims have trended lower, and initial jobless claims remain subdued. Taken together, the signal is unambiguous: the labor market has bottomed.

The natural worry is that a tightening labor market feeds back into inflation through wages. It is a concern we believe is premature. Neither the Atlanta Fed's Wage Growth Tracker nor the Employment Cost Index is flashing the kind of acceleration that would force the Fed's hand. The unemployment rate has largely hovered around 4.3-4.4% for almost a year, instead of dropping quickly. This is a labor market that has stabilized, but not one that is running away from the central bank. At least for now. There is a tendency in macro analysis to treat any improvement in employment as the opening act of an overheating story. We think that framing skips several chapters. For wages to become a problem, you need sustained tightness: a sub-4% jobless rate, rising quits, employers bidding aggressively for workers.

We are nowhere near that. What we have instead is an economy generating jobs at a decent pace, but with enough slack to keep unit labor costs from spiraling. That is a favorable configuration, not a threatening one. For investors, the implication is straightforward. A firming labor market extends the earnings cycle: profits fund payrolls, payrolls fund spending, spending funds revenues. The virtuous loop remains intact. The risk would be if hiring surged to a point where wage costs eroded margins, but the data offer no evidence that this threshold is close.

The labor market is doing exactly what one would want it to do in the middle innings of an expansion: growing steadily without generating the kind of heat that forces a policy response.

The consumer: Weaker than the data suggest, or stronger than the bears admit? A firming labor market ought to translate into resilient household spending. But the headline savings data in the US tell a more cautious story. At 2.6%, the household saving rate leaves almost no buffer between the US consumer and a pullback in spending. The logic is simple: if households are saving almost nothing, any shock – a job loss, an energy spike, a wobble in confidence – forces an immediate retrenchment. Real disposable income growth reinforces the concern. On a per capita basis, it fell 0.5% in April alone, and on a year-over-year basis, it is declining at roughly 1.5%, the weakest reading since 2022. On its face, this looks like a stretched consumer.

We do think consumption will soften a little in H2, but are skeptical of any doom-and-gloom narrative. Not because the numbers are wrong, but because we have seen this story before. Twice in recent years, the Bureau of Economic Analysis has conducted annual revisions to the national accounts that substantially raised the saving rate after the fact. The most striking instance came in September 2024, when the BEA revised the saving rate from 3.3% to 5.2% through the second quarter, an upgrade of nearly two full percentage points. The source was a sharp upward revision to gross domestic income, which had significantly understated how much Americans were actually earning. In both episodes, the prevailing narrative was that the consumer was dangerously overstretched. In both cases, the revised data told us the opposite. We would not be surprised if a similar recalibration is ahead.

The weakness in real income growth deserves acknowledgment; it is the one element of the bear case that carries genuine weight. But it needs to be weighed against the forces running in the other direction. Fiscal transfers remain substantial. The federal deficit is still running at 5.5-6% of GDP, a level of government dissaving that puts significant income into household pockets. Financial wealth effects are large and growing: the S&P 500 is near record highs, housing wealth remains elevated, and IPO activity should create a fresh cohort of liquid wealth. And the AI capex cycle, now on track to reach a trillion dollars by 2027, is generating employment, income and demand beyond the technology sector itself.

Calling for a sharp consumer-led slowdown requires one to believe that soft real income growth will overwhelm the combination of fiscal support, buoyant asset prices, and the strongest corporate earnings cycle in years. That is a view we don't buy. The saving rate is likely overstating the fragility of household balance sheets, just as it has before. The offsetting forces are simply too large to support a conviction call for a strong pullback in consumption. The bears have a data point. They do not have a story that holds together.

## AI capital expenditure: The debate is over, the build-out is not

A year ago, the skeptics' case against the AI capex cycle had a certain logic to it. The technology was impressive, but the revenue models were unclear and enterprise adoption was nascent. There was a credible argument that the hyperscalers were overbuilding into an unproven demand curve. That argument has been overtaken by the numbers. Annualized AI-related revenues across the major cloud platforms have roughly tripled over the past year. Enterprise deployment has moved from pilot programs to production workloads. And the commitment pipeline has accelerated: aggregate AI infrastructure spending is on course to reach \$1trn in 2027.

When the companies writing the checks are simultaneously reporting explosive earnings growth from the same technology, the use-case question answers itself. Even away from the hyperscalers, the revenue growth of major AI “labs,” such as Anthropic and OpenAI, is

impressive. Anthropic for example is on track to become the fastest firm on record to reach \$40bn-plus in annual recurring revenue (ARR) this year, barely four years from founding. The debate about whether AI monetization is real is functionally settled. What remains is a question of magnitude, not direction.

The broader economy benefits from the second-order footprint of this spending. A trillion-dollar build-out does not stay inside data centers. It flows into power generation, electrical infrastructure, construction, cooling systems, and the labor required to install and maintain all of it. It reshapes capital allocation in materials and industrials, creating procurement bottlenecks that themselves generate pricing power for suppliers (and sometimes these prices can truly spiral, like memory chips). Semiconductor fabrication capacity, already stretched, is being expanded on multi-year timelines that lock in demand for years. This is not speculative expenditure that will be switched off in a downturn; much of it is contractual and under construction. For as long as this cycle runs, it acts as a structural tailwind to earnings, employment, and GDP growth that sits mostly outside the traditional business cycle. Investors may be tired of hearing about capex. The economy is not tired of receiving it.

## Semiconductors: The macro risk hiding in a micro sector

It is tempting to treat the semiconductor cycle as a sector-level concern, something for technology analysts to parse and for macro investors to observe from a distance. That would be a mistake. Of the 15-16 companies globally that exceed a trillion dollars in market capitalization (at the time of writing), barely a handful – Berkshire Hathaway, Aramco, Eli Lilly – are not related to technology hardware or the infrastructure that supports it. Nvidia is the world's most valuable company at around \$5trn. TSMC, Samsung, and SK hynix between them account for trillions more. The semiconductor complex is not a subsector of the equity market, it is now its heartbeat, and its gravitational influence extends well beyond share prices. Its influence is also extending into the credit markets. The hyperscalers will likely issue more than \$400bn in new debt this year alone, more than twice the amount they raised in 2025, making the semiconductor supply chain a first-order focus for credit markets. After all, when the semiconductor cycle turns, it does not turn gently. It snaps. And when it snaps, it takes the macro with it. That is what happened in 2000. And it is the reason macro investors should pay close attention to semis.

The comparison with the dot-com bust is the one that surfaces most often. In 2000, the telecom equipment sector, led by Nortel and Lucent, sat at the center of the technology complex in much the same way that semiconductor companies do today. Both were critical enablers of a transformative infrastructure build-out. Both attracted enormous capital flows on the promise that demand was structural and durable. Both had share prices reach levels that implied years of flawless execution. And when the cycle broke, the damage was catastrophic. Nortel's shares fell from almost \$87 to 18 cents. Lucent went from a \$60bn company to a forced merger with Alcatel. The collapse did not stay contained within telecom, it dragged markets down and then the economy. The semiconductor index itself famously fell 82% from peak and took decades to recover.

But the 2000 template, while instructive, breaks down on closer inspection. Nortel and Lucent were not just selling equipment into a boom; they were financing the boom themselves. Nortel extended over \$7bn in vendor financing to startup telecom carriers, many of which had little or no revenue and no viable path to profitability. Lucent aggressively lent money to its own customers and then recorded those loans as sales revenue, temporarily inflating reported earnings while accumulating enormous credit risk. When the startups defaulted, demand did not slow, it vanished overnight.

The semiconductor cycle today is fundamentally different in this respect. Nvidia's four largest customers, Microsoft, Alphabet, Amazon, and Meta, generated several hundred billion dollars in free cash flow last year. These are not leveraged startups buying chips on credit; they are the most cash-generative enterprises in the history of capitalism, funding purchases out of earnings and issuing debt from balance sheets that any sovereign would envy. That distinction matters enormously for the durability of the current semiconductor order book. In 2000, demand was a function of financing availability. Today, it is a function of competitive necessity. No hyperscaler can afford to fall behind, and the capital commitments reflect that – and so do semiconductor earnings.

SK Hynix reported a 72% operating margin in the first quarter of this year, surpassing Nvidia's peak. Samsung's first-quarter operating profit exceeded its entire full-year earnings for 2025. Forward price-to-earnings ratios for Samsung and SK Hynix sit at 6-7x. Even for a famously boom-bust sector, these are not worrying multiples. They are the multiples of a cycle

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
