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
EQUITY: INTERNET & NEW MEDIA

# Expect weaker 2Q26F profits on investment losses

## New game performing in line; maintain Buy rating

2Q26F: investment losses likely to derail an otherwise decent quarter; maintain Buy We anticipate NetEase (NTES) to report in-line revenue and better operating profit (OP), but net profit likely came in lower due to the bigger investment losses stemming from its holdings of Alibaba (BABA US, Buy) and Pinduoduo (PDD US, Neutral) shares.

We have modeled for 5% y-y revenue growth to CNY29.3bn, which is largely in line with the Bloomberg consensus estimate of CNY29.4bn. 2Q was a quiet quarter for NTES' online gaming business due to a lack of new titles, but we estimate NTES' online game and VAS segment likely posted impressive growth of 6% y-y, despite a still-high base effect, driven by the resilient performance of evergreen titles such as PC FWJ, Eggy Party and WWM.

The gross margin (GM) of NTES' online gaming business likely expanded 2.8pp y-y to $73\%$ backed by an increased share of revenue from higher-margin self-developed PC games. As a result, the blended GM likely improved 2.5pp to $67.2\%$ , better than the Street consensus of $66.9\%$ .

We project GAAP operating profit (OP) likely increased a robust 20% y-y to CNY10.8bn, which is 2% above the consensus estimate of CNY10.6bn due to higher margins. Our projected GAAP operating profit margin (OPM) improved 4.5pp y-y to 37% on the back of GM expansion and spending discipline. Our non-GAAP OP likely rose 14% to CNY11.4bn.

While we are expecting better-than-expected OP, NTES' non-GAAP net profit likely came in at CNY9.4bn, which is 8% below consensus of CNY10.2bn due to its holdings of Alibaba and PDD shares. Based on our calculation, the mark-to-market investment loss related to these two holdings likely amounted to CNY663mn in 2Q26F.

NTES launched its widely-anticipated new game, Sea of Remnants (SoR) recently. The performance of this game has been in line with our expectations so far – and likely on track to generate CNY200-300mn/month in gross billing. While SoR is not a super blockbuster title like WWM, we believe its launch will still serve to accelerate NTES' game growth in 2H26F.

We maintain our Buy rating and TP of USD155, implying an unchanged 17x FY26F P/E, vs the current FY26F P/E of 13x.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>112,626</td><td>119,723</td><td>119,723</td><td>128,358</td><td>128,358</td><td>134,258</td><td>134,258</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>33,760</td><td>38,394</td><td>38,394</td><td>41,864</td><td>41,864</td><td>44,072</td><td>44,072</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>37,344</td><td>40,742</td><td>40,742</td><td>44,386</td><td>44,386</td><td>46,712</td><td>46,712</td><td></td></tr><tr><td>FD normalised EPS</td><td>58.02</td><td>63.62</td><td>63.62</td><td>69.66</td><td>69.66</td><td>73.68</td><td>73.68</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>11.9</td><td>9.6</td><td>9.6</td><td>9.5</td><td>9.5</td><td>5.8</td><td>5.8</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>14.7</td><td>-</td><td>12.8</td><td>-</td><td>11.7</td><td>-</td><td>11.1</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>12.8</td><td>-</td><td>9.5</td><td>-</td><td>8.6</td><td>-</td><td>7.2</td><td></td></tr><tr><td>Price/book (x)</td><td>3.3</td><td>-</td><td>2.7</td><td>-</td><td>2.4</td><td>-</td><td>2.1</td><td></td></tr><tr><td>Dividend yield (%)</td><td>2.5</td><td>-</td><td>3.0</td><td>-</td><td>3.3</td><td>-</td><td>3.4</td><td></td></tr><tr><td>ROE (%)</td><td>22.6</td><td>22.1</td><td>22.1</td><td>20.9</td><td>20.9</td><td>19.3</td><td>19.3</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

27 July 2026

Rating Remains Buy

Target price Remains USD 155.00

Closing price 24 July 2026 USD 119.55

