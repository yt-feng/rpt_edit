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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China

# Exports powered by AI and green tech

April exports beat market expectations by a wide margin against the backdrop of a global manufacturing upturn. Strong momentum was led by AI-related and green-tech products, reinforcing exports as the main growth engine amid weak domestic demand. Rising commodity prices lifted imports value.

- April: $14.1\%$ y/y for exports, and $25.3\%$ y/y for imports (both in USD terms)   
- Bloomberg consensus (BARC): $8.4\%$ y/y $(6.5\%)$ for exports, and $20\%$ y/y $(18\%)$ for imports   
- March: $2.5\%$ y/y for exports, and $27.8\%$ y/y for imports (both in USD terms)

China's export growth returned to double-digit growth, rising to $14.1\%$ y/y in April, far exceeding expectations (Bloomberg $8.4\%$ , BARC: $6.5\%$ ). Such strong exports came against the backdrop of 1) robust uptick in global manufacturing (versus slowing services sector), with global manufacturing PMI rising to a 4-year high in April despite the prolonged energy shock, and 2) strong exports across major manufacturing economies, ranging from low-to-mid product exports from Vietnam (April: $21\%$ y/y), to high-end oriented product exports from Korea (April: $48\%$ ), to the full-supply-chain exports from China (April: $14\%$ ).

