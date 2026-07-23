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
# China: Fiscal revenue and expenditure growth both improved in June, while land sales revenue contracted further

## Bottom line:

Year-on-year growth in on-budget fiscal revenue improved in June amid higher PPI inflation and mixed activity growth, as faster tax revenue growth more than offset slower non-tax revenue growth. Fiscal expenditure growth also rebounded, but it remained below fiscal revenue growth. Property-related government revenue weakened further in June, mainly due to a wider year-on-year contraction in off-budget land sales revenue. Combining on-budget and off-budget financing channels, our proprietary “augmented fiscal deficit” (AFD) metric continued to narrow in June on both a 3-month and 12-month moving average basis. We estimate the negative fiscal impulse in Q2 contributed more than 40% of the sequential decline in real GDP growth from Q1 to Q2. After weaker-than-expected Q2 GDP, we expect policymakers to strengthen easing rhetoric and pledge to accelerate implementation of planned demand-side measures at the upcoming July Politburo meeting.

Lisheng Wang
+852-3966-4004 |
lisheng.wang@gs.com
GS (Asia) L.L.C.

## Key numbers:

Fiscal revenue growth: +8.7% yoy in June (+2.6% mom sa non-annualized, estimated by GS), vs. +6.6% yoy in May (-0.5% mom sa non-annualized).

Fiscal expenditure growth: +4.0% yoy in June (+0.9% mom sa non-annualized), vs. -1.6% yoy in May (-0.5% mom sa non-annualized).

Land sales revenue growth: -42.1% yoy in June (-9.2% mom sa non-annualized), vs. -35.8% yoy in May (-2.5% mom sa non-annualized).

Property-related tax revenue growth: -12.3% yoy in June, vs. -2.6% yoy in May.

Effective fiscal deficit ratio (after GS seasonal adjustment): -3.9% of GDP 3mma and -4.7% 12mma as of June, vs. -4.0% of GDP 3mma and -4.7% 12mma as of May.

Augmented fiscal deficit (AFD) ratio (after GS seasonal adjustment): -7.0% of GDP 3mma and -10.2% 12mma as of June, vs. -8.4% of GDP 3mma and -10.6% 12mma as of May. $^{1}$

## Main points:

1. On-budget fiscal revenue growth rose to $+8.7\%$ yoy in June from $+6.6\%$ yoy in May (Exhibit 1) amid higher PPI inflation and mixed activity growth, as faster tax revenue growth (to +10.8% yoy in June from +6.8% yoy in May) more than offset slower non-tax revenue growth (to +2.9% yoy from +5.6% yoy). The May-to-June improvement in year-on-year tax revenue growth was led by corporate income tax and individual income tax, while VAT and consumption tax revenue growth slowed. Year-on-year growth in stamp duty on stock trading remained strong at +145.3% in June (vs. +145.9% in May), though it only accounted for 1.2% of total tax revenue in 2025.

2. Year-on-year growth in on-budget fiscal expenditure rebounded to +4.0% in June from -1.6% in May, as faster spending growth in agriculture & water conservancy, social security & employment, and urban & rural community affairs more than offset slower spending growth in science & technology, although it remained below fiscal revenue growth. Based on our estimates, growth in infrastructure-related on-budget fiscal spending $^{2}$ rose to -1.8% yoy in June from -12.0% yoy in May, which, together with still-subdued infrastructure investment growth (to -9.4% yoy in June from -11.2% yoy in May), points to persistent weakness in some off-budget financing channels.

3. Property-related government revenue weakened further in June — year-on-year contraction in off-budget land sales revenue widened to -42.1% in June from -35.8% in May, and on-budget property-related tax revenue growth fell to -12.3% yoy from -2.6% yoy (Exhibit 2). $^{3}$ Combining these two items, we estimate that government revenue directly from the property sector contracted 31.6% yoy in June (vs. -23.9% yoy in May). Despite recent green shoots in home transactions in some large cities, most property activity indicators such as land sales, new home starts and property investment were weaker than market expectations in H1. We now expect land sales revenue to decline by around 20% yoy this year, given the prolonged property downturn (especially for construction activity) and still-stretched funding conditions for many developers.

4. Taking into consideration the general public budget and government-managed fund budget, we estimate year-on-year growth in total government revenue slowed to +1.8% in June from +2.4% in May, and the year-on-year contraction in total government expenditure widened to -12.0% from -3.9%. Further incorporating more off-budget financing channels, our proprietary “augmented fiscal deficit” (AFD) metric continued to narrow in June, on both a 3-month and 12-month moving average basis (Exhibit 3). Although our proprietary measure of the fiscal “spend-through” ratio (which is based on 12-month moving average) and the year-on-year change in the outstanding amount of fiscal deposits pointed to slightly faster government spending of previously raised funds in June (Exhibit 4), the meaningful tightening of our AFD metric suggests fiscal policy became a growth drag in Q2, on the back of falling land sales revenue and shrinking policy bank support. We estimate the negative fiscal impulse contributed more than 40% of the sequential decline in real GDP growth from Q1 to Q2 (Exhibit 5).

