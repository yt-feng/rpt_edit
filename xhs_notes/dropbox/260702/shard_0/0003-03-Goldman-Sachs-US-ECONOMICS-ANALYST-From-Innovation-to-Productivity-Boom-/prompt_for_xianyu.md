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
US ECONOMICS ANALYST

# From Innovation to Productivity Boom: Lessons from the ICT Revolution for the AI Era

We expect AI to meaningfully boost productivity growth over the next decade. Already, dozens of research studies and corporate anecdotes show evidence of large productivity gains at the micro level in a range of applications. But key questions for both equity and macro investors are when and where we might first see evidence of AI-driven productivity gains at the macro level.

Elsie Peng  
+1(212)357-3137 | elsie.peng@gs.com  
GS & Co. LLC

We look back at the information and communications technology revolution (ICT) from roughly 1980-2000 to draw insights from history. A key lesson of that period is that the path from technological innovation to broad-based productivity gains is neither fast nor uniform.

When did the impact of ICT on productivity first appear? The ICT productivity boom arrived 15 years after the commercialization of the personal computer. While ICT investment began rising sharply in the early 1980s, industry-level data show that its impact on productivity followed a J-curve: a modest drag on measured productivity growth in the first four years, with clear gains emerging only after eight years and peaking at year twelve. The impact was slow because key ICT component costs were initially high, network effects did not kick in until adoption reached a critical mass, and human and institutional impediments slowed technology adoption and were only gradually overcome with substantial investment in intangible organizational capital.

\- Where did convincing evidence that ICT was boosting productivity first appear? Early productivity gains appeared in industries where ICT was already deeply embedded in the production process even before the innovation breakthrough of the early 1980s, in industries that invested in ICT earliest, and especially in industries that invested heavily in reorganization to use ICT more effectively. While productivity growth in these industries picked up earlier and more strongly than in the aggregate statistics, providing persuasive early evidence that ICT was having a meaningful impact, some of the key measures used today to identify these early winners, such as intangible investment, might not have been obvious to observers at the time.

To what degree will these historical lessons from ICT apply to AI? With regard to timing, we expect to see a quicker impact of AI on productivity because costs are falling much faster for AI models than they did for ICT equipment, and network effects are less vital for realizing productivity gains. But similar human and institutional obstacles to adoption are again likely to delay the impact on

productivity. While investment in hardware is already rising even faster than during the ICT buildout, investment in reorganization of work processes appears to be moving more slowly.

With regard to where to look for the earliest tests of whether AI is boosting productivity growth, the industries to watch are clearer today thanks to the availability of higher frequency data on AI exposure and adoption in addition to data on investment in tangible and intangible capital. Our composite ranking across these measures implies that industries such as information, professional services, insurance, and finance should show the earliest and largest pickups in productivity growth. While productivity trends for these industries should provide the earliest test, industry-level data come out with a lag, so even here the evidence will likely take at least several years to arrive.

## From Innovation to Productivity Boom: Lessons from the ICT Revolution for the AI Era

We expect AI to meaningfully boost productivity growth over the next decade. Already, dozens of research studies and corporate anecdotes show evidence of large productivity gains at the micro level in a range of applications. But key questions for both equity and macro investors are when and where we might first see evidence of AI-driven productivity gains at the macro level.

We look back at the information and communications technology revolution (ICT) from roughly 1980-2000 to draw some insight from history. A key lesson of that period is that the path from technological innovation to broad-based productivity gains is neither fast nor uniform.

## When Did the Impact of ICT on Productivity First Appear in the Macro Data?

The commercialization of the personal computer in the early 1980s set off a wave of technological innovation. Exhibit 1 shows that there was a sharp and sustained rise in breakthrough ICT patents per capita through the late 1980s and early 1990s. But productivity growth remained stubbornly flat for nearly 15 years, accelerating only in the second half of the 1990s.

Exhibit 1: The Commercialization of the Personal Computer in the Early 1980s Set Off a Wave of Innovation, but Productivity Growth Did Not See a Meaningful Increase Until the Late 1990s  
![](images/14a1ec9acb71a672a24d67d1133c4ad26f5dee10f54d92cf7e7d684e80954548.jpg)  
\*Creative patents are defined as patents that contain original terminologies (e.g. "cloud computing" first emerged in 2007 patents). Patent data are from Kalyani (2024) and Kelly, Papanikolaou, Seru, and Taddy (2021).  
Source: GS Global Investment Research, Department of Labor

