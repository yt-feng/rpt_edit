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

Exhibit 1: USD still trading within its previous 12m range, while labor surprise measures reach fresh multi-year highs  
DXY & Bloomberg US Labor Surprise Index  
![](images/e9ed827188e3b97fd938d95b6f6d12dca9ba211b1cc055fa89b243996dc9d053.jpg)

<details>
<summary>line chart</summary>

| Date   | DXY (LHS) |
|--------|-----------|
| Jan-23 | 107       |
| Jul-23 | 108       |
| Jan-24 | 106       |
| Jul-24 | 105       |
| Jan-25 | 109       |
| Jul-25 | 103       |
| Jan-26 | 104       |
</details>

Source: Bloomberg; BofA Global Research  
BofA GLOBAL RESEARCH

Exhibit 3: Policy differentials now priced for modest but steady narrowing (towards EUR)...  
Fed & ECB policy rate  
![](images/82a8d9223d596ade4b563c4076b0e9d04e860aaa28ecac7a95abc4f8ac80787a.jpg)

<details>
<summary>line chart</summary>

| Date   | ECB-Fed | Fed Effective | ECB Effective | ECB-OIS | ECB-OIS | ECB-Fed OIS |
|--------|---------|---------------|---------------|---------|---------|-------------|
| Jan-21 | -1.0    | 0.0           | 0.0           | 0.0     | 0.0     | 0.0         |
| Jan-22 | -1.0    | 0.0           | 0.0           | 0.0     | 0.0     | 0.0         |
| Jan-23 | -2.0    | 4.0           | 2.0           | 0.0     | 0.0     | 0.0         |
| Jan-24 | -1.5    | 5.5           | 4.0           | 0.0     | 0.0     | 0.0         |
| Jan-25 | -1.5    | 5.5           | 3.5           | 0.0     | 0.0     | 0.0         |
| Jan-26 | -1.5    | 4.5           | 2.0           | 3.5     | 2.5     | 0.0         |
| Jan-27 | -1.5    | 3.5           | 2.0           | 4.0     | 3.0     | 1.0         |
</details>

Source: Bloomberg; BofA Global Research  
BofA GLOBAL RESEARCH

Exhibit 5: Since the closure of the Strait of Hormuz, the EUR has remained resilient relative to the upward pressure on gas prices  
European Gas (TZT) & EUR (inverted)  
![](images/5411ed40e69252d34e72ecb796bad0027cce00bc356fc3c0b1a049bf486e2bac.jpg)

<details>
<summary>line chart</summary>

| Date    | European Gas | EUR (RHS, inverted) |
|---------|--------------|---------------------|
| Jan-24  | 35           | 40                  |
| Jun-24  | 30           | 45                  |
| Nov-24  | 40           | 50                  |
| Apr-25  | 55           | 55                  |
| Sep-25  | 30           | 25                  |
| Feb-26  | 40           | 1.0                 |
</details>

Source: Bloomberg; BofA Global Research  
BofA GLOBAL RESEARCH

Exhibit 2: Relative US vs. Euro area data trends have been stark, suggesting further space for the EUR to depreciate further  
Economic Change Indices: EA - USA  
![](images/7fa8d0d41965bddb241c9a050d767ef796bd625e176d65db3f2c933e72d35b5c.jpg)

<details>
<summary>line chart</summary>

| Date   | EU-US Economic Change Index Differential | EUR (RHS) |
|--------|------------------------------------------|-----------|
| Jan-23 | -200                                     | 1.0       |
| Jul-23 | 500                       

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
