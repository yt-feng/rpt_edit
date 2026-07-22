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
NATURAL GAS ANALYST

# Slower Hormuz Export Ramp Leads Us to Raise Our Near-Term TTF Forecast

As uncertainty in the Middle East remains high, we now assume a further delayed normalization of Persian Gulf LNG exports (Oct26, vs Jul26 prev.). The resulting tightening of European gas balances, and in particular Europe's increased vulnerability to a cold shock in the winter, raises the risk that TTF might need to rise to 65 EUR/MWh, the threshold that we have observed disincentivizes Asian LNG demand more visibly, heading into the winter. As a result, we see TTF approaching this threshold and sustaining such elevated prices in the coming months, and we raise our Bal3Q26/4Q26 TTF forecasts to 60/53 EUR/MWh from 41/40 EUR, close to forwards currently at 58/57 EUR/MWh.

Risks to our near-term TTF forecast remain skewed to the upside and we continue to recommend that gas users hedge their exposure to winter European gas and LNG price spikes. Specifically, in a scenario where Middle East energy exports normalize only gradually through 2027, we estimate that Dec26 TTF would likely need to move above 100 EUR/MWh, 110% above our 50 EUR/MWh base case, to discourage Asia LNG demand. In contrast, we estimate that a faster-than-expected ramp of Hormuz flows would allow TTF to sell off back in line with the coal-to-gas switching threshold of 40 EUR/MWh, 20% below our current Dec26 TTF price base case.

\- Longer term, we maintain our bearish 2028/29 TTF view at 19/16 EUR/MWh (vs forwards at 29/25) - although it is important to emphasize that Hormuz being fully open for shipping is a key underlying assumption of our view. Further out in the forecast horizon, we see risks to this price view skewed to the downside. Recent FIDs of new US LNG export projects signal a larger and longer-lasting LNG oversupply vs what we already embed in our balances. In addition, a potential pick up in coal and renewable generation in the aftermath of the Iran conflict might reduce Asia's appetite for natural gas demand in the coming years vs our base case.

Samantha Dart
+1(212)357-9428 |
samantha.dart@gs.com
GS & Co. LLC

Laura Cyr
+1(212)902-3435 | laura.x.cyr@gs.com
GS & Co. LLC

## Slower Hormuz Export Ramp Leads Us to Raise Our Near-Term TTF Forecast

Following the recent escalation in hostilities in the Middle East, we now assume a later normalization of Persian Gulf LNG exports (Oct26) vs previously (Jul26) (Exhibit 1 and Exhibit 2). We estimate that this net 16 mtpa (4%) reduction in balance-of-summer global LNG supply will leave North West Europe end-Oct26 (start of winter) gas storage near 67% full (vs our previous expectations of 74%) and end-Mar27 (end of winter) at 28% full, assuming 10-year average temperatures through the season (Exhibit 3 and Exhibit 4). Importantly, these estimates already take into account a marginal 4 mtpa downward revision to our average Asia demand expectations for the remainder of summer to 262 mtpa owing to higher LNG prices.

Exhibit 1: Visible LNG exports via the Strait of Hormuz have halted...  
![](images/84e0c0d8b7421b4be722a08473276c40b91ff3ec4722a0784dca2c538f420faf.jpg)  
Source: Kpler, GS Global Investment Research

Exhibit 2: ...leading us to assume a slower ramp of Qatari LNG exports  
![](images/b8eda9751bf0b0fb3e1c2e18c45a5970aa4e1135762ed151bfc47c8dc670ca04.jpg)  
Source: Kpler, GS Global Investment Research

Exhibit 3: With Asia LNG demand back up yoy, at least during peak summer...
Global LNG net imports (4wma)  
![](images/ea8d4b3cba1985f2d910d1dd2b81cf909c64335873b72a1738145b80812252c9.jpg)  
Source: Kpler, GS Global Investment Research

