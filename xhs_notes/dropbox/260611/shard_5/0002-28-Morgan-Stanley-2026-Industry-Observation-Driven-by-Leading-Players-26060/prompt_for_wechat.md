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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Hong Kong/China Insurance | Asia Pacific

# 2026 Industry Observation: Driven by Leading Players

Greater disclosure in solvency reports improves industry visibility. We expect diversified product strategies, optimized investment allocation, and continued industry de-risking, with limited system-wide risks. Leading insurers should sustain their competitive edge.

China insurers must deliver solvency reports with more detailed operating metrics from 1Q26, improving our ability to assess and track listed insurers' performance and the broader industry.

Large insurers leading par product transition towards more diversified product strategy. Over the past two years, listed insurers have largely completed the transition, with $>80\%$ of new premiums in par products in 1Q26. Many small and medium-sized (SME) insurers have shown similar trends across channels. However, many SMEs are now revisiting product strategies, with some reinvigorating traditional product sales since 2Q26. We expect the pricing interest rate for current par products to continue declining (from 1.75% to $\sim1.25\%$ ) over the next few quarters, alongside the illustration rate. Large insurers may continue to focus on par products, while SMEs adopt a more balanced mix between par and non-par. By channel, large insurers could maintain their banca edge despite tighter regulation and further optimize payment-period structures, while SMEs need to rethink channel partnerships and cash flow management. The agency channel will remain core for large insurers, with quality improving over time.

Ongoing optimization of investment strategies across accounts amid low-rate, volatile market. Interest rates have stabilized over the past year, and a steeper yield curve could offer some support to insurers. However, bond-trading demand remains strong. Listed insurers have increased equity allocations, taking a more proactive approach in par reserve accounts while maintaining a more prudent strategy in non-par accounts. Large insurers should continue to benefit from an edge in alternative asset investments.

## Solvency remains a key constraint, and insurers are improving operations.

Despite some deregulation, solvency pressure could continue to weigh on certain insurers' asset allocation and liability growth, and we see limited scope for solvency rule revisions in 2026. At the industry level, insurers are taking effective measures to mitigate risks and enhance long-term competitiveness, while duration mismatch is unlikely to rank as a near-term priority under the current backdrop. Risks remain concentrated in select pockets, and large insurers should maintain their advantages. We continue to favor high-quality names including Ping An, China Life, and AIA despite short-term headwinds, which should have limited structural impact.

MS ASIA LIMITED+

## Rick Zhao

Equity Analyst

Rick.Zhao@morganstanley.com +852 2239-7033

## Richard Xu, CFA

Equity Analyst

Richard.Xu@morganstanley.com +852 2848-6729

## Chenqian Liu

Research Associate

Chenqian.Liu@morganstanley.com +852 3963-0359

## Asia Summer School 2026

![](images/9289ed196970660095fe9986dd1c29dad1ccec9e8480d784e6442b7f282ce996.jpg)

## HONG KONG/CHINA INSURANCE

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Large insurers leading industry-wide liability-side transition

## Insurers have largely completed shift to par products over past two years at industry level

Par products now account for $>80\%$ of listed insurers' new business in 2026. Declining long-term interest rates in recent years, together with regulatory guidance, have driven China insurers' product strategy shift from traditional to participating products. While long-term rates remain relatively low this year despite some recovery in 2H25, demand for savings-related insurance remains resilient, as both duration and potential returns exceed bank deposits. As a result, listed insurers have accelerated par product roll-outs since 2H24 and largely completed the transition from traditional to participating products across both agency and banca channels in 2026. In 1Q26, most listed insurers recorded a $\sim90\%$ par product mix in regular FYP (first-year premiums), up from $<50\%$ in 1H25.

Exhibit 1: Insurers' pricing interest rate caps have been declining over the past three years in China  
![](images/fa724ee0a6d217aae5443505d58fed41b3d4d01e05a9f0b045a2385ca75f79e4.jpg)

<details>
<summary>line chart</summary>

