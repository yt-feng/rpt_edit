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
# China & Japan Semiconductors

# Memory Interface Chip Primer: Riding on the agentic AI boom

![](images/2c2f6f7fb2ad290d5b9a324759d91ae82faf1c7b1194512a93747c9d2c4d924f.jpg)

![](images/85d6328afdee7dccc60dca14aae87dc3d385bec7049eae8d47a5627791a2766a.jpg)

Qingyuan Lin, Ph.D.
+852 2123 2654
qingyuan.lin@bernsteinsg.com

![](images/dc435f3a942a59879236e551087acb069ae6658a6ca00fe000ba8edcc94409cd.jpg)

![](images/8247c0f4d5df7fe3851d89b0d998967a9c561ef07bcbce52738e16c14afa8448.jpg)

+852 2918 5704
david.dai@bernsteinsg.com

![](images/cee8dcc7902a773005de066ab110b1f2ab0278c5be49b3eab4ef75bb34a428bb.jpg)

Francis Ma
+852 2123 2626
francis.ma@bernsteinsg.com

![](images/d8362b6cf491b929990b128b2a1db8d0ad03cb6eae8b92634d720e2e801fc810.jpg)

Kai Zhang
+852 2123 2665
kai.zhang@bernsteinsg.com

![](images/28a26b0048a8636c66df7ebe78d183f1fe603947dbafcf09ad7a4cc39ba85493.jpg)

Jack Lin
+852 2123 2683
jack.lin@bernsteinsg.com

+81 3 6777 6980

juho.hwang@bernsteinsg.com

Carmine Milano, CFA
+44 20 7762 1857
carmine.milano@bernsteinsg.com

We initiated coverage on Montage in April (initiation report and deck) where we discuss the opportunity for memory interface chip vendors driven by agentic AI. In this primer, we provide a comprehensive overview of the industry's growth drivers, competitive dynamics, and investment implications to help investors navigate the sector. Updated models can be downloaded here: Memory Interface Chip Industry Model and Montage Model. Reiterate Outperform on Montage, PT revised up from HKD 320 to 520 in H-share and CNY 220 to 400 in A-share. Reiterate Outperform on Renesas.

Memory interface chips are a direct and amplified beneficiary of the server CPU Renaissance driven by Agentic AI. As the industry shifts from GPU-centric training toward inference-heavy agentic AI deployments—where the CPU reclaims its role as orchestrator of multistep, sequential tasks—server CPU volumes are poised to grow structurally faster than expected (our CPU report), and the role of memory interface chip becomes increasingly important when the DRAM capacity and bandwidth per CPU grows. We project the global memory interface chips TAM to reach USD 20Bn by 2030 (3x of our previous projection) at 65% CAGR (vs 32%), driven by three reinforcing tailwinds: rising server CPU volume, increasing DRAM package count per CPU, and higher interface chip content per package through the MRDIMM upgrade.

MRDIMM penetration is an important driver, as interface chip value per MRDIMM module is roughly 10× that of RDIMM. Each MRDIMM adopts a "1 MRCD+10 MDB" architecture, versus just one RCD in standard DDR5 RDIMM. We project MRDIMM penetration to reach 25% (vs 20% previously) of global server DDR DIMM shipments by 2030, driven by the bandwidth improvement MRDIMM delivers. The adoption hurdle is manageable: MRDIMM premium is only about 10% of the current 128GB RDIMM price, and this gap narrows further as rising DRAM die prices reduce the premium.

The competitive landscape for core memory interface chips is a textbook oligopoly that drives high margin. Montage, Renesas, and Rambus (RMBS, not covered) collectively control 90%+ of global share, protected by rigorous JEDEC qualification cycles and deep co-development ties with DRAM IDMs and CPU platforms. The chip is crucial for the package performance but takes only LSD% of the package price, customers have very low incentive to shift to new vendors and are willing to offer high margin to secure the quality. The three vendors compete neck-and-neck on the RDIMM roadmap, while Renesas and Montage hold early-mover advantages in MRDIMM. The complementary supporting chips segment is more fragmented, where Renesas leads thanks to its analog heritage.

