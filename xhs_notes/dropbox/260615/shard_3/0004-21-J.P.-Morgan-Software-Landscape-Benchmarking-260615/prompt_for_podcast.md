你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Software Landscape Benchmarking

## Security Software Technology

Brian Essex, CFA

(1-212) 622-5990

brian.essex@JPM.com

JPM Securities LLC

John Lee

(1-212) 622-6064

John.h.lee@JPM.com

JPM Securities LLC

Alex Isaac

(1-212) 622-9159

alex.isaac@JPM.com

JPM Securities LLC

The authors wish to thank Rachit Agrawal, of the JPM Global Research Center, for contributions to this report.

This material is provided for information only and is not intended as a recommendation or an offer or solicitation for the purchase or sale of any security or financial instrument. This material is not a research report, although it may refer to information and data contained in JPM published research reports or models from all JPM affiliated regions. Opinions and estimates constitute our judgment as of the date of this material and are subject to change without notice. Past performance is not indicative of future results. Securities, financial instruments or strategies mentioned herein may not be suitable for all investors. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein. Please refer to the most recent published research or model for complete information on the specific security or financial instrument mentioned in this material, including important disclosures and Research Analysts' certifications. © 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is

## Software Universe Comps Overview – As of 6/12/26

<table><tr><td></td><td colspan="2">EV/Sales</td><td colspan="2">EV/Sales/G</td><td colspan="2">EV/EBITDA</td><td colspan="2">EV/FCF</td><td colspan="2">EV/(FCF-SBC)</td><td colspan="2">P/E</td><td rowspan="2">N</td></tr><tr><td>Averages</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td></tr><tr><td>Total</td><td>5.7x</td><td>4.8x</td><td>0.41x</td><td>0.42x</td><td>16.6x</td><td>15.3x</td><td>20.3x</td><td>18.2x</td><td>24.9x</td><td>22.2x</td><td>21.6x</td><td>20.1x</td><td>101</td></tr><tr><td>Large Cap (&gt;$20bn Mkt Cap)</td><td>10.3x</td><td>8.5x</td><td>0.49x</td><td>0.55x</td><td>23.7x</td><td>19.1x</td><td>28.0x</td><td>26.8x</td><td>31.2x</td><td>27.5x</td><td>27.4x</td><td>26.2x</td><td>31</td></tr><tr><td>Mid Cap ($3bn - $20bn Mkt Cap)</td><td>5.0x</td><td>4.3x</td><td>0.37x</td><td>0.33x</td><td>17.3x</td><td>17.0x</td><td>21.5x</td><td>18.2x</td><td>20.8x</td><td>20.0x</td><td>20.8x</td><td>19.6x</td><td>41</td></tr><tr><td>Small Cap (&lt;$3bn Mkt Cap)</td><td>1.9x</td><td>1.7x</td><td>0.40x</td><td>0.38x</td><td>8.6x</td><td>9.4x</td><td>11.4x</td><td>9.4x</td><td>24.4x</td><td>18.9x</td><td>14.2x</td><td>11.3x</td><td>29</td></tr><tr><td>Security &amp; Analytics</td><td>9.2x</td><td>7.6x</td><td>0.51x</td><td>0.51x</td><td>23.7x</td><td>22.2x</td><td>26.8x</td><td>25.7x</td><td>26.6x</td><td>27.9x</td><td>26.0x</td><td>27.8x</td><td>23</td></tr><tr><td>Vertical</td><td>4.7x</td><td>4.1x</td><td>0.36x</td><td>0.39x</td><td>14.6x</td><td>13.7x</td><td>19.7x</td><td>15.8x</td><td>25.6x</td><td>21.5x</td><td>20.6x</td><td>16.0x</td><td>36</td></tr><tr><td>Rule of 40: Growth (&gt;20% y/y)</td><td>13.7x</td><td>11.7x</td><td>0.48x</td><td>0.48x</td><td>25.4x</td><td>12.5x</td><td>34.2x</td><td>44.1x</td><td>34.7x</td><td>37.6x</td><td>30.3x</td><td>20.1x</td><td>12</td></tr><tr><td>Growth (10-19% y/y)</td><td>7.0x</td><td>6.9x</td><td>0.43x</td><td>0.46x</td><td>17.3x</td><td>17.4x</td><td>21.8x</td><td>22.0x</td><td>24.1x</td><td>27.2x</td><td>22.2x</td><td>22.1x</td><td>11</td></tr><tr><td>Growth (&lt;10% y/y)</td><td>4.3x</td><td>5.0x</td><td>0.76x</td><td>0.59x</td><td>9.6x</td><td>13.6x</td><td>11.9x</td><td>16.2x</td><td>16.7x</td><td>21.4x</td><td>13.3x</td><td>17.5x</td><td>6</td></tr></table>