<table><tr><td>Implied upside</td><td>+29.7%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>76,541.9</td></tr><tr><td>ADT (USD mn)</td><td>124.6</td></tr></table>

## Relative performance chart

![](images/98c205c2cbdad45f8091c42f811caa2fbe622eafe92d423f489215edb2f1eb0a.jpg)  
Source: LSEG, NOM

## Research Analysts

China Internet & New Media

Jialong Shi - NIHK

Jialong.shi@NOM.com +852 2252 1409

Rachel Guo - NIHK
rachel.guo@NOM.com
+852 2252 1400

## Key data on NetEase

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (USD)</td><td>1.6</td><td>8.1</td><td>-12.3</td><td>M cap (USDmn)</td><td>76,541.9</td></tr><tr><td>Absolute (USD)</td><td>1.6</td><td>8.1</td><td>-12.3</td><td>Free float (%)</td><td>55.6</td></tr><tr><td>Rel to NASDAQ COMPOSITE</td><td>3.6</td><td>7.6</td><td>-30.9</td><td>3-mth ADT (USDmn)</td><td>124.6</td></tr></table>

<table><tr><td colspan="6">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>105,295</td><td>112,626</td><td>119,723</td><td>128,358</td><td>134,258</td></tr><tr><td>Cost of goods sold</td><td>-38,302</td><td>-39,219</td><td>-39,549</td><td>-41,659</td><td>-43,428</td></tr><tr><td>Gross profit</td><td>66,993</td><td>73,406</td><td>80,173</td><td>86,700</td><td>90,830</td></tr><tr><td>SG&amp;A</td><td>-33,526</td><td>-33,924</td><td>-35,318</td><td>-37,481</td><td>-38,801</td></tr><tr><td>Employee share expense</td><td>-3,883</td><td>-3,648</td><td>-2,411</td><td>-2,585</td><td>-2,704</td></tr><tr><td>Operating profit</td><td>29,584</td><td>35,835</td><td>42,444</td><td>46,634</td><td>49,325</td></tr><tr><td>EBITDA</td><td>32,002</td><td>38,082</td><td>44,833</td><td>49,195</td><td>52,004</td></tr><tr><td>Depreciation</td><td>-2,418</td><td>-2,247</td><td>-2,389</td><td>-2,561</td><td>-2,679</td></tr><tr><td>Amortisation</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBIT</td><td>29,584</td><td>35,835</td><td>42,444</td><td>46,634</td><td>49,325</td></tr><tr><td>Net interest expense</td><td>4,921</td><td>3,953</td><td>4,000</td><td>4,000</td><td>4,000</td></tr><tr><td>Associates &amp; JCEs</td><td>355</td><td>732</td><td>600</td><td>600</td><td>600</td></tr><tr><td>Other income</td><td>858</td><td>311</td><td>465</td><td>1,087</td><td>1,087</td></tr><tr><td>Earnings before tax</td><td>35,718</td><td>40,830</td><td>47,508</td><td>52,320</td><td>55,012</td></tr><tr><td>Income tax</td><td>-5,461</td><td>-6,033</td><td>-8,076</td><td>-9,418</td><td>-9,902</td></tr><tr><td>Net profit after tax</td><td>30,256</td><td>34,798</td><td>39,432</td><td>42,902</td><td>45,110</td></tr><tr><td>Minority interests</td><td>-559</td><td>-1,038</td><td>-1,038</td><td>-1,038</td><td>-1,038</td></tr><tr><td>Other items</td><td>3,813</td><td>3,584</td><td>2,348</td><td>2,522</td><td>2,641</td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td>33,511</td><td>37,344</td><td>40,742</td><td>44,386</td><td>46,712</td></tr><tr><td>Extraordinary items</td><td>-3,813</td><td>-3,584</td><td>-2,348</td><td>-2,522</td><td>-2,641</td></tr><tr><td>Reported NPAT</td><td>29,698</td><td>33,760</td><td>38,394</td><td>41,864</td><td>44,072</td></tr><tr><td>Dividends</td><td>-11,879</td><td>-13,504</td><td>-15,358</td><td>-16,746</td><td>-17,629</td></tr><tr><td>Transfer to reserves</td><td>17,819</td><td>20,256</td><td>23,036</td><td>25,119</td><td>26,443</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>18.7</td><td>16.3</td><td>13.6</td><td>12.4</td><td>11.7</td></tr><tr><td>Normalised P/E (x)</td><td>16.6</td><td>14.7</td><td>12.8</td><td>11.7</td><td>11.1</td></tr><tr><td>FD normalised P/E (x)</td><td>16.6</td><td>14.7</td><td>12.8</td><td>11.7</td><td>11.1</td></tr><tr><td>Dividend yield (%)</td><td>2.2</td><td>2.5</td><td>3.0</td><td>3.3</td><td>3.4</td></tr><tr><td>Price/cashflow (x)</td><td>14.0</td><td>10.8</td><td>8.5</td><td>22.2</td><td>7.5</td></tr><tr><td>Price/book (x)</td><td>4.0</td><td>3.3</td><td>2.7</td><td>2.4</td><td>2.1</td></tr><tr><td>EV/EBITDA (x)</td><td>15.5</td><td>12.8</td><td>9.5</td><td>8.6</td><td>7.2</td></tr><tr><td>EV/EBIT (x)</td><td>16.7</td><td>13.6</td><td>10.0</td><td>9.0</td><td>7.6</td></tr><tr><td>Gross margin (%)</td><td>63.6</td><td>65.2</td><td>67.0</td><td>67.5</td><td>67.7</td></tr><tr><td>EBITDA margin (%)</td><td>30.4</td><td>33.8</td><td>37.4</td><td>38.3</td><td>38.7</td></tr><tr><td>EBIT margin (%)</td><td>28.1</td><td>31.8</td><td>35.5</td><td>36.3</td><td>36.7</td></tr><tr><td>Net margin (%)</td><td>28.2</td><td>30.0</td><td>32.1</td><td>32.6</td><td>32.8</td></tr><tr><td>Effective tax rate (%)</td><td>15.3</td><td>14.8</td><td>17.0</td><td>18.0</td><td>18.0</td></tr><tr><td>Dividend payout (%)</td><td>40.0</td><td>40.0</td><td>40.0</td><td>40.0</td><td>40.0</td></tr><tr><td>ROE (%)</td><td>22.6</td><td>22.6</td><td>22.1</td><td>20.9</td><td>19.3</td></tr><tr><td>ROA (pretax %)</td><td>19.7</td><td>23.5</td><td>26.3</td><td>27.9</td><td>28.6</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>1.8</td><td>7.0</td><td>6.3</td><td>7.2</td><td>4.6</td></tr><tr><td>EBITDA</td><td>4.0</td><td>19.0</td><td>17.7</td><td>9.7</td><td>5.7</td></tr><tr><td>Normalised EPS</td><td>3.4</td><td>11.9</td><td>9.6</td><td>9.5</td><td>5.8</td></tr><tr><td>Normalised FDEPS</td><td>3.4</td><td>11.9</td><td>9.6</td><td>9.5</td><td>5.8</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>32,002</td><td>38,082</td><td>44,833</td><td>49,195</td><td>52,004</td></tr><tr><td>Change in working capital</td><td>-9,958</td><td>-10,374</td><td>22,269</td><td>-18,478</td><td>24,297</td></tr><tr><td>Other operating cashflow</td><td>17,633</td><td>23,031</td><td>-5,821</td><td>-7,276</td><td>-7,495</td></tr><tr><td>Cashflow from operations</td><td>39,677</td><td>50,740</td><td>61,281</td><td>23,441</td><td>68,806</td></tr><tr><td>Capital expenditure</td><td>-2,206</td><td>-2,052</td><td>-1,133</td><td>-1,214</td><td>-1,270</td></tr><tr><td>Free cashflow</td><td>37,470</td><td>48,687</td><td>60,148</td><td>22,227</td><td>67,536</td></tr><tr><td>Reduction in investments</td><td>25,415</td><td>-17,198</td><td>-5,000</td><td>-5,000</td><td>-5,000</td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>1,011</td><td>1,773</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Inc in other LT liabilities</td><td>-169</td><td>112</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Adjustments</td><td>-6,134</td><td>-15,816</td><td>5,000</td><td>5,000</td><td>5,000</td></tr><tr><td>CF after investing acts</td><td>57,593</td><td>17,558</td><td>60,148</td><td>22,227</td><td>67,536</td></tr><tr><td>Cash dividends</td><td>-11,165</td><td>-13,826</td><td>-14,431</td><td>-16,052</td><td>-17,187</td></tr><tr><td>Equity issue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>-7,476</td><td>-5,799</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>-8,688</td><td>-917</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>-27,330</td><td>-20,541</td><td>-14,431</td><td>-16,052</td><td>-17,187</td></tr><tr><td>Net cashflow</td><td>30,264</td><td>-2,982</td><td>45,718</td><td>6,176</td><td>50,348</td></tr><tr><td>Beginning cash</td><td>24,206</td><td>54,470</td><td>51,487</td><td>97,205</td><td>103,380</td></tr><tr><td>Ending cash</td><td>54,470</td><td>51,487</td><td>97,205</td><td>103,380</td><td>153,729</td></tr><tr><td>Ending net debt</td><td>-54,470</td><td>-51,487</td><td>-97,205</td><td>-103,380</td><td>-153,729</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>54,470</td><td>51,487</td><td>97,205</td><td>103,380</td><td>153,729</td></tr><tr><td>Marketable securities</td><td>75,441</td><td>92,639</td><td>97,639</td><td>102,639</td><td>107,639</td></tr><tr><td>Accounts receivable</td><td>5,669</td><td>5,338</td><td>5,158</td><td>6,095</td><td>5,676</td></tr><tr><td>Inventories</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other current assets</td><td>17,745</td><td>31,151</td><td>14,770</td><td>34,463</td><td>17,033</td></tr><tr><td>Total current assets</td><td>153,325</td><td>180,615</td><td>214,773</td><td>246,578</td><td>284,077</td></tr><tr><td>LT investments</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Fixed assets</td><td>8,520</td><td>8,425</td><td>7,169</td><td>5,822</td><td>4,413</td></tr><tr><td>Goodwill</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other intangible assets</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT assets</td><td>34,147</td><td>32,374</td><td>32,374</td><td>32,374</td><td>32,374</td></tr><tr><td>Total assets</td><td>195,992</td><td>221,415</td><td>254,316</td><td>284,774</td><td>320,864</td></tr><tr><td>Short-term debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accounts payable</td><td>721</td><td>643</td><td>2,694</td><td>823</td><td>2,844</td></tr><tr><td>Other current liabilities</td><td>48,947</td><td>51,726</td><td>55,384</td><td>59,407</td><td>63,833</td></tr><tr><td>Total current liabilities</td><td>49,668</td><td>52,369</td><td>58,078</td><td>60,230</td><td>66,677</td></tr><tr><td>Long-term debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Convertible debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other LT liabilities</td><td>3,830</td><td>3,942</td><td>3,942</td><td>3,942</td><td>3,942</td></tr><tr><td>Total liabilities</td><td>53,497</td><td>56,311</td><td>62,020</td><td>64,172</td><td>70,619</td></tr><tr><td>Minority interest</td><td>3,809</td><td>4,808</td><td>5,846</td><td>6,884</td><td>7,922</td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Retained earnings</td><td>118,454</td><td>136,251</td><td>160,551</td><td>186,431</td><td>214,153</td></tr><tr><td>Proposed dividends</td><td>11,879</td><td>13,504</td><td>15,358</td><td>16,746</td><td>17,629</td></tr><tr><td>Other equity and reserves</td><td>8,350</td><td>10,538</td><td>10,538</td><td>10,538</td><td>10,538</td></tr><tr><td>Total shareholders&#x27; equity</td><td>138,686</td><td>160,296</td><td>186,450</td><td>213,718</td><td>242,323</td></tr><tr><td>Total equity &amp; liabilities</td><td>195,992</td><td>221,415</td><td>254,316</td><td>284,774</td><td>320,864</td></tr><tr><td colspan="6">Liquidity (x)</td></tr><tr><td>Current ratio</td><td>3.09</td><td>3.45</td><td>3.70</td><td>4.09</td><td>4.26</td></tr><tr><td>Interest cover</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="6">Leverage</td></tr><tr><td>Net debt/EBITDA (x)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td colspan="6">Per share</td></tr><tr><td>Reported EPS (CNY)</td><td>45.96</td><td>52.45</td><td>59.95</td><td>65.70</td><td>69.51</td></tr><tr><td>Norm EPS (CNY)</td><td>51.86</td><td>58.02</td><td>63.62</td><td>69.66</td><td>73.68</td></tr><tr><td>FD norm EPS (CNY)</td><td>51.86</td><td>58.02</td><td>63.62</td><td>69.66</td><td>73.68</td></tr><tr><td>BVPS (CNY)</td><td>216.67</td><td>251.53</td><td>294.04</td><td>338.73</td><td>386.00</td></tr><tr><td>DPS (CNY)</td><td>18.56</td><td>21.19</td><td>24.22</td><td>26.54</td><td>28.08</td></tr><tr><td colspan="6">Activity (days)</td></tr><tr><td>Days receivable</td><td>21.0</td><td>17.8</td><td>16.0</td><td>16.0</td><td>16.0</td></tr><tr><td>Days inventory</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td></td></tr><tr><td>Days payable</td><td>7.6</td><td>6.3</td><td>15.4</td><td>15.4</td><td>15.5</td></tr><tr><td>Cash cycle</td><td>13.3</td><td>11.5</td><td>0.6</td><td>0.6</td><td>0.6</td></tr></table>

