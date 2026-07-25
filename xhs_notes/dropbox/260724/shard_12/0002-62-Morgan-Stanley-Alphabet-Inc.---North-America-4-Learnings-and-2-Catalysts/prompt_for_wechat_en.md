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
# 4 Learnings and 2 Catalysts

## WHAT'S CHANGED

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Alphabet Inc. (GOOGL.O)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>$415.00</td><td>$400.00</td></tr></table>

GOOGL cloud showed the ROIC and GenAI capex/opportunities are getting larger. We have further color on TPU accounting and SPCX. But with EPS heading \~5% lower (investments outweigh revs), new products (Gemini 4 suite of models) and visibility into '28 (TPUs) key from here. \$400PT has 20% upside.

We leave GOOGL EPS with 4 Notable Learnings and 2 Future Catalysts

1. Google Cloud: Rule of 118%...Faster, More Profitable and Durable Growth = GenAI ROIC Signal on Display: Google Cloud grew 82% y/y, beating our 77% y/y growth..as the company added \$4.7bn Q/Q. Google Cloud profitability remains impressive, with a 54% incremental margin (vs. the 57% in 1Q) and 36% 2Q EBIT margin (we were at 35%). Google Cloud's backlog reached \$514bn, up \$52bn Q/Q, and was 7% above us. This backlog gives us further confidence in durable multi-year growth ahead. Big picture, we continue to view hyperscaler revenue growth and EBIT margins as the cleanest near-term signals on GenAI investment ROIC. As a read across to AWS, in an investment world where relative share matters, this level of growth will put extra tactical pressure on AWS to deliver (our 34% y/y AWS growth implies \~\$4bn of sequential net revenue growth). That said, we would remind investors that AWS' larger contribution from API-driven revenue (with net accounting) and TPU sales make this comparison somewhat noisy.

2. GenAI Capex and Opportunities Both Getting Larger: GOOGL modestly raised its '26 capex (raising it by \$15bn at the top end to \$205bn). This was driven by an acceleration in delivery of capacity (more compute) and not component inflation. We model GOOGL's capex to increase to \$375bn in '27 as it invests for future capacity to come...notably the '28 TPUs and GPUs. Please let us know if interested in our bottom up cost per GW and capacity build for GOOGL and the hyperscalers. While spend continues to ramp, management's tone about the multitude of GenAI opportunities across enterprise and consumer and the fact that they are more bullish now than 1 year ago about the opportunities ahead (combined with their disciplined budgeting) speaks to the still under-appreciated GOOGL forward growth in years to come.

3. A Little TPU Accounting Debit and Credit Confirmation: While we didn't learn anything about '28 and that TPU opportunity (see below) we did get confirmation of our accounting debit and credit assumptions, with GOOGL purchasing TPUs and the system of components (racks, etc.) building in inventory over time. Gross TPU sales are registered in the backlog and flow through revenue within Google Cloud as they are sold. GOOGL is not licensing the technology but rather building inventory and selling it with a gross margin. While 2Q included a small amount of TPU third party

<table><tr><td colspan="2">Brian Nowak, CFA</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Brian.Nowak@morganstanley.com</td><td>+1 212 761-3365</td></tr><tr><td>Nikhil Javeri</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Nikhil.Javeri1@morganstanley.com</td><td>+1 212 761-3742</td></tr><tr><td>Gregory Gao</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Greg.Gao@morganstanley.com</td><td>+1 212 296-3125</td></tr><tr><td>Julian Herrera</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Julian.Herrera@morganstanley.com</td><td>+1 212 761-1784</td></tr><tr><td>Kavya A Narayanan</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Kavya.Narayanan@morganstanley.com</td><td>+1 212 761-4183</td></tr></table>

## Alphabet Inc. (GOOGL.O, GOOGL US)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$400.00</td></tr><tr><td>Shr price, close (Jul 22, 2026)</td><td>$342.09</td></tr><tr><td>Mkt cap, curr (mm)</td><td>$4,192,380</td></tr><tr><td>52-Week Range</td><td>$408.61-187.46</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

