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
14 Jun 2026 21:35:36 ET | 24 pages

# Artificial Intelligence

Citi's Inference Ahead - Bridging the Gaps

## CITI'S TAKE

The vertical wall is spilling further into prior generations of silicon, with rentals of A100 up 0.6% WoW and 11% over six weeks (Figure 3). Segmentation moved inside a single release, with the top leaderboard score shifting from 61 to 65 as the blended price roughly doubled (Figure 4). Rationing became a product feature, with the new top model moving behind usage credits after June 22. Scarcity is being monetized faster than it is being solved, though new non-sequential models, routing architectures, and emerging world models seem to be painting the path forward through performance, efficiencies, and a breadth of applications.

Models. DiffusionGemma (6/10) achieves up to 4x faster inference than Gemma 4 by shifting the decode bottleneck from memory bandwidth to compute. Google built DiffusionGemma by adapting Gemma 4 so a similar adaptation of Gemini Flash or Pro is plausible, though for now at a quality cost intrinsic to non-sequential generation (6/10). Another open-weight model, Poolside's Laguna, is helping advance agentic coding, while Odyssey's Starchild-1 (the first multimodal world model) and Agora-1 (a multi-agent world model) support the expansion of AI's use cases beyond languages.

Watts. A private neocloud recently announced 4.9GW contracted against a 40GW+ pipeline while ending its involvement in a 1.8GW project, illustrating both the explosiveness of demand and the challenges of growing supply (Bloomberg, 6/9). The 12% contracted-to-planned ratio reframes pipelines as books of options written by developers and exercised site-by-site by a smaller number of tenants.

Capacity. Data center locations cluster in regions with retail power rates of 9-12¢/kWh (Figure 1), with states above 25% renewable share drawing outsized capacity (Figure 2). PPAs and carbon commitments are likely co-determining site selection alongside raw rates, and CapEx per H100-equivalent is steadily rising (Figure 8) as component costs trend upward and power costs increasingly move from post-construction operating costs to pre-construction capital costs.

Tokens. No provider currently holds all three vertices of the intelligence-speed-price triangle. The new frontier release debuted +4 points of intelligence at 2x the prior cost. Meanwhile, speed is accruing to the mid-tier, with median top-20 output speed up from 64 to 105 tok/s over six weeks (Figure 3). The proprietary-open gap widening from 6 to 10 points shows the frontier defending its intelligence vertex structurally rather than competing down with open models on price (Figure 4). Although Google now faces a steeper climb before it can credibly claim all three vertices at once, Gemini 3.5 Pro remains on the event horizon.

Routing. The rents/savings this segmentation creates accrue to the layer compiling inference and owning the profiling data (i.e., which model, at which quantization, on which hardware, produces acceptable output for which subtask). The challenge is capturing that data and achieving efficient routing without leaking enterprise IP or PII (Touheed, 5/31). As adoption ramps (Figure 13), the Databricks and AWS summits are the near-term venues where enterprise routing primitives may surface (Figure 6).

## Heath Terry $^{AC}$

+1-212-723-4624

heath.terry@citi.com

## Shelby Spencer

+1-212-816-0416

shelby.spencer@citi.com

## Ashley Kim

+1-212-816-6689

ashley.kim@citi.com

## Janna Withrow

+1-212-723-0439

janna.withrow@citi.com

Figure 1. AI Data Centers and State Power Costs  
![](images/83469792af745ef56df58e492ee9f283d33f363c0c9b1f3c67351a7bc14e246a.jpg)

<details>
<summary>bubble chart</summary>

