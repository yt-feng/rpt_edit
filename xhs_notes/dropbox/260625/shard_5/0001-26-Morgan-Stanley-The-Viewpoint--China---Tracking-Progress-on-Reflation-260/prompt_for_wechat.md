你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Asia Economics | Asia Pacific

# The Viewpoint: China – Tracking Progress on Reflation

Sustained strong exports growth will lift profit margins for the non-commodity sector, which will drive wage growth and a cyclical pickup in underlying inflation. But we don't expect a normalized inflation of $2 - 3\%$ yet, given that policy measures to address structural issues are not as forthcoming.

## Key Takeaways

The recent positive PPI prints are not a sign of reflation as corroborated by the contraction in retail sales in May.

But we do expect a cyclical pickup in underlying inflation as the Asia capex supercycle drives a sustained improvement in China's exports.

This in turn will lift margins for select non-commodity sectors, providing modest support to wage growth and consumption with a lag.

However, we don't see a return to a normalized $2 - 3\%$ GDP deflator yet.

To achieve sustainable inflation, we will need policy measures to address the structural issues of property and social security support.

MS ASIA LIMITED

Chetan Ahya
Chief Asia Economist
Chetan.Ahya@morganstanley.com +852 2239-7812

Robin Xing
Chief China Economist
Robin.Xing@morganstanley.com +852 2848-6511

MS ASIA (SINGAPORE) PTE.
Derrick Y Kam
Asia Economist
Derrick.Kam@morganstanley.com +65 6834-8272

Jonathan Cheung
Economist
Jonathan.Cheung@morganstanley.com +852 2848-5652

Kelly Wang
Economist
Kelly.Wang@morganstanley.com +852 3963-0891

Asia Summer School 2026

![](images/7bb9c8ab545a0ab74c72b67a8c6446afecf8f66ecff39a160e2f9bc71e3a871c.jpg)

In this report, we address the cyclical and structural factors that will influence China's transition from deflation to sustainable and normalized inflation.

## Where we are in China's reflation journey

The recent positive PPI prints are not necessarily a sign of reflation: While the producer price index (PPI) has turned positive on a YoY basis after \~3.5 years in deflation, we have been arguing that it is not a sign of a sustainable transition to normalized inflation. It is increasingly clear that the upward momentum in headline PPI in recent months has been driven by higher oil prices, which will now move back to reverse mode as oil prices decline. The higher commodity PPI is leading also to higher non-commodity PPI and that will lift the GDP deflator into positive territory in 2Q26. But that is still not full-fledged reflation. Margins for the non-commodity sector have remained flat or, in other words, the non-commodity sector has not been able to regain pricing power.

Why reflation has been held back so far: A confluence of cyclical and structural reasons has been holding back reflation in China. Persistent deflationary pressures have been weighing on the non-commodity sector and in turn wage growth. This was then compounded by the slow pace of fiscal rollout since 1Q26 and higher oil prices – which affected consumer purchasing power and therefore weighed on consumption. Structurally, weaker demographic trends means that the structural demand for property is weak. This, coupled with the modest and reactive policy support for the sector, have kept property prices on a correction path. Meanwhile the lack of an adequate social security net keeps the household saving ratio high, especially for migrant workers.

Where are we headed – cyclical uplift but structural drag remains: Our chief China economist Robin Xing expects that inflation will rise modestly from here and remain structurally firmer than in 2023-25, as the improvement in exports amid Asia's industrial and capex supercycle supports a modest improvement in wage growth. However, the structural challenges we highlighted above are still in place, meaning that a sustained transition to a 2-3% GDP deflator is not yet in sight.

What we are tracking: To assess the progress on reflation, we are tracking the following indicators:

1. Non-commodity industrial profit margins: To assess if corporates will feel confident and have the room to increase wages.

2. Wage growth: A pickup in wage growth will help support consumption growth cyclically.

3. Retail sales: The key, comprehensive and high frequency indicator to track consumption growth.

## Cyclical factors holding back reflation

We see three cyclical factors that have weighed on reflation:

\- Withdrawal of policy stimulus

\- Impact of trailing weak wage growth

\- Higher oil prices

Trailing wage growth has been weak, weighing on consumption: While industrial profit growth has picked up year-to-date, the uptick has been driven more by higher commodity prices. Non-commodity sector profit margins have stabilized but remain relatively weak given the persistent deflationary backdrop. This is also corroborated by still relatively weak consensus earnings growth of 6% for CSI300 in 1Q. Reflecting this, wage growth remains weak at 4.9%Y in 1Q. As a result, consumption growth momentum has been soft. Moreover, as the effects of the consumption trade-in program has faded, this has resulted into an outright contraction in headline retail sales. The latest datapoints we have on services consumption also exhibit similar weakness. Our hotel and transportation research teams note that June hotel revenue per available room growth and air passenger traffic growth around the Dragon Boat Festival remain weak.

