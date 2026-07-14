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
# Payments, Processors & IT Services

# FISV, FIS, GPN: What is the 'true' multiple?

![](images/2ed13a5b7052f037141a34924a9d8783b7875a97efbfacd409322858b827fffd.jpg)

Harshita Rawat, CFA

+1 917 344 8485

harshita.rawat@bernsteinsg.com

![](images/f4c3c8e7610183ff43829ac95cf83e774d7f75ecb6d7fde4615bd48db9e7fc30.jpg)

Viola Chen

+1 917 344 8614

viola.chen@bernsteinsg.com

![](images/e82adea6155319c96656d4a6042bc83af6ba259b583956bec089495d4a158247.jpg)

Simran Ratani

+1 917 344 8329

simran.ratani@bernsteinsg.com

FIS, FISV and GPN are currently trading at 6.4x/6.0x/5.1x NTM PE multiple, near their lowest levels in history (also see our note). As such, investors appear to be taking a fresh look at the names. It is, however, a bit challenging to assess the ‘true’ multiples for the stocks given the earnings adjustments (which have historically been more recurring in nature), lower FCF conversion, high leverage and very low ‘adj’ tax rates. In this note, we present our updated earnings quality analysis, and present what we believe are clean EV/NOPAT multiples (we find EV/NOPAT a better metric vs. P/E given the leverage) across the 3 names. We also discuss potential for buybacks and capital returns.

## When adjusted for earnings quality and tax rates, we see several turns of

differences between clean and reported multiples. While the multiples are abysmally low on non-GAAP 2026 EPS (FIS 6.7x, FISV 6.3x, GPN 5.6x), they are several turns higher on clean EV/NOPAT (FIS 14.3x, FISV 10.8x, GPN 11.3x). We note that 2027 analysis gets a bit trickier because we have to make a fair bit of assumptions on ‘adjustments’. Our estimates for 2027 clean EV/NOPAT multiples include \~13x for FIS, \~10x for FISV and \~10x for GPN vs. non-GAAP PE (on consensus adj. numbers) of \~6x for FIS, \~6x for FISV and \~5x for GPN.

We see clean earnings as a % of non-GAAP earnings at 77%/76% for FIS, 94%/75% for FISV, and 75%/71% for GPN in 2025/1Q26, respectively. On Clean FCF conversion, we estimate 53%/64% conversion for FIS, 90%/12% for FISV and 67%/-50% for GPN in FY2025 and 1Q26, respectively. We do note that FIS started reporting a cleaner version of FCF since late 2025, which is calculated as Cash From Operating Activities - CapEx - true one-time cash outflows.

In our clean earnings definition, we give companies the benefit of adding back the somewhat understandable purchase accounting amortization and true one-offs, but include other expenses e.g. ‘transformation costs’, often-vague restructuring costs, M&A integration expenses which can continue for several years post a deal (also M&A has been recurring for the companies and not truly one-time). In our clean FCF definition, we similarly exclude true one-offs but add back recurring cash expenses. We also wonder to what extent a low ‘adj.’ tax rate (e.g., FIS at \~12%/13% in 2026/2027) is sustainable.

Sometimes companies adjust M&A integration expenses far beyond what is typically acceptable (several years after a deal closes). Transformation has become a major adjustment recently too - e.g. FISV added back >\$140mn of transformation expense related to the One Fiserv initiative to adj. net income in 1Q26; GPN added back \$96mn in 1Q26 related to the more recent Genius build-out reorg, but we note this is a longer-running add-back covering ongoing internal transformation and GTM realignment initiatives. FIS has been adding back enterprise transformation and platform modernization expenses of \$262mn in 2024, \$157mn in 2025 and \$93m in 1Q26.

More buybacks at these valuation levels? GPN is already doing this. By year-end 2027, GPN (and PayPal) could buy back \~30% of their existing market cap (investors may have to wait longer for FIS and FISV). The complication for FIS and FISV is that they are in the midst of de-leveraging post recent acquisitions. We will do more work on potential for unlocking shareholder value through asset sales (e.g., for FISV). See our recent note on STAR/Accel.

## INVESTMENT IMPLICATIONS

Overall, while we acknowledge rock bottom valuation levels across the fintech space (including for FIS, GPN, FISV), we continue to prefer V, MA and Adyen as our favorite ideas.

We rate V, MA, Adyen, Block and Toast OP. We rate Klarna, FISV, FIS, GPN and PYPL OP.

## OUR METHODOLOGY AND EXHIBITS

## A note on Earnings adjustment methodology:

