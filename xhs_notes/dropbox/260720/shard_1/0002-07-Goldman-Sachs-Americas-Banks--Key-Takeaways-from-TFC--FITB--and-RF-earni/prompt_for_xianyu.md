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
# Americas Banks: Key Takeaways from TFC, FITB, and RF earnings

TFC: Expecting a \~14%+ ROTCE in 2026; sees \~10% fee growth in 2026

TFC reported decent 2Q26 results as core PPNR came in ahead of street (Visible Alpha Consensus Data) expectations as lower NII was more than offset by higher fees and lower expenses (incl. adj. for NQDCP). On credit, NCOs came in lower than expectations (50bps. vs. cons of 55bps) which along with a lower provision helped to drive the EPS beat. The focus was on TFC's updated 2026 / 3Q26 outlook, which pointed to lower revenues for 2026 (+3.5 -4%, down from \~4%) and a lower 3Q guide (\~1% downside to street PPNR) largely on higher expenses and implies moderate PPNR improvement in 4Q (\~2% downside vs. street). The downside to FY PPNR was largely on lower NII where TFC sees lesser improvement vs. prior expectations (had expected modestly up for full-year now guide implies flat to down) while TFC took up its fee income expectations to +10% YoY (vs. HSD prior). Additionally, TFC laid out a plan for some balance sheet optimization where it expects lower production in indirect auto while shutting down marine and RV lending given a focus on improving profitability and while it continues to expect loan growth of +3-4% (high-end) it sees flat to 1% growth in consumer with the rest coming from commercial (largely C&I). Lastly, TFC slightly refined its 2026 ROTCE expectations where it now expects a \~14%+ ROTCE vs. \~14% prior.

Ryan M. Nash, CFA
+1(212)902-8963 | ryan.nash@gs.com
GS & Co. LLC

Shares were in-line (-1.41% vs. KRE -1.58%) as the market digested the results and lower guidance. Looking ahead while guide was mixed, we believe positioning was negative on concerns of the risk of TFC lowering guidance. Now that it happened, we walk away somewhat upbeat on the fundamentals from here, as: 1) despite the softer NII message from a lower NIM (tighter loan spreads, swaps coming on, lower betas), TFC is seeing stronger fee income growth as it noted expectations for \~10% YoY growth (likely led by IBD and trading) and with an improved fee mix for the year this should help support the >14% ROTCE expectation even further, 2) loan growth was soft in 2Q given a decline in C&I as well as the planned reductions in indirect portfolios; however, the constructive backdrop for commercial lending should allow TFC to reach the high-end of its loan growth guide in 2026 (2Q EOP implies 4% growth already). Additionally, while the guidance implies shrinking consumer loans on an EOP basis, the reduction in lower-returning loans should be accretive to its ROTCE given a) an ability to payoff high-cost funding, b) a higher mix of commercial lending which is likely higher-returning, 3) the message on ROTCE for 2026 was positive, with TFC taking up expectations to \~14%+ (vs. \~14% prior) despite the NII headwinds and while commentary on the call pointed to expectations for continued ROTCE improvement in 2027 / 2028, TFC's message on retaining the right of

Lucas Haimes
+1(212)902-3305 |
lucas.haimes@gs.com
GS & Co. LLC

flexibility to achieve its ROTCE goals likely provides a path for its new CEO to make adjustments to the timing of when its 16-18% ROTCE goal can be achieved. With shares trading at \~1.6x P/TBV (peers at 1.8x), the market believes that profitability will continue to lag peers though with numbers likely in a better place for 2026, we think performance from here will come down to what the incoming CEO's message is on return expectations for 2027+. Therefore, if TFC is able to deliver on improving returns in 2027, shares should have meaningful upside over time.

Exhibit 1: TFC guidance summary

