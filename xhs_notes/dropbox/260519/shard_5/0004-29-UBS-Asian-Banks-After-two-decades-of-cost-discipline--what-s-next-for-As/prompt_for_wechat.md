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
# Asian Banks

# After two decades of cost discipline, what's next for Asian banks?

# AI as the next phase of cost efficiency

Asian banks have spent the past two decades relying heavily on cost discipline to offset structural revenue headwinds, with meaningful but incomplete success in our view. As traditional efficiency levers mature, we believe AI now represents the most important opportunity to drive structural cost efficiencies, albeit with likely limited near-term P&L impact as deployments remain incremental. Our key takeaways are threefold: 1) historical cost efficiency gains have cushioned, but not fully offset, revenue pressure; 2) AI's medium-term impact will likely be highly uneven across markets and banks, driven by structural readiness rather than technology availability alone; and 3) despite this, AI optionality appears largely unpriced, with little differentiation at the sector, market or bank level today. Over time, we see scope for AI readiness to emerge as a driver of valuation divergence (please refer to our companion APAC Focus note here).

# Cost efficiency has been the primary offset – but insufficient

Over the past 20 years, banks have used cost efficiency as the dominant lever to defend profitability, with opex-to-assets declining materially across most Asian markets. These gains have been driven by banking consolidation, branch rationalisation, process automation and tighter headcount discipline. Banks have also invested heavily in technology over this period; however, much of this spend has largely focused on maintaining competitiveness and operational stability, with limited evidence of step-change cost savings at the system level. As a result, cost savings have only partially offset structural revenue pressure at an aggregate level.

# AI adoption is accelerating, but near-term P&L impact remains limited

AI adoption across Asian banks is accelerating, but current deployments remain narrow and largely siloed, focused on use cases such as customer servicing, compliance monitoring, credit assessments and internal productivity tools. As with past waves of technology investment, near-term financial benefits tend to show up as capacity release, risk reduction or cost avoidance rather than explicit cost cuts. In many cases, productivity gains are reinvested into further digitalisation, data infrastructure or compliance requirements. As a result, evidence of a consistent and material near-term P&L uplift from AI remains mixed, reinforcing our view that the early phase of AI adoption is evolutionary rather than transformative.

# Medium term: AI as the scalable efficiency lever

Looking ahead, we see AI as the most meaningful lever to drive structural cost efficiencies over the medium term, particularly given that operations and labour account for roughly 60–70% of banks' total cost bases. We believe successful, end-to-end AI integration has the potential to decouple revenue growth from headcount and physical infrastructure, allowing digitally enabled labour to scale at very low marginal cost. However, the ability to realise these gains will vary materially across markets and institutions, depending on factors such as scale, technology culture, data infrastructure, labour flexibility and competitive urgency. While execution risks are significant, higher AI readiness may help sustain relative cost and valuation advantages even as cyclical tailwinds fade.

# Equities

Asia

Banks

Aakash Rawat, CFA

Analyst

aakash.rawat@ubs.com

+65-6495 8283

Benjamin Tan

Analyst

benjamin.tan-yx@ubs.com

+65-6495 3239

# Contents

Executive summary....3

Asian banks are facing structural headwinds on revenue ..... 6

Can lower operating expenses help to offset the headwinds on revenue?....7

What led to the lower opex/ assets ratio over the last 20y?....8

Are there significant differences on the cost-to-income ratio? ..... 10

Banking consolidation has helped in lowering cost pressures. . . . . . . . 11

Branch rationalisation initiatives are also underway....13

Even as total employee headcount has generally risen.... 14

...growth in staff costs per employee has lagged nominal GDP growth . 15

How much are banks spending on technology? 17

Are the technology investments leading to costs savings?....18

Alternate measures of operating efficiency 19

Loans per branch ratio. 19

Deposits per branch ratio 21

Will AI drive better costs efficiency for the Asian banks? . . . . 23

How do banking markets compare on opex related metrics?.. 27

Aakash Rawat, CFA

Analyst

aakash.rawat@ubs.com

+65-6495 8283

Benjamin Tan

Analyst

benjamin.tan-yx@ubs.com

+65-6495 3239

# Executive summary

Asian banks are facing structural revenue headwinds driven by demographics-led pressure on net interest income (NII) and persistent challenges in scaling fee income. While operating cost discipline over the past two decades has been meaningful, we think it has not been sufficient to fully offset revenue erosion, raising the key question of whether AI can unlock the next leg of sustainable efficiency gains.

