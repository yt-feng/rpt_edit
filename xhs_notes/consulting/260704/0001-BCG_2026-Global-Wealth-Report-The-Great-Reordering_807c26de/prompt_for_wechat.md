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
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
FINANCIAL INSTITUTIONS
GLOBAL WEALTH REPORT 2026
26TH EDITION

# The Great Reordering

May 2026

By Michael Kahlich, Daniel Kessler, Akin Soysal, Peter Czerepak, Renaud Fages, Dean Frankle, Mayank Jha, Wei Chuan Lim, Michael Boardman, Yves Robert-Charrue, Gloria Ong, Sam Kittross-Schnell, Omar Rahman, Felix Werner, and Nisha Mittal

![](images/b3640098af13e35ab5e661526323a482f1e6d2154047bfa2ea00cdb2559b75a3.jpg)

![](images/862c16519056a86d8405628a722a84894e5b6cee1c0e13a3c2a95adcc8d19b6f.jpg)

Foreword

# Global financial wealth grew at its fastest level since 2021. But where wealth is growing, who holds it, and what it will take to serve clients well are changing rapidly.

This report examines four dimensions of that change. The first is geographic. Wealth creation continues to concentrate in a smaller number of regions and booking centers. Two hubs increasingly capture the bulk of cross-border flows. Firms that credibly straddle both clusters will command a structural advantage.

The second is the emerging market opportunity. Not counting China, roughly 10% of global financial wealth growth through 2030 will come from emerging markets, led by India, Brazil, and Mexico. The affluent and emerging high-net-worth (HNW) segment in these markets is among the least well served in the industry. Retail and corporate banks have the relationships and distribution reach to capture this opportunity but will need to change how they operate to do so.

The third is generational. Asia's first large-scale intergenerational wealth transfer is already underway, and the decisions families make in the coming decade about governance, leadership, ownership, and purpose will determine what gets passed on and how. Wealth managers that help families navigate the complexities of this transition will define the next era of the industry in the region.

The fourth is technological. AI is already drafting financial plans, automating compliance workflows, predicting client churn, and executing complex processes with minimal human intervention. The question now is whether firms are building around it or simply layering generative tools and agents onto existing processes. The difference between those two approaches will widen quickly.

Some of these topics have bearing on specific markets and segments. Together they show that wealth management is entering a period of immense change. The tools available to serve clients are being transformed. And the competitive positions that firms have taken for granted are under pressure in ways that were not visible even two years ago.

The four shifts this report describes are already influencing growth, profitability, and competitive position across the industry. Our hope is that senior leaders use it to take a hard look at where their firm is leading, where it is exposed, and whether its current pace of change is sufficient for what the market now demands.

## Contents

04 The Great Reshuffling of Financial Wealth

11 Where the Next Wave of Wealth Is Coming From

16 The Succession Reckoning

20 AI and the New Economics of

Wealth Management

24 About the Authors

![](images/045a7df27daeecc73c7c3de35b15fb75e79e859eb44eee2788f8479e18aff7b4.jpg)

# The Great Reshuffling of Financial Wealth

Against a backdrop of trade wars, tariff brinkmanship, and escalating geopolitical tension, global financial wealth rose 10.7% to \$333 trillion in 2025.

This is up 2 percentage points over the prior year—the highest rate of growth since 2021. (See Exhibit 1.) Including real assets, net wealth reached \$550 trillion, up 9.3%.

The gains were not evenly distributed. Equities surged 13.2% while real assets expanded 7.4%, pinched by high prices and rising supply in major developed markets. Gold was the standout, rising roughly 44%, driven by robust retail buying and a wave of central bank accumulation that reflects deepening unease about reserve currency stability.

Financial wealth is projected to grow at a 7% compound annual rate through 2030, though the pace of gains assumes an easing of geopolitical tensions and energy disruptions in the second half of 2026.

# Financial Wealth Rose 10.7% Globally, with Wide Variation Across Regions

FINANCIAL WEALTH GROWTH. 2024–2025 (%)