<table><tr><td colspan="4">2026 Guidance Table</td></tr><tr><td colspan="4">TFC</td></tr><tr><td></td><td>3Q26</td><td>2026</td><td>Medium/Long-term</td></tr><tr><td>NII</td><td>- NII expected to increase 1% driven by an additional day and higher client deposit balances- Expect NIM to modestly improve throughout the year via fixed- asset repricing</td><td>- NII expected to grow 1-1.5% from a baseline of $14.6bn- Expect swaps for 3Q/4Q of $100mn/over $100mn-$42bn of loans rolling off at 6.43% (6.90% roll-on yield)- $15bn of securities rolling off a 3.76%</td><td>- Make progress in 2026 towards the 3 teens NIM number have talked about and hope to get there in 2027- Expect 3.5-4%+ revenue growth in 2026 driven by NII growth, NIM expansion, and fees (QTD Update)</td></tr><tr><td>Fee Income</td><td>- Non-interest income to decline 1% from baseline of $1.56bn implying $1.54bn- Expect stable revenue in 2Q</td><td>- 10% growth in Non-interest income- Expect TM to grow LDD- Expect to grow IB LDD</td><td>- Expect capital markets to grow at LDD CAGR over time</td></tr><tr><td>Total Revenues</td><td>- Expect revenue to increase ~1%</td><td>- Expect revenues to increase 3.5-4%</td><td></td></tr><tr><td>Expenses</td><td>- Expenses expected to increase ~2% due to higher personnel expense from a baseline of $3.1bn implying $3.2bn in 2Q</td><td>- Expect expenses to grow 1.75% from a baseline of $12.1bn implying $12.3bn- Expect 275bps of positive operating leverage (GAAP)- Expect lower severance</td><td>- Expect to continue to grow OL</td></tr><tr><td>Balance sheet</td><td></td><td>- Expect LSD EOP deposit growth- Expect LSD EOP loan growth- Expect average loans to grow 3-4% with the bulk coming from C&amp;I and consumer up 1%- Loan growth to be more wholesale driven vs consumer- AEA will grow at slower rate through the year than average loans as average investment securities are expected to decline by 4-5%- Loan spreads expected down 5-10bps yoy- Expect auto and mortgage loans growth to slow or be flat- Deposit mix to be closer to 25% by the end of the year.</td><td></td></tr><tr><td>Credit</td><td></td><td>- NCOs are expected to be ~55bps- Do not expect reserve releases</td><td></td></tr><tr><td>Capital</td><td>- Targeting $1.2bn in share repurchases</td><td>- Targeting $5bn in share repurchases- Expect greater than 14% ROTCE- Expect dividend payout 30-40%, 30-40% buybacks, and leaving the rest to grow</td><td>- Targeting 15% ROTCE in 2027; 16-18% Long term- Trend towards 10% CET1 by 4Q27</td></tr><tr><td>Tax rate</td><td></td><td>- 14.5% effective, 16.5% FTE</td><td></td></tr></table>

Note: Expense guidance will be GAAP moving forward  
Source: Company data, GS Global Investment Research

## FITB: Expense synergies tracking better than expected; signals upside to 2027 loan expectations

FITB reported decent 2Q26 results as a slight PPNR beat was driven by core fees coming in modestly higher than expected while core expenses were lower while NII was in-line (in-line NIM and AEA). Provisions came in lower than expected and NCOs were a touch lower helping to drive the EPS beat. The focus was on FITB's 3Q / updated 2026 outlook which pointed to slight PPNR downside in 3Q due to the timing of cost saves and upside in 4Q along with updates on the progress of the merger where FITB pointed to consumer deposit campaign outperformance (\$2.5bn of growth; \$1bn initially expected), expense synergies tracking ahead of its initial \$850mn expectations (with upside potentially reinvested), and reiterated expectations for a Labor Day systems conversion with the remainder of expense synergies pulling through in 4Q.

