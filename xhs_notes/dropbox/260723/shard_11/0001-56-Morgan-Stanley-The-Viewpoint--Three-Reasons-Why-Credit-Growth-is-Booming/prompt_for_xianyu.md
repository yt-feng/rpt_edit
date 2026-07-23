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
As non-tech capex and non-tech exports are now picking up, improving labour market conditions are lifting household loan growth as well.

As the capex super-cycle continues, we see Asia ex-China bank credit growth staying strong.

In this report, we delve into which segments and geographies are driving stronger credit growth in Asia ex China.

Exhibit 1: Credit growth in Asia ex China at a 18-year high  
![](images/c175c52d378f4f60ae8fdcb0aebffc69c5e3d75d143dac749fe9c92baa457b1b.jpg)  
Source: CEIC, Haver, MS, Note: We calculate the Asia ex China aggregate by weighing it using nominal annual outstanding bank credit in USD terms.

Details

Bank credit is still the most important source of macro funding by far: In Asia, the banking sector remains one of the most important providers of credit, considering that the corporate bond and private credit markets are not mature yet. In EM Asia economies, bank and non-bank finance companies account for over 60% of the flow of resources to the commercial sector. Outside of internal accruals, the order of sources of macro funding is first loans from banks plus the non-bank finance sector, followed by equity issuance at a distant second, and then an even smaller segment is corporate bond issuance.

## What is driving this strong credit demand?

The strongest credit growth since the 2000s: Asia ex-China nominal credit growth picked up to 8.5%Y in May-26, the highest level in 18 years. On a real basis, deflated by the GDP deflator, credit growth in Asia ex-China has also been rising to 6.3%Y, also an 18-year high. The strength has been broad-based with multiple economies seeing cyclical highs in credit growth.

We see three key drivers underpinning this acceleration:

1. Capex activity and trade are booming – lifting industrial production growth to close to the highs seen last during 2000s: As we have been highlighting, Asia is entering its strongest industrial cycle since the 2000s. This is underpinned by a sustained, multi-year rise in capex across AI and AI-related digital infrastructure spending, energy, defense and industrial supply chains. Our preferred high frequency indicators to track capex momentum – capital goods imports growth – has continued to accelerate to 33%Y 3MMA in May, the highest since 2004. Export momentum has also continued to broaden from semis exports, as there has been a sustained pickup in capital and intermediate goods as well. Reflecting the strength in exports and capex, Asia’s nominal industrial production was also at an 18-year high of 12.5%Y in May.

2. PPI inflation is increasing demand for working capital: Asia ex-China PPI inflation has risen to a 4-year high of 9.0%Y, as higher oil and broader commodity prices have pushed up commodity PPI. Higher upstream prices and improving demand conditions have in turn begun to filter through to producer prices in downstream segments. Reflecting this, Asia ex-China non-commodity PPI has also risen to a 3.5-year high of 4.3%. With the pickup in real activity and inflation lifting Asia ex-China's nominal industrial production growth, the price pressures are in turn increasing working capital loan demand across the supply chain and for end-users.

3. As non-tech capex and exports help job creation, consumer credit demand is also picking up: We have previously highlighted the limited positive spillover from tech exports to the labour market due to their smaller share in overall exports and their capital-intensive nature. However, as the recovery is broadening out to non-tech capex and exports as well, we are beginning to see an uplift in overall job creation, which is beginning to boost consumption and consumer credit demand. Indeed, as Asia ex China retail sales growth has improved in recent months, household loan growth has also moved higher, though it remains within the historical range.

Exhibit 2: Asia ex China's credit growth has accelerated to $8.5\%$ Y, the highest in 18 years  
![](images/e245382c40e6839126add988201ebe8726a697f292ab0b7cc74fd867e54c24d2.jpg)  
Source: CEIC, Haver, MS, Note: We calculate the Asia ex China aggregate by weighing it using nominal annual outstanding bank credit in USD terms.

Exhibit 3: Meanwhile China, with its counter-cyclical growth model, is slowing leverage  
![](images/b586813589921002e1be72098e202c07d38256870167bd32d121a91ee24216a0.jpg)  
Exhibit 4: Real bank credit growth (deflated by GDP deflator) is also at the highest since 2008  
Source: CEIC, Haver, MS

![](images/428c18617c496126f1ea24868d48a919218b791ce7be3e55d6ddef747477f946.jpg)

Source: CEIC, Haver, MS, Note: Real credit growth is calculated by adjusting nominal credit growth with the GDP deflator. For Korea and Taiwan, the 2025 average GDP deflator is used in Jan-May 26 as reported 1Q26 deflators were significantly boosted by a sharp rise in semiconductor price. For the remaining economies, the 1Q26 GDP deflator is used for Apr-26 and May-26 due to data availability issue. Credit growth is in local currency terms. We calculate the Asia ex China aggregate by weighing it using nominal annual outstanding bank credit in USD terms.

