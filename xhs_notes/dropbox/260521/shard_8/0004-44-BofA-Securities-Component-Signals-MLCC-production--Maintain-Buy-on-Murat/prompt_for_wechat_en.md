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
# MLCC production: Maintain Buy on Murata and TDK on solid earnings support

Price Objective Change

# Impact of front-loaded orders became evident in Jan-Mar

According to METI statistics, domestic ceramic capacitor (MLCC) production value in March 2026 declined $9\%$ YoY and increased $14\%$ MoM. While orders for AI servers continue to expand, front-loaded orders likely persisted in the IT equipment market, reflecting concerns over future price increases and material shortages. As a result, product mix rather deteriorated. The overall ASP in March declined $23\%$ YoY, marking a significant decline for three consecutive months. Meanwhile, production volume increased $18\%$ YoY and $12\%$ MoM, which we believe contributed to higher utilization rates at each company.

# S/D balance to improve on rising high-end demand

Given that the BB ratio of major MLCC makers exceeded 1.3 in Jan-Mar 2026, production value from Apr to Jun onward is highly likely to improve. We think a reactionary decline from front-loaded orders, mainly for the IT equipment market, could occur. However, production volume of small, high-capacitance and high-voltage products for AI servers is increasing, and utilization rates are rising, particularly in front-end processes. With tightening supply demand balance, price trends should also stabilize.

# Maintain Buy on Murata Mfg and TDK

Among the three domestic MLCC makers, we maintain Buy on Murata Mfg (6981) and TDK (6762). Through mix improvement and stabilization in MLCC ASP, we expect Murata Mfg profitability to show steady improvement. For TDK, in addition to solid battery performance and expansion in HDD-related components, MLCC and inductor demand for AI servers should expand from 2H onward.

# Taiyo Yuden share price reflects excessive expectations

For Taiyo Yuden (6976), we raise our earnings forecasts in line with expanding MLCC orders as shown in Exhibit 6, and raise our price objective (PO) from ¥3,250 to ¥3,800. However, we reiterate our Underperform rating. The reasons are (1) we believe excessive expectations for MLCC price increases are reflected in the share price, as domestic MLCC makers deny price hikes based solely on supply/demand, and (2) Taiyo Yuden's MLCC operating profit (OP) margin remains in the single digits owing to weak productivity. Our new PO implies significant downside from the current share price, but given the company's current profitability, we judge this to be an appropriate level.

# 19 May 2026

Equity

Japan

Electronics

Masashi Kubota >>

Research Analyst

BofAS Japan

+81 3 6225 7138

masashi.kubota@bofa.com

Hazel Xue >>

Research Analyst

BofAS Japan

hazel.xue@bofa.com

Exhibit 1: Maintain Buy on Murata/TDK   
PO of MLCC makers 

<table><tr><td rowspan="2"></td><td colspan="2">Price Objective</td><td>Last</td></tr><tr><td>Old</td><td>New</td><td>May 19 ¥</td></tr><tr><td rowspan="2">TDK(6762)</td><td colspan="2">Buy (C-1-7)</td><td></td></tr><tr><td>3,500 →</td><td>3,500</td><td>2,985.5</td></tr><tr><td>ADR: TTDKY</td><td>22.58 →</td><td>22.58</td><td>19.11</td></tr><tr><td rowspan="2">Murata(6981)</td><td colspan="2">Buy (B-1-7)</td><td></td></tr><tr><td>6,200 →</td><td>6,200</td><td>6,171</td></tr><tr><td rowspan="2">Taiyo Yuden(6976)</td><td colspan="2">U/P (C-3-7)</td><td></td></tr><tr><td>3,250 ↗</td><td>3,800</td><td>7,194</td></tr></table>

Source: BofA Global Research   
Note: U/P = Underperform

BofA GLOBAL RESEARCH

ASP: Average Selling Price

BB ratio: Book-to-Bill Ratio

HDD: Hard Disk Drive

METI: Ministry of Economy, Trade and Industry

S/D: Supply/Demand

MLCC: Multi-layer Ceramic Capacitor

Exhibit 2: Production value in March 2026 declined $9\%$ YoY Japan MLCC production value and YoY growth   
![](images/678cac6c31fc83fce264bff7e0d1000924f63254e3695a7800cf35103f1db8ee.jpg)

<details>
<summary>bar_line</summary>

