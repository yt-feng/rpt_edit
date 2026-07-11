You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
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

<table><tr><td rowspan="2"></td><td colspan="5">Chinese Heritage Gold brands</td><td colspan="2">MNC Hard Luxury</td></tr><tr><td>Laopu Gold</td><td>Jemper</td><td>BWF Gold</td><td>Borland</td><td>LamChiu</td><td>Cartier</td><td>Tiffany</td></tr><tr><td>Founded year</td><td>2009</td><td>2004</td><td>2012</td><td>1988</td><td>2006</td><td>1847</td><td>1837</td></tr><tr><td>Founder background</td><td>Xu Gaoming (Former Arts &amp; Crafts administrator)</td><td>Experts with deep roots in jadeite and high-jewelry inlay</td><td>n.a.</td><td>Descended from a dynastic lineage of Beijing gold smiths</td><td>Ma Chaoxian (Second-generation craftsman from Lanzhou. His family involved in gold smithing since 1977)</td><td>Louis-François Cartier (A jewelry apprentice)</td><td>Charles Lewis Tiffany (Started as a stationery shop owner)</td></tr><tr><td>(Potential/Core) drivers of the luxury positioning</td><td>Pioneer of heritage gold, distinct craftsmanship and service</td><td>Oriental new chic, distinct craftsmanship</td><td>Imperial craftsmanship</td><td>Imperial craftsmanship</td><td>Pure handmade and seal cutting</td><td>It served almost every royal house in Europe</td><td>Iconic &#x27;Tiffany Blue&#x27;, pioneering six-prong diamond setting, and cinematic influence</td></tr><tr><td>Positioned market</td><td></td><td></td><td colspan="3">Heritage gold jewelry</td><td>Jewelry &amp; Watches</td><td>Jewelry</td></tr><tr><td>Consumer profile</td><td></td><td colspan="4">HNWIs with appreciation for Intangible Cultural Heritage (ICH)</td><td>Global HNWIs</td><td>Global HNWIs</td></tr><tr><td>Haute Couture</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>Accessible via private salon appointments, delivering historical provenance</td><td>Specializes in custom designs and rare colored gemstones for VVIPs</td></tr><tr><td>Auctions (# of lots sold in Christie&#x27;s)</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>c.20k</td><td>c.9k</td></tr><tr><td rowspan="2">Iconic products and price</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pure gold, Diamond, Ruby (~15g)Rmb 43,896</td><td>Pure gold, Diamond, Ruby (~15g)Rmb 41,830</td><td>Pure gold, Diamond, Ruby (~15g)Rmb 43,000</td><td>Pure gold (~15g)Rmb 32,229</td><td>Pure gold (~15g)Rmb 36,900</td><td>18k gold, Dimaond Rmb 42,500</td><td>18k gold, Diamond Rmb 17,400</td></tr><tr><td>Exclusivity Resale discount of regular SKUs (as of Jun-26)</td><td>Sufficient inventory ~32% discount</td><td>Sufficient inventory ~32% discount</td><td>Sufficient inventory n.a.</td><td>Sufficient inventory ~44% discount</td><td>Lead time &gt;6M ~40% discount</td><td>Sufficient inventory ~43% discount</td><td>Sufficient inventory ~63% discount</td></tr><tr><td>GMV by channels</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GMV (Rmb mn)</td><td>31,440</td><td>900</td><td>n.a.</td><td>300</td><td>500</td><td>11,584</td><td>8,085</td></tr><tr><td># of boutiques (2025)</td><td>45</td><td>8</td><td>7</td><td>3</td><td>1</td><td>52</td><td>34</td></tr><tr><td>Avg sales per boutique (Rmb mn)</td><td>559</td><td>150</td><td>n.a.</td><td>100</td><td>500</td><td>204</td><td>237</td></tr><tr><td>Online GMV (Rmb mn)</td><td>5,363</td><td>156</td><td>n.a.</td><td>n.a.</td><td>208</td><td>962</td><td>10</td></tr><tr><td>Online GMV mix</td><td>17%</td><td>17%</td><td>n.a.</td><td>n.a.</td><td>42%</td><td>8%</td><td>0.1%</td></tr><tr><td>Globalization historical pa

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
