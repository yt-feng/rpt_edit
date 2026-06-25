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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`BARC`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份BARC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
U.S. Equity Strategy

# Upgrading Into Uncertainty: Raise S&P 500 PT to 7800, FY26 EPS to \$337

Equities remain choppy as peace talks stop and start, and questions linger around AI spend, funding and monetization, higher for longer rates, and consumer strength. We focus on the improving earnings outlook, taking our FY26 EPS to \$337 from \$321, and our 2026 PT to 7800 from 7650.

\- Macro regime remains complex, but the balance of risks still leans constructive. Labor data are strong enough to reduce recession risk, but also to push rate cuts further out. Input costs are rising again, though not yet a growth shock large enough to derail the cycle. The equity bull case remains intact, but earnings and AI capex visibility must do more of the work as Fed support fades and positioning is less able to absorb disappointment.

\- We raise our FY26 S&P 500 EPS estimate to \$337 from \$321, modestly below the Street's \$341 and implying \~21% Y/Y growth from \$279 in FY25. Tech earnings guidance and visibility remains underpinned by expanding AI capex, reflationary pressure should support nominal revenue growth, and the industrial side of the economy looks relatively supportive into 2027, offsetting potential downside to consumer spending. We also introduce our FY27 EPS estimate at \$389 (+15% Y/Y), below the Street's \$398.

\- Our 2026 S&P 500 price target goes to 7800 from 7650. We trim our valuation assumptions modestly from the last update (23x FY26 EPS, down from \~24x) to account for uncertainties around the scale, funding and monetization timeline of capex, AI-led dispersion, and higher nominal yields and inflation. This leaves earnings to do the work in raising our price target. We also introduce our 2027 price target at 8800.

\- We go to Neutral on Financials and Healthcare. Our bull thesis on the Financials sector has not played out, as banks-driven positive earnings revisions were offset by private credit concerns, regulatory risks within payments, and AI disruption. We believe downward EPS revisions for Healthcare have mostly run their course, leaving risk/reward more balanced. The balance of our sector views remain unchanged: Positive on TMT, Industrials and Utilities, Negative on the Consumer space.

\- Risks we are watching into the back half of the year include signs of stress in the AI investment cycle, including the 'what-ifs' we debated last September: model advancement, availability of power, and funding (especially as the financing mix grows more complex).

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

SIGNATURE

U.S. Equity Strategy
Venu Krishna, CFA
+1 212 526 7328
venu.krishna@BARC.com
BCI, US

Rex Feng
+ 1 212 526 6114
rex.feng@BARC.com
BCI, US

Riddhiman Dass
+1 212 526 0850
riddhiman.dass@BARC.com
BCI, US

Tianqi Feng
+1 212 526 9179
tianqi.feng@BARC.com
BCI, US

Data as of 19 June 2026.
Source: BARC

Rates are re-centering as a key risk factor with a new Fed Chair taking the reins amid resurgent inflation. Finally, we are keeping a close eye on the U.S. consumer as higher inflation and lower purchasing power have the potential to generate lagged pressures in 2H26.

FIGURE 1. BARC FY26 and FY27 Year-End Estimates for S&P 500

<table><tr><td></td><td colspan="5">BARC S&amp;P 500 FY 2026 Estimates</td><td colspan="4">BARC S&amp;P 500 FY 2027 Estimates</td></tr><tr><td>Scenario</td><td>EPS</td><td>Growth (yoy)</td><td>PE Multiple</td><td>YE Value</td><td>Upside / Downside</td><td>EPS</td><td>Growth (yoy)</td><td>PE Multiple</td><td>YE Value</td></tr><tr><td>Bull Case</td><td>$343</td><td>22.9%</td><td>24.8x</td><td>8500</td><td>13.3%</td><td>$397</td><td>17.8%</td><td>24.2x</td><td>9600</td></tr><tr><td>Base Case</td><td>$337</td><td>20.8%</td><td>23.1x</td><td>7800</td><td>4.0%</td><td>$389</td><td>15.4%</td><td>22.6x</td><td>8800</td></tr><tr><td>Bear Case</td><td>$329</td><td>17.9%</td><td>19.1x</td><td>6300</td><td>-16.0%</td><td>$380</td><td>12.8%</td><td>18.7x</td><td>7100</td></tr><tr><td>Current S&amp;P 500 Price</td><td></td><td></td><td></td><td>7,501</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 2026: the (equity) story so far

