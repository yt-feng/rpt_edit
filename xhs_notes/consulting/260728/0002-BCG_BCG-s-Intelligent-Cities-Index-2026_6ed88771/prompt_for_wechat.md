你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# BCG's Intelligent Cities Index 2026

How AI Shapes Urban Living

By Akram Awad, Rami Mourtada, Cecilia Bousoño, Suresh Subudhi, Vladislav Boutenko, Ramsey Baker, and Ekaterina Shapochka

![](images/3a3d0e764b0663f2eac13260572b48d9b65c6bbf219b351e010f84cbd0681fa8.jpg)

Cities around the world are deploying AI and digital technology to deliver new levels of service to residents. Yet as these technologies evolve continuously, even the world's most advanced cities must also evolve to provide ever-greater services, meet growing expectations, and help drive resident outcomes and economic opportunities.

BCG's inaugural Intelligent Cities Index (ICI) assesses how 61 of the world's biggest cities use technology to serve their residents and businesses. It offers a perspective on intelligent city maturity that is tech-focused, enabler-driven, and outcomes-oriented. We analyze maturity across five domains: outcomes, strategy, adoption, ways of working, and enablers. A city's overall maturity level reflects its combined domain maturity: leading, accelerating, emerging, or developing. (See “About the Intelligent Cities Index.”)

The five leading cities are London, Dubai, New York City, Washington, and Amsterdam. All five show leading maturity across two or more of the five domains. However, no one city leads every domain; even cities at the cutting edge of technology implementation have areas to strengthen. (See Exhibit 1.)

The Index also offers lessons from global pioneers like London, which tops the Index overall. The growth of intelligent city capability draws on the contributions of a diverse cast of participants, from city government leaders to private sector partners and ultimately residents themselves. A city's success requires a balanced approach to key enabling factors, especially digital technology and AI, across domains. The good news is that there are multiple pathways to success.

The Intelligent Cities Index Leaderboard

<table><tr><td colspan="2"></td><td>City</td><td>Total score</td><td>Outcomes</td><td>Strategy</td><td>Adoption</td><td>Ways of working</td><td>Enablers</td></tr><tr><td rowspan="5">Leading</td><td>1</td><td>London</td><td>85</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>2</td><td>Dubai</td><td>80</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>3</td><td>New York City</td><td>80</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>4</td><td>Washington</td><td>80</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>5</td><td>Amsterdam</td><td>80</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td rowspan="28">Accelerating</td><td>6</td><td>Berlin</td><td>78</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>7</td><td>San Francisco</td><td>77</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>8</td><td>Shanghai</td><td>77</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>9</td><td>Beijing</td><td>76</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>10</td><td>Seoul</td><td>76</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>11</td><td>Singapore</td><td>76</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>12</td><td>Vienna</td><td>75</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>13</td><td>Copenhagen</td><td>75</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>14</td><td>Shenzhen</td><td>75</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>15</td><td>Boston</td><td>74</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>16</td><td>Los Angeles</td><td>74</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>17</td><td>Stockholm</td><td>74</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>18</td><td>Zurich</td><td>74</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>19</td><td>Munich</td><td>73</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>20</td><td>Abu Dhabi</td><td>72</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>21</td><td>Oslo</td><td>72</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>22</td><td>Austin</td><td>71</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>23</td><td>Madrid</td><td>71</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>24</td><td>Dallas</td><td>71</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>25</td><td>Manchester</td><td>71</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>26</td><td>Dublin</td><td>70</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>27</td><td>Chicago</td><td>70</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>28</td><td>Toronto</td><td>70</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>29</td><td>Helsinki</td><td>70</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>30</td><td>Sydney</td><td>70</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>31</td><td>Paris</td><td>68</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>32</td><td>Barcelona</td><td>67</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>33</td><td>Riyadh</td><td>67</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td rowspan="23">Emerging</td><td>34</td><td>Doha</td><td>64</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>35</td><td>Tokyo</td><td>63</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>36</td><td>Hong Kong</td><td>63</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>37</td><td>Medina</td><td>63</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>38</td><td>Almaty</td><td>62</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>39</td><td>Jakarta</td><td>61</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>40</td><td>Rome</td><td>61</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>41</td><td>Milan</td><td>61</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>42</td><td>Melbourne</td><td>60</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>43</td><td>Delhi</td><td>59</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>44</td><td>São Paulo</td><td>59</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>45</td><td>Jeddah</td><td>59</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>46</td><td>Bengaluru</td><td>59</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>47</td><td>Warsaw</td><td>58</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>48</td><td>Ho Chi Minh City</td><td>58</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>49</td><td>Mecca</td><td>58</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>50</td><td>Kuala Lumpur</td><td>58</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>51</td><td>Mumbai</td><td>57</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>52</td><td>Istanbul</td><td>55</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>53</td><td>Mexico City</td><td>55</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>54</td><td>Dammam</td><td>55</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>55</td><td>Buenos Aires</td><td>53</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>56</td><td>Osaka</td><td>52</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td rowspan="5">Developing</td><td>57</td><td>Budapest</td><td>48</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>58</td><td>Johannesburg</td><td>47</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>59</td><td>Casablanca</td><td>46</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>60</td><td>Cairo</td><td>43</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>61</td><td>Lagos</td><td>34</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>

