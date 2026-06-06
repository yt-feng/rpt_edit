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
# China Insurance: Financials trip takeaways

We spent five days (May 25-29) in mainland China, meeting a broad set of financial companies, including banks, insurers, brokers, and online lending platforms. Among insurers, we met the IR and management teams of Ping An, CPIC, China Taiping, ZhongAn (not covered), China Life, NCI, and PICC P&C.

Life insurers remain confident of strong growth in the bancassurance channel and expect the tightening of channel expense supervision to benefit the large insurers. On the asset side, strong equity market performance since the end of March has driven a rebound in investment results, but insurers mostly see stable equity allocation at the current level, emphasizing a balanced portfolio between growth and dividend stocks. P&C insurers generally expect to see improvements in underwriting results, as a result of expense regulation (both auto & non-auto insurance) and reductions in claims frequency (auto insurance).

Overall, we believe industry fundamentals are solid, with continued new policy sales momentum for lifers, and profit and book value growth recovery for all insurers following the equity market rebound.

# Thomas Wang

+852-2978-1697

thomas.wang@gs.com

GS (Asia) L.L.C.

# Simone Chen

+852-2978-0619

simone.chen@gs.com

GS (Asia) L.L.C.

Exhibit 1: China Insurance valuation comp 

<table><tr><td rowspan="2">As of 05-Jun-2026</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Share price</td><td rowspan="2">Target Price</td><td rowspan="2">Potential upside /downside%</td><td colspan="3">P/B</td><td colspan="3">P/E</td><td>Div. yield</td><td>ROE</td></tr><tr><td>2025</td><td>2026E</td><td>2027E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2026E</td><td>26/27E</td></tr><tr><td>China insurers - H share</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>China Life Insurance Co. (H)</td><td>2628.HK</td><td>Neutral</td><td>28.00</td><td>28.5</td><td>2%</td><td>1.2</td><td>1.1</td><td>1.0</td><td>4.7</td><td>8.9</td><td>8.0</td><td>3.5%</td><td>13%</td></tr><tr><td>Ping An Insurance Group (H)</td><td>2318.HK</td><td>Buy</td><td>56.90</td><td>75.0</td><td>32%</td><td>0.9</td><td>0.9</td><td>0.8</td><td>6.8</td><td>7.3</td><td>6.5</td><td>5.3%</td><td>12%</td></tr><tr><td>China Pacific Insurance (H)</td><td>2601.HK</td><td>Buy</td><td>31.10</td><td>38.0</td><td>22%</td><td>0.9</td><td>0.8</td><td>0.8</td><td>5.1</td><td>6.5</td><td>6.3</td><td>4.1%</td><td>13%</td></tr><tr><td>New China Life Insurance (H)</td><td>1336.HK</td><td>Sell</td><td>47.38</td><td>37.0</td><td>-22%</td><td>1.2</td><td>1.1</td><td>1.1</td><td>3.7</td><td>7.0</td><td>7.7</td><td>4.3%</td><td>15%</td></tr><tr><td>China Taiping Insurance Holdings</td><td>0966.HK</td><td>Neutral</td><td>19.31</td><td>21.0</td><td>9%</td><td>0.7</td><td>0.7</td><td>0.6</td><td>2.7</td><td>5.4</td><td>5.2</td><td>3.8%</td><td>13%</td></tr><tr><td>PICC Group (H)</td><td>1339.HK</td><td>Neutral</td><td>5.08</td><td>6.7</td><td>32%</td><td>0.7</td><td>0.6</td><td>0.6</td><td>4.5</td><td>6.1</td><td>5.5</td><td>5.0%</td><td>11%</td></tr><tr><td>PICC P&amp;C</td><td>2328.HK</td><td>Buy</td><td>14.27</td><td>19.6</td><td>37%</td><td>1.0</td><td>1.0</td><td>0.9</td><td>7.2</td><td>8.3</td><td>7.6</td><td>5.4%</td><td>12%</td></tr><tr><td>China insurers - A share</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>China Life Insurance Co. (A)</td><td>601628.SS</td><td>Neutral</td><td>32.82</td><td>42.0</td><td>28%</td><td>1.6</td><td>1.4</td><td>1.3</td><td>6.0</td><td>11.4</td><td>10.2</td><td>2.7%</td><td>13%</td></tr><tr><td>Ping An Insurance Group (A)</td><td>601318.SS</td><td>Buy</td><td>53.48</td><td>77.0</td><td>44%</td><td>1.0</td><td>0.9</td><td>0.8</td><td>7.0</td><td>7.5</td><td>6.7</td><td>5.2%</td><td>12%</td></tr><tr><td>China Pacific Insurance (A)</td><td>601601.SS</td><td>Neutral</td><td>31.05</td><td>39.0</td><td>26%</td><td>1.0</td><td>0.9</td><td>0.8</td><td>5.6</td><td>7.1</td><td>6.9</td><td>3.8%</td><td>13%</td></tr><tr><td>New China Life Insurance (A)</td><td>601336.SS</td><td>Sell</td><td>56.35</td><td>49.0</td><td>-13%</td><td>1.6</td><td>1.5</td><td>1.4</td><td>4.8</td><td>9.1</td><td>10.0</td><td>3.3%</td><td>15%</td></tr><tr><td>PICC Group (A)</td><td>601319.SS</td><td>Sell</td><td>6.57</td><td>6.1</td><td>-7%</td><td>0.9</td><td>0.9</td><td>0.8</td><td>6.3</td><td>8.5</td><td>7.8</td><td>3.5%</td><td>11%</td></tr></table>

