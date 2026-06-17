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
# China: May fixed asset investment and retail sales data missed market expectations

## Bottom line:

China’s May fixed asset investment and retail sales data missed market expectations, while industrial production was largely in line. Industrial production (IP) growth rose modestly to 4.5% yoy in May from 4.1% yoy in April thanks to stronger-than-expected exports, with faster output growth in computer and other equipment, electronic machinery, and utilities industries more than offsetting slower output growth in chemicals and non-ferrous metal smelting industries. On a single-month basis, fixed asset investment (FAI) growth fell further -10.6% yoy in May from -8.2% yoy in April, reflecting both adverse weather conditions and a still-slow pace of government bond issuance. Retail sales growth continued to slow in May, to -0.6% yoy from +0.2% yoy in April, the lowest since December 2022, partly due to last May’s high base. That said, the services industry output index growth – which is on a real basis and tracks tertiary (services) GDP growth closely – edged up to 4.4% yoy in May from 4.3% yoy in April, and we believe its widening gap with retail sales growth suggests that services consumption growth continued to outperform goods consumption growth. Weaker-than-expected April-May activity data pose a downside risk to our Q2 real GDP growth forecast (4.0% qoq sa annualized and 4.7% yoy currently), while the latest development in the Middle East and recent policy communications bode well for a sequential growth improvement in Q3, in our view.

## Asia-MAP scores:

Industrial production: 0 (5, 0)

Fixed asset investment: -10 (2, -5)

Retail sales: 0 (1, 0)

## Key numbers:

Industrial production (IP): +4.5% yoy in May (GS forecast: +4.3% yoy; Bloomberg consensus: +4.4% yoy), vs. +4.1% yoy in April. Note sequential figures are highly sensitive to the specific seasonal adjustment methodology (NBS estimates: +0.4% mom sa non-annualized in May, vs. +0.1% mom sa non-annualized in April; GS estimates: +0.2% mom sa non-annualized in May, vs. -1.1% mom sa non-annualized in April).

Fixed asset investment (FAI): -4.1% ytd yoy in May (GS: -3.1% ytd yoy; consensus: -2.3% ytd yoy), vs. -1.6% ytd yoy in April; May single-month by GS estimates: -10.6% yoy, vs. -8.2% yoy in April (sequential growth by GS estimates: -4.4% mom sa non-annualized in May, vs. -9.4% mom sa non-annualized in April).

Lisheng Wang

+852-3966-4004

lisheng.wang@gs.com

GS (Asia) L.L.C.

Retail sales: -0.6% yoy in May (GS: -0.6% yoy; consensus: -0.2% yoy), vs. +0.2% yoy in April (sequential growth by GS estimates: -0.4% mom sa non-annualized in May, vs. -1.0% mom sa non-annualized in April).

Services industry output index: +4.4% yoy in May, vs. +4.3% yoy in April (sequential growth by GS estimates: +0.4% mom sa non-annualized in May, vs. -0.2% mom sa non-annualized in April).

Surveyed unemployment rates:

Nationwide: 5.1% in May, vs. 5.2% in April.  
■ 31 major cities: 5.1% in May, vs. 5.2% in April.

Property-related activity data:

■ Floor space sold: -13.1% yoy in May, vs. -9.5% yoy in April (value of sales: -9.5% yoy in May, vs. -7.7% yoy in April).  
■ Floor area under construction: -12.3% yoy in May, vs. -12.1% yoy in April.  
■ New home starts: -24.6% yoy in May, vs. -26.6% yoy in April.  
■ New home completions: -19.9% yoy in May, vs. -18.8% yoy in April.  
Real estate investment: -24.3% yoy in May, vs. -20.1% yoy in April.

## Main points:

1. Industrial production (IP) growth rose modestly to 4.5% yoy from 4.1% yoy thanks to stronger-than-expected exports, although automobile output growth remained weak and the ongoing global energy shock continued to weigh on chemical-related manufacturing output. In sequential terms, IP gained 0.2% mom non-annualized in May based on our estimates (vs. -1.1% mom non-annualized in April; Exhibit 1). By industry, the April-to-May acceleration in year-on-year IP growth was led by faster output growth in computer & other equipment, electronic machinery, and utilities industries, more than offsetting slower output growth in chemicals and non-ferrous metal smelting industries (Exhibit 2). Among major industrial products (different from by-industry breakdown), year-on-year growth in industrial robot output, metal cutting machine output and power generation rose to +27.9%, +10.7% and +4.2%, respectively, in May from +15.1%, +7.5% and +2.6% in April, while automobile, computer and smartphone output growth in year-on-year terms slowed to -3.2%, -19.4% and -8.8%, respectively, from -2.6%, -9.3% and +4.7%. Year-on-year growth in chemical fiber and sulfuric acid output remained weak at -3.3% and -1.6%, respectively, in May (vs. -3.9% and -2.2% in April), owing to continued supply chain disruptions amid the Middle East conflict. Crude steel and cement output growth increased slightly to -2.7% yoy and -8.1% yoy, respectively, in May from -2.8% yoy and -10.8% yoy in April.

