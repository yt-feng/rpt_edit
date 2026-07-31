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
## Amazon.com

# AWS Set to Accelerate Further into 40%+ Growth

## Key Takeaways

The updated disclosure of \$25B in AI ARR for AWS alongside \$496B in backlog - both suggest that demand from enterprises for Bedrock and core are both accelerating. We had anticipated the backlog to step up by \$100B given the previously-announced Anthropic agreement, but it grew by an incremental \$51B QOQ. This sets the stage for what should be \~39% YOY growth for AWS into 2H26 and what should be above 40% growth next year as OpenAI starts to use Trainium chips in early-2027. Adjusting for a \$600M energy cost benefit, AWS operating margins were flat QOQ at 38% - we note that investors have been hesitant to underwrite prospects of stable or increasing margins given rising mix of AI compute workloads. We contend that in view of the revenue dollar growth for AWS into 2027, Amazon has to figure out a way to increase SG&A expenses at 3x the speed of recent years to keep margins down. This in our view points the way to continued segment margin expansion into 2027. We expect the Street to continue to close the gap to our estimates on both revenue and operating profit and eventually re-rate AMZN shares higher - we reiterate our Buy rating as the stock at current levels is showing at 19x our 2027E GAAP EPS and does not deserve to trade below the market multiple, in our view. Our price target increases to \$318 from \$305.

## Upside Case

Bulls may argue: 1) AWS acceleration to 37% vs 28% in 1Q26 and 17% in 2Q25 alongside margin expansion over the same periods driven by core and AI services, 2) incremental backlog of \$496B likely as the \$100B from its Anthropic deal arrived in the quarter, 3) AWS chips business exceeded \$25B in annualized revenue vs \$20B disclosed in 1Q26, 4) across the board reported beat on revenue and OI with notable uplift from AWS and North American retail as Int'l came approx. in line with consensus, and 5) AWS AI revenue ARR more than doubled QOQ from \$10B to \$25B in 2Q26.

## Downside Case

Bears could counter: 1) Net income included \~\$53.4B gain from its Anthropic investment but excluding the benefit, reported results would have come in under the Street, 2) revised CapEx guide in FY26 to \$220B driven by higher memory costs, 3) lower-than-anticipated 3Q26 revenue guide likely due to US Prime Day shift into June vs typical July, and 4) shipping cost growth of 19% outpacing units sold at 17% likely due to investments into faster delivery alongside higher shipping costs.

## Valuation:

We revise our price target to \$318 (from \$305) as we derive our valuation based on a P/FCF and apply a 30x multiple (unchanged) on our 3Q27-2Q28 estimate of \$116.3 billion.

## Equities

<table><tr><td>Americas</td></tr><tr><td>Internet Services</td></tr></table>

12-month rating Buy

12m price target US\$318.00

Prior : US\$305.00

Price (30 Jul 2026) US\$258.12

RIC: AMZN.O BBG: AMZN US  
Trading data and key metrics