Source: BCG's Intelligent Cities Index 2026.  
Note: APAC = Asia-Pacific; MEA = Middle East and North Africa.

## AI Is a Key Foundation of the Intelligent City

A striking pattern stands out: cities that are embedding AI into core services are delivering faster, better resident outcomes.

As shown in Exhibit 2, leading cities in AI adoption—about one-third—are delivering higher numbers of use cases and a high quality of life. These cities are making AI an integral part of public services and daily city operations. Yet the positioning of AI-driven challengers and AI-light performers suggests that progress is not linear; a city can drive resident outcomes by expanding AI deployment even if it starts with a lower number of use cases.

The message is important, especially for AI-light performers and AI-developing cities. The advancement and expansion of AI use cases can deliver better quality of life, and deployment of AI into more use cases overall is a necessary action—not the only action, but a vital one—for cities that seek to boost their overall intelligent city maturity.

## EXHIBIT 2

## When Deployed in High Numbers, AI Use Cases Lift Resident Outcomes

AI-enabled use cases score vs. outcomes score

![](images/4612b69ad455a54bb6a49b310d0b6214bc9e43f99ba069e04c372b985914246b.jpg)

Initially, progress is not linear, as a city can drive resident outcomes by expanding AI deployment even at a lower number of use cases.

Source: BCG's Intelligent Cities Index 2026. Note: Quadrants are centered to average scores.

# AI Adoption, User Optimism, and the Virtuous Circle of AI Value

Positive sentiment toward AI provides a key element—confidence in the technology's future place in the world—that can shape how the intelligent city evolves.

Our research found a powerful link between how frequently residents use GenAI tools and how positively they view AI's role in their future. As shown in Exhibit 3, residents who have the highest use—AI enthusiasts—also have the highest sentiment. Pragmatic power users are engaging AI more opportunistically but still show a higher level of sentiment than residents who are cautious about their use of the technology.

Such widespread adoption signals a turning point. Citizens are beginning to see AI as a practical technology that can elevate opportunity, productivity, and quality of life. Several geographies especially share this outlook, with cities throughout Africa, Asia, and the Middle East reporting strong enthusiasm and adoption.

A virtuous circle forms in a setting where residents feel strongly about what AI means for their well-being. When residents feel good about how AI is serving them, city leaders have an opening to enable AI more fully and provide more value to beneficiaries. This value feeds more optimism, which is a driver of more engagement, innovation, scaling, and on and on.

## EXHIBIT 3

## GenAI Users Are Optimistic About the Technology

