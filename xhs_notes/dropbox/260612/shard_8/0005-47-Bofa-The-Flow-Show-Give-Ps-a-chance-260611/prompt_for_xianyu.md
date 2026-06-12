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
# The Flow Show

# Give Ps a chance

Scores on the Doors: oil 50.4%, intl stocks 9.3%, SPX 8.0%, cash 1.6%, US\$ 1.5%, HY bonds 1.5%, IG bonds 0.1%, govt bonds -1.3%, gold -2.9%, bitcoin -27.5% YTD.

Zeitgeist: “...all that, plus the Knicks as Champs, I mean you couldn’t script a better top.”

The Price is Right: 3Ps of bullish Positioning, bullish Profit expectations, Policy flipping from rate cuts to hikes...keep taking trading chips off table until tighter financial conditions peak once Warsh turns hawkish at the July $29^{\text{th}}$ FOMC.

Tale of the Tape: inflation >4%, Trump inflation approval @ 27% (below Biden lows - Chart 4), US oil inventories down to 48 days (close to 45-year lows – Chart 5), policy maker conviction best route to “America First” via “Wall Street First”...why rush to end US-Iran conflict; best contrarian “peace” winners...consumer stocks, REITs (new highs this week), Europe, deleveraged crypto & gold, EM FX esp. India, Indonesia.

The Biggest Picture: booms & bubbles ended by bonds (punitive cost of capital), leaders (not a good look if “cheap” MAGS can’t hold \$65), or elections (voters wanting more jobs or lower inflation); we’re getting there...but for now asset allocation frozen bullish, positioned for late-cycle greed, not at all tempted by 5% yields at the long-end (BofA private client exposure to UST bonds >10-year duration tiny 4% - Chart 2).

Chart 2: Private clients rotating from T-bills to T-notes, but interest in T-bonds  
BofA private client % allocation within US Treasuries  
![](images/436be8e8f90f6b7ae0387895717d84656352c356764fdab42acf0f8cda8652e9.jpg)

<details>
<summary>line chart</summary>

| Year | T-notes | T-bills | T-bonds |
|------|---------|---------|---------|
| '05  | 65%     | 25%     | 10%     |
| '07  | 60%     | 30%     | 10%     |
| '09  | 48%     | 40%     | 12%     |
| '11  | 68%     | 20%     | 10%     |
| '13  | 60%     | 30%     | 12%     |
| '15  | 60%     | 25%     | 15%     |
| '17  | 55%     | 35%     | 12%     |
| '19  | 45%     | 50%     | 8%      |
| '21  | 35%     | 55%     | 10%     |
| '23  | 30%     | 65%     | 2%      |
| '25  | 45%     | 50%     | 2%      |
| '27  | 49%     | 47%     | 4%      |
</details>

Source: BofA Global Investment Strategy. T-bills: 4-52 weeks, T-notes: 2-10 years, T-bond: 20-30 years  
BofA GLOBAL RESEARCH

More on page 2...

## 11 June 2026

Investment Strategy

Global

BofA

Data

Analytics

![](images/06b231837a772ed35a3b7c270d861393a6390ddbe4988d7c56e3d52d2ccd7b61.jpg)

Michael Hartnett

Investment Strategist

BofAS

+1 646 855 1508

michael.hartnett@bofa.com

Anya Shelekhin

Investment Strategist

BofAS

+1 646 855 3753

anya.shelekhin@bofa.com

Myung-Jee Jung

Investment Strategist

BofAS

+1 646 855 0389

myung-jee.jung@bofa.com

Jessica Guo

Investment Strategist

BofAS

+1 646 855 0033

jessica.guo@bofa.com

Chart 1: BofA Bull & Bear Indicator  
Up to 8.8 from 8.7  
![](images/5fa2da422c077e92e8e01665d6a75c6e459191d6708258f93d936d7767744472.jpg)

<details>
<summary>gauge chart</summary>

| Category | Value |
|---|---|
| Extreme Bearish | 2 |
| Buy | 6 |
| Sell | 8.8 |
| Extreme Bullish | 10 |
</details>

Source: BofA Global Investment Strategy. The indicator identified above as the BofA Bull & Bear Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 12 to 14.

