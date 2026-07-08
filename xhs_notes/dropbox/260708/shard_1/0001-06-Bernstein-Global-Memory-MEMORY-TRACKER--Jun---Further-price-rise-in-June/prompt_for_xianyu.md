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

# MEMORY TRACKER (Jun): Further price rise in June, but with the pace of the rise moderating into 3QCY26

![](images/6e2486ca8451bb50fd82b6564361996c10df3f5be16614b172bdca89f92bd35b.jpg)

![](images/2f09a8b44d489136bc184623c5b84001ce6f57f79241daa80f712b254b54f84d.jpg)

![](images/5eb1ee030c554598d4d6ddbfe4ef4623c7f40b26db7e83020626e0c0b0303e03.jpg)

![](images/7b63227377f69232d544bb1f6e05f501de9dd14c0b869eb33cb3adfca77bc9f3.jpg)

Mark Li
+852 2123 2645
mark.li@bernsteinsg.com

![](images/f04e501f8c2ac8b38cbe66ae1f6799f9431cb3c94b8bdc3e3ff1f56c3630c382.jpg)

Mark C. Newman
+1 212 845 7822
mark.newman@bernsteinsg.com

Edward Hou, CFA
+852 2123 2623
edward.hou@bernsteinsg.com

Yipin Cai, CFA
+852 2123 2669
yipin.cai@bernsteinsg.com

April Li
+1 917 344 8339
april.li@bernsteinsg.com

![](images/490fac49113700ddbae8d5b058fe3eec15c57a24ec71ad75cd3c3953ea8a9c20.jpg)

Phoebe Sun
+1 917 344 8481
phoebe.sun@bernsteinsg.com

This monthly tracker (download dataset here) summarizes contract/spot price data released by TrendForce/DRAMeXchange & compares that with our model & investor expectation.

DRAM: June contract price rose further MoM & indicated 74% QoQ increase for conventional DRAM contract price in 2QCY26.

Spot price: DRAM spot price further increased in June following the recovery in May. PC DRAM spot price rebounded by 5.6-11.5% MoM while server DRAM was up 6.1-26.4% MoM. Notably, spot price of Server DDR5 was particularly strong in the past month, but we expect the volume is too small to move the needle.

Contract price: DRAM contract prices in June rose further vs. May & indicated 2QCY26 price to be 74% higher than 1QCY26, with 49% for PC, 67% for Server, \~80% for Mobile & \~85% for Consumer. Notably, price increase is still expected to decelerate into 3QCY26. On LTA, suppliers have mostly concluded the negotiations with US CSPs. TrendForce observed that the price ceiling of LTA may be higher for other suppliers, but for Micron may be near its 2QCY26 level, as Micron prefers longer contract durations. Discussion with Chinese CSPs will continue into 3QCY26.

NAND: Wafer contract price was only slightly higher MoM, but the overall 2QCY26 NAND price increase will be supported by SSD and mobile NAND.

Spot price: Unlike DRAM spot price, NAND wafer spot price further dropped by 3-4% in June after a stable May though wafer is a small portion of the NAND market.

Contract price: Wafer contract price was up only 0.3-3.7% MoM, but the overall 2QCY26 NAND contract price is still expected to rise by \~60% vs. 1QCY26, thanks to c. 70-80% price increase in Mobile NAND & SSD, & c. 24-29% increase for wafer. Similar to DRAM price, NAND price is also expected to continue rising but at a narrower pace into 3QCY26.

