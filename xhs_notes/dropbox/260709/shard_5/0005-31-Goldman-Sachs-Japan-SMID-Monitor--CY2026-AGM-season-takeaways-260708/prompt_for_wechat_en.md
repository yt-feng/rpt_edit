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
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Japan SMID Monitor: CY2026 AGM season takeaways

In this month's edition of the Japan SMID Monitor, we focus on the 2026 AGM season trends within Japan SMID universe versus the larger cap space. One conclusion is that Japan SMID stocks currently appear to be under slightly more shareholder pressure versus their larger cap peers. Just over $15\%$ of Japan SMIDs have CEO approval ratings below $80\%$ (Exhibit 7), compared with less than $10\%$ for companies with 6M ADTV over US\$20mn. However, in terms of overall average approval rating changes over time (Exhibit 5) and inter-quartile ranges (Exhibit 6), there appears to be very little difference between the two data-sets. Historically, CEO approval IQRs were significantly higher with Japan SMID stocks (Exhibit 6), but this difference largely disappeared in CY2026. After peaking in CY2024 at over $11\%$ (versus just $7\%$ for the more liquid universe), the SMID CEO approval IQR fell 2ppts to $9\%$ by CY2026, while the more liquid universe's CEO Approval IQR has risen 2ppts to the same $9\%$ level.

Tech Hardware, Industrials and Inbound Tourism out-performed IT Services in GS Japan coverage universe: The best-performing SMID names in June covered by GS Japan analysts included Taiyo Yuden (+37% mom), Japan Material (+25% mom), Kyoritsu Maintenance (+21% mom) and Kotobuki Spirits (+19% mom). The two worst-performers were ANYCOLOR (-22% mom), and Cover Corp (-14%).

Japan SMID thematic and sub-sector index data showed that Financials led in June while Software lagged: The best-preforming indices last month were Regional Banks (+17% mom) and Banks (+11% mom), while the worst-performers included SAAS (-13% mom) and Software (-9% mom).

GS Japan SMID team remain bullish on the Japan Shipbuilding sector: GS Japan SMID analyst Norihiro Miyazaki published a sector update on the Japan Shipbuilding sector (LINK). Japan's May 2026 order backlog was a very healthy 29.3mn GT (vessel demand for the next 3-4 years), and media reports also suggest that the US Navy may start to procure ships from US and South Korean shipyards. If confirmed, this would be a very positive catalyst for this sector in Japan.

■ Individuals net bought TSE Growth and TSE Standard, whilst foreigners net sold both: As can be seen in Exhibit 1 and Exhibit 2 below, for the month of June, individuals net bought ¥11.4bn and ¥84.3bn of Standard cash equities and Growth cash, whilst foreigners net sold -¥13.9bn and -¥63.4bn, respectively.

Bruce Kirk, CFA
+81(3)4587-9950 | bruce.kirk@gs.com
GS Japan Co., Ltd.

Julius Chan
+81(3)4587-1789 | julius.chan@gs.com
GS Japan Co., Ltd.

Exhibit 1: TSE Standard net buying 2-year chart as of Jun 26 2026, JPY bn  
![](images/a9060d64199e28ff0e77ac17592192d2214d2871ab89ff8c22269c24bbf8bf2a.jpg)  
Source: Bloomberg, Tokyo Stock Exchange

Exhibit 2: TSE Growth net buying
2-year chart as of Jun 26 2026, JPY bn  
![](images/6c08717a895b45bc7ca8ea75960646961d747a6bc10067506ee6f626dbeb8af4.jpg)  
Source: Bloomberg, Tokyo Stock Exchange

## GS Covered Japan SMID Stocks

Exhibit 3: GS covered SMID stocks ranked by monthly performance
Data as of Jun 30 2026