Prices are as of Jun 5. Target prices are 12-month.   
Source: Thomson Reuters, GS Global Investment Research

# Sector takeaways

1) Investment strategy: Lifers generally hold a neutral view on the interest rate outlook, while focusing on asset and liability duration and cash flow matching. Long-term government bonds remain an important instrument to anchor asset duration. However, given that the long-term bond yield remains depressed (vs. historical levels), the focus is more on the equity investment side, especially on high-dividend yield stocks that can be held over the long term, thereby providing a bond-like yield and duration.

In the near-term, strong equity market performance since the end of March has driven a rebound in portfolio returns for all insurers. But insurers generally do not expect a material uplift in equity asset allocation (vs. the current level). Within equity investment, despite the rally in AI-related stocks, insurers are targeting a more balanced allocation between growth and value stocks. Dividend stocks remain a focus, as evident in the increase in the mix of OCI equity investment (vs. FVTPL). The target dividend yield is generally $4\%$ or higher.

2) Bancassurance regulation and growth: The life insurers we met all welcomed the new regulation on bancassurance channel fees, issued by the NFRA in March, as they expect the more granular examination of channel fees to further encourage banks to cooperate with large insurers. That said, insurers do expect to see near-term disruptions, as sales incentives are reduced. Generally, insurers do not expect this to have a material impact on margins, as companies are likely to pass on most of the savings to policyholders.

3) Agency development: Lifers generally expect stable agent headcount over the next 2-3 years, and the focus is mostly on (high-quality) productive agents. There are targeted recruitment and training processes in place, while resource support is also tilted towards the high-quality agency team. Despite the surge in bancassurance sales, most lifers believe agents are better positioned to serve upper affluent and HNW customers.

4) Auto insurance underwriting results outlook: Excluding the potential impact from natural catastrophes, insurers generally see room for improvement in underwriting results, driven by: 1) better risk underwriting and more pricing flexibility, 2) higher

penetration and usage of ADAS features, 3) improvements in the repair process, and 4) the potential re-calibration of the risk premium. While premium growth in 2026 could be affected by a yoy decline in new car sales, insurers generally expect premium growth to recover to low-to-mid single digits in the medium term.

5) Update to the C-ROSS regime: The Phase III update for the C-ROSS regime is still under discussion, as the regulator has yet to decide on the various risk parameters. Companies expect that implementation is likely in 2H26 or 2027. For the large insurers, companies noted that current solvency ratios are well above the regulatory minimum.

# Company meeting takeaways

# Ping An

- Ping An reiterated its multi-channel distribution strategy, including agency, bancassurance, community finance, and others. In the bancassurance channel, Ping An is working with fewer than 30k bank branches, just over $10\%$ of more than 220k bank branches in China. Ping An expects to increase branch penetration, and noted that in the last 2 years, it could add as many as 1,000 branches in a single month, although the pace of growth is likely to be slower going forward.   
- On equity investment, Ping An reiterated a balanced strategy, with a focus on using equity as an important through-cycle instrument, providing bond-like duration and yield. On dividend stocks, the company has a diversified portfolio, not just banks. The target yield is above $4\%$ , but the company noted that the hurdle rate could be reduced if the cost of liability continues to decline.   
On asset quality, Ping An continues to expect the asset management segment to provide a positive profit contribution in 2026. The company sees limited property-related impairment pressure in 2026, thanks to provisions already taken and improved market sentiment in Tier 1 and Tier 2 cities. Within the asset management segment, Ping An highlighted that the securities business achieved a high ROE in 1Q26, well above the industry average.