sales, we continue to think the majority of TPU sales (\~3.5GW) will hit in '27...with another \~4GW estimated in '28. Please let us know if interested in our TPU or updated GOOGL Cloud backlog files.

4. GOOGL's \$50/Watt Deal with SPCX Further Explained...Apple and Labs
Causing A Further Surge in Demand?: In work here we analyzed GOOGL's rental agreement with SPCX for an estimated \$50/watt. We now know this was to service "very large cloud customers" where short-term rental costs may be high, but the lifetime value of the relationships are "highly ROI positive." Given the upcoming launch of the Gemini-powered Siri AI this fall and private labs that are customers of GCP continuing to train new models, it's safe to say there are multiple explanations for GOOGL's surging near-term capacity needs. AAPL is covered by Erik Woodring. On the cost side, we are incorporating the SPCX deal into our model and adding \~\$1bn/\~\$3bn of opex in 3Q/4Q based on the deal's September start date and rate of \$920mn/month. In '27 we model an additional \~\$3bn of opex in 1Q, but assume that GOOGL will take its earliest opportunity to terminate the contract (as either party may cancel with 90 days notice after December 31). Even GOOGL management's comments about this being a 6 month deal speak to how the company is likely to opt out once they bring on their own, substantially less expensive, compute capacity.

## 2 Catalysts

Gemini 4 Suite of Models and Accelerated Go to Market: We believe GOOGL needs to deliver its Gemini 3.5 Pro and Gemini 4 suite of models (including efficient, low-cost models) to re-assure investors that it will remain on the frontier. We remain confident GOOGL will...but admittedly don't know when the models are coming. That said, management's comments about being focused on staying on the frontier and increasing the cadence of model shipping as we reach Gemini 4 (monthly) is notable.

'28 TPU Opportunity Still Under-Appreciated: While we learned some color on TPU accounting as detailed in Diving into '28 Compute Capacity, TPU Sales and Revenue to Come, we continue to think GOOGL's '28 TPU opportunity is under appreciated and that investors underestimate 1) the capex needed and 2) the upside to revenue from hosted cloud/third party TPU sales. While we still don't know the revenue per GW or margin, our base model assumes GOOGL sells each GW of TPU racks for \$20/watt (or a 20% gross margin). This is admittedly an assumption we continue to try analyze and try to learn more about.

Lower '27 EPS by 7% as Investment Outweighs Revenue, PT to \$400, Remain OW: Updating our model, we raise '26/'27 capex by 8%/7%. We now model \$375bn of capex in '27. We are also incorporating the SPCX deal into '26/'27. In all, our '27/'28 EPS falls by 7%/5% as higher investment outweighs faster revenue growth. Notably, our model assumes GOOGL will raise \$80bn of debt between now and the end of '27. We remain OW (\$400 PT has 20% upside) but believe model launches/ innovation or more visibility into long-term growth ('28 and beyond) will be important to driving outperformance.

<table><tr><td>Peer Median</td><td>14%</td><td>16x</td><td>1.2x</td></tr></table>

Exhibit 1: Our new \$400 PT implies a 24x multiple on an average of our \$15/\$18 EPS in '27/'28....

<table><tr><td colspan="4">GOOGL Valuation</td></tr><tr><td></td><td>Bear</td><td>Base</td><td>Bull</td></tr><tr><td>&#x27;27/&#x27;28 Avg. EPS</td><td>$15.18</td><td>$16.62</td><td>$17.52</td></tr><tr><td>(X) P/E</td><td>15X</td><td>24X</td><td>26X</td></tr><tr><td>(=) Price Per Share</td><td>$225</td><td>$400</td><td>$450</td></tr><tr><td>% upside/(downside)</td><td>(33%)</td><td>20%</td><td>35%</td></tr><tr><td>Implied P/E on &#x27;27 EPS</td><td>15X</td><td>27X</td><td>30X</td></tr><tr><td>Implied P/E on &#x27;28 EPS</td><td>12X</td><td>22X</td><td>25X</td></tr></table>

