You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Australian Retail & Consumer Sector

# How are Companies Using AI in Our Coverage?

# Benchmarking AI adoption across Australian retail & consumer coverage

AI is a transformative technology that has the potential to change the competitive position of Retail & Consumer companies within our coverage universe, both in absolute and relative to peers. We have leveraged the AI benchmarking analysis utilised by our US Softlines Retail peers. This scorecard of 6 components, with a score attributed (0, 0.5, 1) covers: (1) Supply Chain & Logistics; (2) Marketing; (3) Sales & Customer Experience; (4) Store Operations; (5) Organization & Support Functions; and (6) Product Development & Innovation. This data is based on publicly available information, which may not incorporate all progress in AI for each company with commerciality a possible reason for silence, while there may be an incentive for some companies to overstate the primacy of AI in their actions given increased investor focus. Despite these limitations, this is an important benchmark to provide an initial comparison across our coverage.

# The highest share of AI uses across coverage, use cases and financial impact

Organisation & support (83% of relevant companies use across our coverage): uses include internal LLM tools, strategic partnerships, and governance. Marketing (83%): uses include personalised marketing, promotional optimisation, proprietary datasets, retail media, and content creation. Sales & customer experience (72%): uses include customer facing agents, search tools, contact centres, and quality control. Supply chain & logistics (72%): uses include demand & inventory forecasting, fulfilment & execution, AI in distribution centres, eCommerce, and weather forecasting. Store operations (44%): uses include frontline AI assistants, markdown tools, security & stock loss, rostering optimisation, eCommerce fulfilment, and agentic systems. Product development & innovation (21%): uses include product design & speed to market, range optimisation and consumer trend recognition. Key ROI drivers include lower CODB, lower COGS, higher revenue and working capital efficiency, noting these gains may be moderated by some AI headwinds for our coverage from a competition, consumer & cost perspective.

# AI leaders in our coverage include WES, COL, WOW, EDV, BRG

AI is being used by all companies in our coverage, yet implementation & disclosure varies widely, favouring the larger names in our coverage. Of the 18 companies we analysed, only WES received a score of 1.0/1.0 which indicates meaningful AI adoption across all applicable dimensions. Other companies that scored well were COL (0.83), WOW (0.83), EDV (0.83) & BRG (0.80). Companies that did not score as well were PMV (0.08), UNI (0.17) & LOV (0.33), based on our analysis.

# What are the attributes of the most well positioned companies using AI?

The attributes of companies most well positioned to harness the benefits of AI are evolving and not fully settled. To date, the attributes of the better positioned companies are: (1) large, high quality first-party data sets often from long standing loyalty programmes; (2) usage having evolved from quantity to sophistication, extending across the entire business rather than specific use cases so benefits compound; and (3) have significant in-house AI organisational capability including governance, with these companies able to access some of the financial benefits identified, although investment is required. Larger companies are initially better positioned, noting most companies in our coverage are large in their industry, while smaller companies are also able to benefit with specific projects able to drive improvement. We anticipate providing further use cases of AI across our coverage, with our US Softline Retail peers identifying 10 specific use cases, with use more advanced in the United States vs Australia.

# Equities

Australia

Retail

Shaun Cousins

Analyst

shaun.cousins@ubs.com

+61-2-9324 3844

James Meares

Analyst

james.meares@ubs.com

+61-29-324 3575

Zack Pontey

Associate Analyst

zack.pontey@ubs.com

+61-2-9324 2475

# AI SCORECARD

# AI Scorecard Methodology

The AI Scorecard leverages the work of the UBS US Softline Retail team which deployed this scorecard across its own coverage. Each company is assessed across six dimensions of AI adoption, with scores of 0 (no evidence), 0.5 (partial or emerging evidence) or 1 (clear adoption), and an overall score calculated as the average across all applicable dimensions, excluding those deemed not relevant (NA). The dimensions assessed include: (1) Supply Chain & Logistics; (2) Marketing; (3) Sales & Customer Experience; (4) Store Operations; (5) Organization & Support Functions; and (6) Product Development & Innovation.

Figure 1: AI Scorecard - UBS Retail & Consumer Coverage 