| State       | Color  | Bubble Size |
| ----------- | ------ | ----------- |
| California  | Brown  | Large       |
| Texas       | Blue   | Medium      |
| Florida     | Red    | Large       |
| New York    | Green  | Medium      |
| Pennsylvania| Blue   | Medium      |
| Illinois    | Light Blue | Medium    |
| Ohio        | Dark Blue | Small     |
| Georgia     | Dark Grey | Small     |
| North Carolina | Dark Grey | Small     |
| Michigan    | Dark Grey | Small     |
| Virginia    | Dark Grey | Small     |
| Washington  | Dark Grey | Small     |
| Arizona     | Dark Grey | Small     |
| Massachusetts | Dark Grey | Small     |
| Tennessee   | Dark Grey | Small     |
| Indiana     | Dark Grey | Small     |
| Maryland    | Dark Grey | Small     |
| Wisconsin   | Dark Grey | Small     |
| Minnesota   | Dark Grey | Small     |
| Colorado    | Dark Grey | Small     |
| Iowa        | Dark Grey | Small     |
| Missouri    | Dark Grey | Small     |
| Utah        | Dark Grey | Small     |
| Kentucky    | Dark Grey | Small     |
| Alabama     | Dark Grey | Small     |
| Louisiana   | Dark Grey | Small     |
| Mississippi | Dark Grey | Small     |
| Arkansas    | Dark Grey | Small     |
| Louisiana   | Dark Grey | Small     |
| Oklahoma    | Dark Grey | Small     |
| West Virginia | Dark Grey | Small     |
| Maine       | Dark Grey | Small     |
| Vermont     | Dark Grey | Small     |
| New Hampshire | Dark Grey | Small     |
| Rhode Island | Dark Grey | Small     |
| Montana     | Dark Grey | Small     |
| South Dakota | Dark Grey | Small     |
| North Dakota | Dark Grey | Small     |
| Delaware    | Dark Grey | Small     |
| Alaska      | Dark Grey | Small     |
| Hawaii      | Dark Grey | Small     |
| Maine       | Dark Grey | Small     |
| Vermont     | Dark Grey | Small     |
| New Hampshire | Dark Grey | Small     |
| Rhode Island | Dark Grey | Small     |
| Montana     | Dark Grey | Small     |
| South Dakota | Dark Grey | Small     |
| North Dakota | Dark Grey | Small     |
| Delaware    | Dark Grey | Small     |
| Alaska      | Dark Grey | Small     |
| Hawaii       | Dark Grey | Small     |
| Maine       | Dark Grey | Small     |
| Vermont     | Dark Grey | Small     |
| New Hampshire | Dark Grey | Small     |
| Rhode Island | Dark Grey | Small     |
| Montana     | Dark Grey | Small     |
| South Dakota | Dark Grey | Small     |
| North Dakota | Dark Grey | Small     |
| Delaware    | Dark Grey | Small     |
| Alaska      | Dark Grey | Small     |
| Hawaii: The chart contains no labels for the data series. The labels are not explicitly provided in the code. The data series is inferred from the visual representation of the bubbles. There is only one data series labeled 'bubble' in the image.
</details>

Retail Electricity Rate (¢/kWh)  
![](images/9f711767a0cf214f0031d03b54a9e928c4764c71a325a95a4a662710c65a4f78.jpg)

Data Center Power (MW)  
![](images/4f9c98ff3c83a901f9e87694b0ba42dafb4bebf6be722f42143aa0368f2d1d67.jpg)

![](images/b51e33d3d72943850fb264c0d0dd4d685c5d6048cfb0a461a18b859c1b879611.jpg)  
Operational

![](images/5192d3949c3f4423ce3a03043f8c6ac7ee33e17fb907eb4966690bc4e757e544.jpg)  
Planned

Owner  
![](images/843c055078b8b3f6c6cf919896220e7b3c40d065b2cbb0097ff261d20b9344ca.jpg)  
Oracle

![](images/60247f23cbc315c713325738bae1198eb97fadeefcf14e10414ed169f53b7193.jpg)  
Meta

![](images/c743cc2aeca0b3e4bb5ed8600830e6a0123679531fe04d8406cc6973ebe45e92.jpg)  
Amazon

![](images/651d12605a1d3eb937795a9b3e3c9d976b074d76f1535e4f85495edc6269760b.jpg)  
Fluidstack

![](images/5087091d118cae6543e8f03be7c49abf50b37c6e9dfdeb26ab50c03772207e6b.jpg)  
Google

![](images/ddb23713692936e3f503e48f9e27b96c75792375820a2247a734b07d0cea63ea.jpg)  
Microsoft

![](images/435f048a0f14545128079b5168fee5ae40213ba9a3a3754bb822ac17fcfb0f78.jpg)  
Softbank

![](images/d7c1a528c656df1195ed1b05ccc2eb29d09b026c8ba79e7f3174c6c864ee9710.jpg)  
Other

© 2026 Citi Inc. No redistribution without Citi's written permission.

Source: Citi, Berkeley Lab, Epoch AI

Figure 2. Retail Rates and Renewable Generation v. Data Center Capacity  
![](images/76314f8c1f0f2053cf5a5d3e6fd2b3a7d37f0140d2b34e74be3dce145d89285d.jpg)  
South West Midwest Northeast  
South West Midwest Northeast  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Berkeley Lab, Epoch AI

Figure 3. A Summary of Signals