<table><tr><td>Ticker</td><td>Name</td><td>Analyst</td><td>1W</td><td>2W</td><td>1M</td><td>3M</td><td>6M</td><td>YTD</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>Daiki Takayama</td><td>19%</td><td>0%</td><td>36%</td><td>398%</td><td>469%</td><td>469%</td></tr><tr><td>6055</td><td>Japan Material</td><td>Takeru Adachi</td><td>1%</td><td>7%</td><td>25%</td><td>55%</td><td>66%</td><td>66%</td></tr><tr><td>9616</td><td>Kyoritsu Maintenance</td><td>Norihiro Miyazaki</td><td>5%</td><td>11%</td><td>21%</td><td>21%</td><td>8%</td><td>8%</td></tr><tr><td>2222</td><td>Kotobuki Spirits Co.</td><td>Norihiro Miyazaki</td><td>7%</td><td>9%</td><td>19%</td><td>32%</td><td>36%</td><td>36%</td></tr><tr><td>6622</td><td>Daihen</td><td>Ryo Harada</td><td>-3%</td><td>11%</td><td>14%</td><td>46%</td><td>81%</td><td>81%</td></tr><tr><td>6407</td><td>CKD</td><td>Yuichiro Isayama</td><td>-2%</td><td>0%</td><td>14%</td><td>58%</td><td>144%</td><td>144%</td></tr><tr><td>6103</td><td>Okuma</td><td>Yuichiro Isayama</td><td>4%</td><td>4%</td><td>13%</td><td>24%</td><td>27%</td><td>27%</td></tr><tr><td>6728</td><td>Ulvac</td><td>Shuhei Nakamura</td><td>4%</td><td>15%</td><td>9%</td><td>18%</td><td>46%</td><td>46%</td></tr><tr><td>4205</td><td>Zeon</td><td>Atsushi Ikeda</td><td>2%</td><td>1%</td><td>8%</td><td>31%</td><td>32%</td><td>32%</td></tr><tr><td>6254</td><td>NOM Micro Science</td><td>Takeru Adachi</td><td>-2%</td><td>7%</td><td>7%</td><td>49%</td><td>65%</td><td>65%</td></tr><tr><td>7988</td><td>Nifco Inc.</td><td>Kota Yuzawa</td><td>4%</td><td>8%</td><td>7%</td><td>7%</td><td>0%</td><td>0%</td></tr><tr><td>4912</td><td>Lion</td><td>Takashi Miyazaki</td><td>4%</td><td>2%</td><td>6%</td><td>0%</td><td>4%</td><td>4%</td></tr><tr><td>7721</td><td>Tokyo Keiki</td><td>Norihiro Miyazaki</td><td>0%</td><td>18%</td><td>5%</td><td>-5%</td><td>16%</td><td>16%</td></tr><tr><td>6951</td><td>JEOL</td><td>Shuhei Nakamura</td><td>7%</td><td>12%</td><td>5%</td><td>22%</td><td>48%</td><td>48%</td></tr><tr><td>9706</td><td>Japan Airport Terminal</td><td>Norihiro Miyazaki</td><td>7%</td><td>5%</td><td>4%</td><td>-7%</td><td>15%</td><td>15%</td></tr><tr><td>6432</td><td>Takeuchi MFG</td><td>Takeru Adachi</td><td>-4%</td><td>-4%</td><td>4%</td><td>9%</td><td>5%</td><td>5%</td></tr><tr><td>3774</td><td>Internet Initiative Japan</td><td>Chikai Tanaka, CFA</td><td>5%</td><td>8%</td><td>3%</td><td>28%</td><td>16%</td><td>16%</td></tr><tr><td>4202</td><td>Daicel</td><td>Atsushi Ikeda</td><td>6%</td><td>3%</td><td>3%</td><td>9%</td><td>-2%</td><td>-2%</td></tr><tr><td>2229</td><td>Calbee Inc</td><td>Takashi Miyazaki</td><td>5%</td><td>5%</td><td>2%</td><td>-5%</td><td>-1%</td><td>-1%</td></tr><tr><td>8304</td><td>Aozora Bank</td><td>Makoto Kuroda</td><td>-1%</td><td>-1%</td><td>2%</td><td>3%</td><td>8%</td><td>8%</td></tr><tr><td>7581</td><td>Saizeriya</td><td>Sho Kawano</td><td>4%</td><td>3%</td><td>1%</td><td>-18%</td><td>-1%</td><td>-1%</td></tr><tr><td>4483</td><td>JMDC</td><td>Akinori Ueda, Ph.D.</td><td>6%</td><td>4%</td><td>1%</td><td>-16%</td><td>-28%</td><td>-28%</td></tr><tr><td>6592</td><td>Mabuchi Motor</td><td>Daiki Takayama</td><td>-1%</td><td>-1%</td><td>1%</td><td>-3%</td><td>9%</td><td>9%</td></tr><tr><td>3994</td><td>Money Forward</td><td>Chikai Tanaka, CFA</td><td>8%</td><td>13%</td><td>1%</td><td>21%</td><td>-6%</td><td>-6%</td></tr><tr><td>6324</td><td>Harmonic Drive Systems</td><td>Yuichiro Isayama</td><td>1%</td><td>11%</td><td>0%</td><td>113%</td><td>106%</td><td>106%</td></tr><tr><td>4194</td><td>Visional</td><td>Norihiro Miyazaki</td><td>9%</td><td>8%</td><td>-1%</td><td>6%</td><td>-22%</td><td>-22%</td></tr><tr><td>6674</td><td>GS Yuasa Corp.</td><td>Kota Yuzawa</td><td>-9%</td><td>-2%</td><td>-1%</td><td>14%</td><td>72%</td><td>72%</td></tr><tr><td>8570</td><td>Aeon Financial Service Co.</td><td>Makoto Kuroda</td><td>2%</td><td>-2%</td><td>-3%</td><td>-8%</td><td>-16%</td><td>-16%</td></tr><tr><td>6508</td><td>Meidensha</td><td>Ryo Harada</td><td>-6%</td><td>4%</td><td>-3%</td><td>20%</td><td>75%</td><td>75%</td></tr><tr><td>4061</td><td>Denka</td><td>Atsushi Ikeda</td><td>-1%</td><td>3%</td><td>-3%</td><td>15%</td><td>58%</td><td>58%</td></tr><tr><td>6754</td><td>Anritsu</td><td>Ryo Harada</td><td>-2%</td><td>7%</td><td>-3%</td><td>47%</td><td>96%</td><td>96%</td></tr><tr><td>4587</td><td>PeptiDream</td><td>Akinori Ueda, Ph.D.</td><td>9%</td><td>13%</td><td>-4%</td><td>-15%</td><td>-36%</td><td>-36%</td></tr><tr><td>3697</td><td>SHIFT</td><td>Chikai Tanaka, CFA</td><td>10%</td><td>6%</td><td>-4%</td><td>-1%</td><td>-31%</td><td>-31%</td></tr><tr><td>7383</td><td>Net Protections Holdings</td><td>Makoto Kuroda</td><td>-1%</td><td>-1%</td><td>-4%</td><td>-12%</td><td>-35%</td><td>-35%</td></tr><tr><td>7014</td><td>Namura Shipbuilding Co.</td><td>Norihiro Miyazaki</td><td>-4%</td><td>-6%</td><td>-5%</td><td>-20%</td><td>0%</td><td>0%</td></tr><tr><td>4478</td><td>freee K.K.</td><td>Chikai Tanaka, CFA</td><td>7%</td><td>5%</td><td>-5%</td><td>-4%</td><td>-34%</td><td>-34%</td></tr><tr><td>6770</td><td>Alps Alpine</td><td>Daiki Takayama</td><td>-4%</td><td>-3%</td><td>-6%</td><td>-8%</td><td>3%</td><td>3%</td></tr><tr><td>3923</td><td>Rakus Co.</td><td>Norihiro Miyazaki</td><td>7%</td><td>6%</td><td>-6%</td><td>21%</td><td>-9%</td><td>-9%</td></tr><tr><td>6966</td><td>Mitsui High-tec Inc.</td><td>Kota Yuzawa</td><td>-12%</td><td>-14%</td><td>-7%</td><td>57%</td><td>25%</td><td>25%</td></tr><tr><td>3116</td><td>Toyota Boshoku</td><td>Kota Yuzawa</td><td>0%</td><td>-5%</td><td>-7%</td><td>-14%</td><td>-15%</td><td>-15%</td></tr><tr><td>4443</td><td>Sansan Inc.</td><td>Norihiro Miyazaki</td><td>8%</td><td>6%</td><td>-8%</td><td>30%</td><td>-10%</td><td>-10%</td></tr><tr><td>4369</td><td>Tri Chemical Laboratories Inc</td><td>Atsushi Ikeda</td><td>-5%</td><td>-7%</td><td>-8%</td><td>25%</td><td>29%</td><td>29%</td></tr><tr><td>5805</td><td>SWCC</td><td>Ryo Harada</td><td>-6%</td><td>-2%</td><td>-9%</td><td>5%</td><td>30%</td><td>30%</td></tr><tr><td>4922</td><td>Kose Holdings</td><td>Takashi Miyazaki</td><td>0%</td><td>-3%</td><td>-10%</td><td>-17%</td><td>-4%</td><td>-4%</td></tr><tr><td>5253</td><td>Cover Corp.</td><td>Norihiro Miyazaki</td><td>14%</td><td>-3%</td><td>-14%</td><td>-1%</td><td>-9%</td><td>-9%</td></tr><tr><td>5032</td><td>ANYCOLOR</td><td>Norihiro Miyazaki</td><td>10%</td><td>-3%</td><td>-22%</td><td>-25%</td><td>-54%</td><td>-54%</td></tr></table>

