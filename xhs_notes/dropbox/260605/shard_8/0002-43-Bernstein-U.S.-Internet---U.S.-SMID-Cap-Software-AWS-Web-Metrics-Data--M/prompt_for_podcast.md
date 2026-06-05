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
# U.S. Internet & U.S. SMID-Cap Software

# AWS Web Metrics Data: Mid-Q2'26 caution signal emerging?

![](images/8c6d51abf7bc820cec5a4603c9dba437000ab50388ee6a799e35a1820ee86332.jpg)

Mark Shmulik

+1 917 344 8508

mark.shmulik@bernsteinsg.com

![](images/a70e31f06807b983102b3b17bdc2829bd6e2ce5f5b116c1b2a684ef670fb51e5.jpg)

Peter Weed

+1 917 344 8390

peter.weed@bernsteinsg.com

![](images/4b78a5cefe22f89854e343adcf9753354816373db0a9165dd77061f6bebb4be7.jpg)

Luwei Yang

+1 917 344 8342

luwei.yang@bernsteinsg.com

![](images/4984759129675f21ad1b130b0df801f1b50646b94c09afc4e93495d271e3e5e9.jpg)

Deeksha Pandey

+1 917 344 8447

deeksha.pandey@bernsteinsg.com

![](images/f12a4c89f82abc5584e454b0e67449c2d79cf7b22dbba904afc32a847bca6d4e.jpg)

Wenhuan Chang

+1 917 344 8546

wenhuan.chang@bernsteinsg.com

![](images/b9d77292dcc59b1d56640d2dfa1f2a00e574594d9fe6e09884fdb59cf41cce14.jpg)

Armin Hadavi, CFA

+1 917 344 8463

armin.hadavi@bernsteinsg.com

Our regular web metric updates over the last few quarters showed exceptionally strong demand signals — arguably the strongest since COVID. The strength has translated into reported results, with revenue growth acceleration in AWS as AI workloads slowly ramped, and cloud consumption linked names like Datadog, Snowflake, and Cloudflare. That said, we want to flag a trend that we are watching closely: growth flattened unusually over the last four weeks (+ start of this week) relative to the pattern seen over the prior three years (Exhibit 2). Reminder: this is alt data with good historic fit, but for a variety of reasons it could stop being predictive. Fundamental explanation remains important.

Limited Q2 revenue impact expected. It is important to remember that our data effectively operates on a one-quarter lead relative to reported financials. What we are measuring is closer to incremental ARR added in the quarter, whereas reported results reflect postpaid billing and revenue recognition from existing ARR. As a result, Q2 revenue should largely reflect the strength we saw in Q1 web metric signal (Exhibit 1) — we think Q2 could show another 100 bps acceleration.

Q3 non-AI revenue impact likely limited. Q2 started strong, so if the recent implied weakness reverses in June, Q3 would still have a “normal” Q/Q growth. Note there may be a modest mathematical Y/Y headwind to non-AI growth as Q3'25 was strong.

Q4 could be an issue. Where the setup becomes more challenging is if the current flattening persists into Q3 web metric data. If the trend remains subdued, the result would be a pronounced Y/Y growth headwind to non-AI consumption in Q4.

What's driving the softness. We asked leaders of top software companies, large growth software PE portfolios, as well as consultants working with enterprise buyers and the common thesis we heard: hyperscalers are running into capacity constraints with incremental compute heavily allocated toward frontier AI labs, leaving less available supply for other buyers (e.g., enterprises, software vendors). More narrowly, from a very deeply integrated source within product team buyers a couple added thesis emerged: 1) Mythos induced cyber urgency creates a HUGE backlog of issues to address. Companies are sprinting to do this, as opposed to working on next incremental new workload. 2) tokenmaxxing hangover as some product teams attempt to moderate spending growth on coding agents and AI copilots. After a period of rapid adoption, there is some effort to reset and impose discipline.

Regardless of the driver, the shift is notable and raises a warning signal that we will keep watching. A softer consumption backdrop in Q3+ could impact demand from traditional enterprise buyers and cloud software vendors, while less problematic for the "Born-in-AI" cohort (i.e., AI-linked trajectory for AWS and Datadog).

Could AWS benefit? In practice, supply constraints point to a more competitive environment for securing capacity to bring new workloads into production, which could give AWS pricing leverage. Similarly, if available capacity has shifted towards higher margin AI workloads, then AWS may also find its financials in a better position.

