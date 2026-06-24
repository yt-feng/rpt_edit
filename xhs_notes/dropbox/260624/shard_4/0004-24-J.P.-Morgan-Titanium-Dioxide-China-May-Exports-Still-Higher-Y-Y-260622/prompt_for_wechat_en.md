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
## Titanium Dioxide

## China May Exports Still Higher Y/Y

\- China exported 152.8kt of TiO2 in May, or $13\%$ more tons versus 135.6kt last year. Notably, China's exports of chloride-based TiO2 were higher by $39\%$ compared to last year, year to date. Sulfate-based shipments in May were higher by $7\%$ y/y at 118.4kt versus 110.7kt, though lower sequentially. Net exports in 2026 YTD were 857.2kt, or higher by 107kt or $\sim 14\%$ y/y.

\- Exports to EU-27 were 17.5kt in May compared to 20.3kt in April and 15.5kt in May of 2025; YTD exports to EU-27 are higher by $29\%$ at 97kt vs 75kt in the same period last year. Exports to the EU totaled 169kt in 2025, accounting for about $9\%$ of Chinese TiO2 exports. Exports to India rose from 126kt to 166kt year to date or by $32\%$ .

\- The May average export price of \$2,218/t was 8.8% higher sequentially and 7.0% y/y. The average export price per ton in April 2026 was \$2,038/t, and prices averaged \$2,072/t in May of last year. Import prices were (8.3%) lower sequentially at \$2,958/t vs. \$3,225/t in April and (11.1%) lower versus \$3,329/t in the prior-year period. Please see Table 9 for more details.

Chemicals: Specialty, Commodity, Agricultural, and Paper & Packaging

Jeffrey J. Zekauskas AC (1-212) 622-6644 jeffrey.zekauskas@JPM.com

Katie Zhang (1-212) 622-3262 katie.zhang@jpmchase.com

Silke Kueck (1-212) 622-6503 silke.x.kueck@JPM.com

Lydia Huang  
(1-212) 622-0086  
lydia.huang@JPM.com  
JPM Securities LLC

Table 1: China Total TiO2 Export Data (in kt)

<table><tr><td>Exports</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>48.2</td><td>52.0</td><td>59.3</td><td>69.1</td><td>69.9</td><td>102.9</td><td>106.7</td><td>141.4</td><td>131.6</td><td>159.7</td><td>158.5</td><td>183.8</td></tr><tr><td>February</td><td>42.1</td><td>44.7</td><td>52.1</td><td>70.1</td><td>64.6</td><td>71.2</td><td>94.4</td><td>101.4</td><td>154.2</td><td>133.6</td><td>157.5</td><td>151.5</td></tr><tr><td>March</td><td>46.9</td><td>61.0</td><td>68.7</td><td>103.6</td><td>98.1</td><td>157.1</td><td>126.9</td><td>145.0</td><td>151.3</td><td>196.0</td><td>185.0</td><td>201.5</td></tr><tr><td>April</td><td>43.6</td><td>55.7</td><td>64.8</td><td>87.0</td><td>77.0</td><td>88.1</td><td>107.2</td><td>118.6</td><td>128.9</td><td>157.4</td><td>148.0</td><td>193.5</td></tr><tr><td>May</td><td>47.3</td><td>71.2</td><td>72.8</td><td>79.9</td><td>88.5</td><td>66.5</td><td>104.8</td><td>115.7</td><td>144.8</td><td>149.3</td><td>135.6</td><td>152.8</td></tr><tr><td>June</td><td>44.2</td><td>63.9</td><td>78.5</td><td>83.0</td><td>83.6</td><td>77.3</td><td>100.5</td><td>124.4</td><td>125.6</td><td>176.4</td><td>131.9</td><td></td></tr><tr><td>July</td><td>46.5</td><td>63.6</td><td>68.8</td><td>70.2</td><td>88.6</td><td>97.5</td><td>87.5</td><td>125.8</td><td>135.9</td><td>159.6</td><td>134.7</td><td></td></tr><tr><td>August</td><td>38.4</td><td>65.4</td><td>71.2</td><td>75.7</td><td>87.3</td><td>117.1</td><td>102.6</td><td>104.1</td><td>137.5</td><td>160.7</td><td>138.7</td><td></td></tr><tr><td>September</td><td>40.4</td><td>63.1</td><td>62.4</td><td>74.0</td><td>83.8</td><td>111.8</td><td>108.0</td><td>96.3</td><td>145.0</td><td>146.8</td><td>156.3</td><td></td></tr><tr><td>October</td><td>45.5</td><td>54.6</td><td>67.6</td><td>63.0</td><td>79.4</td><td>110.2</td><td>115.8</td><td>99.1</td><td>118.8</td><td>154.3</td><td>146.4</td><td></td></tr><tr><td>November</td><td>39.7</td><td>63.2</td><td>76.3</td><td>70.0</td><td>81.9</td><td>112.3</td><td>123.6</td><td>107.2</td><td>124.9</td><td>149.3</td><td>152.2</td><td></td></tr><tr><td>December</td><td>55.6</td><td>62.0</td><td>88.1</td><td>62.4</td><td>100.7</td><td>102.0</td><td>133.7</td><td>127.0</td><td>143.3</td><td>158.4</td><td>171.8</td><td></td></tr><tr><td>Total YTD</td><td>538.4</td><td>720.5</td><td>830.9</td><td>908.0</td><td>1003.4</td><td>1214.1</td><td>1311.6</td><td>1405.9</td><td>1641.8</td><td>1901.5</td><td>1816.9</td><td>883.1</td></tr><tr><td>% change</td><td>(3%)</td><td>34%</td><td>15%</td><td>9%</td><td>11%</td><td>21%</td><td>8%</td><td>7%</td><td>17%</td><td>16%</td><td>(4%)</td><td>13%</td></tr></table>

