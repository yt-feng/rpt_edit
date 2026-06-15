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
## China Credit Observation: three findings of K-shaped economy

China's May TSF data unveiled a deepened K-shape economy. Liquidity improved on the surface, yet largely reflect precautionary cash positioning. New loans relied on bill financing, whereas HH credit demand remained subdued. We highlight three findings from recent macro data, and favor three opportunities in China financials: a barbell positioning in China banks, BOC (H) and BONB (A), and HKEx as long-term beneficiary of expanding formal capital connect schemes.

Headline TSF buoyed by govt credit: May-26 new TSF printed at Rmb2,029bn, 19% above consensus, driven by Rmb1.2tn issuance in government bonds, which contributes to 60% of new monthly TSF. Total TSF balance printed at Rmb458,810bn, +7.7% YoY. Corporate bond financing improved 14.6% YoY, partially offsetting the weakness on corporate LT loans. Shadow banking components further contracted.

M1 improved to 5.5%, but likely low quality: M1 and M2 growth printed at 5.5% (0.5ppt above consensus) and 8.6% in May respectively. We read this set of data into two perspectives 1) a narrowing M2-M1 gap indicates further term deposit activation, which can potentially lead to further consumptions/investments; 2) yet M1 strength is likely driven by precautionary liquidity rather than genuine corporate cash deployment, given a weaker PMI new order print (-0.7ppt MoM to 49.9), thus is low quality in our view.

Real economy credit demand is yet to recover: New Rmb loans printed at Rmb520bn in May, leading to a 5.5% system level loan balance growth to Rmb281.02tn. Structure was not improving, as 107% of new Rmb loans was boosted by discounted bills, while household ST/LT loans stayed in contraction zones. Overall China's credit impulse weakened on MoM basis.

Three findings about K-shaped economy: First, we track the gap between RatingDog PMI and official NBS PMI, and a widening spread in May suggests service-led, export-driven business activities are picking up faster driven by AI super-cycle, whereas overall manufacturing/infra activities landed on a softer patch. Second, export and domestic consumption like come in a divergent pair. China's custom export +19.4% YoY in May-26, beat consensus estimate of 15% YoY, marking the strongest since Feb-26, supported by continued strong demand for renewable and AI-related goods. On the other hand, Core CPI dipped 0.1% MoM to 1.1%, with softness in both services and core goods. Third, PPI continued to edge up at +3.9% YoY (vs +2.8% in Apr-26/3.8% consensus), the inflationary pressure from Middle East shock eased a bit evidenced from sequentially lower PMI raw material price, but the constant gap between purchase and ex-factory price suggests the limited pass-through, as such downstream sectors are still early to a reflationary scenario.

Three ideas in China Financials: Amid a K-shaped recovery in real economy, soft domestic demand, and a continued household deleveraging trend, we recommend barbell strategy in China banks - BOC (H) and Bank of Ningbo (A) are our top picks. We believe recent State Council's outbound investment regulations focus more on real investments, and CSRC's agenda is to clean up cross-border stock trading happening onshore with the end goal of facilitating capital flows into official channels, such as QDII, Southbound Connect, and Wealth Management Connect. As such, HKEx will be a long-term beneficiary of expanding formal capital connect channels.

Figure 1 - TSF quick read

