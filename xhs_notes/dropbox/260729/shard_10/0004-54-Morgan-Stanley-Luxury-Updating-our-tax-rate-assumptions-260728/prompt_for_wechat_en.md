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
Luxury | Europe

# Updating our tax rate assumptions

## Key Takeaways

We believe the market may be underestimating the likelihood of the French tax surcharge being cemented amid the political risk and fiscal challenges in France

We now incorporate the tax surcharge for LVMH and Hermès into our outer years (our effective tax rate assumptions are +300-400bps higher than VA css for 2027-2029)

Our France Economics teams have published this morning A Comprehensive Framework Ahead of French Elections, where they note that France faces a challenging political calendar with the budget season (autumn 2026), the presidential election (18 April and 2 May 2027) and, in their baseline scenario, snap parliamentary elections around mid-June 2027. They believe these events are likely to keep policy uncertainty elevated well into the middle of next year. We think there is a risk for the French corporate tax surcharge to be extended into 2027 and beyond.

LVMH, Hermès, Kering and Richemont are exposed to any changes to corporate tax rates for large companies in France. While their sales exposure to France is limited (<10% for all), taxation is based on where the economic value creation is produced – thus skewed to where goods production takes place (Hermès discloses that 74% of its products are manufactured in France, and around \~50% for LVMH, \~35% for Richemont and \~15% for Kering, on our estimates).

As a reminder, in 2025 the French government implemented a corporate income tax surcharge of 20% (that is, tax rate going to 30% from 25%) for companies with revenues of €1-3bn in France (this includes Kering), and a surcharge of 41% (tax rate going to 35.25% from 25%) for those with revenues above €3bn in France (includes LVMH, Hermès and Richemont; note we include inter-company sales when estimating total sales generated in France).

We believe the political and fiscal challenges France faces may cement the tax surcharge. We adjusted our tax rate for LVMH yesterday evening (post LVMH results - see Off the call / updating estimates (27 Jul 2026)) and adjust the tax rate for Hermès. We now model the same effective tax rate as 2025 (when the recent corporate tax surcharge was implemented) for the outer years in our model for both companies.

Overall, we believe the market may be underestimating the EPS impact to LVMH and Hermès (\~6% EPS downside) from a sustained tax surcharge. As can be seen in Exhibit 1 below, current Visible Alpha consensus does not incorporate the French

<table><tr><td colspan="3">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="3">Natasha Bonnet</td></tr><tr><td colspan="3">Equity Analyst</td></tr><tr><td>Natasha.Bonnet@morganstanley.com</td><td></td><td>+44 20 7677-5723</td></tr><tr><td colspan="3">Edouard Aubin</td></tr><tr><td colspan="3">Equity Analyst</td></tr><tr><td>Edouard.Aubin@morganstanley.com</td><td></td><td>+44 20 7425-3160</td></tr><tr><td colspan="3">Grace Smalley, CFA</td></tr><tr><td colspan="3">Equity Analyst</td></tr><tr><td>Grace.Smalley@morganstanley.com</td><td></td><td>+44 20 7425-9629</td></tr><tr><td colspan="3">Cedric Norest</td></tr><tr><td colspan="3">Research Associate</td></tr><tr><td>Cedric.Norest@morganstanley.com</td><td></td><td>+44 20 7425-1462</td></tr><tr><td colspan="3">BRANDS</td></tr><tr><td colspan="3">Europe</td></tr><tr><td colspan="2">Industry View</td><td>In-Line</td></tr><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Hermes International S.C.A.(HRMS.PA)Price Target</td><td>From€1,930.00</td><td>To€1,850.00</td></tr><tr><td>2027e ModelWare EPS (€)</td><td>51.35</td><td>49.56</td></tr><tr><td>2028e ModelWare EPS (€)</td><td>57.10</td><td>55.12</td></tr><tr><td>Richemont SA (CFR.S)Price Target</td><td>FromSFr 225.00</td><td>ToSFr 220.00</td></tr><tr><td>2027e ModelWare EPS (€)</td><td>7.43</td><td>7.26</td></tr><tr><td>2028e ModelWare EPS (€)</td><td>8.61</td><td>8.41</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

