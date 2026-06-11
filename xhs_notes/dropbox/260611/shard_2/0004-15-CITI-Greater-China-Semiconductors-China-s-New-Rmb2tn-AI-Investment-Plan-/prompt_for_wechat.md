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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Citi`。标题格式建议：`# Citi：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
09 Jun 2026 09:01:07 ET | 10 pages

# Greater China Semiconductors

## China's New Rmb2tn AI Investment Plan Positive for Domestic AI Supply Chain

## CITI'S TAKE

Bloomberg reported on June $9^{\text{th}}$ that China is preparing to invest Rmb2tn (US\$295bn) over the next 5 years on data centers/networks to support its domestic AI sector. Chinese telcos will operate the data centers using at least 80% local AI accelerators. We view the new initiative as positive to: 1) foundries SMIC, Hua Hong (both covered by Laura Chen); 2) OSATs JCET, Tongfu, 3) equipment suppliers ASMPT, Vital Deeptech; and 4) AI accelerator vendors; given a clearer roadmap ahead for China's AI localization. The 80%+ AI chip localization target should be achievable as domestic AI chip vendors have effectively captured the commanding majority of China's AI accelerator market this year with Nvidia H200 import largely stalled. This may also be more constructive to smaller AI chip vendors as state-funded data centers are more willing to purchase from a broader range of suppliers, in our view.

Figure 1. China AI Accelerator Comparison

<table><tr><td rowspan="2">Vendor</td><td rowspan="2">Model</td><td rowspan="2">Node</td><td colspan="2">Performance (PELOP)</td><td colspan="3">Memory</td></tr><tr><td>FP16</td><td>FP8</td><td>Type</td><td>Size</td><td>Bandwidth</td></tr><tr><td>Nvidia</td><td>H200</td><td>4nm</td><td>2.0</td><td>4.0</td><td>HBM3e</td><td>141GB</td><td>4.8 TB/s</td></tr><tr><td>Nvidia</td><td>H20</td><td>5nm</td><td>0.3</td><td>0.6</td><td>HBM3</td><td>96GB</td><td>4.0 TB/s</td></tr><tr><td>Huawei</td><td>910B</td><td>7nm</td><td>0.4</td><td>0.8</td><td>HBM2e</td><td>64GB</td><td>1.6 TB/s</td></tr><tr><td>Huawei</td><td>910C</td><td>7nm</td><td>0.8</td><td>1.6</td><td>HBM2e</td><td>96GB</td><td>3.2 TB/s</td></tr><tr><td>Huawei</td><td>920</td><td>6nm</td><td>0.9</td><td>1.8</td><td>HBM3</td><td>128GB</td><td>4.0 TB/s</td></tr><tr><td>Huawei</td><td>950 PR</td><td>6nm</td><td>1.0</td><td>2.0</td><td>HBM3e</td><td>192GB</td><td>1.6 TB/s</td></tr><tr><td>Huawei</td><td>950 DT</td><td>6nm</td><td>1.0</td><td>2.0</td><td>HBM3e</td><td>256GB</td><td>4.0 TB/s</td></tr><tr><td>Cambricon</td><td>S590</td><td>7nm</td><td>0.3</td><td>0.6</td><td>HBM2e</td><td>64GB</td><td>1.6 TB/s</td></tr><tr><td>Cambricon</td><td>S690</td><td>7nm</td><td>0.7</td><td>1.4</td><td>HBM3</td><td>96GB</td><td>2.4 TB/s</td></tr><tr><td>Baidu (Kunlun)</td><td>P800</td><td>7nm</td><td>0.3</td><td>0.7</td><td>HBM2e</td><td>64GB</td><td>0.8 GB/s</td></tr><tr><td>Baidu (Kunlun)</td><td>P900</td><td>7nm</td><td>0.5</td><td>1.0</td><td>HBM3</td><td>96GB</td><td>1.6 TB/s</td></tr><tr><td>Biren</td><td>BR100</td><td>7nm</td><td>1.0</td><td>2.0</td><td>HBM2e</td><td>64GB</td><td>1.2 TB/s</td></tr><tr><td>Iluvatar CoreX</td><td>V100</td><td>7nm</td><td>0.2</td><td>0.4</td><td>HBM2e</td><td>32GB</td><td>2.4 TB/s</td></tr><tr><td>Iluvatar CoreX</td><td>V200</td><td>7nm</td><td>0.4</td><td>0.8</td><td>HBM3</td><td>64GB</td><td>2.3 TB/s</td></tr><tr><td>MetaX</td><td>C500</td><td>7nm</td><td>0.2</td><td>0.4</td><td>HBM3</td><td>48GB</td><td>0.8 GB/s</td></tr><tr><td>MetaX</td><td>C600</td><td>6nm</td><td>0.3</td><td>0.6</td><td>HBM3</td><td>80GB</td><td>1.6 TB/s</td></tr><tr><td>Moore Threads</td><td>S4000</td><td>7nm</td><td>0.1</td><td>0.2</td><td>GDDR6</td><td>48GB</td><td>0.8 GB/s</td></tr><tr><td>Moore Threads</td><td>S5000</td><td>7nm</td><td>0.5</td><td>1.0</td><td>HBM</td><td>80GB</td><td>1.6 TB/s</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi

## Kevin Chen $^{AC}$

+852-2501-2125

kevin.y.chen@citi.com

## Kyna Wong

+852-2868-7820

kyna.wong@citi.com

## Yiming Li, CFA

+852-2501-2857

yiming.li@citi.com

## Karen Huang

+852-2501-2755

karen.xw.huang@citi.com

## See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

Figure 2. Share Price Movement – by Sectors

<table><tr><td>9-Jun-2026</td><td>1W</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td></tr><tr><td>Foundry</td><td>-4.8%</td><td>13.6%</td><td>32.9%</td><td>43.6%</td><td>158.9%</td></tr><tr><td>OSAT</td><td>-1.7%</td><td>28.3%</td><td>31.1%</td><td>61.8%</td><td>103.9%</td></tr><tr><td>Equipment - Front end</td><td>4.8%</td><td>17.6%</td><td>35.2%</td><td>49.3%</td><td>127.5%</td></tr><tr><td>Equipment - Back end</td><td>4.6%</td><td>20.1%</td><td>62.7%</td><td>142.4%</td><td>306.8%</td></tr><tr><td>CPU / SoC</td><td>-6.6%</td><td>-8.6%</td><td>13.3%</td><td>27.2%</td><td>54.3%</td></tr><tr><td>GPU / ASIC</td><td>0.5%</td><td>-8.2%</td><td>34.4%</td><td>0.4%</td><td>34.8%</td></tr><tr><td>Memory</td><td>2.2%</td><td>16.6%</td><td>51.2%</td><td>81.9%</td><td>265.2%</td></tr><tr><td>SiPh / CPO</td><td>5.0%</td><td>18.1%</td><td>82.4%</td><td>183.8%</td><td>743.2%</td></tr><tr><td>Analog</td><td>2.2%</td><td>10.9%</td><td>39.5%</td><td>68.3%</td><td>70.9%</td></tr><tr><td>Power - IDM &amp; Fabless</td><td>1.7%</td><td>21.5%</td><td>22.1%</td><td>52.0%</td><td>90.2%</td></tr><tr><td>Power - Wide Bandgap</td><td>0.9%</td><td>13.7%</td><td>24.5%</td><td>26.0%</td><td>43.7%</td></tr><tr><td>CIS</td><td>-2.6%</td><td>-5.4%</td><td>-10.1%</td><td>-8.1%</td><td>-11.6%</td></tr><tr><td>RF</td><td>0.5%</td><td>-8.5%</td><td>-1.9%</td><td>12.3%</td><td>15.2%</td></tr><tr><td>EDA / Design service</td><td>2.4%</td><td>-1.0%</td><td>7.3%</td><td>21.0%</td><td>68.0%</td></tr><tr><td>Wafer</td><td>20.0%</td><td>22.9%</td><td>48.3%</td><td>53.0%</td><td>68.6%</td></tr><tr><td>Materials</td><td>11.5%</td><td>11.8%</td><td>48.2%</td><td>94.6%</td><td>151.7%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: dataCentral, Citi

