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
June 15, 2026 10:19 AM GMT

## Semiconductors | North America

# Takeaways from public company meetings on our bus tour

We summarize positive meetings with CEOs of ALAB, MRVL, INTC.

## Key Takeaways

■ ALAB remains confident in the scale-up opportunity both short and long term  
Marvell showing new levels of confidence about everything, especially scale-up  
Intel CEO shows commitment to foundry, positive on microprocessors  
Private company writeups coming later this week – focus on scale-up and low-latency inference

## ALAB

Management expects content per XPU to continue growing from roughly \~\$1,000 today as AI infrastructure becomes more interconnect-intensive. The company is investing across optical, UAL, and NVL, and highlighted that customers are increasingly describing Astera's large PCIe switch as an "NVSwitch for the open ecosystem."

While some workloads and protocols will move elsewhere, PCIe is expected to continue growing for at least the next several years. PCIe remains particularly important in China, where many AI systems are add-in-card-based and therefore PCIe-native. Management sees China as a meaningful opportunity because less powerful GPUs require more interconnect, though it does not expect China to be larger than the U.S. in PCIe scale-up.

For the emerging UAL opportunity, management is confident in its competitive position but does not think the switch opportunity will be winner takes all. First deployments expected next year, with a bigger ramp in 2028.

CXL and memory pooling are still nascent, but management sees growing relevance as inference drives KV-cache offload demand. CXL has not lived up to expectations so far, but management expects revenue in 2027, with both smaller AI platform providers and hyperscalers qualifying systems. Management also noted demand from customers wanting to use DDR4 via CXL to extend server memory lifespans as new CPUs do not support DDR4 directly.

On CPO / NPO, management argued that the most important factor is owning a switch product that optics can attach to. Astera demonstrated PCIe 6 over LPO at Computex and expects NPO deployments first in 2027. If NPO works, it may push out CPO for some customers, while NVDA can move directly to CPO. Astera's

MS & CO. LLC

## Joseph Moore

Equity Analyst

Joseph.Moore@morganstanley.com +1 212 761-7516

## Mason Wayne

Research Associate

Mason.Wayne@morganstanley.com +1 212 761-6012

## Shane Brett

Equity Analyst

Shane.Brett@morganstanley.com +1 212 761-1022

## Nicole Kozhukhov

Research Associate

Nicole.Kozhukhov@morganstanley.com +1 212 761-1636

## Ella Tulchinsky

Research Associate

Ella.Tulchinsky@morganstanley.com +1 212 761-2222

## SEMICONDUCTORS

North America

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

aiXscale acquisition is expected to generate qualifying revenues in 2027, while CPO for scale-up is more likely a 2028 opportunity at minimum, with perhaps one customer earlier. The company sees an advantage from having electrical IC, PIC, and aiXscale capabilities to produce a full optical engine.

Despite optical enthusiasm, management expects copper to remain relevant inside the rack. Many scale-up links are passive today and may only add retimers, while rack-to-rack connectivity will move to optical because 400G rack-to-rack cannot be copper. This transition should be positive for revenues: even if retimer content is lost when links move to NPO, as the new optical link is materially more valuable. Astera believes its incumbent position in copper links, Cosmos software, and broad suite of standard-specific products reduce the risk of share loss.

Strategically, management contrasted Astera's focus with companies that "invest in everything." Astera is focused on areas where it believes it can win, including a \~\$10bn UAL TAM and NVL Fusion content. The company could build scale-up Ethernet switches, but customers are currently asking it to focus on PCIe. Management framed the 2030 market as roughly \$10bn PCIe TAM and \$10bn Ethernet TAM, with NVL and ICI solutions likely among the largest parts of a broader >\$100bn market, though not quantified.

On custom silicon, management sees opportunities from new XPUs and NVL Fusion. The company wants solutions for all major architectures and is willing to do custom I/O. NVL Fusion is its first custom engagement in this category, but management noted many more requests. ASIC vendors like AVGO will still have influence, through COT programs the hyperscaler can enforce their preferred scale-up architecture.

## In-house SerDes development intended to intercept the optical inflection.

Management wants to be selective about where it invests in custom SERDES, but sees a need around optical, and has the internal team in place. The company's philosophy is to buy IP off the shelf where available to improve opex efficiency, but build internally when required.

Our take: We are OW the stock, and remain very positive heading into the Amazon Trainium 3 scale-up ramp in 2h, and see positive prospects to migrate that to UALink/NVLink Fusion/optical opportunities longer term, though conceding that the strong run-up in the stock price creates a high bar.

## Marvell

Marvell framed the AI opportunity as increasingly interconnect-driven, today most growth is coming from scale-out but there is a significant scale-up / scale-across opportunity still ahead. The company's model contemplates custom growing from \~\$4bn to \~\$10bn, legacy segments starting at a\~\$2.5bn base growing roughly with GDP, and \~\$10bn of connectivity growing \~70% with no near-term slowdown. Management also noted that none of the potential agentic-AI CPU uplift is included in current numbers; more agentic workloads could drive additional NICs, CXL, and switches.