<table><tr><td>Company</td><td>Supply Chain &amp; Logistics</td><td>Marketing</td><td>Sales &amp; Customer Experience</td><td>Store Operations</td><td>Organisation &amp; Support</td><td>Product Development &amp; Innovation</td><td>Overall AI Adoption Score</td></tr><tr><td>WES</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.00</td></tr><tr><td>COL</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.83</td></tr><tr><td>WOW</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.83</td></tr><tr><td>EDV</td><td>0.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.83</td></tr><tr><td>BRG</td><td>1.0</td><td>1.0</td><td>1.0</td><td>NA</td><td>1.0</td><td>0.0</td><td>0.80</td></tr><tr><td>TWE</td><td>1.0</td><td>1.0</td><td>0.0</td><td>NA</td><td>0.5</td><td>1.0</td><td>0.70</td></tr><tr><td>HVN</td><td>0.5</td><td>1.0</td><td>1.0</td><td>0.0</td><td>1.0</td><td>NA</td><td>0.70</td></tr><tr><td>GYG</td><td>0.5</td><td>1.0</td><td>0.5</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.67</td></tr><tr><td>DMP</td><td>0.0</td><td>0.5</td><td>0.5</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.50</td></tr><tr><td>ADH</td><td>0.0</td><td>1.0</td><td>1.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.50</td></tr><tr><td>AX1</td><td>0.5</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>NA</td><td>0.50</td></tr><tr><td>JBH</td><td>0.5</td><td>1.0</td><td>0.5</td><td>0.0</td><td>0.5</td><td>NA</td><td>0.50</td></tr><tr><td>MTS</td><td>1.0</td><td>0.0</td><td>0.5</td><td>0.0</td><td>1.0</td><td>NA</td><td>0.50</td></tr><tr><td>SIG</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.5</td><td>1.0</td><td>0.0</td><td>0.42</td></tr><tr><td>SUL</td><td>0.5</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.42</td></tr><tr><td>LOV</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.33</td></tr><tr><td>UNI</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.17</td></tr><tr><td>PMV</td><td>0.0</td><td>0.5</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.08</td></tr></table>

Source: Company data, news & press releases. All publicly disclosed information. UBSe. NA not included in respective company scores. \*Limitations: Analysis based solely on publicly disclosed company information. Firms with more transparent or proactive communication may appear more advanced, while others may have significant but undisclosed activity. Scoring involves qualitative judgement. Higher scores indicate broader/clearer disclosure, but not necessarily better execution or returns. The analysis is static and may not fully reflect the pace of AI adoption nor be exhaustive.

Figure 2: Key AI use cases and ROI drivers across UBS Consumer & Retail coverage 

<table><tr><td>Business Segment</td><td>Coverage Usage</td><td>Key examples</td><td>ROI Drivers</td></tr><tr><td>Supply Chain &amp; Logistics</td><td>72%</td><td>- Demand forecasting &amp; Inventory (WES, COL, BRG, GYG, AX1, JBH, SIG, SUL, MTS, LOV)- Fulfilment speed and execution (WES, COL, WOW)- AI technology in distribution centres (COL, WOW)- E-commerce delivery efficiency &amp; optimisation (COL, WOW, HVN)- Weather forecasting (TWE)</td><td>Revenue, COGS, CODB, Working Capital</td></tr><tr><td>Marketing</td><td>83%</td><td>- Personalised marketing &amp; promotional optimisation (COL, WOW, EDV, DMP, ADH, AX1, JBH, SUL, LOV)- Proprietary datasets (WES, COL, WOW)- Retail media effectiveness (WES, WOW, EDV, JBH)- Content creation (EDV, TWE, HVN, PMV)</td><td>Revenue, COGS, CODB</td></tr><tr><td>Sales &amp; Customer Experience</td><td>72%</td><td>- Customer facing agents (WES, WOW)- Search tools (WES, COL, EDV, BRG, ADH, MTS, UNI)- Contact centres/customer service (WES, BRG, HVN, ADH, LOV, UNI)- Quality control (DMP)</td><td>Revenue, COGS, CODB</td></tr><tr><td>Store Operations</td><td>44%</td><td>- Frontline AI assistants (WES, WOW)- Markdown tools (WES, COL)- Security &amp;/or stock loss (WES, COL, EDV)- Rostering optimisation (COL, WOW, EDV, DMP)- eCommerce fulfillment (WOW)- Agentic systems &amp; food safety (GYG)</td><td>Revenue, COGS, CODB, Working Capital</td></tr><tr><td>Organisation &amp; Support</td><td>83%</td><td>- Internal LLM tools &amp; strategic partnerships (WES, COL, WOW, EDV, BRG, HVN, GYG, DMP, ADH, AX1, SIG, SUL, JBH, MTS)- Governance (WES, WOW, BRG, TWE, HVN, DMP, SIG, SUL, MTS)</td><td>CODB</td></tr><tr><td>Product Development &amp; Innovation</td><td>21%</td><td>- Product design &amp;/or speed to market (WES)- Range optimisation (EDV)- Consumer trend recognition (TWE)</td><td>Revenue, COGS, Working Capital</td></tr></table>

