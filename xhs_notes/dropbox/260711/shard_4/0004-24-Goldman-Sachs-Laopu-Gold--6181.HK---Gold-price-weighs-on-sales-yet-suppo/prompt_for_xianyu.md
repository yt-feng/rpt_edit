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
# Laopu Gold (6181.HK): Gold price weighs on sales yet supports margin; cut earnings/TP on growth deceleration but remain Buy rated

Since Laopu's price hike on Feb 28th, the gold price has corrected by $>20\%$ to $\sim$ US\$4,100/oz, which has weighed on Laopu's sales performance as a fixed price-based player. Based on our tracker, Laopu's Tmall flagship store sales declined by $63\%$ yoy in 2Q26 compared to $155\%$ yoy growth in 1Q26 with pressure during 618 from a high base/with offline dilution; while we expect the overall offline sales performance to be better than online and continuous customer acquisition should still provide support, the relatively price sensitive demand (including reseller demand) also contributed to the high base last year and we expect it to be relatively weak, with Laopu's per gram price at high DD% to $>100\%$ premium to weight based product currently. We also note weight-based products have been outperforming amid the gold price pull back, where both Chow Tai Fook and Luk Fook saw solid SSSG in 2Q driven by strong growth of fixed priced products.

On the positive side, we note Laopu's brand popularity remains healthy and ahead of other heritage gold-focused brands, evidenced by an increase in followers/discussions on social media platforms. The company has been testing LSD%-MSD% lower price via new products/allowing stacks of membership discount during promotion, which saw positive initial impact on demand (for example, Shanghai's Xintiandi store allows stack discounts, and saw 1-2 hour queues during the weekend, according to social media platforms). That said, customer perception on brand positioning also needs to be watched if the company further rolls out these pricing actions.

We revise down 2026 earnings by 9% to Rmb8bn with slower growth outlook for 2H amid a weaker gold price backdrop, while 1H26 net income forecast remains at Rmb4.7bn (or Rmb4.8bn adjusted NP) with lowered sales offset by higher GPM on favorable inventory procurement price. For 2027-28E, we lower our earnings forecast by 19%-22% driven by topline. That said, with the stock currently trading at 7x 2026 P/E, we believe the demand pressure has been reflected in market expectation. If the gold price stabilizes or picks up (currently at \~US\$4,100/oz, and GS forecast price to reach US\$4,900 at year end), we would expect the worst backdrop for sales to be behind us, with gradual consumption sentiment recovery post price hikes, digestion of reseller inventory, and new product launches (including lowered prices) stimulating customer demand. Laopu's dividend yield is also high at \~10%. Remain Buy rated with a TP of HK\$650 (from HK\$1,108 prior, based on lowered 2026 P/E of 13X).

Xinyu Ruan  
+852-2978-7347 | xinyu.ruan@gs.com  
GS (Asia) L.L.C.

Michelle Cheng  
+852-2978-6631 |  
michelle.cheng@gs.com  
GS (Asia) L.L.C.

Molly Dai  
+852-3966-4000 | molly.dai@gs.com  
GS (Asia) L.L.C.

## Pricing: expanded premium to weight based products; but testing lower price

Laopu conducted 20%-30% price hike on Feb 28th when the gold price was at a relatively high level of >US\$5000/oz. That said, since the price hike, the gold price has corrected by >20%. While we believe Laopu's advantage in products and customer experience backs its price premium and continues to attract less price sensitive customers (Laopu has c.80% customer overlap with global luxury brands as of Mar 2026), relatively price sensitive demand (including purchase from resellers) also backs Laopu's strong sales performance in 2025/2026 CNY, especially when Laopu's price hike magnitude was below the gold price increase. Currently, at a gold price of \~US\$4100/oz and assuming Laopu procures inventory at this level, it implies Laopu is able to reach \~50% GPM after discount, vs. company's target GPM of 40%. This also implies \~teens% per gram price premium to Chow Tai Fook's fixed priced products, or high DD% (for pure gold) to >100% (for gem set) premium to per gram price of weight based product currently. The gold price correction has brought pressure to Laopu's near term sales — in the online channel, our tracker suggests 63% yoy decline in 2Q26 (vs. +155% growth in 1Q26); in the offline channel, we expect the overall performance to be better than online and new store addition (store count was up low teens% in 1H26 yoy) is a support, while there has also been divergence across channels where the channels with higher reseller exposure underperformed.

