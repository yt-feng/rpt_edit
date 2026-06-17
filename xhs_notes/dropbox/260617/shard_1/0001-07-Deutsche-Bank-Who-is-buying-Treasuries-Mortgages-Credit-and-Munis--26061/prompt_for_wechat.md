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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`DB`。标题格式建议：`# DB：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份DB研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
![](images/4e7f9a90cf377cbc33b78059a671e049021832a1c4da0b77ae98a0ebadd5e249.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Bills | < 3yr | 3-6yr | 6-11yr | > 11yr | FRN | TIPS |
|------|-------|-------|-------|--------|--------|-----|------|
| 2008 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~0   |
| 2010 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~0   |
| 2012 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~0   |
| 2014 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~0   |
| 2016 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~0   |
| 2018 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~0   |
| 2020 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~0   |
| 2022 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~0   |
| 2024 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~0   |
| 2026 | ~0    | ~0    | ~0    | ~0     | ~0     | ~0  | ~550 |
The chart includes a legend for each category (Bills, < 3yr, 3-6yr, 6-11yr, > 11yr, FRN, TIPS) but lacks explicit numerical labels on the data series.
</details>

Source: New York Fed, Macrobond, DB

## Bank holdings of Treasury and agency debt expanding again after contracting during the Fed tightening cycle

Holdings of Treasury and agency securities by commercial banks  
![](images/2e9a3017df97495362438b335f8abea7bd4c199b0619be62ef98cd834793f8c6.jpg)

<details>
<summary>line chart</summary>

| Year | Value ($, trillion) |
| ---- | ------------------- |
| 2010 | 1.3                 |
| 2012 | 1.7                 |
| 2014 | 1.8                 |
| 2016 | 2.3                 |
| 2018 | 2.5                 |
| 2020 | 3.0                 |
| 2022 | 4.7                 |
| 2024 | 4.0                 |
| 2026 | 4.8                 |
</details>

Source: Fed, Macrobond, DB

## What are foreign central banks doing?

## Global FX reserves: \$13trn as of 2025 Q3

Global FX Reserves  
![](images/65927c9aa4a51be6fedf1262ad06660e2f2168c5c04780f5c3cfc542e864f636.jpg)

<details>
<summary>line chart</summary>

| Year | Value ($, trillion) |
| ---- | ------------------- |
| 2008 | 5.7                 |
| 2009 | 7.5                 |
| 2010 | 8.2                 |
| 2011 | 9.5                 |
| 2012 | 10.2                |
| 2013 | 11.0                |
| 2014 | 11.8                |
| 2015 | 11.5                |
| 2016 | 11.0                |
| 2017 | 10.8                |
| 2018 | 11.5                |
| 2019 | 11.7                |
| 2020 | 11.8                |
| 2021 | 12.5                |
| 2022 | 13.0                |
| 2023 | 11.5                |
| 2024 | 12.5                |
| 2025 | 13.0                |
| 2026 | 13.5                |
</details>

Source: IMF, Macrobond, DB

## Global FX reserves: USD share trending lower but remains abo

[中间内容因长度限制已省略]

the Russian Federation.

Kingdom of Saudi Arabia: Deutsche Securities Saudi Arabia (DSSA) is a closed joint stock company authorized by the Capital Market Authority of the Kingdom of Saudi Arabia with a license number (No. 37-07073) to conduct the following business activities: Dealing, Arranging, Advising, and Custody activities. . DSSA registered office is at Faisaliah Tower, 17th floor, King Fahad Road - Al Olaya District Riyadh, Kingdom of Saudi Arabia P.O. Box 301806.

United Arab Emirates: DB AG in the Dubai International Financial Centre (registered no. 00045) is regulated by the Dubai Financial Services Authority. DB AG - DIFC Branch may only undertake the financial services activities that fall within the scope of its existing DFSA license. Principal place of business in the DIFC: Dubai International Financial Centre, The Gate Village, Building 5, PO Box 504902, Dubai, U.A.E. This information has been distributed by DB AG. Related financial products or services are available only to Professional Clients, as defined by the Dubai Financial Services Authority.

Australia and New Zealand: This research is intended only for "wholesale clients" within the meaning of the Australian Corporations Act and New Zealand Financial Advisors Act, respectively. Please refer to Australian specific research disclosures and related information at https://www.dbresearch.com/PROD/RPS\_EN-PROD/PROD000000000521304.xhtml . Where research refers to any particular financial product recipients of the research should consider any product disclosure statement, prospectus or other applicable disclosure document before making any decision about whether to acquire the product. In preparing this report, the primary analyst or an individual who assisted in the preparation of this report has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2025 DB AG
"""
