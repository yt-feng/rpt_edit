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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Bernstein`。标题格式建议：`# Bernstein：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Software, US and China Internet, & US Communications Infrastructure Cloud in the Quarter: How did the hyperscalers do in 1Q26?

![](images/5b7b89fe83063324d0ff041239d58ffd5b0a6ff11c0a7e724fa102c37cf9eddd.jpg)

![](images/9151f91c456e56345547e631ce9f84304d14990721e70358c0f53fa8235f6048.jpg)

![](images/3683141398a81249dfb2e0db1c48a91734f840d2b9039f4b6235f7003343832d.jpg)

![](images/313ed065b2481a2c3df73e6806eaae81f5bf8decd032f2e47280b00273ff4958.jpg)

![](images/559d7f15ab681f45ce41cf6c1ef1d8b28aaaad8aa689785966028ccbd727fa31.jpg)

![](images/1e23f61c0129995554bb5a8f3702228771b27cf0779aab99ac0193c518fec0b2.jpg)

![](images/1de7aba99e3ec554a8a9feba045e2cb67051c370d6b58d8baf5b7194bf23a216.jpg)

![](images/513b0733fe979af8106d31f3d484ae84777fe8cdb675e910feb3714b8975e321.jpg)

![](images/99b221c87edebb156e9611543677754ffe58055b915fa1a07f61d7a04e1744d4.jpg)

![](images/60f69066355aa90a4bc49a45317c5ad72cff5dee8726da1388bb53a19ce7c319.jpg)

Mark L. Moerdler, Ph.D.
+1 917 344 8506
mark.moerdler@bernsteinsg.com

Mark Shmulik
+1 917 344 8508
mark.shmulik@bernsteinsg.com

Robin Zhu
+852 2123 2659
robin.zhu@bernsteinsg.com

Madison Rezaei
+1 917 344 8622
madison.rezaei@bernsteinsg.com

Firoz Valliji, CFA
+1 917 344 8316
firoz.valliji@bernsteinsg.com

Shelly Tang, CFA
+1 917 344 8342
shelly.tang@bernsteinsg.com

Deeksha Pandey
+1 917 344 8447
deeksha.pandey@bernsteinsg.com

Wenhuan Chang
+1 917 344 8546
wenhuan.chang@bernsteinsg.com

Charles Gou
+852 2123 2618
charles.gou@bernsteinsg.com

Nancy Wu
+1 917 344 8545
nancy.wu@bernsteinsg.com

The hyperscale market has become a picks & shovels basket to support the Generative AI wave even though it was predominantly a CPU driven business. Investors remain concerned about the CAPEX growth and the associated margins / returns of AI infrastructure investment as AI becomes a more meaningful contributor to revenues. Suddenly, the laggard in hyperscale appears the leader in AI cloud with Google's vertically integrated solution now neck-and-neck with Microsoft for incremental cloud dollars added Q/Q.

Even with CAPEX stepping up, CSPs all point to capacity constraints, before it was GPU availability, but that seems to have shifted to physical powered up datacenter capacity. All this ushers in a slew of new investor questions: Are Microsoft and Amazon going to see a return on CAPEX? Is speed and cost to bring capacity online the new basis of competition? Do the model wars determine winners and losers? What are the economics of Oracle's AI build-out, and can they rely on their OpenAI commitments? Are NVIDIA and OpenAI losers to Google or kingmakers? When will AI drive increased cloud IT budgets? Bernstein's Cloud in the Quarter note, which focuses on the largest hyperscale Cloud providers, should help investors get a better picture of the secular issues and why results may differ between providers. This quarter we added another perspective and neocloud data.

The hyperscale market is the largest tangible market opportunity in Software / Cloud / Internet (\$1.3-1.5T — see Diving into the Cloud TAM) and possibly the largest in all of tech. Bernstein's Global Hyperscale Cloud Team (Global Software, U.S. Internet, and China Internet and now US Comm. Infrastructure) supplies this quarterly note to help pull all the data together in one place for Amazon, Microsoft, Google, Alibaba Oracle and now a neocloud - CoreWeave.

Updating our data through this quarter, today's note looks at the metrics each of the companies supply as well as our estimates through Q1 CY2026. The note also supplies our updated thoughts on the different companies' hyperscale businesses, where we are on AI, and how the markets and companies are progressing on what we believe is going to be a very long and valuable journey. This is the 21 $^{st}$ note in our series comparing and contrasting the hyperscale vendors. This many years of historical perspective should help investors better understand the trends and the opportunities.

