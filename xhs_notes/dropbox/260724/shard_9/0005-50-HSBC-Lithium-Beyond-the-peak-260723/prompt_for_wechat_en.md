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
\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

Lithium

Beyond the peak

Lithium prices have retreated from May's peak but remain elevated; equity valuations discount a steeper decline

\- We expect demand to remain strong in 2H26; mine restarts to add material supply in 2027

\- Maintain Buy ratings on SQM, ALB and LAR, and Hold rating on LAC; revise TPs

Lithium prices have fallen from the peak but remain elevated: China BG lithium carbonate prices are down c28% from the May 2026 peak, yet remain up c25% year-to-date. Pricing has been pressured by signs of softer EV sales momentum in China, the restart of previously curtailed supply, and broader weakness in global technology equities. This pullback is not unique to lithium – other major commodities (including copper and aluminium) have also retreated from their May 2026 highs.

Headwinds are brewing: We see increasing headwinds for the lithium market, suggesting the cycle peak in prices may now be behind us. The restart of the Jianxiawo mine will remove an uncertainty and add to supply in 2H26. The arrival of shipments from Zimbabwe will further ease supply pressures in 2H26. While the restarts in Australia will add meaningfully to supply in 2027 (c60-70kt incremental in 2027), news of the restarts has already weighed on sentiment. The announcement of a consumption tax on lithium batteries in China could also be detrimental to prices. That said, we expect demand to be seasonally strong in 2H26. We increase our China BG lithium carbonate price forecasts for 2026e, but we cut our 2028-29e forecasts to reflect higher supply. See Metals Quarterly Q3 2026 - Shaky “MoUmentum”, 19 July 2026, for more details.

Lithium equities pricing in a much lower lithium price: Current valuations across lithium equities suggest the market is pricing in an average lithium carbonate price of cUSD13,500-14,000/t over the next 12 months – around 33-37% below spot. While we also expect prices to moderate, our forecast over the same period is much higher, at USD19,300/t. See p6 for the analysis.

Maintain Buy on SQM, ALB and LAR and Hold on LAC; cut TPs: We prefer SQM due to its operational excellence, strong balance sheet, and volume growth. We believe ALB's continuous efforts to control costs and efficiency gains position it to benefit despite potential decline in lithium prices. The continuous improvement in production at LAR's Cauchari Olaroz operations indicates operational stability.

# Equities Metals & Mining

Global

## Ishan Jain\*

Analyst, Metals & Mining, Pulp & Paper
HSBC Securities and Capital Markets (India) Private Limited
ishanjain@hsbc.co.in
+91 80 4550 3767

## Jonathan Brandt, CFA

Analyst, GEMs ex-Asia Metals & Mining, Pulp & Paper
HSBC Securities (USA) Inc.
jon.brandt@us.hsbc.com
+1 212 525 4499

Gustavo Hwang\*, CFA
Analyst, GEMs ex-Asia Metals & Mining, Pulp & Paper
Banco HSBC S.A.
gustavo.hwang@hsbc.com
+55 11 2802 3257

## Sriharsha Pappu\*

Global Head of Energy & Materials
HSBC Bank plc
sriharsha.pappu@hsbc.com
+44 20 7991 9243

Key changes to ratings and estimates

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Currency</td><td rowspan="2">Current price</td><td colspan="2">TP</td><td colspan="2">Rating</td><td rowspan="2">Upside/ downside</td><td rowspan="2">Market cap (USDm)</td><td rowspan="2">3m ADTV (USDm)</td><td rowspan="2">2026e EV/EBITDA</td><td rowspan="2">2027e EV/EBITDA</td><td rowspan="2">2026e PE</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td></tr><tr><td>SQM</td><td>SQM US</td><td>USD</td><td>68.84</td><td>100.00</td><td>95.00</td><td>Buy</td><td>Buy</td><td>38.0%</td><td>20,447</td><td>92</td><td>6.4</td><td>7.6</td><td>12.1</td></tr><tr><td>Albemarle</td><td>ALB US</td><td>USD</td><td>118.62</td><td>230.00</td><td>170.00</td><td>Buy</td><td>Buy</td><td>43.3%</td><td>13,989</td><td>364</td><td>5.6</td><td>7.9</td><td>10.8</td></tr><tr><td>Lithium Argentina</td><td>LAR US</td><td>USD</td><td>6.29</td><td>13.00</td><td>8.50</td><td>Buy</td><td>Buy</td><td>35.1%</td><td>1,032</td><td>2</td><td>13.2</td><td>20.3</td><td>20.4</td></tr><tr><td>Lithium Americas</td><td>LAC US</td><td>USD</td><td>3.06</td><td>4.75</td><td>3.30</td><td>Hold</td><td>Hold</td><td>7.7%</td><td>1,108</td><td>55</td><td>nm</td><td>nm</td><td>nm</td></tr></table>

