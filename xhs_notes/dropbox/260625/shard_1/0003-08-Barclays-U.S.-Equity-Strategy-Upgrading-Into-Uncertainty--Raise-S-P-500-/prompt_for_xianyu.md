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

Looking ahead, we introduce a preliminary FY27 EPS estimate of \$389, reflecting a modest deceleration in growth. Our framework assumes a partial recovery in consumption on a Y/Y basis, coupled with continued strength in industrial production as the lagged effects of prior tightening fade. This is partially offset by a normalization in nominal pricing power, particularly as disinflationary forces broaden. The resulting bull and bear cases of \$397/\$380 capture a similar set of crosscurrents, with upside tied to a more durable demand recovery and sustained Tech momentum, whi

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
