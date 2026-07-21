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
Global Memory

# Korea Memory Export Tracker (Jun): Strong HBM in 2Q26, esp. for Samsung

![](images/def86fcf161bde2e465f6427fbe47a1a24afad88342bddd387bee3e749ba62df.jpg)

Mark Li

+852 2123 2645

mark.li@bernsteinsg.com

![](images/acca9756cb994d9a83f0de271c0f54b532a1c81a8661a7f69669a8359bfb46a3.jpg)

Edward Hou, CFA

+852 2123 2623

edward.hou@bernsteinsg.com

![](images/d4f6b58abf48d8aa8610e14e4407b2a531456e869c4e62b86f52c974f6220a68.jpg)

Yipin Cai, CFA

+852 2123 2669

yipin.cai@bernsteinsg.com

We track the Korea export data as it is a good early indicator for Samsung's & SK hynix's HBM revenue in the same quarter, and update this tracker with the Jun data. Details of our methodology can be found in our prior note. The dataset can be downloaded at this link.

Overall HBM export was very strong, up 46% QoQ vs. Mar, & set another record high. Jun data grew 45% MoM on seasonality & more importantly up 46% QoQ. Overall 2Q26 exports increased by 39% QoQ.

Data suggested Samsung 2Q26 HBM growth could beat our estimates. Export from S. Chungcheong Province (where Samsung packages HBM) grew 2x MoM, and was stronger than expected. Overall 2Q26 was up 75% QoQ. Regression predicts Samsung's 2Q26 HBM revenue to rise by 89% QoQ to US\$6.7B, above our model.

Export for SK hynix stayed robust. Jun export from N. Chungcheong & Icheon recovered by 11% MoM and was up 5% QoQ. Regression predicts SK hynix 2Q26 HBM revenue to grow 25% QoQ to US\$7.6B, in line with our forecast.

Data suggests a continued ramp of HBM4 at Samsung. As HBM has much higher dollar value per weight, we track “value per weigh” as it may be directionally suggestive of HBM price change. Jun “value per weight” grew another 30% MoM for Samsung but remained largely flattish for SK hynix. We believe this was likely driven by a continued ramp of Samsung’s HBM4 rather than a broad HBM price hike. The trend over the past few months has been generally positive for Samsung but flattish or declining for SK hynix.

Data shows HBM price has been insulated from the volatility of conventional memory price. Conventional memory price surged, but HBM price, as suggested by value per weight, largely stayed in the same range as before, as indicated by SK hynix's data.

Export to Malaysia bounced back sharply. It surged to US\$1.1B in Jun, mainly thanks to a recovery of exports from Samsung. And generally export to Malaysia has been growing meaningfully over the past few quarters. No sign of HBM export to destinations other than Taiwan & Malaysia, and also no sign that Samsung or SK hynix was producing HBM at a location that we don't track. Our methodology thus remains robust.

Overall Jun data suggested robust HBM growth for 2Q26, with a notable sign of HBM4 ramp at Samsung. Between the two, Samsung appeared to be stronger & ahead of our forecast, while SK hynix was in line. We also maintain that Samsung is improving its position in HBM4 & should gain more momentum in 2H26. On the other hand, HBM price being resetting now should trigger an upward revision for 2027.

Conventional memory price rise will continue in 3Q26 and HBM price increase should also bring earnings revision. We see continued price increase in 3Q27 & also HBM price hike in 2027 to lead to more earnings revision. We remain structurally constructive on Samsung, SK hynix & Micron but negative on KIOXIA on China competition (see our sector update). Our detailed SOTP valuation also finds KIOXIA over-valued.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">20 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>005930.KS (SEC- Samsung)</td><td>O</td><td>KRW</td><td>251,500</td><td>440,000</td><td>247.4%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td>38.0</td><td>5.2</td><td>3.3</td></tr><tr><td>005935.KS (SEC-Pref - Samsung)</td><td>O</td><td>KRW</td><td>169,200</td><td>374,000</td><td>180.8%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td>25.6</td><td>3.5</td><td>2.2</td></tr><tr><td>SMSN.LI (Samsung)</td><td>O</td><td>USD</td><td>4,200.00</td><td>7,350.00</td><td>226.8%</td><td>USD</td><td>116.15</td><td>812.39</td><td>1,290.80</td><td>36.2</td><td>5.2</td><td>3.3</td></tr><tr><td>000660.KS (SK hynix)</td><td>O</td><td>KRW</td><td>1,841,000</td><td>3,300,000</td><td>557.0%</td><td>KRW</td><td>60,341</td><td>395,677</td><td>568,862</td><td>30.5</td><td>4.7</td><td>3.2</td></tr><tr><td>MU (Micron)</td><td>O</td><td>USD</td><td>848.95</td><td>1,300.00</td><td>623.7%</td><td>USD</td><td>8.29</td><td>67.39</td><td>158.99</td><td>102.5</td><td>12.6</td><td>5.3</td></tr><tr><td>285A.JP (KIOXIA)</td><td>U</td><td>JPY</td><td>52,110</td><td>40,000</td><td>2087.2%</td><td>JPY</td><td>1,014.00</td><td>10,013</td><td>9,656.84</td><td>51.4</td><td>5.2</td><td>5.4</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,865.18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EM</td><td></td><td></td><td>1,732.38</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,457.69</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