# CPIC

■ VONB growth and margin outlook: CPIC aims to achieve a balanced value contribution between the agency and bancassurance channels. The agency VONB margin is close to 30%, largely driven by long premium term savings products. The bancassurance margin is around 15%, and the company sees potential upside by reducing the mix of single premium policies. Participating products are an important growth driver in both channels, and CPIC sees potential for the market to evolve toward HK par products, with a low guaranteed return and diversified investment allocation.   
On P&C, CPIC sees potential for a further reduction in the expense ratio, thanks to tight regulation for both auto and non-auto insurance. In the NEV segment, there is room for the COR to decline as autonomous driving features improve, and the repair network and process develop. On credit guarantee insurance, CPIC sees positive

development in 2026, after a business adjustment starting from early 2025.

# China Taiping

Bancassurance contribution: Taiping noted that banks prefer 3- to 5-year products and struggle to sell protection products, so margin upside is limited. But there is significant volume growth potential, given that moderate deposit migration from banks can be a significant growth driver for insurers. For Taiping, bancassurance VONB contribution was c.35% in 2025, but management sees potential for this to gradually increase toward 50%. Taiping noted that the channel is dominated by the top 7 largest life insurers (including Taiping Life), following the regulatory clampdown on channel expenses.   
Investments: Taiping Life is cautiously optimistic on equity market performance, and holds a neutral view on rates. The focus is on duration and cash flow matching, to ensure the investment return covers the cost of liability. The company would also seek to enhance the yield on the fixed income portfolio through trading gains.

# ZhongAn

Online health insurance: ZhongAn (ZA) noted that health insurance in mainland China has significant development potential, while online penetration within health insurance is also low. ZA is the largest online health insurance distributor and expects to maintain strong growth momentum as the market develops.

# China Life

China Life expects VONB growth momentum to normalize in the coming quarters, after an exceptional 1Q26 (+75% yoy). The base effects in 2Q and 3Q are higher, and China Life also noted that the new bancassurance channel expense regulation could disrupt near-term sales momentum. Nonetheless, China Life is confident of double-digit VONB growth for FY26 and sees margin expansion, driven by 2025 repricing actions and a greater focus on long-term, regular premium policy sales.   
Equities investment will continue to increase as new premiums come in, but China Life sees relatively stable overall equity investment allocation. Allocation within the portfolio is diversified, tracking broad market indices, despite strong performance in the AI supply chain. China Life noted that the mix of OCI equity investment has increased, reaching c.30% of the equity portfolio, broadly in line with the industry average.

# NCI

Both agency and bancassurance sales and VONB are tracking well ahead of FY26 targets. Starting from 2Q26, NCI is focusing on health insurance and long-term products. Detailed regulation on the participating critical illness (CI) product has not been launched, so sales are mainly of the traditional CI product in the agency channel. The bancassurance channel is still mainly a savings-product channel.

On investment, total equity investment allocation was $22\%$ in 2025, and declined slightly in 1Q26, due to market movement. In the medium term, NCI does not have a target level, but does not expect this to increase to the 25-30% range. NCI sees opportunities in H-shares now, especially when considering dividend yield and cash flow.

On dividend payout, the $25\%$ payout ratio in 2025 was sufficient to drive DPS growth, even off a high base in 2024. There is no decision yet on the FY26 dividend policy, but the company will take absolute DPS into consideration.

# PICC P&C

Equity investment is approaching 30% of the portfolio, including stakes in Huaxia Bank, Industrial Bank, PICC Life, and PICC Health. PICC P&C sees limited room for a further increase in the equity asset mix, as 30% is the cap based on its current comprehensive solvency ratio. The target investment return is 3-4% in 2026.

PICC P&C attributed the industry-wide decline in auto insurance premiums in 1Q26 to the decline in new vehicle sales and the usual pricing factor changes. Management expects auto sales to recover gradually, driving improvements in auto insurance premium growth in the coming quarters.

In terms of underwriting results, PICC P&C attributes its better COR to a combination of: 1) better risk pricing, 2) internal expense management, 3) a close relationship with OEMs, and 4) expertise in claims management. As the NEV market gradually matures, PICC P&C expects the claims ratio to improve broadly, and believes its competitive advantages can enable the company to continue delivering above-peer underwriting results.

