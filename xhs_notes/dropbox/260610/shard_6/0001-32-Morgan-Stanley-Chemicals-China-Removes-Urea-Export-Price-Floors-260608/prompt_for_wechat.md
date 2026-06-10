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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 8, 2026 12:39 PM GMT

## Chemicals | North America

# China Removes Urea Export Price Floors

Trade sources are reporting that China has now removed the export price floors it set on May 27 for its initial 3mm mt of urea exports. While this is not overly surprising given that global prices have moved well below these floors, it represents an important data point, in our view, because the alternative would have suggested China was tactically looking to limit exports strategically but max cash generation for its local urea producers.

We believe that China has been selective with both urea and DAP/MAP exports in recent years given potential (and now real) supply disruptions from various geopolitical conflicts (first Russia/Ukraine and now Iran). This has created local oversupply, which in turn has provided extremely low prices for Chinese farmers, but limited profits and cash flows for local Chinese fertilizer companies. Price floors could have limited exports versus the 3mm mt quota but maxed cash flow for producers while strategically keeping higher inventory in country.

There had been some concern in the markets that China would remain guarded with urea exports until the Strait of Hormuz had reopened and it was possible the institution of price floors was related to that. However, the price floors are now gone and the SOH remains closed at present.

As always, Chinese fertilizer export policy is subject to change, so we will stay closely tuned here. The next important development for markets is whether Chinese MAP/DAP exports resume in August. Given continued dislocations in sulfur markets - and not just SOH related (i.e., Russia further reducing exports in recent weeks), we believe resumption of exports in August is harder to call at present and likely much more reliant on improvement in both sulfur availability and costs.

China initially put urea exports price floors at \$660 mt FOB (prilled) and \$670 mt FOB (granular), with a separate floor of \$680 mt FOB for any prills sold to India. The removal of price floors is ahead of the close of the most recent India tender, though it is still not clear how much China is participated in the event.

Small Favor – Vote for us in the Extel (fka Institutional Investor) poll! If you find this report helpful, please consider voting for Vincent Andrews as a five-star Chemicals analyst in this year's Extel poll. Please also vote for team members Steven Haynes, Turner Hinrichs and Justin Pellegrino in Chemicals. If you need a ballot, please let us know. We really appreciate your support.

MS & CO. LLC

## Vincent Andrews

Equity Analyst

Vincent.Andrews@morganstanley.com

+1 212 761-3293

MS & CO. INTERNATIONAL PLC+

## Lisa H De Neve

Equity Analyst

Lisa.De.Neve@morganstanley.com

+44 20 7677-0250

MS & CO. LLC

## Justin T Pellegrino

Research Associate

Justin.Pellegrino@morganstanley.com

+1 212 761-4054

![](images/81ab461620ee4f12ec7200b82bec674da921f81dc6e4e6c9338cb0497641cb89.jpg)

<details>
<summary>text_image</summary>

2026 EXTEL
ALL-AMERICA
RESEARCH POLL
VIEW OUR
ANALYSTS >
May 26 – June, 12 2026
</details>

## CHEMICALS

North America

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Vincent Andrews; Lisa H De Neve.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of April 30, 2026, MS beneficially owned $1\%$ or more of a class of common equity securities of the following companies covered in MS: Air Products and Chemicals Inc., Albemarle Corporation, Celanese Corp., CF Industries, Chemours Co, Corteva Inc., Dow Inc., DuPont De Nemours Inc., Eastman Chemical Co, Ecolab Inc., FMC Corporation, Huntsman Corp, International Flavors & Fragrances, Intrepid Potash, Linde PLC, LyondellBasell Industries N.V., Mosaic Company, Nutrien Ltd, Olin Corp., PPG Industries Inc., RPM International Inc., Sherwin-Williams Co., Tronox Holdings Plc-Class A.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Celanese Corp., Chemours Co, Eastman Chemical Co, Ecolab Inc., LyondellBasell Industries N.V., PPG Industries Inc..

