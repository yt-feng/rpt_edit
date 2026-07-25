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
# JPM

## China Equity Strategy

Policy put emerges after tech sell-off, 2Q earnings catalyst

Policy put emerges after AI-led deaveraging. The sharp AI-led onshore sell-off has finally triggered a policy response. Over the weekend, China Reform Holding and China Chengtong announced Rmb60bn of purchases in onshore equities and ETFs, while indicating they will continue to add holdings. Notably, tech companies were explicitly included alongside central SOE stocks and ETFs. Our ETF flow tracker shows a swift reversal over the past week across both benchmark ETFs and AI/tech-focused products such as STAR 50 and STAR Chip ETFs. Daily A-share buybacks have also recently surged to a YTD high (Figure 1-Figure 4). Positioning also looks less stretched, with the A-share margin-buy ratio normalized and, regionally, Korea's leveraged ETF unwind estimated to be \~75% through. In early July we called for a tactical rotation into non-AI trades, but this trade may regain traction in late July/early August as solid global earnings guidance coincides with a healthier price set-up following the recent deleveraging. Our US equity strategist expects 2Q26 hyperscaler results to continue validating the AI infrastructure build-out, with upside risk to consensus capex over the next 4–6 quarters and further upward earnings revisions for semiconductors. However, a more sustainable market rebalancing in China equities still requires stronger fundamental support from non-AI and domestic demand cohorts, which appears limited at this stage. Our China economists expect additional policy support could be introduced after the July Politburo meeting if June activity data and 3Q momentum remain soft. JPM China AI ecosystem top picks are Zhongji Innolight, Victory Giant-H, JCET-A and Weichai-H in the global supply chain, and NAURA, AMEC-A, Baidu, Zhipu and Iluvatar CoreX as localization plays. We think China's AI ecosystem can reassert leadership during the earnings season, outperforming on both 2Q results and 2H guidance.

\- 2Q26 earnings: achievable bar, eye on potential upgrades from Materials, IT, Industrials, and non-bank Financials. The 2Q26 EPS y-y consensus growth estimates of $2.8\% / 15.7\%$ for MXCN/CSI-300 appear achievable to us without significant downward revision. Resilient performance from upstream commodities, IT, industrials and non-bank financials should help offset continued pressure in broad consumption, property, traditional infrastructure and related upstream sectors. However, bifurcation could remain within sectors, e.g. across internet platforms where revenue quality is improving in AI cloud service though bottom-line consensus remains constrained by elevated AI capex and reinvestment cycles. We recommend investors position for names with visible earnings upgrade trajectories and improving margins, namely IT, industrials, and materials while remaining cautious on sectors where revenue deceleration coincides with sticky cost structures, i.e. consumer staples in particular liquor, and second-tier property.

\- The Internet Sector Conundrum: China's internet sector may see a revenue-up, earnings-flat dynamic. The nuance lies in the divergence between operating momentum in core businesses and the dilutive impact of accelerated AI investment on bottom-line outcomes. Tencent: for 2Q26, JPM forecasts revenue to rise \~9%y-y, with VAS up 5–6%, games up 9–10%, marketing services up 18–19%, and fintech up around 5%, showing continued strength in established businesses; however, adjusted EPS was cut by 5% after the FY26 capex estimate was raised to RMB200bn, with the reduction attributed to heavier AI investment and depreciation from 2H26 rather than any deterioration

See page 8 for analyst certification and important disclosures, including non-US analyst disclosures.

Equity Macro Research  
Erin Zhang, CFA AC  
(86-21) 6106 6328  
erin.zhang@JPM.com  
SAC Registration Number: S1730521090002  
JPM Securities (China) Company Limited

Tim Huang  
(852) 2800-4323  
tim.huang@JPM.com  
JPM Securities (Asia Pacific) Limited/  
JPM Broking (Hong Kong) Limited

Rajiv Batra  
(65) 6882-8151  
rajiv.j.batra@JPM.com  
JPM Securities Singapore Private Limited

Head of China Research

Alex Yao  
(86 21) 6106 6505  
alex.yao@JPM.com  
SAC Registration Number: S1730523020001  
JPM Securities (China) Company Limited

