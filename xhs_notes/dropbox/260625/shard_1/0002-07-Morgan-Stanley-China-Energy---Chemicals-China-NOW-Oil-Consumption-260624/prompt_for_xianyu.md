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
# China Energy & Chemicals | Asia Pacific

## China NOW: Oil Consumption

## Key Takeaways

China's implied gasoline and diesel demand weakened sharply in May, posting $12\%$ and $21\%$ declines YoY, respectively.

Jet fuel consumption remained resilient, rising roughly $5\%$ YoY, while naphtha consumption was broadly unchanged.

Total oil products consumption declined by 13.5% YoY in May, and down \~12% YoY since SOH disruption.

This suggests that the primary source of demand destruction remains road transportation and infrastructure building activity, rather than aviation or chemical.

We believe the weakness reflects a combination of softer economic activity, slowing infrastructure and logistics demand, and accelerating substitution toward EV-dominated shared-mobility - high oil prices likely encouraged consumers to shift mobility toward electric vehicles and public transit, further intensifying structural pressure on traditional transport fuel consumption.

Exhibit 1: China monthly fuel consumption (including inventory movement)  
![](images/c506111aefe9a8fda2656195607f66e55a30eb38dabf8628f8a3dec796958580.jpg)

![](images/85eb30a1c800fa7fc831362bae4c88a85889f02272fd602ad7f76e2599847379.jpg)  
Source: CEIC, China Customs, Oilchem, MS

Exhibit 2: China fuel inventory and refiner run-rates: fuel inventory has been elevated since SOH disruptions despite significant run-rate cuts at refiners

![](images/4e038d614d1dc22b7997d92b82c94c543490548fd5a405915277a8aa91af13ad.jpg)  
Source: Oilchem, SCI, MS

![](images/1d18a6e003a221c8e5cbe2307138ab39096b99d55c561b4813d9e1c781a6eb00.jpg)

MS ASIA LIMITED+

Jack Lu

Equity Analyst

Jack.Lu@morganstanley.com

+852 2848-5044

Kaylee Xu  
Equity Analyst  
Kaylee.Xu@morganstanley.com +852 2239-1506

![](images/184d92ab7be3f95eeb2e73f4ba6166f7f5c28767dece3e16b1202b478373161f.jpg)

Asia Summer School 2026

CHINA ENERGY & CHEMICALS

Asia Pacific

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Jack Lu; Kaylee Xu.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: China Oilfield Services Ltd., Contemporary Amperex Technology Co. Ltd., EVE Energy Co Ltd, PetroChina, Shandong Sinocera Functional Material, Shenzhen Senior Technology Material Co, Sunresin New Materials Co Ltd.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Bluestar Adisseo Co, Contemporary Amperex Technology Co. Ltd.. Within the last 12 months, MS has received compensation for investment banking services from Bluestar Adisseo Co, Contemporary Amperex Technology Co. Ltd..

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Bluestar Adisseo Co, China Petroleum & Chemical Corp., Contemporary Amperex Technology Co. Ltd., EVE Energy Co Ltd, Hengli Petrochemical Co Ltd, Ningbo Ronbay New Energy Technology, REPT Battero Energy Co, Rongsheng Petrochemical Co Ltd, Shanghai Putailai New Energy Tech Co Ltd, Shenzhen Senior Technology Material Co, Wanhua Chemical, Yunnan Energy New Material Co Ltd, Zhejiang NHU Co. Ltd..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from China Petroleum & Chemical Corp., CNOOC, PetroChina, Wanhua Chemical.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Bluestar Adisseo Co, China Petroleum & Chemical Corp., Contemporary Amperex Technology Co. Ltd., EVE Energy Co Ltd, Hengli Petrochemical Co Ltd, Ningbo Ronbay New Energy Technology, REPT Battero Energy Co, Rongsheng Petrochemical Co Ltd, Shanghai Putailai New Energy Tech Co Ltd, Shenzhen Senior Technology Material Co, Wanhua Chemical, Yunnan Energy New Material Co Ltd, Zhejiang NHU Co. Ltd..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: China Petroleum & Chemical Corp., CNOOC, PetroChina, Wanhua Chemical.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report. Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

## (as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td rowspan="2">Stock Rating Category</td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment Services Clients (MISC)</td></tr><tr><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of Rating Category</td><td>Count</td><td>% of Total Other MISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td><td>16%</td><td>201</td><td>12%</td></tr><tr><td>Total</td><td>3,667</td><td></td><td>920</td><td></td><td></td><td>1632</td><td></td></tr></table>

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

## Important Disclosures for MS Smith Barney LLC Customers

Important disclosures regarding any material conflict of interest that can reasonably be expected to have influenced MS Smith Barney LLC's choice of a third-party research provider or the subject company of a third-party research report, are available on the MS Wealth Management disclosure website at www.morganstanley.com/online/researchdisclosures. For MS specific disclosures, you may refer to https://www.morganstanley.com/eqr/disclosures/webapp/generalresearch.