<table><tr><td rowspan="2">Averages</td><td colspan="2">Revenue Growth</td><td colspan="2">Gross Margins</td><td colspan="2">FCF Margins</td><td colspan="2">SBC as % of Rev</td></tr><tr><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td></tr><tr><td>Total</td><td>17%</td><td>14%</td><td>76%</td><td>76%</td><td>20%</td><td>23%</td><td>13%</td><td>12%</td></tr><tr><td>Large Cap (&gt;$20bn Mkt Cap)</td><td>24%</td><td>17%</td><td>76%</td><td>76%</td><td>19%</td><td>24%</td><td>12%</td><td>12%</td></tr><tr><td>Mid Cap ($3bn - $20bn Mkt Cap)</td><td>14%</td><td>13%</td><td>78%</td><td>78%</td><td>25%</td><td>27%</td><td>13%</td><td>12%</td></tr><tr><td>Small Cap (&lt;$3bn Mkt Cap)</td><td>7%</td><td>9%</td><td>72%</td><td>72%</td><td>15%</td><td>16%</td><td>13%</td><td>13%</td></tr><tr><td>Security &amp; Analytics</td><td>17%</td><td>15%</td><td>80%</td><td>80%</td><td>15%</td><td>14%</td><td>15%</td><td>14%</td></tr><tr><td>Vertical</td><td>16%</td><td>13%</td><td>72%</td><td>72%</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td></tr><tr><td>Rule of 40: Growth (&gt;20% y/y)</td><td>39%</td><td>36%</td><td>75%</td><td>75%</td><td>6%</td><td>-7%</td><td>11%</td><td>9%</td></tr><tr><td>Growth (10-19% y/y)</td><td>16%</td><td>15%</td><td>79%</td><td>79%</td><td>29%</td><td>32%</td><td>9%</td><td>10%</td></tr><tr><td>Growth (&lt;10% y/y)</td><td>7%</td><td>7%</td><td>81%</td><td>80%</td><td>38%</td><td>34%</td><td>11%</td><td>9%</td></tr></table>

## Security Software & Analytics Comps Table – As of 6/12/26

<table><tr><td>Company</td><td>Market Cap</td><td>Ticker</td><td>Rating</td></tr><tr><td>C3.ai Inc</td><td>1,547</td><td>AI</td><td>UW</td></tr><tr><td>Cellebrite DI Ltd</td><td>3,329</td><td>CLBT</td><td>OW</td></tr><tr><td>Check Point Software</td><td>13,163</td><td>CHKP</td><td>OW</td></tr><tr><td>Crowdstrike Holdings Inc</td><td>176,081</td><td>CRWD</td><td>OW</td></tr><tr><td>Elastic</td><td>6,356</td><td>ESTC</td><td>OW</td></tr><tr><td>Fortinet Inc</td><td>108,672</td><td>FTNT</td><td>UW</td></tr><tr><td>Gitlab Inc</td><td>4,766</td><td>GTLB</td><td>N</td></tr><tr><td>IBM</td><td>258,329</td><td>IBM</td><td>N</td></tr><tr><td>JFrog Ltd</td><td>9,737</td><td>FROG</td><td>OW</td></tr><tr><td>Netskope</td><td>3,620</td><td>NTSK</td><td>OW</td></tr><tr><td>Okta Inc</td><td>21,404</td><td>OKTA</td><td>OW</td></tr><tr><td>Palo Alto Networks Inc</td><td>225,653</td><td>PANW</td><td>OW</td></tr><tr><td>Qualys Inc</td><td>3,969</td><td>QLYS</td><td>UW</td></tr><tr><td>Rapid7 Inc</td><td>552</td><td>RPD</td><td>N</td></tr><tr><td>SailPoint Inc</td><td>8,256</td><td>SAIL</td><td>OW</td></tr><tr><td>SentinelOne Inc</td><td>5,079</td><td>S</td><td>N</td></tr><tr><td>Tenable Holdings Inc</td><td>3,154</td><td>TENB</td><td>OW</td></tr><tr><td>Varonis Systems Inc</td><td>4,429</td><td>VRNS</td><td>OW</td></tr><tr><td>Zscaler Inc</td><td>21,416</td><td>ZS</td><td>OW</td></tr></table>

