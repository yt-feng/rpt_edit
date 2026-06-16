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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`美国银行`。标题格式建议：`# 美国银行：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份美国银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Asia Fund Manager Survey

# Tech Hardware rises; Indonesia slips

## BofA June Asia Fund Manager Survey

Spotlight: Energy security concerns have eased significantly, with respondents saying high/extreme concern falling to 18% in Jun (vs. 91% in Apr), while moderate concern has become the majority view (68%). Reflecting this shift, growth and earnings expectations strengthened further in June. Notably, 41% of respondents remain unhedged against downside risk in the AI trade.

Expected Returns: expected 12-month returns for APAC equities moderated following last month's improvement but remain broadly in line with historical norms. AI upside still appears underappreciated, with only $9\%$ of FMS investors believing the positive impact of AI on equities is more than fully priced in.

Themes: Earnings are increasingly viewed as key driver for Japan equities, rising to 41% in Jun, while policy normalization has also gained traction (27%). Taiwan (41%) remains the clear beneficiary of the AI cycle, while the US saw increased interest, rising from 10% in May to 18% in Jun.

Positioning: Indonesia has overtaken India as investors' least preferred market, while North Asia remains the clear favorite. In APAC ex Japan, FMS investors are now more overweight Tech Hardware than Semiconductors, with Financial Services emerging as a new favored sector. June also saw rotation out of Materials and Consumer Discretionary (ex Retailing) into Financial Services and Telecom. In Japan, Tech Hardware (41%) has risen to tie with Banks as the second-most preferred sector, after Semiconductors.

Exhibit 1: Investors are split on de-risking the AI trade, with 41% remaining unhedged and another 41% rotating into other sectors or underweighting  
How are you currently hedging downside risk in the AI trade over the next 6-12 months?  
![](images/af430cfc83d4603cb671bdc840d98afae9207b5665a5ea4d70a37cb729b34275.jpg)

<details>
<summary>bar chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| No hedge - remain overweight AI | 27 |
| Rotate into value / cyclicals | 18 |
| Rotate into defensive sectors | 14 |
| Rotate within AI value chain | 14 |
| Short / underweight crowded AI beneficiaries | 9 |
</details>

Source: BofA Asia Fund Manager Survey. Notes: Votes for ‘Don’t know’ are not shown above.

BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 16 to 18.

12984360

16 June 2026

Equity Strategy

Asia Pacific

BofA

Data

Analytics

![](images/3aaa2d6870b3b8c1e633c7dbafd7e531f9963ec93cc08b4e97dc4dcd5c42ba14.jpg)

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

## Notes to readers

A total of 198 panelists with \$540bn AUM participated in the May survey. 172 participants with \$465bn AUM responded to the Global FMS questions and 99 participants with \$270bn AUM responded to the Regional FMS questions.

Survey period: 5 Jun – 11 Jun 2026

## How to join the FMS panel

Investors/clients are encouraged to sign up to participate in the Survey. This can be done by contacting Michael Hartnett or your BofA sales representative.

Participants in the survey receive the full set of results for the months in which they participate.

## Macro

Exhibit 2: APAC ex-Japan growth expectations turned positive in June, marking a continued recovery from April's sharp downturn  
Net % expecting a stronger Global / APAC ex-Japan economy  
![](images/c09f6c777627e11cabcc2627fa8358589fd350e68d34eaa7363beaebf8f11a60.jpg)

<details>
<summary>line chart</summary>

| Year | Asia Pacific ex-Japan | Global |
|------|------------------------|--------|
| 97   | ~40                    | ~40    |
| 99   | ~90                    | ~40    |
| 01   | ~80                    | ~60    |
| 03   | ~100                   | ~80    |
| 05   | ~60                    | ~40    |
| 07   | ~40                    | ~20    |
| 09   | ~-100                  | ~-40   |
| 11   | ~60                    | ~80    |
| 13   | ~40                    | ~60    |
| 15   | ~60                    | ~80    |
| 17   | ~40                    | ~60    |
| 19   | ~20                    | ~40    |
| 21   | ~100                   | ~80    |
| 23   | ~60                    | ~40    |
| 25   | ~40                    | ~20    |
</details>

Source: BofA Global & Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 3: Inflation expectations remain elevated but eased in June, though still sitting well above the long-term average  
Net % expecting higher inflation in Asia Pacific ex-Japan in the next 12 months  
![](images/23face56dd6a76d1b69187d5056b26ff8ca63d5c5af415a936d28d88b97478c6.jpg)

<details>
<summary>line chart</summary>

| Year | Net % expecting higher inflation |
| ---- | -------------------------------- |
| Jun'26 | 68% |
</details>

Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 4: Corporate profit expectations strengthened further in June, well above the long-run average  
Net % expecting better corporate profits in Asia Pacific ex-Japan in the next 12 months  
![](images/d7c345b7a5cef7b965439c117ae6080158c76e52bcdd0b53132c5d0ccc1d767c.jpg)

<details>
<summary>line chart</summary>

| Year | Net % expecting better profits |
|------|---------------------------------|
| 26   | 50%                             |
</details>

Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 5: Concern that APAC ex-Japan earnings estimates are too high continue to fade in June, now at 14th percentile historically  
Net % deeming consensus EPS estimates for the coming year as high  
![](images/8129cd772fee2fc1ad9df08382d5fe3684f44fe1b28976d504692aaec71f1b4d.jpg)

<details>
<summary>line chart</summary>

| Year | Net % deeming consensus EPS estimates for the coming year as high | Asia Pac ex-Japan 1m ERR, inverted, RHS |
|------|------------------------------------------------------------------------|------------------------------------------|
| 08   | ~95                                                                    | ~60                                      |
| 10   | ~-30                                                                   | ~-20                                     |
| 12   | ~80                                                                    | ~65                                      |
| 14   | ~50                                                                    | ~45                                      |
| 16   | ~100                                                                   | ~60                                      |
| 18   | ~40                                                                    | ~35                                      |
| 20   | ~95                                                                    | ~70                                      |
| 22   | ~60                                                                    | ~55                                      |
| 24   | ~30                                                                    | ~40                                      |
| 26   | ~10                                                                    | ~25                                      |
</details>

Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 6: Energy security concerns have normalized: high/extreme concern dropped 73pts since Apr, while moderate concern became the majority view  
How concerned are you about energy security risks for APAC region in current geopolitical environment?  
![](images/48e35c4bde42e0955ec05be709cbd6b97fbbaa4eafcc373618f00c99dd69010d.jpg)

<details>
<summary>bar chart</summary>

| Concern Level | Jun-26 (%) | May-26 (%) | Apr-26 (%) |
|---|---|---|---|
| Highly to extremely concerned | 18 | 52 | 91 |
| Slightly to moderately concerned | 68 | 48 | 9 |
| Not concerned | 14 | | |
The chart displays a single data series with three distinct color-coded bars for each category. The x-axis represents percentage from 0% to 100%. The y-axis lists the concern levels in Chinese.
</details>

Source: BofA Asia Fund Manager Survey. Notes: Votes for ‘Don’t know’ are not shown above.  
BofA GLOBAL RESEARCH

Exhibit 7: China growth sentiment remains negative, with net reading unchanged at -14% vs. May Net % expecting a stronger Chinese economy in the next 12 months  
![](images/6fe2d43b51fbbc69c5d32691b2b3b78922fdd6c09dee377484aba95acf8701f9.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jun'26 | -14%  |
</details>

Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 8: Japan growth expectations improved further in June, surpassing the long-term average  
Net % expecting a stronger Japanese economy over the next 12 months  
![](images/093a38b9b3f88975a2f35c72f7ac335f477e00d67e6a748e9ec7ba3aa4ce4863.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jun'26 | 59%   |
</details>

Source: BofA Asia Fund Manager Survey. Notes: Votes for ‘Don’t know’ are not shown above.

BofA GLOBAL RESEARCH

Exhibit 9: Investors expect the next rate hike to be most likely in Jun  
When do you think the BOJ next rate hike will be?  
![](images/d5eca9f8c0aa8056028906e843b979f01e8dd4a64af3358e7bf4a4b6c2e40378.jpg)

<details>
<summary>bar chart</summary>

When do you think the BOJ next rate hike will be?
| Month | Percentage (%) |
| :--- | :--- |
| Jun 2026 | 64 |
| Jul 2026 | 14 |
| Sep 2026 | 18 |
| Oct 2026 or later | 5 |
</details>

Source: BofA Asia Fund Manager Survey

BofA GLOBAL RESEARCH

## Expected Returns and Valuations

Exhibit 10: Investor optimism cooled after last month's improvement but remains broadly in line with historical norms  
FMS views on expected upside for Asia Pac ex-Japan equities over the next 12 months  
![](images/0520edb7cd027cd3447f1a4d534e270dcb8b6ff2740d3a09f901dd3e316fe972.jpg)

<details>
<summary>area chart</summary>

| Date   | Expected upside for APAC ex-Japan equities over the next 12 months |
|--------|------------------------------------------------------------------|
| 10/22  | 4%                                                               |
| 12/22  | 7%                                                               |
| 02/23  | 5%                                                               |
| 04/23  | 4%                                                               |
| 06/23  | 5%                                                               |
| 08/23  | 5%                                                               |
| 10/23  | 3%                                                               |
| 12/23  | 5%                                                               |
| 02/24  | 5%                                                               |
| 04/24  | 5%                                                               |
| 06/24  | 5%                                                               |
| 08/24  | 4%                                                               |
| 10/24  | 5%                                                               |
| 12/24  | 4%                                                               |
| 02/25  | 5%                                                               |
| 04/25  | -3%                                                              |
| 06/25  | 4%                                                               |
| 08/25  | 5%                                                               |
| 10/25  | 5%                                                               |
| 12/25  | 6%                                                               |
| 02/26  | 6%                                                               |
| 04/26  | 3%                                                               |
| 06/26  | 6%                                                               |
</details>

Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 11: Similar to Asia ex, optimism in Japan has normalized after last month's peak  
FMS views on expected upside for Japan equities over the next 12 months  
![](images/bdd93e8253ee25c3ed653adca3b020290033dbf2cbeafefeb06ee88bbdbd847b.jpg)

<details>
<summary>area chart</summary>

| Date   | Expected returns for Japan equities over the next 12 months (%) |
|--------|------------------------------------------------------------------|
| 11/23  | 6.0                                                              |
| 01/24  | 5.5                                                              |
| 03/24  | 6.5                                                              |
| 05/24  | 5.3                                                              |
| 07/24  | 4.8                                                              |
| 09/24  | 5.6                                                              |
| 11/24  | 5.4                                                              |
| 01/25  | 5.0                                                              |
| 03/25  | 5.8                                                              |
| 05/25  | 1.5                                                              |
| 07/25  | 4.2                                                              |
| 09/25  | 4.7                                                              |
| 11/25  | 4.8                                                              |
| 01/26  | 5.5                                                              |
| 03/26  | 4.5                                                              |
| 05/26  | 6.8                                                              |
</details>

Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 12: FMS investors still see APAC ex-Japan equities as slightly undervalued  
Net % saying Asia Pacific ex-Japan equities are overvalued  
![](images/78f3d25edae72b92d008bfc42fd824cde233c06e871bb77106106e8f26cb1eef.jpg)

<details>
<summary>line chart</summary>

| Date  | Value |
|-------|-------|
| Jun'26 | -5%   |
</details>

Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 13: AI upside still looks underappreciated. Only 9% of FMS investors say the positive AI impact on equities is more than fully priced in  
How much of the positive AI impact on equities is already reflected in the price?  
![](images/3fd86955ed1e10ed783db5fe8772ea52e528bde5f0bb460e0910c005509eb0aa.jpg)

<details>
<summary>bar chart</summary>

| Pricing Category | Jun-26 (%) | May-26 (%) |
|---|---|---|
| More than fully priced in | 9 | 5 |
| Broadly fairly priced | 41 | 33 |
| Partially priced in | 41 | 52 |
| Mostly not priced in | | 5 |
</details>

Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH

## Themes

Exhibit 14: Within China, AI/semis and buybacks/dividend remain key investor priorities
FMS views on TWO most favorite themes in China  
![](images/237b94184c0a10e9f19c04944c41c3ac643a58a23abd695eb704cdddd3f66781.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (%) |
| :--- | :--- |
| AI / Semiconductors | 50 |
| Buybacks/Dividend | 23 |
| Internet | 14 |
| Green economy | 14 |
| SOEs | 9 |
| Cyclicals | 9 |
| Healthcare | 5 |
| Anti-involution | 5 |
| Others | 5 |
| Real Estate | 5 |
| Travel & leisure | 0 |
</details>

Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH  
FMS views on the themes that hold the key for Japan equities in the near-to-medium term

Exhibit 15: Earnings increasingly seen as key driver for Japan equities, rising to 41% in Jun, while policy normalization also gained traction at 27%

![](images/829c02a5c1038061a81f433ee95af5a0d4238dadae057d00e2c2bd9a62b5c197.jpg)

<details>
<summary>bar chart</summary>

Key themes for Japan equities in the near-to-medium term
| Theme | May-26 (%) | Jun-26 (%) |
| :--- | :--- | :--- |
| Earnings | 38 | 41 |
| Policy normalization by the BoJ | 19 | 27 |
| Corporate governance reforms & Japan Exchange Group (JPX) initiatives | 19 | 14 |
| Currency (JPY) moves | 14 | 9 |
| Others | 5 | 0 |
</details>

Source: BofA Asia Fund Manager Survey. Notes: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH

Exhibit 16: Investor expectations for the Korea/Taiwan semis cycle eased from May but stay firmly positive in June  
FMS views on the semis cycle (Korea/Taiwan exports growth) over the next 12 months  
![](images/362b2a9c3e5568674e1a2d537c3f5e1f4a74617b66df4195b6637edeba1ed341.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jun-2026 | 55%   |
</details>

Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 17: Taiwan remains the clear AI-cycle beneficiary, while US gained momentum in Jun Which market benefits most from the next phase of the AI cycle?  
![](images/142a7263440ae53d8fd7d9a16cc222534be08d2e62981a2c81c77dc2af13e5d6.jpg)

<details>
<summary>bar chart</summary>

| Country | May-26 (%) | Jun-26 (%) |
| :--- | :--- | :--- |
| Taiwan | 43 | 41 |
| Korea | 29 | 23 |
| US | 10 | 18 |
| Japan | 14 | 9 |
| China | 0 | 5 |
</details>

Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH

Exhibit 18: The absence of a clear AI play remains the primary concern for the Indian market. What is your key concern for Indian market?  
![](images/3617b3f394d5466e64de74dad8e56531dab2377b6e9c6723e323e23d9116b4cf.jpg)

<details>
<summary>bar chart</summary>

| Category | Percentag

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
