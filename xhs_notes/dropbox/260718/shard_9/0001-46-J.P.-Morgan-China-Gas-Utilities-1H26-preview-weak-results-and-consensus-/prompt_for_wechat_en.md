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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## China Gas Utilities

## 1H26 preview - weak results and consensus earnings cuts are likely; turning point yet to come

We expect weak 1H26 results for China Gas utilities and the majority of the companies to report lower earnings yoy (Table 3) on the back of weak gas volumes, a decline in new connections and gas margins. We expect a round of earnings cuts post results; our FY26-27E earnings forecasts are \~7% below consensus. Despite YTD underperformance and undemanding valuations (\~6% yield on average), we believe a turning point for the sector is yet to come as winter gas prices may climb yoy, bringing uncertainty to winter gas margins. We remain selective on stocks and suggest to buy on dips post-results. Our top pick is ENN Energy, as the company offers >7% yield in FY26E with guaranteed DPS (HK\$3/share). We see room for a cut to growth capex and improving FCF, and we think management may consider a buyback/raising DPS amid the significant underperformance YTD, which is not factored in to the price.

\- 1H results likely to disappoint: We forecast most gas utilities to miss on 1H26 results (see Table 3) with \~4% decline in profits on average. HKCG is the only company for which we expect positive earnings growth on strong SAF profits amid elevated oil prices. We trim our earnings for 26-27E by \~5-6% on average (Table 4) and our forecasts are \~7% below consensus. We expect consensus earnings cuts post earnings.

\- Turning point yet to come: Despite a $>20\%$ share decline YTD (HSCEI $\sim 7\%$ ), we remain selective on stocks. This comes as the operating outlook remains challenging with weak gas volume growth ( $<1\%$ in 26E for our covered names), elevated gas prices and a continued decline in new connections. These factors aren't likely to change much during 2H26. Also, we see uncertainties around winter gas margins on the back of continued uncertainty in global gas supply and LNG procurement costs. Yet, we see value for names with attractive yield with upstream resources (which could better weather gas price volatility). These include ENN Energy ( $>7\%$ yield in 26E with LNG trading profits in 2H with its overseas contracts) and ENN Natural Gas ( $>6\%$ yield in 27E with $>3$ bcm of overseas LNG sales on JPMe).

\- Winter gas margin remains uncertain: Our global energy analyst forecasts winter gas prices to almost double yoy in 4Q26 with tight global LNG supply-demand balances and low European storage levels. Note that NWE+UK storage facilities were $41\%$ full as of July 12 (vs $56\%$ at the same time last year and the 2022-25 average of $70\%$ ) (note). This poses downside risks to winter gas margins in our view, as residential heating volume was low last year due to the warm winter. Some gas utilities may need to procure spot LNG to satisfy winter heating demand. We believe the sector is unlikely to re-rate positively until investors have more clarity on the gas price outlook.

China

Power Equipment and Utilities

Stephen Tsui, CFA AC

(852) 2800-8592

stephen.tsui@JPM.com

Vento Suen

(852) 2800-8546

vento.suen@JPM.com

Alan Hon

(852) 2800-8573

alan.hon@JPM.com

JPM Securities (Asia Pacific) Limited/JPM Broking (Hong Kong) Limited

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>China Resources Gas</td><td>1193 HK</td><td>4,593</td><td>HKD</td><td>15.56</td><td>N</td><td>n/c</td><td>16.50</td><td>Jun-27</td><td>18.50</td><td>Dec-26</td></tr><tr><td>ENN Energy</td><td>2688 HK</td><td>6,145</td><td>HKD</td><td>42.56</td><td>OW</td><td>n/c</td><td>57.00</td><td>Jun-27</td><td>68.00</td><td>Dec-26</td></tr><tr><td>ENN Natural Gas – A</td><td>600803 CH</td><td>7,457</td><td>CNY</td><td>16.30</td><td>OW</td><td>n/c</td><td>21.00</td><td>Jun-27</td><td>25.00</td><td>Dec-26</td></tr><tr><td>Kunlun Energy</td><td>135 HK</td><td>7,460</td><td>HKD</td><td>6.77</td><td>OW</td><td>n/c</td><td>7.60</td><td>Jun-27</td><td>8.50</td><td>Dec-26</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 16 Jul 26.