Source: HSBC estimates. Priced as of close of 21 July 2026

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: HSBC Securities and Capital Markets (India) Private Limited

View HSBC Global Investment Research at: https://www.research.hsbc.com

## Strong demand outlook for 2H26

China's total battery sales (including exports) grew $49\%$ y-o-y in 1H26

Energy storage is now the primary incremental growth driver for the battery sector. In 1H26, China's total battery sales (including exports) reached 979GWh, representing $49\%$ year-on-year growth. This total comprised 661GWh of EV batteries $(+36\%$ y-o-y) and 318GWh of energy storage batteries $(+83\%$ y-o-y).

Historically, energy storage demand has been driven mainly by renewable energy integration policies and grid modernisation. However, a new demand catalyst is emerging: the rapid expansion of AI workloads. Although AI data centres (AIDCs) accounted for only 2% of ESS battery demand in 2025 (ICC data), accelerating AI-related power consumption is reshaping the investment case for ESS deployment in AIDCs, particularly in the US. Given that dependable power is critical to AI infrastructure, we believe ESS solutions serving this segment may be less price-sensitive than those used in more conventional storage applications.

China EV battery sales volumes (incl. exports) up 36% y-o-y in 1H26  
![](images/f931536a55af541f49bee51d9db032dddf866d859ee121cd15edcd70325cc008.jpg)  
Source: CABIA, HSBC

China ESS battery sales volumes (incl. exports) up 83% y-o-y in 1H26  
![](images/0f47fb601adef749ae0eee27ac44d96f43dcf2675bbeac7860a4c18bdb7b5677.jpg)  
Source: CABIA, HSBC

China EV battery exports up 50% y-o-y in 1H26  
![](images/d36b0f95b295d89d5de50f36736982e5e944afa996316ac111beb5f003ecb384.jpg)  
Source: CABIA, HSBC

China ESS battery exports up 28% y-o-y in 1H26  
![](images/374137f178e16235c21abe20ad335badb9d9d66713f264f46ba8baac3509b9be.jpg)  
Source: CABIA, HSBC

While China's BEV volumes were softer than we anticipated in 1H26, we expect demand to regain momentum, supported by new model launches, technology upgrades, and the release of replacement demand (influenced by subsidies and supply dynamics). HSBC China autos analysts forecast $10\%$ growth in China EV volumes (see China EV Tracker, 18 May 2026).

In 1H26, EV demand in China was strongest for premium, large electric SUVs, consistent with an expanding RMB200k+ segment. Despite the broader slowdown in domestic EV sales, EV battery installations increased 12% y-o-y, driven by higher battery capacity per vehicle and a marked rise in commercial EV penetration.

Looking ahead, more than 160 new EV models are expected to launch in 2H26, with many targeting the mass market. HSBC China auto analysts expect this to help support a demand recovery in that segment.

We expect lithium demand to grow 19% y-o-y in 2026e and at a 14% CAGR during 2026-30e.

ESS is becoming the primary incremental growth driver  
![](images/a1f34cfdc73f3779b937ab18ee2d3de0a76866f80ff399dc379dcc5c5ac0ae12.jpg)  
Source: Wood Mackenzie, Company reports, HSBC estimates

## Keeping a close eye on supply

CATL's Jianxiawo mine has now obtained all required permits and is in the process of restarting. Operations were halted in August 2025 after the relevant approvals were not renewed. The mine and associated refinery have an estimated nameplate capacity of c100kt LCE per annum. The restart timeline is broadly consistent with our expectations, and we forecast production of c48kt LCE in 2026..

