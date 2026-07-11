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
## The force awakens

\- We expect core CPI inflation remained relatively stable at $0.215\%$ m-o-m in June following a $0.208\%$ advance in May. Core goods inflation remained negative in June, while supercore CPI accelerated.

\- Overall, based on our CPI and PPI forecast, core PCE inflation likely moderated slightly to $0.271\%$ m-o-m from $0.320\%$ in May, leaving y-o-y inflation at $3.4\%$ , well above the Fed's target. However, considering the upcoming methodology changes to certain PCE prices, core PCE inflation is unlikely to accelerate more than the median SEP forecast implies.

## Research Analysts

North America Economics

Aichi Amemiya - NSI
aichi.amemiya@NOM.com
+1 212 667 9347

Jeremy Schwartz - NSI
jeremy.schwartz@NOM.com
+1 212 667 9637

Ruchir Sharma - NSI  
ruchir.sharma@NOM.com  
+1 212 667 9186

\- The Fed announced the members of five task forces. We think that the choice of members does not signal any clear bias in terms of the future path of monetary policy. Future work by the task forces will likely be evolutionary as opposed to revolutionary.

## Another benign reading of core CPI inflation is expected

We expect core CPI inflation remained relatively stable at $0.215\%$ m-o-m in June after having risen by $0.208\%$ in May and $0.376\%$ in April (Fig. 1).

The impact from tariffs has been waning, and used vehicle prices declined. The global shortage of semiconductors did not appear to exert significant upward pressures on consumer electronics prices in the month. As a result, we expect a second consecutive decline in CPI core goods prices (Fig. 2).

Fig. 1: We expect core CPI inflation remained relatively stable at $0.215\%$ m-o-m in June

Decomposition of m-o-m core CPI inflation

![](images/6c1d25dbdce371f301c681a376deb506c128b8a9c87b2ddc60f0d5ab86afa8df.jpg)  
Note: For CPI components that are not available in October 2025, we assume no inflation on a not-seasonally adjusted basis for survey-based components, but seasonal adjustment is applied.  
Source: BLS, Haver, NOM

Fig. 2: Core goods inflation likely remained negative in June, partly due to lower used vehicle prices Decomposition of m-o-m core goods CPI inflation  
![](images/7b19dbe04918406a6002382b82cc94cc8814d410f4aab2a062b9f96702bfa5b8.jpg)  
Source: BLS, Haver, NOM

Our forecast for supercore CPI inflation is $0.373\%$ m-o-m for June, above the $0.273\%$ advance in May (Fig. 3). Lodging-away-from home prices likely rose, somewhat boosted by the FIFA World Cup. By contrast, we expect inflation of transportation service prices

Fig. 4: Core PCE inflation likely moderated slightly, but remained elevated in June Decomposition of m-o-m core PCE inflation by data source remained soft in June as lower jet fuel prices appear to have weighed down airline fares in the middle of June.

We expect inflation of regular rent and owners' equivalent rent (OER) moderated to $0.24\%$ m-o-m and $0.28\%$ m-o-m in June, as temporary strength in May likely waned in June.

Fig. 3: CPI supercore inflation likely accelerated in June Decomposition of m-o-m CPI supercore inflation  
![](images/dbaa6b2d69e3fb8b3aae9f61a903adbe340ba0aefe9c9c7046b97f2fdf09d8d0.jpg)  
Source: BLS, Haver, NOM

![](images/e5bfaa0f2b1f736158f173fe62acbf2e17ebd0c69e9f3354426e8146eb448a84.jpg)  
Source: BLS, BEA, Haver, NOM

Based on our forecasts for CPI and PPI data, we expect June core PCE inflation to moderate modestly to $0.271\%$ m-o-m from $0.320\%$ in May, which would keep y-o-y inflation at $3.4\%$ (Fig. 4). Some expected softness in June CPI data does not feed into core PCE inflation, while PPI's portfolio management and investment advice services, a key input into core PCE inflation, appears to have increased at a decent pace of $2.7\%$ m-o-m in June, which helps core PCE inflation outpace core CPI inflation.

