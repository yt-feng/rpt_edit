You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
## Long Term Strategy

## Which equity income strategy long-term investors should adopt?

\- The current regime of “2020–2026 Post-COVID — AI era” has posed a challenge for traditional dividend income funds targeting high dividend yield as they significantly underperformed the broader market.

\- As a result of this large underperformance, there has been an increased focus on three alternative approaches beyond traditional high dividend yield strategies:

• Targeting high dividend growth stocks

\- Targeting high total shareholder yield stocks (i.e. dividend plus buyback yield)

\- Enhancement of equity income strategies via call overwriting i.e., strategies that harvest options income by sacrificing some of the equity upside

\- With the AI hype likely to eventually normalise, the regime we are likely to be on over the next ten years is in our opinion more likely to be like the “1963–1989 Normal business cycle swings” rather than the current “2020–2026 Post-COVID — AI era” regime.

\- This implies that over the long-term, the next ten years or so, asset allocation should factor in a strong positive correlation between the dividend and the value factor, a strong negative correlation between the dividend and the market/beta factor and a strong negative correlation between the dividend and the profitability factor.

\- At same time given the attractiveness of dividend growth strategies in terms of offering the best balance of good vol-adjusted returns, relatively consistent overall performance in drawdowns and some exposure to tech/growth factor, we believe that long-term investors aiming for equity income going forward should combine traditional dividend yield strategies with dividend growth strategies.

## Global Markets Strategy

Mika Inkinen AC
(44-20) 7742 6565
mika.j.inkinen@JPM.com
JPM Securities plc

Nikolaos Panigirtzoglou AC

(44-20) 7134-7815

nikolaos.panigirtzoglou@JPM.com

JPM Securities plc

Krutik P Mehta

(91-22) 6157-5016

krutik.mehta@jpmchase.com

JPM India Private Limited

Mayur Yeole

(91 22) 6157 3872

mayur.yeole@jpmchase.com

JPM India Private Limited

Equity income strategies such as those focusing on dividend yields have traditionally been a significant component of investor portfolios as historically around a third of total equity returns have come from dividends. The importance of equity income strategies naturally increases in periods of low interest rates such as that seen between the financial crisis of 2008 and 2021.

Since 2022, the shift to a higher interest rate environment has somewhat hit the relative attractiveness of equity dividend yields vs bond yields. However, as shown by Figure 1 which depicts the MSCI World Index dividend yield vs the Global Agg Bond Index yield to worst, the gap between bond yields and dividend yield had been much larger in previous periods, such as during 1990s, without denting the interest on high dividend yield stocks at the time. This is shown by Figure 2 which depicts the google books search for keyword “equity income”. The frequency of mentioning or popularity of the theme of “equity income” kept rising steadily from 1970s to around 2004 with a declining trend from 2004 till the pandemic. Post the pandemic there has been stabilization.

Figure 1: MSCI World Index dividend yield vs Global Agg Bond Index yield to worst  
![](images/a9aa09b6a3d46b7cfb9c46db95a8a5c658fe4e3a22ecb873eee72a400204fd98.jpg)  
Source: Bloomberg Finance L.P., JPM.

Figure 2: Google books search for keyword “equity income”  
![](images/e3fe51a6db7428420b6e6f716364632f830126658f0eee2dd38f995ba095524f.jpg)  
Source: Google.

The decline since 2004 perhaps reflects the rise in tech in equity markets which reduced the attractiveness of traditional dividend income strategies given these strategies are inherently underweights tech. This is shown in Figure 3, which

depicts the sectoral deviation vs the S&P500 index of the 10 largest US high dividend yield funds. These high dividend yield funds have been typically UW Tech, Communication Services and Consumer Discretionary sectors and OW Financials, Staples, Energy, Healthcare.

Figure 3: Sectoral deviation vs the S&P500 index of the 10 largest US high dividend yield funds  
![](images/7410efa0ffc4711cbc95f35f03beb51e8e9b9c572d3c97032114a287be6683e6.jpg)  
Source: Bloomberg Finance L.P., JPM.  
That said, high dividend yield stocks have other properties that make them attractive to investors. For example using the Fama-French equity factors and by looking at the correlation matrix (Figure 4) of 6 factors (Mkt\_RF-overall market or beta factor, SMB-size factor, HML-value factor, RMW-operating profitability factor, CMA-conservative investment factor, DY-dividend yield factor proxied by the difference in the performance of high vs low dividend yield stocks), we find that there has been strong negative correlation between the market/beta factor and the dividend yield factor, suggests that high dividend yield stocks historically served as a hedge to equity market drawdowns. The strong negative correlation between the market factor and the dividend factor reflects at least partly the growth tilt of the equity market as during strong equity market phases, growth stocks tend to outperform more value oriented /dividend stocks.