# 1. Structural revenue pressure is real – and persistent

Asian banks are facing increasingly structural revenue headwinds (revenue/assets fell 60bps over the past 20 years), driven primarily by demographic pressures that are weighing on traditional banking income streams.

Ageing populations across the region are slowing deposit accumulation and loan growth, compressing net interest margins and placing net interest income on a long-term downtrend.

Over the past two decades, net interest income as a percentage of assets has declined materially across Asia, while efforts to pivot toward non-interest income have delivered limited relief. Regulatory constraints, structural market features and competitive intensity have made fee income difficult to scale, resulting in a decline in fee income/ assets at the regional level.

Taken together, total revenue/assets has fallen meaningfully over the past 20 years, reinforcing our view that revenue pressures facing Asian banks are structural rather than cyclical in nature.

Figure 1: Net interest income/assets ratio has declined 45bps on average over the past 20y for Asian banks   
![](images/4f0019d7d45315f4335ea96dcbbf5b8da199fc11bfab4a97bb18d4512464f012.jpg)

<details>
<summary>line</summary>

| Year | Average (Asia) | Average (Asia - DM) | Average (Asia - EM) |
|------|----------------|---------------------|---------------------|
| 2004 | 2.4%           | 1.7%                | 3.0%                |
| 2005 | 2.5%           | 1.8%                | 3.0%                |
| 2006 | 2.4%           | 1.6%                | 3.0%                |
| 2007 | 2.4%           | 1.6%                | 3.0%                |
| 2008 | 2.4%           | 1.6%                | 3.0%                |
| 2009 | 2.3%           | 1.5%                | 3.0%                |
| 2010 | 2.3%           | 1.4%                | 3.0%                |
| 2011 | 2.3%           | 1.4%                | 3.0%                |
| 2012 | 2.3%           | 1.4%                | 3.0%                |
| 2013 | 2.2%           | 1.3%                | 2.9%                |
| 2014 | 2.2%           | 1.3%                | 2.9%                |
| 2015 | 2.2%           | 1.3%                | 2.9%                |
| 2016 | 2.1%           | 1.3%                | 2.9%                |
| 2017 | 2.1%           | 1.3%                | 2.9%                |
| 2018 | 2.2%           | 1.3%                | 3.0%                |
| 2019 | 2.2%           | 1.3%                | 3.0%                |
| 2020 | 2.1%           | 1.1%                | 3.0%                |
| 2021 | 2.1%           | 1.1%                | 3.0%                |
| 2022 | 2.2%           | 1.3%                | 3.0%                |
| 2023 | 2.3%           | 1.3%                | 3.0%                |
| 2024 | 2.2%           | 1.3%                | 3.0%                |
| 2025 | 2.1%           | 1.3%                | 2.9%                |
</details>

Source: Central banks, company data, UBS estimates. Note: JP, AU, KR, SG, HK, TW banks are classified as DM banks above, while IN, CN, ID, PH, TH, MY, VN banks are classified as EM banks.

Figure 2: Fee income/assets has declined by 15bps on average over the past 20y for Asian banks   
![](images/6e94bbd4171e5ce5fead6b400cdfeaa84872259fcc6112aa4a825d657b22a301.jpg)

<details>
<summary>line</summary>

| Year | Average (Asia) | Average (Asia - DM) | Average (Asia - EM) |
|------|----------------|---------------------|---------------------|
| 2004 | 0.56%          | 0.60%               | 0.53%               |
| 2005 | 0.54%          | 0.52%               | 0.54%               |
| 2006 | 0.51%          | 0.47%               | 0.55%               |
| 2007 | 0.58%          | 0.54%               | 0.65%               |
| 2008 | 0.53%          | 0.40%               | 0.67%               |
| 2009 | 0.53%          | 0.41%               | 0.68%               |
| 2010 | 0.54%          | 0.40%               | 0.67%               |
| 2011 | 0.51%          | 0.39%               | 0.62%               |
| 2012 | 0.49%          | 0.38%               | 0.60%               |
| 2013 | 0.49%          | 0.38%               | 0.59%               |
| 2014 | 0.48%          | 0.37%               | 0.58%               |
| 2015 | 0.48%          | 0.37%               | 0.58%               |
| 2016 | 0.47%          | 0.36%               | 0.58%               |
| 2017 | 0.47%          | 0.35%               | 0.58%               |
| 2018 | 0.46%          | 0.34%               | 0.57%               |
| 2019 | 0.45%          | 0.33%               | 0.56%               |
| 2020 | 0.42%          | 0.31%               | 0.53%               |
| 2021 | 0.43%          | 0.29%               | 0.54%               |
| 2022 | 0.41%          | 0.26%               | 0.53%               |
| 2023 | 0.41%          | 0.25%               | 0.52%               |
| 2024 | 0.41%          | 0.27%               | 0.53%               |
| 2025 | 0.42%          | 0.29%               | 0.53%               |
</details>