<table><tr><td>(Rmbbn)</td><td>May-25</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>New total social financing (TSF)</td><td>2,290</td><td>5,226</td><td>625</td><td>2,029</td></tr><tr><td>- Loans (Rmb &amp; FX)</td><td>606</td><td>3,195</td><td>(382)</td><td>513</td></tr><tr><td>- Shadow banking *</td><td>(116)</td><td>80</td><td>(570)</td><td>(72)</td></tr><tr><td>- Corporate bonds</td><td>150</td><td>395</td><td>452</td><td>172</td></tr><tr><td>- Government bonds (central &amp; local)</td><td>1,459</td><td>1,162</td><td>904</td><td>1,222</td></tr><tr><td>- Others (equity, ABS, write-off, etc.)</td><td>192</td><td>395</td><td>220</td><td>195</td></tr><tr><td>TSF balance</td><td>426,160</td><td>456,460</td><td>456,890</td><td>458,810</td></tr><tr><td>TSF balance growth</td><td>8.7%</td><td>7.9%</td><td>7.8%</td><td>7.7%</td></tr><tr><td colspan="5">* Shadow banking include entrusted loans, trust loans and undiscounted bills</td></tr><tr><td>New Rmb loans</td><td>620</td><td>2,990</td><td>-10</td><td>520</td></tr><tr><td>- Household short-term loans</td><td>(21)</td><td>196</td><td>(446)</td><td>(84)</td></tr><tr><td>- Household long-term loans</td><td>75</td><td>295</td><td>(341)</td><td>(57)</td></tr><tr><td>- Corporate short-term loans</td><td>110</td><td>1,480</td><td>(460)</td><td>100</td></tr><tr><td>- Corporate long-term loans</td><td>330</td><td>1,350</td><td>(410)</td><td>(20)</td></tr><tr><td>- Discounted bills</td><td>75</td><td>(191)</td><td>1,243</td><td>557</td></tr><tr><td>- NBFi loans</td><td>59</td><td>(169)</td><td>175</td><td>(86)</td></tr><tr><td>Loan balance</td><td>266,321</td><td>280,510</td><td>280,502</td><td>281,020</td></tr><tr><td>Loan balance growth</td><td>7.1%</td><td>5.7%</td><td>5.6%</td><td>5.5%</td></tr><tr><td>New deposits</td><td>2,183</td><td>4,470</td><td>273</td><td>1,770</td></tr><tr><td>- Household deposits</td><td>470</td><td>2,440</td><td>-1,940</td><td>-110</td></tr><tr><td>- Corporate deposits</td><td>-418</td><td>2,725</td><td>-1,250</td><td>-170</td></tr><tr><td>M1 growth</td><td>2.3%</td><td>5.1%</td><td>5.0%</td><td>5.5%</td></tr><tr><td>M2 growth</td><td>7.9%</td><td>8.5%</td><td>8.6%</td><td>8.6%</td></tr></table>

Source: PBOC, Wind, CEIC, JEF

Figure 2 - Household deposit vs household debt  
![](images/4913cd230bce447eca7a7b343d677abebc9a90f4ecb00df625112f7b3774fe5e.jpg)

<details>
<summary>bar chart</summary>

| Year | Household deposit (Rmbtn) | Household debt (Rmbtn) |
|---|---|---|
| 2013 | 6 | 4 |
| 2014 | 4 | 3 |
| 2015 | 4 | 4 |
| 2016 | 6 | 5 |
| 2017 | 5 | 7 |
| 2018 | 7 | 7 |
| 2019 | 10 | 7 |
| 2020 | 11 | 8 |
| 2021 | 10 | 8 |
| 2022 | 18 | 4 |
| 2023 | 17 | 5 |
| 2024 | 14 | 3 |
| 2025 | 15 | 0 |
| 2025Q1-7 | 6 | -1 |
</details>

Source: PBOC, Wind, CEIC, JEF

Figure 3 - All new deposits breakdown by savers  
![](images/7cd052c417232eb5c2d8e4a9c2c2f971f9506016e1cf69a884319277fc3debf1.jpg)  
Source: PBOC, Wind, JEF

Figure 4 - China credit impulse  
![](images/7f4c93922384806e67898010481069e88e9995679023e0243f4095caee4e20c0.jpg)

<details>
<summary>line chart</summary>

China's credit impulse (3-m TSF change % quarterly GDP)
| Date | Value (%) |
|---|---|
| Mar-08 | 30 |
| Mar-09 | 70 |
| Sep-09 | 55 |
| Sep-10 | 40 |
| Sep-11 | 25 |
| Sep-12 | 35 |
| Sep-13 | 45 |
| Sep-14 | 30 |
| Sep-15 | 40 |
| Sep-16 | 35 |
| Sep-17 | 40 |
| Sep-18 | 30 |
| Sep-19 | 35 |
| Sep-20 | 55 |
| Sep-21 | 30 |
| Sep-22 | 25 |
| Sep-23 | 30 |
| Sep-24 | 40 |
| Sep-25 | 35 |
| Mar-26 | 40 |
</details>

Source: PBOC, Wind, JEF

Figure 5 - RatingDog PMI vs Official PMI  
![](images/b845122076973268a435c5e31bc00ceef2696ca01268b2efc18bf4e8aec71bb7.jpg)

<details>
<summary>line chart</summary>