BERNSTEIN TICKER TABLE 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">4 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>ClosingPrice</td><td>PriceTarget</td><td>TargetPerf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>AMZN (Amazon)</td><td>O</td><td>USD</td><td>253.79</td><td>315.00</td><td>(4.6)%</td><td>USD</td><td>7.17</td><td>8.78</td><td>11.12</td><td>35.4</td><td>28.9</td><td>22.8</td></tr><tr><td>DDOG (Datadog)</td><td>O</td><td>USD</td><td>243.60</td><td>180.00</td><td>76.5%</td><td>USD</td><td>2.05</td><td>2.66</td><td>3.24</td><td>118.6</td><td>91.6</td><td>75.2</td></tr><tr><td>TWLO (Twilio)</td><td>M</td><td>USD</td><td>236.64</td><td>183.00</td><td>70.4%</td><td>USD</td><td>4.89</td><td>5.88</td><td>6.89</td><td>48.3</td><td>40.2</td><td>34.3</td></tr><tr><td>NET (Cloudflare)</td><td>M</td><td>USD</td><td>268.64</td><td>136.00</td><td>30.2%</td><td>USD</td><td>0.92</td><td>1.33</td><td>1.73</td><td>290.5</td><td>202.6</td><td>155.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,584.31</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended   
AMZN estimate is Reported EPS; AMZN valuation is Reported P/E (x);   
Source: Bloomberg, Bernstein estimates and analysis.

# INVESTMENT IMPLICATIONS

No change to models, price targets, or recommendations.

Amazon: we maintain our Outperform rating and \$315 PT.

Datadog: we maintain our Outperform rating and \$180 PT.

Twilio: we maintain our Market-Perform rating and \$183 PT.

Cloudflare: we maintain our Market-Perform rating and \$136 PT.

# DETAILS

EXHIBIT 1: 2026 had a strong start with the AWS web metric data accelerating in January and maintaining the strong level throughout Q1.   
![](images/47898738fb73393309d0760b63abc13fdc0209b85d74adaaecc3ff7aa5daed5f.jpg)

<details>
<summary>line</summary>

| Week | 2023 | 2024 | 2025 | 2026 |
|------|------|------|------|------|
| Jan  | 10%  | -5%  | 0%   | -5%  |
| Jan  | 10%  | -5%  | 0%   | 2%   |
| Jan  | 10%  | -5%  | 0%   | 5%   |
| Jan  | 10%  | -5%  | 3%   | 7%   |
| Jan  | 10%  | -5%  | 3%   | 8%   |
| Jan  | 9%   | -5%  | 3%   | 8%   |
| Feb  | 6%   | 7%   | 10%  | 14%  |
| Feb  | 6%   | 3%   | 8%   | 11%  |
| Feb  | 4%   | 5%   | 9%   | 7%   |
| Feb  | 5%   | 12%  | 9%   | 12%  |
| Mar  | 7%   | 12%  | 10%  | 11%  |
| Mar  | 3%   | 5%   | 9%   | 9%   |
| Mar  | 7%   | -4%  | 7%   | 14%  |
</details>

Source: Similarweb, Bernstein analysis

EXHIBIT 2: The strong acceleration continued in early Q2 with the web metric data performing better than the prior 3 years until the first week of May. But the trend flatlined in May, underperforming the trends we saw in 2023 and 2024.   
![](images/a3045593202ade790032e3810af68b229eaf23fa1e16c12753f08d0801818abe.jpg)

<details>
<summary>line</summary>

| Period | 2023 | 2024 | 2025 | 2026 |
|--------|------|------|------|------|
| 1st week: Apr | -18% | -5% | -7% | -2% |
| 2nd week: Apr | -5% | -3% | -4% | 0% |
| 3rd week: Apr | 5% | -2% | -8% | 7% |
| 4th week: Apr | 4% | -1% | -9% | 6% |
| 1st week: May | -10% | -8% | -11% | 0% |
| 2nd week: May | 3% | -4% | -7% | 0% |
| 3rd week: May | 6% | 1% | -3% | 1% |
| 4th week: May | 5% | 4% | -1% | 0% |
| 5th week: May | 4% | -3% | -5% | -15% |
| 1st week: June | 8% | 9% | 1% | 13% |
| 2nd week: June | 14% | 13% | 5% | 13% |
</details>

Source: Similarweb, Bernstein analysis

# WHY DO WE CARE ABOUT AWS WEB METRICS DATA

# SSO DATA SERVES AS A LEADING INDICATOR FOR AWS EX-AI REVENUE

