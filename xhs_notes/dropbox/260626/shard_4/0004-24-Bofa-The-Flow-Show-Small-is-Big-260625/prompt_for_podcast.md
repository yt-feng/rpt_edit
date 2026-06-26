你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
\*Eccles to Powell use annualized 10Y yield & S&P 500 returns from term start to term end  
\*Warsh uses non-annualized returns from term start to 6/25/26

# The Flow Show

# Small is Big

Scores on the Doors: oil 21.9%, international stocks 11.5%, SPX 7.5%, US\$ 3.2%, cash 1.7%, HY bonds 1.4%, IG bonds 0.1%, govt bonds -1.3%, gold -7.2%, bitcoin -30.5% YTD.

Zeitgeist: "How far do hyperscalers need to fall for market to start trading capex cuts?"

Tale of the Tape: MAGS <\$60 (Chart 3), AUDJPY <110 (Chart 4), yield curve inversion catalysts for proper risk-off summer; meantime 16% margins (Chart 6) = love for stocks, and liquidity pulled from mega-cap AI arms racers simply racing into semis & illiquid cyclicals (small/mid-cap, housing, REITs) to front-run Trump pivot to affordability.

The Price is Right: gold <\$4k, silver <\$60, XBT <\$60k as Iran and era of sanctions end & dollar pop; but 2020s to remain era of fractured geopolitics and populist politics prioritizing booms over inflation; we say US dollar a “rent” not an “own”, gold <\$4k good entry point for gold (Chart 5), and secular trade remains long EM (Chart 2).

The Biggest Picture: since Warsh's term started on May $22^{\text{nd}}$ , US Treasuries up $3.2\%$ , stocks $-1.6\%$ ; early days and nouveau-hawkish Fed yet to convince any investor to abandon core "Anything But Bonds" allocation, but Warsh thus far mirroring "lower yield" Fed chairs (Eccles, Volcker, Greenspan, Bernanke – Table 1), and long the long-end remains most contrarian secular trade in markets.

Table 1: So far Warsh mirroring few Fed chairs whose terms saw lower bond yields History of Fed chairs + annualized 10-year yield & S&P 500 performance

<table><tr><td>Fed Chair</td><td>Term Start</td><td>Term End</td><td>10Y Yield Change (bps)*</td><td>S&amp;P 500 Change (%)*</td></tr><tr><td>Eccles</td><td>Nov&#x27;34</td><td>Jan&#x27;48</td><td>-7</td><td>4%</td></tr><tr><td>McCabe</td><td>Apr&#x27;48</td><td>Mar&#x27;51</td><td>7</td><td>12%</td></tr><tr><td>Martin</td><td>Apr&#x27;51</td><td>Jan&#x27;70</td><td>28</td><td>8%</td></tr><tr><td>Burns</td><td>Feb&#x27;70</td><td>Jan&#x27;78</td><td>2</td><td>1%</td></tr><tr><td>Miller</td><td>Mar&#x27;78</td><td>Aug&#x27;79</td><td>62</td><td>13%</td></tr><tr><td>Volcker</td><td>Aug&#x27;79</td><td>Aug&#x27;87</td><td>-2</td><td>16%</td></tr><tr><td>Greenspan</td><td>Aug&#x27;87</td><td>Jan&#x27;06</td><td>-23</td><td>8%</td></tr><tr><td>Bernanke</td><td>Feb&#x27;06</td><td>Jan&#x27;14</td><td>-24</td><td>4%</td></tr><tr><td>Yellen</td><td>Feb&#x27;14</td><td>Feb&#x27;18</td><td>7</td><td>12%</td></tr><tr><td>Powell</td><td>Feb&#x27;18</td><td>May&#x27;26</td><td>22</td><td>13%</td></tr><tr><td>Warsh</td><td>May&#x27;26</td><td>--</td><td>-17</td><td>-2%</td></tr></table>

Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

More on page 2...

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 10 to 12.
12987196

## 25 June 2026

Investment Strategy
Global

BofA
Data Analytics