12983719

Weekly Flows: \$31.5bn to stocks, \$20.8bn to bonds, \$0.7 from crypto, \$2.3bn from gold, \$2.5bn from cash.

## Flows to Know:

- Crypto: \$0.7bn outflow, past 5 weeks \$6.6bn outflows...record (Chart 9),  
• Gold: \$2.3bn outflow, 4 $^{th}$ week of outflows (Chart 10),  
- IG bonds: \$11.8bn inflow, $10^{\text{th}}$ week of inflows,  
- US equities: \$17.4bn inflow, 11 $^{th}$ week of inflows...longest streak since Dec'25,  
• EM equities: \$4.5bn inflow, 1 $^{st}$ inflow in 9 weeks (Chart 11),  
- Korea equities: \$5.9bn inflow, biggest inflow since Mar'26,  
- Tech: \$12.3bn inflow, biggest weekly inflow ever (incl \$3.0bn to Direxion Daily Semiconductor Bull 3x and \$2.9bn to iShares Semiconductor ETF – Chart 12).

BofA Private Clients: \$4.5tn AUM...65.5% stocks, 17.4% bonds, 9.8% cash; biggest outflow from equities in 8 weeks but note GWIM equity ETF share count up 0.3% past week and 4.9% YTD, shows underlying equity buying; in ETFs past 4 weeks, private clients buying materials, MLP, TIPS and selling Japan, staples, utilities.

BofA Bull & Bear Indicator $^{1}$ : rises to 8.8 from 8.7 as strong tech equity inflows partially offset by HY and EM bond outflows and weaker global stock index breadth; 4th week of “sell signal” triggered May'26; 17 "sell signals" since '02, average loss for global stocks over 2-3 months is 2-3%, hit ratio of \~60%, max drawdowns of 15-20% (see BofA Bull & Bear Indicator).

1994 analog: US headline CPI (avg 0.5% past 6 months) heading above 5% by midterms (Chart 6 - core CPI on course for 3.0-3.5%); past 100 years when CPI crossed above 4%, SPX averaged -4% next 3 months, -7% next 6 months; US CPI (4.2%) almost higher than unemployment rate (4.3%), rare and tends to coincide with years of Fed hikes (e.g., '66, '73, '90, '00, '08, '21 – Chart 7), none of which remembered fondly on Wall St; market analogs galore, but don't forget 1994 analog which has parallels with 2026...extended Fed easing and jobless recovery in early '90s ended with blowout payrolls in Q1'94 forcing big hikes from behind-the-curve Fed, stocks stumbled into multi-month trading range until bond yields stopped rising after deleveraging Mexico peso crisis & Orange County bankruptcy events in Dec'94 (Chart 8).

Chart 3: Deleveraging in gold  
Gold spot price (\$/oz)  
![](images/da1bf783a6951578f0ee2117293e1ff1153c5136dddadc2fc91321346118e767.jpg)

<details>
<summary>line chart</summary>

| Year | Gold spot price ($/oz) |
| ---- | ---------------------- |
| 1960 | ~$0                   |
| 1970 | ~$0                   |
| 1980 | ~$500                  |
| 1990 | ~$500                  |
| 2000 | ~$500                  |
| 2010 | ~$2,000                |
| 2020 | ~$3,000                |
| 2023 | ~$5,500                |
</details>

Source: BofA Global Investment Strategy, Bloomberg, GFD Finaeon  
BofA GLOBAL RESEARCH

Chart 5: US oil supply down sharply...and Trump approval at lows  
US crude oil, days of supply, including US SPR  
![](images/4ab6b3423d74ebd428a628c637fd8704ba0d50e5ec32f521bd9a733804c7f165.jpg)

<details>
<summary>line chart</summary>

| Year | US crude oil, days of supply incl. Strategic Petroleum Reserve |
| ---- | --------------------------------------------------------------- |
| '82  | ~50                                                             |
| '86  | ~65                                                             |
| '90  | ~70                                                             |
| '94  | ~65                                                             |
| '98  | ~60                                                             |
| '02  | ~55                                                             |
| '06  | ~75                                                             |
| '10  | ~70                                                             |
| '14  | ~75                                                             |
| '18  | ~85                                                             |
| '22  | ~50                                                             |
| '26  | ~45                                                             |
</details>

Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 7: When u-rate lower than inflation...there be dragons  
US unemployment rate (%) – US headline CPI (YoY %)  
![](images/be59a17d7c284038f4a7a89ae60ee2176560e714e6a7eb94fc583f13b26730f4.jpg)

