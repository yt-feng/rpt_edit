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
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Japan Economic Weekly

Economics - Japan

## The focus of attention has shifted to growth strategies and consumption tax cuts

The economy, prices, and financial conditions favor more rate hikes

1. Domestic policy (BOJ): The economy, prices, and financial conditions at the heart of monetary policy management (Kyohei Morita)

\- The focus of the BOJ's monetary policy management is likely to be on the economy, prices, and financial conditions. It will take some time for an easing of the tensions in the Middle East to be reflected in an easing of quantitative and price-related supply constraints. Nevertheless, we think these three factors (the economy, prices, and financial conditions) favor more rate hikes.

2. Domestic policy (government): Focus in late June likely to be on growth strategies and consumption tax cuts (Kengo Tanahashi, Masaki Kuwahara)

\- Now that the monetary policy meeting is over, we expect the focus of attention to shift from monetary policy to fiscal policy. By the end of this month we expect the government to finalize its growth strategies for this year and Prime Minister Takaichi to make a final decision on the consumption tax cuts.

\- The Growth Strategy Council is reportedly envisioning public-private investment of around ¥370trn by FY40. It will be interesting to see how much public-sector support is provided and how it is funded.

\- We think the government's proposal is likely to be a combination of a cut to the consumption tax for food to 1% from 2027 and cash handouts in the autumn of 2027 and 2028. However, the opposition parties have strongly objected to such a proposal, and it remains to be seen how it would be funded.

3. Japanese economy: Gradual easing of supply constraints stemming from Middle East, AI boom (Yuki Ito, Elias Liu)

\- In this section, we identify key themes for the outlook for the economy. We focus on: (1) supply constraints stemming from the Middle East; (2) automobile exports; and (3) the AI boom.

\- A number of statistics already show signs of an AI boom. Orders for computers and Chinese orders for machine tools have started to rise. The recent strength of orders may point to signs of growth in exports and capex in the near term.

4. Digest of recent reports

5. The week ahead

6. Japanese macroeconomic indicators

7. Calendar of world events in 2026

8. Economic forecasts for Japan

9. Policy stance of BOJ Policy Board

## Research Analysts

## Japan Economics

Kyohei Morita - NSC
kyohei.morita@NOM.com
+81 3 6703 1395

## Masaki Kuwahara - NSC

masaki.kuwahara@NOM.com
+81 3 6703 3876

Kengo Tanahashi - NSC
kengo.tanahashi@NOM.com
+81 3 6703 1295

Uichiro Nozaki - NSC
uichiro.nozaki@NOM.com
+81 3 6703 1284

Yuki Ito - NSC
yuki.ito@NOM.com
+81 3 6703 3867

## Yuna Minegishi - NSC

yuna.minegishi@NOM.com
+81 3 6703 1287

## Global Economics

Elias Liu - NSC
elias.liu@NOM.com
+81 3 6703 3844

## Key points for monetary policy

Our main scenario is that the BOJ hikes rates in June and December 2026 and June 2027. Since its April monetary policy meeting the BOJ's stance has been to "continue to raise the policy interest rate and adjust the degree of monetary accommodation, in accordance with economic activity, prices, and financial conditions." Looking ahead, we will keep a close eye on the BOJ's policy stance, focusing on: (1) the impact of the Middle East situation on the economy and prices; and (2) the Takaichi administration's management of fiscal policy.

Japanese report published on 19 June 2026

# 1. Domestic policy (BOJ): The economy, prices, and financial conditions at the heart of monetary policy management

Monetary policy meeting: (1) three points to note; (2) we retain our main scenario

The BOJ raised its policy rate from "around 0.75%" to "around 1.0%" on 16 June. The rate hike itself came as no surprise as it had been sufficiently priced in by the market (see our 16 June 2026 report BOJ Watch).

However, there were a number of noteworthy developments related to the rate hike decision. We see three main takeaways.

First, Policy Board member Toichiro Asada voted against a rate hike. Ayano Sato, who, like Mr Asada, was appointed to the Board by the Takaichi Cabinet, will take up office on 30 June as the successor to Policy Board member Junko Nakagawa. Given that Mr Asada voted against the rate hike, Ms Sato may also oppose rate hikes any time soon. The market is also interested in how the end of the terms of office for hawkish Policy Board members Hajime Takata and Naoki Tamura in July 2027 will affect the BOJ's policy stance. However, from a fundamental point of view, we think the current rate-hiking cycle is likely to end in mid- to late 2027, anyway.

