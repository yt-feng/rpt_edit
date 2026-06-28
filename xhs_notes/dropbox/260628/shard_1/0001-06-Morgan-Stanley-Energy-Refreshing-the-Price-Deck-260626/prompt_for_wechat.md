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
Energy | North America

# Refreshing the Price Deck

WTI has fallen to \~\$72, oil E&Ps back at pre-conflict levels, and Majors -9% below it. We refresh our estimates for the latest prices. FCF yields are still strong, with '27 median of 12% for oil E&Ps, while intrinsic valuations only reflect \~\$64 WTI. Risk-rewards screen better post the pullback.

## Key Takeaways

WTI oil has fallen another $\sim 15\%$ since the MoU, now back to $\sim$ 72/bbl. Alongside softer crude, energy stocks have also moved lower

We update our price deck to 6/19 strip, WTI assumption falls 12% in '26 while '27 stays at \$70. Our EBITDA ests are -7% vs consensus for FY26 and -6% for '27

For 2Q, our EBITDA ests are in-line with consensus for oil producers and 8% below for gas. We also forecast above consensus 2Q EPS for XOM

At \$70, our oil coverage offers median '27 FCF yield of 10% (12% US E&Ps, 9% Majors, 10% Canada). Valuations reflect \~\$64 WTI. '27 FCF yields of 9% for gas

We retain our preference for Majors and E&Ps with positive rate of change (DVN, PR & CVE). LNG producers VG and Cheniere also screen attractive.

Have stocks corrected too much? Since the US and Iran announced a memorandum of understanding (MoU) on June 14, oil prices have declined another \~15%. WTI now sits at \~\$72, only slightly above pre-conflict levels. Alongside softer crude, energy stocks have also moved lower. Notably, oil E&Ps are now trading back at pre-conflict levels and US Majors -9%. While uncertainty persists around the macro picture, we do think the risk-reward has improved post the pullback. FCF yields are strong, with a 2027 median of \~10% at prices near strip, and stocks intrinsically reflect \~\$64 WTI - below futures and our long-run \$70/bbl price expectation. We view the recent pullback as an opportunity to add exposure to Majors and high-quality E&Ps.

\- Crude Oil. Flows through the Strait of Hormuz have risen sharply over the last few weeks as oil tankers that were previously trapped behind the waterway make their way to market. Vortexa shows oil exports from countries behind the Strait exceeding 10 mb/d over the last week, approaching $\frac{2}{3}$ of pre-conflict levels. This includes a surge in Iranian flows, which have also benefited from eased sanctions and the lifting of the US blockade. Globally, US exports remain historically high and Chinese imports low, both continuing to serve as important buffers for the seaborne oil market. Still, global inventories have already drawn substantially. Fully restoring regional production and refilling storage will take time. See the latest from MS Strategist Martijn Rats here: 'Let the Oil Flow'.

\- Global Gas & LNG. JKM (Asia LNG) prices have fallen back toward \$15/ mmbtu, well off the highs but still up >50% YTD. Recent statements from QatarEnergy point to \~50% recovery in export volumes in about one month

## MS & CO. LLC

<table><tr><td colspan="2">Devin McDermott</td></tr><tr><td colspan="2">Equity Analyst and Commodities Strategist</td></tr><tr><td>Devin.McDermott@morganstanley.com</td><td>+1 212 761-1125</td></tr><tr><td colspan="2">Joe Laetsch, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joe.Laetsch@morganstanley.com</td><td>+1 212 761-8804</td></tr><tr><td colspan="2">Helen Lin</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Helen.Lin@morganstanley.com</td><td>+1 212 761-0766</td></tr><tr><td colspan="2">Svetlana Do</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Svetlana.DO@morganstanley.com</td><td>+1 212 761-2409</td></tr><tr><td colspan="2">Justin W Latran, CFA</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Justin.Latran@morganstanley.com</td><td>+1 212 761-2869</td></tr><tr><td colspan="2">Jacqueline M Kenny</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Jacqueline.Kenny@morganstanley.com</td><td>+1 212 761-2253</td></tr><tr><td colspan="2">Zackary C Warden</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Zackary.Warden@morganstanley.com</td><td>+1 212 761-4164</td></tr></table>

