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
# India: Higher exports, higher imports, wider deficit

FY27 CA deficit is likely at 2.4% of GDP, with a large BOP deficit. Additional measures to manage the BOP are on the way.

India's April trade deficit widened to a larger-than-expected USD28.4bn (Consensus: USD26.0bn), driven by higher import and resilient export growth, the latter similar to the experience in other Asian economies. Meanwhile, stable import growth could signal resilient domestic demand, although we believe price effects could be exaggerating the rise. Services trade surplus remained robust at USD20.6bn in April vs USD21.0bn in March, with strong export growth (13.4% y-o-y vs 7.3% in March).

# April trade deficit widens

In the second month of the Iran war, India's merchandise trade deficit widened to USD28.4bn in April from USD20.7bn in March, above expectations (Consensus: USD26.0bn, NOM: USD25.5bn, Figure 1). Price effects have ballooned both the export and the import bill, but the breakdown shows that the wider deficit was mainly led by higher imports. In contrast, exports held up, despite trade disruptions (higher insurance and shipping costs).

# What has driven the exports pickup?

Export growth surged to 13.8% y-o-y in April from -7.4% in March, significantly above expectations (NOM: -4.4%), reflecting not just higher prices, but also an incremental pick-up in volume growth (Figure 2). Electronics posted the strongest growth in exports (40.3% y-o-y), reflecting higher prices and volume share gain in smartphone assembly, while the strength in petroleum products and chemical exports largely reflects price effects, in our view. In contrast, textiles and gems & jewellery export growth continued to contract, with the latter likely weighed down by slower shipments to the Persian Gulf (Figures 3 and 4).

Partially available geographical break-up of exports shows that while export growth to key markets like the US and select European partners remains weak, exports to China/HK, Singapore, and Vietnam have remained strong (Figure 5). Exports to Middle East destinations like Saudi Arabia and UAE continued to contract, but at a slower pace than in March.

# Import growth drivers

Import growth rose to $10.0\%$ y-o-y in April from $-6.5\%$ in March, above expectations (NOM: $-5.0\%$ ). Oil imports contracted on a y-o-y basis, but picked up sequentially, as higher cost of imported oil likely more than offset the drop in volumes. Gold imports surged $(81.7\%$ y-o-y), despite media reports that gold shipments were stuck at customs owing to administrative delays from ambiguity on taxation.

Core import growth also posted strong growth of $15.4\%$ y-o-y in April from $10.2\%$ in March, which we estimate reflects, both price and volume effects (Figure 6). That said, it seems that the pick-up in core import growth has been primarily driven by consumer goods, particularly electronics, while investment/industrial goods growth continued to moderate (Figure 7). Supply bottlenecks also weighed on imports of chemicals.

# NOM view: More BOP measures are on the way

The resilience of exports in April is in line with the strength in other Asian economies, and NOM's leading index of Asian exports points to continued pickup. Meanwhile, stable import growth signals resilient domestic demand, although we believe price effects could be exaggerating the rise. In our baseline, we expect the current account deficit to average $2.4\%$ of GDP in FY27, and weak capital inflows suggest the balance of payment is tracking a deficit of $\sim$ USD70bn. On the policy front, the government has imposed curbs on

# Research Analysts

# Asia Economics

Sonal Varma - NSL

sonal.varma@NOM.com

+65 6433 6527

Aurodeep Nandi - NFASL

aurodeep.nandi@NOM.com

+91 22 4037 4087

gold imports, and raised retail prices of petrol/diesel to reduce the current account deficit (CAD). We expect more measures to manage the BOP pressures in the coming days.

Fig. 1: Trade at a glance 

