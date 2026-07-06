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
# Semiconductor Capital Equipment | North America

## Rolling over PTs to 2028

\$200bn of WFE in 2027 is well understood, and \$250bn in 2028 is starting to be priced in. We see opportunity in MKS and ONTO, where 2027 earnings power remains underappreciated. We are slightly less enthusiastic on the large caps.

What's Changed? We revise up our 2026 forecast from \$149bn (+27% y/y) to \$155bn (+32%), our 2027 forecast comes up from \$191bn (+28%) to \$202bn (+31%) and our 2028 forecast comes up from \$215bn (+13%) to \$227bn (+13%). The majority of our 2026-27 revisions are from our intra-quarter memory WFE revisions, and our 2028 revisions are driven by foundry logic.

$200$ bn in 2027 is priced in. Our large-cap US SPE coverage now trades at 37x our CY27 forecasts, which have been adjusted to reflect our updated WFE outlook. That 37x multiple represents a 75% premium to the 21x through-cycle average at which these stocks have traded since 2020, and a 20%+ premium to the most recent peak of 30x in July 2024. We think $200$ bn of WFE in 2027 is well understood by the market and are therefore shifting our valuation base year to 2028. Based on our $227$ bn WFE forecast for 2028, our large-cap coverage now trades at 33x, implying that $250$ bn of WFE in 2028 may already be close to priced in.

$250bn+$ in 2028 is possible, but we are not ready to underwrite it. Over the past two weeks, 2028 WFE expectations have increased significantly, but we question both the legitimacy of pricing in such upside during 2026 and the feasibility of a $250bn$ WFE environment. We are not doubting the possibility of $250bn+$ , but the key questions we are asking ourselves are: 1) Memory: Can the market digest $80bn+/30bn+$ of DRAM/NAND WFE, which would imply bit supply growth north of 40%? 2) EUV: Can ASML supply the approximately 130 tools required? 3) Logic: Are we willing to underwrite a meaningful contribution ( $10bn+$ ) from the likes of TeraFab and Rapidus? We are continuing to work through these questions, but without greater comfort, we are not yet ready to reflect $250bn+$ in our models.

We revise up target multiples for KLA and AMAT, as we see the broadening of leading-edge customers benefiting KLA, while the strength of DRAM WFE in CY26 should benefit AMAT. Given that we have yet to see NAND WFE revisions, we leave target multiples for LAM and MKS unchanged. We revise down multiples for NVMI and CAMT, as we have questions around whether NVMI can outgrow WFE in 2027 and have market share concerns in HBM for CAMT (see Exhibit 3 for details).

Across our US SPE coverage, our preference is for companies whose earnings power on \$200bn of WFE in 2027 remains underappreciated. Specifically, we think Top Pick MKS and OW-rated ONTO present substantial upside from undemanding valuations on 2027 earnings. We remain OW on KLA and LAM, but our enthusiasm toward both names is slightly more muted, as we think expectations for \$250bn+ of WFE in 2027 are already partially priced in.

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Shane Brett</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Shane.Brett@morganstanley.com</td><td>+1 212 761-1022</td></tr><tr><td colspan="2">Joseph Moore</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joseph.Moore@morganstanley.com</td><td>+1 212 761-7516</td></tr><tr><td colspan="2">Mason Wayne</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Mason.Wayne@morganstanley.com</td><td>+1 212 761-6012</td></tr><tr><td colspan="2">Ella Tulchinsky</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ella.Tulchinsky@morganstanley.com</td><td>+1 212 761-2222</td></tr><tr><td colspan="2">Nicole Kozhukhov</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Nicole.Kozhukhov@morganstanley.com</td><td>+1 212 761-1636</td></tr></table>

