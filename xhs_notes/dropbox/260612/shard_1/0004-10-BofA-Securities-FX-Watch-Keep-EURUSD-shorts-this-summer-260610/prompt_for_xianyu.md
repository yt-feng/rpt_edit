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
## Key takeaways

- On 20 May we went short euro via a 1.15-1.13 put spread. We remain short into summer: techs + fundamentals point to downside.  
- Technicals: Post NFP, euro broke trend line support. A head and shoulders top is still forming. And 2018 is still repeating.  
- Fundamentals: Relative data flow underpriced, amid growing risk to USD-supportive monetary policy repricing.

## View: Keep EURUSD shorts this summer

On May 20, we recommended positioning for euro weakness into summer via a EURUSD 1.15/1.13 3m put spread (spot 1.1610, vols 6.22%/6.72%) at a cost of 0.3591% (current: 0.47%). We remain short. See report: Six reasons to short euro 20 May 2026

## Technicals: Euro broke support, bias is to fade bounces

One immediate market response to the latest US payrolls release was a decline in euro, which broke an uptrend line and reinforced our bearish view. On June 8, euro tested the psychological 1.15 support level and has begun to bounce. We prefer to fade rebounds and continue to look for renewed downside. On the weekly chart, euro continues to form the right shoulder of a head and shoulders top, with neckline support at 1.1411–1.1392. A decisive break below this zone would materially increase downside risk.

Finally, DXY behaviour during President Trump's second term continues to track his first. In 2018, the second year of term one, DXY bottomed in the first half and rallied in the second. DXY is now attempting to base, with a daily close above 100.51 needed to confirm a renewed uptrend and continuing repeating 2018.

## Fundamentals: relative data vs. geopolitical wish-casting

There is a case to be made for EUR/USD to potentially trade through our Q2 forecast of 1.14, which is also just below its 12-month lows. The growth divergence between the US and EA is notable and arguably being underpriced by rates markets.

But hope for a peace agreement in the Middle East has prevented larger themes from taking hold. Even as there has been some associated reprieve in energy markets, upside risks points to downside risks to the EUR (from a terms-of-trade perspective). This suggests a real possibility of further USD supportive Fed repricing, while ECB hikes could prove counter-productive for the EUR.

In the meantime, the market will likely be in a more of a holding pattern as these next two weeks bring the May CPI report (this Wed) and the first FOMC under Chair Warsh (next Wed). Any hint of further upside pressure from the data, or a less assertive dovish tone from Chair Warsh could serve as the next (non-Iran related) catalyst for a USD rally.

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 8 to 10. Analyst Certification on page 7. 12982831

## 10 June 2026

G10 FX Strategy Global

## Alex Cohen, CFA

FX Strategist

BofAS

alex.cohen2@bofa.com

## Paul Ciana, CMT

Technical Strategist

BofAS

paul.ciana@bofa.com

## Michalis Rousakis

FX Strategist

MLI (UK)

michalis.rousakis@bofa.com

## Adarsh Sinha

FX and Rates Strategist

MLI (UK)

adarsh.sinha@bofa.com

For a list of open trade recommendations and trade recommendations closed in the last 12 months, please see the Global FX Weekly: A game of two halves report.

## Keep EUR shorts on this summer

## EURUSD: Bearish trend line breakdown

## Post strong US payroll data, euro broke trend line support

Following stronger-than-expected US payrolls data on June 5, EURUSD sold off sharply, breaking below trendline support and falling to its lowest level since early April. This breakdown reinforces our bearish bias.

On June 8, EURUSD tested 1.15 and has since started to bounce. In the near term, we view former support as resistance, beginning at 1.1576 (May 21 low) and extending up to the broken trendline near 1.16.

We continue to favor selling EUR into rallies, including the current bounce. Ideally, EURUSD does not post a daily close above the prior range resistances, which include the 50-day SMA, 200-day SMA, and downtrend line in the 1.1671–1.1685 area.

Chart 4: EURUSD bearish trend line breakdown, test of psychological support at 1.15, bounce to resistance should be faded.

Daily candles, 50d SMA, 200d SMA, Ichimoku Cloud RSI, MACD, Fibonacci levels

![](images/4385121427444a9d87e73f439d45508953e57ca42d733573c50d6b4312ae7605.jpg)  
Source: BofA Global Research, Bloomberg  
BofA GLOBAL RESEARCH

## EURUSD: Head-and-shoulders top still forming

## Right shoulder of a head and shoulders top continues to form

Price action continues to suggest the right shoulder of a potential head-and-shoulders top is developing, leaving EURUSD vulnerable to a deeper pullback.

