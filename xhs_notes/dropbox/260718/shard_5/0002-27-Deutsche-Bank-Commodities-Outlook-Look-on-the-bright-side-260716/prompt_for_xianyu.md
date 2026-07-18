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
# Commodities Commodities Outlook

Europe
North America
Global

Date
16 July 2026

# Look on the bright side

Voting for this year's Extel Global Fixed Income Research Survey is open, and we would appreciate your 5-star vote in the Global Commodities category (Link).

## Challenging external environment is not all bad

The external environment remains a challenging one for commodities from the standpoint of geopolitical volatility, which we expect to continue. However global growth has remained resilient to the energy disruption with only minor downgrades, and we prefer not to chase recent USD strength, maintaining a bearish dollar bias into year-end. Moreover, there is a silver lining in terms of the resulting incentive to build supply resilience in both critical minerals and energy.

## Precious metals: Limits to Fed hawkishness

We see limits to Fed hawkishness and its impact on gold. Recent moves have been orthogonal to the gold-rates regression, and the 2022 example shows that such relationships are subject to change. Speculative flows remain a headwind but we expect gold and silver higher by the end of the year as structural government debt expansion wins out over sharp but short-lived moves in rates and FX. For the PGMs, combined demand may drop 455 koz (3%) on weaker catalysed vehicle sales, although palladium is temporarily shielded by a one-off decline in Russian production. Large dislocations persist in crude oil supply, refinery runs, and crack spreads which will take at least until the end of the year to normalise. However once complete, we think the reality of a significant surplus in 2027 will become the dominant focus.

## Industrial metals: macro headwinds, structural story intact

Copper prices have come under pressure from a firmer US dollar and a pull back in Al capex related equities. The supply-side remains tight and we forecast a rising profile from \~\$13,000/t in Q3 to \~\$13,600/t in Q4. An update on US copper tariffs is expected in H2 and could create volatility, depending on the outcome (refer to our US tariffs report for details). Aluminium prices have corrected sharply amid evidence of quicker than expected smelter restarts in the Gulf. We see scope for a modest rebound in prices in H2 (\~\$3,300/t in Q4), before normalising towards \~\$3,000/t through 2027 as supply from the Gulf returns. Iron ore has been under pressure as the war drivers have largely unwound, while firm seaborne exports and early signs of Simandou ramp-up are reinforcing the supply headwind. We expect support from the upper end of the cost curve (> \$100/t) to limit downside during a seasonally soft summer.

Liam Fitzpatrick
Research Analyst
+44-20-754-13233

Bastian Synagowitz
Research Analyst
+41-44-227-3377

Corinne Blanchard
Research Analyst
+1-904-645-2360

## Table Of Contents

Commodities outlook....3   
DB commodity price forecasts....4   
Outlook: Challenging external environment is not all bad....5   
Key calls....10   
Copper: structural tightness amidst tariff uncertainty....10   
Aluminium: supply recovery....10   
Iron ore: cost curve support....11   
Crude oil: Refined product tightness persists....11   
Gold and silver: Limits to Fed hawkishness....12   
PGMs: Auto sales weakness on higher oil....13   
Commodities in charts....14   
China and LME inventory snapshot....14   
Copper: refined surplus, mine supply deficit....16   
Aluminium: passing the peak....18   
Iron ore: war drivers fading....20   
Gold and silver: Limits to Fed hawkishness....23   
PGMs: Auto sales weakness on higher oil....24   
Crude oil: Refined product tightness persists....25

## Commodities outlook

## Energy

Figure 1: Last 1 month performance (%)  
![](images/eb3ca8843e428cdf054661870eed6c8672c174f7bba01b00421da0e52da1017a.jpg)  
Industrial metals and ferrous

Figure 2: Last 12 months' performance (%)  
![](images/1c3815244a77bf28e64988d52ad2dc8ab989a90b8a5398a1f1c63f487ecc8e66.jpg)  
Source : DB, Bloomberg Finance LP (data as of 14-Jul-26)

Figure 3: Last 1 month performance (%)  
![](images/a78f1777c2fea93815972faaba52c1fabfbbac2c044fd5a082e5c5f3b181b2cc.jpg)  
Source : DB, Bloomberg Finance LP (data as of 14-Jul-26). Coking coal represent 1m Futures

