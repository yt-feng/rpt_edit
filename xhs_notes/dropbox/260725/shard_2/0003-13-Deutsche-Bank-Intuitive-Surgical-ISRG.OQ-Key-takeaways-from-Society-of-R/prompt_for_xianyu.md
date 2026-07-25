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
Rating Sell

# Company Intuitive Surgical

North America
United States

Health Care
Medical Supplies & Devices

Reuters
ISRG.OQ

Bloomberg
ISRG US

Exchange NMS

Ticker
ISRG

Date
23 July 2026

Industry Update

<table><tr><td>Price at 22 Jul 2026 (USD)</td><td>340.69</td></tr><tr><td>Price Target</td><td>324.00</td></tr><tr><td>52-week range</td><td>592.85 - 340.69</td></tr></table>

# Key takeaways from Society of Robotic Surgery investor summit

Ahead of the SRS scientific sessions that kick off Thursday, today the Society held its annual investor symposium featuring program updates from senior executives of several robotic surgery companies as well as KOL panel discussions spanning an array of hot topics du jour including technology innovation, site of care, AI, and remanufactured instruments. This morning's earlier-than-expected US FDA approval of J&J's Ottawa generated considerable buzz, and herein we present key takeaways from panel discussions with leadership of J&J, Intuitive, Medtronic, and Stryker.

We also highlight some interesting findings from a large survey of SRS members (n=451 surgeons across specialties from around the world) that help inform the outlook for robot-assisted surgeries: technology adoption/procedure growth, competitive landscape, and structural trends like continued surgical volume migration to the ASC and expected impact of AI.

## SRS physician survey

On average, robot-assisted surgery penetration is expected to increase from 33% presently to 48% five years hence on a worldwide basis. This implies a WW robotic surgery procedure CAGR of +\~11% over this timeframe and continuing to be driven both by conversion of open to a MIS approach broadly and, within the latter, further shift from conventional lap to robot-assisted surgery.

In looking at the US survey respondent subgroup, robotic penetration is projected to rise from 64% currently to 69% over this timeframe – thus implying more modest robotic surgery volume growth relative to OUS/WW rates, which of course reflects a more penetrated US market vs internationally. This expected increase in US robotic penetration is expected to come exclusively from conversion of open surgeries as conventional lap usage is projected to remain flattish.

Notably, given the selection bias of this survey targeting SRS membership (with a median of 17 years of experience as an attending), technology adoption amongst this cohort is obviously higher than the overall market and hence this growth rate surely understates the overall market outlook. Indeed, the consensus view of all the companies remains that the overall soft-tissue robotic surgery global TAM is still $< 10\%$ penetrated.

\- Regarding competitive landscape, on a worldwide basis, Intuitive's da Vinci currently holds an $81\%$ installed base share, which is forecasted to

## Valuation & Risks

Imron Zafar
Research Analyst
+1-212-250-3676

Pito Chickering
Research Analyst
+1-917-635-9954

Kieran Ryan
Research Analyst
+1-212-250-6879

Ben Shaver
Research Associate
+1-212-250-9926

decline to 68% over the next five years, at which point Medtronic is expected to be the #2 player with Hugo garnering 10% terminal share amongst survey respondents.

In the US, da Vinci's installed base share currently stands at 98% and likewise is expected to decline in the years ahead – though expectations for Intuitive to maintain a still-dominant 84% share five years hence is notable in light of market entry of several competitors including Medtronic and J&J, who are entering this market with the advantage of a longstanding strong presence in surgical devices. One caveat here is that the survey was conducted in March, and given the rapid developments in this category (case in point being today's FDA approval of Ottawa), share dynamics will continue to be fluid – but the clear takeaway is that da Vinci remains well-positioned for clear and sustained category leadership.

\- Regarding site of care, survey data project that roughly one-third of all addressable surgeries will be done in the ASC setting five years hence. For frame of reference, we believe Intuitive's mix of procedures and installed base currently stands in the \~MSD range.

In terms of AI, survey data clearly portend a significant impact on various aspects of robotic surgery, with intra-operative anatomic intelligence and pre-operative planning expected to be among the most important benefits at least initially.

## J&J Ottava

