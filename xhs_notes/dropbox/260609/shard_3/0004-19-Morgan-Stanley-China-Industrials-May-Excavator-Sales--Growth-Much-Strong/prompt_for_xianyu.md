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
## China Industrials | Asia Pacific

# May Excavator Sales: Growth Much Stronger than Feared

May-26 sales grew 36% YoY (-14% MoM, 5M26 +25% YoY). Domestic sales grew 39% YoY in May (5M26 +18% YoY), driven by front-loaded LGSB issuance and replacement demand for electric models. OEM price hikes (including Sany, XCMG, and Liugong), effective from mid-May to June, should support margin recovery. Exports remained resilient at +34% YoY (5M26 +33% YoY), despite the Middle East conflict and rising fuel prices, driven by ongoing market share gains across multiple regions, including Europe, LatAm, and Africa.

We remain positive on the global construction machinery upcycle. After meetings with Sany and Zoomlion last week, we came away positive on their 2Q26 outlook. Sany guides to c.20% YoY top-line growth on overseas demand, a better excavator mix, and stable pricing. Zoomlion expects improving growth as FX drag eases and overseas momentum broadens.

Exhibit 1: China excavator sales volume

<table><tr><td rowspan="2"></td><td colspan="3">May</td><td colspan="2">5M26</td></tr><tr><td>Sales volume (units)</td><td>YoY</td><td>MoM</td><td>Sales volume (units)</td><td>YoY</td></tr><tr><td>Total China excavator sales</td><td>24,794</td><td>36%</td><td>-14%</td><td>126,875</td><td>25%</td></tr><tr><td>Domestic sales</td><td>11,628</td><td>39%</td><td>-31%</td><td>68,127</td><td>18%</td></tr><tr><td>Export sales</td><td>13,166</td><td>34%</td><td>11%</td><td>58,748</td><td>33%</td></tr></table>

Source: China Construction Machinery Association (CCMA), MS.

Exhibit 2: China's monthly excavator sales volume vs. Sany Heavy's share price  
![](images/f4b19e8a90a6b8649e243ec7e0b45f2be309e32bb157632580b2b963acf5d4af.jpg)

<details>
<summary>line chart</summary>

| Date       | Monthly China excavator sales volume (LHS) | Sany stock price (RHS) |
| ---------- | ------------------------------------------ | ---------------------- |
| 2/1/2005   | ~0                                         | ~0                     |
| 2/1/2006   | ~5,000                                     | ~5                     |
| 2/1/2007   | ~10,000                                    | ~10                    |
| 2/1/2008   | ~15,000                                    | ~15                    |
| 2/1/2009   | ~20,000                                    | ~20                    |
| 2/1/2010   | ~30,000                                    | ~30                    |
| 2/1/2011   | ~45,000                                    | ~40                    |
| 2/1/2012   | ~35,000                                    | ~35                    |
| 2/1/2013   | ~25,000                                    | ~25                    |
| 2/1/2014   | ~15,000                                    | ~15                    |
| 2/1/2015   | ~10,000                                    | ~10                    |
| 2/1/2016   | ~15,000                                    | ~15                    |
| 2/1/2017   | ~20,000                                    | ~20                    |
| 2/1/2018   | ~35,000                                    | ~35                    |
| 2/1/2019   | ~45,000                                    | ~45                    |
| 2/1/2020   | ~55,000                                    | ~55                    |
| 2/1/2021   | ~85,000                                    | ~45                    |
| 2/1/2022   | ~35,000                                    | ~35                    |
| 2/1/2023   | ~25,000                                    | ~25                    |
| 2/1/2024   | ~30,000                                    | ~35                    |
| 2/1/2025   | ~35,000                                    | ~45                    |
| 2/1/2026   | ~35,000                                    | ~45                    |
</details>

Source: CCMA, FactSet, MS.

MS ASIA LIMITED+

## Sheng Zhong

Equity Analyst

Sheng.Zhong@morganstanley.com +852 2239-7821

## Carlos Chai

Research Associate

Carlos.Chai@morganstanley.com +852 3963-3180

## Chelsea Wang

Equity Analyst

Jinlin.Wang@morganstanley.com +852 2239-1118

## Asia Summer School 2026

![](images/0224626bf85bd166691880b02a8fce15a33c79b6191613fe27916f1b3571ac2d.jpg)

## CHINA INDUSTRIALS

Asia Pacific

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Valuation Methodology and Risks

## Zoomlion Heavy Industry (000157.SZ)

Our H-share valuation is based on 13x 2026e P/E. We think this multiple is appropriate, in line with the average of 13x P/E over 2017-26. We apply a 20% A-H premium to derive our PT for the A-shares, implying 18x A-share P/E for 2026.

## Risks to Upside

■ Stronger-than-expected replacement demand from emissions standard upgrade.  
■ Stronger demand for excavators and aerial work platform products.

