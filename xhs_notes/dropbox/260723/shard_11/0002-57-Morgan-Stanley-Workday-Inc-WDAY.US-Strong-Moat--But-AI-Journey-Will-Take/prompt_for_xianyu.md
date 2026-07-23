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
e = MS estimates

# Strong Moat, But AI Journey Will Take Time; Downgrade to Underweight

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Workday Inc (WDAY.O)</td><td>From</td><td>To</td></tr><tr><td>Rating</td><td>Equal-weight</td><td>Underweight</td></tr><tr><td>Price Target</td><td>$185.00</td><td>$145.00</td></tr></table>

While WDAY scored high on our Moat framework and there is a large automation opportunity in the back-office, the Journey to realize AI acceleration will take time. With an uncertain growth & margin path, lack of positive catalysts, and at 23X CY27 GAAP P/E, we see more downside risk here vs peers.

## Key Takeaways

We downgrade Workday to Underweight as AI monetization remains too early to offset slowing core growth.

The retirement of management's prior growth and margin framework creates greater uncertainty around the earnings outlook.

While Workday has a strong moat, we expect AI-driven revenue acceleration to take relatively longer than the rest of our coverage.

■ Back-office AI automation is a meaningful opportunity, but compliance and governance requirements will likely slow adoption.

At 23X CY27 GAAP P/E, we view Workday as expensive relative to peers with similar growth profiles.

With this note, Adam Wood is assuming lead coverage of WDAY at Underweight rating and \$145 PT.

## Downgrade to Underweight on 3 Key Points:

1. AI Monetization Is Too Nascent to Underwrite as a Near-Term Growth Driver. The most pressing concern is the continued growth deceleration in the core business, driven in large part by limited transparency into what is occurring within HCM and FINS, combined with AI monetization that remains in pilot phase. HCM growth has slowed to 13% in FY26, and we model HCM YoY growth continuing to decelerate to 9% in FY28/CY27. While FINS remains more robust at 20% growth, the overall subscription revenue CAGR of 12-13% through FY28 implies Workday's overall market share remains relatively flat (HCM loses share while FINS gains). Management itself acknowledged Q1 FY27 benefited from Q4 deal slippage, and the durability of new ACV acceleration through H2 FY27 remains the key test. Until

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Adam Wood</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Adam.Wood@morganstanley.com</td><td>+1 212 761-3656</td></tr><tr><td colspan="2">Chris Quintero</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Chris.Quintero@morganstanley.com</td><td>+1 212 761-1686</td></tr><tr><td colspan="2">Abhishek S Murli</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Abhishek.S.Murli@morganstanley.com</td><td>+1 212 761-7388</td></tr></table>

Workday Inc (WDAY.O, WDAY US)

Software | United States of America