Second, there were changes in the BOJ's assessment of the risks to the economy and prices. With respect to the economy, it said that "the risk of a significant slowdown in the economy appears to have decreased compared with a while ago," while, with respect to prices, it warned that "there is a risk of underlying CPI inflation deviating upward to a level above the price stability target of 2 percent." Such a risk assessment provides justification for ongoing rate hikes.

Third, there were also changes to the wording on the future conduct of monetary policy. Whereas the BOJ had previously given "real interest rates are at significantly low levels" as a reason for continuing to raise the policy interest rate, this was replaced by "financial conditions have been accommodative." At the press conference that followed the meeting, BOJ Deputy Governor Shinichi Uchida positioned this as a change not in the BOJ's assessment but in how it explains it. However, we think it would make more sense to see the removal of the phrase "significantly low" as an indication that the BOJ has lowered its assessment of the degree of monetary easing by one notch.

In view of the above three points, we think the BOJ may have passed the halfway mark of this rate-hiking cycle. Accordingly, our views on the outlook for monetary policy are as follows.

• Main scenario: a total of two rate hikes in December 2026 and June 2027

\- Risk scenario: a total of three rate hikes in October 2026, Mar–Apr 2027, and Sep–Oct 2027

Economy: Crude oil import volumes and the degree of shipment delays in the manufacturing sector will be key points to watch as tensions in the Middle East ease

We identify two main takeaways from the BOJ's monetary policy stance.

(1) In view of the current accommodative monetary conditions, the BOJ will continue to raise its policy rate and adjust the degree of monetary easing in accordance with the economy, prices, and financial conditions.

(2) The BOJ will consider the timing and pace of any adjustments to the degree of monetary easing while keeping a close eye on the situation in the Middle East as well as on the likelihood of its median forecasts for the economy and prices proving to be accurate.

In view of these two points, we think that careful monitoring of (a) the economy, (b) prices, and (c) financial conditions will be key to assessing the outlook for BOJ policy management.

(a) With regard to the economy, the latest important development is that tensions in the Middle East have started to ease, with the US and Iran signing a memorandum of understanding on 18 June (US time).

However, in order for global economic activity to normalize, the Strait of Hormuz will need to be reopened and crude oil prices will need to stabilize. The number of tankers transiting the Strait of Hormuz has dwindled to more or less zero from 60–70 per day before the situation in the Middle East deteriorated (Figure 1). While the number of tankers transiting the nearby Bab-el-Mandeb has risen slightly since the second half of March, we can by no means say that alternative routes to the Strait of Hormuz have been established, even if we include the Suez Canal.

This suggests that it will take time for quantitative supply constraints, which have a direct bearing on the economy, to ease even as the situation in the Middle East eases. Looking ahead, we will need to keep a close eye on the extent of the recovery in petroleum and petroleum product import volumes (Figure 2) and on the extent of any delays to the procurement of raw materials faced by manufacturers in the major economies (Figure 3).

Fig. 1: Number of tanker transits in the Middle East still a long way from returning to normal  
![](images/b71a098ce34a6791105484fb89be260be45174f646932e2319a5bea4dd6df7c7.jpg)  
Note: Shows number of tanker transits per day. Latest data as of 18 June 2026.
Source: NOM, based on Bloomberg data

![](images/cfe970d33bac784a904510cdee52759dd8097cb4f27ad0223662afdc77103a19.jpg)

![](images/8e101536af597340348d3dc0c47929bdd9f3630d0cc5220adda99d2f0b61eff3.jpg)

Fig. 2: Sharp decline in imports of oil and petroleum products  
![](images/5610240befa484f9294496d7f7ad6b7b2c95411d36d61cdb1f965879a4de83bd.jpg)  
Source: NOM, based on MOF

Fig. 3: Delays in delivery of raw materials and parts  
![](images/b1d22679e0b5b8c143063a266fe52cdc459086ca2c18d183b55befd2d5c97100.jpg)  
Source: NOM, based on S&P Global data

## Prices: We expect CPI inflation to peak in 2027 Q1

The second factor that will need to be monitored to see whether the BOJ is likely to continue to hike interest rates is (b) prices.

prices of the three main crudes (Dubai, WTI, and Brent) have been edging lower in anticipation of an easing of tensions in the Middle East (Figure 4). This suggests to us that, while quantitative supply constraints are likely to persist for a while longer, price-related supply constraints may ease first.

