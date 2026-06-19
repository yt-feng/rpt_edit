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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## China Consumer

Cheap but unloved – stay selective while waiting for the earnings floor

## China Consumer

Jessie Xu AC

Phone: +852 2800-8590

E-mail: jessie.j.xu@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See the end pages of this presentation for analyst certification and important disclosures, including non-US analyst disclosures.

## Key thesis

China Consumer Top Picks: (1) Nongfu (OW): strong brand momentum and margin buffer; (2) Anta (OW): well-executed multi-brand portfolio and overseas upside; (3) Guming (OW): continued runway for network growth and improving brand equity.

Earnings revisions YTD: 2026 consensus EPS is down 9% for Staples and 7% for Discretionary. 80% of our coverage is down YTD, led by Baijiu, beauty, etc. Winners on revisions are fewer but real: Guming, Laopu, Li Ning, and Nongfu. “Full pricing” of cost pressure may not show up until late 2026.  
What if the Iran conflict ended now? Packaging and industrial inputs (e.g. PE/PET) are up 15-40% vs the 2025 average. JPM China Economics team forecasts PPI at 3.5%/3.9%/3.5% in 2-4Q26 and CPI at 1.3%/1.4%/1.1%, widening the CPI-PPI gap to -2.9pp. In this tape, Baijiu and beer look more insulated (less cut-throat competition), while beverages are more exposed. Pricing power matters: Moutai, major brewers, and Haitian should be better positioned to pass costs through.  
Alpha comes from operator quality, not beta. Demand may stay headline-noisy, but the real story is the split underneath. Operator quality – not broad category beta – should be the primary source of alpha. Based on our scoring across fundamentals (demand/supply/pricing/margins), returns (dividends), and valuation, sportswear, pop toys, and white appliances stand out over the next 3-5 years. In our coverage, we like Anta, Pop Mart, and Midea.  
Catalysts to watch and strategy: Cost inflation hitting from 3Q26 is a headwind for beverages. Mid-Autumn Festival and October Golden Week are key read-throughs for baijiu and gold/jewelry.

Positioning: add FMD after June (Guming, Luckin, Chagee); avoid beverages (especially crowded dividend trades) in 3Q26. Comps get friendlier over time: Moutai (N) from 3Q26, FMD and Pop Mart (N) from 4Q26, and beverages from 2Q27.

## Focus Charts

Earnings revisions and share price performance