Within the last 12 months, MS has received compensation for investment banking services from Avient Corporation, Celanese Corp., Chemours Co, Corteva Inc., Eastman Chemical Co, Ecolab Inc., Huntsman Corp, International Flavors & Fragrances, LyondellBasell Industries N.V., PPG Industries Inc..

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Air Products and Chemicals Inc., Albemarle Corporation, Ashland Inc., Avient Corporation, Axalta Coating Systems Ltd, Celanese Corp., Chemours Co, Corteva Inc., DuPont De Nemours Inc., Eastman Chemical Co, Ecolab Inc., Huntsman Corp, ICL Group Ltd, International Flavors & Fragrances, Linde PLC, LyondellBasell Industries N.V., Olin Corp., PPG Industries Inc., RPM International Inc., Sherwin-Williams Co., Westlake Corp.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Albemarle Corporation, Ashland Inc., Avient Corporation, Axalta Coating Systems Ltd, Celanese Corp., CF Industries, Chemours Co, Corteva Inc., DuPont De Nemours Inc., Eastman Chemical Co, Ecolab Inc., FMC Corporation, Huntsman Corp, ICL Group Ltd, International Flavors & Fragrances, Linde PLC, LyondellBasell Industries N.V., Mosaic Company, Nutrien Ltd, PPG Industries Inc., Westlake Corp.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Air Products and Chemicals Inc., Albemarle Corporation, Ashland Inc., Avient Corporation, Axalta Coating Systems Ltd, Celanese Corp., Chemours Co, Corteva Inc., DuPont De Nemours Inc., Eastman Chemical Co, Ecolab Inc., Huntsman Corp, ICL Group Ltd, International Flavors & Fragrances, Linde PLC, LyondellBasell Industries N.V., Olin Corp., PPG Industries Inc., RPM International Inc., Sherwin-Williams Co., Westlake Corp.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Albemarle Corporation, Ashland Inc., Avient Corporation, Axalta Coating Systems Ltd, Celanese Corp., CF Industries, Chemours Co, Corteva Inc., DuPont De Nemours Inc., Eastman Chemical Co, Ecolab Inc., FMC Corporation, Huntsman Corp, ICL Group Ltd, International Flavors & Fragrances, Linde PLC, LyondellBasell Industries N.V., Mosaic Company, Nutrien Ltd, PPG Industries Inc., RPM International Inc., Sherwin-Williams Co., Westlake Corp.

MS & Co. LLC makes a market in the securities of Ashland Inc., Avient Corporation, Celanese Corp., Chemours Co, Eastman Chemical Co, Ecolab Inc., Huntsman Corp, International Flavors & Fragrances, RPM International Inc., Tronox Holdings Plc-Class A, Westlake Corp.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment Services Clients (MISC)</td></tr><tr><td>Stock Rating Category</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of Rating Category</td><td>Count</td><td>% of Total Other MISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td><td>16%</td><td>201</td><td>12%</td></tr><tr><td>Total</td><td>3,667</td><td></td><td>920</td><td></td><td></td><td>1632</td><td></td></tr></table>

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

MS policy is to update research reports as and when the Research Analyst and Research Management deem appropriate, based on developments with the issuer, the sector, or the market that may have a material impact on the research views or opinions stated therein. In addition, certain Research publications are intended to be updated on a regular periodic basis (weekly/monthly/quarterly/annual) and will ordinarily be updated with that frequency, unless the Research Analyst and Research Management determine that a different publication schedule is appropriate based on current conditions.

MS is not acting as a municipal advisor and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of Section 975 of the Dodd-Frank Wall Street Reform and Consumer Protection Act.

MS produces an equity research product called a "Tactical Idea." Views contained in a "Tactical Idea" on a particular stock may be contrary to the recommendations or views expressed in research on the same stock. This may be the result of differing time horizons, methodologies, market events, or other factors. For all research available on a particular stock, please contact your sales representative or go to Matrix at http://www.morganstanley.com/matrix.

