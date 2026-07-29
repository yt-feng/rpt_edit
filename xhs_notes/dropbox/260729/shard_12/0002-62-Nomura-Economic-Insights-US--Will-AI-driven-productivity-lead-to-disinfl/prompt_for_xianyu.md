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
Economics - North America

## US: Will AI-driven productivity lead to disinflation?

\- We view Chair Warsh's optimism on the disinflationary impact of productivity as an important signal of his dovish inclination.

\- In theory, productivity can have either a positive or negative impact on inflation. Historically, there is some negative correlation, but the relationship is inconsistent and has performed especially poorly in recent decades.

\- The policy implications of productivity trends are subtle. In real time, strong productivity growth is a good reason to tolerate hawkish signals from growth or wages. This is different from assuming future productivity growth will drive incremental disinflation.

## Research Analysts

North America Economics  
Jeremy Schwartz - NSI  
jeremy.schwartz@NOM.com  
+1 212 667 9637

Ruchir Sharma - NSI
ruchir.sharma@NOM.com
+1 212 667 9186

Aichi Amemiya - NSI  
aichi.amemiya@NOM.com  
+1 212 667 9347

\- Warsh has not convinced other Fed officials that AI will be predictably disinflationary. His repeated emphasis on productivity and supply growth makes us skeptical that he will turn hawkish and support pre-emptive rate hikes though.

Fig. 1: Data point to little evidence for "disinflationary productivity" Correlation between trend productivity and headline CPI  
![](images/a46296bd1d08aac2578e272a599a2acee549e2949839fe93f8cdad723ea273a8.jpg)  
Note: Labor productivity is real output per hour of all persons. Following Gordon (2005), we define trend productivity growth as the HP trend of the 8 qtr change (with smoothing parameter as 6400, based on Gordon (2003))  
Source: BLS, BEA, Haver, NOM

As Fed Chair, Kevin Warsh consistently emphasizes productivity growth, suggesting this should be an important driver of policy decisions. One of his five task forces will focus on "productivity and jobs in an era of transformation." And despite aggressive editing through most of the June FOMC statement, one conspicuous addition was a reference to strong productivity growth.

Warsh claims that technological progress is a reason to expect disinflation. Before his nomination, he wrote that “AI will be a significant disinflationary force.” In his Humphrey-Hawkins testimony he added that “productivity improvements over time will be structurally disinflationary,” and that “everything technology touches ultimately gets cheaper.”

In this note, we argue that productivity is not inherently disinflationary. In the near term, technological progress is driving investment higher, likely boosting inflation. Many (including Warsh) argue that relief is on the way from a future productivity payoff, but we do not see evidence for a clear directional impact.

In real time, productivity can be a helpful benchmark for gauging inflation trends – if productivity accelerates, it should make policymakers more willing to tolerate stronger growth in output and wages.

This is different from assuming future productivity growth will drive incremental disinflation though. Productivity itself tends to drive output and wage growth trends. Consequently, even if it seems certain that there would be an acceleration in labor productivity in the future, this would not be a sufficient reason to forecast a gap between wage growth and productivity or between actual output and potential.

## Is productivity disinflationary in theory?

There are early signs that AI diffusion is leading to productivity gains. That said, the read-through to inflation and interest rates is not clear.

In theory, productivity can have either a positive or negative impact on inflation.

Intuition tends to point to a disinflationary impact. For any particular business or industry, productivity growth typically leads to cost cutting and falling prices. Economic history adds to the intuition for “disinflationary productivity.” Under certain policy regimes – like a gold standard – productivity growth tends to be disinflationary. A managed money supply will tend to keep nominal GDP steady – implying faster real growth will lead to cooling inflation. Indeed, strong productivity growth is often cited by economic historians as a factor behind deflationary episodes in the late-19 $^{th}$ century $^{[1]}$ .

What we think this intuition misses is the dynamic impact of productivity on demand. Productivity raises real income, and more importantly, can incentivize business capex. This implies that even if the most productive sectors see cost relief from productivity gains, the economy-wide effect could be inflationary. Again, the policy regime matters. This demand channel could be especially prevalent for modern central banks, which target interest rates and manage financial conditions.

## Inflation pressure has already materialized

This inflationary impact of technological progress is already on clear display. Capex in AI is booming (Fig. 2), driving up tech component prices and leading to inflation pressure for consumer electronics (Fig. 4).

Fig. 2: Earnings calls and anecdotal evidence indicate businesses are increasingly willing to spend on capex
Hyperscalers' capex plans  
![](images/93007ae72fea6cea82cb67ac8c933e6c3349451189ea82a89d87965508ba6d88.jpg)  
Source: Company filings, Bloomberg, NOM