<table><tr><td>% y-o-y</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td>Exports</td><td>1.1</td><td>0.4</td><td>-0.8</td><td>-7.4</td><td>13.8</td></tr><tr><td>Oil</td><td>-12.3</td><td>5.7</td><td>-40.2</td><td>5.7</td><td>34.7</td></tr><tr><td>Non-oil/gems &amp; jewellery</td><td>3.4</td><td>2.0</td><td>6.6</td><td>-7.5</td><td>10.4</td></tr><tr><td>Imports</td><td>10.3</td><td>19.8</td><td>25.0</td><td>-6.5</td><td>10.0</td></tr><tr><td>Oil</td><td>5.9</td><td>-0.3</td><td>9.0</td><td>-35.9</td><td>-10.0</td></tr><tr><td>Gems &amp; jewellery</td><td>14.2</td><td>242.2</td><td>182.9</td><td>-17.8</td><td>51.1</td></tr><tr><td>Non-oil/gems &amp; jewellery</td><td>11.1</td><td>2.5</td><td>14.0</td><td>10.2</td><td>15.4</td></tr><tr><td>Trade balance (USD bn)</td><td>-26.2</td><td>-34.8</td><td>-27.1</td><td>-20.7</td><td>-28.4</td></tr><tr><td colspan="6">Sequential momentum (% m-o-m, seasonally adjusted)</td></tr><tr><td>Exports</td><td>-10.8</td><td>-0.9</td><td>-1.2</td><td>-5.9</td><td>21.8</td></tr><tr><td>Oil</td><td>0.2</td><td>2.1</td><td>-32.0</td><td>57.1</td><td>47.8</td></tr><tr><td>Non-oil/gems &amp; jewellery</td><td>-10.3</td><td>0.5</td><td>0.8</td><td>-14.2</td><td>22.7</td></tr><tr><td>Imports</td><td>2.7</td><td>13.8</td><td>-11.3</td><td>-11.5</td><td>30.6</td></tr><tr><td>Oil</td><td>4.4</td><td>-3.5</td><td>-8.4</td><td>-17.7</td><td>60.9</td></tr><tr><td>Non-oil/gems &amp; jewellery</td><td>0.1</td><td>2.8</td><td>-0.3</td><td>-1.7</td><td>12.0</td></tr><tr><td>Trade balance (sa, USD bn)</td><td>-28.0</td><td>-37.3</td><td>-29.4</td><td>-24.0</td><td>-34.3</td></tr></table>

Source: CEIC and NOM Global Economics

Fig. 2: Core export growth: price versus volume   
![](images/487242f0a7d5c224f83b08cae0257d688ec19a1fddc1f83dfaa2fba2e0ea4ae5.jpg)

<details>
<summary>line</summary>

| Date   | Export (ex-oil) volume growth | Export (ex-oil) price growth | Export (ex-oil) value growth |
|--------|-------------------------------|------------------------------|------------------------------|
| Apr-21 | 45                            | 10                           | 45                           |
| Apr-22 | 15                            | 5                            | 25                           |
| Apr-23 | -5                            | -5                           | -10                          |
| Apr-24 | 5                             | 5                            | 10                           |
| Apr-25 | 0                             | 5                            | 15                           |
| Apr-26 | -10                           | 10                           | -5                           |
</details>

Source: The World Bank, Ministry of Commerce, CEIC and NOM Global Economics

Fig. 3: Export growth by key categories   
![](images/1628b7e594720f40573b55ebe7cf0ac08fcd6d1ebabe829c2479c6179ec79286.jpg)

<details>
<summary>line</summary>

| Month    | Engineering goods | Chemicals (incl drugs) | Electronic goods | Gems and Jewellery | Textiles |
|----------|-------------------|------------------------|------------------|--------------------|----------|
| Apr-22   | 25                | 15                     | 45               | 10                 | 15       |
| Oct-22   | -10               | -5                     | 60               | -5                 | -10      |
| Apr-23   | -5                | -10                    | 50               | -10                | -15      |
| Oct-23   | 5                 | 0                      | 10               | -20                | -20      |
| Apr-24   | 10                | 20                     | 30               | 0                  | 0        |
| Oct-24   | 20                | 10                     | 55               | -10                | 10       |
| Apr-25   | 10                | 5                      | 45               | -5                 | 5        |
| Oct-25   | 5                 | 10                     | 30               | 0                  | 0        |
| Apr-26   | 10                | 5                      | 15               | -10                | -10      |
</details>

