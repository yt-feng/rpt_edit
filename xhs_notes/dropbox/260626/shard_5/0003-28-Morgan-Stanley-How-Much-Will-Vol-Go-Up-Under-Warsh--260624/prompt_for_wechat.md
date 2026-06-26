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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 24, 2026 11:55 AM GMT

US Rates Strategy | North America

# How Much Will Vol Go Up Under Warsh?

The first FOMC under Warsh suggests less forward guidance. Markets would likely place greater weight on economic data and react more strongly to surprises. Looking back to the Greenspan era, we quantify how changes in market sensitivity to economic data could translate into higher rates volatility.

## Key Takeaways

\- Warsh's first press conference suggests less forward guidance. Economic data should play a larger role in market pricing.

The Greenspan era provides the closest comparison for a less guided Fed and offers clues on how much market sensitivity to economic data could increase.

We measure market sensitivity using the relationship between economic surprises and Treasury yield moves, with both variables normalized.

■ Market reaction to data surprises declined steadily from the Greenspan era through the pre-COVID period. Warsh could reverse part of that decline.

\- Higher market sensitivity to economic data argues for higher short-dated volatility. Intermediate expiries should follow. Stay long 2y10y straddles.

MS & CO. LLC

Shaun.Zhou@morganstanley.com +1 212 761-3348

Strategist
Matthew.Hornbach@morganstanley.com +1 212 761-1837

Strategist
Martin.Tobias@morganstanley.com +1 212 761-6076

Aryaman Singh
Strategist
Aryaman@morganstanley.com +1 212 761-1993

# Interest Rate Derivative Strategy

## United States | How much will vol go up under Warsh?

MS & CO. LLC
Shaun Zhou
Shaun.Zhou@morganstanley.com
+1 212 761-3348

Matthew.Hornbach@morganstanley.com +1 212 761-1863

Martin.Tobias@morganstanley.com +1 212 761-6076

Aryaman@morganstanley.com +1 212 761-1993

Eli.Carter@morganstanley.com +1 212 761-4703

## Fed communication policy revamped

The first FOMC press conference under Chair Warsh suggests a meaningful shift in the Fed's communication strategy. By scaling back forward guidance, the Fed is providing markets with less information about its expected policy path.

A market that receives less guidance from policymakers must extract more information from economic releases. That argues for greater sensitivity to macro data and higher rates volatility.

To gauge the potential increase in market sensitivity, we look to the Greenspan era, when forward guidance played a much smaller role in monetary policy. If Warsh continues down this path, that period offers the closest historical comparison.

## Measure market sensitivity to economic releases

We quantify market sensitivity by examining the relationship between economic surprises and Treasury yield moves on release dates.

To ensure comparability across different Fed regimes, both variables are normalized. Economic surprises are scaled by their rolling two-year standard deviation, while yield moves are scaled by three-month realized volatility.

The resulting measure captures how strongly rates respond to a given economic surprise over time.

## Market sensitivity to NFP

Exhibit 1 plots normalized NFP surprises against normalized changes in the 2-year Treasury yield on payroll release dates. Each point represents a monthly observation, with colors denoting different Fed chairs. We also overlay a separate regression line for each Fed regime, splitting Powell's tenure into pre- and post-COVID periods to account for the different macro environments.

The positive relationship between payroll surprises and front-end rates is consistent across all regimes: stronger payrolls tend to push 2-year yields higher. The more

important question is whether market sensitivity to payroll surprises has changed over time.

Exhibit 2 cuts through the noise by reporting the estimated sensitivity of 2-year yields to NFP surprises, along with 90% confidence intervals. While the estimates are subject to uncertainty given the limited number of observations within each Fed regime, the trend is clear: market sensitivity to payroll surprises declined steadily from the Greenspan era through the pre-COVID period.

During the pre-COVID period of Powell's first term, the response of the 2-year Treasury yield to a given payroll surprise was roughly half of its Greenspan-era level. While multiple factors likely contributed to this decline, the increase in policy transparency and forward guidance was clearly part of the shift.

The pandemic reversed this trend. Elevated inflation, higher policy rates, and a series of large macro shocks increased the market's response to economic data, bringing sensitivity to NFP back to levels comparable to the Greenspan era.

