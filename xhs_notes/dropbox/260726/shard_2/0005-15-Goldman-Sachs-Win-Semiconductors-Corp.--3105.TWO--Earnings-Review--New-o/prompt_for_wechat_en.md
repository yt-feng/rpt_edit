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
# Win Semiconductors Corp. (3105.TWO)

# Earnings Review: New optical product to ramp up in 2H26, higher margin but limited contribution; reiterate Sell

3105.TWO 12m Price Target: NT\$142.00 Price: NT\$341.50 Downside: 58.4%

Win Semi's 2Q26 core business (operating income) was 56/5% higher than GSe/BBG consensus, mainly due to a more favorable product mix with higher contribution from high margin infrastructure business, which led to a 1.9ppt QoQ increase in 2Q26 GPM, and came in 0.4ppt above GSe but is 1.0ppt below BBG consensus. Win Semi's OPEX further declined to NT\$743mn (vs. NT\$778mn in 1Q26). NI was 114/52% higher than GSe/BBG consensus due to the NT\$447mn recognized in non-operating income (account for 38% of total pretax income).

For 3Q26, the company expects revenue to increase by low teens QoQ, and expects optical business to deliver the strongest growth driven by the ramp up of new PD (photodiodes) products at the end of 2Q26, infrastructure should also see strong growth, while cellular and WiFi business might see flattish to slight QoQ increase. On GM, the company guides the 3Q26 level to be around low-thirties %, which is better than our prior expectation but is in line with BBG consensus of 31.3%. Management indicated 2Q26 UTR to be higher at 65% (was 60% in 1Q26), with no guidance for 3Q26, and we expect UTR to further increase to \~70%.

Win Semi continued to highlight the company's progress with its AI-related business, expecting shipments of new PD (photodiodes) products for a single client to ramp up in 2H26. For new LD (laser diodes) products, the company is currently engaged with multiple clients on several new solutions (including CW laser and EML solutions), but expects to see more contribution in 2027/28. The company mentioned that CAPEX this year will mainly focus on expanding InP and GaN capacity for the datacom optical and infrastructure business. Overall, management now expect that the AI-related business might reach double-digits of total revenue in 2027 and potentially reach a similar scale as the cellular and infrastructure business in the long term (each at $30 - 35\%$ in 2Q26).

## SELL

Chao Wang
+886(2)2730-4195 | kuan-chao.wang@gs.com
GS (Asia) L.L.C., Taipei Branch

Allen Chang
+852-2978-2930 | allen.k.chang@gs.com
GS (Asia) L.L.C.

Al Wang
+886(2)2730-4081 | al.wang@gs.com
GS (Asia) L.L.C., Taipei Branch

## Key Data

Market cap: NT\$137.7bn / \$4.3bn
Enterprise value: NT\$141.8bn / \$4.4bn
3m ADTV: NT\$12.5bn / \$396.1mn
Taiwan
Taiwan Electronic Components
M&A Rank: 3
Leases incl. in net debt & EV?: No

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (NT$ mn) New</td><td>16,638.5</td><td>21,320.0</td><td>24,016.0</td><td>25,863.5</td></tr><tr><td>Revenue (NT$ mn) Old</td><td>16,638.5</td><td>20,119.5</td><td>22,342.2</td><td>25,147.4</td></tr><tr><td>EBITDA (NT$ mn)</td><td>4,708.4</td><td>6,085.5</td><td>6,569.2</td><td>7,276.9</td></tr><tr><td>EPS (NT$) New</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>EPS (NT$) Old</td><td>4.00</td><td>5.13</td><td>6.09</td><td>7.31</td></tr><tr><td>P/E (X)</td><td>25.9</td><td>45.5</td><td>53.7</td><td>43.5</td></tr><tr><td>P/B (X)</td><td>1.1</td><td>3.4</td><td>3.3</td><td>3.2</td></tr><tr><td>Dividend yield (%)</td><td>1.9</td><td>1.4</td><td>1.2</td><td>1.5</td></tr><tr><td>CROCI (%)</td><td>8.2</td><td>9.9</td><td>9.7</td><td>10.1</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS (NT$)</td><td>2.30</td><td>2.73</td><td>1.22</td><td>1.06</td></tr></table>