Shares underperformed (-2.29% vs. KRE -1.58%) as the market digested the EPS beat along with somewhat upbeat guidance. We think the underperformance was driven by the softer PPNR outlook in 3Q26 (though we note the higher expenses is timing related), and it should see performance improve into 4Q with potential upside (which it may choose to reinvest). Looking ahead, the CMA integration appears to be tracking as planned or better (even posted 1% loan growth after 3-4 years of stability) and while the PPNR guidance has some moving pieces in 3Q it should improve by 4Q positioning FITB to deliver efficiency in the 51-52% range for the quarter (and 53% or lower next year). Given that, we remain upbeat on fundamentals, as: 1) EOP loans outperformed, with legacy FITB C&I growing \~2% QoQ while CMA C&I grew \~1% and FITB noted it expects the growth it saw to be sustainable (ex-macro changes). Post the conversion, FITB expects an acceleration in growth led by the CMA franchise (we model \~1.5% quarterly in '27) and with the street (Visible Alpha) looking for \~4% EOP loan growth in 2027 we think there is upside to 2027 growth expectations, 2) FITB noted it saw its Southwest and CA deposit campaign outperform expectations (\$2.5bn of growth vs. \$1bn of expectations) and while campaign promos typically come on at a higher cost, FITB noted it expects deposit costs to be stable to slightly up in a flat rate environment which should allow it to fund the stronger loan growth (particularly in 2027) it is expecting without diluting margin / returns, 3) the message on returns / growth was positive, with FITB continuing to expect to deliver a 51-52% efficiency in 4Q26 and a \~19%+ ROTCE in 2027 with incremental profitability from synergies / growth supporting investments in the business which should allow FITB to sustain a higher than peer TBV multiple (given its ROTCE) along with accelerating TBV growth which should support shares over the medium-term. While shares are trading at 11.6x our 2027E, a premium to peers at 10.8x, we believe it is due to the market's confidence in the momentum of the CMA transaction and ability to sustain peer-leading returns / TBV growth, and as FITB continues to deliver on the integration as well as execute on its medium-term targets, shares should have further upside over time.

Exhibit 2: FITB guidance summary

<table><tr><td colspan="4">2026 Guidance Table</td></tr><tr><td rowspan="2"></td><td colspan="3">FITB</td></tr><tr><td>3Q26</td><td>2026</td><td>Medium/Long-term</td></tr><tr><td>NII</td><td>- NII growth of 2-2.5% driven by extra days and fixed rate repricing- Forward curve expect hike in September- Deposit costs stable to slightly up even in a flat fed funds world- A hike would see asset-side repricing outweigh deposit costs, benefiting NII</td><td>- NII guided to $8.74-$8.80bn for FY, assumes 12/31/31 fed rate of 4.00%- Normalized margin expected to move into the 3.40s sometime next year.- Exit-2026 profitability and efficiency to align with (and likely beat) 2027 targets</td><td>- Expect receive-fixed swap rate of 3.44% by YE31 with notional value of $5bn (current 3.26%)- Deposit growth to remain MSD in long term</td></tr><tr><td>Fee Income</td><td>- Adj. noninterest income expected to grow by 1-3%</td><td>- Expected between $4.06-$4.16bn</td><td>- Capital markets mid to HSD growth business in the LT</td></tr><tr><td>Total Revenues</td><td>- Guidance implied adj. revenue up by ~2% and PPNR up by ~7%</td><td>- Guidance implies adj. revenue at $12.9bn and PPNR at $5.6bn</td><td></td></tr><tr><td>Expenses</td><td>- Expenses to trend down between 1-2%; included impact of anticipated amortization- 4Q is seasonally most efficient, so results should beat 53% efficiency</td><td>- Guided to $7.22-$7.26bn- The $850 mn of savings figure is unchange- On track to open 55 branches this year</td><td>- To have 600 branches by YE28- Will add 150 branches to CMA&#x27;s Texas footprint</td></tr><tr><td>Balance sheet</td><td>- MSD deposit growth is sustainable and can accelerate with marketing, supporting MSD loan growth</td><td>- Avg. loans to grow to $174-$176bn implying 2%; growth in 2H- Loan growth is sustainable barring a macro change, with broad confidence aided by Middle East de-escalation and settled tariff confusion.- For deposits 2H has seasonality with a 4Q ramp as commercial builds.- Growth accelerated and should not decelerate; legacy C&amp;I up over 2%, Comerica up 1% from flat, all production-driven.- Same-platform migration post conversion should accelerate blended C&amp;I growth.</td><td>- 2026 solar originations down 70-80% from 2025; don&#x27;t see till stabilization until 2028- Four $10 bn opportunities frame a $40 bn total over five to seven years: Southeast, Southwest, small business, and tech and life sciences.</td></tr><tr><td>Credit</td><td>- 2H net charge-offs of 30-35 bps</td><td>- NCO ratio between 30-40bps</td><td></td></tr><tr><td>Capital</td><td>- Buybacks resume in 2H- 3Q buybacks smaller given deal charges (~$50 mn-$100 mn) and loan growth dependency.</td><td>- Near term CET1 of 10.5%- Expect preferred dividend schedule to be at ~$32 in 4Q- 4Q back to normalized pacing of $200 mn-$300 mn per quarter.- 4Q is seasonally most efficient, so results should beat 19% ROTCE</td><td>- Expect AOCI accretion of =19%/~41% (~$0.34-$1bn) by YE26/YE28- Expect TBV to improve by +3%/+2%/+2% by YE26/27/28 from AOCI accretion assuming 10Y UST to be at 4.8% by YE28</td></tr><tr><td>Taxes</td><td>- Effective tax rate of 22.5%</td><td>- Effective tax rate of 22-23%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

## RF: Expecting stable deposit costs from here; NIM headed to 3.70% (with further upside over time)

RF reported decent 2Q26 results as PPNR was largely in-line (touch higher NII, higher fees offset by higher expenses) while the EPS beat was driven by stronger credit as lower

NCOs (42bps vs. street (Visible Alpha) of 47bps) and a reserve release. The focus was on its outlook where RF tweaked its fee guide to the low end of the 3-5% growth given softer capital markets activity, while leaving the rest of the outlook unchanged. The outlook implies 2H PPNR that is relatively in-line with street expectations. For 3Q (and implied 4Q), it pointed to NII up \~2% QoQ with a stable to modestly higher NIM in 3Q (vs 3.66% in 2Q) with an exit rate of 3.70% for YE26 which implied modestly stronger AEA trends. Additionally, within that it expects deposit costs to remain largely flat and noted that the margin should have a further upward bias over time driven by fixed rate re-pricing.

Shares underperformed (-2.31% vs. -1.58% for KRE) as the market digested the results and updated message. We are uncertain what drove the underperformance as positioning was negative coming in and the results were decent. Some pointed to a lower fee guide without signaling lower expenses (which tend to be linked) while others we spoke with cited the slower buyback. Looking ahead, while this was not an inflection quarter (more consistent), we come out reasonably upbeat on fundamentals, as: 1) despite fears of increasing competition for deposits in the Southeast, RF was able to hold lower deposit costs to 1.69% (from 1.72% in 1Q) and expects continued stability through year-end despite a lower benefit from CD repricing (roll-on roll-off rates now in-line) which should help support its expectations for margin expansion over time, 2) loan growth in 2Q was solid, with EOP increasing \~1.3% and while the first half benefited from line draws that RF does not expect to re-occur, it kept its average growth guide unchanged and we think the guide could prove conservative as 2Q's average loans are already up 3% vs. 2025's average and even with a little slower growth it should be well positioned for MSD+ growth in 2027, 3) the message on credit was solid, with losses in the quarter outperforming expectations and RF's guidance implying a low 40bps NCO rate in 2H (vs. expectations for mid-40s) which along with a \~3% QoQ decline in NPAs is supportive of RF's commentary that credit has largely normalized. Additionally, while RF didn't confirm this view, it recognized that losses could fall below 40bps given how well problem assets have been worked out and what the new pipelines look like (said it's being actively debated). Post results, shares trade at 11.1x our 2027E vs. peers at 11.0x. We believe if RF shows improving and sustainable b

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
