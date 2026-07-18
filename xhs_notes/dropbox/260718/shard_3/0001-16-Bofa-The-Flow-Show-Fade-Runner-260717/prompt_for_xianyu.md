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

# Fade Runner

Scores on the Doors: commods 49.0%, oil 38.2%, intl stocks 12.3%, SPX 10.1%, US\$ 2.4%, cash 2.0%, HY 1.8%, IG -0.4%, govt bonds -1.7%, gold -8.3%, bitcoin -26.9% YTD.

The Biggest Picture: Bank of Korea hikes rates (25bps to 2.75%), $1^{\text{st}}$ hike since '23, signaled more hikes to come; Korean real policy rates still -ve (-45bps) but rally in won says financial conditions starting to tighten in world's most speculative market (Chart 2).

Tale of the Tape: SOX index trading just 33% above 200dma vs. 76% June 3 $^{rd}$ (overbought level surpassed only at Mar'00 tech bubble top - Chart 4); SOX -20%, SOXL -55% from peak...big price unwind but no positioning unwind in chip stocks to buy...another \$2.3bn inflow to 8 largest semiconductor ETFs this week $^{1}$ (adding to YTD \$46bn = 31% of AUM – Chart 3), and past 3 weeks record \$48bn inflows to tech funds.

The Price is Right: BofA Bull & Bear Indicator at 9.6...extreme bull positioning says best summer tactic remains retreat from risk assets and/or rotate to duration, defensives, dividend yields, US dollar, rather than reload (not “time to buy”); MAGS key to watch within dystopian tape...MAGS break <\$65 = broader market retreat that hurts longs in cyclicals (banks, brokers, industrials)...MAGS advance >\$70 = best reload signal.

Chart 2: Rally in Korean won says Korean financial conditions starting to tighten KOSPI vs KRW to USD exchange rate  
![](images/94110303d956d98000c920b5529cd079d885f333195ce5932355483f2660db3a.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
$^{1}$ Includes fund flows for 8 ETFs... SMH, SOXX, USD, XSD, FTXL, PSI, SOXQ, DRAM

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 13 to 15.
12995766

## 17 July 2026 Corrected

Investment Strategy
Global

## BofA Data Analytics

![](images/dd5706d8039195a4b21794ffe808b21208a3ab90e04b322ce0801a39db6487ef.jpg)

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

## Chart 1: BofA Bull & Bear Indicator Rises to 9.6

![](images/8d35b2b8674a93301fbbe6400e1c04f76ca2079cf5131ab8da17e698894432f5.jpg)

Source: BofA Global Investment Strategy. The indicator identified above as the BofA Bull & Bear Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

BofA GLOBAL RESEARCH

BofA GLOBAL RESEARCH

Weekly Flows: \$55.8bn to stocks, \$20.0bn to bonds, \$0.5bn to gold, \$0.1bn from crypto, \$119.6bn from cash.

## Flows to Know:

• Cash: \$119.6bn outflow, biggest since Apr'26,

\- IG bonds: \$9.5bn inflow, 15 $^{th}$ week of inflows,

• EM equities: \$25.0bn inflow, biggest since Apr'25 (Chart 14),

• Tech: \$15.6bn inflow, record 3-week inflow (\$48.8bn – Chart 15),

• Financials: \$2.7bn inflow, biggest since Jan'26 (Chart 16).

BofA Private Clients: \$4.6tn AUM...65.8% allocation to stocks, 17.3% to bonds, 9.6% to cash (record low); private clients continue to add stocks...equity ETF share count up 8.9% YTD, 0.9% in past 4 weeks, 0.2% in past week; private clients buying muni bond and defensive sector ETFs (staples, healthcare, utilities) past 4 weeks, selling materials, low-volatility and energy ETFs.

BofA Bull & Bear Indicator $^{2}$ : up from 9.4 to 9.6 pushing further into extreme bull territory on plunge in institutional cash levels (3.6% in July FMS (see report)), strong equity inflows, stronger global stock index breadth, partially offset by rising AT1 credit spreads; BofA Bull & Bear “sell signal” remains in place, extreme bull positioning says markets “toppy”, reduce equity exposure, retreat or rotate much smarter summer tactic for risk assets than reload.

BofA Global Fund Manager Survey: July survey showed investors very bullish driven by expectation of no landing for economy, no hike by the Fed, no cut to AI hyperscaler capex, and no DEM sweep in US midterms; no landing, no hike, no cut, no sweep...why no bears; July survey also showed best contrarian trades, hedges, opportunities...

When 54% say no landing = long duration, defensives, dividend yield: record 54% in BofA July Global FMS say no landing for global economy, expectations of macro boom highest since Feb'22; global bank stocks, best expression of "boom", agree...US banks at all-time highs (Chart 5), Japan banks highest since Nov'96 (still 49% below ATHs – Chart 6), UK banks highest since Dec'07 (19% below ATHs – Chart 7), European banks highest since Jun'08 (39% below ATHs – Chart 8); but when all positioned for boom, contrarian trade is buy 3Ds of unloved Duration (10-year government bonds), Defensives (like staples, Mag7 monopolies), high Dividend yielding stocks, as well as long bonds, UK & high dividend yielders, short industrials & banks.

When 83% say no Fed hike = long US dollar: 83% of FMS investors say no Fed hike before November midterms; yet US CPI still on trend to end 2026 at 3.9% (CPI 3mma trend = 0.3% - Chart 9), Hormuz shut again with US crude inventories lowest in 45 years (43 days of supply – Chart 10) as investor end-year oil price assumption slumps to \$71/bbl from \$86/bbl; best trade for surprise Fed hike before Nov = long US Dollar.

When 61% say no cut in hyperscaler AI capex = long Mag7/software, short SOX, short cyclicals: AI capex soaring (Chart 11) and 61% of FMS investors say no AI hyperscaler to announce capex cut before end-26; but hyperscaler free cash flow turning negative (Chart 12), funding pressure in bond market continue...Oracle CDS & IG tech bond (59bps back in Sep'25 now 87bps – Chart 13) trending back toward highs, and "long MAGS, short SOX" performance recent weeks hints capex cut coming; biggest surprise would be capex cut does not catalyze Mag7 to new highs (> \$71), which given

\*Includes fund flows for 8 ETFs... SMH, SOXX, USD, XSD, FTXL, PSI, SOXQ, DRAM the big negative growth & asset price implication of this would catalyze shorts in banks, brokers, industrials.

Chart 3: Big \$46bn inflow into semiconductor ETFs\* this year
Cumulative inflows to semiconductor ETFs since 2017 (\$bn)  
![](images/e84d4772c4dad971fe2e24ed0571e64e93d44935da05161a3bce3ab0a0a2875a.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 4: SOX no longer “peak overbought”
SOX % deviation from 200-day moving average  
![](images/905d51bce8b935749823fd00147da881a22afff1619e739b5065879521d41efa.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 5: US bank stocks at all-time high S&P 500 banks index  
![](images/27a594722e06819f61e2e5a9c64ac00a874d1a163d0911733d8b6c7f6de3b0b4.jpg)  
Source: BofA Global Investment Strategy, Bloomberg,  
BofA GLOBAL RESEARCH

Chart 6: Japan bank stocks highest since Nov'96 TOPIX banks index  
![](images/944ba78df9362d127d30bf16609962980b451f97dd193d91b774fc19fb47f048.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 7: UK bank stocks highest since Dec'07
FTSE 350 banks index  
![](images/5dd9e6e0556d3c31043a9272d45c40ea638507d360195e1f97906a80130b6d10.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 8: European bank stocks highest since Jun'08
Euro Stoxx banks index  
![](images/1517256c03c257915728449e88d49525c3c3c055287c7dac80d476804fec69ea.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Source: BofA Global Investment Strategy, EPFR

Chart 9: US CPI trend = 3.9% CPI at year-end
Paths for US CPI assuming monthly growth rate  
![](images/bfbe18c9f69f8980b812785fb9046c38efedc9bcd3566770ee91a9d6d740fb37.jpg)  
BofA GLOBAL RESEARCH  
Source: BofA Global Investment Strategy, Bloomberg

Chart 10: US crude inventories lowest in 45 years
US crude oil, day supply including Strategic Petroleum Reserve

![](images/3ee09e334d1970f077d8ed8f294f4359c53b35621dbe216e8014cc6d2fd4497e.jpg)  
BofA GLOBAL RESEARCH

Chart 11: Hyperscaler capex expected to jump 87% to \$769bn in '26 Al hyperscaler capex forecasts by year (\$bn)  
![](images/2b9d5962e5ed8445f9c5d20a5f1f9b913d6ca18c7ed07abbd67017c9bf7f4207.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 12: Hyperscaler free cash flow expected to turn negative in '27 Al hyperscaler free cash flow forecasts by year (\$bn)  
![](images/6e03c686e7d2b173fdfffa4a289d289272b9b96b8060a0440d488784c790bec8.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 13: Oracle CDS trending back to highs US IG tech spreads vs Oracle 5-year CDS  
![](images/71fd91aa50a3e9e5394bd4c1c15be390a6256815ddec7550c4b1756ac7b43632.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 14: Biggest inflow to EM equities since Apr'25 Flows to EM equity funds, weekly vs 4wk-ma (\$bn)  
![](images/e393d1648bcb2bd2670dfed4f4b3193a64ab1cf62b95810ff87e7540ab979b1c.jpg)  
BofA GLOBAL RESEARCH

Chart 15: Record inflow to tech funds past 3 weeks
Flows to tech equity funds, weekly vs 4wk-ma (\$bn)  
![](images/0d98642e4d4b184cb8406ca5bba5a223ab2c56f9e492ab2c606e0d5f7294c70e.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 16: Biggest inflow to financials since Jan'26 Flows to financials equity funds, weekly vs 4wk-ma (\$bn)  
![](images/eed92a2486f7706e6b33bdba178cbe8efc07375f3b191053737b59110a78fd3e.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

## Asset Class Flows (Table 1)

Equities: \$55.8bn inflow (\$74.7bn to ETFs, \$19.0bn from mutual funds)

Bonds: inflows past 64 weeks (\$20.0bn)

Precious metals: inflows past 2 weeks (\$0.5bn)

## Fixed Income Flows (Chart 17)

IG Bond inflows past 15 weeks (\$9.5bn)

HY Bond outflows resume (\$0.3bn)

EM Debt inflows past 5 weeks (\$0.9bn)

Munis inflows past 13 weeks (\$1.8bn)

Govt/Tsy inflows past 3 weeks (\$6.5bn)

TIPS inflows past 24 weeks (\$0.6bn)

Bank loan inflows past 6 weeks (\$0.6bn)

## Equity Flows (Table 2)

US: inflows past 2 weeks (\$15.7bn)

Japan: inflows past 6 weeks (\$1.9bn)

Europe: inflows past 2 weeks (\$0.7bn)

EM: inflows past 2 weeks (\$25.0bn)

By style: inflows US large cap (\$14.9bn), US value (\$0.3bn), outflows US small cap (\$0.8bn), US growth (\$5.3bn),

By sector: inflows tech (\$15.6bn), financials (\$2.7bn), hcare (\$0.7bn), energy (\$0.6bn), materials (\$0.5bn), utils (\$0.3bn), telcos (\$0.1bn); outflows real estate (\$0.5bn), consumer goods (\$1.1bn).

Table 1: Cumulative YTD flows by asset class Global flows by asset class, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td><td>YTD %AUM</td></tr><tr><td>Equities</td><td>0.2%</td><td>628,247</td><td>2.1%</td></tr><tr><td>ETFs</td><td>0.4%</td><td>938,952</td><td>5.7%</td></tr><tr><td>LO</td><td>-0.1%</td><td>-310,431</td><td>-2.5%</td></tr><tr><td>Bonds</td><td>0.2%</td><td>531,307</td><td>5.6%</td></tr><tr><td>Commodities</td><td>0.1%</td><td>9,949</td><td>1.0%</td></tr><tr><td>Money-market</td><td>-1.1%</td><td>361,846</td><td>3.2%</td></tr></table>

\*week ended 7/15/2026: Source: EPFR Global  
BofA GLOBAL RESEARCH

Table 2: Big YTD inflows to DM stocks
Global equity flows by region, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td></tr><tr><td>Total Equities</td><td>0.2%</td><td>628,247</td></tr><tr><td>long-only funds</td><td>-0.1%</td><td>-310,431</td></tr><tr><td>ETFs</td><td>0.4%</td><td>938,952</td></tr><tr><td>Total EM</td><td>0.8%</td><td>-95,332</td></tr><tr><td>Brazil</td><td>-1.7%</td><td>3,565</td></tr><tr><td>India</td><td>-0.2%</td><td>-9,258</td></tr><tr><td>China</td><td>2.4%</td><td>-220,785</td></tr><tr><td>Total DM</td><td>0.1%</td><td>723,579</td></tr><tr><td>US</td><td>0.1%</td><td>356,293</td></tr><tr><td>Europe</td><td>0.0%</td><td>-13,991</td></tr><tr><td>Japan</td><td>0.2%</td><td>17,774</td></tr><tr><td>International</td><td>0.2%</td><td>338,009</td></tr></table>

Total Equities = Total EM + Total DM
Source: EPFR Global  
BofA GLOBAL RESEARCH

Chart 17: FICC inflows to USTs, TIPS, bank loans Weekly FICC flows as a % AUM  
![](images/3f3947f0ed662299ba786a164314fb7660c57bb9d05719379d7cf2cd1a5f86c0.jpg)  
Source: BofA Global Investment Strategy, EPFR Global  
BofA GLOBAL RESEARCH

## BofA private client flows & allocations

Chart 18: Private clients bought munis, staples, healthcare
BofA private clients 4-week ETF flows as % of AUM  
![](images/f3c685c96f714477c224f5b1f52030d4d2439c274ce8990195b7f698c00f0bf6.jpg)  
Source: BofA Global investment Strategy

Chart 19: GWIM equity allocation at 66%
BofA private client equity holdings as % of AUM  
![](images/05c700da88b12245c1d361a47965504978e4bef41229d0caa5090d1bf3f1a592.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH  
BofA GLOBAL RESEARCH

![](images/5d56b9c9a0d8ddc08472213c7ccfa45546a1d0b439f087debed3eb1b7c8706c3.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 21: GWIM cash allocation at 10%
BofA private client cash holdings as % of AUM  
![](images/7c553d8d8671b1231b3c046ea907e7c5747be987bbfd5480287b4a3bc44c9fa5.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 22: GWIM equity ETFs 21%, debt ETFs 18% of AUM
BofA private client ETF holdings as % of AUM  
![](images/df397b2db89439a971f966c0c602ceddb087b6c6e7a35756bb65bbe5fb40e580.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 23: \$50bn to T-notes vs \$27bn to T-bills since 2020
BofA private client cumulative inflow to Treasuries since 2020 (\$bn)  
![](images/496b69192d512fd173fba26ca4bce3ca3c64b99bf87b321ad6eaeecff48ab573.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

## The Asset Class Quilt of Total Returns

Chart 24: Historical asset class performance by year
Ranked cross asset returns by year

<table><tr><td>2000</td><td>2001</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026*</td></tr><tr><td>Commodities 58.2%</td><td>US Treasuries 6.7%</td><td>Commodities 39.5%</td><td>MSCI EM 56.3%</td><td>REITS 32.0%</td><td>MSCI EM 34.5%</td><td>REITS 37.5%</td><td>MSCI EM 39.8%</td><td>US Treasuries 14.0%</td><td>MSCI EM 79.0%</td><td>Gold 29.2%</td><td>US Treasuries 9.8%</td><td>REITS 23.8%</td><td>S&amp;P 500 32.4%</td><td>S&amp;P 500 13.7%</td><td>S&amp;P 500 1.4%</td><td>Commodities 17.5%</td><td>MSCI EM 37.8%</td><td>Cash 1.8%</td><td>S&amp;P 500 31.5%</td><td>Gold 24.8%</td><td>Commodities 46.3%</td><td>Commodities 31.1%</td><td>S&amp;P 500 26.3%</td><td>Gold 26.7%</td><td>Gold 60.7%</td><td>Commodities 49.3%</td>

[中间内容因长度限制已省略]

ect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
