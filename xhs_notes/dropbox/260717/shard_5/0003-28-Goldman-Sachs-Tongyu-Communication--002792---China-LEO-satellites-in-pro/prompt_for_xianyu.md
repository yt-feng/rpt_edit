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
# Tongyu Communication (002792.SZ): China LEO satellites in progress; 2Q26 NI midpoint guidance indicates narrowing losses vs. 1Q26; Buy

Tongyu reported its 2Q26 net income guidance (link), with the mid-point guidance at a loss of Rmb12m, narrowing from a loss of Rmb13m in 1Q26, though falling below our estimate of Rmb11m gains. Management highlighted that raw material price hikes, market competition, product mix changes, and FX impacts continue to weigh on 2Q26 earnings. Meanwhile, the company will maintain its R&D commitment to RFs for LEO satellites, ground stations, and user terminals, expanding its product lines from traditional RFs for telecom base stations to LEO satellites, so as to capitalize on strong market growth and RF specification upgrades. Management also highlighted that overseas revenues continued to see positive YoY growth in 1H26, reflecting a comprehensive market exposure that supports blended revenue growth through market cycles. With the build-out of China's LEO satellite constellations, we remain positive on Tongyu's growth outlook, considering its accumulated experience in LEO satellite phased array antennas, comprehensive product offerings, and early penetration into major LEO constellations' supply chains. Maintain Buy.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Yifan Hu
+852-2978-0996 | yifan.hu@gs.com
GS (Asia) L.L.C.

Exhibit 1: Tongyu's waterfall chart for 2025-30E Satellite networking equipment as key drivers ahead