Source: Central banks, Company data, UBS estimates. Note: JP, AU, KR, SG, HK, TW banks are classified as DM banks above, while IN, CN, ID, PH, TH, MY, VN banks are classified as EM banks.

# 2. Cost efficiency has helped – but only partially

Against this backdrop, banks have leaned heavily on cost discipline to protect profitability. Operating efficiency has improved steadily over the past two decades, with total operating expenses/assets declining (\~40bps over the past 20y) across most Asian markets.

However, these cost savings have only partially offset the revenue decline. At the aggregate level, lower operating expenses have compensated for roughly $\frac{2}{3}$ of the fall in revenues, and have not fully insulated bottom-line profitability.

There is also a clear divergence across regions: emerging market banks have, on average, more than offset revenue pressure through cost reductions, while developed market banks have only been able to offset around $\frac{1}{2}$ of the revenue decline.

Cost-to-income ratios have converged across Asia, with both developed and emerging market banks now operating at broadly similar levels, contrary to the common perception that emerging market banks are structurally less efficient.

Figure 3: Total opex/assets ratio declined by 40bps on average over the past 20y for Asian banks   
![](images/f616597057387356f9384ab1a4dac85a6a6b142617fdea230011e20201015aeb.jpg)

<details>
<summary>line</summary>

| Year | Average (Asia) | Average (Asia - DM) | Average (Asia - EM) |
|------|----------------|---------------------|---------------------|
| 2002 | 1.80%          | 1.40%               | 2.30%               |
| 2003 | 1.85%          | 1.38%               | 2.35%               |
| 2004 | 1.80%          | 1.35%               | 2.25%               |
| 2005 | 1.78%          | 1.32%               | 2.28%               |
| 2006 | 1.80%          | 1.30%               | 2.30%               |
| 2007 | 1.85%          | 1.28%               | 2.35%               |
| 2008 | 1.78%          | 1.25%               | 2.30%               |
| 2009 | 1.75%          | 1.22%               | 2.25%               |
| 2010 | 1.78%          | 1.20%               | 2.20%               |
| 2011 | 1.75%          | 1.18%               | 2.15%               |
| 2012 | 1.70%          | 1.15%               | 2.10%               |
| 2013 | 1.65%          | 1.12%               | 2.05%               |
| 2014 | 1.60%          | 1.10%               | 2.00%               |
| 2015 | 1.55%          | 1.08%               | 1.95%               |
| 2016 | 1.50%          | 1.05%               | 1.90%               |
| 2017 | 1.48%          | 1.03%               | 1.88%               |
| 2018 | 1.45%          | 1.00%               | 1.90%               |
| 2019 | 1.50%          | 0.98%               | 1.95%               |
| 2020 | 1.45%          | 0.95%               | 1.90%               |
| 2021 | 1.40%          | 0.92%               | 1.85%               |
| 2022 | 1.38%          | 0.90%               | 1.83%               |
| 2023 | 1.40%          | 0.92%               | 1.85%               |
| 2024 | 1.42%          | 0.95%               | 1.83%               |
| 2025 | 1.45%          | 0.98%               | 1.85%               |
</details>

Source: Central banks, company data, UBS estimates. Note: JP, AU, KR, SG, HK, TW banks are classified as DM banks above, while IN, CN, ID, PH, TH, MY, VN banks are classified as EM banks.

Figure 4: Cost-to-income ratios for both DM and EM banks have declined over the past 20y   
![](images/41335b38653df0537e530173b9e599f01e33a3cd94e396fa5a08c6132a444a3a.jpg)

<details>
<summary>line</summary>