As Warsh reduces the role of forward guidance, we expect some further increase in sensitivity. While the exact magnitude is uncertain, a full reversal of the decline since the Greenspan era would imply an increase of up to 0.5x daily volatility per unit of data surprise.

Exhibit 1: Normalized market response to NFP surprises since 1997  
![](images/656f238b2895b28fea4b1cae663f876ec6fc55cfda7d05dcde38e95a874acfda.jpg)  
Source: Bloomberg. MS.

Exhibit 2: Market sensitivity to NFP surprises declined since Greenspan  
![](images/c70379b1a1aa96bf42f67458ac18afe4423179252cdfe4ac4c0e32835440f0a9.jpg)  
Source: Bloomberg. MS.

## Different pattern for inflation data

Exhibit 3 plots normalized surprises in monthly CPI against normalized changes in the 2-year Treasury yield.

Unlike payrolls, inflation surprises had little consistent impact on front-end rates prior to COVID. While CPI releases occasionally generated large market moves, the relationship between inflation surprises and Treasury yields was weak and statistically unstable across earlier Fed regimes.

The pandemic changed this. As inflation became a key driver of monetary policy, markets began responding more consistently to CPI surprises. Exhibit 4 shows that the market sensitivity increased sharply in the post-COVID period. Our FX strategies team documented a similar shift in currency markets.

Markets are already highly sensitive to inflation data, and recent FOMC communications suggest that inflation remains the primary policy concern under Warsh. As a result, inflation releases could have a larger impact on front-end rates than employment data in the near term.

Exhibit 3: Normalized market response to CPI surprises since 1998  
![](images/fbcdf3577025dcd5b9edf54ce8e37558b2dfe15f25718e49e4dae7dcc1f12e61.jpg)  
Source: Bloomberg. MS.

Exhibit 4: Market sensitivity to CPI increased post-pandemic  
![](images/a512ace6b0fd090dcdec7c57365661eead9a1b44aa92c72e7d446a4a127bc514.jpg)  
Source: Bloomberg. MS.

## Trend confirmed by intraday moves

Daily yield changes capture more than the market response to economic releases. To isolate the direct impact of NFP and CPI, we expand the analysis to yield changes over the 60 minutes following the 8:30 a.m. release.

Data availability limits the intraday analysis to the period since 2013, preventing a direct comparison with the Greenspan era. Nevertheless, the results closely mirror the patterns observed in the daily data, confirming that market sensitivity tends to be higher under a less guided Fed:

\- Market sensitivity to payroll surprises declined from the Bernanke era through the pre-COVID period.

• Markets did not respond consistently to CPI surprises prior to the pandemic.

\- Market sensitivity to both employment and inflation surprises increased after the pandemic.

Exhibit 5: Market sensitivity to NFP surprises: 60-minute response

<table><tr><td>Chair</td><td>market sensitivity (beta)</td><td>R^2</td><td>t-stat</td></tr><tr><td>Bernanke</td><td>1.11</td><td>0.60</td><td>3.23</td></tr><tr><td>Yellen</td><td>0.68</td><td>0.22</td><td>3.55</td></tr><tr><td>Powell (pre COVID)</td><td>0.38</td><td>0.24</td><td>2.67</td></tr><tr><td>Powell (post COVID)</td><td>0.81</td><td>0.22</td><td>4.50</td></tr></table>

Source: Bloomberg. MS.

Exhibit 6: Market sensitivity to CPI surprises: 60-minute response

<table><tr><td>Chair</td><td>market sensitivity (beta)</td><td>R^2</td><td>t-stat</td></tr><tr><td>Bernanke</td><td>0.11</td><td>0.08</td><td>0.73</td></tr><tr><td>Yellen</td><td>0.33</td><td>0.10</td><td>2.18</td></tr><tr><td>Powell (pre COVID)</td><td>0.24</td><td>0.16</td><td>2.03</td></tr><tr><td>Powell (post COVID)</td><td>0.79</td><td>0.35</td><td>6.09</td></tr></table>

Source: Bloomberg. MS.

## Conclusion