| Date | Manufacturing | Service | RatingDog PMI | NBS PMI |
|---|---|---|---|---|
| 2024-12 | 51.5 | 51.8 | 50.0 | 50.0 |
| 2025-01 | 51.3 | 51.6 | 50.0 | 49.7 |
| 2025-02 | 51.1 | 51.4 | 50.0 | 49.4 |
| 2025-03 | 50.9 | 51.2 | 50.0 | 49.1 |
| 2025-04 | 50.7 | 51.0 | 50.0 | 48.8 |
| 2025-05 | 49.8 | 50.8 | 50.0 | 48.5 |
| 2025-06 | 50.3 | 51.1 | 50.0 | 48.7 |
| 2025-07 | 50.6 | 51.3 | 50.0 | 48.9 |
| 2025-08 | 51.0 | 51.6 | 50.0 | 49.1 |
| 2025-09 | 51.3 | 51.9 | 50.0 | 49.3 |
| 2025-10 | 51.6 | 52.2 | 50.0 | 49.5 |
| 2025-11 | 51.9 | 52.5 | 50.0 | 49.7 |
| 2025-12 | 52.2 | 52.8 | 50.0 | 49.9 |
| 2026-01 | 52.6 | 53.1 | 50.0 | 50.1 |
| 2026-02 | 53.1 | 53.4 | 54.4 | 49.8 |
| 2026-03 | 51.8 | 53.7 | 54.4 | 49.6 |
| 2026-04 | 51.6 | 53.9 | 54.4 | 49.4 |
| 2026-05 | 51.8 | 54.0 | 54.4 | 49.3 |
</details>

Source: RatingDog, S&P, NBS, JEF

Betty Li \* | Equity Analyst

+852 3767 1279 | betty.li@JEF.com

Hongyu Tian \* | Equity Associate

+852 6806 1456 | hongyu.tian@JEF.com

We would like to thank Tao Xue, employee of Evalueserve Inc., for providing research support services to our preparation of this report.

## Company Valuation/Risks

## Bank of China Limited

Our PT of HKD 6.3 is based on DDM with $7.69\%$ cost of equity. This implies a 0.67x H-share 2026E P/B and $4.0\%$ dividend yields. Long term ROE is set at $6.4\%$ , implying a long-term H-share P/B of 0.59x. A/H premium is set at $26.4\%$ , A-share TP is set at Rmb 7.4, implied a 0.84x A-share 2026E P/B. Our base case assumes an EPS of Rmb 0.76 based on $1.23\%$ NIM and $0.50\%$ CoR.

Upside risks: easing global tension; better-than-expected offshore interest rate movement; and better-than-expected HK market growth; potential upside in cross-border opportunities. Downside risks: worsening geopolitical conditions that hurt China's exports and economy, or prompt sanctions on financial institutions; further weak credit demand; and significant deterioration in asset quality.

## Bank of Ningbo Co Ltd

Our PT of Rmb 42.0 is based on DDM with $8.6\%$ cost of equity. This implies a 1.12X 2026E P/B. Our base case assumes an EPS of Rmb 4.72 based on $1.69\%$ NIM and $1.00\%$ CoR.

Upside risk: Better than expected earnings recovery; regional economy further outpaces the country; better-than-expected wealth management business development; better-than-expect retail recovery. Downside risks: significant asset quality deterioration; worsening geopolitical conditions that hurt China's exports and economy.

## Hong Kong Exchanges and Clearing Limited

We use P/E multiple to value HKEx. Upside risks: better-than-expected market turnover; better-than-expected fund flow; and better-than-expected economy. Downside risks: worse-than-expected market turnover; worse-than-expected fund flow; and worse-than-expected Chinese ADR return.

## Analyst Certification:

I, Betty Li, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Hongyu Tian, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

Registration of non-US analysts: Betty Li is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst.

Registration of non-US analysts: Hongyu Tian is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst. As is the case with all JEF employees, the analyst(s) responsible for the coverage of the financial instruments discussed in this report receives compensation based in part on the overall performance of the firm, including investment banking income. We seek to update our research as appropriate, but various regulations may prevent us from doing so. Aside from certain industry reports published on a periodic basis, the large majority of reports are published at irregular intervals as appropriate in the analyst's judgement.

## Investment Recommendation Record

## (Article 3(1)e and Article 7 of MAR)

Recommendation Published

June 12, 2026 14:28 P.M.

Recommendation Distributed

June 12, 2026 14:28 P.M.

## Company Specific Disclosures

## Explanation of JEF Ratings

Buy - Describes securities that we expect to provide a total return (price appreciation plus yield) of 15% or more within a 12-month period. Hold - Describes securities that we expect to provide a total return (price appreciation plus yield) of plus 15% or minus 10% within a 12-month period. Underperform - Describes securities that we expect to provide a total return (price appreciation plus yield) of minus 10% or less within a 12-month period. The expected total return (price appreciation plus yield) for Buy rated securities with an average security price consistently below \$10 is 20% or more within a 12-month period as these companies are typically more volatile than the overall stock market. For Hold rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is plus or minus 20% within a 12-month period. For Underperform rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is minus 20% or less within a 12-month period.

