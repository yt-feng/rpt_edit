你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
## Global Internet

# Global Internet: A framework for AI model commoditisation, and market segmentation

![](images/a741e57886786ddc32abda26f651a0107aa245730b69130faca2b586ff741747.jpg)  
Robin Zhu

+852 2123 2659

robin.zhu@bernsteinsg.com

![](images/535c14565976acf9f366282c6e117c8407077b029731e41e244113db768d7f54.jpg)  
Mark Shmulik

+1 917 344 8508

mark.shmulik@bernsteinsg.com

![](images/5fb91feda346785989e606132f4ce1d83a37f563a8481067096aeda318e81853.jpg)  
Charles Gou

+852 2123 2618

charles.gou@bernsteinsg.com

![](images/00e5ab24d4ccdbb14683701bbf691ebce73a5a8740e8140055f3ab8a4a776e3a.jpg)  
Min-Joo Kang

+852 2123 2644

minjoo.kang@bernsteinsg.com

![](images/fbec7ebd0eb3cc6127d0fce606f347a29dbb5f76fa11f08608cb895040d35b3d.jpg)  
Hyrum Caesar

+81 3 6777 6979

hyrum.caesar@bernsteinsg.com

![](images/43e21dce08d454bed4d2f267b4336d9eb97ef4374249eb7df8e735417fda22f0.jpg)  
Wenhuan Chang

+1 917 344 8546

wenhuan.chang@bernsteinsg.com

![](images/d809283d99792fb93be6559b6593d9b230cf3ff380adf6984c6bdb69edb6af3c.jpg)  
Deeksha Pandey

+1 917 344 8447

deeksha.pandey@bernsteinsg.com

A shift in the AI zeitgeist? We're long-term AI bulls, and have increasingly built agentic AI into our day-to-day workflows. That said, several recent events strike us as being noteworthy as far as AI competition and ROI is concerned. The high cost of Anthropic's Claude Fable 5 pricing causing devs to ration usage feels like a notable development. See also headlines pointing to OpenAI potentially cutting prices to win share, and large AI users (e.g. Tencent, Microsoft) doing a double-take on the costs of token-maxxing.

An alternative mental model for AI model commoditisation. Rather than model intelligence necessarily converging, we increasingly think AI model commoditisation will be driven by human user perception across various end uses, and the timeline on which competing models become “good enough”, and reliable at scale. We’ve long argued that consumer-focused AI (ordering bubble tea, booking hotel rooms) will commoditise relatively quickly. Enterprise use cases like coding and Excel work are more complex, and will take longer to solve. Solving frontier science (e.g. defence, healthcare, nuclear fusion, space travel) likely merits the use of frontier AI more or less ad infinitum.

## The implications for AI market segmentation... and competition. Once the

AI supporting a given use case becomes “good enough”, we’d expect the arbiter of competition and market share to shift from reasoning capabilities to availability and price. Our base case is the US frontier labs continue to unlock new model capabilities that command a rising price premium among increasingly specialised customers. Data security concerns and global geopolitics likely prevent some US and European enterprises from deploying Chinese models. But elsewhere we’d expect the Chinese AI labs to take share, serving “good enough” reasoning capabilities at significantly lower prices.

Chinese open source models as the value option. Hardware advancements will make it cheaper for the US frontier labs to serve tokens, and drive Jevon's Paradox. Nonetheless, it would surprise us if trailing edge AI didn't become another sector where Chinese competition takes market share, in part thanks to a willingness to accept lower prices and margins. The ability to follow global SOTA as a lighthouse for R&D direction means the Chinese AI labs need to do less exploratory research. Our market segmentation suggests they should be able to access 35-40% of the global AI TAM - even taking geopolitical constraints into consideration, and assuming minimal US traction.