## Figure 4: Correlation Matrix

Based on monthly data from 1963 to 2026.

<table><tr><td></td><td>Mkt_RF</td><td>SMB</td><td>HML</td><td>RMW</td><td>CMA</td><td>DY</td></tr><tr><td>Mkt_RF</td><td>1</td><td>0.27</td><td>-0.21</td><td>-0.19</td><td>-0.36</td><td>-0.52</td></tr><tr><td>SMB</td><td>0.27</td><td>1</td><td>0.01</td><td>-0.34</td><td>-0.08</td><td>-0.21</td></tr><tr><td>HML</td><td>-0.21</td><td>0.01</td><td>1</td><td>0.09</td><td>0.68</td><td>0.68</td></tr><tr><td>RMW</td><td>-0.19</td><td>-0.34</td><td>0.09</td><td>1</td><td>0.01</td><td>0.06</td></tr><tr><td>CMA</td><td>-0.36</td><td>-0.08</td><td>0.68</td><td>0.01</td><td>1</td><td>0.61</td></tr><tr><td>DY</td><td>-0.52</td><td>-0.21</td><td>0.68</td><td>0.06</td><td>0.61</td><td>1</td></tr></table>

Source: JPM.

The correlation matrix of Figure 4 provides some additional insights:

\- Value–Conservative Investment–Dividend Cluster (HML,

CMA, DY factors) are highly correlated and thus using all three of them in a multi-factor portfolio would induce multicollinearity. What creates this high correlation is relatively simple: firms with high book-to-market (value stocks) tend to be conservative in terms of their propensity to invest and firms that invest conservatively tend to also pay higher dividends.

\- The profitability factor (RMW) is effectively orthogonal to the value/conservative investment/dividend cluster.

\- The size factor is negatively correlated with the dividend factor as small stocks tend to pay lower dividends.

Do the above correlations change across sub periods? Have there been any structural changes? To answer this question, we look at Figure 5 which depicts the DY factor correlations across sub-periods.

Figure 5: DY Factor Correlations Across Sub-Periods

<table><tr><td>Period</td><td>Mkt_RF</td><td>SMB</td><td>HML</td><td>RMW</td><td>CMA</td></tr><tr><td>1963-1975</td><td>-0.50</td><td>-0.23</td><td>0.80</td><td>-0.49</td><td>0.75</td></tr><tr><td>1976-1989</td><td>-0.69</td><td>-0.41</td><td>0.80</td><td>-0.31</td><td>0.62</td></tr><tr><td>1990-1999</td><td>-0.66</td><td>-0.32</td><td>0.74</td><td>0.21</td><td>0.75</td></tr><tr><td>2000-2009</td><td>-0.34</td><td>-0.26</td><td>0.68</td><td>0.42</td><td>0.50</td></tr><tr><td>2010-2019</td><td>-0.60</td><td>-0.31</td><td>0.07</td><td>0.47</td><td>0.37</td></tr><tr><td>2020-2026</td><td>-0.30</td><td>0.39</td><td>0.76</td><td>0.08</td><td>0.58</td></tr></table>

Source: JPM.

Overall Figure 5 points to five distinct regimes:

1963–1989 (Normal business cycle swings): DY strongly correlated with HML (+0.80) and CMA (+0.75), strongly negatively correlated with Mkt\_RF (-0.50 to -0.68) and RMW (-0.31 to -0.49). Traditional correlation between “value” and “income” factors.

1990–1999 (Dot-Com bubble era-dominance of growth stocks): DY vs RMW flips from negative to positive (+0.21). As growth stocks dominated, the profitability factor's relationship with dividends changed.

2000–2009 (credit bubble and GFC crisis): DY vs RMW reaches +0.42. Flight-to-quality during the financial crisis strengthened the link between dividends and profitability. DY vs Mkt\_RF weakens to -0.34.

2010–2019 (Low-Rate Environment post GFC): structural break, DY vs HML collapses to +0.07 (from +0.68 in prior period). The prolonged low-rate environment caused investors to chase yield regardless of value characteristics, decoupling dividend yield from traditional value.

2020–2026 (Post-COVID — AI era): Massive policy interventions and the emergence of the AI trade reshape factor relationships, DY vs SMB flips positive (+0.39) for the first time in 60 years. DY vs HML rebounds to +0.76. DY vs RMW drops back to near-zero (+0.08).

