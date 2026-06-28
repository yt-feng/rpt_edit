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
Energy | North America

# Refreshing the Price Deck

WTI has fallen to \~\$72, oil E&Ps back at pre-conflict levels, and Majors -9% below it. We refresh our estimates for the latest prices. FCF yields are still strong, with '27 median of 12% for oil E&Ps, while intrinsic valuations only reflect \~\$64 WTI. Risk-rewards screen better post the pullback.

## Key Takeaways

WTI oil has fallen another $\sim 15\%$ since the MoU, now back to $\sim$ 72/bbl. Alongside softer crude, energy stocks have also moved lower

We update our price deck to 6/19 strip, WTI assumption falls 12% in '26 while '27 stays at \$70. Our EBITDA ests are -7% vs consensus for FY26 and -6% for '27

For 2Q, our EBITDA ests are in-line with consensus for oil producers and 8% below for gas. We also forecast above consensus 2Q EPS for XOM

At \$70, our oil coverage offers median '27 FCF yield of 10% (12% US E&Ps, 9% Majors, 10% Canada). Valuations reflect \~\$64 WTI. '27 FCF yields of 9% for gas

We retain our preference for Majors and E&Ps with positive rate of change (DVN, PR & CVE). LNG producers VG and Cheniere also screen attractive.

Have stocks corrected too much? Since the US and Iran announced a memorandum of understanding (MoU) on June 14, oil prices have declined another \~15%. WTI now sits at \~\$72, only slightly above pre-conflict levels. Alongside softer crude, energy stocks have also moved lower. Notably, oil E&Ps are now trading back at pre-conflict levels and US Majors -9%. While uncertainty persists around the macro picture, we do think the risk-reward has improved post the pullback. FCF yields are strong, with a 2027 median of \~10% at prices near strip, and stocks intrinsically reflect \~\$64 WTI - below futures and our long-run \$70/bbl price expectation. We view the recent pullback as an opportunity to add exposure to Majors and high-quality E&Ps.

\- Crude Oil. Flows through the Strait of Hormuz have risen sharply over the last few weeks as oil tankers that were previously trapped behind the waterway make their way to market. Vortexa shows oil exports from countries behind the Strait exceeding 10 mb/d over the last week, approaching $\frac{2}{3}$ of pre-conflict levels. This includes a surge in Iranian flows, which have also benefited from eased sanctions and the lifting of the US blockade. Globally, US exports remain historically high and Chinese imports low, both continuing to serve as important buffers for the seaborne oil market. Still, global inventories have already drawn substantially. Fully restoring regional production and refilling storage will take time. See the latest from MS Strategist Martijn Rats here: 'Let the Oil Flow'.

\- Global Gas & LNG. JKM (Asia LNG) prices have fallen back toward \$15/ mmbtu, well off the highs but still up >50% YTD. Recent statements from QatarEnergy point to \~50% recovery in export volumes in about one month

## MS & CO. LLC

<table><tr><td colspan="2">Devin McDermott</td></tr><tr><td colspan="2">Equity Analyst and Commodities Strategist</td></tr><tr><td>Devin.McDermott@morganstanley.com</td><td>+1 212 761-1125</td></tr><tr><td colspan="2">Joe Laetsch, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joe.Laetsch@morganstanley.com</td><td>+1 212 761-8804</td></tr><tr><td colspan="2">Helen Lin</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Helen.Lin@morganstanley.com</td><td>+1 212 761-0766</td></tr><tr><td colspan="2">Svetlana Do</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Svetlana.DO@morganstanley.com</td><td>+1 212 761-2409</td></tr><tr><td colspan="2">Justin W Latran, CFA</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Justin.Latran@morganstanley.com</td><td>+1 212 761-2869</td></tr><tr><td colspan="2">Jacqueline M Kenny</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Jacqueline.Kenny@morganstanley.com</td><td>+1 212 761-2253</td></tr><tr><td colspan="2">Zackary C Warden</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Zackary.Warden@morganstanley.com</td><td>+1 212 761-4164</td></tr></table>

## EXPLORATION & PRODUCTION