![](images/d1e57248e5f115d5f16a971758388ad201206297aca7841818b991189b0de1e1.jpg)  
FINANCIAL WEALTH GROWTH (IN \$TRILLIONS) $^{2}$

<table><tr><td>Global</td><td></td><td>2024</td><td>2025</td><td>2030</td><td>Growth&#x27;24-&#x27;25</td><td>CAGR&#x27;25-&#x27;30</td></tr><tr><td rowspan="4">+32T</td><td>Financial assets</td><td>300.5</td><td>332.7</td><td>457.1</td><td>10.7%</td><td>7%</td></tr><tr><td>Liabilities</td><td>59.8</td><td>64.4</td><td>78.7</td><td>7.7%</td><td>4%</td></tr><tr><td>Real assets</td><td>261.9</td><td>281.3</td><td>335.2</td><td>7.4%</td><td>4%</td></tr><tr><td>Net wealth</td><td>502.6</td><td>549.6</td><td>713.6</td><td>9.3%</td><td>5%</td></tr></table>

Western Europe

<table><tr><td colspan="2">North America</td><td>2024</td><td>2025</td><td>2030</td><td>Growth&#x27;24–&#x27;25</td><td>CAGR&#x27;25–&#x27;30</td></tr><tr><td rowspan="4">+10.8T</td><td>Financial assets</td><td>145.1</td><td>155.9</td><td>214.3</td><td>7.4%</td><td>7%</td></tr><tr><td>Liabilities</td><td>22.2</td><td>23.0</td><td>28.4</td><td>3.4%</td><td>4%</td></tr><tr><td>Real assets</td><td>67.0</td><td>69.0</td><td>83.6</td><td>3.1%</td><td>4%</td></tr><tr><td>Net wealth</td><td>189.9</td><td>202.0</td><td>269.5</td><td>6.4%</td><td>6%</td></tr></table>

<table><tr><td rowspan="4">+8.3T</td><td>Financial assets</td><td>54.4</td><td>62.7</td><td>79.6</td><td>15.3%</td><td>5%</td></tr><tr><td>Liabilities</td><td>12.9</td><td>14.7</td><td>17.6</td><td>13.7%</td><td>4%</td></tr><tr><td>Real assets</td><td>62.6</td><td>70.6</td><td>81.7</td><td>12.8%</td><td>3%</td></tr><tr><td>Net wealth</td><td>104.1</td><td>118.6</td><td>143.7</td><td>14.0%</td><td>4%</td></tr></table>

CEE and Central Asia

<table><tr><td rowspan="4">+1.3T</td><td>Financial assets</td><td>5.3</td><td>6.6</td><td>8.6</td><td>23.8%</td><td>6%</td></tr><tr><td>Liabilities</td><td>1.0</td><td>1.3</td><td>1.6</td><td>26.5%</td><td>4%</td></tr><tr><td>Real assets</td><td>8.1</td><td>10.2</td><td>13.3</td><td>26.1%</td><td>5%</td></tr><tr><td>Net wealth</td><td>12.4</td><td>15.5</td><td>20.3</td><td>25.1%</td><td>6%</td></tr></table>

Latin America

<table><tr><td rowspan="4">+5.4T</td><td>Financial assets</td><td>36.1</td><td>41.5</td><td>62.8</td><td>15.0%</td><td>9%</td></tr><tr><td>Liabilities</td><td>11.3</td><td>12.0</td><td>13.2</td><td>6.0%</td><td>2%</td></tr><tr><td>Real assets</td><td>51.8</td><td>54.2</td><td>58.8</td><td>4.7%</td><td>2%</td></tr><tr><td>Net wealth</td><td>76.5</td><td>83.7</td><td>108.4</td><td>9.4%</td><td>5%</td></tr></table>