<table><tr><td>Metric</td><td>Unit</td><td>Latest Date</td><td>Period</td><td>Calculation</td><td>Period-Over- Period Δ</td><td>Latest Period</td><td>2nd Latest Period</td><td>3rd Latest Period</td><td>4th Latest Period</td><td>5th Latest Period</td><td>6th Latest Period</td><td>Trendline</td></tr><tr><td colspan="13">Proprietary and Open Models (Artificial Analysis)</td></tr><tr><td>Highest Intelligence for Proprietary Models</td><td>Points</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+4.9%</td><td>64</td><td>61</td><td>60</td><td>60</td><td>60</td><td>60</td><td></td></tr><tr><td>Highest Intelligence for Open Models</td><td>Points</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+1.9%</td><td>55</td><td>54</td><td>54</td><td>54</td><td>54</td><td>54</td><td></td></tr><tr><td>Gap in Proprietary and Open Intelligence</td><td>Points</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+28.6%</td><td>9</td><td>7</td><td>6</td><td>6</td><td>6</td><td>6</td><td></td></tr><tr><td colspan="13">Highest Intelligence Models from the Top-20 Providers (Artificial Analysis)</td></tr><tr><td>Median Intelligence</td><td>Points</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+9.5%</td><td>46</td><td>42</td><td>38</td><td>38</td><td>38</td><td>38</td><td></td></tr><tr><td>Median Latency</td><td>Sec</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▼-7.0%</td><td>2.25</td><td>2.42</td><td>2.20</td><td>2.52</td><td>2.37</td><td>2.16</td><td></td></tr><tr><td>Median Speed</td><td>Tok/Sec</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+5.0%</td><td>105</td><td>100</td><td>96</td><td>67</td><td>66</td><td>64</td><td></td></tr><tr><td colspan="13">GPU Index Pricing (Bloomberg)</td></tr><tr><td>A100</td><td>$/Hour</td><td>6/10/26</td><td>Week</td><td>7d Avg</td><td>▲+0.6%</td><td>1.63</td><td>1.62</td><td>1.57</td><td>1.53</td><td>1.50</td><td>1.47</td><td></td></tr><tr><td>H100/H200</td><td>$/Hour</td><td>6/10/26</td><td>Week</td><td>7d Avg</td><td>▼-0.8%</td><td>2.64</td><td>2.66</td><td>2.61</td><td>2.89</td><td>2.71</td><td>2.50</td><td></td></tr><tr><td>(G)B200/(G)B300</td><td>$/Hour</td><td>6/10/26</td><td>Week</td><td>7d Avg</td><td>▲+0.8%</td><td>4.82</td><td>4.78</td><td>4.67</td><td>4.66</td><td>4.54</td><td>4.31</td><td></td></tr><tr><td colspan="13">Model Pricing for Output Tokens (Artificial Analysis)</td></tr><tr><td>US+EU Avg</td><td>$/1M Tok</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+28.4%</td><td>14.17</td><td>11.04</td><td>11.04</td><td>11.04</td><td>11.00</td><td>11.00</td><td></td></tr><tr><td>China Avg</td><td>$/1M Tok</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>—0.0%</td><td>5.11</td><td>5.11</td><td>5.11</td><td>5.11</td><td>5.21</td><td>5.21</td><td></td></tr><tr><td>Frontier Avg</td><td>$/1M Tok</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+24.1%</td><td>11.70</td><td>9.43</td><td>9.43</td><td>9.43</td><td>9.42</td><td>9.42</td><td></td></tr><tr><td colspan="13">Developer Usage (PyPI)</td></tr><tr><td>Multi-Provider SDK Downloads</td><td>%</td><td>6/9/26</td><td>Week</td><td>WoW Δ in 7d Avg</td><td>▲+11.5</td><td>+11.8</td><td>+0.3</td><td>+2.8</td><td>+1.0</td><td>+2.7</td><td>+0.9</td><td></td></tr><tr><td>Gemini SDK Downloads</td><td>%</td><td>6/9/26</td><td>Week</td><td>WoW Δ in 7d Avg</td><td>▼-6.6</td><td>-2.7</td><td>+3.9</td><td>+3.5</td><td>+17.6</td><td>+7.2</td><td>-2.2</td><td></td></tr><tr><td>Mistral SDK Downloads</td><td>%</td><td>6/9/26</td><td>Week</td><td>WoW Δ in 7d Avg</td><td>▼-59.7</td><td>-1.2</td><td>+58.5</td><td>+3.8</td><td>-15.7</td><td>+26.3</td><td>+6.4</td><td></td></tr><tr><td colspan="13">App Usage (Sensor Tower)</td></tr><tr><td>Gemini App WAU</td><td>%</td><td>6/8/26</td><td>Week</td><td>WoW Δ</td><td>▼-3.3</td><td>-0.1</td><td>+3.2</td><td>+0.1</td><td>+3.1</td><td>+1.3</td><td>+0.6</td><td></td></tr><tr><td>Qwen App WAU</td><td>%</td><td>6/8/26</td><td>Week</td><td>WoW Δ</td><td>▲+0.3</td><td>+0.6</td><td>+0.3</td><td>-1.5</td><td>+4.9</td><td>-3.0</td><td>-1.1</td><td></td></tr><tr><td>Kimi App WAU</td><td>%</td><td>6/8/26</td><td>Week</td><td>WoW Δ</td><td>▲+0.2</td><td>-0.3</td><td>-0.5</td><td>-0.7</td><td>-0.2</td><td>+0.4</td><td>+0.1</td><td></td></tr><tr><td colspan="13">Web Usage (Similarweb)</td></tr><tr><td>Gemini Web Visits</td><td>%</td><td>5/30/26</td><td>Week</td><td>WoW Δ in 7d Avg</td><td>▼-4.1</td><td>-2.1</td><td>+2.0</td><td>+0.8</td><td>+1.6</td><td>-2.1</td><td>+0.5</td><td></td></tr><tr><td>Qwen Web Visits</td><td>%</td><td>5/30/26</td><td>Week</td><td>WoW Δ in 7d Avg</td><td>▲+9.8</td><td>+9.1</td><td>-0.7</td><td>+9.8</td><td>-4.3</td><td>-6.2</td><td>+0.6</td><td></td></tr><tr><td>Kimi Web Visits</td><td>%</td><td>5/30/26</td><td>Week</td><td>WoW Δ in 7d Avg</td><td>▼-3.3</td><td>-5.2</td><td>-1.9</td><td>+5.9</td><td>-0.7</td><td>-7.1</td><td>+14.0</td><td></td></tr><tr><td colspan="13">Layoffs (WSJ)</td></tr><tr><td>All Layoffs Announced</td><td>People</td><td>6/8/26</td><td>Month</td><td>MTD</td><td>▼-90.8%</td><td>1,690</td><td>18,360</td><td>11,645</td><td>35,100</td><td>12,900</td><td>55,375</td><td></td></tr><tr><td>AI-Driven Layoffs Announced</td><td>People</td><td>6/2/26</td><td>Month</td><td>MTD</td><td>▼-95.4%</td><td>350</td><td>7,560</td><td>10,400</td><td>31,600</td><td>4,000</td><td>51,975</td><td></td></tr></table>

