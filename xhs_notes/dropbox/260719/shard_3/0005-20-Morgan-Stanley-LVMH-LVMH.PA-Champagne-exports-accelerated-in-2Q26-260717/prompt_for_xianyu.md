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
LVMH | Europe

# Champagne exports accelerated in 2Q26

## Key Takeaways

Industry data for champagne sales in June has just been published.

In volume (million of bottles), total sales increased +3.8% YoY in June.

The export market, however, was up +8% in volumes YoY in June (up +4% YTD). The champagne export market is dominated by LVMH (\~50% share in value, we estimate).

VA Consensus currently expects Champagne & Wines OSG up+1.4% YoY in 2Q26 after a +5% YoY posted in 1Q26.

This suggests small upside risk to sales in 2Q26 when the Group reports on July 27 (although the impact would be clearly modest within the scope of the Group, <4% of sales).

What's new? The CIVC, the Champagne industry body, has released June figures for the sector.

Bottom line: Overall Champagne volume growth remains anemic so far this year (up only +1% 1H26). However, exports have been accelerating in recent months, up +6.3% YoY in 2Q26 in volume terms. With LVMH generating >80% of its sales in value terms in the export market and dominating the category, this suggests some upside risk to the Champagne & Wines sales vs current consensus estimates for 2Q26.

What the Champagne data says for June: As per the CIVC, Champagne sales by volume were up +4% YoY in June after -1.0% in May and flat in April. YTD total industry volumes are up +1%. Exports were up a solid +8% YoY in June, while shipments domestically declined -2% YoY (vs. -4% in May). Year-to-date, exports are up +4% in volume (with 1Q26 up +3.7% YoY and 2Q26 +6.3% YoY). YTD, sales in volume in France are down -3%, marking the weakest starts to the year in absolute terms for a long time, excluding the Covid-affected year of 2020.

LVMH is very significantly more exposed to the export market: in 2025, we estimate that LVMH shipped \~52m bottles outside France vs only \~8m in France (a \~14% / \~86% split). With a total of 60m bottles shipped in 2025 vs an industry total of 266m, LVMH has a market share in volume terms of \~23%. However, as per our estimates above, LVMH has an export market share in volume terms of \~34% (and thus \~50% in value terms), as per our estimates, as prestige brands such as Veuve Cliquot, Dom Perignon or Ruinart tend to generate a very high share of their worldwide sales outside of France.

For example, as can be seen in Exhibit 9, LVMH dominates the US champagne

<table><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="2">Edouard Aubin</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Edouard.Aubin@morganstanley.com</td><td>+44 20 7425-3160</td></tr><tr><td colspan="2">Grace Smalley, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Grace.Smalley@morganstanley.com</td><td>+44 20 7425-9629</td></tr><tr><td colspan="2">Natasha Bonnet</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Natasha.Bonnet@morganstanley.com</td><td>+44 20 7677-5723</td></tr><tr><td colspan="2">Cedric Norest</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Cedric.Norest@morganstanley.com</td><td>+44 20 7425-1462</td></tr></table>

<table><tr><td colspan="2">Brands | France</td></tr><tr><td>Stock Rating</td><td>Equal-weight</td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td>Price target</td><td>€540.00</td></tr><tr><td>Shr price, close (Jul 16, 2026)</td><td>€503.10</td></tr><tr><td>52-Week Range</td><td>€654.70-440.00</td></tr><tr><td>Mkt cap, curr (mn)</td><td>€250,532</td></tr><tr><td>Net debt (12/26e) (mn)*</td><td>€3,254</td></tr><tr><td>EV, curr (mn)*</td><td>€258,865</td></tr></table>

\* = GAAP or approximated based on GAAP

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>Sales / Revenue(€mn)**</td><td>80,807</td><td>80,542</td><td>85,326</td><td>91,603</td></tr><tr><td>EBIT (€mn)**</td><td>17,755</td><td>17,370</td><td>19,261</td><td>21,001</td></tr><tr><td>EPS (€)**</td><td>22.73</td><td>21.72</td><td>25.74</td><td>28.21</td></tr><tr><td>Prior EPS (€)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>ModelWare EPS (€)</td><td>22.73</td><td>21.72</td><td>25.74</td><td>28.21</td></tr><tr><td>EPS (€)§</td><td>21.44</td><td>22.01</td><td>25.24</td><td>27.67</td></tr><tr><td>P/E**</td><td>28.4</td><td>23.2</td><td>19.5</td><td>17.8</td></tr><tr><td>EV/revenue*</td><td>4.1</td><td>3.2</td><td>2.9</td><td>2.7</td></tr><tr><td>EV/EBIT**</td><td>18.6</td><td>14.7</td><td>13.1</td><td>11.8</td></tr><tr><td>Total dividends pershare (€)</td><td>10.91</td><td>10.42</td><td>12.36</td><td>13.54</td></tr><tr><td>Div yld (%)</td><td>1.7</td><td>2.1</td><td>2.5</td><td>2.7</td></tr><tr><td>FCF yld ratio (%)**</td><td>3.5</td><td>4.5</td><td>5.0</td><td>5.6</td></tr><tr><td>Net debt (€mn)*</td><td>6,856</td><td>3,254</td><td>(1,174)</td><td>(6,207)</td></tr><tr><td>RNOA (%)**</td><td>11.3</td><td>11.7</td><td>12.8</td><td>13.6</td></tr><tr><td>ROE (%)**</td><td>16.8</td><td>16.0</td><td>17.6</td><td>17.6</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
§ = Consensus data is provided by Refinitiv Estimates
\* = GAAP or approximated based on GAAP
e = MS estimates

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

