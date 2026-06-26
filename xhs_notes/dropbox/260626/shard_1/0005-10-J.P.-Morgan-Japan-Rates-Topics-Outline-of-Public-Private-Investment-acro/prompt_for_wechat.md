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
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# JPM

# Japan Rates Topics

# Outline of Public–Private Investment across 17 Sectors Begins to Take Shape

## Summary

\- At the joint meeting of the Council on Economic and Fiscal Policy and the Japan Growth Strategy Council held yesterday, the Takaichi administration presented its policy direction for public–private investment. The government envisages total public–private investment exceeding JPY 370 trillion by FY2040, with the growth strategy centered on AI and semiconductors (JPY 186 trillion) and biotechnology (JPY 98 trillion).

\- The framework is designed to use government spending as a catalyst to encourage private investment, and the introduction of a new investment framework under the “Strong and Prosperous Japan” policy from FY2027 is under consideration, alongside potentially bold fiscal expansion.

\- Funding is expected to be arranged through special accounts, with the use of bridge bonds likely. If the public–private mix is similar to that of GX investment, the government share would amount to approximately 15% of the total. Assuming spending is distributed over time, this would imply an annual scale of around JPY 4 trillion.

\- However, the released materials include simulations assuming fiscal spending of around JPY 10 trillion per year, suggesting that a scale closer to this level cannot be ruled out. While the use of special accounts may preserve fiscal discipline in form, a substantial increase in calendar-based JGB issuance from FY2027 is a key concern.

\- Additional fiscal factors are likely to accumulate, including expanded public-private investment, supplementary budgets associated with energy subsidies, consumption tax cuts, and higher defense spending. With multiple fiscal expansion factors progressing simultaneously, fiscal concerns are likely to persist for the time being.

\- The Ministry of Finance will likely seek ways to mitigate the impact of the Takaichi administration's expansionary fiscal stance on the JGB market, but if issuance itself continues to increase, this may exceed the Ministry's capacity to respond. A better balance between expansionary and more prudent fiscal policy (i.e., prioritization across policy measures) will be important.

Japan Markets Research

Takafumi Yamawaki AC (81-3) 6736-1748 takafumi.yamawaki@JPM.com

Hiroki Yagi AC

(81-3) 6736-6783

hiroki.yagi@JPM.com

JPM Securities Japan Co., Ltd.

## Overall Picture of the JPY 370 Trillion Investment Policy

At the joint meeting held yesterday, the government presented the public–private investment policy under the Takaichi administration (Link, Japanese only). Total investment across 17 sectors is estimated to exceed JPY 370 trillion cumulatively through FY2040, with a framework that leverages government spending as a catalyst for private investment.

By sector, AI, semiconductors, digital, and ICT-related areas account for JPY 186 trillion, while biotechnology and drug discovery account for JPY 98 trillion. The resources and energy sector is also sizable at JPY 29 trillion, with these areas forming the core of the growth strategy (Figure 1).

Prime Minister Takaichi also indicated that a new investment framework under the “Strong and Prosperous Japan” policy will be introduced from the FY2027 budget to support these investments. For investments aimed at raising potential growth, no upper limit will be imposed on ministry budget requests. Further details are expected to be included in the Basic Policy to be released in July.

Figure 1: Investment Areas across 17 Sectors

<table><tr><td>Tn JPY</td><td>byFY30-35</td><td>byFY40</td><td>Total</td></tr><tr><td>AI / semiconductors</td><td></td><td>101.6</td><td>101.6</td></tr><tr><td>Digital / cyber security</td><td>42.0</td><td>13.4</td><td>55.4</td></tr><tr><td>Information/ communications</td><td></td><td>28.8</td><td>28.8</td></tr><tr><td>Quantum</td><td></td><td>13.2</td><td>13.2</td></tr><tr><td>Defence industry</td><td></td><td>4.7</td><td>4.7</td></tr><tr><td>Aerospace</td><td></td><td>18.5</td><td>18.5</td></tr><tr><td>Marine</td><td></td><td>3.3</td><td>3.3</td></tr><tr><td>Shipbuilding</td><td>1.1</td><td></td><td>1.1</td></tr><tr><td>Materials</td><td></td><td>16.9</td><td>16.9</td></tr></table>

Source: JPM, Cabinet Office

<table><tr><td>Tn JPY</td><td>byFY30-35</td><td>byFY40</td><td>Total</td></tr><tr><td>Bio technology</td><td></td><td>33.6</td><td>33.6</td></tr><tr><td>Drug/advanced medical</td><td></td><td>64.1</td><td>64.1</td></tr><tr><td>Resources/Energy/GX</td><td></td><td>28.8</td><td>28.8</td></tr><tr><td>Fusion energy</td><td></td><td>3.1</td><td>3.1</td></tr><tr><td>Disaster prevention</td><td>2.6</td><td></td><td>2.6</td></tr><tr><td>Ports logistics</td><td></td><td>1.2</td><td>1.2</td></tr><tr><td>Food Tech</td><td></td><td>9.7</td><td>9.7</td></tr><tr><td>Content (Game Anime etc)</td><td>9.2</td><td></td><td>9.2</td></tr></table>

