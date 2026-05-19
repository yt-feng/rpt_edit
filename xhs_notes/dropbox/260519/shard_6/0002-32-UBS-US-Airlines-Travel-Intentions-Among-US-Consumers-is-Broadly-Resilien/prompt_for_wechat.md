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
# US Airlines

# Travel Intentions Among US Consumers is Broadly Resilient - Only Slight YoY Volume Moderation Per UBS Survey

# US Consumer Travel Intentions moderated only slightly despite the surge in fuel prices

In this note, we present the key findings from US airlines' perspective from the 12th UBS Evidence Lab travel intentions survey (> Access Dataset), which was undertaken during March and early April of 2026 (see here for our global survey note). The key takeaway was that intentions among US consumers to undertake leisure and business travel over the next 12 months remains high, but moderated slightly year-over-year with leisure travel intentions down -30 bps YoY to 82.8%. Intentions for business travel moderated to 32.6% from 35.0% in Mar '25. Still, both leisure and business travel intentions are up relative to 2-yrs ago. With respect to spend, the survey results show that significantly more US consumers expect to increase spend in the next 12 months than spend less on their trips - a trend that's consistent with last year's survey.

\- We believe the year-over-year moderation in travel intentions this year was likely due to higher jet fuel and other geopolitical concerns. Importantly, despite the backdrop, travel intentions among US consumers was still above the March'24 levels and is close to the highs over the past 9 years. We view this a sign that travel remains a priority for US consumers. This is being manifested in recent airline commentary that suggests demand remains strong despite fare increases with limited impact on load factors.

# Spending intentions for leisure travel is strong, but there are some puts & takes

Specifically, around 48% of respondents expect to increase spending on leisure travel in the next 12 months vs. 49% in the Mar'25 survey. Further, 23% expect to decrease spending on leisure travel or not spend at all, down vs. 24% last year. That said, the rate of increase might be slowing as those expecting to increase spend by up to 10% increased 120 bps YoY, but those planning on spending 11-40% more decreased -150 bps YoY.

# What are the key factors driving purchase behavior for leisure air travel in the US?

Price is still the most important consideration with 77% of respondents citing price as the key factor when purchasing airline tickets for leisure purposes. Destination (55%) and airline brand (49%) were also important elements.

- Airline brand was meaningfully more important than 3 years ago (+600 bps) as was seat class (+900 bps vs. 3 years ago). This should bode well for the larger airlines with a stronger loyalty/premium offering including DAL & UAL and also for AAL and ALK. More on figures 9-10.   
- With respect to travel to locations outside of North America, intentions to travel to Europe remained high among US consumers even as it moderated YoY. Specifically, 36% of US respondents cited plans to travel to Europe for leisure purposes in March'26, down -600 bps YoY. Still, its up 350 bps from 2-yrs ago and also up meaningfully from 2019's 26.2% reading. Overall, we see DAL/UAL benefitting from continued propensity for Transatlantic travel. Separately, intentions to travel to the Caribbean increased 470 bps YoY to 23.4%. Details in figure 11-12.

How are travel intentions among consumers for the largest US airlines?

# Equities

Americas

Airlines

Atul Maheswari

Analyst

atul.maheswari@ubs.com

+1-212-713 4103

Jarrod Castle, CFA

Analyst

jarrod.castle@ubs.com

+44-20-7568 8883

Thomas Wadewitz

Analyst

thomas.wadewitz@ubs.com

+1-212-713 6116

