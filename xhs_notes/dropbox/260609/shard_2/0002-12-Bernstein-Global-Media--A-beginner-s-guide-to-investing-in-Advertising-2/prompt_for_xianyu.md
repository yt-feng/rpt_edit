你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
## Global Media

# Global Media: A beginner's guide to investing in Advertising

![](images/926308b3278039d0720ea336ed935311e223280fe4e76558ef69c2ac6a15fcf4.jpg)  
Annick Maas

+44 20 7676 6683

annick.maas@bernsteinsg.com

![](images/2819577ee4c0242fc0e917eada851d9991d1261a73ef846ec841ce6df3ef5d3d.jpg)  
Christophe Cherblanc

+41 582 723 540

christophe.cherblanc@bernsteinsg.com

![](images/cab9428688dc3c7833fdbe250f867785d7fcf229587e3c086f1b52d2c4b1e5cf.jpg)  
Mark Shmulik

+1 917 344 8508

mark.shmulik@bernsteinsg.com

![](images/f9504084ee8fdd3cff0d9d79d710dee37f76f6c7f6f11cf226eed4e8d5018faa.jpg)  
Laurent Yoon

+1 917 344 8502

laurent.yoon@bernsteinsg.com

![](images/ed382a0c394d98db8749613d0c2ee4d35c0eddc6fff8d63399243eebe16b72c3.jpg)  
Nikhil Devnani, CFA

+1 917 344 8425

nikhil.devnani@bernsteinsg.com

Advertising is totally unnecessary. Unless you hope to make money." - Jef I. Richards

Following on from “A beginner's guide to investing in Media” published last year, we are focusing this year on the sub-sector Advertising. From traditional media owners, over agencies, ad tech and martech to the big digital platforms, combined this ever evolving industry is worth \$1trn globally. We look into the various sub-sectors, what KPIs to look into, the share price drivers and how the US/European markets compare/contrast.

The key structural insight: advertising growth is driven by redistribution, not consumption expansion. Global media consumption has plateaued at \~11 hours per day, constraining total inventory growth and implying intensifying competition for attention. Rather than structural volume expansion, value is shifting across formats and platforms, with digital now accounting for over two-thirds of global ad spend. This fragmentation increases execution complexity and raises the premium on scale, targeting, and measurement—favouring large digital platforms with superior data ecosystems

## Two distinct advertising markets underpin diverging growth and risk profiles.

Market #1 (agencies, traditional media) is concentrated, cyclical, and dependent on a few thousand large clients; spend is volatile and often the first cost to be cut in downturns. Market #2 (digital platforms) is driven by millions of SMEs, structurally more resilient, and less predictable from top-down indicators. Our data shows SME-driven revenues account for roughly two-thirds of major platform ad revenues, highlighting a fundamentally different growth engine. This distinction is often underappreciated by the market and explains persistent outperformance of platform-led models.

## Digital advertising growth remains intact, but is evolving into a second phase.

The first phase was driven by SME onboarding and self-serve tools; the second phase (since \~2023) is driven by inventory expansion (retail media, marketplaces, OTT) and personalisation at scale. Retail media in particular represents structurally high-margin, near-zero-cost inventory with strong targeting advantages, benefiting platforms like Amazon and delivery ecosystems. AI acts as an accelerant—enhancing targeting, creative generation, and conversion—while reinforcing the competitive moat of scaled platforms

## Traditional players are adapting—but the mix shift remains insufficient.

Broadcasters, OOH, and agencies are successfully replicating digital characteristics (e.g., ITVx, VIOOH), achieving higher growth in these segments. However, these businesses still represent a small proportion of group revenues, limiting their impact on overall growth and valuation. Meanwhile, core linear advertising continues to decline in markets like the US, with DTC growth only partially offsetting the gap. High client concentration and cyclical exposure further weigh on investment appeal.

## Table Of Contents

How to think about Global Advertising Categorisations....2

Revenue model - A volatile ride, but it is worth it....3

The exchange and free rider model....4

From digital transition to digital fragmentation in advertising....4

Digital advertising growth formula....6

Advertising - It is not all the same - market #1 emulates market #2 successfully....7

This drives some conclusions, which we believe are essential to consider when looking at the advertising market:....9

Complexity - Fragmentation - Data transparency....11

Regulation & Measurement....12

Advertising and AI....13

The Advertising Sub-Sectors....14

Free-to-Air and pay tv in transition....14

Transition from Linear Advertising to DtC Advertising in the US....15

Outdoor Advertisers....19

Advertising Agencies....21

Classifieds....23

Ad Tech....24

Social media....25

Marketplaces....26

Commerce Advertising / Retail Media....27

## DETAILS

## HOW TO THINK ABOUT GLOBAL ADVERTISING CATEGORISATIONS