<table><tr><td colspan="3">SEMICONDUCTOR CAPITAL EQUIPMENT</td></tr><tr><td>North AmericaIndustry View</td><td></td><td>In-Line</td></tr><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Camtek (CAMT.O)Price Target</td><td>From$163.00</td><td>To$167.00</td></tr><tr><td>KLA Corp (KLAC.O)Price Target</td><td>From$190.00</td><td>To$274.00</td></tr><tr><td>Lam Research Corp (LRCX.O)Price Target</td><td>From$331.00</td><td>To$404.00</td></tr><tr><td>MKS Inc. (MKSI.O)Price Target</td><td>From$374.00</td><td>To$442.00</td></tr><tr><td>Nova Ltd (NVMI.O)Price Target</td><td>From$494.00</td><td>To$540.00</td></tr><tr><td>Applied Materials Inc.(AMAT.O)Price Target</td><td>From$502.00</td><td>To$647.00</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

## WFE Forecast Table

Exhibit 1:

<table><tr><td>($mn)</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td></tr><tr><td>WFE Revenue</td><td>91,092</td><td>96,222</td><td>96,008</td><td>105,057</td><td>117,048</td><td>154,638</td><td>201,887</td><td>227,269</td></tr><tr><td>Semi Revenue</td><td>553,540</td><td>573,978</td><td>526,820</td><td>630,549</td><td>791,061</td><td>1,607,055</td><td>1,959,883</td><td>1,959,883</td></tr><tr><td>Semi Capex</td><td>157,788</td><td>187,982</td><td>176,924</td><td>198,540</td><td>215,972</td><td>305,309</td><td>357,665</td><td>351,202</td></tr><tr><td colspan="9">Y/Y Change %</td></tr><tr><td>WFE Revenue</td><td>43%</td><td>6%</td><td>0%</td><td>9%</td><td>11%</td><td>32%</td><td>31%</td><td>13%</td></tr><tr><td>Semi Revenue</td><td>26%</td><td>4%</td><td>-8%</td><td>20%</td><td>25%</td><td>103%</td><td>22%</td><td>0%</td></tr><tr><td>Semi Capex</td><td>33%</td><td>19%</td><td>-6%</td><td>12%</td><td>9%</td><td>41%</td><td>17%</td><td>-2%</td></tr><tr><td colspan="9">Metrics</td></tr><tr><td>WFE Intensity</td><td>16%</td><td>17%</td><td>18%</td><td>17%</td><td>15%</td><td>10%</td><td>10%</td><td>12%</td></tr><tr><td>WFE% of Total Capex</td><td>58%</td><td>51%</td><td>54%</td><td>53%</td><td>54%</td><td>51%</td><td>56%</td><td>65%</td></tr><tr><td>Semi Capital Intensity</td><td>29%</td><td>33%</td><td>34%</td><td>31%</td><td>27%</td><td>19%</td><td>18%</td><td>18%</td></tr><tr><td colspan="9">3rd Party Sources</td></tr><tr><td>Semi</td><td>87,499</td><td>94,100</td><td>95,610</td><td>104,270</td><td>115,700</td><td>126,100</td><td>135,200</td><td></td></tr><tr><td>Gartner</td><td>92,843</td><td>101,101</td><td>102,820</td><td>111,777</td><td>124,452</td><td>144,886</td><td>161,086</td><td>154,674</td></tr><tr><td colspan="9">WFE by segment</td></tr><tr><td>Foundry/Logic</td><td>50,265</td><td>59,180</td><td>70,023</td><td>69,192</td><td>75,307</td><td>89,479</td><td>114,491</td><td>133,729</td></tr><tr><td>Memory</td><td>39,828</td><td>35,854</td><td>24,794</td><td>35,228</td><td>41,118</td><td>64,261</td><td>86,438</td><td>92,215</td></tr><tr><td>DRAM</td><td>20,664</td><td>18,256</td><td>19,579</td><td>29,244</td><td>31,083</td><td>48,621</td><td>62,430</td><td>64,108</td></tr><tr><td>NAND</td><td>19,164</td><td>17,598</td><td>5,215</td><td>5,985</td><td>10,035</td><td>15,640</td><td>24,009</td><td>28,107</td></tr><tr><td>Other</td><td>999</td><td>1,188</td><td>1,192</td><td>637</td><td>622</td><td>898</td><td>957</td><td>1,324</td></tr><tr><td colspan="9">Y/Y Change %</td></tr><tr><td>Foundry/Logic</td><td>45%</td><td>18%</td><td>18%</td><td>-1%</td><td>9%</td><td>19%</td><td>28%</td><td>17%</td></tr><tr><td>Memory</td><td>42%</td><td>-10%</td><td>-31%</td><td>42%</td><td>17%</td><td>56%</td><td>35%</td><td>7%</td></tr><tr><td>DRAM</td><td>53%</td><td>-12%</td><td>7%</td><td>49%</td><td>6%</td><td>56%</td><td>28%</td><td>3%</td></tr><tr><td>NAND</td><td>31%</td><td>-8%</td><td>-70%</td><td>15%</td><td>68%</td><td>56%</td><td>54%</td><td>17%</td></tr><tr><td>Other</td><td>19%</td><td>19%</td><td>0%</td><td>-47%</td><td>-2%</td><td>44%</td><td>7%</td><td>38%</td></tr><tr><td colspan="9">% of Total</td></tr><tr><td>Foundry/Logic</td><td>55%</td><td>62%</td><td>73%</td><td>66%</td><td>64%</td><td>58%</td><td>57%</td><td>59%</td></tr><tr><td>Memory</td><td>44%</td><td>37%</td><td>26%</td><td>34%</td><td>35%</td><td>42%</td><td>43%</td><td>41%</td></tr><tr><td>DRAM</td><td>23%</td><td>19%</td><td>20%</td><td>28%</td><td>27%</td><td>31%</td><td>31%</td><td>28%</td></tr><tr><td>NAND</td><td>21%</td><td>18%</td><td>5%</td><td>6%</td><td>9%</td><td>10%</td><td>12%</td><td>12%</td></tr><tr><td>Other</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>0%</td><td>1%</td></tr><tr><td colspan="9">WFE Intensity</td></tr><tr><td>Semi ex-Memory revenue</td><td>399,706</td><td>444,153</td><td>434,511</td><td>465,032</td><td>568,550</td><td>727,417</td><td>835,151</td><td>835,151</td></tr><tr><td>Memory revenue</td><td>153,834</td><td>129,825</td><td>92,309</td><td>165,516</td><td>222,512</td><td>879,638</td><td>1,124,732</td><td>1,124,732</td></tr><tr><td>DRAM</td><td>92,960</td><td>77,769</td><td>51,945</td><td>94,860</td><td>150,598</td><td>581,901</td><td>675,059</td><td>675,059</td></tr><tr><td>NAND</td><td>55,953</td><td>47,109</td><td>36,104</td><td>66,427</td><td>67,685</td><td>293,508</td><td>445,443</td><td>445,443</td></tr><tr><td colspan="9">WFE Intensity</td></tr><tr><td>Foundry Logic</td><td>13%</td><td>13%</td><td>16%</td><td>15%</td><td>13%</td><td>12%</td><td>14%</td><td>16%</td></tr><tr><td>Memory</td><td>26%</td><td>28%</td><td>27%</td><td>21%</td><td>18%</td><td>7%</td><td>8%</td><td>8%</td></tr><tr><td>DRAM</td><td>22%</td><td>23%</td><td>38%</td><td>31%</td><td>21%</td><td>8%</td><td>9%</td><td>9%</td></tr><tr><td>NAND</td><td>34%</td><td>37%</td><td>14%</td><td>9%</td><td>15%</td><td>5%</td><td>5%</td><td>6%</td></tr><tr><td colspan="9">% of Memory WFE</td></tr><tr><td>DRAM</td><td>52%</td><td>51%</td><td>79%</td><td>83%</td><td>76%</td><td>76%</td><td>72%</td><td>70%</td></tr><tr><td>NAND</td><td>48%</td><td>49%</td><td>21%</td><td>17%</td><td>24%</td><td>24%</td><td>28%</td><td>30%</td></tr></table>