2. Fixed asset investment (FAI) growth fell further -10.6% yoy in May from -8.2% yoy in April on a single-month basis (Exhibit 3), reflecting both adverse weather conditions (e.g., heavy rainfall in southern and central China and a heatwave in northern China) and a still-slow pace of government bond issuance. This takes year-to-date FAI growth to -4.1% yoy in May (vs. -1.6% yoy in April). By sector, year-on-year growth in infrastructure, property and other investment (i.e., services and agriculture-related) fell to -11.2%, -24.3% and -13.2%, respectively, in May from -5.6%, -20.1% and -10.6% in

April, while manufacturing investment growth improved slightly to -4.1% yoy from -4.8% yoy. That said, we caution that the occasional NBS “statistical correction” of previously over-reported data may have exaggerated the volatility of reported FAI growth in recent quarters, as the year-on-year contraction in crude steel and cement output narrowed modestly in May.

3. Nominal retail sales growth continued to slow in May, to -0.6% yoy from +0.2% yoy in April, the lowest since December 2022 (during the Covid exit wave), with year-on-year growth in goods sales and restaurant sales revenue both weakening. Offline goods sales growth dropped to -2.4% yoy in May from -0.2% yoy in April, while online goods sales growth rose to +2.8% yoy from +0.1% yoy. Restaurant sales revenue growth slowed to 0.6% yoy in May from 2.2% yoy in April. Retail sales by enterprises above the designated size declined 4.9% yoy in May (vs. -4.4% yoy in April), much weaker than headline retail sales growth, suggesting large retailers have underperformed smaller ones in recent months. Among major products, year-on-year growth in home appliance and electronic equipment sales slowed further to -15.6% and +0.7%, respectively, in May from -15.1% and +6.2% in April on a high base last year, and year-on-year contraction in automobile sales widened to -16.1% from -15.3%. Gasoline and other oil products sales growth remained subdued at -3.2% yoy in May, despite a modest improvement from -6.5% yoy in April. Adjusting for price factors, we estimate gasoline and other oil product sales volume contracted by 13% yoy in May (vs. -17% yoy in March-April) amid an 11% yoy increase in domestic fuel prices, which implies a larger demand response than historical patterns would suggest, likely because alternatives such as non-fossil energy supply, rapid EV adoption, and urban public transportation are now more widely available than in earlier oil-price upcycles. In sequential terms, retail sales value declined by 0.4% mom sa non-annualized in May after seasonal adjustment, based on our estimates (vs. -1.0% mom sa non-annualized in April).

4. Year-on-year growth in the Services Industry Output Index – which is on a real basis and tracks tertiary GDP growth closely (58% of the Chinese economy as of 2025) – edged up to 4.4% in May from 4.3% in April. Its gap with retail sales growth widened further to 5.0pp in May from 4.1pp in April, suggesting that services consumption growth continued to outperform goods consumption growth. In sequential terms, we estimate the Services Industry Output Index gained 0.4% mom sa non-annualized in May (vs. -0.2% mom sa non-annualized in April).

5. Property activity data remained under pressure in May despite recent green shoots in large cities (Exhibit 4). Year-on-year growth in property sales registered -13.1% in volume (floor space) terms and -9.5% in value terms in May (vs. -9.5%/-7.7% in April). New home under construction and completions growth slowed to -12.3% yoy and -19.9% yoy, respectively in May from -12.1% yoy and -18.8% yoy in April. New home starts growth remained depressed at -24.6% yoy in May, despite a modest improvement from -26.6% yoy in April. NBS and private sector data both showed continued downward pressure on home prices in May, mainly in lower-tier cities.

6. Regarding the labor market, both the nationwide and 31-city unemployment rates (not seasonally adjusted) edged down to $5.1\%$ for May from $5.2\%$ for April. After seasonal adjustment, we estimate the nationwide unemployment rate inched down to $5.2\%$ in May from $5.3\%$ in April, and the 31-city metric remained flat at $5.2\%$ (Exhibit 5). The unemployment rate for migrant workers (without local Hukou) edged down to $4.9\%$ in May from $5.0\%$ in April after seasonal adjustment. Following the NBS definition

revisions (excluding students in schools) in January 2024, the release of youth unemployment rate data has been delayed by around three days vs. general labor market statistics. The latest data available suggests the unemployment rate of the 16-24 age group declined to 16.3% in April from 16.9% in March (vs. 15.8% in April 2025), while we caution that this indicator may have underestimated the labor market stress that younger generation is facing amid weak domestic demand and risks of AI adoption weighing on entry-level white-collar jobs, because of the definition change.

7. In our view, weaker-than-expected April-May activity data reflects the negative impact from the global energy-supply shock, adverse weather conditions and a lack of significant policy easing, and we see a downside risk to our Q2 real GDP growth forecast (4.0% qoq sa annualized and 4.7% yoy currently). However, the latest development in the Middle East and recent policy communications bode well for a sequential growth improvement in Q3, especially given the significant unused government bond quota left for the remainder of this year. We see July as an important window to monitor potential policy fine-tuning: if Q2 GDP disappoints meaningfully, there is a decent chance for policymakers to step up their easing rhetoric in the July Politburo meeting and draw on remaining fiscal buffers quickly to stabilize investment and growth.