We favor all three leading suppliers, as market has not fully priced in upside from CPU acceleration and MRDIMM adoption. We raise Montage TP to CNY400/ HKD520 for A-/H-Share, supported by CPU-driven demand across both its memory interface and PCIe businesses, as well as share gains from CXMT expansion. Renesas's memory interface is at a scale similar to Montage's despite contributing only 6% of it revenue, yet its market cap is only 25% above Montage's; it appears significantly undervalued, and management's guidance for 20-30% growth CAGR for this business is too low. Rambus benefits across both interface chip products and memory controller IP royalties; its smaller revenue base and market cap give it the largest potential upside elasticity.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Cur</td><td rowspan="2">8 Jul 2026 Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>688008.CH (Montage)</td><td>O</td><td>CNY</td><td>247.15</td><td>400.00</td><td>169.8%</td><td>CNY</td><td>1.97</td><td>3.21</td><td>5.68</td><td>125.5</td><td>77.1</td><td>43.5</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>220.00</td><td></td><td></td><td></td><td>3.00</td><td>4.77</td><td></td><td></td><td></td></tr><tr><td>6809.HK (Montage)</td><td>O</td><td>HKD</td><td>321.40</td><td>520.00</td><td>NA</td><td>CNY</td><td>1.97</td><td>3.21</td><td>5.68</td><td>141.4</td><td>86.9</td><td>49.1</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>320.00</td><td></td><td></td><td></td><td>3.00</td><td>4.77</td><td></td><td></td><td></td></tr><tr><td>6723.JP (Renesas)</td><td>O</td><td>JPY</td><td>4,662.00</td><td>6,300.00</td><td>93.0%</td><td>JPY</td><td>181.61</td><td>244.76</td><td>298.54</td><td>25.7</td><td>19.0</td><td>15.6</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,945.70</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JPL</td><td></td><td></td><td>2,651.83</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD  
O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
6723.JP estimate is Adjusted EPS; 6723.JP valuation is Adjusted P/E (x);  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Since April the shares of Montage, Rambus, and Renesas have rallied for several months, reflecting strong investor interest in the memory interface chip sector as the CPU vendors comment on strong server CPU demand. Over the past month, however, their share prices have corrected 10–30% from peak levels as investors increasingly question whether valuations have become overstretched. We expect sentiment to remain weak in the near term, reflecting continued softness in memory-related sentiment, profit-taking following the strong share price rally, and concerns around weak near-term earnings due to substrate shortage for Montage and Rambus. From a tactical perspective, investors may prefer to remain on the sidelines for the near term. However, we expect that on a 12-month horizon, as the MRDIMM penetration continue to increase, when investor start to look into the potential upsides in 2028 then the stocks could work again, therefore long-onlys should look to buy the dip when the market corrects.

Montage Technology: We rate Montage Technology as Outperform and raise our A-share TP to CNY 400, based on 50x 2BF P/E (27Q3–28Q2 earnings). We believe a 2BF framework better reflects the upcoming earnings inflection driven by the 2027–2028 product cycle, including the ramp-up of MRDIMM interface chips, and the P/E is lower than the 5-year CAGR so should have more upside as well. We raise our 2027/2028 EPS estimates by 19%/73%, respectively, on a stronger outlook for the CPU cycle and better MRDIMM penetration. We also increase our target multiple from 44x to 50x, supported by the rapid growth of the ESP business (76.5% CAGR2025–28). For the H shares, we set a target price of HKD 520, implying a 15% premium to our A-share TP (we use the CNY to HKD exchange rate at 1:1.13). The H share premium reflects that global investors favor Montage as a scarce China AI-exposed name without direct geopolitical risks, unlike many other Chinese semiconductor companies that face entity list restrictions or export control headwinds. At our target price, the implied P/E multiple on 2BF EPS for H shares is 58x. H share has limited free float due to lock up, so we still expect H share premium to maintain at high level for the near term. After lock-up period, the H share premium could start to narrow again.

Renesas: We are constructive on AI data center semiconductors (refer to Artificial Intelligence - Energizing the Future of AI Data Centers and Global Semis: The CPU Renaissance? Beneficiaries of a \$223bn TAM). Within Renesas' AI infrastructure portfolio, we see both power semiconductors and memory interface ICs as attractive growth drivers. We forecast AI infrastructure revenue to account for 27% of Renesas' total revenue by 2028, vs. 11% in 2025 (refer to Infineon/Renesas: CPU renaissance emerges as a second engine for power semi demand, set to outstrip supply). We rate Renesas Outperform, with PT = ¥6,300.00.

EXHIBIT 1: Montage Bern. forecast vs. Consensus vs. Bern Old