<table><tr><td rowspan="4">+1.3T</td><td>Financial assets</td><td>7.4</td><td>8.7</td><td>12.0</td><td>17.7%</td><td>7%</td></tr><tr><td>Liabilities</td><td>1.5</td><td>1.8</td><td>2.7</td><td>20.3%</td><td>8%</td></tr><tr><td>Real assets</td><td>10.1</td><td>11.6</td><td>14.3</td><td>14.2%</td><td>4%</td></tr><tr><td>Net wealth</td><td>16.0</td><td>18.5</td><td>23.6</td><td>15.2%</td><td>5%</td></tr></table>

Middle East and Africa

<table><tr><td rowspan="4">+1.0T</td><td>Financial assets</td><td>8.2</td><td>9.2</td><td>13.1</td><td>12.3%</td><td>7%</td></tr><tr><td>Liabilities</td><td>1.4</td><td>1.6</td><td>2.3</td><td>11.4%</td><td>7%</td></tr><tr><td>Real assets</td><td>11.3</td><td>12.1</td><td>15.9</td><td>6.9%</td><td>6%</td></tr><tr><td>Net wealth</td><td>18.1</td><td>19.7</td><td>26.7</td><td>9.0%</td><td>6%</td></tr></table>

Asia-Pacific (ex. China)

<table><tr><td rowspan="4">+4.1T</td><td>Financial assets</td><td>44.0</td><td>48.0</td><td>66.7</td><td>9.2%</td><td>7%</td></tr><tr><td>Liabilities</td><td>9.4</td><td>10.0</td><td>12.9</td><td>7.0%</td><td>5%</td></tr><tr><td>Real assets</td><td>51.1</td><td>53.7</td><td>67.5</td><td>5.1%</td><td>5%</td></tr><tr><td>Net wealth</td><td>85.7</td><td>91.7</td><td>121.3</td><td>7.0%</td><td>6%</td></tr></table>

Sources: BCG Expand Global Wealth Management Database 2026; BCG analysis.  
Note: CEE = Central and Eastern Europe.  
$^{1}$ US and Canada. $^{2}$ Wealth in local currency was converted into US at the year-end exchange rate across all time periods. $^{3}$ Wealth in local currency was converted into US using a constant exchange rate across all time periods.

## Where Wealth Is Scaling

Global financial wealth is expanding, but 2025 revealed a widening divide between regions generating wealth at scale through deep capital markets and those held back by policy uncertainty or weak economic fundamentals.

Asia-Pacific remained a key engine of growth, supported by its central role in the AI supply chain, from semiconductor exports in South Korea to accelerating data center investment across Southeast Asia, and strong equity market performance in Hong Kong and Japan. Mainland China led the region, with financial wealth expanding by 15% in 2025 and projected to grow at 9% annually through 2030. The rest of Asia-Pacific grew by 9.2%, with 7% annual growth expected over the same period. Trade barriers remain a risk, but the region is set to remain among the fastest-growing globally.

North America delivered a more measured rise of 7.4%, a step down from an exceptional 2024. A weaker US dollar offset strong equity gains, while performance remained concentrated in a narrow group of mega-cap technology stocks. That concentration leaves the market vulnerable to a correction if the AI capital expenditure cycle turns. Growth is expected to average around 7% annually through 2030, in line with global wealth.

Western Europe was the year's positive surprise, rising $15.3\%$ . This growth was supported by favorable currency movements and a persistently high household savings rate. Underlying equity market performance remained modest, driven by weaker economic momentum and limited exposure to high-growth sectors. Over the next five years, wealth creation in the region is expected to grow at an annual rate of $5\%$ .

In the Middle East and Africa, nominal wealth grew 12.3% in line with a broader rally in emerging markets. Accelerating economic diversification and strong investment activity in the Gulf States underpinned this growth, alongside robust GDP expansion across Sub-Saharan Africa. A 7% five-year CAGR shows real structural momentum, tempered by geopolitical uncertainty, uneven inflation, and the underdeveloped capital markets that still characterize much of the African continent.

## From Concentration to Clustering

Cross-border wealth rose 8.4% to \$15.7 trillion in 2025, lifted by strong market performance and heightened demand for geographical diversification. The top ten booking centers took almost 90% of new cross-border flows. (See Exhibit 2.) They also hold over 80% of existing stock. Concentration is not new in this industry, but it is intensifying.

