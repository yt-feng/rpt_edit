你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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

# Ground Control to Major TAM

Scores on the Doors: oil 70.4%, international stocks 10.1%, US stocks 8.8%, gold 4.4%, cash 1.4%, HY bonds 1.0%, US\$ 0.9%, IG -0.4%, govt bonds -1.6%, bitcoin -11.7% YTD.

Zeitgeist: “Everyone is now convinced that equities are the best inflation hedge.”

The Biggest Picture: strong price action, retail mania, slumping vol...so bubbly; add mega IPOs to AI big boys and market concentration easily surpasses (\~48%) bubbles of roaring '20s, Nifty 50 '70s, Japan '80s, TMT '90s (Chart 2 - but not railroads in 1880s); surge in bond yields how booms/bubbles end...why bond vigilantes on maneuvers; yield tells...XBI to \$120 = yield to melt-up, XRT>\$85 = bond shock delayed.

The Price is Right: Asia tech advancing sharply, Asia exporting inflation (Korea export prices for semis up 148% YoY, DRAMs up 223% YoY – Chart 9); yet Korean won flirting with 30-year lows, Japan yen with 35-year lows, Indonesian rupiah & Indian rupee collapsing to record lows (Charts 3-4); surging global cost of capital cracking periphery of risk (plus housing, consumer, PE) and EM always where the big risk-offs start.

Tale of the Tape: BofA Bull & Bear Indicator hits 8.0...sell-signal for risk assets triggered; consensus max bullish on Positioning & Profits, plus yields breaking up suggests some profit taking here; but no one cutting longs in stocks before historic IPOs and big top Policy tightening will come after CPI hits 4-5% in coming months (Table 2).

Chart 2: The history of stock market bubble concentration   
The bubble history of stock market concentration measured as % of US market cap   
![](images/bf5a6ad1522ac619d7981f875cb3e1dfbd4962d6e52dd432ab6351f1a22f82dd.jpg)

<details>
<summary>line</summary>

| Year | Railroads | Nifty Fifty | TMT | Utilities/telco/industrials | Japan, % MSCI ACWI | AI Big 10* |
|------|-----------|-------------|-----|-----------------------------|--------------------|------------|
| 1835 | ~10%      | ~10%        | ~10%| ~10%                        | ~10%               | ~10%       |
| 1920 | ~63%      | ~36%        | ~36%| ~36%                        | ~36%               | ~36%       |
| 1972 | ~40%      | ~40%        | ~40%| ~40%                        | ~40%               | ~40%       |
| 1985 | ~44%      | ~44%        | ~44%| ~44%                        | ~44%               | ~44%       |
| 1999 | ~41%      | ~41%        | ~41%| ~41%                        | ~41%               | ~41%       |
| 2023 | ~40%      | ~40%        | ~40%| ~40%                        | ~40%               | ~40%       |
</details>

Source: BofA Global Investment Strategy, GFD Finaeon, Bloomberg. Note: Japan is measured as % of MSCI ACWI, all others as % of US stock market. \*\*AI Big 10\* = Magnificent 7 + Broadcom, AMD, Micron.   
BofA GLOBAL RESEARCH

More on page 2...

# 22 May 2026

Investment Strategy Global

BofA

# Data Analytics

![](images/794b06b21f0b373a013fd8c2d3df668532a7d0b7c54cf977fcfacceba1ecbf1f.jpg)

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
Up to 8.0 from 7.8   
![](images/a096dcfab595a7b579a68bbace053e8a0b5bf26fd5863141274fc737c683e5d1.jpg)

<details>
<summary>gauge</summary>

| Category | Value |
|---|---|
| Sell | 8.0 |
| Buy | 2 |
| Extreme Bearish | 0 |
</details>

Source: BofA Global Investment Strategy. The indicator identified above as the BofA Bull & Bear Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 12 to 14.

12977064

Weekly Flows: \$30.5bn to bonds, \$2.4bn to stocks, \$1.2bn to cash, \$1.1bn from gold, \$1.5bn from crypto.

# Flows to Know:

• Crypto: \$1.5bn outflow, biggest since Feb'26,   
• Treasuries: \$10.8bn inflow, biggest in 9 weeks,   
• US equities: \$9.5bn inflow, 8 weeks of inflows, longest streak since Dec'25,   
• Europe: \$2.3bn outflow, 6 weeks of outflows, longest streak since Feb'25 (Chart 10),   
- EM equities: \$7.9bn outflow, 6 weeks of outflows, longest streak since Nov'24 (Chart 11),   
• Tech: \$9.0bn inflow, biggest since Oct'25 (Chart 12),   
• Financials: \$2.4bn outflow, biggest in 10 weeks,   
• Materials: \$2.9bn outflow, biggest in 8 weeks.

