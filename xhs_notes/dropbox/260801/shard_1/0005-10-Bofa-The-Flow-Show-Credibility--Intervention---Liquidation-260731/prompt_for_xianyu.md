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

# Credibility, Intervention & Liquidation

Scores on the Doors: oil 45.7%, intl stocks 8.7%, SPX 8.6%, cash 2.1%, US\$ 1.6%, HY bonds 1.2%, IG bonds -1.2%, govt bonds -2.5%, gold -5.5%, bitcoin -26.1% YTD.

The Price is Right: credibility event...Fed nakedly dovish, so financial conditions to continue to tighten until Fed forced to restore credibility via aggressive hikes (= higher yields into Warsh @ Jackson Hole Aug 28 $^{th}$ ); we say retreat/rotate from risk assets rather than reload until higher inflation and one of those nasty “higher yields-lower dollar” vigilante events (Chart 5) forces monetary & fiscal policy U-turns.

Tale of the Tape: intervention event...US/Japan/Korea coordinated FX intervention most imp event of week as policy makers try to short-circuit risk of JPY collapse, JGB yield melt-up, contagion into Korea/Taiwan bonds, disorderly UST-negative capital flows...better work; also shows new era of AI PKOs (price keeping operations)...US policymakers will act to prevent weakness in Japan/Korea/Taiwan stocks from impeding race with China for AI supremacy.

The Biggest Picture: liquidation events...KOSDAQ (Korea small cap tech) @ Oct'22 lows (Chart 2), Mirae (largest Korea broker) -66% @ Jul'07 levels (Chart 3), stock price of many US retail darlings under water (e.g., SPCX 30%, NASA 36%, DRNZ 20%, DRAM 10% below VWAP average investor entry point YTD), plus Situational Awareness; no big rally on lovey-dovey Fed + AI PKOs + liquidation...risk assets capped into mid-terms.

## Chart 2: K-pop

Korea small cap tech stocks (KOSDAQ)

![](images/d263d7343516654e2fda3ca73b6d9023446f4e76d757e1a4526547a1e312ba0c.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

More on page 2...

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 12 to 14.
13002280

## 31 July 2026

Investment Strategy Global

## BofA Data Analytics

![](images/87e03185fbc9737785647963682033c6b4c220a8679b61badb7fee0b2b131b87.jpg)

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
Down to 9.4 from 9.6  
![](images/477a79715fc537aa5b83a0d8c99e26bca77dc3dbc9ece973a4bcdaf1a5b3b522.jpg)  
Source: BofA Global Investment Strategy. The indicator identified above as the BofA Bull & Bear Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.  
BofA GLOBAL RESEARCH

Weekly Flows: \$63.7bn to stocks, \$12.5bn to bonds, \$5.0bn to cash, \$1.3bn to gold, \$0.4bn from crypto.

## Flows to Know:

• IG bonds: \$5.8bn inflow, 17 $^{th}$ week of inflows,

\- Global equities: \$63.7bn inflow, fearless buy-the-dip continues,

• US equities: \$30.4bn inflow, largest in 6 weeks,

• China equities: \$15.9bn inflow, largest 4-week inflow ever (\$62.4bn – Chart 6),

\- Korea equities: \$1.6bn inflow, pace slowing but no day of Korea outflow in past week (Chart 7),

• Tech: \$15.7bn inflow, largest 5-week inflow ever (\$68.5bn – Chart 8),

\- Semiconductor ETFs $^{1}$ : \$5.3bn inflow, no reversal in big \$53bn inflow YTD despite SOX -25% (Chart 9),

• Consumer: \$0.6bn inflow, largest in 9 weeks.

BofA Private Clients: \$4.5tn AUM...65.5% stocks, 17.5% bonds, 9.7% cash; private clients continue to add to stocks... equity ETF share count up 6.1% YTD, 0.6% past 4 weeks, and 0.3% in past week; in ETFs past 4 weeks, private clients buying municipal bonds, Japan equity, EM debt ETFs, selling low-volatility, bank loan, precious metal ETFs.

BofA Bull & Bear Indicator: down to 9.4 from 9.6 on EM debt outflows; extreme bull market positioning remains headwind for risk assets, as has been case since BofA Bull & Bear Indicator "sell signal" triggered May $26^{\text{th}}$ (since when a lot of rotation and a little retreat...healthcare up $9\%$ , banks $8\%$ vs. ACWI $-3\%$ , MAGS $-8\%$ , SOX $-11\%$ , oil $-11\%$ , bitcoin $-15\%$ ); "old" Bull & Bear Indicator at 7.4 (see BofA Bull & Bear Indicator).

## On Portfolios:

\- We recommend investors retreat from risk assets and/or rotate into some defensives (e.g. staples), duration (e.g. REITs, small cap, biotech) and US dollar, all protected from ongoing tightening of financial conditions, less cyclically vulnerable than banks, industrials, semis to bull consensus “no macro landing, no Fed hike, no AI capex cut, no DEM midterm sweep” disappointment.

\- This week's combo of coordinated FX policy intervention & market liquidation normally bullish "end of deleveraging" events (note XBD & NYA bounce back to high), but policymakers fine-tuning (trying to cap) government bond yields rather than adopting monetary shock therapy (Fed & BoJ hikes) to reverse inflation risks and lower bond yields & cost of capital (why MAGS can't break out to new highs).