Source: CEIC and NOM Global Economics

Fig. 4: Exports by products 

<table><tr><td>% y-o-y</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td>Exports</td><td>18.6</td><td>1.1</td><td>0.4</td><td>(0.8)</td><td>(7.4)</td><td>13.8</td></tr><tr><td>Oil</td><td>4.5</td><td>(12.3)</td><td>5.7</td><td>(40.2)</td><td>5.7</td><td>34.7</td></tr><tr><td>Non-Oil</td><td>20.3</td><td>3.1</td><td>(0.2)</td><td>6.4</td><td>(9.2)</td><td>9.0</td></tr><tr><td colspan="7">By products</td></tr><tr><td>Agri &amp; allied products</td><td>(1.2)</td><td>(8.2)</td><td>(9.7)</td><td>0.5</td><td>(14.6)</td><td>(1.9)</td></tr><tr><td>Marine products</td><td>15.5</td><td>11.7</td><td>13.3</td><td>13.3</td><td>0.8</td><td>14.7</td></tr><tr><td>Ores &amp; minerals</td><td>46.8</td><td>21.0</td><td>13.0</td><td>(0.9)</td><td>(8.0)</td><td>13.3</td></tr><tr><td>Leather products</td><td>5.9</td><td>(3.8)</td><td>(7.7)</td><td>(4.8)</td><td>(14.4)</td><td>0.4</td></tr><tr><td>Gems &amp; jewellery</td><td>27.8</td><td>(2.1)</td><td>(23.0)</td><td>4.1</td><td>(29.4)</td><td>(7.1)</td></tr><tr><td>Pharmaceuticals</td><td>20.9</td><td>5.7</td><td>1.0</td><td>3.4</td><td>(23.2)</td><td>7.1</td></tr><tr><td>Chemicals</td><td>18.5</td><td>1.1</td><td>(0.2)</td><td>6.9</td><td>(2.0)</td><td>7.3</td></tr><tr><td>Electronic goods</td><td>39.0</td><td>16.8</td><td>0.3</td><td>10.4</td><td>(3.3)</td><td>40.3</td></tr><tr><td>Engineering goods</td><td>23.8</td><td>1.3</td><td>10.4</td><td>12.9</td><td>1.1</td><td>8.8</td></tr><tr><td>Textiles &amp; allied products</td><td>8.5</td><td>0.1</td><td>(3.8)</td><td>(5.0)</td><td>(14.9)</td><td>(4.7)</td></tr><tr><td>Petroleum products</td><td>11.7</td><td>(6.5)</td><td>8.5</td><td>(40.1)</td><td>5.9</td><td>34.7</td></tr><tr><td>Others</td><td>4.9</td><td>(1.3)</td><td>(5.0)</td><td>5.4</td><td>(13.9)</td><td>10.5</td></tr></table>

Source: CEIC and NOM Global Economics

Fig. 5: Exports across select destinations 