## Lisheng Wang

Exhibit 1: Industrial production rose in month-on-month terms in May after seasonal adjustment  
![](images/8a4ba5d6a1ecdec87b57b1ccb167b123923eea00814b75a22c7e5b05e3603fd6.jpg)

<details>
<summary>line chart</summary>

| Year | Month-over-month | 3m/3m |
|------|------------------|-------|
| 2019 | ~10              | ~5    |
| 2020 | ~80              | ~80   |
| 2021 | ~20              | ~15   |
| 2022 | ~45              | ~10   |
| 2023 | ~15              | ~5    |
| 2024 | ~10              | ~5    |
| 2025 | ~5               | ~5    |
| 2026 | ~0               | ~5    |
</details>

Sequential IP growth numbers refer to GS estimates.  
Source: NBS, CEIC, GS Global Investment Research

Exhibit 2: April-to-May acceleration in year-on-year IP growth was led by computer & other equipment, electric machinery and utilities industries  
![](images/e3afca2a28b1c9c5a51bb5c976b4cdad211805cbfd2cc36ddab12c00a8e08de1.jpg)

<details>
<summary>bar chart</summary>

| Category               | Percentage points |
| ---------------------- | ----------------- |
| Computer and Other     | 0.2               |
| Equipment              | 0.15              |
| Electric Machinery     | 0.1               |
| Electricity & Heat     | 0.08              |
| Special Equipment      | 0.06              |
| Pharmaceutical         | 0.05              |
| General Equipment      | 0.04              |
| Metal Product          | 0.03              |
| Non-metal Product       | 0.02              |
| Ferrous Smelting       | 0.01              |
| Rubber & Plastic       | 0.0               |
| Textile                | -0.01             |
| Food                   | -0.02             |
| Rail, Ship and Aircraft| -0.03             |
| Auto                   | -0.05             |
| Agricultural & Sideline Food | -0.07            |
| Non Ferrous Smelting   | -0.1              |
| Chemicals              | -0.4              |
</details>

Source: NBS, CEIC, GS Global Investment Research

Exhibit 3: FAI growth declined further in May  
![](images/58c6bfeafa70a68b07c1abecdffcdd698d0b7d93fdf1b72e8b35323191eef3b7.jpg)

<details>
<summary>line chart</summary>

| Year | Headline | Manufacturing | Property | Infrastructure | Other |
|------|----------|---------------|----------|----------------|-------|
| 2019 | 100      | 100           | 100      | 100            | 100   |
| 2020 | 75       | 70            | 75       | 75             | 75    |
| 2021 | 105      | 105           | 115      | 110            | 85    |
| 2022 | 115      | 115           | 105      | 115            | 95    |
| 2023 | 120      | 125           | 95       | 125            | 105   |
| 2024 | 125      | 135           | 85       | 135            | 105   |
| 2025 | 130      | 145           | 75       | 145            | 95    |
| 2026 | 125      | 155           | 65       | 155            | 85    |
</details>

Source: CEIC, Data compiled by GS Global Investment Research

Exhibit 4: Most property activity data remained subdued in May  
![](images/8f1d8607aff3af0ce4facd84d7a25b6669a060392fdcf14e29ad56431ae9a555.jpg)

<details>
<summary>line chart</summary>

| Year | Floor Space Started | Floor Space Completed | Floor Space Sold | Sales value |
|------|---------------------|-----------------------|------------------|-------------|
| 2019 | ~100                | ~100                  | ~100             | ~100        |
| 2020 | ~55                 | ~75                   | ~105             | ~55         |
| 2021 | ~85                 | ~150                  | ~115             | ~130        |
| 2022 | ~60                 | ~80                   | ~90              | ~70         |
| 2023 | ~40                 | ~110                  | ~80              | ~95         |
| 2024 | ~35                 | ~90                   | ~70              | ~75         |
| 2025 | ~30                 | ~75                   | ~65              | ~65         |
| 2026 | ~20                 | ~60                   | ~55              | ~55         |
</details>

Source: CEIC, Data compiled by GS Global Investment Research

Exhibit 5: After seasonal adjustment, nationwide surveyed unemployment rate edged down in May, while the 31-city metric stayed flat  
![](images/294adae3702b89f1031fb8060d51ecd56f685f8d9e4a264e1505624aa56cdf8a.jpg)

<details>
<summary>line chart</summary>

| Year | National | 31 major cities |
|------|----------|-----------------|
| 2017 | ~5.1     | ~5.0            |
| 2018 | ~4.9     | ~4.8            |
| 2019 | ~5.0     | ~4.9            |
| 2020 | ~5.9     | ~5.8            |
| 2021 | ~5.3     | ~5.4            |
| 2022 | ~6.1     | ~6.8            |
| 2023 | ~5.8     | ~6.8            |
| 2024 | ~5.1     | ~5.0            |
| 2025 | ~5.2     | ~5.1            |
| 2026 | ~5.3     | ~5.1            |
</details>

Source: NBS, Wind, GS Global Investment Research

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

I, Lisheng Wang, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Lisheng Wang GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the exte

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