While Laopu's existing product price and discount magnitude (10% discount during promotion period) remains stable, we note the brand has been testing market feedback on lower prices via: 1) select newly launched products, with a per gram price at \~Rmb2,100-2,200/2,700-2,800 for pure gold/gem set products (or below 2,000/2,400-2,500 after 10% discount), which is c.3% cheaper than existing products based on our tracker; 2) in select promotions, 5% membership discount is able to be added on top of 10% promotion discounts, implying mid-teens% discount level (vs. 10% previously, or maximum low teens% discount if adding shopping mall points) — e.g. in recently upgraded Shanghai Xintiandi stores, there were 1-2 hour weekend line-up during the promotion according to social media platforms.

Exhibit 1: Laopu historical price hike  
![](images/cc584d4f9f18adb99714c9efece0e8d83a06e664823d055e714f2dbc866574cc.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 2: GS expects COMEX gold price to reach \$4,900 by Dec-26, implying \~18% upside from now  
![](images/4defc50965dd994e6bcb36c2725a1414756ba40ca6f204e6923b42fc2e297230.jpg)  
Source: Refinitiv Eikon, GS Global Investment Research

Exhibit 3: Post the Feb price hike, Laopu is able to reach 40% GPM when gold price at \~USD5000; gold price decline translates to further GPM upside

<table><tr><td rowspan="2"></td><td colspan="5">Scenario (post Feb price hike, with 10% discount)</td></tr><tr><td>Target GPM</td><td>I</td><td>II</td><td>III</td><td>IV</td></tr><tr><td>Gold price (USD/oz)</td><td>5,000</td><td>4,900</td><td>4,600</td><td>4,300</td><td>4,000</td></tr><tr><td>COGS per 100 revenue</td><td>60</td><td>59</td><td>55</td><td>52</td><td>48</td></tr><tr><td>GPM</td><td>40%</td><td>41%</td><td>45%</td><td>48%</td><td>52%</td></tr></table>

GPM comparison based on Gold price scenarios

![](images/83084d96608eb457f005d1ee1c1df9d75afede913d4e869e5081a508b8870dde.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: Laopu's per gram price premium to weight based products has notably expanded since price hike; but the company has been testing lower prices for newly launched products  
Rmb per gram of fixed-price products (Tag price)

<table><tr><td colspan="11">Kmb per gram of fixed-price products (Tag price)</td></tr><tr><td>Brands</td><td colspan="4">Laopu</td><td colspan="3">Jemper</td><td colspan="3">Borland</td></tr><tr><td>Product types</td><td>Pure gold</td><td>Gem-set</td><td>New pure gold</td><td>New gem set</td><td>Pure gold</td><td>Gem-set</td><td>New product</td><td>Pure gold</td><td>Gem-set</td><td>New product</td></tr><tr><td>Product images</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td><img src="images/3327b8871e36b2f210a400c7ed8bc96d27120ce99c4023a1fb7c604404f5deed.jpg"/></td><td><img src="images/c67d8e9f81150f0cb27ce686e8132ea996d11b30cdedc7b5d7948606749687f6.jpg"/></td></tr><tr><td>Jan-26</td><td>1,723</td><td>2,180</td><td></td><td></td><td>N.A.</td><td>2,175</td><td></td><td>1,943</td><td>2,669</td><td></td></tr><tr><td>vs SGE gold price</td><td>52%</td><td>92%</td><td></td><td></td><td></td><td>91%</td><td></td><td>71%</td><td>135%</td><td></td></tr><tr><td>vs CTF weighted gold price</td><td>14%</td><td>44%</td><td></td><td></td><td></td><td>43%</td><td></td><td>28%</td><td>76%</td><td></td></tr><tr><td>Feb-26</td><td>2,223</td><td>2,824</td><td></td><td></td><td>N.A.</td><td>2,175</td><td></td><td>2,268</td><td>2,988</td><td></td></tr><tr><td>YTD price increase (%)</td><td>29%</td><td>30%</td><td></td><td></td><td></td><td>0%</td><td></td><td>17%</td><td>12%</td><td></td></tr><tr><td>vs SGE gold price</td><td>92%</td><td>144%</td><td></td><td></td><td></td><td>88%</td><td></td><td>96%</td><td>158%</td><td></td></tr><tr><td>vs CTF weighted gold price</td><td>40%</td><td>78%</td><td></td><td></td><td></td><td>37%</td><td></td><td>43%</td><td>88%</td><td></td></tr><tr><td>Mar-26</td><td>2,223</td><td>2,824</td><td></td><td></td><td>N.A.</td><td>3,123</td><td></td><td>2,268</td><td>2,988</td><td></td></tr><tr><td>YTD price increase (%)</td><td>29%</td><td>30%</td><td></td><td></td><td></td><td>44%</td><td></td><td>17%</td><td>12%</td><td></td></tr><tr><td>vs SGE gold price</td><td>112%</td><td>170%</td><td></td><td></td><td></td><td>198%</td><td></td><td>116%</td><td>185%</td><td></td></tr><tr><td>vs CTF weighted gold price</td><td>59%</td><td>102%</td><td></td><td></td><td></td><td>123%</td><td></td><td>62%</td><td>113%</td><td></td></tr><tr><td>Apr-26</td><td>2,223</td><td>2,824</td><td></td><td></td><td>N.A.</td><td>3,123</td><td></td><td>2,268</td><td>2,988</td><td></td></tr><tr><td>YTD price increase (%)</td><td>29%</td><td>30%</td><td></td><td></td><td></td><td>44%</td><td></td><td>17%</td><td>12%</td><td></td></tr><tr><td>vs SGE gold price</td><td>119%</td><td>179%</td><td></td><td></td><td></td><td>208%</td><td></td><td>124%</td><td>195%</td><td></td></tr><tr><td>vs CTF weighted gold price</td><td>61%</td><td>104%</td><td></td><td></td><td></td><td>125%</td><td></td><td>64%</td><td>116%</td><td></td></tr><tr><td>May-26</td><td>2,223</td><td>2,824</td><td></td><td></td><td>N.A.</td><td>3,123</td><td></td><td>2,268</td><td>2,988</td><td></td></tr><tr><td>YTD price increase (%)</td><td>29%</td><td>30%</td><td></td><td></td><td></td><td>44%</td><td></td><td>17%</td><td>12%</td><td></td></tr><tr><td>vs SGE gold price</td><td>126%</td><td>187%</td><td></td><td></td><td></td><td>217%</td><td></td><td>130%</td><td>203%</td><td></td></tr><tr><td>vs CTF weighted gold price</td><td>63%</td><td>107%</td><td></td><td></td><td></td><td>129%</td><td></td><td>66%</td><td>119%</td><td></td></tr><tr><td>Jun-26</td><td>2,223</td><td>2,824</td><td>2,146</td><td>2,725</td><td>N.A.</td><td>3,123</td><td>3,034</td><td>2,268</td><td>2,988</td><td>2,160</td></tr><tr><td>YTD price increase (%)</td><td>29%</td><td>30%</td><td></td><td></td><td></td><td>44%</td><td></td><td>17%</td><td>12%</td><td></td></tr><tr><td>vs SGE gold price</td><td>153%</td><td>221%</td><td>144%</td><td>210%</td><td></td><td>255%</td><td>245%</td><td>158%</td><td>240%</td><td>146%</td></tr><tr><td>vs CTF weighted gold price</td><td>81%</td><td>131%</td><td>75%</td><td>122%</td><td></td><td>155%</td><td>148%</td><td>85%</td><td>144%</td><td>76%</td></tr></table>

In Rmb. Based on tagged price.  
Source: Taobao, Company data, GS Global Investment Research

Exhibit 5: Laopu's resale discount corrected with gold price correction Transaction prices on platforms  
Laopu Gold value retention: resell price/original price  
![](images/dc49e4193927ef3ca410da6ec87b1f305ea9fcd0cf8fe71fc8dcc0f67a5c3744.jpg)  
Source: Xianyu, Red, Company data, GS Global Investment Research

Exhibit 6: Laopu's online sales were under pressure in 2Q

<table><tr><td rowspan="2">Tmall Flagship store</td><td colspan="10"></td></tr><tr><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td></tr><tr><td colspan="11">Local brands</td></tr><tr><td>Laopu Gold</td><td>185%</td><td>137%</td><td>176%</td><td>248%</td><td>545%</td><td>288%</td><td>784%</td><td>232%</td><td>155%</td><td>-63%</td></tr><tr><td>Chow Tai Fook</td><td>10%</td><td>6%</td><td>10%</td><td>187%</td><td>127%</td><td>38%</td><td>60%</td><td>-23%</td><td>-18%</td><td>8%</td></tr><tr><td>Luk Fook</td><td>16%</td><td>-23%</td><td>-16%</td><td>21%</td><td>54%</td><td>67%</td><td>127%</td><td>15%</td><td>12%</td><td>8%</td></tr><tr><td>Chow Tai Seng</td><td>90%</td><td>18%</td><td>28%</td><td>-13%</td><td>3%</td><td>-6%</td><td>17%</td><td>31%</td><td>-30%</td><td>-30%</td></tr><tr><td>Chow Sang Sang</td><td>12%</td><td>14%</td><td>26%</td><td>48%</td><td>139%</td><td>58%</td><td>-32%</td><td>-9%</td><td>-35%</td><td>-9%</td></tr><tr><td colspan="11">International brands</td></tr><tr><td>Swarovski</td><td>-8%</td><td>n.a.</td><td>-18%</td><td>-16%</td><td>17%</td><td>n.a.</td><td>27%</td><td>-8%</td><td>-19%</td><td>0%</td></tr><tr><td>APM</td><td>-26%</td><td>n.a.</td><td>20%</td><td>108%</td><td>97%</td><td>n.a.</td><td>13%</td><td>50%</td><td>23%</td><td>3%</td></tr><tr><td>Pandora</td><td>-38%</td><td>n.a.</td><td>-48%</td><td>20%</td><td>16%</td><td>n.a.</td><td>18%</td><td>-31%</td><td>-4%</td><td>4%</td></tr></table>

<table><tr><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td>-64%</td><td>-50%</td><td>-71%</td></tr><tr><td>10%</td><td>-32%</td><td>61%</td></tr><tr><td>-34%</td><td>0%</td><td>73%</td></tr><tr><td>-53%</td><td>-32%</td><td>-4%</td></tr><tr><td>-16%</td><td>-32%</td><td>45%</td></tr><tr><td>50%</td><td>10%</td><td>-23%</td></tr><tr><td>9%</td><td>0%</td><td>3%</td></tr><tr><td>53%</td><td>-20%</td><td>8%</td></tr></table>

Source: Moojing, GS Global Investment Research

## Competitive landscape: new players emerging yet scale remains much smaller; weight based products outperform amid gold price pull back

Multiple heritage gold brands emerged and have been expanding in the top tier shopping mall systems. While we view shopping mall access as not necessarily a barrier, with shopping malls eager to capture the heritage gold trend (evidenced by multiple heritage gold brands in MixC, Nanjing Deji, Shanghai IFC etc.), we believe Laopu enjoys moats include: 1) better location in the shopping malls, thanks to the brand's proved sales performance in the system; 2) stronger brand recognition and customer awareness, with Laopu as a pioneer in the heritage gold industry. Laopu's follower numbers on social media platform are notably higher than other heritage gold brands, and continue to increase at a decent pace; 3) larger scale, which enables Laopu to have more sufficient resources in inventory preparation, investment in stores and marketing. In fact, Laopu's sales scale is more than 30x that of the second largest heritage gold focused player Jemper, in 2025, based on our estimation, with leading store productivity.