To further help understand the long-term opportunities, we've published notes diving into the historical trends in IaaS and PaaS in the U.S. and globally. We give our thoughts on the progression of the industry (see Link). We would also call attention to our notes that looks at the capital intensity of IaaS/PaaS based on our proprietary work on capital intensity at Azure and AWS — What does it really cost to offer IaaS / PaaS? as well as the impact of AI driven CAPEX in Why Azure CAPEX will slow and revenue accelerate, Microsoft Azure AI margins, Oracle: The story is better than we thought

On the Generative AI opportunity we have published numerous notes including: Can GPU intensive AI compute be a profitable business for hyperscalers?, Generative AI 101 Primer, Gen AI 201 — Inferencing, Generative AI 301 — Reasoning models, Generative AI 401: Agents, AI Infrastructure: The build-out is huge. Bonanza or bubble?, Shifting from Training to Inferencing impact on datacenters and 5 Takeaways on datacenter build-out.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">18 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>GOOGL (Alphabet)</td><td>M</td><td>USD</td><td>368.03</td><td>390.00</td><td>86.7%</td><td>USD</td><td>10.81</td><td>14.47</td><td>14.32</td><td>34.1</td><td>25.4</td><td>25.7</td></tr><tr><td>AMZN (Amazon)</td><td>O</td><td>USD</td><td>244.39</td><td>315.00</td><td>(10.7)%</td><td>USD</td><td>7.17</td><td>8.78</td><td>11.12</td><td>34.1</td><td>27.8</td><td>22.0</td></tr><tr><td>MSFT (Microsoft)</td><td>O</td><td>USD</td><td>379.40</td><td>646.00</td><td>(46.7)%</td><td>USD</td><td>13.64</td><td>16.85</td><td>19.16</td><td>27.8</td><td>22.5</td><td>19.8</td></tr><tr><td>ORCL (Oracle)</td><td>O</td><td>USD</td><td>184.29</td><td>325.00</td><td>(38.3)%</td><td>USD</td><td>7.63</td><td>8.57</td><td>12.86</td><td>24.2</td><td>21.5</td><td>14.3</td></tr><tr><td>BABA (Alibaba )</td><td>O</td><td>USD</td><td>107.10</td><td>180.00</td><td>(31.3)%</td><td>CNY</td><td>65.41</td><td>26.82</td><td>46.57</td><td>11.1</td><td>27.0</td><td>15.6</td></tr><tr><td>9988.HK (Alibaba)</td><td>O</td><td>HKD</td><td>104.90</td><td>176.00</td><td>(53.1)%</td><td>HKD</td><td>8.82</td><td>3.69</td><td>6.68</td><td>10.3</td><td>24.6</td><td>13.6</td></tr><tr><td>700.HK (Tencent)</td><td>O</td><td>HKD</td><td>440.20</td><td>780.00</td><td>(58.6)%</td><td>CNY</td><td>28.09</td><td>30.00</td><td>34.91</td><td>13.5</td><td>12.7</td><td>10.9</td></tr><tr><td>CRWV (CoreWeave)</td><td>U</td><td>USD</td><td>117.95</td><td>67.00</td><td>(56.3)%</td><td>USD</td><td>(1.20)</td><td>(4.20)</td><td>(2.41)</td><td>39.9</td><td>15.6</td><td>8.3</td></tr><tr><td>SPX</td><td></td><td></td><td>7,500.58</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,048.07</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
GOOGL, AMZN estimate is Reported EPS; GOOGL, AMZN valuation is Reported P/E (x); CRWV valuation is EV/EBITDA (x); ORCL base year is 2026; Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Microsoft (MSFT, TP \$646, Outperform): Microsoft made a big bet on Azure, investing aggressively in a global footprint and technology innovation. Starting in \~CY2019 they doubled down on their existing AI investment as they prepared for and added Gen AI capabilities, built AI datacenters and invested in their own chips. With AI ARR reaching \$37B last quarter, AI has become a meaningful contributor to top line growth and not a headwind. We also believe Microsoft is strongly positioned in the case of an AI bubble because their first-party usage of capacity is ramping thanks to their diversified app base, along with third-party contracts which comes from not only OpenAI but a diversified large enterprise customer base, and contract duration is well aligned with useful life of the equipment. While most of software is slowing, Azure is stable and will, we believe, accelerate supporting Microsoft's strong double-digit revenue growth and GAAP margins in the mid 40s. We like the setup and see the current valuation as an attractive entry point. In addition, we are now starting to see substantial seat growth at Office 365 Copilot and usage at GitHub which both show that AI will over time drive not just GPU be increased CPU usage.