Exhibit 4: ...NW Europe will stay tight, with end-summer storage likely the lowest in at least 14 years
NW European underground gas storage  
![](images/e8b5d24a3583fc46f52fdf26c59c625dbd7aeb7825d9646d73c6ff9b2aff697c.jpg)  
Source: Bloomberg, GS Global Investment Research

To be clear, ending winter at 28% full is not an issue. The issue might arise if 28% full is the storage estimate assuming average winter weather, and winter ends up being significantly colder than average. Specifically, we estimate that a

two-standard-deviation colder-than-average winter typically raises gas demand enough to lower end-winter storage fill by 24 pp.

With our estimated tightness in winter gas balances in Europe leaving little room for error, we expect that, for the remainder of this summer, TTF will price very close to the 65 EUR/MWh threshold (or above, for a bigger tightening shock) that we think destroys Asia industrial demand for gas more visibly. Once winter starts to materialize, from November, barring a colder-than-average shock, we expect that the TTF risk premium will gradually moderate. On net, this leads us to raise our Bal3Q26/4Q26/2027 TTF forecasts to 60/53/31 EUR/MWh from 41/40/30 EUR.

## Risks to Our Near-Term TTF Forecast Remain Skewed to The Upside...

In a scenario where Middle East energy exports normalize only gradually through 2027, we estimate that Dec26 TTF would likely need to move above 100 EUR/MWh (\$35/mmBtu), 110% above our 50 EUR/MWh base case, to discourage Asia LNG demand and manage European gas storage levels away from a stockout $^{1}$ . Importantly, this upside to prices assumes 10-year average weather. Under a colder-than-average winter, TTF would likely spike significantly more to destroy further demand and limit the weather-driven incremental drawdown in gas storage.

In contrast, we estimate that a faster-than-expected ramp of Hormuz flows would allow TTF to sell off back in line with the gas-to-coal switching threshold of 40 EUR/MWh, 20% below our current Dec26 TTF price base case. A warmer-than-average winter would likely remove the need for gas-to-coal switching, and hence the 40 EUR/MWh TTF floor, potentially bringing forward the 30 EUR/MWh type of price we expect to see on average in 2027.

As a result, we continue to recommend that gas users hedge their exposure to winter European gas and LNG price spikes (Exhibit 5).

Exhibit 5: Risks to our near-term TTF forecasts remain skewed to the upside  
![](images/2992c04cd5976fa31875f56eaa108be427cb9d04f45d0d82e0b7d5208d6790be.jpg)  
Forwards as of July 17th.

<table><tr><td></td><td>GS TTF Base Case - Flow normalized in Oct 2026</td><td>Price Upside Scenario - Only gradual flow normalization by Oct 2027</td><td>Price Downside Scenario - Normalized flows by mid-Jul, faster NFE start</td></tr><tr><td>Bal 3Q26</td><td>60</td><td>78</td><td>46</td></tr><tr><td>4Q26</td><td>53</td><td>102</td><td>40</td></tr><tr><td>Bal 2026</td><td>56</td><td>92</td><td>43</td></tr><tr><td>2027</td><td>31</td><td>65</td><td>30</td></tr></table>

Source: ICE, GS Global Investment Research

...While Risks to Our Bearish Long-Term TTF view Are Skewed to The Downside Longer term, we maintain our bearish 2028/29 TTF view at 19/16 EUR/MWh (vs forwards at 29/25) - although it's important to emphasize that Hormuz being fully open for shipping is a key underlying assumption of our view.

Further, we see risks to this view skewed to the downside. Recent FIDs of new US LNG export projects signal a larger and longer-lasting LNG oversupply vs what we already embed in our balances. In addition, a potential pick up in coal and renewable generation in the aftermath of the Iran conflict might reduce Asia's appetite for natural gas demand in the coming years vs our base case.

Appendix  
Exhibit 6: We raise our near-term TTF and JKM forecasts
TTF and JKM GS forecasts vs forwards