| Date     | 10-year treasury bond yield | Pricing interest rate cap | 3-year deposit rate | Research value for pricing interest rate |
|----------|------------------------------|----------------------------|---------------------|------------------------------------------|
| 1/2023   | ~2.9                         | 3.5                        | ~2.6                | -                                        |
| 4/2023   | ~2.8                         | 3.5                        | ~2.6                | -                                        |
| 7/2023   | ~2.7                         | 3.0                        | ~2.5                | -                                        |
| 10/2023  | ~2.6                         | 3.0                        | ~2.4                | -                                        |
| 1/2024   | ~2.5                         | 3.0                        | ~2.3                | -                                        |
| 4/2024   | ~2.4                         | 3.0                        | ~2.2                | -                                        |
| 7/2024   | ~2.3                         | 3.0                        | ~2.1                | -                                        |
| 10/2024  | ~2.2                         | 3.0                        | ~2.0                | -                                        |
| 1/2025   | ~2.1                         | 3.0                        | ~1.9                | -                                        |
| 4/2025   | ~1.9                         | 3.0                        | ~1.8                | -                                        |
| 7/2025   | ~1.8                         | 3.0                        | ~1.7                | -                                        |
| 10/2025  | ~1.7                         | 3.0                        | ~1.6                | -                                        |
| 1/2026   | ~1.6                         | 3.0                        | ~1.5                | -                                        |
| 4/2026   | ~1.5                         | 3.0                        | ~1.4                | -                                        |
</details>

Source: IAC, PBOC, CFETS, Company data, MS

Exhibit 2: Par account cash flows as a % of operating cash flows increased across most peers in 1Q26 vs. 1Q25  
![](images/9bd629f06acaa1e16c3cd38fe1acd40b2581c145999bfd05a9e2cac55769c533.jpg)

<details>
<summary>bar chart</summary>

| Company | 1Q26 (%) | 1Q25 (%) |
| :--- | :--- | :--- |
| China Life | 30 | -10 |
| Ping An Life | 38 | -45 |
| China Post Life | 20 | -70 |
| Taiang Life | 68 | 60 |
| CPIC Life | 20 | 5 |
| New China Life | 50 | -10 |
| Taiping Life | 15 | -15 |
| Sunshine Life | 45 | -25 |
| AIA Life | 75 | 25 |
| Generali China | 78 | 55 |
| Cigna CMB | 75 | 55 |
| Pramerica Fosun | 15 | -25 |
| Manulife Sinochem | 85 | -15 |
| MetLife China | 80 | 80 |
| ICBC AXA | 10 | -40 |
| Great Wall Life | 25 | -90 |
| ABC Life | -90 | -80 |
| BOC Samsung | -10 | 45 |
| CITIC Prudential | 90 | -35 |
| Happy Life | 20 | 5 |
| Aviva-Cotco | 40 | 30 |
| BOB-Caribf | 55 | 30 |
| HSBCI Life | 80 | -30 |
| Sun Life Everbright | 60 | -35 |
| Heng An Standard | 90 | 70 |
| SooChow Life | -10 | 5 |
| BoComm Life | -20 | -40 |
| Cathay Lujiazui | 65 | 25 |
| Huatai Life | 120 | 45 |
| Minsheng Life | 15 | 10 |
| Aegon THF | 35 | -15 |
| CMB Life | -45 | -35 |
| Allianz China | 70 | 50 |
| East Wealth Life | -5 | 40 |
| Guobao Life | -30 | 30 |
| China United Life | -90 | -10 |
| Hengqin Life | 25 | 120 |
| Hetai Life | 15 | -20 |
| Livit Life | 10 | -15 |
| Changsheng Life | 5 | 120 |
| Three Gorges Life | 10 | 120 |
| Junlong Life | -90 | 120 |
</details>

Source: Company data, MS

From an industry-wide perspective, most unlisted insurers have delivered similar trends. 1) Most insurers posted positive YoY operating cash flow growth in 1Q26 (Exhibit 2), with a \~11% median. We see a material increase in participating products' contribution to operating cash flow in 1Q26 vs. 1Q25 across most names, making par products a key driver of liability-side growth and near-term cash flow improvement. 2) In the banca channel, on which most unlisted insurers rely, par products contributed \~90% of foreign insurers' new premiums and \~70% of unlisted domestic insurers' new premiums (Exhibit 11).

However, we expect a more diversified product strategy to emerge between large insurers and the rest. We view this round of product transition as more regulator-led, especially as the pricing interest rate gap between traditional and par products narrowed from 50bps to 25bps since 3Q25. SME insurers may shift back to a more balanced par/non-par mix, considering:

\- Higher actual cost: although par products carry lower guaranteed liability costs vs. traditional products, actual liability costs (including non-guaranteed components)

are higher, and cutting the fulfillment ratio could undermine competitiveness.

- Customer profit-sharing mechanisms: par products feature profit sharing, which can reduce retained shareholder profits, especially when insurers generate excess investment returns, potentially slowing the de-risking process.  
- Potential higher capital requirements: par products can be more capital-intensive than traditional products, especially with more proactive asset allocation.  
- Cash flow management challenges: par products are more complex to manage vs. traditional products, particularly for small insurers handling participating fund reserves and surrender risk.