Encouraged by the higher price environment, we are seeing the resumption of assets previously placed on care and maintenance during the previous downturn – most notably Ngungaju, Bald Hill, and Finniss. At full utilisation, these three operations could collectively contribute c500-600kt per year of spodumene concentrate (equivalent to c65-80kt LCE). Given typical ramp-up profiles, the bulk of the supply impact is likely to be felt in 2027 rather than immediately.

Following an initial announcement of a ban on lithium concentrate exports, Zimbabwe subsequently indicated it would move to an export quota regime in 2026, alongside requests for commitments to establish lithium sulphate processing capacity for exports from 2027. We expect shipments to normalise in 2H26. At present, approximately 110-120kt LCE of lithium sulphate capacity is under construction, with additional projects also announced. These developments should help stabilise supply; however, allowing for commissioning and ramp-up, we expect a material uplift in supply from 2027 onwards.

There is a pipeline of probable projects globally which, if approved, can add more supply towards the end of the decade

We highlight that there is a pipeline of probable projects globally that, if approved, can add more supply towards the end of the decade. The list of projects includes: PPG, expansion at Cauchari-Olaroz, Thacker Pass Phase 2, Wodgina expansion, Nova Andino, PMET Resources' Shaakichiuwaanaan, Franklin, Neves, Salares Altoandinos, Salar De Maricunga, P2000, and Carolina, etc.

In fact, this week, SQM along with its partner Wesfarmers (WES AU, CMP AUD89.90, Not covered) announced the final decision to double production capacity at Mt Holland in Australia from 380kt to 760kt (of 5.5% Li2O spodumene concentrate). The construction of the project will start in 2H27, and the companies expect production to start in 1H30.

The restarts to add to supply growth next year; there is a pipeline of probable projects globally which, if approved, can add more supply towards the end of the decade  
![](images/e37dda0e3141ef1d1b53d79d70e7eeb2ea95edcab152733ef8ac4554d1837c87.jpg)  
Source: Wood Mackenzie, Company reports, HSBC estimates

## Lithium prices to remain elevated in 2H26, but headwinds are brewing

Lithium carbonate (BG China) prices are up 25% y-t-d but have come down c28% from the peak witnessed in May 2026. The restart of the Jianxiawo mine will remove an uncertainty and add to supply in 2H26. The arrival of shipments from Zimbabwe will further ease supply pressures in 2H26. While we expect the restarts in Australia will add meaningfully to supply in 2027 (c60-70kt incremental in 2027), the news of the restart will weigh on sentiment.

Lithium prices have fallen in the past couple of months but remain elevated  
![](images/1b3882ff657721506a7c6eaf7fc63d653dadc86ddf4ab5e5462c7b1f9c76e368.jpg)  
Source: Bloomberg, HSBC

China has announced that it will introduce a 2% consumption tax on lithium batteries from 1 September 2026, rising to 4% from 1 September 2027. Sodium-ion batteries, solid-state batteries, fuel cells, and certain advanced solar cells will be exempt until the end of 2028. We see two potential implications. In the near-term, buyers may front-load battery purchases in 3Q26 to avoid the initial tax, which could provide a short-term boost to battery shipments and, in turn, support near-term demand for battery metals. Although the tax rates are modest, the policy direction appears intended to encourage adoption of non-lithium alternatives over time, reinforcing incentives to diversify away from conventional lithium-based chemistries in the medium term.

Please click here for our lithium S&D model and price forecasts

Seasonally, demand is stronger in 2H. Our expectations are for auto sales in China to recover sequentially in 2H26. However, slower-than-expected demand growth remains a key risk. We expect lithium prices to remain elevated, but supply growth from the restarts could be meaningful and could outpace demand growth in 2027. We increase our China BG lithium carbonate price forecasts for 2026e, but we cut our 2028-29e forecasts to reflect higher supply. See Metals Quarterly Q3 2026 - Shaky "MoUmentum", 19 July 2026, for more details.

HSBC lithium S&D model