<table><tr><td rowspan="2">Company name</td><td rowspan="2">Sub-sector</td><td rowspan="2">BBG Ticker</td><td rowspan="2">Price (LC)</td><td rowspan="2">Mkt Cap (USDmn)</td><td colspan="2">Net profit YoY</td><td>NP CAGR</td><td colspan="3">FY26 sales revisions</td><td colspan="3">FY26 NP revisions</td><td colspan="3">Share performance</td></tr><tr><td>2026E</td><td>2027E</td><td>25-27E</td><td>1Q26</td><td>2QTD</td><td>YTD</td><td>1Q26</td><td>2QTD</td><td>YTD</td><td>1M</td><td>3M</td><td>YTD</td></tr><tr><td colspan="17">China/HK SAR Staples</td></tr><tr><td>Moutai - A</td><td>Baijiu</td><td>600519 CH</td><td>1240.0</td><td>229,024</td><td>4.1%</td><td>6.6%</td><td>5.4%</td><td>-2%</td><td>-6%</td><td>-8%</td><td>-2%</td><td>-10%</td><td>-11%</td><td>-6%</td><td>-16%</td><td>-10%</td></tr><tr><td>Wuliangye - A</td><td>Baijiu</td><td>000858 CH</td><td>77.5</td><td>44,440</td><td>126.3%</td><td>9.1%</td><td>57.2%</td><td>-5%</td><td>-20%</td><td>-24%</td><td>-5%</td><td>-20%</td><td>-24%</td><td>-9%</td><td>-25%</td><td>-27%</td></tr><tr><td>Luzhou Laojiao - A</td><td>Baijiu</td><td>000568 CH</td><td>82.9</td><td>18,037</td><td>-4.6%</td><td>8.8%</td><td>1.8%</td><td>-3%</td><td>-11%</td><td>-14%</td><td>-4%</td><td>-12%</td><td>-16%</td><td>-8%</td><td>-22%</td><td>-29%</td></tr><tr><td>Yanghe - A</td><td>Baijiu</td><td>002304 CH</td><td>42.1</td><td>9,366</td><td>29.4%</td><td>15.6%</td><td>22.3%</td><td>-3%</td><td>-10%</td><td>-13%</td><td>-12%</td><td>-23%</td><td>-32%</td><td>-7%</td><td>-18%</td><td>-31%</td></tr><tr><td>Budweiser APAC</td><td>Beer</td><td>1876 HK</td><td>6.7</td><td>11,238</td><td>20.5%</td><td>9.5%</td><td>14.9%</td><td>-3%</td><td>-1%</td><td>-4%</td><td>-15%</td><td>-4%</td><td>-18%</td><td>-12%</td><td>-9%</td><td>-12%</td></tr><tr><td>CRB</td><td>Beer</td><td>291 HK</td><td>22.1</td><td>9,157</td><td>51.7%</td><td>6.4%</td><td>27.0%</td><td>-2%</td><td>-1%</td><td>-3%</td><td>-2%</td><td>-1%</td><td>-3%</td><td>-16%</td><td>-14%</td><td>-16%</td></tr><tr><td>Tsingtao - A</td><td>Beer</td><td>600600 CH</td><td>56.1</td><td>9,796</td><td>9.2%</td><td>5.3%</td><td>7.2%</td><td>-1%</td><td>0%</td><td>-1%</td><td>-2%</td><td>-1%</td><td>-3%</td><td>-9%</td><td>-11%</td><td>-8%</td></tr><tr><td>Tsingtao - H</td><td>Beer</td><td>168 HK</td><td>46.9</td><td>9,796</td><td>9.2%</td><td>5.3%</td><td>7.2%</td><td>-1%</td><td>0%</td><td>-1%</td><td>-2%</td><td>-1%</td><td>-3%</td><td>-8%</td><td>-5%</td><td>-4%</td></tr><tr><td>Nongfu Spring</td><td>Beverage</td><td>9633 HK</td><td>42.8</td><td>61,365</td><td>13.0%</td><td>12.8%</td><td>12.9%</td><td>5%</td><td>0%</td><td>5%</td><td>4%</td><td>0%</td><td>4%</td><td>0%</td><td>-1%</td><td>-9%</td></tr><tr><td>Eastroc - A</td><td>Beverage</td><td>605499 CH</td><td>125.4</td><td>13,402</td><td>31.5%</td><td>18.5%</td><td>24.9%</td><td>0%</td><td>-1%</td><td>-1%</td><td>-1%</td><td>-2%</td><td>-4%</td><td>-12%</td><td>-30%</td><td>-39%</td></tr><tr><td>CR Beverage</td><td>Beverage</td><td>2460 HK</td><td>7.6</td><td>2,314</td><td>12.0%</td><td>16.0%</td><td>14.0%</td><td>-6%</td><td>-2%</td><td>-8%</td><td>-20%</td><td>-8%</td><td>-26%</td><td>-7%</td><td>-21%</td><td>-25%</td></tr><tr><td>Mixue Group</td><td>FMD</td><td>2097 HK</td><td>253.8</td><td>12,294</td><td>7.5%</td><td>13.2%</td><td>10.3%</td><td>0%</td><td>0%</td><td>0%</td><td>-4%</td><td>-1%</td><td>-5%</td><td>-3%</td><td>-26%</td><td>-38%</td></tr><tr><td>Luckin Coffee</td><td>FMD</td><td>LKNCY US</td><td>30.7</td><td>8,786</td><td>34.1%</td><td>26.0%</td><td>30.0%</td><td>0%</td><td>2%</td><td>1%</td><td>-7%</td><td>1%</td><td>-7%</td><td>-3%</td><td>-10%</td><td>-8%</td></tr><tr><td>Guming</td><td>FMD</td><td>1364 HK</td><td>21.2</td><td>6,446</td><td>23.5%</td><td>20.5%</td><td>22.0%</td><td>12%</td><td>2%</td><td>14%</td><td>20%</td><td>3%</td><td>24%</td><td>-6%</td><td>-27%</td><td>-14%</td></tr><tr><td>Chagee</td><td>FMD</td><td>CHA US</td><td>11.5</td><td>2,198</td><td>51.0%</td><td>9.3%</td><td>28.4%</td><td>-2%</td><td>-10%</td><td>-12%</td><td>-4%</td><td>-19%</td><td>-23%</td><td>13%</td><td>5%</td><td>-1%</td></tr><tr><td>WH Group</td><td>Meat</td><td>288 HK</td><td>8.9</td><td>14,538</td><td>-2.4%</td><td>2.2%</td><td>-0.1%</td><td>-1%</td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>1%</td><td>-5%</td><td>-8%</td><td>2%</td></tr><tr><td>Yum China</td><td>QSR &amp; Condiment</td><td>YUMC US</td><td>43.3</td><td>15,032</td><td>-1.9%</td><td>8.8%</td><td>3.3%</td><td>0%</td><td>-1%</td><td>0%</td><td>0%</td><td>-1%</td><td>-1%</td><td>-5%</td><td>-18%</td><td>-9%</td></tr><tr><td>Haitian - A</td><td>QSR &amp; Condiment</td><td>603288 CH</td><td>33.3</td><td>28,489</td><td>14.0%</td><td>10.6%</td><td>12.3%</td><td>1%</td><td>0%</td><td>1%</td><td>0%</td><td>0%</td><td>1%</td><td>-8%</td><td>-14%</td><td>-9%</td></tr><tr><td>Yili - A</td><td>Dairy</td><td>600887 CH</td><td>24.7</td><td>23,056</td><td>5.2%</td><td>8.1%</td><td>6.6%</td><td>0%</td><td>0%</td><td>-1%</td><td>-1%</td><td>2%</td><td>0%</td><td>-10%</td><td>-8%</td><td>-14%</td></tr><tr><td>Mengniu</td><td>Dairy</td><td>2319 HK</td><td>15.8</td><td>7,816</td><td>144.7%</td><td>10.9%</td><td>64.7%</td><td>0%</td><td>0%</td><td>1%</td><td>-7%</td><td>0%</td><td>-7%</td><td>-9%</td><td>-5%</td><td>6%</td></tr><tr><td>Feihe</td><td>Dairy</td><td>6186 HK</td><td>3.0</td><td>3,417</td><td>4.7%</td><td>6.7%</td><td>5.7%</td><td>-6%</td><td>-2%</td><td>-8%</td><td>-17%</td><td>-6%</td><td>-22%</td><td>-6%</td><td>-22%</td><td>-25%</td></tr><tr><td>Simple average</td><td></td><td></td><td></td><td></td><td>27.9%</td><td>11.3%</td><td>18.3%</td><td>-1%</td><td>-2%</td><td>-3%</td><td>-2%</td><td>-7%</td><td>-9%</td><td>-7%</td><td>-15%</td><td>-13%</td></tr><tr><td colspan="17">China/HK SAR Discretionary</td></tr><tr><td>Midea - A</td><td>Home app</td><td>000333 CH</td><td>79.2</td><td>88,779</td><td>6.7%</td><td>8.4%</td><td>7.5%</td><td>1%</td><td>0%</td><td>0%</td><td>0%</td><td>-3%</td><td>-3%</td><td>-4%</td><td>3%</td><td>1%</td></tr><tr><td>Haier - H</td><td>Home app</td><td>6690 HK</td><td>21.0</td><td>27,170</td><td>1.7%</td><td>8.7%</td><td>5.2%</td><td>-2%</td><td>-2%</td><td>-4%</td><td>-8%</td><td>-6%</td><td>-13%</td><td>2%</td><td>-16%</td><td>-14%</td></tr><tr><td>Haier - A</td><td>Home app</td><td>600690 CH</td><td>20.5</td><td>27,170</td><td>1.7%</td><td>8.7%</td><td>5.2%</td><td>-2%</td><td>-2%</td><td>-4%</td><td>-8%</td><td>-6%</td><td>-13%</td><td>-3%</td><td>-18%</td><td>-21%</td></tr><tr><td>Gree - A</td><td>Home app</td><td>000651 CH</td><td>37.2</td><td>30,745</td><td>0.1%</td><td>3.4%</td><td>1.7%</td><td>-1%</td><td>-3%</td><td>-3%</td><td>-2%</td><td>-5%</td><td>-6%</td><td>-6%</td><td>-5%</td><td>-8%</td></tr><tr><td>Ecovac - A</td><td>Home app</td><td>603486 CH</td><td>53.3</td><td>4,558</td><td>26.8%</td><td>18.1%</td><td>22.4%</td><td>-2%</td><td>0%</td><td>-1%</td><td>-4%</td><td>-4%</td><td>-8%</td><td>-22%</td><td>-16%</td><td>-34%</td></tr><tr><td>Supor - A</td><td>Home app</td><td>002032 CH</td><td>41.7</td><td>4,926</td><td>7.8%</td><td>6.7%</td><td>7.2%</td><td>-1%</td><td>-1%</td><td>-2%</td><td>-3%</td><td>-2%</td><td>-5%</td><td>-13%</td><td>-7%</td><td>-5%</td></tr><tr><td>Robam - A</td><td>Home app</td><td>002508 CH</td><td>15.6</td><td>2,181</td><td>16.6%</td><td>6.3%</td><td>11.4%</td><td>-2%</td><td>-8%</td><td>-10%</td><td>-3%</td><td>-16%</td><td>-18%</td><td>-11%</td><td>-25%</td><td>-19%</td></tr><tr><td>Bosideng</td><td>Apparel</td><td>3998 HK</td><td>4.1</td><td>6,083</td><td>20.3%</td><td>1.4%</td><td>10.5%</td><td>-3%</td><td>-1%</td><td>-4%</td><td>-4%</td><td>-1%</td><td>-6%</td><td>-2%</td><td>0%</td><td>-9%</td></tr><tr><td>HLA Corp - A</td><td>Apparel</td><td>600398 CH</td><td>5.7</td><td>4,023</td><td>4.8%</td><td>8.8%</td><td>6.8%</td><td>0%</td><td>-1%</td><td>0%</td><td>-4%</td><td>-6%</td><td>-10%</td><td>-4%</td><td>-9%</td><td>-6%</td></tr><tr><td>Semir - A</td><td>Apparel</td><td>002563 CH</td><td>5.2</td><td>2,078</td><td>16.1%</td><td>10.9%</td><td>13.5%</td><td>0%</td><td>-2%</td><td>-2%</td><td>0%</td><td>-8%</td><td>-8%</td><td>-9%</td><td>-6%</td><td>-4%</td></tr><tr><td>Peacebird - A</td><td>Apparel</td><td>603877 CH</td><td>13.0</td><td>907</td><td>58.0%</td><td>23.2%</td><td>39.5%</td><td>0%</td><td>-7%</td><td>-7%</td><td>-7%</td><td>-7%</td><td>-13%</td><td>-5%</td><td>-13%</td><td>-10%</td></tr><tr><td>Botanee - A</td><td>Beauty</td><td>300957 CH</td><td>33.6</td><td>2,102</td><td>23.6%</td><td>16.3%</td><td>19.9%</td><td>-1%</td><td>0%</td><td>-1%</td><td>-3%</td><td>4%</td><td>1%</td><td>-14%</td><td>-20%</td><td>-15%</td></tr><tr><td>Proya - A</td><td>Beauty</td><td>603605 CH</td><td>66.0</td><td>3,861</td><td>9.8%</td><td>9.9%</td><td>9.8%</td><td>-3%</td><td>-6%</td><td>-9%</td><td>-4%</td><td>-7%</td><td>-11%</td><td>17%</td><td>-2%</td><td>-4%</td></tr><tr><td>Jahwa - A</td><td>Beauty</td><td>600315 CH</td><td>18.1</td><td>1,801</td><td>149.4%</td><td>29.1%</td><td>79.5%</td><td>1%</td><td>-1%</td><td>0%</td><td>-13%</td><td>-10%</td><td>-22%</td><td>-2%</td><td>-17%</td><td>-19%</td></tr><tr><td>Marubi - A</td><td>Beauty</td><td>603983 CH</td><td>21.8</td><td>1,289</td><td>45.4%</td><td>19.5%</td><td>31.8%</td><td>-1%</td><td>-11%</td><td>-12%</td><td>-3%</td><td>-25%</td><td>-27%</td><td>-12%</td><td>-21%</td><td>-34%</td></tr><tr><td>Chicmax</td><td>Beauty</td><td>2145 HK</td><td>31.6</td><td>1,641</td><td>18.5%</td><td>20.9%</td><td>19.7%</td><td>4%</td><td>0%</td><td>4%</td><td>-2%</td><td>-2%</td><td>-5%</td><td>-23%</td><td>-48%</td><td>-57%</td></tr><tr><td>CTG Duty Free - A</td><td>Duty-free shop</td><td>601888 CH</td><td>56.8</td><td>17,257</td><td>42.1%</td><td>18.0%</td><td>29.5%</td><td>0%</td><td>-4%</td><td>-3%</td><td>3%</td><td>2%</td><td>5%</td><td>-2%</td><td>-24%</td><td>-40%</td></tr><tr><td>Pop Mart</td><td>IP merchandise</td><td>9992 HK</td><td>171.3</td><td>29,110</td><td>13.3%</td><td>16.9%</td><td>15.1%</td><td>-7%</td><td>-6%</td><td>-13%</td><td>-9%</td><td>-10%</td><td>-18%</td><td>14%</td><td>-23%</td><td>-9%</td></tr><tr><td>Miniso - ADR</td><td>IP merchandise</td><td>MNSO US</td><td>12.2</td><td>3,763</td><td>162.9%</td><td>13.5%</td><td>72.8%</td><td>0%</td><td>0%</td><td>1%</td><td>-1%</td><td>-11%</td><td>-12%</td><td>-15%</td><td>-29%</td><td>-35%</td></tr><tr><td>Miniso - H</td><td>IP merchandise</td><td>9896 HK</td><td>24.1</td><td>3,813</td><td>162.9%</td><td>13.5%</td><td>72.8%</td><td>0%</td><td>0%</td><td>1%</td><td>-1%</td><td>-11%</td><td>-12%</td><td>-14%</td><td>-30%</td><td>-34%</td></tr><tr><td>Chow Tai Fook^</td><td>Jewelry</td><td>1929 HK</td><td>12.6</td><td>15,811</td><td>39.3%</td><td>-0.7%</td><td>17.6%</td><td>-8%</td><td>-3%</td><td>-11%</td><td>1%</td><td>-1%</td><td>0%</td><td>14%</td><td>7%</td><td>1%</td></tr><tr><td>Laopu Gold</td><td>Jewelry</td><td>6181 HK</td><td>452.0</td><td>10,194</td><td>70.8%</td><td>20.6%</td><td>43.5%</td><td>16%</td><td>5%</td><td>23%</td><td>17%</td><td>6%</td><td>25%</td><td>-17%</td><td>-33%</td><td>-27%</td></tr><tr><td>Lao Feng Xiang - A</td><td>Jewelry</td><td>600612 CH</td><td>34.9</td><td>2,264</td><td>-10.1%</td><td>7.5%</td><td>-1.7%</td><td>2%</td><td>-9%</td><td>-7%</td><td>0%</td><td>-11%</td><td>-11%</td><td>-6%</td><td>-18%</td><td>-22%</td></tr><tr><td>Anta</td><td>Sportswear</td><td>2020 HK</td><td>72.1</td><td>25,730</td><td>6.9%</td><td>9.1%</td><td>8.0%</td><td>0%</td><td>1%</td><td>1%</td><td>-4%</td><td>1%</td><td>-4%</td><td>-5%</td><td>-8%</td><td>-10%</td></tr><tr><td>Li Ning</td><td>Sportswear</td><td>2331 HK</td><td>16.6</td><td>5,465</td><td>-8.2%</td><td>12.6%</td><td>1.7%</td><td>4%</td><td>1%</td><td>4%</td><td>7%</td><td>1%</td><td>8%</td><td>-10%</td><td>-18%</td><td>-11%</td></tr><tr><td>Xtep</td><td>Sportswear</td><td>1368 HK</td><td>4.1</td><td>1,472</td><td>-6.5%</td><td>13.4%</td><td>3.0%</td><td>-2%</td><td>-2%</td><td>-4%</td><td>-7%</td><td>-9%</td><td>-16%</td><td>-2%</td><td>-18%</td><td>-23%</td></tr><tr><td>Shenzhen</td><td>Textiles</td><td>2313 HK</td><td>42.7</td><td>8,181</td><td>3.5%</td><td>10.2%</td><td>6.8%</td><td>-2%</td><td>-5%</td><td>-8%</td><td>-6%</td><td>-12%</td><td>-17%</td><td>-7%</td><td>-23%</td><td>-30%</td></tr><tr><td>Luolai - A</td><td>Textiles</td><td>002293 CH</td><td>10.1</td><td>1,242</td><td>12.8%</td><td>12.6%</td><td>12.7%</td><td>0%</td><td>0%</td><td>0%</td><td>1%</td><td>1%</td><td>2%</td><td>-9%</td><td>0%</td><td>-2%</td></tr><tr><td>Luthai - A</td><td>Textiles</td><td>000726 CH</td><td>5.8</td><td>633</td><td>28.0%</td><td>11.0%</td><td>19.2%</td><td>-4%</td><td>-9%</td><td>-13%</td><td>-2%</td><td>-10%</td><td>-12%</td><td>-6%</td><td>-22%</td><td>-19%</td></tr><tr><td>Best Pacific</td><td>Textiles</td><td>2111 HK</td><td>2.5</td><td>337</td><td>-1.2%</td><td>12.1%</td><td>5.2%</td><td>-5%</td><td>-1%</td><td>-5%</td><td>-11%</td><td>-5%</td><td>-15%</td><td>-9%</td><td>-19%</td><td>-22%</td></tr></table>