| Month | Production value (bn yen) | Production value YoY (%) |
|---|---|---|
| Mar-24 | 67 | 21 |
| May-24 | 65 | 18 |
| Jul-24 | 78 | 22 |
| Sep-24 | 68 | -3 |
| Nov-24 | 72 | 3 |
| Jan-25 | 65 | 5 |
| Mar-25 | 70 | -5 |
| May-25 | 65 | 9 |
| Jul-25 | 75 | -10 |
| Sep-25 | 60 | 10 |
| Nov-25 | 78 | 4 |
| Jan-26 | 58 | -15 |
| Mar-26 | 63 | -8 |
</details>

Source: METI, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 3: Product mix deteriorated due to front-loaded orders Japan MLCC production value, volume and ASP   
![](images/6251ff83d3af8c3e20b64d8eea787b69bc8abe1a6103d024afdb4a81529810f2.jpg)  
Source: METI, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 4: Production volumes continued to grow at a double-digit rate YoY Japan domestic ceramic capacitor production 

<table><tr><td></td><td>Volume (K units)</td><td>YoY</td><td>MoM</td><td>Value (mn yen)</td><td>YoY</td><td>MoM</td><td>Average price (yen)</td><td>YoY</td><td>MoM</td></tr><tr><td>Mar-23</td><td>66,015,902</td><td>-36.6%</td><td>19.2%</td><td>54,682</td><td>-17.2%</td><td>11.9%</td><td>0.83</td><td>30.6%</td><td>-6.1%</td></tr><tr><td>Apr-23</td><td>79,034,337</td><td>-26.2%</td><td>19.7%</td><td>61,342</td><td>-8.8%</td><td>12.2%</td><td>0.78</td><td>23.5%</td><td>-6.3%</td></tr><tr><td>May-23</td><td>73,302,223</td><td>-23.9%</td><td>-7.3%</td><td>55,121</td><td>-15.6%</td><td>-10.1%</td><td>0.75</td><td>10.8%</td><td>-3.1%</td></tr><tr><td>Jun-23</td><td>89,475,861</td><td>-0.4%</td><td>22.1%</td><td>63,479</td><td>-1.3%</td><td>15.2%</td><td>0.71</td><td>-0.9%</td><td>-5.7%</td></tr><tr><td>Jul-23</td><td>89,345,899</td><td>-7.9%</td><td>-0.1%</td><td>63,417</td><td>-5.0%</td><td>-0.1%</td><td>0.71</td><td>3.2%</td><td>0.0%</td></tr><tr><td>Aug-23</td><td>97,603,510</td><td>2.2%</td><td>9.2%</td><td>68,976</td><td>-0.3%</td><td>8.8%</td><td>0.71</td><td>-2.4%</td><td>-0.4%</td></tr><tr><td>Sep-23</td><td>104,649,030</td><td>5.9%</td><td>7.2%</td><td>69,048</td><td>-2.5%</td><td>0.1%</td><td>0.66</td><td>-8.0%</td><td>-6.6%</td></tr><tr><td>Oct-23</td><td>93,806,210</td><td>12.9%</td><td>-10.4%</td><td>69,981</td><td>7.2%</td><td>1.4%</td><td>0.75</td><td>-5.0%</td><td>13.1%</td></tr><tr><td>Nov-23</td><td>91,179,426</td><td>18.9%</td><td>-2.8%</td><td>66,639</td><td>11.7%</td><td>-4.8%</td><td>0.73</td><td>-6.0%</td><td>-2.0%</td></tr><tr><td>Dec-23</td><td>94,155,954</td><td>12.5%</td><td>3.3%</td><td>67,911</td><td>5.5%</td><td>1.9%</td><td>0.72</td><td>-6.3%</td><td>-1.3%</td></tr><tr><td>Jan-24</td><td>82,951,377</td><td>18.9%</td><td>-11.9%</td><td>63,083</td><td>18.3%</td><td>-7.1%</td><td>0.76</td><td>-0.5%</td><td>5.4%</td></tr><tr><td>Feb-24</td><td>79,361,175</td><td>43.2%</td><td>-4.3%</td><td>59,222</td><td>21.2%</td><td>-6.1%</td><td>0.75</td><td>-15.4%</td><td>-1.9%</td></tr><tr><td>Mar-24</td><td>89,103,904</td><td>35.0%</td><td>12.3%</td><td>66,383</td><td>21.4%</td><td>12.1%</td><td>0.75</td><td>-10.1%</td><td>-0.2%</td></tr><tr><td>Apr-24</td><td>95,933,302</td><td>21.4%</td><td>7.7%</td><td>74,662</td><td>21.7%</td><td>12.5%</td><td>0.78</td><td>0.3%</td><td>4.5%</td></tr><tr><td>May-24</td><td>82,009,859</td><td>11.9%</td><td>-14.5%</td><td>64,473</td><td>17.0%</td><td>-13.6%</td><td>0.79</td><td>4.5%</td><td>1.0%</td></tr><tr><td>Jun-24</td><td>82,678,033</td><td>-7.6%</td><td>0.8%</td><td>64,841</td><td>2.1%</td><td>0.6%</td><td>0.78</td><td>10.5%</td><td>-0.2%</td></tr><tr><td>Jul-24</td><td>99,894,095</td><td>11.8%</td><td>20.8%</td><td>77,261</td><td>21.8%</td><td>19.2%</td><td>0.77</td><td>9.0%</td><td>-1.4%</td></tr><tr><td>Aug-24</td><td>92,324,886</td><td>-5.4%</td><td>-7.6%</td><td>67,223</td><td>-2.5%</td><td>-13.0%</td><td>0.73</td><td>3.0%</td><td>-5.9%</td></tr><tr><td>Sep-24</td><td>100,074,749</td><td>-4.4%</td><td>8.4%</td><td>69,853</td><td>1.2%</td><td>3.9%</td><td>0.70</td><td>5.8%</td><td>-4.1%</td></tr><tr><td>Oct-24</td><td>90,642,911</td><td>-3.4%</td><td>-9.4%</td><td>72,213</td><td>3.2%</td><td>3.4%</td><td>0.80</td><td>6.8%</td><td>14.1%</td></tr><tr><td>Nov-24</td><td>88,365,306</td><td>-3.1%</td><td>-2.5%</td><td>68,271</td><td>2.4%</td><td>-5.5%</td><td>0.77</td><td>5.7%</td><td>-3.0%</td></tr><tr><td>Dec-24</td><td>94,341,682</td><td>0.2%</td><td>6.8%</td><td>71,916</td><td>5.9%</td><td>5.3%</td><td>0.76</td><td>5.7%</td><td>-1.3%</td></tr><tr><td>Jan-25</td><td>83,483,545</td><td>0.6%</td><td>-11.5%</td><td>64,265</td><td>1.9%</td><td>-10.6%</td><td>0.77</td><td>1.2%</td><td>1.0%</td></tr><tr><td>Feb-25</td><td>78,378,362</td><td>-1.2%</td><td>-6.1%</td><td>65,986</td><td>11.4%</td><td>2.7%</td><td>0.84</td><td>12.8%</td><td>9.4%</td></tr><tr><td>Mar-25</td><td>85,478,775</td><td>-4.1%</td><td>9.1%</td><td>69,276</td><td>4.4%</td><td>5.0%</td><td>0.81</td><td>8.8%</td><td>-3.7%</td></tr><tr><td>Apr-25</td><td>90,380,132</td><td>-5.8%</td><td>5.7%</td><td>71,674</td><td>-4.0%</td><td>3.5%</td><td>0.79</td><td>1.9%</td><td>-2.1%</td></tr><tr><td>May-25</td><td>78,214,941</td><td>-4.6%</td><td>-13.5%</td><td>64,817</td><td>0.5%</td><td>-9.6%</td><td>0.83</td><td>5.4%</td><td>4.5%</td></tr><tr><td>Jun-25</td><td>89,974,684</td><td>8.8%</td><td>15.0%</td><td>70,222</td><td>8.3%</td><td>8.3%</td><td>0.78</td><td>-0.5%</td><td>-5.8%</td></tr><tr><td>Jul-25</td><td>98,762,026</td><td>-1.1%</td><td>9.8%</td><td>74,698</td><td>-3.3%</td><td>6.4%</td><td>0.76</td><td>-2.2%</td><td>-3.1%</td></tr><tr><td>Aug-25</td><td>98,615,801</td><td>6.8%</td><td>-0.1%</td><td>60,557</td><td>-9.9%</td><td>-18.9%</td><td>0.61</td><td>-15.7%</td><td>-18.8%</td></tr><tr><td>Sep-25</td><td>104,232,201</td><td>4.2%</td><td>5.7%</td><td>76,915</td><td>10.1%</td><td>27.0%</td><td>0.74</td><td>5.7%</td><td>20.2%</td></tr><tr><td>Oct-25</td><td>94,735,172</td><td>4.5%</td><td>-9.1%</td><td>76,247</td><td>5.6%</td><td>-0.9%</td><td>0.80</td><td>1.0%</td><td>9.1%</td></tr><tr><td>Nov-25</td><td>81,351,726</td><td>-7.9%</td><td>-14.1%</td><td>71,276</td><td>4.4%</td><td>-6.5%</td><td>0.88</td><td>13.4%</td><td>8.9%</td></tr><tr><td>Dec-25</td><td>105,236,963</td><td>11.5%</td><td>29.4%</td><td>67,068</td><td>-6.7%</td><td>-5.9%</td><td>0.64</td><td>-16.4%</td><td>-27.3%</td></tr><tr><td>Jan-26</td><td>95,211,635</td><td>14.0%</td><td>-9.5%</td><td>58,039</td><td>-9.7%</td><td>-13.5%</td><td>0.61</td><td>-20.8%</td><td>-4.4%</td></tr><tr><td>Feb-26</td><td>90,094,255</td><td>14.9%</td><td>-5.4%</td><td>55,734</td><td>-15.5%</td><td>-4.0%</td><td>0.62</td><td>-26.5%</td><td>1.5%</td></tr><tr><td>Mar-26</td><td>101,116,355</td><td>18.3%</td><td>12.2%</td><td>63,248</td><td>-8.7%</td><td>13.5%</td><td>0.63</td><td>-22.8%</td><td>1.1%</td></tr></table>

