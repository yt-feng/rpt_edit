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
# Global Equity Volatility Insights

# Stock vs index vol at 90s Dotcom extremes

## Stock vs index vol near Dotcom extreme... shock risk is real

With US equity sectors & factors still gyrating sharply amid continued AI-related bubble-like price action, single stock realized vol has risen to levels last seen in the latter stages of the 90s dotcom bubble, with earnings season on deck. However, index vol remains relatively muted, driving a historic divergence that could widen further, and potentially surpass dotcom extremes, if valuations (not just price action) move further into bubble-like territory. What's been the key driver of this sharp divergence? In a nutshell, semis. Indeed, instability in large stocks like MU and AMD has driven single stock vol higher, while the increasing de-correlation of semis from other megacaps and software has driven index-wide correlation to near-record lows and suppressed index vol. Interestingly, semis' rise in vol and de-correlation vs other key equities has been concurrent with a rise in its BRI levels. Against this backdrop, the risk of higher index vol from a correlation uptick is historically acute, especially given the upcoming seasonally challenging period for equities. To hedge this risk, we like VIX call spreads, offering >15x max payout ratios.

## SX5E-vs-SXXP put switch for cheapened EU cyclical hedge

The recent decline in SX5E implied volatility has tightened its volatility spread vs the STOXX 600 to historically low levels, with the implied vol spread now below the recent realised vol spread. This also cheapens the price of SX5E-vs-SXXP put switches, which are now suggesting an "implied beta" that is lower than the index's empirically observed cyclicality. Given SX5E's overweight exposure to cyclical sectors such as Technology, Consumer Discretionary and Industrials, put switches offer a relatively low-premium way to hedge downside risk in Europe's cyclical sectors, particularly as the recent sell-off from SX5E's all-time highs was driven primarily by weakness in Industrials and Tech.

## Own TSMC into earnings & cheapen NKY hedges by 74%

Own the upside, not the downside, into TSMC earnings. Strong sales momentum supports our positive fundamental view, but the risk-reward into Thursday's print appears skewed as markets remain highly sensitive to any AI capex concerns. We recommend switching cash equity exposure into option structures that cap downside at 1.3% while preserving substantial upside convexity. Rich upside volatility further supports call ratios, particularly given our expectation of a more orderly rally and lower post-event vols. Separately, elevated vol has made Nikkei hedges expensive, but rich downside vol creates opportunity to cut protection costs by up to 74%. Given the Nikkei's rising sensitivity to AI and global macro risk, we view it as an attractive vehicle for hedging a potential 10–20% correction.

## Also in the GEVI

Screening for cheap European earnings gamma ahead of Q2 reporting.

Commodities & equities brought global cross-asset stress lower despite Iran escalation

## 14 July 2026

Equity Derivatives
Global

BofA
Data Analytics

![](images/8c1a524102368caa6063ff0023a53c7919a4e7592977d8f7e3c558459202ce5b.jpg)

Global Equity Derivatives Rsch
BofAS

Riddhi Prasad >> Equity-Linked Analyst MLI (UK)

Arjun Goyal
Equity-Linked Analyst
BofAS

Nitin Saksena
Equity-Linked Analyst
BofAS

Lars Naeckter >>
Equity-Linked Analyst
BofA (DIFC)

Vittoria Volta >> Equity-Linked Analyst BofASE (France)

Meriem Hafid >> Research Analyst BofASE (France)

Benjamin Bowler
Equity-Linked Analyst
BofAS
benjamin.bowler@bofa.com

Abhinandan Deb >> Equity-Linked Analyst MLI (UK)

Nicholas Dunne
Equity-Linked Analyst
BofAS

See Team Page for List of Analysts

Exhibit 1: 3M volatility (2weeks chg)  
Level & changes (in parentheses) in vol pts

