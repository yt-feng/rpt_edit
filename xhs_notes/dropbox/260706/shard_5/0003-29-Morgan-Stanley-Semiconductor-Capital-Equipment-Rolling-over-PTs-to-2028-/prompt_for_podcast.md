你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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

Exhibit 6: AMAT/LAM/KLA FwdPE vs 2020- average  
![](images/a6baed6bd08ede043afdc95d0735b5289530f0209fd3a66071171583d54029c8.jpg)  
Source: FactSet, MS. Note: average since Jan 2020

Exhibit 7: AMAT/LAM/KLA FwdPE & Premium vs S&P  
![](images/cf18f19d685d0cb29b1d436417e35a3b19dfcb20e9aae222732648ecfbd67ee8.jpg)  
Source: FactSet, MS.

## Risk Reward – Applied Materials Inc. (AMAT.O)

DRAM/Leading Logic upside & China/ICAPS derisked

## PRICE TARGET \$647.00

\~30x CY28e EPS of \$21.55, a 4-turn discount to LAM and 8-turns to KLA to reflect growth prospects in DRAM but concerns around market share loss in foundry logic.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/215e3d1a261c48e204ff4a696277acd0be5e9f91a8ae44b42a2c39a6642221e3.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/5f204c934c17d1dacf95d699a880e6b5e43f8a952ecce560149087a870b764d2.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 2 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## EQUAL-WEIGHT THESIS

■ AMAT has traded at a material valuation discount vs LAM & KLA given execution and concerns around market share loss in China. We think AMAT will be a share gainer in 2026 but given our growth forecast is in-line with broader WFE in 2027 we think the valuation discount is unlikely to narrow in the near term.

■ AMAT has the highest DRAM mix in their portfolio (CY26 31% vs LAM 23%, KLA 28%) and is most levered to greenfield wafer additions. We see DRAM as the fastest growing end-market in 2026 but the slowest growing in 2027.

![](images/66aa19747a1909738ba410d5cce40b337363a9b004de21f3c69527394d59a523.jpg)

## Risk Reward Themes

New Data Era: Positive
View descriptions of Risk Rewards Themes here

## BULL CASE

\$854.00

## \~35x CY28 EPS of \$24.41

DRAM & ICAPS remain strong and AMAT's margin expansion accelerates.

\- Revenue grows 24.6% in CY28 as AMAT outperforms WFE

\- Gross margin expands to 51.9% in CY27

\- Multiples expand to 35x PE, as equipment is perceived as a growth sector within semis

## BASE CASE

## \$647.00 BEAR CASE

## \~30x CY27 EPS of \$21.55

AMAT grows in-line 

[中间内容因长度限制已省略]

ponsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

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