If this structure persists, EURUSD should retest the neckline at 1.1411–1.1392. A decisive break below this zone would confirm the topping pattern and open downside toward 1.11 and the rising 200-week moving average near 1.0980.

While the neckline has yet to break, we view the weeks of May 15 and June 5 as key bearish impulses contributing to the topping process. A subsequent, comparably strong bullish impulse in the coming weeks would reduce conviction in the head-and-shoulders scenario.

Chart 4: EURUSD still looks at risk of forming a head and shoulders top.  
Weekly candles, 50d SMA, 200d SMA, Ichimoku Cloud RSI, MACD, Fibonacci levels  
![](images/f028c03bf4dcb4e3a1f2b88183c2daad3ba26ea14039ff9ce43684c14fd2d30d.jpg)

<details>
<summary>line chart</summary>

| Date       | EURUSD Curncy - Last Price | SMAVG (200) on Close (EURUSD) | Inter-Period MA Avg (200, Monthly) (EURUSD) |
|------------|---------------------------|-------------------------------|---------------------------------------------|
| 2023       | ~1.1561                   | +0.0039                       | ~1.1882                                     |
| 2024       | ~1.1392                   | ~1.0979                       | ~1.1882                                     |
| 2025       | ~1.1795                   | ~1.1881                       | ~1.1882                                     |
| 2026       | ~1.1411 to 1.1392         | ~1.1392                       | ~1.1882                                     |
| 2027       | ~1.1795                   | ~1.1392                       | ~1.1882                                     |
| 2021 peak   | 1.2349                    | —                             | —                                           |
| 61.8%      | —                         | —                             | —                                           |
| (Hammer candle and double bottom) | —                     | —                             | —                                           |
| RSI        | 45.9527                   | —                             | —                                           |
| OB         | 70.00                     | —                             | —                                           |
| OS         | 30.00                     | —                             | —                                           |
| Diff       | -0.0019                   | —                             | —                                           |
| MACD       | -0.001                    | —                             | —                                           |
| Sig(9)     | 0.0008                    | —                             | —                                           |
| Difference | -0.0019                   | —                             | —                                           |
</details>

Source: BofA Global Research, Bloomberg

BofA GLOBAL RESEARCH

## DXY in 2024-2026 has been repeating 2016-2018

## If the DXY continues to repeat Trump's term 1 trend, the DXY rallies in 2H26.

DXY price action continues to closely mirror the 2016–2018 post-election cycle, suggesting further upside risk if the pattern holds. We're on watch for a daily close above 100.51 to confirm a repeat bottom rhyming with 2018 and further upside. This would be the highest daily close since May 2025, eclipsing that of March 30, 2026.

Following the November 2016 election, DXY broke out of a multi-year range and rallied \~6.4%, before forming a head-and-shoulders top and declining through 2017. The index then bottomed in 1Q18, broke higher in late April, and went on to rally a further \~6.6% into August 2018.

A similar sequence has unfolded after the November 2024 election, DXY broke out and rallied \~6.3%, then formed a top and declined through 2025. In 1Q26, DXY established a key low and has begun to base.

If this analogue continues to hold, a confirmed breakout from the current base would point to a renewed USD uptrend, with potential for DXY to rally toward 103–105 in the coming months.

Chart 5: Below we compare the DXY trend in 2016 through 2018 vs 2024 through today. They are tracking closely and, if they continue to, the DXY will soon bottom and rally this summer and euro will decline.

Daily line chart of closing prices. Top panel is 2016-2018, bottom is 2024-2026.

![](images/bf489cae85650c907939a1ddb3a37383d1499581c1ed7861bec12fcfa038bf83.jpg)

<details>
<summary>line chart</summary>