Our analysis suggests that market sensitivity to economic data declined steadily from the Greenspan era through the pre-COVID period. This likely reflects a combination of factors, including Fed forward guidance, the expanded policy toolkit, and changes in the macro environment. Regardless of the cause, the historical evidence shows a clear relationship between more forward guidance and lower market sensitivity to economic data.

Historical experience suggests that some of the decline in market sensitivity since the Greenspan era could reverse under Warsh. With markets already responding more strongly to employment and inflation data than they did before the pandemic, we think further increases would translate into larger moves around key economic releases.

Ultimately, long-term volatility will likely depend on the size of future economic surprises. However, a market that relies more heavily on incoming data should see larger rate moves in response to a given surprise. This argues for higher short-dated volatility. As markets digest changes in Fed communication, intermediate expiries should follow. We therefore maintain our recommendation to own 2y10y volatility through long straddles.

## SDR Monitor

Following the FOMC, dealer gamma positioning has normalized in the front end, with desks now broadly flat gamma across tails of 2 years and shorter. In contrast, dealers remain short gamma in the long end, particularly in tails of 9 years and longer.

Investor flows remained balanced over the past two weeks, with modest gamma selling in 3m10y and 3m15y. Elsewhere, investors rotated into longer-dated expiries, buying 10y+ expiries against selling 5y expiries.

Exhibit 7: Dealer net gamma exposure  
![](images/d14681eb1c6acd3209171478c032b8cc45afaf91ea095ca61107a39538a5fae6.jpg)  
Source: DTCC, MS

Exhibit 8: Historical spot dealer net gamma exposure  
![](images/f9430453890341017ea91d650018c5943ec1e68249564a4428ca9977d37b187e.jpg)  
Source: DTCC, MS

Exhibit 9: Net customer flow in gamma (\$k)

<table><tr><td>exp\tail</td><td>1Y</td><td>2Y</td><td>3Y</td><td>5Y</td><td>10Y</td><td>15Y</td><td>20Y</td><td>30Y</td></tr><tr><td>1M</td><td>(1)</td><td>3</td><td>0</td><td>(27)</td><td>(29)</td><td>(4)</td><td>(5)</td><td>(8)</td></tr><tr><td>2M</td><td>0</td><td>1</td><td>0</td><td>(1)</td><td>6</td><td>0</td><td>0</td><td>22</td></tr><tr><td>3M</td><td>(6)</td><td>(4)</td><td>2</td><td>6</td><td>(42)</td><td>(89)</td><td>(0)</td><td>(23)</td></tr><tr><td>6M</td><td>1</td><td>(3)</td><td>0</td><td>8</td><td>0</td><td>0</td><td>0</td><td>(10)</td></tr><tr><td>9M</td><td>(3)</td><td>2</td><td>0</td><td>2</td><td>1</td><td>0</td><td>1</td><td>(3)</td></tr><tr><td>1Y</td><td>(2)</td><td>(12)</td><td>1</td><td>3</td><td>14</td><td>0</td><td>0</td><td>16</td></tr><tr><td>18M</td><td>(0)</td><td>(0)</td><td>(4)</td><td>0</td><td>2</td><td>0</td><td>0</td><td>3</td></tr><tr><td>2Y</td><td>(3)</td><td>(2)</td><td>0</td><td>2</td><td>(4)</td><td>0</td><td>(0)</td><td>1</td></tr><tr><td>3Y</td><td>0</td><td>0</td><td>0</td><td>(1)</td><td>(2)</td><td>0</td><td>1</td><td>(0)</td></tr><tr><td>5Y</td><td>(0)</td><td>1</td><td>0</td><td>0</td><td>(3)</td><td>0</td><td>(1)</td><td>(7)</td></tr><tr><td>10Y</td><td>0</td><td>(0)</td><td>0</td><td>0</td><td>(0)</td><td>0</td><td>2</td><td>(0)</td></tr><tr><td>15Y</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>20Y</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Source: DTCC, MS

Exhibit 10: Net customer flow in vega (\$k)