The above observations suggest portfolio construction/asset allocation for long term investors is regime dependent. And with the AI hype likely to eventually normalise, the regime we are likely to be on over the next ten years is in our opinion more likely to be like the “1963–1989 Normal business cycle swings” rather than the current “2020–2026 Post-COVID — AI era” regime.

This implies that over the long-term, the next ten years or so, asset allocation should factor in a strong positive correlation between the dividend and the value factor, a strong negative correlation between the dividend and the market/beta factor and a strong negative correlation between the dividend and the profitability factor.

At the same time, we recognize that the current regime of “2020–2026 Post-COVID — AI era” has posed a challenge for traditional dividend income funds targeting high dividend yield as they significantly underperformed the broader market. As a result of this large underperformance, there has been an increased focus on three alternative approaches beyond traditional high dividend yield strategies:

1. Targeting high dividend growth stocks

2. Targeting high total shareholder yield stocks (i.e. dividend plus buyback yield)

3. Enhancement of equity income strategies via call overwriting i.e., strategies that harvest options income by sacrificing some of the equity upside

How big has the shift been towards these three new approaches? Have they outperformed the traditional approach targeting high dividend yields?

To assess how these strategies have performed in practice, we look at total returns on equity ETFs and mutual funds in the following categories: dividend yield-focused, dividend growth-focused, total shareholder yield and enhanced or option-augmented equity income. Returns are equal-weighted within each category to reflect strategy-level outcomes, rather than be dominated by individual large funds, and we focus on the period from 2014 onward, as there are few funds of the latter three categories trading before then. We use up to ten of the largest ETFs and mutual funds for each category. Figure 6 shows the cumulative returns for the four strategies. While the four strategies had followed each other more closely up to 2020, there has been a notable divergence since then with the

dividend growth strategies compounding most strongly.  
Figure 6: Cumulative return on equity income funds  
![](images/51edcab68288da718f0d3749a47a3a5f07ce158086c99a29c3080df92bb70c11.jpg)  
Source: JPM.

Figure 7 shows annualized returns and information ratios for these strategies for the full sample as well as a split to pre-2020 and post-2020 periods. The overall returns and information ratios for the traditional income strategies focused on dividend yield and dividend growth were closer to the S&P 500 in the pre-2020 period. Post-pandemic, however, the returns of the S&P, increasingly dominated by a relatively small number of mega-cap tech companies that are under-weighted by these income strategies, have outperformed both outright and on a risk-adjusted basis. Dividend growth funds outperformed dividend yield funds in both periods both on an outright and risk-adjusted basis, but while the total yield focused funds outperformed both in the post-2020 period outright higher volatility dragged risk-adjusted returns lower. The latter may be e.g. due to higher tech content and a smaller, less established fund universe of total yield focused funds. And the enhanced/option-augmented strategies have produced similar returns on a risk adjusted basis post-2020 at the expense of somewhat lower absolute returns, likely on a combination of a reduction in market beta via premium income from call overwriting offsetting some of the negative returns in drawdowns (and some strategies within these category buy puts for downside protection) while also capping some of the upside in recoveries.

Figure 7: Annualized return and information ratio of S&P 500 and equity income funds

<table><tr><td>Annualized return</td><td>SPX</td><td>Dividend yield-focused</td><td>Dividend growth-focused</td><td>Total yield focused</td><td>Enhanced/Option-augmented</td></tr><tr><td>2014-2019</td><td>11.3%</td><td>9.6%</td><td>10.9%</td><td>9.2%</td><td>7.6%</td></tr><tr><td>2020-2026</td><td>14.8%</td><td>10.3%</td><td>11.7%</td><td>12.1%</td><td>8.9%</td></tr><tr><td>Full sample</td><td>13.0%</td><td>10.0%</td><td>11.4%</td><td>10.6%</td><td>8.3%</td></tr><tr><td>IR</td><td colspan="5"></td></tr><tr><td>2014-2019</td><td>1.00</td><td>0.94</td><td>0.97</td><td>0.71</td><td>0.83</td></tr><tr><td>2020-2026</td><td>0.86</td><td>0.64</td><td>0.70</td><td>0.62</td><td>0.68</td></tr><tr><td>Full sample</td><td>0.89</td><td>0.74</td><td>0.80</td><td>0.64</td><td>0.74</td></tr></table>

Source: JPM.