Fig. 4: Crude oil prices edging lower  
![](images/6868ffd0bf18302a28946579d80a26a2db858334a1bf8ab1ac1b3a21d34a7d7f.jpg)  
Source: NOM, based on Bloomberg data

![](images/2cd9227de427076244a02820382d40911c3823cca3cd6373b1d490bc2c76b6a4.jpg)

Even if they do, we think it may take until around mid-2027 for price-related supply constraints to spread downstream. This is because of the time it takes for upward pressure on prices to work its way from upstream in the supply chain to downstream.

Looking at goods prices, we see that yen-denominated import prices have risen sharply. This will now work its way down the supply chain from (B2B) producer prices (PPI) to (B2C) consumer prices (CPI) (Figure 5). We think it will take until Jan–Mar 2027 for downstream (y-y) consumer price (CPI) inflation to peak (Figure 6).

In the meantime, we expect the BOJ to remain on the lookout for upside risks to prices, a concern it expressed in its June monetary policy statement.

Fig. 5: Upward pressure on prices mounts upstream  
![](images/467f6b02a8777482fde7bc81f58fcf4db8993c0533310f00b753eb70c618252b.jpg)  
Note: Data cover only goods.  
Source: NOM, based on Ministry of Internal Affairs and Communications and BOJ data

Fig. 6: Core CPI inflation expected to peak in 2027 Q1  
![](images/7052f443b1e44866738bc0ba0d0bd225b6e1a3c93ccf7ce682e4c01cdbc78aad.jpg)  
Note: (1) The core CPI excludes fresh food. The core-core CPI excludes energy and core food (food less fresh food and alcoholic beverages). (2) We assume that the consumption tax rate on food and beverages will be reduced to zero in April 2027.
Source: Actual figures from Ministry of Internal Affairs and Communications, forecasts by NOM

## Financial conditions: Growth in lending justifies additional rate hikes

The third factor that will need to be monitored to see whether the BOJ is likely to continue to hike interest rates is (c) financial conditions.

Financial conditions can include a wide range of factors, including lending, exchange rates, and asset (eg, share) prices. Lending is of particular interest when it comes to gauging the size of any gap between the policy interest rate and the neutral rate of interest. This is because sustained growth in lending can be seen as evidence that the policy rate is lower than the neutral rate.

Loans outstanding at banks and shinkin banks are up 6% y-y, outpacing CPI inflation (Figure 7). Growth in lending by city banks is particularly marked.

Home loans have also been rising steadily. As the BOJ raises its policy interest rate, much is often made of the impact on home loan interest rates. However, home loans outstanding at private-sector financial institutions have continued to rise by 3-4% y-y, partly as a result of rising house prices (Figure 8). Moreover, the BOJ's housing loan demand DI (stronger - weaker) has turned positive. This shows that lenders are aware of the growing demand for home loans.

We have looked at the main aspects of the economy, prices, and financial conditions that will need to be monitored. It will take some time for an easing of the tensions in the Middle East to be reflected in an easing of quantitative and price-related supply constraints. Nevertheless, we think these three factors (the economy, prices, and financial conditions) currently favor more rate hikes.

(Kyohei Morita)

Fig. 7: Rate of increase in loans outstanding rises, particularly at city banks  
![](images/c37989aee03d50b3245bd450dd7e15343feb931531b657bf2e5c82ee28599e2d.jpg)  
Note: City banks, etc. includes city banks and trust banks.
Source: NOM, based on BOJ data

Fig. 8: Home loan demand on the rise  
![](images/ca9f3841827f02ce40f8bca5ab63a11a5770d64b7c570624e3259ac9c7524fb8.jpg)  
Source: NOM, based on BOJ data

# 2. Domestic policy (government): Focus in late June likely to be on growth strategies and consumption tax cuts

Key points to watch in macroeconomic policy: Following BOJ meeting, focus likely to shift to fiscal policy management under Takaichi administration

Now that the June monetary policy meeting is over, we expect the focus of attention to shift from monetary policy to fiscal policy. We await the interim report on growth strategies, consumption tax cuts, and refundable tax credits later this month, while the Cabinet is expected to approve this year's Basic Policy in July. Both of these are important for gauging the outlook for the Japanese economy. It will also be interesting to see how "responsible" the Takaichi administration's fiscal management is.

Growth strategies: Media reports suggest public-private investment of around ¥370trn by FY40

NHK reported on 18 June that the Japan Growth Strategy Council is considering a total of around ¥370trn in public and private-sector investment in 17 strategic areas by FY40 (see our 19 June 2026 report Fiscal Insight).