While J&J's receipt of FDA approval for Ottawa was widely expected, this morning's timing was ahead of expectations (as evidenced by the fact that J&J did not come to SRS prepared to showcase the system to surgeon attendees).

■ Management pointed out that the de novo pathway to FDA approval (vs 510k) is noteworthy in terms of demonstrating the technology differentiation and simply not having a predicate necessary for the latter pathway.

One key differentiator of Ottawa that will clearly be central to the “sales pitch” is the significantly smaller footprint, taking up 30-50% less space in the OR – which will surely be a competitive advantage particularly in the ASC channel.

Initial FDA clearance includes a handful of general surgery procedures, with management noting that a steady cadence of additional indication approvals across other key specialties like urology and gynecology (and additional general surgery approvals like hernia) should follow in fairly short order.

\- Along with these additional indication approvals, J&J's pipeline will yield a steady output of new offerings ranging from digital, instrumentation, software, and beyond.

In terms of commercial strategy, like Intuitive, J&J plans to offer flexible Ottawa acquisition models, ranging from outright capex purchases to operating leases to per-click installations.

Notably, unlike Medtronic (and the typical medtech playbook in general), J&J made a deliberate strategic decision to pursue US FDA approval first rather than initially targeting OUS markets with an easier/faster pathway to regulatory clearance – which management cited as a sign of confidence in the platform.

In terms of OUS, management is next prioritizing the Japan and Western European markets, though refrained from providing estimated timelines

here.

While the company acknowledges the market dominance of da Vinci as it enters the soft tissue robotic surgery market decades later than Intuitive, confidence remains high that Ottawa represents a major growth vector for JNJ longer term given Ethicon's strong incumbent presence in MIS and the fact that global TAM penetration is still single-digits – hence the focus should remain more on market growth vs market share.

## Intuitive da Vinci

To preface, this panel discussion was pre-recorded a couple days prior to last week's 2Q results and hence the discussion did not hit on the sequential US volume slowdown nor management's reaction to this morning's approval of Ottawa.

\- Management is increasingly focused on the ASC channel given the continued shift of lower acuity soft tissue surgeries to this site of care. While the current da Vinci business mix (both installed base and procedures) in the ASC segment is currently single digits, the company noted that \~70% of all US ASCs are aligned with IDNs that already have da Vinci systems in the hospital setting – and as such is working collaboratively with these customers as they reallocate the lower acuity cases to the surgery center and thus freeing up more capacity for more complex surgeries to be done in the acute hospital. As more hospitals upgrade to dV5, uptake of XiR in the ASC channel has been quite good given XiR's lower price point and the much greater cost sensitivity of ASCs.

■ Launch of EUP round two in 2027 is expected to yield higher technology adoption by lowering the per-procedure I&A expense specifically for high-volume, lower acuity surgeries, though we strongly suspect this was in part also a defensive strategic move given the intensifying competition from other robotic platforms as well as remanufactured instruments.

On remanufactured instruments, the company again noted that it has thus far not seen any meaningful hit from remanufactured instrument adoption and remains largely dismissive of this threat going forward, positing that the value proposition extends beyond just instrument ASP to include reliability, safety, etc. Our checks continue to indicate a much greater risk to the I&A segment relative to the company's stance.

As discussed below, Stryker's CEO again noted today that they are watching this remanufactured da Vinci instrument space with high interest.

As evidenced by last week's disclosure that a GI robot is in late-stage development, Intuitive has increased its investments in new platforms in pursuit of adjacent opportunities – with the “quintuple aim” remaining foundational to the investment strategy. No additional detail was disclosed on the GI platform relative to timelines etc.

In terms of capital deployment, organic investment remains the top priority (particularly on R&D), though external opportunities will continue to be evaluated in a focused and disciplined manner.

## Stryker

CEO Kevin Lobo, whose then-controversial venture into Mako in 2013 has, and continues to, pay off in spades as adoption of robotic-assisted recon surgery continues to increase and expand into new categories.

While Mako now accounts for $70\%$ of US and $50\%$ of Stryker's global knee recon procedures, confidence is high that there still remains ample runway for continued growth/share gains in both the US and especially internationally. Ditto for Mako hip where penetration is still considerably lower and where uptake of revisions is seeing increasing momentum. Mako revision knee remains a work in progress, and while confidence here is high, no timelines were provided.