Fig. 3: Strong capex appears to be broadening out to other industries  
![](images/b38e47d40253491b4e7f234dec58d4351ef38b45648022128b72da9da68b8398.jpg)  
Source: BEA, Census Bureau, Haver, NOM

With the Fed remaining on hold, there is no circuit breaker for this strong demand. Financial conditions have remained easy, and rather than crowding out other sectors, strong capex appears to be broadening out to other industries (Fig. 3).

From the perspective of a hyperscaler, policy likely appears procyclical. Given rapid price increases for tech equipment, the “real interest rate” for pulling forward debt-financed investment is likely deeply negative (and becoming even more negative as demand strengthens) (Fig. 5). Earnings calls indicate businesses are increasingly willing to spend on capex, with activity only constrained by supply and availability of equipment.

Fig. 4: Booming capex in AI is driving up tech component prices  
![](images/755015175ff526658ed046988a4bb148e6791ff8bf35d34a82447416d11afa53.jpg)  
Source: BLS, Haver, NOM

Fig. 5: Rising equipment costs incentivize hyperscalers to frontload orders  
![](images/959856c1ce8d393a6b61cfe5f4ff6d4803a1d42efdb8e376f70a4dc26475cec7.jpg)  
Source: Bloomberg, inSpectrum, NOM

## Is there relief on the way?

Warsh has acknowledged the demand impulse from AI, but he has also suggested that a disinflationary impulse from productivity is still likely to occur with a lag.

At the June FOMC press conference, he said “it may well be an intuition the supply side is going to expand, but it’ll take longer.” In the Humphrey-Hawkins testimony, Warsh went even further to say that this lagged disinflationary impact was sufficient reason to discount the demand-driven inflation already evident in current data.

## Evaluating potential channels for productivity led disinflation

In our view, productivity growth on its own is insufficient reason to expect meaningful inflation relief. Strong productivity can coincide with disinflation in some scenarios, but the relationship is inconsistent and has weakened in recent decades. In particular, it is important to consider both inflationary and disinflationary pressure from productivity growth, as well as potential attenuating factors like wage growth and margins adjustments.

Beyond the theoretical reasons to be skeptical of “disinflationary productivity,” historical data also point to ambiguity (Fig. 1). There was some negative correlation between labor productivity and inflation from the mid-1960s through the early 1990s. However, the relationship has weakened since then though and has especially broken down post-GFC. Weak productivity growth in the 2010s coincided with a period of low inflation (at the time, theories of ‘secular stagnation’ often cited the era’s low productivity growth as a cause of sluggish inflation). In contrast, inflation has surged post-pandemic alongside an acceleration in trend productivity.

## Can productivity growth cause an output gap?

Productivity growth is often viewed as a positive shock to aggregate supply – which could in theory lead to a negative output gap (actual growth lower than potential) and therefore disinflation.

In practice though, there is almost no correlation between productivity trends and economic slack measures (Fig. 6).

And at least some of the limited relationship between productivity and slack is likely driven by reverse causality. Productivity often rises early in recessions as businesses prioritize their most essential workers (and remaining workers increase their efforts) during periods of slack demand and layoffs. The recent pandemic also saw a technical spike in

productivity as shutdowns tended to impact lower-productivity service sectors. Adjusting for cyclical fluctuations, measures such as trend labor productivity and utilization-adjusted total factor productivity offer no evidence that productivity is associated with disinflationary slack (Fig. 7).

Fig. 6: There is almost no correlation between productivity trends and economic slack measures  
![](images/57a4f730ea02b90f3765fe19fc4ae1117fe233b401149027364a6256f0d33b53.jpg)  
Note: Labor slack refers to the difference between realized u-rate and CBO's estimate of the noncyclical rate of unemployment (formerly called NAIRU)  
Source: CBO, BLS, BEA, Haver, NOM

Fig. 7: Adjusting for cyclical fluctuations, alternative measures offer no evidence that productivity is associated with disinflationary slack  
![](images/5381a9bfc93a931e0fe79d7eec9635f315de5911f5b4979fecffc7cc905c256d.jpg)  
Note: The utilization adjustments follows Basu, Fernald, and Kimball (BFK, 2006)  
Source: SF Fed, BLS, Haver, NOM

It is true that strong growth is less likely to be inflationary if it is driven by productivity gains rather than cyclical tightening. This is close to the argument Chair Greenspan made in the 1990s, when inflation was subdued and the Fed was debating pre-emptive tightening.

It's more difficult to explain why ex ante productivity growth would be a reason to expect disinflation though, specifically when inflation has remained elevated and above the Fed's target for five years.