\- We calculate FY25/1Q26 Clean Net Income by taking company reported Non-GAAP Net Income and subtracting adjustments that we deem valid (e.g. merger, integration costs, severance costs, and reorg/transformation costs).

\- For calculating clean FCF, we took company reported adj. FCF for FY25 and 1Q26, and removed acquisition and integration expenses and other company specific-adjustments we view as not adjustable.

\- For Clean NOPAT calculation, we took Clean Operating Income calculated in a similar way as Clean Net Income, subtracting normalized tax expense assuming 20% tax rate. Adj. NOPAT is calculated as Adjusted Operating Income as reported by companies minus Adjusted Taxes.

EXHIBIT 1: We see clean earnings as a % of non-GAAP earnings as 77%/76% for FIS, 94%/75% for FISV, and 75%/71% for GPN in 2025/1Q26, respectively

<table><tr><td rowspan="2"></td><td colspan="2">FIS</td><td colspan="2">FISV</td><td colspan="2">GPN</td></tr><tr><td>2025</td><td>1Q26</td><td>2025</td><td>1Q26</td><td>2025</td><td>1Q26</td></tr><tr><td>GAAP Net Income</td><td>908</td><td>152</td><td>3,480</td><td>571</td><td>1,400</td><td>(1,800)</td></tr><tr><td>Merger, integration costs</td><td>708</td><td>167</td><td>59</td><td>29</td><td>332</td><td>291</td></tr><tr><td>Severance costs</td><td>-</td><td>-</td><td>79</td><td>73</td><td>-</td><td>-</td></tr><tr><td>Amortization of acquisition-related intangible assets</td><td>669</td><td>290</td><td>1,304</td><td>311</td><td>1,367</td><td>747</td></tr><tr><td>Tax impact of adjustments</td><td>(40)</td><td>14</td><td>(275)</td><td>(94)</td><td>(97)</td><td>1,454</td></tr><tr><td>Gain on sale of businesses</td><td>18</td><td>104</td><td>(68)</td><td>(83)</td><td>(572)</td><td>(22)</td></tr><tr><td>Unconsolidated affiliate activities</td><td>561</td><td>11</td><td>(11)</td><td>9</td><td>(69)</td><td>5</td></tr><tr><td>Transformation</td><td>-</td><td>-</td><td>125</td><td>142</td><td>406</td><td>96</td></tr><tr><td>Other</td><td>199</td><td>(33)</td><td>52</td><td>-</td><td>190</td><td>39</td></tr><tr><td>Adj. Net Income, reported</td><td>3,023</td><td>705</td><td>4,745</td><td>958</td><td>2,957</td><td>809</td></tr><tr><td>(-) Merger, integration costs</td><td>708</td><td>167</td><td>59</td><td>29</td><td>332</td><td>141</td></tr><tr><td>(-) Severance costs</td><td>-</td><td>-</td><td>79</td><td>73</td><td>-</td><td>-</td></tr><tr><td>(-) Transformation</td><td>-</td><td>-</td><td>125</td><td>142</td><td>406</td><td>96</td></tr><tr><td>Clean Net Income</td><td>2,315</td><td>538</td><td>4,482</td><td>714</td><td>2,219</td><td>572</td></tr><tr><td>Clean Net Income as % of adj. Net Income</td><td>77%</td><td>76%</td><td>94%</td><td>75%</td><td>75%</td><td>71%</td></tr><tr><td>Adj. EPS</td><td>$5.76</td><td>$1.36</td><td>$8.64</td><td>$1.79</td><td>$12.22</td><td>$2.96</td></tr><tr><td>Clean EPS</td><td>$4.41</td><td>$1.04</td><td>$8.16</td><td>$1.33</td><td>$9.17</td><td>$2.09</td></tr></table>

FISV/FIS/GPN: We remove merger, integration and other costs, severance costs and reorganization/traformation costs from non-GAAP earnings/NOPAT to arrive at clean earnings/NOPAT. For GPN: we add back one-time transaction-related costs due to the WP deal closing to clean earnings/NOPAT.
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 2: FCF conversion has also been weak even as a % of adj. earnings