<table><tr><td>exp\tail</td><td>1Y</td><td>2Y</td><td>3Y</td><td>5Y</td><td>10Y</td><td>15Y</td><td>20Y</td><td>30Y</td></tr><tr><td>1M</td><td>(5)</td><td>18</td><td>0</td><td>(184)</td><td>(158)</td><td>(20)</td><td>(28)</td><td>(42)</td></tr><tr><td>2M</td><td>4</td><td>22</td><td>0</td><td>(9)</td><td>77</td><td>0</td><td>0</td><td>235</td></tr><tr><td>3M</td><td>(114)</td><td>(84)</td><td>44</td><td>118</td><td>(799)</td><td>(1,611)</td><td>(3)</td><td>(336)</td></tr><tr><td>6M</td><td>53</td><td>(166)</td><td>0</td><td>302</td><td>32</td><td>0</td><td>0</td><td>(361)</td></tr><tr><td>9M</td><td>(199)</td><td>175</td><td>0</td><td>157</td><td>101</td><td>0</td><td>65</td><td>(136)</td></tr><tr><td>1Y</td><td>(206)</td><td>(1,122)</td><td>134</td><td>223</td><td>1,043</td><td>0</td><td>0</td><td>1,246</td></tr><tr><td>18M</td><td>(8)</td><td>(30)</td><td>(480)</td><td>0</td><td>184</td><td>0</td><td>0</td><td>325</td></tr><tr><td>2Y</td><td>(545)</td><td>(276)</td><td>0</td><td>267</td><td>(633)</td><td>22</td><td>(0)</td><td>131</td></tr><tr><td>3Y</td><td>0</td><td>36</td><td>0</td><td>(289)</td><td>21</td><td>0</td><td>297</td><td>(100)</td></tr><tr><td>5Y</td><td>(201)</td><td>555</td><td>0</td><td>141</td><td>(1,332)</td><td>0</td><td>(302)</td><td>(2,554)</td></tr><tr><td>10Y</td><td>0</td><td>(26)</td><td>0</td><td>248</td><td>(11)</td><td>0</td><td>1,047</td><td>(70)</td></tr><tr><td>15Y</td><td>0</td><td>0</td><td>0</td><td>0</td><td>396</td><td>0</td><td>0</td><td>0</td></tr><tr><td>20Y</td><td>0</td><td>0</td><td>0</td><td>0</td><td>62</td><td>0</td><td>0</td><td>0</td></tr></table>

Source: DTCC, MS

## Callable Issuance Monitor

June issuance slowed along expected seasonal lines. Coupons on 6–10y supranational bonds have risen toward 5%, providing a healthier spread pickup over comparable-duration Treasuries.

Exhibit 11: Notional of callable issuance  
![](images/daf5df717b0144e2b58d1262a30e7df7a2b1273fa95eb3c2147d958d8063ee04.jpg)  
Source: Bloomberg, MS

Exhibit 12: Vega supply from callable issuance  
![](images/82da3655896c34190c13ccafc3188a331d685a7d5440b10433730da2007fffea.jpg)  
Source: Bloomberg, MS

Exhibit 13: Recent vega supply by pricing date  
![](images/8589469b012020b4298788d6bef20f8635b5b68ee947279bbf57dbe6f0b4314e.jpg)  
Source: Bloomberg, MS

Exhibit 14: Coupon of supranational issuance (6-10y maturity) vs. 10y Treasury yields  
![](images/04a857815dea418cca6e806ca1e27693628ce6aac4fb3777b32274c6ecedd44b.jpg)  
Source: Bloomberg, MS

## Skew Signal Monitor

The recent rally in long-end rates has been accompanied by a normalization in skew. The 21-day change in 3m10y skew has reverted to near zero. Skew signal suggests approximately 30% of max short duration exposure.

Exhibit 15: Skew change and duration position  
![](images/d14337b1aed417a78189c4b92d12b13e3546619960fa39c23faeac0406010573.jpg)  
Source: Bloomberg, S&P, MS.  
Exhibit 16: Duration position and signal performance

![](images/d5dcb0ec36779b805c8762fccdeb94480b4c1ce2cdc8bb9190c73a5c9475ae79.jpg)  
Source: Bloomberg, S&P, MS.

• Trade idea: Maintain long 2y10y straddle outright

• Trade idea: Maintain long 1y1y F/F+25/F+50 payer ladder

## Valuation Methodology and Risks

