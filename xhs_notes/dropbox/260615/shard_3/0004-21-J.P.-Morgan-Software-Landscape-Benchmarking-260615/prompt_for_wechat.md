你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
