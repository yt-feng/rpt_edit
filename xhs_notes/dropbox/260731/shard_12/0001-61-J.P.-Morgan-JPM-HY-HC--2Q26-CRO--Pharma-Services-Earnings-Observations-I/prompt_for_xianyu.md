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
# JPM HY HC: 2Q26 CRO, Pharma Services Earnings Observations

IQV, FTRE, and AVTR Earnings Review

IQV, FTRE, and AVTR reported their 2Q26 earnings this week. All three spoke to positive funding environments and/or improving macro backdrops. Further, they all raised their revenue guidance for FY26, reflecting confidence in 2H26 trends and healthy demand resulting in organic growth. We note that ICLR echoed this constructive view on end-market demand for the remainder of 2026 and a healthy pharma funding environment. Though mainly highlighted in the IQV call, we will continue to watch for any AI disruption in the space and monitor funding in pharma, biotech, and EBP.

Table 1: Pricing

<table><tr><td rowspan="2">CREDIT</td><td rowspan="2">RATE</td><td rowspan="2">RANKING</td><td rowspan="2">MATURITY</td><td colspan="3">RATINGS</td><td colspan="3">PRICING</td></tr><tr><td>M</td><td>/</td><td>S&amp;P</td><td>Px</td><td>YTW</td><td>SPREAD</td></tr><tr><td>FTRE</td><td>7.500%</td><td>Secured</td><td>7/1/2030</td><td>B3</td><td>/</td><td>B-</td><td>101.8</td><td>6.509%</td><td>225</td></tr><tr><td>PRXL</td><td>TSFR1M+275bp, Indx FI: 50</td><td>Term Loan</td><td>12/12/2031</td><td>B2</td><td>/</td><td>B+</td><td>100.3</td><td>6.442%</td><td>269</td></tr><tr><td>SYNH</td><td>TSFR1M+350bp, Indx FI: 0</td><td>Term Loan</td><td>9/30/2030</td><td>B1</td><td>/</td><td>B</td><td>100.0</td><td>7.248%</td><td>350</td></tr><tr><td>SYNH</td><td>9.000%</td><td>Secured</td><td>10/1/2030</td><td>B1</td><td>/</td><td>B</td><td>104.5</td><td>6.725%</td><td>244</td></tr><tr><td>IQV</td><td>TSFR3M+175bp, Indx FI: 0</td><td>Term Loan</td><td>1/2/2031</td><td>Baa3</td><td>/</td><td>BBB-</td><td>100.5</td><td>5.459%</td><td>162</td></tr><tr><td>IQV</td><td>5.700%</td><td>Secured</td><td>5/15/2028</td><td>Baa3</td><td>/</td><td>BBB-</td><td>101.3</td><td>4.924%</td><td>71</td></tr><tr><td>IQV</td><td>6.250%</td><td>Secured</td><td>2/1/2029</td><td>Baa3</td><td>/</td><td>BBB-</td><td>102.8</td><td>5.029%</td><td>73</td></tr><tr><td>IQV</td><td>5.000%</td><td>Unsecured</td><td>10/15/2026</td><td>Ba2</td><td>/</td><td>BB</td><td>100.0</td><td>4.927%</td><td>127</td></tr><tr><td>IQV</td><td>5.000%</td><td>Unsecured</td><td>5/15/2027</td><td>Ba2</td><td>/</td><td>BB</td><td>99.9</td><td>5.154%</td><td>115</td></tr><tr><td>IQV</td><td>2.250%</td><td>Unsecured</td><td>1/15/2028</td><td>Ba2</td><td>/</td><td>BB</td><td>98.1</td><td>3.620%</td><td>81</td></tr><tr><td>IQV</td><td>2.875%</td><td>Unsecured</td><td>6/15/2028</td><td>Ba2</td><td>/</td><td>BB</td><td>98.9</td><td>3.532%</td><td>72</td></tr><tr><td>IQV</td><td>2.250%</td><td>Unsecured</td><td>3/15/2029</td><td>Ba2</td><td>/</td><td>BB</td><td>96.6</td><td>3.645%</td><td>82</td></tr><tr><td>IQV</td><td>6.500%</td><td>Unsecured</td><td>5/15/2030</td><td>Ba2</td><td>/</td><td>BB</td><td>101.6</td><td>5.527%</td><td>130</td></tr><tr><td>IQV</td><td>6.250%</td><td>Unsecured</td><td>6/1/2032</td><td>Ba2</td><td>/</td><td>BB</td><td>101.3</td><td>5.878%</td><td>150</td></tr><tr><td>IQV</td><td>4.625%</td><td>Unsecured</td><td>6/15/2033</td><td>Ba2</td><td>/</td><td>BB</td><td>100.4</td><td>4.588%</td><td>169</td></tr><tr><td>AVTR</td><td>EUR003M+200bp, Indx FI: 0</td><td>Term Loan</td><td>10/12/2032</td><td>Ba1</td><td>/</td><td>BBB-</td><td>100.5</td><td>4.364%</td><td>191</td></tr><tr><td>AVTR</td><td>3.875%</td><td>Unsecured</td><td>7/15/2028</td><td>B1</td><td>/</td><td>BB</td><td>100.0</td><td>3.868%</td><td>131</td></tr><tr><td>AVTR</td><td>4.625%</td><td>Unsecured</td><td>7/15/2028</td><td>B1</td><td>/</td><td>BB</td><td>98.9</td><td>5.236%</td><td>97</td></tr><tr><td>AVTR</td><td>3.875%</td><td>Unsecured</td><td>11/1/2029</td><td>B1</td><td>/</td><td>BB</td><td>95.1</td><td>5.532%</td><td>119</td></tr></table>

