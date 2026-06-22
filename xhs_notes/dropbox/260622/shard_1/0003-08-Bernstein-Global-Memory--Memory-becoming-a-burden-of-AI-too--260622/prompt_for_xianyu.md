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
Global Memory

# Global Memory: Memory becoming a burden of AI too?

![](images/1c0e7d1a56221f7185b4d113d8f2aa4a5bb24c8cc12672258bab6f69b0848817.jpg)

Mark Li

+852 2123 2645

mark.li@bernsteinsg.com

![](images/63f8ba3708791cd6e89cc85b08a4c36e797cabbfb4d064a3f582c59badbce52f.jpg)

Edward Hou, CFA

+852 2123 2623

edward.hou@bernsteinsg.com

![](images/d4faa4905d176b39519e8a85f565f0124814f2214145521fea4304b58d15fcbd.jpg)

Yipin Cai, CFA

+852 2123 2669

yipin.cai@bernsteinsg.com

We update our memory & industry models (models for HBM, DRAM, NAND, Samsung, SK hynix, Micron & KIOXIA) & maintain Outperform ratings on Samsung, SK hynix & Micron & Underperform on KIOXIA.

HBM price needs to go higher to narrow the profitability gap vs. conventional DRAM. From 3QCY25 to 2QCY26, conventional DRAM price has risen c. 4.5x, but HBM price is locked by annual contracts and hasn't moved. As the result, we estimate in CY26 deploying capacity to conventional DRAM will generate over 2x revenue & nearly 3x gross profit dollar per wafer capacity vs. HBM. This is why memory suppliers and GPU/XPU companies are negotiating CY27 HBM price now to narrow the gap.

The possible “markup” of GPU/XPU suppliers will amplify the cost burden on hyperscalers. Unlike conventional DRAM & NAND that hyperscalers can source directly from memory suppliers, HBM is packaged in GPUs/XPUs and is part of the COGS of, for example, NVIDIA. NVIDIA needs to mark up the HBM price hike 4x if NVIDIA has 75% gross margin & wants to keep 75% unchanged, despite the HBM price hike. This will make the HBM price hike even a heavier burden for hyperscalers.

inevitable and may squeeze weaker suppliers. Using Vera Rubin (VR, NVL72) rack as an example, hyperscalers will find their capex higher by 30% if they deploy a data center with this rack and with the same memory capacity installed in the rack, because of higher conventional DRAM & NAND cost, higher HBM cost & the markup charged by NVIDIA. With funding availability and competitive pressure, we think hyperscalers will still invest in AI, but may try to “re-calibrate” their costs across different component suppliers (& possibly even token prices across different customers too?).

To reflect higher HBM price, a notable earnings revision is coming to support the stock prices of Samsung, SK hynix Micron but not KIOXIA. We raise HBM price 2-2.5x, not as much as the size of conventional DRAM price hike, as we assume memory suppliers recognize the strategic value of HBM and choose to price less aggressively. We update our forecast & find our FY27 EPS 25-40% above consensus as the result. As HBM negotiation gradually concludes in the next few months, we expect consensus to move upward and to provide an upward support to the stock of Samsung, SK hynix and Micron, but not KIOXIA as KIOXIA has only NAND & does not have HBM. Please note this also means higher HBM exposure will result lower profitability for memory suppliers.

MediaTek may benefit if hyperscalers prefer to source HBM directly to avoid the possible markup. The stock went up c. 130% in the past 2 months but we reiterate Outperform.