![](images/09adb6427a076293cecab83fb7967522f31021d719a30e06e49c1dadabef5bee.jpg)  
Source: BCG's Intelligent Cities Index 2026.

Cities in Africa, the Middle East, and Asia show the strongest GenAI momentum, pairing high usage with high optimism.

Positive sentiment toward AI is a driver of more engagement, innovation, and citywide scaling.

Intelligent city app usage drives satisfaction. Cities whose residents use smart city apps more frequently also tend to score higher on satisfaction. This includes London and Dubai, leaders in the Index and high scorers in app user satisfaction. Resident satisfaction with smart city apps is quite low in cities where the frequency of usage is lower than average.

Our study finds that use and satisfaction tend to be higher in younger cities. Several cities where more than half of the population is under age 35 fall in the standout cohort. (See Exhibit 4.)

Improving app performance will likely have a positive impact on satisfaction and open the door for more deployment and better outcomes. The same cycle of engagement and optimism that drives AI usage can also drive smart city app scaling.

## EXHIBIT 4

## Smart City App Usage and Satisfaction Are Aligned

![](images/fb89668f614930ce81a565d9cc5098c750a39fb60c5fd432298c0c697c461c6f.jpg)

Source: BCG's Intelligent Cities Index 2026.

## A balance of hard and soft enablers drives a city

forward. The most mature cities in the Index are supported by an assortment of well-developed enablers. (See Exhibit 5.) These cities employ both hard enablers such as data, tech, and infrastructure and soft enablers like talent and funding. In all, 37 cities have found this balance, including Dublin.

Outside this set of balanced players, several other cities excel in hard enablers. For example, Sydney is strong in infrastructure and living labs. The Australian city enjoys accelerating maturity in part because of its focus on these elements.

A story forms: a city can build a strong infrastructure foundation without robust supplies of talent or funding. But technology isn't enough if a city wants to reach the highest levels of maturity.

To do so, a city needs to build up its talent development and funding ecosystems, including venture capital and foreign direct investment, to match the quality of its hard enablers. This is no small task; a city will need to focus money and resources on strengthening funding and talent streams, but the equal focus will likely pay off down the road. Balance is key.

## EXHIBIT 5

## Top Intelligent Cities Excel at Balancing Hard and Soft Enablers

Scores from hard vs. soft enablers $^{1}$

![](images/3d845acfc4b452ec8d13c29d5c47e807750a285f3960bc5f7f62ba7a044a10ba.jpg)

A city can first build stronger hard enablers (e.g., infrastructure) with limited soft enablers (e.g., talent or funding), but a mix of both hard and soft enablers is most impactful.

Funding, talent, and ecosystems can be harder to build than infrastructure—as no city outperforms on soft enablers alone.

Source: BCG's Intelligent Cities Index 2026. $^{1}$ Hard enablers include data and technology, infrastructure, and AI deployment. Soft enablers include ecosystem and funding and talent and skills.

Entrepreneurship and innovation ecosystems create economic opportunities for leading cities. Among the cities in the Index that lead in overall maturity, there's a solid link between the strength of entrepreneurship and innovation ecosystems and overall economic opportunities. Startups are important actors in the push to innovate with technology and deploy new AI and smart city apps. With sufficient capital, these businesses keep developing more powerful, faster, and more satisfying solutions that drive economic growth.

Exhibit 6 shows that four of the Index's top cities score highest in both economic opportunities and ecosystem and funding assessments.

It’s harder to find clear patterns among less mature cities. Weaker ecosystems do not guarantee poorer economic outcomes but instead show highly uneven performance. However, the performance of leading cities suggests that the focus of these locations on entrepreneurship and innovation has been key to their fulfillment of resident expectations.

## EXHIBIT 6

Smart City Funding and Startup Ecosystems Drive Economic Activity  
![](images/3afd1f93897dfc26f161183775a00c6a3399542547c270b89f254b2d90defbb2.jpg)