Table 1: China Gas Utilities – Valuation Comps

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">JPM Rating</td><td rowspan="2">JPM PT (Local)</td><td rowspan="2">Last price (Local)</td><td rowspan="2">Upside (%)</td><td rowspan="2">Mkt cap (US$mn)</td><td rowspan="2">Avg daily liquidity (US$mn)</td><td colspan="2">P/E (x)</td><td colspan="2">P/B (x)</td><td colspan="2">Yield (%)</td><td colspan="2">Net debt/equity (%)</td><td colspan="2">RoE (%)</td><td colspan="2">EV/EBITDA (x)</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td></tr><tr><td>HKCG</td><td>3 HK</td><td>N</td><td>7.3</td><td>6.7</td><td>9.1</td><td>15,924</td><td>21.6</td><td>20.9</td><td>20.3</td><td>2.1</td><td>2.1</td><td>5.2</td><td>5.2</td><td>75.7</td><td>76.2</td><td>11.9</td><td>12.4</td><td>15.4</td><td>15.1</td></tr><tr><td>Kunlun</td><td>135 HK</td><td>OW</td><td>7.6</td><td>6.8</td><td>12.3</td><td>7,459</td><td>11.4</td><td>9.4</td><td>9.0</td><td>0.7</td><td>0.7</td><td>5.4</td><td>5.5</td><td>(28)</td><td>(31)</td><td>7.8</td><td>7.8</td><td>3.4</td><td>3.3</td></tr><tr><td>China Gas*</td><td>384 HK</td><td>N</td><td>5.7</td><td>5.8</td><td>(1.0)</td><td>4,003</td><td>11.3</td><td>10.8</td><td>10.6</td><td>0.5</td><td>0.5</td><td>6.1</td><td>6.1</td><td>79</td><td>75</td><td>5.0</td><td>5.0</td><td>9.7</td><td>9.6</td></tr><tr><td>CR Gas</td><td>1193 HK</td><td>N</td><td>16.5</td><td>15.6</td><td>6.0</td><td>4,593</td><td>8.8</td><td>10.0</td><td>9.7</td><td>0.8</td><td>0.8</td><td>6.1</td><td>6.1</td><td>19</td><td>14</td><td>7.9</td><td>7.9</td><td>6.7</td><td>6.5</td></tr><tr><td>ENN Energy</td><td>2688 HK</td><td>OW</td><td>57.0</td><td>42.6</td><td>33.9</td><td>6,145</td><td>30.6</td><td>7.2</td><td>7.1</td><td>0.8</td><td>0.8</td><td>7.0</td><td>7.1</td><td>18</td><td>16</td><td>11.5</td><td>11.1</td><td>5.3</td><td>5.1</td></tr><tr><td>ENN Natural Gas</td><td>600803 CH</td><td>OW</td><td>21.0</td><td>16.3</td><td>28.8</td><td>7,455</td><td>26.4</td><td>9.7</td><td>8.0</td><td>1.9</td><td>1.7</td><td>5.9</td><td>6.3</td><td>18</td><td>12</td><td>20.2</td><td>22.2</td><td>7.0</td><td>6.1</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>11.3</td><td>10.8</td><td>1.1</td><td>1.1</td><td>6.0</td><td>6.0</td><td>30</td><td>27</td><td>10.7</td><td>11.1</td><td>7.9</td><td>7.6</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates. Priced as of 16 Jul 2026.

Table 2: JPM Commodities Research global natural gas price forecasts