in established businesses. Alibaba: JPM expects substantial upward revision in cloud profitability to be largely offset by continued softness in core commerce customer management revenue, leaving group-level full-year earnings essentially unchanged net-net. Baidu: Advertising revenue is expected to decline by \~23%/21% in 2Q26/2026, alongside sustained AI investment intensity, which has driven \~12% YTD downward revisions to full-year EPS, despite high double-digit AI cloud revenue growth (JPMe: +87%y-y in 2Q26). The net takeaway is that the internet sector is not experiencing a traditional earnings downgrade cycle, but rather a deliberate reinvestment cycle that is compressing near-term margins in exchange for longer-term optionality—an outcome that the market is still in the process of re-rating.

\- Likely outperformer #1 – Information Technology & AI Supply Chain: Global AI capex remains the dominant secular tailwind for China's technology hardware ecosystem. The dual-circulation dynamic—domestic AI infrastructure buildout alongside overseas hyperscaler demand—continues to drive export momentum and electronic supply chain profitability. Semiconductor equipment stands out with a 70.0% positive profit alert ratio, while the broader IT sector is expected to deliver 72% y-y EPS growth in Q2 for CSI 300 constituents, with full-year 2026 consensus at 96%. Materials sectors leveraged to advanced manufacturing, particularly specialty chemicals and new materials, are compounding this uplift.

\- Likely outperformer #2 – Industrials & Advanced Manufacturing: Industrial profit momentum has inflected decisively higher. Operating profit growth for above-scale industrial enterprises continues to outpace revenue expansion, indicating sustained net profit margin improvement across the sector. Machinery, high-end equipment and defense contractors are seeing tangible order conversion, with capacity utilization rates for auto manufacturing and chemical fibers sitting at elevated percentiles versus history. Within the CSI 300 universe, the industrials sector is expected to deliver 10.6% y-y EPS growth in Q2, with full-year 2026 consensus at 20.3%. The breadth of positive profit alerts is particularly encouraging—machinery and electrical equipment sectors report 85.7% and 69.8% positive pre-announcement rates respectively, signaling broad-based operational improvement rather than idiosyncratic strength.

\- Likely outperformer #3 – Financials: The financial sector is experiencing a pronounced earnings rebound driven by capital markets recovery. Average daily A-share trading value doubled y-y in Q2, accompanied by substantial margin financing expansion, and ongoing IPO rush. Securities firms are the primary beneficiaries (Figure 17 and Figure 18). Insurance companies are also seeing meaningful recovery in equity investment floating gains. Within the CSI 300, financials EPS growth reaches 3.7% y-y in Q2, accelerating to 31.6% for full-year 2026 as the operating leverage from market activity compounds. Energy and materials sectors, while cyclical in nature, are delivering the strongest headline EPS growth at 52.8% and 72.4% respectively for Q2 CSI 300, supported by commodity price stabilization and supply discipline.

\- Likely underperformer #1 – Real Estate & Post-Property Cycle: Property and its downstream value chain remain the most significant drag on aggregate earnings. Thirty-city commodity housing sales continue to contract y-y, with no meaningful inflection in sight. Building materials, home appliances, and furniture sectors face sustained revenue pressure, compounded by raw material cost increases including resin price hikes. Furniture industry operating profits collapsed 59% y-y in the first five months, while real estate development and management have reported an 18.7% first-loss ratio among pre-announcing firms.

\- Likely underperformer #2 – Consumers: Consumer sectors are navigating a high-base hangover from last year's trade-in subsidy programs. Auto and home appliance sales growth has decelerated materially in Q2 as the favorable year-ago comparison rolls off. Auto industry operating profit fell 20% y-y in 5M26, with auto components reporting a 14.1% first-loss ratio. Consumer discretionary overall is tracking -6.9% y-y EPS growth for MXCN names in Q2 on consensus, with autos, household durables, and specialty retail all contributing negatively. Even consumer staples are seeing pressure, with food products and beverages registering elevated earnings decline ratios.

\- We maintain our end-2026 base case targets for the MXCN index and CSI-300 at 100 and 5,200, respectively, with bear-case targets of 80 and 4,000, underpinned by $13\%$ and $24\%$ consensus year-over-year EPS growth projections and broadly supportive liquidity conditions. Our China economists expect additional policy support could be introduced after the July Politburo meeting if June activity data and 3Q momentum remain soft. Our top picks in the non-AI fields include Bank of China-H, CICC-H, Innovent, BYD-H and CR Land.

Figure 1: Accumulative benchmark ETF inflows since 2024: market tends to recover following the ETF inflow upticks  
![](images/30000da183ea0c64ea81153a12624fe2a53c558207a71df83b36dac4015c41fe.jpg)  
Source: Wind (21 Jul 2026)