Exhibit 4: GS covered SMID stocks by analyst, 1M performance and consensus valuations
Data as of Jun 30 2026

<table><tr><td>Ticker</td><td>Name</td><td>Analyst</td><td>1M price return</td><td>P/B</td><td>P/E NTM</td><td>ROE FY26E</td><td>DY FY26E</td></tr><tr><td>4483</td><td>JMDC</td><td>Akinori Ueda, Ph.D.</td><td>1%</td><td>2.3</td><td>21.9</td><td>8.6</td><td>0.7</td></tr><tr><td>4587</td><td>PeptiDream</td><td>Akinori Ueda, Ph.D.</td><td>-4%</td><td>2.7</td><td>9.0</td><td>30.4</td><td>0.0</td></tr><tr><td>4205</td><td>Zeon</td><td>Atsushi Ikeda</td><td>8%</td><td>1.2</td><td>13.3</td><td>9.5</td><td>3.3</td></tr><tr><td>4202</td><td>Daicel</td><td>Atsushi Ikeda</td><td>3%</td><td>1.0</td><td>9.9</td><td>8.7</td><td>4.9</td></tr><tr><td>4061</td><td>Denka</td><td>Atsushi Ikeda</td><td>-3%</td><td>1.2</td><td>19.6</td><td>6.9</td><td>2.3</td></tr><tr><td>4369</td><td>Tri Chemical Laboratories Inc.</td><td>Atsushi Ikeda</td><td>-8%</td><td>3.1</td><td>20.0</td><td>14.4</td><td>1.1</td></tr><tr><td>3774</td><td>Internet Initiative Japan</td><td>Chikai Tanaka, CFA</td><td>3%</td><td>3.6</td><td>20.5</td><td>16.3</td><td>1.4</td></tr><tr><td>3994</td><td>Money Forward</td><td>Chikai Tanaka, CFA</td><td>1%</td><td>5.8</td><td>102.2</td><td>2.7</td><td>0.0</td></tr><tr><td>3697</td><td>SHIFT</td><td>Chikai Tanaka, CFA</td><td>-4%</td><td>4.5</td><td>12.6</td><td>21.7</td><td>0.0</td></tr><tr><td>4478</td><td>freee K.K.</td><td>Chikai Tanaka, CFA</td><td>-5%</td><td>5.8</td><td>34.9</td><td>4.0</td><td>0.0</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>Daiki Takayama</td><td>36%</td><td>7.3</td><td>80.7</td><td>7.7</td><td>0.5</td></tr><tr><td>6592</td><td>Mabuchi Motor</td><td>Daiki Takayama</td><td>1%</td><td>1.1</td><td>17.9</td><td>6.2</td><td>3.2</td></tr><tr><td>6770</td><td>Alps Alpine</td><td>Daiki Takayama</td><td>-6%</td><td>0.9</td><td>13.5</td><td>6.3</td><td>3.2</td></tr><tr><td>7988</td><td>Nifco Inc.</td><td>Kota Yuzawa</td><td>7%</td><td>1.5</td><td>11.7</td><td>12.1</td><td>2.5</td></tr><tr><td>6674</td><td>GS Yuasa Corp.</td><td>Kota Yuzawa</td><td>-1%</td><td>1.6</td><td>15.6</td><td>10.0</td><td>1.6</td></tr><tr><td>6966</td><td>Mitsui High-tec Inc.</td><td>Kota Yuzawa</td><td>-7%</td><td>1.5</td><td>16.2</td><td>10.0</td><td>2.0</td></tr><tr><td>3116</td><td>Toyota Boshoku</td><td>Kota Yuzawa</td><td>-7%</td><td>0.8</td><td>7.8</td><td>9.6</td><td>4.1</td></tr><tr><td>8304</td><td>Aozora Bank</td><td>Makoto Kuroda</td><td>2%</td><td>0.8</td><td>13.1</td><td>5.7</td><td>3.7</td></tr><tr><td>8570</td><td>Aeon Financial Service Co.</td><td>Makoto Kuroda</td><td>-3%</td><td>0.7</td><td>14.1</td><td>4.3</td><td>3.6</td></tr><tr><td>7383</td><td>Net Protections Holdings</td><td>Makoto Kuroda</td><td>-4%</td><td>1.6</td><td>14.8</td><td>9.9</td><td>0.0</td></tr><tr><td>9616</td><td>Kyoritsu Maintenance</td><td>Norihiro Miyazaki</td><td>21%</td><td>1.9</td><td>14.5</td><td>13.2</td><td>1.5</td></tr><tr><td>2222</td><td>Kotobuki Spirits Co.</td><td>Norihiro Miyazaki</td><td>19%</td><td>8.0</td><td>25.8</td><td>27.1</td><td>1.5</td></tr><tr><td>7721</td><td>Tokyo Keiki</td><td>Norihiro Miyazaki</td><td>5%</td><td>2.2</td><td>20.0</td><td>10.7</td><td>0.8</td></tr><tr><td>9706</td><td>Japan Airport Terminal</td><td>Norihiro Miyazaki</td><td>4%</td><td>2.2</td><td>18.1</td><td>11.9</td><td>1.9</td></tr><tr><td>4194</td><td>Visional</td><td>Norihiro Miyazaki</td><td>-1%</td><td>3.8</td><td>16.0</td><td>22.9</td><td>0.0</td></tr><tr><td>7014</td><td>Namura Shipbuilding Co.</td><td>Norihiro Miyazaki</td><td>-5%</td><td>1.8</td><td>10.3</td><td>16.2</td><td>1.7</td></tr><tr><td>3923</td><td>Rakus Co.</td><td>Norihiro Miyazaki</td><td>-6%</td><td>12.9</td><td>16.7</td><td>72.4</td><td>0.7</td></tr><tr><td>4443</td><td>Sansan Inc.</td><td>Norihiro Miyazaki</td><td>-8%</td><td>10.9</td><td>21.2</td><td>37.1</td><td>0.1</td></tr><tr><td>5253</td><td>Cover Corp.</td><td>Norihiro Miyazaki</td><td>-14%</td><td>4.5</td><td>12.7</td><td>31.2</td><td>0.0</td></tr><tr><td>5032</td><td>ANYCOLOR</td><td>Norihiro Miyazaki</td><td>-22%</td><td>5.0</td><td>8.2</td><td>51.1</td><td>3.7</td></tr><tr><td>6622</td><td>Daihen</td><td>Ryo Harada</td><td>14%</td><td>2.8</td><td>23.3</td><td>10.9</td><td>1.3</td></tr><tr><td>6508</td><td>Meidensha</td><td>Ryo Harada</td><td>-3%</td><td>2.5</td><td>20.1</td><td>12.1</td><td>1.6</td></tr><tr><td>6754</td><td>Anritsu</td><td>Ryo Harada</td><td>-3%</td><td>4.2</td><td>36.0</td><td>10.9</td><td>1.2</td></tr><tr><td>5805</td><td>SWCC</td><td>Ryo Harada</td><td>-9%</td><td>4.1</td><td>18.8</td><td>19.4</td><td>2.0</td></tr><tr><td>7581</td><td>Saizeriya</td><td>Sho Kawano</td><td>1%</td><td>2.1</td><td>18.8</td><td>10.3</td><td>0.6</td></tr><tr><td>6728</td><td>Ulvac</td><td>Shuhei Nakamura</td><td>9%</td><td>2.2</td><td>21.1</td><td>8.7</td><td>1.6</td></tr><tr><td>6951</td><td>JEOL</td><td>Shuhei Nakamura</td><td>5%</td><td>2.5</td><td>16.4</td><td>14.6</td><td>1.7</td></tr><tr><td>4912</td><td>Lion</td><td>Takashi Miyazaki</td><td>6%</td><td>1.5</td><td>18.3</td><td>7.8</td><td>2.0</td></tr><tr><td>2229</td><td>Calbee Inc</td><td>Takashi Miyazaki</td><td>2%</td><td>1.7</td><td>19.6</td><td>8.9</td><td>2.3</td></tr><tr><td>4922</td><td>Kose Holdings</td><td>Takashi Miyazaki</td><td>-10%</td><td>1.0</td><td>22.8</td><td>4.0</td><td>3.0</td></tr><tr><td>6055</td><td>Japan Material</td><td>Takeru Adachi</td><td>25%</td><td>4.2</td><td>22.8</td><td>17.3</td><td>1.2</td></tr><tr><td>6254</td><td>NOM Micro Science</td><td>Takeru Adachi</td><td>7%</td><td>4.8</td><td>19.7</td><td>25.2</td><td>1.6</td></tr><tr><td>6432</td><td>Takeuchi MFG</td><td>Takeru Adachi</td><td>4%</td><td>1.7</td><td>12.2</td><td>12.9</td><td>3.1</td></tr><tr><td>6407</td><td>CKD</td><td>Yuichiro Isayama</td><td>14%</td><td>3.3</td><td>26.0</td><td>11.5</td><td>1.4</td></tr><tr><td>6103</td><td>Okuma</td><td>Yuichiro Isayama</td><td>13%</td><td>1.1</td><td>17.2</td><td>6.3</td><td>2.2</td></tr><tr><td>6324</td><td>Harmonic Drive Systems</td><td>Yuichiro Isayama</td><td>0%</td><td>9.2</td><td>114.3</td><td>6.6</td><td>0.3</td></tr></table>

