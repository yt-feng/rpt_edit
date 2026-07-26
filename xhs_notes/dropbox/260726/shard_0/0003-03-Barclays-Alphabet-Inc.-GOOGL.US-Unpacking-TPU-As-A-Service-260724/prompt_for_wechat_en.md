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
Alphabet Inc.

# Unpacking TPU-As-A-Service

GOOGL is about to embark on a major new initiative to scale AI outside of its datacenter walls via a new economic model, initially with Anthropic, but potentially with others down the road. We think this effort could boost '28 cons. gross profit by 15% and OI by more.

The Key Take-Away: Google is about to kick off one of its largest new business models with the help of several partners, to increase AI capacity industry-wide. Most investors are aware of TPU-aaS given the commentary on the recent earnings call, but the magnitude of how big this effort could be is likely underappreciated by the Street. Semiconductor buysiders have a decent handle on this theme, but we think now is the time for the consumer internet buyside to take notice. TPU-aaS is where Google takes inventory and sells TPUs directly to customers as a merchant vendor. One only has to look at the \$811B (up +\$479B Q/Q) in purchase commitments buried in the 10-Q this week, the \$275B+ increase in backlog in the past 6 months, or AVGO's commitment of 20+ GWs, to start to see how massive this could be. We are raising our Google Cloud revenue and OI estimates significantly with this report, after a full rebuild of our model. We'd also point out that this effort may reverse some future capex growth (potentially downside to our \$500B '28 estimate), as this asset-light approach to AI infrastructure helps GOOGL's capital efficiency.

The TPU-aaS effort has implications for many companies across the AI ecosystem including:

\- Anthropic: gains additional control of its business model, vertically integrates, and is less exposed to restrictions around hyperscaler service agreements.

\- Broadcom: opens a substantial new revenue pool and diversifies its business to other partners (consistent with our semiconductor research team's companion report on this topic today).

\- Blackstone and others: allows the companies to scale up their investments into new AI infrastructure and financial vehicles.

\- Fluidstack: massively increases its footprint as a colo managed service provider (what the industry calls "smart hands", or managed kubernetes) outside of Google's walls. In our view, Fluidstack's recent fundraise may signal its intentions to become a TPU neocloud.

We view this new business model as a win-win across the ecosystem and should allow TPU to become more of an industry standard for AI developers and other AI labs.

GOOGL OVERWEIGHT Unchanged

U.S. Internet POSITIVE Unchanged

Price Target USD 425.00 Unchanged

Price (23-Jul-26) USD 317.69

Potential Upside/Downside +33.8% Source: Bloomberg, BARC

<table><tr><td>Market Cap (USD mn)</td><td>3889212</td></tr><tr><td>Shares Outstanding (mn)</td><td>12230.00</td></tr><tr><td>Free Float (%)</td><td>98.77</td></tr><tr><td>52 Wk Avg Daily Volume (mn)</td><td>33.9</td></tr><tr><td>Dividend Yield (%)</td><td>0.28</td></tr><tr><td>Return on Equity TTM (%)</td><td>49.55</td></tr><tr><td>Current BVPS (USD)</td><td>50.90</td></tr><tr><td colspan="2">Source: Bloomberg</td></tr></table>

![](images/128a062385cefaae23f730698ae21f994bf5fc911ce99287f3f44766806f3aa1.jpg)  
Source: IDC  
Link to BARC Live for interactive charting

## U.S. Internet

Ross Sandler

+1 415 263 4470

ross.sandler@BARC.com

Alex Hughes  
+1 212 526 3069  
alexander.hughes@BARC.com  
BCI, US

## Background On TPU-As-A-Service

Two major announcements have happened in the past quarter that could be material to GOOGL financials over the coming years. The first was on May 18 $^{th}$ where Blackstone and Google Cloud set up a JV run by a former Google exec to provide TPU-as-a-service to customers, with the first 0.5 GWs coming online in '27 and more capacity into the future $^{1}$ . This was followed up by another mega-deal announcement forming an AI XPV Platform between Broadcom and Blackstone/Apollo, enabling as much as 20 GWs of AI capacity through 2028, with the first >1 GW coming online starting in "mid-2026" $^{2}$ . The latter will involve AI labs bringing both TPUs and other custom ASICs (OpenAI's Jalepeno, etc.) online.

For purposes of this report we only really care about the portion that flows through Google's P+L. These two entities could bring online 15-20 GWs of TPU-as-a-service AI cloud capacity outside of what Google is doing inside GCP.

## First Off, What Is TPU-As-A-Service (TPU-aaS)?

Historically, the only way an AI lab or enterprise customer could access AI specific compute running on Google's TPUs was via Google Cloud Platform (GCP). Customers would enter into agreements with Google to rent AI capacity on various terms. However, this is starting to change in '26 with the new "off platform" structures noted above. In the very near future, AI labs who are the largest buyers of AI compute (Anthropic, OpenAI, Meta, etc.) will be able to buy compute through a new vehicle that allows for more direct control. Broadcom explained it best in their press release: "It also establishes a scalable framework for future deployments of XPU-based compute capacity and networking to enable frontier model training and inference at the lowest cost and lowest power, significantly lowering per-token delivery costs."3 The XPU cost through this new entity is likely to be comparable to buying the same capacity through the existing cloud providers, but offers more control to the AI labs.

## TPU-aaS Entity Structure

Noted above, this new AI XPV Platform was announced in early June by Broadcom, Blackstone, and Apollo. Because we are conducting the analysis from the perspective of impact to GOOGL's shareholders, we are calling it TPU-as-a-service (while Broadcom calls it XPU as it involves non-TPU compute as well, like OpenAI's upcoming Jalepeno chip).

