You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# China Economics

## A Plateauing Inflation Path in 26H2E after Energy Shock?

## CITI'S TAKE

CPI and PPI staged a small miss compared with expectations in June, but it came mostly from external factors including oil and gold prices. Domestic demand could have remained lackluster but largely stable, with supply conditions driving most of the volatility. For the whole quarter of 26Q2, nominal growth could rise further despite a real growth slowdown. We expect a plateauing path for inflation in 26H2E, with sporadic gains from AI inflation across CPI and PPI and a tentative stabilization of the pork cycle. Domestic demand could remain weak in this K-shaped economy, yet targeted support along with supply-side efforts on anti-involution could capture the downside to prices, in our view. The upcoming Politburo meeting could offer more signals.

Xinyu Ji $^{AC}$ +852-2501-2792
xinyu.ji@citi.com

Xiangrong Yu AC

+852-2501-2754

xiangrong.yu@citi.com

Inflation readings missed expectations in June as the energy shock faded. CPI edged down to 1.0%YoY (Citi/Mkt: 1.1%YoY) from earlier 1.2%YoY. Its sequential change was softer than seasonality at -0.3%MoM vs. an average of -0.2%MoM in the past three years. The small miss came from external factors of oil and gold. By major components,

\- Food prices dipped -0.4%MoM in June and stayed largely unchanged at -1.6%YoY (vs. -1.7%YoY in May). Pork downcycle could be closer to its bottom, with sequential change at -0.8%MoM, the smallest contraction in four months. Most food prices were stable, with vegetables at -1.0%MoM (-0.3%YoY) and fruits at -2.0%MoM (-0.7%YoY). Egg prices rose sharply amid hot weather at 5.8%MoM (16.0%YoY). Extreme weather events as El Nino develops are starting to have a more visible impact on China, and it is likely that supply conditions over the summer drives more price volatility.

■ Energy prices retreated as the oil shock faded. Prices dropped -4.5%MoM for transportation fuel, and its year-on-year change normalized to 15.3%YoY from 21.1%YoY in May, the first decline since the conflict. More downside is likely ahead in July with deeper adjustment of retail fuel prices, and year-on-year change could inch towards low single digits.

■ Core inflation dipped to 1.0%YoY, with its sequential change at -0.1%MoM and in line with seasonality. [1] Core goods inflation eased further to 1.3%YoY per our estimate, the lowest reading in one year. Gold prices eased to -5.9%MoM and 28.1%YoY and are largely responsible for the miss in June combined with oil prices. Durable goods prices are mixed: telecom equipment CPI rose to 7.6%YoY, an all-time high amid AI inflation, while auto CPI stayed unchanged at -1.1%YoY and home appliances prices retreated to 2.2%YoY (vs. 3.4%YoY). [2] Services CPI was lackluster but steady at 0.0%MoM and 0.8%YoY before the travel season.

Sequential PPI turned negative with energy shock fading. PPI dropped - 0.3%MoM, the first negative reading since July 2025, while its year-on-year reading continued to rise on base effect to 4.1%YoY (Citi/Mkt: 4.3/4.1%YoY).

■ Mideast conflict: We estimated that energy and chemical related sectors dragged 0.2ppts to sequential change of PPI of -0.3%MoM with Mideast conflict impact fading. With global oil prices easing in June, oil & gas extraction dropped -11.8%MoM and fuel processing declined -1.9%MoM in June, while chemicals eased -2.0%MoM.

■ Domestic energy prices: Coal prices rose into the summer and partially offset the drag from global prices. PPI for coal extraction inched up to 5.6%MoM with its year-on-year change at 20.6%YoY after turning positive only three months ago. Coal prices could have had wider spillover to ferrous metal processing, whose PPI rose to 5.2%YoY.

■ AI inflation: PPI for computer and other electronics mfg rose to 3.3%YoY, also an all-time high since 1996. Its momentum sustained with sequential change at 0.7%MoM, and 3M/3M annualized change at 7.9% in the past few months, hinting at further upside ahead. The NBS noted broad-based price hikes among electronics, with VR at 8.4%MoM, wearables at 3.4%MoM and industrial PCs at 3.3%MoM (NBS, Jul 9 $^{th}$ ).