The impact on productivity growth took a while to appear even though ICT investment began to rise sharply as early as the 1980s (Exhibit 1, left). The increase in ICT investment was fairly broad-based, though industries like professional services, wholesale trade, transportation, and finance invested much more intensively (Exhibit 2, right).

Exhibit 2: ICT Investment Began Rising Sharply in the Early 1980s, With Increases Seen Across Most Industries  
![](images/ead7e274c8db41dc2322337807fa8b5089605bdb3f246ac469b3eb1953bf9c8a.jpg)

![](images/1f1684f3f165611f63dc1dc41e90190bfe294364a7c8efa2e0e2aa8b8a11afce.jpg)  
Note: ICT investment includes investment in personal computers, mainframes, storage devices, printers, terminals, tape drives, system integrators, and communication devices. Data are from BEA's fixed asset survey.  
Source: GS Global Investment Research, Department of Commerce

But it took a long time for an increase in ICT investment to have a notable impact on productivity. Using industry panel data, we find that an increase in ICT investment actually led to a modest decline in measured productivity growth in the first four years. The positive effects emerged only with a substantial lag: a 1pp increase in ICT investment as a percentage of the capital stock did not produce a statistically significant rise in productivity growth until roughly 8 years later, with the impact peaking at around 0.6pp in year twelve. $^{1}$

Exhibit 3: ICT Investment Initially Weighed on Productivity Growth, With Positive Effects Emerging Roughly 8 Years Later  
![](images/8ac3629863071082a34b4446d8b39a18f26892b901b3d28ea14f666a96427ee1.jpg)  
Note: Error bars indicate $95\%$ confidence interval.  
Source: GS Global Investment Research

We see three factors that delayed productivity gains.

First, key ICT components—such as semiconductors and telecommunication devices—remained expensive throughout the 1980s. Prices only began falling after regulatory interventions and increased competition opened previously concentrated markets in the 1990s.

Exhibit 4: Key ICT Components Remained Expensive Through the 1980s; Prices Only Started to Fall Following Increased Competition and Regulatory Changes in the 1990s

![](images/422ea6aff642543bfa09851e238de0cd7c37664ff0aeed3dbeea20e8a992e1e3.jpg)  
Source: GS Global Investment Research, Department of Labor

Second, many ICT applications such as the internet exhibited strong network effects, generating far greater value for their users after adoption reached a critical mass. Productivity gains tended to emerge only after adoption rates passed an inflection point in the late 1990s.

Exhibit 5: ICT Applications Exhibited Strong Network Effects, and Productivity Gains Only Emerged After Adoption Rates for Technologies Like the Internet Passed an Inflection Point in the Late 1990s  
![](images/97c235db80609481512bfe9cf71d3b8d22b1eb5c5b4165741e670019cf5c7f38.jpg)  
Source: GS Global Investment Research

Third, an even more important bottleneck was the time and resources required for firms to build intangible assets needed to support the technological transition, such as redesigning workflows, retraining workers, and restructuring organizations, and building new data systems, as discussed in detail in our Global Economics team's prior report. The left panel of Exhibit 6 shows that each \$1 of ICT hardware investment likely required at least an additional \$1.7 of complementary intangible investment, with roughly two-thirds directed toward software and data systems and the remainder toward workforce reorganization. $^{2}$ The right panel of Exhibit 6 shows that there was a clear increase in intangible capital investment in the mid-1990s, and even this likely understates the increase because much of the early spending for reorganization was not captured in the official GDP statistics.

Exhibit 6: ICT Required Meaningful Investment in Intangible Capital to Reach Its Full Productivity Potential, and Companies Only Started to Invest Heavily in Intangible Capital in the Late 1990s  
![](images/3f2be14c275bac4367435da1e929904141ffb842f07de1c976d7041ef97fc3f6.jpg)  
Source: GS Global Investment Research, EUKLEMS, Haver Analytics

## Where Did the Impact of ICT on Productivity First Become Visible?

To identify where the ICT productivity boom first became visible at the industry level, we use a standard statistical test for structural breaks in productivity growth across major industries. Exhibit 7 shows the year in which each industry first exhibited a statistically significant acceleration in productivity growth. We find that education, management, wholesale trade, professional services, and administrative support were among the earliest to show a clear pickup, in some cases several years ahead of the acceleration in the aggregate data.

How confident can we be that these structural breaks were driven by ICT rather than other factors? As a check, we estimate the impact of ICT investment on productivity growth separately for each major industry group and combine these estimates with actual ICT investment data at the detailed industry level to estimate impulses from ICT investment to productivity growth for each industry. We then run the same structural break test on these industry-level ICT impulses to productivity growth and find that the resulting break years are broadly consistent with those identified using productivity data alone, supporting the conclusion that these early productivity pickups were most likely ICT-driven.

