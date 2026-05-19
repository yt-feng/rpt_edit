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
# Asia Fund Manager Survey

# From growth concerns to AI conviction

# BofA April Asia Fund Manager Survey

Spotlight: The MSCI Asia Pacific Index has rallied 17.6% since its March low to reach record highs, driven by strong optimism in AI-exposed markets such as Japan, Taiwan, and Korea (the top three preferred markets among FMS investors). Taiwan is viewed as the clearest beneficiary of the next phase of the AI cycle. Meanwhile, concerns around energy security have eased materially MoM (from 91% to 52%).

Macro: Growth expectations remain negative but have improved significantly MoM (from net 55% to 5%). Net 81% now expect higher inflation. 67% of investors see the next BoJ rate hike as most likely in Jun, consistent with our economist's view (see Japan Watch note).

Expected Returns: Expected 12-month returns for APAC ex-Japan equities have rebounded sharply to 6.0%, while expected returns for Japan equities rise to 6.9% (all-time high). Notably, fewer investors think AI-driven equity upside is priced in or over-valued.

Themes: Within China, AI/semis remain the top investor priorities, in line with our recent China Conference takeaways (see report: Equity Strategy – China: China Conference feedback, 15 May 2026), while Internet has seen improving preference MoM. In Japan, earnings are cited by the largest share of investors (38%) as the primary driver of Japan equity prospects. Net 71% (up from 14% two months ago) expect a stronger semis cycle, putting it in the 91st percentile of history (see US Semiconductors: AI 2030 report).

Positioning: Japan, Taiwan & Korea have further consolidated their leadership in investor preference. India is viewed as the first market to be reduced across APAC if global growth weakens further. Within APAC ex-Japan, May saw rotation out of Energy and Consumer Staples into Consumer Discretionary (ex Retailing), Real Estate, and Software.

Exhibit 1: Taiwan is seen as the clearest beneficiary of the next phase of the AI cycle   
FMS views on beneficiaries of the next phase of the AI cycle   
![](images/dfa933807a1484aaa788edfd0539363bd628744c7784a98ee91b0e6f9ba2706a.jpg)

<details>
<summary>bar</summary>

| Country | Percentage (%) |
| :--- | :--- |
| Taiwan | 43 |
| Korea | 29 |
| Japan | 14 |
| US | 10 |
| China | 0 |
</details>

Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above

BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 16 to 18.

12975729

# 19 May 2026

Equity Strategy

Asia Pacific

BofA

Data

Analytics

![](images/133776dd8c2c30c7afe58c722b5fa3a3a0b2e47238415d1334caa63f4b23d3c8.jpg)

Kaspar Lam >>

Research Analyst

BofA (Hong Kong)

kaspar.lam@bofa.com

Masashi Akutsu >>

Strategist

BofAS Japan

masashi.akutsu@bofa.com

Winnie Wu >>

Research Analyst

BofA (Hong Kong)

winnie.wu@bofa.com

Amish Shah, CFA >>

Research Analyst

BofAS India

shah.amish@bofa.com

FMS: Fund Manager Survey

APAC: Asia Pacific

# Notes to readers

A total of 200 panelists with \$517bn AUM participated in the May survey. 170 participants with \$461bn AUM responded to the Global FMS questions and 92 participants with \$209bn AUM responded to the Regional FMS questions.

Survey period: 8 May – 14 May 2026

# How to join the FMS panel

Investors/clients are encouraged to sign up to participate in the Survey. This can be done by contacting Michael Hartnett or your BofA sales representative.

Participants in the survey receive the full set of results for the months in which they participate.

BoJ – Bank of Japan

# Macro

Exhibit 2: Growth expectations stay in negative territory, but have eased significantly compared to last month   
Net % expecting a stronger Global / APAC ex-Japan economy   
![](images/4cdeaa414dcd9de06bf96e11832d7ab20adb95f5d578c7a787908d2191a4c69f.jpg)

<details>
<summary>line</summary>

