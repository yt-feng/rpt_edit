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
## Economic Insights

Economics - Global

## NOM Investment Forum Asia 2026: A recap of our macro views and what investors think

We hosted our annual flagship Asian investment forum in Singapore over 2-5 June, with our Global Economic Outlook panel held on 3 June, where our chief economists presented their macro outlooks. We also polled the audience on several topics and present the results of our nine polling questions.

## Summary of chief economists' presentations

## Global (Rob Subbaraman)

- Our global economic outlook features increasing divergence with economies marching to different tunes. The US economy is the clear outperformer in the DM world, while many EM economies are struggling from the commodity price surge while benefitting little from the AI boom.  
- Even if the Strait of Hormuz (SoH) reopens soon, there will remain significant inertia when it comes to global supply-side disruptions. Excluding the period during the pandemic, the NY Fed's Global Supply Chain Pressure Index (GSCPI) has risen to its highest level since 1998, and during the pandemic, US CPI inflation peaked six months after the GSCPI peaked in December 2021.  
- The world has been facing a series of supply shocks, and while the media focuses on the oil price shock, it is actually much broader than that. There is a trio of energy, chip and, increasingly, food price shocks that is driving this divergence in economic performance.  
- Broadly speaking, we expect central banks to hike by less than market pricing, as we expect the “stag” part of stagflation to be more serious than during the last 2021-22 global inflation surge, since, unlike the post-Covid inflation surge, there is no post-pandemic, pent-up demand and far less fiscal and monetary stimulus. That said, there could be a few exceptions, notably the US (AI boom and more pricing power muscle memory, given inflation has exceeded the Fed’s target for five years), and Japan (monetary policy remains exceptionally loose and risks of fiscal dominance).  
- Another reason why we generally expect less price pass-through to underlying inflation this time around is because of the China shock 2.0, which is intensifying China-led price competition in Asia and Europe.  
- Time snapshots of bond markets at the end of ultra-low policy rates (December 2021), the end of the global rate hiking cycle (September 2023), the start of the US-Iran war (end-February 2026) and end-May 2026 all highlight rises in sovereign bond yields and steepening curves, which reflect: 1) rising inflation and an erosion of central bank independence; 2) continued large budget deficits and rising public debt ratios; and 3) massive global government bond issuance at a time when mega-tech firms are also starting to issue debt.  
- These four snapshots highlight the fragility in global bond markets and warn that bond market vigilantes could be reawakening. These four snapshots also reveal how China has moved from one of the highest yielding sovereigns to now the lowest yielding while, in terms of the yield curve, Japan has moved from the flattest to the steepest.

## United States (David Seif)

- The US is set to grow above trend and at a faster rate than other DM countries.  
- The US is capturing the lion's share of the AI infrastructure investment, likely raising GDP growth by a full percentage point.  
• Although the Iran war is a negative for the US, it is less of a negative than for most DM

## Research Analysts

## Global Economics

Rob Subbaraman - NSL

rob.subbaraman@NOM.com

+65 6433 6548

George Buckley - Nlplc

george.buckley@NOM.com

+44 (0) 20 7102 1800

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

Kyohei Morita - NSC

kyohei.morita@NOM.com

+81 3 6703 1395

Euben Paracuelles - NSL

euben.paracuelles@NOM.com

+65 6433 6956

David Seif - NSI

david.seif@NOM.com

+1 212 667 9180

Sonal Varma - NSL

sonal.varma@NOM.com

+65 6433 6527

Si Ying Toh, CFA - NSL

siying.toh@NOM.com

+65 6433 6666

countries, because North America has a separate natural gas market and because the US is a net exporter of oil.

- Core inflation is rising in the US due to “software goods,” which are related to the AI capex boom (note that Steve Miran says its weighting in the PCE is too high).  
- Trimmed-mean PCE, which Chair Warsh favors, has historically lagged core PCE in responding to changes in inflation trends.  
- Warsh likely disagrees with most of the FOMC in that he is more dovish, which will likely limit his ability to have the same level of control over monetary policy as his predecessors.  
• We expect the Fed to keep rates steady through the end of 2027 at least, and we see roughly equal chances of a hike and a cut.

## Euro area (George Buckley)

