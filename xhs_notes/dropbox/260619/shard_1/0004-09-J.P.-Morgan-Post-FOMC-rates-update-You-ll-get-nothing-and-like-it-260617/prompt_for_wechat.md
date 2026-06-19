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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Post-FOMC rates update

You'll get nothing and like it

- Front-end yields rose 11bp, and the broad curve flattened by a similar amount, as markets interpreted Chair Warsh's maiden voyage as FOMC chair in a hawkish fashion...  
- ...As a result, OIS forwards are now pricing in a full hike by the October FOMC meeting and in excess of 45bp of hikes by next spring. The implied distribution from options on Dec'26 SOFR futures shifted hawkishly and became more symmetric, with both tails strengthening, indicating elevated policy uncertainty.  
- Despite energy prices providing the opportunity to turn more dovish, the hawkish comments should continue to bias real yields higher and breakevens lower, in line with today's moves.  
- We think yields are biased higher over the near term, especially if those FOMC members who have forecast hikes this year take the opportunity to elaborate on their projections in the coming weeks...  
...Moreover, Warsh is more clearly putting his imprimatur on the Committee's communications, and reduced forward guidance risks volatility rising over time, which would also increase term premium and nominal yields. Even after today's move, curves still appear too steep, and we recommend maintaining 10s/30s flatteners.  
- We continue to expect no material near-term change to the Fed's balance sheet, particularly as Warsh indicated that the balance sheet task force's assessments would occur in 2H26—suggesting any resulting balance sheet changes could come in 2027.  
- A reduction in forward guidance could result in greater weights being placed on event days, which would help keep vols supported across the surface, especially in the upper left.  
- Treasury will auction \$24bn reopened 5-year TIPS at 1pm, unchanged in size from the last reopening in December. Against the backdrop of lower real yields, mixed valuations, and increased uncertainty, we think tomorrow's auction likely requires more of a concession in order to be digested smoothly.  
- Treasury will announce end-of-month supply at 11pm tomorrow. We think the 2-, 5-, and 7-year rolls should open at 0.75bp, 0.125bp, and 0.5bp, respectively.  
- The 2s/5s curve flattens into the lower end of its 2025-2026 trading range, now well below the 12-13bp mid-range technical inflection. Next support rests at 6bp and then the key 0bp range lows. We believe the curve will hold that support into the early summer period.

## Fixed Income Strategy

Jay Barry AC

(1-212) 834-4951

john.f.barry@JPM.com

Jason Hunter AC

(1-212) 270-0034

jason.x.hunter@JPM.com

Teresa Ho AC

(1-212) 834-5087

teresa.c.ho@JPM.com

Ipek Ozil AC

(1-212) 834-2305

ipek.ozil@JPM.com

Pankaj Vohra

(1-212) 834 5292

pankaj.x.vohra@jpmchase.com

Harry Downie

(1-212) 270-9500

harry.j.downie@JPM.com

Chris Hayward

(1-212) 622-6152

chris.hayward@jpmchase.com

Liam L Wash

(1-212) 834-5230

liam.wash@jpmchase.com

Amanda Berke

(1-212) 834-5739

amanda.berke@JPM.com

Molly Herckis

(1-212) 622-0899

molly.herckis@jpmchase.com

Emre Alptuna

(1-212) 270-4843

emre.alptuna@JPM.com

JPM Securities LLC

## Market views