## EXHIBIT 2

The Top Ten Booking Centers Dominate Cross-Border Flows  
![](images/341081cfe8d4c586fca68a4f653694917df1e940d444010fd55a0a58e15a193a.jpg)  
Sources: BCG Expand Global Wealth Management Database 2026; BCG analysis.  
Note: Wealth in local currency was converted into US\$ at the year-end exchange rate across all time periods.

Sources: BCG Expand Global Wealth Management Database 2026; BCG analysis.
Note: Wealth in local currency was converted into US\$ at the year-end exchange rate across all time periods. Numbers may not sum to 100 due to rounding. $^{1}$ US and Canada.

For the first time, Hong Kong narrowly overtook Switzerland as the world's largest cross-border booking center. (See Exhibit 3.) Cross-border wealth rose $10.7\%$ to $\$2.9$ trillion, driven by mainland China flows and a vigorous stock market that delivered significant IPO activity and strong gains in benchmark-heavy internet platforms. With mainland flows representing over $60\%$ of assets under management, Hong Kong is cementing its role as China's gateway to global markets, though that same concentration ties its trajectory tightly to economic and regulatory developments on the mainland. Growth of around $9\%$ annually is projected through 2030.

Switzerland, also at \$2.9 trillion, grew 7.6%. Its client base is oriented toward Western European markets, with less exposure to the fast-growing market inflows that powered rivals, though that positioning may prove an advantage as geopolitical uncertainty reaffirms Switzerland's role as a core global booking center, attracting flight-to-safety flows from more volatile regions such as the Middle East. Growth is expected to average around 6% annually through 2030.

Singapore is positioned as the most diversified wealth hub in Asia, serving as a neutral conduit between Asian and Western capital markets. That role has made it a beneficiary of safe-haven flows amid US-China tensions. Regulatory stability, institutional credibility, and a strong wealth management ecosystem have attracted over 2,000 single family offices to the city-state as well as more than 100 independent wealth management firms. (See “Independent Wealth Managers Are a Rising Force.”) Cross-border wealth rose 10.3% in 2025 and should stay at around 9% annually over the next five years.

## EXHIBIT 3

Hong Kong Claims the Top Spot as the World’s Largest Booking Center
CROSS-BORDER WEALTH BY SOURCE MARKET (IN \$TRILLIONS)

Hong Kong  
![](images/43733437712d312351b08a0a7846d9c290cc24fc073addf72447cfd5858b00bb.jpg)

Switzerland  
![](images/d459f9add51664a72339c15a21006bae3fb58ed03d27f76bd96f6b1b7d9e8ad0.jpg)

# Independent Wealth Managers Are a Rising Force

Independent wealth managers (IWMs) now control roughly a quarter of US HNW assets and sit in the high teens in Switzerland and Germany. They are also the fastest-growing channel in the UAE, India, and Singapore.

IWMs combine discretionary and advisory offerings, operate with lower client thresholds than private banks (around \$250,000 in many markets), and typically do not rely on a banking license or proprietary product platforms. This translates into distinct client advantages: open-architecture advice without pressure to push in-house

products, diversification across custodians, and integrated access to a broader range of services. IWMs also tend to see lower advisor turnover, longer client relationships, greater flexibility in executing bespoke investments, and a more personalized experience at lower wealth tiers. A \$10 million client may be entry level at a large bank, but a core relationship for an independent.

The channel's scale and growth trajectory vary considerably across markets, with emerging booking centers now outpacing mature ones by a wide margin. (See the exhibit.)

Independent Wealth Managers Enjoy Rapid Rates of Growth, Especially in Emerging Markets