Exhibit 1: Non-commodity sector profit margins have stabilized but remain relatively weak...  
![](images/3bbe8810dd64994a36331b0c5774a796278f4dd36554409d0663f84cd56546e0.jpg)  
Source: CEIC, MS

Exhibit 2: ...leading to subdued trends in wage growth  
![](images/cc1dfde3b438cd273438e8d2e252c4ae1bb5551afeecec1b3ef571eae907b74a.jpg)  
Exhibit 3: As the effects of the consumption trade-in program have faded, this has resulted in an outright contraction in headline retail sales  
Source: CEIC, MS

![](images/76c7dd83e5fd11f1d6790f017ab309c1ea42a7a72fe541ac6aecf06ac46682c7.jpg)  
Source: CEIC, MS

Exhibit 4: Hotel RevPAR indicates soft demand – June is tracking only 2% YoY despite a very low base in 2025  
![](images/59ebb276bb052d566b4ecc38afa8036bae7596710cdb407cbcda897310da90e6.jpg)  
Source: STR, Jun-26 and 2Q26 numbers are MS Equity Research estimates

The withdrawal of stimulus – counter-cyclical growth model in action again: In past cycles, we have observed that policymakers in China tend to pull back on policy easing in a countercyclical manner when external demand is strong. We have seen this playbook again on the back of the stronger-than-expected 1Q real GDP growth and the robust momentum year-to-date in exports. The augmented fiscal deficit has narrowed from 11.9% of GDP in Jan-26 to 10.9% of GDP in May as policymakers slowed the pace of fiscal rollout in 2Q. Reflecting this, nominal FAI growth has slowed to a year-to-date low of -10.7%Y – with infrastructure FAI in particular slowing from 9.2%Y in 1Q26 to -10.8%Y in May. With 2Q GDP growth tracking at below the full-year growth target at 4.4%Y, our China economics team expects policymakers to step up the pace of fiscal rollout in 3Q26 to smooth growth (see China Economics: 2Q Tracking GDP Softens to 4.4% on Weak Domestic Demand, June 16, 2026).

Exhibit 5: Policymakers are following the countercyclical growth model of pulling back policy stimulus when external demand is strong  
![](images/1bf660db9f8222ba75c810ba33a1a9fda61b4b09b9b5c49f428958dbd4c4aa8d.jpg)  
Source: CEIC, Haver, MS

Exhibit 6: Augmented deficit has narrowed from 11.9% of GDP in Jan-26 to 10.9% of GDP in May  
![](images/cea2a35de6356ab56a830824f713b3595aa0ef635dff83ed3708cf79dae9f309.jpg)  
Source: CEIC, Haver, MS

Higher oil prices had posed a near-term drag on consumption: Since the onset of the energy shock, domestic gasoline prices have risen by a peak of 26% and have remained 18% higher than end-February levels. Reflecting this, fuel CPI has accelerated to 21%Y in May, vs. -9%Y in Feb. Given fuel and electricity together account for about 11% of the CPI basket, this also likely posed a drag on consumption momentum in the past few months. The recent move lower in international oil prices will likely mean a reduced drag going forward.

Exhibit 7: Domestic gasoline prices have also risen by a peak of 26%, and have remained 18% higher than end-February levels  
![](images/3a0879f51c4ac3d28cbdc42d7c260b31206b9366b7300646cdc78afe6d2bb9cc.jpg)  
Source: CEIC, MS; Note: Domestic retail fuel prices are calculated as the average maximum retail price of RON95 gasoline across 84 cities.

Exhibit 8: Fuel CPI accelerated sharply but has likely peaked in  
![](images/6996fec76e4df3900e8fa9ba76423a4bf294f5605561d405954c2e604706f0c8.jpg)  
Source: CEIC, MS, Note: Domestic retail fuel prices are calculated as the average maximum retail price of RON95 gasoline across 84 cities. June MTD is as of June 19, 2026.

## Structural factors holding back reflation

Three intertwined factors: There are also structural factors at play – which weigh on aggregate demand and hence explain the weak inflationary impulse. Behind this is the lack of consumption or the weak role that consumption plays in the economy. We’d highlight three intertwined factors:

\- Weakening demographics

• Structurally weaker property market

\- Lack of a social security safety net

Weakening demographic trend: China's working age (15-64) population has declined from a peak of 1bn in 2015 to 990mn currently. Moreover, the total population has been in decline since 2022. This will remain a structural drag on aggregate demand in the economy.

