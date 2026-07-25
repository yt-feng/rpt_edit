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

# Bonds bringing the heat

Scores on the Doors: oil 60.6%, international stocks 11.4%, US stocks 8.2%, US\$ 3.2%, cash 2.0%, HY 1.6%, IG -0.9%, govt bonds -2.4%, gold -6.7%, bitcoin -25.7% YTD.

Zeitgeist: “Smarter politically for Fed to hike next week, not wait until September, no?”

Tale of the Tape: highest 30-year yield (5.2%) since Jun'07, 30-year real yield (3%) since Nov'08, US tech bond prices at 2-year lows; tighter financial conditions (FCI) surprising more than profits (EPS)...ends only once Fed hikes to calm long-end; watch "up in bond yields, up in bank stocks" bull combo flipping to "higher yields = lower banks"...trigger for risk asset deleveraging; long US dollar best hedge for hawkish Fed.

The Price is Right: lead indicator for industrial cycle “blue collar semis” $^{1}$ down 21% from June peak (Chart 3)...hyperscaling MAGS struggling to hold 200dma (\$65); challenges “boom” consensus (Jul’26 BofA Global FMS); we say long defensives, dividends, duration, short banks (seeing large inflows), brokers, tech, industrials (investors most overweight since Jul’21) best trades for reversal in “boom” expectations.

The Biggest Picture: long-term buy opportunity = Hong Kong property stocks (Chart 2)... same price as 30 years ago, limited downside/big H2'2020s upside likely as play on stable China financial backdrop, secular rise in China/Asia tech, new bulls in EM & real estate, less Dubai, Singapore allure; we are secular buyers of any dips caused by Fed tightening or BoJ currency crisis (Japan yen weakest vs. US\$ since 1986).

