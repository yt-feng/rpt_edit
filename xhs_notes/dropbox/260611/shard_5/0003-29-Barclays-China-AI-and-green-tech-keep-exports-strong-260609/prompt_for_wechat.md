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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`BARC`。标题格式建议：`# BARC：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份BARC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
China

# AI and green-tech keep exports strong

Exports accelerated further in May, exceeding expectations amid a global manufacturing upswing. AI-related and green-tech goods remained key drivers, supported by the AI investment boom and energy shock-driven demand for renewables. Imports were lifted by higher commodity and electronics prices.

• May: 19.4% y/y for exports, and 27.4% y/y for imports (both in USD terms)  
- Bloomberg consensus (BARC): 15% y/y (14%) for exports, and 26% y/y (25%) for imports  
- April: $14.1\%$ y/y for exports, and $25.3\%$ y/y for imports (both in USD terms)

China's export growth accelerated further, rising 19.4% y/y in May following a 14.1% increase in April, exceeding both the market and our expectations (Bloomberg: 15%, BARC: 14%). Breakdown data suggest stronger shipments to the US and across the region (ASEAN, Korea, Japan and Taiwan), while shipments to the EU and UK softened. The robust performance came against the backdrop of 1) a continued uptick in global manufacturing activity, evidenced by the global manufacturing PMI holding at a four-year high of 52.6 in May despite the prolonged energy shock, and 2) broad-based strength across major manufacturing exporters, ranging from low-to-mid product exports from Vietnam (May: 18% y/y), to high-end oriented product exports from Korea (May: 53.2%), to the full-supply-chain exports from China (May: 19.4%).

Demand for high-tech products, particularly AI-related and green-tech goods, remained a key driver, helping to alleviate concerns over the impact of the Middle East energy shock on external demand. The ongoing global AI capex cycle continues to underpin demand for China's AI-related exports, given the country is a key supplier of AI manufactured components. High-tech exports accounted for 29.8% of total export value in May, growing 51% y/y (April: 39%), with notable acceleration in semiconductors (+111%) and automatic data processing equipment and parts (+66%). At the same time, the energy shock is supporting demand for renewable products, while persistent geopolitical tensions could further accelerate the global green transition, an area where China remains well positioned as a leading low-cost, high-quality supplier. Year-to-date data show sustained double-digit growth in EVs, lithium batteries, wind turbines, and solar cells.

## Details of May export data

\- By destination: Trade flows between the US and China are showing signs of continued normalization, with shipments to the US surging $35.4\%$ y/y (April: $11.3\%$ ) partly helped by a low base a year earlier following the Liberation Day tariffs. On a sequential basis, exports to

## Ying Zhang

+852 2903 2652

ying.zhang3@BARC.com

BARC Bank, Hong Kong

## Yingke Zhou

+852 2903 2653

yingke.zhou@BARC.com

BARC Bank, Hong Kong

## Jian Chang

+852 2903 2654

jian.chang@BARC.com

BARC Bank, Hong Kong

the US rose by 6.2% m/m-better than the 2022–24 average of around 5.6% (excluding tariff-distorted dynamics in 2025)-pointing to recovery in shipment momentum. It contributed 3.2pp to headline export growth, well above the 1.2pp recorded in April. Meanwhile, regional exports to ASEAN (May: 24.3%, April: 15.2%) and to Japan, Korea and Taiwan (May: 27.5%, April: 16.8%) strengthened further. In contrast, export growth to the EU (May: 7.6%, April: 13.4%) and the UK (May: 1.7%, April: 9.6%) weakened. Moreover, shipments to Africa continued to expand at double-digit pace (May: 18.6%, April: 17.3%), while exports to LatAm softened.

\- By product: Most major export categories accelerated in May. Semiconductor exports value more than doubled from a year earlier, up 110.9% y/y following an already strong 99.6% increase in the previous month. Auto exports remained resilient, rising 39% y/y, although softening from the 44% increase in April. Exports of mechanical and electrical products grew 27.4% y/y, up from 20.3% previously, while home appliance exports continued to expand. Exports of furniture, general equipment and machinery also reversed to pick up in May.

FIGURE 1. China May exports accelerated...  
![](images/a05aaa87a57396264600e606778f084f758d3a9b6dc0d8fb1e8282c9da32634f.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date    | Trade balance (USD bn, RHS) | Exports (% y/y) | Imports (% y/y) |
|---------|-----------------------------|-----------------|-----------------|
| Nov-23  | 12                          | 0               | 0               |
| May-24  | 18                          | 60              | 30              |
| Nov-24  | 18                          | 120             | -30             |
| May-25  | 24                          | 60              | 30              |
| Nov-25  | 24                          | 120             | 90              |
| May-26  | 24                          | 120             | 150             |
</details>

Source: Wind, BARC

FIGURE 2. ... with faster regional trade (Asean, Japan, Korea and Taiwan) and shipments to the US  
![](images/133ddd7dfcb72121ac31ce30bcb4601c5fd3d13905c3f7c8e7121b7d3c1c501e.jpg)

<details>
<summary>line chart</summary>

| Date   | Exports value: headline | US  | EU  | UK  | ASEAN | Africa |
|--------|--------------------------|-----|-----|-----|-------|--------|
| Nov-23 | ~5                       | ~5  | ~-10| ~-5 | ~-5   | ~-5    |
| May-24 | ~10                      | ~5  | ~10 | ~-10| ~20   | ~-25   |
| Nov-24 | ~10                      | ~10 | ~10 | ~-5 | ~10   | ~20    |
| May-25 | ~5                       | ~-30| ~10 | ~10 | ~20   | ~40    |
| Nov-25 | ~10                      | ~-30| ~10 | ~-5 | ~30   | ~50    |
| May-26 | ~20                      | ~35 | ~10 | ~-5 | ~25   | ~20    |
</details>

Source: Wind, BARC

FIGURE 3. Strong exports were led by AI-related and green-tech products  
![](images/1dfd1d653ff5391857c6bdd327d75cef35fcdc3ca52dc71530c8c558bdab2a94.jpg)

<details>
<summary>bar chart</summary>

| Category | 2025 export value growth (%) | 2026YTD growth (%) |
| :--- | :---: | :---: |
| Semiconductor | 27.0 | 90.0 |
| Drones | 94.0 | 77.0 |
| Autos | 21.0 | 50.4 |
| Wind turbines | 48.0 | 47.7 |
| Lithium-ion batteries | 25.0 | 47.6 |
| Solar cells | -5.0 | 35.4 |
| Transformers | 35.0 | 31.3 |
| Ships | 27.0 | 26.5 |
| Overall exports | 5.0 | 19.4 |
</details>

Source: Wind, BARC

FIGURE 4. High frequency shipping data showed still strong exports in early June  
![](images/4c79f80b5f401881704d8d4934157bfb038c3f8d3fb6919235550220456da73b.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| 1    | 5.9  | 6.1  | 6.5  |
| 5    | 5.3  | 5.3  | 7.4  |
| 9    | 4.4  | 5.6  | 5.6  |
| 13   | 5.9  | 6.0  | 6.8  |
| 17   | 6.2  | 6.5  | 6.8  |
| 21   | 6.0  | 6.5  | 6.9  |
| 25   | 6.3  | 6.7  | -    |
| 29   | 6.4  | 6.5  | -    |
| 33   | 6.2  | 6.8  | -    |
| 37   | 6.5  | 6.7  | -    |
| 41   | 6.4  | 6.5  | -    |
| 45   | 6.3  | 6.8  | -    |
| 49   | 6.2  | 6.7  | -    |
| 53   | 5.6  | 6.0  | -    |
</details>

Source: Wind, BARC

## May headline imports posted a strong growth due to price effects

Imports have continued to exceed expectations this year. Against the backdrop of surging energy and semiconductor related prices, China's import value posted a solid growth of 27.4% y/y in May, following a 25.3% increase in April, supported by robust imports of mechanical and electrical products (May: 38.2%, April: 33.5%) and commodities (May: 16.4%, April: 13.3%). In contrast, imports of agricultural products softened, while auto imports remained weak, falling 25% y/y after a 34% decline previously.

On a volume basis, imports of energy-related products showed mixed developments. Crude oil imports fell at a faster pace of 29% y/y, following a 20% decline in April. Imports of coal continued to decline, but the pace moderated to -7.7% versus -12.5% previously. In contrast, natural gas imports stabilized after two consecutive months of double-digit declines (May: 0%; April: -12.9%). Market reports suggest a pickup in LNG purchases since mid-April $^{1}$ , driven by expectations of stronger summer power demand, with momentum extending into June. Major buyers have stepped up purchases, increasing imports from Canada, Malaysia, and Russia to offset reduced LNG shipments from Qatar.

Imports of industrial materials showed mixed developments: iron ore import volume growth reversed to fall, while steel imports declined for a second month, though at a slower pace. In contrast, copper imports accelerated, up 4.4% versus 2.7% previously.

Import value of agricultural products rose by 4% following a 20% increase previously. China has agreed to expand agriculture trade with the US following the mid-May Trump–Xi summit, with the US readout noting purchases of at least USD17bn of US agricultural products annually in 2026–2028, on top of earlier soybean commitments. Soybean imports moderated, falling 10% (April: +49.3%) in value terms and 15% (April: +39.5%) in volume in May. That said, the import level of 11.79 million metric tons was still the second highest on record for the month, supported by strong Brazil supplies and faster customs clearance $^{2}$ .

FIGURE 5. Imports of mechanical and electrical products accelerated...  
![](images/510359e0df8212db73a3a9f80547dabe2ada268b0d53eb6390ad4b62f8ca07fe.jpg)

<details>
<summary>line chart</summary>

| Date   | Imports value: headline | Commodities (iron ore, crude oil and copper) | Mechanical & electrical products | Agricultural products | Autos |
|--------|--------------------------|-----------------------------------------------|-----------------------------------|------------------------|-------|
| May-23 | -5                       | -10                                           | -15                               | -5                     | -30   |
| Feb-24 | 5                        | 10                                            | 10                                | 5                      | 20    |
| Nov-24 | 0                        | -10                                           | 0                                 | -10                    | -50   |
| Aug-25 | 5                        | -10                                           | 10                                | 5                      | -50   |
| May-26 | 30                       | 15                                            | 40                                | 20                     | -40   |
</details>

Source: Wind, BARC

FIGURE 6. ...with semiconductor import surging on a value basis  
![](images/79e4104a4c23920168cf6b1a21542f64baa921f360696574b97e4a60af392179.jpg)

<details>
<summary>line chart</summary>

| Date   | Semiconductor imports volume | Semiconductor imports value |
|--------|------------------------------|-----------------------------|
| Nov-18 | -10                          | -5                          |
| May-20 | 60                           | 30                          |
| Nov-21 | 20                           | 25                          |
| May-23 | -15                          | -40                         |
| Nov-24 | 15                           | 10                          |
| May-26 | 10                           | 70                          |
</details>

Source: Wind, BARC

FIGURE 7. Imports of steel and iron ore stayed soft  
![](images/d1bc230701bb026f2bae609caa63101240561f7b8abbf87600b2b8f35aa14e3b.jpg)

<details>
<summary>line chart</summary>

| Date   | Iron ore | Copper | Steel |
|--------|----------|--------|-------|
| May-23 | ~5       | ~-5    | ~-25  |
| Feb-24 | ~10      | ~25    | ~-10  |
| Nov-24 | ~5       | ~20    | ~-15  |
| Aug-25 | ~10      | ~-15   | ~-20  |
| May-26 | ~5       | ~5     | ~-10  |
</details>

Source: Wind, BARC

FIGURE 8. Imports of crude oil weakened further  
![](images/40b2d0bc6c927575c711b294f8bb1b6b8e89c38b47a4eb2d7d98e74a1be69727.jpg)

<details>
<summary>line chart</summary>

| Date   | Coal | Crude oil | Natural gas |
|--------|------|-----------|-------------|
| May-23 | 70   | 45        | 15          |
| Feb-24 | 50   | 5         | 20          |
| Nov-24 | 25   | 10        | 15          |
| Aug-25 | -20  | 10        | 0           |
| May-26 | -10  | -30       | -10         |
</details>

Source: Wind, BARC

## Analyst(s) Certification(s):

We, Yingke Zhou, Jian Chang and Ying Zhang, hereby certify (1) that the views expressed in this research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC").

All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

For current important disclosures regarding any issuers which are the subject of this research report please refer to https://publicresearch.barlays.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that BARC may have a conflict of interest that could affect the objectivity of this report. BARC Capital Inc. and/or one of its affiliates regularly trades, generally deals as principal and generally provides liquidity (as market maker or otherwise) in the debt securities that are the subject of this research report (and related derivatives thereof). BARC trading desks may have either a long and / or short position in such securities, other financial instruments and / or derivatives, which may pose a conflict with the interests of investing customers. Where permitted and subject to appropriate information barrier restrictions, BARC fixed income research analysts regularly interact with its trading desk personnel regarding current market conditions and prices. BARC fixed income research analysts receive compensation based on various factors including, but not limited to, the quality of their work, the overall performance of the firm (including the profitability of the Investment Banking Department), the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst. To the extent that any historical pricing information was obtained from BARC trading desks, the firm makes no representation that it is accurate or complete. All levels, prices and spreads are historical and do not necessarily represent current market levels, prices or spreads, some or all of which may have changed since the publication of this document. BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations and trade ideas contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

## Disclosure(s) regarding Information Sources

Bloomberg® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”) and the Bloomberg Indices are trademarks of Bloomberg. Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Bloomberg does not approve or endorse this material, or guarantee the accuracy or completeness of any information herein, or make any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, Bloomberg shall have no liability or responsibility for injury or damages arising in connection therewith.

All pricing information is indicative only. Unless otherwise indicated, prices are sourced from LSEG Data & Analytics and reflect the closing price in the relevant trading market, which may not be the last available price at the time of publication.

## Types of investment recommendations produced by BARC FICC Research:

In addition to any ratings assigned under BARC' formal rating systems, this publication may contain investment recommendations in the form of trade ideas, thematic screens, scorecards or portfolio recommendations that have been produced by analysts in FICC Research. Any such investment recommendations produced by non-Credit Research teams shall remain open until they are subsequently amended, rebalanced or closed in a future research report. Any such investment recommendations produced by the Credit Research teams are valid at current market conditions and may not be otherwise relied upon.

## Disclosure of other investment recommendations produced by BARC FICC Research:

BARC FICC Research may have published other investment recommendations in respect of the same securities/instruments recommended in this research report during the preceding 12 months. To view all investment recommendations published by BARC FICC Research in the preceding 12 months please refer to https://live.barcap.com/go/research/Recommendations.

BARC does not assign ratings to asset backed securities. BARC Capital Inc. and/or one of its affiliates may have acted as an underwriter for public offerings of any asset backed securities that are otherwise recommended in trade ideas contained within its securitised research reports.

## Legal entities involved in producing BARC:

BARC Bank PLC (BARC, UK)

BARC Capital Inc. (BCI, US)

BARC Bank Ireland PLC, Frankfurt Branch (BBI, Frankfurt)

BARC Bank Ireland PLC, Paris Branch (BBI, Paris)

BARC Bank Ireland PLC, Milan Branch (BBI, Milan)

BARC Se

[中间内容因长度限制已省略]

 scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