<table><tr><td></td><td>Implied</td><td>Realized</td></tr><tr><td>S&amp;P500</td><td>14.5 (-1.7)</td><td>13.1 (-2.1)</td></tr><tr><td>ESTX50</td><td>15.5 (-0.8)</td><td>16.7 (-2.7)</td></tr><tr><td>FTSE</td><td>12.5 (0.0)</td><td>12.3 (-1.5)</td></tr><tr><td>DAX</td><td>16.1 (-0.6)</td><td>16.9 (-2.1)</td></tr><tr><td>NKY</td><td>30.7 (-3.2)</td><td>31.0 (-3.1)</td></tr><tr><td>HSCEI</td><td>22.2 (-0.5)</td><td>20.2 (0.4)</td></tr><tr><td>KOSPI</td><td>72.0 (-3.4)</td><td>65.0 (-0.5)</td></tr><tr><td>EEM US</td><td>33.5 (-0.5)</td><td>32.1 (-1.0)</td></tr><tr><td>XIN9I</td><td>21.7 (-1.6)</td><td>19.0 (1.3)</td></tr></table>

Source: BofA Global Research

BofA GLOBAL RESEARCH

See list of acronyms at the end of the report

## BofA GFSI™ X-Asset Risk Landscape

## Commodity & equity stress falls but remains highest

The GFSI resumed its decline over the last two weeks, moving from -0.16 on 26-Jun-26 to -0.20 on 10-Jul-26. Notably, the declines in stress mostly came in the week of 29-Jun to 3-Jul, as the GFSI then increased on last week's re-escalation in the Iran conflict. The index is still low relative to history in its $23^{rd}$ percentile since 2000.

All asset classes apart from rates saw stress fall over the last two weeks with commodities and equities posting the largest declines (Exhibit 4). In fact, seven of the top eight stress-decliners were commodity or equity subcomponents with Nikkei implied vol recording the largest stress decrease (Exhibit 3). Copper implied vol was the third largest stress-decliner, and copper and Nikkei implied vols both experienced declines in stress in their top deciles versus history (Exhibit 6). Gold and crude implied vols were also among the top eight stress-decliners, and commodity vol was the top decliner versus all cross-asset vols and spreads (Exhibit 3 & Exhibit 7). Despite the recent declines in stress, commodities and equities remain the two most stressed asset classes, and the only ones with stress above long-run median levels (Exhibit 4).

In other asset classes, FX and credit stress declined while rates stress slightly rose (Exhibit 4). GBPUSD implied vol was the only subcomponent outside of equities and commodities in the top eight stress-decliners as GBP strengthened amid declining UK political risk after it became clear that Andy Burnham will be the next PM. Meanwhile, European subcomponents led rates stress higher with Euribor-OIS and interest rate implied vol EUR posting the top two stress increases (Exhibit 3). Coincidentally, Europe was the only region to see stress increase over the last two weeks (Exhibit 5).

\- The GFSI averaged -0.10 in Q2-26. This is lower than the Q1-26 average of +0.01 and equivalent to the 2025 full year average. Notably, stress was down significantly since Q2-25 when tariffs led the GFSI to average +0.18.

\- Crude implied vol stress spiked to +0.66 on 8-Jul as Iran and the US exchanged hostilities. Stress declined to +0.43 by Friday (Exhibit 2)

## Exhibit 2: Latest\* stress across GFSI sub-components

Tibor-OIS is the most stressed while sub-IG foreign sovereign bond spreads are the least stressed

![](images/91f7aa3ea9677615dc375e3c9fca3d2011d61804fda6c0e24225dc922b3e906c.jpg)  
Source: BofA Global Research. \*Latest as of 10-Jul-26. Disclaimer: The indicator identified above as BofA GFSI is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

## Exhibit 3: Change\*\* in stress across GFSI sub-components

