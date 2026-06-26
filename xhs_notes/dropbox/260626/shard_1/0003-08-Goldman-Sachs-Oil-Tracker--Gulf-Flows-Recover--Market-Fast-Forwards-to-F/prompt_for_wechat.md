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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Oil Tracker: Gulf Flows Recover: Market Fast-Forwards to Future Surplus

Spot Brent futures prices decreased by 8% over the last week following reported “major progress” regarding US-Iran negotiations, a sizable pick-up in visible Persian Gulf oil flows, a US waiver authorizing Iranian oil sales, and a continuing decline in crude positioning.

The market is likely extrapolating the swift (thus far) recovery of Mideast supply and already pricing expected future surpluses.

☐ Total Gulf exports have returned to 63% of normal levels (7-day moving average) (Exhibit 1) following a rapid recovery of visible Hormuz flows (Exhibit 6), likely reflecting more crossings and a larger share of crossings that are “visible” (ships that are now keeping their AIS on).

☐ Empty tanker capacity continued to rise in the Persian Gulf, with 52mb more empty tankers entering the Gulf over the last week vs. 53mb of loadings leaving the Gulf (Exhibit 7).

While we don't expect shipping availability to be a major binding constraint, Iraq has reportedly halted production at the West Qurna 2 oil field on a shortage of empty tankers.

☐ There have been no reported attacks on ships in/around Hormuz since June 11.

The US Treasury issued a 60-day waiver authorizing sales of Iranian oil, including oil transported on previously sanctioned vessels.

☐ The waiver may unlock up to around 60mb of Iranian oil on water (Exhibit 2).

However, we do not expect a large pick-up in Iranian oil production even if the sanctions relief extends beyond the August 21st expiration date.

\- On the demand side, Asia and China in particular will likely remain the main buyers of Iranian crude (Exhibit 2) as vast EU and UK sanctions on Iranian oil and vessels remain in place.

\- On the supply side, Iran grew its production by 1.3mb/d (59%) between 2020–2025 even under the US “maximum pressure” campaign, suggesting that US sanctions might not be a very tight constraint on production growth.

The pace of global visible stocks draws has slowed sharply in June to -1.8mb/d from -5.5mb/d in May (Exhibit 10) as oil on water has picked up.

Yulia Zhestkova Grigsby  
+1(646)446-3905 |  
yulia.grigsby@gs.com  
GS & Co. LLC

Alexandra Paulus
+1(212)902-7111 |
alexandra.paulus@gs.com
GS & Co. LLC

Filippo Cuscito  
+44(20)7051-9073 |  
filippo.cuscito@gs.com  
GS International

## Daan Struyven

+1(212)357-4172 | daan.struyven@gs.com GS & Co. LLC

☐ Global oil in transit has increased by 137mb since late March, offsetting nearly 60% of the initial drop as global exports have ramped up and demand has likely fallen (Exhibit 3).

\- US exports accounted for all of the pick-up in oil on water in April-May, while Persian Gulf ex Iran exports drove nearly all of the June recovery.

☐ Some of the demand losses may prove sticky, especially in Asia, as:

\- China crude imports continue to decline and are now down 4.5mb/d YoY despite the moderation in prices.

\- EV sales have accelerated since the beginning of the Hormuz shock, with the EV penetration rate up 3.4pp globally and 11.4pp in China.

The market may be placing an increasing probability on our oil price downside scenario, which features Brent around \$60/bbl by Dec26.

☐ Aside from potentially larger demand scarring, Middle East supply may recover even faster than we expect (for example, UAE exports are already reportedly at 85% of pre-war levels), while production beats outside of the Middle East may continue.

☐ High supply expectations have flipped Dubai prompt timespreads into contango (Exhibit 17).

☐ However, the US oil market is tight following record exports, in contrast to March when US stocks were building.

\- Last week, total US oil inventories hit their lowest level since 1984, while Cushing crude storage dropped below 19mb.

■ Beyond the spot-price selloff, the market is increasingly challenging its prior assumption that long-dated prices need to incorporate a sticky security premium.

☐ While supply disruption risk is high, the ability of the oil market (via elasticity of demand and flexibility of Mideast supply channels) to respond to the sharpest oil supply shock ever has been a key surprise that is likely eroding this security premium.

## Charts of the Week