<table><tr><td>in LCE kt</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td><td>Change 2026-30e</td><td>CAGR 2026e-30e</td></tr><tr><td colspan="10">Demand</td></tr><tr><td>EVs</td><td>707</td><td>915</td><td>1,063</td><td>1,197</td><td>1,406</td><td>1,595</td><td>1,774</td><td>859</td><td>14%</td></tr><tr><td>Battery demand (ex-EV)</td><td>415</td><td>561</td><td>714</td><td>806</td><td>933</td><td>1,057</td><td>1,162</td><td>601</td><td>16%</td></tr><tr><td>Total battery demand</td><td>1,122</td><td>1,476</td><td>1,777</td><td>2,003</td><td>2,339</td><td>2,653</td><td>2,936</td><td>1,459</td><td>15%</td></tr><tr><td>y-o-y</td><td>33%</td><td>32%</td><td>20%</td><td>13%</td><td>17%</td><td>13%</td><td>11%</td><td></td><td></td></tr><tr><td>Total non-battery demand</td><td>149</td><td>153</td><td>158</td><td>162</td><td>167</td><td>172</td><td>178</td><td>24</td><td>3%</td></tr><tr><td>y-o-y</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td></td><td></td></tr><tr><td>Total demand</td><td>1,271</td><td>1,630</td><td>1,935</td><td>2,165</td><td>2,507</td><td>2,825</td><td>3,114</td><td>1,484</td><td>14%</td></tr><tr><td>y-o-y</td><td>28%</td><td>28%</td><td>19%</td><td>12%</td><td>16%</td><td>13%</td><td>10%</td><td></td><td></td></tr><tr><td colspan="10">Supply</td></tr><tr><td>Total refined supply before recycling</td><td>1,277</td><td>1,646</td><td>1,943</td><td>2,230</td><td>2,458</td><td>2,641</td><td>2,799</td><td>1,152</td><td>11%</td></tr><tr><td>y-o-y</td><td>38%</td><td>29%</td><td>18%</td><td>15%</td><td>10%</td><td>7%</td><td>6%</td><td></td><td></td></tr><tr><td>Recycling</td><td>51</td><td>68</td><td>88</td><td>122</td><td>170</td><td>208</td><td>253</td><td>185</td><td>30%</td></tr><tr><td>y-o-y</td><td>41%</td><td>34%</td><td>28%</td><td>40%</td><td>39%</td><td>23%</td><td>22%</td><td></td><td></td></tr><tr><td>Total Refined supply</td><td>1,328</td><td>1,715</td><td>2,031</td><td>2,352</td><td>2,627</td><td>2,850</td><td>3,052</td><td>1,337</td><td>12%</td></tr><tr><td>y-o-y</td><td>38%</td><td>29%</td><td>18%</td><td>16%</td><td>12%</td><td>8%</td><td>7%</td><td></td><td></td></tr><tr><td colspan="10">Market balance</td></tr><tr><td>Inventory changes</td><td>(85)</td><td>(25)</td><td>34</td><td>106</td><td>26</td><td>33</td><td>30</td><td></td><td></td></tr><tr><td>Surplus / (deficit) post inventory changes</td><td>141</td><td>110</td><td>62</td><td>81</td><td>95</td><td>(8)</td><td>(92)</td><td></td><td></td></tr></table>

Reproduced from Metals Quarterly Q3 2026 - Shaky "MoUmentum", 19 July 2026  
Source: HSBC estimates, USGS, Wood Mackenzie

## What lithium prices are equities pricing in?

We estimate that the market is valuing lithium equities at a multiple around one standard deviation below their 12-month forward historical average, likely reflecting expectations of a further decline in lithium prices.

Current share prices of lithium miners imply an average price of USD13,500–14,000/t over the next 12 months—around 33–37% below the current spot price

If these stocks were valued in line with average historical multiples, current share prices would imply an expectation that lithium carbonate averages approximately USD13,500-14,000/t over the next 12 months – around 33-37% below the current spot price.

While we also anticipate lithium prices moderating from current levels, our forecast is for an average of USD19,300/t over the next 12 months, which is materially above the price levels implied by current equity valuations.

Average lithium price implied in the stock prices based on 12m forward multiples

