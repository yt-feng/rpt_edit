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
# Asia Communication Infrastructure

## 800VDC Architecture for Next-Generation AI Data Centers

## CITI'S TAKE

In this Super-Sector report, we outline likely implications of the 800VDC transition and potential Asia beneficiaries in the grey space and IT rack power/cooling in AI datacenters. As GPU rack power density approaches 1MW, we forecast 800VDC to reach 79% of new global DC capacity by 2030E, with SST demand surging from 901 MVA in 2027E to 37,152 MVA in 2030E to replace traditional LV transformers. 800VDC architecture is driving combined BESS and BBU battery demand at an 80%+ CAGR through 2030E. We see this as a multi-layer investment opportunity across six segments: DC operators riding AI demand tailwind; power equipment names riding SST architecture upcycle; BESS and BBU suppliers benefiting from rising battery demand; IT rack power/cooling vendors (incl. BBU, MLCC) benefiting from surging power density and cooling requirement; liquid cooling providers capturing structural thermal upgrades; and power semiconductor suppliers underpinning the entire conversion chain.

Traditional AC Chain Gives Way to SST — GPU rack power density has grown nearly 100x since 2020, rendering conventional AC distribution physically unviable. We project 800VDC adoption to reach 79% of new global data center capacity by 2030E, displacing legacy power architecture while creating new equipment categories including SST, BESS, BBU, and new cooling solutions.

Data Center Operators — We expect the near-term AI demand tailwind to be intact. We like China DC market leaders GDS and VENT. In Australia, we think NextDC and CDC/Infratil are positioned to incorporate 800VDC into future builds.

Power Equipment — We see Delta as uniquely positioned with end-to-end grid-to-chip portfolio. Hyosung, Sieyuan and TGOOD should benefit from LV transformer and SST for domestic buildout and export opportunities. Hongfa should ride rising relay products for 800VDC migration. Hitachi Energy India, GE Vernova T&D India, CG Power and Industrial should benefit from India domestic demand and exports.

BESS — 800VDC battery demand could accelerate at an 80%+ CAGR in 2027-30E; Sungrow (SST launch July 2026), BYD, CATL and EVE Energy are key beneficiaries.

IT Rack Power & Cooling — We forecast BBU content value per rack to rise from US\$4-5K in 2022 to US\$33-34K by 2029E, with Panasonic, Dynapack and AES the direct plays. We see Murata, SEMCO and Yageo as key MLCC beneficiaries. We also believe Taiwan and Chinese rack cooling players may benefit from IT cabinets and liquid cooling upgrade.

Cooling Solutions— Higher rack power densities make liquid cooling a structural necessity. LG Electronics, Daikin and Envicool are key names to watch.

Power Semiconductors — VIS leads at high-voltage front end; UMC leveraged to PMIC/BCD specialty nodes; Renesas could benefit via Transphorm GaN acquisition. For China, SG Micro, CR Micro and Silan Micro could benefit from SiC/GaN demand.

![](images/4b0725a8c7f9c8a886bfd7e98e81cf2487933fbe7ba923763752521330429417.jpg)

Kyna Wong $^{AC}$ +852-2868-7820
kyna.wong@citi.com

Yiming Li, CFA
+852-2501-2857
yiming.li@citi.com

Air Ma $^{AC}$

Angela Hsu $^{AC}$

Anusha Madireddy $^{AC}$

Desmond Law $^{AC}$

Eric Lau $^{AC}$

Graeme McDonald $^{AC}$

Howard Penny $^{AC}$

Jack Shang, CFA $^{AC}$

Jamie Wang $^{AC}$

Jeff Chung $^{AC}$

Karen Huang $^{AC}$

Kevin Chen $^{AC}$

Laura (Chia Yi) Chen $^{AC}$

Masahiro Shibano $^{AC}$

Michael Hung $^{AC}$

Michael Rollins, CFA $^{AC}$

Peter Lee $^{AC}$

Pierre Lau, CFA $^{AC}$

Siraj Ahmed AC

Suraj Nebhani, CFA AC

Takayuki Naito $^{AC}$

Takero Fujiwara $^{AC}$

## Contents