Stepping off the exponential - and the path to AI lab profits. If we're right about AI commoditisation being driven by task completion and user perception, the implications for AI lab economics might actually be reasonably hopeful. Once a use case becomes “solved” the return on doing incremental R&D on the same topic diminishes, meaning R&D effort can be redirected elsewhere along the frontier. Over time, we'd expect the envelope of use cases worth spending exponentially higher amounts to solve will narrow... meaning aggregate model training costs rise more slowly, making it easier for the AI labs to show operating leverage.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">11 Jun 2026</td><td colspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>700.HK (Tencent)</td><td>O</td><td>HKD</td><td>457.20</td><td>780.00</td><td>(47.3)%</td><td>CNY</td><td>28.09</td><td>30.00</td><td>34.91</td><td>14.1</td><td>13.2</td><td>11.3</td><td></td></tr><tr><td>BABA (Alibaba )</td><td>O</td><td>USD</td><td>115.38</td><td>180.00</td><td>(23.7)%</td><td>CNY</td><td>65.41</td><td>26.82</td><td>46.57</td><td>12.0</td><td>29.1</td><td>16.8</td><td></td></tr><tr><td>9988.HK (Alibaba)</td><td>O</td><td>HKD</td><td>107.40</td><td>176.00</td><td>(44.8)%</td><td>HKD</td><td>8.82</td><td>3.69</td><td>6.68</td><td>10.5</td><td>25.2</td><td>13.9</td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,920.52</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,266.99</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We're AI bulls at a high level, but think events in the past week are worthy of attention. The high cost of Claude Fable 5 tokens making token-maxxing uneconomic wasn't necessarily on our list of high-likelihood events for the year, but likely accelerates the timeline on which AI devs and users start to examine AI ROI more closely. The idea that AI users will select across a range of models to match the marginal cost of tokens to the marginal benefit of task completion (with considerations perhaps given to quality-of-life aspects like response times and model “personality”) makes sense to us.

To take things one step further, our mental framework for AI model commoditisation focuses on whether task completion becomes reliable at scale as perceived by human users, as opposed to some academic measure of underlying convergence. Once agentic AI “solves” various vertical use cases, we’d expect the arbiter of competition to shift from reasoning capabilities and task completion to more mundane variables like cost per task, reliability, and developer trust. The debate on whether the top Chinese AI models are 6 or 12 months behind US SOTA is intellectually interesting, but probably almost meaningless commercially except in the case of specialised use cases.

Longer term, we think it's logical to assume a two-tier market split across (1) the US SOTA labs serving the frontier, where the workloads become increasingly specialised and novel, while a narrower field of customers exhibits high willingness to pay; and (2) a market for trailing edge AI that serves more mundane enterprise and consumer end uses, where the availability and cost of reasoning drives adoption - and share shifts. Consumer-oriented AI should be one of the first end uses where a wide range of players achieve “good enough” status, for example.

## VALUATION COMPS TABLE

EXHIBIT 1: Asia Internet: valuation summary

