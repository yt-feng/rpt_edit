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
U.S. Software

# The Q2 On-Cycle Earnings Guide – Too Early to Get Excited

We see Q2 earnings as a continuation of trends we saw in Q1. It is too early for the SaaS names (NOW, HUBS etc.) to show significant AI upside, which means there can't be a major reversal here yet. Infra names like DDOG will show ongoing momentum. We like MSFT here.

Raimo's Read on Q2: We expect another volatile earnings season in software. Overall spending trends are steady but there is the risk of a crowding-out effect, which was apparent by the recent IBM profit warning. However, that seemed more capex than opex related. The bigger issue is that we are still in the early innings on the AI monetization side for many of our names. This means the core issue for our space still exists – how do you prove AI success when overall numbers are not moving higher. We expect steady numbers for SaaS names like NOW or HUBS but that is likely not enough to change the sentiment on these names as the AI part is still too small to trigger major estimate increases. Investors want to see acceleration stories (see SNOW last quarter). Here, we think DDOG remains well-positioned as the growing AI momentum drives the need for more DDOG observability (and hence higher estimates). Microsoft could also show a small acceleration in Azure growth and might get revisited again. Lastly, we believe the payroll names have a good set-up.

MSFT – Small Acceleration and Low Expectations: We like MSFT for Q2 earnings. The name has not been in the spotlight for investors in recent quarters. We do not expect a major turnaround of this situation, but do acknowledge that Azure growth could show a small growth acceleration in the low 40% range (remember guidance is 39-40% YoY). Management will likely talk about the usage of its own LLMs, which shows the growing independence from the frontier model providers. Lastly, buy-side capex expectations seem to be in the \$250-270bn range already, which should limit negative surprises. In other words, there does not seem to be a strong catalyst, but solid numbers with a backdrop of very low expectations.

HCM/Payroll Software – Healthy Beat & Raise Potential Against Low Expectations: We see constructive set-ups for Paycom and Paylocity with muted sentiment for back-office HCM/ payroll peers pairing well with potential for solid beat & raise quarters. For PAYC, consensus is modeling \~7% recurring revenue ex-float growth and muted adj. EBITDA margin expansion, which leaves room for a modest 1-1.5% beat and a slight raise to FY26 total revenue and adj. EBITDA guidance. Paylocity also has a relatively undemanding set-up with consensus expecting growth to decelerate \~200bps to 9.6% y/y and Q2 adj. EBITDA to contract \~200bps y/y (\~135bps ex-float). Further, PCTY is reporting its fiscal Q4 2026 quarter where it is expected to give initial

U.S. Software
POSITIVE
Unchanged

U.S. Software
Raimo Lenschow, CFA
+1 212 526 2712
raimo.lenschow@BARC.com
BCI, US

Sheldon McMeans
+1 212 526 1544
sheldon.mcmeans@BARC.com
BCI, US

Eamon Coughlin
+1 212 526 6142
eamon.coughlin@BARC.com
BCI, US

Becky Sun
+1 212 526 0416
yuyao.sun@BARC.com
BCI, US

FY27 guidance, where we see bias for in-line to slight upside to consensus expectations that call for recurring revenue ex-float growth to decelerate to \~8% exiting FY27.

AI Infrastructure Peers - Best Set-up for DOCN Following Recent Underperformance, CRWV/WYFI More 2H Story: We see a more favorable sentiment backdrop for the AI infrastructure pure-play names entering Q2 after the space has seen pressure from elevated concerns on component costs, competition and customer concentration risk (CRWV -37%, DOCN -30%, WYFI -30% last month vs. IGV +5%). However, we see these risks skewed more towards large players in the space (e.g. CRWV, ORCL) and hence, see the recent weakness creating an attractive entry point for DOCN that positively pre-announced earlier this month that came with \~29% Q2 total revenue growth, +\$550mn in Q/Q RPO and increased FY27/FY28 capacity expansion expectations (see DigitalOcean: Positive Pre-Announcement Corroborates Capacity-Driven Acceleration Story, 7/7/26). For CRWV and WYFI, we see a better set-up in 2H26 as Q2 is expected to be the trough in terms of profitability and revenue growth for the two companies respectively, that are both seeing short-term noise from large capacity deployments that are coming online (see within for details).

