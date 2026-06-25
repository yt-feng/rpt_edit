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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
JAPAN SHIPBUILDING

# Abundant catalysts to buoy the medium-term earnings outlook, we remain bullish on sector stocks

We summarize our overall view on Japan's shipbuilding industry, upcoming catalysts to watch, business trends at select non-covered (NC) companies, and the implications for our coverage companies Namura Shipbuilding, Mitsui E&S, and Tokyo Keiki. Key points are as follows.

Norihiro Miyazaki  
+81(3)4587-9842 |  
norihiro.miyazaki@gs.com  
GS Japan Co., Ltd.

Ryohei Kurita  
+81(3)4587-1799 |  
ryohei.kurita@gs.com  
GS Japan Co., Ltd.

Current conditions in Japan's shipbuilding industry: The order backlog as of end-May 2026 disclosed by the Japan Ship Exporters' Association was 29.27 mn GT, meaning the industry has already secured vessel demand scheduled for delivery over the next three and a half years. The backlog remains at a historically high level. Cumulative order volume for Jan-May 2026 was 3.6 mn GT (-2% yoy). We focus on the following two industry trends as potential catalysts.

(1) Potential for order backlog expansion via capacity enhancements: In late February 2026, the Maritime Bureau of the Ministry of Land, Infrastructure, Transport and Tourism (MLIT) announced revisions to its shipbuilding-related policy initiatives. The Bureau is starting a framework for capacity enhancement, and said operators must have plans to expand capacity by $50\%$ or more from 2024 levels to be eligible for support from the Shipbuilding Industry Revitalization Fund ( $\yen 350$ bn over 10 years). Japan's Cabinet is scheduled to approve a growth strategy targeting 17 strategic sectors, including shipbuilding, in around summer 2026, after which we think the focus will be on whether Namura Shipbuilding and other major shipbuilders will utilize the revitalization fund. Although Japanese shipbuilders are currently operating at full capacity, if we see an expansion in order volume (and order backlog) that factors in future capacity enhancements, we believe it will be a catalyst for raising the earnings growth outlook and valuations for names in our sector coverage.

(2) Emergence of defense demand: We see several potential catalysts ahead that could underpin expectations for a further expansion in domestic and international defense demand, including the Basic Policy on Economic and Fiscal Management and Reform 2026 (July), a Defense White Paper (July), the revision of Japan's three strategic security

documents (by end-2026), and the US defense budget for FY2027. Regarding the US defense budget, media reports have said the US may allocate c.US\$1.85 bn to procuring naval vessels utilizing shipyards in Japan or South Korea. If orders are placed in Japan, our coverage company Tokyo Keiki could benefit as a naval vessel component supplier. We believe the theme of growing demand for Japanese and US naval vessel repairs remains intact for Namura Shipbuilding's ship repair/maintenance business as well.

Global shipbuilding industry order trends: In response to the recent situation in Iran, freight rates have been surging on the back of longer transportation distances accompanying alternative procurement, leading to a strong demand environment, particularly for crude oil tankers. Recent new vessel prices remain at historically high levels.

Trends at NC companies: Japan Engine expects steady sales and profit growth in FY3/27, driven by a rise in license revenue accompanying capacity enhancement by Chinese engine manufacturers that occurred from 3Q3/26 onwards (although earnings are set to be heavily weighted toward 2H due to the timing of internal combustion engine deliveries). Furuno Electric reported strong sales to European shipping companies and Asian shipbuilders (especially in China), and in its defense-related business, the company confirmed potential for margin improvement backed by utilization of existing commercial products. Chugoku Marine Paints noted it expects an earnings impact from the rise in costs for inputs (cuprous oxide and epoxy resin) since the beginning of the year, mainly affecting sales to South Korean shipbuilders where a surcharge system has not been introduced. Daihatsu Infinearth expects sales and profit growth in FY3/27 amid stronger demand on the back of increased container ship production and the startup of a new plant. Meanwhile, regarding internal combustion engines for use at data centers, the company indicated it anticipates no short-term earnings impact; while it supplies gas turbines, which are highly space-efficient and adopted in urban data centers, it does not handle the high-output diesel engines that are currently expected to see demand expansion.