<table><tr><td>52-wk range</td><td>US$274.99-198.79</td></tr><tr><td>Market cap.</td><td>US$2,710b</td></tr><tr><td>Shares o/s</td><td>10,500m (COM)</td></tr><tr><td>Free float</td><td>80%</td></tr><tr><td>Avg. daily volume (&#x27;000)</td><td>49,013</td></tr><tr><td>Avg. daily value (m)</td><td>US$12,224.6</td></tr><tr><td>Common s/h equity (12/26E)</td><td>US$550b</td></tr><tr><td>P/BV (12/26E)</td><td>5.1x</td></tr><tr><td>Net debt to EBITDA (12/26E)</td><td>1.2x</td></tr></table>

EPS (UBS, diluted) (USD)

<table><tr><td rowspan="2"></td><td colspan="4">12/26E</td></tr><tr><td>From</td><td>To</td><td>% ch</td><td>Cons.</td></tr><tr><td>Q1</td><td>3.20</td><td>3.20</td><td>0</td><td>2.78</td></tr><tr><td>Q2</td><td>2.34</td><td>6.31</td><td>170</td><td>1.82</td></tr><tr><td>Q3E</td><td>2.47</td><td>2.33</td><td>-6</td><td>1.90</td></tr><tr><td>Q4E</td><td>3.03</td><td>3.05</td><td>1</td><td>2.39</td></tr><tr><td>12/26E</td><td>11.03</td><td>14.88</td><td>35</td><td>8.83</td></tr><tr><td>12/27E</td><td>17.09</td><td>17.08</td><td>-0</td><td>10.06</td></tr><tr><td>12/28E</td><td>25.36</td><td>25.58</td><td>1</td><td>13.06</td></tr></table>

Stephen Ju
Analyst
stephen.ju@ubs.com
+1-212-882 5192

Vanessa Fong
Associate Analyst
vanessa.fong@ubs.com
+1-212-882 0079

<table><tr><td>Highlights (US$m)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>Revenues</td><td>574,785</td><td>637,959</td><td>716,924</td><td>824,858</td><td>969,524</td><td>1,167,881</td><td>1,390,306</td><td>1,624,433</td></tr><tr><td>EBIT (UBS)</td><td>60,875</td><td>90,604</td><td>99,442</td><td>128,755</td><td>217,824</td><td>326,936</td><td>447,198</td><td>566,612</td></tr><tr><td>Net earnings (UBS)</td><td>55,227</td><td>82,123</td><td>102,330</td><td>162,356</td><td>187,928</td><td>283,751</td><td>392,737</td><td>503,545</td></tr><tr><td>EPS (UBS, diluted) (US$)</td><td>5.26</td><td>7.66</td><td>9.45</td><td>14.88</td><td>17.08</td><td>25.58</td><td>35.09</td><td>44.57</td></tr><tr><td>DPS (net) (US$)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Net (debt) / cash</td><td>(135,611)</td><td>(130,900)</td><td>(152,987)</td><td>(253,097)</td><td>(255,719)</td><td>(256,227)</td><td>(264,787)</td><td>(267,541)</td></tr></table>

<table><tr><td>Profitability/valuation</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>EBIT (UBS) margin %</td><td>10.6</td><td>14.2</td><td>13.9</td><td>15.6</td><td>22.5</td><td>28.0</td><td>32.2</td><td>34.9</td></tr><tr><td>ROIC (EBIT) %</td><td>19.5</td><td>24.0</td><td>20.3</td><td>18.8</td><td>24.0</td><td>28.0</td><td>29.2</td><td>28.1</td></tr><tr><td>EV/EBITDA (UBS core) x</td><td>12.6</td><td>14.2</td><td>14.4</td><td>13.7</td><td>9.0</td><td>6.3</td><td>4.8</td><td>3.8</td></tr><tr><td>P/E (UBS, diluted) x</td><td>23.1</td><td>24.1</td><td>23.0</td><td>17.4</td><td>15.1</td><td>10.1</td><td>7.4</td><td>5.8</td></tr><tr><td>Equity FCF (UBS) yield %</td><td>3.0</td><td>2.0</td><td>0.6</td><td>0.2</td><td>2.2</td><td>6.5</td><td>7.6</td><td>13.1</td></tr><tr><td>Dividend yield (net) %</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Source: Company accounts, LSEG Eikon, UBS estimates. Metrics marked as (UBS) have had analyst adjustments applied. Valuations: based on an average share price that year, (E): based on a share price of US\$ 258.12 on 30-Jul-2026

This report has been prepared by UBS LLC. ANALYST CERTIFICATION AND REQUIRED DISCLOSURES, INCLUDING INFORMATION ON THE QUANTITATIVE RESEARCH REVIEW PUBLISHED BY UBS, BEGIN ON PAGE 12.

## Investment Case: AWS Set to Accelerate Further into 40%+ Growth

Amazon reported 2Q26 results with revenue of \$200.6 billion vs UBSe \$196.2 billion and the Street \$196.8 billion. Operating income came in at \$27.5 billion vs UBSe of \$24.2 billion and the Street at \$23.8 billion including \~\$1.2 billion one-time benefit. Our 2026 estimates for revenue and operating income are now \$824.9 billion and \$108.8 billion respectively vs \$830.7 billion and \$107.0 billion prior. We maintain our Buy rating and revise our price target to \$318 from \$305.

Despite the revision to its CapEx guide for 2026 from \$200 billion to \$220 billion, driven largely by rising supply chain costs, we believe that investors are more than willing to justify the incremental \$20 billion spend given the outsized AWS growth in the quarter. AWS came in 37% year over year vs UBSe 32% and the Street 31% while we believe investors were anticipating \~36%. Otherwise the significant step up in Performance Obligations of \$496 billion in the quarter was likely well contemplated as it now includes the \$100 billion from Anthropic - we were forecasting \$478 billion. Hence as we recalibrate our backlog and revenue estimates, our AWS growth rates rise to 38.9% and 36.1% in 3Q26 and FY26 respectively vs 35.8% and 33.3% prior. And even as our estimates remain well ahead of consensus, we believe that the Street will continue to catch up with us.

Management offered 3Q26 revenue guide of \$197 billion to \$202 billion (+9%-12% YOY) vs the Street \$203.9 billion (+14.9%) and UBSe \$207.0 billion (+13.2%) and excluding the impact of Prime Day in 2025 and 2026, growth would be \~400bps higher. Furthermore it anticipates unfavorable currency impact of \~80bps. Operating income guide of \$22.5 billion to \$26.5 billion implies margins of 11.4%-13.1% vs our pre-print expectations of \$25.6 billion / 12.4% and the Street at \$25.4 billion / 12.4%.

As our usual practice, we update the figure below for Amazon's latest disclosures around unit and shipping cost growth which we have for some time viewed as a proxy for margin improvements within its e-commerce business. Even as cost growth of 19% outpaced units growth of 17% in the quarter (the first time that the metrics have inflected since the pandemic) we believe that the more important takeaway is that the latter grew sequentially by 2pts which indicates to us that customer demand remains strong and continues to grow off a significantly larger base. Otherwise the higher cost growth is being driven elevated fuel prices alongside Amazon's ongoing investment into its e-commerce segment including scaling One / Same day delivery, 2) expansion of Amazon Now, its 30-min or less delivery service particularly into its international markets, and 3) higher volume of essentials / groceries / pharmacy which implies regularity / repeat purchases.