Source: Company data, MS

Exhibit 2: ... and implies a \~30% premium to peers on a growth adjusted basis (vs. the \~10% premium that GOOGL currently trades at)

<table><tr><td>Peer Set</td><td>Share Price</td><td>&#x27;28 EPS</td><td>&#x27;25-&#x27;28 EPS CAGR</td><td>&#x27;28 P/E</td><td>&#x27;28 PEG</td></tr><tr><td>AAPL</td><td>$326</td><td>$11</td><td>10%</td><td>29x</td><td>2.8x</td></tr><tr><td>MSFT</td><td>$390</td><td>$27</td><td>14%</td><td>15x</td><td>1.1x</td></tr><tr><td>META</td><td>$627</td><td>$33</td><td>9%</td><td>19x</td><td>2.0x</td></tr><tr><td>AMZN</td><td>$245</td><td>$15</td><td>20%</td><td>16x</td><td>0.8x</td></tr><tr><td>NFLX</td><td>$69</td><td>$4</td><td>15%</td><td>15x</td><td>1.0x</td></tr></table>

<table><tr><td>GOOGL @ Current Share Price</td><td>Share Price</td><td>&#x27;28 EPS</td><td>&#x27;25-&#x27;28 EPS CAGR</td><td>&#x27;28 P/E</td><td>&#x27;28 PEG</td></tr><tr><td>GOOGL</td><td>$333</td><td>$18.2</td><td>14%</td><td>18x</td><td>1.3x</td></tr><tr><td>Premium/(Discount) vs. Median</td><td></td><td></td><td></td><td>13%</td><td>11%</td></tr></table>

<table><tr><td>GOOGL @ $400 PT</td><td>Share Price</td><td>&#x27;28 EPS</td><td>&#x27;25-&#x27;28 EPS CAGR</td><td>&#x27;28 P/E</td><td>&#x27;28 PEG</td></tr><tr><td>GOOGL</td><td>$400</td><td>$18.2</td><td>14%</td><td>22x</td><td>1.6x</td></tr><tr><td>Premium/(Discount) vs. Median</td><td></td><td></td><td></td><td>35%</td><td>33%</td></tr></table>

Source: Company data, MS

## Changes to Our Estimates

Exhibit 3: Changes to our GOOGL estimates

