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
02 Jun 2026 06:29:35 ET | 12 pages

# Global Semiconductors

Key Takeaways from Computex 2026: Personal AI, AI CPU, and Physical AI

# CITI'S TAKE

During Computex 2026 in Taiwan, Nvidia (Covered by Atif Malik) shared key updates across personal AI, AI CPU, and Physical AI. With RTX Spark and DGX Station loading >10x higher DRAM content vs. traditional laptop/desktop PC, we expect strong upside to DRAM demand. While Vera CPU should drive the demand for server DDR5 and SoCAMM2 thanks to AI inference, the ongoing transition into physical AI should further support the structural growth of memory industry.

Personal AI: RTX Spark, N1X chip, and DGX Station — Nvidia introduced Windows AI PC products during its GTC Taipei keynote, aimed at running large AI models and agents locally rather than in the cloud. RTX Spark, powered by the N1X chip offers 128GB LPDDR5X memory and delivers up to 1 petaflop of FP4 AI performance with 600 GB/s of NVLink-C2C bandwidth. With RTX Spark, users can run AI models with up to roughly 120bn parameters. Nvidia also shared its desktop PC, DGX Station for Windows, which offers up to 748GB memory (252GB HBM3e + 496GB LPDDR5X) and up to 20 petaFLOPS of FP4 compute and can run AI models with up to 1tr parameters. The new NVDA's personal AI PC now loads >10x times more DRAM (128GB) vs. conventional laptop with \~12GB DRAM. Moreover, in terms of desktop PC, Nvidia is now offering DGX station with 748GB memory higher than the avg. DRAM content (600GB) of general server DRAM.

AI CPU: Vera CPU — Nvidia shared that Vera CPU is in full production and delivering roughly 1.8x faster task completion than x86 processors across workloads like agentic AI, reinforcement learning, and data processing. Vera is powered by a custom core called Olympus, featuring 88 cores, and an LPDDR5X memory subsystem with up to 1.2TB/s of bandwidth. It functions as the host CPU offering up to 1.8TB/s of CPU-GPU bandwidth and integrates into BlueField-4 STX AI storage platforms. We project AI CPU demand to drive memory demand for server DDR5 and SoCAMM2, which we highlighted in our recent report: Samsung Electronics (005930.KS): Sustained Memory ASP Momentum; Raise TP to W460k

Physical AI: Launching Cosmos 3 — NVIDIA launched Cosmos 3, an open frontier foundation model for physical AI and the world's first fully open ‘omnimodel.’ Cosmos 3 can natively understand and generate text, images, video, sound, and actions with leading physics accuracy, reducing physical AI training and evaluation cycles from months to days. The models come in three tiers: Cosmos 3 Super (highest accuracy for robotics/AV post-training), Cosmos 3 Nano (fast video and action reasoning), and Cosmos 3 Edge (real-time edge inference).

Implication – As AI inference demand is expanding from GPU to CPU, we project the demand for Server DDR5 and SoCAMM2 to increase further. As we highlighted in our personal AI in-depth report (Global Semiconductors – The AI Hardware Shift in IT Devices: The Era of Personal AI Server Begins), we believe AI memory demand will

# Peter Lee $^{AC}$

+82-2-3705-0720

peter.sc.lee@citi.com

Jayden Oh

+82-2-3705-0747

jayden.oh@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations expand from centralized computing into distributed computing. As such the potential upside for Korea memory suppliers, such as Samsung Electronics, to benefit is set to become even more pronounced, in our view.

# NVIDIA Corp

(NVDA.O; US\$224.36; 1; 01 Jun 26; 16:00)

# Valuation

Our price target for NVDA of \$300 is based on \~28x P/E on C27E earnings power of \~\$11.9 (incl. SBC) discounted back. Our 28x P/E multiple is in-line with 3 year average.

# Risks