Oracle (ORCL, TP \$325, Outperform): The Oracle story has shifted quickly from a potential Cloud and hyperscaler story to a major hyperscaler and AI training / inferencing provider. Oracle has \$638B in Remaining Performance Obligations (RPO) and exceptional OCI growth (\$166B in OCI revenue guidance for FY30), driven by multiple multi-billion dollar deals led by \~\$300B in RPO from OpenAI. Based on the work we have done on understanding the value of this transition (Oracle: The story is better than we thought, with better upside potential), we believe it would be highly value accretive. While near term this might impact margins and cash, it will likely drive very substantial earnings and FCF growth over the next 5–10 years. The stock has taken a beating over the last 9+ months due to various concerns, but we see the overhangs getting gradually clearer as Oracle is securing its most, if not all the financing it will need for current demand by the end of FY27, sentiment around OpenAI continues to improve, and OCI growth demonstrates strong execution as seen this past quarter.

Amazon (AMZN, TP \$315, Outperform): In light of the tightening compute supply environment marked by rising BOM costs, Amazon continues to demonstrate why it has earned its reputation as the leading infrastructure player and is expected to lead hyperscalers in getting compute online with BOM advantages. AI revenue is tracking in the right direction, supported by a renewed appreciation of data gravity as enterprises increasingly choose to run AI workloads where their data already resides. The chips business is a key highlight, with Trainium seeing \~\$225B in revenue commitments and Graviton advantages coming into sharper focus amid constrained CPU supply. Core non-AI workloads should continue their strength into Q2 although more recently, it seems like hyperscalers are running into capacity constraints with incremental compute heavily allocated toward frontier AI labs (see our latest SSO tracker/work). While operating margins may fluctuate as AI workloads scale, they are expected to remain healthy in the low to mid 30% range, supported by continued efficiency gains and disciplined cost control.

Google (GOOGL, TP \$390, Market-Perform): Google Cloud's outlook remains particularly strong, anchored by exceptional backlog growth and emerging new growth vectors (such as third-party TPU sales). Backlog nearly doubled Q/Q to \~\$462B with over 50% expected to convert to revenue over the next 24 months, providing a solid foundation for continued growth. Importantly, the inclusion of third party TPU hardware sales introduces a potentially meaningful incremental driver, as Google begins supplying its custom AI chips directly into customer data centers. While revenue from these deals is expected to be back end loaded in 2026 and more material in 2027, they significantly enhance long term revenue visibility and strategic positioning. Combined with strong ongoing momentum in AI workloads and core GCP, this positions Google Cloud for durable, multi year growth. Margins have also inflected sharply, reaching \~33% in 1Q26 (vs \~30% in 4Q25 and \~17.8% in 1Q25), though this remains an area to watch with headwinds from higher depreciation and a low single digit impact from the Wiz acquisition in 2026, even as Google focuses on efficiency gains to help offset these pressures.

Alibaba (BABA, TP US\$180/HK\$176, Outperform): Alicloud's revenue growth accelerated to 38.2% year-on-year in the March 2026 quarter, while the adjusted EBITA margin improved slightly to 9.1% from 9.0% in the previous quarter. AI-related cloud products continued to deliver triple-digit growth for the eleventh consecutive quarter, accounting for 30% of external cloud revenues. Management indicated that external revenue growth is expected to continue accelerating beyond 40% in the coming quarters, with adjusted EBITA margins projected to reach low-teens levels. MaaS revenue was guided to triple from RMB9bn in the March quarter to RMB30bn by the end of FY3/27E.

Coreweave (CRWV, TP \$67, Underperform): While CRWV has shown impressive growth, successfully standing up a neocloud to monetize its power assets, it is much smaller than any of the other cloud providers listed here. We do not believe the company has a structural advantage of right to win in the cloud market (GPUs or otherwise), and in fact believe it is at a disadvantage to hyperscalers over the long-term. While we believe the company may sign more deals in the next \~12 months, on a long-term fundamental basis, we have concerns about the viability of the business model and CRWV's role in the infrastructure ecosystem. We are Underperform with a price target of \$67.

## DETAILS

The hyperscaler story has changed significantly over the last 2 years as AI has become the big driver of sentiment. The biggest debate to date, arguably, is how long can this build-out continue, and when will we have the proof of ROI?.