U.S. equities entered 2026 with plenty of good news already priced in: Global macro was holding together, AI capex was an undeniable tailwind, and market leadership was beginning to broaden beyond mega-cap Tech into cyclicals, small caps and “old economy” beneficiaries of the AI buildout. But high valuations left a narrower margin for error. By February, the months-long debate over AI disruption in software had boiled over, leading the industry to give back all of its outperformance vs. SPX since 2022. Concerns over debt-laden software companies spilled over into already-simmering worries about private credit, which then bled into a broader reassessment of long-duration growth at the same time geopolitical risk was moving to the center of the macro debate. The war in the Middle East then sparked a generational oil shock, stoking renewed fears over inflation, central-bank reaction functions and global growth. Equity markets had to price not just AI disruption, but also the possibility that the soft-landing narrative was drifting toward something closer to stagflation-lite.

We believed there was value in looking through the noise and focusing on both the underlying strength of the U.S. economy and the improving fundamentals within U.S. equities. Indeed, once ceasefire headlines shrunk both the left tail and the immediate geopolitical risk premium, investors quickly returned to the parts of the market where earnings visibility looked strongest. Big Tech, Growth and Momentum surged as investors re-engaged with AI- and Tech-exposed names. A strong 1Q26 earnings season, with Tech EPS growth sitting at the best levels since 2010 and revisions to full year EPS hitting a record pace, pointed to more fundamental headroom.

Positioning amplified the speed and magnitude of the round trip. Portfolios came into the year very long equities, leaving stocks vulnerable to synchronized de-risking across discretionary and systematic investors as sentiment turned in 1Q26. Long-only managers cut equity exposure to near year-lows and built cash, hedge funds de-grossed, and systematic strategies rapidly cut equity exposure. Clearing the ceasefire overhang saw these exact dynamics play out in reverse: elevated cash provided fuel for redeployment, real money inflows surged, systematic strategies bought the dip, and option flows pointed to upside-chasing in single stocks.

As it stands, the S&P 500 is within a few percentage points of its all-time high, set just earlier this month. While neither the software, private credit nor geopolitical and energy shocks have yet been large or persistent enough to overturn our core equity thesis, new concerns are emerging into the back half of the year as markets tangle with resurgent inflation, AI capex scales to unprecedented levels, and a Fed rate path narrows more than before.

## A banner year for earnings, with risks at the margin

The earnings growth engine is firing on all cylinders. Activity data remain constructive: industrial production is on the rise, ISM manufacturing PMI is finally back in expansionary territory, and both durable goods and S&P Global manufacturing output point to solid momentum. The jobs market looks solid, but not overheating. Hyperscalers are redoubling commitments to AI capex and expanding their financing toolkit to match liabilities and capital commitments, which is lengthening earnings upside visibility for a growing swath of downstream industries. And AI is not the only source of investment; energy infrastructure buildout, rising defense spending and the need to rebuild supply chain resilience could lift investment-to-GDP among advanced economies to levels not seen since the 1990s (Supersize me: The coming investment cycle, 26 March 2026).

To be fair, it is not a clean read all around: higher rates, slower real income growth, and rising costs all pose risks to consumption. On the input cost front, our colleagues in commodities argue the market is still underpricing the forward oil strip, expecting crude to still average \$100/barrel this year as inventory buffers continue to erode against still-resilient demand (Energy Sigma: We have a deal, 16 June 2026). Activity, employment and commodity prices all feed the inflation and Fed reaction-function debates, increasingly tilting the narrative toward renewed tightening into year-end.

The rebound in equities following the U.S.-Iran détente reinforces the market's resilience, but we believe yields are re-centering as a key risk factor for equities. The relationship between yields and equities has turned notably negative, suggesting that higher yields are now being read less as a growth signal and more as a constraint on valuations and liquidity. In this regime, incremental increases in either inflation or term premia carry asymmetric downside risk for equities, particularly given the market's dependence on longer-duration growth assets.

FIGURE 2. The yield-equity correlation is testing the lower bound of its historical range at current levels of nominal 10Y  
![](images/36220a0f7abc4fcfeec11d05fff59e9d6773f49cc6f6509ea6ce70eb670b5d65.jpg)  
Data as of 22 June 2026. 6m rolling correlations observed at monthly average 10Y yields. Source: Bloomberg, BARC