<table><tr><td>North AmericaIndustry View</td><td>In-Line</td></tr><tr><td colspan="2">INTEGRATED OIL</td></tr><tr><td>North AmericaIndustry View</td><td>Attractive</td></tr></table>

See our price target changes in Exhibit 33

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

and 80% after two months - a recovery of everything except the damaged trains. This still leaves a very short window to normalize inventories before next winter. Over the last month, global consumption has started to inflect higher again alongside summer weather & storage refill needs. We see some upside to 2H26 post the pullback, followed by a more balanced 2027. See more here and here.

\- US Natural Gas. Prompt Henry Hub prices have been range-bound in the low-to-mid \$3s for most of June. We still do expect a modest improvement in 3Q, supported by higher LNG flows & power burn. LNG exports in June so far are running \~0.3 bcf/d above the May average, with feedgas deliveries to Golden Pass reaching \~600 mmcf/d this week. That said, the outlook softens again into 2027 - reflecting associated gas growth & still-elevated Haynesville activity. That said, the silver lining of lower oil prices is that it could moderate associated gas risks. See more here.

Softer prices, but valuations still attractive. We refresh our price deck and estimates using strip as of 6/19 (see Exhibit 12), lowering our FY26 WTI assumption to \~\$78/bbl (from \~\$88/bbl) with \$73 WTI for the back half of the year, while 2027 is unchanged at \~\$70. For integrated companies, US Gulf Coast refining margin assumptions are moving 22% higher in 2026. Our Henry Hub moves -8% lower for 2027. Overall, price targets move lower by -5% for oil E&Ps and -8% for gas names, but still imply 25% average upside. At prices near strip (\~\$70 WTI), we estimate a median 2027 FCF yield of 10% across our oil coverage (12% for oil E&Ps, 9% for US majors, and 10% for Canada). Intrinsically, oil E&Ps reflect long-run WTI of\~\$64/bbl, \~6% below 12-month strip.

Preliminary 2Q outlook. Incorporating actual 2Q oil & gas prices and downstream margins, our quarterly EBITDA estimates are in-line with consensus for oil producers and 8% below for gas. We also forecast above consensus EPS for XOM.

Exhibit 1: MS Price Deck (Based on 6/19/2026 Strip)

<table><tr><td>MS Model Assumptions</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>103.54</td><td>77.80</td><td>76.72</td><td>84.75</td><td>74.52</td><td>75.00</td></tr><tr><td>WTI ($/Bbl)</td><td>93.00</td><td>74.00</td><td>72.00</td><td>77.92</td><td>70.00</td><td>70.00</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2.90</td><td>3.20</td><td>3.50</td><td>3.66</td><td>3.50</td><td>3.75</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>31.05</td><td>25.02</td><td>24.78</td><td>26.86</td><td>25.49</td><td>25.58</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>29.93</td><td>31.22</td><td>25.87</td><td>25.83</td><td>24.05</td><td>14.20</td></tr></table>

<table><tr><td>Prior MS Assumptions</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>112.00</td><td>103.12</td><td>92.71</td><td>97.26</td><td>76.05</td><td>75.00</td></tr><tr><td>WTI ($/Bbl)</td><td>100.00</td><td>95.00</td><td>85.00</td><td>88.24</td><td>70.00</td><td>70.00</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2.85</td><td>3.20</td><td>3.60</td><td>3.67</td><td>3.80</td><td>3.75</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>33.56</td><td>33.70</td><td>32.62</td><td>31.65</td><td>28.26</td><td>28.04</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>24.66</td><td>23.20</td><td>20.59</td><td>21.19</td><td>14.20</td><td>14.20</td></tr></table>

<table><tr><td>% Change</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>-8%</td><td>-25%</td><td>-17%</td><td>-13%</td><td>-2%</td><td>0%</td></tr><tr><td>WTI ($/Bbl)</td><td>-7%</td><td>-22%</td><td>-15%</td><td>-12%</td><td>0%</td><td>0%</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2%</td><td>0%</td><td>-3%</td><td>0%</td><td>-8%</td><td>0%</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>-7%</td><td>-26%</td><td>-24%</td><td>-15%</td><td>-10%</td><td>-9%</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>21%</td><td>35%</td><td>26%</td><td>22%</td><td>69%</td><td>0%</td></tr></table>