Figure 2: Accumulative STAR50 + STAR Chip ETF inflows since 2024  
![](images/548015c87c1d824d215d53e9c574785c6386c16efbb36d128fc7747ae4198a81.jpg)  
Source: Wind (21 Jul 2026)

Figure 3: Accumulative A-share ETF net flow has seen more than RMB1trn drop this year  
![](images/8e040d18137c7821e2d2def5af66f91b7987e30fd66cbd4823ba87a8bd2d0c93.jpg)  
Source: Wind (21 Jul 2026)

Figure 4: A-share daily buyback surged to YTD high  
![](images/d27b338c30b020ac23b707f379d6f4fef89e8169abd2edee9426ae0ddb814d36.jpg)  
Source: Wind (21 Jul 2026)

Figure 5: Onshore margin activity has cooled  
![](images/24273fea4652ce1ee5f0e55f657816ed7a56f104fa2f2b2279f8a6417679ff3e.jpg)  
Source: Wind (21 Jul 2026)

Figure 6: A-share margin balance eased on the margin  
![](images/c8911a63c9e9f7c2872e04a0fc6f467bfe198c2841f6efb5202f0d68a6d2031b.jpg)  
Source: Wind (21 Jul 2026)

Revenue y-y: industrial enterprises above designated side (YTD)
Operating profit y-y: industrial enterprises above designated side (YTD)
Source: Wind (17 Jul 2026)

Figure 7: MXCN EPS y-y by sector (2Q26/2H26/2026 on consensus)

<table><tr><td>GICS Sector Name</td><td>1Q26</td><td>2Q26</td><td>2H26</td><td>2026</td></tr><tr><td>Index</td><td>-19.1%</td><td>2.8%</td><td>16.7%</td><td>8.8%</td></tr><tr><td>Communication Services</td><td>5.8%</td><td>2.7%</td><td>4.1%</td><td>6.0%</td></tr><tr><td>Consumer Discretionary</td><td>-68.8%</td><td>-6.9%</td><td>81.5%</td><td>13.1%</td></tr><tr><td>Consumer Staples</td><td>-47.7%</td><td>-0.1%</td><td>69.8%</td><td>18.2%</td></tr><tr><td>Energy</td><td>12.5%</td><td>44.0%</td><td>38.7%</td><td>25.1%</td></tr><tr><td>Financials</td><td>-7.4%</td><td>-0.5%</td><td>-6.6%</td><td>-0.1%</td></tr><tr><td>Health Care</td><td>-32.4%</td><td>16.9%</td><td>109.9%</td><td>36.4%</td></tr><tr><td>Industrials</td><td>-9.0%</td><td>6.0%</td><td>15.3%</td><td>13.4%</td></tr><tr><td>Information Technology</td><td>0.6%</td><td>-12.6%</td><td>25.1%</td><td>14.5%</td></tr><tr><td>Materials</td><td>16.5%</td><td>73.2%</td><td>82.8%</td><td>71.0%</td></tr><tr><td>Real Estate</td><td>-85.6%</td><td>-9.8%</td><td>26.4%</td><td>8.9%</td></tr><tr><td>Utilities</td><td>-2.5%</td><td>5.2%</td><td>-30.1%</td><td>-12.1%</td></tr></table>

Source: LSEG Workspace (17 Jul 2026), Wind (17 Jul 2026), MSCI (1 Jul 2026)

Figure 8: CSI-300 EPS y-y by sector (2Q26/2H26/2026 on consensus)

<table><tr><td>GICS Sector Name</td><td>1Q26</td><td>2Q26</td><td>2H26</td><td>2026</td></tr><tr><td>Index</td><td>6.8%</td><td>15.7%</td><td>38.3%</td><td>24.4%</td></tr><tr><td>Communication Services</td><td>2.3%</td><td>6.8%</td><td>52.4%</td><td>20.0%</td></tr><tr><td>Consumer Discretionary</td><td>-9.3%</td><td>-5.0%</td><td>30.8%</td><td>6.4%</td></tr><tr><td>Consumer Staples</td><td>-6.2%</td><td>-8.6%</td><td>22.3%</td><td>3.1%</td></tr><tr><td>Energy</td><td>17.8%</td><td>52.8%</td><td>43.3%</td><td>31.6%</td></tr><tr><td>Financials</td><td>-5.5%</td><td>3.8%</td><td>5.3%</td><td>4.9%</td></tr><tr><td>Health Care</td><td>5.2%</td><td>-2.3%</td><td>71.6%</td><td>26.1%</td></tr><tr><td>Industrials</td><td>9.3%</td><td>10.6%</td><td>20.4%</td><td>20.3%</td></tr><tr><td>Information Technology</td><td>76.5%</td><td>71.9%</td><td>109.9%</td><td>96.3%</td></tr><tr><td>Materials</td><td>83.0%</td><td>74.1%</td><td>63.1%</td><td>61.0%</td></tr><tr><td>Real Estate</td><td>-22.8%</td><td>58.8%</td><td>92.9%</td><td>80.4%</td></tr><tr><td>Utilities</td><td>6.3%</td><td>6.2%</td><td>-2.5%</td><td>3.6%</td></tr></table>