| Year | Asia Pacific ex-Japan | Global |
|------|------------------------|--------|
| 97   | ~35                    | ~40    |
| 99   | ~95                    | ~45    |
| 01   | ~-80                   | ~-60   |
| 03   | ~100                   | ~85    |
| 05   | ~-40                   | ~-20   |
| 07   | ~-20                   | ~-40   |
| 09   | ~-100                  | ~-60   |
| 11   | ~-20                   | ~-40   |
| 13   | ~-60                   | ~-20   |
| 15   | ~-40                   | ~-20   |
| 17   | ~-80                   | ~-40   |
| 19   | ~-60                   | ~-20   |
| 21   | ~100                   | ~90    |
| 23   | ~-80                   | ~-60   |
| 25   | ~-60                   | ~-40   |
</details>

Source: BofA Global & Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 3: Inflation expectations remain elevated, with a net 81% of respondents anticipating higher inflation over the next 12 months, the highest level since Apr 2022   
Net % expecting higher inflation in Asia Pacific ex-Japan in the next 12 months   
![](images/9ea4a2af6a7f38327f2f7410ad3c1d42ba3eb824d0aed525f0b898143249a922.jpg)

<details>
<summary>line</summary>

| Year | Net % expecting higher inflation |
| ---- | -------------------------------- |
| 2026 | 81%                            |
</details>

Source: BofA Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 4: Corporate profit expectations have swung sharply, with a net 33% now expecting stronger profits (from net 45% expecting weaker)   
Net % expecting better corporate profits in Asia Pacific ex-Japan in the next 12 months   
![](images/fadb518b76e68b93b0cd93b6e6dfe7beb680b61d9331496c663c88461a337e82.jpg)

<details>
<summary>line</summary>

| Month | Net % expecting better profits |
|-------|--------------------------------|
| May'26 | 33%                            |
</details>

Source: BofA Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 5: Concern that APAC ex-Japan earnings estimates are too high eased slightly in May
Net % deeming consensus EPS estimates for the coming year as high   
![](images/ce0eec7a8c58f5855f5c97bdc6985d1c499cb547202458b37afb64a8d9d7e070.jpg)

<details>
<summary>line</summary>

| Year | Net % deeming consensus EPS estimates for the coming year as high | Asia Pac ex-Japan 1m ERR, inverted, RHS |
|------|------------------------------------------------------------------------|------------------------------------------|
| 08   | ~95%                                                                   | ~0.4                                     |
| 10   | ~-30%                                                                  | ~0.6                                     |
| 12   | ~80%                                                                   | ~0.5                                     |
| 14   | ~50%                                                                   | ~0.4                                     |
| 16   | ~100%                                                                  | ~0.3                                     |
| 18   | ~40%                                                                   | ~0.2                                     |
| 20   | ~95%                                                                   | ~0.1                                     |
| 22   | ~70%                                                                   | ~0.3                                     |
| 24   | ~30%                                                                   | ~0.4                                     |
| 26   | ~20%                                                                   | ~0.5                                     |
</details>

Source: BofA Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 6: Energy security concerns have declined materially MoM (from 91% to 52%)   
How concerned are you about energy security risks for APAC region in current geopolitical environment?   
![](images/df032764c6452f16fd08073d396dbb3dc5e114b1d4c68072864c99abc2a841f1.jpg)

<details>
<summary>bar</summary>

| Concern Level              | May-26 | Apr-26 |
| -------------------------- | ------ | ------ |
| Extremely concerned        | 5%     | 19%    |
| Highly concerned           | 48%    | 73%    |
| Slightly to moderately concerned | 48%    | 10%    |
| Not concerned              | 0%     | 0%     |
</details>

Source: BofA Asia Fund Manager Survey. Notes: Votes for ‘Don’t know’ are not shown above.   
BofA GLOBAL RESEARCH

Exhibit 7: China growth sentiment remains negative, but improved vs. last month   
Net % expecting a stronger Chinese economy in the next 12 months   
![](images/8eb2c279602fa317d69d83a7094103e9daa9987724ea980deea4ff83d2275d08.jpg)

<details>
<summary>line</summary>

| Date   | Value |
|--------|-------|
| May'26 | -14%  |
</details>

Source: BofA Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 8: Japan growth expectations bounce back strongly in May, though still below the highs seen earlier in the year   
Net % expecting a stronger Japanese economy over the next 12 months   
![](images/e1db4933a261d300aab4683728208428b7e01804a6584bd9149bfe51e0bf8ecf.jpg)

<details>
<summary>line</summary>

| Date   | Value |
|--------|-------|
| May'26 | 38%   |
</details>

Source: BofA Asia Fund Manager Survey. Notes: Votes for 'Don't know' are not shown above.   
BofA GLOBAL RESEARCH