## Risks to Downside

■ Lower-than-expected infrastructure and property investment growth.  
■ Lower-than-expected overseas demand.

## Zoomlion Heavy Industry (1157.HK)

Our H-share valuation is based on 13x P/E (previously 12x) 2026e EPS excluding FX losses. We think this multiple is appropriate, as it is in line with the average P/E over 2017-26 of 13x. FX losses are a near-term impact and are largely priced in by the market.

## Risks to Upside

■ Stronger-than-expected replacement demand from emissions standard upgrade.  
■ Stronger demand for excavators and aerial work platform products.

## Risks to Downside

■ Lower-than-expected infrastructure and property investment growth.  
■ Lower-than-expected overseas demand.

## Sany Heavy Industry Co., Ltd. (600031.SS)

Base case, derived from P/E methodology. We apply a target multiple of 23x to our 2026e EPS excl. FX loss estimate. We think this multiple is appropriate, as it is in line with Sany's average \~23x P/E multiple during the domestic construction machinery upcycle in 2016-17. FX losses are a near-term impact and are largely priced in by the market.

## Risks to Upside

■ Stronger-than-expected bargaining power amid market competition.  
■ Stronger-than-expected infrastructure and property construction activities.  
■ Faster-than-expected overseas penetration.

## Risks to Downside

■ Lower-than-expected infrastructure and property investment growth.  
■ Weaker-than-expected bargaining power with intensifying competition.  
■ Weaker-than-expected sales performance in overseas developing markets.

## Jiangsu Hengli Hydraulic Co.Ltd (601100.SS)

Our price target is derived by 1) applying a 35x 2026e P/E multiple to its core business (excl. FX impact); and 2) using DCF for the humanoid robot parts business, discounting 2025-50e cash flows at a WACC of 11% and applying a terminal growth rate of 4%. Combining both yields a price target of Rmb133.

## Risks to Upside

■ Stronger-than-expected excavator and pumps & valves demand.  
■ Notable penetration into foreign brands' supply chain.  
■ Faster-than-expected humanoid robots penetration and market share gain in the supply chain.

## Risks to Downside

■ Sharp decline in excavator and pumps & valves demand in China.  
■ Failure to expand its share in non-excavator parts.  
■ Slower-than-expected humanoid robot penetration.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Carlos Chai; Chelsea Wang; Sheng Zhong.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of April 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Beijing Geekplus Technology Co., Ltd., China Railway Group, DR Laser, Sany Heavy Industry Co., Ltd., Shenzhen Envicool Technology Co Ltd, Shenzhen SC New Energy Technology Corp, Suzhou Maxwell Technologies Co Ltd, WeiChai Power, Wuxi Autowell Technology Co Ltd, Wuxi Lead Intelligent, Zhejiang Dingli Machinery Co Ltd., Zhejiang Shuanghuan Driveline Co. Ltd., Zoomlion Heavy Industry.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Beijing Geekplus Technology Co., Ltd., Zoomlion Heavy Industry.

Within the last 12 months, MS has received compensation for investment banking services from Shenzhen Inovance Technology, Zoomlion Heavy Industry.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Beijing Geekplus Technology Co., Ltd., China State Construction Engineering, Sany Heavy Industry Co., Ltd., Shenzhen Inovance Technology, Wuxi Lead Intelligent, Zhejiang Hangke Technology, Zoomlion Heavy Industry.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from China State Construction Engineering, CRRC Corp Ltd, Haitian International Holdings Limited, Sinotruk (Hong Kong) Limited.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Beijing Geekplus Technology Co., Ltd., China State Construction Engineering, Sany Heavy Industry Co., Ltd., Shenzhen Inovance Technology, Wuxi Lead Intelligent, Zhejiang Hangke Technology, Zoomlion Heavy Industry.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Beijing Geekplus Technology Co., Ltd., China State Construction Engineering, CRRC Corp Ltd, Haitian International Holdings Limited, Sinotruk (Hong Kong) Limited.

An employee, director or consultant of MS is a director of Beijing Geekplus Technology Co., Ltd.. This person is not a research analyst or a member of a research analyst's household. The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's deci