Source: Bloomberg, FactSet, MS estimates. Note: GC 321 Brent crack spread is unadjusted for RINs.

## Key Charts

Exhibit 2: Oil E&Ps are now back to pre-conflict levels (including gas, the E&P sector is -5% below). The group has underperformed the broader market by \~12% over the same period.  
![](images/e27abad03cbe4a824d5f918e023e01163e526190d987bce42449d6b1d550c6e5.jpg)  
Source: Bloomberg, FactSet, MS

Exhibit 3: We estimate consensus is currently pricing in \~\$73 WTI based on 2027 EBITDAX forecasts, higher than the full-year 2027 strip price of \~\$67.  
![](images/83be30febc2b59942f8c718da173e69699ccba5ac7695b283caa364a7fbf0b8c.jpg)  
Source: FactSet, MS estimates

Exhibit 4: The median 2027 FCF yield for our oil coverage is 10% near strip (\~\$70 WTI), 12% looking just at oil E&Ps. This would move by \~3% for every \$10 change in oil.  
![](images/f04245556f0fd2077e3346ee881de7429f11f7cbdcd12d8e442f4073589bb7d9.jpg)  
Source: FactSet, MS estimates.

Exhibit 5: At \$70 WTI, near strip, our oil coverage has 5% downside vs consensus estimates (7% downside for just oil E&Ps).  
![](images/31b4f14b839379194c9a5b537278535a9f0b37480872bdbd7f45da2468d8335c.jpg)  
Source: MS estimates.

Exhibit 6: Our 2027 FCF estimates are \~11% below consensus...  
![](images/9b7cede9d5f8003745db7c13dd8f35d55cc8f136d083fc7f2e539ff417c908c3.jpg)  
Source: FactSet, MS estimates. Note: Axis cut at 30%

Exhibit 7: ...with 2027 EBITDA 6% below consensus.  
![](images/225f7c2a7b0c0ee93f0c38dd3096859aa4f901bedc4631e7a004a16ec2e0e650.jpg)  
Source: FactSet, MS estimates. Note: Axis cut at 2%

Exhibit 8: Our oil coverage has hedged $\sim 5\%$ of 2027 production on average...  
![](images/45f6a6042e955b0b62f43dcb841618f2d132c53c3f3fb12d23d98990ade9cd77.jpg)  
Source: Company Data, MS estimates

Exhibit 9: ...and \~30% for gas E&Ps  
![](images/f569fa276f916538d1b5028eb5a5be2259ba730b84b46a5b0225dbab17df7aad.jpg)  
Source: Company Data, MS estimates

Exhibit 10: Our oil coverage is pricing an average WTI price of \~\$64, \~6% below 12-month strip.  
![](images/28f954f6dba87eadffbd43393ac2b955ff8148cc348374f93d22b3d5b899bd01.jpg)  
Source: Bloomberg, MS. Note: close prices of 6.24.26.

Exhibit 11: Gas E&Ps reflect an average Henry Hub price of \~\$3.50, at the 12 month strip.  
![](images/ca1bd49898696efef0c05a7f5f2ca03698f60f7c0ab0ea93fbcdccdceaa5c11b.jpg)  
Source: Bloomberg, MS. Note: close prices of 6.24.26

## Price Target Changes

Exhibit 12: MS Price Deck (Based on 6/19/2026 Strip)

<table><tr><td>MS Model Assumptions</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>103.54</td><td>77.80</td><td>76.72</td><td>84.75</td><td>74.52</td><td>75.00</td></tr><tr><td>WTI ($/Bbl)</td><td>93.00</td><td>74.00</td><td>72.00</td><td>77.92</td><td>70.00</td><td>70.00</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2.90</td><td>3.20</td><td>3.50</td><td>3.66</td><td>3.50</td><td>3.75</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>31.05</td><td>25.02</td><td>24.78</td><td>26.86</td><td>25.49</td><td>25.58</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>29.93</td><td>31.22</td><td>25.87</td><td>25.83</td><td>24.05</td><td>14.20</td></tr></table>