This makes the path of interest rates from here especially consequential. Even in an environment of broadly stable growth, upside surprises in inflation could challenge the durability of the recent rally if they lead to a durable repricing of the policy path. Markets are already assigning some probability to additional Fed tightening by year-end, at odds with our more benign baseline expectations for policy. While the historical record surrounding Fed "reversal of easing" suggests that the mere prospect of the Fed resuming hikes has not typically derailed equities ahead of the event, the weeks and months following the event could be a different story.

FIGURE 3. The prospect of resumed hikes has not typically derailed equities ahead of the event  
S&P 500 Performance Around Fed Reversal of Easing  
![](images/28676079a14f27a811693671bf77cb17cd37f9b7ea7adae24718c795bcddd7d2.jpg)  
The Fed did not announce targeted rate changes prior to 1994. For 1983 and 1987, we anchor dates to Fed meetings immediately preceding rates tightening. Source: Bloomberg, BARC

In addition, AI capex continues to pose its own risks. While boosting EPS growth now, it also raises execution risks later. We believe "peak capex" has been deferred further out, reflecting both persistent supply constraints in training compute capacity as well as a material steepening of the demand curve as enterprise adoption accelerates and model improvements unlock new use cases. Hyperscalers are responding with sustained growth in investment over a longer horizon. The result is a growing mismatch between internally generated cash flow and projected capital requirements, as our Internet & Semis research teams point out in AI's S-Curve is Steepening (1 June 2026).

FIGURE 4. BARC now sees north of \~\$1.1T in 2028 total hyperscaler capex post-1Q results...  
![](images/34f952bae11fde4a32af1e233a8f4e1005f9b6c4952d13131c5ba5f3cfd1aad0.jpg)  
From AI's S-Curve Is Steepening (1 June 2026).
Source: BARC Estimates, Company Disclosures  
FIGURE 5. ...which is \~26% above the Street....

![](images/877ae81173f4d8fd714a6533a30b19eb686fbd09a46acb4f7eaddba963955f7d.jpg)  
From AI's S-Curve Is Steepening (1 June 2026). Source: Bloomberg, BARC

FIGURE 6. ...driving operating cash flow pressure that we expect to intensify into 2028...  
![](images/08891f24914863fbf59994cdc5d61779be090912ae8d7f54ddb961bb61fa40f1.jpg)  
Estimates from BARC' Internet research team. Note that for AMZN, capex is AWS only, while OCF is total AMZN.  
Source: Bloomberg, BARC

FIGURE 7. ...which is not baked into consensus estimates  
![](images/e05cb348b9e48e04a713b0ff4e65c1c3f39568afdb618a61c462f6eaeb9ac871.jpg)

Source: Bloomberg, BARC

All in, while it's clear that the macro regime remains complex, we believe the balance of risks still leans constructive. Labor data are strong enough to reduce recession risk, but also to push rate cuts further out. Input costs are rising again, though not yet a growth shock large enough to derail the cycle. The equity bull case remains intact, but earnings and AI capex visibility must do more of the work as Fed support fades and positioning is less able to absorb disappointment.

## Raise FY26 EPS estimate to \$337 from \$321

We raise our FY26 S&P 500 EPS estimate to \$337 from \$321, modestly below the Street's \$341 and implying 20.8% Y/Y growth from \$279 in FY25. Since our last update, three developments argue for a higher EPS estimate: 1) 1Q26 earnings season was materially stronger than expected, confirming that Big Tech and the rest of TMT continue to convert AI-related demand into earnings upside, and upward revisions to full-year consensus are running well ahead of average; 2) reflational pressure through 2026 should support nominal revenue growth, particularly in sectors with operating leverage or commodity exposure; and 3) the industrial side of the economy looks relatively supportive into 2027, with our economists' forecasts pointing to a better industrial production backdrop next year. We expect these upside drivers to be modestly offset by weaker consumption: spending data have cooled and real purchasing power gains look more modest at current inflation.

Around our base case of \$337, we estimate a relatively tight bull/bear range of \$343/\$329, underscoring that the core debate is less about directional earnings risk and more about the magnitude and persistence of key cyclical drivers. The dispersion is primarily a function of uncertainty around the durability of Tech beat-and-raise alongside the trajectory of goods consumption and whether recent resilience can be sustained into a softer macro backdrop. Industrial activity represents a second-order swing factor, particularly given its sensitivity to both global demand and inventory dynamics, while the path of inflation also remains critical.

