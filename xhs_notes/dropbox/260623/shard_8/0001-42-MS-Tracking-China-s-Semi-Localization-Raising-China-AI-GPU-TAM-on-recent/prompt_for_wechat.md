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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 22, 2026 09:07 AM GMT

Tracking China's Semi Localization | Asia Pacific

# Raising China AI GPU TAM on recent geopolitical dynamics

The recent tightening of US export controls for China's overseas entities may create a new TAM for China's AI GPU.

Recent news regarding halting of AI chip shipments to Chinese firms outside of China poses a 'bull case' scenario for China AI GPU: in early June, news reported that the US Department of Commerce had moved to close a potential loophole that may have led companies to export the world's most advanced chips – such as NVIDIA's most sophisticated Blackwell processors – to subsidiaries of Chinese companies located outside China. We think that, in the short term, China CSPs may turn to more GPU rental to fulfill the strong computing demand, while in the mid-to-longer term, it is likely that China AI GPU may potentially see overseas adoption, which is the bull base we argue in our China AI GPU Insight report.

We raise our forecast of China's AI chip TAM to US\$91bn by 2030, up 36%, from US\$67bn previously, implying a 23% CAGR over 2025-30. The upward revision is mainly because of: 1) Adding "CSP's overseas capex" as the new TAM; 2) Bytedance's plan to sharply increase its capital spending in 2026 and 2027 (link); 3) the addition of Kingsoft Cloud to the database; and 4) revised up sovereign and SOE-related TAM on back of government advocacy to increase spending on AI infrastructure.

Domestic AI infrastructure enters a critical deployment window: Our recent field trip in China in suggests that despite ongoing capacity expansion, major CSPs continue to face compute shortages, while vendor qualification activity is accelerating. We believe 2026 will be a critical year for domestic suppliers to enter CSP procurement systems, with competition increasingly driven by ecosystem maturity, software optimization and cluster deployment capabilities. On the supply side, access to leading-edge foundry capacity remains a key differentiator. Vendors approved for CCATS (Commodity Classification Automated Tracking System) with BIS (Bureau of Industry and Security) are allowed access to TSMC manufacturing and generally benefit from better cost and power efficiency, for example 7nm/6nm node for Iluvatar. Meanwhile, domestic advanced-node capacity continues to ramp. Industry participants expect a more stable local supply chain to emerge in 2027-28 other than SMIC South, supporting broader adoption of domestic AI infrastructure.

Stock implications – OW China GPU companies, fab and semicap plays: We like Cambricon (OW) – we raise our PT to Rmb1,528, and Iluvatar CoreX (OW) – we raise our PT to HK\$688 on back of stronger China CSP demand; we also like SMIC (0981.HK, OW) and Hua Hong (1347.HK, EW) as key enablers of China's AI localization. We are constructive on Chinese semi equipment – Naura (002371.SZ), AMEC (688012.SS) and ACMR (ACMR.O) – on their positioning in China's accelerating semiconductor localization cycle; and ASMPT (0522.HK) as an enabler of China advanced packaging.

MS TAIWAN LIMITED+

Daniel Yen, CFA
Equity Analyst
Daniel Yeng@morganstanley.com +896 2 2730-2863

<table><tr><td colspan="2">Daisy Dai, CFA</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Daisy Dai@morganstanley.com</td><td>+852 2848-7310</td></tr></table>

<table><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Tiffany Yeh</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Tiffany Yeh@morganstanley.com</td><td>+886 2 7712-3032</td></tr></table>

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Henry Zhao</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Henry.Zhao@morganstanley.com</td><td>+852 2239-7731</td></tr></table>

<table><tr><td colspan="2">Ethan Jia</td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Ethan.Jia@morganstanley.com</td><td>+852 3963-2287</td></tr></table>

<table><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Lucas Wang</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Lucas.Wang@morganstanley.com</td><td>+886 2 2730-2875</td></tr></table>

Asia Summer School 2026

![](images/48ec4002e0099e3d08e4524c1eb8856c092283ab2d50f2779ad12bc296da7f9d.jpg)

<table><tr><td colspan="2">GREATER CHINA TECHNOLOGY SEMICONDUCTORS</td></tr><tr><td>Asia Pacific</td><td></td></tr><tr><td>Industry View</td><td>Attractive</td></tr></table>