MU estimate is Adjusted EPS; MU valuation is Adjusted P/E (x);

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Samsung Electronics: We rate Samsung Electronics Outperform with price target of KRW 440,000.

SK hynix : We rate SK hynix Outperform with price target of KRW 3,300,000.

## DETAILS

Korea Customs Service has released export data for Jun. As our previous note found, the export data for certain memory products bears close correlation with HBM revenues of Samsung and SK hynix. We hence track the monthly data to provide investors a preview on HBM revenues from the two companies in the same quarter. Details of our methodology can be found in the previous note. You may also download the export data at this link.

Export data suggests Samsung's 2Q26 HBM revenue likely was notably ahead of our estimates thanks to a very robust Jun. SK hynix HBM revenue is indicated to grow healthily and in line with our expectation, but notably slower than Samsung.

\- Jun Korea total multichip memory export to Taiwan and Malaysia was up strongly by 45% MoM, & reached another record high of US\$6.2B. Jun data was up 46% QoQ (vs. Mar) and also up 119% YoY (Exhibit 1). For all of 2Q26, export was up significantly by 39% QoQ. As we analyzed before, multichip memory export to Taiwan and Malaysia tracked closely with HBM revenues of Samsung and SK hynix and therefore the Jun data indicated strong and accelerating momentum into 2Q26.

\- If we focus on the export from S. Chungcheong Province, where Samsung's back-end fabs are and likely where its HBM is packaged, Jun export surged to US\$3.4B, doubling from May. And we also note that Jun single month export by Samsung surpassed that of SK hynix, for the first time since HBM exports took off in early 2024 (Exhibit 2). Overall 2Q26 export grew by 75% QoQ, which is notably stronger than our forecast of 51% growth for Samsung HBM in 2Q26 (Exhibit 3). According to the regression using historical data, Apr-Jun data suggested US\$6.7B in HBM revenue for Samsung in 2Q26, notably ahead of our estimate of US\$5.4B by 25%, and represented 89% QoQ growth (Exhibit 4). If we run the regression using only data points from 1Q25, the Apr-Jun data would also suggest roughly US\$6.7B in HBM revenue for 2Q26 (Exhibit 5). Samsung's HBM export monthly seasonality indeed was more backend loaded in 2Q26 compared to the previous few quarters, with 55% of export coming from Jun. Though we note that 2Q and 3Q25 seasonality was also very backend loaded and we wonder if 3Q26 will follow a similar pattern (Exhibit 6). Overall Samsung's HBM growth momentum was faster than expected in 2Q26, primarily supported by a very strong Jun. This also aligns with Samsung's guidance that HBM4 ramp should accelerate meaningfully into 2H26, & we hence remain positive on Samsung's HBM share gain this year (see Samsung 1Q26 earnings takeaway).

\- For SK hynix, we have identified that its HBM export should come nearly all from N. Chungchoeng Province and Icheon City, where its wafer fabs are. Jun export data rose by 11% MoM and 5% QoQ (vs Mar) (Exhibit 7). Overall 2Q26 export was up by 19% QoQ, quite close to our current forecast of 25% growth in HBM revenue in 2Q26 by hynix (Exhibit 8). Regression also finds that the export value suggests US\$7.6B HBM revenue by hynix in 2Q26, exactly in line with our forecast (Exhibit 9). Monthly seasonality of hynix's exports continued to be relatively balanced compared to Samsung's backend loaded one (Exhibit 10). All things considered, data indicated that SK hynix HBM is likely to grow healthily and in line with our estimates, but notably slower than Samsung.

EXHIBIT 1: Being a close proxy for HBM shipment, Korea multichip memory export to Taiwan and Malaysia reached a historical high at USD 6.2B in Jun 2026.  
![](images/5d4c1f0c6b4af5a132dd56ffbc61320ddfad28a4c63243427c25ab01d988bf61.jpg)  
Source: Korea Custom Service, KITA, company reports, Bernstein estimates and analysis