We reiterate our Buy rating on Namura Shipbuilding/Mitsui E&S/Tokyo Keiki. Many investors we speak with express caution on the sector, given the shift in investor funds toward the generative AI theme. Fundamentally however, the earnings outlook is actually moving higher owing to both a favorable order environment and policy support, and we maintain our bullish stance on shipbuilding stocks in our coverage. For Namura Shipbuilding, in addition to the potential utilization of the Shipbuilding Industry Revitalization Fund, we look for steady earnings growth in FY3/27, backed by a mix shift to large vessels, margins on which we believe are relatively high. For Mitsui E&S, while we view its guidance for a yoy decline in operating profits in FY3/27 as overly conservative given recent earnings trends, we assume that investors' confidence in upside to earnings guidance will increase from 2H3/27 onward, given the company's traditionally conservative stance. In the medium term, if capacity enhancements by Japanese shipbuilders move into full swing, we see potential for tightening supply/demand (i.e., unit price

improvement) in the domestic engine market, which is already operating at full capacity, and we are upbeat on the strong prospect for stronger margins at the company. We believe Tokyo Keiki is positioned to benefit from the overall upcycle in the global shipbuilding industry, in addition to the expansion of defense demand (especially O&M-related), which we expect to see domestic and overseas growth over the medium to long term.

\- Our estimate revisions: For Namura Shipbuilding, we revise our operating profit forecasts for FY3/27-FY3/29 by +0.4%/+1.7%/-0.2%, reflecting recent shipbuilding progress. Our 12-month target price of ¥5,600 is unchanged. For Mitsui E&S, we revise our operating profit forecasts for FY3/27-FY3/29 by 0%/-5%/-4%, as we have lowered our expectations for the pace of profit improvement for peripheral services from FY3/28 onward, mainly based on recent earnings. Our SOTP-based 12-month target price is unchanged at ¥7,000. We leave our estimates for Tokyo Keiki intact, as the current business overview and outlook were already incorporated in our recent initiation report. We maintain our 12-month target price of ¥8,800 for Tokyo Keiki.

Exhibit 1: Overview of shipbuilders and related companies

<table><tr><td></td><td>Namura Shipbuilding</td><td>Mitsui E&amp;S</td><td>Furuno Electric</td><td>Tokyo Keiki</td><td>Daihatsu Infinearth</td><td>Japan Engine Corporation</td><td>Chugoku Marine Paints</td><td>Terasaki Electric</td></tr><tr><td>Ticker</td><td>7014.T</td><td>7003.T</td><td>6814.T</td><td>7721.T</td><td>6023.T</td><td>6016.T</td><td>4617.T</td><td>6637.T</td></tr><tr><td>Market cap (JPY bn)</td><td>255</td><td>431</td><td>189</td><td>107</td><td>70</td><td>71</td><td>185</td><td>44</td></tr><tr><td>ADTV (JPYbn; last 6 months)</td><td>7.2</td><td>32.3</td><td>3.7</td><td>2.6</td><td>0.5</td><td>2.3</td><td>1.5</td><td>0.3</td></tr><tr><td colspan="9">Ship-related business overview</td></tr><tr><td>Ship-related business (% of FY0 companywide OP)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>After-service business (% of FY0 companywide ship-related sales wherever applicable)*</td><td>13%</td><td>20%</td><td>c. 33% of the commercial ships segment</td><td>50%</td><td>46%</td><td>52%</td><td>47%</td><td>13%</td></tr><tr><td>Mainstay products</td><td>Shipbuilding (dry bulk and tanker), maintenance for vessels (commercial &amp; naval)</td><td>Engine manufacturer specifically for Japanese shipbuilders; lisencee from Everllence and WinGD.</td><td>Electronic chart display and information system (ECDIS)</td><td>Auto-pilot system and gyrocompass for vessels</td><td>Auxiliary engine to generate electricity for commercial vessels</td><td>UE engine manufacturer and licenser.</td><td>Painting &amp; coating products for commercial and naval vessels.</td><td>Power distribution systems and engine monitoring systems for ships</td></tr><tr><td>Market share of those mainstay products (volume-based, FY25)</td><td>c. 7% in Japan</td><td>c. 60% in Japan</td><td>c. 40% globally</td><td>c. 60% globally</td><td>c. 45% in Japan and 25% globally</td><td>c. 10% in Japan and globally</td><td>c. 60% in Japan and 20% globally</td><td>c. 20-30% in Japan; c. 30% in China; up to 10% in South Korea</td></tr><tr><td colspan="9">Impacts of key industry trends</td></tr><tr><td>Demand for shipbuilding to shift from China to Japan</td><td>✓</td><td>✓</td><td>▲</td><td>▲</td><td>✓</td><td>✓</td><td>✓</td><td>▲</td></tr><tr><td>Price improvement in order backlog</td><td>✓</td><td>✓</td><td>▲</td><td>▲</td><td>▲</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Rising defense-related demand</td><td>✓</td><td>▲</td><td>✓</td><td>✓</td><td>▲</td><td>▲</td><td>✓</td><td>✓</td></tr><tr><td>Tighter emission controls in shipbuilding</td><td>▲</td><td>✓</td><td>▲</td><td>▲</td><td>✓</td><td>✓</td><td>✓</td><td>▲</td></tr><tr><td>Increase in # of active commercial vessels operating</td><td>▲</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Increase in own production capacity</td><td>▲</td><td>▲</td><td>▲</td><td>▲</td><td>✓</td><td>✓</td><td>▲</td><td>✓</td></tr><tr><td colspan="9">✓=potentially positive to earnings, ▲ = likely neutral or limited impact</td></tr><tr><td colspan="9">Earnings summary</td></tr><tr><td>Companywide sales (FY0; JPYmn)</td><td>159,035</td><td>353,196</td><td>140,616</td><td>61,186</td><td>88,066</td><td>29,707</td><td>139,364</td><td>62,859</td></tr><tr><td>Companywide operating profit (FY0; JPYmn)</td><td>28,085</td><td>37,641</td><td>16,246</td><td>5,362</td><td>7,621</td><td>5,458</td><td>17,437</td><td>6,197</td></tr><tr><td>OPM (FY0; %)</td><td>18%</td><td>11%</td><td>12%</td><td>9%</td><td>9%</td><td>18%</td><td>13%</td><td>10%</td></tr></table>