Property sector adjustment: The backdrop of weakening demographics has meant a structural decline in property demand. This, together with the lack of policy support for the sector, has meant that property prices have stayed weak. But it is also the case that there has already been an extensive adjustment in the sector. For example, real estate FAI (excluding land costs) has declined to 6% of GDP in 2025, from a peak of 16% in 2014, and is now below 2004 levels. We believe that the drag from the property market on the broader economy will reduce, but it is unlikely that it will be a significant growth driver going forward.

Exhibit 9: Weakening demographic trend exerting pressure on growth  
![](images/ef98aa37816fe1b053829cfbdfdbfe9b9a9fa5bff9e66821c82717ac37cef4af.jpg)  
Source: Haver, MS

Exhibit 10: Extensive adjustment means property sector should exert less of a drag on the broader economy going forward, but will also not be a significant growth driver given structural headwinds  
![](images/c9baccfc5fa06372ac00c52219cb109b38f0ba528421add42e47cff1ee0513ce.jpg)  
Source: CEIC, Haver, MS

Lack of social security: A longer-term issue weighing on consumption is a high household savings rate, which reflects large precautionary savings in reaction to both inadequate structural access to social services (especially amongst the migrant worker population) and weak labour market conditions. The household savings rate is elevated at 32% in China, vs 23% in India, 4.6% in US and 4.1% in Japan. For migrant workers (300 million), their savings ratio is much higher than the national average. As such, our long-held view has been that there is a need to lift social welfare spending, especially for the migrant

worker population, which will help manage aggregate demand and unlock precautionary savings (see China's 3D Journey: How China could avoid a 1990s Japan situation, August 2023).

Exhibit 11: Household savings rate remains elevated and has been rising

China 1Q surveyed household saving rate 35.0% (4Q trailing sum % of disposable income)

![](images/9fa4315f2e37a1cf271fe71a0746ff96953591e4f6fda56dd1d5a4c692a2b3c4.jpg)  
Source: CEIC, Haver, MS

# What would we be watching to track China reflation?

Policy measures to address the structural issues are not likely to be as forthcoming: An increase in social welfare spending is seen to be a long-term commitment to raise spending permanently. Against this backdrop, policymakers remain hesitant to commit to large-scale social welfare reforms. This is especially as the government revenue to GDP ratio continues to decline and the outlook for public finances remains challenging. Moreover, our China economics team notes that the 15th Five-Year Plan has already affirmed that the growth model will remain tech-led and supply-centric, while policy support for consumption and social welfare reforms would remain gradual.

While policymakers have slowed new manufacturing investment growth, they are not taking aggressive steps to cut existing excess capacity due to concerns over the implications for the labour market.

In this context, since we don't expect meaningful policy support measures, the cyclical improvement in exports will assume more importance in the reflation journey. To assess the progress, we will be tracking:

1. Exports

2. Non-commodity sector profit margin

3. Wage growth

Exports recovery is broadening out: We have been highlighting that Asia's industrial and capex supercycle – underpinned by multiple medium-term drivers - is driving a broadening out of Asia's export recovery from tech to non-tech. We see China as one of the key beneficiaries given it is positively levered to a pickup in export opportunities driven by capex in the rest of the world in areas such as energy, defense, AI and AI infrastructure, and industrial supply chain buildout. China's non-semis exports have only just recently posted stronger growth at close to double digits in the past two months.

This will help non-commodity sector profit margins and wage growth with a lag: Given industrial capacity utilization has just started to improve from low levels in 1Q and progress on efforts to address excess capacity remains gradual, the improvement in exports would only translate to better non-commodity sector profit margin and hence wage growth with some lag.

Exhibit 12: China's non-tech exports showed broad-based improvement across passenger cars, intermediate goods and capital goods  
![](images/1d34b88e43f31af8c8d52065866e1efea9b99afe5685b38c9ef61fd87431d6fe.jpg)  
Source: CEIC, Haver, MS

Exhibit 13: Sustained strong exports will lift capacity utilization  
![](images/270d8e33ba78b23effdcbccd4052e55cb3e7eb91e441a334f969f2f416e989ac.jpg)  
Source: CEIC, Haver, MS

## Disclosure Section

Information and opinions in MS were prepared or are disseminated by one or more of the following, which accept responsibility for its contents: MS Asia Limited, and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105), Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Disclosures

MS is not acting as a municipal advisor and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of Section 975 of the Dodd-Frank Wall Street Reform and Consumer Protection Act.

MS does not provide individually tailored investment advice. MS has been prepared without regard to the circumstances and objectives of those who receive it. MS recommends that investors independently evaluate particular investments and strategies, and encourages investors to seek the advice of a financial adviser. The appropriatene

[中间内容因长度限制已省略]

ts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 14-9169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