To examine drawdowns more specifically, Figure 8 shows cumulative maximum drawdowns from prior peaks in time series form, while Figure 9 shows the maximum end-month drawdown for each strategy across six key correction episodes.

Figure 8: Drawdowns of S&P 500 and equity income fund types  
![](images/5ef392a87693331d3acb9dcfd211e96992f1edf5034466eab7389bdfeb25a957.jpg)  
Source: JPM.

Figure 9: Maximum drawdowns by episode

<table><tr><td>Maximum end-month drawdown in:</td><td>SPX</td><td>Dividend yield-focused</td><td>Dividend growth-focused</td><td>Total yield-focused</td><td>Enhanced/Option-augmented</td></tr><tr><td>Sep15/Jan16 China deval/EM growth scare</td><td>-8.6%</td><td>-8.7%</td><td>-9.0%</td><td>-11.1%*</td><td>-7.3%</td></tr><tr><td>Dec18 Fed tightening/liquidity withdrawal</td><td>-14.2%</td><td>-10.1%</td><td>-12.4%</td><td>-16.2%</td><td>-11.8%</td></tr><tr><td>Mar20 Pandemic</td><td>-20.7%</td><td>-25.8%</td><td>-24.5%</td><td>-30.9%</td><td>-23.7%</td></tr><tr><td>Sep22 Inflation shock</td><td>-25.4%</td><td>-14.8%</td><td>-20.6%</td><td>-21.7%</td><td>-17.6%</td></tr><tr><td>Apr25 Liberation day</td><td>-7.7%</td><td>-7.2%</td><td>-9.0%</td><td>-11.9%</td><td>-6.4%</td></tr><tr><td>Mar26 Middle East conflict</td><td>-5.8%</td><td>-4.1%</td><td>-5.4%</td><td>-2.6%</td><td>-4.0%</td></tr></table>

\* Trough in Jan16 for total yield-focused, Sep15 for S&P and other income strategies. Source: JPM.

The first episode shows a relatively uniform drawdown across the S&P as well as different equity income types. The second shows significant downside mitigation relative to the broader market for most income strategies (with the exception of total shareholder yield), particularly for the dividend yield focused and option-augmented income strategies, where a value/short duration tilt supported the former while the latter saw offsets from call writing to augment income and/or buy some puts for downside protection. The third, the pandemic shock, hit equity income strategies harder than the broader market both on the way down and in the recovery as earnings impairments and dividend cuts in energy, financials and real estate weighed on income strategies disproportionately while the S&P's greater exposure to tech supported the broader market on a relative basis. The fourth was an inflation shock that prompted significant central bank interest rate hikes, which disproportionately hurt long-duration growth stocks and within income strategies dividend growth focused funds with a higher quality/growth tilt that also skews longer duration as well as total shareholder yield focused funds amid longer-duration tech/growth tilts than dividend yield strategies. By contrast, income funds focusing on current yields with a shorter-duration tilt held up better and option-augmented strategies perhaps also benefited from higher implied volatility boosting premium income and/or put exposure. The fifth was a tariff shock and the sixth a geopolitical uncertainty shock that both saw elevated uncertainty, which saw broadly similar drawdowns overall though the option-augmented income funds likely benefited from option premium income while total shareholder yield did better in the sixth episode.

Taken together, the above highlights that the relative drawdown performance of equity income funds is fundamentally regime-dependent. In monetary tightening-driven corrections in 2018 and 2022, income strategies particularly based on dividend yield benefited from a short-duration value tilt while long duration assets suffered. In the earnings/cash flow destruction shock in 2020, income strategies broadly underperformed the broader market. Dividend yield and growth strategies were penalised as their sector composition (e.g. lower exposure to tech and higher exposure to sectors where earnings/dividends suffered) amplified the initial loss and lagged in the recovery, while total shareholder yield strategies likely suffered from higher mid-cap exposure. And in the shorter, sharper vol spikes in 2015, 2025 and 2026 option-augmented strategies most consistently demonstrated resilience from premium income. A related distinction is that traditional income strategies based on dividend yield and dividend growth can behave differently, with the former having more of a value tilt given it focuses on current yield while the latter has more of a quality/growth tilt, while total shareholder yield strategies appear to introduce a more procyclical element via buybacks.

In the shorter, sharper volatility episodes of 2015, 2025, and 2026, option-augmented strategies most consistently demonstrated resilience from premium income, while total shareholder yield strategies were disproportionately impaired in the tariff shock of 2025 — reflecting t

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 14 Jul 2026 04:04 PM BST

Disseminated 14 Jul 2026 04:04 PM BST
"""