Exhibit 1: Oil Exports from the Persian Gulf Have Returned to 63% of Normal Levels  
![](images/77495bb49d43053cc3c105f3945a3e3550b5ee3e6bf9eae93311d234a18f7b7a.jpg)  
Includes flows through the Strait of Hormuz, Yanbu, Fujairah, Gulf of Oman, and Botas Ceyhan.

Yanbu is on the west coast of Saudi Arabia, bordering the Red Sea and connected to Saudi eastern oil fields via the East-West pipeline. Fujairah lies east (outside) of the Strait of Hormuz and is connected to Abu Dhabi's onshore fields via the Abu Dhabi Crude Oil Pipeline (ADCOP). The Gulf of Oman connects the Strait to the Arabian Sea (southeast). The Kirkuk-Ceyhan pipeline allows northern Iraqi crude to be pumped through Turkey to the Mediterranean sea. "Normal" flows are assumed to be 20mb/d for Strait of Hormuz and 2025 average for Yanbu (1.4mb/d), Fujairah (1.7mb/d), Gulf of Oman (0mb/d), and Botas Ceyhan (0mb/d).

Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research

Exhibit 2: The US 60-Day Waiver May Unlock Up to Around 60mb of Iran Oil on Water Overhang  
![](images/80bd40f4d69ec10efe213fb1c5f06063fc84b02f38b6625a550f225b17db3b2b.jpg)  
Source: Kpler, GS Global Investment Research

Exhibit 3: Oil in Transit Has Increased by 68mb Since May 31 as Persian Gulf Flows Are Recovering  
![](images/1c3047e814f041aad52adbc61f6cccdf1a1a081f96b18175a50b52ebd920da6e.jpg)  
Source: Kpler, GS Global Investment Research

## 1) Persian Gulf Exports

Exhibit 4: Normalization in Oil Exports From Gulf Producers to Their Pre-War Level May Be Achieved With an 8.5mb/d Increase in Hormuz Flows From Current Levels

![](images/49a638f3cea08c2479ffce8dd608d74ca0352c9bf378128a25c29bbde492c34d.jpg)  
Yanbu is on the west coast of Saudi Arabia, bordering the Red Sea and connected to Saudi eastern oil fields via the East-West pipeline. Fujairah lies east (outside) of the Strait of Hormuz and is connected to Abu Dhabi's onshore fields via the Abu Dhabi Crude Oil Pipeline (ADCOP). The Gulf of Oman connects the Strait to the Arabian Sea (southeast). The Kirkuk-Ceyhan pipeline allows northern Iraqi crude to be pumped through Turkey to the Mediterranean sea.  
Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research

Exhibit 5: We Estimate That 1.2mb/d of Visible OECD SPR Releases Have Reduced the Estimated Hit to Global Commercial Oil Stocks Since March to 4.3mb/d  
![](images/fcf3f900cd427d117ec89339772dfce7cd25d5d21100155e5a5d50a8adf6fcaf.jpg)  
We estimate global oil inventory draws from latest GS oil balance.

![](images/27d98c078a40b14142cd5f3cd97a6c1774ad005bbfe98d28f39b978ea01bd80c.jpg)  
Source: Kpler, GS Global Investment Research

Exhibit 6: The Estimated Total Hit to Oil Flows from the Persian Gulf Decreased to 7.9mb/d (4-Day Moving Average)

![](images/571a7a3ee20c4d51ab136a212a782cf4033f45c44c660e6cc08343dc695afac3.jpg)  
Normal flows are assumed to be 20mb/d for Strait of Hormuz and 2025 average for Yanbu (1.4mb/d), Fujairah (1.7mb/d), Gulf of Oman (0.0mb/d), and Botas Ceyhan (0.0mb/d).

![](images/57b39cef6c012123ea50c0bf9cb36ea2e90f8ebd09aa2b60538222b2757d799a.jpg)  
Hit is calculated relative to normal flows. Redirections include Yanbu, Fujairah, Gulf of Oman, and Botas Ceyhan flows.  
Source: S&P Global Commodities at Sea, Kpler, GS Global Investment Research

Exhibit 7: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 785mb  
![](images/a2f3815c78fe362296b3f01f0c2cab72c7f2fee72f7e0bed3f7697b738cfe284.jpg)  
Source: Kpler, GS Global Investment Research

