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
# China: Energy-led PPI increased further in May, while core CPI softened

## Bottom line:

China's headline CPI inflation was flat at $+1.2\%$ yoy in May, as higher energy prices were broadly offset by lower food prices. Core CPI inflation edged down to $+1.1\%$ yoy, likely due to softer tourism-related services prices. Headline PPI inflation increased further to $+3.9\%$ yoy in May from $+2.8\%$ yoy in April, mainly due to higher chemical, energy, and coal prices. Overall, upstream sectors accounted for around $82\%$ of the rebound in year-over-year headline PPI inflation.

## Key numbers:

CPI: +1.2% yoy (+1.0% mom annualized\*) in May vs. GS: +1.4% yoy, Bloomberg consensus: +1.3% yoy; April: +1.2% yoy (+2.4% mom annualized\*).

Food: -1.7% yoy in May (-0.9% mom annualized\*) vs. -1.6% yoy in April.  
Non-food: +1.9% yoy in May (+1.8% mom annualized\*) vs. +1.8% yoy in April.  
Core: +1.1% yoy in May (-0.1% mom annualized\*) vs. +1.2% yoy in April.

PPI: +3.9% yoy in May (+9.7% mom annualized\*) vs. GS: +4.0% yoy, Bloomberg consensus: +3.9% yoy; April: +2.8% yoy (+22.4% mom annualized\*).

(\*seasonally adjusted by GS)

## Main points:

1. China's headline CPI was flat at $+1.2\%$ yoy in May, as higher energy prices were broadly offset by lower food prices (Exhibit 1). In month-on-month terms, headline CPI slowed to $+1.0\%$ (annualized, seasonally adjusted) in May (vs. $+2.4\%$ mom s.a. ann in April).

2. In year-over-year terms, food inflation edged down to $-1.7\%$ yoy in May from $-1.6\%$ yoy in April (Exhibit 2). Among major food items, pork prices fell by $16.1\%$ yoy in May (vs. $-15.2\%$ yoy in April). Fresh vegetable prices rose by $1.6\%$ yoy in May (vs. $-0.5\%$ yoy in April), and fresh fruit prices fell by $2.2\%$ yoy in May (vs. $-1.0\%$ yoy in April).

3. Non-food CPI inflation edged up to $+1.9\%$ yoy in May from $+1.8\%$ yoy in April, mainly on higher energy prices (Exhibit 3). Specifically, fuel costs rose by $+21.1\%$ yoy in May (vs. $+17.4\%$ yoy in April), accounting for all of the increase in non-food CPI inflation from April to May. After excluding food and energy prices, core CPI inflation edged down to $+1.1\%$ yoy in May (vs. $+1.2\%$ yoy in April), likely reflecting softer tourism-related services prices, with transportation services inflation easing to $4.7\%$

Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

yoy in May (vs. +5.1% yoy in April).

4. Year-over-year PPI inflation rose to $+3.9\%$ yoy in May from $+2.8\%$ yoy in April, largely reflecting higher chemical, oil & gas, and coal prices (Exhibit 4). Overall, upstream sectors accounted for around $82\%$ of the rebound in headline PPI inflation, with chemicals, oil & gas, and coal contributing 0.3pp, 0.2pp, and 0.2pp, respectively, to the 1.1pp increase in headline PPI inflation. In month-over-month terms, PPI inflation fell to $9.7\%$ (annualized, seasonally adjusted) in May (vs. $22.4\%$ in April). PPI inflation in producer goods rose to $+5.2\%$ yoy in May from $+3.8\%$ yoy in April, and PPI inflation in consumer goods edged up to $-0.8\%$ yoy in May (vs. $-1.0\%$ yoy in April).

## Xinquan Chen

Exhibit 1: Year-over-year PPI inflation increased further from April to May  
![](images/4f057dedc324e75aa99a5975642e80a081414f78224a3bef7cad8d19b7d7cb77.jpg)

<details>
<summary>line chart</summary>

