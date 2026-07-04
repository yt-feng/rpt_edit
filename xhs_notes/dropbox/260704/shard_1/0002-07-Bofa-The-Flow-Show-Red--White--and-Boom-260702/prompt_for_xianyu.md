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

# Red, White, and Boom

Scores on the Doors: commods 33.3%, oil 19.2%, intl stocks 12.0%, SPX 9.3%, US\$ 2.6%, cash 1.9%, HY 1.8%, IG 0.2%, govt bonds -1.2%, gold -4.7%, bitcoin -30.1% YTD.

Tale of the Tape: Q2 AI/US boom leaders... SOX 88%, KOSPI 64%, biotech 24%, small cap 21%, banks 17%; Q2 war/inflation laggards... Saudi -4%, China -10%, gold -14%, bitcoin -14%, energy -15%, defense -16%, oil -31%; USTs vs. gold breaking 2020s down-trend (Chart 3 – peak inflationary de-globalization), boomy secular breakout for EM & small cap, AI arms race hyperscalers (MAGS) sideways for third straight quarter... all big stuff.

The Price is Right: since independence in 1776... US beats UK on population growth (2.0% vs. 0.8% – Table 1), nominal GDP growth (6.0% vs. 5.8% – Chart 5), real GDP growth (3.6% vs. 2.1%), and US has better inflation record (2.5% vs. 3.9% for UK); but UK has enjoyed lower cost of government debt... UK 10-year bond yield average 5.6% past 250 years vs. 5.8% in US (Chart 6); note US govt debt has grown 5.8% p.a. since 1780), and annual total return from US Treasuries since independence is 5.1%.

The Biggest Picture: red, white, and boom... past 250 years, US stocks (USA Top 100 index) have annualized 3.6% price return (Chart 2), 8.7% total return; even stronger past 150 years (S&P 500 = 4.9% price return & 9.3% total return); but in their first 50 years, US stocks annualized a 2% loss (flat in first 100 years) driven by panics of 1819 & 1837, limited growth drivers until railroads, and highly concentrated indices (First Bank of the United States = >80% of market cap of Philadelphia Stock Exchange in 1792).

Chart 2: Red, White & Boom – US stock prices since independence USA Top 100 index since 1972 (price return, log scale)  
![](images/84a7f33668e405d6ca74fe721973afd67efd82fb642b8459b2e0c5ed8c9cb812.jpg)  
Source: BofA Global Investment Strategy, GFD Finaeon  
BofA GLOBAL RESEARCH

More on page 2...

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 11 to 13.
12990253

## 02 July 2026

Investment Strategy
Global

## BofA Data Analytics

![](images/deaadd2e1d82c7a9459f79a370fb8fd4396136fbbda95d08e1d81bed79a5d74d.jpg)

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

## Chart 1: BofA Bull & Bear Indicator Up to 9.5 from 9.1

![](images/0bc5182417d88537ae561c6bf34a47a92bd0fd9e066ad1ba70991d899445b4ee.jpg)  
Source: BofA Global Investment Strategy. The indicator identified above as the BofA Bull & Bear Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.  
BofA GLOBAL RESEARCH

Weekly Flows: \$55.0bn to cash, \$29.1bn to bonds, \$2.0bn from crypto, \$3.0bn from gold, \$13.9bn from stocks.

## Flows to Know:

• Crypto: \$2.0bn outflow, biggest since Nov'25,

• Gold: \$3.0bn outflow, 7 $^{th}$ week of outflows, longest streak since Mar'24,

• IG bonds: \$17.2bn inflow, 13 $^{th}$ week of inflows,

• HY bonds: \$3.4bn inflow, biggest since May'25,

• US equities: \$17.2bn outflow, biggest since Mar'26,

• Japan equities: \$1.9bn inflow, biggest in 7 weeks,

• Financials: \$2.2bn inflow, biggest since Jan'26,

• Telcos: \$2.4bn inflow, biggest since Aug'25,

• Tech: \$14.3bn inflow, on track for record \$152bn inflow YTD,

• Energy: \$3.2bn outflow, biggest since Jul'24,

• Materials: \$6.8bn outflow, biggest since Mar'26.

BofA Private Clients: \$4.5tn AUM... 65.4% stocks, 17.6% bonds, 9.8% cash; biggest outflow to equities in four weeks; private clients extending duration in USTs... fifth week of outflow from T-bills, inflows to T-notes; private client equity ETF share count up 5.4% YTD, 0.6% MTD, 0.1% past week; in ETFs past four weeks, private clients buying materials, healthcare, munis, and selling Japan, staples, financials.

