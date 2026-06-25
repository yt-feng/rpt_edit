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
# Global Metals & Mining: Met Coal Singapore Conference: China mine disruption impact 15-20Mt, prices could test US\$280/t in 2H.

We recently attended the Singapore Ferrous week which included participating in the MySteel Global Iron Ore and S&P Coking Coal Conferences in Singapore where we met with physical and financial iron ore and coking coal traders, iron ore and coking coal producers, and steel mills. We highlight the key takeaways from our conversations below.

The Shanxi accident - 15-20Mt lost, Australian-China prices at parity for first time in >4yrs

Structural reset lower: Discussions across both conferences were dominated by the recent Shanxi coal accident, with the focus on the headline volume loss and also the potential structural supply reset that may follow. Estimates for lost production this year ranged from 15-20Mt (up to end of August), or \~5% of annual domestic consumption, but the key issue is how capacity fully restarts. Feedback suggests 50-55Mt still remains offline, and there is a growing expectation that not all of this capacity will come back. Traders suggest some mines may return at only 70-80% of capacity versus prior levels of \~110% in certain cases. With increased regulatory scrutiny and officials under investigation for oversight failures, there is an increased likelihood of a structural reset lower in production output, and a shift higher in the domestic cost curve, noting these mines are 1-1.5km deep in some cases.

\- High strength (CSR) coal lost: The lost supply is primarily high strength (CSR) low-vol coal that Mongolia and Russia cannot replicate. This has forced domestic prices higher, positioning Australian coal at parity to domestic prices. China CFR (portside) prices have risen \~US\$40/t since the accident (Exhibit 2), and spot prices suggest Australian coal is now US\$5/t cheaper than domestic coals (see Exhibit 1); the first time in several years (Exhibit 3). Traders highlighted that Tier 1 and Tier 2 (and PCI) Australian coals are increasingly being diverted to China, with rising spot liquidity in the prime hard index potentially lifting prices to US\$260-280/t in 2H'26 vs spot of US\$244/t. With China and Australian prices trading at parity, it will improve the overall price realisation for miners as some have been selling coal directly into China to avoid spot cargoes on the Australian exchange, as this may have previously pulled down Australian benchmark price that sets the price for term contracts.

■ Seasonal slowdown to help offset margin pressure: Higher coal prices are

Matt Greene  
+44(20)7051-0489 |  
matt.greene@gs.com  
GS International

Paul Young  
+61(2)9321-8302 |  
paul.young1@gs.com  
GS Australia Pty Ltd

Chris Bulgin  
+61(2)9321-8936 | chris.bulgin@gs.com  
GS Australia Pty Ltd

Riccardo D'Agata +44(20)7051-0958 | riccardo.dagata@gs.com GS International

expected to pressure steel mill margins, but the response is likely to be measured rather than reactive, with mills remaining cautious on restocking and potentially using the seasonal July/Aug maintenance period to curtail output. This could mean that restocking takes place in September, when Indian mills returns post monsoon, which may tighten the premium coal market. Prime mid-vol coals (important for Indian blends) is already tight due to Australian supply challenges in the last year and now prime low-vol coals could also tighten as China leans on imports to offset the domestic loss. Both of these coals contribute to setting the Australian FOB price index.

\- Could the US help offset tightness? Cargoes of US coal recently left for China in the last week, despite the 28% tariff; suggesting some traders are perhaps taking a view that China may ease tariffs on US coals if seaborne prices remain elevated. The US previously supplied \~10Mtpa before tariffs were introduced last year. A removal/reduction of tariffs could redirect US flows away from India/Brazil and potentially ease spot activity in the Australian index. It would also impact pricing for Indian and Brazilian mills that have been purchasing US coals at competitive prices since the tariff was introduced, as this flow may redirect to Chinese buyers at a higher price.

## India imports to grow strongly but remain focused on lean coal blends and price

India driving coal incremental coal demand: India imports around 80Mtpa of coking coals, and this is expected to increase to >120Mtpa (Exhibit 9). The demand mix remains highly supportive for blast furnace steelmaking, with infrastructure and construction accounting for around 64% of steel demand versus a global average closer to 52% according to commentary from one steel producer. With limited scrap availability and insufficient domestic gas, India remains structurally tied to BF/BOF production, underpinning ongoing demand for both iron ore and coking coal.