As discussed in our recent note, the BEA will make substantial changes to the way it estimates PCE prices for computer software and accessories, portfolio management and investment advice services, and legal services. The combined contribution of those components to y-o-y core PCE inflation was about 60bp in May (Fig. 5). We estimate that those methodological changes will reduce y-o-y core PCE inflation by about 20bp. Against this backdrop, policymakers might discount some of the anticipated boost from portfolio management and investment advice prices (\~5bp to June core PCE inflation).

Beyond June, we expect that warning impact of tariffs, lower crude oil prices, moderating wage growth and negative residual seasonality (Fig. 6) will lead to gradual moderation in core PCE inflation, which is consistent with our Fed call of no rate hikes through the end of 2027.

Fig. 5: Portfolio management & investment advice services, and computer software & accessories substantially boosted core PCE inflation

Contributions to y-o-y core PCE inflation from the components that are subject to methodological changes

![](images/bfb17e448992a14d2289dfdcd321bf3e27d87bdcf159cdfe3771ea9ff1c652e0.jpg)  
Source: BEA, Haver, NOM

Fig. 6: M-o-M core PCE inflation tends to be weighed down by negative residual seasonality in the second half of the year The median and average of m-o-m core PCE inflation by month over the past three years vs. 2026  
![](images/60989b1747b9692cbfadde00d189334414c956c4338dfe9210cdaa1a95970ae5.jpg)  
Source: BEA, Haver, NOM

## Rollout of the Fed task force members

The Fed announced the leadership of five task forces as part of Chair Warsh's broader review of the monetary policy framework. We do not see any clear bias in the choice of members in terms of rate policy. Based on these personnel choices, we expect policy recommendations will be evolutionary, not revolutionary.

In some cases, such as the balance sheet task force, Warsh has included members who might oppose his long-held views, a signal that the results of the task force are not a fait accompli. We think this will increase credibility on future work from those task forces.

Although the purpose of task forces is not to discuss fiscal policy, some members appear to favor limiting not using the Fed's balance sheet to accommodate expansionary fiscal policy, which is consistent with Warsh's previous comment that the Fed should "get out of the fiscal business."

There is a risk that a majority of the FOMC participants might not accept policy proposals from the task forces, which are expected to be submitted by the end of this year. Note that New York Fed President Williams described the timeline of task forces as “pretty aggressive.”

Chair Warsh announced the leadership of the five task forces. The Fed statement noted that each task force will consider whether policymakers' means and methods, analytical tools, and policy approaches can be improved upon. Members include former central bankers, industry professionals, and academics. Overall, the statement suggests the review is comprehensive and not focused on a narrow set of goals.

## Warsh's testimony next week is unlikely to break new ground

In terms of Fedspeak next week, the highlight is Warsh's first semi-annual testimony at House Financial Service Committee on Tuesday and Senate Banking Committee on Wednesday. Given that affordability issues are at the center of discussions, Warsh will stress the importance of achieving price stability, but fall short of how to do so. Now that the five task forces will commence, we expect Warsh to defer to future work by the task forces when asked about the monetary policy outlook. Elsewhere, Governors Waller, Barr, Cook, Bowman, and Jefferson, regional Fed presidents Williams, Musalem, Logan, and Schmid will be speaking publicly next week.

## Growth momentum continues

Data scheduled for release next week is likely to point to continued resilience in growth. We expect retail sales growth slowed to 0.3% in June following a 0.9% increase in May. The weakness was primarily driven by a decline in gasoline sales, while other components remained strong. Industrial production likely rebounded, supported by stronger

manufacturing output, including gains in both autos and core manufacturing.

## Q2 GDP tracking

We have lowered our Q2 GDP tracking estimate to $2.3\%$ q-o-q ar from $2.4\%$ last week.

Our estimate for real final sales to private domestic purchasers edged up to 2.9%.

Fig. 7: NOM's inflation forecasts (without the impact of upcoming methodology changes to certain PCE prices)