Exhibit 5: Nominal industrial production growth has also risen to the highest levels since 2008 (excluding Covid base effects), adding to corporate credit demand  
![](images/dda264d16534e64561d55f0f0cffc9c582f1566b7a1bd120504424360459c7ad.jpg)  
Source: CEIC, Haver, MS, Note: Nominal industrial production is calculated by adding PPI growth to real industrial production growth, For India WPI is used.

## Which segments are growing?

Corporate sector credit demand is leading the cycle: To the extent that the current cycle has been primarily capex-driven so far, corporate credit demand has been growing faster than loans to households. Corporate loan growth has accelerated to the highest in 18 years. This is also as bank credit remains the largest source of debt funding for the corporate sector in Asia, as the corporate bond market is still not as mature as the US. According to OECD, debt securities on average make up just 14% of total debt for non-financial firms in Asian economies.

Exhibit 6: Bank credit remains the largest source of debt funding for the corporate sector in Asia  
![](images/9d7d4e125ef69acde2d37633144628a1c61a9573cb5078e413d133ec0dd65029.jpg)  
Source: OECD Asia Capital Market Report, MS

Exhibit 7: The industrial and capex super-cycle is driving corporate sector credit demand  
![](images/addb4795c09bdf6b5067b7dd15a90b9715fc5960ef1f9958c61985a71e410088.jpg)  
Source: CEIC, Haver, MS estimate

Household lending also recovering: As positive spillover effects to labour market conditions from the export and capex cycles filter through, and as energy-related headwinds gradually ease, Asia ex China's consumption momentum has shown signs of improvement in recent months – led by India, Korea, Taiwan and to some extent Japan. Retail sales in Asia ex China ex India have averaged 4% year-to-date, vs. 2.8% in 2025, while India's vehicle registrations (a consumption proxy) continued to record double-digit growth in June. Consequently, household loan growth bottomed in Sep-25 at 5.6% and gradually improved to 6.6% in May-26, albeit still within the historical range.

Exhibit 8: Household loans are also recovering  
![](images/161dff9ac2f882545b5771ab680092b6ae1ca54f8c4c59a88c698c5ca3c1b9ce.jpg)  
Source: CEIC, Haver, MS

# Which Asia ex-China economies are showing the strongest growth?

Broad-based pickup across Asia ex-China: India, Japan, Singapore, Hong Kong, Australia and Taiwan have seen the biggest accelerations in loan growth. Korea has been an exception as corporate capex is largely funded from internal accruals. Thailand is the only economy in the group that has weak credit growth given an uneven expansion so far in which households have continued to delever.

Exhibit 9: A broad-based pickup in loan growth in Asia ex China

![](images/2c87baecbadb49ed9509abd06301e2dae0ac0894a391d804d7af808f0da64779.jpg)  
Source: CEIC, Haver, MS

India: The sustained strength in domestic demand conditions since 2H25, rising WPI in recent months and RBI's regulatory easing measures since 2025 have meant that credit growth has now accelerated to the strongest level since 2009–2012. The strength has been broad-based across segments, but with particular momentum driven by the corporate sector – which has picked up to 18.3%Y in May, the highest since 2012. Household loan growth has also sustained above 15%Y for the fourth consecutive month, in part also benefiting from the recovery in unsecured personal lending growth amid RBI regulatory easing (see India Financials: Unsecured Personal Loan Growth Improved to 12% YoY in F4Q26 and India – Banks: Tracking Credit Growth – May 2026). Additionally, NBFCs retail loan growth has also strengthened to 19.5% YoY (vs. 14.9% in May 2025) (see India Financials: Tracking NBFC Credit Growth – May 2026). We expect overall credit demand to remain strong, supported by capex and exports growth, and household loan growth to be supported by housing and strength in discretionary consumption.

Japan: Loan growth has accelerated to a new high of 7%Y since 1999 (when we have available data). Within this, corporate loan growth has picked up meaningfully to 8.4%Y in May, pushing up overall loan growth. Going forward, our Japan financials analyst Mia Nagasaka continues to expect improving loan growth for Japanese banks as corporate capex demand, supply chain rebuilding and digital transformation spending contribute to firm demand for funds. She expects healthy asset content and ample reserve capacity will keep credit costs at manageable level (see Japan: Continue to Favor Bank Stocks in

Positive Cycle for Earnings and Returns).

Korea: Korea's credit growth has remained soft. While capex growth is strong, it has largely been driven by large companies which have strong cashflows and hence this capex has been largely funded through internal accruals. At a macro level, Korea's strong export growth has lifted its current account surplus to $9.1\%$ of GDP, the highest since 1998. Our Korea financials analyst Joon Seok notes that credit growth will continue to be primarily driven by the corporate sector, as household loan growth will be constrained by a policy which has set a cap of $1.5\%$ Y growth for loans to households.

Indonesia: Overall loan growth has been improving since the trough in Jul-25 but has remained broadly within the historical range. Of note, the key driver to improving loan growth has been investment loans. This in turn has been supported by loans provided to village cooperatives. In other words, lending is being supported by a policy push rather than by the private sector. Meanwhile, consumer loan growth has continued to decelerate amid weak sentiment. Given the lack of a private capex cycle, the pass-through of rate hikes as well as tight liquidity conditions, our Indonesia financials analyst Selvie Jusman expects loan growth to stabilise.