<details>
<summary>line chart</summary>

| Year | US unemployment rate minus US headline CPI (YoY %) |
| ---- | -------------------------------------------------- |
| Oct'66 | 0 |
| Feb'68 | 0 |
| Apr'73 | 0 |
| Dec'77 | 0 |
| Feb'90 | 0 |
| Mar'00 | 0 |
| Nov'07 | 0 |
| Jul'08 | 0 |
| Jul'21 | 0 |
</details>

Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 4: Trump approval on inflation now below Biden's low  
Biden vs Trump approval ratings on inflation  
![](images/bf1645fc35d76c1eda73f5ec1a64d99e4526fc7b17b1a4d6ac14b56a382a3208.jpg)

<details>
<summary>line chart</summary>

| Year | Biden Approval on Inflation (%) | Trump Approval on Inflation (%) |
|------|----------------------------------|----------------------------------|
| '22  | 28%                              | -                                |
| '26  | 27%                              | -                                |
</details>

Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 6: US CPI on track for >5% by November midterms  
Paths for US CPI assuming pace of monthly change  
![](images/ae067173028b2bb9db643b41fb13e6ea9993fd88562033875596a9119874b826.jpg)

<details>
<summary>line chart</summary>

| Year | 0.1% MoM | 0.2% MoM | 0.3% MoM | 0.4% MoM | 0.5% MoM |
|------|----------|----------|----------|----------|----------|
| '20  | ~2.5%    | ~2.5%    | ~2.5%    | ~2.5%    | ~2.5%    |
| '21  | ~1.5%    | ~1.5%    | ~1.5%    | ~1.5%    | ~1.5%    |
| '22  | ~8.5%    | ~8.5%    | ~8.5%    | ~8.5%    | ~8.5%    |
| '23  | ~6.0%    | ~6.0%    | ~6.0%    | ~6.0%    | ~6.0%    |
| '24  | ~3.5%    | ~3.5%    | ~3.5%    | ~3.5%    | ~3.5%    |
| '25  | ~3.0%    | ~3.0%    | ~3.0%    | ~3.0%    | ~3.0%    |
| '26  | ~4.0%    | ~4.0%    | ~4.0%    | ~4.0%    | ~4.0%    |
| '27  | 3.4%     | 4.0%     | 4.6%     | 5.2%     | 5.9%     |
</details>

Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 8: The 1994 analog  
US 2-year yield vs Fed Funds rate vs S&P 500  
![](images/870d64f7e7ea2e5aa387e19b9bf5c96675351bac28b01e68c2747c36b313a9f0.jpg)

<details>
<summary>line chart</summary>

| Date       | US 2y yield (%) | Fed funds rate (%) | S&P 500 (RHS) |
| ---------- | --------------- | ------------------ | ------------- |
| Feb'94 Fed hike | ~3.5            | ~3.5               | ~3.5          |
| Dec'94 Mexico crisis & Orange County | ~7.5            | ~550               | ~550          |
| Jan'96      | ~4.5            | ~500               | ~650          |
</details>

Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 9: Record \$6.6bn 5-week outflow from crypto funds  
Flows to crypto funds, weekly vs 4wk-ma (\$bn)  
![](images/ef989867036b66825e0ce998e97ddfdd71e27605bf501d02eca275cc83188581.jpg)

<details>
<summary>line chart</summary>

| Year | Crypto fund flows ($bn) | 4-week moving average |
|------|--------------------------|------------------------|
| '26  | -1.5                     | -1.8                   |
</details>

Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 10: Gold funds see $4^{\text{th}}$ week of outflows  
Flows to gold funds, weekly vs 4wk-ma (\$bn)  
![](images/fc118129f43571f41586c6da5c441ad4445f0aeb2b9df1542e3bc94ea5b39751.jpg)

<details>
<summary>line chart</summary>