market. According to data recently published by Circana, thanks to Veuve Cliquot and Moet & Chandon's very strong market share in that market, the LVMH Group has a combined market share (in value terms) of about two-thirds. Veuve Clicquot's dominance is especially striking, with the US absorbing roughly 40% of its total production (vs. just 10% for the industry overall).

What the Champagne data says for the full year 2025. As per the CIVC, 266m Champagne bottles were shipped last year and Champagne Houses generated a combined turnover of €5.17bn. This is down -2% from 271.4m bottles shipped in 2024 (with France -4% and Exports down -1%) and marks the third consecutive year of decline.

Trends in the Champagne market in recent years. In recent years, Champagne consumption has been under pressure, as can be seen in the charts below, impacted by a number of cyclical and structural factors, such as: 1) Shifting consumer tastes & behaviors: alcohol consumption is contracting in key markets, particularly among younger demographics, who drink less alcohol overall and are more health-focused; 2) Champagne demand is tied to mood and confidence; weaker consumer confidence in markets such as Europe over the last few years has dampened buying. We note that Champagne consumption in France has been particularly weak over the past few years and that it has remained so YTD in 2026; 3) Competitive alternatives: Sparkling wines like Prosecco have proved resilient and grown their share, often at lower price points, drawing consumers away from Champagne. As per IWSR data, most leading Champagne brands have raised prices very materially over the past five to six years, pricing out the middle consumer (as has happened for the personal luxury goods market more broadly). Partially offsetting these adverse developments, the industry is structurally premiumising, which benefits LVMH (as it owns the majority of the leading prestige brands).

Exhibit 1: Champagne Shipments Growth YoY (in volume)  
![](images/5e2a9b3b455b5f6ed96eb52f801a586e5460c478dadb6dcdec1a8960ebc96a58.jpg)  
Source: CIVC, MS

Exhibit 2: Champagne Exports Growth YoY (in volume)  
![](images/c4ab4cf7f3f9d92071e4050e5257d1717b196620bb2b9ca6040b47ecc584d5ae.jpg)  
Source: CIVC, MS

## Additional Charts

Exhibit 3: Champagne Shipments over time (number of bottles)  
![](images/81a1b0a46482d93f48511c896b922448f21fdcdc6e655944d99da9ddc0dadb5f.jpg)  
Source: Champagne.fr, MS

Exhibit 4: Champagne Turnover (billion euros)  
![](images/1c3b88d267bd7c927d4062591787e34d103b657abe64d37421b8bfc2a39300e0.jpg)  
Source: Champagne.fr, MS

Exhibit 5: LVMH Sales breakdown by division in 2025  
![](images/63ebfdb34556b03f3464607bbbeea10b45c6896cc1834ef1ca57baf96f8af7f6.jpg)  
Source: Company data, MS

Exhibit 6: LVMH EBIT breakdown by division in 2025  
![](images/388180e12aeaa4d013f7f61158df62097208fa16ceeba256b209601424c8f81d.jpg)  
Source: Company data, MS

Exhibit 7:  
Champagne and Wines contribution to LVMH Total Sales & EBIT since 1997  
![](images/2aedd3d9af58c95d37a9f669bee16909e11c9bf5b5fc321fc1b57fbce0c512c2.jpg)  
Source: Company data, MS estimates

Exhibit 8: Wines & Spirits (includes champagne, cognac, etc.) contribution in LVMH Total Sales & EBIT since 1997  
![](images/0f8492487ca77992e49dc3b62703ec1d9b214ca9f1da137dfd6b53bdf9325afe.jpg)  
Source: Company data, MS

Exhibit 9: US Champagne Market Share by Brand in 2025 (in value)  
![](images/6a0e1283f7e94e8a42e110c45d4216f1fb4937f1765cce39b4f62e20951685b7.jpg)  
Source: Circana, MS

## Valuation Methodology and Risks

## LVMH Moet Hennessy Louis Vuitton SA (LVMH.PA)

We use a DCF-based valuation methodology, which we think best reflects LVMH's margin potential and cash flow. We assume a WACC of 8.8% and long-term growth rate of 2.8%.

## Risks to Upside

■ Chinese luxury consumption accelerates more than expected

■ Demand in the West does not contract next year

## Risks to Downside

■ A slowdown in Chinese consumer spending remains the biggest risk for LVMH and peers