BofA Bull & Bear Indicator $^{1}$ : rises to 9.5 from 9.1 driven by more bullish hedge fund positioning (reducing S&P 500 futures shorts and reducing VIX futures longs), bond inflow to HY bonds, equity inflows to tech and healthcare; BofA Bull and Bear Indicator "sell signal" triggered May 20 $^{th}$ ; since 2002 there have been 17 "sell signals", average loss for global stocks over 2-3 months is 2-3%, hit ratio of \~60%, max drawdowns of 15-20% (see BofA Bull & Bear Indicator revamp report).

Chart 3: 2020s bear market in Treasuries vs. Gold inflecting
TLT (20+ year US Treasury ETF) vs gold – price relative  
![](images/9b9ea15a7806a69b6dc5f6cfde77ac1cff010607d80b476f26f36fcee84860b4.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 4: June payrolls weak, but profits why jobs stronger in '26 US payrolls MoM (3mma) vs S&P 500 forward EPS YoY (RHS)  
![](images/9516318b3060d88e9a8854adfc8774ef3c41791c316856c388c585fecd05eb75.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Table 1: 250 years of US demographic, economic & financial history
Evolution of US economic and financial markets

<table><tr><td colspan="2">250 years of US history...</td></tr><tr><td>Population growth</td><td>2.0%</td></tr><tr><td>Nominal GDP growth</td><td>6.0%</td></tr><tr><td>Real GDP growth</td><td>3.6%</td></tr><tr><td>Inflation</td><td>2.5%</td></tr><tr><td>Government debt growth</td><td>5.8%</td></tr><tr><td>10-year UST yield</td><td>5.6%</td></tr><tr><td>10-year UST total return</td><td>5.1%</td></tr><tr><td>US stocks price return (USA Top 100 index since 1792)</td><td>3.6%</td></tr><tr><td>US stocks total return</td><td>8.7%</td></tr><tr><td>US stocks real price return</td><td>1.8%</td></tr><tr><td>US stocks real total return</td><td>6.7%</td></tr><tr><td>US stocks price return (S&amp;P 500 index since 1871)</td><td>4.9%</td></tr><tr><td>US stocks total return</td><td>9.3%</td></tr><tr><td>US stocks real price return</td><td>2.4%</td></tr><tr><td>US stocks real total return</td><td>6.7%</td></tr></table>

\*GDP growth and inflation figures are annual averages since 1789; 10-year UST yield is average since 1786; population growth, government debt growth, US stocks returns are CAGRs from 1780, 1792, and 1871, respectively.

Chart 5: US vs. UK nominal GDP since independence
US nominal GDP vs UK nominal GDP (log scale)  
![](images/b993d04782a989f61a8485d719031a8d7a40c0387098104ef0fcbf1ef2f3b284.jpg)  
Source: BofA Global Investment Strategy, GFD Finaeon \*log scale, rebased to 1789  
BofA GLOBAL RESEARCH

Chart 6: US 10-year Treasury yield since 1786
US 10-year Treasury yield since 1786 (%)  
![](images/dc634e4c3642182e43370014b323dad45f7a8909b8a01a4789ea738be94fc4b8.jpg)  
Source: BofA Global Investment Strategy, GFD Finaeon  
BofA GLOBAL RESEARCH

Chart 7: S&P 500 in real terms since 1871
S&P 500 in real terms since 1871 (log scale)  
![](images/827a985ec3c30272da3b2453152c7ae5165bca208d2adc219ca7bbe22d79c2cb.jpg)  
Source: BofA Global Investment Strategy, GFD Finaeon  
BofA GLOBAL RESEARCH

Chart 8: Tech funds on track for record \$152bn inflow in '26 Flows to tech funds, weekly vs 4wk-ma (\$bn)  
![](images/fa2bef8493f45fcd0feba3034dbb08e67471973ab207805037bf31f86239f705.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 9: Biggest inflow to financials since Jan'26 Flows to financials funds, weekly vs 4wk-ma (\$bn)  
![](images/a1fe71ce775f49842d7fb8e08353813619de5011223cddd7d619a9fa24c01b78.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 10: Biggest outflow from materials since Mar'26 Flows to materials funds, weekly vs 4wk-ma (\$bn)  
![](images/b65ff26157643ea28a61410b942671a363668c8040082d04262908013cde6853.jpg)  
Source: BofA Global Investment Strategy, EPFR

Chart 11: Biggest outflow from energy since Jul'24 Flows to energy funds, weekly vs 4wk-ma (\$bn)  
![](images/63c7ab62937ce6f94c6921a3c90a524edaf34b1d4bbe5d7d06ce31aa53c63014.jpg)  
Source: BofA Global Investment Strategy, EPFR

## Asset Class Flows (Table 2)

Equities: \$13.9bn outflow (\$5.2bn to ETFs, \$18.8bn from mutual funds)

Bonds: inflows past 62 weeks (\$29.1bn)

Precious metals: outflows past 7 weeks (\$3.0bn)

## Fixed Income Flows (Chart 12)

IG Bond inflows past 13 weeks (\$17.2bn)

HY Bond inflows past 3 weeks (\$3.4bn)

EM Debt inflows past 3 weeks (\$0.8bn)

Munis inflows past 11 weeks (\$1.9bn)

Govt/Tsy inflows resume (\$4.7bn)

TIPS inflows past 22 weeks (\$0.3bn)

Bank loan inflows past 4 weeks (\$0.8bn)

## Equity Flows (Table 3)

US: outflows past 2 weeks (\$17.2bn)

Japan: inflows past 4 weeks (\$1.9bn)

Europe: outflows past 12 weeks (\$3.7bn)

EM: outflows past 3 weeks (\$4.0bn)

By style: outflows US small cap (\$3.0bn), US large cap (\$11.0bn), US growth (\$13.3bn), US value (\$15.8bn).

By sector: inflows tech (\$14.4bn), com svs (\$2.4bn), financials (\$2.2bn), hcare (\$1.6bn), utilities (\$0.2bn), consumer (\$48mn); outflows real estate (\$0.2bn), energy (\$3.2bn), materials (\$3.8bn).

Table 2: Cumulative YTD flows by asset class Global flows by asset class, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td><td>YTD %AUM</td></tr><tr><td>Equities</td><td>0.0%</td><td>516,137</td><td>1.8%</td></tr><tr><td>ETFs</td><td>0.0%</td><td>802,094</td><td>4.9%</td></tr><tr><td>LO</td><td>-0.1%</td><td>-285,653</td><td>-2.3%</td></tr><tr><td>Bonds</td><td>0.3%</td><td>480,004</td><td>5.0%</td></tr><tr><td>Commodities</td><td>-0.6%</td><td>7,800</td><td>0.8%</td></tr><tr><td>Money-market</td><td>0.5%</td><td>441,922</td><td>4.0%</td></tr></table>

\*week ended 7/1/2026: Source: EPFR Global  
BofA GLOBAL RESEARCH

Table 3: Big YTD inflows to US stocks
Global equity flows by region, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td></tr><tr><td>Total Equities</td><td>0.0%</td><td>516,137</td></tr><tr><td>long-only funds</td><td>-0.1%</td><td>-285,653</td></tr><tr><td>ETFs</td><td>0.0%</td><td>802,094</td></tr><tr><td>Total EM</td><td>-0.1%</td><td>-135,297</td></tr><tr><td>Brazil</td><td>-0.7%</td><td>4,098</td></tr><tr><td>India</td><td>-0.3%</td><td>-8,829</td></tr><tr><td>China</td><td>-0.9%</td><td>-245,942</td></tr><tr><td>Total DM</td><td>0.0%</td><td>651,434</td></tr><tr><td>US</td><td>-0.1%</td><td>315,462</td></tr><tr><td>Europe</td><td>-0.2%</td><td>-15,052</td></tr><tr><td>Japan</td><td>0.2%</td><td>14,659</td></tr><tr><td>International</td><td>0.1%</td><td>313,720</td></tr></table>

Total Equities = Total EM + Total DM
Source: EPFR Global  
BofA GLOBAL RESEARCH

Chart 12: FICC inflows to HY bonds, cash, and bank loans Weekly FICC flows as a % AUM  
![](images/b8435788d6914ee5307b272f0b7ef8b63cad12a8c95221f9e704bed22219d3e6.jpg)  
Source: BofA Global Investment Strategy, EPFR Global  
BofA GLOBAL RESEARCH

## BofA private client flows & allocations

Chart 13: Private clients bought materials, healthcare, munis
BofA private clients 4-week ETF flows as % of AUM  
![](images/ae0619f81b6749a1e623c2f79b425c76bdf0160744943359791b060c5d02df43.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 14: GWIM equity allocation at 65%
BofA private client equity holdings as % of AUM  
![](images/ca1545e605aa21c12a89c9a74b63e0ccb5ba700e522b0dd6ec56006e7238c4dd.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 15: GWIM debt allocation at 18%
BofA private client debt holdings as % of AUM  
![](images/b59cf1dd685e18b566470dbe82b08b04825886e22476fc3e89b65e731817c405.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 16: GWIM cash allocation at 10%
BofA private client cash holdings as % of AUM  
![](images/d1c25273d39c9e53e85142cb15ff4d0b69701b6f17f692b43fa0da6b0ae5d400.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 17: GWIM equity ETFs 21%, debt ETFs 18% of AUM
BofA private client ETF holdings as % of AUM  
![](images/8a57c0734d64a5dabd0a918991ecaf98365fa4e1938318a1cbdc26f396b50ac1.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 18: \$49bn to T-notes vs \$27bn to T-bills since 2020
BofA private client cumulative inflow to Treasuries since 2020 (\$bn)  
![](images/e49ad533d8f5a7db5b0dc491c4d7abd75ea4e4ed4db24fe489ba5c4eb777a70a.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

## The Asset Class Quilt of Total Returns

Chart 19: Historical asset class performance by year
Ranked cross asset returns by year

<table><tr><td>2000</td><td>2001</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026*</td></tr><tr><td>Commodities 58.2%</td><td>US Treasuries 6.7%</td><td>Commodities 39.5%</td><td>MSCI EM 56.3%</td><td>REITS 32.0%</td><td>MSCI EM 34.5%</td><td>REITS 37.5%</td><td>MSCI EM 39.8%</td><td>US Treasuries 14.0%</td><td>MSCI EM 79.0%</td><td>Gold 29.2%</td><td>US Treasuries 9.8%</td><td>REITS 23.8%</td><td>S&amp;P 500 32.4%</td><td>S&amp;P 500 13.7%</td><td>S&amp;P 500 1.4%</td><td>Commodities 17.5%</td><td>MSCI EM 37.8%</td><td>Cash 1.8%</td><td>S&amp;P 500 31.5%</td><td>Gold 24.8%</td><td>Commodities 46.3%</td><td>Commodities 31.1%</td><td>S&amp;P 500 26.3%</td><td>Gold 26.7%</td><td>Gold 60.7%</td><td>Commodities 33.6%</td></tr><tr><td>US Treasuries 13.4%</td><td>Global IG 4.6%</td><td>Gold 25.6%</td><td>MSCI EAFE 39.2%</td><td>Commodities 28.7%</td><td>Commodities 33.7%</td><td>MSCI EM 32.6%</td><td>Commodities 33.0%</td><td>Gold 4.3%</td><td>Global HY 62.0%</td><td>MSCI EM 19.2%</td><td>Gold 8.9%</td><td>Global HY 19.3%</td><td>MSCI EAFE 23.3%</td><td>REITS 11.7%</td><td>US Treasuries 0.8%</td><td>Global HY 14.8%</td><td>MSCI EAFE 25.9%</td><td>US Treasuries 0.8%</td><td>REITS 27.4%</td><td>MSCI EM 18.8%</td><td>REITS 37.1%</td><td>Cash 1.5%</td><td>MSCI EAFE 18.9%</td><td>S&amp;P 500 25.0%</td><td>MSCI EM 32.0%</td><td>MSCI EM 24.0%</td></tr><tr><td>REITS 8.5%</td><td>Cash 4.4%</td><td>Global IG 14.9%</td><td>REITS 33.5%</td><td>MSCI EM 26.0%</td><td>Gold 17.8%</td><td>MSCI EAFE 26.9%</td><td>Gold 31.9%</td><td>Cash 2.1%</td><td>MSCI EAFE 32.5%</td><td>REITS 15.9%</td><td>Global IG 4.5%</td><td>MSCI EM 18.6%</td><td>Global HY 8.0%</td><td>US Treasuries 6.0%</td><td>Cash 0.1%</td><td>S&amp;P 500 12.0%</td><td>S&amp;P 500 22.0%</td><td>Gold -1.9%</td><td>MSCI EAFE 22.8%</td><td>S&amp;P 500 18.4%</td><td>S&amp;P 500 28.7%</td><td>Gold -0.8%</td><td>Global HY 13.4%</td><td>MSCI EM 8.0%</td><td>MSCI EAFE 29.0%</td><td>REITS 12.2%</td></tr><tr><td>Cash 6.2%</td><td>Global HY 3.1%</td><td>US Treasuries 11.6%</td><td>Commodities 30.1%</td><td>MSCI EAFE 20.7%</td><td>MSCI EAFE 14.0%</td><td>Gold 23.2%</td><td>MSCI EAFE 11.6%</td><td>G

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