<table><tr><td></td><td>GS TTF fcast. (EUR/MWh)</td><td>Previous</td><td>TTF fwrd. (EUR/MWh)</td><td>GS TTF fcast. TTF ($/mmBtu)</td><td>Previous</td><td>GS JKM fcast. ($/mmBtu)</td><td>Previous</td><td>JKM fwrd. ($/mmBtu)</td></tr><tr><td>Bal 3Q26</td><td>60</td><td>41</td><td>58</td><td>20.15</td><td>13.95</td><td>21.65</td><td>15.45</td><td>20.90</td></tr><tr><td>4Q26</td><td>53</td><td>40</td><td>57</td><td>17.90</td><td>13.75</td><td>18.90</td><td>14.75</td><td>20.20</td></tr><tr><td>1Q27</td><td>40</td><td>38</td><td>54</td><td>13.55</td><td>12.95</td><td>14.40</td><td>13.80</td><td>18.50</td></tr><tr><td>2Q27</td><td>31</td><td>31</td><td>40</td><td>10.55</td><td>10.55</td><td>11.30</td><td>11.30</td><td>14.00</td></tr><tr><td>3Q27</td><td>27</td><td>27</td><td>38</td><td>9.05</td><td>9.20</td><td>9.80</td><td>9.95</td><td>13.45</td></tr><tr><td>4Q27</td><td>25</td><td>25</td><td>37</td><td>8.40</td><td>8.50</td><td>9.15</td><td>9.25</td><td>13.30</td></tr><tr><td>Bal 2026</td><td>56</td><td>41</td><td>57</td><td>18.80</td><td>13.85</td><td>20.00</td><td>15.05</td><td>20.50</td></tr><tr><td>2027</td><td>31</td><td>30</td><td>42</td><td>10.40</td><td>10.30</td><td>11.15</td><td>11.10</td><td>14.80</td></tr><tr><td>2028</td><td>19</td><td>19</td><td>29</td><td>6.40</td><td>6.50</td><td>6.80</td><td>6.90</td><td>10.55</td></tr><tr><td>2029</td><td>16</td><td>16</td><td>25</td><td>5.45</td><td>5.50</td><td>5.65</td><td>5.70</td><td>9.20</td></tr><tr><td>2030</td><td>20</td><td>20</td><td>23</td><td>6.65</td><td>6.75</td><td>6.90</td><td>7.00</td><td>8.65</td></tr><tr><td>2031</td><td>21</td><td>21</td><td>23</td><td>7.05</td><td>7.15</td><td>7.35</td><td>7.45</td><td>8.85</td></tr><tr><td>2032</td><td>21</td><td>21</td><td>23</td><td>7.05</td><td>7.15</td><td>7.50</td><td>7.60</td><td>9.05</td></tr><tr><td>2033</td><td>32</td><td>32</td><td>24</td><td>10.75</td><td>10.90</td><td>11.35</td><td>11.50</td><td>9.30</td></tr><tr><td>2034</td><td>42</td><td>42</td><td>24</td><td>14.10</td><td>14.30</td><td>15.20</td><td>15.40</td><td>9.60</td></tr><tr><td>2035</td><td>42</td><td>42</td><td>25</td><td>14.10</td><td>14.30</td><td>15.30</td><td>15.50</td><td>9.90</td></tr></table>

Forwards as of July 17th. Our TTF forecasts in \$/mmBtu might fluctuate owing to FX shifts since we last published, as illustrated by the recent weakening of the Euro. Bal 3Q26 averages Aug26-Sep26 contracts. Bal 2026 averages Aug26-Dec26 contracts.  
Source: ICE, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Samantha Dart and Laura Cyr, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Samantha Dart GS & Co. LLC, Laura Cyr GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant information and disclosures can be found at this link:

https://www.goldmansachs.com/worldwide/india/research-analyst. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no responsibility for any investment decisions that may be taken by a client or any other person based on this research report. Singapore: GS (Singapore) Pte. (Company Number: 198602165W), which is regulated by the Monetary Authority of Singapore, accepts legal responsibility for this research, and should be contacted with respect to any matters arising from, or in connection with, this research. Taiwan: This material is for reference only and must not be reprinted without permission. Investors should carefully

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