<table><tr><td></td><td>Rating</td><td>Price target</td><td>Last price</td><td>Crncy</td><td>Market cap (US$mn)</td><td>2026E</td><td>PE 2027E</td><td>2028E</td><td>2026E</td><td>EV/sales 2027E</td><td>2028E</td></tr><tr><td colspan="12">China Internet coverage</td></tr><tr><td>Tencent</td><td>O</td><td>780</td><td>465.60</td><td>HKD</td><td>534,208</td><td>13.5x</td><td>11.6x</td><td>10.1x</td><td>4.5x</td><td>3.9x</td><td>3.4x</td></tr><tr><td>PDD</td><td>M</td><td>110</td><td>81.82</td><td>USD</td><td>116,462</td><td>7.5x</td><td>6.8x</td><td>6.0x</td><td>0.6x</td><td>0.4x</td><td>0.1x</td></tr><tr><td>Meituan</td><td>M</td><td>85</td><td>79.00</td><td>HKD</td><td>62,014</td><td>176.3x</td><td>16.3x</td><td>9.5x</td><td>0.8x</td><td>0.7x</td><td>0.6x</td></tr><tr><td>NetEase</td><td>O</td><td>150</td><td>125.52</td><td>USD</td><td>80,098</td><td>13.8x</td><td>12.8x</td><td>12.2x</td><td>3.3x</td><td>3.0x</td><td>2.8x</td></tr><tr><td>Boss Zhipin</td><td>O</td><td>18</td><td>13.24</td><td>USD</td><td>6,402</td><td>10.7x</td><td>8.9x</td><td>7.9x</td><td>2.4x</td><td>1.6x</td><td>1.1x</td></tr><tr><td>JD</td><td>O</td><td>40</td><td>28.45</td><td>USD</td><td>38,858</td><td>9.2x</td><td>6.7x</td><td>5.1x</td><td>0.2x</td><td>0.2x</td><td>0.2x</td></tr><tr><td>Alibaba</td><td>O</td><td>180</td><td>115.38</td><td>USD</td><td>276,812</td><td>28.9x</td><td>16.9x</td><td>14.4x</td><td>1.9x</td><td>1.7x</td><td>1.6x</td></tr><tr><td colspan="12">China Internet other</td></tr><tr><td>Kuaishou</td><td></td><td></td><td>46.02</td><td>HKD</td><td>25,219</td><td>10.4x</td><td>9.1x</td><td>8.1x</td><td>1.0x</td><td>0.9x</td><td>0.9x</td></tr><tr><td>Bilibili</td><td></td><td></td><td>18.08</td><td>USD</td><td>7,685</td><td>18.2x</td><td>13.9x</td><td>10.8x</td><td>1.1x</td><td>1.0x</td><td>0.9x</td></tr><tr><td>TME</td><td></td><td></td><td>9.21</td><td>USD</td><td>15,303</td><td>9.5x</td><td>8.6x</td><td>7.8x</td><td>2.0x</td><td>1.8x</td><td>1.7x</td></tr><tr><td>Baidu</td><td></td><td></td><td>117.48</td><td>USD</td><td>39,973</td><td>15.0x</td><td>13.4x</td><td>10.8x</td><td>1.2x</td><td>1.1x</td><td>1.0x</td></tr><tr><td>VIPshop</td><td></td><td></td><td>13.71</td><td>USD</td><td>6,585</td><td>5.4x</td><td>5.2x</td><td>4.9x</td><td>0.2x</td><td>0.2x</td><td>0.2x</td></tr><tr><td>Tencent Music</td><td></td><td></td><td>9.21</td><td>USD</td><td>15,303</td><td>9.5x</td><td>8.6x</td><td>7.8x</td><td>2.0x</td><td>1.8x</td><td>1.7x</td></tr><tr><td>Trip.com</td><td></td><td></td><td>47.97</td><td>USD</td><td>30,207</td><td>11.7x</td><td>10.3x</td><td>9.1x</td><td>2.4x</td><td>2.1x</td><td>1.9x</td></tr><tr><td>KE Holdings</td><td></td><td></td><td>16.00</td><td>USD</td><td>18,517</td><td>18.3x</td><td>15.7x</td><td>15.7x</td><td>1.1x</td><td>1.0x</td><td>1.0x</td></tr><tr><td colspan="12">Asian Internet</td></tr><tr><td>Naver</td><td>O</td><td>330,000</td><td>220,500</td><td>KRW</td><td>22,910</td><td>15.9x</td><td>14.4x</td><td>12.8x</td><td>1.7x</td><td>1.4x</td><td>1.2x</td></tr><tr><td>Kakao</td><td>O</td><td>80,000</td><td>37,650</td><td>KRW</td><td>11,268</td><td>21.9x</td><td>19.3x</td><td>15.9x</td><td>1.2x</td><td>0.9x</td><td>0.7x</td></tr><tr><td>Hybe</td><td>O</td><td>400,000</td><td>201,000</td><td>KRW</td><td>6,153</td><td>20.0x</td><td>19.8x</td><td>16.1x</td><td>1.3x</td><td>1.4x</td><td>1.2x</td></tr><tr><td>Coupang</td><td>U</td><td>12</td><td>15.12</td><td>USD</td><td>27,141</td><td>-41.2x</td><td>65.0x</td><td>32.7x</td><td>0.6x</td><td>0.6x</td><td>0.5x</td></tr><tr><td>Sea Ltd.</td><td></td><td></td><td>82.44</td><td>USD</td><td>50,493</td><td>22.1x</td><td>16.1x</td><td>12.8x</td><td>1.4x</td><td>1.2x</td><td>1.0x</td></tr><tr><td>Grab</td><td></td><td></td><td>3.27</td><td>USD</td><td>13,409</td><td>31.7x</td><td>21.2x</td><td>15.8x</td><td>2.2x</td><td>1.8x</td><td>1.6x</td></tr><tr><td colspan="12">US Internet</td></tr><tr><td>Amazon</td><td></td><td></td><td>238.00</td><td>USD</td><td>2,560,192</td><td>23.1x</td><td>20.5x</td><td>16.7x</td><td>3.2x</td><td>2.8x</td><td>2.6x</td></tr><tr><td>Alphabet</td><td></td><td></td><td>356.38</td><td>USD</td><td>4,320,705</td><td>24.9x</td><td>23.3x</td><td>19.4x</td><td>10.2x</td><td>8.4x</td><td>7.1x</td></tr><tr><td>Meta</td><td></td><td></td><td>570.98</td><td>USD</td><td>1,449,389</td><td>16.1x</td><td>14.8x</td><td>12.3x</td><td>5.8x</td><td>4.8x</td><td>4.1x</td></tr><tr><td>Netflix</td><td></td><td></td><td>82.00</td><td>USD</td><td>345,285</td><td>23.0x</td><td>21.2x</td><td>17.9x</td><td>6.8x</td><td>6.1x</td><td>5.5x</td></tr><tr><td>Uber</td><td></td><td></td><td>68.61</td><td>USD</td><td>139,662</td><td>21.1x</td><td>15.3x</td><td>12.5x</td><td>2.5x</td><td>2.2x</td><td>1.9x</td></tr><tr><td>Spotify</td><td></td><td></td><td>503.10</td><td>USD</td><td>103,554</td><td>34.0x</td><td>27.6x</td><td>22.6x</td><td>4.1x</td><td>3.6x</td><td>3.2x</td></tr><tr><td>DoorDash</td><td></td><td></td><td>151.00</td><td>USD</td><td>65,794</td><td>31.7x</td><td>21.6x</td><td>17.0x</td><td>3.6x</td><td>3.0x</td><td>2.5x</td></tr></table>