| Year | CPI   | PPI   |
|------|-------|-------|
| 07   | 3.0   | 2.5   |
| 08   | 8.0   | 10.0  |
| 09   | -2.0  | -8.0  |
| 10   | 4.0   | 6.0   |
| 11   | 6.0   | 8.0   |
| 12   | 4.0   | 6.0   |
| 13   | 3.0   | 4.0   |
| 14   | 2.0   | 2.0   |
| 15   | 1.0   | -2.0  |
| 16   | 2.0   | -6.0  |
| 17   | 3.0   | 8.0   |
| 18   | 2.0   | 4.0   |
| 19   | 3.0   | 2.0   |
| 20   | 5.0   | -4.0  |
| 21   | -1.0  | 12.0  |
| 22   | 3.0   | -6.0  |
| 23   | 1.0   | -4.0  |
| 24   | 0.0   | -2.0  |
| 25   | -1.0  | -4.0  |
| 26   | 1.0   | 4.0   |
</details>

Source: NBS

Exhibit 2: Food CPI inflation fell in May on a broad-based decline in food prices  
![](images/28a733db4f85f9687b8eab18ae465a61db3150206efcb6c78aaf8a8f6899c324.jpg)

<details>
<summary>bar chart</summary>

Contribution to year-over-year food inflation
| Year | Pork (%) | Fresh vegetables (%) | Fresh fruits (%) | Eggs (%) | Others (%) |
|---|---|---|---|---|---|
| 19 | -0.5 | 0.2 | 0.8 | 0.3 | 2.1 |
| 20 | 14.2 | -0.8 | -1.5 | 12.3 | 18.7 |
| 21 | -2.1 | 0.5 | 0.3 | -1.2 | 1.8 |
| 22 | -6.8 | -1.2 | 0.7 | -0.5 | 3.5 |
| 23 | -1.5 | 0.1 | 0.9 | -0.2 | 5.2 |
| 24 | -3.2 | -0.3 | -0.1 | -0.8 | -6.1 |
| 25 | 0.8 | 0.5 | 0.4 | 0.2 | 0.9 |
| 26 | -0.7 | -0.4 | -0.6 | -0.3 | 1.2 |
</details>

Source: NBS, GS Global Investment Research

Exhibit 3: Non-food CPI inflation edged up on higher energy prices  
![](images/911cd38abe2e4797aec40147c37d93d56d693d5beea8e9045ff954cce394d91b.jpg)

<details>
<summary>line chart</summary>

| Year | Energy | Tourism-related | Durable goods | Shelter | Administered items | Others | Nonfood |
|------|--------|-----------------|---------------|---------|--------------------|--------|---------|
| 16   | -0.5   | 0.5             | 0.0           | 0.0     | 0.0                | 0.0    | 1.0     |
| 17   | 0.0    | 1.0             | 0.5           | 0.5     | 0.5                | 0.5    | 2.5     |
| 18   | 0.5    | 1.5             | 1.0           | 1.0     | 1.0                | 1.0    | 2.5     |
| 19   | 1.0    | 2.0             | 1.5           | 1.5     | 1.5                | 1.5    | 2.0     |
| 20   | -0.5   | 0.5             | 0.0           | 0.0     | 0.0                | 0.0    | 1.5     |
| 21   | -1.0   | -1.0            | -0.5          | -0.5    | -0.5               | -0.5   | -1.0    |
| 22   | 0.5    | 1.5             | 1.0           | 1.0     | 1.0                | 1.0    | 2.5     |
| 23   | -0.5   | 0.5             | 0.0           | 0.0     | 0.0                | 0.0    | 1.5     |
| 24   | 0.0    | 1.0             | 0.5           | 0.5     | 0.5                | 0.5    | 2.0     |
| 25   | -0.5   | 0.5             | 0.0           | 0.0     | 0.0                | 0.0    | 1.5     |
| 26   | 0.5    | 1.5             | 1.0           | 1.0     | 1.0                | 1.0    | 2.5     |
</details>

Source: CEIC, GS Global Investment Research

Exhibit 4: PPI inflation increased further from April to May, mainly due to higher energy and related chemical prices  
![](images/d84351128c8e0a529c6c6fde8dcbc4df76e092b21d74a2e6c62802306457e636.jpg)

<details>
<summary>bar-line hybrid</summary>