Exhibit 7: Some Industries Showed a Clear Pickup in Productivity Growth Several Years Ahead of the Acceleration in the Aggregate Data

![](images/b7dbef2778c81064b14eb62b371ea81eaa83349413439861bf0bc9d607a31bec.jpg)  
\*Structural break years are estimated using the supremum Wald test. The test identifies the year in which allowing productivity growth to follow a different statistical relationship before and after that year yields the greatest improvement in model fit.  
Source: GS Global Investment Research, Department of Labor

What characteristics distinguished the earliest and largest beneficiaries of ICT?

We find that industries where ICT was already deeply embedded in the production process before the technological breakthroughs of the early 1980s—or those that were among the earliest to invest heavily in the new technologies when they first became available—tended to see an earlier productivity payoff, with productivity growth in these industries peaking as early as the mid-1990s (Exhibit 8).

Exhibit 8: Industries Where ICT Was Already Deeply Embedded in the Production Process Before the Technological Breakthrough of the Early 1980s or Those That Adopted the New Technologies Earliest Tended to See an Earlier Productivity Payoff

![](images/5a9143138722220bc6f90a0e19f9fb9bc7716916ce98ad43e439c43881ca885b.jpg)  
Source: GS Global Investment Research, Department of Labor

But the ultimate winners were those that invested heavily in intangible organizational capital alongside their ICT investment—restructuring workflows, retraining workers, and redesigning business processes. As Exhibit 9 shows, these industries went from underperforming the rest of the economy in productivity growth to pulling sharply ahead by the early 1990s—and sustained that lead for years afterward. This finding reinforces a central lesson of the ICT experience: the industries that gained the most were not simply those that adopted the technology first or invested the most in hardware, but those that also made the largest complementary investments in reorganizing their operations around it.

Exhibit 9: The Ultimate Industry Winners Were Those That Invested Heavily in Reorganization Capital Alongside Their ICT Investment  
![](images/7fc9d27010487eeeb5fbcdac2801aa649b7072bfcef07e4ec5116a3278b14d32.jpg)  
Source: GS Global Investment Research, Department of Labor

## The Lessons of the ICT Revolution for the AI Era

To what degree will these historical lessons from ICT apply to AI? With regard to timing, we expect to see a quicker impact of AI on productivity because costs are falling faster for AI models than they did for ICT equipment. That said, headline pricing for some frontier US AI models has risen in recent months as leading providers seek to expand margins. Our equity analysts expect overall token prices to stabilize as competitive pressure and continued declines in underlying compute costs limit providers' ability to sustain elevated pricing. In addition, unlike with communication-oriented technologies, network effects are probably less vital for realizing productivity gains from AI.

Exhibit 10: The Price of Using AI Models Is Falling Much More Quickly Than Personal Computer Prices Did  
![](images/e2ab93653766318c64c0e742f6b85ac401f14c46b36a02b5a69c051f7bb06d37.jpg)  
\*Price per million tokens averaged across different LLM models, indexed to March 2023.  
\*\*Quality-adjusted LLM model price index from Demirer, Fradkin, Tadelis, and Peng (2025)

## Source: GS Global Investment Research, Department of Commerce

But similar human and institutional obstacles to adoption are again likely to delay the impact on productivity. The left side of Exhibit 11 shows that investment in hardware is already rising even faster than during the ICT buildout. Investment in reorganizing work processes—as measured by the share of compensation paid to employees engaging in reorganization—appears to be moving more slowly (Exhibit 11, right), though some intangible investment already underway might not be fully captured by official measures. For example, a recent Atlanta Fed survey of enterprises implies roughly \$280 billion in AI-related intangible capital spending in 2026, and our prior analysis based on company data suggest that labor costs associated with the AI transition are likely running at \$150bn/year in the US, and executive time allocations suggest \$40bn/year in organization capital investment is likely underway.

Exhibit 11: Investment in Hardware Supporting AI Is Already Growing Very Quickly, but the Investment in Intangible Capital That Will Likely Be Required to Fully Exploit AI Appears Not to Have Followed Yet

![](images/f52280b93907825c7e63934103f29f2e4c3e580474fbb132799bf1e2c3ab312b.jpg)

![](images/bc9e68bd730addc0842fa5ba45d4761a7a4ebefe7d1e71af1632243b5d4155c7.jpg)  
\* EUKLEMS intangible investment data only starts from 1987, so we also track intangible investment usi

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
