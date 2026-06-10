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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`BARC`。标题格式建议：`# BARC：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份BARC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
IT Hardware and Communications Equipment

# Server Model Update: Enterprise Surprises Up, AI Momentum Remains

We update our detailed Server model following recent results and industry conversations. Enterprise strength surprised materially to the upside across server players with AI momentum still strong this earnings cycle. We believe ASP is driving a majority of the upside, with unit growth also cited.

Following recent results and industry conversations, we adjust our Cloud and Enterprise server estimates. Recall, this year we changed our model methodology where we now break out Cloud (inclusive of AI) and Enterprise servers vs previously where we used AI vs Traditional.

Our Cloud estimates move higher, in line with major hyperscalers' lifted capex expectations, and we now estimate Cloud growing at a 5-year CAGR of \~62% (2022-27E) up from our prior estimate of \~59%. We view our revenue estimates moving higher as impressive, especially given how large our revenue estimates now are.

Enterprise surprised materially to the upside this past Q across server players. Although we believe the majority of the upward movement was pull-in and ASP driven, companies also cited how agentic AI and inference are driving a new opp for traditional servers. However, we do not expect traditional server growth to continue into next year, and estimate LSD moving forward. Because of this year's expected outsized traditional server growth (we now estimate 33% growth assuming some unit growth coupled with higher ASPs), our Enterprise 5-year CAGR through 2027 is now MSD (\~6%) vs our prior estimate of \~flat.

Positive capex commentary continues from hyperscalers with >\$700Bn in capex now expected in CY26, up from \~\$423Bn in CY25. Recent results from DELL, HPE, and SMCI are positive proof points to this higher capex directly translating into AI-related network infrastructure investments. Despite memory-related headwinds, we now expect Enterprise to grow >30% this year, assuming significant ASP increases and some unit volume. We are of the view that for Enterprise players, where purchases are on bits not necessarily units, pricing actions will fill the gap with potentially lower unit volumes. However, we do expect \~1% growth in CY27, given our estimates this year on top of two strong years of growth in 2024-25 are hard to sustain, especially given continued price increases may erode demand more than current expectations.

IT Hardware and Communications

Equipment

NEUTRAL

IT Hardware and Communications

Equipment

Tim Long

+1 212 526 4043

tim.long@BARC.com

BCI, US

Alyssa Shreves

+1 212 526 7570

alyssa.shreves@BARC.com

BCI, US

Mary Lenox

+1 212 526 6277

mary.lenox@BARC.com

BCI, US

Clarisse Yu

+1 212 526 7025

clarisse.yu@BARC.com

BCI, US

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

## THE 2026 EXTEL SURVEY IS NOW OPEN

# Support our industry-leading analysts with 5-Star votes in this year's Extel All-America Research Survey

Vote Now

View Analysts

## Server Model Wrap Up

- Our CY26Cloud server revenue forecasts move lower and CY27 move higher, accounting for the above-mentioned strength in hyperscaler capex and focus on technical infrastructure investments. However, we do acknowledge some lack of visibility on AI server builds could make numbers lumpy (like we've previously seen with SMCI).  
- Our new Cloud server revenue estimates are \$567Bn/\$885Bn in CY26/27 vs our prior estimates of \$585Bn/\$817Bn, respectively. We model growth of 77% and 56% in 2026/2027 vs our prior estimates of 84% and 40%. xPU server estimates and updated segmentation from HPE (we adjusted our 2025 metrics), primarily accounted for the drop in 2026 growth vs prior estimates (not a fundamental change). DELL (and to lesser extent SMCI) drove the tick up in our estimates on the OEM front, with another increase in implied ODM growth.  
- Despite the move higher in CY27 estimates, we expect there is potential upside bias to our estimates, given the strong capex announcements from the large hypers, the rising interest in enterprise/inferencing opportunities, and if large AI training deals get appropriate funding. However, there is also a scenario in which we could see a push-out in revenues, given some of the larger sovereign deals are scheduled for the Middle East, although we have yet to hear of any deployment delays.  
- We now estimate Enterprise server revenues up \~33% in CY26 (vs prior estimate of \~2%), given the material outperformance and commentary from OEM players. DELL now expects traditional servers to grow >60% for the FY, and HPE cited traditional server orders increased DDD in the Q. DELL also mentioned that despite ASP increases, the company saw traditional server unit growth in the Q. We believe OEM players are enjoying multiple ASP increases coupled with customer buying behavior holding up better than expected. We believe units may be up MSD-HSD, although ASPs are up most likely closer to 40-50%. We expect further ASP increases and the cyclicality of the enterprise business to normalize growth next year down to \~1% growth (with downside bias to estimates, if unit volumes and demand erode further than we've currently estimated).  
- Overall, we model total server revenue growth of 70%/49% in CY26/27, from 71%/36% prior estimates, as we expect continued AI strength momentum coupled with greater than expected Enterprise strength (in terms of revenues).

Server market performance has been bifurcated, with Cloud growth materially diverged from Enterprise over the past few years, and we do not expect this phenomenon to change. Hyperscaler capex is one of the main data points to watch for AI servers.

FIGURE 1. Cloud Server Revs vs Top Hyperscalers' Capex  
![](images/87195c03650710011dd05cd2a36fdbc875dceb4e1f27d3e0bf3b55ef487ca1ef.jpg)

<details>
<summary>bar-line hybrid</summary>

Cloud Capex Spend ($B)
| Year | Cloud Server Revenue ($Bn) | Total Cloud Capex ($Bn) | Cloud Server Growth Rate Y/Y (%) |
| :--- | :--- | :--- | :--- |
| 2022 | 80.5 | 158.0 | -11.4 |
| 2023 | 102.9 | 155.9 | 27.9 |
| 2024 | 216.4 | 247.4 | 110.2 |
| 2025 | 320.3 | 422.7 | 48.0 |
| 2026E | 567.0 | 754.0 | 77.0 |
| 2027E | 884.8 | 1,003.8 | 56.1 |
</details>

Source: 650 Group, Company Documents, Bloomberg, BARC Estimates

We expect growth from Cloud and Enterprise servers moving through CY26-27. We find the Cloud growth impressive, given the large base it's growing from. Additionally, our Enterprise server growth this year accounts for the ASP increases along with continued volume growth (despite memory headwinds) OEMs cited this past earnings cycle.

FIGURE 2. Total Server Revenue Growth  
![](images/4900fd87019cb2e9d3a846b1ceb7032a49472eb3fa454fa017bd30d8d13ea396.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | Total Cloud Server Revenue ($M) | Total Enterprise Server Revenue ($M) | Y/Y % Change (%) |
| :--- | :--- | :--- | :--- |
| 2021 | 90,793 | 57,883 | |
| 2022 | 80,463 | 61,797 | -4 |
| 2023 | 102,921 | 50,914 | 8 |
| 2024 | 216,370 | 56,818 | 78 |
| 2025 | 320,296 | 60,968 | 40 |
| 2026E | 567,007 | 81,023 | 70 |
| 2027E | 884,826 | 82,109 | 49 |
</details>

Source: 650 Group, Company Documents, Bloomberg, BARC Estimates

AI has been a big positive for the server industry, with a focus on companies' growing AI server share and backlog. The Cloud server market has grown to multiples the size of the Enterprise server market, on a revenue basis. White box (inclusive of NVDA) continues to take market share from branded players, and we expect this to continue. A breakdown below of NVDA-based server revenues compared to xPU and CPU server share for 2026E.

FIGURE 3. % Share of NVDA-based server share, xPU and CPU server share for 2026E  
![](images/3b50b02adf85b9a019d8ca8e6aba834ecf773d7f8f0024a5534518684c807a7f.jpg)

<details>
<summary>pie chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| CPU Server | 13 |
| xPU Server | 16 |
| GPU server | 71 |
</details>

Source: 650 Group, Company Documents, Bloomberg, BARC Estimates

However, once Enterprise/Inferencing and Sovereign AI ramp more meaningfully, we expect some share distribution towards branded players.

FIGURE 4. Cloud Server Market by Vendor  
![](images/a64c9b3a1537134c92f90c2dd6811a4afff43d3e9ed52979a65d2f5000d62d40.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | Dell ($M) | Super Micro ($M) | CPU WB ($M) | HPE ($M) | Nvidia/GPU WB ($M) | xPU WB ($M) | Others - Vendors ($M) | y/y growth (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2023 | 100,000 | 10,000 | 50,000 | 10,000 | 50,000 | 10,000 | 10,000 | 28 |
| 2024 | 150,000 | 15,000 | 60,000 | 15,000 | 100,000 | 20,000 | 15,000 | 110 |
| 2025 | 150,000 | 15,000 | 65,000 | 15,000 | 150,000 | 35,000 | 25,000 | 48 |
| 2026E | 150,000 | 15,000 | 75,000 | 15,000 | 250,000 | 65,000 | 45,000 | 77 |
| 2027E | 150,000 | 15,000 | 85,000 | 15,000 | 350,000 | 95,000 | 65,000 | 56 |
</details>

Source: 650 Group, Company Documents, Bloomberg, BARC Estimates

We entered the year under the assumption ASP increases would offset expected unit volume declines. However, ASP increases coupled with unit volumes holding in better than expected caused material upside to our estimates. Although we believe the majority of outperformance is most likely ASP driven (with pull-in benefiting YTD results), the benefit of unit volumes has propelled estimates much higher than expected. We do expect demand erosion to eventually catch up with numbers, especially if companies continue to raise prices, which is why we assume \~1% growth into CY27 (with a downward bias). The market share picture within Enterprise servers has remained largely steady over the past few years with DELL and HPE \~30% and 20s% share, respectively.

FIGURE 5. Enterprise Server Market by Vendor  
![](images/039944f773093d776462772406a16669eeed4c60cc143d987ac49f3dc79192ad.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Cisco ($M) | Dell ($M) | IBM ($M) | Super Micro ($M) | Lenovo ($M) | HPE ($M) | Oracle ($M) | Others - Vendors ($M) | y/y growth (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2023 | 1000 | 5000 | 4000 | 2000 | 6000 | 10000 | 3000 | 1000 | -18% |
| 2024 | 1000 | 15000 | 5000 | 2000 | 8000 | 12000 | 4000 | 1500 | 12% |
| 2025 | 1000 | 15000 | 6000 | 2000 | 9000 | 13000 | 5000 | 1800 | 7% |
| 2026E | 1000 | 31000 | 5000 | 2000 | 12000 | 25000 | 4500 | 2500 | 33% |
| 2027E | 1000 | 32500 | 4500 | 2500 | 11500 | 24500 | 4500 | 2500 | 1% |
</details>

Source: 650 Group, Company Documents, Bloomberg, BARC Estimates

## Vendor Takeaways

\- DELL AI server momentum continued last Q with AI server revenue \~37% of total revenue in the Q and up 80% Q/Q. AI backlog increased to \$51.3Bn, up 19% Q/Q, and management guided to \~\$60Bn in FY AI server revenue compared to prior view of \$50B. AI customer base is now \~5,000 customers (up >50% in last six months). Traditional server results were also impressive in the Q, up over 90% y/y with management now expecting traditional servers to grow just over 60% for the FY. We expect pricing and pull-ins are accounting for some of the traditional server demand, although management also highlighted how agentic AI and inference are driving a new opp for traditional servers, and we know ASPs are up a lot on higher commodity costs and richer configurations.

\- HPE saw orders in traditional server up triple digits last Q. However, ASP is playing a significant role right now. The company is seeing customers start new projects even given where ASPs are, with the company seeing agentic AI and inferencing use cases. Customers are early on in their agentic journey but focused on it and what they need to do to invest. \$1.8bn in AI orders in the quarter and \$16.4bn cumulative. We continue to view HPE as being more selective with AI deals, focusing on GM and working capital. Given the acquisition of JNPR, we view HPE now more as a networking company vs server, especially given networking now is expected to comprise >50% of total company operating profit for the year.

\- SMCI results missed on the top line last Q, due to customer readiness, with revenue of \$10.2Bn vs guidance of "at least \$12.3Bn." Management guided to FQ4 revenue in the range of \$11-\$12.5Bn (within range of our prior estimate) and FY26 revenue in the range of \$38.9-\$40.4Bn (slightly below prior guidance of "at least \$40Bn"). Enterprise, which was \~28% of revenue this Q up from \~15% the prior Q, also contributed to margin outperformance this Q. Rev rec visibility remains limited, and we expect this to remain into the following Qs. Some customers have slowed their plans with the company since the indictment and ongoing investigation, although we suspect limited business was lost, given the record backlog.

## Analyst(s) Certification(s):

I, Tim Long, hereby certify (1) that the views expressed in this research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC"). All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

Where any companies are the subject of this research report, for current important disclosures regarding those companies please refer to https://publicresearch.BARC.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

The analysts responsible for preparing this research report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by investment banking activities, the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst.

Research analysts employed outside the US by affiliates of BARC Capital Inc. are not registered/qualified as research analysts with FINRA. Such non-US research analysts may not be associated persons of BARC Capital Inc., which is a FINRA member, and therefore may not be subject to FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst's account.

Analysts regularly conduct site visits to view the material operations of covered companies, but BARC policy prohibits them from accepting payment or reimbursement by any covered company of their travel expenses for such visits.

BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

## Materially Mentioned Stocks (Ticker, Date, Price)

Cisco Systems, Inc. (CSCO, 08-Jun-2026, USD 124.15), Equal Weight/Neutral, CD/CE/D/J/K/L/M

Dell Technologies Inc. (DELL, 08-Jun-2026, USD 400.77), Overweight/Neutral, A/D/E/J/K/L/M/N

Hewlett Packard Enterprise Company (HPE, 08-Jun-2026, USD 49.87), Overweight/Neutral, A/CD/CE/D/E/FA/J/K/L/M

Super Micro (SMCI, 08-Jun-2026, USD 43.99), Equal Weight/Neutral, D/FA/J/L

Unless otherwise indicated, prices are sourced from Bloomberg and reflect the closing price in the relevant trading market, which may not be the last available closing price at the time of publication.

## Disclosure Legend:

A: BARC Bank PLC and/or an affiliate has been lead manager or co-lead manager of a publicly disclosed offer of securities of the issuer in the previous 12 months.

B: An employee or non-executive director of BARC PLC is a director of this issuer.

CD: BARC Bank PLC and/or an affiliate is a market-maker in debt securities issued by this issuer.

CE: BARC Bank PLC and/or an affiliate is a market-maker in equity securities issued by this issuer.

CH: BARC Bank PLC and/or its group companies makes, or will make, a market in the securities (as defined under paragraph 16.2 (k) of the HK SFC Code of Conduct) in respect of this issuer.

D: BARC Bank PLC and/or an affiliate has received compensation for investment banking services from this issuer in the past 12 months.

E: BARC Bank PLC and/or an affiliate expects to receive or intends to seek compensation for investment banking services from this issuer within the next 3 months.

FA: BARC Bank PLC and/or an affiliate beneficially owns 1% or more of a class of equity securities of this issuer, as calculated in accordance with US regulations.

FB: BARC Bank PLC and/or an affiliate beneficially owns a long position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FC: BARC Bank PLC and/or an affiliate beneficially owns a short position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FD: BARC Bank PLC and/or an affiliate beneficially owns 1% or more of a class of equity securities of this issuer, as calculated in accordance with South Korean regulations.

FE: BARC Bank PLC and/or its group companies has financial interests in relation to this issuer and such interests aggregate to an amou

[中间内容因长度限制已省略]

 scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
