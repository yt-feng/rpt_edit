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
BofA GLOBAL RESEARCH

Global Memory Tech

# Weekly theme: Samsung correction, strong indicator, CXMT IPO, Nanya Tech upturn

Industry Overview

## Samsung share-price correction vs strong fundamentals

Many investors have asked why Samsung Electronics' share price corrected despite reporting (7 July) strong 2Q OP of W89.4tn. In our view, the bearish sentiment stemmed from following concerns: (1) Meta US – chip order cut; (2) CXMT China – large capacity; and (3) QoQ growth – no longer strong after 2Q peak. That said, we don't see any downturn signals – our weekly channel check still indicates strong memory chip demand (from US Big Tech), low impact of CXMT (no severe competition), and more favorable 3Q ASP (many new quarterly contracts already reveal 20%+ price hike, in our view). In fact, we have slightly raised 3Q DRAM ASP assumptions in our global memory industry model (new: +21% QoQ vs old +17%); see Exhibit 15 for our new forecast summary.

## Super-cycle reconfirmed by BofA memory indicator

Our memory indicator, which is based on YoY changes in spot price, global billings, Korea exports, etc., remained at a record-high level, with May results at 183 – far above 2017/2024 peaks (120-130; mid-cycle: 100; downturn: 80). DRAM/NAND global billings grew more than 300% YoY in May, according to our analysis using WSTS's data. We also note solid June sales (Nanya Tech: +621% YoY; Phison +301% YoY), exports (Korea semis: +199%) and DRAM spot (+700%; even NAND shows +600% despite MoM drop). One of the most interesting point in Jun results was resumption of DRAM spot rally MoM (+11% on average vs -4%/+3% in Apr/May) but this is weaker than Korea's semis exports (+21% MoM) that include more high-end memory (HBM4, SOCAMM, etc.) vs May level.

## CXMT's IPO share subscription date announced - 16 July

CXMT, China-based DRAM manufacturer, stated the firm's IPO share subscription date will be 16 July. Thus, actual listing can happen in late-July if the government regulations are properly followed. CXMT has disclosed its 2Q26 sales guidance (CNY59-69bn; \~US\$9.5bn). This is 7x YoY growth but still only high-single-digit% of global DRAM market share despite large wafer capacity (high-200k wpm or 300k, according to media reports; this accounts for mid-teen% of global total DRAM capacity). We still assume high-end DRAM (10Ghz+ LPDDR5, HBM, SOCAMM, GDDR7, etc.) will be supplied mostly by ex-China memory chipmakers due to quality and US's strict control (on China semis).

## Nanya Tech's legacy DRAM more profitable vs HBM

Nanya Tech reported very strong 2Q results (sales up 684% YoY; OP margin 74% vs large loss or -43% a year ago). The key contributor was DRAM ASP rise (up 60%+ QoQ; 500%+ YoY). Management's guidance was also bullish for 3Q and even for the long term (shortage of legacy DRAM such as DDR3 & 4 continues, low impact of China memory players' capacity expansion, etc). We also learned that Nanya Tech's DRAM business is more profitable than HBM. Since 2Q results were broadly in line with our already bullish forecasts, our EPS estimate changes (2026-28) are almost nil and, as such, PO (NT\$660; 9x 2027-28E P/E) is unchanged; maintain Buy on solid earnings and low multiples.

## 11 July 2026

Equity
Global
Technology

Simon Woo, CFA >> Research Analyst BofA (Seoul) +82 2 3707 0554 simon.woo@bofa.com

Dai Shen >>
Research Analyst
BofA (Hong Kong)
dai.shen@bofa.com

Vivek Arya
Research Analyst
BofAS
vivek.arya@bofa.com

Mikio Hirakawa >>
Research Analyst
BofAS Japan
mikio.hirakawa@bofa.com

Matt Shin >>
Research Analyst
BofA (Seoul)
matt.shin2@bofa.com

## Exhibit 1: Global memory outlook - supercycle likely to continue through 2027 despite 2026 quadrupling BofA global memory forecasts