<table><tr><td></td><td>2026 Prior</td><td>2027 Prior</td><td>2028 Prior</td></tr><tr><td>Total Gross revenue (GAAP)</td><td>497,283.6</td><td>650,119.0</td><td>782,949.4</td></tr><tr><td>Traffic acquisition costs (TAC)</td><td>65,702.9</td><td>70,981.9</td><td>75,371.5</td></tr><tr><td>TAC as % of advertising revenue</td><td>19.7%</td><td>19.4%</td><td>19.1%</td></tr><tr><td>Total Net revenue</td><td>431,580.7</td><td>579,137.0</td><td>707,578.0</td></tr><tr><td>Other cost of revenue (ex-TAC, ex-SBC)</td><td>121,879.3</td><td>180,643.9</td><td>231,645.7</td></tr><tr><td>Gross profit (GAAP)</td><td>304,738.6</td><td>392,811.8</td><td>469,495.4</td></tr><tr><td>Gross margin</td><td>70.6%</td><td>67.8%</td><td>66.4%</td></tr><tr><td>Total costs &amp; expenses (GAAP)</td><td>316,622.6</td><td>408,202.8</td><td>493,768.3</td></tr><tr><td>Total operating expenses (Non-GAAP)</td><td>124,077.6</td><td>150,895.7</td><td>180,314.3</td></tr><tr><td>Research and development (ex-SBC)</td><td>60,207.8</td><td>80,275.0</td><td>102,323.9</td></tr><tr><td>Sales and marketing (ex-SBC)</td><td>26,685.6</td><td>28,747.8</td><td>31,231.8</td></tr><tr><td>General and administrative (ex-SBC)</td><td>13,357.4</td><td>14,620.8</td><td>15,882.2</td></tr><tr><td>Stock-based compensation</td><td>28,789.5</td><td>32,933.3</td><td>37,313.3</td></tr><tr><td>Depreciation</td><td>34,539.8</td><td>70,221.8</td><td>117,636.6</td></tr><tr><td>Non-recurring items</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>EBITDA (adjusted)</td><td>245,262</td><td>346,781</td><td>444,233</td></tr><tr><td>EBITDA margin (adjusted)</td><td>56.8%</td><td>59.9%</td><td>62.8%</td></tr><tr><td>Incremental EBITDA margin</td><td>79.1%</td><td>68.8%</td><td>75.9%</td></tr><tr><td>Total operating income (GAAP)</td><td>180,661</td><td>241,916</td><td>289,181</td></tr><tr><td>Total operating income margin (GAAP)</td><td>36.3%</td><td>37.2%</td><td>36.9%</td></tr><tr><td>Other income/(expense), net (GAAP)</td><td>40,039.5</td><td>1,280.6</td><td>(2,594.5)</td></tr><tr><td>Pretax income (GAAP)</td><td>220,700.5</td><td>243,196.8</td><td>286,586.6</td></tr><tr><td>Income tax expense (GAAP)</td><td>37,760.2</td><td>38,911.5</td><td>46,956.8</td></tr><tr><td>Tax rate (GAAP)</td><td>17.1%</td><td>16.0%</td><td>16.4%</td></tr><tr><td>Net income (reported GAAP)</td><td>182,940.4</td><td>204,285.3</td><td>239,629.8</td></tr><tr><td>Net income (GAAP), continuing ops</td><td>182,940.4</td><td>204,285.3</td><td>239,629.8</td></tr><tr><td>EPS (GAAP)</td><td>$14.80</td><td>$16.30</td><td>$19.12</td></tr><tr><td>Basic shares</td><td>12,227.5</td><td>12,399.7</td><td>12,397.8</td></tr><tr><td>Diluted shares</td><td>12,361.8</td><td>12,536.0</td><td>12,534.0</td></tr><tr><td>Free Cash Flow</td><td>20,659.9</td><td>(33,366.0)</td><td>23,164.6</td></tr><tr><td>Free Cash Flow per Share</td><td>$1.67</td><td>($2.66)</td><td>$1.85</td></tr><tr><td>Capex</td><td>$189,596.00</td><td>$349,846.00</td><td>$374,846.00</td></tr></table>

Source: Company data, MS

<table><tr><td>2026Current</td><td>2027Current</td><td>2028Current</td></tr><tr><td>500,610.9</td><td>653,470.7</td><td>793,581.8</td></tr><tr><td>65,567.3</td><td>70,315.9</td><td>75,049.4</td></tr><tr><td>19.6%</td><td>19.4%</td><td>19.1%</td></tr><tr><td>435,043.7</td><td>583,154.8</td><td>718,532.4</td></tr><tr><td>125,230.1</td><td>198,462.1</td><td>255,299.0</td></tr><tr><td>304,646.7</td><td>378,980.8</td><td>456,981.6</td></tr><tr><td>70.0%</td><td>65.0%</td><td>63.6%</td></tr><tr><td>324,215.6</td><td>426,009.6</td><td>512,699.8</td></tr><tr><td>128,251.4</td><td>151,519.8</td><td>176,099.6</td></tr><tr><td>60,713.9</td><td>80,900.7</td><td>99,681.5</td></tr><tr><td>27,487.1</td><td>28,779.9</td><td>31,149.9</td></tr><tr><td>15,225.9</td><td>14,450.1</td><td>15,289.8</td></tr><tr><td>29,991.3</td><td>33,100.9</td><td>36,230.2</td></tr><tr><td>34,069.4</td><td>74,108.9</td><td>124,665.4</td></tr><tr><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>241,667</td><td>337,106</td><td>441,880</td></tr><tr><td>55.6%</td><td>57.8%</td><td>61.5%</td></tr><tr><td>72.2%</td><td>64.4%</td><td>77.4%</td></tr><tr><td>176,395</td><td>227,461</td><td>280,882</td></tr><tr><td>35.2%</td><td>34.8%</td><td>35.4%</td></tr><tr><td>135,399.7</td><td>(2,171.2)</td><td>(8,057.7)</td></tr><tr><td>311,795.0</td><td>225,289.8</td><td>272,824.3</td></tr><tr><td>56,694.8</td><td>36,046.4</td><td>44,941.4</td></tr><tr><td>18.2%</td><td>16.0%</td><td>16.5%</td></tr><tr><td>255,100.2</td><td>189,243.5</td><td>227,883.0</td></tr><tr><td>255,100.2</td><td>189,243.5</td><td>227,883.0</td></tr><tr><td>$20.62</td><td>$15.08</td><td>$18.16</td></tr><tr><td>12,221.3</td><td>12,399.7</td><td>12,397.8</td></tr><tr><td>12,369.6</td><td>12,550.8</td><td>12,548.8</td></tr><tr><td>(11,545.2)</td><td>(67,956.2)</td><td>(9,140.3)</td></tr><tr><td>($0.93)</td><td>($5.41)</td><td>($0.73)</td></tr><tr><td>$204,996.00</td><td>$375,046.00</td><td>$400,046.00</td></tr></table>