As a result, we expect listed insurers to continue focusing on par products over the longer term, supported by agent channel inertia that ensures product continuity. However, the pricing interest rate could decline to \~1.25% over the next few quarters, likely through regulatory window guidance and product filing management, with some insurers already rolling out such products in 2026. In March 2026, the illustration rate was guided down from 3.9% to 3.5%, and actual dividend payout was \~3.2% for 2025. We expect the illustration rate to decline further to \~3.2% over the next few quarters. For most SME insurers, we expect a more balanced approach between traditional and par products, with some potentially fully shifting back to traditional products in response to shareholder demands.

## Clear opportunities in the banca channel, with large insurers maintaining their edge

Continued strong banca channel growth at the industry level... Bancassurance rebounded with $>15\%$ new premium growth in 2025 after a brief adjustment due to tighter expense regulation (“Bao Xing He Yi”) in late 2023 and early 2024. Momentum carried into 1Q26, with $\sim17\%$ FYP growth and $\sim19\%$ RP FYP growth YoY. Higher channel margins and a maturing term deposit base (Exhibit 5 – a large 2023 term deposit cohort matures around 2026) have supported growth.

Exhibit 3: Industry-wide banca channel premiums  
![](images/ade9d689d43cb40c15bb5071355e23dfb9c6991689bd29fa86d4587503c0172f.jpg)

<details>
<summary>bar chart</summary>

| Year | FYP (Rmb bn) | RP FYP (Rmb bn) | Growth (%) |
| :--- | :--- | :--- | :--- |
| 2023 | 930 | 415 | |
| 2024 | 730 | 360 | +16 |
| 2025 | 845 | 400 | +11 |
| Mar-25 | 310 | 150 | +17 |
| Mar-26 | 370 | 180 | +19 |
</details>

Source: NAFR, MS

Exhibit 4: More term deposits in China in 2023, with potentially higher demand to reinvest at maturity  
![](images/82a37968c0477d45b03ecd3e69558af2b22af1fc64e776943898fc3ed717c025.jpg)

<details>
<summary>bar chart</summary>

| Year | New demand (Rmb trn) | New term and other (Rmb trn) |
| :--- | :--- | :--- |
| 2022 | 4.1 | 13.7 |
| 2023 | 0.6 | 16.0 |
| 2024 | 2.3 | 11.9 |
| 2025 | 2.7 | 11.9 |
</details>

Source: NAFR, PBOC, NBS, AMAC, MS

...and SME insurers rely heavily on the banca channel. Channel structures have diverged between large insurers and mid-to-small players. Most insurers with assets between Rmb10bn and Rmb1tn derive 50–100% of gross premiums from banca (Exhibit 6), while insurers with assets above Rmb1tn, including most listed players, maintain a more balanced mix – with the agency channel contributing \~60–80% of total premiums – supporting stronger margins and more sustainable value creation through better control of proprietary channels and tied agents.

Exhibit 5: 1Q26 par product mix in banca channel  
![](images/6b399128465ce73d26da84729f76136c5291cc5665e2df8c3684dc62321786bb.jpg)

<details>
<summary>bar chart</summary>

| Category | Large domestic insurers (%) | Other domestic insurers (%) | Foreign insurers (%) |
| :--- | :---: | :---: | :---: |
| FYP | 85 | 58 | 89 |
| RP FYP | 89 | 64 | 83 |
</details>

Source: Company data, MS

Exhibit 6: 1Q26 banca channel mix as a % of total premium vs. total asset  
![](images/2fb158211fc71561e4364569b49c756e5ff120d197311c4b6b4bd19ab7861a14.jpg)

<details>
<summary>scatter plot</summary>