In the survey, we also asked respondents whether they intend to book more, less, or about the same at various US carriers over the next 12 months. Most airlines witnessed a YoY moderation in those willing to fly more while witnessing a corresponding increase in those willing to fly "about the same" at the airline. In total, those willing to spend more or about the same increased 100 bps for DAL to 57% and was down -100 bps YoY for UAL to 59%. This metric was flattish YoY for AAL at 58% and increased 200 bps YoY for LUV to 48% (but was still below Mar'24 of 53%). Details in figures 13-16.

# Around 12% of US respondents cited use of AI assistants for travel booking

From the total base of US respondents in our survey, around 44% of them said they trust these AI tools (Grok, Open AI, Gemini etc.) a fair amount. Another 17% said, they trust these tools a great deal. Separately, 31% said, they do not trust these tools at all or "do not trust them very much".

# SUMMARY

# UBS Evidence Lab Consumer survey on travel intentions

This is the 12th wave of the Europe US Travel Consumer Survey. UBS Evidence Lab conducted an online survey of 6,877 consumers across worldwide (1,754 in the U.S.) between the 3rd of March to the 6th of April 2026. The key takeaways from a US airlines perspective included:

1) Travel Intentions in the US leveled off relative to last year. In the US, Intentions to travel for leisure moderated slightly to 82.8% in Mar'26 relative to 83.1 in Mar'25. Still, it remains modestly above 2-yrs ago. Intentions for business travel in the next 12 months among US based respondents decreased to 32.6% in March '26, down from 35% in March'25, but up from 31.7% in Mar'24.   
2) Around half of US consumers expect to spend more year-over-year. Around 48% of respondents expect to increase spending on leisure travel for the next 12 months vs. 49% last year. Further, 23% expect to decrease spending on leisure travel or not spend at all vs. 24% last year. Still, there were some mixed trends as the rate of increase might be slowing with those expecting to increase spend by up to 10% increased 120 bps, but those planning on spending 11-40% more decreased -150 bps. Spending on business travel increased with 36% planing on increasing spending, up 200 bps YoY. Those planning on spending nothing on business travel moderated by -300 bps YoY.   
3) Price remains a key factor when purchasing airline tickets for leisure travel. For leisure flying, around 77% of US respondents answered that price is the important factor. Destination (55%) and airline brand (49%) were also important elements. Airline brand was meaningfully more important than 3 years ago (+600 bps) as was seat class (+900 bps vs. 3 years ago). This should bode well for the larger airlines with a stronger loyalty/premium offering.   
4) Intentions to travel to Europe moderated, but still remains well above pre-pandemic levels among US consumers per the survey. In the latest survey, intentions for leisure travel to Europe in the next 12 months was cited by 36% of US respondents, down -600 bps YoY, but still up 350 bps compared to Mar'24. Plus, it remains well above the sub-30% levels from pre-pandemic periods.   
5) Intentions to fly more or about the same was broadly stable across the larger airlines year-over-year. Specifically, percentage of respondents intending to travel more or about the same over the next 12 months was at 57% for DAL (up from 56% in March'25). For UAL, it was at 59%, down from 60% last year. Those planning on traveling more or about the same with AAL remained stable at 58% while for LUV, it increased 200 bps to 48%. However, it remained below Mar'24 level of 53%.

# Survey results in more details below -

Specifically, the likelihood of leisure travel in the next 12 months among US based respondents is slightly lower at 82.8% in March '26 relative to 83.1% in March '25. Those that noted that they are very likely to take a leisure trip in the next 12 months increased to 62.1%, up +20 bps YoY.

Figure 1: Likelihood of leisure travel in the next 12 months - US Passengers   
![](images/ca0951c99ec53832b889d03b4bdbcd00c0215b768cbbf309e9f6a9de93dc5e6c.jpg)

<details>
<summary>bar</summary>

| Month    | Very likely | Somewhat likely | Not sure yet | Somewhat unlikely | Very unlikely |
|----------|-------------|-----------------|--------------|--------------------|---------------|
| Aug'18   | 60%         | 20%             | 13%          | 3%                 | 5%            |
| Aug'19   | 57%         | 19%             | 13%          | 5%                 | 5%            |
| July'20  | 33%         | 24%             | 30%          | 5%                 | 7%            |
| Mar'21   | 46%         | 24%             | 20%          | 4%                 | 5%            |
| Mar'22   | 61%         | 21%             | 11%          | 3%                 | 4%            |
| Mar'23   | 61%         | 19%             | 11%          | 3%                 | 4%            |
| Mar'24   | 61%         | 21%             | 11%          | 3%                 | 4%            |
| Mar'25   | 61.9%       | 21.3%           | 10%          | 3%                 | 4%            |
| Mar'26   | 62.1%       | 20.7%           | 11%          | 3%                 | 4%            |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Figure 2: Likelihood of leisure travel in the next 12 months - US Passengers   
![](images/ef844e6081aa9ba70bb9ee1e665ffe367eb03e9b4ec453564063eb4a7bc7a965.jpg)

<details>
<summary>line</summary>

| Month    | NET: Likely | NET: Unlikely |
| -------- | ----------- | ------------- |
| Aug'18   | 78%         | 8%            |
| Aug'19   | 75%         | 10%           |
| July'20  | 55%         | 12%           |
| Mar'21   | 70%         | 8%            |
| Mar'22   | 80%         | 6%            |
| Mar'23   | 82%         | 5%            |
| Mar'24   | 82%         | 5%            |
| Mar'25   | 83.1%       | 6.6%          |
| Mar'26   | 82.8%       | 6.3%          |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Further, the survey results showed that likelihood for business travel has moderated year-over-year, but remains above 2024 survey levels. Specifically, the likelihood of business travel in the next 12 months among US based respondents decreased to 32.6% in March '26, down from 35% in March'25, but up from 31.7% in Mar'24. We also note respondents that are very likely to take a business trip in the next 12 months decreased to 19.8%, down -140 bps YoY. Still, it was up 30 bps vs. March'24.

Figure 3: Likelihood of business travel in the next 12 months - US Passengers   
![](images/721dae8b5341731772f2676db6734dbe536b4e8c4fb689e3e4ef862f6c242dbc.jpg)

<details>
<summary>bar</summary>

| Month   | Very likely | Somewhat likely | Not sure yet | Somewhat unlikely | Very unlikely |
|---------|-------------|-----------------|--------------|--------------------|---------------|
| Aug'18  | 19%         | 12%             | 14%          | 8%                 | 46%           |
| Aug'19  | 19%         | 11%             | 15%          | 8%                 | 46%           |
| July'20 | 14%         | 13%             | 17%          | 8%                 | 46%           |
| Mar'21  | 19%         | 16%             | 13%          | 7%                 | 43%           |
| Mar'22  | 23%         | 17%             | 11%          | 6%                 | 41%           |
| Mar'23  | 24%         | 15%             | 9%           | 7%                 | 43%           |
| Mar'24  | 19%         | 12%             | 12%          | 8%                 | 47%           |
| Mar'25  | 21.2%       | 13%             | 12%          | 7%                 | 45.3%         |
| Mar'26  | 19.8%       | 13%             | 13%          | 8%                 | 45.0%         |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Figure 4: Likelihood of business travel in the next 12 months - US Passengers   
![](images/044274c10945fd0a999390bb12aa90cb4c689187b01ec9594d615340aaa3cf25.jpg)

<details>
<summary>line</summary>

| Month    | NET: Likely | NET: Unlikely |
| -------- | ----------- | ------------- |
| Aug'18   | 31.7%       | 55.8%         |
| Aug'19   | 30.0%       | 54.0%         |
| July'20  | 27.0%       | 54.0%         |
| Mar'21   | 35.0%       | 50.0%         |
| Mar'22   | 41.0%       | 47.0%         |
| Mar'23   | 39.0%       | 51.0%         |
| Mar'24   | 31.7%       | 55.8%         |
| Mar'25   | 35.0%       | 52.7%         |
| Mar'26   | 32.6%       | 53.4%         |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Spending intentions - With respect to spending intentions on leisure travel in the next 12 months, there were mixed results from the survey. Notably, 4% of respondents highlighted plans to increase leisure travel spend by more than 40%. This compares to 5% citing plans to increase leisure travel spend by more than 40% in Mar '25. Around 22% of respondents plans to increase leisure spending by up to 10% (vs. 21% in March'25 and 17% in March'24). These increases was partially offset by those noting an 11% to 40% increase (22% in Mar '26 vs. 23% in Mar '25). We believe such results may be interpreted by a partial shift of respondents from up 11% to 40% group to the cohort to those who are planning to increase spending by up to 10%.

Figure 5: Expected Increase/decrease in spending on leisure travel - US Passengers   
![](images/760584cdb21104a26eed3073b216d87ca8897d1f5cf54ba72ee2072bfc1f4ae6.jpg)

<details>
<summary>bar</summary>

| Category | Mar'23 | Mar'24 | Mar'25 | Mar'26 |
| -------- | ------ | ------ | ------ | ------ |
| Decrease by more than -40% | 5% | 2% | 3% | 3% |
| Decrease by -11% to -40% | 9% | 6% | 6% | 6% |
| Decrease by upto -10% | 2% | 3% | 5% | 4% |
| No Change | 26% | 30% | 28% | 29% |
| Increase by Up to 10% | 13% | 17% | 21% | 22% |
| Increase by 11% to 40% | 26% | 26% | 23% | 22% |
| Increase by more than 40% | 7% | 4% | 5% | 4% |
| Will Spend Nothing | 11% | 12% | 10% | 11% |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Further, the UBS Evidence Lab survey shows positive trend in the rate of increase in spending among those expecting to take a business trip in the next 12 months. The group planning 11% to 40% spending increase has grown to 17% in March'26 (from 16% in March'25). Plus, 27% of respondents are planning to spend nothing in next 12 months, down from 30% in March'25 and 37% in March'24. However, those noting >40% spending increase are now at 3% (vs. 5% in March'25).

Figure 6: Expected increase/decrease in spending on business air travel - US Passengers   
![](images/2c7fa07a24a1c708c145ecd541dc6f3bb147058779f281d84eefba0c2fc45858.jpg)

<details>
<summary>bar</summary>

| Intentions to Spend on Business Travel | March'23 (%) | March'24 (%) | March'25 (%) | March'26 (%) |
|---|---|---|---|---|
| Decrease by more than -40% | 3 | 3 | 3 | 2 |
| Decrease by -11% to -40% | 5 | 5 | 5 | 6 |
| Decrease by up to -10% | 2 | 2 | 4 | 5 |
| No Change | 16 | 19 | 24 | 25 |
| Increase by Up to 10% | 8 | 13 | 13 | 16 |
| Increase by 11% to 40% | 18 | 17 | 16 | 17 |
| Increase by more than 40% | 3 | 4 | 5 | 3 |
| Will Spend Nothing | 45 | 37 | 30 | 27 |
Intentions to spend on business travel is positive. Only 27% of US respondents expect to spend nothing (vs. 30% in Mar'25 and 37% in Mar'24).
</details>

Source: UBS Evidence Lab (> Access Dataset)

Number of flights consumers are planning to take - We also used the results of the survey to showcase how many flights consumers were planning to take in both leisure and business category. As can be seen in figure below, the group of respondents intending to take 1 or 2 leisure related flights declined, but those intending to take 3-6 flights over the next 12 months increased. Last year, around \~47% planned on taking 1-2 flights while in this year, the number moderated to 46%. Importantly, the percentage of respondents expecting to take 3-6 flights increased from 33% to 35%. Those planning on 7-10 flights, and 10+ flights decreased by -60 bps and -130 bps respectively.

When looking at number of business related flights, we notice a mix of respondents which are going to take 1 or 2 flights in next 12 months - with respondents in the 1 category seeing a 70 bps increase from March'25 to 10.4% in March'26 and those in the latter category see a 170 bps decrease YoY . There was a decrease in those planning on taking 3-6 flights and 7-10 flights additionally, but an increase among those with intentions to take 11+ flights for business purposes in the next 12 months.

Figure 7: Number of flights intending to take in next 12 months (Leisure) - US Passengers   
![](images/2b07b3df2e0d0509c6e1b0681fb5367906df1df8a98efc8e91846b67389b2995.jpg)

<details>
<summary>bar</summary>

| Category   | March'24 | March'25 | March'26 |
| ---------- | -------- | -------- | -------- |
| 1          | 12%      | 10%      | 10%      |
| 2          | 39%      | 37%      | 36%      |
| 3 to 6     | 29%      | 33%      | 35%      |
| 7 to 10    | 6%       | 7%       | 6%       |
| 11+        | 2%       | 4%       | 2%       |
| Don't know | 11%      | 10%      | 10%      |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Figure 8: Number of flights intending to take in next 12 months (Business) - US Passengers   
![](images/a0c0eb318ca71e8ce0cc2ed5dcf4dfa7ecf3f4d2e77166f5bf29299f51020dd6.jpg)

<details>
<summary>bar</summary>

| Category   | March'24 | March'25 | March'26 |
| ---------- | -------- | -------- | -------- |
| 1          | 9%       | 10%      | 10%      |
| 2          | 34%      | 38%      | 36%      |
| 3 to 6     | 29%      | 24%      | 23%      |
| 7 to 10    | 7%       | 10%      | 6%       |
| 11+        | 5%       | 6%       | 8%       |
| Don't know | 17%      | 13%      | 16%      |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Factors Influencing decision on purchasing flight tickets - In the survey, we also asked US respondents about factors influencing their decision when buying a flight ticket for leisure purposes. Around 77% of respondents answered that price is the important factor. Unsurprisingly, destination (55%) and airline brand (49%) were also significantly important elements. When looking at other factors included in Figure 9 below, cabin cleanliness saw a positive bump between March'25 (19%) to March'26 (\~21%). Several other factors saw slight declines from the same time a year ago. Interestingly, safety ratings significance saw decline from 36% to 33% in the same time.

Figure 9: Factors important in influencing decision when buying a flight ticket for leisure purposes - US Passengers   
![](images/552bec75e932b06af9800e0b4e227ad52e508ed7176559a1be6d106021c3dbf7.jpg)

<details>
<summary>bar</summary>

| Factor | March '23 | March '24 | March '25 | March '26 |
| --- | --- | --- | --- | --- |
| Price | 68.0% | 75.0% | 77.0% | 77.0% |
| Safety ratings | 28.0% | 35.0% | 35.0% | 33.1% |
| Cabin cleanliness | 22.0% | 22.0% | 18.0% | 20.6% |
| Airline brand | 43.0% | 49.0% | 50.0% | 49.4% |
| Destination | 50.0% | 55.0% | 55

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/639ba32a7ddec6e61d4911d6dc9e019ba85ff19f893a5a941de24a7fc06d3053.jpg)
"""