Front-end yields rose 11bp, and the broad curve flattened by a similar amount, as markets interpreted Chair Warsh's maiden voyage as FOMC chair in a hawkish fashion. We tend to agree with the market's assessment and think this supports a continued bearish stance for a few reasons. First, the policy statement, projections, and prepared remarks were quite hawkish. The statement was completely overhauled and more closely resembled a statement from the Greenspan era, offering no forward guidance, but offering, “The Committee will deliver price stability” (see We don't need no stinking guidance, Michael Feroli, 6/17/2026). Second, the SEP was more hawkish than we had expected, as the 2026 dots show 12.5bp of rate hikes, and 6 of the 18 dots projected two or more hikes (Figure 1). Finally, the press conference read hawkishly as well, as Warsh led with the Committee’s commitment to price stability. Warsh was evasive when asked about the Fed’s current policy stance, but he offered, “The best way I can describe it is uneven. I see some restrictiveness in things like housing. It's hard to use those same words anywhere else.” Implicitly, he argued that policy is not restrictive now.

Figure 1: The 2026 dots show 12.5bp of rate hikes, and 6 of the 18 dots projected two or more hikes  
Distribution of projected midpoint of fed funds target range for 2026, March 2026 vs. June 2026; number of participants  
![](images/92a249bc929c91062af967744b4e483a171d3301d3f8ad892240e500016e43b5.jpg)

<details>
<summary>bar chart</summary>

| X-Axis | Mar-26 | Jun-26 |
|---|---|---|
| 2.625 | 1 | 0 |
| 2.875 | 2 | 0 |
| 3.125 | 2 | 0 |
| 3.375 | 7 | 1 |
| 3.625 | 7 | 8 |
| 3.875 | 0 | 3 |
| 4.125 | 0 | 5 |
| 4.375 | 0 | 1 |
</details>

Source: Federal Reserve

Figure 2: Both the statement and the press conference were scored hawkishly  
Fed Hawk-Dove Score\* of FOMC statements and prepared press conference remarks; Index  
![](images/3c7a87d99a557b1e370571dbc262ebdb785296bf2942f8bc3eca68e53870a925.jpg)

<details>
<summary>line chart</summary>

| Date   | Statement | Prepared remarks |
|--------|-----------|-----------------|
| Jun 21 | -45       | -15             |
| Jun 22 | 50        | 60              |
| Jun 23 | 45        | 40              |
| Jun 24 | 20        | 10              |
| Jun 25 | -20       | -10             |
| Jun 26 | 20        | 25              |
</details>

\*For methodology, see Listen up: Upgrading JPM's central bank NLP machine, Joseph Lupton and Dan Weitzenfeld, 7/2/2024
Source: JPM

Our NLP model agrees: it scored the statement as the most hawkish in a year, and the press conference was scored as the most hawkish since May 2024 (Figure 2). As a result, OIS forwards are now pricing in a full hike by the October FOMC meeting and in excess of 45bp of hikes by next spring. The implied distribution inferred from options on Dec'26 SOFR futures (Figure 3) changed substantially post-FOMC: the distribution shifted hawkishly, with the mean and mode both moving to the right. Interestingly, both tails strengthened, and the distribution now appears more symmetric, which indicates higher policy uncertainty post-FOMC.

Turning to inflation, markets reacted hawkishly, in line with nominals, with 5-,10-, and 30-year breakevens falling 3bp, 2bp, and 1bp, respectively. However, these changes were smaller in magnitude than the upward shifts in real yields, which rose by 10bp, 5bp, and 1bp in the 5-,10-, and 30-year tenors, respectively (Figure 4). When evaluating the impact on inflation going forward, we would highlight the following: First, the price goal for the Committee will, at least for now, be close to the one they have today. When asked whether he would review the 2% target, Warsh first stated that the Committee

needed to meet the 2% target, which they have not done over the last 5 years. In the last 5 years, alternative measures of inflation such as Truflation reached below 2%, whereas the traditional Fed gauge of core PCE reached a low of 2.61% in 2024, still 61bps above the 2% target, in line with Warsh's comments on missing the target. Second, Warsh downplayed the impact of the US-Iran conflict on inflation, given that half his colleagues believe that economic impacts of the conflict justify higher policy rates and half lower. Now that Brent crude oil has fallen from highs of 118 to below 80, the Fed Chair has the opportunity to lean on the impact of energy prices driving disinflation over the near term. As such, this impact risks lower breakevens than we previously assumed, in line with today's pricing (see TIPS Strategy: 2026 Mid-Year Outlook, 6/12/2026). The ultimate impact on inflation markets over the medium term will depend on the outcome of the task force on inflation and data gathering, which Warsh expects to be completed before year end.

Figure 3: Post-FOMC, the implied distribution for Dec '26 shifted hawkishly, and both tails strengthened, indicating higher policy uncertainty  
Probabilities of different fed funds outcomes for Dec '26 calculated from the risk-neutral probability density function\* inferred from Z6 3M SOFR futures options, 6/16 and 6/17  
![](images/75c9349557ae48d76447d800919d7bd2e94dd1052fda39e2579f6d7d8d6fa1d1.jpg)

<details>
<summary>bar chart</summary>

| Range | 6/16/2026 (%) | 6/17/2026 (%) |
| :--- | :--- | :--- |
| <3 | 2.0 | 2.5 |
| 3-3.25 | 0.5 | 5.0 |
| 3.25-3.5 | 5.0 | 9.5 |
| 3.5-3.75 | 31.0 | 14.5 |
| 3.75-4 | 24.0 | 17.0 |
| 4-4.25 | 16.0 | 16.0 |
| 4.25-4.5 | 9.5 | 13.0 |
| 4.5-4.75 | 4.0 | 9.5 |
| 4.75-5 | 1.0 | 6.0 |
| 5+ | 1.0 | 4.0 |
</details>

\* We compute call premiums for a broad range of strikes and apply the Breeden-Litzenberger method to infer the risk-neutral probability density function. We then use this to compute the market-implied probabilities of different Fed outcomes. See Interest Rate Derivatives 2026 Outlook, 11/25/2025 for full details. Implied distributions computed daily are included in the US Interest Rate Derivatives Package, available via JPM Markets
Source: JPM

Figure 4: Inflation markets shifted hawkishly with rising real yields and falling breakevens  
Daily change from 6/16 to 6/17 in 5-, 10-, and 30-year breakevens and real yields, bps  
![](images/8533c95397ea7b98dd584a7a27d667933446c8dfe3243e4570faaeae2abf8e82.jpg)

<details>
<summary>bar chart</summary>

| Category | Breakeven | Real yield |
|---|---|---|
| 5Yr | -2.6 | 10.4 |
| 10Yr | -1.7 | 5.3 |
| 30Yr | -1.4 | 1.1 |
</details>

Source: JPM

Looking ahead, with markets pricing in a significantly more hawkish path for Fed policy than the single hike we have forecast in 3Q27, it's tempting to think that yields should find some stability around current levels. However, we think there is a risk of further bearish follow-through, especially if those FOMC members who have forecast hikes this year take the opportunity to elaborate on their projections in the coming weeks. Moreover, Warsh is clearly putting his imprimatur on the Committee's communications more quickly than we had expected, as both the statement and prepared remarks had the lowest relevance scores in decades. As we have previously argued, improvements in the transparency of Fed communications to the public since the GFC likely supported moderating term premium in the decade leading up to the onset of the COVID-19 pandemic, and this is a significant independent variable in our term premium model. Reduced forward guidance risks volatility rising over time, which would also increase term premium and nominal yields (see In the eye of the beholder, 9/17/2023). Finally, we added 10s/30s flatteners as an expression of this view, because they expressed a bearish view with some relative value. Even with today's moves, the 10s/30s curve remains 12bp too steep after controlling for its fundamental drivers, nearly two standard deviations above our model-implied fair value. Net of these factors, we recommend

## maintaining 10s/30s flatteners.

Meanwhile, today's FOMC meeting did not provide any materially new details on balance sheet policy. However, one of the five task forces announced by Chair Warsh will focus on the balance sheet. We continue to expect no material near-term change to the Fed's balance sheet, particularly as Warsh indicated that the task force's assessments would occur in 2H—suggesting any resulting balance sheet changes could come in 2027. Additionally, any meaningful reduction in the size of the balance sheet would likely need to be accompanied by changes to liquidity regulation and further efforts to de-stigmatize the Fed's liquidity backstops in order to preserve the smooth functioning of funding markets.

On balance sheet composition, Warsh indicated that the task force will assess “the benefits and risks of the current ample-reserves regime as well as the composition of the balance sheet.” As we have discussed previously, roughly \$1.9tn of coupon-bearing Treasuries held in SOMA will mature between 2026 and 2030. While we think it is unlikely that the Fed would reinvest all of these maturities into T-bills, a more plausible approach would be to direct a portion—perhaps half—of these proceeds into bills

(Figure 5). Under such a scenario, the WAM of the SOMA portfolio would converge toward the maturity profile of outstanding Treasury debt by mid-2029, leaving reserves as the primary means to facilitate a smaller balance sheet (see The name on the front, 2/11/2026).

Figure 5: The WAM of the Fed's SOMA remains significantly longer than that of the overall Treasury market

Weighted average maturity of marketable Treasury debt outstanding and SOMA Treasury holdings, with JPM forecasts assuming baseline assumptions\* and alternate scenario\*\*; months

![](images/f86d126f54eeff8d84ee0bded049644695d7c7f7a0b2cb73a38a8a116b5fb74f.jpg)

<details>
<summary>line chart</summary>

| Date   | Overall WAM | SOMA WAM | Current add-on schedule | 50% reinvestment in bills |
|--------|-------------|----------|--------------------------|---------------------------|
| Dec 05 | 50          | 35       | 35                       | 35                        |
| Dec 10 | 60          | 80       | 80                       | 80                        |
| Dec 15 | 65          | 100      | 100                      | 100                       |
| Dec 20 | 70          | 90       | 90                       | 90                        |
| Dec 25 | 70          | 105      | 105                      | 105                       |
| Dec 30 | 65          | 65       | 65                       | 65                        |
</details>

\*See see The name on the front, 2/11/2026 for more details  
Source: Federal Reserve, US Treasury, JPM

Swap yields spiked \~12bp in the front end, in excess of our estimate of the delivered move that markets were pricing in, thanks to an SEP and press conference that read more hawkish than expected (Interest Rate Derivatives, US Fixed Income Markets Weekly, 6/5/2026). Looking ahead, a reduction in forward guidance could result in greater weight being placed on event days, which should help keep vols supported across the surface, especially in the upper left.

## 5-year TIPS auction preview

Treasury will auction \$24bn reopened 5-year TIPS at 1pm, unchanged in size from the last reopening in December. The last auction cleared 0.3bp cheap to pre-auction levels as the end-user share fell 3.1%-pts to 91.5%, roughly in line with its 6-month average. Auction allotment data shows foreign investor takedown fell 11.5%-pts to 10.5%, below the 6-month average, while investment manager demand rose 2.6%-pts to 74.6%

## (Figure 6).

Figure 6: The April 5-year TIPS auction cleared 0.5bp cheap to pre-auction levels as end-user demand rose to 91.5%  
Statistics for 5-year TIPS auctions; units as indicated

<table><tr><td>Date</td><td>Yield (%)</td><td>Size ($bn)</td><td>Tail (bp)</td><td>Bid/ cover</td><td>Direct (%)</td><td>Indirect (%)</td><td>End user (%)</td><td>Foreign (%)</td><td>Inv. mgr (%)</td></tr><tr><td>12/19/24</td><td>2.121</td><td>22</td><td>7.4</td><td>2.10</td><td>23.1</td><td>51.4</td><td>74.6</td><td>14.2</td><td>59.4</td></tr><tr><td>4/17/25</td><td>1.702</td><td>25</td><td>1.8</td><td>2.28</td><td>17.8</td><td>64.2</td><td>81.9</td><td>5.1</td><td>75.4</td></tr><tr><td>6/17/25</td><td>1.650</td><td>23</td><td>-1.6</td><td>2.53</td><td>18.8</td><td>74.6</td><td>93.4</td><td>4.4</td><td>87.8</td></tr><tr><td>10/23/25</td><td>1.182</td><td>26</td><td>1.1</td><td>2.51</td><td>24.4</td><td>62.1</td><td>86.5</td><td>9.9</td><td>75.5</td></tr><tr><td>12/18/25</td><td>1.433</td><td>24</td><td>-0.8</td><td>2.62</td><td>21.9</td><td>72.6</td><td>94.6</td><td>22.0</td><td>72.0</td></tr><tr><td>4/23/26</td><td>1.367</td><td>26</td><td>0.3</td><td>2.57</td><td>26.9</td><td>64.6</td><td>91.5</td><td>10.5</td><td>74.6</td></tr><tr><td>3-aucn avg</td><td>1.327</td><td>25</td><td>0.2</td><td>2.57</td><td>24.4</td><td>66.5</td><td>90.9</td><td>14.1</td><td>74.0</td></tr><tr><td>6-aucn avg</td><td>1.576</td><td>24</td><td>1.4</td><td>2.44</td><td>22.2</td><td>64.9</td><td>87.1</td><td>11.0</td><td>74.1</td></tr></table>

Source: US Treasury, JPM

Five-year real yields have risen 52bp since their last auction (26bp net of carry) and are now trading at their highest levels in over a year. Moreover, since the last auction, the 5s/10s real yield curve has flattened by 24bps over the period and is at its flattest level since January 2025. Additionally, Brent oil prices are down 25% over this time period, and we currently believe the stance of Fed policy is more restrictive than is necessary given the underlying economic backdrop (see U.S. Fixed Income Market Weekly, 06/12/2026). Meanwhile, 5-year breakevens have narrowed 21bp and are now in-line with their 3-year average. Breakevens have largely underperformed fundamentals in recent weeks and now appear roughly 44bp cheap to our fair value model, almost 3 standard deviations cheap (Figure 7).

Meanwhile, technicals appear supportive, with inflows into inflation-focused ETFs have remained largely positive since the last auction, suggesting increased focus on inflation protection and supporting asset manager demand. However, clients have become more neutral since March, with the active clients survey showing the most neutrals since March 30th, 2026. Additionally, the FOMC today added to uncertainty over the medium-term outlook for real yields and breakevens. Against the backdrop of higher real yields but increased uncertainty, we think tomorrow's auction will likely require more of a concession in order to be digested smoothly.

Figure 7: 5-year breakevens have underperformed fundamentals since May and no longer appear fairly valued to our framework  
5-year TIPS breakeven fair value model $^{*}$ ; bp  
![](images/76dfbd959967bd9fcc2491755096dab823be168454567c0a033a279a1ca52087.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jun 19 | -10   |
| Jun 20 | 35    |
| Jun 21 | 40    |
| Jun 22 | 55    |
| Jun 23 | 30    |
| Jun 24 | -20   |
| Jun 25 | -40   |
| Jun 26 | -50   |
</details>

\*Breakevens (bp) regressed against JPMCCI, JPMCCI-squared, 3mx3m/15mx3m OIS curve (bp), and VIX Index; model uses daily data over the past seven years; R^2 = 92.5%, SE=14.94bp Source: JPM

Figure 8: On-the-run volumes in the 5-year TIPS sector usually see a large spike on auction days  
Daily Treasury volumes of 5-year on-the-run TIPS versus 0- to 5-year TIPS off

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 17 Jun 2026 07:20 PM EDT

Disseminated 17 Jun 2026 07:20 PM EDT
"""