Source: Company data, news & press releases. All publicly disclosed information. UBSe. \*Note: Coverage usage calculation includes any evidence of usage (0.5 & 1 scores), and excludes companies with NA scores.

# WESFARMERS (WES-AU)

Figure 3: WES AI Scorecard 

<table><tr><td>AI Dimension</td><td>WES Score</td><td>Max score</td><td>Key Evidence/Examples</td></tr><tr><td>Supply Chain &amp; Logistics</td><td>1.0</td><td>1.0</td><td>Demand forecasting: Data driven AI &amp; &quot;Machine Learning&quot; to support inventory optimisation and replenishment. Officeworks has integrated Gen AI agents into order management systems to improve fulfilment speed and execution.</td></tr><tr><td>Marketing</td><td>1.0</td><td>1.0</td><td>Personalisation: OneData supports targeted promotions and cross-brand campaigns. Measurement: AI led segmentation to improve measurement of advertising effectiveness.</td></tr><tr><td>Sales &amp; Customer Experience</td><td>1.0</td><td>1.0</td><td>Digital experience: &quot;Search with OnePass&quot; (AI powered), &quot;Buddy&quot; AI agentic shopping assistant. Service quality: GenAI in contact centres.</td></tr><tr><td>Store Operations</td><td>1.0</td><td>1.0</td><td>Labour productivity: AI assistants for frontline team, real-time technical product information, AI driven markdown tool saving duplicated manual effort. Security: AI Facial recognition to protect frontline team members &amp; combat store crime.</td></tr><tr><td>Organisation &amp; Support</td><td>1.0</td><td>1.0</td><td>AI capability: Microsoft 365 Copilot, strategic partnerships with Google &amp; Microsoft. Upskilling &amp; governance: Internal training &amp; a formal AI governance policy, AI risk oversight.</td></tr><tr><td>Product Development &amp; Innovation</td><td>1.0</td><td>1.0</td><td>Product design: AI use in private label product development (Kmart).</td></tr><tr><td>Overall AI Adoption Score</td><td>1.00</td><td colspan="2"></td></tr></table>

Source: Company data, news & press releases. \*All publicly disclosed information. UBSe.

# Supply Chain & Logistics: Score 1/1

\- WES leverages AI & machine learning across its supply chain particularly within its retail divisions Bunnings, Kmart & Officeworks. Key areas include demand forecasting, inventory optimisation, availability & speed. For example, Kmart pairs predictive modelling with RFID-enabled inventory visibility to improve on-shelf availability. Officeworks has integrated Gen AI agents into order management systems to improve fulfilment speed and execution.

# Marketing: Score 1/1