<table><tr><td colspan="4">SQM</td></tr><tr><td></td><td></td><td>Trough</td><td>Average</td></tr><tr><td>Current market cap</td><td>USDm</td><td>20,068</td><td>20,068</td></tr><tr><td>Net debt (last reported)</td><td>USDm</td><td>2,283</td><td>2,283</td></tr><tr><td>Others (preferred, minority, etc)</td><td>USDm</td><td>47</td><td>47</td></tr><tr><td>Implied EV</td><td>USDm</td><td>22,398</td><td>22,398</td></tr><tr><td>Historical 12m fwd 10-year avg EV/EBITDA multiple</td><td>x</td><td>5.8</td><td>9.4</td></tr><tr><td>Implied EBITDA</td><td>USDm</td><td>3,862</td><td>2,383</td></tr><tr><td>EBITDA for other division (including corporate)</td><td>USDm</td><td>919</td><td>919</td></tr><tr><td>Implied lithium division&#x27;s EBITDA</td><td>USDm</td><td>2,942</td><td>1,464</td></tr></table>

Average lithium prices (incl VAT) in the next twelve months to arrive at the implied lithium EBITDA based on our model assumptions USD/t 22,400 13,500

<table><tr><td colspan="4">ALB</td></tr><tr><td></td><td></td><td>Trough</td><td>Average</td></tr><tr><td>Current market cap</td><td>USDm</td><td>13,940</td><td>13,940</td></tr><tr><td>Net debt (last reported)</td><td>USDm</td><td>1,461</td><td>1,461</td></tr><tr><td>Others (preferred, minority, etc)</td><td>USDm</td><td>2,493</td><td>2,493</td></tr><tr><td>Implied EV</td><td>USDm</td><td>17,894</td><td>17,894</td></tr><tr><td>Historical 12m fwd 10-year avg EV/EBITDA multiple</td><td>x</td><td>7.3</td><td>12.3</td></tr><tr><td>Implied EBITDA</td><td>USDm</td><td>2,451</td><td>1,455</td></tr><tr><td>EBITDA for other division (including corporate)</td><td>USDm</td><td>244</td><td>244</td></tr><tr><td>Implied lithium division&#x27;s EBITDA</td><td>USDm</td><td>2,207</td><td>1,211</td></tr><tr><td>Average lithium prices (incl VAT) in the next twelve months to arrive at the implied lithium EBITDA based on our model assumptions</td><td>USD/t</td><td>21,100</td><td>14,300</td></tr></table>

## SQM (SQM US, CMP USD68.84) – maintain Buy; cut TP to USD95 (from USD100)

## Investment thesis

We like SQM due to expectations of increase in volumes, its operational excellence, and strong balance sheet. The ramp up of the Kwinana refinery, expansion at the Mt Holland in Australia and increased volumes in Chile should drive volume growth and improve product mix.

## Sensitivity to changes in lithium prices

Lithium prices are volatile, and SQM's stock price shows a high degree of sensitivity to changes in lithium prices. SQM's realised prices follow the spot price movement closely. The impact of changes in the lithium price assumptions during the forecast period (including long-ter

[中间内容因长度限制已省略]

 Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures". If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Securities and Capital Markets (India) Private Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Securities and Capital Markets (India) Private Limited.

## Stay connected to our topical and timely thought leadership

![](images/05646d42f44447b2714d9dd5689f00f3436eb99941ff122c8543ab9253711721.jpg)

## Download the HSBC Global Investment Research app

From Apple's App Store or Google Play The app features topical and timely curated reports, multimedia, and upcoming events

![](images/ab6ad2c03e5ff09b464e40b7a705ade19117c56d99a1cc8f7ed3274fc66ddd73.jpg)

## Log on to the Global Investment Research website

To access all reports and videos, visit research.hsbc.com

![](images/70617ffbeace50b190fd0c3f152a137b275ebb2397eabdd8ec95129a28e2fb0f.jpg)

## Connect with Global Investment Research on LinkedIn

Search #HSBCResearch for free to view insights that can easily be shared with clients and prospects

![](images/a57fb62b92260ba0a00230b6df6ac95ab523ecd8b6fab38474b72c73b5fa23db.jpg)

## Subscribe and listen

Under the Banyan Tree by HSBC Global Investment Research on Apple, Spotify or YouTube

The Macro Brief by HSBC Global Investment Research on Apple, Spotify or YouTube

![](images/1cb06321e01a5ae7ed8f7c8e9545f3750ef6ccdc536c7f77dc9ef487f76358db.jpg)

## Newsletters

Subscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points
"""