By way of comparison, the government's green transformation (GX) policy, which started in 2023, called for public-private investment of around ¥150trn over 10 years. On an annual basis, this translates to ¥15trn in public-private investment and ¥2trn in support through GX economy transition bonds.

Assuming public-private investment of ¥370trn over the 14 years from FY27 to FY40, this growth strategy works out at around ¥26trn a year, around 1.8x the level of public-private investment envisioned in the GX policy. Assuming a 1.8x increase in public support per year, we estimate annual public-sector support of ¥3.5trn, for a total of ¥49trn over 14 years.

Of course, the ratio of public-sector support to required public-private investment will not necessarily be the same as for the GX policy. It will be interesting to see how much public-sector support is provided relative to public-private investment and how it is funded.

Consumption tax cuts: Opposition parties oppose LDP proposal, question mark against agreement by end-June

LDP Research Commission Chairman Itsunori Onodera submitted a draft proposal to the National Council on Social Security on 17 November as an indication of what to expect in the forthcoming interim report. Under the proposal, refundable tax credits will be fully introduced around autumn 2029, and in the meantime the government will: (1) lower the consumption tax rate on food and beverages to 1% from April 2027; and (2) provide cash handouts closely linked to income and worth in total the equivalent of 1% of consumption tax (around ¥600.0bn) in the autumn of 2027 and 2028. The ruling coalition pledged to lower the consumption tax rate to 0% in the February Lower House election and is now aiming to achieve the same effect by combining (1) and (2).

While discussions are likely to be based on the above proposal, final agreement has yet to be reached. The Sankei Shimbun reported on 17 June that opposition parties had expressed strong dissatisfaction at the National Council meeting. At present, the LDP has a two-thirds majority in the Lower House on its own, so even if all the opposition parties were to oppose the ruling coalition's tax cut bill in the Upper House, it would still be able to get the bill through the Lower House by putting it to a second vote. However, if the ruling coalition's bill does not adequately reflect discussions at the National Council, which is supposed to be a nonpartisan forum, forcing a bill through the Lower House in this way would create a bad impression.

The DPP, which has a relatively similar economic policy stance to the ruling coalition, has proposed the introduction of refundable (income/residents') tax and social insurance premium credits by FY27. In the meantime it is also calling for cash handouts of ¥50,000 each for around 10mn middle- and low-income workers. While the total amount of around ¥500.0bn is broadly in line with the ruling coalition's proposal, the DPP is calling for the handouts to be made before the end of this year, which is different from the ruling coalition's proposal that they be made in the autumn of 2027. It will be interesting to see whether the ruling coalition and the DPP can reconcile their differences from next week onwards.

## Still not clear how consumption tax cuts will be funded, focus now on what proposals will be considered

The total cost of the consumption tax cuts, comprising a cut in the rate on food to 1% and handouts to households, will be about ¥5trn. While the ruling and opposition parties have indicated that they will not rely on deficit-financing bonds to fund such a move, they have not presented any definite proposals at the National Council.

One possibility would be to use surplus funds from the Foreign Exchange Fund Special Account (FEFSA). Around ¥5.4trn in surplus funds were generated in FY24, of which around ¥3.2trn was allocated to the general account for FY25. Of the remaining ¥2.2trn, ¥1.4trn is earmarked as foreign exchange funds and ¥800.0bn as FEFSA revenue for the following fiscal year. Every year the Ministry of Finance (MOF) earmarks a portion of the surplus as foreign exchange funds. In 

[中间内容因长度限制已省略]

‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## Disclaimers required in Japan

Credit ratings in the text that are marked with an asterisk (\*) are issued by a rating agency not registered under Japan's Financial Instruments and Exchange Act (“Unregistered Ratings”). For details on Unregistered Ratings, please contact the Research Production Operation Dept. of NOM Securities Co., Ltd.

Investors in the financial products offered by NOM Securities may incur fees and commissions specific to those products (for example, transactions involving Japanese equities are subject to a sales commission (all figures on a tax-inclusive basis) of up to 1.43% of the transaction amount or a commission of ¥2,860 for transactions of ¥200,000 or less, while transactions involving investment trusts are subject to various fees, such as commissions at the time of purchase and asset management fees, such as commissions at the time of purchase and asset management fees (trust fees), specific to each investment trust).

In addition, all products carry the risk of losses owing to price fluctuations or other factors. Fees and risks vary by product. Please thoroughly read the written materials provided, such as documents delivered before making a contract, listed securities documents, or prospectuses.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved.
"""