\- Traditional Advertising: The term traditional media typically refers to the advertising channels that were around before the emergence of the digital advertising era. Traditional advertising sub-sectors include free-to-air broadcasters, outdoor advertisers (e.g. billboard advertising companies), radio and newspapers, although the latter are no longer listed as standalone categories

\- Digital Advertising: Digital advertising encompasses the sub-sectors that have emerged with the rise of the internet. It is a very wide wrapper that includes anything from digital advertising video on demand, classifieds, marketplaces, ad tech companies and the FAANGs.

Beyond the traditional/digital dissection, advertising can be split in the following four categories.

\- Big digital platforms: search, social, video platforms - essentially consumer platforms that aim to sell targeted advertising at scale.

\- Search engines: platforms that monetize intent via keyword auctions and other advertising products.

- Social networks: stories, short-form video and feeds that are monetized via native advertising formats.  
• Video platforms: these platforms include long and short-form videos with in-stream, in-feed, and sponsorship formats.  
- Marketplaces and retail media: e-commerce and marketplace platforms selling on-site search/display and sponsored advertising/listings.

\- Traditional media owners: TV broadcasters, outdoor advertising, print, radio and their digital extensions - these companies monetize their audiences as they sell advertising space alongside their content.

• TV and streaming: broadcasters, cable/satellite networks, and AVoD platforms.  
- Out-of-home (OOH): traditional/digital billboards, street furniture, transport advertising networks.  
- Print: newspapers, magazines, and digital news' groups monetizing their audiences via advertising.  
- Audio: radio and digital audio platforms (i.e. streaming music) that have ad-supported tiers.  
- Thematic/specialist publishers: niche websites, trade media, and other information portals monetizing via display advertising.

\- Agencies/holding groups: This category includes advertising/media agencies that plan, buy, create and execute media campaigns for brands; they take a fee or margin on ad spend.

- Holding companies: The likes of WPP, Publicis, Omnicom. They manage diversified networks offering creative, media, PR, and other data/consulting services.  
- Specialist agencies: These tend to be focused on particular verticals (healthcare, performance, influencer, etc.).  
- Digital-first performance agencies: Agencies that tend to focus on all things digital and data-driven i.e. programmatic, search, social, CRM, and data-driven performance marketing.

\- Ad tech and martech: demand-side platforms (DSPs), supply-side platforms (SSP), measurement, data, and marketing-automation providers that enable digital advertising. These tend to be softwares that sit between the advertisers and the media owners and take a cut on the spend.

- Demand-side platforms (DSPs): tools advertisers and agencies use to buy advertising inventory on exchanges.  
• Supply-side platforms (SSPs): platforms that help media owners to monetize inventory via auctions.  
- Ad servers: They manage ad delivery and frequency for web and in-app inventory.  
- Attribution and measurement: Platforms that track and attribute advertising posts and conversion rates.  
- Verification and brand safety: viewability, fraud detection and brand suitability.  
- Connected TV/OTT ad platforms: marketplaces that allow seamless booking/buying of streaming video ad inventory.

## REVENUE MODEL - A VOLATILE RIDE, BUT IT IS WORTH IT

Advertising powered revenue models are dominant in the media sector. An advertising revenue model has the following features:

- Advertising is typically viewed as being early cycle as it (arguably counter intuitively) is the first expense that companies cut when the macro environment deteriorates. It tends to show a correlation with consumer confidence KPIs. We’d argue that exactly in these pressure moments it is crucial to invest in advertising to support brand strength and, over the long term, a company’s valuation.  
- Advertising revenues are therefore relatively volatile, with DD quarterly swings in stressed macro conditions.  
- As a rule of thumb, one can assume that most advertising-driven businesses are consumer-facing.  
- The overall advertising world has been benefitting from a mix shift to digital, which tends to grow quicker than traditional advertising. Over the last decade advertising spend has aggregated around a few platforms only.  
- Advertising is all about scale. The more a platform is scaled the higher advertising prices it can command. Advertising is paid generally by CPM/CPT in other words one is paying to have access to 1000 impressions.

## THE EXCHANGE AND FREE RIDER MODEL

Most advertising models provide something in exchange to be able to charge advertising. For example, free-to-air broadcasters provide content (TV shows and films) in exchange for advertising breaks that allow them to collect revenues. Outdoor advertisers provide bus shelters and billboards that allow councils to display community messages in exchange for being able to place advertising on these panels as well. News portals provide content/information and display advertising alongside to pay for it.

Then there are the free riders. For example, the leading classified players, which can display cars for sale and have car dealers pay to be able to place these listings (the content in this case) on the website. These types of firms consistently exhibit very high margins across many geographies. This is the by-product of enjoying a content supply paid for by external contributors (the ultimate sweet spot for a “media” business!). This is also the case for social media platforms enjoying free user-generated content.

## FROM DIGITAL TRANSITION TO DIGITAL FRAGMENTATION IN ADVERTISING

