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
<table><tr><td colspan="2">Brian Nowak, CFA</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Brian.Nowak@morganstanley.com</td><td>+1 212 761-3365</td></tr><tr><td>Julian Herrera</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Julian.Herrera@morganstanley.com</td><td>+1 212 761-1784</td></tr><tr><td>Gregory Gao</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Greg.Gao@morganstanley.com</td><td>+1 212 296-3125</td></tr><tr><td>Nikhil Javeri</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Nikhil.Javeri1@morganstanley.com</td><td>+1 212 761-3742</td></tr><tr><td>Kavya A Narayanan</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Kavya.Narayanan@morganstanley.com</td><td>+1 212 761-4183</td></tr></table>

# \$1.4trln of Capex, 4X in Compute Capacity, and AI Revenue Streams to Watch into '28

Updated bottom up cost per GW and rising forward capacity expectations cause us to raise hyperscaler capex to \$1.4t in '28 painting a path to 120 GW (from 30 in '25). META top pick with 5 under-appreciated call options, and AMZN and GOOGL hyperscale revs set to accelerate with strong profitability

The Ecosystem Remains Compute-Constrained And Urgency to Spend Remains High...We have written extensively about the rising value, strategic importance and monetization optionality associated with access to compute (see here and here). In effect, limitations on chips/racks, powered shells (see our thematic teams' work here, led by Stephen Byrd) and other bottlenecks are stretching timelines from breaking ground to opening data centers to as much as 3 years. Furthermore, we also believe growing social backlash to data center development and political uncertainty into the '28 presidential election are causing hyperscalers to start building sooner to emphasize job creation. This adds even further to inflationary pressures. As such, we expect capex spend to continue to head higher (now expected to reach to \$1.2tr/\$1.4tr across the five primary companies we track) and are laser focused on companies' ability to bring on capacity to drive and benefit from incremental AI-enabled revenue (from bare metal compute to fuller stack first/third party software and services).

...As We Now See Hyperscaler Capex Reaching \~\$1.2tr/\$1.4tr in '27/'28... As detailed here, we continue to utilize a bottom-up model around required capex for compute capacity coming online. We have estimates for IT hardware costs (server racks with chips, memory, CPU, networking, etc.) and costs outside of the racks (building materials, electrical and mechanical systems) to arrive at the estimated cost to build each GW of capacity...by chip type (across 10 different chips). Please see Exhibit 10 for our latest estimates on cost per GW...which are going up by \~20% (for GPUs) due to further inflationary pressure on memory and powered shell-related costs. We then apply these building costs to the estimated GPU/ASIC supply allocations by hyperscaler to arrive at forward capex.

We raised our GOOGL forward capex substantially in Alphabet Inc.: Diving into '28 Compute Capacity, TPU Sales and Revenue to Come (29 Jun 2026). Today we are raising our META and AMZN (AWS) capex, as we raise our META '27/'28 capex by 29%/22%, reaching \$225bn/\$250bn...and our AMZN company-wide capex by 15%/29%, reaching \$308bn/\$318bn.

## INTERNET

North America
Industry View
Attractive

Please let us know if interested in our updated bottom-up cost per GW, GW capacity, or new Meta API monetization models to flex, adjust and utilize.

Exhibit 1: We are raising '27/'28 total hyperscaler capex (ex-SPCX, included for first time) by 9%/10%, now modeling \~\$1.2tr/\$1.4tr of '27/'28 capex:

![](images/ab97bd33611b78970273173488ccf8f237bead45bbf10026c3ce081e0c11bd72.jpg)  
Source: Company data, MS Estimates, Note: AMZN represents total company capex, SPCX represents terrestrial compute capex. Note: MSFT capex estimates are calendar year.

...Which We See Leading to a 4x Lift in Available Compute Capacity by '28: But we see this spend leading to more compute capacity...with total hyperscaler available compute expected to approach 120GW by '28, up from \~30 in '25. While GOOGL is expected to add the most compute capacity (9 GW/11 GW in '27/'28) we see AWS having the most available compute in '28 (at 35 GW vs GOOGL at 31 GW). We see META reaching 14/21 total GW of capacity by '27/'28, up from \~3.5 GW at YE25. Note that this compares to a recent press article that spoke to the company having \~14 GW by YE27. For META, we see 55%/90% of additions in '26/'27 being first party, with 45%/10% coming from third party relationships.

Exhibit 2: Our bottom-up work shows how total hyperscaler compute capacity is set to reach \~120 GW by '28...up from \~30 GW in '25:

![](images/77a53f5c8a08e06f36448d23ff560f4a89b774d96307d1d819eaba7e94f719d8.jpg)  
Source: Company data, MS Estimates, Note: SPCX represents terrestrial compute capacity. Note: GOOGL capacity represents additions for both internal GOOGL and Google Cloud, and we expect $\sim 1/2$ of capacity additions to go towards each. Note: MSFT capacity estimates represent fiscal year estimates. Note: META capacity estimates include both internally owned and externally leased capacity.

Exhibit 3: ...with GOOGL expected to add the most capacity, followed by AMZN and META.

![](images/8a82981f056a8b6b9393c4ef93586198e90f49415fff6de25dde65354a3af108.jpg)  
Source: Company data, MS Estimates, Note: SPCX represents terrestrial compute capacity. Note: GOOGL capacity represents additions for both internal GOOGL and Google Cloud, and we expect \~1/2 of capacity additions to go towards each. Note: MSFT capacity estimates represent fiscal year estimates. Note: META capacity estimates include both internally owned and externally leased capacity.

Which Revenue Streams and Factors Matter Most To META, AMZN and GOOGL to Justify the Spend and Drive Outperformance? AMZN, GOOGL, META are currently trading at 16X-20X '28 EPS. Given the still rising spend, we expect investors to remain hyper focused on signal of materially incremental, durable, and profitable revenue growth. So how do we think about each of these in 2H and into '27?

Exhibit 4: AMZN, GOOGL, META are currently trading at 16X-20X '28 EPS:

<table><tr><td>Peer Set</td><td>Current Price</td><td>Price Target</td><td>% Upside</td><td>&#x27;28 EPS</td><td>&#x27;28 P/E (Current)</td><td>&#x27;28 P/E (PT)</td><td>&#x27;26-&#x27;28 EPS CAGR</td><td>&#x27;28 PEG (Current)</td><td>&#x27;28 PEG (PT)</td></tr><tr><td>AMZN</td><td>$246</td><td>$330</td><td>34%</td><td>$15</td><td>16x</td><td>22x</td><td>25%</td><td>0.6x</td><td>0.9x</td></tr><tr><td>GOOGL</td><td>$357</td><td>$415</td><td>16%</td><td>$19</td><td>19x</td><td>22x</td><td>14%</td><td>1.4x</td><td>1.6x</td></tr><tr><td>META</td><td>$666</td><td>$775</td><td>16%</td><td>$33</td><td>20x</td><td>23x</td><td>1%</td><td>14.3x</td><td>16.6x</td></tr></table>

Source: Company Data, MS Estimates

META: 5 Under-appreciated Call Options and EPS Drivers...Remains Top Pick. \$775 PT has 15% Upside, But There Could Be More. As shown below, and detailed in Meta Platforms Inc: 4 Products to Turn Meta Back into an "AI Winner" (2 Jun 2026) we now see 5 META call options for higher earnings power beyond our base case \~\$33 of '28 EPS that are not priced. We recognize the risk of these and that the company needs to deliver these products to drive higher earnings power and multiple expansion...but META still has the most call optionality, where the market is penalizing them for the spend and not giving them credit for potential revenue from the spend.

In aggregate these could represent as much as \~\$10 of EPS (or \~30% upside to our estimates)...meaning META could be trading at \~15X '28 EPS right now if all these went right. You don't need them all, but you just need META to successfully ship and scale these products for the market to feel more confident in the ROIC on this spend.

Exhibit 5: Wee see multiple under-appreciated \$1-3 EPS call options at META...giving us many paths to \$38-\$40 of '28 EPS.  
![](images/4619bdbe7d24267d170178767741f463b628adc882111324ea7652ca01b3aa2f.jpg)  
Source: Company data, MS Estimates

Sizing the API Revenue Opportunity from Supply and Demand Side While we have previously sized the neocloud, search, and subscription opportunities, the launch and pricing of Muse Spark 1.1 to third parties is notable as it is priced anywhere from 30%-85% below private company offerings.

Exhibit 6: Muse Spark 1.1 is priced meaningfully below its peers on the frontier.

<table><tr><td>Model</td><td>Input $/1M Tokens</td><td>Output $/1M Tokens</td><td>Input Pricing vs Muse Spark</td><td>Output Pricing vs Muse Spark</td></tr><tr><td>Muse Spark 1.1</td><td>$1.25</td><td>$4.25</td><td>Baseline</td><td>Baseline</td></tr><tr><td>Frontier Model A</td><td>$2.00</td><td>$6.00</td><td>(38%)</td><td>(29%)</td></tr><tr><td>Frontier Model B</td><td>$5.00</td><td>$30.00</td><td>(75%)</td><td>(86%)</td></tr><tr><td>Frontier Model C</td><td>$5.00</td><td>$25.00</td><td>(75%)</td><td>(83%)</td></tr><tr><td>Frontier Model D</td><td>$2.00</td><td>$10.00</td><td>(38%)</td><td>(58%)</td></tr><tr><td>Frontier Model E</td><td>$2.00</td><td>$12.00</td><td>(38%)</td><td>(65%)</td></tr></table>

Source: Company data, MS Estimates

As a result, we aim to size META's API revenue opportunity in the context of the advertisers/companies most likely to use it. But it all starts with capacity allocation, and in our methodology we bridge to API revenue from GPUs required for a given amount of capacity, and what we know from public benchmarks on tokens/GPUs as well as Muse Spark 1.1's API pricing. Using this, we estimate that every 100 MW of compute allocated toward Meta's API could generate as much as \$8bn of revenue and \~\$2 of '28 EPS. With Meta expected to add \~10 GW of compute across '26/'27, clearly they will have capacity if demand is there.

But the demand from companies and advertisers will be key to driving adoption (with tools like business agents, coding assistants, ad campaign management, and a model harness expected to be developed). If the tools drive ROI, we would expect adoption...so tools Meta develops will be important. Other LLMs currently charge \$200-\$300 per month for their premium tiers of products. In our base case, we assume that 25%, or \~4mn of Meta's 15mn advertisers pay it \~\$200/month for its products, which again yields \$8bn of revenue and \~\$2 of '28 EPS.

To be clear, this new business does come with higher execution risk, but we are hopeful/confident that Meta's existing advertiser/business relationships (and aggressive pricing) should give it a head start in building out a business here. To facilitate the API business, we estimate META would only need to allocate \~100MW of GB300 capacity, as shown below, and could easily serve additional API demand with its \~21GW capacity base by YE28, yielding further upside to revenue and EPS.

## Please let us know if interested in our META API revenue model.

Exhibit 7: From a capacity perspective, we estimate that every 100 MW of GB300 capacity deployed toward the API for Muse Spark 1.1 could create as much as \~6% upside to our '28 EPS...

<table><tr><td colspan="2">META API Revenue Based on GB300 Capacity Deployed to API</td></tr><tr><td>Capacity Deployed Towards API (MW)</td><td>100</td></tr><tr><td>(/) KW Per Rack</td><td>135</td></tr><tr><td>(=) Racks Deployed Towards API</td><td>741</td></tr><tr><td>(X) GPUs Per Rack</td><td>72</td></tr><tr><td>(=) GPUs Deployed Towards API</td><td>53,333</td></tr><tr><td>(X) Tokens/Second/GPU</td><td>4,300</td></tr><tr><td>(X) Seconds per Year</td><td>31,536,000</td></tr><tr><td>(X) GPU Utilization</td><td>75%</td></tr><tr><td>(=) Tokens per Year (tn)</td><td>5,424</td></tr><tr><td>(X) Blended Token Pricing</td><td>$1.58</td></tr><tr><td>(=) API Revenue ($mn)</td><td>$8,588</td></tr><tr><td>% Upside to &#x27;28 Revenue</td><td>2%</td></tr><tr><td>API Revenue</td><td>$8,588</td></tr><tr><td>(X) Gross Margin</td><td>75%</td></tr><tr><td>(=) Gross Profit</td><td>$6,441</td></tr><tr><td>(X) GP Flow Through</td><td>100%</td></tr><tr><td>(=) Incremental EBIT</td><td>$6,441</td></tr><tr><td>(X) Marginal Tax Rate</td><td>21%</td></tr><tr><td>(=) Net Income</td><td>$5,089</td></tr><tr><td>(/) Shares Outstanding</td><td>2,669</td></tr><tr><td>(=) EPS Upside</td><td>$1.91</td></tr><tr><td>% Upside to &#x27;28 EPS</td><td>6%</td></tr></table>

Source: Company data, MS Estimates

Exhibit 8: In our base case, we assume that 25%, or \~4mn of Meta's 15mn advertisers pay \~\$200/month for its products, which yields \~\$8bn of revenue and \~\$2 of EPS.

<table><tr><td>Advertisers (mn)</td><td>15</td><td>15</td><td>15</td><td>15</td><td>15</td></tr><tr><td>(X) Advertiser Penetration of API</td><td>15%</td><td>25%</td><td>35%</td><td>45%</td><td>55%</td></tr><tr><td>(=) Advertisers Using API (mn)</td><td>2.3</td><td>3.8</td><td>5.3</td><td>6.8</td><td>8.3</td></tr><tr><td>API Revenue ($mn)</td><td>$8,588</td><td>$8,588</td><td>$8,588</td><td>$8,588</td><td>$8,588</td></tr><tr><td>(/) Advertisers Using API (mn)</td><td>2.3</td><td>3.8</td><td>5.3</td><td>6.8</td><td>8.3</td></tr><tr><td>(=) Annual Spend Per Customer</td><td>$3,817</td><td>$2,290</td><td>$1,636</td><td>$1,272</td><td>$1,041</td></tr><tr><td>(/) Months in Year</td><td>12</td><td>12</td><td>12</td><td>12</td><td>12</td></tr><tr><td>(=) Monthly Spend per Customer</td><td>$318</td><td>$191</td><td>$136</td><td>$106</td><td>$87</td></tr></table>

Source: Company data, MS

## AMZN: Strong AWS Revenue, Profitability and Backlog Ahead. \$330 PT has \~35% Upside.

First, AMZN compute capacity is scaling nicely and likely set to drive better than expected (and priced) AWS revenue growth. Indeed, even our 35%/40% '26/'27 AWS revenue growth is arguably conservative given it only implies \$7/\$9 of incremental revenue/incremental watt. For more on this please see Internet: GOOGL's \$50/Watt Deal and What It Signals for GOOGL, AMZN, META and GenAI ROIC (17 Jun 2026).

We also expect AWS backlog to rise substantially, up \$110bn Q/Q in 2Q, reaching \~\$475bn due to private lab deals. This should give the market more confidence in multi-year growth durability. We also think AWS's access to almost all of the leading models, small/medium and customized models position it as a winner in a world where optimizing token cost per task is the key. Bedrock is a winner here. Lastly, remember that if META does indeed scale its agentic offerings, it is likely to run partially on Graviton (see here), further supporting AWS's strong AI positioning.

## Please let us know if interested in our updated AWS model and backlog files.

Second, AMZN's Retail business remains (our view) an under-appreciated GenAI winner with improving algorithmic matching, a stronger ad business, and a call option for even stronger long-term unit economics with robotics (see here).

Exhibit 9: We see upward bias to forward hyperscaler revenue estimates as implied incremental revenue per incremental watt looks conservative...most notably at AWS:  
![](images/abf110dc32e040fe2b4623b77f5156fe3c2b5c4c24174f3c3f0d4ce637bd2090.jpg)  
Source: Company data, MS Estimates

GOOGL: Leading Full Stack AI Winner with Accelerating Cloud Business and Improving '28 Visibility...But Tactical Risk on Capacity. \$415 PT has \~20% Upside: We detailed our views about GOOGL's on-prem cloud and third party TPU opportunity in Alphabet Inc.: Diving into '28 Compute Capacity, TPU Sales and Revenue to Come (29 Jun 2026). This, in our view is the key thesis driver as we model 77%/78% Google Cloud growth in 2Q:26/'26. But we also expect continu

[中间内容因长度限制已省略]

) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Internet

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/10/2026)</td></tr><tr><td colspan="3">Brian Nowak, CFA</td></tr><tr><td>Airbnb Inc (ABNB.O)</td><td>U (12/06/2022)</td><td>$148.62</td></tr><tr><td>Alphabet Inc. (GOOGL.O)</td><td>O (08/11/2015)</td><td>$357.18</td></tr><tr><td>Amazon.com Inc (AMZN.O)</td><td>O (04/24/2015)</td><td>$245.34</td></tr><tr><td>Booking Holdings Inc (BKNG.O)</td><td>O (02/23/2026)</td><td>$178.39</td></tr><tr><td>DoorDash Inc (DASH.O)</td><td>O (02/21/2024)</td><td>$191.82</td></tr><tr><td>Expedia Inc. (EXPE.O)</td><td>E (01/09/2019)</td><td>$270.83</td></tr><tr><td>Instacart (CART.O)</td><td>E (01/29/2024)</td><td>$48.39</td></tr><tr><td>Lyft Inc (LYFT.O)</td><td>E (10/24/2019)</td><td>$15.61</td></tr><tr><td>Meta Platforms Inc (META.O)</td><td>O (03/20/2023)</td><td>$669.21</td></tr><tr><td>Pinterest Inc (PINS.N)</td><td>O (07/20/2025)</td><td>$22.52</td></tr><tr><td>Reddit Inc (RDDT.N)</td><td>O (12/08/2024)</td><td>$195.34</td></tr><tr><td>Snap Inc. (SNAP.N)</td><td>E (07/22/2024)</td><td>$4.68</td></tr><tr><td>Uber Technologies Inc (UBER.N)</td><td>O (06/04/2019)</td><td>$74.54</td></tr><tr><td colspan="3">Matthew Cost</td></tr><tr><td>AppLovin Corp (APP.O)</td><td>O (04/10/2025)</td><td>$506.98</td></tr><tr><td>Compass, Inc. (COMP.N)</td><td>E (01/12/2026)</td><td>$11.72</td></tr><tr><td>Criteo SA (CRTO.O)</td><td>E (01/26/2016)</td><td>$22.88</td></tr><tr><td>DoubleVerify Holdings Inc (DV.N)</td><td>E (06/25/2024)</td><td>$11.67</td></tr><tr><td>Electronic Arts Inc (EA.O)</td><td>E (08/04/2021)</td><td>$206.41</td></tr><tr><td>Liftoff Mobile Inc. (LFTO.O)</td><td>E (06/29/2026)</td><td>$24.83</td></tr><tr><td>MNTN Inc (MNTN.N)</td><td>E (06/16/2025)</td><td>$10.50</td></tr><tr><td>Opendoor Technologies Inc (OPEN.O)</td><td>E (07/24/2023)</td><td>$4.77</td></tr><tr><td>Playtika Holding Corp (PLTK.O)</td><td>E (11/27/2022)</td><td>$3.83</td></tr><tr><td>Roblox Corporation (RBLX.N)</td><td>O (11/04/2024)</td><td>$55.35</td></tr><tr><td>Shutterstock Inc (SSTK.N)</td><td>E (07/28/2022)</td><td>$8.49</td></tr><tr><td>Take-Two Interactive Software (TTWO.O)</td><td>O (02/01/2018)</td><td>$243.20</td></tr><tr><td>Trade Desk Inc (TTD.O)</td><td>E (09/10/2025)</td><td>$19.53</td></tr><tr><td>Unity Software Inc (U.N)</td><td>O (09/02/2024)</td><td>$30.89</td></tr><tr><td>Webtoon Entertainment Inc (WBTN.O)</td><td>E (07/22/2024)</td><td>$11.54</td></tr><tr><td>Yelp Inc (YELP.N)</td><td>U (01/10/2019)</td><td>$25.81</td></tr><tr><td>Zillow Group Inc (Z.O)</td><td>E (04/18/2018)</td><td>$32.19</td></tr><tr><td colspan="3">Nathan Feather</td></tr><tr><td>Bumble Inc. (BMBL.O)</td><td>E (03/08/2021)</td><td>$3.03</td></tr><tr><td>Chewy Inc (CHWY.N)</td><td>O (10/31/2023)</td><td>$20.88</td></tr><tr><td>Duolingo Inc (DUOL.O)</td><td>E (02/27/2026)</td><td>$124.76</td></tr><tr><td>eBay Inc (EBAY.O)</td><td>O (04/18/2024)</td><td>$117.20</td></tr><tr><td>Etsy Inc (ETSY.N)</td><td>E (07/20/2025)</td><td>$81.05</td></tr><tr><td>FIGS, Inc. (FIGS.N)</td><td>E (02/29/2024)</td><td>$10.04</td></tr><tr><td>Grindr Inc. (GRND.N)</td><td>O (07/01/2026)</td><td>$15.69</td></tr><tr><td>Match Group Inc (MTCH.O)</td><td>E (04/18/2024)</td><td>$38.85</td></tr><tr><td>Peloton Interactive, Inc. (PTON.O)</td><td>E (03/14/2022)</td><td>$5.86</td></tr><tr><td>Revolve Group Inc (RVLV.N)</td><td>E (10/20/2024)</td><td>$23.93</td></tr><tr><td>WW International Inc (WW.O)</td><td>E (08/01/2025)</td><td>$15.40</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