Summary of Rating, Price Target, Model Changes 6
Recent Price Performance and Current Short Interest 7
Earnings Calendar 10
Valuation Table 11
Must See Charts For Q2 12
FX Fluctuations 12
Business & Employment Charts Indicate Improving Trends Exiting Q2 12
Developer Job Posts Highlight Positive Growth Trends Exiting Q2 14
Company Setups 16
Appian (UW/POS, PT \$23) – Conservative Expectations and Potential for Better Momentum to Continue Sentiment Rebound 16
Atlassian (OW/POS, PT \$112) – Expecting FY27 Guide to Be a Clearing Event Ahead of a Difficult Data Center Comp 18
CoreWeave (EW/POS, PT \$90) – Sentiment More Balanced but 2H Profitability Ramp May Be Needed to Drive Upside Amid Industry Overhang 20
Datadog (OW/POS, PT \$290) – AI and Core Momentum Should Continue to Power Acceleration Story 22
DigitalOcean (OW/POS, PT \$160) – Limited Surprises Post Pre-Announcement but More Balanced Sentiment Creates Entry Point 24
Dynatrace (OW/POS, PT \$48) – Stable Quarter, Though Likely Not Enough to Drive Share Inflection 25
HubSpot (OW/POS, PT \$270) – Core Growth Drivers Intact, Though Slow Start Potentially Limits Q2 Beat Upside, Q3 Guide 26
IBM (OW/POS, PT \$288) – Waiting for Answers 26
JFrog (OW/POS, PT \$88) – Expecting a Q2 Cloud Accel and Healthy FY26 Guidance Raise 28
Klaviyo (OW/POS, PT \$25) – Awaiting Growth Stabilization: Solid Execution May Not Be Enough to Shift Sentiment 29
Microsoft (OW/POS, PT \$545) – Small Acceleration Could Be Enough 30 monday.com (OW/POS, PT \$100) – AI Momentum Partially Offsetting Pricing Headwinds, but Growth Stabilization Remains the Key Debate 31

OpenText (EW/POS, PT \$27) – Too Early to Get Excited 32
Paycom (EW/POS, PT \$154) – Small Beat Against Low Expectations Could Continue Rebounding HCM/Payroll Sentiment 33
Paylocity (EW/POS, PT \$128) – Small Beat Potential and Limited Surprises for FY27 Guidance Create Opportunity for Small Sentiment Improvement 35
Pegasystems (OW/POS, PT \$48) – Steady Q2 and Expected 2H Ramp Creates Better Set-up in Q3/Q4 36
SAP (OW, \$255 PT) – Q2 Should Be Solid but Unlikely to Be a Turning Point for the Shares 36
ServiceNow (OW, PT \$134) - Q2 to Highlight AI Traction and Best-in-Class SaaS Metrics but More Excitement in 2H 38
Teradata (UW/POS, PT \$28) – Tough Comp Could See Q2 ARR Growth Below 2-4% FY26 Guidance Range, Likely Not Enough Given Uncertain Backdrop 40
WhiteFiber (EW, \$29 PT) - Focus on CapEx, Pipeline Build and NC-1 Progress to Determine Potential Binary Outcome 41
Company Snapshots 41
Appendix – Software Engineering Job Postings Methodology 53

Summary of our Ratings, Price Targets and Earnings Changes in this Report (all changes are shown in bold)