However, amid the gold price pull back, weight-based products have been gaining attraction over fixed priced products. In 2Q, Chow Tai Fook/Luk Fook outperformed in SSSG, driven by weight-based products. Meanwhile, pricing for fixed priced products is also relatively favorable compared to leading heritage gold-focused brands which conducted price hikes in 1Q — Chow Tai Fook withdrew a price hike which was planned in Mar; Luk Fook also adjusted prices/discounts based on the gold price trend.

Exhibit 7: Comparison table between Chinese Heritage Gold brands and MNC hard luxury brands

<table><tr><td rowspan="2"></td><td colspan="5">Chinese Heritage Gold brands</td><td colspan="2">MNC Hard Luxury</td></tr><tr><td>Laopu Gold</td><td>Jemper</td><td>BWF Gold</td><td>Borland</td><td>LamChiu</td><td>Cartier</td><td>Tiffany</td></tr><tr><td>Founded year</td><td>2009</td><td>2004</td><td>2012</td><td>1988</td><td>2006</td><td>1847</td><td>1837</td></tr><tr><td>Founder background</td><td>Xu Gaoming (Former Arts &amp; Crafts administrator)</td><td>Experts with deep roots in jadeite and high-jewelry inlay</td><td>n.a.</td><td>Descended from a dynastic lineage of Beijing gold smiths</td><td>Ma Chaoxian (Second-generation craftsman from Lanzhou. His family involved in gold smithing since 1977)</td><td>Louis-François Cartier (A jewe

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
