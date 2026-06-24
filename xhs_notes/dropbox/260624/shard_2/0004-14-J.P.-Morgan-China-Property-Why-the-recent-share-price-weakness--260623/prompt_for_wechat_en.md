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
# JPM

## China Property

## Why the recent share price weakness?

Over the past 4 trading days, China Property has underperformed the HSI by $9\%$ . While high-frequency data (after adjustments as last week's data was disrupted by public holidays) maintains a similar trend vs. the past few months, we believe the share price weakness has mostly been driven by (1) negative read-through from weakening consumption data; (2) the sector's higher-beta nature amid the broader market sell-off; (3) a lack of near-term catalysts especially when high-frequency data is, while intact, not turning significantly better; (4) some investors may have focused on the weaker M/M secondary sales volume; however, in our view, this not an accurate way to gauge the market well-being due to seasonality (March & April typically see stronger sales), and thus Y/Y would be more reasonable. Even for leading SOEs like CRL & COLI, while their share prices had been relatively resilient throughout May & the first half of June (Figure 7), they both abruptly corrected $11\%$ (HSI: $-2\%$ ) over the past 2 trading days. We believe this was due to profit-taking amid broader market weakness as both stocks remain outperformers year-to-date. In fact, even after the correction, year-to-date, CRL $(+15\%) / \text{COLI} (+7\%)$ are still outperforming the HSI $(-7\%)$ (Figure 6). However, as data in tier-1 cities continues to show stabilization, on dips we'd selectively buy SOE developers with (1) outperforming sales growth; (2) strong exposure to tier-1 cities (COLI, CRL & Jinmao), but we remain cautious on most non-SOE developers (e.g. Vanke, Sunac) who may not benefit from the K-shaped stabilization.

## A quick look at the latest high-frequency data

\- Iceberg Index real-time secondary data (冰山指数实时二手成交): As of 21 June, 9-city (excluding Shanghai as data is not yet available as of the time of writing) real-time weekly secondary sales marginally rose $1\%$ Y/Y (down from $+12\%$ Y/Y). However, the drop is mainly due to the Dragonboat Festival. If we compare last week's data to the week last year with the Dragonboat Festival, the Y/Y growth would be $+15\%$ Y/Y, which is similar to the range $(10 - 20\%$ Y/Y) in previous weeks.

\- Iceberg Index tier-1 city secondary listings (冰山指数二手挂牌量): Likely under-appreciated by the market, the volume of secondary listings in tier-1 cities has been consistently coming down (dropped $2.5\%$ from the peak in March), and this is a key factor that will support continual secondary home price stabilization.

\- Sales registrations (official data with lag of a few weeks): The 60-city primary weekly sales registrations (一手网签) fell $23\%$ Y/Y, mostly due to the inclusion of the 3-day Dragon Boat Festival (during public holidays, sales registrations are significantly lower than usual). Compared to the same 3-day Dragon Boat Festival period in 2025, sales registrations were up $60\%$ Y/Y (but the sample size is too small, so we do not think this alone is representative). Similarly, the 12-city secondary sales registrations (二手网签) fell $13\%$ Y/Y (for a similar reason), reversing the positive Y/Y growth for the past 9 weeks. We expect both the primary & secondary sales registrations to see solid W/W

Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC (852) 2800-8513 karl.chan@JPM.com

Jocelyn Gao (852) 2800-8529 jocelyn.gao@JPM.com

(852) 2800-8599

venus.choi@JPM.com

JPM Securities (Asia Pacific) Limited/JPM Broking (Hong Kong) Limited

improvement due to the quarter-end-loaded nature of sales registrations, but we believe Y/Y growth is a more accurate way to assess market trend.

\- Home price stabilization in tier-1 cities has continued into May: According to the NBS home price index, tier-1 cities continued to register positive M/M growth (+0.2% in primary; +0.3% in secondary) in May (the $3^{rd}$ consecutive month). For the Centraline tier-1 secondary home price index, although the M/M growth slowed from +0.6% in April to +0.3% in May, this was the $4^{th}$ consecutive month of positive M/M growth. For more discussion, please see our earlier report with commentary on the latest NBS data.

## Iceberg Index – real time data

Figure 1: Iceberg Index - 10-city real time secondary daily sales since April 2026 (冰山指数实时二手成交)  
![](images/0a0bab2195a638ad5bb6df97b95af5881e1579e1572e1c739c95740dec8500e9.jpg)  
Source: Iceberg Index, JPM  
Note: The data for the last week is excluded as Shanghai data is not yet available. Please check our "Property Data Monitor" report for subsequent updates.

Figure 2: Iceberg Index - tier-1 cities' secondary listing volume (冰山指数二手挂牌量)  
No. of secondary listings ('000 units) - Tier 1 cities  
![](images/5271c35f7b5ec1219c86ddc7f2352935ed3b4d67c2ec86c9bd563f3efa0762e6.jpg)  
Source: Iceberg Index, JPM

## Official sales registrations (lag of a few weeks)

Figure 3: 60-city weekly primary sales registrations (一手网签) – compared with 2019-25  
![](images/240ae6a1af05cfcc1d2f77be2617707ab57419d000a9449e024284b75945fcb3.jpg)  
Source: CREIS  
Note: The steeper Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holidays).

Figure 4: 60-city weekly primary sales registrations (一手网签)  
![](images/7682170656aa19cf460030520e7dcf98f4521db303291f7bd81657a2080032cd.jpg)  
Source: CREIS  
Note: The Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holidays).

