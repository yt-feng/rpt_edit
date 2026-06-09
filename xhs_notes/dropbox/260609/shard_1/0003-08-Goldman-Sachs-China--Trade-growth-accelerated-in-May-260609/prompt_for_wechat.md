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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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
# China: Trade growth accelerated in May

## Bottom line:

China's trade growth accelerated in May and came in above consensus expectations (exports: +19.4% yoy, imports: +27.5% yoy). The pickup in headline export growth was likely driven by stronger US-bound shipments, partly supported by a low base last year. By region, Chinese exports rose sequentially across major trading partners, except the EU and Latin America, while Chinese imports from major trading partners fell (except the US and Japan). By product, export value rose broadly from April to May, with tech-related products rising the most. Higher import value growth seems to be more price-driven than volume-led, as evidenced by the higher chip and energy prices. Overall, the trade surplus was US\$105.4bn in May, up from US\$84.8bn in April.

Asia-MAP Scores:

Exports: +3 (3, +1)

Imports: 0 (3, 0)

## Key numbers:

USD-denominated:

Exports: $19.4\%$ yoy in May (GS: $15.0\%$ , Bloomberg consensus: $15.0\%$ ). April: $14.1\%$ yoy. Sequential growth (seasonally adjusted by GS): $3.0\%$ non-annualized in May vs. $4.2\%$ in April.

Imports: 27.5% yoy in May (GS: 30.0%, Bloomberg consensus: 26.0%). April: 25.3% yoy. Sequential growth (seasonally adjusted by GS): 0.1% non-annualized in May vs. 2.2% in April.

Trade balance: US\$105.4bn NSA in May (GS: US\$86.2bn, Bloomberg consensus: US\$92.3bn). April: US\$84.8bn.

RMB-denominated:

Exports: $13.8\%$ yoy in May vs. $9.8\%$ yoy in April.

Imports: 21.6% yoy in May vs. 20.6% yoy in April.

## Main points:

1. In year-over-year terms, China's trade growth accelerated in May. Exports increased by $19.4\%$ yoy (vs. $14.1\%$ yoy in April), and imports increased by $27.5\%$ yoy (vs. $25.3\%$ yoy in April; Exhibit 1). In sequential terms, exports grew by $3.0\%$ sa

Chelsea Song

+852-2978-0106

chelsea.song@gs.com

GS (Asia) L.L.C.

non-annualized in May (vs. +4.2% in April), and imports increased by 0.1% sa non-annualized in May (vs. +2.2% in April). China's trade surplus increased to US\$105.4bn in May (not seasonally adjusted), vs. US\$84.8bn in April (Exhibit 2). Today's release of trade data only covers major trading partners and products. $^{1}$ The detailed breakdown of trade by country and by product will be released on June 20.

2. By major destination, Chinese nominal exports to major trading partners increased sequentially in May, except for the EU and Latin America (Exhibit 3). Chinese imports from major trading partners fell across major trading partners, except for the US and Japan (Exhibit 4). Among major DM countries, China's exports to the US increased by $35.4\%$ yoy in May (vs. $+11.3\%$ yoy in April), with a sequential gain of $1.5\%$ (mom sa non-annualized). The strong yoy increase in exports to the US partly reflects a low base last year. China's imports from the US also increased by $20.4\%$ yoy in May (vs. $+9.0\%$ yoy in April). Exports to the EU increased by $7.6\%$ yoy in May (vs. $+13.4\%$ yoy in April), while imports from the EU fell by $1.3\%$ yoy in May (vs. $+14.5\%$ yoy in April). Among major EM countries, exports to ASEAN increased by $24.3\%$ yoy in May (vs. $+15.2\%$ yoy in April), with a sequential gain of $2.6\%$ . Exports to other EMs (such as South Korea and Russia) and Africa remained strong, rising $21.9\%$ yoy and $18.6\%$ yoy respectively. Imports from major EM countries declined from April to May.

3. By major category and in sequential terms, export value rose broadly from April to May, with tech-related products rising the most, followed by metals and housing-related products. In year-over-year terms, semiconductors export value increased by $110.9\%$ yoy in May (vs. $+99.6\%$ in April), while its export volume rose only modestly by $2.1\%$ (vs. $+3.6\%$ in April), suggesting the increase was largely price-driven. Among metal products, exports of aluminium increased by $38.5\%$ yoy in May (vs. $+31.4\%$ yoy in April), and exports of rare-earth ores and minerals surged by $237.4\%$ yoy in May (vs. $+196.5\%$ yoy in April), mostly driven by price effects. Among housing-related products, exports of home appliances rose by $9.2\%$ yoy in May (vs. $+7.0\%$ yoy in April).

4. Among major categories and in sequential terms, import value of semiconductors and automobiles increased in May, while imports of energy, metal ores, and agricultural products fell. In year-over-year terms, import value growth of semiconductors increased by 68.0% yoy in May (vs. 54.7% yoy in May), driven entirely by higher prices, as its import volume decreased by 1% yoy (vs. +11.2% in April). Higher prices continued to contribute to the increase in year-over-year import growth of energy goods. Import value of crude oil increased by 15.3% yoy in May (vs. +13,2% yoy in April), while import volume of crude oil fell by 29.0% yoy in May (vs. -20.0% yoy in April). Import value of natural gas increased by 11.0% yoy in May (vs. -14.5% yoy in April), while import volume remained roughly flat in May (vs. -12.9% yoy in April). Among major metal ores, the import value of copper ore increased by 34.0% yoy in May (vs. +16.3% yoy in April), while its import volume fell by 1.4% yoy (vs. -19.6% yoy in April). Import value of aircraft also rose sharply by 443% yoy in May (vs. -45.8% yoy in April), likely as part of the initial purchase agreement with the US following the Trump-Xi meeting in May.