# Price Target Risks and Methodology - China Life Insurance Co.

We rate China Life H/A at Neutral/Neutral. Our 12-month, ROA-based target prices are HK\$28.5/Rmb42.0, implying 1.0X/1.7X FY27E P/B.

Downside risks: Further weakness in the investment market, which could reduce the solvency ratio and limit its ability to raise dividends; a further decline in the 10-year government bond yield to below $2\%$ ; weak insurance sales growth in lower-tier cities, where China Life has a more dominant market share; below-peer agent productivity gains.

Upside risks: Strong A-share performance given China Life's leverage to A-share returns; sustained double-digit NBV growth; better-than-expected shareholders' return plans; an increase in long-term bond yield.

# Price Target Risks and Methodology - Ping An Insurance Group

We are Buy rated on Ping An's A and H shares. Our 12-month SOTP-based target prices are HK\$75.0/Rmb77.0, implying 1.1X/1.3X FY27E P/Bs. We value 1) Ping An Life at 1.9X/2.4X FY27E P/B, based on our ROA projection, 2) Ping An P&C at 1.0X P/B, based on FY27E ROE of 12%; and 3) Ping An Bank at 2.125X target P/PPOP (covered by Shuo Yang).

Downside risks: A further decline in operating profit and/or CSM (contractual service margin) would put downward pressure on dividend growth; further deterioration in sales mix, leading to greater sensitivity of future profit to interest rate and investment returns; further investment asset losses/impairment in non-insurance businesses, such as banking and asset management businesses.

# Price Target Risks and Methodology - China Pacific Insurance

We are Buy/Neutral rated on CPIC H/A. Our 12-month, SOTP-based target prices are HK\$38.0/Rmb39.0, implying 0.9X/1.1X FY27E P/B. We value 1) CPIC Life at 1.2X/1.5X FY27E P/B, based on our ROA projection; and 2) CPIC P&C at 1.2X/1.2X P/B, based on FY27E ROE of 13.2%.

Upside risks: Faster-than-expected strong NBV growth, driven by strong new policy sales, further margin expansion and/or improving product profitability; Better-than-expected P&C underwriting results, allowing for more capital upstream to the group; More aggressive near-term dividend policy, on the back of strong profit growth; A meaningful recovery in long-term bond yields, leading to improving investment returns and long-term product profitability.

Downside risks: Inability to grow core agent headcount, leading to average or below-average NBV growth vs. leading peers; Increase in P&C underwriting losses as a result of increasing competition from medium-sized competitors; Lower dividend payout ratio as a result of higher savings product mix and capital consumption at CPIC Life; Further decline in long-term government bond yield.

# Price Target Risks and Methodology - New China Life Insurance

We are Sell rated on NCI H/A. Our 12-month, ROA-based target prices are HK\$37.0/Rmb49.0, implying 0.8X/1.2X FY27E P/B.

Upside risks: Rally in the A-share market given NCI's greater leverage to investment results; cost discipline to improve long-term ROE and shareholder returns; sustained NBV growth, driven by improvements in efficiency gains; increasing asset allocation to OCI debt to mitigate negative impacts from bond yield declines; a more aggressive dividend policy than expected going forward.

# Price Target Risks and Methodology - China Taiping Insurance Holdings

We are Neutral rated on China Taiping. Our 12-month, SOTP-based target price is HK\$21.0, implying 0.6X FY27E P/B. We value 1) Taiping Life at 0.7X FY27E P/B, based on our ROA projection; and 2) Taiping P&C and Taiping Re at 0.5X/0.4X P/B, based on FY27E ROE of 7.3%/6.8%.

Upside risks: Further improvement in life core solvency capital position and increase in capital upstream to the group, which could allow for higher dividend payout; Reduced capital consumption in the HK life insurance operation; Improvements in operating results in non-insurance segments; Better-than-expected investment results and normalized tax expenses.

Downside risks: Weaker-than-expected investment results dragging profit growth; Inability to maintain new policy sales growth, leading to a continued decline in CSM balance and lower-than-expected NBV; Lower dividend payout ratio, reflecting further solvency constraints and profit growth pressure from both life and non-life insurance segments.

# Price Target Risks and Methodology - PICC Property and Casualty Co.

We are Buy rated on PICC

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
