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
- 已识别机构名：`UBS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份UBS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Chemical Sector Fluorochemicals: Beneficiary of AI-driven new opportunities

## Fluorochemicals outperformed chemical sector amid AI-driven opportunities

The fluorochemical index has outperformed the broader chemical index by c.9% since early May, which we mainly attribute to 1) the US announcement about a delay in the phase-out of certain third-generation refrigerants across selected applications, and 2) market expectations for growing potential of fluorochemical materials' application in the AI field. We expect fast growth in the AI-related applications of fluorochemicals, amidst the higher compute power demand and the iteration of material systems induced by AI developments. Currently, fluorochemical material suppliers are trading at a notable discount to electronic chemical material firms. We think the market has yet to fully price in the growth opportunities that AI brings to fluorochemical materials and see further re-rating potential for select fluorochemical firms poised to ride the AI tailwinds.

## Semis applications: watching EG-HF, fluorinated fluids and fluorinated gases

We expect domestic semiconductor (semis) chemical material manufacturers to benefit from cyclical recovery and ongoing domestic substitution. We suggest watching: Electronic-grade hydrofluoric acid (EG-HF): G5 (semis-grade) products have higher technical barriers, with the top three producers exerting stronger market influence. Fluorinated fluids: Indispensable in semis manufacturing. The largest producer, 3M, ceased production at end-2025 due to per- and polyfluoroalkyl substances (PFAS) regulations, creating substitution opportunities for Chinese suppliers. Fluorinated gases: Among a wide range of products, we suggest focusing on those with high technical barriers, strong localisation potential and favorable pricing outlooks, such as tungsten hexafluoride and hexafluorobutadiene.

## Data centre applications: eyes on PTFE/liquid cooling chemical materials

Given AI servers' rising requirements for cooling efficiency and low dielectric constants, we see fluorochemical materials as a viable solution. PTFE could serve as a candidate material for next-generation PCB systems, given its low dielectric constant and low dielectric loss. We see leading PTFE producers with advanced technologies as potential beneficiaries. For liquid cooling chemical materials, mainstream solutions have yet to be standardized. We suggest watching 1) refrigerants for cold-plate liquid cooling (with R134a/R1234yf likely to benefit), and 2) the pace of immersion cooling adoption and the choice of cooling medium (where fluorinated fluids look set to benefit).

## We lift PTs for Dongyue/Capchem/EM Technology; we also like Guanggang

We prefer fluorochemical material producers such as Dongyue and Capchem, as well as Guanggang (see note) as potential beneficiaries of AI-driven demand growth. We raise earnings estimates for Dongyue's fluoropolymer/silicone segments, lift profit estimates for Capchem's capacitor chemicals/fluorochemicals, and nudge up revenue estimates for EM Technology's high-frequency resin segment. We lift our price targets based on expectations for AI-driven fluorochemical material demand and peer re-rating.

Figure 1: Earnings estimates and PT changes

<table><tr><td rowspan="2">Company</td><td rowspan="2">Rating</td><td colspan="3">Price target (lcy)</td><td colspan="3">Earnings Change</td><td rowspan="2">2028E earnings exposure to AI-related downstream</td><td colspan="2">PE</td><td>EPS CAGR</td><td rowspan="2">PEG</td></tr><tr><td>New</td><td>Old</td><td>Chg.</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2026-28E</td></tr><tr><td>Capchem</td><td>Buy</td><td>122.0</td><td>86.0</td><td>42%</td><td>21%</td><td>12%</td><td>14%</td><td>15-20%</td><td>31</td><td>25</td><td>18%</td><td>1.8</td></tr><tr><td>Dongyue Group</td><td>Buy</td><td>29.7</td><td>17.5</td><td>70%</td><td>5%</td><td>8%</td><td>7%</td><td>3-5%</td><td>13</td><td>11</td><td>8%</td><td>1.6</td></tr><tr><td>EM Technology</td><td>Buy</td><td>94.1</td><td>41.5</td><td>127%</td><td>1%</td><td>11%</td><td>17%</td><td>60-65%</td><td>96</td><td>56</td><td>53%</td><td>1.8</td></tr><tr><td>Guanggang</td><td>Buy</td><td>42.0</td><td>42.0</td><td>-</td><td></td><td></td><td></td><td>&gt;50%</td><td>101</td><td>63</td><td>52%</td><td>1.9</td></tr></table>

Source: Wind, UBS-S estimates. Note: Pricing data as of 18 June 2026.

Equities

China

Chemicals

Amily Guo

Analyst

amily.guo@ubs.com

+86-105-832 8845

Richard Li

Analyst

S1460121090003

richard-ze.li@ubs.com

+86-21-3866 8802

Jay LIN

Analyst

S1460525070001

jay.lin@ubs.com

+86-105-832 8044

Eason Tang

Analyst

eason.tang@ubs.com

+852-3712 3883

Figure 2: Fluorochemical value chain and its connection with Al  
![](images/51d83f6a0c1e4e0243801ef14d6b28da75acbf1f9f12b01e1390faecbca51eec.jpg)  
Source: UBS-S

## Semis manufacturing: electronic-grade hydrofluoric acid

Electronic-grade hydrofluoric acid (EG-HF) is a key wet electronic chemical. It is an aqueous solution prepared by purifying anhydrous hydrogen fluoride and absorbing it into ultrapure water. EG-HF is one of the larger-scale categories in the field of wet electronic chemicals with relatively rigid demand, with 2025 market size around Rmb4.25bn in China. EG-HF has seen its total addressable market (TAM) driven by downstream capacity expansion (e.g. semis and display panels) as well as domestic substitution. It is mainly used in cleaning and etching processes in semiconductor manufacturing. Cleaning primarily involves removing the natural oxide layer and trace residual impurities from the wafer surface to ensure the interface cleanliness required for subsequent thin-film deposition and processing. Etching, which is primarily based on its chemical reaction with materials such as silicon dioxide, is to achieve precise patterning and structural formation on the wafer surface.

Figure 3: China's electronic-grade hydrofluoric acid consumption and revenue  
![](images/e3299cb0c14870879c195c17222021b81cf24a6f74b14e5b5370370dce21f8b9.jpg)  
Source: Befar Group's H-share IPO prospectus (Application Proof), China Chemical Economic and Technological Development Center (CNCET), Frost & Sullivan analysis

In terms of application and purity levels, EG-HF is classified into grades of EL, UP, UPS, UPSS, and UPSSS (semis G5). UPSSS is currently the highest grade (typically used in 12-inch wafer manufacturing at 55nm and below) and features notably higher technical barriers and pricing than lower-grade products. Global G5 hydrofluoric acid leaders include Stella Chemifa, Kanto Chemical, Soulbrain and ENF Technology.

The supply landscape of G5-grade EG-HF among Chinese companies is concentrated. According to Befar Group's H-share IPO prospectus (Application Proof), China's EG-HF (semis G5) capacity, output and revenue reached 135kt, 74.9kt and Rmb658m in 2025, respectively. Among the approximately 30 domestic EG-HF producers, only a limited number can meet semiconductor G5 standards and deliver sustained, stable supply. The CR5 of G5 electronic hydrofluoric acid supplied by domestic players stands at $98\%$ in 2025. Among listcos, Do-Fluoride, Grandit (Juhua's associated company) and Befar Group are the key domestic suppliers. Sanmei and Capchem also show presence in the market through joint venture/associated companies.

Figure 4: UPSSS-grade EG-HF prices are higher than those of other grades  
![](images/294d06bf0c3b79d1269e8a17f815b6410fa4461b0a0e078f7ec9a6116b25ed94.jpg)  
Source: Baiinfo

We expect Chinese G5 EG-HF producers to benefit from downstream semiconductor demand growth and the trend of import substitution. We expect the fast demand growth of G5-grade EG-HF to sustain driven by AI. On the supply side, reports indicate that the Middle East conflict has tightened global sulfur supply since March, pushing up anhydrous hydrofluoric acid prices and raising expectations for EG-HF price hikes. Supply of high-end G5 products is tight due to robust demand from memory. China is the world's largest supplier of anhydrous hydrofluoric acid. We believe domestic EG-HF producers could benefit from stable raw material supply and further expand their global market share.

Figure 5: China's anhydrous hydrogen fluoride price on the rise overall YTD  
![](images/4b06c06d72cedce2f314ca9e896f8f6606411d9ab2a0a34216ed80370a07895d.jpg)  
Source: Baiinfo

Figure 6: Profile of major domestic EG-HF listcos

<table><tr><td>Company</td><td>Ticker</td><td>Product layout</td><td>Key customers and progress</td></tr><tr><td>Do-Fluoride</td><td>002407.SZ</td><td>Capacity of 60,000 tons/year (40,000 tons semiconductor grade + 20,000 tons photovoltaic grade)</td><td>Semiconductor-grade hydrofluoric acid has been supplied in batches to leading semiconductor manufacturers such as TSMC and Samsung</td></tr><tr><td>Grandit (associate of Juhua)</td><td>688549.SH</td><td>The company disclosed 2021 sales volume of 8,507 tons for integrated circuit applications, with a domestic market share of 20%; According to Bainfo, its subsidiary Kaisheng Fluorochemical has electronic-grade hydrofluoric acid capacity of 28,000 tons</td><td>Supplies leading domestic wafer fabs; obtained SK hynix confirmation for batch supply for 12-inch 1Xnm (10–20 nm) process</td></tr><tr><td>Capchem</td><td>300037.SZ</td><td>Holds a 24.03% equity stake in Fujian Yongjing Technology, expanding into electronic-grade hydrofluoric acid</td><td>Fujian Yongjing&#x27;s hydrofluoric acid has achieved small-batch deliveries to downstream semiconductor and panel customers.</td></tr><tr><td>Befar Group</td><td>601678.SH</td><td>Capacity of 6,000 tons/year (all G5 grade)</td><td>Successfully used by leading domestic semiconductor manufacturers and exported to overseas markets including Japan, South Korea, and Singapore</td></tr><tr><td>Sanmei Chemical</td><td>603379.SH</td><td>Electronic-grade hydrofluoric acid business is arranged through investee company Morita New Materials</td><td>Morita New Materials mainly produces industrial-grade anhydrous hydrofluoric acid and ultra-pure microelectronics etching and cleaning-grade products, used in semiconductor microelectronics manufacturing</td></tr></table>

Source: Company data, Baiinfo

## Semis manufacturing: fluorinated fluids

Fluorinated fluids refer to a large category of high-performance fluids based on fluorinated molecules. They are widely used in cleaning and cooling processes in semiconductor manufacturing, due to their strong chemical inertness, non-flammability, excellent electrical insulation, low surface tension, and minimal residue after volatilisation.

Among mainstream products, hydrofluoroether (HFE) is commonly used for cleaning and drying precision electronic components, as it can penetrate microstructures by leveraging its low surface tension and high volatility to remove particles, organic residues, and moisture. Perfluoropolyether (PFPE) is primarily applied in high-end thermal management applications. With superior chemical stability and insulation properties, PFPE is primarily used for temperature control and cooling in semis etching processes. In addition, some perfluorocarbons and other fluorinated fluids are also used for cleaning and temperature control during semis manufacturing.

Fluorinated fluids are essential in semis manufacturing, while 3M's exit from PFAS production may lead to a substantial supply shortfall. HFE and PFPE, as mainstream fluorinated fluids, are both PFAS, which have been under increasingly stringent regulation globally in recent years due to their high persistence, non-degradability and potential environmental and health risks. The US and Europe have been shifting their regulatory frameworks from single-product restrictions to broader category controls (see Japan ESG and Sustainability Research "Update", Leigha Miyata, 28 May 2026). Against this backdrop, 3M, the world's largest supplier of semis-grade fluoridated fluids, exited from PFAS manufacturing at end-2025. Given the lack of substitutes (overseas regulators are considering longer exemption periods for critical applications, including electronics and semis), the semis industry may face a significant deficit in fluorinated fluid supply (see "APAC Focus: Exploring opportunities in the China fluorine chemicals sector," Amily Guo, 24 Jan 2024).

Figure 7: PFAS substitutes and Chinese manufacturers (by chemical)

<table><tr><td>Chemical</td><td>Category</td><td>Application</td><td>Non-PFAS Alternative (Chinese producer)</td><td>Availability</td></tr><tr><td>HFCs (HFC-125, HFC-134a, etc.)</td><td>Refrigerant</td><td>Application for fluorinated gases - Refrigeration</td><td>Hydrocarbon refrigerant (Juhua, Dymatic)</td><td>Mature for some uses, early stage for others</td></tr><tr><td rowspan="3">PFPE &amp; HFE</td><td rowspan="3">Fine chemical</td><td>Electronics- Data center immersion cooling agent</td><td>Silicone oil (Runhe High-tech Materials), Synthetic Hydrocarbon oil</td><td>Mature for some uses, early stage for others</td></tr><tr><td>Semiconductor-Heat transfer fluid</td><td>-</td><td>Immature</td></tr><tr><td>Industrials-Lubricant in harsh conditions / for safety equipment</td><td>-</td><td>Immature for some uses</td></tr><tr><td>Hexafluoroethane (C2F6)Carbon tetrafluoride (CF4)</td><td>Electronic gas</td><td>Electronics-Dry etching, chamber cleaning for chip manufacture</td><td>Nitrogen trifluoride (NF3, Peric, Nata, Haohua, Huate)</td><td>Mature for some uses</td></tr><tr><td rowspan="7">PTFE</td><td rowspan="7">Fluoropolymer</td><td>Industrials-Gasket</td><td>PU (Wanhua), Graphite (BTR, Xiang Fenghua)</td><td>Mature for some uses</td></tr><tr><td>Industrials-Engineering Plastic</td><td>PE/PP (SinoChem, Hengli, Rongsheng etc.)</td><td>Mature for mid-to-low end uses</td></tr><tr><td>Consumer-Non-stick pan coating</td><td>Ceramic (Sinocera), Andonized Aluminum (Yunan Aluminum, Nanshan Aluminum)</td><td>Mature, likely higher cost</td></tr><tr><td>Electronics-PCB CCL</td><td>PPO/Hydrocarbon resin (EM Technology)</td><td>Mature for some uses</td></tr><tr><td>Electronics-insulation and fireproof</td><td>PVC (Sanyou, Junzheng Group), PE/PP (SinoChem, Hengli, Rongsheng etc.)</td><td>Mature for mid-to-low end uses</td></tr><tr><td>Healthcare-some medical devices (guidewire, artificial blood vessels, etc.)</td><td>PA, HDPE (Rongsheng, Satellite Chemical, Wanhua)</td><td>Early stage for some uses, immature for others</td></tr><tr><td>Aviation and aerospace- mechanical component</td><td>-</td><td>Immature</td></tr><tr><td rowspan="2">FEP</td><td rowspan="2">Fluoropolymer</td><td>Electronics-insulation and fireproof</td><td>PVC (Sanyou, Junzheng Group), PE/PP (SinoChem, Hengli, Rongsheng etc.)</td><td>Mature for mid-to-low end uses</td></tr><tr><td>Healthcare-some medical devices (guidewire, artificial blood vessels, etc.)</td><td>PA, HDPE (Rongsheng, Satellite Chemical, Wanhua)</td><td>Early stage for some uses, immature for others</td></tr><tr><td></td><td></td><td>Industrials-Engineering Plastic</td><td>PE/PP (SinoChem, Hengli, Rongsheng etc.)</td><td>Mature for mid-to-low end uses</td></tr><tr><td></td><td></td><td>Aviation and aerospace- mechanical component</td><td>-</td><td>Immature</td></tr><tr><td rowspan="4">PVDF</td><td rowspan="4">Fluoropolymer</td><td>Industrials-Coating</td><td>Silicon Modified Polyester</td><td>Mature</td></tr><tr><td>Energy-Solar back panel</td><td>PET &amp; PA membrane (EM technology, Shuangxing), Glass panel (Xinyi Solar, Flat)</td><td>Mature</td></tr><tr><td>Energy-EV battery separator coating</td><td>Boehmite/aluminium oxide (Sinocera, Estone), Aramid fibre (Tayho), PMMA (Wanhua, Enjie)</td><td>Mature, likely higher cost for some alternatives</td></tr><tr><td>Energy-EV battery cathode binder</td><td>Polyimide (Tinci, lone)</td><td>Immature</td></tr><tr><td>FKM</td><td>Fluoropolymer</td><td>Automobile-exhaust after treatment system</td><td>Silicone rubber (Hoshine, Dongyue), Polyurethane (Wanhua)</td><td>Mature for some uses</td></tr><tr><td>PFSA</td><td>Fluoropolymer</td><td>Energy-Fuel Cell/Electrolyzer PEM</td><td>PEEK (ZYPEEK), Non-fluorine PEM (Valiant)</td><td>Immature</td></tr></table>

Source: UBS estimates, UBS-S estimates Note: APAC Focus: Exploring opportunities in the China fluorine chemicals sector, Amily Guo, 24 Jan 2024

Figure 8: 3M's PFAS net sales and EBITDA (US\$bn)  
![](images/92507615f5302a949d37247b65f193f5e0fcf26eb1bcdf4481279869055c294c.jpg)  
Source: Company data, UBS-S

Figure 9: Semis and auto contributed 35-40% of 3M's PFAS revenue  
![](images/527b83243e1420fe4bdc5c26fcc54ed54317ada58177a857e0aa2df38f45d94e.jpg)  
Source: Company data, UBS, see note 3M Company "Plan to Phase Out PFAS Production by YE 2025"

Chinese fluorinated fluid producers are embracing domestic substitution opportunities, with Capchem being better positioned in the semis-grade fluorinated fluid segment. 3M's exit from PFAS production has created considerable substitution demand, and Chinese suppliers are grasping the opportunity, with Capchem, Zhejiang Juhua and Yongtai Technology having established capacity in fluorinated fluids. Among them, we think Capchem is better placed to capture the substitution demand in the semis space. Since fluorinated fluids directly impact process stability and product yields in downstream wafer manufacturing, the industry has high technical barriers, long customer verification cycles and high entry barriers. As such, first

Leveraging its well-established product development and application service capabilities, Capchem has built stable partnerships with major domestic fabs (covering both logic and memory), OEMs, and cooling equipment manufacturers. In the field of semiconductor cooling fluid, the company ranks No.1 among domestic players in China by market share. As for capacity layout, Capchem has built 3ktpa HFE capacity and 2.5ktpa PFPE capacity, and plans to release capacity in a timely manner, based on the construction progress of its 30ktpa high-end fluorinated fine chemicals project and evolving market demand dynamics.

Figure 10: Fluorinated fluid capacity layout of main listcos

<table><tr><td>Company</td><td>Ticker</td><td>Product matrix</td><td>Progress in semis/data centre applications</td></tr><tr><td>Capchem</td><td>300037.SZ</td><td>3ktpa HFE capacity + 2.5ktpa PFPE capacity</td><td>Stable mass shipments of fluorinated fluids (incl. HFE/PFPE) to clients for semis process cooling, precision cleaning, and immersion cooling in data centres etc.</td></tr><tr><td>Juhua</td><td>600160.SH</td><td>Electronic fluorinated fluids include HFE D 

[中间内容因长度限制已省略]

lated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