## Establishment of Special Accounts and Use of Bridge Bonds

From a bond market perspective, the key focus is the extent to which these measures will translate into additional JGB issuance. These investments are planned over multiple years, and there is consideration to revise the current principle of limiting fund management to within three years, allowing for more flexible funding operations.

In addition, the new investment framework under the “Strong and Prosperous Japan” policy will be managed through a special account separate from the General Account, and bridge bonds are likely to be used for funding purposes. Bridge bonds provide a mechanism to cover temporary funding shortfalls, to be repaid using future revenues, and have already been used for GX Economic Transition Bonds, Semiconductor & AI Bonds, and Childcare Support Bonds.

That said, the scale and timing of government spending within total public–private investment remain unclear at this stage. Prime Minister Takaichi has only stated that “sufficient scale will be secured while ensuring fiscal sustainability.” While some sector estimates were presented through FY2030–2035, most figures extend to FY2040, making it difficult to estimate the scale and timing of government spending at this point.

One useful reference point is the GX investment framework. Under that framework, government upfront investment of JPY 20 trillion over 10 years is designed to induce total public–private investment exceeding JPY 150 trillion, implying a government share of approximately 15% (Figure 2). Applying a similar approach, the government share of the JPY 370 trillion investment would also be around 15%, which, if distributed evenly over FY2027–2040, implies annual spending of roughly JPY 4 trillion.

On the other hand, the materials also include simulations under the “medium- to long-term economic and fiscal outlook under the Japan Growth Strategy” (Link, Japanese only), which assume additional fiscal spending of JPY 10 trillion in FY2027, followed by increases broadly in line with inflation and wage growth. Even under this assumption, the debt-to-GDP ratio is projected to decline, implying that actual spending could exceed the earlier estimate of JPY 4 trillion and move closer to JPY 10 trillion.

Figure 2: List of Bridge Bonds

<table><tr><td colspan="2">GX Economy Transition Bonds (CT Bonds)</td></tr><tr><td>Purpose</td><td>Public-private GX investment (JPY150tn+)Govt upfront (JPY20tn)</td></tr><tr><td>Issuance</td><td>FY2023~2032</td></tr><tr><td>Issued</td><td>FY23 1.6tn · FY24 1.4tn · FY25 1.2tn · FY26 1.0tn</td></tr><tr><td>Redemption resources</td><td>Carbon pricing- FY28: Fossil fuel levy on importers- FY33: Paid emissions allowances for power generators</td></tr><tr><td>Maturity</td><td>By FY2050</td></tr><tr><td>Account</td><td>Energy Policy Special Account</td></tr><tr><td colspan="2">Semiconductor &amp; AI Bonds</td></tr><tr><td>Purpose</td><td>Semiconductors / AI funding (FY25–30)Public support 10tn+Subsidies ~6tn / Financial support 4tn+</td></tr><tr><td>Issuance</td><td>FY2025~2030</td></tr><tr><td>Issued</td><td>FY25 (0.0兆円) · FY26 (0.8兆円)</td></tr><tr><td>Redemption resources</td><td>Government financial resources : General account and FILP funds / Repayments from funds / Dividends and proceeds from asset sales</td></tr><tr><td>Maturity</td><td>By FY2050</td></tr><tr><td>Account</td><td>Energy Policy Special Account</td></tr><tr><td colspan="2">Child &amp; Childcare Support Bonds</td></tr><tr><td>Purpose</td><td>Front-loaded measures (FY25–27, total 3.6tn)</td></tr><tr><td>Issuance</td><td>FY2024~2028</td></tr><tr><td>Issued</td><td>FY24 0.2tn · FY25 1.1tn · FY26 0.5tn</td></tr><tr><td>Redemption resources</td><td>Childcare support contributions (from FY26)Collected as a surcharge on health insurance premiums</td></tr><tr><td>Maturity</td><td>By FY2051</td></tr><tr><td>Account</td><td>Child and Childcare Support Special Account</td></tr></table>

Source: JPM estimates, MoF

## Fiscal Concerns to Persist

The investment framework involves the use of special accounts, which may avoid deterioration in the General Account primary balance, and the boost to GDP from investment may help prevent an increase in the debt-to-GDP ratio. However, even if fiscal discipline is maintained in form through the use of special accounts, underlying JGB issuance pressure could in fact intensify.

As multiple fiscal factors accumulate simultaneously, as outlined below, fiscal concerns are likely to persist in the bond market for the time being. The Ministry of Finance will likely seek ways to mitigate the market impact of the Takaichi administration's expansionary fiscal stance, but if issuance volumes continue to rise, this may exceed its

ability to respond.

Attention will also focus on whether any changes are announced in JGB issuance plans from July onward. A better balance between expansionary and prudent fiscal policy (i.e., prioritizing policy measures, see Figure 3) will be required.

