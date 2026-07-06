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
# Circle Internet Group (CRCL): Key takeaways from management meetings

On June 30 $^{th}$ , we hosted meetings with CRCL's: 1) Co-founder, Chief Executive Officer and Chairman, Jeremy Allaire; and 2) Chief Financial Officer, Jeremy Fox-Green. Further detail within.

Management remain constructive on stablecoin adoption, citing growing adoption across both the digital asset ecosystem, and, increasingly, across a variety of areas within traditional finance, and highlighting recent growth in stablecoin volumes and market cap, vs. a weaker softer crypto market. The company highlighted broadening adoption across: 1) digital assets, driven by partnerships with scaled or fast-growing platforms (e.g., Hyperliquid); 2) cross-border payments and treasury management; 3) consumer commerce, with uptake and payments acceptance among leading payments companies, and, separately, the rise of stablecoin-linked credit cards; 4) capital markets, in which institutions are increasingly evaluating or adopting stablecoin as a settlement currency or as collateral, and facilitated by ongoing US regulatory reform; and 5) emerging agentic commerce use cases, with USDC representing \~99% of stablecoin payments on the dominant agentic commerce protocol, x402. Management also see upside from continued growth of tokenized real world assets (RWAs), for which stablecoin remains the natural settlement currency.

In terms of the competitive landscape, the company views stablecoins as structurally advantaged, relative to other forms of tokenized money, given greater interoperability and liquidity, by virtue of being a public and open internet financial system. It believes that USDC remain uniquely positioned to grow within the stablecoin ecosystem. Management noted that USDC is differentiated in its: 1) broad distribution and platform ecosystem, amplified by continuing to add partnerships that drive liquidity supernovas; 2) deep global liquidity across products and markets; and 3) differentiated infrastructure, in terms of robust transparency and global regulation. Further, the company noted that the cold start problem (including issues, such as a lack of network effects) likely limits the success of new stablecoins, vs. USDC, and that tokenized deposits have shortcomings, relative to stablecoins, in terms of more limited interoperability, as well the fact that they have bank credit risk, whereas stablecoins are fully reserved, without credit risk.

The company highlighted a strategic focus on adding additional partnerships, as well as building and expanding three key infrastructure offerings, which it believes can be combined with USDC to form a comprehensive on-chain financial

James Yaro
+1(212)902-1913 |
james.e.yaro@gs.com
GS & Co. LLC

Matthew Weng
+1(212)902-8484 |
matthew.weng@gs.com
GS & Co. LLC

Divyam Harlalka
+1(332)245-7818 |
divyam.harlalka@gs.com
GS India SPL

Lokesh Kumar Sangewar
+1(332)245-7846 |
lokesh.sangewar@gs.com
GS India SPL

stack: 1) the ARC Layer 1 blockchain, which CRCL views as a comprehensive financial operating system designed to enhance liquidity and interoperability appealing to traditional finance institutions; 2) the Circle Payments Network (CPN) cross-border payments product, which enables faster, more efficient cross-border payments through blockchain settlement; and 3) CRCL's agentic stack, in which investments are targeted at maintaining CRCL's dominant share in AI-related economic activities. In addition, management highlighted that they remain committed to expanding USDC distribution through partnerships, targeting platforms with strong, rapidly scaling liquidity that reinforce USDC's existing network effects. They will continue to share economics with this type of partner.

Management view the proposed market structure bill as a regulatory unlock, rather than a risk to the growth or economics of USDC. They believe that, as currently drafted, the CLARITY Act market structure bill would continue to allow issuers to incentivize distribution through revenue sharing, while establishing a clearer regulatory framework that could accelerate broader digital asset, and thus stablecoin, adoption. In terms of rewards, the company believes that, by permitting usage-based, rather than passive, yield-liked incentives, the bill would encourage transactional activity using stablecoins, rather than idle balance accumulation, which would more directly support adoption.

## Additional key takeaways:

Stablecoin/USDC adoption: Management continue to see proliferation of stablecoin use cases across both crypto and decentralized finance, and, increasingly, in traditional finance, as evidenced by the recent decoupling of stablecoin growth from declining crypto volumes and prices. Specifically, the company highlighted growing USDC adoption across:

☐ Cross-border payments and treasury management: Management highlighted that stablecoins are increasingly being used in bilateral cross-border payment flows, driven by the instant settlement and minimal transaction cost of stablecoins. They allow for more efficient treasury operations to achieve more efficient global settlement and money movements across card networks and other payments companies. Further, the company noted digital dollarization, or broad based organic growth in global dollar-backed stablecoin demand as a substitute for currencies or domestic banking, as a significant structural tailwind to adoption. They are seeing emerging markets adopt USDC, as well as transactions between developed and emerging markets.

☐ Consumer commerce: While nascent, CRCL noted growing consumer commerce usage of stablecoins, namely: 1) the rise of stablecoin-linked credit cards, through which users can hold and spend stablecoins; and 2) emerging stablecoin payment acceptance of USDC on major commerce platforms, e.g., Stripe and Shopify. When customers check out, they can choose to pay for purchases with USDC.

□ Agentic commerce: Management noted that AI agents have begun to undertake economic activity, namely in fraction-of-a-cent transactions through machine-native protocols, on which stablecoin's atomic settlement and minimal transaction costs are uniquely suitable. Further, the company pointed to its dominant share within agentic commerce, with USDC accounting for \~99% of all transactions on x402, the leading agentic payment protocol.

☐ Capital market: The company highlighted that stablecoins are beginning to see proliferation within traditional financial markets as a form of collateral, and as a settlement currency. The company noted increasing use of USDC in derivatives, tokenized asset markets, and broader financial market infrastructure. Further, they view the recent CFTC permission of Futures Commission Merchants (FCMs) to treat select stablecoins as readily marketable collateral as an important catalyst that could enable adoption over time. Finally, management noted that continued tokenization of real world assets likely supports further adoption, as stablecoins represent the natural on-chain cash leg for transacting and settlement.

Strategic focus areas: Management remained focused on expanding its infrastructure offerings, as CRCL continues to transition into an internet financial platform. They highlighted three key near-term product focus areas: 1) Arc, CRCL's proprietary L1 blockchain, which they view as a comprehensive financial operating system, designed to improve liquidity and interoperability; 2) Circle Payments Network (CPN), CRCL's cross-border payments product, which has continued to see strong and growing institutional adoption; and 3) CRCL's agentic products, in which the company is investing to enable developers and enterprises to build and deploy AI agents. Management noted that these three products are intrinsically connected to the broader Circle ecosystem, and reinforce the company's utility network effects. In addition, management emphasized that partnerships remain central to CRCL's distribution strategy, and they will continue to target partners with large, established liquidity, as well as attractive growth profiles. As scaling the network remains key to its strategy, CRCL is willing to strategically share issuance economics for key new partnerships that expand distribution.

Competitive backdrop: The company highlighted that stablecoins generally, and USDC in particular, are network effect businesses, and they are networks. The network is the public software infrastructure on the internet - anyone can connect to this stablecoin network, across individuals, businesses, or developers. Management view stablecoins as the form of tokenized cash with the most utility, and believe USDC is best-positioned offering within stablecoins, given its best-in-class interoperability, its best-in-class liquidity, and the strength of its infrastructure, in terms of transparency and significant global regulation. Further detail:.

☐ Stablecoin vs. tokenized deposits: Management view stablecoins as structurally advantaged, relative to tokenized deposits. Specifically, the company noted that stablecoins: 1) inherently offer greater liquidity and interoperability, by virtue of being public and open, whereas tokenized deposits are more likely to remain confined within individual bank or consortium ecosystems, which is the way banks have been built until now; and 2) represent fully reserved bearer digital cash, rather than tokenized bank liabilities that have bank credit risk.