Reiterate Outperform on Samsung, SK hynix and Micron too. We raise target price to KRW440,000 for Samsung (6.2x 1-year forward P/E), KRW3,300,00 for SK hynix (6.2x 1-year forward P/E), and US\$1,300 for Micron (7.7x 1-year forward P/E). Maintain Underperform on KIOXIA (see KIOXIA: All parties come to an end - Underperform).

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">19 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>005930.KS (SEC- Samsung)</td><td>O</td><td>KRW</td><td>350,500</td><td>440,000</td><td>442.0%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td>53.0</td><td>7.2</td><td>4.5</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>225,000</td><td></td><td></td><td></td><td>35,740</td><td>49,548</td><td></td><td></td><td></td></tr><tr><td>005935.KS (SEC-Pref - Samsung)</td><td>O</td><td>KRW</td><td>222,000</td><td>374,000</td><td>308.8%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td>33.6</td><td>4.6</td><td>2.9</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>191,250</td><td></td><td></td><td></td><td>35,740</td><td>49,548</td><td></td><td></td><td></td></tr><tr><td>SMSN.LI (Samsung)</td><td>O</td><td>USD</td><td>5,710.00</td><td>7,350.00</td><td>387.0%</td><td>USD</td><td>116.15</td><td>812.39</td><td>1,290.80</td><td>49.2</td><td>7.0</td><td>4.4</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>3,888.00</td><td></td><td></td><td></td><td>617.62</td><td>856.24</td><td></td><td></td><td></td></tr><tr><td>000660.KS (SK hynix)</td><td>O</td><td>KRW</td><td>2,755,000</td><td>3,300,000</td><td>925.0%</td><td>KRW</td><td>60,341</td><td>395,677</td><td>568,862</td><td>45.7</td><td>7.0</td><td>4.8</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>1,150,000</td><td></td><td></td><td></td><td>286,732</td><td>385,594</td><td></td><td></td><td></td></tr><tr><td>MU (Micron)</td><td>O</td><td>USD</td><td>1,133.99</td><td>1,300.00</td><td>805.2%</td><td>USD</td><td>8.29</td><td>67.39</td><td>158.99</td><td>136.9</td><td>16.8</td><td>7.1</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>510.00</td><td></td><td></td><td></td><td>62.53</td><td>121.03</td><td></td><td></td><td></td></tr><tr><td>285A.JP (KIOXIA)</td><td>U</td><td>JPY</td><td>108,600</td><td>40,000</td><td>4607.8%</td><td>JPY</td><td>1,014.00</td><td>10,013</td><td>9,656.84</td><td>107.1</td><td>10.8</td><td>11.2</td></tr><tr><td>2454.TT (MediaTek)</td><td>O</td><td>TWD</td><td>4,390.00</td><td>4,380.00</td><td>204.2%</td><td>TWD</td><td>66.17</td><td>69.52</td><td>170.50</td><td>66.3</td><td>63.1</td><td>25.7</td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,048.07</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EM</td><td></td><td></td><td>1,898.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,500.58</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended MU estimate is Adjusted EPS; MU valuation is Adjusted P/E (x);
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Samsung, SK hynix, Micron: We maintain Outperform on Samsung, SK hynix and Micron and raise price targets to KRW440,000 (vs 225,000), KRW3,300,000 (vs 1,150,000) and US\$1,300 (vs 510) respectively, driven by increased forecasts of conventional memory pricing as well as HBM pricing going forward. We now value them using 1-year forward P/E and target 6.2x for Samsung, 6.2x for SK hynix and 7.7x for Micron.

## DETAILS

Please feel free to download our industry (DRAM, NAND, CoWoW/HBM) and company models (Samsung, SK hynix, Micron & KIOXIA).

We think HBM price will be higher. And added with the "markup" on HBM, the increase will make AI feel the burden of memory price hike too. A "re-calibration" to share the cost burden is probably inevitable.

\- As a result of the DRAM supply shortage, and skyrocketing conventional DRAM prices, we think HBM price is also bound to go up next year, by 2-2.5x vs this year (Exhibit 1 - Exhibit 2), and will exert a heavy pressure on server rack cost and also hyperscaler capex. The cost pressure possibly won't be limited to just the higher purchase cost of HBM stacks paid to memory suppliers. Take NVIDIA as an example. HBM is packaged inside NVIDIA's GPUs, and the HBM cost paid memory suppliers is part of NVIDIA's COGS. Simply passing through this HBM cost increase to NVIDIA's customers will dilute NVIDIA's gross margin. Assume NVIDIA earns $75\%$ gross margin on the VR200 racks, NVIDIA will need to increase its rack price by 4x the cost increase of HBM in order to maintain margin at $75\%$ .

\- We estimate before the HBM price increase HBM was 5% of VR200 price that NVIDIA charges. With the HBM price increase alone, the selling price of VR200 needs to be higher by 6% price increase. If NVIDIA marks up by 4x to keep gross margin at 75%, the rack price can go up by 24%. For a hyperscaler deploying VR200 racks, its total data center capex (including out-of-rack capex) needs to go up by 4% if only HBM cost is passed on, or 15% if all markup is included. Additionally, conventional DRAM and NAND prices have both gone up substantially too, and contribute another 14% increase to the total data center capex (Exhibit 3). All together with 2-2.5x HBM price increase+markup, and conventional DRAM & NAND price increase (& no markup), we find hyperscalers' AI capex needs to be higher by 30% just to cover higher memory costs. Should they build their ROI analysis based on the original budget of VR200, they likely now need to redo the analysis with "I" (investment) 30% higher than original.

\- In summary, the burden of memory price hike is now propagating from consumer applications to AI too. Hyperscalers need to redo their ROI analysis, as memory is now making the investment requirement bigger. Given the competitive pressure and funding availability, we don't think this will make hyperscalers slow down AI investments. A "re-calibration" is however inevitable, so that hyperscalers, supply chain & maybe even token price together make adjustments to cope with the burden. Weaker suppliers may be squeezed in this "re-calibration" but companies in our coverage are well positioned and some may emerge as a beneficiary of this "re-calibration".

