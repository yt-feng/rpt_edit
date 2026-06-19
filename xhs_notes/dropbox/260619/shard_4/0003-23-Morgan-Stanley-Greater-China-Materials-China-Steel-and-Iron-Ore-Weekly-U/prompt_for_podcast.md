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
## Greater China Materials | Asia Pacific

# China Steel and Iron Ore Weekly Update

## Key Takeaways

\- Apparent consumption of long products rose 5.1% WoW, while that of flat products grew 2.0% WoW.

Weekly output increased for long products and flat products; inventory dipped at traders, but inched up at mills. Utilization rates rose at electric arc furnaces (EAF).

Iron ore inventory declined at mills: Operating rates improved, along with daily output.

Iron ore shipments: Combined shipments from Australia and Brazil were up by 0.59 Mt WoW for the period 8th June to 14th June. Shipments from Australia were down by (1.64) Mt WoW. Shipments from Brazil were up by 2.24 Mt WoW.

Exhibit 1: Weekly data summary

<table><tr><td colspan="4">Steel</td><td colspan="3">Iron Ore</td></tr><tr><td></td><td>Volume (kt) / rate (%)</td><td>WoW</td><td>YoY</td><td></td><td>Volume (kt) / rate (%)</td><td>WoW</td></tr><tr><td>Inventory - Traders</td><td>11,259</td><td>-0.6%</td><td>23.3%</td><td>Inventory - Ports</td><td>157,070</td><td>0.7%</td></tr><tr><td>Inventory - Mills</td><td>4,311</td><td>0.7%</td><td>1.3%</td><td>Inventory - Per Mill</td><td>225</td><td>-1.2%</td></tr><tr><td>Weekly Consumption - Long</td><td>3,069</td><td>5.1%</td><td>-0.3%</td><td>Operating rate</td><td>62.9%</td><td>0.8 ppts</td></tr><tr><td>Weekly Consumption - Flat</td><td>5,643</td><td>2.0%</td><td>-2.1%</td><td>Average daily output</td><td>397</td><td>1.2%</td></tr><tr><td>Weekly Output - Long</td><td>3,058</td><td>2.7%</td><td>2.9%</td><td>Shipments - Australia</td><td></td><td>-1.64Mt</td></tr><tr><td>Weekly Output - Flat</td><td>5,622</td><td>0.5%</td><td>-1.6%</td><td>Shipments - Brazil</td><td></td><td>+2.24Mt</td></tr><tr><td>Utilization - 247 mills</td><td>90.3%</td><td>0.1 ppts</td><td>(0.5 ppts)</td><td></td><td></td><td></td></tr><tr><td>Utilization - EAF</td><td>64.4%</td><td>2.0 ppts</td><td>7.7 ppts</td><td></td><td></td><td></td></tr></table>

Source: Mysteel, MS. Note: EAF = electric arc furnace.

Exhibit 2: Weekly steel demand  
![](images/66982753339c034314327607ad8d9d4f21af7ff16f8d8338fd0d156dd96b378f.jpg)

<details>
<summary>line chart</summary>

| Month | 2023 Long | 2024 Long | 2022 Long | 2025 Long | 2026 Long | 2022 Flat (RHS) | 2023 Flat (RHS) | 2024 Flat (RHS) | 2025 Flat (RHS) |
|-------|-----------|-----------|-----------|-----------|-----------|-----------------|-----------------|-----------------|-----------------|
| Jan   | ~350      | ~400      | ~400      | ~350      | ~350      | ~350            | ~350            | ~350            | ~350            |
| Feb   | ~100      | ~100      | ~100      | ~100      | ~100      | ~100            | ~100            | ~100            | ~100            |
| Mar   | ~450      | ~450      | ~450      | ~450      | ~450      | ~450            | ~450            | ~450            | ~450            |
| Apr   | ~450      | ~450      | ~450      | ~450      | ~450      | ~450            | ~450            | ~450            | ~450            |
| May   | ~450      | ~450      | ~450      | ~450      | ~450      | ~450            | ~450            | ~450            | ~450            |
| Jun   | ~450      | ~450      | ~450      | ~450      | ~450      | ~450            | ~450            | ~450            | ~450            |
| Jul   | ~450      | ~450      | ~450      | ~450      | ~450      | ~450            | ~450            | ~450            | ~450            |
| Aug   | ~450      | ~450      | ~450      | ~450      | ~450      | ~450            | ~450            | ~450            | ~450            |
| Sep   | ~450      | ~450      | ~450      | ~450      | ~450      | ~450            | ~450            | ~450            | ~450            |
| Oct   | ~350      | ~350      | ~350      | ~350      | ~350      | ~350            | ~350            | ~350            | ~350            |
| Nov   | ~350      | ~350      | ~350      | ~350      | ~350      | ~350            | ~350            | ~350            | ~350            |
| Dec   | ~350      | ~350      | ~350      | ~350      | ~350      | ~350            | ~350            | ~350            | ~350            |
</details>

Source: Mysteel, MS

MS ASIA LIMITED+

## Rachel L Zhang

Equity Analyst

Rachel.Zhang@morganstanley.com +852 2239-1520