5. In the first half of 2026, on-budget fiscal revenue grew $4.7\%$ yoy (vs. $-1.7\%$ yoy in 2025), exceeding the MOF's full-year budget projection of a $2.2\%$ yoy gain thanks to a notable improvement in tax revenue growth amid higher global energy prices and domestic PPI inflation, while anecdotal evidence suggests that some local governments, under financial strain, have collected tax revenues more aggressively. On-budget fiscal expenditure only rose by 1.5% yoy in H1 2026 (vs. +1.0% yoy in 2025), well below the budget projection for full-year 2026 of a 4.4% yoy increase. Off the budget, government-managed fund revenue declined by 21.6% yoy in H1 2026 (vs. -7.0% yoy in 2025), mainly weighed on by the 31.5% yoy contraction in land sales revenue (-14.7% yoy in 2025) and implying the budget projection of a 0.6% yoy gain this year will likely be missed. Accordingly, government-managed fund expenditure also declined by 16.4% yoy in H1 2026 (vs. +11.3% yoy in 2025), with year-on-year growth slowed meaningfully in Q2 vs. Q1.

6. Onboarding the negative fiscal impulse in Q2, we recently lowered our 2026 full-year AFD forecast by 0.5pp of GDP to $11.5\%$ (vs. $11.0\%$ in 2025). After weaker-than-expected Q2 GDP, we expect policymakers to strengthen easing rhetoric and pledge to accelerate implementation of already-planned demand-side measures in the upcoming July Politburo meeting, while maintaining their strategic focus on high-tech sectors and key supply chains. However, resilient exports and a still-achievable full-year growth target suggest limited urgency for broad-based, sizable near-term stimulus. We expect central and local governments to accelerate bond issuance and proceeds spending in coming months, speed up implementation of the RMB800bn new policy-based financial instrument, and leave the door open for additional easing later this year if needed. Key risks are central-level complacency and local-level implementation constraints during political turnover ahead of next year's $21^{st}$ Party Congress, in our view.

## Lisheng Wang

Exhibit 1: Fiscal revenue growth continued to outperform spending growth in June  
![](images/901097c51cb31e6dba071dbe8bf2e7c8c554299a2fe6701edc911df2f85da157.jpg)  
Source: Wind, Data compiled by GS Global Investment Research

Exhibit 2: Property-related government revenue weakened further in June  
![](images/11cb9ea8e9d7daa89f2b24fd2908110eb9b420c0cdab4d8b35c864942d75501e.jpg)  
Source: Wind, Data compiled by GS Global Investment Research

Exhibit 3: Our augmented fiscal deficit (AFD) metric continued to narrow in June  
![](images/9922ddf77d7539253c3c5d7102ca89dec5ad4b2fdf24dcabc19e5ae5c8383917.jpg)  
Source: Wind, CEIC, GS Global Investment Research

Exhibit 4: China's fiscal "spend-through" ratio rose in June on a 12mma basis  
![](images/625d3236969011abe21dfab0123d3d36036dc8476a9804c05f89b3575ff7434c.jpg)  
Shaded areas refer to periods when China's year-to-date real GDP growth was equal to or below the full-year growth target. Note that the Chinese government did not set a national growth target for 2020.  
Source: MOF, Wind, CEIC, GS Global Investment Research

Exhibit 5: Fiscal impulse turned negative in Q2, while we expect it to turn positive in H2  
![](images/8d6984db8601929628b46f8b376e9664eaa2f25e26868352b25f2ff186e68ee2.jpg)  
Source: GS Global Investment Research

## The China Economics Team

Andrew Tilton  
+852-2978-1802  
andrew.tilton@gs.com  
GS (Asia) L.L.C.

Hui Shan  
+852-2978-6634  
hui.shan@gs.com  
GS (Asia) L.L.C.

Lisheng Wang +852-3966-4004 lisheng.wang@gs.com GS (Asia) L.L.C.

## Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

Yuting Yang  
+852-2978-7283  
yuting.y.yang@gs.com  
GS (Asia) L.L.C.

Chelsea Song

+852-2978-0106

chelsea.song@gs.com

GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Lisheng Wang, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Lisheng Wang GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant information and disclosures can be found at this link:

https://www.goldmansachs.com/worldwide/india/research-analyst. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no responsibility for any investment decisions that may be taken by a client or any other person based on this research report. Singapore: GS (Singapore) Pte. (Company Number: 198602165W), which is regulated by the Monetary Authority of Singapore, accepts legal responsibility for this research, and should be contacted with respect to any matters arising from, or in connection with, this research. Taiwan: This material is for reference only and must not be reprinted without permission. Investors should carefully consider their own investment risk. Investment results are the responsibility of the individual investor. United Kingdom: Persons who would be categorized as retail clients in the United Kingdom, as such term is defined in the rules of the Financial Conduct Authority, should read this research in conjunction with prior GS on the covered companies referred to herein and should refer to the risk warnings that have been sent to them by GS International. A copy of these risks warnings, and a glossary of certain financial terms used in this report, are

available from GS International on request.

European Union and United Kingdom: Disclosure information in relation to Article 6 (2) of the European Commission Delegated Regulation (EU) (2016/958) supplementing Regulation (EU) No 596/2014 of the European Parliament and of the Council (including as that Delegated Regulation is implemented into Unit

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
