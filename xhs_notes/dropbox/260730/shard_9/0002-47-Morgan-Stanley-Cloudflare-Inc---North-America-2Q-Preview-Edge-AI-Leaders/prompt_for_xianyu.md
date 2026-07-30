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
# 2Q Preview: Edge AI Leadership and Platform Strength Driving Durable Momentum

Channel checks point to another solid qtr for Cloudflare, driven by durable CDN/AppSec and Developer Platform strength. Our recent Edge AI survey further reinforces NET's leadership in distributed AI inference and supports an even more constructive 2H26 outlook.

## Key Takeaways

\- Channel checks again screened positive, with Cloudflare remaining one of the fastest-growing vendors across partner software practices.

■ Growth continues to be led by CDN/AppSec and Developer Services, while Cloudflare continues gaining share in Zero Trust.

\- Expect another Q2 revenue beat and FY26 raise, with an even stronger setup into 2H supported by platform and AI momentum.

\- Our recent Edge AI survey positions Cloudflare as the clear leader in distributed AI inference, reinforcing our long-term thesis.

■ Continued large-deal activity, expanding Pool of Funds consumption, and AI monetization likely support further consensus estimate revisions throughout FY26. Remain OW.

Best Athlete in Software Continues to Execute Across the Platform. Our latest channel checks suggest continued strong momentum for Cloudflare, with partners again coming in above expectations and reinforcing its position as one of the fastest-growing vendors across their software practices. From a demand perspective, growth continues to be driven by durable strength in the core platform, particularly around CDN / Application Security and Edge AI / developer-related offerings, where partners continue to see increasing utilization and consumption (namely Workers) alongside rising traffic volumes. These trends, combined with broader industry tailwinds tied to AI inference and edge computing, continue to position Cloudflare as a key beneficiary of the next phase of enterprise AI deployments. More broadly, partners highlighted healthy demand across API management, data security, and broader developer services, while continuing to note Cloudflare's strong developer ecosystem as a key competitive advantage, particularly as enterprise AI adoption accelerates. While Cloudflare One / SASE remains an increasingly important part of the broader platform story, our conversations suggest it is not the primary driver of growth, though partners continue to see Cloudflare competing in an increasing number of Zero Trust and network modernization opportunities, supporting our view that the company is steadily gaining share in the enterprise security market.

<table><tr><td colspan="2">Sanjit K Singh</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Sanjit.Singh@morganstanley.com</td><td>+1 415 576-2060</td></tr></table>