Proprietary and Open Models (Artificial Analysis)

<table><tr><td>Highest Intelligence for Proprietary Models</td><td>Points</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+4.9%</td><td>64</td><td>61</td><td>60</td><td>60</td><td>60</td><td>60</td></tr><tr><td>Highest Intelligence for Open Models</td><td>Points</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+1.9%</td><td>55</td><td>54</td><td>54</td><td>54</td><td>54</td><td>54</td></tr><tr><td>Gap in Proprietary and Open Intelligence</td><td>Points</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+28.6%</td><td>9</td><td>7</td><td>6</td><td>6</td><td>6</td><td>6</td></tr></table>

Highest Intelligence Models from the Top-20 Providers (Artificial Analysis)

<table><tr><td>Median Intelligence</td><td>Points</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+9.5%</td><td>46</td><td>42</td><td>38</td><td>38</td><td>38</td><td>38</td></tr><tr><td>Median Latency</td><td>Sec</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▼-7.0%</td><td>2.25</td><td>2.42</td><td>2.20</td><td>2.52</td><td>2.37</td><td>2.16</td></tr><tr><td>Median Speed</td><td>Tok/Sec</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲+5.0%</td><td>105</td><td>100</td><td>96</td><td>67</td><td>66</td><td>64</td></tr></table>

GPU Index Pricing (Bloomberg)

<table><tr><td>A100</td><td>$/Hour</td><td>6/10/26</td><td>Week</td><td>7d Avg</td><td>▲+0.6%</td><td>1.63</td><td>1.62</td><td>1.57</td><td>1.53</td><td>1.50</td><td>1.47</td><td></td></tr><tr><td>H100/H200</td><td>$/Hour</td><td>6/10/26</td><td>Week</td><td>7d Avg</td><td>▼-0.8%</td><td>2.64</td><td>2.66</td><td>2.61</td><td>2.89</td><td>2.71</td><td>2.50</td><td></td></tr><tr><td>(G)B200/(G)B300</td><td>$/Hour</td><td>6/10/26</td><td>Week</td><td>7d Avg</td><td>▲+0.8%</td><td>4.82</td><td>4.78</td><td>4.67</td><td>4.66</td><td>4.54</td><td>4.31</td><td></td></tr></table>

Model Pricing for Output Tokens (Artificial Analysis)

<table><tr><td>US+EU Avg</td><td>$/1M Tok</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>▲ +28.4%</td><td>14.17</td><td>11.04</td><td>11.04</td><td>11.04</td><td>11.00</td><td>11.00</td></tr><tr><td>China Avg</td><td>$/1M Tok</td><td>6/11/26</td><td>Week</td><td>7d Avg</td><td>— 0.0%</td><td>5.11</td><td>5.11</td><td>5.11</td><td>5.11</td><td>5.21</td><td>5.21</td></tr><tr><td>Frontier Avg</td><td>$/1M Tok

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