## EXPLORATION & PRODUCTION

<table><tr><td>North AmericaIndustry View</td><td>In-Line</td></tr><tr><td colspan="2">INTEGRATED OIL</td></tr><tr><td>North AmericaIndustry View</td><td>Attractive</td></tr></table>

See our price target changes in Exhibit 33

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

and 80% after two months - a recovery of everything except the damaged trains. This still leaves a very short window to normalize inventories before next winter. Over the last month, global consumption has started to inflect higher again alongside summer weather & storage refill needs. We see some upside to 2H26 post the pullback, followed by a more balanced 2027. See more here and here.

\- US Natural Gas. Prompt Henry Hub prices have been range-bound in the low-to-mid \$3s for most of June. We still do expect a modest improvement in 3Q, supported by higher LNG flows & power burn. LNG exports in June so far are running \~0.3 bcf/d above the May average, with feedgas deliveries to Golden Pass reaching \~600 mmcf/d this week. That said, the outlook softens again into 2027 - reflecting associated gas growth & still-elevated Haynesville activity. That said, the silver lining of lower oil prices is that it could moderate associated gas risks. See more here.

Softer prices, but valuations still attractive. We refresh our price deck and estimates using strip as of 6/19 (see Exhibit 12), lowering our FY26 WTI assumption to \~\$78/bbl (from \~\$88/bbl) with \$73 WTI for the back half of the year, while 2027 is unchanged at \~\$70. For integrated companies, US Gulf Coast refining margin assumptions are moving 22% higher in 2026. Our Henry Hub moves -8% lower for 2027. Overall, price targets move lower by -5% for oil E&Ps and -8% for gas names, but still imply 25% average upside. At prices near strip (\~\$70 WTI), we estimate a median 2027 FCF yield of 10% across our oil coverage (12% for oil E&Ps, 9% for US majors, and 10% for Canada). Intrinsically, oil E&Ps reflect long-run WTI of\~\$64/bbl, \~6% below 12-month strip.

Preliminary 2Q outlook. Incorporating actual 2Q oil & gas prices and downstream margins, our quarterly EBITDA estimates are in-line with consensus for oil producers and 8% below for gas. We also forecast above consensus EPS for XOM.

Exhibit 1: MS Price Deck (Based on 6/19/2026 Strip)

<table><tr><td>MS Model Assumptions</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>103.54</td><td>77.80</td><td>76.72</td><td>84.75</td><td>74.52</td><td>75.00</td></tr><tr><td>WTI ($/Bbl)</td><td>93.00</td><td>74.00</td><td>72.00</td><td>77.92</td><td>70.00</td><td>70.00</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2.90</td><td>3.20</td><td>3.50</td><td>3.66</td><td>3.50</td><td>3.75</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>31.05</td><td>25.02</td><td>24.78</td><td>26.86</td><td>25.49</td><td>25.58</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>29.93</td><td>31.22</td><td>25.87</td><td>25.83</td><td>24.05</td><td>14.20</td></tr></table>

<table><tr><td>Prior MS Assumptions</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>112.00</td><td>103.12</td><td>92.71</td><td>97.26</td><td>76.05</td><td>75.00</td></tr><tr><td>WTI ($/Bbl)</td><td>100.00</td><td>95.00</td><td>85.00</td><td>88.24</td><td>70.00</td><td>70.00</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2.85</td><td>3.20</td><td>3.60</td><td>3.67</td><td>3.80</td><td>3.75</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>33.56</td><td>33.70</td><td>32.62</td><td>31.65</td><td>28.26</td><td>28.04</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>24.66</td><td>23.20</td><td>20.59</td><td>21.19</td><td>14.20</td><td>14.20</td></tr></table>

<table><tr><td>% Change</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>-8%</td><td>-25%</td><td>-17%</td><td>-13%</td><td>-2%</td><td>0%</td></tr><tr><td>WTI ($/Bbl)</td><td>-7%</td><td>-22%</td><td>-15%</td><td>-12%</td><td>0%</td><td>0%</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2%</td><td>0%</td><td>-3%</td><td>0%</td><td>-8%</td><td>0%</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>-7%</td><td>-26%</td><td>-24%</td><td>-15%</td><td>-10%</td><td>-9%</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>21%</td><td>35%</td><td>26%</td><td>22%</td><td>69%</td><td>0%</td></tr></table>