Source: China General Administration of Customs. Note: Data in the table do not precisely match calculations due to rounding.

Table 2: China Total TiO2 Import Data (in kt)

<table><tr><td>Imports</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>13.7</td><td>13.5</td><td>17.9</td><td>20.1</td><td>12.4</td><td>7.5</td><td>15.9</td><td>12.0</td><td>3.6</td><td>6.6</td><td>7.3</td><td>6.1</td></tr><tr><td>February</td><td>13.4</td><td>13.0</td><td>18.6</td><td>8.6</td><td>8.4</td><td>17.7</td><td>14.5</td><td>12.0</td><td>4.8</td><td>7.2</td><td>5.2</td><td>3.5</td></tr><tr><td>March</td><td>14.3</td><td>13.7</td><td>17.6</td><td>17.0</td><td>11.6</td><td>12.2</td><td>16.2</td><td>12.9</td><td>4.7</td><td>10.5</td><td>8.3</td><td>5.9</td></tr><tr><td>April</td><td>20.3</td><td>13.1</td><td>18.7</td><td>19.1</td><td>13.2</td><td>12.3</td><td>18.7</td><td>15.4</td><td>5.5</td><td>6.8</td><td>6.5</td><td>5.1</td></tr><tr><td>May</td><td>19.4</td><td>15.9</td><td>20.4</td><td>18.3</td><td>13.7</td><td>14.0</td><td>15.8</td><td>15.0</td><td>6.4</td><td>9.2</td><td>7.5</td><td>5.3</td></tr><tr><td>June</td><td>18.3</td><td>19.3</td><td>21.3</td><td>17.6</td><td>15.9</td><td>13.9</td><td>16.3</td><td>12.7</td><td>7.1</td><td>7.5</td><td>4.9</td><td></td></tr><tr><td>July</td><td>22.1</td><td>19.9</td><td>17.9</td><td>17.4</td><td>15.1</td><td>14.6</td><td>17.5</td><td>11.1</td><td>8.0</td><td>9.1</td><td>7.3</td><td></td></tr><tr><td>August</td><td>19.0</td><td>13.2</td><td>17.0</td><td>15.9</td><td>15.2</td><td>12.3</td><td>15.1</td><td>12.4</td><td>9.2</td><td>6.4</td><td>3.4</td><td></td></tr><tr><td>September</td><td>21.1</td><td>14.8</td><td>15.6</td><td>15.9</td><td>11.2</td><td>14.6</td><td>17.0</td><td>3.9</td><td>6.8</td><td>8.3</td><td>6.4</td><td></td></tr><tr><td>October</td><td>12.7</td><td>13.0</td><td>18.7</td><td>16.5</td><td>18.2</td><td>16.6</td><td>12.2</td><td>3.3</td><td>7.8</td><td>6.4</td><td>5.6</td><td></td></tr><tr><td>November</td><td>16.0</td><td>18.5</td><td>16.6</td><td>18.2</td><td>14.8</td><td>16.1</td><td>17.0</td><td>5.7</td><td>9.3</td><td>6.7</td><td>5.3</td><td></td></tr><tr><td>December</td><td>13.5</td><td>21.3</td><td>14.6</td><td>12.8</td><td>17.1</td><td>16.5</td><td>15.8</td><td>6.9</td><td>11.2</td><td>7.3</td><td>6.7</td><td></td></tr><tr><td>Total YTD</td><td>203.7</td><td>189.3</td><td>215.0</td><td>197.5</td><td>166.9</td><td>168.2</td><td>191.9</td><td>123.1</td><td>84.5</td><td>92.0</td><td>74.5</td><td>25.9</td></tr><tr><td>% change</td><td>(6%)</td><td>(7%)</td><td>14%</td><td>(8%)</td><td>(16%)</td><td>1%</td><td>14%</td><td>(36%)</td><td>(31%)</td><td>9%</td><td>(19%)</td><td>(26%)</td></tr></table>