Oil Tanker Capacity on Both Sides of Hormuz  
![](images/8cf03f54c835b45c26060ce8344a938b8d34860e2916635ab60cab7b70460329.jpg)

Exhibit 8: 35% of the Hit to Persian Gulf Crude/Condensate Exports Is Currently Being Offset, With Contributions From Higher Exports from the US/Russia/Americas Ex US of 11pp/8pp/5pp

![](images/f1d5e9d0b401a9cf0f27ff126effa0c0c20ba8afa807a78bd809b5f362298308.jpg)  
Refined products include LPG.  
Source: Kpler, GS Global Investment Research

## 2) Inventories

Exhibit 9: China and Middle East Landed Visible Inventories Have Drawn by 2.2mb/d and 0.8mb/d, Respectively, Over the Last 14 Days  
![](images/a4addff8ba430c7400a082305f630c3a5d62695f5903837312df7bdfa2c27806.jpg)  
Source: IEA, Kpler, DOE, Euroilstocks, ARA PJK, PAJ, Haver, GS Global Investment Research

Exhibit 10: Global Visible Draws Have Averaged 3.4mb/d Since March 1st

<table><tr><td colspan="5">Visible Oil Stocks, Month-Over-Month Changes (mb/d)</td></tr><tr><td></td><td>June</td><td>May</td><td>April</td><td>Average Since March 1st</td></tr><tr><td>Global Visible Stocks</td><td>-1.8</td><td>-5.5</td><td>-1.4</td><td>-3.4</td></tr><tr><td>Landed Crude Stocks</td><td>-2.5</td><td>-2.9</td><td>-1.8</td><td>-1.7</td></tr><tr><td>OECD</td><td>-1.3</td><td>-2.7</td><td>-2.1</td><td>-1.5</td></tr><tr><td>China</td><td>-1.1</td><td>-0.3</td><td>0.4</td><td>-0.1</td></tr><tr><td>Non-OECD Ex China</td><td>-0.1</td><td>0.1</td><td>0.0</td><td>-0.1</td></tr><tr><td>Landed Products Stocks</td><td>-0.3</td><td>-0.7</td><td>-1.1</td><td>-0.9</td></tr><tr><td>OECD NGL</td><td>0.1</td><td>0.2</td><td>0.4</td><td>0.2</td></tr><tr><td>OECD Refined Products</td><td>0.2</td><td>-0.5</td><td>-1.5</td><td>-0.8</td></tr><tr><td>Non-OECD Total Products</td><td>-0.6</td><td>-0.3</td><td>0.1</td><td>-0.2</td></tr><tr><td>Oil on Water</td><td>1.0</td><td>-1.9</td><td>1.4</td><td>-0.9</td></tr><tr><td>Floating Crude</td><td>-1.3</td><td>-0.9</td><td>0.4</td><td>0.1</td></tr><tr><td>Floating Products</td><td>-0.4</td><td>0.0</td><td>0.0</td><td>0.1</td></tr><tr><td>Crude in Transit</td><td>3.3</td><td>-0.5</td><td>1.4</td><td>-0.2</td></tr><tr><td>Products in Transit</td><td>-0.6</td><td>-0.5</td><td>-0.4</td><td>-0.8</td></tr></table>

Latest observation is today, and data is unsmoothed. “Crude” categories (landed and on water) include both crude and condensate. Month-over-month changes are calculated by taking the end-of-month level, subtracting the previous month’s end-of-month level, and dividing by the number of days.

Exhibit 11: Global Diesel High-Frequency Visible Stocks Increased to 6% Above Their Year-Ago Levels Last Week, While Gasoline Stocks Continued to Trend Downwards to 4% Below Their Year-Ago Levels

![](images/020c15d3ef07fede4f843c4bef3e3c71abe0959810b68a0f8792ef189b72b1fa.jpg)  
Source: DOE, Longzhong, ARA PJK, Fujairah, Singapore Enterprise, IEA, PAJ, GS Global Investment Research

## 3) Refining

Exhibit 12: Estimated Chinese Refineries Runs Have Declined by 1.5mb/d From a Year Ago  
![](images/2c6a4accbdf8eba19a77da033d7c6628f84d166c3119d0bf6ee58f5b11d05168.jpg)  
Source: Oilchem, GS Global Investment Research