Chart 2: Secular upside likely for Hong Kong property
Hang Seng (Hong Kong) Property Index  
![](images/744cecd4bfa1c5623ccb4a5dc9e784ea2c387217002ed1c3bd34965df257fb25.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

More on page 2...

$^{1}$ Texas Instruments, Analog Devices, NXP, Microchip, ON, STMicroelectronics, Infineon, Monolithic Power

## 23 July 2026

Investment Strategy
Global

## BofA Data Analytics

![](images/cf34c0f4506fe43413ef20f405c50f563a457642555dc863920dc359ff8bdf39.jpg)

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

## Chart 1: BofA Bull & Bear Indicator Stays at 9.6

![](images/f70044162e6681a22f6bd167211e9fedcaf6b327eeddc075d0f07b5f53d2d635.jpg)

Source: BofA Global Investment Strategy. The indicator identified above as the BofA Bull & Bear Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

BofA GLOBAL RESEARCH

Weekly Flows: \$30.4bn to stocks, \$14.9bn to bonds, \$2.0bn to gold, \$0.9bn to crypto, \$33.9bn from cash.

## Flows to Know:

• Crypto: \$0.9bn inflow, biggest in 11 weeks (Chart 8),

• Gold: \$2.0bn inflow, biggest since Apr'26,

\- IG bonds: \$5.9bn inflow, 16 $^{th}$ week of inflows,

• EM equities: \$29.6bn inflow, 2 $^{nd}$ biggest inflow ever,

• China equities: \$21.3bn inflow, 3 $^{rd}$ biggest inflow ever (Chart 9),

\- Korea equities: \$1.5bn inflow, record \$16.3bn inflow past 4 weeks (Chart 10),

• UK equities: \$1.2bn outflow, biggest since Nov'25,

• Tech: \$4.0bn inflow, with record \$52.8bn inflow past 4 weeks (Chart 11),

• Financials: \$1.5bn inflow, biggest 4-week inflow since Jan'22 (\$8.8bn - Chart 12).

BofA Private Clients: \$4.5tn AUM...65.6% stocks, 17.5% bonds, 9.6% cash (back at May'26 record-low); private client equity ETF share count up 5.8% YTD, 0.5% past 4 weeks, 0.2% past week; in ETFs past 4 weeks, private clients buying muni bonds & defensive sectors (staples, healthcare), and selling materials, low-vol, and Japan.

BofA Bull & Bear Indicator $^{2}$ : stays at 9.6 on strong tech inflows, partially offset by more bearish hedge fund positioning in oil, 2-year USTs, VIX, and slowing EM debt inflows; BofA Bull and Bear Indicator sell signal triggered May'26 and remains intact; 17 sell signals since '02, average loss for ACWI over 2-3 months is 2-3%, hit ratio of \~60%, max drawdowns of 15-20% (see BofA Bull & Bear Indicator).

FCI > EPS: 23 central bank rate hikes thus far in '26, BofA forecasts 18 more by end '26; modest tightening but summer market blues as 83% of investors in BofA July FMS said no Fed hike before Nov midterms...market pushing back with new 38% implied probability of hike at July 29 $^{th}$ FOMC, Fed hike fully priced by Sep 16 $^{th}$ FOMC; bonds more fearful “no forward guidance Warsh” hikes given 3-4% CPI and labor market not disrupted by AI (biggest macro surprise of year); stock investors less worried thus far, do not yet see level of interest rates as threat to ‘Anything But Bonds’ bull market in risk assets, but would be negatively surprised if equity-friendly US admin tolerates hike to help “tamp brakes” on stocks and anti-billionaire rhetoric in run-up to midterms.

2020s: rise of political populism, globalization to national security, fiscal excess to AI capex excess, Fed independence to deference, US exceptionalism to global rebalancing, inflationary shifts in 2020s investment backdrop (Chart 4); “supply” bigger driver of macro & markets than “demand”; supply of labor constrained by immigration controls... US initial jobless claims at lowest level since 1969; supply of imports constrained by protectionism and tariffs...US set to impose new tariffs on 60 trading partners; supply of oil constrained by geopolitical disruption...\~80mn barrels/day transited by sea around the world, \~64mn barrels through vulnerable “chokepoints” such as Strait of Hormuz, and Bab el-Mandeb (Table 1 & Chart 5); less constrained in future is bond supply (US government still running \$2tn deficit, paying \$1tn in interest per annum despite \$250bn of tariff revenue past 12 months – Charts 6 & 7) and equity supply (free cash flow negative corps = less stock buybacks); why gold & bitcoin basing in ’26, and Main St plays (BKX) outperform Wall St plays (XBD & PSP) in H2’2020s.

Chart 3: “Blue collar” semis...lead indicator for industrial cycle
Equal-weighted blue collar semis index  
![](images/bbb4b52bab40535f643546beb4098cd9e176e4ad1715c6f2e9ac6166ae4ad44c.jpg)  
Source: BofA Global Investment Strategy, Bloomberg. Blue collar semis = Texas Instruments, Analog Devices, NXP, Microchip, ON, STMicroelectronics, Infineon, Monolithic Power

Chart 4: Inflationary shifts in 2020s investment themes
Investment themes for the 2010s vs 2020s  
![](images/c9ec869f3ef2b22f6fd90d36498133fabc3a9cdfe99443d51421b1b68cfd9af2.jpg)  
Source: BofA Global Investment Strategy  
BofA GLOBAL RESEARCH  
BofA GLOBAL RESEARCH

Table 1: \~80mn barrels/day transited by sea around the world
Volume of oil transported through world chokepoints in H1'25

<table><tr><td>Oil trade chokepoint</td><td>Volume of oil transported (mn barrels/day)</td></tr><tr><td>Strait of Malacca</td><td>23.2</td></tr><tr><td>Strait of Hormuz</td><td>20.9</td></tr><tr><td>Suez Canal and SUMED Pipeline</td><td>4.9</td></tr><tr><td>Bab el-Mandeb</td><td>4.2</td></tr><tr><td>Danish Straits</td><td>4.9</td></tr><tr><td>Turkish Straits (Dardanelles)</td><td>3.7</td></tr><tr><td>Panama Canal</td><td>2.3</td></tr><tr><td>Cape of Good Hope</td><td>9.1</td></tr><tr><td>World maritime oil trade</td><td>79.8</td></tr><tr><td>World total oil supply</td><td>104.4</td></tr></table>

Source: U.S. Energy Information Administration  
BofA GLOBAL RESEARCH

Chart 5: Oil transit of \~64mn barrels/day of through “chokepoints” Transit volumes of oil through chokepoints (mn barrels/day, H1'25)  
![](images/bc690893a96748ebda54dfdd28bdac1de4b7829c88090ceb56d2aa6a79fdb521.jpg)  
Source: U.S. Energy Information Administration  
BofA GLOBAL RESEARCH

BofA GLOBAL RESEARCH

BofA GLOBAL RESEARCH

Chart 6: US government still running \$2tn deficit, paying \$1tn in interest per annum
US government revenues and spending for FY 2026  
![](images/cb8a1b10814dacb26a3392a3b1ccdd13570b34c8e94d8c19127ff88139b4958d.jpg)  
Source: BofA Global Investment Strategy, Congressional Budget Office

Chart 7: Revenue from tariffs starting to roll over Cumulative US federal customs duties since 2016  
![](images/c199be350ea56f97f79dd75bc1548cf598ba4a1baf3aa0da9fdbc7797f8b9b5a.jpg)

Chart 8: Big inflows to crypto & gold funds past six years
Cumulative flows to crypto vs gold funds since 2020 (\$bn)  
![](images/f5d31631af3b35c9a55c28a255cb5c35b3fef20f17dbc745c273dd92f6d9069f.jpg)

Chart 9: China equities see $3^{rd}$ biggest weekly inflow on record Flows to China equity funds, weekly vs 4-wk ma (\$bn)  
![](images/c261daf291c29455dfa68a5bccd0a3d8e6a398ac8310bb03957d50bcb6686678.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 10: Korea equities have record \$16bn inflow past 4 weeks Flows to Korea equity funds, weekly vs 4-wk ma (\$bn)  
![](images/eb42df8daf1b149e0ea089e56a8260bd57f812a17272c4f99b344830469fb5f8.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 11: Tech funds have record \$53bn inflow past 4 weeks
Flows to tech equity funds, weekly vs 4-wk ma (\$bn)  
![](images/eceeb32475072356bc7d4fe55bb141814790b5543341a36af0be89c4224aed4f.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 12: Financials funds have biggest 4-week inflow since Jan'22 Flows to financials equity funds, weekly vs 4-wk ma (\$bn)  
![](images/32b000fec1215fdae4eb695d5d826226dde31a12cdafb8724e23c29043d3b087.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

## Asset Class Flows (Table 2)

Equities: \$30.4bn inflow (\$48.0bn to ETFs, \$17.5bn from mutual funds)

Bonds: inflows past 65 weeks (\$14.9bn)

Precious metals: inflows past 3 weeks (\$2.0bn)

## Fixed Income Flows (Chart 13)

IG Bond inflows past 16 weeks (\$5.9bn)

HY Bond inflows resume (\$0.4bn)

EM Debt inflows past 6 weeks (\$0.9bn)

Munis inflows past 14 weeks (\$0.3bn)

Govt/Tsy inflows past 4 weeks (\$5.7bn)

TIPS inflows past 25 weeks (\$0.4bn)

Bank loan inflows past 7 weeks (\$1.0bn)

## Equity Flows (Table 3)

US: outflows resume (\$7.2bn)

Japan: inflows past 7 weeks (\$1.5bn)

Europe: outflows resume (\$1.6bn)

EM: inflows past 3 weeks (\$29.6bn)

By style: outflows US large cap (\$0.1bn), US small cap (\$2.2bn), US value (\$2.8bn), US growth (\$4.4bn).

By sector: inflows tech (\$4.0bn), materials (\$2.0bn), financials (\$1.4bn), hcare (\$0.8bn), energy (\$0.2bn), utils (\$0.2bn), outflows consumer (\$0.3bn), com svs (\$0.5bn), real estate (\$0.5bn).

Table 2: Cumulative YTD flows by asset class Global flows by asset class, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td><td>YTD %AUM</td></tr><tr><td>Equities</td><td>0.1%</td><td>658,672</td><td>2.2%</td></tr><tr><td>ETFs</td><td>0.3%</td><td>986,907</td><td>5.9%</td></tr><tr><td>LO</td><td>-0.1%</td><td>-327,904</td><td>-2.6%</td></tr><tr><td>Bonds</td><td>0.2%</td><td>546,157</td><td>5.7%</td></tr><tr><td>Commodities</td><td>0.5%</td><td>14,445</td><td>1.5%</td></tr><tr><td>Money-market</td><td>-0.3%</td><td>327,989</td><td>2.9%</td></tr></table>

\*week ended 7/22/2026: Source: EPFR Global  
BofA GLOBAL RESEARCH

Table 3: Big YTD inflows to DM stocks
Global equity flows by region, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td></tr><tr><td>Total Equities</td><td>0.1%</td><td>658,672</td></tr><tr><td>long-only funds</td><td>-0.1%</td><td>-327,904</td></tr><tr><td>ETFs</td><td>0.3%</td><td>986,907</td></tr><tr><td>Total EM</td><td>1.0%</td><td>-65,736</td></tr><tr><td>Brazil</td><td>1.7%</td><td>3,979</td></tr><tr><td>India</td><td>0.0%</td><td>-9,240</td></tr><tr><td>China</td><td>3.1%</td><td>-199,466</td></tr><tr><td>Total DM</td><td>0.0%</td><td>724,407</td></tr><tr><td>US</td><td>0.0%</td><td>349,066</td></tr><tr><td>Europe</td><td>-0.1%</td><td>-15,548</td></tr><tr><td>Japan</td><td>0.1%</td><td>19,310</td></tr><tr><td>International</td><td>0.1%</td><td>344,809</td></tr></table>

Total Equities = Total EM + Total DM. Source: EPFR Global  
BofA GLOBAL RESEARCH

Chart 13: FICC inflows to commodities, bank loan, Treasuries Weekly FICC flows as a % AUM  
![](images/ff587039b581622175c61899f9455e874106223ccf6d20453b4683a79480005e.jpg)  
Source: BofA Global Investment Strategy, EPFR Global

## BofA private client flows & allocations

Chart 14: Private clients bought munis, staples, healthcare
BofA private clients 4-week ETF flows as % of AUM  
![](images/a605383258a86b6406be16a283d8918833a3ac2c5560e62276e87c877f6dfc9c.jpg)  
Source: BofA Global investment Strategy

Chart 15: GWIM equity allocation at 66%
BofA private client equity holdings as % of AUM  
![](images/bcaa1e01cae4b96923605ccc177ef807a10b5de824a76cdbbb7aa1ef6c5d72ad.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH  
BofA GLOBAL RESEARCH

Chart 16: GWIM debt allocation at 17%
BofA private client debt holdings as % of AUM  
![](images/e5900d1f54eee556b43df6a044658797c1bb05c150c44a47cc8eecf60c5bed0c.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 17: GWIM cash allocation at 10%
BofA private client cash holdings as % of AUM  
![](images/69a03c2778ba96689ac55e34076395c14731dcbc444bb38f3cc3e369919a30c9.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 18: GWIM equity ETFs 21%, debt ETFs 18% of AUM
BofA private client ETF holdings as % of AUM  
![](images/bde2b3742f0c485956d3b7ba242c144f096c38d4cb4636d6a7fbda49120733b0.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 19: \$50bn to T-notes vs \$27bn to T-bills since 2020
BofA private client cumulative inflow to Treasuries since 2020 (\$bn)  
![](images/c5796c4d6d5e4b0f26ae8e67480f226371aae6260b5a7477dec3b519a798dd40.jpg)  
Source: BofA Global investment Strategy

BofA GLOBAL RESEARCH

## The Asset Class Quilt of Total Returns

Chart 20: Historical asset class performance by year
Ranked cross asset returns by year

<table><tr><td>2000</td><td>2001</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026*</td></tr><tr><td>Commodities 58.2%</td><td>US Treasuries 6.7%</td><td>Commodities 39.5%</td><td>MSCI EM 56.3%</td><td>REITS 32.0%</td><td>MSCI EM 34.5%</td><td>REITS 37.5%</td><td>MSCI EM 39.8%</td><td>US Treasuries 14.0%</td><td>MSCI EM 79.0%</td><td>Gold 29.2%</td><td>US Treasuries 9.8%</td><td>REITS 23.8%</td><td>S&amp;P 500 32.4%</td><td>S&amp;P 500 13.7%</td><td>S&amp;P 500 1.4%</td><td>Commodities 17.5%</td><td>MSCI EM 37.8%</td><td>Cash 1.8%</td><td>S&amp;P 500 31.5%</td><td>Gold 24.8%</td><td>Commodities 46.3%</td><td>Commodities 31.1%</td><td>S&amp;P 500 26.3%</td><td>Gold 26.7%</td><td>Gold 60.7%</td><td>Commodities 57.7%</td></tr><tr><td>US Treasuries 13.4%</td><td>Global IG 4.6%</td><td>Gold 25.6%</td><td>MSCI EAFE 39.2%</td><td>Commodities 28.7%</td><td>Commodities 33.7%</td><td>MSCI EM 32.6%</td><td>Commodities 33.0%</td><td>Gold 4.3%</td><td>Global HY 62.0%</td><td>MSCI EM 19.2%</td><td>Gold 8.9%</td><td>Global HY 19.3%</td><td>MSCI EAFE 23.3%</td><td>REITS 11.7%</td><td>US Treasuries 0.8%</td><td>Global HY 14.8%</td><td>MSCI EAFE 25.9%</td><td>US Treasuries 0.8%</td><td>REITS 27.4%</td><td>MSCI E

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