Source: METI, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 5: TDK (6762) - Double-digit profit growth YoY driven by stable battery performance and expansion in HDD-related businesses   
Consolidated earnings estimates 

<table><tr><td></td><td>Sales (mn¥)</td><td>YoY (%)</td><td>OP (mn¥)</td><td>YoY (%)</td><td>PTP (mn¥)</td><td>YoY (%)</td><td>NP (mn¥)</td><td>YoY (%)</td><td>EPS (¥)</td><td>P/E (x)</td><td>P/CF (x)</td></tr><tr><td colspan="12">Quarterly</td></tr><tr><td>FY3/27 1Q BofA E</td><td>624,400</td><td>16.5</td><td>64,200</td><td>13.8</td><td>67,800</td><td>17.6</td><td>50,300</td><td>21.3</td><td>25.9</td><td>-</td><td>-</td></tr><tr><td>FY3/27 2Q BofA E</td><td>684,200</td><td>5.7</td><td>88,600</td><td>-2.9</td><td>92,200</td><td>2.6</td><td>68,600</td><td>-1.9</td><td>35.3</td><td>-</td><td>-</td></tr><tr><td>FY3/27 3Q BofA E</td><td>678,700</td><td>0.5</td><td>85,200</td><td>2.5</td><td>89,100</td><td>1.7</td><td>66,300</td><td>-5.0</td><td>34.1</td><td>-</td><td>-</td></tr><tr><td>FY3/27 4Q BofA E</td><td>648,700</td><td>0.4</td><td>63,700</td><td>52.5</td><td>67,700</td><td>61.8</td><td>50,300</td><td>245.5</td><td>25.9</td><td>-</td><td>-</td></tr><tr><td colspan="12">Full year</td></tr><tr><td>FY3/26 A</td><td>2,504,820</td><td>13.6</td><td>272,415</td><td>21.5</td><td>276,810</td><td>16.4</td><td>195,663</td><td>17.1</td><td>103.0</td><td>29.8</td><td>14.9</td></tr><tr><td>FY3/27 CoE</td><td>2,580,000</td><td>3.0</td><td>295,000</td><td>8.3</td><td>300,000</td><td>8.4</td><td>225,000</td><td>15.0</td><td>118.5</td><td>25.1</td><td>12.4</td></tr><tr><td>FY3/27 BofA E</td><td>2,635,500</td><td>5.2</td><td>301,700</td><td>10.8</td><td>316,800</td><td>14.4</td><td>235,500</td><td>20.4</td><td>121.2</td><td>24.6</td><td>12.2</td></tr><tr><td>FY3/27 Consensus E</td><td>2,624,127</td><td>4.8</td><td>301,238</td><td>10.6</td><td>311,194</td><td>12.4</td><td>229,367</td><td>17.2</td><td>118.0</td><td>25.2</td><td>12.5</td></tr><tr><td>FY3/28 BofA E</td><td>2,821,193</td><td>7.0</td><td>339,800</td><td>12.6</td><td>360,210</td><td>13.7</td><td>268,610</td><td>14.1</td><td>138.2</td><td>21.5</td><td>10.8</td></tr><tr><td>FY3/28 Consensus E</td><td>2,821,575</td><td>7.5</td><td>354,252</td><td>17.6</td><td>362,306</td><td>16.4</td><td>267,303</td><td>16.5</td><td>137.5</td><td>21.7</td><td>11.4</td></tr><tr><td>FY3/29 BofA E</td><td>2,994,593</td><td>6.1</td><td>382,200</td><td>12.5</td><td>404,951</td><td>12.4</td><td>302,151</td><td>12.5</td><td>155.4</td><td>19.2</td><td>9.9</td></tr><tr><td>FY3/29 Consensus E</td><td>2,990,009</td><td>6.0</td><td>398,040</td><td>12.4</td><td>407,476</td><td>12.5</td><td>300,469</td><td>12.4</td><td>154.6</td><td>19.3</td><td>10.7</td></tr></table>