Contribution to year-over-year PPI inflation
| Year | Ferrous metals mining/smelting (%) | Petrol mining/processing (%) | Raw chemicals/chemical fiber (%) | Downstream (%) | Nonferrous metals mining/smelting (%) | Coal mining (%) | Nonmetal mining/mfg (%) | Headline (%) |
|---|---|---|---|---|---|---|---|---|
| 19 | 0.5 | 0.2 | -0.3 | 0.1 | 0.4 | 0.6 | 0.7 | 0.3 |
| 20 | -0.8 | -1.2 | -0.5 | -0.6 | -0.3 | -0.1 | -0.2 | -1.5 |
| 21 | 1.2 | 0.8 | 0.5 | 0.3 | 1.5 | 1.8 | 1.6 | 1.2 |
| 22 | 2.5 | 2.0 | 1.8 | 1.5 | 3.0 | 2.5 | 2.2 | 3.5 |
| 23 | -0.5 | -0.8 | -0.3 | -0.4 | -0.2 | -0.6 | -0.7 | -1.8 |
| 24 | -0.3 | -0.5 | -0.2 | -0.3 | -0.1 | -0.4 | -0.5 | -1.2 |
| 25 | -0.1 | -0.3 | -0.1 | -0.2 | 0.1 | -0.2 | -0.3 | -0.8 |
| 26 | 0.8 | 1.2 | 0.9 | 0.7 | 1.5 | 1.8 | 1.6 | 3.5 |
Percentage point: Fertures metals mining/smelting; Petrol mining/processing; Raw chemicals/chemical fiber; Downstream; Nonferrous metals mining/smelting; Coal mining; Nonmetal mining/mfg; Headline.
</details>

Source: NBS, GS Global Investment Research

## The China Economics Team

## Andrew Tilton

+852-2978-1802

andrew.tilton@gs.com

GS (Asia) L.L.C.

## Hui Shan

+852-2978-6634

hui.shan@gs.com

GS (Asia) L.L.C.

## Lisheng Wang

+852-3966-4004

lisheng.wang@gs.com

GS (Asia) L.L.C.

## Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

## Yuting Yang

+852-2978-7283

yuting.y.yang@gs.com

GS (Asia) L.L.C.

## Chelsea Song

+852-2978-0106

chelsea.song@gs.com

GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Xinquan Chen, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Xinquan Chen GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annual audit compliance report can be found at this link: https://publishing.gs.com/content/site/india-annual-compliance-report.html. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no responsibility for any investment decisions that may be taken by a client or any other person based on this research report. Singapore: GS (Singapore) Pte. (Company Number: 198602165W), which is regulated by the Monetary Authority of Singapore, accepts legal responsibility for this research, and should be contacted with respect to any matters arising from, or in connection with, this research. Taiwan: This material is for reference only and must not be reprinted without permission. Investors should carefully consider their own investment risk. Investment results are the responsibility of the individual investor. United Kingdom: Persons who would be categorized as retail clients in the United Kingdom, as such term is defined in the rules of the Financial Conduct Authority, should read this research in conjunction with prior GS on the covered

companies referred to herein and should refer to the risk warnings that have been sent to them by GS International. A copy of these risks warnings, and a glossary of certain financial terms used in this report, are available from GS International on request.

European Union and United Kingdom: Disclosure information in relation to Article 6 (2) of the European Commission Delegated Regulation (EU) (2016/958) supplementing Regulation (EU) No 596/2014 of the European Parliament and of the Council (including as that Delegated Regulation is implemented into United Kingdom domestic law and regulation following the United Kingdom's departure from the European Union and the European Economic Area) with regard to regulatory technical standards for the technical arrangements for objective presentation of investment recommendations or other information recommending or suggesting an investment strategy and for disclosure of particular interests or indications of conflicts of interest is available at https://www.gs.com/disclosures/europeanpolicy.html which states the European Policy for Managing Conflicts of Interest in Connection with Investment Research.

Japan: GS Japan Co., Ltd. is a Financial Instrument Dealer registered with the Kanto Financial Bureau under registration number Kinsho 69, and a member of Japan Securities Dealers Association, Financial Futures Association of Japan Type II Financial Instruments Firms Association, and Investm

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