<table><tr><td colspan="2">Pricing</td></tr><tr><td>Price6/12/2026</td><td>JPMPT</td></tr><tr><td>10.90</td><td>7.00</td></tr><tr><td>12.84</td><td>20.00</td></tr><tr><td>124.06</td><td>135.00</td></tr><tr><td>682.80</td><td>800.00</td></tr><tr><td>60.35</td><td>80.00</td></tr><tr><td>146.30</td><td>75.00</td></tr><tr><td>27.79</td><td>32.00</td></tr><tr><td>272.24</td><td>270.00</td></tr><tr><td>77.69</td><td>76.00</td></tr><tr><td>9.04</td><td>14.00</td></tr><tr><td>116.29</td><td>120.00</td></tr><tr><td>279.62</td><td>326.00</td></tr><tr><td>111.24</td><td>87.00</td></tr><tr><td>7.14</td><td>7.00</td></tr><tr><td>14.62</td><td>22.00</td></tr><tr><td>14.85</td><td>18.00</td></tr><tr><td>26.80</td><td>35.00</td></tr><tr><td>33.34</td><td>39.00</td></tr><tr><td>129.52</td><td>205.00</td></tr></table>

<table><tr><td colspan="2"></td></tr><tr><td colspan="2">EV/Sales</td></tr><tr><td>CY26</td><td>CY27</td></tr><tr><td>4.3x</td><td>4.0x</td></tr><tr><td>5.1x</td><td>4.2x</td></tr><tr><td>3.8x</td><td>3.6x</td></tr><tr><td>29.0x</td><td>23.8x</td></tr><tr><td>2.9x</td><td>2.5x</td></tr><tr><td>13.5x</td><td>12.3x</td></tr><tr><td>3.1x</td><td>2.6x</td></tr><tr><td>4.2x</td><td>4.0x</td></tr><tr><td>14.2x</td><td>12.0x</td></tr><tr><td>3.7x</td><td>3.0x</td></tr><tr><td>6.0x</td><td>5.4x</td></tr><tr><td>17.1x</td><td>14.5x</td></tr><tr><td>4.5x</td><td>4.2x</td></tr><tr><td>0.9x</td><td>0.9x</td></tr><tr><td>6.2x</td><td>5.2x</td></tr><tr><td>3.6x</td><td>3.0x</td></tr><tr><td>2.9x</td><td>2.7x</td></tr><tr><td>5.0x</td><td>4.1x</td></tr><tr><td>5.0x</td><td>4.2x</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="2">EV/Sales/G</td></tr><tr><td>CY26</td><td>CY27</td></tr><tr><td></td><td>-0.11x</td><td>0.56x</td></tr><tr><td></td><td>0.25x</td><td>0.21x</td></tr><tr><td></td><td>1.32x</td><td>0.59x</td></tr><tr><td></td><td>1.22x</td><td>1.11x</td></tr><tr><td></td><td>0.16x</td><td>0.15x</td></tr><tr><td></td><td>0.85x</td><td>1.25x</td></tr><tr><td></td><td>0.17x</td><td>0.16x</td></tr><tr><td></td><td>0.64x</td><td>0.76x</td></tr><tr><td></td><td>0.71x</td><td>0.63x</td></tr><tr><td></td><td>0.14x</td><td>0.13x</td></tr><tr><td></td><td>0.60x</td><td>0.54x</td></tr><tr><td></td><td>0.61x</td><td>0.81x</td></tr><tr><td></td><td>0.52x</td><td>0.58x</td></tr><tr><td></td><td>-0.42x</td><td>0.85x</td></tr><tr><td></td><td>0.32x</td><td>0.28x</td></tr><tr><td></td><td>0.18x</td><td>0.17x</td></tr><tr><td></td><td>0.33x</td><td>0.32x</td></tr><tr><td></td><td>0.27x</td><td>0.19x</td></tr><tr><td></td><td>0.22x</td><td>0.24x</td></tr></table>