| Year | Average (Asia) | Average (Asia - DM) | Average (Asia - EM) |
|------|----------------|---------------------|---------------------|
| 2002 | 51.5%          | 49.0%               | 56.0%               |
| 2003 | 49.0%          | 47.0%               | 54.0%               |
| 2004 | 48.0%          | 44.0%               | 52.0%               |
| 2005 | 50.0%          | 46.0%               | 54.0%               |
| 2006 | 50.5%          | 47.5%               | 53.5%               |
| 2007 | 51.0%          | 49.0%               | 53.0%               |
| 2008 | 51.5%          | 50.5%               | 52.5%               |
| 2009 | 51.0%          | 48.5%               | 51.5%               |
| 2010 | 50.5%          | 49.5%               | 50.5%               |
| 2011 | 50.0%          | 50.5%               | 49.5%               |
| 2012 | 49.5%          | 50.5%               | 49.0%               |
| 2013 | 49.5%          | 50.5%               | 48.5%               |
| 2014 | 49.5%          | 51.5%               | 49.0%               |
| 2015 | 50.5%          | 52.0%               | 49.5%               |
| 2016 | 49.5%          | 51.0%               | 48.5%               |
| 2017 | 49.0%          | 50.5%               | 47.5%               |
| 2018 | 48.5%          | 50.0%               | 47.0%               |
| 2019 | 48.5%          | 51.0%               | 46.5%               |
| 2020 | 49.0%          | 52.5%               | 46.0%               |
| 2021 | 48.5%          | 51.5%               | 46.0%               |
| 2022 | 47.0%          | 49.0%               | 44.5%               |
| 2023 | 46.0%          | 46.5%               | 44.0%               |
| 2024 | 46.5%          | 47.5%               | 43.5%               |
| 2025 | 46.5%          | 49.0%               | 43.5%               |
</details>

Source: Central banks, company data, UBS estimates. Note: JP, AU, KR, SG, HK, TW banks are classified as DM banks above, while IN, CN, ID, PH, TH, MY, VN banks are classified as EM banks.

# 3. What drove past cost improvements?

The sources of past efficiency gains suggest many traditional cost levers are now approaching maturity.

Staff costs account for just under half of total operating expenses, and while they have been a key driver of cost reduction in emerging markets, their contribution has been more limited in developed markets.

Other operating expenses, including branch, administrative and IT costs, have been the primary source of efficiency gains for developed market banks, reflecting consolidation and branch rationalisation.

While branch networks have been significantly reduced across most Asian markets in recent years, total bank headcount has, interestingly, continued to rise in many countries, likely driven by a shift away from customer-facing roles toward technology, data and back-office functions.

At the same time, technology spending has continued to increase, with Asian banks now spending around 4–5% of revenues on technology on average, and materially more in markets such as Singapore, Australia and Taiwan.

Furthermore, past tech investments have generally not resulted in a big improvement in operational efficiency for the sector. Many banks that increased their tech spend over the past 5 years are yet to see any reduction in their total opex to assets.

Figure 5: Staff opex/ assets ratio declined by 15bps over the past 20y for Asian banks   
![](images/6838b4bfda3b883c3a59625b79a1f536ec2b2d937a16deb0e2568b7cc29ec2f1.jpg)

<details>
<summary>line</summary>

| Year | Average (Asia) | Average (Asia - DM) | Average (Asia - EM) |
|------|----------------|---------------------|---------------------|
| 2002 | 0.78%          | 0.60%               | 1.05%               |
| 2003 | 0.85%          | 0.58%               | 1.15%               |
| 2004 | 0.81%          | 0.56%               | 1.08%               |
| 2005 | 0.81%          | 0.55%               | 1.07%               |
| 2006 | 0.82%          | 0.56%               | 1.09%               |
| 2007 | 0.84%          | 0.57%               | 1.11%               |
| 2008 | 0.78%          | 0.50%               | 1.08%               |
| 2009 | 0.76%          | 0.52%               | 1.05%               |
| 2010 | 0.79%          | 0.53%               | 1.04%               |
| 2011 | 0.79%          | 0.54%               | 1.03%               |
| 2012 | 0.78%          | 0.53%               | 1.02%               |
| 2013 | 0.76%          | 0.52%               | 1.01%               |
| 2014 | 0.75%          | 0.51%               | 1.00%               |
| 2015 | 0.74%          | 0.50%               | 0.99%               |
| 2016 | 0.73%          | 0.49%               | 0.98%               |
| 2017 | 0.73%          | 0.48%               | 0.97%               |
| 2018 | 0.72%          | 0.47%               | 0.96%               |
| 2019 | 0.71%        

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/3a744877329e96aff896934c16027932ff01c791600b16eeffbe8953f1391bf5.jpg)
"""