## CY2026 AGM CEO approval ratings in SMID space

Exhibit 5: Median / mean CEO approval ratings
Stocks with 6M ADTV > \$10mn, Mktcap JPY 50bn - 500bn

![](images/a8dcbe7f82ac6f130b4c2d02170484b1cbb0b1c00a93b30f3c0803123fe5cb63.jpg)  
Source: Company Data, Data compiled by GS Global Investment Research  
Exhibit 7: Over 85% of SMID companies now have approval ratings over 80%
ADTV > \$10mn  
Exhibit 6: Disparity historically higher amongst SMIDs
SMID: ADTV > \$10mn, Mktcap JPY50-500bn. Whole universe: ADTV > \$20mn

![](images/da908391ea9e1a49f711ee75f9c84d1c0f9484fc0d71d98de3acd915b739c899.jpg)  
Source: Company Data, Data compiled by GS Global Investment Research  
Exhibit 8: Volatility of yoy changes in SMID CEO approval ratings  
■ % of cos with CEO approval ratings > 80%    ■ > 90%

![](images/79577ecbc9396252bd4809944c7b38d14bf75cee4e632cae92a684479e13b89c.jpg)  
Source: Company Data, Data compiled by GS Global Investment Research  
■ Volatility of YoY changes in AGM CEO approval rating