<table><tr><td></td><td colspan="2">Rating</td><td>Price</td><td colspan="3">Price Target</td><td colspan="3">EPS FY1 (E)</td><td colspan="3">EPS FY2 (E)</td></tr><tr><td>Company</td><td>Old</td><td>New</td><td>20-Jul-26</td><td>Old</td><td>New</td><td>%Chg</td><td>Old</td><td>New</td><td>%Chg</td><td>Old</td><td>New</td><td>%Chg</td></tr><tr><td>U.S. Software</td><td>Pos</td><td>Pos</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Atlassian (TEAM)</td><td>OW</td><td>OW</td><td>96.43</td><td>112.00</td><td>112.00</td><td>-</td><td>5.45</td><td>5.45</td><td>-</td><td>6.64</td><td>6.46</td><td>-3</td></tr><tr><td>CoreWeave, Inc (CRWV)</td><td>EW</td><td>EW</td><td>73.06</td><td>120.00</td><td>90.00</td><td>-25</td><td>-3.76</td><td>-4.13</td><td>-10</td><td>-3.70</td><td>-3.32</td><td>10</td></tr><tr><td>Datadog, Inc. (DDOG)</td><td>OW</td><td>OW</td><td>263.20</td><td>260.00</td><td>290.00</td><td>12</td><td>2.39</td><td>2.39</td><td>-</td><td>2.80</td><td>2.80</td><td>-</td></tr><tr><td>DigitalOcean (DOCN)</td><td>OW</td><td>OW</td><td>119.09</td><td>184.00</td><td>160.00</td><td>-13</td><td>1.32</td><td>1.44</td><td>9</td><td>1.18</td><td>1.02</td><td>-14</td></tr><tr><td>Dynatrace, Inc. (DT)</td><td>OW</td><td>OW</td><td>44.71</td><td>44.00</td><td>48.00</td><td>9</td><td>1.95</td><td>1.95</td><td>-</td><td>2.22</td><td>2.22</td><td>-</td></tr><tr><td>IBM Corp. (IBM)</td><td>OW</td><td>OW</td><td>213.00</td><td>350.00</td><td>288.00</td><td>-18</td><td>12.36</td><td>12.36</td><td>-</td><td>13.12</td><td>13.12</td><td>-</td></tr><tr><td>OpenText Corp. (OTEX)</td><td>EW</td><td>EW</td><td>23.33</td><td>27.00</td><td>27.00</td><td>-</td><td>4.19</td><td>4.18</td><td>-</td><td>4.42</td><td>4.40</td><td>-</td></tr><tr><td>Paycom (PAYC)</td><td>EW</td><td>EW</td><td>149.71</td><td>148.00</td><td>154.00</td><td>4</td><td>10.73</td><td>10.71</td><td>-</td><td>12.65</td><td>12.65</td><td>-</td></tr><tr><td>Paylocity Holding Corp (PCTY)</td><td>EW</td><td>EW</td><td>127.29</td><td>128.00</td><td>128.00</td><td>-</td><td>8.08</td><td>8.12</td><td>-</td><td>8.83</td><td>8.84</td><td>-</td></tr><tr><td>SAP SE (SAP)</td><td>OW</td><td>OW</td><td>158.35</td><td>257.00</td><td>255.00</td><td>-1</td><td>8.54</td><td>8.49</td><td>-1</td><td>10.11</td><td>10.01</td><td>-1</td></tr><tr><td>ServiceNow, Inc. (NOW)</td><td>OW</td><td>OW</td><td>104.70</td><td>134.00</td><td>134.00</td><td>-</td><td>4.01</td><td>4.01</td><td>-</td><td>5.02</td><td>5.02</td><td>-</td></tr><tr><td>WhiteFiber, Inc. (WYFI)</td><td>EW</td><td>EW</td><td>27.13</td><td>27.00</td><td>29.00</td><td>7</td><td>-0.74</td><td>-0.84</td><td>-14</td><td>-0.29</td><td>-0.33</td><td>-14</td></tr></table>

Source: BARC. Share prices and target prices are shown in the primary listing currency and EPS estimates are shown in the reporting currency. FY1(E): Current fiscal year estimates by BARC. FY2(E): Next fiscal year estimates by BARC. Stock Rating: OW: Overweight; EW: Equal Weight; UW: Underweight; RS: Rating Suspended Industry View: Pos: Positive; Neu: Neutral; Neg: Negative.

## Summary of Rating, Price Target, Model Changes

\- Atlassian: We maintain our Overweight rating and our PT of \$112. This valuation is now based on \~15x EV/CY27E FCF (unchanged) and CY27E FCF of \~\$2.1 bil (prior: \~\$2.12 bil). We updated some of our revenue estimates for TEAM (more below) to better reflect our expectations for its upcoming FY27 guide.

\- CoreWeave: We maintain our Equal Weight rating and lower our price target to \$90 (from \$120) based on 36x CY27E EV/CY27E adj. EBIT (from 43x) and CY27E adj. EBIT of \$3.61bn (unchanged). We lower our valuation multiple to reflect lower valuation levels for AI infrastructure peers.

\- Datadog: We maintain our Overweight rating, and raise our PT to \$290 (from \$260) to reflect our stronger expectations for DDOG's near-term growth algorithm. Our PT is now based on \~75x CY27E FCF (prior: \~67x CY27E FCF) on our CY27 FCF estimate of \~\$1,357mn (unchanged).

\- DigitalOcean: We maintain our Overweight rating and lower our PT to \$160 (from \$184) based on 36x CY30E EPS of \$6.20 discounted back to CY27E (implying \$4.66, from \$6.04 implying \$4.60)) to reflect lower peer group valuation levels. We updated our model slightly to better account for adj. EBITDA seasonality expectations in 2H26/1H27.

\- Dynatrace: We maintain our Overweight rating, and raise our price target to \$48 (from \$44) to reflect our slightly more optimistic expectations for FY27 upside. Our PT is based on \~20x CY27E EV/FCF (prior: \~18x CY27E EV/FCF), and our CY27E FCF estimate of \~\$677mn (unchanged).

\- IBM: We maintain our Overweight rating and lower our price target to \$288 (from \$350) based on 18x EV/CY27E uFCF (from 21x) and CY27E uFCF of \$18.4bn (unchanged). We lower our price target to account for IBM's weaker than expected pre-announcement and lower peer group valuation levels.