<table><tr><td colspan="2"></td><td>2023</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>2026</td><td>1Q27</td><td>2Q27</td><td>3Q27</td><td>4Q27</td><td>2027</td></tr><tr><td rowspan="7">Forecast</td><td>TTF (EUR/MWh)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>55.00</td><td>60.00</td><td>51.68</td><td>60.00</td><td>40.00</td><td>40.00</td><td>45.00</td><td>46.25</td></tr><tr><td>NBP (GBp/Therm)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>135.00</td><td>150.00</td><td>128.62</td><td>150.00</td><td>97.00</td><td>97.00</td><td>113.00</td><td>114.25</td></tr><tr><td>HH ($/MMBtu)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3.60</td><td>4.15</td><td>3.92</td><td>4.00</td><td>3.45</td><td>3.60</td><td>3.85</td><td>3.73</td></tr><tr><td>JKM ($/MMBtu)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>18.90</td><td>20.60</td><td>17.57</td><td>20.60</td><td>14.40</td><td>14.40</td><td>15.60</td><td>16.25</td></tr><tr><td>TTF ($/MMBtu)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>18.40</td><td>20.10</td><td>17.41</td><td>20.10</td><td>13.40</td><td>13.40</td><td>15.10</td><td>15.50</td></tr><tr><td>NBP ($/MMBtu)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>18.10</td><td>20.10</td><td>17.27</td><td>20.10</td><td>13.00</td><td>13.00</td><td>15.10</td><td>15.30</td></tr><tr><td>TTF - JKM spread ($/MMBtu)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.50</td><td>-0.50</td><td>-0.16</td><td>-0.50</td><td>-1.00</td><td>-1.00</td><td>-0.50</td><td>-0.75</td></tr><tr><td rowspan="7">Actual / Futures curve</td><td>TTF (EUR/MWh)</td><td>41.47</td><td>34.64</td><td>46.78</td><td>35.60</td><td>32.97</td><td>30.09</td><td>36.36</td><td>40.03</td><td>45.67</td><td>44.37</td><td>43.93</td><td>43.50</td><td>42.15</td><td>33.49</td><td>32.22</td><td>31.97</td><td>34.96</td></tr><tr><td>NBP (GBp/Therm)</td><td>102.56</td><td>84.92</td><td>114.74</td><td>85.16</td><td>80.57</td><td>78.03</td><td>89.63</td><td>100.85</td><td>111.96</td><td>105.62</td><td>110.03</td><td>107.12</td><td>107.99</td><td>81.64</td><td>76.80</td><td>80.19</td><td>86.66</td></tr><tr><td>HH ($/MMBtu)</td><td>2.72</td><td>2.33</td><td>3.60</td><td>3.69</td><td>3.29</td><td>3.52</td><td>3.52</td><td>4.02</td><td>2.86</td><td>3.25</td><td>3.18</td><td>3.33</td><td>4.01</td><td>2.96</td><td>3.16</td><td>3.37</td><td>3.16</td></tr><tr><td>JKM ($/MMBtu)</td><td>14.47</td><td>11.89</td><td>14.03</td><td>12.37</td><td>11.84</td><td>10.85</td><td>12.27</td><td>13.21</td><td>17.60</td><td>16.07</td><td>15.43</td><td>15.58</td><td>14.56</td><td>11.66</td><td>11.56</td><td>11.60</td><td>11.61</td></tr><tr><td>TTF ($/MMBtu)</td><td>13.13</td><td>10.97</td><td>14.43</td><td>11.84</td><td>11.30</td><td>10.26</td><td>11.96</td><td>13.73</td><td>15.55</td><td>14.88</td><td>14.73</td><td>14.72</td><td>14.13</td><td>11.23</td><td>10.80</td><td>10.72</td><td>11.72</td></tr><tr><td>NBP ($/MMBtu)</td><td>12.74</td><td>10.84</td><td>14.10</td><td>11.28</td><td>11.00</td><td>10.61</td><td>11.74</td><td>13.61</td><td>15.01</td><td>14.14</td><td>14.73</td><td>14.37</td><td>14.46</td><td>10.93</td><td>10.28</td><td>10.74</td><td>11.60</td></tr><tr><td>TTF - JKM spread ($/MMBtu)</td><td>-1.34</td><td>-0.91</td><td>0.40</td><td>-0.53</td><td>-0.55</td><td>-0.58</td><td>-0.31</td><td>0.52</td><td>-2.05</td><td>-1.19</td><td>-0.70</td><td>-0.86</td><td>-0.42</td><td>-0.43</td><td>-0.76</td><td>-0.87</td><td>0.11</td></tr></table>

Source: Bloomberg Finance L.P., JPM Commodities Research.

## 1H26E earnings preview

Table 3: 1H26E earnings preview