Figure 1: Amazon.com, Inc. - Unit Growth vs Shipping Cost Growth (1Q18-2Q26)  
![](images/deb60e8b82b77d16d1ba75744f9b066217a24a7a743c8b289b4e5314b6d225c7.jpg)  
Source: UBS, Company data

Reported net sales of \$200.6 billion vs guidance range of \$194 billion to \$199 billion (+16%-19% YOY) came in above the Street \$196.8 billion and UBSe \$196.2 billion alongside the upper end of its outlook. Operating income of \$27.5 billion also delivered a beat vs UBSe \$24.2 billion and the Street at \$23.8 billion vs \$20 billion to \$24 billion guide implying margins of 10%-12% - this includes \~\$1.2B benefit from tariff related refunds and change in fair value of energy contracts towards Amazon's North America and AWS segment respectively. AWS came in at +37% growth year over year and above the Street +31% and our pre-print estimate of +32%. North America retail grew \$116.2 billion and above our estimate of \$111.9 billion and the Street at \$113.8 billion driven by US Prime Day pull forward into June from its regular July timing. CapEx came in at \$54.2 billion and in-line with our expectations but above the Street at \$52.6 billion.

Given the AWS beat and higher than anticipated backlog number in the quarter, we revisit both accordingly and as such as our revenue estimates move up in 3Q26 and beyond. We also recalibrate our CapEx assumptions but our FY26 forecast is essentially unchanged with modest revisions in FY27 and FY28. Otherwise we recalibrate down our GMV and e-commerce estimates given the shift of dollars into 2Q26 / June Prime Day that would typically be recognized in 3Q26 / July. We also revise down our advertising revenue forecast given the modest miss in the quarter.

We maintain our Buy rating and move our price target to \$318 (from \$305) as the company continues to execute along our thesis centered around the following drivers:

\- Prospects for faster gross merchandise (GMV) growth and share gains (across its 1P wholesale and 3P merchant) on a higher level of service (faster delivery) amidst its ongoing fulfilment regionalization efforts in the US and eventual global roll-out.

\- Ongoing margin expansion in its e-commerce franchise due to improving economics - most easily illustrated with faster units relative to shipping cost growth.

\- New high-margin revenue stream from Prime Video with ads - although still in its early innings should become a more meaningful contributor over time.

\- All incremental CapEx and OpEx related to AWS, e-commerce, sports licensing deals, and Amazon Leo are already in our projections beginning in 2025 with minimal revenue upside from these investments incorporated into our model.

## Changes to Estimates

Changes to our 3Q26, 2026, 2027, and 2028 financial and operating estimates are as summarized below:

Figure 2: Amazon.com, Inc. - Summary Changes to UBS Estimates

