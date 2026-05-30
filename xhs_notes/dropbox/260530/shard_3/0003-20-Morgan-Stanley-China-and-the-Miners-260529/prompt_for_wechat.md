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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Australia Materials | Asia Pacific

# China and the Miners

Our monthly report summarizes key data/charts from China to give investors quick insights into China's macroenvironment and its demand for mineral resources.

China view – Energy Shock and Weaker Consumption: Our China economics team notes that April activity slowed more sharply than expected, weighed by the oil shock impacting energy-intensive sectors and broad-based consumption weakness, with retail sales dropping to a record low ex-Covid and property showing no signs of stabilization despite selective gains in top-tier secondary markets. While export-linked production (EVs, machinery, tech) remained resilient on AI-led global capex strength, they cut 2Q GDP tracking by 20bps to 4.5%Y, and expect a recovery toward 5%Y in 2H as the oil shock fades and exports stay strong, although consumption is likely to lag amid weak labour markets, fading policy support, and ongoing property adjustment (see here).

Macro – Production Declines for Majority: China's IP was 4.1% YoY in April (Mar 5.7%); April PMI was 50.3 (Mar 50.4). April CPI was 1.2% YoY (Mar 1.0%). New property starts fell 27.1% YoY in April (Mar -17.1% YoY) and GFA sold fell 10.3% YoY in April (Mar -8.0% YoY). Our China property team notes that while secondary home sales in top-tier cities exceeded expectations in March–April, momentum has slowed sharply in May, with divergence widening across cities as lower-tier markets continue to weaken in both listings and prices. Combined with fragile sentiment and fading policy support, they remain cautious on the rebound's durability, although near-term declines may stay modest on favorable base effects. FAI was down 9.4% YoY in April (Mar +1.6% YoY). April aluminum production was up 3.1% YoY to 3.9mnt, reflecting capacity resumption in Liaoning.

Commodities data – Steel Exports Slowed: Steel exports in April decreased 9% YoY to 9.5mnt, and crude steel output was down 2.8% YoY in April, while domestic steel apparent consumption fell 3.1% YoY. China's iron ore imports were up 1% YoY in April to 104mnt. Port inventories started to draw slowly during the month but remain elevated.