GS Factor Profile

![](images/9890ed73e96f9676fc11358f0471472dbe1dfdc4ad5174bc83cec7d2e485a192.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Win Semiconductors Corp. (3105.TWO) Rating since Dec 2, 2024

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>25.9</td><td>45.5</td><td>53.7</td><td>43.5</td></tr><tr><td>P/B (X)</td><td>1.1</td><td>3.4</td><td>3.3</td><td>3.2</td></tr><tr><td>FCF yield (%)</td><td>7.4</td><td>1.5</td><td>1.7</td><td>2.3</td></tr><tr><td>EV/EBITDAR (X)</td><td>10.6</td><td>24.5</td><td>22.5</td><td>20.1</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>10.6</td><td>24.5</td><td>22.5</td><td>20.1</td></tr><tr><td>CROCI (%)</td><td>8.2</td><td>9.9</td><td>9.7</td><td>10.1</td></tr><tr><td>ROE (%)</td><td>4.3</td><td>7.6</td><td>6.2</td><td>7.5</td></tr><tr><td>Net debt/equity (%)</td><td>13.3</td><td>15.6</td><td>20.6</td><td>23.2</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>13.3</td><td>15.6</td><td>20.6</td><td>23.2</td></tr><tr><td>Interest cover (X)</td><td>1.0</td><td>4.7</td><td>5.1</td><td>5.6</td></tr><tr><td>Days inventory outst, sales</td><td>109.4</td><td>92.4</td><td>93.4</td><td>94.2</td></tr><tr><td>Receivable days</td><td>32.9</td><td>32.7</td><td>34.0</td><td>34.7</td></tr><tr><td>Days payable outstanding</td><td>39.9</td><td>42.5</td><td>42.7</td><td>43.7</td></tr><tr><td>DuPont ROE (%)</td><td>4.0</td><td>7.9</td><td>6.9</td><td>8.9</td></tr><tr><td>Turnover (X)</td><td>0.3</td><td>0.4</td><td>0.4</td><td>0.4</td></tr><tr><td>Leverage (X)</td><td>1.4</td><td>1.5</td><td>1.5</td><td>1.6</td></tr><tr><td>Gross cash invested (ex cash) (NT$)</td><td>61,343.0</td><td>63,693.2</td><td>67,123.2</td><td>70,164.4</td></tr><tr><td>Average capital employed (NT$)</td><td>48,929.8</td><td>47,177.2</td><td>46,772.6</td><td>46,370.8</td></tr><tr><td>BVPS (NT$)</td><td>98.00</td><td>100.63</td><td>102.85</td><td>105.60</td></tr></table>

Balance Sheet (NT\$ mn)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>(4.7)</td><td>28.1</td><td>12.6</td><td>7.7</td></tr><tr><td>EBITDA growth</td><td>(13.8)</td><td>29.2</td><td>7.9</td><td>10.8</td></tr><tr><td>EPS growth</td><td>120.5</td><td>88.0</td><td>(15.4)</td><td>23.7</td></tr><tr><td>DPS growth</td><td>NM</td><td>144.1</td><td>(15.4)</td><td>23.7</td></tr><tr><td>EBIT margin</td><td>4.3</td><td>13.7</td><td>13.1</td><td>13.3</td></tr><tr><td>EBITDA margin</td><td>28.3</td><td>28.5</td><td>27.4</td><td>28.1</td></tr><tr><td>Net income margin</td><td>10.2</td><td>14.9</td><td>11.2</td><td>12.9</td></tr></table>

Price Performance  
![](images/92895170fd00a6eff43adf5e86df2f6885970facf2dd79b3bba9867a878c0f6d.jpg)  
Source: FactSet. Price as of 24 Jul 2026 close.

Income Statement (NT\$ mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>16,638.5</td><td>21,320.0</td><td>24,016.0</td><td>25,863.5</td></tr><tr><td>Cost of goods sold</td><td>(12,612.4)</td><td>(15,172.2)</td><td>(16,882.8)</td><td>(17,933.7)</td></tr><tr><td>SG&amp;A</td><td>(1,711.1)</td><td>(1,807.1)</td><td>(2,098.7)</td><td>(2,172.3)</td></tr><tr><td>R&amp;D</td><td>(1,600.3)</td><td>(1,416.7)</td><td>(1,893.1)</td><td>(2,327.7)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>4,708.4</td><td>6,085.5</td><td>6,569.2</td><td>7,276.9</td></tr><tr><td>Depreciation &amp; amortization</td><td>(3,993.7)</td><td>(3,161.4)</td><td>(3,427.8)</td><td>(3,847.1)</td></tr><tr><td>EBIT</td><td>714.7</td><td>2,924.1</td><td>3,141.4</td><td>3,429.8</td></tr><tr><td>Net interest inc./(exp.)</td><td>(546.0)</td><td>(417.3)</td><td>(437.8)</td><td>(485.4)</td></tr><tr><td>Income/(loss) from associates</td><td>0.0</td><td>(149.2)</td><td>(500.0)</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>1,386.9</td><td>3,221.4</td><td>2,641.4</td><td>3,429.8</td></tr><tr><td>Provision for taxes</td><td>(297.1)</td><td>(686.4)</td><td>(566.8)</td><td>(729.6)</td></tr><tr><td>Minority interest</td><td>604.0</td><td>649.2</td><td>619.0</td><td>631.2</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>1,693.8</td><td>3,184.1</td><td>2,693.6</td><td>3,331.4</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>1,693.8</td><td>3,184.1</td><td>2,693.6</td><td>3,331.4</td></tr><tr><td>EPS (basic, pre-except) (NT$)</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>EPS (diluted, pre-except) (NT$)</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>EPS (basic, post-except) (NT$)</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>EPS (diluted, post-except) (NT$)</td><td>4.00</td><td>7.51</td><td>6.35</td><td>7.86</td></tr><tr><td>DPS (NT$)</td><td>2.00</td><td>4.88</td><td>4.13</td><td>5.11</td></tr><tr><td>Div. payout ratio (%)</td><td>50.1</td><td>65.0</td><td>65.0</td><td>65.0</td></tr></table>

<table><tr><td colspan="5">Balance Sheet (NT$ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>7,066.9</td><td>6,343.4</td><td>4,665.0</td><td>4,005.7</td></tr><tr><td>Accounts receivable</td><td>1,713.9</td><td>2,102.8</td><td>2,368.7</td><td>2,550.9</td></tr><tr><td>Inventory</td><td>4,978.5</td><td>5,819.5</td><td>6,475.6</td><td>6,878.7</td></tr><tr><td>Other current assets</td><td>797.6</td><td>797.6</td><td>797.6</td><td>797.6</td></tr><tr><td>Total current assets</td><td>14,556.9</td><td>15,063.2</td><td>14,306.8</td><td>14,232.8</td></tr><tr><td>Net PP&amp;E</td><td>19,671.9</td><td>19,297.5</td><td>18,856.7</td><td>18,096.7</td></tr><tr><td>Net intangibles</td><td>65.5</td><td>(21.5)</td><td>(108.6)</td><td>(195.6)</td></tr><tr><td>Total investments</td><td>21,091.0</td><td>20,941.8</td><td>20,441.8</td><td>20,441.8</td></tr><tr><td>Other long-term assets</td><td>5,343.4</td><td>5,343.4</td><td>5,343.4</td><td>5,343.4</td></tr><tr><td>Total assets</td><td>60,728.7</td><td>60,624.4</td><td>58,840.2</td><td>57,919.1</td></tr><tr><td>Accounts payable</td><td>1,661.9</td><td>1,870.5</td><td>2,081.4</td><td>2,211.0</td></tr><tr><td>Short-term debt</td><td>330.7</td><td>330.7</td><td>330.7</td><td>330.7</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>3,872.5</td><td>5,094.4</td><td>4,775.5</td><td>5,190.0</td></tr><tr><td>Total current liabilities</td><td>5,865.1</td><td>7,295.6</td><td>7,187.6</td><td>7,731.7</td></tr><tr><td>Long-term debt</td><td>12,328.2</td><td>12,328.2</td><td>12,328.2</td><td>12,328.2</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>544.5</td><td>544.5</td><td>544.5</td><td>544.5</td></tr><tr><td>Total long-term liabilities</td><td>12,872.7</td><td>12,872.7</td><td>12,872.7</td><td>12,872.7</td></tr><tr><td>Total liabilities</td><td>18,737.9</td><td>20,168.3</td><td>20,060.4</td><td>20,604.5</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>41,545.3</td><td>42,659.7</td><td>43,602.5</td><td>44,768.4</td></tr><tr><td>Minority interest</td><td>445.6</td><td>(2,203.6)</td><td>(4,822.6)</td><td>(7,453.8)</td></tr><tr><td>Total liabilities &amp; equity</td><td>60,728.7</td><td>60,624.4</td><td>58,840.2</td><td>57,919.1</td></tr><tr><td>Net debt, adjusted</td><td>5,592.0</td><td>6,315.5</td><td>7,993.9</td><td>8,653.2</td></tr></table>

<table><tr><td colspan="5">Cash Flow (NT$ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>1,693.8</td><td>3,184.1</td><td>2,693.6</td><td>3,331.4</td></tr><tr><td>D&amp;A add-back</td><td>3,993.7</td><td>3,161.4</td><td>3,427.8</td><td>3,847.1</td></tr><tr><td>Minority interest add-back</td><td>(604.0)</td><td>(649.2)</td><td>(619.0)</td><td>(631.2)</td></tr><tr><td>Net (inc)/dec working capital</td><td>207.1</td><td>(1,021.2)</td><td>(711.1)</td><td>(455.8)</td></tr><tr><td>Other operating cash flow</td><td>(337.6)</td><td>149.2</td><td>500.0</td><td>-</td></tr><tr><td>Cash flow from operations</td><td>4,953.0</td><td>4,824.4</td><td>5,291.3</td><td>6,091.5</td></tr><tr><td>Capital expenditures</td><td>(1,691.4)</td><td>(2,700.0)</td><td>(2,900.0)</td><td>(3,000.0)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>6,292.1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>511.6</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>5,112.3</td><td>(2,700.0)</td><td>(2,900.0)</td><td>(3,000.0)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>(423.9)</td><td>(847.9)</td><td>(2,069.7)</td><td>(1,750.8)</td></tr><tr><td>Inc/(dec) in debt</td><td>791.3</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>(8,785.0)</td><td>(2,000.0)</td><td>(2,000.0)</td><td>(2,000.0)</td></tr><tr><td>Cash flow from financing</td><td>(8,417.6)</td><td>(2,847.9)</td><td>(4,069.7)</td><td>(3,750.8)</td></tr><tr><td>Total cash flow</td><td>1,647.6</td><td>(723.5)</td><td>(1,678.4)</td><td>(659.3)</td></tr><tr><td>Free cash flow</td><td>3,261.6</td><td>2,124.4</td><td>2,391.3</td><td>3,091.5</td></tr></table>

Source: Company data, GS estimates.

## Downward revision to PA foundry TAM on weaker smartphone shipment We have revised down our 2026/27/28E PA foundry TAM by 1/1/4% to

US\$1.3bn/1.4bn/1.6bn as we factor in our latest smartphone shipment assumptions (-10%/+3% in 2026/27, was -6%/+2% previously, and now expect shipment to see +1% in 2028, see here) as end-demand continues to be impacted by high memory price (see here). Despite the near-term weakness in the smartphone market, we continue to believe the PA foundry house will gain share in the smartphone PA segment. This continues to be driven by the increasing design complexity and production costs of the PA, and we continue to see newer smartphone projects from design houses being allocated to foundries, which will benefit Win Semi in the long term. We expect the market TAM to deliver an 11% CAGR over 2025-30E (was 13% previously), and we expect foundries' cellular PA shipments to increase by 11% in 2026 (vs. 17% previously), while weak smartphone shipments continue to offset content value growth driven by higher 5G penetration in 2026.

Win Semi delivered 2Q26 revenue that in line with the company's guidance, with the cellular business seeing PA inventory pull-in. Management expects this momentum to continue into 3Q26 and guided revenue to be flattish to slight QoQ growth in the cellular business. We now expect Win Semi's PA foundry revenue to grow 28% YoY in 2026, outpacing the overall PA foundry TAM growth of 17% YoY, as the company continue to focus on mid-to-high-end and premium smartphone models, which are relatively more resilient to rising memory costs, although management did acknowledge potential downside risks to end-demand if high-end smartphone prices increase. Moreover, we expect Win Semi's PA foundry market share to decline from 74% in 2020 to 52% in 2026, and further to 40–50% by 2030, but its revenue will continue to expand further due to the growing foundry TAM.

We continue to see a modest recovery in 2026 CAPEX plans among Taiwan PA foundry players. However, we do not see this as an indication of a more constructive demand outlook for the PA foundry industry. Win Semi reiterated its 2026 CAPEX guidance of NT\$2-3bn, with the majority of spending allocated to the optical and infrastructure businesses rather than GaAs capacity expansion. We continue to believe GaAs capacity remains sufficient, with Win Semi's utilization rate likely reaching at most 80% during 2026-28E, implying no meaningful need for additional GaAs capacity expansion.

Exhibit 1: Win Semi's GM will be driven by utilization rate and product mix  
![](images/c5ff4d3b8304076747b721bbf235ea87ccf1c8461f536807d150e0fa45aba48d.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 2: We expect cellular PA foundry shipments to increase $11\% / 4\% / 4\%$ in 2026/27/28E  
![](images/5c6ae61c95fc4d5b7f9372ef8d1f648582319837b96792eb757c89aeebf5db70.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 3: China cellular PA market share - Foundry continues to outgrow IDM  
![](images/1006891a67081eb16a1b7e417371453e6ce804e9dd96b33054e1ebec5b1d8650.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: We believe Taiwan PA foundries' CAPEX will gradually improve starting from 2026  
![](images/f1a8f1128ffca23254820600626027a27624a894a23c5ca3bfcd50123ab6cfe6.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 5: We believe the foundry penetration rate will grow to 15%/16%/17% in 2026/27/28E  
![](images/042439d0fdff9c93273a75e94239b999360f2257af5c7959ecbc189d2c6cc93d.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 6: Win Semi 2Q26 result vs. GSe/consensus

<table><tr><td colspan="2">Win Semi (3105.TWO)</td><td colspan="2">2Q26</td><td colspan="2">QoQ</td><td colspan="2">YoY</td><td colspan="2">Bloomberg consensus</td></tr><tr><td>P&amp;L (NT$mn)</td><td>Actual</td><td>GS est.</td><td>Diff (%)</td><td>1Q26</td><td>QoQ</td><td>2Q25</td><td>YoY</td><td>Consensus</td><td>%</td></tr><tr><td>Revenue</td><td>5,257</td><td>5,109</td><td>3%</td><td>4,590</td><td>15%</td><td>3,780</td><td>39%</td><td>5,298</td><td>-1%</td></tr><tr><td>Gross profits</td><td>1,485</td><td>1,422</td><td>4%</td><td>1,209</td><td>23%</td><td>698</td><td>113%</td><td>1,550</td><td>-4%</td></tr><tr><td>Operating profits</td><td>742</td><td>477</td><td>56%</td><td>431</td><td>72%</td><td>(119)</td><td>723%</td><td>705</td><td>5%</td></tr><tr><td>Pre-tax income</td><td>1,188</td><td>477</td><td>149%</td><td>532</td><td>123%</td><td>(551)</td><td>316%</td><td>717</td><td>66%</td></tr><tr><td>Net profit</td><td>977</td><td>456</td><td>114%</td><td>533</td><td>83%</td><td>(421)</td><td>332%</td><td>656</td><td>49%</td></tr><tr><td>EPS, NT$</td><td>2.30</td><td>1.08</td><td>114%</td><td>1.26</td><td>83%</td><td>(0.99)</td><td>332%</td><td>1.51</td><td>52%</td></tr><tr><td>Gross margin (%)</td><td>28.2%</td><td>27.8%</td><td>0.4ppt</td><td>26.3%</td><td>1.9ppt</td><td>18.5%</td><td>9.8ppt</td><td>29.3%</td><td>-1.0ppt</td></tr><tr><td>EBIT margin (%)</td><td>14.1%</td><td>9.3%</td><

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any

such system.
"""