<table><tr><td>$M unless otherwise stated</td><td>3Q26Prior</td><td>3Q26Current</td><td>% Δ</td><td>2026Prior</td><td>2026Current</td><td>% Δ</td><td>2027Prior</td><td>2027Current</td><td>% Δ</td><td>2028Prior</td><td>2028Current</td><td>% Δ</td></tr><tr><td>Physical Stores</td><td>5876.6</td><td>5876.6</td><td>0.0%</td><td>23724.6</td><td>23624.0</td><td>-0.4%</td><td>24281.8</td><td>24281.8</td><td>0.0%</td><td>24122.3</td><td>24122.3</td><td>0.0%</td></tr><tr><td>Online Stores</td><td>69751.1</td><td>66404.2</td><td>-4.8%</td><td>288459.0</td><td>286099.9</td><td>-0.8%</td><td>310421.9</td><td>301238.9</td><td>-3.0%</td><td>339100.4</td><td>327160.1</td><td>-3.5%</td></tr><tr><td>Retail Third-Party Seller Services</td><td>48893.2</td><td>45455.9</td><td>-7.0%</td><td>199318.0</td><td>193956.3</td><td>-2.7%</td><td>224902.1</td><td>219508.7</td><td>-2.4%</td><td>257374.8</td><td>251244.7</td><td>-2.4%</td></tr><tr><td>Retail Subscription Services</td><td>13940.5</td><td>13940.5</td><td>0.0%</td><td>55475.4</td><td>55439.3</td><td>-0.1%</td><td>61538.1</td><td>61494.7</td><td>-0.1%</td><td>68212.8</td><td>68160.7</td><td>-0.1%</td></tr><tr><td>AWS</td><td>44815.1</td><td>45859.0</td><td>2.3%</td><td>171534.5</td><td>175200.0</td><td>2.1%</td><td>254155.9</td><td>258845.0</td><td>1.8%</td><td>369355.9</td><td>377739.5</td><td>2.3%</td></tr><tr><td>Other</td><td>23703.1</td><td>22566.0</td><td>-4.8%</td><td>92209.9</td><td>90538.7</td><td>-1.8%</td><td>106907.0</td><td>104154.9</td><td>-2.6%</td><td>122721.5</td><td>119453.9</td><td>-2.7%</td></tr><tr><td>Net Revenue</td><td>206979.6</td><td>200102.2</td><td>-3.3%</td><td>830721.5</td><td>824858.2</td><td>-0.7%</td><td>982206.9</td><td>969524.0</td><td>-1.3%</td><td>1180887.7</td><td>1167881.1</td><td>-1.1%</td></tr><tr><td>Cost of Sales</td><td>98883.3</td><td>94620.4</td><td>-4.3%</td><td>404180.6</td><td>397893.5</td><td>-1.6%</td><td>413037.4</td><td>403628.9</td><td>-2.3%</td><td>444657.9</td><td>432738.9</td><td>-2.7%</td></tr><tr><td>Gross Profit</td><td>108096.3</td><td>105481.9</td><td>-2.4%</td><td>426540.8</td><td>426964.6</td><td>0.1%</td><td>569169.5</td><td>565895.1</td><td>-0.6%</td><td>736229.8</td><td>735142.2</td><td>-0.1%</td></tr><tr><td>Operating Income</td><td>25615.9</td><td>23951.0</td><td>-6.5%</td><td>107001.2</td><td>108829.7</td><td>1.7%</td><td>197640.9</td><td>196381.7</td><td>-0.6%</td><td>302606.0</td><td>303559.5</td><td>0.3%</td></tr><tr><td>GAAP Net Income (Loss)</td><td>21504.7</td><td>20173.5</td><td>-6.2%</td><td>100148.3</td><td>141421.8</td><td>41.2%</td><td>166130.4</td><td>165507.1</td><td>-0.4%</td><td>257434.8</td><td>259395.1</td><td>0.8%</td></tr><tr><td>GAAP Diluted EPS</td><td>$1.97</td><td>$1.85</td><td>-6.3%</td><td>$9.18</td><td>$12.96</td><td>41.1%</td><td>$15.12</td><td>$15.04</td><td>-0.5%</td><td>$23.25</td><td>$23.39</td><td>0.6%</td></tr><tr><td>Adjusted Diluted EPS</td><td>$2.47</td><td>$2.33</td><td>-5.7%</td><td>$11.03</td><td>$14.88</td><td>34.8%</td><td>$17.09</td><td>$17.08</td><td>-0.1%</td><td>$25.36</td><td>$25.58</td><td>0.9%</td></tr><tr><td>Adjusted EBITDA</td><td>52303.2</td><td>50630.2</td><td>-3.2%</td><td>210102.0</td><td>212960.7</td><td>1.4%</td><td>328366.3</td><td>329330.6</td><td>0.3%</td><td>463274.4</td><td>467823.7</td><td>1.0%</td></tr><tr><td>Capital Expenditures</td><td>59525.9</td><td>58708.1</td><td>-1.4%</td><td>221240.9</td><td>221241.7</td><td>0.0%</td><td>264711.0</td><td>264882.1</td><td>0.1%</td><td>292660.6</td><td>293858.5</td><td>0.4%</td></tr><tr><td>Unlevered Free Cash Flow</td><td>(2956.7)</td><td>439.7</td><td>114.9%</td><td>12561.8</td><td>533.2</td><td>-95.8%</td><td>61813.5</td><td>62336.8</td><td>0.8%</td><td>170925.5</td><td>173578.0</td><td>1.6%</td></tr></table>

