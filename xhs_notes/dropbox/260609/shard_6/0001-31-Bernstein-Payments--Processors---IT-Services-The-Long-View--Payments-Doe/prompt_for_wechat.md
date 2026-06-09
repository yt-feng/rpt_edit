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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Bernstein`。标题格式建议：`# Bernstein：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Payments, Processors & IT Services

# The Long View: Payments - Does Cash Digitization Runway Still Exist?

![](images/1bac511ab1c4e005f9b82dea3f67da9d805d60a8eaf0adfaee504d6b2277796a.jpg)

Harshita Rawat, CFA

+1 917 344 8485

harshita.rawat@bernsteinsg.com

![](images/a4eb14d244b898c078202b57f38ff467655485e825a16ea963913c209026b7c2.jpg)

Simran Ratani

+1 917 344 8329

simran.ratani@bernsteinsg.com

![](images/54e06bad7e378e8849583260cbf76e770ad11131f4afa0bc166677e967b38261.jpg)

Viola Chen

+1 917 344 8614

viola.chen@bernsteinsg.com

We publish the 12 $^{th}$ annual edition of our global payments forecast model. A lot has changed in the last 10+ years - U.S. is now highly penetrated by cards (72% vs. 58% ten years ago), local payment methods have gained traction (e.g., in Asia where card volume growth has somewhat stalled), domestic schemes have lost share (e.g., in Europe), other alternative ways to pay (e.g., A2A) have generated noise but have remained contained, and stablecoins are finding some utility in markets where dollars are desirable. Last year was the first time when we brought our forecasts down (see link) - largely because of market maturing in the U.S. and regional dynamics in Asia. Against that dynamic backdrop, our global payments forecast model remains the under-pinning of our investment view on the sector and V/MA in particular - even as value-added services capture a growing share of revenue.

We forecast 8% cc (\~7-8% nominal) card volume growth from 2025-30E (below 2022-25 CAGR of 9% cc), driven by 5-6% PCE growth and 2-3% card penetration-driven growth (penetration growing to 71%, up from 64% in 2025). The exit growth rate in 2030 in our model is 7%. We forecast deceleration vs. history (\~8% cc vs. 9% cc historically) due to already high penetration in the U.S. (where we now forecast \~5-6% card volume growth CAGR vs. \~6% CAGR between 2022-25), slowdown in Asia (due to local market nuances). Europe remains an attractive market for cards: we forecast 11% cc volume growth driven by continental Europe (e.g., Germany, Italy, Spain) vs. 16% historically. We are monitoring optionality driven by possible inflection in eCommerce from Agentic commerce and autonomous agent transactions as a growth driver for card payments but note that it's simply too early to bake anything into our numbers. We will closely monitor how cards' commercial models to address historically tougher to address categories such as rent and healthcare.

We forecast a stronger growth at 9% in the number of transactions globally between 2025-30E (10% 2022-25). Card penetration is lower when assessed as a % of number of transactions (as opposed to transaction value). V/MA derive >1/3rd of their gross revenue from # of transactions, which tend to grow faster than \$ volumes. Cross-border is at an interesting point, and we will address that in a separate note.

Card volumes only tell part of the story. We see a runway in tokens, VAS penetration and optionality in new flows (more details in a separate note), which along with 9% growth in transactions can drive DD% revenue growth despite card volume growth of 8%. For reference, even in high card penetration markets, networks have historically demonstrated an ability to grow revenues at double digits. Domestic schemes (\~\$4T of volumes globally) are an underappreciated opportunity e.g., Visa gained 5-6ppt share in Continental Europe vs Girocard / CB card in Germany/France in 2024.

Alternative ways-to-pay drive HSD-LDD% of consumer-to-business payments globally. While account-to-account and local methods are a risk to debit (especially in certain markets), even where A2A/local payments have had success (e.g., India, Brazil), credit-card volumes are growing HSD-LDD%. Finally, on a 5yr time horizon, we view stablecoins as a solution looking for a problem in retail consumer payments (note).

## INVESTMENT IMPLICATIONS

We rate V, MA, ADYEN, XYZ and TOST OP. We rate PYPL, FIS, FISV, GPN, KLAR MP.

## PLEASE SEE LINKS TO OUR RECENT RESEARCH