\- Policymakers continue to corroborate asset allocation view that equity market is “too big to fail” as economy dependent on wealth effect and AI capex; political leaders continue to struggle for popularity (Trump approval ratings falling again – Chart 4) so keeping upward pressure on government spending until higher inflation and one of those nasty “higher yields-lower dollar” vigilante events (Chart 5) forces fiscal policy U-turn; only then will asset allocation to bonds rise.

Chart 3: Largest Korean broker Mirae at same price as in Jul'07
Mirae Asset Securities price (in KRW)  
![](images/9df296344d0e4144cadaf975f7123223b003449139c99df208b548b0978439d3.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 4: U-turn in Trump approval ratings
Trump approval ratings  
![](images/0796ff8b24a0bf800b8ff412fb1bd8593550eaa65a372737bb1a719ecf9ea3ff.jpg)  
Source: BofA Global Investment Strategy, Real Clear Politics  
BofA GLOBAL RESEARCH

Chart 5: Correlation between yields & US dollar close to turning -ve US 30-year Treasury yield vs US dollar – 50-day correlation  
![](images/50d2735260a6eae7671bb53a927215d4d6aeffc699dcbc8220a33b4da81ac8fa.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 6: Largest 4-week inflow to China equities ever Flows to China equity funds, weekly vs 4-wk ma (\$bn)  
![](images/bea199e355782ca32ca892d996510caf9ed84a39cf475375ce7f5c34f1ae90f4.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 7: Weekly flows to Korea equities still positive Flows to Korea equity funds, weekly vs 4-wk ma (\$bn)  
![](images/cc54cadaa0b3a615c9b853fc42f8d001d844ace95f18193a606e6d8830c73386.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

Chart 8: Largest 5-week inflow to tech funds ever Flows to tech equity funds, weekly vs 4-wk ma (\$bn)  
![](images/0d3d5e26e283e8494b065de1d17926882c06f63c76b44d4c9b265300b8b903e0.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

\*Fund flows for 8 largest semiconductor ETFs: SMH, SOXX, USD, XSD, FTXL, PSI, SOXQ, DRAM.

Chart 9: \$53bn of inflows to semiconductor ETFs YTD
Cumulative flows to semiconductor ETFs vs SOX price index (RHS)  
![](images/4ab32d64731dbd491186bbc30d7724553bd4491fb818f7bb6bff9bd2a13bbe47.jpg)  
Source: BofA Global Investment Strategy, EPFR, Bloomberg.

BofA GLOBAL RESEARCH

## Asset Class Flows (Table 1)

Equities: \$63.7bn inflow (\$71.1bn to ETFs, \$7.4bn from mutual funds)

Bonds: inflows past 66 weeks (\$12.5bn)

Precious metals: inflows past 4 weeks (\$1.3bn)

## Fixed Income Flows (Chart 10)

IG Bond inflows past 17 weeks (\$5.8bn)

HY Bond inflows past 2 weeks (\$41mn)

EM Debt outflows resume (\$0.2bn)

Munis inflows past 15 weeks (\$2.0bn)

Govt/Tsy inflows past 5 weeks (\$2.6bn)

TIPS inflows past 26 weeks (\$0.8bn)

Bank loan inflows past 8 weeks (\$1.0bn)

## Equity Flows (Table 2)

US: inflows resume (\$30.4bn)

Japan: inflows past 8 weeks (\$1.2bn)

Europe: outflows past 2 weeks (\$2.3bn)

EM: inflows past 4 weeks (\$24.0bn)

By style: inflows US large cap (\$20.6bn), US value (\$1.1bn), outflows US small cap (\$0.6bn), US growth (\$1.9bn).

Table 1: Cumulative YTD flows by asset class Global flows by asset class, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td><td>YTD %AUM</td></tr><tr><td>Equities</td><td>0.1%</td><td>722,381</td><td>2.5%</td></tr><tr><td>ETFs</td><td>0.3%</td><td>1,058,054</td><td>6.3%</td></tr><tr><td>LO</td><td>-0.1%</td><td>-335,291</td><td>-2.6%</td></tr><tr><td>Bonds</td><td>0.2%</td><td>558,678</td><td>5.8%</td></tr><tr><td>Commodities</td><td>0.5%</td><td>14,782</td><td>1.5%</td></tr><tr><td>Money-market</td><td>-0.3%</td><td>332,994</td><td>3.0%</td></tr></table>

\*week ended 7/29/2026: Source: EPFR Global  
BofA GLOBAL RESEARCH

Table 2: Big YTD inflows to DM stocks
Global equity flows by region, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td></tr><tr><td>Total Equities</td><td>0.1%</td><td>722,381</td></tr><tr><td>long-only funds</td><td>-0.1%</td><td>-335,291</td></tr><tr><td>ETFs</td><td>0.3%</td><td>1,058,054</td></tr><tr><td>Total EM</td><td>1.0%</td><td>-41,718</td></tr><tr><td>Brazil</td><td>1.7%</td><td>3,959</td></tr><tr><td>India</td><td>0.0%</td><td>-9,923</td></tr><tr><td>China</td><td>3.1%</td><td>-183,534</td></tr><tr><td>Total DM</td><td>0.0%</td><td>764,099</td></tr><tr><td>US</td><td>0.0%</td><td>379,506</td></tr><tr><td>Europe</td><td>-0.1%</td><td>-17,827</td></tr><tr><td>Japan</td><td>0.1%</td><td>20,477</td></tr><tr><td>International</td><td>0.1%</td><td>354,604</td></tr></table>

Total Equities = Total EM + Total DM. Source: EPFR Global  
BofA GLOBAL RESEARCH

By sector: inflows tech (\$15.7bn), hcare (\$1.1bn), consumer (\$0.6bn), financials (\$0.4bn), utils (\$0.1bn), real estate (\$4mn); outflows materials (\$11mn), com svs (\$0.2bn), energy (\$0.5bn).

Chart 10: FICC inflows to commodities, bank loan, Treasuries Weekly FICC flows as a % AUM

![](images/2940b018ebc6acdcaa98d5f4b7430a4025c5d6e3ea218b3799bab4aef7fd2546.jpg)  
Source: BofA Global Investment Strategy, EPFR Global  
BofA GLOBAL RESEARCH

## BofA private client flows & allocations

Chart 11: Private clients bought munis, Japan, EM debt
BofA private clients 4-week ETF flows as % of AUM

BofA private client debt holdings as % of AUM  
![](images/de629fa1a51516cd4d1ec726bedfdd7d4c42d32ea69f7042f9d08305a4db09ed.jpg)  
Source: BofA Global investment Strategy

Chart 12: GWIM equity allocation at 65%
BofA private client equity holdings as % of AUM  
![](images/e7a62f832716b97f781847c2e4e2469c2d77c903750704e78db65d53fdc7c2a6.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH  
BofA GLOBAL RESEARCH

Chart 13: GWIM debt allocation at 17%  
![](images/ad1f6f2092714b458e9e850b14fb173218491935542689e40d7a1c3dc90a8102.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH  
Chart 14: GWIM cash allocation at 10%  
BofA private client cash holdings as % of AUM

![](images/cb1fbf9132169f6b325e7b7c5e702f8a86a6a951a85276ab8097ff4274b925d9.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 15: GWIM equity ETFs 21%, debt ETFs 18% of AUM
BofA private client ETF holdings as % of AUM  
![](images/1723dec6057a000493433961774114f64ef483c71051a2642ec2be0c01f06cb0.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 16: \$51bn to T-notes vs \$27bn to T-bills since 2020
BofA private client cumulative inflow to Treasuries since 2020 (\$bn)  
![](images/23dd0c29d280ce982bf53811be2c781340acfbba92f3fc2bca4b8a30039fb90d.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

## The Asset Class Quilt of Total Returns

Chart 17: Historical asset class performance by year
Ranked cross asset returns by year

<table><tr><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td> $2026^*$ </td></tr><tr><td>MSCI EM 39.8%</td><td>US Treasuries 14.0%</td><td>MSCI EM 79.0%</td><td>Gold 29.2%</td><td>US Treasuries 9.8%</td><td>REITS 23.8%</td><td>S&amp;P 500 32.4%</td><td>S&amp;P 500 13.7%</td><td>S&amp;P 500 1.4%</td><td>Commodities 17.5%</td><td>MSCI EM 37.8%</td><td>Cash 1.8%</td><td>S&amp;P 500 31.5%</td><td>Gold 24.8%</td><td>Commodities 46.3%</td><td>Commodities 31.1%</td><td>S&amp;P 500 26.3%</td><td>Gold 26.7%</td><td>Gold 60.7%</td><td>Commodities 55.6%</td></tr><tr><td>Commodities 33.0%</td><td>Gold 4.3%</td><td>Global HY 62.0%</td><td>MSCI EM 19.2%</td><td>Gold 8.9%</td><td>Global HY 19.3%</td><td>MSCI EAFE 23.3%</td><td>REITS 11.7%</td><td>US Treasuries 0.8%</td><td>Global HY 14.8%</td><td>MSCI EAFE 25.9%</td><td>US Treasuries 0.8%</td><td>REITS 27.4%</td><td>MSCI EM 18.8%</td><td>REITS 37.1%</td><td>Cash 1.5%</td><td>MSCI EAFE 18.9%</td><td>S&amp;P 500 25.0%</td><td>MSCI EM 32.0%</td><td>REITS 16.8%</td></tr><tr><td>Gold 31.9%</td><td>Cash 2.1%</td><td>MSCI EAFE 32.5%</td><td>REITS 15.9%</td><td>Global IG 4.5%</td><td>MSCI EM 18.6%</td><td>Global HY 8.0%</td><td>US Treasuries 6.0%</td><td>Cash 0.1%</td><td>S&amp;P 500 12.0%</td><td>S&amp;P 500 22.0%</td><td>Gold -1.9%</td><td>MSCI EAFE 22.8%</td><td>S&amp;P 500 18.4%</td><td>S&amp;P 500 28.7%</td><td>Gold -0.8%</td><td>Global HY 13.4%</td><td>MSCI EM 8.0%</td><td>MSCI EAFE 29.0%</td><td>MSCI EM 12.5%</td></tr><tr><td>MSCI EAFE 11.6%</td><td>Global IG -8.3%</td><td>REITS 31.7%</td><td>S&amp;P 500 15.1%</td><td>Global HY 2.6%</td><td>MSCI EAFE 17.9%</td><td>REITS 0.7%</td><td>Global IG 3.2%</td><td>MSCI EAFE -0.8%</td><td>MSCI EM 11.2%</td><td>Gold 12.9%</td><td>Global HY -3.3%</td><td>Commodities 20.1%</td><td>Global IG 10.3%</td><td>MSCI EAFE 11.9%</td><td>US Treasuries -12.9%</td><td>Gold 12.7%</td><td>Global HY 7.5%</td><td>S&amp;P 500 18.5%</td><td>MSCI EAFE 9.6%</td></tr><tr><td>US Treasuries 9.1%</td><td>Global HY -27.9%</td><td>S&amp;P 500 26.5%</td><td>Global HY 13.9%</td><td>S&amp;P 500 2.1%</td><td>S&amp;P 500 16.0%</td><td>Global IG 0.1%</td><td>Gold 0.1%</td><td>REITS -3.4%</td><td>Gold 8.6%</td><td>REITS 11.5%</td><td>Global IG -3.4%</td><td>MSCI EM 18.6%</td><td>MSCI EAFE 8.4%</td><td>Global HY 1.4%</td><td>Global HY -13.2%</td><td>REITS 11.3%</td><td>Commodities 5.5%</td><td>Global HY 9.9%</td><td>S&amp;P 500 7.6%</td></tr><tr><td>Global IG 7.3%</td><td>S&amp;P 500 -37.0%</td><td>Commodities 26.1%</td><td>Commodities 13.3%</td><td>Cash 0.1%</td><td>Global IG 11.1%</td><td>Cash 0.1%</td><td>Cash 0.0%</td><td>Global IG -3.8%</td><td>Global IG 4.3%</td><td>Global HY 10.2%</td><td>REITS -3.9%</td><td>Gold 17.9%</td><td>US Treasuries 8.2%</td><td>Cash 0.0%</td><td>MSCI EAFE -13.9%</td><td>MSCI EM 10.1%</td><td>Cash 5.3%</td><td>Global IG 9.8%</td><td>Cash 2.1%</td></tr><tr><td>S&amp;P 500 5.5%</td><td>Commoditie

[中间内容因长度限制已省略]

ent not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies. Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
