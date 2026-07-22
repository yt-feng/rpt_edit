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
## Korea Equity Strategy

Update on the de-leveraging process in Korea

While the fundamentals of the Korea market remain on solid ground (despite some concerns – see below), an intense period of de-leveraging has driven equity prices lower. The KOSPI index is now down a sizable -28% from the peak on 22 June in a highly volatile move. What was triggered by routine fundamental concerns and rotational flow, was amplified by leveraged ETFs, and in recent days increasingly has the hallmarks of hedge fund positioning unwind (especially given the -30% Price Momentum factor drawdown). The rapid pace of gains in the Korea market over the past year made it an inevitable destination of leverage - from retail investors, equity L/S hedge funds as well as macro funds - compounding these gains. As we have noted for the past 6-7 weeks now (see here, here), some of the side effects of this growth have been the elevated volatility and forced foreign selling - producing a self-correcting mechanism. In the near term, our focus remains on the extent of normalization in these conditions (we estimate leveraged ETF unwind to be 75% through and equity H/F de-leveraging >50% through). Stepping back, though, our view remains that the fundamental strength in the market remains good for several years ahead (a combination of global AI spend, security/resilience spend, wealth effect across corporates/households/government and structural governance improvements), meaning that the market should be able to overcome positioning unwinds and persevere with the positive trend. We remain OW Korea in our regional allocations and our 12m-out base case KOSPI target remains 12,500.

\- Extent of leverage “normalization”: Of all the leverage channels in Korea, we see (1) futures & options largely an institutional market with limited signs of speculative excess, and (2) retail leverage via margin and bank loans as relatively modest (down a lot in KOSDAQ though). The issues around (3) swap capacity (globally rising funding costs compounded by Korea-specific capital constraints and concentration issues) and (4) volatility from outstanding leveraged ETFs – both remain but have materially eased (tactically, because the market is lower, and structurally, because the underlying issues are being addressed). We estimate leveraged ETF unwind to be 75% through (to an acceptable level of \~\$18bn) and equity H/F deleveraging more than 50% through (assuming L/S ratios reach the upper end of 2025’s range).

\- Leveraged ETFs: Leveraged ETFs with Korea underlyings grew to \$50bn in AUM (mostly due to the growth of the market) by late June. Relative to its market size, this was 4x larger than the US and led to very pronounced volatility (and forced de-leveraging on down-days) - the VKOSPI to VIX ratio is sill closer to 5x vs the usual 1x. Not only does this detract from vol-sensitive inflows, but it makes vol-based risk-management harder for asset managers and securities companies. Over Jun and July we have seen this excessive volatility compound the modest AI jitters seen elsewhere in global AI hardware stocks. Similar to previous deleveraging of leveraged products (Nikkei in 2015, Nasdaq in 2022, Oil in 2020, and most famously - even if somewhat differently - the inverse VIX products in 2018), this period of volatility has shrunk leveraged ETFs with Korea underlyings now to \$26bn. With new regulations aimed at keeping tighter checks on the growth of this space (minimum deposit requirement raised to KRW30mn from KRW10mn from

Equity Macro Research

Mixo Das AC (852) 2800-0511  
mixo.das@JPM.com  
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Stanley Yang  
(82-2) 758-5712  
stanley.yang@JPM.com  
JPM Securities (Far East) Limited, Seoul Branch

Rajiv Batra  
(65) 6882-8151  
rajiv.j.batra@JPM.com  
JPM Securities Singapore Private Limited

Joy Wang  
(852) 2800-2322  
joy.y.wang@JPM.com  
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 8 for analyst certification and important disclosures, including non-US analyst disclosures.

Aug 5 $^{th}$ , only cash will be recognized as the initial margin from Aug 19 $^{th}$ , new listings of single-stock levered ETF products are temporarily halted, minimum trading unit for single-stock leveraged products will be raised from 1 share to 20 shares starting in Nov), further moderation in size is likely ahead.

\- HF leverage and swap capacity: Swap capacity limits (for investors to access Korea equities via brokers) have been tightening for a while - faced with rapidly rising interest from global equity and macro investors (gross and net exposure towards Korea in the JPM Prime book have risen rapidly since April). This is partly a global story, where higher demand for financing (due to growth in markets and shift in AUM mix to higher leveraged entities) and tightening regulations having driven funding rates higher. It is also partly a Korea story, given the higher capital needed to match higher trading volumes (6-7x over the past year) and difficulty in managing concentration risks of investors unanimously preferring positions in the memory space. With the decline in market size and underperformance of memory names, though, this capacity tightness has eased substantially (a full normalization is still some distance away as brokers and investors work through these constraints). Similarly, in the present de-leveraging process, L/S ratios in the JPM Prime book have declined from highs of $>5.5\mathrm{x}$ to now $<4\mathrm{x}$ .