<table><tr><td colspan="3">Cambricon Technology</td></tr><tr><td>Corporation (688256.SS)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>Rmb1,342.28</td><td>Rmb1,528.00</td></tr></table>

<table><tr><td colspan="3">lluvatar CoreX Semiconductor</td></tr><tr><td>Co., Ltd. (9903.HK)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>HK$600.00</td><td>HK$688.00</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## China AI GPU market TAM

China's AI GPU demand is concentrated across a small number of large buyer groups, whose capex decisions ultimately define the size of the addressable market.

\- The first group comprises China's CSPs – including ByteDance, Alibaba and Tencent – which procure AI chips both to train and run inference on proprietary models and to deploy AI infrastructure for external cloud customers.

\- The second group includes China's telecom operators, SOEs and municipal governments – the so-called sovereign-AI buyers – where demand is driven by national AI infrastructure build-out, data sovereignty, and public-sector applications.

\- AI start-ups (e.g., DeepSeek, MiniMax) and auto OEMs (e.g., Xpeng, Xiaomi) also purchase AI chips, although their volumes currently remain smaller than those of the first two groups.

## We forecast China's AI chip TAM to reach US\$91bn by 2030 up 36% from US\$67bn previously, implying a 23% CAGR over 2025-30. The upward revision is mainly because:

\- We added new category (China CSP's overseas AI data center using local GPU). In the short term, China CSPs may turn to more GPU rental to fulfill the strong computing demand, while in the mid-to-longer term, it is likely that China AI GPU may potentially see overseas adoption. Therefore we assume that part to be zero until 2027, but from 2028 onwards, we expect $3\% / 10\% / 20\%$ of overseas capex to be addressed by local CPU in 2028/29/30.

\- Bytedance is planning to sharply increase its capital spending in 2026 and 2027 in a bid to lead the Chinese artificial intelligence market and challenge the top US players abroad – the news reported that 2027 capex could be US\$100 bn if economic and business conditions are favourable, we put US\$80bn (\~Rmb54+2bn) to build in some conservatism.

\- We added Kingsoft Cloud to the database, its capex surged to Rmb3bn, with full-year 2026 capital investments projected to exceed Rmb15-20bn to meet explosive AI and cloud demand.

\- We revised up sovereign and SOE-related TAM to US\$9bn up from US\$7bn previously. Recent news (Bloomberg, Jun 9) reported that China is preparing Rmb2tn over the next five years for building data centres across the country, so far we did not see specific government guidance, but directionally SOE and local government will spend more on AI infrastructure.

We expect China's AI-chip self-sufficiency to rise from 42% in 2025 to 70% in 2030e. We expect leading-node-capacity expansion and continued chip-performance improvement to drive local AI-chip revenue growth.

Exhibit 1: We expect China AI chip TAM to grow to US\$91bn by 2030E  
![](images/af519d53ec485e88a48bd1ab33e662d5c91a10c6aef9cf9cf313f8222b911d85.jpg)  
Source: Company data, MS (E) estimates

Exhibit 2: We expect China AI chip self-sufficiency to reach 70% in 2030E  
![](images/2cce4dcc3e8fe6f66ea7c5265ed7dcebf624b22c272ebe70dff677de1b4c4995.jpg)  
Source: Company data, MS (e) estimates

## China Semi Equipment Import Trends

China's semi equipment import value was US\$2.4bn in Apr 2026, down 6% Y/Y. On a three-month moving average basis, the Y/Y growth was -9%, up from the -14% YoY in Mar 2026 (Exhibit 3). Our US team expects China WFE to grow at 16% yoy in 2026, to US \$48bn, mainly driven by memory and leading-node capacity expansion (link). We expect local equipment vendors to further gain market share on the back of an increasing China WFE TAM.

YTD, import values from the US, Netherlands, Korea and Japan have all decreased: -43%, -22%, -23% and -28% Y/Y, respectively. Only import from Singapore was up 43% YoY.

Exhibit 3: Growth in China's semi equipment imports declined to -9% Y/Y (3MMA) in Apr 2026  
![](images/b02e9de0e0a19cc5a5ab58b5178181367c4336f237383ebb4dcb9cfa3110fc9a.jpg)  
Source: China's General Administration of Customs, MS.

Exhibit 4: Semi equipment imports from most major countries was down yoy (YTD)  
![](images/6e9258df3b5c6527a8018705fcba8dcb6d50b80f865ced14d2cf1b2840f8021b.jpg)  
Source: China's General Administration of Customs, MS

## Monthly Performance and Catalysts

Outperformers: ACMR +49.2%, Gigadevice +36.2%, JCET +24.8%

Underperformers: Shanghai Fudan -38.4%, USI -20.7%, Maxscend -18.3%

Over the past month, ACMR has outperformed, because of strong demand from memory clients and, in our view, because Huawei's LogicFolding process will drive increased adoption of ECP for TSV metallization, catalyzing rapid growth in ACMR's non-wet cleaning tool business (link). For Gigadevice, we see recent developments for servers (for high performance NAND) suggest potential adoption of SLC in datacenters, as SLC is ideal for fast reading and writing speed, Gigadevice is one of the beneficiary of this trend. Also NOR is seeing more tightness on mature foundry shortages (link).

Among the underperformers, Shanghai Fudan's share price saw a decline of 38.4% in the past month on corrected sentiment toward low earth orbit satellites, as carrier rockets are not yet recyclable. Also, USI share price declined by 20.7%, reflect market concern regarding delays in CPO introduction (link).

Exhibit 5: Share price performance of key Chinese semi localization stocks

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">Price (loc)</td><td rowspan="2">Mkt Cap (US$ mn)</td><td rowspan="2">Stock Rating</td><td colspan="4">Performance</td></tr><tr><td>1M</td><td>3M</td><td>12M</td><td>YTD</td></tr><tr><td colspan="9">Foundry</td></tr><tr><td>0981.HK</td><td>SMIC</td><td>71.65</td><td>91,921</td><td>O</td><td>(6.5%)</td><td>13.5%</td><td>75.6%</td><td>0.3%</td></tr><tr><td>1347.HK</td><td>Hua Hong Semiconductor Ltd</td><td>139.20</td><td>36,794</td><td>E</td><td>7.5%</td><td>46.5%</td><td>366.3%</td><td>87.3%</td></tr><tr><td colspan="9">Backend</td></tr><tr><td>601231.SS</td><td>Universal Scientific Ind. (Shanghai)</td><td>33.90</td><td>11,978</td><td>O</td><td>(20.7%)</td><td>(13.3%)</td><td>136.9%</td><td>13.0%</td></tr><tr><td>600584.SS</td><td>JCET</td><td>68.92</td><td>18,240</td><td>E</td><td>24.8%</td><td>50.7%</td><td>114.6%</td><td>87.4%</td></tr><tr><td colspan="9">AI GPU</td></tr><tr><td>688256.SS</td><td>Cambricon Technology Corporation</td><td>1,240.00</td><td>115,226</td><td>O</td><td>(3.0%)</td><td>68.1%</td><td>205.5%</td><td>36.3%</td></tr><tr><td>9903.HK</td><td>Iluvatar CoreX Semiconductor Co., Ltd.</td><td>528.00</td><td>17,136</td><td>O</td><td>1.5%</td><td>67.6%</td><td>--</td><td>--</td></tr><tr><td>688802.SS</td><td>MetaX Integrated Circuits</td><td>694.89</td><td>41,120</td><td>E</td><td>(10.6%)</td><td>33.6%</td><td>--</td><td>19.8%</td></tr><tr><td colspan="9">Equipment</td></tr><tr><td>ACMR.O</td><td>ACM Research Inc</td><td>93.95</td><td>6,493</td><td>O</td><td>49.2%</td><td>107.5%</td><td>265.2%</td><td>138.1%</td></tr><tr><td>0522.HK</td><td>ASMPT Ltd</td><td>182.90</td><td>9,789</td><td>O</td><td>3.8%</td><td>67.3%</td><td>236.5%</td><td>136.2%</td></tr><tr><td>688012.SS</td><td>Advanced Micro-Fabrication Equipment Inc</td><td>303.92</td><td>42,059</td><td>O</td><td>16.6%</td><td>43.6%</td><td>172.8%</td><td>66.0%</td></tr><tr><td>002371.SZ</td><td>NAURA Technology Group Co Ltd</td><td>667.19</td><td>71,582</td><td>O</td><td>14.7%</td><td>45.7%</td><td>122.8%</td><td>45.3%</td></tr><tr><td colspan="9">Analog</td></tr><tr><td>300661.SZ</td><td>SG Micro Corp.</td><td>111.44</td><td>10,290</td><td>E</td><td>7.8%</td><td>49.0%</td><td>57.7%</td><td>62.4%</td></tr><tr><td colspan="9">Smartphone Semis</td></tr><tr><td>300782.SZ</td><td>Maxscend Microelectronics Co Ltd</td><td>89.76</td><td>7,633</td><td>U</td><td>(18.3%)</td><td>9.6%</td><td>27.3%</td><td>10.2%</td></tr><tr><td>603501.SS</td><td>OmniVision Integrated Circuits Group Inc</td><td>86.01</td><td>15,871</td><td>E</td><td>(16.7%)</td><td>(23.8%)</td><td>(31.5%)</td><td>(31.7%)</td></tr><tr><td>603160.SS</td><td>Shenzhen Goodix Technology Co Ltd</td><td>55.99</td><td>3,858</td><td>U</td><td>(15.6%)</td><td>(22.4%)</td><td>(17.6%)</td><td>(29.1%)</td></tr><tr><td colspan="9">Consumer Semis</td></tr><tr><td>688018.SS</td><td>Espressif Systems</td><td>112.00</td><td>3,883</td><td>O</td><td>(9.8%)</td><td>1.7%</td><td>14.5%</td><td>(7.8%)</td></tr><tr><td colspan="9">Memory</td></tr><tr><td>603986.SS</td><td>GigaDevice Semiconductor Beijing Inc</td><td>481.47</td><td>50,330</td><td>O</td><td>36.2%</td><td>75.2%</td><td>301.4%</td><td>124.7%</td></tr><tr><td colspan="9">Cloud Semis</td></tr><tr><td>688008.SS</td><td>Montage Technology Co Ltd -A</td><td>224.88</td><td>41,563</td><td>O</td><td>(6.6%)</td><td>52.1%</td><td>176.7%</td><td>90.9%</td></tr><tr><td>6809.HK</td><td>Montage Technology Co Ltd -H</td><td>355.00</td><td>41,563</td><td>O</td><td>(14.0%)</td><td>91.4%</td><td>--</td><td>--</td></tr><tr><td colspan="9">Power Semis/SiC</td></tr><tr><td>688396.SS</td><td>China Resources Microelectronics Limited</td><td>60.80</td><td>11,944</td><td>U</td><td>(0.2%)</td><td>19.0%</td><td>33.0%</td><td>15.0%</td></tr><tr><td>603290.SS</td><td>StarPower Semiconductor Ltd</td><td>109.00</td><td>3,861</td><td>E</td><td>(3.7%)</td><td>(0.1%)</td><td>36.3%</td><td>13.4%</td></tr><tr><td>300373.SZ</td><td>Yangjie Technology</td><td>96.68</td><td>7,787</td><td>O</td><td>23.3%</td><td>22.6%</td><td>97.8%</td><td>42.2%</td></tr><tr><td>600460.SS</td><td>Hangzhou Silan Microelectronics Co. Ltd.</td><td>32.15</td><td>7,913</td><td>U</td><td>6.4%</td><td>10.9%</td><td>35.0%</td><td>13.2%</td></tr><tr><td>688234.SS</td><td>SICC Co Ltd</td><td>123.70</td><td>8,454</td><td>O</td><td>(4.9%)</td><td>48.9%</td><td>120.4%</td><td>39.2%</td></tr><tr><td>2577.HK</td><td>InnoScience</td><td>57.70</td><td>6,738</td><td>E</td><td>(17.7%)</td><td>(9.3%)</td><td>59.4%</td><td>(26.4%)</td></tr><tr><td colspan="9">EDA/IP</td></tr><tr><td>301269.SZ</td><td>Empyrean Technology Co Ltd</td><td>94.57</td><td>7,629</td><td>E</td><td>(1.3%)</td><td>(0.3%)</td><td>(19.3%)</td><td>(11.1%)</td></tr><tr><td colspan="9">FPGA</td></tr><tr><td>002049.SZ</td><td>Unigroup Guoxin Microelectronics Co Ltd</td><td>71.51</td><td>8,986</td><td>U</td><td>(10.2%)</td><td>(4.9%)</td><td>13.7%</td><td>(9.3%)</td></tr><tr><td>1385.HK</td><td>Shanghai Fudan Microelectronics</td><td>26.80</td><td>5,206</td><td>O</td><td>(38.4%)</td><td>(37.0%)</td><td>(3.8%)</td><td>(40.9%)</td></tr><tr><td></td><td>CSI 300</td><td>4,777.32</td><td></td><td></td><td>(3.5%)</td><td>1.9%</td><td>22.7%</td><td>3.2%</td></tr><tr><td></td><td>SSE Composite</td><td>4,031.51</td><td></td><td></td><td>(4.3%)</td><td>(2.4%)</td><td>18.5%</td><td>1.6%</td></tr></table>

Source: FactSet, MS. Note: Market data as of the close on Jun 12, 2026. Past performance is no guarantee of future results. Results shown do not include transaction costs.

Exhibit 8:  
Exhibit 6: 12-month share price performance, by segment  
![](images/13b90ef21557523a16d22396751a7ab7064490d8034ef602d8c23f510b6118af.jpg)  
Source: FactSet, MS. Note: Market data as of the close on Jun 12, 2026. Past performance is no guarantee of future results. Results shown do not include transaction costs.

Exhibit 7: Key stocks' 12-month share price performance  
![](images/226f6f68998c99a4a0d518d8452c45ead935da1baeb06ab14cc9c0ec99a4d506.jpg)  
Source: FactSet, MS. Note: Market data as of the close on Jun 12, 2026. Past performance is no guarantee of future results. Results shown do not include transaction costs.

Greater China semi localization stocks' performance trends  
![](images/08428838b98a774ee795c3e0180162d64f8f2d0b43717f1b2171fc06d2a285ce.jpg)  
Source: FactSet, MS. Note: Market data as of the close on Jun 9, 2026. Past performance is no guarantee of future results. Results shown do not include transaction costs.

## Catalysts and key events

<table><tr><td>Date</td><td>Event</td><td>Location</td></tr><tr><td>July 17-20, 2026</td><td>World Artificial Intelligence Conference</td><td>Shanghai, China</td></tr><tr><td>August 26-28, 2026</td><td>AGIC Shenzhen Int&#x27;l AGI Conference &amp; Expo</td><td>Shenzhen, China</td></tr><tr><td>Aug 31 - Sep 2, 2026</td><td>Semiconductor Equipment, Materials and Core Parts Exhibition (CSEAC)</td><td>Wuxi China</td></tr><tr><td>Sept 9-11, 2026</td><td>China International Optoelectronics Exposition &amp; Int&#x27;l Integrated Circuit Innovation Expo</td><td>Shenzhen, China</td></tr><tr><td>Oct 14-16, 2026</td><td>SemiBay</td><td>Shenzhen, China</td></tr><tr><td>Oct 27-29, 2026</td><td>China Int&#x27;l Semiconductor Technology &amp; Application Expo</td><td>Shenzhen, China</td></tr><tr><td>Nov 26-28, 2026</td><td>China AI &amp; Robot Industry Chain Expo</td><td>Shenzhen, China</td></tr></table>

## Cambricon: Earnings estimate revisions and quarterly financials

We raise our revenue forecasts 6% for 2026, 10% for 2027 and 9% for 2028: This primarily reflects our upgraded China AI accelerator market TAM. Cambricon, as on

[中间内容因长度限制已省略]

d>Gudeng Precision (3680.TWO)</td><td>O (11/25/2025)</td><td>NT$547.00</td></tr><tr><td>Hua Hong Semiconductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$168.10</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$630.00</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$339.00</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb112.38</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$4,465.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb758.00</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$505.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb745.00</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb90.56</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,580.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb136.81</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$673.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$76.50</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,510.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$160.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$191.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$541.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$208.80</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb78.20</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$178.50</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb101.71</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb44.80</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$66.90</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb91.33</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$29.62</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb158.00</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb135.59</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb81.96</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb37.49</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb128.11</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$1,115.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,450.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$19,275.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$122.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb123.11</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb689.70</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$185.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$446.40</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb280.05</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$567.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$216.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$695.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$81.60</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$900.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb59.19</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$222.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$112.50</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$225.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb159.28</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb616.16</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,260.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$712.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$18.11</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,915.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,425.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$321.66</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,460.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