The XPV structure looks a lot like other AI lab compute structures, with a few key layers of the stack. First, Blackstone/Apollo would set up a SPV (special purpose entity) which is financed with equity and debt (collateralized by the compute assets). This SPV would subsequently buy the TPUs from Google, which are co-designed with Broadcom and manufactured by TSMC. These compute assets would go into a datacenter provided by another entity and managed by Fluidstack. Anthropic would then lease the capacity from the SPV at predetermined rates. We have attempted to illustrate this structure below.

FIGURE 1. A Hypothetical 1 GW TPU-aaS Structure  
![](images/0101cc4c35c861e53c9db6465b38ca2228d2539e75747c390cdc1fa1d7230588.jpg)  
Source: BARC Estimates, Company Disclosures

## What Is Google's Incentive?

Investors may ask that if there is only a static number of TPUs being produced in any given year, and if Alphabet as a whole is compute constrained, then why wouldn't the company just keep all the TPUs for itself and continue the existing business model of GCP leasing capacity to others? The answer is likely somewhat complex: 1) there are natural limits around how much AI capex GOOGL can deploy on its own, namely capital and to a lesser degree DC power, 2) unlike traditional cloud computing, select large customers of GCP (like Anthropic, Meta, and others) increasingly demand more control and flexibility and are willing to pay Google for that, 3) the TPU-aaS structure is a capital-light way to standardize more of the AI industry and the developer community around your stack, which could have downstream benefits, and 4) selling TPUs insulates Alphabet from the downstream liabilities that may come up from time to time within AI around copyright, security, privacy, and many other issues that have yet to emerge.

## What Is Anthropic's Incentive? (Or Other AI Labs?)

Large AI labs have scaled on the back of cloud computing contracts, and while this has been a great "asset-light" way of building their businesses, limitations exist. GCP and AWS provide compute services to Anthropic and others, but that's basically it; the AI lab has zero rights beyond what is laid out in the agreement with the hyperscaler.

For Anthropic, the incentives around controlling its own infrastructure have many benefits to its business model. These include: 1) the company can customize compute more effectively at various layers, and owning compute (via SPV) allows much deeper root access to the TPUs that would not likely be granted within GCP, 2) the company can more easily vertically integrate, and 3) while unlikely to happen, controlling the compute insulates Anthropic's business model from any discrepancies in terms stated in hyperscaler cloud service agreements (i.e., violations of AUPs which can result in termination of said agreement).

## Google's Unit Economics