■ Domestic demand: demand weakness remains a concern, as auto PPI remained subdued at -2.1% YoY and non-metallic mining at -3.3% YoY. Seasonal demand drove air conditioner mfg prices up 0.4% MoM.

Figure 1. CPI and PPI posed a small miss in June mostly on external factors  
![](images/33b6ffd6538be76346561108cfa61536b17e7bdf2125fb99e2b4c8d6fe1c99c5.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 2. Core goods prices eased further as soft demand met various supply conditions  
![](images/e02ce4f3c7297e8c14b122325ed440cba2a52a6dd2605f648f785c59b487e761.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi

Figure 3. Telecom equipment CPI rose to an all-time high amid AI inflation  
![](images/8b41192431cc18c81b04fc26875827b6094ca50de505b209c83962ef9279290d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi

Figure 4. We estimate a drag of -0.2ppts from energy & chemical to sequential PPI in June  
![](images/a2d88f3a4520d27c5749873c35e8c10e639d503de83f7c24281a4ad75d8424fc.jpg)  
Energy Chemical Non-Ferrous Construction Others PPI, %MoM © 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi

Figure 5. Mideast conflict impact retreated for PPI, but domestic energy prices and AI inflation rose further

<table><tr><td rowspan="2" colspan="3">Sector</td><td rowspan="2">Deflation easing sequentially?</td><td rowspan="2">Consecutive months of PPI deflation</td><td colspan="3">%YoY</td><td colspan="3">3M/3M Annualized</td></tr><tr><td>Apr</td><td>May</td><td>Jun</td><td>Apr</td><td>May</td><td>Jun</td></tr><tr><td>Up</td><td>煤炭开采和洗选业</td><td>Coal mining and washing</td><td></td><td></td><td>3.1</td><td>10.0</td><td>20.6</td><td>6.1</td><td>22.8</td><td>52.1</td></tr><tr><td>Up</td><td>石油和天然气开采业</td><td>Petroleum and natural gas extraction</td><td></td><td></td><td>28.6</td><td>35.7</td><td>16.8</td><td>332.6</td><td>253.2</td><td>18.9</td></tr><tr><td>Up</td><td>石油、煤炭及其他燃料加工业</td><td>Petroleum, coal and other fuel processing</td><td></td><td></td><td>14.2</td><td>18.4</td><td>16.7</td><td>133.7</td><td>130.0</td><td>70.0</td></tr><tr><td>Up</td><td>黑色金属矿采选业</td><td>Ferrous metal mining</td><td></td><td></td><td>1.3</td><td>3.3</td><td>5.2</td><td>-5.1</td><td>1.6</td><td>4.1</td></tr><tr><td>Up</td><td>有色金属矿采选业</td><td>Non-ferrous metal mining</td><td></td><td></td><td>38.9</td><td>36.5</td><td>25.5</td><td>82.8</td><td>31.3</td><td>-21.4</td></tr><tr><td>Up</td><td>非金属矿采选业</td><td>Non-metallic mineral mining</td><td>Yes</td><td>20</td><td>-4.1</td><td>-3.4</td><td>-3.3</td><td>-0.4</td><td>3.7</td><td>0.0</td></tr><tr><td>Middle</td><td>电力、热力的生产和供应业</td><td>Electricity and heat production/supply</td><td></td><td>32</td><td>-4.2</td><td>-4.4</td><td>-4.4</td><td>-12.3</td><td>4.0</td><td>-5.1</td></tr><tr><td>Middle</td><td>燃气生产和供应业</td><td>Gas production/supply</td><td></td><td></td><td>-0.6</td><td>2.5</td><td>4.0</td><td>3.2</td><td>12.6</td><td>15.4</td></tr><tr><td>Middle</td><td>水的生产和供应业</td><td>Water production/supply</td><td></td><td></td><td>1.6</td><td>1.7</td><td>0.9</td><td>0.4</td><td>1.6</td><td>-1.6</td></tr><tr><td>Middle</td><td>黑色金属冶炼及压延加工业</td><td>Ferrous metal smelting</td><td></td><td></td><td>-1.1</td><td>1.0</td><td>3.1</td><td>4.1</td><td>8.7</td><td>9.2</td></tr><tr><td>Middle</td><td>有色金属冶炼及压延加工业</td><td>Non-ferrous metal smelting</td><td></td><td></td><td>22.5</td><td>24.0</td><td>23.4</td><td>25.6</td><td>9.6</td><td>4.9</td></tr><tr><td>Middle</td><td>金属制品业</td><td>Metal products</td><td></td><td></td><td>0.5</td><td>0.8</td><td>1.6</td><td>2.4</td><td>1.6</td><td>2.0</td></tr><tr><td>Middle</td><td>非金属矿物制品业</td><td>Non-metallic mineral products mfg</td><td>Yes</td><td>46</td><td>-5.5</td><td>-5.1</td><td>-4.4</td><td>-3.5</td><td>-5.1</td><td>-5.8</td></tr><tr><td>Middle</td><td>化学原料及化学制品制造业</td><td>Chemical</td><td></td><td></td><td>8.9</td><td>12.7</td><td>11.3</td><td>66.9</td><td>71.5</td><td>37.3</td></tr><tr><td>Middle</td><td>纺织业</td><td>Textile</td><td></td><td></td><td>0.2</td><td>1.1</td><td>1.5</td><td>4.9</td><td>7.9</td><td>6.6</td></tr><tr><td>Down</td><td>农副食品加工业</td><td>Agricultural products</td><td>Yes</td><td>38</td><td>-1.3</td><td>-1.4</td><td>-1.2</td><td>-1.2</td><td>-3.5</td><td>-4.7</td></tr><tr><td>Down</td><td>食品制造业</td><td>Food mfg</td><td></td><td>39</td><td>-1.6</td><td>-1.0</td><td>-1.0</td><td>0.4</td><td>3.2</td><td>1.6</td></tr><tr><td>Down</td><td>酒、饮料和精制茶制造业</td><td>Wine and beverage mfg</td><td></td><td>26</td><td>-2.9</td><td>-1.9</td><td>-5.3</td><td>-2.8</td><td>1.2</td><td>-12.3</td></tr><tr><td>Down</td><td>烟草制品业</td><td>Tobacco products</td><td></td><td></td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Down</td><td>纺织服装、服饰业</td><td>Textile and apparel mfg</td><td>Yes</td><td>17</td><td>-1.5</td><td>-1.4</td><td>-1.3</td><td>-3.5</td><td>-0.4</td><td>0.4</td></tr><tr><td>Down</td><td>木材加工及木、竹、藤、棕、草制品业</td><td>Wood and wood products</td><td></td><td>44</td><td>-2.3</td><td>-1.9</td><td>-1.9</td><td>-0.4</td><td>-0.8</td><td>0.0</td></tr><tr><td>Down</td><td>造纸及纸制品业</td><td>Paper and paper products</td><td>Yes</td><td>7</td><td>-1.2</td><td>-0.7</td><td>-0.1</td><td>-3.9</td><td>-0.8</td><td>0.4</td></tr><tr><td>Down</td><td>印刷业和记录媒介的复制</td><td>Printing</td><td></td><td>42</td><td>-2.7</td><td>-2.7</td><td>-2.8</td><td>-2.0</td><td>-1.2</td><td>-2.0</td></tr><tr><td>Down</td><td>医药制造业</td><td>Pharmaceutical mfg</td><td></td><td>30</td><td>-4.7</td><td>-4.5</td><td>-4.5</td><td>-4.3</td><td>-3.5</td><td>-3.5</td></tr><tr><td>Down</td><td>化学纤维制造业</td><td>Chemical fiber mfg</td><td></td><td></td><td>5.4</td><td>8.5</td><td>7.4</td><td>45.6</td><td>50.9</td><td>27.8</td></tr><tr><td>Down</td><td>橡胶和塑料制品业</td><td>Rubber and plastic products mfg</td><td></td><td></td><td>-1.3</td><td>0.5</td><td>1.4</td><td>8.3</td><td>16.3</td><td>15.8</td></tr><tr><td>Down</td><td>通用设备制造业</td><td>General machinery</td><td>Yes</td><td>42</td><td>-1.0</td><td>-0.9</td><td>-0.7</td><td>-1.2</td><td>-0.8</td><td>-0.4</td></tr><tr><td>Down</td><td>汽车制造业</td><td>Auto</td><td></td><td>46</td><td>-2.0</td><td>-2.0</td><td>-2.1</td><td>-2.4</td><td>-2.4</td><td>-0.4</td></tr><tr><td>Down</td><td>铁路、船舶、航空航天和其他运输设备制造</td><td>Railway and other transportation</td><td>Yes</td><td>13</td><td>-0.3</td><td>-0.3</td><td>-0.2</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Down</td><td>计算机、通信和其他电子设备制造业</td><td>Computer and other electronics</td><td></td><td></td><td>1.5</td><td>2.1</td><td>3.3</td><td>7.9</td><td>7.9</td><td>7.9</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Wind, Citi

Nominal growth is set to rise further in 26Q2E. CPI averaged 1.1% YoY in the past quarter vs. 0.8% YoY in 26Q1, while PPI rose to 3.6% YoY vs. -0.6% YoY. GDP deflator could rise to 1½ \~2%, lifting nominal growth even as real growth slows – with our GDP forecast at 4.5% YoY for 26Q2E, nominal growth could still challenge the high rate since mid-2023.

We see a plateauing path for inflation in 26H2E. The miss in June for both CPI and PPI is mostly from external volatility, instead of further intensifying domestic weakness – on the former, the corrections seem to have been factored in the data. On the domestic side, stabilization of pork cycle could provide some relief to CPI, while AI inflation creates sporadic gains across CPI and PPI. Domestic demand could remain weak in this K-shaped economy, yet targeted support along with supply-side efforts on anti-involution could capture the downside to prices, in our view. The upcoming Politburo meeting could offer more signals.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at

https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

## RESEARCH ANALYST AFFILIATIONS / NON-US RESEARCH ANALYST DISCLOSURES

The legal entities employing the authors of this report are listed below (and their regulators are listed further herein). Non-US research analysts who have prepared this report (i.e., all research analysts listed below other than those identified as employed by Citi Global Markets Inc.) are not registered/qualified as research analysts with FINRA. Such research analysts may not be associated persons of the member organization (but are employed by an affiliate of the member organization) and therefore may not be subject to the FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Citi Global Markets Asia Limited

Xinyu Ji; Xiangrong Yu

## OTHER DISCLOSURES

Any price(s) of instruments mentioned in recommendations are as of the prior day's market close on the primary market for the instrument, unless otherwise stated.

The completion and first dissemination of any recommendations made within this research report are as of the Eastern date-time displayed at the top of the Product. If the Product references views of other analysts then please refer to the price chart or rating history table for the date/time of completion and first dissemination with respect to that view.

<table><tr><td>European regulations require that where a recommendation differs from any of the author&#x27;s previous recommendations concerning the same financial instrument or issuer that has been published during the preceding 12-month period that the change(s) and the date of that previous recommendation are indicated. Please refer to the trade history in the published research or contact the research analyst.</td></tr><tr><td>Citi has implemented policies for identifying, considering and managing potential conflicts of interest arising as a result of publication or distribution of investment research. A description of these policies can be found at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures.</td></tr><tr><td>The proportion of all Citi recommendations that were the equivalent to &quot;Buy&quot;, &quot;Hold&quot;, &quot;Sell&quot; at the end of each quarter over the prior 12 months (with the % of these that had received investment firm services from Citi in the prior 12 months shown in brackets) is as follows; Q1 2026 Buy 33%(63%), Hold 44% (52%), Sell 23% (46%), RV 0.5% (89%): Q4 2025 

[中间内容因长度限制已省略]

t may have tax implications for private customers whereby levels and basis of taxation may be subject to change. If in doubt, investors should seek advice from a tax adviser. The Product does not purport to identify the nature of the specific market or other risks associated with a particular transaction. Advice in the Product is general and should not be construed as personal advice given it has been prepared without taking account of the objectives, financial situation or needs of any particular investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the "Product"), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