## The core message was that Marvell's breadth is becoming a competitive

advantage. The company positioned itself as one of the few vendors spanning DCI, die-to-die IP, scale-out switching, scale-up switching, optics, SerDes, CXL, NICs, and custom silicon. Management argued this full-stack position matters more as customers confront constrained supply chains and the complexity of integrating switches, optics, third-party IP, and XPUs.

On scale-up, Marvell sees multiple optionality vectors across UAL, ESUN, and NVL Fusion. Management framed scale-up switching as still up for grabs, but scale-up optics as an area where Marvell expects to be number one in merchant solutions. The company also argued that customer preference for non-AVGO alternatives should support Marvell's position, particularly where software, silicon, and optical integration matter.

On XPUs, management sees the potential for upside to its medium-term targets, cautioned investors on over-extrapolating supply-chain datapoints. It continues to focus on higher-margin custom opportunities and believes inference creates more shots on goal.

On supply chain, Marvell says it runs five-year rolling forecasts with suppliers and is getting upside, with interconnect providing more flexibility than custom compute.

Our take: The enthusiasm and confidence both short and long term are very clear, and seem justified to us; however we struggle with the valuation at 2.5x NVDA multiple for a company that has not outgrown NVDA in a long while.

## Intel

For new CEO Lip-Bu Tan, the initial priority was cultural now that focus has shifted toward finding ways to grow the business and executing on the product roadmap.

In CPUs, management highlighted the hiring of Alex Katouzian as important for improving low-power competitiveness and deepening Arm-related expertise.

There were definite changes to be made to the server roadmap, such as bringing back SMT and the P-core / E-core distinction. But management is more confident in the roadmap today, emphasizing that execution is the key variable; if Intel executes, management believes the company can stop losing share in roughly nine months. Agentic AI should be a long-term driver of CPU demand, suggesting that CPU/GPU ratios could reach 4:1 in some contexts.

The x86 ecosystem remains an area of strength Intel is leaning into, where there is potential in vertical markets where x86 customization creates differentiation, which is not something Intel has considered historically.

Lip-Bu has also made the decision to do double down on foundry, believing that the internal product engine and external foundry business should reinforce each other, while external manufacturing remains part of the model where appropriate. Intel wants to remain a top-10 TSMC customer, but believes having both internal and external options create healthy competitive tension and improve customer confidence.

14A is the critical foundry milestone. Management said all Intel-designed products will move to 14A, and early process indicators are improving. Intel is seeing roughly 0.5 defect density and \~40% yield, with a goal of reaching 0.1-0.2 defect density by Q1 next year. Customer conversations are improving and PDF/KLA support was highlighted as part of the effort to accelerate foundry readiness. The 14A 0.5 PDK is out and 0.9 is expected in October. Risk production is framed around 2028 and volume around 2029, broadly comparable to TSMC timing. As an IDM, Intel expects to run internal test chips in 2027, which should give the company a proving ground before external customer volume ramps.

Given the shortage at the leading edge, Lip-Bu said the board is now asking Intel to invest more in capex and that the message has been received. The board is more confident than before, but Intel still needs to prove that incremental spend can translate into customer wins, volume, and margin recovery. Initially, management suggested volume is more important than margin, particularly in foundry, where scale and customer confidence are prerequisites.

On capacity, Intel said Oregon and Arizona have room to expand, and Ohio will be accelerated. Germany has been shut down, but management is now concerned Intel may not have enough capacity if demand continues to improve. TerraFab was discussed as a potential additional platform, though nothing has been announced.

Management also described EMIB as a “secret weapon” with strong technology and large customer potential, but also meaningful complexity and reliability questions. Individual customer opportunities could be worth billions, but execution depends on building the right team, improving automation, and proving reliability at scale.

Management sees advanced packaging as a potential bottleneck across the AI infrastructure ecosystem, which could create an opening for Intel if it can execute. Intel also noted substrate constraints, including the need to prepay in some cases.

We note that our recent Asia checks were a bit mixed on EMIB, and some of the current wins being reported have yet to be completely secured.

The memory shortage is also a focus area for Intel and its partners. Intel does not have the balance sheet of a company like NVDA to secure DRAM, but management said the company needs to be more aggressive in this area.

Our take: We have missed the move in Intel's stock, largely because of concerns on the roadmap, which we still have; we think expectations of share gains vs. AMD seem premature, given AMD's stated ability to procure more wafers for its leadership Venice product. That said, shortages of advanced process nodes, and shortages of CPUs, are certainly a positive backdrop for near-term earnings.

## Valuation Methodology and Risks

## Astera Labs Inc (ALAB.O)

