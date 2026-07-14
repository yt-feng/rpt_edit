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
# Global Fund Manager Survey

# Pain trades: duration, dividend, defensives

## BofA July Global Fund Manager Survey

Bottom line: investor sentiment more bullish driven by optimism on macro “boom”, AI capex, dovish Fed; FMS cash levels fall from 4.1% to uber-low 3.6%, US equity OW biggest since Dec'24, as forecasts for “boom” highest since Feb'22; BofA Bull & Bear Indicator @ extreme bull reading of 9.4... says reduce equity & high-beta exposure, summer upside for risk assets to remain stymied by bull positioning.

FMS on Macro: record 54% predict no landing for economy (39% soft & 2% hard), CPI expectations lowest since Jan'25 as FMS oil price forecast slumps from \$86/bbl to \$71/bbl; asked will Fed hike before midterms 83% say no, i.e. Fed stays dovish; outcome of US midterms... 44% say DEM House/GOP Senate, followed by DEM sweep (27%).

FMS on AI: investors say long global semis most crowded trade (huge 82% - Chart 1) & AI hyperscaler capex most likely source of credit event (48%), trimmed July tech longs to hedge AI risks; but no one short... asked if AI stocks in bubble 48% said no (vs. 43% yes), asked if an AI hyperscaler will announce a capex cut... 61% said no (vs. 28% yes).

FMS on AA: investors adding to equity length via US, Eurozone, healthcare, industrials (most OW since Jul'21), cutting UK (most UW since Aug'20), EM, commodities, energy (largest drop since Jun'10), staples (most UW since Feb'14); note first time since May'17 investors predict low-dividend yield stocks to outperform high-dividend yielders.

FMS Contrarian Trades: based on extreme FMS positions best contrarian trades for a surprise hawkish Fed = long staples & gold, short semis & healthcare, and for “peak boom” = long bonds, UK & high dividend yielders, short industrials & banks.

Chart 1: 82% of FMS investors say “long global semiconductors” is world’s most crowded trade. What do you think is currently the most crowded trade?