tax surcharge post 2026 for LVMH nor Hermès. Should the corporate tax surcharge be cemented for longer (as is now our base case), there is \~5-6% EPS downside to consensus on LVMH and Hermès from the tax rate change alone.

\- We note that LVMH paid €5.5bn in taxes in 2025, of which roughly half in France, according to the company. We estimate the French tax surcharge amounted to close to €700m in that year. We adjusted our tax rate for LVMH yesterday evening (post LVMH results - see here); the impact to our EPS from just the change in our tax rate assumptions was -6.2% in 2027-2029.

\- The CFO of Hermès (whose tax bill was €2.3bn in 2025, of which around half paid in France) observed that the tax surcharge in 2025 amounted to \~ €330m, saying that it was "equivalent to a 5% increase [in the company's tax rate] in 2025" and that "we hope that it just happens for a couple of years, but maybe this exceptional tax will be a feature in years to come". We adjust our tax rate for Hermès, now modeling a tax rate of 33.4% (in-line with 2025) going forward. Our 2027-29 EPS come down by 3.5%. Our price target is now €1,850 (vs. €1,930 previously).

\- At Richemont, while we estimate \~35% of its production takes places in France, Cartier's headquarters are based in Geneva (not Paris), so we assume the majority of its profits are generated in Switzerland (under international tax principles, profits are allocated according to where strategic decision-making, brand stewardship, pricing architecture and intellectual property oversight are located). Therefore, we assume that only \~5% of its profits are exposed to French taxation and thus the surcharge impact was not meaningful in the last financial year. We nonetheless take this opportunity to refresh our estimates regarding Richemont's tax rate; we now model the tax rate in line with its FY26 (year to March 2026) effective rate of 20.4% (note that the dip in tax rate in FY25, to 16.5%, was due to non-cash accounting factors). Our FY27-FY29 EPS come down by 2.3%. Our price target is now CHF 220 (vs. CHF 225 previously).

\- Kering manufactures about \~15% of its products in France, we estimate (with most of its brands manufactured in Italy), so we estimate its revenue in France (including inter-company sales) is less than €3bn. On that basis, we presume Kering would fall into the lower tax surcharge bracket. As a result of both these factors, the tax surcharge did not have a meaningful impact in 2025.

Exhibit 1: Effective tax rate for LVMH, Hermès and Richemont