In summary, both DRAM & NAND contract prices rose mildly MoM and still indicated a major price increase for 2QCY26. Server demand continued to absorb incremental supply allocated by suppliers, while demand destruction in consumer segment has been more limited than feared due to pulled-forward purchases. Spot price also appeared to be stabilizing. Nevertheless, we still believe demand destruction in consumer segment will eventually happen & the pace of the price increase should narrow notably into 3QCY26. LTAs can reduce the impact of a correction, and we expect more clarity on these LTAs as more are signed. We model memory prices to gradually peak & begin to normalize from 2HCY27 and into CY28. See Global Memory: Memory becoming a burden of AI too? and Memory: What do New Memory LTAs mean for sustainability of earnings and multiples? Raising SNDK TP to \$3000 for details.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Cur</td><td colspan="3">7 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>ClosingPrice</td><td>PriceTarget</td><td>PriceTarget</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>005930.KS (SEC- Samsung)</td><td>O</td><td>KRW</td><td>291,000</td><td>440,000</td><td>338.6%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td></td><td>44.0</td><td>6.0</td><td>3.8</td></tr><tr><td>005935.KS (SEC-Pref - Samsung)</td><td>O</td><td>KRW</td><td>199,300</td><td>374,000</td><td>251.7%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td></td><td>30.1</td><td>4.1</td><td>2.6</td></tr><tr><td>SMSN.LI (Samsung)</td><td>O</td><td>USD</td><td>4,714.00</td><td>7,350.00</td><td>286.4%</td><td>USD</td><td>116.15</td><td>812.39</td><td>1,290.80</td><td></td><td>40.6</td><td>5.8</td><td>3.7</td></tr><tr><td>000660.KS (SK hynix)</td><td>O</td><td>KRW</td><td>2,167,000</td><td>3,300,000</td><td>633.1%</td><td>KRW</td><td>60,341</td><td>395,677</td><td>568,862</td><td></td><td>35.9</td><td>5.5</td><td>3.8</td></tr><tr><td>MU (Micron)</td><td>O</td><td>USD</td><td>938.38</td><td>1,300.00</td><td>662.1%</td><td>USD</td><td>8.29</td><td>67.39</td><td>158.99</td><td></td><td>113.2</td><td>13.9</td><td>5.9</td></tr><tr><td>285A.JP (KIOXIA)</td><td>U</td><td>JPY</td><td>72,400</td><td>40,000</td><td>2699.5%</td><td>JPY</td><td>1,014.00</td><td>10,013</td><td>9,656.84</td><td></td><td>71.4</td><td>7.2</td><td>7.5</td></tr><tr><td>SNDK (SanDisk)</td><td>O</td><td>USD</td><td>1,617.70</td><td>3,000.00</td><td>3457.0%</td><td>USD</td><td>2.99</td><td>65.43</td><td>243.73</td><td></td><td>541.0</td><td>24.7</td><td>6.6</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,945.70</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EM</td><td></td><td></td><td>1,806.44</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,503.85</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
MU, SNDK estimate is Adjusted EPS; MU, SNDK valuation is Adjusted P/E (x);

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Samsung Electronics: We rate Samsung Electronics Outperform with price target of KRW 440,000.

SK hynix : We rate SK hynix Outperform with price target of KRW 3,300,000.

Micron: We rate Micron Outperform with price target of US\$1,300.00.

KIOXIA: We rate KIOXIA Underperform with price target of JPY 40,000.

SanDisk: We rate SNDK Outperform with a price target of \$3,000.00

## DETAILS

TrendForce (who publishes research on memory market & also maintains DRAMeXchange for memory spot market) has released the Jun 2026 contract prices for DRAM & NAND covering different applications (dataset can be downloaded at Memory Price Tracker). We select mainstream products from each segment, apply different weights on them to derive an industry average price change. SSD & HBM are not in the samples but will be additionally considered so that we can compare the overall ASP with our projection. Spot price is noisy but we also summarize some spot price data as it can be a leading indicator of contract price. Please feel free to find our most recent market review and download our industry and company models from the links below.

• CoWoS/HBM Model

• DRAM Industry Model

• NAND Industry Model

• Samsung Electronics Model

\- SK hynix Model

\- Micron Model

\- KIOXIA Model

\- SanDisk Model

June contract price rose further from May and suggested in 2QCY26 conventional DRAM ASP will be 74% above 1QCY26.

## Spot price:

\- PC DRAM: PC DRAM chip spot price further increased in June, up by 5.6% and 11.5% MoM for DDR4 and DDR5, respectively (Exhibit 1, Exhibit 3, Exhibit 4, Exhibit 5, Exhibit 6). Distributors had sold some inventory earlier, and that caused spot price to correct somehow. However, it appeared that the supply released from this has been digested, and spot price hence stabilized & further rose in June.

\- Server DRAM: Server DRAM module spot price was up by 6.1-26.4% MoM, in which DDR5 was particularly strong (Exhibit 1, Exhibit 11, Exhibit 12). Similar to PC DRAM chip spot pride, server DRAM module spot prices had seen some drop previously, but they have stabilized and further increased during the past two months. Overall spot prices remained considerably above contract prices, especially for DDR5 modules, and thus still indicated shortage in the market. With AI demand staying robust, we don't think spot prices will fall off a cliff any time soon.

## - Contract price:

\- Average: Overall, taking a weighted average of multiple samples, we find contracts set in June indicated conventional DRAM prices to rise by 74% QoQ in 2QCY26, c. 10 pts higher than what the May contracts indicated (Exhibit 1). This is also above our current model, though the actual company reported ASP may differ due to changing mix among PC, Mobile, server, etc., and also the balance from steadier HBM price that is largely set by annual contracts. Thus, the weighted average contract price increase here may not match the increase reported in company earnings releases but does serve as an important indication for where the market is heading.

\- PC DRAM: Contract price in June was slightly up MoM, and indicated 2QCY26 contract price to be $51\%$ higher QoQ (Exhibit 1, Exhibit 3, Exhibit 7). Most PC OEMs had finished price negotiation for 2QCY26 in Apr hence June's overall DRAM module prices only increased marginally over May. Demand stayed more resilient than expected, and good demand for MacBook Neo & promotion of Microsoft were two of the reasons. DRAM chip contract prices also rose MoM, though

module houses were shifting production to server DRAM modules. Looking ahead to 3QCY26, TrendForce raises price expectation to 15-20% QoQ increase. That is more than the 8-13% increase forecast previously, but still represents a notable deceleration from the hike of 45-50% in 2QCY26.

\- PC DDR4: PC DDR4 chip contract price moderately rose by 5% MoM, on par with DDR5 chips, though DDR4 module was flattish (Exhibit 5, Exhibit 8, Exhibit 9, Exhibit 10). DDR4 price increase has been primarily driven by Nanya (2408 TT, not covered), which is becoming the main supplier of DDR4. Demand is still resilient driven by low-end PCs and consumer applications. Hence price is likely to stay robust and possibly stronger than DDR5.

\- Server DRAM: June server DRAM contract price went up MoM by 0-9.1%, and indicated 2QCY26 price to be 60% higher than 1QCY26 (Exhibit 1, Exhibit 11, Exhibit 13). While SK hynix and Micron had largely concluded price negotiations in Apr, Samsung continued to push for higher prices, and likely will be ahead of other suppliers in 2QCY26 price. Vendors continued supplying more server DRAM, through allocating capacity from other segments to server DRAM, and also from wafer capacity released from the delayed HBM4 ramp. Any increased supply was however quickly absorbed by demand especially low capacity (<64GB) RDIMM for CPU servers. US CSPs continued to be the key customers and enjoy priority supply. Micron's LTA price ceiling is near its are contract price level, while Samsung & SK hynix's LTA price ceiling may be higher, according to TrendForce. Chinese CSPs were still in discussion for LTA but likely won't get as much fulfillment or as favorable terms as US CSPs. At the same time, Chinese CSPs will seek supply from domestic suppliers in addition. Looking ahead to 3QCY26, TrendForce expects price to rise by 13-18% QoQ.