<table><tr><td>Revenue (RMB mn)</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Bernstein</td><td>2,286</td><td>3,639</td><td>5,456</td><td>7,733</td><td>13,552</td><td>25,211</td><td>41,966</td><td>58,298</td></tr><tr><td>Growth YoY</td><td>(38%)</td><td>59%</td><td>50%</td><td>42%</td><td>75%</td><td>86%</td><td>66%</td><td>39%</td></tr><tr><td>Consensus</td><td>2,286</td><td>3,639</td><td>5,456</td><td>7,448</td><td>10,752</td><td>13,656</td><td></td><td></td></tr><tr><td>Growth YoY</td><td></td><td></td><td>50%</td><td>36%</td><td>44%</td><td>27%</td><td></td><td></td></tr><tr><td>Bernstein vs. consensus</td><td></td><td></td><td></td><td>3.8%</td><td>26.0%</td><td>84.6%</td><td></td><td></td></tr><tr><td>Bernstein old</td><td></td><td></td><td></td><td>7,793</td><td>11,688</td><td>14,941</td><td>20,420</td><td>25,508</td></tr><tr><td>New vs. Old</td><td></td><td></td><td></td><td>(0.8%)</td><td>16.0%</td><td>68.7%</td><td>105.5%</td><td>128.6%</td></tr><tr><td colspan="9">Gross profit</td></tr><tr><td>Bernstein</td><td>1,347</td><td>2,115</td><td>3,395</td><td>5,233</td><td>8,988</td><td>16,378</td><td>26,537</td><td>35,832</td></tr><tr><td>Growth YoY</td><td></td><td>57%</td><td>61%</td><td>54%</td><td>72%</td><td>82%</td><td>62%</td><td>35%</td></tr><tr><td>GP Margin</td><td>58.9%</td><td>58.1%</td><td>62.2%</td><td>67.7%</td><td>66.3%</td><td>65.0%</td><td>63.2%</td><td>61.5%</td></tr><tr><td>Consensus</td><td>1,347</td><td>2,115</td><td>3,395</td><td>5,264</td><td>7,817</td><td>9,969</td><td></td><td></td></tr><tr><td>Growth YoY</td><td></td><td>57%</td><td>61%</td><td>55%</td><td>48%</td><td>28%</td><td></td><td></td></tr><tr><td>GP Margin</td><td></td><td></td><td>62.2%</td><td>70.7%</td><td>72.7%</td><td>73.0%</td><td></td><td></td></tr><tr><td>Bernstein vs. consensus - GP</td><td></td><td></td><td></td><td>(0.6%)</td><td>15.0%</td><td>64.3%</td><td></td><td></td></tr><tr><td>Bernstein vs. consensus - GPM</td><td></td><td></td><td></td><td>(301bps)</td><td>(638bps)</td><td>(804bps)</td><td></td><td></td></tr><tr><td>Bernstein old</td><td></td><td></td><td></td><td>5,168</td><td>7,828</td><td>10,191</td><td>14,183</td><td>18,004</td></tr><tr><td>New vs. Old</td><td></td><td></td><td></td><td>1.3%</td><td>14.8%</td><td>60.7%</td><td>87.1%</td><td>99.0%</td></tr><tr><td colspan="9">Operating profit</td></tr><tr><td>Bernstein</td><td>199</td><td>1,046</td><td>1,971</td><td>3,531</td><td>6,943</td><td>13,962</td><td>23,681</td><td>32,491</td></tr><tr><td>Growth YoY</td><td></td><td>426%</td><td>88%</td><td>79%</td><td>97%</td><td>101%</td><td>70%</td><td>37%</td></tr><tr><td>OP Margin</td><td>8.7%</td><td>28.8%</td><td>36.1%</td><td>45.7%</td><td>51.2%</td><td>55.4%</td><td>56.4%</td><td>55.7%</td></tr><tr><td>Consensus</td><td>199</td><td>1,046</td><td>1,971</td><td>3,534</td><td>5,185</td><td>6,960</td><td></td><td></td></tr><tr><td>Growth YoY</td><td></td><td>426%</td><td>88%</td><td>79%</td><td>47%</td><td>34%</td><td></td><td></td></tr><tr><td>OP Margin</td><td></td><td></td><td>36.1%</td><td>47.5%</td><td>48.2%</td><td>51.0%</td><td></td><td></td></tr><tr><td>Bernstein vs. consensus - OP</td><td></td><td></td><td></td><td>(0.1%)</td><td>33.9%</td><td>100.6%</td><td></td><td></td></tr><tr><td>Bernstein vs. consensus - OPM</td><td></td><td></td><td></td><td>(179bps)</td><td>301bps</td><td>441bps</td><td></td><td></td></tr><tr><td>Bernstein old</td><td></td><td></td><td></td><td>3,517</td><td>5,868</td><td>7,931</td><td>11,576</td><td>15,010</td></tr><tr><td>New vs. Old</td><td></td><td></td><td></td><td>0.4%</td><td>18.3%</td><td>76.0%</td><td>104.6%</td><td>116.5%</td></tr><tr><td colspan="9">Net income attributable to shareholders</td></tr><tr><td>Bernstein</td><td>451</td><td>1,412</td><td>2,236</td><td>3,721</td><td>6,594</td><td>12,706</td><td>21,071</td><td>28,545</td></tr><tr><td>Growth YoY</td><td>(65%)</td><td>213%</td><td>58%</td><td>66%</td><td>77%</td><td>93%</td><td>66%</td><td>35%</td></tr><tr><td>NP Margin</td><td>19.7%</td><td>38.8%</td><td>41.0%</td><td>48.1%</td><td>48.7%</td><td>50.4%</td><td>50.2%</td><td>49.0%</td></tr><tr><td>Consensus</td><td>451</td><td>1,412</td><td>2,236</td><td>3,562</td><td>5,246</td><td>7,383</td><td></td><td></td></tr><tr><td>Growth YoY</td><td></td><td></td><td>58%</td><td>59%</td><td>47%</td><td>41%</td><td></td><td></td></tr><tr><td>NP Margin</td><td>19.7%</td><td>38.8%</td><td>41.0%</td><td>47.8%</td><td>48.8%</td><td>54.1%</td><td></td><td></td></tr><tr><td>Bernstein vs. consensus - NP</td><td></td><td></td><td></td><td>4.5%</td><td>25.7%</td><td>72.1%</td><td></td><td></td></tr><tr><td>Bernstein vs. consensus - NPM</td><td></td><td></td><td></td><td>30bps</td><td>(13bps)</td><td>(366bps)</td><td></td><td></td></tr><tr><td>Bernstein old</td><td></td><td></td><td></td><td>3,628</td><td>5,769</td><td>7,645</td><td>10,877</td><td>13,908</td></tr><tr><td>New vs. Old</td><td></td><td></td><td></td><td>3%</td><td>14%</td><td>66%</td><td>94%</td><td>105.2%</td></tr><tr><td colspan="9">Basic EPS</td></tr><tr><td>Bernstein</td><td></td><td>1.25</td><td>1.97</td><td>3.21</td><td>5.68</td><td>10.82</td><td>17.93</td><td>24.04</td></tr><tr><td>Growth YoY</td><td></td><td></td><td>58%</td><td>63%</td><td>77%</td><td>91%</td><td>66%</td><td>34%</td></tr><tr><td>Consensus</td><td></td><td>1.25</td><td>1.97</td><td>3.02</td><td>4.36</td><td>6.09</td><td></td><td></td></tr><tr><td>Growth YoY</td><td></td><td></td><td>58%</td><td>53%</td><td>44%</td><td>40%</td><td></td><td></td></tr><tr><td>Bernstein vs. consensus</td><td></td><td></td><td></td><td>6.2%</td><td>30.3%</td><td>77.8%</td><td></td><td></td></tr><tr><td>Bernstein old</td><td></td><td></td><td></td><td>3</td><td>5</td><td>6</td><td>9</td><td>11</td></tr><tr><td>New vs. Old</td><td></td><td></td><td></td><td>7%</td><td>19%</td><td>73%</td><td>102%</td><td>113.7%</td></tr></table>

Source: Bloomberg, Bernstein analysis and estimates

## Table Of Contents

Memory Interface Chip: Core beneficiary in the agentic AI era....4   
Product Primer: Memory module and memory interface chips....8   
CORE interface chips....9   
Complementary chips....12   
PC DDR module formats and CKD....13   
TAM sizing and analysis on growth drivers....15   
Increasing server CPU shipments....15   
Rising DIMM modules per CPU....17   
Higher memory interface chips value per module from MRDIMM migration....

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