Source: Company data, Visible Alpha, BofA Global Research estimates   
BofA GLOBAL RESEARCH

Exhibit 6: Murata Mfg (6981) - Component segment profitability to improve on stabilization in MLCC ASP   
Consolidated earnings estimates 

<table><tr><td></td><td>Sales (mn¥)</td><td>YoY (%)</td><td>OP (mn¥)</td><td>YoY (%)</td><td>PTP (mn¥)</td><td>YoY (%)</td><td>NP (mn¥)</td><td>YoY (%)</td><td>EPS (¥)</td><td>P/E (x)</td><td>P/CF (x)</td></tr><tr><td colspan="12">Quarterly</td></tr><tr><td>FY3/27 1Q BofA E</td><td>465,000</td><td>11.7</td><td>88,700</td><td>43.9</td><td>93,200</td><td>49.5</td><td>70,800</td><td>42.4</td><td>36.1</td><td>-</td><td>-</td></tr><tr><td>FY3/27 2Q BofA E</td><td>529,000</td><td>8.7</td><td>113,500</td><td>9.6</td><td>118,000</td><td>4.9</td><td>89,700</td><td>8.5</td><td>45.7</td><td>-</td><td>-</td></tr><tr><td>FY3/27 3Q BofA E</td><td>510,000</td><td>9.1</td><td>109,000</td><td>187.8</td><td>113,500</td><td>129.3</td><td>86,300</td><td>245.6</td><td>44.0</td><td>-</td><td>-</td></tr><tr><td>FY3/27 4Q BofA E</td><td>503,000</td><td>9.2</td><td>104,800</td><td>33.0</td><td>109,300</td><td>29.6</td><td>83,100</td><td>8.8</td><td>42.3</td><td>-</td><td>-</td></tr><tr><td colspan="12">Full year</td></tr><tr><td>FY3/26 A</td><td>1,830,856</td><td>5.0</td><td>281,835</td><td>0.8</td><td>308,643</td><td>1.4</td><td>233,920</td><td>0.0</td><td>127.7</td><td>40.3</td><td>24.9</td></tr><tr><td>FY3/27 CoE</td><td>1,960,000</td><td>7.1</td><td>380,000</td><td>34.8</td><td>390,000</td><td>26.4</td><td>293,000</td><td>25.3</td><td>161.0</td><td>38.3</td><td>26.1</td></tr><tr><td>FY3/27 BofA E</td><td>2,007,000</td><td>9.6</td><td>416,000</td><td>47.6</td><td>434,000</td><td>40.6</td><td>329,900</td><td>41.0</td><td>168.1</td><td>36.7</td><td>23.8</td></tr><tr><td>FY3/27 Consensus E</td><td>1,994,091</td><td>8.9</td><td>412,604</td><td>46.4</td><td>429,999</td><td>39.3</td><td>324,654</td><td>38.8</td><td>165.4</td><td>37.3</td><td>23.5</td></tr><tr><td>FY3/28 BofA E</td><td>2,250,100</td><td>12.1</td><td>511,000</td><td>22.8</td><td>527,200</td><td>21.5</td><td>400,700</td><td>21.5</td><td>204.1</td><td>30.2</td><td>20.4</td></tr><tr><td>FY3/28 Consensus E</td><td>2,295,104</td><td>15.1</td><td>547,849</td><td>32.8</td><td>565,632</td><td>31.5</td><td>426,925</td><td>31.5</td><td>217.5</td><td>28.4</td><td>19.0</td></tr><tr><td>FY3/29 BofA E</td><td>2,510,600</td><td>11.6</td><td>608,700</td><td>19.1</td><td>626,700</td><td>18.9</td><td>476,300</td><td>18.9</td><td>242.6</td><td>25.4</td><td>17.7</td></tr><tr><td>FY3/28 Consensus E</td><td>2,519,979</td><td>9.8</td><td>610,950</td><td>11.5</td><td>629,783</td><td>11.3</td><td>475,225</td><td>11.3</td><td>242.1</td><td>25.5</td><td>17.5</td></tr></table>