<table><tr><td>Prior MS Assumptions</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>112.00</td><td>103.12</td><td>92.71</td><td>97.26</td><td>76.05</td><td>75.00</td></tr><tr><td>WTI ($/Bbl)</td><td>100.00</td><td>95.00</td><td>85.00</td><td>88.24</td><td>70.00</td><td>70.00</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2.85</td><td>3.20</td><td>3.60</td><td>3.67</td><td>3.80</td><td>3.75</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>33.56</td><td>33.70</td><td>32.62</td><td>31.65</td><td>28.26</td><td>28.04</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>24.66</td><td>23.20</td><td>20.59</td><td>21.19</td><td>14.20</td><td>14.20</td></tr></table>

<table><tr><td>% Change</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>-8%</td><td>-25%</td><td>-17%</td><td>-13%</td><td>-2%</td><td>0%</td></tr><tr><td>WTI ($/Bbl)</td><td>-7%</td><td>-22%</td><td>-15%</td><td>-12%</td><td>0%</td><td>0%</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2%</td><td>0%</td><td>-3%</td><td>0%</td><td>-8%</td><td>0%</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>-7%</td><td>-26%</td><td>-24%</td><td>-15%</td><td>-10%</td><td>-9%</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>21%</td><td>35%</td><td>26%</td><td>22%</td><td>69%</td><td>0%</td></tr></table>

Source: Bloomberg, FactSet, MS estimates. Note: GC 321 Brent crack spread is unadjusted for RINs.

Exhibit 13: Price Target Changes

<table><tr><td>Company</td><td>Ticker</td><td>New PT</td><td>Old PT</td><td> $\Delta (\%)$ </td><td>New Rating</td><td>Old Rating</td><td>PT% Upside</td></tr><tr><td colspan="8">US Majors</td></tr><tr><td>Chevron Corp.</td><td>CVX</td><td>210</td><td>214</td><td>(2%)</td><td>OW</td><td>OW</td><td>22%</td></tr><tr><td>Exxon Mobil Corporation</td><td>XOM</td><td>168</td><td>171</td><td>(2%)</td><td>OW</td><td>OW</td><td>22%</td></tr><tr><td>Integrateds Median</td><td></td><td></td><td></td><td>(2%)</td><td></td><td></td><td>22%</td></tr><tr><td colspan="8">Canadian Integrateds (CAD unless noted)</td></tr><tr><td>Canadian Natural Resources Ltd</td><td>CNQ</td><td>67</td><td>67</td><td>0%</td><td>EW</td><td>EW</td><td>19%</td></tr><tr><td>Cenovus Energy Inc</td><td>CVE</td><td>43</td><td>43</td><td>0%</td><td>OW</td><td>OW</td><td>23%</td></tr><tr><td>Imperial Oil Ltd</td><td>IMO</td><td>138</td><td>141</td><td>(2%)</td><td>EW</td><td>EW</td><td>(14%)</td></tr><tr><td>Suncor Energy Inc</td><td>SU</td><td>92</td><td>93</td><td>(1%)</td><td>EW</td><td>EW</td><td>19%</td></tr><tr><td>Canadian Integrateds Median</td><td></td><td></td><td></td><td>(1%)</td><td></td><td></td><td>19%</td></tr><tr><td colspan="8">Oil E&amp;Ps</td></tr><tr><td>APA Corp.</td><td>APA</td><td>41</td><td>44</td><td>(7%)</td><td>UW</td><td>UW</td><td>23%</td></tr><tr><td>Chord Energy Corp.</td><td>CHRD</td><td>169</td><td>175</td><td>(3%)</td><td>OW</td><td>OW</td><td>41%</td></tr><tr><td>ConocoPhillips</td><td>COP</td><td>146</td><td>153</td><td>(5%)</td><td>OW</td><td>OW</td><td>37%</td></tr><tr><td>Devon Energy Corp.</td><td>DVN</td><td>63</td><td>66</td><td>(5%)</td><td>OW</td><td>OW</td><td>48%</td></tr><tr><td>Diamondback Energy, Inc.</td><td>FANG</td><td>216</td><td>229</td><td>(6%)</td><td>OW</td><td>OW</td><td>18%</td></tr><tr><td>EOG Resources Inc.</td><td>EOG</td><td>156</td><td>160</td><td>(3%)</td><td>EW</td><td>EW</td><td>17%</td></tr><tr><td>Matador Resources Co.</td><td>MTDR</td><td>66</td><td>75</td><td>(12%)</td><td>EW</td><td>EW</td><td>32%</td></tr><tr><td>Murphy Oil Corp.</td><td>MUR</td><td>35</td><td>37</td>