![](images/a27d5ec51b38e0ae5c198245e5d9d0ad3092e37bf67119570ed55bfc65a10d7d.jpg)

## Michael Hartnett

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
Down to 9.1 from 9.2  
![](images/c9fb50450a3fb12e933bf4ad80abae357ebd602844eb06fb0cf0035343a49fb5.jpg)

Source: BofA Global Investment Strategy. The indicator identified above as the BofA Bull & Bear Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

BofA GLOBAL RESEARCH

Weekly Flows: \$16.6bn to bonds, \$0.5bn from gold, \$0.6bn from crypto, \$5.0bn from equities, \$25.5bn from cash (biggest in 8 weeks).

## Flows to Know:

• Treasuries \$94mn outflow, 1 $^{st}$ in 9 weeks;

• IG bonds: \$9.0bn inflow, smallest in 8 weeks;

\- US stocks: 8.5bn outflow, 1 $^{st}$ outflow since Mar'26 (follows record 119.2bn inflow);

• Tech: \$9.3bn record outflow (follows record \$19.2bn inflow);

• Real estate: \$0.9bn inflow, biggest since Mar'24;

• Infrastructure: \$1.5bn inflow, biggest in 6 weeks;

• Energy: \$1.5bn outflow, biggest since Apr'25 (Chart 7).

BofA Private Clients: \$4.6tn AUM...65.8% stocks, 17.3% bonds, 9.6% cash; biggest inflow to equities in 6 weeks; private client equity ETF share count up 5.3% YTD, 0.5% MTD, 0.2% past week; in ETFs past 4 weeks, private clients buying materials, munis, TIPS, and selling Japan, staples, financials.

BofA Bull & Bear Indicator $^{1}$ : falls to 9.1 from 9.2 driven by equity outflows and weaker credit market technicals (widening HY/AT1 spreads); BofA Bull and Bear Indicator "sell signal" triggered on May'26; 17 "sell signals" since '02, average loss for global stocks over 2-3 months is 2-3%, hit ratio of \~60%, max drawdowns of 15-20% (see note, BofA Bull & Bear Indicator).