<table><tr><td>Tax rate</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td></tr><tr><td>LVMH</td><td>30.7%</td><td>29.6%</td><td>31.8%</td><td>30.8%</td><td>27.1%</td><td>33.0%</td><td>32.6%</td><td>29.2%</td><td>26.3%</td><td>27.4%</td><td>32.7%</td><td>26.2%</td><td>26.7%</td><td>26.2%</td><td>28.5%</td><td>32.8%</td><td></td><td></td><td></td><td></td></tr><tr><td>MSe</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>32.8%</td><td>32.8%</td><td>32.8%</td><td>32.8%</td></tr><tr><td>VA css</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>32.1%</td><td>29.4%</td><td>29.0%</td><td>28.9%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+74 bps</td><td>+344 bps</td><td>+377 bps</td><td>+385 bps</td></tr><tr><td>Hermes</td><td>33.7%</td><td>32.3%</td><td>31.7%</td><td>33.3%</td><td>33.2%</td><td>35.8%</td><td>33.7%</td><td>35.4%</td><td>32.5%</td><td>33.1%</td><td>30.9%</td><td>29.5%</td><td>28.2%</td><td>27.8%</td><td>28.7%</td><td>33.4%</td><td></td><td></td><td></td><td></td></tr><tr><td>MSe</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>33.4%</td><td>33.4%</td><td>33.4%</td><td>33.4%</td></tr><tr><td>VA css</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>33.4%</td><td>30.2%</td><td>29.4%</td><td>29.1%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+5 bps</td><td>+322 bps</td><td>+404 bps</td><td>+427 bps</td></tr><tr><td></td><td>FY-11</td><td>FY-12</td><td>FY-13</td><td>FY-14</td><td>FY-15</td><td>FY-16</td><td>FY-17</td><td>FY-18</td><td>FY-19</td><td>FY-20</td><td>FY-21</td><td>FY-22</td><td>FY-23</td><td>FY-24</td><td>FY-25</td><td>FY-26</td><td>FY-27</td><td>FY-28</td><td>FY-29</td><td>FY-30</td></tr><tr><td>Richemont</td><td>16.7%</td><td>14.6%</td><td>15.6%</td><td>16.5%</td><td>21.5%</td><td>17.9%</td><td>22.5%</td><td>25.5%</td><td>21.6%</td><td>22.6%</td><td>15.1%</td><td>17.2%</td><td>17.9%</td><td>18.1%</td><td>16.5%</td><td>20.4%</td><td></td><td></td><td></td><td></td></tr><tr><td>MSe</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>20.4%</td><td>20.4%</td><td>20.4%</td><td>20.4%</td></tr><tr><td>VA css</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>18.6%</td><td>18.5%</td><td>18.4%</td><td>17.9%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+178 bps</td><td>+190 bps</td><td>+199 bps</td><td>+253 bps</td></tr></table>

Source: Visible Alpha, Company data, MS estimates (e). Note: Consensus as of 27 July 2026

Risk Rewards

## Risk Reward – Hermes International S.C.A. (HRMS.PA)

We see the risk/reward profile as balanced

## PRICE TARGET €1,850.00

We use a DCF-based valuation methodology, as we think this best reflects Hermès' margin potential and cash flow generation. We assume a WACC of 6.3% and a long-term growth rate of 2.8%.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/578d69de972fee2987e1aa2bae1e93356b2fce508acb3115e4a93a3cc27465cb.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/258d7e1b3622550b9eba620c2ee208e3091707353afcbb7a0bc142644594273f.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

## EQUAL-WEIGHT THESIS

We believe that Hermès' shares are appropriately valued by the market, with top-line estimates embedding high-single-digit growth for the next couple of years.

![](images/dac4c6908f71db44ea589a100bf320823320019c8c9dd8cd34774e7a5ac407af.jpg)  
Source: Refinitiv, MS

## Risk Reward Themes

Pricing Power: Positive
Secular Growth: Positive
View descriptions of Risk Rewards Themes here

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 27 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## BULL CASE

€2,450.00

## Faster increase in the share of leather goods

We model Hermès increasing its operating margin from 40% in 2025 to \~44% in 2034e (and 15% average top-line growth), mostly driven by a higher share of leather goods (from 50% in 2020 to 60% in 2024, more or less in line with Saint Laurent today at 69%) in the sales mix and acceleration in growth of the non-leather goods category.

## BASE CASE

## €1,850.00 BEAR CASE

## Steady HSD/LDD growth

We forecast Hermès' EBIT margin to reach 43% by 2033. Margin expansion is a function of higher sales densities (annual selling space growth remains limited), higher share of online sales and higher-margin categories increasing in the mix.

€1,220.00

## Margin reversion and slower growth

Assumes that Hermès' margin reverts within five years, reaching 38% by 2030 vs. 41% in 2022 (and top-line growth is +6% on average). This is mostly driven by lower pricing power on its iconic products as the brand's desirability declines and overall demand for luxury goods from Chinese nationals softens.

<table><tr><td>5/5 MOST</td><td>3 Month Horizon</td></tr></table>

- Spending of Chinese nationals on luxury goods