<table><tr><td rowspan="2"></td><td colspan="2">FIS</td><td colspan="2">FISV</td><td colspan="2">GPN</td></tr><tr><td>2025</td><td>1Q26</td><td>2025</td><td>1Q26</td><td>2025</td><td>1Q26</td></tr><tr><td>Adj. FCF</td><td>2,166</td><td>474</td><td>4,435</td><td>259</td><td>3,001</td><td>544</td></tr><tr><td>(-) Acquisition, integration expenses</td><td>563</td><td>22</td><td>158</td><td>46</td><td>332</td><td>141</td></tr><tr><td>(-) Other acqui. and separation adjustments</td><td>0</td><td>0</td><td>-</td><td>-</td><td>308</td><td>719</td></tr><tr><td>(-) Transformation</td><td>0</td><td>0</td><td>9</td><td>95</td><td>382</td><td>90</td></tr><tr><td>Clean FCF</td><td>1,603</td><td>452</td><td>4,268</td><td>118</td><td>1,980</td><td>(406)</td></tr><tr><td>Clean FCF conversion (as % of Adj. NI)</td><td>53%</td><td>64%</td><td>90%</td><td>12%</td><td>67%</td><td>-50%</td></tr><tr><td>Adj. FCF conversion (as % of Adj. NI)</td><td>72%</td><td>67%</td><td>93%</td><td>27%</td><td>101%</td><td>67%</td></tr></table>

Adjustment calculations: we subtract from Adj. FCF acquisition, integration and other expenses, severance and other seperation expenses, and reorg/ transformation expenses to to arrive at clean FCF. For GPN: we add back one-time transaction-related costs due to the WP deal closing to clean FCF. Source: Company reports, Bernstein estimates and analysis  
EXHIBIT 3: For FIS and GPN - clean earnings are consistently 20-30% below adjusted numbers  
'Clean' Net Income as % of Adj. Net Income

![](images/e86ea8aeaf360b9fdca7196cb558a2a1867f665d9664db0e09054e72ae6e3ee5.jpg)  
For GPN: we add back one-time transaction-related costs due to the WP deal closing to clean earnings  
Source: Company reports, Bernstein estimates and analysis  
EXHIBIT 4: We have been closely watching ‘clean’ FCF as % of reported adj. FCF  
Clean FCF Conversion (as % of Adj. FCF)

![](images/1474afe5fcd9c49a45d23de9b5f3f54fffdc848ad4ac510ca497ca6842388236.jpg)  
For GPN: we added back one-time transaction-related costs due to the WP deal closing to clean FCF  
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 5: While the multiples are abysmally low on non-GAAP 2026 EPS (FIS 6.7x, FISV 6.3x, GPN 5.6x)...

P/E Multiple (2026E)  
![](images/32a1f9dbc6d94507ec658b7ec69d760b0b62c1c92623857a22db4a0ec054d2a4.jpg)  
Market data as of 7/13/2026  
Source: Company reports, Bernstein estimates and analysis  
EXHIBIT 6: ...they are several turns higher on clean EV/NOPAT (FIS 14.3x, FISV 10.8x, GPN 11.3x)  
EV/NOPAT Multiple (2026E)

![](images/994870c154d90d8f9e064af1a28e459838e1deed8fae28b5d3b763b29ac2f6df.jpg)  
EXHIBIT 7: We note that 2027 analysis gets a bit trickier because we have to make a fair bit of assumptions on ‘adjustments’. Our estimates for 2027 PE multiples include 7.3x for FIS, 6.3x for FISV, and 5.8x for GPN

P/E Multiple (2027E)  
![](images/548263c33fddfe3198951147e93e647aa6c954093482a90b88c5063b0fb27441.jpg)  
Market data as of 7/13/2026  
Source: Company reports, Bernstein estimates and analysis  
Adj NOPAT is calculated using reported Adj. Operating Income - reported Adj. tax expenses; Clean NOPAT is calculated using Clean Operating Income - Taxes assuming normalized 20% tax rate; Market data as of 7/13/2026
Source: Company reports, Bernstein estimates and analysis  
EXHIBIT 8: ...and clean EV/NOPAT multiples include \~13x for FIS, \~10x for FISV and \~10x for GPN  
EV/NOPAT Multiple (2027E)

![](images/7a831e3a2dffc8b3a5bf1cfe269c42b67e08084a07a5d5c817a5782879082df1.jpg)  
Adj NOPAT is calculated using reported Adj. Operating Income - reported Adj. tax expenses; Clean NOPAT is calculated using Clean Operating Income - Taxes assuming normalized 20% tax rate; Market data as of 7/13/2026
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 9: Many companies (e.g., PYPL and GPN) are already doing aggressive buybacks; FIS and FISV are leverage constrained.

Buybacks as a % of Market Cap (FY26E)

![](images/402f9a0afda59b4453bfcf11c5804b221c80caea2812b22d9bf1bf222d208844.jpg)  
Market data as of 7/13/2026
Source: Company reports, Bernstein estimates and analysis  
EXHIBIT 10: FIS, FISV are in the midst of de-leveraging post recent acquisitions (important for their banking business) - and meaningful buybacks can't happen in the near-term