<table><tr><td>MARKET</td><td>AUM ($BILLIONS, RANGE)</td><td>ESTIMATED CAGR (2022-2025)</td><td>FIRMS</td><td>DEFINITION</td></tr><tr><td>US</td><td>3.5K-4K</td><td>10%</td><td>8K-10K</td><td>SEC-registered investment advisors (excl. broker-tied hybrids, banks)</td></tr><tr><td>Switzerland</td><td>1K-1.1K</td><td>5%</td><td>1.3K-1.4K</td><td>FINMA-licensed EAMs/IAMs under FinIA</td></tr><tr><td>Canada</td><td>900-1.2K</td><td>6%-12%</td><td>300-400</td><td>Provincial portfolio manager registrants, private-client subset</td></tr><tr><td>UK</td><td>700-1K</td><td>6%</td><td>400-600</td><td>Financial Conduct Authority DFM/IFAs (excl. SJP, Quilter, banks)</td></tr><tr><td>Germany</td><td>450-550</td><td>8%</td><td>400-500</td><td>BaFin-licensed Vermögensverwalter (WpIG)</td></tr><tr><td>Italy</td><td>200-280</td><td>11%</td><td>200-300</td><td>Listed independents (Azimut), SCFs, MFOs</td></tr><tr><td>Hong Kong</td><td>200-250</td><td>&lt;2%</td><td>70-100</td><td>Non-bank SFC Type 9 EAMs serving private clients</td></tr><tr><td>France</td><td>150-250</td><td>5%</td><td>400-700</td><td>AMF SGPs and CGP cabinets with discretion</td></tr><tr><td>India</td><td>150-250</td><td>15%</td><td>700-1K</td><td>SEBI PMS + RIAs + MFOs + AIF Cat III</td></tr><tr><td>Singapore</td><td>150-200</td><td>12%</td><td>100-150</td><td>MAS-licensed EAMs and multifamily offices</td></tr><tr><td>UAE</td><td>100-150</td><td>20%-30%</td><td>100-120</td><td>DFSA/ADGM independent private-client firms</td></tr><tr><td>Brazil</td><td>100-120</td><td>5%</td><td>150-200</td><td>ANBIMA gestores de patrimônio (excl. escritórios)</td></tr></table>

Sources: BCG analysis; Industry experts.
Note: ADGM = Abu Dhabi Global Market; AIF = alternative investment fund; AMF = Autorité des Marchés Financiers; AUM: assets under management; BaFin: German Federal Financial Supervisory Authority; CGP: Conseiller en Gestion de Patrimoine; DFM: Discretionary Fund Manager; DFSA: Dubai Financial Services Authority; EAM = external asset manager; FCA: = Financial Conduct Authority; FINMA: Swiss Financial Market Supervisory Authority; IAM = independent asset manager; IFA = independent financial advisor; IWM = independent wealth manager; MAS: Monetary Authority of Singapore; MFOs = multi-family offices; PMS = portfolio management services; PWM = private wealth management; RIA = registered investment advisor; SCF= Società di Consulenza Finanziaria; SEC = Securities and Exchange Commission; SEBI = Securities and Exchange Board of India; SFC = Securities and Futures Commission; SGP = Société de Gestion de Portefeuille.

Margins are under pressure from compliance burdens, retrocession restrictions, and rising technology and cyber resilience requirements.

Where the Model Is Under Pressure

While we project growth to remain strong in many markets, independent IWMs now face challenges that disproportionately affect smaller players, particularly in mature markets.

Recruiting senior bankers and their books has become less economical in the US, UK, and Switzerland given tighter retention programs and non-competes; in Singapore, Dubai, and Brazil, the constraint is talent scarcity. Either way, hiring-led growth is harder and more expensive than it was.

The personal nature of the IWM model, long its greatest strength, is becoming a vulnerability. In mature markets, relationships tied to individual advisors often do not transfer as clients hand over wealth, and many next-generation clients choose a different advisor. Firm succession compounds the issue. Independent WMs are typically founder-driven, so when the senior advisor retires, many firms face a continuity question, often resolved through a sale or wind-down.

Margins are under pressure from compliance burdens, retrocession restrictions, and rising technology and cyber resilience 

[中间内容因长度限制已省略]

 will make better decisions about where to invest and where to defend.