Source: Company data, Visible Alpha, BofA Global Research estimates   
BofA GLOBAL RESEARCH

Exhibit 7: Taiyo Yuden (6976) - The gap between the current share price level and fundamentals is widening

Consolidated earnings estimates

<table><tr><td></td><td>Sales (mn¥)</td><td>YoY (%)</td><td>OP (mn¥)</td><td>YoY (%)</td><td>RP (mn¥)</td><td>YoY (%)</td><td>NP (mn¥)</td><td>YoY (%)</td><td>EPS (¥)</td><td>P/E (x)</td><td>P/CF (x)</td></tr><tr><td colspan="12">Quarterly</td></tr><tr><td>FY3/27 1Q BofA E</td><td>90,800</td><td>7.1</td><td>6,100</td><td>131.9</td><td>5,900</td><td>-29.6</td><td>4,000</td><td>-36.6</td><td>27.1</td><td>-</td><td>-</td></tr><tr><td>FY3/27 2Q BofA E</td><td>100,400</td><td>8.2</td><td>10,500</td><td>78.5</td><td>10,300</td><td>31.2</td><td>7,100</td><td>10.7</td><td>48.2</td><td>-</td><td>-</td></tr><tr><td>FY3/27 3Q BofA E</td><td>99,200</td><td>12.1</td><td>9,900</td><td>32.1</td><td>9,700</td><td>-17.1</td><td>6,700</td><td>-5.4</td><td>45.4</td><td>-</td><td>-</td></tr><tr><td>FY3/27 4Q BofA E</td><td>97,000</td><td>8.2</td><td>8,500</td><td>117.7</td><td>8,300</td><td>83.4</td><td>5,700</td><td>139.9</td><td>38.7</td><td>-</td><td>-</td></tr><tr><td colspan="12">Full year</td></tr><tr><td>FY3/26 A</td><td>355,341</td><td>4.1</td><td>19,996</td><td>91.2</td><td>24,129</td><td>129.4</td><td>14,806</td><td>536.0</td><td>107.6</td><td>66.9</td><td>19.4</td></tr><tr><td>FY3/27 CoE</td><td>384,000</td><td>8.1</td><td>30,000</td><td>50.0</td><td>27,000</td><td>11.9</td><td>18,000</td><td>21.6</td><td>143.9</td><td>50.0</td><td>16.1</td></tr><tr><td>FY3/27 BofA E (New)</td><td>387,400</td><td>9.0</td><td>34,900</td><td>74.5</td><td>34,100</td><td>41.3</td><td>23,400</td><td>58.0</td><td>158.7</td><td>45.3</td><td>14.8</td></tr><tr><td>FY3/27 BofA E (Old)</td><td>372,300</td><td>4.8</td><td>32,900</td><td>64.5</td><td>33,700</td><td>39.7</td><td>23,900</td><td>61.4</td><td>162.1</td><td>44.4</td><td>14.4</td></tr><tr><td>FY3/27 Consensus E</td><td>381,722</td><td>7.4</td><td>36,013</td><td>80.1</td><td>35,778</td><td>48.3</td><td>24,865</td><td>67.9</td><td>190.2</td><td>37.8</td><td>12.8</td></tr><tr><td>FY3/28 BofA E (New)</td><td>421,800</td><td>8.9</td><td>46,100</td><td>32.1</td><td>45,600</td><td>33.7</td><td>31,700</td><td>35.5</td><td>215.0</td><td>33.5</td><td>13.2</td></tr><tr><td>FY3/28 BofA E (Old)</td><td>396,300</td><td>6.4</td><td>39,800</td><td>21.0</td><td>40,800</td><td>21.1</td><td>29,700</td><td>24.3</td><td>201.5</td><td>35.7</td><td>13.1</td></tr><tr><td>FY3/28 Consensus E</td><td>418,254</td><td>9.6</td><td>52,468</td><td>45.7</td><td>53,257</td><td>48.9</td><td>37,72

[中间内容因长度限制已省略]

ions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