Source: Gartner, SEMI, Company data, MS. e = MS estimates

Exhibit 2:

<table><tr><td>($mn)</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td></tr><tr><td colspan="9">WFE by Region</td></tr><tr><td>Total</td><td>91,092</td><td>96,222</td><td>96,008</td><td>105,057</td><td>117,048</td><td>154,638</td><td>201,887</td><td>227,269</td></tr><tr><td>North America</td><td>7,755</td><td>10,239</td><td>11,346</td><td>13,657</td><td>10,534</td><td>12,680</td><td>16,555</td><td>18,636</td></tr><tr><td>Europe</td><td>2,879</td><td>5,982</td><td>5,741</td><td>4,202</td><td>2,341</td><td>2,629</td><td>3,028</td><td>3,409</td></tr><tr><td>Japan</td><td>6,879</td><td>7,244</td><td>6,438</td><td>7,354</td><td>8,779</td><td>10,825</td><td>14,536</td><td>16,591</td></tr><tr><td>Korea</td><td>22,757</td><td>19,655</td><td>18,965</td><td>18,910</td><td>23,410</td><td>35,567</td><td>48,453</td><td>52,954</td></tr><tr><td>Taiwan</td><td>23,566</td><td>26,566</td><td>19,501</td><td>15,233</td><td>27,506</td><td>40,515</td><td>56,528</td><td>63,635</td></tr><tr><td>China</td><td>24,695</td><td>22,105</td><td>31,682</td><td>42,548</td><td>41,552</td><td>48,711</td><td>57,941</td><td>68,181</td></tr><tr><td>Other</td><td>2,561</td><td>4,431</td><td>2,334</td><td>3,152</td><td>2,926</td><td>3,711</td><td>4,845</td><td>3,864</td></tr><tr><td colspan="9">WFE by Region (Y/Y)</td></tr><tr><td>North America</td><td>28%</td><td>32%</td><td>11%</td><td>20%</td><td>-23%</td><td>20%</td><td>31%</td><td>13%</td></tr><tr><td>Europe</td><td>8%</td><td>108%</td><td>-4%</td><td>-27%</td><td>-44%</td><td>12%</td><td>15%</td><td>13%</td></tr><tr><td>Japan</td><td>14%</td><td>5%</td><td>-11%</td><td>14%</td><td>19%</td><td>23%</td><td>34%</td><td>14%</td></tr><tr><td>Korea</td><td>51%</td><td>-14%</td><td>-4%</td><td>0%</td><td>24%</td><td>52%</td><td>36%</td><td>9%</td></tr><tr><td>Taiwan</td><td>54%</td><td>13%</td><td>-27%</td><td>-22%</td><td>81%</td><td>47%</td><td>40%</td><td>13%</td></tr><tr><td>China</td><td>48%</td><td>-10%</td><td>43%</td><td>34%</td><td>-2%</td><td>17%</td><td>19%</td><td>18%</td></tr><tr><td>Other</td><td>40%</td><td>73%</td><td>-47%</td><td>35%</td><td>-7%</td><td>27%</td><td>31%</td><td>-20%</td></tr><tr><td colspan="9">WFE by Region (% of Total)</td></tr><tr><td>North America</td><td>9%</td><td>11%</td><td>12%</td><td>13%</td><td>9%</td><td>8%</td><td>8%</td><td>8%</td></tr><tr><td>Europe</td><td>3%</td><td>6%</td><td>6%</td><td>4%</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td></tr><tr><td>Japan</td><td>8%</td><td>8%</td><td>7%</td><td>7%</td><td>8%</td><td>7%</td><td>7%</td><td>7%</td></tr><tr><td>Korea</td><td>25%</td><td>20%</td><td>20%</td><td>18%</td><td>20%</td><td>23%</td><td>24%</td><td>23%</td></tr><tr><td>Taiwan</td><td>26%</td><td>28%</td><td>20%</td><td>15%</td><td>24%</td><td>26%</td><td>28%</td><td>28%</td></tr><tr><td>China</td><td>27%</td><td>23%</td><td>33%</td><td>41%</td><td>36%</td><td>32%</td><td>29%</td><td>30%</td></tr><tr><td>Other</td><td>3%</td><td>5%</td><td>2%</td><td>3%</td><td>3%</td><td>2%</td><td>2%</td><td>2%</td></tr></table>