One possibility is that AI is a uniquely disruptive technology for labor markets, causing productivity growth mostly through a reduction in hours worked, rather than through faster output growth. We see little evidence in recent labor data to support this view though.

## Unit labor costs

Another channel linking productivity to inflation is unit labor costs (ULC). This measures the ratio of total-economy compensation and output, which can also be expressed as the ratio of average wages and labor productivity. ULC has a strong contemporaneous correlation to inflation, so this appears to be a channel for productivity to put downward pressure on inflation. However, despite a strong intuitive connection, we see two shortcomings with this framework.

First, productivity trends do not consistently drive ULC growth. Although productivity is the denominator in the formula for unit labor costs, it does not follow that ULC mechanically slows when productivity accelerates (Fig. 8). (This would be like saying a baseball player's batting average inevitably falls as they get more at bats, or a stock's P/E ratio declines whenever there is faster earnings growth.) The implicit assumption behind this formulaic interpretation is that the numerator, wage growth, is held constant. This is reasonable for short-run forecasts, but over a longer time horizon, productivity growth is one of the strongest drivers of real wages (Fig. 9). Empirically, the relationship between productivity and ULC varies over time and has tended to be weak in recent decades (Fig. 8).

Fig. 8: Productivity does not mechanically reduce ULC, since wage growth also changes over time Correlation between trend productivity and ULC  
![](images/a0e8e74d3ee64970464106e0e856eec943bb3ad409e5676a9bea8321acb202c1.jpg)  
Source: BEA, Haver, NOM

Second, the causal relationship between ULC and inflation tends to be overstated. Profit margins often adjust to limit the pass-through of labor costs to final prices especially, if labor productivity improves due to capital deepening (Fig. 10). A large share of the consumer basket is also relatively insensitive to labor costs – including imported goods and housing services.

In practice, while ULC has a reasonable contemporaneous correlation to inflation, it adds little or no value as a forecast of future inflation.

Fig. 9: Over a longer time horizon, productivity growth is one of the strongest drivers of real wages  
![](images/483d4104a0b254633b4868c2094f7cc9b9cfba319e25ad4f8a29ce32e5f44f2a.jpg)  
Source: BEA, BLS, Haver, NOM

Fig. 10: Profit margins often adjust to limit the pass-through of labor costs to final prices  
![](images/aa94199ffd2304aaf0cc2bb6a0e640213f9e622413e9a30294372d0ae71e4eaf.jpg)  
Source: BLS, Haver, NOM

## Productivity in inflation models

Some macro inflation forecast equations will incorporate trend productivity growth with a negative coefficient.

In most cases though, these models are capturing a partial or conditional impact of productivity growth. For instance, Robert Gordon's "Goldilocks" inflation model includes trend productivity growth in addition to demand indicators and lagged inflation.

In other words, these models do not consider the full impact of productivity on inflation but

instead take demand indicators as a given.

This is a reasonable approach for short-term inflation forecasting and can help to shed some light on real-time policymaking. Faster trend productivity should make officials more willing to tolerate a strong labor market or above-trend GDP growth.

In our opinion, these models are less helpful when analyzing productivity from a forward-looking perspective though. The main channel for productivity growth to be inflationary is by boosting demand (because of faster real income growth or by increasing incentives to invest). A policymaker who expects future productivity strength would want to consider the unconditional impact, not a partial relationship which takes demand growth as a given.

## Productivity surprises and policy mistakes

One possibility is that productivity does not drive inflation in general, but productivity surprises can. This could help explain why productivity and inflation are correlated at times, but inconsistently.

The narrative record of the 1970s inflation episode demonstrated Fed officials' slowness in realizing that trend productivity had shifted (the reasons for the slowdown were still being debated well into the subsequent decades). This, in turn, contributed to overly dovish policy as inflation was attributed to cost shocks rather than an overheated economy.

Considering the current context, it seems unlikely that policymakers would be caught off guard by an AI-driven productivity boom. (The Fed chair described the productivity impact of AI as the most important narrative in his adult life). While mismeasurement and misperception of growth trends are always risks, we do not expect faster productivity growth to lead the Warsh Fed into persistent hawkish policy errors that drive inflation lower.

## Policy implications

Economic theory and history do not make a strong case for disinflationary productivity. Recent price pressure in IT goods suggest the near-term impact of technological progress may be inflationary. And we do not see strong evidence to expect disinflationary relief in the longer run.

Most Fed officials do not appear convinced by Warsh's argument tha

[中间内容因长度限制已省略]

ansmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Securities International, Inc., US. All rights reserved.
"""