[中间内容因长度限制已省略]

 without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Industrials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/05/2026)</td></tr><tr><td>Chelsea Wang</td><td></td><td></td></tr><tr><td>China Railway Group (601390.SS)</td><td>E (05/12/2022)</td><td>Rmb4.69</td></tr><tr><td>China Railway Group (0390.HK)</td><td>E (08/11/2025)</td><td>HK$3.64</td></tr><tr><td>China State Construction Engineering (601668.SS)</td><td>U (08/11/2025)</td><td>Rmb4.72</td></tr><tr><td>Han's Laser (002008.SZ)</td><td>O (10/02/2025)</td><td>Rmb127.87</td></tr><tr><td>Hefei Meyer Optoelectronic Technology (002690.SZ)</td><td>E (09/08/2025)</td><td>Rmb15.00</td></tr><tr><td>iRay Technology Company Limited (688301.SS)</td><td>E (01/16/2025)</td><td>Rmb173.25</td></tr><tr><td>Neway Valve (Suzhou) Co., Ltd (603699.SS)</td><td>O (09/12/2025)</td><td>Rmb57.81</td></tr><tr><td>Shanghai BOCHU Electronic Technology (688188.SS)</td><td>O (08/22/2024)</td><td>Rmb157.13</td></tr><tr><td>Shenzhen Envicool Technology Co Ltd (002837.SZ)</td><td>O (08/19/2024)</td><td>Rmb65.90</td></tr><tr><td colspan="3">Sheng Zhong</td></tr><tr><td>Beijing Geekplus Technology Co., Ltd. (2590.HK)</td><td>O (08/07/2025)</td><td>HK$14.99</td></tr><tr><td>Centre Testing International Group (300012.SZ)</td><td>E (11/18/2024)</td><td>Rmb14.34</td></tr><tr><td>CRRC Corp Ltd (1766.HK)</td><td>U (01/22/2026)</td><td>HK$5.30</td></tr><tr><td>CRRC Corp Ltd (601766.SS)</td><td>U (01/22/2026)</td><td>Rmb5.66</td></tr><tr><td>DR Laser (300776.SZ)</td><td>E (12/17/2021)</td><td>Rmb170.16</td></tr><tr><td>Estun Automation Co Ltd (002747.SZ)</td><td>U (06/30/2022)</td><td>Rmb31.02</td></tr><tr><td>Haitian International Holdings Limited (1882.HK)</td><td>E (09/08/2025)</td><td>HK$20.68</td></tr><tr><td>Hongfa Technology Co Ltd (600885.SS)</td><td>O (05/23/2023)</td><td>Rmb33.32</td></tr><tr><td>Jiangsu Guomao Reducer Co Ltd (603915.SS)</td><td>U (01/08/2025)</td><td>Rmb16.43</td></tr><tr><td>Jiangsu Hengli Hydraulic Co.Ltd (601100.SS)</td><td>O (05/23/2023)</td><td>Rmb117.20</td></tr><tr><td>Jingsheng Mechanical &amp; Electrical Co (300316.SZ)</td><td>U (01/08/2025)</td><td>Rmb48.89</td></tr><tr><td>Leader Harmonious Drive Systems (688017.SS)</td><td>O (01/22/2026)</td><td>Rmb393.00</td></tr><tr><td>Sany Heavy Industry Co., Ltd. (600031.SS)</td><td>O (01/08/2025)</td><td>Rmb18.65</td></tr><tr><td>Shenzhen Inovance Technology (300124.SZ)</td><td>++</td><td>Rmb75.08</td></tr><tr><td>Shenzhen SC New Energy Technology Corp (300724.SZ)</td><td>U (09/08/2025)</td><td>Rmb74.51</td></tr><tr><td>Sinotruk (Hong Kong) Limited (3808.HK)</td><td>E (05/19/2025)</td><td>HK$41.58</td></tr><tr><td>Suzhou Maxwell Technologies Co Ltd (300751.SZ)</td><td>U (09/15/2023)</td><td>Rmb229.51</td></tr><tr><td>Times Electric (3898.HK)</td><td>E (01/22/2026)</td><td>HK$39.64</td></tr><tr><td>WeiChai Power (2338.HK)</td><td>O (03/30/2026)</td><td>HK$37.96</td></tr><tr><td>WeiChai Power (000338.SZ)</td><td>O (03/30/2026)</td><td>Rmb31.12</td></tr><tr><td>Wuxi Autowell Technology Co Ltd (688516.SS)</td><td>U (09/08/2025)</td><td>Rmb58.34</td></tr><tr><td>Wuxi Lead Intelligent (300450.SZ)</td><td>O (09/08/2025)</td><td>Rmb46.98</td></tr><tr><td>Zhejiang Dingli Machinery Co Ltd. (603338.SS)</td><td>O (11/05/2025)</td><td>Rmb52.40</td></tr><tr><td>Zhejiang Hangke Technology (688006.SS)</td><td>O (09/08/2025)</td><td>Rmb31.66</td></tr><tr><td>Zhejiang Shuanghuan Driveline Co. Ltd. (002472.SZ)</td><td>O (08/25/2023)</td><td>Rmb42.86</td></tr><tr><td>Zoomlion Heavy Industry (1157.HK)</td><td>O (09/08/2025)</td><td>HK$7.70</td></tr><tr><td>Zoomlion Heavy Industry (000157.SZ)</td><td>O (09/08/2025)</td><td>Rmb7.52</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.
"""