Source: China General Administration of Customs.  
Note: Data in the table do not precisely match calculations due to rounding.

Table 3: China Total TiO2 Annual Trade Data (in kt)

<table><tr><td></td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>Net exports/(imports)</td><td>337</td><td>334.8</td><td>531.2</td><td>615.9</td><td>710.5</td><td>836.5</td><td>1045.8</td><td>1119.7</td><td>1282.8</td><td>1557.3</td><td>1809.5</td><td>1742.4</td><td>857.2</td></tr><tr><td>Net change</td><td>127</td><td>(2.1)</td><td>196.4</td><td>84.7</td><td>94.6</td><td>126.0</td><td>209.3</td><td>73.9</td><td>163.1</td><td>274.5</td><td>252.2</td><td>(67.1)</td><td>107.4</td></tr><tr><td>% change</td><td>60.2%</td><td>(0.6%)</td><td>58.7%</td><td>16.0%</td><td>15.4%</td><td>17.7%</td><td>25.0%</td><td>7.1%</td><td>14.6%</td><td>21.4%</td><td>16.2%</td><td>(3.7%)</td><td>14.3%</td></tr></table>

Source: China General Administration of Customs.

Table 4: China TiO2 Exports by Destination 2026 vs 2025 '000s of tons

<table><tr><td colspan="3">2026TD</td></tr><tr><td>Export Destination</td><td>Volume (in kt)</td><td>% of total</td></tr><tr><td>India</td><td>166</td><td>19%</td></tr><tr><td>EU-27</td><td>97</td><td>11%</td></tr><tr><td>Turkey</td><td>58</td><td>7%</td></tr><tr><td>Indonesia</td><td>50</td><td>6%</td></tr><tr><td>Vietnam</td><td>48</td><td>5%</td></tr><tr><td>Republic of Korea</td><td>46</td><td>5%</td></tr><tr><td>Malaysia</td><td>32</td><td>4%</td></tr><tr><td>Thailand</td><td>31</td><td>4%</td></tr><tr><td>Russia</td><td>28</td><td>3%</td></tr><tr><td>United Arab Emirates</td><td>25</td><td>3%</td></tr><tr><td>Other</td><td>302</td><td>34%</td></tr><tr><td>Total</td><td>883</td><td></td></tr></table>

<table><tr><td colspan="3">2025TD</td></tr><tr><td>Export Destination</td><td>Volume (in kt)</td><td>% of total</td></tr><tr><td>India</td><td>126</td><td>14%</td></tr><tr><td>EU-27</td><td>75</td><td>9%</td></tr><tr><td>Turkey</td><td>54</td><td>6%</td></tr><tr><td>Republic of Korea</td><td>41</td><td>5%</td></tr><tr><td>Vietnam</td><td>35</td><td>4%</td></tr><tr><td>Brazil</td><td>35</td><td>4%</td></tr><tr><td>Indonesia</td><td>35</td><td>4%</td></tr><tr><td>United Arab Emirates</td><td>33</td><td>4%</td></tr><tr><td>Thailand</td><td>29</td><td>3%</td></tr><tr><td>Egypt</td><td>27</td><td>3%</td></tr><tr><td>Other</td><td>294</td><td>33%</td></tr><tr><td>Total</td><td>785</td><td></td></tr></table>