How are we positioned? BHP.AX remains our preferred diversified exposure, supported by low-cost WAIO cash generation with accretive 330Mtpa expansion optionality, Copper SA valuation upside, potential for further asset crystallisation, and stronger long term growth profile than peers (see our recent insight note here). Our iron ore order of preference: BHP.AX (OW), DRR.AX (OW), RIO.AX (EW), then FMG.AX (UW). In coal, WHC.AX (OW) is most preferred (#1 in our OOP, see our 2Q Strategy), supported by potential gas-to-coal switching in North Asia and tight met coal following the major coal mine accident in Shanxi, triggering safety inspections. We remain OW S32.AX for base metals exposure, with aluminium supported by supply disruption, high energy prices and a slower Indonesian ramp. In lithium, we see some merit in taking profits; we are EW PLS, remaining preferred over IGO (UW), with the Greenbushes LOM plan still a key uncertainty.

MS AUSTRALIA LIMITED+

# Rahul Anand, CFA

Equity Analyst

R.Anand@morganstanley.com

+61 2 9770-1136

# Michael A Stancliff

Research Associate

Michael.Stancliff@morganstanley.com

+61 2 9770-9253

# AUSTRALIA MATERIALS

Asia Pacific

Industry View

Attractive

# Recent Research:

Asia Energy Security and AI: Energy Meets
Compute: Supercycle Recharges (21 May 2026)
Mineral Resources Limited: TripNotes: Wodgina
Site Visit (20 May 2026)
BHP Group Ltd: Rising data centre build favours
BHP's commodity mix – but there's plenty of
alpha too (13 May 2026)
Boss Energy Ltd: Updating Estimates and Price
Target (1 May 2026)
Mineral Resources Limited: Updating Estimates
(30 Apr 2026)
South32 Ltd: Hermosa: Higher capex somewhat
offset by longer life. A large overhang is
removed with modest impact expected. (29 Apr
2026)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# Industrial Production Data and Trade Data

# IP data:

New starts were down 27.1% YoY in April, and GFA sold fell 10.3% YoY, while property completions were down 19.0% YoY. Our China property team notes that while secondary home sales in top-tier cities exceeded expectations in March–April, momentum has slowed sharply in May, with divergence widening across cities as lower-tier markets continue to weaken in both listings and prices. Combined with fragile sentiment and fading policy support, they remain cautious on the durability of the rebound, although near-term declines may stay modest on favorable base effects.

Domestic steel apparent consumption decreased 3.1% YoY in April, together with a 9% decline in net exports while key steel mills production was down 5.7% YoY in April.

April aluminum production was up 3.1% YoY, to 3.9mnt. The slight MoM increase in production volume was mainly due to capacity resumption in Liaoning province. Currently, the total operating capacity in China has reached 45.3mnt, which is at the ceiling imposed by China's government with limited upside.

April coal production was down 1% YoY and down 12.5% MoM to 386mnt. The MoM drop in coal volume mainly reflected the seasonal decline, as the winter heating season ended in March. Total coal production increased 1.2% YoY YTD. Thermal power generation rose 3.1% YoY in April to 463.8bn kWh, accounting for 62% of total power generation vs. 66% in Mar-26 as hydro power generation gradually picked up moving towards the rainy season.

# Trade data:

Iron ore imports were up 1% YoY in April to 104Mt. Port inventories in China started to draw slowly during the month but remain elevated. Pig iron production at steel mills is down 4% YTD.

Coal imports decreased 13% YoY and 15% MoM in April to 33Mt. Total YTD coal imports in 4M26 were down by 2% YoY to 149mnt. The decline in coal imports reflected the seasonal decline in demand in slow consumption season and higher imported coal prices.

The following material was published in a report titled: China Materials: April IP Data: Production Declines for Majority (18 May 2026)

Property – New starts fell 27.1% YoY in April (vs. -17.1% YoY in March). GFA sold fell 10.3% YoY (vs. -8% YoY in March) and property completions were down 19% YoY (vs. -19.3% YoY in March), all based on restated data for 2025. While secondary real-time home sales in select high-tier cities beat market expectations in March-April, our China property team notes a rapid deceleration so far in May. Also, they note further divergence among cities in terms of secondary listing volume and listing prices, with select tier-2 and low-tier cities continuing to worsen. Together with still-fragile resident sentiment and diminishing effects of recent city-level policies, the team remains prudent about the durability of the sales rebound, although the drops may remain narrow in coming months on favorable bases.

FAI was down $9.4\%$ YoY in April 26 (vs. $+1.6\%$ YoY in March). Highway FAI slipped $18.1\%$ YoY in April.

Crude steel output was -2.8% YoY in April (vs. -6.3% YoY in March). 4M26 production was down 4.1% YoY. We estimate domestic steel apparent consumption was down 3.1% in April (vs. -7.1% YoY in March), together with a 9% decline in net exports.

Cement production was -10.8% YoY in April (vs. -21% YoY in March). 4M26 production was down 8.6% YoY. Output YoY decline is narrowing in May due to lower base numbers. The cement price hikes in east China continued to decline in April-May due to weak downstream demand and wet weather conditions.

Aluminum production was up 3.1% YoY and 0.5% MoM to 3.9mnt in Apr 26. The slight MoM increase in production volume was mainly due to capacity resumption in Liaoning province. Currently, the total operating capacity in China has reached 45.3mnt, which is at the ceiling imposed by China's government with limited upside. Constrained by the limited supply increase, aluminum smelters saw solid margins >Rmb8,600/t in April.

Coal production was down 1% YoY and down 12.5% MoM to 386mnt in April 2026. The MoM drop in coal volume mainly reflected the seasonal decline, as the winter heating season ended in March. Total coal production increased 1.2% YoY YTD. Thermal power generation rose 3.1% YoY in April to 463.8bn kWh, accounting for 62% of total power generation vs. 66% in Mar-26 as hydro power generation gradually picked up moving towards the rainy season.

Exhibit 1: April 2026 industrial production data 

<table><tr><td>Apr 2026 Production Data</td><td>Growth rate trend</td><td>Apr 2026</td><td>MoM Apr 2026</td><td>YoY Apr 2026</td><td>Mar 2026</td><td>Jan+Feb 2026</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>Sep-25</td><td>Aug-25</td><td>Jul-25</td><td>Jun-25</td><td>May-25</td><td>Apr-25</td><td>2025</td></tr><tr><td>Crude steel (Mnt)</td><td></td><td>83.6</td><td>-3.9%</td><td>-2.8%</td><td>-6.3%</td><td>-3.6%</td><td>-10.3%</td><td>-10.9%</td><td>-12.1%</td><td>-4.6%</td><td>-0.7%</td><td>-4.0%</td><td>-9.2%</td><td>-6.9%</td><td>0.0%</td><td>-4.4%</td></tr><tr><td>Finished steel (Mnt)</td><td></td><td>122.6</td><td>-6.4%</td><td>-1.7%</td><td>-2.3%</td><td>-1.1%</td><td>-3.8%</td><td>-2.6%</td><td>-0.9%</td><td>5.1%</td><td>9.7%</td><td>6.4%</td><td>1.8%</td><td>3.4%</td><td>6.6%</td><td>3.1%</td></tr><tr><td>Cement (Mnt)</td><td></td><td>145.7</td><td>18.4%</td><td>-10.8%</td><td>-21.0%</td><td>6.8%</td><td>-6.6%</td><td>-8.2%</td><td>-15.8%</td><td>-8.6%</td><td>-6.2%</td><td>-5.6%</td><td>-5.3%</td><td>-8.1%</td><td>-5.3%</td><td>-6.9%</td></tr><tr><td>Aluminum (Mnt)</td><td></td><td>3.9</td><td>0.5%</td><td>3.1%</td><td>2.7%</td><td>3.0%</td><td>3.0%</td><td>2.5%</td><td>0.4%</td><td>1.8%</td><td>-0.5%</td><td>0.6%</td><td>3.4%</td><td>5.0%</td><td>4.2%</td><td>2.4%</td></tr><tr><td>Glass (mn wt cases)</td><td></td><td>72.8</td><td>-4.6%</td><td>-7.9%</td><td>-6.6%</td><td>-3.5%</td><td>3.4%</td><td>3.7%</td><td>3.3%</td><td>-9.7%</td><td>-2.0%</td><td>-3.4%</td><td>-4.5%</td><td>-5.7%</td><td>-4.6%</td><td>-3.0%</td></tr><tr><td>Coal production (Mnt)</td><td></td><td>385.6</td><td>-12.5%</td><td>-1.0%</td><td>0.0%</td><td>-0.3%</td><td>-1.0%</td><td>-0.5%</td><td>-2.3%</td><td>-1.8%</td><td>-3.2%</td><td>-3.8%</td><td>3.0%</td><td>4.2%</td><td>3.8%</td><td>1.2%</td></tr><tr><td>Thermal power generation (kWH bn)</td><td></td><td>463.8</td><td>-12.9%</td><td>3.1%</td><td>4.2%</td><td>3.3%</td><td>-3.2%</td><td>-4.2%</td><td>7.3%</td><td>-5.4%</td><td>1.7%</td><td>4.3%</td><td>1.1%</td><td>1.2%</td><td>-2.3%</td><td>-1.0%</td></tr><tr><td>FAI, % YoY</td><td></td><td>-9.4%</td><td>-11.0ppt</td><td>-9.4%</td><td>1.6%</td><td>-4.4%</td><td>-15.1%</td><td>-12.0%</td><td>-12.2%</td><td>-7.1%</td><td>-7.1%</td><td>-5.3%</td><td>-0.1%</td><td>2.7%</td><td>3.5%</td><td>-3.8%</td></tr><tr><td>IP, %, YoY</td><td></td><td>4.1%</td><td>-1.6ppt</td><td>4.1%</td><td>5.7%</td><td>6.3%</td><td>5.2%</td><td>4.8%</td><td>4.9%</td><td>6.5%</td><td>5.2%</td><td>5.7%</td><td>6.8%</td><td>5.8%</td><td>6.1%</td><td>5.9%</td></tr><tr><td colspan="17">Property</td></tr><tr><td>FS starts (mn sqm)</td><td></td><td>35.3</td><td>-33.3%</td><td>-27.1%</td><td>-17.1%</td><td>-23.1%</td><td>-19.3%</td><td>-27.7%</td><td>-29.3%</td><td>-15.0%</td><td>-19.8%</td><td>-15.2%</td><td>-9.5%</td><td>-18.7%</td><td>-22.3%</td><td>-20.5%</td></tr><tr><td>FS sold (mn sqm)</td><td></td><td>57.3</td><td>-44.0%</td><td>-10.3%</td><td>-8.0%</td><td>-13.5%</td><td>-16.6%</td><td>-17.9%</td><td>-19.6%</td><td>-11.9%</td><td>-11.0%</td><td>-8.4%</td><td>-6.6%</td><td>-4.6%</td><td>-2.9%</td><td>-9.5%</td></tr><tr><td>FS completions (mn sqm)</td><td></td><td>21.0</td><td>-39.6%</td><td>-19.0%</td><td>-19.3%</td><td>-27.9%</td><td>-18.4%</td><td>-25.4%</td><td>-27.9%</td><td>0.4%</td><td>-21.3%</td><td>-29.4%</td><td>-2.2%</td><td>-19.1%</td><td>-28.2%</td><td>-18.2%</td></tr><tr><td>Investment (Rmb bn)</td><td></td><td>624.9</td><td>-22.9%</td><td>-20.1%</td><td>-11.7%</td><td>-10.3%</td><td>-36.8%</td><td>-31.4%</td><td>-23.2%</td><td>-21.3%</td><td>-19.9%</td><td>-17.1%</td><td>-12.4%</td><td>-12.4%</td><td>-11.5%</td><td>-17.4%</td></tr><tr><td colspan="17">Infrastructure FAI</td></tr><tr><td>Highway (Rmb bn)*</td><td></td><td>280.6</td><td>-46.3%</td><td>-18.1%</td><td>5.6%</td><td>-0.6%</td><td>-18.4%</td><td>-8.7%</td><td>-15.4%</td><td>0.9%</td><td>-11.6%</td><td>-16.6%</td><td>3.4%</td><td>1.1%</td><td>-2.7%</td><td>-6.0%</td></tr></table>

Source: National Bureau of Statistics, MS. \*Note: Railway and highway FAI growth is rebased.

The following material was published in our recent report: China Materials: April Trade Data: Aluminium Exports Start to Rise (10 May 2026)

Steel exports in April decreased 9% YoY but improved 4% MoM to 9.5Mt, which is slower than we expected. We think steel billets export may grow quickly in April. Daily production of CISA member mills decreased 5.7% YoY in April (vs -6.1% YoY in March).

China's imports of copper and copper products (refined + alloys) were 452kt in April, up $9 \%$ MoM and $3 \%$ YoY. A pullback in the copper price in March encouraged Chinese buyers to re-engage, with the import arbitrage opening briefly. Despite the higher imports, inventories drew strongly during the month, potentially driven by downstream restocking. The Yangshan premium held between \$60 and \$75/t during the month. Copper ore and concentrate imports fell 11% MoM and 20% YoY to 2.35 mln tonnes as treatment charges fell, although strong sulphuric acid prices supported smelter margins.

Aluminium and product exports rose 23% MoM and 15% YoY to 598kt in April to the highest level since November 2024. Supply disruptions in the Middle East drove ex-China tightness and took LME prices higher, widening the export arbitrage. Despite these strong exports, Chinese aluminium inventories rose to all-time highs, and have not yet started to draw.

China's iron ore imports totalled 104Mt in April, down $1\%$ MoM and up $1\%$ YoY. Port inventories in China started to draw slowly during the month but remain elevated. Pig iron production at steel mills is down $4\%$ YTD. China lifted the ban on procuring BHP's seaborne cargoes including previously restricted products during the month which may ease some of the tightness.

Coal imports were down 13% YoY and 15% MoM in April 2026, to 33mnt. Total YTD coal imports in 4M26 were down by 2% YoY to 149mnt. The decline in coal import reflected the seasonal decline in demand in slow consumption season and higher imported coal prices. May coal imports may see some rebound MoM on restocking at power plants in China to prepare for the upcoming peak consumption in summer. The improved demand would support coal prices to further go up in the near term.

Exhibit 2: China: April 2026 trade data 

<table><tr><td rowspan="2">Apr 2026Trade data</td><td rowspan="2">Apr 2025 - Apr 2026</td><td colspan="12">Jan+Feb</td><td rowspan="2">2026YTD</td></tr><tr><td>Apr-26</td><td>Mar-26</td><td>2026</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>Sep-25</td><td>Aug-25</td><td>Jul-25</td><td>Jun-25</td><td>May-25</td><td>Apr-25</td></tr><tr><td rowspan="3">Finished Steel Imports (kt)</td><td></td><td>465</td><td>512</td><td>827</td><td>517</td><td>496</td><td>503</td><td>548</td><td>500</td><td>452</td><td>470</td><td>481</td><td>522</td><td>1,804</td></tr><tr><td>Change %, YoY</td><td>-11%</td><td>2%</td><td>-21%</td><td>-17%</td><td>5%</td><td>-6%</td><td>-1%</td><td>-2%</td><td>-10%</td><td>-18%</td><td>-24%</td><td>-21%</td><td>-13%</td></tr><tr><td>Change %, MoM</td><td>-9%</td><td>39%</td><td>NA</td><td>4%</td><td>-1%</td><td>-8%</td><td>10%</td><td>11%</td><td>-4%</td><td>-2%</td><td>-8%</td><td>4%</td><td>NA</td></tr><tr><td rowspan="3">Finished Steel Exports (kt)</td><td></td><td>9,498</td><td>9,135</td><td>15,591</td><td>11,301</td><td>9,980</td><td>9,782</td><td>10,465</td><td>9,510</td><td>9,836</td><td>9,678</td><td>10,578</td><td>10,462</td><td>34,214</td></tr><tr><td>Change %, YoY</td><td>-9%</td><td>-13%</td><td>-8%</td><td>16%</td><td>8%</td><td>-13%</td><td>3%</td><td>0%</td><td>26%</td><td>11%</td><td>10%</td><td>13%</td><td>-10%</td></tr><tr><td>Change %, MoM</td><td>4%</td><td>17%</td><td>NA</td><td>13%</td><td>2%</td><td>-7%</td><td>10%</td><td>-3%</td><td>2%</td><td>-9%</td><td>1%</td><td>0%</td><td>NA</td></tr><tr><td rowspan="3">Iron Ore Imports (mnt)</td><td></td><td>104</td><td>105</td><td>210</td><td>120</td><td>111</td><td>111</td><td>116</td><td>105</td><td>105</td><td>106</td><td>98</td><td>103</td><td>419</td></tr><tr><td>Change %, YoY</td><td>1%</td><td>11%</td><td>10%</td><td>6%</td><td>9%</td><td>7%</td><td>12%</td><td>4%</td><td>2%</td><td>9%</td><td>-4%</td><td>1%</td><td>8%</td></tr><tr><td>Change %, MoM</td><td>-1%</td><td>7%</td><td>NA</td><td>8%</td><td>-1%</td><td>-4%</td><td>11%</td><td>1%</td><td>-1%</td><td>8%</td><td>-5%</td><td>10%</td><td>NA</td></tr><tr><td rowspan="3">Copper and Products Imports (kt)</td><td></td><td>452</td><td>416</td><td>700</td><td>437</td><td>427</td><td>438</td><td>485</td><td>425</td><td>480</td><td>464</td><td>427</td><td>438</td><td>1,567</td></tr><tr><td>Change %, YoY</td><td>3%</td><td>-11%</td><td>-16%</td><td>-22%</td><td>-19%</td><td>-13%</td><td>1%</td><td>2%</td><td>10%</td><td>6%</td><td>-17%</td><td>0%</td><td>-10%</td></tr><tr><td>Change %, MoM</td><td>9%</td><td>32%</td><td>NA</td><td>2%</td><td>-3%</td><td>-10%</td><td>14%</td><td>-11%</td><td>3%</td><td>9%</td><td>-3%</td><td>-6%</td><td>NA</td></tr><tr><td rowspan="3">Copper Ores &amp; Concentrates Imports (kt)</td><td></td><td>2,352</td><td>2,630</td><td>4,934</td><td>2,704</td><td>2,526</td><td>2,451</td><td>2,587</td><td>2,759</td><td>2,560</td><td>2,350</td><td>2,395</td><td>2,924</td><td>9,915</td></tr><tr><td>Change %, YoY</td><td>-20%</td><td>10%</td><td>5%</td><td>7%</td><td>13%</td><td>6%</td><td>6%</td><td>7%</td><td>18%</td><td>2%</td><td>6%

[中间内容因长度限制已省略]

prietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Australia Materials 

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (05/28/2026)</td></tr><tr><td>Rahul Anand, CFA</td><td></td><td></td></tr><tr><td>BHP Group Ltd (BHPB.L)</td><td>O (09/19/2024)</td><td>3,274p</td></tr><tr><td>BHP Group Ltd (BHGJ.J)</td><td>O (09/19/2024)</td><td>ZAc 71,313</td></tr><tr><td>BHP Group Ltd (BHP.AX)</td><td>O (09/19/2024)</td><td>A$62.31</td></tr><tr><td>Boss Energy Ltd (BOE.AX)</td><td>O (01/16/2026)</td><td>A$1.28</td></tr><tr><td>Deterra Royalties Ltd (DRR.AX)</td><td>O (01/16/2026)</td><td>A$4.50</td></tr><tr><td>Fortescue Metals Group Ltd. (FMG.AX)</td><td>U (01/16/2026)</td><td>A$22.31</td></tr><tr><td>IGO Ltd (IGO.AX)</td><td>U (07/15/2025)</td><td>A$9.58</td></tr><tr><td>Iluka Resources Ltd (ILU.AX)</td><td>O (05/22/2025)</td><td>A$7.90</td></tr><tr><td>Lynas Rare Earths (LYC.AX)</td><td>E (04/14/2026)</td><td>A$19.19</td></tr><tr><td>Mineral Resources Limited (MIN.AX)</td><td>++</td><td>A$73.47</td></tr><tr><td>Paladin Energy Ltd (PDN.AX)</td><td>O (10/08/2025)</td><td>A$11.32</td></tr><tr><td>PLS Group Ltd (PLS.AX)</td><td>E (04/14/2026)</td><td>A$6.46</td></tr><tr><td>Rio Tinto Limited (RIO.AX)</td><td>E (04/09/2025)</td><td>A$185.63</td></tr><tr><td>Sandfire Resources Ltd (SFR.AX)</td><td>U (12/16/2024)</td><td>A$19.63</td></tr><tr><td>South32 Ltd (S32.AX)</td><td>O (12/16/2024)</td><td>A$4.81</td></tr><tr><td>South32 Ltd (S32J.J)</td><td>O (12/16/2024)</td><td>ZAc 5,499</td></tr><tr><td>Whitehaven Coal Ltd (WHC.AX)</td><td>O (04/14/2026)</td><td>A$8.75</td></tr><tr><td>Shannon J Sinha</td><td></td><td></td></tr><tr><td>Nickel Industries (NIC.AX)</td><td>E (04/09/2025)</td><td>A$1.06</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.

© 2026 MS
"""