<table><tr><td rowspan="2"></td><td colspan="2">Headline PCE</td><td colspan="3">Core PCE</td><td colspan="2">Headline CPI</td><td colspan="3">Core CPI</td><td>CPI NSA</td></tr><tr><td>m/m %</td><td>y/y %</td><td>m/m %</td><td>y/y %</td><td>qtrly, y/y %</td><td>m/m %</td><td>y/y %</td><td>m/m %</td><td>y/y %</td><td>qtrly, y/y %</td><td>Index</td></tr><tr><td>Jan-25</td><td>0.35</td><td>2.61</td><td>0.31</td><td>2.78</td><td></td><td>0.43</td><td>3.00</td><td>0.43</td><td>3.26</td><td></td><td>317.671</td></tr><tr><td>Feb-25</td><td>0.40</td><td>2.71</td><td>0.45</td><td>2.97</td><td></td><td>0.23</td><td>2.82</td><td>0.25</td><td>3.12</td><td></td><td>319.082</td></tr><tr><td>Mar-25</td><td>0.02</td><td>2.36</td><td>0.10</td><td>2.67</td><td>2.81</td><td>0.03</td><td>2.39</td><td>0.07</td><td>2.79</td><td>3.08</td><td>319.799</td></tr><tr><td>Apr-25</td><td>0.17</td><td>2.28</td><td>0.19</td><td>2.61</td><td></td><td>0.16</td><td>2.31</td><td>0.24</td><td>2.78</td><td></td><td>320.795</td></tr><tr><td>May-25</td><td>0.18</td><td>2.46</td><td>0.23</td><td>2.78</td><td></td><td>0.10</td><td>2.35</td><td>0.13</td><td>2.79</td><td></td><td>321.465</td></tr><tr><td>Jun-25</td><td>0.29</td><td>2.59</td><td>0.26</td><td>2.81</td><td>2.74</td><td>0.25</td><td>2.67</td><td>0.23</td><td>2.93</td><td>2.82</td><td>322.561</td></tr><tr><td>Jul-25</td><td>0.17</td><td>2.61</td><td>0.25</td><td>2.86</td><td></td><td>0.23</td><td>2.70</td><td>0.31</td><td>3.06</td><td></td><td>323.048</td></tr><tr><td>Aug-25</td><td>0.26</td><td>2.75</td><td>0.22</td><td>2.91</td><td></td><td>0.35</td><td>2.92</td><td>0.31</td><td>3.11</td><td></td><td>323.976</td></tr><tr><td>Sep-25</td><td>0.26</td><td>2.79</td><td>0.19</td><td>2.83</td><td>2.87</td><td>0.30</td><td>3.01</td><td>0.22</td><td>3.02</td><td>3.06</td><td>324.800</td></tr><tr><td>Oct-25</td><td>0.19</td><td>2.71</td><td>0.23</td><td>2.75</td><td></td><td>0.03</td><td>2.76</td><td>0.11</td><td>2.81</td><td></td><td>324.372</td></tr><tr><td>Nov-25</td><td>0.22</td><td>2.82</td><td>0.18</td><td>2.83</td><td></td><td>0.22</td><td>2.74</td><td>0.08</td><td>2.63</td><td></td><td>324.122</td></tr><tr><td>Dec-25</td><td>0.33</td><td>2.88</td><td>0.33</td><td>2.97</td><td>2.85</td><td>0.30</td><td>2.68</td><td>0.23</td><td>2.64</td><td>2.69</td><td>324.054</td></tr><tr><td>Jan-26</td><td>0.35</td><td>2.88</td><td>0.44</td><td>3.10</td><td></td><td>0.17</td><td>2.39</td><td>0.30</td><td>2.50</td><td></td><td>325.252</td></tr><tr><td>Feb-26</td><td>0.40</td><td>2.87</td><td>0.39</td><td>3.05</td><td></td><td>0.27</td><td>2.41</td><td>0.22</td><td>2.46</td><td></td><td>326.785</td></tr><tr><td>Mar-26</td><td>0.67</td><td>3.54</td><td>0.30</td><td>3.25</td><td>3.14</td><td>0.87</td><td>3.26</td><td>0.20</td><td>2.60</td><td>2.53</td><td>330.213</td></tr><tr><td>Apr-26</td><td>0.41</td><td>3.80</td><td>0.25</td><td>3.32</td><td></td><td>0.64</td><td>3.81</td><td>0.38</td><td>2.75</td><td></td><td>333.020</td></tr><tr><td>May-26</td><td>0.45</td><td>4.07</td><td>0.32</td><td>3.41</td><td></td><td>0.47</td><td>4.25</td><td>0.21</td><td>2.85</td><td></td><td>335.123</td></tr><tr><td>Jun-26</td><td>0.038</td><td>3.814</td><td>0.271</td><td>3.420</td><td>3.38</td><td>-0.203</td><td>3.754</td><td>0.215</td><td>2.804</td><td>2.79</td><td>334.671</td></tr><tr><td>Jul-26</td><td>0.12</td><td>3.76</td><td>0.21</td><td>3.38</td><td></td><td>0.07</td><td>3.60</td><td>0.22</td><td>2.71</td><td></td><td>334.675</td></tr><tr><td>Aug-26</td><td>0.22</td><td>3.71</td><td>0.20</td><td>3.36</td><td></td><td>0.24</td><td>3.48</td><td>0.22</td><td>2.62</td><td></td><td>335.244</td></tr><tr><td>Sep-26</td><td>0.20</td><td>3.65</td><td>0.20</td><td>3.37</td><td>3.37</td><td>0.21</td><td>3.37</td><td>0.22</td><td>2.61</td><td>2.65</td><td>335.759</td></tr><tr><td>Oct-26</td><td>0.14</td><td>3.60</td><td>0.22</td><td>3.36</td><td></td><td>0.09</td><td>3.43</td><td>0.22</td><td>2.73</td><td></td><td>335.500</td></tr><tr><td>Nov-26</td><td>0.21</td><td>3.59</td><td>0.21</td><td>3.39</td><td></td><td>0.22</td><td>3.41</td><td>0.22</td><td>2.87</td><td></td><td>335.177</td></tr><tr><td>Dec-26</td><td>0.25</td><td>3.50</td><td>0.21</td><td>3.27</td><td>3.34</td><td>0.28</td><td>3.37</td><td>0.22</td><td>2.85</td><td>2.82</td><td>334.989</td></tr><tr><td>Jan-27</td><td>0.20</td><td>3.35</td><td>0.25</td><td>3.07</td><td></td><td>0.18</td><td>3.39</td><td>0.27</td><td>2.82</td><td></td><td>336.286</td></tr><tr><td>Feb-27</td><td>0.15</td><td>3.09</td><td>0.20</td><td>2.88</td><td></td><td>0.12</td><td>3.25</td><td>0.20</td><td>2.80</td><td></td><td>337.403</td></tr><tr><td>Mar-27</td><td>0.19</td><td>2.60</td><td>0.20</td><td>2.78</td><td>2.91</td><td>0.18</td><td>2.57</td><td>0.20</td><td>2.80</td><td>2.81</td><td>338.703</td></tr><tr><td>Apr-27</td><td>0.13</td><td>2.31</td><td>0.20</td><td>2.73</td><td></td><td>0.08</td><td>1.98</td><td>0.19</td><td>2.62</td><td></td><td>339.597</td></tr><tr><td>May-27</td><td>0.15</td><td>2.00</td><td>0.20</td><td>2.61</td><td></td><td>0.11</td><td>1.59</td><td>0.19</td><td>2.60</td><td></td><td>340.448</td></tr><tr><td>Jun-27</td><td>0.16</td><td>2.13</td><td>0.20</td><td>2.53</td><td>2.62</td><td>0.14</td><td>1.94</td><td>0.19</td><td>2.57</td><td>2.60</td><td>341.162</td></tr><tr><td>Jul-27</td><td>0.18</td><td>2.19</td><td>0.19</td><td>2.52</td><td></td><td>0.17</td><td>2.04</td><td>0.19</td><td>2.54</td><td></td><td>341.509</td></tr><tr><td>Aug-27</td><td>0.19</td><td>2.17</td><td>0.19</td><td>2.50</td><td></td><td>0.20</td><td>2.00</td><td>0.18</td><td>2.50</td><td></td><td>341.952</td></tr><tr><td>Sep-27</td><td>0.21</td><td>2.18</td><td>0.19</td><td>2.48</td><td>2.50</td><td>0.23</td><td>2.02</td><td>0.18</td><td>2.47</td><td>2.50</td><td>342.557</td></tr><tr><td>Oct-27</td><td>0.15</td><td>2.19</td><td>0.19</td><td>2.45</td><td></td><td>0.12</td><td>2.06</td><td>0.18</td><td>2.43</td><td></td><td>342.397</td></tr><tr><td>Nov-27</td><td>0.21</td><td>2.20</td><td>0.18</td><td>2.43</td><td></td><td>0.23</td><td>2.08</td><td>0.18</td><td>2.38</td><td></td><td>342.137</td></tr><tr><td>Dec-27</td><td>0.25</td><td>2.19</td><td>0.18</td><td>2.40</td><td>2.43</td><td>0.28</td><td>2.09</td><td>0.18</td><td>2.34</td><td>2.38</td><td>341.981</td></tr></table>