| Year | Gold flows ($bn) | Gold flows 4-week MA ($bn) |
|------|-------------------|----------------------------|
| '17  | ~0                | ~0                         |
| '18  | ~0                | ~0                         |
| '19  | ~0                | ~0                         |
| '20  | ~0                | ~0                         |
| '21  | ~0                | ~0                         |
| '22  | ~0                | ~0                         |
| '23  | ~0                | ~0                         |
| '24  | ~0                | ~0                         |
| '25  | ~0                | ~0                         |
| '26  | ~-8               | ~-2                        |
</details>

Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 11: First inflow to EM equity funds in 9 weeks  
Flows to EM equity funds, weekly vs 4wk-ma (\$bn)  
![](images/e58b142fb70b60503e82ccee7549d8c780699b9b4584fd9be730d91d032f7a40.jpg)

<details>
<summary>line chart</summary>

| Year | EM equities flows ($bn) | EM equities flows 4-week MA ($bn) |
|------|--------------------------|------------------------------------|
| '26  | -40                      | -10                                |
</details>

Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 12: Record \$12.3bn weekly inflow to tech funds  
Flows to tech funds, weekly vs 4wk-ma (\$bn)  
![](images/8b4dcabc2d771a48466e7c220e829dd6ad53a18918194ecbc24f21b76bfdb1b4.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | Tech flows ($bn) | Tech flows 4-week MA ($bn) |
|------|-------------------|----------------------------|
| '27  | ~12               | ~5                         |
</details>

Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

## Asset Class Flows (Table 1)

Equities: \$31.5bn inflow (\$47.1bn to ETFs, \$15.3bn from mutual funds)

Bonds: inflows past 59 weeks (\$20.8bn)

Precious metals: outflows resume (\$2.3bn)

## Fixed Income Flows (Chart 14)

IG Bond inflows past 10 weeks (\$11.8bn)

HY Bond outflows resume (\$0.2bn)

EM Debt outflows resume (\$0.2bn)

Munis inflows past 8 weeks (\$1.6bn)

Govt/Tsy inflows past 7 weeks (\$5.0bn)

TIPS inflows past 19 weeks (\$0.4bn)

Bank loan inflows resume (\$1.0bn)

## Equity Flows (Table 2)

US: inflows past 11 weeks (\$17.4bn)

Japan: inflows resume (\$0.8bn)

Europe: outflows past 9 weeks (\$3.9bn)

EM: inflows resume (\$4.5bn)

By style: inflows US large cap (\$11.3bn), outflows US small cap (\$1.1bn), US value (\$1.8bn), US growth (\$4.5bn).

By sector: inflows tech (\$12.3bn), com svs (\$1.1bn), financials (\$1.0bn), healthcare (\$0.7bn), outflows real estate (\$0.1bn), utils (\$0.3bn), energy (\$0.6bn), consumer (\$1.4bn), materials (\$2.0bn).

Chart 13: FICC inflows to bank loans, Treasuries, IG Bonds  
Weekly FICC flows as a % AUM  
![](images/cb0d6a55a39550a3f4323e171731e1c433ed4bcb213214353db9fd93f07404d0.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (%) |
|---|---|
| Bank loan | 0.55 |
| Govt/Tsy | 0.30 |
| Corp IG | 0.22 |
| TIPS | 0.21 |
| Money-market | -0.03 |
| Corp HY | -0.03 |
| EM debt | -0.04 |
| Gold & Silver | -0.38 |
| Commodities | -0.38 |
</details>

Source: BofA Global Investment Strategy, EPFR Global

Table 1: Cumulative YTD flows by asset class  
Global flows by asset class, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td><td>YTD %AUM</td></tr><tr><td>Equities</td><td>0.1%</td><td>408,563</td><td>1.4%</td></tr><tr><td>ETFs</td><td>0.3%</td><td>647,758</td><td>4.0%</td></tr><tr><td>LO</td><td>-0.1%</td><td>-239,270</td><td>-1.9%</td></tr><tr><td>Bonds</td><td>0.2%</td><td>414,620</td><td>4.4%</td></tr><tr><td>Commodities</td><td>

[中间内容因长度限制已省略]

lect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