[中间内容因长度限制已省略]

ere, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Exploration & Production

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/25/2026)</td></tr><tr><td colspan="3">Devin McDermott</td></tr><tr><td>Antero Resources Corp (AR.N)</td><td>O (04/17/2024)</td><td>$34.50</td></tr><tr><td>APA Corp (APA.O)</td><td>U (04/15/2024)</td><td>$33.42</td></tr><tr><td>Chord Energy Corporation (CHRD.O)</td><td>O (03/27/2026)</td><td>$119.48</td></tr><tr><td>CNX Resources Corp (CNX.N)</td><td>U (01/10/2025)</td><td>$33.61</td></tr><tr><td>Comstock Resources Inc. (CRK.N)</td><td>E (01/10/2025)</td><td>$13.87</td></tr><tr><td>ConocoPhillips (COP.N)</td><td>O (12/16/2024)</td><td>$106.41</td></tr><tr><td>Devon Energy Corp (DVN.N)</td><td>O (12/11/2023)</td><td>$42.60</td></tr><tr><td>Diamondback Energy Inc (FANG.O)</td><td>O (12/11/2020)</td><td>$182.55</td></tr><tr><td>EOG Resources Inc (EOG.N)</td><td>E (12/11/2023)</td><td>$133.59</td></tr><tr><td>EQT Corp. (EQT.N)</td><td>O (11/18/2021)</td><td>$51.65</td></tr><tr><td>Expand Energy Corp (EXE.O)</td><td>O (01/10/2025)</td><td>$88.44</td></tr><tr><td>Matador Resources Co (MTDR.N)</td><td>E (01/10/2025)</td><td>$50.16</td></tr><tr><td>Murphy Oil Corporation (MUR.N)</td><td>U (01/22/2025)</td><td>$35.39</td></tr><tr><td>Northern Oil &amp; Gas Inc. (NOG.N)</td><td>U (08/18/2025)</td><td>$19.74</td></tr><tr><td>Occidental Petroleum Corp (OXY.N)</td><td>E (08/18/2025)</td><td>$51.21</td></tr><tr><td>Ovintiv Inc (OVV.N)</td><td>E (03/27/2026)</td><td>$53.55</td></tr><tr><td>Permian Resources Corp (PR.N)</td><td>O (01/10/2025)</td><td>$18.86</td></tr><tr><td>Range Resources Corp. (RRC.N)</td><td>E (03/26/2025)</td><td>$36.31</td></tr><tr><td>Tourmaline Oil Corp. (TOU.TO)</td><td>E (01/10/2025)</td><td>C$60.02</td></tr><tr><td>Viper Energy Inc (VNOM.O)</td><td>O (08/18/2025)</td><td>$43.55</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## INDUSTRY COVERAGE: Integrated Energy

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/25/2026)</td></tr><tr><td colspan="3">Devin McDermott</td></tr><tr><td>Canadian Natural Resources Ltd (CNQ.TO)</td><td>E (10/07/2021)</td><td>C$56.19</td></tr><tr><td>Cenovus Energy (CVE.TO)</td><td>O (10/07/2021)</td><td>C$34.96</td></tr><tr><td>Chevron Corporation (CVX.N)</td><td>O (08/04/2025)</td><td>$172.24</td></tr><tr><td>Exxon Mobil Corporation (XOM.N)</td><td>O (05/14/2024)</td><td>$137.55</td></tr><tr><td>Imperial Oil Ltd (IMO.TO)</td><td>E (10/07/2021)</td><td>C$160.92</td></tr><tr><td>Suncor Energy Inc (SU.TO)</td><td>E (12/16/2024)</td><td>C$77.10</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

## © 2026 MS
"""