<table><tr><td>Stock Rating</td><td>Underweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$145.00</td></tr><tr><td>Shr price, close (Jul 17, 2026)</td><td>$144.78</td></tr><tr><td>Mkt cap, curr (mm)</td><td>$39,262</td></tr><tr><td>52-Week Range</td><td>$249.85-110.36</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/26</td><td>12/27e</td><td>12/28e</td><td>12/29e</td></tr><tr><td>EPS ($)**</td><td>9.21</td><td>10.37</td><td>12.20</td><td>14.21</td></tr><tr><td>Prior EPS ($)**</td><td>-</td><td>9.80</td><td>12.24</td><td>15.00</td></tr><tr><td>P/E</td><td>33.6</td><td>31.9</td><td>22.7</td><td>17.2</td></tr><tr><td>EPS ($)§</td><td>10.73</td><td>12.59</td><td>14.58</td><td>15.34</td></tr><tr><td>Div yld (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework

\*\* = Based on consensus methodology

§ = Consensus data is provided by Refinitiv Estimates

## QUARTERLY EPS (\$)

<table><tr><td>Quarter</td><td>2026</td><td>2027e Prior</td><td>2027e Current</td><td>2028e Prior</td><td>2028e Current</td></tr><tr><td>Q1</td><td>2.24</td><td>2.66</td><td>2.66</td><td>2.90</td><td>2.86</td></tr><tr><td>Q2</td><td>2.18</td><td>2.42</td><td>2.54</td><td>2.98</td><td>2.95</td></tr><tr><td>Q3</td><td>2.32</td><td>2.34</td><td>2.56</td><td>3.16</td><td>3.12</td></tr><tr><td>Q4</td><td>2.47</td><td>2.38</td><td>2.61</td><td>3.20</td><td>3.27</td></tr></table>

e = MS estimates

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

adoption moves beyond pilots and targeted deployments, it will be difficult for us and investors to underwrite AI as a near-term growth accelerator.

2. The Prior Analyst Day Framework Is No Longer Relevant, Creating a Lack of Direction in the Near Term. The prior medium-term operating framework, which investors had been underwriting, is now explicitly being retired. Management noted margin expansion will be at a slower pace near term than previously communicated, and said they will update the growth and "sliding scale" margin framework at the next Analyst Day. This injects meaningful uncertainty into the medium-term outlook at precisely the wrong time. The FY27 GAAP operating margin is expected to be approximately 18-19 points lower than the non-GAAP margin of 30.5%, a gap that remains a persistent overhang for investors focused on GAAP profitability. We see downside risk to margin / earnings estimates relative to current consensus given this potential margin framework change. The lack of a clear framework also makes it difficult for investors to anchor expectations.

3. Valuation Remains Expensive Versus Similarly Growing Peers. Using our new segmented valuation framework, Workday's valuation should be evaluated on EV / FCF ex. SBC and GAAP P/E against similarly growing mature-at-scale peers (CRM, INTU, SAP, ADBE, ADSK). Workday is currently trading at 23X CY27 GAAP P/E, a meaningful premium to ADSK at 20X, CRM at 18X, SAP at 16X, INTU at 13X, and ADBE at 11X. It also trades at a premium on a FCF ex. SBC basis (Exhibit 2). As such, we see downside multiple risk at Workday compared to peers.

A Strong Moat, But A Long Journey. Despite a large potential market opportunity, best-in-class retention rate, and a growing product portfolio, we have seen consensus expectations around growth deteriorate over the past few years, leading to investor concerns of continued drags on growth. And now with the advent of AI, there is increased uncertainty around Workday's positioning and growth path going forward. Leveraging our new Moat & Journey framework from our sector Insight, we ultimately view Workday as well positioned given their strong moat, but from a timing perspective think it will take some time before AI starts driving a meaningful growth acceleration, so on a relative basis there are more attractive opportunities elsewhere in our coverage group today.

On the moat, Workday ranked as the company with the 9th strongest moat in our coverage given they are 1) a core system of record, 2) have regulatory / compliance / legal gravity, and 3) have proprietary data / context. The platform processes over 1 trillion transactions annually across more than 11,500 customers, including 65%+ of the Fortune 500, and 80 million users under contract. That proprietary data set is hard to replicate and gives Workday's AI models a context-specific advantage that general-purpose LLMs cannot match. Gross revenue retention has held at 97%, and the platform's embeddedness in mission-critical HR and finance workflows creates switching costs that are among the highest in enterprise software.

The AI journey is what will take time. The timing of when Workday's AI investments translate into durable top-line re-acceleration is the crux of the investor debate and we think there are other opportunities in our coverage that have faster AI journeys than Workday. While we are bullish on the low-hanging fruit available in back-office automation, an area organizations have historically neglected from a digital transformation perspective, the HR and finance end-markets are typically more risk-averse, and we expect a longer runway before buyers are fully comfortable adopting and scaling AI.