\- Server DDR4: Server DDR4 contract price was unchanged MoM, vs +9% from DDR5 (Exhibit 12, Exhibit 14). And hence DDR5's premium over DDR4 expanded slightly to 22% (Exhibit 15). DDR4 likely will remain in shortage with supply EOL from large suppliers. However, DDR5 was likely already over 90% of the market into 2QCY26 and hence should be the focus.

\- Mobile DRAM: TrendForce updates Mobile DRAM contract price data only in the first month of a quarter. 2QCY26 contract price should have been finalized by the end of May. So far Samsung and Micron have asked for 80%+ increase over 1QCY26, while SK hynix's initial provisional ask was more lenient at 55-60%. With that, TrendForce expects 2QCY26 Mobile DRAM contract price to eventually arrive at close to 80% QoQ increase, with LPDDR5 rising more than LPDDR4 (Exhibit 1, Exhibit 16, Exhibit 17, Exhibit 18). After two quarters of unprecedented price surge, smartphone OEMs are adjusting their production plan and also memory usage. Now TrendForce expects smartphone unit to drop by 16% this year with 2QCY26 dropped by more than 10% YoY. The shortage is relatively more benign for LPDDR4, as CXMT and SK hynix are still providing supply, & low to mid-end smartphones, which mainly use LPDDR4, are cut more than high-end ones that use LPDDR5.

\- Specialty DRAM: Specialty DRAM contract price moved up meaningfully, by 8.3-13.6% MoM, in June, and June contracts indicated 2QCY26 to be 105-108% higher vs. 1QCY26 (Exhibit 1, Exhibit 19). Supply for legacy products was increasingly coming from Taiwanese suppliers and remained significantly below demand. TrendForce did observe some de-spec-ing among consumer OEMs, who were degrading to lower densities or earlier generations (DDR3) to reduce cost. It is however offset by more demand from AI related applications like network switch & Server SSD and Auto applications which are also equipped with legacy DRAM. TrendForce now expects the contract price for DDR3/DDR4 to rise 35-40%/28-33% QoQ in 3QCY26, respectively.

\- In summary, contract price further rose MoM in June and hence still indicated a strong contract price increase in 2QCY26 for conventional DRAM. However into 3QCY26, price increase is expected to decelerate significantly to 13-18% QoQ, as PC, mobile & consumer segment demand shrink. LTAs likely have been signed with some US CSPs and likely still in discussion for China CSPs and some consumer customers. And the ceiling price, if agreed in LTAs, may imply further ASP increase will be increasingly more from transactions not covered of the ceiling. Overall the shortage remains and price likely can remain strong into CY27, but we believe it should start to dip from 2HCY27 and into CY28, as more LTAs become effective Y& more capacity is brought online. See Global Memory: Memory becoming a burden of AI too? for details.

NAND wafer contract price rose moderately MoM in June, but with prices of mobile NAND and SSD still strong, the blended NAND contract price in 2QCY26 should increase \~60% QoQ in 2QCY26. The pace of the price hike is also expected to narrow notably in 3QCY26.

## - Spot price:

\- NAND Wafer: June NAND wafer spot price dropped by 3.3% MoM following almost flattish May (Exhibit 2, Exhibit 20, Exhibit 21). At the end of June spot price was close to 20-25% below contract price, but we are mindful that wafer is a small part of the overall NAND market and spot wafer even smaller.

## - Contract price:

\- Average: Taking the average of multiple samples of NAND wafer and eMMC/UFS, we find contracts set in June indicated 42% QoQ NAND price increase from 1QCY26 to 2QCY26 (Exhibit 2). However, our samples don't include client and enterprise SSDs and over-considers NAND wafer. We understand the price hike of SSDs in 2QCY26 may be as much as 70%, similar to that of mobile NAND. Considering that, we think c. 60% should be a more accurate estimate for the blended contract price QoQ increase for 2QCY26, and it is slightly ahead of our forecast too. Still actual company reported 2QCY26 ASP may differ as product mix changes can have a significant impact on blended ASP.

\- NAND Wafer: NAND wafer contract price increase continued but only moderately

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
