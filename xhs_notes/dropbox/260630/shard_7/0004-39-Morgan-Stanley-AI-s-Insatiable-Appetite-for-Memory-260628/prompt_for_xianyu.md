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
June 28, 2026 03:00 PM GMT

Software Snippets | Europe

# AI's Insatiable Appetite for Memory

Important events in the world of Software & Services in the week ahead, and key MS research / stories from the past week.

## Key Takeaways

Micron blows past 3Q26 earnings expectations as agentic AI's demands rise (#Software)

■ Informa: Intersecting Growth, Quality, and Value (\*MS Research\*, #Informa)

SAP CEO: "there is a chance that in 3-4 years there is actually no one developing software inside SAP any more" (#Software, #SAP)

Springer Nature Tech Event - AI is driving process efficiencies in academic publishing (\*MS Research\*, #RELX, #Informa, #Wolters Kluwer)

1) Micron blows past 3Q26 earnings expectations as agentic AI's demands rise (#Software): US-listed memory and data storage company Micron (covered by Joe Moore) posted record numbers mid-week, as strong AI demand and soaring memory prices combined. Fiscal 3Q revenue was up nearly 350% y/y to \$41 billion, from c. \$9bn a year ago. The obvious explanation is the build-out of AI data centers, but the more interesting software read-through is what is changing inside the workloads themselves. AI is moving from one-off prompts and chat responses toward more agentic systems that plan, call tools, read documents, retain session history, spawn sub-agents and iterate toward an outcome. These are the increasingly sophisticated, end-to-end workflows. As AI becomes more persistent and more workflow-oriented, it needs more context to store and retrieve, and the market is increasingly debating whether this wave of memory demand is less cyclical than in the past and more structural - potentially evidenced by Micron's 16 signed long-term strategic customer agreements. Our global Semis colleagues, led by Shawn Kim, recently explored this topic in detail in Chipflation - Navigating A Memory Crisis.

Exhibit 1: Micron's y/y revenue growth has rapidly accelerated in recent quarters  
![](images/b293bc1604784e082dcdc7470c199bf677fee3c4455bbbeb1b769ba6ce303e27.jpg)  
Note: Micron's fiscal year ends August 31st. Source: Company data, MS

<table><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="2">George W Webb</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>George.Webb@morganstanley.com</td><td>+44 20 7425-2686</td></tr><tr><td colspan="2">Mark Hyatt</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Mark.Hyatt@morganstanley.com</td><td>+44 20 7677-3663</td></tr><tr><td colspan="2">William Richards</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>William.Richards1@morganstanley.com</td><td>+44 20 7425-0269</td></tr></table>

## TECHNOLOGY - SOFTWARE & SERVICES

Europe

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

2) Informa: Intersecting Growth, Quality, and Value (\*MS Research\*, #Informa): In an AI-saturated world where digital outreach risks losing authenticity, Informa's scale and leadership in B2B live events provide a differentiated platform for human connection and long-term revenue growth. This week we published a new sum-of-the-parts analysis reinforcing our view that fair value for Informa is >20% higher than current levels. Focusing on Live B2B Events, we look at precedent transactions, as well as valuation benchmarks from other sectors - such as Business Services, Luxury, and Capital Goods. We believe Live B2B Events should garner a high-teens FY26 EV/EBIT multiple within the group mix, with Informa as a whole around 16x (at our target price). Rolling forward, our price target implies a little over 16x FY27 adj. P/E, for a business we see as a durable 6% underlying revenue grower, and closer to 12% on EPS (inc. buybacks), with a >2.5% p.a. dividend yield. However, we also previewed 1H26 results in the note, and we think investors should be mindful of modelling dynamics around >\$175m of event revenue that has shifted between 1H and 2H this year, as Informa has changed their scheduling. We don't think these are material factors as we think it mainly just reflects intra-year seasonality between 1H and 2H this year, but consensus estimates likely need to adjust for this and investors should expect optically weaker y/y results in 1H. See our full note here.

Exhibit 2: Informa historical NTM adj. P/E valuation (consensus)  
![](images/83482e105a398411d8d927df162dc657a0d4f42fe715d952332e06931cd85080.jpg)  
Source: Factset data (consensus), MS

3) SAP CEO: "there is a chance that in 3-4 years there is actually no one developing software inside SAP any more" (#Software, #SAP): Speaking to the Australian Financial Review, SAP CEO Christian Klein talked to the view that "Software development is the function most impacted by AI" because of AI-powered coding tools and agents, adding that "there is a chance that in 3-4 years there is actually no one [human] developing software inside SAP any more". However, he framed this more as a workforce reshaping rather than a simple headcount reduction - as Mr Klein put it: "We need product managers who can vibe code and who can actually understand businesses [...] Software developers are of lower demand, but we need more data scientists". We think this echoes the new 'quality over quantity' hiring philosophy that SAP spoke to at Sapphire 2026, where they articulated a desire to hire top-caliber AI talent under a 3-to-1 ratio (one highly skilled AI expert replacing three traditional hires) and redesigning their compensation packages accordingly to remain competitive in a scarce AI talent market.

## 4) Springer Nature Tech Event - AI is driving process efficiencies in academic

4) Springer Nature Tech Event - AI is driving process efficiencies in academic publishing (\*MS Research\*, #RELX, #Informa, #Wolters Kluwer): Springer Nature (covered by David Nolan) hosted an investor technology event this week. Springer is the #2 Academic Publishing player, behind RELX's Elsevier, and larger than the likes of Taylor & Francis from Informa. We think the Academic Publishing names have been subject to AI debates over the past 12-18 months, though we believe there are more near-term upsides from AI than downsides, relating to a faster pace of research publication, and from easing pre-existing bottlenecks in the research publishing process. For Springer Nature, David noted the event highlighted a prolonged publishing process "... at c.200 days on average and c.300 days for Nature-branded journals. SN's team walked through several tools aimed at reducing friction across the process. Journal and Funding Finder is author-facing and helps researchers identify suitable journals and funding routes. SNAPP Editorial Evaluation supports faster initial manuscript assessment, SNAPP Reviewer Recommender helps editors identify relevant reviewers, and SNAPP Transfer Recommender redirects manuscripts to better-fit journals within the SN ecosystem." David also noted: "AI adoption among researchers is already high according to management, with \~75% of researchers using AI tools and \~1/3 willing to pay for them." Academic publishers already earn high margins across the board, and there remains a delicate industry balance to strike around economics, but the increasing use of AI tooling is present across the leading players, which should support a better experience for researchers, peer reviewers and editors - ultimately bolstering further incremental margin expansion. Whether publishers can monetise specific research-adjacent workflow tools (such as Springer Nature's Nature Research Assistant or RELX's LeapSpace) effectively remains a more open debate. Read David's full takeaways from the event here.

Exhibit 3: Key week ahead events

<table><tr><td>Monday29/06/2026</td><td>Tuesday30/06/2026</td><td>Wednesday01/07/2026</td><td>Thursday02/07/2026</td><td>Friday03/07/2026</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Key</td><td>MS Europe Coverage</td><td>Other Global Stocks</td><td>Industry Event</td><td>Other</td></tr></table>

Source: MS

Coverage Valuation vs. European Market  
Exhibit 4: European Software NTM P/E vs STOXX Europe 600  
![](images/30463a30b57aeb65aebe830b6d6b73004da473c9502d4221780997928883fe11.jpg)  
NB: Mean of CAP, DSY, INF, NEM, REL, SGE, SAP, TEMN, TIETO, and WKL. Price at close as of T-1 business day. Source: FactSet, MS

## Long-Term Valuation Charts

Exhibit 5: Amadeus P/NTM Earnings  
![](images/7216ad557be22735b003c045ab8bb16836f27d221ff6690ccc9957d6d7e88b7b.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 6: Capgemini P/NTM Earnings  
![](images/0aef9d65402aa70b5e72a2e3ba853f27bea760e9aafeda6bc25b6965aec84034.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 7: Dassault Systemes P/NTM Earnings  
![](images/34bdb6489c29db2221423142a417d025f040cf06a5b3c2cc8003ca13a081db00.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 8: HBX Group International P/NTM Earnings  
![](images/7a82b00b98b5f5095baabe1d4e85e7a6bd27bca3689cf4b2ccc7361d3c43cb56.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 9: Indra P/NTM Earnings  
![](images/eb3f324f884b0cccc9e8735dd4cfd5f1d98f7bb10218a5063d6594a99c9fd84b.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 10: Informa P/NTM Earnings  
![](images/a9c3da11b688a34ca4b1682f5ea67bccd0e0dfe6905dbb9c7ed59bae784c5aa3.jpg)

Exhibit 11: IONOS P/NTM Earnings  
![](images/9c23b31bb900c96ad1002e214749889f6f942bf51b8aa88d1519928784fefa51.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 12: Nemetschek Group P/NTM Earnings  
![](images/57c374b66e493c1cfe955f0d722432c0ce9af66c9a7f627b9487a1efb261b3ca.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 13: Netcompany P/NTM Earnings  
![](images/98346d6b05d7053fc03d9b791b63e7237399619a4a9245b0ddefb6c73543befe.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 14: RELX P/NTM Earnings  
![](images/8b0181f29f14c685e2b362dc45a9ffbfd7addffe25da97fe4bde98940b3fdaf0.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 15: Sage Group P/NTM Earnings  
![](images/e633b77ec9c0b2f3e27ccaf737addbbf1548929dc3d58e8d305f901a70bc5ef1.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 16: SAP P/NTM Earnings  
![](images/579dd8c392b68333eba50d99f7a997af81f2447f38d370b8502e50e62b4730b7.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 17: Temenos P/NTM Earnings  
![](images/f4e5c329477096490ffcb23ba5ea721de841e598aea5c33247f3f8b0f2fc5873.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 18: Tieto P/NTM Earnings  
![](images/365ae19dccf77513e4ba573a6dc457c18a215e146dfb9e84eb36eb7397b204e7.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 19: Wolters Kluwer P/NTM Earnings  
![](images/0278b301413d168b986b5b4c4e61fa0c1221a7f0cb5cce75fa65155daac3322b.jpg)  
NB: Price at close as of T-1 business day. Source: FactSet, MS

## Coverage Company Guidance

Exhibit 20: Company Forward Guidance (1/2)

<table><tr><td colspan="3">Published Company Guidance / Targets</td></tr><tr><td></td><td>FY26</td><td>Mid-term / Long-term</td></tr><tr><td>Amadeus</td><td>High single digit revenue growth (in cc)Adj. EBIT margin stable at cc (FY25: 29.1%)Adj. diluted EPS growth at low double-digitFCF between €1.35-1.45 billion</td><td>Over 2026-2028:High single digit annual revenue growth (in cc)Adj. EBIT margin expansion over the periodAdj. diluted EPS growth CAGR at low double-digitFCF growth CAGR at high single digit</td></tr><tr><td>Capgemini</td><td>Revenue growth of +6.5 to 8.5% cc (organic c. 1.5 to 4%, MSe)Operating margin of 13.6% to 13.8%Organic FCF of €1.8 to 1.9bn</td><td>2028 financial ambitions:2025-28 revenue CAGR at cc of +5.5-7.5% (c. +3.5-5.5% organic)Operating Profit pre-acquisition expense to reach 12.1-12.3% of revenue (c. 130-150bps expansion vs 2025)Cumulative organic FCF &gt;€6bn over 2026-28</td></tr><tr><td>Dassault Systemes</td><td>Total revenue growth between 3 to 5% (cc)Software revenue growth 3 to 5% (cc)Services revenue growth of 2 to 6% (cc)Adj. EBIT margin guidance is 32.2 to 32.6%EPS €1.30 to 1.34</td><td>Basic 2029 EPS of €2.4</td></tr><tr><td>HBX Group</td><td>+11 to +15% YoY growth in TTV-4 to +1% YoY revenue growth-5 to -2% adj. EBITDA growthc. 90 to 100% operating FCF conversion</td><td>Low-double digit TTV annual growthHigh-single digit revenue growthLow sixties adj. EBITDA margin %c. 100% cash conversion</td></tr><tr><td>Indra Sistemas</td><td>Revenue &gt;€7,000m in local currencyStated EBIT of &gt;€700mFree cash flow of &gt;€375m</td><td>Long-term (FY24-FY30):Revenues to reach €10bn in FY30EBITDA margins &gt;12% by FY26 and &gt;14% by FY30EBIT margin at 10% in FY26 and 12% in FY30Cumulative FCF of &gt;€3bn from FY24-FY30</td></tr><tr><td>Informa</td><td>6%± underlying revenue growth7%+ B2B Events underlying revenue growth4%± Taylor &amp; Francis underlying revenue growthReturn to revenue growth for TechTargetUnderlying double-digit growth in adj. EPS</td><td>5%+ underlying revenue growth p.a. out to FY28</td></tr><tr><td>IONOS Group</td><td>Group: c. 7% revenue growth with c. 37-38% adj. EBITDA margin (CC)Web Presence &amp; Productivity: 7-8% revenue growth (CC)Cloud Solutions: c. 10% revenue growth (CC)</td><td>Total revenue growth (CAGR) c. 10%Web Presence &amp; Productivity revenue growth (CAGR) c. 9%Cloud Solutions revenue growth (CAGR) c. 20%Adj. EBITDA margin c. 40%Capex (% of revenue) c. 6%</td></tr><tr><td>Nemetschek Group</td><td>14-15% constant currency revenue growth32-33% adj. EBITDA margin</td><td>None</td></tr><tr><td>Netcompany Group</td><td>Group revenue growth of 15-20% y/y (in CC), 5-10% excluding NBSAdj. EBITDA margin of 16-19%, 17-20% excluding NBS</td><td>Long-term:Annual organic revenue growth of 5-10% &quot;through any business cycle&quot;Adj. EBITDA margins &gt;20% by (in) FY29</td></tr><tr><td>RELX</td><td>&quot;We continue to see positive momentum across the group, and we expect another year of strong underlying growth in revenue and adjusted operating profit, as well as strong growth in adjusted earnings per share on a constant currency basis&quot;.Buybacks of £2,250m</td><td>None</td></tr></table>

Source: Company data, compiled by MS

Exhibit 21: Company Forward Guidance (2/2)

<table><tr><td colspan="3">Published Company Guidance / Targets</td></tr><tr><td></td><td>FY26</td><td>Mid-term / Long-term</td></tr><tr><td>Sage Group</td><td>Organic total revenue growth in FY26 to be above 9%Operating margins are expected to trend upwards in FY26 and beyond</td><td>None</td></tr><tr><td>SAP</td><td>Cloud revenue of €25.8-26.2bn at cc (23% to 25% cc growth).Cloud and software revenue of €36.3-36.8bn at cc (12%-13% cc growth).Non-IFRS EBIT of €11.9-12.3bn (14

[中间内容因长度限制已省略]

audi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Technology - Software & Services

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/25/2026)</td></tr><tr><td colspan="3">Adam Wood</td></tr><tr><td>Indra (IDR.MC)</td><td>E (01/12/2026)</td><td>€47.39</td></tr><tr><td>SAP SE (SAP.N)</td><td>O (02/20/2026)</td><td>US$148.06</td></tr><tr><td>SAP SE (SAPG.DE)</td><td>O (03/20/2020)</td><td>€132.28</td></tr><tr><td colspan="3">George W Webb</td></tr><tr><td>Amadeus IT Holdings S.A. (AMA.MC)</td><td>O (04/10/2026)</td><td>€52.16</td></tr><tr><td>Capgemini (CAPP.PA)</td><td>E (02/19/2026)</td><td>€88.50</td></tr><tr><td>Dassault Systemes SA (DAST.PA)</td><td>E (03/17/2026)</td><td>€17.59</td></tr><tr><td>Hexagon AB (HEXAb.ST)</td><td></td><td>SKr 80.62</td></tr><tr><td>IONOS Group SE (IOSn.DE)</td><td>E (05/12/2025)</td><td>€26.50</td></tr><tr><td>Nemetschek SE (NEKG.DE)</td><td>E (07/13/2022)</td><td>€52.05</td></tr><tr><td>Netcompany Group A/S (NETCG.CO)</td><td>U (01/12/2026)</td><td>DKr 292.80</td></tr><tr><td>Sage (SGE.L)</td><td>O (12/08/2021)</td><td>796p</td></tr><tr><td colspan="3">Mark Hyatt</td></tr><tr><td>HBX Group International PLC (HBX.MC)</td><td>E (04/17/2026)</td><td>€6.80</td></tr><tr><td>Temenos Group AG (TEMN.S)</td><td>U (12/15/2017)</td><td>SFr 64.75</td></tr><tr><td>Tieto Oyj (TIETO.HE)</td><td>U (01/12/2026)</td><td>€19.06</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