![](images/915da701f06ed70cf12093bddd5cf6f4d94f304b3c11907c90f240de94fb1cbc.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 24 to 26.
12993843

## 14 July 2026

Investment Strategy
Global

## BofA Data Analytics

![](images/081a1fc5855c6dc99195335f3fc4ae0f1592707622ca717bb5e891ef13ac3428.jpg)

## Michael Hartnett

Investment Strategist
BofAS
+1 646 855 1508
michael.hartnett@bofa.com

## Anya Shelekhin

Aanya shelekhin
Investment Strategist
BofAS
+1 646 855 3753
anya.shelekhin@bofa.com

## Myung-Jee Jung

myung-jee.jung
Investment Strategist
BofAS
+1 646 855 0389
myung-jee.jung@bofa.com

Jessica Guo
Investment Strategist
BofAS
+1 646 855 0033
jessica.guo@bofa.com

## Notes to Readers

Source for all tables and charts: BofA Fund Manager Survey, DataStream

Survey period July 2 $^{nd}$ to 9 $^{th}$ , 2026

210 panellists with \$555bn AUM participated in the survey. 181 participants with \$484bn AUM responded to the Global FMS questions and 109 participants with \$274bn AUM responded to the Regional FMS questions.

## How to join the FMS panel

Investors/clients are encouraged to sign up to participate in the Survey. This can be done by contacting Michael Hartnett or your BofA sales representative.

Participants in the survey will continue to receive the full set of monthly results but only for the relevant month in which they participate.

OW: overweight; UW: underweight

AA: asset allocation

## Charts of the Month

Chart 2: BofA Global FMS investor sentiment most bullish since Feb'26
Percentile rank of FMS growth expectations, cash level, and equity allocation  
![](images/5b25ab67232715b3e6d8ab7c489dda50cc582ccbdd73a31c0e0822b2efe96018.jpg)  
Percentile rank of FMS growth expectations + cash AA + equity AA (scale 1-10)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

July BofA Global FMS shows investors are the most bullish since Feb'26; our broadest measure of FMS sentiment, based on cash levels, equity allocation, and global growth expectations, rose to 7.2 from 6.0.

Chart 3: Cash level falls to 3.6% from 4.1%
BofA FMS average cash level (% of AUM)  
![](images/922b4c1c237e2d389e0ef05b08736f482cfadf5ea8e9b37b24ad7261e9b4ebb2.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

BofA FMS cash level dropped from 4.1% to uber-low 3.6% of AUM (lowest since Feb'26), triggering a sell signal on the BofA Global FMS Cash Rule ("sell" when cash at or below 4.0%).

Table 1: On past occasions of FMS cash 3.6% or lower... stocks -1% in two weeks that followed Average returns for MSCI ACWI & US Treasuries in 1wk/2mo after certain FMS cash levels

<table><tr><td rowspan="2">FMS cash %</td><td rowspan="2"># of signals since 2002</td><td colspan="2">Global equities</td><td colspan="2">Treasuries</td></tr><tr><td>2 weeks</td><td>1 month</td><td>2 weeks</td><td>1 month</td></tr><tr><td>3.5</td><td>11</td><td>-1.1%</td><td>-1.5%</td><td>0.6%</td><td>0.6%</td></tr><tr><td>3.6</td><td>16</td><td>-0.8%</td><td>-0.5%</td><td>0.6%</td><td>0.4%</td></tr><tr><td>3.7</td><td>24</td><td>-0.5%</td><td>0.1%</td><td>0.5%</td><td>0.4%</td></tr><tr><td>3.8</td><td>39</td><td>-0.1%</td><td>0.5%</td><td>0.3%</td><td>0.1%</td></tr><tr><td>3.9</td><td>57</td><td>-0.1%</td><td>0.6%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>4.0</td><td>71</td><td>0.1%</td><td>0.3%</td><td>0.3%</td><td>0.3%</td></tr></table>

Source: BofA Global Fund Manager Survey, Bloomberg

Note FMS cash level fell to 3.6% or lower in 16 prior instances since 2002... on average, stocks fell 1% in the two weeks after (-0.5% in the month after) and Treasuries outperformed.

Chart 4: 54% say "no landing," 39% say "soft landing," 2% say "hard landing" What is the most likely outcome for the global economy in the next 12 months?  
![](images/1524a9bcf9864bf7f4363c3ad02c1c5e7c0fb037a10c91dc5b106dfabe6268a4.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

Chart 5: Global growth expectations rise to 5-month high
Net % expect stronger global economy and S&P 500 (YoY %)  
![](images/cc30eb51bd4abe7c45d3b6907b7af98e6dec9ff633afebf9d9fcbbaf4b44f2ca.jpg)  
Source: BofA Global Fund Manager Survey, Bloomberg  
BofA GLOBAL RESEARCH

Chart 6: Consensus flip from higher to lower inflation tempering rate hike expectations
Net % expecting higher global CPI and net % expecting higher short-term rates  
![](images/d1e8d5faafcf36bef58fcda29e6d97a8b0502c6c41ac635d13b3b94095742076.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

Asked what the most likely outcome for the global economy is in the next 12 months...

A record 54% of investors expect "no landing".

Another 39% expect a "soft landing," while a record-low 2% expect a "hard landing."

Global growth optimism rose to a 5-month high in July... net 21% expect a stronger economy.

Macro expectations are catching up to US equity performance.

On inflation... net 4% of July FMS investors expect lower global inflation, a big flip from last month when net 45% expected higher inflation.

The outlook on rates fell alongside the CPI outlook... net 1% expect higher short-term rates, down from 34%.

Chart 7: FMS oil forecast drops to \$71/bbl by end '26 (from \$86)
In which of the following ranges do you expect the price of oil to trade in by year-end 2026?  
![](images/39f0bdfe5d6645c38b0fff3e2da8f7b45d21731ba4e8f994d23963a66ee8ca64.jpg)  
Source: BofA Global Fund Manager Survey

Chart 8: $83\%$ say no Fed hike before November midterm election Will the Fed hike before the November US midterms?  
![](images/9abf41ecdf4fd511e2aa43a665a1724446786ea052939aa44f6fcb2e2e79f2d7.jpg)  
Source: BofA Global Fund Manager Survey

Chart 9: 44% expect DEM House/GOP Senate post-midterms, 27% say DEM sweep What outcome do you expect from the 2026 US midterm elections?  
![](images/643aa6a1a0c5a8c9f7409ed88c886d822bdd0448a0e5ba04e71b3bbecd5aaa7c.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

Inflation expectations were lowered as FMS end-year oil price forecast slumped 17% from \$86/bbl in June (on a weighted-average basis) to \$71/bbl.

Just 2% of investors expect oil to trade above \$90/bbl.

On policy... asked whether the Fed will hike before US midterms, 83% said no (14% said yes).

Separately when asked how the Fed will change the Fed Funds rate in the next year, just 36% said they expected at least one hike and 29% expect no change.

On the US midterm elections (Republicans currently hold majorities in both the House and Senate)...

Expectations for a DEM sweep (Democratic House & Democratic Senate) rose to 27% from 22%, but FMS investors say the most likely outcome is a split Democratic House & Republican Senate (44%).

Chart 10: 61% of FMS say no hyperscaler capex cut in '26
Will one of the AI hyperscalers announce a cut in capex in 2026?  
![](images/071c207a248cab3ed7fce215a22fdb71faf219f66dc8b6b4d1c9c37955e31d8d.jpg)  
Source: BofA Global Fund Manager Survey  
A greater share of FMS investors also continue to believe that AI stocks are not in a bubble (48% vs the 43% that say "yes").

Chart 11: 48% of FMS investors think no AI bubble (vs 43% yes)
Do you think that AI stocks are in a bubble?  
![](images/928636ce36b809102341a2496903b7acdc4db444ecc33c59ef76e34d50eb4958.jpg)  
Source: BofA Global Fund Manager Survey

FMS investors also remain positive on the outlook for AI... asked if one of the AI hyperscalers would announce a cut in capex in 2026, the majority (61%) of FMS investors expect no cut to hyperscaler capex (vs 28% "yes").

Chart 12: 45% of FMS investors say AI bubble is the biggest tail risk
What do you consider the biggest 'tail risk'?  
![](images/9060c351812840d363b3240229705698e5370bad262d23711b7e0b5b1fae15e4.jpg)  
BofA GLOBAL RESEARCH

"AI bubble" rose to the top spot for the biggest tail risk in July per 45% of FMS investors (up from 28% last month).

In June, the #1 perceived tail risk was '2 $^{nd}$ wave inflation'... this has dropped to #2 (26% of investors, from 34%).

BofA GLOBAL RESEARCH

Chart 13: AI hyperscaler capex = #1 most likely source of a systemic credit event
What is the most likely source of a systemic credit event?  
![](images/457e375b0918d4d08373483172c6b5a328cf273ce7e72382549c4fb332b2b5bf.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

Chart 14: Gold deemed most undervalued since Mar'23
Net % say gold is overvalued  
![](images/4c6f6f813c9598c919dc1c64427cd6bbf9cc9077ab76ebdba47a9fb550857514.jpg)  
Source: BofA Global Fund Manager Survey

Chart 15: FMS investors most OW US equities since Dec'24
Net % overweight US equities  
![](images/d498468231957d68832e6385e5e07b650c82cd11ee1cc3a0eabef591cfef7b09.jpg)  
Source: BofA Global Fund Manager Survey

July also saw 48% of FMS investors say that 'AI hyperscaler capex' is the most likely source of a systemic credit event, followed by 34% 'private credit.'

Asked about the current price of gold, net 6% of FMS investors say gold is undervalued (most undervalued since Mar'23).

## On asset allocation...

FMS investors increased their overweight in US equities to net 24% OW, the biggest OW since Dec'24 and the 3 $^{rd}$ highest US weighting in the past 5 years.

Chart 16: FMS investors most UW UK equities since Aug'20
Net % overweight UK equities  
![](images/4a6bde5e5fd0745bed955de5f96e8cb4a5e544f60d172d8a02476a4bd4837234.jpg)  
On the other hand, FMS investors further reduced their allocation to UK equities to net 37% UW, the lowest allocation since Aug'20.  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

Chart 17: Lowest FMS allocation to consumer stocks since May'06
Net % OW staples + net % OW discretionary  
![](images/2d7e57d9a4edca138835086a5a39ea20d73cbd15d2a123d472006843af703be0.jpg)  
Source: BofA Global Fund Manager Survey  
On sector allocation...  
FMS investors were net 53% underweight consumer sectors (staples + discretionary), the lowest allocation since May'06.  
For the first time since May'17, FMS investors expect low-dividend yield stocks to outperform high-dividend yield stocks.

Chart 18: FMS says low-dividend yield > high-dividend yield for first time since May'17
Net % think high dividend yield will outperform vs low dividend yield stocks

![](images/afbc23edee3d87684ec4db0f300b11e8739f0927234b8fa1eb3236a83bfd3f17.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

BofA GLOBAL RESEARCH

Chart 19: July rotation into healthcare, EU and bonds vs out of energy, commodities and UK Monthly change in FMS investor positioning  
![](images/41c2d0b0b92de1ba8cbb432436affc4570f5112d352eb5734daef558a0ae70d3.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

Chart 20: FMS most OW stocks, EM and healthcare vs most UW UK, bonds and staples
FMS absolute positioning (net % overweight)  
![](images/91dfba80030990532de8d9a57bddc7ffe8d107e2d370bf20adca88767914646d.jpg)  
Source: BofA Global Fund Manager Survey

Chart 21: Relative to history, OW utilities, US and industrials vs UW staples, UK and energy FMS positioning vs history (z-score)  
![](images/a165ff462d246344e26cb6507694c8a59e1666504703d1408ee195804d60ff1a.jpg)  
Source: BofA Global Fund Manager Survey  
This chart shows July's monthly changes in FMS investor allocation.  
Investors increased allocation to healthcare, Europe, and bonds...

... and reduced allocation to energy, commodities, and UK.

This chart shows absolute FMS investor positioning (net % overweight).

In July, investors are most overweight equities, EM, and healthcare...

... vs. most underweight UK, bonds, and consumer staples.

This chart shows absolute FMS investor positioning (net % overweight).

In July, investors are most overweight utilities, US, and industrials...

... vs. most underweight consumer staples, UK, and energy.

Chart 22: Evolution of Global FMS “biggest tail risk” History of Global FMS “biggest tail risk” answers  
![](images/62f0ccb8bb90f829f689c7226927f7cd5224c3d9c7d46253c97dd054415aa911.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

\- This chart shows the full history of the biggest “tail risk” for markets from BofA’s monthly Global Fund Manager Survey.

\- The dominant concerns of investors since 2011 have been Eurozone debt, Chinese growth, populism, quantitative tightening & trade wars, global coronavirus, inflation, and central bank rate hikes; US\$ debasement, AI bubble, and geopolitics.

• The top tail risk is “AI bubble” (45%) in July.

Chart 23: Evolution of Global FMS “most crowded trade” History of Global FMS “most crowded trade” answers  
![](images/2ec28448f00a76c6c5ed68efd5e134379ace136606e6e85d8028d8c75e03e411.jpg)  
Source: BofA Global Fund Manager Survey  
BofA GLOBAL RESEARCH

\- This chart shows the full history of the most “crowded trade” according to BofA’s monthly Global Fund Manager Survey.

\- The market leadership has been relatively narrow since 2013, shifting from high yielding debt; long US\$; long Quality; long Tech; long Emerging Markets; long US Treasuries, long US tech & growth stocks, long Bitcoin, long commodities, long tech, long commodities, long US dollar, long Magnificent Seven, short US dollar, long gold, long oil, long global semiconductors.

\- The #1 FMS most cro

[中间内容因长度限制已省略]

ct information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any

securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