FIGURE 8. Q1 beat-and-raise, secular growth and nominal pricing power to underpin FY26 EPS growth  
![](images/5c7d034d0bf0cc1a38a4a52d05f17b8a558bf46653fec02f318300549f135c42.jpg)  
Data as of 10 June 2026.
Source: LSEG Data & Analytics, Bloomberg, BARC

FIGURE 9. We estimate \$337 in FY26 EPS (+21% Y/Y) vs. Street at \$341  
![](images/c618acc7ce7b7234c2df8c34360696243eb5c011c8e68cc2fd9548da6b176e75.jpg)  
Data as of 16 Jun 2026

FIGURE 10. FY26 base, bull & bear case EPS scenarios  
![](images/e06c3bac5b88f1ced7ada755bb2db7af1d39487a840b1957f52763b6e27b7251.jpg)  
Source: LSEG Data & Analytics, Bloomberg, BARC  
Data as of 10 Jun 2026
Source: LSEG Data & Analytics, Bloomberg, BARC

Looking ahead, we introduce a preliminary FY27 EPS estimate of \$389, reflecting a modest deceleration in growth. Our framework assumes a partial recovery in consumption on a Y/Y basis, coupled with continued strength in industrial production as the lagged effects of prior tightening fade. This is partially offset by a normalization in nominal pricing power, particularly as disinflationary forces broaden. The resulting bull and bear cases of \$397/\$380 capture a similar set of crosscurrents, with upside tied to a more durable demand recovery and sustained Tech momentum, while downside reflects the risk of a more protracted normalization in margins and growth.

FIGURE 11. We estimate \$389 in FY27 EPS (+15% Y/Y) vs. Street at \$398  
![](images/4b8cf85e56daedd4375daee63c94de3d80a7d8c819ae3aea3b13a1c102ec2038.jpg)  
Data as of 10 Jun 2026  
Source: LSEG Data & Analytics, Bloomberg, BARC

FIGURE 12. FY27 base, bull & bear case EPS scenarios  
![](images/d126872f824ecc1e0c1ca234c5310ce6d5fd727f0b0e38788afbf599bed98058.jpg)  
Data as of 10 Jun 2026  
Source: LSEG Data & Analytics, Bloomberg, BARC

We recognize that a central pillar of our EPS framework rests on the view that Tech can continue to deliver positive earnings upside even as consensus estimates and revisions already sit at elevated levels vs. history. Skepticism around the magnitude and durability of this outperformance is understandable, particularly given concerns about where we are in the AI investment cycle and whether current growth assumptions embed an implicit peak. Still, our industry analyst colleagues see good reason to believe that much of the supply-demand imbalance in AI compute will persist well into CY27 (Making the Case for Another Leg Higher in the Memory Trade, 26 May 2026), and we think this visibility provides a degree of near-term de-risking to NTM estimates. While we do not dismiss the possibility of normalization further out, current conditions argue that earnings estimates for Tech over the near term are not overly heroic.

FIGURE 13. YTD revisions to full-year EPS are running well ahead of 10Y norms...  
![](images/98d15c597d88ad98de41580e24bda6cb0d83937ad4bf006b1b342c678e216ff2.jpg)  
Data as of 16 June 2026. 10Y average from 2014-2025, excluding 2020 & 2021. Source: Bloomberg, BARC

FIGURE 14. ...with all quarters seeing a pickup in EPS estimates since the end of calendar 1Q26  
![](images/3f221fcbd83ab077f33cd60ba79a0d62efd1275936fd9fd199876fde981f0f08.jpg)  
Data as of 16 June 2026.
Source: Bloomberg, LSEG Data & Analytics, BARC

FIGURE 15. FY26 EPS growth estimates for Tech industries, YE25 vs. today

<table><tr><td>FY26 EPS Growth Estimates</td><td>12/31/2025</td><td>Today</td></tr><tr><td>Semiconductor and Semiconductor Equipment</td><td>66%</td><td>127%</td></tr><tr><td>Technology Hardware, Storage &amp; Peripherals</td><td>14%</td><td>39%</td></tr><tr><td>Software</td><td>18%</td><td>13%</td></tr><tr><td>Communications Equipment</td><td>14%</td><td>14%</td></tr><tr><td>IT Services</td><td>16%</td><td>4%</td></tr><tr><td>Electronic Equipment and Components</td><td>30%</td><td>33%</td></tr></table>

Data as of 13 June 2026.
Source: Bloomberg, BARC

FIGURE 16. Semis and IT Hardwar

[中间内容因长度限制已省略]

 scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