<table><tr><td colspan="2">Adam Wood</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Adam.Wood@morganstanley.com</td><td>+1 212 761-3656</td></tr><tr><td colspan="2">Jonathan Eisenson</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Jonathan.Eisenson@morganstanley.com</td><td>+1 212 761-2808</td></tr></table>

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$322.00</td></tr><tr><td>Shr price, close (Jul 28, 2026)</td><td>$264.10</td></tr><tr><td>Mkt cap, curr (mm)</td><td>$97,716</td></tr><tr><td>52-Week Range</td><td>$290.82-158.84</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS ($)**</td><td>0.93</td><td>1.20</td><td>1.41</td><td>1.70</td></tr><tr><td>Prior EPS ($)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>P/E</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EPS ($)§</td><td>0.92</td><td>1.21</td><td>1.61</td><td>2.30</td></tr><tr><td>Div yld (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
§ = Consensus data is provided by Refinitiv Estimates
e = MS estimates

<table><tr><td>Quarter</td><td>2025</td><td>2026e Prior</td><td>2026e Current</td><td>2027e Prior</td><td>2027e Current</td></tr><tr><td>Q1</td><td>0.16</td><td>-</td><td>0.25a</td><td>-</td><td>0.27</td></tr><tr><td>Q2</td><td>0.21</td><td>-</td><td>0.27</td><td>-</td><td>0.32</td></tr><tr><td>Q3</td><td>0.27</td><td>-</td><td>0.33</td><td>-</td><td>0.40</td></tr><tr><td>Q4</td><td>0.28</td><td>-</td><td>0.35</td><td>-</td><td>0.41</td></tr></table>

e = MS estimates, a = Actual Company reported data

Similar to recent quarters, we also picked up signs of healthy large enterprise activity, with Cloudflare participating in an increasing number of strategic infra modernization and AI-related deployments. These trends also align with management's commentary around accelerating developer adoption, improving enterprise sales productivity, and record large-deal activity, which we believe continue to support durable platform demand. Bottom line, our latest checks reinforce sustained momentum across the platform, healthy pipeline visibility, and continued large-deal traction, supporting our view that Cloudflare remains one of the best-positioned vendors across software.

From a numbers perspective, expecting upside to Q2 consensus' \~29.8% YoY revenue growth, with a typical \~2-3% beat, driven by multiple product cycles, improving platform momentum, and increasing AI tailwinds, with the FY26 guide likely raised by the magnitude of the Q2 beat. Similarly, expecting current RPO (cRPO) YoY growth to beat consensus' expectations for \~31.8%. While Cloudflare has consistently put up better-than-expected results in the past several quarters, we believe the setup into 2H26 appears even more constructive, supported by continued Pool of Funds consumption, improving enterprise sales execution, accelerating large-deal activity, and increasing monetization across Developer Services, AI infrastructure, and the broader platform. Recall that Q1 revenue growth came in slightly below higher buy-side expectations, reflecting the lag inherent in ramping newer Pool of Funds deals and the broader revenue-recognition drag tied to the ramping usage-based model, both of which should modestly improve in Q2 (and in 2H and beyond). Similarly, RPO growth decelerated in Q1 against a difficult comp, as the prior-year period benefited from the initial signing of the company's largest-ever deal (\~\$130mn TCV). Taken together, we continue to lean positive ahead of Q2 results, expecting Cloudflare to deliver another quarter of 30%+ topline growth, with strong bookings momentum and an expanding mix of the higher-growth Acts likely supporting further upward consensus estimate revisions through the remainder of the year. In terms of the fairly mixed survey results for Cloudflare (see Security Reseller Survey Results), we flag that our live channel conversations (several with partners with >\$50mn in annual Cloudflare sales) were incrementally bullish across the entire Cloudflare platform, while most of the resellers from our below VAR survey results were smaller and largely security-focused. In our view, these security resellers likely have smaller non-security practices and may not accurately reflect the strength of Cloudflare's broader portfolio.

## Our Recent Edge AI Survey Further Reinforces Our OW Thesis on Cloudflare.

While enterprise Edge AI adoption remains in the early innings, our inaugural Edge AI survey (see As Inference Expands Beyond the Hyperscalers, New Leaders Begin to Emerge (16 Jul 2026)) suggests Cloudflare has already established itself as the clear leader in distributed AI inference, with 55% of partners identifying the company as gaining the most share in edge inference over the past three months (Exhibit 9) and 63% selecting Cloudflare as the preferred platform for edge AI compute (Exhibit 8), well ahead of other edge infrastructure vendors. We were also encouraged by continued momentum across the Developer Platform, where Workers AI screened as Cloudflare's fastest-growing developer product, while partners consistently cited AI inference at the edge, edge compute, and agentic AI workloads as the primary drivers of adoption. Importantly, although the majority of partners expect

meaningful enterprise Edge AI deployments to occur in 2027, current demand trends suggest Cloudflare is already benefiting from increasing developer adoption and early inference workloads, positioning the company well ahead of what we believe will be a multi-year deployment cycle. Overall, our Edge AI survey results closely align with our latest channel conversations and further strengthen our conviction that Cloudflare's differentiated edge architecture, developer ecosystem, and multi-product platform position the company as one of the best ways to play the next phase of enterprise AI infrastructure spending across software.

Exhibit 1: While AWS, Azure, and Cloudflare dominate current AI inference share...  
Amongst your customer base, which vendors/platforms has the largest share for executing AI inference currently?  
![](images/b4c2b6223307bf16c36662245846fdf732590ac88073b222630b418bf425330a.jpg)  
Source: MS estimates, n=38

Exhibit 2: ... Cloudflare and other challengers have been gaining share from AWS in inference over the past three months  
Amongst your customer base, which of the following vendors/platforms has seen the largest share gains in the AI inferencing market over the past 3 months?  
![](images/59f9de2c5ea77e6ac9ca64e027ee3fd5d65be3b098e2a213042ffccc1b90fc86.jpg)  
Source: MS estimates, n=38

Exhibit 3: NET: MSe vs. Consensus

<table><tr><td rowspan="2">NET</td><td colspan="2">2Q26e</td><td colspan="2">3Q26e</td><td colspan="2">FY26e</td><td colspan="2">FY27e</td></tr><tr><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td></tr><tr><td>Total Revenue</td><td>$665.0</td><td>$664.8</td><td>$722.2</td><td>$721.6</td><td>$2,809.6</td><td>$2,810.9</td><td>$3,574.4</td><td>$3,590.3</td></tr><tr><td>YoY Growth</td><td>29.8%</td><td>29.8%</td><td>28.5%</td><td>28.4%</td><td>29.6%</td><td>29.7%</td><td>27.2%</td><td>27.7%</td></tr><tr><td>QoQ Growth</td><td>3.9%</td><td>3.9%</td><td>8.6%</td><td>8.5%</td><td></td><td></td><td></td><td></td></tr><tr><td>cRPO</td><td>$1,735.1</td><td>$1,718.9</td><td>$1,803.4</td><td>$1,814.2</td><td>$2,072.9</td><td>$2,046.8</td><td>$2,705.1</td><td>$2,619.4</td></tr><tr><td>YoY Growth</td><td>33.0%</td><td>31.8%</td><td>31.5%</td><td>32.3%</td><td>31.0%</td><td>30.2%</td><td>30.5%</td><td>28.0%</td></tr><tr><td>QoQ Growth</td><td>5.8%</td><td>5.6%</td><td>3.9%</td><td>5.5%</td><td></td><td></td><td></td><td></td></tr><tr><td>Op. Income</td><td>$90.5</td><td>$90.6</td><td>$125.2</td><td>$117.9</td><td>$419.5</td><td>$419.9</td><td>$534.4</td><td>$624.5</td></tr><tr><td>Op. Margin</td><td>13.6%</td><td>13.6%</td><td>17.3%</td><td>16.3%</td><td>14.9%</td><td>14.9%</td><td>15.0%</td><td>17.4%</td></tr><tr><td>EPS</td><td>$0.27</td><td>$0.27</td><td>$0.33</td><td>$0.32</td><td>$1.20</td><td>$1.20</td><td>$1.41</td><td>$1.60</td></tr><tr><td>FCF</td><td>$100.0</td><td>$54.0</td><td>$101.6</td><td>$92.2</td><td>$365.2</td><td>$370.9</td><td>$500.4</td><td>$552.0</td></tr></table>

Source: Company data, MS estimates, Visible Alpha

Exhibit 4: NET: Beat vs. Consensus

<table><tr><td colspan="17">% Beat vs. Consensus</td></tr><tr><td></td><td>NET</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>4 Qtr. Avg.</td></tr><tr><td>Total Revenue Beat</td><td></td><td>0.2%</td><td>-0.2%</td><td>1.0%</td><td>1.6%</td><td>2.7%</td><td>1.4%</td><td>1.7%</td><td>1.5%</td><td>1.8%</td><td>2.1%</td><td>2.3%</td><td>3.2%</td><td>4.1%</td><td>3.0%</td><td>3.1%</td></tr><tr><td>Non-GAAP Op. Margin Beat</td><td></td><td>139.5bps</td><td>254.5bps</td><td>180.4bps</td><td>642.9bps</td><td>275.7bps</td><td>193.8bps</td><td>518.0bps</td><td>271.4bps</td><td>205.5bps</td><td>4.9bps</td><td>145.3bps</td><td>134.8bps</td><td>37.2bps</td><td>1.5bps</td><td>79.0bps</td></tr><tr><td>Non-GAAP EPS Beat</td><td></td><td>$0.02</td><td>$0.05</td><td>$0.03</td><td>$0.06</td><td>$0.03</td><td>$0.03</td><td>$0.06</td><td>$0.02</td><td>$0.01</td><td>-$0.01</td><td>$0.03</td><td>$0.04</td><td>$0.01</td><td>$0.02</td><td>$0.02</td></tr><tr><td>#RPO Beat</td><td></td><td>-3.5%</td><td>-1.0%</td><td>-2.4%</td><td>-3.9%</td><td>1.1%</td><td>0.3%</td><td>-1.7%</td><td>2.4%</td><td>-0.2%</td><td>0.4%</td><td>0.1%</td><td>0.1%</td><td>3.2%</td><td>-1.2%</td><td>0.5%</td></tr><tr><td>Total RPO Beat</td><td></td><td>0.7%</td><td>0.8%</td><td>-0.9%</td><td>-2.9%</td><td>4.9%</td><td>5.3%</td><td>1.6%</td><td>2.1%</td><td>0.6%</td><td>6.0%</td><td>3.3%</td><td>3.3%</td><td>6.1%</td><td>-2.1%</td><td>2.6%</td></tr><tr><td>FCF Beat</td><td></td><td>49%</td><td>NM</td><td>NM</td><td>65%</td><td>8%</td><td>71%</td><td>5%</td><td>17%</td><td>6%</td><td>40%</td><td>-33%</td><td>-33%</td><td>0%</td><td>8%</td><td>-14.4%</td></tr></table>

Source: Company data, MS, Refinitiv, Visible Alpha

Preview to earnings

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Cloudflare Inc NET.N</td></tr><tr><td>Total Revenue</td><td>↑Very likely upside surprise</td><td>↑Modest revision higher</td></tr></table>

\*Likely impact to consensus EPS is for the next 12 months

Source: Company data, MS

## Risk Reward – Cloudflare Inc (NET.N)

A Multi-Product Platform Expansion Story Warrants Premium Multiple

## PRICE TARGET \$322.00

We project FCF through CY2034, apply a 51X EV/FCF multiple and discount back at an 11% weighted average cost of capital, resulting in our base case price target of \$322. 51X is a premium to peers, reflecting Cloudflare's higher growth and improving margin profile.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/65281c344c7912c26a1aba5d0be8b73aec1ffda7d622fc5cc9522cf65857234e.jpg)

## RISK REWARD CHART

![](images/b97c6da79c59fdff6871752c549626f3b84f010fdfd063ee0f1014616babcc4d.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target  
Source: Refinitiv, MS

## BULL CASE

\$428.00

55X 2034e FCF \~\$6.4B (Implies \~44X EV/27e Sales)

Competitive Security Positioning for Enterprise Use Cases and Monetization of Edge AI Drive Durable Long-term Revenue Growth. With a better enterprise revenue mix, rev growth sustains at \~27% CAGR thru 2034. Operating margins scale to \~30% in CY34 to generate \~\$6.4B of FCF on \~\$18.6B rev. We apply a 55X EV/FCF multiple (1.7x EV/FCF/G).

BASE CASE

\$322.00

51X 2034e FCF \~\$5.1B (Implies \~35X EV/27e Sales)

Further Progress Upmarket and Go-to-Market Execution Drive Growth and Margin Expansion. Rev growth slows from \~52% in CY21 to \~20% in 2034. Operating Margins scale from (1%) in 2021 to \~26% in 2034 to generate \~\$5.1B FCF on \~\$15.6B rev. We apply a 51X EV/FCF multiple in CY34 (1.6x EV/FCF/G).

## OVERWEIGHT THESIS

■ Cloudflare's purpose-built cloud solutions address the complex security and website performance needs of a broad customer base. Penetration into attractive \$116B+ TAM by 2028e depends on the strength of security and a swiftly expanding solution portfolio, including AI-related solutions like Workers/R2 for the emerging edge computing opportunity and Access/Cloudflare for Teams for remote access.

We see a long runway of durable 20%+ growth as Cloudflare becomes a key Edge AI enabler for AI inference workloads. This should sustain a premium multiple vs peers, in our view.

![](images/149f8d6de5a57162d92e3dd8ea362f7dc594d07e7240b9238b216bc7f95a8b79.jpg)  
Source: Refinitiv, MS

##

[中间内容因长度限制已省略]

td>Klaviyo, Inc (KVYO.N)</td><td>O (04/29/2026)</td><td>$18.89</td></tr><tr><td>LegalZoom.com Inc (LZ.O)</td><td>U (07/28/2022)</td><td>$8.08</td></tr><tr><td>Liveramp Holdings Inc (RAMP.N)</td><td>E (01/13/2025)</td><td>$37.75</td></tr><tr><td>NICE Ltd. (NICE.O)</td><td>E (07/21/2026)</td><td>$101.41</td></tr><tr><td>RingCentral Inc (RNG.N)</td><td>E (08/08/2023)</td><td>$56.93</td></tr><tr><td>Sprinklr Inc (CXM.N)</td><td>E (07/19/2021)</td><td>$6.31</td></tr><tr><td>Sprout Social Inc (SPT.O)</td><td>E (11/17/2020)</td><td>$8.69</td></tr><tr><td>Twilio Inc (TWLO.N)</td><td>O (02/24/2025)</td><td>$194.33</td></tr><tr><td>Wix.Com Ltd (WIX.O)</td><td>E (07/21/2026)</td><td>$58.55</td></tr><tr><td>Zeta Global Holdings Corp (ZETA.N)</td><td>E (08/01/2024)</td><td>$21.89</td></tr><tr><td>ZoomInfo Technologies Inc (GTM.O)</td><td>E (02/01/2024)</td><td>$3.28</td></tr><tr><td colspan="3">Josh Baer, CFA</td></tr><tr><td>Asana Inc (ASAN.N)</td><td>U (05/20/2025)</td><td>$8.19</td></tr><tr><td>Box Inc (BOX.N)</td><td>E (05/21/2024)</td><td>$31.50</td></tr><tr><td>CCC Intelligent Solutions Holdings Inc (CCC.O)</td><td>O (11/13/2024)</td><td>$6.12</td></tr><tr><td>Commerce.com Inc. (CMRC.O)</td><td>++</td><td>$3.20</td></tr><tr><td>CoreWeave (CRWV.O)</td><td>E (04/22/2025)</td><td>$67.30</td></tr><tr><td>Coursera, Inc. (COUR.N)</td><td>E (04/22/2026)</td><td>$5.85</td></tr><tr><td>DigitalOcean Holdings Inc (DOCN.N)</td><td>O (01/16/2025)</td><td>$112.51</td></tr><tr><td>Docebo Inc. (DCBO.O)</td><td>E (05/12/2025)</td><td>$20.99</td></tr><tr><td>DocuSign Inc (DOCU.O)</td><td>E (01/16/2024)</td><td>$55.97</td></tr><tr><td>Lightspeed Commerce Inc. (LSPD.N)</td><td>E (02/18/2021)</td><td>$10.72</td></tr><tr><td>monday.com Ltd (MNDY.O)</td><td>O (08/12/2025)</td><td>$87.09</td></tr><tr><td>Nebius Group NV (NBIS.O)</td><td>E (01/15/2026)</td><td>$169.69</td></tr><tr><td>Sabre Corp (SABR.O)</td><td>E (03/16/2021)</td><td>$1.88</td></tr><tr><td>ServiceTitan Inc (TTAN.O)</td><td>O (01/20/2026)</td><td>$78.39</td></tr><tr><td>Toast, Inc. (TOST.N)</td><td>O (12/16/2021)</td><td>$32.34</td></tr><tr><td>Via Transportation Inc (VIA.N)</td><td>O (01/20/2026)</td><td>$20.59</td></tr><tr><td>Zoom Communications (ZM.O)</td><td>E (10/11/2022)</td><td>$91.48</td></tr><tr><td colspan="3">Meta A Marshall</td></tr><tr><td>Check Point Software Technologies Ltd. (CHKP.O)</td><td>E (10/16/2023)</td><td>$137.64</td></tr><tr><td>CrowdStrike Holdings Inc (CRWD.O)</td><td>O (03/10/2026)</td><td>$181.80</td></tr><tr><td>Fortinet Inc. (FTNT.O)</td><td>E (07/21/2026)</td><td>$149.98</td></tr><tr><td>Gen Digital Inc. (GEN.O)</td><td>E (06/07/2024)</td><td>$27.58</td></tr><tr><td>Netskope, Inc. (NTSK.O)</td><td>O (10/13/2025)</td><td>$11.98</td></tr><tr><td>Okta, Inc. (OKTA.O)</td><td>O (12/02/2024)</td><td>$136.21</td></tr><tr><td>Palo Alto Networks Inc (PANW.O)</td><td>O (10/10/2017)</td><td>$319.00</td></tr><tr><td>Qualys Inc (QLYS.O)</td><td>U (02/09/2021)</td><td>$135.75</td></tr><tr><td>Rapid7 Inc (RPD.O)</td><td>U (07/21/2026)</td><td>$9.61</td></tr><tr><td>SailPoint Inc (SAIL.O)</td><td>O (09/02/2025)</td><td>$15.78</td></tr><tr><td>SentinelOne, Inc. (S.N)</td><td>E (12/02/2024)</td><td>$18.34</td></tr><tr><td>Tenable Holdings Inc (TENB.O)</td><td>E (12/02/2024)</td><td>$31.37</td></tr><tr><td>Varonis Systems, Inc. (VRNS.O)</td><td>E (01/26/2026)</td><td>$44.67</td></tr><tr><td>Zscaler Inc (ZS.O)</td><td>E (04/22/2026)</td><td>$151.63</td></tr><tr><td colspan="3">Sanjit K Singh</td></tr><tr><td>Akamai Technologies, Inc. (AKAM.O)</td><td>O (01/12/2026)</td><td>$111.79</td></tr><tr><td>Appian Corp (APPN.O)</td><td>E (04/30/2026)</td><td>$27.35</td></tr><tr><td>C3.ai (AI.N)</td><td>U (01/04/2021)</td><td>$8.90</td></tr><tr><td>Cloudflare Inc (NET.N)</td><td>O (12/02/2024)</td><td>$264.10</td></tr><tr><td>Datadog, Inc. (DDOG.O)</td><td>O (01/12/2026)</td><td>$250.88</td></tr><tr><td>Dynatrace Inc (DT.N)</td><td>E (02/13/2024)</td><td>$43.90</td></tr><tr><td>Elastic NV (ESTC.N)</td><td>E (07/21/2026)</td><td>$62.10</td></tr><tr><td>GitLab Inc (GTLB.O)</td><td>E (01/12/2026)</td><td>$32.97</td></tr><tr><td>JFrog Ltd. (FROG.O)</td><td>E (07/21/2026)</td><td>$76.43</td></tr><tr><td>MongoDB Inc (MDB.O)</td><td>O (04/12/2023)</td><td>$310.62</td></tr><tr><td>Oracle Corporation (ORCL.N)</td><td>E (01/15/2019)</td><td>$119.96</td></tr><tr><td>PagerDuty, Inc. (PD.N)</td><td>U (07/21/2026)</td><td>$10.31</td></tr><tr><td>Palantir Technologies Inc. (PLTR.O)</td><td>E (02/04/2025)</td><td>$123.53</td></tr><tr><td>Snowflake Inc. (SNOW.N)</td><td>O (06/24/2025)</td><td>$270.36</td></tr><tr><td>UiPath Inc (PATH.N)</td><td>E (09/07/2022)</td><td>$12.19</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
