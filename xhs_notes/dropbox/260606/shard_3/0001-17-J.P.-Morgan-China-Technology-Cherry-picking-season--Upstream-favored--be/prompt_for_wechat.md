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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## China Technology

## Cherry-picking season: Upstream favored, be selective downstream

The China tech sector rallied $18\%$ in May, and we view the recent pullback as offering buy-on-dips opportunities for selective companies/sectors. We are more positive on upstream players, such as Semi equipment, OSAT and foundry suppliers, thanks to increasing backlogs and rising ASPs. However, we are more selective on downstream players given looming margin pressure caused by rising costs; this is especially the case for consumer electronic applications with weakening demand. We update our sub-sector pecking order for Semi space which is now: Semi equipment $>$ OSAT $>$ Foundry $>$ Fabless. Iluvatar CoreX, Naura, AMEC, Luxshare and Cowell are our top picks in the China Tech space.

\- Semi equipment retains stronger order backlog. We expect memory and advanced logic demand for local WFE suppliers to increase by more than $50\%$ and $30\%$ YoY respectively in 2026, with further upside in 2027, thanks to progressing IPO timelines for CXMT and YMTC. In addition, with ramping indigenous AI chip volume from 2H26, backend equipment vendors could also benefit from incremental demand for advanced package, testing, etc. Extending growth visibility of semi equipment companies could help to support buoyed valuation of the sector, in our view.

\- OSAT/Foundry: margin upside ahead. We witnessed strong and continuous price hikes for foundries and OSAT suppliers in 2Q26, thanks to elevated utilization and pass-through of increasing material costs. Although we expect rising depreciation due to intensified CAPEX, price rises could still drive better margins for OSAT/Foundry players from 2H26 onwards. This is especially true for OSAT players more exposed to high-margin AI-related products, such as GPU, PMIC, etc.

\- Be selective on downstream. From a downstream demand perspective, we expect intact and strong CSP investment with proliferating AI applications, while component demand from automotive and industry has been recovering in 2Q26. However, demand for consumer electronic products, such as Android phones and AIoT devices, is weakening. We believe increasing local foundry supply could help to accelerate sales growth for indigenous GPU/ AI ASIC players, which are debuting next-generation chips and fulfilling strong CSP demand. On the other hand, hiking upstream costs could weigh on margins of fabless players which are highly exposed to consumer electronics and cannot pass through incremental costs.

\- Cherry picking: Iluvatar CoreX is our top pick in AI chip fabless, given its intact supply and client/product breakthrough. We are also positive on the WFE sector, thanks to strong CAPEX for memory and advanced logic fabs, and believe top WFE platforms in China NAURA and AMEC are set to benefit. With higher exposure to premium iPhone models (iPhone17/18 pro/pro max), we think Luxshare will benefit most from stronger than expected iPhone volume.

## Technology

Billy Feng AC

(86-21) 6106 6359

billy.feng@JPM.com

SAC Registration Number: S1730520030005

## Ri Xu

(86-21) 6106 6318

ri.xu@jpmchase.com

SAC Registration Number: S1730522100001

## Cherry Liu

(86-21) 6106-6200

ye.liu@JPM.com

SAC Registration Number: S1730521090001

JPM Securities (China) Company Limited

Companies Discussed in This Report (all prices in this report as of market close on 04 June 2026, unless otherwise indicated)