## Hannah Yang, CFA

Equity Analyst

Hannah.Yang1@morganstanley.com +852 2239-7079

## Chris Jiang

Equity Analyst

Chris.Jiang@morganstanley.com +852 3963-1593

## Cynthia Tang

Research Associate

Cynthia.Tang@morganstanley.com +852 3963-4360

MS & CO. INTERNATIONAL PLC+

## Amy Gower (Amy Sergeant), CFA

Commodities Strategist

Amy.Gower1@morganstanley.com +44 20 7677-6937

## Asia Summer School 2026

![](images/06ea02084db86dd28faf84d31e3cb249462fb0d9b055d82ca16f18bf694a57b2.jpg)

## GREATER CHINA MATERIALS

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Amy Gower (Amy Sergeant), CFA; Chris Jiang; Hannah Yang, CFA; Rachel L. Zhang.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Aluminum Corp. of China Ltd., Anhui Honglu Steel Construction, Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Flat Glass Group Co Ltd, Ganfeng Lithium Co. Ltd., GEM Co Ltd, Jiangxi Copper, JL Mag Rare-Earth Co. Ltd, Shandong Gold Mining Co. Ltd, Shenzhen Kedali Industry Co Ltd, Sinomine Resource Group Co Ltd, Tianqi Lithium Industries Inc., Zijin Mining Group.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of CNGR Advanced Material Co., Ltd., Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for investment banking services from Zijin Mining Group.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from China Jushi, China Steel Corp., CMOC Group Ltd, Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Mining Group.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: China Jushi, China Steel Corp., CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Gold International, Zijin Mining Group.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td><td>16%</td><td>201</td><td>12%</td></tr><tr><td>Total</td><td>3,667</td><td></td><td>920</td><td></td><td></td><td>1632</td><td></td></tr></table>

Data include common stock and ADRs currently assigned ratings. Investment Banking Clients are companies from whom MS received investment banking compensation in the last 12 months. Due to rounding off of decimals, the percentages provided in the "% of total" column may not add up to exactly 100 percent.

## Analyst Stock Ratings

Overweight (O). The stock's total return is expected to exceed the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Equal-weight (E). The stock's total return is expected to be in line with the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Not-Rated (NR). Currently the analyst does not have adequate conviction about the stock's total return relative to the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Underweight (U). The stock's total return is expected to be below the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Unless otherwise specified, the time frame for price targets included in MS is 12 to 18 months.

## Analyst Industry Views

Attractive (A): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be attractive vs. the relevant broad market benchmark, as indicated below.

In-Line (I): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be in line with the relevant broad market benchmark, as indicated below. Cautious (C): The analyst views the performance of his or her industry coverage universe over the next 12-18 months with caution vs. the relevant broad market benchmark, as indicated below. Benchmarks for each region are as follows: North America - S&P 500; Latin America - relevant MSCI country index or MSCI Latin America Index; Europe - MSCI Europe; Japan - TOPIX; Asia - relevant MSCI country index or MSCI sub-regional index or MSCI AC Asia Pacific ex Japan Index.

## Important Disclosures for MS Smith Barne

[中间内容因长度限制已省略]

ysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Greater China Materials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/18/2026)</td></tr><tr><td colspan="3">Chris Jiang</td></tr><tr><td>Anhui Honglu Steel Construction (002541.SZ)</td><td>U (12/16/2025)</td><td>Rmb16.60</td></tr><tr><td>CGN Mining Co Ltd (1164.HK)</td><td>O (01/18/2023)</td><td>HK$2.90</td></tr><tr><td>Chengxin Lithium Group Co. Ltd. (002240.SZ)</td><td>E (12/16/2025)</td><td>Rmb45.74</td></tr><tr><td>GEM Co Ltd (002340.SZ)</td><td>U (04/20/2026)</td><td>Rmb7.42</td></tr><tr><td>Shenzhen Kedali Industry Co Ltd (002850.SZ)</td><td>O (08/21/2023)</td><td>Rmb203.81</td></tr><tr><td>Sinomine Resource Group Co Ltd (002738.SZ)</td><td>O (12/16/2025)</td><td>Rmb60.71</td></tr><tr><td>Yongxing Special Materials Technology (002756.SZ)</td><td>E (11/25/2022)</td><td>Rmb61.15</td></tr><tr><td>Zhejiang Huayou Cobalt Co Ltd (603799.SS)</td><td>O (10/08/2025)</td><td>Rmb52.10</td></tr><tr><td colspan="3">Hannah Yang, CFA</td></tr><tr><td>China Hongqiao Group (1378.HK)</td><td>O (09/15/2023)</td><td>HK$22.74</td></tr><tr><td>Chuangxin Industries Holdings Ltd. (2788.HK)</td><td>O (03/19/2026)</td><td>HK$16.68</td></tr><tr><td>Flat Glass Group Co Ltd (6865.HK)</td><td>O (07/30/2020)</td><td>HK$7.00</td></tr><tr><td>Flat Glass Group Co Ltd (601865.SS)</td><td>O (07/30/2020)</td><td>Rmb10.63</td></tr><tr><td>MMG Ltd (1208.HK)</td><td>O (12/16/2024)</td><td>HK$8.25</td></tr><tr><td>Shandong Pharmaceutical Glass Co. Ltd. (600529.SS)</td><td>U (04/20/2026)</td><td>Rmb18.55</td></tr><tr><td>Shenhuo Coal and Power (000933.SZ)</td><td>O (09/02/2025)</td><td>Rmb23.74</td></tr><tr><td>Tianshan Aluminum (002532.SZ)</td><td>O (03/19/2026)</td><td>Rmb12.05</td></tr><tr><td>Xinyi Glass Holding Limited (0868.HK)</td><td>U (05/14/2024)</td><td>HK$9.22</td></tr><tr><td>Zhongfu Shenying Carbon Fiber Co Ltd (688295.SS)</td><td>O (08/25/2023)</td><td>Rmb51.15</td></tr><tr><td colspan="3">Rachel L Zhang</td></tr><tr><td>Aluminum Corp. of China Ltd. (601600.SS)</td><td>O (11/30/2020)</td><td>Rmb9.38</td></tr><tr><td>Aluminum Corp. of China Ltd. (2600.HK)</td><td>O (11/30/2020)</td><td>HK$8.55</td></tr><tr><td>Baoshan Iron &amp; Steel (600019.SS)</td><td>O (01/16/2016)</td><td>Rmb5.68</td></tr><tr><td>Beijing New Building Materials (000786.SZ)</td><td>O (04/09/2024)</td><td>Rmb19.72</td></tr><tr><td>Beijing Oriental Yuhong Waterproof Techn (002271.SZ)</td><td>E (09/25/2024)</td><td>Rmb12.13</td></tr><tr><td>China Jushi (600176.SS)</td><td>O (12/22/2020)</td><td>Rmb53.50</td></tr><tr><td>China Lesso Group Holdings Ltd (2128.HK)</td><td>U (10/08/2025)</td><td>HK$4.00</td></tr><tr><td>China Steel Corp. (2002.TW)</td><td>U (12/16/2025)</td><td>NT$19.10</td></tr><tr><td>CMOC Group Ltd (3993.HK)</td><td>O (09/24/2019)</td><td>HK$18.87</td></tr><tr><td>CMOC Group Ltd (603993.SS)</td><td>O (06/21/2024)</td><td>Rmb20.04</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (300919.SZ)</td><td>E (01/12/2026)</td><td>Rmb48.64</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (2579.HK)</td><td>O (01/12/2026)</td><td>HK$28.84</td></tr><tr><td>FangDa Carbon New Material Co. Ltd. (600516.SS)</td><td>U (12/16/2024)</td><td>Rmb5.82</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (002460.SZ)</td><td>O (04/20/2026)</td><td>Rmb69.36</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (1772.HK)</td><td>O (12/16/2025)</td><td>HK$56.00</td></tr><tr><td>Henan Liliang Diamond Co. Ltd (301071.SZ)</td><td>U (04/20/2026)</td><td>Rmb76.60</td></tr><tr><td>Jiangsu Dingsheng New Materials (603876.SS)</td><td>U (04/20/2026)</td><td>Rmb25.35</td></tr><tr><td>Jiangxi Copper (0358.HK)</td><td>O (10/08/2025)</td><td>HK$41.06</td></tr><tr><td>Jiangxi Copper (600362.SS)</td><td>O (10/08/2025)</td><td>Rmb53.31</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (6680.HK)</td><td>O (04/23/2025)</td><td>HK$19.40</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (300748.SZ)</td><td>O (04/23/2025)</td><td>Rmb33.43</td></tr><tr><td>Nine Dragons Paper (2689.HK)</td><td>E (01/04/2023)</td><td>HK$6.85</td></tr><tr><td>Shandong Gold Mining Co. Ltd (600547.SS)</td><td>O (04/23/2025)</td><td>Rmb26.91</td></tr><tr><td>Shandong Gold Mining Co. Ltd (1787.HK)</td><td>O (12/12/2024)</td><td>HK$21.46</td></tr><tr><td>Shandong Nanshan Aluminium Co. (600219.SS)</td><td>O (11/30/2020)</td><td>Rmb4.53</td></tr><tr><td>Tianqi Lithium Industries Inc. (9696.HK)</td><td>O (12/16/2025)</td><td>HK$43.80</td></tr><tr><td>Tianqi Lithium Industries Inc. (002466.SZ)</td><td>O (04/20/2026)</td><td>Rmb62.18</td></tr><tr><td>Weixing New Building Materials (002372.SZ)</td><td>U (10/08/2025)</td><td>Rmb8.64</td></tr><tr><td>Zhaojin Mining Industry (1818.HK)</td><td>O (06/21/2024)</td><td>HK$19.77</td></tr><tr><td>Zijin Gold International (2259.HK)</td><td>O (11/06/2025)</td><td>HK$109.60</td></tr><tr><td>Zijin Mining Group (2899.HK)</td><td>O (11/06/2025)</td><td>HK$32.08</td></tr><tr><td>Zijin Mining Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb29.69</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.
"""