<table><tr><td colspan="2">EV/EBITDA</td></tr><tr><td>CY26</td><td>CY27</td></tr><tr><td>---</td><td>---</td></tr><tr><td>19.0x</td><td>15.5x</td></tr><tr><td>9.4x</td><td>8.8x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>16.8x</td><td>12.9x</td></tr><tr><td>37.4x</td><td>33.7x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>14.8x</td><td>14.1x</td></tr><tr><td>---</td><td>53.5x</td></tr><tr><td>---</td><td>73.4x</td></tr><tr><td>22.7x</td><td>14.8x</td></tr><tr><td>56.5x</td><td>45.2x</td></tr><tr><td>10.1x</td><td>9.5x</td></tr><tr><td>4.9x</td><td>4.8x</td></tr><tr><td>31.3x</td><td>25.4x</td></tr><tr><td>22.7x</td><td>16.9x</td></tr><tr><td>11.4x</td><td>10.2x</td></tr><tr><td>---</td><td>30.1x</td></tr><tr><td>18.6x</td><td>15.5x</td></tr></table>

<table><tr><td colspan="2">EV/FCF</td></tr><tr><td>CY26</td><td>CY27</td></tr><tr><td>---</td><td>---</td></tr><tr><td>16.4x</td><td>13.5x</td></tr><tr><td>8.9x</td><td>8.2x</td></tr><tr><td>---</td><td>74.8x</td></tr><tr><td>15.5x</td><td>14.0x</td></tr><tr><td>40.8x</td><td>38.3x</td></tr><tr><td>19.2x</td><td>13.7x</td></tr><tr><td>19.0x</td><td>17.7x</td></tr><tr><td>59.7x</td><td>40.1x</td></tr><tr><td>---</td><td>40.6x</td></tr><tr><td>21.8x</td><td>18.7x</td></tr><tr><td>47.4x</td><td>35.2x</td></tr><tr><td>10.8x</td><td>11.0x</td></tr><tr><td>5.5x</td><td>5.7x</td></tr><tr><td>39.8x</td><td>24.4x</td></tr><tr><td>55.7x</td><td>35.6x</td></tr><tr><td>11.7x</td><td>10.3x</td></tr><tr><td>36.2x</td><td>24.5x</td></tr><tr><td>22.0x</td><td>15.4x</td></tr></table>

<table><tr><td colspan="2">EV/(FCF-SBC)</td></tr><tr><td>CY26</td><td>CY27</td></tr><tr><td>---</td><td>---</td></tr><tr><td>22.2x</td><td>18.1x</td></tr><tr><td>11.2x</td><td>10.4x</td></tr><tr><td>--</td><td>--</td></tr><tr><td>---</td><td>---</td></tr><tr><td>46.9x</td><td>44.8x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>20.9x</td><td>19.1x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>---</td><td>---</td></tr><tr><td>49.5x</td><td>37.4x</td></tr><tr><td>---</td><td>55.9x</td></tr><tr><td>15.3x</td><td>16.6x</td></tr><tr><td>20.2x</td><td>30.1x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>---</td><td>---</td></tr><tr><td>37.5x</td><td>29.1x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>---</td><td>---</td></tr></table>

<table><tr><td colspan="2">P/E</td></tr><tr><td>CY26</td><td>CY27</td></tr><tr><td>---</td><td>---</td></tr><tr><td>22.9x</td><td>19.5x</td></tr><tr><td>11.7x</td><td>10.6x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>20.1x</td><td>16.1x</td></tr><tr><td>46.4x</td><td>43.3x</td></tr><tr><td>34.3x</td><td>28.6x</td></tr><tr><td>22.0x</td><td>20.1x</td></tr><tr><td>---</td><td>62.7x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>30.4x</td><td>26.4x</td></tr><tr><td>---</td><td>64.0x</td></tr><tr><td>14.6x</td><td>13.5x</td></tr><tr><td>4.6x</td><td>4.7x</td></tr><tr><td>45.7x</td><td>37.5x</td></tr><tr><td>40.1x</td><td>29.7x</td></tr><tr><td>13.6x</td><td>11.5x</td></tr><tr><td>---</td><td>42.2x</td></tr><tr><td>29.2x</td><td>24.9x</td></tr></table>