Source: Bloomberg, FactSet, MS estimates. Note: GC 321 Brent crack spread is unadjusted for RINs.

## Key Charts

Exhibit 2: Oil E&Ps are now back to pre-conflict levels (including gas, the E&P sector is -5% below). The group has underperformed the broader market by \~12% over the same period.  
![](images/e27abad03cbe4a824d5f918e023e01163e526190d987bce42449d6b1d550c6e5.jpg)  
Source: Bloomberg, FactSet, MS

Exhibit 3: We estimate consensus is currently pricing in \~\$73 WTI based on 2027 EBITDAX forecasts, higher than the full-year 2027 strip price of \~\$67.  
![](images/83be30febc2b59942f8c718da173e69699ccba5ac7695b283caa364a7fbf0b8c.jpg)  
Source: FactSet, MS estimates

Exhibit 4: The median 2027 FCF yield for our oil coverage is 10% near strip (\~\$70 WTI), 12% looking just at oil E&Ps. This would move by \~3% for every \$10 change in oil.  
![](images/f04245556f0fd2077e3346ee881de7429f11f7cbdcd12d8e442f4073589bb7d9.jpg)  
Source: FactSet, MS estimates.

Exhibit 5: At \$70 WTI, near strip, our oil coverage has 5% downside vs consensus estimates (7% downside for just oil E&Ps).  
![](images/31b4f14b839379194c9a5b537278535a9f0b37480872bdbd7f45da2468d8335c.jpg)  
Source: MS estimates.

Exhibit 6: Our 2027 FCF estimates are \~11% below consensus...  
![](images/9b7cede9d5f8003745db7c13dd8f35d55cc8f136d083fc7f2e539ff417c908c3.jpg)  
Source: FactSet, MS estimates. Note: Axis cut at 30%

Exhibit 7: ...with 2027 EBITDA 6% below consensus.  
![](images/225f7c2a7b0c0ee93f0c38dd3096859aa4f901bedc4631e7a004a16ec2e0e650.jpg)  
Source: FactSet, MS estimates. Note: Axis cut at 2%

Exhibit 8: Our oil coverage has hedged $\sim 5\%$ of 2027 production on average...  
![](images/45f6a6042e955b0b62f43dcb841618f2d132c53c3f3fb12d23d98990ade9cd77.jpg)  
Source: Company Data, MS estimates

Exhibit 9: ...and \~30% for gas E&Ps  
![](images/f569fa276f916538d1b5028eb5a5be2259ba730b84b46a5b0225dbab17df7aad.jpg)  
Source: Company Data, MS estimates

Exhibit 10: Our oil coverage is pricing an average WTI price of \~\$64, \~6% below 12-month strip.  
![](images/28f954f6dba87eadffbd43393ac2b955ff8148cc348374f93d22b3d5b899bd01.jpg)  
Source: Bloomberg, MS. Note: close prices of 6.24.26.

Exhibit 11: Gas E&Ps reflect an average Henry Hub price of \~\$3.50, at the 12 month strip.  
![](images/ca1bd49898696efef0c05a7f5f2ca03698f60f7c0ab0ea93fbcdccdceaa5c11b.jpg)  
Source: Bloomberg, MS. Note: close prices of 6.24.26

## Price Target Changes

Exhibit 12: MS Price Deck (Based on 6/19/2026 Strip)

<table><tr><td>MS Model Assumptions</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>103.54</td><td>77.80</td><td>76.72</td><td>84.75</td><td>74.52</td><td>75.00</td></tr><tr><td>WTI ($/Bbl)</td><td>93.00</td><td>74.00</td><td>72.00</td><td>77.92</td><td>70.00</td><td>70.00</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2.90</td><td>3.20</td><td>3.50</td><td>3.66</td><td>3.50</td><td>3.75</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>31.05</td><td>25.02</td><td>24.78</td><td>26.86</td><td>25.49</td><td>25.58</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>29.93</td><td>31.22</td><td>25.87</td><td>25.83</td><td>24.05</td><td>14.20</td></tr></table>