Euribor-OIS was the largest stress riser over the last two weeks while Nikkei implied vol stress fell the most  
![](images/4daf17382c36e848f239535a9132249b74d100c902e7fd8a1bba3c406e6d36c5.jpg)  
Source: BofA Global Research. \*\*Latest as of 5-Jun-26. Change from 26-Jun-26 to 10-Jul-26.  
BofA GLOBAL RESEARCH

The GFSI Risk Allocator (using Bull, Bear & Neutral weights of 2, 0, 1) suggested a 22.0% overweight position as of 10-Jul-26 (vs a 17.1% overweight position as of 26-Jun-26). The percentages of Bullish, Bearish, and Neutral GFSI components (as used in the Risk Allocator) as of 10-Jul-26 were 31.7%, 9.8%, and 58.5%, respectively.

Exhibit 4: Commodity stress decreased the most in the last two weeks In contrast, rates stress slightly increased

![](images/9271ffe98956a4ba1611497645b4c305fa4c354ebd6fa2ddfe7b76b9e091237b.jpg)  
Source: BofA Global Research. Change from 26-Jun-26 to 10-Jul-26.  
BofA GLOBAL RESEARCH

Exhibit 5: Japan led regional stress lower over the last two weeks
Meanwhile, Europe posted the only stress increase  
![](images/5abbc13c805945aad7c282ab2086594fd3f6ea411b631036f8aab56b409fa6b4.jpg)  
Source: BofA Global Research. Change from 26-Jun-26 to 10-Jul-26.  
BofA GLOBAL RESEARCH  
Exhibit 6: Top 10 biggest stress movers (vs history)
Copper implied vol saw a historically large stress decline

![](images/91dcf74987254f458581bef8c91a0297ca05e3648912a796a59464b2f8586c29.jpg)  
Source: BofA Global Research. \* %-ile of 10-day moves in stress vs all historical 10-day moves (earliest 3-Jan-00). Bar colors represent rise (red) or fall (green) in stress. 10-day change (26-Jun-26 to 10-Jul-26).

Exhibit 7: Biggest stress movers in cross-asset vols and spreads
Commodity vol experienced the largest decrease in stress over the last two weeks  
![](images/faefbae593d1fb615319a95086850543d7f61de2cbd66488b5e94aac6d89c1cf.jpg)  
Source: BofA Global Research. Change from 26-Jun-26 to 10-Jul-26.  
BofA GLOBAL RESEARCH

## BofA Bubble Risk Indicator Landscape BRI levels retreat mildly in Kospi, Nikkei and Nasdaq

The BofA Bubble Risk Indicator (BRI) is a price-based measure designed to detect bubble-like asset dynamics. Inspired by the way the first four moments describe a statistical distribution, the BRI distils an asset's returns, volatility, momentum, and fragility into a single bubble-risk reading on a 0 to 1 scale; 1 represents extreme bubble-like price action while 0 represents none. Historic asset bubbles have exhibited high BRI levels as they formed and peaked (see our 2026 Year Ahead for more details).

Exhibit 8: BRI levels on the Kospi, Nikkei and Nasdaq / US tech have mildly retreated but remain high vs other major assets & markets
BofA Bubble Risk indicator (as of 10-Jul-26) across global equity indices, US equity sectors, commodities and crypto (bars: range of short- to long-term sub-indicators)

![](images/51140faa37d4a65b17829b47a66363553931f7c439a127fae59e4df87494300a.jpg)  
Source: BofA Global Research. Data as of 10-Jul-26. Underlying tickers: SPX, NDX, RTY, SX5E, SX7E, CAC, DAX, UKX, NKY, HSCEI, KOSPI2, NIFTY, MXWD, IXB, IXCPR, IXE, IXM, IXI, IXT, IXR, IXRE, IXU, IXV, IXY, BM7P, BCOM, CO1, XAU, XAG, HG1, XBTUSD, XETUSD. Disclaimer: The indicator identified as the BofA Bubble Risk Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.  
BofA GLOBAL RESEARCH  
Exhibit 9: Semis & cybersecurity stocks are still showing relatively high bubble-like dynamics among popular equity themes...  
Highest BRI readings across popular equity themes (as of 10-Jul-26)