\* Terasaki Electric's after-service share % is based on the FY24 number.

Notes: Based on closing prices as of June 23, 2026. The impacts of key industry trends are based on interviews with each company, except for Namura Shipbuilding, Mitsui E&S, and Tokyo Keiki. Note that we use FY24 figures for the sales mix of Terasaki Electric's ship-related after-sales services.

Exhibit 2: Valuations

<table><tr><td rowspan="2" colspan="2"></td><td>Market Cap</td><td colspan="2">ADTV (6M)</td><td colspan="2">PER</td><td colspan="2">PBR</td><td colspan="4">SP performance</td><td rowspan="2">Net Debt/Equity</td></tr><tr><td>JPY bn</td><td>JPY bn</td><td>FY1</td><td>FY2</td><td>FY3</td><td>FY1</td><td>1M</td><td>3M</td><td>6M</td><td>1Y</td><td>FY0</td></tr><tr><td>Namura Shipbuilding</td><td>7014.T</td><td>267</td><td>7.2</td><td>12</td><td>11</td><td>8</td><td>1.7</td><td>1%</td><td>-23%</td><td>7%</td><td>41%</td><td>(0.36)</td><td></td></tr><tr><td>Mitsui E&amp;S</td><td>7003.T</td><td>435</td><td>32.3</td><td>12</td><td>11</td><td>10</td><td>1.7</td><td>-6%</td><td>-35%</td><td>-20%</td><td>52%</td><td>0.08</td><td></td></tr><tr><td>Tokyo Keiki</td><td>7721.T</td><td>112</td><td>2.6</td><td>22</td><td>21</td><td>17</td><td>2.2</td><td>9%</td><td>-16%</td><td>29%</td><td>54%</td><td>0.16</td><td></td></tr><tr><td>Japan Engine Corporation*</td><td>6016.T</td><td>71</td><td>2.3</td><td>14</td><td>13</td><td>11</td><td>3.1</td><td>-7%</td><td>-36%</td><td>-29%</td><td>22%</td><td>(0.02)</td><td></td></tr><tr><td>Furuno Electric*</td><td>6814.T</td><td>189</td><td>3.7</td><td>14</td><td>13</td><td>12</td><td>1.9</td><td>2%</td><td>-8%</td><td>-18%</td><td>94%</td><td>(0.05)</td><td></td></tr><tr><td>Daihatsu Infiniearth*</td><td>6023.T</td><td>70</td><td>0.5</td><td>10</td><td>9</td><td>9</td><td>1.2</td><td>-10%</td><td>23%</td><td>6%</td><td>31%</td><td>(0.06)</td><td></td></tr><tr><td>Chugoku Marine Paints*</td><td>4617.T</td><td>185</td><td>1.5</td><td>13</td><td>12</td><td>N/A</td><td>1.7</td><td>8%</td><td>0%</td><td>-22%</td><td>46%</td><td>(0.13)</td><td></td></tr><tr><td>Terasaki Electric*</td><td>6637.T</td><td>44</td><td>0.3</td><td>9</td><td>8</td><td>8</td><td>0.7</td><td>-1%</td><td>-15%</td><td>-22%</td><td>3%</td><td>(0.21)</td><td></td></tr><tr><td colspan="2">Median</td><td>148</td><td>2.5</td><td>13</td><td>12</td><td>10</td><td>1.7</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