Figure 4: Last 12 months' performance (%)  
![](images/5960e96ae8fbc779668609bb611abbbacfd1d8c92aa290e06bd77d39350c6fd7.jpg)  
Source : DB, Bloomberg Finance LP (data as of 14-Jul-26). Coking coal represent 1m Futures  
Figure 5: Last 1 month performance (%)

Precious metals

![](images/32f5c8498bb61c0cf3d91da58a9ad00ec8e0ee23d54702cdede10fe989b30433.jpg)

Figure 6: Last 12 months' performance (%)  
![](images/74600e6b6450a1c9ae87983fafe01e8602e70427498ce5b57cda3aef86f84ef5.jpg)  
Source : DB, Bloomberg Finance LP (data as of 14-Jul-26)

## DB commodity price forecasts

Figure 7: Base metals price forecasts

<table><tr><td>USD/t</td><td>2024</td><td>2025</td><td>Q1 26</td><td>Q2 26</td><td>Q3 26</td><td>Q4 26</td><td>2026</td><td>2027</td><td>2028</td><td>Spot</td></tr><tr><td>Aluminium (USc/lb)</td><td>109.8</td><td>119.3</td><td>145.1</td><td>161.7</td><td>145.1</td><td>149.7</td><td>150.4</td><td>144.0</td><td>136.1</td><td>144.1</td></tr><tr><td>USD/t</td><td>2,420</td><td>2,631</td><td>3,198</td><td>3,565</td><td>3,200</td><td>3,300</td><td>3,316</td><td>3,175</td><td>3,000</td><td>3,177</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>-20.0%</td><td>-13.2%</td><td>-9.4%</td><td>-10.6%</td><td>-6.3%</td><td></td></tr><tr><td>Copper (USc/lb)</td><td>414.9</td><td>451.3</td><td>581.7</td><td>604.8</td><td>589.7</td><td>616.9</td><td>598.3</td><td>567.0</td><td>569.6</td><td>616.7</td></tr><tr><td>USD/t</td><td>9,146</td><td>9,949</td><td>12,824</td><td>13,333</td><td>13,000</td><td>13,600</td><td>13,189</td><td>12,500</td><td>12,558</td><td>13,596</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>4.0%</td><td>8.8%</td><td>3.2%</td><td>4.2%</td><td>13.2%</td><td></td></tr><tr><td>Zinc (USc/lb)</td><td>126.0</td><td>130.0</td><td>146.8</td><td>156.9</td><td>154.2</td><td>154.2</td><td>153.1</td><td>145.1</td><td>137.7</td><td>163.5</td></tr><tr><td>USD/t</td><td>2,777</td><td>2,866</td><td>3,237</td><td>3,460</td><td>3,400</td><td>3,400</td><td>3,374</td><td>3,200</td><td>3,035</td><td>3,605</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>13.3%</td><td>13.3%</td><td>6.5%</td><td>10.3%</td><td>7.4%</td><td></td></tr></table>

Source: DB estimates; Figures are period averages. Q3 26 to 2028 are our forecasts. Aluminium price changes in comparison to the "Global Aluminium" report published on 1 June 2026. Copper and zinc price changes in comparison to the "Pricing Update" report published on 14 April 2026.

Figure 8: Oil price forecasts

<table><tr><td>USD</td><td>2024</td><td>2025</td><td>Q1 26</td><td>Q2 26</td><td>Q3 26</td><td>Q4 26</td><td>2026</td><td>2027</td><td>2028</td><td>Spot</td></tr><tr><td>WTI (bbl)</td><td>75.8</td><td>64.9</td><td>72.3</td><td>92.5</td><td>77.0</td><td>72.0</td><td>78.5</td><td>67.0</td><td>73.3</td><td>79.9</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>6.9%</td><td>7.5%</td><td>3.3%</td><td>0.0%</td><td>0.0%</td><td></td></tr><tr><td>Brent (bbl)</td><td>79.9</td><td>68.2</td><td>78.4</td><td>96.7</td><td>80.0</td><td>75.0</td><td>82.5</td><td>70.0</td><td>76.4</td><td>85.3</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>6.7%</td><td>7.1%</td><td>3.1%</td><td>0.0%</td><td>0.0%</td><td></td></tr></table>