<table><tr><td>Prior MS Assumptions</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>112.00</td><td>103.12</td><td>92.71</td><td>97.26</td><td>76.05</td><td>75.00</td></tr><tr><td>WTI ($/Bbl)</td><td>100.00</td><td>95.00</td><td>85.00</td><td>88.24</td><td>70.00</td><td>70.00</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2.85</td><td>3.20</td><td>3.60</td><td>3.67</td><td>3.80</td><td>3.75</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>33.56</td><td>33.70</td><td>32.62</td><td>31.65</td><td>28.26</td><td>28.04</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>24.66</td><td>23.20</td><td>20.59</td><td>21.19</td><td>14.20</td><td>14.20</td></tr></table>

<table><tr><td>% Change</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E+</td></tr><tr><td>Brent ($/Bbl)</td><td>-8%</td><td>-25%</td><td>-17%</td><td>-13%</td><td>-2%</td><td>0%</td></tr><tr><td>WTI ($/Bbl)</td><td>-7%</td><td>-22%</td><td>-15%</td><td>-12%</td><td>0%</td><td>0%</td></tr><tr><td>Henry Hub ($/MMBtu)</td><td>2%</td><td>0%</td><td>-3%</td><td>0%</td><td>-8%</td><td>0%</td></tr><tr><td>Mont Belvieu NGL ($/Bbl)</td><td>-7%</td><td>-26%</td><td>-24%</td><td>-15%</td><td>-10%</td><td>-9%</td></tr><tr><td>GC 321 Brent ($/Bbl)</td><td>21%</td><td>35%</td><td>26%</td><td>22%</td><td>69%</td><td>0%</td></tr></table>

Source: Bloomberg, FactSet, MS estimates. Note: GC 321 Brent crack spread is unadjusted for RINs.

Exhibit 13: Price Target Changes

