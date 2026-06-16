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
## Software Snippets | Europe

# Visualising the AI Software Drawdown

Important events in the world of Software & Services in the week ahead, and key MS research / stories from the past week.

## Key Takeaways

■ Visualising the AI Software drawdown (#Software)  
AI Counts - The Accounting Automation Wave (\*MS Research\*, #Wolters Kluwer)  
Databricks, Lovable, and PhysicsX funding rounds and reports (#Software)  
■ UK company account digital filing requirements likely a small tailwind for Sage (#Sage)  
London Tech Week 2026 Takeaways: All things AI (\*MS Research\*, #Software, #Informa)

1) Visualising the AI Software Drawdown (#Software): The weak price performance across application software largely stems back to around August last year, albeit we have started to see some sub-sector level dispersion between other areas of the software market such as data infrastructure and cybersecurity names. However, here we visualise an around 2-decade perspective, but look at a selection of mid/large-cap software stocks that have been listed since January 2005 (>50 in total in our analysis). We have run their stock performance over this period in an equal-weighted aggregated way into a visualisation that also shows the depth of drawdowns from the latest all-time high through this period. While there is inherently a degree of survivorship bias in this, it paints an interesting picture; this selection peaked during COVID, in late 2021, and did not quite manage to reach new all-time highs in late 2024/early 2025. As such, it is closing in on a 1,700 day run without reaching a new all-time high level, and is tracking down >35% from its last all-time highs. Similar deep magnitudes of drawdowns were only seen during the global financial crisis, and during the rate-hike and multiple-compression period coming out of COVID-19.

MS & CO. INTERNATIONAL PLC+

## George W Webb

Equity Analyst

George.Webb@morganstanley.com +44 20 7425-2686

## Mark Hyatt

Equity Analyst

Mark.Hyatt@morganstanley.com +44 20 7677-3663

## William Richards

Research Associate

William.Richards1@morganstanley.com +44 20 7425-0269

## TECHNOLOGY - SOFTWARE & SERVICES

Europe

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Exhibit 1: Long-listed global software stock selection - performance over time  
![](images/be2e96f62630b955abc61f4d1f8770765698a635a2d1a26ebdbc3a8996fd75c6.jpg)

<details>
<summary>line chart</summary>

| Date       | Value |
| ---------- | ----- |
| Jan-2005   | ~3900 |
| Jan-2006   | ~3800 |
| Jan-2007   | ~3700 |
| Jan-2008   | ~3500 |
| Jan-2009   | ~2000 |
| Jan-2010   | ~3800 |
| Jan-2011   | ~3900 |
| Jan-2012   | ~3700 |
| Jan-2013   | ~3800 |
| Jan-2014   | ~3900 |
| Jan-2015   | ~3700 |
| Jan-2016   | ~3500 |
| Jan-2017   | ~3800 |
| Jan-2018   | ~3900 |
| Jan-2019   | ~3800 |
| Jan-2020   | ~3700 |
| Jan-2021   | ~3800 |
| Jan-2022   | ~3900 |
| Jan-2023   | ~3700 |
| Jan-2024   | ~3800 |
| Jan-2025   | ~3900 |
| Jan-2026   | ~3700 |
</details>

Source: Refinitiv data, MS for analysis

## 2) AI Counts - The Accounting Automation Wave (\*MS Research\*, #Wolters

Kluwer): Our colleague Toni Kaplan (who covers US Information Services) led a note this week on the AI growth opportunity for the Tax & Accounting Industry, focusing on the market serving tax and accounting firms themselves. This is a market led by Wolters Kluwer and Thomson Reuters, but also with Intuit and Drake Software as key players at the lower end of the market. The accounting industry is increasingly embracing AI as a solution to two structural challenges: a persistent shortage of qualified professionals and growing regulatory complexity. Generative AI adoption within the tax and accounting industries is accelerating rapidly, with Thomson Reuters' 2026 AI in Professional Services Report showing that over a third of tax firms and corporate tax departments (c. 34% for both) have already deployed GenAI at an organizational level. While AI-native startups are increasingly attacking individual workflow steps, we expect the core tax engine market to remain dominated by incumbents such as Thomson Reuters and Wolters Kluwer, whose established infrastructure, trusted compliance systems, and embedded customer workflows create durable barriers to entry. See the full note here.

Exhibit 2: Wolters Kluwer Tax & Accounting segment vs Thomson Reuters Tax & Accounting Professionals segment  
![](images/82b67d2399bdb80b79c7dec931dc966b574ce3f0686f6d8b3a4f3bb80b9558e0.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | WKL - Tax & Accounting revenue (%) | TRI - Tax & Accounting Professionals revenue (%) | WKL - Tax & Accounting Y/Y org. revenue growth (%) | TRI - Tax & Accounting Professionals Y/Y org. revenue growth (%) |
| :--- | :--- | :--- | :--- | :--- |
| FY20 | 6.5 | 1.0 | 2.5 | 5.0 |
| FY21 | 7.0 | 3.0 | 3.0 | 9.0 |
| FY22 | 7.3 | 3.5 | 3.5 | 9.0 |
| FY23 | 8.2 | 4.0 | 4.0 | 1,00 |
| FY24 | 9.0 | 4.8 | 4.8 | 1,00 |
| FY25 | 10.5 | 5.8 | 5.8 | 1,11 |
</details>

NB: WKL data translated at relevant EUR/USD FY average FX rates. Source: Company data, MS

## 3) Databricks, Lovable, and PhysicsX funding rounds and reports (#Software):

According to The Information (unconfirmed), Databricks is reportedly in talks to raise funds at a \$165bn+ valuation, which would be a jump from the last round at a \$134bn valuation in February. The news comes on the back of renewed interest in the data infrastructure software segment of the software market, which has rallied despite broader weakness across application software; Snowflake's stock is c. +58% over the past month, MongoDB c. +15%, and Datadog c. +17%. Separately, Forbes reported (unconfirmed) that Sweden-based Lovable, an AI-powered app-builder, is in talks to raise funds at a \$12bn valuation, which would be a notable step-up from its \$6.6bn Series B round in December 2025. Elsewhere, PhysicsX, a physical-AI engineering platform announced a \$330m Series C financing at a valuation of c. \$2.4 billion, up from a nearly \$1 billion valuation at their Series B.

## 4) UK company account digital filing requirements likely a small tailwind for

Sage (#Sage): Companies House has confirmed a delayed version of its Economic Crime and Corporate Transparency Act (ECCT) accounts reforms. From April 2028, all UK companies will need to file annual accounts using commercial software. We think this should drive further software adoption across the long tail of UK companies, with c. 4.9m companies on the effective register and Companies House previously noting back in 2023 that over 65% of companies already used software filing. For Sage, we think this change is likely to be supportive of UKIA growth (where we forecast c. 9% CAGR FY26-29e), but it is unlikely to be a major group level tailwind, given the remaining opportunity is likely concentrated in smaller/micro entities, dormant companies, and low-complexity holding/SPV structures where average revenue per user is relatively low. However, we acknowledge the 2028 implementation deadline comes a year later than was previously expected, to give businesses greater time to prepare for the changes.

## 5) London Tech Week 2026 Takeaways: All things AI (\*MS Research\*, #Software, #Informa): We attended London Tech Week, hosted by Informa. We share a few of our takeaways below, but for our full takeaways see our note here.

- Enterprise worker AI usage: Many UK workers have tried AI but daily usage, training, and measurable productivity gains remain limited, implying enterprise AI adoption is still early and ROI is not yet broadly well measured.  
- Legal AI: The volume of tokens Harvey has processed on its platform has grown from 1 trillion per month at the start of the year, to 15 trillion now. Meanwhile, Legora has opened new offices in Madrid, Milan and Paris.  
- Websites, search, marketing, and GEO: Marketing is shifting from traditional SEO toward Generative Engine Optimisation, where brands must structure online context for AI systems while websites remain important as the enterprise's digital home.  
- AI adoption in financial services: Banks and asset managers are moving from AI experimentation toward targeted, ROI-focused deployments, with greater attention to token budgets, governance, model routing, and build-versus-buy discipline.

Exhibit 3: Key week ahead events

<table><tr><td>Monday15/06/2026</td><td>Tuesday16/06/2026</td><td>Wednesday17/06/2026</td><td>Thursday18/06/2026</td><td>Friday19/06/2026</td></tr><tr><td></td><td>Wiley 4Q26 Results</td><td></td><td>Informa 2026 AGMAccenture 3Q26 Results</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Key</td><td>MS Europe Coverage</td><td>Other Global Stocks</td><td>Industry Event</td><td>Other</td></tr></table>

Source: MS

## Coverage Valuation vs. European Market

Exhibit 4: European Software NTM P/E vs STOXX Europe 600  
![](images/ee532c42812ae74e4d0d7017a2d87996a5537527fc7927acfb4682f632d59938.jpg)

<details>
<summary>line chart</summary>

| Year | NTM P/E | Mean | +1σ Lower | +1σ Upper | -1σ Lower | -1σ Upper |
|------|---------|------|-----------|-----------|-----------|-----------|
| 2006 | ~17.5   | 20   | ~14       | ~25       | ~13       | ~26       |
| 2007 | ~18.5   | 20   | ~14       | ~25       | ~13       | ~26       |
| 2008 | ~13     | 20   | ~9        | ~25       | ~8        | ~26       |
| 2009 | ~14     | 20   | ~10       | ~25       | ~9        | ~26       |
| 2010 | ~14.5   | 20   | ~10.5     | ~25       | ~9.5      | ~26       |
| 2011 | ~13     | 20   | ~9        | ~25       | ~8        | ~26       |
| 2012 | ~14     | 20   | ~10       | ~25       | ~9        | ~26       |
| 2013 | ~15     | 20   | ~11       | ~25       | ~10       | ~26       |
| 2014 | ~16     | 20   | ~12       | ~25       | ~11       | ~26       |
| 2015 | ~18     | 20   | ~13       | ~25       | ~12       | ~26       |
| 2016 | ~20     | 20   | ~14       | ~25       | ~13       | ~26       |
| 2017 | ~22     | 20   | ~14.5     | ~25       | ~13.5     | ~26       |
| 2018 | ~25     | 20   | ~15       | ~25       | ~14       | ~26       |
| 2019 | ~27     | 20   | ~15.5     | ~25       | ~14.5     | ~26       |
| 2020 | ~18     | 20   | ~11      | ~25       | ~11       | ~26       |
| 2021 | ~32     | 20   | ~16       | ~25       | ~17       | ~33       |
| 2022 | ~24     | 20   | ~13       | ~25       | ~13       | ~26       |
| 2023 | ~25     | 20   | ~13.5     | ~25       | ~13.5     | ~26       |
| 2024 | ~27     | 20   | ~14       | ~25       | ~14       | ~26       |
| 2025 | ~28     | 20   | ~14.5     | ~25       | ~14.5     | ~26       |
| 2026 | ~15     | 20   | ~13.5     | ~25       | ~13.5     | ~26       |
</details>

NB: Mean of CAP, DSY, INF, NEM, REL, SGE, SAP, TEMN, TIETO, and WKL. Price at close as of T-1 business day. Source: FactSet, MS

## Long-Term Valuation Charts

Exhibit 5: Amadeus P/NTM Earnings  
![](images/8a82014fcd875c346c7b31da888deb073a27c54d846b6eb5e1930f9d75a3414d.jpg)

<details>
<summary>line chart</summary>

| Year | NTM P/E | Mean | +1σ | -1σ |
|------|---------|------|-----|-----|
| 2010 | ~14     | 25   | 40  | 9   |
| 2011 | ~13     | 25   | 40  | 9   |
| 2012 | ~10     | 25   | 40  | 9   |
| 2013 | ~12     | 25   | 40  | 9   |
| 2014 | ~15     | 25   | 40  | 9   |
| 2015 | ~18     | 25   | 40  | 9   |
| 2016 | ~20     | 25   | 40  | 9   |
| 2017 | ~22     | 25   | 40  | 9   |
| 2018 | ~25     | 25   | 40  | 9   |
| 2019 | ~30     | 25   | 40  | 9   |
| 2020 | ~15     | 25   | 40  | 9   |
| 2021 | ~50     | 25   | 40  | 9   |
| 2022 | ~45     | 25   | 40  | 9   |
| 2023 | ~30     | 25   | 40  | 9   |
| 2024 | ~25     | 25   | 40  | 9   |
| 2025 | ~20     | 25   | 40  | 9   |
| 2026 | ~15     | 25   | 40  | 9   |
</details>

NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 6: Capgemini P/NTM Earnings  
![](images/865b9f6474c2567ec971f1ca3f290a70e138f4ae00223e17b0c21d0483732a0a.jpg)

<details>
<summary>line chart</summary>

| Year | NTM P/E | Mean | +1σ | -1σ |
|------|---------|------|-----|-----|
| 2006 | ~18     | 15   | 17  | 11  |
| 2007 | ~19     | 15   | 17  | 11  |
| 2008 | ~7      | 15   | 17  | 11  |
| 2009 | ~14     | 15   | 17  | 11  |
| 2010 | ~19     | 15   | 17  | 11  |
| 2011 | ~16     | 15   | 17  | 11  |
| 2012 | ~9      | 15   | 17  | 11  |
| 2013 | ~13     | 15   | 17  | 11  |
| 2014 | ~15     | 15   | 17  | 11  |
| 2015 | ~18     | 15   | 17  | 11  |
| 2016 | ~16     | 15   | 17  | 11  |
| 2017 | ~14     | 15   | 17  | 11  |
| 2018 | ~17     | 15   | 17  | 11  |
| 2019 | ~16     | 15   | 17  | 11  |
| 2020 | ~9      | 15   | 17  | 11  |
| 2021 | ~23     | 15   | 17  | 11  |
| 2022 | ~15     | 15   | 17  | 11  |
| 2023 | ~14     | 15   | 17  | 11  |
| 2024 | ~18     | 15   | 17  | 11  |
| 2025 | ~13     | 15   | 17  | 11  |
| 2026 | ~7      | 15   | 17  | 11  |
</details>

NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 7: Dassault Systemes P/NTM Earnings  
![](images/5b7056635a2ef1fb2ff53b9a7568bf3d91529d1671385bd7aeeaec683a4ca0ad.jpg)

<details>
<summary>line chart</summary>

| Year | NTM P/E |
|------|---------|
| 2006 | 22      |
| 2007 | 20      |
| 2008 | 15      |
| 2009 | 18      |
| 2010 | 20      |
| 2011 | 19      |
| 2012 | 21      |
| 2013 | 24      |
| 2014 | 26      |
| 2015 | 30      |
| 2016 | 28      |
| 2017 | 32      |
| 2018 | 38      |
| 2019 | 35      |
| 2020 | 37      |
| 2021 | 55      |
| 2022 | 45      |
| 2023 | 35      |
| 2024 | 30      |
| 2025 | 25      |
| 2026 | 15      |
</details>

NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 8: HBX P/NTM Earnings  
![](images/9d8a08b7348845db0a1d64d6c6db547807e9ec83ea967fa348d0d8e7fb4af2d4.jpg)

<details>
<summary>line chart</summary>

| Year | NTM P/E | Mean | +1σ | -1σ |
|------|---------|------|-----|-----|
| 2025 | 13.0    | 8.5  | 11.0| 6.5 |
| 2026 | 6.0     | 8.5  | 11.0| 6.5 |
</details>

NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 9: Indra P/NTM Earnings  
![](images/d82658d8db5de44855840d05e0bba60cce3555c3515921d1cb1dcd59476427cd.jpg)

<details>
<summary>line chart</summary>

| Year | NTM P/E | Mean | +1σ | -1σ |
|------|---------|------|-----|-----|
| 2006 | ~18     | 13   | 16  | 9   |
| 2007 | ~20     | 13   | 16  | 9   |
| 2008 | ~16     | 13   | 16  | 9   |
| 2009 | ~14     | 13   | 16  | 9   |
| 2010 | ~13     | 13   | 16  | 9   |
| 2011 | ~10     | 13   | 16  | 9   |
| 2012 | ~8      | 13   | 16  | 9   |
| 2013 | ~10     | 13   | 16  | 9   |
| 2014 | ~17     | 13   | 16  | 9   |
| 2015 | ~23     | 13   | 16  | 9   |
| 2016 | ~16     | 13   | 16  | 9   |
| 2017 | ~15     | 13   | 16  | 9   |
| 2018 | ~14     | 13   | 16  | 9   |
| 2019 | ~12     | 13   | 16  | 9   |
| 2020 | ~10     | 13   | 16  | 9   |
| 2021 | ~12     | 13   | 16  | 9   |
| 2022 | ~8      | 13   | 16  | 9   |
| 2023 | ~10     | 13   | 16  | 9   |
| 2024 | ~13     | 13   | 16  | 9   |
| 2025 | ~25     | 13   | 16  | 9   |
| 2026 | ~20     | 13   | 16  | 9   |
</details>

NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 10: Informa P/NTM Earnings  
![](images/3ac16b257135a6e426c4462522e6f33e70b8c24c10ac312f876bca8526c2bc48.jpg)

<details>
<summary>line chart</summary>

| Year | NTM P/E | Mean | +1σ | -1σ |
|------|---------|------|-----|-----|
| 2006 | ~13.5   | 13.5 | 17.0 | 10.0 |
| 2007 | ~16.5   | 13.5 | 17.0 | 10.0 |
| 2008 | ~4.0    | 13.5 | 17.0 | 10.0 |
| 2009 | ~8.0    | 13.5 | 17.0 | 10.0 |
| 2010 | ~11.0   | 13.5 | 17.0 | 10.0 |
| 2011 | ~9.0    | 13.5 | 17.0 | 10.0 |
| 2012 | ~10.5   | 13.5 | 17.0 | 10.0 |
| 2013 | ~12.0   | 13.5 | 17.0 | 10.0 |
| 2014 | ~13.0   | 13.5 | 17.0 | 10.0 |
| 2015 | ~14.0   | 13.5 | 17.0 | 10.0 |
| 2016 | ~14.5   | 13.5 | 17.0 | 10.0 |
| 2017 | ~15.0   | 13.5 | 17.0 | 10.0 |
| 2018 | ~17.0   | 13.5 | 17.0 | 10.0 |
| 2019 | ~13.0   | 13.5 | 17.0 | 10.0 |
| 2020 | ~9.0    | 13.5 | 17.0 | 10.0 |
| 2021 | ~24.0   | 13.5 | 17.0 | 10.0 |
| 2022 | ~25.5   | 13.5 | 17.0 | 10.0 |
| 2023 | ~18.0   | 13.5 | 17.0 | 10.0 |
| 2024 | ~16.5   | 13.5 | 17.0 | 10.0 |
| 2025 | ~15.5   | 13.5 | 17.0 | 10.0 |
| 2026 | ~13.5   | 13.5 | 17.0 | 10.0 |
</details>

NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 11: IONOS P/NTM Earnings  
![](images/ba247597736c51715d09c1593db0edd19547716e8be30877de5801c1bd428401.jpg)

<details>
<summary>line chart</summary>

| Year | NTM P/E | Mean | +1σ | -1σ |
|------|---------|------|-----|-----|
| 2022 |         |      |     |     |
| 2023 |         |      |     |     |
| 2024 |         |      |     |     |
| 2025 |         |      |     |     |
| 2026 |         |      |     |     |
</details>

NB: Price at close as of T-1 business day. Source: FactSet, MS

Exhibit 12: Nemetschek Group P/NTM Earnings  
![](images/c574f977a08a522df9504e23276d1a7feb97f781caf404711f9233be8153b11f.jpg)

<details>
<summary>line chart</summary>

| Year | NTM P/E | Mean | +1σ | -1σ |
|------|---------|------|-----|-----|
| 2006 | ~15     | 33   | 54  | 13  |
| 2007 | ~12     | 33   | 54  | 13  |
| 2008 | ~8      | 33   | 54  | 13  |
| 2009 | ~10     | 33   | 54  | 13  |
| 2010 | ~12     | 33   | 54  | 13  |
| 2011 | ~15     | 33   | 54  | 13  |
| 2012 | ~18     | 33   | 54  | 13  |
| 2013 | ~20     | 33   | 54  | 13  |
| 2014 | ~25     | 33   | 54  | 13  |
| 2015 | ~30     | 33   | 54  | 13  |
| 2016 | ~35     | 33   | 54  | 13  |
| 2017 | ~40     | 33   | 54  | 13  |
| 2018 | ~50     | 33   | 54  | 13  |
| 2019 | ~60     | 33 

[中间内容因长度限制已省略]

 who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Technology - Software & Services

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/12/2026)</td></tr><tr><td colspan="3">Adam Wood</td></tr><tr><td>Indra (IDR.MC)</td><td>E (01/12/2026)</td><td>€56.04</td></tr><tr><td>SAP SE (SAP.N)</td><td>O (02/20/2026)</td><td>US$164.18</td></tr><tr><td>SAP SE (SAPG.DE)</td><td>O (03/20/2020)</td><td>€140.26</td></tr><tr><td colspan="3">George W Webb</td></tr><tr><td>Amadeus IT Holdings S.A. (AMA.MC)</td><td>O (04/10/2026)</td><td>€50.96</td></tr><tr><td>Capgemini (CAPP.PA)</td><td>E (02/19/2026)</td><td>€96.72</td></tr><tr><td>Dassault Systemes SA (DAST.PA)</td><td>E (03/17/2026)</td><td>€17.21</td></tr><tr><td>Hexagon AB (HEXAb.ST)</td><td></td><td>SKr 79.00</td></tr><tr><td>IONOS Group SE (IOSn.DE)</td><td>E (05/12/2025)</td><td>€26.64</td></tr><tr><td>Nemetschek SE (NEKG.DE)</td><td>E (07/13/2022)</td><td>€56.30</td></tr><tr><td>Netcompany Group A/S (NETCG.CO)</td><td>U (01/12/2026)</td><td>DKr 332.00</td></tr><tr><td>Sage (SGE.L)</td><td>O (12/08/2021)</td><td>818p</td></tr><tr><td colspan="3">Mark Hyatt</td></tr><tr><td>HBX Group International PLC (HBX.MC)</td><td>E (04/17/2026)</td><td>€6.89</td></tr><tr><td>Temenos Group AG (TEMN.S)</td><td>U (12/15/2017)</td><td>SFr 64.30</td></tr><tr><td>Tietoevry Oyj (TIETO.HE)</td><td>U (01/12/2026)</td><td>€20.34</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.
"""