## Companies Mentioned:

ASMPT (0522.HK; HK\$185.3; 1; 09 Jun 26; 16:10) | Baidu Inc (9888.HK; HK\$116.6; Not Rated; 09 Jun 26; 16:10) | Baidu.com (BIDU.O; US\$119.1; 1; 08 Jun 26; 16:00) | Cambricon Technologies Corp Ltd (688256.SS; Rmb1270.01; Not Rated; 09 Jun 26; 15:00) | Hua Hong Grace Semiconductor (1347.HK; HK\$140.1; 1; 09 Jun 26; 16:10) | JCET Group (600584.SS; Rmb75.29; 1; 09 Jun 26; 15:00) | MetaX Integrated Circuits (Shanghai) Co Ltd (688802.SS; Rmb704.98; Not Rated; 09 Jun 26; 15:00) | Moore Threads Technology Co Ltd (688795.SS; Rmb615.89; Not Rated; 09 Jun 26; 15:00) | NVIDIA Corp (NVDA.O; US\$208.64; 1; 08 Jun 26; 16:00) | Shanghai Biren Technology Co Ltd (6082.HK; HK\$54.5; Not Rated; 09 Jun 26; 16:10) | Shanghai Iluvatar CoreX Semiconductor Co Ltd (9903.HK; HK\$515.5; Not Rated; 09 Jun 26; 16:10) | Shanghai Vital Deeptech (600641.SS; Rmb27.03; 3; 09 Jun 26; 15:00) | SMIC (0981.HK; HK\$75.0; 1; 09 Jun 26; 16:10) | TongFu Microelectronics (002156.SZ; Rmb64.43; 1; 09 Jun 26; 15:00)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>The Firm has made a market in the publicly traded equity securities of Shanghai Biren Technology Co Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Baidu Inc on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Semiconductor Manufacturing International Corp is subject to Executive Order 13959 described below.The Firm has made a market in the publicly traded equity securities of Semiconductor Manufacturing International Corp on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of ASMPT Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>The Firm has made a market in the publicly traded equity securities of Hua Hong Grace Semiconductor Ltd on at least one occasion since 1 Jan 2025.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from ASMPT,Baidu.com,JCET Group,NVIDIA Corp,TongFu Microelectronics in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: ASMPT,Baidu.com,JCET Group,NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: ASMPT,Baidu.com,JCET Group,NVIDIA Corp,TongFu Microelectronics.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to Baidu.com,NVIDIA Corp. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr><tr><td>The Firm is a market maker in the publicly traded equity securities of ASMPT,Baidu.com,Hua Hong Grace Semiconductor,SMIC,Shanghai Biren Technology Co Ltd.</td></tr><tr><td>Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.</td></tr></table>

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Apr 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>8%</td><td>37%</td><td>47%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>41%</td><td>28%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks.

Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

## Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share price to rise (fall) in absolute terms over a specified period of 30 or 90 days in reaction to one or more specific near-term catalysts or events impacting the company or the market. A Catalyst Watch will be published when Analyst confidence is high that an impact to share price will occur; it will be a STV when confidence level is moderate. A Catalyst Watch or STV Upside/Downside call will automatically expire at the end of the specified 30/90 day period. The Catalyst Watch will also be automatically removed if share price performance (calculated at market close) exceeds 15% against the direction of the call (unless over-ridden by the analyst). The analyst may also remove a Catalyst Watch or STV call prior to the end of the specified period in a published research note. A Catalyst Watch/STV Upside or Downside call may be different from and does not affect a stock's fundamental equity rating, which reflects a longer-term total absolute return expectation. For purposes of FINRA ratings-distribution-disclosure rules, a Catalyst Watch/STV Upside call corresponds to a buy recommendation and a Catalyst Watch/STV Downside call corresponds to a sell recommendation. Any stock not assigned to a Catalyst Watch Upside, Catalyst Watch Downside, STV Upside, or STV Downside call is considered Catalyst Watch/STV No View. For purposes of FINRA ratings distribution-disclosure rules, we correspond Catalyst Watch/STV No View to Hold in our ratings distribution table for our Catalyst

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