Source: BCG's Intelligent Cities Index 2026.

Cities with stronger overall enablers convert ecosystem strength into economic opportunity more effectively, emerging as standout innovation transformers.

# Where Each City Leads: A Domain-Level Analysis

As Exhibit 7 illustrates, leaders in each domain make up a broad group of cities with varying overall maturity levels. Their progress suggests that public sector and corporate decision makers have options in their approach, and they can develop many different areas to make an intelligent city stronger.

## EXHIBIT 7

## Leaders in Outcomes and Other Domains

![](images/24136a7386ef29812cdc55caa65c0b7332c1b0b9d5ba7484e29398248a6e05e6.jpg)  
Source: BCG's Intelligent Cities Index 2026.

Outcomes. Our analysis factors in outcomes. The top ten leaders in this domain are using technology to deliver results in livability, economic opportunities, social capital, and engagement with government.

There's more. Some of the most mature intelligent cities in the study are leaders in this domain. The implication: improving intelligent city maturity levels translates into a better city experience for residents.

London is the Index's leader in this area. The UK capital scored highest in resident outcomes related to quality of life and delivery of economic opportunities. The city's success here also helps it land as the Index's top city overall—more proof that maturity and outcomes are clearly linked.

Strategy. The Index assesses the depth and quality of each locale's intelligent cities strategy. This includes documentation of the strategy and any updates to keep pace with technology evolution and changing priorities. We also analyzed the number of smart city sectors covered by a city's strategy. Madrid tops this domain with a good balance of sector coverage and specificity in its strategy.

The clearer and more specific the strategic priorities, the more success a city will have in creating a sharper long-term direction for its intelligent technology maturity. With this future direction defined, government leaders and business partners can then steadily focus investment on the use cases that will deliver the greatest resident impact.

Adoption. The Index assessed adoption of smart city apps and AI technologies, which include business-oriented and resident-oriented e-government portals or digital platforms and apps. We also surveyed resident satisfaction with these technologies.

Adoption showed the highest overall scores of any domain in the Index. From our five leading cities to a city like Lagos, adoption is moving forward. It’s encouraging that cities can boost resident optimism with AI and apps even without strong infrastructure or funding; it goes a long way in building the momentum that can eventually bring a city to higher levels of maturity. However, while adoption is broadly achieved, it is often capped; many cities can push intelligent city or AI use cases only so far. At times, scaling falls short without enablers and ways of working in place. It’s vital to make the most of adoption while ramping up other areas.

The second highest city in the Index, Dubai, is joined as a leader in adop

[中间内容因长度限制已省略]

levels (leading, accelerating, emerging, and developing), translating detailed scores into a clear, comparable view of overall city maturity.

## Intelligent Cities Index Methodology

## Intelligent Cities Index domains

Strategy declaration
(official intelligent city strategy document, etc.)

![](images/066382d38f499dd3ccea57eecf146bc6578f3ccb1631b93fc465a04e109b0bdc.jpg)

15%
Ways of working

25% Enablers

Resident outcomes (resident outcomes for quality of living and economic opportunities, etc.)

## Intelligent Cities Index dimensions