Pricing date June 3, 2026. The valuation multiples of our China and Asian Internet coverage are based on Bernstein estimates; the other companies shown reflect Bloomberg consensus estimates.  
Source: Corporate reports, Bloomberg, Bernstein estimates and analysis.

## DETAILS

## A MENTAL MODEL FOR AI MODEL SEGMENTATION AND COMMODITISATION

The debate over whether AI models can remain differentiated or are doomed to commoditise in the long run remains a key one when it comes to the economic value associated with frontier intelligence, and the valuations of market bellwethers like OpenAI and Anthropic. Our own views on this topic have meandered over time. But we increasingly think a generalisable framework for AI model evolution, market competition, and how the AI industry as a collective “step off the exponential” hinges on end user perceptions of intelligence, and when task completion becomes “good enough” for various verticals, and reliable at scale… regardless of whether the underlying tech necessarily converges fully in a strict academic sense (see Exhibit 2).

As AI model performance continues to improve, and agentic task completion horizons lengthen, we'd expect a broadening range of tasks to become possible to an acceptable degree of accuracy, and then deployable at scale. This is especially true if we assume guardrails like user confirmation of transactions are embedded in the workflow, which helps to ring-fence the downside to reasoning errors. As of June 2026, AI-generated images and videos are already increasingly difficult to distinguish versus the real thing. Tencent's Weixin agentic AI announcement - and Alibaba's efforts within its Qwen app - suggest that purchases of bubble tea, flight tickets, or T-shirts will soon become ready for commercial deployment. Once task completion becomes reliable at scale, the return to doing more R&D on these end uses drops dramatically... which should mean the AI labs turn their energy towards more complex tasks.

On a relative basis, we'd expect most consumer use cases for agentic AI to become “solved” relatively quickly, followed by more deterministic enterprise workloads (e.g. Excel work, imagine looking for hallucinations in several hundred lines of modelling), more complex strategic planning, and fields like cybersecurity (e.g. Project Glasswing), advanced engineering (e.g. Gen 7 fighter jets supported by autonomous drone swarms), and frontier science (drug discovery, nuclear fusion, space exploration).

## Do AI models commoditise... when human users stop being able to tell them apart?

At the market level, our latest thinking is that there will be a “bell curve” of differentiation between the closed SOTA labs, and open source, where differences in capabilities diverge periodically, driven by access to compute and frontier R&D unlocking new capabilities. It feels plausible to us for example that the US frontier labs moving from Blackwell to Rubin and subsequent generations of chips will at least momentarily cause the gap between US and China SOTA to wid

[中间内容因长度限制已省略]

 you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