<table><tr><td>Average</td></tr><tr><td>Median</td></tr></table>

<table><tr><td>7.1x</td><td>6.1x</td></tr><tr><td>4.5x</td><td>4.1x</td></tr></table>

<table><tr><td>0.42x</td><td>0.50x</td></tr><tr><td>0.32x</td><td>0.54x</td></tr></table>

<table><tr><td>21.2x</td><td>24.0x</td></tr><tr><td>18.6x</td><td>15.5x</td></tr></table>

<table><tr><td>26.9x</td><td>24.5x</td></tr><tr><td>20.5x</td><td>18.2x</td></tr></table>

<table><tr><td>28.0x</td><td>29.1x</td></tr><tr><td>21.6x</td><td>29.1x</td></tr></table>

<table><tr><td>25.8x</td><td>28.4x</td></tr><tr><td>22.9x</td><td>25.6x</td></tr></table>

<table><tr><td colspan="3">Other Related JPM Coverage</td></tr><tr><td>Dropbox Inc</td><td>6,412 DBX</td><td>N</td></tr><tr><td>Datadog Inc</td><td>83,852 DDOG</td><td>OW</td></tr><tr><td>Dynatrace Inc</td><td>12,181 DT</td><td>OW</td></tr><tr><td>Microsoft Corp</td><td>2,909,059 MSFT</td><td>OW</td></tr><tr><td>Cloudflare Inc</td><td>80,568 NET</td><td>N</td></tr></table>

<table><tr><td>27.09</td><td>25.00</td></tr><tr><td>229.90</td><td>320.00</td></tr><tr><td>40.75</td><td>45.00</td></tr><tr><td>390.74</td><td>550.00</td></tr><tr><td>228.48</td><td>145.00</td></tr></table>

<table><tr><td>3.4x</td><td>3.4x</td></tr><tr><td>18.5x</td><td>15.3x</td></tr><tr><td>4.9x</td><td>4.3x</td></tr><tr><td>8.1x</td><td>6.8x</td></tr><tr><td>28.1x</td><td>21.8x</td></tr></table>

<table><tr><td>-12.07x</td><td>-6.47x</td></tr><tr><td>0.67x</td><td>0.92x</td></tr><tr><td>0.27x</td><td>0.30x</td></tr><tr><td>0.45x</td><td>0.47x</td></tr><tr><td>0.93x</td><td>0.87x</td></tr></table>

<table><tr><td>7.2x</td><td>6.8x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>31.1x</td><td>26.2x</td></tr><tr><td>17.6x</td><td>15.2x</td></tr><tr><td>---</td><td>---</td></tr></table>

<table><tr><td>9.7x</td><td>8.9x</td></tr><tr><td>66.1x</td><td>57.9x</td></tr><tr><td>16.3x</td><td>16.2x</td></tr><tr><td>---</td><td>58.0x</td></tr><tr><td>---</td><td>---</td></tr></table>

<table><tr><td>15.3x</td><td>14.1x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>30.7x</td><td>37.5x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>---</td><td>---</td></tr></table>

<table><tr><td>8.4x</td><td>8.0x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>22.4x</td><td>18.7x</td></tr><tr><td>22.5x</td><td>18.6x</td></tr><tr><td>---</td><td>---</td></tr></table>

<table><tr><td colspan="3">Non-Covered Security, Analytics, and DevOps Coverage</td></tr><tr><td>Atlassian Corp</td><td>23,101 TEAM</td><td>NC</td></tr><tr><td>BlackBerry Ltd</td><td>5,915 BB</td><td>NC</td></tr><tr><td>Commvault Systems Inc</td><td>5,527 CVLT</td><td>NC</td></tr><tr><td>Gen Digital Inc</td><td>14,811 GEN</td><td>NC</td></tr><tr><td>MongoDB Inc</td><td>27,943 MDB</td><td>NC</td></tr><tr><td>N-able Inc/US</td><td>602 NABL</td><td>NC</td></tr><tr><td>Palantir Technologies Inc</td><td>329,053 PLTR</td><td>NC</td></tr><tr><td>Rubrik Inc</td><td>13,888 RBRK</td><td>NC</td></tr></table>