<table><tr><td>YoY</td><td>24</td><td>25</td><td>26E</td><td>27E</td></tr><tr><td>DRAM sales</td><td>86%</td><td>52%</td><td>325%</td><td>45%</td></tr><tr><td>NAND sales</td><td>84%</td><td>4%</td><td>299%</td><td>30%</td></tr><tr><td>DRAM ASP</td><td>62%</td><td>29%</td><td>249%</td><td>25%</td></tr><tr><td>NAND ASP</td><td>65%</td><td>-8%</td><td>238%</td><td>9%</td></tr><tr><td>DRAM bit</td><td>15%</td><td>18%</td><td>22%</td><td>17%</td></tr><tr><td>NAND bit</td><td>11%</td><td>13%</td><td>18%</td><td>20%</td></tr><tr><td>DRAM capex</td><td>49%</td><td>43%</td><td>65%</td><td>27%</td></tr><tr><td>NAND capex</td><td>4%</td><td>-5%</td><td>55%</td><td>18%</td></tr><tr><td>DRAM capa</td><td>7%</td><td>8%</td><td>11%</td><td>9%</td></tr><tr><td>NAND capa</td><td>-2%</td><td>-7%</td><td>5%</td><td>4%</td></tr></table>

Source: BofA Global Research estimates
BofA GLOBAL RESEARCH

Exhibit 2: DDR5 and DDR4 price up in Jun/early-Jul, while NAND prices softened Spot-market prices among DRAM and NAND

<table><tr><td>US$</td><td>Current</td><td>WoW</td><td>QoQ</td><td>YoY</td></tr><tr><td colspan="5">DRAM spot</td></tr><tr><td>16Gb DDR5</td><td>47.8</td><td>2%</td><td>29%</td><td>688%</td></tr><tr><td>16Gb DDR4</td><td>77.6</td><td>2%</td><td>9%</td><td>825%</td></tr><tr><td>8Gb DDR4</td><td>37.8</td><td>3%</td><td>13%</td><td>661%</td></tr><tr><td colspan="5">NAND spot</td></tr><tr><td>1Tb wafer</td><td>24.2</td><td>-1%</td><td>-9%</td><td>377%</td></tr><tr><td>512Gb wafer</td><td>19.3</td><td>-3%</td><td>-11%</td><td>621%</td></tr><tr><td>256Gb wafer</td><td>10.2</td><td>0%</td><td>-7%</td><td>578%</td></tr></table>

Source: DRAMeXchange

Nanya Tech – Gross and OP margin trend

ASP-driven memory super-cycle to continue
Exhibit 3: New record-high in Jun (NT\$29.4bn; +6% MoM); more than 5x higher than 2025-avg (NT\$5.5bn)
Nanya Tech – Monthly sales (Jun 2026)  
![](images/d706ca355994ac258f001c6d6bc36fb1dfc21c1cb6f61b969b595021da73863b.jpg)  
Source: Company  
BofA GLOBAL RESEARCH

Exhibit 5: Exceptionally strong ASP hike in 2Q (up >60% QoQ) even after robust 1Q (up >70%); we assume decelerating growth in 2H, but still strong at 23%/8% in 3Q/4Q, respectively; no downturn in 2027 – just softening ASP QoQ (still super-cycle)
Nanya Tech DRAM ASP trend – quarterly; 8Gb equiv.  
![](images/b65c3dca24b4a93c5e33ff40badd5b02048bcfc1568431f13c181c211abaf7d0.jpg)  
Source: Company, BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 7: Also at all-time high in Jun (NT\$24.9bn; +9% MoM); more than 4x higher than 2025-avg (NT\$6.1bn)
Phison Electronics – Monthly sales (Jun 2026)  
![](images/4cbbb9a589cd509dc719d78d8101c468d4d85d23918de844a8d6ff26ac793e17.jpg)  
Exhibit 4: Robust YoY growth continued in Jun (+621%); already 11 consecutive months of triple-digit rebound
Nanya Tech – YoY monthly sales (Jun 2026)  
Source: Company

![](images/a7674349bb45d703917ffd638ae3e39718400701ea9b2486ea553234430a80cd.jpg)  
BofA GLOBAL RESEARCH  
Source: Company  
Source: Company, BofA Global Research estimates  
BofA GLOBAL RESEARCH