Over the past few years, we have seen massive CAPEX ramp (Exhibit 1), and that race does not seem to stop: cash CAPEX across the 4 hyperscalers reached roughly \$130B in 1Q26, and with the guidances these companies have given, Bernstein is modeling \$623B cash Capex across the 4 hyperscalers for 2026 (plus Meta it would be close to \$760B). Meanwhile, we estimate cash flow from operations across the 4 this year to be around the same level at \$635B, ignoring buybacks and dividends. Assuming CAPEX will continue to grow strongly in 2027 and CFO growth lags as it has been (Exhibit 5), this implies that most, if not all (Microsoft still has a little more room), of the hypersclaers needs funding from the capital markets for their buildout next year (and certainly in 2028 if the game continues). Recently we have seen these fundraising activities from Amazon, Google and Oracle.

On the other hand, investors in not only the cloud providers but also infrastructure names are looking for signs to prove or disprove the sustainability and rationality of this investment cycle. Depending on the metric they look at, the message is so far mixed. In terms of revenue, while growth began to accelerate in the last few quarters (Exhibit 2) it is still early to justify the ROI on all these investments - revenue growth needs to accelerate more in the upcoming quarters. For those that focus on backlog, recently, we have witnessed a significant pickup in backlog growth (Exhibit 3), which is an encouraging sign. Although this ignores certain confounding factors like contract duration and high customer concentration. For those that are more bearish on the build out, an earnings-like metric such as CFO growth (Exhibit 4) would fit their narrative as it is bouncing around and has yet to see a definitive strong acceleration.

To put a broader perspective, especially on the conversation of CAPEX / Cloud capacity we have added our recently launched US Communications Infrastructure team lead by Madison Rezaei to this series. We recommend you read their work which focuses on data center capacity and the neoclouds.

Finally, at the same time as investors are worried about an AI bubble, they are also concerned on whether AI is going to eat enterprise software. With the quantity, level and frequency of information flow in the space, who is an AI winner and who is a loser is changing quite frequently across tech and this can be seen even across the hyperscalers.

EXHIBIT 1: Hyperscaler Capex has grown significantly and is expected to continue to grow

Hyperscaler quarterly capex (\$B)  
![](images/b46734c7bce87385b7220d24365fdab8e4d8a521962256bda646e6cb46bd756c.jpg)  
Based on calendar quarters (Calendar Q1 = Microsoft and Oracle FQ3). Forward estimates based on Bernstein estimates
Source: Company disclosures, Bernstein analysis and estimates

EXHIBIT 2: While cloud revenue growth has accelerated in the recent quarters, it needs to continue accelerating to keep up with the pace of capex growth

Quarterly Cloud Revenue: AWS+Azure+GCP+OCI  
![](images/51643e5861545a9f77de14766387417f5fa19a67f85b074208e0990cdf64d683.jpg)  
Based on calendar quarters (Calendar Q1 = Microsoft and Oracle FQ3). Azure revenue based on Bernstein estimates
Source: Company disclosures, Bernstein analysis and estimates

EXHIBIT 3: On the other hand, ignoring contract duration, total backlog (RPO) growth has accelerated significantly across all hypersclaers in recent quarters, totaling \$2T as of 1Q26

![](images/ed256313689118973b3ceb8b40295b78c1f408cdffc69932433a086ce8e8bf7b.jpg)  
Based on calendar quarters (Calendar Q1 = Microsoft and Oracle FQ3). Source: Company disclosures, Bernstein analysis

EXHIBIT 4: So, which tale would you rather believe?  
Y/Y Growth%: Revenue vs. Capex vs. CFO vs. Backlog  
![](images/a1c4378fa3d899f63e5a8759641e1e80b85aabf59343a2fa469bd827e146ac28.jpg)  
Source: Company disclosures, Bernstein analysis and estimates

EXHIBIT 5: Meanwhile, as hyperscalers are running out of internal funding, to increase Capex further they likely need to (and have been) raise capital, through either debt or equity

Hyperscaler Cash Flow vs. Capex, CY 26E  
![](images/b1b9390556e45c34e218ddbdad1f6dd0e243cd68d52ddb63cd15295689dde0ad.jpg)

Based on calendar quarters (Calendar Q1 = Microsoft and Oracle FQ3). Forward estimates based on Bernstein estimates
Source: Company disclosures, Bernstein analysis and estimates

## DETAILS FROM LAST QUARTER'S RESULTS

Azure grew 39% in CC (40% reported) in 3FQ26, beating guidance of 37-38% CC. Management is guiding to 39-40% CC growth for next quarter, as well as “modest acceleration” in 2H CY26 as compared to first half. Management continues to take the long view in a supply constrained world, prioritizing 1st party applications and R&D while balancing strong customer demand for Azure. AI ARR, which includes Azure AI and SaaS Copilot revenues, surpassed \

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