Source: Gartner, SEMI, Company data, MS. e = MS estimates

Exhibit 3: Multiple revision rationale

<table><tr><td></td><td>Old PT</td><td>New PT</td><td>Old Multiple (CY27)</td><td>New Multiple (CY28)</td><td>Multiple revision rationale</td></tr><tr><td>KLA</td><td>$190</td><td>$274</td><td>33x</td><td>38x</td><td>Broadening of leading edge logic customers (Intel, Rapidus, TeraFab)</td></tr><tr><td>AMAT</td><td>$502</td><td>$647</td><td>28x</td><td>30x</td><td>DRAM WFE far stronger than anticipated in CY26</td></tr><tr><td>LAM</td><td>$331</td><td>$404</td><td>34x</td><td>34x</td><td rowspan="2">Waiting for NAND WFE revisions to reward multiple expansion</td></tr><tr><td>MKS</td><td>$374</td><td>$442</td><td>22x</td><td>22x</td></tr><tr><td>NVMI</td><td>$494</td><td>$540</td><td>36x</td><td>33x</td><td>Questions around outgrowth vs WFE in 2027</td></tr><tr><td>CAMT</td><td>$163</td><td>$167</td><td>32x</td><td>27x</td><td>Market share worries in HBM vs ONTO/KLA</td></tr></table>