Chart 2: Secular trade remains long EM > US stocks
S&P 500 vs Emerging Markets – price relative  
![](images/8ac53cb182fece5b4f3b45afba56da81a91569298390a42c0922cb2d7141629c.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 3: If MAGS < 60... “risk-off” for summer MAGS (Magnificent Seven ETF)  
![](images/217e26494d374aa1a0f4c1e8a587528ece0bd635ff508fc4a51143a5b6168b73.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 4: AUDJPY <110 would be summer “risk-off” catalyst
Australian dollar / Japanese yen  
![](images/adf311de27f391b3f2ff13797392ecb830b7c5f4ae982b7231a7a0d778cb0c20.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 5: Now = good entry point into gold
Gold spot price since 1960 (\$/oz)  
![](images/fc300f8fe28e9b26f427f475e9c34d7dec8188fa45d572029462a24cc0c83dfc.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 6: 16% margins keep the love for stocks
S&P 500 operating margin vs S&P 500 2-yr return (RHS)  
![](images/5a416d2aada20ff7bac232a946c5ca35999f6523c6bd5dce4d9e1e7a0bbe6ef3.jpg)  
Source: BofA Global Investment Strategy, Bloomberg  
BofA GLOBAL RESEARCH

Chart 7: \$1.5bn outflow, biggest since Apr'25 Flows to energy funds, weekly vs 4wk-ma (\$bn)  
![](images/402efbce4a4f7bed078b437d5eb24e511b91d70c7c78286c6b6dc36be890437b.jpg)  
Source: BofA Global Investment Strategy, EPFR  
BofA GLOBAL RESEARCH

## Asset Class Flows (Table 2)

Equities: \$5.0bn outflow (\$9.2bn to ETFs, \$14.1bn from mutual funds)

Bonds: inflows past 61 weeks (\$16.6bn)

Precious metals: outflows past 6 weeks (\$0.4bn)

## Fixed Income Flows (Chart 8)

IG Bond inflows past 12 weeks (\$9.0bn)

HY Bond inflows past 2 weeks (\$1.8bn)

EM Debt inflows past 2 weeks (\$3.2bn)

Munis inflows past 10 weeks (\$1.2bn)

Govt/Tsy 1 $^{st}$ outflow in 9 weeks (94mn)

TIPS inflows past 21 weeks (\$69mn)

Bank loan inflows past 3 weeks (\$0.5bn)

## Equity Flows (Table 3)

US: 1 $^{st}$ outflow in 13 weeks (\$8.5bn)

Japan: inflows past 3 weeks (\$0.5bn)

Europe: outflows past 11 weeks (\$1.3bn)

EM: outflows past 2 weeks (\$11.1bn)

By style: inflows US large cap (\$28.6bn), US value (\$5.8bn), US growth (\$1.2bn); outflow US small cap (\$9.2bn).

By sector: inflows REITs (\$0.9bn), healthcare (\$0.3bn), utilities (\$0.1bn); outflows consumer (\$0.1bn), com svs (\$0.5bn), financials (\$1.0bn), energy (\$1.5bn), materials (\$2.2bn), tech (\$9.3bn).

Table 2: Cumulative YTD flows by asset class Global flows by asset class, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td><td>YTD %AUM</td></tr><tr><td>Equities</td><td>0.0%</td><td>529,996</td><td>1.8%</td></tr><tr><td>ETFs</td><td>0.1%</td><td>796,919</td><td>4.8%</td></tr><tr><td>LO</td><td>-0.1%</td><td>-266,845</td><td>-2.1%</td></tr><tr><td>Bonds</td><td>0.2%</td><td>450,929</td><td>4.7%</td></tr><tr><td>Commodities</td><td>-0.2%</td><td>13,095</td><td>1.3%</td></tr><tr><td>Money-market</td><td>-0.2%</td><td>386,922</td><td>3.5%</td></tr></table>

\*week ended 06/24/2026: Source: EPFR Global  
BofA GLOBAL RESEARCH

Table 3: Table 5: Big YTD inflows to DM stocks
Global equity flows by region, \$mn

<table><tr><td></td><td>Wk % AUM</td><td>YTD</td></tr><tr><td>Total Equities</td><td>0.0%</td><td>529,996</td></tr><tr><td>long-only funds</td><td>-0.1%</td><td>-266,845</td></tr><tr><td>ETFs</td><td>0.1%</td><td>796,919</td></tr><tr><td>Total EM</td><td>-0.4%</td><td>-131,267</td></tr><tr><td>Brazil</td><td>-0.9%</td><td>4,249</td></tr><tr><td>India</td><td>-0.1%</td><td>-8,580</td></tr><tr><td>China</td><td>-1.6%</td><td>-240,191</td></tr><tr><td>Total DM</td><td>0.0%</td><td>661,263</td></tr><tr><td>US</td><td>-0.1%</td><td>332,669</td></tr><tr><td>Europe</td><td>-0.1%</td><td>-11,347</td></tr><tr><td>Japan</td><td>0.0%</td><td>12,804</td></tr><tr><td>International</td><td>0.2%</td><td>304,798</td></tr></table>

Total Equities = Total EM + Total DM  
Source: EPFR Global  
BofA GLOBAL RESEARCH

Chart 8: FICC inflows to EM debt, HY bonds, and bank loans
Weekly FICC flows as a % AUM  
![](images/db7bd05d3bcae4c2aa1ed651c0528879c30c0d66d0f2c32a321c3e1dabdcd717.jpg)  
Source: BofA Global Investment Strategy, EPFR Global

## BofA private client flows & allocations

Chart 9: Private clients bought materials, munis, TIPS
BofA private clients 4-week ETF flows as % of AUM

![](images/00cedbb001fce2adbf0edf959554ce84e33a93cf3b8cf11226c657ae02ab1b6c.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 10: GWIM equity allocation at 66%
BofA private client equity holdings as % of AUM  
![](images/db69964ca1710b3da314369e82a474fa76a0ee81a8bd989723563fadbb4cc43d.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 11: GWIM debt allocation at 17%
BofA private client debt holdings as % of AUM  
![](images/e6f803b26d298fa861586874555341569320bd5a6023c96b7ea6000160ad3297.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 12: GWIM cash allocation at 10%
BofA private client cash holdings as % of AUM  
![](images/e416d0a3d5aa48de8d3825885c5114f1b3374657b1043c083b175fa8ef8083c7.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 13: GWIM equity ETFs 21%, debt ETFs 18% of AUM
BofA private client ETF holdings as % of AUM  
![](images/dce3f835d68dc53d69bc7ba074b5987db7606942756f6c8029146881b1507af7.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

Chart 14: \$48bn to T-notes vs \$28bn to T-bills since 2020
BofA private client cumulative inflow to Treasuries since 2020 (\$bn)  
![](images/758418878a35e1921e31a2f3da2321474814d0bd5d9075d0e34f7759ce8be9e3.jpg)  
Source: BofA Global investment Strategy  
BofA GLOBAL RESEARCH

## The Asset Class Quilt of Total Returns

Chart 15: Historical asset class performance by year
Ranked cross asset returns by year

<table><tr><td>2000</td><td>2001</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026*</td></tr><tr><td>Commodities 58.2%</td><td>US Treasuries 6.7%</td><td>Commodities 39.5%</td><td>MSCI EM 56.3%</td><td>REITS 32.0%</td><td>MSCI EM 34.5%</td><td>REITS 37.5%</td><td>MSCI EM 39.8%</td><td>US Treasuries 14.0%</td><td>MSCI EM 79.0%</td><td>Gold 29.2%</td><td>US Treasuries 9.8%</td><td>REITS 23.8%</td><td>S&amp;P 500 32.4%</td><td>S&amp;P 500 13.7%</td><td>S&amp;P 500 1.4%</td><td>Commodities 17.5%</td><td>MSCI EM 37.8%</td><td>Cash 1.8%</td><td>S&amp;P 500 31.5%</td><td>Gold 24.8%</td><td>Commodities 46.3%</td><td>Commodities 31.1%</td><td>S&amp;P 500 26.3%</td><td>Gold 26.7%</td><td>Gold 60.7%</td><td>Commodities 32.7%</td></tr><tr><td>US Treasuries 13.4%</td><td>Global IG 4.6%</td><td>Gold 25.6%</td><td>MSCI EAFE 39.2%</td><td>Commodities 28.7%</td><td>Commodities 33.7%</td><td>MSCI EM 32.6%</td><td>Commodities 33.0%</td><td>Gold 4.3%</td><td>Global HY 62.0%</td><td>MSCI EM 19.2%</td><td>Gold 8.9%</td><td>Global HY 19.3%</td><td>MSCI EAFE 23.3%</td><td>REITS 11.7%</td><td>US Treasuries 0.8%</td><td>Global HY 14.8%</td><td>MSCI EAFE 25.9%</td><td>US Treasuries 0.8%</td><td>REITS 27.4%</td><td>MSCI EM 18.8%</td><td>REITS 37.1%</td><td>Cash 1.5%</td><td>MSCI EAFE 18.9%</td><td>S&amp;P 500 25.0%</td><td>MSCI EM 32.0%</td><td>MSCI EM 24.5%</td></tr><tr><td>REITS 8.5%</td><td>Cash 4.4%</td><td>Global IG 14.9%</td><td>REITS 33.5%</td><td>MSCI EM 26.0%</td><td>Gold 17.8%</td><td>MSCI EAFE 26.9%</td><td>Gold 31.9%</td><td>Cash 2.1%</td><td>MSCI EAFE 32.5%</td><td>REITS 15.9%</td><td>Global IG 4.5%</td><td>MSCI EM 18.6%</td><td>Global HY 8.0%</td><td>US Treasuries 6.0%</td><td>Cash 0.1%</td><td>S&amp;P 500 12.0%</td><td>S&amp;P 500 22.0%</td><td>Gold -1.9%</td><td>MSCI EAFE 22.8%</td><td>S&amp;P 500 18.4%</td><td>S&amp;P 500 28.7%</td><td>Gold -0.8%</td><td>Global HY 13.4%</td><td>MSCI EM 8.0%</td><td>MSCI EAFE 29.0%</td><td>REITS 13.6%</td></tr><tr><td>Cash 6.2%</td><td>Global HY 3.1%</td><td>US Treasuries 11.6%</td><td>Commodities 30.1%</td><td>MSCI EAFE 20.7%</td><td>MSCI EAFE 14.0%</td><td>Gold 23.2%</td><td>MSCI EAFE 11.6%</td><td>Global IG -8.3%</td><td>REITS 31.7%</td><td>S&amp;P 500 15.1%</td><td>Global HY 2.6%</td><td>MSCI EAFE 17.9%</td><td>REITS 0.7%</td><td>Global IG 3.2%</td><td>MSCI EAFE -0.8%</td><td>MSCI EM 11.2%</td><td>Gold 12.9%</td><td>Global HY -3.3%</td><td>Commodities 20.1%</td><td>Global IG 10.3%</td><td>MSCI EAFE 11.9%</td><td>US Treasuries -12.9%</td><td>Gold 12.7%</td><td>Global HY 7.5%</td><td>S&amp;P 500 18.5%</td><td>MSCI EAFE 8.4%</td></tr><tr><td>Global IG 3.1%</td><td>Gold -0.7%</td><td>Cash 1.8%</td><td>Global HY 30.7%</td><td>Global HY 12.4%</td><td>REITS 10.7%</td><td>S&amp;P 500 15.8%</td><td>US Treasuries 9.1%</td><td>Global HY -27.9%</td><td>S&amp;P 500 26.5%</td><td>Global HY 13.9%</td><td>S&amp;P 500 2.1%</td><td>S&amp;P 500 16.0%</td><td>Global IG 0.1%</td><td>Gold 0.1%</td><td>REITS -3.4%</td><td>Gold 8.6%</td><td>REITS 11.5%</td><td>Global IG -3.4%</td><td>MSCI EM 18.6%</td><td>MSCI EAFE 8.4%</td><td>Global HY 1.4%</td><td>Global HY -13.2%</td><td>REITS 11.3%</td><td>Commodities 5.5%</td><td>Global HY 9.9%</td><td>S&amp;P 500 8.1%</td></tr><tr><td>Gold -5.4%</td><td>MSCI EM -2.4%</td><td>Global HY -1.1%</td><td>S&amp;P 500 28.7%</td><td>S&amp;P 500 10.9%</td><td>S&amp;P 500 4.9%</td><td>Global HY 13.5%</td><td>Global IG 7.3%</td><td>S&amp;P 500 -37.0%</td><td>Commodities 26.1%</td><td>Commodities 13.3%</td><td>Cash 0.1%</td><td>Global IG 11.1%</td><td>Cash 0.1%</td><td>Cash 0.0%</td><td>Global IG -3.8%</td><td>Global IG 4.3%</td><td>Global HY 10.2%</td><td>REITS -3.9%</td><td>Gold 17.9%</td><td>US Treasuries 8.2%</td><td>Cash 0.0%</td><td>MSCI EAFE -13.9%</td><td>MSCI EM 10.1%</td><td>Cash 5.3%</td><td>Global IG 9.8%</td><td>Cash 1.7%</td></tr><tr><td>Global HY -5.8%</td><td>REITS -7.8%</td><td>REITS -2.4%</td><td>Gold 19.9%</td><td>Global IG 9.4%</td><td>Cash 3.1%</td><td>Global IG 7.2%</td><td>S&amp;P 500 5.5%</td><td>Commodities -42.6%</td><td>Gold 25.0%</td><td>MSCI EAFE 8.2%</td><td>Commodities -2.6%</td><td>Gold 8.3%</td><td>Commodities -2.1%</td><td>Global HY -0.1%</td><td>Global HY -4.2%</td><td>REITS 1.3%</td><td>Global IG 9.3%</td><td>S&amp;P 500 -4.3%</td><td>Global HY 13.7%</td><td>Global HY 8.0%</td><td>MSCI EM -2.3%</td><td>Global IG -16.7%</td><td>Global IG 9.5%</td><td>MSCI EAFE 4.4%</td><td>US Treasuries 6.1%</td><td>Global HY 1.4%</td></tr><tr><td>S&amp;P 500 -9.1%</td><td>S&amp;P 500 -11.9%</td><td>MSCI EM -6.0%</td><td>Global IG 14.5%</td><td>Gold 4.6%</td><td>US Treasuries 2.8%</td><td>Cash 4.9%</td><td>Cash 5.0%</td><td>MSCI EAFE -43.1%</td><td>Global IG 19.2%</td><td>Global IG 6.0%</td><td>REITS -9.4%</td><td>US Treasuries 2.2%</td><td>MSCI EM -2.3%</td><td>MSCI EM -1.8%</td><td>Gold -10.4%</td><td>US Treasuries 1.1%</td><td>Commodities 7.6%</td><td>Commodities -13.1%</td><td>Global IG 11.4%</td><td>Cash 0.5%</td><td>US Treasuries -2.4%</td><td>S&amp;P 500 -18.1%</td><td>Cash 5.1%</td><td>REITS 3.2%</td><td>Commodities 5.9%</td><td>US Treasuries 0.7%</td></tr><tr><td>MSCI EAFE -14.0%</td><td>MSCI EAFE -21.2%</td><td>MSCI EAFE -15.7%</td><td>US Treasuries 2.3%</td><td>US Treasuries 3.5%</td><td>Global HY 1.5%</td><td>US Treasuries 3.1%</td><td>Global HY 3.0%</td><td>REITS -50.2%</td><td>Cash 0.2%</td><td>US Treasuries 5.9%</td><td>MSCI EAFE -11.7%</td><td>Cash 0.1%</td><td>US Treasuries -3.3%</td><td>MSCI EAFE -4.5%</td><td>MSCI EM -14.9%</td><td>MSCI EAFE 1.0%</td><td>US Treasuries 2.4%</td><td>MSCI EAFE -13.2%</td><td>US Treasuries 7.0%</td><td>REITS -4.4%</td><td>Global IG -3.0%</td><td>MSCI EM -19.8%</td><td>US Treasuries 3.9%</td><td>Global IG 1.2%</td><td>Cash 4.0%</td><td>Global IG 0.2%</td></tr><tr><td>MSCI EM -30.6%</td><td>Commodities -21.4%</td><td>S&amp;P 500 -22.1%</td><td>Cash 1.1%</td><td>Cash 1.3%</td><td>Global IG -3.0%</td><td>Commodities -0.2%</td><td>REITS -10.0%</td><td>MSCI EM -53.2%</td><td>US Treasuries -3.7%</td><td>Cash 0.1%</td><td>MSCI EM -18.2%</td><td>Commodities -0.3%</td><td>Gold -27.3%</td><td>Commodities -29.3%</td><td>Commodities -29.4%</td><td>Cash 0.3%</td><td>Cash 0.8%</td><td>MSCI EM -14.3%</td><td>Cash 2.2%</td><td>Commodities -15.0%</td><td>Gold -4.1%</td><td>REITS -25.2%</td><td>Commodities -3.5%</td><td>US Treasuries 0.5%</td><td>REITS 3.5%</td><td>Gold -7.7%</td></tr></table>

Source: BofA Global Investment Strategy, Bloomberg. \*2026 YTD  
BofA GLOBAL RESEARCH

BofA GLOBAL RESEARCH

## BofA Rules & Tools

Table 4: Table 6: BofA Global Investment Strategy Proprietary Indicators
C

[中间内容因长度限制已省略]

h information is distributed simultaneously to internal and client websites and other portals by BofA and is not publicly-available material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

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