<table><tr><td rowspan="2"></td><td colspan="3">Profit (RC mn)</td><td rowspan="2">Retail gas volume growth (%)</td><td rowspan="2">Dollar margin (Rmb/m3)</td><td rowspan="2">New connections (mn households)</td></tr><tr><td>1H25</td><td>1H26E</td><td>YoY%</td></tr><tr><td>CR Gas</td><td>2,403</td><td>2,383</td><td>-0.8%</td><td>0.2%</td><td>0.54</td><td>0.66</td></tr><tr><td>ENN Energy*</td><td>3,223</td><td>3,003</td><td>-6.8%</td><td>0.1%</td><td>0.53</td><td>0.55</td></tr><tr><td>ENN NG*</td><td>2,736</td><td>2,482</td><td>-9.3%</td><td></td><td></td><td></td></tr><tr><td>HKCG*</td><td>3,084</td><td>3,259</td><td>5.7%</td><td>0.3%</td><td>0.53</td><td>0.55</td></tr><tr><td>Kunlun</td><td>3,161</td><td>2,982</td><td>-5.6%</td><td>0.2%</td><td>0.43</td><td>0.35</td></tr></table>

Source: Companies' 1H25 results announcements/presentations, JPM estimates.\*Core profit is used, attributable profit for other companies. Note that ENN NG disclosed core profit in 1H25 and switched to "operating profit" since FY25. RC = Reporting Currency

ENN Energy: We forecast ENN Energy's 1H26 core earnings to drop by $\sim 7\%$ yoy to $\sim$ Rmb 3.0bn. We expect almost flattish retail gas volume and a slight decline in gas margin, while the company's earnings are likely to be dragged by lower new connections and a single-digit decline in integrated energy and value-added services businesses. Higher trading profits yoy from the LNG business could partly offset other operational weakness, however.

CR Gas: We forecast CR Gas's 1H26 earnings to drop by $\sim 1\%$ yoy to $\sim$ HK\$2.4bn due to a decline in new connections and lukewarm momentum for other segments (limited volume growth and margin expansion). This could be partly offset by CNY appreciation (as reporting currency for CR Gas is in HKD).

Kunlun: We forecast Kunlun's 1H26 earnings to drop by $\sim 6\%$ yoy to $\sim$ Rmb 3.0bn, as we expect flattish retail gas volumes yoy and a slight decline in gas margin, and lower utilization for the LNG terminals yoy.

ENN Natural Gas: We forecast ENN NG's 1H26 core operating profit to fall \~9% yoy to \~Rmb2.5bn, mainly due to weaker earnings from the city gas business (through ENN Energy) and the LNG terminal. That said, we expect the direct gas sales business to deliver a higher contribution, driven by elevated global gas prices and incremental earnings from the new LNG contract.

HKCG: We forecast HKCG's core earnings to grow by $\sim 6\%$ yoy in 1H26 to HK\$3.3bn. While we expect the mainland city gas business to be lukewarm (flattish volume growth, a slight decline in gas margin and a decline in new connections), these are likely to be more than offset by the strength in the biofuel associate on elevated oil prices.

## Earnings and PT changes

Table 4: Earnings and PT changes