<table><tr><td>Company</td><td>Ticker</td><td>New PT</td><td>Old PT</td><td> $\Delta (\%)$ </td><td>New Rating</td><td>Old Rating</td><td>PT% Upside</td></tr><tr><td colspan="8">US Majors</td></tr><tr><td>Chevron Corp.</td><td>CVX</td><td>210</td><td>214</td><td>(2%)</td><td>OW</td><td>OW</td><td>22%</td></tr><tr><td>Exxon Mobil Corporation</td><td>XOM</td><td>168</td><td>171</td><td>(2%)</td><td>OW</td><td>OW</td><td>22%</td></tr><tr><td>Integrateds Median</td><td></td><td></td><td></td><td>(2%)</td><td></td><td></td><td>22%</td></tr><tr><td colspan="8">Canadian Integrateds (CAD unless noted)</td></tr><tr><td>Canadian Natural Resources Ltd</td><td>CNQ</td><td>67</td><td>67</td><td>0%</td><td>EW</td><td>EW</td><td>19%</td></tr><tr><td>Cenovus Energy Inc</td><td>CVE</td><td>43</td><td>43</td><td>0%</td><td>OW</td><td>OW</td><td>23%</td></tr><tr><td>Imperial Oil Ltd</td><td>IMO</td><td>138</td><td>141</td><td>(2%)</td><td>EW</td><td>EW</td><td>(14%)</td></tr><tr><td>Suncor Energy Inc</td><td>SU</td><td>92</td><td>93</td><td>(1%)</td><td>EW</td><td>EW</td><td>19%</td></tr><tr><td>Canadian Integrateds Median</td><td></td><td></td><td></td><td>(1%)</td><td></td><td></td><td>19%</td></tr><tr><td colspan="8">Oil E&amp;Ps</td></tr><tr><td>APA Corp.</td><td>APA</td><td>41</td><td>44</td><td>(7%)</td><td>UW</td><td>UW</td><td>23%</td></tr><tr><td>Chord Energy Corp.</td><td>CHRD</td><td>169</td><td>175</td><td>(3%)</td><td>OW</td><td>OW</td><td>41%</td></tr><tr><td>ConocoPhillips</td><td>COP</td><td>146</td><td>153</td><td>(5%)</td><td>OW</td><td>OW</td><td>37%</td></tr><tr><td>Devon Energy Corp.</td><td>DVN</td><td>63</td><td>66</td><td>(5%)</td><td>OW</td><td>OW</td><td>48%</td></tr><tr><td>Diamondback Energy, Inc.</td><td>FANG</td><td>216</td><td>229</td><td>(6%)</td><td>OW</td><td>OW</td><td>18%</td></tr><tr><td>EOG Resources Inc.</td><td>EOG</td><td>156</td><td>160</td><td>(3%)</td><td>EW</td><td>EW</td><td>17%</td></tr><tr><td>Matador Resources Co.</td><td>MTDR</td><td>66</td><td>75</td><td>(12%)</td><td>EW</td><td>EW</td><td>32%</td></tr><tr><td>Murphy Oil Corp.</td><td>MUR</td><td>35</td><td>37</td><td>(5%)</td><td>UW</td><td>UW</td><td>(1%)</td></tr><tr><td>Northern Oil and Gas, Inc.</td><td>NOG</td><td>25</td><td>29</td><td>(14%)</td><td>UW</td><td>UW</td><td>27%</td></tr><tr><td>Occidental Petroleum Corp.</td><td>OXY</td><td>68</td><td>74</td><td>(8%)</td><td>EW</td><td>EW</td><td>33%</td></tr><tr><td>Ovintiv Inc.</td><td>OVV</td><td>65</td><td>68</td><td>(4%)</td><td>EW</td><td>EW</td><td>21%</td></tr><tr><td>Permian Resources Corp.</td><td>PR</td><td>24</td><td>25</td><td>(4%)</td><td>OW</td><td>OW</td><td>27%</td></tr><tr><td>Oil E&amp;Ps Median</td><td></td><td></td><td></td><td>(5%)</td><td></td><td></td><td>27%</td></tr><tr><td colspan="8">Gas E&amp;Ps</td></tr><tr><td>Antero Resources Corp.</td><td>AR</td><td>48</td><td>56</td><td>(14%)</td><td>OW</td><td>OW</td><td>39%</td></tr><tr><td>CNX Resources Corp.</td><td>CNX</td><td>32</td><td>34</td><td>(6%)</td><td>UW</td><td>UW</td><td>(5%)</td></tr><tr><td>Comstock Resources Inc.</td><td>CRK</td><td>16</td><td>18</td><td>(11%)</td><td>EW</td><td>EW</td><td>15%</td></tr><tr><td>EQT Corp.</td><td>EQT</td><td>68</td><td>74</td><td>(8%)</td><td>OW</td><td>OW</td><td>32%</td></tr><tr><td>Expand Energy Corp.</td><td>EXE</td><td>131</td><td>139</td><td>(6%)</td><td>OW</td><td>OW</td><td>48%</td></tr><tr><td>Range Resources Corp.</td><td>RRC</td><td>44</td><td>50</td><td>(12%)</td><td>EW</td><td>EW</td><td>21%</td></tr><tr><td>Tourmaline Oil Corp.</td><td>TOU</td><td>65</td><td>70</td><td>(7%)</td><td>EW</td><td>EW</td><td>8%</td></tr><tr><td>Gas E&amp;Ps Median</td><td></td><td></td><td></td><td>(8%)</td><td></td><td></td><td>21%</td></tr><tr><td colspan="8">Royalties &amp; Minerals</td></tr><tr><td>Viper Energy, Inc.</td><td>VNOM</td><td>46</td><td>49</td><td>(6%)</td><td>OW</td><td>OW</td><td>6%</td></tr><tr><td>Total Coverage Median</td><td></td><td></td><td></td><td>(6%)</td><td></td><td></td><td>22%</td></tr></table>

Source: FactSet, MS estimates

Exhibit 14: Bear/Bull Cases  
![](images/081156c584a22cdd23f3c53574d120dfa7f75415e4abb67d9fa3d86346520ef3.jpg)  
Source: FactSet, MS estimates

## Performance & Key Industry Metrics