<table><tr><td>2026Revision</td><td>2027Revision</td><td>2028Revision</td></tr><tr><td>0.7%</td><td>0.5%</td><td>1.4%</td></tr><tr><td>-0.2%</td><td>-0.9%</td><td>-0.4%</td></tr><tr><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>0.8%</td><td>0.7%</td><td>1.5%</td></tr><tr><td>2.7%</td><td>9.9%</td><td>10.2%</td></tr><tr><td>0.0%</td><td>-3.5%</td><td>-2.7%</td></tr><tr><td>2.4%</td><td>4.4%</td><td>3.8%</td></tr><tr><td>3.4%</td><td>0.4%</td><td>-2.3%</td></tr><tr><td>0.8%</td><td>0.8%</td><td>-2.6%</td></tr><tr><td>3.0%</td><td>0.1%</td><td>-0.3%</td></tr><tr><td>14.0%</td><td>-1.2%</td><td>-3.7%</td></tr><tr><td>4.2%</td><td>0.5%</td><td>-2.9%</td></tr><tr><td>-1.4%</td><td>5.5%</td><td>6.0%</td></tr><tr><td>--</td><td>--</td><td>--</td></tr><tr><td>-1.5%</td><td>-2.8%</td><td>-0.5%</td></tr><tr><td>-1.3%</td><td>-2.1%</td><td>-1.3%</td></tr><tr><td>-6.9%</td><td>-4.4%</td><td>1.5%</td></tr><tr><td>-2.4%</td><td>-6.0%</td><td>-2.9%</td></tr><tr><td>-1.1%</td><td>-2.4%</td><td>-1.5%</td></tr><tr><td>238.2%</td><td>-269.5%</td><td>210.6%</td></tr><tr><td>41.3%</td><td>-7.4%</td><td>-4.8%</td></tr><tr><td>50.1%</td><td>-7.4%</td><td>-4.3%</td></tr><tr><td>107 bp</td><td>0 bp</td><td>9 bp</td></tr><tr><td>39.4%</td><td>-7.4%</td><td>-4.9%</td></tr><tr><td>39.4%</td><td>-7.4%</td><td>-4.9%</td></tr><tr><td>39.4%</td><td>-7.5%</td><td>-5.0%</td></tr><tr><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>0.1%</td><td>0.1%</td><td>0.1%</td></tr><tr><td>-155.9%</td><td>103.7%</td><td>-139.5%</td></tr><tr><td>-155.8%</td><td>103.4%</td><td>-139.4%</td></tr><tr><td>8.1%</td><td>7.2%</td><td>6.7%</td></tr></table>

# Results vs. MS Estimates

## Exhibit 4: GOOGL 2Q26 results vs MS estimates