The export momentum is underpinned by high-tech products, particularly AI-related and green-tech goods. The strong global AI capex cycle underpins demand for China's AI-related exports, given the country is a key supplier of AI manufactured components. The breakdown data show that exports of semiconductors (\~8% of China's total exports YTD) rose 100% y/y, while exports of automatic data processing equipment and related parts (\~6% of China's total exports YTD) increased 47% y/y. We estimate that these two categories together contributed \~8pp to headline exports growth, explaining \~60% of exports growth. For context, China accounts for over 30% of global export value in critical AI-related products, well above Korea (\~6%), - including electronic chips, computers, semiconductor components, electrical boards and chip-making equipment.

Turning to green-tech, the ongoing energy supply shock is fuelling Chinese growth by boosting demand for its renewable energy-tech exports. YTD exports data showed strong, double-digit growth in these segments, including EVs (+68% y/y), lithium batteries (+55% y/y), wind turbines (+55% y/y) and solar cells (+34%). We think a prolonged period of geopolitical tensions could accelerate the global green transition, which would ultimately benefit China as the world's leading green-technology powerhouse given the low costs and high quality green products and technologies. Indeed, following the Middle East conflict, we see a surge in export orders for solar

# Yingke Zhou

+852 2903 2653

yingke.zhou@BARC.com

BARC Bank, Hong Kong

# Ying Zhang

+852 2903 2652

ying.zhang3@BARC.com

BARC Bank, Hong Kong

# Jian Chang

+852 2903 2654

jian.chang@BARC.com

BARC Bank, Hong Kong

panels, wind turbines, electric vehicles, and other electrified products in the past two months, underscoring how an energy shock can reinforce the shift toward renewables $^{1}$ .

Looking ahead, we expect exports to remain a critical growth driver this year supported by green-tech, and AI related products. High frequency shipping data showed still strong exports in May. We expect net exports to continue to contribute about 30% of GDP growth this year (2025: 32%), adding 1.4pp to our full-year 2026 GDP growth forecast of 4.6%. By contrast, the contribution from consumption is likely to fall below 50% amid a deteriorating labour market and reduced pro-consumption sUBSidies. The high-frequency consumption indicators (eg, auto sales, May holiday trip data) weakened visibly in the past month, suggesting consumption will remain a drag on growth in Q2. Overall, we expect the two-speed economy – strong exports versus weak domestic demand – to persist this year.

# Details of April export data

\- By destination: Export growth improved broadly across major markets in April. Shipments to the US rebounded by 11.3% y/y, partly reflecting a low base a year earlier following the Liberation Day tariffs. On a m/m basis, exports to the US surged 24.8%, well above the 2022–24 average of 3.2% (excluding the tariff-affected year of 2025). Export growth to the EU (April: 13.4%, March: 8.6%) and the UK (9.6%, 3.4%) also strengthened. Regional exports to ASEAN (15.2%, 6.9%) and to Japan, Korea and Taiwan (16.8%, 16.0%) posted double-digit gains. Meanwhile, shipments to Africa and LatAm accelerated meaningfully, contributing 2.1pp to headline export growth in April, compared with a drag of 0.1pp in March.

\- By product: Most major export categories accelerated in April. Semiconductor exports value almost doubled from a year earlier, following an already strong $85\%$ increase in the previous month. Auto exports remained resilient, rising $44\%$ y/y, broadly in line with March. Exports of mechanical and electrical products grew $20\%$ y/y, up from $11\%$ in March, while home appliance exports returned to positive growth. In contrast, exports of furniture, general equipment and machinery continued to contract, albeit at a slower pace.

FIGURE 1. China April exports returned to double-digit growth...   
![](images/3b97bc9d185f70713602f01a988a7b9d021f02207e8e52333711474eb4a602f4.jpg)

<details>
<summary>bar_line</summary>

| Date    | Trade balance (USD bn, RHS) | Exports (% y/y) | Imports (% y/y) |
|---------|-----------------------------|-----------------|-----------------|
| Apr-23  | 18                          | 12              | -6              |
| Oct-23  | 14                          | -12             | -12             |
| Apr-24  | 16                          | 6               | 6               |
| Oct-24  | 18                          | 12              | -6              |
| Apr-25  | 20                          | 6               | -12             |
| Oct-25  | 18                          | 12              | 6               |
| Apr-26  | 18                          | 12              | 150             |
</details>

Source: Wind, BARC

FIGURE 2. ... with shipments to major partners improving   
![](images/303682f9e6407db3c971fddc17801c7f4e85b945cf46c2918b038888ee1675ff.jpg)

<details>
<summary>line</summary>

| Date   | Exports value: headline | US  | EU  | UK  | ASEAN | Africa |
|--------|--------------------------|-----|-----|-----|-------|--------|
| Oct-23 | ~0                       | ~5  | ~-10| ~-5 | ~-15  | ~0     |
| Apr-24 | ~5                       | ~0  | ~-5 | ~-10| ~20   | ~-25   |
| Oct-24 | ~10                      | ~10 | ~10 | ~5  | ~10   | ~25    |
| Apr-25 | ~5                       | ~-30| ~15 | ~10 | ~20   | ~35    |
| Oct-25 | ~10                      | ~-25| ~10 | ~5  | ~30   | ~50    |
| Apr-26 | ~15                      | ~-10| ~15 | ~10 | ~30   | ~50    |
</details>

Source: Wind, BARC

FIGURE 3. Strong exports were led by AI-related and green-tech products   
![](images/e062a53efe31c6f563b7ad07a6529c67bf2f730fc29b5c856641d038e5cdf11e.jpg)

<details>
<summary>bar</summary>

| Category | 2025 export value growth (%) | 2026Jan-Apr growth (%) |
|---|---|---|
| Drones | 93.1 | 106.1 |
| Semiconductor | 27.8 | 83.7 |
| Wind turbines | 48.0 | 54.9 |
| Lithium-ion batteries | 25.0 | 54.7 |
| Autos | 20.0 | 54.1 |
| Transformers | 35.0 | 37.8 |
| Solar cells | -5.0 | 34.2 |
| Ships | 27.0 | 25.6 |
| Overall exports | 5.0 | 14.5 |
</details>

Source: Wind, BARC

FIGURE 4. High frequency shipping data showed still strong exports in May   
![](images/5890917389cca9f83a023ebf01d59217d1697d7c28aedf97b9c036cac187f66c.jpg)

<details>
<summary>line</summary>

China port cargo throughput, weekly, mn TEUs
| Week | 2024 (mn TEUs) | 2025 (mn TEUs) | 2026 (mn TEUs) |
|---|---|---|---|
| 1 | 5.9 | 6.1 | 6.5 |
| 5 | 5.3 | 5.3 | 7.4 |
| 9 | 4.4 | 5.6 | 5.6 |
| 13 | 5.6 | 6.0 | 6.8 |
| 17 | 5.9 | 6.5 | 6.8 |
| 21 | 6.2 | 6.5 | 7.0 |
| 25 | 6.3 | 6.7 | - |
| 29 | 6.4 | 6.4 | - |
| 33 | 5.6 | 6.8 | - |
| 37 | 6.4 | 6.7 | - |
| 41 | 6.5 | 6.8 | - |
| 45 | 6.4 | 6.8 | - |
| 49 | 6.2 | 6.7 | - |
| 53 | 5.6 | 6.1 | - |
</details>

Source: Wind, BARC

# April headline imports posted a strong growth due to price effects

Imports have continued to exceed expectations this year. Against the backdrop of surging energy prices, and semiconductor related prices, China's import value growth posted a solid growth of $25.3\%$ y/y in April, following a $27.8\%$ increase in March, supported by robust imports of mechanical and electrical products (April: $33.5\%$ , March: $26\%$ ), agricultural products (April: $20\%$ , March: $13.6\%$ ), and commodities (April: $13\%$ , March: $2\%$ ). In contrast, auto imports remained weak, falling $34\%$ y/y after a $40\%$ decline in March.

On a volume basis, imports of energy-related products weakened notably. Crude oil imports fell 20% y/y, widening sharply from a 2.8% decline in March. Natural gas imports dropped 13% (March: -11%), while coal imports fell 12.5%. Imports of industrial materials also stayed soft: iron ore import growth slowed to 0.7% from 11.5% in March, and steel imports declined 11% y/y, reversing a 2% increase previously.

By contrast, soybean imports reached 8.48 million metric tons in April, more than doubling from 4.02 million tons in March. This marked a 39.4% y/y increase in April, following a 15% gain previously. Looking ahead, President Trump is scheduled to visit China for meetings with President Xi from 13–15 May, when China could likely pledge incremental purchases of US agricultural products (such as soybeans and corn), energy (including LNG and crude oil), and Boeing aircraft.

FIGURE 5. Imports by key categories   
![](images/2ef919c25af0dd2dc9b54149324b19fb38e36358bf46237eb87ae70335bdc5f7.jpg)

<details>
<summary>line</summary>

| Date   | Imports value: headline | Commodities (iron ore, crude oil and copper) | Mechanical & electrical products | Agricultural products | Autos |
|--------|--------------------------|-----------------------------------------------|----------------------------------|------------------------|-------|
| Apr-23 | -10                      | -20                                           | -15                              | -10                    | -40   |
| Jan-24 | 5                        | 10                                            | 10                               | 5                      | 20    |
| Oct-24 | -5                       | -10                                           | 0                                | -5                     | -30   |
| Jul-25 | 0                        | -5                                            | 5                                | 0                      | -50   |
| Apr-26 | 30                       | 15                                            | 30                               | 20                     | -40   |
</details>

Source: Wind, BARC

FIGURE 6. Semiconductor import value accelerated   
![](images/d1bea46ad7fd953037463788a827a129003e58c7433f112fb707c750e1e8a0b2.jpg)

<details>
<summary>line</summary>

| Date   | Semiconductor imports volume | Semiconductor imports value |
|--------|-------------------------------|-----------------------------|
| Oct-18 | -15                           | 20                          |
| Apr-20 | 60                            | 50                          |
| Oct-21 | 25                            | 30                          |
| Apr-23 | -20                           | -40                         |
| Oct-24 | 15                            | 10                          |
| Apr-26 | 10                            | 55                          |
</details>

Source: Wind, BARC

FIGURE 7. Imports of key industrial materials stayed soft...   
![](images/a40a09e1cbf86b6ce684b20ef0fdfaa5870e2378e1cb185ce356b13d1b1100fc.jpg)

<details>
<summary>line</summary>

| Date   | Iron ore | Copper | Steel |
|--------|----------|--------|-------|
| Apr-23 | 10       | -15    | -40   |
| Jan-24 | 10       | 25     | -10   |
| Oct-24 | 10       | -10    | -25   |
| Jul-25 | 10       | 10     | -20   |
| Apr-26 | 10       | 0      | -10   |
</details>

Source: Wind, BARC

FIGURE 8. ... while imports of crude oil and natural gas weakened visibly   
![](images/ec4b851be3ef3a86ff040282b417572496d01a7f32e937387a6b22cba6c33680.jpg)

<details>
<summary>line</summary>

| Date    | Coal | Crude oil | Natural gas |
|---------|------|-----------|-------------|
| Apr-23  | 75   | 0         | 10          |
| Jan-24  | 50   | 10        | 20          |
| Oct-24  | 30   | 15        | 25          |
| Jul-25  | -25  | 10        | -5          |
| Apr-26  | -20  | -20       | -10         |
</details>

Source: Wind, BARC

# Analyst(s) Certification(s):

We, Yingke Zhou, Jian Chang and Ying Zhang, hereby certify (1) that the views expressed in this research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

# Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC").

All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

# Availability of Disclosures:

For current important disclosures regarding any issuers which are the subject of this research report please refer to https://publicresearch.BARC.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that BARC may have a conflict of interest that could affect the objectivity of this report. BARC Capital Inc. and/or one of its affiliates regularly trades, generally deals as principal and generally provides liquidity (as market maker or otherwise) in the debt securities that are the subject of this research report (and related derivatives thereof). BARC trading desks may have either a long and / or short position in such securities, other financial instruments and / or derivatives, which may pose a conflict with the interests of investing customers. Where permitted and subject to appropriate information barrier restrictions, BARC fixed income research analysts regularly interact with its trading desk personnel regarding current market conditions and prices. BARC fixed income research analysts receive compensation based on various factors including, but not limited to, the quality of their work, the overall performance of the firm (including the profitability of the Investment Banking Department), the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst. To the extent that any historical pricing information was obtained from BARC trading desks, the firm makes no representation that it is accurate or complete. All levels, prices and spreads are historical and do not necessarily represent current market levels, prices or spreads, some or all of which may have changed since the publication of this document. BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations and trade ideas contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

# Disclosure(s) regarding Information Sources

Bloomberg® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”) and the Bloomberg Indices are trademarks of Bloomberg. Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Bloomberg does not approve or endorse this material, or guarantee the accuracy or completeness of any information herein, or make any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, Bloomberg shall have no liability or responsibility for injury or damages arising in connection therewith.

All pricing information is indicative only. Unless otherwise indicated, prices are sourced from LSEG Data & Analytics and reflect the closing price in the relevant trading market, which may not be the last available price at the time of publication.

# Types of investment recommendations produced by BARC FICC Research:

In addition to any ratings assigned under BARC' formal rating systems, this publication may contain investment recommendations in the form of trade ideas, thematic screens, scorecards or portfolio recommendations that have been produced by analysts in FICC Research. Any such investment recommendations produced by non-Credit Research teams shall remain open until they are sUBSequently amended, rebalanced or closed in a future research report. Any such investment recommendations produced by the Credit Research teams are valid at current market conditions and may not be otherwise relied upon.

# Disclosure of other investment recommendations produced by BARC FICC Research:

BARC FICC Research may have published other investment recommendations in respect of the same securities/instruments recommended in this research report during the preceding 12 months. To view all investment recommendations published by BARC FICC Research in the preceding 12 months please refer to https://live.barcap.com/go/research/Recommendations.

BARC does not assign ratings to asset backed securities. BARC Capital Inc. and/or one of its af

[中间内容因长度限制已省略]

 scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to sUBScribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