■ Vertical integration (mostly downstream) results in operational deleverage

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) and/or MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority. MS & Co. International plc disseminates in the UK research that it has prepared, and which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. As used in this disclosure section, MS includes RMB MS Proprietary Limited, MS Europe S.E., MS & Co International plc and its affiliates.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Edouard Aubin; Natasha Bonnet; Grace Smalley, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Adidas, Avolta AG, Birkenstock Holding plc, Burberry, Ferrari NV, Hermes International S.C.A., Hugo Boss AG, Kering, Moncler SpA, Pandora A/S, PUMA SE.

Within the last 12 months, MS has received compensation for investment banking services from Avolta AG, LVMH Moet Hennessy Louis Vuitton SA, Richemont SA.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Adidas, Avolta AG, Burberry, EssilorLuxottica SA, Ferrari NV, Hermes International S.C.A., Kering, Luxexperience BV, LVMH Moet Hennessy Louis Vuitton SA, Moncler SpA, Pandora A/S, Prada SpA, PUMA SE, Richemont SA, Salvatore Ferragamo Spa. Within the last 12 months, MS has received compensation for products and services other than investment banking services from Adidas, Avolta AG, EssilorLuxottica SA, Ferrari NV, Kering, LVMH Moet Hennessy Louis Vuitton SA, Richemont SA, Salvatore Ferragamo Spa.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Adidas, Avolta AG, Burberry, EssilorLuxottica SA, Ferrari NV, Hermes International S.C.A., Kering, Luxexperience BV, LVMH Moet Hennessy Louis Vuitton SA, Moncler SpA, Pandora A/S, Prada SpA, PUMA SE, Richemont SA, Salvatore Ferragamo Spa.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Adidas, Avolta AG, Burberry, EssilorLuxottica SA, Ferrari NV, Kering, LVMH Moet Hennessy Louis Vuitton SA, Richemont SA, Salvatore Ferragamo Spa.

MS & Co. LLC makes a market in the securities of Ermenegildo Zegna.

MS & Co. International plc is a corporate broker to Burberry.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are

[中间内容因长度限制已省略]

ly. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Brands

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/16/2026)</td></tr><tr><td colspan="3">Edouard Aubin</td></tr><tr><td>Adidas (ADSGn.DE)</td><td>O (04/15/2024)</td><td>€182.95</td></tr><tr><td>Birkenstock Holding plc (BIRK.N)</td><td>E (11/06/2023)</td><td>US$44.31</td></tr><tr><td>Ferrari NV (RACE.N)</td><td>O (06/15/2026)</td><td>US$382.58</td></tr><tr><td>Ferrari NV (RACE.MI)</td><td>O (06/15/2026)</td><td>€334.05</td></tr><tr><td>Hermes International S.C.A. (HRMS.PA)</td><td>E (10/06/2025)</td><td>€1,706.00</td></tr><tr><td>Kering (PRTP.PA)</td><td>E (04/10/2026)</td><td>€255.40</td></tr><tr><td>LVMH Moet Hennessy Louis Vuitton SA (LVMH.PA)</td><td>E (01/19/2026)</td><td>€503.10</td></tr><tr><td>Richemont SA (CFR.S)</td><td>O (02/05/2025)</td><td>SFr 197.40</td></tr><tr><td colspan="3">Grace Smalley, CFA</td></tr><tr><td>Burberry (BRBY.L)</td><td>O (05/18/2026)</td><td>1,121p</td></tr><tr><td>EssilorLuxottica SA (ESLX.PA)</td><td>O (07/05/2023)</td><td>€169.50</td></tr><tr><td>Hugo Boss AG (BOSSn.DE)</td><td>E (07/09/2024)</td><td>€37.90</td></tr><tr><td>Luxexperience BV (LUXE.N)</td><td>E (09/15/2023)</td><td>US$8.09</td></tr><tr><td>Pandora A/S (PNDORA.CO)</td><td>E (01/16/2023)</td><td>DKr 800.60</td></tr><tr><td>PUMA SE (PUMG.DE)</td><td>++</td><td>€29.37</td></tr><tr><td colspan="3">Natasha Bonnet</td></tr><tr><td>Avolta AG (AVOL.S)</td><td>E (04/24/2026)</td><td>SFr 48.68</td></tr><tr><td>Brunello Cucinelli (BCU.MI)</td><td>O (01/27/2026)</td><td>€83.64</td></tr><tr><td>Ermenegildo Zegna (ZGN.N)</td><td>E (02/12/2026)</td><td>US$14.43</td></tr><tr><td>Moncler SpA (MONC.MI)</td><td>E (06/22/2026)</td><td>€52.08</td></tr><tr><td>Prada SpA (1913.HK)</td><td>E (06/29/2026)</td><td>HK$41.16</td></tr><tr><td>Salvatore Ferragamo Spa (SFER.MI)</td><td>U (02/12/2026)</td><td>€10.59</td></tr></table>

\* Historical prices are not split adjusted.  
Stock Ratings are subject to change. Please see latest research for each company.

## © 2026 MS
"""
