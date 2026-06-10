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
## AD TECH PRIMER

## US Internet

## Intro to Mobile Ad Tech: Who Are the Players, What Do They Do, and What's Changing?

MS
North America

MS & Co. LLC

## Matthew Cost

Matthew.Cost@morganstanley.com

+1 212 761 7252

## Brian Nowak, CFA

Brian.Nowak@morganstanley.com

+1 212 761 3365

## Cela VanLieshout

Cela.VanLieshout1@morganstanley.com

+1 212 761 2679

## Intro to Mobile Ad Tech

![](images/bebbdbbc02060b03ff3beee5c37537af39fa94996b17150dd9fefb1b8d53b1cd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["1\nMobile Ad Tech Ecosystem Overview"] --> B["2\nSustainability Of Growth"]
  B --> C["3\nCompetition"]
  C --> D["4\nImpact of AI"]
  D --> E["5\nSignal/Privacy & Platform Risk"]
```
</details>

## In-App Ads Typically Send Consumers to the App Stores to Download New Products – Today, Most of Those Ads Are Promoting Games...

![](images/74fa9c6e0ef24bcc2724bdb81a218ecadc8f2328456e642c508327c7a2531bdf.jpg)

<details>
<summary>text_image</summary>

4:29
5G
WORDS with friends™
ATGO
</details>

User Opens & Plays a Publisher's App

![](images/23f24f1100fe1d7da3b2f6fbdd215d2d05b87abf543ff0291111aee36898150a.jpg)

![](images/ca35faca11f02d2c0e74405bb58dde36a31a7e5c3d941b4185ae6c1af9300285.jpg)

<details>
<summary>text_image</summary>

Kingshot
Play Now
4
0
10
Swipe to move
</details>

An Interactive or Video Ad Will Appear for User

![](images/fa1cbfe42ca1451e47d70ae02e29805fec394921d4f131d1db6b42cd01650faf.jpg)

![](images/22c707856aa0d8fe1f3b45a6f164b98e639878c012073636ca1bd0922096b43e.jpg)

<details>
<summary>text_image</summary>

Done
Kingshot
Century Games Pte. Ltd.
Get In-App Purchases
148K RATINGS AGE CHART
4.6 9+ #4
Years Old Strategy Cen
DEFEND EXPLO
</details>

User is Prompted to Download the Game

## ...But Other Categories like Retail and Entertainment Are Important Drivers of the \$79bn Opportunity for Independent In-App Ad Tech Platforms Like APP and U

Global Ad Spend on Independent In-App Ad Tech Platforms is Projected to Reach \$136bn in 2030\*  
![](images/c32b23e0b3ec8fd9b91220932d8d474658948a69eca96f053e6643a0f3984fb6.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Gaming ($bns) | Non-Gaming Entertainment ($bns) | Retail ($bns) | Social Media ($bns) | Other (Education, Finance, Messaging) ($bns) | AI Apps ($bns) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2025E | 46 | 12 | 5 | 5 | 8 | 0 |
| 2026E | 47 | 12 | 5 | 5 | 8 | 0 |
| 2027E | 49 | 13 | 5 | 5 | 8 | 0 |
| 2028E | 51 | 14 | 5 | 5 | 8 | 0 |
| 2029E | 53 | 15 | 5 | 5 | 8 | 0 |
| 2030E | 55 | 16 | 5 | 5 | 8 | 136 |
~11% '25-'30 CAGR; total ad spend is projected at $136 billion. The chart displays a single stacked bar for each year from 2025E to 2030E.
</details>

## The Estimated Near-Term Market Opportunity is \$79bn, Though Total In-App and Mobile Advertising Are Larger, When Including Walled Garden Platforms like GOOGL and META

![](images/5e8a2ddf4da89d4bde19324664c153b76bdfb127b105f65560bb97b06aaba7fd.jpg)

<details>
<summary>venn diagram chart</summary>

| Category | Value |
| -------- | ----- |
| Global Mobile Ad Spend | $554bn^(2) |
| Global In-App Ad Spend | $332bn^(1) |
| Independent Ad-Tech Platform Opportunity | $79bn^(1) |
</details>

(1) According to Altman Solon  
(2) According to eMarketer  
(3) According to SensorTower

## 5bn

Smartphone Users Globally $^{(2)}$

## \~3 hours

Spent on Apps per Day $^{(3)}$

## \$554bn

Global Mobile Ad Spend per Year $^{(2)}$

## 90%

Mobile Time Spent In-App $^{(2)}$

## We Also Expect Meaningful Growth Across Broader Markets Like In-App Advertising (incl. Walled Gardens) as well as Total Mobile Advertising

![](images/0c0686b1f2ab44ad83f1e0fc5a92890d6100be31078df11756aa99cb98df9f84.jpg)

<details>
<summary>bar chart</summary>

| Year | Global Mobile Ad Spend** ($bn) | Global In-App Ad Spend* ($bn) |
| ---- | ------------------------------ | ----------------------------- |
| 2025 | 554                            | 332                           |
| 2029 | 812                            | 545                           |
</details>

\*According to Altman Solon  
\*\*According to eMarketer  
Source: Company Data, MS, Altman Solon, eMarketer  
Note: 2029 Number for Global In-App Ad Spend Found by Using 2025-2030 CAGR

## We Expect In-App Advertising to Grow at an 11% CAGR through '30, Materially Faster than Growth on In-Game Purchases at a 5% CAGR...

![](images/ed909fbe51e673761ed0860b3efc1bf8b367aa228b1663f648e9ac772a95d823.jpg)

<details>
<summary>bar chart</summary>

| Category                  | 2025   | 2030   |
| ------------------------- | ------ | ------ |
| In-App Ads (Altman Solon) | $79    | $136   |
| In-App Purchases ($bn)   | $116   | $146   |
</details>

## ...But This Has Strong Precedent, as User Acquisition Costs for Mobile Games Materially Outgrew Spend per User Pre-COVID...

## 24%

Cost Per Install

2012-2019 CAGR

![](images/d30307d9d20c4a63c5715d1d272bfae6e08cb7805ca596a1199c405e2307c472.jpg)

<details>
<summary>bar chart</summary>

| Year | Cost Per Install ($) |
| :--- | :--- |
| 2012 | 0.97 |
| 2019 | 4.37 |
</details>

## 17%

Average Revenue Per Mobile Gamer

2012-2019 CAGR

![](images/ed24888ca17fe8b939e90d85e84004217fbcfa6e8c96c30f03100100f7ddfada.jpg)

<details>
<summary>bar chart</summary>

| Year | In-App Ad Revenue Per Mobile User ($) |
| :--- | :--- |
| 2012 | 12.85 |
| 2019 | 38.06 |
</details>

## ...and the Trend Has Continued in Recent Years, With Mobile Gaming UA Spend Growing at a 15% '20-'25 CAGR vs. IAP Growing Just 3% Over the Same Period

## 15%

Mobile Gaming UA Ad Spend

2020-2025 CAGR

![](images/66a9236c11f699c7ab609d6aeba09788b1e2edfe3a7822a048746b896164b1c7.jpg)

<details>
<summary>bar chart</summary>

| Year | Mobile Gaming UA Ad Spend ($bn) |
| :--- | :--- |
| 2020 | 12 |
| 2021 | 14.5 |
| 2022 | 26.8 |
| 2023 | 29.0 |
| 2024 | 22.8 |
| 2025 | 25.0 |
</details>

In-App Ad Spend Arguably Remains Under-Monetized Relative to Other Ad Channels  
![](images/8823c5ff1d2b9b499aa0a79ee70cba00f9bb242af90ccbae0f38fd78e2a87bcf.jpg)

<details>
<summary>bar chart</summary>

| Category | Ad Spend Per User Hour ($) |
| :--- | :--- |
| In-App 3rd Party | 0.07 |
| Walled Garden In-App | 0.14 |
| CTV | 0.24 |
| Traditional TV | 0.38 |
</details>

3 $^{rd}$ Party In-App Represents One of the Highest Growth Opportunities in Digital Advertising

Who Are Some of the Players in Mobile Ad Tech and What Roles Do They Play?  
![](images/e3aef6e2b3ab8ebab4630ad495358c866bf7890b1e628c3ff6a38bdcabef0e6e.jpg)

<details>
<summary>table</summary>

| Company | DSP | SSP | Mediation |
| :--- | :--- | :--- | :--- |
| APPLOVIN | ✓ | | ✓ |
| Unity® | ✓ | ✓ | ✓ |
| Meta | ✓ | | |
| Google | ✓ | ✓ | ✓ |
| Mintegral | ✓ | ✓ | |
| InmOBI™ | ✓ | ✓ | |
| Moloco | ✓ | ✓ | |
| CloudX | | ✓ | ✓ |
</details>

## What Do Those Roles Mean?

<table><tr><td>Advertisers</td><td>Companies aiming to acquire new usersIn this market, typically app-based businesses or those with an app</td></tr><tr><td>DSP</td><td>Software that helps advertisers buy digital ads programmatically (i.e. in an automated way)Aids advertisers in targeting the right users and selecting creative to achieve their objective by analyzing all available and relevant data, as well as learning from past ad campaigns</td></tr><tr><td>SSP</td><td>Software that publishers use to make their ad inventory available to many potential buyers (generally DSPs) as possible in an auction formatTypically applies rules and works towards the goal of maximizing revenue for each impression</td></tr><tr><td>Mediation</td><td>Software that publishers use to connect to multiple SSPs, compare their bids or expected value, and serves the best-paying adGenerally compare bids in real time auction format rather than in series (i.e. waterfall) as in the past</td></tr><tr><td>Publishers</td><td>Companies aiming to show ads inside their app, site, or service for profitIn this market, typically app-based businesses or those with an app</td></tr></table>

## There Are Many Players Across Public/Private Markets, With Many Filling Multiple Roles

## Advertisers

![](images/704b3b70f01490ab4e95fd2e180439ed64639c454adf0fdf25bc8edc34b48c68.jpg)

SCOPELY

Quince

![](images/bed9badb57f2c09d1c31e3f609e22ee1864d6a66a52a006d7a6a30c78243febb.jpg)

zynga®

dream

![](images/df70f67f44b8e7c192776898423d0e35fccb3928b3d179626ceb1b618f6c2b5e.jpg)

Booking.com

## Publishers

WSJ

![](images/db0db2f631d1ff3b800d89307571c8db497769388b77d8d38be1daa9a2867fb8.jpg)

NATIONAL GEOGRAPHIC

NETFLIX

![](images/77c5ec000c5c777c73963f201fd3deb8833d7cc67acb4fcd121cdd4f9c9a1321.jpg)

TRAVEL+ LEISURE

The New York Times

## Mediation

![](images/a66ec1c38def4b2bd0a3e7ce2004128ea6e0a1b28797a422aa62a3a03f39375b.jpg)

APPLOVIN

![](images/625a2d93799e9d0f3701be6b87ef924e8665f0b96829bd0ad0080c42cae5f902.jpg)

Unity®

Google

![](images/df9ab03bda5bd751eab59fa8e54f3095225ce6c7e0732d9d66e55c9854e81d10.jpg)

PubMatic

InmOBI™

CloudX

## DSP

![](images/7af7dd11b44bb27f570bc3adf9851106cc5782f9aa923752e3e56792cf31480e.jpg)

theTradeDesk

![](images/6953a0be4812be61d85b28da39d7c6a92d4b4021d21c875e33e49b88c239913f.jpg)

Unity®

dataxu

CRITEO

![](images/c1afc1fee9d72085d1678d02cd306e17222b85e65aabccb360006d7308450723.jpg)

APPLOVIN

xandr

![](images/ac4f0414b7c28a8d301da6be7eab8f78eae634082cee8c00f8501574ad710c04.jpg)

Meta

![](images/74c766ed58ddcf0e48bb8cf84c9370bf3989f76c726e6c6fcef0a59382e759c6.jpg)

AMOBEE

Google

Oath:

InmOBI

![](images/b775b12e279e44993d2ddb2cdda7c3cc25e060c550e72f6cfc2f42331004973d.jpg)

Adobe

MOLOCO adform

amazonadvertising

## SSP

SPOTX

![](images/5104866f16550d59ab3358476d1dfcac4c7862e5fcbce263791817c596caf28e.jpg)

APPLOVIN

Magnite

![](images/156ae568810e4336f98a071a74e6c2bcd80bf7d06eedaf241198e4654f3a244d.jpg)

xandr

![](images/b674dd1498ca90b6bc004e2c5a34a8643284389ae3646c563df3624ffd04dc6b.jpg)

Unity

![](images/f67097695e22d189d14e113122c336834d29c5b111f52c6ad73780d500b04089.jpg)

AppNexus

![](images/a1d10a0bfcd1aa85744ba2fffa005554657fa07c89cd204d737f9ae13e64df40.jpg)

OpenX

CloudX

Mintegral

Google

InmOBI

MOLOCO

## In a Classical Example, Advertisers Execute Campaigns via DSPs, Which Bid into Auctions Run by SSPs on Behalf of Publishers

![](images/9f7123307106a273c30cc08f7086b9340a684467df581b99250fc5b4b1c59c13.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Advertisers"] --> B["DSP"]
  B --> C["Bidding"]
  C --> D["SSP"]
  D --> E["Placement"]
  E --> F["Winning Bid & Ad Position Determined"]
  F --> G["Publishers"]
  G --> H["Consumer Audience 1"]
  G --> I["Consumer Audience 2"]
  G --> J["Consumer Audience 3"]
  G --> K["Consumer Audience 4"]
```
</details>

## Mediation Tools Allow Publishers to Work with Multiple SSPs or Ad Networks at Once, With the Goal of Maximizing the Value of Publishers' Ad Inventory

SSP/Ad Network #1  
![](images/c03cc60a7eb692ca796caebfe2611e1c6b83a9b760713aa704cf6929a306c7cb.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Advertisers"] --> B["DSP"]
  B --> C["Bidding"]
  C --> D["SSP"]
  D --> E["Placement"]
  E --> F["Winning Bid & Ad Position Determined"]
  G["Ad Creative Likely Personalized Based on 1P/3P Targeting and Audience Data"] --> F
```
</details>

SSP/Ad Network #2  
![](images/b5fbe776853aa957fce24d2addb84631dd48413bba312c900d6379184cdc83ef.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Advertisers"] --> B["DSP"]
  B --> C["Bidding"]
  C --> D["SSP"]
  D --> E["Placement"]
  E --> F["Winning Bid & Ad Position Determined"]
  G["Ad Creative Likely Personalized Based on 1P/3P Targeting and Audience Data"] --> F
```
</details>

SSP/Ad Network #3  
![](images/b5d6357045f7575c1d9372fef0d59c80f56dbac68c8102815e0e06417088a0d6.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Advertisers"] --> B["DSP"]
  B --> C["Bidding"]
  C --> D["SSP"]
  D --> E["Placement"]
  E --> F["Winning Bid & Ad Position Determined"]
  G["Ad Creative Likely Personalized Based on 1P/3P Targeting and Audience Data"] --> F
```
</details>

![](images/a767a77e128c73e30e3ee366f4ea99c36969cd7ee824bb05bec6b642b877d491.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Mediation"] --> B["Publishers"]
  C["Consumer Audience 1"] --> B
  D["Consumer Audience 2"] --> B
  E["Consumer Audience 3"] --> B
```
</details>

## The Majority of the Unit Economics Accrue to Publishers, with DSPs and SSPs Capturing Most of the Remainder

![](images/92901ea2d1959a7b555de22e2bf9245f22c38de9183b0a4cbf37c4d592cd7472.jpg)

<details>
<summary>flow diagram</summary>

| Category               | Value   |
| ---------------------- | ------- |
| Advertisers & Agencies  | $3.00 CPM |
| DSP                    | $0.45   |
| SSP                    | $0.45   |
| Mediation              | $0.06   |
| Publishers             | $2.04   |
</details>

## Any Other Potential Fees?

- Ad servers  
• Data management platforms (estimated 1-2% but can be included within the DSP take rate)  
• Digital media analytics fees are paid separately by the advertiser (i.e. not a percentage of CPM)

## Intro to Mobile Ad Tech

![](images/de61191e96decb66e93de113a2db1d687fd28533074f5b85b8e0bc777acaf987.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["1\nMobile Ad Tech Ecosystem Overview"] --> B["2\nSustainability Of Growth"]
  B --> C["3\nCompetition"]
  C --> D["4\nImpact of AI"]
  D --> E["5\nSignal/Privacy & Platform Risk"]
```
</details>

## Introduction: Sustainability of Growth

## What Is The Debate?

- Broadly speaking, there is debate around how much room there is for further growth in mobile advertising, including improvement in existing unit economics or performance, expansion into new verticals, and exposure to macroeconomic pressure.  
- Specifically, this includes discussion of how high advertisers can raise take rates and conversion rates, which directly impacts potential growth in revenue for ad tech players.  
- Debate has also centered on how scalable ecommerce and other verticals outside of in-game advertising are.

## What's Changing?

- Recent initiatives from ad platforms to expand beyond core in-game advertising and into web and e-commerce have driven debate around the durability and scale of these new verticals  
- Potential entry of larger platforms into in-game advertising has raised questions regarding the sustainability of conversion rates and take-rate expansion for incumbent players. Separately, there is investor focus on exposure to broader macroeconomic headwinds and potential cyclicality.

## Why Does It Matter?

- Take rates and conversion rates are key drivers of monetization efficiency for platforms and directly impact revenue. Improvement in these metrics signals stronger advertiser ROI and platform pricing power, while any degradation may indicate rising competition or weakening demand quality.  
- Expansion beyond in-game advertising could meaningfully increase TAM, supporting higher long-term revenue and margin growth

## Who Is Primarily Impacted?

- Potential Beneficiaries: APP, U, and other players that can meaningfully scale into new verticals while improving conversion rates.  
- Potentially At Risk: Existing ad platforms in new verticals that fail to outperform other players on conversion rates or advertiser-specific performance metrics (ROAS, etc.).

## Higher Conversion Rates Allow Ad Tech Companies to Increase Their Take Rates and Net Revenue...

## What Are Conversion Rates and Take Rates? Why Do They Matter?

- Click Through Rates: the portion of users that click on an ad after viewing it  
- Conversion Rates: the portion of ad impressions (clicks) that result in a desired outcome (app install, purchase, etc.)  
- “Take Rates”: The share of advertiser spend captured by the ad platform, contributing to net revenue for the platform  
• Media Spend: Spend by the ad platform to win placements and impressions to result in one conversion

## Total Impressions:

Users who view the ad

x Click Through Rate

## Total Engagement:

Users who interact with the ad

x Conversion Rate

## Conversions

Users Who Complete

The Desired

Outcome

- Higher conversion rates result in better campaign efficiency, increasing the value of each impression. If conversion rates improve, the ad platform needs fewer impressions to deliver the same number of installs.  
- Improved conversion lowers effective CPI for the ad platform by lowering the number of impressions needed to result in one conversion. If advertiser spend remains stable, the platform keeps a larger spread between spend and inventory cost.

## ...Presenting a Growth Opportunity that Is Separate from Growth in Total Ad Dollars Spend by Advertisers

Improved Conversion Rates Can Improve The Effective “Take Rate” Of An Ad Platform, Increasing Net Revenue Without Relying on Change in Advertiser Spend. With higher conversion rates, Ad platforms need to buy less impressions to results in one conversion.

If It Takes 20 Ad Impressions To Generate One App Install Today......  
![](images/50db8af23e56c95e57fc01fcddd83cdcfb87e4d22e1de630abb53dd32e928582.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Advertiser offers $10 per App Install"] --> B["Ad Platform Spends $8 On Ad Impressions"]
  B --> C["Ad Platform Shows 20 Impressions"]
  C --> D["Impressions Lead to an Install"]
  D --> E["Platform Keeps $2 20% “Take Rate”"]
  F["$2\nNet Revenue\n$8\nMedia Spend"] --> G["$2\nNet Revenue\n$8\nMedia Spend"]
```
</details>

...An Improvement To 15 Impressions Per Install Would Lead "Take Rate" To Double  
![](images/c9ac2c912f29a7dedc431260ac23416c43c757af71cb8014c16c80a03a516146.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Advertiser offers $10 per App Install"] --> B["Ad Platform Spends $6 On Ad Impressions"]
  B --> C["Ad Platform Shows 15 Impressions"]
  C --> D["Impressions Lead to an Install"]
  D --> E["Platform Keeps $4 40% “Take Rate”"]
  F["$4 Net Revenue"] --> G["$6 Media Spend"]
```
</details>

## We Estimate Leading Platforms Like META Enjoy “True” Conversion Rates \~10x Above APP’s, Suggesting Significant Headroom Even If APP’s Rates Never Reach META’s

## META Conversion Rates are \~10x Those of APPs, Representing Significant Potential Upside to APP Revenue If Conversion Rates and Platform Performance Continue to Improve

APP

<table><tr><td>% of Ads that Generate an App Install</td><td>1.3%</td></tr><tr><td>x In-Game Paying Ratio</td><td>2.0%</td></tr><tr><td>= &quot;True&quot; Conversion Rate</td><td>0.026%</td></tr></table>

META

<table><tr><td>Click-Through Rate

[中间内容因长度限制已省略]

 preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## Disclosure Section (cont.)

INDUSTRY COVERAGE: Internet

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/04/2026)</td></tr><tr><td colspan="3">Brian Nowak, CFA</td></tr><tr><td>Airbnb Inc (ABNB.O)</td><td>U (12/06/2022)</td><td>$133.72</td></tr><tr><td>Alphabet Inc. (GOOGL.O)</td><td>O (08/11/2015)</td><td>$372.19</td></tr><tr><td>Amazon.com Inc (AMZN.O)</td><td>O (04/24/2015)</td><td>$253.79</td></tr><tr><td>Booking Holdings Inc (BKNG.O)</td><td>O (02/23/2026)</td><td>$167.49</td></tr><tr><td>DoorDash Inc (DASH.O)</td><td>O (02/21/2024)</td><td>$160.07</td></tr><tr><td>Expedia Inc. (EXPE.O)</td><td>E (01/09/2019)</td><td>$227.18</td></tr><tr><td>Instacart (CART.O)</td><td>E (01/29/2024)</td><td>$41.48</td></tr><tr><td>Lyft Inc (LYFT.O)</td><td>E (10/24/2019)</td><td>$14.12</td></tr><tr><td>Meta Platforms Inc (META.O)</td><td>O (03/20/2023)</td><td>$627.57</td></tr><tr><td>Pinterest Inc (PINS.N)</td><td>O (07/20/2025)</td><td>$21.59</td></tr><tr><td>Reddit Inc (RDDT.N)</td><td>O (12/08/2024)</td><td>$183.91</td></tr><tr><td>Snap Inc. (SNAP.N)</td><td>E (07/22/2024)</td><td>$6.07</td></tr><tr><td>Uber Technologies Inc (UBER.N)</td><td>O (06/04/2019)</td><td>$72.21</td></tr><tr><td colspan="3">Matthew Cost</td></tr><tr><td>AppLovin Corp (APP.O)</td><td>O (04/10/2025)</td><td>$558.87</td></tr><tr><td>Compass, Inc. (COMP.N)</td><td>E (01/12/2026)</td><td>$7.88</td></tr><tr><td>Criteo SA (CRTO.O)</td><td>E (01/26/2016)</td><td>$17.29</td></tr><tr><td>DoubleVerify Holdings Inc (DV.N)</td><td>E (06/25/2024)</td><td>$10.57</td></tr><tr><td>Electronic Arts Inc (EA.O)</td><td>E (08/04/2021)</td><td>$203.40</td></tr><tr><td>MNTN Inc (MNTN.N)</td><td>E (06/16/2025)</td><td>$9.69</td></tr><tr><td>Opendoor Technologies Inc (OPEN.O)</td><td>E (07/24/2023)</td><td>$4.95</td></tr><tr><td>Playtika Holding Corp (PLTK.O)</td><td>E (11/27/2022)</td><td>$3.15</td></tr><tr><td>Roblox Corporation (RBLX.N)</td><td>O (11/04/2024)</td><td>$43.35</td></tr><tr><td>Shutterstock Inc (SSTK.N)</td><td>E (07/28/2022)</td><td>$13.19</td></tr><tr><td>Take-Two Interactive Software (TTWO.O)</td><td>O (02/01/2018)</td><td>$216.65</td></tr><tr><td>Trade Desk Inc (TTD.O)</td><td>E (09/10/2025)</td><td>$21.03</td></tr><tr><td>Unity Software Inc (U.N)</td><td>O (09/02/2024)</td><td>$30.03</td></tr><tr><td>Webtoon Entertainment Inc (WBTN.O)</td><td>E (07/22/2024)</td><td>$11.66</td></tr><tr><td>Yelp Inc (YELP.N)</td><td>U (01/10/2019)</td><td>$23.63</td></tr><tr><td>Zillow Group Inc (Z.O)</td><td>E (04/18/2018)</td><td>$35.92</td></tr><tr><td colspan="3">Nathan Feather</td></tr><tr><td>Bumble Inc. (BMBL.O)</td><td>E (03/08/2021)</td><td>$2.99</td></tr><tr><td>Chewy Inc (CHWY.N)</td><td>O (10/31/2023)</td><td>$20.82</td></tr><tr><td>Duolingo Inc (DUOL.O)</td><td>E (02/27/2026)</td><td>$109.15</td></tr><tr><td>eBay Inc (EBAY.O)</td><td>O (04/18/2024)</td><td>$109.15</td></tr><tr><td>Etsy Inc (ETSY.N)</td><td>E (07/20/2025)</td><td>$67.05</td></tr><tr><td>FIGS, Inc. (FIGS.N)</td><td>E (02/29/2024)</td><td>$11.70</td></tr><tr><td>Grindr Inc. (GRND.N)</td><td>E (02/24/2026)</td><td>$10.70</td></tr><tr><td>Match Group Inc (MTCH.O)</td><td>E (04/18/2024)</td><td>$34.76</td></tr><tr><td>Peloton Interactive, Inc. (PTON.O)</td><td>E (03/14/2022)</td><td>$6.17</td></tr><tr><td>Revolve Group Inc (RVLV.N)</td><td>E (10/20/2024)</td><td>$19.33</td></tr><tr><td>WW International Inc (WW.O)</td><td>E (08/01/2025)</td><td>$17.27</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## The Americas

1585 Broadway

New York, NY 10036-8293

United States

+1 212 761 4000

## Europe

20 Bank Street, Canary Wharf

London E14 4AD

United Kingdom

+44 (0)20 7425 8000

## Japan

1-9-7 Otemachi, Chiyoda-ku

Tokyo 100-8104

Japan

+81 (0) 3 6836 5000

## Asia/Pacific

1 Austin Road West

Kowloon

Hong Kong

+852 2848 5200
"""