As we have shared over the past few years, we have observed a strong correlation between -1 quarter (last quarter) engagement with AWS' single-sign-on ("SSO") page and current quarter revenue growth for AWS. This makes sense as the amount of human interaction with the SSO can't really oscillate that much due to personal work preference, and instead it more likely represents the portion of people actually tasked with doing projects on AWS. And because the amount of work any individual person can do (and is expected to deliver) remains pretty consistent over time, and their work turns into similar amount of revenue (with some curvature created by issues such as changing list prices and productivity, that can be adjusted for), then the volume of people will translate through the SSO volume into consumption volumes.

However, that level of human work comes before the revenue is observed. Why does this make sense? Their work turns into consumption, which gets more fully realized in the following period (between the ramp-up of their projects and usage, and timing within the quarter not providing full-quarter usage). Our data is available daily, so we've tested a variety of time-shifts, and find the highest correlation is \~1 quarter. Thus, the level of human engagement with the SSO last quarter is a leading indicator of revenue recognition changes in the current quarter.

But the engagement levels alone still have variation to fit. Over time, AWS changes its rate cards, offers credits, sees rationalization (that changes consumption per person), and even has sales behaviors that can pull forward some level of revenue. We try to adjust for these variations and look at the regression only for the “base” AWS revenue.

# REMINDER: ALT DATA MAY DISCONNECT FOR A VARIETY OF REASONS, EVEN WITH GOOD HISTORIC FIT.

We have seen the data gyrate for short periods of time in the past. We had not brought up this deviation until now, given this reality. But at 4+ weeks of weakness it seems more likely a trend. With that said many things could go wrong on this readthrough. For instance the vendor itself has even occasionally changed their collection methodology creating weirdness during a transition period. We are most interested when a fundamental explanation supports the data. We are continuing to gather data points that could refute (or further confirm) if the trend readthrough makes sense and is predictive of future financial results.

# Past notes:

22 April 2026 - AWS Web Metrics Data: End of Q1'26 update, early Q2 view   
18 Feb 2026 - AWS Web Metrics Data: Early-Feb'26 Update   
20 Jan 2026 - AWS Web Metrics Data: Hint into the Print - Mid-Jan'26 Update   
19 Nov 2025 - AWS Web Metrics Data: Hint into the Print - Mid-Nov'25 Update   
29 Oct 2025 - AWS Web Metrics Data: Hint into the Print - Oct '25 Update   
8 Oct 2025 - Datadog (DDOG): Strong H2 cloud consumption trends   
24 Jul 2025 - Datadog (DDOG): Q2 cloud consumption + AI momentum   
10 Feb 2025 - AWS & Datadog: Just how 'lumpy' could 1Q25 be?   
12 Jul 2024 - Amazon Web Services (AWS) & Datadog (DDOG): 2Q24 Web Metrics Update   
15 Apr 2024 - Amazon Web Services (AWS) & Datadog (DDOG): 1Q24 web metrics update   
23 Jan 2024 - Amazon Web Services (AWS) & Datadog (DDOG): 4Q23 web metrics update   
11 Oct 2023 - AWS + DDOG Q3'23 preview: Confusing signals hide positive direction   
21 Jul 2023 - US Internet & Software: AWS + DDOG setup to rebound in H2?   
14 Apr 2023 - US Internet & Software: Wagging the Dog, updating AWS and Datadog estimates

# APPENDIX - FINANCIAL FORECASTS

EXHIBIT 3: Our AMZN Model   
in millions except per share and percentage data 