Note: ^ refers to year end in Mar.

## Focus Charts

China/HK consumer staples valuation  
Trading at 16x forward P/E, 1.5 STD below 10-year mean  
![](images/c7e1ee89a65dc232fe556d3392b946ecbf253cdd7d19aab4d9a307ddf84ee889.jpg)

<details>
<summary>line chart</summary>

| Year | Forward P/E | Average | Avg - 1STD | Avg + 1STD | Avg - 2STD |
|------|-------------|---------|------------|------------|------------|
| 2015 | ~28x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2016 | ~25x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2017 | ~26x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2018 | ~25x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2019 | ~24x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2020 | ~26x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2021 | ~38x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2022 | ~30x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2023 | ~28x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2024 | ~18x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2025 | ~16x        | ~25x    | ~25x       | ~25x       | ~25x       |
| 2026 | ~16x        | ~25x    | ~25x       | ~25x       | ~25x       |
</details>

Source: Bloomberg Finance L.P. and JPM.

China/HK consumer discretionary valuation  
Trading at 13x forward P/E, 1.5 STD below 10-year mean  
![](images/566a5e8119784b11a1389c9473fb5083f3ad09c38b92d7f0d44977493d68c5c6.jpg)

<details>
<summary>line chart</summary>

| Year | Forward P/E | Average | Avg + 1STD | Avg - 1STD | Avg - 2STD |
|------|-------------|---------|------------|------------|------------|
| 2015 | ~18x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2016 | ~19x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2017 | ~18x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2018 | ~19x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2019 | ~13x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2020 | ~18x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2021 | ~24x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2022 | ~20x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2023 | ~19x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2024 | ~13x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2025 | ~15x        | 17x     | ~17x       | ~15x       | ~12x       |
| 2026 | ~13x        | 17x     | ~17x       | ~15x       | ~12x       |
</details>

Source: Bloomberg Finance L.P. and JPM.

## Current P/E multiple vs 10Y range

Beverage, beer, condiments, catering, sportswear, beauty, jewelry are trading in the bottom decile of their respective 10Y valuation ranges  
![](images/27905ad955702bc98a3b94bfd0dfef62f69ea16f08021fad345dfb01750a2968.jpg)

<details>
<summary>bar chart</summary>

| Category | Consumer staples - Current | Consumer staples - 1Y ago | Consumer staples - 10Y Range | Consumer discretio

[中间内容因长度限制已省略]

are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any

## Disclosures

reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