# Exhibit 9: Investors expect the next rate hike to be most likely in June

When do you think the BOJ next rate hike will be?

When do you think the BOJ next rate hike will be?   
![](images/2fa62a699846ebebc5645af85375612edc1fe163e3418f5e109f62a31c97b79b.jpg)

<details>
<summary>bar</summary>

| Period | Percentage (%) |
| :--- | :--- |
| Jun 2026 | 67 |
| Jul 2026 | 10 |
| Sep 2026 | 14 |
| Oct 2026 or later | 10 |
</details>

Source: BofA Asia Fund Manager   
BofA GLOBAL RESEARCH

# Expected Returns and Valuations

Exhibit 10: Investor optimism picked up again after the April dip, with expected returns moving back above average   
FMS views on expected upside for Asia Pac ex-Japan equities over the next 12 months   
![](images/0a6a492a6bf33b86ce4ae3ebc9a29d3a49a5c0281b1d09f40f329c00b8b334ab.jpg)

<details>
<summary>area</summary>

| Date   | Expected upside for APAC ex-Japan equities over the next 12 months |
|--------|------------------------------------------------------------------|
| May'26 | 6.0%                                                             |
</details>

Source: BofA Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 11: Japan return expectations have climbed to an all-time high of 6.9%   
FMS views on expected upside for Japan equities over the next 12 months   
![](images/f3dacb6445fdd316d1a2360f160237e23645db54aa17849aead1db70dcabb104.jpg)

<details>
<summary>line</summary>

| Date   | Expected returns for Japan equities over the next 12 months (%) |
|--------|---------------------------------------------------------------|
| May'26 | 6.9%                                                          |
</details>

Source: BofA Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 12: Sentiment is tilted toward undervaluation   
Net % saying Asia Pacific ex-Japan equities are overvalued   
![](images/74f1ef12f5233ab4a99d3bd08e19c81a58c7b57b50c5f6351ec3163d724d2f4a.jpg)

<details>
<summary>line</summary>

| Year | Value |
| ---- | ----- |
| May'26 | -14% |
</details>

Source: BofA Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 13: Investors appear more constructive on AI upside in May, with fewer viewing AI as fully or broadly fairly priced in   
How much of the positive AI impact on equities is already reflected in the price?   
![](images/0932d2f0841512572f443ca88e7916f192cad1dce5e59a98b896cc2b76ee64fa.jpg)

<details>
<summary>bar</summary>

| Pricing Status | May-26 (%) | Apr-26 (%) |
|---|---|---|
| More than fully priced in | 5 | 14 |
| Broadly fairly priced | 33 | 41 |
| Partially priced in | 52 | 28 |
| Mostly not priced in | 5 | 4 |
</details>

Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above   
BofA GLOBAL RESEARCH

# Themes

