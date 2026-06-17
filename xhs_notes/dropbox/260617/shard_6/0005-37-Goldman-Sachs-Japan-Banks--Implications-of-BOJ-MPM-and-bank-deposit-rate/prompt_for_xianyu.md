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
# Japan Banks: Implications of BOJ MPM and bank deposit rate hike; continued upside for bank shares

BOJ hiked the policy rate from $0.75\%$ to $1.0\%$ at the June 15-16th MPM. In the policy statement and vice governor's press conference, BOJ communicated its view that the current financial conditions remain accommodative, and that it expects to continue to hike the policy rate while monitoring growth and inflation conditions.

Post-MPM, MUFG raised its ordinary deposit rate by +10bp from 0.30% to 0.40%, and hiked its short-term prime rate by +25bp from 2.125% to 2.375%, keeping ordinary deposit beta to policy rate at 40% as widely expected. SMFG and Mizuho followed with ordinary rate hikes to 0.40%. Aozora Bank hiked deposit rate by +25bp for deposits below Y1 million, same as after the previous rate hike, and SBI Shinsei Bank kept its deposit beta contained while announcing a campaign rate for Hyper Deposits. Yokohama Financial Group released new material on the BOJ rate hike impact on its FY3/28 net revenue (excluding securities investment related), showing a rate hike impact of FY3/28 Y14bn pre-tax / approximately Y10bn post-tax / ROE +0.7% rise, in addition to the previous disclosure of FY3/27 post-tax Y3bn impact.

We believe the implications to bank shares are as follows.

1) First, given the policy rate has been hiked to 1.0%, there is now a possibility that many banks with 0.75% policy rate assumptions for FY3/27 guidance may revise up. Also, banks may make progress on disclosing the positive profit impact of this BOJ rate hike to FY3/28 profits, as Yokohama FG has done.

2) With the continuation of policy rate hike cycle confirmed, market may now see higher likelihood that banks may meet or beat FY3/29 midterm plans where policy rate assumptions are 0.75-1.0%. The fact that deposit betas have been in line with expectations in deposit rate hikes disclosed so far also helps to raise likelihood of banks meeting plans.

3) Into this BOJ MPM, we think market positioning in bank stocks was relatively light given also the backdrop of Middle East uncertainty. We think this may be a similar pattern as the December 2025 rate hike, which was preceded by a period of tariff uncertainty. Going forward, we think bank shares my see re-rating or short-covering on awareness of underpricing of policy rate hikes by bank stocks, similar to what was seen after December 2025 policy rate hike. We believe that banks stocks P/B currently price in policy rate of about 0.75-1.0% based on banks' midterm plan ROE targets and cost of capital (link). Given the BOJ MPM signaled continuation of rate hike cycle, we think there is room to price in further rate normalization.

## Makoto Kuroda

+81(3)4587-9920

makoto.kuroda@gs.com

GS Japan Co., Ltd.

## Hibiki Takuma

+81(3)4587-4935

hibiki.takuma@gs.com

GS Japan Co., Ltd.

Exhibit 1: Coverage banks' guidance, policy rate assumption, and stated profit impact of policy rate hike

<table><tr><td colspan="2">(Unit: bn JPY)</td><td rowspan="2">FY26E Net Income Guidance</td><td rowspan="2">Assumption policy rate</td><td rowspan="2">Impact of +25bp Policy rate hike</td><td rowspan="2">Impact to Net Income(%)</td></tr><tr><td></td><td>Ticker</td></tr><tr><td>MUFG</td><td>8306.T</td><td>2,700</td><td>1.0% (FY26)</td><td>Full year impact +180bn</td><td>4.7%</td></tr><tr><td>SMFG</td><td>8316.T</td><td>1,700</td><td>0.75%</td><td>1st year impact: +110bn5th year impact: +150bn</td><td>4.5%~6.2%</td></tr><tr><td>Mizuho FG</td><td>8411.T</td><td>1,300</td><td>0.75%</td><td>Full year impact: +120bn</td><td>6.5%</td></tr><tr><td>SMTG</td><td>8309.T</td><td>380</td><td>0.75%</td><td>+10bp policy rate full year impact: +6bn</td><td>1.1%</td></tr><tr><td>Resona HD</td><td>8308.T</td><td>310</td><td>1.0% (27/1)</td><td>Full year impact +60bn</td><td>13.5%</td></tr><tr><td>Yokohama FG</td><td>7186.T</td><td>129</td><td>0.75%</td><td>Full year impact +14bn</td><td>7.6%</td></tr><tr><td>Chiba Bank</td><td>8331.T</td><td>107</td><td>0.75%</td><td>Full year net income impact+4-5bn (assuming June 26 hike)</td><td>3.7%-4.7%</td></tr><tr><td>Fukuoka FG</td><td>8354.T</td><td>100</td><td>0.75%</td><td>+4.5bn(FY26)/+13bn(FY27)(assuming June 26 hike)</td><td>3.2%(FY26)9.1%(FY27)</td></tr><tr><td>Japan Post Bank</td><td>7182.T</td><td>660</td><td>Forward rate</td><td></td><td></td></tr><tr><td>Aozora Bank</td><td>8304.T</td><td>27</td><td>+25bp(26/6-7)+25bp(27/1-3)</td><td>Full year impact: +3bn</td><td>7.8%</td></tr><tr><td>SBI Shinsei Bank</td><td>8303.T</td><td>n/a</td><td>two hikes in FY26</td><td>Full year impact: +16bn</td><td>n/a</td></tr><tr><td>Rakuten Bank</td><td>5838.T</td><td>81.3</td><td>0.75%</td><td>Full year impact: +14.5bn</td><td>12.5%</td></tr></table>