\- Paycom: We maintain our Equal Weight rating and raise our price target to \$154 (from \$148) based on 13x EV/CY27E adj. FCF and CY27E FCF of \$617mn (from \$610mn) and update our model primarily to better reflect our expectations for Q3/Q4 revenue and cash flow seasonality.

\- OpenText: We maintain our Equal Weight rating and our price target of \$27. This valuation is based on \~10x CY27 uFCF (unchanged) and FCF of \$1.20bn (from \$1.21bn). We updated our model slightly to better reflect our expectations for its upcoming FY27 guide.

\- ServiceNow: We maintain our Overweight rating and price target of \$134 based on 20x EV/ CY27E FCF of \$6.91bn (both unchanged). We update our model primarily to account for updated FX impacts.

\- WhiteFiber: We maintain our Equal Weight rating and raise our price target to \$29 (from \$27) based on 15x (from 14x) CY29E adj. EPS of \$2.56 discounted back to CY27E (implying \$1.97). We update our model to better account for our expectations of the NC-1 capacity ramp and raise our multiple slightly to account for higher peer group valuation levels for AI infrastructure names relative to our last model update.

## Recent Price Performance and Current Short Interest

FIGURE 1. Month-to-Date Price Performance  
![](images/e9ff78f8fc0964bfcc2421099c4a3b77d68ae21854ff1c593391ada474177f45.jpg)  
Prices as of 7/20/2026
Source: Bloomberg, BARC

FIGURE 2. Year to Date Price Performance  
![](images/6a6f39ecb5caa8589768d8b8795edd0dbca7b7af8401ad6e1ed4a3c9e3de19cf.jpg)  
Source: Bloomberg, BARC  
Prices as of 7/20/2026

FIGURE 3. WYFI / PEGA / KVYO short interest has increased the most since April 15. Most companies saw an increase in short interest in the last 3 months, though SPT / PAYC short interest decreased by greater than 200bps.

<table><tr><td colspan="4">Short Interest % of Float</td></tr><tr><td>Company</td><td>7/15/2026</td><td>4/15/2026</td><td>BPS Change</td></tr><tr><td>SPT</td><td>9.4%</td><td>11.6%</td><td>-218bps</td></tr><tr><td>PAYC</td><td>9.5%</td><td>11.6%</td><td>-214bps</td></tr><tr><td>DOCN</td><td>13.7%</td><td>15.3%</td><td>-159bps</td></tr><tr><td>OTEX</td><td>5.1%</td><td>5.9%</td><td>-77bps</td></tr><tr><td>SMWB</td><td>1.3%</td><td>1.6%</td><td>-22bps</td></tr><tr><td>MSFT</td><td>1.2%</td><td>1.1%</td><td>8bps</td></tr><tr><td>DT</td><td>3.6%</td><td>3.3%</td><td>28bps</td></tr><tr><td>DDOG</td><td>4.5%</td><td>3.9%</td><td>59bps</td></tr><tr><td>CMRC</td><td>9.7%</td><td>9.0%</td><td>63bps</td></tr><tr><td>PCTY</td><td>6.4%</td><td>5.6%</td><td>88bps</td></tr><tr><td>APPN</td><td>16.9%</td><td>15.5%</td><td>131bps</td></tr><tr><td>IBM</td><td>3.7%</td><td>2.4%</td><td>131bps</td></tr><tr><td>GTM</td><td>19.8%</td><td>17.6%</td><td>222bps</td></tr><tr><td>NOW</td><td>6.0%</td><td>3.8%</td><td>227bps</td></tr><tr><td>CRWV</td><td>21.5%</td><td>18.8%</td><td>268bps</td></tr><tr><td>TEAM</td><td>10.8%</td><td>8.0%</td><td>275bps</td></tr><tr><td>FIVN</td><td>11.7%</td><td>8.6%</td><td>311bps</td></tr><tr><td>TDC</td><td>18.3%</td><td>14.4%</td><td>392bps</td></tr><tr><td>FROG</td><td>10.2%</td><td>5.8%</td><td>434bps</td></tr><tr><td>HUBS</td><td>12.4%</td><td>7.1%</td><td>525bps</td></tr><tr><td>MNDY</td><td>20.2%</td><td>14.8%</td><td>539bps</td></tr><tr><td>KVYO</td><td>16.6%</td><td>8.9%</td><td>765bps</td></tr><tr><td>PEGA</td><td>18.1%</td><td>9.2%</td><td>885bps</td></tr><tr><td>WYFI</td><td>36.2%</td><td>23.7%</td><td>1249bps</td></tr><tr><td>Median</td><td>10.5%</td><td>8.8%</td><td>177bps</td></tr></table>

Source: Bloomberg

FIGURE 4. Median short interest for our on-cycle coverage increased \~180bps since April 15

<table><tr><td colspan="3">Short Interest % of Float</td><

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