\- Attack the highest-cost workflows. Financial planning, portfolio management, and compliance automation represent both the largest cost pools and the clearest near-term AI applications. Automated portfolio drafting, AI-generated rationales, knowledge assistants, and compliance automation should be scaled now. The time for piloting is over.

\- Rebuild the advisor experience around AI. Next-best-action prompts, retention alerts, automated documentation, and personalized outreach need to work as a unified system. Fragmented tools will not close the productivity gap, and advisors who are not fluent in working alongside AI agents will find themselves at a growing disadvantage.

\- Encode institutional knowledge into agents. Pairing top practitioners with engineers to build, govern, and refine AI agents is what separates differentiated capability from generic automation. The judgment of the best advisors needs to be embedded in the agents being built today. Without centralized ownership and evaluation against client outcomes, agent quality will fragment and competitive differentiation will erode.

To get the most out of agentic workflows, wealth managers should introduce a decoupled data layer that separates operational source systems such as core banking from data consumption. This layer should deliver real-time, API-accessible, curated data for AI agents, while ensuring all actions are governed by deterministic control layers such as transaction systems, rules engines, and workflows.

The wealth management industry has long assumed it sits safely on the relationship side of the automation line. The two scenarios in this chapter challenge that assumption. In one, the economics of advice get reshaped but the human core survives. In the other, the advisor becomes optional for a significant share of the market. Most firms are not yet building seriously for either.

## About the Authors

Michael Kahlich is a managing director and partner in BCG's Zurich office. You may contact him by email at kahlich.michael@bcg.com.

Daniel Kessler is a managing director and senior partner in BCG's Zurich office. You may contact him by email at kessler.daniel@bcg.com.

Akin Soysal is a managing director and partner in BCG's Zurich office. You may contact him by email at soysal.akin@bcg.com.

Peter Czerepak is a managing director and senior partner in BCG's Boston office. You may contact him by email at czerepak.peter@bcg.com.

Renaud Fages is a managing director and partner in BCG's Los Angeles office. You may contact him by email at fages.renaud@bcg.com.

Dean Frankle is a managing director and partner in BCG's London office. You may contact him by email at frankle.dean@bcg.com.

Mayank Jha is a managing director and partner in BCG's Mumbai office. You may contact him by email at jha.mayank@bcg.com.

Wei Chuan Lim is a managing director and senior partner in BCG's Singapore office. You may contact him by email at lim.weichuan@bcg.com.

Michael Boardman is a senior advisor in BCG's New York office. You may contact him by email at boardman.michael@advisor.bcg.com.

Yves Robert-Charrue is a senior advisor in BCG's Zurich office. You may contact him by email at robertcharrue.yves@advisor.bcg.com.

Gloria Ong is a managing director and partner in BCG's Singapore office. You may contact her by email at ong.gloria@bcg.com.

Sam Kittross-Schnell is a partner in BCG's Boston office. You may contact him by email at kittrossschnell.sam@bcg.com.

Omar Rahman is a principal in BCG's Zurich office. You may contact him by email at rahman.omar@bcg.com.

If you would like to discuss this report, please contact the authors.

Felix Werner is a project leader in BCG's Frankfurt office. You may contact him by email at werner.felix@bcg.com.

Nisha Mittal is a principal in BCG Expand's Gurugram-India office. You may contact her by email at nisha.mittal@bcgexpand.com.

## For Further Contact

## Acknowledgments

The authors sincerely thank the following BCG and affiliated colleagues for their valuable insights and contributions to this report:

Core operational and market sizing team: Denise Daelemans, Bhawna Jain, Grace Miu, Youssef Intabli, Aayushi Sah, Sevde Temiz, and Amit Parmar.

This year's Global Wealth Report was enriched with data and insights provided by BCG Expand, a wholly owned subsidiary of Boston Consulting Group.

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X.

![](images/7cae113a411c1eee30d5fe2bd5fa20d9019d781637a6fb5ed948d0741043d3ba.jpg)
"""
