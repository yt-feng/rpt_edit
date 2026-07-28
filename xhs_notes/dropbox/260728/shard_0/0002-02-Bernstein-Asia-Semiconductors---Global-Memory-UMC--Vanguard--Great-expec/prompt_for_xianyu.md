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
# Asia Semiconductors & Global Memory

# UMC, Vanguard: Great expectations but on false assumptions?

![](images/41a660caff3806596e943ef463647d379a2331361fe3c7b004f3da87713a2cb0.jpg)

Mark Li

+852 2123 2645

mark.li@bernsteinsg.com

![](images/d69e3b421045a596c75c8346680352b80384cd6b5b07496f2ac6fb8b35302101.jpg)

Yipin Cai, CFA

+852 2123 2669

yipin.cai@bernsteinsg.com

![](images/a63ef9387ba2ca746b842884e175dbc03594fc047ef8ee5fed7ed97f8fd4066f.jpg)

Edward Hou, CFA

+852 2123 2623

edward.hou@bernsteinsg.com

UMC and Vanguard have rallied by c. 150% & 65%, respectively, YTD on the thesis of price increase & spillover demand from TSMC (Exhibit 1). Expectations are great, but we find on false assumptions.

"We are increasing our mature node capacity", said TSMC. We believe TSMC is indeed phasing out its two oldest fabs (Fab 2 (6") & Fab 5 (8)), but even if the demand all moves to UMC & Vanguard, it'd represent only 8-13% of their combined 6" & 8" capacity, or 4-6% of their total capacity (Exhibit 2). Moreover, in the most recent earnings call, TSMC confirmed it is expanding mature-node capacity in Japan & Europe. The demand spilled over from TSMC, if any, is hardly meaningful.

Raising prices in 2027 amid high memory cost? UMC & Vanguard successfully raised prices this year & some expect more to come, citing hikes from other foundries. Chinese foundries benefit from localization & PSMC (6770 TT, not covered) sold a fab to Micron. With their fabs fully utilized for a while, their price hikes are well-supported, but these factors don't apply to UMC & Vanguard. More importantly, “the mature node demand … is not that strong”, said TSMC and we further worry the demand will be eventually hurt by high memory costs.

Between UMC & Vanguard, we find Vanguard relatively better. TSMC indicated mature-node demand is sluggish, but power management IC & CMOS image sensor are exceptions. With over 75% of its revenue from power management (Exhibit 11), Vanguard is thus relatively better positioned than UMC. Strong CoWoS demand results in strong interposer demand for TSMC, & TSMC outsourcing some of the interposers to Vanguard will help Vanguard bring its new VSMC 12" fab sooner to profitability.

Silicon photonics may be good for UMC but too early to price it in. Though UMC announced to produce PIC (photonic IC) for SILITH not long ago, with tech licensing from imec happening just late last year, we think it can take years for UMC to gain traction meaningfully enough to move the needle for the company. Tower Semiconductor (TSEM US, not covered) saw its silicon photonic revenue increase 3x YoY in 1Q26 and has secured contracts for US\$1.3B revenue in 2027. To support that, Tower is expanding capacity with US\$920M capex but we've not seen UMC's capex for this yet.

3nm will allow UMC to differentiate from Chinese rivals technologically, but without any experience & customer base on 7nm & 5nm, we don't see what UMC can bring to the collaboration. The capex burden is heavy if UMC wants to share the burden from Intel. And as Intel's 3nm has been nearly entirely used internally, it will take great efforts to make it "foundry-friendly". Hence discussion between them is likely but unlikely to materialize into a joint project & financial benefit to UMC.

We updated our models on UMC, Vanguard & Novatek and reiterate Underperform on UMC and Market-Perform on Vanguard & Novatek.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">27 Jul 2026</td><td colspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">P/B (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Target</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>2330.TT (TSMC)</td><td>O</td><td>TWD</td><td>2,350.00</td><td>2,780.00</td><td>78.1%</td><td>TWD</td><td>66.25</td><td>101.62</td><td>124.63</td><td>11.2</td><td>8.3</td><td>6.4</td><td></td></tr><tr><td>TSM (TSMC)</td><td>O</td><td>USD</td><td>403.41</td><td>430.00</td><td>47.8%</td><td>USD</td><td>10.48</td><td>16.07</td><td>19.70</td><td>12.2</td><td>9.0</td><td>6.9</td><td></td></tr><tr><td>2303.TT (UMC)</td><td>U</td><td>TWD</td><td>126.00</td><td>88.00</td><td>162.5%</td><td>TWD</td><td>3.34</td><td>4.58</td><td>5.56</td><td>4.2</td><td>3.8</td><td>3.5</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>47.00</td><td></td><td></td><td></td><td>3.31</td><td>3.85</td><td></td><td></td><td></td><td></td></tr><tr><td>UMC (UMC)</td><td>U</td><td>USD</td><td>19.48</td><td>13.60</td><td>150.4%</td><td>USD</td><td>0.54</td><td>0.74</td><td>0.89</td><td>4.2</td><td>3.6</td><td>3.4</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>7.40</td><td></td><td></td><td></td><td>0.53</td><td>0.62</td><td></td><td></td><td></td><td></td></tr><tr><td>5347.TT (Vanguard)</td><td>M</td><td>TWD</td><td>157.00</td><td>146.00</td><td>37.2%</td><td>TWD</td><td>4.30</td><td>5.70</td><td>6.59</td><td>4.6</td><td>4.3</td><td>4.1</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>94.00</td><td></td><td></td><td></td><td>4.34</td><td>4.44</td><td></td><td></td><td></td><td></td></tr><tr><td>3034.TT (Novatek)</td><td>M</td><td>TWD</td><td>518.00</td><td>480.00</td><td>(22.3)%</td><td>TWD</td><td>26.87</td><td>30.43</td><td>32.54</td><td>19.3</td><td>17.0</td><td>15.9</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>370.00</td><td></td><td></td><td></td><td>24.21</td><td>25.10</td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,880.30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,411.98</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

3034.TT valuation is Reported P/E (x);

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

TSMC: We rate TSMC Outperform with PT=NT\$ 2,780.00

Novatek: We rate Novatek Market-Perform with PT raised to NT\$ 480.00 from NT\$370.00 based on the same 14x target P/E and revised up Q5-Q8 EPS due to better growth in SoC segment.

UMC: We rate UMC Underperform with PT revised up to NT\$ 88.00 from NT\$47.00. We revised up our target P/B to 2.5x from 1.5x as we forecast its ROE to stay in the range of 15-20% going forward, higher vs. the pre-cycle average of below MSD%. We also revised up Q5-Q8 BVPS mainly on higher ASP assumption.

Vanguard: We rate Vanguard Market-Perform with PT raised to NT\$ 146.00 from NT\$94.00 based on revised up 4x target P/B from 3x and revised up Q5-Q8 BVPS mainly on higher visibility for VSMC and better utilization.

## DETAILS

EXHIBIT 1: UMC & Vanguard rallied 148% & 67%, respectively, YTD. on the thesis of price increase & spillover demand from TSMC.

![](images/26314a5c940b3eb5efd17bca72551b85ead985051a92d9c9d4afe3f42437945a.jpg)  
Source: Bernstein analysis  
EXHIBIT 2: TSMC's Fab 2&5 would represent only 8-13% of combined non-12" capacity and 4-6% of total capacity of UMC and Vanguard.

TSMC's Fab 2 &5 Capacity vs. UMC and Vanguard Current Capacity  
![](images/17c80b0d7136092f7e08e0aaedfab49e209a2d6b3bf7d6920cc96a187667c3b0.jpg)  
Source: SEMI, Bernstein estimates and analysis

## Even after the recent correction, UMC is traded at a peak valuation. We reiterate Underperform.

\- The stock rallied by c. 150% YTD mainly on the expectation of mature node price hike and spillover demand from TSMC. Speculation on extended collaboration with Intel and CPO business also make some investors interested in the stock. Our channel checks however suggest the price hike thus far is only c. HSD% (High Single-Digit %) in 2H26, but that however is insufficient to justify such a rally. We also don't think the Intel collaboration is likely to take place as UMC does not have any technology or customer base to offer. Silicon photonics may be a market addressable for UMC's mature-node capacity, but it will take years to materialize even if UMC succeeds. The stock is still traded at 3.8x forward P/B even after the recent pullback, still higher than the peak valuation in 2022 when COVID resulted in an unprecedented supply shortage & hence unprecedented price hikes for UMC (Exhibit 3).

\- We revised up our ASP assumption for 2026 (Exhibit 4) to reflect the recent price hike & now forecast $3.4\%$ and $6.5\%$ QoQ price increase in 3Q26 and 4Q26, respectively. We also lifted the utilization rate (Exhibit 5) slightly to reflect marginally better supply/demand dynamics for mature nodes. As a result, we forecast UMC's revenue to grow by $16\%$ in 2026 and $15\%$ in 2027, and GM & OPM also on a rising trajectory (Exhibit 6) thanks to better mix (i.e. higher contribution from 22nm). This supports an ROE expansion from $14\%$ to $18\%$ from 2026 to 2028, but that is still a lot lower vs. the ROE of $28\%$ during COVID (Exhibit 7 - Exhibit 8).

\- Our projection is below consensus likely because we assume heavier depreciation across 2026-2028 (Exhibit 10). We also assume the price of 8" mature nodes will eventually drop due to competitive pressure from China in the long term. We raise our target P/B to 2.5x from 1.5x on better ROE in the medium term & historical correlation between P/B & ROE (Exhibit 9), and lift our TP to NT\$88.00 from NT\$47.00. This implies 31% potential downside as of July 24 market close. Dividend yield could provide c. 2% return. Maintain Underperform.

EXHIBIT 3: UMC is still trading above the P/B peak in COVID even after recent correction. We believe it's overvalued.  
![](images/5a258fedfce83d88a3c959e9e7ada43f76b3b04c70f9b8124ad1cee2b95f724d.jpg)  
Source: Bloomberg and Bernstein analysis

EXHIBIT 4: We revised up ASP estimates for 2026 to reflect the successful price hike in 2H26. On a longer run, we believe mature node ASP is still under competitive pressure from China.  
![](images/a0049cba5b483af5950ade21c089a891fc9569316780df860ab7fd57dd3fcdf0.jpg)  
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 5: We also lifted the utilization rate to reflect marginally better supply/demand dynamics for mature nodes.  
![](images/dcfc37db6536f7b883bcc4b1b914af90b44feb1c11efc18f2f057bc3ae976fed.jpg)  
Source: Company report, Bernstein estimates and analysis  
EXHIBIT 6: GM & OPM will be on a growth trajectory thanks to a better mix (i.e. higher contribution from 22nm) & higher utilization rate.

![](images/d5ae4e7b86ff9bb973a5d5cb4bcbfa157e05b48f4e3fa32def31951c0f0a4d19.jpg)  
Source: Company report, Bernstein estimates and analysis

EXHIBIT 7: We forecast UMC's revenue to grow by $16\%$ in 2026 and $15\%$ in 2027 driven by higher ASP and utilization rate.  
![](images/9202884e73f4cff4763254736173c89668e395f14fbd6f87e135e2526b7bb2e8.jpg)  
Source: Company report, Bernstein estimates and analysis

EXHIBIT 8: We model ROE to improve gradually & stay higher vs. pre-COVID level thanks to higher profit margin, but still shy of the COVID level.  
![](images/4fae63c092bea0c20e94637ca7082206783aab5b7ccdeebb04759da58882ac44.jpg)  
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 9: Based on the historical correlation between P/B and ROE and our projected 2026-2028 ROE, we assign a 2.5x target P/B multiple for UMC.  
![](images/a5d43b541e9f7e78373aa9f7c65fd78f074cc6331034e4bd25d3feb52f25c31d.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 10: Our estimates are below consensus likely because we assume heavier depreciation across 2026-2028. We also assume the strong pricing of mature nodes will eventually drop due to competitive pressure in the long-term.

<table><tr><td rowspan="3">UMC</td><td colspan="5">2026E</td><td colspan="5">2027E</td><td colspan="3">2028E</td></tr><tr><td colspan="5">Bernstein</td><td colspan="5">Bernstein</td><td colspan="3">Bernstein</td></tr><tr><td>New</td><td>Old</td><td>% Chg</td><td>Consensus</td><td>% Diff</td><td>New</td><td>Old</td><td>% Chg</td><td>Consensus</td><td>% Diff</td><td>New</td><td>Consensus</td><td>% Diff</td></tr><tr><td>Revenue (NT$ B)</td><td>274.8</td><td>251.9</td><td>9.1%</td><td>275.3</td><td>-0.2%</td><td>315.9</td><td>267.4</td><td>18.1%</td><td>323.8</td><td>-2.4%</td><td>333.4</td><td>378.0</td><td>-11.8%</td></tr><tr><td>YoY</td><td>15.7%</td><td>6.0%</td><td></td><td>16.8%</td><td></td><td>14.9%</td><td>6.2%</td><td></td><td>17.6%</td><td></td><td>5.6%</td><td>16.7%</td><td></td></tr><tr><td>Gross Margin</td><td>31.5%</td><td>27.8%</td><td>3.7%</td><td>31.5%</td><td>0.0%</td><td>33.2%</td><td>28.7%</td><td>4.4%</td><td>34.6%</td><td>-1.4%</td><td>36.7%</td><td>38.0%</td><td>-1.3%</td></tr><tr><td>Operating Margin</td><td>21.1%</td><td>17.1%</td><td>4.0%</td><td>21.1%</td><td>0.0%</td><td>23.1%</td><td>18.5%</td><td>4.6%</td><td>24.8%</td><td>-1.7%</td><td>26.5%</td><td>27.7%</td><td>-1.3%</td></tr><tr><td>EPS (NT$)</td><td>4.58</td><td>3.31</td><td>38.4%</td><td>4.62</td><td>-0.8%</td><td>5.56</td><td>3.85</td><td>44.6%</td><td>5.74</td><td>-3.1%</td><td>6.62</td><td>7.82</td><td>-15.4%</td></tr><tr><td>YoY</td><td>37.2%</td><td>-0.9%</td><td></td><td>37.1%</td><td></td><td>21.4%</td><td>16.2%</td><td></td><td>24.3%</td><td></td><td>19.0%</td><td>36.2%</td><td></td></tr></table>

Source: Company reports, Bloomberg, Bernstein estimates and analysis

## We maintain Market-Perform on Vanguard on its relatively better position, but see a new-term downside risk.

\- Vanguard's stock price rose by c. 65% YTD on similar thesis as UMC's, but we believe Vanguard is relatively better positioned because of its large revenue exposure to power management product (Exhibit 11). The incremental interposer order from TSMC also improves the demand visibility for the Singapore 12-inch fab (VSMC). Its phase 1 capacity (now capped at 44KWPM, lowered from 55KWPM) is now fully secured by demand committed in LTAs. The fab successfully produced its first 40nm wafers in June & is on track for mass production in 1Q27. Given strong customer demand, the management is evaluating the feasibility of a phase 2.

\- We revised up our utilization assumptions for VSMC and the strong AI power management IC demand for 0.18um node. We also lifted our ASP forecasts to reflect the above-average price of interposer, as well as the price adjustments on 8" mature nodes. Additionally, we modeled a lighter depreciation burden in outer years as TSMC bring its own equipment for interposer production. As a result, our EPS is revised up notably. We're now roughly in line with consensus on revenue across 2026-2028 but slightly below consensus on net earnings, mainly due to heavier opex assumptions (Exhibit 12 - Exhibit 15, Exhibit 18).

\- We raise our target P/B to 4x from 3x on better visibility of VSMC and improved price outlook of 8" power management products. And with the revised Q5-Q8 BVPS, we increase our price target to NT\$146.00/share, implying 7% downside as of July 24 market close. Dividend yield will add c. 3% return. Maintain Market-Perform (Exhibit 16 - Exhibit 17).

EXHIBIT 11: Vanguard has over 75% revenue exposure to Power Management products and thus relatively better-positioned, in our view.  
Vanguard Revenue Breakdown by Platform  
![](images/f49c6ab8a0ccd04174b0467f680677e5cd7b7a7dcd9e7d2f1f12216bab865dab.jpg)  
Source: Company reports and Bernstein analysis

EXHIBIT 12: We assumed a faster ramp up for the 12" new capacity at VSMC as interpose business from TSMC improves demand visibility.  
![](images/9df8df9830504e6a4a5b594d6f98c1938522729cb238a5445de2105ebf9c9fd0.jpg)  
Source: Com

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