Source : DB estimates; Figures are period averages. Q3 26 to 2028 are our forecasts. Price change in comparison to the "Hsueh on Oil" report published on 6 July 2026.

## Figure 9: Iron ore and coking coal price forecasts

<table><tr><td>USD/t</td><td>2024</td><td>2025</td><td>Q1 26</td><td>Q2 26</td><td>Q3 26</td><td>Q4 26</td><td>2026</td><td>2027</td><td>2028</td><td>Spot</td></tr><tr><td>Iron Ore 61% Fines CFR</td><td>110</td><td>102</td><td>104</td><td>105</td><td>98</td><td>100</td><td>102</td><td>100</td><td>99</td><td>99</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>0.0%</td><td>-0.4%</td><td>0.0%</td><td>0.0%</td><td></td></tr><tr><td>Premium HCC</td><td>244</td><td>188</td><td>232</td><td>238</td><td>230</td><td>230</td><td>233</td><td>225</td><td>220</td><td>233</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>7.0%</td><td>0.0%</td><td>1.8%</td><td>0.0%</td><td>0.0%</td><td></td></tr><tr><td>Newcastle thermal FOB</td><td>136</td><td>106</td><td>120</td><td>137</td><td>135</td><td>130</td><td>131</td><td>130</td><td>120</td><td>128</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>-3.6%</td><td>0.0%</td><td>-0.6%</td><td>0.0%</td><td>0.0%</td><td></td></tr></table>

Source: DB estimates; Figures are period averages. Q3 26 to 2028 are our forecasts. Prior to 2026, iron ore prices were marked to market based on the 62% Fe benchmark price. Price changes in comparison to the "Pricing Update" report published on 14 April 2026.

Figure 10: Precious metals price forecasts

<table><tr><td>USD/oz</td><td>2024</td><td>2025</td><td>Q1 26</td><td>Q2 26</td><td>Q3 26</td><td>Q4 26</td><td>2026</td><td>2027</td><td>2028</td><td>Spot</td></tr><tr><td>Gold</td><td>2,387</td><td>3,440</td><td>4,873</td><td>4,508</td><td>4,300</td><td>4,600</td><td>4,570</td><td>5,100</td><td>5,442</td><td>4,033</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-4.2%</td><td>-1.1%</td><td>-3.8%</td><td>0.0%</td><td></td></tr><tr><td>Silver</td><td>28.2</td><td>40.1</td><td>83.9</td><td>73.1</td><td>65.0</td><td>70.0</td><td>73.0</td><td>77.5</td><td>78.5</td><td>58.0</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-4.1%</td><td>-1.0%</td><td>-3.7%</td><td>-6.2%</td><td></td></tr><tr><td>Platinum</td><td>956</td><td>1,283</td><td>2,204</td><td>1,915</td><td>1,720</td><td>1,840</td><td>1,920</td><td>2,040</td><td>2,300</td><td>1,623</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-4.2%</td><td>-1.0%</td><td>-3.8%</td><td>0.0%</td><td></td></tr><tr><td>Palladium</td><td>983</td><td>1,151</td><td>1,706</td><td>1,408</td><td>1,300</td><td>1,390</td><td>1,451</td><td>1,478</td><td>1,570</td><td>1,296</td></tr><tr><td>% Change</td><td></td><td></td><td></td><td></td><td>0.0%</td><td>-4.1%</td><td>-1.0%</td><td>-3.7%</td><td>0.0%</td><td></td></tr></table>

Source : DB estimates; Figures are period averages. Q3 26 to 2028 are our forecasts. Price change in comparison to the "Precious Special Report" published on 22 June 2026.

## Outlook: Challenging external environment is not all bad

Figure 11: YTD price performance trends (US\$ basis)  
![](images/d6406c4c4594d83cd1b475d66b356290b868d0a7e03c58c5acbb2a5d7a3fb859.jpg)  
Source : DB, Bloomberg Finance LP