<table><tr><td>88.52</td><td>--</td></tr><tr><td>9.19</td><td>--</td></tr><tr><td>127.76</td><td>--</td></tr><tr><td>24.32</td><td>--</td></tr><tr><td>342.52</td><td>--</td></tr><tr><td>3.21</td><td>--</td></tr><tr><td>127.99</td><td>--</td></tr><tr><td>68.19</td><td>--</td></tr></table>

<table><tr><td>3.3x</td><td>2.9x</td></tr><tr><td>9.8x</td><td>9.1x</td></tr><tr><td>4.3x</td><td>3.9x</td></tr><tr><td>4.3x</td><td>4.0x</td></tr><tr><td>8.6x</td><td>7.3x</td></tr><tr><td>1.6x</td><td>1.5x</td></tr><tr><td>41.5x</td><td>28.6x</td></tr><tr><td>8.1x</td><td>6.6x</td></tr></table>

<table><tr><td>0.16x</td><td>0.19x</td></tr><tr><td>0.98x</td><td>1.15x</td></tr><tr><td>0.40x</td><td>0.35x</td></tr><tr><td>0.37x</td><td>0.60x</td></tr><tr><td>0.42x</td><td>0.41x</td></tr><tr><td>0.18x</td><td>0.17x</td></tr><tr><td>0.57x</td><td>0.63x</td></tr><tr><td>0.32x</td><td>0.31x</td></tr></table>

<table><tr><td>10.6x</td><td>9.6x</td></tr><tr><td>51.5x</td><td>40.9x</td></tr><tr><td>20.5x</td><td>17.7x</td></tr><tr><td>9.0x</td><td>7.7x</td></tr><tr><td>41.8x</td><td>33.6x</td></tr><tr><td>5.2x</td><td>4.6x</td></tr><tr><td>71.6x</td><td>49.0x</td></tr><tr><td>---</td><td>---</td></tr></table>

<table><tr><td>12.4x</td><td>9.7x</td></tr><tr><td>68.6x</td><td>46.1x</td></tr><tr><td>19.7x</td><td>19.2x</td></tr><tr><td>13.4x</td><td>12.2x</td></tr><tr><td>46.6x</td><td>37.7x</td></tr><tr><td>10.4x</td><td>9.5x</td></tr><tr><td>---</td><td>52.7x</td></tr><tr><td>44.6x</td><td>32.1x</td></tr></table>

<table><tr><td>---</td><td>44.1x</td></tr><tr><td>---</td><td>56.8x</td></tr><tr><td>35.9x</td><td>35.4x</td></tr><tr><td>15.6x</td><td>14.0x</td></tr><tr><td>---</td><td>---</td></tr><tr><td>25.1x</td><td>22.8x</td></tr><tr><td>---</td><td>69.3x</td></tr><tr><td>---</td><td>---</td></tr></table>

<table><tr><td>14.6x</td><td>13.2x</td></tr><tr><td>51.9x</td><td>46.4x</td></tr><tr><td>25.4x</td><td>21.9x</td></tr><tr><td>8.7x</td><td>7.6x</td></tr><tr><td>55.8x</td><td>46.7x</td></tr><tr><td>7.7x</td><td>6.7x</td></tr><tr><td>---</td><td>62.0x</td></tr><tr><td>---</td><td>---</td></tr></table>

## Most Expensive and Least Expensive Stock Performance

YTD Performance – 5 Most Expensive and 5 Least Expensive (>20% y/y Growth) Software Stocks\*  
![](images/2ea5ccc4e25967ee87d1c000b865c4d76acb764247e26bb1e52690fd6a5c8b1b.jpg)

<details>
<summary>line chart</summary>

| Date       | Top 5 Expensive Performance Avg | Least 5 Expensive (>20% y/y Growth) Performance Avg | SPX Index |
|------------|----------------------------------|-----------------------------------------------------|---------|
| 31-Dec-25  | ~0%                              | ~0%                                                 | ~0%     |
| 7-Jan-26   | ~-5%                             | ~-

[中间内容因长度限制已省略]