800VDC Architecture for Next-Generation AI Data Centers 3
Nvidia's 800VDC Architecture: Four Generations, from Multi-Stage AC to a Single Integrated DC Conversion 4
Traditional AC Chain Has Four Lossy Conversion Stages — All of Which Collapse into One under 800VDC 7
Key Equipment Demand Projection in 800VDC Transition 9
Key Beneficiaries across Infrastructure Stack within a Data Center 12
Deep Dive into Key Asia Beneficiaries in 800VDC Transition 14
Data Center Operators 14
Power Equipment 15
Battery Energy Storage System 19
IT Rack Power and Cooling 21
Cooling Solutions 27
Power Semiconductors 28
Glossary 31
Appendix A-1 33

## 800VDC Architecture for Next-Generation AI Data Centers

In this report, we outline likely implications of the 800V DC transition in AI infrastructure and potential beneficiaries in Asia.

The rapid proliferation of AI workloads is fundamentally reshaping the power infrastructure of modern data centers. GPU rack power density has grown nearly 100-fold compared to traditional web servers — from 10kW per rack in 2020, to 120kW with Blackwell, and should exceed 1MW with the forthcoming Rubin Ultra and Kyber platforms by 2028. This near-exponential trajectory does not merely cause an incremental engineering challenge; it represents a structural inflection point that renders conventional power distribution architectures physically and economically unviable.

In response, the industry is converging on 800VDC as the optimal power distribution standard for next-generation AI infrastructure. By delivering power at higher voltage, 800VDC dramatically reduces current levels, copper requirements, and conversion losses across the entire power chain from the utility grid to the compute chip.