NR - The investment rating and price target have been temporarily suspended. Such suspensions are in compliance with applicable regulations and/or JEF policies.

CS - Coverage Suspended. JEF has suspended coverage of this company.

NC - Not covered. JEF does not cover this company.

Restricted - Describes issuers where, in conjunction with JEF engagement in certain transactions, company policy or applicable securities regulations prohibit certain types of communications, including investment recommendations.

Monitor - Describes securities whose company fundamentals and financials are being monitored, and for which no financial projections or opinions on the investment merits of the company are provided.

## Valuation Methodology

JEF' methodology for assigning ratings may include the following: market capitalization, maturity, growth/value, volatility and expected total return over the next 12 months. The price targets are based on several methodologies, which may include, but are not restricted to, analyses of market risk, growth rate, revenue stream, discounted cash flow (DCF), EBITDA, EPS, cash flow (CF), free cash flow (FCF), EV/EBITDA, P/E, PE/growth, P/CF, P/FCF, premium (discount)/average group EV/EBITDA, premium (discount)/average group P/E, sum of the parts, net asset value, dividend returns, and return on equity (ROE) over the next 12 months.

## JEF Franchise Picks

JEF Franchise Picks include stock selections from among the best stock ideas from our equity analysts over a 12 month period. Stock selection is based on fundamental analysis and may take into account other factors such as analyst conviction, differentiated analysis, a favorable risk/reward ratio and investment themes that JEF analysts are recommending. JEF Franchise Picks will include only Buy rated stocks and the number can vary depending on analyst recommendations for inclusion. Stocks will be added as new opportunities arise and removed when the reason for inclusion changes, the stock has met its desired return, if it is no longer rated Buy and/or if it triggers a stop loss. Stocks having 120 day volatility in the bottom quartile of S&P stocks will continue to have a $15\%$ stop loss, and the remainder will have a $20\%$ stop. Franchise Picks are not intended to represent a recommended portfolio of stocks and is not sector based, but we may note where we believe a Pick falls within an investment style such as growth or value.

## Risks which may impede the achievement of our Price Target

This report was prepared for general circulation and does not provide investment recommendations specific to individual investors. As such, the financial instruments discussed in this report may not be suitable for all investors and investors must make their own investment decisions based upon their specific investment objectives and financial situation utilizing their own financial advisors as they deem necessary. Past performance of the financial instruments recommended in this report should not be taken as an indication or guarantee of future results. The price, value of, and income from, any of the financial instruments mentioned in this report can rise as well as fall and may be affected by changes in economic, financial and political factors. If a financial instrument is denominated in a currency other than the investor's home currency, a change in exchange rates may adversely affect the price of, value of, or income derived from the financial instrument described in this report. To the extent prices are shown in non-US currency, please note that our local currency price targets are based on a currency conversion using an exchange rate as of the prior trading day (unless otherwise noted). Should there be fluctuations in the exchange rate after this date, that will affect the non-US target prices and should no longer be relied upon. In addition, investors in securities such as ADRs, whose values are affected by the currency of the underlying security, effectively assume currency risk.

## Other Companies Mentioned in This Report

• Bank of China Limited (3988 HK: HK\$5.37, BUY)  
• Bank of Ningbo Co Ltd (002142 CH: CNY32.85, BUY)  
• Hong Kong Exchanges and Clearing Limited (388 HK: HK\$374.00, BUY)

Rating and Price Target History for: Bank of Ningbo Co Ltd (002142 CH) as of 06-11-2026  
![](images/ae9d8180bb111ac4c7ea4c4614ab959dad35fd69086fab66bf578dce78cc56e4.jpg)

<details>
<summary>line chart</summary>

| Date       | Price |
| ---------- | ----- |
| 05/13/2026 | 34.00 |
</details>

Rating and Price Target History for: Hong Kong Exchanges and Clearing Limited (388 HK) as of 06-11-2026  
![](images/b52400a11e50f2c9f914c6987f85c9ed2578e0d38a0d69083709fc0db208b486.jpg)

<details>
<summary>line chart</summary>

| Date       | Price (HK$) |
| ---------- | ----------- |
| 02/23/2026 | 502.00      |
</details>

Rating and Price Target History for: Bank of China Limited (3988 HK) as of 06-11-2026  
![](images/cbba89a116e20e3d83d5861a0b3d99080916c740d2c38cf0af8c443b8d8cece9.jpg)

<details>
<sum

[中间内容因长度限制已省略]

ular investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