Source: BLS, BEA, Haver, NOM  
Note: Oct and Nov CPI refers to NOM's estimates.

## Data Preview

## The week ahead

We expect a $0.215\%$ m-o-m rise in the core CPI in June.

Consumer prices (Tuesday): We expect core CPI inflation remained relatively stable at 0.215% m-o-m in June, after a 0.208% advance in May.

The waning impact from tariffs and lower used vehicle prices likely kept month-on-month core goods inflation in contractionary territory.

We expect supercore CPI inflation accelerated to $0.373\%$ m-o-m in June, following a $0.273\%$ advance in May. A positive impact from higher lodging-away-from-home prices appears to have been partially offset by slower increases in airline fares and medical care service prices. Inflation of rent-related components likely reverted lower following an upside surprise in May.

We expect CPI energy prices declined by 5.2% m-o-m in June, led by falling gasoline prices. This likely pushed down headline CPI inflation to -0.203% m-o-m.

Based on our forecast for CPI and PPI, June core PCE inflation likely moderated to 0.271% m-o-m in June (or 3.3% annualized) after a 0.320% advance in May.

While June core PCE inflation likely remained above an annual rate of 2%, we expect the anticipated negative headline inflation and upcoming methodological changes to PCE prices will keep the Fed patient on rate hikes at the July FOMC meeting.