Downside risks to the attainment of our target price include: 1) competition on gaming could drive the stock lower if Nvidia loses market share; 2) slower-than-expected adoption of new platforms can drive lower data center and gaming sales; 3) lumpiness in auto and data center markets can add volatility to the stock/multiple; and 4) cryptomining impact on gaming sales.

# Samsung Electronics

(005930.KS; W360500.0; 1; 02 Jun 26; 15:45)

# Valuation

Our 12-month target price for Samsung of W460,000 is derived using a sum-of-the-parts (SOTP) methodology, based on 2026E EBITDA. In calculating total operating value, we reference global peers in assigning fair-value EV/EBITDA multiples for the five main divisions (7.9x for Memory, 4.1x for Foundry, 0.5x for Display Panel, 4.8x for Mobile and 2.0x for Consumer Electronics), in line with trading multiples of relevant peer companies.

# Risks

Downside risks that could prevent the shares from reaching our target price include: 1) Longer-than-expected approval delay in HBM shipment to its key customers; 2) PC sales weaken more than our forecast and NAND demand fails to meet our expectations; 3) aggressive investment by competitors in memory semiconductor/foundry could have a negative impact on prices; 4) competition in the handset market intensifies, reducing SEC's handset margins; 5) any major appreciation of the won would impact SEC's earnings.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

# Appendix A-1

# ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

# IMPORTANT DISCLOSURES

# NVIDIA Corp (NVDA)

Ratings and Target Price History
Fundamental Research

Analyst: Atif Malik

![](images/9726e59ad8893626ac6cd232911e702aea6c8b3c182ab44a1770e3c9d2a8c45d.jpg)

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>17-Jul-23 01:50:06</td><td>1</td><td>*52.00</td><td>46.46</td></tr><tr><td>2</td><td>24-Aug-23 02:36:33</td><td>1</td><td>*63.00</td><td>47.16</td></tr><tr><td>3</td><td>18-Oct-23 00:32:40</td><td>1</td><td>*57.50</td><td>42.20</td></tr><tr><td>4</td><td>22-Feb-24 02:01:24</td><td>1</td><td>*82.00</td><td>78.54</td></tr><tr><td>5</td><td>20-Mar-24 06:26:15</td><td>1</td><td>*103.00</td><td>90.37</td></tr><tr><td>6</td><td>23-May-24 02:55:03</td><td>1</td><td>*126.00</td><td>103.80</td></tr><tr><td>7</td><td>26-Jun-24 05:00:00</td><td>1</td><td>*150.00</td><td>126.40</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>8</td><td>12-Nov-24 08:00:00</td><td>1</td><td>*170.00</td><td>148.29</td></tr><tr><td>9</td><td>21-Nov-24 05:00:00</td><td>1</td><td>*175.00</td><td>146.67</td></tr><tr><td>10</td><td>05-Feb-25 08:00:00</td><td>1</td><td>*163.00</td><td>124.83</td></tr><tr><td>11</td><td>10-Apr-25 22:30:00</td><td>1</td><td>*150.00</td><td>107.57</td></tr><tr><td>12</td><td>29-May-25 01:37:50</td><td>1</td><td>*180.00</td><td>139.19</td></tr><tr><td>13</td><td>07-Jul-25 02:00:00</td><td>1</td><td>*190.00</td><td>158.24</td></tr><tr><td>14</td><td>28-Aug-25 01:41:01</td><td>1</td><td>*210.00</td><td>180.17</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>15</td><td>08-Sep-25 02:00:00</td><td>1</td><td>*200.00</td><td>168.31</td></tr><tr><td>16</td><td>30-Sep-25 04:04:43</td><td>1</td><td>*210.00</td><td>186.58</td></tr><tr><td>17</td><td>10-Nov-25 06:11:57</td><td>1</td><td>*220.00</td><td>199.05</td></tr><tr><td>18</td><td>20-Nov-25 02:46:50</td><td>1</td><td>*270.00</td><td>180.64</td></tr><tr><td>19</td><td>26-Feb-26 02:41:17</td><td>1</td><td>*300.00</td><td>184.89</td></tr></table>