In the last 25 years the media sector has been dominated by the digital transition theme. This digitalisation has led to the disruption of some business models, higher capex/opex spend and, ultimately, to the emergence of new companies. The world's biggest advertising firms have only appeared in the last two decades. Today >2/3rds of global advertising revenues are coming from Digital.

EXHIBIT 1: Digital vs Traditional ad spending growth worldwide, 2020-2026  
![](images/3ffee5918793808ee276b734271007a48672515b50a99a25e2886fe48b42252b.jpg)

<details>
<summary>line chart</summary>

| Year | Digital (%) | Traditional (%) |
| :--- | :--- | :--- |
| 2020 | 15.7 | -16.4 |
| 2021 | 29.5 | 9.8 |
| 2022 | 8.6 | -0.9 |
| 2023* | 10.5 | 0.1 |
| 2024* | 11.0 | 2.2 |
| 2025* | 10.1 | 0.6 |
| 2026* | 9.1 | 1.6 |
</details>

digital includes advertising that appears on desktop and laptop computers as well as mobile phones, tablets, and other internet-connected devices, and includes all the various formats of advertising on the platforms; traditional includes TV, magazines, newspapers, out-of-home, and radio

\* Forecast

Source: eMarketer

EXHIBIT 2: Digital advertising spending worldwide from 2021 to 2026 (in billion U.S. dollars)  
![](images/c1eac432ebdf8c9ec467d020c9604c9ca5b05e5b69f04595c0d3a659c164ab9d.jpg)

<details>
<summary>bar chart</summary>

| Year | Value |
| :--- | :--- |
| 2021 | 522.5 |
| 2022* | 567.49 |
| 2023* | 626.86 |
| 2024* | 695.96 |
| 2025* | 765.98 |
| 2026* | 835.82 |
</details>

includes advertising that appears on desktop and laptop computers as well as mobile phones connected devices, and includes all the various formats of advertising on those platforms

\* Forecast

Source: eMarketer, PubMatic

EXHIBIT 3: Digital ad spending worldwide, 2021-2026 (in billions)  
![](images/2b697c4ac2ec4cf681d2e97cb62578ce46429978e1886f195b2f4510242561c8.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | Digital ad spending | % change |
|------|---------------------|----------|
| 2021 | $523                | 30%      |
| 2022 | $567                | 9%       |
| 2023 | $627                | 10%      |
| 2024 | $696                | 11%      |
| 2025 | $766                | 10%      |
| 2026 | $836                | 9%       |
</details>

includes advertising that appears on desktop and laptop computers as well as mobile phones, tablets, and other internet-connected devices, an includes all the various formats of advertising on the platforms; excludes SMS, MMS, P2P messaging-based advertising

Source: eMarketer

Digital ad growth has remained robust. There are three key reasons why Digital ad growth has continued to defy expectations, even though its share of the total ad market is maturing and user time spent on media is stabilizing.

- Commercial activity continues to migrate online. Globally ex-China, e-commerce penetration of total retail is in the mid-teens. Given that digital advertising is more measurable than analogue and often tied directly to a conversion event, there's a strong correlation between digital ad spend growth and e-commerce growth rates.  
- Time spent shift to digital channels. While slowing, time spent with media continues to shift from traditional to digital channels. For example Connected TV have reached a tipping point with YouTube now the most watched TV channel in the US.  
- AI improvements to advertising performance. In no field outside of coding/engineering has the impact of AI been more pronounced than in digital advertising. Not only have algorithms made it easier for advertisers to target their ads and send the right message to the right person at the right time, regardless of their campaign objective, but generative AI is now driving a shift in advertising creation.

## DIGITAL ADVERTISING GROWTH FORMULA

## Online ad growth = Volume (penetration/usage) x Price (auction based) x New clients (2/3s SMEs)

The two stages of digital advertising growth:

Stage 1: In this stage, which has dominated the last decade, we saw digital growth driven by SMEs as they were enjoying newfound self-service communications capabilities. To put this statement into context, SMEs actually account for two-thirds of online mega caps Alphabet and Meta's ad revs.

Stage 2: This phase started in 2023, with the accelerated expansion of media inventory (retail media, marketplaces, delivery apps, OTT platforms). Combined with emerging personalisation-at-scale opportunities, this creates the once unthinkable opportunity for larger advertisers to move more fluidly up and down the marketing funnel. Redefining the marketing funnel, with Retail Media exploiting free ad inventory at scale is a major opportunity for what were originally ‘non-media’ companies (retailers, apps, marketplaces).

EXHIBIT 4: Only four of today's top 10 most valuable digital companies existed prior to 2000

<table><tr><td></td><td>Est. brand value in 2026</td><td>Launch year</td></tr><tr><td>Google</td><td>$1,484bn</td><td>1998</td></tr><tr><td>Facebook</td><

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