BofA Private Clients: \$4.5tn AUM...65.7% stocks (record high), 17.3% bonds (lowest since Mar'22), 9.9% cash (record low); largest weekly inflow to cash since Dec'25 (\$4.1bn); GWIM increasing equity exposure (ETF share count up 4.4% YTD); note BofA private client cumulative inflow to T-bills down since peak 3-month yield in Dec'23 (Chart 5), and higher 10-year yield needed to spur greater flows to bonds (Chart 6); past 4 weeks private clients buying muni bonds, materials, HY vs selling low vol, utilities, REITs.

BofA Bull & Bear Indicator $^{1}$ : up to 8.0, triggering contrarian sell signal for risk assets, on tech/EM debt inflows + record monthly jump in FMS equity allocation + drop in FMS cash levels to 3.9%; there have been 17 “sell signals” since ’02, average loss for global stocks over 2-3 months is 2-3% (hit ratio of \~60%), with max drawdowns of 15-20%; see BofA Bull & Bear Indicator Revamp for full backtest results.

A Short History of IPOs: Table 1 shows price action in broad indices after top 10 IPO launches of all time; Alibaba and ICBC IPOs were “rocket fuel” for Chinese equities in following 3-12 months; NTT & ENEL were timed before big bear markets but big bear began a year later; in contrast, Visa & AIA were “toppy” IPOs, with SPX & Hang Seng much lower 9-12 months after launch; Aramco, Softbank, Facebook, GM launches were inconsequential for broader stock market.

Wealth-Price spiral not Wage-Price spiral: wealth-stocks-boom loop ongoing; but 28% inflation approval for Trump, 35% economic approval for Trump, equal-weight consumer stocks below their GFC lows relative to S&P 500 (Chart 7), AI cutting the price of labor (but not the quantity of labor – see payrolls), little wonder investors pricing in stock-bullish end of Iran conflict as US admin starts to address affordability angst/energy price inflation via big cuts in US SPR, Strategic Petroleum Reserve (down 10% or 41mn bbls since March – Chart 8); we think EM & commodities remain structural bulls, but consumer stocks will be best post-bubble contrarian play (best AI play will be small cap tech adopters & transformers that kill monopolies, duopolies, oligopolies...just like late '70s after Nifty Fifty pop).

London client feedback: “we’re long and paranoid,” “Trump wants/needs to de-escalate Iran, and stocks pop, yields drop on deal,” “if UK gilts find love, everything finds love,” “European electorate shifting decisively right, Farage in UK, Le Pen in France, and you watch the AfD in Germany will win Saxony-Anhalt in September, their first state election," "the fear in bonds is nowhere near as strong as greed in equities," "Warsh will be rhetorically hawkish but practically dovish over the summer," "US actions in Venezuela, Ukraine, Iran, Greenland, Cuba should be viewed through single strategic lens competition with China in AI, which can only be won by securing access to critical resources."

Chart 3: Indian rupee at record low vs US dollar   
Indian rupee spot (1 USD in INR)   
![](images/1d2bf6733810ed569720ccadb73254b1f83647ee94d4b51fab59c9c43ba512c2.jpg)

<details>
<summary>line</summary>

| Year | India rupee |
| ---- | ----------- |
| May 26 | 95 |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Chart 4: Indonesian rupiah weakening past 1998 and 2020 lows   
Indonesian rupiah spot (1 USD in IDR)   
![](images/0695f2ffa5144606d19632a1efb2e8ac0a3f6ea066cf53b794bf7271f014076b.jpg)

<details>
<summary>line</summary>

| Year | Indonesia rupiah |
| ---- | ---------------- |
| May'26 | 17000 |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Chart 5: Private client T-bill inflows down since Dec'23 peak in yields   
US 3-month T-bill yield & BofA private client flows to T-bills (\$bn)   
![](images/a328db0411fa0c8dca59b9c2d7bc586b57c585f4c9e0adce888fedf84ef23512.jpg)

<details>
<summary>line</summary>

| Year | US 3-month T-bill yield % | BofA private client cumulative T-bill flows ($bn, RHS) |
|------|---------------------------|--------------------------------------------------------|
| '12  | ~0.5%                     | ~0                                                     |
| '13  | ~0.5%                     | ~0                                                     |
| '14  | ~0.5%                     | ~0                                                     |
| '15  | ~0.5%                     | ~0                                                     |
| '16  | ~0.5%                     | ~0                                                     |
| '17  | ~1.5%                     | ~5                                                     |
| '18  | ~2.5%                     | ~10                                                    |
| '19  | ~3.0%                     | ~15                                                    |
| '20  | ~0.5%                     | ~10                                                    |
| '21  | ~0.5%                     | ~15                                                    |
| '22  | ~0.5%                     | ~20                                                    |
| '23  | ~6.0%                     | ~70                                                    |
| '24  | ~6.5%                     | ~85                                                    |
| '25  | ~5.5%                     | ~70                                                    |
| '26  | ~4.5%                     | ~40                                                    |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Chart 6: Higher UST 10Y yield needed to spur greater flows to bonds   
UST 10Y yield & BofA private client flows to T-notes & T-bonds (\$bn)   
![](images/863d972ca08c085f4c7f2f6c725c2b447feffd238b0ad956e9403e5c390d5b0f.jpg)

<details>
<summary>line</summary>

| Year | US 10-year Treasury yield % | BofA private client cumulative T-note & T-bond flows ($bn, RHS) |
|------|-----------------------------|---------------------------------------------------------------|
| '12  | ~2%                         | ~0                                                            |
| '13  | ~1.5%                       | ~0                                                            |
| '14  | ~2.8%                       | ~0                                                            |
| '15  | ~2.5%                       | ~0                                                            |
| '16  | ~1.5%                       | ~0                                                            |
| '17  | ~2.5%                       | ~0                                                            |
| '18  | ~3.0%                       | ~0                                                            |
| '19  | ~2.0%                       | ~0                                                            |
| '20  | ~0.5%                       | ~0                                                            |
| '21  | ~1.5%                       | ~0                                                            |
| '22  | ~3.0%                       | ~10                                                           |
| '23  | ~4.5%                       | ~30                                                           |
| '24  | ~5.0%                       | ~45                                                           |
| '25  | ~4.5%                       | ~50                                                           |
| '26  | ~4.5%                       | ~55                                                           |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Chart 7: Equal-weight consumer stocks vs S&P 500 below GFC lows   
US consumer discretionary (equal-weight) vs S&P 500   
![](images/a2588148e85063cb080072b6d1287c58550cb80494a9d0feacb7d24719b4744d.jpg)

<details>
<summary>line</summary>

| Year | US consumer discretionary (equal-weight) vs S&P 500 |
| ---- | -------------------------------------------------- |
| '07  | 0.11                                               |
| '09  | 0.08                                               |
| '11  | 0.13                                               |
| '13  | 0.14                                               |
| '15  | 0.15                                               |
| '17  | 0.14                                               |
| '19  | 0.12                                               |
| '21  | 0.11                                               |
| '23  | 0.09                                               |
| '25  | 0.08                                               |
| '27  | 0.07                                               |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Table 1: Alibaba and ICBC were the “rocket fuel” IPOs   
Largest 10 IPOs of all time + market reaction 

<table><tr><td>Company</td><td>IPO Date</td><td>IPO Size</td><td>3M %Chg*</td><td>6M %Chg*</td><td>9M %Chg*</td><td>12M %Chg*</td></tr><tr><td>Aramco</td><td>Dec&#x27;19</td><td>$26bn</td><td>-5%</td><td>-8%</td><td>+0%</td><td>+10%</td></tr><tr><td>Alibaba</td><td>Sep&#x27;14</td><td>$22bn</td><td>+32%</td><td>+51%</td><td>+119%</td><td>+38%</td></tr><tr><td>SoftBank</td><td>Dec&#x27;18</td><td>$21bn</td><td>-1%</td><td>-2%</td><td>-0%</td><td>+10%</td></tr><tr><td>NTT</td><td>Oct&#x27;98</td><td>$18bn</td><td>-2%</td><td>+17%</td><td>+30%</td><td>+23%</td></tr><tr><td>Visa</td><td>Mar&#x27;08</td><td>$18bn</td><td>+2%</td><td>-6%</td><td>-34%</td><td>-43%</td></tr><tr><td>AIA Group</td><td>Oct&#x27;10</td><td>$18bn</td><td>+3%</td><td>-1%</td><td>-8%</td><td>-22%</td></tr><tr><td>Enel</td><td>Nov&#x27;99</td><td>$17bn</td><td>+22%</td><td>+36%</td><td>+29%</td><td>+26%</td></tr><tr><td>Facebook</td><td>May&#x27;12</td><td>$16bn</td><td>+8%</td><td>+5%</td><td>+16%</td><td>+25%</td></tr><tr><td>GM</td><td>Nov&#x27;10</td><td>$16bn</td><td>+13%</td><td>+13%</td><td>+0%</td><td>+7%</td></tr><tr><td>ICBC</td><td>Oct&#x27;06</td><td>$14bn</td><td>+54%</td><td>+102%</td><td>+118%</td><td>+237%</td></tr></table>

Source: BofA Global Investment Strategy, Bloomberg   
\*Tadawul (Saudi Aramco), Shanghai Composite (Alibaba, ICBC), Hang Seng (AIA Group), Nikkei (SoftBank, NTT), S&P 500 (Visa, Facebook, GM), Euro Stoxx 50 (Enel)   
BofA GLOBAL RESEARCH

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