Exhibit 15: WoW Energy Sub-sector Performance

WoW Performance

![](images/a6aed8ba131169e593c118334ce0812a746614fdd148ef02d3e3f0d69ba89437.jpg)  
Source: Bloomberg, FactSet, MS. Note: prices as of 6.25.26 close.

Exhibit 16: YTD Energy Sub-sector Performance  
YTD Performance  
![](images/0d479f0b2d8a3282b9ad2904e137199c099fb

[中间内容因长度限制已省略]

hich this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Exploration & Production

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/25/2026)</td></tr><tr><td colspan="3">Devin McDermott</td></tr><tr><td>Antero Resources Corp (AR.N)</td><td>O (04/17/2024)</td><td>$34.50</td></tr><tr><td>APA Corp (APA.O)</td><td>U (04/15/2024)</td><td>$33.42</td></tr><tr><td>Chord Energy Corporation (CHRD.O)</td><td>O (03/27/2026)</td><td>$119.48</td></tr><tr><td>CNX Resources Corp (CNX.N)</td><td>U (01/10/2025)</td><td>$33.61</td></tr><tr><td>Comstock Resources Inc. (CRK.N)</td><td>E (01/10/2025)</td><td>$13.87</td></tr><tr><td>ConocoPhillips (COP.N)</td><td>O (12/16/2024)</td><td>$106.41</td></tr><tr><td>Devon Energy Corp (DVN.N)</td><td>O (12/11/2023)</td><td>$42.60</td></tr><tr><td>Diamondback Energy Inc (FANG.O)</td><td>O (12/11/2020)</td><td>$182.55</td></tr><tr><td>EOG Resources Inc (EOG.N)</td><td>E (12/11/2023)</td><td>$133.59</td></tr><tr><td>EQT Corp. (EQT.N)</td><td>O (11/18/2021)</td><td>$51.65</td></tr><tr><td>Expand Energy Corp (EXE.O)</td><td>O (01/10/2025)</td><td>$88.44</td></tr><tr><td>Matador Resources Co (MTDR.N)</td><td>E (01/10/2025)</td><td>$50.16</td></tr><tr><td>Murphy Oil Corporation (MUR.N)</td><td>U (01/22/2025)</td><td>$35.39</td></tr><tr><td>Northern Oil &amp; Gas Inc. (NOG.N)</td><td>U (08/18/2025)</td><td>$19.74</td></tr><tr><td>Occidental Petroleum Corp (OXY.N)</td><td>E (08/18/2025)</td><td>$51.21</td></tr><tr><td>Ovintiv Inc (OVV.N)</td><td>E (03/27/2026)</td><td>$53.55</td></tr><tr><td>Permian Resources Corp (PR.N)</td><td>O (01/10/2025)</td><td>$18.86</td></tr><tr><td>Range Resources Corp. (RRC.N)</td><td>E (03/26/2025)</td><td>$36.31</td></tr><tr><td>Tourmaline Oil Corp. (TOU.TO)</td><td>E (01/10/2025)</td><td>C$60.02</td></tr><tr><td>Viper Energy Inc (VNOM.O)</td><td>O (08/18/2025)</td><td>$43.55</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## INDUSTRY COVERAGE: Integrated Energy

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/25/2026)</td></tr><tr><td colspan="3">Devin McDermott</td></tr><tr><td>Canadian Natural Resources Ltd (CNQ.TO)</td><td>E (10/07/2021)</td><td>C$56.19</td></tr><tr><td>Cenovus Energy (CVE.TO)</td><td>O (10/07/2021)</td><td>C$34.96</td></tr><tr><td>Chevron Corporation (CVX.N)</td><td>O (08/04/2025)</td><td>$172.24</td></tr><tr><td>Exxon Mobil Corporation (XOM.N)</td><td>O (05/14/2024)</td><td>$137.55</td></tr><tr><td>Imperial Oil Ltd (IMO.TO)</td><td>E (10/07/2021)</td><td>C$160.92</td></tr><tr><td>Suncor Energy Inc (SU.TO)</td><td>E (12/16/2024)</td><td>C$77.10</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

## © 2026 MS
"""