We estimate Google sells each TPU for around \$20k per unit to the SPV while likely earning around a 25% gross margin, or around \$5k gross profit per unit. Each GW in '26 can host around 700k units, or \~\$14B in revenue per GW to Google. Future clusters will have next-generation TPUs (8t, 8i, 9, etc.) whereby revenue per unit and revenue per GW likely moves upward like most compute systems going forward, illustrated below.

FIGURE 2. GOOGL Likely Earning \~25% GM On External TPU-aaS Sales

<table><tr><td>TPU Economics</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Unit Revenue</td><td>20,000</td><td>33,333</td><td>53,333</td></tr><tr><td>- Unit Cost</td><td>15,000</td><td>25,000</td><td>40,000</td></tr><tr><td>Gross Profit</td><td>5,000</td><td>8,333</td><td>13,333</td></tr><tr><td>% Gross Margin</td><td>25%</td><td>25%</td><td>25%</td></tr><tr><td colspan="4">Per GW:</td></tr><tr><td>TPU Revenue ($B)</td><td>14.3</td><td>18.3</td><td>22.0</td></tr><tr><td>TPUs per GW</td><td>714,286</td><td>549,286</td><td>411,964</td></tr></table>

Source: BARC Estimates, Company Disclosures

Broadcom has stated that this new AI XPV initiative amounts to 20 GWs over the next few years. The company has also stated that OpenAI and a few others are designing custom XPUs that would be included in this 20 GWs but separate from Google. We estimate TPU may be as much as 15 GW of the total, illustrated below.

FIGURE 3. Broadcom/Blackstone/Apollo AI XPV Platform GW Breakdown

<table><tr><td></td><td>2026E</td><td>2027E</td><td>2028E</td><td>Total</td></tr><tr><td>TPU GW</td><td>1.4</td><td>3.2</td><td>10.0</td><td>14.6</td></tr><tr><td>Other GW</td><td>--</td><td>--</td><td>--</td><td>5.4</td></tr><tr><td>Total GW</td><td></td><td></td><td></td><td>20</td></tr></table>

Source: BARC Estimates, Company Disclosures