<td>Cory A Carpenter</td><td>OW</td></tr><tr><td>Veeva Systems</td><td>VEEV</td><td>Alexei Gogolev</td><td>OW</td></tr><tr><td>Varonis Systems</td><td>VRNS</td><td>Brian Essex</td><td>OW</td></tr><tr><td>ZoomInfo</td><td>GTM</td><td>Arti Vula</td><td>OW</td></tr><tr><td>Zoom</td><td>ZM</td><td>Arti Vula</td><td>N</td></tr><tr><td>Zscaler</td><td>ZS</td><td>Brian Essex</td><td>OW</td></tr></table>

<table><tr><td colspan="3">Pricing</td></tr><tr><td>Price 6/12/2026</td><td>Market Cap</td><td>Current EV</td></tr><tr><td>108.24</td><td>141,075</td><td>135,332</td></tr><tr><td>232.78</td><td>80,400</td><td>79,727</td></tr><tr><td>453.89</td><td>87,212</td><td>94,742</td></tr><tr><td>67.68</td><td>16,758</td><td>23,657</td></tr><tr><td>88.52</td><td>23,101</td><td>22,953</td></tr><tr><td>26.80</td><td>3,154</td><td>3,147</td></tr><tr><td>204.08</td><td>32,195</td><td>30,842</td></tr><tr><td>298.84</td><td>12,894</td><td>12,548</td></tr><tr><td>18.75</td><td>3,659</td><td>4,957</td></tr><tr><td>130.80</td><td>33,264</td><td>30,887</td></tr><tr><td>45.91</td><td>2,588</td><td>1,692</td></tr><tr><td>50.25</td><td>5,093</td><td>4,293</td></tr><tr><td>159.54</td><td>26,482</td><td>19,169</td></tr><tr><td>33.34</td><td>4,429</td><td>3,643</td></tr><tr><td>10.03</td><td>3,034</td><td>4,176</td></tr><tr><td>93.68</td><td>28,126</td><td>20,405</td></tr><tr><td>129.52</td><td>21,416</td><td>17,877</td></tr></table>