The Back-Office Automation Opportunity Is Real, But Timing Is Compliance-Gated. Putting a finer point on this, payroll, compliance, financial close, and workforce planning remain heavily manual at most organizations. We have written multiple reports on the large back-office automation opportunity (see Are We Underestimating Back Office AI? (September 19, 2025)). Workday's role-based agents are purpose-built for exactly these workflows: the Recruiter Agent delivers up to 50% productivity gains for recruiters and accelerates time-to-hire by up to 40%; the Contract Intelligence Agent reduces contract execution time by up to 65%; and the Self-Service Agent has reduced HR case volume by 25% and increased employee productivity by 20% in early access deployments. The challenge is that the markets Workday operates in (HR and finance) are precisely the domains where compliance, auditability, and regulatory accuracy are table stakes. This is a double-edged sword. On one hand, it reinforces Workday's moat: the deterministic business process logic that defines policy compliance and correctness in key processes, from managing people to closing the books, is something only Workday can provide at scale. On the other hand, it means enterprise-wide agent deployments require a level of governance, testing, and regulatory sign-off that extends decision cycles materially. Our channel checks confirm this: customers are piloting agents in sandboxes, with unresolved concerns around probabilistic outputs and legal liability. The back-office automation wave is coming, but the compliance and regulatory gating means it is not a near-term catalyst.

Exhibit 1: Workday Scores Well on Moat, Though Its Position on Journey Timing Is More Elongated

<table><tr><td colspan="3">Software Company AI-Readiness: Moat vs Journey Scores</td></tr><tr><td></td><td>Mean Score</td><td>Mean Moat Score</td></tr><tr><td>MID</td><td>24.0</td><td>23.5</td></tr><tr><td>CMR</td><td>24.0</td><td>23.5</td></tr><tr><td>DOOR</td><td>24.0</td><td>23.5</td></tr><tr><td>COUR</td><td>24.0</td><td>23.5</td></tr><tr><td>DOOR</td><td>24.0</td><td>23.5</td></tr></table>

Source: MS

Lowering PT to \$140. Given the new paradigm we are in within the software sector, we leverage our new segmented valuation framework from our sector Insight to adjust our price target on Workday. Given Workday's position as a mature-at-scale business, we now value Workday based on EV/FCF ex. SBC as opposed to EV/FCF previously and look to other mature-at-scale peers (ADBE, ADSK, CRM, INTU, SAP) as the right valuation comps. We lower our price target to \$145 (from \$185 previously) as we now apply a 17X multiple (vs. 21X previously) to our CY27 FCF estimate. We believe 17X CY27 FCF ex-SBC is warranted given it is more in-line with peers.

Exhibit 2: Workday screens expensive on a EV/FCF-SBC basis...  
![](images/e08c591b22fb580a3db844ef8c19736533439970d278921bbf9fee777c58f7b7.jpg)  
Source: MS

Exhibit 3: ...as well as on a GAAP P/E basis  
![](images/8df44470317e82e8ca0513478b9038534c7e163e93b3342dc0e3e0337708889f.jpg)  
Source: MS

## What Could Make Us More Constructive?

1. Evidence that AI products are accelerating revenue. The most effective rebuttal to the bear case would be a clear re-acceleration in organic subscription growth demonstrating tangible participation in the AI innovation cycle. While this may take some time before occurring, continued disclosures around AI ARR and Agentic ARR likely help build investor confidence in the overall growth path in anticipation of an overall revenue inflection.

2. A clearer disclosure framework. Greater visibility into the specific contribution from new logos, pricing levers, cross-sell, AI ARR as a percentage of total subscription revenue, and enterprise vs. mid-market revenue / associated growth rates would help investors better contextualize the growth profile and assess durability.

3. More attractive entry point. A FCF ex. SBC and/or GAAP P/E multiple in the low-to-mid teens range would represent a much more attractive entry point versus the current premium multiple.

Model Changes

Exhibit 4: Model Changes Tab