| Election Day | ~94.000 | - | 50.0% |
| --- | --- | --- | --- |
| Election Day | ~94.000 | - | 50.0% |
| Election Day | ~94.000 | - | 50.0% |
| Election Day | ~94.000 | - | 50.0% |
| Election Day (Dec 12/31/16) | ~111.000 | +6.32% | - |
| Election Day (Dec 12/31/17) | ~111.000 | 61.8% | - |
| Election Day (Dec 12/31/18) | ~111.000 | 50.0% | - |
| Election Day (Dec 12/31/19) | ~111.000 | - | - |
| Election Day (Dec 12/31/25) | ~111.000 | - | - |
| Election Day (Dec 12/31/26) | ~111.000 | - | - |
| Election Day (Dec 12/31/27) | ~111.000 | - | - |
| Election Day (Dec 12/31/28) | ~111.000 | - | - |
| Election Day (Dec 12/31/29) | ~111.000 | - | - |
| Election Day (Dec 12/31/3) | ~111.000 | - | - |
| Election Day (Dec 12/31/31) | ~111.000 | - | - |
| Election Day (Dec 12/31/32) | ~111.000 | - | - |
| Election Day (Dec 12/31/33) | ~111.000 | - | - |
| Election Day (Dec 12/31/34) | ~111.000 | - | - |
| Election Day (Dec 12/31/35) | ~111.000 | - | - |
| Election Day (Dec 12/31/36) | ~111.000 | - | - |
| Election Day (Dec 12/31/37) | ~111.000 | - | - |
| Election Day (Dec 12/31/38) | ~111.000 | - | - |
| Election Day (Dec 12/31/39) | ~111.000 | - | - |
| Election Day (Dec 12/31/4) | ~111.000 | - | - |
| Election Day (Dec 12/31/42) | ~111.000 | - | - |
| Election Day (Dec 12/31/43) | ~111.000 | - | - |
| Election Day (Dec 12/31/44) | ~111.000 | - | - |
| Election Day (Dec 12/31/45) | ~111.000 | - | - |
| Election Day (Dec 12/31/46) | ~111.000 | - | - |
| Election Day (Dec 12/31/47) | ~111.000 | - | - |
| Election Day (Dec 12/31/48) | ~111.000 | - | - |
| Election Day (Dec 12/31/49) | ~111.000 | - | - |
| Election Day (Dec 12/31/5) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/52) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/53) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/54) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/55) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/56) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/57) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/58) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/59) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/6) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/62) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/63) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/64) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/65) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/66) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/67) | ~97.676 | +6.57% | 67% |
| Election Day (Dec 12/31/68) | ~97.676 | +6.57% | 67% |
</details>

Source: BofA Global Research, Bloomberg  
BofA GLOBAL RESEARCH

## Fundamentals: Relative data vs. geopolitical wish-casting

As the EUR/USD's mostly narrow 12-month range has endured even though the start of the Iran war, relative economic data performance has continued to shift in the USD's favor (Exhibit 2). This was reinforced last Friday, by the US employment report, which served as the latest example of a resilient (if not strengthening) labor market, serving to push the pair towards the post-April ceasefire lows (Exhibit 1, see report: Rates & FX: World Cup, labor, markets 08 June 2026).

Still, this comes against a backdrop of continued hope for an eventual peace agreement, which has prevented the market from more materially trading off growth and/or rate differentials. And even as anticipations mount for an eventual resolution to the Iran war, the Strait of Hormuz remains closed, keeping energy prices elevated (albeit well past peak for now). Energy inventory issues will likely persist well after any hypothetical agreement is reached. In Europe, the rise in gas prices – while quite small compared to that of 2022 – remains a source of stagflationary concern. (Exhibit 5)

## Talk of Fed hikes getting louder, while durability of ECB hikes in question

At the onset of the war, the market was quick to price the ECB (and several other G10 central banks) for eventual hikes to address the global inflation shock. At the same time, entrenched expectations for a more structurally dovish Fed prevented such an assertive adjustment in the US rates. Data flow on both sides of the Fed's mandate has started to change this.

Yet the market remains priced for even more hikes by the ECB, which for now has also mitigated a correction lower in the pair. (Exhibit 3; Exhibit 4) But given a more anemic growth backdrop, this isn't necessarily a bullish sign for the EUR, as eventual ECB tightening could be short-lived, and/or risk a policy mistake (see report: Global FX weekly: A game of two halves 05 June 2026).

At the same time, even if the market is right to expect Chair Warsh to resist hikes, the Fed's hand could easily be forced by a combination of ongoing inflationary pressure, further labor improvement and broader easing of financial conditions (ie. resilient equities). While markets reflect some likelihood of a hike this year, the vast majority of Fed forecasters (in Bloomberg) have yet to call for any (Exhibit 6).

## (Fundamental) bottom line

Fundamentally, there is a case to be made for the EUR/USD pair to at least trade through our Q2 forecast of 1.14, which is also just below its 12-month lows. The growth divergence between the US and EA is notable, and arguably being underpriced by rates markets.

But hope for a peace agreement in the Middle East has prevented larger themes from taking hold. Even as there has been some associated reprieve in energy markets, upside risks point to downside risks to the EUR (from a terms-of-trade perspective). This suggests a real possibility of further USD supportive Fed repricing, while ECB hikes could prove counter-productive for the EUR.

In the meantime, the market will likely be in a more of a holding pattern as the next two weeks bring the May CPI report (this Wed) and the first FOMC under Chair Warsh (next Wed). Any hint of further upside pressure from the data, or a less assertive dovish tone from Chair Warsh could serve as the next (non-Iran related) catalyst for a dollar rally.

Exhibit 1: USD still trading within its previous 12m range, while labor surprise me

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