## Risk Reward – Hermes International S.C.A. (HRMS.PA)

## KEY EARNINGS INPUTS

<table><tr><td>Drivers</td><td>Dec 2025</td><td>Dec 2026e</td><td>Dec 2027e</td><td>Dec 2028e</td></tr><tr><td>Group % Change - constant currency (%)</td><td>8.9</td><td>7.1</td><td>9.1</td><td>10.7</td></tr><tr><td>Europe % Change - constant currency (%)</td><td>10.3</td><td>6.5</td><td>9.7</td><td>11.2</td></tr><tr><td>Americas % Change - constant currency (%)</td><td>12.4</td><td>14.0</td><td>10.0</td><td>10.0</td></tr><tr><td>APAC % Change - constant currency (%)</td><td>6.5</td><td>5.5</td><td>8.3</td><td>10.4</td></tr></table>

## INVESTMENT DRIVERS

\- Brand desirability

• Leather goods supply

## GLOBAL REVENUE EXPOSURE

![](images/2ca7ff36f55e287db87ee88d21cb4780e179673ffd62e5027d89b7bdffa10075.jpg)

![](images/3bf0616d565fbf986a953f9d96a7f216b81a45cbcef2d1f9cca6b4f23c36ac16.jpg)  
Source: MS Estimate View explanation of regional hierarchies here  
- Operating margin lifted by a higher share of most profitable categories in the sales mix

## MS ALPHA MODELS

Source: Refinitiv, FactSet, MS; 1 is the highest favored Quintile and 5 is the least favored Quintile

## RISKS TO PT/RATING

## RISKS TO UPSIDE

## RISKS TO DOWNSIDE

\- Discount rate: two-thirds of Hermes' equity value is in its TV

\- FX: majority of Hermès' products are manufactured in the euro zone

\- Overdependence on a few iconic products? We estimate Birkin & Kelly bags account for \~25% & 33% of sales & profits, respectively

\- Middle-income consumers become the main growth driver

## OWNERSHIP POSITIONING

<table><tr><td>Inst. Owners, % Active</td><td>65.7%</td><td colspan="4"></td></tr><tr><td>HF Sector Long/Short Ratio</td><td>1.6x</td><td colspan="4"></td></tr><tr><td>HF Sector Net Exposure</td><td>7.6%</td><td colspan="4"></td></tr></table>

Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

MS ESTIMATES VS. CONSENSUS  
![](images/db3574a7d8bc2ab49bfda68e3d9ba39569af8aea490c10ef0dfaaa2880895319.jpg)  
◆ Mean ◆ MS Estimates
Source: Refinitiv, MS

Source: Refinitiv, MS

![](images/44201fd65cc4b0de0fe3c75781e7b899cb55e4ccbfb753cdcbf86a1b37fb8c32.jpg)

## Risk Reward – Richemont SA (CFR.S)

Risk/reward profile is skewed to the upside

## PRICE TARGET SFr 220.00

We use a DCF-based valuation methodology, which we think best reflects the company's margin potential and cash flow. We assume a WACC of 8.4% and long-term growth rate of 2.5%.

Consensus Price Target Distribution

Source: Refinitiv, MS

SFr 132.14