<table><tr><td></td><td>FY26</td><td>FY27E</td><td>FY28E</td><td>FY29E</td></tr><tr><td>New Subscription Rev</td><td>8,832.0</td><td>9,937.5</td><td>11,086.9</td><td>12,305.6</td></tr><tr><td>YoY Growth</td><td>14.4%</td><td>12.5%</td><td>11.6%</td><td>11.0%</td></tr><tr><td>Old Subscription Rev</td><td>8,832.0</td><td>9,937.5</td><td>11,244.3</td><td>12,694.8</td></tr><tr><td>YoY Growth</td><td>14.4%</td><td>12.5%</td><td>13.1%</td><td>12.9%</td></tr><tr><td>% Change</td><td>-</td><td>-</td><td>(1.4%)</td><td>(3.1%)</td></tr><tr><td>New Total Revenue</td><td>9,552.0</td><td>10,647.5</td><td>11,772.3</td><td>12,962.3</td></tr><tr><td>YoY Growth</td><td>13.1%</td><td>11.5%</td><td>10.6%</td><td>10.1%</td></tr><tr><td>Old Total Revenue</td><td>9,552.0</td><td>10,647.5</td><td>11,939.3</td><td>13,372.2</td></tr><tr><td>YoY Growth</td><td>13.1%</td><td>11.5%</td><td>12.1%</td><td>12.0%</td></tr><tr><td>% Change</td><td>-</td><td>-</td><td>(1.4%)</td><td>(3.1%)</td></tr><tr><td>New Operating Income</td><td>2,823.0</td><td>3,247.8</td><td>3,750.3</td><td>4,362.8</td></tr><tr><td>New Operating Margin</td><td>29.6%</td><td>30.5%</td><td>31.9%</td><td>33.7%</td></tr><tr><td>Old Operating Income</td><td>2,823.0</td><td>3,247.8</td><td>4,010.9</td><td>4,734.5</td></tr><tr><td>Old Operating Margin</td><td>29.6%</td><td>30.5%</td><td>33.6%</td><td>35.4%</td></tr><tr><td>% Change</td><td>-</td><td>-</td><td>(6.5%)</td><td>(7.9%)</td></tr><tr><td>Margin Change (bps)</td><td>0</td><td>0</td><td>-174</td><td>-175</td></tr><tr><td>New Non-GAAP EPS</td><td>9.21</td><td>10.37</td><td>12.20</td><td>14.21</td></tr><tr><td>Old Non-GAAP EPS</td><td>9.21</td><td>9.80</td><td>12.24</td><td>15.00</td></tr><tr><td>% Change</td><td>0.0%</td><td>5.8%</td><td>-0.3%</td><td>-5.3%</td></tr><tr><td>New OCF</td><td>2,939.0</td><td>3,459.8</td><td>4,056.1</td><td>4,641.8</td></tr><tr><td>New Margin</td><td>30.8%</td><td>32.5%</td><td>34.5%</td><td>35.8%</td></tr><tr><td>Old OCF</td><td>2,939.0</td><td>3,448.2</td><td>4,122.2</td><td>4,885.2</td></tr><tr><td>Old Margin</td><td>30.8%</td><td>32.4%</td><td>34.5%</td><td>36.5%</td></tr><tr><td>% Change</td><td>-</td><td>0.3%</td><td>(1.6%)</td><td>(5.0%)</td></tr><tr><td>Margin Change (bps)</td><td>0</td><td>11</td><td>-7</td><td>-72</td></tr></table>

Source: MS

## Risk Reward – Workday Inc (WDAY.O)

Strong Moat, But AI Journey Will Take Time

## PRICE TARGET \$145.00

17x Base Case CY27e FCF ex-SBC, more in-line with mature-at-scale peers.

Consensus Price Target Distribution Source: Refinitiv, MS