AMEC - A(688012.SS/Rmb289.39/OW), Cowell e Holdings - H(1415.HK/HK\$28.76/OW), Iluvatar CoreX - H(9903.HK/HK\$430.20/OW), Luxshare - A(002475.SZ/Rmb74.59/OW), NAURA - A(002371.SZ/Rmb627.00/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to AMEC - A, Luxshare - A, NAURA - A or related entities.  
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Luxshare - A or related entities.  
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Luxshare - A or related entities.  
- Debt Position: JPM may hold a position in the debt securities of AMEC - A, Cowell e Holdings - H, Luxshare - A, NAURA - A, Iluvatar CoreX - H or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

AMEC - A (688012.SS, 688012 CH) Price Chart  
![](images/391c70163217090b6eb9bed93f0ca90603f78cba03058b293a902692ba13d93a.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(Rmb) |
| ---------- | ---------- |
| Jul 24     | OW Rmb178  |
| Jan 25     | OW Rmb195  |
| Jan 25     | OW Rmb220  |
| Jul 25     | OW Rmb345  |
| Jul 25     | OW Rmb230  |
| Jan 26     | OW Rmb380  |
| Jan 26     | OW Rmb430  |
| Jan 26     | OW Rmb400  |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>29-Jul-24</td><td>OW</td><td>146.78</td><td>178</td></tr><tr><td>31-Oct-24</td><td>OW</td><td>181.15</td><td>195</td></tr><tr><td>20-Feb-25</td><td>OW</td><td>201.27</td><td>220</td></tr><tr><td>31-Aug-25</td><td>OW</td><td>214.17</td><td>230</td></tr><tr><td>24-Sep-25</td><td>OW</td><td>280.00</td><td>345</td></tr><tr><td>30-Oct-25</td><td>OW</td><td>296.66</td><td>352</td></tr><tr><td>11-Jan-26</td><td>OW</td><td>336.68</td><td>380</td></tr><tr><td>06-Apr-26</td><td>OW</td><td>293.50</td><td>400</td></tr><tr><td>28-Apr-26</td><td>OW</td><td>352.01</td><td>430</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Jul 29, 2024. All share prices are as of market close on the previous business day.

Cowell e Holdings - H (1415.HK, 1415 HK) Price Chart  
![](images/8a3c6ff44d5566ce6a6884f931397ac1a5cf37344ccad594b88087172a65b7cc.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(HK$) |
| ---------- | ---------- |
| Sep 25     | 44         |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target (HK$)</td></tr><tr><td>04-Aug-25</td><td>OW</td><td>26.65</td><td>44</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Aug 04, 2025. All share prices are as of market close on the previous business day.

Luxshare - A (002475.SZ, 002475 CH) Price Chart  
![](images/7674ae35f233af4d1fb3dfa7a8c892a2d9d75e036dcdc5aedd8c9b1cb3a29fc3.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(Rmb) |
| ---------- | ---------- |
| Jul 24     | OW Rmb46   |
| Jan 25     | OW Rmb53   |
| Jul 25     | OW Rmb63   |
| Jan 26     | OW Rmb75   |
| Jan 26     | OW Rmb82   |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>25-Aug-24</td><td>OW</td><td>37.89</td><td>46</td></tr><tr><td>28-Oct-24</td><td>OW</td><td>43.35</td><td>53</td></tr><tr><td>28-Aug-25</td><td>OW</td><td>44.98</td><td>63</td></tr><tr><td>24-Sep-25</td><td>OW</td><td>65.70</td><td>75</td></tr><tr><td>29-Apr-26</td><td>OW</td><td>69.88</td><td>82</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Sep 25, 2018. All share prices are as of market close on the previous business day.

NAURA - A (002371.SZ, 002371 CH) Price Chart  
![](images/31b25838d30b797a0559d4efce24d979201ad9f9dab761a7717c61b2198811c1.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(Rmb) |
| ---------- | ---------- |
| Jan 24     | 250        |
| Jul 24     | 350        |
| Jan 25     | 450        |
| Jul 25     | 350        |
| Jan 26     | 500        |
| Apr 26     | 700        |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>04-Nov-25</td><td>OW</td><td>401.00</td><td>610</td></tr><tr><td>30-Apr-26</td><td>OW</td><td>510.71</td><td>700</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Nov 04, 2025. All share prices are as of market close on the previous business day.

Iluvatar CoreX - H (9903.HK, 9903 HK) Price Chart  
![](images/7b898ed054725382afb47abe1f821eb390e1242024c9786b0c1a1c7e35e15fcc.jpg)

<details>
<summary>line chart</summary>

| Date  | Price(HK$) |
|-------|------------|
| Apr   | 620        |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target (HK$)</td></tr><tr><td>07-Apr-26</td><td>OW</td><td>219.80</td><td>620</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends.  
Initiated coverage Apr 07, 2026. All share prices are as of market close on the previous business day.

The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period.

JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Feng, Billy : AMEC - A (688012.SS), AtHub - A (603881.SS), China Resources Microelectronics - A (688396.SS), Dongshan Precision - A (002384.SZ), Gigadevice Semiconductor - A (603986.SS), Goertek - A (002241.SZ), Hangzhou HikVision Digital Technology Co., Ltd - A (002415.SZ), Huafeng Test & Control - A (688200.SS), Iluvatar CoreX - H (9903.HK), Inspur - A (000977.SZ), JCET - A (600584.SS), Luxshare - A (002475.SZ), Maxscend Microelectronics - A (300782.SZ), MetaX - A (688802.SH), NAURA - A (002371.SZ), OmniVision - A (603501.SS), Sinnet - A (300383.SZ), Universal Scientific Industrial (Shanghai) - A (601231.SS), Wingtech Tech - A (600745.SS), Zhejiang Dahua Technology Co., Ltd - A (002236.SZ), Zhongji Innolight - A (300308.SZ)

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.  
\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.  
For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance obligations when making investment decisions.

Any digital or crypto assets discussed in this research report are subject to a rapidly changing regulatory landscape. For relevant regulatory advisories on crypto assets, including bitcoin and ether, please see https://www.JPM.com/disclosures/cryptoasset-disclosure.

The author(s) of this research report may not be licensed to carry on regulated activities in your jurisdiction and, if not licensed, do not hold themselves out as being able to do

[中间内容因长度限制已省略]

re subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to

certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