<table><tr><td>AMZN</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>FY2024</td><td>FY2025</td><td>FY2026E</td><td>FY2027E</td><td>FY2028E</td></tr><tr><td colspan="14">GAAP INCOME STATEMENT</td></tr><tr><td>Revenue</td><td>155,667</td><td>167,702</td><td>180,169</td><td>213,386</td><td>181,519</td><td>197,983</td><td>210,110</td><td>248,241</td><td>637,959</td><td>716,924</td><td>837,854</td><td>960,215</td><td>1,089,239</td></tr><tr><td>Cost of Revenue</td><td>76,976</td><td>80,809</td><td>88,670</td><td>109,959</td><td>87,463</td><td>94,799</td><td>99,118</td><td>121,490</td><td>326,288</td><td>356,414</td><td>402,870</td><td>429,806</td><td>456,123</td></tr><tr><td>Fulfillment</td><td>24,593</td><td>25,976</td><td>27,679</td><td>30,826</td><td>27,289</td><td>29,742</td><td>31,683</td><td>36,340</td><td>98,505</td><td>109,074</td><td>125,054</td><td>139,883</td><td>151,905</td></tr><tr><td>Marketing</td><td>9,763</td><td>11,416</td><td>11,686</td><td>14,264</td><td>10,314</td><td>12,869</td><td>13,867</td><td>16,880</td><td>43,907</td><td>47,129</td><td>53,931</td><td>63,466</td><td>72,979</td></tr><tr><td>Technology and Content</td><td>22,994</td><td>27,166</td><td>28,962</td><td>29,399</td><td>29,567</td><td>32,271</td><td>34,668</td><td>40,960</td><td>88,544</td><td>108,521</td><td>137,466</td><td>160,689</td><td>185,171</td></tr><tr><td>General and administrative</td><td>2,628</td><td>2,965</td><td>2,875</td><td>2,704</td><td>2,587</td><td>3,366</td><td>3,152</td><td>3,724</td><td>11,359</td><td>11,172</td><td>12,828</td><td>14,102</td><td>15,505</td></tr><tr><td>Other</td><td>308</td><td>199</td><td>2,875</td><td>1,257</td><td>447</td><td>792</td><td>840</td><td>993</td><td>763</td><td>4,639</td><td>3,072</td><td>3,841</td><td>4,357</td></tr><tr><td>Total Expenses</td><td>137,262</td><td>148,531</td><td>162,747</td><td>188,409</td><td>157,667</td><td>173,839</td><td>183,328</td><td>220,387</td><td>569,366</td><td>636,949</td><td>735,221</td><td>811,787</td><td>886,040</td></tr><tr><td>EBIT</td><td>18,405</td><td>19,171</td><td>17,422</td><td>24,977</td><td>23,852</td><td>24,145</td><td>26,782</td><td>27,855</td><td>68,593</td><td>79,975</td><td>102,633</td><td>148,428</td><td>203,199</td></tr><tr><td>D&amp;A</td><td>14,262</td><td>15,227</td><td>16,796</td><td>19,471</td><td>18,945</td><td>20,788</td><td>22,062</td><td>27,307</td><td>52,795</td><td>65,756</td><td>89,101</td><td>115,604</td><td>144,586</td></tr><tr><td>EBITDA (incl. SBC)</td><td>32,667</td><td>34,398</td><td>34,218</td><td>44,448</td><td>42,797</td><td>44,933</td><td>48,843</td><td>55,161</td><td>121,388</td><td>145,731</td><td>191,734</td><td>264,032</td><td>347,784</td></tr><tr><td>Other Expenses (Benefits)</td><td>1,278</td><td>1,007</td><td>(3,765)</td><td>3,785</td><td>(6,403)</td><td>4,010</td><td>4,472</td><td>4,641</td><td>9,345</td><td>2,305</td><td>6,720</td><td>25,221</td><td>34,997</td></tr><tr><td>Net Income</td><td>17,127</td><td>18,164</td><td>21,187</td><td>21,192</td><td>30,255</td><td>20,135</td><td>22,310</td><td>23,214</td><td>59,248</td><td>77,670</td><td>95,913</td><td>123,207</td><td>168,201</td></tr><tr><td>Weight Avg. Diluted Shares</td><td>10,793</td><td>10,806</td><td>10,845</td><td>10,863</td><td>10,874</td><td>10,910</td><td>10,946</td><td>10,981</td><td>10,721</td><td>10,827</td><td>10,928</td><td>11,071</td><td>11,217</td></tr><tr><td>GAAP EPS</td><td>1.59</td><td>1.68</td><td>1.95</td><td>1.95</td><td>2.78</td><td>1.85</td><td>2.04</td><td>2.11</td><td>5.52</td><td>7.17</td><td>8.78</td><td>11.12</td><td>14.99</td></tr><tr><td colspan="14">GAAP Margins:</td></tr><tr><td>Gross Margin</td><td>51%</td><td>52%</td><td>51%</td><td>48%</td><td>52%</td><td>52%</td><td>53%</td><td>51%</td><td>49%</td><td>50%</td><td>52%</td><td>55%</td><td>58%</td></tr><tr><td>EBIT Margin</td><td>12%</td><td>11%</td><td>10%</td><td>12%</td><td>13%</td><td>12%</td><td>13%</td><td>11%</td><td>11%</td><td>11%</td><td>12%</td><td>15%</td><td>0%</td></tr><tr><td>EBITDA Margin</td><td>21%</td><td>21%</td><td>19%</td><td>21%</td><td>24%</td><td>23%</td><td>23%</td><td>22%</td><td>19%</td><td>20%</td><td>23%</td><td>27%</td><td>0%</td></tr><tr><td colspan="14">Y/Y Growth (GAAP):</td></tr><tr><td>Revenue</td><td>9%</td><td>13%</td><td>13%</td><td>14%</td><td>17%</td><td>18%</td><td>17%</td><td>16%</td><td>11%</td><td>12%</td><td>17%</td><td>15%</td><td>13%</td></tr><tr><td>EBIT</td><td>20%</td><td>31%</td><td>0%</td><td>18%</td><td>30%</td><td>26%</td><td>54%</td><td>12%</td><td>86%</td><td>17%</td><td>28%</td><td>45%</td><td>37%</td></tr><tr><td>EPS</td><td>62%</td><td>33%</td><td>37%</td><td>5%</td><td>75%</td><td>10%</td><td>4%</td><td>8%</td><td>91%</td><td>30%</td><td>22%</td><td>27%</td><td>35%</td></tr><tr><td colspan="14">NON-GAAP METRICS</td></tr><tr><td>Adjusted EBITDA</td><td>36,356</td><td>40,932</td><td>39,065</td><td>48,845</td><td>46,829</td><td>52,654</td><td>54,502</td><td>60,281</td><td>143,399</td><td>165,198</td><td>214,266</td><td>289,852</td><td>377,112</td></tr><tr><td>Adjusted EBITDA Margin</td><td>23%</td><td>24%</td><td>22%</td><td>23%</td><td>26%</td><td>27%</td><td>26%</td><td>24%</td><td>22%</td><td>23%</td><td>26%</td><td>30%</td><td>35%</td></tr><tr><td>Adjusted EPS (ex Rivian)</td><td>1.59</td><td>1.68</td><td>1.95</td><td>1.95</td><td>2.78</td><td>1.85</td><td>2.04</td><td>2.11</td><td>5.52</td><td>7.17</td><td>8.78</td><td>11.12</td><td>14.99</td></tr><tr><td>Adjusted EPS growth</td><td>62%</td><td>33%</td><td>37%</td><td>5%</td><td>75%</td><td>10%</td><td>4%</td><td>8%</td><td>89%</td><td>30%</td><td>22%</td><td>27%</td><td>35%</td></tr><tr><td colspan="14">KEY METRICS</td></tr><tr><td>eCommerce GMV (Est.)</td><td>182,825</td><td>198,595</td><td>214,331</td><td>267,703</td><td>209,775</td><td>224,412</td><td>243,265</td><td>302,505</td><td>769,594</td><td>863,454</td><td>979,957</td><td>1,077,953</td><td>1,164,189</td></tr><tr><td>GMV Growth (Y/Y)</td><td>8%</td><td>13%</td><td>13%</td><td>14%</td><td>15%</td><td>13%</td><td>14%</td><td>13%</td><td>10%</td><td>12%</td><td>13%</td><td>10%</td><td>8%</td></tr><tr><td>Retail Revenue (Est.)</td><td>111,167</td><td>119,636</td><td>128,045</td><td>154,781</td><td>125,044</td><td>136,530</td><td>143,149</td><td>172,870</td><td>468,764</td><td>513,629</td><td>577,594</td><td>625,642</td><td>670,855</td></tr><tr><td>Retail Growth (Y/Y)</td><td>6%</td><td>11%</td><td>11%</td><td>10%</td><td>12%</td><td>14%</td><td>12%</td><td>12%</td><td>8%</td><td>10%</td><td>12%</td><td>8%</td><td>7%</td></tr><tr><td>AWS Revenue (Reported)</td><td>29,267</td><td>30,873</td><td>33,006</td><td>35,579</td><td>37,587</td><td>40,444</td><td>43,898</td><td>48,032</td><td>107,556</td><td>128,725</td><td>169,960</td><td>229,446</td><td>298,280</td></tr><tr><td>AWS Growth (Y/Y)</td><td>17%</td><td>17%</td><td>20%</td><td>24%</td><td>28%</td><td>31%</td><td>33%</td><td>35%</td><td>19%</td><td>20%</td><td>32%</td><td>35%</td><td>30%</td></tr><tr><td>Advertising Revenue (Est.)</td><td>13,921</td><td>15,

[中间内容因长度限制已省略]

nce system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