<table><tr><td></td><td>European countries*</td><td>US</td><td>China</td><td>UK</td><td>Middle East countries**</td><td>Others</td></tr><tr><td rowspan="5">Months</td><td colspan="6">Share in FY25 (% of total exports)</td></tr><tr><td>11.2</td><td>19.8</td><td>3.3</td><td>3.3</td><td>11.1</td><td>38.0</td></tr><tr><td colspan="6">Share in latest month (% of total exports)</td></tr><tr><td>8.2</td><td>14.5</td><td>4.1</td><td>2.8</td><td>4.7</td><td>41.9</td></tr><tr><td colspan="6">Growth rates (% y-o-y)</td></tr><tr><td>Apr-25</td><td>-36.9</td><td>16.2</td><td>11.1</td><td>-20.3</td><td>7.5</td><td>8.4</td></tr><tr><td>May-25</td><td>-0.7</td><td>14.9</td><td>22.5</td><td>-20.0</td><td>-13.4</td><td>-4.8</td></tr><tr><td>Jun-25</td><td>-10.5</td><td>24.6</td><td>15.4</td><td>-9.5</td><td>-10.5</td><td>-5.3</td></tr><tr><td>Jul-25</td><td>2.4</td><td>27.8</td><td>28.0</td><td>7.8</td><td>14.4</td><td>15.0</td></tr><tr><td>Aug-25</td><td>5.5</td><td>6.6</td><td>21.6</td><td>1.5</td><td>14.3</td><td>7.6</td></tr><tr><td>Sep-25</td><td>-11.6</td><td>-12.6</td><td>33.0</td><td>11.9</td><td>21.3</td><td>18.6</td></tr><tr><td>Oct-25</td><td>-22.5</td><td>-8.5</td><td>41.0</td><td>-27.1</td><td>-9.1</td><td>-1.7</td></tr><tr><td>Nov-25</td><td>4.6</td><td>21.7</td><td>89.3</td><td>15.3</td><td>7.9</td><td>29.2</td></tr><tr><td>Dec-25</td><td>-8.4</td><td>-10.0</td><td>66.5</td><td>-8.4</td><td>0.3</td><td>1.9</td></tr><tr><td>Jan-26</td><td>12.2</td><td>-25.1</td><td>55.3</td><td>-7.9</td><td>23.2</td><td>4.0</td></tr><tr><td>Feb-26</td><td>-10.7</td><td>-12.9</td><td>32.2</td><td>-4.7</td><td>-2.9</td><td>8.9</td></tr><tr><td>Mar-26</td><td>-22.3</td><td>-37.8</td><td>28.1</td><td>-13.5</td><td>-58.3</td><td>0.6</td></tr><tr><td>Apr-26</td><td>-12.3</td><td>-24.7</td><td>27.0</td><td>14.8</td><td>-29.6</td><td>30.9</td></tr></table>

Note: \*Consists of Germany, France, Netherlands and Italy; \*\*Consists of Saudi Arabia and UAE. Source: CEIC and NOM Global Economics

Fig. 6: Core import growth by categories   
![](images/c4ff5000b0897e86c6071965a03e13015cf0c6a58d1302cc8267a0399419a158.jpg)

<details>
<summary>line</summary>

| Date   | Investment/Industrial goods | Consumer goods | Non-agri commodities |
|--------|-----------------------------|----------------|----------------------|
| Apr-23 | (5)                         | (20)           | (35)                 |
| Apr-24 | (10)                        | (10)           | (5)                  |
| Apr-25 | (15)                        | (15)           | (5)                  |
| Apr-26 | (10)                        | (20)           | (15)                 |
</details>

Source: CEIC and NOM Global Economics

Fig. 7: Core import growth: price versus volume   
![](images/dfb559d9d30cc0d9325ad81a40666398665817854fa7252a59d8d035a37ed006.jpg)

<details>
<summary>bar_line</summary>

| Date   | Imports (ex-oil, gold) volume growth | Imports (ex-oil, gold) price growth | Imports (ex-oil, gold) value growth |
|--------|--------------------------------------|-------------------------------------|-------------------------------------|
| Apr-21 | 45                                   | 30                                  | 45                                  |
| Apr-22 | 30                                   | 15                                  | 35                                  |
| Apr-23 | 15                                   | -15                                 | -5                                  |
| Apr-24 | 10                                   | -5                                  | 0                                   |
| Apr-25 | 15                                   | -5                                  | 10                                  |
| Apr-26 | 10                                   | 0                                   | 15                                  |
</details>

Source: The World Bank, Ministry of Commerce, CEIC, and NOM Global Economics

# Appendix A-1

This report has been produced by NOM Singapore Ltd. (NSL), Singapore.

See Disclaimers for NOM Group entity details.

# Analyst Certification

We, Sonal Varma and Aurodeep Nandi, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

# Important Disclosures

# Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

# Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and sUBSidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms a

[中间内容因长度限制已省略]

xchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian Citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are Citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its sUBSidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

# NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved.
"""