Source: LSEG Workspace (17 Jul 2026), Wind (17 Jul 2026)  
Figure 9: Industrial enterprises' revenue y-y and operating profit y-y

![](images/27d878f3eaf0fe9af38a2f45bbff9273b217bd4083740f7d1b57d64cb2644592.jpg)  
Source: Wind (17 Jul 2026)  
Figure 10: Industrial Production by sector

![](images/a8a247e58d403a29f6f3fb35e38afe51ef63ce5f6b9703b1e16f1cf5c3974619.jpg)

Figure 11: Industrial capacity utilization  
![](images/3cfd41cabb6768dc660691f533a11c7c99417b8efd545fdb03aaaf4d14c90aca.jpg)  
Source: Wind (17 Jul 2026)  
Source: Wind (17 Jul 2026)

Figure 12: Industrial capacity utilization by sector  
![](images/d9fc9bbb309f1dbb48205f06a7b0c19be77687818176b14d67489707d99d71a8.jpg)  
Source: Wind (17 Jul 2026)

Figure 13: China 30-cities' commodity housing sales (mn sqm, rolling 90d sum y-y)  
![](images/74552035eafd5f9f65327c306175e852b070ccf7aeb68b9bf989f7f6de6803ee.jpg)  
Source: Wind (17 Jul 2026)

Figure 14: Selected consumer industries' revenue and OP y-y in 5M26  
![](images/e76ee20a5f3a9afbdf821b4529b473e2423d935a4efd5b95936e46c5a076b9f5.jpg)  
Source: Wind (17 Jul 2026)

Figure 15: China raw milk ASP y-y  
![](images/d37db14ceb03d6c86b299fe9c65063959bcead2ad62d784b8b7ead1416474e76.jpg)  
Source: Wind (17 Jul 2026)

Figure 16: China auto sales y-y  
![](images/a481ebe18e36547d7ac688f984553e1f5e9cad6fecff9c539bbc1639a9de3dca.jpg)  
Source: Wind (17 Jul 2026)

Figure 17: A-share turnover  
![](images/0f2e1ad6f9539c843f4794bed7ff1a882d6395949400ef5438eba61da6d8535a.jpg)  
Source: Wind (17 Jul 2026)

Figure 18: HK market's equity financing  
![](images/77dcac3d775aee78be64d10191a18b5341fc3d273c4a24bc7866daefc49b5e0b.jpg)  
Source: Wind (17 Jul 2026)

Figure 19: A-share 2Q profit alerts

<table><tr><td>GICS Sector</td><td>GICS Industry</td><td>Aggr. FF mkt cap (Rmb bn)</td><td>Return since end 1Q26</td><td>Return YTD</td><td>Positive profit alert %</td><td>(Sizable increase - sizable decrease)/ total</td><td>(Loss to profit - first loss)/ total</td></tr><tr><td rowspan="12">Consumer Discretionary</td><td>Auto Components</td><td>246.8</td><td>-10.9%</td><td>-18.5%</td><td>34.4%</td><td>-1.6%</td><td>-14.1%</td></tr><tr><td>Automobiles</td><td>191.7</td><td>-34.6%</td><td>-43.1%</td><td>33.3%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Distributors III</td><td>11.0</td><td>-8.1%</td><td>-7.3%</td><td>50.0%</td><td>50.0%</td><td>-50.0%</td></tr><tr><td>Diversified Consumer Services</td><td>12.0</td><td>-20.2%</td><td>-31.3%</td><td>33.3%</td><td>16.7%</td><td>0.0%</td></tr><tr><td>Hotels, Restaurants &amp; Leisure</td><td>38.2</td><td>-23.2%</td><td>-26.8%</td><td>31.3%</td><td>-18.8%</td><td>18.8%</td></tr

[中间内容因长度限制已省略]

es discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