\- With Stryker's OUS sales mix remaining well below large cap medtech peers, this remains a top area of focus/investment and momentum in key businesses continues to build. While large markets like Japan, India, Germany, France and Canada have lagged in their adoption of Mako for various reasons, momentum in all is now building. For instance, in India, following significant implant price cuts in 2018, Stryker opted to deemphasize this market – but with economics here (both on the implant and Mako system sides) having improved, management noted that this is now one of the highest growth geographies for the recon franchise.

■ Launch of the handheld Mako RPS robotic system continues to be very well received and which management expects to help sustain the share gain momentum in knee implants. Indeed, the company noted that a majority of early unit placements have been at competitive accounts. Stryker has not seen, nor expects to see, any cannibalization of Mako by the RPS launch.

\- Rollout of Mako 4 continues to gain momentum, with management remaining bullish on the shoulder recon opportunity where expectations remain for Mako to yield market expansion given the highly challenging nature of the conventional approach that has limited the number of orthopedic surgeons doing the procedure. Mako should drive higher treatment rates.

On soft tissue surgery, this remains an area of high interest and potential M&A opportunities continue to be evaluated, with management again noting that entry into this space would surely be via acquisition. He pointed out that, unlike J&J and Medtronic whose entry into this category was largely defensive given their strong incumbent presence in laparoscopic devices, such a move by Stryker would be purely offensive and hence will continue to be disciplined on this front.

\- When asked about remanufactured da Vinci instruments, management once again confirmed that it is watching this space with high interest – and any such move here by Stryker would obviously have big implications for Intuitive.

In terms of other robotic opportunities, management noted that robotic stroke intervention technologies are of high interest – and here too any such move here would be via acquisition vs organic R&D investment. Broadly speaking, stroke continues to be an increasing area of focus at SRS this year by other development-stage companies.

## Medtronic Hugo

While disclosures around Hugo adoption (installed base etc) continue to be frustratingly limited, directional commentary from management continues to be positive – particularly internationally where the system has now been approved/launched for some time and has broader clearances.

While US approval is still limited to urology, clearances for general surgery and gynecology are in pursuit and once in hand will allow Hugo to address \~80% of the soft tissue robotic surgery market – and thus compel more hospitals/ASCs to evaluate the Medtronic platform.

Management spun today's approval of J&J's Ottawa as a positive for the overall robotic surgery market, arguing that technology penetration remains much more important than market share – also noting that global TAM penetration is still just single digits.

Medtronic's marketing pitch centers around five main differentiating attributes of Hugo: (1) modularity (enables flexibility in the OR relative to port placement etc.); (2) open visualization console that better facilitates collaboration in the OR vs the immersive da Vinci console; (3) advanced instrumentation like Ligasure that has been used in over 35 million procedures; (4) digital surgery (Touch Surgery ecosystem now in over 1500 ORs); (5) partnership model with customers.

# Appendix 1

Important Disclosures

\*Other information available upon request

<table><tr><td colspan="4">Disclosure checklist</td></tr><tr><td>Company</td><td>Ticker</td><td>Recent price*</td><td>Disclosure</td></tr><tr><td>Intuitive Surgical</td><td>ISRG.OQ</td><td>340.69 (USD) 22 Jul 2026</td><td>2, 14, 24</td></tr></table>

\*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Important Disclosures Required by U.S. Regulators

Disclosures marked with an asterisk may also be required by at least one jurisdiction in addition to the United States. See Important Disclosures Required by Non-US Regulators and Explanatory Notes.

2. DB and/or its affiliate(s) may act as a market maker or liquidity provider in the financial instruments issued by this company.

14. DB and/or its affiliate(s) has received compensation from this company within the past year for non-investment banking related services.

## Important Disclosures Required by Non-U.S. Regulators

Disclosures marked with an asterisk may also be required by at least one jurisdiction in addition to the United States. See Important Disclosures Required by Non-US Regulators and Explanatory Notes.

2. DB and/or its affiliate(s) may act as a market maker or liquidity provider in the financial instruments issued by this company.

24. DB and/or its affiliate(s) is or has been over the previous 12 months party to an agreement with the company relating to the provision of services set out in Sections A and B of Annex I of Dir

[中间内容因长度限制已省略]

ted performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