- AI led segmentation via OneReach (WES' retail media network, supported by OneData), has enabled closed-loop measurement of advertising effectiveness.   
- OneData, WES' group shared data asset houses 12.5m unique customer records (2025 Strategy day transcript) powering proprietary data capability (FY25 Result transcript).

# Sales & Customer Experience: Score 1/1

- Bunnings has recently released its new 'Buddy' AI-powered agentic shopping assistant which is replacing the existing 'Ask Bunnings AI' tool.   
- Search with OnePass, an AI powered tool to shop across multiple retail brands.   
- Gen AI has been deployed in contact centres to improve response times and service quality.

# Store Operations: Score 1/1

- Frontline retail members are equipped with AI assistants, enabling staff to access technical information in real-time, improving productivity & service quality.   
- AI driven price markdown tool in Bunnings saving \~100,000 hours of duplicated manual effort (1H26 Result transcript)   
- Al Facial recognition to protect frontline team members & combat store crime.

# Organisation & Support Functions: Score 1/1

- Strategic partnerships with Microsoft & Google to access leading global AI talent, alongside AI tools (Microsoft Copilot).   
- AI upskilling internally across its \~120k person workforce, with a formal AI Governance Policy, impact assessments & AI risk oversight.

# Product Development & Innovation: Score 1/1

\- 3D design/ digitisation of Kmart sourcing suggest AI use in speed to market & product design within Kmart.

# COLES (COL-AU)

Figure 4: COL AI Scorecard 

<table><tr><td>AI Dimension</td><td>COL Score</td><td>Max score</td><td>Key Evidence/Examples</td></tr><tr><td>Supply Chain &amp; Logistics</td><td>1.0</td><td>1.0</td><td>Demand forecasting: Machine learning applied across inventory forecasting, demand planning, ranging, and workflow and transport optimisation. Exploring digital twin capabilities. E-Commerce: AI enabled CFCs, predictive AI to optimise last-mile delivery.</td></tr><tr><td>Marketing</td><td>1.0</td><td>1.0</td><td>Personalisation: Flybuys loyalty enables AI-driven personalised content and data-led marketing.</td></tr><tr><td>Sales &amp; Customer Experience</td><td>1.0</td><td>1.0</td><td>Customer experience: AI product recommendations, basket building tools, augmented customer care, and enhanced search.</td></tr><tr><td>Store Operations</td><td>1.0</td><td>1.0</td><td>Productivity: Optimised rostering, dynamic markdowns, and improved workflows. Digitised in-store inventory management. Stock Loss: AI prevention &amp; computer vision to monitor POS activity.</td></tr><tr><td>Organisation &amp; Support</td><td>1.0</td><td>1.0</td><td>Internal tools: OpenAI ChatGPT Enterprise deployment at scale. Flagship &quot;mycoles assistant&quot;.</td></tr><tr><td>Product Development &amp; Innovation</td><td>0.0</td><td>1.0</td><td>COL has not publicly disclosed AI-driven product development or R&amp;D initiatives related to private label formulation or design</td></tr><tr><td>Overall AI Adoption Score</td><td>0.83</td><td></td><td></td></tr></table>

Source: Company data, news & press releases. \*All publicly disclosed information. UBSe.

# Supply Chain & Logistics: Score 1/1

- Machine learning is applied across inventory forecasting, demand planning, ranging, workflow and transport optimisation.   
- COL operates two Ocado powered Customer Fulfilment Centres (CFCs) that employ an AI driven "air traffic control" system to manage a dense 3D grid and coordinate over 700 robots on each grid.   
- Predictive AI optimises last mile delivery based on real-time traffic data and vehicle tonnage, improving delivery speed and fuel efficiency.   
- COL is exploring emerging digital twin capabilities to support more end-to-end supply chain orchestration and optimisation, including more dynamic management of capacity and fulfilment across the network.

# Marketing: Score 1/1

\- The Flybuys loyalty programme (jointly owned with WES), enables AI driven personalisation and data-led marketing.

# Sales & Customer Experience: Score 1/1

\- Implemented AI features to improve customer experience include product recommendations, basket building tools, augmented customer care and enhanced search capabilities.

# Store Operations: Score 1/1

- AI has allowed optimised rostering, dynamic in-store markdown and improved workflows. Team members are dynamically prioritised to certain activities and rostering, reducing member churn by 25% and 80% of staff now work preferred shifts (2024 Investor day transcript).   
- GenAI & computer vision embedded into checkout systems and exit gates, monitoring point of sale activity in order to prevent stock loss.

# Organization & Support Functions: Score 1/1

- Major collaboration with OpenAI, as the first major Australian retailer to deploy ChatGPT enterprise at scale.   
- Flagship internal tool the "mycoles assistant", a generative AI knowledge assistant integrated into the staff portal.

# Product Development & Innovation: Score 0/1

\- No explicit disclosure regarding AI use in product development.

# WOOLWORTHS (WOW-AU)

Figure 5: WOW AI Scorecard 

<table><tr><td>AI Dimension</td><td>WOW Score</td><td>Max score</td><td>Key Evidence/Examples</td></tr><tr><td>Supply Chain &amp; Logistics</td><td>1.0</td><td>1.0</td><td>E-Commerce Fulfillment: Store-based picking optimisation, KNAPP robotic systems &amp; automation at Customer Fulfillment Centres (CFCs), AI telematics across driving fleet. Logistics optimisation: Transport routing, delivery windows, crate utilisation &amp; last-mile delivery fleet allocation.</td></tr><tr><td>Marketing</td><td>1.0</td><td>1.0</td><td>Personalisation: AI enabled Everyday Rewards, Machine learning models for tailored offers, &quot;Next Gen Promos&quot; improving promotional ROI. Marketing assistant supporting E2E campaign process.</td></tr><tr><td>Sales &amp; Customer Experience</td><td>1.0</td><td>1.0</td><td>AI Agents: Rollout of Olive (customer facing) &amp; other internal agents (Mandy, Dot) to automate customer service contracts.</td></tr><tr><td>Store Operations</td><td>1.0</td><td>1.0</td><td>Productivity: AI prioritisation tool Quick Assist used by ~6,000 team leaders. Rostering: AI driven rostering models to align labour to forecast demand.</td></tr><tr><td>Organisation &amp; Support</td><td>1.0</td><td>1.0</td><td>Team Tools: AI tools such as Gemini &amp; Team Coach, supported by wiqLABS, identifying &gt;1,500 GenAI use cases. G

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/c68bf75c9351f76c2c0507357127c6995e99fab4a34d6d6422ee46f48bf2d2ef.jpg)
"""