![](images/89c424fa3a89cea36d2ec71d0fcf59e880aad3d106b6021bbeb66f57f6101228.jpg)  
Source: BofA Global Research. Data as of 10-Jul-26. Underlying tickers: ICESEMIT, NQCYBRN, FTTWN, DJSPHMT, SP500MUT, SPTSCUT, SPSIBITR, SPSIINST, GPVAN2TR, CRSPMIT. See Disclaimer in Exhibit 8.  
Exhibit 10: ... though semis & cybersecurity BRI levels (and most popular equity themes in general) have retreated over the past week Largest 1w changes in BRI across popular equity themes (as of 10-Jul-26)

![](images/718486348e809938c25b01c91288029d7f70751fa9be18fa7eb79e8434fd0e69.jpg)  
Source: BofA Global Research. Data as of 10-Jul-26. Underlying tickers: DJSPHMT, SPSIINST, SP500MUT, ICESEMIT, NQCYBRN. See Disclaimer in Exhibit 8.  
BofA GLOBAL RESEARCH  
BofA GLOBAL RESEARCH

Exhibit 11: S&P stocks are showing increasingly frothy price action, both in terms of the number of stocks...
# of SPX stocks with BRIs above 0.8  
![](images/99a6b9ffbcd0e36068b0216a183fe33c78730c015ef91bd0d9c966b0d64848c3.jpg)  
Source: BofA Global Research. Data from 1-Jan-95 to 10-Jul-26. Stocks' BRI computed using data since SPX inclusion. See Disclaimer in Exhibit 8.  
BofA GLOBAL RESEARCH

Exhibit 12: ... and when measured by total index weight
Total weight of SPX stocks with BRIs above 0.8  
![](images/cc515a6451733b87284c04bb71bde424c10f028b0fa8cfcca5c38ccb3614add8.jpg)  
Source: BofA Global Research. Data from 1-Jan-95 to 10-Jul-26. Stocks' BRI computed using data since SPX inclusion. See Disclaimer in Exhibit 8.  
BofA GLOBAL RESEARCH

Exhibit 13: Tech stocks like AMAT, WDAY, HPE and CSCO rank highest in terms of their Bubble Risk Indicators amongst S&P 500 members S&P 500 member stocks with highest BRI reading (as of 10-Jul-26)  
![](images/3dd88b8a4dd8dcdc8b25bd87884d67827592b1afe68d6cafd27c0626efd90b9b.jpg)  
Source: BofA Global Research. Data as of 10-Jul-26. Note: Stocks' BRI computed using data since S&P 500 inclusion. See Disclaimer in Exhibit 8. Note that the BRI is a purely price-based metric intended to quantify the degree of bubble-like price action. It is not a fundamental view on the stock and should be used only as a complement to fundamental and positioning-based metrics.

## Exhibit 14: US Exporters, EU semis, and China tech localization stocks are amongst the global themes showing bubble-like price action as per their high BRIs

Bubble Risk Indicator on selected BofA Custom Baskets\* (as of 10-Jul-26)