Rate hike impact is pre-tax unless otherwise noted, and % profit impact is vs FY26 guidance  
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 2: Banks' product rate hikes reflecting BOJ policy rate hike

<table><tr><td rowspan="2"></td><td rowspan="2">Deposit type</td><td colspan="3">Deposit rate</td><td rowspan="2">Effective date</td><td rowspan="2">Short-term prime rate</td><td rowspan="2">Effective date</td></tr><tr><td>Old</td><td>New</td><td>Change</td></tr><tr><td>MUFG</td><td>Ordinary</td><td>0.30%</td><td>0.40%</td><td>+10bp</td><td>8/3/2026</td><td>+25bp (2.125-&gt;2.375%)</td><td>8/3/2026</td></tr><tr><td>SMFG</td><td>Ordinary</td><td>0.30%</td><td>0.40%</td><td>+10bp</td><td>8/3/2026</td><td></td><td></td></tr><tr><td>Mizuho</td><td>Ordinary</td><td>0.30%</td><td>0.40%</td><td>+10bp</td><td>8/3/2026</td><td>+25bp (2.125-&gt;2.375%)</td><td>8/3/2026</td></tr><tr><td>SMTG</td><td>Ordinary</td><td>0.30%</td><td>0.40%</td><td>+10bp</td><td>8/3/2026</td><td></td><td></td></tr><tr><td rowspan="2">Aozora</td><td>Ordinary (BANK,0.75%1.00%+25bp7/1/2026</td><td></td><td>1.00%</td><td>+25bp</td><td>7/1/2026</td><td></td><td></td></tr><tr><td>Ordinary (BANK, Y1mln+)</td><td>0.50%</td><td>0.65%</td><td>+15bp</td><td>7/1/2026</td><td></td><td></td></tr><tr><td rowspan="3">SBI Shinsei</td><td>Ordinary</td><td>0.30%</td><td>0.40%</td><td>+10bp</td><td>7/10/2026</td><td></td><td></td></tr><tr><td>Ordinary (Diamond Stage)</td><td>0.40%</td><td>0.45%</td><td>+5bp</td><td>7/10/2026</td><td></td><td></td></tr><tr><td>Hyper deposit</td><td>0.50%</td><td>0.55%</td><td>+5bp</td><td>7/10/2026</td><td></td><td></td></tr></table>

Source: Company data

Exhibit 3: Topix banks' share price performance in 30 days before and after previous rate hikes  
![](images/e21eb2d5d238fa17022341cf072cc67453cbd2f615c39f6916ffe0f9f6a9801d.jpg)

<details>
<summary>line chart</summary>

| days | hike to 0.50% | hike to 0.75% |
| ---- | ------------- | ------------- |
| -30  | 0.99          | 0.90          |
| -28  | 0.99          | 0.91          |
| -26  | 0.99          | 0.92          |
| -24  | 0.98          | 0.93          |
| -22  | 0.97          | 0.94          |
| -20  | 0.96          | 0.95          |
| -18  | 0.97          | 0.96          |
| -16  | 0.98          | 0.97          |
| -14  | 0.99          | 0.98          |
| -12  | 1.00          | 0.99          |
| -10  | 1.01          | 1.00          |
| -8   | 1.00          | 1.01          |
| -6   | 1.01          | 1.02          |
| -4   | 1.02          | 1.03          |
| -2   | 1.01          | 1.04          |
| 0    | 1.00          | 1.05          |
| 2    | 1.01          | 1.06          |
| 4    | 1.02          | 1.07          |
| 6    | 1.03          | 1.08          |
| 8    | 1.04          | 1.09          |
| 10   | 1.05          | 1.10          |
| 12   | 1.06          | 1.12          |
| 14   | 1.07          | 1.15          |
| 16   | 1.08          | 1.18          |
| 18   | 1.07          | 1.16          |
| 20   | 1.06          | 1.14          |
| 22   | 1.05          | 1.13          |
| 24   | 1.04          | 1.12          |
| 26   | 1.03          | 1.14          |
| 28   | 1.02          | 1.16          |
| 30   | 1.01          | 1.20          |
</details>

Source: Data compiled by GS Global Investment Research, LSEG Data & Analytics

## Disclosure Appendix

## Reg AC

We, Makoto Kuroda and Hibiki Takuma, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Makoto Kuroda GS Japan Co., Ltd., Hibiki Takuma GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Distribution of ratings: See the distribution of ratings disclosure above. Price chart: See the price chart, with changes of ratings and price targets in prior periods, above, or, if electronic format or if with respect to multiple companies which are the subject of this report, on the GS website at https://www.gs.com/research/hedge.html.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or 

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