## Chelsea Song

Exhibit 1: Year-over-year nominal trade growth accelerated in May  
![](images/d72c967398e20cc0d587f50230f3ce573b00cb1f9ec132a22e357da5778a2d4d.jpg)

<details>
<summary>line chart</summary>

| Year | Exports | Imports |
|------|---------|---------|
| 2018 | ~25     | ~20     |
| 2019 | ~15     | ~10     |
| 2020 | ~-15    | ~-10    |
| 2021 | ~60     | ~50     |
| 2022 | ~25     | ~30     |
| 2023 | ~-10    | ~-5     |
| 2024 | ~5      | ~0      |
| 2025 | ~10     | ~5      |
| 2026 | ~20     | ~30     |
</details>

Source: China Customs

Exhibit 2: China's trade surplus increased to US\$105.4bn in May  
![](images/de8073737aa30cd1de25097e26a86956541ae9425a99fa719de0d9840683d582.jpg)

<details>
<summary>area chart</summary>

| Year | Trade Balance (USD bn) |
|------|------------------------|
| 2018 | ~25                    |
| 2019 | ~50                    |
| 2020 | ~-10                   |
| 2021 | ~75                    |
| 2022 | ~90                    |
| 2023 | ~75                    |
| 2024 | ~60                    |
| 2025 | ~100                   |
| 2026 | ~110                   |
</details>

Source: China Customs

Exhibit 3: Chinese nominal exports to major trading partners increased sequentially in May, except the EU and Latin America  
![](images/8c138c56359a2b1ec168057ac3c0e0ce634e2ec1f7f40a8b8753197f21c358d0.jpg)

<details>
<summary>line chart</summary>

| Year | Headline | ASEAN | EU | Africa | Latin America | Japan | US | Others (mostly EM) |
|------|----------|-------|----|--------|---------------|-------|----|---------------------|
| 2019 | ~100     | ~100  | ~100 | ~100   | ~100          | ~100  | ~100 | ~100                |
| 2020 | ~100     | ~100  | ~75  | ~100   | ~100          | ~100  | ~75  | ~100                |
| 2021 | ~130     | ~130  | ~110 | ~130   | ~140          | ~110  | ~120 | ~130                |
| 2022 | ~150     | ~175  | ~130 | ~150   | ~180          | ~130  | ~140 | ~150                |
| 2023 | ~140     | ~175  | ~120 | ~140   | ~200          | ~120  | ~130 | ~140                |
| 2024 | ~145     | ~165  | ~125 | ~155   | ~185          | ~125  | ~135 | ~155                |
| 2025 | ~155     | ~185  | ~135 | ~175   | ~225          | ~135  | ~145 | ~175                |
| 2026 | ~175     | ~225  | ~145 | ~245   | ~225          | ~145  | ~165 | ~200                |
| 2027 | ~180     | ~235  | ~150 | ~235   | ~235          | ~150  | ~175 | ~225                |
</details>

Chinese exports to the US/EU/Japan/ASEAN/LatAm/Africa were around 13.2%/14.6%/4.2%/17.1%/7.8%/5.4% of total exports in 2025. Overall they accounted for 62% of Chinese exports.  
Source: China Customs, GS Global Investment Research

Exhibit 4: Chinese imports from major trading partners fell sequentially in May, except the US and Japan  
![](images/32e553f0787a1063c3f171170cc9be8f2bf63bc8e59737cd5b64c48b4cc9df01.jpg)

<details>
<summary>line chart</summary>

| Year | Headline | ASEAN | Latin America | Japan | EU | US | Africa | Others (mostly EM) |
|------|----------|-------|---------------|-------|----|----|--------|---------------------|
| 2019 | 100      | 80    | 110           | 100   | 100| 100| 100    | 100                 |
| 2020 | 100      | 100   | 80            | 90    | 90 | 90 | 80     | 90                  |
| 2021 | 130      | 140   | 150           | 120   | 110| 150| 120    | 130                 |
| 2022 | 140      | 150   | 160           | 130   | 120| 160| 140    | 140                 |
| 2023 | 130      | 140   | 150           | 120   | 110| 150| 130    | 130                 |
| 2024 | 140      | 150   | 160           | 130   | 120| 140| 140    | 140                 |
| 2025 | 130      | 140   | 150           | 120   | 110| 130| 130    | 130                 |
| 2026 | 150      | 160   | 180           | 140   | 130| 170| 160    | 170                 |
| 2027 | 160      | 180   | 190           | 150   | 140| 180| 170    | 180                 |
</details>

Chinese imports from the US/EU/Japan/ASEAN/LatAm/Africa were around 6.1%/10.3%/6.2%/15.5%/9.3%/4.6% of total imports in 2025. Overall they accounted for 52% of Chinese imports.  
Source: China Customs, GS Global Investment Research

## The China Economics Team

## Andrew Tilton

+852-2978-1802

andrew.tilton@gs.com

GS (Asia) L.L.C.

## Hui Shan

+852-2978-6634

hui.shan@gs.com

GS (Asia) L.L.C.

## Lisheng Wang

+852-3966-4004

lisheng.wang@gs.com

GS (Asia) L.L.C.

## Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

## Yuting Yang

+852-2978-7283

yuting.y.yang@gs.com

GS (Asia) L.L.C.

## Chelsea Song

+852-2978-0106

chelsea.song@gs.com

GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Chelsea Song, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Chelsea Song GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annual audit compliance report can be found at this link: https://publishing.gs.com/content/site/india-annual-compliance-report.html. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no responsibility for any investment decisions that may be taken by a client or any other person based on this research report. Singapore: GS (Singapore) Pte. (Company Number: 198602165W), which is regulated by the Monetary Authority of Singapore, accepts legal responsibility for this research, and should be cont

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