<table><tr><td rowspan="2"></td><td colspan="3">Previous</td><td colspan="3">Current</td><td colspan="3">Change</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>CR Gas (HK$ mn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>103,877</td><td>107,466</td><td>109,827</td><td>103,437</td><td>104,170</td><td>106,179</td><td>-0.4%</td><td>-3.1%</td><td>-3.3%</td></tr><tr><td>Gross profit</td><td>17,781</td><td>18,493</td><td>18,870</td><td>17,420</td><td>17,522</td><td>17,727</td><td>-2.0%</td><td>-5.3%</td><td>-6.1%</td></tr><tr><td>Attributable profit</td><td>3,585</td><td>4,016</td><td>4,392</td><td>3,556</td><td>3,665</td><td>3,800</td><td>-0.8%</td><td>-8.7%</td><td>-13.5%</td></tr><tr><td>PT (HK$/sh)</td><td></td><td></td><td>18.5</td><td></td><td></td><td>16.5</td><td></td><td></td><td>-10.8%</td></tr><tr><td>Rating</td><td></td><td></td><td>N</td><td></td><td></td><td>N</td><td></td><td></td><td></td></tr><tr><td>ENN Energy (Rmb mn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>114,407</td><td>118,658</td><td>116,109</td><td>115,072</td><td>115,507</td><td>117,125</td><td>0.6%</td><td>-2.7%</td><td>0.9%</td></tr><tr><td>Gross profit</td><td>13,137</td><td>13,434</td><td>13,279</td><td>12,766</td><td>12,626</td><td>12,686</td><td>-2.8%</td><td>-6.0%</td><td>-4.5%</td></tr><tr><td>Attributable profit</td><td>6,001</td><td>6,163</td><td>6,305</td><td>5,679</td><td>5,761</td><td>5,781</td><td>-5.4%</td><td>-6.5%</td><td>-8.3%</td></tr><tr><td>PT (HK$/sh)</td><td></td><td></td><td>68.0</td><td></td><td></td><td>57.0</td><td></td><td></td><td>-16.2%</td></tr><tr><td>Rating</td><td></td><td></td><td>OW</td><td></td><td></td><td>OW</td><td></td><td></td><td></td></tr><tr><td>ENN NG (Rmb mn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>140,648</td><td>149,700</td><td>152,936</td><td>140,637</td><td>146,152</td><td>153,319</td><td>0.0%</td><td>-2.4%</td><td>0.3%</td></tr><tr><td>Gross profit</td><td>19,358</td><td>22,064</td><td>23,355</td><td>18,644</td><td>20,870</td><td>22,139</td><td>-3.7%</td><td>-5.4%</td><td>-5.2%</td></tr><tr><td>Attributable profit</td><td>5,337</td><td>6,624</td><td>7,259</td><td>5,197</td><td>6,313</td><td>6,962</td><td>-2.6%</td><td>-4.7%</td><td>-4.1%</td></tr><tr><td>PT (Rmb/sh)</td><td></td><td></td><td>25.0</td><td></td><td></td><td>21.0</td><td></td><td></td><td>-16.0%</td></tr><tr><td>Rating</td><td></td><td></td><td>OW</td><td></td><td></td><td>OW</td><td></td><td></td><td></td></tr><tr><td>Kunlun Energy (Rmb mn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>210,168</td><td>216,953</td><td>224,258</td><td>210,048</td><td>215,756</td><td>222,118</td><td>-0.1%</td><td>-0.6%</td><td>-1.0%</td></tr><tr><td>Gross profit</td><td>25,043</td><td>25,678</td><td>26,441</td><td>24,014</td><td>24,523</td><td>25,213</td><td>-4.1%</td><td>-4.5%</td><td>-4.6%</td></tr><tr><td>Attributable profit</td><td>5,788</td><td>5,961</td><td>6,185</td><td>5,391</td><td>5,596</td><td>5,808</td><td>-6.9%</td><td>-6.1%</td><td>-6.1%</td></tr><tr><td>PT (HK$/sh)</td><td></td><td></td><td>8.5</td><td></td><td></td><td>7.6</td><td></td><td></td><td>-10.6%</td></tr><tr><td>Rating</td><td></td><td></td><td>OW</td><td></td><td></td><td>OW</td><td></td><td></td><td></td></tr></table>

Source: JPM estimates.

ENN Energy: We trim our 26-28E earnings estimates by \~7% on average to reflect lower assumptions on gas margin/volume growth, and also revenue growth for the integrated energy/value-added services segments to reflect lukewarm macro momentum and elevated gas prices. We also lower our valuation multiple from \~10x to \~9x to reflect the execution issue highlighted by management on the proposed privatization (see note). We roll forward our PT from Dec-26 to Jun-27 and lower it from HK\$68 to HK\$57 to reflect the above-mentioned drivers. Maintain OW on valuation (\~7% yield).

CR Gas: We trim our 26-28E earnings estimates by \~8% on average to reflect lower assumptions on gas margin/volume growth to reflect lukewarm macro momentum and elevated gas prices. We roll forward our PT from Dec-26 to Jun-27 and lower it from HK\$18.5 to HK\$16.5 to reflect the above-mentioned drivers.

Kunlun: We trim our 26-28E earnings estimates by 6-7%

[中间内容因长度限制已省略]

erial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to

certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