\*Indicates Change   
Rating/target price changes above reflect Eastern Time

# Samsung Electronics (005930.KS)

Ratings and Target Price History
Fundamental Research

Analyst: Peter Lee

![](images/05addd5d7b885beec1132fdb84709e02a03d70ca305b2e2d6b3190e478a3b63a.jpg)

<details>
<summary>line</summary>

| Month-Year | Covered | Not covered |
| ---------- | ------- | ----------- |
| J 2024     | 1       | 2           |
| J 2024     | 3       |             |
| A 2024     | 4       |             |
| S 2024     | 5       |             |
| O 2024     |         |             |
| N 2024     |         |             |
| D 2024     |         |             |
| J 2024     |         |             |
| F 2024     |         |             |
| M 2024     |         |             |
| A 2024     | 6       |             |
| M 2024     |         |             |
| A 2024     |         |             |
| M 2024     |         |             |
| J 2024     |         |             |
| J 2024     |         |             |
| A 2024     |         |             |
| S 2024     | 7       |             |
| O 2024     | 8       |             |
| N 2024     |         |             |
| D 2024     |         |             |
| J 2024     | 9       |             |
| F 2024     |         |             |
| M 2024     |         |             |
| A 2024     |         |             |
| M 2024     |         |             |
| J 2024     |         |             |
| J 2024     |         |             |
| A 2024     |         |             |
| S 2024     |         |             |
| O 2024     |         |             |
| N 2024     |         |             |
| D 2024     |         |             |
| J 2024     |         |             |
| J 2024     |         |             |
| A 2024     |         |             |
| S 2024     |         |             |
| O 2024     |         |             |
| N 2024     |         |             |
| D 2024     |         [1]  |             |
| J 2024     |         [1]  |             |
| J 2024     |         [1]  |             |
| A 2024     |         [1]  |             |
| S 2024     |         [1]  |             |
| O 2024     |         [1]  |             |
| N 2024     |         [1]  |             |
| D 2024     |         [1]  |             |
| J 2024     |         [1]  |             |
| J 2024     |         [1]  |             |
| A 2024     |         [1]  |             |
| S 2024     |         [1]  |             |
| O 2024     |         [3]  |             |
| N 2024     |         [3]  |             |
| D 2024     |         [3]  |             |
| J 2024     |         [3]  |             |
| J 2024     |         [3]  |             |
| A 2024     |         [3]  |             |
| S 2024     |         [3]  |             |
| O 2024     |         [3]  |             |
| N 2024     |         [3]  |             |
| D 2024     |         [3]  |             |
| J 2024     |         [3]  |             |
| J 2024     |         [3]  |             |
| A 2024     | [1]   |             |
| S 2024     | [1]   |             |
| O 2024     | [1]   |             |
| N 2024     | [1]   |             |
| D 2024     | [1]   |             |
| J 2024     | [1]   |             |
| J 2024     | [1]   |             |
| A 2024     | [1]   |             |
| S 2024     | [1]   |             |
| O 2024     | [1]   |             |
| N 2024     | [1]   |             |
| D 2024     | [1]   |             |
| J 2024     | [1]   |             |
|
| J 2024     | [1]   |             |
| A 2024     | [1]   |             |
| S 2024     | [1]   |             |
| O 2024     | [1]   |             |
| N 2024     | [1]   |             |
| D 2024     | [1]   |             |
| J 1999     | [1]   ]          |               |
| J 1999     | [1]   ]          |               |
| A 1999     | [1]   ]          |               |
| S 1999     | [1]   ]          |               |
| O 1999     | [1]   ]          |               |
| N 1999     | [1]   ]          |               |
| D 1999     | [1]   ]          |               |
| J 1999     | [1]   ]          |               |
| J 1999     | [1]   ]          |               |
| A 1999     | [1]   ]          |               |
| S 1999     | [1]   ]          |               |
| O 1999     | [1]   ]          |               |
| N 1999     }<fcel>[1]   ]          :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :              :            :            :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :                :        /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                  /                 /                        :
                          (Note: The actual data for some series will vary due to the random nature of the data generation.)    }
                          (Note: The data for some series will be truncated here)    }
                          (Note: The data for some series will be truncated here)    }
                          (Note: The data for some series will be truncated here)    }
                          (Note: The data for some series will be truncated here)    }
                          (Note: The data for some series will be truncated here)    }
                          (Note: The data for some series will be truncated here)    }
                          (Note: The data for some series will be truncated here)    }
                          ...                         ...                     ...