![](images/a5b689c87e8849a6dee78ba804685720af325611ae7aa3adf668fd0ee0202f99.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 2: Tongyu's revenue and GM trends  
![](images/0af22f80c355edaac960514817478fdf9949df98327018fa0a859b80e8dac37e.jpg)  
Source: Company data, GS Global Investment Research

Global LEO satellite TAM: We updated our Global LEO satellite TAM in Jul (report link) and expect to see continuous growth in the satellite installed base from 10k units in 2025 to 13k/17k units by 2026E/27E (vs. our previous estimate of 12k/15k units). We project the installed base to reach 24k/305k units by 2028E/31E (vs. our previous estimate of 19k/42k units), with China's installed base increasing from 253 units in 2025 to 23,750 units in 2031E, reflecting our positive view on the development of China LEO satellite constellations. We view Tongyu as well-positioned in China's LEO satellite ecosystem, leveraging its accumulated experience in antennas to serve major LEO satellite constellations in the Chinese market, which should support the company's growth ahead.

Exhibit 3: We expect the LEO satellite installed base to reach 24k/305k units by 2028E/31E

<table><tr><td></td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td></tr><tr><td colspan="8">Satellite - new estimate</td></tr><tr><td>LEO Satellite installed base (units)</td><td>9,982</td><td>13,088</td><td>17,292</td><td>23,796</td><td>90,042</td><td>164,244</td><td>305,293</td></tr><tr><td>YoY%</td><td></td><td>31%</td><td>32%</td><td>38%</td><td>278%</td><td>82%</td><td>86%</td></tr><tr><td>Installed base by application (units)</td><td>9,982</td><td>13,088</td><td>17,292</td><td>23,796</td><td>90,042</td><td>164,244</td><td>305,293</td></tr><tr><td>Satellite internet</td><td>9,982</td><td>13,088</td><td>17,292</td><td>23,796</td><td>33,219</td><td>46,697</td><td>63,807</td></tr><tr><td>Space data center</td><td>-</td><td>-</td><td>-</td><td>-</td><td>56,823</td><td>117,547</td><td>241,486</td></tr><tr><td>Others</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Mix by application</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr><tr><td>Satellite internet</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>37%</td><td>28%</td><td>21%</td></tr><tr><td>Space data center</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>63%</td><td>72%</td><td>79%</td></tr><tr><td>Others</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Installed base by vendor region (units)</td><td>9,982</td><td>13,088</td><td>17,292</td><td>23,796</td><td>90,042</td><td>164,244</td><td>305,293</td></tr><tr><td>US</td><td>9,077</td><td>11,833</td><td>15,581</td><td>21,419</td><td>83,748</td><td>150,651</td><td>281,050</td></tr><tr><td>China</td><td>253</td><td>603</td><td>1,103</td><td>1,853</td><td>5,780</td><td>13,100</td><td>23,750</td></tr><tr><td>EU</td><td>652</td><td>652</td><td>608</td><td>524</td><td>514</td><td>493</td><td>493</td></tr><tr><td>Mix by vendor region</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr><tr><td>US</td><td>91%</td><td>90%</td><td>90%</td><td>90%</td><td>93%</td><td>92%</td><td>92%</td></tr><tr><td>China</td><td>3%</td><td>5%</td><td>6%</td><td>8%</td><td>6%</td><td>8%</td><td>8%</td></tr><tr><td>EU</td><td>7%</td><td>5%</td><td>4%</td><td>2%</td><td>1%</td><td>0%</td><td>0%</td></tr><tr><td>New vs. Old</td><td>3%</td><td>7%</td><td>16%</td><td>25%</td><td>252%</td><td>399%</td><td>634%</td></tr></table>

Source: Company data, GS Global Investment Research

Earnings revisions: We factor in Tongyu's 2Q26 net income guidance and revise down our 2026E net income by $11\%$ , mainly on lower GM. We cut our 2026E GM by 0.7ppts to reflect the GM YoY decline in 1H26, while still modeling a GM uptrend in the coming years, driven by rising contribution from LEO satellite components, which carry a higher GM than other product lines. Our 2027E-28E estimates are largely unchanged.

Exhibit 4: Earnings revisions

<table><tr><td rowspan="2">Rmb mn</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td></tr><tr><td>Revenue</td><td>1,454</td><td>1,451</td><td>0%</td><td>1,985</td><td>1,985</td><td>0%</td><td>3,767</td><td>3,767</td><td>0%</td></tr><tr><td>GP</td><td>297</td><td>285</td><td>-4%</td><td>435</td><td>435</td><td>0%</td><td>898</td><td>898</td><td>0%</td></tr><tr><td>OP</td><td>4</td><td>3</td><td>-23%</td><td>48</td><td>48</td><td>0%</td><td>194</td><td>194</td><td>0%</td></tr><tr><td>Net income</td><td>49</td><td>44</td><td>-11%</td><td>63</td><td>63</td><td>0%</td><td>155</td><td>155</td><td>0%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>GM</td><td>20.4%</td><td>19.7%</td><td></td><td>21.9%</td><td>21.9%</td><td></td><td>23.8%</td><td>23.8%</td><td></td></tr><tr><td>OPM</td><td>0.2%</td><td>0.2%</td><td></td><td>2.4%</td><td>2.4%</td><td></td><td>5.1%</td><td>5.1%</td><td></td></tr><tr><td>NM</td><td>3.4%</td><td>3.0%</td><td></td><td>3.2%</td><td>3.2%</td><td></td><td>4.1%</td><td>4.1%</td><td></td></tr></table>

Source: GS Global Investment Research

Valuation: We continue to derive our 12-month target price based on a discounted P/E methodology to capture the company's long-term growth, which is in line with our Greater China Technology coverage. Our unchanged 2030E target P/E multiple of 44.7x is derived from (1) peers' correlation between forward-year net income growth and trading P/E, and (2) Tongyu's 2030E-31E avg. net income YoY at 94%. We apply the 44.7x target P/E to 2030E EPS and discount it back to 2027E at a COE of 10.8%. Our 12m TP is unchanged at Rmb79. Maintain Buy.

Exhibit 5: Peers' correlation of forward-year NI YoY and trading P/E  
![](images/7d7b0cd97553ffbc193e3ebc918ea884366b54bf5de8d106decaa7afd19551d5.jpg)  
Data for not covered companies (Iridium, Fibocom) are Refinitiv Eikon consensus.

Exhibit 6: Tongyu's 12m forward P/E  
![](images/df252c4705a30d50e3e66fd536bc071575967878b8339234c8bfc77b1f7d7136.jpg)  
Source: Company data, GS Global Investment Research

Source: GS Global Investment Research, Refinitiv Eikon

<table><tr><td>2030E target P/E</td><td>44.7</td></tr><tr><td>Target multiple x EPS</td><td>107</td></tr><tr><td>Discounted back to 2027; TP (Rmb)</td><td>79.0</td></tr><tr><td>Implied 2027 P/E</td><td>659</td></tr><tr><td colspan="2">COE assumption</td></tr><tr><td>Beta</td><td>1.2</td></tr><tr><td>Risk free</td><td>3.0%</td></tr><tr><td>Market risk premium</td><td>6.5%</td></tr><tr><td>COE</td><td>10.8%</td></tr></table>

Exhibit 7: Tongyu's discounted P/E-based TP derivation

<table><tr><td>Rmb m</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td><td>2032E</td></tr><tr><td>Satellite network revenue</td><td></td><td></td><td>43</td><td>54</td><td>345</td><td>857</td><td>2,640</td><td>7,742</td><td>14,710</td><td></td><td></td></tr><tr><td>Revenue</td><td>1,407</td><td>1,294</td><td>1,194</td><td>1,110</td><td>1,451</td><td>1,985</td><td>3,767</td><td>9,286</td><td>16,583</td><td>24,875</td><td>31,094</td></tr><tr><td>YoY</td><td></td><td>-8%</td><td>-8%</td><td>-7%</td><td>31%</td><td>37%</td><td>90%</td><td>147%</td><td>79%</td><td>50%</td><td>25%</td></tr><tr><td>Gross profit</td><td>287</td><td>261</td><td>265</td><td>224</td><td>285</td><td>435</td><td>898</td><td>2,415</td><td>4,627</td><td>7,089</td><td>8,706</td></tr><tr><td>Gross margin</td><td>20.4%</td><td>20.2%</td><td>22.2%</td><td>20.2%</td><td>19.7%</td><td>21.9%</td><td>23.8%</td><td>26.0%</td><td>27.9%</td><td>28.5%</td><td>28.0%</td></tr><tr><td>OPEX</td><td>279</td><td>263</td><td>254</td><td>237</td><td>283</td><td>387</td><td>704</td><td>1,690</td><td>2,985</td><td>4,403</td><td>5,473</td></tr><tr><td>YoY</td><td></td><td>-6%</td><td>-4%</td><td>-6%</td><td>19%</td><td>37%</td><td>82%</td><td>140%</td><td>77%</td><td>47%</td><td>24%</td></tr><tr><td>Opex ratio</td><td>19.8%</td><td>20.3%</td><td>21.2%</td><td>21.4%</td><td>19.5%</td><td>19.5%</td><td>18.7%</td><td>18.2%</td><td>18.0%</td><td>17.7%</td><td>17.6%</td></tr><tr><td>Operating profit</td><td>8</td><td>-2</td><td>12</td><td>-13</td><td>3</td><td>48</td><td>194</td><td>725</td><td>1,642</td><td>2,687</td><td>3,234</td></tr><tr><td>YoY</td><td></td><td>na</td><td>na</td><td>na</td><td>na</td><td>1607%</td><td>306%</td><td>274%</td><td>126%</td><td>64%</td><td>20%</td></tr><tr><td>Operating margin</td><td>1%</td><td>0%</td><td>1%</td><td>-1%</td><td>0%</td><td>2%</td><td>5%</td><td>8%</td><td>10%</td><td>11%</td><td>10%</td></tr><tr><td>Pre-tax profit</td><td>79</td><td>92</td><td>38</td><td>53</td><td>56</td><td>82</td><td>204</td><td>735</td><td>1,649</td><td>2,694</td><td>3,241</td></tr><tr><td>Net profit</td><td>82</td><td>81</td><td>41</td><td>41</td><td>44</td><td>63</td><td>155</td><td>559</td><td>1,253</td><td>2,048</td><td>2,463</td></tr><tr><td>EPS (Rmb, diluted)</td><td>0.20</td><td>0.16</td><td>0.08</td><td>0.08</td><td>0.08</td><td>0.12</td><td>0.30</td><td>1.07</td><td>2.39</td><td>3.91</td><td>4.70</td></tr><tr><td>YoY</td><td></td><td>0%</td><td>-49%</td><td>-1%</td><td>6%</td><td>44%</td><td>147%</td><td>260%</td><td>124%</td><td>63%</td><td>20%</td></tr><tr><td>TP implied P/E</td><td>395</td><td>494</td><td>988</td><td>1,004</td><td>950</td><td>659</td><td>267</td><td>74</td><td>33</td><td>20</td><td>17</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: Our 12-month target price of Rmb79.0 is based on a 44.7x 2030E P/E, discounted back to 2027E at a COE of 10.8%. Our target multiple is derived from the correlation between consumer electronic peers' forward-year NI YoY and trading P/E.

Key downside risks: Slower-than-expected LEO satellite launches in China; Fiercer-than-expected market competition; Lower-than-expected base station end demand.

<table><tr><td>002792.SZ</td><td colspan="2">12m Price Target: Rmb79.00</td><td colspan="2">Price: Rmb28.63</td><td colspan="2">Upside: 175.9%</td></tr><tr><td>Buy</td><td></td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11">Market cap: Rmb15.0bn / $2.2bn Enterprise value: Rmb15.0bn / $2.2bn 3m ADTV: Rmb1.6bn / $239.5mn China Greater China Technology M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: Yes</td><td rowspan="11"></td><td>Revenue (Rmb mn) New</td><td>1,110.3</td><td>1,450.6</td><td>1,984.9</td><td>3,767.2</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>1,110.3</td><td>1,453.6</td><td>1,984.9</td><td>3,767.2</td></tr><tr><td>EBITDA (Rmb mn)</td><td>28.2</td><td>46.0</td><td>94.2</td><td>245.7</td></tr><tr><td>EPS (Rmb) New</td><td>0.08</td><td>0.08</td><td>0.12</td><td>0.30</td></tr><tr><td>EPS (Rmb) Old</td><td>0.08</td><td>0.09</td><td>0.12</td><td>0.30</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>NM</td><td>96.7</td></tr><tr><td>P/B (X)</td><td>3.2</td><td>5.2</td><td>5.1</td><td>4.9</td></tr><tr><td>Dividend yield (%)</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.2</td></tr><tr><td>CROCI (%)</td><td>(0.1)</td><td>3.1</td><td>4.0</td><td>7.9</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>(0.02)</td><td>(0.02)</td><td>0.06</td><td>0.07</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 15 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Yifan Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Yifan Hu GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses i

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