MS is provided to our clients through our proprietary research portal on Matrix and also distributed electronically by MS to clients. Certain, but not all, MS products are also ma

[中间内容因长度限制已省略]

Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Chemicals

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/05/2026)</td></tr><tr><td>Lisa H De Neve</td><td></td><td></td></tr><tr><td>ICL Group Ltd (ICL.N)</td><td>E (01/05/2024)</td><td>$5.60</td></tr><tr><td>International Flavors &amp; Fragrances (IFF.N)</td><td>O (11/11/2024)</td><td>$73.01</td></tr><tr><td>Steven K Haynes, CFA</td><td></td><td></td></tr><tr><td>Ashland Inc. (ASH.N)</td><td>E (09/08/2025)</td><td>$56.20</td></tr><tr><td>Vincent Andrews</td><td></td><td></td></tr><tr><td>Air Products and Chemicals Inc. (APD.N)</td><td>E (05/29/2025)</td><td>$282.35</td></tr><tr><td>Albemarle Corporation (ALB.N)</td><td>E (12/15/2025)</td><td>$155.44</td></tr><tr><td>Avient Corporation (AVNT.N)</td><td>E (12/14/2020)</td><td>$33.94</td></tr><tr><td>Axalta Coating Systems Ltd (AXTA.N)</td><td>++</td><td>$32.18</td></tr><tr><td>Celanese Corp. (CE.N)</td><td>E (01/20/2026)</td><td>$51.03</td></tr><tr><td>CF Industries (CF.N)</td><td>E (05/25/2016)</td><td>$113.49</td></tr><tr><td>Chemours Co (CC.N)</td><td>E (01/30/2018)</td><td>$20.50</td></tr><tr><td>Corteva Inc. (CTVA.N)</td><td>O (12/14/2020)</td><td>$77.03</td></tr><tr><td>Dow Inc. (DOW.N)</td><td>E (12/01/2019)</td><td>$33.97</td></tr><tr><td>DuPont De Nemours Inc. (DD.N)</td><td>E (05/26/2021)</td><td>$46.85</td></tr><tr><td>Eastman Chemical Co (EMN.N)</td><td>O (01/17/2019)</td><td>$71.84</td></tr><tr><td>Ecolab Inc. (ECL.N)</td><td>O (01/28/2025)</td><td>$257.97</td></tr><tr><td>FMC Corporation (FMC.N)</td><td>E (10/24/2023)</td><td>$11.64</td></tr><tr><td>Huntsman Corp (HUN.N)</td><td>E (12/11/2023)</td><td>$14.21</td></tr><tr><td>Intrepid Potash (IPI.N)</td><td>U (10/03/2013)</td><td>$34.96</td></tr><tr><td>Linde PLC (LIN.O)</td><td>O (02/09/2020)</td><td>$507.90</td></tr><tr><td>LyondellBasell Industries N.V. (LYB.N)</td><td>O (12/01/2019)</td><td>$64.50</td></tr><tr><td>Mosaic Company (MOS.N)</td><td>E (03/16/2016)</td><td>$22.24</td></tr><tr><td>Nutrien Ltd (NTR.N)</td><td>O (01/14/2026)</td><td>$67.20</td></tr><tr><td>Olin Corp. (OLN.N)</td><td>U (01/10/2023)</td><td>$24.54</td></tr><tr><td>PPG Industries Inc. (PPG.N)</td><td>E (11/01/2019)</td><td>$113.80</td></tr><tr><td>RPM International Inc. (RPM.N)</td><td>E (12/14/2020)</td><td>$104.96</td></tr><tr><td>Sherwin-Williams Co. (SHW.N)</td><td>O (03/19/2014)</td><td>$305.30</td></tr><tr><td>Tronox Holdings Plc-Class A (TROX.N)</td><td>E (01/30/2018)</td><td>$7.34</td></tr><tr><td>Westlake Corp (WLK.N)</td><td>E (01/09/2018)</td><td>$84.64</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