Source: China General Administration of Customs.

Table 5: China TiO2 Exports by Destination 2025 vs 2024

<table><tr><td colspan="3">2025</td></tr><tr><td>Export Destination</td><td>Volume (in kt)</td><td>% of total</td></tr><tr><td>India</td><td>257</td><td>14%</td></tr><tr><td>EU-27</td><td>169</td><td>9%</td></tr><tr><td>Turkey</td><td>120</td><td>7%</td></tr><tr><td>Vietnam</td><td>103</td><td>6%</td></tr><tr><td>S.Korea</td><td>93</td><td>5%</td></tr><tr><td>Indonesia</td><td>83</td><td>5%</td></tr><tr><td>UAE</td><td>74</td><td>4%</td></tr><tr><td>Brazil</td><td>70</td><td>4%</td></tr><tr><td>Thailand</td><td>64</td><td>4%</td></tr><tr><td>Egypt</td><td>62</td><td>3%</td></tr><tr><td>Other</td><td>721</td><td>40%</td></tr><tr><td>Total</td><td>1,817</td><td></td></tr></table>

Source: China General Administration of Customs.

<table><tr><td colspan="3">2024</td></tr><tr><td>Export Destination</td><td>Volume (in kt)</td><td>% of total</td></tr><tr><td>India</td><td>308</td><td>16%</td></tr><tr><td>EU-27</td><td>244</td><td>13%</td></tr><tr><td>Brazil</td><td>137</td><td>7%</td></tr><tr><td>S.Korea</td><td>97</td><td>5%</td></tr><tr><td>Turkey</td><td>97</td><td>5%</td></tr><tr><td>Vietnam</td><td>93</td><td>5%</td></tr><tr><td>Indonesia</td><td>81</td><td>4%</td></tr><tr><td>UAE</td><td>77</td><td>4%</td></tr><tr><td>Russia</td><td>75</td><td>4%</td></tr><tr><td>Belgium</td><td>61</td><td>3%</td></tr><tr><td>Other</td><td>327</td><td>22%</td></tr><tr><td>Total</td><td>1,902</td><td></td></tr></table>

Table 6: China Chloride TiO2 Export/Import Data (in kt)

<table><tr><td>Exports</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>27.1</td><td>28.7</td><td>45.4</td></tr><tr><td>February</td><td>26.9</td><td>29.8</td><td>39.4</td></tr><tr><td>March</td><td>44.7</td><td>39.1</td><td>51.0</td></tr><tr><td>April</td><td>32.2</td><td>30.4</td><td>42.8</td></tr><tr><td>May</td><td>23.0</td><td>24.9</td><td>34.4</td></tr><tr><td>June</td><td>29.5</td><td>24.4</td><td></td></tr><tr><td>July</td><td>25.5</td><td>24.5</td><td></td></tr><tr><td>August</td><td>26.4</td><td>25.0</td><td></td></tr><tr><td>September</td><td>27.0</td><td>28.8</td><td></td></tr><tr><td>October</td><td>26.5</td><td>32.3</td><td></td></tr><tr><td>November</td><td>29.9</td><td>34.5</td><td></td></tr><tr><td>December</td><td>27.7</td><td>44.2</td><td></td></tr><tr><td>Total YTD</td><td>346.4</td><td>366.5</td><td>212.9</td></tr><tr><td>% change</td><td></td><td>6%</td><td>39%</td></tr></table>

Note: Data in the table do not precisely match calculations due to rounding. Source: China General Administration of Customs.

<table><tr><td>Imports</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>4.5</td><td>4.6</td><td>4.1</td></tr><tr><td>February</td><td>5.9</td><td>2.7</td><td>2.3</td></tr><tr><td>March</td><td>8.1</td><td>4.6</td><td>3.8</td></tr><tr><td>April</td><td>3.8</td><td>3.8</td><td>2.6</td></tr><tr><td>May</td><td>6.9</td><td>4.2</td><td>2.8</td></tr><tr><td>June</td><td>4.6</td><td>3.5</td><td></td></tr><tr><td>July</td><td>6.0</td><td>5.3</td><td></td></tr><tr><td>August</td><td>3.8</td><td>1.9</td><td></td></tr><tr><td>September</td><td>4.6</td><td>3.5</td><td></td></tr><tr><td>October</td><td>4.4</td><td>2.8</td><td></td></tr><tr><td>November</td><td>3.7</td><td>3.8</td><td></td></tr><tr><td>December</td><td>4.2</td><td>3.5</td><td></td></tr><tr><td>Total YTD</td><td>60.5</td><td>44.3</td><td>15.6</td></tr><tr><td>% change</td><td></td><td>(27%)</td><td>(22%)</td></tr></table>

