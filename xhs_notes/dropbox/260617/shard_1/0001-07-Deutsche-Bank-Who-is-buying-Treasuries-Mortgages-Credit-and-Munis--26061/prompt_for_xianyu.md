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
## Who is buying Treasuries, Mortgages, Credit, and Munis?

Matthew Luzzetti, Justin Weidner, Steven Zeng, Brett Ryan, Amy Yang, Raj Bhattacharyya
1 Columbus Circle

New York, New York 10019

Tel: 212 250 6161

June 2026

<table><tr><td>Table of contents</td><td>Page Number</td></tr><tr><td>Featured charts</td><td>02</td></tr><tr><td>What are foreign central banks doing?</td><td>17</td></tr><tr><td>Auction demand</td><td>27</td></tr><tr><td>Who is buying Treasuries?</td><td>35</td></tr><tr><td>Who is buying GSE MBS and agency debt?</td><td>50</td></tr><tr><td>Who is buying Corporate and Foreign Bonds?</td><td>54</td></tr><tr><td>Who is buying municipal securities and loans?</td><td>57</td></tr><tr><td>Asset allocations by investor account</td><td>61</td></tr><tr><td>Outlook</td><td>68</td></tr></table>

## Featured charts

Change in debt securities outstanding  
![](images/2a50fe7effea57ce6cc3bbb00189b24193e5ad9c745f3c2e638d0692aaaa4031.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Tsy | Munis | Open market | Mortgages | Bank loans | Agency | Corp & frn | Cons. credit | Oth. loans | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1996 |  |  |  |  |  |  |  |  |  | $1.3 trillion |
| 1998 |  |  |  |  |  |  |  |  |  | $1.4 trillion |
| 2000 |  |  |  |  |  |  |  |  |  | $1.5 trillion |
| 2002 |  |  |  |  |  |  |  |  |  | $1.6 trillion |
| 2004 |  |  |  |  |  |  |  |  |  | $1.7 trillion |
| 2006 |  |  |  |  |  |  |  |  |  | $1.8 trillion |
| 2008 |  |  |  |  |  |  |  |  |  | $1.9 trillion |
| 2010 |  |  |  |  |  |  |  |  |  | $1.0 trillion |
| 2012 |  |  |  |  |  |  |  |  |  | $1.1 trillion |
| 2014 |  |  |  |  |  |  |  |  |  | $1.2 trillion |
| 2016 |  |  |  |  |  |  |  |  |  | $1.3 trillion |
| 2018 |  |  |  |  |  |  |  |  |  | $1.4 trillion |
| 2020 |  |  |  |  |  |  |  |  |  | $1.5 trillion |
| 2022 |  |  |  |  |  |  |  |  |  | $1.6 trillion |
| 2024 |  |  |  |  |  |  |  |  |  | $1.7 trillion |
| 2026 |  |  |  |  |  |  |  |  |  | $1.8 trillion |
</details>

Source: Fed, Macrobond, DB

## Total US fixed income securities outstanding: \$61trn as of Q1 2026

Outstanding debt securities  
![](images/eeb0f16ae8a73c06bd8f04ccd4fa5ba0ba68f64137a6613dc9130e0fc8d781c3.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Treasury bills | Treasury coupons | Agency debt & MBS | Agency Mortgage pools | Munis | Nonfin. CP | Fin. corp. bonds | Fin. CP |
|------|-----------------|-------------------|--------------------|------------------------|-------|------------|------------------|---------|
| 2025 | ~6.5 trillion   | ~30 trillion      | ~15 trillion       | ~10 trillion            | ~8 trillion | ~5 trillion | ~40 trillion    | ~30 trillion |
</details>

Source: Fed, Macrobond, DB

## Treasury and agency securities make up about 70% of US fixed income

Outstanding debt securities  
![](images/10e791793526504d8ddc2075be73a3743153b189554448c583d05217ddd1bc7e.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Treasury bills | Treasury coupons | Agency debt & MBS | Agency Mortgage pools | Munis | Fin. CP | Nonfin. corp. bonds | Nonfin. CP | Fin. corp. bonds |
|------|----------------|------------------|-------------------|------------------------|-------|---------|---------------------|------------|------------------|
| 1960 | ~15%           | ~30%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 1965 | ~10%           | ~25%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 1970 | ~10%           | ~20%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 1975 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 1980 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 1985 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 1990 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 1995 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 2000 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 2005 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 2010 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 2015 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 2020 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
| 2025 | ~10%           | ~15%             | ~10%              | ~15%                   | ~20%  | ~5%     | ~20%                | ~5%        | ~10%             |
</details>

Source: Fed, Macrobond, DB

## Treasuries' share of US fixed income has expanded significantly since the Global Financial Crisis

Treasury securities as a share of debt outstanding  
![](images/d674a528b1eec70ca76359a9d56f6e26e303d5f843f08f83bcd65e8b4b48424f.jpg)

<details>
<summary>line chart</summary>

| Year | Value |
|------|-------|
| 2025 | 46%   |
</details>

Source: Fed, Macrobond, DB

## Treasury debt as a percentage of GDP is currently 96%, up from 75% before Covid

Treasury securities outstanding as a share of GDP  
![](images/3e973160cb8cd5e05933d50c45a6d8989aa3f7b3ffedbf36b7f656f792021899.jpg)

<details>
<summary>line chart</summary>

| Year | Value |
| ---- | ----- |
| 2020 | 96%   |
</details>

Source: Fed, BEA, Macrobond, DB

## Non-financial corporate debt as a percentage of GDP declined from a peak of 55% during Covid to 41% currently

Non-financial corporate debt securities and loans as a share of GDP  
![](images/45b2f2ff2faa72bc8f09160beba51ee4390cf3ba02f5f21edd700da54c8e2793.jpg)

<details>
<summary>line chart</summary>

| Year | Value |
|------|-------|
| 2025 | 41%   |
</details>

Source: Fed, BEA, Macrobond, DB

Transactions in US Treasury securities  
![](images/c49afe66bc98228d852374328d7280b8cca9073a87cfb318ca3b16b17b914f89.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | Net purchases by domestic sector ($ billion) | Rest of world ($ billion) | Fed ($ billion) |
|------|-----------------------------------------------|--------------------------|----------------|
| 2008 | ~200                                          | ~100                     | ~-50           |
| 2010 | ~300                                          | ~200                     | ~-100          |
| 2012 | ~200                                          | ~150                     | ~-50           |
| 2014 | ~150                                          | ~100                     | ~-50           |
| 2016 | ~200                                          | ~150                     | ~-50           |
| 2018 | ~300                                          | ~200                     | ~-50           |
| 2020 | ~1000                                         | ~1200                    | ~1200          |
| 2022 | ~400                                          | ~300                     | ~-50           |
| 2024 | ~700                                          | ~400                     | ~-50           |
| 2026 | ~500                                          | ~300                     | ~-50           |
</details>

Source: Fed, Macrobond, DB  
Note: Domestic sector includes households, banks, pension funds, insurance, govt. retirement funds, mutual funds, GSEs and others.

## Foreign ownership of US Treasuries fell slightly to 30% in Q1 2026, not far from the multi-decade low of 29% seen in 2023 Q3

Holdings of Treasuries as % of treasury debt outstanding  
![](images/5f54b109863d3eb44faa1892f9b2d7753032316972b7df3d0c4b90caf6d1d300.jpg)

<details>
<summary>line chart</summary>

| Year | Rest of world | Fed  | State & Local |
|------|---------------|------|---------------|
| 2025 | 30%           | 13%  | 5.1%          |
</details>

Source: Fed, Macrobond, DB

## Private holdings of US Treasuries concentrated in maturity of 5 years or less

Marketable debt held outside the Federal Reserve: Maturity breakdown  
![](images/3fe97c08314f146a7cc857fdea3f82d1221f2eaa17a377f183617fd084f38cd9.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Less than 1 yr | 1-5 yrs | 5-10 yrs | >10 yrs | Total outstanding |
|------|-----------------|---------|----------|---------|-------------------|
| 1975 | ~6              | ~4      | ~3       | ~2      | ~12               |
| 1980 | ~7              | ~5      | ~4       | ~3      | ~14               |
| 1985 | ~8              | ~6      | ~5       | ~4      | ~16               |
| 1990 | ~9              | ~7      | ~6       | ~5      | ~18               |
| 1995 | ~10             | ~8      | ~7       | ~6      | ~20               |
| 2000 | ~8              | ~6      | ~5       | ~4      | ~16               |
| 2005 | ~9              | ~7      | ~6       | ~5      | ~18               |
| 2010 | ~12             | ~10     | ~8       | ~7      | ~22               |
| 2015 | ~13             | ~11     | ~9       | ~8      | ~24               |
| 2020 | ~15             | ~13     | ~11      | ~9      | ~28               |
| 2025 | ~18             | ~16     | ~13      | ~11     | ~32               |
</details>

Source: U.S. Treasury, BEA, Macrobond, DB

## Federal Reserve still owns close to 30% of Treasuries with 10-year or longer maturity

Fed holdings of Treasury securities outstanding (% by maturity)  
![](images/531017c48d9a48b66fde1a090716c597e842bddfb798db1c0d3cccb57af2136e.jpg)

<details>
<summary>line chart</summary>

| Year | < 1yr | 1-5yr | 5-10yr | > 10yr |
|------|-------|-------|--------|--------|
| 2004 | 24.5  | 17.0  | 13.5   | 15.0   |
| 2006 | 25.0  | 14.5  | 10.5   | 14.5   |
| 2008 | 26.5  | 9.0   | 11.0   | 15.5   |
| 2010 | 3.5   | 13.0  | 17.0   | 20.0   |
| 2012 | 6.0   | 19.0  | 28.0   | 20.0   |
| 2014 | 0.0   | 15.0  | 35.0   | 43.0   |
| 2016 | 6.0   | 21.0  | 20.0   | 38.0   |
| 2018 | 11.0  | 18.0  | 12.0   | 32.0   |
| 2020 | 7.5   | 13.0  | 9.5    | 27.5   |
| 2022 | 18.5  | 25.5  | 26.0   | 38.5   |
| 2024 | 9.5   | 18.0  | 19.0   | 33.0   |
| 2026 | 8.5   | 13.5  | 12.0   | 28.5   |
</details>

Source: Fed, U.S. Treasury, Macrobond, DB

## Foreigners, insurance, and mutual funds make up majority of the investor in credit markets (IG, HY, and loans)

Holdings of corporate and foreign bonds as % outstanding  
![](images/2465ec399842601443fdf6a2040c1972762a00bbe5c46a0ac8ad6f6c9b5196ba.jpg)

<details>
<summary>line chart</summary>

| Year | Rest of the world | Life insurance companies | Hedge and households | Private pension funds | Mutual funds | Banks | Funding corporations |
|------|-------------------|--------------------------|----------------------|------------------------|--------------|-------|----------------------|
| 1955 | ~8                | ~62                      | ~8                   | ~12                    | ~1           | ~7    | ~1                   |
| 1960 | ~6                | ~55                      | ~10                  | ~16                    | ~1           | ~5    | ~1                   |
| 1965 | ~4                | ~50                      | ~8                   | ~18                    | ~1           | ~4    | ~1                   |
| 1970 | ~3                | ~40                      | ~12                  | ~14                    | ~1           | ~6    | ~1                   |
| 1975 | ~4                | ~35                      | ~18                  | ~12                    | ~1           | ~8    | ~1                   |
| 1980 | ~5                | ~35                      | ~15                  | ~14                    | ~1           | ~7    | ~1                   |
| 1985 | ~8                | ~33                      | ~10                  | ~16                    | ~2           | ~8    | ~1                   |
| 1990 | ~10               | ~32                      | ~12                  | ~10                    | ~4           | ~7    | ~1                   |
| 1995 | ~12               | ~30                      | ~18                  | ~8                     | ~6           | ~6    | ~1                   |
| 2000 | ~15               | ~28                      | ~10                  | ~6                     | ~8           | ~5    | ~1                   |
| 2005 | ~20               | ~25                      | ~8                   | ~4                     | ~7           | ~4    | ~1                   |
| 2010 | ~25               | ~20                      | ~6                   | ~3                     | ~10          | ~3    | ~1                   |
| 2015 | ~28               | ~22                      | ~4                   | ~4                     | ~14          | ~3    | ~1                   |
| 2020 | ~30               | ~24                      | ~2                   | ~5                     | ~16          | ~3    | ~1                   |
| 2025 | ~28               | ~23                      | ~1                   | ~4                     | ~14          | ~3    | ~1                   |
</details>

Source: Fed, Macrobond, DB

## Primary dealer net holdings of Treasuries have risen sharply since 2022

Primary dealer positions by asset class  
![](images/adb2c1fdda646ad0fc49b76395176636856856eee6168c54b716428b8aae3e77.jpg)

<details>
<summary>line chart</summary>

| Year | GSE (billion $) | Corporate (billion $) | US government securities (billion $) |
|------|-----------------|------------------------|--------------------------------------|
| 2002 | ~70             | ~0                     | ~0                                   |
| 2004 | ~90             | ~-50                   | ~-100                                |
| 2006 | ~100            | ~-100                  | ~-150                                |
| 2008 | ~170            | ~-150                  | ~-180                                |
| 2010 | ~80             | ~-50                   | ~-50                                 |
| 2012 | ~60             | ~50                    | ~100                                 |
| 2014 | ~40             | ~50                    | ~100                                 |
| 2016 | ~30             | ~40                    | ~150                                 |
| 2018 | ~20             | ~30                    | ~250                                 |
| 2020 | ~15             | ~30                    | ~300                                 |
| 2022 | ~15             | ~20                    | ~150                                 |
| 2024 | ~15             | ~20                    | ~300                                 |
| 2026 | ~15             | ~20                    | ~550                                 |
</details>

Source: New York Fed, Macrobond, DB

## Maturity composition of primary dealers' inventory of Treasuries

Primary Dealer Net Outright Position in US Govt. securities by category  
![](images/4e7f9a90cf377cbc33b78059a671e049021832a

[中间内容因长度限制已省略]

siness in the DIFC: Dubai International Financial Centre, The Gate Village, Building 5, PO Box 504902, Dubai, U.A.E. This information has been distributed by DB AG. Related financial products or services are available only to Professional Clients, as defined by the Dubai Financial Services Authority.

Australia and New Zealand: This research is intended only for "wholesale clients" within the meaning of the Australian Corporations Act and New Zealand Financial Advisors Act, respectively. Please refer to Australian specific research disclosures and related information at https://www.dbresearch.com/PROD/RPS\_EN-PROD/PROD000000000521304.xhtml . Where research refers to any particular financial product recipients of the research should consider any product disclosure statement, prospectus or other applicable disclosure document before making any decision about whether to acquire the product. In preparing this report, the primary analyst or an individual who assisted in the preparation of this report has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2025 DB AG
"""