Source: UBS estimates

## 2Q26 Reported Results

Reported net sales of \$200.6 billion was higher than our estimate of \$196.2 billion and the Street at \$196.8 billion. Management was guiding towards \$194.0 billion to \$199.0 billion.

Figure 3: Amazon.com, Inc. - Financial Results vs UBS Estimates

<table><tr><td>$M unless otherwise stated</td><td>2Q26E</td><td>2Q26A</td><td>% Δ</td><td>Analysis</td></tr><tr><td>Amazon Consolidated Revenue</td><td>196245.1</td><td>200606.0</td><td>2.2%</td><td>AWS and 1P beat vs UBSe and the Street</td></tr><tr><td>Cost of Sales</td><td>94892.4</td><td>95778.0</td><td>0.9%</td><td>Higher shipping costs</td></tr><tr><td>Gross Profit</td><td>101352.7</td><td>104828.0</td><td>3.4%</td><td></td></tr><tr><td>Fulfillment</td><td>28687.9</td><td>29633.0</td><td>3.3%</td><td>Driven by elevated demand for Prime Day in the US and other major markets</td></tr><tr><td>Marketing</td><td>11929.5</td><td>11698.0</td><td>-1.9%</td><td></td></tr><tr><td>Technology and Content</td><td>33549.6</td><td>33158.0</td><td>-1.2%</td><td></td></tr><tr><td>General Administrative</td><td>2824.8</td><td>2788.0</td><td>-1.3%</td><td></td></tr><tr><td>Other Operating Expense (Income), Net</td><td>199.0</td><td>90.0</td><td>-54.8%</td><td></td></tr><tr><td>Total Operating Expenses</td><td>77190.9</td><td>77367.0</td><td>0.2%</td><td></td></tr><tr><td>Income From Operations</td><td>24161.7</td><td>27461.0</td><td>13.7%</td><td>Versus consensus $23.8B and guidance $20.0B-$24.0B</td></tr><tr><td>Interest Income</td><td>1135.0</td><td>1295.0</td><td>14.1%</td><td></td></tr><tr><td>Interest Expense</td><td>1335.1</td><td>1314.0</td><td>-1.6%</td><td></td></tr><tr><td>Other Income (Expense), Net</td><td>0.0</td><td>53415.0</td><td>NM</td><td>$53.4B gain mark to market for Anthropic stake</td></tr><tr><td>Total Non-Operating Income (Expense), Net</td><td>(200.1)</td><td>53396.0</td><td>26781.3%</td><td>~$1.2B from tariff related refunds and energy contracts</td></tr><tr><td>Pretax Income</td><td>23961.6</td><td>80857.0</td><td>237.4%</td><td></td></tr><tr><td>Income Tax</td><td>3594.2</td><td>18199.0</td><td>406.3%</td><td></td></tr><tr><td>Equity-Method Investment Activity, Net of Tax</td><td>0.0</td><td>11.0</td><td>NM</td><td></td></tr><tr><td>Net Income (Loss)</td><td>20367.4</td><td>62647.0</td><td>207.6%</td><td></td></tr><tr>

[中间内容因长度限制已省略]

 Republic of Türkiye are allowed to purchase or sell the financial instruments traded in financial markets outside of the Republic of Türkiye. Further to this, pursuant to article 9 of the Communiqué on Principles Regarding Investment Services, Activities and Ancillary Services No. III-37.1, investment services provided abroad to residents of the Republic of Türkiye based on their own initiative are not restricted. United Arab Emirates (UAE) / DIFC / Abu Dhabi: UBS is not licensed in the UAE by the Central Bank of the UAE nor by the Emirates' Securities and Commodities Authority and does not undertake banking activities in the UAE. This document is provided for your information only and does not constitute financial advice. DIFC: UBS AG Dubai Branch is regulated by the DFSA in the DIFC. This material is strictly intended for Professional Clients and/or Market Counterparties only as classified under the DFSA rulebook. It should not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