Table 7: China Sulfate TiO2 Export/Import Data (in kt)

<table><tr><td>Exports</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>133.2</td><td>129.8</td><td>138.4</td></tr><tr><td>February</td><td>106.7</td><td>127.7</td><td>112.1</td></tr><tr><td>March</td><td>151.4</td><td>145.9</td><td>150.6</td></tr><tr><td>April</td><td>125.2</td><td>117.6</td><td>150.7</td></tr><tr><td>May</td><td>126.3</td><td>110.7</td><td>118.4</td></tr><tr><td>June</td><td>146.9</td><td>107.5</td><td></td></tr><tr><td>July</td><td>134.2</td><td>110.2</td><td></td></tr><tr><td>August</td><td>134.2</td><td>113.7</td><td></td></tr><tr><td>September</td><td>119.7</td><td>127.6</td><td></td></tr><tr><td>October</td><td>127.8</td><td>114.2</td><td></td></tr><tr><td>November</td><td>119.3</td><td>117.7</td><td></td></tr><tr><td>December</td><td>130.7</td><td>127.7</td><td></td></tr><tr><td>Total YTD</td><td>1555.7</td><td>1450.3</td><td>670.1</td></tr><tr><td>% change</td><td></td><td>(7%)</td><td>6%</td></tr></table>

Note: Data in the table do not precisely match calculations due to rounding. Source: China General Administration of Customs.

<table><tr><td>Imports</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>2.1</td><td>2.7</td><td>2.0</td></tr><tr><td>February</td><td>1.3</td><td>2.5</td><td>1.2</td></tr><tr><td>March</td><td>2.4</td><td>3.7</td><td>2.2</td></tr><tr><td>April</td><td>3.0</td><td>2.7</td><td>2.5</td></tr><tr><td>May</td><td>2.3</td><td>3.2</td><td>2.4</td></tr><tr><td>June</td><td>3.0</td><td>1.4</td><td></td></tr><tr><td>July</td><td>3.1</td><td>2.0</td><td></td></tr><tr><td>August</td><td>2.6</td><td>1.6</td><td></td></tr><tr><td>September</td><td>3.7</td><td>2.9</td><td></td></tr><tr><td>October</td><td>2.0</td><td>2.8</td><td></td></tr><tr><td>November</td><td>3.0</td><td>1.5</td><td></td></tr><tr><td>December</td><td>3.0</td><td>3.1</td><td></td></tr><tr><td>Total YTD</td><td>31.5</td><td>30.2</td><td>10.3</td></tr><tr><td>% change</td><td></td><td>(4%)</td><td>(30%)</td></tr></table>

Table 8: Chinese Monthly Total TiO2 Exports to EU-27