GenAI (residents' sentiment toward and use of GenAI, etc.)

Governance
(a dedicated intelligent city central government unit, etc.)

G2C and G2B (government e-portal engagement, etc.)

Data and technology (citywide data integration platform, etc.)

Tech impacts
(technology benefits across residents' city-related tasks, etc.)

## Ecosystem and funding

Strategic details
(specificity and sector coverage, etc.)

(number of funded startups in city-related sectors, etc.)

Smart city apps (app usage and satisfaction, etc.)

Use cases (number of active intelligent city use cases, etc.)

PPPs
(number of active intelligent city partnerships, etc.)

## Infrastructure and deployment

and deployment (number of IoT devices and presence of living labs, etc.)

Talent and skills (number of tech graduates, etc.)

Source: BCG's Intelligent Cities Index 2026.
Note: G2C = government to citizen; G2B = government to business; PPPs = public-private partnerships; IoT = Internet of Things.

# About the Authors

![](images/66e2c4d1d86f5c127d2f835549aa04c28aa6b58008f3892ef8eb57ca0e1c8221.jpg)  
Akram Awad
awad.akram@bcg.com

Akram is a managing director and partner in the Dubai office of Boston Consulting Group. He is a core member of BCG's Public Sector and Technology Advantage practices and has advised public sector leaders in the Middle East on the value of unlocking national data through AI.

![](images/2ea08fc429c6242b5dc058d028a0156bcfee26f4581c8944ae9a3cee39a76e26.jpg)

## Cecilia Bousoño bousono.cecilia@bcg.com

Cecilia is a senior analyst, BCG Vantage, in BCG's Madrid office. She partners with travel, engineering, real estate, logistics, and city clients globally to improve their AI, data, and digital transformations by leveraging the power of technology, sustainability, and innovation.

![](images/1be92d9b860f068997341541f077ca5c36e2b3e202b372543309748aa2d48077.jpg)

## Vladislav Boutenko boutenko.vladislav@bcg.com

Vladislav is a managing director and senior partner with BCG, where he leads BCG's work with cities globally. He has also directed cities research with the BCG Institute since 2019. His forthcoming book, The Way We Live Next, is due from Harper Business in Spring 2027.

![](images/694d5f0b138abc668f4703f7f56b6482f84d1cfd1e971686aec132969d32e886.jpg)

## Ekaterina Shapochka shapochka.ekaterina@bcg.com

Ekaterina is a partner and associate director, Cities & Regions, in BCG's Riyadh office. She is an expert in regional policy, urban development, quality of life, and smart cities whose work spans projects in Europe, Asia, and the Middle East.

## Acknowledgments

The authors express their sincere gratitude for the extensive support of Mariana Chaverri, Eva González, Shravani Joshi, Maxim Khakhin, Margot Li, Poorti Sathe, and Lynn Zhuo from the BCG consulting and Vantage teams. They also acknowledge contributions from Faisal Alsaedi, Nishan Banerjee,

![](images/17d7e0ea55784b377bfabbca9d9d289a39f53d53114daebb1beb41b41e397cd7.jpg)  
Rami Mourtada
mourtada.rami@bcg.com

Rami is a partner and director in BCG's Technology & Digital Advantage practice in the firm's Dubai office. He is a core member of BCG's Global Center for the Future of Cities and Center for Digital Government. Rami's work spans AI and smart city topics across private and public sectors.

![](images/7cacc1197fefbc72d2029df9e06b14eed95a791e1c03bb0ebfb185daa48342ce.jpg)

## Suresh Subudhi subudhi.suresh@bcg.com

Suresh is a managing director and senior partner in BCG's Dubai office. He is the global leader for the firm's Travel, Cities & Infrastructure practice. Suresh also co-leads BCG's Global Center for the Future of Cities and Center for Mobility Innovation.

![](images/cb145ca72379cac870ee77627c7bf1bc1fd9a6f7d077bbbceb584609de8591ae.jpg)

Ramsey Baker
baker.ramsey@bcg.com

Ramsey is a managing director and partner in BCG's Atlanta office. An expert in travel and tourism, he is the global lead for the firm's work at the intersection of the Technology & Digital Advantage and Travel, Cities & Infrastructure practices.

Shubhika Bilgrami, Madawi Binghannam, Evan Bruning, Vanshika Gupta, Janit Pagaria, Lara Schober, Marcel Sieg, and Nadya Smakhtina. Their insights, feedback, and dedication were invaluable to this report.

## BCG

## About Boston Consulting Group

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change—bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.

![](images/d86ffe441ed1681361a5f8ea01e85fa5fb7423f76d07db9debdc4b8c68308acf.jpg)
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