Source: Bloomberg Finance, L.P.

## IQVIA (IQV)

Recommendation: We maintain our Neutral rating on IQV. Results were generally in line and management sentiment around the current and future market environment and AI was overwhelmingly positive. The company has a strong competitive position and is the leading provider to the EBP customer base, which is quickly growing and requires complete outsourcing. FCF is strong and leverage is stable. However, the Commercial business remains vulnerable to AI disruption and it's too early to see the anticipated tailwinds pan out. Management made no mention of targeting IG ratings and current levels have little upside. Risks to our rating include leveraged acquisitions, AI disruption, and a weakening pharma, EBP, or biotech funding environment.

Summary: 2Q26 results were in line with expectations. Revenue grew 8.7% YoY to \$4.4bn and EBITDA margins expanded 30bp to 22.8%, resulting in EBITDA of \$994mm. The company's newly increased revenue guidance is higher than the street while EBITDA remains consistent with consensus estimates. The market demand continues to improve, as evidenced by double-digit RFP flow growth YoY

See page 6 for analyst certification and important disclosures.

North America Corporate Credit - Healthcare (HY)

Rishi S Parekh AC
(1-212) 622-2379
rishi.parekh@JPM.com

Rachel Barish
(1-212) 270-0970
rachel.barish@JPM.com
JPM Securities LLC

in the clinical environment, shortening decision timelines, and elevated emergent biopharma funding. The Commercial Solutions segment is supported by a $\sim45\%$ increase in new drug launches in 1H26 compared to 1H25 and an increasing trend from large pharma customers seeking to outsource the full commercialization of certain therapies in select geographies.

Strength in emerging biopharma funding. Management highlighted emerging biopharma (“EBP”) as a key driver of market demand, with EBP funding at \$35bn in 2Q26 (more than double the 2Q25 amount). EBP now represents \~35% of IQV’s R&DS revenue and the company derives more revenue from the emerging biopharma segment than its CRO peers. This is important given that IQV is the largest provider to the EBP segment and it continues to be where much of the industry’s innovation is coming from. For reference, a decade ago, EBP represented \~45% of all clinical trial starts globally; today, it comprises \~70%. IQVIA expects EBP R&D to grow at 2x-3x the rate of large pharma R&D spend. EBP has proven additionally beneficial as trials in the segment are full-service outsourcing, compared to large pharma trials which can be in-sourced.

AI remains a focus. Management reiterated its view that AI will contribute to market expansion in 2027 and beyond. They cited clients stating that AI in discovery will increase CRO demand as more molecules with a higher predictable success are entering development. Further, the company's AI-enabled capabilities are improving study design, accelerating timelines, and reducing operational risk across complex global trials. We believe it's still too early to determine how exactly AI will impact the CRO universe, and, although these statements seem plausible, we are cautious of how AI may impact IQV's analytics and consulting businesses within the Commercial segment.

Highlights. Book-to-bill of 1.2x was driven by \$3.15bn in new bookings (19% YoY growth), with notable strength in full-service bookings. Passthroughs and cancelations were in the normal range. Leverage remained flat sequentially at 4.1x (3.6x net) and liquidity remained ample with \$1.9bn of cash on the balance sheet and full capacity under the \$2bn RC.

3Q26 guidance. For the third quarter, IQVIA expects revenue between \$4.35bn and \$4.39bn, representing YoY growth of 5.2%-7.1%. EBITDA is expected to be \$1bn-\$1.02bn, demonstrating 5.4%-7.5% YoY growth.