![](images/c0d60580ec26fb5d3c14786f82169550dd8575aa963b12d2519b209ed424bad0.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/0929d1915803adbf73ccf11bbea60df6b353c86af36cc0641907e55f9d70e767.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

## OVERWEIGHT THESIS

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 27 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

Richemont is a fundamentally stronger organisation today than five or 10 years ago, mostly as a function of the fact that its two largest brands (Cartier and Van Cleef) are performing better and account for a greater share of the Group's sales and profits.

## Risk Reward Themes

Pricing Power: Positive
Self-help: Positive
View descriptions of Risk Rewards Themes here

## BULL CASE

SFr 264.00

## BASE CASE

## Sustained top-line and EBIT growth

Assumes that Jewellery Maisons organic sales grow at a double-digit CAGR in the next five years. EBIT margin of Jewellery Maisons division reaches 40% in FY28.

## SFr 220.00 BEAR CASE

## Top-line growth, operating leverage

We forecast Jewellery Maisons organic sales to grow at c.+9% CAGR to €20.4bn in FY28. We expect further operating leverage as JM's margins should broadly reach \~35% in FY28.

SFr 143.00

## Flattish Jewellery Maison sales FY24-28e

Assumes that demand from the West contracts over the next 12 months, while China recovery is more sluggish than anticipated. Sales at both Jewellery Maisons and Specialist Watchmaker divisions turn negative, leading to further margin contraction. We model flattish Jewellery Maisons sales across FY24-28. Jewellery Maisons margins contract by -150 bps on average per year across FY24-28 to below 30%.

## Risk Reward – Richemont SA (CFR.S)

## KEY EARNINGS INPUTS

[中间内容因长度限制已省略]

 Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Brands

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/27/2026)</td></tr><tr><td colspan="3">Edouard Aubin</td></tr><tr><td>Adidas (ADSGn.DE)</td><td>O (04/15/2024)</td><td>€179.65</td></tr><tr><td>Birkenstock Holding plc (BIRK.N)</td><td>E (11/06/2023)</td><td>US$41.55</td></tr><tr><td>Ferrari NV (RACE.N)</td><td>O (06/15/2026)</td><td>US$380.01</td></tr><tr><td>Ferrari NV (RACE.MI)</td><td>O (06/15/2026)</td><td>€331.80</td></tr><tr><td>Hermes International S.C.A. (HRMS.PA)</td><td>E (10/06/2025)</td><td>€1,659.00</td></tr><tr><td>Kering (PRTP.PA)</td><td>E (04/10/2026)</td><td>€242.85</td></tr><tr><td>LVMH Moet Hennessy Louis Vuitton SA (LVMH.PA)</td><td>E (01/19/2026)</td><td>€466.80</td></tr><tr><td>Richemont SA (CFR.S)</td><td>O (02/05/2025)</td><td>SFr 193.95</td></tr><tr><td colspan="3">Grace Smalley, CFA</td></tr><tr><td>Burberry (BRBY.L)</td><td>O (05/18/2026)</td><td>1,086p</td></tr><tr><td>EssilorLuxottica SA (ESLX.PA)</td><td>O (07/05/2023)</td><td>€165.40</td></tr><tr><td>Hugo Boss AG (BOSSn.DE)</td><td>E (07/09/2024)</td><td>€37.92</td></tr><tr><td>Luxexperience BV (LUXE.N)</td><td>E (09/15/2023)</td><td>US$8.26</td></tr><tr><td>Pandora A/S (PNDORA.CO)</td><td>E (01/16/2023)</td><td>DKr 780.20</td></tr><tr><td>PUMA SE (PUMG.DE)</td><td>++</td><td>€28.49</td></tr><tr><td colspan="3">Natasha Bonnet</td></tr><tr><td>Avolta AG (AVOL.S)</td><td>E (04/24/2026)</td><td>SFr 48.14</td></tr><tr><td>Brunello Cucinelli (BCU.MI)</td><td>O (01/27/2026)</td><td>€83.56</td></tr><tr><td>Ermenegildo Zegna (ZGN.N)</td><td>E (02/12/2026)</td><td>US$14.89</td></tr><tr><td>Moncler SpA (MONC.MI)</td><td>E (06/22/2026)</td><td>€48.25</td></tr><tr><td>Prada SpA (1913.HK)</td><td>E (06/29/2026)</td><td>HK$38.90</td></tr><tr><td>Salvatore Ferragamo Spa (SFER.MI)</td><td>U (02/12/2026)</td><td>€9.93</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

## © 2026 MS
"""