Below you will find a list of our current trade ideas, entry levels, entry dates, rationales, and risks.

<table><tr><td colspan="5">Interest Rate Derivatives</td></tr><tr><td>TRADE</td><td>ENTRY LEVEL</td><td>ENTRY DATE</td><td>RATIONALE</td><td>RISKS</td></tr><tr><td>Buy 2y10y straddle</td><td>670c</td><td>6/10/2026</td><td>2y10y expected to be supported by structural flow from mortgage hedgers demand and reduced supply from callable issuance.</td><td>The risk is if vol drops significantly while rates remain anchored near strike level.</td></tr><tr><td>Buy 1y1y F/F+25/F+50 payer ladder</td><td>0c</td><td>3/10/2026</td><td>Recent selloff in rates and pick up in vol created an attractive window for 1y1y payer ladders. Breakeven level sits at levels that imply Fed hike over the next 2 years.</td><td>The risk is if energy-driven inflation becomes sustainable and forces the Fed to hike rates as a response.</td></tr></table>

## Global Macro Strategy Team

<table><tr><td>MS &amp; CO. LLC</td><td>Matthew Hornbach, CMTMatthew.Hornbach@morganstanley.com</td><td>Global Head of Macro Strategy</td><td>+1 212 761-1837</td></tr><tr><td></td><td>Martin Tobias, CFA, CMT</td><td>US Rates Strategist</td><td>+1 212 761-6076</td></tr><tr><td></td><td>Shaun Zhou</td><td>US Rates Strategist</td><td>+1 212 761-3348</td></tr><tr><td></td><td>Aryaman Singh</td><td>US Rates Strategist</td><td>+1 212 761-1993</td></tr><tr><td></td><td>Eli Carter</td><td>US Rates Strategist</td><td>+1 212 761-4703</td></tr><tr><td>MS &amp; CO. LLC</td><td>Andrew Watrous</td><td>G10 FX Strategist</td><td>+1 212 761-5287</td></tr><tr><td></td><td>Molly Nickolin</td><td>G10 FX Strategist</td><td>+1 212 761-3592</td></tr><tr><td></td><td>Simon WaeverSimon.Waever@morganstanley.com</td><td>Head of EM Sovereign Credit and Latin America Fixed Income Strategy</td><td>+1 212 296-8101</td></tr><tr><td></td><td>Ioana Zamfir</td><td>Head of Latin America Macro Strategy</td><td>+1 212 761-4012</td></tr><tr><td></td><td>Emma Cerda</td><td>Latin America Sovereign Credit</td><td>+1 212 761-2344</td></tr><tr><td></td><td>Sofia Palacios</td><td>Latin America Macro Strategist</td><td>+1 212 761-0428</td></tr><tr><td>MS &amp; CO.INTERNATIONAL PLC</td><td>James K. LordJames.Lord@morganstanley.com</td><td>Global Head of FXEM Strategy</td><td>+44 20 7677-3254</td></tr><tr><td></td><td>Gianluca SalfordLuca.Salford@morganstanley.com</td><td>Head of European Rates Strategy</td><td>+44 20 7677-1337</td></tr><tr><td></td><td>Maria Chiara Russo</td><td>Euro Area Rates Strategist</td><td>+44 20 7425-3499</td></tr><tr><td></td><td>Fabio Bassanin, CFA</td><td>UK Rates Strategist</td><td>+44 20 7425-1869</td></tr><tr><td></td><td>David S. Adams, CFADavid.S.Adams@morganstanley.com</td><td>Head of G10 FX Strategy</td><td>+44 20 7425-3518</td></tr><tr><td></td><td>Neville Mandimika</td><td>CEEMEA Sovereign Credit Strategist</td><td>+44 20 7425-2509</td></tr><tr><td></td><td>Arnav Gupta</td><td>CEEMEA Rates Strategist</td><td>+44 20 7677-0382</td></tr><tr><td>MS ASIALIMITED+</td><td>Gek Teng Khoo</td><td>AXJ Macro Strategist</td><td>+

[中间内容因长度限制已省略]

ce Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Aryaman Singh; Shaun Zhou; Eli P Carter; Matthew Hornbach; Martin W Tobias, CFA.

© 2026 MS
"""