FY26 guidance. Off the back of stronger than expected organic revenue growth and changes to M&A and FX impacts, IQV raised its revenue guidance to \$17.275bn-\$17.475bn, representing growth of 6.5% at the midpoint compared to the prior guidance midpoint of 5.8%. Of this 70bp increase, 100bp are related to higher organic revenue growth and 50bp higher contribution from M&A, partially offset by an 80bp reduction to FX tailwind. We note that acquisition impact is historically $\frac{2}{3}$ commercial and $\frac{1}{3}$ RD&S. EBITDA guidance was also increased to \$4bn-\$4.05bn, growing 6.25% at the midpoint and reconfirming flat YoY margins at \~23.2%.

Table 2: Summary Model

<table><tr><td></td><td>FY 2024</td><td>Q1:25</td><td>Q2:25</td><td>Q3:25</td><td>Q4:25</td><td>FY 2025</td><td>Q1:26</td><td>Q2:26</td></tr><tr><td>LTM EBITDA</td><td>3,684</td><td>3,705</td><td>3,728</td><td>3,738</td><td>3,788</td><td>3,788</td><td>3,837</td><td>3,921</td></tr><tr><td>LTM FCF</td><td>2,114</td><td>2,163</td><td>2,010</td><td>2,211</td><td>2,051</td><td>2,051</td><td>2,115</td><td>2,181</td></tr><tr><td>Cash</td><td>1,702</td><td>1,740</td><td>2,039</td><td>1,814</td><td>1,980</td><td>1,980</td><td>1,947</td><td>1,909</td></tr><tr><td>Secured Debt</td><td>7,965</td><td>8,166</td><td>7,046</td><td>7,003</td><td>7,767</td><td>7,767</td><td>8,576</td><td>7,688</td></tr><tr><td>Total Debt</td><td>14,045</td><td>14,389</td><td>15,573</td><td>15,034</td><td>15,800</td><td>15,800</td><td>15,908</td><td>16,081</td></tr><tr><td>Secured leverage</td><td>2.2x</td><td>2.2x</td><td>1.9x</td><td>1.9x</td><td>2.1x</td><td>2.1x</td><td>2.2x</td><td>2.0x</td></tr><tr><td>Total leverage</td><td>3.8x</td><td>3.9x</td><td>4.2x</td><td>4.0x</td><td>4.2x</td><td>4.2x</td><td>4.1x</td><td>4.1x</td></tr><tr><td>Net leverage</td><td>3.4x</td><td>3.4x</td><td>3.6x</td><td>3.5x</td><td>3.6x</td><td>3.6x</td><td>3.6x</td><td>3.6x</td></tr></table>

<table><tr><td>Revenue</td><td>15,405</td><td>3,829</td><td>4,017</td><td>4,100</td><td>4,364</td><td>16,310</td><td>4,151</td><td>4,368</td></tr><tr><td>Cost of Revenue</td><td>(10,030)</td><td>(2,531)</td><td>(2,694)</td><td>(2,727)</td><td>(2,928)</td><td>(10,880)</td><td>(2,796)</td><td>(2,933)</td></tr><tr><td>Percent of sales</td><td>65.1%</td><td>66.1%</td><td>67.1%</td><td>66.5%</td><td>67.1%</td><td>66.7%</td><td>67.4%</td><td>67.1%</td></tr><tr><td>SG&amp;A</td><td>(1,992)</td><td>(508)</td><td>(509)</td><td>(514)</td><td>(468)</td><td>(1,999)</td><td>(502)</td><td>(574)</td></tr><tr><td>Percent of sales</td><td>12.9%</td><td>13.3%</td><td>12.7%</td><td>12.5%</td><td>10.7%</td><td>12.3%</td><td>12.1%</td><td>13.1%</td></tr><tr><td>Equity in affiliate</td><td>90</td><td>(15)</td><td>(11)</td><td>31</td><td>94</td><td>99</td><td>(4)</td><td>(12)</td></tr><tr><td>Adjustment</td><td>206</td><td>121</td><td>108</td><td>59</td><td>(52)</td><td>236</td><td>78</td><td>130</td></tr><tr><td>EBITDA</td><td>3,684</td><td>883</td><td>910</td><td>949</td><td>1,046</td><td>3,788</td><td>932</td><td>994</td></tr><tr><td>EBITDA margin</td><td>23.9%</td><td>23.1%</td><td>22.7%</td><td>23.1%</td><td>24.0%</td><td>23.2%</td><td>22.5%</td><td>22.8%</td></tr></table>

<table><tr><td>Cash flow from ops</td><td>2,716</td><td>568</td><td>443</td><td>908</td><td>735</td><td>2,654</td><td>618</td><td>558</td></tr><tr><td>Less capex</td><td>(602)</td><td>(142)</td><td>(151)</td><td>(136)</td><td>(174)</td><td>(603)</td><td>(127)</td><td>(198)</td></tr><tr><td>Percent of sales</td><td>3.9%</td><td>3.7%</td><td>3.8%</td><td>3.3%</td><td>4.0%</td><td>3.7%</td><td>3.1%</td><td>4.5%</td></tr><tr><td>Free Cash Flow</td><td>2,114</td><td>426</td><td>292</td><td>772</td><td>561</td><td>2,051</td><td>491</td><td>360</td></tr></table>