India's role in price formation: Several panellists argued that India is increasingly the centre of PLV price formation, particularly with Chinese CFR at times trading well below index levels. However, India's pricing power is constrained by its heavy reliance on term contracts. Spot participation is still limited, with many buyers keeping only \~10% of volumes open, largely for security of supply reasons and because spot market liquidity remains thin. That means India can influence the market through demand, but not always through active price discovery. A structural constraint is market infrastructure; India's port, stockyard and blending ecosystem still lacks the depth of China's coastal market, limiting liquidity and the development of a deeper spot pricing mechanism. A trader suggested only \~10 buyers would participate in spot onshore trades in India, versus >100 in China. The read through is that India can still drive episodic price spikes, particularly post-monsoon, but the pricing is likely to swing back to China whenever there is a major supply shock, as we are currently witnessing.

Stamp charging technology enabling leaner coal blends: Every Indian mill we spoke with is looking at greater substitution of lower-quality coals, using more sophisticated, leaner blending practices to increase the share of Tier 2, semi-soft and weaker coals (see our previous report on the shift in coal blends). The shift in blend can raise the proportion of domestic and medium coking coals in blends from below 10% to around 35-55%, while still meeting blast furnace coke specifications and delivering cost savings of US\$10-15/t of coal or US\$15-20/t of met coke. This shift towards greater diversification across coal types and geographies is expected to continue, with domestic coals also gaining share over the next 2-5 years as integrated mills and miners invest in wash plant upgrades to reduce ash content. However, with India currently producing only \~5Mt of commercial met coal, plans to double output would leave the country structurally reliant on seaborne imports to support steel growth.

## Australia cost pressure (royalties, fuel, labour, geology inflation) and declining exports due to permitting delays and mine depletion

\- Rising structural cost pressures: Increasing stripping ratios, deeper pits and declining reserve quality are lifting operating costs, and pushing the QLD coal miners higher on the global cost curve. Fuel presents a cost headwind, with diesel at 10-20% of opex and highly price sensitive, fuel inflation has already added US\$8-12/t to costs. QLD operating costs are already 30-40% above early 2022 levels (when the royalties were introduced), with diesel and labour pressuring costs further.

\- Constrained supply response and declining flexibility: Australian exports have fallen from \~220Mt to \~195Mt over the past decade, and could fall a further 10Mt by 2030 due to mine depletion (e.g. Oaky Creek closure) which will offset mine restarts (e.g Moranbah North, Grosvenor and North Goonyella). There is limited supply elasticity amid cost inflation, royalties and regulatory constraints. Lengthy permitting (>5 years for existing mine extensions) and higher QLD royalties continue to weigh on investment and supply responsiveness, and there appeared to be some clear frustration by several stakeholders on the uncompetitiveness of QLD royalties.

Structural cost inflation pushing up the cost curve: Rising stripping ratios, deeper pits and declining reserve quality increasing operating complexity. Productivity challenges and geological depletion are further pushing assets higher on the global cost curve. One panellist suggested \~10Mt of Australian production could deplete by 2030 with little greenfield replacement currently visible.

## Mongolian and Russian supply increasing mitigates supply risk and further demand requirements

■ Strong supply growth into China: A key offset to tightening conditions elsewhere is the continued growth of Mongolian and Russian coal supply into China. Mongolia is already exporting roughly 80-90Mtpa (raw met coal, 50-55Mt washed) into China and several speakers expect volumes to exceed this level in the near term. The upgrade to the Tavantolgoi railway is scheduled for completion in 2027 adding \~30Mt of annual capacity while significantly reducing logistics costs from \$30-35/t to \$8-12/t, which could unlock marginal tonnes.

Russia ramping with policy support: Russian exports are also rising as payment mechanisms normalise and producers benefit from government support, with major projects such as Elga continuing to ramp up. The Elga mine is currently operating at

20-25Mt, although can only wash 8Mt with the balance sold as unwashed coal (including some thermal) to China.

Exhibit 1: Based on spot FOB, China CFR and freight, we estimate the arb has opened, Australian imports are now \$5/t cheaper than China CFR and freight
HCC Aus-China arb at spot prices  
![](images/3df7f2ca3463f962a77ae7021e546e661a1ba160a3baca1309b93e86ed2b0dbc.jpg)  
Source: Bloomberg, Platts, GS Global Investment Research

Exhibit 2: The sharp rise in Chinese CFR has opened the import arb, making Australian coal competitive for the first time this year China HCC netback to Aus QLD vs. FOB price (spot)  
![](images/eee61aca00bc0b47730397d09c1097fd3915681798292f4edddcc785ef455475.jpg)  
Source: Company data, Bloomberg, Platts, GS Global Investment Research