![](images/cd04e14389bc0bbebd27438b854b34944ddb649d1fab81c5efc3a60c79f33566.jpg)  
Source: Company data, Data compiled by GS Global Investment Research

## Exhibit 9: Top 15 SMID companies by CEO approval rating yoy change

6M ADTV > \$10mn, Mktcap JPY 50bn - 500bn

<table><tr><td>Ticker</td><td>Name</td><td>CY2025</td><td>CY2026</td><td>YoY Change</td></tr><tr><td>2432</td><td>DENA CO LTD</td><td>72%</td><td>95%</td><td>23.1pp</td></tr><tr><td>5985</td><td>SUNCALL CORP</td><td>80%</td><td>99%</td><td>19.2pp</td></tr><tr><td>4902</td><td>KONICA MINOLTA INC</td><td>63%</td><td>81%</td><td>17.8pp</td></tr><tr><td>6055</td><td>JAPAN MATERIAL CO</td><td>77%</td><td>94%</td><td>16.6pp</td></tr><tr><td>3994</td><td>MONEY FORWARD INC</td><td>77%</td><td>89%</td><td>12.3pp</td></tr><tr><td>3350</td><td>METAPLANET INC</td><td>77%</td><td>89%</td><td>12.1pp</td></tr><tr><td>1662</td><td>JAPAN PETROLEUM EX</td><td>82%</td><td>93%</td><td>10.8pp</td></tr><tr><td>4461</td><td>DKS CO. LTD.</td><td>82%</td><td>92%</td><td>10.6pp</td></tr><tr><td>6472</td><td>NTN CORP</td><td>63%</td><td>72%</td><td>8.3pp</td></tr><tr><td>8358</td><td>SURUGA BANK</td><td>90%</td><td>99%</td><td>8.2pp</td></tr><tr><td>1885</td><td>TOA CORP (CONST)</td><td>88%</td><td>96%</td><td>8.0pp</td></tr><tr><td>5301</td><td>TOKAI CARBON CO</td><td>86%</td><td>94%</td><td>7.8pp</td></tr><tr><td>6753</td><td>SHARP CORP</td><td>91%</td><td>99%</td><td>7.7pp</td></tr><tr><td>5715</td><td>FURUKAWA CO</td><td>90%</td><td>98%</td><td>7.4pp</td></tr><tr><td>9065</td><td>SANKYU INC</td><td>87%</td><td>94%</td><td>7.1pp</td></tr></table>

6M ADTV > \$10mn, Mktcap JPY 50bn - 500bn

Source: Company data, Data compiled by GS Global Investment Research

## Exhibit 10: Bottom 15 companies by CEO approval rating yoy change

<table><tr><td>Ticker</td><td>Name</td><td>CY2025</td><td>CY2026</td><td>

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