EXHIBIT 2: Export from S. Chungcheong was up 93% MoM and 75% QoQ vs. Mar.  
Multichip Memory Export from S. Chungcheong to TW+MY vs Samsung HBM Revenue  
![](images/b5b9301f8ca99548b184a5168c169a25f07e744219c6052b86f1670b65b45152.jpg)  
Samsung HBM revenue in 2Q26 is Bernstein estimate  
Source: Korea Custom Service, KITA, company reports, Bernstein estimates and analysis

Qtrly Samsung HBM Revenue vs. Qtrly Multichip Memory Export from S. Chungcheong to TW+MY (1Q25-1Q26)

Qtrly Samsung HBM Revenue vs. Qtrly Multichip Memory Export from S. Chungcheong to TW+MY (1Q23-1Q26)

EXHIBIT 3: Export from S.Chungcheong was up 75% QoQ in 2Q26.  
Samsung HBM Revenue vs. Multichip Memory Export from S. Chungcheong to TW+MY  
![](images/fdddf66c8c217a94271088b2de861a0705176a63612f858f22008ad0c5302f14.jpg)  
Samsung HBM revenue in 2Q26 is Bernstein estimates
Source: Korea Custom Service, KITA, company reports and Bernstein analysis

EXHIBIT 4: This suggests US\$6.7B and 89% QoQ growth for Samsung 2Q26 HBM revenue, ahead of our expectation.  
![](images/231cd88b9478ca369b0aee2533ce7b5a1eec499e431e7c5f776c38f352264916.jpg)  
Source: Korea Custom Service, KITA, company reports and Bernstein analysis

EXHIBIT 5: If we use only the data from recent quarters, Jun data would also suggest Samsung to have US\$6.7B in 2Q26 HBM sales.  
![](images/9190887827acd322e27710f6e43ddbe6f3fe1397706f331b6fff52aaeb1dfb60.jpg)  
Source: Korea Custom Service, KITA, company reports and Bernstein analysis

EXHIBIT 6: Monthly seasonality of export from S. Chungcheong has been more back-end loaded.  
S. Chungcheong Multichip Memory Export to TW+MY Monthly Seasonality Within Quarter  
![](images/53449bf036cbef8483353b656cdf481704cc4e404a7c35aafcdf821381936d19.jpg)  
Source: Korea Custom Service, KITA and Bernstein analysis

EXHIBIT 7: Export from N. Chungcheong and Icheon was up 11% MoM in Jun.  
![](images/f76f021a787037019c71ac56435c92b56ac92a6e1f2c5ece2d8c43f639fd530b.jpg)  
SK hynix HBM revenue in 2Q26 is Bernstein estimate  
Source: Korea Custom Service, KITA, company reports, Bernstein estimates and analysis

EXHIBIT 8: Export from N.Chungcheong and Icheon was up by 19% QoQ in 2Q26.  
SK hynix HBM Revenue vs. Multichip Memory Export from N. Chungcheong & Icheon to TW+MY  
![](images/184048f61885d22c38074f934a9bd46082bbe34e9b890a0be83e3c29347b978a.jpg)  
SK hynix 2Q26 HBM revenue is Bernstein estimate
Source: Korea Custom Service, KITA, company reports and Bernstein analysis  
EXHIBIT 9: This indicates US\$7.6B HBM revenue in 2Q26 for SK hynix, which is in line with our expectation.  
Qtrly SK hynix HBM Revenue vs. Qtrly Multichip Memory Export from N. Chungcheong & Icheon to TW+MY (1Q23-1Q26)

![](images/121cb8b90d2b0735d66626cf3ad386ec012839be6b0c37eb3dac78fd596c1024.jpg)  
Source: Korea Custom Service, KITA, company reports and Bernstein analysis

EXHIBIT 10: Monthly seasonality for N. Chungcheong + Ichoen remained much more balanced compared to Samsung.  
N. Chungcheong + Icheon Multichip Memory Export to TW+MY Monthly Seasonality Within Quarter  
![](images/aeb9384de49e3d1f734b7aefce09b938cb05a1618980ba08b26706efdef4462d.jpg)  
Source: Korea Custom Service, KITA and Bernstein analysis

## Samsung's export value per weight surged further in Jun likely thanks to rising HBM4 shipment.

\- Export value per weight for Korea multichip memory loosely correlates with HBM ASP, though it likely is only directionally indicative and not significant enough to make precise estimates. For Jun, export value per weight remained largely flattish MoM for N. Chungcheong+Ichoen (proxy for SK hynix). But data for S. Chungcheong (proxy for Samsung) continued surging very strongly in Jun by another 30% MoM and cumulatively by 70% vs Apr (Exhibit 11). This, along with surge in monthly export, could likely be related to rising HBM4 shipment, which should command notably higher value per weight than HBM3E. Samsung guided its HBM4 to cross over prior generations in 3Q26 and the data in the past two months indeed