\* Not Covered  
Forward P/E and P/B for Namura Shipbuilding, Mitsui E&S, and TOKYO KEIKI are based on GS forecasts. All others are based on LSEG Data & Analytics consensus forecasts. We use closing prices on June 23, 2026.

Source: LSEG Data & Analytics, GS Global Investment Research  
Exhibit 3: Monthly trend in P/E (FY1) for Japanese, South Korean, and Chinese shipbuilding sectors  
![](images/51b9e77cc1ac98f593267934b874011bf50a5a4eb66091df7d2820ca2a9ab606.jpg)  
Source: LSEG Data & Analytics, Data compiled by GS Global Investment Research

Exhibit 4: Monthly trend in global shipbuilding orders (vessel basis)  
![](images/b9bf47c6247c31814a94481cec16aafa52c56fd9760dac140de93170ce7e5d6f.jpg)  
Figures for Japan are based on export ship contract data from the Japan Ship Exporters' Association. Data for other countries is from Clarksons.  
Source: Clarksons, Japan Ship Exporters' Association, Data compiled by GS Global Investment Research

Exhibit 5: Monthly domestic order intake and order backlog (gross tonnage)  
![](images/755ab88fd437cd004c2c950a8d791587e52385cbd5eabe65b9133a3c7043a742.jpg)  
Note: We use combined figures for major member companies of the Japan Ship Exporters' Association  
Source: Japan Ship Exporters' Association, Data compiled by GS Global Investment Research

Exhibit 6: Global order backlog for alternative fuel capable ships (number of vessels) and their share of total order backlog  
![](images/171ecacfbef1c1196c0b0d7da3e31913d4bdae265de10f05e8418a265d01b44f.jpg)  
Source: Clarksons, Data compiled by GS Global Investment Research

Exhibit 7: Quarterly orders at Japanese shipbuilders and related companies  
![](images/bec2ba59a3bc552e6308305329a3b87c2e306a6288faffb5a7f2e36a5855906b.jpg)  
Namura Shipbuilding data is calculated from the QoQ difference in the order backlog of the new shipbuilding business (while also adding back sales from the corresponding quarter).

Source: Company data, Data compiled by GS Global Investment Research

## Exhibit 8: Quarterly operating profits for Japanese shipbuilding-related companies

![](images/a742fd2885a5003ff6de22790cbeaf12de229bd2031bac27264f4865d3d64e02.jpg)  
Furuno Electric's FY-end is February  
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 9: Road map for revitalization of Japan's shipbuilding industry  
![](images/8812955679ac6db76f413371bc361c168eb4058d73b5f840cbe434211edbd646.jpg)  
Source: Ministry of Land, Infrastructure, Transport and Tourism, Data compiled by GS Global Investment Research

Exhibit 10: Namura Shipbuilding: Earnings summary