Table 1: 12-city primary sales registrations (一手网签) (comparing first 3 days of Dragon Boat Festival only)

<table><tr><td colspan="3">Primary - First 3 days of Dragon Boat Festival</td></tr><tr><td>Year</td><td>No. of units sold</td><td>2026 vs.</td></tr><tr><td>2020</td><td>17,067</td><td>-67%</td></tr><tr><td>2021</td><td>8,490</td><td>-34%</td></tr><tr><td>2022</td><td>5,319</td><td>6%</td></tr><tr><td>2023</td><td>5,535</td><td>2%</td></tr><tr><td>2024</td><td>3,919</td><td>44%</td></tr><tr><td>2025</td><td>3,519</td><td>60%</td></tr><tr><td>2026</td><td>5,628</td><td></td></tr></table>

Source: CREIS  
Note: As the sample size is small, the Y/Y growth may not necessarily be representative.

Figure 5: 8-city secondary sales registrations (二手网签)  
![](images/83c284fa3f7c4432ef2bb90aca1b18048b256e72f3c24521751bc398cadf7af8.jpg)  
Source: CREIS  
Note: The Y/Y decline in the last week is due to the inclusion of Dragon Boat Festival (sales registrations are typically significantly lower than usual during public holidays).

## Home price trend

Table 2: Monthly home price index in tier-1 cities