Exhibit 3: Over the past 3-4 years, New entrants have led to lower Asian prices, with Australia remaining uncompetitive, to incentivise imports into China China HCC netback to Aus QLD vs. FOB price (spot)  
![](images/b889be57687eaa26efb5928fd32e23ef976b4cad710cbe230cac5a12d79b4e9e.jpg)  
Source: Bloomberg, Platts, GS Global Investment Research  
Exhibit 4: Seaborne coal freight rates have almost normalised to pre-war levels
Seaborne freight (\$/t) - Australia to China

![](images/de60053e8b527e816b060e7f561d216b58761ee70e15c6fb0c9eb346697c05b9.jpg)  
Source: Bloomberg, Platts, GS Global Investment Research

Exhibit 5: Australia remains a small share of China imports (\~7% in 2025), with Aus exports to China down materially from pre-2020  
Australia Coking Coal Export Volumes to China  
![](images/fbff6d92a9168fe973b17ca61be50d1de7e3ea7b1c11b47b5a9d6def7c87c718.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 6: Mongolian and Russian coal has almost fully replaced imports from Australia, despite total import growth  
China's coking coal imports - share by country  
![](images/890ea2b7dbc3d076f1b1993785164866ffe23253fb9b8b319f938dac6366e95f.jpg)  
Source: Trade data, GS Global Investment Research

Exhibit 7: China imports are dominated by Mongolia (\~50% in 2025), with 2026 volumes up \~70% YTD compared to the same period last year
China Coking Coal Import Volumes: Mongolia  
![](images/e1c1535bd90b92ff35ddf3b032afb9933c96bca75bebdeb1328494d4357a493e.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 8: Total Russian exports have increased \~6% compared to the same period last year
Total Russia Coking Coal Export Volumes  
![](images/6c8ccebc74db47b98090fac3fef4094804ddd4f89fa28ffbfd9f2bd0c97d8c2d.jpg)  
Source: Argus Media, Data compiled by GS Global Investment Research

Exhibit 9: India met coal imports (Mt annualised)  
![](images/ba0bff63a6706749666b762b97c763591d0aff17411e10437e29ac26abe07463.jpg)  
Source: Bloomberg, GS Global Investment Research

Global Coking Coal Prices  
Exhibit 10: Australian HCC, PCI and Semi-Soft prices  
![](images/e89d1178c6b7343810a9571513ee0672fd063a1bfb4c9eb883c8091594ec9347.jpg)  
Source: Bloomberg

Exhibit 11: Australia, US and China met coal prices  
![](images/efd0ed65cb4a637a26e320bf0f7f475684c3a7f27f043c27dfb20c21cf0584fd.jpg)  
Source: Bloomberg  
Australian Coal Supply

Exhibit 12: QLD Coal Exports from Abbott Point, Hay Point, Dalrymple Bay and Gladstone (Mt annualised)  
![](images/b5f4a205b4be7bf5a7807b02255e97ed28e7cea8fa30df9dddae4418f8685fee.jpg)  
Source: Gladstone Ports Corp, North Queensland Bulk Ports

Exhibit 13: Abbot Point (GLEN/Adani/QCoal) monthly exports (annualised)  
![](images/8cd5f58099b764152c2312f1ccc5fe31b851c232e69383b9067972c766f7d4ac.jpg)  
Source: North Queensland Bulk Ports

Exhibit 14: Hay Point (BHP) monthly exports (annualised)  
![](images/38d354c17854c613ccf45de06c60372d958fea3222e0b0f63e577d5115546eae.jpg)  
Source: North Queensland Bulk Ports

Exhibit 15: Dalrymple Bay (WHC/SMR/AAL) monthly exports (annualised)  
![](images/6f25cfb4eb2ce476dfb027b804b1b293c3ab365868fbdf613f1bedf80234429e.jpg)  
Source: North Queensland Bulk Ports

Exhibit 16: Gladstone (WHC) monthly exports (annualised)  
![](images/9e8357ea62bbb6a583635c23543b57af31af69f7257a0fb36c756156773e8e08.jpg)  
Source: Gladstone Ports Corp

## Disclosure Appendix

## Reg AC

We, Matt Greene, Paul Young, Chris Bulgin and Riccardo D'Agata, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Matt Greene GS International, Paul Young GS Australia Pty Ltd, Chris Bulgin GS Australia Pty Ltd, Riccardo D'Agata GS International.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