![](images/b95e9fa5adbc495156bf158a71864c87433a57fa112645c9c7dd075f55d590f5.jpg)  
BofA GLOBAL RESEARCH

Exhibit 6: We expect robust margins to continue in 2H26-27 (GM/OPM 70%+); record-high margins well-proved in 2Q (GM 79%, OPM 74%)  
Exhibit 8: Strong YoY growth continued in Jun (+621%); already six consecutive months of triple-digit rebound
Phison Electronics – YoY monthly sales (Jun 2026)  
![](images/a4eb4a5539f4e66d47104b6d56997d648a2a09297153dad260c164eb43bd383c.jpg)  
Source: Company  
BofA GLOBAL RESEARCH

Exhibit 9: Given 2Q results were broadly in-line with our already bullish forecasts, our EPS estimate changes (2026-28) are almost nil and consequently PO (NT\$660; 9x 2027-28E P/E) is unchanged; reiterate Buy on strong earnings and low multiples
Nanya Tech – Earnings revisions (2026-28E)

<table><tr><td>(NT$bn, NT$)</td><td>1Q26</td><td>2Q26</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EPS (FD)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>8.3</td><td>14.6</td><td>18.7</td><td>20.2</td><td>20.8</td><td>21.3</td><td>21.9</td><td>20.7</td><td>4.7</td><td>-2.4</td><td>-1.6</td><td>2.1</td><td>62.6</td><td>84.6</td><td>68.3</td></tr><tr><td>Old</td><td>8.3</td><td>14.7</td><td>19.0</td><td>20.5</td><td>20.9</td><td>21.3</td><td>21.8</td><td>20.6</td><td>4.7</td><td>-2.4</td><td>-1.6</td><td>2.1</td><td>62.6</td><td>84.7</td><td>68.0</td></tr><tr><td>Diff</td><td>n/a</td><td>-1%</td><td>-2%</td><td>-1%</td><td>-1%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Dividend/share</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>0.0</td><td>1.4</td><td>0.0</td><td>0.0</td><td>0.0</td><td>20.0</td><td>0.0</td><td>0.0</td><td>2.1</td><td>0.0</td><td>0.0</td><td>1.4</td><td>20.0</td><td>25.0</td><td>25.0</td></tr><tr><td>Old</td><td>0.0</td><td>1.4</td><td>0.0</td><td>0.0</td><td>0.0</td><td>20.0</td><td>0.0</td><td>0.0</td><td>2.1</td><td>0.0</td><td>0.0</td><td>1.4</td><td>20.0</td><td>25.0</td><td>25.0</td></tr><tr><td>Difference</td><td>n/a</td><td>nm</td><td>nm</td><td>nm</td><td>nm</td><td>nm</td><td>nm</td><td>nm</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Sales total</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>49.1</td><td>82.5</td><td>110.7</td><td>120.5</td><td>126.2</td><td>130.9</td><td>138.1</td><td>134.8</td><td>57.0</td><td>29.9</td><td>34.1</td><td>66.6</td><td>362.9</td><td>530.0</td><td>519.2</td></tr><tr><td>Old</td><td>49.1</td><td>82.2</td><td>102.6</td><td>111.6</td><td>116.8</td><td>121.1</td><td>127.8</td><td>124.8</td><td>57.0</td><td>29.9</td><td>34.1</td><td>66.6</td><td>345.5</td><td>490.5</td><td>480.5</td></tr><tr><td>Diff</td><td>n/a</td><td>0%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>5%</td><td>8%</td><td>8%</td></tr><tr><td>OP margin</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>61.3%</td><td>73.7%</td><td>76.7%</td><td>76.2%</td><td>74.9%</td><td>73.8%</td><td>72.0%</td><td>69.7%</td><td>19.3%</td><td>-48.4%</td><td>-30.9%</td><td>7.9%</td><td>73.8%</td><td>72.5%</td><td>59.8%</td></tr><tr><td>Old</td><td>61.3%</td><td>72.5%</td><td>75.6%</td><td>75.1%</td><td>73.2%</td><td>71.8%</td><td>69.8%</td><td>67.3%</td><td>19.3%</td><td>-48.4%</td><td>-30.9%</td><td>7.9%</td><td>72.7%</td><td>70.5%</td><td>57.8%</td></tr><tr><td>Diff</td><td>n/a</td><td>1.1%</td><td>1.1%</td><td>1.1%</td><td>1.7%</td><td>2.0%</td><td>2.2%</td><td>2.3%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>1.1%</td><td>2.1%</td><td>2.0%</td></tr><tr><td>EBITDA</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>33.0</td><td>63.8</td><td>87.8</td><td>94.9</td><td>97.5</td><td>99.8</td><td>102.7</td><td>97.4</td><td>26.2</td><td>0.9</td><td>5.6</td><td>19.5</td><td>279.5</td><td>397.4</td><td>326.3</td></tr><tr><td>Old</td><td>33.0</td><td>62.6</td><td>80.5</td><td>86.8</td><td>88.5</td><td>90.2</td><td>92.5</td><td>87.5</td><td>26.2</td><td>0.9</td><td>5.6</td><td>19.5</td><td>262.9</td><td>358.7</td><td>293.5</td></tr><tr><td>Diff</td><td>n/a</td><td>2%</td><td>9%</td><td>9%</td><td>10%</td><td>11%</td><td>11%</td><td>11%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>6%</td><td>11%</td><td>11%</td></tr><tr><td>Capex</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>2.8</td><td>4.0</td><td>15.0</td><td>28.1</td><td>18.0</td><td>16.0</td><td>17.0</td><td>19.0</td><td>20.7</td><td>13.2</td><td>16.1</td><td>13.4</td><td>50.0</td><td>70.0</td><td>70.0</td></tr><tr><td>Old</td><td>2.8</td><td>10.0</td><td>15.0</td><td>27.2</td><td>18.0</td><td>16.0</td><td>17.0</td><td>19.0</td><td>20.7</td><td>13.2</td><td>16.1</td><td>13.4</td><td>55.0</td><td>70.0</td><td>70.0</td></tr><tr><td>Diff</td><td>n/a</td><td>-60%</td><td>0%</td><td>4%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-9%</td><td>0%</td><td>0%</td></tr><tr><td>DRAM sales (US$mn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>1,551</td><td>2,612</td><td>3,325</td><td>3,645</td><td>3,840</td><td>4,002</td><td>4,248</td><td>4,160</td><td>1,935</td><td>958</td><td>1,062</td><td>2,156</td><td>11,133</td><td>16,249</td><td>16,082</td></tr><tr><td>Old</td><td>1,551</td><td>2,411</td><td>3,060</td><td>3,356</td><td>3,537</td><td>3,687</td><td>3,915</td><td>3,833</td><td>1,935</td><td>958</td><td>1,062</td><td>2,156</td><td>10,378</td><td>14,972</td><td>14,820</td></tr><tr><td>Diff</td><td>n/a</td><td>8%</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>7%</td><td>9%</td><td>9%</td></tr><tr><td>Shipments (8Gb, mn)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>220</td><td>220</td><td>224</td><td>226</td><td>233</td><td>243</td><td>262</td><td>265</td><td>447</td><td>429</td><td>450</td><td>705</td><td>890</td><td>1,002</td><td>1,154</td></tr><tr><td>Old</td><td>220</td><td>212</td><td>216</td><td>219</td><td>225</td><td>234</td><td>253</td><td>255</td><td>447</td><td>429</td><td>450</td><td>705</td><td>867</td><td>967</td><td>1,114</td></tr><tr><td>Diff</td><td>n/a</td><td>4%</td><td>4%</td><td>4%</td><td>4%</td><td>4%</td><td>4%</td><td>4%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>3%</td><td>4%</td><td>4%</td></tr><tr><td>ASP US$/8b equiv</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>7.90</td><td>12.70</td><td>15.62</td><td>16.87</td><td>17.21</td><td>17.21</td><td>16.86</td><td>16.36</td><td>4.49</td><td>2.52</td><td>2.86</td><td>3.54</td><td>13.31</td><td>16.89</td><td>14.50</td></tr><tr><td>Old</td><td>7.90</td><td>12.23</td><td>14.98</td><td>16.18</td><td>16.50</td><td>16.50</td><td>16.17</td><td>15.69</td><td>4.49</td><td>2.52</td><td>2.86</td><td>3.54</td><td>12.81</td><td>16.20</td><td>13.91</td></tr><tr><td>Diff</td><td>n/a</td><td>4%</td><td>4%</td><td>4%</td><td>4%</td><td>4%</td><td>4%</td><td>4%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>4%</td><td>4%</td><td>4%</td></tr><tr><td>ASP chg (QoQ/YoY)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>71%</td><td>61%</td><td>23%</td><td>8%</td><td>2%</td><td>0%</td><td>-2%</td><td>-3%</td><td>-10%</td><td>-44%</td><td>13%</td><td>24%</td><td>276%</td><td>27%</td><td>-14%</td></tr><tr><td>Old</td><td>71%</td><td>55%</td><td>23%</td><td>8%</td><td>2%</td><td>0%</td><td>-2%</td><td>-3%</td><td>-10%</td><td>-44%</td><td>13%</td><td>24%</td><td>262%</td><td>26%</td><td>-14%</td></tr><tr><td>Diff</td><td>n/a</td><td>6%</td><td>1%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>14%</td><td>0%</td><td>0%</td></tr><tr><td>Cost US$/8Gb equiv</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>3.05</td><td>3.34</td><td>3.64</td><td>4.01</td><td>4.33</td><td>4.50</td><td>4.73</td><td>4.96</td><td>3.61</td><td>3.75</td><td>3.74</td><td>3.30</td><td>3.52</td><td>4.64</td><td>5.83</td></tr><tr><td>Old</td><td>3.05</td><td>3.36</td><td>3.66</td><td>4.03</td><td>4.43</td><td>4.65</td><td>4.88</td><td>5.13</td><td>3.61</td><td>3.75</td><td>3.74</td><td>3.30</td><td>3.53</td><td>4.79</td><td>5.88</td></tr><tr><td>Diff</td><td>n/a</td><td>-2%</td><td>-2%</td><td>-2%</td><td>-10%</td><td>-15%</td><td>-16%</td><td>-17%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-1%</td><td>-14%</td><td>-4%</td></tr><tr><td>Bit growth (QoQ/YoY)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>-27%</td><td>-4%</td><td>5%</td><td>57%</td><td>26%</td><td>13%</td><td>15%</td></tr><tr><td>Old</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>-27%</td><td>-4%</td><td>5%</td><td>57%</td><td>23%</td><td>12%</td><td>15%</td></tr><tr><td>Diff</td><td>n/a</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>3%</td><td>1%</td><td>0%</td></tr></table>

Source: Company, BofA Global Research estimates  
BofA GLOBAL RESEARCH

## BofA Memory Indicator

Exhibit 10: Our memory indicator still near all-time high level in May (183) vs 186/189/189 in Feb/Mar/Apr-26, driven by exceptionally strong DRAM/NAND spot pricing, rising ASPs and billings, along with Korea's $150\%+$ export growth.

BofA Memory Indicator – back to upturn level since Oct-2025 and hit highest peak in Mar/Apr-26 (back-tested)

![](images/b6fe3fdea88f5893bef96f2e352c2d47026ce60063c52811248e177e8d82ce6a.jpg)

Note: Our indicator had previously been capped at \~140, but the recent unprecedented surge—driven by memory spot prices, ASPs, and billings—has led us to raise the ceiling (up to 240 levels) to reflect a more accurate relative comparison. This exceptional strength is further validated by strong earnings from memory chipmakers.

Source: DRAMeXchange, WSTS, MoTIR Korea, BofA Global Research \*The shaded area represents back-tested results from January 1991 to March 2021. The unshaded area represents actual performance since April 2021. This performance is back-tested up to March-2021, and does not represent the actual performance of any account or fund. Back-tested performance depicts the theoretical (not actual) performance of a particular strategy over the time 

[中间内容因长度限制已省略]

ns, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit

purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