</details>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>31-May-23 03:36:58</td><td>1</td><td>*100,000.00</td><td>71,400.00</td></tr><tr><td>2</td><td>28-Jun-23 08:19:44</td><td>1</td><td>*105,000.00</td><td>72,700.00</td></tr><tr><td>3</td><td>27-Jul-23 05:53:47</td><td>1</td><td>*110,000.00</td><td>71,700.00</td></tr><tr><td>4</td><td>31-Aug-23 06:54:46</td><td>1</td><td>*120,000.00</td><td>66,900.00</td></tr><tr><td>5</td><td>22-Sep-23 09:53:22</td><td>1</td><td>*110,000.00</td><td>68,800.00</td></tr><tr><td>6</td><td>01-Apr-24 05:23:20</td><td>1</td><td>*120,000.00</td><td>82,000.00</td></tr><tr><td>7</td><td>09-Sep-24 02:31:35</td><td>1</td><td>*110,000.00</td><td>67,500.00</td></tr><tr><td>8</td><td>02-Oct-24 05:16:51</td><td>1</td><td>*97,000.00</td><td>61,300.00</td></tr><tr><td>9</td><td>26-Dec-24 07:42:50</td><td>1</td><td>*87,000.00</td><td>53,600.00</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>10</td><td>31-Dec-24 06:21:22</td><td>1</td><td>*83,000.00</td><td>53,200.00</td></tr><tr><td>11</td><td>16-Jul-25 05:08:04</td><td>1</td><td>*90,000.00</td><td>64,700.00</td></tr><tr><td>12</td><td>31-Jul-25 02:49:57</td><td>1</td><td>*100,000.00</td><td>71,400.00</td></tr><tr><td>13</td><td>08-Sep-25 09:30:31</td><td>1</td><td>*110,000.00</td><td>70,100.00</td></tr><tr><td>14</td><td>22-Sep-25 05:57:03</td><td>1</td><td>*120,000.00</td><td>83,500.00</td></tr><tr><td>15</td><td>14-Oct-25 07:05:40</td><td>1</td><td>*133,000.00</td><td>91,600.00</td></tr><tr><td>16</td><td>20-Oct-25 06:25:10</td><td>1</td><td>*145,000.00</td><td>98,100.00</td></tr><tr><td>17</td><td>30-Oct-25 11:44:04</td><td>1</td><td>*150,000.00</td><td>104,100.00</td></tr><tr><td>18</td><td>23-Nov-25 10:07:18</td><td>1</td><td>*170,000.00</td><td>94,800.00</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>19</td><td>02-Jan-26 02:41:08</td><td>1</td><td>*200,000.00</td><td>128,500.00</td></tr><tr><td>20</td><td>26-Jan-26 09:32:20</td><td>1</td><td>*240,000.00</td><td>152,100.00</td></tr><tr><td>21</td><td>24-Feb-26 05:11:17</td><td>1</td><td>*280,000.00</td><td>200,000.00</td></tr><tr><td>22</td><td>02-Apr-26 07:54:27</td><td>1</td><td>*300,000.00</td><td>178,400.00</td></tr><tr><td>23</td><td>07-Ap

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be

reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