GOOGL

Actuals versus Estimates (\$ in millions)

<table><tr><td rowspan="2"></td><td colspan="2">2Q2026</td><td colspan="2">Variance</td></tr><tr><td>Actual</td><td>Estimate</td><td>Absolute</td><td>Percent</td></tr><tr><td>Total Gross revenue (GAAP)</td><td>119,796.0</td><td>117,443.8</td><td>2,352.2</td><td>2.0%</td></tr><tr><td>Google Search &amp; Other</td><td>63,271.0</td><td>63,633.3</td><td>(362.3)</td><td>-0.6%</td></tr><tr><td>YouTube Ads</td><td>11,055.0</td><td>10,779.1</td><td>275.9</td><td>2.6%</td></tr><tr><td>Google properties</td><td>74,326.0</td><td>74,412.4</td><td>(86.4)</td><td>-0.1%</td></tr><tr><td>% Y/Y ex-FX growth</td><td>15.1%</td><td>13.1%</td><td>2.0%</td><td></td></tr><tr><td>Gross Google Network websites</td><td>7,303.0</td><td>7,181.8</td><td>121.2</td><td>1.7%</td></tr><tr><td>% Y/Y ex-FX growth</td><td>-2.4%</td><td>-7.6%</td><td>5.1%</td><td></td></tr><tr><td>Gross Other revenue (Google + Other Bets)</td><td>38,061.0</td><td>35,899.7</td><td>2,161.3</td><td>6.0%</td></tr><tr><td>Traffic acquisition costs (TAC)</td><td>16,179.0</td><td>16,243.1</td><td>(64.1)</td><td>-0.4%</td></tr><tr><td>TAC as % of advertising revenue</td><td>19.8%</td><td>19.9%</td><td>(9) bp</td><td></td></tr><tr><td>Total Net revenue</td><td>103,617.0</td><td>101,200.7</td><td>2,416.3</td><td>2.4%</td></tr><tr><td>Other cost of revenue (ex-TAC, ex-SBC)</td><td>28,414.0</td><td>28,985.2</td><td>(571.2)</td><td>-2.0%</td></tr><tr><td>% of Revenue</td><td>27%</td><td>29%</td><td>(122) bp</td><td></td></tr><tr><td>Gross profit (GAAP)</td><td>73,853.0</td><td>71,059.8</td><td>2,793.2</td><td>3.9%</td></tr><tr><td>Gross margin</td><td>71.3%</td><td>70.2%</td><td>106bp</td><td></td></tr><tr><td>Total costs &amp; expenses (GAAP)</td><td>79,026.0</td><td>75,584.4</td><td>3,

[中间内容因长度限制已省略]