Net Debt / EBITDA (1Q26)  
![](images/ebe1c057829b9e26f8053299cffcc243b10dd389834c2eba7e769c4039a59989.jpg)  
Net Debt = Current portion of long-term debt + long term debt - cash and cash equivalents; EBITDA = 1Q26 Annualized
Source: Company reports, Bernstein analysis  
EXHIBIT 11: We also wonder to what extent a low ‘adj’ tax rate (e.g., FIS at \~12% in 2026/13% in 2027) is sustainable

Adjusted Tax Rates (2026E)  
![](images/ec5849c2ecce23813f7dd548063945d1f388ce7ec1ca86dad217a050ee7586b6.jpg)  
Source: Company reports, Bernstein estimates and analysis

NTM PE Multiple (Last 10 Years)

EXHIBIT 12: FIS, FISV and GPN are currently trading at 6.4x/6.0x/5.1x NTM PE multiple, near their lowest levels in history  
![](images/abba20c11f6e7590177db09b8476d6992ffdf01597c5af7e5700008e684fc041.jpg)  
market data as of 7/13/20206

Source: Bloomberg, Bernstein analysis

## PLEASE SEE LINKS TO OUR RECENT RESEARCH:

• Payments: WSJ Reports Large Banks Explore Fiserv Debit Network Deal; Implications for V/MA, Fiserv, Fintechs (July 2026)

\- Payments/Fintech: Stocks near 10yr lows – is it time for bold actions? (June 2026)

• US Long View: 2026 Edition (May 2026)

• The Age of Agents: Insights from our Inaugural Agentic Commerce Day (April 2026)

• Payments/Fintech 2026: A year to remember? Top themes and stock ideas (January 2025)

• Payments: Stripe-Stablecoins, Walmart-Open AI, Visa Agent Protocol, Spending Trends. Our perspectives. (October 2025)

• Payments: Ripe for stock-picking? (September 2025)

• Payments: Debit Interchange Ruling; Our thoughts (August 2025)

• Global Payments-Elliott: What can an activist do? (July 2025)

• Payments Primer: Our Slide Deck (June 2025)

• GPN-FIS-Worldpay: The weekend after; does the deal go through? (April 2025)

\- Quick Take: GPN-Worldpay - why now (vs. buybacks) and why this price? FIS-Issuer - likely synergistic at an decent price (April 2025)

• Payments: What happens in a recession? (Mar 2025)

• Payments 2025: Key Themes to Watch and Stock Cheatsheets (Jan 2025)

• Payments: A look at earnings quality and our 'clean' comps table (Jan 2024)

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">13 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>FIS (FIS)</td><td>M</td><td>USD</td><td>41.93</td><td>73.00</td><td>(67.3)%</td><td>USD</td><td>5.76</td><td>6.30</td><td>6.91</td><td>7.3</td><td>6.7</td><td>6.1</td></tr><tr><td>FISV(Fiserv)</td><td>M</td><td>USD</td><td>51.18</td><td>76.00</td><td>(89.7)%</td><td>USD</td><td>8.64</td><td>8.06</td><td>8.76</td><td>5.9</td><td>6.3</td><td>5.8</td></tr><tr><td>GPN (Global Payments)</td><td>M</td><td>USD</td><td>76.85</td><td>86.00</td><td>(23.1)%</td><td>USD</td><td>12.22</td><td>13.89</td><td>16.13</td><td>6.3</td><td>5.5</td><td>4.8</td></tr><tr><td>XYZ (Block Inc)</td><td>O</td><td>USD</td><td>78.72</td><td>85.00</td><td>0.2%</td><td>USD</td><td>2,084</td><td>3,347</td><td>4,700</td><td>44.2%</td><td>50.2%</td><td>32.0%</td></tr><tr><td>PYPL (PayPal)</td><td>M</td><td>USD</td><td>47.65</td><td>45.00</td><td>(53.8)%</td><td>USD</td><td>5.31</td><td>5.23</td><td>5.30</td><td>9.0</td><td>9.1</td><td>9.0</td></tr><tr><td>MA (Mastercard)</td><td>O</td><td>USD</td><td>537.70</td><td>710.00</td><td>(22.9)%</td><td>USD</td><td>17.01</td><td>19.82</td><td>22.82</td><td>31.6</td><td>27.1</td><td>23.6</td></tr><tr><td>TOST (Toast)</td><td>O</td><td>USD</td><td>29.96</td><td>39.00</td><td>(51.6)%</td><td>USD</td><td>633.00</td><td>802.7

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