\- Please note that the analysis here isn't perfect and the estimate is simply a ballpark one. First it is very possible that hyperscalers will mix VR200 servers with those with other accelerators and/or with CPUs only for different computation and agentic needs. Further some conventional DRAM and NAND will be pre-installed in the servers shipped by NVIDIA and hence may be subject to markups. The analysis above however for simplistic sake assumes no markups - essentially assuming NVIDIA allows customers to weigh trier computation needs against memory cost and all conventional DRAM & NAND are installed by customers. Finally, GPU & accelerator providers may argue the existence of the markups on HBM. They will highlight HBM being an integral part of the entire system, and the integration of HBM with logic dies, package, and other components in the rack & software. They may hence argue that they charge no markups on HBM, & treat HBM just as “pass-through” revenue but deserve high margin on the rest of the system. In any case, it is true the HBM is part of the COGS of these GPUs/accelerators and the gross margin % of these GPU/accelerators suppliers will contract if they simply pass the higher HBM cost downward without a markup. They will be tempted to charge a markup if they would like to defend the gross margin %, but that as discussed above resulting in an amplified capex burden on hyperscalers.

EXHIBIT 1: We forecast 2-2.5x increase in HBM prices YoY next year so that the profitability of HBM & conventional DRAM can narrow.  
![](images/10a867b952d639b0901f65b239eb90e729c25dda3ae97b0206f848f2b22997a6.jpg)  
Source: Company reports, TrendForce, Bernstein estimates and analysis

EXHIBIT 2: We expect the price increase to take place at all generations of HBM.  
![](images/b867b6460bc3ab2634c5c1da5858016af74db281881d192fd8467a56caff4aa7.jpg)  
Source: Company reports, TrendForce, Bernstein estimates and analysis

EXHIBIT 3: We estimate HBM price increase, its cost markup, and also DRAM & NAND price increase together require nearly 30% increase in AI data center capex.  
![](images/d90bb316c7162dccf7aa367273e9ddd0e2c668b6274a24440ceeaab6c0635ef9.jpg)  
Source: Expert conversations, company reports, TrendForce, Bernstein estiates and analysis

The profitability of HBM may stay below that of conventional memory next year should suppliers recognize the strategic value of HBM and price HBM less aggressively.

\- Conventional DRAM price is expected to have moved up by \~4.5x by 2QCY26 compared to 3QCY25, and we think prices can possibly rise by another turn in CY27 (or another \~25% from 2QCY26) before peaking (Exhibit 4-Exhibit 5). As a result of that, conventional DRAM now enjoys similar if not higher ASP per bit than HBM. And given its higher bit density and yield, conventional DRAM, we estimate, will generate 2x revenue per wafer capacity vs. HBM this year (Exhibit 6), and command a notably higher margins too (Exhibit 7). Both Samsung and Micron clearly said non-HBM DRAM margin was already ahead of HBM margin in their 1QCY26 earnings calls, as conventional DRAM price keeps climbing, the margin gap between the two keeps widening.

\- Given conventional DRAM price may rise further next year, we think memory suppliers will demand a significant increase in HBM prices to balance the profitability between the two. Samsung in its earnings call also mentioned that it expects the margin differential to be “significantly reduced in 2027”, implying raising HBM prices. We estimate 3x increase in HBM price is needed for HBM revenue per wafer capacity to catch up with conventional DRAM. Some, on the other hand, may argue HBM is a vital part of AI and is critical to the entire AI infrastructure build out. We think suppliers may recognize this and understand that high HBM cost can be unhealthy for overall AI ecosystem development and ultimately to memory demand as well. SK hynix indeed also stressed that it will try to achieve “optimal allocation between HBM and general DRAM”, and will not try to maximize revenue. We hence model 2-2.5x increase in HBM price next year on account of the above considerations (Exhibit 1-Exhibit 2). HBM profitability hence will remain below that of conventional DRAM next year, but the gap should be much smaller than this year.

\- Across different HBM suppliers, Samsung we believe now leads in HBM4 technology. Our latest Korea memory export tracker (report link) did find a meaningful increase in export value per weight from Samsung in May, which can be due to HBM4 starting shipment (Exhibit 8). We think this can enable Samsung to grow its HBM market share this year and next year (Exhibit 9-Exhibit 10). However, as mentioned above, more HBM exposure may likely mean less profit for memory suppliers. And we do get the impression that Samsung is more focused on achieving higher profit margins, and hence may choose to deploy more capacity for conventional memory, even with Samsung's technological lead in HBM4.

EXHIBIT 4: Conventional DRAM price has gone up by 4.5x and we see another 25% increase before reaching the peak.  
Conventional DRAM ASP (US\$/Gb)  
![](images/bf43aaf5b9ebbe10cb4e4e254e3e735d0a650269ddeac7b19030950520594928.jpg)  
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 5: We forecast DRAM price to continue rising after 2QCY26 though at a slower rate and reach peak in CY27.  
![](images/1fc844bfd3be3ae67e207e2665224dea4d038b5c8ce3c9aa68763dcf3ce480df.jpg)  
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 6: Conventional DRAM now generates considerably more revenue per wafer capacity than HBM, and we project an HBM price hike next year to narrow that gap.  
![](images/4003822fe58fa1b71396307a32fa245c99f1517dde13f68f2f51d3130249bc12.jpg)  
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 7: We believe the margin gap be

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