Figure 1. 800VDC Architecture Key Potential Asia Beneficiaries (data as at 16-Jul-2026)

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Analyst</td><td rowspan="2">TP</td><td rowspan="2">Price 16-Jul</td><td rowspan="2">Currency</td><td rowspan="2">Mar Cap (US$M)</td><td colspan="2">P/S (x)</td><td colspan="2">P/E (x)</td><td colspan="3">EPS Growth</td><td colspan="3">Sales Growth</td><td colspan="2">P/BV (x)</td><td colspan="2">ROE</td><td colspan="2">Div. Yield</td></tr><tr><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2025</td><td>2026</td><td>2027</td><td>2025</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td></tr><tr><td colspan="24">Data Centers</td></tr><tr><td>GDS</td><td>GDS.O</td><td>Buy</td><td>Kyna Wong</td><td>58.10</td><td>32.75</td><td>USD</td><td>6,759</td><td>4.0</td><td>4.0</td><td>22.4</td><td></td><td>217%</td><td>101%</td><td>-106%</td><td>11%</td><td>12%</td><td>9%</td><td>1.5</td><td>1.6</td><td>8.5%</td><td>-0.5%</td><td></td><td></td></tr><tr><td>VNET</td><td>VNET.O</td><td>Buy</td><td>Kyna Wong</td><td>16.40</td><td>7.72</td><td>USD</td><td>2,198</td><td>1.2</td><td>1.0</td><td></td><td></td><td>-207%</td><td>-175%</td><td>92%</td><td>20%</td><td>18%</td><td>21%</td><td>3.7</td><td>3.7</td><td>-47.0%</td><td>-1.5%</td><td></td><td></td></tr><tr><td>NextDC</td><td>NXT.AX</td><td>Buy</td><td>Siraj Ahmed</td><td>19.10</td><td>13.45</td><td>AUD</td><td>7,164</td><td>18.5</td><td>14.7</td><td></td><td></td><td>-10%</td><td>-98%</td><td>-207%</td><td>6%</td><td>14%</td><td>42%</td><td>1.9</td><td>2.0</td><td>-3.0%</td><td>-6.8%</td><td></td><td></td></tr><tr><td>Goodman</td><td>GMG.AX</td><td>Buy</td><td>Howard Penny</td><td>40.00</td><td>29.12</td><td>AUD</td><td>41,758</td><td></td><td></td><td>22.2</td><td>20.1</td><td>10%</td><td>11%</td><td>11%</td><td></td><td></td><td></td><td>2.4</td><td>2.2</td><td>9.6%</td><td>11.5%</td><td>1.0%</td><td>1.0%</td></tr><tr><td>Infratil</td><td>IFT.AX</td><td>Buy</td><td>Suraj Nebhani, CFA</td><td>15.18</td><td>12.85</td><td>AUD</td><td>9,031</td><td>4.5</td><td>4.6</td><td>28.5</td><td></td><td>-132%</td><td>280%</td><td>-143%</td><td>23%</td><td>-9%</td><td>-3%</td><td>2.0</td><td>2.1</td><td>7.7%</td><td>-3.2%</td><td>1.3%</td><td>1.3%</td></tr><tr><td>Stockland</td><td>SGP.AX</td><td>Buy</td><td>Suraj Nebhani, CFA</td><td>5.10</td><td>4.08</td><td>AUD</td><td>6,958</td><td></td><td></td><td>11.0</td><td>11.0</td><td>3%</td><td>10%</td><td>0%</td><td></td><td></td><td></td><td>0.9</td><td>0.9</td><td>8.2%</td><td>8.4%</td><td>6.1%</td><td>6.1%</td></tr><tr><td colspan="24">Power Equipment</td></tr><tr><td>Delta</td><td>2308.TW</td><td>Buy</td><td>Laura (Chia Yi) Chen</td><td>2,480.00</td><td>1,905.00</td><td>TWD</td><td>154,921</td><td>6.0</td><td>4.2</td><td>48.6</td><td>30.9</td><td>71%</td><td>69%</td><td>57%</td><td>32%</td><td>50%</td><td>43%</td><td>12.7</td><td>9.3</td><td>27.8%</td><td>34.7%</td><td>1.1%</td><td>1.7%</td></tr><tr><td>Hongfa</td><td>600885.SS</td><td>Buy</td><td>Jamie Wang</td><td>43.00</td><td>33.00</td><td>CNY</td><td>7,544</td><td>2.4</td><td>2.0</td><td>24.8</td><td>19.8</td><td>-22%</td><td>11%</td><td>25%</td><td>22%</td><td>24%</td><td>21%</td><td>3.4</td><td>3.0</td><td>15.0%</td><td>16.2%</td><td>1.2%</td><td>1.5%</td></tr><tr><td>Inovance</td><td>300124.SZ</td><td>Buy</td><td>Jamie Wang</td><td>75.00</td><td>60.31</td><td>CNY</td><td>24,123</td><td>3.0</td><td>2.5</td><td>28.1</td><td>22.8</td><td>17%</td><td>15%</td><td>23%</td><td>22%</td><td>21%</td><td>19%</td><td>4.0</td><td>3.5</td><td>15.4%</td><td>16.6%</td><td>1.0%</td><td>1.2%</td></tr><tr><td>Sieyuan Electric</td><td>002028.SZ</td><td>Buy</td><td>Pierre Lau, CFA</td><td>216.00</td><td>151.40</td><td>CNY</td><td>17,503</td><td>4.2</td><td>3.3</td><td>31.8</td><td>24.4</td><td>53%</td><td>18%</td><td>31%</td><td>39%</td><td>30%</td><td>29%</td><td>6.4</td><td>5.2</td><td>21.8%</td><td>23.6%</td><td>0.5%</td><td>0.7%</td></tr><tr><td>TBEA</td><td>600089.SS</td><td>Buy</td><td>Pierre Lau, CFA</td><td>36.00</td><td>18.88</td><td>CNY</td><td>14,093</td><td>0.9</td><td>0.8</td><td>10.5</td><td>9.2</td><td>84%</td><td>23%</td><td>14%</td><td>1%</td><td>13%</td><td>11%</td><td>1.3</td><td>1.2</td><td>12.7%</td><td>13.2%</td><td>3.0%</td><td>3.4%</td></tr><tr><td>TGOOD</td><td>300001.SZ</td><td>Buy</td><td>Air Ma</td><td>49.60</td><td>31.28</td><td>CNY</td><td>4,877</td><td>2.0</td><td>1.7</td><td>22.8</td><td>17.4</td><td>36%</td><td>17%</td><td>31%</td><td>3%</td><td>4%</td><td>18%</td><td>3.4</td><td>2.9</td><td>15.8%</td><td>17.9%</td><td>0.7%</td><td>1.0%</td></tr><tr><td>Dongfang Electric</td><td>1072.HK</td><td>Buy</td><td>Pierre Lau, CFA</td><td>30.00</td><td>21.22</td><td>HKD</td><td>9,357</td><td>0.8</td><td>0.7</td><td>13.1</td><td>10.6</td><td>18%</td><td>26%</td><td>24%</td><td>-3%</td><td>11%</td><td>7%</td><td>1.3</td><td>1.3</td><td>10.4%</td><td>12.2%</td><td>3.8%</td><td>4.8%</td></tr><tr><td>Yantai Jereh</td><td>002353.SZ</td><td>Buy</td><td>Desmond Law</td><td>146.00</td><td>130.50</td><td>CNY</td><td>19,738</td><td>6.4</td><td>5.0</td><td>37.0</td><td>27.0</td><td>2%</td><td>35%</td><td>37%</td><td>21%</td><td>28%</td><td>29%</td><td>5.2</td><td>4.5</td><td>14.8%</td><td>17.9%</td><td>0.9%</td><td>1.2%</td></tr><tr><td>Weichai Power</td><td>2338.HK</td><td>Buy</td><td>Jeff Chung</td><td>50.00</td><td>32.04</td><td>HKD</td><td>35,296</td><td>0.9</td><td>0.8</td><td>14.6</td><td>11.5</td><td>-4%</td><td>50%</td><td>27%</td><td>7%</td><td>13%</td><td>19%</td><td>2.3</td><td>2.1</td><td>16.9%</td><td>19.4%</td><td>4.0%</td><td>5.1%</td></tr><tr><td>Mitsubishi Electric</td><td>6503.T</td><td>Buy</td><td>Masahiro Shibano</td><td>7,600.00</td><td>5,666.00</td><td>JPY</td><td>71,852</td><td>2.0</td><td>1.8</td><td>28.6</td><td>21.9</td><td>15%</td><td>27%</td><td>30%</td><td>5%</td><td>7%</td><td>8%</td><td>2.6</td><td>2.3</td><td>9.7%</td><td>11.0%</td><td>1.0%</td><td>1.1%</td></tr><tr><td>Hyundai Electric</td><td>267260.KS</td><td>Buy</td><td>Pierre Lau, CFA</td><td>1,440,000.00</td><td>797,000.00</td><td>KRW</td><td>18,975</td><td>5.8</td><td>4.7</td><td>28.3</td><td>22.0</td><td>46%</td><td>38%</td><td>29%</td><td>23%</td><td>20%</td><td>24%</td><td>10.3</td><td>7.6</td><td>42.0%</td><td>39.8%</td><td>0.9%</td><td>1.2%</td></tr><tr><td>Hyosung Heavy</td><td>298040.KS</td><td>Buy</td><td>Pierre Lau, CFA</td><td>4,500,000.00</td><td>2,789,000.00</td><td>KRW</td><td>17,176</td><td>3.6</td><td>2.9</td><td>30.7</td><td>22.2</td><td>167%</td><td>42%</td><td>38%</td><td>22%</td><td>22%</td><td>22%</td><td>8.7</td><td>6.7</td><td>32.0%</td><td>34.1%</td><td>0.7%</td><td>0.9%</td></tr><tr><td>LS Electric</td><td>010120.KS</td><td>Buy</td><td>Pierre Lau, CFA</td><td>320,000.00</td><td>190,000.00</td><td>KRW</td><td>18,823</td><td>4.5</td><td>3.5</td><td>60.3</td><td>41.7</td><td>16%</td><td>68%</td><td>45%</td><td>9%</td><td>27%</td><td>28%</td><td>12.0</td><td>10.1</td><td>21.3%</td><td>26.2%</td><td>0.5%</td><td>0.8%</td></tr><tr><td>Hitachi Energy India</td><td>HITN.NS</td><td>Buy</td><td>Anusha Madireddy</td><td>46,700.00</td><td>33,545.00</td><td>INR</td><td>15,851</td><td>18.4</td><td>11.4</td><td>151.4</td><td>83.2</td><td>123%</td><td>157%</td><td>82%</td><td>22%</td><td>28%</td><td>61%</td><td>28.9</td><td>21.6</td><td>21.0%</td><td>29.7%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>GE Vernova T&amp;D India</td><td>GETD.NS</td><td>Buy</td><td>Anusha Madireddy</td><td>6,200.00</td><td>4,584.10</td><td>INR</td><td>12,444</td><td>18.8</td><td>14.0</td><td>94.8</td><td>62.1</td><td>236%</td><td>103%</td><td>53%</td><td>35%</td><td>45%</td><td>35%</td><td>43.5</td><td>26.7</td><td>55.3%</td><td>53.3%</td><td>0.1%</td><td>0.2%</td></tr><tr><td>CG Power</td><td>CGPO.NS</td><td>Buy</td><td>Anusha Madireddy</td><td>1,100.00</td><td>921.95</td><td>INR</td><td>15,394</td><td>11.7</td><td>9.0</td><td>121.7</td><td>78.2</td><td>-30%</td><td>19%</td><td>56%</td><td>23%</td><td>25%</td><td>30%</td><td>17.8</td><td>14.6</td><td>19.6%</td><td>20.5%</td><td>0.1%</td><td>0.2%</td></tr><tr><td>Siemens Energy India</td><td>SIEE.NS</td><td>Neutral</td><td>Anusha Madireddy</td><td>4,000.00</td><td>3,405.30</td><td>INR</td><td>12,857</td><td>10.9</td><td>9.2</td><td>70.6</td><td>56.2</td><td>83%</td><td>56%</td><td>26%</td><td>64%</td><td>42%</td><td>19%</td><td>19.9</td><td>14.7</td><td>32.8%</td><td>30.0%</td><td></td><td></td></tr><tr><td colspan="24">BESS</td></tr><tr><td>BYD</td><td>1211.HK</td><td>Buy</td><td>Jeff Chung</td><td>142.00</td><td>90.95</td><td>HKD</td><td>105,725</td><td>0.7</td><td>0.6</td><td>17.8</td><td>15.1</td><td>-22%</td><td>24%</td><td>18%</td><td>3%</td><td>35%</td><td>7%</td><td>2.6</td><td>2.3</td><td>15.5%</td><td>16.3%</td><td></td><td></td></tr><tr><td>CATL (H)</td><td>3750.HK</td><td>Buy</td><td>Jack Shang, CFA</td><td>888.00</td><td>621.00</td><td>HKD</td><td>255,764</td><td>3.7</td><td>3.0</td><td>23.8</td><td>19.3</td><td>40%</td><td>40%</td><td>23%</td><td>17%</td><td>58%</td><td>24%</td><td>6.1</td><td>5.1</td><td>27.8%</td><td>28.7%</td><td>2.1%</td><td>2.6%</td></tr><tr><td>CATL (A)</td><td>300750.SZ</td><td>Buy</td><td>Jack Shang, CFA</td><td>603.00</td><td>366.20</td><td>CNY</td><td>255,764</td><td>2.5</td><td>2.0</td><td>16.2</td><td>13.2</td><td>40%</td><td>40%</td><td>23%</td><td>17%</td><td>58%</td><td>24%</td><td>4.1</td><td>3.5</td><td>27.8%</td><td>28.7%</td><td>3.1%</td><td>3.8%</td></tr><tr><td>Sungrow</td><td>300274.SZ</td><td>Buy</td><td>Pierre Lau, CFA</td><td>185.00</td><td>105.84</td><td>CNY</td><td>32,415</td><td>2.0</td><td>1.6</td><td>14.6</td><td>11.6</td><td>23%</td><td>11%</td><td>26%</td><td>15%</td><td>25%</td><td>19%</td><td>3.8</td><td>3.0</td><td>28.5%</td><td>28.9%</td><td>1.7%</td><td>2.2%</td></tr><tr><td>EVE Energy</td><td>300014.SZ</td><td>Buy</td><td>Jack Shang, CFA</td><td>87.90</td><td>51.61</td><td>CNY</td><td>16,569</td><td>1.0</td><td>0.7</td><td>12.8</td><td>10.4</td><td>1%</td><td>100%</td><td>23%</td><td>27%</td><td>79%</td><td>33%</td><td>2.2</td><td>1.9</td><td>18.4%</td><td>19.6%</td><td>1.9%</td><td>2.4%</td></tr><tr><td colspan="24">IT Rack Power &amp; Cooling</td></tr><tr><td>Lenovo</td><td>0992.HK</td><td>Buy</td><td>Kyna Wong</td><td>31.00</td><td>22.26</td><td>HKD</td><td>35,206</td><td>0.4</td><td>0.4</td><td>16.9</td><td>14.0</td><td>34%</td><td>44%</td><td>21%</td><td>21%</td><td>20%</td><td>12%</td><td>4.9</td><td>4.9</td><td>30.3%</td><td>11.5%</td><td>1.9%</td><td>1.9%</td></tr><tr><td>ZTE</td><td>0763.HK</td><td>Neutral</td><td>Kyna Wong</td><td>25.40</td><td>26.28</td><td>HKD</td><td>16,028</td><td>0.8</td><td>0.7</td><td>15.1</td><td>12.9</td><td>-33%</td><td>28%</td><td>17%</td><td>10%</td><td>7%</td><td>9%</td><td>1.3</td><td>1.1</td><td>8.9%</td><td>9.2%</td><td>2.3%</td><td>2.7%</td></tr><tr><td>BYD Electronics</td><td>0285.HK</td><td>Sell</td><td>Kyna Wong</td><td>22.60</td><td>23.46</td><td>HKD</td><td>6,740</td><td>0.3</td><td>0.2</td><td>13.6</td><td>9.2</td><td>-18%</td><td>-5%</td><td>47%</td><td>1%</td><td>0%</td><td>10%</td><td>1.2</td><td>1.1</td><td>9.3%</td><td>12.4%</td><td>0.7%</td><td>1.1%</td></tr><tr><td>Dynapack</td><td>3211.TWO</td><td>Buy</td><td>Angela Hsu</td><td>800.00</td><td>426.50</td><td>TWD</td><td>2,060</td><td>3.7</td><td>2.7</td><td>28.4</td><td>17.1</td><td>-49%</td><td>66%</td><td>67%</td><td>-5%</td><td>35%</td><td>35%</td><td>7.4</td><td>6.8</td><td>24.4%</td><td>41.4%</td><td>2.8%</td><td>4.7%</td></tr><tr><td>AES</td><td>6781.TW</td><td>Buy</td><td>Angela Hsu</td><td>1,680.00</td><td>1,045.00</td><td>TWD</td><td>2,795</td><td>4.7</td><td>3.7</td><td>22.5</td><td>17.0</td><td>50%</td><td>21%</td><td>32%</td><td>59%</td><td>18%</td><td>28%</td><td>4.3</td><td>3.7</td><td>21.2%</td><td>23.6%</td><td>2.2%</td><td>2.9%</td></tr><tr><td>Yageo</td><td>2327.TW</td><td>Buy</td><td>Michael Hung</td><td>1,500.00</td><td>776.00</td><td>TWD</td><td>50,326</td><td>9.3</td><td>6.6</td><td>43.6</td><td>24.7</td><td>20%</td><td>55%</td><td>76%</td><td>9%</td><td>29%</td><td>40%</td><td>8.2</td><td>6.1</td><td>20.0%</td><td>28.3%</td><td>0.8%</td><td>1.2%</td></tr><tr><td>SEMCO</td><td>009150.KS</td><td>Buy</td><td>Peter Lee</td><td>3,000,000.00</td><td>1,277,000.00</td><td>KRW</td><td>62,997</td><td>6.2</td><td>3.9</td><td>60.2</td><td>28.3</td><td>4%</td><td>124%</td><td>113%</td><td>10%</td><td>37%</td><td>57%</td><td>9.6</td><td>7.2</td><td>16.2%</td><td>29.1%</td><td>0.2%</td><td>0.2%</td></tr><tr><td>Murata</td><td>6981.T</td><td>Buy</td><td>Takayuki Naito</td><td>15,000.00</td><td>8,400.00</td><td>JPY</td><td>94,751</td><td>8.4</td><td>7.8</td><td>66.1</td><td>44.1</td><td>30%</td><td>2%</td><td>50%</td><td>6%</td><td>5%</td><td>7%</td><td>5.6</td><td>5.2</td><td>8.8%</td><td>12.3%</td><td>0.9%</td><td>0.9%</td></tr><tr><td>Panasonic</td><td>6752.T</td><td>Buy</td><td>Masahiro Shibano</td><td>5,100.00</td><td>4,218.00</td><td>JPY</td><td>61,030</td><td>1.2</td><td>1.2</td><td>60.6</td><td>21.5</td><td>-18%</td><td>-56%</td><td>181%</td><td>0%</td><td>-5%</td><td>-2%</td><td>1.9</td><td>1.8</td><td>3.3%</td><td>8.5%</td><td>1.0%</td><td>1.4%</td></tr><tr><td c

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