<table><tr><td>Basket</td><td>Ticker</td><td>BRI</td></tr><tr><td colspan="3">AMRS</td></tr><tr><td>US Exporters</td><td>MLUXPORT</td><td>0.90</td></tr><tr><td>US AI Compute</td><td>MLUCOMPU</td><td>0.86</td></tr><tr><td>US Cyber Security Basket</td><td>MLCYBRS</td><td>0.86</td></tr><tr><td>US TMT Memory Basket</td><td>MLUMEMOR</td><td>0.85</td></tr><tr><td>US Hardware</td><td>MLUSHRDW</td><td>0.84</td></tr><tr><td>US Cyclicals Ex Commods</td><td>MLCYCLX</td><td>0.83</td></tr><tr><td>US 800v DC Transition</td><td>MLU800V</td><td>0.82</td></tr><tr><td>US AI Beneficiaries</td><td>MLUSAI</td><td>0.81</td></tr><tr><td>US Managed Care</td><td>MLDIMNGC</td><td>0.80</td></tr><tr><td>US TMT Momentum Factor</td><td>MLUPTMMO</td><td>0.80</td></tr><tr><td>US Health Care Momentum Factor</td><td>MLUPHCMO</td><td>0.79</td></tr><tr><td>US Data Center Builders</td><td>MLDATACB</td><td>0.79</td></tr><tr><td>US Quality Factor</td><td>MLUPQUAL</td><td>0.77</td></tr><tr><td>US Transports</td><td>MLUTRANS</td><td>0.75</td></tr><tr><td>US Financials Momentum Factor</td><td>MLUPFINM</td><td>0.75</td></tr><tr><td>US TMT Supply Shortage</td><td>MLUTMTSP</td><td>0.74</td></tr><tr><td>US Industrials Momentum Factor</td><td>MLUPINMO</td><td>0.71</td></tr><tr><td>US TMT Durable Compounders</td><td>MLUTMTDC</td><td>0.69</td></tr><tr><td>US SMID Cap Semis</td><td>MLSEMISM</td><td>0.69</td></tr><tr><td>US Efficient Growth</td><td>MLUEGROW</td><td>0.66</td></tr><tr><td>US Boomers Spend</td><td>MLUBOOM</td><td>0.66</td></tr><tr><td>US Electric Grid Enablers</td><td>MLUGRID</td><td>0.65</td></tr><tr><td>US AI Infrastructure</td><td>MLAIINFR</td><td>0.65</td></tr><tr><td>US TMT Profitable Growth</td><td>MLUTMTPG</td><td>0.64</td></tr><tr><td>US Momentum Factor</td><td>MLUPMOMO</td><td>0.61</td></tr><tr><td>US China Importers</td><td>MLCHIMPT</td><td>0.61</td></tr><tr><td>US Consensus Growth Shorts</td><td>MLDIMSGR</td><td>0.60</td></tr><tr><td>Canada Infrastructure &amp; Defense</

[中间内容因长度限制已省略]

esearch personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.

## Research Analysts

## Benjamin Bowler

Equity-Linked Analyst
BofAS
+1 415 676 3595
benjamin.bowler@bofa.com

## Abhinandan Deb >>

Equity-Linked Analyst
MLI (UK)
+44 20 7995 7148
abhinandan.deb@bofa.com

## Nitin Saksena

Equity-Linked Analyst
BofAS
+1 646 855 5480
nitin.saksena@bofa.com

## Lars Naeckter >>

Equity-Linked Analyst
BofA (DIFC)
+971 4425 8218
lars.naeckter@bofa.com

## Chintan Kotecha

Equity-Linked Analyst
BofAS
+1 646 855 5478
chintan.kotecha@bofa.com

## Riddhi Prasad >>

Equity-Linked Analyst
MLI (UK)
+44 20 7995-7852
riddhi.prasad@bofa.com

## Michael Youngworth, CFA

CBs, Pfds & Derivs Strategist
BofAS
+1 646 855 6493
michael.youngworth@bofa.com

Vittoria Volta >>
Equity-Linked Analyst
BofASE (France)
+33 1 8770 0703
vittoria.volta@bofa.com

Nicholas Dunne
Equity-Linked Analyst
BofAS
+1 646 855 2631
nicholas.dunne@bofa.com

Arjun Goyal
Equity-Linked Analyst
BofAS
+1 646 743 4273
arjun.goyal@bofa.com

Meriem Hafid >>
Research Analyst
BofASE (France)
+33 1 5365 5664
meriem.hafid@bofa.com

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules. Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.
"""