- Weekend Tech Byte: The 'cost' of cards — the often misleading comparisons; our perspectives in key charts (June 2026)  
• Visa: Reflections on our Fireside Chat with CEO Ryan McInerney (June 2026)  
- Payments: Stablecoins — What we learned from our dozens of industry conversations; Slide deck (May 2026)  
• Visa, Mastercard: Numbers look good but will it matter? (April 2026)  
• Visa, Mastercard: The bull case; slide deck from deep dive call on Agentic, Stablecoins, VAS and Regulation (March 2026)  
• The Age of Agents: Insights from our Inaugural Agentic Commerce Day (April 2026)  
• Payments: Mastercard's BVNK acquisition; what Stablecoins truly mean for payments (March 2026)  
• Visa, Mastercard: Payments-ocalypse, will AI doom the networks? (February 2026)  
• Payments: The growing regulatory risk premium? But will the numbers be impacted in the medium-term?  
• Payments/Fintech 2026: A year to remember? Top themes and stock ideas (January 2026)  
• Visa, Mastercard: Why we like the networks more now vs. 5yrs ago (October 2025)  
- Stablecoins: Let's Play Out a Scenario for Disruption in Consumer Payments.. (June 2025)  
• Payments: What happens in a recession? (Mar 2025)

## DETAILS

## OUR FORECAST: \~8% CC (\~7-8% NOMINAL) CARD VOLUME GROWTH FROM 2025-30

We forecast \~8% constant currency (\~7-8% nominal) C2B purchase volume CAGR over the next 5 years - slightly below the \~9% growth between 2022-25 and \~11% between 2019-22 (Exhibit 3).

## Card penetration grew 2-3ppt/year from 2022-25. We estimate it to grow \~1-2ppt/year going forward (Exhibit 1).

Card penetration grew \~1ppt in 2025. The \~1ppt penetration growth in 2025 was driven by healthy penetration growth in regions such as Europe (up 3ppt), LATAM (3ppt), MEA (\~3ppt), offset by more muted growth in Canada (90%+ penetration), US (flat) and APAC (\~-1ppt; flat ex-V/MA volumes in China). The pandemic very clearly accelerated cash digitization through faster growth in eCommerce, an increase in contactless usage, greater adoption of digital payments by merchants and by bringing in new digital payment users. From 2019-22, global card penetration grew \~3ppt/year, twice the historical average rate.

We forecast deceleration vs. history (\~8% cc vs. 9%) due to already high penetration in the U.S. (where we forecast \~5-6% card volume growth CAGR vs. \~6% CAGR between 2022-25), slowdown in Asia (due to local market nuances in certain markets and unique dynamics in mainland China - see details in the note). Our estimates embed the fact that many developed markets are now at high card penetration and EM is a battleground. In 2025, we estimate US card penetration at \~72%, up from \~67% in 2019. We estimate markets representing \~50% of global GDP (e.g., US, UK, Canada, Australia, South Korea) are now already at >80% digital payments penetration.

## Note:

- Our forecasts do not include meaningful tailwind from new payment flows, nor do they incorporate benefits from agentic commerce (it's simply too early to bake into our numbers). We also exclude Visa direct (in addition to commercial cards) from the numerator. Our forecast doesn't fully incorporate new ways to pay i.e. cards used to fund digital wallets as this can be quite tricky for a few markets.  
- Our card penetration numbers might differ slightly vs our prior estimates as we update our denominator (i.e. PCE numbers) to reflect recent data.

EXHIBIT 1: We expect card penetration to approach \~71% by 2030, up from 64% in 2025  
![](images/58c2cf2b53f3216a96daf20a96e24753eb3bdfb6dfe732c4dbe995b4ae3d117b.jpg)

<details>
<summary>bar chart</summary>

Card Penetration of Purchase PCE (Nominal and Adj. ex-China)
| Year | Penetration (%) |
| :--- | :--- |
| 2010 | 30 |
| 2013 | 36 |
| 2016 | 41 |
| 2019 | 47 |
| 2022 | 57 |
| 2025 | 64 |
| 2028E | 69 |
| 2030E | 71 |
</details>

Source: Nilson, World Bank, IMF, Bernstein estimates and analysis

EXHIBIT 2: Majority of card volume growth from 2025 to 2030E will still be driven by US and Europe  
![](images/c7e55997480f9858c0bfc90725d60d6e0786927b2658d49d28e192af81b4b264.jpg)

<details>
<summary>bar chart</summary>

Growth in Global General Purpose Card Dollar Volume, Purchases (2025-2030E, CC)
| Region | Value ($) |
| :--- | :--- |
| 2025 GP Volume | ~$26T |
| US | ~$3.5T |
| Europe | ~$3.5-4T |
| Asia | ~$1T |
| LATAM | ~$1-1.5T |
| Canada | <$1T |
| MEA | ~$1T |
| 2030E GP Volume | ~$37T |
</details>

Source: Nilson, World Bank, IMF, Bernstein estimates and analysis

EXHIBIT 3: On a cc basis, card volumes grew at \~11% between 2019-22, \~9% between 2022-25 and we forecast \~8% growth between 2025-30.  
![](images/f44c3845b0e727abb97ad90d0f8906fa7965dd61b3ad0ce5565193929e070b2d.jpg)

<details>
<summary>stacked bar chart</summary>

Global Card Purchase Volume Growth Drivers (ex. China)
| Age Group | PCE Growth (%) | Penetration Driven Growth (%) |
| :--- | :--- | :--- |
| 16-19 | 4 | 6 |
| 19-22 | 6 | 4 |
| 22-25 | 7 | 3 |
| 25-30E | 5 | 2 |
~10% ~11% ~9% ~8% CC
</details>

Note: Exclusion of Russia has a modest negative impact on 2019-22, 22-25 growth CAGRs  
Source: Nilson, World Bank, IMF, Bernstein estimates and analysis

EXHIBIT 5: Card volumes grew at \~8% on a nominal basis in 2025..  
![](images/e090cd7f7cbb23bcbafbb68b7dc0e47fb0f99bc2e8aa2e1017f99b5f80a881b2.jpg)

<details>
<summary>stacked bar chart</summary>

Global Card Purchase Volume Growth Drivers (ex. China)
| Year | PCE Growth (%) | Penetration Driven Growth (%) |
| :--- | :--- | :--- |
| 2023 | 7 | 2 |
| 2024 | 7 | 2 |
| 2025 | 6 | 2 |
CC
10%
</details>

Source: Nilson, World Bank, IMF, Bernstein estimates and analysis

EXHIBIT 4: On a nominal basis, we forecast \~7-8% card volume growth over 2025-30E globally.  
![](images/e6153ac24a65e5f6957325e93c62e51320f4da7e5b8ecf20553fd0f6c628acba.jpg)

<details>
<summary>stacked bar chart</summary>

Global Card Purchase Volume Growth Drivers (ex. China)
| Nominal | PCE Growth (%) | Penetration Driven Growth (%) |
| :--- | :--- | :--- |
| 16-19 | 4 | 5 |
| 19-22 | 3 | 6 |
| 22-25 | 6 | 3 |
| 25-30E | 5 | 2 |
~8% ~10% ~8% ~7-8%
</details>

Note: Exclusion of Russia has a modest negative impact on 2019-22, 22-25 growth CAGRs  
Source: Nilson, World Bank, IMF, Bernstein estimates and analysis

EXHIBIT 6: ..and also on cc basis  
![](images/3be3947989a298c469868ae6fab9001f38aff6f69f85336df30a9a5035b31d34.jpg)

<details>
<summary>stacked bar chart</summary>

Global Card Purchase Volume Growth Drivers (ex. China)
| Year | PCE Growth (%) | Penetration Driven Growth (%) |
| :--- | :--- | :--- |
| 2023 | 6 | 2 |
| 2024 | 5 | 1 |
| 2025 | 6 | 2 |
Nominal
10%
6%
6%
8%
</details>

Source: Nilson, World Bank, IMF, Bernstein estimates and analysis

## CARD VOLUME GROWTH WILL LIKELY BE MORE CYCLICAL VS. HISTORY AS PENETRATION-DRIVEN GROWTH SOMEWHAT EASES

On a nominal basis, our \~7-8% volume CAGR forecast from 2025-30E comprises \~5% underlying global PCE growth & \~2ppt of secular cash to card conversion growth.

Our 5-yr nominal growth outlook by region is \~5-6% for U.S., \~11% cc (\~10% nominal) for Europe, \~5% cc (\~4% nominal) for Asia, \~13% for Latam cc (similar on nominal basis), 5% for Canada cc (\~6% nominal) and 14% cc (12% nominal) for MEA. We estimate that U.S. is \~72% penetrated by cards (up from \~67% in 2019), Europe at \~77% (up from 44% in 2019), Asia-Pac (ex-mainland China) at \~41% (up from 36% in 2019), Latam at \~48% (up from 29%), Canada at \~92% (up from 79% in 2019) and MEA at \~61% (up from 26%) (Exhibit 9).

We currently exclude mainland China from our forecasts but note that Mastercard went live in mainland China in May 2024 after acquiring a domestic license. Further, in APAC, in addition to mainland China, there are also certain local market dynamics which we will discuss later in the note.

EXHIBIT 7: Our growth forecast by region on cc basis - US - \~5-6%, Europe - 11%, APAC - 5%, LATAM - 13%, Canada - 5%, MEA - 14%

General Purpose Card Purchase Volume Growth Drivers by Region (CC, ex. China)  
![](images/b29f0072b1912e9e44c9e0bf75e4f0aab8782e2a489a408fe1bdc390793cf4da.jpg)

<details>
<summary>stacked bar chart</summary>

| Region | Period | PCE (%) | Penetration driven growth (%) |
| :--- | :--- | :--- | :--- |
| Global | 22-25 | 7 | 3 |
| Global | 25-30E | 5 | 3 |
| US | 22-25 | 5 | 1 |
| US | 25-30E | ~4-5 | -1-2 |
| Europe | 22-25 | 7 | 8 |
| Europe | 25-30E | 5 | 5 |
| APAC | 22-25 | 7 | (2) |
| APAC | 25-30E | 7 | (2) |
| Latam | 22-25 | 11 | 6 |
| Latam | 25-30E | 6 | 6 |
| Canada | 22-25 | 5 | 0 |
| Canada | 25-30E | 4 | 1 |
| MEA | 22-25 | 5 | 11 |
| MEA | 25-30E | 7 | 6 |
~9-10%; ~7-8%; ~5-6%; ~11%; ~9%-10%; ~5%-2%; ~11%; ~11%; ~13%; ~5%; ~5%; ~5%; ~14%.
</details>

Source: Nilson, World Bank, IMF, Bernstein estimates and analysis

EXHIBIT 8: Our nominal growth forecast by region - US - \~5-6%, Europe - 10%, APAC - 4%, LATAM - 13%, Canada - 6%, MEA - 12%

General Purpose Card Purchase Volume Growth Drivers by Region (Nominal, ex. China)  
![](images/a18377fba0aeab8f9c5c102fa4f326f59869301d9dc230846163bc300ccae570.jpg)

<details>
<summary>stacked bar chart</summary>

| Region | Period | PCE (%) | Penetration driven growth (%) |
| :--- | :--- | :--- | :--- |
| Global | 22-25 | 6 | 3 |
| Global | 25-30E | 5 | 2 |
| US | 22-25 | 5 | 1 |
| US | 25-30E | 4 | -1 |
| Europe | 22-25 | 8 | 7 |
| Europe | 25-30E | 5 | 5 |
| APAC | 22-25 | 4 | -2 |
| APAC | 25-30E | 6 | -2 |
| Latam | 22-25 | 6 | 7 |
| Latam | 25-30E | 6 | 6 |
| Canada | 22-25 | 3 | 1 |
| Canada | 25-30E | 5 | 1 |
| MEA | 22-25 | -1 | 15 |
| MEA | 25-30E | 6 | 6 |
The chart displays two data series: 'PCE' (blue bars) and 'Penetration driven growth' (teal bars). The values in parentheses indicate percentage changes relative to a baseline. The x-axis labels are 'Global', 'US', 'Europe', 'APAC', 'Latam', and 'Canada'. The y-axis is implied by the percentage labels above each bar.
</details>

Source: Nilson, World Bank, IMF, Bernstein estimates and analysis

EXHIBIT 9: We expect card penetration growth to be driven by Europe, Latam, and MEA  
Card Penetration of C2B Addressable PCE (Nominal, adjusted ex China)  
![](images/5e84612ef132050df8ef272071d6dfb8c925121e4f00a6de375ad7ae01ebaa5d.jpg)

<details>
<summary>bar chart</summary>

| Region | 2019 (%) | 2022 (%) | 2025 (%) | 2028E (%) | 2030E (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Global | 47 | 57 | 64 | 68 | 71 |
| United States | 67 | 72 | 72 | 74 | 74 |
| Europe | 44 | 61 | 76 | 86 | 92 |
| Asia-Pac | 36 | 37 | 40 | 41 | 41 |
| Latam | 29 | 39 | 48 | 59 | 65 |
| Canada | 79 | 89 | 92 | 94 | 95 |
| ME-A | 26 | 40 | 61 | 73 | 81 |
</details>

For APAC, the numerator excludes V/MA from China from General Purpose Card Volumes in the previous exhibits  
Source: Nilson, World Bank, IMF and Bernstein estimates and analysis

## THERE IS STILL A FAIR AMOUNT OF CASH/CHECK THAT EXISTS GLOBALLY

Although it sure feels like cards are everywhere, there is still a good amount of cash/ check in existence globally. Consumer-to-business (C2B) payments is a \$40T market and is currently 64% penetrated by cards (vs. 47% in 2019). We expect card penetration to approach \~70-75% by 2030. We est. \~\$11T of cash/check opportunity globally split across different regions e.g., U.S./Canada (\~\$2T), Europe (\~\$3T), Asia-Pac ex-mainland China (\~\$3-4T), Latam (\~\$1.5-2T), MEA (\~\$0.5-T) in 2025 (Exhibit 10). We estimate that the top 25 markets by GDP combined have at least \~\$3-4T of cash (excluding checks).

Catalysts for continued cash digitization — contactless, e-commerce and possibly agentic commerce. Contactless has proven to be a powerful catalyst for accelerating cash-to-card conversion. And these payments are a great tool for habit formation in digital purchases through very sticky every day use-cases such as transit, groceries, vending machines, etc. Global tap-to-pay or contactless penetration of face-to-face transactions for MA grew 5ppt in 2025 to 77% (78% in 1Q26) and, up from 45% in 2021. eCommerce and the era of agentic transactions, potentially micropayments are also catalysts that can accelerate volume and transactions (more on this below) growth.

EXHIBIT 10: Although it sure feels like cards are everywhere, there is still a surprising amount of cash/check in existence globally  
Global Cash/Other volumes by region (2025E, Total \$11T)  
![](images/876076ac33605f372d8894006abecbf941e59b1dd61b90dd13c096dcb7f8176a.jpg)

<details>
<summary>pie chart</summary>

| Region | Value | Percentage (%) |
| :--- | :--- | :--- |
| Canada | 0.1 | 1 |
| ME-A | 0.8 | 7 |
| U.S | 2.0 | 18 |
| Europe | 3.1 | 29 |
| APAC | 3.4 | 31 |
Latam | 1.6 | 14 |
</details>

Source: Nilson, WEO, World Bank, Mastercard Whitepaper (Cashless journey), Corporate reports and Bernstein estimates and analysis

## DIGITAL PAYMENTS PENETRATION VARY SIGNIFICANTLY BY COUNTRY

Digital payments (and cards) penetration vary significantly by country and payments are local and how people pay truly varies by country. Cards being one of the most popular payment methods, is often complemented with digital wallets, RTP networks, etc. depending on the country you look at.

EXHIBIT 11: Cash Usage varies widely by country; Mexico, Japan, Indonesia, Germany still have high amounts of cash..  
Cash as a % of POS Transaction Value (Top 15 GDP Countries, 2025)  
![](images/fbbd3d7b7f7878bbb106b315ad99089b2d65bd2e6bfcedc97169e023e87308e0.jpg)

<details>
<summary>bar chart</summary>

| Country | Percentage (%) |
| :--- | :--- |
| Mexico | 40 |
| Japan | 38 |
| Indonesia | 36 |
| Spain | 34 |
| Germany | 32 |
| Italy | 24 |
| Türkiye | 20 |
| India | 14 |
| Brazil | 12 |
| France | 12 |
| Australia | 12 |
| United States | 10 |
| Canada | 10 |
| United Kingdom | 9 |
| South Korea | 6 |
</details>

Source: Global Payments Report, Bernstein analysis

EXHIBIT 12: Share of domestic schemes also varies widely by country..  
Share of Domestic Schemes within Overall Network (%, 2024)  
![](images/9a033c7af7791f9ededd02a40c96b65f2228e4d0375c3549e1d807d7a0d6006d.jpg)

<details>
<summary>bar chart</summary>

| Country | Percentage (%) |
| :--- | :--- |
| South Korea | 97 |
| France | 76 |
| Germany | 67 |
| Italy | 36 |
| Japan | 29 |
| Canada | 29 |
| Australia | 21 |
| Indonesia | 16 |
| India | 13 |
| Brazil | 9 |
| Türkiye | 3 |
</details>

South Korea includes BC, Hana, Hyundai, KB Kookmin, Lotte,  
NH, Samsung, Shinhan, Woori; France includes Cartes Bancaires; Germany includes Girocard; Italy includes Poste Italiane, Bancomat; Japan includes JCB;

Canada includes Interac; Australia includes EFTPOS; Indonesia includes GPN;

India includes 

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