Each MS report is reviewed and approved on behalf of MS Smith Barney LLC. This review and approval is conducted by the same person who reviews the research report on behalf of MS. This could create a conflict of interest.

## Other Important Disclosures

MS policy is to update research reports as and when the Research Analyst and Research Management deem appropriate, based on developments with the issuer, the sector, or the market that may have a material impact on the research views or opinions stated therein. In addition, certain Research publications are intended to be updated on a regular periodic basis (weekly/monthly/quarterly/annual) and will 

[中间内容因长度限制已省略]

n nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: China Energy & Chemicals

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/23/2026)</td></tr><tr><td>Jack Lu</td><td></td><td></td></tr><tr><td>Bluestar Adisseo Co (600299.SS)</td><td></td><td>Rmb9.43</td></tr><tr><td>China Oilfield Services Ltd. (2883.HK)</td><td>E (03/28/2026)</td><td>HK$6.71</td></tr><tr><td>China Oilfield Services Ltd. (601808.SS)</td><td>U (03/28/2026)</td><td>Rmb11.60</td></tr><tr><td>China Petroleum &amp; Chemical Corp. (600028.SS)</td><td>E (08/19/2024)</td><td>Rmb4.73</td></tr><tr><td>China Petroleum &amp; Chemical Corp. (0386.HK)</td><td>O (07/29/2025)</td><td>HK$4.11</td></tr><tr><td>CNOOC (0883.HK)</td><td>O (03/17/2021)</td><td>HK$21.90</td></tr><tr><td>Contemporary Amperex Technology Co. Ltd. (300750.SZ)</td><td>O (06/25/2025)</td><td>Rmb392.51</td></tr><tr><td>Contemporary Amperex Technology Co. Ltd. (3750.HK)</td><td>O (05/04/2026)</td><td>HK$704.00</td></tr><tr><td>EVE Energy Co Ltd (300014.SZ)</td><td>E (05/31/2022)</td><td>Rmb67.28</td></tr><tr><td>Gotion High Tech Co Ltd (002074.SZ)</td><td>E (04/17/2023)</td><td>Rmb29.55</td></tr><tr><td>Guangzhou Tinci Materials Technology Co (002709.SZ)</td><td>E (01/08/2026)</td><td>Rmb54.04</td></tr><tr><td>Hengli Petrochemical Co Ltd (600346.SS)</td><td>++</td><td>Rmb18.17</td></tr><tr><td>Ningbo Ronbay New Energy Technology (688005.SS)</td><td>U (10/27/2025)</td><td>Rmb33.96</td></tr><tr><td>Ningxia Baofeng Energy Group Co., Ltd. (600989.SS)</td><td>E (04/15/2026)</td><td>Rmb21.91</td></tr><tr><td>PetroChina (601857.SS)</td><td>O (08/19/2024)</td><td>Rmb9.41</td></tr><tr><td>PetroChina (0857.HK)</td><td>O (03/17/2021)</td><td>HK$8.94</td></tr><tr><td>REPT Battero Energy Co (0666.HK)</td><td>E (10/20/2025)</td><td>HK$13.92</td></tr><tr><td>Rongsheng Petrochemical Co Ltd (002493.SZ)</td><td>E (07/29/2025)</td><td>Rmb11.81</td></tr><tr><td>Shanghai Putailai New Energy Tech Co Ltd (603659.SS)</td><td>U (10/27/2025)</td><td>Rmb29.15</td></tr><tr><td>Shenzhen Senior Technology Material Co (300568.SZ)</td><td>E (01/08/2026)</td><td>Rmb18.94</td></tr><tr><td>Yunnan Energy New Material Co Ltd (002812.SZ)</td><td>O (10/27/2025)</td><td>Rmb68.81</td></tr><tr><td colspan="3">Kaylee Xu</td></tr><tr><td>Jiangsu Cnano Technology Co Ltd (688116.SS)</td><td>U (03/10/2025)</td><td>Rmb38.89</td></tr><tr><td>Jiangsu Yangnong Chemical (600486.SS)</td><td>O (06/12/2026)</td><td>Rmb55.43</td></tr><tr><td>Shandong Sinocera Functional Material (300285.SZ)</td><td>E (03/23/2026)</td><td>Rmb90.78</td></tr><tr><td>Shenzhen Capchem Technology Co Ltd (300037.SZ)</td><td>E (06/07/2023)</td><td>Rmb88.00</td></tr><tr><td>Sunresin New Materials Co Ltd (300487.SZ)</td><td>E (10/25/2024)</td><td>Rmb58.50</td></tr><tr><td>Wanhua Chemical (600309.SS)</td><td>O (04/10/2026)</td><td>Rmb72.80</td></tr><tr><td>Zhejiang NHU Co. Ltd. (002001.SZ)</td><td>E (01/26/2026)</td><td>Rmb29.75</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