Source: Company filings, JPM

## Fortrea (FTRE)

Recommendation: Despite an improved backdrop and diversification benefits, we remain Underweight on the credit. Fortrea remains a show-me story, leverage remains elevated, and we have yet to find a compelling reason to chase the bonds at current levels. Despite this view, we believe the company is positioned to refinance its TLA, TLB and possibly its A/R facility (reset covenants, etc.). It would not surprise us if the company attempts a global approach, but the cost savings will not be significant. Risks to our UW include stronger new bookings, market share wins, and aggressive debt paydowns. Risks to our rating include an early refinancing, M&A and stronger improvement in results.

Summary. Overall, Fortrea posted a good quarter, beating both our estimates and the street's driven by new business wins and continued booking diversification efforts. The macro and funding environment continues to improve and we believe expectations of positive FCF for 2H26 and FY26 are realistic based on 1H26 results. However, FTRE remains highly levered at 7.5x 1L leverage and did not comment on any future debt redemptions.

Backlog and new wins. Backlog was \$7.8bn and cancelations remained in line with historical trends. Backlog burn of 8.6% in 2Q26 was higher sequentially driven by service fee growth in the Clinical Pharmacology business and sequentially higher pass-through revenue in Clinical Pharmacology and Clinical Development. Fortrea noted it is looking to diversify its bookings and backlog, which is burning off into revenue, some of which are higher-margin projects. In line with the market, the company has seen the most strength in oncology compared to other therapeutic areas. Management noted that the mix of projects coming into its pipeline will likely remain steady, and would only shift if the company took on a very large vaccine or Phase III GLP-1 study earlier.

Improved biotech funding and its impact on pipeline. Similar to its peers, Fortrea noted that biotech funding has improved meaningfully, and that has bled into increasing the speed at which RFPs are coming into Fortrea's pipeline. The speed at which biotech decisions are entering and exiting the company's pipeline is starting to normalize and improve sequentially, compared to 2H25 which was characterized by extraordinarily slow decision making because funding ws oftentimes delayed or off cycle.

Momentum in China. China continues to be a hub for innovative medicines and FTRE remains focused on maintaining a strong presence in the region. Management believes this presence makes it a strong option for customers looking to run global studies in China. Echoing 1Q26 commentary, the company called out growth from Chinese biotechs and U.S. companies partnering with Chinese biotechs that are brinign medicines into the global landscape.

FY26 guidance. Fortrea increased its FY26 revenue and EBITDA guidance to \$2.62bn-\$2.69bn (from \$2.55-2.65bn) and \$205mm-\$220mm (from \$190-200mn), respectively. These improvements reflect solid performance in 1H26 due to execution against an improving mix in backlog and new business wins. Management stated that it remains focused on the balance sheet and capital allocation, and continues to expect positive FCF for the remainder of the year and the full year.

## Table 3: Summary Model

<table><tr><td></td><td>FY 2024</td><td>1Q:25</td><td>2Q:25</td><td>3Q:25</td><td>4Q:25</td><td>FY 2025</td><td>1Q:26</td><td>2Q:26</td></tr><tr><td>LTM EBITDA</td><td>181</td><td>195</td><td>192</td><td>178</td><td>182</td><td>182</td><td>198</td><td>204</td></tr><tr><td>Cash</td><td>119</td><td>102</td><td>81</td><td>131</td><td>175</td><td>175</td><td>148</td><td>169</td></tr><tr><td>Total Debt</td><td>1,440</td><td>1,531</td><td>1,492</td><td>1,366</td><td>1,366</td><td>1,366</td><td>1,366</td><td>1,366</td></tr><tr><td>Total leverage</td><td>7.9x</td><td>7.9x</td><td>7.8x</td><td>7.7x</td><td>7.5x</td><td>7.5x</td><td>6.9x</td><td>6.7x</td></tr><tr><td>Net leverage</td><td>7.3x</td><td>7.3x</td><td>7.4x</td><td>6.9x</td><td>6.5x</td><td>6.5x</td><td>6.1x</td><td>5.9x</td></tr><tr><td>Revenue</td><td>2,696</td><td>651</td><td>710</td><td>701</td><td>661</td><td>2,723</td><td>637</td><td>678</td></tr><tr><td>Direct costs</td><td>(2,162)</td><td>(535)</td><td>(577)</td><td>(579)</td><td>(529)</td><td

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