<table><tr><td colspan="2">Namura Shipbuilding Co Ltd</td><td>26/3 1Q</td><td>26/3 2Q</td><td>26/3 3Q</td><td>26/3 4Q</td><td>27/3 1Q</td><td>27/3 2Q</td><td>27/3 3Q</td><td>27/3 4Q</td><td>3/2025</td><td>3/2026</td><td>3/2027E</td><td>3/2028E</td><td>3/2029E</td><td>3/2030E</td><td>3/2031E</td><td>3/2027E</td></tr><tr><td></td><td></td><td>A</td><td>A</td><td>A</td><td>A</td><td>GSe</td><td>GSe</td><td>GSe</td><td>GSe</td><td>A</td><td>A</td><td>GSe</td><td>GSe</td><td>GSe</td><td>GSe</td><td>GSe</td><td>CoE</td></tr><tr><td>Revenue</td><td>JPYmn</td><td>36,487</td><td>36,123</td><td>42,693</td><td>43,732</td><td>43,305</td><td>39,895</td><td>44,824</td><td>43,920</td><td>159,227</td><td>159,035</td><td>171,944</td><td>184,064</td><td>204,484</td><td>232,884</td><td>267,854</td><td>170,000</td></tr><tr><td>YoY</td><td>%</td><td>-8%</td><td>-6%</td><td>1%</td><td>14%</td><td>19%</td><td>10%</td><td>5%</td><td>0%</td><td>18%</td><td>0%</td><td>8%</td><td>7%</td><td>11%</td><td>14%</td><td>15%</td><td>7%</td></tr><tr><td>Gross profit</td><td>JPYmn</td><td>7,527</td><td>6,987</td><td>10,617</td><td>11,047</td><td>9,530</td><td>8,780</td><td>11,210</td><td>9,744</td><td>36,308</td><td>36,178</td><td>39,264</td><td>46,014</td><td>57,534</td><td>71,774</td><td>88,394</td><td></td></tr><tr><td>YoY</td><td>%</td><td>-26%</td><td>-14%</td><td>3%</td><td>43%</td><td>27%</td><td>26%</td><td>6%</td><td>-12%</td><td>58%</td><td>0%</td><td>9%</td><td>17%</td><td>25%</td><td>25%</td><td>23%</td><td></td></tr><tr><td>GPM</td><td>%</td><td>21%</td><td>19%</td><td>25%</td><td>25%</td><td>22%</td><td>22%</td><td>25%</td><td>22%</td><td>23%</td><td>23%</td><td>23%</td><td>25%</td><td>28%</td><td>31%</td><td>33%</td><td></td></tr><tr><td>Operating profit</td><td>JPYmn</td><td>5,758</td><td>5,014</td><td>8,708</td><td>8,605</td><td>7,430</td><td>6,530</td><td>9,060</td><td>6,834</td><td>29,466</td><td>28,085</td><td>29,854</td><td>35,474</td><td>45,974</td><td>59,094</td><td>74,494</td><td>29,000</td></tr><tr><td>YoY</td><td>%</td><td>-33%</td><td>-23%</td><td>0%</td><td>52%</td><td>29%</td><td>30%</td><td>4%</td><td>-21%</td><td>79%</td><td>-5%</td><td>6%</td><td>19%</td><td>30%</td><td>29%</td><td>26%</td><td>3%</td></tr><tr><td>OPM</td><td>%</td><td>16%</td><td>14%</td><td>20%</td><td>20%</td><td>17%</td><td>16%</td><td>20%</td><td>16%</td><td>19%</td><td>18%</td><td>17%</td><td>19%</td><td>22%</td><td>25%</td><td>28%</td><td>17%</td></tr><tr><td>SG&amp;A</td><td>JPYmn</td><td>1,769</td><td>1,973</td><td>1,909</td><td>2,442</td><td>2,100</td><td>2,250</td><td>2,150</td><td>2,910</td><td>6,842</td><td>8,093</td><td>9,410</td><td>10,540</td><td>11,560</td><td>12,680</td><td>13,900</td><td></td></tr><tr><td>YoY</td><td>%</td><td>19%</td><td>21%</td><td>18%</td><td>16%</td><td>19%</td><td>14%</td><td>13%</td><td>19%</td><td>6%</td><td>18%</td><td>16%</td><td>12%</td><td>10%</td><td>10%</td><td>10%</td><td></td></tr><tr><td 

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