<table><tr><td colspan="13">Valuation</td></tr><tr><td colspan="2">EV/Sales</td><td colspan="2">EV/Sales/G</td><td colspan="2">EV/EBITDA</td><td colspan="2">EV/FCF</td><td colspan="2">EV/(FCF-SBC)</td><td colspan="2">P/E</td><td></td></tr><tr><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td>CY26E</td><td>CY27E</td><td></td></tr><tr><td>9.1x</td><td>7.4x</td><td>0.30x</td><td>0.32x</td><td>48.5x</td><td>37.7x</td><td>50.3x</td><td>40.6x</td><td>64.3x</td><td>50.8x</td><td>57.6x</td><td>46.5x</td><td></td></tr><tr><td>13.1x</td><td>10.4x</td><td>0.42x</td><td>0.45x</td><td>53.6x</td><td>36.8x</td><td>56.2x</td><td>45.4x</td><td>---</td><td>---</td><td>---</td><td>---</td><td></td></tr><tr><td>9.6x</td><td>8.7x</td><td>0.41x</td><td>0.81x</td><td>24.0x</td><td>18.3x</td><td>24.4x</td><td>27.4x</td><td>32.5x</td><td>--</td><td>30.4x</td><td>---</td><td></td></tr><tr><td>3.5x</td><td>3.3x</td><td>0.40x</td><td>0.49x</td><td>8.8x</td><td>7.8x</td><td>15.6x</td><td>13.6x</td><td>17.7x</td><td>15.1x</td><td>9.8x</td><td>8.6x</td><td></td></tr><tr><td>3.3x</td><td>2.9x</td><td>0.16x</td><td>0.19x</td><td>10.6x</td><td>9.6x</td><td>12.4x</td><td>9.7x</td><td>--</td><td>--</td><td>---</td><td>---</td><td></td></tr><tr><td>2.9x</td><td>2.7x</td><td>0.33x</td><td>0.32x</td><td>11.4x</td><td>10.2x</td><td>11.7x</td><td>10.3x</td><td>37.5x</td><td>29.1x</td><td>13.6x</td><td>11.5x</td><td></td></tr><tr><td>5.3x</td><td>4.8x</td><td>0.34x</td><td>0.55x</td><td>26.8x</td><td>24.7x</td><td>26.3x</td><td>24.3x</td><td>51.0x</td><td>41.3x</td><td>37.9x</td><td>34.4x</td><td></td></tr><tr><td>4.9x</td><td>4.5x</td><td>0.51x</td><td>0.39x</td><td>16.8x</td><td>13.3x</td><td>17.5x</td><td>15.7x</td><td>22.8x</td><td>20.4x</td><td>23.6x</td><td>19.7x</td><td></td></tr><tr><td>3.9x</td><td>3.5x</td><td>0.22x</td><td>0.36x</td><td>9.2x</td><td>8.3x</td><td>15.7x</td><td>14.4x</td><td>17.9x</td><td>16.4x</td><td>11.3x</td><td>10.8x</td><td></td></tr><tr><td>2.9x</td><td>2.6x</td><td>0.24x</td><td>0.23x</td><td>8.8x</td><td>7.7x</td><td>9.6x</td><td>8.8x</td><td>20.1x</td><td>18.8x</td><td>11.9x</td><td>9.9x</td><td></td></tr><tr><td>0.7x</td><td>0.7x</td><td>0.05x</td><td>0.05x</td><td>4.9x</td><td>3.6x</td><td>3.6x</td><td>2.7x</td><td>7.7x</td><td>4.6x</td><td>8.8x</td><td>6.7x</td><td></td></tr><tr><td>3.9x</td><td>3.4x</td><td>0.16x</td><td>0.18x</td><td>11.3x</td><td>8.7x</td><td>9.2x</td><td>7.6x</td><td>10.3x</td><td>8.4x</td><td>22.6x</td><td>17.4x</td><td></td></tr><tr><td>5.3x</td><td>4.7x</td><td>0.35x</td><td>0.37x</td><td>11.6x</td><td>10.3x</td><td>12.2x</td><td>10.4x</td><td>19.0x</td><td>16.1x</td><td>17.6x</td><td>16.1x</td><td></td></tr><tr><td>5.0x</td><td>4.2x</td><td>0.27x</td><td>0.20x</td><td>---</td><td>30.1x</td><td>36.2x</td><td>24.5x</td><td>---</td><td>---</td><td>---</td><td>42.2x</td><td></td></tr><tr><td>3.5x</td><td>3.5x</td><td>NM</td><td>NM</td><td>8.7x</td><td>8.6x</td><td>9.4x</td><td>9.1x</td><td>12.4x</td><td>11.6x</td><td>9.0x</td><td>9.2x</td><td></td></tr><tr><td>4.0x</td><td>3.9x</td><td>0.84x</td><td>1.02x</td><td>9.2x</td><td>8.9x</td><td>11.8x</td><td>10.4x</td><td>21.2x</td><td>16.1x</td><td>15.7x</td><td>15.4x</td><td></td></tr><tr><td>5.0x</td><td>4.2x</td><td>0.22x</td><td>0.24x</td><td>18.6x</td><td>15.5x</td><td>22.0x</td><td>15.4x</td><td>---</td><td>---</td><td>29.2x</td><td>24.9x</td><td></td></tr></table>

## Appendix – JPM U.S. Software Equity Research

## Large and SMiD Cap Security & Analytics

Brian Essex, CFA AC

brian.essex@jpmchase.com

(1-212) 622-5990

John Lee

John.h.lee@JPM.com

(1-212) 622-6064

Alex Isaac

alex.isaac@JPM.com

(1-212) 622-9159

## Large Cap Enterprise Software

Arti Vula, CFA AC

arti.vula@jpmchase.com

(1-415) 315-5919

Jaiden R Patel

jaiden.patel@jpmchase.com

(1-646) 342-6427

Brian Hyska

brian.hyska@jpmchase.com

(1-212) 622-2883

Mashu Nishi

mashu.nishi@JPM.com

(1-212) 622-0078

## Vertical Software

Alexei Gogolev AC

alexei.gogolev@jpmchase.com

(1-212) 622-9391

Ella Smith

ella.smith@jpmchase.com

(1-212) 622-2451

Destiny Jackson

destiny.jackson@JPM.com

(1-212) 622-4360

Isabella A Camaj

bella.camaj@JPM.com

(1-212) 834-2379
"""