![](images/e9c8a17434f1cb7e8422719c0dd611a95f3a8f524a3563bc1210a60053dc9cca.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/5c052ffba7e7411d7126368a4256a6f12f8f91dcba677841b38efc2eafb9134d.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 17 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## UNDERWEIGHT THESIS

Despite a large potential market opportunity, best-in-class retention rate, and a growing product portfolio, we have seen consensus expectations around growth deteriorate over the past few years, leading 

[中间内容因长度限制已省略]

sforce, Inc. (CRM.N)</td><td>O (12/21/2023)</td><td>$173.79</td></tr><tr><td>Sprinklr Inc (CXM.N)</td><td>E (07/19/2021)</td><td>$5.95</td></tr><tr><td>Sprout Social Inc (SPT.O)</td><td>E (11/17/2020)</td><td>$8.62</td></tr><tr><td>Twilio Inc (TWLO.N)</td><td>O (02/24/2025)</td><td>$205.24</td></tr><tr><td>Wix.Com Ltd (WIX.O)</td><td>O (01/13/2025)</td><td>$51.45</td></tr><tr><td>Zeta Global Holdings Corp (ZETA.N)</td><td>E (08/01/2024)</td><td>$21.34</td></tr><tr><td>ZoomInfo Technologies Inc (GTM.O)</td><td>E (02/01/2024)</td><td>$3.07</td></tr><tr><td colspan="3">Josh Baer, CFA</td></tr><tr><td>Asana Inc (ASAN.N)</td><td>U (05/20/2025)</td><td>$7.60</td></tr><tr><td>Box Inc (BOX.N)</td><td>E (05/21/2024)</td><td>$30.85</td></tr><tr><td>CCC Intelligent Solutions Holdings Inc (CCC.O)</td><td>O (11/13/2024)</td><td>$6.05</td></tr><tr><td>Commerce.com Inc. (CMRC.O)</td><td>++</td><td>$3.04</td></tr><tr><td>CoreWeave (CRWV.O)</td><td>E (04/22/2025)</td><td>$73.21</td></tr><tr><td>Coursera, Inc. (COUR.N)</td><td>E (04/22/2026)</td><td>$5.46</td></tr><tr><td>DigitalOcean Holdings Inc (DOCN.N)</td><td>O (01/16/2025)</td><td>$119.09</td></tr><tr><td>Docebo Inc. (DCBO.O)</td><td>E (05/12/2025)</td><td>$20.38</td></tr><tr><td>DocuSign Inc (DOCU.O)</td><td>E (01/16/2024)</td><td>$52.74</td></tr><tr><td>Lightspeed Commerce Inc. (LSPD.N)</td><td>E (02/18/2021)</td><td>$10.37</td></tr><tr><td>Microsoft (MSFT.O)</td><td>O (01/13/2016)</td><td>$393.82</td></tr><tr><td>monday.com Ltd (MNDY.O)</td><td>O (08/12/2025)</td><td>$78.69</td></tr><tr><td>Nebius Group NV (NBIS.O)</td><td>E (01/15/2026)</td><td>$177.71</td></tr><tr><td>Sabre Corp (SABR.O)</td><td>E (03/16/2021)</td><td>$1.73</td></tr><tr><td>ServiceTitan Inc (TTAN.O)</td><td>O (01/20/2026)</td><td>$76.00</td></tr><tr><td>Shopify Inc (SHOP.O)</td><td>O (04/19/2024)</td><td>$123.56</td></tr><tr><td>Toast, Inc. (TOST.N)</td><td>O (12/16/2021)</td><td>$30.85</td></tr><tr><td>Via Transportation Inc (VIA.N)</td><td>O (01/20/2026)</td><td>$18.59</td></tr><tr><td>Zoom Communications (ZM.O)</td><td>E (10/11/2022)</td><td>$91.13</td></tr><tr><td colspan="3">Meta A Marshall</td></tr><tr><td>Check Point Software Technologies Ltd. (CHKP.O)</td><td>E (10/16/2023)</td><td>$137.10</td></tr><tr><td>CrowdStrike Holdings Inc (CRWD.O)</td><td>O (03/10/2026)</td><td>$203.08</td></tr><tr><td>Fortinet Inc. (FTNT.O)</td><td>U (09/02/2025)</td><td>$161.61</td></tr><tr><td>Gen Digital Inc. (GEN.O)</td><td>E (06/07/2024)</td><td>$26.74</td></tr><tr><td>Netskope, Inc. (NTSK.O)</td><td>O (10/13/2025)</td><td>$13.59</td></tr><tr><td>Okta, Inc. (OKTA.O)</td><td>O (12/02/2024)</td><td>$149.35</td></tr><tr><td>Palo Alto Networks Inc (PANW.O)</td><td>O (10/10/2017)</td><td>$358.68</td></tr><tr><td>Qualys Inc (QLYS.O)</td><td>U (02/09/2021)</td><td>$159.43</td></tr><tr><td>Rapid7 Inc (RPD.O)</td><td>E (08/11/2015)</td><td>$12.20</td></tr><tr><td>SailPoint Inc (SAIL.O)</td><td>O (09/02/2025)</td><td>$15.68</td></tr><tr><td>SentinelOne, Inc. (S.N)</td><td>E (12/02/2024)</td><td>$19.46</td></tr><tr><td>Tenable Holdings Inc (TENB.O)</td><td>E (12/02/2024)</td><td>$39.88</td></tr><tr><td>Varonis Systems, Inc. (VRNS.O)</td><td>E (01/26/2026)</td><td>$47.54</td></tr><tr><td>Zscaler Inc (ZS.O)</td><td>E (04/22/2026)</td><td>$149.94</td></tr><tr><td colspan="3">Sanjit K Singh</td></tr><tr><td>Akamai Technologies, Inc. (AKAM.O)</td><td>O (01/12/2026)</td><td>$120.19</td></tr><tr><td>Appian Corp (APPN.O)</td><td>E (04/30/2026)</td><td>$26.11</td></tr><tr><td>Atlassian Corporation PLC (TEAM.O)</td><td>O (01/13/2020)</td><td>$93.29</td></tr><tr><td>C3.ai (AI.N)</td><td>U (01/04/2021)</td><td>$8.61</td></tr><tr><td>Cloudflare Inc (NET.N)</td><td>O (12/02/2024)</td><td>$272.42</td></tr><tr><td>Datadog, Inc. (DDOG.O)</td><td>O (01/12/2026)</td><td>$258.69</td></tr><tr><td>Dynatrace Inc (DT.N)</td><td>E (02/13/2024)</td><td>$44.71</td></tr><tr><td>Elastic NV (ESTC.N)</td><td>O (12/16/2024)</td><td>$62.74</td></tr><tr><td>GitLab Inc (GTLB.O)</td><td>E (01/12/2026)</td><td>$32.72</td></tr><tr><td>JFrog Ltd. (FROG.O)</td><td>O (12/21/2023)</td><td>$88.54</td></tr><tr><td>MongoDB Inc (MDB.O)</td><td>O (04/12/2023)</td><td>$312.33</td></tr><tr><td>Oracle Corporation (ORCL.N)</td><td>E (01/15/2019)</td><td>$121.38</td></tr><tr><td>PagerDuty, Inc. (PD.N)</td><td>E (01/24/2024)</td><td>$10.34</td></tr><tr><td>Palantir Technologies Inc. (PLTR.O)</td><td>E (02/04/2025)</td><td>$132.38</td></tr><tr><td>ServiceNow Inc (NOW.N)</td><td>O (09/24/2025)</td><td>$104.70</td></tr><tr><td>Snowflake Inc. (SNOW.N)</td><td>O (06/24/2025)</td><td>$274.34</td></tr><tr><td>UiPath Inc (PATH.N)</td><td>E (09/07/2022)</td><td>$12.16</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