S. Chungcheong Export N. Chungcheong Export + Icheon Export Other Provinces

suggests good progress toward that.

\- Looking at the data over the past several months, we find the trend remained positive for S. Chungcheong (hence Samsung). The notable increase in the recent months suggests beginning of volume shipment of HBM4. On the other hand, there was no sign of HBM4 shipment for SK hynix, as trend for N. Chungcheong+Icheon (i.e. SK hynix) has been downward or at best flattish since mid 2025.

\- Another important observation is while the price of conventional memory has been rising quickly, the data suggested that of HBM has been much steadier. Export value per weight from S.Chungcheong indeed grew but that's due to mix improvement from HBM4, rather than a general HBM price hike. The blended average even fell when we consider SK hynix's larger scale in HBM and the falling value per weight trend for the company. That said, we believe that suppliers and customers are negotiating the HBM contracts and prices for 2027 now. We expect this to trigger an upward revision for 2027 earnings, and this will also support memory stock prices in the near term.

EXHIBIT 11: Samsung's export value per weight continued to surge in Jun, probably indicating growing HBM4 shipment.

Korea Multichip Memory Export Value per Weight to TW+MY  
![](images/c2c8143297762df691c00e2200cb6bf7315af63170afd0857c602a07f2b42c62.jpg)  
Source: Korea Custom Service, KITA and Bernstein analysis

Export to Malaysia rebounded seasonally and generally has been growing at meaningful paces over the past few quarters. It likely suggested continued interest in EMIB, but we also wonder why the increase happened so early. Besides that we found no sign of new HBM packaging sites in Korea or new export destination countries.

\- Korea total multichip memory export to all countries was US\$12.7B in Jun, up by 32% MoM & up 48% QoQ, thanks to both growth in HBM and also surging prices of conventional memory. Taiwan and Malaysia accounted for 48% of the total export, down slightly QoQ from 49% in Mar, as conventional memory export value to other destinations grew faster with price increase (Exhibit 12). Looking at export value per weight chart, Taiwan remained notably higher than other countries, confirming Taiwan was still the primary destination of HBM export from Korea in Jun. Value per weight to Malaysia increased further in May & hence still strongly indicated presence of HBM. So far Taiwan and Malaysia remained the only destinations where we see very high export per weight, and therefore very likely HBM export (Exhibit 13). Export value per weight to Hong Kong and China Mainland was mixed, with China dipping and Hong Kong still growing. While we observe some increase in value per weight in regions other than Taiwan and Malaysia, we still assume it was due to rising conventional memory prices, and not due to HBM shipment, as Samsung and SK hynix likely exported considerable amounts of mobile memory packages to these regions & memory packages are categorized as multichip memory too (Exhibit 14). And it also supports conventional memory enjoys rapidly rising prices and commands better revenue and profit per wafer than HBM now.

\- Export to Malaysia bounced back sharply by 231% MoM to \~US\$1.1B in Jun, probably largely on seasonality. Average run rate in the last 6 month was to US\$0.55B, compared to US\$3.5B for exports to Taiwan. We understand that Malaysia is home to Intel's high-end packaging facilities, where some high-end server CPUs equipped with HBM are packaged with EMIB. Separately we picked up a growing customer interest in EMIB, and we note Intel is set to bring online a new advanced packaging fab into production this year as well (link). However, even if customers decide to adopt, we believe any volume production should be 1-2 years from now, and wonder why HBM export to Malaysia took place so early. All in all the export to Malaysia is worth continued monitoring.

\- Rebound in export to Malaysia was mainly attributable to Samsung, and apparently driven by seasonality as well. Though overall Samsung's export to Malaysia grew robustly in 2Q26 (Exhibit 15). Export from SK hynix's facilities recovered a bit in Jun but overall remained more or less flattish (Exhibit 16). Broadly the export to Malaysia has been growing quickly and has benefited Samsung more and has been one of the reasons behind Samsung's HBM revenue growth. It also supports Samsung's broadening customer recognition in HBM.

\- For the origin of export, Jun data showed that S. Chungcheong, N. Chungcheong and Ichoen continued to account for almost all of multichip memory export to Taiwan & Malaysia (Exhibit 17). So it does not appear either Samsung or SK hynix has started packaging HBM in other locations within Korea.

\- Overall, all the data above suggested that HBM export continued to concentrate in mostly Taiwan and to a lesser degree Malaysia. However, we'd like to point out the limitations to our methodology. One is if either of them moves any HBM packaging outside of Korea

[中间内容因长度限制已省略]

nce system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