Exhibit 14: Within China, AI/semis and buybacks/dividend remain key investor priorities, while Internet has seen improving preference vs. last month   
FMS views on TWO most favorite themes in China   
![](images/d624996f1f49f597b22ad63eca4ec34318ae02d32beea047cee4ada68e2d9cb9.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
| :--- | :--- |
| AI / Semiconductors | 57 |
| Buybacks/Dividend | 19 |
| Internet | 19 |
| SOEs | 10 |
| Healthcare | 10 |
| Cyclicals | 10 |
| Anti-involution | 5 |
| Green economy | 5 |
| Others | 0 |
| Travel & leisure | 0 |
</details>

Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above   
BofA GLOBAL RESEARCH

Exhibit 15: Earnings have now become the primary driver of Japan equity prospects   
FMS views on the themes that hold the key for Japan equities in the near-to-medium term   
Key themes for Japan equities in the near-to-medium term   
![](images/5ab102c5c477b7b0e8d9cc7b415a6ad711fb626bb6016a57d2e9cc79eda9adf7.jpg)

<details>
<summary>bar</summary>

| Category | Apr-26 (%) | May-26 (%) |
|---|---|---|
| Earnings | 18 | 38 |
| Policy normalization by the BoJ | 23 | 19 |
| Corporate governance reforms & Japan Exchange Group (JPX) initiatives | 23 | 19 |
| Currency (JPY) moves | 9 | 14 |
| Others | 5 | 5 |
</details>

Source: BofA Asia Fund Manager Survey. Notes: Votes for 'Don't know' are not shown above   
BofA GLOBAL RESEARCH

Exhibit 16: Investor views on the Korea/Taiwan semis cycle strengthened materially in last 2 months, putting it in the 91st percentile of history   
FMS views on the semis cycle (Korea/Taiwan exports growth) over the next 12 months   
![](images/cd7de9cb4d3621038bca5ba193f992e5add1a26f4de13a7d06a2149b474f1d72.jpg)

<details>
<summary>line</summary>

| Date   | Value |
|--------|-------|
| May-2026 | 71%   |
</details>

Source: BofA Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 17: Investors turned more positive on Korea's ‘Corporate Value Program’, post the election FMS views on the efficacy of the ‘Corporate Value-Up Program’ in Korea   
FMS view of the efficacy of the ‘Corporate Value-Up Program’ in Korea   
![](images/157120e31d75983eea41207bbbba5058fe056dd3ae6d522a75b6614132c52923.jpg)

<details>
<summary>line</summary>

| Date   | Strongly positive impact (like in Japan) | Moderately positive impact | No significant impact |
|--------|------------------------------------------|-----------------------------|------------------------|
| Mar-24 | 5%                                       | 57%                         | 13%                    |
| Jun-24 | 0%                                       | 47%                         | 16%                    |
| Sep-24 | 10%                                      | 40%                         | 39%                    |
| Dec-24 | 6%                                       | 29%                         | 35%                    |
| Mar-25 | 8%                                       | 32%                         | 27%                    |
| Jun-25 | 3%                                       | 35%                         | 29%                    |
| Sep-25 | 15%                                      | 50%                         | 10%                    |
| Dec-25 | 18%                                      | 47%                         | 10%                    |
| Mar-26 | 24%                                      | 60%                         | 9%                     |
</details>

Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above   
BofA GLOBAL RESEARCH

Exhibit 18: The absence of a clear AI play is cited as the primary concern for the Indian market   
What is your key concern for Indian market?   
![](images/fbc4142e3a685076ca9e46585dbd80d1b9fd22de8dcc779b13a6ebea13a71158.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| No AI play | 29 |
| Depreciating currency | 14 |
| Weak growth | 10 |
| Lack of reforms | 10 |
| High valuations | 5 |
</details>

Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above   
BofA GLOBAL RESEARCH

# Positioning

Exhibit 19: Japan, Taiwan and Korea consolidated their leadership even further, reinforcing a more concentrated North Asia overweight   
Asia Pacific market sentiment: Net % overweight   
Asia Pacific market sentiment: Net % overweight (% saying overweight - % saying underweight)   
![](images/6991f3a700b4389a905ce2d7fa8ec7a22c4a7f3885d8b39310366451253863fd.jpg)

<details>
<summary>bar</summary>

| Country | Value |
| :--- | :--- |
| Japan | 62 |
| Taiwan | 43 |
| South Korea | 33 |
| Australia | 5 |
| New Zealand | -5 |
| Singapore | -5 |
| China | -5 |
| Malaysia | -10 |
| Thailand | -19 |
| Indonesia | -24 |
| Philippines | -29 |
| India | -38 |
Underweight (red arrow) < Lowerweight (green arrow) Overweight (green arrow)
</details>

Source: BofA Asia Fund Manager Survey   
BofA GLOBAL RESEARCH

Exhibit 20: India is viewed as the first one to be reduced across APAC if global growth deteriorates further, in line with its largest underweight positioning   
If global growth weakens further, you would first reduce exposure to...?   
![](images/f17f58453a3fd5ca776690963be26eabe37f42f75a59db581c71f9d1a5f60f3b.jpg)

<details>
<summary>bar</summary>

| Country/Region | Percentage (%) |
| :--- | :--- |
| India | 24 |
| China | 19 |
| Korea | 14 |
| ASEAN | 14 |
| Japan | 10 |
| Taiwan | 0 |
| Australia | 0 |
</details>

Source: BofA Asia Fund Manager Survey. Note: Votes for ‘Don't know / Not applicable’ are not shown above   
BofA GLOBAL RESEARCH

Exhibit 21: FMS investors most overweight in Semis and Tech Hardware, while Materials and Software saw increased positioning

Asia Pacif

[中间内容因长度限制已省略]

ch information is distributed simultaneously to internal and client websites and other portals by BofA and is not publicly-available material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