☐ New stablecoin competitors: The company expects to see additional new stablecoin competition, but noted that the cold start problem likely limits the success of these new stablecoins. Specifically, management stated that these new stablecoins lack network effects that CRCL has built over more than a decade.

☐ Competitive advantages of USDC: The company believes USDC remains differentiated vs. other stablecoins, as evidenced by its dominant \~80% stablecoin transaction volume share in 1Q26. The company highlighted several competitive advantages of USDC, including: 1) the breadth of its distribution and platform ecosystem, which continues to strengthen through additional partnerships; 2) deep global liquidity across exchanges, OTC markets, payments and collateral markets, reinforcing network effects and utility; and 3) a differentiated regulatory infrastructure spanning multiple jurisdictions, which management believe will encourage institutional adoption.

☐ Increasing stablecoin participation by tradfi: The company views increasing participation from traditional financial institutions in the stablecoin ecosystem as an opportunity rather than a competitive threat, arguing that broader issuer participation should accelerate institutional adoption and ecosystem growth.

International expansion: Management maintained a constructive view on international expansion opportunities for USDC, highlighting growing demand for regulated digital dollars outside of the United States, particularly for cross-border payments and treasury use cases. The company believes international adoption should be supported by: 1) increasing institutional demand for fast, low-cost cross-border payments; 2) ongoing stablecoin regulation globally; and 3) partnerships with regional financial institutions, payment providers, and digital asset platforms that should broaden local stablecoin distribution.

Regulatory backdrop: The company continues to view the CLARITY Act market structure bill as a USDC growth tailwind, rather than a constraint on its economics and distribution. Management highlighted that, as written, CLARITY: 1) would maintain issuers' ability to enter into revenue sharing arrangements for distribution, which support CRCL's ability to continue to add partners; 2) could unlock meaningful incremental institutional crypto adoption, leading to greater overall stablecoin usage; and 3) promotes usage-based, instead of passive, yield-equivalent rewards. In the company's view, this incentivization encourages greater active use of stablecoin, rather than idle balance accumulation, which is good for overall adoption of the product.

Rating: We are Neutral-rated on CRCL. Our 12-month price target of \$96 is based on 35.0x Q5-Q8 P/E.

Risks: Downside risks: Ecosystem growth slows; as a result of a weaker crypto market backdrop; Market share gains from USDT not continuing; Coinbase de-emphasizes USDC; and competition from other stable coins. Upside risks: favorable crypto regulation; further increases in crypto market cap; acceleration in market share gains from USDT; higher for longer rates benefiting reserve income.

<table><tr><td>CRCL</td><td>12m Price Target: $96.00</td><td>Price: $64.62</td><td>Upside: 48.6%</td></tr></table>

<table><tr><td>Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $17.5bn</td><td>Revenue ($ mn)</td><td>1,083.0</td><td>1,201.5</td><td>1,660.1</td><td>2,191.1</td></tr><tr><td>3m ADTV: $1.4bn</td><td>EPS ($)</td><td>1.33</td><td>1.34</td><td>2.46</td><td>3.67</td></tr><tr><td>United States</td><td>P/E (X)</td><td>101.4</td><td>48.4</td><td>26.3</td><td>17.6</td></tr><tr><td>Americas Banks and Advisors</td><td>P/B (X)</td><td>4.6</td><td>4.2</td><td>3.7</td><td>3.3</td></tr><tr><td>M&amp;A Rank: 3</td><td>ROA (%)</td><td>0.6</td><td>0.4</td><td>0.5</td><td>0.5</td></tr><tr><td></td><td>ROE (%)</td><td>18.8</td><td>10.1</td><td>16.5</td><td>21.8</td></tr><tr><td></td><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS ($)</td><td>0.32</td><td>0.30</td><td>0.32</td><td>0.39</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 2 Jul 2026 close.

## Disclosure Appendix

## Reg AC

I, James Yaro, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: James Yaro GS & Co. LLC, Matthew Weng GS & Co. LLC, Divyam Harlalka GS India SPL, Lokesh Kumar Sangewar GS India SPL.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for

equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