| Asset, Rmb bn | Banca channel mix % |
| ------------- | ------------------- |
| 1             | 85                  |
| 2             | 75                  |
| 3             | 50                  |
| 4             | 45                  |
| 5             | 40                  |
| 6             | 45                  |
| 7             | 50                  |
| 8             | 55                  |
| 9             | 60                  |
| 10            | 65                  |
| 11            | 70                  |
| 12            | 75                  |
| 13            | 80                  |
| 14            | 85                  |
| 15            | 90                  |
| 16            | 95                  |
| 17            | 90                  |
| 18            | 85                  |
| 19            | 80                  |
| 20            | 75                  |
| 21            | 70                  |
| 22            | 65                  |
| 23            | 60                  |
| 24            | 55                  |
| 25            | 50                  |
| 26            | 45                  |
| 27            | 40                  |
| 28            | 35                  |
| 29            | 30                  |
| 30            | 25                  |
| 31            | 20                  |
| 32            | 15                  |
| 33            | 10                  |
| 34            | 5                   |
| 35            | 0                   |
| 36            | 5                   |
| 37            | 10                  |
| 38            | 15                  |
| 39            | 20                  |
| 40            | 25                  |
| 41            | 30                  |
| 42            | 35                  |
| 43            | 40                  |
| 44            | 45                  |
| 45            | 50                  |
| 46            | 55                  |
| 47            | 60                  |
| 48            | 65                  |
| 49            | 70                  |
| 50            | 75                  |
| 51            | 80                  |
| 52            | 85                  |
| 53            | 90                  |
| 54            | 95                  |
| 55            | 90                  |
| 56            | 85                  |
| 57            | 80                  |
| 58            | 75                  |
| 59            | 70                  |
| 60            | 65                  |
| 61            | 60                  |
| 62            | 55                  |
| 63            | 50                  |
| 64            | 45                  |
| 65            | 40                  |
| 66            | 35                  |
| 67            | 30                  |
| 68            | 25                  |
| 69            | 20                  |
| 70            | 15                  |
| 71            | 10                  |
| 72            | 5                   |
| 73            | 0                   |
| 74            | 5                   |
| 75            | 10                  |
| 76            | 15                  |
| 77            | 20                  |
| 78            | 25                  |
| 79            | 30                  |
| 80            | 35                  |
| 81            | 40                  |
| 82            | 45                  |
| 83            | 50                  |
| 84            | 55                  |
| 85            | 60                  |
| 86            | 65                  |
| 87            | 70                  |
| 88            | 75                  |
| 89            | 80                  |
| 90            | 85                  |
| 91            | 90                  |
| 92            | 95                  |
| 93            | 90                  |
| 94            | 85                  |
| 95            | 80                  |
| 96            | 75                  |
| 97            | 70                  |
| 98            | 65                  |
| 99            | 60                  |
| 100           | 55                  |
| 101           | 50                  |
| 102           | 45                  |
| 103           | 40                  |
| 104           | 35                  |
| 105           | 30                  |
| 106           | 25                  |
| 107           | 20                  |
| 108           | 15                  |
| 109           | 10         

[中间内容因长度限制已省略]

uthority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of AIA Group Ltd, China Life Insurance Co Ltd, China Pacific Insurance Group Co Ltd, New China Life Insurance Company Ltd, PICC Group, PICC P&C Company Ltd, Ping An Insurance Group Co of China Ltd, ZhongAn Online P & C Insurance Co Ltd listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Hong Kong/China Insurance

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/09/2026)</td></tr><tr><td colspan="3">Richard Xu, CFA</td></tr><tr><td>AIA Group Ltd (1299.HK)</td><td>O (12/12/2023)</td><td>HK$71.00</td></tr><tr><td>FWD Group Holdings Ltd (1828.HK)</td><td>O (08/13/2025)</td><td>HK$29.90</td></tr><tr><td>Ping An Insurance Group Co of China Ltd (2318.HK)</td><td>O (05/30/2023)</td><td>HK$56.90</td></tr><tr><td>Ping An Insurance Group Co of China Ltd (601318.SS)</td><td>O (05/30/2023)</td><td>Rmb53.93</td></tr><tr><td colspan="3">Rick Zhao</td></tr><tr><td>China Life Insurance Co Ltd (601628.SS)</td><td>E (05/30/2023)</td><td>Rmb33.14</td></tr><tr><td>China Life Insurance Co Ltd (2628.HK)</td><td>O (05/30/2023)</td><td>HK$27.38</td></tr><tr><td>China Pacific Insurance Group Co Ltd (601601.SS)</td><td>O (06/07/2024)</td><td>Rmb31.55</td></tr><tr><td>China Pacific Insurance Group Co Ltd (2601.HK)</td><td>O (05/30/2023)</td><td>HK$31.68</td></tr><tr><td>China Taiping Insurance Holdings Co Ltd (0966.HK)</td><td>E (05/30/2023)</td><td>HK$19.77</td></tr><tr><td>New China Life Insurance Company Ltd (601336.SS)</td><td>U (05/30/2023)</td><td>Rmb55.87</td></tr><tr><td>New China Life Insurance Company Ltd (1336.HK)</td><td>U (07/31/2025)</td><td>HK$47.28</td></tr><tr><td>PICC Group (1339.HK)</td><td>O (09/23/2024)</td><td>HK$5.06</td></tr><tr><td>PICC Group (601319.SS)</td><td>E (07/31/2025)</td><td>Rmb6.61</td></tr><tr><td>PICC P&amp;C Company Ltd (2328.HK)</td><td>O (05/30/2023)</td><td>HK$14.83</td></tr><tr><td>ZhongAn Online P &amp; C Insurance Co Ltd (6060.HK)</td><td>O (05/30/2023)</td><td>HK$10.55</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.
"""