\- Public–Private Investment: Bridge bond issuance to date has remained relatively limited, with GX bonds totaling JPY 5.2 trillion (FY23–26), Semiconductor & AI bonds JPY 0.8 trillion (FY25–26), and Childcare bonds JPY 1.8 trillion (FY24–26). However, if fiscal costs of around JPY 10 trillion per year are required solely for this public–private investment framework, the burden (JGB supply) on the bond market would become significantly heavier.

\- Supplementary Budget (Second Round): A first supplementary budget of JPY 3.1 trillion has already been implemented for energy-related measures. However, gasoline subsidies of JPY 400–500 billion per month could be depleted in the near term, creating the possibility that a second supplementary budget will be required at an early stage.

\- Consumption Tax Measures: A cross-party national council has proposed cutting the consumption tax rate on food to $1\%$ for two years from April 2027, and introducing cash transfers to low- and middle-income households from around autumn 2027. The measures would be funded using roughly JPY 600 billion, equivalent to one percentage point of the food consumption tax. The overall fiscal cost is expected to reach around JPY 5 trillion annually.

However, several concerns remain, including (1) the potential need for fiscal support for sectors negatively affected by the tax cut (e.g., restaurants and agriculture), (2) the risk that the tax rate cannot be restored to 8% after two years, and (3) possible delays in the design of the refundable tax credit system intended to replace the tax cuts. Attention will focus on whether an exit strategy for the tax cut and the feasibility of the refundable tax credit will be clarified.

\- Defense Spending: Over the medium to long term, defense spending—already expanded to JPY 9.0 trillion in the FY2026 initial budget—will remain a key focus. Funding has been secured through a dedicated scheme (FY2023–2027) drawing on transfers from the Foreign Exchange Fund Special Account, repayments from public entities, and proceeds from selling government assets. However, such sources alone are insufficient, and defense-related tax increases (corporate tax, income tax, and tobacco tax) have already been implemented. Beyond FY2028, reliance on this funding scheme will no longer be possible, raising concerns over a “defense funding cliff” as funding shortages emerge. If defense spending is to be raised to 2% of GDP (JPY 13.4 trillion) in line with the revised national security strategy, this would add further pressure for fiscal expansion.

Figure 3: Fiscal Concerns in the FY2026–2029 Budget

<table><tr><td>FY26 Supp.Budget</td><td>- JPY +3.1tn in total; no increase in JGB issuance in the market (fully pre-funded)</td></tr><tr><td>FY26 Supp.Budget 2nd</td><td>- Additional energy budget may be required as existing funds are depleted- Possible subsidies for firms facing energy supply constraints?</td></tr><tr><td>FY27 Budget</td><td>- Bridge bond issuance for growth strategy spending (~JPY 10tn per year?)- If consumption tax cuts are implemented → funding shortfall of ~JPY 4–5tn per year- Cash transfers (equivalent to 1% of the food consumption tax)- Possible support for adversely affected sectors (restaurants, farmers, etc.)</td></tr><tr><td>FY28 Budget</td><td>- “Defense funding cliff” → significant shortfall in defense funding- Continued burden from bridge bond issuance for growth strategy spending- JGB interest payment burden likely to increase significantly</td></tr><tr><td>FY29 Budget</td><td>- Whether the food consumption tax rate can be restored to 8%?- If restored → large transfers to low-income households likely?- Whether a smooth transition to refundable tax credits is achievable?</td></tr></table>

Source: JPM estimates, BoJ

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance obligations when making investment decisions.

Any digital or crypto assets discussed in this research report are subject to a rapidly changing regulatory landscape. For relevant regulatory advisories on crypto assets, including bitcoin and ether, please see https://www.JPM.com/disclosures/cryptoasset-disclosure.

The author(s) of this research report may not be licensed to carry on regulated activities in your jurisdiction and, if not licensed, do not hold themselves out as being able to do so.

Exchange-Traded Funds (ETFs): JPM Securities LLC (“JPMS”) acts as authorized participant for substantially all U.S.-listed ETFs. To the extent that any ETFs are mentioned in this report, JPMS may earn commissions and transaction-based compensation in connection with the distribution of those ETF shares and may earn fees for performing other trade-related services, such as securities lending to short sellers of the ETF shares. JPMS may also perform services for the ETFs themselves, including acting as a broker or dealer to the ETFs. In addition, affiliates of JPMS may perform services for the ETFs, including trust, custodial, administration, lending, index calculation and/or maintenance and other services.

Options and Futures related research: If the information contained herein regards options- or futures-related research, such information is available only to persons who have received the proper options or futures risk disclosure documents. Please contact your JPM Representative or visit https://www.theocc.com/components/

[中间内容因长度限制已省略]

PMS”) is a member of the NYSE, FINRA, SIPC, and the NFA. JPM Chase Bank, N.A. is a member of the FDIC. Material published by non-U.S. affiliates is distributed in the U.S. by JPMS who accepts responsibility for its content.

General: Additional information is available upon request. The information in this material has been obtained from sources believed to be reliable. While all reasonable care has been taken to ensure that the facts stated in this material are accurate and that the forecasts, opinions and expectations contained herein are fair and reasonable, JPM Chase & Co. or its affiliates and/or subsidiaries (collectively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase &
"""