Australia: Overall loan growth has been strong at 8%Y in May, driven by loans to corporates growing at 9.5%Y and loans to households growing at 6.7%. However, given the large share of housing related loans in overall bank loans in Australia, the housing market outlook has a significant bearing on overall loan growth. In this context, our Australia economist Chris Read believes the tax changes to negative gearing and capital gains fundamentally shift the investment case for property in Australia. He expects a 5-10% decline in national house prices given headwinds from rates, taxes, and a slowing economy. As housing credit growth tends to lag prices by 6 months on average, it should slow with a delay. Our Australia banks analyst Richard Wiles expects system mortgage growth to slow to 3% in FY27, vs. 6% currently (see Australia Banks: A Tough Day).

Hong Kong and Singapore: Loan growth in Hong Kong and Singapore is also picking up, and as our Hong Kong and ASEAN financials analyst Nick Lord notes, this has been driven by non-resident or cross-border lending. Corporate lending across multiple sectors has been consistently positive, confirming that robust capex and trade activities are likely the key drivers. In Hong Kong, our property analyst Praveen Choudhary sees the recovery of the market sustaining and broadening into office and retail. This should also be supportive of overall loan growth in 2H26.

Exhibit 10: Sustained strength in domestic demand, rising WPI and RBI's regulatory easing measures, have meant credit growth has accelerated to the strongest level since 2009–2012 on a broad base  
![](images/3c1b1281c16d7051c4a39ca70e547a336ee4eb38f893acf5aad41de99511df5d.jpg)  
Source: CEIC, Haver, MS

Exhibit 11: In Japan, corporate loan growth picked up to 8.4%Y in May, pushing up overall loan growth  
![](images/4a2ed2cf4a16a9645f0044543bb3d83b7a9ac35887171f9144805f2ff1c9ada0.jpg)  
Source: CEIC, Haver, MS

Exhibit 12: In Korea, corporate loan growth is recovering, while household loan growth is constrained by a loan growth cap of 1.5%Y  
![](images/b6cf1ea13042b7db71aaf77b3def65c45a739fc3d48c6de24c7c51dea5231bbf.jpg)  
Source: CEIC, Haver, MS

Exhibit 13: In Indonesia, loan growth acceleration has been driven by policy directives rather than private sector demand  
![](images/63c1da294d5eddb53ec085105d5511c00b62e6b4d387ca795b3cf33886ec3426.jpg)  
Source: CEIC, Haver, MS

Exhibit 14: In Australia, housing tax policy changes will continue to weigh on overall loan growth  
![](images/09a42a9a338f2e643dbe44dc5619ab1e25268999539e465ac15d341c598fb23d.jpg)  
Source: CEIC, Haver, MS

Exhibit 15: Hong Kong loan growth has been driven more by trade financing and loans for use outside of Hong Kong  
![](images/2eba881c7e66644ed7d7917cce779efd24dbe09ec222ccd47832b58d5bfc3630.jpg)  
Source: CEIC, Haver, MS

Exhibit 16: Similarly, loans to non-residents have been the bigger driver of headline loan growth in Singapore  
![](images/83e72ac00234aea410c7abd7a231e1c6680fe43bfc8f63b571c92b0bafdb0f8a.jpg)  
Source: CEIC, Haver, MS

Exhibit 17: Strong growth in corporate credit in Malaysia  
![](images/e553265d74e4f4ef11007bf6a2d757dae9f4c849a00161c89a2362d379f6dd7f.jpg)  
Source: CEIC, Haver, MS

# China – Why is credit growth decelerating?

Counter-cyclical growth model at play: Over the years China has been managing its growth model in a counter-cyclical manner, juxtaposed against the trend in exports. Moreover, the sharp rise in public debt as well as total debt since Covid has meant that policy-makers are keen to use the opportunity presented by the strength in exports to withdraw policy stimulus (i.e. cut leverage). Our China financials analyst Richard Xu notes that “the transition toward more sustainable debt growth remains underway”.

Exhibit 18: Households have led the loan growth slowdown, followed by a slowing in corporate loans  
![](images/87f61a00576c2a03c47b9ac98aa5a2112c8ddafed873a4a617f1e833363d55c5.jpg)  
Source: CEIC, Haver, MS

Exhibit 19: In China, the counter-cyclical growth model is leading to slowing credit growth  
![](images/4a330172e733acc5483ebe66ffc8ead55ebb215f67a9865a4f88752561f32edd.jpg)  
Source: CEIC, Haver, MS

Households led the slowdown, corporate sector following: China's overall loan growth has further decelerated from 6.2%Y in Dec-25 to 5.1% in Jun-26. This has also been mirrored in total social financing, which has decelerated from 8.5%Y to 7.5% over the same period. Within loans, the subdued property market has meant that mortgage loans have been the weakest segment. Moreover, given the disinflationary pressures and subdued momentum in wage growth, consumers have been cutting back on non-mortgage retail loans as well. Finally, industrial loan growth has been holding up better than household loan growth. Against th

[中间内容因长度限制已省略]

P-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 14-9169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