PPI (Wednesday): Lower energy prices likely weighed on headline PPI inflation while "core" PPI which exclude volatile energy, food and trade services appears to have remained positive. It's important to monitor if manufactured goods prices reacted to the recent decline in commodity prices. Also, as the focus is shifting from tariffs/crude oil prices towards AI-induced price pressures, PPI's prices for electronic components including semiconductors are worth watching. Among PCE-relevant components, we expect PPI's portfolio management and investment advice prices continued to rise at a solid pace of $2.7\%$ m-o-m in June following a $4.9\%$ jump in May. We assume that PPI's domestic airline fares were down by $0.5\%$ m-o-m in June, while it's uncertain how this component reacted to the recent ups and downs in jet fuel prices.

Beige Book (Wednesday): The overall assessment on economic activity in the next Beige Book might be upgraded to reflect strong economic activity supported by the AI business investment. However, as was the case with the May Beige Book, the next Beige Book might highlight a deeper K-shaped bifurcation among households. In terms of prices, easing of price pressures due to lower commodity prices will likely be reported. Also, businesses might have reported that increased financial stress on middle-to-low income households made consumers more sensitive to price increases. Lastly, the May Beige Book mentioned “little to no change” in employment across eleven Districts, which was not consistent with the recent strength in nonfarm payrolls growth. We expect some upgrade to the assessment on employment growth in the Beige Book next week.

Retail sales (Thursday): We expect retail sales rose by 0.3% m-o-m in June following a 0.9% increase in May. The slowdown was primarily driven by a decline in sales at gasoline stations as real sales edged lower and gasoline prices fell in the month following the US-Iran ceasefire. However, excluding gasoline sales, consumption remained strong, supported by steady payroll income growth and higher tax refunds.

We expect nominal control retail sales rose by 0.6% m-o-m, driven by a pickup in online sales due to Amazon Prime Day and other competitive sales. Motor vehicle and parts sales growth also edged up as unit auto sales rebounded sharply in June.

NAHB Housing Market Index (Thursday): We expect the NAHB Housing Market Index picked up to 37 in July from 35 in June. Mortgage rates edged lower, and the US-Iran ceasefire was announced during the surv

[中间内容因长度限制已省略]

t of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Securities International, Inc., US. All rights reserved.
"""