We update our assessment of the external environment for commodities here, along the dimensions we explored in January ("Structurally higher geopolitical risk"). These topics may influence commodity markets without necessarily being discussed in our individual commodity views: the geopolitical climate, the US dollar, investor positioning, and the macroeconomic picture.

(A) On geopolitics, DB's mid-year outlook sees an extension of geopolitical volatility in keeping with the idea that we have seen a structural shift. A continuation of an unpredictable and fragmented global operating environment finds expression in a number of ways.

On the US, we should expect more foreign policy volatility where incentives are increased for visible foreign policy wins. There is potential for renewed conflict in the Middle East, and difficult US-Iran negotiations are likely to extend beyond the initial 60-day period. A US-China détente does not negate the fact that the broader relationship will remain one of strategic competition, marred by mistrust and competing national security priorities. A fractured EU-US relationship means that Europe will face a possibility of renewed economic and trade clashes, and continued pressure to overcome internal divisions to build more strategic autonomy. For Ukraine, trilateral negotiations have stalled, but a winding down of the Middle East crisis could mean increased attention on a potential ceasefire and peace plan, along with possible easing of sanctions on Russia.

The most direct line of transmission to commodity markets may well be the global initiatives to build resilience in critical mineral supply, including both in diversification of the supply chain as well as stockpiling of reserves. In late 2025, the US signed agreements with Japan, Australia, Malaysia, Vietnam, Cambodia and Thailand. That momentum has built further with the US Project Vault (a critical minerals reserve), the US-EU Critical Minerals Plan, US-India Critical Minerals Framework, a European Critical Raw Minerals Centre, the Quad Critical Minerals Initiative Framework, and Australia's Critical Minerals Strategic Reserve all announced within the first half of this year.

(B) On the US dollar, we prefer not to chase recent dollar strength which reached 1y high on the Bloomberg spot dollar index. To its credit, the US is now expected to grow the most amongst G10 economies, and its 2y and 3m rate rankings amongst G10 economies are reasonably supportive. However, hawkish Fed repricing may not support a continued uptrend given that it has gone quite far in comparison to the US core CPI overshoot (Link). Additionally we have observed a very strong positioning move, with net long positioning similar to January 2025 when the DXY index level was some 6-7% stronger (Link). We see room for riskier currencies to rebound, although catalysts for broader dollar weakness inclusive of EUR and JPY are difficult to identify for now. Our forecasts have the USD moderately lower (-3.7%) on the Fed's trade-weighted broad dollar index by year-end.

Figure 12: USD implied net long positioning near 2025 high, with much lower level of DXY index  
![](images/20c664279e5a7c887956fee04c8d0cb2b6c78c9e63182630422e8ab2da907ab1.jpg)  
Source : CFTC, Bloomberg Finance LP, DB

Figure 13: Surveys show similarly high proportion of reserve managers intend to accumulate gold over next 12 months  
![](images/3f4569df16d905aba42d2a75fb9c9729ebcf39f2f6cda51ad2e1d899952cb4d0.jpg)  
Source : World Gold Council, OMFIF

(C) The third item is capital flows and investor positioning where we see a more obvious inclination to pursue a de-dollarisation agenda amongst reserve managers than private investors. In the OMFIF's Global Public Investor survey data, more reserve managers expressed a long-term (10y) intention to decrease (24%) than increase (16%) USD exposure, with a majority (60%) intending to maintain USD exposure.

On the other hand, private investor activity shows very little obvious divergence from past history, although such a judgment that it has diverged is difficult given that investment activity has turned negative for substantial periods and then reversed to positive. For example, public investors were net sellers of US Treasury bonds between 2015-2020, and private investors were sizeable net sellers of US equities in 2022 and 2024. In those instances, one could not necessarily have differentiated intentions between de-dollarisation and a view on the asset class, for instance. The difference now is that earlier this year, we have heard from major private investment entities that they would be pursuing diversification from US assets. Yet the aggregate data for both private and public investors does not clearly suggest anything of the sort.

Figure 14: Private investor net foreign investment in US assets (3m avg monthly rate, USD bn)  
![](images/32eb7bc06b3794ea3cfe63cb0f1d6365d00cceeb47d2ab75b13dd05

[中间内容因长度限制已省略]

ed performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