- The stagflationary revisions to consensus forecasts for the euro area have been among the largest for DM economies since the Iran war began (i.e., weaker GDP, stronger inflation).  
- Rates markets are still strongly bound by oil prices. Current levels (\$95/bbl) are consistent with our view of two ECB rate hikes and one BoE hike this year. We think the BoE will more than unwind that hike by rate cuts in H2 2027.  
- For various reasons the latest inflation shock looks very different to 2022. Notably, monetary and fiscal policy are tighter now (note Germany's fiscal largesse is being offset by tightening elsewhere), labour markets are looser, there is more economic slack and inflation was better behaved ahead of the Iran war than Russia/Ukraine.  
- This justifies a recalibration of monetary policy (only modest tightening) rather than full-on hiking cycles. Residual stickiness in services inflation supports this need for some tightening.  
- Our audience poll suggests that more respondents thought that European central banks should be worried about the downside threat from the Iran war to growth (70%) than the upside risks to inflation (30%), providing further support to the need for only cautious monetary tightening.

## Japan (Kyohei Morita)

- Assuming the Middle East (ME) tensions do not last into H2 2026 and the Strait of Hormuz gradually reopens, we believe Japan's economy will remain on a recovery path after contracting in Q2 2026.  
- Upstream inflation induced by the ME tensions should translate into CPI inflation with a lag of around six months. We expect core CPI inflation (less fresh food) to accelerate, peaking at 3.6% y-o-y in Q1 2027.  
- Shunto (spring wage negotiations) for 2026 is confirming that wage hikes are growing more harmonized and sustainable. Together with companies' efforts to reduce labor dependence via labor saving investment, wage hikes will further increase sustainability, in our view.  
- With underlying inflation inching up to 2%, we expect the BOJ to hike in June and December 2026, and June 2027, bringing the policy rate to 1.5% within the estimated range of the neutral rate.  
- The Takaichi government will most likely publish the "Basic Policy on Economic and Fiscal Management and Reform" in June, and in this report, the government will likely show its commitment to fiscal sustainability and also to implement expansionary fiscal policy, in line with an increase in tax revenue.

## China (Ting Lu)

\- China's big AI boom does support China's economy and stock markets. AI drives the economy mainly through fixed asset investment (FAI) with AI-linked capex contributing around 0.3pp to GDP growth in 2026. As Beijing is pushing an ambitious “AI+” strategy by aiming to integrate AI into 90% of the economy, we expect AI capex to rise further and raise productivity. However, this positive impact should not be overstated.

As China is still heavily reliant on imports of advanced chips for running its AI models and its data centres, part of its AI investment will leak to other economies. Also, surging chip prices worsen its terms of trade and suppress China's net exports.

\- While China has been experiencing an AI boom, the severe property bust has persisted. In the decade before 2021, the property sector was China's single largest growth pillar, contributing around $25\%$ of GDP, $38\%$ of fiscal revenue and $60\%$ of household wealth at the peak in 2021. Then came the dramatic bust, with new home sales values of the top 100 developers slumping by $72.7\%$ in 2021-25 and falling by $19.7\%$ y-o-y in the first four months of 2026. This collapse has sapped domestic demand, damaged the balance sheets of governments, corporates and households, and resulted in a huge amount of bad debt.

\- The AI boom will also likely worsen the two existing intertwined K-shapes, which in turn could dent aggregate demand. The property bust since 2021 has led to 14mn migrant workers losing their construction jobs. As home prices have dropped much more in low-tier cities than in large cities, and as those low-paid migrant workers tended to buy homes in their hometowns in low-tier cities, the property bust increased income and wealth inequality. The AI boom further split the social fabric into two classes: those that benefit from the boom on their talents, well protected jobs and wealth versus those that are fully or partly replaced by AI.

\- There is another K-shape from a geographic perspective. While the 2000-21 property boom was a broad-based wealth creator, the AI supercycle is a centralizing event. Success in this new AI era is gated by massive compute density, data pools and top talents, which are highly concentrated in a handful of existing top-tier cities. A few of those “smart” cities take much of the national gain of AI development and even siphoning resources from the rest of the country.

\- The two K-shapes could be reinforcing each other. As the top talent and financial resources flow to top-tier smart cities, displaced workers tend to be crowded out of those cities and are forced into the gig economy or low-end service sectors, driving down wages in legacy cities and worsening service sector deflation. The rapid demographic shift from the aging and falling population, a surge in college education and a highly unequal social welfare system could further reinforce these two K-shapes.

\- For both markets and Beijing's policymakers, they cannot assume the new AI economy will cure China's economic woes caused mainly by the property bust. Beijing also needs to closely track the divergence between the upper arms and lower arms of the two K-shapes and take some precautionary steps to prevent the gaps from becoming excessive. Despite the AI boom, Beijing may still eventually be impelled to step up policy measures to clean up the mess in the property sector and speed up fiscal reforms to support those cities that have been left behind.

## Asia ex-Japan (Sonal Varma)

\- Asia's outlook is being driven by two themes: AI revolution and energy prices. Together, these themes are likely to create a North-South divide, since AI is benefiting North Asian economies, while higher energy prices will hurt South/Southeast Asia most. We expect growth outperformance in Singapore, Taiwan and Malaysia, while Thailand and the Philippines are likely to lag.

\- South Korea remains one of the largest beneficiaries of the AI upcycle. We expect the AI-related terms-of-trade benefit to boost Korea's current account surplus to a record high of $15.5\%$ of GDP in 2026, but we see more limited spillovers to the domestic economy, leading to K-shaped growth. We expect the BOK to raise rates by 75bp to $3.25\%$ by Q1 2027, less than market pricing, due to a more gradual rise in private consumption.

\- In India, we expect the RBI's monetary policy response to be reactive. Low underlying inflation and uncertainty on the inflation impact (of both the ongoing energy shock and the incoming El Niño) should keep the RBI patient for now. On the other hand, fiscal risks are likely to materialize, as India has mounted a fiscal defense to the energy shock, which we expect to worsen the government's fiscal deficit to $4.6\%$ of GDP in FY27 (versus the $4.3\%$ budget target). Non-monetary measures to manage the currency are more likely to narrow the current account deficit and boost net capital inflows.

\- Asia is being rewired. The transition from a unipolar to a multipolar world order, intense China competition and the AI revolution are structural shifts that require a reshaping of Asia's growth model. In our anchor report, we dive into eleven themes that will create winners and losers at the country, industry and company levels.

## ASEAN (Euben Paracuelles)

- The bifurcated economic outlook in ASEAN is continuing: we still see Singapore and Malaysia as resilient, while Indonesia, the Philippines and Thailand are looking increasingly vulnerable. This divide is only worsened by the war in Iran.  
- We expect 2026 growth in both in Singapore and Malaysia to be above potential for an impressive third year in a row, driven not only by the tech supercycle but also by other domestic drivers, such as infrastructure implementation, progress on the Johor-Singapore special economic zone and strong labor market conditions.  
- Among the laggards, Indonesia faces worsening balance-of-payments pressures, due to widening current account deficits and high policy uncertainty. In the Philippines, political risks are also rising, with the impeachment trial of VP Duterte. In Thailand, structural constraints are more binding, particularly deteriorating competitiveness.  
- We still expect additional rate hikes of 75bp by BSP – as inflation remains above target – and another 25bp by BI in response to FX weakness. We expect a 25bp hike by BNM in Q4 to pre-empt a buildup in financial imbalance risks. In contrast, we see BOT leaving its policy rate unchanged, given growth concerns.

## Results of polling questions to the audience

A large majority of respondents expect the Fed to fall behind the curve: Most respondents (79%) expect the Fed to fall behind the curve this year (Fig. 1), with a majority expecting the Fed to stay on hold through end-2026. Among respondents who expect the Fed to tweak policy, risks are clearly skewed towards hikes rather than cuts. Most of the respondents who leaned towards tighter Fed policy expect only one 25bp rate hike this year (Fig. 2).

An AI-led stock market correction is unlikely in the near term: A majority of respondents expect a major AI-led US S&P500 correction within the next 12 months. Nonetheless, a sizeable one-third of respondents believe in the resilience of the AI-led stock market boom, and do not see a correction within the next 12 months, while among those that do see a major correction, the majority expect it only in 6-12 months, rather than in the near term (Fig. 3).

Europe's central banks are expected to focus more on growth than inflation: A majority of respondents (almost $70\%$ ) hold a dovish view, believing that Europe's central banks should be more concerned about the downside growth impact of the Iran war, as opposed to the upside inflationary impact (Fig. 4).

Japan's monetary policy: Similar to what is thought about the Fed, most respondents (69%) expect the BOJ to fall behind the curve (Fig. 5), although interestingly, the share is lower than that of the Fed (79%). Consistent with this view, a majority (52%) expect only one 25bp BOJ rate hike through end-2026 (Fig. 6).

China's 10-year CGB yield: A majority of respondents (64%) believe that, at the end of 2026, the 10-year CGB yield will be lower than the current, already-low $1.72\%$ , with the most popular option being $1.60 - 1.70\%$ (Fig. 7).

India's monetary policy: Most respondents (71%) expect the RBI to hike rates over the next 12 months, though they expect a gradual hiking cycle rather than an aggressive one, with cumulative hikes of 25bp to 50bp (i.e., 1-2 hikes) being the most popular option (Fig. 8).

Indonesia's

[中间内容因长度限制已省略]

ken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved.
"""