<table><tr><td></td><td>Volume (in kt)</td><td>Price ($/ton)</td></tr><tr><td>Jan-24</td><td>32.3</td><td>2,099</td></tr><tr><td>Feb-24</td><td>28.7</td><td>2,123</td></tr><tr><td>Mar-24</td><td>32.1</td><td>2,215</td></tr><tr><td>Apr-24</td><td>33.6</td><td>2,242</td></tr><tr><td>May-24</td><td>24.3</td><td>2,250</td></tr><tr><td>Jun-24</td><td>16.8</td><td>2,216</td></tr><tr><td>Jul-24</td><td>7.5</td><td>2,160</td></tr><tr><td>Aug-24</td><td>18.5</td><td>2,132</td></tr><tr><td>Sep-24</td><td>11.0</td><td>2,221</td></tr><tr><td>Oct-24</td><td>16.8</td><td>2,206</td></tr><tr><td>Nov-24</td><td>10.5</td><td>2,107</td></tr><tr><td>Dec-24</td><td>11.6</td><td>2,102</td></tr><tr><td>Jan-25</td><td>12.4</td><td>2,050</td></tr><tr><td>Feb-25</td><td>14.5</td><td>2,051</td></tr><tr><td>Mar-25</td><td>16.8</td><td>2,080</td></tr><tr><td>Apr-25</td><td>16.2</td><td>2,133</td></tr><tr><td>May-25</td><td>15.5</td><td>2,186</td></tr><tr><td>Jun-25</td><td>16.2</td><td>2,165</td></tr><tr><td>Jul-25</td><td>11.2</td><td>2,121</td></tr><tr><td>Aug-25</td><td>10.7</td><td>2,024</td></tr><tr><td>Sep-25</td><td>10.6</td><td>1,952</td></tr><tr><td>Oct-25</td><td>15.5</td><td>1,952</td></tr><tr><td>Nov-25</td><td>13.6</td><td>1,943</td></tr><tr><td>Dec-25</td><td>16.3</td><td>1,934</td></tr><tr><td>Jan-26</td><td>16.4</td><td>1,945</td></tr><tr><td>Feb-26</td><td>18.9</td><td>1,999</td></tr><tr><td>Mar-26</td><td>23.9</td><td>2,094</td></tr><tr><td>Apr-26</td><td>20.3</td><td>2,272</td></tr><tr><td>May-26</td><td>17.5</td><td>2,431</td></tr></table>

Source: China General Administration of Customs, JPM estimates

Table 9: Chinese Total TiO2 Export/Import Prices

<table><tr><td></td><td>import price $/mt</td><td>Sq. % change</td><td>Y/y % change</td><td>export price $/mt</td><td>Sq. % change</td><td>Y/y % change</td></tr><tr><td>Feb-20</td><td>2,873</td><td>-1.4%</td><td>-6.7%</td><td>2,037</td><td>0.0%</td><td>-9.4%</td></tr><tr><td>Mar-20</td><td>2,914</td><td>0.0%</td><td>-1.3%</td><td>2,047</td><td>0.5%</td><td>-9.7%</td></tr><tr><td>Apr-20</td><td>2,926</td><td>0.4%</td><td>-3.0%</td><td>2,060</td><td>0.6%</td><td>-10.0%</td></tr><tr><td>May-20</td><td>2,817</td><td>-3.7%</td><td>-4.1%</td><td>2,031</td><td>-1.4%</td><td>-11.2%</td></tr><tr><td>Jun-20</td><td>2,847</td><td>1.0%</td><td>-6.0%</td><td>1,919</td><td>-5.5%</td><td>-15.3%</td></tr><tr><td>Jul-20</td><td>2,918</td><td>2.5%</td><td>-2.7%</td><td>1,821</td><td>-5.1%</td><td>-17.1%</td></tr><tr><td>Aug-20</td><td>2,887</td><td>-1.0%</td><td>-5.1%</td><td>1,787</td><td>-1.9%</td><td>-17.0%</td></tr><tr><td>Sep-20</td><td>2,745</td><td>-4.9%</td><td>-11.8%</td><td>1,785</td><td>-0.1%</td><td>-16.0%</td></tr><tr><td>Oct-20</td><td>2,701</td><td>-1.6%</td><td>-6.9%</td><td>1,817</td><td>1.8%</td><td>-14.2%</td></tr><tr><td>Nov-20</td><td>2,808</td><td>3.9%</td><td>-3.7%</td><td>1,911</td><td>5.2%</td><td>-9.1%</td></tr><tr><td>Dec-20</td><td>2,856</td><td>1.7%</td><td>0.2%</td><td>2,019</td><td>5.6%</td><td>-2.8%</td></tr><tr><td>Jan-21</td><td>2,838</td><td>-0.6%</td><td>-2.6%</td><td>2,200</td><td>9.0%</td><td>8.0%</td></tr><tr><td>Feb-21</td><td>2,881</td><td>1.5%</td><td>0.3%</td><td>2,357</td><td>7.1%</td><td>15.7%</td></tr><tr><td>Mar-21</td><td>2,978</td><td>3.4%</td><td>2.2%</td><td

[中间内容因长度限制已省略]

in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Morgan any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 22 Jun 2026 04:10 PM EDT

Disseminated 22 Jun 2026 04:10 PM EDT
"""