Exhibit 13: Japanese Refineries Runs Are Starting to Pick Up  
![](images/35743b3cbb8836a536bc14bb51fc40fb5328f04bdd7802fb5e2fbe0b31f67694.jpg)  
Source: PAJ, GS Global Investment Research

Exhibit 14: The Utilization Rate of US Refineries Is Up 0.3mb/d Year-Over-Year as US Product Margins Remain High  
![](images/94130ed6caa54d40fb36ede5157945499bf0939c34517db19363b498aa8b2d63.jpg)  
Source: EIA, GS Global Investment Research

## 4) Energy Prices

## Energy Prices Across Regions

Exhibit 15: US Wholesale Gasoline Prices Continue to Outperform Regional Counterparts and Products Across the Barrel on Strong Summer Demand and Low Stocks

![](images/f995efe11bee8958b7f26b2a57f5c81e191aa04dbc4780f8a4138205b58e2c5b.jpg)  
Bar labels indicate crude/refined products prices as of June 23rd market close. We consider cash or cash-equivalent prices.  
Source: ICE, Platts, GS Global Investment Research  
Exhibit 16: Global Wholesale Refined Products Margins Continue to Normalize, While Retail Margins Remain Near Their All-Time High

![](images/46b3dfaca5e0b77aacc4c2d359456fbb8318b22235b48de194c318ba53172dcd.jpg)

![](images/95cb4154bcacb671bbacf8d5785b5bc252c1da9f7b3e6bce2fe8ccc1a9afe383.jpg)

The global wholesale refined product price is a demand-weighted average of wholesale price indices in the US, Europe, and Asia, which are themselves demand-weighted averages of gasoline, diesel, jet fuel, naphtha, and fuel oil prices. The global retail refined product price is a simple average of global retail gasoline and diesel price indices, which are each demand-weighted averages of 40 country-level retail product prices.

Source: Platts, EIA, Government Sources, ICE, GS Global Investment Research

## Crude Prices

Exhibit 17: Dubai Prompt Timespreads Remain in Contango, While the Brent Physical Contract Is Now Trading at a Discount to Its Financial Counterpart

![](images/0598afcc32a6156a3536af6f14229004228ee68d515a0292e62ecc43f9b6a90f.jpg)  
Percentiles over a sample from 2011 to the present.

![](images/f2ad7bc9b07a9cd9cd0be4bf76e54939cb761b9015717ffb00228bf0ff4c7785.jpg)  
Percentiles over a sample from 2011 to the present.

Basis represents the difference (in % of 1M ahead futures) between spot physical crude futures and 1M ahead financial futures. We include Brent, Dubai, and WTI in crude basis on the left panel and in 1M/2M timespreads on the right panel.

Source: Platts, CME, GS Global Investment Research

## 5) Demand

Exhibit 18: We Estimate That Global Jet Fuel Demand in June Will be 130kb/d Softer Year-Over-Year, or 6% Below Trend

![](images/aad6624f6dc6e127a4a89665141c2a35bcfe20efb0818d6942da21a3b14bab59.jpg)  
Source: EIA, OAG, GS Global Investment Research

Exhibit 19: Our US Gasoline Demand Nowcast Is Now Roughly In Line With Its Year-Ago Seasonal Levels  
![](images/01db9a4578ca633e51bfbeca444999fddf5bb5a16fc94d6078979ceaea294346.jpg)

![](images/0babde8bfdb16f0873c63fec6d2386d0418990337c93048f162736f48c3c332b.jpg)  
Source: IEA, S&P, Kpler, GTT, Oilchem, MySteel, Bloomberg, GS Global Investment Research

Exhibit 20: Global Crude/Condensate Imports Are Down 5.9mb/d from 2025 Average Levels, and Refined Products Imports Are Down 4.6mb/d

![](images/5248c9a78eb844ee17834bacdeadc954019a995880ced566b95415981c5e1c81.jpg)  
Refined products include LPG.  
Source: Kpler, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Yulia Zhestkova Grigsby, Alexandra Paulus, Filippo Cuscito and Daan Struyven, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yulia Zhestkova Grigsby GS & Co. LLC, Alexandra Paulus GS & Co. LLC, Filippo Cuscito GS International, Daan Struyven GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Disclosure

Iran is subject to comprehensive sanctions by the United States.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States
The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain Goldman

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
