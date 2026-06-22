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

EXHIBIT 7: We believe the margin gap between HBM and conventional DRAM to narrow next year.  
![](images/367dd725719d2d153d13914bb473ee5c3d091687603b9849595ae2f636662c29.jpg)  
Source: Company reports, Bernstein estimates and analysis

S. Chungcheong Export N. Chungcheong Export + Icheon Export Other Provinces

EXHIBIT 8: Value per weight remained largely in the same range though the export value per weight for Samsung rose notably & suggested HBM4 shipment in May.  
Korea Multichip Memory Export Value per Weight to TW+MY  
![](images/922632d8aeb9df542292cefd167ecd4e29c7e565cff61bc963098dbd40d319d4.jpg)  
Source: Korea Custom Service, KITA and Bernstein analysis  
EXHIBIT 9: We see Samsung to gain share in HBM on better HBM4 performance & more capacity, but also see uncertainty as Samsung may choose to allocate more capacity to conventional DRAM for better profitability.  
HBM Market Share by Bit Shipment

![](images/1028801a221c3d29d885199f09d1cbe8ae706a68ffcbbb252eeb16ce405759f3.jpg)  
EXHIBIT 10: With the expected HBM price increase, we forecast HBM's revenue mix in DRAM to rebound next year.  
HBM Contribution to DRAM Revenue

![](images/d71acb1edc5fb116be6148ef77fb59f0ec22e7f2d6780b9630cc57615e46d144.jpg)  
Source: TrendForce, company reports, Bernstein estimates and analysis  
Source: TrendForce, Bernstein estimates and analysis

## DRAM stocks will benefit from a rapid upward earnings revision in the near term.

\- We believe negotiation of HBM supply for next year is still ongoing and we should hear more news on that in the coming months. And we also don't think this HBM price increase has been fully reflected in the sell-side consensus on Bloomberg. We will elaborate our model revision below, but we're above consensus in CY2027 meaningfully as we incorporate HBM price hike in this revision. We expect other sell-side forecasts to follow and hence a notable upward change to CY2027

consensus soon, which in turn support stock prices to move upward in the near term.

\- Please note this HBM revision will only benefit Samsung, SK hynix and Micron. Pure NAND suppliers, such as KIOXIA, do not have HBM and hence will not benefit from this revision.

## MediaTek may benefit if hyperscalers demand to source HBM directly to avoid the markup.

\- Though we expect NVIDIA & other AI accelerator suppliers to emphasize the importance of integrating HBM with the rest of their offerings and hence continuing having HBM as part of their revenue, many hyperscalers, we believe, will negotiate and try to source HBM directly to avoid the chance of HBM markup. We believe this trend to favor Asian ASIC service providers as their business model allows hyperscalers to do so now.

\- MediaTek thus can benefit from this trend. The execution on its first and second TPU project is also solid. Our recent supply chain checks also suggest an upside risk to our 2028 projection. The stock went 

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