Source: MS

## How do we think about SPE valuation?

Our guiding principle for US SPE coverage valuation is that multiples are closer aligned to gross margin rather than growth rates. Gross margin is reflective of the “value” equipment companies provide to customers, which in the case of process tools is throughput while for inspection it would be yield. Gross margin for SPE doesn’t materially vary y/y given these companies aren’t rewarded/punished for where we are in the cycle. Gross margin expansion comes from operational improvement or providing customers with more value, rather than opportunistically increasing pricing.

Exhibit 4: US SPE CY28 P/E vs CY26-28 EPS CAGR  
![](images/4bdf2b9bed5da0be193557b38662c96167b7e34ed2d95f1689e8c3d4482e82b7.jpg)  
Source: FactSet, MS. e = MS estimates

Exhibit 5: US SPE CY28 P/E vs CY27 Gross Margin (%)  
![](images/f693f8d996b730660426ae96491a3b30a94e3ba36b7bdf07a18df1f369ac6650.jpg)  
Source: FactSet, MS. e = MS estimates

Our large cap US SPE coverage now trades at 37x CY27, a 20%+ premium to the most recent peak of 30x in Jul. 2024 when the market was increasingly looking towards \$125bn of WFE in 2025. Based on our \$227bn WFE in 2028, our large caps now trade at 33x, implying that \$250bn in 2028 may be close to being priced in.

Exhibit 6: AMAT/LAM/KLA FwdPE vs 20

[中间内容因长度限制已省略]

sons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Semiconductor Capital Equipment

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/02/2026)</td></tr><tr><td colspan="3">Shane Brett</td></tr><tr><td>Applied Materials Inc. (AMAT.O)</td><td>E (05/18/2026)</td><td>$603.04</td></tr><tr><td>Camtek (CAMT.O)</td><td>E (12/01/2025)</td><td>$142.50</td></tr><tr><td>KLA Corp (KLAC.O)</td><td>O (01/15/2026)</td><td>$235.55</td></tr><tr><td>Lam Research Corp (LRCX.O)</td><td>O (05/18/2026)</td><td>$351.41</td></tr><tr><td>MKS Inc. (MKSI.O)</td><td>O (08/04/2024)</td><td>$365.56</td></tr><tr><td>Nova Ltd (NVMI.O)</td><td>E (12/01/2025)</td><td>$470.14</td></tr><tr><td>ONTO Innovation Inc (ONTO.N)</td><td>O (06/14/2026)</td><td>$307.58</td></tr><tr><td>Teradyne Inc (TER.O)</td><td>E (07/30/2025)</td><td>$369.09</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