Source: Company data, NOM estimates

## Company profile

NetEase is one of the largest game developers and publishers in China. The company also provides a variety of other services including music streaming, live broadcasting, news service, and education service, among others.

## Valuation Methodology

We value the company's online gaming business at US73bn based on 17x FY26F P/E. We value NTES' music business at USD2bn based on its latest market cap. The resulting TP is USD155. The benchmark index for the company is Nasdaq Composite.

Risks that may impede the achievement of the target price

Downside risks: 1) bigger margin contraction from incubated business; and 2) lower-than-expected grossing of legacy titles like FWJ.

## ESG

NetEase's business is environment-friendly as it does not cause pollution or generate greenhouse gas.

Fig. 1: NTES: 2Q26F results preview

<table><tr><td colspan="8">2Q26F results preview</td></tr><tr><td>CNYmn</td><td>2Q26F</td><td>1Q26</td><td>2Q25</td><td>YoY</td><td>QoQ</td><td>Cons.</td><td>vs Cons.</td></tr><tr><td>Revenues</td><td>29,291</td><td>30,591</td><td>27,892</td><td>5%</td><td>-4%</td><td>29,435</td><td>-0.5%</td></tr><tr><td>Gross profit</td><td>19,697</td><td>21,217</td><td>18,052</td><td>9%</td><td>-7%</td><td>19,706</td><td>0%</td></tr><tr><td>Gross margin</td><td>67.2%</td><td>69.4%</td><td>64.7%</td><td>2.5ppt</td><td>-2.1ppt</td><td>66.9%</td><td>0.3ppt</td></tr><tr><td>Operating profit</td><td>10,841</td><td>12,657</td><td>9,061</td><td>20%</td><td>-14%</td><td>10,628</td><td>2%</td></tr><tr><td>Operating margin</td><td>37.0%</td><td>41.4%</td><td>32.5%</td><td>4.5ppt</td><td>-4.4ppt</td><td>36.1%</td><td>0.9ppt</td></tr><tr><td>Non-GAAP op</td><td>11,431</td><td>13,273</td><td>10,007</td>

[中间内容因长度限制已省略]

SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public

offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