<table><tr><td></td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td colspan="14">Primary (NBS)</td></tr><tr><td>Beijing</td><td>-0.4%</td><td>-0.3%</td><td>0.0%</td><td>-0.4%</td><td>0.2%</td><td>-0.1%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.0%</td><td>-0.2%</td><td>-0.2%</td></tr><tr><td>Shanghai</td><td>0.7%</td><td>0.4%</td><td>0.3%</td><td>0.4%</td><td>0.3%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td><td>0.0%</td><td>0.2%</td><td>0.3%</td><td>0.4%</td><td>0.2%</td></tr><tr><td>Guangzhou</td><td>-0.8%</td><td>-0.5%</td><td>-0.3%</td><td>-0.2%</td><td>-0.6%</td><td>-0.8%</td><td>-0.5%</td><td>-0.6%</td><td>-0.6%</td><td>0.0%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td></tr><tr><td>Shenzhen</td><td>-0.4%</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>-1.0%</td><td>-0.7%</td><td>-0.9%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.1%</td><td>0.4%</td></tr><tr><td>Tier-1 Primary (NBS)</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.3%</td><td>-0.3%</td><td>-0.5%</td><td>-0.3%</td><td>-0.3%</td><td>0.0%</td><td>0.2%</td><td>0.1%</td><td>0.2%</td></tr><tr><td colspan="14">Secondary (NBS)</td></tr><tr><td>Beijing</td><td>-0.8%</td><td>-1.0%</td><td>-1.1%</td><td>-1.2%</td><td>-0.9%</td><td>-1.1%</td><td>-1.3%</td><td>-1.3%</td><td>-0.2%</td><td>0.3%</td><td>0.6%</td><td>0.4%</td><td>0.1%</td></tr><tr><td>Shanghai</td><td>-0.7%</td><td>-0.7%</td><td>-0.9%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.6%</td><td>-0.4%</td><td>0.2%</td><td>0.4%</td><td>0.7%</td><td>0.6%</td></tr><tr><td>Guangzhou</td><td>-0.8%</td><td>-0.7%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.9%</td><td>-1.2%</td><td>-1.0%</td><td>-0.7%</td><td>-0.5%</td><td>0.2%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>Shenzhen</td><td>-0.5%</td><td>-0.5%</td><td>-0.9%</td><td>-0.8%</td><td>-1.0%</td><td>-0.9%</td><td>-1.0%</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>0.4%</td><td>0.3%</td><td>0.6%</td></tr><tr><td>Tier-1 Secondary (NBS)</td><td>-0.7%</td><td>-0.7%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.9%</td><td>-1.1%</td><td>-0.9%</td><td>-0.5%</td><td>-0.1%</td><td>0.4%</td><td>0.4%</td><td>0.3%</td></tr><tr><td colspan="14">Secondary (Centaline)</td></tr><tr><td>Beijing</td><td>-0.9%</td><td>-1.6%</td><td>-1.5%</td><td>-1.8%</td><td>-2.1%</td><td>-1.9%</td><td>-1.9%</td><td>-1.9%</td><td>-0.5%</td><td>1.2%</td><td>1.5%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>Shanghai</td><td>-1.4%</td><td>-1.4%</td><td>-1.7%</td><td>-1.7%</td><td>-1.5%</td><td>-2.2%</td><td>-2.0%</td><td>-2.8%</td><td>-0.5%</td><td>0.9%</td><td>1.0%</td><td>1.6%</td><td>0.9%</td></tr><tr><td>Guangzhou</td><td>-1.0%</td><td>-1.4%</td><td>-1.2%</td><td>-1.8%</td><td>-1.4%</td><td>-2.0%</td><td>-1.9%</td><td>-1.3%</td><td>-0.8%</td><td>-1.5%</td><td>0.8%</td><td>-0.3%</td><td>-0.2%</td></tr><tr><td>Shenzhen</td><td>-1.1%</td><td>-0.5%</td><td>-1.1%</td><td>-1.0%</td><td>-1.5%</td><td>-0.5%</td><td>-1.0%</td><td>-1.6%</td><td>-1.3%</td><td>0.9%</td><td>0.1%</td><td>1.0%</td><td>0.1%</td></tr><tr><td>Tier-1 Secondary (Centaline)</td><td>-1.1%</td><td>-1.2%</td><td>-1.4%</td><td>-1.6%</td><td>-1.6%</td><td>-1.6%</td><td>-1.7%</td><td>-1.9%</td><td>-0.8%</td><td>0.4%</td><td>0.9%</td><td>0.6%</td><td>0.3%</td></tr></table>

Source: NBS, Centraline

Sector share price performance

Figure 6: China property – year-to-date share price performance by stock

![](images/01aae231d85b523f2bd65f456046924e5b0e8e1c88f3bf766b617c1115227035.jpg)  
Source: Bloomberg Finance L.P. as of 22 June 2026, JPM

Figure 7: MSCI China Real Estate Index vs. HSI, year-to-date  
![](images/4a81120f9d91c6d31b7fd6922d79f4d86e730a416bc8dd74899f9c9abd29333a.jpg)  
Source: Bloomberg Finance L.P. as of 22 June 2026, JPM  
Note: normalized to 100 as of 5 January 2026

## Valuation Summary

Table 3: China property – valuation summary