tivity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Internet

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/22/2026)</td></tr><tr><td colspan="3">Brian Nowak, CFA</td></tr><tr><td>Airbnb Inc (ABNB.O)</td><td>U (12/06/2022)</td><td>$140.05</td></tr><tr><td>Alphabet Inc. (GOOGL.O)</td><td>O (08/11/2015)</td><td>$342.09</td></tr><tr><td>Amazon.com Inc (AMZN.O)</td><td>O (04/24/2015)</td><td>$244.85</td></tr><tr><td>Booking Holdings Inc (BKNG.O)</td><td>O (02/23/2026)</td><td>$177.86</td></tr><tr><td>DoorDash Inc (DASH.O)</td><td>O (02/21/2024)</td><td>$177.73</td></tr><tr><td>Expedia Inc. (EXPE.O)</td><td>E (01/09/2019)</td><td>$261.08</td></tr><tr><td>Instacart (CART.O)</td><td>E (01/29/2024)</td><td>$44.73</td></tr><tr><td>Lyft Inc (LYFT.O)</td><td>E (10/24/2019)</td><td>$14.66</td></tr><tr><td>Meta Platforms Inc (META.O)</td><td>O (03/20/2023)</td><td>$627.17</td></tr><tr><td>Pinterest Inc (PINS.N)</td><td>O (07/20/2025)</td><td>$22.54</td></tr><tr><td>Reddit Inc (RDDT.N)</td><td>O (12/08/2024)</td><td>$170.38</td></tr><tr><td>Snap Inc. (SNAP.N)</td><td>E (07/22/2024)</td><td>$4.47</td></tr><tr><td>Uber Technologies Inc (UBER.N)</td><td>++</td><td>$70.33</td></tr><tr><td colspan="3">Matthew Cost</td></tr><tr><td>AppLovin Corp (APP.O)</td><td>O (04/10/2025)</td><td>$412.48</td></tr><tr><td>Compass, Inc. (COMP.N)</td><td>E (01/12/2026)</td><td>$11.26</td></tr><tr><td>Criteo SA (CRTO.O)</td><td>E (01/26/2016)</td><td>$21.05</td></tr><tr><td>DoubleVerify Holdings Inc (DV.N)</td><td>E (06/25/2024)</td><td>$10.89</td></tr><tr><td>Electronic Arts Inc (EA.O)</td><td>E (08/04/2021)</td><td>$208.95</td></tr><tr><td>Liftoff Mobile Inc. (LFTO.O)</td><td>E (06/29/2026)</td><td>$22.34</td></tr><tr><td>MNTN Inc (MNTN.N)</td><td>E (06/16/2025)</td><td>$8.57</td></tr><tr><td>Opendoor Technologies Inc (OPEN.O)</td><td>E (07/24/2023)</td><td>$4.38</td></tr><tr><td>Playtika Holding Corp (PLTK.O)</td><td>E (11/27/2022)</td><td>$3.82</td></tr><tr><td>Roblox Corporation (RBLX.N)</td><td>O (11/04/2024)</td><td>$49.64</td></tr><tr><td>Shutterstock Inc (SSTK.N)</td><td>E (07/28/2022)</td><td>$7.38</td></tr><tr><td>Take-Two Interactive Software (TTWO.O)</td><td>O (02/01/2018)</td><td>$233.58</td></tr><tr><td>Trade Desk Inc (TTD.O)</td><td>E (09/10/2025)</td><td>$17.58</td></tr><tr><td>Unity Software Inc (U.N)</td><td>O (09/02/2024)</td><td>$29.27</td></tr><tr><td>Webtoon Entertainment Inc (WBTN.O)</td><td>E (07/22/2024)</td><td>$9.43</td></tr><tr><td>Yelp Inc (YELP.N)</td><td>U (01/10/2019)</td><td>$24.81</td></tr><tr><td>Zillow Group Inc (Z.O)</td><td>E (04/18/2018)</td><td>$31.36</td></tr><tr><td colspan="3">Nathan Feather</td></tr><tr><td>Bumble Inc. (BMBL.O)</td><td>E (03/08/2021)</td><td>$2.81</td></tr><tr><td>Chewy Inc (CHWY.N)</td><td>O (10/31/2023)</td><td>$21.52</td></tr><tr><td>Duolingo Inc (DUOL.O)</td><td>E (02/27/2026)</td><td>$119.51</td></tr><tr><td>eBay Inc (EBAY.O)</td><td>O (04/18/2024)</td><td>$110.95</td></tr><tr><td>Etsy Inc (ETSY.N)</td><td>E (07/20/2025)</td><td>$80.48</td></tr><tr><td>FIGS, Inc. (FIGS.N)</td><td>E (02/29/2024)</td><td>$9.92</td></tr><tr><td>Grindr Inc. (GRND.N)</td><td>O (07/01/2026)</td><td>$14.50</td></tr><tr><td>Match Group Inc (MTCH.O)</td><td>E (04/18/2024)</td><td>$38.03</td></tr><tr><td>Peloton Interactive, Inc. (PTON.O)</td><td>E (03/14/2022)</td><td>$6.26</td></tr><tr><td>Revolve Group Inc (RVLV.N)</td><td>E (10/20/2024)</td><td>$25.37</td></tr><tr><td>WW International Inc (WW.O)</td><td>E (08/01/2025)</td><td>$14.75</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