\- Retail leverage and margins: Margin balances have declined somewhat from a high of >\$25bn to \~\$21bn now. Notably, most of the declines and margin calls have been in smaller-cap KOSDAQ market, and not in KOSPI. But at \$21bn, this is just 0.5% of equity market cap (vs 1.9% of market cap in the US and 2.8% in China A-shares). In addition, unlike leveraged ETFs that undergo a process of forced de-leveraging on any spot price declines, margin lending comes with buffers and discretion. Korean retail investors still have ample equity gains, cash balances, higher incomes and overseas assets to tap into to absorb any margin calls should they want to keep the position. We are thus less concerned about margin calls and de-leveraging through this channel becoming a systemic problem.

\- Record foreign outflows are slowing: There has been >\$110bn of foreign outflows from Korea YTD - which would handily break the record of annual outflows from any market in Asia. The two memory names had become so large that they started to hit mandate limits for EM investors - which we estimated to be affecting roughly 10% of the foreign ownership in both stocks in 2Q. This forced investors to sell on rallies. Indeed, \~90% of YTD foreign outflows from Korea come from the memory names alone. This selling pressure has eased tactically as Korea (and particularly the memory names) has underperformed, meaning that the two heavyweights are now only 7.5% and 5.7% weights in MSCI EM (vs 9.5% and 8.3% in late June).

\- Fundamentals: We remain bullish on the AI cycle and related fundamentals. Earnings growth rate in Korea will slow from the scorching pace of 2026, but the question in Korea now is less about growth and more about sustainability (how much visibility can we have about higher earnings levels). While monetization at the model layer is being questioned again (with very positive reception to open-source models), at the hyperscaler layer the rental economics for data centers remain very positive. This means that hyperscalers should keep spending up. All our indicators on this are currently green across model capability, funding availability and rental rates. And external risks (like regulation, recession, etc.) don’t look imminent. Memory demand has been questioned recently with reported technological and process breakthroughs reducing memory demand – but we are yet to see this in reality. And in terms of supply, the supply of memory equity should not be conflated with supply of physical memory. Outside of AI, there are earnings tailwinds from growth in a variety of (AI-adjacent and other) Industrials, potential wealth-effect boost to Financials and Consumer, and ongoing (if incremental) valuation tailwinds from the governance reforms (which will likely come back to prominence later this year).