<table><tr><td rowspan="2">Company</td><td rowspan="2">Stock Code</td><td rowspan="2">JPM Rating</td><td rowspan="2">Last Close (HK$)</td><td rowspan="2">Market Cap US$M</td><td rowspan="2">ADV US$M</td><td colspan="2">P/E</td><td colspan="2">Dvd Yield</td><td colspan="2">P/B</td><td colspan="4">Share price return</td></tr><tr><td>1FY (x)</td><td>2FY (x)</td><td>1FY (%)</td><td>2FY (%)</td><td>1FY (x)</td><td>2FY (x)</td><td>5D</td><td>YTD</td><td>1Y</td><td>vs. AT high</td></tr><tr><td colspan="16">Mainland China Developers</td></tr><tr><td>China Resources Land</td><td>1109.HK</td><td>OW</td><td>31.18</td><td>28,362</td><td>110.2</td><td>9.0</td><td>8.9</td><td>4.1%</td><td>4.2%</td><td>0.6</td><td>0.6</td><td>-14%</td><td>18%</td><td>22%</td><td>-25%</td></tr><tr><td>China Overseas Land</td><td>0688.HK</td><td>OW</td><td>13.13</td><td>18,331</td><td>64.6</td><td>10.4</td><td>9.4</td><td>3.5%</td><td>3.9%</td><td>0.3</td><td>0.3</td><td>-16%</td><td>7%</td><td>2%</td><td>-60%</td></tr><tr><td>China Jinmao</td><td>0817.HK</td><td>OW</td><td>1.35</td><td>2,327</td><td>10.8</td><td>21.1</td><td>16.8</td><td>2.6%</td><td>2.7%</td><td>0.4</td><td>0.4</td><td>-16%</td><td>12%</td><td>25%</td><td>-79%</td></tr><tr><td>C&amp;D International</td><td>1908.HK</td><td>NC</td><td>12.96</td><td>3,703</td><td>14.6</td><td>6.9</td><td>6.3</td><td>7.7%</td><td>8.6%</td><td>0.7</td><td>0.7</td><td>-16%</td><td>-12%</td><td>-15%</td><td>-53%</td></tr><tr><td>Greentown China</td><td>3900.HK</td><td>NC</td><td>6.97</td><td>2,258</td><td>13.1</td><td>32.7</td><td>16.4</td><td>2.2%</td><td>4.8%</td><td>0.4</td><td>0.4</td><td>-17%</td><td>-18%</td><td>-23%</td><td>-65%</td></tr><tr><td>Yuexiu Property</td><td>123.HK</td><td>NC</td><td>3.71</td><td>1,905</td><td>6.1</td><td>33.7</td><td>17.6</td><td>2.6%</td><td>4.5%</td><td>0.2</td><td>0.2</td><td>-17%</td><td>-6%</td><td>-8%</td><td>-81%</td></tr><tr><td>Poly Property</td><td>119.HK</td><td>NC</td><td>1.66</td><td>809</td><td>5.0</td><td>22.7</td><td>10.5</td><td>1.7%</td><td>5.7%</td><td>0.2</td><td>0.2</td><td>-13%</td><td>-16%</td><td>20%</td><td>-87%</td></tr><tr><td colspan="5">SOEs</td><td>76.9</td><td>11.7</td><td>9.8</td><td>3.9%</td><td>4.4%</td><td>0.5</td><td>0.5</td><td>-15%</td><td>10%</td><td>10%</td><td>-44%</td></tr><tr><td>Longfor</td><td>0960.HK</td><td>OW</td><td>6.60</td><td>5,975</td><td>21.6</td><td>-</td><td>-</td><td>0.0%</td><td>1.1%</td><td>0.2</td><td>0.2</td><td>-25%</td><td>-22%</td><td>-27%</td><td>-88%</td></tr><tr><td>Seazen Group</td><td>1030.HK</td><td>N</td><td>1.45</td><td>1,344</td><td>6.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.2</td><td>0.2</td><td>-13%</td><td>-29%</td><td>-37%</td><td>-87%</td></tr><tr><td colspan="5">POEs</td><td>18.7</td><td>-</td><td>-</td><td>0.0%</td><td>0.9%</td><td>0.2</td><td>0.2</td><td>-22%</td><td>-24%</td><td>-29%</td><td>-88%</td></tr><tr><td>China Vanke - H</td><td>2202.HK</td><td>UW</td><td>2.47</td><td>5,158</td><td>8.7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.3</td><td>0.3</td><td>-6%</td><td>-25%</td><td>-47%</td><td>-94%</td></tr><tr><td>Country Garden</td><td>2007.HK</td><td>UW</td><td>0.19</td><td>1,146</td><td>12.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-8%</td><td>-53%</td><td>-50%</td><td>-99%</td></tr><tr><td>Sunac China</td><td>1918.HK</td><td>UW</td><td>0.72</td><td>1,567</td><td>21.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.4</td><td>0.8</td><td>-14%</td><td>-45%</td><td>-50%</td><td>-99%</td></tr><tr><td>Shimao</td><td>0813.HK</td><td>UW</td><td>0.08</td><td>99</td><td>0.5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-8%</td><td>-59%</td><td>-89%</td><td>-100%</td></tr><tr><td>Agile</td><td>3383.HK</td><td>NC</td><td>0.16</td><td>106</td><td>0.1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-17%</td><td>-39%</td><td>-57%</td><td>-99%</td></tr><tr><td>Logan</td><td>3380.HK</td><td>NC</td><td>1.44</td><td>1,044</td><td>3.1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-6%</td><td>-20%</td><td>78%</td><td>-91%</td></tr><tr><td>CIFI</td><td>884.HK</td><td>NC</td><td>0.05</td><td>104</td><td>0.7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-12%</td><td>-72%</td><td>-81%</td><td>-99%</td></tr><tr><td>R&amp;F</td><td>2777.HK</td><td>NC</td><td>0.24</td><td>114</td><td>0.3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-13%</td><td>-53%</td><td>-75%</td><td>-99%</td></tr><tr><td colspan="5">Distressed</td><td>10.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.2</td><td>0.3</td><td>-8%</td><td>-32%</td><td>-35%</td><td>-95%</td></tr><tr><td colspan="6">Mainland China Developers (Overall HK Listed)</td><td>9.1</td><td>7.6</td><td>3.1%</td><td>3.5%</td><td>0.4</td><td>0.4</td><td>-15%</td><td>1%</td><td>1%</td><td>-55%</td></tr><tr><td colspan="16"></td></tr><tr><td colspan="16">Mainland China Property Management</td></tr><tr><td>China Resources Mixc</td><td>1209.HK</td><td>OW</td><td>38.48</td><td>11,204</td><td>21.6</td><td>17.3</td><td>15.6</td><td>5.8%</td><td>6.4%</td><td>4.9</td><td>4.8</td><td>-10%</td><td>-8%</td><td>7%</td><td>-30%</td></tr><tr><td>China Overseas PH</td><td>2669.HK</td><td>UW</td><td>3.44</td><td>1,441</td><td>4.9</td><td>7.3</td><td>7.5</td><td>6.2%</td><td>6.2%</td><td>1.5</td><td>1.3</td><td>-13%</td><td>-24%</td><td>-33%</td><td>-69%</td></tr><tr><td>Poly Property Services</td><td>6049.HK</td><td>OW</td><td>27.22</td><td>1,921</td><td>4.0</td><td>8.0</td><td>7.6</td><td>6.2%</td><td>6.6%</td><td>1.1</td><td>1.1</td><td>-11%</td><td>-10%</td><td>-10%</td><td>-71%</td></tr><tr><td>Greentown Service</td><td>2869.HK</td><td>OW</td><td>4.18</td><td>1,670</td><td>2.2</td><td>10.7</td><td>10.0</td><td>6.7%</td><td>7.2%</td><td>1.3</td><td>1.3</td><td>-13%</td><td>-11%</td><td>-1%</td><td>-70%</td></tr><tr><td colspan="5">Backed by SOE developers</td><td>16.0</td><td>14.6</td><td>13.4</td><td>6.0%</td><td>6.5%</td><td>3.8</td><td>3.7</td><td>-11%</td><td>-10%</td><td>1%</td><td>-43%</td></tr><tr><td>Country Garden Services</td><td>6098.HK</td><td>N</td><td>5.25</td><td>2,182</td><td>5.5</td><td>6.0</td><td>5.9</td><td>10.1%</td><td>10.2%</td><td>0.4</td><td>0.4</td><td>-5%</td><td>-4%</td><td>-10%</td><td>-94%</td></tr><tr><td>A-Living</td><td>3319.HK</td><td>UW</td><td>1.84</td><td>333</td><td>0.8</td><td>3.0</td><td>3.4</td><td>3.6%</td><td>3.2%</td><td>0.2</td><td>0.2</td><td>-14%</td><td>-17%</td><td>-32%</td><td>-96%</td></tr><tr><td>Sunac Services</td><td>1516.HK</td><td>UW</td><td>0.78</td><td>301</td><td>1.4</td><td>4.4</td><td>5.2</td><td>6.8%</td><td>4.2%</td><td>0.4</td><td>0.4</td><td>-10%</td><td>-44%</td><td>-53%</td><td>-97%</td></tr><tr><td colspan="5">Backed by POE developers</td><td>4.5</td><td>5.4</td><td>5.5</td><td>9.0%</td><td>8.7%</td><td>0.4</td><td>0.4</td><td>-7%</td><td>-10%</td><td>-17%</td><td>-94%</td></tr><tr><td colspan="5">Property Management (Overall)</td><td>14.3</td><td>13.3</td><td>12.2</td><td>6.4%</td><td>6.8%</td><td>3.3</td><td>3.2</td><td>-10%</td><td>-10%</td><td>-2%</td><td>-50%</td></tr></table>

Source: Company data, Bloomberg Finance L.P. as of Jun 22, 2026, JPM estimates.  
Note: Companies marked with "NC" are not covered by JPM; all such estimates are based on Bloomberg consensus estimates.

Companies Discussed in This Report (all prices in this report as of market close on 22 June 2026, unless otherwise indicated)

China Jinmao (0817)(0817.HK/HK\$1.35/OW), China Overseas Land & Investment (0688)(0688.HK/HK\$13.13/OW), China Resources Land (1109)(1109.HK/HK\$31.18/OW), China Vanke - H(2202.HK/HK\$2.47/UW), SUNAC China(1918.HK/HK\$0.72/UW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are p

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