Noted above, Google also has a similar JV structure (outside of Broadcom's announced 20 GW) where it invested alongside Blackstone into a new TPU-aaS entity run by former Google infra exec Ben Treynor Sloss that amounts to another 500 MWs in 2027 and "plans to scale significantly" into the future.

Both of these result in a total of 3.7 GWs in '27 and 11.5 GWs in '28 of potential TPU-aaS external sales, illustrated below.

FIGURE 4. GOOGL Could Have $15+$ GWs Online By 2028

<table><tr><td>External TPU Sales Framework</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Blackstone-Google TPU Cloud JV</td><td></td><td></td><td></td></tr><tr><td># GW</td><td></td><td>0.5</td><td>1.5</td></tr><tr><td># TPUs</td><td></td><td>274,643</td><td>617,946</td></tr><tr><td>Broadcom-Apollo-Blackstone AI XPV Platform</td><td></td><td></td><td></td></tr><tr><td># GW</td><td>1.4</td><td>3.2</td><td>10.0</td></tr><tr><td># TPUs</td><td>1,000,000</td><td>1,757,714</td><td>4,119,643</td></tr><tr><td>Total External TPU GW</td><td>1.4</td><td>3.7</td><td>11.5</td></tr><tr><td># TPUs</td><td>1,000,000</td><td>2,032,357</td><td>4,737,589</td></tr><tr><td>GOOGL Revenue ($B)</td><td>20.0</td><td>67.7</td><td>252.7</td></tr><tr><td>TPU External ASP</td><td>20,000</td><td>33,333</td><td>53,333</td></tr><tr><td>GOOGL Gross Profit ($B)</td><td>5.0</td><td>16.9</td><td>63.2</td></tr></table>

For illustrative purposes  
Source: BARC Estimates, Company Disclosures

Based on the capacity scaling noted above, and using the ASP for the TPUs noted above, we think TPU-as-a-service revenue can reach as much as \$250B in 2028, at which point would represent 35%+ upside to current consensus Alphabet revenue and 15% to gross profit.

FIGURE 5. TPU-aaS Could Represent $15\%$ Potential Upside To Consensus Alphabet GP In '28

<table><tr><td></td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="5">Current Consensus Estimates:</td></tr><tr><td>Alphabet Total Revenue</td><td>402.8</td><td>493.0</td><td>597.9</td><td>711.1</td></tr><tr><td>% Y/Y Change</td><td>36%</td><td>22%</td><td>21%</td><td>19%</td></tr><tr><td>Alphabet Gross Profit</td><td>240.3</td><td>299.2</td><td>361.3</td><td>431.9</td></tr><tr><td>% Margin</td><td>60%</td><td>61%</td><td>60%</td><td>61%</td></tr><tr><td colspan="5">External TPU Contribution:</td></tr><tr><td>External TPU Revenue</td><td></td><td>20.0</td><td>67.7</td><td>252.7</td></tr><tr><td>% Upside to Total Revenue</td><td></td><td>4%</td><td>11%</td><td>36%</td></tr><tr><td>External TPU Gross Profit</td><td></td><td>5.0</td><td>16.9</td><td>63.2</td></tr><tr><td>% Upside to Total Gross Profit</td><td></td><td>2%</td><td>5%</td><td>15%</td></tr></table>

For illustrative purposes

Source: BARC Estimates, Company Disclosures, Bloomberg Consensus as of 7/23/26

This new structure has many benefits to Anthropic's business model (or any other AI lab/TPU customer), noted above, but it also begs the question around just how much more or less a 1 GW TPU-as-a-service cluster may cost in terms of overall capex and annual opex, relative to Anthropic's ability to just rent TPUs directly from GCP. Below we attempt to illustrate a side by side comparison.

FIGURE 6. Difference In AI Lab Unit Economics For GCP Rental Vs.Owned TPU-aaS

<table><tr><td>AI Lab Unit Econ - 1 GW</td><td>GCP</td><td>TPUaaS</td></tr><tr><td>TPUs per GW (m)</td><td>0.7</td><td>0.7</td></tr><tr><td>Training TPUs</td><td>0.4</td><td>0.4</td></tr><tr><td>Inference TPUs</td><td>0.4</td><td>0.4</td></tr><tr><td>Total Capex per GW ($m)</td><td>20,000</td><td>25,000</td></tr><tr><td>TPU Capex per GW ($m)</td><td>10,714</td><td>14,286</td></tr><tr><td>TPU ASP</td><td>15,000</td><td>20,000</td></tr><tr><td>Other Capex per GW ($m)</td><td>9,286</td><td>10,714</td></tr><tr><td>Other Capex per TPU</td><td>13,000</td><td>15,000</td></tr><tr><td>Annual Depreciation Cost per GW ($m)</td><td>4,000</td><td>5,000</td></tr><tr><td>Total Cost per TPU</td><td>28,000</td><td>35,000</td></tr><tr><td>Depreciation/TPU/Year</td><td>5,600</td><td>7,000</td></tr><tr><td>Useful Life (Years)</td><td>5</td><td>5</td></tr><tr><td>AI Lab Inference Revenue per GW ($m)</td><td>6,667</td><td>6,667</td></tr><tr><td>AI Lab Inference Margin</td><td>70%</td><td>63%</td></tr><tr><td>AI Lab Inference Cost per GW</td><td>2,000</td><td>2,500</td></tr></table>

2026E  
Source: BARC Estimates, Company Disclosures

## What's Already Been Announced

Noted above, Broadcom/Blackstone/Apollo's AI XPV initiative spans 20 GWs through 2028. It is not yet clear how big the Blackstone-Google JV TPU project (outside of the AI XPV initiative) is going to be longer term but has already announced 500 MWs in '27. We have identified the first tranches of datacenters coming online to support these efforts from TeraWulf and others, illustrated below.

We estimate Google has around \$88B of TPU revenue in the backlog as of 2Q26. This number should ramp up to over \$300B cumulative over time, but obviously some revenue starts dropping out of the backlog once TPUs have been sold through.

FIGURE 7. What's Already Been Announced From Compute DC Providers

<table><tr><td></td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>1Q27</td><td>2Q27</td><td>3Q27</td><td>4Q27</td></tr><tr><td>AI Compute Capacity by Shell Provider (MW)</td><td>42</td><td>457</td><td>901</td><td>798</td><td>924</td><td>960</td><td>1,019</td></tr><tr><td>Terawulf</td><td>42</td><td>168</td><td>336</td><td>50</td><td>50</td><td>162</td><td>320</td></tr><tr><td>Cipher Digital</td><td></td><td>168</td><td>39</td><td></td><td></td><td>50</td><td>200</td></tr><tr><td>Next Frontier (Coatue)</td><td></td><td></td><td>300</td><td></td><td>130</td><td></td><td></td></tr><tr><td>Hut 8</td><td></td><td></td><td></td><td></td><td>245</td><td></td><td></td></tr><tr><td>Estimated Undisclosed Capacity</td><td>0</td><td>121</td><td>226</td><td>748</td><td>499</td><td>748</td><td>499</td></tr><tr><td>Cumulative Compute (MW)</td><td>42</td><td>499</td><td>1,400</td><td>2,198</td><td>3,122</td><td>4,081</td><td>5,100</td></tr><tr><td>Implied TPU Revenue ($B)</td><td>$0.6</td><td>$6.5</td><td>$12.9</td><td>$14.6</td><td>$16.9</td><td>$17.6</td><td>$18.7</td></tr><tr><td>Cumulative TPU Revenue ($B)</td><td>$0.6</td><td>$7.1</td><td>$20.0</td><td>$34.6</td><td>$51.5</td><td>$69.1</td><td>$87.7</td></tr><tr><td>% of 2Q26 Cloud Backlog</td><td>0.1%</td><td>1.4%</td><td>3.9%</td><td>6.7%</td><td>10.0%</td><td>13.4%</td><td>17.1%</td></tr><tr><td>Cumulative TPU COGS ($B)</td><td>$0.5</td><td>$5.4</td><td>$15.0</td><td>$26.0</td><td>$38.6</td><td>$51.8</td><td>$65.8</td></tr><tr><td>% of 2Q26 Purchase Commitments</td><td>0.1%</td><td>0.9%</td><td>2.5%</td><td>4.3%</td><td>6.4%</td><td>8.5%</td><td>10.8%</td></tr><tr><td>Inventory Balance</td><td>$10.0</td><td>$11.4</td><td>$14.4</td><td>$15.6</td><td>$16.8</td><td>$17.9</td><td>$19.6</td></tr></table>

Source: BARC Estimates, Company Disclosures

## Estimate Changes and Valuation

We have done a complete overhaul of our Google Cloud segment to factor in TPU-aaS revenues and profits. Google's CFO provided some high-level explanation of how TPU-aaS may flow through the company's financial statements last night, and combined with the new inventory line on the BS and the \$811B in purchase commitments, we can now piece together what this may look like.

We fully appreciate that our estimates are moving upwards rather dramatically on this revision, but as of now this is our best estimate of how the next three years may play out.

FIGURE 8. Estimate Changes

<table><tr><td rowspan="2"></td><td colspan="3">3Q26E</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old Est.</td><td>Delta</td><td>New</td><td>Old Est.</td><td>Delta</td><td>New</td><td>Old Est.</td><td>Delta</td><td>New</td><td>Old Est.</td><td>Delta</td></tr><tr><td colspan="13">Google Services</td></tr><tr><td>Search Revenue</td><td>64,486.4</td><td>64,486.4</td><td>0.0%</td><td>259,428.9</td><td>259,428.9</td><td>0.0%</td><td>285,371.8</td><td>285

[中间内容因长度限制已省略]

rporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.

<table><tr><td colspan="2">U.S. Internet</td></tr><tr><td>Owen Clendenin</td><td>Alexander Kessinger</td></tr><tr><td>+1 212 526 7518</td><td>+1 212 526 1324</td></tr><tr><td>owen.clendenin@BARC.com</td><td>alexander.kessinger@BARC.co</td></tr><tr><td>BCI, US</td><td>m</td></tr><tr><td></td><td>BCI, US</td></tr></table>
"""