We use 0.53x CY27 EV/sales/growth (\~21x ev/sales), assuming a 40% revenue CAGR. This is a premium to AI peers

## Risks to Upside

■ Increase AI spend to propel data center revenue  
■ Quicker upgrade of underlying technology driving content growth  
■ New product launches increasing TAM

## Risks to Downside

■ Increased competition reduces Astera's market share meaningfully  
■ Pause in AI spend and data center investment halts future revenue growth  
■ CXL servers and 1.6T port speeds are significantly delayed, preventing new products from gaining traction

## Intel Corporation (INTC.O)

\~42x EPS CY2027 EPS of \$1.73, 42x is above the high end of the large cap logic semi peer group, reflecting high leverage potential on numbers that are still depressed, and foundry optionality, despite our longer term skepticism

## Risks to Upside

■ Foundry partnerships de-risk the story and further improve the multiple  
■ The company regains lost share in desktop and server following CPU shortages

## Risks to Downside

■ AMD competition increasingly becomes more significant, which could lead to further share losses in processors and pressure on ASPs  
■ Minimal success in foundry leads to an inflated cost structure

## Marvell Technology Group Ltd (MRVL.O)

\~40X CY27e Base Case MW EPS \$4.98, in-line with high growth AI semis

## Risks to Upside

■ AI opportunities (Inphi optical businesses) realize earlier than expected  
■ Cloud custom silicon projects are larger than expected  
■ The storage market recovers

## Risks to Downside

■ AI opportunities are smaller than expected  
■ The strength we estimate for Storage and Networking surprise to the downside  
■ Enterprise DC and Networking continue to weigh on results

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Shane Brett; Nicole Kozhukhov; Joseph Moore; Ella Tulchinsky; Mason Wayne.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Advanced Micro Devices, Aeva Technologies Inc, Ambarella Inc, Amkor Technology Inc, Analog Devices Inc., Arm Holdings plc, Astera Labs Inc, Broadcom Inc., Cadence Design Systems Inc, Cerebras Systems, Intel Corporation, IonQ Inc, Marvell Technology Group Ltd, Microchip Technology Inc., Micron Technology Inc., NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Qorvo Inc, Qualcomm Inc., SanDisk Corporation., Semtech Corp., Silicon Laboratories Inc., Skyworks Solutions Inc, Synopsys Inc., Texas Instruments, Wolfspeed, INC.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Aeva Technologies Inc, Analog Devices Inc., Broadcom Inc., Cerebras Systems, GlobalFoundries Inc, Intel Corporation, NXP Semiconductor NV, ON Semiconductor Corp., Semtech Corp..

Within the last 12 months, MS has received compensation for investment banking services from Advanced Micro Devices, Aeva Technologies Inc, Allegro Microsystems Inc, Amkor Technology Inc, Analog Devices Inc., Broadcom Inc., Cerebras Systems, Intel Corporation, IonQ Inc, Micron Technology Inc., NXP Semiconductor NV, ON Semiconductor Corp., Semtech Corp., Texas Instruments.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Advanced Micro Devices, Aeva Technologies Inc, Allegro Microsystems Inc, Ambarella Inc, Amkor Technology Inc, Analog Devices Inc., Arm Holdings plc, Astera Labs Inc, Broadcom Inc., Cadence Design Systems Inc, Cerebras Systems, GlobalFoundries Inc, Intel Corporation, IonQ Inc, Marvell Technology Group Ltd, Microchip Technology Inc., Micron Technology Inc., Navitas Semiconductor Corp, NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Qualcomm Inc., SanDisk Corporation., Semtech Corp., Silicon Laboratories Inc., Skyworks Solutions Inc, Synopsys Inc., Texas Instruments, Wolfspeed, INC.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Advanced Micro Devices, Ambarella Inc, Amkor Technology Inc, Analog Devices Inc., Broadcom Inc., Cadence Design Systems Inc, GlobalFoundries Inc, Intel Corporation, Marvell Technology Group Ltd, Microchip Technology Inc., Micron Technology Inc., NVIDIA Corp., NXP Semiconductor NV, ON Semiconductor Corp., Qualcomm Inc., Silicon Laboratories Inc., Synopsys Inc., Texas Instruments.

Within the last 12 months, MS has provided or is providing inve

[中间内容因长度限制已省略]

available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/12/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$511.57</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$24.89</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$50.41</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$67.78</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$82.78</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$417.79</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$367.15</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$382.07</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$214.00</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$81.38</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$124.57</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$57.85</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$279.70</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$95.24</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$981.61</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$23.39</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$205.19</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$304.86</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>E (05/11/2025)</td><td>$116.79</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$98.59</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>U (02/10/2026)</td><td>$211.72</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,980.10</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$166.71</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$219.51</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$73.97</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$301.12</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$43.14</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$380.81</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$384.96</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$453.89</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