Figure 1: KOSPI index has declined $-29\%$ from the peak of 22 Jun  
![](images/97bfff5d72c608a0f287a2109a73c0563e3121699e423a70eef0640a179036b5.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 2: Bringing the index RSI to lowest levels since the start of this rally post Liberation Day in 2025  
![](images/4b78bf52af8a754f88e475038e31616b8806d19d68357ce034d97614ed287e60.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 3: Korea is still the best performing market in the region YTD in USD terms  
![](images/e4a14f97f531dd2e443f85451ce96e75e137648ffc32878df8d2f06de83eed57.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 4: KOSPI has largely been a reflection of memory upside in recent months  
![](images/7a8923e25ba17384aa5df37964ee5745f34e7e6c495e5368563e13779c90b4f7.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 5: Margin balances and leveraged products are the primary channels for retail investors to access leveraged upside - in Korea margin balances are very acceptable, but leveraged ETFs outstanding are still large

<table><tr><td>$bn</td><td>Market cap</td><td>Margin balances</td><td>% of Mcap</td><td>Leveraged ETFs outstanding</td><td>% of Mcap</td></tr><tr><td>US</td><td>80000</td><td>1502</td><td>1.9%</td><td>250</td><td>0.3%</td></tr><tr><td>Korea</td><td>4000</td><td>21</td><td>0.5%</td><td>26</td><td>0.7%</td></tr><tr><td>Japan</td><td>8800</td><td>43</td><td>0.5%</td><td>5</td><td>0.1%</td></tr><tr><td>China A</td><td>15000</td><td>422</td><td>2.8%</td><td>1</td><td>0.0%</td></tr><tr><td>Taiwan</td><td>5000</td><td>19</td><td>0.4%</td><td>8</td><td>0.2%</td></tr></table>

Source: Bloomberg Finance L.P., FINRA, KOFIA, JPX, JPM Equity Macro Research.

Figure 6: For retail investors, margin leverage is not too high (and falling vs market cap)  
![](images/0f913d87ae2be07d2b67b7471959766b2d7816cedd1dbdee2d0a3fe8643d3c9a.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 8: In terms of leveraged ETFs, their AUM has declined from highs of \$50bn to now \$26bn  
![](images/d3e32e2dda2804005044a4e554b877b272ca8c03edb9290135bcca166d7d6735.jpg)

Figure 7: Similarly there is little evidence at the aggregate level that Korean households are borrowing from banks to invest in equities loans to households %y-y. Data as of April 2026  
![](images/b46ad7cb234095a6b986b096bac0511481855415529be72713c0d347006ad384.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 9: To be sure, much of this is simply due to the decline in the market, as flows have continued to actually be positive
cumulative inflows, USD mn  
![](images/15a8e7fd0a37266ce24545b9e13f91ad9c28f3ad1958b221aaa75f26ac4fb750.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 10: Largely as a result of leveraged ETF hedging, volatility in Korea has notably disconnected from volatility elsewhere - and yet to normalize  
X  
![](images/27e95acd2d1ab58341b1a4727df5ae2c5e8e41ecc801f5ee5b349d0ef04dc103.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 12: Separately, Korean equities have seen >\$110bn of outflows YTD, but most of this is due to mandate constraints for LOs on owning large-caps

cumulative flow, \$mn, KRX data

![](images/c8e4992ffe0bb130e893d50fca8067f545e7dc9ddab5de48ad5077199adeff04.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.  
Figure 11: The open interest of single stock futures (implementation channel of the leveraged ETFs) has started to decline now USD mn  
cumulative flow, \$mn

![](images/505bfbf5ce804a49f4e9eff64a7b39b9177d18c2065ada00a5af3fc9610317b0.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 13: Indeed, $90\%$ of the outflow is from the two memory names. The decline in EM index weights of these stocks has substantially slowed outflows

![](images/d74474c117ed1817b0a88b1752d298e0581a708862b665b89b533ceeb57a1413.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 18: Price momentum factor has seen a deep drawdown in recent weeks - similar to US, Japan etc indicative performance of L/S quintiles

Figure 14: L/S ratios for hedge funds in the JPM Prime book has declined from highs, but not fully normalized  
![](images/5b52e97a78650e70bd6dbd254d1312840a07c9d981a2f6d1bbf688c342442d1d.jpg)  
Source: Bloomberg Finance L.P., JPM Positioning Intelligence.

Figure 15: EM LO investors have become more UW Korea YTD as mandate constraints bite  
weightings relative to the MSCI benchmark and net OW/UW  
![](images/65e126524cb87298b78394513d34eb4df8d01f855498b8aef8c1d5e6e843a4ee.jpg)  
Source: Bloomberg Finance L.P., EPFR, MSCI, JPM Equity Macro Research.

Figure 16: Retail investors have been the main buyers of Korean equities - sentiment about equities and leverage is still strong KRW bn, KRX data  
![](images/133e97636985b058725453251c75514c48896c7945e3bb7706aa4f3315f23887.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 17: Since the beginning of June, most purchased overseas stocks by Korean retail investors include several leveraged products \$bn  
![](images/e4c223bde643cdd8e559c2679b7d114e594b084dba2e956dd620fc06552b037b.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

<table><tr><td></td><td>Px Momentum</td><td>EPS revision</td><td>Growth</td><td>Quality</td><td>Value</td><td>Low Vol</td></tr><tr><td>Week ending 03-Jul</td><td>-10.8%</td><td>-4.9%</td><td>-0.8%</td><td>3.3%</td><td>0.9%</td><td>8.7%</td></tr><tr><td>Week ending 10-Jul</td><td>-7.9%</td><td>-3.1%</td><td>-2.1%</td><td>0.8%</td><td>5.6%</td><td>7.9%</td></tr><tr><td>Week ending 17-Jul</td><td>-6.3%</td><td>-3.0%</td><td>0.6%</td><td>1.9%</td><td>1.3%</td><td>7.0%</td></tr><tr><td>Week ending 24-Jul</td><td>-1.7%</td><td>0.4%</td><td>-1.0%</td><td>-0.2%</td><td>1.3%</td><td>3.4%</td></tr></table>

Figure 19: Momentum crowding is now starting to come off  
![](images/27e33f927e6448f4036a2803c67ea2d9ee6e6f692648c934aaec4c77dc44f531.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 20: Drawdown in Price Momentum factor still leaves strong YTD performance

indicative performance of L/S quintile - log scale

![](images/4a9f1e5da43a05bc8de20c1d4aa531693eea7077c4f0c6d8361ff02ce8d47e34.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 21: 3Q tends to be reasonably strong seasonally for Price Momentum factor performance in Korea - 4Q is more challenging Average performance over past five years  
![](images/4e94cd57382fa67ffe79d035ec671f57bf672589887d4ea41371a6906072c405.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 22: Korea sector EPS revisions remain strong as earnings get underway

<table><tr><td rowspan="2"></td><td colspan="3">2026 EPS</td><td colspan="3">2027 EPS</td></tr><tr><td>1m</td><td>3m</td><td>6m</td><td>1m</td><td>3m</td><td>6m</td></tr><tr><td>Market</td><td>7.8%</td><td>35.5%</td><td>143.4%</td><td>12.2%</td><td>53.7%</td><td>199.8%</td></tr><tr><td>Tech</td><td>8.5%</td><td>42.2%</td><td>215.5%</td><td>13.1%</td><td>63.1%</td><td>303.3%</td></tr><tr><td>Financials</td><td>1.7%</td><td>5.7%</td><td>9.8%</td><td>2.3%</td><td>6.5%</td><td>11.1%</td></tr><tr><td>Industrials</td><td>11.8%</td><td>42.6%</td><td>91.0%</td><td>18.1%</t

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 21 Jul 2026 03:22 AM HKT

Disseminated 21 Jul 2026 03:22 AM HKT
"""
